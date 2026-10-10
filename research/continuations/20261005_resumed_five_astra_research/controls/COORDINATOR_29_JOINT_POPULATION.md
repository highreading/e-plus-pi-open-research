> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# An explicit infinite original-family locus for the third-defect theorem

Coordinator author derivation, October 5, 2026; independent review pending.
This supplies a sufficient locus, not a classification of every residual zero.
The original family is b=3^a, n=2001b, a=432827+682892t, t>=0.
Write p=29, L=p^4, b=687936+Lh, h=pH+d, 0<=d<=24, and
A=69h+67=2001H+69d+67. The actual residual terms are

X_k=binom(A,k) binom(2A+H-k,H-k), 0<=k<=H,
mathcal T=sum X_k^2, T=mathcal T modp, U=sum k X_k^2 modp.
On T=0, T1=mathcal T/p modp and the retained exact original norm digit is
D1=C_n^2 [f(d)T1+beta(d)U] modp (A2 prior turn19, equation4.6).
C_n and f(d) are units at the retained eligible-d scope.

## Gate and classical overlap

Before this construction, focused archive searches located the stated
component-common-content observation in A2 turn19: if every X_k is p-divisible,
then T1=U=0. It is reused, not reproved as a new principle. The searched reports
did not give the sufficient (d,H mod29) cylinders and their original-exponent
classes below. This is a bounded overlap check, not an exhaustive novelty claim.
Lucas/Kummer and prime-power binomial methods are classical; Granville's
primary binomial paper is already retained. Rowland--Yassawi's original paper
https://jtnb.centre-mersenne.org/item/10.5802/jtnb.901.pdf was opened, including
Proposition1.9 and Theorem2.1, before developing the auxiliary finite recursion.
No generic automaticity theorem is needed for the elementary cylinder proof.

## A sufficient one-digit vanishing cylinder

Let a_low=(11d+9) mod29, chosen in 0,...,28. Choose

1<=a_low<=14, and 29-a_low<=r=H mod29<=28.                 (P)

For every actual k in 0,...,H, put k0=k mod29. If k0>a_low,
Lucas makes binom(A,k) divisible by29. Otherwise k0<=a_low<r,
so there is no units-digit borrow in H-k, whose low digit is j0=r-k0.
At the units digit of 2A+(H-k) there is no incoming carry. Its low
sum is 2a_low+j0. We have

29<=a_low+r<=2a_low+r-k0<=2a_low+r<=56<58.

Thus its low digit is 2a_low+r-k0-29, strictly less than j0 since
2a_low<29. Lucas makes binom(2A+H-k,H-k) divisible by29.
This proves p|X_k for EVERY actual k, including both endpoints, with
no condition on any higher digit. Consequently

mathcal T in p^2 Z, T=T1=U=0, and D1=0.                 (1)

No statement that the residual vector is nonzero modulo29 is intended.
These are precisely component-common-content cylinders. They do not
populate the more delicate nonzero isotropic-vector locus U!=0.

For d=0,...,24 the admissible a_low values are
9,2,13,6,10,3,14,7,11,4,8,1,12. Each value contributes a_low choices
of r. Their sum is100. Thus (P) gives exactly100 distinct h mod841
cylinders in the eligible range.

## Infinite ORIGINAL exponent reachability, including the next digit

Use the exact bounded modular computations recorded in the attached receipt:

3^432827 mod29^6 =687936+29^4*741,
(3^682892-1)/29^4 mod29^2 =73.

The second identity refers to the quotient of the least modular representative
3^682892 mod29^6 minus1; it is sufficient to specify the full congruence
3^682892=1+73*29^4 mod29^6. Since 73 is a29-unit, g=3^682892 has
v29(g-1)=4 exactly, hence order29^2 modulo29^6 by LTE.
For EVERY integer t>=0, the binomial theorem (2*4>=6) gives

h(t) =741+695t mod841,
695=(3^432827 mod841)*73 mod841.

The coefficient695 is a29-unit (695=-1 mod29). Therefore this is a
bijection on t mod841. Each of the100 desired h=d+29r classes determines
one t class modulo841, and each such t class contains infinitely many
nonnegative integers. These are the original exponents, not auxiliary
independent choices of A,H or a replacement parameter family.
For example d=0, r=20 is reached at t=364 mod841. The entire100-row
certificate gives all classes. The retained low-digit formula d=16-t mod29
is recovered from741=16 mod29 and695=-1 mod29.

Thus the joint population lemma has an unconditional sufficient solution,
at the retained original force and digit interfaces. It is not a full
classification of T=D1=0 and says nothing about their natural density as
functions of all integer exponents outside the original progression.

## Third-defect consequence and its exact limitation

The reviewed theorem M-(6C_n)^(-1)D=0 mod29^3 applies on these infinitely
many original indices, since d<=24,T=0,D1=0 are satisfied. If D/29^2 is a
unit, both norm and mixed valuations are exactly2; if it vanishes, both
are at least3. This construction DOES NOT evaluate D/29^2 and does not
bound the difference of deeper valuations. In fact T1=U=0 already kills
the third-defect contraction r0T1+r1U in the earlier formula; the newly
computed universal Gamma0 identity is useful on a larger conditional locus,
not required for this particular common-content cylinder.

The actual primitive denominator remains
v29(q)=max(0,2v29(n!)-v29(b!)-1+v29(D)-v29(M)).
No global cancellation or small primitive error follows from (1).

## Auxiliary six-state Lucas recursion (not needed for (P))

For arbitrary nonnegative A,H, process their base29 digits from low to high.
A state is (borrow,carry) in {0,1} x {0,1,2}, initialized at(0,0).
Given digits a_i,r_i and a summation digit k_i in0,...,28, set

j_i=(r_i-k_i-borrow) mod29,
borrow'=[r_i-k_i-borrow<0],
s_i=(2a_i+j_i+carry) mod29,
carry'=floor((2a_i+j_i+carry)/29).

Multiply the transition weight by
binom(a_i,k_i)^2 binom(s_i,j_i)^2 mod29,
and sum over k_i. This is a6x6 transfer matrix. Lucas gives its exact
product meaning for X_k^2; paths with an eventual borrow are rejected,
retaining the true restriction k<=H. Process all digits of A,H and an
extra zero digit if desired; accept borrow0, sum over the final carry.
Trailing carry belongs to the upper binomial and contributes binom(carry,0)=1.
For U mod29, weight only the first digit transition by k0, because higher
k digits are multiples of29. With A=2001H+69d+67, the affine A digit can
instead be generated by carry c initialized at69d+67, via
a_i=(2001r_i+c) mod29, c'=floor((2001r_i+c)/29).
This adds a bounded affine carry, or one may simply compute A's digits.

The independent exact-integer recurrence
X_(k+1)=X_k(A-k)(H-k)/[(k+1)(2A+H-k)]
was used with verified EXACT division, never a modular inverse of an even
or29-divisible denominator. The6-state method matches2525 auxiliary
cases H=0,...,100, d=0,...,24. This finite check supports implementation;
the proof is the preceding Lucas path factorization, not the samples.
A mod841 recursion for T1 still requires its own carry/unit corrections.
