> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: both actual even-degree P gates

Date: 2026-09-13. Reviewer: audit_sources.

**Result: pass.** The proof in `raw_even_P_second_dyadic_gate.md`
establishes, for every even n>=2 and s=1,2,

    v_2(p_s) >= v_2(Xi_n)+min(n,v_2(n)+1).

Together with the previously reviewed B-coefficient theorem and
the exact cubic coefficient identities, it proves that the actual
accessory cubic has no triple root in every even degree. It does
not prove squarefreeness or solve the arithmetic question about
e+pi.

## 1. The actual moments and all normalization factors

The raw functional L(t^a) is the Taylor coefficient of arctan(z)
at exponent a+1. For U(t)=t^n C(1/t), the coefficient of
C(z)arctan(z) at exponent n+1+k is therefore exactly L(t^k U).
The absence of an A coefficient at that exponent proves the
displayed moment identity for 0<=k<=2n-1. This uses the full
canonical polynomial, not a top-row approximation.

The monic recurrence has coefficient j^2/(4j^2-1), so each Q_j
is in Z_(2)[t]. The norm

    h_j=(-1)^j 4^j / ((2j+1) binom(2j,j)^2)

has valuation 2phi(j), including h_0=1. The unit assertions for
Q_(2r)(0) and Q_(2r+1)'(0) follow from the displayed recurrence
and derivative formula without renormalizing Q_j.

For N>=n+1, every actual term b_j/(N-j)! has valuation at least
phi(n)-phi(N). The same bound applies to every monomial in Q_j,
with the weakest of its denominators at N=n+1+j. Orthogonality
then gives

    v_2(u_j) >= phi(n)-phi(n+1+j)-2phi(j), j<n.

The factor 2phi(j) is precisely the norm valuation; no additional
leading coefficient or factorial belongs in this formula. All
needed moments are within the proved range, since j<n.

The right side is nonincreasing in j and at j=n-1 equals
-n-2phi(n-1), which is at least M. At even n, evaluating U at
zero recovers c_n; the coefficient Q_n(0) of u_n is a unit.
The already reviewed c_n bound then gives v_2(u_n)>=M. Thus
all orthogonal coefficients, and hence all monomial coefficients,
of the full U have valuation at least M. There is no cancellation
assumption in this last step: subtracting terms of valuation at
least M preserves that lower bound.

## 2. The polarized identities, including parity and the factor 2

I independently differentiated the full polarized expression

    T_ij=2QiQj+D(Qi Sj'+Qj Si'-Qi' Sj-Qj' Si).

Using (D Q_j')'=lambda_j Q_j and
(D S_j')'=lambda_j S_j-2Q_j' leaves exactly

    T_ij'=(lambda_j-lambda_i)(Qi Sj-Qj Si).

This convention is the full cross term in the quadratic
expansion T_U=sum u_i^2 T_(Q_i)+sum_(i<j)u_i u_j T_ij;
there is no extra factor 2 when the terms are summed. The
coefficient extraction at t^2 does divide the derivative by 2,
which accounts for the -1 in the valuation bound (18).

For even indices, the identity for S_i'(0) gives two
-Qi(0)Qj(0) terms with opposite signs. They cancel exactly;
the remaining norm terms have valuation at least 2phi(i).
For odd indices, Q_i'(0) is a unit and
S_i(0)=h_(i-1)/Q_(i-1)(0) has valuation 2phi(i), so the
same lower bound holds. This includes i=0 in the even case:
S_0'(0)=1-1=0.

Equal parities make j+i+1 odd, and hence give

    v_2([t^2]T_ij) >= 2phi(i)+v_2(j-i)-1.

Opposite parities make T_ij odd and its quadratic coefficient
zero. The diagonal expressions are constant, so there are no
unexamined diagonal contributions.

## 3. Uniform summation bounds and the exceptional adjacent pair

For a same-parity pair i<j<=n, necessarily i<=n-2 and j-i is
even. Use the sharper bound on u_i and the uniform M bound on
u_j. Then

    v_2(u_i u_j [t^2]T_ij)
      >= M+phi(n)-phi(n+1+i)+v_2(j-i)-1
      >= M+phi(n)-phi(2n-1)
      = K+v_2(n)+1.

Thus the displayed estimate (19) is valid for all pairs at once,
including j=n. Neither i=n nor i=n-1 can occur as the smaller
index of a same-parity pair. No asymptotic or growing-index
qualification is needed.

For the linear coefficient, the opposite-parity bracket at zero
has valuation at least 2phi(i), and the eigenvalue difference has
at least one factor 2. When i<=n-2 this gives K+v_2(n)+2.
The only pair with i=n-1 is (n-1,n); its eigenvalue difference
is exactly 2n. The sharper bound for u_(n-1), together with the
exact valuation of its second-kind central value, gives
K+v_2(n)+1 as written in (20).

All sums are finite. Addition and possible cancellation can only
increase these lower bounds. The n=2 case includes i=0 and the
single exceptional adjacent pair and is covered without a
separate numerical check.

## 4. Exact low reconstruction and the exponential correction

The polynomial part of U(t)arctan(1/t) is S_U(t). Reversing the
actual Taylor reconstruction of A therefore gives exactly
V=-S_U-E_B. The sign in

    t^(2n)P(1/t)=T_U+D(E_B'U-E_BU')

is correct. The earlier coefficient bound on B applies to every
term of every low Taylor coefficient, so E_B is dyadically
integral. More precisely its coefficient at t^s has valuation
at least phi(n)-phi(n-s), for 0<=s<=n.

Every coefficient of U is at least M, and ordinary
differentiation multiplies coefficients by integers. Therefore
the entire correction has coefficientwise valuation at least
M=K+n. Combining it with the preceding T_U bounds proves the
claimed min(n,v_2(n)+1) for both p_1 and p_2. This argument
handles the exponential contribution exactly; it does not
silently discard an appended-row or endpoint-border term.

## 5. Cubic consequence and exact limitations

At even n, b_n is a unit and both b_(n-1),b_(n-2) are even.
The new theorem makes p_1/p_0 and p_2/p_0 even. Substitution in
the previously independently checked cubic formulas gives

    q_2/q_3 = 0 mod 2,    q_1/q_3 = 1 mod 2.

Thus (q_2^2-3q_3q_1)/q_3^2 is a unit and is nonzero in Q.
The all-index leading-B/Xi theorem ensures q_3!=0, so this is
indeed a cubic. A triple root over the algebraic closure would
force that expression to vanish; it is excluded.

The conclusion allows a double root. It does not bound the
height of the three-integer endpoint carrier, the size of any
primitive denominator, or the Archimedean remainder. The new
argument does not use squarefreeness, normality over a finite
field, or the conclusion it is intended to prove.

No new canonical solve or numerical scan was used in this review.
The moment proof independently strengthens the earlier first-gate
determinant argument, whose review remains valid as a separate
proof.
