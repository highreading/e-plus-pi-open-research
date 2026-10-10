> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the leading-B dyadic theorem and its tied pair

Date: 2026-09-13. Reviewed `raw_leading_B_dyadic_partial.md` against
the actual archived integer matrix, the incidence identity and
bordered-Cauchy proof in `sources/raw_arctan_bordered_rank_proof.md`,
and the distinct endpoint determinant theorem in
`sources/raw_arctan_endpoint_arithmetic.md`.

The partial nonvanishing theorem passes: the canonical leading B
coefficient is a dyadic unit for every even n and every n=3 mod4.
For n=1 mod4, the proof establishes divisibility but leaves possible
zero values open, apart from the explicit n=1 case. The tied-pair
refinement also passes and does not close that remaining class.

## 1. Changed appended row and exact normalization

The current appended row extracts the coefficient B_(n,n), rather
than evaluating B(1) or n!A(1). Dividing a high jet row indexed k by
k! and then expanding the coordinate row removes column B_n. This
leaves B columns0,...,n-1 and C columns0,...,n, with high rows
n+1,...,3n and the matching border. There is no appended factorial
factor. The valuation restoration is exactly



$$
v_2(B_\star)=\sum_{k=n+1}^{3n}v_2(k!)+v_2(D_n).
$$



The cofactor identity for the canonical coefficient is
B_(n,n)=B_star/Delta_B, since the denominator's appended functional is
B(1). That ratio has no further n!, leading-coefficient scale, or
primitive-polynomial gcd. The old Delta_B valuation is used only after
the new numerator determinant has been treated independently.

## 2. Arctangent block and the changed odd offset

When the matching border is assigned to C, the arctangent minor has
n high rows and an evaluation-at-one row. The archived incidence
identity (11a) identifies it, up to a common sign, with the exact
arctangent difference minor at parameter ell=n, without division.
Therefore its all-row-set valuation bound L_n is applicable.

I checked the relevant parity blocks explicitly. If n=2r+1 and
U0={n+1,...,2n}, then there are r+1 even rows and r odd rows. The
odd-pole block is square. The bordered block has even poles starting
at zero and odd ordinary rows
2r+3,2r+5,...,4r+1. Its first row-to-pole difference is **2r+3**.
If U* replaces 2n by2n+1, its bordered block instead has odd poles
starting at1 and even rows beginning2r+2. Its first difference is
**2r+1**. Thus the distinction in the new proof is correct.

For odd r, F_r(a)=a-1 mod4 gives an extra factor at a=2r+3=1 mod4,
but exact minimal valuation at a=2r+1=3 mod4. For even r, F_r(a) is
a unit for either offset. The ordinary row sets in both blocks are
consecutive within their parity classes, so their Vandermonde bounds
are exact. For even n, the U0 equality case is exactly the archived
one. The empty-row interpretation at n=1 is valid.

The compact expression L_n=2S(n)+2 floor((n+2)/4) agrees with the
archived parity formulas. This follows directly from
S(2r)=r(r-1)+2S(r) and
S(2r+1)=r^2+2S(r)+v_2(r!), together with the displayed bordered-Cauchy
valuation. It is not a new unproved numerical simplification.

## 3. Both exponential border assignments

Without the matching border, the exponential block has the ordinary
falling-factorial columns0,...,n-1, so its determinant is exactly
V(S)/product_(k in S)k!. There is no Lambda factor. The only maximum
factorial-sum sets are S0 and S*, because the cutoff is the sole
unselected/selected consecutive factorial tie. Their Vandermonde
valuations differ by v_2(n). Every other row set loses at least one
in its factorial sum, while all its other valuation bounds remain
valid.

Consequently S0 is uniquely minimal for even n, and S* is uniquely
minimal for n=3 mod4. In the remaining odd class both terms truly
have the same minimum valuation. The proof does not mistake that
tie for a unique term.

When the matching border is assigned to B, its factor -4 contributes
two powers. The exponential minor has n-1 ordinary nodes and the
integral functional Lambda on falling factorials through degree n-1.
Its lower bound is 2+S(n-1)-H_(n-1). The complementary C minor has
n+1 pure moment rows; the monic integral orthogonal basis supplies
the lower bound 2S(n+1). Subtracting the candidate minimum gives



$$
2+n+2v_2(n!)+v_2(n)-2\left\lfloor\frac{n+2}{4}\right\rfloor>0.
$$



I expanded this difference independently. Its sign is strict even at
n=1, and possible zero determinants or cancellation inside Lambda
can only raise the bound. This assignment therefore cannot cancel
the unique minimum in the proved classes.

For n=1 mod4, the two dyadic units at the minimum add to an element
divisible by two, possibly zero. All remaining terms are already at least one level
higher, so the divisibility conclusion is valid, including the
possibility of an identically zero numerator. At n=1 the entire
C-border contribution cancels and the other assignment gives the
known coefficient8; this exceptional small example is handled
correctly rather than suppressed by the positive-gap argument.

## 4. The additional tied-pair formula

The following refinement supplied by audit_sources also passes.
Let Q_k denote the raw monic Legendre polynomial and
beta_k=k^2/(4k^2-1). In the current paragraph these are the raw
orthogonal-polynomial objects, not the scalar accessory cubic.

After reversing C columns, the U0 moment determinant is, up to its
common fixed sign,



$$
\left(\prod_{j=0}^{n-1}h_j\right)Q_n(1).
$$



For U*, the final ordinary moment row has degree n rather than n-1.
In the monic orthogonal basis its Q_(n-1) entry vanishes by parity,
and its Q_n entry is h_n. Thus the ratio of the C minors is



$$
-\frac{h_n}{h_{n-1}}\frac{Q_{n-1}(1)}{Q_n(1)}
=\beta_n\frac{Q_{n-1}(1)}{Q_n(1)}.
$$



The exponential ratio is n(2n+1), and the Laplace signs differ by
minus. Therefore the two distinguished terms have combined factor



$$
1-\frac{n^3Q_{n-1}(1)}{(2n-1)Q_n(1)}.
\tag{A}
$$



At n=4s+1>=5, put a=v_2(n-1). The already proved bordered-Cauchy
valuations imply
v_2(Q_n(1))=v_2(Q_(n-1)(1))=2s and
v_2(Q_(n-2)(1))>=2s+1. The raw recurrence gives exactly



$$
\begin{aligned}
(2n-1)Q_n(1)-n^3Q_{n-1}(1)
={}&-(n-1)(n^2+n-1)Q_{n-1}(1)\\
&+(2n-1)\beta_{n-1}Q_{n-2}(1).
\end{aligned}
$$



The first term has valuation a+2s, since n^2+n-1 is odd. The second
has valuation at least2a+2s+1. Thus (A) gains exactly a powers, and
the pair's valuation is the baseline plus v_2(n-1). This is a result
about the pair only. Other row sets may contribute below or at that
new level, so it does not prove a valuation or nonvanishing statement
for the whole determinant in this residue class.

## 5. Saved-data controls and retained limits

I checked the already saved leading B coefficients at
n=2,3,4,5,8,16 and the explicit n=1 value. The dyadic valuations are
respectively0,0,0,2,0,0 and3. They match the theorem and its partial
divisibility statement. No coefficient matrix was solved and no new
degree was constructed. The input provenance and exact checks are
recorded in `raw_leading_B_independent_checks.json`.

The theorem proves leading-B nonvanishing in three residue classes.
It does not by itself prove cubic accessory degree, a nonzero
infinity cross-minor, a real size bound for the leading coefficient,
or a signed Legendre endpoint noncancellation estimate. The unfinished
quarter class and the lack of Archimedean estimates remain explicit.
