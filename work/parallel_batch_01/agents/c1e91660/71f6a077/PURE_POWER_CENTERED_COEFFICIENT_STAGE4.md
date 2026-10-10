> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Pure-power centered coefficient: stage 4

Status: author algebraic reduction from the inherited complete insertion identity. No infinite growing-pole nonvanishing or sign theorem is established. No independent review or new computation is claimed. S denotes the actual e+pi.

## Scope and hypotheses

Use the actual rational stack beta(T)=det[C;R+TV], with all moments and endpoint derivatives as defined in historical main/GENERAL_POLE_RANK_M_PRIMITIVE_INTERFACE.md. Assume k>=131072 and 3<=m<=k, so the inherited complete-product theorem supplies degree exactly m and a nonzero leading coefficient. Its insertion identity is used as an inherited input. The source texts and the completed stage-3 displacement calculation are available in the supplied transcript; this stage does not repeat their audits or the boundary-nondegeneracy branch.

Write beta(S+t)=sum b_l t^l, d=m-1, and
w_j=j! 2^j binom(d,j)(2(d-j)-1)!!/(2d-1)!! for 0<=j<=d.
Set w_j=0 outside this range and g_m=w_d=4^(m-1)/binom(2m-2,m-1). These are normalized Taylor coefficient weights: replacing w_j by the unnormalized derivative coefficient would lose j!.

## Exact finite near-leading insertion formula

For l in {m-2,m-1,m}, let x consist of k-l compact variables and define

Q_l(x;v)=product_(a=1)^l product_(i=1)^(k-l)(v_a-1-x_i)^2 F(x,v_1-1,...,v_l-1),

where F is the COMPLETE conditional determinant for rho=mu-nu_m from the inherited insertion identity. In particular, upper endpoint jets remain inside F before differentiation. Put

q_(l,alpha)(x)=[v^alpha]Q_l(x;v)=partial^alpha Q_l(x;0)/product_a alpha_a!.

For permutations pi,tau of {1,...,l}, define
z_a=pi(a)+tau(a)-2.
Then define the exact finite integrand

H_l(x)=sum_(pi,tau) sgn(pi)sgn(tau)
        sum_(alpha>=0; alpha_a+z_a<=d for all a)
        q_(l,alpha)(x) product_a w_(alpha_a+z_a).

An inner sum is empty if some z_a>d. There are no omitted derivatives or approximate weights in this formula.

Proof: expand both determinants in Vand(v)^2. Their product has monomials v^z with coefficient sgn(pi)sgn(tau). Applying each actual jet functional to v^z Q_l selects its Taylor coefficients with weight w_(alpha_a+z_a). Summing proves the formula, including signs and factorials.

Since sum_a z_a=l(l-1), every contributing alpha satisfies

|alpha|<=l(m-l).

Consequently the next-to-leading coefficient requires Taylor derivatives of Q_(m-1) of total order at most m-1, and the following coefficient requires derivatives of Q_(m-2) of total order at most 2(m-2). These are exact truncations, not bounds on the discarded remainder: all higher Taylor terms contribute zero. The coordinate restrictions alpha_a+z_a<=d must still be imposed; the total-degree restriction alone is insufficient.

Define

Z_l=1/[l!(k-l)!] integral_[0,1]^(k-l) Vand(x)^2 H_l(x) d sigma_m^(k-l).

The complete insertion identity gives exactly b_l=(-1)^k Z_l. The measure sigma_m retains the same pole order m at every l. No change to sigma_l is allowed.

For l=m, the total-degree restriction forces alpha=0. The confluent Vandermonde coefficient gives

H_m(x)=(-1)^binom(m,2) m! g_m^m Q_m(x;0),

and hence

Z_m=(-1)^binom(m,2) g_m^m J_m,
J_m=1/(k-m)! integral Vand(x)^2 product_i(1+x_i)^(2m) F(x,(-1)^m) d sigma_m^(k-m)>0.

For k=m this is a zero-variable integral, equal to F*. This retains the leading common normalization and its sign exactly.

## The invariant and the second centered coefficient

Translation gives
b_m=beta_m,
b_(m-1)=beta_(m-1)+m S beta_m,
b_(m-2)=beta_(m-2)+(m-1)S beta_(m-1)+binom(m,2)S^2 beta_m.

Direct cancellation proves

D=(m-1)b_(m-1)^2-2m b_m b_(m-2)
 =(m-1)Z_(m-1)^2-2m (-1)^binom(m,2) g_m^m J_m Z_(m-2).             (1)

Thus (1), together with the finite Taylor-permutation formulas above, is an exact expression for the requested invariant in the ACTUAL insertion data. It is not an identity for an assumed symmetric effective matrix.

Let t_bar=-b_(m-1)/(m b_m), so S+t_bar is the mean of the roots. In beta(S+t_bar+u), the coefficient of u^(m-1) is zero and that of u^(m-2) is

b_(m-2)-(m-1)b_(m-1)^2/(2m b_m)=-D/(2m b_m).

The exact rational scalar used for primitive normalization must be retained: if P=lambda beta, where lambda is the signed full moment clearer divided by the final coefficient gcd, then D(P)=lambda^2 D(beta). Therefore nonvanishing and sign are unchanged, but the magnitude is not unchanged. No coefficient gcd is estimated here.

For completeness, the root identity D=beta_m^2 sum_(i<j)(alpha_i-alpha_j)^2 follows from the first two elementary symmetric functions. These are algebraic squares, not absolute squares. It supplies no positivity assertion for complex roots. A pure linear power has D=0, while D=0 alone does not imply a pure power.

## Missing premise and stopping point

A sufficient actual sign statement would be

(-1)^binom(m,2) Z_(m-2)<0,

because J_m>0 then makes (1) strictly positive. More generally, the exact necessary and sufficient inequality for D>0 is

(m-1)Z_(m-1)^2 > 2m (-1)^binom(m,2) g_m^m J_m Z_(m-2).

Neither inequality has been proved here on an infinite growing-pole range. The inherited comparison 0<F<=F* on real nodes controls values, and the inherited Taylor estimates control absolute derivatives. They do not control the signed permutation sums defining Z_(m-1) and Z_(m-2), or their joint cancellation in (1). Positivity of the compact integration measure does not remedy a signed integrand.

In particular, the truncation at l=m does not extend to l=m-1 or m-2: derivatives can fall on both the cross factors and F. Setting those derivatives to zero would replace the actual polynomial by another object. Differentiating F without its upper endpoint terms would likewise be invalid.

The stage-3 displacement identity retains moments through index 3k-1 and shows why truncated multiplication produces terminal boundary contributions. Nothing in the present derivation cancels those terminal moments or justifies omitting them. Pursuing a multiplication or trace reduction without an additional identity would return to the already recorded boundary gap, so that branch is not reopened.

The next useful interface is a signed evaluation or comparison for the two displayed finite Taylor-permutation integrals, including derivatives of the complete F. The formula isolates exactly which derivatives are needed. Without such a comparison, this bounded stage stops rather than proposing symmetry, hyperbolicity, or a factorization atlas.

## Outcome and evidence

The new output is the exact near-leading finite insertion formula with total derivative cutoffs m-1 and 2(m-2), its complete factorial normalization, and equation (1). It does not prove D nonzero or determine its sign on an explicit infinite growing-pole range. Consequently it does not yet rule out the pure-power alternative in Main's trace-denominator lemma. Main owns that lemma's arithmetic consequences.

No code execution, numerical sign evidence, networking, installations, old m=2 reproof, or review of the earlier upper-bound refinement was performed. The main irrationality question remains open.
