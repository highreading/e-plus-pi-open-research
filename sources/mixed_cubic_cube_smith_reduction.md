> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Cubic Smith reduction for the fixed-gap cube-support problem

Date: 2026-08-28

## 1. Scope and exact status

This note proves an algebraic reduction that is uniform in the admissible
fixed gap $q$: the cubic gcd $G_q$ divides the third determinant divisor
$\Delta _3(q)$ of an explicit $3\times6$ multiplication matrix, and hence
divides the cube of its largest Smith invariant $d_3(q)$, all away from
the primes $2$ and $3$.

The remaining assertion



$$
d_3(q)\mid P_q,
 \qquad
 P_q=\prod_{j=0}^{q-2}(2q-3-3j),                 \tag{1}
$$



is **not proved here**. A standard-library certificate gives exact finite
evidence for (1) for every positive odd $q\le1001$ with $3\nmid q$.
Consequently, this package is a reduction plus finite evidence, not a
uniform cube-support theorem.

## 2. The four coefficients and the cubic algebra

Let $q$ be a positive odd integer with $3\nmid q$, and put



$$
n=q-1,\qquad A=2q-3,\qquad K=4^n.
$$



Use the fixed-gap coefficients



$$
\begin{aligned}
C_0&=[z^n](2+z)
 \bigl((1+z)(1+z+z^2/2)\bigr)^{A/3},\\
C_1&=\frac12[z^n](2+z)^4
 \bigl((1+z)(1+z+z^2/2)\bigr)^{A/3-1},\\
T_0&=[z^n]\frac{(1+z)(1+z^2)^{A/3}}{(1-z)^q},\\
T_1&=[z^n]\frac{(1+z)^4(1+z^2)^{A/3-1}}{(1-z)^q}.
\end{aligned}                                                       \tag{2}
$$



They lie in $\mathcal R=\mathbb Z[1/6]$. Indeed, for every prime
$\ell\ne3$, the number $A/3$ is in $\mathbb Z_\ell$, and
$\binom{A/3}{k}\in\mathbb Z_\ell$; the only other denominators in
(2) come from powers of $2$. Equivalently, this follows by approximating
$A/3$ by nonnegative integers modulo a sufficiently high power of
$\ell$ in the integer-valued polynomial $\binom{x}{k}$.

Choose a common denominator $D$, supported only at $2,3$, and write



$$
(c_0,t_0,c_1,t_1)=D(C_0,T_0,C_1,T_1)\in\mathbb Z^4.              \tag{3}
$$



Multiplication by $D$ is multiplication by a unit in $\mathcal R$, so
it does not change any invariant away from $2,3$.

In the cubic algebra



$$
\mathcal A=\mathcal R[X]/(X^3-K),
 \qquad \lambda_s=c_sX-t_s,
$$



consider the map



$$
\mathcal A^2\longrightarrow\mathcal A,\qquad
 (u,v)\longmapsto\lambda_0u+\lambda_1v.
$$



In the basis $1,X,X^2$, its matrix is



$$
M_q=
\begin{pmatrix}
-t_0&0&Kc_0&-t_1&0&Kc_1\\
c_0&-t_0&0&c_1&-t_1&0\\
0&c_0&-t_0&0&c_1&-t_1
\end{pmatrix}.                                                     \tag{4}
$$



## 3. The twelve maximal-minor forms

Set



$$
\begin{aligned}
\rho&=c_0t_1-c_1t_0,\\
U_0&=t_0^3-Kc_0^3,&
U_1&=t_1^3-Kc_1^3,\\
M_{001}&=t_0^2t_1-Kc_0^2c_1,&
M_{011}&=t_0t_1^2-Kc_0c_1^2.
\end{aligned}                                                       \tag{5}
$$



Number the columns of (4) from $0$ through $5$. Direct determinant
expansion gives the following complete list, up to sign:

| maximal-minor form | column triples |
|---|---|
| $U_0$ | $012$ |
| $U_1$ | $345$ |
| $M_{001}$ | $015,024,123$ |
| $M_{011}$ | $045,135,234$ |
| $c_0\rho$ | $013$ |
| $t_0\rho$ | $014,023$ |
| $Kc_0\rho$ | $025,124$ |
| $Kt_0\rho$ | $125$ |
| $c_1\rho$ | $034$ |
| $t_1\rho$ | $035,134$ |
| $Kc_1\rho$ | $145,235$ |
| $Kt_1\rho$ | $245$ |

Thus the twelve forms account for all twenty $3\times3$ minors. The
certificate checks the signed identity for every column triple, not only
the gcd that results from them.

## 4. A DVR lemma for the two mixed cubics

**Lemma.** Let $\mathcal O$ be a DVR with valuation $v$, and suppose
$K\in\mathcal O^\times$ and
$c_0,t_0,c_1,t_1\in\mathcal O$. With (5), and with $v(0)=+\infty$, put



$$
g=\min\{v(\rho),v(U_0),v(U_1)\}.
$$



Then



$$
v(M_{001})\ge g,\qquad v(M_{011})\ge g.             \tag{6}
$$



**Proof.** First suppose the quadruple is primitive, so at least one of
its entries is a unit. If $c_0$ or $t_0$ is a unit, the identities



$$
\begin{aligned}
c_0M_{001}&=t_0^2\rho+c_1U_0,\\
t_0M_{001}&=t_1U_0+Kc_0^2\rho
\end{aligned}                                                       \tag{7}
$$



give the first inequality in (6).

It remains to treat the case in which the first pair supplies no unit.
Primitivity says that the second pair does. If $c_1$ is a unit, put
$y=t_1/c_1$. Since $t_0=c_0y-\rho/c_1$, direct expansion gives



$$
M_{001}=
 \frac{c_0^2U_1}{c_1^2}-2c_0y^2\rho+\frac{y\rho^2}{c_1}.           \tag{8}
$$



If instead $t_1$ is a unit, put $x=c_1/t_1$. Since
$c_0=xt_0+\rho/t_1$, one obtains



$$
M_{001}=
 \frac{t_0^2U_1}{t_1^2}-2Kx^2t_0\rho-\frac{Kx\rho^2}{t_1}.        \tag{9}
$$



Every term on the right side of (8) or (9) has valuation at least $g$.
This proves the assertion for $M_{001}$. Interchanging the subscripts
$0,1$ proves it for $M_{011}$; the sign change in $\rho$ is harmless.

For a nonprimitive quadruple, factor a largest common power
$\pi^h$. Then $\rho$ acquires $2h$, while
$U_0,U_1,M_{001},M_{011}$ acquire $3h$. Applying the primitive result
to the divided quadruple gives



$$
3h+\min\{v(\rho'),v(U'_0),v(U'_1)\}
\ge
\min\{2h+v(\rho'),3h+v(U'_0),3h+v(U'_1)\},
$$



which is exactly (6). This completes the proof.

## 5. The exact Smith reduction

Let $\Delta_i(q)$ be the $i$-th determinant divisor of $M_q$ over
$\mathcal R$, and let



$$
d_1=\Delta_1,\qquad d_2=\Delta_2/\Delta_1,\qquad
 d_3=\Delta_3/\Delta_2                                      \tag{10}
$$



be its Smith invariant factors, chosen up to units of $\mathcal R$.
Define the cubic gcd away from $2,3$ by



$$
G_q=\prod_{\ell>3}\ell^{
 \min\{v_\ell(\rho),v_\ell(U_0),v_\ell(U_1)\}}.                 \tag{11}
$$



This is independent of the common-denominator choice (3).

Fix a prime $\ell>3$ and apply the lemma in $\mathbb Z_\ell$. Here
$K=4^n$ is a unit. The six minors represented by the two mixed forms
have valuation at least the exponent in (11); the remaining minors are
$U_0,U_1$ or multiples of $\rho$. Therefore every maximal minor has
at least that valuation. Taking the gcd of the maximal minors and then
ranging over $\ell>3$ proves



$$
\boxed{G_q\mid\Delta_3(q)}.                                  \tag{12}
$$



Since $d_1\mid d_2\mid d_3$ and
$\Delta_3=d_1d_2d_3$, one also has



$$
\boxed{G_q\mid\Delta_3(q)\mid d_3(q)^3}.                     \tag{13}
$$



Consequently, the still-missing uniform divisibility (1) would imply



$$
\boxed{G_q\mid P_q^3}.                                      \tag{14}
$$



No claim of a uniform proof of (1), and hence no unconditional claim of
(14), is made in this package.

## 6. Conditional exclusion of compatible fresh primes

Assume (1). Let $p=6m+q$ be prime with $m\ge1$. Then $p>q$ and
$p\equiv q\pmod3$. Every factor



$$
f_j=2q-3-3j,\qquad 0\le j\le q-2,
$$



satisfies



$$
3-q\le f_j\le2q-3,\qquad f_j\equiv-q\pmod3.                  \tag{15}
$$



Because $-p<f_j<2p$, a factor divisible by $p$ could only be $0$ or
$p$. It cannot be $0$, since $3\nmid q$. If it were $p$, then
$q\equiv p=f_j\equiv-q\pmod3$, again forcing $3\mid q$. Hence



$$
p\nmid P_q.
$$



Conditionally on (1), equations (13)--(14) therefore give $p\nmid G_q$.
Equivalently, the three congruences
$\rho\equiv U_0\equiv U_1\equiv0\pmod p$ cannot hold together for a
compatible fresh prime. The word “conditionally” is essential here.

## 7. Reproducible finite evidence

The companion file mixed_cubic_cube_smith_certificate.py uses only the
Python standard library and exact rational/integer arithmetic. Its audited
run checks all 334 admissible $q\le1001$. For every such $q$, it
verifies:

1. the common coefficient denominator has support only at $2,3$;
2. all twenty signed maximal-minor identities in Section 3;
3. the Smith divisibility chain;
4. $G_q\mid\Delta_3(q)$;
5. $d_3(q)\mid P_q$ and $G_q\mid P_q^3$ in this finite range.

The largest prime-to-$6$ representative of $d_3$ encountered has 837
bits. The JSON records selected rows and a SHA-256 digest of the complete
witness stream. Reproduce it with

    python mixed_cubic_cube_smith_certificate.py --max-q 1001 --output mixed_cubic_cube_smith_certificate_q1001.json

Items 1--4 mirror uniform algebraic facts proved above. Item 5 remains
finite evidence only. Proving $d_3(q)\mid P_q$ for every admissible
$q$ is precisely the open step left by this reduction.
