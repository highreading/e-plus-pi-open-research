> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Combined coordinate companion: cancellation and the 13-adic ledger

This note completes original paper deductions from ELIGIBLE_COORDINATE_GCD.md, agent1/RECONSTRUCTED_SELECTOR_HEIGHT.md, and ../COMBINED_COMPANION_DENOMINATOR_DRAFT.md. It uses their already established identities and the previously executed single residue gate; it does not rerun that gate or claim a new numerical experiment.

## Exact coordinate decomposition

Use the integer clearing and reconstruction notation of ELIGIBLE_COORDINATE_GCD.md:

Cclear=diag(2^n(n+i)!), M=Cclear T, Delta=det M,
P=Cclear fP=(n!)^2 V, E=Cclear fExp, Lnorm=Cclear fLog.

Write Ffac=(n!)^2. For reconstruction row a_j put

X_j=a_j adj(M)V,
E_j=a_j adj(M)E,
L_j=a_j adj(M)Lnorm,
Z_j=L_j+delta_(j,0) Delta.

Then u_j=Ffac X_j/Delta and v_j=(E_j+Z_j)/Delta. For u_j!=0,

alpha_j=E_j/(Ffac X_j),
r_j+beta_j=Z_j/(Ffac X_j),
t_j=v_j/u_j=alpha_j+r_j+beta_j.

The correction r_j is zero for j>=1. At j=0 it equals Delta/(Ffac X_j), and must be included before reduction. This notation for r_j is the rational correction, not a row gcd used in other notes.

Put Dcoord=Ffac |X_j|. The THREE actual reduced denominators are

Qexp_j=Dcoord/gcd(Dcoord,|E_j|),
B_j=den(r_j+beta_j)=Dcoord/gcd(Dcoord,|Z_j|),
q_j=den(t_j)=Dcoord/gcd(Dcoord,|E_j+Z_j|).

All gcds are positive; gcd(Dcoord,0)=Dcoord. A zero rational numerator thus gives denominator 1. There is no asserted product identity among these three denominators.

For the rationally eligible positive coordinates, the deciding gcd is exactly

Glog_j=gcd(Ffac |X_j|,|L_j|),
B_j=Ffac |X_j|/Glog_j.

It differs from the previously studied total-coordinate gcd gcd(Ffac |X_j|,|E_j+L_j|).

## Primitive selector and polynomial content

Let s_i=(n+i)!/n!, C_j=a_j adj(M)diag(s_i), eta_j=content(C_j)>0, and let l_j=C_j/eta_j be the primitive selector coefficient row. The reconstructed-selector identities give

Hsel_j=||C_j||_1/eta_j,
Usel_j=X_j/eta_j,
A_j=|Usel_j|,
Hsel_j/A_j=||C_j||_1/|X_j|.

Thus reconstruction-row content eta_j cancels from the height-to-endpoint ratio. Its removal does not establish a small ratio.

For the polynomial selector construction Ksel=2^n t^n D^n(Vpoly^n Lsel)/n!, Vpoly=t^2-t+1/2, let g_j=content(Ksel)>0, K0=Ksel/g_j, U0=K0(1). This polynomial content is distinct from eta_j and from other row gcds. Choose any positive integer moment clearer D such that

Jmoment=D calL((K0-U0)/(t-1))

is integral. For positive coordinates,

X_j=eta_j g_j U0,
L_j=Ffac eta_j g_j Jmoment/D,
B_j=D |U0|/gcd(D |U0|,|Jmoment|).

These equalities exhibit full cancellation of both row and polynomial content in the rational companion. Enlarging D multiplies both entries of the gcd by the same factor and does not change B_j.

More generally, for r=a/v with v>0 and beta=Jmoment/(D U0),

B=v D |U0|/gcd(v D |U0|,|a D U0+v Jmoment|).

This is the combined correction formula; den(r) den(beta) is only an upper bound. Coordinate zero and Gram centers require their own corrections and cannot inherit r=0 from positive coordinates.

## Fixed progression and hypotheses

Now fix b=3, the admissible weight parameter m=1, and

n>=2^22, n=3 (mod 13).

Here the prior normality/envelope results apply, the rational eligible set is nonempty, and every eligible row has j in {1,2,3} and X_j!=0. Eligibility is determined from rational lift data, without evaluating e+pi. The claims below apply to every such row, including one chosen by minimizing the actual q_j.

Set a=(n-3)/13, f=v_13(n!), x_j=v_13(X_j), and h=floor(log_13(2n+2)). Inherited transfer plus the executed b=r=3, p=13 gate gives

Delta=7*2^(3a) (mod 13),
(X_1,X_2,X_3)=2^(3a) h_a (1,10,1) (mod 13),
(E_1,E_2,E_3)=2^(3a)(8,3,3) (mod 13),

where h_a=[w^a]Q0(w)^a/(1-w)^(a+1), Q0(w)=1-w+w^2/2. No general unit assertion about h_a is needed. The established logarithmic coefficient bound, followed by integral adjugate contraction, gives

ell_j:=v_13(L_j)>=2f-h>0.

Use ell_j=+infinity if L_j=0. In particular E_j and E_j+L_j are 13-units, even when h_a vanishes modulo 13.

## What cancels, and where

The exact valuation formulas are

v_13(Qexp_j)=v_13(q_j)=2f+x_j,
v_13(B_j)=max(0,2f+x_j-ell_j).

Consequently

0<=v_13(B_j)<=x_j+h,
v_13(q_j)-v_13(B_j)>=2f-h.

The factorial 13-part survives in the exponential companion and in the total coordinate denominator. It largely cancels INSIDE the logarithmic companion. Thus a large 13-part of q_j is not evidence for a comparable 13-part of B_j.

Take the explicit subprogression n_s=13^(s+1)+3, s>=5. The retained transfer proof gives h_(13^s)=1 (mod 13), so x_j=0 for all three positive rows. Legendre's formula and the base-13 digit sum 4 give

v_13(q_j)=v_13(Qexp_j)=2v_13(n_s!)=(n_s-4)/6,
0<=v_13(B_j)<=s+1.

Here h=s+1. The contribution of this prime to 2 log B_j is at most 2(s+1)log 13=O(log n_s), whereas its contribution to log q_j is linear in n_s.

This is an all-index consequence of the inherited transfer and gate, not extrapolation from a new finite sample. For the entire progression it also yields log q_j>=(log 13)n/6-O(log n), and hence q_j tends to infinity. That lower rate is below log 2 and settles neither smallness nor obstruction for q_j times the coordinate error envelope.

## The deciding gcd and the missing global exponent

Exactly determining the residual 13-part requires ell_j relative to the threshold 2f+x_j. It vanishes in B_j if and only if ell_j>=2f+x_j; below that threshold its exponent is 2f+x_j-ell_j. The available lower bound ell_j>=2f-h does not decide which case occurs, even on n_s.

Globally, the exact deciding quantity for positive coordinates is

Glog_j=gcd(Ffac |X_j|,|L_j|).

Writing the active companion budget in terms of this gcd gives

log(Hsel_j/A_j)+2log B_j
=log(||C_j||_1/|X_j|)+2log(Ffac |X_j|)-2log Glog_j.

Equivalently one may use gcd(D |U0|,|Jmoment|). No control established here bounds the other-prime contribution to B_j or the global ratio ||C_j||_1/|X_j|. Therefore no exponent for this normalized budget has been proved.

Under the hypotheses of the combined-companion elementary-e argument, its implication is

(2+epsilon)log q_j>=log(n!)-log(Hsel_j/A_j)-(2+epsilon)log B_j-O_epsilon(n).

In particular log(Hsel_j/A_j)=O(n) and log B_j=o(n log n) would imply liminf log q_j/(n log n)>=1/2. Those estimates are not supplied by the local calculation. Conversely, with log q_j=O(n), log B_j=O(n log n), and |log(Hsel_j/A_j)|=O(n log n), the argument requires liminf [log(Hsel_j/A_j)+2log B_j]/(n log n)>=1. This remains a necessary conditional budget, not a proved growth law for the eligible coordinates.

No complete-error lower bound, signed asymptotic, nonstabilization statement, shrinking independent pair, or irrationality conclusion is asserted.
