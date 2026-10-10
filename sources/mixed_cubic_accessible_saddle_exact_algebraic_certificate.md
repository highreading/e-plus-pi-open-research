> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact algebraic certificate for the mixed-cubic accessible saddle

Checked: 2026-08-27 UTC.

## 1. Verdict

Define



$$
\Psi(v)=\frac{(1+2v)^6(1+(1-i)v)^6}{v^4(1+v)^4},
 \quad
 b_0(v)=\frac{1+(1+i)v}{1+v},
 \quad
 b_2(v)=
 \frac{(1-i)(4v^4+8v^3+2v^2-2v-1)}
      {32v(1+v)^2},                                    \tag{1}
$$



and, exactly,



$$
\begin{aligned}
 S(v)&=4v^3+(6-i)v^2-iv-1-i,\\
 \frac{\Psi'(v)}{\Psi(v)}
 &=\frac{(2-2i)S(v)}
 {v(1+v)(1+2v)(1+(1-i)v)}.
 \end{aligned}                                         \tag{2}
$$



This note completes the exact algebraic part of the accessible-saddle
handoff.  It proves all of the following.

1. A specific algebraic radius $R<1/2$ and point
   $\tau=x+iy$, $|\tau|=R$, are isolated by rational intervals, and
   $S(\tau)=0$.
2. The angular critical polynomial of
   $|\Psi(Re^{i\theta})|$ has exactly two real roots.
3. Their exact sign pattern makes $\tau$ the unique global maximum of
   $|\Psi|$ on the valid fixed circle $|v|=R$.
4. The quadratic coefficient satisfies
   $\operatorname {Re}\lambda>2$.
5. The determinant amplitude satisfies
   

$$
\frac8{125}
    <\operatorname {Im}\frac{b_2(\tau)}{b_0(\tau)}
    <\frac{13}{200}.
$$



All theorem-facing signs, root counts, and interval decisions use exact
integer or rational arithmetic.  The decimal values in Section 7 are
diagnostics only.

This is deliberately an **algebraic certificate**, not the final analytic
saddle theorem.  No coefficient asymptotic or uniform error estimate is
asserted here.  In particular, this note does not prove that $e+\pi$ is
irrational or transcendental.

## 2. Exact isolation of the radius and saddle

Put



$$
\begin{aligned}
 g(z)={}&128z^6-384z^5+280z^4-20z^3-55z^2+z+2,\\
 f(R)={}&g(R^2).
 \end{aligned}                                         \tag{3}
$$



Use the broad and narrow rational intervals



$$
\begin{aligned}
 J&=\left(\frac{458133}{10^6},\frac{458136}{10^6}\right),\\
 K&=\left(
 \frac{458133387942745}{10^{15}},
 \frac{458133387942746}{10^{15}}\right),\\
 R_0&=\frac{91627}{200000}\in J.
 \end{aligned}                                         \tag{4}
$$



An ordinary rational Sturm calculation gives



$$
\begin{array}{c|ccc}
 & (0,K_-)&(K_-,K_+)&(K_+,+\infty)\\ \hline
 f&0&1&1\\
 g\ \text{on squared endpoints}&0&1&1 .
 \end{array}                                           \tag{5}
$$



The signs of both polynomials at their narrow endpoints are $+,-$.
Consequently there is a unique $R\in K$, its square



$$
a=R^2                         \tag{6}
$$



is the smaller positive root of $g$, and $R<1/2$.

Define



$$
\begin{aligned}
 x={}&-\frac{(4a+1)(16a^4-52a^3+49a^2-18a+1)}5,\\
 y={}& \frac{64a^5-208a^4+196a^3-67a^2-11a+5}5.
 \end{aligned}                                         \tag{7}
$$



Exact polynomial division modulo $g(a)$ gives



$$
x^2+y^2=a,\qquad
             \operatorname {Re}S(x+iy)=
             \operatorname {Im}S(x+iy)=0.              \tag{8}
$$



Thus $\tau=x+iy$ lies on $|v|=R$ and is a saddle.  Exact interval
Horner evaluation gives the convenient coarse bounds



$$
\frac3{10}<x<\frac12,\qquad
             \frac15<y<\frac14,\qquad R+x>0.           \tag{9}
$$



The half-angle coordinate of $\tau$ satisfies



$$
q_\tau=\frac{y}{R+x}\in
 \left(\frac{11}{40},\frac{69}{250}\right),
 \quad
 y-\frac{11}{40}(R+x)>\frac1{2000},
 \quad
 \frac{69}{250}(R+x)-y>\frac1{10000}.                 \tag{10}
$$



Every inequality in (9)--(10) is an exact rational-interval comparison.

## 3. The angular critical polynomial

For $v=x+iy$ on $x^2+y^2=R^2$, put



$$
A=1+4x+4R^2,\qquad
 B=1+2x+2y+2R^2,\qquad
 C=1+2x+R^2.                                          \tag{11}
$$



They are the squared moduli of $1+2v$, $1+(1-i)v$, and $1+v$.
Since $R<1/2$, none can vanish, and



$$
|\Psi(v)|=\frac{A^3B^3}{R^4C^2}.   \tag{12}
$$



The numerator of the angular logarithmic derivative is



$$
D=-12yBC+6(x-y)AC+4yAB.           \tag{13}
$$



With $q=\tan(\theta/2)$, direct exact expansion gives



$$
\begin{aligned}
 P_R(q)={}&R^4(12q^6+16q^5+12q^4+32q^3-12q^2+16q-12)\\
 &+R^3(-36q^6-80q^5+20q^4+20q^2+80q-36)\\
 &+R^2(39q^6+106q^5-89q^4-44q^3+89q^2+106q-39)\\
 &+R(-18q^6-60q^5+50q^4+50q^2+60q-18)\\
 &+(3q^6+14q^5+3q^4+28q^3-3q^2+14q-3),
                                                               \tag{14}
\end{aligned}
$$



and



$$
D=-\frac{2R}{(1+q^2)^3}P_R(q). \tag{15}
$$



The leading coefficient and discriminant factor exactly as



$$
\operatorname {lc}_qP_R=3(R-1)^2(2R-1)^2,\qquad
 \operatorname {disc}_qP_R=2^{27}R^4H(R),             \tag{16}
$$



where



$$
\begin{aligned}
H(R)={}&20805484544R^{32}+118385819648R^{30}
-461272903680R^{28}-3015229972480R^{26}\\
&+19436998272000R^{24}-51409006671360R^{22}
+83735894372480R^{20}-94424804475520R^{18}\\
&+77503914653480R^{16}-47303904493980R^{14}
+21553646606705R^{12}-7258682924440R^{10}\\
&+1763836890375R^8-296858859770R^6
+32451744695R^4-2075138598R^2+61484669.
                                                               \tag{17}
\end{aligned}
$$



Exact interval Horner arithmetic on the broad interval $J$ proves



$$
400000<H(R)<600000
 \qquad(R\in J).                                       \tag{18}
$$



The leading coefficient is also positive on $J$.  Hence neither a
multiple root nor a root escaping through infinity can occur as $R$
moves within $J$.

## 4. Exactly two critical points and the unique maximum

At the rational base radius $R_0$, the ordinary
$\mathbb Q[q]$-Sturm sequence has degrees
$6,5,4,3,2,1,0$.  Its exact signs are



$$
\begin{array}{c|c|c}
 q&\text{Sturm signs}&V(q)\\ \hline
 -\infty &(+,-,+,-,-,-,+)&4\\
 +\infty &(+,+,+,+,-,+,+)&2 .
 \end{array}                                           \tag{19}
$$



Thus $P_{R_0}$ has exactly two real roots.  Equations (16)--(18), the
connectedness of $J$, and invariance of roots under a simple,
degree-preserving polynomial homotopy prove



$$
\#\{q\in\mathbb R:P_R(q)=0\}=2               \tag{20}
$$



at the selected algebraic embedding $R\in K$.  This argument uses no
Sturm arithmetic over $\mathbb Q(R)$.

Narrow exact interval evaluation at that embedding gives



$$
\begin{array}{c|cccc}
 q&-282&-281&11/40&69/250\\ \hline
 \operatorname {sign}P_R(q)&+&-&-&+\\
 \text{certified bound}
   &>6\!\cdot\!10^9&<-4\!\cdot\!10^9&<-2/25&>3/200 .
 \end{array}                                           \tag{21}
$$



Consequently the two simple roots obey



$$
q_-\in(-282,-281),\qquad
 q_+\in(11/40,69/250).                                 \tag{22}
$$



Because the leading coefficient is positive and the degree is even, their
simplicity gives



$$
\operatorname {sign}P_R(q)=
 \begin{cases}
 +,&q<q_-,\\
 -,&q_-<q<q_+,\\
 +,&q>q_+.
 \end{cases}                                           \tag{23}
$$



The half-angle parameter is strictly increasing with $\theta$.
Equations (12)--(15) therefore give the angular derivative pattern



$$
\operatorname {sign}\frac d{d\theta}\log|\Psi(Re^{i\theta})|=
 \begin{cases}
 -,&q<q_-,\\
 +,&q_-<q<q_+,\\
 -,&q>q_+.
 \end{cases}                                           \tag{24}
$$



At the omitted half-angle point $q=\pm\infty$, equation (15) tends to
$-2R\operatorname {lc}_qP_R<0$, so no critical point is hidden at the
seam.  Equation (8) makes $q_\tau$ a critical root, and (10) identifies
it with $q_+$.  Hence



$$
\boxed{\tau\ \text{is the unique global maximum of }
        |\Psi(v)|\text{ on }|v|=R.}                  \tag{25}
$$



The other critical point $q_-$ is the unique minimum.

## 5. Exact quadratic and determinant signs

At the saddle, put



$$
\lambda=\tau^2(\log\Psi)''(\tau)
 =\frac{(2-2i)\tau S'(\tau)}
 {(1+\tau)(1+2\tau)(1+(1-i)\tau)}.                    \tag{26}
$$



Cross multiplication in $\mathbb Q[a]/(g)$ gives



$$
\begin{aligned}
 \operatorname {Re}\lambda
 &=\frac4{15}
 (3456a^5-11040a^4+9680a^3-2460a^2-810a+217),\\
 \operatorname {Im}\lambda
 &=-\frac2{15}
 (3456a^5-12160a^4+13000a^3-4820a^2-505a+222).
                                                               \tag{27}
\end{aligned}
$$



Exact interval Horner evaluation on $K^2$ proves



$$
2<\operatorname {Re}\lambda<3.             \tag{28}
$$



If $L(\theta)=\log|\Psi(Re^{i\theta})|$, then
$\Psi'(\tau)=0$ gives



$$
L''(\theta_\tau)
 =-\operatorname {Re}\lambda<-2.                    \tag{29}
$$



Thus the unique maximum is nondegenerate.

The other exact algebraic reduction is



$$
\operatorname {Im}\frac{b_2(\tau)}{b_0(\tau)}
 =\frac{(2a-1)(128a^4-416a^3+352a^2-44a-47)}{400}.    \tag{30}
$$



The same exact interval gives



$$
\boxed{
 \frac8{125}
 <\operatorname {Im}\frac{b_2(\tau)}{b_0(\tau)}
 <\frac{13}{200}.}                                    \tag{31}
$$



No denominator was silently canceled.  From $0<R<1/2$,



$$
\tau\ne0,\quad
 1+\tau\ne0,\quad
 1+2\tau\ne0,\quad
 1+(1-i)\tau\ne0,\quad
 1+(1+i)\tau\ne0,                                     \tag{32}
$$



because the moduli of $\tau$, $2\tau$, and
$(1\pm i)\tau$ are respectively $R$, $2R$, and
$\sqrt2R<1$.  Thus (26)--(31) are valid identities, not merely
cross-multiplied necessary conditions.

## 6. Why this is the accessible saddle

The fixed circle is a legitimate coefficient contour.  Apart from the
central coefficient pole at zero, the integrands in the parent contour
formula have their first pole at $v=-1$, while



$$
0<R<\frac12<1.               \tag{33}
$$



The numerator zeros at $-1/2$ and $-(1+i)/2$ create no contour
obstruction.  Therefore the original small coefficient circle can be
expanded directly to $|v|=R$, without crossing a nonzero pole.

There is an equal-modulus saddle outside the pole cycle, arising from
$v\mapsto-1-\overline v$.  Its squared radius is
$1+2x+a>1$, since $x>3/10$.  Hence



$$
|\tau|=R<\frac12<1<
 |-1-\overline\tau|.                                  \tag{34}
$$



It is not discarded by a dominance comparison: it is absent from the
chosen fixed-circle integral because the pole at $-1$ separates the two
radial regions.  The exact unique-maximum theorem (25) is therefore the
appropriate algebraic input for a one-dimensional fixed-circle saddle
analysis.

## 7. Numerical diagnostics and remaining analytic work

For orientation only,



$$
\begin{aligned}
 R&=0.458133387942745883976258263842\ldots,\\
 \tau&=0.393343586940663786762530462701\ldots\\
 &\hspace{2.8em}
 +0.234876613907283175916788717192\ldots\,i,\\
 q_\tau&=0.2758461130900741\ldots .
 \end{aligned}
$$



These decimals are not used for any sign, isolation, or root-count claim.

What remains is analytic rather than algebraic: one must write the uniform
fixed-circle saddle expansion for the two amplitudes $b_0,b_2$, including
the complementary-arc bound and the square-root branch convention.  The
strict unique maximum, the nondegenerate curvature (28)--(29), and the
positive amplitude (31) are now exact inputs to that argument.  This package
does not itself promote the conditional coefficient asymptotic in the
handoff.

## 8. Deterministic replay

From the research directory run

    python3 scripts/mixed_cubic_accessible_saddle_exact_algebraic_certificate.py

The replay uses ordinary rational Sturm arithmetic, exact discriminants,
exact rational interval Horner evaluation, and polynomial reduction in
$\mathbb Q[a]/(g)$.  It checks the pinned parent package and handoff,
source markup, control bytes, and a 40 GiB RAM guard.  It needs no hardware
accelerator.
