> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Native Taylor--Robin sign control forces factorial-quarter-root degree

Checked: 2026-08-27 UTC.

## 1. Verdict

Put



$$
t=1-x,\qquad u=1+x^2,\qquad
 {\cal T}P=(1-x)P'-xP,
$$



and write



$$
(1-i)^N=R_N+iI_N,\qquad M_N=N!-R_N.                    \tag{1}
$$



For $N\geq2$, the native integral Taylor--Robin correction is



$$
K_N(x)=I_N-\frac{M_N}{2}(1-x).                          \tag{2}
$$



Let $h\in\mathbb Z[x]$ satisfy the full admissibility conditions



$$
h\equiv1\pmod {u^2},\qquad h(0)=0,\qquad
 0\leq h(x)\leq1\quad(0\leq x\leq1),                    \tag{3}
$$



and define



$$
F_{N,h}(x)=(1-x)^N+{\cal T}(hK_N)(x).                  \tag{4}
$$



This note proves an all-parameter sign barrier.

**Native sign theorem.**  If $F_{N,h}$ is one-signed on $[0,1]$,
then it is nonnegative, $I_N\leq0$, and, with $d=\deg h$,



$$
\boxed{
 d^4\geq\frac{M_N(N+1)}{54e}.}                           \tag{5}
$$



When $I_N<0$, there is also the independent bound



$$
\boxed{
 d^2\geq\frac{(-I_N)(N+1)}{8e}.}                         \tag{6}
$$



Both estimates have exact rational corollaries



$$
162d^4>M_N(N+1),\qquad
 24d^2>(-I_N)(N+1)\quad(I_N<0).                          \tag{7}
$$



In particular,



$$
\boxed{
 \log d\geq\frac14N\log N-\frac14N+O(\log N).}           \tag{8}
$$



Thus every sign-controlled native localizer has
factorial-quarter-root degree.  This excludes polynomial degree,
ordinary exponential degree $C^N$, and, more generally,
$\exp(o(N\log N))$.

The raw integral behaves in the opposite way.  For the positive
common-kernel weight



$$
\Omega(t)=e^{1-t}+\frac4{t^2-2t+2},                    \tag{9}
$$



put



$$
L_{N,h}=\int_0^1F_{N,h}(1-t)\Omega(t)\,dt.
$$



Every sign-controlled residual satisfies the two-sided estimate



$$
\boxed{
 \frac1{N+1}\leq L_{N,h}\leq\frac{5e}{N+1}.}             \tag{10}
$$



Consequently the *raw* positive integral automatically tends to zero.
This by itself is not a primitive integer linear form.

Indeed, write the exact rational coordinate as



$$
L_{N,h}=N!(e+\pi)+\frac{c_{N,h}}{D_{N,h}},
 \qquad
 D_{N,h}>0,\quad (c_{N,h},D_{N,h})=1,                   \tag{11}
$$



and set



$$
g_{N,h}=\gcd(N!,c_{N,h}).
$$



After denominator clearing and removal of all content, the positive
primitive output is



$$
\Lambda_{N,h}=\frac{D_{N,h}}{g_{N,h}}L_{N,h}.           \tag{12}
$$



Equations (10)--(12) give the exact bottleneck



$$
\boxed{
 \frac{D_{N,h}/g_{N,h}}{N+1}
 \leq\Lambda_{N,h}
 \leq
 \frac{5e\,D_{N,h}/g_{N,h}}{N+1}.}                      \tag{13}
$$



Thus, along any sign-controlled sequence,



$$
\boxed{
 \Lambda_{N,h}\longrightarrow0
 \quad\Longleftrightarrow\quad
 \frac{D_{N,h}}{g_{N,h}}=o(N).}                         \tag{14}
$$



This cleanly separates the analytic and arithmetic halves.  Sign
control would already make the raw integral small, but it forces an
enormous degree.  A primitive contradiction additionally requires
near-total cancellation of the rational denominator against output
content.  The earlier full-window CRT theorem does not prove (14), and
the present theorem does not construct a sign-controlled $h$.

No conclusion about the arithmetic nature of $e+\pi$ follows.

## 2. Endpoint data forced by integrality

Write



$$
H(t)=h(1-t).
$$



Since $h=1+u^2q$ with $q\in\mathbb Z[x]$, evaluation at $x=1$
gives



$$
h(1)=1+4q(1)\equiv1\pmod4.
$$



The bounds in (3) force



$$
H(0)=h(1)=1,\qquad H(1)=h(0)=0,\qquad 0\leq H\leq1.    \tag{15}
$$



The coefficient $M_N/2$ in (2) is integral.  For $N\geq2$,
$(1-i)^N$ is divisible by $(1-i)^2=-2i$ in
$\mathbb Z[i]$, so $R_N$ is even; $N!$ is also even.
Moreover $M_N>0$: this is direct for $N=2$, and for $N\geq3$,



$$
N!>|1-i|^N=2^{N/2}\geq |R_N|.
$$



At $t=0$, equations (2)--(4) give the exact endpoint value



$$
F_{N,h}(1)=-I_N.                \tag{16}
$$



Hence $I_N>0$ makes nonnegativity impossible.  Since



$$
I_N=-2^{N/2}\sin\frac{N\pi}{4},
$$



the impossible congruence classes are



$$
N\equiv5,6,7\pmod8.             \tag{17}
$$



There is a second integral endpoint constraint.  Suppose $I_N\leq0$,
put



$$
a=-I_N\geq0,\qquad b=\frac{M_N}{2}>0.
$$



Then $K_N(0)=-(a+b)$ in the $x$-coordinate, and



$$
F_{N,h}(0)=1-(a+b)h'(0).        \tag{18}
$$



Nonnegativity of $h$ at its zero endpoint gives $h'(0)\geq0$;
integrality makes $h'(0)$ an integer.  For $N\geq2$, one has
$a+b>1$: at $N=2$ it equals $3$, while for $N\geq3$,
$N!-2^{N/2}>2$ and hence $b=(N!-R_N)/2>1$.  Therefore (18) and
$F_{N,h}(0)\geq0$ force



$$
h'(0)=0,\qquad F_{N,h}(0)=1.    \tag{19}
$$



Thus every positive candidate begins with at least a double zero at
$x=0$.  The much stronger degree obstruction below uses the whole
endpoint layer, not merely this first derivative.

## 3. The exact integrating-factor identity

For an arbitrary polynomial $Y(t)$, the Stein operator is



$$
{\cal T}Y=-tY'(t)-(1-t)Y(t).
$$



Consequently



$$
\left(te^{-t}Y(t)\right)'
 =e^{-t}\{tY'(t)+(1-t)Y(t)\}.                            \tag{20}
$$



Take $Y=HK_N$.  Since $H(1)=0$, both boundary terms in (20)
vanish: the factor $t$ kills the endpoint $t=0$, and $Y(1)=0$.
Equations (4) and (20) therefore give, without any sign hypothesis,



$$
\boxed{
 \int_0^1e^{-t}F_{N,h}(1-t)\,dt
 =\int_0^1e^{-t}t^N\,dt.}                               \tag{21}
$$



The right side is strictly positive.  It follows at once that a
one-signed residual cannot be nonpositive.  Hence every one-signed
residual is nonnegative, proving the first assertion of the theorem.

Assume from now on that $F_{N,h}\geq0$.  By (16), $I_N\leq0$, and



$$
K_N(1-t)=-(a+bt).
$$



A direct product-rule calculation gives



$$
\begin{aligned}
 F_{N,h}(1-t)
 &=t^N+t(a+bt)H'(t)\\
 &\quad+\{a(1-t)+bt(2-t)\}H(t).                         \tag{22}
\end{aligned}
$$



Introduce the positive integrating factor



$$
\mu(t)=t(a+bt)e^{-t}.           \tag{23}
$$



The logarithmic derivative identity



$$
\frac{\mu'}{\mu}
 =\frac1t+\frac{b}{a+bt}-1
 =\frac{a(1-t)+bt(2-t)}{t(a+bt)}
$$



turns (22) into



$$
\boxed{
 (\mu H)'=e^{-t}\{F_{N,h}(1-t)-t^N\}.}                  \tag{24}
$$



Nonnegativity and $H(1)=0$ now imply, for every $0<t\leq1$,



$$
\boxed{
 \mu(t)H(t)
 \leq\int_t^1e^{-s}s^N\,ds
 \leq\frac1{N+1}.}                                      \tag{25}
$$



Equivalently, every positive candidate lies below the explicit endpoint
envelope



$$
\boxed{
 H(t)\leq
 \frac{e^t}{t(a+bt)}
 \int_t^1e^{-s}s^N\,ds.}                                \tag{26}
$$



For $I_N=0$, this specializes to



$$
H(t)\leq
 \frac{2e^t}{M_Nt^2}
 \int_t^1e^{-s}s^N\,ds.
$$



The $t^{-2}$ endpoint layer in this formula is the source of the
fourth-root degree obstruction.

## 4. Markov versus the endpoint envelope

Let $d=\deg h=\deg H$.  The endpoint values in (15) imply $d\geq1$.
Markov's inequality on $[0,1]$ gives



$$
\|H'\|_\infty\leq2d^2.          \tag{27}
$$



At



$$
t_a=\frac1{4d^2},
$$



equations (15) and (27) give $H(t_a)\geq1/2$.
Using $e^{-t_a}\geq e^{-1}$ in (25) yields



$$
\frac{a}{8ed^2}\leq\frac1{N+1},
$$



which proves (6).

For the factorial term, use instead



$$
t_b=\frac1{3d^2}.
$$



Then $H(t_b)\geq1/3$, and the $bt^2$ part of (23)--(25) gives



$$
\frac{b}{27ed^4}\leq\frac1{N+1}.
$$



Since $b=M_N/2$, this is exactly (5).

For a completely rational version, the elementary series estimate



$$
e=\sum_{j=0}^\infty\frac1{j!}
 <2+\sum_{j=2}^\infty\frac1{2^{j-1}}=3
$$



turns (5)--(6) into (7).

Finally, $|R_N|\leq2^{N/2}=o(N!)$, so



$$
\log M_N=\log N!+o(1)
          =N\log N-N+O(\log N).
$$



Taking logarithms in (5) proves (8).

For the degree-$48q+13$ CRT localizers of the preceding package,
(5) has the concrete consequence



$$
q\geq
 \frac1{48}
 \left(\frac{M_N(N+1)}{54e}\right)^{1/4}
 -\frac{13}{48}.                                        \tag{28}
$$



Thus a sign-compatible member of that family would require a
factorial-quarter-root localization parameter.  This is a necessary
condition only; it does not assert that such a member exists.

## 5. Raw weighted size

Set



$$
B_N=\int_0^1e^{-t}t^N\,dt.
$$



Since $e^{-1}\leq e^{-t}\leq1$,



$$
\frac{e^{-1}}{N+1}
 \leq B_N\leq\frac1{N+1}.                               \tag{29}
$$



Equation (21) fixes the exponential part of the common-kernel integral:



$$
\int_0^1e^{1-t}F_{N,h}(1-t)\,dt=eB_N.                  \tag{30}
$$



On the other hand,



$$
\frac{\Omega(t)}{e^{-t}}
 =e+\frac{4e^t}{t^2-2t+2}\leq5e
 \qquad(0\leq t\leq1).                                  \tag{31}
$$



If $F_{N,h}\geq0$, equations (29)--(31) prove (10).  In
particular, the raw integral is already of exact order $1/N$;
localization cannot make it asymptotically smaller than this scale.

## 6. Primitive normalization

The Taylor identity is



$$
N!+{\cal T}P_N^{(0)}=(1-x)^N,
$$



where $P_N^{(0)}\in\mathbb Z[x]$.  The correction (2) repairs its
two Robin defects.  Since $h\equiv1\pmod {u^2}$,



$$
{\cal T}(hK_N)-{\cal T}K_N
$$



is divisible by $u$.  Hence the polynomial



$$
P_{N,h}=P_N^{(0)}+hK_N
$$



is Robin, and



$$
Q_{N,h}=\frac{F_{N,h}-N!}{u}\in\mathbb Z[x].            \tag{32}
$$



The exact common-kernel output formula gives



$$
L_{N,h}
 =N!(e+\pi)-N!-P_{N,h}(0)
   +4\int_0^1Q_{N,h}(x)\,dx.                             \tag{33}
$$



Thus the non-$e+\pi$ coordinate is rational, proving (11).
After multiplying (11) by $D_{N,h}$, the two integer coefficients are



$$
N!D_{N,h},\qquad c_{N,h}.
$$



Their content is



$$
\begin{aligned}
 \gcd(N!D_{N,h},c_{N,h})
 &=\gcd(N!,c_{N,h})\\
 &=g_{N,h},                                               \tag{34}
\end{aligned}
$$



because $(D_{N,h},c_{N,h})=1$.  Dividing by (34) proves
(12).  Multiplying (10) by $D_{N,h}/g_{N,h}$ proves
(13)--(14).

In particular, even obtaining one primitive value below one requires



$$
D_{N,h}<g_{N,h}(N+1)\leq N!(N+1).                      \tag{35}
$$



More importantly, a sequence of primitive values tending to zero
requires the much sharper ratio $D_{N,h}/g_{N,h}=o(N)$.
Neither a large raw polynomial degree nor cancellation of one prime
window alone proves this ratio.

There is also a useful rational-approximation normalization.  Put



$$
q_{N,h}=\frac{N!D_{N,h}}{g_{N,h}},\qquad
 p_{N,h}=-\frac{c_{N,h}}{g_{N,h}}.                       \tag{36}
$$



These are coprime integers with $q_{N,h}>0$, and (11) gives the
identity



$$
\boxed{
 \left|(e+\pi)-\frac{p_{N,h}}{q_{N,h}}\right|
 =\frac{L_{N,h}}{N!}.}                                  \tag{37}
$$



Consequently every sign-controlled candidate satisfies



$$
\boxed{
 \frac1{(N+1)N!}
 \leq
 \left|(e+\pi)-\frac{p_{N,h}}{q_{N,h}}\right|
 \leq\frac{5e}{(N+1)N!}.}                              \tag{38}
$$



This exposes a second, stronger arithmetic threshold.  Suppose that
for some fixed $0<\delta<1/2$, infinitely many $N\to\infty$ admit
sign-controlled $h$ for which



$$
q_{N,h}\leq(N!)^{1/2-\delta}.                          \tag{39}
$$



Then $e+\pi$ would be transcendental.  Here is the complete
conditional argument.  If $e+\pi=A/B$ were rational, in lowest terms,
then the strict positivity in (38) and elementary separation of unequal
rationals would give



$$
\left|(e+\pi)-\frac{p_{N,h}}{q_{N,h}}\right|
 \geq\frac1{Bq_{N,h}},
$$



which contradicts (38)--(39) for large $N$.  If $e+\pi$ were
algebraic irrational, take $\varepsilon=2\delta$.  Since



$$
(1/2-\delta)(2+\varepsilon)
 =1-\delta-2\delta^2<1,
$$



the upper bound in (38) is eventually strictly smaller than
$q_{N,h}^{-2-\varepsilon}$.  The denominators must be unbounded (a
bounded-denominator sequence cannot approach an irrational number), so
this contradicts Roth's theorem.  Thus both algebraic cases would be
excluded.

Condition (39) is exactly



$$
\boxed{
 \frac{g_{N,h}}{D_{N,h}}
 \geq(N!)^{1/2+\delta}.}                                \tag{40}
$$



Neither (39) nor (40) is proved here.  In particular, (14), which is
the exact threshold for decay of the primitive *linear form*, is much
weaker than the Roth-scale threshold (40) for this conditional
transcendence route.

## 7. Exact scope and replay

The theorem applies to every integral $h$ satisfying (3), regardless
of its sparsity, coefficient height, order at zero, or construction.
It proves:

* outright impossibility for $N\equiv5,6,7\pmod8$;
* factorial-quarter-root degree for every remaining sign-controlled
  candidate;
* exact $1/N$ raw weighted size;
* the necessary and sufficient denominator/content condition (14) for
  primitive decay;
* the exact rational-approximation identity (37) and the conditional
  Roth-scale threshold (40).

It does **not** prove that a sign-controlled polynomial exists in the
remaining residue classes, and it does not prove or refute (14).
Accordingly it is a rigorous analytic obstruction and reduction, not a
proof about $e+\pi$.

The deterministic exact replay verifies the Gaussian recurrence,
endpoint identities, integrating-factor algebra, rational versions of
the degree bounds, raw moment identity, common-kernel divisibility, and
primitive-content formula in representative symbolic and exact cases.
From the research directory run

    python3 scripts/common_kernel_native_sign_endpoint_degree_certificate.py
    sha256sum -c results/common_kernel_native_sign_endpoint_degree_hashes.sha256

The replay uses exact CPU arithmetic.  No hardware accelerator is useful
for these small symbolic and integer calculations, and RAM use stays far
below the available $50$ GiB.

The Diophantine-approximation theorem used above is K. F. Roth,
``Rational approximations to algebraic numbers,'' *Mathematika* **2**
(1955), 1--20.
