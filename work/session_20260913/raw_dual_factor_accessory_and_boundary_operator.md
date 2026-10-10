> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Both ends of the actual factor, bounded accessories, and an analytic boundary operator

Date: 2026-09-13. Original continuation by audit_computations.
Independent review: PASS by audit_sources; see raw_dual_factor_boundary_independent_review.md. This note continues the uniform Hardy
factor theorem, whose proof is saved separately in
raw_actual_dual_hardy_factor_allocation.md. All statements concern
the actual even family n=2m>=2. No new degree is constructed.

## 1. Reversal controls the other end of the polynomial

Retain F(z)=Phi_m^*(-z^2), v_0=v(0), and C_*=e sec(1).
The Hardy factor theorem gives

    ||v/(v_0F)||_(H^2)<=C_*.

Define reversal with respect to the full degree n even when v has
a degree defect:

    v^*(z)=z^n conjugate(v(1/conjugate(z))),
    Rtilde_n(z)=v^*(z)/(v_0 F(z)).                         (1)

On the unit circle |v^*|=|v|. The exact positive-measure replacement
applies to both degree-at-most-n polynomials, so

    ||Rtilde_n||_(H^2)=||v/(v_0F)||_(H^2)<=C_*.

Write Rtilde_n=sum_(j>=0)alpha_(n,j)z^j. Then

    sum_j |alpha_(n,j)|^2<=C_*^2.                        (2)

Since F(z)=1-(n/4)z^2+O(z^4), the three final polynomial
coefficients are exactly

    v_n/v_0=alpha_0,
    v_(n-1)/v_0=alpha_1,
    v_(n-2)/v_0=alpha_2-(n/4)alpha_0.                    (3)

Here alpha_j abbreviates alpha_(n,j). The definitions and (3)
remain valid when v_n or v_(n-1) vanishes. In particular no lower
bound on alpha_0 has been established.

## 2. Exact quadratic coefficients and a proved scaling

The two-function Padé note defines C(z)=z^nB(1/z), with
B(z)=1+b_1z+b_2z^2+..., and the quadratic K by

    D(Cv'-C'v)+(D+2nz)Cv=z^(2n)K,
    D=1+z^2,             K=K_0+K_1z+K_2z^2.             (4)

Coefficients absent because of degree drops are zero. Expanding
the three highest coefficients in (4), with C monic, gives

    K_2=v_n,
    K_1=v_(n-1)+(b_1+2n)v_n,
    K_0=v_(n-2)+(b_1+2n-1)v_(n-1)
                    +[b_2+(2n+1)b_1+1]v_n.             (5)

For the derivative term, the degree-(2n-1) coefficient of
Cv'-C'v cancels exactly, and the next coefficient is
b_1v_n-v_(n-1). This accounts for the -1 and the extra b_1
in the last line; omitting that cancellation gives incorrect
accessory coefficients.

Substitution of (3) yields

    K_2/v_0=alpha_0,
    K_1/v_0=alpha_1+(2n+b_1)alpha_0,
    K_0/v_0=alpha_2+(2n-1+b_1)alpha_1
       +[b_2+(2n+1)b_1+1-n/4]alpha_0.                  (6)

The already proved first two prediction bounds give, with the
safe constant C_p=e^2/cos(1),

    |b_1|<=C_p,
    |b_2|<=C_p(m+2)/2=C_p(n/4+1).                        (7)

Together with (2), these establish all-index bounds

    |K_2|/v_0<=C_*,
    |K_1|/v_0<=C_*[1+2n+C_p],
    |K_0|/v_0<=C_*[2n+2+C_p+C_p(n/4+1)
                              +(2n+1)C_p+n/4].           (8)

In particular K/(nv_0) is coefficientwise bounded, and its
quadratic coefficient tends to zero. Every subsequence has a
further coefficientwise-convergent subsequence with a polynomial
limit of degree at most one. That limit may be zero: neither
nonvanishing nor a lower bound for a leading accessory has been
proved by this compactness argument. Thus it is not legitimate
to divide a limiting differential equation by that polynomial
without additional information.

## 3. Exact finite model space and the actual normalized equation

Let

    S_n={p/F: deg p<=n} subset H^2.

The positive-measure replacement proves that p ->p/F identifies
the original degree-n polynomial inner product, multiplied by c_m,
with the Hardy inner product on S_n. The constant one belongs to
S_n because F has degree n. Define the actual compressed operator
T_mu on S_n by

    <T_mu(p/F),q/F>_(H^2)
         =c_m integral exp(z)p(z)conjugate(q(z)) dmu(z),   (9)
    dmu=|1+z^2|^(2m)dtheta/(2pi).

Its norm is at most e. Its real part is at least e^(-1)I,
by the same pointwise estimate used in the Hardy theorem. In
particular it is invertible with inverse norm at most e.
The ACTUAL normalized factor R_n=v/(v_0F) satisfies exactly

    T_mu R_n=(c_m/v_0)1,             R_n(0)=1.            (10)

The scalar c_m/v_0 is not dropped from (10).

For comparison define

    T_nu=P_(S_n) M_(exp z)|_(S_n),
    dnu=H_m |F|^(-2)dtheta/(2pi),
    E_n=T_mu-T_nu.                                       (11)

The space S_n is invariant under the backward shift: if p/F is
in S_n, then ((p/F)-p(0))/z=(p-p(0)F)/(zF) remains in S_n.
Hence S_n perpendicular is invariant under the forward shift.
For S_b=P_(S_n)M_z|_(S_n), this proves

    T_nu=exp(S_b),      T_nu^(-1)=exp(-S_b),
    ||T_nu||,||T_nu^(-1)||<=e.                            (12)

Thus the unresolved normalized factor is governed by the exact
equation

    [I+exp(-S_b)E_n]R_n
       =(c_m/v_0) P_(S_n)exp(-z).                        (13)

Equation (13) retains an explicit boundary correction E_n. It
does not replace the actual coupled equations by the comparison
measure's equations.

## 4. Uniform factorial approximation by finite-rank corrections

Let e_t(z)=sum_(j=0)^t z^j/j! and let E_n^[t] denote the
difference of the two compressed multiplication operators with
exp(z) replaced by e_t(z). For every t>=0,

    ||E_n-E_n^[t]||<=2e/(t+1)!.                          (14)

Indeed the scalar remainder on the circle is bounded by
e/(t+1)!; both positive-measure multiplication compressions have
operator norm at most the scalar supremum, and their polynomial
norms are exactly identified by (5) of the preceding note.
There is no factor depending exponentially on n in (14).

The original and replacement measures match through moments
from -n to n. They are also both invariant under z ->-z, so
their moments at the two odd exponents +/-(n+1) vanish. For
t>=1, if q is divisible by z^(t-1) and deg q<=n, every Laurent
power in e_t p conjugate(q) lies between -n and n+1. Thus
the difference pairing is zero for all such q. Consequently

    rank E_n^[t]<=min(max(t-1,0),n+1).                    (15)

For t=0,1 the correction is exactly zero. When t-1>n the
rank assertion is only the trivial full dimension bound.
For t-1<=n, its range lies in the orthogonal complement of

    {z^(t-1)p/F: deg p<=n-t+1},

an explicitly specified space of dimension t-1. It is a span
of the first t-1 coefficient-evaluation kernels at the origin.
This is a uniform finite-rank approximation of the actual
correction, not a claim that the correction tends to zero.

For example, the singular values obey the valid uniform estimate

    s_(t+1)(E_n)<=2e/(t+2)!,

whenever the stated singular value exists: use the degree-(t+1)
approximation, whose rank is at most t.

## 5. The first surviving correction is explicit and nonzero

The difference for multiplication by z^2 is exactly rank one.
Write Psi=(-1)^m Phi_m(-z^2) as before and put a_m=m/(2m+1).
The next circular-binomial recurrence gives

    Psi_(n+2)=z^2 Psi+(-1)^(m+1)a_m F,

where Psi_(n+2) is the monic degree-(n+2) orthogonal polynomial
for the ORIGINAL measure mu. It follows that projection of
z^2 Psi onto its degree-n polynomial space is (-1)^m a_m F.
Under nu the corresponding projection is zero: for deg q<=n,

    integral z^2 Psi conjugate(q)dnu
       =H_m integral z^(n+2)conjugate(q)/F=0.

For general p, subtract p_n Psi. The remaining polynomial has
degree at most n-1, so the moment agreement through n+1 makes
its difference pairing zero. Therefore

    E_(z^2)(p/F)=(-1)^m a_m p_n 1.                       (16)

The functional p/F ->p_n has norm exactly one. Indeed

    p_n=<p/F,Psi/F>_(H^2),       ||Psi/F||_(H^2)=1.

Thus ||E_(z^2)||=a_m ->1/2. The degree-two exponential
correction is E_n^[2]=E_(z^2)/2, not zero. This does not prove
a positive lower bound on ||E_n||, because the higher Taylor
terms could interact. It does prove that simply suppressing
the boundary correction on the basis of growing dimension is
not a justified derivation of an exp(-z) limit for R_n.

## 6. What a limit theorem now requires

Both R_n and Rtilde_n belong to a fixed Hardy ball, so they have
locally uniform subsequential analytic limits, after passing to
a common subsequence. The limit of R_n has value one at zero.
Its uniformly controlled root allocation and fixed-disk phase
were proved in the preceding note. They do not identify that
limit on their own.

Equations (13)-(16) give a concrete finite-data route: determine
the limits of each fixed-degree boundary correction together
with the finite model-space coefficient kernels, then use the
uniform factorial tail (14) to pass to the complete operator.
The explicit circular-binomial recurrence supplies the needed
finite boundary coefficients; identifying and inverting the
resulting limiting operator remains to be carried out. The
rank-one term (16) must be included in such a limit.

Even an interior limit of R_n would still need a justified passage
through the exact left-semicircle functional in (23)-(26) of
raw_actual_dual_hardy_factor_allocation.md. Its kernel depends
on n and the endpoints lie on the unit circle. The Hardy bound
is a useful uniform input, not by itself an estimate of that
signed, growing-kernel pairing. The original endpoint gcd also
remains unchanged.
