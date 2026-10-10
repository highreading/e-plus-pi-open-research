> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Supplement: the remaining fresh-prime log-residue obstruction

Date: 2026-08-28

This supplement does not alter
`sources/mixed_cubic_coordinates_and_synchronization_audit.md`.  It records the exact
scalar recurrence and the strongest reduction obtained after that note was
frozen.  No all-prime coprimality theorem is claimed.

## 1. Exact scalar generating function

Put



$$
A(t)=(-1+t)(2-t)=-2+3t-t^2,\qquad
 R(t)=t^2-2t+2
$$



and



$$
f_m(t)=\frac{A(t)^{6m}}{R(t)^{4m+2}}
       =\sum_{j\geq0}f_{m,j}t^j.
$$



Then (f_{m,0}=2^{2m-2}), and logarithmic differentiation gives, with
(f_{m,j}=0) for (j<0),



$$
\begin{split}
 -4(j+1)f_{m,j+1}={}&(20m-8-10j)f_{m,j}
 +(10j+10-20m)f_{m,j-1}\\
 &+(10m-5j-6)f_{m,j-2}
 +(j+1-4m)f_{m,j-3}.                         \tag{1.1}
\end{split}
$$



The integral normalization



$$
g_{m,j}=\frac{2^j f_{m,j}}{f_{m,0}}
$$



has the exact generating function



$$
\boxed{
 \sum_{j\geq0}g_{m,j}v^j
 =\frac{(1-v)^{6m}(1-2v)^{6m}}
        {(1-2v+2v^2)^{4m+2}}.}                 \tag{1.2}
$$



In particular (g_{m,j}\in\mathbb Z).  The two normalized logarithmic
residues are exactly



$$
\boxed{
 \ell_{0,m}:=2^{2m}L_0
 =g_{m,4m}-2g_{m,4m-1}+2g_{m,4m-2},\qquad
 \ell_{1,m}:=2^{2m+2}L_1=g_{m,4m+1}.}          \tag{1.3}
$$



Equations (1.1)--(1.3) are a much faster exact way to compute the
log-residue pair than Gaussian convolution.

## 2. An exact terminating hypergeometric formula

The identity (A=t-R) gives an additional exact simplification.  For
(s=0,1), put



$$
a_s=2m-1-s,\qquad q_s=2m+1+2s,
$$



and define the terminating polynomial



$$
P_{N,a}(z)=\sum_{r\geq0}(-1)^r\binom{N}{a+r}z^r
 =\binom Na,{}_2F_1(1,a-N;a+1;z),\qquad N=6m. \tag{2.1}
$$



In the expansion of (A^N/R^{4m+1+s}), every term arising from a power
(t^jR^{a_s-j}) with (j\leq a_s) has degree strictly below the target
(4m+s).  The remaining terms therefore give the exact identity



$$
\boxed{
 L_s=2(-1)^{a_s}[t^{q_s}]
 P_{N,a_s}\!\left(\frac t{R(t)}\right).}          \tag{2.2}
$$



If (a=2m-1), (q=2m+1), and (z=t/R(t)), the elementary contiguous
identity



$$
P_{N,a-1}(z)=\binom N{a-1}-zP_{N,a}(z)
$$



turns (2.2) into the single-polynomial pair



$$
\boxed{
 L_0=-2[t^q]P_{N,a}(z(t)),\qquad
 L_1=-2[t^{q+2}]z(t)P_{N,a}(z(t)).}              \tag{2.3}
$$



This is an explicit binomial/hypergeometric formula, but no available
contiguous relation turns simultaneous vanishing of the two coefficient
functionals in (2.3) into a nonzero constant.

## 3. Fresh-prime Frobenius formula

Let (p>6m), (k_s=4m+1+s), and (d_s=k_s-1=4m+s).  Since (d_s<p)
and



$$
R(t)^p=R(t^p)\equiv2\pmod{(p,t^p)},
$$



the defining residue formula gives



$$
\boxed{
 L_s\equiv[t^{d_s}]A(t)^{6m}R(t)^{p-k_s}\pmod p.} \tag{3.1}
$$



Equivalently, if (r=p-6m), then



$$
\boxed{
 L_s\equiv-4[t^{d_s}]A(t)^{-r}R(t)^{-k_s}\pmod p,} \tag{3.2}
$$



where the negative powers mean their Taylor expansions at (t=0).
Formula (3.1) is a finite polynomial coefficient; (3.2) is often better
for a fixed linear ray in ((m,p)).

For completeness, expanding (A=t-R) and then (R^Q) also gives a fully
finite double-binomial version.  If
(e_s=p-k_s), (Q_j=6m+e_s-j), and
(\lambda=d_s-j), then



$$
\begin{split}
 L_s\equiv(-1)^{d_s}
 \sum_{j=0}^{d_s}\binom{6m}{j}
 \sum_{b=0}^{\lfloor\lambda/2\rfloor}
 2^{Q_j-b}\binom{Q_j}{b}
 \binom{Q_j-b}{\lambda-2b}\pmod p.              \tag{3.3}
\end{split}
$$



This is explicit but does not show nonvanishing.

## 4. Consecutive-zero reduction and its exceptional ray

Write (r_0=4m) and temporarily suppress the first index on (f).  Set



$$
x=f_{r_0},\quad y=f_{r_0-1},\quad
 z=f_{r_0-2},\quad w=f_{r_0-3}.
$$



Assume (p>6m).  If (L_0=L_1=0), then (1.3) in the (f)-normalization
gives (f_{r_0+1}=0) and (z=2y-2x).  The recurrence at (j=r_0)
then gives (w=-4x+2y).  At (j=r_0-1), it gives



$$
-4(4m)x=(-20m+2)y+20mz-(10m+1)w,
$$



and substitution reduces this to



$$
4(4m+1)x=0.
$$



Because (4m+1<p), (x=0).  Thus



$$
\boxed{L_0=L_1=0\pmod p\quad\Longrightarrow\quad
 f_{4m}=f_{4m+1}=0\pmod p.}                       \tag{4.1}
$$



Conversely, suppose (f_{4m}=f_{4m+1}=0).  The same two recurrence rows
now eliminate (w) and give



$$
\boxed{
 2(5m+1)(10m+3)(2f_{4m-1}-f_{4m-2})=0\pmod p.}   \tag{4.2}
$$



Since (p>6m), (5m+1) is a unit.  Therefore



$$
\boxed{
 p\nmid(10m+3)\quad\Longrightarrow\quad
 \bigl(L_0=L_1=0\iff f_{4m}=f_{4m+1}=0\bigr).}   \tag{4.3}
$$



For (m\geq1), (10m+3<2p) whenever (p>6m).  Hence the only possible
exception to the reverse implication in (4.3) is the single ray



$$
\boxed{p=10m+3\quad\text{with }p\text{ prime}.}                 \tag{4.4}
$$



The forward implication (4.1), which is the one needed for a common-log
zero, has no exceptional prime.

## 5. Degree-five inverse reduction on the exceptional ray

On the ray (4.4), let



$$
h_0=4m+1=\frac{2p-1}{5},\qquad
 h_1=4m+2=\frac{2p+4}{5},\qquad S=AR.
$$



Equation (3.2) specializes to



$$
L_0\equiv-4[t^{h_0-1}]A^{-2}S^{-h_0},\qquad
 L_1\equiv-4[t^{h_1-1}]A^{-1}S^{-h_1}\pmod p.   \tag{5.1}
$$



There is a special degree-five identity



$$
tS(t)=tA(t)R(t)=(1-t)^5-(1-t).                  \tag{5.2}
$$



Let (T(z)) be the formal inverse at zero of the left side of (5.2).
Lagrange inversion gives



$$
[t^{h-1}]H'(t)S(t)^{-h}=h[z^h]H(T(z)).          \tag{5.3}
$$



Thus (5.1) is exactly a simultaneous coefficient-nonvanishing question
for (H_0(T)), (H_1(T)), where (H_0'=A^{-2}) and (H_1'=A^{-1}).
Equivalently, after (y=1-T), the algebraic inverse is governed by
(y^5-y=z).  This is the sharpest exceptional-ray reduction currently
available.  It resembles a Hasse--Witt coefficient problem; no uniform
nonvanishing theorem was obtained.

## 6. Exact finite scans

The scalar recurrence was independently checked against the Gaussian
residue computation at (m=1,\ldots,11,20,40).  Two new finite scans were
then run.

1. `mixed_cubic_log_residue_exact_support_scan.py` computed the exact pair
   ((\ell_{0,m},\ell_{1,m})) for every (1\leq m\leq2000), took the
   exact gcd, and divided out every prime at most (6m).  Every residual
   cofactor was one.  This checks all prime sizes for those 2000 indices,
   not merely a bounded (p/m) window.
2. `mixed_cubic_exceptional_prime_scan.py` tested every (m\leq10000) for
   which (10m+3) is prime (2402 indices).  It found neither a common
   log-residue zero nor a consecutive Taylor zero.

Hashes:



$$
\begin{array}{c|c}
\text{file}&\text{SHA256}\\ \hline
\texttt{mixed\_cubic\_log\_residue\_exact\_support\_scan.py}
&62D15002273FFC1A41A6855F872255212E6D74747665FDF04F2125ABEA04C556\\
\texttt{mixed\_cubic\_log\_residue\_exact\_support\_scan\_m2000.json}
&2F54383CE2D46D497F5F8838381B60E9FA0C2DE2C53657CAF8FC793E7E2CD19B\\
\texttt{mixed\_cubic\_exceptional\_prime\_scan.py}
&C5FA9122E5C49F165EDFCF6A91410A873B4BFD05E201956374677978A3628E67\\
\texttt{mixed\_cubic\_exceptional\_prime\_scan\_m10000.json}
&29FA3FE35AEA46CDD206DCA30D19ED24A71E9C88932B00C3FD4D3A8B43D698D0
\end{array}
$$



Both scans are finite diagnostics.  They do not justify extrapolation.

## 7. Why the attempted Bezout closure stops

The first-order differential equation for (f_m) becomes a four-step
coefficient recurrence.  Two consecutive zero coefficients therefore leave
a genuine two-dimensional backward state.  Away from (p=10m+3), the
special rows at (4m-1,4m) identify that condition with a common log zero,
but do not force the remaining state to vanish.  On the exceptional ray,
one of those two row constraints degenerates exactly by the factor
(10m+3), and (5.1)--(5.3) is what remains.

Reciprocity of the polynomial in (3.1) supplies a reflected pair of zero
coefficients, and Frobenius splits it into coefficient blocks of length
(p), but the resulting relations are equalities among later Taylor
coefficients, not a nonzero scalar supported on primes at most (6m).
No uniform Bezout identity, resultant, or Casoratian with the required
prime support was found.  Producing such an identity, or finding a genuine
fresh-prime counterexample, remains the exact unresolved gap.

## 8. Audit cautions for the frozen main note

* In its equation (2.6), the word “algebraic” uses the standard formal
  Laurent-series branch/constant-term convention.  Equivalently, one first
  encodes the constant term as a bivariate rational diagonal and invokes
  the algebraicity theorem for bivariate rational diagonals.  Equation
  (2.7) is only asserted D-finite; it need not be algebraic.
* The low-order recurrence search used 181 terms (m=0,\ldots,180) and
  command-line bounds order 20, degree 8, subject to at least four more
  equations than unknowns.  Therefore the valid rectangular null boxes are
  order at most 16/degree at most 8 and order at most 20/degree at most 6.
  The JSON does not itself preserve the command-line arguments.
* The coordinate support checks through (m=100), and the isolated probes
  at (m=150,200), remain finite.  The new (m\leq2000) scan concerns only
  the log-residue gcd, not the full primitive coordinate (c_m).
* The beta congruence used in the main note is the exact prime-power
  statement (q_{N+p^a}\equiv-q_N\pmod{p^a}) for odd (p).  Iteration,
  including its alternating sign, is what yields
  (p^a\mid q_N\iff p^a\mid q_{N\bmod p^a}).
