> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Mixed-cubic boundary ray: Cartier content, an adjacent recurrence, and the remaining saddle gap

Date: 2026-08-27.

## 1. Scope

Let



$$
u=x(1-x),\qquad Q=(1+x)(1+x^2),\qquad
 H_s=\int_0^1\frac{u^{6m}}{Q^{4m+1+s}}\,dx\quad(s=0,1,2),             \tag{1}
$$



where $m\geq1$.  Write, as in the parent construction,



$$
H_s=R_s+\frac{L_s}{4}\log2+\frac{E_s}{8}\pi,qquad
 R_s,L_s,E_s\in\mathbb Q.                                             \tag{2}
$$



The adjacent log-cancelled form is



$$
\Lambda_{01}=L_1H_0-L_0H_1=A_m+B_m\pi,
 \quad A_m=L_1R_0-L_0R_1,
 \quad B_m=\frac{L_1E_0-L_0E_1}{8}.                                  \tag{3}
$$



This note proves four exact all-parameter facts.

1. A direct dyadic/lcm clearing much smaller than the ambient Hermite
   clearing is available:

   

$$
\boxed{\mathcal D_m=2^{9m+5}M_{4m+1}\quad\hbox{clears both }A_m,B_m,}
                                                                         \tag{4}
$$



   where $M_N=\operatorname {lcm}(1,\ldots,N)$.
   A second Cartier argument removes every prime in $(2m,3m)$, giving

   

$$
\boxed{\mathcal D_m^\sharp=
     \frac{2^{9m+5}M_{4m+1}}{\displaystyle\prod_{2m<p<3m}p}.}          \tag{4a}
$$


2. A Cartier-exactness criterion supplies a proved common-content product.
   In particular, every prime $4m+1<p\leq6m$ divides the common content.
   The full criterion has logarithmic product

   

$$
\left(-4\log2+\frac{\pi}{\sqrt3}+3\log3\right)m+o(m).             \tag{5}
$$


3. The three adjacent integrals in (1) satisfy an exact order-two relation.
   Thus the next adjacent log-cancelled form is only a rational multiple of
   (3); it is not a new approximation.
4. The two endpoint residues admit an exact common-phase contour formula.
   Integration by parts removes their leading ratio $5/8$ and identifies
   the first nontrivial adjacent determinant amplitude.

These theorems do **not** by themselves prove that the normalized
approximation exponent is greater than one.  The final section shows that the
proved arithmetic would cross one by a small margin **if** the indicated
accessible-saddle asymptotic is established.  No saddle limit,
primitive-height limit, irrationality statement, or transcendence statement
is asserted.

## 2. A direct dyadic and odd-denominator clearing

Use the involution



$$
x=\frac{1-y}{1+y}.
$$



Since



$$
Q\left(\frac{1-y}{1+y}\right)
 =\frac{4(1+y^2)}{(1+y)^3},                                             \tag{6}
$$



one obtains, exactly,



$$
H_s=2^{-2m-1-2s}\int_0^1
 \frac{y^{6m}(1-y)^{6m}(1+y)^{1+3s}}
      {(1+y^2)^{4m+1+s}}\,dy.                                          \tag{7}
$$



Put $K_s=4m+1+s$, and let $c_{s,j}$ be the coefficient of
$(y-i)^{-j}$ in the partial-fraction expansion of the integrand in
(7), including its power of two.  Taylor expansion at $i$ gives



$$
c_{s,j}=2^{-2m-1-2s}[t^{K_s-j}]
 \frac{(i+t)^{6m}(1-i-t)^{6m}(1+i+t)^{1+3s}}
      {(2i+t)^{K_s}}.                                                    \tag{8}
$$



After $t=2iv$, the remaining factors are products of



$$
(1+2v)^{6m},\quad (1+(1-i)v)^{6m},\quad
 (1+(1+i)v)^{1+3s},\quad (1+v)^{-K_s},
$$



and hence have Gaussian-integer series coefficients and constant term
one.  Write $\varpi=1+i$, so $v_\varpi(2)=2$.  In (8), including the
outside factor in (7), the denominator valuation is



$$
(4m+2+4s)+2K_s+2(K_s-j)-(6m+1+3s)
 =14m+5+5s-2j.                                                        \tag{8a}
$$



The four terms are respectively the outside power of two, the constant
$(2i)^{K_s}$, the coefficient rescaling, and the numerator constants
$(1-i)^{6m}(1+i)^{1+3s}$.  Replacing two powers of $\varpi$ by one
power of 2 gives



$$
2^{7m+3-j}c_{0,j}\in\mathbb Z[i],\qquad
 2^{7m+5-j}c_{1,j}\in\mathbb Z[i].                                    \tag{9}
$$



The simple pole contributes



$$
c_{s,1}\left(\frac12\log2+\frac{i\pi}{4}\right)
 +\overline{c_{s,1}}
  \left(\frac12\log2-\frac{i\pi}{4}\right),                          \tag{10}
$$



so



$$
L_s=4\operatorname {Re}c_{s,1},\qquad
 E_s=-4\operatorname {Im}c_{s,1}.                                     \tag{11}
$$



For $j\geq2$,



$$
\int_0^1\frac{dy}{(y-i)^j}
 =\frac{(1-i)^{1-j}-(-i)^{1-j}}{1-j}.                                 \tag{12}
$$



The numerator degrees in (7) are $12m+1$ for $s=0$ and $12m+4$
for $s=1$, whereas the denominator degrees are $8m+2$ and
$8m+4$.  Monic division therefore leaves polynomial quotients of
degrees exactly $4m-1$ and $4m$.  Their coefficients have no odd
denominators, and integrating them introduces only the divisors
$1,\ldots,4m$ and $1,\ldots,4m+1$, respectively.  Thus (9) and
(12), together with this quotient calculation, give



$$
\begin{array}{c|c|c}
 &\text{power-of-two clearing}&\text{odd clearing}\ \\ \hline
R_0&2^{7m+2}&M_{4m}\\
R_1&2^{7m+4}&M_{4m+1}.
\end{array}                                                            \tag{13}
$$



For completeness, the logarithmic coordinate has a sharper bound than
(9).  At the root $-1$, substitute $t=2v$ in



$$
\frac{L_s}{2}=[t^{K_s-1}]
 \frac{(-1+t)^{6m}(2-t)^{6m}}{(t^2-2t+2)^{K_s}}.                       \tag{14}
$$



This yields



$$
2^{2m}L_0\in\mathbb Z,\qquad 2^{2m+2}L_1\in\mathbb Z.                \tag{15}
$$



Equations (9), (11), and (15) also give



$$
2^{7m}E_0\in\mathbb Z,qquad 2^{7m+2}E_1\in\mathbb Z.                \tag{16}
$$



Combining (13), (15), and (16) proves



$$
2^{9m+4}M_{4m+1}A_m\in\mathbb Z,qquad
 2^{9m+5}B_m\in\mathbb Z,                                             \tag{17}
$$



and hence (4).  Notice that the odd denominator occurs only in the
rational coordinate; $B_m$ is dyadic.

## 3. Cartier exactness and a common-content theorem

We first record an elementary characteristic-$p$ lemma, in a form which
does not require Cartier-operator terminology.

**Lemma 3.1 (exact differential test).**  Let $p$ be an odd prime and
let $f\in\mathbb F_p(x)$.  If $P\in\mathbb F_p[x]$ has degree at most
$p-2$, then



$$
f(x)^pP(x)\,dx                                                        \tag{18}
$$



is an exact rational differential.

Indeed, all integers $1,\ldots,p-1$ are invertible in $\mathbb F_p$,
so $P=T'$ for a polynomial $T$.  Since $(f^p)'=0$, (18) equals
$d(f^pT)$.

For positive integers $N,K$, write



$$
N=a p+r,\qquad K=b p+s,qquad 0\leq r,s<p,                            \tag{19}
$$



and define



$$
d_p(N,K)=
 \begin{cases}
  2r,&s=0,\\
  2r+3(p-s),&1\leq s<p.
 \end{cases}                                                          \tag{20}
$$



If $s=0$, then in $\mathbb F_p(x)$



$$
\frac{u^N}{Q^K}=\left(\frac{u^a}{Q^b}\right)^p u^r.                  \tag{21}
$$



If $s>0$, then



$$
\frac{u^N}{Q^K}
 =\left(\frac{u^a}{Q^{b+1}}\right)^p u^rQ^{p-s}.                      \tag{22}
$$



The polynomial factors on the right of (21)--(22) have degree
$d_p(N,K)$.  Lemma 3.1 therefore proves:

**Theorem 3.2 (exactness/content criterion).**  Define



$$
\mathcal P_m=\left\{p\text{ odd prime}:
 d_p(6m,4m+1)\leq p-2\ \text{and}\
 d_p(6m,4m+2)\leq p-2\right\}.                                       \tag{23}
$$



For every $p\in\mathcal P_m$, all finite residues of both differentials
in (1) vanish modulo $p$.  Here no splitting assumption is hidden:
$\operatorname {disc}Q=-16$, so $Q$ is separable for every odd
$p$, and its roots lie in at most $\mathbb F_{p^2}$.  The local
Laurent coefficients are integral at $p$, because every root difference
is a unit in that splitting field.  Exactness over $\mathbb F_p(x)$
forces each residue to be zero after extension to $\mathbb F_{p^2}$.
Finally, $L_s,E_s$ are rational linear combinations of these residues
whose only fixed denominators are powers of 2.  Therefore vanishing after
reduction is precisely the assertion



$$
v_p(L_0),v_p(E_0),v_p(L_1),v_p(E_1)\geq1.                            \tag{24}
$$



If



$$
X_m=\mathcal D_mA_m,\qquad Y_m=\mathcal D_mB_m,                      \tag{25}
$$



then



$$
\boxed{\prod_{p\in\mathcal P_m}p\ \mid\ \gcd(X_m,Y_m).}           \tag{26}
$$



To justify the last step even when $p\leq4m+1$, let
$e=v_p(M_{4m+1})$.  Equation (13) gives $v_p(R_s)\geq-e$, while
(24) gives $v_p(A_m)\geq1-e$ and $v_p(B_m)\geq2$.  Multiplication
by $\mathcal D_m$ therefore puts both coordinates in $p\mathbb Z_p$.

There is a particularly simple unconditional subfamily.  If
$4m+1<p\leq6m$, write $6m=p+r$.  Since



$$
3(4m+1)=2p+2r+3,                                                      \tag{27}
$$



the degrees in (20) for $K=4m+1,4m+2$ are respectively $p-3$ and
$p-6$.  Thus



$$
\boxed{\prod_{4m+1<p\leq6m}p\ \mid\ \gcd(X_m,Y_m).}                \tag{28}
$$



No unproved gcd cancellation is used in (26) or (28).

The full criterion has a clean prime-number-theorem constant.  Away from
finitely many interval endpoints, put $p/m\to x>0$.  Then (23) is
equivalent to



$$
2\left\lfloor\frac6x\right\rfloor
 \geq3\left\lfloor\frac4x\right\rfloor+2.                            \tag{29}
$$



This occurs precisely on



$$
\frac4{2j+1}<x<\frac6{3j+1},\qquad j=0,1,2,\ldots.                   \tag{30}
$$



The interval lengths sum to



$$
\begin{aligned}
 \mathfrak C
 &=\sum_{j\geq0}\frac2{(2j+1)(3j+1)}\\
 &=2\left(\psi\left(\frac12\right)-\psi\left(\frac13\right)\right)\\
 &=-4\log2+\frac\pi{\sqrt3}+3\log3\\
 &=2.3370475079987656871\ldots.                                      \tag{31}
 \end{aligned}
$$



The prime number theorem on each fixed finite set of intervals, followed
by the Chebyshev bound for the tail $p\ll m/j$, gives



$$
\log\prod_{p\in\mathcal P_m}p=\mathfrak C m+o(m).                   \tag{32}
$$



## 4. A relative-Cartier cancellation of the middle prime band

We need a termwise endpoint version of Cartier reduction.  The following
elementary formulation is sufficient.

**Lemma 4.1 (relative Cartier endpoint lemma).**  Let $p$ be odd and let
$\omega$ be a rational differential over $\mathbb Z_{(p)}$, with no
pole at 0 or 1.  Suppose its polynomial quotient has degree less than
$2p-1$, all finite poles are separable modulo $p$, and their orders are
at most $2p$.  In the partial-fraction integral from 0 to 1, multiply the
rational endpoint coordinate by $p$, but leave the simple-residue period
coordinates unchanged.  Modulo $p$, this coordinate vector is the
Frobenius of the ordinary endpoint/period coordinate vector of
$\mathcal C(\overline\omega)$, where $\mathcal C$ is the Cartier
operator.

This is a direct termwise calculation.  In the polynomial quotient, only
$y^{p-1}dy$ can acquire a denominator $p$.  At a finite pole, only
$(y-\alpha)^{-p-1}dy$ can do so.  Cartier sends these two terms to
$dy$ and $(y-\overline\alpha)^{-2}dy$, respectively.  For example,



$$
p\int_0^1(y-\alpha)^{-p-1}dy
 =-\left((1-\alpha)^{-p}-(-\alpha)^{-p}\right),                       \tag{32a}
$$



which is the Frobenius of the integral of the corresponding double pole.
The simple poles are fixed by Cartier up to the same Frobenius.  Every
other term has a $p$-integral primitive and vanishes after the rational
coordinate is multiplied by $p$.  This proves the lemma, including when
the poles split only over an unramified quadratic extension.

Now let $p$ be prime with



$$
2m<p<3m,\qquad r=6m-2p,qquad t=4m+1-p.                              \tag{32b}
$$



In the transformed representation (7), put



$$
G(y)=\frac{y^2(1-y)^2}{1+y^2}.                                      \tag{32c}
$$



The two differentials factor modulo $p$ as



$$
\begin{aligned}
 F_0(y)dy&=G(y)^p g_0(y)dy,&
 g_0&=2^{-2m-1}\frac{y^r(1-y)^r(1+y)}{(1+y^2)^t},\\
 F_1(y)dy&=G(y)^p g_1(y)dy,&
 g_1&=2^{-2m-3}\frac{y^r(1-y)^r(1+y)^4}{(1+y^2)^{t+1}}.               \tag{32d}
\end{aligned}
$$



Here $0\leq r<p$, $0<t<p$, and $t+1\leq p$.  Moreover
$g_0=O(y^{-3})$ and $g_1=O(y^{-2})$ at infinity.  Their only finite
poles are $\pm i$, of order at most $p$.  Hence Cartier can retain
only the simple local terms.  Regularity at infinity forces their two
residues to sum to zero, so



$$
\mathcal C(g_s(y)dy)=\gamma_s\frac{dy}{1+y^2}\quad(s=0,1)             \tag{32e}
$$



for some $\gamma_s\in\mathbb F_p$ (the differential is
$\mathbb F_p$-rational).  Cartier semilinearity
therefore gives



$$
\mathcal C(F_s(y)dy)=\gamma_s\Omega,qquad
 \Omega=G(y)\frac{dy}{1+y^2}.                                       \tag{32f}
$$



The hypotheses of Lemma 4.1 hold: the quotient degrees are $4m-1,4m$,
both less than $2p-1$, and the pole orders are at most $2p$.  Thus the
vectors



$$
(pR_s,L_s,E_s)\pmod p                                               \tag{32g}
$$



are proportional for $s=0,1$.  In particular,



$$
pA_m=L_1(pR_0)-L_0(pR_1)\equiv0\pmod p.                             \tag{32h}
$$



Since (13) gives $v_p(A_m)\geq-1$, (32h) proves
$v_p(A_m)\geq0$.  The coordinate $B_m$ is dyadic, so it is already
$p$-integral.  Also $v_p(M_{4m+1})=1$ in this prime range.  We have
proved:

**Theorem 4.2 (middle-band denominator cancellation).**  The number
$\mathcal D_m^\sharp$ in (4a) clears both $A_m$ and $B_m$.
Furthermore, the middle-band primes are disjoint from $\mathcal P_m$:
indeed (20) gives $d_p(6m,4m+1)=2p-3>p-2$.  Consequently



$$
\prod_{q\in\mathcal P_m}q
 \ \mid\ 
 \gcd(\mathcal D_m^\sharp A_m,\mathcal D_m^\sharp B_m).              \tag{32i}
$$



The omitted endpoint $p=3m$ can occur for a prime only at $m=1,p=3$
and is irrelevant to the asymptotic; it can also be checked directly.
By the prime number theorem,



$$
\log\prod_{2m<p<3m}p=m+o(m).                                       \tag{32j}
$$



## 5. An exact three-adjacent recurrence

Set



$$
\begin{aligned}
 a_m&=(10m+2)(10m+3),\\
 b_m&=-(10m+3)(20m+5),\\
 c_m&=8(2m+1)(4m+1),                                                    \tag{33}\\
 S_m(x)&=-(6m+1)-(10m+3)(x+x^2+x^3)-x^4.
\end{aligned}
$$



A direct differentiation gives the polynomial identity



$$
\frac d{dx}\left(\frac{u^{6m+1}S_m(x)}{Q^{4m+2}}\right)
 =\frac{u^{6m}}{Q^{4m+3}}
   \left(a_mQ^2+b_mQ+c_m\right).                                     \tag{34}
$$



The boundary term vanishes at both endpoints.  Hence



$$
\boxed{a_mH_0+b_mH_1+c_mH_2=0.}                                    \tag{35}
$$



The same relation holds separately for $R_s,L_s,E_s$.  If
$\Lambda_{12}=L_2H_1-L_1H_2$, substitution from (35) gives



$$
\boxed{\Lambda_{12}=\frac{a_m}{c_m}\Lambda_{01}.}                   \tag{36}
$$



Thus primitive reduction of the next adjacent pair gives exactly the same
rational approximation.  The signs in (33)--(36) are essential:
$a_m,c_m>0$, while $b_m<0$.

## 6. Exact common-phase residue identity

Let $c_0,c_1$ now denote the simple-pole residues at $y=i$ of the two
integrands in (7).  Define



$$
\Psi(v)=\frac{(1+2v)^6(1+(1-i)v)^6}{v^4(1+v)^4},\qquad
 b_0(v)=\frac{1+(1+i)v}{1+v},                                        \tag{37}
$$



and



$$
r(v)=\frac{1-i}{8}\,
 \frac{(1+(1+i)v)^3}{v(1+v)}.                                       \tag{38}
$$



Coefficient extraction after $t=2iv$ gives, on any sufficiently small
positively oriented circle about zero,



$$
\begin{aligned}
 c_0&=C_m I_0, &
 I_0&=\frac1{2\pi i}\oint\Psi(v)^m b_0(v)\frac{dv}{v},\\
 c_1&=C_m I_1, &
 I_1&=\frac1{2\pi i}\oint\Psi(v)^m b_0(v)r(v)\frac{dv}{v},            \tag{39}\\
 C_m&=2^{-7m-2}(-1)^mi^m(1-i).
\end{aligned}
$$



Put



$$
S(v)=4v^3+(6-i)v^2-iv-1-i.                                         \tag{40}
$$



Exact simplification gives



$$
\frac{\Psi'}{\Psi}
 =\frac{(2-2i)S(v)}{v(1+v)(1+2v)(1+(1-i)v)},
 \qquad
 r(v)-\frac58=\frac{iS(v)}{8v(1+v)}.                                \tag{41}
$$



Thus $r=5/8+h\Psi'/\Psi$, where



$$
h(v)=\frac{-1+i}{32}(1+2v)(1+(1-i)v).                               \tag{42}
$$



Contour integration by parts is exact and yields



$$
I_1-\frac58I_0=\frac1m I_2,qquad
 I_2=\frac1{2\pi i}\oint\Psi(v)^m b_2(v)\frac{dv}{v},                \tag{43}
$$



with



$$
b_2(v)=\frac{(1-i)(4v^4+8v^3+2v^2-2v-1)}
               {32v(1+v)^2}.                                        \tag{44}
$$



By (10)--(11),



$$
B_m=2\operatorname {Im}(c_1\overline{c_0})
 =\frac{2|C_m|^2}{m}\operatorname {Im}(I_2\overline{I_0}).           \tag{45}
$$



This proves an exact one-order cancellation in the adjacent determinant.
It does not, by itself, prove that the contour is governed by any selected
saddle or that (45) is nonzero for every $m$.

## 7. Conditional saddle ledger and the precise remaining hypothesis

This section is deliberately conditional.  It records what the exact
arithmetic theorems above would imply **if** the accessible-saddle analysis
suggested by (39) is completed.

The cubic (40) has a root



$$
\tau=0.3933435869406637868
       +0.2348766139072831759\,i.                                    \tag{46}
$$



At this root, (41) gives $r(\tau)=5/8$, while



$$
\operatorname {Im}\frac{b_2(\tau)}{b_0(\tau)}
 =0.06429869302479854446\ldots\ne0.                                 \tag{47}
$$



The candidate single-residue exponential rate per $n=6m$ is



$$
\ell=\frac{\log|\Psi(\tau)|-7\log2}{6}
 =0.5872327431518037137\ldots.                                      \tag{48}
$$



The positive integral (1) does have a standard rigorous Laplace rate



$$
\phi=\max_{0<x<1}
 \left(\log x+\log(1-x)-\frac23\log Q(x)\right)
 =-1.7498296312071692822\ldots,                                     \tag{49}
$$



where the maximizer is the unique root in $(0,1)$ of
$5x^3+5x^2+5x-3$.

If one proves from (39) that the accessible saddle $\tau$ is uniquely
dominant with a uniform error term, then (43)--(47) predict



$$
\frac1n\log|B_m|\longrightarrow2\ell,qquad
 \limsup\frac1n\log|\Lambda_{01}|\leq\phi+\ell,                     \tag{50}
$$



and hence normalized error exponent



$$
d=\ell-\phi=2.3370623743589729959\ldots.                            \tag{51}
$$



Under this analytic hypothesis, the **proved** sharpened clearing (4a),
the middle-band cancellation (32j), and the disjoint content theorem
(26), (32) yield



$$
\begin{aligned}
 h_{\rm cert}
 &=2\ell+\frac32\log2+\frac12-\frac{\mathfrak C}{6}\\
 &=2.3246783391437311\ldots,                                        \tag{52}\\
 \frac d{h_{\rm cert}}&=1.0053272038\ldots>1.
\end{aligned}
$$



Thus the exact arithmetic now has a positive, but small, conditional margin
for the exponent greater than one required by the proposed combination with
an $e$-form:



$$
d-h_{\rm cert}=0.0123840352152419\ldots\quad\text{per }n.            \tag{53}
$$



The remaining decisive gap in this route is therefore analytic: one must
prove that the saddle $\tau$ in (46) is the uniquely accessible dominant
saddle for both contour integrals in (39), with an error term strong enough
to pass through (43)--(45).  The exact identity (47) then prevents loss of
the first nontrivial determinant amplitude.  Until that contour theorem is
proved, (52)--(53) remain conditional and give no irrationality or
transcendence conclusion.
