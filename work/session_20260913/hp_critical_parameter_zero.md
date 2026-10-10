> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The critical real parameter: a simple zero and an exact tuning criterion

Date: 2026-09-13. Continuation of `hp_moving_mobius_parameter.md`.
This is an analytic and arithmetic reduction, not a proof that e+pi is
rational or irrational.

## 1. Statement with the parameter and normalization fixed

Write



$$
\rho=1+\sqrt2,\quad
 \kappa_*=(2e\rho)^{-1},\quad
 c=\frac72\kappa_*,\quad
 b_n(x)=\kappa_*n+c\log n+x.
$$



Let epsilon_n>0 be the common pure pi Padé error, and let R/Y be the
exact normalized degree-(n,1,n) matched remainder for the Möbius parameter
b_n(x). Define



$$
E_n(x)=\frac{(-1)^nR_{n,b_n(x)}(1)}{Y_{n,b_n(x)}\epsilon_n}.
 \tag{1}
$$



The preceding note defined a positive constant
C_*=e^(-1)C_P/(2pi sqrt(2pi)), with
p_(n,1)(1)~C_P(rho/4)^n, and
x_*=-kappa_*log(C_*sqrt(2)). The following stronger convergence holds:



$$
\boxed{E_n(x)\longrightarrow F(x):=1-\exp((x-x_*)/\kappa_*)}
 \tag{2}
$$



locally uniformly on the complex x-plane. For each compact set, E_n is
holomorphic on its neighborhood for every sufficiently large n. Every
fixed-order derivative also converges locally uniformly.

For any fixed R>0, the real interval [x_*-R,x_*+R] contains exactly one
real zero x_n^* of E_n for all sufficiently large n. It is simple, and



$$
x_n^*\to x_*,\qquad E_n'(x_n^*)\to-1/\kappa_*.
 \tag{3}
$$



The resulting real parameter
b_n^*=kappa_*n+c log n+x_n^* is the same locally unique branch regardless
of the fixed R once n is large. This is uniqueness in each fixed critical
window, not a claim about every real zero of the degree-(2n+1) endpoint
polynomial.

## 2. Why complex parameters preserve the actual estimates

The proof of (2) requires more than real uniform convergence. The
following verifies the complex extension of each analytic dependency in
the moving-parameter note. Fix a disk |x|<=R_0, and let n grow.
Then Re(b_n(x)) is asymptotic to kappa_*n and |Im b_n(x)| is bounded.
In particular a=1+b is nonzero and all relevant origin polynomial values
are nonzero.

The vertical moment identity extends algebraically to these complex
parameters:



$$
\mathcal L_b(P)=\frac2a\int_{-1}^1P((b+iu)/a)du.
$$



Its endpoint is exactly pi, since
L_b(1/(1-t))=2int_(-1)^1 du/(1-iu)=pi, independently of b. Thus no branch
change of arctan has been assumed. The polynomial, norm, kernel and
second-kind scaling formulas are rational identities in b and continue
to hold. The definitions of X,Y and R/Y therefore remain the same
analytic identities as on the real axis.

The zeros of U=p_(n+1,b) are (b+iu_j)/a, with real Legendre zeros
|u_j|<1. Their reciprocals converge to one uniformly in both the zero
index and the bounded complex x. They have a fixed absolute bound, and



$$
U(z/n)/U(0)\to e^{-z}
 \tag{4}
$$



locally uniformly in z and uniformly in x. This follows by expanding the
logarithm of the root product: its quadratic remainder is O(1/n) on
fixed z-disks, while the average reciprocal root tends uniformly to one.

The Jacobi matrix for U is no longer constrained by a real Hermitian
part when b is complex. Instead, use the stronger elementary estimate
that applies in this window: its diagonal is b/a=1-1/a and its
off-diagonal entries have absolute value at most 1/(sqrt(3)|a|).
Consequently



$$
\|J_{n,b}-I\|\le(1+2/\sqrt3)/|a|=O(1/n)
 \tag{5}
$$



uniformly in x. On any fixed disk |t|<=r<1, the resolvent is therefore
uniformly bounded by a Neumann series, and its corner entry satisfies



$$
q_n(t)=p_{n,b}(t)/p_{n+1,b}(t)\to1/(t-1)
 \tag{6}
$$



uniformly in t,x, together with t-derivatives on smaller disks.
In particular mu_n=-1/q_n(0)->1. The endpoint and second-kind ratios
retain their exact scaling by 2/a, so
a lambda_n->rho/2 and a alpha_n^*->(1-sqrt(2))/2 uniformly.
Every denominator in the normalized quotients G_V,G_W and their
difference factorization is thus bounded away from zero for large n.
Their uniform analytic bounds and H_n'(0)->-1 hold in this complex
window just as on the real axis.

All factorial estimates in the preceding note used absolute coefficient
bounds and a summable exponential majorant. They therefore extend to
these complex coefficients without a positivity assumption. In
particular the leading factorial estimates, and the determinant with
its factored small coefficient c_n, have uniform complex relative errors
tending to zero. The positivity arguments used for real parameters are
replaced here by nonzero complex leading terms.

For the kernel asymptotic one must also replace absolute values by the
correct signed rational identities. Set
U_0=(-1)^n p_(n,b)(0) and h_0=(-1)^n h_(n,b). Pairing the real Legendre
zeros gives the complex identity



$$
U_0=(b/a)^n\prod_{u_j>0}(1+u_j^2/b^2)
 =(b/a)^n(1+O(n/|b|^2)),
 \tag{7}
$$



uniformly in x. The exact Christoffel–Darboux value is
V(0)=p_(n,b)(1)U_0(mu_n+lambda_n)/h_0. Thus the same positive real
constant C_P and Stirling estimate yield the **complex** asymptotic



$$
t_1\sim C_*\frac a{\sqrt n}
 \left(\frac{2e\rho b}{n}\right)^n.
 \tag{8}
$$



There is no ambiguous power here: it is an integer n-th power. Expanding
log(1+(c log n+x)/(kappa_*n)) in its disk about one gives uniformly



$$
\left(\frac{b}{\kappa_*n}\right)^n
 =n^{7/2}\exp(x/\kappa_*)(1+O((\log n)^2/n)).
 \tag{9}
$$



It follows that t_1/n^4 tends uniformly to
C_*kappa_*exp(x/kappa_*), which is bounded away from zero on each compact
x-set. Hence 1+t_1 does not vanish there for large n. Also
Delta(V)/t_1->1 uniformly, so Delta(V) does not vanish. The rational
endpoint quotient R/Y, and therefore E_n, are holomorphic on the fixed
x-disk for all sufficiently large n; the matching system is normal there.

Finally the exact identity and determinant estimate from the preceding
note give, uniformly in complex x,



$$
E_n(x)=\frac{\mu_n+\alpha_n^*}{\mu_n+\lambda_n}
 \left\{(1+o(1))-
 \frac{c_n t_1}{n^3}(1+o(1))\right\}.
 \tag{10}
$$



The prefactor tends to one, and c_n t_1/n^3 tends to
C_*sqrt(2) exp(x/kappa_*). These limits prove (2) uniformly on the
chosen disk. Since the disk was arbitrary, they prove local uniform
holomorphic convergence on the plane in the stated eventual sense.

## 3. Derivative control, the simple zero, and a local error estimate

Apply Cauchy's integral formula on a slightly larger fixed disk than any
given compact set. Uniform convergence in (2) implies uniform convergence
of each fixed-order derivative there. For real x,



$$
F'(x)=-\kappa_*^{-1}\exp((x-x_*)/\kappa_*)<0.
$$



The coefficients and the target e+pi are real for real b, so E_n and its
derivative are real on the real axis. On I_R=[x_*-R,x_*+R], derivative
convergence proves E_n'<0 for all sufficiently large n. The endpoint
values of E_n have the same opposite signs as those of F. Thus E_n has
exactly one zero in I_R. Its derivative is nonzero, so it is simple.
Uniform convergence forces that zero to converge to x_*, and derivative
convergence proves (3). No assertion of uniqueness is deduced from a
mere first-order value asymptotic.

For example, for all sufficiently large n and all real x in I_R,



$$
\frac{e^{-R/\kappa_*}}{2\kappa_*}
 \le |E_n'(x)|\le
 \frac{2e^{R/\kappa_*}}{\kappa_*}.
 \tag{11}
$$



The mean value theorem between x and x_n^* consequently yields



$$
\boxed{c_R\epsilon_n|b-b_n^*|
 \le |R_{n,b}(1)/Y_{n,b}|
 \le C_R\epsilon_n|b-b_n^*|}
 \tag{12}
$$



for b=b_n(x), x in I_R, where the positive constants may be taken from
(11). This comparison is uniform down to arbitrarily small real
distances from the actual zero. It therefore supplies the precision
control that the earlier o(1) cancellation formula alone could not.

## 4. The exact reduced-denominator criterion, with no assumed tuning

Let b_n=r_n/s_n be any sequence of rational parameters in a fixed
critical interval I_R. Let X,Y be the raw rational endpoint pair from
the parameter note, and let q_(n,b) be the reduced positive denominator
of X/Y. The primitive form is



$$
\mathcal P_{n,b}=q_{n,b}(e+\pi+X/Y).
$$



If b_n differs from b_n^*, the form is nonzero. Equation (12) gives



$$
c_R q_{n,b_n}\epsilon_n|b_n-b_n^*|
 \le|\mathcal P_{n,b_n}|
 \le C_R q_{n,b_n}\epsilon_n|b_n-b_n^*|.
 \tag{13}
$$



Thus along any subsequence with nonzero distance, shrinking primitive
forms are **equivalent** to



$$
q_{n,b_n}\epsilon_n|b_n-b_n^*|\longrightarrow0.
 \tag{14}
$$



A sufficient concrete exponential condition uses only nonzero-distance
indices. Define I={n:b_n!=b_n^*}, and assume I is infinite. Then



$$
\liminf_{\substack{n\to\infty\\n\in I}}
 \frac{\log q_{n,b_n}+\log|b_n-b_n^*|}{n}
 <2\log(1+\sqrt2),
 \tag{15}
$$



would prove irrationality by the usual lower bound on a nonzero integer
form at a rational number. Zero-distance indices are not allowed to
realize this liminf. No
sequence satisfying (14) or (15) is constructed here.

An exactly rational zero parameter would instead give
e+pi=-X/Y rational, because its endpoint is nonzero. No such rational
zero is certified. Merely knowing that a unique real zero exists cannot
decide either arithmetic alternative.

For b=r/s the complete unchanged ledger is



$$
D=H^2L_n s^{2n+1},\quad H=4^{n+1}(2n+1)!,\quad
 q_{n,b}=|DY|/\gcd(|DX|,|DY|).
 \tag{16}
$$



The new local estimate (12) allows precise real tuning, but it neither
reduces the exponent 2n+1 of the parameter denominator in this common
clearer nor proves any favorable gcd. In the critical window the raw Y
has order n^4. Hence the available upper bound from (16) is of size
exp(4n log n+O(n))s^(2n+1), up to polynomial factors. Combining that
upper bound with a generic error of order 1/s^2 does not establish (14).
This failure of the available bound is not a lower bound on the actual
q and does not rule out exceptional cancellation in its gcd.

There is now also an actual lower divisor, proved in
`hp_parameter_primitive_denominator.md` and independently checked in
`hp_parameter_primitive_denominator_independent_review.md`. Let s_> and
(r+s)_> denote the full prime-power parts supported on primes p>2n+1,
and let



$$
T_n=nU_n^2-nU_nV_n+V_n^2>0,\quad
 U_n=n!L_n^n(1),\quad V_n=n!L_{n-1}^{n+1}(1).
$$



Then



$$
\left(s_>/\gcd(s_>,T_n)\right)^n(r+s)_>\mid q_{n,r/s}.
 \tag{16a}
$$



Unlike (16), this factor survives the endpoint gcd. It gives a necessary
version of (14) with this divisor in place of q. It is not sufficient;
small-prime factors and the varying coefficient T_n prevent replacing
the displayed parameter factor by the whole s. The joint tuning problem
therefore remains open, with a more explicit arithmetic restriction.

## 5. Fractional parts of the real zero: a density result only

The sequence of locally unique real parameters satisfies



$$
b_n^*=\kappa_*n+c\log n+x_*+o(1).
 \tag{17}
$$



It is uniformly distributed modulo one. First, kappa_* is irrational:
if it were algebraic, e=1/(2rho kappa_*) would be algebraic, contradicting
the classical transcendence of e. In fact this also proves kappa_*
transcendental, but only irrationality is needed here.

For every nonzero integer h, let z=exp(2pi i h kappa_*), so z!=1. Its
geometric partial sums are bounded. The weight
w_n=n^(2pi i h c) has |w_n|=1 and
|w_(n+1)-w_n|=O_h(1/n). Summation by parts therefore gives



$$
\sum_{n\le N}\exp(2\pi i h(\kappa_*n+c\log n+x_*))
 =O_h(\log N).
$$



The o(1) perturbation in (17) changes the normalized sum by o(1), by
Cesaro averaging of its vanishing termwise difference. Every nontrivial
Fourier average thus tends to zero. Weyl's criterion proves uniform
distribution of (b_n^*) modulo one.

Consequently, for every fixed 0<delta<1/2, the natural density of indices
with distance(b_n^*,Z)<delta is 2delta. For every sequence delta_n->0,
the set with distance(b_n^*,Z)<=delta_n has upper density zero: eventually
it is contained in the fixed-delta set, and then delta can decrease to
zero. This includes exponentially small distances, but does **not**
assert that there are only finitely many such indices.

If only integer parameters in a fixed critical interval are allowed,
(12) therefore shows that an additional fixed exponential improvement
over epsilon_n can occur only on a density-zero set of indices. The same
conclusion holds when the rational parameter denominator is bounded by
one fixed integer, by taking a finite union of rational residue grids.
No rate for growing denominators is asserted. A density-zero exceptional
subsequence could still be infinite and is exactly enough to matter for
an irrationality construction, so this corollary does not close (14).

The remaining arithmetic target is thus explicit: control the reduced
denominator and the distance to this particular moving real zero
simultaneously. Holomorphic normality, simple-zero control, and ordinary
equidistribution do not supply that joint estimate.
