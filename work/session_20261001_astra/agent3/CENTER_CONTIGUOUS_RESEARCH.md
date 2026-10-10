> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Contiguous structure of the factorially weighted B-only center

Status: original author derivation, not an independent audit. The previously saved contact reduction and slow-range normality are provisional dependencies. The algebraic contiguous identities below are exact wherever the indicated contact matrices are invertible. No numerical samples, scans, or old checkers are used. Infinite nonstabilization remains open; Section 9 gives a closed, sparse, rational condition for it.

This note concerns ONLY the factorially weighted B-only center of the multi-row complete-form construction. It does not identify this center with the earlier full-coefficient center.

## 1. Family and an explicit admissible range

All logarithms are natural. For integer n set

    b=b(n)=floor(log n), m=m(n)=floor((b-1)/2),
    a=n+m+1, r=a-b,
    w_j=r!/(a-j)!, 0<=j<=b.

Take n>=N0=2^96. Then b>=64, 1<=m<=floor((b-1)/2), and b<=n. Both n and n+1 are in the provisional normality range n>=512 b^4 log n. Indeed, for x>=64,

    exp(x)>=512(x+1)^4 x.

At x=64 this follows from exp(64)>2^64 and 512*65^4*64<2^43. The logarithmic derivative of exp(x)/((x+1)^4 x) is 1-4/(x+1)-1/x>0. Also log(2^96)>64, since log 2>2/3. This proves the stronger bound with b replaced by b+1 at the old index. The same argument applies at n+1. All factorial arguments below are positive. Also a<=2n, so w_min>= (2n)^(-b), as required by the retained inverse estimates.

Write

    epsilon=b(n+1)-b(n) in {0,1}, B=b+epsilon,
    eta=m(n+1)-m(n) in {0,1}.

If epsilon=0, eta=0. At a border epsilon=1, eta=1 exactly when the old b is even. Put a'=a+1+eta and r'=r+1+eta-epsilon.

## 2. Rational input streams and the two actual forcing columns

Use q(z)=Q0(z)=1-z+z^2/2 and F(0)=0, F'=2/q. Define

    h^P=1/(1-z), h^Q=(exp(z)+F(z))/(1-z),
    G_n=exp(z)q(z)^n=sum_k g^n_k z^k,
    H_n^alpha=q^n D^n h^alpha=sum_k h^alpha_{n,k} z^k,
    alpha in {P,Q}.

Negative coefficient indices mean zero. The actual b-by-b system is

    T_ij=g^n_{n+i-j},
    u_i=h^P_{n,n+i}, v_i=h^Q_{n,n+i}, 0<=i,j<b,
    x=T^(-1)u, y=T^(-1)v.

These are rational data independent of e+pi. A finite coefficient specification, useful for closing every boundary term below, is

    h^alpha_{n,k}=sum_{s=0}^{min(2n,k)} q^n_s
                       (n+k-s)!/(k-s)! H^alpha_{n+k-s},
    H^P_l=1,
    H^Q_l=sum_{j=0}^l(1/j!+F_j),
    g^n_k=sum_{s=0}^{min(2n,k)}q^n_s/(k-s)!.

Here q^n_s=[z^s]q^n. For a wholly rational seed recurrence, set c_j=[z^j]F'= (j+1)F_{j+1}. Then c_0=2, c_j=c_{j-1}-c_{j-2}/2 for j>=1, with c_{-1}=0. Thus no boundary datum below is an unspecified forcing value.

The streams have different contiguous operators:

    G_{n+1}=q G_n,
    H_{n+1}^alpha=q (H_n^alpha)'-n q' H_n^alpha.       (1)

In coefficients,

    g^{n+1}_k=g^n_k-g^n_{k-1}+g^n_{k-2}/2,
    h^alpha_{n+1,k}=(k+1)h^alpha_{n,k+1}
                    +(n-k)h^alpha_{n,k}
                    +((k-1)/2-n)h^alpha_{n,k-1}.       (2)

In particular the shifted forcing window is

    f'^alpha_i=(n+2+i)h^alpha_{n,n+2+i}
                -(1+i)h^alpha_{n,n+1+i}
                +(i-n)h^alpha_{n,n+i}/2,
    0<=i<B.                                           (3)

Applying q alone to the forcing streams would be incorrect. Both P and Q obey (1)-(3), with their distinct rational seeds.

## 3. Toeplitz window shift and dimension border

Define the old-index B-by-B extension

    Tbar_ij=g^n_{n+i-j}, 0<=i,j<B.

For epsilon=0 this is T. For epsilon=1 it is the ordinary border

    Tbar = [ T  c ; ell  d ],
    c_i=g^n_{n+i-b}, ell_j=g^n_{n+b-j}, d=g^n_n.

Thus det Tbar=det T*(d-ell T^(-1)c). The stronger admissibility in Section 1 makes both old-index dimensions normal under the retained theorem. This border is separate from the change n to n+1.

Let R_B have diagonal -1, upper diagonal 1, lower diagonal 1/2. Define row vectors

    rho_plus_j=g^n_{n+B-j}, rho_minus_j=g^n_{n-1-j}.

The new contact matrix is exactly

    T'=R_B Tbar+e_{B-1}rho_plus+(1/2)e_0 rho_minus.    (4)

Entrywise this says T'_ij=g^n_{n+1+i-j}-g^n_{n+i-j}+g^n_{n-1+i-j}/2. It retains the shift of the central coefficient index from n to n+1. No invertibility of R_B is assumed or needed.

## 4. Reconstruction converts the update into a sparse defect

Let D_b be differentiation on coefficient vectors of polynomials of degree <b, let

    J_{n,b}=(I+D_b)^(-n)
       =sum_{l=0}^{b-1}(-1)^l binom(n+l-1,l)D_b^l,
    Z_b p=(z-1)p.

Z_b is a (b+1)-by-b coefficient matrix. The actual endpoint-normalized B columns are

    beta=Z_b J_{n,b}x,
    gamma=e_0+Z_b J_{n,b}y.                           (5)

Let I embed degree <b polynomials into degree <B and let E embed B-coefficient vectors of length b+1 into length B+1. Polynomial differentiation commutes with these zero embeddings. Therefore

    J_{n+1,B}(I+D_B)I=I J_{n,b}.                       (6)

This identifies the correct predictors xhat=(I+D_B)Ix and yhat=(I+D_B)Iy. Simply reusing x,y as transformed predictors would not preserve the old actual B polynomials.

For alpha=P,Q, put x^P=x, x^Q=y and

    R^alpha(z)=H_n^alpha(z)-G_n(z)x^alpha(z),
    R^alpha_k=[z^k]R^alpha.

The solved equations give R^alpha_k=0 for n<=k<=n+b-1. A generating-function identity strengthens the entrywise update:

    H_{n+1}^alpha-G_{n+1}(I+D)x^alpha
      =(qD-nq')R^alpha.                              (7)

Proof: qG_n'-nq'G_n=qG_n, so the product rule gives (7) exactly. This is the cancellation that makes the correction sparse.

Consequently d^alpha=f'^alpha-T'(I+D_B)Ix^alpha has entries

    d^alpha_i=(n+2+i)R^alpha_{n+2+i}
               -(1+i)R^alpha_{n+1+i}
               +(i-n)R^alpha_{n+i}/2.                 (8)

All entries with i<b-2 vanish. The possibly nonzero entries are

    d^alpha_{b-2}=(n+b)R^alpha_{n+b},
    d^alpha_{b-1}=(n+b+1)R^alpha_{n+b+1}
                         -b R^alpha_{n+b},           (9)

and, only when epsilon=1,

    d^alpha_b=(n+b+2)R^alpha_{n+b+2}
                -(b+1)R^alpha_{n+b+1}
                +(b-n)R^alpha_{n+b}/2.               (10)

Let s=2+epsilon and let S_B be the B-by-s selector with columns e_{b-2},...,e_{B-1}. Let delta^alpha be the s-vector in (9)-(10). Then

    x'^alpha=(I+D_B)Ix^alpha+T'^(-1)S_B delta^alpha,
    beta'=E beta+Z_B J_{n+1,B}T'^(-1)S_B delta^P,
    gamma'=E gamma+Z_B J_{n+1,B}T'^(-1)S_B delta^Q.     (11)

The endpoint e_0 in gamma is retained because its embedding is again e_0. At fixed b the entire cross-index B update uses only two inverse columns and two tail defects per forcing. A dimension border adds exactly one tail defect and one inverse column. The next forcing streams need not be solved independently from scratch.

Every correction is in the image of Z_B and hence has coefficient sum zero. Equation (11) therefore preserves beta'(1)=0 and gamma'(1)=1, an exact normalization check built into the derivation.

## 5. Factorial weights: ordinary steps and m borders

On old coordinates 0<=j<=b, the normalized weight ratio is

    w'_j/w_j=(r'!/r!)/product_{h=1}^{1+eta}(a+h-j).    (12)

Thus an ordinary step has w'_j/w_j=(r+1)/(a+1-j). At a b border with eta=0 it is 1/(a+1-j). At a b border with eta=1 it is (r+1)/((a+1-j)(a+2-j)). The new coordinate, if present, has w'_B=1. These cases separate the dimension change from the extra factorial change when m rises.

For exact center arithmetic it is useful to remove only a documented common scalar. Define integer falling-factorial weights

    f_j=a!/(a-j)!, W=diag(f_j^2).

Then diag(w_j^2)=(r!/a!)^2 W. This positive common scalar cancels from the B-only center, not from arbitrary complete-form estimates. At the next index use f'_j=a'!/(a'-j)! and W'=diag((f'_j)^2), 0<=j<=B. On old coordinates,

    f'_j/f_j=product_{h=1}^{1+eta}(a+h)
                         /product_{h=1}^{1+eta}(a+h-j). (13)

The new weight f'_B=a'!/r'! is kept. Neither (12) nor (13) is a coordinate-independent rescaling. A weight contribution to a center difference therefore persists even if both polynomial corrections vanish.

## 6. Adjugate normalization and explicit small-boundary updates

The following version involves no rational solution vector left implicit. Set

    Delta=det T, X=adj(T)u, Y=adj(T)v,
    A=Z_b J_{n,b}X,
    C=Delta e_0+Z_b J_{n,b}Y.

Then beta=A/Delta and gamma=C/Delta. Here C is a B coefficient vector, not the logarithmic polynomial of the original triple.

For alpha=P,Q, use X^P=X, X^Q=Y and define the boundary numerators

    rho^alpha_k=Delta h^alpha_{n,k}
                   -sum_{j=0}^{b-1}g^n_{k-j}X^alpha_j,
    k=n+b,...,n+b+1+epsilon.                          (14)

Form the s-vectors v^alpha by the right sides of (9)-(10) with R replaced by rho. Thus v^alpha=Delta delta^alpha exactly. Set

    Delta'=det T',
    K=Z_B J_{n+1,B}adj(T')S_B,
    P=K v^P, Q=K v^Q,
    A0=E A, C0=E C.

Equations (11) now become the fully normalized rational recurrence

    beta'=(Delta' A0+P)/(Delta Delta'),
    gamma'=(Delta' C0+Q)/(Delta Delta').              (15)

All entries in (14)-(15) have finite rational definitions in Sections 2-4. For a determinant implementation, the entries of adj(T')S_B are cofactors

    (adj(T')S_B)_{j,l}=(-1)^(i_l+j)
                         det T'[delete row i_l, delete col j],
    i_l=b-2+l, 0<=l<s.

Thus (15) needs only the two or three specified adjugate columns, rather than an unspecified second fraction. No sign or content of either determinant has been discarded.

## 7. Exact numerator of the change in center

The actual B-only center is

    t_n=(beta^T diag(w^2)gamma)/(beta^T diag(w^2)beta)
        =V/U,
    U=A^T W A>0, V=A^T W C.

Its rational endpoint normalization Delta and common weight factor (r!/a!)^2 have canceled explicitly in this displayed ratio. Define

    U0=A0^T W' A0, V0=A0^T W' C0,
    Dnew=Delta'^2 U0+2Delta' A0^T W' P+P^T W' P,
    Nnew=Delta'^2 V0
          +Delta'(A0^T W' Q+P^T W' C0)+P^T W' Q.

By (15), t_{n+1}=Nnew/Dnew and Dnew>0. In particular Dnew is the squared W' norm of Delta'A0+P; its nonvanishing follows from the nonzero first endpoint lift, not from a guessed sign of a determinant.

Define the three explicit contributions

    H_weight=U V0-V U0,
    H_linear=U(A0^T W' Q+P^T W' C0)
                            -2V A0^T W' P,
    H_quadratic=U P^T W' Q-V P^T W' P,
    H_n=Delta'^2 H_weight+Delta' H_linear+H_quadratic. (16)

Then

    t_{n+1}-t_n=H_n/(U Dnew),
    sign(t_{n+1}-t_n)=sign H_n.                       (17)

Unlike a cross product of unspecified fractions, (16) resolves the numerator into a known diagonal weight change, a term linear in two or three explicitly supplied boundary defects of BOTH forcing columns, and a quadratic term in those same defects. It also includes the reconstruction operator and every dimension border. For example, writing z=C-(V/U)A and z0=E z, the weight term is U A0^T W' z0. Old W-orthogonality does not make this new-weight expression zero.

The special case P=Q=0 leaves H_n=Delta'^2 H_weight. Conversely an apparent cancellation of the weight term alone proves nothing about the two forcing corrections. These distinctions matter even inside a fixed-b, fixed-m plateau.

## 8. A literal integer zero test with no hidden rational scaling

Equations (14)-(16) are rational, not generally integral. An explicit positive clearer is as follows. Let L be the least common multiple of the positive denominators, in lowest terms, of all entries of

    Delta', A, C, P, Q.

Zero entries have denominator one. This is a finite definition using only the exact data already specified. W and W' are integer matrices. The polynomial degree of every term of H_n in these listed rational entries is at most six. The same is true of U Dnew. Hence

    I_n=L^6 H_n is an integer,
    J_n=L^6 U Dnew is a positive integer,
    t_{n+1}-t_n=I_n/J_n.                              (18)

Its reduced numerator is I_n/gcd(|I_n|,J_n), including zero in the usual way. Thus exact equality of adjacent actual centers is equivalent to I_n=0, without assumptions on the signs of Delta,Delta' or an unretained cancellation. This is a zero-test normalization, not a reduced-denominator bound; those bounds remain Child 4's task.

The common normalizations originally removed are exactly Delta^(-2)(r!/a!)^2 at the old index and (Delta Delta')^(-2)(r'!/a'!)^2 at the new index when using (15). They multiply the corresponding numerator and denominator equally. No coordinate-dependent factorial factor or endpoint e_0 term is canceled by that observation.

## 9. Nonstabilization: precise result and unresolved condition

Conditional on the retained normality theorem, all identities above apply at every integer n>=2^96. They yield an explicit closed recurrence for both actual B columns, and an exact signed integer condition:

    the centers are not eventually constant
      iff I_n != 0 for arbitrarily large n.           (19)

Here I_n is specifically the degree-at-most-six expression (14)-(18), driven by only two boundary coefficients per forcing in an ordinary step, or three at a dimension border. It is not an unspecified numerator. The remaining mathematical problem is to rule out eventual exact cancellation among the three contributions in (16). No sign claim for an individual contribution has been proved.

An explicit interior sequence removes all simultaneous border issues. For integer k>=96 let

    n_k=ceil(exp(k))+2.

Then n_k>=2^96 and b(n_k)=b(n_k+1)=k: indeed exp(k)<=n_k and n_k+1<exp(k)+4<exp(k+1). Also m is unchanged. Thus (9), with s=2, and the ordinary weight update apply at every pair (n_k,n_k+1). Proving I_{n_k}!=0 for infinitely many k would establish infinitely many changes on this explicit unbounded sequence of adjacent pairs. This restricted condition is sufficient, not necessary, for global nonstabilization.

A sufficient signed domination condition at any step is, for example,

    |Delta'^2 H_weight|>
                 |Delta' H_linear+H_quadratic|,

with the analogous alternatives obtained by selecting either other contribution. These inequalities have not been established. Nor has an arithmetic argument excluding I_n=0 on an unbounded set been established. The identities do not assert that the sparse defects, the weight term, or their sum has a fixed sign.

The retained B-only orientation estimate implies t_n tends to e+pi on this family, conditional on its provisional inverse input. Convergence alone does not exclude eventual rational constancy without a further theorem about this same center or about e+pi. A nonzero error for the different full-coefficient center supplies no such theorem. No such transfer is made here.

## 10. Scope and ownership

The advance is the sparse defect cancellation (7)-(11), the exact dimension and factorial border ledger, and the normalized numerator decomposition (14)-(18). Nonstabilization is unresolved, but reduced to a concrete closed signed condition on explicitly generated rational boundary data.

No forcing-vector estimate, positive forcing-column lower bound, or reduced-center denominator estimate is claimed as new work here. Those remain with Child 2, the main agent, and Child 4 respectively. There is no independent audit, no numerical evidence, and no irrationality conclusion. All new files for this task are confined to work/session_20261001_astra/agent3/.
