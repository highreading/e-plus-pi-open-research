> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact non-diagonal endpoint scan for the high-radius integral-jet pullback

## Scope and verdict

Let



$$
\phi(z)=z+\frac{z^7-z^8}{140},\qquad
 G(z)=4\arctan\frac{\phi(z)}{2-\phi(z)},\qquad s=e+\pi .
\tag{1}
$$



Then $\phi(0)=0$, $\phi(1)=1$, and $G(1)=\pi$.  The all-order
integrality proof in
sources/high_radius_composed_integral_jet_pullback.md gives



$$
g_k:=G^{(k)}(0)\in\mathbb Z\qquad(k\geq0).
\tag{2}
$$



This note has two logically different parts.

1.  An exact finite computation treats every nonnegative degree triple
    $(a,b,c)$ with $a+b+c\leq18$.  It finds no decreasing family:
    the global minimum occurs already at $(0,5,0)$, and no total budget
    $6,\ldots,18$ improves it.
2.  An all-degree theorem rules out the constant-$B=C$ ray
    $(a,b,c)=(a,0,0)$.  The theorem is stated abstractly, with its
    denominator-growth and irrationality-measure hypotheses explicit, so
    it applies to any fixed rational-jet $\pi$-pullback satisfying the
    standard exponential common-denominator condition.

The finite scan is diagnostic outside the proved rays.  In particular,
it is not an all-degree rank theorem and it says nothing about whether
$s=e+\pi$ is algebraic or transcendental.

## 1. The exact dimension-balanced system

For fixed $a,b,c\geq0$, put



$$
M=a+b+c+1
\tag{3}
$$



and seek



$$
\deg A\leq a,\quad \deg B\leq b,\quad \deg C\leq c,
 \qquad
 A+B e^z+C G=O(z^M),\qquad B(1)=C(1).
\tag{4}
$$



Write $B(z)=\sum_{j=0}^bB_jz^j$ and
$C(z)=\sum_{j=0}^cC_jz^j$.  The derivative equations of orders
$0,\ldots,a$ uniquely reconstruct $A$.  The remaining equations have
orders $k=a+1,\ldots,M-1$.  In derivative-scaled form their entries are
integers:



$$
\sum_{j=0}^{b} k^{\underline j}B_j+
 \sum_{j=0}^{c} k^{\underline j}g_{k-j}C_j=0,
 \qquad
 k=a+1,\ldots,M-1,
\tag{5}
$$



where a term with $j>k$ is zero.  Appending



$$
-\sum_{j=0}^{b}B_j+\sum_{j=0}^{c}C_j=0
\tag{6}
$$



gives an integral matrix



$$
{\cal M}_{a,b,c}\in
 M_{\,b+c+1,\ b+c+2}(\mathbb Z).
\tag{7}
$$



Thus full row rank is exactly the expected rank, and then the
$(B,C)$-kernel is one-dimensional.

The program computes the rank and nullspace over $\mathbb Q$, reduces
the high kernel to a primitive integer vector, and computes its maximal
cofactor content.  If $v$ is the primitive kernel and $v_j\ne0$, then



$$
K_{a,b,c}=
 \left|\frac{\det {\cal M}_{a,b,c}^{(j)}}{v_j}\right|
\tag{8}
$$



is independent of $j$ and is the gcd of all signed maximal cofactors.
The low equations reconstruct $A$ over $\mathbb Q$; the complete
coefficient vector $(A,B,C)$ is then cleared and made primitive
separately.  This distinction prevents high-matrix cofactor content from
being confused with low-reconstruction content.

Finally set



$$
\alpha=A(1),\qquad \beta=B(1)=C(1).
\tag{9}
$$



For the primitive full triple its endpoint is



$$
\alpha+\beta s.
\tag{10}
$$



The program divides $(\alpha,\beta)$ by
$\gcd(|\alpha|,|\beta|)$ one more time.  Hence the stored endpoint gcd,
the primitive full-triple height, and the cofactor content are genuinely
different arithmetic quantities.

## 2. Directed endpoint and independent tail certificates

The sign and decimal decade of every finite endpoint are certified with
rational intervals, not floating-point evaluations.  The interval for
$e$ is a Taylor partial sum with a rational remainder bound.  The
interval for $\pi$ uses Machin's identity



$$
\pi=16\arctan(1/5)-4\arctan(1/239)
\tag{11}
$$



and alternating rational remainder bounds.  All comparisons with zero
are therefore exact.

There is also an independent rational Cauchy check.  On
$|z|\leq r=5/4$,



$$
|\phi(z)|\leq
 \frac{2434385}{1835008}
 <\frac{1414213}{10^6}<\sqrt2.
\tag{12}
$$



The distance from $\phi(z)$ to each base singularity $1\pm i$ is at
least



$$
\delta=\frac{2511049511}{28672000000},
\tag{13}
$$



and



$$
|\phi'(z)|\leq\frac{167813}{114688}.
\tag{14}
$$



Since



$$
G'(z)=
 \frac{4\phi'(z)}
 {(\phi(z)-(1+i))(\phi(z)-(1-i))}
\tag{15}
$$



and $G(0)=0$, radial integration gives the exact circle bound



$$
\max_{|z|=5/4}|G(z)|
 \leq {\cal G}:=
 \frac{6014417920000000000000}
 {6305369646693339121}
 <954.
\tag{16}
$$



After endpoint reduction, let $H_B,H_C$ be the maximum absolute
coefficient heights of $B,C$, and put



$$
K_E=M-b,\qquad K_G=M-c.
\tag{17}
$$



Cancellation through order $M-1$, the elementary exponential-tail
bound, and Cauchy's estimate give



$$
|\alpha+\beta s|
 \leq
 H_B(b+1)\frac{K_E+1}{K_EK_E!}
 +H_C(c+1)
 \frac{{\cal G}r^{-K_G}}{1-r^{-1}}.
\tag{18}
$$



The archived result stores both terms as exact fractions and checks that
the independently directed endpoint interval lies below (18).

## 3. Exhaustive results through total budget 18

There are



$$
\sum_{T=0}^{18}\binom{T+2}{2}=\binom{21}{3}=1330
\tag{19}
$$



degree triples.  The exact results are:

- every one of the 1330 matrices has full row rank and nullity one;
- the only identically zero endpoint pair is $(a,b,c)=(1,1,1)$;
- the only zero first-free coefficient is $(1,2,0)$: the advertised
  first-free derivative at $k=4$ is zero, but the derivative at $k=5$
  is $8$, so there is exactly one extra vanishing order;
- 1326 triples attain all three advertised degree bounds.  The four
  slack boxes are
  

$$
(0,1,0),\quad(1,2,1),\quad(1,3,0),\quad(2,2,0).
  \tag{20}
$$


  The last three are padded presentations of the $(1,2,0)$ polynomial
  triple; that triple has the same reduced endpoint pair $(6,-1)$ as
  $(0,2,1)$, but it has one additional vanishing order;
- all 1329 nonzero endpoint pairs have a directed interval disjoint from
  zero, and all 1329 pass the independent bound (18);
- at exact total $T=18$, cofactor-content lengths range from 1 to 109
  decimal digits, primitive full-triple heights from 17 to 67 digits, and
  endpoint gcds from 1 to 18 digits.

As a separate consistency check, the six diagonal cases
$(a,b,c)=(n,n,n)$, $1\leq n\leq6$, agree field for field with the
independently generated diagonal artifact
results/high_radius_composed_pullback_hp_n15.json: rank, nullity, high
kernel hash, primitive full-triple hash, raw and reduced endpoint pairs,
endpoint gcd, first-free rational coefficient, cofactor-content digit
length, and full-triple height length all coincide.

Exactly sixteen nonzero primitive endpoints have absolute value below one:



$$
\begin{array}{c|l}
T& (a,b,c)\\ \hline
2&(2,0,0)\\
3&(0,2,1),(1,2,0),(3,0,0)\\
4&(0,4,0),(1,0,3),(1,2,1),(1,3,0),(2,2,0)\\
5&(0,5,0),(1,4,0),(2,1,2),(2,2,1),(2,3,0)\\
6&(3,1,2),(4,0,2).
\end{array}
\tag{21}
$$



There are none at exact totals $7,\ldots,18$.

The global minimum through $T=18$ is attained at



$$
(a,b,c)=(0,5,0),\qquad
 (\alpha,\beta)=(129,-22).
\tag{22}
$$



Its exact primitive coefficient vector, in $A\mid B\mid C$ order, is



$$
(3096\mid -3096,4152,-2076,692,-217,17\mid -528).
\tag{23}
$$



Its full-triple height is $4152$, its maximal-cofactor content is $24$,
and its endpoint gcd is $24$.  The rational directed enclosure sharpens
the numerical statement to



$$
\frac{82761394925}{10^{12}}
 <129-22(e+\pi)<
 \frac{82761394926}{10^{12}}.
\tag{24}
$$



Thus the value is approximately $0.08276139492555$, but (24), not that
decimal, is the certificate.

The cumulative record changes only at total budgets



$$
\begin{array}{c|c|c}
T&(a,b,c)&(\alpha,\beta)\\ \hline
0&(0,0,0)&(1,-1)\\
1&(1,0,0)&(4,-1)\\
2&(2,0,0)&(11,-2)\\
3&(0,2,1)&(6,-1)\\
4&(1,0,3)&(88,-15)\\
5&(0,5,0)&(129,-22).
\end{array}
\tag{25}
$$



No budget $6,\ldots,18$ improves (24).  If one requires both $B$ and
$C$ to have positive attained degree, the best endpoint decades for
totals $2,\ldots,18$ are



$$
10^{\,0,-1,0,-1,-1,0,0,2,3,4,5,6,7,9,9,11,11},
\tag{26}
$$



where an exponent denotes the certified floor of the base-10 logarithm
of the absolute value.  If all three degrees are positive and attained,
the corresponding exponents for totals $4,\ldots,18$ are



$$
0,-1,-1,0,0,2,3,4,6,6,7,9,10,11,12.
\tag{27}
$$



These are finite allocation diagnostics, not monotonicity theorems.

### 3.1 Why the apparent late winner is a repeated fixed form

At every exact total $T=8,\ldots,18$, the unrestricted minimum is
reported at $(0,0,T)$, with reduced pair $(1,-1)$.  This does not
constitute a new approximation.

Indeed, on the entire ray $(a,b,c)=(0,0,c)$, the constant equation gives
$A_0=-B_0$, while the endpoint equation gives $C(1)=B_0$.  A nonzero
solution must have $B_0\ne0$: if $B_0=0$, then



$$
C(z)G(z)=O(z^{c+1}).
\tag{28}
$$



Since $G(z)=2z+O(z^2)$, triangular comparison forces
$C_0=\cdots=C_{c-1}=0$; then $C(1)=0$ also forces $C_c=0$.
Therefore every nonzero solution has endpoint



$$
B_0\bigl((e+\pi)-1\bigr).
\tag{29}
$$



After endpoint reduction this is exactly
$\pm(s-1)$, independently of $c$.  Since $e>2$ and $\pi>3$, its
absolute value is greater than $4$.

## 4. Exact continuation of the best finite edge $(0,b,0)$

The finite winner belongs to the edge with $A,C$ constant and
$\deg B\leq b$.  This edge has an exact two-coordinate description.
Put



$$
H(z)=e^{-z}G(z)=\sum_{k\geq0}\eta_k\frac{z^k}{k!},
\qquad
 \eta_k=\sum_{j=0}^{k}\binom{k}{j}(-1)^{k-j}g_j\in\mathbb Z.
\tag{30}
$$



Multiplying the cancellation equation by $e^{-z}$ gives



$$
B=-T_b(Ae^{-z}+CH).
\tag{31}
$$



The endpoint condition $B(1)=C$ is therefore



$$
-A\,U_b=C\,V_b,
\tag{32}
$$



where



$$
U_b=b!\sum_{k=0}^{b}\frac{(-1)^k}{k!},
\qquad
 V_b=b!\left(1+\sum_{k=0}^{b}\frac{\eta_k}{k!}\right).
\tag{33}
$$



Both coordinates are integers and obey the exact recurrences



$$
U_0=1,\quad U_b=bU_{b-1}+(-1)^b,
\qquad
 V_0=1,\quad V_b=bV_{b-1}+\eta_b.
\tag{34}
$$



Consequently, with $d_b=\gcd(U_b,V_b)$, the endpoint reduced directly
from this natural coordinate pair is



$$
L_b=\frac{U_b(e+\pi)-V_b}{d_b},
\tag{35}
$$



up to a simultaneous sign.  Equations (30), (34), and (35) are exact for
every $b$, not empirical fits.

For a finite-order recurrence for $\eta_b$, write



$$
p=140z+z^7-z^8,\quad
 P_0=560p',\quad Q_0=p^2-280p+39200.
\tag{36}
$$



Since $G'=P_0/Q_0$ and $G=e^zH$,



$$
Q_0(z)(H'(z)+H(z))=e^{-z}P_0(z).
\tag{37}
$$



Taking $n$-th derivatives at zero gives



$$
\sum_{j=0}^{\min(n,16)}
 \binom nj Q_0^{(j)}(0)
 \bigl(\eta_{n-j+1}+\eta_{n-j}\bigr)
 =
 \sum_{j=0}^{\min(n,7)}
 \binom nj P_0^{(j)}(0)(-1)^{n-j}.
\tag{38}
$$



The leading coefficient is $Q_0(0)=39200$, so (38) is a fixed-order
exact recurrence.

The archive continues (30)--(35) through $b=250$, with an exact
directed interval at every step.  The unique minimum on this computed
range is still $b=5$.  Selected certified endpoint decades are



$$
\begin{array}{c|rrrrrrrr}
b&5&10&20&50&100&150&200&250\\ \hline
\lfloor\log_{10}|L_b|\rfloor&
-2&3&12&53&135&231&333&441.
\end{array}
\tag{39}
$$



The observed $d_b$ never exceeds $202$ through $250$, but this is
only a diagnostic.  A uniform upper bound, or even a sufficiently slow
growth bound, for $d_b$ has not been proved here.  Thus (39) is not
promoted to an all-degree obstruction.  Formula (35) isolates the exact
remaining arithmetic issue rather than hiding it in polynomial
normalization.

## 5. An abstract all-degree obstruction for constant $B=C$

The following theorem does not depend on the special form of (1).

**Theorem 1 (constant-$B=C$ obstruction).**  Let



$$
J(z)=\sum_{k\geq0}\gamma_kz^k,\qquad \gamma_k\in\mathbb Q,
\tag{40}
$$



be a germ with a defined continuation to $z=1$ and $J(1)=\pi$.  Put



$$
\Pi_a=\sum_{k=0}^{a}\gamma_k=\frac{u_a}{D_a}
\quad\text{in lowest terms}.
\tag{41}
$$



Assume there are constants $C_0,C_1$, independent of $a$, such that



$$
\log D_a\leq C_1a+C_0.
\tag{42}
$$



For the endpoint-matched system



$$
\deg A\leq a,\qquad B,C\text{ constant},\qquad
 A+Be^z+CJ=O(z^{a+1}),\qquad B=C,
\tag{43}
$$



let the nonzero full polynomial triple be cleared primitively and let its
endpoint pair be reduced.  Then its primitive endpoint form $L_a$
satisfies



$$
\boxed{\log|L_a|\geq\frac12a\log a-O_J(a),}
\qquad\text{and hence}\qquad |L_a|\longrightarrow\infty.
\tag{44}
$$



The proof uses these two established rational-approximation inputs:
there are absolute constants $c_e,c_\pi>0$ such that every reduced
rational $r/q$ and $u/D$ satisfies



$$
\left|e-\frac rq\right|
 \geq\frac{c_e}{q^2\log(2q)},
\qquad
 \left|\pi-\frac uD\right|
 \geq c_\pi D^{-36/5}.
\tag{45}
$$



The first follows directly from Euler's continued fraction for $e$.
For the second, $36/5=7.2$ is a safe weakening of the proved upper
bound $7.103205334137\ldots$ for the irrationality measure of $\pi$;
finitely many small denominators are absorbed into $c_\pi$.  A primary
reference is D. Zeilberger and W. Zudilin,
[*The Irrationality Measure of Pi is at most
7.103205334137...*](https://arxiv.org/abs/1912.06345).

**Proof.**  Put



$$
E_a=\sum_{k=0}^{a}\frac1{k!},\qquad
 R_a=E_a+\Pi_a=\frac{P_a}{Q_a}
\tag{46}
$$



in lowest terms.  The unique rational solution line of (43) is generated
by



$$
\bigl(-T_a(e^z+J),\,1,\,1\bigr).
\tag{47}
$$



Suppose clearing and full primitivization scales the two constants to an
integer $m\ne0$.  Its raw endpoint pair is



$$
\left(-\frac{mP_a}{Q_a},\,m\right).
\tag{48}
$$



The first coordinate is an integer, so $Q_a\mid m$.  Since
$\gcd(P_a,Q_a)=1$, the gcd of the two coordinates in (48) is
$|m|/Q_a$.  Therefore the separately reduced endpoint is exactly



$$
L_a=Q_a(e+\pi)-P_a
\tag{49}
$$



up to sign.  This proves that later coefficient clearing cannot conceal
an additional endpoint gcd.

Write $E_a=r_a/q_a$ in lowest terms.  The exponential Taylor tail and
the trivial divisibility $q_a\mid a!$ give



$$
\frac1{(a+1)!}<e-E_a<\frac2{(a+1)!},
 \qquad q_a\leq a!.
\tag{50}
$$



Applying the first inequality in (45) to $E_a$, and using
$\log(2q_a)\leq\log(2a!)$, yields



$$
q_a^2>
 \frac{c_e(a+1)!}{2\log(2a!)},
\tag{51}
$$



so Stirling's formula gives



$$
\log q_a\geq\frac12a\log a-O(a).
\tag{52}
$$



Because $E_a=R_a-\Pi_a$, the reduced denominator $q_a$ divides
$\operatorname{lcm}(Q_a,D_a)$.  No coprimality assumption is needed.
Thus



$$
q_a\leq Q_aD_a,
\tag{53}
$$



and (42), (52) imply



$$
\log Q_a\geq\frac12a\log a-O_J(a).
\tag{54}
$$



The second inequality in (45) and (42) give



$$
|\pi-\Pi_a|
 \geq c_\pi D_a^{-36/5}
 \geq\exp(-O_J(a)).
\tag{55}
$$



By (50),



$$
|e-E_a|=\exp(-a\log a+O(a)),
\tag{56}
$$



which is at most half the lower bound in (55) for all sufficiently large
$a$.  The reverse triangle inequality, with no sign assumption, now
gives



$$
\begin{aligned}
 |(e+\pi)-R_a|
 &=|(e-E_a)+(\pi-\Pi_a)|\\
 &\geq|\pi-\Pi_a|-|e-E_a|
 \geq\exp(-O_J(a)).
 \end{aligned}
\tag{57}
$$



Multiplying (57) by the denominator lower bound (54), and using (49),
proves (44). $\square$

Only rationality of the Taylor coefficients is not enough for Theorem 1:
the exponential common-denominator hypothesis (42) is essential.  The
theorem applies in particular whenever the coefficients through order
$a$ have a common denominator at most $C^a$, as in the standard
G-function denominator axiom.  Hence it covers fixed polynomial or
rational G-function pullbacks for which $J(1)=\pi$ and the pullback is
regular at the expansion point and endpoint.

## 6. Specialization of Theorem 1 to the pullback (1)

For (1), let $p=140z+z^7-z^8$.  Direct differentiation gives



$$
G'(z)=\frac{P_0(z)}{Q_0(z)}
 =\frac{560p'(z)}{p(z)^2-280p(z)+39200},
\tag{58}
$$



where, in low-to-high form,



$$
P_0(z)=78400+3920z^6-4480z^7
\tag{59}
$$



and



$$
\begin{aligned}
 Q_0(z)={}&39200-39200z+19600z^2-280z^7+560z^8-280z^9\\
 &+z^{14}-2z^{15}+z^{16}.
 \end{aligned}
\tag{60}
$$



If $G'(z)=\sum_{n\geq0}h_nz^n$, coefficient comparison gives the exact
fixed-order recurrence



$$
39200h_n=(P_0)_n-
 \sum_{j=1}^{\min(n,16)}(Q_0)_jh_{n-j}.
\tag{61}
$$



Induction in (61) proves



$$
\operatorname{den}(h_n)\mid39200^{\,n+1}.
\tag{62}
$$



Since $[z^k]G=h_{k-1}/k$ for $k\geq1$, the reduced denominator of
$\Pi_a=T_aG(1)$ divides



$$
39200^a\operatorname{lcm}(1,2,\ldots,a).
\tag{63}
$$



Chebyshev's elementary estimate
$\log\operatorname{lcm}(1,\ldots,a)=O(a)$ proves (42).  Theorem 1
therefore yields, rigorously, for the ray $(a,0,0)$,



$$
|L_a|\geq
 \exp\!\left(\frac12a\log a-O(a)\right)\longrightarrow\infty.
\tag{64}
$$



The exact continuation through $a=200$ is consistent with (64).  At



$$
a=0,2,5,10,20,50,100,150,200
\tag{65}
$$



the certified endpoint decades are respectively



$$
0,-1,0,2,11,53,135,229,330.
\tag{66}
$$



Unlike the finite patterns in Sections 3--4, conclusion (64) is an
all-degree theorem.

## 7. Reproducible artifacts and limitations

The exact source and result frozen with this note are:

- scripts/high_radius_composed_nondiagonal_probe.py  
  SHA-256:
  022444b3fc11d501c9f36369cb8d0f645fe1341e538df0736315b5e7814a04b8
- results/high_radius_composed_nondiagonal_T18.json  
  SHA-256:
  951ea7bff82ab32b0303655a2d71dc4b14c47b02ac6e6ee8dce4eb9500a697c6

The JSON embeds the source-script hash, Python version, SymPy version,
all 1330 per-triple records, 284 exact derivative jets, the
$(0,b,0)$ continuation through $250$, the constant-$B=C$
continuation through $200$, and the exact recurrence and Cauchy
certificates.

What has been proved:

- the matrix formulation and every finite assertion through $T=18$;
- the complete repeated-form obstruction on $(0,0,c)$;
- the exact all-degree formulas and recurrences on $(0,b,0)$;
- divergence of the constant-$B=C$ ray under the precise hypotheses of
  Theorem 1, including the pullback (1).

What has not been proved:

- full rank or endpoint nonvanishing for every degree triple;
- an all-degree lower bound on the primitive $(0,b,0)$ edge, because
  the gcd $d_b$ in (35) remains uncontrolled;
- any statement deciding the algebraicity or transcendence of
  $e+\pi$.
