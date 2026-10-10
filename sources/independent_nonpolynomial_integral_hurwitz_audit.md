> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the nonpolynomial integral-Hurwitz certificate

## Scope and verdict

This note independently audits the entire pullback and diagonal diagnostic
defined in:

- sources/nonpolynomial_integral_hurwitz_pullback.md;
- sources/nonpolynomial_integral_hurwitz_hp_diagnostic.md.

The candidate is



$$
\begin{aligned}
\phi(z)={}&z
+\frac{46}{7!}z^7(1-z)
+\frac{213}{9!}z^9(1-z)
-\frac{762}{10!}z^{10}(1-z)
+\frac{20073}{11!}z^{11}(1-z)\\
&+\frac{1215540}{15!}z^{15}(z-1)e^{-z}\\
&+\frac{65574371633155024}{26!}z^{26}(z-1)e^{-z}\\
&+\frac{40126919362525583214229456433446912}{40!}
 z^{40}(z-1)e^z,
\end{aligned}
\tag{B1}
$$



with



$$
F(w)=4\arctan\frac{w}{2-w},\qquad G=F\circ\phi.
\tag{B2}
$$



I found no substantive defect.  Independent exact arithmetic confirms



$$
\boxed{
\phi(0)=0,\quad\phi(1)=1,\quad
\phi^{(n)}(0),G^{(n)}(0)\in\mathbb Z,\quad
G(1)=\pi,\quad
\rho(G)>\frac{707}{400}.
}
\tag{B3}
$$



It also confirms every finite diagonal Hermite--Padé record through
$n=15$.  The numerical roots and sampled winding numbers remain
diagnostics, as the source explicitly states.

The independent implementation uses SymPy's exact Gaussian-integer domain
$\mathbb Z[i]$, while the source certificate uses hand-written integer
pairs.  It also constructs a new 160-bit reflection-product lower bound in
addition to reproducing the archived 128-bit bound.

## 1. Frozen audit snapshot

The audited files and hashes are:



$$
\begin{array}{l|l}
\text{artifact}&\text{SHA-256}\\ \hline
\text{pullback source}&
7c194175b3a5501740d0b0d46bd720dc4396ebb46e35210aa879c3a7c5f405af\\
\text{certificate script}&
2e4ad9a01716d1e808b60ae04f5137d9d6020d46f52d22853c2415c105c41efd\\
\text{certificate result}&
9d24c15e4f69fc5e8e1618f812e95ffa9d0351b401951795a023c4eaff9afb15\\
\text{HP source}&
aa93d76dea21a3d7ab24bd40362d6948c8586df11fc7e7138866247e6b79f78b\\
\text{HP script}&
27574fa09fc8a63231347776fa06f6a17b6fa8aafebec48224d5619ad29066b9\\
\text{HP result}&
ab01f6a7a731066f860c6f2f91423f30940b5cf9ecccb785c703fdfa867206fc.
\end{array}
\tag{B4}
$$



The independent program asserts all six hashes before doing any
calculation.  Fresh runs of the frozen certificate and HP scripts were
byte-for-byte identical to their archived JSON results.

## 2. Endpoints and all-order integral jets

Every perturbation in (B1) vanishes at both $0$ and $1$, so



$$
\phi(0)=0,\qquad \phi(1)=1,\qquad G(1)=F(1)=\pi.
\tag{B5}
$$



For a polynomial term $Kz^m(1-z)/m!$, the only nonzero derivative
contributions are



$$
K\quad\text{in order }m,\qquad
-(m+1)K\quad\text{in order }m+1.
\tag{B6}
$$



For



$$
H_{m,a,k}(z)=\frac{k}{m!}z^m(z-1)e^{az},
\qquad m\geq1,\quad a,k\in\mathbb Z,
\tag{B7}
$$



direct coefficient extraction gives



$$
H_{m,a,k}^{(m)}(0)=-k
\tag{B8}
$$



and, for $n=m+r$, $r\geq1$,



$$
H_{m,a,k}^{(n)}(0)
=k\binom{n}{m}\left(ra^{r-1}-a^r\right)\in\mathbb Z.
\tag{B9}
$$



Thus every derivative jet of $\phi$ is integral.  The independent program
recomputes the first 121 jets from (B6)--(B9); their canonical-vector hash is



$$
\texttt{4c87f4d9e585302aab6d512af4c03847080d7f422c2a981370708a3a15bc93f9},
\tag{B10}
$$



exactly matching the certificate.

For the base germ,



$$
(2-2w+w^2)F'(w)=4.
\tag{B11}
$$



If $f_n=F^{(n)}(0)$, differentiation at zero yields



$$
f_{n+1}=nf_n-\frac{n(n-1)}2f_{n-1},
\qquad f_0=0,\quad f_1=2.
\tag{B12}
$$



This integer recurrence proves $f_n\in\mathbb Z$ for all $n$.  The
set-partition form of Faà di Bruno then writes $G^{(n)}(0)$ as a sum of
products of integral $F$- and $\phi$-jets.  Therefore



$$
\boxed{G^{(n)}(0)\in\mathbb Z\qquad(n\geq0).}
\tag{B13}
$$



As a finite implementation cross-check, the audit directly composes
$F(\phi)$ through order $60$; every resulting jet is integral.

## 3. Independent reconstruction of the degree-61 truncation

Put



$$
r_0=\frac{707}{400},\qquad
E_{a,20}(z)=\sum_{\nu=0}^{20}\frac{(az)^\nu}{\nu!}.
\tag{B14}
$$



Replacing each exponential in (B1) by $E_{a,20}$ gives $\phi_{20}$,
and set



$$
q_{20}(z)=\phi_{20}(z)-(1+i).
\tag{B15}
$$



The independent script constructs (B15) by symbolic exact polynomial
expansion rather than the source coefficient loop.  It confirms



$$
\deg q_{20}=40+1+20=61,
\tag{B16}
$$



and obtains the exact real-coefficient-list hash



$$
\texttt{1d9bf38eb5e0627b828c6ff239f385e2330f25cc57c61c697bf8f0ddc9f7528a}.
\tag{B17}
$$



The imaginary part has only the constant coefficient $-1$.  Both facts
match the frozen certificate.

Reverse at $r_0$:



$$
P_0(w)=w^{61}q_{20}(r_0/w).
\tag{B18}
$$



After exact denominator clearing and ordinary integer-content removal, the
independent primitive Gaussian-integer state has hash



$$
\texttt{86cf6c8908e4ea01c0fb64b5c31911caab744456c865f7ae4614a88050d41be1},
\tag{B19}
$$



again exactly matching the source.  The pre-primitive common denominator
also matches, and the initial integer content is $1$.

## 4. Fraction-free Schur orientation

Write a degree-$d$ polynomial in leading-to-constant order as



$$
P(w)=a_0w^d+\cdots+a_d
\tag{B20}
$$



and define



$$
P^*(w)=w^d\overline{P(1/\overline w)}.
\tag{B21}
$$



The source transform is



$$
\mathcal C(P)
=\frac{\overline{a_0}P-a_dP^*}{w}.
\tag{B22}
$$



Its constant numerator coefficient is
$\overline{a_0}a_d-a_d\overline{a_0}=0$, so division by $w$ is exact.
Its leading coefficient is



$$
\Delta=|a_0|^2-|a_d|^2.
\tag{B23}
$$



To check that (B22) has the correct orientation, normalize
$p=P/a_0$ and put $c=a_d/a_0$.  Since
$p^*=P^*/\overline{a_0}$,



$$
p-cp^*
=\frac{\overline{a_0}P-a_dP^*}{|a_0|^2}.
\tag{B24}
$$



Thus (B22), after division by $w$, differs from the standard monic Schur
transform only by a nonzero scalar.  The condition $\Delta>0$ is exactly
$|c|<1$.  Removing an ordinary integer content at the end of a stage
also changes only a scalar and cannot change any root.

The independent program performs all 61 transforms in SymPy's
$\mathbb Z[i]$ domain.  At each degree $61,60,\ldots,1$, it verifies:

- the complete incoming state hash;
- leading- and constant-norm bit lengths;
- positivity, bit length, and SHA-256 of $\Delta$;
- the exact 128-bit reflection upper bound and factor;
- removed-content bit length;
- the complete outgoing state hash.

Every field matches the archived record exactly.  The final primitive
degree-zero state is $1$.  Therefore every root of $P_0$ lies in
$|w|<1$.  Since $w=r_0/z$,



$$
q_{20}(z)\ne0\qquad(|z|\leq r_0).
\tag{B25}
$$



This proves zero-freeness of the truncation throughout the closed disk,
not merely at sampled points.

## 5. Quantitative boundary lower bound

For each normalized monic stage $p_j$, let $c_j$ be its constant
coefficient and



$$
g_j=1-|c_j|^2>0.
\tag{B26}
$$



The next normalized stage is



$$
p_{j+1}(w)
=\frac{p_j(w)-c_jp_j^*(w)}{wg_j}.
\tag{B27}
$$



On $|w|=1$, $|p_j^*(w)|=|p_j(w)|$.  Hence



$$
\begin{aligned}
g_j|p_{j+1}(w)|
&\leq(1+|c_j|)|p_j(w)|,\\
|p_j(w)|
&\geq(1-|c_j|)|p_{j+1}(w)|.
\end{aligned}
\tag{B28}
$$



At the archived precision, let $u_j$ be the least integer such that



$$
\left(\frac{u_j}{2^{128}}\right)^2
\geq |c_j|^2.
\tag{B29}
$$



The exact integer-square-root calculation also gives $u_j<2^{128}$.
Thus every factor



$$
1-\frac{u_j}{2^{128}}
\tag{B30}
$$



is positive and no greater than $1-|c_j|$.  With



$$
B_{128}=\prod_{j=0}^{60}
\left(1-\frac{u_j}{2^{128}}\right),
\tag{B31}
$$



iteration of (B28) gives $|p_0|\geq B_{128}$ on the unit circle.

The initial *rational* reversed polynomial in (B18), before integer
clearing, has leading coefficient $q_{20}(0)=-1-i$, of modulus
$\sqrt2$.  Reflection coefficients are invariant under the scalar used
for denominator clearing.  Also $|w^{61}|=1$.  Consequently



$$
|q_{20}(z)|=|P_0(w)|
\geq\sqrt2\,B_{128},
\qquad |z|=r_0,\quad w=r_0/z.
\tag{B32}
$$



This verifies the potentially delicate leading-factor bookkeeping.

The independent program exactly reproduces the archived fraction
$B_{128}$.  It then repeats the integer-square-root construction at a
new precision of 160 bits, producing



$$
B_{160}=\prod_{j=0}^{60}
\left(1-\frac{v_j}{2^{160}}\right).
\tag{B33}
$$



This second rational number is independently stored in full.  It satisfies
the same boundary proof and supplies a separate check that the conclusion
does not depend on a transcription of the archived 128-bit factors.

## 6. Exponential tail and Rouché comparison

For $|z|\leq r_0<2$ and $a=\pm1$,



$$
\left|e^{az}-E_{a,20}(z)\right|
\leq e^{|z|}\frac{|z|^{21}}{21!}
<9\frac{r_0^{21}}{21!}.
\tag{B34}
$$



The final rational constant is rigorous: $e<3$, hence
$e^{r_0}<e^2<9$.  Moreover,



$$
|z^m(z-1)|\leq r_0^m(1+r_0).
\tag{B35}
$$



Therefore



$$
|q-q_{20}|\leq T,
\tag{B36}
$$



where



$$
T=
9\frac{r_0^{21}}{21!}(1+r_0)
\left(\sum_{(m,a,k)}
\frac{|k|r_0^m}{m!}\right).
\tag{B37}
$$



Here the sum is over the three exponential terms in (B1).  The independent
exact fraction for $T$ matches the archive.  It is approximately
$4.26998\times10^{-16}$, whereas $B_{128}$ is approximately
$7.41844\times10^{-14}$.

Exact rational cross multiplication gives both



$$
2B_{128}^2>T^2
\qquad\text{and}\qquad
2B_{160}^2>T^2.
\tag{B38}
$$



The squared ratio in the first inequality lies between $10^4$ and
$10^5$.  Positivity therefore permits square roots, and (B32),
(B36), and either inequality in (B38) give the strict boundary estimate



$$
|q-q_{20}|<|q_{20}|.
\tag{B39}
$$



Rouché's theorem and (B25) show that



$$
\phi(z)\ne1+i\qquad(|z|\leq707/400).
\tag{B40}
$$



All coefficients of $\phi$ are real, so



$$
\phi(z)-(1-i)
=\overline{\phi(\overline z)-(1+i)}.
\tag{B41}
$$



Conjugation proves the same closed-disk exclusion for $1-i$.  Both
targets are therefore covered by one exact calculation.

## 7. Taylor radius and noncancellation

The map $\phi$ is entire.  It contributes no finite pole, branch point,
or essential singularity.  Differentiation gives



$$
G'(z)=
\frac{4\phi'(z)}
 {(\phi(z)-(1+i))(\phi(z)-(1-i))}.
\tag{B42}
$$



If $\phi-(1+i)$ has multiplicity $s$ at $z_0$, then $\phi'$ has
multiplicity $s-1$, while the other denominator factor is $2i$.
Thus $G'$ has a simple pole with residue $-2si\ne0$, so $G$ has a
genuine logarithmic singularity.  The conjugate statement holds over
$1-i$.  Critical points do not cancel the pulled-back singularity.

Conversely, (B42) is holomorphic on the simply connected disk certified in
(B40)--(B41); its primitive matches the Taylor germ at zero.  Hence



$$
\boxed{\rho(G)>\frac{707}{400}=1.7675.}
\tag{B43}
$$



The strict inequality follows because the entire closed disk is
zero-free.

## 8. Numerical diagnostics

Independent high-precision root refinement reproduces the three displayed
computed moduli:



$$
\begin{aligned}
1.767911996804389328738519825748\ldots,\\
1.767914547445647271303690871682\ldots,\\
1.767917074162390436607751332140\ldots.
\end{aligned}
\tag{B44}
$$



The differences from the archived decimal strings are below
$5\times10^{-70}$.  These are not certified root enclosures and are not
used in (B43).  Likewise, the sampled winding numbers in the source result
remain explicitly diagnostic.

## 9. Independent diagonal Hermite--Padé audit

The independently composed jet vectors through order $46$ have hashes



$$
\begin{aligned}
\operatorname{SHA256}(\phi^{(0)},\ldots,\phi^{(46)})
&=\texttt{c370b3107e2e11f0124a9b778567a662ffbeb72543be2c3aacba0a3e64f0dc1d},\\
\operatorname{SHA256}(G^{(0)},\ldots,G^{(46)})
&=\texttt{db192d18af2ea0ba5f18439f5bbe325a0cc190ad1c31ee614fd87d353ded69b4}.
\end{aligned}
\tag{B45}
$$



They exactly match the frozen HP result.  For every $1\leq n\leq15$,
the audit independently constructs the $(2n+1)\times(2n+2)$ high matrix,
computes its ordinary exact nullspace, and evaluates a Bareiss maximal
minor at the last nonzero kernel coordinate.  The source generic routine
uses a polynomial-domain matrix and the first coordinate.

For all fifteen cases, the following exact fields agree:

- rank $2n+1$ and nullity one;
- primitive high-kernel hash and maximal-cofactor content length;
- primitive full-triple hash and height length;
- raw endpoint pair, endpoint gcd, and reduced endpoint pair;
- exact first-free numerator and denominator.

A separately constructed rational enclosure for $e+\pi$ reproduces the
endpoint decades



$$
\text{zero},\ 0,\ 7,\ 17,\ 29,\ 50,\ 72,\ 99,\ 134,\ 173,\ 217,\
268,\ 328,\ 391,\ 464.
\tag{B46}
$$



The $n=1$ endpoint pair is exactly $(0,0)$, but its first-free
coefficient is $-1/12$.  Every first-free coefficient through $n=15$
is nonzero.  For $n\geq2$, every endpoint sign is rigorously certified.
These are finite statements only; no all-degree conclusion is inferred.

## 10. Independent artifacts

The audit script is

scripts/independent_nonpolynomial_integral_hurwitz_audit.py

with SHA-256



$$
\texttt{6640fb5ceec6327f3732bb2bbbb5f17205980c53e00f1343a8f5626ef6114ff6}.
\tag{B47}
$$



Its output is

results/independent_nonpolynomial_integral_hurwitz_audit.json

with SHA-256



$$
\texttt{ad8a2b7ae447ba9e0236955ba9c7bd75acf3aa4374a6992b224d4ef4846867df}.
\tag{B48}
$$



The JSON embeds the audit-script hash and all six frozen input hashes.  It
contains the complete stage-by-stage Schur comparisons, both exact
reflection products, the exact tail and squared comparisons, integral-jet
hashes, numerical root cross-checks, and complete independent HP records
with per-matrix hashes.

**Final verdict:** the fraction-free orientation, quantitative boundary
lower bound, exact exponential tail, Rouché comparison, conjugate-target
transfer, all-order jet integrality, and finite HP diagnostics all pass
independent audit.  None of these artifacts decides whether $e+\pi$ is
algebraic or transcendental.
