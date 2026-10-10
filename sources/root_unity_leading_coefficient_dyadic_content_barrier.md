> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A leading-coefficient content cap for the corrected root-of-unity endpoint

## An exact power-of-two subfamily and the remaining two-coefficient obstruction

Checked: 2026-08-27 UTC

## 1. Scope and verdict

This note studies the arithmetic normalization (39) of
`sources/root_unity_corrected_exterior_primitive_height_audit.md` on the
infinite subfamily



$$
m=3,\qquad D=2,\qquad h=2^q,\qquad n=h-1,
 \qquad q\ge2.                                             \tag{1}
$$



Thus $n$ is odd and $n\ge D$.  The centered checkerboard theorem and
endpoint normality make the saturated endpoint exterior vector especially
simple:



$$
p=e_0\wedge e_2.                  \tag{2}
$$



Choose the corresponding endpoint basis



$$
C(z)=1,\qquad D(z)=z^2.            \tag{3}
$$



The corrected exterior polynomial is



$$
\Delta(z)=2z-\beta_{z^2}(z)+z^2\beta_1(z),               \tag{4}
$$



and the top-cardinal theorem gives



$$
\deg\Delta=n+D=h+1.               \tag{5}
$$



This note proves an exact formula and valuation for the leading
coefficient.

> **Leading-coefficient theorem.**  In (1), there is an explicitly defined
> odd integer $u_h\ne0$ such that
> 

$$
> \boxed{
> [z^{h+1}]\Delta
> =-\frac{u_h}{2^{h+q+1}(h-1)!},
> \qquad
> v_2([z^{h+1}]\Delta)=-2h.}                              \tag{6}
>
$$



Let $q_\Delta$ and $\mathfrak c_\Delta$ be the intrinsic minimal
denominator and cleared content in item (39) of the primitive-height audit.
Write (6) in lowest terms as $N_h/D_h$.  Then



$$
\boxed{
 2^{2h}\mid q_\Delta,qquad
 \mathfrak c_\Delta\mid N_h,qquad
 2\nmid\mathfrak c_\Delta.}                               \tag{7}
$$



In particular, the leading coefficient gives a genuine total corrected-
content cap,



$$
\mathfrak c_\Delta\le |N_h|,          \tag{8}
$$



and the explicit estimate below gives



$$
\log\mathfrak c_\Delta
                         =O(h\log h).                      \tag{9}
$$



For the universal integer clearing $Q=Q_{3,h-1}$, if
$\mathfrak c_Q=\operatorname {cont}(Q\Delta)$, then



$$
\boxed{
 v_2(\mathfrak c_Q)\le v_2(Q)-2h.}                        \tag{10}
$$



This is useful but does **not** close the arithmetic route.  The leading
coefficient alone allows the worst cases
$\mathfrak c_\Delta=|N_h|$ and $q_\Delta=D_h$, in which the primitive
leading coefficient has absolute value one.  Therefore it supplies no
nontrivial primitive-height lower bound without a gcd theorem involving a
second coefficient.  The exact finite rows have
$\mathfrak c_\Delta=1$, but that observation is not extrapolated.

No conclusion about the arithmetic nature of $e+\pi$ is claimed here.

The deterministic replay files are

* `scripts/root_unity_leading_coefficient_dyadic_content_certificate.py`;
* `results/root_unity_leading_coefficient_dyadic_content_certificate.json`.

## 2. Saturated endpoint normalization

For $D=2$, the endpoint matrix has one row and three columns.  In (1),
the centered checkerboard rule gives



$$
K=(0,K_{0,1},0).                  \tag{11}
$$



Endpoint normality says $K_{0,1}\ne0$.  Hence



$$
\ker K\cap\mathbb Z^3=\mathbb Ze_0\oplus\mathbb Ze_2,   \tag{12}
$$



which is already saturated.  Its primitive Pluecker vector is (2), with no
hidden rational-nullspace scale.

For the basis (3),



$$
W(C,D)=2z,qquad
 \Gamma_{C,D}=\beta_{z^2}-z^2\beta_1.                    \tag{13}
$$



Since $\deg\beta_C\le n=h-1$, only the last term in (13) can contribute
to degree $h+1$.  With the cardinal-row convention



$$
E_{b,a}=[z^b]\beta_{z^a}=-\mathcal L(\Lambda_b^{(a)}),   \tag{14}
$$



we get the exact leading coefficient



$$
[z^{h+1}]\Delta=E_{h-1,0}
                    =-\mathcal L(\Lambda_{h-1}).          \tag{15}
$$



## 3. Explicit top cardinal

Put



$$
\Phi(X)=\{X(X-1)(X-2)\}^h.                              \tag{16}
$$



Because $h$ is even, the top-cardinal residue formula is



$$
\frac{\Lambda_{h-1}(X)}{\Phi(X)}
 =\frac1{(h-1)!}
 \left\{
  \frac1{2^hX}-\frac1{X-1}+\frac1{2^h(X-2)}
 \right\}.                                               \tag{17}
$$



Define the integer polynomial



$$
\begin{aligned}
 A_h(X)
 &=\frac{\Phi(X)}X+\frac{\Phi(X)}{X-2}
        -2^h\frac{\Phi(X)}{X-1}\\
 &=2X^{h-1}(X-1)^{h+1}(X-2)^{h-1}
   -2^hX^h(X-1)^{h-1}(X-2)^h.                            \tag{18}
 \end{aligned}
$$



Then



$$
\Lambda_{h-1}(X)=\frac{A_h(X)}{2^h(h-1)!},
 \qquad
 [z^{h+1}]\Delta=-\frac{\mathcal L(A_h)}{2^h(h-1)!}.     \tag{19}
$$



Equation (18) also shows that every coefficient of $A_h$ is even.

## 4. The unique minimal dyadic term

The logistic moments are



$$
\mu_0=\frac12,\qquad \mu_{2s}=0\ (s\ge1),
 \qquad
 \mu_{2s-1}=-\frac{(2^{2s}-1)B_{2s}}{2s}.                \tag{20}
$$



Von Staudt--Clausen gives $v_2(B_{2s})=-1$.  Therefore



$$
v_2(\mu_{2s-1})=-2-v_2(s).        \tag{21}
$$



The polynomial $A_h$ has degree at most $3h-1$, so only
$s\le3h/2$ occurs in $\mathcal L(A_h)$.  Since $h=2^q$, the unique
integer in that range with $2$-adic valuation $q$ is $s=h$; every
other $s$ has valuation at most $q-1$.

It remains to inspect the coefficient of $X^{2h-1}$.  Put



$$
B_h=X^{h-1}(X-1)^{h+1}(X-2)^{h-1}.                      \tag{22}
$$



Modulo two,



$$
B_h\equiv X^{2h-2}(X+1)^{h+1}\pmod2.                   \tag{23}
$$



Thus



$$
[X^{2h-1}]B_h\equiv {h+1\choose1}=h+1\equiv1\pmod2.   \tag{24}
$$



The second summand in (18) is divisible by $2^h$, with $h\ge4$.
Consequently,



$$
v_2([X^{2h-1}]A_h)=1.             \tag{25}
$$



The $s=h$ summand in $\mathcal L(A_h)$ therefore has valuation
$-q-1$.  Every other nonzero odd-degree summand has valuation at least



$$
1-2-(q-1)=-q.                    \tag{26}
$$



The minimum is unique, so cancellation is impossible:



$$
v_2(\mathcal L(A_h))=-q-1.        \tag{27}
$$



More explicitly, if $T_{2s-1}\in\mathbb Z$ is the signless tangent
number, then



$$
\mu_{2s-1}=\frac{(-1)^sT_{2s-1}}{2^{2s}}. \tag{27a}
$$



Thus all logistic moments are dyadic rationals.  Hence



$$
u_h:=2^{q+1}\mathcal L(A_h)       \tag{28}
$$



is an odd nonzero integer.  Legendre's formula and the binary expansion of
$h-1=2^q-1$ give



$$
v_2((h-1)!)=h-1-q.               \tag{29}
$$



Substitution of (27)--(29) into (19) proves (6).

## 5. Minimal denominator and corrected content

Let



$$
g_h=\gcd(|u_h|,(h-1)!),
 \qquad
 N_h=-\frac{u_h}{g_h},
 \qquad
 D_h=\frac{2^{h+q+1}(h-1)!}{g_h}.                        \tag{30}
$$



Because $u_h$ is odd, (30) is the reduced form of (6).  Equation (29)
gives



$$
v_2(D_h)=2h.                     \tag{31}
$$



The intrinsic denominator $q_\Delta$ is a common denominator of all
coefficients, so $D_h\mid q_\Delta$.  This proves the first assertion in
(7).

We use a general elementary fact.  If $q$ is the least common denominator
of a finite rational vector and $c$ is the gcd after multiplication by
$q$, then



$$
\gcd(q,c)=1.                 \tag{32}
$$



Indeed, for every prime dividing $q$, some reduced coordinate denominator
contains its full exponent in $q$, so that cleared coordinate is a unit at
that prime.

Now $\mathfrak c_\Delta$ divides the cleared leading coefficient



$$
\frac{q_\Delta}{D_h}N_h.          \tag{33}
$$



By (32), $\mathfrak c_\Delta$ is coprime to
$q_\Delta/D_h$.  It follows that



$$
\mathfrak c_\Delta\mid N_h.       \tag{34}
$$



Since $2\mid q_\Delta$, equation (32) also makes
$\mathfrak c_\Delta$ odd.  This proves the rest of (7) and (8).

For the universal clearing, equation (41) of the primitive-height audit is



$$
\mathfrak c_Q
 =\frac{Q}{q_\Delta}\mathfrak c_\Delta.                  \tag{35}
$$



Equations (31)--(32) immediately give (10).

## 6. Explicit size of the numerator cap

Indeed, the Bernoulli--zeta formula gives



$$
|\mu_{2s-1}|=
 \frac{2(1-2^{-2s})\zeta(2s)}{\pi^{2s}}(2s-1)!
 \le\frac{(2s-1)!}{2},                                   \tag{35a}
$$



while $\mu_{2s}=0$ for $s\ge1$ and $|\mu_0|=1/2$.
Thus the elementary bound $|\mu_r|\le r!/2$ gives



$$
|u_h|\le 2^q(3h-1)!\,\|A_h\|_1.                        \tag{36}
$$



From the two products in (18),



$$
\|A_h\|_1
 \le 2^{h+2}3^{h-1}+2^{2h-1}3^h.                        \tag{37}
$$



Consequently,



$$
\boxed{
 \mathfrak c_\Delta
 \le |N_h|\le|u_h|
 \le2^q(3h-1)!
       \left(2^{h+2}3^{h-1}+2^{2h-1}3^h\right).}         \tag{38}
$$



This proves (9) with a fully explicit constant.

For comparison, the universal clearing in this subfamily is



$$
Q=2^{3h}
   \left(\prod_{a=0}^{h-1}a!\right)^3 2^{h^2}.            \tag{39}
$$



The binary digit-sum identity on a complete block of length $h=2^q$
gives



$$
\sum_{a=0}^{h-1}v_2(a!)
 =\frac{h(h-1-q)}2.                                      \tag{40}
$$



Hence



$$
\begin{aligned}
 v_2(Q)&=\frac{5h^2+3h-3qh}{2},\\
 v_2(\mathfrak c_Q)&\le
       \frac{5h^2-h-3qh}{2}.                             \tag{41}
 \end{aligned}
$$



Thus the leading coefficient proves that at least $2h$ dyadic powers in
the universal clearing cannot survive in the corrected content.  This loss
is only linear in $h$, whereas $v_2(Q)=(5/2+o(1))h^2$.

## 7. Consequence for the item-(69) threshold

Let $d=\deg\Delta=h+1$, and under the algebraicity hypothesis write



$$
\kappa=r^2(h+1)+r-1.              \tag{42}
$$



The leading coefficient gives the exact necessary content substitution



$$
\log\mathfrak c_Q
 \le \log\frac{Q}{q_\Delta}+\log|N_h|.                   \tag{43}
$$



Therefore item (69) can hold only if



$$
\begin{aligned}
 (\kappa+1)
 \left\{\log\frac{Q}{q_\Delta}+\log|N_h|\right\}
 &>\kappa\log H(N_Q)+\log(C_0H_W)\\
 &\quad-2\mathcal G_1-\log Q.                            \tag{44}
 \end{aligned}
$$



Here, exactly on (1),



$$
\mathcal G_1=(2h+2)\log\frac{2h+2}{3e\pi}
                  -(h-1)\log\pi=O(h\log h).             \tag{45}
$$



Equations (38), (41), and (45) give a precise verdict.

1. The intrinsic numerator content is at most exponential in
   $O(h\log h)$; it cannot hide a quadratic-in-$h$ dyadic content.
2. The dominant dyadic part of the universal clearing is forced denominator
   clearing.  The leading coefficient removes only $2h$ additional
   dyadic powers, a lower-order change in that ledger.
3. Most importantly, a single leading coefficient cannot lower-bound the
   primitive height.  Equations (30), (33), and (34) still permit
   

$$
q_\Delta=D_h,\qquad
      \mathfrak c_\Delta=|N_h|,
$$


   for which the primitive leading coefficient is $\pm1$.

Thus the new theorem is a valid corrected-content filter for (69), but not
a contradiction or a primitive-height theorem.  To go further one must
prove a nontrivial bound for



$$
\gcd\left(N_h, q_\Delta[z^j]\Delta\right)              \tag{46}
$$



for at least one second coefficient $j$, or determine the full intrinsic
content.  This is the precise arithmetic lemma left open by the leading-
coefficient route.

## 8. Deterministic replay and logical scope

The companion certificate uses exact rational arithmetic and less than
$0.2$ GiB of resident memory.  It

1. reconstructs $A_h$, $\mathcal L(A_h)$, $u_h$, and the reduced
   leading coefficient for $q=2,\ldots,6$;
2. verifies the unique-minimal-term valuation proof coefficient by
   coefficient;
3. checks the checkerboard endpoint row and saturated vector (2) on a
   finite exact grid; and
4. constructs the complete corrected polynomial for $h=4,8,16$, checks
   the absolute value of its leading coefficient against (6), and records
   its intrinsic content.  The full-polynomial routine canonically orients
   its primitive vector by the first nonzero coefficient, whereas (6) uses
   the fixed exterior orientation $e_0\wedge e_2$; this accounts for the
   documented possible global sign.

The exact finite contents in item 4 are diagnostic only.  The infinite
theorems are (6)--(10) and (38)--(44), proved above.
