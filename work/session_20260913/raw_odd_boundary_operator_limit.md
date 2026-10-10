> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A fixed half-line limit for the two odd boundary matrices

Date: 2026-09-13. Original bounded continuation by audit_results.
Independent review: PASS by audit_sources; see raw_odd_boundary_operator_limit_independent_review.md.

This continues raw_odd_exact_two_mode_boundary_matrices.md. It proves convergence of the actual bounded 2 by 2 and 3 by 3 boundary matrices to explicitly defined, fixed half-line operator data. It does not assert that the two limiting determinants are nonzero.

The new sufficient condition for the odd root-product theorem is therefore the nonvanishing of two fixed determinants, rather than an estimate for a growing family with unspecified normalization.

## 1. Cayley coordinates and the varying positive measure

Let n=2m+1. Put

    t=(1+iy)/(1-iy),       beta=2m+2.

The scalar polynomial map u(t)->(1-iy)^m u(t) identifies degree-at-most-m polynomials in the positive circle metric with degree-at-most-m polynomials in

    const_m (1+y^2)^(-beta)dy.

The scalar constant is positive and will cancel from all normalized vectors and recurrence coefficients. Let q_j^(m), 0<=j<=2m+1, be its orthonormal polynomials with positive leading coefficient. These degrees have finite squared norms. In the ranges used below multiplication by y obeys

    y q_j=a_(j+1,m)q_(j+1)+a_(j,m)q_(j-1),
    a_(j,m)^2=
       j(2beta-j)/[(2beta-2j)^2-1].                        (1)

This is the already checked Cauchy-weight Rodrigues norm ratio. The multiplication recurrence is used for 0<=j<=2m, so its q_(j+1) still has finite norm. Every fixed neighborhood of j=m lies within this valid range for large m.

For each fixed integer k,

    a_(m+k,m)->a_*:=sqrt(3)/2.                             (2)

For j<=m+1 the coefficients are at most one. Thus the compressed multiplication matrix on degrees 0,...,m has norm at most two, uniformly.

In the two components the rational factor becomes particularly simple:

    a0(y)=1/2 [ 0       1+iy ],
                [ 1-iy     0 ].

Write

    Jb=[0 i; -i 0],       Jb*=Jb,       Jb^2=I.

The bounded exponential multiplier is the continuous matrix function

    F(y)=exp [0 t(y); 1 0].                               (3)

It has norm at most e and Hermitian part at least c_*I, c_*=e^(-1)cos(1), for every real y. Its finite limit as |y| tends to infinity also exists. The multiplication operator y is unbounded on the full weighted space; no boundedness of that full operator is assumed.

## 2. The exact finite boundary maps in these coordinates

Reverse the polynomial indices: q_(m-r) is placed at position r, 0<=r<=m. Let P_m now denote the corresponding two-component polynomial compression. Let e_m:P_m->C^2 extract position zero, namely the original top polynomial coefficient.

Multiplication by a0 loses exactly one polynomial degree, so

    (I-P_m)a0 P_m
       =gamma_m iota_(m+1) Jb e_m,
    gamma_m=a_(m+1,m)/2 ->sqrt(3)/4,                       (4)

where iota_(m+1) inserts the two-component q_(m+1) vector into the full weighted space. This is the same rank-two correction as in the preceding note, with a harmless unitary change in its two-dimensional boundary coordinates.

Define

    A0_m=P_m a0 P_m,       E_m=P_m F P_m,
    T_m=A0_m E_m,          Q_m=T_m^(-1),
    U_m=gamma_m e_m*,
    W_m=iota_(m+1)* F P_m, V_m=Jb W_m.                    (5)

Then the actual normalized odd matrix is

    A_m=T_m+U_m V_m,
    ||Q_m||<=2/c_*.

The bounded-adjoint justification in the preceding note applies unchanged.

## 3. The actual endpoint vector has an explicit geometric limit

In Cayley coordinates the original functional u(0) is evaluation of the transformed polynomial at y=i, times the common scalar 2^(-m). Consequently its normalized Riesz vector has coefficients proportional to conjugate(q_j^(m)(i)) in the first component, and zero in the second.

Rodrigues gives the exact monic value

    Q_j(i)=(2i)^j (beta-j)_j/(2beta-2j)_j,

where rising factorials are used. Indeed after multiplying the Rodrigues derivative by (1+y^2)^beta, evaluation at y=i kills every Leibniz term except the one with all j derivatives on the factor (y-i)^(j-beta). Dividing by the leading coefficient gives the displayed formula.

Using (1), its orthonormal ratio is

    q_j(i)/q_(j-1)(i)
       =i sqrt[(2beta-j)(2beta-2j-1)/
                    (j(2beta-2j+1))].                    (6)

For 1<=j<=m, the magnitude in (6) is at least sqrt(3). One way to see this is that both factors

    (2beta-j)/j,       (2beta-2j-1)/(2beta-2j+1)

decrease with j. Their product at j=m is
(3m+4)(2m+3)/(m(2m+5))>3. For m=0 the vector consists of one coordinate.

After reversing indices and multiplying the unit vector by the harmless phase i^m, its r-th coordinate is i^r times a positive number. Equation (6) implies

    |v_(m,r)|<=3^(-r/2),       0<=r<=m,

and, for every fixed r, the ratio to coordinate zero tends (i/sqrt(3))^r. Normalization and the geometric dominating series therefore prove norm convergence

    v_m -> v_infty,
    v_infty(r)=sqrt(2/3)(i/sqrt(3))^r [1;0],
    r=0,1,... .                                           (7)

Changing the phase of v changes neither s_m nor the determinants below.

## 4. Local functional-calculus convergence without an invalid infinite Jacobi basis

Let J_infty be the bilateral constant Jacobi operator on ell^2(Z),

    J_infty e_r=a_*(e_(r-1)+e_(r+1)).

It is bounded and has spectrum [-sqrt(3),sqrt(3)]. Let P_+ project onto positions r>=0.

For every fixed finite set of reversed indices and every fixed polynomial p, recurrence (1) and (2) imply convergence of the matrix coefficients and squared norms of p(y) applied to those polynomial vectors to the corresponding quantities for p(J_infty). All involved polynomial degrees and moments exist for sufficiently large m.

This implies the same local convergence for any bounded continuous scalar f on R, and yields norm convergence after projecting onto r>=0. Here are the needed approximation details. For a fixed input vector, its spectral moments of each fixed order converge to those of the compactly supported limiting measure. Choose R>sqrt(3), and approximate f uniformly on [-R,R] by a polynomial p. Outside that interval, the squared error is bounded by a constant times 1+|y|^(2deg p). For any fixed integer L, the corresponding tail integrals are bounded by R^(-2L) times fixed higher moments. Taking m to infinity first and then L to infinity makes this tail arbitrarily small, since the limiting moments have support within [-sqrt(3),sqrt(3)].

Thus p may be chosen with arbitrarily small limiting upper L^2 error. Its action has fixed finite propagation and converges by (1)-(2), proving the asserted norm convergence. Projection can only decrease the error.

This argument applies entrywise to F and F*, which are bounded continuous. It does not identify the original full weighted space with an infinite orthogonal-polynomial Jacobi basis: only finitely many polynomial moments are used at each approximation stage.

Consequently, after reversing indices and extending the finite operators by identities outside positions 0,...,m,

    E_m -> E_+:=P_+ F(J_infty)P_+                         (8)

strongly, and their adjoints converge strongly as well. Here F(J_infty) denotes the two-component continuous matrix functional calculus. The extensions are only for strong convergence; they do not alter any finite determinant.

The compressed multiplication matrices similarly converge strongly to

    Y_+=P_+J_infty P_+,
    A0_+=1/2 [0 I+iY_+; I-iY_+ 0].                       (9)

Uniform boundedness follows from (1). The finite A0 operators may be extended outside their finite spaces by I/2 in each component, ensuring uniform invertibility of the extensions; their strong limit is still (9).

Both E_+ and A0_+ are invertible with the same bounds as the finite operators. For E_+ this follows from uniform strict accretivity, applied also to its adjoint; for A0_+ it follows from selfadjointness of Y_+ and invertibility of I+/-iY_+. The identity

    S_m^(-1)-S^(-1)=S_m^(-1)(S-S_m)S^(-1)

therefore proves strong convergence of both inverse families. In particular

    Q_m -> Q_+:=E_+^(-1)A0_+^(-1)                         (10)

strongly, with the uniform norm bound 2/c_*.

The same functional-calculus argument applied to the input at original degree m+1, or reversed position -1, gives

    W_m -> W_+:=iota_(-1)*F(J_infty)P_+                  (11)

in operator norm as maps into C^2. Indeed their adjoints are two columns, each converging in norm; finite output dimension then gives operator-norm convergence.

## 5. The limiting boundary matrices

Let e:P_+ell^2(Z;C^2)->C^2 extract position zero, and put

    U_+=(sqrt(3)/4)e*,       V_+=Jb W_+.

Define fixed matrices

    D2_+=I_2+V_+Q_+U_+,

    D3_+=[ D2_+            V_+Q_+v_infty ],
         [ v_infty*Q_+U_+  v_infty*Q_+v_infty ].            (12)

The corresponding finite formulas are exactly those of the preceding rank-two note, in the boundary coordinates (4). Equations (4), (7), and (10)-(11) imply

    D2_m -> D2_+,       D3_m -> D3_+                       (13)

in finite matrix norm. No determinant inversion is used in proving this convergence.

For a completely explicit description of the limiting operators, Fourier transformation sends J_infty to multiplication by sqrt(3)cos(theta). Hence E_+ is the half-line Toeplitz compression of

    F(sqrt(3)cos(theta)),

and W_+ consists of its coefficients from position -1 to positions 0,1,... . Its inverse exists by accretivity. These fixed operator data, together with (7), specify every entry of (12).

## 6. Exact scope of the new sufficient condition

All finite D2_m and D3_m are nonzero by the actual all-index A and B theorems. Their limits need not be nonzero merely for that reason.

If

    det D2_+ !=0 and det D3_+ !=0,                         (14)

then (13) and the exact scalar identity prove

    s_m -> det D2_+/det D3_+ !=0.

This implies log|s_m|=o(m) and therefore the desired absolute odd root-product limit 3sqrt(3)/e.

Condition (14) is not proved here. If either limiting determinant vanishes, convergence alone does not give the needed rate; a further expansion or an independent lower bound would be required. No quantitative convergence rate is asserted.

This note uses no new degree, prime, root, or singular-value sample. It obtains the actual boundary limit from exact Rodrigues values, fixed-degree moment convergence, bounded continuous multipliers, and uniform invertibility only of the known base factors.
