> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact dual-coefficient interface for the original LOW/HIGH projection

Coordinator derivation, 8 October 2026. This is a classical finite kernel and
block-inverse interface for the ACTUAL pole projection. It evaluates its input
entries and terminal row by finite rational formulas; it does not evaluate the
remaining middle-block inverse or prove a new growing ternary saving. External
independent review is still required.

## Scoped overlap and primary-source gate

The complete A1turn0, A1turn1 and original A1turn18 have been read in this round.
A scoped search in archive sources and the complete 20261007 Markdown response
files for full-Gram/Jacobi-inverse/middle-monomial/dual-coefficient expressions
found no evaluated same-W directional formula. An earlier search accidentally
included JSON single-line reports and its output was truncated; that output is
not treated as a complete reading. Only the explicit Markdown-scoped search
is used here. Classical identities are reused, with no global novelty claim.

The standard kernel modification outside the support is given in
[DLMF18.2](https://dlmf.nist.gov/18.2#v); the finite Jacobi expansion is in
[DLMF18.5](https://dlmf.nist.gov/18.5#iii). Their parameter hypotheses hold here.
The derivation below retains the original omitted monomial window; an
orthogonal basis is used only to evaluate the FULL inverse kernel.

## 1. Original finite pole Gram and its exact moments

Retain j=84645 modulo531441, m=2^(2j-1), n=2m+1, A=2m-1,
beta=-A-71, x=y-1, and the original h,D,nu,d=D+nu. Define the pole form

    P(f,g)=3^h sum_(v=0)^(2n-2)
                    [y^v] x^A(beta+3y) f(y)g(y)/(2v+1).

For deg f,deg g<=m, the polynomial in this sum has degree at most
A+1+2m=4m=2n-2. The EXACT integral identity is

    P(f,g)=(3^h/2) int_0^1 y^(-1/2)(1-y)^A(A+71-3y)f(y)g(y)dy.

Set z=(A+71)/3>1 and c=3^(h+1)/2. This is the positive measure

    dmu_P=c(z-y)dmu_0,  dmu_0=y^(-1/2)(1-y)^A dy.

Let B=(P(y^r,y^s))_(0<=r,s<=m). Its entries are finite rational quantities:

    I_A(u)=int_0^1 t^(2u)(1-t^2)^A dt
          =2^A A! / prod_(v=0)^A(2u+2v+1),
    B_rs=3^h(-1)^A[beta I_A(r+s)+3 I_A(r+s+1)].                 (1)

The largest denominator in the second product at r+s=2m is
2(2m+1+A)+1=8m+1=4n-3, exactly the physical finite pole cutoff. No successor
moment is introduced. The complete Q_c includes its additional y+1 factor
and has degree at most2n-1, its own already accepted boundary.

## 2. Full inverse kernel and the actual scalar normalizations

For r>=0 let p_r be the monic polynomial orthogonal for mu_0 and h_r its norm.
All coefficients and norms are rational. One explicit form is

    ell_r=binom(2r+A-1/2,r),
    p_r(y)=ell_r^(-1) sum_(j=0)^r
                 binom(r+A,j)binom(r-1/2,r-j)(y-1)^(r-j)y^j,
    h_r=(r+1)_A / [(r+1/2)_A(2r+A+1/2)ell_r^2].                (2)

Here generalized binomials and Pochhammer symbols are finite rational
products. Formula(2) is the usual shifted Jacobi normalization with parameters
(A,-1/2), both greater than-1. It can also be verified from Rodrigues' formula
and the beta integral(1). Its leading coefficient is one; the denominator
ell_r and the full norm h_r are explicitly retained.

Since every zero of p_r lies in(0,1), p_r(z)>0. Define

    a_r=p_(r+1)(z)/p_r(z),
    q_r(y)=[p_(r+1)(y)-a_r p_r(y)]/(y-z),
    H_r=c a_r h_r.                                           (3)

The numerator vanishes at z, so the quotient is exactly a polynomial, monic
of degree r. For deg u<r, base orthogonality gives

    int q_r u dmu_P
       =c int[-p_(r+1)+a_r p_r]u dmu_0=0.

Also int q_r p_(r+1)dmu_0=0 and int q_r p_r dmu_0=h_r, hence

    int q_r^2 dmu_P=c a_r h_r=H_r>0.                          (4)

Writing v_r for the coefficient column of q_r in degrees0..m, the exact FULL
inverse is therefore

    B^(-1)=sum_(r=0)^m v_r v_r^T/H_r.                        (5)

Proof: the unitriangular matrix of monic orthogonal coefficients diagonalizes
B with diagonal H_r. Formula(5) follows by multiplying that exact identity.
Equivalently its bivariate coefficient kernel is the finite reproducing
kernel. Each p_r(z), ell_r, h_r and H_r division in(2)--(5) is part of the
explicit rational normalization; none is assumed to be a ternary unit.

The temporary p_(m+1) in(3) is a classical closed polynomial formula defining
q_m. Verifying q_m orthogonality and(4) requires integrals of degree at most2m
under mu_P and degree at most2m+1 under mu_0. The resulting highest beta pole
is8m+1, still the original physical cutoff. This introduces no complete-core
moment beyond2n-1.

## 3. The exact original omitted coefficient window

Let I={D,...,d-1}, J={0,...,D-1} union{d,...,m}. The actual W uses LOW x^u
for u<D and HIGH y^v for d<=v<=m. LOW x^u and LOW y^u differ by an integral
unitriangular transformation, so W is exactly the J coefficient subspace.
It is NOT a subspace of consecutive Jacobi degrees.

Let E_I denote inclusion of the I coordinates and

    M=E_I^T B^(-1)E_I.

It is positive definite. For the original middle columns z_i=x^D y^i,
0<=i<nu, their I coefficients form the exact upper unitriangular matrix

    T_ri=(-1)^(i-r)binom(D,i-r) if r<=i; otherwise0,
    det T=1.                                                 (6)

Its inverse has entries binom(D+i-r-1,i-r) for r<=i. In particular no
fractional change of middle basis is introduced.

Let X be the FULL coefficient matrix of their actual pole-corrected columns.
The middle coefficients are X_I=T, and orthogonality to W gives (BX)_J=0.
Thus BX=E_I Y for some Y, and multiplication by B^(-1) gives

    X=B^(-1)E_I M^(-1)T,
    S_P=X^T B X=T^T M^(-1)T.                                 (7)

This proves(7) for the exact selected projection rather than a replacement
orthogonal-degree projection. Jacobi's complementary-minor identity also
gives

    det S_P=1/det M=det B/det B_JJ.                           (8)

The LOW basis's determinant is one, so det B_JJ is the actual pole W Gram
determinant. All of det M, det B and det B_JJ are retained as rational factors.

## 4. Physical terminal row without a successor coefficient

Let v be the I coefficient column of the monic q_m. Only q_m contributes to
the y^m row of(5), since all preceding q_r have smaller degree. Therefore

    e_m^T B^(-1)E_I=v^T/H_m,
    [y^m] F_P=v^T M^(-1)T/H_m.                               (9)

For any original middle combination with coefficient column u, set a=Tu.
Its exact terminal amplitude and corrected pole norm are

    gamma_P(u)=v^T M^(-1)a/H_m,
    P(F_Pu,F_Pu)=a^T M^(-1)a.                                (10)

There is no omission of physicalY_m. The terminal amplitude vanishes exactly
when its displayed numerator vanishes, not because a trial column has no y^m
term.

An exact rank-one version is useful for identifying a possible resonance.
Put M_< =sum_(r=0)^(m-1) (v_r)_I(v_r)_I^T/H_r. Since max I=d-1<m,
the monic polynomials up to degree m-1 span every I coefficient direction;
M_< is positive definite. With theta=v^T M_<^(-1)v,

    gamma_P(u)=v^T M_<^(-1)a/(H_m+theta).                     (11)

This is Sherman--Morrison with its complete divisor H_m+theta. Real
positivity excludes a zero real denominator, but gives no bound on its
3-adic valuation. It must not be used to claim ternary nonresonance.

For completeness, M>=v v^T/H_m yields v^T M^(-1)v<=H_m. Cauchy--Schwarz
therefore proves the real coefficient estimate

    |gamma_P(u)|^2 <= P(F_Pu,F_Pu)/H_m.                       (12)

This is an exact real estimate, not an arithmetic divisibility statement.

## 5. Transfer scope and unresolved obligation

The accepted A1turn0 pole/complete comparison is reused:

    F_P-F_c in3^(h-1) W M,  S_P-S_c in3^h M.

It transfers the terminal row(9) to physical complete terminal coefficients
only modulo3^(h-1), and transfers(7) to corrected pairings only modulo3^h.
It does not identify the full evaluated real determinant with its pole form.
The original prefix/J/endpoint/diagonal/producer/rank-b returns still require
their original payments, followed by actual contents, least clearer, final
ALL-prime gcd, actual primitive denominator and nonzero whole error at the
same infinite indices.

The remaining arithmetic is now explicit: estimate the selected rational
kernel inverse M^(-1), or the paid quotient in(11), in the actual original
ternary direction and subwindow. Positivity, a finite closed entry formula,
and a named determinant are not such an estimate. No growing relative
saving or irrationality result is claimed here, and no astronomical dense
calculation is authorized by this note.
