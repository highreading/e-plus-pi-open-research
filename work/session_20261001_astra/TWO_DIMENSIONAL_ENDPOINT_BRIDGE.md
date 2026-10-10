> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Two-dimensional endpoint bridge

Status: new main-agent elementary deductions. Not independently reviewed. No unconditional conclusion about e+pi follows without the unresolved estimates stated below. This note introduces a relaxed-contact construction and an exact arithmetic bridge; it does not reopen a completed audit.

## 1. Relaxed contact and endpoint kernel

Let a,b,c be positive integers, M=a+b+c, and

    F(z)=4 arctan(z/(2-z)),  F(1)=pi.

Its Taylor coefficients at zero are rational. Let V be the rational vector space of polynomial triples with caps (a,b,c) satisfying

    R(z)=A(z)+B(z)exp(z)+C(z)F(z)=O(z^M),
    B(1)=C(1).

There are N=M+3 coefficients and M+1 linear constraints, hence dim V>=2. Define the rational endpoint map

    E: V -> Q^2,  E(A,B,C)=(A(1),B(1)).

Every triple in ker E has A(1)=B(1)=C(1)=0. Thus there are unique polynomials A',B',C' with

    (A,B,C)=(z-1)(A',B',C'),

and degree caps (a-1,b-1,c-1). Multiplication by z-1 is a unit in Q[[z]], so R has order at least M exactly when A'+B'exp(z)+C'F(z) does. Endpoint matching imposes no further condition on the primed triple.

Let J be the M by M Taylor matrix whose rows are coefficient indices 0,...,M-1 and whose columns are the functions

    z^j,             0<=j<a;
    z^j exp(z),      0<=j<b;
    z^j F(z),        0<=j<c.

Componentwise division gives an exact vector-space isomorphism ker E = ker J. In particular, if det J!=0, then E is injective. Since dim V>=2 and its codomain has dimension two, dim V=2 and E is an isomorphism onto Q^2.

This is a sufficient normality criterion. If J is singular, this argument alone does not determine the endpoint image rank: the original solution space can also have larger dimension.

For the balanced case a=c=n, M=2n+b. The previous one-dimensional construction imposed contact 2n+b+1. This note removes its last Taylor condition while keeping endpoint matching. For the separate asymmetric branch, take a=2n, c=n and b=max(1,floor(log n)).

## 2. Integer kernel and exact endpoint index

Clear each of the M Taylor rows by a positive integer D_i sufficient to make that row integral. Append the integer matching row C(1)-B(1). This gives an integer matrix T of size (N-2) by N. No minimality of the D_i is assumed.

Let E also denote the integer two-row endpoint matrix on coefficient vectors, taking A(1) and B(1). Assume T has full row rank r=N-2 and that E has rank two on ker_Q T. Define

    L=ker_Q(T) intersect Z^N.

This is a saturated rank-two lattice. Choose an integer basis K, an N by 2 matrix, for L. The endpoint lattice is Lambda=E L, with finite index

    I=[Z^2:Lambda]=abs(det(EK)).

Let Delta_r(T)>0 be the gcd of the r by r minors of T. Then

    I=abs(det([T;E]))/Delta_r(T).                 (1)

Proof. Saturation means that the columns of K extend to a unimodular basis [U K] of Z^N. One way to see this is that Z^N/L is isomorphic to the image of T, a free abelian group; a basis of that image can be lifted and joined to a basis of L. Multiplying T by this unimodular matrix gives [TU 0], where TU is a nonsingular r by r integer matrix. Unimodular column operations preserve the ideal of maximal minors, so abs(det(TU))=Delta_r(T). Moreover,

    [T;E][U K] = [TU  0; EU  EK].

Taking absolute determinants proves (1). It also proves that the ratio is an integer. This is an exact index identity, not an estimate for an individual reduced denominator.

## 3. The augmented determinant is the normality determinant

Use coordinates A',B',C',X,Y,Z defined by

    A=(z-1)A'+X,
    B=(z-1)B'+Y,
    C=(z-1)C'+Y+Z.

This is a unimodular change of integer coefficient coordinates: division of an integer polynomial by z-1 leaves its integer value at one as the remainder, and the replacement of the three remainders by X,Y,Z is unimodular. In these coordinates, the matching row is Z and the endpoint rows are X,Y.

The Taylor block on the primed variables equals J followed on the left by the matrix for multiplication by z-1 on the first M Taylor coefficients. That lower triangular matrix has diagonal entries -1 and determinant (-1)^M. Therefore expansion along the three endpoint-coordinate rows gives

    abs(det([T;E]))=(product_i D_i)*abs(det J).   (2)

Column and row order choices affect only the discarded sign. The row clearers affect both the augmented determinant and Delta_r(T) by the same product. Consequently (1) is invariant under their enlargement.

Equations (1)-(2) identify the exact arithmetic object needing study:

    I=(product_i D_i)*abs(det J)/Delta_r(T).

They do not prove useful asymptotics for I. Establishing det J!=0 supplies the rank assumptions needed above, but not a small basis of Lambda.

## 4. Primitive endpoint reduction

For a nonzero lattice vector (X,Y), put g=gcd(abs(X),abs(Y)) and define

    P=X/g,  Q=Y/g,
    L_primitive=P+Q(e+pi)=R(1)/g.

This divides by the final endpoint gcd, not merely the polynomial coefficient content. When Y!=0, the actual positive reduced denominator is abs(Y)/g.

For a basis K of the saturated coefficient kernel, let the two endpoint columns have gcds g_1,g_2. Their primitive determinant has absolute value

    I/(g_1*g_2),

a positive integer. For a different independent integer pair K C, with nonsingular integer 2 by 2 matrix C, the numerator becomes I*abs(det C), followed by division by that pair's two endpoint gcds.

These identities preserve the distinction between lattice index, basis choice, and primitive denominator. Index alone does not bound the sizes or conditioning of two useful endpoint vectors. A rank-two image permits arbitrary rational endpoint data, so rank alone also gives no approximation estimate.

## 5. Paired-form irrationality criterion

Let S be a real number. Suppose that, for each j in an unbounded sequence, two integer pairs (P_(j,1),Q_(j,1)) and (P_(j,2),Q_(j,2)) satisfy

    P_(j,1)Q_(j,2)-P_(j,2)Q_(j,1)!=0,

and

    max_i abs(P_(j,i)+Q_(j,i)S) -> 0.           (3)

Then S is irrational.

Proof. If S=u/v with integers u,v and v>0, each v(P+QS) is an integer. Condition (3) makes both of these integers zero for all sufficiently large j. Both independent pairs would then be annihilated by the nonzero vector (v,u), contradicting their nonzero determinant.

No separate nonvanishing theorem for either individual full remainder is required. Exact pairwise independence ensures that under a rationality assumption at least one form in every pair is nonzero. Primitivity is not needed for this logical lemma, but using primitive pairs is essential for the best available smallness estimate.

For the relaxed Hermite–Pade construction, a sufficient analytic-arithmetic target is therefore an independent integer pair of triples at each selected index such that

    max_i abs(R_i(1))/g_i -> 0.                 (4)

All terms of R_i(1), including exponential and arctangent tails, remain in (4). If one endpoint coordinate Y is zero, its nonzero primitive form is +1 or -1, so a pair satisfying (4) automatically avoids that case eventually.

A useful consistency constraint is

    abs(P_1 Q_2-P_2 Q_1)
      <=abs(Q_2)*abs(L_1)+abs(Q_1)*abs(L_2).

It prevents interpreting a lattice-volume estimate alone as a small-form result. It does not rule out small independent forms with sufficiently large denominators.

## 6. New research obligations

Child 3 investigates the actual normality determinant. Child 4 develops the index/content formula into arithmetic information about useful primitive pairs. Child 2 seeks complete remainder estimates for those pairs with cancellation retained. Child 1 changes degree balance and parameter growth to test a separate analytic budget.

None of det J!=0, adequate endpoint gcds, useful basis conditioning, or (4) is proved here on an unbounded growing-degree set. The contribution is the exact change of proof obligations and the lattice formula tying them together. No inference about the rationality of e+pi is made before these remaining requirements are fulfilled.
