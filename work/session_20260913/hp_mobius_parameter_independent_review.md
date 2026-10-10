> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the Möbius-parameter HP continuation

Date: 2026-09-13. Reviewed `hp_mobius_parameter_dependence.md`, including
its subsequent Section7 extension. Coordinated directly with its author.
Here beta denotes the Möbius parameter; the degree of B remains one.

## Verdict

The affine identities, pure-pi endpoint invariance, exact HP endpoint
pair, whole-remainder identity, and symbolic non-redundancy all pass.
The original fixed-beta>1/3 sign argument also passes. The stronger
Section7 argument proves, for **every one fixed beta>0**,



$$
\frac{(-1)^nR_n(1)}{Y_n\epsilon_n}\longrightarrow
 k(\beta)=
 \frac{\beta+\sqrt{1+\beta^2}+1-\sqrt2}
 {\beta+\sqrt{1+\beta^2}+1+\sqrt2}>0.
\tag{1}
$$



No uniform moving-parameter theorem is established. In particular this
does not authorize replacing beta by beta_n or by a parameter chosen
separately for each prime. Rationality of a fixed parameter ensures the
arithmetic construction is rational; it does not supply uniformity.

The review also led jointly with the author to a sharper exact integer
ledger. For beta=r/s in lowest terms, r>=0,s>=1, n>=1, set



$$
H_n=4^{n+1}(2n+1)!,\qquad L_n=\operatorname{lcm}(1,\ldots,n).
$$



Then



$$
D_n=H_n^2 L_n s^{2n+1}
\tag{2}
$$



clears the raw rational endpoint pair X_beta,Y_beta. This removes
s^(2n+1)(r+s)^n from the older safe clearer. For integer beta this
clearer is independent of beta. This is denominator bookkeeping, not
a theorem about the final reduced denominator.

## 1. Affine normalization and the pure-pi approximant

Writing a=1+beta, substitution t=(beta+iu)/a gives



$$
\mathcal L_\beta(P)=\frac2a\int_{-1}^1P((\beta+iu)/a)\,du,
 \quad F_\beta(z)=z\mathcal L_\beta((1-tz)^{-1}).
$$



The factor2/a is necessary and agrees with F_beta'(0)=4/a. Combining
the leading coefficient of the Legendre polynomial with the displayed
prefactor makes p_(k,beta) monic, and its norm is exactly



$$
h_{k,\beta}=\frac{4(-4)^k}
 {a^{2k+1}(2k+1)\binom{2k}{k}^2}.
$$



For S_beta(t)=(at-beta+1)/2 the measure contributes2/a, each polynomial
contributes(2/a)^k, and the norm therefore contributes(2/a)^(2k+1).
The kernel scale is consequently a/2, not1. The second-kind integral
has the additional factor a/2 from 1/(1-t), so it scales as(2/a)^k.
These checks also verify the projection-error scale
Psi_beta=(a/2)Psi_1 composed with S_beta.

The pure diagonal Padé transformation multiplies by(a-beta z)^n/a^n
after substituting w=z/(a-beta z). It preserves the degree caps and
the order2n+1 condition. Its denominator is the canonical monic-reversal
denominator and is positive at z=1. Since w(1)=1, the reduced rational
endpoint is exactly invariant. Parity-related degree drops at beta=0
cause no failure of this argument; its degree bounds need not be equalities.

## 2. The anchored HP identities and a fresh symbolic check

The high Taylor rows run from n+1 through2n+1 and give exactly the n+1
reproduced moments. Thus C*=-ell_B K determines C completely. The
remaining endpoint row is(1+t_0)B_0+(1+t_1)B_1=0. Its stated raw
representative gives X=(1+t_1)a_0-(1+t_0)a_1 and Y=t_1-t_0.

The whole-remainder identity is obtained by subtracting all Taylor terms
through degree n; it is not a first-tail estimate. The factorial series
defining ell_j(Psi) converges absolutely. For beta>0, the Taylor radius
of F_beta exceeds1, so evaluation is direct. At beta=0 the endpoint
identity follows by the indicated Abel or continuity argument; it does
not imply any analytic nonvanishing theorem there.

I independently reconstructed the n=2 family from the direct moments



$$
m_k=\frac4{a^{k+1}}
 \sum_{\substack{0\le j\le k\\j\text{ even}}}
 \binom kj\frac{(-1)^{j/2}\beta^{k-j}}{j+1}.
$$



Solving the resulting three-by-three rational moment matrix, reversing
C*, and reconstructing A verifies every high row and endpoint equation.
The resulting raw endpoint and ratio are exactly



$$
Y_{2,\beta}=(\beta+1)(14\beta^2-17\beta+17)/32,
$$





$$
X_{2,\beta}/Y_{2,\beta}=
 -\frac{13\beta^5+\beta^4+2562\beta^3-382\beta^2-191\beta+3277}
 {32(\beta+1)(14\beta^2-17\beta+17)}.
$$



This independent derivation agrees with the source's symbolic identity.
The quadratic has negative discriminant and positive leading coefficient,
so Y is nonzero for beta>=0. The ratios at beta=0,1,2 differ; a projective
rescaling cannot change a rational ratio. Thus the anchored e^z problem
has actual parameter dependence even though the pure-pi endpoint does not.

## 3. The fixed-beta>1/3 sign proof

The rescaled GWS argument is valid. If reciprocal roots lie in the disk
with center M/2 and radius M/2, they lie in |z|<=M. The chosen threshold
N>=24M+12 gives lambda_i>N/6-1>=4M+1. On[0,2M],



$$
\sum_i z/(\lambda_i-z)\le2z\sum_i1/\lambda_i\le4M<N.
$$



Hence the positive zeros of Nf+zf' lie above2M. Their reciprocal sum
is at most2, so the claimed e^(-4M) and e^(2M) bounds follow by taking
products. The corresponding ell_0 and ell_1 symbols satisfy the same
safe estimates. The convex-disk GWS hypothesis and the conjugate-pair
homotopy verify the sign; no positivity of the complex measure is used.

For the actual numerator Q, its Jacobi Hermitian part gives the lower
real-part bound(beta-1/3)/a. The comparison in the source's equation(24)
also checks exactly: after dividing numerator and denominator by PV,
it is



$$
\epsilon_n\frac{1-|\alpha_n^*|U/V}
 {1+(P'/P)U/V},
$$



with U/V<=a/beta, |alpha_n*|<1/(3a), and P'/P<=4/(3a).
This gives the stated lower factor(3beta-1)/(3beta+4).

Shifting the factorial index to N=n+r when expanding Q/(1-t) is valid,
since deg Q=n+1<=N+1. The identity
sum_(N>=n)N/(N+1)!=1/n! controls the entire tail. The matched endpoint
tends to zero, making the correction Y ell_1(Psi) smaller than its
nonzero Delta term eventually. Thus the sign and rate follow at fixed beta.

## 4. Why the stronger theorem holds for every fixed positive beta

The origin-ratio proof must avoid assuming a one-step contraction
uniformly for small beta. The source now does so correctly. With
c=beta/a>0 and gamma=1/(4a^2), the ratios are positive and bounded.
Their liminf and limsup satisfy L=c+gamma/U and U=c+gamma/L;
multiplication shows cU=cL, giving convergence. This proves the
origin-ratio limit mu for every fixed beta>0. The endpoint and second-kind
limits lambda and alpha* also follow as stated, and mu+alpha*>0.

The exact Legendre derivative identity was checked with all normalization
factors. At x=i beta,



$$
\frac{p_{n,\beta}'(0)}{n p_{n,\beta}(0)}
 =-\frac a{1+\beta^2}
 \left(\beta+\frac{n}{a(2n-1)\mu_{n-1}}\right).
$$



Its limit is -a/sqrt(1+beta^2). The fixed reciprocal-root bound a/beta
then controls the second-order logarithmic error uniformly on every
compact scaled disk, proving the local exponential limit.

The degree-two factorial lemma's leading-order part applies with any
one fixed reciprocal-root bound, by replacing its3^k/k! domination
with(2L)^k/k!. The normalized V and W quotients are analytic and bounded
on any fixed disk |t|<=rho<beta/a, using the corner resolvent and the
strictly positive limiting scalar denominators. In particular the roots
of Q itself need not satisfy a positive-half-plane bound here.

It follows that Delta(V)~V(0)e^(-c_beta)/n!, and likewise for W and
ell_1(W). The latter correction in the exact R/Y identity is relatively
negligible because V(0)/n! tends to zero. The exact ratio



$$
\frac{W(0)}{V(0)}=(-1)^{n+1}\epsilon_n
 \frac{\mu_n+\alpha_n^*}{\mu_n+\lambda_n}
$$



therefore proves(1), including eventual nonvanishing and its sign.

## 5. Sharper polynomial arithmetic and the revised clearer

The following derivation was obtained independently by both the author
and reviewer, then checked against the exact affine laws.

The ordinary Legendre integral-coefficient formula gives



$$
4^{n+1}K_{n,\beta}(t,u)\in\mathbb Z[\beta,t,u],
 \qquad \deg_\beta K\le2n+1.
$$



Its coefficient of t^(n-l) is divisible by a^(n-l+1). After factorial
contraction this proves



$$
H_n C_{j,l}(\beta)/a^{n-l+1}\in\mathbb Z[\beta].
\tag{3}
$$



Since [z^k]F_beta=4 Im(beta+i)^k/(k a^k), every low product with l+k<=n
cancels its apparent a^k denominator by(3). Therefore



$$
H_nL_n a_j\in\mathbb Z[\beta].
\tag{4}
$$



There is no remaining(r+s)^n factor in this denominator.

For the degree bound, let V_beta=K_(n,beta)(t,1) and introduce the
rational polynomial J_beta=pi V_beta-H_(n,beta). Each of its coefficients
is rational, since v_k/p_k(1)=pi-f_k and f_k is rational. Both V and J
have the exact affine scale(a/2) times their beta=1 polynomial evaluated
at S_beta(t). Consequently they have beta-degree at most n+1. Moreover,



$$
t_j=\ell_j V_\beta,\qquad
 a_j=-E_{n-j}+\ell_j J_\beta.
$$



Their top beta^(n+1) coefficients are constant multiples of the same
contractions ell_j((t-1)^n). Thus the beta^(2n+2) coefficient in
t_1a_0-t_0a_1 cancels identically. We obtain



$$
H_n^2 L_n X_\beta\in\mathbb Z[\beta],\quad
 \deg_\beta X\le2n+1,\qquad
 H_nY_\beta\in\mathbb Z[\beta],\quad
 \deg_\beta Y\le n+1.
\tag{5}
$$



Evaluating(5) at beta=r/s proves the sharper clearer(2). Actual degree
drops are harmless. Since the old clearer was
H_n^2 L_n s^(4n+2)(r+s)^n, the removed factor is exactly
s^(2n+1)(r+s)^n. Both clearers give the same reduced q when their full
gcd is taken; a reduction of an arbitrary clearer alone is not a
reduction of q.

## 6. The exact arithmetic target for choosing a fixed parameter

The strengthened analytic theorem leaves a single common exponential
threshold T=2log(1+sqrt2) for all fixed positive parameters. Its positive
constant k(beta) cannot create an exponential margin. Define the actual
integer polynomials



$$
\mathcal X_n(\beta)=H_n^2L_n X_\beta,
 \qquad\mathcal Y_n(\beta)=H_n^2L_n Y_\beta.
$$



Using N=2n+1, homogenize both at the same degree:



$$
P_n(r,s)=s^N\mathcal X_n(r/s),\qquad
 Q_n(r,s)=s^N\mathcal Y_n(r/s).
$$



These are integers, and the exact normalized arithmetic object is



$$
q_{n,r/s}=\frac{|Q_n(r,s)|}{\gcd(P_n(r,s),Q_n(r,s))}.
\tag{6}
$$



A sufficient favorable theorem is the existence of **one fixed** coprime
positive pair(r,s), an eta>0, and infinitely many n such that



$$
\log\gcd(P_n(r,s),Q_n(r,s))
 \ge\log|Q_n(r,s)|-(T-\eta)n.
\tag{7}
$$



Equivalently, the actual positive valuation defects of the two raw
rational endpoints must satisfy



$$
\sum_p\max(0,v_p(Y_{n,r/s})-v_p(X_{n,r/s}))\log p
 \le(T-\eta)n.
\tag{8}
$$



The common factors introduced by H_n,L_n and homogenization cancel in
these expressions automatically. Thus a proposed prime saving must be
proved in the valuation difference, not just in either cleared integer.

There is a further exact restriction on this target. Let A=r+s and
d_(n,beta)=A^(2n+1)lcm(1,...,2n+1), which clears all moments through2n.
The last two high moment rows give, for every integral matched triple,



$$
\frac{(2n)!}{\gcd((2n)!,d_{n,\beta})}\mid B_0,B_1,Y.
\tag{9}
$$



For fixed beta, a nonzero endpoint therefore has size at least
exp(2n log n-O_beta(n)) before its endpoint gcd is removed. Parameter
variation has not eliminated that factorial-scale requirement. Also the
common coefficient denominator of C_0-C_1 is at least
exp(2n log n-O_beta(n)), by its exact moment2n/(2n+1)!.

The next arithmetic work should address(7) or its complementary
lower-bound obstruction for a fixed parameter. Positive integer beta
has the useful ledger simplification s=1, but this does not prove it
outperforms rational parameters after reduction. There is presently no
proved arithmetic criterion selecting a particular beta as favorable;
neither its Taylor radius, kernel growth factor, nor k(beta) supplies one.

## 7. Moving parameters remain outside the proved theorem

Near beta=0, the reciprocal-root bound a/beta diverges and the available
resolvent disk shrinks. At large beta, the kernel's exponential growth
factor changes; t_1 tending to zero at fixed beta does not automatically
hold along beta_n. The height of r_n/s_n also enters the exact integer
pair above. Each issue must be controlled by a separate uniform proof
before allowing n-dependent parameters.

Choosing beta separately modulo different primes is an arithmetic local
construction, not a fixed rational parameter in the analytic theorem.
It needs a compatible single parameter or a new moving-parameter theorem
with its actual height cost. No such compatibility or uniformity has
been assumed in this review.
