> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the sparse multijet pullback certificate

## Audit scope and conclusion

This note audits the exact theorem and finite diagnostics in
sources/sparse_multijet_pullback_radius_improvement.md at frozen SHA-256



$$
\texttt{ea37af35ebfb97e0b8a79353eff5d6da4cbe49aebb1bd9ad0a7d6e9d1306163a}.
\tag{A1}
$$



The audited pullback is



$$
\begin{aligned}
\phi(z)={}&z+\frac{46}{7!}z^7(1-z)
 +\frac{213}{9!}z^9(1-z)
 -\frac{763}{10!}z^{10}(1-z)\\
 &+\frac{20078}{11!}z^{11}(1-z),
\qquad
G(z)=4\arctan\frac{\phi(z)}{2-\phi(z)}.
\end{aligned}
\tag{A2}
$$



I found no substantive defect.  Independent exact arithmetic confirms



$$
G(1)=\pi,\qquad
G^{(n)}(0)\in\mathbb Z\ (n\geq0),\qquad
\rho(G)>\frac{1747}{1000}.
\tag{A3}
$$



It also confirms the exact $3^4$ neighboring-lattice classification and
every stated diagonal Hermite--Padé record through $n=15$.  The numerical
root and search orderings remain diagnostics, exactly as labeled in the
source note.

The independent implementation deliberately differs from the source
program in three places:

1. Schur reduction uses SymPy's exact Gaussian-rational domain
   $\mathbb Q(i)$; the source certificate uses hand-written pairs of
   Python fractions.
2. The jets of $G=F(\phi)$ are obtained by direct formal power-series
   composition; the source HP program instead divides the rational
   derivative $G'$.
3. HP kernels are computed with the ordinary exact matrix nullspace, and
   cofactor content with a Bareiss determinant at the last nonzero kernel
   coordinate; the source program uses a polynomial-domain matrix and the
   first nonzero coordinate.

Thus the matches below do not arise from calling the source routines.

## 1. Frozen inputs and deterministic reruns

The seven audited inputs are:



$$
\begin{array}{l|l}
\text{artifact}&\text{SHA-256}\\ \hline
\text{source note}&
ea37af35ebfb97e0b8a79353eff5d6da4cbe49aebb1bd9ad0a7d6e9d1306163a\\
\text{certificate script}&
b32190715af12fa82a223a5f8165e75efbf307f1f0bcfa813a8b524e4b1fed0c\\
\text{certificate result}&
5b71cb31187d87037524a1932ea422ad3d757e68583ca84eadce9078549169db\\
\text{search script}&
946e8e9df6177cdff848ffd668291c20eec8b91b41726373fb655b4b4010241c\\
\text{search result}&
fa7ecd1590f01ce2b1185edea26e9bfd1889dd1168f18b855a89a1badc1568eb\\
\text{HP script}&
6ab090b23352b42f6c21126afda57cff52e1c5dbf50e719aa3c7407f218946c4\\
\text{HP result}&
1b64b42a0caaadd6e7670ec65305698af55e5ac1bf11f34856f42324d67bfedd.
\end{array}
\tag{A4}
$$



All hashes are asserted before the independent audit starts.  In
addition, I reran each of the three source programs with its archived
parameters.  The certificate, search, and HP outputs were respectively
byte-for-byte identical to the three frozen JSON files in (A4).

## 2. Endpoint polynomial and derivative jets

Direct rational expansion of (A2) gives



$$
\begin{aligned}
\phi(z)={}&z+\frac{23}{2520}z^7-\frac{23}{2520}z^8
 +\frac{71}{120960}z^9-\frac{2893}{3628800}z^{10}\\
 &+\frac{28471}{39916800}z^{11}
 -\frac{10039}{19958400}z^{12}.
\end{aligned}
\tag{A5}
$$



The independent program verifies exactly



$$
\phi(0)=0,\qquad \phi(1)=1,
\tag{A6}
$$



and obtains the derivative jets of orders $1,\ldots,12$:



$$
(1,0,0,0,0,0,46,-368,213,-2893,28471,-240936).
\tag{A7}
$$



These coefficients and jets match the certificate JSON exactly.

The all-order argument in the source note is sound.  For a term



$$
\frac{a_m}{m!}z^m(1-z),
\tag{A8}
$$



the only derivative-jet contributions are $+a_m$ in order $m$ and
$-(m+1)a_m$ in order $m+1$.  Hence every jet of $\phi$ is integral.
For



$$
F(w)=4\arctan\frac{w}{2-w},
\tag{A9}
$$



the exact formula



$$
F^{(k)}(0)=4(k-1)!2^{-k/2}\sin\frac{k\pi}{4}
\tag{A10}
$$



is integral in all four residue classes modulo $4$.  The valuation
bounds quoted in the source are sufficient, including the explicitly
separated small cases.  Faà di Bruno's formula then expresses every
$G^{(n)}(0)$ as an integer polynomial in the integral jets of $F$ and
$\phi$.  This is a genuine all-order proof; it does not depend on the
finite jet computation.

Finally, (A6) gives



$$
G(1)=F(1)=4\arctan(1)=\pi,
\qquad G(0)=F(0)=0.
\tag{A11}
$$



The explicit statement $G(0)=0$ is needed when identifying the Taylor
germ, and it is present in the frozen source.

## 3. No cancellation at a pulled-back singularity

Differentiation gives



$$
G'(z)=
\frac{4\phi'(z)}
 {(\phi(z)-(1+i))(\phi(z)-(1-i))}.
\tag{A12}
$$



Suppose $\phi(z)-(1+i)$ has multiplicity $s\geq1$ at $z_0$.
Then $\phi'$ has multiplicity exactly $s-1$, while the other
denominator factor is $2i\ne0$.  Thus the quotient in (A12) has a
simple pole with nonzero residue.  Its integral has a genuine logarithmic
singularity; the numerator cannot remove it.  The argument for $1-i$
is identical.

Conversely, in a simply connected disk without either kind of preimage,
(A12) is holomorphic and its integral from zero continues the germ.
Therefore



$$
\rho(G)=
\min\{|z|:\phi(z)=1+i\ \text{or}\ \phi(z)=1-i\}.
\tag{A13}
$$



Because $\phi$ has real coefficients, the two preimage sets are
conjugate.  Proving the bound for $1+i$ therefore proves it for both
targets.  This part of the source proof is complete.

## 4. Independent exact Schur--Cohn calculation

Let



$$
q(z)=\phi(z)-(1+i),\qquad r=\frac{1747}{1000},
\qquad
P_{12}(w)=w^{12}q(r/w).
\tag{A14}
$$



The orientation is important.  If $z$ is a zero of $q$, then
$w=r/z$ is a zero of $P_{12}$.  Thus



$$
|w|<1\quad\Longleftrightarrow\quad |z|>r.
\tag{A15}
$$



There is no zero at $z=0$, and the degree-12 leading coefficient of
$\phi$ is nonzero, so the reciprocal correspondence accounts for all
twelve roots.

For a monic polynomial



$$
P_d(w)=w^d+\cdots+c_d,
\tag{A16}
$$



put



$$
P_d^*(w)=w^d\overline{P_d(1/\overline w)},\qquad
S(P_d)=\frac{P_d-c_dP_d^*}{w}.
\tag{A17}
$$



The leading coefficient of $S(P_d)$ is



$$
g_d=1-|c_d|^2.
\tag{A18}
$$



The normalized Schur lemma says that $P_d$ has all roots in the open
unit disk if and only if $g_d>0$ and $S(P_d)$ has all its roots there.
For $d=1$, this reduces to the immediate condition $|c_1|<1$, so the
orientation and base case agree.

The independent program carries out (A17) in the exact domain
$\mathbb Q(i)$.  At every stage it normalizes the leading coefficient,
forms the conjugate reversal, verifies that the numerator has zero
constant term, drops that term to divide by $w$, and verifies that the
new leading coefficient is exactly $g_d$.

The independently recomputed numerator and denominator digit counts are



$$
\begin{array}{c|rrrrrrrrrrrr}
d&12&11&10&9&8&7&6&5&4&3&2&1\\ \hline
\#\operatorname{num}&87&174&348&521&695&868&1041&1214&1387&1560&1730&1895\\
\#\operatorname{den}&87&174&348&521&695&868&1041&1214&1387&1560&1732&1899.
\end{array}
\tag{A19}
$$



All twelve exact numerators and denominators are positive.  More strongly,
every normalized constant and every full gap fraction agrees exactly with
the frozen certificate JSON.  The independent result stores the complete
fractions and their hashes.

It follows successively from $d=1$ back through $d=12$ that every
zero of $P_{12}$ lies strictly inside the unit disk.  Equations
(A13)--(A15), plus conjugation, prove



$$
\boxed{\rho(G)>\frac{1747}{1000}.}
\tag{A20}
$$



No numerical root value is used in this implication.

## 5. Exact neighboring-lattice classification

I independently recomputed all



$$
3^4=81
\tag{A21}
$$



tuples obtained by adding $-1,0,$ or $1$ independently to



$$
(a_7,a_9,a_{10},a_{11})=(46,213,-763,20078).
\tag{A22}
$$



At $r=1747/1000$, the tuple (A22) is the unique one for which every
Schur gap is positive.  Among the other 80 tuples, the first nonpositive
gap occurs with counts



$$
\begin{array}{c|rrr}
\text{degree}&4&2&1\\ \hline
\text{count}&27&46&7.
\end{array}
\tag{A23}
$$



These exact counts match the source certificate.  This proves only the
stated finite-box classification; it does not prove global optimality.

## 6. Numerical diagnostics

The high-precision root calculation was independently repeated.  Its
smallest computed root for $\phi(z)=1+i$ is



$$
\begin{aligned}
z_{\rm comp}={}&
1.2312893806441062802399904642440212331\ldots\\
&+1.2397165470811756840418771959462179564\ldots\,i,
\end{aligned}
\tag{A24}
$$



with computed modulus



$$
r_{\rm comp}
=1.7472752090022395014604089188792222552\ldots.
\tag{A25}
$$



The frozen source correctly calls this the smallest *computed* root
modulus, not an exact equality for $\rho(G)$.

For the search artifact, an independently written NumPy polynomial
builder recomputed:

- all 30 archived one-term lattice records;
- all 9 selected multijet catalog records;
- all 2197 points in the displayed $13^3$ local box.

The maximum absolute radius differences from the archive were
$2.31\times10^{-14}$ and $7.04\times10^{-14}$ for the first two
groups.  The independent local-box winner was again exactly
$(46,213,-763,20078)$.  These comparisons validate reproducibility,
but remain floating-point diagnostics and are not used in (A20).

## 7. Independent formal jets and Hermite--Padé rows

The source HP program obtains the jets of $G$ by exact series division
of $G'$.  The audit instead starts from



$$
(w^2-2w+2)F'(w)=4
\tag{A26}
$$



to generate the ordinary Taylor coefficients of $F$, then directly
composes the truncated series $F(\phi(z))$.  Through order $46$, every
coefficient times its factorial is integral.  The resulting jet-vector
hash is



$$
\texttt{7eee931d26648dd605b882a5c94f0e844179b87c24c5639619c353529855eaf5},
\tag{A27}
$$



exactly matching the source derivative-division computation.

For each $1\leq n\leq15$, the independently constructed high matrix has
rows



$$
\left(
 k^{\underline0},\ldots,k^{\underline n}
 \ \middle|\
 k^{\underline0}g_k,\ldots,k^{\underline n}g_{k-n}
\right),
\quad k=n+1,\ldots,3n,
\tag{A28}
$$



followed by the endpoint row



$$
(-1,\ldots,-1\mid1,\ldots,1).
\tag{A29}
$$



Thus its shape is



$$
(2n+1)\times(2n+2).
\tag{A30}
$$



The exact nullspace is one-dimensional in all fifteen cases.  A nonzero
maximal minor, computed by Bareiss elimination, independently certifies
full row rank $2n+1$.  The audit used the last nonzero primitive-kernel
coordinate to extract cofactor content; the source used the first.  The
contents agree.

For every $n$, the following fields match the frozen HP result exactly:

- matrix shape, rank, and nullity;
- primitive high-kernel hash;
- maximal-cofactor content digit count;
- primitive full-triple hash and height digit count;
- raw endpoint pair, endpoint gcd, and reduced endpoint pair;
- exact first-free numerator and denominator.

The audit also used a separately constructed rational interval for
$e+\pi$, with different truncation lengths from the source.  It
independently reproduces the endpoint decades



$$
\text{zero},\ 0,\ 7,\ 17,\ 30,\ 51,\ 74,\ 102,\ 137,\ 177,\ 222,\
274,\ 334,\ 393,\ 458
\tag{A31}
$$



for $n=1,\ldots,15$.  At $n=1$, the endpoint pair is exactly
$(0,0)$; the first-free coefficient is nevertheless $-1/12$.  For
all $n=2,\ldots,15$, the endpoint interval has a certified nonzero sign.
Every first-free coefficient for $1\leq n\leq15$ is nonzero.

These are exact finite statements.  They imply no all-degree rank,
nonvanishing, content, height, or asymptotic theorem.

## 8. Universal-ceiling wording

The source note uses the archive's separately proved universal ceiling
$R_*=5.262410788162385\ldots$.  I did not rederive that elliptic-uniformization
theorem in this audit.  I did check the logic of the displayed interval:
(A20) supplies the strict lower inequality



$$
\frac{1747}{1000}<\sup\rho(F\circ\phi),
\tag{A32}
$$



while $R_*<5.262410788162386$ makes the rounded strict upper inequality
valid.  The diagnostic value (A25) is not substituted for the certified
lower endpoint.

## 9. Independent audit artifacts

The independent script is

scripts/independent_sparse_multijet_pullback_audit.py

with SHA-256



$$
\texttt{2f5a13f9018ce6441fc6ff0ac2513920982fb63463cd8618cb9d55a61896fdac}.
\tag{A33}
$$



Its exact output is

results/independent_sparse_multijet_pullback_audit.json

with SHA-256



$$
\texttt{39e4ca71c5e19d5af215bcfbb272b2947172087348775e7efb91b96e0d3bf5be}.
\tag{A34}
$$



The result embeds the audit-script hash and all seven frozen input hashes.
It stores all twelve full Schur gap fractions, all 81-neighbor outcomes
in classified form, the independently composed jet hash, per-$n$ matrix
hashes, complete HP invariants, independent endpoint certificates, and
the numerical diagnostic cross-checks.

**Final verdict:** the exact radius theorem, endpoint and all-order jet
proof, no-cancellation argument, local exact classification, and finite HP
claims in the frozen source are all supported.  No claim in these
artifacts decides whether $e+\pi$ is algebraic or transcendental.
