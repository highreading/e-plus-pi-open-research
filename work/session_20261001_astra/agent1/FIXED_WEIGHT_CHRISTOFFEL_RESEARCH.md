> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Fixed-weight Christoffel research

Status: new paper proofs supported by 41 successful symbolic controls. No numerical HP indices, degree sweep, prime search, or previous checker execution was used. Earlier results and unfinished companion material are preserved.

We study a=n+1, c=n, contact M=2n+b+1, and B(1)=C(1), with b slowly growing. The main quantitative range below is n>=40, b=floor(log n), with natural logarithm. In this range 3<=b<=n/2. The polynomial transformation itself holds in every degree.

The outcome has two parts. The fixed weight removes the weighted Gram-nonsingularity gap of the preceding changing-weight proposal. It yields explicit transformed reference and complete-companion estimates. It does not yet prove a smaller primitive evaluated remainder: the actual weighted contact determinant, choice of rational direction, and final endpoint reduction remain essential. One natural selector gives exactly the balanced forms and is stopped as a proposed new-family improvement.

## 1. Exact weight and rational solution space

Use the established functional

    L(f)=integral_{-1}^1 f((1+iu)/2) du,
    F(z)=z L(1/(1-tz)), F(1)=pi.

Write Cstar(t)=t^n C(1/t), B(z)=sum_{j=0}^b beta_j z^j. At Taylor degree n+2+r the equation is

    ellhat_beta(t^r)+L(t^(r+1) Cstar)=0,
    ellhat_j(t^r)=1/(n+2+r-j)!.

Thus the exact weight is the fixed polynomial t:

    Lhat(f)=L(tf).

For contact M the high equations have r=0,...,n+b-2. Including matching, there are n+b equations in n+b+2 rational B,C coefficients, so the solution space has dimension at least two. This does not establish a nonzero matched endpoint.

For b>=2, the first n+1 equations determine Cstar by weighted projection, once the weighted Gram matrix is known nonsingular. We prove that nonsingularity below. The remaining high tests have degrees n+1,...,n+b-2, hence number b-2. Contact M+1 adds one test. No contact normality is inferred from the equation count.

The bilinear form Lhat(fg) is complex-segment integration without conjugation. Its norms have alternating signs. All later positivity statements concern real scalar bounds or auxiliary absolute-value integrals, not this bilinear form or its determinants.

## 2. One-step transformation and signed norms

Let p_k be the established monic Legendre system, with

    h_k=L(p_k^2)=2(-1)^k/((2k+1)binom(2k,k)^2),
    A_k=p_k(1)>0, b_k=A_(k+1)/A_k,
    p_k(0)=(-1)^k A_k,
    p_(k+1)=(t-1/2)p_k+beta_k p_(k-1),
    beta_k=k^2/[4(4k^2-1)].

Define

    Q_k(t)=[p_(k+1)(t)+b_k p_k(t)]/t.                 (1)

The numerator vanishes at zero, so Q_k is a rational monic polynomial of degree k. For every polynomial f of degree below k,

    Lhat(Q_k f)=L((p_(k+1)+b_k p_k)f)=0.

Since Q_k is monic,

    hhat_k=Lhat(Q_k^2)=b_k h_k!=0.                    (2)

Consequently the weighted Gram matrix through degree n is nonsingular for every n. More precisely,

    det[L(t^(i+j+1))]_(i,j=0)^n
      =A_(n+1) det[L(t^(i+j))]_(i,j=0)^n.

This follows by taking the product of the signed norms; product_{k=0}^n b_k=A_(n+1). It is not a positivity argument. It proves polynomial projection normality only, not normality of the factorial contact matrix.

The transformed recurrence is

    Q_(k+1)=(t-a_hat_k)Q_k+beta_hat_k Q_(k-1),
    a_hat_k=1/2+b_k-b_(k+1),
    beta_hat_k=beta_k b_k/b_(k-1)=b_k(b_k-1/2), k>=1.

Its initial polynomials are Q_0=1 and Q_1=t-1/3. In particular a_hat_0=1/3 and a_hat_1=17/30. These are exact initial identities, not sampled approximants.

The endpoint values are

    Ahat_k=Q_k(1)=2A_(k+1),
    Ahat_(k+1)/Ahat_k=b_(k+1).                         (3)

## 3. Second-kind functions and the rational shift

For z off the integration segment define

    m(z)=L(1/(z-t)),
    v_k(z)=L(p_k(t)/(z-t)),
    w_k(z)=L((p_k(t)-p_k(z))/(t-z)).

Thus v_k(z)=p_k(z)m(z)-w_k(z). The transformed functions satisfy exactly

    mhat(z)=z m(z)-2,
    vhat_k(z)=v_(k+1)(z)+b_k v_k(z),
    what_k(z)=w_(k+1)(z)+b_k w_k(z)-2Q_k(z).           (4)

The last expression is a rational-coefficient polynomial in z. At z=1,

    mhat(1)=pi-2,
    vhat_k=(b_k+alpha_k)v_k,
    alpha_k=v_(k+1)/v_k.

The established bounds b_k>=1/2 and -1/6<alpha_k<0 show that vhat_k has strict sign (-1)^k. This derives its sign from the original system without assuming weighted positivity.

The transformed Wronskians are

    Ahat_k what_(k+1)-Ahat_(k+1) what_k=hhat_k,
    Ahat_(k+1)vhat_k-Ahat_k vhat_(k+1)=hhat_k.

Define epsilon_k=|v_k|/A_k and epsilon_hat_k=|vhat_k|/Ahat_k. Then

    epsilon_hat_k/epsilon_k=(1+alpha_k/b_k)/2,
    1/3<epsilon_hat_k/epsilon_k<1/2.                  (5)

The ordinary scalar exponential rate is unchanged. With s=(sqrt(2)-1)^2, the established two-sided estimates imply, for k>=1,

    (2/3)exp(-s)s^k <= epsilon_hat_k
                         <=4s^k/(1-s)^2.             (6)

There is also an exact rational-approximant interpretation:

    2+what_k/Ahat_k
      =1/2[w_k/A_k+w_(k+1)/A_(k+1)].                 (7)

The shift by 2 is indispensable. The transformed reference is an adjacent average of rational pi approximants, with their alternating errors. Formula (7) alone gives no statement about the HP endpoint gcd.

## 4. Uniform transformed reference estimates

First, for k>=2,

    3/5<=b_k<=11/18.

The starting value is b_2=3/5. Induction follows from b_(k+1)=1/2+beta_(k+1)/b_k, using 1/16<=beta_(k+1)<=1/15. Therefore, for k>=2,

    22/45<=a_hat_k<=23/45,
    0<beta_hat_k<=11/162.

On |t|<=1/20, recurrence induction gives negative real parts for every Q_(k+1)/Q_k. The first ratio has real part at most -17/60, the second at most -31/60, and for k>=2 the upper bound is -79/180. In particular

    rhat_n=Q_n/Q_(n+1) is analytic,
    Re rhat_n<0, |rhat_n|<=180/79, n>=2.              (8)

The transformed second-kind recurrence, valid from k>=1, is

    vhat_(k+1)=(1-a_hat_k)vhat_k+beta_hat_k vhat_(k-1).

Apply it backwards at k=n+1, using the alternating signs. For n>=2,

    alpha_hat_n=vhat_(n+1)/vhat_n<0,
    |alpha_hat_n|
      =beta_hat_(n+1)/(1-a_hat_(n+1)+|alpha_hat_(n+1)|)
      <5/36.                                        (9)

Let Uhat=Q_(n+1), Vhat be the weighted kernel at endpoint 1, and What be the actual weighted projection remainder of 1/(1-t). CD subtraction gives

    What/Uhat=(vhat_n/hhat_n)(1-alpha_hat_n rhat_n)/(1-t),
    Vhat/Uhat=-(Ahat_n/hhat_n)(1-b_(n+1)rhat_n)/(1-t).

Put mu_hat=vhat_n/hhat_n>0 and nu_hat=Ahat_n/|hhat_n|. Their exact comparison with the original amplitudes is

    mu_hat=(1+alpha_n/b_n)mu_n,
    nu_hat=2nu_n,
    mu_hat/nu_hat=epsilon_hat_n.

Equations (8)-(9) prove the explicit shape bounds

    360/553 <= |(1-alpha_hat_n rhat_n)/(1-t)| <=2080/1501,
    20/21 <= |(1-b_(n+1)rhat_n)/(1-t)| <=3780/1501.

Thus one may use

    Mhat_W=(2080/1501)mu_hat,
    Mhat_V=(3780/1501)nu_hat,
    Mhat_W/Mhat_V=(104/189)epsilon_hat_n.              (10)

As in the balanced half-plane argument, comparing the squared moduli of 1+c r and 1-b r, for 0<c<b and Re r<=0, yields the direct estimate

    (2/7)epsilon_hat_n <= |What/Vhat| <=epsilon_hat_n. (11)

The denominator is actually nonzero, not replaced by an upper bound. Both reference functions are nonzero on this disk. Their factorial determinant contractions need not be nonzero.

For the high reference ratios, k>=3 gives

    |Q_(k+1)/Q_k|
      <=1/20+23/45+(11/162)(180/79)=1131/1580.         (12)

This is smaller than 397/540, but its use in a normalized determinant requires the actual endpoint loss to be retained.

Two additional estimates will be useful. All a_hat_k>=1/3, and beta_hat_k>0. The same real-part induction on Re t<1/3 proves that every zero of Q_k has modulus at least 1/3. Hence

    |Q_(n+1)(1/z)|<=|Q_(n+1)(0)|(1+3/|z|)^(n+1).

Also

    (2/3)A_k<=|Q_k(0)|<=A_k.                          (13)

To prove (13), let d_k be the derivative at zero of p_(k+1)/p_k. Then Q_k(0)=p_k(0)d_k, d_0=1, and

    d_k=1-beta_k d_(k-1)/b_(k-1)^2.

Since beta_k/b_(k-1)^2<=1/3, induction gives 2/3<=d_k<=1.

## 5. Actual weighted projection and endpoint normalization

For b>=2, the established moment reduction now has a nonsingular weighted Gram matrix. It reconstructs Cstar uniquely from beta. The remaining conditions are

    ellhat_beta(Q_(n+l))=0, l=1,...,b-2,
    sum_j beta_j(1+uhat_j)=0,
    uhat_j=ellhat_j(Vhat).                            (14)

The b-2 high tests and matching leave at least two rational directions. Polynomial Gram nonsingularity has not proved the rank or endpoint properties of this reduced system.

Write

    T_hat_j(P)=sum_m [t^m]P Epartial_(n+1+m-j).

All partial-sum indices are nonnegative. The complete factorial-tail identity gives

    ellhat_j(P/(1-t))=eP(1)-T_hat_j(P).

With A0=Ahat_n, A1=Ahat_(n+1), h=hhat_n, and w0=what_n, w1=what_(n+1), the elementary endpoints are

    uhat_j=(A0 T_hat_j(Uhat)-A1 T_hat_j(Q_n))/h,
    xhat_j=(w0 T_hat_j(Uhat)-w1 T_hat_j(Q_n))/h+2uhat_j.

For every solution beta of (14),

    X=A(1)=sum beta_j xhat_j,
    Y=B(1)=sum beta_j=C(1),
    R(1)=ellhat_beta(What)=X+Y(e+pi).                  (15)

The term 2uhat_j is the rational endpoint shift caused by Lhat(1/(1-t))=pi-2. On Y!=0,

    X/Y=-2+[w0 T_hat_beta(Uhat)-w1 T_hat_beta(Q_n)]
                 /[A1 T_hat_beta(Q_n)-A0 T_hat_beta(Uhat)].

It must be retained in the actual numerator. Since 2 is an integer, it does not itself improve the reduced denominator: den(r-2)=den(r).

For a cofactor representative at contact M, append one specified rational selector to the b-2 high rows. At contact M+1, use the additional actual high row instead. Let N represent the resulting alternating form after any common rational scale has been removed. Define

    tau_U=T_hat(Uhat), tau_P=T_hat(Q_n),
    Z0=-evec^T N tau_U, Z1=-evec^T N tau_P,
    d=A1 Z1-A0 Z0, K=tau_U^T N tau_P.

On d!=0 the complete quotient identities are

    D_W/D_V=(vhat_n Z0-vhat_(n+1)Z1)/d,
    Tcomp/D_V=-e-K/d,
    X/Y=-2-(w1 Z1-w0 Z0)/d+K/d.                      (16)

Both partial-exponential rows and both rational second-kind terms are present. These formulas also identify precisely which selected weighted determinant must not vanish: d, equivalently det[Hhigh;evec;ellhat(Vhat)]. No slow-growth normality theorem for the balanced family is imported to establish this condition.

## 6. Complete exponential companion: normalized and absolute bounds

There are two useful exact normalizations. They must not be confused.

For the cofactor companion in (16), put

    beta_vec=A0 tau_U-A1 tau_P,
    lambda_N=N beta_vec/d.

Then sum lambda_N,j=1 and Hhigh lambda_N=0. The full-tail rows a=ellhat(Uhat/(1-t)), c=ellhat(Q_n/(1-t)) satisfy

    beta_vec=A1 c-A0 a,
    e+K/d=(lambda_N dot a)/A1.                       (17)

For an arbitrary actual matched solution, put lambda_B=beta/Y. Matching instead gives A1(lambda_B dot c)-A0(lambda_B dot a)=-h. Consequently

    R(1)/Y=[lambda_B dot a+vhat_(n+1)]/A1.            (18)

This last identity is a complete evaluated-remainder formula independent of a selector. It moves all direction conditioning into the normalized exponential contraction. In general lambda_N and lambda_B are different vectors.

A transformed Rodrigues formula makes either contraction explicit. With Pcal_k=x^k H_k(x), define the rational polynomial

    Psi_k=Pcal_(k+1)' + b_k(2k+2)(2k+1)Pcal_k.

From (1) and the ordinary monic Rodrigues identity,

    sum_l [t^l]Q_k(t) x^(k+1+l)/(k+1+l)!
       =Psi_k(x)/(2k+2)!.                            (19)

The cancelled constant coefficient in p_(k+1)+b_k p_k shows x^(k+1) divides Psi_k. Its degree is 2k+1.

Take k=n+1. The complete tail, whose first factorial is n+2+l-j, requires derivative j+1:

    a_j=e/(2n+4)! integral_0^1 exp(-x)Psi_(n+1)^(j+1)(x) dx.

For either normalized vector lambda define S_lambda=sum_j lambda_j Psi_(n+1)^(j). In the slow range n>=40, b>=3, the first actual residual high row is ellhat(Uhat), so S_lambda(1)=0. Also x^r divides S_lambda, with r=n+2-b>=1. Therefore

    G_lambda=S_lambda/[x^r(1-x)] is rational polynomial,
    deg G_lambda<=n+b.

Integration by parts has zero boundary contribution at both endpoints and gives

    (lambda dot a)/A1
      =e/[A1(2n+4)!] integral_0^1 exp(-x)x^r(1-x)G_lambda(x) dx.

Thus any proved H_lambda>=sup_[0,1]|G_lambda| supplies

    |(lambda dot a)/A1|
       <=e H_lambda/[A1(2n+4)!(r+1)(r+2)].             (20)

At contact M+1 the first high row exists already for b>=2. At contact M and b=2, the boundary condition at one requires an additional suitable selector and is not automatic.

The apparent extra factorials in (19)-(20) are not independent arithmetic gains: Psi_k contains the factor (2k+2)(2k+1) in its second summand. More importantly, G_lambda contains the actual d or Y. No useful uniform bound for its norm has been proved by writing this representation.

A second uniform bound makes comparison with the balanced family particularly transparent. Set

    Fhat_n=max(||Q_n||_1/Ahat_n,||Q_(n+1)||_1/Ahat_(n+1)),
    Delta_hat=|d|/(A0|Z0|+A1|Z1|),
    C_hat=min_{j:kappa_j!=0} sum_i |N_ji|/|kappa_j|,
    kappa_j=sum_i N_ij.

On d!=0 the minimum is nonempty. The two-dimensional alternating-form identity and the complete-tail bound give

    |Tcomp/D_V|<=C_hat e Fhat_n/[Delta_hat(n+2-b)!],
    |D_W/D_V|<=epsilon_hat_n/Delta_hat.               (21)

These bounds hold with all the actual conditioning quantities retained. For every k>=2,

    8/11 <= (||Q_k||_1/Ahat_k)/(||p_k||_1/A_k) <=43/54.

For proof, the zero half-plane and real coefficients make Q_k's coefficients alternate in sign. The same holds for p_k. If c_k=||p_(k+1)||_1/||p_k||_1, then c_k=3/2+beta_k/c_(k-1), so 3/2<=c_k<=14/9. Evaluating (1) at -1 makes the displayed ratio (c_k-b_k)/(2b_k), and the stated bounds follow from 3/5<=b_k<=11/18. Thus, with Fbal_n the analogous maximum for p_n,p_(n+1),

    (8/11)Fbal_n<=Fhat_n<=(43/54)Fbal_n.              (22)

The normalized companion majorant has one additional tail factorial relative to the same-index balanced bound. This advantage is conditional on comparing the actual conditioning and reduced denominators, not merely on (22).

## 7. Explicit all-size determinant companion majorant

For completeness, retain the established Gaussian/divided-difference factors C_d(R), J_d(R) on the disk 1/20, and set

    Ehat_n(R)=exp(R)(R+1)R^(-n-2)|Q_(n+1)(0)|(1+3/R)^(n+1).

The high-row product for contact M with a selector is

    Hhat=M_selector(1131/1580)^((b-2)(b-3)/2), b>=3,

where M_selector bounds its representing polynomial divided by Uhat. Such a finite explicit coefficient bound exists because Uhat has no zeros on the disk; it is retained, not treated as harmless. For contact M+1 use Hhat=(1131/1580)^((b-1)(b-2)/2).

The complete absolute bounds are

    Bhat_V=C_b Hhat Mhat_V Ehat_n^b J_b/b!,
    Bhat_W=C_b Hhat Mhat_W Ehat_n^b J_b/b!,
    Bhat_T=C_(b+1)Hhat Mhat_V Mhat_W
                    [Ehat_n/(R+1)]^(b+1)J_(b+1)/(b+1)!.

All dimensions, row factors and the outside integration factorial remain present. Their positive companion ratio is exactly

    Xi_hat=Bhat_T/Bhat_W
      =[(b+1)^((b+1)/2)/b^(b/2)]rho^(-b)
         (1-1/(rho R))^(-(b+1))
         *Mhat_V Ehat_n(R)/(R+1)^(b+1)
         *b!/[sqrt(2pi)(4R/pi^2)^(b+1/2)], rho=1/20.

At R=n, n>=40 and b<=n/2,

    Xi_hat <= exp(26)/n^2
                  *[e/(s n)]^n[5pi^2/(2n)]^b.        (23)

Here is a uniform justification. The dimension prefactor is at most exp(1/2)sqrt(b+1), the disk gap contributes at most exp(21), and the factorial/Gaussian factor is at most sqrt(pi/(8n))(pi^2/8)^b. Equations (3),(13) and the balanced scalar bounds give

    Mhat_V |Q_(n+1)(0)|<=cV_hat exp(s)a s^(-n),
    cV_hat=3780/1501, a=(1+sqrt(2))/4.

The reciprocal-root correction is at most exp(123/40). Finally cV_hat a<2<e, s<1/5, and sqrt(pi(b+1)/(8n))<1. The remaining exponential constant is below exp(1031/40)<exp(26), proving (23).

In fact Xi_hat<1/400 throughout n>=40 in this range: use e<3, s>1/6, pi<4, 18/n<1/2, and 3^26<2^42. The right side of (23) is then below 2^(42-n)/n^2<=1/400. In particular this is a justified common threshold for b=floor(log n).

For fixed lambda>0 and R=lambda n in the slow range,

    log Xi_hat=-n log n+O_lambda(n).

This is the logarithm of a positive majorant ratio. It does not prove that the actual companion is small relative to D_W, which may vanish.

The same-index balanced ratio Xi_bal has the same dimension factors. From (13), their exact comparison is

    Xi_hat/Xi_bal
      =2(cV_hat/cV_bal)d_(n+1)/R
         *[(1+3/R)/(1+2/R)]^(n+1),
    2/3<=d_(n+1)<=1, cV_bal=1340/513.                (24)

For R=n this is less than 6/n. This is a quantitative improvement in the selected companion majorant, not yet in a primitive form.

## 8. Same-index primitive comparison and exact stopping result

Normalize a rational solution by making the combined B,C coefficient vector primitive integral. The established integer derivative recurrence for F shows that (n+1)! clears A. With X=A(1), Y=B(1)!=0, define

    g_w=gcd(|(n+1)!X|,|(n+1)!Y|),
    q_w=|(n+1)!Y|/g_w.

Then exactly

    |L_w|=q_w|R(1)/Y|=(n+1)!|R(1)|/g_w.              (25)

This includes all full-polynomial content and final endpoint cancellation. Neither (n+1)! nor d replaces q_w. Equations (20)-(21) therefore give, respectively,

    |L_w|<=q_w[epsilon_hat_(n+1)
        +eH_lambdaB/(A1(2n+4)!(r+1)(r+2))],

and the selected-cofactor certificate

    |L_w|<=q_w/Delta_hat
           [epsilon_hat_n+C_hat eFhat_n/(n+2-b)!].   (26)

Compare (26) with the established balanced certificate at exactly the same n,b and contact 2n+b+1:

    B_primitive_bal=q_bal/Delta_bal
           [epsilon_n+C_bal eFbal_n/(n+1-b)!].

For its two summands, the ratios of the weighted to balanced majorants are bounded by

    principal ratio:
      (q_w Delta_bal)/(q_bal Delta_hat) * epsilon_hat_n/epsilon_n,

    companion ratio:
      (q_w Delta_bal)/(q_bal Delta_hat) * (C_hat/C_bal)
                           * (43/54)/(n+2-b).         (27)

The first scalar ratio lies between 1/3 and 1/2. Thus the analytic comparison is explicit, including the complete companion, but neither q_w/Delta_hat nor C_hat/C_bal is controlled by the Christoffel identity. No primitive improvement is claimed without those missing quantities.

For the determinant-majorant formulation put delta_w=log(q_w Bhat_V/|D_V,w|), and define delta_bal using the same-index balanced majorants and actual endpoint. Then their complete positive primitive certificates have exact ratio

    exp(delta_w-delta_bal) * (6968/6993)
       * (epsilon_hat_n/epsilon_n)
       * (1+Xi_hat)/(1+Xi_bal).                      (28)

The unknown loss difference in (28) prevents an inference from the smaller raw bounds. At b of order log n, a constant high-row slack accumulated quadratically in b has logarithm O((log n)^2)=o(n); the earlier quadratic-in-n obstruction cannot simply be imported.

There is a rigorous stopping result for one natural selector. Let ell_j(t^r)=1/(n+1+r-j)! be the balanced factorial functional, and put a_j=ell_j(p_(n+1)). Direct Christoffel algebra gives the rank-one relations

    t Vhat_n=V_n+(2A_n/h_n)p_(n+1),
    t What_n=W_n-[vhat_n/(b_n h_n)]p_(n+1).           (29)

Since ellhat_j(P)=ell_j(tP), weighted and balanced endpoint/remainder rows differ only by multiples of a.

More concretely, the weighted contact equations are exactly the balanced high Taylor equations with the lowest equation, at degree n+1, omitted. For a weighted solution let f_0 be that missing coefficient of B exp(z)+C F(z). Orthogonality of p_(n+1) against Cstar and the weighted equations of powers 1,...,n+1 give

    ell_beta(p_(n+1))=p_(n+1)(0)f_0.

The factor p_(n+1)(0) is nonzero. Hence the selector ell_beta(p_(n+1))=0 is exactly the missing balanced equation, equivalently [z^(n+1)]A=0. Its selected triples are precisely the balanced triples at the same n,b and contact M. Their complete evaluated remainders and rational endpoints agree, not merely their asymptotic rates.

For the identical primitive integral B,C pair, the balanced clearer is n!, while the weighted clearer is (n+1)!. Therefore

    g_w=(n+1)g_bal, q_w=q_bal,
    L_w=L_bal after the same endpoint sign normalization.

The extra clearer factor cancels in the actual gcd. This selector is stopped as a proposed new-family primitive improvement. It may permit alternative bounds for the same forms, but it does not create improved primitive forms by changing the degree cap.

The entire weighted two-direction family is not thereby excluded or proved equivalent to the balanced family. Whether a nonbalanced direction with a nonzero endpoint exists, and whether it improves (25), remains a rank-and-arithmetic question. No balanced contact-normality theorem is silently extended to it.

## 9. Precise remaining research gap

Polynomial Gram nonsingularity is now proved for every degree, so that obstacle from weight t^n has genuinely disappeared. The residual contact matrix is explicit: rows ellhat_j(Q_(n+l)), l=1,...,b-2, together with matching. A chosen rational selector, or the M+1 contact row, produces the determinant d in (16). Its nonvanishing and quantitative conditioning must be established in the weighted family itself.

A primitive improvement beyond the balanced selector requires a specified nonbalanced direction and control of its actual q_w/Delta_hat and companion conditioning, or a direct estimate for the normalized polynomial G_lambdaB that retains Y. The final endpoint gcd in (25) cannot be replaced by a coefficient clearer. Complete-remainder nonvanishing is an additional requirement for nonzero integer forms.

The new proofs establish signed Christoffel normality, second-kind transformations, explicit uniform reference ratios, the complete normalized companion representations and bounds, a same-index primitive budget comparison, and exact equivalence for the stopped balanced selector. They do not establish shrinking, actual-family divergence, or irrationality of e+pi.

Supporting evidence: check_fixed_weight_christoffel.py completed with exit code 0 and sandboxed=true; fixed_weight_christoffel_checks.json records PASS_FIXED_WEIGHT_CHRISTOFFEL_CONTROLS for 41 new symbolic checks. These verify algebraic transformations, rational constants, normalization indices, and the exact common-pair gcd comparison. The all-index conclusions above rest on their written proofs. No previous successful control was rerun, and the stopped coarse inverse certificate and unfinished companion audit were not reopened.
