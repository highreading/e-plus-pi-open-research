> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact right-block Smith response and the surviving quotient obstruction

Bounded author completion: Agent 2, 2026-10-02. Fresh gate: `SHORT_STACK_RIGHT_BLOCK_SCHUR_GATE.md`. Generic Smith/Schur operations are classical and explicitly credited there. The result below finishes the current actual compact-diagonal interface; the uniform arithmetic step remains open. No new determinant scan or prime atlas is used.

## 1. Fixed actual blocks and all index costs

Use the integer even-Legendre basis and exact matrices N',W' from `SHORT_STACK_COMPACT_DIAGONAL_INDEX.md`. Its contents satisfy

    h'_N=Delta_(2k-1) h_N theta_N, theta_N|Delta_k^2,
    h'_W=Delta_k Delta_(k-1) h_W theta_W, theta_W|Delta_(2k).

All Delta and theta costs are retained. They have total logarithm O(k^2), and their prime factors are at most 8k-4. Assume beta1!=0 (in particular every k>=24 by Agent3's author theorem). Then N' has full column rank and W' full row rank.

Partition the tall matrix as

    N'=[ X_N | P_N ],
    X_N:2k by k, columns j=0,...,k-1,
    P_N:2k by (k-1), columns j=k,...,2k-2.

The compact diagonal is exactly zero in P_N. It is the TWO COMPLETE Gamma projections

    P_N=[mu((y+1)ell_i ell_j); -L f((y+1)ell_i ell_j)].

Because ALL columns of N' are independent, P_N has rational rank k-1. This rank statement is proved from the actual beta1 nonzero input; no independent pure-Gamma normality is assumed.

## 2. Tall quotient: an exact multiplicative content formula

Choose integer unimodular U,V with

    U P_N V=[D_N;0],
    D_N=diag(d1,...,d_(k-1)), di>0, di|d_(i+1),
    delta_N=product di=gcd(all maximal minors of P_N).

Write U X_N=[A_N;S_N], where S_N has size (k+1) by k. It is the actual left block mapped to the FREE quotient by the saturated rational span of P_N. Then

    h'_N=delta_N h(S_N),                               (1)

where h(S_N) is the positive gcd of all its k by k minors.

Proof: after the right-block column transformation, the full matrix is

    [[A_N,D_N],[S_N,0]].

A maximal minor omitting one of the top k-1 rows is zero: its k+1 remaining bottom rows have entries in only k left columns. A minor omitting a bottom row is, up to sign, delta_N times the corresponding k-minor of S_N. Taking the gcd proves (1), including every prime depth and all cancellations inside each residual determinant. Full column rank also proves S_N has rank k.

Thus the original actual content is exactly

    h_N=delta_N h(S_N)/(Delta_(2k-1) theta_N).           (2)

The pure-Gamma right block supplies one known index; it does NOT by itself control the residual content h(S_N).

## 3. The COMPLETE affine response reduces to dimension k+1

Let m0 denote the original first column in the integer column basis 1,(y+1),...,y^(2k-2)(y+1). In that basis

    det[m0+t u,N]=I0+t J1,
    I0=L^k beta0, J1=L^(k-1) beta1, I1=LJ1.

Apply diag(T_k,T_k) to the rows and the even-Legendre basis to the N columns, keeping the first column unchanged. Put

    D_basis=Delta_k^2 Delta_(2k-1),
    m0'=diag(T_k,T_k)m0, u'=diag(T_k,T_k)u.

The new full pencil is [m0'+t u',X_N,P_N], whose coefficient pair is D_basis(I0,J1). In the same Smith quotient as Section2, let a,b be the bottom k+1 coordinates of U m0',U u'. Define the INTEGER residual coefficients

    A=det[a,S_N], B=det[b,S_N].

There is one common orientation sign epsilon such that

    D_basis I0=epsilon delta_N A,
    D_basis J1=epsilon delta_N B,
    D_basis I1=epsilon delta_N L B.                    (3)

Consequently the FINAL primitive center, denominator, and full gcd obey EXACTLY

    c=-A/(L B),
    q=L|B|/gcd(A,L B),
    D_basis G_actual=delta_N gcd(A,L B).               (4)

The actual beta1 nonzero input gives B!=0. No division by an error, a cofactor, or an unproved response occurs. Equations (3)--(4) keep BOTH coefficients and the physical extra L. In particular delta_N cannot be counted as a new divisor of the original physical pair without accounting for D_basis. The unimodular multipliers may have large entries; no small-height gain for individual Schur entries is claimed.

## 4. A local Schur formula when the right block is saturated

At any prime for which a (k-1)-square minor P0 of P_N is a unit, permute its rows and write

    P_N=[P0;P1], X_N=[X0;X1].

Over Z_p the exact quotient is

    S_N=X1-P1 P0^(-1)X0,
    a=m01-P1 P0^(-1)m00,
    b=u1-P1 P0^(-1)u0.                                (5)

The row eliminations are p-unimodular because det P0 is a unit. This formula retains the entire compact diagonal inside X1/X0. Saturation gives v_p(delta_N)=0, so (1) says v_p(h'_N)=v_p(h(S_N)), rather than zero automatically.

For p>8k-4, the basis indices and L are units. Even when P_N is saturated, the ACTUAL output denominator is

    v_p(q)=max(0,v_p(B)-v_p(A)),                       (6)

and simultaneous coefficient content can still arise from the residual quotient. Thus a right-block unit minor alone is insufficient to prove the full affine pair primitive.

## 5. Wide block: the exact largest-pivot loss

In W', partition at the last compact diagonal column:

    W'=[X_W|P_W],
    X_W:(2k-1) by (k-1), columns j=0,...,k-2,
    P_W:(2k-1) by (k+1), columns j=k-1,...,2k-1.

The compact part is zero in P_W, but its top C block STILL contains -ell_i(-1)ell_j(-1). Thus P_W is the two Gamma projections PLUS the actual rank-one endpoint; it is not permissible to label it pure Gamma after dropping that term.

For k>=2, its rational rank is at least k because W' has rank 2k-1 and X_W has k-1 columns. There are exactly two cases.

If rank P_W=k+1, take its integer Smith form U P_W V=[D_W;0], with r=k+1 positive pivots e1|...|er and delta_W=product ei. Write U X_W=[A_W;S_W]; here S_W has size (k-2) by (k-1) and full row rank. Put h_S=h(S_W), with h_S=1 when k=2, and

    z_i=det[A_(W,i);S_W]/h_S, i=1,...,r.

These are integers because expansion along the first row is an integer combination of the maximal minors of S_W. The COMPLETE maximal-minor content is

    h'_W=gcd(delta_W times all maximal minors of S_W,
             (delta_W/e_i)det[A_(W,i);S_W] for every i)
         =delta_W h_S/zeta_W,

    zeta_W=lcm_i(e_i/gcd(e_i,z_i)), zeta_W|e_r.         (7)

Proof: a maximal row minor omits one column. Omitting a left column leaves all Smith pivot columns and gives the first class. Omitting right pivot i leaves the ith top row filled by the left block and gives the second class. The first class, after division by h_S, has gcd delta_W; taking prime valuations gives the lcm expression (7). Zeros of z_i are handled by gcd(e_i,0)=e_i and contribute the factor 1, so the formula has no zero division.

Hence an unsaturated right block may lose up to its LARGEST Smith pivot in the wide content. One must not replace (7) by h'_W=delta_W h_S without proving zeta_W=1. If delta_W is a p-unit, then v_p(h'_W)=v_p(h_S), again leaving a residual compact-plus-Gamma quotient condition.

If rank P_W=k, its Smith form has k positive pivot columns and one zero column. Let delta_W be the product of those pivots. The bottom quotient S_W is now a square (k-1)-matrix of nonzero determinant. Only the maximal minor omitting the zero column is nonzero, giving exactly

    h'_W=delta_W |det S_W|.                            (8)

This rational rank-loss branch cannot be excluded merely from the full W' rank. No actual all-k assertion selecting one of the two branches is made. Both transfer back to h_W through the retained Delta/theta identity.

## 6. Explicit remaining obstruction and scope endpoint

Even a saturated right block and a UNIT diagonal compact summand do not force a saturated quotient. For the simple abstract tall block with k=2, take P=(1,0,0,0)^t and

    X=[[0,0],[p,0],[0,1],[0,0]], p any prime.

Its right-block content is 1, but the quotient S=[[p,0],[0,1],[0,0]] has maximal-minor content p. It can be written with the compact contribution diag(1,1) in the bottom two rows by taking the corresponding Gamma-left rows (-1,1) and (0,-1). This is an explicit obstruction to the proposed STRUCTURAL inference from compact diagonality and right-block saturation. It is NOT a claim that the fixed actual Gamma moments realize this artificial example.

For the ACTUAL family the surviving arithmetic problem is now explicit: bound or construct unit minors for S_N and S_W, while controlling the actual right-block Smith indices, endpoint term, zeta_W, and nonmonic Delta/theta factors. Outside primes<=8k-4, if both right blocks are saturated, the known full-pair content sandwich becomes

    max(v_p h(S_N),v_p h(S_W))
       <=v_p G_actual<=v_p h(S_N)+v_p h(S_W).

A nonzero complete response and compact positivity do not settle these p-adic quotient contents. No uniform odd-content upper law or actual denominator lower law has been proved. The all-k dyadic divisor and the actual response scale remain valid completed results; the current compact-diagonal route ends at this exact unresolved quotient interface.

Readiness: current bounded route is finished. The Smith/Schur tools used here are established methods. No further extension or numerical scan of this family was planned without fresh human steering.
