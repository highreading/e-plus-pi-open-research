> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A quantitative lower bound for the low-degree root-of-unity endpoint polynomial

Checked: 2026-08-27 UTC

## 1. Verdict

Let



$$
s=e+\pi
\tag{1}
$$



and assume temporarily that $s$ is algebraic.  The constrained
root-of-unity Hermite--Padé construction considered in
`sources/root_unity_constrained_hermite_pade_audit.md` has the form



$$
R(z)=\sum_{j=0}^{m}A_j(z)e^{jz},\qquad
 S(z)=\sum_{j=0}^{m}(-1)^jA_j(z),\qquad \deg S\le D.
\tag{2}
$$



At the endpoint $z=i\pi$,



$$
R(i\pi)=S(i\pi).
\tag{3}
$$



After making the *endpoint polynomial* $S$, rather than the entire
Hermite--Padé vector, primitive over the integers, (3) becomes the value at
$e$ of a degree-$D$ polynomial with algebraic-integer coefficients.
This note gives a completely normalized lower bound for every nonzero such
value.

Put



$$
r=[\mathbb Q(s):\mathbb Q].
\tag{4}
$$



For fixed $r,D$, if $P\in\mathcal O_{\mathbb Q(s,i)}[X]\setminus\{0\}$
has degree at most $D$ and coefficient house at most $H$, then the
strongest lower bound used here is



$$
|P(e)|\ge H^{-\left(r^2D+r-1+o(1)\right)}
 \qquad(H\longrightarrow\infty).
\tag{5}
$$



The sign in the exponent is perhaps clearer in logarithmic form:



$$
-\log|P(e)|\le
 \bigl(r^2D+r-1+o(1)\bigr)\log H.
\tag{6}
$$



Equation (5) is not an ineffective appeal to Lindemann--Weierstrass.  Section
4 gives an explicit finite-$H$ version, including every hypothesis and
constant, by taking the relative polynomial norm down to $\mathbb Q(i)$
and applying Theorem 2.1 of Ernvall-Hytönen--Matala-aho--Seppälä.  Section 5
also records the completely explicit all-height alternative supplied by
Proposition 1 of Fischler--Rivoal.

The comparison with the constrained Hermite--Padé branch is decisive but
does not finish the main problem.

* For fixed $D$, a contradiction requires the **primitive endpoint
  value**, not merely the unscaled remainder, to beat the exponent
  $r^2D+r-1$.  The height of coefficients that disappear from $S$ is
  irrelevant.
* In the $m=1$, fixed-$D$ family, put

  

$$
b_D=2\lfloor D/2\rfloor+1.
  \tag{7}
$$



  The companion audit proves, with the exceptional trivial cases separated,

  

$$
\frac{|C_n(i\pi)|}{H(C_n)}=\Theta_D(b_D^{-n})
  \tag{8}
$$



  for the primitive endpoint polynomial $C_n$.  Under algebraicity of
  $s$, (5) and (8) force

  

$$
\bigl(r^2D+r+o(1)\bigr)\log H(C_n)
  \ge n\log b_D.
  \tag{9}
$$



  Thus $\log H(C_n)=o(n)$ along an infinite subsequence would prove that
  $e+\pi$ is transcendental.  On the other hand,
  $\log H(C_n)\asymp n\log n$ makes the primitive endpoint value grow;
  it gives no contradiction.  If the heights on the selected subsequence
  are bounded rather than tending to infinity, there are only finitely many
  primitive integer endpoint polynomials; (8) then gives the contradiction
  directly.  Thus the asymptotic height hypothesis in (5) hides no bounded
  subsequence exception.
* For $D=2$, the exact survivor is a consecutive tangent-number gcd.
  If $n\in\{2q-1,2q\}$, the primitive endpoint is

  

$$
C_q(z)=P_q+Q_qz^2,
  \quad
  Q_q=\frac{T_{q+1}}
  {\gcd\bigl(T_{q+1},\,8q(2q+1)T_q\bigr)},
  \tag{10}
$$



  where $T_q$ is the $q$-th tangent number.  The companion audit proves

  

$$
|C_q(i\pi)|=\left(\frac{8\pi^2}{9}+o(1)\right)Q_q9^{-q}.
  \tag{11}
$$



  Consequently, algebraicity of degree $r$ forces

  

$$
\bigl(2r^2+r+o(1)\bigr)\log Q_q\ge2q\log3.
  \tag{12}
$$



  In particular, $\log Q_q=o(q)$ on an infinite subsequence would prove
  transcendence, for every possible finite algebraic degree $r$.  No such
  upper bound is known.  Conversely, even the plausible estimate
  $\log\gcd(T_q,T_{q+1})=o(q\log q)$ would make $Q_q$ factorially large
  and the endpoint value in (11) grow.  It would close this family in the
  negative direction, not prove the main theorem.
* If $D=D_n\to\infty$, $m$ is fixed,
  $\log H(P_n)\asymp n\log n$, and the actual endpoint smallness has only
  the factorial scale

  

$$
-\log|P_n(e)|=O_m(n\log n),
  \tag{13}
$$



  then (6) is weaker by a factor comparable to $D_n$.  Hence neither fixed
  $D$ nor the statement $D=o(n)$ alone creates a contradiction.  A
  surviving growing-parameter regime would have to keep the primitive
  endpoint height much smaller, or let $m$ grow at least on the
  $r^2D$ scale while retaining the analytic gain.

The exact missing arithmetic condition is therefore a primitive endpoint
height/content theorem.  The lower bound does not prove that condition and
does not classify $e+\pi$.

## 2. The correct endpoint normalization

The normalization issue is essential because an arbitrarily rescaled
algebraic-coefficient polynomial has no absolute lower bound.

Suppose $S\ne0$.  There is a unique rational scaling up to sign for which



$$
C(z)=c_0+c_1z+\cdots+c_dz^d\in\mathbb Z[z],
 \qquad \gcd(c_0,\ldots,c_d)=1,
 \qquad d\le D.
\tag{14}
$$



The same scaling is applied to $R$, so (3) becomes



$$
R_{\rm end}(i\pi)=C(i\pi).
\tag{15}
$$



Choose a positive rational integer $\delta$ such that



$$
\theta=\delta s\in\mathcal O_{\mathbb Q(s)}
\tag{16}
$$



and define



$$
P_C(X)=\delta^d C\bigl(i(s-X)\bigr).
\tag{17}
$$



For every term of degree $j$,



$$
\delta^d c_ji^j(s-X)^j
 =c_ji^j\delta^{d-j}(\theta-\delta X)^j.
\tag{18}
$$



It follows coefficientwise that



$$
P_C\in\mathcal O_K[X],\qquad K=\mathbb Q(s,i),\qquad
 \deg P_C=d,
\tag{19}
$$



and, using $s-e=\pi$,



$$
P_C(e)=\delta^d C(i\pi).
\tag{20}
$$



The polynomial in (17) is nonzero whenever $C\ne0$.  Its value at $e$
is also nonzero, either because $i\pi$ is transcendental or because
Lindemann's theorem says that $e$ is transcendental over the algebraic
coefficient field.

Let



$$
H(C)=\max_j|c_j|,
 \qquad
 \Theta=\max_{\tau:\mathbb Q(s)\hookrightarrow\mathbb C}|\tau(\theta)|.
\tag{21}
$$



Taking the coefficient $\ell^1$-norm in (18) gives the explicit house
bound



$$
H(P_C)\le(d+1)H(C)(\Theta+\delta)^d.
\tag{22}
$$



The inverse affine substitution $C(z)=\delta^{-d}P_C(s+iz)$ gives a
bound in the other direction.  Thus, for fixed hypothetical $s$ and
$\delta$,



$$
\bigl|\log H(P_C)-\log H(C)\bigr|
 =O_{s,\delta}(d+\log(d+1)).
\tag{23}
$$



This proves that fixed-degree comparisons may use $H(C)$, but only after
the endpoint polynomial itself has been made primitive.  The primitive
height of the full vector $(A_0,\ldots,A_m)$ can be much larger and does
not occur in (17).

If $S=0$, there is no nonzero endpoint polynomial to which a
transcendence measure can be applied.  Any complete construction must prove
$S\ne0$ on its selected infinite family.

## 3. Relative norm down to the Gaussian field

Put



$$
E=\mathbb Q(s),\qquad F=\mathbb Q(i),\qquad K=EF.
\tag{24}
$$



In its distinguished embedding, $E\subset\mathbb R$.  Hence



$$
E\cap F=\mathbb Q,\qquad [K:F]=[E:\mathbb Q]=r.
\tag{25}
$$



Let



$$
P(X)=\sum_{j=0}^{D}a_jX^j\in\mathcal O_K[X]\setminus\{0\},
 \qquad
 H=\max_{j,\sigma}|\sigma(a_j)|\ge1.
\tag{26}
$$



Take the polynomial norm



$$
Q(X)=N_{K/F}(P(X))
 =\prod_{\tau:K/F\hookrightarrow\overline{\mathbb Q}}P^\tau(X).
\tag{27}
$$



Because the coefficients of $P$ are integral,



$$
Q\in\mathcal O_F[X]=\mathbb Z[i][X],\qquad
 Q\ne0,\qquad \deg Q\le M:=rD.
\tag{28}
$$



For a fixed coefficient of the product in (27), the first $r-1$ input
degrees determine the last.  There are at most $(D+1)^{r-1}$ choices.
Therefore



$$
H(Q)\le T:=(D+1)^{r-1}H^r.
\tag{29}
$$



At the distinguished embedding,



$$
Q(e)=P(e)\prod_{\tau\ne1}P^\tau(e).
\tag{30}
$$



Since $e>1$, every remaining factor satisfies



$$
|P^\tau(e)|\le (D+1)e^DH=:B_0.
\tag{31}
$$



Both $Q(e)$ and every factor in (30) are nonzero because $e$ is
transcendental.  Combining any lower bound for a Gaussian-integer
polynomial $Q(e)$ with (30)--(31) yields



$$
|P(e)|\ge |Q(e)|B_0^{-(r-1)}.
\tag{32}
$$



The descent to $\mathbb Q(i)$, rather than all the way to $\mathbb Q$,
is useful.  The 2019 primary theorem applies over every imaginary quadratic
field.  A full rational norm would replace $rD$ by $2rD$ and lose a
factor four in the leading height exponent.

## 4. A completely explicit finite-height theorem

The primary source in this section is

> A.-M. Ernvall-Hytönen, T. Matala-aho, and L. Seppälä,
> “On Mahler's Transcendence Measure for $e$,” *Constructive
> Approximation* **49** (2019), 405--444,
> [DOI 10.1007/s00365-018-9429-3](https://doi.org/10.1007/s00365-018-9429-3),
> Theorem 2.1.

The inspected author version was arXiv:1704.01374v3, dated 2 May 2018, with
SHA-256

    151e8e659be98c50bf931f1d9c35faa54c4a9a770e0d9ed66724593974d3c4dd

The paper explicitly states that all of its results hold over an imaginary
quadratic field.  The notation needed for its theorem is reproduced here so
that no constant is hidden.

For an integer $M\ge2$, put



$$
\mathfrak s_M=
 \begin{cases}
 e,&M=2,\\
 M(\log M)^2,&M\ge3.
 \end{cases}
\tag{33}
$$



For $M\ge5$, define



$$
\kappa_M={1\over M}
 \sum_{\substack{p\le(M+1)/2\\p\ \mathrm{prime}}}
 \min_{0\le j\le M}
 \left(\left\lfloor{j\over p}\right\rfloor+
       \left\lfloor{M-j\over p}\right\rfloor\right)
 {\log p\over p-1}\,
 w_p(\mathfrak s_Me^{\mathfrak s_M}),
\tag{34}
$$



where



$$
w_p(x)=1-{p\over x}-{p-1\over\log p}{\log x\over x}.
\tag{35}
$$



Set



$$
\mathfrak d_M=
 \begin{cases}
 0.3654,&M=2,\\
 0.5139,&M=3,\\
 1.6016,&M=4,\\
 (M+\tfrac12)\log M-(1+\kappa_M)M-1.02394,&M\ge5,
 \end{cases}
\tag{36}
$$





$$
\mathfrak B_M=
 \begin{cases}
 2.4099,&M=2,\\
 3.6433,&M=3,\\
 9.7676,&M=4,\\
 M^2\log M-(1+\kappa_M)M^2+(M+1)\log(M+1)\\
 \qquad+\tfrac12M\log M-(1.02394+\kappa_M)M+0.0000525,
 &M\ge5,
 \end{cases}
\tag{37}
$$



and



$$
\mathfrak D_M=
 \begin{cases}
 3.8111,&M=2,\\
 5.1819,&M=3,\\
 7.3631,&M=4,\\
 (M+1)\log(M+1)-\kappa_MM+0.0000525+Me^{-\mathfrak s_M},
 &M\ge5.
 \end{cases}
\tag{38}
$$



Let $z(y)$ denote the inverse on $[1/e,\infty)$ of $x\mapsto x\log x$.
For $T\ge1$, define $\varepsilon_M(T)$ by



$$
\varepsilon_M(T)\log(2T)=
 \mathfrak B_M z\!\left(
 {\log(2T)\over1-\mathfrak d_M/\mathfrak s_M}\right)
 +M\log z\!\left(
 {\log(2T)\over1-\mathfrak d_M/\mathfrak s_M}\right).
\tag{39}
$$



The cited theorem says that, provided



$$
\log T\ge\mathfrak s_Me^{\mathfrak s_M},
\tag{40}
$$



every nonzero $(\lambda_0,\ldots,\lambda_M)\in\mathbb Z[i]^{M+1}$
with $\max_{1\le j\le M}|\lambda_j|\le T$ satisfies



$$
\left|\sum_{j=0}^{M}\lambda_je^j\right|
 >{1\over2e^{\mathfrak D_M}}(2T)^{-M-\varepsilon_M(T)}.
\tag{41}
$$



If $Q$ in (28) has degree below $M$, append zero coefficients.  Thus
(41) applies to it.  Equations (29), (31), (32), and (41) prove the exact
lower bound



$$
\boxed{
 |P(e)|>
 { (2T)^{-M-\varepsilon_M(T)}
  \over
  2e^{\mathfrak D_M}\bigl((D+1)e^DH\bigr)^{r-1}},
 \quad
 M=rD,\qquad T=(D+1)^{r-1}H^r,
 }
\tag{42}
$$



whenever $M\ge2$ and (40) holds.  This is the promised completely
explicit bound.

For direct use with the primitive rational endpoint in Section 2, suppose
$d=\deg C\ge1$, and define



$$
\mathcal H_C=(d+1)H(C)(\Theta+\delta)^d,
 \qquad
 \mathcal T_C=(d+1)^{r-1}\mathcal H_C^r.
$$



Taking $H=\mathcal H_C$ in the theorem gives the fully expanded
 endpoint corollary



$$
|C(i\pi)|>
 {\delta^{-d}(2\mathcal T_C)^{-rd-
       \varepsilon_{rd}(\mathcal T_C)}
  \over
  2e^{\mathfrak D_{rd}}
  \bigl((d+1)e^d\mathcal H_C\bigr)^{r-1}},
$$



provided $rd\ge2$ and


$$
\log\mathcal T_C\ge
\mathfrak s_{rd}e^{\mathfrak s_{rd}}
$$

.  This displays every clearing and
field-height factor seen by the endpoint; no coefficient of the rest of
the Hermite--Padé vector occurs.  If $d=0$, primitivity makes
$C=\pm1$, so there is no small endpoint to estimate.

For fixed $M$, the inverse-function formula gives
$\varepsilon_M(T)=O_M(1/\log\log T)$.  Since



$$
\log T=r\log H+O_{r,D}(1),
\tag{43}
$$



(42) immediately yields (5)--(6): the norm polynomial contributes
$r(rD)=r^2D$ powers of $H$, and the other $r-1$ factors in (30)
contribute the remaining $r-1$.

If $D=0$, the relative norm in (27) is a nonzero Gaussian integer, so
(30)--(32) immediately give $|P(e)|\ge H^{-(r-1)}$, exactly the exponent
in (5).  The other exceptional case $M=1$ means $r=D=1$.  It also
admits an elementary explicit estimate, so no ineffective measure is being
hidden.  Put
$\varphi=(1+\sqrt5)/2$.  For $T\ge1$ and every nonzero
$(\lambda_0,\lambda_1)\in\mathbb Z[i]^2$ with
$|\lambda_1|\le T$,



$$
|\lambda_0+\lambda_1e|>
 {1\over T\bigl(6+2\log T/\log\varphi\bigr)}.
$$



Here is a proof.  Euler's continued fraction is
$e=[2;1,2,1,1,4,1,1,6,\ldots]$, so its $N$-th partial quotient is at
most $2N$.  The convergent denominators satisfy
$q_n\ge F_{n+1}\ge\varphi^{n-1}$ for $n\ge1$.  If a reduced rational
$a/q$ is not a convergent, Legendre's criterion gives
$|e-a/q|\ge1/(2q^2)$.  If it is the $n$-th convergent, the standard
complete-quotient identity gives



$$
|e-a/q|>{1\over(a_{n+1}+2)q^2},
 \qquad
 a_{n+1}+2\le6+{2\log q\over\log\varphi}.
$$



Reducing $-A/B$, and multiplying by $|B|$, therefore proves the same
display for real integers $A,B$ with $0<|B|\le T$.  For Gaussian
integers, choose a nonzero real or imaginary component of $\lambda_1$
and use that the modulus of a complex number dominates the modulus of each
component.  If $\lambda_1=0$, the value has modulus at least one.  This
proves (5) also in the only case omitted by Theorem 2.1.  In the constrained
$m=1,D=1$ family the endpoint polynomial is, moreover, explicitly
constant or proportional to $z$, so it supplies no contracting endpoint.

There is a real limitation to (40) when $D$ grows.  If
$\log H\asymp n\log n$ and $r$ is fixed, (40) is guaranteed, for
example, throughout



$$
D\le(1-\epsilon){\log n\over r(\log\log n)^2}
\tag{44}
$$



for any fixed $\epsilon>0$ and all sufficiently large $n$.  It is not
uniformly guaranteed for the entire range $D=o(n)$.  The next section
records an all-height fallback.

## 5. A completely explicit all-height fallback

The primary source is

> S. Fischler and T. Rivoal, “A new transcendence measure for the values
> of the exponential function at algebraic arguments,” author manuscript
> dated 2 November 2025, [arXiv:2502.17992](https://arxiv.org/abs/2502.17992),
> Proposition 1.

The inspected author PDF had SHA-256

    0a1c89fb0856c29dca98720080968adec49a3f236ad06bbc501859b5860b1562

This manuscript is a primary preprint/accepted-manuscript source, not used
as a substitute for the published 2019 theorem in Section 4.  Its advantage
is that the following formula holds for every $H\ge1$, without (40).

Let $k=[K:\mathbb Q]=2r$, let $p\ge kD$, and put



$$
\begin{aligned}
 q&=\operatorname {lcm}(1,\ldots,p),\qquad t=1,\\
 a&=(p+1)!\exp\!\left({p(p+1)\over2}\right)(2qt)^{pD},\\
 b&=(2qt)^{(p+1)D},\\
 u&=\left(2a^kH^{(p-D+1)k}\right)^{1/(p-kD+1)},\\
 v&=e\,b^{k/(p-kD+1)},\\
 \psi(k,D,p)&={Dk^2(p-D+1)\over p-kD+1}
             +k(p-D+1)-1.
 \end{aligned}
\tag{45}
$$



Specializing Proposition 1 to $\alpha=1$ gives, for every nonzero
$P\in\mathcal O_K[X]$ of degree at most $D$ and house at most $H$,



$$
\boxed{
 |P(e)|\ge
 {1\over
 (2a^k)^{1+Dk/(p-kD+1)}
 \left(b^{k+Dk^2/(p-kD+1)}\right)^{1+v^2}
 u^{\left(k+Dk^2/(p-kD+1)\right)
       4\log b/\log\log(u+2)}
 H^{\psi(k,D,p)}}.}
\tag{46}
$$



The best leading exponent in this theorem is obtained at one of



$$
p_1=kD-1+\left\lfloor D\sqrt{k^2-k}\right\rfloor,
 \qquad p_2=p_1+1.
\tag{47}
$$



Writing the smaller value as $\mu(k,D)$, the primary paper proves



$$
\begin{aligned}
 &(2k^2+2k\sqrt{k^2-k}-k)D-1\\
 &\hspace{1cm}\le\mu(k,D)\\
 &\hspace{1cm}\le
 (2k^2+2k\sqrt{k^2-k}-k)D-1
 +{k\over D\sqrt{k^2-k}-1}.
 \end{aligned}
\tag{48}
$$



Thus (46) has a leading height exponent linear in $D$, but it is much
weaker for the present special value $e$ than the relative-norm bound
(5).  Its constants also grow very rapidly with $D$.  Its proper use
here is to make the growing-degree statement effective when the much
sharper threshold (40) is unavailable; it does not create a hidden
contradiction in the range $D=o(n)$.

## 6. Exact comparison criteria

For a sequence of nonzero, integrally normalized endpoint polynomials, set



$$
h_n=\log H(P_n),\qquad u_n=-\log|P_n(e)|,\qquad D_n=\deg P_n.
\tag{49}
$$



Whenever (40) applies, (42) gives the exact necessary inequality under the
algebraicity hypothesis:



$$
\begin{aligned}
 u_n<&\ (rD_n+\varepsilon_{rD_n}(T_n))\log(2T_n)
 +(r-1)\log\bigl((D_n+1)e^{D_n}H(P_n)\bigr)\\
 &+\log2+\mathfrak D_{rD_n},
 \qquad
 T_n=(D_n+1)^{r-1}H(P_n)^r.
 \end{aligned}
\tag{50}
$$



A certified analytic upper bound smaller than the right side of (42)
would therefore contradict algebraicity.  This is the exact comparison;
phrases such as “factorially small” or “exponentially small relative to the
coefficients” are not enough.

### 6.1 Fixed degree

If $D_n=D$ and $h_n\to\infty$, then (50) becomes



$$
u_n\le(r^2D+r-1+o(1))h_n.
\tag{51}
$$



Hence



$$
\limsup_{n\to\infty}{u_n\over h_n}>r^2D+r-1
\tag{52}
$$



would contradict the degree-$r$ algebraicity hypothesis.  If a proposed
family has only



$$
|P_n(e)|=\exp(-O(n)),\qquad h_n\asymp n\log n,
\tag{53}
$$



then $u_n/h_n\to0$, and (51) is far too weak to conflict with it.  If the
only gain is



$$
{|P_n(e)|\over H(P_n)}=\exp(-O(n)),
\tag{54}
$$



then $|P_n(e)|$ actually grows once $h_n\asymp n\log n$.

For the $m=1$ family, (8) says



$$
u_n=n\log b_D-\log H(C_n)+O_{s,D}(1).
\tag{55}
$$



Substitution in (51) gives precisely (9).  Notice the extra $+1$ in
(9): the endpoint asymptotic is a *relative* estimate
$H(C_n)b_D^{-n}$, whereas (5) is $H(C_n)^{-r^2D-r+1-o(1)}$.

### 6.2 Growing $D$ and fixed $m$

Suppose an audited two-sided endpoint estimate gives



$$
h_n\ge\kappa n\log n,\qquad
 u_n\le C_mn\log n
\tag{56}
$$



with fixed positive $\kappa,C_m$, while $D_n\to\infty$.  This regime
has an exact no-contradiction comparison, without incorrectly applying the
fixed-degree asymptotic (51) uniformly in $D_n$.

When (40) holds, let $L_n^{\rm EH}$ be the right side of (50).  Every
term that was added to its leading term is nonnegative, and
$T_n\ge H(P_n)^r$.  Hence



$$
L_n^{\rm EH}\ge rD_n\log T_n\ge r^2D_nh_n.
\tag{57}
$$



It follows from (56) that
$u_n\le(C_m/\kappa)h_n<L_n^{\rm EH}$ for all sufficiently large $n$.
When (40) is unavailable, take the optimized accessory parameter in (46)
and call the logarithm of its denominator $L_n^{\rm FR}$.  All its
factors are at least one, so (48), with $k=2r$, gives



$$
L_n^{\rm FR}\ge\mu(2r,D_n)h_n
 \ge\left(c_rD_n-1\right)h_n,
 \qquad
 c_r=8r^2+4r\sqrt{4r^2-2r}-2r>0.
$$



Thus the same strict compatibility holds for the all-height theorem.  This
is a rigorous no-contradiction result for any family for which the
two-sided scale (56) is proved, including all subranges $D_n=o(n)$.  It
does not assert that a one-sided remainder upper bound automatically gives
the second inequality in (56); unexpectedly strong cancellation must be
excluded separately.

The audited Lambert diagonal is the concrete endpoint case
$m=1,D_n=n$.  After (17), its exact estimates remain



$$
h_n=n\log n+O_s(n),\qquad u_n=n\log n+O_s(n).
$$



The all-height bound permits at least
$\mu(2r,n)h_n\asymp_r n^2\log n$ on the right side of the necessary
inequality.  It is therefore weaker than the actual endpoint scale by a
full factor of order $n$.  The superfactorially small primitive Lambert
endpoint is genuine; its growing degree is exactly what prevents a
contradiction through the available polynomial measure.

The same comparison can be written without asymptotic shorthand.  If



$$
h_n\sim\kappa_{m,D}n\log n,\qquad
 u_n\sim\rho_{m,D}n\log n,
\tag{58}
$$



then fixed-$D$ contradiction through (5) requires



$$
\rho_{m,D}>(r^2D+r-1)\kappa_{m,D}.
\tag{59}
$$



Since the maximal vanishing order in the constrained system is



$$
L=mn+m+D
\tag{60}
$$



(with the parity bonus recorded in the companion audit), a factorial
remainder naturally offers only $\rho=O(m)$ when $m,D$ are fixed.
Thus a plausible surviving wedge with growing $m$ must have, at minimum,



$$
m\ \hbox{larger than a constant multiple of }r^2D\kappa_{m,D},
\tag{61}
$$



and must retain nonvanishing and the predicted endpoint decay after
primitive endpoint normalization.  None of those arithmetic statements is
proved by a dimension count.

The degree $r$ in (59)--(61) is unknown, but this is not a logical defect
in a proof by contradiction: after assuming $s$ algebraic, one may choose
construction parameters depending on its fixed degree.  It does mean that
a single fixed $m$ and a positive height exponent cannot exclude
algebraic numbers of every possible degree merely through (59).

## 7. The exact $D=2$ tangent-number survivor

Write



$$
\tan x=\sum_{q\ge1}T_q{x^{2q-1}\over(2q-1)!}.
\tag{62}
$$



The companion constrained-HP audit proves that, for
$n\in\{2q-1,2q\}$, the rational endpoint denominator has coefficients
proportional to



$$
u_q+u_{q+1}z^2,\qquad
 u_q={T_q\over2^{2q}(2q-1)!}.
\tag{63}
$$



Since



$$
{u_q\over u_{q+1}}
 ={8q(2q+1)T_q\over T_{q+1}},
\tag{64}
$$



reduction to lowest terms gives (10).  Moreover,



$$
u_q={2\over\pi^{2q}}
 \sum_{\substack{k\ge1\\k\ \mathrm{odd}}}{1\over k^{2q}},
\tag{65}
$$



so



$$
{u_q\over u_{q+1}}-\pi^2
 =\left({8\pi^2\over9}+o(1)\right)9^{-q}.
\tag{66}
$$



Equations (64)--(66) give (11) directly.  Because
$P_q/Q_q\to\pi^2$, one has



$$
H(C_q)\asymp Q_q.
\tag{67}
$$



Applying (51) with $D=2$ to (11) and (67) proves (12).

The tangent numbers satisfy



$$
\log T_{q+1}=2q\log q+O(q).
\tag{68}
$$



This last estimate needs no unrecorded arithmetic theorem: (63) and (65)
give


$$
T_{q+1}=2^{2q+2}(2q+1)!\,
2\pi^{-2q-2}(1+O(3^{-2q}))
$$

, and Stirling's formula gives (68).

Therefore a subexponential $Q_q$ would require the gcd in (10) to absorb
all but $o(q)$ of this factorial logarithm.  This is much stronger than
ordinary coprimality or a subfactorial gcd bound.  Exact computation through
$q=300$ also shows that the odd part of
$\gcd(T_q,T_{q+1})$ is nontrivial at $q=45$ and $q=168$, with odd
parts $587$ and $491$, respectively.  Thus even the tempting assertion
that consecutive tangent numbers have only a power-of-two gcd is false.
The companion certificate and the independent certificate listed below
verify these finite statements; they are diagnostics, not an asymptotic
gcd theorem.

## 8. Reproducibility

The companion script

`scripts/root_of_unity_polynomial_e_measure_certificate.py`

uses exact integer and rational arithmetic.  It verifies:

1. the optimizer (47) for a finite rectangular family and the exact values
   of $\psi$;
2. the relative-norm asymptotic exponent $r^2D+r-1$ against the direct
   all-height exponent $\mu(2r,D)$;
3. the tangent recurrence and the exact ratio (64) through index $300$;
4. the two exceptional odd consecutive tangent gcds through index $300$;
5. the exact quotient in (10) and selected logarithmic diagnostics.

Its deterministic output is

`results/root_of_unity_polynomial_e_measure_certificate.json`.

These finite checks certify the formulas and implementation.  The
all-parameter lower bound is the deduction from the primary theorem in
Sections 3--4, and the tangent asymptotic and HP normalization are proved
in the companion source, not inferred from the scan.

## 9. Final assessment

The algebraic-coefficient value left by the low-degree root-of-unity
endpoint is not outside quantitative transcendence theory.  After the
correct primitive normalization it satisfies the explicit bound (42), and
for fixed coefficient-field degree and polynomial degree it satisfies the
sharp usable asymptotic (5).

That result closes several false shortcuts:

* full-vector height cannot replace primitive endpoint height;
* an $\exp(-cn)$ gain cannot beat a lower bound on the
  $\exp(-c'n\log n)$ scale;
* $D=o(n)$ is not by itself a favorable regime, because the lower-bound
  exponent grows linearly in $D$; and
* the $D=2$ construction is not complete until the exact tangent-number
  quotient $Q_q$ is controlled.

The sharp survivor is also explicit.  Subexponential primitive endpoint
height in the fixed-degree family, and in particular
$\log Q_q=o(q)$ in (10), would contradict every hypothetical algebraic
degree via (9) or (12).  No theorem in the archive proves that arithmetic
condition.  Consequently this lower-bound audit does not prove or disprove
the transcendence of $e+\pi$.
