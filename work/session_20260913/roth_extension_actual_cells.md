> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Roth extension to the actual ordinary j=1 cell

2026-09-13. Status: rigorous auxiliary extension, using the explicitly identified archived all-index gauge and recurrence theorems. It proves an averaged support estimate. It does not prove a divisor lower bound or decide e+pi. The large Item243 rational interpolation and Newton computations are imported archived proof dependencies; their complete arithmetic was not recomputed in this bounded pass.

## 1. Result

For the actual ordinary j=1 cell, let W_1(M) be the sum of log p over primes whose two divided common-log coordinates vanish at construction index M. Then

    sum_(X<M<=2X) W_1(M)=o(X^2).

More precisely, the full necessary residual gate at each fixed prime has

    Z_1(p) << p exp(-c(log log p)^(1/9))

for some c>0 and all sufficiently large primes, using the quantitative theorem imported in `fixed_prime_roth_density.md`. Consequently the normalized dyadic average of W_1(M)/(6M) is zero, and W_1(M)=o(M) on a density-one set of indices. The former raw radical-support ceiling1/36 is therefore replaced by zero in this averaged sense. No pointwise replacement at every M is proved.

The comparison left OPEN in Item237 was subsequently proved by Item243. No extrapolation of Item237's finite comparisons, and no promotion of a quadratic norm to an equivalent collision condition, is needed here.

## 2. Exact chain from the actual collision to the algebraic coefficient

The relevant chain is Item218 -> Item222 -> Item243, with the unit audit made explicit in Items229/280/288 and summarized in Item293.

* Item218, Sections1-4, gives the complete actual parameterization

      p=4h+6s+3, h,s>=1, 3 does not divide h,
      M=3h+4s+2.

  Its two actual divided common-log coordinates vanish if and only if the two rational tails Q_0,Q_1 vanish modulo p. Eliminating their factorial prefactors proves the necessary condition E_h(s)=0 modulo p. Every tail denominator is a p-unit.

* Item222, Sections2-4, specializes s to s*=-(4h+3)/6 modulo p. It gives the exact rational value

      E_h*= h x v/(4h+3) + 9(4h+1)u y/[2(4h+3)]

  and an integer clearing whose every denominator factor has absolute value <=4h+3<p. Thus every actual collision implies E_h*=0 modulo p.

* Item237 proves c_h*=[x^(2h)]C(x) and its all-h step-three recurrence. Its comparison c_h*=R_h E_h* was only finite at that point. **Item243 is the subsequent missing proof.** It proves an actual-family order-six recurrence for the defect of the proposed gauged E recurrence. The proof uses exact Gosper identities and endpoint checks, a cleared degree bound2240 with2241 exact regular interpolation points, and a degree1806 forward cofactor with nonpositive Newton coefficients and strictly negative coefficient at index0. Twelve exact defect initials propagate the recurrence, after which six separate gauge initials and Item237's positive leading coefficient prove

      c_h*=R_h E_h* for every h>=1 with 3 not dividing h.

  This is an actual-family proof, not the false assertion that the one-step defect covector vanishes in the whole ambient15-dimensional space.

The gauge is specified by

    R_1=-49/18, R_2=4235/1944,

    R_(h+3)/R_h =
    h(4h+1)(4h+5)(4h+7)(4h+9)(4h+11)(4h+15)^2
    /[864(h+1)(h+2)(2h+1)^2(2h+3)(2h+5)^2(4h+3)].

In the finite product generating R_h, every nonconstant factor has absolute value <=4h+3, and all factors are nonzero. The initial factors and864 have prime support within this same threshold (or at2,3). Hence R_h is a p-unit on every actual row. This independently explains the unit assertion in Item280, Section3, and Item288, equation(1.6).

It follows rigorously that

    actual ordinary j=1 collision
        => E_h*=0 mod p
        <=> c_h*=[x^(2h)]C(x)=0 mod p.                 (A)

Only the first implication is needed for the upper estimate. The converse from a residual zero to a genuine collision is not asserted.

The fixed algebraic series C is Item237's specified Taylor branch, not an arbitrary conjugate. Its parameterization is

    x=y(1+y)/(1+y+y^2/2)^(2/3),
    C(x(y))=N(y)/D(y)^3,
    D(y)=6+14y+7y^2+2y^3,
    N(y)=432+2064y+4440y^2+5376y^3+4044y^4
         +1860y^5+486y^6+48y^7.

## 3. Fixed-prime indexing is compatible with the proved operator

Let p>3 be prime. Choose e=1 when p=1 mod6 and e=2 when p=5 mod6. Put

    s0=(p-4e-3)/6,
    h_n=e+3n, s_n=s0-2n,
    N_p=floor((p-4e+3)/12).

For N_p>0 these give precisely all actual ordinary j=1 rows at p, with0<=n<N_p. Indeed the phase fixes h modulo3; s>=1 gives exactly the displayed bound. In particular N_p=p/12+O(1).

Define u_n=c_(h_n)*. Item237 gives

    sum_(j=0)^3 P_j(h_n)u_(n+j)=0,                   (B)

with exactly the same degree16 polynomials P_j as the ordinary j=2 proof. This time h_n starts at the integers1 or2 rather than the half-integers1/2 or5/2. The recurrence step is still h->h+3.

Every u_n in the actual interval is p-integral. One direct verification is Item237's coefficient formula in h: it involves coefficients of degree at most2h of binomial series with denominators supported in6 and (2h)!, while2h<p on every actual row. Alternatively this follows from the p-unit gauge and Item222's integral localization.

The global construction index is

    M=(2p+e)/3+n.                                     (C)

Thus keeping p fixed and changing n changes M by1 while preserving the characteristic. This is the average over M that the older fixed-M alignment objections did not address.

## 4. Nonzero state and singularity control

Exact initial coefficients are

    c_1*=364/27, c_2*=94490/729.

They were independently recomputed from Item237's Lagrange coefficient formula in this pass. Exclude the finitely many primes dividing their numerators and the fixed rational coefficients in the recurrence/desingularization certificates. Then u_0 is nonzero modulo p in both residue families.

The reverse monic order-four identity in `fixed_prime_stepanov_attempt.md` is a rational-function identity in h, so it applies to (B) without alteration. Its denominator roots are the displayed integers, half-integers and quarter-integers; the largest primitive numerator on an actual row is4h+51. Hence every denominator is a p-unit when s>=9, since p=4h+6s+3>4h+51.

If four consecutive actual u-values vanish, the reverse monic recurrence, applied one index earlier, forces the preceding value to vanish: at that start s is at least9. Repetition contradicts u_0!=0. Therefore no four-zero block exists.

If u_j,u_(j+1),u_(j+2) all vanish, j cannot be0. The preceding value is nonzero by the four-zero exclusion. The original recurrence at j-1 forces P_0(h_j-3)=0 modulo p. Its linear factors are p-units because the start has s>=7 and the largest primitive factor is4h+39. The canonical factorization

    P_0(h)=L_0(h)Q(h+3),
    Q(h)=214443126+369944721h+239554248h^2
         +72513072h^3+10358560h^4+564080h^5

therefore forces Q(h_j)=0. Outside the fixed divisors of564080 this polynomial has at most five roots modulo p. The values h_j=e+3j are distinct modulo p in the actual interval. Thus the zero-three-state count is at most five, exactly as needed by the observation argument.

This argument uses no finite prime scan and no generic nonvanishing assumption. The initial term and the reverse monic identity supply the required actual nonzero-state theorem.

## 5. Apply the observation lemma and sum over M

All remaining inputs in `fixed_prime_roth_density.md` are unchanged: the companion matrix, its limiting nondegenerate cubic, observation numerators J_d, degree48d, coefficient-height estimate, and denominator product of degree32d are properties of the same fixed operator. Their finite-field root bounds require only p>3 and injectivity of h_n, which hold here. The five-zero-state estimate in Section4 replaces its corresponding ordinary j=2 input.

The same proof consequently yields

    Z_1(p):=#{0<=n<N_p: c_(e+3n)*=0 mod p}
       <<p exp(-c(log log p)^(1/9))=o(p).

By (A), this bounds actual simultaneous collisions. By (C), and the equivalent exact actual-prime interval

    (4M+3)/3 <=p<=(3M-1)/2

from Item264, a dyadic interval X<M<=2X uses only p<3X. Therefore

    sum_(X<M<=2X) W_1(M)
      <=sum_(p<3X) Z_1(p)log p=o(X^2).

The last implication uses uniformity of the fixed-prime o(p), then Chebyshev's estimate sum_(p<=Y)p log p=O(Y^2); each fixed prime has only finitely many actual rows. No independence across primes is used. Markov's inequality gives W_1(M)<=epsilon M for all but o(X) indices in each dyadic interval, for every fixed epsilon>0; a diagonal choice gives a density-one set with W_1(M)=o(M).

Item264's former1/36 is the raw radical-support ceiling. The proved change here is its zero **averaged retained support**. There is no pointwise strict-cap theorem for every M, no new positive divisibility rate, and no automatic subtraction from the compatible total-content ceiling.

## 6. Why the other suggested chains are not needed

Item321 supplies genuine all-index factor solutions for the period norm carrier D_(s,epsilon), and its exact Casoratian has strong p-unit control. However the norm is split at every actual prime, and the note explicitly avoids asserting that either specified factor vanishes on the actual orbit merely from common-operator transport. Using its necessary carrier would require a separate factorwise admission and eigenvalue analysis. It is unnecessary once the simpler direct residual bridge (A) is recovered.

Item382's order-three degree19/23 candidates for A_x,A_u are expressly fitting-and-holdout results with no all-index creative-telescoping certificate. Those candidates remain unavailable as theorem inputs. Its fixed-M cross-prime objection remains valid for pointwise propagation but does not obstruct the fixed-prime average above.

Item424 provides a different first-Witt rational-endpoint determinant. It does not identify that determinant with c_h*, and no bridge from all its rank-zero rows to this fixed algebraic coefficient family was found. It is not silently included in the present estimate.

## 7. Support versus valuation: exact scope of depth consequences

The result bounds one logarithmic support copy per prime. Every higher common-coordinate gate within the same ordinary j=1 cell is a subset of the first collision support: for example p^k dividing both Item197 coefficients C_0(M),C_1(M), with any fixed k>=2, implies their p^2 divisibility and hence (A). Thus each fixed depth's radical mass, and any fixed finite sum of such layers, has the same averaged zero conclusion.

This does **not** bound the complete valuation sum

    sum_p v_p(gcd(C_0(M),C_1(M))) log p

or an analogous post-booking content valuation. The number of layers is not known uniformly bounded, and the quantitative support decay does not justify summing infinitely many layers. The coarse exponential height bound permits one remaining prime to carry valuation of order M/log M, so an o(M/log M) count of support primes alone cannot force an o(M) total weight. A separate uniform tail or integrability estimate for valuations is needed.

Item393's raw and post-booking layer decompositions make exactly this distinction. Its forced fifth-layer target remains outside the present conclusion unless it is first restricted to rows satisfying this actual ordinary-cell collision gate.

Item424 gives, on its separately defined rank-zero branch with p^2>4m+1,

    v_p(c_m)>=b_(m,p)+1 iff kappa_(m,p)=0,
    kappa=0 and xi!=0 => v_p(c_m)=b_(m,p)+1.

The first condition describes support of a first extra layer, and the second identifies a stopping subbranch. For kappa=xi=0, deeper layers remain uncontrolled. No fixed-prime rational recurrence with a verified nondegenerate observation determinant for kappa was identified in this audit. Accordingly neither its whole first-Witt support nor its depth sum receives a Roth bound here. The archived ceilings0.3895079... and0.0561745... are explicitly one-layer ceilings and must not be treated as all-depth bounds.

The most useful next step after this completed extension is an actual p-adic upper-tail theorem on the remaining ordinary-cell collision support, or a new fixed-prime all-index recurrence for the complete first-Witt endpoint determinant. These are distinct tasks from repackaging mod-p coordinates.

## 8. Verification record

This pass read the relevant proof reports for Items218,222,229,237,243,264,280,288,293,321,382 and the relevant bridge/depth sections of424. It inspected Item243's theorem assembler, degree/Newton certificate records and historical audit, and verified all44 manifest file/dependency SHA-256 pins against current bytes. The current theorem-assembler replay has identical JSON content and identical bytes after normalizing the canonical file's CRLF endings to LF; it is not byte-identical before that normalization. An assembler replay checks the recorded proof inputs and logic; it does not rerun the2241-point rational computation or all Newton coefficients.

The script `check_roth_j1_extension.py` records those current hash checks, exact initial coefficients, the two finite initial recurrence substitutions, and the algebraic fixed-prime reindexing. These are bounded consistency checks of proved formulas, not evidence extrapolated into the zero-density theorem.
