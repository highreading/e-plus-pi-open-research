> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Canonical high denominators and endpoint-corrected factorial content

Status: main-agent author proofs, not independently reviewed. This stage consolidates the recovered denominator deductions and their subsequent extensions. Automatic author records preserve provenance but are not verification verdicts. No new calculation, seed evaluation, or replay of an accepted review is claimed. The actual rationality or irrationality of e+pi remains OPEN.

The underlying canonical companion identities and fixed-b analytic estimates are retained inputs from agent3/CANONICAL_COMPANION_TRANSFER.md and agent3/CANONICAL_DENOMINATOR_OVERLAP.md. Their author status and construction-specific hypotheses remain attached. HISTORY_RECOVERY_20261002.md has been read. The recovered Laguerre individual-row argument is outside this stage and is not a determinant-sign theorem.

## 1. One fixed construction and its integer data

Work with the SAME factorial B-only Gram center, b=3 and weight parameter m_w=1. For analytic applications take sufficiently large even n in the retained slow-growth normality domain. The integer contractions below also make sense at seed indices r>=3, without requiring their matrices to be invertible modulo a prime.

Let D differentiate coefficient polynomials of degree at most two, and let Z multiply by t-1. Put

    Krec=Z(I+D)^(-n),
    D0=diag(1,n+1,(n+1)(n+2)),
    d=(n+1)(n+2), F=(n!)^2,
    Omega=diag(1,(n+2)^2,((n+2)(n+1))^2,
                       ((n+2)(n+1)n)^2).

All entries of Krec are integers. Define

    b_s(n)=[t^s](2-2t+t^2)^n,
    Dcal_0=1, Dcal_j=j Dcal_(j-1)+1.

The normalized Toeplitz matrix and exponential vector are

    M_ij=sum_s b_s(n)(n+i)_(j+s),                 0<=i,j<=2,
    Ecal_i=sum_s b_s(n)(n+2)_(2-i+s)Dcal_(2n+i-s), 0<=i<=2.

Their respective ranges are

    0<=s<=min(2n,n+i-j),
    0<=s<=min(2n,n+i).

Falling factorials have nonnegative lengths and endpoints in these ranges. Define the integer endpoint sequence by

    sum_(a>=0) P_a t^a=(1-4t-4t^2)^(-1/2),
    P_0=1, P_1=2,
    (a+1)P_(a+1)=2(2a+1)P_a+4aP_(a-1).

The retained forcing identities give the integral vector

    J=(P_n, P_n/2+P_(n+1)/4, P_(n+2)/8)^T.

Set

    Delta=det M,
    Cmat=Krec adj(M)D0,
    y=adj(M)D0 J, x=Cmat J=Krec y,
    Dg=x^T Omega x,
    z=Cmat^T Omega x,
    g=gcd(z_0,z_1,z_2)>0.

On a normal index, Dg>0 and z^T J=Dg. In particular g divides Dg. Let

    Acal=z^T Ecal, Rcal=Delta x_0, S=Acal+d Rcal.

The primitive selector is G(t)=sum_i(z_i/g)t^i. Write e=deg G<=2, N=2n+e, and choose the retained moment clearer

    L=2^(N-1) lcm(1,...,N).

Define

    K_z(t)=t^n D_t^n[(1-2t+2t^2)^n sum_i z_i t^i]/n!,
    T_z=L calL((K_z-Dg)/(t-1)),
    calL(P)=integral_(-1)^1 P((1+iu)/2)du.

The retained exact bridge gives K_z(1)=Dg, T_z integral, and g dividing T_z and Acal. The ACTUAL rational companions are

    alpha=Acal/(F d Dg),
    kappa=Rcal/(F Dg),
    beta=T_z/(L Dg),
    c=alpha+kappa+beta, q=den(c).

All denominators in this paper are positive and reduced when den is used. In particular den(0)=1. The endpoint correction kappa must remain in S.

## 2. General rational denominator mismatch

Write reduced rationals alpha=a/Q and gamma=b/B, and put c=alpha+gamma=p/q. Define

    G0=gcd(Q,B), u=Q/G0, v=B/G0,
    Nsum=av+bu, delta=gcd(G0,|Nsum|).

Then gcd(u,v)=1 and gcd(Nsum,uv)=1. For example, at any prime dividing u, the term bu vanishes and av is a unit, since a is coprime to Q and v is coprime to u. The argument for v is identical.

Consequently

    q=(G0/delta)uv,
    uv divides q,
    gcd(delta,uv)=1,
    gcd(q,B)=B/delta.

Thus delta is exactly the retained overlap deficit. Moreover

    Q=delta q/v, B=delta q/u, Nsum=delta p,
    log(Q/G0)+log(B/G0)<=log q.

If X tends to infinity and log q=o(X), these identities imply

    log Q=log B=log delta+o(X).

These assertions include zero companions with reduced denominator one. They do not assert that the requisite common denominator cancellation occurs in the canonical family.

## 3. Removing the logarithmic numerator from a high denominator

For the canonical data set H=L Dg and Z0=F d. Multiplication of the complete center gives

    Hc=LS/Z0+T_z.

Let

    a0=gcd(Z0,|LS|), Qhigh=Z0/a0, s0=LS/a0.

Then gcd(s0,Qhigh)=1, so

    Hc=(s0+Qhigh T_z)/Qhigh

is reduced. Therefore

    Qhigh=q/gcd(q,H),
    q=H Qhigh/gcd(H,|s0+Qhigh T_z|).                (1)

In particular Qhigh divides q. Its formula contains neither Dg nor T_z.

The two simpler rational terms L Acal/(Fd) and L Rcal/F have denominators

    Astar=Fd/gcd(Fd,L|Acal|),
    Kstar=F/gcd(F,L|Rcal|).

The general mismatch lemma proves

    Mstar=Astar Kstar/gcd(Astar,Kstar)^2

 divides Qhigh, hence divides q. This follows directly by adding the two scaled terms; no estimate for their separate contents is needed.

At a prime p, if

    v_p(S)<v_p(Fd)-v_p(L),

then Qhigh has positive p-depth. Its reduced numerator is a p-unit, so (1) gives exactly

    v_p(q)=v_p(Dg)+v_p(Fd)-v_p(S).                 (2)

The logarithmic numerator cannot change this depth. Primes where Qhigh has zero depth may still involve cancellation against T_z.

## 4. Primitive content and the metric determinant

Put

    Hmat=Krec^T Omega Krec, h=det(Hmat)>0.

The canonical equations give

    z=D0 adj(M)^T Hmat y.

Every diagonal entry d_i of D0 divides d. Multiplying this identity by M^T diag(d/d_i) gives

    M^T diag(d/d_i)z=d Delta Hmat y.

Multiplication by adj(Hmat), followed by Krec, proves that g divides every coordinate of d Delta h x. Hence

    g divides d Delta h gcd(x),
    g divides dh Rcal,
    g/gcd(g,|Rcal|) divides dh.                    (3)

This includes x_0=0. In that case the last quotient is one.

Since det((I+D)^(-n))=1, h=det(Z^T Omega Z). The tridiagonal determinant equals the sum of the four products of three diagonal weights of Omega. Explicitly,

    h=(n+2)^4(n+1)^2
      *{n^2[((n+2)^2+1)(n+1)^2+1]+1}.             (4)

It has degree twelve, so dh has degree fourteen. Thus the unmatched selector content in (3) has logarithm O(log n). This proposed obstruction is automatically controlled; it cannot supply a positive factorial-scale mismatch rate.

Define the normalized endpoint-corrected integer

    S_eff=hS/g.

It is integral because g divides Acal and dh Rcal. Also put

    A=Dg/g, T0=T_z/g, H0=L A.

Then

    H0 c=LS/(Fd g)+T0=LS_eff/(Fdh)+T0.

It follows exactly that

    Qprim:=q/gcd(q,H0)
      =Fd g/gcd(Fd g,|LS|)
      =Fdh/gcd(Fdh,|L S_eff|).                    (5)

Moreover Qhigh divides Qprim and Qprim/Qhigh divides g. All versions represent the same rational denominator after the indicated scaling.

Equation (5) implies the necessary inequality

    log gcd(F,|S_eff|)>=log F-log L-log q.          (6)

Indeed F/gcd(F,|LS_eff|) divides Qprim, and gcd(F,|LS_eff|)<=L gcd(F,|S_eff|). For fixed b=3, log L=O(n). Therefore a geometric bound log q=O(n) requires

    log gcd((n!)^2,|S_eff|)>=2log(n!)-O(n).         (7)

No such global content estimate is established.

There is an additional useful expression without an adjugate in the coefficient vector of this linear contraction. Let ell=z/g and let k0 be row zero of Krec. The same matrix identity gives

    S_eff=ell^T[h Ecal+diag(d/d_i)M adj(Hmat)k0^T]. (8)

The bracket is an integer vector and retains the endpoint contribution. The primitive vector ell itself remains arithmetically nontrivial.

## 5. Nonzero numerator in the fixed-b analytic domain

The retained canonical estimates imply

    |alpha-e|<=n^C/n!, |kappa|<=n^C/n!

for some fixed C on sufficiently large even fixed-b=3 indices. For the second estimate, Cauchy–Schwarz gives |kappa|<=w_0/sqrt(a), with a=||u||_W^2. The retained reconstruction bound and fP_0>=n! M^n/(2pi sqrt(n)), M=1+sqrt(2), give 1/sqrt(a)<=n^C/n!; w_0<=1.

Consequently

    S_eff/(Fdh A)=alpha+kappa -> e>0.

Thus S_eff is positive and nonzero eventually in this analytic domain. This observation justifies the finite valuations used below. It is an application of the named author analytic inputs, not a new independent acceptance of them.

## 6. A varying-residue gate for the actual center denominator

Let p>=7 be prime, p<=n, and write n=ap+r. Assume

    3<=r<=p-3.

The integer data at r are defined by Section 1 even when M_r is singular modulo p. Put tau=2^(ap).

In M_n, every falling-factorial term longer than its residue-r counterpart contains ap and vanishes modulo p. The surviving coefficient indices satisfy s<=r+2<p. Their coefficients in (1-t+t^2/2)^n are polynomials in n with p-unit denominators. Therefore

    M_n=tau M_r mod p.

The exponential vector has the same truncation. Its surviving Dcal indices are 2ap+j. The division-free recurrence Dcal_j=jDcal_(j-1)+1 resets at 2ap and gives Dcal_(2ap+j)=Dcal_j modulo p for every needed j, including j that crosses p. Hence

    Ecal_n=tau Ecal_r mod p.

The generating function for P satisfies over F_p

    sum P_j t^j=(1-4t-4t^2)^((p-1)/2) sum P_j t^(pj).

The polynomial factor has degree p-1 and constant coefficient one. Thus P_(pa)=P_a modulo p. Propagating the P recurrence from ap through r+2 steps uses only the unit divisors 1,...,r+2. It follows that

    J_n=P_a J_r mod p.

The reconstruction and metric matrices are integer polynomials in n for b=3 and reduce to their r-values. Taking the exact adjugates and contractions gives

    z_n=tau^4 P_a z_r,
    Dg_n=tau^4 P_a^2 Dg_r,
    Acal_n=tau^5 P_a Acal_r,
    Rcal_n=tau^5 P_a Rcal_r,
    S_n=tau^5 P_a S_r                              mod p. (9)

If p does not divide P_a S_r, then S_n is a p-unit. Also p does not divide d_n. Put f=v_p(n!) and e_p=v_p(L). We have

    e_p<=floor(log_p(2n+2))<2floor(n/p)<=2f.

For the strict inequality, with a=floor(n/p)>=1, use 2n+2<=2p(a+1)<p^(2a) for p>=7. The first rational term S_n/(FdDg) consequently has strictly greater denominator depth than beta. Therefore

    v_p(q_n)=2v_p(n!)+v_p(Dg_n).                   (10)

No unit assumption on Dg_n is needed. This is an author all-index gate derived from the explicit formulas; it does not establish how often P_a S_r is a unit.

## 7. Fixed-prime lifting and its restricted contribution

The retained exact seed values include

    S_3=3836501339775392808960,
    Dg_3=1960127638514171904,
    Delta_3=-1169408.

These values come from the earlier seed record; no evaluation is repeated here.

Fix p>=7 with p not dividing Delta_3 h_3. Put t_p=v_p(S_3), eta_p=v_p(Dg_3). For n=p^k+3 and sufficiently large k, the same truncation argument works modulo p^k: all discarded falling factorials contain p^k, and the surviving coefficient indices are at most five. The exponential recurrence resets at 2p^k. The endpoint recurrence propagates through the next five unit divisors.

With a=p^k and tau=2^a, this proves

    z_n=tau^4 P_a z_3,
    Dg_n=tau^4 P_a^2 Dg_3,
    S_n=tau^5 P_a S_3                              mod p^k.

Furthermore P_a=2 modulo p. The matrix taking J_3 to z_3 is

    D0 adj(M_3)^T Hmat_3 adj(M_3)D0,

which is invertible modulo p under the stated exclusions. Since the first coordinate of J_3 is 32, z_3 is nonzero modulo p. Thus p does not divide g_n; also h_n is a p-unit. For k>max(t_p,eta_p),

    v_p(S_eff,n)=t_p, v_p(Dg_n)=eta_p.

Here v_p(L)=k, v_p(dh)=0, and

    v_p(F)=2(p^k-1)/(p-1).

Eventually this exceeds k+t_p. Applying (5) at its positive depth gives

    v_p(q_n)=2(p^k-1)/(p-1)+eta_p-t_p.             (11)

This is a local author theorem. Different primes in (11) describe different index progressions; their contributions cannot simply be added.

A general limitation quantifies this issue. For any residue set R_n contained in {0,...,n-1}, of size s_n>=1, grant every prime dividing product_(r in R_n)(n-r) its entire factorial contribution. Then

    sum_(p dividing that product) 2v_p(n!)log p
      =O(n[1+log(s_n log n)]).                    (12)

Proof: v_p(n!)<=n/(p-1). Split the prime sum at y=max(2,s_n log n). Above y, the sum of log p is at most s_n log n, so its weighted contribution is O(1). Below y, the retained lcm bound gives theta(t)<=t log 4, and partial summation gives sum_(p<=y)log p/(p-1)=O(1+log y).

In particular a fixed finite atlas gives O(n log log n), and a subpolynomial-size atlas gives o(n log n). This is a limitation on factorial-scale rates, not on every possible exclusion of geometric q: an attained superlinear logarithmic denominator bound could still suffice.

## 8. Removing endpoint zeros and boundary residues in a large-prime range

The elementary lcm estimate also gives the useful harmonic identity

    sum_(p<=x) log p/p=log x+O(1).                 (13)

For completeness, expand log(N!) as sum_(p^j<=N)floor(N/p^j)log p. The rounding error after division by N is at most psi(N)/N=O(1). The sum of terms with j>=2 is bounded by the convergent series sum_(l>=2)log l/[l(l-1)]. The elementary factorial estimate proves (13).

Put A0=floor(n^(1/3)). Consider primes n/(A0+1)<p<=n, and let C_n consist of those also satisfying

    3<=n mod p<=p-3,
    p not dividing P_floor(n/p).

Then

    sum_(p in C_n)log p/p=(1/3)log n+O(1).         (14)

Indeed, (13) gives log(A0+1)+O(1) for the unrestricted interval. Boundary primes divide (n-2)(n-1)n(n+1)(n+2), so their harmonic weight is o(1). The positive constant-term identity

    P_a=CT_x(2+x+2/x)^a

implies 1<=P_a<=5^a. The endpoint-excluded primes divide product_(a=1)^A0 P_a, so their harmonic weight is at most

    (A0+1)/n * (log 5)A0(A0+1)/2=O(1).

This proves (14) without an additional prime-distribution hypothesis.

Split C_n into G_n, where p does not divide S_(n mod p), and Z_n, where it does. Equation (10) proves

    log q_n>=2 sum_(p in G_n)v_p(n!)log p.

All these primes exceed sqrt(n) eventually. Using v_p(n!)=floor(n/p) and theta(n)=O(n), (14) yields

    2 sum_(p in C_n)v_p(n!)log p=(2/3)n log n+O(n),

and hence

    2 sum_(p in Z_n)v_p(n!)log p
      >=(2/3)n log n-log q_n-O(n).                 (15)

Equivalently,

    sum_(p in Z_n)log p/p
      >=(1/3)log n-log q_n/(2n)-O(1).

Thus geometric q would require first-order zeros of the endpoint-corrected residue numerators on essentially the entire leading mass of this candidate set. These zeros are necessary, not sufficient for the deeper cancellation required by (7). No upper bound for their aggregate mass is proved here.

## 9. A necessary deep valuation above the square-root scale

For sufficiently large normal even n, Section 5 gives S_eff!=0. Define

    Pset_n={p prime:sqrt(2n+2)<p<=n, p not dividing dh},
    K_n=max_(p in Pset_n) v_p(S_eff).

The set is nonempty eventually, as also follows from the weighted estimate below. At every such prime, v_p(L)=1 and v_p(F)=2floor(n/p). Equation (5) gives

    v_p(q)>=max(0,2floor(n/p)-1-v_p(S_eff)).        (16)

Equation (13) and theta(n)=O(n) show

    sum_(p in Pset_n)(2floor(n/p)-1)log p
      =n log n+O(n).

Removing primes dividing dh costs at most O(sqrt(n)log n), because log(dh)=O(log n).

For every integer K>=0, uniformly in K,

    sum_(p<=n)min(K,2floor(n/p))log p
      <=2n log(K+1)+O(n).                         (17)

For K>=1 with 2<=2n/(K+1)<=n, split at 2n/(K+1). The lower range contributes O(n) by theta; the upper range is bounded using (13). The cases outside this range follow from the full factorial bound or are immediate. K=0 contributes zero.

Subtracting (17) from the available mass in (16) proves

    log q>=n log n-2n log(K_n+1)-O(n),             (18)

with the O(n) constant independent of K_n. Therefore:

* log q=O(n) requires K_n+1>=c sqrt(n) for some c>0 depending on that geometric bound.
* log q=o(n log n) requires K_n+1>=n^(1/2-o(1)).
* K_n<=n^(epsilon+o(1)), epsilon<1/2, would imply liminf log q/(n log n)>=1-2epsilon.
* K_n+1<=sqrt(n)/omega(n), omega(n)->infinity, would already exclude every uniform geometric bound, through log q>=2n log omega(n)-O(n).

No such upper bound for K_n has been established. A height bound for S_eff is not a proof of a sufficiently small primewise valuation bound.

## 10. What remains to be proved

The main target is now the normalized endpoint-corrected integer S_eff, not an unreduced logarithmic clearer. Small q requires almost all double-factorial content in (7), many residue zeros in (15), and a deep valuation in (18). These are simultaneous necessary conditions, not evidence that any one is attained.

The next paper, CANONICAL_FACTORIAL_COEFFICIENT_LIFTING.md, records a recurrence and a division-free contraction formula for investigating these valuations. It removes an artificial modular division problem but does not settle the global content question.

Child 3 studies the exceptional factor of the total Gram overlap deficit, which is a separate task. Child 4 studies coordinate centers, not these Gram centers. Children 1 and 2 retain their logarithmic residual and isolated-phase tasks. No completed audit or seed calculation is repeated. None of the results in this stage decides the actual e+pi problem.
