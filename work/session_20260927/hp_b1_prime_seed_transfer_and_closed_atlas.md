> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Actual b=1 numerator: all-residue prime transfer and a closed seed atlas

Date: 2026-09-27. Author: audit_computations.
Status: FULL PASS in `hp_b1_uniform_5_13_independent_review.md`
(audit_results), including all 72 seed rows, the general all-residue
transfer, and the separate all-depth root-disk lift in
`hp_b1_residue_one_actual_numerator.md`, Sections 1-2.

## 1. Exact arithmetic objects

Use exactly the sums and actual endpoint quotient in
`hp_b1_ternary_actual_denominator.md`, now independently FULL PASS:



$$
\frac XY=\frac{\mathscr U_n}{\Delta_n},\qquad
 \mathscr U_n=\mathscr Q_n+
                   \frac{2^{n+1}}{(n!)^2}\mathscr C_n,
$$




$$
\mathscr Q_n=2K_{n+1}Q_n-(n+1)H_nQ_{n+1},\qquad
 \mathscr C_n=K_{n+1}\mathscr A_n-H_n\mathscr B_n.
 \tag{1}
$$


All H,K are integers, all A,B,C are in Z[1/2], and Delta is the
actual integer denominator before endpoint reduction. Its eventual
nonvanishing is already proved analytically. The following argument
does not assume a Legendre endpoint is a unit.

## 2. Uniform modulo-p transfer at every residue

For every odd prime p, let r be the residue of n in {0,...,p-1}.
Then



$$
\boxed{(H_n,K_{n+1},\mathscr A_n,\mathscr B_n,\mathscr C_n)
 \equiv(H_r,K_{r+1},\mathscr A_r,\mathscr B_r,\mathscr C_r)\pmod p.}
 \tag{2}
$$



Here r=0 is a legitimate scalar seed even though the actual degree-one
HP family is studied at larger n. Its sums are finite and exactly defined.

Proof: write a_s(k)=[x^s](1-x+x^2/2)^k. The recurrence for
D_j=j! sum_(d=0)^j1/d! shows D_(ap)=1 modulo p and hence
D_(ap+b)=D_b modulo p for 0<=b<p. The sum for H_n or A_n
has factor (n)_s. If s>r this vanishes modulo p; if s<=r<p,
both (n)_s and a_s(n) agree with their r counterparts modulo p.
For the latter assertion apply Frobenius to the generating polynomial;
its p-th power contributes only powers divisible by p. The D index
2n-s likewise reduces to 2r-s, which is nonnegative on this range.
This proves the first and third coordinates.

For K and B the factor is (n)_(s-1). If r<=p-2, only
s<=r+1<p survive, and every factor reduces to the r formula.
If r=p-1, all s>=p+1 vanish. For 1<=s<p, a_s(n+1)=0
by Frobenius. The s=p term has factor 2n+2-p=0 modulo p.
Thus only the displayed s=0 term survives, and the same calculation
holds at the seed r=p-1. This proves the second and fourth coordinates,
and their determinant proves the fifth.

This proof treats the prime-block boundary explicitly. It does not
divide by n+1 when that number is divisible by p.

## 3. Actual reduced denominators away from the seed zero set

Let Z_p={r:mathscr C_r=0 modulo p}. If n mod p is outside Z_p
and n>=p, then



$$
v_p(\mathscr U_n)=-2v_p(n!),\qquad
 \boxed{v_p(q_n)=2v_p(n!)+v_p(\Delta_n)\ge2v_p(n!),}
 \tag{3}
$$


whenever Delta_n!=0.

Indeed the second-kind convolution bounds
v_p(mathscr Q_n)>=-floor(log_p(n+1)). For n>=p,



$$
2v_p(n!)>\lfloor\log_p(n+1)\rfloor.                  \tag{4}
$$


If the floor is 1 this follows from v_p(n!)>=1. If it is a>=2,
then n>=p^a-1 and 2v_p(n!)>=2(p^(a-1)-1)>a for odd p.
Therefore the scaled Q part in (1) vanishes modulo p, whereas C_n is
a unit by (2). This proves the first equality in (3), and actual
rational reduction proves the rest. A large valuation of Delta only
increases the denominator here.

## 4. Exact predeclared seed classification

The closed prime list is 5,7,11,13,17,19, assigned before calculation.
The complete C-residue vectors, in the order r=0,...,p-1, are

| p | C residues modulo p | Z_p |
|---:|---|---|
| 5 | 3,0,1,3,1 | {1} |
| 7 | 5,0,0,0,3,1,5 | {1,2,3} |
| 11 | 9,0,0,5,6,7,7,9,1,6,10 | {1,2} |
| 13 | 11,0,2,8,7,12,2,6,10,6,8,7,1 | {1} |
| 17 | 15,0,16,0,7,14,5,5,10,3,9,0,8,9,5,3,8 | {1,3,11} |
| 19 | 17,0,17,15,3,18,4,10,3,15,15,13,5,17,0,11,9,10,7 | {1,14} |

Certificate: `hp_b1_predeclared_prime_seed_certificate.json`.
Reproduction: `check_hp_b1_predeclared_prime_seeds.py`.

For every listed residue the checker compares two distinct exact
constructions: (i) the modular Rodrigues tail sums in (2); (ii) ordinary
integer Legendre recurrence, followed by direct rational factorial and
exponential-partial-sum functionals and the exact normalization (6) of
the ternary note. It checks every coordinate H,K,A,B,C, not just C.
No HP nullspace, canonical degree solve, factorization, or unbounded
prime search is used. These are complete finite seeds for the
all-index congruence (2), rather than a sample of actual degrees.

## 5. The separately required lift at the forced root

At r=1 the exact seeds are



$$
H_1=0,\quad K_2=0,\quad \mathscr A_1=3,\quad \mathscr B_1=10.
 \tag{5}
$$


The following local statement closes the root for p!=3. It is proved
in `hp_b1_residue_one_actual_numerator.md`, Sections 1-2, using the
previously reviewed analytic first-lift theorem:
for a=v_p(n-1)>=1,



$$
\frac{H_n}{n-1}=-\frac32\pmod p,\qquad
 \frac{K_{n+1}}{n-1}=4\pmod p.
 \tag{6}
$$


The quotients in (6) are required to be p-integral. Together with (2)
and (5), (6) would give



$$
\mathscr C_n/(n-1)=4\cdot3-(-3/2)\cdot10=27\pmod p.
 \tag{7}
$$


For p!=3 this is a unit. H,K divisibility gives
v_p(Delta_n)>=a and v_p(mathscr Q_n)>=a-floor(log_p(n+1)).
The same strict separation (4) then proves



$$
v_p(\mathscr U_n)=a-2v_p(n!),\quad
 v_p(q_n)=2v_p(n!)+v_p(\Delta_n)-a\ge2v_p(n!).
 \tag{8}
$$



The full first congruence in (6) is a genuine extra lemma. For a=1,
individual high-tail terms with pure index p or p+1 can have valuation
a, although their pair cancels at the required precision. A termwise
estimate copied from the old second-derivative lift does not suffice.
Neither a formal ordinary derivative at n=1 nor finite seed data is
used here as a replacement for (6).

Thus 5 and 13 are the uniform primes supplied by this closed list,
using the separately proved lift. Their combined rate with the
already proved all-even dyadic bound is



$$
\frac32\log2+\frac12\log5+\frac16\log13
       >2\log(1+\sqrt2).
 \tag{9}
$$


This excludes shrinking at all even indices of b=1, rather than
just the two ternary residue classes; the full proof is assembled in
`hp_b1_uniform_five_thirteen_and_even_exclusion.md`. Its review status
must remain separate until the root-disk lift and these finite seeds
are independently audited (now FULL PASS in the review named above).
The two odd-prime contributions alone do not exceed the error
exponent, so no all-odd conclusion follows from this list.
