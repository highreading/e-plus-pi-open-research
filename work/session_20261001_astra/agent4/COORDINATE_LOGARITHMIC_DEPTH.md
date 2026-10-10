> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact logarithmic depth for eligible positive coordinates

This is new paper arithmetic, using the retained coordinate reconstruction identities. No old residue computation is repeated. The new ingredient is a top-denominator moment calculation, followed by an exact compatibility identity for the adjugate selector.

## 1. Domain and actual decomposition

Fix b=3, weight parameter m=1, h=s+1>=6, P=13^h, and n=P+3. Thus n>2^22 and the retained rational eligible set Jelig is nonempty. Its elements belong to {1,2,3}; the claims below apply to every such eligible coordinate. They actually hold for all three positive coordinates, whose X_j are units by the previously accepted transfer theorem. No statement is transferred to a Gram center or coordinate zero.

Use Ffac=(n!)^2, f=v_13(n!), and the fixed integral normalization M, Delta, V, E, Lnorm from ELIGIBLE_COORDINATE_GCD.md. For positive reconstruction row a_j define

X_j=a_j adj(M)V,
E_j=a_j adj(M)E,
L_j=a_j adj(M)Lnorm.

Here L_j denotes the logarithmic numerator, not a selector polynomial. The actual decomposition is

alpha_j=E_j/(Ffac X_j),
gamma_j=L_j/(Ffac X_j),
t_j=alpha_j+gamma_j.

In the previous companion notation gamma_j=r_j+beta_j=beta_j, since the positive-coordinate correction r_j is zero. Put B_j=den(gamma_j) and q_j=den(t_j), always after full cancellation.

The accepted arithmetic supplies v_13(X_j)=v_13(E_j)=0 and v_13(q_j)=2f. These are retained dependencies, not the new result. The task here is to determine L_j at depth 2f-h.

## 2. The raw adjugate selector preserves the logarithmic identity

Let s_i=(n+i)!/n!, i=0,1,2, and define the integral selector row

C_j=a_j adj(M)diag(s_0,s_1,s_2).

Write its polynomial as C_j(t)=sum_i (C_j)_i t^i. Define Q(t)=1-2t+2t^2 and

K_j(t)=t^n/n! * D^n[Q(t)^n C_j(t)].

Equivalently this is 2^n t^n D^n[(t^2-t+1/2)^n C_j(t)]/n!. The retained selector identities, before removal of row content, give exactly

K_j(1)=X_j,
L_j/Ffac=calL((K_j(t)-K_j(1))/(t-1)).                 (1)

Indeed, writing C_j=eta_j times the primitive selector multiplies both its endpoint and logarithmic moment by eta_j. The previously established primitive identity therefore yields (1). There is no extra adjugate determinant or factorial to insert into this moment identity.

All coefficients of K_j are integers: if Q^n C_j=sum_d b_d t^d, then K_j=sum_{d>=n} binom(d,n)b_d t^d. Its degree is at most 2n+2=2P+8.

## 3. Only two moment indices survive at the first unresolved depth

For k>=1 write

mu_(k-1)=calL(t^(k-1))
=((1+i)^k-(1-i)^k)/(i 2^(k-1) k).

The numerator divided by i is an integer. Hence v_13(mu_(k-1))>=-v_13(k). Since 2P+8<3P and h>=6, every k between 1 and 2P+8 has valuation at most h; equality occurs precisely at k=P and k=2P.

Consequently P mu_(k-1) is 13-integral for every relevant index and vanishes modulo 13 except possibly at these two indices. Their exact residues are

P mu_(P-1)=2 mod 13,
P mu_(2P-1)=1 mod 13.                              (2)

For completeness these follow by reducing the Gaussian integer expression modulo 13 with i=5. Frobenius gives (1+i)^P=1+i and (1-i)^P=1-i, while 2^(P-1)=1. This proves the first residue. For the second, the numerator becomes (1+i)^2-(1-i)^2=4i and 2^(2P-1)=2, giving 4/(2*2)=1. All divisions here are by units; the factor P has already canceled the nonunit part of k. Since the original moments are rational, this finite-field evaluation computes their rational residues.

Write K_j=sum_d c_d t^d and

(K_j-K_j(1))/(t-1)=sum_{k>=1} A_k t^(k-1),
A_k=sum_{d>=k} c_d.

Combining (1) and (2) gives the new deciding lift

P L_j/Ffac = 2 A_P + A_(2P) mod 13.                 (3)

Lower-depth moments cannot contribute to (3), regardless of their number: each scaled summand is individually zero modulo 13.

## 4. Frobenius and Lucas determine the contracted moment

Reduce coefficients modulo 13 and put

D_j(t)=Q(t)^3 C_j(t),   deg D_j<=8.

As P is a power of 13,

Q(t)^n C_j(t)=Q(t^P)D_j(t) mod 13
=(1-2t^P+2t^(2P))D_j(t) mod 13.

All low degrees l satisfy 0<=l<=8<13, so there are no overlapping blocks. Applying Lucas to binom(d,P+3), the block d=l contributes zero, while

binom(P+l,P+3)=binom(l,3) mod 13,
binom(2P+l,P+3)=2 binom(l,3) mod 13.

For l<3 the displayed low binomial is zero. If d_l=[t^l]D_j, define

H_j(t)=sum_(l=3)^8 binom(l,3)d_l t^l.

The whole polynomial K_j therefore satisfies

K_j(t)=(-2t^P+4t^(2P))H_j(t) mod 13.                (4)

This calculation allows arbitrary coefficients of the actual adjugate selector C_j; they need not be constant along the progression. It therefore already includes the reconstruction-row dependence without requiring a new large matrix calculation.

Let H=H_j(1). Equation (4) gives

A_P=2H mod 13,
A_(2P)=4H mod 13,
X_j=K_j(1)=2H mod 13.

Substituting into (3) proves the decisive identity

P L_j/Ffac = 8H = 4X_j mod 13.                     (5)

This is the next moment/adjugate lift beyond the earlier lower bound. The accepted unit property of X_j now prevents cancellation at this first possible depth. No numerical value of e+pi or eligibility approximation is used.

## 5. Exact valuations and overlap

Since X_j is a 13-unit, the right side of (5) is nonzero. Therefore

v_13(P L_j/Ffac)=0,
v_13(L_j)=2f-h.                                    (6)

In particular L_j is nonzero. Equivalently,

13^h gamma_j=4 mod 13,
v_13(gamma_j)=-h.

Thus, after full cancellation,

v_13(B_j)=h=s+1.                                   (7)

This establishes equality in the old upper bound, not merely a stronger lower bound for q_j. Since 2f=(P-1)/6>h and the retained result gives v_13(q_j)=2f,

v_13(gcd(q_j,B_j))=h=s+1.                          (8)

The local part of the logarithmic cancellation gcd is now also exact:

v_13(gcd(Ffac |X_j|,|L_j|))=2f-h.

For explicit factorization write

q_j=13^(2f) q_j^*,  B_j=13^h B_j^*,
13 does not divide q_j^* B_j^*.

Then the full overlap is exactly

gcd(q_j,B_j)=13^h gcd(q_j^*,B_j^*).

Only its 13-primary factor is determined here; the remaining factor is not asserted to equal one.

## 6. Scope and verification status

The new all-index proof is the scaled-moment identity (5). Its derivation uses only the exact coordinate moment identity, Frobenius, Lucas, and the explicit two surviving moment residues. The prior X_j unit theorem is an inherited dependency; its accepted residue gate was not rerun. No new numerical experiment is claimed.

The result preserves positive-coordinate restrictions and rational eligibility. Other primes, the global size of B_j, selector-height ratios, and the upper growth window for q_j remain unresolved. The local contribution to log B_j is exactly (s+1)log 13, still only logarithmic in n. This does not establish a global companion-budget exponent, shrinking primitive forms, or any rationality conclusion for e+pi.
