> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact unit lifts and two complete local special-gcd formulas

Date: 2026-09-13. Original bounded continuation of the special-value gate
in `hp_b1_special_gcd_and_denominator.md`. No extension of the finite
prime-support scan was used.

## Result

Let



$$
H_n(x)=n![t^n]e^{xt}(1-t+t^2/2)^n,
 \qquad J_n(x)=nH_n(x)+H_n'(x),
$$



and let g_n=gcd(H_n(1),J_(n+1)(1)), n>=2. For every odd prime p dividing
n-1,



$$
\boxed{v_p(g_n)=v_p(n-1).}
\tag{1}
$$



In fact, if a=v_p(n-1)>=1, the stronger actual-sequence congruence is



$$
\boxed{J_{n+1}(1)\equiv8(n-1)\pmod{p^{a+1}}.}
\tag{2}
$$



Thus the already proved divisor oddpart(n-1) occurs to *exactly* its
indicated valuation at every one of its odd prime factors. It has no
additional lifts, including at p=3. Equivalently,



$$
\gcd\left(g_n/\operatorname{oddpart}(n-1),
               \operatorname{oddpart}(n-1)\right)=1.
\tag{3}
$$



This does not classify other residue branches. In particular p>2n+2
cannot divide n-1, so it does not settle the original large-prime
endpoint-gcd gate. Its concrete use is to remove the entire forced
branch n=1 mod p from further higher-lift searches.

The addendum in Sections7–9 also proves the exact all-index formulas



$$
v_3(g_n)=v_3(n-1),\qquad
 v_5(g_n)=v_5(n-1)+\min\{v_5(n+1),2\}.
\tag{3a}
$$



These use complete fixed-prime residue information and a convergent
factorial constant, not an extension of the finite index scan.

## 1. Two exact differential identities

Put phi(t)=1-t+t^2/2. Direct differentiation of the coefficient formula
gives



$$
H'_{n+1}(x)=(n+1)
 \left(H_n(x)-H_n'(x)+\frac12H_n''(x)\right).
\tag{4}
$$



There is also the raising identity



$$
H_{n+1}(x)=\frac x2H_n''(x)
 +(n+1-x)\bigl(H_n'(x)-H_n(x)\bigr).
\tag{5}
$$



For an entirely formal proof of (5), write F=e^(xt)phi(t)^n. The
coefficient of t^(n+1) in



$$
t(\phi F)'-(n+1)\phi F
 =\left(xt\phi+(n+1)(t\phi'-\phi)\right)F
$$



is zero. Here t phi'-phi=t^2/2-1. Expanding this identity and rearranging
gives (5) after multiplication by n!. Thus no unverified integration
constant or special-function identification is involved.

Set x=1 in (4) and (5) and form J_(n+1)=(n+1)H_(n+1)+H'_(n+1).
The result is the exact identity



$$
\boxed{J_{n+1}(1)=(n+1)
 \left(H_n''(1)+(n-1)\bigl(H_n'(1)-H_n(1)\bigr)\right).}
\tag{6}
$$



It is this special x=1 identity, rather than the full polynomial
resultant in x, that controls the local branch.

## 2. Congruences for differentiated special values

For nonnegative integers b,c put r=b+2c and s=b+c. For every derivative
order j>=0, expansion of the defining coefficient gives



$$
H_n^{(j)}(1)=\sum_{b,c\ge0}
 \frac{(-1)^b}{2^c}
 (n)_{r+j}\binom ns\binom sc.
\tag{7}
$$



The sums are finite: (n)_(r+j) vanishes when r+j>n. The factors are
rational integers except for powers of2, so termwise odd-prime
valuation arguments are legitimate.

The previously proved elementary congruence lemma applies to every term
of (7): (n)_R binom(n,s) preserves congruences modulo p^a when R>=s.
It follows either directly from its integer-polynomial difference and
Vandermonde's identity, or from



$$
v_p\bigl(\binom ms-\binom ns\bigr)
 \ge a-\lfloor\log_p s\rfloor,
 \qquad v_p((n)_R)\ge v_p(R!)
 \ge\lfloor\log_p s\rfloor.
$$



Consequently, if n=1 mod p^a,



$$
H_n(1)\equiv H_1(1)=0,
 \qquad H_n'(1)\equiv H_1'(1)=1\pmod{p^a}.
\tag{8}
$$



These are congruences for the actual special values, not a formal
derivative of n treated as a continuous variable.

## 3. The second-derivative lift

Fix n>=2 and an odd prime p with a=v_p(n-1)>=1. Write n=1+p^a u,
where p does not divide u. In (7) for j=2 put R=r+2, so R>=s+2.

Every term with s>=2 has valuation at least2a. Here is a full check,
including the possible carry ranges.

If R>=p^a+2, a nonzero falling factorial (n)_R contains both n-1 and
n-1-p^a. Both are divisible by p^a. All other factors in the term are
p-integral, so its valuation is at least2a. If R>n the term is zero
and the conclusion remains valid.

If R<=p^a+1, then s<=r=R-2<=p^a-1. The factor n-1 is the only one
in (n)_R whose offset from n has a difference divisible by p^a. All
remaining offsets have lower valuation, giving the exact formulas



$$
v_p((n)_R)=a+v_p((R-2)!),
$$





$$
v_p\binom ns
 =a+v_p((s-2)!)-v_p(s!)
 =a-v_p(s(s-1)).
$$



Because p is odd and s,s-1 are consecutive, at most one is divisible
by p. If its valuation is k, then p^k<=s<=R-2. Therefore



$$
v_p((R-2)!)\ge k=v_p(s(s-1)).
$$



The total term valuation is at least2a, as claimed. This second case
is the point where a missing factorial factor would have invalidated
the proposed lift; the derivative order2 supplies exactly that factor.

Since 2a>=a+1, all s>=2 terms vanish modulo p^(a+1). The remaining
terms have s=0 or1, hence (b,c)=(0,0),(1,0),(0,1), and their exact sum is



$$
(n)_2-n(n)_3+\frac n2(n)_4.
\tag{9}
$$



This polynomial in n vanishes at n=1 and has first derivative3 there.
Writing h=n-1, its value is3h+O(h^2), with coefficients in Z[1/2].
Because p is odd, the error is divisible by p^(2a). We have proved



$$
\boxed{H_n''(1)\equiv3(n-1)\pmod{p^{a+1}}.}
\tag{10}
$$



No restriction such as p>n is required for this argument.

## 4. Unit coefficient8 and exact common valuation

Insert (8) and (10) into (6). Multiplication of (8) by n-1 improves its
modulus from p^a to p^(2a), so



$$
J_{n+1}(1)
 \equiv(n+1)\bigl(3(n-1)+(n-1)\bigr)
 =4(n+1)(n-1)
 \equiv8(n-1)\pmod{p^{a+1}}.
$$



Since8 is a p-unit for every odd prime, this proves
v_p(J_(n+1)(1))=a. Equation(8) gives v_p(H_n(1))>=a. Their gcd
therefore has valuation exactly a, proving (1).

This also handles p=3: H_n(1) itself can have a higher valuation there,
as H_4(1)=45 illustrates, but the second gate has the exact unit lift.
For n=4, J_5(1)=-1515 has valuation1 at3, and the common valuation is1.

## 5. Exact root-tree interpretation and remaining scope

For the actual residue sets



$$
Z_{p,a}=\{0\le r<p^a:H_r(1)=J_{r+1}(1)=0\pmod{p^a}\},
$$



the branch reducing to1 modulo p has exactly one lift at every level:



$$
\boxed{Z_{p,a}\cap\{r:r\equiv1\pmod p\}=\{1\}.}
\tag{11}
$$



The inclusion of1 follows from H_1(1)=J_2(1)=0. If another residue
r=1 mod p were a root at level a, its exact common valuation from(1)
would be v_p(r-1)<a, a contradiction. The level a=1 is immediate.

Thus the forced root does not split into further common-zero branches,
and no extra common valuation is available on its nontrivial nearby
integer indices. Additional odd prime factors of g_n must come from
other classes modulo p; proving that such factors never exceed2n+2,
or finding a counterexample, remains unresolved. The earlier finite
prefix through256 is not used in this theorem.

The full integral HP endpoint-gcd gate previously proved only applies
at p>2n+2. Such primes are absent from the branch just analyzed. Hence
this result makes no new direct claim about that full endpoint gcd,
about the final reduced q_n, or about rationality of e+pi. It is a
structural local theorem for the exact auxiliary gcd and removes one
specific higher-lift obstruction from its study.

## 6. Exact controls

`check_hp_special_gcd_unit_lift.py` verifies the two polynomial identities
at n=1,2,4,8 by exact coefficient arithmetic. Nine predeclared local
controls cover p=3,5,7,11, precisions a=1,2, and several unit quotients
of n-1. They check the second-derivative congruence, the unit8 lift,
the exact common valuation, and each nonzero s>=2 summand's2a valuation
bound in those instances. Every check passes; results are in
`hp_special_gcd_unit_lift_checks.json`. These controls test algebra and
normalization only; the all-index proof is Sections1–4.

Audit_computations independently reviewed Sections1–5 and accepted both
differential identities, every range in the2a valuation argument, the
unit coefficient8, and the exact root-tree consequence. No substantive
gap was found.

## 7. A second exact unit lift for the J gate

Put h_m=H_m(1). The already proved exponential generating function is



$$
\sum_{m\ge0}h_m\frac{z^m}{m!}=\frac{e^{w(z)}}{\sqrt{1+2z-z^2}},
 \qquad w=z(1-w+w^2/2).
$$



Define E_m=m![z^m]e^(w(z)). The identities
z(e^w)'=w e^w/sqrt(1+2z-z^2) and
z^2(e^w)'+e^w=(1+z)e^w/sqrt(1+2z-z^2) give



$$
H_m'(1)=mE_m,\qquad
 E_m=h_m+mh_{m-1}-m(m-1)E_{m-1},\quad E_0=1.
\tag{12}
$$



In particular every E_m is an integer, without assuming that division
of H_m'(1) by m is harmless. If p is odd and p|m, congruence preservation
gives h_m=H_0(1)=1 mod p, and (12) gives E_m=1 mod p. Thus



$$
\boxed{J_m(1)=m(h_m+E_m)\equiv2m
 \pmod{p^{v_p(m)+1}},\qquad v_p(J_m(1))=v_p(m).}
\tag{13}
$$



Consequently, on the other automatic J-root branch n=-1 mod p, its
valuation is exactly v_p(n+1). The H gate remains to be evaluated.

## 8. The other branch is governed by one p-adic factorial constant

For each odd prime p, the convergent p-adic series



$$
\mathcal C_p=\sum_{r=0}^{\infty}(-1)^r r!c_r,
 \qquad c_r=[t^r](1-t+t^2/2)^{-1}
\tag{14}
$$



is well defined: c_r belongs to Z[1/2], and v_p(r!) tends to infinity.
It equals the p-adic limit of H_(p^k-1)(1).

To justify this limit without an illicit infinite interchange, write



$$
h_m=\sum_{r\ge0}(m)_r[t^r](1-t+t^2/2)^m.
$$



For nonnegative integer m, every coefficient of the quadratic power is
p-integral and v_p((m)_r)>=v_p(r!). Thus the tail is uniformly zero
modulo any fixed power of p once r is sufficiently large, independently
of m. For each remaining fixed r, both factors are polynomials in m
over Q and hence continuous over Q_p. Letting m=p^k-1 tend to -1 gives
(m)_r->(-1)^r r! and the coefficient of the inverse quadratic. This
proves the asserted limit at every finite precision.

If n=-1 mod p^a, congruence preservation then gives



$$
H_n(1)\equiv\mathcal C_p\pmod{p^a}.
\tag{15}
$$



Let lambda_p=v_p(C_p), allowing infinity when C_p=0. Combining(13)
and(15), for every n=-1 mod p with a=v_p(n+1), proves



$$
\boxed{v_p(g_n)=\min\{a,\lambda_p\}.}
\tag{16}
$$



If lambda_p<a, the congruence fixes the H valuation exactly; if
lambda_p>=a, the J valuation caps the gcd at a. Thus(16) does not
require deciding whether C_p can vanish p-adically.

This is a structural reduction for a specific residue branch. It is
not a statement that all common roots modulo p lie on the two branches
1 and -1, nor a bound uniform over p.

## 9. Complete local arithmetic at3 and5

The exact small-index gate values are

| r | H_r(1) | J_(r+1)(1) |
|---:|---:|---:|
| 0 | 1 | 1 |
| 1 | 0 | 0 |
| 2 | 1 | -3 |
| 3 | -5 | 88 |
| 4 | 45 | -1515 |

This is a complete residue table modulo3 using its first three rows,
and modulo5 using all five rows. Consequently the joint root sets at
precision one are Z_(3,1)={1} and Z_(5,1)={1,4}. The first set and(1)
already prove v_3(g_n)=v_3(n-1) for every n>=2.

It remains to determine lambda_5 for the second set. The coefficients
in(14) satisfy c_0=c_1=1 and c_r=c_(r-1)-c_(r-2)/2. Their exact values
repeat by c_(r+4)=-c_r/4. Since v_5(r!)>=3 for r>=15, only the first
fifteen terms matter modulo125. Their exact rational values in this
case are integers after multiplication by r!, and their sum is



$$
\sum_{r=0}^{14}(-1)^r r!c_r=-591174425
 \equiv75\pmod{125}.
\tag{17}
$$



For transparency the nonzero terms, with the initial1 and-1 canceled,
are



$$
1,-6,30,-90,2520,-22680,113400,
 -7484400,97297200,-681080400.
$$



Their sum verifies(17) directly. The omitted tail is zero modulo125,
so lambda_5=2 exactly. On the residue4 branch, (16) therefore gives
min(v_5(n+1),2); on residue1, (1) gives v_5(n-1); all other residues
have valuation zero. This proves the second formula in(3a).

For example n=24 has v_5(g_24)=2 although5 does not divide n-1. Thus
one cannot strengthen the forced-divisor description by assuming all
additional odd factors occur only to the first power.

This completes the local description at two fixed primes. It does not
bound the total logarithm of g_n, its other residue branches, or the
large-prime part relevant to the original endpoint-gcd gate.

Audit_computations independently reviewed Sections7--9 and accepted
the integrality argument, exact unit-2 lift, uniform factorial-tail
passage, branch valuation formula, and complete valuations at3 and5.
Root independently checked the addendum as well. No gap was found.
