> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A fixed-dimensional factorial-moment quotient for the complete boundary contraction

Author mathematics, target L13, 2026-10-02. This is a structural reduction of the all-depth normalized boundary theorem, rather than another prime atlas. It compresses its seed adjugate and every long derivative sum to an h-dimensional residual matrix and4h factorial moments, with explicit quadratic-character endpoint data. No independent review or unconditional conclusion about e+pi is asserted.

Use the canonical b,m,h definitions of ALL_STRUCTURAL_BOUNDARY_CHARTS.md, with

    1<=h<=min(m+1,b-m-2), d=b-h, M=m+1-h,
    p>2b an odd prime, chi=(-1)^((p-1)/2),
    alpha_s=[z^s]q0(z)^(-h), q0=1-z+z²/2, alpha_s=0 for s<0.

Assume the seed endpoint P=J_0(p-h) is a unit; all endpoint digits being units is the additional hypothesis needed by the existing all-depth/actual-q theorem. This note identifies its finite constants delta and nu exactly and does not strengthen that digit hypothesis.

## 1. Two moment sequences, each of order2h

For every integer c define, in F_p,

    mu_c = sum_(t=0)^(p-1) alpha_(t+c)(-1)^t t!,
    lambda_c = sum_(t=0)^(p-1) alpha_(t+c)(-1)^t t!
                                      Dcal_((-h-1-t) mod p).     (1)

Here Dcal_0=1,Dcal_j=jDcal_(j-1)+1,0<=j<p. Only these actual scalar residues are used. Let q0(z)^h=sum_(j=0)^(2h) q_j z^j. Formal inversion gives

    sum_j q_j alpha_(s-j)=1 if s=0, and0 otherwise.

Multiplying this identity by the respective fixed t weights and summing proves

    sum_(j=0)^(2h)q_j mu_(c-j)
       = (-1)^(-c)(-c)!                       if -(p-1)<=c<=0,
       = 0                                    otherwise;

    sum_(j=0)^(2h)q_j lambda_(c-j)
       = (-1)^(-c)(-c)! Dcal_((c-h-1) mod p)  if -(p-1)<=c<=0,
       = 0                                    otherwise.          (2)

Both edge coefficients q_0=1 and q_(2h)=2^(-h) are units. Therefore mu_0,...,mu_(2h-1) and lambda_0,...,lambda_(2h-1) determine every index required by the quotient, by exact forward/backward recurrence. The number of prime-dependent factorial moments is4h, independent of b and p. This is a parameter-count reduction, not a claim that these4h residues are independent or that computing them costs constant time in p.

Every additional Dcal residue required by the finite forcing is an affine function of C_p=Dcal_(p-1)=sum_(j=0)^(p-1)(-1)^j j!, or a fixed small nonnegative-index value. In the index range used below and under p>2b, negative offsets have magnitude at most b+2h-1<=2b and are strictly below p. Their affine formulas follow by repeatedly solving Dcal_(p-j)=(-j)Dcal_(p-j-1)+1 backwards from C_p; only j<p is divided out. The positive short values and their g derivatives are fixed rational data. Thus the recurrence uses no new p-length Dcal vector as an independent arithmetic parameter.

## 2. The endpoint vector is fixed by chi

Write a=-1+i, abar=-1-i and qplus(z)=1+2z+2z²=(1-az)(1-abar z). The seed endpoint identity is

    J_i(p-h)=[z^(p-h)]qplus(z)^(-h)(1+z)^i mod p.              (3)

Indeed Frobenius sends qplus^(p-h) to qplus(z^p)/qplus(z)^h, and its positive z^p block cannot enter a coefficient of degree p-h. Define e=abar/a,d0=1-e and

    L_(h-k)=(-1)^k binom(h+k-1,k)e^k d0^(-h-k),0<=k<h.

Expansion at each pole gives the exact rational partial fraction identity

    qplus(z)^(-h)=sum_(j=1)^h L_j/(1-az)^j
                                 +conjugate branch.           (4)

For 0<=k<b, p>2b makes p-h-k nonnegative, and its coefficient reduces to the fixed Gaussian rational expression

    E_k(chi)=sum_(j=1)^h L_j binom(-h-k+j-1,j-1)
                                  (-1+chi i)a^(-h-k)
                                      +conjugate branch.       (5)

The binomial coefficient is an integer polynomial value with p-unit factorial denominator, and a^p=-1+chi i in F_p[i]. Formula (5) holds whether F_p[i] is a field or the split algebra; a and a-abar remain units. Its sum is rational and affine in chi. Therefore

    J_i(p-h)=sum_(k=0)^i binom(i,k)E_k(chi) mod p.              (6)

This eliminates any independent endpoint-vector parameter. The known generalized central-trinomial reflection identity gives the particular check P=chi(-4)^(1-h)P_(h-1); (3)–(6) also supply it directly. The reflection principle is existing primary literature, including Henningsen/Straub and the2026 Kohen paper recorded in TARGET_LEDGER.md. The application to the normalized corrected Gram quotient is the new derivation here.

For example h1 yields, through i=4,

    J(chi=1) =(1,1,1/2,0,-1/4),
    J(chi=-1)=(-1,0,1/2,1/2,1/4).

For h2 it yields

    J(chi=1) =(-1/2,0,1/4,0,-3/8),
    J(chi=-1)=(1/2,0,1/4,1/2,3/8).

The normalized vector J/P uses only this fixed rational data, with its displayed endpoint-unit proviso.

## 3. A residual h-dimensional seed block, with no full inverse

At the seed n=p-h, upper row i<h has t=h-i. Direct falling-factorial reduction in the ranges that precede the first zero factor gives

    N_(i,j)=(-1)^(t-1)/(t-1)! · mu_(1-t-j),
    A_i    =(-1)^(t-1)/(t-1)! · lambda_(1-t).                  (7)

For A, the scalar offset is 2n+i-s=-h-1-(s+t-1) modulo p, which is precisely the weight in (1). Terms beyond the original finite range contribute zero because the factorial contains p; no negative-index scalar extrapolation is invoked.

The lower d rows of N are [T0,0], where

    T_(l,j)=l![z^(l-j)]e^z/q0(z)^h for j<=l,0 otherwise.

Its diagonal l! is a unit. Let U0 be the first d columns of the upper h rows and U1 their last h columns. Put

    tau=product_(l=0)^(d-1) l!, sigma=(-1)^(hd),
    Delta=sigma tau det(U1).

This is the exact seed det(N), after moving the lower rows first. For the normalized top endpoint e_i=D0_i J_i/P,0<=i<h, the cofactor response is

    Ybar=(0_d, sigma tau adj(U1)e).                            (8)

Let a0=T0^(-1)A_lower, where A_lower is the explicit short contact sum from the existing chart. The complete seed exponential cofactor is

    Bbar_lower=Delta a0,
    Bbar_high=sigma tau adj(U1)(A_top-U0 a0).                  (9)

Both (8) and (9) are polynomial block-adjugate identities. They can be checked when U1 is invertible and then hold identically over the polynomial coefficient ring, so their specialization permits det(U1)=0. Only T0 is inverted. For h1, adj([a])=[1] even at a=0, and e_0=1, so the final Ybar coordinate is the universal constant (-1)^(b-1)product_(l=0)^(b-2)l!. The earlier singular determinant obstacle remains harmless.

## 4. Every long first-order sum is a moment

For f_(l,v)(u)=(u+l)_v, its derivative at0 has the exact form

    f1_(l,l+1+t)=l!(-1)^t t!,0<=t<p.                         (10)

All lengths v>=p+l+1 contain the second zero factor and lie outside the one-u derivative window. Accordingly the derivative matrix of FINITE_BOUNDARY_QUOTIENT_FORMULA.md is

    G_(l,j)=l!mu_(l+1-j)
         +sum_(s=0)^max(l-j) [alpha_s f1_(l,j+s)
                                      +adot_s f0_(l,j+s)],    (11)

where adot_s=[z^s]q0^-h log q0, and an empty short sum is0. The logarithmic scalar derivative vector is

    F_l=l!lambda_(l+1)
        +sum_(s=0)^l [alpha_s f1_(l,s)+adot_s f0_(l,s)]
                                             Dcal_((l-h-s) mod p)
        +sum_(s=0)^max(l-h)alpha_s f0_(l,s)g_(l-h-s),         (12)

with g_0=2C_p,g_j=jg_(j-1)+2Dcal_(j-1). In (12), substituting s=t+l+1 in the long tail makes its Dcal offset -h-1-t, independent of l. Equations (11),(12) contain exactly the long sums already proved in the all-depth chart; no formal derivative at a varying negative scalar index is substituted for them.

Now substitute (8),(9),(11),(12) into the two triangular solves and final contractions of FINITE_BOUNDARY_QUOTIENT_FORMULA.md. This computes the exact delta,nu with no b-dimensional adjugate and no separate p-length window for each derivative row. Low Tc_0 remains the quotient (t0+Delta)/u, so nu retains the entire endpoint correction kappa.

## 5. The local cancellation variety

Fix b,m,h and chi. Write U=(mu_0,...,mu_(2h-1)) and L=(lambda_0,...,lambda_(2h-1)). The preceding formulas yield explicit rational polynomials

    delta=mathcalD_(b,m,h,chi)(U),
    nu=mathcalV_(b,m,h,chi)(U,L,C_p).                          (13)

Their coefficient denominators divide a fixed integer depending only on b,h and the fixed endpoint P; at primes p>2b where P is a unit they are p-integral. The recurrence forcing makes every mu_c affine in U and every lambda_c affine in L,C_p. Consequently delta has U-degree at most2h, and nu is affine jointly in L,C_p, with U-degree at most2h+1 (total degree at most2h+2). These are safe upper bounds; reductions or actual moment relations may lower them. The h-dimensional adjugate in (8),(9) makes the assertions valid on det(U1)=0 as well.

Thus the complete first normalized numerator vanishes exactly when the actual prime-dependent moment point lies on mathcalV=0. It is not determined by C_p alone in the supplied formula, and no independence or distribution assertion about U,L is made. For the b5,h1 and h2 instances, the saved nonzero specializations prove each corresponding polynomial is nonzero. A general nonzero-polynomial theorem for every b,m,h is not claimed.

This is a precise higher-content gateway. On the hypersurface, the all-depth theorem gives v_p(V_n)>=2v_p(n+h)+1 throughout that boundary disk; it does not supply an arbitrarily deep numerator loss or a smaller actual q. Off the hypersurface, nu is a unit and the existing full-beta comparison gives

    v_p(q_n)=2v_p(n!)+v_p(D_n)-2v_p(n+h)>=2v_p(n!)

for every normal n>=2p, with the actual evaluated gcd. The first normalized delta may vanish independently and create deeper raw denominator content; that still does not imply primitive cancellation. No numerical moment pattern is used to infer a supply of good primes or a shrinking form.

## 6. Exact supporting receipt and remaining obstacle

boundary_moment_quotient.py constructs the two initial2h moment blocks, expands them by (2), computes the fixed endpoint data by exact Gaussian rational arithmetic, and uses only the h-dimensional residual adjugate. BOUNDARY_MOMENT_QUOTIENT_RECEIPT.json agrees in Delta,P,T,G,F,Ybar,Bbar,X,Tc,xbar,tbar,delta,nu with22 own previously defined finite-chart references: the20 b5 certificate charts, one b4,h1 case p43, and one new single h3 case b7,m2,p17. The latter has(delta,nu)=(15,2). This is author implementation evidence, not an independent mathematical audit or a higher-depth experiment.

The unresolved arithmetic is now concentrated in4h prime-dependent factorial moments and their explicit corrected polynomial contraction. A C_p-only expression, a distribution theorem preventing mathcalV=0, or a deeper normalized tower on that hypersurface would be a substantive next result. The compression itself proves none of these. It supplies a compact local algebraic target that remains distinct from root's global content/resultant analysis and the separate inverse-Apéry Hermite–Padé target.
