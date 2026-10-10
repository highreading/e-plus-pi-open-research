> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Asymptotic capacity of the corrected root-of-unity exterior endpoint

## Exact content thresholds, scalable parameter regimes, and a conditional
## fixed-quadratic parity-pair survivor

Checked: 2026-08-27 UTC

## 1. Verdict

Put



$$
M=m(n+1),\qquad L=M+D-1,\qquad
 A_{\rm an}=L-n=(m-1)n+m+D-1,                              \tag{1}
$$



where throughout the proved constrained construction



$$
m\ge2,\qquad n\ge D\ge2.           \tag{2}
$$



The optimized one-column Schwarz gain is



$$
\mathcal G_1=A_{\rm an}
       \log\frac{A_{\rm an}}{e\pi m}-n\log\pi,             \tag{3}
$$



when the stationary radius $A_{\rm an}/m$ is larger than $\pi$.
The corrected two-column value estimate has analytic gain
$2\mathcal G_1$, not a larger exterior-power gain.

This audit proves the following statements.

1. The denominator in the frozen primitive-height audit satisfies the
   all-parameter inequality

   

$$
\boxed{2\mathcal G_1<\log Q_{m,n}}.       \tag{4}
$$



   If the stationary radius is not admissible, the boundary Schwarz
   estimate is weaker, so it does not create an omitted favorable case.

2. There are basis-free universal coefficient majorants.  With the
   notation defined in Section 3,

   

$$
\boxed{
   \begin{aligned}
    H(N_Q)&\le \widehat H_N
       :=P_0\{Q\omega_D+D(D+1)mC_B\},\\
    H\!\left(W(\overline R_C,\overline R_D)\right)
       &\le \widehat H_W
       :=2R_D(m+1)(n+1)(n+m)P_0(Q+2C_B)^2.
   \end{aligned}}                                          \tag{5}
$$



   Here $p=C\wedge D$ is the primitive saturated Pluecker vector;
   the bound is linear in $H(p)$, rather than quadratic in the height
   of an arbitrarily chosen lattice basis.

3. Let

   

$$
\chi=\log\mathfrak c_Q,
       \qquad \kappa=r^2d+r-1,                              \tag{6}
$$



   where $r=[\mathbb Q(e+\pi):\mathbb Q]$ under the temporary
   algebraicity hypothesis and $d=\deg P_\Delta$.  Substitution of (5)
   into the leading algebraic-number lower bound can certify a
   contradiction only if

   

$$
\boxed{
   (\kappa+1)\chi>
      \kappa\log\widehat H_N+
      \log\{(2m+1)(2n+1)\widehat H_W\}
      -2\mathcal G_1-\log Q.}                              \tag{7}
$$



   The only currently proved all-parameter lower bound is
   $\chi\ge0$.  With $\chi=0$, (4)--(5) make the certified absolute
   smallness exponent strictly negative.  Thus the present universal
   bounds do not even certify $|P_\Delta(i\pi)|<1$, let alone beat an
   algebraic-number lower bound.  This is a statement about what the
   proved bounds certify.  It is not a lower bound for the true endpoint
   value, and it does not exclude cancellations not captured by (5).

4. In every presently proved exact-degree family,

   

$$
d=n+D\quad\hbox{or}\quad d=n+D-1.                    \tag{8}
$$



   On any quadratic noncollapse regime satisfying (48), the relative Schwarz
   exponent is $O(1/n)$ when $n\to\infty$, uniformly in $m,D$.
   The easiest algebraic threshold is already $d+1\gg n$.  The analytic
   component alone is short by a factor of order at least $n^2$.  If $n,D$
   are fixed and $m\to\infty$, the relative capacity is
   $O_{n,D}(1/(m\log m))$, so growing the number of frequencies is also
   unfavorable.

5. In the two even-$m$ forced-parity families, only
   $\Delta\ne0$ and $d\le n+D$ are currently proved.  No stronger
   degree statement is assumed here.  If a sharper computation supplies a
   relative exponent $\Theta$, then a degree collapse can help the
   degree-$r$ algebraicity comparison exactly when

   

$$
\boxed{d<\frac{\Theta-r}{r^2}.}          \tag{9}
$$



   Under the quadratic noncollapse hypothesis (48), $\Theta=o(1)<r$, so even a
   hypothetical collapse to degree zero would not suffice by itself.
   With the present universal majorants and no content theorem, the
   certified absolute exponent is negative, so no nonnegative degree can
   help.

6. A different, presently **conditional**, regime deserves separate
   attention.  In the unconstrained endpoint space of dimension
   $\nu=n+1$, take even $n=D$ and a parity pair consisting of one odd
   and one even endpoint.  Exact $n=4$ computations suggest degree
   $d=2$ and origin order $2M$ for the Wronskian.  The parity-Segre
   geometry and the exact $n=6,8$ eliminants described in Section 9
   give evidence against persistence of a rational branch.  No all-even-
   $n$ existence, degree, or height theorem is asserted here.  If those
   statements hold and the intrinsic exteriorly normalized coefficient
   costs are

   

$$
\log H_W^{\rm int}=a\,n\log n+o(n\log n),\qquad
       \log H(P_\Delta)=b\,n\log n+o(n\log n),              \tag{10}
$$



   then fixed $m$ can beat the degree-two measure precisely at leading
   order when

   

$$
\boxed{a+(2r^2+r-1)b<2(m-1).}                 \tag{11}
$$



   In the matched quadratic model
   $a=b=2\lambda$, the required one-column intrinsic height exponent is

   

$$
\boxed{\lambda<\frac{m-1}{2r^2+r}.}     \tag{12}
$$



   The universal Cramer majorant has logarithm of order
   $n^2\log n$ for fixed $m$, a full factor $n$ above the analytic
   gain.  Therefore it cannot prove (11); an intrinsic saturated
   height/content theorem is essential.  Conversely, because the Cramer
   estimate is only an upper bound, its size does not disprove the
   conditional parity-pair route.

7. Allowing a rational **sum** of endpoint Wronskians removes the
   decomposability requirement altogether.  In an endpoint space of
   dimension $\nu$, the exterior domain has
   $N=\binom{\nu}{2}$ rational variables.  If
   $N>S:=n+D-d$, ordinary rational linear algebra can kill every
   corrected coefficient above a fixed target degree $d$.  Taking
   $N\sim\tau S$, $\tau>1$, needs only $\nu=O(\sqrt n)$, so the
   origin order loses $O(\sqrt n)$, while the elementary Siegel exponent
   becomes $S/(N-S)\sim1/(\tau-1)$.  This is a genuine dimensional
   improvement.  It does not by itself solve the height problem: the
   current Cramer majorant still has logarithm $O(n^2\log n)$ for fixed
   $m$, against analytic gain $O(n\log n)$.  If an intrinsic
   saturation theorem instead gives Wronskian and primitive endpoint
   exponents $a\,n\log n$ and $b\,n\log n$, the sharp conditional
   fixed-$d$ requirement is

   

$$
\boxed{a+(r^2d+r-1)b<2(m-1+\delta),\qquad
              D/n\to\delta\in[0,1].}                       \tag{12a}
$$



   In a matched quadratic model $a=b=2\lambda$, this becomes
   $\lambda<(m-1+\delta)/(r^2d+r)$.  A separate nonvanishing/rank-gap
   theorem is also required: a vector killing the high coefficients could
   otherwise kill the entire corrected polynomial.

No conclusion about the arithmetic nature of $e+\pi$ is claimed.

## 2. Denominator and analytic notation

The proved common clearing denominator is



$$
\boxed{
 Q=Q_{m,n}=2^M\mathscr V_{m,n},\qquad
 \mathscr V_{m,n}=
 \left(\prod_{a=0}^{n}a!\right)^m
 \prod_{h=1}^{m-1}h^{(m-h)(n+1)^2}.}                       \tag{13}
$$



Write



$$
S_n=\sum_{a=1}^n\log(a!),\qquad
 T_m=\sum_{h=1}^{m-1}(m-h)\log h.                          \tag{14}
$$



Then exactly



$$
\log Q=M\log2+mS_n+(n+1)^2T_m.               \tag{15}
$$



The standard Euler--Maclaurin estimates give



$$
\begin{aligned}
 S_n&=\frac12n^2\log n-\frac34n^2+O(n\log n),\\
 T_m&=\frac12m^2\log m-\frac34m^2+O(m\log m).
 \end{aligned}                                             \tag{16}
$$



For every $C\in\mathbb Z[z]_{\le D}$, put



$$
U_C=QT_C.
$$



The frozen Cramer estimate says that $U_C$ is integral and



$$
H(U_C)\le C_BH(C),                                        \tag{17}
$$



where



$$
\begin{aligned}
 B_0&=\max\{1,(M-1)^n(m-1)^{M-1}\},\\
 C_B&=2^{M-1}(D+1)M!(M-1)!B_0^{M-1}.                       \tag{18}
 \end{aligned}
$$



The expression in (18) is valid for $m\ge2$; in particular no
ambiguous $0^0$ convention is needed.

For the endpoint kernel, put



$$
\begin{aligned}
 N_0&=M+D-2,\\
 B_K&=2^{N_0}N_0!N_0^D(m!)^{n+1},\\
 P_0&=(D-1)!B_K^{D-1}.                                    \tag{19}
 \end{aligned}
$$



If $p$ is the primitive saturated Pluecker vector, the proved minor
bound, with the unknown minor gcd only bounded below by one, is



$$
H(p)\le P_0.                    \tag{20}
$$



No cancellation from that minor gcd is used anywhere below.

## 3. Basis-free exterior coefficient majorants

Let $e_a=z^a$, $0\le a\le D$, and define the universally cleared
coordinate remainder



$$
F_a=\overline R_{e_a}=Qe_a+(1+e^z)U_{e_a}(z,e^z).          \tag{21}
$$



Equations (17)--(18) imply



$$
H(F_a)\le Q+2C_B.                 \tag{22}
$$



Each $F_a$ has frequencies $0,\ldots,m$ and polynomial degree at most
$n$.  An individual coordinate remainder need only have the basic
interpolation order $M$.  What has order $L$ is the linear combination
$\sum_ac_aF_a=\overline R_C$ when $C$ belongs to the constrained
endpoint kernel.  The coefficient estimate below uses only the frequency,
degree, and height statements for the individual $F_a$'s.

For a saturated oriented basis $C,D$, write



$$
p_{ab}=c_ad_b-c_bd_a,\qquad 0\le a<b\le D.                \tag{23}
$$



Alternating bilinearity gives the exact identity



$$
W(\overline R_C,\overline R_D)
     =\sum_{0\le a<b\le D}p_{ab}W(F_a,F_b).                \tag{24}
$$



For any two exponential polynomials of coefficient height at most $H_F$,
frequencies $0,\ldots,m$, and polynomial degree at most $n$, direct
coefficient convolution and one differentiation give



$$
H(W(F,G))\le
       2(m+1)(n+1)(n+m)H_F^2.                              \tag{25}
$$



Put



$$
R_D={D+1\choose2},\qquad
        \omega_D=\left\lfloor\frac{(D+1)^2}{4}\right\rfloor. \tag{26}
$$



Summing (25) in (24), then using (20), proves the second bound in (5).

For the first bound, let



$$
N_Q=Q\Delta,\qquad
              \mathfrak c_Q=\operatorname {cont}(N_Q),
              \qquad P_\Delta=N_Q/\mathfrak c_Q.           \tag{27}
$$



The cleared endpoint matrix satisfies



$$
QE_{b,a}=[z^b]U_{e_a}(z,-1).                              \tag{28}
$$



The evaluation at $-1$ sums at most $m$ coefficients, so



$$
H(QE)\le mC_B.                    \tag{29}
$$



Apply the exact corrected coefficient map from the primitive-height audit
with clearing $Q$.  There are at most the fixed-sum Wronskian weight
$\omega_D$, and at most $D(D+1)$ nonzero antisymmetric endpoint
terms.  Hence



$$
H(N_Q)\le H(p)\{Q\omega_D+D(D+1)mC_B\},                  \tag{30}
$$



which proves the first bound in (5).

The bounds (5) use the primitive exterior vector directly.  They neither
choose a poorly conditioned kernel basis nor assume that a small
Pluecker vector factors into two simultaneously small basis vectors.

## 4. A global denominator-versus-gain inequality

This section proves (4) by elementary inequalities.  First note that



$$
A_{\rm an}\le M-1,\qquad
                  \frac{A_{\rm an}}m<n+1.                  \tag{31}
$$



We use only



$$
e>\frac83,\qquad \pi>3,\qquad
 \log2>\frac23,\qquad \log x\le\frac xe\quad(x>0).        \tag{32}
$$



The first inequality follows from the positive Taylor series after the
terms through $1/3!$, and the third follows, for example, from



$$
\log x\ge\frac{2(x-1)}{x+1}\quad(x\ge1).
$$



If $n\le7$, then $A_{\rm an}/m<n+1\le8<e\pi$, so
$\mathcal G_1<0<\log Q/2$.

Suppose $n\ge8$.  Since $e\pi>8$, (31) and the nonnegative number
$\log((n+1)/8)$ give



$$
\frac{2\mathcal G_1}{m}
 <2(n+1)\log\frac{n+1}{8}
 \le\frac{(n+1)^2}{4e}
 <\frac{3(n+1)^2}{32}.                                    \tag{33}
$$



On the other hand, $a!\ge2^{a-1}$ gives



$$
S_n\ge\frac{n(n-1)}2\log2.
$$



Because $T_m\ge0$, equations (15) and (32) imply



$$
\frac{\log Q}{m}
 \ge\left(n+1+\frac{n(n-1)}2\right)\log2
 >\frac{n^2+n+2}{3}.                                      \tag{34}
$$



Finally,



$$
32(n^2+n+2)-9(n+1)^2=23n^2+14n+55>0.                    \tag{35}
$$



Equations (33)--(35) prove (4).

## 5. Exact algebraic comparison and the missing inputs

Assume temporarily that $s=e+\pi$ is algebraic of degree $r$.  Let



$$
d=\deg P_\Delta,\qquad
 h_0=\log H(N_Q),\qquad
 \chi=\log\mathfrak c_Q,\qquad
 h=h_0-\chi.                                               \tag{36}
$$



Put $C_0=(2m+1)(2n+1)$.  The corrected Schwarz estimate is



$$
-\log|P_\Delta(i\pi)|
 \ge2\mathcal G_1+\log Q+\chi-\log(C_0H_W),               \tag{37}
$$



where $H_W$ is any proved upper bound for the cleared Wronskian
coefficient height.  The leading algebraic-number lower bound has exponent



$$
\kappa=r^2d+r-1.                  \tag{38}
$$



Thus (37) can beat the leading lower bound only if



$$
(\kappa+1)\chi>
 \kappa h_0+\log(C_0H_W)-2\mathcal G_1-\log Q.             \tag{39}
$$



This is the intrinsic threshold.  Literal finite-height use requires the
field, norm, and affine-substitution constants from the polynomial
$e$-measure to be added to the right side.

Substituting $h_0\le\log\widehat H_N$ and
$H_W\le\widehat H_W$ gives the sufficient all-parameter condition (7).
The currently proved content information is only



$$
0\le\chi\le h_0\le\log\widehat H_N.          \tag{40}
$$



There is no all-parameter positive lower bound for $\chi$.  The bare
Wronskian content, the cardinal content, the $\Gamma$-content, and a
finite grid of corrected contents do not change (40).

With only $\chi=0$, define the absolute exponent certified by the
universal majorants,



$$
u_{\rm univ}:=
 2\mathcal G_1+\log Q-\log(C_0\widehat H_W).                \tag{41}
$$



Since $\widehat H_W\ge Q^2$, equations (4) and (41) give



$$
u_{\rm univ}\le2\mathcal G_1-\log Q<0.  \tag{42}
$$



This proves the no-certificate assertion in the verdict for every finite
admissible triple, not only asymptotically.

The exact size of either missing input can now be stated.

* **Missing corrected content.**  In the universal ledger, the strict
  leading threshold is

  

$$
\boxed{
  \chi_{\rm req}=
   \frac{\kappa\log\widehat H_N+
       \log(C_0\widehat H_W)-2\mathcal G_1-\log Q}
        {\kappa+1}.}                                      \tag{43}
$$



  One must prove $\chi>\chi_{\rm req}$, with the finite-height constants
  added.  No presently proved gcd theorem approaches (43).

* **Missing analytic gain.**  If an improved value theorem replaces
  $2\mathcal G_1$ by $2\mathcal G_1+J$, while a particular corrected
  content $\chi$ is proved, the least leading logarithmic improvement is

  

$$
\boxed{
  J_{\rm req}=\Bigl[
     \kappa\log\widehat H_N-(\kappa+1)\chi
     +\log(C_0\widehat H_W)-2\mathcal G_1-\log Q
       \Bigr]_+.}                                         \tag{44}
$$



* **Required primitive-height collapse.**  Put
  $\widehat h=\log\widehat H_N-\chi$.  Equation (7) is equivalently

  

$$
\boxed{
  (\kappa+1)\widehat h<
   \log\widehat H_N+2\mathcal G_1+\log Q
        -\log(C_0\widehat H_W).}                           \tag{45}
$$



  This is the precise residual primitive height that a structured
  saturation/content theorem would have to leave.

### 5.1 A proved dyadic content filter on one infinite subfamily

The companion leading-coefficient theorem gives more arithmetic information
when



$$
m=3,\qquad D=2,\qquad h=n+1=2^q,\qquad q\ge2.             \tag{45a}
$$



Here $p=e_0\wedge e_2$, the degree is exactly $d=h+1$, and the reduced
leading coefficient has dyadic valuation $-2h$.  If $q_\Delta$ and
$\mathfrak c_\Delta$ are the intrinsic denominator and corrected content,
that theorem proves



$$
2^{2h}\mid q_\Delta,\qquad
 \mathfrak c_\Delta\mid N_h,\qquad
 2\nmid\mathfrak c_\Delta,\qquad
 \log|N_h|=O(h\log h).                                    \tag{45b}
$$



For universal clearing it follows that



$$
v_2(\mathfrak c_Q)\le v_2(Q)-2h.                         \tag{45c}
$$



This is a genuine all-parameter content cap, not a finite-grid pattern.  It
shows that the intrinsic corrected content cannot contain a hidden
quadratic-in-$h$ dyadic factor.  It does not, however, lower-bound the
primitive height: the leading coefficient alone still permits
$q_\Delta$ to equal its reduced denominator and
$\mathfrak c_\Delta=|N_h|$, leaving primitive leading coefficient
$\pm1$.

On (45a),



$$
\mathcal G_1=O(h\log h),\qquad
 \kappa=r^2(h+1)+r-1.                                     \tag{45d}
$$



Therefore a comparison whose total certified absolute gain remains
$O(h\log h)$ must leave primitive logarithmic height only $O_r(\log h)$
to have any chance against the algebraic exponent.  The theorem (45b)
does not prove that collapse; a second-coefficient gcd or full primitive-
height theorem remains necessary.

## 6. The proved degree regimes

The top-cardinal and forced-parity theorems currently give the following
complete exact-degree list except for two even-frequency families.



$$
\begin{array}{c|c}
\text{parameter family}&\text{proved degree}\\ \hline
n+D\text{ even},\ m\ge2&d=n+D\\
m,n\text{ odd and }D\text{ even}&d=n+D\\
m\ge3\text{ odd},\ n\text{ even},\ D\text{ odd}&d=n+D-1\\
m\text{ even},\ n\text{ even},\ D\text{ odd}
 &\Delta\ne0,\quad d\le n+D\quad\text{only}\\
m\text{ even},\ n\text{ odd},\ D\text{ even}
 &\Delta\ne0,\quad d\le n+D\quad\text{only}.
\end{array}                                                 \tag{46}
$$



In particular, every odd $m\ge3$ has an exact degree: the third row is
the only top-forced odd-$m$ case.  No next-coefficient theorem is imported
into either of the last two rows.

The relative algebraic threshold is



$$
r^2d+r.                            \tag{47}
$$



The easiest possible hypothesis is $r=1$, for which the threshold is
$d+1$.  Failure even for $r=1$ implies failure for every $r\ge1$.

## 7. Optimization across scalable regimes

This section isolates scale, rather than pretending that an upper Cramer
bound is the true intrinsic height.  Suppose a noncollapse theorem supplies
a one-column logarithmic height scale $\eta$ with



$$
\log H(N_Q)=(2+o(1))\eta,\qquad
 \log H_W=(2+o(1))\eta,\qquad
 \log Q=o(\eta),\qquad \chi=o(\eta).                       \tag{48}
$$



Then the frozen primitive-height identity gives



$$
\Theta_{\rm Schwarz}=\frac{\mathcal G_1}{\eta}+o(1). \tag{49}
$$



If only the first two relations in (48) and $\chi=o(\eta)$ hold, while
$\log Q$ is not negligible, the exact matched-scale expression is



$$
\Theta_{\rm Schwarz}
 =\frac{\mathcal G_1}{\eta}
   +\frac{\log Q}{2\eta}+o(1).                              \tag{49a}
$$



Thus an optimistic lower noncollapse condition
$\eta\ge c\log Q$, with fixed $c>0$, gives at most a constant
$1/(2c)$ from the clearing term plus the analytic component studied
below.  It does **not** turn the full relative exponent into
$\mathcal G_1/\log Q$.  None of these lower noncollapse conditions is
currently proved; the unconditional statements remain (7), (39), and
(42).

### 7.1 Uniformly in $m,D$, with $n\to\infty$

The elementary upper bound



$$
(\mathcal G_1)_+\le M\log(n+1)            \tag{50}
$$



and (15)--(16) give, uniformly in $m\ge2$ and $2\le D\le n$,



$$
\frac{(\mathcal G_1)_+}{\log Q}\le
                 \frac{2+o(1)}n.                           \tag{51}
$$



In every exact-degree row of (46), $d\ge n+D-1\ge n+1$.  Thus the
analytic component, measured against denominator scale, has missing
multiplicative factor at least



$$
\frac{r^2d+r}{\mathcal G_1/\log Q}
                      =\Omega(r^2n^2).                      \tag{52}
$$



Under the stronger hypothesis (48), this is also the deficit of the full
relative exponent.  Under only $\eta\ge c\log Q$, equation (49a) permits
a bounded clearing contribution, but the threshold still grows like
$r^2n$; its remaining deficit is at least of order $n$.

Increasing $m$ cannot improve the order in (51).  The additional
positive node-Vandermonde term $(n+1)^2T_m$ in fact makes the ratio
smaller when $m$ grows.

### 7.2 Fixed $m$, and $D/n\to\delta\in[0,1]$

Here the leading constants can be retained:



$$
\begin{aligned}
 \mathcal G_1&=(m-1+\delta)n\log n+O_m(n),\\
 \log Q&=\frac m2n^2\log n+O_m(n^2).                       \tag{53}
 \end{aligned}
$$



In an exact-degree family $d=(1+\delta)n+O(1)$.  Therefore the
analytic-gain amplification at denominator scale needed to reach (47) is



$$
\boxed{
  \frac{r^2m(1+\delta)}{2(m-1+\delta)}n^2(1+o(1)).}         \tag{54}
$$



For $m>2$, the analytic gain per endpoint degree is largest at
$\delta=0$, that is, fixed or sublinear $D$; for $m=2$ its leading
constant is independent of $\delta$.  Even the optimal choice retains
the factor $n^2$.

### 7.3 Fixed $n,D$, with $m\to\infty$

Now



$$
\begin{aligned}
 \mathcal G_1&=O_n(m),\\
 \log Q&=\frac12(n+1)^2m^2\log m+O_n(m^2).                 \tag{55}
 \end{aligned}
$$



If $n+1\le e\pi$, the leading coefficient in $\mathcal G_1$ is
nonpositive; otherwise it is still only linear in $m$.  Hence



$$
\frac{(\mathcal G_1)_+}{\log Q}
                      =O_n\!\left(\frac1{m\log m}\right). \tag{56}
$$



Under (48), the exact degree is fixed in the first three rows of (46), but
its positive algebraic threshold cannot be met by a quantity tending to
zero.  The analytic component is short by
$\Omega_{n,D,r}(m\log m)$.

### 7.4 Both $m,n\to\infty$

Combining the two positive pieces of (15) yields



$$
\frac{(\mathcal G_1)_+}{\log Q}
 =O\!\left(
  \min\left\{\frac1n,
       \frac{\log(n+1)}{mn\log m}\right\}\right).         \tag{57}
$$



Thus the exponent deficit is at least of order



$$
r^2n^2\max\left\{1,\frac{m\log m}{\log(n+1)}\right\}     \tag{58}
$$



for the analytic component at denominator scale in the exact-degree
families.  There is no growing-
$m$ wedge hidden between the fixed-$m$ and diagonal regimes.

Equations (51)--(58) do not assume a gcd cancellation.  Rather, they say
exactly how large an exceptional cancellation must be to escape the
noncollapse scale.  The unconditional required cancellation is (39) or
(43), not an extrapolation from these asymptotics.

## 8. The even-frequency degree-collapse loophole

Keep either of the last two rows of (46), and suppose an independent
calculation proves enough arithmetic information to give a relative
small-value exponent



$$
\Theta=-\frac{\log(|P_\Delta(i\pi)|/H(P_\Delta))}
                    {\log H(P_\Delta)}.                    \tag{59}
$$



The degree-$r$ lower bound is contradicted only if



$$
\Theta>r^2d+r.                    \tag{60}
$$



Solving (60) for the unknown degree gives (9).  The largest allowable
integer degree is



$$
d_{\max}(r,\Theta)=
  \left\lceil\frac{\Theta-r}{r^2}\right\rceil-1,           \tag{61}
$$



provided this number is nonnegative.  Relative to the generic top degree,
a proof would therefore need a collapse of at least



$$
(n+D)-d_{\max}(r,\Theta).              \tag{62}
$$



For $r=1$, this reduces to



$$
d<\Theta-1.                        \tag{63}
$$



On the denominator-scale regimes of Section 7,
$\Theta_{\rm Schwarz}=o(1)$.  Since the threshold for even $d=0$ is
already $r$, degree collapse alone is not asymptotically large enough.
For $n\to\infty$, collapsing from order $n$ to zero removes one of the
two missing factors of $n$ in (52), but a further factor $n$ in
analytic gain or primitive-height reduction remains.  With only the
universal facts (5) and $\chi\ge0$, equation (42) is stronger: the
certified absolute exponent is negative, so no degree at all can make the
comparison work.

This conclusion does not assert that the actual degree in the two even-
frequency forced families is large.  It quantifies exactly when learning
that degree would begin to matter.

## 9. Conditional unconstrained parity-pair regime

This section concerns a different endpoint space and is not used in the
proofs above.  Let the endpoint degree be even $n=D$, take the full
endpoint space of dimension $\nu=n+1$, and suppose there exist rational
parity directions $C_{\rm odd},D_{\rm even}$ such that



$$
R_C,R_D=O(z^M),\qquad M=m(n+1).                            \tag{64}
$$



Assume further that their corrected exterior polynomial is nonzero of
exact degree two for all even $n$ in an infinite family:



$$
\Delta=W(C,D)-\{C\beta_D-D\beta_C\},\qquad
                         \deg\Delta=2.                     \tag{65}
$$



Only finite $n=4$ calculations currently motivate (65); (64)--(65) are
hypotheses in this section.

The stationary gain is now



$$
\mathcal G_1^{\circ}=(M-n)
     \log\frac{M-n}{e\pi m}-n\log\pi.                     \tag{66}
$$



For fixed $m$,



$$
\mathcal G_1^{\circ}
                   =(m-1)n\log n+O_m(n).                  \tag{67}
$$



Normalize the exterior pair intrinsically so that (65) is the primitive
integer polynomial.  Let $H_W^{\rm int}$ be a coefficient-height bound
for the Wronskian in that same exterior normalization, with every rational
clearing and exterior content already accounted for.  Schwarz gives



$$
-\log|P_\Delta(i\pi)|
 \ge2\mathcal G_1^{\circ}
       -\log\{(2m+1)(2n+1)H_W^{\rm int}\}.                 \tag{68}
$$



For $d=2$, the absolute algebraic exponent is



$$
\kappa_2=2r^2+r-1.                \tag{69}
$$



Consequently the exact intrinsic leading condition is



$$
\boxed{
 \log H_W^{\rm int}+\kappa_2\log H(P_\Delta)
               <2\mathcal G_1^{\circ}-\log\{(2m+1)(2n+1)\}.} \tag{70}
$$



Equations (10)--(11) follow immediately from (67) and (70).

In the common matched-height model, let one intrinsically normalized
column have coefficient-height exponent



$$
\log H_{\rm col}=\lambda n\log n+o(n\log n), \tag{71}
$$



and suppose both the Wronskian coefficient height and the primitive
quadratic endpoint height have their natural quadratic scale



$$
\log H_W^{\rm int}=2\lambda n\log n+o(n\log n),\qquad
 \log H(P_\Delta)=2\lambda n\log n+o(n\log n).             \tag{72}
$$



Then (70) becomes exactly (12).

The distinction between intrinsic and Cramer height is decisive.  Applying
the general interpolation estimate mechanically with $D=n$ gives



$$
\begin{aligned}
 H_R&\le A(Q+2C_B),\\
 H_W&\le2(m+1)(n+1)(n+m)A^2(Q+2C_B)^2,\\
 H(N_Q)&\le A^2\{2n^2Q+2m(n+1)C_B\},                       \tag{73}
 \end{aligned}
$$



where $A=\max(H(C),H(D))$.  For fixed $m\ge2$, (18) gives



$$
\log C_B=m n^2\log n+O_m(n^2),               \tag{74}
$$



whereas (67) is only of order $n\log n$.  Hence (73) is too coarse by a
full factor $n$ even before the algebraic exponent is paid.  Proving the
conditional survivor requires an intrinsic exterior saturation/content
theorem that reduces (73) to the scale (70).  It is not legitimate to
identify the height of a specially normalized parity pair with the Cramer
majorant, in either direction.

There is also a geometric obstruction to rational persistence.  Write
$n=2s$.  Projectively, an odd endpoint direction lies in
$\mathbb P^{s-1}$ and an even endpoint direction lies in
$\mathbb P^s$.  Their decomposable pairs form the Segre variety



$$
\mathbb P^{s-1}\times\mathbb P^s,\qquad
 \dim=n-1,\qquad
 \deg={n-1\choose s-1}.                                    \tag{75}
$$



If $\varrho\ge1$ is a target half-degree and the high corrected
coefficients are independent, the conditions
$\deg\Delta\le2\varrho$ impose $n-\varrho$ rational hyperplanes.
For maximal quadratic collapse, $\varrho=1$, the expected intersection
is zero-dimensional and has total algebraic degree



$$
{n-1\choose s-1}
 \sim\frac{2^n}{\sqrt{2\pi n}}.                            \tag{76}
$$



The exact eliminants currently split by component degree as



$$
\begin{array}{c|c|c}
 n&{n-1\choose s-1}&\text{observed component degrees}\\ \hline
 4&3&1+2\\
 6&10&4+6\\
 8&35&15+20.
 \end{array}                                                \tag{77}
$$



Thus the rational component at $n=4$ is exceptional in the tested
sequence; the next two rows have no degree-one component.  Formula (75)
is an exact geometric count, while persistence, transversality, and the
component pattern in (77) beyond the displayed rows remain open.

This distinction also matters arithmetically.  Equations (68)--(72) require
a rational exterior pair, or at least a primitive rational quadratic
$\Delta$ with an equally strong rational height theorem.  Merely finding
a pair over a number field of degree $q_n$ does not preserve the
fixed-degree advantage: taking its norm can raise the endpoint degree from
two to as much as $2q_n$, and coefficient heights acquire the associated
norm cost.  The Segre degree (76) shows why a generic field degree can grow
exponentially.  A successful parity-pair construction would therefore
need an additional descent or rationality mechanism, not just algebraic
existence on the zero-dimensional intersection.

## 10. Nondecomposable exterior sums

This section audits the stronger construction suggested by the linearity of
the corrected exterior map.

### 10.1 Endpoint space and exact identity

For $2\le\nu\le D+1$, let $E_\nu$ be the endpoint space obtained by
imposing the $D+1-\nu$ endpoint constraints



$$
K_{q,a}=\mathcal L\!\left((X^q\Phi_{m,n})^{(a)}\right),
 \qquad 0\le q\le D-\nu,\quad0\le a\le D.                 \tag{78}
$$



Endpoint normality gives $\dim E_\nu=\nu$.  Every $C\in E_\nu$ has a
remainder



$$
R_C=C+(1+e^z)T_C(z,e^z)=O(z^{L_\nu}),\qquad
 L_\nu=M+D+1-\nu.                                         \tag{79}
$$



Thus $E_2$ recovers $L=M+D-1$, while increasing the endpoint dimension
from two to $\nu$ loses exactly $\nu-2$ orders.

Choose a saturated integral basis $C_1,\ldots,C_\nu$ and define



$$
\begin{aligned}
 \Delta_{ij}&=W(C_i,C_j)
       -\{C_i\beta_{C_j}-C_j\beta_{C_i}\},\\
 \mathcal W_{ij}&=W(R_{C_i},R_{C_j}).
 \end{aligned}                                             \tag{80}
$$



For an arbitrary integral exterior coordinate vector
$x=(x_{ij})_{i<j}$, decomposable or not, put



$$
\Delta_x=\sum_{i<j}x_{ij}\Delta_{ij},\qquad
             \mathcal W_x=\sum_{i<j}x_{ij}\mathcal W_{ij}. \tag{81}
$$



Linearity of the endpoint identity gives



$$
\boxed{\Delta_x(i\pi)=\mathcal W_x(i\pi),\qquad
        \operatorname {ord}_0\mathcal W_x\ge2L_\nu.}       \tag{82}
$$



No Pluecker relation is needed.  If $\Delta_x\ne0$, then
$\Delta_x(i\pi)\ne0$ because $i\pi$ is transcendental.

### 10.2 Killing the high coefficients

The general corrected degree bound is $\deg\Delta_{ij}\le n+D$.  Fix a
target degree $d\ge0$, and let



$$
N={\nu\choose2},\qquad S=n+D-d.                    \tag{83}
$$



The coefficients of degrees $d+1,\ldots,n+D$ define a rational linear
map



$$
\mathcal T_{\rm high}:\mathbb Q^N
                         \longrightarrow\mathbb Q^S.       \tag{84}
$$



If $N>S$, its kernel is nonzero.  Every $x$ in that kernel has
$\deg\Delta_x\le d$.  To obtain a usable endpoint, one must additionally
prove the rank-gap condition



$$
\boxed{\ker\mathcal T_{\rm high}\not\subseteq
        \ker\mathcal T_{\rm all}.}                         \tag{85}
$$



Dimension alone proves neither (85) nor $\Delta_x\ne0$.

For fixed $d$, $D/n\to\delta\in[0,1]$, and a fixed oversampling factor
$\tau>1$, choose



$$
N\sim\tau S,\qquad
 \nu\sim\sqrt{2\tau(1+\delta)n}.                           \tag{86}
$$



This requires $\nu\le D+1$.  When $\delta>0$ that is automatic for
large $n$.  When $\delta=0$, one may take the particularly favorable
full endpoint space



$$
D=\nu-1=\Theta(\sqrt n).          \tag{86a}
$$



Then the constraint matrix (78) is empty, the saturated monomial basis has
$A_\nu=1$, and $L_\nu=M$.

Then



$$
L_\nu-n=(m-1+\delta)n-O(\sqrt n),                         \tag{87}
$$



and the optimized one-column gain is



$$
\mathcal G_\nu=(L_\nu-n)
   \log\frac{L_\nu-n}{e\pi m}-n\log\pi
 =(m-1+\delta)n\log n+O_{m,\delta,\tau}(n).                \tag{88}
$$



Thus fixed degree is achieved at no leading analytic cost.  This is the
main advantage over the constrained $E_2$ exact-degree families.

### 10.3 Exact elementary Siegel bound

Let



$$
A_\nu=\max_jH(C_j)                \tag{89}
$$



for the chosen saturated basis.  The universal interpolation estimate gives



$$
H(U_{C_j})\le C_BA_\nu.                                   \tag{90}
$$



Consequently every coefficient of $Q\Delta_{ij}$ has absolute value at
most



$$
B_\Delta=A_\nu^2\{2D^2Q+2m(D+1)C_B\}.                    \tag{91}
$$



After clearing by $Q$, (84) is therefore an integer $S$-by-$N$
matrix of height at most $B_\Delta$.

An elementary pigeonhole form of Siegel's lemma says that an integer
$S$-by-$N$ matrix of height $B\ge1$, with $N>S$, has a nonzero
integer kernel vector of height at most



$$
X_{N,S}(B)=
 \left\lfloor(2NB+1)^{S/(N-S)}\right\rfloor+1.             \tag{92}
$$



Indeed, compare the $(X+1)^N$ vectors in
$\{0,\ldots,X\}^N$ with their images, each coordinate of which has at
most $2NBX+1$ possible values, and choose $X$ just above the threshold
in (92).

Taking $B=B_\Delta$, there is therefore a high-coefficient null vector
with



$$
H(x)\le X:=X_{N,S}(B_\Delta).      \tag{93}
$$



When $N\sim\tau S$,



$$
\log X\le\frac1{\tau-1}
               \{\log B_\Delta+O(\log n)\}.                \tag{94}
$$



Thus oversampling changes the disastrous cofactor exponent $S$ of a
one-dimensional nullspace into the constant $1/(\tau-1)$.  This is a
real Siegel-lemma gain.

### 10.4 Universal value and primitive-height ledger

For each cleared pair,



$$
H\!\left(W(\overline R_{C_i},\overline R_{C_j})\right)
 \le B_W:=
 2(m+1)(n+1)(n+m)A_\nu^2(Q+2C_B)^2.                       \tag{95}
$$



Therefore the sum selected in (93) satisfies



$$
\widehat H_W^{(\nu)}
 :=N X B_W,\qquad
 \widehat H_N^{(\nu)}
 :=N X B_\Delta.                                          \tag{96}
$$



Let $N_{Q,x}=Q\Delta_x$,
$\mathfrak c_x=\operatorname {cont}(N_{Q,x})$, and
$\chi_x=\log\mathfrak c_x$.  Provided the rank-gap condition (85) holds,
the primitive endpoint is $P_x=N_{Q,x}/\mathfrak c_x$, and Schwarz gives



$$
-\log|P_x(i\pi)|
 \ge2\mathcal G_\nu+\log Q+\chi_x
      -\log\{(2m+1)(2n+1)\widehat H_W^{(\nu)}\}.            \tag{97}
$$



For $\kappa_d=r^2d+r-1$, the universal leading certificate requires



$$
\boxed{
 (\kappa_d+1)\chi_x>
 \kappa_d\log\widehat H_N^{(\nu)}
 +\log\{(2m+1)(2n+1)\widehat H_W^{(\nu)}\}
 -2\mathcal G_\nu-\log Q.}                                \tag{98}
$$



This is the exact analogue of (7).

The content-free universal estimate still fails before the algebraic
threshold is paid.  Whenever the stationary radius for (88) is admissible,
$\mathcal G_\nu\le\mathcal G_1$, because $L_\nu\le L$ and the optimized
gain is increasing with $L-n$ above that radius.  Hence (4) gives



$$
2\mathcal G_\nu<\log Q.           \tag{99}
$$



Since $\widehat H_W^{(\nu)}\ge Q^2$, setting
$\chi_x=0$ in (97) again gives a negative certified absolute exponent.
The added exterior dimension does not manufacture a proved gcd.

### 10.5 Does the Siegel gain offset endpoint height?

No, not with the currently proved coefficient bounds.  For fixed
$m\ge2$, $D/n\to\delta\in[0,1]$, equations (18) and (91), even under the
unrealistically favorable formal choices $A_\nu=X=1$, contain the scale



$$
\log C_B=m n^2\log n+O_{m,\delta}(n^2),\qquad
 2\log(Q+2C_B)=2m n^2\log n+O_{m,\delta}(n^2).             \tag{100}
$$



whereas (88) is only $O(n\log n)$.  Equation (94) prevents an additional
factor $S=\Theta(n)$ from entering $\log H(x)$, but it cannot remove
the $C_B$ term already present in each endpoint remainder.

The saturated endpoint lattice has its own unresolved cost.  With
$R_0=D+1-\nu$, the cleared endpoint matrix has $R_0$ rows.  Its
primitive maximal-minor vector has the unconditional bound



$$
H(p_\nu)\le R_0!\,B_{K,\nu}^{R_0},\qquad
 B_{K,\nu}=2^{N_{0,\nu}}N_{0,\nu}!N_{0,\nu}^D(m!)^{n+1},
 \quad N_{0,\nu}=M+D-\nu.                                  \tag{101}
$$



For (86) with $\delta>0$,
$\log B_{K,\nu}=O_{m,\delta}(n\log n)$ and $R_0=\Theta(n)$, so (101)
is again $O(n^2\log n)$ logarithmically.  It is a
covolume/exterior bound, not a proof that every basis vector has that
height.  In the full endpoint choice (86a), $R_0=0$ and $A_\nu=1$, so
this endpoint-lattice obstruction disappears completely.  Nevertheless,
the interpolation majorant $C_B$ in (90), which is already
$\exp\{m n^2\log n+O_m(n^2)\}$, remains.  No current theorem replaces
that Cramer scale by the needed intrinsic $O(n\log n)$ scale for the
selected exterior sum.

Thus the dimensional construction has removed the growing polynomial
degree and the high-map cofactor exponent, but two arithmetic inputs remain:

1. the rank gap (85);
2. an intrinsic remainder height or corrected-content theorem that replaces
   the Cramer interpolation scale in (90)--(100) by $O(n\log n)$-scale
   bounds; and, outside the full endpoint choice (86a), compatible
   saturated endpoint-lattice height control.

If such a theorem gives, after intrinsic exterior normalization,



$$
\log H_W^{\rm int}=a\,n\log n+o(n\log n),\qquad
 \log H(P_x)=b\,n\log n+o(n\log n),                        \tag{102}
$$



then fixed target degree $d$ and (88) give the sharp leading condition



$$
\boxed{a+(r^2d+r-1)b<2(m-1+\delta).}                      \tag{103}
$$



If both heights have matched quadratic scale $a=b=2\lambda$, this is



$$
\boxed{\lambda<
                    \frac{m-1+\delta}{r^2d+r}.}            \tag{104}
$$



Unlike the constrained exact-degree route, (103) has a fixed right-side
algebraic cost for fixed hypothetical $r,d$.  The nondecomposable
exterior-sum idea is therefore a legitimate conditional survivor.  What
is missing is arithmetic height control and nonvanishing, not analytic
order.

## 11. Replay and scope

The companion certificate is

* `scripts/root_unity_corrected_asymptotic_capacity_certificate.py`;
* `results/root_unity_corrected_asymptotic_capacity_certificate.json`.

It evaluates (13), (18)--(20), and (5) exactly on representative parity
rows, verifies the integer inequalities used in Section 4, checks the
degree-regime classifier against the proved parity statements, and reports
the leading threshold quantities.  It also replays the Segre degrees,
the $N,S,\nu$ exterior-sum dimension counts, the associated Siegel
exponents, and the conditional intrinsic thresholds.  Finite rows are
diagnostics only.  The
all-parameter results are the displayed identities and elementary proofs
above.

The audit deliberately does **not**:

1. assume a positive corrected gcd or a transfer from any other content;
2. assert an exact degree in either even-$m$ forced family;
3. infer the unconstrained degree-two parity-pair hypotheses from the
   $n=4$ grid;
4. treat an upper Cramer height bound as a lower bound for intrinsic height;
5. assume that the high-coefficient exterior kernel has nonzero corrected
   low image;
6. claim a proof about $e+\pi$.
