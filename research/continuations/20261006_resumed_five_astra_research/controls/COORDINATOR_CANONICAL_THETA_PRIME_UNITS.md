> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Canonical shared scalar: exact selected-prime units

Coordinator derivation, October 6, 2026; independent review requested. This is a target-specific application of existing complete moment identities and classical constant-term Lucas congruences.

Use the canonical integer from A3 turn 9,
Theta = 2^((n+1)/2) D_L / n!, for odd n in the original endpoint families. Write m=n+1, L=2^(m/2), tau_k=[t^k](1-2t-t^2)^(-1/2), h=n! tau_n, ell=n! tau_(n+1), h_1=m(h+ell)/2. The complete residuals and shared scalar are



$$
b_0=u_n-E_nh-a_n,\quad b_1=u_{n+1}-E_nh_1-a_{n+1},
\quad K=h b_1-h_1 b_0-2(n!)^3,
$$




$$
D_L=mZ(Qh-P\ell)-FK,
\quad X=ma_n,\ Y=mn a_{n-1},\ Z=2a_{n+1}-ma_n,
$$




$$
P=nX+Y,\quad Q=nZ+2X-Y,\quad
F=2m(Y-2X-(n-1)Z).
$$



Let p be any odd prime dividing n. The divided-power coefficients c_i=i![z^i](1-z+z^2/2)^n for i>=1 are integer polynomials in n whose every term contains a positive-length falling factorial of n. Their pairing coefficients i!/((i-2k)! k! 2^k) are integers. Consequently c_i=0 modulo p for all i>=1. The complete identities a_j=sum_i bin(j,i)c_i and u_j=sum_i bin(j,i)c_i E_(n+j-i) give a_j=1 and u_j=E_(n+j) modulo p. E_k=k E_(k-1)+1 has period p modulo p, beginning E_0=E_p=1. Hence E_n=u_n=1 and u_(n+1)=2 modulo p.

Since tau_k belongs to Z[1/2], n! tau_k is divisible by p. Therefore b_0=0, b_1=1, X=Z=1, Y=P=0, Q=2 and F=-2 modulo p. Divide the exact expression for D_L by n! in Z_p, using h/n!=tau_n, rather than dividing a zero residue. It follows that



$$
\boxed{\Theta\equiv4L\tau_n\pmod p\qquad(p\text{ odd},\ p\mid n).}
$$



The tau sequence has the rational constant-term representation



$$
\tau_n=\operatorname{CT}(1+x+(2x)^{-1})^n
=\sum_k\binom n{2k}\binom{2k}k2^{-k}.
$$



Reduce its coefficients in F_p. Frobenius and support [-1,1] imply tau_(pq+r)=tau_q tau_r modulo p, 0<=r<p: the low polynomial has exponents strictly between -p and p, so only exponent zero can pair with a multiple of p. Repeating gives the base-p digit product. This is a classical Lucas property, also covered by Henningsen--Straub, *Generalized Lucas congruences and linear p-schemes*, Corollaries 2.2 and 3.1; the author-hosted primary PDF was inspected. The localization at 2 is harmless for odd p and the short proof above pays it explicitly.

The complete digit tables are



$$
p=3:\ (1,1,2),\qquad
p=5:\ (1,1,2,4,1),\qquad
p=7:\ (1,1,2,4,5,1,6).
$$



All entries are nonzero. Thus tau_n is a unit at 3,5,7 for every n, and the displayed Theta congruence gives



$$
\boxed{\gcd(\Theta,15)=1\text{ on }n=15^r;\qquad
\gcd(\Theta,105)=1\text{ on }n=105^r.}
$$



This excludes an exact divisibility of Theta by (n!)^3, or a canonical smooth factor containing its full selected-prime factorial part. It does NOT exclude a lower bound log U >= 3 log(n!)-O(n): the omitted fixed-prime contributions have only O(n) logarithmic size. A finite small smooth factor at n=3375 likewise does not disprove a different asymptotic subsequence. The useful new datum is the exact selected-prime obstruction for the canonical scalar, with no arbitrary multiplication by a localized unit.

Primary source: https://arminstraub.com/downloads/pub/generalized-lucascongruences.pdf . Scoped local searches found no earlier application to this canonical complete-force shared scalar; no exhaustive novelty claim is made. A new bounded coordinator control will check the congruence at auxiliary odd indices and the already retained Theta at original3375, without regenerating a producer or any old denominator/gcd result.
