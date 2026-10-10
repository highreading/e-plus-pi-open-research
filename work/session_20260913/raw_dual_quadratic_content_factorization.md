> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact dual-quadratic content and an explicit factorial divisor

Date: 2026-09-13. Original bounded continuation by audit_results.
Independent review: PASS by audit_sources; see raw_dual_quadratic_content_independent_review.md.

The previously reviewed note raw_dual_quadratic_and_endpoint_separation.md constructs an integral quadratic K from the actual simultaneous triple Q=Qhat, P=Pe, T=Pa. This note gives its three coefficients, an exact content factorization, and an explicit full-depth divisor for its content. The new divisor improves the earlier statement that its prime factors are at most 2n; it does not bound cancellation at the fixed combination P(1)+4T(1).

All polynomial contents below are positive gcds of their coefficients. Put

    m=2n, D=1+z^2,
    E=D(QT'-Q'T)-Q^2,
    R_n=(2n)!/n!.

The principal results are

    content(K)=content(P) content(E),                         (1)

    content(E) | 2^(4n) content(Q)^2,                       (2)

    content(Q)|R_n,  content(P)|R_n,
    content(K) | 2^(4n) R_n^3.                              (3)

Consequently the actual simultaneous endpoint content satisfies the full integer divisibility

    gcd(|Z|,|P(1)|,|T(1)|) | 2^(4n) R_n^3.                 (4)

These are statements with all prime-power exponents retained, not only radical or prime-support bounds. In particular the logarithm of the explicit carrier in (4) is 3n log n+O(n).

The inspected predecessors were the dual quadratic theorem and its independent review, the actual integral dual numerator theorem, the extremal dual polynomial/content identity, and the endpoint scalar Cauchy restriction. The earlier cubic content results concern a different, selected type-I triple. No earlier note supplies (1), the residue-saturation lemma below, or (2). No new canonical degree or prime scan was used.

## 1. Six top coefficients determine the quadratic

For arbitrary integral Q,P,T of degrees at most m, put E as above. The cancellation in QT'-Q'T gives degree E<=2m. Write

    p_j=[z^(m-j)]P,       e_j=[z^(2m-j)]E,       j=0,1,2.

For the actual family, Wcal=z^(3m)K and the three coefficients are exactly

    [z^2]K = -p_0 e_0,
    [z]K   = (2p_0-p_1)e_0-p_0e_1,
    [1]K   = -(p_0+p_2)e_0+(3p_0-p_1)e_1-p_0e_2.           (5)

These are valid even when one or more of the designated top coefficients vanish.

Here is a derivation which also fixes all signs. Define

    F=QP'-Q'P-QP.

The rational Wronskian identity from the earlier note gives the exact polynomial identity

    Q Wcal = D(FE'-F'E+FE)-D'FE.                            (6)

First suppose the coefficient q_0=[z^m]Q is nonzero, and write q_1=[z^(m-1)]Q. Set r=F/Q. Laurent expansion at infinity gives

    r=-P+(p_0q_1/q_0-p_1)z^(m-2)+O(z^(m-3)).

After division of (6) by Q,

    Wcal=D{rE+rE'-r'E-(Q'/Q)rE}-D'rE.

The order z^(3m-1) terms in the derivative brace cancel. Its coefficient at z^(3m-2) is

    p_0e_1-p_1e_0-(q_1/q_0)p_0e_0.

Combining this with D rE and -D'rE cancels q_1/q_0 and yields (5) as the coefficients at z^(3m+2),z^(3m+1),z^(3m). Both sides of those coefficient identities are polynomials with integer coefficients in the original input coefficients. Their validity on the dense set q_0!=0 therefore proves them identically, including q_0=0. This use of density concerns only polynomial identities in characteristic zero; the resulting integer identities are valid in every characteristic.

If direct original coefficients are preferable, write q_j=[z^(m-j)]Q and t_j=[z^(m-j)]T, with negative-index powers interpreted as zero. Then

    s_0=q_1t_0-q_0t_1,
    s_1=2(q_2t_0-q_0t_2),
    s_2=3q_3t_0+q_2t_1-q_1t_2-3q_0t_3,

    e_0=s_0-q_0^2,
    e_1=s_1-2q_0q_1,
    e_2=s_2+s_0-q_1^2-2q_0q_2.                             (7)

No origin error coefficient or limiting operation is needed for these exact formulas.

## 2. Two Gauss-valuation identities

Fix a prime p. The Gauss valuation v_G on Q_p(z) is the minimum coefficient valuation for a polynomial and the difference of those valuations for a rational quotient. The derivative satisfies v_G(f')>=v_G(f).

For every nonzero rational f,g,

    v_G(f'-f)=v_G(f),
    v_G(fg'-f'g+fg)=v_G(f)+v_G(g).                          (8)

To prove either identity, scale each input to Gauss valuation zero and reduce modulo p. The rational reductions are nonzero. The equation f'=f would force the logarithmic derivative of a nonzero rational function to equal 1; that derivative is O(1/z) at infinity in every characteristic. Likewise fg'-f'g+fg=0 would force the logarithmic derivative of g/f to equal -1. Both are impossible. Thus the normalized reductions are nonzero. This proof also works at p=2; it does not use the simple poles of 1/D.

For Q,P nonzero, let

    a=P/Q, L=a'-a,
    H=(T/Q)'-1/D=E/(DQ^2).

In characteristic zero H is nonzero, since a rational derivative cannot have the nonzero simple-pole residues of 1/D. The earlier identity is

    Wcal=D^2 Q^3(LH'-L'H+LH).

Writing a_p=v_p(content Q), b_p=v_p(content P), and e_p=v_p(content E), equation (8) gives

    v_G(L)=b_p-a_p,  v_G(H)=e_p-2a_p,
    v_p(content Wcal)=b_p+e_p.                             (9)

This proves (1) at every prime because removing z^(6n) does not change content. More generally content(Wcal)=content(P)content(E) for any nonzero integral Q,P and arbitrary integral T.

The elementary lower divisor

    content(P) content(Q) gcd(content(Q),content(T))
       | content(K)                                       (10)

also follows, since each term of E contains either one Q and one T or two Q factors. In (10), content(0)=0 may be used for the universal statement.

## 3. Residues of a Gauss-integral rational derivative

The following saturation fact is essential. It is weaker than asserting that reduction remains an exact rational derivative, which is false (for example d(z^p/p)=z^(p-1)dz).

**Lemma.** Let K be a finite extension of Q_p, with valuation ring O, uniformizer pi, and residue field k. If b in K(z) has Gauss-integral derivative b', then the reduction of b' has residue zero at every finite point over an algebraic closure of k.

It suffices to pass to a finite unramified extension containing the point and choose an integral lift alpha. Put u=z-alpha; integral translation preserves the Gauss valuation.

Consider the ring

    A = inverse_limit_h (O/pi^h O)((u)),

where at each h the Laurent series has only finitely many negative powers. Every Gauss-integral rational function embeds in A. Indeed a primitive polynomial denominator B has nonzero reduction u^s c(u), c(0)!=0. Write B=u^s C+pi E with C an integral power-series unit. Modulo pi^h its inverse is the finite geometric expansion of

    u^(-s) C^(-1) (1+pi E u^(-s)C^(-1))^(-1).

The expansions are compatible as h changes and reduce to the usual Laurent expansion of the reduced rational function. They commute with differentiation. Every rational b lies in A[1/pi] after multiplication by a constant power of pi. The coefficient of u^(-1) in its derivative is identically zero: the only possible source would be the derivative of its constant term. This assertion holds coefficientwise in every quotient and after inverting pi.

If b' is Gauss-integral, its image lies in A and its reduction is the Laurent expansion of the reduced rational function. The preceding zero coefficient therefore proves the lemma. No assertion about reducing a nonintegral primitive itself is made.

For odd p, apply this lemma after adjoining i, an unramified extension if necessary. If v_G(H)>0, then

    (T/Q)' = H+1/(1+z^2)

is Gauss-integral and reduces to 1/(1+z^2). That reduction has residue 1/(2i), a unit, at the simple root i. This contradicts the lemma. Consequently

    v_G(H)<=0,
    v_p(content E)<=2v_p(content Q)       (p odd).          (11)

If v_p(content T)>=v_p(content Q), then H is integral and the same argument gives v_G(H)=0. Thus in that case equality holds in the second inequality of (11).

## 4. The dyadic bound by separating the two roots

The odd-prime argument cannot be copied modulo two because the two roots of D merge. Instead extend to K=Q_2(i), keeping the valuation normalized by v(2)=1, and use

    z=i+2iu,   D(z)=-4u(u+1).

Let b=T/Q and put H_*(u)=H(i+2iu), b_*(u)=b(i+2iu). The chain rule gives

    4H_* = [(2/i)b_*]' + 1/[u(u+1)].                      (12)

The two poles of the last rational function are distinct modulo the maximal ideal of O_K, and its residue at zero is a unit. The residue-saturation lemma therefore gives

    v_G(H_*)<=-2.                                         (13)

This conclusion permits arbitrary constant denominators in b_*. It does not assert that b_* is integral.

Let a=v_2(content Q), Q_0=2^(-a)Q, and

    sigma=v_G(Q_0(i+2iu)).

Translation by i preserves the Gauss norm, and scaling the variable by 2i multiplies the coefficient of degree j by a number of valuation j. Since Q_0 has at least one unit coefficient after translation and degree at most m,

    0<=sigma<=m.                                          (14)

For H=E_0/(D Q_0^2), the numerator E_0=2^(-2a)E has Gauss valuation v_G(H). Translation by i and subsequent scaling by 2i cannot decrease that numerator valuation. Its denominator after substitution has valuation 2+2sigma. Hence

    v_G(H_*)>=v_G(H)-2-2sigma.

Combining with (13) proves the sharper actual bound

    v_G(H)<=2sigma,
    v_2(content E)<=2a+2sigma<=2a+2m.                      (15)

Together with (11), this proves the full integer divisor

    content(E) | 2^(2m) content(Q)^2.

For m=2n this is (2). The proof does not require squarefreeness or any bound on the heights or locations of Q's roots.

## 5. Both factorial-transform contents divide R_n

The primitive dual factorization is

    W(t)=t^n(t-1)^n V(t),  V in Z[t], content V=1,
    Q(z)=sum_(k=n)^(3n) (k!/n!)w_k z^(3n-k).

The first n+1 coefficients w_n,...,w_(2n) have gcd one: they are obtained from the n+1 coefficients of V by a lower triangular integer matrix with diagonal (-1)^n. For n<=k<=2n the multiplier k!/n! divides R_n. An integer Bezout combination of these w_k, multiplied by R_n, therefore shows that content(Q) divides R_n.

There is an equally direct formula for P. Write

    W(1+t)=sum_k a_k t^k=t^n(1+t)^n V(1+t).

Reversing the finite Taylor convolution defining P gives

    P(z)=sum_(k=n)^(3n) (k!/n!)a_k z^(3n-k).               (16)

Integer translation preserves the primitivity of V. The first n+1 coefficients a_n,...,a_(2n) again have gcd one, by the triangular factor (1+t)^n. The same Bezout argument gives content(P)|R_n.

For the coefficient formulas in Section 1 one may also use

    p_0=V(1),
    p_1=(n+1)[nV(1)+V'(1)],
    p_2=(n+1)(n+2)[binom(n,2)V(1)+nV'(1)+V''(1)/2].

All these quantities are integers; no endpoint nonvanishing is assumed.

Combining this paragraph with (1) and (2) proves (3). Combining (3) with the reviewed global divisor of the simultaneous endpoint gcd into content(K) proves (4).

## 6. What is exact, and what is still missing

Equation (1) is an exact content identity; (5) gives three explicit scalar coefficients realizing that gcd. Equation (9) is an exact prime-by-prime equality. Equations (11) and (15) supply valuation upper bounds, rather than formulas for the unknown error of the rational derivative at every small prime.

At an odd prime, the remaining scalar depth in content(K) is exactly

    v_G((T/Q)'-1/D),

which lies between min(v_p(content T)-v_p(content Q),0) and zero. At two, the upper bound is 2sigma rather than an asserted equality. Thus the explicit factorial carrier does not by itself determine v_p(content K), nor does it make the endpoint triple gcd equal to that content.

Most importantly, the actual endpoint gcd

    gcd(Z,P(1)+4T(1))

is a different quantity. It may be large when T(1) is a unit, and is not bounded by (4). The passed separation theorem remains necessary to describe that distinction. No estimate for the fixed unit ratio near -4 follows from the present carrier.

## 7. Frozen normalization controls

Only the previously saved n=1,2 simultaneous triples were inspected. They give

    n=1: (p_0,p_1,p_2)=(1,0,-6),
         (e_0,e_1,e_2)=(20,-48,0),
         content(Q)=2, content(P)=1, content(E)=4;

    n=2: (p_0,p_1,p_2)=(925,5652,12504),
         (e_0,e_1,e_2)=(7160384,-40248576,18834816),
         content(Q)=4, content(P)=1, content(E)=64.

Formula (5) reproduces the two already reviewed quadratics. At n=1 the dyadic sigma is zero, and at n=2 it is one; the upper bound (15) is attained in both controls. These finite facts check scales and signs only, not the all-index proof or a proposed equality at other degrees.
