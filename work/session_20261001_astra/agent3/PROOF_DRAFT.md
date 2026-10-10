> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Finite prime certificates exclude shrinking throughout the b=1 family

Status: exact computation and proof assembly complete; submitted for independent audit. Historical dependencies retain their previously reviewed scope. This document does not claim a new independent audit.

Let S={5,13,41,43,59,67}. For the actual endpoint-matched degree-(n,1,n) construction, let q_n be the positive reduced denominator of A_n(1)/B_n(1), and let L_n be its primitive integer form in e+pi. The finite certificates below, together with the reviewed transfer, residue-one lift, and evaluated-error theorem, imply

    liminf_(n→∞) log(q_n)/n >= W := sum_(p in S) 2 log(p)/(p-1),
    liminf_(n→∞) log|L_n|/n >= W-2 log(1+sqrt(2)) >= 20453/200000 > 0.

These are statements on all sufficiently large indices, with no parity restriction. Thus every subsequence with indices tending to infinity has primitive forms growing in absolute value. This excludes shrinking for this fixed b=1 family. It does not establish rationality or irrationality of e+pi, or exclude other degree allocations or constructions.

## 1. Exact finite input and bounded stopping

The predeclaration fixed all 38 primes from 23 through 199, processed increasingly. Only the following prefix was tested:

| p | Complete zero set of Ccal_r modulo p, 0<=r<p |
|---:|---|
| 23 | {1,18} |
| 29 | {1,14} |
| 31 | {1,12} |
| 37 | {1,23} |
| 41 | {1} |
| 43 | {1} |
| 47 | {1,27} |
| 53 | {1,3,32} |
| 59 | {1} |
| 61 | {1,33,40} |
| 67 | {1} |

There are 491 complete modular scalar rows. The selected primes 41,43,59,67 have 210 rows in total. All five coordinates H,K,Acal,Bcal,Ccal agree between two distinct exact constructions in every selected row, giving 1050 coordinate comparisons. The certificate includes both residue arrays and the exact rational scalar values for r=0,...,66. Existing primes 5 and 13 are cited within the scope of work/session_20260927/hp_b1_uniform_5_13_independent_review.md; their old atlas was not rerun.

Construction I uses a_s(k)=[x^s](1-x+x^2/2)^k in F_p[x], D_0=1, D_j=jD_(j-1)+1, and falling factorials:

    H_n = sum_(s=0)^n (n)_s a_s(n),
    Acal_n = sum_(s=0)^n (n)_s a_s(n) D_(2n-s),
    K_(n+1) = 2 + sum_(s=1)^(n+1) (n)_(s-1)(2n+2-s)a_s(n+1),
    Bcal_n = 2D_(2n+1)
             + sum_(s=1)^(n+1) (n)_(s-1)(2n+2-s)a_s(n+1)D_(2n+1-s),
    Ccal_n = K_(n+1) Acal_n - H_n Bcal_n.

Construction II starts from ordinary integer Legendre coefficients:

    J_k(t) = sum_(j=0)^floor(k/2)
             (2k-2j)!/[j!(k-j)!(k-2j)!] (2t-1)^(k-2j).

Write E_d=sum_(h=0)^d 1/h!, R_k=sum_j [t^j]J_k/(n+j)!, and T_k=sum_j [t^j]J_k E_(n+j), always keeping the same n for k=n and k=n+1. With f=(n!)^2/2^n, compute over Q

    H_n=f R_n,                 Acal_n=f T_n,
    K_(n+1)=f(n+1)R_(n+1)/2,   Bcal_n=f(n+1)T_(n+1)/2.

Only after exact rational normalization are the coordinates reduced modulo p. All denominators are verified to be powers of two; H and K are integers. No division modulo p by n+1 is made, including at r=p-1. Ccal is then computed from its determinant. This is independent of the modular Rodrigues polynomial engine and D recurrence. The normalization identities are those in the reviewed actual-denominator source.

The deterministic checker is check_bounded_prime_extension.py. Its output exact_certificate.json records the complete finite data, the stopping history, exact rate bounds, and source hashes. Every earlier accumulated successful subset had rate strictly below the target. The first surplus occurred upon accepting 67, so all 27 declared candidates from 71 through 199 remain untested.

## 2. From finite rows to every residue at every index

Use the reviewed all-residue transfer in work/session_20260927/hp_b1_prime_seed_transfer_and_closed_atlas.md, Section 2:

    (H_n,K_(n+1),Acal_n,Bcal_n,Ccal_n)
      == (H_r,K_(r+1),Acal_r,Bcal_r,Ccal_r) modulo p,
    r=n mod p, 0<=r<p.

Its proof includes r=0 and the prime-block boundary r=p-1. The D recurrence resets modulo p. Falling factorials remove the high tails, and Frobenius reduces the surviving coefficient terms. At r=p-1 in K and Bcal, s=1,...,p-1 vanish by Frobenius, s=p vanishes through 2n+2-s, and s>=p+1 vanish through the falling factorial. Thus the boundary involves no forbidden division by n+1.

For each p in S, the complete seed zero set is exactly {1}. Consequently Ccal_n is a p-unit whenever n is not 1 modulo p. The finite data prove this all-index assertion through the transfer theorem; they are not samples of canonical HP degrees.

## 3. Actual numerator separation and residue-one compensation

The reviewed exact endpoint formula is

    x_n=A_n(1)/B_n(1)=Ucal_n/Delta_n,
    Ucal_n=Qcal_n + 2^(n+1) Ccal_n/(n!)^2,
    Qcal_n=2K_(n+1)Q_n-(n+1)H_n Q_(n+1),
    Delta_n=(n+1)P_(n+1)H_n-2P_n K_(n+1),
    P_k=J_k(1),
    Q_k=8 sum_(j=1)^k P_(j-1)P_(k-j)/j.

Delta_n is an integer. All claims involving this quotient are restricted to Delta_n!=0. The accepted analytic endpoint theorem supplies that condition for every sufficiently large n. No finite seed argument is used to assert nonvanishing of Delta.

Fix p in S and n>=p. Put f_p=v_p(n!) and ell=floor(log_p(n+1)). The integral P coefficients in the convolution give v_p(Q_k)>=-floor(log_p k). Also

    2f_p > ell.

Indeed if ell=1, f_p>=1. If ell>=2, then n>=p^ell-1 and

    2f_p >= 2 floor(n/p) >= 2(p^(ell-1)-1) > ell.

First suppose n is not 1 modulo p. Then v_p(Ccal_n)=0, so the factorial term in Ucal has valuation -2f_p, strictly smaller than the lower bound -ell for Qcal. The least-valuation term is unique; therefore

    v_p(Ucal_n)=-2f_p.

Since q_n is the actual positive reduced denominator of Ucal_n/Delta_n, rational reduction gives

    v_p(q_n)=max(0,v_p(Delta_n)-v_p(Ucal_n))
            =2f_p+v_p(Delta_n) >=2f_p.

Now suppose n is 1 modulo p and let a=v_p(n-1)>=1. The all-depth residue-one theorem for every p>=5 in work/session_20260927/hp_b1_residue_one_actual_numerator.md, Sections 1–2, proves

    v_p(Ccal_n)=a,
    v_p(H_n)>=a,   v_p(K_(n+1))>=a.

Its essential unit is Ccal_n/(n-1)==27 modulo p. It follows from the reviewed restricted analytic lift H/(n-1)==-3/2 and K/(n-1)==4, together with Acal==3 and Bcal==10. Exact vanishing at n=1 permits analytic root division, so the conclusion holds at every depth a, not just at a=1. This is a separate proved analytic input; the finite zero sets alone do not establish it.

Thus v_p(Delta_n)>=a and v_p(Qcal_n)>=a-ell. The factorial term has valuation a-2f_p<a-ell. Strict separation again yields

    v_p(Ucal_n)=a-2f_p,
    v_p(q_n)=max(0,2f_p+v_p(Delta_n)-a)
            =2f_p+v_p(Delta_n)-a >=2f_p.

The shared root in Delta compensates for the forced numerator root. No unit assumption on a Legendre endpoint is needed. These are bounds for the fully reduced q_n, including numerator cancellation, not bounds for a coefficient clearer or unreduced height.

For every n>=67 with Delta_n!=0, all six inequalities therefore hold simultaneously:

    product_(p in S) p^(2v_p(n!)) divides q_n.

Eventual Delta nonvanishing makes this an unconditional eventual assertion within the accepted analytic domain of this family.

## 4. Exact strict rate certificate

Legendre's factorial valuation formula gives v_p(n!)=n/(p-1)+O(log n) for each fixed prime. Since S is fixed and finite,

    log q_n >= sum_(p in S) 2v_p(n!)log p = Wn+O(log n),
    W = (log 5)/2 + (log 13)/6 + (log 41)/20
        + (log 43)/21 + (log 59)/29 + (log 67)/33.

The rate comparison uses rational arithmetic exclusively. For 0<=z<1 and m>=1 define

    S_m(z)=2 sum_(j=0)^(m-1) z^(2j+1)/(2j+1),
    T_m(z)=2z^(2m+1)/[(2m+1)(1-z^2)].

The positive logarithm series, with its geometric tail bound, proves

    S_m(z) <= log((1+z)/(1-z)) <= S_m(z)+T_m(z).

For any rational x>=1 write x=2^k y with 1<=y<2, then apply these bounds to log 2 with z=1/3 and to log y with z=(y-1)/(y+1). The checker uses m=16 and outward rational rounding to multiples of 10^-12.

For the target tau=2 log(1+sqrt(2)), put

    d=18446744073709551616,
    a=26087635650665564424.

Exact integer arithmetic gives

    2d^2-a^2=36478007661041971136>0,
    (a+1)^2-2d^2=15697263640289157713>0.

Hence a/d<sqrt(2)<(a+1)/d. Monotonicity and the same rational logarithm bounds give bounds for tau. The certificate records

    W >= 4308181309389547/2310000000000000,
    tau <= 44068679351/25000000000,
    W-tau >= 236235337357147/2310000000000000 > 0.

A simpler outward weakening is

    W >= 1865013/1000000,
    tau <= 440687/250000,
    W-tau >= 20453/200000 > 0.

All intermediate prime logarithm enclosures and all stopping comparisons are stored in exact_certificate.json. The saved enclosures were also checked locally using fresh 24-term rational sums, without repeating or extending the scalar scan. That check is recorded in stored_certificate_validation.json; it is not an independent researcher audit.

## 5. Primitive-form consequence and precise scope

The accepted evaluated-error theorem gives eventual nonvanishing of the normalized remainder and

    log|L_n|=log q_n-tau n+o(n).

Here if x_n=u_n/q_n is in lowest terms with q_n>0, then

    L_n=u_n+q_n(e+pi)=q_n R_n(1)/B_n(1).

Combining the analytic identity with the simultaneous actual-denominator bounds proves

    liminf_(n→∞) log|L_n|/n >= W-tau >= 20453/200000 > 0.

In particular, for each 0<c<20453/200000, eventually |L_n|>=exp(cn). The conclusion covers both parities and every residue class. It uses no estimate of proximity to either the dyadic or ternary analytic root and requires no infinite prime-density claim.

The new finite seed extension and this assembly await independent audit. The historical general transfer, residue-one Sections 1–2, and 5/13 seeds were independently passed in work/session_20260927/hp_b1_uniform_5_13_independent_review.md. The analytic evaluated-error and endpoint inputs are given in work/session_20260913/hp_b1_endpoint_attempt.md and the reviewed synthesis work/session_20260927/hp_b1_uniform_five_thirteen_and_even_exclusion.md. The separate fixed-degree theorem in work/session_20260927/fixed_exponential_degree_error_theorem.md also supplies the analytic rate for b=1. Historical statements of remaining arithmetic gaps describe their earlier state and are not altered by this report.
