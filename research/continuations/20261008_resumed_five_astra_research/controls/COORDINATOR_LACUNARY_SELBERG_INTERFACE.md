> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A classical finite product-sum for the actual lacunary pole minor

Coordinator derivation, 8 October 2026. Provisional pending independent review.
This makes the actual LOW/HIGH minor a precisely normalized Schur/Selberg
quantity. No ternary valuation, directional nonresonance, growing saving,
least global clearer or final gcd estimate follows merely from this identity.

## Scoped gate and a literature-scope distinction

The archive-source and 20261007 Markdown searches for Selberg, Kadell,
Schur/Jacobi found sieve results, a different top-symmetric polynomial,
and a catalogue sieve discussion; no same-W Jacobi lacunary minor evaluation
was found in those searched files. This is not an exhaustive absence claim.
The preceding same-W dual interface supplies the original index and boundary
ledger; all earlier complete A1 corrections and returns remain required.

The primary [AFLT-type Selberg integrals](https://arxiv.org/html/2001.05637v2)
was read here only through its Introduction, including equations(1.4)--(1.6),
Theorem1.1 and its hypotheses. The single-Schur specialization is classical
Kadell. The paper's two-polynomial formula has a plethystically shifted second
argument. Our beta parameter is A+1, so its unshifted two-factor simplification
does not apply to s_lambda(y)^2. We use a finite Schur product expansion instead.
No full-paper proof verification is claimed. The single-Schur identity needed
here is proved directly below in the gamma=1 case.

## 1. Direct beta-determinant proof of the single-Schur integral

For positive a,b and an integer w>=1 set

    J_w=det(Beta(a+i+j,b))_(0<=i,j<w),
    dProb=V(y)^2 prod_i y_i^(a-1)(1-y_i)^(b-1)dy/[w! J_w].

For a partition kappa of length<=w the bialternant formula and Andreief give
an exact determinant, with increasing exponents

    t_i=i-1+kappa_(w+1-i), i=1,...,w,
    E s_kappa(y)=det(Beta(a+t_i+j,b))_(i=1..w,j=0..w-1)/J_w.   (1)

For any distinct t_i the beta determinant equals

    Gamma(b)^w prod_i Gamma(a+t_i)/Gamma(a+b+t_i+w-1)
       * V(t_1,...,t_w) * prod_(j=0)^(w-1)(b)_j.              (2)

Divide row i by Gamma(b)Gamma(a+t_i)/Gamma(a+b+t_i+w-1).
The jth remaining polynomial is (a+t)_j(a+b+t+j)_(w-1-j), of degree w-1.
Their alternating determinant is a constant times V(t). Evaluate at
t=-a-r, r=0,...,w-1: the matrix is triangular since (-r)_j=0 for j>r.
Its diagonal is (-1)^r r! (b)_(w-1-r), whereas the Vandermonde there is
(-1)^(w(w-1)/2)prod r!. The ratio is exactly prod(b)_j, proving(2).
These test t lie outside the integral domain but are used only in the
polynomial coefficient identity after the gamma factors were removed.

At t_i=i-1, formula(2) gives

    J_w=prod_(j=0)^(w-1)
        j! Gamma(a+j)Gamma(b+j)/Gamma(a+b+w+j-1).              (3)

Dividing(2) by(3) and using the Weyl dimension formula proves

    E s_kappa(y)=s_kappa(1^w) prod_(i=1)^w
                   (a+w-i)_(kappa_i)/(a+b+2w-i-1)_(kappa_i). (4)

All factors are positive for the present real parameters, and all half-integer
gamma constants cancel in the application below. Formula(4) is a reuse of
classical mathematics, not a newly discovered Selberg theorem.

## 2. The exact original exponent gap

Use the preceding dual-interface notation: A=2m-1, a=1/2, b=A+1,
z=(A+71)/3, c=3^(h+1)/2, d=D+nu, w=m+1-nu and

    J={0,...,D-1} union{d,...,m},
    lambda=(nu repeated m-d+1 times, 0 repeated D times).

The original LOW x^u span differs from the LOW y^u span by a unitriangular
integer change; its Gram determinant is unchanged. For increasing exponents
e_i in J, e_i=i-1 on the LOW part and e_i=i-1+nu on the HIGH part. Therefore
the actual alternant is exactly V(y)s_lambda(y). Andreief proves

    det B_JJ=c^w J_w E[s_lambda(y)^2 prod_(i=1)^w(z-y_i)].      (5)

The expectation in(5) uses only the BASE Jacobi weight. The full linear pole
factor is retained inside the integrand. Because z>1, this expectation is
strictly positive, so no real singularity is introduced.

## 3. An explicit rational product-sum, with every divisor displayed

Let c_(lambda,lambda)^kappa be the usual nonnegative integer Schur product
coefficient. Write mu/kappa vertical-j-strip for adding j boxes with at most
one box in each row. The ordinary Schur product and Pieri identities yield

    C_J(z):=E[s_lambda^2 prod(z-y_i)]
      =sum_(j=0)^w (-1)^j z^(w-j)
         sum_kappa c_(lambda,lambda)^kappa
          sum_(mu/kappa vertical j-strip, length(mu)<=w)
            s_mu(1^w) prod_(i=1)^w
              (a+w-i)_(mu_i)/(a+b+2w-i-1)_(mu_i).             (6)

This is a FINITE rational sum specified by the original integer parameters,
not an infinite asymptotic extension. It has positive beta-product summands
but alternating z coefficients. Formula(6) does not establish a 3-adic unit:
cancellation between its paid rational summands must still be evaluated.
In particular z has negative ternary valuation in the original subwindow;
asserting dominance of its leading power requires actual valuation bounds
on the other coefficients, which have not been proved.

The largest individual compact power in any expanded alternant term is at
most2m+1: mu_1<=2nu+1 and mu_1+2(w-1)<=2m+1. Its beta products therefore
use no pole beyond2(A+2m+1)+1=8m+1=4n-3, the original physical cutoff.
Rational expansion denominators are retained in(6), not declared new global
clearers.

## 4. Exact pole Schur determinant, and the remaining inverse direction

The full Gram determinant for c(z-y)dmu_0 is the Christoffel identity

    det B=c^(m+1) J_(m+1) p_(m+1)(z).                        (7)

The monic norm product from the dual-interface note proves it directly:
prod_(r=0)^m H_r=c^(m+1)prod h_r *prod[p_(r+1)(z)/p_r(z)].
The last quotient telescopes because p_0=1, and prod h_r=J_(m+1).
Thus the ACTUAL pole Schur determinant of the same W is

    det S_P=c^nu J_(m+1) p_(m+1)(z)/[J_w C_J(z)].             (8)

Every scalar denominator and extracted factor in(8) remains present. The
kernel note gives the exact terminal-direction formula v^T M^(-1)T/H_m.
Formula(8) alone does not bound that inverse direction or the denominator
H_m+theta in its rank-one form.

An arithmetic next step would evaluate the ternary leading balance of(6)
and the corresponding endpoint-adapted minors on the SAME original index
progression, including all correction returns. No computation with an
astronomical original m is requested. A finite representation, positivity,
and classical gamma products do not establish the relative cofactor gain
or whole primitive error decay needed to decide e+pi.
