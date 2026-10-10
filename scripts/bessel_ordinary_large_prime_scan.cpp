#include <algorithm>
#include <atomic>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <mutex>
#include <sstream>
#include <stdexcept>
#include <string>
#include <sys/resource.h>
#include <tuple>
#include <vector>

#include <omp.h>

using u64 = std::uint64_t;
using u128 = unsigned __int128;

struct SquareRecord {
    int prime;
    int index;
    int valuation_at_least;
    u64 unit_mod_prime;
};

struct ScanResult {
    int lower;
    int upper;
    long long prime_count;
    long long root_orbits;
    long long ordinary_orbits;
    long long singular_orbits;
    long long divisible_values;
    long long square_values;
    long long cube_values;
    std::vector<SquareRecord> squares;
};

static u64 mul_add_mod(u64 coefficient, u64 value, u64 addend, u64 modulus) {
    return static_cast<u64>(((u128)coefficient * value + addend) % modulus);
}

static std::vector<int> primes_below(int upper) {
    std::vector<bool> is_prime(upper, true);
    if (upper > 0) is_prime[0] = false;
    if (upper > 1) is_prime[1] = false;
    for (int candidate = 2; (long long)candidate * candidate < upper; ++candidate) {
        if (!is_prime[candidate]) continue;
        for (int multiple = candidate * candidate; multiple < upper; multiple += candidate) {
            is_prime[multiple] = false;
        }
    }
    std::vector<int> primes;
    for (int value = 5; value < upper; ++value) {
        if (is_prime[value]) primes.push_back(value);
    }
    return primes;
}

static ScanResult scan_range(
    int lower, int upper, const std::vector<int>& all_primes
) {
    std::vector<int> primes;
    for (int prime : all_primes) {
        if (lower <= prime && prime < upper) primes.push_back(prime);
    }

    std::atomic<long long> root_orbits{0};
    std::atomic<long long> ordinary_orbits{0};
    std::atomic<long long> singular_orbits{0};
    std::atomic<long long> divisible_values{0};
    std::atomic<long long> square_values{0};
    std::atomic<long long> cube_values{0};
    std::mutex square_mutex;
    std::vector<SquareRecord> squares;

    #pragma omp parallel for schedule(dynamic, 4)
    for (std::size_t prime_index = 0; prime_index < primes.size(); ++prime_index) {
        const u64 prime = static_cast<u64>(primes[prime_index]);
        const u64 prime_square = prime * prime;
        const u64 modulus = prime_square * prime;
        std::vector<u64> q(2 * prime);
        q[0] = 1;
        q[1] = 1;
        for (u64 n = 2; n < 2 * prime; ++n) {
            q[n] = mul_add_mod(4 * n - 2, q[n - 1], q[n - 2], modulus);
        }

        long long local_divisible = 0;
        long long local_square = 0;
        long long local_cube = 0;
        std::vector<SquareRecord> local_squares;
        for (u64 n = 0; n < 2 * prime; ++n) {
            if (q[n] % prime != 0) continue;
            ++local_divisible;
            if (q[n] % prime_square != 0) continue;
            ++local_square;
            const bool cube = q[n] == 0;
            if (cube) ++local_cube;
            local_squares.push_back(
                {
                    static_cast<int>(prime),
                    static_cast<int>(n),
                    cube ? 3 : 2,
                    (q[n] / prime_square) % prime,
                }
            );
        }

        long long local_roots = 0;
        long long local_ordinary = 0;
        long long local_singular = 0;
        for (u64 root = 0; root <= (prime - 1) / 2; ++root) {
            if (q[root] % prime != 0) continue;
            ++local_roots;
            const u64 c = (q[root] / prime) % prime;
            const u64 translated = (q[root + prime] / prime) % prime;
            const u64 delta = (prime - ((c + translated) % prime)) % prime;
            if (delta == 0) ++local_singular;
            else ++local_ordinary;
        }

        divisible_values += local_divisible;
        square_values += local_square;
        cube_values += local_cube;
        root_orbits += local_roots;
        ordinary_orbits += local_ordinary;
        singular_orbits += local_singular;
        if (!local_squares.empty()) {
            std::lock_guard<std::mutex> guard(square_mutex);
            squares.insert(squares.end(), local_squares.begin(), local_squares.end());
        }
    }

    std::sort(
        squares.begin(), squares.end(),
        [](const SquareRecord& left, const SquareRecord& right) {
            return std::tie(left.prime, left.index)
                < std::tie(right.prime, right.index);
        }
    );
    return {
        lower,
        upper,
        static_cast<long long>(primes.size()),
        root_orbits.load(),
        ordinary_orbits.load(),
        singular_orbits.load(),
        divisible_values.load(),
        square_values.load(),
        cube_values.load(),
        squares,
    };
}

int main(int argc, char** argv) {
    const auto started = std::chrono::steady_clock::now();
    std::vector<std::pair<int, int>> ranges;
    if (argc == 1) {
        ranges = {{10000, 50000}, {50000, 200000}, {200000, 500000}};
    } else if (argc == 3) {
        ranges = {{std::stoi(argv[1]), std::stoi(argv[2])}};
    } else {
        throw std::invalid_argument("usage: scanner [LOWER UPPER]");
    }
    int maximum_upper = 0;
    for (const auto& range : ranges) {
        if (range.first < 5 || range.first >= range.second) {
            throw std::invalid_argument("invalid scan range");
        }
        maximum_upper = std::max(maximum_upper, range.second);
    }
    if (maximum_upper > 2000000) {
        throw std::invalid_argument("upper bound exceeds the uint64 p^3 guard");
    }
    const std::size_t estimated_worker_bytes =
        static_cast<std::size_t>(omp_get_max_threads())
        * 2ULL * static_cast<std::size_t>(maximum_upper) * sizeof(u64);
    if (estimated_worker_bytes > (2ULL << 30)) {
        throw std::runtime_error("per-worker array RAM guard exceeded");
    }

    const std::vector<int> primes = primes_below(maximum_upper);
    std::vector<ScanResult> results;
    for (const auto& range : ranges) {
        results.push_back(scan_range(range.first, range.second, primes));
    }

    std::cout << "{\n";
    std::cout << "  \"description\": \"Finite exact mod-p^3 Bessel window scan; diagnostic only.\",\n";
    std::cout << "  \"maximum_upper_exclusive\": " << maximum_upper << ",\n";
    std::cout << "  \"omp_threads\": " << omp_get_max_threads() << ",\n";
    std::cout << "  \"estimated_worker_array_bytes\": " << estimated_worker_bytes << ",\n";
    std::cout << "  \"ranges\": [\n";
    for (std::size_t i = 0; i < results.size(); ++i) {
        const auto& result = results[i];
        std::cout << "    {\n";
        std::cout << "      \"lower_inclusive\": " << result.lower << ",\n";
        std::cout << "      \"upper_exclusive\": " << result.upper << ",\n";
        std::cout << "      \"prime_count\": " << result.prime_count << ",\n";
        std::cout << "      \"root_orbits\": " << result.root_orbits << ",\n";
        std::cout << "      \"ordinary_orbits\": " << result.ordinary_orbits << ",\n";
        std::cout << "      \"singular_orbits\": " << result.singular_orbits << ",\n";
        std::cout << "      \"divisible_values\": " << result.divisible_values << ",\n";
        std::cout << "      \"square_values\": " << result.square_values << ",\n";
        std::cout << "      \"cube_values\": " << result.cube_values << ",\n";
        std::cout << "      \"squares\": [";
        if (!result.squares.empty()) std::cout << "\n";
        for (std::size_t j = 0; j < result.squares.size(); ++j) {
            const auto& square = result.squares[j];
            std::cout << "        {\"prime\": " << square.prime
                      << ", \"index\": " << square.index
                      << ", \"valuation_at_least\": " << square.valuation_at_least
                      << ", \"q_over_p2_mod_p\": " << square.unit_mod_prime << "}";
            if (j + 1 != result.squares.size()) std::cout << ",";
            std::cout << "\n";
        }
        if (!result.squares.empty()) std::cout << "      ";
        std::cout << "]\n";
        std::cout << "    }";
        if (i + 1 != results.size()) std::cout << ",";
        std::cout << "\n";
    }
    std::cout << "  ],\n";
    std::cout << "  \"scope_warning\": \"All scan claims are finite diagnostics, not universal valuation bounds.\"\n";
    std::cout << "}\n";

    const auto finished = std::chrono::steady_clock::now();
    const double elapsed = std::chrono::duration<double>(finished - started).count();
    struct rusage usage {};
    getrusage(RUSAGE_SELF, &usage);
    std::cerr << "live_metrics: elapsed_seconds=" << elapsed
              << ", peak_rss_mib=" << usage.ru_maxrss / 1024.0 << "\n";
    return 0;
}
