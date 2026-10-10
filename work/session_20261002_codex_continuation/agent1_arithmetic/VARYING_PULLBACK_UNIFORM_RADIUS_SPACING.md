> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Varying pullbacks: uniform radius supplies endpoint spacing without shared jets

Status: original author deduction, 2026-10-02; not independently reviewed. This strengthens the domain of the shared-prefix spacing result. It imposes a quantitative denominator constraint, not an irrationality conclusion or an existence theorem for low-denominator pullbacks.

For each index N in a set I of even positive integers, choose a real rational polynomial P_N with P_N(0)=0, P_N(1)=1 and all derivative jets integral. Let G_[N]=F∘P_N be the branch at0 with G_[N](0)=0. Assume each G_[N] is analytic on the common disk |z|<R, R>1, and G_[N](1)=pi. Define

    H_[N]=e^z+G_[N],
    c_N=sum_{j=0}^N H_[N]^(j)(0)/j!=p_N/q_N,
    o_N=odd(q_N), f_N=v_2(N!).

There is no requirement that different P_N share jets, have bounded degree, or have bounded coefficient height.

## 1. Uniform Cauchy constants follow from the common radius

As germs at zero one has the exact identity, with v=exp(iG_[N]/2),

    P_N=2(1-v)/[(1-i)-(1+i)v].                    (1)

Cross-multiplication continues analytically throughout the common disk. If G_[N] equalled -pi+4pi k anywhere, then v=-i, making the denominator zero but the numerator nonzero. A finite polynomial value P_N cannot satisfy that equality. Hence G_[N] omits every value -pi+4pi k, in particular -pi and3pi.

The normalized function W_[N]=(G_[N]+pi)/(4pi) omits0 and1 and satisfies W_[N](0)=1/4. The classical Schottky theorem therefore gives, for every r<R, a finite bound B_(r,R) depending only on r/R and1/4 such that

    sup_N sup_(|z|<=r) |G_[N](z)| <= B_(r,R).

No growth of P_N's coefficients or degree is charged. Including e^z and using Cauchy's estimate gives a constant T_(r,R)>0, independent of N, with

    |S-c_N| <= T_(r,R) r^(-N),  S=e+pi.           (2)

For example one may take T=(e^r+B)/(r-1). No numerical evaluation of the Schottky constant is claimed.

## 2. Exact difference parity also needs no shared jets

Integral-Hurwitz composition makes every G_[N] derivative jet even. Thus Z_N=N!c_N is an odd integer at even N, and the final dyadic denominator is exactly2^f_N. For M<N in I,

    N!c_M=(N!/M!)(M!c_M)

is an even integer, since N!/M! contains the even factor N. Therefore N!(c_N-c_M) is odd and the two rational fractions are distinct, regardless of their different polynomials.

As in the shared-prefix argument, the actual denominator of their difference has dyadic part2^f_N and odd part dividing lcm(o_N,o_M). Hence

    |c_N-c_M| >= 1/[2^f_N lcm(o_N,o_M)].

Using both complete tails (2),

    |c_N-c_M| <= 2T_(r,R) r^(-M),

so the finite inequality is

    log lcm(o_N,o_M)
      >= M log r-N log2+s_2(N)log2
                              -log(2T_(r,R)).     (3)

This is actual endpoint arithmetic after each final gcd. It does not identify c_N-c_M with one common Taylor coefficient block.

## 3. Consequences for cancellation families

If all sufficiently large even N are admitted, M=N-2 in (3) implies

    limsup_(N even) log o_N/N >= (1/2)log(R/2),

whenever R>2. All eventual even q_N cannot be purely dyadic, even for independently chosen polynomials.

More generally, let N_1<N_2<... be any admitted even sequence with log o_(N_j)<=eta N_j+o(N_j). The same bounded-ratio argument as in SHARED_PREFIX_ODD_DENOMINATOR_RADIUS.md gives

    liminf_j N_(j+1)/N_j
       >= (log R-eta)/(log2+eta),                 (4)

provided log R>eta. Subexponential odd-part indices therefore satisfy a ratio lower bound log R/log2. Pure dyadic cancellation is compatible only with sufficiently sparse index sets under these hypotheses.

The all-index one-jet construction in SINGLE_JET_ACTUAL_DENOMINATOR_CANCELLATION.md retains every fixed radius below2. Equation (3) shows that it cannot be promoted to an all-even-index family with one common radius>2 by a different choice of high polynomial coefficients. Sparse indices and families with positive exponential odd-denominator cost remain outside that exclusion.

If infinitely many pure dyadic admitted indices with a common R>2 could be constructed, (2) would yield |q_N S-p_N|<=T(2/r)^N→0 for2<r<R. Parity makes those forms eventually nonzero under every rationality hypothesis S=a/b, because f_N eventually exceeds v_2(b). Such an infinite construction would consequently prove irrationality of S. This note does not establish that construction; it states the arithmetic/analytic gateway and its index-spacing constraint explicitly.

## 4. Primary and archive gate

Archive query before this target searched Schottky, normal families, local boundedness, uniform pullbacks, geometric dyadic denominators and denominator lacunarity over sources and the canonical work sessions. The matches concern old HP normal-family limits and restricted selector approximations, not uniform pullback endpoint spacing. Root's recent analytic existence theorem already uses normalized cover compactness; this author deduction concerns its missing evaluated-denominator interface.

Current primary queries: `"Schottky" "omit" "two" "values" normal family theorem 2025`; `"Landau" "Schottky" "theorem" "arxiv"`; `"omit two values" "bounded" holomorphic Schottky`. Opened the2026 primary paper by Bharathi Thiruvengadam and Jaikrishnan Janardhanan, [Revisiting Kobayashi hyperbolicity on planar domains](https://arxiv.org/html/2604.19095v1), especially Theorem4.2 and its proof. It states the required fixed-center uniform bound on compact subdisks. Also opened P. V. Dovbush, [Applications of Zalcman's lemma](https://arxiv.org/pdf/1907.00925), Theorem1.3, as a second primary formulation. Neither full paper is independently audited here; the classical theorem is used with its displayed hypotheses. The novelty boundary is the fixed omitted lattice of the pullback G, the automatic uniform tail constant, and the independent-family parity/denominator spacing. The Schottky theorem itself is standard.
