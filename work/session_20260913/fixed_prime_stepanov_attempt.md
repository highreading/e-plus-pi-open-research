> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Fixed-prime Item334 attempt: a proved bounded-run estimate

Date: 2026-09-13. Scope: the actual ordinary-j=2 determinant gate and its
simultaneous-collision subset. This is an upper bound on one component. It
does not prove a positive common-divisor gain or irrationality of e+pi.

## Result and dependencies

Let p>3 be prime. List all actual rows

    p=2r+6s+3, r>=1 odd, 3 does not divide r, s>=1

in increasing r. Outside a fixed finite set of primes described below,
the determinant gate can vanish at no more than

    (2/3)|I|+6

rows of any consecutive subinterval I of this list. The same upper bound
therefore holds for actual simultaneous collisions, including degenerate
connection charts. In fact, four consecutive determinant zeros are
impossible, and there are at most five starting positions for three
consecutive zeros.

This uses the exact global algebraic coefficient recurrence from Item237,
its second-branch theorem from Item309, and the all-row p-unit determinant
bridge from Item314. The new algebra is an exact desingularization of that
recurrence and the following zero-run argument. The old global recurrence
and branch identities are explicit proof dependencies; this note does not
claim to reproduce their entire algebraic-differential certificates.
No fitted recurrence or empirical zero count is used.

New exact verification artifacts:

- `check_stepanov_desingularization.py`: reconstructs the old recurrence
  from its canonical coefficient lists; performs exact rational polynomial
  Euclidean arithmetic; verifies both desingularizations; computes the two
  initial minors by exact Lagrange coefficient formulas.
- `fixed_prime_desingularization_check.json`: complete rational coefficient
  lists for the resulting order-four recurrences, all denominator factors,
  exact zero-remainder checks, and initial minors.

The checker uses Fraction arithmetic from the archived Item306 module; it
does not require SymPy and does not run a bulk prime experiment.

## 1. The phase and second-branch scale cancel exactly

For fixed p, set e=1 if p=5 mod 6, and e=5 if p=1 mod 6. Put

    s0=(p-2e-3)/6,
    r_n=e+6n,  s_n=s0-2n,
    N=floor((p-2e+3)/12).

The actual rows are precisely 0<=n<N (when N>0). In particular N=p/12+O(1).
Write a_r=[X^r]A(X) and b_r=[x^r]C_+(x), with the branch definitions in
Items309 and314. The determinant gate is, up to the certified p-unit in
Item314, the residue of

    u_n=18*4^s0*16^(-n)*a_(e+6n)+11*b_(e+6n).              (1)

Indeed 2^(2s_n)=4^s0*16^(-n). Item309, equations(6.5)-(6.6), proves that
16^(-n)*a_(e+6n) satisfies exactly the same recurrence as b_(e+6n).
Consequently, with h=e/2+3n,

    sum_(j=0)^3 P_j(h) u_(n+j)=0,                          (2)

where P_j are Item237's degree-16 recurrence polynomials. Thus fixed-p
variation does not enlarge the order to six: it stays three. The initial
linear combination depends on p; the operator does not.

This argument uses the actual phase. Replacing it by an unrelated phase
would lose the cancellation.

## 2. The quintic singularity is removable in both directions

Let

    Q(h)=214443126+369944721h+239554248h^2
         +72513072h^3+10358560h^4+564080h^5.

The canonical factor lists give the exact identity

    P_0(h)=L_0(h)Q(h+3),   P_3(h)=L_3(h)Q(h),              (3)

where L_0 and L_3 are products of the recorded linear factors times their
rational scalar. The checker independently expands Q(h+3) and verifies
that it is precisely P_0's quintic core. Also gcd(Q(h),Q(h+3))=1.

Here is a compact exact definition of the reverse desingularization; it
specifies every coefficient without printing several pages of integers.
Use a superscript + for the shift h->h+3, and ++ for h->h+6. Let B be the
unique polynomial of degree at most four satisfying

    B = -P_1*(L_0 Q^{++})^(-1)  modulo Q^+.               (4)

The inverse exists in Q[h]/(Q^+). The exact arithmetic check verifies

    P_2 L_0^+ + B P_1^+ L_0 = 0 modulo Q^+,
    P_3 L_0^+ + B P_2^+ L_0 = 0 modulo Q^+.               (5)

Normalize (2) by P_0. If a_j=P_j/P_0 and

    b=Q^{++} B/Q^+,

add b times the shifted normalized recurrence to the original. This
gives the rational-function identity

    u_n + R_1(h)u_(n+1)+R_2(h)u_(n+2)
        +R_3(h)u_(n+3)+R_4(h)u_(n+4)=0,                 (6)

where R_j=a_j+b a_(j-1)^+ for 1<=j<=3, and R_4=b a_3^+.
Equations(3)-(5) cancel every quintic denominator. The fully reduced
denominators are monic products with the following roots; each root occurs
once and the remaining factor is exactly 1:

| Coefficient | Denominator roots in h |
|---|---|
| R_1 | -5,-3,-3/2,-15/4,-9/4 |
| R_2 | -8,-6,-3,-9/2,-3/2,-27/4,-21/4,-15/4,-9/4 |
| R_3 | -9,-6,-3,-15/2,-9/2,-3/2,-39/4,-33/4,-27/4,-21/4,-15/4,-9/4 |
| R_4 | -9,-6,-15/2,-9/2,-51/4,-45/4,-39/4,-33/4,-27/4,-21/4 |

The rational coefficient denominators themselves introduce a fixed finite
set of exceptional primes; they do not depend on h, n, or p. The largest
variable numerator after putting h=r/2 is 2r+51. Therefore all the displayed
denominators are p-units whenever s>=9, because p=2r+6s+3>2r+51. Factors of
the form r+c are smaller still. This bound includes the entire reverse
recurrence, not merely its leading or trailing coefficient.

The checker also constructs and verifies the analogous forward monic
order-four recurrence. Its denominators have only integer or half-integer
roots between -2 and -12, with no quintic core. The forward version is
useful independent confirmation but is not needed for the proof below.

## 3. The initial state cannot be zero

For each e, the n=0,1 rows of the two branch sequences have nonzero
determinant. Exact Lagrange inversion gives:

| e | a_e | 16^(-1)a_(e+6) | b_e | b_(e+6) | determinant |
|---|---:|---:|---:|---:|---:|
| 1 | -20/3 | -1414094/243 | -40/9 | -216470078/59049 | -252263000/177147 |
| 5 | -4004 | -727260625/243 | -868777/2187 | -25563514068625/86093442 | 143540931625/43046721 |

Exclude the prime divisors of these two nonzero determinant numerators and
the fixed coefficient denominators, together with the primes <=13 and the
prime divisors of 564080. This defines a fixed finite exceptional set E;
it need not be factored to establish the asymptotic statement. For p not
in E, the two branch columns remain linearly independent in their first
two coordinates. The coefficient vector (18*4^s0,11) is nonzero. Hence
u_0 and u_1 cannot both vanish modulo p.

One completely explicit definition of E is: take the prime divisors of
the product of the two displayed minor numerators, 2*3*5*7*11*13*564080,
and the denominators of every rational coefficient in P_0,...,P_3 and
the four reduced R_j stored in the JSON. This is finite and independent
of the research index. Small primes with fewer than four actual rows can
alternatively be covered by the additive constant in the final bound.

## 4. Rigorous zero-run and counting argument

First suppose u_j,u_(j+1),u_(j+2),u_(j+3) all vanish, and all four indices
are actual. If j=0, this contradicts Section3. If j>=1, apply (6) at j-1.
Since its last row is j+3, the start has

    s_(j-1)=s_(j+3)+8>=9.

Every denominator is therefore a p-unit, and the coefficient of u_(j-1)
is exactly 1. It follows that u_(j-1)=0. Repeating propagates the block
back to u_0=u_1=0, a contradiction. Thus there is no four-zero block.

Next suppose u_j,u_(j+1),u_(j+2) all vanish. Again j cannot be zero. The
absence of four-zero blocks implies u_(j-1)!=0. Apply the original (2) at
j-1. It follows that

    P_0(h_j-3)=0 modulo p.                                (7)

The start row has s_(j-1)=s_(j+2)+6>=7. Every linear factor of P_0 is a
p-unit at this row: the largest quarter-root factor is 2r+39<p.
By (3), equation(7) consequently implies Q(h_j)=0 modulo p.

For p not in E, Q is a nonzero polynomial of degree five modulo p. The
values h_j=e/2+3j are distinct in F_p for the actual indices because
their number is <p and p>3. There are therefore at most five all-zero
triple starting positions.

Partition any consecutive index interval I into disjoint blocks of three,
with at most two indices left over. Each block contributes at most two
zeros, except for at most five exceptional blocks. Hence

    #{n in I : u_n=0 mod p} <= (2/3)|I|+17/3
                            <= (2/3)|I|+6.               (8)

Item314 makes determinant vanishing equivalent to u_n=0 on every actual
row. Item334's simultaneous collision always implies determinant
vanishing, without dividing by a connection minor. Thus (8) applies to
the full collision support on every chart.

## 5. Exact aggregate consequence and its limit

For the original construction index M, the fixed-p map is

    M=(7p+e)/6+n.

Consequently restricting M to any interval restricts n to an interval,
so (8) can be summed without assuming independence across primes.
Let W(M) be the sum of log p over the actual Item334 collision primes,
and let R(M) be the corresponding sum over all possible ordinary-j=2
prime rows. For a dyadic block X<M<=2X,

    sum W(M) <= (2/3) sum R(M)+O(X).                      (9)

The error comes from O(1) per fixed prime; Chebyshev's bound gives
sum_(p<=12X/7) log p=O(X). Each fixed exceptional prime supports only
finitely many actual rows and so disappears from all sufficiently large
dyadic blocks.

The actual row interval is 4M/5<p<6M/7, up to bounded endpoint shifts.
The prime number theorem therefore gives

    R(M)=(2/35)M+o(M).

Combining with (9) proves

    limsup_(X->infinity) [sum_(X<M<=2X) W(M)]
                         /[6 sum_(X<M<=2X) M] <= 2/315.  (10)

The old raw ceiling was 1/105=3/315. Thus the averaged ordinary-j=2
ceiling is reduced by one third, namely 1/315 per normalized index.
The saving is strictly an averaged upper-cap reduction. It is not a
pointwise upper-cap improvement, not an almost-all o(M) estimate, not a
positive divisibility rate, and not a change in the proved lower bound
for the favorable-subsequence gain Gamma.

## 6. What this changes in the route ranking

The fixed-prime recurrence route has now delivered a concrete material
upper estimate, so the previous statement that the first usable actual
index theorem is entirely missing should be updated. It can be ranked
as a completed bounded-run step toward an upper estimate for this small
component. Its relevance to the main lower-gain target remains limited.

The sharper useful unresolved problem is now precise:

    For the particular sequence (1), prove
    #{0<=n<N : u_n=0 mod p}=o(p),

or prove such an estimate for the joint Item334 coordinate gate. The
operator and its degree are fixed, the phase has been absorbed exactly,
and quintic singularities no longer obstruct propagation. What is missing
is a bound on isolated or short-cluster zeros. A fixed-order recurrence
and exclusion of long zero runs alone do not give o(p): periodic sequences
can have fixed positive zero density. A discrete Stepanov argument would
need an additional algebraic-independence or nonperiodicity input specific
to these two branches. No finite-logarithm polynomial in the index with an
o(p)-degree perturbation has been constructed here. Existing Stepanov
theorems for zeros in the argument of a truncated function cannot simply
be applied to these coefficient indices.

Root requested that the attempt stop at the useful bounded result rather
than further package coordinates without an o(p) target; the present note
therefore leaves that narrower problem explicit.
