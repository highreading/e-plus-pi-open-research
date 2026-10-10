> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Fresh review of the mixed-cubic analytic inputs

Status: a review of specified auxiliary inputs, not a proof of irrationality
of e+pi. No main-objective termination condition has been met.

## Scope and independence

The root read the complete mathematical text of:

- `sources/mixed_cubic_boundary_cartier_content_and_recurrence.md`;
- `sources/mixed_cubic_accessible_saddle_exact_algebraic_certificate.md`;
- `sources/mixed_cubic_fixed_circle_complex_laplace_theorem.md`.

The principal matching correction was separately recovered from
`sources/mixed_cubic_matching_factor_two_and_classification_barrier.md`.
The review below checks the logical chain, with a new exact certificate for
the selected saddle. It does not label the entire archive independently
verified.

`check_saddle_independent.py` imports no archived mathematical routine and
requires no symbolic package. It constructs the angular polynomial directly
from the phase modulus and uses outward-rounded 192-bit dyadic intervals.
Its polynomial identities use exact rational arithmetic modulo the sextic.
The results are in `saddle_independent_checks.json`. This is a second route
to the requisite signs, not a byte replay of the earlier discriminant
certificate.

## 1. The residue determinant and its cancellation

Write



$$
H_s=\int_0^1\frac{[x(1-x)]^{6m}}{[(1+x)(1+x^2)]^{4m+1+s}}\,dx
 =R_s+\frac{L_s}4\log2+\frac{E_s}8\pi,
$$



and



$$
A=L_1R_0-L_0R_1,\qquad
B=\frac{L_1E_0-L_0E_1}{8}.
$$



Then the exact identity is



$$
A+B\pi=L_1H_0-L_0H_1.
$$



The term in log 2 cancels identically, without an independence assumption
on logarithms. The involution x=(1-y)/(1+y) transforms the integral to



$$
2^{-2m-1-2s}\int_0^1
\frac{y^{6m}(1-y)^{6m}(1+y)^{1+3s}}
{(1+y^2)^{4m+1+s}}\,dy.
$$



If c_s denotes its residue at i, the partial-fraction normalization is
L_s=4 Re c_s and E_s=-4 Im c_s. Hence
B=2 Im(c_1 conjugate(c_0)). This sign is material.

With the archive's phase and amplitudes,



$$
\Psi(v)=\frac{(1+2v)^6(1+(1-i)v)^6}{v^4(1+v)^4},\qquad
b_0(v)=\frac{1+(1+i)v}{1+v},
$$



write c_j=C_m I_j, where
I_j=(2 pi i)^{-1} integral Psi(v)^m b_j(v) dv/v and
|C_m|^2=2^{-14m-3}. The rational identity



$$
r(v)-\frac58=h(v)\frac{\Psi'(v)}{\Psi(v)},\qquad
h(v)=\frac{-1+i}{32}(1+2v)(1+(1-i)v)
$$



with b_1=b_0 r, followed by integration of a derivative around the closed
circle, gives



$$
I_1-\frac58I_0=\frac1m I_2,\quad
b_2=-v\frac{d}{dv}\left(\frac{b_0h}{v}\right)
=\frac{(1-i)(4v^4+8v^3+2v^2-2v-1)}{32v(1+v)^2}.
$$



This is an exact cancellation before taking any asymptotic expansion. In
particular,



$$
B=\frac{2|C_m|^2}{m}\operatorname{Im}(I_2\overline{I_0}).
$$



Using a leading saddle term for I_1 and I_0 directly would miss the real
leading ratio 5/8; the integration-by-parts step is essential.

## 2. Independent exact selection of the accessible saddle

Let alpha be the unique root in the squared interval below of



$$
g(a)=128a^6-384a^5+280a^4-20a^3-55a^2+a+2.
$$



Put rho=sqrt(alpha), with



$$
\frac{458133387942745}{10^{15}}<\rho<
\frac{458133387942746}{10^{15}}<\frac12.
$$



Exact rational endpoint evaluations give opposite signs of g, and an
interval evaluation of g' is strictly negative there. Define



$$
x=-\frac{(4a+1)(16a^4-52a^3+49a^2-18a+1)}5,
\quad
y=\frac{64a^5-208a^4+196a^3-67a^2-11a+5}5.
$$



Polynomial reduction modulo g independently gives x^2+y^2=a and



$$
S(x+iy)=0,\qquad S(v)=4v^3+(6-i)v^2-iv-1-i.
$$



Since Psi'/Psi=(2-2i)S/[v(1+v)(1+2v)(1+(1-i)v)],
tau=x+i y is a genuine stationary point. All denominator factors are
nonzero on a thin annulus about this circle; the nearest zero of Psi has
modulus 1/2, strictly larger than rho.

For a direct angular check, set q=tan(theta/2). After cancelling the
common factor 1+q^2, define the quadratic polynomials



$$
\begin{aligned}
\mathsf A&=(1+2R)^2+(1-2R)^2q^2,\\
\mathsf B&=1+2R+2R^2+4Rq+(1-2R+2R^2)q^2,\\
\mathsf C&=(1+R)^2+(1-R)^2q^2.
\end{aligned}
$$



The angular logarithmic derivative has the opposite sign to



$$
P_R(q)=12q\mathsf B\mathsf C
-3(1-2q-q^2)\mathsf A\mathsf C-4q\mathsf A\mathsf B.
$$



This polynomial was constructed from the derivative, not copied from the
archive's coefficient list. Its degree is six, with positive leading
coefficient 3(R-1)^2(2R-1)^2. Exact interval Euclidean division, uniformly
over the displayed radius interval, produces a full Sturm chain of
degrees 6,5,4,3,2,1,0. The signs at minus infinity are
(+,-,+,-,-,-,+), and at plus infinity (+,+,+,+,-,+,+).
There are therefore exactly two real angular critical points.

The polynomial signs at -282,-281,11/40,69/250 are (+,-,-,+), and
y/(rho+x) lies strictly between 11/40 and 69/250. Thus tau is the
unique angular maximum, while the other root is the minimum. The seam
theta=pi is not a critical point because the leading angular coefficient
is nonzero. Compactness then gives a strictly smaller maximum outside
any sufficiently small arc around tau.

The same exact intervals certify Re(lambda)>2 for
lambda=tau^2 (log Psi)''(tau), and
Im(b_2(tau)/b_0(tau))>0. The latter was evaluated directly as a complex
rational expression, without using the archive's reduced amplitude
formula. These signs imply a nondegenerate saddle and a positive
determinant amplitude.

## 3. The local asymptotic argument

Parameterize the circle near tau by v=tau exp(iu). The first derivative
vanishes and the second derivative of log Psi along u is -lambda.
A local logarithm exists because Psi has no zero there. Re(lambda)>0
gives Gaussian decay on a sufficiently small real arc.

For the stated remainder O(1/m), use |u|<=m^{-2/5} and put t=sqrt(m)u.
Then |t|<=m^{1/10}. Taylor expansion of the analytic phase and amplitude
gives a leading Gaussian and an order m^{-1/2} odd polynomial times
that Gaussian. The odd term integrates to zero over the symmetric
interval. Taylor remainders are bounded by a fixed polynomial in t times
an integrable smaller Gaussian, yielding O(1/m). The portion between
m^{-2/5} and a fixed small arc decays like exp(-c m^{1/5}); the remaining
circle has a fixed exponential gap. These estimates justify extending
the Gaussian integral to the real line and give



$$
I_j=\frac{\Psi(\tau)^m}{\sqrt{2\pi m}\sqrt\lambda}
\left(b_j(\tau)+O(m^{-1})\right),\qquad j=0,2.
$$



The square root is the branch with positive real part. In the product
I_2 conjugate(I_0), the possibly oscillating phase Psi(tau)^m cancels.
Consequently



$$
B_m=\frac{2^{-14m-3}|\Psi(\tau)|^{2m}}
{\pi m^2|\lambda|}
\left(\operatorname{Im}(b_2(\tau)\overline{b_0(\tau)})
+O(m^{-1})\right)>0
$$



for all sufficiently large m. There is no need to select a phase-favorable
subsequence for B. Nonzero real or imaginary parts of an individual
residue were not assumed.

## 4. Clearing, content, and exponents

The boundary report's clearing argument is logically separate from the
saddle proof. Its rational partial fractions give the integer clearer
D=2^{9m+5} lcm(1,...,4m+1). A rank-one Cartier argument saves the middle
prime band 2m<p<3m. The exact-differential test over F_p supplies the
squarefree content product from the stated degree condition. The middle
band and that support are disjoint, so those savings can be combined.
The all-prime support asymptotic follows from finitely many prime-number-
theorem intervals followed by a Chebyshev tail bound. None of these
steps implies independently distributed higher prime powers.

This review read those arguments and found no new logical correction in
their stated scope. It did not independently reconstruct every partial-
fraction identity or promote the work-only higher-digit drafts.

Define



$$
\ell=\frac{\log|\Psi(\tau)|-7\log2}{6},\qquad
\phi=\max_{0<x<1}\left(\log x+\log(1-x)-\frac23\log Q(x)\right).
$$



The determinant asymptotic gives log|B_m|/(6m)->2 ell. The integral
identity gives only an error upper bound with exponent ell+phi; equality
is not needed or claimed. Including the certified clearer/content
factor yields



$$
\frac{\log|V_m|}{6m}\to h,\qquad
\limsup\frac{\log|U_m+V_m\pi|}{6m}\le h-d,
$$



where d=ell-phi and h is the archived coefficient exponent. Because
V_m is a nonzero integer eventually and pi is irrational, the raw pi
form is also nonzero. This is an allowed use of known irrationality of
pi; it does not assume anything about e+pi.

The early boundary report's statement that d>h is enough after matching
is superseded by the archive's factor-two correction. Matching to the
beta forms introduces both coefficient scales. The sufficient optimized
gain threshold is h-d/2, not h-d. This audit supplies no additional
content to reach that threshold.
