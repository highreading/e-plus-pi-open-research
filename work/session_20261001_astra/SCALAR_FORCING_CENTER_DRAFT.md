> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Scalar forcing center: complete error and actual denominator

Status: new main-agent author deduction, not independently reviewed. This preserves the latest unsaved argument. No computation or independent verification is claimed. The construction uses the first forcing coordinate directly and requires neither contact normality nor a Toeplitz inverse. It differs from every previously selected Gram center.

## 1. Exact rational construction

Put Q0(z)=1-z+z^2/2 and F(z)=4 arctan(z/(2-z)). For n>=1 define

    fP=[z^n]Q0(z)^n D^n(1/(1-z)),
    fQ=[z^n]Q0(z)^n D^n((exp(z)+F(z))/(1-z)),
    c_n=fQ/fP.

These are rational coefficients. Let p_n be the established monic transformed Legendre polynomial, A_n=p_n(1)>0, C_n=binom(2n,n), and v_n=L(p_n/(1-t)), where L(g)=integral_-1^1 g((1+iu)/2)du. The exact positive-forcing identity is

    fP=n! C_n A_n>0.

Write S=e+pi. The complete forcing decomposition is

    fQ=S fP+eF+eE.

The logarithmic forcing satisfies exactly

    eF=-n! C_n v_n.                                  (1)

Indeed, the coefficient/derivative identity in the complete forcing representation gives

    eF=-L(t^n D_t^n[(t^2-t+1/2)^n]/(1-t)).

Rodrigues gives D_t^n[(t^2-t+1/2)^n]=n! C_n p_n(t). Also

    (t^n-1)/(1-t)=-(1+t+...+t^(n-1)).

Orthogonality of p_n to every polynomial of degree less than n removes this difference, proving (1). Consequently

    c_n-S=eE/fP-v_n/A_n.                             (2)

This identity includes both complete errors.

## 2. Complete signed error

Put M=1+sqrt(2) and s=M^(-2). The retained reference estimates give

    v_n/A_n=(-1)^n epsilon_n,
    2exp(-s)s^n<=epsilon_n<=8s^n/(1-s)^2.

The complete exponential forcing obeys

    |eE|<=27 M^n/(n+1).

Together with fP>=n! M^(n-1)/sqrt(n), this gives

    |eE/fP|<=27M/(sqrt(n)n!).                         (3)

The factorial bound in (3) is o(epsilon_n). Thus, eventually,

    sign(c_n-S)=(-1)^(n+1),
    epsilon_n/2<=|c_n-S|<=3epsilon_n/2,
    log|c_n-S|=-2n log M+O(1).                        (4)

No effective threshold is asserted here. This scalar argument does not need the newer vector saddle estimate or quantitative inverse theorem. Its inputs are the complete scalar forcing identity, Rodrigues orthogonality, the retained reference bounds, and (3).

In particular c_n converges to S, is eventually unequal to S, and cannot eventually stabilize. Its reduced positive denominators tend to infinity: if infinitely many remained bounded, convergence would force a subsequence from a finite set of rationals to equal S eventually, contradicting (4).

## 3. Exact integral numerator

Use the existing integer polynomial L_n(t)=2^n C_n p_n(t), with endpoint P_n=L_n(1)>0. Define

    Qcal_n=8 sum_(j=1)^n P_(j-1)P_(n-j)/j,
    E_d=sum_(r=0)^d 1/r!, D_d=d! E_d,
    a_s(n)=[z^s]Q0(z)^n,
    Acal_n=sum_(s=0)^n (n)_s a_s(n) D_(2n-s).

The established second-kind identity gives

    L((L_n-P_n)/(t-1))=Qcal_n.

For clarity the exponential part of fQ is exactly

    sum_(s=0)^n a_s(n)(2n-s)! E_(2n-s)/(n-s)!
      =Acal_n/n!.

The logarithmic part, by (1), is n! Qcal_n/2^n. Since fP=n!P_n/2^n,

    c_n=[(n!)^2 Qcal_n+2^n Acal_n]/[(n!)^2 P_n].     (5)

Put N_n=(n!)^2 Qcal_n+2^n Acal_n and Z_n=(n!)^2 P_n. Both are integers. In fact 2^n clears every coefficient of Q0^n, so 2^n Acal_n is integral; n! clears every denominator j in Qcal_n. Therefore the ACTUAL reduced denominator is

    q_n=Z_n/gcd(Z_n,|N_n|).                          (6)

An integer clearer is not substituted for q_n. All complete numerator terms remain in (5).

## 4. An all-index 5-adic law

The existing all-residue transfer applies to this same Acal_n. Its five exact seeds, obtained by the displayed finite formula, are

    Acal_0,...,Acal_4 = 1,3,21,394,13293.

Their residues modulo 5 are 1,3,1,4,3. Hence Acal_n is a 5-adic unit for every n.

The transfer can also be seen directly: in its defining sum, falling factorials remove all terms beyond r=n mod 5; surviving coefficients transfer by Frobenius. The recurrence D_d=d D_(d-1)+1 resets at multiples of 5, so the remaining D indices also transfer to the seed at r. No division by a multiple of 5 is introduced.

The endpoint generating function is

    G(z)=sum_n P_n z^n=(1-4z-4z^2)^(-1/2).

Over F_5 it satisfies

    G(z)=(1+2z+3z^2+2z^3+z^4)G(z^5).

Every base-5 digit multiplier is nonzero. Therefore P_n is a 5-adic unit at every index.

For n>=5,

    v_5(Qcal_n)>=-floor(log_5 n),
    2v_5(n!)>floor(log_5 n).

For the strict inequality, if k=floor(log_5 n)>=1, Legendre's formula gives v_5(n!)>=(5^k-1)/4>=k. Thus (n!)^2 Qcal_n has positive valuation, whereas 2^n Acal_n is a unit. The complete numerator N_n is a unit. Equation (6) proves

    v_5(q_n)=2v_5(n!), n>=5.                          (7)

This is a new consequence for this scalar construction, using the retained transfer framework. No new residue scan or execution is claimed. In particular

    log q_n >= (log 5)n/2-O(log n).

This lower bound supplies no useful upper bound.

## 5. Remaining irrationality criterion

From (4), a sufficient same-index arithmetic result would be

    limsup log q_n/n < 2log(1+sqrt(2)).                (8)

Then the primitive forms q_n(S-c_n) would be nonzero eventually and tend to zero, proving irrationality. Neither (8) nor any substitute upper bound of sufficient strength is established.

Adjacent eventual errors have opposite signs. Thus their rational centers differ, and rational separation gives

    1/(q_n q_(n+1))<=|c_n-c_(n+1)|<=C M^(-2n)

for some fixed C. Consequently

    log q_n+log q_(n+1)>=2n log M-O(1).

The 5-adic lower law is compatible with this stronger two-index constraint; it is not a complete description of q_n.

The unresolved arithmetic is precisely the final gcd in (6). The existing Gram-center gcd formulas cannot be transferred to this new center without derivation. Failure of a sufficient bound would concern this construction, not resolve e+pi.

## 6. Scope

The new author conclusions are the scalar reduction, complete eventual sign, exact denominator formula, and law (7). No independent PASS is claimed. This note preserves the argument before further research into its gcd, recurrence, or rational combinations. The unconditional rationality or irrationality of e+pi remains unresolved.
