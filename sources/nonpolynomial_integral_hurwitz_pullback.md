> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# An entire integral-Hurwitz pullback with radius $>17679119/10000000$

## Scope and theorem

Define the real entire function



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
\tag{1}
$$



and put



$$
F(w)=4\arctan\frac{w}{2-w},
\qquad G(z)=F(\phi(z)).
\tag{2}
$$



This note proves exactly that



$$
\boxed{
\phi(0)=0,\quad \phi(1)=1,\quad
\phi^{(n)}(0)\in\mathbb Z\ (n\geq0),\quad
G(1)=\pi,\quad G^{(n)}(0)\in\mathbb Z\ (n\geq0),\quad
\rho(G)>\frac{17679119}{10000000}=1.7679119.
}
\tag{3}
$$



The strengthened radius proof uses a degree-24 Taylor truncation of each
exponential, a 65-step exact fraction-free Schur--Cohn computation, an exact
lower bound for
the truncated polynomial on the boundary, and Rouché's theorem. It excludes
both singular values $1+i$ and $1-i$ throughout the entire closed disk,
not merely at sampled boundary points.

The nearest high-precision diagnostic root has modulus
$1.7679119968\ldots$, only about $9.68\times10^{-8}$ above the certified
rational radius. It is still only a numerical diagnostic and is not part of
the theorem.

## 1. Endpoint fixing and all-order derivative-jet integrality

Every perturbation in (1) contains both a positive power of $z$ and a
factor $z-1$ or $1-z$. Therefore



$$
\phi(0)=0,
\qquad
\phi(1)=1.
\tag{4}
$$



The polynomial terms are integral-Hurwitz immediately: for



$$
P_{m,K}(z)=\frac{K}{m!}z^m(1-z),
$$



the only nonzero derivative jets at zero are



$$
P_{m,K}^{(m)}(0)=K,
\qquad
P_{m,K}^{(m+1)}(0)=-(m+1)K.
\tag{5}
$$



For the non-polynomial terms, let



$$
H_{m,a,k}(z)=\frac{k}{m!}z^m(z-1)e^{az},
\qquad m\geq1,\quad a,k\in\mathbb Z.
\tag{6}
$$



Expanding the exponential gives



$$
H_{m,a,k}(z)
=\frac{k}{m!}\sum_{s=0}^{\infty}
\frac{a^s}{s!}\left(z^{m+s+1}-z^{m+s}\right).
\tag{7}
$$



At order $m$, equation (7) gives



$$
H_{m,a,k}^{(m)}(0)=-k.
\tag{8}
$$



For $n=m+r$ with $r\geq1$, it gives



$$
\begin{aligned}
H_{m,a,k}^{(n)}(0)
&=\frac{k n!}{m!}
\left(
\frac{a^{r-1}}{(r-1)!}-\frac{a^r}{r!}
\right)\\
&=k\binom{n}{m}
\left(r a^{r-1}-a^r\right)\in\mathbb Z.
\end{aligned}
\tag{9}
$$



Equations (5), (8), and (9), together with the initial term $z$, prove



$$
\boxed{\phi^{(n)}(0)\in\mathbb Z\quad(n\geq0).}
\tag{10}
$$



This is an all-order proof. The certificate also evaluates the first 121
jets from these formulas as a consistency check; their canonical-vector
SHA-256 is

4c87f4d9e585302aab6d512af4c03847080d7f422c2a981370708a3a15bc93f9.

Since $F(1)=\pi$, the endpoint identity is



$$
G(1)=F(\phi(1))=\pi.
\tag{11}
$$



It remains important to pass from the integral jets of $\phi$ to those of
the function $G$ that enters the Hermite--Padé construction.  Direct
differentiation of (2) gives



$$
(2-2w+w^2)F'(w)=4.
\tag{11a}
$$



Write $f_n=F^{(n)}(0)$.  Then $f_0=0$, $f_1=2$, and, after taking
the $n$-th derivative of (11a) at zero, for every $n\geq1$,



$$
2f_{n+1}-2n f_n+n(n-1)f_{n-1}=0,
$$



or equivalently



$$
f_{n+1}=n f_n-\frac{n(n-1)}2 f_{n-1}.
\tag{11b}
$$



The coefficient $n(n-1)/2$ is an integer.  Induction in (11b) therefore
proves



$$
F^{(n)}(0)\in\mathbb Z\qquad(n\geq0).
\tag{11c}
$$



Finally, the set-partition form of the Faà di Bruno formula is



$$
G^{(n)}(0)
=\sum_{\mathcal P}
F^{(|\mathcal P|)}(\phi(0))
\prod_{B\in\mathcal P}\phi^{(|B|)}(0),
\tag{11d}
$$



where the sum is over all set partitions $\mathcal P$ of
$\{1,\ldots,n\}$.  Every summand in (11d) is an integer by (4), (10),
and (11c).  Together with $G(0)=F(0)=0$, this proves the HP-relevant
all-order conclusion



$$
\boxed{G^{(n)}(0)\in\mathbb Z\qquad(n\geq0).}
\tag{11e}
$$



## 2. The exact polynomial truncation

Let



$$
r_0=\frac{17679119}{10000000}
\tag{12}
$$



and define



$$
E_{a,24}(z)=\sum_{n=0}^{24}\frac{(az)^n}{n!}.
\tag{13}
$$



Replace the three exponentials in (1) by the corresponding polynomials
$E_{a,24}$, obtaining $\phi_{24}$, and set



$$
q(z)=\phi(z)-(1+i),
\qquad
q_{24}(z)=\phi_{24}(z)-(1+i).
\tag{14}
$$



The polynomial $q_{24}$ has degree



$$
40+1+24=65
\tag{15}
$$



and coefficients in $\mathbb Q(i)$. Its constant coefficient is
$-1-i$.

The exact certificate constructs every coefficient directly as a Python
Fraction. The SHA-256 of the canonical list of its real coefficients is

e00fdc2dbdfbaea19d56dd3e272ce6491bb8feb268b6f4c1a90f1a1e0fa95aa5.

The imaginary coefficient list has only its constant entry nonzero. Its
canonical SHA-256 is

f76392fe8eaea783791d9776ce4cc078868c35ba90806c5c9d7561e012b8a6f5.

## 3. Fraction-free Schur--Cohn proof for the truncation

Reverse the root problem at radius $r_0$:



$$
P_0(w)=w^{65}q_{24}(r_0/w).
\tag{16}
$$



Every root $z$ of $q_{24}$ corresponds to a root $w=r_0/z$ of
$P_0$. Thus $q_{24}$ has no zero in $|z|\leq r_0$ if every root
of $P_0$ lies strictly in $|w|<1$.

For a degree-$d$ polynomial written in leading-to-constant order,



$$
P(w)=a_0w^d+a_1w^{d-1}+\cdots+a_d,
$$



write



$$
P^*(w)=\overline{a_d}w^d+\overline{a_{d-1}}w^{d-1}
+\cdots+\overline{a_0}.
$$



The fraction-free Cohn transform used by the certificate is



$$
\mathcal C(P)(w)
=\frac{\overline{a_0}P(w)-a_dP^*(w)}{w}.
\tag{17}
$$



Its numerator has zero constant coefficient, and its leading coefficient is



$$
\Delta=|a_0|^2-|a_d|^2.
\tag{18}
$$



Multiplication by a nonzero scalar and removal of a common integer content do
not change the roots. Cohn's degree-reduction rule says that, when
$\Delta>0$, all $d$ roots of $P$ are in the open unit disk if and only
if all $d-1$ roots of $\mathcal C(P)$ are there.

After clearing the rational denominators of (16), all coefficients are
Gaussian integers. The program applies (17), removes the ordinary integer
content after each step, and continues through degrees



$$
65,64,\ldots,1.
$$



All 65 exact integers $\Delta$ are strictly positive. Consequently every
root of $P_0$ lies in the open unit disk and



$$
q_{24}(z)\ne0
\qquad(|z|\leq r_0).
\tag{19}
$$



For each of the 65 stages, the JSON certificate stores:

* SHA-256 hashes of the complete Gaussian-integer state before and after the
  transform;
* the exact gap's bit length and SHA-256;
* the leading and constant squared-modulus bit lengths;
* the removed content's bit length; and
* the exact 256-bit dyadic upper bound used in the boundary estimate below.

Every sign decision is made on an exact integer.

## 4. An exact boundary lower bound from the Schur recursion

Schur positivity proves (19), but Rouché also needs a quantitative lower
bound for $|q_{24}|$ on $|z|=r_0$. The same recursion provides one.

At stage $j$, divide the polynomial by its leading coefficient and call the
result $p_j$. Let $c_j$ be its constant coefficient and put



$$
g_j=1-|c_j|^2>0.
$$



The next normalized monic polynomial is



$$
p_{j+1}(w)=\frac{p_j(w)-c_jp_j^*(w)}{w g_j}.
\tag{20}
$$



On $|w|=1$, one has $|p_j^*(w)|=|p_j(w)|$. Therefore



$$
\begin{aligned}
g_j|p_{j+1}(w)|
&=|p_j(w)-c_jp_j^*(w)|\\
&\leq(1+|c_j|)|p_j(w)|,
\end{aligned}
$$



and hence



$$
|p_j(w)|\geq(1-|c_j|)|p_{j+1}(w)|.
\tag{21}
$$



For every stage, the program finds the smallest integer $u_j$ such that



$$
\left(\frac{u_j}{2^{256}}\right)^2
\geq |c_j|^2.
\tag{22}
$$



This uses only integer multiplication, division, and integer square root. It
also verifies $u_j<2^{256}$. Thus



$$
1-|c_j|\geq 1-\frac{u_j}{2^{256}}>0.
$$



Put the exact rational number



$$
B=\prod_{j=0}^{64}\left(1-\frac{u_j}{2^{256}}\right).
\tag{23}
$$



The final normalized degree-zero polynomial has modulus one. Iterating (21)
and using that the leading coefficient of the original $P_0$ is
$-1-i$, of modulus $\sqrt2$, gives



$$
|q_{24}(z)|=|P_0(w)|\geq\sqrt2 B
\qquad(|z|=r_0,\ w=r_0/z).
\tag{24}
$$



The exact fraction $B$ is stored in the result. For readability only, its
decimal size is



$$
B=8.0649634472\ldots\times10^{-20},
$$



and the exact squared lower bound in (24) is



$$
2B^2=1.3008727081\ldots\times10^{-38}.
\tag{25}
$$



The proof uses the stored rational fraction, not these decimals.

## 5. Exact exponential-tail upper bound and Rouché

For $|z|\leq r_0<2$ and $a=\pm1$, the exponential remainder satisfies



$$
\left|
e^{az}-E_{a,24}(z)
\right|
\leq e^{|z|}\frac{|z|^{25}}{25!}
<9\frac{r_0^{25}}{25!}.
\tag{26}
$$



The last rational constant is rigorous: $e<3$, so
$e^{r_0}<e^2<9$.

Also



$$
|z^m(z-1)|\leq r_0^m(1+r_0).
$$



It follows that, on the closed disk,



$$
|q(z)-q_{24}(z)|\leq T,
\tag{27}
$$



where the exact rational number



$$
T=
9\frac{r_0^{25}}{25!}(1+r_0)
\sum_{(m,a,k)}\frac{|k|r_0^m}{m!}
\tag{28}
$$



uses the three exponential triples from (1). The certificate stores $T$
exactly. Its decimal size is



$$
T=1.3865550243\ldots\times10^{-20}.
\tag{29}
$$



Finally, the program proves by exact rational cross multiplication that



$$
2B^2>T^2.
\tag{30}
$$



For scale only, the exact rational quotient in this comparison is



$$
\frac{2B^2}{T^2}
=67.6644544557\ldots>1.
$$



Both $B$ and $T$ are positive, so (30) and (24) imply



$$
|q-q_{24}|<|q_{24}|
\qquad(|z|=r_0).
$$



Rouché's theorem says that $q$ and $q_{24}$ have the same number of zeros
inside the circle. Equation (19) says that number is zero. The strict
boundary inequality also excludes a zero of $q$ on the circle itself.
Therefore



$$
\boxed{
\phi(z)\ne1+i\qquad
\left(|z|\leq\frac{17679119}{10000000}\right).
}
\tag{31}
$$



Because $\phi$ has real coefficients,



$$
\phi(z)-(1-i)=\overline{\phi(\overline z)-(1+i)}.
$$



Conjugating (31) gives the second required exclusion:



$$
\boxed{
\phi(z)\ne1-i\qquad
\left(|z|\leq\frac{17679119}{10000000}\right).
}
\tag{32}
$$



Thus both singular values are absent throughout the entire closed disk.

## 6. No additional finite singularities

The map $\phi$ is a finite sum of polynomials times exponentials, hence is
entire. It has no finite pole, branch point, or essential singularity. Its
essential behavior at infinity does not impose a finite Taylor singularity.

Moreover,



$$
(F\circ\phi)'(z)=
\frac{4\phi'(z)}
{(\phi(z)-(1+i))(\phi(z)-(1-i))}.
\tag{33}
$$



If $\phi(z)-(1+i)$ has multiplicity $s\geq1$ at $z_0$, then
$\phi'$ has multiplicity exactly $s-1$, while the other denominator
factor equals $2i$. Consequently (33) has a simple pole with nonzero
residue $-2si$. The conjugate calculation applies above $1-i$.
Every preimage is therefore a genuine logarithmic singularity; critical
points cannot cancel it.

Conversely, on the simply connected disk certified by (31)--(32), the
rational expression (33) is holomorphic and has the primitive matching the
germ $F\circ\phi$ at zero. Therefore



$$
\boxed{\rho(F\circ\phi)>\frac{17679119}{10000000}.}
\tag{34}
$$



## 7. Numerical diagnostics and search scope

High-precision Newton iteration suggests that the first three solutions of
$\phi(z)=1+i$ have moduli



$$
\begin{aligned}
1.7679119968043893287385198257\ldots,\\
1.7679145474456472713036908717\ldots,\\
1.7679170741623904366077513321\ldots.
\end{aligned}
\tag{35}
$$



These values are not certified root enclosures and are not used in (34).
The difference between the first displayed diagnostic modulus and the
certified rational radius is approximately
$9.68044\times10^{-8}$.
Floating-point argument-principle diagnostics, adaptively refined until each
principal argument step was below $0.25$, counted zero roots at radius
$1.7675$ and three at radii $1.768$ and $1.77$. The exact
Schur--Rouché proof, rather than those samples, supplies the rigorous
zero-free disk.

Before the sparse perturbation was constructed, a diagnostic single-term
search examined



$$
z+\frac{k}{m!}z^m(z-1)e^{az}
$$



for $1\leq m\leq30$, $0<|a|\leq20$, all nonzero integers
$|k|\leq50$, and additional logarithmically spaced effective coefficients
$k/m!$ ranging roughly from $10^{-14}$ to $10^5$. Across 291,920
sampled parameter triples, none had numerical winding number zero on the
circle of radius $1.72231$. This is a finite diagnostic, not a theorem
about the whole one-term family.

The successful candidate was obtained by perturbing a four-jet polynomial
with three low-exponential-frequency terms and optimizing the three nearly
coincident closest roots, followed by exact integer rounding and the proof in
Sections 2--5.

## 8. Reproducible artifacts and hashes

The strengthened exact certificate program is

scripts/nonpolynomial_integral_hurwitz_generalized_certificate.py

with SHA-256

b9fc93179ef0def5a5214bd928d489744652215fbf49faab1e030032eeb6721d.

Its frozen output is

results/nonpolynomial_integral_hurwitz_radius_17679119_10000000_certificate.json

with SHA-256

62ce908eef68dd3472f0841c6c20b09a94f8356465812aa19c204026d9dacdc0.

The exact core can be recomputed with

    python scripts/nonpolynomial_integral_hurwitz_generalized_certificate.py \
      --output /tmp/nonpolynomial_integral_hurwitz_radius_certificate.json

The JSON contains the initial polynomial-state hash, all 65 before/after
state hashes, every gap hash, the exact reflection product, the exact boundary
square lower bound, the exact tail and tail square upper bounds, and the final
exact comparison flag. These fields provide stage-by-stage hooks for an
independent implementation without requiring enormous gap integers to be
copied into this note.

The generalized program imports the exact arithmetic primitives and frozen
candidate constants from

scripts/nonpolynomial_integral_hurwitz_pullback_certificate.py

whose SHA-256 is

2e4ad9a01716d1e808b60ae04f5137d9d6020d46f52d22853c2415c105c41efd.

The earlier $707/400$ result remains preserved as

results/nonpolynomial_integral_hurwitz_pullback_certificate.json

with SHA-256

9d24c15e4f69fc5e8e1618f812e95ffa9d0351b401951795a023c4eaff9afb15.

That baseline JSON contains the longer numerical root and winding
diagnostics; the strengthened JSON deliberately contains only exact
certificate data plus a decimal rendering of an exact rational ratio.
Nothing in this construction proves algebraicity or transcendence of
$e+\pi$; it supplies a stronger exact analytic pullback for the continuing
Hermite--Padé search.
