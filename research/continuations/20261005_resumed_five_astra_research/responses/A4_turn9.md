> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4, Turn 9 — Independent audit of the fixed-degree endpoint defect, ternary radical, and binary model pairing

## Executive verdict

The three new specialized results have different scopes.

1. **A3’s fixed-degree endpoint contrast passes.** The coefficient
   

$$
d(2d-3-3\sqrt2)
$$


   follows from the exact finite endpoint insertion, with the exponential phase, circular Vandermonde correction, scalar averaging, and normalized division all retained. The fixed-dimensional remainder argument can be made rigorous without invoking any growing-degree theorem. I give that justification below.

   With the accepted complete residual bounds and prime-survival theorem, this establishes the claimed **whole actual primitive-form divergence**
   

$$
|\widehat q(e+\pi)-\widehat p|\longrightarrow\infty
$$


   for $d=2,\ 105\mid n$, and for $d=3,4,\ 385\mid n$. These are exclusion results for those particular families, not irrationality results.

2. **A1’s residue decomposition and unavoidable core singularity pass.** The original endpoint $\nu=D/2-1$ genuinely produces an $s\times(s-1)$ block. The stated class sizes, rank formula, degeneration thresholds, triangular radicals, and endpoint-image obstruction are correct.

   This is a theorem about the **core** $\mathcal C_7$. Its identification with the actual depth-seven digit still requires the unproved actual producer-strip vanishing. A1 Turn 4 does not silently restore that missing hypothesis in its later conclusions.

3. **A5’s content-relative pairing theorem passes as an exact model theorem.**
   

$$
S(C,D)\in2^{2\mu+2}\mathbb Z,\qquad
   \frac{S(C,D)}{2^{2\mu+2}}\equiv \xi M\pmod2.
$$


   The terminal pair is handled correctly. The hypergeometric formula also retains the necessary terminal correction.

   The relation to the actual norm remains only
   

$$
N=2S(C,D)+256R_u,\qquad R_u\in\mathbb Z_2.
$$


   No huge actual valuation follows.

A further exact consequence on A5’s original family is


$$
\boxed{\xi_u\equiv u\pmod2.}
$$


Thus every even $u$ has one additional forced model bit:


$$
\boxed{S(C_u,D_u)\in2^{2\mu_u+3}\mathbb Z\qquad(u\ \text{even}).}
$$


This still makes no assertion about the corresponding actual norm beyond its established precision.

No tools were executed. The supplied certificates are treated as finite mathematical evidence, not as substitutes for the proofs audited here.

---

# I. A3: the exact fixed-degree endpoint contrast

## 1. Exact scope and insertion

Throughout this section,


$$
\sigma=\sqrt2,\qquad M=1+\sqrt2,\qquad \rho=M^{-1},
\qquad d=b-1\ge2
$$


is a **fixed integer**, and $n\to\infty$ through both parities.

The finite boundaries remain


$$
\mathsf T,C,\mathcal S:\{0,\ldots,d\}^2,
\qquad
Z:\{0,\ldots,d+1\}\times\{0,\ldots,d\}.
$$


Nothing in the following calculation extends those matrices.

On polynomials of degree at most $d$,


$$
(1+D_t)^{-n}
=\sum_{k=0}^{d}(-1)^k\frac{n^{\overline k}}{k!}D_t^k.
$$


Consequently the supplied insertion


$$
R_j(z)=[t^j](t-1)(1+D_t)^{-n}
                 \prod_{\ell=1}^d(z_\ell+t/\sigma)
$$


gives exactly


$$
R_b=\sigma^{-d},
$$


and


$$
R_0=(-1)^{d+1}n^{\overline d}\sigma^{-d}W_{n,d},
$$


where


$$
W_{n,d}
=\sum_{r=0}^{d}(-1)^r\sigma^r
  \frac{n^{\overline{d-r}}}{n^{\overline d}}e_r(z).
$$


There is no infinite insertion remainder.

For $d=2$,


$$
W_{n,2}
=1-\frac{\sigma}{n+1}(z_1+z_2)
+\frac{2}{n(n+1)}z_1z_2.
$$



The full scalar integrals and particle functional imply


$$
\boxed{
\frac{F_0/P_0}{F_b/P_b}
=\frac{\mathbb E_-W_{n,d}}{\mathbb E_+W_{n,d}}.
}
$$


The normalization multiplying $R_0$ cancels here. This identity is the correct finite starting point for the contrast; a common leading error law alone would not suffice.

---

## 2. Audit of the particle calculation

### 2.1 Full measure and local amplitude

The particle weight is


$$
|\Delta(e^{i\theta})|^2
\prod_{\ell=1}^{d}
(1+\sigma\cos\theta_\ell)^n e^{-\sigma e^{i\theta_\ell}},
\qquad \theta_\ell\in[-\pi,\pi].
$$


The factor $e^{-\sigma e^{i\theta}}$ is complex and must not be replaced by its modulus.

For a characteristic parameter $q$ near $M$ or $\rho$, set


$$
p=(1+q)^{-1},\quad c=\sigma+p,\quad
u=\frac{\sigma-p+p^2}{2},\quad
v=\frac{\sigma+p-3p^2+2p^3}{6}.
$$


Then


$$
-\sigma e^{i\theta}+\log(e^{-i\theta}+q)
=\text{constant}-ic\theta+u\theta^2+iv\theta^3+O(\theta^4).
$$


The displayed coefficients are correct.

Also,


$$
\log(1+\sigma\cos\theta)
=\log M-\frac{\alpha\theta^2}{2}+a_4\theta^4+O(\theta^6),
$$


where


$$
\alpha=2-\sigma,\qquad a_4=\frac{\alpha}{24}-\frac{\alpha^2}{8}.
$$



For the circular Vandermonde,


$$
\prod_{i<j}
\left(\frac{2\sin((\theta_i-\theta_j)/2)}
{\theta_i-\theta_j}\right)^2
=
1-\frac{dQ_2-X^2}{12}+O_d(\|\theta\|^4),
$$


with $X=\sum\theta_i$ and $Q_r=\sum\theta_i^r$. Thus A3’s circular correction is also correct.

### 2.2 Gaussian moments

For the Gaussian eigenvalue measure


$$
\Delta(\theta)^2e^{-\alpha nQ_2/2}\,d\theta,
\qquad t=(\alpha n)^{-1},
$$


the quoted moment identities pass.

They can be checked independently using the Hermitian Gaussian matrix $H$ with covariance


$$
\mathbb E H_{ij}H_{kl}=t\,\delta_{il}\delta_{jk}.
$$


For example,


$$
\mathbb E\operatorname{Tr}H^4=(2d^3+d)t^2
$$


comes from the three Wick pairings. Integration by parts in the identity-matrix direction gives


$$
\mathbb E(XQ_3)=3d^2t^2,\qquad
\operatorname{Cov}(X^2,Q_4)=12d^2t^3.
$$


Radial scaling gives


$$
\operatorname{Cov}(Q_2,Q_4)
=4(2d^3+d)t^3.
$$


These identities use the stated finite dimension $d$; no universality or positive approximation of the original complex functional is involved.

### 2.3 The normalized $m_2$ calculation

It is important to expand the observable after subtracting its constant:


$$
e_1-d=iX-\frac{Q_2}{2}-\frac{iQ_3}{6}+\frac{Q_4}{24}+\cdots.
$$


The second-order amplitude contains


$$
UQ_2+\left(\frac1{12}-\frac{c^2}{2}\right)X^2+na_4Q_4,
\qquad U=u-\frac d{12}.
$$



The fourth-order contribution to the normalized expectation is precisely


$$
\begin{aligned}
\frac{m_2(p)}{n^2}
={}&-\left(v+\frac c6\right)\mathbb E(XQ_3)\\
&+\left(cU-\frac1{24}+\frac{c^2}{4}\right)
  \operatorname{Cov}(X^2,Q_2)
+\frac c{12}\operatorname{Var}(X^2)
-\frac U2\operatorname{Var}(Q_2)\\
&+na_4\left[
c\,\operatorname{Cov}(X^2,Q_4)
-\frac12\operatorname{Cov}(Q_2,Q_4)\right]
+\frac1{24}\mathbb E Q_4.
\end{aligned}
$$


In particular, the cubic phase contribution is


$$
-\frac{c^3}{6}\mathbb E X^4
+\frac{c^3}{2}(\mathbb E X^2)^2=0.
$$


This cancellation is a consequence of Gaussian trace normality, not a discarded term.

Substitution yields


$$
\begin{aligned}
m_2(p)
={}&\frac1{\alpha^2}\left[
-3d^2v+(2dc-d^2)u+\frac{dc^2}{2}
-\frac{cd^2}{2}+\frac{4d^3-d}{24}\right]\\
&+\frac{a_4}{\alpha^3}(12cd^2-4d^3-2d),
\end{aligned}
$$


as claimed.

The lower-order moments are likewise


$$
m_1(p)=\frac d\alpha\left(\sigma+p-\frac d2\right),
$$




$$
h_1(p)=\frac{d(d-1)}\alpha
\left(\sigma+p-\frac{d-1}{2}\right).
$$



**Finding:** the phase, normalization, circular interaction, and quartic saddle terms needed for the contrast are all present.

---

## 3. The outstanding analytic point: a rigorous fixed-$d$ remainder

A3’s remainder conclusion is valid, but the phrase “expand through scaled degree five” should be interpreted in the following precise way.

### Fixed-dimensional normalized Laplace lemma

Choose disjoint sufficiently small complex neighborhoods of the two anchors $q=M,\rho$, with $1+q\ne0$. For fixed $d$, the full normalized particle integrals satisfy, uniformly in those neighborhoods,


$$
\mathbb E_qe_1
=d+\frac{m_1(p)}n+\frac{m_2(p)}{n^2}+O_d(n^{-3}),
$$




$$
\mathbb E_qe_2
=\binom d2+\frac{h_1(p)}n+O_d(n^{-2}),
$$


and, for each fixed $r\le d$,


$$
\mathbb E_qe_r=\binom dr+O_d(n^{-1}).
$$



### Proof of the required remainder statement

**Outer sectors.** The absolute maximum of $1+\sigma\cos\theta$ on the full circle is uniquely $M$, attained at zero. Outside a fixed neighborhood of zero,


$$
|1+\sigma\cos\theta|\le M(1-\delta).
$$


All other particle factors are uniformly bounded on the compact torus and the chosen $q$-neighborhoods. Thus any sector with at least one remote particle contributes at most


$$
C_dM^{nd}(1-\delta)^n
$$


before normalization. The local denominator has order


$$
M^{nd}n^{-d^2/2}.
$$


Hence remote contributions are exponentially small relative to it, even after multiplication by any fixed power of $n$. This includes the negative-$g_+$ sectors for odd $n$.

**Local rescaling.** Set $h=n^{-1/2}$, $\theta=hy$. The Vandermonde scaling and volume element supply $h^{d^2}$. After extracting the constant amplitude, the integrand has the form


$$
\Delta(y)^2e^{-\alpha Q_2(y)/2}
\times \text{analytic amplitude in }h,y.
$$


The saddle exponent contributes, for example,


$$
h^2a_4Q_4(y)+h^4a_6Q_6(y)+\cdots.
$$


Thus “degree” here means the power of $h$ **after including the factor $n$ in the exponent**.

On $\|y\|\le h^{-1/10}$, Taylor expansion through $h^5$, with an integral remainder, is bounded by


$$
C_dh^6(1+\|y\|^{K_d})e^{-c\|y\|^2}
$$


after multiplication by the Gaussian and Vandermonde. One obtains this bound by retaining the Gaussian quadratic term and absorbing the small quartic and higher perturbations into a weaker Gaussian. The part outside this scaled cutoff is exponentially small.

**Parity.** The coefficient of $h^k$ has parity $(-1)^k$ under $y\mapsto-y$. Odd powers integrate to zero on the symmetric cutoff. This leaves an integrated remainder $O_d(h^6)=O_d(n^{-3})$.

For $e_1-d$, a pure fourth-order amplitude correction cannot affect the $h^4$ coefficient, because the observable starts at order $h$. Its first possible contribution is order $h^5$, which is odd. This explains why the sextic saddle and fourth-order amplitude terms need not appear in the displayed formula for $m_2$, although they belong in a systematic remainder proof.

**Division.** The denominator has leading term


$$
K_d e^{-\sigma d}(1+q)^dM^{nd}n^{-d^2/2},
\qquad K_d>0.
$$


It is uniformly nonzero on sufficiently small anchor neighborhoods for all sufficiently large $n$. Dividing the two controlled expansions proves the normalized statements.

This establishes the required fixed-$d$ remainder independently of the coordinator’s symbolic calculation.

---

## 4. Scalar correction and joint normalization

The scalar variable changes the parameter to


$$
q(s)=\sigma+\epsilon e^{is}.
$$


At $s=0$,


$$
p_\epsilon=(1+\sigma+\epsilon)^{-1},\qquad
\beta_\epsilon=\frac{\sigma}{\sigma+\epsilon}.
$$


The leading particle amplitude is $(1+q(s))^d$, whose logarithmic linear term is $id\epsilon p_\epsilon s$.

Therefore


$$
\langle s\rangle
=\frac{id\epsilon p_\epsilon}{\beta_\epsilon n}+O_d(n^{-2}),
\qquad
\langle s^2\rangle
=\frac1{\beta_\epsilon n}+O_d(n^{-2}).
$$


It follows that


$$
\langle q-q_\epsilon\rangle
=-\frac{dp_\epsilon+\epsilon/2}{\beta_\epsilon n}
+O_d(n^{-2}),
$$




$$
\langle(q-q_\epsilon)^2\rangle
=-\frac1{\beta_\epsilon n}+O_d(n^{-2}).
$$


Taylor expansion of $m_1(q)$ gives


$$
s_2(\epsilon)
=\frac d{\alpha\beta_\epsilon}
\left((d-1)p_\epsilon^3+\frac{\epsilon p_\epsilon^2}{2}\right).
$$



Corrections of order $1/n$ to the particle denominator do not change this coefficient: their effect on these leading scalar moments is one order later.

The scalar remainder is controlled on the **original** intervals:


$$
[-\pi,\pi]\quad\text{and}\quad[-\pi/4,\pi/4].
$$


On the minus interval, $g_-(s)=\sigma\cos s-1$ is nonnegative, has a unique maximum at zero, and vanishes at the two original endpoints. Remote scalar contributions must be bounded as unnormalized integrals; the source correctly avoids dividing by conditional particle denominators there.

The same rescaling-and-parity argument, now in dimension $d+1$, supplies the needed joint remainder.

---

## 5. Contrast coefficient and normalized division

The joint differences are


$$
\Delta m_1=\frac d\sigma,
$$




$$
\Delta m_2^{\rm joint}
=2d+\frac{\sigma d(2-d)}2,
$$




$$
\Delta h_1=\frac{d(d-1)}\sigma.
$$


The coordinator certificate checks the finite algebra leading to these expressions. The preceding analysis supplies the missing asymptotic justification.

The finite insertion then gives


$$
\mathbb E_-W-\mathbb E_+W
=-\frac d{n^2}
+\frac{d[2d-3+\sigma(d-3)]}{n^3}
+O_d(n^{-4}).
$$


Terms with $r\ge3$ contribute only $O_d(n^{-4})$ to this difference, since their coefficients are $O_d(n^{-r})$ and their expectation differences are $O_d(n^{-1})$.

The denominator is


$$
\mathbb E_+W=1-\frac{\sigma d}{n}+O_d(n^{-2}).
$$


Its reciprocal therefore changes the cubic coefficient by $-\sigma d^2$, yielding


$$
\boxed{
\frac{F_0/P_0}{F_b/P_b}
=1-\frac d{n^2}
+\frac{d(2d-3-3\sigma)}{n^3}
+O_d(n^{-4}).
}
$$



For $d=2$, the decisive sequence is


$$
2-2\sigma
\quad\longmapsto\quad
2-6\sigma
$$


under normalized division. Omitting that division correction would give the wrong answer.

---

## 6. Complete force, amplification, and the whole error

The exact coordinate error is


$$
c_j-(e+\pi)
=\frac{E_j}{P_j}
+(-1)^{n+1}\frac{F_j}{P_j}
+(-1)^n\delta_{j0}\frac D{P_j}.
$$


The complete exponential force remains


$$
eE_i
=-[z^{n+i}]Q(z)^n
\int_0^1s^ne^{1-s+sz}\,ds,
\qquad Q(z)=1-z+\frac{z^2}{2},
$$




$$
E_j=\nu_{n,d}\!\left(
R_j\sum_{i=0}^d\sigma^ie_{d-i}(z^{-1})eE_i
\right).
$$



For $\lambda=n^2/d$, the whole amplified residual is


$$
\mathcal R_{n,d}
=\lambda E_0/P_0+(1-\lambda)E_b/P_b
+(-1)^n\lambda D/P_0.
$$


Using the accepted complete bounds,


$$
\mathcal R_{n,d}=O_d(n^{3/2}/n!).
$$


Relative to the final principal error scale $M^{-2n}/n$, this is


$$
O_d\!\left(\frac{n^{5/2}M^{2n}}{n!}\right)
=o(n^{-K})
$$


for every fixed $K$. Thus the complete residual remains negligible **after** the $n^2$ amplification.

Likewise, the coordinate residuals divided by $F_b/P_b$ are smaller than every fixed inverse power of $n$. They can legitimately be absorbed into the endpoint-ratio remainder.

The endpoint size is


$$
\frac{F_b}{P_b}
=4\pi M^{-2n-d-1}(1+O_d(n^{-1})).
$$


The four factors are exactly the scalar exponential ratio, characteristic amplitude ratio, Gaussian curvature ratio, and original scalar normalization ratio identified in A3.

Writing


$$
C_d=2d-3-3\sqrt2,
$$


one obtains


$$
\boxed{
\widehat c-(e+\pi)
=(-1)^{n+1}4\pi C_d
\frac{M^{-2n-d-1}}n(1+O_d(n^{-1})).
}
$$


Since $C_d\ne0$ for every integer $d$, this is an eventual nonvanishing theorem on both parities.

---

## 7. Actual primitive denominator and divergence

The arithmetic reuse is legitimate only for the actual reduced pair.

With the least two-column clearer $d_B$, reduce the endpoint rows of


$$
U=d_Bu,\qquad V=d_Bv
$$


by their contents $r_0,r_b$. Write


$$
\widetilde u_0=hA,\qquad \widetilde u_b=hB,\qquad \gcd(A,B)=1,
$$


and set


$$
a=\frac{n^2}{\gcd(n^2,d)},\qquad
k=\frac d{\gcd(n^2,d)},
$$




$$
J=B\widetilde v_0-A\widetilde v_b,\qquad
T=aJ+kA\widetilde v_b.
$$


The full cancellation factors are


$$
F=\gcd(|A|,a)\gcd(|B|,a-k),\quad
G=\gcd(k,|J|),\quad
H_{\rm gcd}=\gcd\!\left(h,\frac{|T|}{FG}\right).
$$


Thus


$$
\widehat q=\frac{kh|AB|}{FGH_{\rm gcd}},\qquad
\widehat p=\operatorname{sgn}(AB)\frac{T}{FGH_{\rm gcd}}.
$$



The accepted prime-survival theorem applies at


$$
p>d,\qquad p\mid n,\qquad \tau_nD_d\not\equiv0\pmod p.
$$


It explicitly survives the final shared-content gcd. For $d=2,\ 105\mid n$, it gives


$$
v_p(\widehat q)=2v_p(n!),\qquad p=3,5,7.
$$


Combining its accepted lower bound with the newly proved whole-error lower bound yields


$$
\boxed{
|\widehat q(e+\pi)-\widehat p|
>
\frac{2\pi(3\sqrt2-1)}{11025M^3}
\frac{2^n}{n^7}
}
$$


eventually on $105\mid n$.

The signs are


$$
\widehat q(e+\pi)-\widehat p\to-\infty
\quad\text{through even multiples of }105,
$$




$$
\widehat q(e+\pi)-\widehat p\to+\infty
\quad\text{through odd multiples of }105.
$$



The same argument, at the accepted $5,7,11$ denominator scope, proves divergence for $d=3,4,\ 385\mid n$.

**This closes the old distinction between a diverging denominator budget and a lower bound for the actual form on these families.** The new analytic lower bound is what makes that promotion valid.

---

# II. A1: the true rectangular endpoint block

## 8. Residue classes and singularity

Retain the original domain


$$
n=4^j+1,\quad j>0,\quad81\mid j,\quad
0<D<H/972,\quad H=3^{h-1},
$$


and the actual residual indices


$$
0\le i<\nu,\qquad \nu=D/2-1.
$$



Set


$$
g=3^{v_3(j)+1},\qquad D=2gs,\qquad
L=H/(729g),\qquad
a_0=(g-1)/2,\qquad \eta=(L-1)/2.
$$


Writing $i=ga+r$, the exact class sizes are


$$
n_r=s\quad(0\le r\le g-2),\qquad n_{g-1}=s-1.
$$


This follows directly from $\nu=gs-1$; it is not a choice of convenient padding.

Modulo $3$,


$$
(y-1)^D=(y^g-1)^{2s}.
$$


Hence a block is zero unless


$$
r+r'\equiv a_0\pmod g.
$$


The exceptional paired classes $a_0+1$ and $g-1$ have coupling


$$
J=H_1[:,0,\ldots,s-2],
$$


of size $s\times(s-1)$.

Therefore


$$
\dim\ker J^T\ge1,
$$


and


$$
\boxed{\mathcal C_7\text{ is singular throughout the original domain}.}
$$



The rank formula


$$
\operatorname{rank}\mathcal C_7
=N_0\rho_0+(N_1-2)\rho_1+2\rho_J
$$


is correct. Paired square blocks contribute twice their rank; a fixed class contributes its square-block rank; the exceptional rectangular pair contributes $2\rho_J$.

The listed kernels and images follow block by block.

---

## 9. Degeneration and triangular region

Put $\delta=2s$. The coefficient indices in $H_1$ range from


$$
\eta-1-(\delta-2)\quad\text{to}\quad\eta-1.
$$



If $L>4\delta$, then $\eta\ge2\delta$, and the entire range lies above degree $\delta$. Both $H_0$ and $H_1$ vanish.

If $L<4\delta$, the range contains an index selecting coefficient $0$, $1$, or $\delta$, according to the three cases stated in A1. The relevant coefficients are


$$
1,\quad-\delta,\quad1,
$$


and $-\delta\ne0\pmod3$. Regular full $H_1$ blocks are present in the original domain. Therefore


$$
\boxed{
\mathcal C_7=0\iff D<H/2916.
}
$$



On $L>3\delta$, equivalently $D<H/2187$, the first possible nonzero anti-diagonal selects the leading coefficient $1$. The trailing block sizes are exactly


$$
u=\max(0,4s-1-\eta),\qquad
v=\max(0,4s-\eta),
$$


so


$$
\rho_0=u,\qquad \rho_1=v,\qquad \rho_J=u.
$$


The rectangular truncation removes one column from the $H_1$ pattern and leaves the stated trailing $u\times u$ unit minor.

The coordinate-kernel descriptions and rank formula consequently pass.

---

## 10. Endpoint projection and actual-force qualification

Because $g$ is odd,


$$
(-1)^{ga+r}=(-1)^{a+r}.
$$


Thus the endpoint restricted to class $r$ is


$$
(-1)^r(1,-1,\ldots)^T,
$$


and its pairing with a kernel polynomial $f$ is exactly


$$
(-1)^rf(-1).
$$



For a symmetric matrix over $\mathbb F_3$,


$$
\operatorname{im}\mathcal C_7=(\ker\mathcal C_7)^\perp.
$$


This proves the stated endpoint-image criterion. In the triangular region, the forced kernel contains an initial coordinate vector with nonzero endpoint pairing, so


$$
\boxed{\overline e\notin\operatorname{im}\mathcal C_7
\qquad(D<H/2187).}
$$



These conclusions do **not** automatically hold for


$$
\overline T=\mathcal C_7+\mathcal F_R.
$$


The actual force formula permits cross-couplings between different core residue pairs. The rectangular core radical can therefore be destroyed by the actual force.

A1 correctly preserves this distinction:

- the stronger producer congruence is explicitly unproved;
- the weaker required coefficient strip is explicitly unproved;
- the actual radical compression is formulated using $\ker\overline T$, not automatically $\ker\mathcal C_7$;
- the simplification $R=3S$ is explicitly conditional;
- no actual inverse depth or primitive denominator is inferred from core singularity.

The Schur compression


$$
T_{\rm next}
=\frac{C_0-B_0^TA_0^{-1}B_0}{3}
$$


is valid when $A_0$ is the unit block on a complement of the actual radical. Its endpoint must be transported as stated; a nonzero endpoint residue alone does not prove a nonzero inverse contraction.

The unresolved producer obligation remains


$$
v_3(-3(w_n)_a-\Delta_nc_a)
\ge v_3(\Delta_n)+7,
$$


or the smaller actual strip vanishing. The determinant valuation on the right cannot be omitted.

The standard binomial determinant formula is usable only through the valuation of its **whole integer product**. Nothing in this audit invokes characteristic-zero Hankel nonsingularity as an $\mathbb F_3$ theorem. This respects the warning attached to arXiv:2101.04225.

The coordinator’s three auxiliary assemblies corroborate those three inputs only. They do not prove the producer-strip lemma.

---

# III. A5: exact model pairing, terminal correction, and a new parity simplification

## 11. Pairing theorem

Let


$$
\mathcal B_t=\binom Ct\binom{2C+D-t}{D-t},\qquad
e_t=v_2(\mathcal B_t),
$$


with $D$ odd and $C=4002D+2532$.

The adjacent recurrence is exact:


$$
t(2C+D-t+1)\mathcal B_t
=(C-t+1)(D-t+1)\mathcal B_{t-1}.
$$


For odd $t$, all factors except $C-t+1$ are odd. Thus


$$
e_t-e_{t-1}=v_2(C-t+1)\ge1.
$$


All minima occur at even indices, including when the final pair is considered.

For $t=2k+1$,


$$
v_2(C-2k)=1\quad(k\text{ even}),\qquad
v_2(C-2k)\ge2\quad(k\text{ odd}),
$$


because $C\equiv2\pmod4$.

The polynomial reductions are correct:


$$
P_D(t)\equiv t(t+2)\pmod4,
$$


and


$$
P_D(2k)\equiv4(1+k+\xi)\pmod8.
$$


Also $Q_D$ is odd.

Hence every summand in the exact model contraction is divisible by $2^{2\mu+2}$. A minimizing pair contributes, after division and reduction modulo $2$,


$$
1+k+\xi+\mathbf1_{k\ {\rm even}}\equiv\xi.
$$


Every nonminimizing pair contributes zero.

Therefore


$$
\boxed{
S(C,D)\in2^{2\mu+2}\mathbb Z,\qquad
S(C,D)/2^{2\mu+2}\equiv\xi M\pmod2.
}
$$



For the last pair, the odd coefficient is $Q_D$, not $P_D(D)$. Only its oddness is used at this bit, which is sufficient. Thus the shortened terminal block is genuinely retained.

---

## 12. Hypergeometric terminal correction

The quotient


$$
\frac{\mathcal B_{j+s}}{\mathcal B_j}
=
\frac{(j-C)_s(j-D)_s}
{(j+1)_s(j-2C-D)_s}
$$


and


$$
\binom{j+s}{j}=\frac{(j+1)_s}{s!}
$$


give the stated terminating ${}_4F_3$ representation.

The summation ends at $s=D-j$; no denominator Pochhammer symbol vanishes before then.

Since


$$
\mathcal B_D=\binom CD,
$$


the exact correction


$$
\binom CD^2\bigl(Q_D-P_D(D)\bigr)
$$


is necessary and correct. Without it, the formula would describe a different model with an artificially full terminal block.

This is an exact finite summation identity, not a closed-product evaluation and not an identity for the complete actual columns.

---

## 13. New original-index parity consequence

On the original family,


$$
D_u=\frac{9^{18+32u}-81}{128},\qquad
\xi_u=\frac{D_u-1}{2}.
$$


Modulo $512$,


$$
9^k=(1+8)^k\equiv1+8k+64\binom k2.
$$


For $k=18+32u$,


$$
\binom k2\equiv\binom{18}{2}\equiv1\pmod8,
$$


so


$$
9^{18+32u}\equiv209+256u\pmod{512}.
$$


Therefore


$$
D_u\equiv1+2u\pmod4,
\qquad
\boxed{\xi_u\equiv u\pmod2.}
$$



The model next-bit law becomes


$$
\boxed{
S(C_u,D_u)/2^{2\mu_u+2}\equiv uM_u\pmod2.
}
$$


Consequently:

- for every even $u$,
  

$$
v_2(S(C_u,D_u))\ge2\mu_u+3;
$$


- for odd $u$ with $M_u$ odd,
  

$$
v_2(S(C_u,D_u))=2\mu_u+2.
$$



This is an infinite original-index statement about the model, proved without assuming growth of $\mu_u$.

---

## 14. No promotion to huge actual valuations

The established actual interface remains


$$
N=2S(C_u,D_u)+256R_u,\qquad R_u\in\mathbb Z_2.
$$


The model theorem says


$$
v_2(2S)\ge2\mu_u+3.
$$


It does not bound the actual residual $R_u$.

At the sixteen certified indices, $\mu_u\ge7$, so the valid actual conclusions are only


$$
N\in256\mathbb Z_2,\qquad H\in128\mathbb Z_2,
$$


using the accepted $H-N\in128\mathbb Z_2$.

In particular, neither


$$
v_2(N)=2\mu_u+3
$$


nor any corresponding value of $v_2(H)-v_2(N)$ has been proved.

A concrete sufficient follow-on lemma is


$$
\boxed{
N-2S(C_u,D_u)\in2^{2\mu_u+4}\mathbb Z_2.
}
$$


It must be proved for the complete actual reconstruction, retaining the logarithmic force, relevant factorial tails, shortened terminal block, and exterior $+1$. A separate mixed-contraction theorem would still be needed.

---

# IV. Primitive normalization, proof status, and next calculation

## 15. What remains unchanged globally

For A1, the final pair remains


$$
g_\ell=\gcd(|A_\ell|,|B_\ell|),\qquad
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
$$


when $B_\ell\ne0$, with whole error


$$
q(e+\pi)-p
=\frac{\operatorname{sgn}(B_\ell)\ell^k}{g_\ell}
\det H_{\rm complete}.
$$


Core radical information alone establishes neither $B_\ell\ne0$ nor the size of this complete expression.

For A5, retain


$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B,
$$


including every odd prime in the gcd. The whole error is


$$
q_n(e+\pi)-p_n=-q_n\epsilon_n.
$$


The accepted signed error law retains its stated hypotheses; the model pairing does not estimate the full primitive denominator.

The A3 result is different: there the accepted arithmetic lower bound and the newly proved whole-error lower bound now combine on the same original indices. This is why actual divergence is justified there but no analogous promotion is justified for A1 or A5.

---

## 16. Bounded exact arithmetic worth requesting

No further finite computation is needed to establish A3’s fixed-$d$ asymptotic remainder or A1’s residue decomposition. The supplied symbolic and interval certificates already have the correct finite scope.

The useful new bounded calculation is **A5 minimum-multiplicity parity**.

### Inputs

Use exactly


$$
u=0,\ldots,15,\qquad
D_u=\frac{9^{18+32u}-81}{128},\qquad
C_u=4002D_u+2532.
$$


Augment the accepted carry minimization with the parity of the number of minimum-cost paths, retaining its original start, all digit layers, and final zero-carry condition.

### Expected verifiable output

For each $u$, return


$$
(u,\mu_u,M_u\bmod2,u\bmod2,uM_u\bmod2).
$$


The previously certified $\mu_u$ must be reproduced. Independently check


$$
D_u\bmod4=1+2u\bmod4.
$$



The output must imply only


$$
\begin{cases}
v_2(S)=2\mu_u+2,&uM_u\text{ odd},\\
v_2(S)\ge2\mu_u+3,&uM_u\text{ even}.
\end{cases}
$$


It must not be labeled an actual norm-valuation certificate.

---

## 17. Final proof ledger and exact bottlenecks

| Result | Audit status |
|---|---|
| A3 exact endpoint insertion | Pass |
| A3 phase, circular Vandermonde, Gaussian $m_2$ formula | Pass |
| A3 scalar correction and normalized cubic coefficient | Pass |
| A3 fixed-$d$ remainder, both parities | Pass, with explicit rescaled remainder argument above |
| Complete residual after $n^2$ amplification | Negligible at the required scale |
| A3 actual primitive-form divergence on the stated progressions | Proved using accepted prime-survival hypotheses |
| A1 true class sizes and rectangular endpoint block | Pass |
| A1 core singularity, degeneration criterion, triangular ranks | Pass |
| A1 actual force-strip vanishing | Still unproved |
| A1 actual inverse or primitive-denominator depth | Not established |
| A5 content-relative pairing and terminal correction | Proved for the exact model |
| A5 $\xi_u\equiv u\pmod2$ | New exact consequence proved here |
| A5 huge actual norm or mixed valuation | Not established |

The remaining specialized obligations are precise:

1. **A1:** prove the actual producer-strip lemma, then evaluate the actual operator on the surviving radical and its transported endpoint.
2. **A5:** prove a complete content-relative residual estimate and then a corresponding actual mixed-contraction theorem.
3. **Global irrationality objective:** find a same-index infinite family with its actual primitive denominator and complete nonzero error satisfying
   

$$
0<|q(e+\pi)-p|\longrightarrow0.
$$



A3’s reviewed progressions do not provide such a family: their actual primitive forms diverge. This excludes those particular routes, not rationality or irrationality of the number itself.



$$
\boxed{\text{An unconditional proof or disproof of irrationality of }e+\pi
\text{ remains unresolved.}}
$$


