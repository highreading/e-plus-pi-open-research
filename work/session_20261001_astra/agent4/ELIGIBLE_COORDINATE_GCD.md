> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Eligible coordinate gcds and canonical selector heights

New arithmetic by Agent 4. The completed coordinate-center and inverse reviews are retained without rereading or recalculation. The new limited obstruction review is saved separately as DIRECT_SELECTOR_OBSTRUCTION_REVIEW.md. This note proves an actual factorial denominator contribution on an explicit unbounded analytically eligible subfamily and identifies the remaining content through exact primitive-selector formulas.

The only new numerical operation was one exact residue gate at b=3, p=13, r=3. It returned exit code 0 and PASS_SINGLE_NEW_RESIDUE_GATE. Its full relevant data are recorded below. No prime table, old checker, or canonical approximation solve was rerun.

## 1. Domain, analytic eligibility, and notation

For the general formulas assume the actual relaxed contact lift exists, with caps (n,b,n), contact 2n+b, and endpoint matching. Let Psi be its B-coefficient block, u=Psi(1,0), v=Psi(0,1). For the complete error bound additionally use the retained domain

    n>=16, 3<=b<=n, n>=512 b^4 log n,
    1<=m<=floor((b-1)/2).

Put lambda=n+m+1, omega_i=(lambda)_i, and c_lambda=sum_(i=1)^b omega_i^(-2). The retained coordinate result defines the nonempty rational eligible set

    Jelig={j in {1,...,b}:
      b(1+c_lambda)omega_j^2 u_j^2
         >=sum_(i=0)^b omega_i^2 u_i^2}.

Every eligible coordinate has u_j!=0. Its rational center t_j=v_j/u_j has the complete error bound

    |t_j-(e+pi)|<=delta_coord,
    delta_coord=sqrt(b(1+c_lambda)) delta_n,
    delta_n=n^(10b)[2^(-n)+2((1+sqrt(2))/2)^n/n!].

The selection cost is retained. Neither eligibility nor selection of the smallest denominator within Jelig uses a numerical value of e+pi. The arithmetic below applies to each eligible coordinate separately. Coordinate quotients are not identified with Gram centers or direct scalar forcing ratios.

The explicit arithmetic theorem will use b=3, m=1. Thus lambda=n+2. This is an unbounded set of indices in a fixed-b subfamily, not a theorem for b tending to infinity.

## 2. Fixed integral Toeplitz normalization

Use the actual b by b Toeplitz matrix

    T_ik=[z^(n+i-k)] exp(z)Q0(z)^n,
    Q0(z)=1-z+z^2/2, 0<=i,k<b.

Let fP,fE,fL be its positive, exponential, and logarithmic forcing columns; fQ=fE+fL. These are precisely the forcings used in the contact reconstruction.

Fix the integral row normalization from the existing local arithmetic:

    C=diag(2^n(n+i)!),
    M=C T,
    P=C fP,
    E=C fE,
    L=C fL,
    Z=E+L,
    Delta=det M.

All these normalized matrices and columns are integral. Set

    s_i=(n+i)!/n!,
    H_i=2^n[z^(n+i)]Q0(z)^n/(1-z)^(n+1),
    V_i=s_i H_i.

Here H_i and V_i are integers, and the positive forcing has the exact uniform column factor

    P=(n!)^2 V.                                             (1)

This factor is not removed from Z. The two forcings have different factorial scales.

Let Aop=D_B(D+1)^(-n), an integer (b+1) by b reconstruction matrix. For j>=1 let a_j be its row j. Define

    X_j=a_j adj(M)V,
    Y_j=a_j adj(M)Z,
    N_(j,1)=(n!)^2 X_j,
    N_(j,2)=Y_j.

Then, for the positive coordinates used by Jelig,

    u_j=(n!)^2 X_j/Delta,
    v_j=Y_j/Delta.                                          (2)

There is no additive endpoint term in these rows. At j=0 the term Delta must instead be included in N_(0,2); that coordinate is not used by our eligible selection.

For X_j!=0, the actual denominator and its raw coordinate gcd are

    G_j=gcd((n!)^2|X_j|,|Y_j|),
    q_j=(n!)^2|X_j|/G_j.                                   (3)

Delta cancels from the quotient. This is the actual reduced q_j, not a lift denominator.

## 3. Canonical primitive selector: exact removal of row-clearing content

The actual rational selector row for coordinate j>=1 is a_j T^(-1). A primitive integral representative can be obtained without retaining the common factorial row clearer.

Define the integer row

    B_j=a_j adj(M) diag(s_i),
    eta_j=gcd_i |(B_j)_i|>0,
    l_j=B_j/eta_j.

Choose its overall sign, if desired, by making the first nonzero coefficient positive. This sign has no effect on its height, absolute normalization, or center. With the displayed un-oriented choice the exact selector identity is

    a_j T^(-1)=(2^n n! eta_j/Delta) l_j.                    (4)

Thus l_j is the canonical primitive integer selector up to sign. Its polynomial and height are

    L_j(t)=sum_(i=0)^(b-1) (l_j)_i t^i,
    Hsel_j=sum_i |(l_j)_i|.

Its degree is at most b-1. Its correction term is exactly zero, because j>=1. These are the selector/correction quantities to be compared with Child 1's canonical budget; no particular implementation or filename of a pending normalization package is assumed.

The integer normalization from the newly reviewed obstruction is

    Usel_j=2^n D_t^n[(t^2-t+1/2)^n L_j(t)]_(t=1)/n!.

Using (1) and (4), or directly V_i=s_i H_i, gives the particularly simple identity

    X_j=eta_j Usel_j.                                      (5)

In particular eta_j divides X_j, and Aselector_j=|Usel_j|=|X_j|/eta_j is a positive integer on the eligible set. The selector forcing is exactly

    l_j fP=(n!/2^n) Usel_j.

The original integer selector numerator a_j adj(M)C has content exactly 2^n n! eta_j. Counting that common factorial again as selector height would be incorrect.

There is also an exact elementary restriction on eta_j. Let k_j be the gcd of the entries of a_j adj(M). Since the positive reconstruction rows form the product of two unimodular b by b matrices, each a_j is primitive. Multiplication by M then gives

    k_j|Delta.

Since s_i|s_(b-1) for every i,

    k_j|eta_j|s_(b-1) k_j,
    hence eta_j|s_(b-1)|Delta|.                            (6)

The first assertion follows because every entry of B_j is a multiple of k_j. For the second, eta_j divides s_i(a_j adj(M))_i and therefore divides s_(b-1)(a_j adj(M))_i for every i; take their gcd. These assertions concern the primitive selector content and do not assert that eta_j divides Y_j.

For comparison, the full coordinate-zero center would have rational correction 1/u_0=Delta/((n!)^2X_0), with reduced denominator

    (n!)^2|X_0|/gcd((n!)^2|X_0|,|Delta|).

That correction denominator cannot be discarded in the height obstruction. Our proved nonempty eligible set avoids it entirely.

## 4. Exact residual factorial gcd

The following factorization separates residual positive-column content from cancellation of the explicit factorial in (1). For X_j!=0 put

    K_j=gcd(|X_j|,|Y_j|),
    x_j=X_j/K_j,
    y_j=Y_j/K_j,
    F_j=gcd((n!)^2,|y_j|).

Then gcd(|x_j|,|y_j|)=1, and exactly

    G_j=K_j F_j,
    q_j=((n!)^2/F_j)|x_j|.                                (7)

Indeed gcd((n!)^2 x_j,y_j)=gcd((n!)^2,y_j). This includes Y_j=0: then |x_j|=1, F_j=(n!)^2, and q_j=1.

For any prime p, write f_p=v_p(n!), x=v_p(X_j), y=v_p(Y_j), with v_p(0)=infinity. The full local statement is

    v_p(G_j)=min(2f_p+x,y),
    v_p(q_j)=max(0,2f_p+x-y).                              (8)

The variables in (8) concern the complete second contraction, not only its exponential part. Formula (7) is invariant as a quotient under a common enlargement of the original row clearers; such enlargement changes the separate raw contents and is not a gain.

Combining (5) with K_j also isolates the primitive selector's remaining cancellation. Put rho_j=gcd(eta_j,|Y_j|). Then

    K_j=rho_j gcd(|Usel_j|,|Y_j|/rho_j).                    (9)

The proof divides eta_j and Y_j by their gcd before taking the remaining gcd. Formula (9) is exact; neither residual factor is assumed to be one.

The unresolved global content is now explicit: K_j, and the part F_j of the factorial that divides the primitive complete second contraction. The local theorem below proves that neither contains a factor 13 on a full progression of eligible coordinates.

## 5. Local transfer domain and the one new residue gate

Use the existing Toeplitz local transfer only with

    p odd, p>2b+3, p>=3b,
    n=ap+r, a>=1,
    b<=r<=floor((p-b)/2).

In this domain the retained source proves

    M(n)=2^a M(r) mod p,
    V(n)=2^a h_a V(r) mod p,
    Z(n)=2^a E(r) mod p,

where

    h_a=[w^a]Q0(w)^a/(1-w)^(a+1).

The last congruence uses the vanishing of the complete normalized logarithmic forcing modulo p for a>=1. It uses E(r), not Z(r). The scalar h_a is retained and is not presumed a unit.

Choose b=3, p=13, r=3. All domain restrictions hold: 13>9, 13>=9, and 3<=3<=5. The new exact residue calculation returned

    M(3) mod 13 = [[12,5,8],[8,9,7],[11,1,6]],
    det M(3) mod 13 = 7,
    E(3) mod 13 = (6,0,1)^T,
    V(3) mod 13 = (6,5,11)^T.

The positive-coordinate reconstruction matrix is exactly, for arbitrary n,

    Aplus(n)=[[1,-n-1,n(n+3)],
              [0,1,-2n-1],
              [0,0,1]].

It consists of rows j=1,2,3 of Aop, and is unimodular. At n=3 it is

    [[1,-4,18],[0,1,-7],[0,0,1]].

The calculated contraction vectors were

    Aplus(3) adj(M(3)) V(3) = (1,10,1)^T mod 13,
    Aplus(3) adj(M(3)) E(3) = (8,3,3)^T mod 13.          (10)

Every asserted value in (10), the matrix, determinant, and forcing vectors was checked in the one successful exact execution. The seed n=3 is residue data; it is not presented as an analytically eligible large-n approximation. No other prime or residue was scanned.

For n=13a+3, the integer polynomial matrix Aplus(n) reduces to Aplus(3). The adjugate of a scalar multiple of a 3 by 3 matrix gains the square of that scalar. Therefore the retained transfer gives, at every a>=1,

    Delta(n)=2^(3a)*7 mod 13,
    (X_1,X_2,X_3)^T
       =2^(3a) h_a (1,10,1)^T mod 13,
    (Y_1,Y_2,Y_3)^T
       =2^(3a)(8,3,3)^T mod 13.                        (11)

In particular Delta and all three complete Y_j are 13-adic units, without any assumption on h_a. Equation (11), not sampling of large indices, supplies the all-index conclusion.

## 6. Actual factorial contribution for every eligible coordinate

Theorem. Fix b=3, m=1. For every n>=2^22 with n=3 mod 13, and every j in the retained nonempty set Jelig,

    v_13(G_j)=0,
    v_13(q_j)=2v_13(n!)+v_13(X_j)>=2v_13(n!).           (12)

Equivalently,

    13^(2v_13(n!)) divides q_j.

Proof. Here n=13a+3 with a>=1, so (11) makes Y_j a unit. Eligible coordinates have X_j!=0. Formula (8) proves (12). The same argument shows that both K_j and F_j in (7) are 13-adic units.

The analytic domain is genuine and explicit. At n=2^22,

    512*3^4 log n < 41472*22 < 2^22.

Since n/log n is increasing for n>e, every n>=2^22 satisfies n>=512*3^4 log n. Thus normality, the rational eligibility rule, and the complete coordinate envelope all hold on this unbounded progression. No arithmetic conclusion is being attached to an unspecified or empty eligible set.

Since v_13(n!)=n/12-O(log n), every such eligible coordinate satisfies

    log q_j >= (log 13)n/6-O(log n).                    (13)

This lower exponent is strictly less than log 2, since 13<2^6. It does not by itself close the direct coordinate envelope criterion.

There is an explicit unbounded subset with an exact valuation. Set

    n_s=13^(s+1)+3, s>=5.

Its high block is a=13^s. In characteristic 13, Frobenius gives

    Q0(w)^a/(1-w)^(a+1)
       =Q0(w^a)/[(1-w^a)(1-w)].

Since Q0(y)/(1-y)=1+y^2/[2(1-y)], its coefficient at w^a is one. Hence

    h_(13^s)=1 mod 13.

All three X_j in (11) are now units. Consequently every positive coordinate j=1,2,3 is defined, and every analytically eligible one satisfies

    v_13(q_j)=2v_13(n_s!)=(n_s-4)/6,
    v_13(G_j)=0.                                      (14)

The equality for the factorial follows directly from the base-13 expansion:

    v_13(n_s!)=(13^(s+1)-1)/12.

The choice s>=5 ensures n_s>2^22. This proof handles the high-block scalar explicitly rather than treating it as a unit without justification.

## 7. What the local theorem says about the canonical selector

On n=13a+3, b=3, the three values s_i=(n+i)!/n!, i=0,1,2, are 13-adic units. Delta is a unit by (11). Formula (6) therefore gives

    v_13(eta_j)=0, j=1,2,3.                            (15)

The unreduced integral selector row in (4) has gcd 2^n n! eta_j, whose exact 13-adic valuation is v_13(n!). This factor is removed by canonical primitive normalization.

On the explicit subset n_s, equations (5), (11), and (15) give

    v_13(Usel_j)=0,
    v_13(N_(j,1))=2v_13(n_s!),
    v_13(N_(j,2))=0.                                   (16)

Thus the primitive selector's integer forcing normalization is a unit at 13 even though its coordinate denominator retains two factorial valuations. The factorial contribution cannot be explained away by replacing q_j with a primitive selector clearer or a full-lift denominator.

For the complete original coefficient lattice, the retained unsquared-minor formula is

    G_j=|Delta| h_j/d,
    q_j=g1|xi_j|/h_j,
    h_j=r_j e_j, e_j|chi,

with d,chi,g1,xi_j,h_j,r_j as in the completed coordinate paper. Here Delta is our fixed normalized Toeplitz determinant. The new unit result therefore implies, on the whole progression,

    v_13(h_j)=v_13(d)

for every eligible coordinate. On n_s it additionally gives

    v_13(g1 xi_j)=v_13(d)+2v_13(n_s!).                  (17)

These equations retain the rational scale |Delta|/d. They do not assume that scale is an integer or set any projected-minor content to one. They connect the new factorial result with the already established unsquared-coordinate description.

## 8. Global selector-height requirement for a successful coordinate bound

The narrow review proves the all-size inequality for the primitive selector of an eligible positive coordinate, with no rational correction:

    (2+epsilon)log q_j
      >=log(n!)-log Hsel_j
        -(1+epsilon)log Aselector_j-O_epsilon(n+b).    (18)

The exact inputs here are Hsel_j=||B_j||_1/eta_j and Aselector_j=|X_j|/eta_j. They are not heights of an arbitrary cleared row.

The forcing height estimate gives

    log Aselector_j <= log Hsel_j+O(n+b).

Substitution into (18) yields a useful unconditional height-denominator tradeoff:

    (2+epsilon)(log q_j+log Hsel_j)
      >=log(n!)-O_epsilon(n+b).                        (19)

In particular, along a slow-growth sequence, log q_j=O(n) forces

    liminf log Hsel_j/(n log n)>=1/2.                  (20)

No a priori upper bound on log Hsel_j is needed for (20); for each fixed epsilon it follows directly from (19), then epsilon decreases to zero. If the stronger finite factorial-scale bounds on both log Hsel_j and log Aselector_j hold, the reviewed combined necessary budget also gives

    liminf (log Hsel_j+log Aselector_j)/(n log n)>=1.

A sequence satisfying the sufficient coordinate-envelope condition q_j delta_coord->0 necessarily has log q_j=O(n), because log delta_coord=-n log 2+o(n). It therefore must use canonical primitive selectors of at least the factorial-scale height in (20). This is a concrete restriction on the actual reconstructed selectors; their degree b-1 is small but their primitive coefficient height cannot also be small in a successful low-denominator route.

For completeness, the sharper non-asymptotic obstruction can be written directly as an upper bound on the raw coordinate gcd. Let D_N be the moment clearer from the selector review, with N=2n+deg L_j. Then

    G_j <= (n!)^2 |X_j| *
      [27(2(1+sqrt(2)))^n Hsel_j Aselector_j^(1+epsilon)
          D_N^(2+epsilon)/(C_epsilon(n+1)n!)]^(1/(2+epsilon)).

It is useful only when its actual primitive height terms are controlled. This limitation is explicit; an enlarged row clearer does not improve it.

No signed asymptotic for these coordinate errors is asserted. The scalar divergence theorem cannot be transferred to them. The height restriction alone therefore does not prove divergence of their actual primitive forms.

## 9. The remaining local lemma and global content

The new theorem settles one nontrivial factorial contribution for every eligible coordinate on the stated progression. It does not control the other prime factors in (7). Even on n_s the full denominator is only factored as

    q_j=13^((n_s-4)/6) q_j^(13),
    gcd(q_j^(13),13)=1,

with q_j^(13) unresolved. The actual denominator may have much larger growth than the established 13-adic contribution.

For a further prime in the valid Toeplitz transfer domain, the local problem is concrete. Determine, for a coordinate that remains analytically eligible,

    X_j=a_j adj(M)V,
    Y_j=a_j adj(M)(E+L).

One sufficient first-order lemma is nonvanishing modulo p of the reconstructed exponential seed a_j(r)adj(M(r))E(r). It makes the complete Y_j a unit for all admissible high blocks. Then the entire factor p^(2v_p(n!)) survives in q_j whenever X_j!=0. Exact equality additionally requires nonvanishing of h_a a_j(r)adj(M(r))V(r). The latter cannot be assumed, and the high-block scalar must remain.

If these seed contractions vanish, a first-order statement is insufficient. The required higher-depth lemma must determine the first nonzero coefficient of the COMPLETE Y_j at the threshold 2v_p(n!)+v_p(X_j). The logarithmic depth bound permits omission of L only below its proved valuation, namely at least 2v_p(n!)-floor(log_p(2n+b-1)) for its normalized entries. Multiplication by the integer adjugate and reconstruction row preserves that lower bound. At or above the threshold where L reappears, its cancellation with E must be retained.

Such a lemma must apply to the eligible coordinates, or to all j>=1 as our p=13 gate does. A statement merely guaranteeing a unit at some unrelated row would not meet the analytic selection requirement. For b increasing, fixed p=13 no longer satisfies p>2b+3 and p>=3b; no transfer beyond that domain is claimed.

Globally the outstanding factors are precisely K_j and F_j in (7), or the equivalent primitive-selector factors in (9), together with Hsel_j. Proving upper denominator control would require sufficiently large actual cancellation in those factors; proving stronger lower growth would require further surviving factorial factors. Neither outcome follows by counting clearers or assuming random coprimality.

## 10. Status and provenance

Proved here: the canonical primitive selector formula (4), its integral forcing normalization (5), exact factorial/content decomposition (7), the single-gate transfer (11), the all-eligible factorial theorem (12), exact subfamily law (14), and their connection to selector heights and the retained unsquared-minor normalization.

The residue data came from one new successful exact calculation at p=13,b=r=3. All infinite conclusions use the existing domain-restricted transfer and the additional paper arguments above. No finite computation is presented as an asymptotic proof.

The limited direct-selector review is separate. Its rational-correction asymptotic conclusions explicitly retain degree=o(n log n); its saddle-family corollary remains conditional on Agent 2's author asymptotic. The completed LOG_TWO_INVERSE_REVIEW, COORDINATE_CENTER_ARITHMETIC, and their file operations were not repeated.

The sufficient conditions q_j->infinity and q_j delta_coord->0 remain unresolved for this coordinate route. The new factorial law does prove divergence of q_j on the explicit progression, but its lower exponential rate is below log 2 and supplies no adequate upper bound. A failed sufficient bound is not an exclusion of actual small forms. No conclusion about the rationality of e+pi is claimed.
