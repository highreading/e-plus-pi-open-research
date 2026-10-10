> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Raw endpoint and modified-moment interfaces for the signed Chebyshev producer

Coordinator derivation,8 October2026. These are exact interfaces and scoped
divisibility statements, not a primitive-error theorem. The source plane and
Smith/coefficient-content principles are already established and reused.

## Gate and provenance

Scoped archive searches for Chebyshev Laplace/source moments and coefficient
lattices found the existing quartic_four_power_primitive_content_smith_reduction.
Its sections1--3 were read: primitive coefficient content and selected output
Smith coordinates are distinct. No generic Smith/content theorem is claimed
as new. A superficially matching16n^2 recurrence in item165 was read through
section4; it is a DIFFERENT beta-continuant discriminant and is not imported.
Primary modified-moment literature searches identify classical ODE/integration-
by-parts methods, not an evaluated gcd theorem for this producer. The exact
Chebyshev ODE is read in DLMF18.8 Table18.8.1 row5, and the multiplication
recurrence in DLMF18.9 Table18.9.2. This scoped gate makes no exhaustive
novelty assertion. References:
https://dlmf.nist.gov/18.8.T1 and https://dlmf.nist.gov/18.9.T2.

## 1. A raw integer pair equal to the fully reduced pair

Use exactly the signed producer already defined: B(i)=d, F=B^2, K(i)=0,
eta(F)=I, eta(K)=-U<0, V=I-d^2,

    Wraw=U F+V K, Z=U d^2.

Let L=lcm(1,...,2N-1). Monic division gives integer polynomials

    QF=(F-d^2)/(1+t^2), QK=K/(1+t^2).

Keep the complete factorial endpoint E(H)=sum h_j(-1)^j j!, and define

    X=L*(E(F)-4*int_0^1 QF),
    Y=L*(E(K)-4*int_0^1 QK).

Both are integers, with all factorial endpoints at most2N and quotient
integration denominators at most2N-1. The COMPLETE integer pair is

    Araw=U X+V Y, Braw=L U d^2,
    C=gcd(Braw,Araw), p=Araw/C, q=Braw/C.             (1)

This p/q is exactly the primitive pair obtained with actual h, least
aggregate lambda and final G. Indeed Wraw=h Wprim, so Xraw=L*h*Rprim,
where Rprim=A/lambda in lowest terms. Thus

    (Araw,Braw)=(L*h/lambda)*(A,lambda*M).

The scalar is an integer: lambda divides L because the primitive quotient
is integer. Consequently

    C=(L*h/lambda)*G.                               (2)

No h, lambda or G has been omitted. L is used only in a common raw pair;
the reduced pair in(1) is invariant under such a common clearing.

## 2. A genuinely surviving divisor of actual q

For any integer raw pair Braw=U*(L d^2), its reduced denominator contains
U/gcd(U,Araw). Since Araw=U X+V Y,

    U/gcd(U,V Y) divides q.                         (3)

Proof prime by prime: if u=v_p(U), a=v_p(Araw), b=v_p(Braw)>=u,
then v_p(q)=max(0,b-a)>=max(0,u-a). This proves(3), including any
exceptional cancellation in Araw or polynomial content. In particular,

    q >= U/[gcd(U,V)*gcd(U,Y)].                     (4)

This follows because gcd(U,VY) divides gcd(U,V)*gcd(U,Y). The lower bound
may be weak, but it concerns FINAL q, not the coefficient clearer alone.

The proposed ordinary upper bound is exponential. The signed norm U has
factorial size. A no-go would follow from a sufficiently strong uniform
bound on the two scalar gcds in(4), together with an ACTUAL ordinary-error
lower bound. A success theorem instead needs an upper bound on q times the
actual error. Neither gcd bound is proved here. In particular U is not the
old factorial-polynomial T, and its prime support cannot be transplanted.

## 3. The coefficient-content divisor is only part of the payment

Let g=gcd(U,V), u=U/g, v=V/g, and let delta be the gcd of all nonzero
2-by-2 minors of the integral coefficient matrix[F K]. The polynomials
are linearly independent: K(i)=0 but F(i)=d^2!=0. For h'=content(uF+vK),

    h' divides delta, h=g*h'.                     (5)

Indeed h' divides u*(F_i K_j-F_j K_i) and v times the same minor for each
i,j, and gcd(u,v)=1. Bezout for u,v proves the claim. This is the standard
coefficient-lattice principle applied to the new producer. Delta is at most
the magnitude of any nonzero minor; the two columns have exponential
coefficient heights, so delta<=exp(O(N)). But g remains a genuine scalar
gcd, and the FINAL G in(2) remains genuine. Equation(5) does not settle(3).

## 4. A complete forced fourth-order Chebyshev source recurrence

Let C_j(t)=T_j(2t-1), and S_j=eta(C_j). The exact initial values are

    S0=1, S1=-1, S2=9, S3=-113, S4=1825.

For EVERY j>=2,

    S_(j+2)+12 S_(j+1)+(14-16j^2)S_j
      +12 S_(j-1)+S_(j-2)=8.                       (6)

To prove this, put x=2t-1 and bracket H as its integral against
e^((x-1)/2)/2 on(-infinity,1]. Then

    bracket(H')=H(1)/2-bracket(H)/2.

Use (1-x^2)T_j''-x T_j'+j^2 T_j=0. Two integrations by parts, retaining
the endpoint T_j(1)=1, give

    j^2 S_j=bracket((x^2/4+3x/2+3/4)T_j)-1/2.

For j>=2, xT_j=(T_(j+1)+T_(j-1))/2 and
x^2T_j=(T_(j+2)+2T_j+T_(j-2))/4. Substitution gives(6).
No factorial or derivative endpoint has been deleted.

The complete factorial endpoint E_j=E(C_j) has the DIFFERENT forcing

    E_(j+2)+12 E_(j+1)+(14-16j^2)E_j
      +12 E_(j-1)+E_(j-2)=-8*(-1)^j.               (7)

Its bracket ends at x=-1, where the boundary factor is -T_j(-1)/2.
That sign gives(7). For example E0=1,E1=-3,E2=25,E3=-307.

All S_j and E_j are odd: C_j has constant coefficient(-1)^j and all
nonconstant integer coefficients even. Therefore the gcd of ANY five
consecutive S_j, or any five consecutive E_j, is1. It divides8 by(6) or(7)
and is odd. This is a uniform five-term gcd theorem, not a theorem for two
arbitrary weighted combinations. Dropping8 would falsify that conclusion.

## 5. Express the ACTUAL source scalars through these moments

Write b_j=Im C_j(i). The product identity2 C_r C_s=C_(r+s)+C_|r-s| yields

    2 I = b_(N-1)^2*(1+S_(2N))
          +b_N^2*(1+S_(2N-2))
          -2*b_(N-1)*b_N*(S_(2N-1)+S1).           (8)

This keeps every cross term. The indices stop at2N exactly.
Let k(t)=t(1-t)(1+t^2)^2. Then eta(k)=-332 and

    U=166-(1/2)*eta(k*C_(2N-6)).                  (9)

The weighted moment in(9) is a finite, degree-six multiplier of Chebyshev
moments, with rational coefficients obtained from t=(x+1)/2. Its largest
moment index is2N, still the same boundary. Exact division by2 in(8)--(9)
is paid by the polynomial product identity. The analogous endpoint formulas
retain the forcing(7) and the complete arctangent quotient Y.

The important unanswered task is an evaluated gcd of the ACTUAL weighted
combinations U, I-d^2 and Y. Unimodular recurrence propagation and the
five-term gcd1 do not imply that gcd(U,I-d^2) or gcd(U,Y) is small. The
selected weighted direction, complete endpoint, original infinite N and
whole error must all be treated explicitly.
