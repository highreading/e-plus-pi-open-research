> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Centering the exterior frequency spectrum halves the exponential type

## A correction to the root-of-unity Schwarz ledger

Checked: 2026-08-27 UTC

## 1. Verdict

Let



$$
\overline R_j(z)=\sum_{q=0}^{m}P_{j,q}(z)e^{qz},
 \qquad \deg P_{j,q}\le n,                                  \tag{1}
$$



be any cleared endpoint remainders, and let



$$
F_x(z)=\sum_{i<j}x_{ij}W(\overline R_i,\overline R_j)(z)   \tag{2}
$$



be an arbitrary rational or integral exterior sum.  The vector $x$ need
not be decomposable.  Suppose



$$
\operatorname {ord}_0F_x\ge2L.          \tag{3}
$$



The previously used circle estimate treated the frequencies
$0,\ldots,2m$ as having exponential type $2m$.  That estimate is valid
but not centered.  The exact correction is to put



$$
\widetilde F_x(z)=e^{-mz}F_x(z).    \tag{4}
$$



Then:

* $\widetilde F_x$ has frequencies $-m,\ldots,m$, so its coarse
  circle type is $m$, not $2m$;
* multiplication by $e^{-mz}$ leaves the coefficient height and number
  of coefficient slots unchanged;
* $\operatorname {ord}_0\widetilde F_x=\operatorname {ord}_0F_x$;
* at the endpoint,

  

$$
\widetilde F_x(i\pi)=(-1)^mF_x(i\pi),           \tag{5}
$$



  so the modulus and primitive endpoint form are unchanged up to sign.

If $A=L-n>0$, the sharp stationary radius for the resulting coarse
Schwarz bound is



$$
\boxed{\rho_{\rm ctr}=\frac{2A}{m}}, \tag{6}
$$



and the centered one-column gain is



$$
\boxed{
 \mathcal G_{\rm ctr}(L)
  =A\log\frac{2A}{e\pi m}-n\log\pi.}                        \tag{7}
$$



Thus



$$
\mathcal G_{\rm ctr}(L)
 =\mathcal G_{\rm old}(L)+A\log2,                           \tag{8}
$$



and the total exterior gain improves by $2A\log2$.

This correction supersedes the uncentered $e^{2m\rho}$ analytic ledger
in the earlier corrected-exterior primitive-height and asymptotic-capacity
audits.

It does **not** overturn their universal arithmetic obstruction.  For
every $m\ge2$, $n\ge D\ge2$, and every allowed endpoint dimension
$2\le\nu\le D+1$, the corrected gain still satisfies



$$
\boxed{2\mathcal G_{\nu,{\rm ctr}}<\log Q_{m,n}.}           \tag{9}
$$



Consequently, when the proved Wronskian-height majorant is at least
$Q_{m,n}^2$ and no corrected content is supplied, the certified absolute
smallness exponent remains negative.  The correction improves finite
thresholds, but for fixed $m$ it adds only $O(n)$, so it does not change
the leading $n\log n$ capacity threshold.  It also proves no
nonvanishing, rank-gap, degree classification, primitive-content theorem,
or conclusion about $e+\pi$.

## 2. Exact centering identity

Differentiation preserves each exponential frequency.  A product adds
frequencies.  Therefore every Wronskian in (2), and hence their arbitrary
linear combination, has an exact expansion



$$
F_x(z)=\sum_{q=0}^{2m}F_q(z)e^{qz},
 \qquad \deg F_q\le2n.                                     \tag{10}
$$



Multiplication by $e^{-mz}$ merely relabels these same coefficient
polynomials:



$$
\widetilde F_x(z)=\sum_{r=-m}^{m}F_{r+m}(z)e^{rz}.         \tag{11}
$$



No cancellation or estimate has been used in (11).  In particular, if



$$
H_F=\max_{q,k}|[z^k]F_q|,                                  \tag{12}
$$



then the centered Laurent-frequency expansion has exactly the same
$H_F$.  Negative frequencies cause no analytic difficulty: every term
$e^{rz}$ is entire.

The factor $e^{-mz}$ is a unit in the local ring at $z=0$, so it
preserves the origin order in (3).  At $z=i\pi$, it equals
$e^{-mi\pi}=(-1)^m$, which proves (5).  This last fact is especially
useful here: the centering introduces not merely a unit-modulus phase but
an exact rational sign in the endpoint identity.

One must center the expansion before applying the triangle inequality.
Multiplying the already-coarsened uncentered estimate by
$\max_{|z|=\rho}|e^{-mz}|$ would lose the improvement.  Equation (11) is
the legitimate reason the type is $m$.

## 3. The centered coarse circle and Schwarz bounds

Assume $\rho\ge1$.  For $|z|=\rho$,



$$
|F_{r+m}(z)|\le(2n+1)H_F\rho^{2n},                        \tag{13}
$$



and



$$
|e^{rz}|=e^{r\operatorname {Re}z}
 \le e^{|r|\,|\operatorname {Re}z|}
 \le e^{m\rho}.                                           \tag{14}
$$



Summing the $2m+1$ possible frequencies gives



$$
\boxed{
 \max_{|z|=\rho}|\widetilde F_x(z)|
 \le(2m+1)(2n+1)H_F\rho^{2n}e^{m\rho}.}                   \tag{15}
$$



This is the sharp centered version of the same elementary coefficient
majorant; “sharp” here refers to optimizing this coarse bound, not to an
extremal theorem for the particular entire function.

For every $\rho>\pi$, Schwarz's lemma applied to the zero of order $2L$
gives



$$
\begin{aligned}
 |F_x(i\pi)|
 &=|\widetilde F_x(i\pi)|\\
 &\le(2m+1)(2n+1)H_F
      \left(\frac\pi\rho\right)^{2L}
      \rho^{2n}e^{m\rho}.                                  \tag{16}
\end{aligned}
$$



If the exact endpoint scaling is



$$
F_x(i\pi)=Q\mathfrak c_xP_x(i\pi),                        \tag{17}
$$



where $P_x$ is primitive, then



$$
|P_x(i\pi)|
 \le\frac{(2m+1)(2n+1)H_F}{Q\mathfrak c_x}
      \left(\frac\pi\rho\right)^{2L}
      \rho^{2n}e^{m\rho}.                                  \tag{18}
$$



### 3.1 Interior stationary point

Put $A=L-n$.  Apart from constants independent of $\rho$, the negative
logarithm of the right side in (18) is



$$
2A\log\rho-m\rho.                  \tag{19}
$$



Its derivative is $2A/\rho-m$, so the stationary radius is (6).  If
$2A/m>\pi$, substitution gives



$$
\begin{aligned}
 -\log|P_x(i\pi)|
 \ge{}&2\mathcal G_{\rm ctr}(L)
       +\log(Q\mathfrak c_x)\\
 &-\log\{(2m+1)(2n+1)H_F\},                               \tag{20}
\end{aligned}
$$



with $\mathcal G_{\rm ctr}$ as in (7).  Direct subtraction from the old
gain proves (8).

### 3.2 Boundary case

For completeness, if $2A/m\le\pi$, the function in (19) is nonincreasing
for $\rho\ge\pi$.  Taking the limit $\rho\downarrow\pi$ gives the
boundary form



$$
|P_x(i\pi)|
 \le\frac{(2m+1)(2n+1)H_F}{Q\mathfrak c_x}
          \pi^{2n}e^{m\pi},                                \tag{21}
$$



or the per-column boundary gain



$$
\mathcal G_{\partial}=-n\log\pi-\frac{m\pi}{2}.           \tag{22}
$$



At $2A/m=\pi$, (7) and (22) agree exactly.

The boundary case does not actually occur in the root-of-unity endpoint
range considered here.  For endpoint dimension $2\le\nu\le D+1$,



$$
L_\nu=M+D+1-\nu\ge M=m(n+1).                              \tag{23}
$$



Hence



$$
\frac{2(L_\nu-n)}m
 \ge2+\frac{2n(m-1)}m
 \ge n+2\ge4>\pi.                                         \tag{24}
$$



Thus every allowed $\nu$ uses the interior formula (7).

## 4. The improved gain still lies below the common denominator

The common denominator is



$$
Q=2^M
 \left(\prod_{a=0}^{n}a!\right)^m
 \prod_{h=1}^{m-1}h^{(m-h)(n+1)^2},                        \tag{25}
$$



so, with



$$
S_n=\sum_{a=1}^{n}\log(a!),
 \qquad T_m=\sum_{h=1}^{m-1}(m-h)\log h,                   \tag{26}
$$



one has exactly



$$
\log Q=M\log2+mS_n+(n+1)^2T_m.                           \tag{27}
$$



It is enough to prove (9) for $\nu=2$, because $L_\nu\le L_2$, and



$$
\frac{d}{dA}\left(A\log\frac{2A}{e\pi m}\right)
      =\log\frac{2A}{\pi m}>0                              \tag{28}
$$



throughout the admissible range (24).

Write



$$
A=L_2-n=(m-1)n+m+D-1,                                    \tag{29}
$$



and abbreviate



$$
\mathcal G_0=A\log\frac{A}{e\pi m}-n\log\pi,
 \qquad
 \mathcal G_{\rm ctr}=\mathcal G_0+A\log2.                \tag{30}
$$



We use only the elementary bounds



$$
e>\frac83,\quad 3<\pi<4,\quad
 \frac23<\log2<\frac7{10},\quad
 \log y\le\frac ye\quad(y>0).                             \tag{31}
$$



For the upper bound in (31), the positive exponential series gives



$$
e^{7/10}>
 1+\frac7{10}+\frac1{2!}\left(\frac7{10}\right)^2
  +\frac1{3!}\left(\frac7{10}\right)^3
 =\frac{12013}{6000}>2.                                   \tag{32}
$$



The lower logarithm bound follows, for example, from
$\log y\ge2(y-1)/(y+1)$ at $y=2$.

### 4.1 The cases $n\le3$

Since $A/m<n+1$,



$$
\frac{2A}{e\pi m}<\frac{2(n+1)}{e\pi}
 \le\frac8{e\pi}<1.                                      \tag{33}
$$



Thus $\mathcal G_{\rm ctr}<0<\log Q/2$.

### 4.2 The cases $4\le n\le7$, $m\ge3$

Now $2(n+1)/(e\pi)<2$, so, after dropping the negative
$-n\log\pi$,



$$
2\mathcal G_{\rm ctr}<2A\log2
                     <2m(n+1)\log2.                        \tag{34}
$$



The single $h=2$ term gives $T_m\ge(m-2)\log2$.  Therefore



$$
\log Q\ge
 \{m(n+1)+(n+1)^2(m-2)\}\log2.                            \tag{35}
$$



Since



$$
(n+1)(m-2)-m=n(m-2)-2\ge2,                               \tag{36}
$$



the right side in (35) is strictly larger than the last expression in
(34).

### 4.3 The cases $4\le n\le7$, $m=2$

Here $A=n+D+1\le2n+1$, so



$$
2\mathcal G_{\rm ctr}<(4n+2)\log2.                        \tag{37}
$$



Also $T_2=0$ and



$$
S_n>n\log2.                                               \tag{38}
$$



Indeed, $2!$ contributes one copy of $\log2$, $3!=6>4$
contributes more than two copies, and every $a!$, $4\le a\le n$,
contributes at least one.  Hence



$$
\log Q=2(n+1)\log2+2S_n>(4n+2)\log2,                     \tag{39}
$$



which proves (9) in this range.

### 4.4 The cases $n\ge8$

The uncentered part obeys the elementary estimate



$$
\frac{2\mathcal G_0}{m}
 <\frac{3(n+1)^2}{32}.                                     \tag{40}
$$



For completeness: $A/m<n+1$, $e\pi>8$, and
$\log y\le y/e$ give



$$
\frac{2\mathcal G_0}{m}
 <2(n+1)\log\frac{n+1}{8}
 \le\frac{(n+1)^2}{4e}
 <\frac{3(n+1)^2}{32}.                                    \tag{41}
$$



Using $\log2<7/10$,



$$
\frac{2\mathcal G_{\rm ctr}}m
 <\frac{3(n+1)^2}{32}+\frac{7(n+1)}5.                      \tag{42}
$$



On the other hand, $a!\ge2^{a-1}$ and $\log2>2/3$ give



$$
\frac{\log Q}{m}
 \ge\left(n+1+\frac{n(n-1)}2\right)\log2
 >\frac{n^2+n+2}{3}.                                      \tag{43}
$$



After multiplying the difference between the right sides of (43) and
(42) by $480$, the numerator is



$$
115n^2-602n-397.                   \tag{44}
$$



It equals $2147$ at $n=8$ and is strictly increasing thereafter.
This proves (9) for $n\ge8$, and completes the all-parameter proof.

## 5. Corrected value ledger and what does not change

For endpoint dimension $\nu$, put



$$
A_\nu=L_\nu-n,
 \qquad
 \mathcal G_{\nu,{\rm ctr}}
 =A_\nu\log\frac{2A_\nu}{e\pi m}-n\log\pi.                \tag{45}
$$



Every coarse exterior value inequality in the older ledger should replace
$2\mathcal G_\nu$ by $2\mathcal G_{\nu,{\rm ctr}}$.  In particular,



$$
\begin{aligned}
 -\log|P_x(i\pi)|
 \ge{}&2\mathcal G_{\nu,{\rm ctr}}+\log Q+\chi_x\\
 &-\log\{(2m+1)(2n+1)\widehat H_W^{(\nu)}\},              \tag{46}
\end{aligned}
$$



where $\chi_x$ is the corrected content logarithm and
$\widehat H_W^{(\nu)}$ is any proved upper bound for the centered
coefficient height.  Centering does not change that height.

The content-free universal certificate still fails.  If
$\widehat H_W^{(\nu)}\ge Q^2$ and $\chi_x=0$, then the right side of
(46) is at most



$$
2\mathcal G_{\nu,{\rm ctr}}-\log Q
 -\log\{(2m+1)(2n+1)\}<0                                  \tag{47}
$$



by (9).

For fixed $m$, $D/n\to\delta$, and the endpoint-dimension regimes in
the older capacity audit,



$$
A_\nu=(m-1+\delta)n+o(n).                                 \tag{48}
$$



The correction $A_\nu\log2$ is $O(n)$, whereas the leading gain is



$$
\mathcal G_{\nu,{\rm ctr}}
 =(m-1+\delta)n\log n+O(n).                                \tag{49}
$$



Thus the numerical threshold improves, but its leading $n\log n$
coefficient is unchanged.  In particular, centering alone does not supply
the missing rank-gap, low-degree nonvanishing, rational descent,
primitive-content, or intrinsic-height theorem.

## 6. Deterministic replay

The package consists of the source note, the centered-frequency certificate
script, its JSON result, and a SHA-256 manifest with the corresponding
root-unity-centered-frequency filenames.

Replay from the archive root with

    python3 scripts/root_unity_centered_frequency_schwarz_certificate.py

The replay:

1. expands deterministic nondecomposable sums of Wronskians in exact
   frequency--polynomial dictionaries and verifies support, coefficient
   height, and the exact $(-1)^m$ endpoint multiplier;
2. differentiates and evaluates the centered coarse Schwarz exponent
   symbolically, including the boundary match;
3. checks the exact rational inequalities used in the four-case proof of
   (9);
4. verifies the centered-radius and gain monotonicity on a finite general-
   endpoint grid; and
5. records, as diagnostics only, $8265$ high-precision denominator/gain
   comparisons.

The all-parameter conclusions are proved in Sections 2--5, not inferred
from the finite grid.  The script has no randomized step.
