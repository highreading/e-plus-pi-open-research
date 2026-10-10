> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Finite-degree signed normalization of the paired derangement polynomial

Author theorem: Agent 3, 2026-10-02. Target, archive searches, and primary overlap are recorded in PAIRED_DERANGEMENT_ANALYTIC_GATE.md. The kernel formula is classical Uvarov theory; its application below is proved at each nonsingular degree because this particular functional is not globally quasi-definite.

Let D_m be the derangement numbers, let mu be the probability pushforward of exp(-t)dt on t>=0 by y=(1-t)^2, and let rho=mu-delta_{-1}. Then

    mu(y^r)=D_{2r},   rho(y^r)=D_{2r}-(-1)^r.

The density of mu on y>0 is

    [exp(-1-sqrt(y))+1_{y<1}exp(-1+sqrt(y))]/[2sqrt(y)].

This strictly positive measure has finite moments of every order. Let p_j be its monic orthogonal polynomials, h_j=mu(p_j^2)>0, and define the dimension-n kernel

    K_n(y,z)=sum_{j=0}^{n-1} p_j(y)p_j(z)/h_j.

The indexing here is deliberate: K_n reproduces polynomials of degree less than n.

## Existence and inertia

The n by n moment matrices M_mu,n and M_rho,n satisfy

    M_rho,n=M_mu,n-v_n v_n^T,   v_n=(1,-1,...,(-1)^{n-1})^T,
    det M_rho,n=det M_mu,n [1-K_n(-1,-1)].

Since p_0=1, h_0=1, p_1(y)=y-1, and h_1=D_4-D_2^2=8,

    K_1(-1,-1)=1,
    K_n(-1,-1)>=1+4/8=3/2  (n>=2).

Thus the dimension-one matrix is singular, but EVERY dimension n>=2 matrix is nonsingular and has exactly one negative eigenvalue and n-1 positive eigenvalues. The inertia follows by congruence with I-aa^T, whose squared norm is K_n(-1,-1)>1.

There is no monic degree-one polynomial orthogonal to constants for rho: rho(y+c)=rho(y)=2. For each degree n>=2 there is a unique monic q_n with rho(y^j q_n)=0 for 0<=j<n. This finite-degree existence statement is sufficient for Root's n=2k-1, k>=2 construction, although rho is not a quasi-definite moment functional in the usual all-orders sense.

## Exterior value and all roots

For n>=2 the exact formula is

    q_n(y)=p_n(y)+q_n(-1)K_n(y,-1),
    q_n(-1)=p_n(-1)/[1-K_n(-1,-1)].

Proof: applying mu against any polynomial r of degree <n gives mu(q_n r)=q_n(-1)r(-1); the kernel reproduces r, and the monic difference from p_n has degree <n. Evaluation at -1 then gives the displayed denominator.

All roots of p_n are simple and in (0,infinity), by positivity and infinite support of mu. Hence

    sign q_n(-1)=(-1)^{n+1}.

The polynomial q_n has exactly n-1 simple positive roots and one simple real root xi_n<-1. To prove this, test its rho orthogonality against (y+1)r(y), deg r<=n-2. The exterior atom disappears, giving

    integral q_n(y)r(y)(y+1)dmu(y)=0.

The usual sign-change argument for the positive measure (y+1)mu gives at least n-1 distinct positive sign-change roots. If all n roots were positive, q_n(-1) would have sign (-1)^n, contradicting its established sign. The remaining root is therefore real and nonpositive. Write q_n(y)=(y-xi_n) product_{j=1}^{n-1}(y-z_j), with z_j>0. Its sign at -1 gives -1-xi_n>0, so xi_n<-1. All n roots are distinct.

For the actual odd degree n=2k-1 this yields q_n(-1)>0. Multiplication by a positive primitive-integer clearer preserves these signs; Root's primitive q_n uses that normalization.

## Actual determinant interface, without substituting the positive measure

Reading Root's exact driver identifies the complete matrix as

    H_{ij}=integral_0^1 x^{2i+2j}q_n(x^2)[exp(x)+4/(1+x^2)]dx,
    H=R+(e+pi)q_n(-1)vv^T,  v_i=(-1)^i,  0<=i,j<k.

The entries of R are the rational endpoint terms from BOTH integrals. In particular, the measure in H is supported on [0,1] and multiplied by the SIGNED scalar q_n. It is not the positive pushforward measure mu used to establish normalization. The exterior sign q_n(-1)>0 alone does not prove H positive definite, its determinant nonzero, or its affine coefficient nonzero.

Writing det(R+s q_n(-1)vv^T)=a_k+b_k s, the actual center is c_k=-a_k/b_k whenever b_k!=0. The complete signed error is exactly

    (e+pi)-c_k=det(H)/b_k.

Both full determinant and b_k require a further analytic argument. Root's k=2,...,8 receipts establish their finite nonvanishing and diagnostic signs at those sizes only.

Primary attribution: Delgado--Fernandez--Perez--Pinar, https://arxiv.org/pdf/1601.07194, Theorem 3.1, records the classical kernel modification. The direct finite-degree derivation above handles the deliberately singular first moment prefix and gives the exterior/root signs for this exact functional. No irrationality conclusion is claimed.
