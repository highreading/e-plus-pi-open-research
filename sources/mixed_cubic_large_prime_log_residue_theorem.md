> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Large-prime logarithmic residues: exact reduction and a fixed-gap theorem

Date: 2026-08-28

## 1. Definitions and residue coordinates

Put



$$
n=6m,\qquad k=4m+1,\qquad u=x(1-x),\qquad
 Q=(1+x)(1+x^2),
$$



and



$$
\omega_s=\frac{u^n}{Q^{k+s}}\,dx\quad(s=0,1).
$$



Let $\rho_s=\operatorname {Res}_{x=-1}\omega_s$ and
$\sigma_s=\operatorname {Res}_{x=i}\omega_s$.  Properness at infinity
and rational conjugation give



$$
\rho_s+\sigma_s+\overline{\sigma_s}=0.
$$



With the archive convention



$$
H_s=R_s+\frac{L_s}{4}\log2+\frac{E_s}{8}\pi,
$$



direct evaluation of the three simple-pole logarithms gives the exact map



$$
\boxed{L_s=2\rho_s=-4\operatorname {Re}\sigma_s,\qquad
 E_s=-4\operatorname {Im}\sigma_s.}                 \tag{1}
$$



In particular, over $\mathbb F_p$ or its quadratic extension, $L_s=E_s=0$
is equivalent to the vanishing of all three simple residues of $\omega_s$.

Writing $t=x+1$, the residue at $-1$ is



$$
\boxed{
 \frac{L_s}{2}=[t^{k+s-1}]
 \frac{(-1+t)^n(2-t)^n}{(t^2-2t+2)^{k+s}}.}          \tag{2}
$$



At $i$, if $z=x-i$, one likewise has



$$
\boxed{
 \sigma_s=[z^{k+s-1}]
 \frac{(i+z)^n(1-i-z)^n}
 {((1+i+z)(2i+z))^{k+s}}.}                           \tag{3}
$$



These are explicit finite binomial sums over $\mathbb Z[1/2]$ and
$\mathbb Z[i,1/2]$, respectively.

## 2. Audit of the claimed large-prime equivalence

For a prime $p>6m$, the factors $2$ and $M_{4m+1}$ are $p$-units.
Consequently



$$
p\mid\widehat A_m,\widehat B_m
 \quad\Longleftrightarrow\quad A_m=B_m=0\pmod p.      \tag{4}
$$



If $L_0=L_1=0$, the right side is immediate.  Conversely suppose
$A_m=B_m=0$, but $(L_0,L_1)\ne(0,0)$, and form



$$
\Omega=L_1\omega_0-L_0\omega_1
 =\frac{u^n(L_1Q-L_0)}{Q^{k+1}}\,dx.                 \tag{5}
$$



Its $L$, $E$, and relative endpoint coordinates all vanish.  Equation
(1) says that every simple residue vanishes.  All pole orders are less than
$p$, and (5) is proper at infinity, so termwise partial fractions make
$\Omega=dF$ in $\mathbb F_p(x)$.  The rational coordinate says
$F(0)=F(1)$.

If $p=n+1$, the coefficients of $x^{p-1}dx$ in the local expansions at
0 and 1 must vanish for an exact differential.  They are proportional to
$L_1-L_0$ and $4L_1-L_0$.  Since $p\ge7$, this forces
$L_0=L_1=0$, a contradiction.

If $p>n+1$, subtract the common endpoint value.  Local integration and
the behavior at infinity give



$$
F-C=\frac{u^{n+1}(ax+b)}{Q^k}.                     \tag{6}
$$



Differentiation shows that the numerator multiplying $u^n/Q^{k+1}$ is



$$
D=(n+1)u'(ax+b)Q+uaQ-ku(ax+b)Q'.                   \tag{7}
$$



For $D=L_1Q-L_0$, its $x^4$ coefficient gives
$b=(10m+2)a$; equality of its $x$ and $x^2$ coefficients then gives



$$
4a(4m+1)=0.
$$



Because $p>6m>4m+1$, one gets $a=b=0$, and hence
$L_0=L_1=0$, again a contradiction.  Thus the equivalence is valid:



$$
\boxed{p\mid\widehat A_m,\widehat B_m
 \Longleftrightarrow L_0=L_1=0\pmod p\qquad(p>6m).} \tag{8}
$$



No missing split-prime assumption or endpoint denominator occurs in this
argument.

## 3. Explicit finite-field formulas

The substitution $t=2y/(1+y)$ in (2) gives integral scaled residues



$$
\lambda_0:=2^{2m}L_0
 =[y^{4m}]\frac{(1-y)^{6m}(1+y)}{(1+y^2)^{4m+1}},     \tag{9}
$$





$$
\lambda_1:=2^{2m+2}L_1
 =[y^{4m+1}]\frac{(1-y)^{6m}(1+y)^4}{(1+y^2)^{4m+2}}.\tag{10}
$$



For $p=6m+q>6m$, necessarily $q$ is odd.  Frobenius and the fact that
the requested coefficient degrees are below $p$ turn (9)--(10) into the
polynomial formulas



$$
\boxed{\lambda_0\equiv[y^{4m}]
 \frac{(1+y)(1+y^2)^{2m+q-1}}{(1-y)^q}\pmod p,}      \tag{11}
$$





$$
\boxed{\lambda_1\equiv[y^{4m+1}]
 \frac{(1+y)^4(1+y^2)^{2m+q-2}}{(1-y)^q}\pmod p.}   \tag{12}
$$



Equations (11)--(12) are the clean finite-field hypergeometric form of the
remaining all-prime problem.

### A scalar recurrence and the exceptional ray

There is a second exact reduction which is useful for checking the logic of
simultaneous vanishing.  In the local coordinate $t=x+1$, put



$$
A=-2+3t-t^2,\qquad R=2-2t+t^2,
\qquad \frac{A^{6m}}{R^{4m+2}}=\sum_{j\ge0}f_jt^j.                 \tag{13}
$$



Logarithmic differentiation gives



$$
\begin{split}
-4(j+1)f_{j+1}={}&(20m-8-10j)f_j+(10j+10-20m)f_{j-1}\\
&+(10m-5j-6)f_{j-2}+(j+1-4m)f_{j-3}.              \tag{14}
\end{split}
$$



Let $r=4m$.  The two residues are



$$
\frac{L_1}{2}=f_{r+1},\qquad
 \frac{L_0}{2}=2f_r-2f_{r-1}+f_{r-2}.              \tag{15}
$$



Substituting (15) into (14) at $j=r,r-1$ proves, for every $p>6m$,



$$
L_0=L_1=0\quad\Longrightarrow\quad f_r=f_{r+1}=0. \tag{16}
$$



Conversely, the same two recurrence rows give



$$
2(5m+1)(10m+3)(2f_{r-1}-f_{r-2})=0.              \tag{17}
$$



Thus consecutive vanishing in (16) is equivalent to common log-residue
vanishing unless



$$
\boxed{p=10m+3}                                    \tag{18}
$$



is prime.  There is no exception in the implication actually needed to
exclude common residues, namely (16); (18) is only the exceptional ray for
the converse.

On that ray Frobenius gives the particularly concrete polynomial reduction



$$
f_j\equiv\frac12[t^j]A^{6m}R^{6m+1}\pmod p
 \qquad(j<p).                                        \tag{19}
$$



Since $tA(t)R(t)=(1-t)^5-(1-t)$, (19) can also be written as a
degree-five inverse-series (Hasse--Witt-type) problem for the branch of
$y^5-y=z$ through $y=1$.  This exact simplification has not yet yielded
a uniform nonvanishing proof.

## 4. A theorem for all fresh primes of gap below 49

For fixed odd $q$, set $r=4m$, $A=2m+q-1$, and $X=2^A$.  Extending
the coefficient convolution in (11) or (12) over the full palindromic
numerator gives, modulo $p=6m+q$,



$$
\lambda_0=C_0(q)X-T_0(q),\qquad
 \lambda_1=C_1(q)X-T_1(q),                         \tag{20}
$$



where the four rational numbers are exact coefficients of degree $q-1$.
For example,



$$
C_0(q)=[z^{q-1}](2+z)
 \left((1+z)(1+z+z^2/2)\right)^{2q/3-1},            \tag{21}
$$





$$
C_1(q)=\frac12[z^{q-1}](2+z)^4
 \left((1+z)(1+z+z^2/2)\right)^{2q/3-2}.            \tag{22}
$$



The tails $T_s$ consist of the final $q$ palindromic numerator terms;
the companion script evaluates them with generalized binomial coefficients.
Simultaneous vanishing in (13) requires



$$
\mathcal R_q:=C_0T_1-C_1T_0=0\pmod p.              \tag{23}
$$



For the nonmultiples of 3 through 19 the exact resultants are

| $q$ | $\mathcal R_q$ | compatible prime divisors $p=6m+q$ |
|---:|---:|---:|
| 1 | $-6$ | none |
| 5 | $77/729$ | 11 |
| 7 | $-28732/177147$ | none |
| 11 | $-29624686/1162261467$ | 659 |
| 13 | $343485685865/2259436291848$ | 31, 97 |
| 17 | $-1203769241299625/39531097362172608$ | 859667 |
| 19 | $-1241617202372113385/5403406870691968356$ | 3673, 1669951 |

Every odd gap divisible by 3 makes $p=6m+q>3$ a composite multiple of 3.
For every $q$ coprime to 6 with $1\le q<49$, the companion certificate
computes $\mathcal R_q$, gives a complete prime factorization of its
numerator, and checks the seven deterministic Miller--Rabin witnesses valid
for integers below $2^{64}$.  All factors in this range are below
$2^{64}$, so this is a deterministic primality check, not a probable-prime
claim.

After imposing the necessary congruence $p=6m+q$, the only additional
candidate divisors for gaps $23\le q<49$ are:

| $q$ | compatible prime divisors of $\operatorname{num}\mathcal R_q$ |
|---:|---:|
| 23 | 9086729 |
| 25 | 3817515241 |
| 29 | 71, 1109014802531 |
| 31 | 1215685868497699 |
| 35 | 139705851698215541 |
| 37 | 211, 306055151354467 |
| 41 | 6819625707194544521 |
| 43 | 449595109 |
| 47 | 1772711, 221691347 |

The fixed-gap formulas (20), evaluated with modular exponentiation, give

| $(q,p)$ | $(\lambda_0,\lambda_1)\bmod p$ |
|---:|---:|
| (23,9086729) | (6968972,3280064) |
| (25,3817515241) | (2876431221,2504630867) |
| (29,71) | (47,62) |
| (29,1109014802531) | (868855144685,741687535349) |
| (31,1215685868497699) | (489392167152882,715760424865233) |
| (35,139705851698215541) | (118104015550411676,130851404347489278) |
| (37,211) | (108,155) |
| (37,306055151354467) | (122420954951607,6676729950836) |
| (41,6819625707194544521) | (3407067723498951783,117576888476636043) |
| (43,449595109) | (313264361,405930302) |
| (47,1772711) | (1106710,1593221) |
| (47,221691347) | (68343263,93076840) |

For manageable indices the certificate independently replays these values
from the scalar coefficient recurrence.  The earlier compatible divisors
are likewise checked exactly:

| $(q,p,m)$ | $(\lambda_0,\lambda_1)\bmod p$ |
|---:|---:|
| (5,11,1) | (9,8) |
| (11,659,108) | (233,4) |
| (13,31,3) | (11,16) |
| (13,97,14) | (54,56) |
| (17,859667,143275) | (384753,650528) |
| (19,3673,609) | (1257,1422) |
| (19,1669951,278322) | (115224,147512) |

Therefore:

**Fixed-gap theorem.**  For every $m\ge1$ and every prime $p$ with



$$
6m<p<6m+49,
$$



the two logarithmic residues do not vanish simultaneously.  By (8), such a
prime cannot divide both $\widehat A_m$ and $\widehat B_m$.

## 5. Remaining obstruction

The fixed-gap argument does not scale uniformly with $q=p-6m$.  Equations
(20)--(23) reduce each fixed gap to a finite exact calculation, but the
resultant numerator develops prime divisors larger than $q$, and those
divisors can be compatible with $p=6m+q$.  The power $X=2^{2m+q-1}$
must then be checked as well.  No uniform factorization or finite-field
contiguous identity excluding all such primes has been obtained.

Thus this note proves the equivalence (8), the explicit formulas
(9)--(12), and the fresh-prime interval theorem, but it does **not** prove
the conjecture for every $p>6m$.

