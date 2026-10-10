// Exact finite certificate for first prime-square branching of the Bessel
// denominator q_0=q_1=1, q_n=(4n-2)q_{n-1}+q_{n-2}.
//
// This is a diagnostic, not an all-prime proof.  It scans every root modulo
// every odd prime through --prime-limit, computes the two values needed for
// the affine anti-period lift modulo p^2, and records all singular and fully
// branching roots.  Arithmetic uses exact unsigned integers modulo p^2.

#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using u64 = std::uint64_t;
using u128 = __uint128_t;

struct RootRecord {
  int prime;
  int root;
  u64 base;
  u64 shifted;
  int delta;
  bool central;
};

static std::vector<int> primes_up_to(int limit) {
  std::vector<bool> is_prime(limit + 1, true);
  if (limit >= 0) is_prime[0] = false;
  if (limit >= 1) is_prime[1] = false;
  for (int p = 2; static_cast<long long>(p) * p <= limit; ++p) {
    if (!is_prime[p]) continue;
    for (int multiple = p * p; multiple <= limit; multiple += p)
      is_prime[multiple] = false;
  }
  std::vector<int> answer;
  for (int p = 3; p <= limit; p += 2)
    if (is_prime[p]) answer.push_back(p);
  return answer;
}

static u64 step(int n, u64 q_nm2, u64 q_nm1, u64 modulus) {
  const u64 coefficient = static_cast<u64>(4LL * n - 2);
  return static_cast<u64>((static_cast<u128>(coefficient) * q_nm1 + q_nm2)
                          % modulus);
}

static u64 inverse_mod(u64 value, u64 modulus) {
  // Every use has value < p and modulus p^2, hence gcd(value,modulus)=1.
  std::int64_t old_r = static_cast<std::int64_t>(value);
  std::int64_t r = static_cast<std::int64_t>(modulus);
  std::int64_t old_s = 1, s = 0;
  while (r != 0) {
    const std::int64_t quotient = old_r / r;
    const std::int64_t next_r = old_r - quotient * r;
    old_r = r;
    r = next_r;
    const std::int64_t next_s = old_s - quotient * s;
    old_s = s;
    s = next_s;
  }
  std::int64_t result = old_s % static_cast<std::int64_t>(modulus);
  if (result < 0) result += static_cast<std::int64_t>(modulus);
  return static_cast<u64>(result);
}

static u64 central_hypergeometric(int prime) {
  // H_p=sum_{j=0}^{(p-1)/2} (1/2)_j^2/j! modulo p^2.  The update is
  // t_j/t_{j-1}=(2j-1)^2/(4j), whose denominator is a unit modulo p^2.
  const int middle = (prime - 1) / 2;
  const u64 modulus = static_cast<u64>(prime) * prime;
  u64 term = 1;
  u64 total = 1;
  for (int j = 1; j <= middle; ++j) {
    const u64 odd = static_cast<u64>(2 * j - 1);
    const u64 numerator = (odd * odd) % modulus;
    const u64 denominator = static_cast<u64>(4 * j);
    term = static_cast<u64>((static_cast<u128>(term) * numerator) % modulus);
    term = static_cast<u64>((static_cast<u128>(term)
                             * inverse_mod(denominator, modulus)) % modulus);
    total += term;
    if (total >= modulus) total -= modulus;
  }
  return total;
}

static void write_record(std::ostream &out, const RootRecord &record,
                         const std::string &indent) {
  out << indent << "{\"p\": " << record.prime
      << ", \"r\": " << record.root
      << ", \"q_r_mod_p2\": " << record.base
      << ", \"q_r_plus_p_mod_p2\": " << record.shifted
      << ", \"delta_mod_p\": " << record.delta
      << ", \"central\": " << (record.central ? "true" : "false") << "}";
}

int main(int argc, char **argv) {
  int prime_limit = 200000;
  std::string output_path =
      "results/bessel_denominator_all_lift_branching_certificate.json";
  for (int index = 1; index < argc; ++index) {
    const std::string argument = argv[index];
    if (argument == "--prime-limit" && index + 1 < argc) {
      prime_limit = std::atoi(argv[++index]);
    } else if (argument == "--output" && index + 1 < argc) {
      output_path = argv[++index];
    } else {
      std::cerr << "usage: " << argv[0]
                << " [--prime-limit N] [--output PATH]\n";
      return 2;
    }
  }
  if (prime_limit < 3 || prime_limit > 1000000) {
    std::cerr << "prime limit must lie in [3,1000000]\n";
    return 2;
  }

  const std::vector<int> primes = primes_up_to(prime_limit);
  std::uint64_t total_roots = 0;
  std::uint64_t primes_with_roots = 0;
  std::uint64_t representatives_divisible_by_p2 = 0;
  std::vector<RootRecord> singular;
  std::vector<RootRecord> all_branching;
  std::vector<RootRecord> central_roots;
  std::vector<RootRecord> square_divisible_representatives;

  for (const int p : primes) {
    const u64 modulus = static_cast<u64>(p) * p;
    std::vector<u64> first(p);
    first[0] = 1;
    first[1] = 1;
    u64 q_nm2 = 1, q_nm1 = 1;
    std::vector<int> roots;
    for (int n = 2; n < p; ++n) {
      const u64 q_n = step(n, q_nm2, q_nm1, modulus);
      q_nm2 = q_nm1;
      q_nm1 = q_n;
      first[n] = q_n;
      if (q_n % p == 0) roots.push_back(n);
    }
    if (roots.empty()) continue;
    ++primes_with_roots;
    total_roots += roots.size();
    for (const int r : roots)
      if (first[r] == 0) ++representatives_divisible_by_p2;

    // Continue only rooted primes through index 2p-1.  At index r+p this
    // supplies the second value in the affine lift law.
    std::size_t root_cursor = 0;
    for (int n = p; n < 2 * p; ++n) {
      const u64 q_n = step(n, q_nm2, q_nm1, modulus);
      q_nm2 = q_nm1;
      q_nm1 = q_n;
      const int r = n - p;
      if (root_cursor >= roots.size() || roots[root_cursor] != r) continue;
      ++root_cursor;
      const u64 base = first[r];
      const u64 sum = (base + q_n) % modulus;
      const u64 negative_sum = (modulus - sum) % modulus;
      if (negative_sum % p != 0) {
        std::cerr << "anti-period divisibility failure at p=" << p
                  << ", r=" << r << "\n";
        return 1;
      }
      const int delta = static_cast<int>((negative_sum / p) % p);
      const RootRecord record{p, r, base, q_n, delta,
                              r == (p - 1) / 2};
      if (record.central) {
        central_roots.push_back(record);
        if (delta != 0) {
          std::cerr << "central reflection/slope failure at p=" << p << "\n";
          return 1;
        }
        const u64 hyper = central_hypergeometric(p);
        const u64 predicted = ((p - 1) / 2) % 2 == 0
                                  ? hyper
                                  : (modulus - hyper) % modulus;
        if (predicted != base) {
          std::cerr << "central hypergeometric failure at p=" << p << "\n";
          return 1;
        }
      }
      if (base == 0) square_divisible_representatives.push_back(record);
      if (delta == 0) singular.push_back(record);
      if (delta == 0 && base == 0) {
        if (q_n != 0) {
          std::cerr << "all-branch consistency failure at p=" << p
                    << ", r=" << r << "\n";
          return 1;
        }
        all_branching.push_back(record);
      }
    }
    if (root_cursor != roots.size()) {
      std::cerr << "root cursor failure at p=" << p << "\n";
      return 1;
    }
  }

  std::ofstream out(output_path);
  if (!out) {
    std::cerr << "cannot open output path: " << output_path << "\n";
    return 2;
  }
  out << "{\n";
  out << "  \"description\": \"Exact exhaustive first-lift scan; finite evidence only\",\n";
  out << "  \"prime_limit\": " << prime_limit << ",\n";
  out << "  \"odd_primes_scanned\": " << primes.size() << ",\n";
  out << "  \"primes_with_roots\": " << primes_with_roots << ",\n";
  out << "  \"total_roots_mod_p\": " << total_roots << ",\n";
  out << "  \"root_representatives_divisible_by_p_squared\": "
      << representatives_divisible_by_p2 << ",\n";
  out << "  \"singular_roots\": [\n";
  for (std::size_t i = 0; i < singular.size(); ++i) {
    write_record(out, singular[i], "    ");
    out << (i + 1 == singular.size() ? "\n" : ",\n");
  }
  out << "  ],\n";
  out << "  \"central_roots\": [\n";
  for (std::size_t i = 0; i < central_roots.size(); ++i) {
    write_record(out, central_roots[i], "    ");
    out << (i + 1 == central_roots.size() ? "\n" : ",\n");
  }
  out << "  ],\n";
  out << "  \"root_representatives_divisible_by_p_squared_records\": [\n";
  for (std::size_t i = 0; i < square_divisible_representatives.size(); ++i) {
    write_record(out, square_divisible_representatives[i], "    ");
    out << (i + 1 == square_divisible_representatives.size() ? "\n" : ",\n");
  }
  out << "  ],\n";
  out << "  \"all_p_lift_roots\": [\n";
  for (std::size_t i = 0; i < all_branching.size(); ++i) {
    write_record(out, all_branching[i], "    ");
    out << (i + 1 == all_branching.size() ? "\n" : ",\n");
  }
  out << "  ]\n";
  out << "}\n";
  return 0;
}
