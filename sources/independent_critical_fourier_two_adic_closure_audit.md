> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the critical-Fourier $2$-adic closure

Date: 2026-08-26.

## 1. Verdict and frozen inputs

**Verdict: accept, with the scope stated in the source.**

This audit independently reconstructed the proofs in the following frozen
trio:

| artifact | SHA-256 |
|---|---|
| sources/independent_critical_fourier_two_adic_closure.md | 8ac8fcf223ca5b0950d45308ae69b526484285fc43ed9a1e32ebbf57db9cde32 |
| scripts/independent_critical_fourier_two_adic_closure_certificate.py | 4d02b9e471f281b0c6bc214b1ff5c496ffbc9c004c3f4e6627c2e7ccaf937b57 |
| results/independent_critical_fourier_two_adic_closure.json | 4962773d41014e19d7ef8d7010a4a75f45bdb3ee93a65de348365bee61015663 |

The accepted all-degree conclusions are:



$$
v_2(C_0)
 =r+s_2(K)+(r\bmod2)v_2(K),                                                \tag{A1}
$$





$$
v_2(R_{n,k})
 \geq-k-\lfloor\log_2K\rfloor,                                            \tag{A2}
$$



and, whenever $R_{n,k}\neq0$,



$$
\mathcal L_{n,k}=A+B\pi\longrightarrow+\infty
 \quad\text{uniformly for}\quad
 k\geq\frac1{35}n\log n.                                                   \tag{A3}
$$



Here $n=2r$, $K=k-1$, and
$J_{n,k}=R_{n,k}+Q_{n,k}\pi$, with
$R_{n,k}/Q_{n,k}=A/B$ in lowest terms and $B>0$.

The scope distinction is essential.  Equation (A3) is a theorem about the
primitive $\pi$-component.  For $R_{n,k}\neq0$, it does **not** prove that
the fully primitive matched $e+\pi$-form diverges, because an odd divisor
of $\gcd(q_n,B)$ may survive as final content.  The exceptional branch
$R_{n,k}=0$ is different: there $A+B\pi=\pi$, and the matched form is
already primitive and diverges.  No assertion about the rationality,
irrationality, algebraicity, or transcendence of $e+\pi$ follows.

## 2. Normalizations

For positive even $n=2r$ and $K=k-1\geq2r$, set



$$
J_{n,k}
 =\int_0^1\frac{x^{2r}(1-x)^{2r}}{(1+x^2)^{K+1}}\,dx
 =R_{n,k}+Q_{n,k}\pi.                                                     \tag{A4}
$$



The accepted Fourier normalization gives



$$
Q_{n,k}=\frac{C_0}{2^{2K+2}}=\frac{C_0}{2^{2k}}>0.                        \tag{A5}
$$



When $R\neq0$, write



$$
\frac RQ=\frac AB,\qquad
 A\in\mathbb Z,\quad B\in\mathbb Z_{>0},\quad\gcd(A,B)=1.                  \tag{A6}
$$



Then



$$
\mathcal L_{n,k}=A+B\pi=\frac BQJ_{n,k}>0.                               \tag{A7}
$$



These signs and powers of $2$ agree with the direct Fourier identity:
the constant Fourier mode contributes
$2^{-2K}C_0(\pi/4)=C_0\pi/2^{2K+2}$.

## 3. Independent reconstruction of $v_2(C_0)$

### 3.1 The beta-moment sum

After $x=\tan t$, the full-period mean defining $C_0$ is



$$
C_0
 =2^{2K}\frac1{2\pi}\int_0^{2\pi}
 \sin^{2r}t(\cos t-\sin t)^{2r}
 \cos^{2(K-2r)}t\,dt.                                                     \tag{A8}
$$



For nonnegative $m,\ell$, put



$$
S(m,\ell)=\frac{(2m)!(2\ell)!}{m!\ell!(m+\ell)!}.                         \tag{A9}
$$



Expanding the middle factor in (A8), all odd mixed moments vanish.  The
standard full-period beta integral then gives exactly



$$
C_0=\sum_{j=0}^{r}\binom{2r}{2j}
 S(r+j,K-r-j).                                                            \tag{A10}
$$



Every pair in (A10) has coordinate sum $K$.  Legendre's formula therefore
gives, term by term,



$$
v_2(S(m,K-m))=s_2(K).                                                     \tag{A11}
$$



Thus the issue is the cancellation among the odd normalized summands, not
their individual valuations.

### 3.2 The common numerator

Put $q=K-2r$.  Direct factorial cancellation gives



$$
\frac{S(r+j,K-r-j)}{S(r,K-r)}
 =\prod_{t=0}^{j-1}
   \frac{2r+1+2t}{2K-2r-1-2t}.                                           \tag{A12}
$$



The common odd denominator is



$$
D_r(K)=\prod_{t=0}^{r-1}
 \bigl(2K-(2r+1+2t)\bigr).                                                \tag{A13}
$$



Writing



$$
A_j^{(r)}=\prod_{t=0}^{j-1}(2r+1+2t),\qquad
 B_j^{(q)}=\prod_{t=0}^{j-1}(2q+1+2t),
$$



the common numerator is



$$
N_r(K)=\sum_{j=0}^{r}
 \binom{2r}{2j}A_j^{(r)}B_{r-j}^{(q)}
 \in\mathbb Z[K],                                                        \tag{A14}
$$



and



$$
\frac{C_0}{S(r,K-r)}=\frac{N_r(K)}{D_r(K)}.                              \tag{A15}
$$



### 3.3 EGF identity and the essential odd prefactor

Define



$$
f_a(z)=\sum_{j\geq0}
 \frac{\prod_{t=0}^{j-1}(2a+1+2t)}{(2j)!}z^{2j}.
$$



Formal differentiation of $e^{z^2/2}$, equivalently Kummer's
transformation, yields



$$
f_a(z)=e^{z^2/2}
 \sum_{u=0}^{a}a^{\underline u}\frac{2^uz^{2u}}{(2u)!}.                   \tag{A16}
$$



Since $N_r=(2r)![z^{2r}]f_r f_q$, coefficient extraction gives



$$
\boxed{
 \frac{N_r(K)}{2^r}
 =(2r-1)!!
 \sum_{\substack{u,v,w\geq0\\u+v+w=r}}
 \binom r{u,v,w}
 \frac{r^{\underline u}q^{\underline v}}
 {(2u-1)!!(2v-1)!!}.}                                                    \tag{A17}
$$



The prefactor $(2r-1)!!$ in (A17) is indispensable for the exact identity.
For example, at $r=2,q=0$, the bare triple sum is $17/3$, whereas
$N_r/2^r=17$.  Because the missing factor would be odd, omitting it would
leave a parity-only argument accidentally unchanged; the frozen source
correctly retains it.

All denominators on the right of (A17) are odd, and the falling factorials
have integer coefficients.  Hence $N_r/2^r\in\mathbb Z_{(2)}[K]$.
Because $N_r\in\mathbb Z[K]$, each coefficient of $N_r/2^r$ lies in



$$
\mathbb Z[1/2]\cap\mathbb Z_{(2)}=\mathbb Z.
$$



Thus



$$
G_r(K):=\frac{N_r(K)}{2^r}\in\mathbb Z[K].                               \tag{A18}
$$



### 3.4 Parity and the odd-$r$ factor $K$

Reduce (A17) modulo two.  A falling factorial of length at least two contains
an even factor, so only $u,v\leq1$ survive.  The $(u,v)=(1,1)$ term has
the even multinomial factor $r(r-1)$.  Therefore



$$
G_r(K)\equiv1+r+rq\pmod2.                                                \tag{A19}
$$



Since $q=K-2r$, equation (A19) is odd for every $K$ when $r$ is even,
and is congruent to $K$ when $r$ is odd.

For odd $r$, polynomially continue (A12)--(A15) to $K=0$.  The denominator
is nonzero and the $j$-th quotient is $(-1)^j$.  Hence



$$
\frac{N_r(0)}{D_r(0)}
 =\sum_{j=0}^{r}(-1)^j\binom{2r}{2j}
 =\operatorname{Re}(1+i)^{2r}=0.                                         \tag{A20}
$$



Thus $G_r(K)=KP_r(K)$ for some $P_r\in\mathbb Z[K]$.  It remains to
exclude an additional factor of two when $K$ is even.  Differentiate
(A17) at $K=0$, hence at the even value $q=-2r$.  Modulo two, derivatives
with $v\geq3$ vanish, as do terms with $u\geq2$.  The only potentially
odd pairs are



$$
(u,v)=(0,1),(1,1),(0,2),(1,2).
$$



For odd $r$, their parities are



$$
1,\quad0,\quad\frac{r-1}{2},\quad\frac{r-1}{2}.
$$



The last two cancel, so $G_r'(0)$ is odd.  It follows that $P_r(K)$ is
odd at even $K$; at odd $K$, (A19) already makes $G_r(K)/K$ odd.
Consequently



$$
N_r(K)=2^rK^{\,r\bmod2}P_r(K),
 \qquad P_r(K)\ \text{odd for every integer }K.                           \tag{A21}
$$



Equations (A11), (A13), (A15), and (A21) prove (A1) exactly.

## 4. Independent monomial-coordinate bound

### 4.1 Even monomials

For $0\leq a\leq K$, let



$$
I_{2a,k}=\int_0^1\frac{x^{2a}}{(1+x^2)^k}\,dx,
\qquad
 E_{a,k}=I_{2a,k}-\frac14
 B\left(a+\frac12,k-a-\frac12\right).                                    \tag{A22}
$$



The beta term is the homogeneous $\pi$-coordinate.  Integrating the
derivative of $x^{2a-1}(1+x^2)^{1-k}$ gives



$$
E_{a,k}
 =\frac{2a-1}{2k-2a-1}E_{a-1,k}
 -\frac{1}{2^{k-1}(2k-2a-1)}.                                            \tag{A23}
$$



The substitution $x\mapsto1/x$ in the tail from $1$ to infinity gives



$$
E_{a,k}+E_{K-a,k}=0.                                                     \tag{A24}
$$



If $K$ is even, (A24) anchors the recurrence at
$E_{K/2,k}=0$.  If $K$ is odd, (A23)--(A24) give the two central anchors



$$
E_{(K-1)/2,k}=\frac1{2^kK},
 \qquad
 E_{(K+1)/2,k}=-\frac1{2^kK}.                                             \tag{A25}
$$



All recurrence multipliers in (A23), forward or backward, are ratios of odd
integers, and the inhomogeneous term has valuation at least $-(k-1)$.
Since $K$ is odd in (A25), the anchor valuation is $-k$.  Therefore



$$
v_2(E_{a,k})\geq-k                                                       \tag{A26}
$$



for every $a$.

### 4.2 Odd monomials

For $0\leq a<K$, set $\lambda=K-a$.  The substitutions $u=x^2$ and,
in the tail, $t=1/(1+u)$, give the exact rational formula



$$
I_{2a+1,k}
 =\frac12\left[
 \frac{a!(\lambda-1)!}{K!}
 -\sum_{j=0}^{a}(-1)^j\binom aj
 \frac{2^{-(\lambda+j)}}{\lambda+j}
 \right].                                                               \tag{A27}
$$



Here $1\leq\lambda+j\leq K$.  Each tail term has valuation at least
$-k-\lfloor\log_2K\rfloor$, and the beta term satisfies the same, in fact
slightly stronger, estimate.  Thus



$$
v_2(I_{2a+1,k})
 \geq-k-\lfloor\log_2K\rfloor.                                            \tag{A28}
$$



### 4.3 Reassembly

Expanding $x^{2r}(1-x)^{2r}$, its rational coordinate is



$$
R_{n,k}
 =\sum_{j=0}^{r}\binom{2r}{2j}E_{r+j,k}
 -\sum_{j=0}^{r-1}\binom{2r}{2j+1}
 I_{2(r+j)+1,k}.                                                         \tag{A29}
$$



The nonarchimedean triangle inequality applied to (A26)--(A28) proves
(A2).  Combining (A1), (A2), and (A5), when $R\neq0$, gives



$$
v_2(A/B)
 \geq k-r-s_2(K)-(r\bmod2)v_2(K)
       -\lfloor\log_2K\rfloor.                                           \tag{A30}
$$



With $\ell_2=\lfloor\log_2K\rfloor$,
$s_2(K)\leq\ell_2+1$, and $v_2(K)\leq\ell_2$, the conservative form is



$$
v_2(A/B)\geq D_{n,k}:=k-r-3\ell_2-1.                                    \tag{A31}
$$



If $D_{n,k}>0$, coprimality in (A6) forces $B$ odd and
$2^{D_{n,k}}\mid A$.

## 5. Audit of the high-region limit

The elementary pointwise estimate



$$
|\sin t(\cos t-\sin t)|
 \leq\gamma:=\frac{1+\sqrt2}{2}
$$



gives



$$
Q_{n,k}\leq\frac{\gamma^n}{4}<\gamma^n.                                 \tag{A32}
$$



For $t=\frac14\sqrt{n/k}$, integration over $x\in[t,2t]$, together with
$\log(1-2t)\geq-4t$ and
$(1+n/(4k))^k\leq e^{n/4}$, gives



$$
J_{n,k}\geq
 \left(\frac14\sqrt{\frac nk}\right)^{n+1}
 \exp\left(-n\sqrt{\frac nk}-\frac n4\right).                             \tag{A33}
$$



If $A>0$, then $\mathcal L\geq A\geq2^D$.  If $A<0$, positivity of
$\mathcal L=A+B\pi$ implies $B>2^D/\pi$.  In both cases, weakening the
first bound by $J/(\pi\gamma^n)<1$, equations (A7) and (A32) give



$$
\mathcal L_{n,k}
 \geq\frac{2^{D_{n,k}}J_{n,k}}{\pi\gamma^n}.                              \tag{A34}
$$



Substitution of (A31) and (A33) yields the source's logarithmic lower bound
$\Phi_n(k)$.  Its derivative satisfies



$$
\Phi_n'(k)\geq
 \log2-\frac3{k-1}-\frac{n+1}{2k},                                       \tag{A35}
$$



because the derivative of $-n\sqrt{n/k}$ is positive.  Uniformly for
$k\geq n\log n/35$, the right side is positive for all sufficiently large
$n$.  The lower bound is therefore minimized at the left endpoint.  There,



$$
\frac{\Phi_n(k)}n
 =\frac{\log2}{35}\log n
 -\frac12\log\left(\frac{\log n}{35}\right)+O(1)
 \longrightarrow+\infty.                                                 \tag{A36}
$$



This proves (A3), including uniformity when $k$ grows arbitrarily faster
than $n\log n$.  No unstated saddle-point or upper restriction on $k$
is used.

If $R=0$, lowest terms give $(A,B)=(0,1)$, so the primitive
$\pi$-form is $\pi$, not a divergent sequence.  Minimal matching with
$E_n=q_ne-p_n$, where $\gcd(p_n,q_n)=1$, gives



$$
E_n+q_n\pi=q_n(e+\pi)-p_n.
$$



It is already primitive and is at least $q_n\pi\geq\pi n^n$.  Thus the
source handles this branch correctly and does not falsely call the
primitive $\pi$-component divergent.

## 6. Fully primitive matching: exact content and limitation

For $R\neq0$, let $E_n=q_ne-p_n$ be the primitive beta form.  Its
two-step recurrence has even coefficient and odd initial values, so both
$p_n$ and $q_n$ are odd.  Put



$$
d=\gcd(q_n,B),\qquad q_n=dq_0,\qquad B=dB_0.                              \tag{A37}
$$



The minimally matched raw form has constant and common $e,\pi$
coefficients



$$
M=-B_0p_n+q_0A,\qquad
 C=\frac{q_nB}{d}=dq_0B_0.                                                \tag{A38}
$$



If a prime divides $q_0$, reduction of $M$ leaves the unit
$-B_0p_n$.  If a prime divides $B_0$, reduction leaves the unit
$q_0A$.  Therefore



$$
\gcd(M,q_0B_0)=1,
$$



not just at the level of primes but prime-power by prime-power.  The final
content is consequently



$$
\boxed{
 g=\gcd(M,C)=\gcd(M,d).}                                                   \tag{A39}
$$



This sharpens the often-used statement $g\mid d$.  Since $q_n$ is odd,
$d$ and $g$ are odd; parity does not make them equal to one.

The finite example in the frozen certificate is exact:



$$
n=2,\quad k=10,\quad
 (A,B)=(-149056,135135),\quad
 (p_2,q_2)=(19,7).                                                        \tag{A40}
$$



Here



$$
d=7,\qquad
 M=-515851,\qquad
 C=135135,\qquad
 g=\gcd(M,C)=7.                                                           \tag{A41}
$$



Therefore a proof that $A+B\pi\to+\infty$ is insufficient by itself after
matching: the normalized matched lower bound contains the divisor product
$dg$.  Neither (A1) nor (A2) controls its odd part.  The correct final
classification is:

* in the accepted low region $n<k\leq n\log n/35$, the previously proved
  irrationality-measure bound controls the fully primitive matched form;
* in the high region $k\geq n\log n/35$ and $R\neq0$, the new theorem
  proves primitive $\pi$-form divergence only;
* in the special high-region branch $R=0$, direct matching is primitive
  and diverges;
* a uniform high-region theorem for the fully primitive matched form with
  $R\neq0$ remains open because the odd gcd (A39) is uncontrolled.

## 7. Independent execution and hygiene

I reran the frozen certificate with a separate output path:

    python scripts/independent_critical_fourier_two_adic_closure_certificate.py \
      --output /tmp/independent_critical_fourier_two_adic_closure.audit.json

The rerun completed successfully and was byte-for-byte identical to the
archived JSON.  Its SHA-256 was again

    4962773d41014e19d7ef8d7010a4a75f45bdb3ee93a65de348365bee61015663

The rerun independently covered 1,296 central-coefficient cases, 700
monomial-coordinate cases, and nine Gaussian-Fourier spot checks.  The two
record-stream hashes were

    central:    fd6bec10d692b3b535b39375315a9431219ddf05e62b1de1304f347ff5fad880
    coordinate: 881d1f1ac09902571c9dec378ab4d4cd5942cdd6013c730f9c7a05b918ea3c63

These calculations validate the implementation but are not used as a
substitute for any all-degree proof above.

The frozen theorem source renders with Pandoc and MathJax without stderr.
Its inline and display delimiters are balanced; its equation tags are unique;
UTF-8 decoding passes; and it contains no C0 control bytes or carriage
returns.  The earlier duplicated prefactor fragment in equation (28) is absent
from the frozen SHA: the exact identity has one, and only one, essential
$(2r-1)!!$ prefactor.

## 8. Final assessment

The exact $C_0$ valuation, the independent monomial bound, and the uniform
high-region analytic estimate are mathematically sound.  The source also
states the boundary of the theorem correctly.  It closes the $2$-adic
primitive-$\pi$ component in the high critical-Fourier region; it does not
close the odd final-content problem for fully matched $e+\pi$ forms when
$R\neq0$.
