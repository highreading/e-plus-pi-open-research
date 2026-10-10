> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The surviving h1 logarithmic moment is an integer prime-index jet

Author result, target L16, 2026-10-02. This derives an actual relation for the moment retained in H1_EXPLICIT_MOMENT_CANCELLATION_POLYNOMIAL.md. It also states a narrow functional obstruction to eliminating it. No independence of residues modulo primes is inferred from functional independence, and no new prime atlas is run.

Let

    alpha(z)=1/q0(z), q0(z)=1-z+z²/2,
    L(z)=integral_0^z alpha(t)dt=2atan(z/(2-z)),
    A(z)=e^z alpha(z), J(z)=e^z/(1-z),
    K(z)=J(z)L(z).

Write a_n=alpha^(n)(0),S_n=A^(n)(0),D_n=J^(n)(0),T_n=K^(n)(0). These names are local to this note; D_n and T_n are scalar jets, not the Gram denominator or the selector's factorial clearer. All four sequences are integers. Exact recurrences are

    a_0=1,a_1=1,
    a_n=n a_(n-1)-binom(n,2)a_(n-2), n>=2;
    S_0=1,S_1=2,
    S_n=n S_(n-1)-binom(n,2)S_(n-2)+1, n>=2;
    D_0=1,D_n=n D_(n-1)+1;
    T_0=0,T_1=1,
    T_(n+1)=(n+2)T_n-nT_(n-1)+S_n, n>=1.             (1)

The first two follow by taking jets of q0 alpha=1 and q0 A=e^z. The third is the usual factorial-companion recurrence. Finally

    (1-z)K'-(2-z)K=A

gives the last recurrence. Equivalently the literal Hurwitz product identity is

    T_n=sum_(j=1)^n binom(n,j)a_(j-1)D_(n-j).         (2)

Thus integrality in(1) is not merely generic coefficient clearing.

## 1. Exact reverse-factorial relations

For any odd prime p, set chi=(-1|p), C=C_p=D_(p-1) mod p. Use the actual h1 moments U=mu_0,W=mu_1,Lambda=lambda_0 from the preceding note. Then

    U=S_(p-1),
    W=S_(p-1)+S_(p-2)/2,
    Lambda=-T_(p-1)-chi C                         mod p.       (3)

These identities hold without the endpoint-digit unit assumption. They are arithmetic identities for the actual finite moment sums, rather than a functional-independence inference.

For the first relation, Wilson gives

    1/(p-1-t)!=(-1)^(t+1)t! mod p,0<=t<p.

Hence [z^(p-1)]e^z alpha=-mu_0, and the left coefficient is -S_(p-1) modulo p. The shifted rational series satisfies

    (alpha-1)/z=(1-z/2)alpha,

so the same reversal gives the second relation, including the factor(p-1)/2=-1/2.

For the third relation split the lambda sum at t=p-1. At 0<=t<=p-2,

    (-1)^t t! D_(p-2-t)
       = (1/(t+1))sum_(s=0)^(p-2-t)1/s! mod p,

because t!(p-2-t)!=(-1)^t/(t+1). Their complete sum is exactly

    [z^(p-1)] e^z L(z)/(1-z).

The last term is -alpha_(p-1)C. The Gaussian roots r=(1+i)/2,rbar=(1-i)/2 yield

    alpha_(p-1)=(r^p-rbar^p)/(r-rbar)=chi mod p,

also in the split F_p[i] algebra. The coefficient of K is -T_(p-1) by Wilson, proving(3). The factor1/(1-z) is essential: the scalar D jet contains a partial exponential sum, rather than a single exponential coefficient. Omitting that factor would give an incorrect mu-only identity.

## 2. The complete numerator as one explicit integer-sequence congruence

Substitute(3) into the exact h1 quotient polynomials. For b4,m1,

    nu/4 = -85T_(p-1)+(156-194C)S_(p-1)
                 +(163-97C)S_(p-2)+(12-85chi)C-78 mod p.      (4)

For b5,m1,

    nu/384 = -93T_(p-1)+(24C+90)S_(p-1)
                 +(155-31C)S_(p-2)-(148+93chi)C-28 mod p.     (5)

These congruences retain the full correction in nu. They turn the unit condition into a fixed integer-recurrence problem. They do not prove that(4) or(5) is nonzero for all primes.

In particular, at p>10,p!=31 where all endpoint digits are units, the exact b5 denominator constant35712 is a unit. If the integer combination in(5) is a unit, the existing all-depth origin/boundary comparison with COMPLETE beta gives, throughout n=-1 modulo p and at every depth,

    v_p(D_Gram)=2v_p(n+1), v_p(V_Gram)=2v_p(n+1),
    v_p(q_n)=2v_p(n!) for every normal n>=2p.                 (6)

Here q_n is the final reduced denominator. If(5) vanishes, this note establishes only an extra first digit of numerator content; it makes no claim of smaller actual q or shrinking primitive forms.

## 3. What the prime reset does and does not determine

The integer Hurwitz product rule and binom(p,j)=0 mod p at0<j<p give

    a_(p-1)=-chi, a_p=0,
    S_p=1, T_p=a_(p-1)=-chi mod p.

Evaluating the T recurrence at n=p-1 therefore gives the actual additional relation

    T_(p-1)+T_(p-2)=-U-chi mod p.                            (7)

The reset fixes this sum and does not isolate the surviving T_(p-1). This explicitly identifies the scalar logarithmic connection value still left in(4),(5). The claim that a factorial reset alone reduces Lambda to U,W,C would require a further identity, not supplied by(1) or(7).

## 4. A precise functional obstruction, with its arithmetic limit

K is transcendental over C(z,e^z). This follows from elementary logarithmic monodromy, not a new general theorem about E/G-function values. A loop around z=1+i adds2pi to L, because Res_(1+i)(1/q0)=-i. It therefore adds2pi J(z) to K, while z,e^z and rational functions of them remain single-valued. At a generic base point J is nonzero. Repeating the loop would give infinitely many roots of a purported nonzero polynomial relation for K over that field, a contradiction.

Consequently K cannot be represented by rational field operations on the single-valued meromorphic companions alpha,A,J and their finitely many derivatives. A corresponding sequence obstruction is that no eventual identity can express T_n as a finite sum of polynomial-in-n multiples of forward shifts of the a_n,S_n,D_n sequences: their exponential generating functions, obtained through derivatives and z∂_z, remain single-valued meromorphic, and a finite exceptional prefix adds only a polynomial. Such an identity would make K single-valued meromorphic and contradict the preceding loop.

This obstruction is deliberately narrow. It does NOT forbid every recurrence with an inhomogeneous forcing—(1) is one—nor every integration, backward shift or nonlinear coefficient operation. It also does NOT prove algebraic independence of Lambda,U,W,C modulo primes, exclude accidental prime-index identities, or establish a supply of numerator units. The functional E/G-independence primary papers in the target ledger are background and are not invoked to obtain any modular or endpoint conclusion.

## 5. Receipt and remaining task

h1_logarithmic_jet_relation.py computes the exact integer recurrences and verifies(2) only at the eleven h1 primes already used by the saved b4/b5 quotient receipts. H1_LOGARITHMIC_JET_RELATION_RECEIPT.json retains S_(p-1),S_(p-2),T_(p-1),T_(p-2),the actual moments and complete nu. This is supporting evidence for the new identity, not a new atlas or a numerical theorem.

The new result is the actual relation(3), the complete integer numerator gateways(4),(5), and the explicit connection obstruction(7). A nonzero theorem or a higher-content transfer for these integer combinations remains open. The final evaluated q is still determined only through the complete beta comparison in(6), not through the growth of T_n or unnormalized coefficient content.
