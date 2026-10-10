> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Degree-one exponential coefficient: endpoint sign, sharp analytic rate, and remaining gcd

Date: 2026-09-13. Continuation of `unequal_degree_hp_attempt.md`.
No new matrix scan was performed. The results below concern the original
Möbius pullback F, not its high-radius polynomial composition.

## Outcome

For the unique endpoint-matched family



$$
R_n=A_n+B_n e^z+C_nF(z)=O(z^{2n+2}),\quad
 \deg A_n,\deg C_n\le n,\quad\deg B_n\le1,
 \quad B_n(1)=C_n(1),
$$



the following are now proved:

1. For every n>=64 the solution is unique up to scaling, B_n(0) is
   nonzero, and with B_n(0)=1 its endpoint Y_n=B_n(1) is strictly positive.
   An explicit Christoffel–Darboux formula and factorial bounds control Y_n.

2. For every n>=512 the normalized evaluated remainder R_n(1)/Y_n has
   sign (-1)^n and is bounded above and below by fixed positive constants
   times the ordinary diagonal logarithmic Padé error epsilon_n. In
   particular
   
   

$$
\log|R_n(1)/Y_n|=-2n\log(1+\sqrt2)+o(n).
   \tag{1}
$$


   This is a proved evaluated estimate with nonvanishing, not a deduction
   from finite rank or a first Taylor coefficient.

3. If q_n is the reduced denominator of A_n(1)/Y_n, the complete primitive
   endpoint form satisfies
   
   

$$
\log|L_n|=\log q_n-2n\log(1+\sqrt2)+o(n).
   \tag{2}
$$


   The missing arithmetic problem is precisely the growth of q_n. For
   example, liminf(log q_n)/n<2log(1+sqrt2) would give a nonzero shrinking
   subsequence and prove irrationality. No such denominator estimate is
   proved here. Unlike b=0, this note does not prove primitive growth.

The new mechanism is a concrete Grace–Walsh–Szegő polarization of a
Laguerre polynomial and its logarithmic derivative. It proves signs of
the actual factorial moment transforms. It does not assume positivity
of the original complex moment functional.

## 1. Archive overlap and notation

An archive search for Christoffel–Darboux, reproducing kernels, polarization,
and the allocation (n,1,n) found no preceding result for this family.
The root-of-unity external-node reproducing-kernel notes concern a different
positive real measure and a different determinant carrier. Item176 treats
B=C as the same polynomial with constant A. The constant-coefficient
composed-function theorem has c=0. Neither covers this calculation.

Use the previously verified objects



$$
F(z)=4\arctan\frac{z}{2-z},\quad
 \mathcal L(P)=\int_{-1}^1P((1+iu)/2)\,du,\quad
 F(z)=z\mathcal L\bigl((1-tz)^{-1}\bigr),
$$





$$
p_k(t)=\frac{i^kP_k(-i(2t-1))}{\binom{2k}{k}},\quad
 h_k=\mathcal L(p_k^2)=\frac{2(-1)^k}{(2k+1)\binom{2k}{k}^2}.
\tag{3}
$$



Here P_k is the ordinary Legendre polynomial. The p_k are monic rational
polynomials, p_k(1)>0, p_k(0)=(-1)^k p_k(1), and



$$
p_{k+1}=(t-1/2)p_k+\alpha_kp_{k-1},\qquad
 \alpha_k=\frac{k^2}{4(4k^2-1)}\in(1/16,1/12].
\tag{4}
$$



The kernel



$$
K_n(t,s)=\sum_{k=0}^n\frac{p_k(t)p_k(s)}{h_k}
 =\frac{p_{n+1}(t)p_n(s)-p_n(t)p_{n+1}(s)}{h_n(t-s)}
\tag{5}
$$



reproduces every polynomial of degree at most n under L. In particular



$$
K_n(0,1)=\sum_{k=0}^n\frac{p_k(1)^2}{|h_k|}
 =\frac{2p_n(1)p_{n+1}(1)}{|h_n|}>0.
\tag{6}
$$



Define rational functionals on monomials by



$$
\ell_0(t^j)=\frac1{(n+j+1)!},\qquad
 \ell_1(t^j)=\frac1{(n+j)!},\qquad
 \ell_\Delta=\ell_1-\ell_0.
\tag{7}
$$



The exact projection already derived in the preceding note is



$$
C^*(t)=-\ell_B^{(s)}K_n(t,s),\quad C^*=t^n C(1/t),\quad
 \ell_B=B_0\ell_0+B_1\ell_1.
\tag{8}
$$



Writing



$$
t_j=\ell_j^{(s)}K_n(1,s)\quad(j=0,1),\qquad\delta=t_1-t_0,
$$



the endpoint equation is exactly



$$
(1+t_0)B_0+(1+t_1)B_1=0.
\tag{9}
$$



## 2. A uniform factorial-transform sign lemma

The only external polynomial-location theorem used here is the
Grace–Walsh–Szegő coincidence theorem: a symmetric multiaffine polynomial
evaluated at points in a closed disk has the same value at some diagonal
point in that disk. The disk is convex, so the theorem's convexity
hypothesis is satisfied even if the total degree drops. See Proposition1
of Petter Brändén and David Wagner, *A converse to the Grace–Walsh–Szegő
theorem*, [primary paper](https://arxiv.org/pdf/0809.3225). Every other
root bound needed below follows from the displayed finite matrices.

### 2.1 The actual Laguerre symbol

For integers N>=128 and k<=N+1 set



$$
f_{N,k}(z)=\sum_{j=0}^k\frac{(-1)^j\binom kj z^j}{(N+2)_j},
 \quad g_{N,k}(z)=Nf_{N,k}(z)+zf'_{N,k}(z).
\tag{10}
$$



Thus f is the normalized Laguerre polynomial L_k^(N+1). Its zeros
lambda_i are the eigenvalues of the real symmetric tridiagonal matrix
with indices j=0,...,k-1, diagonal N+2+2j, and off-diagonal
sqrt((j+1)(j+N+2)). This equality follows by comparing its characteristic
polynomial recurrence with the coefficients in (10).

Gershgorin's theorem gives, writing x=j+1<=k,



$$
\lambda_i\ge N+2x-2\sqrt{x(x+N+1)}
 \ge (3-2\sqrt2)N+2-2\sqrt2 > N/6-1>12.
\tag{11}
$$



The first expression decreases with x, so the second inequality uses
x<=N+1. Also the coefficient of z in f gives
sum_i1/lambda_i=k/(N+2)<=1.

All zeros gamma_i of g are real and positive, by Rolle's theorem applied
to (z^N f(z))'. None lies in [0,6], because there



$$
g/f=N-\sum_i\frac z{\lambda_i-z}\ge N-12>0.
$$



The zeros of g therefore exceed6, and



$$
\sum_i1/\gamma_i=\frac{(N+1)k}{N(N+2)}\le2.
\tag{12}
$$



For |z|<=3, factoring g gives



$$
e^{-12}\le|g_{N,k}(z)/N|\le e^6.
\tag{13}
$$



Indeed gamma_i>6 and log(1-3/gamma_i)>=-6/gamma_i. The corresponding
polynomial (N+1)f+zf' has its zeros above6 by the same proof and reciprocal
root sum k/(N+1)<=1, so the same safe bounds apply after dividing it by
N+1. For k=0 the assertions are direct.

### 2.2 Applying polarization to a polynomial's reciprocal roots

Let Q be a real polynomial of degree k<=N+1, all of whose zeros have real
part at least1/3. None is zero. If its reciprocal roots are zeta_j, then
|zeta_j-3/2|<=3/2, and



$$
Q(t)/Q(0)=\prod_{j=1}^k(1-\zeta_jt).
$$



The symmetric multiaffine polynomial



$$
\sum_{j=0}^k\frac{(N+j)(-1)^j e_j(\zeta_1,\ldots,\zeta_k)}{(N+2)_j}
\tag{14}
$$



has diagonal restriction g_{N,k}. It equals
(N+1)! times the factorial transform
sum_j(N+j)Q_j/(N+j+1)!, divided by Q(0). GWS and (13) bound its modulus
between N e^(-12) and N e^6.

Its sign is positive. To see this without asserting positivity of a
complex measure, move every zeta_j linearly to3/2 inside the disk. Conjugate
pairs remain paired, so (14) remains real. GWS says it never vanishes,
and at the common real point it is g(3/2)>0. The same reasoning applies
to the (N+1)f+zf' transform.

Consequently, with sigma=sign Q(0),



$$
e^{-12}\frac{N|Q(0)|}{(N+1)!}
 \le\sigma\sum_j\frac{(N+j)Q_j}{(N+j+1)!}
 \le e^6\frac{N|Q(0)|}{(N+1)!},
\tag{15}
$$



and the transform sum_j Q_j/(N+j)! has the same sign and is at most
e^6 |Q(0)|/N! in absolute value.

### 2.3 The sharper constants needed for p_k

For k<=n the reciprocal roots of p_k lie in |z-1|<=1, because its roots
are (1+iu_j)/2 with real u_j. For n>=64, the same matrix bound with
k<=n gives lambda_i>=3n-2sqrt(n(2n+1))>n/6-1>8.
The zeros of n f+zf' exceed4, since at z<=4 the sum z/(lambda_i-z) is
at most8. Its reciprocal root sum is at most1. On |z|<=2 the bounds are
therefore e^(-4) and e^2. The conjugation-preserving homotopy to1 proves



$$
e^{-4}\frac{n|p_k(0)|}{(n+1)!}
 \le(-1)^k\ell_\Delta(p_k)
 \le e^2\frac{n|p_k(0)|}{(n+1)!}.
\tag{16}
$$



Likewise ell_1(p_k) has sign (-1)^k and absolute value at most
e^2 |p_k(0)|/n!. Applying the same argument directly to f shows ell_0
has that sign as well.

## 3. Endpoint sign and factorial/exponential scale

Every summand in delta=sum p_k(1)ell_Delta(p_k)/h_k is positive by
(16). Thus for every n>=64,



$$
e^{-4}\frac{nK_n(0,1)}{(n+1)!}
 \le\delta\le e^2\frac{nK_n(0,1)}{(n+1)!},
 \qquad 0<t_0<t_1\le e^2 K_n(0,1)/n!.
\tag{17}
$$



Equation (9) now proves normality, and with B_0=1 gives



$$
B_1=-\frac{1+t_0}{1+t_1}\in(-1,0),\qquad
 Y=B(1)=\frac\delta{1+t_1}>0.
\tag{18}
$$



The previously established elementary coefficient bounds imply
K_n(0,1)<=(n+1)^2 64^n. Hence t_1 tends to zero factorially.
For n>=512, the explicit estimate t_1<e^(-20) is safe: at512 use
n!>=(n/3)^n and (513)^2<2^19, and thereafter the ratio of
(n+1)^2 64^n/n! at consecutive indices is less than1.

In particular, for n>=512,



$$
\frac{e^{-4}}4\frac{K_n(0,1)}{n!}
 \le Y\le e^2\frac{K_n(0,1)}{n!}.
\tag{19}
$$



Small-index exceptions must not be erased. At n=1, the exact solution is
(A,B,C)=(-(1-z),1-z,-(1-z)/2), with Y=A(1)=0. Thus a statement asserting
nonzero endpoint at every positive index would be false.

## 4. Exact evaluated remainder and its nonvanishing

Let h(t)=1/(1-t), and let H_n be its orthogonal projection onto degree<=n:



$$
H_n(t)=\mathcal L_s\bigl(K_n(t,s)/(1-s)\bigr).
$$



Define the real second-kind quantities



$$
v_k=\mathcal L\bigl(p_k(t)/(1-t)\bigr).
$$



They have strict sign (-1)^k by the already proved Legendre-square Padé
identity. Christoffel–Darboux gives exactly



$$
\Psi_n(t):=h(t)-H_n(t)
 =\frac{v_n}{h_n}\frac{Q_n(t)}{1-t},\qquad
 Q_n=p_{n+1}-a_np_n,\quad a_n=v_{n+1}/v_n<0.
\tag{20}
$$



There is no unproved asymptotic remainder identity here. Integrating the
kernel identity (5) after multiplying by
1/(1-t)-1/(1-s) proves (20) directly.

The exponential tail at1 equals ell_B(h). By (8), the logarithmic tail
equals -ell_B(H_n). The reconstructed A removes exactly their Taylor
coefficients through n. Therefore



$$
R_n(1)=\ell_B(\Psi_n),\qquad
 \ell_B=-\ell_\Delta+Y\ell_1
 \quad\text{under }B_0=1.
\tag{21}
$$



The functionals on the rational function in (20) are defined by its
Taylor series. All sums converge absolutely because the denominators
are factorials.

### 4.1 The actual numerator Q_n has its roots in a fixed half-plane

From (4) and orthogonality,
v_(k+1)=v_k/2+alpha_k v_(k-1) for k>=1. Applying this one index later,
and using the alternating signs, yields



$$
|a_n|=\frac{\alpha_{n+1}}{1/2+|a_{n+1}|}<2\alpha_{n+1}\le1/6.
\tag{22}
$$



The polynomial Q_n is the characteristic polynomial of the complex
symmetric tridiagonal matrix with diagonal entries1/2, except for the
last entry1/2+a_n, and off-diagonal entries i sqrt(alpha_k). The Hermitian
part is just this real diagonal. For any eigenvector, its Rayleigh
quotient therefore shows that every root has real part at least1/3.
This verifies the hypothesis of the factorial-transform lemma for the
actual numerator, rather than assuming its roots have the locations of
the ordinary orthogonal polynomials.

Also, p_(n+1)(1)>=p_n(1)/2 gives



$$
\operatorname{sign}Q_n(0)=(-1)^{n+1},\qquad
 \frac23p_{n+1}(1)\le|Q_n(0)|\le p_{n+1}(1).
\tag{23}
$$



### 4.2 Applying the sign lemma to the rational function

Expand Q_n/(1-t)=sum_(r>=0)t^r Q_n. In each summand use (15) with
N=n+r and k=n+1. For n>=128 its hypotheses hold uniformly in r.
Every summand has the sign of Q_n(0). Moreover



$$
\sum_{r\ge0}\frac{n+r}{(n+r+1)!}=1/n!.
$$



It follows that ell_Delta(Q_n/(1-t)) has that sign and magnitude between
e^(-12)|Q_n(0)|/n! and e^6|Q_n(0)|/n!. The ell_1 transform has the same
sign and magnitude at most e^7|Q_n(0)|/n!, since
sum_(r>=0)1/(n+r)!<=e/n!.

For n>=512, Y<e^(-20) is smaller than (1/2)e^(-19). Thus the two terms
in (21) cannot cancel. They give the explicit safe bounds



$$
\frac{e^{-12}}2\frac{|\Psi_n(0)|}{n!}
 \le |R_n(1)|\le e^8\frac{|\Psi_n(0)|}{n!},
 \qquad\operatorname{sign}R_n(1)=(-1)^n.
\tag{24}
$$



This proof handles the whole evaluated tail. It does not infer its sign
from the first free coefficient.

### 4.3 Comparison with the explicit logarithmic Padé error

Let f_n be as in the preceding b=0 note and set epsilon_n=|pi-f_n|.
Then |v_n|=p_n(1)epsilon_n. From (6), (20), and (23),



$$
\epsilon_n/3\le |\Psi_n(0)|/K_n(0,1)\le\epsilon_n/2.
\tag{25}
$$



Combining (19), (24), and (25) proves for all n>=512



$$
\frac{e^{-14}}6\epsilon_n
 \le (-1)^n R_n(1)/Y_n\le 2e^{12}\epsilon_n.
\tag{26}
$$



The constants are deliberately loose. The exact old integral estimate is



$$
\frac2{(2n+1)\binom{2n}{n}^2p_n(1)^2}
 \le\epsilon_n\le
 \frac4{(2n+1)\binom{2n}{n}^2p_n(1)^2}.
\tag{27}
$$



The positive recurrence (4) at t=1, with alpha_n tending to1/16, implies
log p_n(1)/n tends to log((1+sqrt2)/4). This follows by comparing its
positive solutions beyond any fixed index with the constant-coefficient
recurrences having second coefficient1/16 and1/16+eta, then letting eta
decrease to zero. Together with log binom(2n,n)/n tending to log4,
(27) proves log epsilon_n/n tends to -2log(1+sqrt2). This proves (1).

## 5. Exact rational endpoint formula and the unresolved arithmetic step

Let C_j^*=-ell_j K_n(t,·), reverse to obtain C_j(z), and put



$$
a_j=-[T_n(z^j e^z+C_jF)](1)\in\mathbb Q\quad(j=0,1).
$$



An exact rational representative of the unique matched endpoint pair is



$$
X=(1+t_1)a_0-(1+t_0)a_1,\qquad Y=\delta=t_1-t_0.
\tag{28}
$$



This representative differs from B_0=1 by the positive factor1+t_1.
It has the same ratio x_n=X/Y. If x_n=p_n'/q_n in lowest terms with
q_n>0, the final primitive form is



$$
L_n=p_n'+q_n(e+\pi)=q_nR_n(1)/Y_n.
\tag{29}
$$



For a completely explicit integer ledger, define J_k(t)=2^k i^k
P_k(-i(2t-1)) in Z[t]. Then



$$
K_n(t,s)=\sum_{k=0}^n\frac{(-1)^k(2k+1)}{2^{2k+1}}J_k(t)J_k(s).
\tag{30}
$$



Thus T=2^(2n+1)(2n+1)! clears the coefficients of both C_j and both t_j.
If d_F=2^n lcm(1,...,n), then D=T^2 d_F clears both numbers X,Y in
(28). Writing U=DX and V=DY gives the exact final denominator



$$
q_n=|V|/\gcd(|U|,|V|).
\tag{31}
$$



The choice D is a convenient common denominator, not a claim of minimal
clearing. Any excess common factor appears on both sides of the gcd and
cancels. Therefore a large gcd computed at this scale cannot automatically
be called a new arithmetic gain.

The analytic part is now fully quantified: q_n epsilon_n tends to zero
along a subsequence if and only if the primitive forms tend to zero on
that subsequence, by (26). Sufficient concrete next lemmas are:

* A positive construction: prove for some eta>0 and infinitely many n
  that q_n<=exp((2log(1+sqrt2)-eta)n). With (26), this would prove
  irrationality of e+pi.
* An obstruction for this family: prove liminf(log q_n)/n>
  2log(1+sqrt2), or stronger factorial growth. Then all sufficiently
  large primitive forms would grow.

Neither is established. A bound on t_1-t_0 as a real number does not
control the rational gcd in (31).

The b=0 continued-fraction argument does not transfer automatically.
Using the exponential-height rational logarithmic approximant f_n now
gives e a rational approximation whose error is only bounded by a
constant times epsilon_n through (26), rather than a factorially small
error. The denominator of f_n already has exponential height. A finite
irrationality measure for e alone does not yield the missing favorable
bound on q_n from these estimates.

## Priority and next step

The b=1 family now has proven eventual rank, nonzero endpoint, evaluated
remainder sign, and its exact exponential rate. Further normality checks,
numerical degree scans, or generic asymptotic packaging would not resolve
its remaining issue. The next work should target the explicit two-by-two
rational endpoint determinant (28) and its reduced ratio (31), seeking
an arithmetic identity or a uniform divisibility bound. This is a smaller
and fully specified task than simultaneous control of the original large
Hermite–Padé matrix. No proof of rationality or irrationality of e+pi is
claimed in this note.

## Verification record

`check_hp_b1_identities.py` performs bounded exact algebra checks at
n=1,2,8,16, without solving a new HP matrix. It uses direct binomial
integration for the complex moments and represents every expression in
Q+Q*pi by a rational pair. The Christoffel–Darboux rational remainder,
all required high Taylor coefficients, the equality of the evaluated
e and pi coefficients, and the displayed common denominator all pass.
It also checks the actual factorial-transform signs at five preselected
(N,k) values, including (64,63), (64,64), and (128,128).
Results are in `hp_b1_identity_checks.json`. These controls are separate
from the uniform proofs.

During checking, the initial transcription of (30) omitted (-1)^k.
It has been corrected. The sign comes from h_k and does not change the
denominator clearer T. An independent reviewer identified the same
transcription issue; the earlier analytic proof did not use (30).
