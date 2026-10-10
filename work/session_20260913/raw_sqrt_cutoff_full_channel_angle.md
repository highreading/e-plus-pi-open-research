> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Full channel conditioning at a cutoff of order sqrt(n)

Date: 2026-09-13. Original root continuation. Independent review
`raw_sqrt_cutoff_angle_independent_review.md` passes the full proof
without correction. The final sharpened comparison below is also
derived in the denominator variational note.

The positive-weight proof can control the full actual channel pair while
retaining only O(sqrt(n)) low nodes. A polynomial of linear degree is used
solely to prove the full angle. The separate rational surrogate supplies
the smaller exceptional-dimension count. These are different uses of
approximation; the linear polynomial degree is not charged to that count.

## 1. Change only the cutoff and the proof polynomial

Use the exact notation and supported positive-weight lemma of
`raw_positive_weight_channel_angle_closure.md`. Set

    N=2n,  b=ceil(192 sqrt(n)),  m=ceil(n/8),
    H₀=(2n+1)I−K_N,
    A_n=12 sqrt(28)n² exp(2sqrt(6n)).

All statements are for sufficiently large n; in particular b<n. Include
indices 0,...,b in their low factors, with the same optional final-root
transfer to equalize the high counts. Write the actual full coefficient
map, with its fixed harmless channel signs, as

    Z=F X,   X=[R(K)W_a,W_b],  F=F_b(K)>0.

The high poles obey β−(2n+1)≥b²/2 for all large n. Indeed the first
high index is greater than b and its true eigenvalue is at least
(b+1)(b+2)+3/4. The same lower bound holds relative to M_n=2n+3/4.
The largest high root obeys β−M_n≤n². In particular the reviewed
interlacing bound 2/n≤R(K)≤1 is still applicable.

F has positive coefficients in H₀, degree h≤n/2+1. The full surrogate

    X_tilde=[p_m(K)W_a,W_b]

has support ending at

    s≤n+2ell_max+2m+2,
    ell_max≤ceil((b+1)/2)+1.

Consequently

    s+h≤7n/4+O(sqrt(n))<2n.                         (1)

This verifies the exact supported polynomial reflection identities for
the entire pair, including all original multiplier degrees. No finite
boundary term is discarded. The supported positive-weight lemma bounds
the surrogate's separately orthonormalized angle by 1/A_n.

## 2. Uniform approximation on the actual row spectrum

The actual row interval [−4n²+3/8,2n+3/4] has length at most 6n².
For each high pole its rescaled Chebyshev location satisfies

    z_β−1≥b²/(6n²).

For large n this lower bound is at most one. The elementary inequality
arcosh(1+u)≥sqrt(u), 0≤u≤1, and the exact positive partial-fraction
weights of the ratio construction give a degree-m polynomial with

    ||R(K)−p_m(K)||≤epsilon_n
      :=2 exp(−(m+1)b/(sqrt(6)n))
      ≤2 exp(−4sqrt(6n)).                           (2)

Indeed (m+1)b≥(n/8)192sqrt(n)=24n sqrt(n). This is the same accuracy
as the earlier n^(3/4) proof. Since R,p_m,F commute, (2) holds as an
operator estimate in F energy as well. Eventually p_m is positive on
the row spectrum, so its channel remains injective.

Let B=diag(B_a,B_b) contain the actual individual energy Gram square
roots of R W_a and W_b. Put E=F^(1/2)X B⁻¹ and use those same
normalizations for E_tilde. The individual error estimate gives

    ||E−E_tilde||≤t_n:=(n/2)epsilon_n.

The surrogate's two blocks each have least singular value at least 1−t_n.
Apply the supported angle bound after separately orthonormalizing them,
then undo that normalization and apply the singular-value perturbation
inequality. Exactly as in the reviewed positive-weight proof,

    delta_n:=sigma_min(E)≥(1−t_n)/A_n−t_n
                          ≥1/(2A_n)                 (3)

for all large n, because A_n t_n→0. This time (3) holds for the FULL
actual pair at a cutoff b=O(sqrt(n)). It does not assert the bound for
the earlier numerical choice b=ceil(2sqrt(n)). The original Z is
unchanged; its factorization, F metric and individual Gram matrices are
those of the new cutoff.

## 3. Retain the rational exceptional count separately

At this new cutoff every high pole still lies in 2n≤β−M_n≤n². Hence
the common-denominator approximation and artificial nodes from
`raw_rational_surrogate_rank_improvement.md` remain valid without a
change in their bins, multiplicity or approximation bound. Restrict the
first multiplier to the same Q multiples as in that proof. Its polynomial
surrogate has support n+O(b), so its positive-weight lemma also applies.
The rational proof therefore gives exactly

    rank Z_L≥n−1−k,
    k=D+ell_0+ell_1−2=O(sqrt(n)log(n)),               (4)

and a good frame of dimension n−1−k with retained defect
eta_n=O(n³ exp(−2sqrt(6n))). All of this is in the same new F metric
as (3). The polynomial m from Section 2 is not used in counting the good
directions in (4). Thus full-pair conditioning and the rational rank
improvement are simultaneously available.

The unchanged physical Schur map still contains S⁻¹, the full spectral
amplitudes g_l and F[L,L]⁻¹/². This theorem does not bound that physical
metric or the exceptional retained singular value.

## 4. Concrete control of the cancellation in minimum-energy lifts

Use H=ZᵀF⁻¹Z=XᵀFX for the coefficient Gram (distinct from H₀ above).
Since the separately normalized blocks of E are isometries, ||E||≤sqrt(2).
Equation (3) gives the exact Loewner bounds

    delta_n² B²≤H≤2B²,
    (1/2)B⁻²≤H⁻¹≤delta_n⁻² B⁻².                 (5)

In particular each actual channel of any coefficient pair obeys

    ||R L_a u_a||_F, ||L_b u_b||_F
        ≤delta_n⁻¹ ||R L_a u_a+L_bu_b||_F,
    ||L_a u_a||_F
        ≤(n/(2delta_n))||R L_a u_a+L_bu_b||_F.        (6)

The functions here mean their actual polynomial/rational calculus on K
and the original offset seeds, as in X. Fixed signs make no difference.
Thus the full channel cancellation costs at most exp(O(sqrt(n))).

For the actual denominator constraint matrix write mathcal J=[J_a,0]
in the first-channel coefficient order, retaining the true low and high
factors and node amplitudes from the resolvent bridge. The full
denominator-complement Gram is G=mathcal J H⁻¹ mathcal Jᵀ. Define its
single-channel comparison

    G_single=J_a B_a⁻² J_aᵀ>0.

Congruencing (5) yields

    (1/2)G_single≤G≤delta_n⁻² G_single,
    delta_n² G_single⁻¹≤G⁻¹≤2G_single⁻¹.            (7)

There is a useful exact improvement of the lower comparison, observed
independently by audit_computations. The first diagonal block of H⁻¹ is
the inverse Schur complement
(B_a²−H_ab B_b⁻² H_ba)⁻¹, which is at least B_a⁻². Consequently

    G_single≤G≤delta_n⁻² G_single,
    delta_n² G_single⁻¹≤G⁻¹≤G_single⁻¹.             (8)

Equivalently, allowing an unconstrained second channel cannot increase
the minimum energy needed to realize first-channel interpolation data.
This comparison uses positive definite matrices and retains all original
constraint normalizations.

Every matrix is the actual one at this new cutoff. These estimates bound
the difference between full minimum-energy interpolation and its
single-channel version. They do not by themselves bound either one's
approximation into the retained prefix. That is the next analytic
problem, now with the possible channel-cancellation loss explicitly
controlled.
