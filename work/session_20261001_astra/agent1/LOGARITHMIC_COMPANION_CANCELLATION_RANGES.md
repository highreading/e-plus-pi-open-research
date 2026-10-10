> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Logarithmic companion: deterministic cancellation ranges

New author research, 2026-10-01. English and offline. The completed prime-support and odd-gate papers are retained without repeated calculations or readbacks. No numerical execution, prime scan, or independent review is claimed.

## 1. Retained arithmetic and the new question

Let n=4k, k>=1, m>=0, N=2n+4m, and J=n+4m. Write

    F(x)=(1+2x+2x^2)^n(1-2x^2)^(2m)=sum_h c_h x^h,
    U=c_n!=0,
    T=calL((K-U)/(t-1)), Bbeta=den(T/U).

The retained rational identity is

    T=sum_{d=-n, d!=0}^J c_(n+d) tau_d/d,
    tau_d=(2/i)(((-1+i)/2)^d-((-1-i)/2)^d).

For an odd prime p<=J, put Q=p^e with e=floor(log_p J), so Q<=J<pQ. The retained highest-layer formula is

    p^e T=S_p modulo p,
    S_p=chi_p^e sum_{a in I_p} c_(n+aQ) tau_a/a,
    I_p={a!=0:-n<=aQ<=J}, chi_p=(-1)^((p-1)/2).       (1)

Every |a| in I_p is less than p. Negative a are part of (1) whenever Q<=n.

The new results below are sufficient integer floor and digit conditions for S_p=0. They remove a factor p from the possible denominator of T before division by U. They do not assert that p disappears from Bbeta.

Use P(x)=1+2x+2x^2 and C(x)=1-2x^2. Thus F=P^n C^(2m).

## 2. A complete monomial-support criterion

The endpoint powers satisfy

    tau_(a+4)=-tau_a/4,
    tau_0=0, tau_1=2, tau_2=-2, tau_3=1.

Consequently tau_a is zero exactly when 4 divides a; otherwise it is a signed power of two and is a unit at every odd prime. This applies to negative a as well. The weights in (1) therefore introduce no additional zero factors except a divisible by four.

Write the base-p digits as

    n=sum_l n_l p^l, 2m=sum_l m_l p^l.

The retained Frobenius product is

    F(x)=product_l P(x^(p^l))^(n_l) C(x^(p^l))^(m_l)
          modulo p.                                  (2)

Before collecting like powers, the possible degrees contributed by digit l are

    E_l={u+2v:0<=u<=2n_l, 0<=v<=m_l}.

Explicitly, E_l is the full integer interval [0,2(n_l+m_l)] when n_l>0, and is the even integers in [0,2m_l] when n_l=0. Every degree in this set has at least one monomial realization whose coefficient is a p-unit: choose linear and quadratic factors in P^(n_l), and quadratic factors in C^(m_l). All multinomial factorials have arguments less than p.

This is a monomial-support set, not an assertion that the collected coefficient is nonzero. Different monomials can cancel modulo p.

Here is an exact finite digit criterion for membership in that support. For a target h>=0 with digits h_l, start with carry z_0=0. A path consists of integers d_l in E_l and nonnegative carries z_(l+1) satisfying

    d_l+z_l=h_l+p z_(l+1),

and ending with zero carry after all digits of the product and target have been processed. Such a path exists if and only if h is a possible exponent of an uncollected monomial in (2). This follows by successive base-p addition; conversely the carry equations reconstruct the degree sum.

It follows that the following criterion guarantees cancellation without evaluating any coefficient:

    For every a in I_p with 4 not dividing a,
    the target h=n+aQ has no digit path.               (3)

Then every corresponding coefficient in (1) is zero modulo p, and S_p=0. Criterion (3) fully describes what can be certified solely by absence of monomials in the Frobenius product. If a path exists, the criterion leaves open cancellation among coefficients or among the weighted terms of S_p.

The next two results turn this criterion into explicit floor ranges.

## 3. Cancellation range A: a missing carry near a prime power

Let r=p^h with 1<=h<e, and suppose

    r divides n,
    A=n/r,
    B=floor(2m/r), s=2m-Br, 0<=s<r,
    A+2B=p^(e-h)-1,
    (r+1)/2<=s<=r-1.                                (4)

These conditions imply A<p^(e-h), hence n<Q. They also give

    J=Q-r+2s,
    Q+1<=J<=Q+r-2<2Q.

Thus Q is indeed the highest p-power at most J, and I_p={1}. No negative Laurent index exists in this particular range because n<Q.

Frobenius at the scale r gives

    F(x)=P(x^r)^A C(x^r)^B C(x)^s modulo p.

The last factor has only even powers and degree 2s<2r. Among its exponents divisible by the odd integer r, only zero occurs: exponent r is odd, and exponent 2r exceeds the degree. Therefore, for every integer v>=0,

    c_(rv)=[y^v]P(y)^A C(y)^B modulo p.               (5)

For the required target n+Q, the right side has index A+p^(e-h). Its polynomial has degree

    2A+2B=A+p^(e-h)-1.

The target is one degree beyond its support. Hence

    c_(n+Q)=0 modulo p, S_p=0.                       (6)

This proves a deterministic cancellation band immediately above Q, with a divisibility condition on n. It uses a degree obstruction and parity, not an unevaluated residual coefficient.

For example, the e=2, h=1 form is particularly simple:

    n=A p, A a positive multiple of four,
    A+2 floor(2m/p)=p-1,
    (p+1)/2<=2m mod p<=p-1.

Every integer tuple satisfying these conditions has S_p=0. When discussing Bbeta, U!=0 remains an independent domain requirement. No nonvanishing theorem for U is inferred from this cancellation band.

Every prime certified by (4) divides n. Consequently, even taking the union over all possible h and e, its one-factor removable mass obeys the unconditional bound

    sum_{p certified by (4)} log p<=log n.            (7)

Repeated ways of certifying the same prime count only once.

## 4. Cancellation range B: an odd high block with no low carry

Let r=p^(e-1), with e>=2. Suppose

    n<r,
    2m=A r+s, 0<=s<r,
    (p+1)/2<=A<=p-1,
    n+2s<r.                                         (8)

Equivalently the last condition is

    0<=2m mod r<=floor((r-n-1)/2).

Then

    J=2A r+n+2s,
    Q<J<2Q,
    n<Q,

so again Q is the highest p-power at most J and I_p={1}.

The exact characteristic-p factorization is

    F(x)=P(x)^n C(x)^s C(x^r)^A.

The low factor has degree 2n+2s<n+r. Among its exponents congruent to n modulo r, only n is possible: n-r is negative and n+r exceeds the degree. Thus

    c_(n+Q)=[x^n]P(x)^n C(x)^s * [y^p]C(y)^A
              modulo p.

The final coefficient is zero because C(y)^A is even and p is odd. Therefore

    S_p=0.                                          (9)

This second range does not require p to divide n. It uses only floor inequalities, parity, and the exact factorization; the low coefficient need not be evaluated or assumed nonzero.

All primes certified here satisfy

    p=Q/r<=J/r<J/n.

The elementary retained bound lcm(1,...,L)<=4^L gives

    sum_{p certified by (8)} log p<=(J/n) log 4.     (10)

For m~rho n log n, the right side is O_rho(log n). Combining (7) and (10), the total one-factor saving certified by these two explicit ranges is at most

    log n+(J/n)log 4=O_rho(log n).                   (11)

These are upper bounds on the available guaranteed saving, not lower bounds asserting that any particular moving interval contains a prime. The ranges can be empty at individual indices.

## 5. Why monomial support alone cannot give a leading saving

There is a stronger limitation on criterion (3), beyond the two displayed bands. Each of the following constructions supplies a p-unit monomial at an index whose weight tau_a/a is nonzero.

### 5.1 If Q<=n, a negative index is always supported

Write n=AQ+r, 0<=r<Q. Since n<=J<pQ, one has 1<=A<p. In the lower digit factors of P^n, choose every factor linearly, giving degree r and a power-of-two coefficient. In P(x^Q)^A choose A-1 linear factors and one constant factor, giving degree (A-1)Q with coefficient A*2^(A-1), a p-unit. Choose all C factors constant.

The resulting exponent is n-Q, corresponding to a=-1 in (1). Since tau_(-1) is a unit, the support criterion cannot certify cancellation here.

This does not prove S_p!=0. It proves that omitting the negative Laurent index would remove an actual admissible contribution and could produce a false support argument.

### 5.2 If n<Q and 2m>=Q, a=2 is always supported

The digit floor(2m/Q) lies between one and p-1. Choose one quadratic term at scale Q in the C factors, all other C factors constant, and every P factor linearly. The exponent is n+2Q, corresponding to a=2. Its monomial coefficient is a p-unit. Also 2Q<=J, so this index is in I_p.

Again criterion (3) cannot certify cancellation, because tau_2 is a unit.

### 5.3 The remaining case when e=1 always supports a=1

Suppose Q=p, n<p, and 2m<p. Since p<=J and J is divisible by four, J>=p+1. Put

    v=(p-n+1)/2.

This is a positive integer and v<=2m. Choose one linear and n-1 quadratic terms from P^n, giving degree 2n-1 and coefficient n*2^n. Choose v quadratic terms from C^(2m). Since n and 2m are less than p, this monomial coefficient is a p-unit. Its exponent is

    2n-1+2v=n+p.

Thus a=1 is supported, and tau_1 is a unit.

These three cases cover every prime with e=1. They prove:

    Every prime eliminated by the monomial-absence criterion (3)
    must have e>=2, and therefore p<=sqrt(J).          (12)

This is a limitation of support-only reasoning, not a noncancellation theorem for the actual sum S_p. Collected coefficients or distinct weighted terms can still cancel at primes with e=1.

Let R_supp be the product of distinct primes certified by (3). Without any prime-distribution assumption,

    log R_supp<=log lcm(1,...,floor(sqrt(J)))
              <=sqrt(J)log 4.                        (13)

Even hypothetical removal of every power of every prime p<=sqrt(J) from O_J would save at most

    sum_{p<=sqrt(J)} floor(log_p J)log p
       <=sqrt(J)log J=o(n log n)                     (14)

when m~rho n log n. Thus no leading n log n saving can follow solely from missing monomials in the Frobenius product. A leading improvement must use actual cancellation of coefficients or of the weighted Laurent sum at primes with e=1.

The argument establishes no density statement about those cancellations.

## 6. A short exact obstruction for the primes relevant to a leading saving

Primes p<=n have total one-factor logarithmic mass at most n log 4=o(n log n). Together with (14), this places the main unresolved mass at primes

    p>max(n,sqrt(J)), p<=J.

Here e=1 and no negative Laurent index occurs. Write

    2m=M p+r, 0<=r<p,
    d=floor((n+2r)/p), so d is 0, 1, or 2,
    ell_v=[x^(n+vp)]P(x)^n C(x)^r, 0<=v<=d.

Frobenius gives

    F(x)=P(x)^n C(x)^r C(x^p)^M modulo p.

The low factor contributes only the three possible residue-class coefficients ell_0, ell_1, ell_2. Define, for 0<=v<=d,

    Phi_v(M)=sum_{h=0}^M, v+2h!=0
       binom(M,h)(-2)^h tau_(v+2h)/(v+2h).

Every denominator in this sum is a p-unit: v+2h is at most

    2M+d=floor(J/p)<p.

Coefficient extraction in (1) now yields the exact three-coefficient reduction

    S_p=chi_p sum_{v=0}^d ell_v Phi_v(M) modulo p.    (15)

There are deterministic floor simplifications:

* If n+2r<p, only ell_0 Phi_0(M) remains.
* If p<=n+2r<2p, only ell_0 Phi_0(M)+ell_1 Phi_1(M) remains.
* If 2p<=n+2r<3p, all three terms can occur.

These simplify the deciding congruence; they do not assert that its remaining terms are zero.

When the third term is present, its scalar has the closed expression

    Phi_2(M)=-((1+i)^(M+1)-(1-i)^(M+1))/(2i(M+1)).   (16)

To see this, integrate x(1-2x^2)^M between a_minus and a_plus and multiply by 2/i. Its primitive is -(1-2x^2)^(M+1)/(4(M+1)); at the endpoints 1-2a_plus^2=1+i and 1-2a_minus^2=1-i. The denominator M+1 is a p-unit in this domain.

In particular Phi_2(M)=0 exactly over Q when M+1 is divisible by four. This removes the third term on an explicit congruence class, but leaves the first two terms of (15). It alone does not certify S_p=0.

For M=0, Phi_0(0)=0, Phi_1(0)=2, and Phi_2(0)=-1 whenever those indices are present. The one-pole interval from the retained paper has M=0 and d=1, recovering its single translated coefficient condition.

The gap-one survival theorem is fully consistent with these ranges. At p=J-1, e=1, M=0, d=1, and the retained coefficient is ell_1=n*2^(N/2), a p-unit. Thus (15) retains the known nonzero value -2n*2^(N/2). Neither cancellation band includes this prime, and the support criterion has an admissible a=1 term.

Equation (15) is the remaining first-layer obstruction for the leading range. Establishing substantial aggregate cancellation requires an actual relation between these collected coefficients and scalar weights, beyond their degree or digit support.

## 7. Denominator refinement and the endpoint distinction

Let C_supp be any set of primes certified by (3), including either explicit floor band. Count each prime once and put

    D_supp=O_J/product_{p in C_supp}p.

The retained highest-layer identity, together with S_p=0 at these primes, proves

    D_supp T belongs to 2Z,
    Bbeta divides D_supp |U|/2.                      (17)

At a certified prime the guaranteed statement is only

    v_p(T)>=1-e.

For e>=2 this generally leaves a possible pole of order e-1. Even if T becomes p-integral, division by U can introduce or preserve the prime.

The exact local interface remains

    R_p=p^e T in Z_(p), u_p=v_p(U),
    v_p(Bbeta)=max(0,e+u_p-v_p(R_p)),                 (18)

with the zero-numerator convention. Absence of p from Bbeta requires

    R_p=0 modulo p^(e+u_p).                          (19)

A support proof gives only the first factor p in R_p. It does not give (19) unless the required precision is one. The exact lift must restore all Laurent terms

    R_p=sum_{d=-n,d!=0}^J c_(n+d) p^e tau_d/d,

including the negative terms and the coefficients whose first residues were zero. A missing monomial in characteristic p proves a coefficient divisible by p; it need not make that integer coefficient zero at higher precision.

Cancellation against U is the separate endpoint-content step in the retained exact factorization of Bbeta. None of the floor ranges assumes U is a p-unit or counts its content twice.

## 8. Rate consequence and confirmed transfer threshold

For m~rho n log n, the retained bound log|U|=o(n log n) applies. The explicit bands save at most O_rho(log n), and every possible monomial-support certification saves o(n log n) by (13)-(14). Thus these new deterministic support results do not improve the leading denominator rate furnished by the existing elementary estimate O_J<=4^J:

    limsup log Bbeta/(n log n)<=4rho log 4.

This is an upper bound for the actual companion denominator through (17), not an identification of that denominator with its clearer. Its subleading refinement does not determine the actual rate, which can be smaller through the unresolved coefficient and endpoint cancellations.

The main has now confirmed the external pi input with safe exponent 36/5. The useful strict transfer threshold is therefore

    limsup log Bbeta/(n log n)<5/82.

The present results supply no new leading-rate extension of the regime already implied by the existing bound. In particular, multiplying or shrinking a moment clearer by a subleading factor does not by itself prove an improved actual-companion rate at this threshold.

The remaining work is concrete: for the leading primes, quantify zeros of the collected three-term expression (15), or prove stronger global content cancellation; after a first zero, compare the full lift (18) with e+v_p(U). No uniform coefficient cancellation, supply of primes in moving intervals, or favorable higher-depth estimate is assumed.

These are original author proofs. No earlier successful calculation was repeated, no prior paper was audited, and no conclusion about rationality or irrationality of e+pi is asserted.
