> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact two-mode factorization and bounded boundary matrices for odd degrees

Date: 2026-09-13. Original bounded continuation by audit_results.
Independent review: FULL PASS by audit_sources; see raw_odd_exact_two_mode_independent_review.md.

This sharpens the independently passed five-mode parametrix theorem without a higher Taylor approximation. At the fixed exponential parameter 1, the actual normalized odd Toeplitz matrix is a uniformly invertible product plus a rank-at-most-two correction. Its exact scalar s_m is a ratio of determinants of explicitly specified 2 by 2 and 3 by 3 matrices, all of whose entries have uniform bounds. Nonvanishing is proved by the previous actual-family theorems; quantitative lower bounds for these boundary determinants remain open.

## 1. Spaces, domains, and the exact factorization

Use the notation of raw_odd_toeplitz_five_mode_boundary_reduction.md:

    n=2m+1, N=2m+2,
    H=L^2(circle, |1+t|^(2m+2)dtheta/(2pi); C^2),
    P_m={(u,v): degree u,degree v<=m},
    P=orthogonal projection onto P_m.

In the scalar version of the same space write P_s for its polynomial projection. Define, on the unit circle,

    J(t)=[ 0 t ],             a0(t)=[ 0       t/(1+t) ],
         [ 1 0 ]                    [ 1/(1+t)       0 ],
    E(t)=exp J(t)=[ c(t) t s(t) ],
                 [ s(t) c(t)   ].

Then J is unitary and normal, with eigenvalues z,-z for either square root z of t. Hence

    ||E||<=e,       Re E>=c_* I,       c_*=e^(-1)cos(1)>0.    (1)

The rational multiplier a0 is selfadjoint almost everywhere, commutes with E, and

    a=a0 E=E a0

is exactly the actual parity symbol from the preceding note.

Although a0 is unbounded on H, it maps P_m into H. It also maps E P_m into H: the only possible singularity is a simple pole at -1, and the weight makes its square integrable even for m=0. The finite map a0 P is bounded. From the independently proved weight comparison I_m<=5 I_(m+1)/4,

    ||a0 P||<=sqrt(5/4).                                   (2)

When P a0 is applied beyond its original domain below, it means the bounded adjoint (a0 P)*. On the domain just described this agrees with multiplication followed by projection.

Set

    A=P a P,        A0=P a0 P,        E0=P E P

as operators on P_m. The operator A is unitarily equivalent to the actual normalized Atilde. By (1), E0 is invertible and

    ||E0^(-1)||<=1/c_*.

Let K=P_s[t/(1+t)]P_s. Then

    A0=[0 K; K* 0],       K+K*=I.

Thus ||K u||>=||u||/2 and, in finite dimension,

    ||A0^(-1)||<=2.                                         (3)

The base product T=A0 E0 is therefore invertible with

    Q=T^(-1),       ||Q||<=K0:=2/c_* .                      (4)

No assertion of positive definiteness for A or A0 is made.

## 2. Two exact boundary functionals

Let

    r(t)=1/(1+t),       h=(I-P_s)r,       rho=||h||>0,
    ell(u)=u(-1),       Lambda(u,v)=rho(ell(u),ell(v)).

The strict positivity of rho follows because r cannot agree almost everywhere with a polynomial. Let Hhat:C^2->H be the isometry

    Hhat(alpha,beta)=rho^(-1)h(t)(alpha,beta),
    J0=[0 -1; 1 0].

Polynomial division gives the EXACT identity

    (I-P)a0 P=Hhat J0 Lambda.                              (5)

Indeed t v/(1+t)=v-v/(1+t) contributes -ell(v)h in the first component, while u/(1+t) contributes ell(u)h in the second. Equation (2), together with the isometry Hhat J0, shows

    ||Lambda||<=sqrt(5/4).                                 (6)

Put

    W=Hhat* E P,       U=Lambda*,       V=J0* W.

Then ||U||<=sqrt(5/4), ||V||<=e. Taking the bounded adjoint of (5) in the cross term proves

    A=A0 E0+P a0(I-P)E P=T+U V.                            (7)

This is an exact rank-at-most-two correction. It contains the whole exponential multiplier, not a truncated series.

## 3. Uniform singular values outside two or three modes

Multiplying (7) by Q gives A Q=I+UVQ. On the kernel of VQ, whose codimension is at most two, this is the identity. The min-max principle and s_j(AQ)<=||Q||s_j(A) yield

    s_(N-2)(A)>=sigma_0:=1/K0=c_*/2,       N>2.             (8)

Singular values are in decreasing order. Thus at most two of them can be below sigma_0.

Retain the actual unit vector v, Pi=I-vv*, and high compression B=Pi A|_(v-perp) from the odd scalar note. With Q_B=Pi Q|_(v-perp),

    B Q_B=I+Pi UVQ Pi-Pi A v v*Q Pi.                       (9)

The correction has rank at most three and ||Q_B||<=K0. Therefore

    s_(N-4)(B)>=sigma_0,       N>4,                         (10)

so at most three singular values of B can be small. The statements at smaller dimensions are understood as counts.

Both A and B are already proved invertible for the actual family. Equations (8)-(10) supply quantitative information only outside the indicated exceptional modes.

## 4. The actual scalar is an exact bounded-size determinant ratio

Define the 2 by 2 and 3 by 3 matrices

    D2=I_2+V Q U,

    D3=[ D2        V Q v ],
       [ v*Q U     v*Q v ].                               (11)

Every entry of these matrices is uniformly bounded in m by (4), (6), and ||V||<=e. The vector v is precisely the normalized original endpoint-coordinate vector; it has not been replaced by a boundary evaluation at -1.

The determinant lemma gives det A=det T det D2. Since A is invertible, D2 is invertible, and the exact Woodbury formula gives

    A^(-1)=Q-Q U D2^(-1)V Q.

The scalar Schur complement of D2 in D3 is consequently v*A^(-1)v. The proved odd normalization says this is 1/s_m. Hence

    det D3=det D2/s_m,
    det B=det T det D3,
    s_m=det D2/det D3.                                    (12)

The second identity also follows from det B=det A(v*A^(-1)v). In particular D3 is invertible because the actual B is invertible. The signs and the order of factors in (11) are required for the minus sign in Woodbury; the lower-left block is positive v*Q U.

This yields an exact remaining target with no dimension-dependent exterior normalization:

    log|det D2|-log|det D3|=o(m).                           (13)

It is equivalent to the desired odd scalar estimate log|s_m|=o(m). The uniform upper bounds for D2,D3 do not give lower bounds for either determinant.

For the full inverse, (7) also supplies the explicit conditional estimate

    ||A^(-1)||<=K0+K0^2 sqrt(5/4)e ||D2^(-1)||.             (14)

No bound for D2^(-1) has yet been proved.

## 5. Relation to the five-mode result and scope

The five-mode proof and its independent review remain correct. The exact factorization (7) improves the exceptional counts to two and three, and (11)-(12) identify actual bounded-size matrices rather than only singular-value products. It uses the rational pole at -1 and the accretive exponential factor, not the indefinite Hermitian gap.

The remaining task is genuinely a boundary estimate: compute or estimate (11), keeping the m-dependent positive polynomial projection, endpoint vector v, and normalized residual h. Replacing these by an unjustified limiting projection would not prove (13).

All arguments are at exponential parameter 1 and all identities retain the actual dimension 2m+2. No new canonical degree, root, or singular-value sample was constructed.
