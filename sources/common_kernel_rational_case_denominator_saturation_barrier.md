> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Conditional rational-output saturation at the native integer threshold

Checked: 2026-08-27 UTC.

## 1. Verdict

Put



$$
s=e+\pi,
 \qquad
 (1-i)^N=R_N+iI_N,
 \qquad
 a=-I_N,
 \qquad
 b=\frac{N!-R_N}{2}.                                  \tag{1}
$$



Throughout this note, $N\geq2$ is **admissible**, meaning
$I_N\leq0$, or equivalently



$$
N\bmod8\in\{0,1,2,3,4\}.           \tag{2}
$$



Let ${\cal H}_N^{\mathbb Z}$ be the strict native integer localizers:
$h\in\mathbb Z[x]$ has



$$
h\equiv1\pmod{(1+x^2)^2},\qquad h(0)=0,              \tag{3}
$$



and its associated native profile has the strict range and residual signs
on $(0,1)$.  Write its positive output as



$$
{\cal L}_{N,h}=N!s+\rho_{N,h},
 \qquad \rho_{N,h}\in\mathbb Q.                       \tag{4}
$$



The exact real-output theorem supplies two endpoints



$$
0<{\cal L}^{\min}_N<{\cal L}^{0}_N \tag{5}
$$



whose open interval is the complete output set for strict smooth profiles
with the required integral endpoint germs.

This note proves the following conditional saturation theorem.

**Theorem.**  Assume temporarily that



$$
s=\frac uv,
 \qquad (u,v)=1,\qquad v\mid N!,                      \tag{6}
$$



and put $M=N!s\in\mathbb Z$.  Then



$$
\boxed{
 \{{\cal L}_{N,h}:h\in{\cal H}_N^{\mathbb Z}\}
 =\mathbb Q\cap({\cal L}^{\min}_N,{\cal L}^{0}_N).}   \tag{7}
$$



If a member of (7), in lowest terms, is $m/D>0$, then the translated
coordinate has the same reduced denominator:



$$
\rho_{N,h}=\frac{m-MD}{D},
 \qquad (m-MD,D)=1.                                   \tag{8}
$$



Consequently every strict integer localizer obeys



$$
\boxed{D{\cal L}^{0}_N>1.}   \tag{9}
$$



Thus the proposed rationality contradiction
$D{\cal L}^{0}_N<1$ cannot be obtained by selecting a rational output
inside the exact real interval while retaining the rationality hypothesis.

The obstruction is sharp.  For every admissible $N\geq1246$, define



$$
D_N=\left\lfloor\frac N5\right\rfloor+1.    \tag{10}
$$



Then



$$
\boxed{
 {\cal L}^{\min}_N<\frac1{D_N}<{\cal L}^{0}_N.}        \tag{11}
$$



Under (6), (7) therefore gives an $h\in{\cal H}_N^{\mathbb Z}$ with



$$
{\cal L}_{N,h}=\frac1{D_N},
 \qquad
 \rho_{N,h}=\frac{1-MD_N}{D_N},
 \qquad
 D_N{\cal L}_{N,h}=1.                                 \tag{12}
$$



Moreover $D_N$ is the least possible reduced coordinate denominator and



$$
\boxed{
 1<D_N{\cal L}^{0}_N<1+\frac5N.}                      \tag{13}
$$



Hence the positive-integer threshold is attained exactly at the integer
one, and its unavoidable excess tends to zero.  The theorem is conditional
on (6).  It does not prove that $e+\pi$ is rational, irrational, or
transcendental.

## 2. Exact inputs from the frozen native packages

Let



$$
W(t)=(a+bt)t(2-t)^2,
 \qquad
 \ell(Q)=4\int_0^1W(t)Q(t)\,dt.                       \tag{14}
$$



For $h=1+(1+x^2)^2q(x)$, put $Q(t)=q(1-t)$.  The exact output-moment
identity is



$$
\rho_{N,h}=C_N-\ell(Q),
 \qquad C_N\in\mathbb Q.                              \tag{15}
$$



Three previously audited theorems will be used exactly as stated.

1. The fixed-index closure theorem says that every value in
   $({\cal L}_N^{\min},{\cal L}_N^0)$ is produced by a strict smooth
   profile $Q$ whose normalized Taylor coefficients through order three
   at both endpoints are integers.  The profiles may be chosen with stable
   strict endpoint germs.

2. If such a $Q$ has $\ell(Q)\in\mathbb Q$, the exact-moment integer
   approximation theorem gives $P_j\in\mathbb Z[t]$ with the same endpoint
   jets,

   

$$
\ell(P_j)=\ell(Q),
    \qquad
    \|P_j-Q\|_{C^3[0,1]}\longrightarrow0.              \tag{16}
$$



   A sufficiently close approximant retains all strict signs.

3. For every admissible $N\geq8$, the exact interval width satisfies

   

$$
{\cal L}^{0}_N-{\cal L}^{\min}_N>\frac{c_*}{N},
    \qquad
    c_*=16e^{-4}\left(\frac{e^{3/4}}{17}
                       -\frac{e^{1/4}}{25}\right).     \tag{17}
$$



The strict inequality in (17) follows because the explicit pair from the
width theorem lies strictly inside the endpoint interval and has difference
at least $c_*/N$.

Finally, the upper endpoint has the exact integral representation



$$
{\cal L}^{0}_N
 =\int_0^1t^N\left\{e^{1-t}
       +\frac4{1+(1-t)^2}\right\}\,dt.                 \tag{18}
$$



Everything below is an elementary consequence of (14)--(18).

## 3. Proof of rational-output saturation

Assume (6).  If $h\in{\cal H}_N^{\mathbb Z}$, then (15) makes
$\rho_{N,h}$ rational, while $M=N!s$ is an integer.  Thus
${\cal L}_{N,h}=M+\rho_{N,h}$ is rational.  The strict sign theorem places
it in the open interval in (7).  This proves one inclusion.

Conversely, choose



$$
y\in\mathbb Q\cap
              ({\cal L}^{\min}_N,{\cal L}^{0}_N).      \tag{19}
$$



The fixed-index theorem supplies a strict smooth profile $Q$, with integral
endpoint jets, whose output is $y$.  Its translated coordinate is



$$
\rho=y-M\in\mathbb Q.          \tag{20}
$$



Equations (15) and (20) give $\ell(Q)=C_N-\rho\in\mathbb Q$.  Apply
(16), and choose an index large enough that the strict signs survive.  If
$P\in\mathbb Z[t]$ is the resulting approximant, put



$$
q_h(x)=P(1-x),
 \qquad
 h(x)=1+(1+x^2)^2q_h(x).                              \tag{21}
$$



The exact endpoint jets give (3), and the $C^3$ approximation gives the
strict range and residual inequalities.  Since the moment is unchanged,
(15) shows that the output remains exactly $y$.  This proves (7).

Now write $y=m/D>0$ in lowest terms.  Integer translation does not alter
its reduced denominator, because



$$
(m-MD,D)=(m,D)=1.                        \tag{22}
$$



Since $y<{\cal L}^{0}_N$,



$$
1\leq m<D{\cal L}^{0}_N,     \tag{23}
$$



which proves (8)--(9).  Notice that (9) applies to the entire strict integer
class under (6), not merely to the approximants used in the converse.

## 4. The exact denominator immediately below the upper endpoint

Put $u=1-t$.  On $0\leq u\leq1$,



$$
e^u>1+u\quad(u>0),
 \qquad
 \frac4{1+u^2}\geq4(1-u^2).                            \tag{24}
$$



Beta integration in (18) therefore gives



$$
\begin{aligned}
 {\cal L}^{0}_N
 &>\frac5{N+1}
   +\frac1{(N+1)(N+2)}
   -\frac8{(N+1)(N+2)(N+3)}\\
 &=\frac5{N+1}
   +\frac{N-5}{(N+1)(N+2)(N+3)}.
                                                               \tag{25}
 \end{aligned}
$$



In particular,



$$
{\cal L}^{0}_N>\frac5{N+1}
 \qquad(N\geq5).                                      \tag{26}
$$



For the other direction, convexity gives
$e^u\leq1+(e-1)u$, and $4/(1+u^2)\leq4$.  Since $e<3$,



$$
\begin{aligned}
 {\cal L}^{0}_N
 &\leq\frac5{N+1}
   +\frac{e-1}{(N+1)(N+2)}
 <\frac5N.                                             \tag{27}
 \end{aligned}
$$



For $D_N$ from (10), direct division with remainder gives



$$
\frac{N+1}{5}\leq D_N\leq\frac{N+5}{5}.  \tag{28}
$$



Equations (26) and (28) yield



$$
\frac1{D_N}
 \leq\frac5{N+1}<{\cal L}^{0}_N.                      \tag{29}
$$



Also (27) gives $1/{\cal L}^{0}_N>N/5$, whereas (29) gives
$1/{\cal L}^{0}_N<D_N$.  Since $D_N$ is the least integer strictly
larger than $N/5$,



$$
\boxed{
 D_N=\left\lfloor\frac1{{\cal L}^{0}_N}\right\rfloor+1}
 \qquad(N\geq5).                                      \tag{30}
$$



Thus no positive rational below ${\cal L}^{0}_N$ can have reduced
denominator smaller than $D_N$.

## 5. The explicit target lies above the lower endpoint

We first record a rational proof of the convenient bound



$$
c_*>\frac1{50}.          \tag{31}
$$



Rewrite the constant in (17) as



$$
c_*=\frac{16(25e^{1/2}-17)}{425e^{15/4}}. \tag{32}
$$



The positive Taylor series gives



$$
e^{1/2}>1+\frac12+\frac18+\frac1{48}=\frac{79}{48}.  \tag{33}
$$



For $x=15/4$, the ratio of every Taylor term after $x^7/7!$ to its
predecessor is at most $x/8=15/32$.  Hence



$$
\begin{aligned}
 e^{15/4}
 &<\sum_{j=0}^{6}\frac{(15/4)^j}{j!}
   +\frac{(15/4)^7}{7!}\frac1{1-15/32}\\
 &=\frac{333375299}{7798784}<43.                       \tag{34}
 \end{aligned}
$$



The inequality in (31) is equivalent to



$$
32(25e^{1/2}-17)>17e^{15/4}. \tag{35}
$$



Equations (33)--(34) bound the left side below by $2318/3$ and the
right side above by $731$; their difference is $125/3>0$.  This proves
(31) without a decimal approximation.

Combining (17), (27), and (31) now gives



$$
{\cal L}^{\min}_N
 <{\cal L}^{0}_N-\frac{c_*}{N}
 <\frac{5-c_*}{N}
 <\frac{249}{50N}.                                    \tag{36}
$$



For $N\geq1246$,



$$
\frac5{N+5}-\frac{249}{50N}
 =\frac{N-1245}{50N(N+5)}>0.                          \tag{37}
$$



Equations (28), (36), and (37) imply



$$
{\cal L}^{\min}_N
 <\frac{249}{50N}
 <\frac5{N+5}
 \leq\frac1{D_N}.                                     \tag{38}
$$



Together with (29), this proves (11).  The threshold is strict at the only
place it matters: (37) is zero at $N=1245$ and positive beginning at
$N=1246$.

Under (6), apply (7) to $y=1/D_N$.  Its translated numerator is
$1-MD_N$, which is coprime to $D_N$ by (22).  Thus its reduced
coordinate denominator is exactly $D_N$.  Equation (30) proves minimality,
and (27)--(28) give



$$
1<D_N{\cal L}^{0}_N
 <\frac{N+5}{5}\frac5N=1+\frac5N,                     \tag{39}
$$



completing (12)--(13).

## 6. What this theorem does and does not close

The realization in (7) is constructive in the qualitative sense of the
exact-moment theorem, but it gives no useful bound for the degree or
coefficient height of the resulting $h$.  The effective nearest-integer
Bernstein construction from the quantitative audit has a very large
certified degree and controls only a denominator *multiple*; it does not
force the exact moment in (12) or its reduced denominator.  Combining the
two results therefore does not produce a short coefficient list or a new
primitive-content estimate.

More importantly, the theorem does not unconditionally exclude an integer
localizer with $D{\cal L}^{0}_N<1$.  Finding such a localizer by an
independent arithmetic construction would contradict (9) under the
rationality hypothesis and would thereby prove $e+\pi$ irrational.  What
is ruled out here is the attempt to obtain that strict inequality solely by
choosing a rational point in the exact real-output interval and invoking
qualitative exact-moment approximation under the same rationality
hypothesis.  That route instead realizes the boundary integer $1$ and is
asymptotically sharp from above.

No claim about the arithmetic classification of $e+\pi$ is made.

## 7. Deterministic replay

From the research directory run

    python3 scripts/common_kernel_rational_case_denominator_saturation_certificate.py

The certificate checks the five frozen dependency manifests, the exact
Taylor bounds proving $c_*>1/50$, the beta-integral ledger, the residue-
class inequalities defining $D_N$, the strict $1245/1246$ threshold,
the denominator-preserving gcd identity on deterministic exact rows, source
markup, control bytes, and a 40 GiB RAM guard.  The finite rows are replay
diagnostics only; the theorem is proved by the all-parameter inequalities
above.  No accelerator is used or useful for this exact symbolic replay.
