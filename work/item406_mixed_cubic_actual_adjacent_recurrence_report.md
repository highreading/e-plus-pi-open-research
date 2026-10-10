> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 406 — Actual mixed-cubic adjacent-diagonal recurrence and the sharp H-only lemma

Date: 2026-09-01  
Status: **WORK ONLY, AUDITED, NO CENTRAL EDIT, NO BOOKING**

## 1. Verdict

Let (q>0) be odd with (3\nmid q), put



$$
n=q-1,\qquad A=2n-1=2q-3,\qquad
 \alpha=A/3,
$$



and retain the actual coefficients (C_0,T_0,C_1,T_1) of canonical
Items 148, 157, and 396.  Canonical Item 403 proves, away from (6),



$$
d_1(q)=d_2(q)=H_q,\qquad d_3(q)=H_qG_q^{\rm prim}.       \tag{1.1}
$$



This item proves an all-(q), coefficientwise Hermite reduction of the
**actual coefficient rows**.  Define



$$
\begin{aligned}
 a_n&=[z^n]H(z)^\alpha,&a_{n-1}&=[z^{n-1}]H(z)^\alpha,\\
 b_n&=[z^n]\frac{(1+z^2)^\alpha}{(1-z)^{n+1}},&
 b_{n-1}&=[z^{n-1}]\frac{(1+z^2)^\alpha}{(1-z)^{n+1}},
\end{aligned}                                             \tag{1.2}
$$



where



$$
H(z)=(1+z)(1+z+z^2/2).
$$



Then



$$
\boxed{
\begin{aligned}
 C_0&=2a_n+a_{n-1},\\
 A C_1&=(5n-1)C_0-6a_n,\\
 T_0&=b_n+b_{n-1},\\
 A T_1&=(5n-7)T_0+6b_n.
\end{aligned}}                                             \tag{1.3}
$$



The two change matrices have determinants (6) and (-6).  Therefore,
for every prime $\ell\nmid6A$,



$$
\boxed{
 v_\ell(H_q)=
 \min\{v_\ell(a_n),v_\ell(a_{n-1}),v_\ell(b_n),v_\ell(b_{n-1})\}.}
                                                               \tag{1.4}
$$



Since (A) is the first factor of



$$
P_q=\prod_{j=0}^{q-2}(A-3j),                                \tag{1.5}
$$



equation (1.4) is an exact reduction of the (H_q)-support problem away
from (6P_q).  It is stronger than a finite factorization pattern and does
not use an ambient perturbation.

The case (q=1) has (H_1=1), so it has no (H)-support obstruction.  For a
compatible prime (p=6m+q) with (m\ge1) and (q\ge5), put (k=4m+1).  The congruence



$$
\alpha\equiv-k\pmod p                                    \tag{1.6}
$$



and a Cayley reciprocal transform reduce (1.4) still further.  Define



$$
R_{m}(z)=\frac{(1-z)^{6m}}{(1+z^2)^k},\qquad
 S_{m}(z)=\frac{R_m(z)}{(1+z)^k}.                           \tag{1.7}
$$



Then



$$
\begin{aligned}
 b_n&\equiv[z^n]R_m,&b_{n-1}&\equiv[z^{n-1}]R_m,\\
 a_{n-1}&\equiv2^{1-n}[z^{n-1}]S_m,&
 a_n&\equiv2^{-n}\bigl([z^n]S_m-[z^{n-1}]S_m\bigr)
 \pmod p.                                                   \tag{1.8}
\end{aligned}
$$



Thus the smallest missing (H)-only statement is exactly:

> **OPEN four-adjacent lemma.**  The two adjacent coefficient pairs in
> degrees (n-1,n) of (R_m) and (S_m) are not both ((0,0)) modulo
> any compatible prime (p=6m+q) with (m\ge1) and (q\ge5).

The reciprocal map (1.7) is lower triangular on the (n)-jet, but its top
two output coefficients depend on the entire preceding input jet.  It does
not by itself prove this lemma.  Hence Item 406 does **not** prove
(p\nmid H_q), (H_q\mid P_q), primitive-(G_q) support, (1.1) divided by
(P_q), or (c_m^>=1).

The second proved result is an exact algebraic recurrence/resultant theorem:
all four adjacent sequences in (1.2), and hence all four actual coefficient
sequences, lie in two explicitly parametrized algebraic function fields of
degree at most six.  This gives a uniform recurrence engine for the real
family, not a scan.  It also makes the remaining boundary precise: an
algebraic/P-recursive description does not automatically control the prime
support of coefficientwise gcds or cubes.

## 2. PROVED — coefficientwise Hermite identities

For a series (F) and a polynomial (S), define



$$
\mathscr D_F(S)=zS'(z)+z\frac{F'(z)}{F(z)}S(z)-nS(z).       \tag{2.1}
$$



The exact-derivative identity



$$
d\bigl(S(z)F(z)z^{-n}\bigr)
 =F(z)z^{-n-1}\mathscr D_F(S)\,dz
$$



gives



$$
[z^n]\mathscr D_F(S)F=0.                                  \tag{2.2}
$$



Take (F_C=H^\alpha) and



$$
S_C=-\frac{3(2+z)}A.
$$



Direct rational-function expansion gives



$$
\frac{(2+z)^4}{2H}
 =\frac{5n-1}{A}(2+z)-\frac6A+\mathscr D_{F_C}(S_C).        \tag{2.3}
$$



The definitions of (C_0,C_1), followed by (2.2), prove the first two
relations in (1.3).

Next take



$$
F_T=\frac{(1+z^2)^\alpha}{(1-z)^{n+1}},\qquad
 S_T=\frac{3(1-z^2)}A.
$$



One has



$$
\frac{(1+z)^4}{1+z^2}
 =\frac{5n-7}{A}(1+z)+\frac6A+\mathscr D_{F_T}(S_T),        \tag{2.4}
$$



which proves the last two relations in (1.3).

Equivalently,



$$
\binom{C_0}{AC_1}
 =\begin{pmatrix}2&1\\10n-8&5n-1\end{pmatrix}
 \binom{a_n}{a_{n-1}},                                    \tag{2.5}
$$





$$
\binom{T_0}{AT_1}
 =\begin{pmatrix}1&1\\5n-1&5n-7\end{pmatrix}
 \binom{b_n}{b_{n-1}}.                                    \tag{2.6}
$$



The determinants are (6) and (-6).  At $\ell\nmid6A$, both
matrices and the scaling by (A) are invertible over
$\mathbb Z_\ell$.  They preserve the generated local ideals, proving
(1.4), including valuations and not merely radicals.

This theorem isolates the common coefficient content (H_q).  It says
nothing by itself about (G_q^{\rm prim}), which is defined only after
the common content has been removed.

## 3. PROVED — two algebraic diagonal kernels

The following formal diagonal lemma is used twice.  If (B(0)=1), (w)
is the unique solution of (w=xB(w)) in (x\mathbb Q[[x]]), and (A(z))
is a formal series, then



$$
\sum_{r\ge0}[z^r]A(z)B(z)^{r+1}x^r
 =\frac{A(w)B(w)}{1-xB'(w)}.                               \tag{3.1}
$$



This follows either by formal residue at the kernel (z=xB(z)) or by
Lagrange inversion.

Put



$$
\mathcal A_0=\sum_{n\ge0}a_nx^n,\quad
 \mathcal A_1=\sum_{n\ge0}a_{n-1}x^n,
$$



with (a_{-1}=0).  Let (w_C=x+O(x^2)) be the branch



$$
w_C^3=x^3H(w_C)^2,\qquad D_C(w)=3H(w)-2wH'(w).             \tag{3.2}
$$



Equation (3.1), with (B=H^{2/3}), gives



$$
\boxed{
 \mathcal A_0=\frac{3w_C}{xD_C(w_C)},\qquad
 \mathcal A_1=w_C\mathcal A_0.}                            \tag{3.3}
$$



Likewise put



$$
\mathcal B_0=\sum_{n\ge0}b_nx^n,\quad
 \mathcal B_1=\sum_{n\ge0}b_{n-1}x^n.
$$



For the branch (w_T=x+O(x^2)),



$$
w_T^3(1-w_T)^3=x^3(1+w_T^2)^2,\qquad
 D_T(w)=3-6w-w^2-2w^3,                                    \tag{3.4}
$$



and (3.1), with (B=(1+z^2)^{2/3}/(1-z)), gives



$$
\boxed{
 \mathcal B_0=\frac{3w_T(1-w_T)}{xD_T(w_T)},\qquad
 \mathcal B_1=w_T\mathcal B_0.}                            \tag{3.5}
$$



These are explicit algebraic parametrizations of degree at most six.  For
example, eliminating (w_C) from (3.2)--(3.3) gives



$$
\begin{aligned}
0={}&16x^9Y^6-216x^7Y^4-216x^6Y^6+216x^6Y^3+729x^5Y^2\\
&+4374x^4Y^4-1458x^4Y+34722x^3Y^6-10206x^3Y^3+729x^3\\
&+6561x^2Y^2+2916xY^4-1458Y^6+1458Y^3,
\end{aligned}                                              \tag{3.6}
$$



with (Y=\mathcal A_0) and branch (Y(0)=1).  Eliminating (w_T) gives



$$
\begin{aligned}
0={}&1024x^9Y^6+1152x^7Y^4-3456x^6Y^6+324x^5Y^2+648x^4Y^4\\
&+138888x^3Y^6-7668x^3Y^3+2187x^2Y^2+16038xY^4-2916xY\\
&-1458Y^6+729Y^3+729,
\end{aligned}                                              \tag{3.7}
$$



with (Y=\mathcal B_0) and (Y(0)=1).

Applying (3.1) directly to the canonical coefficient definitions, rather
than integrating an Euler equation, gives the actual-row generating
functions



$$
\boxed{
\begin{aligned}
 \mathcal C_0&=\frac{3w_C(2+w_C)}{xD_C(w_C)},&
 \mathcal C_1&=\frac{3w_C(2+w_C)^4}
 {2xH(w_C)D_C(w_C)},\\
 \mathcal T_0&=\frac{3w_T(1-w_T)(1+w_T)}{xD_T(w_T)},&
 \mathcal T_1&=\frac{3w_T(1-w_T)(1+w_T)^4}
 {x(1+w_T^2)D_T(w_T)}.
\end{aligned}}                                             \tag{3.8}
$$



Let $\theta=x\,d/dx$, and let $\mathcal C_s,\mathcal T_s$ be the
generating functions of the four fixed-gap coefficient sequences, indexed
by (n=q-1).  Equations (1.3) are the exact Euler recurrences



$$
\begin{aligned}
 \mathcal C_0&=2\mathcal A_0+\mathcal A_1,\\
 (2\theta-1)\mathcal C_1&=(5\theta-1)\mathcal C_0-6\mathcal A_0,\\
 \mathcal T_0&=\mathcal B_0+\mathcal B_1,\\
 (2\theta-1)\mathcal T_1&=(5\theta-7)\mathcal T_0+6\mathcal B_0.
                                                               \tag{3.9}
\end{aligned}
$$



Thus every true admissible row is generated by the two kernels.  The
intervening even or (3\mid q) coefficients in the full formal series are
only an algebraic continuation used to state the recurrence.  They are not
actual mixed-cubic rows and are not used for a booking or density claim.

Algebraicity implies P-recursiveness, but the Smith target contains
coefficientwise gcds and cubes.  Ordinary products of generating functions
encode convolutions, not those coefficientwise operations.  Hence
(3.2)--(3.9) are an actual recurrence/resultant theorem, not a proof of
prime support.

## 4. PROVED — compatible Frobenius/Cayley normal form

The case (q=1) is already settled by (H_1=1).  Hence assume (q\ge5), and
let (m\ge1) and (p=6m+q) be prime.  Since (p>q), (n<p), and



$$
\alpha=\frac{2q-3}{3}\equiv-(4m+1)=-k\pmod p.             \tag{4.1}
$$



Also (p\nmid A): the only possible equality (p=A=2q-3) would give
(q=6m+3), contrary to (3\nmid q).

Because all coefficient degrees under discussion are less than (p),
binomial coefficients depend only on their exponents modulo (p).  The
identity



$$
(1-z)^{-(n+1)}
 =\frac{(1-z)^{p-n-1}}{(1-z)^p}
 \equiv\frac{(1-z)^{6m}}{1-z^p}\pmod p                     \tag{4.2}
$$



proves the two (b)-identities in (1.8).

For the (a)-pair, use the Cayley change



$$
z=\frac{2t}{1-t},\qquad
 H(z)=\frac{(1+t)(1+t^2)}{(1-t)^3}.                         \tag{4.3}
$$



Formal residue invariance gives, for (j=n,n-1),



$$
[z^j]H(z)^{-k}
 =2^{-j}[t^j]
 \{(1+t)(1+t^2)\}^{-k}(1-t)^{j-1+3k}.                     \tag{4.4}
$$



Since



$$
n-1+3k=p+6m+1,\qquad n-2+3k=p+6m,
$$



the factor ((1-t)^p=1-t^p) is invisible below degree (p).  Equations
(4.3)--(4.4) yield the two (a)-identities in (1.8).

Combining (1.4) and (1.8) proves the exact compatible-prime equivalence



$$
\boxed{
p\mid H_q
\Longleftrightarrow
\begin{cases}
[z^{n-1}]R_m=[z^n]R_m=0,\\
[z^{n-1}]S_m=[z^n]S_m=0
\end{cases}
\pmod p.}                                                  \tag{4.5}
$$



The last implication in the desired direction is still OPEN.  Multiplying
by ((1+z)^{-k}) is lower triangular with diagonal one on truncated jets,
but its degree-(n-1,n) outputs use all earlier coefficients.  No two-row
determinant closes (4.5).

## 5. H and primitive G remain separate

At a prime (ell>3), Item 403 first removes the common coefficient
content and then defines



$$
\gamma_\ell=min\{v_\ell(\rho^*),v_\ell(U_0^*),v_\ell(U_1^*)\},
 \qquad G_q^{\rm prim}=\prod_{\ell>3}\ell^{\gamma_\ell}.    \tag{5.1}
$$



Item 406 changes only the description of (H_q).  It does not transform
the primitive forms in (5.1) into ambient rows, and it does not infer
squarefreeness from finite diagnostics.

For overlap-safe primewise reasoning, one may partition a compatible prime
into:

1. (p\mid H_q), governed exactly by (4.5); or
2. (p\nmid H_q) and (p\mid G_q^{\rm prim}), governed by the actual
   primitive (\rho^*,U_0^*,U_1^*).

This partition is disjoint.  The raw factors (H_q) and
(G_q^{\rm prim}) themselves need not have disjoint prime supports, so
their logarithms must not be booked as independent reservoirs.

## 6. Capacity, deficit, bookings, and overlaps

### PROVED numerical status

The frozen booked deficit after the rank-one factor is



$$
T-r_1=1.0196329836694317938803064012\ldots .                \tag{6.1}
$$



Item 390's ceiling for the complete strictly large-prime common-content
component is



$$
C_>=\frac{\log136}{6}
 =0.8187758142893420014168718304\ldots .                    \tag{6.2}
$$



Even granting that full ceiling leaves the admission gap



$$
T-r_1-C_>
 =0.2008571693800897924634345708\ldots .                    \tag{6.3}
$$



### Consequences of hypothetical perfect success

* **CONDITIONAL, H only.**  Proving the four-adjacent lemma removes (H_q)
  from compatible primes.  It gives no present numerical ceiling reduction,
  because the primitive-(G_q) branch can still occupy the entire combined
  ceiling (6.2).  There is no proved disjoint positive lower bound to
  subtract.
* **CONDITIONAL, H and G together.**  Proving the actual support of
  (H_qG_q^{\rm prim}) in (P_q), or just its compatible-prime radical
  form, gives (c_m^>=1) for every (m).  This closes the separate
  (0.8187758\ldots) component ceiling.
* This combined success is a **Closer exclusion**, not a divisor Builder.
  It books no new factor and does not change the frozen booked deficit
  (6.1).  The other declared branches would still have to supply the full
  (1.0196329\ldots) deficit.

### De-overlap

1. Every prime here satisfies (p>6m), disjoint from the booked
   (p<2m) Cartier support, the small-prime remainder of Item 393, and the
   frozen clearing factors.
2. Item 390 already controls all valuation depths at such a prime through
   the actual residue gcd.  The fixed-gap Smith invariant is a first-digit
   exclusion carrier; its exponent is not a second bookable valuation
   reservoir.
3. An upper bound for (c_m^>) cannot be subtracted from Item 393's upper
   bound for total content.  No lower bound for (c_m^>) is known.
4. Large-prime beta matching on the primitive residual target is not
   automatically removed or booked by a common-content exclusion.
5. Canonical Item 387's bare mixed-kernel quotient supplies no independent
   arithmetic factor and is pinned here only as an architecture/claim-audit
   dependency.

Therefore



$$
\boxed{\Delta r_{\rm booked}=0,\qquad
        \Delta C_{\rm total}^{\rm proved}=0.}               \tag{6.4}
$$



## 7. Strict claim ledger

### PROVED

* The four all-(q) identities (1.3).
* The local ideal/valuation equivalence (1.4) away from (6(2q-3)).
* The degree-six algebraic kernels, direct actual-row formulas, and Euler
  recurrences (3.2)--(3.9).
* The compatible-prime reciprocal identities (1.8) and equivalence (4.5).
* The exact H/G primewise partition and zero booking.

### CONDITIONAL

* The four-adjacent lemma implies (p\nmid H_q) for every compatible prime.
* That lemma plus compatible primitive-(G_q) support implies (c_m^>=1).
* Full (H_qG_q^{\rm prim}\mid P_q) implies the same support conclusion,
  with multiplicities stronger than needed for first-digit exclusion.

### OPEN

* The four-adjacent lemma.
* (H_q\mid P_q), including multiplicities at primes already in (P_q).
* Compatible support or full divisibility for (G_q^{\rm prim}).
* (H_qG_q^{\rm prim}\mid P_q).
* Any positive Route-1 booking, Route-1 closure, or irrationality of
  (e+\pi).

No isolated-prime factorization, inferred squarefreeness, or ambient matrix
perturbation is used as progress.

## 8. Replay and pinned dependencies

Run:

```text
python work/item406_mixed_cubic_actual_adjacent_recurrence_certificate.py \
  --output work/item406_mixed_cubic_actual_adjacent_recurrence_certificate.replay.json
```

The standard-library replay:

1. verifies the exact coefficient identities against the canonical actual
   definitions on fixed normalization rows;
2. checks both determinant-(6) changes of basis;
3. reconstructs the four base sequences and all four actual sequences,
   verifies both algebraic kernels, all four direct actual-row formulas,
   and both displayed resultants through a fixed formal-series precision;
4. checks the compatible Frobenius/Cayley formulas on preselected
   normalization rows in both (q\bmod6) branches; and
5. verifies every pinned dependency hash.

The finite rows normalize formulas only.  Uniform claims rest on the
displayed rational, formal-residue, and Frobenius proofs.

Pinned canonical report dependencies:

```text
984445948c10e423cf752af580c80345b6d3d861c41db043312d49c1e81dedcc  sources/mixed_cubic_connection_determinant_3adic_nonvanishing.md
b44cc15d1a846d5298d61b9e53539116b31bbab0338dbc6e320fb0a875b0d0a0  sources/mixed_cubic_cube_smith_reduction.md
061e29589d427ccb5c8549c8344781c0c8f0e674d2fa525da03325312ce40625  sources/item387_mixed_kernel_quotient_and_claim_audit_report.md
5bfb3c871b12524f672df515e920236f2470145d4f68bdcd7b47f29408692f46  sources/item390_mixed_cubic_fresh_primitive_saturation_report.md
5e2c92f87075cbe3ac8af3191d8df7485ac6efd13609ede5f82819e355ae5f96  sources/item393_mixed_cubic_small_prime_strata_ceiling_report.md
7355b6909994357583f799e627e1ff19edb230a6a9002ee845be585057726aca  sources/item396_fixed_gap_resultant_3adic_report.md
9525428ec25231e712c74549e136f3d4c78e1e378164375e7ed4a514531d0214  sources/item403_mixed_cubic_exact_smith_and_finite_local_data_no_go_report.md
```

All Item-406 artifacts remain in `work/`.
