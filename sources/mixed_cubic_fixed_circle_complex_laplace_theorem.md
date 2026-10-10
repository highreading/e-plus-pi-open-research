> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Mixed-cubic boundary ray: the fixed-circle complex-Laplace theorem

Date: 2026-08-27.

## 1. Scope and status

This note audits and completes the analytic implication that was left informal
in item 133 and in
sources/mixed_cubic_accessible_saddle_handoff_20260827.md. It has two parts.

1. The contour orientation, the integration-by-parts sign, and the passage
   from the two contour integrals to the determinant coefficient $B_m$ are
   derived again from the raw coefficient extraction.
2. A self-contained fixed-circle complex-Laplace lemma proves the full leading
   term, including its phase, Gaussian constant, $O(m^{-1})$ relative
   error, and eventual sign.

All local hypotheses of the lemma are certified algebraically below. The
formerly open global condition



$$
\tag{UM}
 |\Psi(\rho e^{i\theta})|<|\Psi(\tau)|
 \quad\text{whenever}\quad
 \rho e^{i\theta}\ne\tau .
$$



is now a theorem of the separately frozen exact-algebraic package
sources/mixed_cubic_accessible_saddle_exact_algebraic_certificate.md. Its
four pinned artifacts have SHA-256 hashes

- source:
  $55454aa99b2fcd06a87d94c1b51bedd912a740b731ba57eecfc391bd4572fc65$;
- script:
  $ee24e16ce7e13781792898deead7736cfd9539ba16dc0dbc97b89fa3d061bccb$;
- JSON:
  $f3377fda1444c21e11483688f7059446c5b709841f8914bdce8f68d2916c6ae0$;
- manifest:
  $3521a1347ec499acf98d60bdd8f48ba991ef2a9e20c00c806313e91d1e5d8b10$.

That package proves (UM) by exact rational Sturm arithmetic, a
discriminant/leading-coefficient homotopy, and exact rational interval
signs. Consequently the theorem for $B_m$ below is unconditional. No
claim about the irrationality or transcendence of $e+\pi$ is made here.

## 2. Raw residue and contour orientation audit

For $m\geq1$, let $c_s$ be the residue at $y=i$ of the transformed
integrand belonging to



$$
H_s=2^{-2m-1-2s}\int_0^1
 \frac{y^{6m}(1-y)^{6m}(1+y)^{1+3s}}
      {(1+y^2)^{4m+1+s}}\,dy,
 \qquad s=0,1.
$$



Put



$$
\begin{aligned}
 \Psi(v)&=\frac{(1+2v)^6(1+(1-i)v)^6}{v^4(1+v)^4},\\
 b_0(v)&=\frac{1+(1+i)v}{1+v},\\
 r(v)&=\frac{1-i}{8}\,
       \frac{(1+(1+i)v)^3}{v(1+v)},                                  \tag{1}\\
 C_m&=2^{-7m-2}(-1)^m i^m(1-i).
 \end{aligned}
$$



The raw Taylor formula for the simple-pole coefficient is



$$
c_s=2^{-2m-1-2s}[t^{4m+s}]
 \frac{(i+t)^{6m}(1-i-t)^{6m}(1+i+t)^{1+3s}}
      {(2i+t)^{4m+1+s}}.                                             \tag{2}
$$



Substituting $t=2iv$ in (2), retaining the coefficient-rescaling factor
$(2i)^{-(4m+s)}$, gives exactly



$$
\begin{aligned}
 c_0&=C_m[v^{4m}]
 \frac{(1+2v)^{6m}(1+(1-i)v)^{6m}(1+(1+i)v)}
      {(1+v)^{4m+1}},\\
 c_1&=C_m\frac{1-i}{8}[v^{4m+1}]
 \frac{(1+2v)^{6m}(1+(1-i)v)^{6m}(1+(1+i)v)^4}
      {(1+v)^{4m+2}}.                                                \tag{3}
 \end{aligned}
$$



On a positively oriented circle about zero, Cauchy's coefficient formula
therefore gives



$$
\begin{aligned}
 c_0&=C_m I_0,&
 I_0&=\frac1{2\pi i}\oint\Psi(v)^m b_0(v)\frac{dv}{v},\\
 c_1&=C_m I_1,&
 I_1&=\frac1{2\pi i}\oint\Psi(v)^m b_0(v)r(v)\frac{dv}{v}.            \tag{4}
 \end{aligned}
$$



There is no orientation reversal in (4). In particular, with
$v=\rho e^{i\theta}$ and increasing $\theta$, one has
$dv/v=i\,d\theta$, and hence



$$
\frac1{2\pi i}\oint\Psi(v)^m b(v)\frac{dv}{v}
 =\frac1{2\pi}\int_{-\pi}^{\pi}
   \Psi(\rho e^{i\theta})^m b(\rho e^{i\theta})\,d\theta.             \tag{5}
$$



The logarithmic and arctangent coordinates of the original integral obey



$$
L_s=4\operatorname{Re}c_s,
 \qquad E_s=-4\operatorname{Im}c_s.                                  \tag{6}
$$



Consequently, for



$$
B_m=\frac{L_1E_0-L_0E_1}{8},                                       \tag{7}
$$



the sign in the residue determinant is



$$
B_m=2\operatorname{Im}(c_1\overline{c_0})
    =2|C_m|^2\operatorname{Im}(I_1\overline{I_0}).                    \tag{8}
$$



Indeed, if $c_s=a_s+ib_s$, then the right side of (7) is
$2(a_0b_1-a_1b_0)=2\operatorname{Im}(c_1\overline{c_0})$.

Now set



$$
\begin{aligned}
 S(v)&=4v^3+(6-i)v^2-iv-1-i,\\
 h(v)&=\frac{-1+i}{32}(1+2v)(1+(1-i)v),\\
 b_2(v)&=\frac{(1-i)(4v^4+8v^3+2v^2-2v-1)}
                {32v(1+v)^2}.                                      \tag{9}
 \end{aligned}
$$



Direct rational simplification gives



$$
\begin{aligned}
 \frac{\Psi'}{\Psi}
 &=\frac{(2-2i)S(v)}
 {v(1+v)(1+2v)(1+(1-i)v)},\\
 r(v)-\frac58&=h(v)\frac{\Psi'(v)}{\Psi(v)},\\
 b_2(v)&=-v\frac d{dv}\left(\frac{b_0(v)h(v)}v\right).               \tag{10}
 \end{aligned}
$$



The differentiated expression in (10) is a single-valued rational
function. Integration by parts on the closed, positively oriented contour
has no boundary term. The minus sign from integration by parts cancels the
minus sign in the last line of (10), giving



$$
I_1-\frac58I_0=\frac1m I_2,
 \qquad
 I_2=\frac1{2\pi i}\oint\Psi(v)^m b_2(v)\frac{dv}{v}.                 \tag{11}
$$



Since $(5/8)I_0\overline{I_0}$ is real, (8) and (11) give the exact
identity



$$
\boxed{
 B_m=\frac{2|C_m|^2}{m}
 \operatorname{Im}(I_2\overline{I_0}).}                              \tag{12}
$$



The integrands in (4) and (11) have no finite pole other than $0$ and
$-1$. Thus the initially small coefficient circles may be expanded to
any $0<\rho<1$ without crossing a pole. Zeros of $\Psi$ are not contour
obstructions. For the local logarithm used below, we take
$\rho<1/2$; then the zeros $-1/2$ and $-(1+i)/2$ also lie off a whole
annular neighborhood of the circle.

## 3. A self-contained fixed-circle complex-Laplace lemma

**Lemma 3.1.** Let $0<\rho$, and suppose that $\Psi$ is holomorphic and
nonzero on an annular neighborhood of $|v|=\rho$. Let $b$ range over a
fixed finite family of functions holomorphic on that neighborhood. Suppose
there is a point



$$
\tau=\rho e^{i\theta_0}
$$



such that



$$
\Psi'(\tau)=0,
 \qquad
 |\Psi(\rho e^{i\theta})|<|\Psi(\tau)|
 \quad(\theta\not\equiv\theta_0\pmod {2\pi}).                         \tag{13}
$$



Define



$$
\lambda=\tau^2(\log\Psi)''(\tau).                                  \tag{14}
$$



If $\operatorname{Re}\lambda>0$, then, uniformly over the fixed family,



$$
J_m(b):=\frac1{2\pi i}\oint_{|v|=\rho}
 \Psi(v)^m b(v)\frac{dv}{v}
 =\frac{\Psi(\tau)^m}{\sqrt{2\pi m}\sqrt\lambda}
  \left(b(\tau)+O(m^{-1})\right).                                   \tag{15}
$$



The contour is positively oriented, and $\sqrt\lambda$ is the unique
square root with positive real part. Equivalently, there are constants
$K,m_0$, independent of the chosen member of the finite family, such that



$$
\left|
 J_m(b)-\frac{\Psi(\tau)^m b(\tau)}
 {\sqrt{2\pi m}\sqrt\lambda}
 \right|
 \leq K|\Psi(\tau)|^m m^{-3/2}
 \qquad(m\geq m_0).                                                   \tag{16}
$$



**Proof.** Shift the angular interval so that it is centered at
$\theta_0$, and write $v=\tau e^{iu}$, $-\pi\leq u\leq\pi$. On a
small complex disk about $u=0$, choose a branch of the logarithm and put



$$
\Phi(u)=\log\frac{\Psi(\tau e^{iu})}{\Psi(\tau)},
 \qquad a(u)=b(\tau e^{iu}).                                        \tag{17}
$$



The chosen logarithm affects neither $e^{m\Phi}$ nor any derivative.
The chain rule and $\Psi'(\tau)=0$ give



$$
\Phi(0)=\Phi'(0)=0,
 \qquad \Phi''(0)=-\tau^2(\log\Psi)''(\tau)=-\lambda.                 \tag{18}
$$



Because $\operatorname{Re}\lambda>0$, after shrinking a fixed
$\delta>0$ there is $c>0$ such that



$$
\operatorname{Re}\Phi(u)\leq-cu^2
 \qquad(|u|\leq\delta).                                               \tag{19}
$$



The strict unique maximum in (13), compactness, and periodicity give an
$\eta>0$ such that the remaining arc contributes at most



$$
O\bigl(|\Psi(\tau)|^m e^{-\eta m}\bigr).                            \tag{20}
$$



On $|u|\leq\delta$, Taylor expansion gives, with constants uniform over
the fixed amplitude family,



$$
\Phi(u)=-\frac\lambda2u^2+\gamma_3u^3+O(u^4),
 \qquad a(u)=a(0)+a'(0)u+O(u^2).                                    \tag{21}
$$



Split the local integral at $|u|=m^{-2/5}$. By (19), the part with
$m^{-2/5}\leq|u|\leq\delta$ is
$O(|\Psi(\tau)|^m e^{-c m^{1/5}})$. In the central part put
$u=t/\sqrt m$. Uniformly for $|t|\leq m^{1/10}$, (21) gives



$$
\begin{aligned}
 e^{m\Phi(t/\sqrt m)}a(t/\sqrt m)
 =e^{-\lambda t^2/2}\biggl[&a(0)
 +m^{-1/2}\{a'(0)t+a(0)\gamma_3t^3\}\\
 &+O\bigl(m^{-1}(1+|t|^8)\bigr)\biggr],                              \tag{22}
 \end{aligned}
$$



where, after increasing its constant, the error is dominated by an
integrable multiple of
$(1+|t|^8)e^{-(\operatorname{Re}\lambda)t^2/4}$. The entire
$m^{-1/2}$ term in braces is odd, so its integral over the symmetric
central interval is zero. Extending the remaining Gaussian integral to the
real line costs an exponentially small amount. For
$\operatorname{Re}\lambda>0$, analytic continuation of the real Gaussian
identity gives



$$
\int_{-\infty}^{\infty}e^{-\lambda t^2/2}\,dt
 =\frac{\sqrt{2\pi}}{\sqrt\lambda},                                  \tag{23}
$$



with the stated square-root branch. Combining (5), (20)--(23), and
$du=dt/\sqrt m$ proves (15)--(16). Taking the maximum of finitely many
analytic bounds makes the constants uniform over the amplitude family.
$\square$

## 4. Exact local algebraic certificate for the selected saddle

Let



$$
g(a)=128a^6-384a^5+280a^4-20a^3-55a^2+a+2.                         \tag{24}
$$



There is exactly one zero $a$ of $g$ in



$$
\frac{1049431}{5000000}<a<\frac{2098863}{10000000};                 \tag{25}
$$



the two endpoints are $0.2098862$ and $0.2098863$. Define



$$
\begin{aligned}
 x(a)&=-\frac{(4a+1)(16a^4-52a^3+49a^2-18a+1)}5,\\
 y(a)&=\frac{64a^5-208a^4+196a^3-67a^2-11a+5}{5},\\
 \tau&=x(a)+iy(a),\qquad \rho=\sqrt a.                               \tag{26}
 \end{aligned}
$$



Exact reduction modulo $g$ gives



$$
x(a)^2+y(a)^2=a,
 \qquad S(\tau)=0.                                                    \tag{27}
$$



In particular, $|\tau|=\rho<1/2$. The first identity in (10), and the
fact that none of its displayed denominator factors vanishes at $\tau$,
give $\Psi'(\tau)=0$.

At this saddle, exact reduction modulo $g$ gives



$$
\lambda=
 \frac{(2-2i)\tau S'(\tau)}
 {(1+\tau)(1+2\tau)(1+(1-i)\tau)},                                  \tag{28}
$$



and



$$
\begin{aligned}
 \operatorname{Re}\lambda
 &=\frac4{15}(3456a^5-11040a^4+9680a^3-2460a^2-810a+217)>0,\\
 \operatorname{Im}\lambda
 &=-\frac2{15}(3456a^5-12160a^4+13000a^3-4820a^2-505a+222).          \tag{29}
 \end{aligned}
$$



The exact checker accompanying this note proves the first inequality by a
rational Sturm query on (25). Numerically,
$\lambda=2.1621300694\ldots-0.2244185193\ldots i$, but no floating-point
sign is used in the proof.

Finally,



$$
\operatorname{Im}\frac{b_2(\tau)}{b_0(\tau)}
 =\frac{(2a-1)(128a^4-416a^3+352a^2-44a-47)}{400}>0.                 \tag{30}
$$



Indeed, (25) gives $0<a<1/4$, so $2a-1<0$; and



$$
128a^4-416a^3+352a^2-44a-47
 <128(1/4)^4+352(1/4)^2-47<0.                                      \tag{31}
$$



Also $b_0(\tau)\ne0$: both the zero of its numerator and its pole have
modulus at least $1/\sqrt2>\rho$. Therefore



$$
\mathcal A:=\operatorname{Im}
       (b_2(\tau)\overline{b_0(\tau)})
 =|b_0(\tau)|^2
  \operatorname{Im}\frac{b_2(\tau)}{b_0(\tau)}>0.                   \tag{32}
$$



Equations (24)--(32) certify every local saddle and amplitude hypothesis of
Lemma 3.1. The pinned exact-algebraic package certifies the remaining global
condition (UM).

## 5. The determinant asymptotic, with phase and sign

**Theorem 5.1.** For the algebraic $\rho,\tau$ in (24)--(26), with the
square root fixed by
$\operatorname{Re}\sqrt\lambda>0$,



$$
I_j=
 \frac{\Psi(\tau)^m}{\sqrt{2\pi m}\sqrt\lambda}
 \left(b_j(\tau)+O(m^{-1})\right),
 \qquad j=0,2,                                                       \tag{33}
$$



and the two error constants can be chosen equal. Consequently,



$$
\operatorname{Im}(I_2\overline{I_0})
 =\frac{|\Psi(\tau)|^{2m}}{2\pi m|\lambda|}
 \left(\mathcal A+O(m^{-1})\right).                                  \tag{34}
$$



There is no residual saddle phase in (34): if



$$
K_m=\frac{\Psi(\tau)^m}{\sqrt{2\pi m}\sqrt\lambda},
$$



then



$$
K_m\overline{K_m}
 =\frac{|\Psi(\tau)|^{2m}}{2\pi m|\lambda|}.                         \tag{35}
$$



Since



$$
|C_m|^2
 =\left|2^{-7m-2}(-1)^mi^m(1-i)\right|^2
 =2^{-14m-3},                                                        \tag{36}
$$



the exact identity (12) yields



$$
\boxed{
 B_m=
 \frac{2^{-14m-3}|\Psi(\tau)|^{2m}}
      {\pi m^2|\lambda|}
 \left(\mathcal A+O(m^{-1})\right).}                                 \tag{37}
$$



In particular, $B_m>0$ for every sufficiently large $m$, and



$$
\lim_{m\to\infty}\frac1{6m}\log|B_m|
 =\frac{2\log|\Psi(\tau)|-14\log2}{6}.                               \tag{38}
$$



If



$$
\ell=\frac{\log|\Psi(\tau)|-7\log2}{6},                            \tag{39}
$$



then the right side of (38) is $2\ell$.

**Proof.** Apply Lemma 3.1 to the finite amplitude family
$\{b_0,b_2\}$. Multiply the two expansions, conjugate the $I_0$
expansion, and take imaginary parts to obtain (34). Equations (12), (32),
and (36) then give (37), its eventual positive sign, and (38).
$\square$

## 6. Discharged hypotheses and limits of the result

The frozen exact-algebraic dependency proves that the angular derivative of
$|\Psi(\rho e^{i\theta})|$ has exactly two zeros on the circle and has the
sign pattern that makes $\tau$ its unique maximum. Thus every hypothesis
of Lemma 3.1 used in Theorem 5.1 has now been discharged exactly; no
floating-point root count is used.

No additional steepest-descent accessibility hypothesis is needed after
(UM): the original positively oriented coefficient contour itself is the
fixed circle $|v|=\rho$. The equal-modulus saddle outside the pole at
$-1$ lies on a different radius and does not contribute to this integral.

The $O(m^{-1})$ in (33)--(37) is a rigorous asymptotic existence statement,
not an explicit numerical error constant or an explicit threshold for the
eventual sign. Such constants could be extracted from exact annular and
angular bounds, but they are unnecessary for the logarithmic rate.

Finally, every downstream height comparison or $e$-form matching argument
is outside this theorem and remains to be re-audited separately. In
particular, this note does not use the previously recorded $d>h$ matching
claim. It proves the contour-to-$B_m$ asymptotic only and does not imply
irrationality or transcendence of $e+\pi$.
