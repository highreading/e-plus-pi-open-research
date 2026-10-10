> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Joint coordinate content and eligible selection

New original paper arithmetic. The effective-content paper, its rank-one exclusion, its exact factorization, and its uniform bound log B_j <= 2n log n+O(n) are preserved. No previous review or computation is repeated. This stage proves joint identities and prime-power restrictions, not an improved asymptotic rate.

## 1. Domain and the actual shared matrix

Throughout n=13^(s+1)+3, s>=5, b=3, with eligibility weight parameter m=1. Index the three positive coordinates by i=0,1,2, corresponding to the previous j=i+1. The rational eligible set E is a nonempty subset of these indices. Statements about approximation or selected denominators always retain E.

Retain the actual matrices from COORDINATE_EFFECTIVE_CONTENT_BOUNDS.md:

Nmat=Qd^T M Aplus^(-1), det Nmat=Delta !=0.

Both outer changes of basis are integral unimodular. Write its rows as x,y,z, where z=(z_0,z_1,z_2). Define

W=adj(Nmat)[:,{0,1}],
W_i=(w_(i,0),w_(i,1)).

These are exactly the previously identified cofactor pairs. Every W_i is nonzero, because its endpoint contraction X_i is nonzero on this family.

Use the retained positive integers

nu_i=gcd(|z_k|,|z_l|), {k,l}={0,1,2}\{i},
k_i=content(row i of adj(Nmat)),
G_i=gcd(k_i,nu_i), kappa_i=k_i/G_i,
ell_i=nu_i kappa_i.

The smaller pair and its remaining content are

T_i=(Pbar_i,Qbar_i)=W_i/ell_i,
tau_i=content(T_i)=gcd(G_i,Pbar_i,Qbar_i), tau_i | G_i.

Thus

rho_i=content(W_i)=ell_i tau_i,
v_i=T_i/tau_i,
content(v_i)=1.

Here v_i is a two-component integer row, not the second endpoint-lift column used elsewhere. The earlier effective content is exactly

r_i=rho_i epsilon_i, epsilon_i | h, h=(n+1)(n+2).

This note does not count k_i, selector content, or shared content again after this factorization.

## 2. Joint adjugate identities

The identity Nmat adj(Nmat)=Delta I gives

x W=(Delta,0), y W=(0,Delta), z W=(0,0).                 (1)

In particular

sum_i z_i W_i=0.                                       (2)

Jacobi's complementary-minor identity gives the three exact minors

det(W_0,W_1)=Delta z_2,
det(W_0,W_2)=-Delta z_1,
det(W_1,W_2)=Delta z_0.                                (3)

For completeness, each identity follows by taking the indicated two rows and first two columns of adj(Nmat). The complementary entry of Nmat is in its third row; the middle case has the negative complementary sign. Thus no new matrix or unrelated pair has been substituted.

Let

g_z=gcd(|z_0|,|z_1|,|z_2|)>0,
c_W=content(W)=gcd(rho_0,rho_1,rho_2).

At least two entries of z are nonzero. Otherwise (2) would make one W_i zero. Equations (1)-(3) prove

g_z | c_W | |Delta|,
Delta_2(W)=|Delta| g_z,
c_W^2 | |Delta| g_z.                                  (4)

The first divisibility holds because every entry of W is a minor containing the third row of Nmat. The second follows from the two nonzero entries Delta in (1). The last follows either from the Smith divisors or by dividing every entry of W by c_W before taking its minors. The Smith divisors of W are exactly

c_W, |Delta|g_z/c_W.

Consequently the primitive shared matrix W/c_W has determinantal divisor |Delta|g_z/c_W^2. This separates shared content from row-specific surplus. It gives no permission to multiply c_W into the already complete products rho_i.

The two earlier effective coordinates form the row matrix W F^T, where

F=[[2n+3,(n+1)(n+2)/2],[-2,0]], det F=h.

Hence

Delta_2(W F^T)=h |Delta|g_z,
c_W | content(W F^T) | h c_W.                         (5)

This is the full joint effect of the nonunimodular quotient map. In particular

r_i r_j | h |Delta z_k|                               (6)

for complementary indices, with divisibility into zero interpreted normally. The factor h cannot also be treated as an independent extra content saving in the individual formulas.

The transformations defining Nmat preserve the full determinantal divisors of M. In particular gcd_i k_i=Delta_2(Nmat)=Delta_2(M). As another joint restriction, if c_k is the gcd of column k of Nmat, complementary minors of the full adjugate give

k_i k_j | |Delta| c_k.                               (7)

These shared divisors and the row-specific k_i remain different quantities.

## 3. Residual contents in different rows share only g_z

This restriction uses the actual common third row, beyond a generic matrix dimension argument. Write z=g_z zhat with zhat primitive, and put

eta_i=gcd(|zhat_k|,|zhat_l|), so nu_i=g_z eta_i.

For distinct i,j,

gcd(eta_i,eta_j)=1,
gcd(nu_i,nu_j)=g_z.                                  (8)

Indeed any divisor of both complementary gcds divides all three entries of zhat. This remains valid if one entry of z is zero, since the other two are nonzero and their primitive gcd is one.

Since tau_i | G_i | nu_i, equation (8) proves the new residual-content obstruction

gcd(tau_i,tau_j) | g_z.                              (9)

Equivalently, for any prime p, put z_p=v_p(g_z) and t_i=v_p(tau_i). Then

min(t_i,t_j)<=z_p for every distinct pair.            (10)

At most one row can have t_i>z_p. In particular, outside the primes dividing g_z, at most one row has any residual tau-content at that prime. The excess factors tau_i/gcd(tau_i,g_z) are pairwise coprime.

This concerns the remaining tau_i, not all of rho_i or r_i. Two rows may still have large contents through k_i or the already isolated factors ell_i. Promoting (9) to pairwise coprimality of the entire effective contents would be false.

## 4. Exact minors of the smaller pairs

Define the integer minors

m_ij=det(T_i,T_j), i<j.

Because W_i=ell_i T_i, equation (3) gives

m_01=Delta z_2/(ell_0 ell_1),
m_02=-Delta z_1/(ell_0 ell_2),
m_12=Delta z_0/(ell_1 ell_2).                         (11)

Each displayed quotient is an integer, by its left side. Dividing rows by ell_i is not unimodular: equation (11) records its exact effect instead of claiming preservation of the minor ideal.

The remaining common divisibility satisfies

tau_i tau_j | m_ij,
det(v_i,v_j)=m_ij/(tau_i tau_j).                     (12)

For a prime p and a nonzero m_ij,

t_i+t_j <= mu_ij, mu_ij=v_p(m_ij).                   (13)

Together with 0<=t_i<=v_p(G_i) and (10), these are explicit necessary conditions on simultaneous large residual content. They apply to the actual smaller cofactor pairs, at their already reduced precision.

For all three rows,

Delta_1(T)=gcd(tau_0,tau_1,tau_2),
Delta_2(T)=gcd(|m_01|,|m_02|,|m_12|),
Delta_1(T)^2 | Delta_2(T).                           (14)

If all three m_ij are nonzero, adding (13) gives

2(t_0+t_1+t_2)<=mu_01+mu_02+mu_12.                  (15)

The minors also give the exact vector relation

m_12 T_0-m_02 T_1+m_01 T_2=0,
sum_i z_i ell_i T_i=0.                              (16)

The two displayed relations agree by (11). A further useful primewise condition follows: among the finite numbers

v_p(z_i)+v_p(ell_i)+t_i, for z_i !=0,                (17)

the minimum is attained at least twice. If it were unique, division of (16) by that power of p would leave a nonzero primitive vector as its sole nonvanishing term modulo p. If just two z_i are nonzero, their two values in (17) are equal.

Conditions (10), (13), and (17) restrict different aspects of the same joint content. They are necessary, not a claim that scalar minor valuations alone suffice to reconstruct the two vector congruences defining every tau_i.

If m_ij=0, the corresponding primitive vectors v_i,v_j are equal up to sign. This is a genuine degeneracy, not a useful finite valuation bound. Under the invertible companion map below it gives identical logarithmic companions and hence B_i=B_j. At least one minor involving each row is nonzero, since W has rank two and no row vanishes.

## 5. Final reduced denominators and joint output cancellation

Retain the integral universal map

Vmat=[[O U_0,O(n+1)U_1],[J_0,(n+1)J_1]],
dV=Delta_1(Vmat), Vprim=Vmat/dV,
D_V=det(Vprim)=O^2 2^(2n+1)/dV^2>0.

Its determinant and rank were proved in the preserved effective-content note. Define the unreduced outputs of the smaller pairs by

(A_i,C_i)^T=Vprim T_i^T,
(Theta_i,Phi_i)^T=Vprim v_i^T.

Thus (A_i,C_i)=tau_i(Theta_i,Phi_i), and exactly

A_i=O X_i/(dV ell_i),
C_i=O R_i/(dV ell_i), R_i=L_i/(n!)^2.

All these output entries are integers. Since X_i!=0, A_i and Theta_i are nonzero. With

e_i=gcd(|Theta_i|,|Phi_i|), e_i | D_V,

full cancellation gives

B_i=|Theta_i|/e_i
   =|A_i|/(tau_i e_i)
   =O|X_i|/(dV ell_i tau_i e_i).                    (18)

The common content of (A_i,C_i) is exactly tau_i e_i. Counting tau_i and then this full output content as independent gains would double-count it.

Taking two output rows yields

A_i C_j-C_i A_j=D_V m_ij,
(tau_i e_i)(tau_j e_j) | D_V m_ij.                  (19)

For nonzero m_ij, the reduced rational companions gamma_i=R_i/X_i satisfy the exact integer identity

B_i B_j |gamma_j-gamma_i|
 = |D_V m_ij|/(tau_i e_i tau_j e_j) in Z_(>0).       (20)

It concerns gamma_i, not the full coordinate center alpha_i+gamma_i, and does not transfer to Gram centers.

Here are precise denominator obstructions in terms of the smaller pairs. Fix p, and put

d_p=v_p(D_V), a_i=v_p(A_i), f_i=v_p(e_i),
g_i=v_p(G_i), b_i=v_p(B_i).

Then

b_i=a_i-t_i-f_i, 0<=f_i<=d_p,
t_i+t_j+f_i+f_j<=d_p+mu_ij                         (21)

for each nonzero minor. Consequently

b_i+b_j >= a_i+a_j-d_p-mu_ij.                       (22)

This forces a contribution in at least one member of a pair when its right side is positive. It does not force it in both, and does not bound the minimum over the pair from below.

For a criterion that really applies to every eligible row, define

c_i(p)=min(g_i, min_(j!=i, m_ij!=0) mu_ij).

The inner set is nonempty. Equations (13) and (21) imply

b_i >= max(0,a_i-c_i(p)-d_p).                       (23)

Therefore, with the actual eligible set E,

p^L_p divides B_i for EVERY i in E,
L_p=min_(i in E) max(0,a_i-c_i(p)-d_p).              (24)

The product over primes of these compulsory factors also divides every eligible denominator. This is an exact, explicit joint prime-power obstruction. No claim that its logarithm has a positive new asymptotic rate is made; that would require estimates on the indicated output depths and minors.

A useful special case of (9) is: if p divides neither D_V nor g_z, then e_i is a unit for every row, and at least two rows satisfy t_i=0. On those rows b_i=a_i exactly. Even if all three a_i are positive, this proves a denominator contribution in at least two rows, not necessarily in a singleton eligible set. To force it in every eligible row, one can for example establish G_i prime to p for every i in E, or use the explicit positive lower bound (23) there.

## 6. Precision for simultaneous content tests

Let lambda_i=v_p(ell_i). The exact defining test is

t_i>=r iff T_i=(0,0) mod p^r
        iff W_i=(0,0) mod p^(lambda_i+r),
1<=r<=g_i.                                         (25)

Knowing T_i modulo p^g_i determines the capped exponent t_i. If both coordinates vanish at the cap, t_i=g_i because tau_i | G_i. Simultaneous tests on two or three rows retain each row's own lambda_i; they do not replace those losses by an unjustified common normalization.

After tau_i is removed, obtaining v_i modulo p^k requires W_i modulo p^(lambda_i+t_i+k), with exact division by the known factors and their unit parts. In particular the residual output gcd e_i is determined from v_i modulo p^d_p. Computing the exponent of Theta_i itself is a separate first-nonzero-digit task, even when d_p=0.

To compute m_ij modulo p^k, it suffices to compute T_i and T_j modulo p^k, hence W_i and W_j at respective precisions p^(lambda_i+k) and p^(lambda_j+k). Determining a finite mu_ij from modular data requires finding its first nonzero digit, through p^(mu_ij+1). An identically zero minor is instead identified by the exact condition z_k=0 in (11).

All statements include p=2. No nonunit division is hidden. The already proved 13-primary layer is retained and is not recalculated in this stage.

## 7. Why the eligible minimum does not improve from these identities alone

There are two different issues. First, bounds such as (13) and (19) are upper restrictions on simultaneous cancellation. They may force one or more denominators to remain large, but do not force a row with a small denominator to exist. Second, even an existence statement among all three rows must be connected to E before it can improve min_(i in E) B_i.

The eligibility rule itself can produce a singleton. Let lambda=n+2, omega_j=(lambda)_j for positive coordinates j=1,2,3, and c_lambda=sum omega_j^(-2). In terms of the nonzero endpoint contractions it is

3(1+c_lambda)omega_j^2 X_j^2
 >= X_0^2+sum_(k=1)^3 omega_k^2 X_k^2,
X_0=-X_1-X_2-X_3.                                  (26)

Fix any preferred j, hold the other two positive X values nonzero and fixed, and let |X_j| tend to infinity. The other two eligibility inequalities eventually fail. The j inequality holds because its limiting comparison is

3(1+c_lambda)omega_j^2 > 1+omega_j^2.

Thus the rule allows E={j}, for any j. One may also vary X_j through any prescribed nonzero residue class modulo 13 and keep the other two in prescribed nonzero classes. Consequently nonvanishing and the retained first-order residue information alone do not rule out singleton eligibility.

This is a statement about what the rational rule and those data imply. It does NOT assert that a singleton has been exhibited for the actual Toeplitz matrices at some n_s. A theorem excluding singleton eligibility on that family would require additional information about its actual archimedean endpoint ratios.

There is also a concrete limitation of the joint cofactor identities themselves. Fix an allowed even n and consider the auxiliary integer matrices

N*(T,L)=[[1,0,0],[0,1,0],[-L,-(L+1),T]], T,L positive.

Their first two adjugate columns are

W*=[[T,0],[0,T],[L,L+1]], det N*=T.                  (27)

They satisfy all the joint adjugate identities (1)-(4). They can be put through the identical integral reconstruction changes by defining M*=Qd^(-T)N* Aplus. This is an algebraic countermodel, not the actual exponential Toeplitz M and not an HP approximation example.

The first two rows have content T and companions independent of T,L. The third row has content one. Put u=U_0>0 and v=(n+1)U_1>0. The three endpoint contractions are

uT, vT, uL+v(L+1).

For fixed n,T and L tending to infinity, (26) selects only the third row. Under Vprim its first output is a positive affine function of L; its reduced output gcd is at most D_V. Therefore B_3 tends to infinity while B_1 and B_2 remain fixed. This proves that shared reconstruction, joint minor identities, and the eligibility inequality alone do not justify selecting one of the two content-favorable rows. It does not contradict the preserved n-dependent bound for the actual family, since the auxiliary matrices are not its Toeplitz matrices.

## 8. The additional relation needed for selection or universal obstruction

For a proposed upper threshold H_n, define the actual favorable set

Good(H_n)={i: O|X_i| <= H_n dV ell_i tau_i e_i}.

Equation (18) makes the required condition exact:

min_(i in E) B_i <= H_n iff E intersects Good(H_n).  (28)

One must prove this intersection from the actual family. A sufficient counting statement is |E|+|Good(H_n)|>3. If E can be a singleton, a direct eligibility/content relation is needed for its unique row. Existence of a preferred favorable row elsewhere does not suffice.

At the factorial scale, the preserved relation and epsilon_i | h give

log B_i=log|X_i|-log rho_i+O(n).

Thus an improved upper rate beta requires an eligible row with

log(|X_i|/rho_i) <= beta n log n+O(n),              (29)

uniformly along the intended sequence. The new joint restrictions do not establish this intersection. They constrain how often large tau-content can occur, rather than guaranteeing that an eligible endpoint has enough total cancellation.

For a lower obstruction on the eligible minimum, the direction of quantifiers is different: every i in E must satisfy the required lower estimate. Equations (23)-(24) provide a sufficient primewise condition. A theorem that at least one, or even at least two, of the three denominators are large does not itself lower-bound their eligible minimum. Even |E|>=2 would only force an intersection with a two-row large-denominator set, not containment in it.

## 9. Completed stage and unresolved rate

The new results are the exact joint minor and relation identities for the actual cofactor pairs; the separation of shared content c_W and g_z from row-specific content; the residual restriction gcd(tau_i,tau_j)|g_z; the reduced-minor bounds (11)-(17); the final-output restrictions (19)-(24); and the explicit precision and eligibility limitations.

No improved uniform rate for min_(i in E) B_i is established. No new prime factor is proved to divide every eligible denominator unconditionally beyond the retained results. Instead (24) specifies exactly a sufficient joint obstruction, using the actual smaller pairs, their minors, and output depths. Its asymptotic strength remains undecided.

The bound log B_i<=2n log n+O(n) remains valid for every eligible row. Rank one remains excluded. The known 13-primary depth remains retained. The unresolved inputs are actual all-prime cofactor congruences and their relation to the rational eligibility inequalities. No Gram transfer, broad scan, numerical evidence, or irrationality conclusion is claimed.
