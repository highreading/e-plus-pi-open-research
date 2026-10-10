> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The corrected root-of-unity constant border for every even number of frequencies

## Exact scalar, a nonnegative Coxian expansion, and the surviving odd central-boundary case

Checked: 2026-08-27 UTC

## 1. Verdict

Let



$$
h=n+1,\qquad
 \Phi(X)=\prod_{j=0}^{m-1}(X-j)^h,\qquad
 c=\frac{m-1}{2},                                         \tag{1}
$$



and let



$$
K_{q,a}=\mathcal L\!\left(\bigl((X-c)^q\Phi\bigr)^{(a)}\right),
 \quad0\le q\le D-2,\quad0\le a\le D                  \tag{2}
$$



be the centered endpoint matrix.  Here



$$
\mathcal L(p)=p(d/dz)\frac1{1+e^z}\bigg|_{z=0}.          \tag{3}
$$



The frozen endpoint-normality theorem gives
$\operatorname {rank}K=D-1$ for $m\ge1$ and
$n\ge D\ge2$.  If $C$ is an endpoint polynomial, write



$$
\beta_C=T_C(z,-1),\qquad
 \Gamma_{C_1,C_2}=C_1\beta_{C_2}-C_2\beta_{C_1},
\qquad
 \Delta_{C_1,C_2}=W(C_1,C_2)-\Gamma_{C_1,C_2}.             \tag{4}
$$



The sign in (4) is essential: with
$W(F,G)=FG'-GF'$, this is the polynomial satisfying
$\Delta(i\pi)=W(R_{C_1},R_{C_2})(i\pi)$.

This note proves:

> **Even-frequency corrected-border theorem.**  For every even
> $m\ge2$ and every $n\ge D\ge2$, the corrected polynomial
> $\Delta$ attached to an oriented basis of $\ker K$ is nonzero.  More
> precisely,
> 

$$
>                         [z^0]\Delta\ne0.                 \tag{5}
>
$$



The proof uses the all-parameter positive pole-truncation theorem, not a
finite extrapolation.  If $m=2k$ and



$$
\Lambda_0(c+U)=U N_{m,n}(-U^2),                           \tag{6}
$$



then the corrected row replaces $N_{m,n}$ by exactly
$N_{m,n}+2$.  With
$\sigma=(-1)^k$, every raw ordered repeated-rate Newton coefficient of
$N_{m,n}$ has sign $\sigma$, and the first one is exactly



$$
\gamma_0=2\sigma.                 \tag{7}
$$



Thus the modification either changes $\gamma_0$ from $2$ to $4$, or
changes it from $-2$ to zero.  Every coefficient after $\gamma_0$
remains strict with the same sign.  The normalized rational quotient is
therefore still strictly completely monotone, even in the zero-first-
coefficient case.  The same divided-difference/Andreief argument as in the
frozen augmented-border proof gives (5).

There are two additional exact conclusions.

1. In the separate parity defect (necessarily $m,n$ odd and $D$ even),
   where both endpoint directions are even,
   

$$
\boxed{[z^1]\Delta\ \doteq\
       \det\!\begin{pmatrix}K\\ e_0^T\\2e_2^T-E_1\end{pmatrix}.} \tag{8}
$$


   The factor $2$ and the minus sign are exact.

2. Combining (5) with the independent top-cardinal degree theorem leaves
   only
   

$$
\boxed{m\ge3\text{ odd},\quad n\text{ even},
                     \quad D\text{ odd}}                  \tag{9}
$$


   outside the presently proved universal $\Delta\ne0$ regimes.

The new canonical-product theorem does not by itself settle (9).  In that
family the corrected centered row contains a genuine low central jet
$2U$, rather than a polynomial perturbation of the transformed numerator.
This is an exact boundary obstruction, not merely a missing numerical check.

No conclusion about the arithmetic nature of $e+\pi$ is claimed here.

The deterministic replay files are

* `scripts/root_unity_corrected_low_border_even_m_certificate.py`;
* `results/root_unity_corrected_low_border_even_m_certificate.json`.

## 2. Exact low coefficients of the corrected exterior form

Let $E_b$ denote the row



$$
E_{b,a}=[z^b]\beta_{z^a}
         =-\mathcal L(\Lambda_b^{(a)}),                    \tag{10}
$$



where the Hermite cardinal polynomial is determined by



$$
\Lambda_b^{(a)}(j)=(-1)^j\delta_{ab},
 \qquad0\le j<m,\quad0\le a,b\le n.                       \tag{11}
$$



Outside the parity defect, endpoint normality splits $\ker K$ into one
even line and one odd line.  Choose an even endpoint $C$ and an odd
endpoint $Q$.  Then



$$
C'(0)=Q(0)=0,                                             \tag{12}
$$



and direct expansion gives



$$
\begin{aligned}
 [z^0]W(C,Q)&=C(0)Q'(0),\\
 [z^0]\Gamma_{C,Q}&=C(0)\beta_Q(0).
 \end{aligned}                                             \tag{13}
$$



Consequently



$$
\boxed{[z^0]\Delta_{C,Q}
       =C(0)\bigl(Q'(0)-\beta_Q(0)\bigr).}                 \tag{14}
$$



In row notation, (14) is the border



$$
\boxed{[z^0]\Delta\ \doteq\
  \det\!\begin{pmatrix}K\\e_0^T\\e_1^T-E_0\end{pmatrix}.} \tag{15}
$$



No unspecified scalar occurs inside the last row; the only $\doteq$ in
(15) is the fixed nonzero Pluecker normalization of the chosen kernel basis.

In the parity defect (an auxiliary odd-$m$ case, not a case of the
even-frequency theorem), write two even endpoints as



$$
C=c_0+c_2z^2+O(z^4),\qquad Q=q_0+q_2z^2+O(z^4).           \tag{16}
$$



Then



$$
[z^1]W(C,Q)=2(c_0q_2-q_0c_2)
             =\det\!\begin{pmatrix}e_0(C)&e_0(Q)\\
                                      2e_2(C)&2e_2(Q)
                       \end{pmatrix}.                       \tag{17}
$$



Because both endpoints have zero odd coefficients,



$$
[z^1]\Gamma_{C,Q}
   =c_0E_1(Q)-q_0E_1(C).                                   \tag{18}
$$



Subtracting (18) from (17) proves (8):



$$
\boxed{[z^1]\Delta\ \doteq\
  \det\!\begin{pmatrix}K\\e_0^T\\2e_2^T-E_1\end{pmatrix}.} \tag{19}
$$



This also fixes a possible factor-of-two ambiguity: the Wronskian
coefficient is $2e_2$, not $e_2$.

## 3. Exact polynomial representatives of the two corrected rows

The first logistic moments are



$$
\mathcal L(1)=\frac12,\qquad
 \mathcal L(X)=-\frac14,\qquad
 \mathcal L(X^2)=0.                                       \tag{20}
$$



They follow either from (3) or from the recurrence obtained by multiplying
$(1+e^z)^{-1}$ by $1+e^z$.

Set



$$
P_1(X)=2X+1.                                              \tag{21}
$$



Equation (20) gives, for every $a\ge0$,



$$
\mathcal L(P_1^{(a)})=\delta_{a1}.                        \tag{22}
$$



Since $E_{0,a}=-\mathcal L(\Lambda_0^{(a)})$, (22) proves



$$
\boxed{(e_1-E_0)_a
       =\mathcal L\!\left((\Lambda_0+2X+1)^{(a)}\right).} \tag{23}
$$



For the defect row, set



$$
P_2(X)=2X^2+2X+1
       =\frac{(2X+1)^2+1}{2}.                              \tag{24}
$$



A second direct use of (20) gives



$$
\mathcal L(P_2^{(a)})=2\delta_{a2}.                       \tag{25}
$$



Therefore



$$
\boxed{(2e_2-E_1)_a
       =\mathcal L\!\left((\Lambda_1+2X^2+2X+1)^{(a)}\right).} \tag{26}
$$



This proves both the scalar and the sign in the defect representative.

## 4. The even-$m$ corrected numerator

Let $m=2k$, so $c=k-\tfrac12$, and define



$$
B_k(x)=\prod_{r=1}^k\left(x+(r-\tfrac12)^2\right).       \tag{27}
$$



Reflection uniqueness for the cardinal jets makes $\Lambda_0(c+U)$ odd,
so there is a polynomial $N=N_{m,n}$ such that



$$
\Lambda_0(c+U)=U N(-U^2),\qquad \deg N=kh-1.             \tag{28}
$$



On odd endpoint columns, the constant part of $2X+1=2U+m$ has zero
derivative.  Hence (23) has the exact centered form



$$
\Lambda_0(c+U)+2U
     =U\bigl(N(-U^2)+2\bigr).                              \tag{29}
$$



There is no boundary term in this parity block.  The divided-difference row
in the Andreief reduction is therefore, up to one fixed nonzero phase,



$$
\widetilde\rho(x)=\frac{N(x)+2}{B_k(x)^h}. \tag{30}
$$



Thus the coefficient $+2$ in (30) is exact; it is not affected by a
cardinal normalization.

List each rate



$$
\frac14,\frac94,\ldots,(k-\tfrac12)^2                    \tag{31}
$$



exactly $h$ times, in increasing order, and write



$$
N(x)=\sum_{d=0}^{kh-1}\gamma_d
             \prod_{j=1}^{d}(x+\lambda_j).                \tag{32}
$$



The positive pole-truncation theorem proves, with
$\sigma=(-1)^k$,



$$
\sigma\gamma_d>0
       \quad(0\le d<kh).                                   \tag{33}
$$



The first coefficient is especially simple.  Evaluating (28) at
$U=\tfrac12$, so that $X=k$ is a cardinal node, gives



$$
\frac12N(-\tfrac14)=\Lambda_0(k)=(-1)^k=\sigma.           \tag{34}
$$



Every Newton basis element after the constant contains
$x+\tfrac14$.  Therefore



$$
\boxed{\gamma_0=N(-\tfrac14)=2\sigma.} \tag{35}
$$



Adding $2$ changes no coefficient except $\gamma_0$.  If
$\sigma=1$, the normalized coefficients of $N+2$ are



$$
4,\ \gamma_1,\ldots,\gamma_{kh-1}>0.     \tag{36}
$$



If $\sigma=-1$, multiply by $-1$; the normalized coefficients are



$$
0,\ -\gamma_1,\ldots,-\gamma_{kh-1},     \tag{37}
$$



and every entry after the first is strictly positive.

Dividing (32) by the full denominator turns each Newton basis term into a
reciprocal suffix product.  Equations (36)--(37) thus express
$\sigma\widetilde\rho$ as a nonzero nonnegative sum of functions



$$
\frac1{\prod_{j=d+1}^{kh}(x+\lambda_j)}.     \tag{38}
$$



Every rate is positive.  Each function in (38) is strictly completely
monotone on $(0,\infty)$, and at least one coefficient is positive.
Consequently



$$
(-1)^r(\sigma\widetilde\rho)^{(r)}(x)>0
 \quad(x>0,\ r=0,1,2,\ldots).                              \tag{39}
$$



The Hermite--Genocchi sign for the divided difference of (39), followed by
Andreief's identity, proves that the odd-column block augmented by
$e_1-E_0$ is nonzero.  The frozen shifted-coordinate theorem proves that
$e_0$ is nonzero on the even endpoint line.  The checkerboard splitting
of (15) therefore makes the full border a product of two nonzero factors.
This proves (5).

Notice that strict positivity of $\gamma_0$ was never required.  A zero
$\gamma_0$ leaves a nonzero positive inverse-Laplace density because all
later coefficients remain strict.

## 5. The exact odd central-jet obstruction

The preceding argument cannot simply be copied to odd $m$.  This is an
algebraic obstruction, not a failure of the finite data.

Let $m=2k+1$, $c=k$, and suppose first that $n$ is even.  Then
$h=n+1$ is odd, and the centered generic cardinal has the exact form



$$
\Lambda_0(c+U)=\sigma+U^{h+1}N^{(0)}(-U^2),
 \qquad\sigma=(-1)^k.                                     \tag{40}
$$



On odd columns the constant $\sigma$ is invisible, but the corrected row
is



$$
\boxed{U^{h+1}N^{(0)}(-U^2)+2U.}                          \tag{41}
$$



Its coefficient of $U$ is exactly $2$, while $h+1\ge4$.  Thus (41)
is not divisible by the common central power $U^{h+1}$.  The term $2U$
is a central boundary jet.  It is not the replacement
$N^{(0)}\mapsto N^{(0)}+2$, and the positive pole-truncation theorem,
which controls the polynomial Hermite remainder after division by the common
central power, does not compare its scalar with the continuous cardinal row.

The same issue is visible in the defect coefficient.  There
$m,n$ are odd, $h$ is even, and



$$
\Lambda_1(c+U)=\sigma U+U^{h+1}N^{(1)}(-U^2).             \tag{42}
$$



Centering (24) gives



$$
P_2(c+U)=2U^2+2mU+\frac{m^2+1}{2}.                        \tag{43}
$$



On even columns, the rows represented by $1$ and by $U$ are scalar
multiples of $e_0$:



$$
\mathcal L(1^{(a)})=\tfrac12\delta_{a0},\qquad
 \mathcal L(U^{(a)})=-\tfrac m4\delta_{a0}\quad(a\text{ even}). \tag{44}
$$



They may therefore be deleted after adjoining $e_0$.  Equations
(26), (42)--(44) show that the defect's second row is represented modulo
$e_0$ by



$$
\boxed{U^{h+1}N^{(1)}(-U^2)+2U^2.}                        \tag{45}
$$



Again, the added term has lower central order than the canonical cardinal
factor.  The all-parameter top-cardinal theorem already proves
$\Delta\ne0$ in the defect, so no defect conclusion is missing globally;
(45) merely explains why the low defect border is not an automatic corollary
of the existing pole-truncation theorem.

## 6. Combination with the top-degree theorem

The independent top-cardinal degree theorem proves



$$
[z^{n+D}]\Gamma\ne0                                      \tag{46}
$$



whenever parity permits.  Since
$\deg W\le2D-2<n+D$, it then proves
$\deg\Delta=n+D$.  Its only parity-forced families are



$$
\begin{array}{ll}
 \mathrm A:&n\text{ even},\ D\text{ odd},\quad m\text{ arbitrary},\\
 \mathrm B:&m\text{ even},\ n\text{ odd},\ D\text{ even}.
 \end{array}                                               \tag{47}
$$



The even-frequency theorem (5) resolves every even-$m$ member of both
families.  All cases outside (47), including the two-even parity defect, are
already resolved by (46).  Therefore, within the $m\ge2$ regime of the two
all-parameter theorems, the exact remaining universal nonvanishing family is
precisely (9).  The separate $m=1$ module is not reclassified here.

This is only a nonvanishing classification of the current analytic endpoint
construction.  Even a proof in (9) would not supply the primitive content or
height/value comparison needed for an arithmetic conclusion about
$e+\pi$.

## 7. Deterministic replay and logical scope

The certificate uses exact rational arithmetic only.  It

1. constructs $\Lambda_0$ and $\Lambda_1$ by polynomial CRT and verifies
   all cardinal jets;
2. on $m=2,4,6,8,10$ and $2\le n\le7$, reconstructs every ordered
   Newton coefficient, verifies (35), changes only $\gamma_0$, and checks
   (36)--(37) exactly;
3. directly computes the corrected constant border for
   $m=2,4$, $2\le n\le5$, and every $2\le D\le n$;
4. verifies the dual polynomial identities (22) and (25);
5. replays (19) on a small exact defect grid, without promoting that finite
   nonvanishing to an all-parameter low-border theorem; and
6. records at $(m,n,D)=(3,4,3)$ the nonzero linear central remainder and
   an exact determinant ratio showing that the boundary coordinate is a
   separate functional.

The finite grids are consistency checks.  The all-parameter conclusion (5)
comes from equations (28)--(39) and the already proved pole-truncation and
shifted-coordinate theorems.
