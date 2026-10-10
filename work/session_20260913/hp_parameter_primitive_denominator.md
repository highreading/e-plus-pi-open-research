> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Actual denominator costs of a rational Möbius parameter

Date: 2026-09-13. Original continuation by root of the reviewed parameter
construction. This note concerns the actual reduced endpoint ratio, not
only a common coefficient clearer. Independent review is requested.

## 1. Two exact leading coefficients

Use the degree-(n,1,n) family, n>=1, with the raw endpoint pair



$$
X=(1+t_1)a_0-(1+t_0)a_1,\qquad Y=t_1-t_0,
\quad a_j=-E_{n-j}+\ell_jJ_\beta,\quad t_j=\ell_jV_\beta,
$$



where ell_j(t^k)=1/(n+k+1-j)!, and E_m=sum_(k=0)^m1/k!.
Let p_k,h_k be the monic polynomials and norms at beta=1, and write
P_k=p_k(1). The reviewed affine identities are, with A=(beta+1)/2,



$$
V_\beta(t)=A V_1(1+A(t-1)),\qquad
J_\beta(t)=A J_1(1+A(t-1)).
\tag{1}
$$



Here J=pi V-H is a rational polynomial. All following algebra uses J;
pi is not an arithmetic coefficient of the endpoint polynomials.

If v_k,j_k are the ordinary t coefficients of V_1,J_1, then



$$
v_n j_{n-1}-v_{n-1}j_n=-1/h_n.\tag{2}
$$



Indeed V_1=sum p_k(t)P_k/h_k and
J_1=sum p_k(t)P_k f_k/h_k, where f_k=pi-v_k^{(2)}/P_k is the rational
pure-logarithmic approximant and v_k^{(2)} its second-kind integral.
Only the degrees n and n-1 survive the cross difference. The monic
three-term recurrence gives the exact Wronskian



$$
v_n^{(2)}P_{n-1}-v_{n-1}^{(2)}P_n=-h_{n-1}.
$$



It starts at n=1 from P_0=1, P_1=1/2, v_0^{(2)}=pi,
v_1^{(2)}=pi/2-2 and h_0=2, and propagates by the norm ratio.
Consequently f_(n-1)-f_n=-h_(n-1)/(P_nP_(n-1)), which proves (2).
The P_k are nonzero by their positive endpoint recurrence.

Put Q_k(t)=(t-1)^k, and define



$$
d_n=\ell_1Q_n\,\ell_0Q_{n-1}
       -\ell_0Q_n\,\ell_1Q_{n-1}.
\tag{3}
$$



The degree 2n+2 term of X cancels. In degree 2n+1 only the cross pair
(n,n-1) contributes, so (1)-(2) give



$$
[\beta^{2n+1}]X=-d_n/(2^{2n+1}h_n).
\tag{4}
$$



Terms linear in V,J have degree at most n+1, which is smaller than
2n+1 for n>=1. The change from ordinary coefficients to the Taylor
coefficients at t=1 leaves the cross difference (2) unchanged.

## 2. Exact positive formula; the parameter degree is not merely an upper bound

Let L_k^alpha denote the ordinary generalized Laguerre polynomial and put



$$
U_n=n!L_n^n(1),\quad V_n=n!L_{n-1}^{n+1}(1),\quad
T_n=nU_n^2-nU_nV_n+V_n^2.
\tag{5}
$$



Both U_n,V_n and T_n are integers, by the finite coefficient formula for
Laguerre polynomials. Directly from that formula,



$$
\ell_j Q_k=(-1)^k\frac{k!}{(n+k+1-j)!}L_k^{n+1-j}(1).
\tag{6}
$$



Writing K=L_n^n(1), N=L_(n-1)^(n+1)(1), the identities
L_n^(n+1)=L_n^n+L_(n-1)^(n+1) and
L_(n-1)^n(1)=K/2+N/(2n) yield



$$
d_n=\frac{T_n}{n(2n+1)((2n)!)^2}.\tag{7}
$$



This number is strictly positive. To verify that without a limiting
argument, let K(x)=L_n^n(x). Its differential equation at x=1 gives
K''(1)=nN-nK, while K'(1)=-N. Hence



$$
T_n/(n!)^2=K'(1)^2-K(1)K''(1)>0.
\tag{8}
$$



The last inequality follows from the n distinct real positive zeros of
L_n^n: away from a zero the expression equals
K(1)^2 sum_lambda(1-lambda)^(-2), and at a zero it equals K'(1)^2>0.
Thus it also covers a hypothetical root at1. These elementary Laguerre
facts follow from orthogonality for the positive weight x^n exp(-x)
on (0,infinity); the parameter n>-1 satisfies its hypotheses.
The normalization, derivative and contiguous identities used here are
also recorded in the primary [NIST DLMF recurrence and derivative tables](https://dlmf.nist.gov/18.9),
with the [Laguerre zero results](https://dlmf.nist.gov/18.16#iv).

Finally h_n=2(-1)^n/((2n+1) binom(2n,n)^2). Substituting (7) into (4),



$$
\boxed{[\beta^{2n+1}]X
 =\frac{(-1)^{n+1}T_n}{n2^{2n+2}(n!)^4}\ne0.}\tag{9}
$$



In particular deg_beta X=2n+1 in every degree n>=1, while the reviewed
bound deg_beta Y<=n+1 remains sufficient below. This is a full-degree
identity, not a numerical pattern or a claimed bound on the reduced q.

## 3. A power of the parameter denominator survives the endpoint gcd

Let beta=r/s in lowest terms, s>0, and suppose Y_(n,beta) is nonzero.
Write q_(n,beta)=den(X_(n,beta)/Y_(n,beta)). The reviewed polynomial
ledger implies that all coefficients of X,Y are integral at every prime
p>2n+1. If such a prime divides s and does not divide T_n, (9) is a
p-unit. Its leading term has strictly smaller p-adic valuation than all
other terms after beta=r/s is substituted. Therefore



$$
v_p(X_{n,r/s})=-(2n+1)v_p(s),\qquad
v_p(Y_{n,r/s})\ge-(n+1)v_p(s).
$$



Taking the valuation difference of the actual rational ratio gives



$$
\boxed{v_p(q_{n,r/s})\ge n v_p(s),
 \quad p>2n+1,\quad p\mid s,\quad p\nmid T_n.}\tag{10}
$$



Let s_good be the product of the full prime powers in s meeting these
conditions. Then s_good^n divides q. Unlike an arbitrary clearer upper
bound, this is a lower bound after all endpoint gcd cancellation. The
excluded primes depend explicitly on n through T_n; their mass has not
been bounded. In particular s_good cannot silently be replaced by s.

One can retain high powers even at exceptional primes. Put v=v_p(s) and
a=v_p(T_n). If v>a, the leading X term is again uniquely least, giving
v_p(X)=a-(2n+1)v and v_p(q)>=nv-a. If v<=a the trivial lower bound0
is sufficient. Consequently, if s_> denotes the full prime-power part
of s supported on primes p>2n+1, then



$$
\boxed{\left(\frac{s_>}{\gcd(s_>,T_n)}\right)^n\mid q_{n,r/s}.}
\tag{10a}
$$



Indeed nv-a>=n(v-a) in the first case. This avoids discarding arbitrarily
large powers of a prime merely because it divides T_n once.

There is a second elementary actual-q divisor. At beta=-1, (1) gives
V=J=0, hence X=-1/n! and Y=0. For any p>2n+1 dividing r+s, s is a p-unit;
the same p-integral polynomial identities show that X is a p-unit and
Y is divisible by p^v_p(r+s). Thus



$$
\boxed{v_p(q_{n,r/s})\ge v_p(r+s),\qquad
p>2n+1,\quad p\mid r+s.}\tag{11}
$$



There is no overlap of the prime supports in (10) and (11), because r,s
are coprime. Neither assertion extends to small primes without additional
coefficient valuation analysis.
Thus, writing (r+s)_> for the absolute prime-power part above2n+1,
their product is an actual divisor:



$$
\left(\frac{s_>}{\gcd(s_>,T_n)}\right)^n(r+s)_>
\ \mid\ q_{n,r/s}.
\tag{11a}
$$



## 4. Relevance and remaining obstruction

The critical-window theorem gives |R/Y| comparable to
epsilon_n |beta-beta_n*|. Thus any rational tuning that gives shrinking
nonzero primitive forms must, in particular, satisfy



$$
s_{good,n}^{\,n}\epsilon_n\,|r_n/s_n-\beta_n^*|\longrightarrow0.
\tag{12}
$$



The stronger factor in (11a) may replace s_good^n in (12).

This is necessary, not sufficient, since the other factors of q are
uncontrolled. It proves a genuine arithmetic cost for parameter
denominators with good prime factors. It neither excludes tuning with
the exceptional prime support nor proves that a useful rational tuning
exists. A continued-fraction accuracy statement of order s^(-2) alone
is only an upper-error guarantee and does not establish this
growing-degree requirement when the good part of s is large. It is not
a lower bound on the actual approximation error; no claim about a
particular zero's irrationality measure is made.

The next useful arithmetic step is to control the prime factors of T_n
that divide a candidate s_n, or obtain an actual upper bound for q along
parameters with special support. The exact formula (9) makes that local
question explicit. It is not a proof about the rationality of e+pi.

## 5. Verification record

The separate checker reconstructs V,J and the entire endpoint pair at
n=1,2,4, checks the exact leading coefficient and beta=-1 values, and
uses fully reduced rational ratios at beta=1/p,1/p^2,p-1. All controls
pass. They verify normalization, not the all-degree proof. A separate
agent review has checked the argument and is being saved.
