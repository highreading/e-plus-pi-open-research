> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# An exact normalized three-dimensional recurrence in the large-prime Fourier band

Date: 2026-08-27.

## 1. Outcome and scope

Fix an even integer $n\ge2$ and an odd prime $p>2n+1$.  This note
packages all admissible one-block Fourier digits for the fixed pair
$(n,p)$ into one exact nonautonomous three-dimensional recurrence over
the Gaussian residue ring



$$
\mathcal R_p=\mathbb F_p[i]=\mathbb F_p[X]/(X^2+1).
 \tag{1}
$$



The word *ring* is intentional: when $p\equiv1\pmod4$, (1) is not a
field.  Every division made below is nevertheless valid, because its
pivot is proved to be a nonzero scalar in $\mathbb F_p$, possibly
multiplied by $i$, and hence is a unit of $\mathcal R_p$.

After removing the explicit factorial normalization from both Fourier
digits, the generic matching congruence becomes



$$
4(q_n/p)\operatorname {Im}\widetilde I_v
 =p_n\Phi_n(2v+1)\pmod p.
 \tag{2}
$$



The recurrence is exact and has dimension three, but it gives no root
count for (2) by itself.  In fact the exact case $(n,p)=(82,953)$ has
two distinct generic returns, at $K=614$ and $K=840$.  This disproves
an at-most-one-return conjecture for a fixed pair $(n,p)$.  It does not
disprove a larger uniform bound, nor does it close the unresolved
critical-Fourier matching strip.

## 2. One-block parameters and endpoint integrals

Put



$$
c=\frac{p-2n-1}{2}.
 \tag{3}
$$



For every integer $v$ with $0\le v\le c-1$, define



$$
s_v=2v+1,\qquad
 \ell_v=\frac{p+s_v}{2},\qquad
 K_v=n+\ell_v,\qquad
 u_v=p-K_v=c-v.
 \tag{4}
$$



Then



$$
K_v<p\le2(K_v-n),\qquad 1\le u_v\le c,
 \tag{5}
$$



so (4) parametrizes exactly the odd first digits in the one-block
large-prime band for the fixed pair $(n,p)$.

Use the accepted Gaussian Fourier polynomial in the form



$$
P_n(z)=(1-i)^n(z-1)^n(z-i)^n,\qquad
 R_v(z)=P_n(z)(1+z)^{2v+1}.
 \tag{6}
$$



If $f(z)=\sum_{r=0}^{p-2}f_rz^r\in\mathcal R_p[z]$, define its formal
endpoint integral by



$$
\int_1^i f(z)\,dz
 :=\sum_{r=0}^{p-2}f_r\frac{i^{r+1}-1}{r+1}.
 \tag{7}
$$



All denominators in (7) are units.  Define



$$
I_v=\int_1^i z^{u_v-1}R_v(z)\,dz
 \quad(0\le v\le c-1),
 \tag{8}
$$



and



$$
J_v=\int_1^i z^{u_v}R_v(z)\,dz
 \quad(0\le v\le c-2).
 \tag{9}
$$



The degree of the integrand in (8) is



$$
2n+c+v\le2n+2c-1=p-2,
 \tag{10}
$$



and the degree of the integrand in (9) is at most $p-2$ on its stated
range.  Thus (7)--(9) are well-defined in every case, including when
$p\equiv1\pmod4$.

Write $R_v(z)=\sum_t\rho_{v,t}z^t$.  Expanding (8) gives



$$
I_v=\sum_t\rho_{v,t}
       \frac{i^{u_v+t}-1}{u_v+t}.
 \tag{11}
$$



The definition of the accepted rational-coordinate digit $U$ therefore
gives the exact identification



$$
\boxed{U_{n,K_v,p}=\operatorname {Im}I_v.}
 \tag{12}
$$



Indeed, for $\rho=a+ib$, the imaginary part of
$\rho(i^m-1)$ is
$a\sin(m\pi/2)-b(1-\cos(m\pi/2))$, exactly the numerator used in the
definition of $U$.

## 3. The two coupled recurrences

### Theorem 3.1

For $0\le v\le c-3$, the endpoint integrals satisfy



$$
a_{0,v}I_v+a_{1,v}I_{v+1}
 +b_{0,v}J_v+b_{1,v}J_{v+1}=0,
 \tag{13}
$$



and



$$
g_{0,v}I_v+g_{1,v}I_{v+1}+g_{2,v}I_{v+2}
 +d_{0,v}J_v+d_{1,v}J_{v+1}=0,
 \tag{14}
$$



where the coefficients in $\mathcal R_p$ are the reductions of the
following Gaussian integers:



$$
\begin{aligned}
 a_{0,v}&=-(2c+3n+3)+i(-2c-n+4v+3),\\
 a_{1,v}&=i(c-v-1),\\
 b_{0,v}&=-(2c+3n+4v+7)+i(-2c-n-1),\\
 b_{1,v}&=c+2n+v+3,
\end{aligned}
\tag{15}
$$





$$
\begin{aligned}
 g_{0,v}&=(2c+3n-4v-3)+i(2c+n-8v-9),\\
 g_{1,v}&=(-c-n+v+1)+i(-4c-n+6v+9),\\
 g_{2,v}&=i(c-v-2),\\
 d_{0,v}&=(2c+3n+1)+i(2c+n-4v-5),\\
 d_{1,v}&=i(-c+v+2)=-g_{2,v}.
\end{aligned}
\tag{16}
$$



Both transition pivots are units.  More precisely,



$$
c+2n+3\le b_{1,v}\le2c+2n=p-1,
 \tag{17}
$$



and



$$
1\le c-v-2\le c-2.
 \tag{18}
$$



Consequently, (13) first determines $J_{v+1}$, and then (14)
determines $I_{v+2}$:



$$
J_{v+1}=-\frac{a_{0,v}I_v+a_{1,v}I_{v+1}+b_{0,v}J_v}{b_{1,v}},
 \tag{19}
$$





$$
I_{v+2}=-\frac{g_{0,v}I_v+g_{1,v}I_{v+1}
                   +d_{0,v}J_v+d_{1,v}J_{v+1}}{g_{2,v}}.
 \tag{20}
$$



Thus (19)--(20) are an exact first-order transition on the
three-dimensional state



$$
(I_v,I_{v+1},J_v)\longmapsto(I_{v+1},I_{v+2},J_{v+1}).
 \tag{21}
$$



When $c<3$, the index range in the theorem is empty and the assertion
is vacuous.

### Proof, including the boundary audit

Set



$$
A(z)=P_n(z)(1+z)z^{c-1},\qquad
 w(z)=\frac{(1+z)^2}{z}.
 \tag{22}
$$



Then



$$
A(z)w(z)^v=z^{c-v-1}R_v(z)=z^{u_v-1}R_v(z).
 \tag{23}
$$



The two rational logarithmic derivatives are



$$
\frac{A'}A=\frac n{z-1}+\frac n{z-i}
             +\frac1{z+1}+\frac{c-1}{z},
 \qquad
 \frac{w'}w=\frac2{z+1}-\frac1z.
 \tag{24}
$$



Let



$$
\Delta=z(z+1)(z-1)(z-i),\qquad
 Q_1=\frac\Delta z=(z+1)(z-1)(z-i),
 \qquad
 Q_2=\frac\Delta{z^2}.
 \tag{25}
$$



For the full recurrence range $0\le v\le c-3$, one has
$u_v\ge3$.  Hence $Q_2Aw^v$ is a polynomial: the lowest power
$z^{u_v-1}$ in (23) cancels the sole $z^{-1}$ in $Q_2$, leaving
lowest exponent at least one.  Moreover,



$$
\deg(Aw^v)\le p-4,\quad
 \deg(Q_1Aw^v)\le p-1,\quad
 \deg(Q_2Aw^v)\le p-2.
 \tag{26}
$$



The endpoint terms are not being suppressed.  From (6), both
$Aw^v$ and $Q_jAw^v$ contain the factors
$(z-1)^n(z-i)^n$; in addition $Q_1,Q_2$ themselves contain
$(z-1)(z-i)$.  There are no endpoint poles at $1$ or $i$.  Thus,
exactly,



$$
(Q_jAw^v)(1)=(Q_jAw^v)(i)=0
 \qquad(j=1,2).
 \tag{27}
$$



The degree bounds (26) permit formal differentiation and integration in
characteristic $p$, so (7) and (27) give



$$
0=\int_1^i (Q_jAw^v)'\,dz
  =\int_1^i Aw^v
   \left(Q_j'+Q_j\left(\frac{A'}A+v\frac{w'}w\right)\right)dz.
 \tag{28}
$$



For completeness, the coefficient reduction in (28) is the pair of
exact rational-function identities



$$
Q_1'+Q_1\left(\frac{A'}A+v\frac{w'}w\right)
 =a_{0,v}+a_{1,v}w+b_{0,v}z+b_{1,v}zw,
 \tag{29}
$$





$$
Q_2'+Q_2\left(\frac{A'}A+v\frac{w'}w\right)
 =g_{0,v}+g_{1,v}w+g_{2,v}w^2+d_{0,v}z+d_{1,v}zw.
 \tag{30}
$$



Substitution of (15)--(16) verifies (29)--(30) after using only



$$
z^{-1}=w-2-z,\qquad z^2=(w-2)z-1.
 \tag{31}
$$



Multiplying the basis terms in (29)--(30) by $Aw^v$, and applying
(8)--(9), gives respectively (13) and (14).

It remains to justify both divisions, rather than merely observe that
the displayed coefficients are nonzero Gaussian residues.  As $v$
runs from $0$ to $c-3$, the ordinary integer $b_{1,v}$ runs from
$c+2n+3$ through $p-1$; hence its residue is a nonzero element of
$\mathbb F_p$, whose inverse is also an inverse in $\mathcal R_p$.
Similarly $c-v-2$ runs from $c-2$ down to $1$, so
$g_{2,v}=i(c-v-2)$ has inverse
$-i(c-v-2)^{-1}$.  This proves both pivot-unit claims and completes the
proof. $\square$

## 4. Exact factorial normalization

Define the exceptional-digit polynomial



$$
\Phi_n(X)=\sum_{h=0}^{n/2}
 \binom n{2h}\frac{(2n-2h)!n!}{(n-h)!}
 2^h\prod_{t=1}^{h}(X+2t-1).
 \tag{32}
$$



The exact digit-polynomial theorem gives, for the parameters (4),



$$
D_v:=D_{n,K_v,p}=\kappa_v\Phi_n(2v+1),
 \qquad
 \kappa_v=-\frac{(2v+1)!}{n!\ell_v!K_v!}
 \in\mathbb F_p^\times.
 \tag{33}
$$



Every factorial argument in (33) is in $[0,p-1]$, so the normalization
is a unit.  Its consecutive ratio is exactly



$$
\lambda_v:=\frac{\kappa_{v+1}}{\kappa_v}
 =\frac{(2v+2)(2v+3)}{(\ell_v+1)(K_v+1)}
 \quad(0\le v\le c-2),
 \tag{34}
$$



and put



$$
\mu_v:=\frac{\kappa_{v+2}}{\kappa_v}
 =\lambda_v\lambda_{v+1}
 \quad(0\le v\le c-3).
 \tag{35}
$$



All four factors displayed in (34), and hence $\lambda_v,\mu_v$, are
units on their stated ranges.  Set



$$
\widetilde I_v=\kappa_v^{-1}I_v,\qquad
 \widetilde J_v=\kappa_v^{-1}J_v.
 \tag{36}
$$



Substitution into (13)--(14), followed by division by $\kappa_v$, gives
the fully normalized equations



$$
a_{0,v}\widetilde I_v
 +a_{1,v}\lambda_v\widetilde I_{v+1}
 +b_{0,v}\widetilde J_v
 +b_{1,v}\lambda_v\widetilde J_{v+1}=0,
 \tag{37}
$$





$$
g_{0,v}\widetilde I_v
 +g_{1,v}\lambda_v\widetilde I_{v+1}
 +g_{2,v}\mu_v\widetilde I_{v+2}
 +d_{0,v}\widetilde J_v
 +d_{1,v}\lambda_v\widetilde J_{v+1}=0.
 \tag{38}
$$



The normalized pivots $b_{1,v}\lambda_v$ and
$g_{2,v}\mu_v$ are units by (17)--(18) and (34)--(35).  Therefore the
normalized three-state transition is explicitly



$$
\widetilde J_{v+1}=
 -\frac{a_{0,v}\widetilde I_v
       +a_{1,v}\lambda_v\widetilde I_{v+1}
       +b_{0,v}\widetilde J_v}
       {b_{1,v}\lambda_v},
 \tag{39}
$$





$$
\widetilde I_{v+2}=
 -\frac{g_{0,v}\widetilde I_v
       +g_{1,v}\lambda_v\widetilde I_{v+1}
       +d_{0,v}\widetilde J_v
       +d_{1,v}\lambda_v\widetilde J_{v+1}}
       {g_{2,v}\mu_v}.
 \tag{40}
$$



If $v_p(q_n)=1$, write $\bar q_n=q_n/p\pmod p$.  Combining
(12), (33), and the accepted generic matching criterion yields



$$
4\bar q_n\operatorname {Im}I_v=p_nD_v
 \quad\Longleftrightarrow\quad
 \boxed{
 4\bar q_n\operatorname {Im}\widetilde I_v
 =p_n\Phi_n(2v+1)}
 \pmod p.
 \tag{41}
$$



This checks both the sign and every factorial in the normalization.

## 5. A rigorous two-return obstruction

The exact Bessel recurrence gives



$$
q_{82}\equiv141997=953\cdot149\pmod{953^2},
 \qquad p_{82}\equiv662\pmod{953}.
 \tag{42}
$$



Thus $v_{953}(q_{82})=1$ and $\bar q_{82}=149$.  There are two
distinct generic solutions of (41):



$$
\begin{array}{c|c|c|c|c|c|c}
v&s&K&D&U&4\bar qU&p_{82}D\\ \hline
55&111&614&405&210&317&317\\
281&563&840&402&632&237&237
\end{array}
\qquad(\bmod 953).
\tag{43}
$$



Both $D$ and $U$ are nonzero in both rows.  The normalization in
(33)--(41) is checked independently by



$$
\begin{array}{c|c|c|c|c|c}
v&\kappa_v&\Phi_n(2v+1)&\operatorname {Im}\widetilde I_v
 &4\bar q\operatorname {Im}\widetilde I_v&p_n\Phi_n(2v+1)\\ \hline
55&49&300&685&376&376\\
281&819&950&422&873&873
\end{array}
\qquad(\bmod 953).
\tag{44}
$$



The companion certificate evaluates every one of the $c=394$
admissible residues for this fixed pair and finds that the full target
residual



$$
F_v=4(q_{82}/953)U_v-p_{82}D_v
 \tag{45}
$$



vanishes exactly at $v=55,281$.  Thus the zeros in (43) are isolated.

The exact logical consequences are as follows.

* Equations (37)--(40) establish an explicit three-dimensional,
  first-order, nonautonomous linear recurrence with coefficients rational
  in the discrete parameter after the factorial normalization.
* Equations (42)--(45) disprove the assertion that, for fixed
  $(n,p)$, the generic matching target can be hit at most once.  Because
  the two zeros are isolated, they also disprove a homogeneous scalar
  first-order law $F_{v+1}=r_vF_v$ with a unit $r_v$ throughout this
  example.
* The calculation does **not** rule out a scalar recurrence of order two
  or three, a useful adjoint or Wronskian identity, an at-most-$C$
  theorem with $C\ge2$, or any weaker asymptotic bound on the number or
  product of surviving primes.  A nonautonomous three-state recurrence
  alone supplies no such zero bound.

## 6. Exact certificate and reproducibility

The companion script independently performs the following tasks using
only integer arithmetic in $(\mathbb Z/p\mathbb Z)[i]$:

1. constructs (6) directly and updates
   $R_{v+1}=R_v(1+z)^2$;
2. evaluates (8)--(9) coefficient by coefficient, with every denominator
   checked to lie in $1,\ldots,p-1$;
3. checks (13)--(14), both pivot ranges, and both reconstructed transition
   values at every admissible step;
4. checks (32)--(38), including the exact $\kappa$, $\lambda$, and
   $\mu$ ratios, at every step;
5. scans the target residuals and verifies (42)--(44), including the two
   and only two zeros for $(82,953)$.

Run

    python -m py_compile scripts/critical_fourier_normalized_three_dimensional_recurrence_certificate.py
    python scripts/critical_fourier_normalized_three_dimensional_recurrence_certificate.py

For a byte-identical rerun, use

    python scripts/critical_fourier_normalized_three_dimensional_recurrence_certificate.py \
      --output /tmp/critical_fourier_normalized_three_dimensional_recurrence_certificate.json
    cmp results/critical_fourier_normalized_three_dimensional_recurrence_certificate.json \
      /tmp/critical_fourier_normalized_three_dimensional_recurrence_certificate.json

The symbolic identities (29)--(30) and the recurrence theorem are
all-parameter statements.  The two-return result is a rigorous finite
counterexample.  Neither is evidence for an unproved all-$k$ closure or
for an arithmetic classification of $e+\pi$.
