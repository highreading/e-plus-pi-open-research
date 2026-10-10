#include <array>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>

using i64 = std::int64_t;
using u64 = std::uint64_t;

constexpr int P = 29;
constexpr int P2 = 841;
constexpr int P3 = 24389;
constexpr int L = 707281;
constexpr int BSTAR = 687936;
constexpr int QMIN = -60;
constexpr int QMAX = 30;
constexpr int NQ = 91;
constexpr int CARRY_SCALE = 25260;

[[noreturn]] void fail(const std::string& s) {
    std::cerr << "FAIL: " << s << "\n";
    std::exit(1);
}

void require(bool b, const std::string& s) {
    if (!b) fail(s);
}

int mod(i64 a, int m) {
    int r = int(a % m);
    return r < 0 ? r + m : r;
}

int inverse(int a, int m) {
    i64 old_r = a, r = m;
    i64 old_s = 1, s = 0;
    while (r != 0) {
        i64 q = old_r / r;
        i64 nr = old_r - q*r;
        old_r = r; r = nr;
        i64 ns = old_s - q*s;
        old_s = s; s = ns;
    }
    require(old_r == 1, "nonunit passed to inverse");
    return mod(old_s, m);
}

struct Half {
    int fact, invfact;
    int lo, hi;
    int eh;
};

struct Record {
    int fact, invfact;
    int g, eh, htop;
};

struct Slot {
    int z = 0;  // constant residue modulo p^2
    int d = 0;  // D harmonic residue modulo p
    int j = 0;  // J harmonic residue modulo p
};

std::array<int, P> harm;
std::array<Half, P2> half_table;
std::array<int, 9> wilson_power;
u64 normalization_counts[2][3] = {};

Record record4(int t) {
    require(0 <= t && t < L, "four-digit argument out of range");
    int lo = t % P2;
    int hi = t / P2;
    const Half& a = half_table[lo];
    const Half& b = half_table[hi];

    Record R;
    R.fact = int(i64(a.fact)*b.fact % P2);
    R.invfact = int(i64(a.invfact)*b.invfact % P2);
    R.g = a.hi + (P+1)*hi + b.hi;
    R.eh = mod(a.eh + b.eh + b.lo*harm[a.hi], P);
    R.htop = harm[b.hi];
    return R;
}

int normalize_raw(
    int coeff, int carry, int base, int available_precision, int column
) {
    // coeff is a nonnegative representative modulo p^available_precision.
    require(available_precision + carry >= base + 2,
            "insufficient raw precision for normalized residue");

    int division_exponent = carry < base ? base-carry : 0;
    require(division_exponent <= 2, "unexpected division depth");
    ++normalization_counts[column][division_exponent];

    if (carry >= base+2) return 0;

    if (carry >= base) {
        int z = coeff % P2;
        if (carry == base+1) z = z*P % P2;
        return z;
    }

    int divisor = division_exponent == 1 ? P : P2;
    require(coeff % divisor == 0, "raw coefficient not exactly divisible");
    return (coeff/divisor) % P2;
}

void insert_slot(
    Slot& s, int z, int unit, int lambda0, int lambdaD, int lambdaJ
) {
    if (z == 0) return;

    int zu = int(i64(z)*unit % P2);
    int constant = int(i64(zu)*(1 + P*lambda0) % P2);
    s.z += constant;
    if (s.z >= P2) s.z -= P2;

    int zu1 = (z % P)*(unit % P) % P;
    s.d = (s.d + zu1*lambdaD) % P;
    s.j = (s.j + zu1*lambdaJ) % P;
}

int main(int argc, char** argv) {
    if (argc != 3) {
        std::cerr << "Usage: pass29 cache29.txt table29.json\n";
        return 2;
    }

    std::ifstream in(argv[1]);
    require(bool(in), "cannot open input cache");

    std::string magic, receipt_sha;
    in >> magic >> receipt_sha;
    require(magic == "A2GAMMA0v1", "wrong cache format");

    std::array<int, 61> E;
    for (int& z : E) {
        in >> z;
        require(bool(in) && 0 <= z && z < L, "bad boundary coefficient");
    }
    require(E[60] == 0, "E_60 must be zero");
    require(E[0] % P == 2 && E[1] % P == 1,
            "wrong leading boundary");
    require((E[2]+E[1]) % P != 0,
            "q=-2 slope unexpectedly not a unit");

    static int acache[P2][31];
    static int qcache[P2][31];
    for (int x = 0; x < P2; ++x) {
        for (int q = 0; q <= 30; ++q) {
            in >> acache[x][q];
            require(bool(in) && 0 <= acache[x][q] &&
                    acache[x][q] < P2, "bad A cache entry");
        }
        for (int q = 0; q <= 30; ++q) {
            in >> qcache[x][q];
            require(bool(in) && 0 <= qcache[x][q] &&
                    qcache[x][q] < P3, "bad Q cache entry");
        }
    }
    std::string extra;
    require(!(in >> extra), "extra input after cache");

    std::array<int, P> factorial, invfactorial;
    factorial[0] = 1;
    harm[0] = 0;
    for (int i = 1; i < P; ++i) {
        factorial[i] = factorial[i-1]*i % P2;
        harm[i] = (harm[i-1] + inverse(i,P)) % P;
    }
    for (int i = 0; i < P; ++i)
        invfactorial[i] = inverse(factorial[i], P2);

    for (int z = 0; z < P2; ++z) {
        int lo = z % P, hi = z / P;
        half_table[z] = {
            factorial[lo]*factorial[hi] % P2,
            invfactorial[lo]*invfactorial[hi] % P2,
            lo, hi, hi*harm[lo] % P
        };
    }

    wilson_power[0] = 1;
    for (int c = 1; c <= 8; ++c)
        wilson_power[c] =
            wilson_power[c-1]*factorial[28] % P2;

    const Record Wtop = record4(191112);

    // Fixed B_bot2 records.
    std::array<Record, NQ> Bbot2;
    for (int qi = 0; qi < NQ; ++qi)
        Bbot2[qi] = record4(382219 + QMIN + qi);

    // Sliding window for B_bot1, initially at x=0.
    std::array<Record, NQ> ring;
    int head = 0;
    for (int qi = 0; qi < NQ; ++qi)
        ring[qi] = record4(BSTAR - (QMIN + qi));

    // Complete affine raw boundary state modulo p^4.
    std::array<int, 61> boundary = E;
    std::array<int, 61> slope;
    for (int k = 0; k <= 60; ++k)
        slope[k] = (E[k] + (k ? E[k-1] : 0)) % L;

    int T0[3][3] = {};
    int TD[3][3] = {};
    int TJ[3][3] = {};

    u64 carry_histogram[NQ][9] = {};
    u64 r_one_counts[NQ] = {};
    u64 shape_counts[3] = {};
    u64 support_size = 0;
    int support_kappa[3] = {};
    int support_g[3] = {};

    const int inv6_p2 = inverse(6, P2);
    const int inv6_p = inverse(6, P);

    for (int x = 0; x < L; ++x) {
        int e = x > 191112;
        int raw_top = 382219 + BSTAR - x;
        int u = raw_top >= L;
        int shape = (e == 0) ? 0 : (u == 1 ? 1 : 2);
        ++shape_counts[shape];

        int vlow = BSTAR - x;
        int wb2low = 191112 - x + L*e;
        int btoplow = raw_top - L*u;

        Record Wbot1 = record4(x);
        Record Wbot2 = record4(wb2low);
        Record Btop = record4(btoplow);

        int carry_base =
            CARRY_SCALE*(e+u) + Wtop.g + Btop.g
            - Wbot1.g - Wbot2.g;

        int unit_base = Wtop.fact;
        unit_base = int(i64(unit_base)*Btop.fact % P2);
        unit_base = int(i64(unit_base)*Wbot1.invfact % P2);
        unit_base = int(i64(unit_base)*Wbot2.invfact % P2);

        int harmonic_base =
            Wtop.eh + Btop.eh - Wbot1.eh - Wbot2.eh
            + 3*Wtop.htop - (3-e)*Wbot2.htop
            + (6+u)*Btop.htop;

        int lambdaJ_base =
            -Wbot1.htop + Wbot2.htop - Btop.htop;

        std::array<Slot,2> A{};
        std::array<Slot,2> Q{};
        int cache_x = x % P2;

        for (int qi = 0; qi < NQ; ++qi) {
            int q = QMIN + qi;
            int ring_index = head + qi;
            if (ring_index >= NQ) ring_index -= NQ;

            const Record& B1 = ring[ring_index];
            const Record& B2 = Bbot2[qi];
            int r = (vlow-q < 0);
            if (r) ++r_one_counts[qi];

            int c = carry_base + CARRY_SCALE*r - B1.g - B2.g;
            require(0 <= c && c <= 8, "invalid low carry count");
            ++carry_histogram[qi][c];

            if (q >= 0)
                require(c >= 2, "positive-power carry bound failed");
            else
                require(c >= 1, "negative-power carry bound failed");
            if (q == 0 || q == -1)
                require(c >= 3, "special unit-boundary carry bound failed");

            int y;
            int q_precision;
            if (q > 0) {
                y = qcache[cache_x][q];
                q_precision = 3;
            } else if (q == 0) {
                y = (qcache[cache_x][0] + boundary[0]) % L;
                q_precision = 3; // contact part is known modulo p^3
            } else {
                y = boundary[-q];
                q_precision = 4;
            }

            int zQ = normalize_raw(y, c, 3, q_precision, 1);
            int zA = 0;
            if (q >= 0)
                zA = normalize_raw(acache[cache_x][q], c, 2, 2, 0);

            if (zA == 0 && zQ == 0) continue;

            int unit = unit_base;
            unit = int(i64(unit)*B1.invfact % P2);
            unit = int(i64(unit)*B2.invfact % P2);
            unit = int(i64(unit)*wilson_power[c] % P2);

            int lambda0 = mod(
                harmonic_base - B1.eh - B2.eh
                + r*B1.htop - 6*B2.htop, P
            );
            int lambdaD = mod(Btop.htop-B1.htop, P);
            int lambdaJ = mod(lambdaJ_base+B1.htop, P);

            insert_slot(A[r], zA, unit, lambda0, lambdaD, lambdaJ);
            insert_slot(Q[r], zQ, unit, lambda0, lambdaD, lambdaJ);
        }

        // Checks of the retained natural leading-column identities.
        require(A[1].z % P == 0, "leading A r=1 slot is nonzero");

        if (x > BSTAR) {
            require(A[0].z == 0 && A[0].d == 0 && A[0].j == 0,
                    "exterior A row lost its h-J factor");
        }

        int a_lead = A[0].z % P;
        if (a_lead != 0) {
            require(shape != 1, "leading support in middle shape");
            require(Q[1].z % P == 0, "leading Q r=1 on A support");
            ++support_size;
            support_kappa[shape] =
                (support_kappa[shape]+a_lead*a_lead) % P;
            support_g[shape] =
                (support_g[shape]+a_lead*(Q[0].z % P)) % P;
        }

        // All four ordered pairs are retained.
        for (int r = 0; r <= 1; ++r) {
            for (int s = 0; s <= 1; ++s) {
                int degree = r+s;

                i64 flat =
                    i64(A[r].z)*Q[s].z
                    - i64(inv6_p2)*A[r].z*A[s].z;
                T0[shape][degree] =
                    mod(T0[shape][degree]+flat, P2);

                int ar = A[r].z % P;
                int as = A[s].z % P;
                int qs = Q[s].z % P;

                i64 hd =
                    i64(ar)*Q[s].d + i64(A[r].d)*qs
                    - i64(inv6_p)*(i64(ar)*A[s].d
                                      + i64(A[r].d)*as);
                i64 hj =
                    i64(ar)*Q[s].j + i64(A[r].j)*qs
                    - i64(inv6_p)*(i64(ar)*A[s].j
                                      + i64(A[r].j)*as);

                TD[shape][degree] = mod(TD[shape][degree]+hd, P);
                TJ[shape][degree] = mod(TJ[shape][degree]+hj, P);
            }
        }

        if (x+1 < L) {
            // Full-modulus affine update, including the q=-2 unit slope.
            for (int k = 0; k <= 60; ++k) {
                boundary[k] += slope[k];
                if (boundary[k] >= L) boundary[k] -= L;
            }

            // Exact shift t(x+1,q)=t(x,q+1).
            ++head;
            if (head == NQ) head = 0;
            int last = head + NQ - 1;
            if (last >= NQ) last -= NQ;

            int new_t = BSTAR - (x+1) - QMAX;
            if (new_t < 0) new_t += L;
            ring[last] = record4(new_t);
        }
    }

    require(shape_counts[0] == 191113 &&
            shape_counts[1] == 171762 &&
            shape_counts[2] == 344406, "wrong shape counts");
    require(support_size == 9108, "wrong leading support size");
    require(support_kappa[0] == 11 && support_kappa[2] == 18,
            "kappa cross-check failed");
    require(support_g[0] == 26 && support_g[2] == 3,
            "mixed leading-constant cross-check failed");

    for (int qi = 0; qi < NQ; ++qi) {
        int q = QMIN + qi;
        require(r_one_counts[qi] == u64(19344+q),
                "wrong r=1 count");
        u64 sum = 0;
        for (int c = 0; c <= 8; ++c) sum += carry_histogram[qi][c];
        require(sum == u64(L), "carry histogram is incomplete");
    }

    for (int s = 0; s < 3; ++s)
        for (int v = 0; v < 3; ++v)
            require(T0[s][v] % P == 0,
                    "one of nine flat constants is not divisible by p");

    u64 countA = 0, countQ = 0;
    for (int k = 0; k <= 2; ++k) {
        countA += normalization_counts[0][k];
        countQ += normalization_counts[1][k];
    }
    require(countA == u64(L)*31, "wrong A normalization count");
    require(countQ == u64(L)*91, "wrong Q normalization count");

    std::ofstream out(argv[2]);
    require(bool(out), "cannot open output file");

    out << "{\n";
    out << "  \"format\": \"A2T27v1\",\n";
    out << "  \"input_receipt_sha256\": \"" << receipt_sha << "\",\n";
    out << "  \"rows_processed\": " << L << ",\n";
    out << "  \"Laurent_records\": " << u64(L)*NQ << ",\n";
    out << "  \"all_normalizations_verified\": true,\n";
    out << "  \"all_flat_divisions_verified\": true,\n";
    out << "  \"support_size\": " << support_size << ",\n";
    out << "  \"shape_counts\": ["
        << shape_counts[0] << "," << shape_counts[1] << ","
        << shape_counts[2] << "],\n";
    out << "  \"normalization_counts_by_division_exponent\": [";
    for (int col = 0; col < 2; ++col) {
        if (col) out << ",";
        out << "[" << normalization_counts[col][0] << ","
            << normalization_counts[col][1] << ","
            << normalization_counts[col][2] << "]";
    }
    out << "],\n";

    out << "  \"table\": [\n";
    int row = 0;
    for (int s = 0; s < 3; ++s) {
        for (int v = 0; v < 3; ++v) {
            out << "    [" << T0[s][v] << ","
                << TD[s][v] << "," << TJ[s][v] << "]";
            out << (++row == 9 ? "\n" : ",\n");
        }
    }
    out << "  ],\n";

    out << "  \"carry_histogram_q_minus60_to30\": [\n";
    for (int qi = 0; qi < NQ; ++qi) {
        out << "    [";
        for (int c = 0; c <= 8; ++c) {
            if (c) out << ",";
            out << carry_histogram[qi][c];
        }
        out << "]" << (qi+1 == NQ ? "\n" : ",\n");
    }
    out << "  ]\n";
    out << "}\n";
    require(bool(out), "output write failed");
    return 0;
}
