> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A sparse integral-jet pullback with radius greater than $1.747$

## Scope and exact theorem

Let



$$
F(w)=4\arctan\frac{w}{2-w}
    =4\int_0^w\frac{dt}{t^2-2t+2}
\tag{1}
$$



as a germ at the origin.  Define



$$
\begin{aligned}
\phi(z)={}&z+\frac{46}{7!}z^7(1-z)
             +\frac{213}{9!}z^9(1-z)\\
           &-\frac{763}{10!}z^{10}(1-z)
             +\frac{20078}{11!}z^{11}(1-z),
\qquad G(z)=F(\phi(z)).
\end{aligned}
\tag{2}
$$



This note proves, by an exact rational Schur--Cohn certificate, that



$$
\boxed{
G(1)=\pi,\qquad G^{(n)}(0)\in\mathbb Z\quad(n\geq0),
\qquad \rho(G)>\frac{1747}{1000}.
}
\tag{3}
$$



Here $\rho(G)$ is the radius of the Taylor germ at zero.  High-precision
root finding, used only as a diagnostic, gives the smallest computed root
modulus



$$
r_{\mathrm{comp}}
=1.7472752090022395014604089188792222552\ldots.
\tag{4}
$$



The exact lower bound in (3) is already larger than both the previous
candidate's certified bound $3/2$ and its reported diagnostic radius
$1.5598556036\ldots$.  This is an analytic and integral-jet improvement.
It is not a proof of algebraicity or transcendence of $e+\pi$.

## 1. The sparse family and its sign convention

For a finite integer sequence $(a_m)$, put



$$
\phi_{\boldsymbol a}(z)
=z+\sum_m\frac{a_m}{m!}z^m(1-z).
\tag{5}
$$



Every summand vanishes at both endpoints, so



$$
\phi_{\boldsymbol a}(0)=0,
\qquad \phi_{\boldsymbol a}(1)=1.
\tag{6}
$$



The sign convention in (5) is unambiguous: the term indexed by $m$
contributes $+a_m$ to $\phi^{(m)}(0)$ and
$-(m+1)a_m$ to $\phi^{(m+1)}(0)$.  Equivalently, if unlisted
parameters are set to zero, then



$$
\phi_{\boldsymbol a}^{(k)}(0)
=\mathbf 1_{k=1}+a_k-k a_{k-1}\in\mathbb Z.
\tag{7}
$$



In particular, the earlier polynomial
$z+(z^7-z^8)/140$ is exactly the one-term choice
$m=7,a_7=36$, since $36/7!=1/140$.

For (2), expansion gives



$$
\begin{aligned}
\phi(z)={}&z+\frac{23}{2520}z^7-\frac{23}{2520}z^8
 +\frac{71}{120960}z^9-\frac{2893}{3628800}z^{10}\\
&+\frac{28471}{39916800}z^{11}
-\frac{10039}{19958400}z^{12},
\end{aligned}
\tag{8}
$$



and its derivative jets of orders $1,\ldots,12$ are



$$
(1,0,0,0,0,0,46,-368,213,-2893,28471,-240936).
\tag{9}
$$



## 2. Endpoint value and all-order integral jets

The endpoint claim follows at once from (1), (2), and (6):



$$
G(1)=F(1)=4\int_0^1\frac{dt}{(t-1)^2+1}=\pi.
\tag{10}
$$



Also $G(0)=F(0)=0$.  For positive orders, the derivative jets of the
base germ are



$$
F^{(k)}(0)
=4(k-1)!2^{-k/2}\sin\frac{k\pi}{4}\in\mathbb Z
\qquad(k\geq1).
\tag{11}
$$



For completeness, integrality in (11) can be checked by residue classes.
If $4\mid k$, the value is zero.  For $k=2j$ with $j$ odd, it is
up to sign $2^{2-j}(2j-1)!$; for $k=2j+1$, it is up to sign
$2^{1-j}(2j)!$.  The elementary bounds
$v_2((2j-1)!)\geq j-2$ and
$v_2((2j)!)\geq j-1$, with the small cases read directly, prove the
claim.

Faà di Bruno's formula now gives



$$
G^{(n)}(0)=
\sum_{k=1}^nF^{(k)}(0)
B_{n,k}\!\left(\phi'(0),\ldots,
\phi^{(n-k+1)}(0)\right),
\tag{12}
$$



where the exponential partial Bell polynomials have integer coefficients.
Equations (7), (11), and (12) prove the all-order integrality assertion in
(3).  No finite jet computation is being promoted to an all-order theorem.

## 3. The radius is a preimage problem with no cancellation

Differentiating the continued germ gives



$$
G'(z)=
\frac{4\phi'(z)}
{(\phi(z)-(1+i))(\phi(z)-(1-i))}.
\tag{13}
$$



Suppose $\phi(z)-(1+i)$ has a zero of multiplicity $s$ at $z_0$.
Then $\phi'$ has multiplicity exactly $s-1$, while the other
denominator factor equals $2i$ at $z_0$.  Thus (13) has a simple pole
at $z_0$, and $G$ has a genuine logarithmic singularity there.  The
same argument applies over $1-i$.

Conversely, on a simply connected disk containing no such preimage, (13)
is holomorphic and its integral from zero defines the continued germ.
Consequently



$$
\rho(G)=
\min\{|z|:\phi(z)=1+i\text{ or }\phi(z)=1-i\}.
\tag{14}
$$



All coefficients of $\phi$ are real, so the two root sets are conjugate
and have the same modulus multiset.

## 4. Exact Schur--Cohn proof of $\rho(G)>1747/1000$

Set



$$
q(z)=\phi(z)-(1+i),qquad r=\frac{1747}{1000},
\tag{15}
$$



and reverse at radius $r$:



$$
\begin{aligned}
P_{12}(w)=w^{12}q(r/w)
={}&-(1+i)w^{12}+rw^{11}
+\frac{23r^7}{2520}w^5-\frac{23r^8}{2520}w^4\\
&+\frac{71r^9}{120960}w^3
-\frac{2893r^{10}}{3628800}w^2
+\frac{28471r^{11}}{39916800}w
-\frac{10039r^{12}}{19958400}.
\end{aligned}
\tag{16}
$$



Every zero $z$ of $q$ corresponds to the zero $w=r/z$ of
$P_{12}$.  It is therefore enough to prove that all zeros of (16) lie
in the open unit disk.

For a degree-$d$ polynomial $P_d$, normalize its leading coefficient
to one, call its constant coefficient $c_d$, and put



$$
P_d^*(w)=w^d\overline{P_d(1/\overline w)},
\qquad
P_{d-1}(w)=\frac{P_d(w)-c_dP_d^*(w)}{w}.
\tag{17}
$$



The numerator in (17) has zero constant term, and its leading coefficient
is



$$
g_d=1-|c_d|^2.
\tag{18}
$$



The normalized Schur--Cohn reduction says that $P_d$ has all $d$ roots
in the open unit disk if and only if $g_d>0$ and $P_{d-1}$ has all its
roots there.  Thus strict positivity at every degree down to one is a
complete certificate.

All coefficients in (16) belong to $\mathbb Q(i)$.  Applying (17) with
pairs of exact rational numbers gives the following audit summary.  The
middle columns are the decimal digit counts of the exact numerator and
denominator of $g_d$; the displayed decimal is only a readability aid.
The complete fractions and every normalized $c_d$ are stored in the
certificate JSON.



$$
\begin{array}{c|r|r|c}
d&\#\operatorname{digits}(\operatorname{num}g_d)
 &\#\operatorname{digits}(\operatorname{den}g_d)&g_d\text{ (diagnostic)}\\ \hline
12&87&87&0.917371629603673\\
11&174&174&0.924710630306305\\
10&348&348&0.913875378937459\\
9&521&521&0.731319143106272\\
8&695&695&0.847303007043636\\
7&868&868&0.934478646855871\\
6&1041&1041&0.907173589519896\\
5&1214&1214&0.817400383735675\\
4&1387&1387&0.856399043016160\\
3&1560&1560&0.979182673923329\\
2&1730&1732&0.00348765407185472\\
1&1895&1899&0.000129250634683842
\end{array}
\tag{19}
$$



Every stored numerator and denominator in (19) is a positive integer.
The exact program asserts this before continuing each reduction.  Hence all
twelve zeros of $P_{12}$ lie in the open unit disk, so every zero of
$q$ has modulus greater than $1747/1000$.  Conjugation handles $1-i$,
and (14) proves (3).

As a separate exact finite classification, the same program replaces each
of



$$
(a_7,a_9,a_{10},a_{11})=(46,213,-763,20078)
\tag{20}
$$



independently by its value minus one, its value, or its value plus one.
Among all $3^4=81$ tuples, (20) is the unique tuple whose Schur recursion
passes at radius $1747/1000$.  Of the other 80 tuples, the first
nonpositive gap occurs at degree $4$, $2$, or $1$, with counts
$27,46,7$, respectively.  This is an exact finite-box statement, not a
claim of global optimality.

## 5. Numerical search diagnostics, clearly delimited

The search script records the following ladder of selected lattice points.
All radii in this table are floating-point diagnostics.



$$
\begin{array}{c|l|c}
\text{support}&(a_m)&\min|\phi^{-1}(1+i)|\\ \hline
\{7\}&(36)&1.559855603626574\\
\{7,8\}&(27,26)&1.604316908786596\\
\{7,10\}&(35,933)&1.618178838639653\\
\{7,18\}&(34,31469398607)&1.629718119909982\\
\{7,8,11\}&(43,32,17835)&1.689567336016155\\
\{7,10,11\}&(52,897,18070)&1.722307962114498\\
\{7,9,10,11\}&(46,213,-763,20078)&1.747275209002294
\end{array}
\tag{21}
$$



The reproducible one-term diagnostic scans $1\leq m\leq30$, first over
a fixed grid in the normalized coefficient $b=a_m/m!\in[-1/4,1/4]$,
then by deterministic scalar refinement and nearby integer rounding.  Its
best lattice record is the known $m=7,a_7=36$ polynomial.  This does not
classify coefficients outside the displayed interval, nor does a scalar
floating-point optimizer prove a global maximum even inside it.

For the final support, the script also exhausts the $13^3=2197$ lattice
points with $a_7=46$ fixed and



$$
207\leq a_9\leq219,qquad
-769\leq a_{10}\leq-757,qquad
20072\leq a_{11}\leq20084.
\tag{22}
$$



The tuple (20) has the largest computed radius in that box.  This ordering
is diagnostic; only the $3^4$ threshold classification following (20) is
exact.

The nearest computed preimage of $1+i$ for (2) is



$$
1.23128938064410628023999046424402\ldots
+1.23971654708117568404187719594622\ldots\,i,
\tag{23}
$$



whose modulus is the value in (4).  The next two computed moduli are
$1.7473666302661551\ldots$ and $1.7485216608077985\ldots$, explaining
the nonsmooth and numerically delicate optimization landscape.  None of
these decimal root values is used in the proof of (3).

## 6. The known universal ceiling

The archive's independent hyperbolic argument applies to every holomorphic
endpoint-fixing pullback that avoids $1\pm i$.  In the notation of
`sources/universal_pullback_radius_bound.md`, it proves



$$
\rho(F\circ\phi)\leq
R_*=\sqrt{\frac{1+y}{1-y}}
=5.2624107881623850775528279\ldots,
\tag{24}
$$



where



$$
y=\operatorname{Im}\left(
i\frac{K((1-i)/2)}{K((1+i)/2)}
\right).
\tag{25}
$$



This bound is sharp for unrestricted holomorphic maps but does not account
for polynomiality, real coefficients, or integral derivative jets.  It is
therefore a rigorous explanation that the possible radius supremum is
finite, but the wide interval



$$
\frac{1747}{1000}<
\sup_{\substack{\phi\text{ polynomial}\\
\phi(0)=0,\ \phi(1)=1\\
\phi^{(k)}(0)\in\mathbb Z}}
\rho(F\circ\phi)
<5.262410788162386
\tag{26}
$$



remains open.  The diagnostic value (4) suggests a slightly stronger lower
endpoint, but the unconditional lower statement in (26) is exactly the
Schur-certified one.

## 7. Finite diagonal Hermite--Padé diagnostic

An exact finite probe constructs the usual diagonal endpoint-matched system
for $1,e^z,G(z)$ through $1\leq n\leq15$.  Every matrix has full row
rank $2n+1$, nullity one, and a nonzero first unconstrained coefficient.
The $n=1$ endpoint form is zero.  For $n=2,\ldots,15$, directed exact
rational intervals certify the base-ten decades



$$
0,7,17,30,51,74,102,137,177,222,274,334,393,458.
\tag{27}
$$



The maximal-cofactor common-content digit counts for $n=1,\ldots,15$ are



$$
1,1,3,4,8,14,20,28,38,51,66,82,102,129,156.
\tag{28}
$$



These primitive endpoint forms grow rapidly.  The finite probe proves no
all-degree rank, height, content, or asymptotic theorem and supplies no
irrationality or transcendence conclusion.

## 8. Reproducible artifacts

The exact radius and local-lattice certificate is
`scripts/sparse_multijet_pullback_certificate.py`, SHA-256
`b32190715af12fa82a223a5f8165e75efbf307f1f0bcfa813a8b524e4b1fed0c`,
with exact output
`results/sparse_multijet_pullback_certificate.json`, SHA-256
`5b71cb31187d87037524a1932ea422ad3d757e68583ca84eadce9078549169db`.

The floating-point search diagnostic is
`scripts/sparse_multijet_pullback_search.py`, SHA-256
`946e8e9df6177cdff848ffd668291c20eec8b91b41726373fb655b4b4010241c`,
with output `results/sparse_multijet_pullback_search.json`, SHA-256
`fa7ecd1590f01ce2b1185edea26e9bfd1889dd1168f18b855a89a1badc1568eb`.

The finite exact diagonal probe is
`scripts/sparse_multijet_pullback_hp_probe.py`, SHA-256
`6ab090b23352b42f6c21126afda57cff52e1c5dbf50e719aa3c7407f218946c4`,
with output `results/sparse_multijet_pullback_hp_n15.json`, SHA-256
`1b64b42a0caaadd6e7670ec65305698af55e5ac1bf11f34856f42324d67bfedd`.

The search and root decimals are explicitly diagnostic.  The theorem (3)
depends only on the endpoint identities, the all-order jet argument, the
no-cancellation argument, and the exact rational Schur--Cohn records.
