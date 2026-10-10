> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the dual-quadratic content theorem

Date: 2026-09-13. Reviewer: audit_sources.
Target: raw_dual_quadratic_content_factorization.md.
Result: **PASS. No mathematical correction required.**

This review checks the complete argument, including arbitrary prime-power depths and the ramified dyadic extension. The finite controls below use only the already saved n=1,2 polynomials; they do not establish any all-index assertion. The proof does not settle the fixed endpoint cancellation gcd(Z,P(1)+4T(1)), and gives no proof about the rationality of e+pi.

## 1. Statements and normalization checked

The target uses the actual integral simultaneous triple (Q,P,T), degree at most m=2n, D=1+z^2, and


$$
E=D(QT'-Q'T)-Q^2,\qquad \mathcal W=z^{6n}K,\quad \deg K\le2.
$$


The reviewed conclusions are


$$
c_K=c_Pc_E,\quad c_E\mid 2^{4n}c_Q^2,\quad
c_Q,c_P\mid R_n=(2n)!/n!,
$$


and consequently


$$
\gcd(|Z|,|P(1)|,|T(1)|)\mid c_K\mid 2^{4n}R_n^3.
$$


Here contents are the actual positive integer coefficient gcds, with no primitive rescaling of K. Removing the factor z^{6n} preserves content exactly. The endpoint divisor is the global integer divisibility already proved in raw_dual_quadratic_and_endpoint_separation.md; it does not require a large-prime cutoff.

## 2. The six-coefficient formula

I independently expanded the exact identity


$$
Q\mathcal W=D(FE'-F'E+FE)-D'FE,\quad F=QP'-Q'P-QP.
$$


If q_0=[z^m]Q is nonzero, division gives


$$
F/Q=-P+(p_0q_1/q_0-p_1)z^{m-2}+O(z^{m-3}).
$$


In the derivative part, the coefficient at z^{3m-1} vanishes, and that at z^{3m-2} is


$$
p_0e_1-p_1e_0-(q_1/q_0)p_0e_0.
$$


Combining all terms cancels the q_1/q_0 contribution and yields exactly


$$
K_2=-p_0e_0,\quad K_1=(2p_0-p_1)e_0-p_0e_1,
$$




$$
K_0=-(p_0+p_2)e_0+(3p_0-p_1)e_1-p_0e_2.
$$


The direct expressions for e_0,e_1,e_2 in the source have the correct signs, including the s_0 contribution from the constant term of D.

The extension to q_0=0 is legitimate: these are polynomial identities with integer coefficients in the original input coefficients, proved on a Zariski-dense characteristic-zero set. It is not a genericity assumption about the actual triple. The resulting integer identities also specialize in finite characteristic.

## 3. Exact Gauss content

Differentiation is nondecreasing for the Gauss valuation on Q_p(z), including p=2. After scaling rational inputs to Gauss valuation zero, their nonzero reductions are rational functions over F_p. Neither


$$
f'=f,\qquad (g/f)'/(g/f)=-1
$$


can hold for a nonzero rational function: its logarithmic derivative is O(1/z) at infinity in every characteristic. Hence


$$
v_G(f'-f)=v_G(f),\quad
v_G(fg'-f'g+fg)=v_G(f)+v_G(g).
$$


The reduction commutes with differentiation because a primitive rational denominator remains a nonzero rational denominator after reduction.

Applying these to


$$
L=(P/Q)'-P/Q,\quad H=(T/Q)'-1/D
$$


gives v_G(L)=v_G(P)-v_G(Q) and v_G(H)=v_G(E)-2v_G(Q). The identity


$$
\mathcal W=D^2Q^3(LH'-L'H+LH)
$$


then gives v_G(\mathcal W)=v_G(P)+v_G(E) exactly, for each prime separately. H is nonzero in characteristic zero by its impossible rational-derivative residue condition. Thus c_K=c_Pc_E has no hidden cancellation exception.

The elementary lower divisor c_P c_Q gcd(c_Q,c_T) also follows termwise from E. It is not used to substitute a primitive content for the actual one.

## 4. The saturated residue lemma

This is the delicate new step, and it is valid.

For a finite extension of Q_p with valuation ring O and uniformizer pi, the ring


$$
\mathcal A=\varprojlim_h(O/\pi^h)((u))
$$


can be realized as series with coefficients in O whose negative-index coefficients tend pi-adically to zero. At each quotient there are only finitely many negative exponents. Multiplication is well defined by this property; differentiation is coefficientwise and preserves it. The ring is pi-torsion free.

An integral translation of the variable preserves the Gauss valuation. A primitive denominator B at the chosen lifted residue point reduces to u^s c(u), c(0) nonzero. Choose a lift C with C(0) a unit and write B=u^s C+pi E. The displayed finite geometric inverse modulo pi^h gives a compatible inverse in \mathcal A. It reduces to the ordinary Laurent expansion of the reduced rational function. Differentiation of the inverse agrees with the rational derivative, by the inverse identity.

Every rational function becomes Gauss-integral after multiplication by a fixed constant power of pi, so it embeds in \mathcal A[1/pi]. The coefficient at u^-1 of its derivative is exactly zero: coefficientwise it would be 0 times the coefficient at u^0. This remains true after inverting pi. If the derivative itself is Gauss-integral, it lies in \mathcal A, and its reduction agrees with the usual Laurent expansion of its rational reduction. That proves the zero residue.

This argument correctly avoids the false assertion that the reduction of the derivative must be an exact rational derivative. For example z^p/p differentiates to z^(p-1), illustrating why one cannot simply reduce the primitive. The completed Laurent construction permits such a nonintegral primitive without sacrificing the residue conclusion.

At odd p, if v_G(H)>0, the integral derivative (T/Q)' reduces to 1/D. Over an unramified extension containing i, the simple-pole residue 1/(2i) is a unit. This contradicts the lemma, so v_G(H)<=0. If T/Q is itself integral, the reverse inequality is immediate, giving equality in that special case.

## 5. Dyadic separation

In Q_2(i), with v(2)=1, substitute z=i+2iu. Then


$$
D(z)=-4u(u+1),\quad
4H_*=[(2/i)b_*]'+1/[u(u+1)],\quad b=T/Q.
$$


Both the coefficient 2/i and the plus sign are correct by the chain rule. The poles 0 and -1 remain distinct in the residue field. If v_G(4H_*)>0, the rational derivative would reduce to the negative of 1/[u(u+1)], which has a nonzero simple-pole residue. The saturated residue lemma therefore proves v_G(H_*)<=-2. It imposes no integrality assumption on b_*.

Writing a=v_2(c_Q), Q_0=2^-a Q, and


$$
\sigma=v_G(Q_0(i+2iu)),
$$


integral translation by i is norm preserving in both directions. After translation there is a unit coefficient of degree at most m; scaling u by 2i multiplies its coefficient valuation by adding that degree. Thus 0<=sigma<=m, including the possibility of half-integral intermediate valuations in the ramified extension.

The numerator E_0=2^-2a E has valuation v_G(H). Substitution cannot lower its valuation. The substituted denominator has valuation 2+2sigma, so


$$
v_G(H_*)\ge v_G(H)-2-2\sigma.
$$


Together these prove v_G(H)<=2sigma<=2m and hence


$$
v_2(c_E)\le2v_2(c_Q)+2m.
$$


The direction of each inequality is correct. No unproved assertion about separated roots of Q, or its degree being exactly m, is used.

## 6. Both factorial-transform content divisors

Write the actual primitive polynomial


$$
W(t)=t^n(t-1)^nV(t),\quad V\in\mathbb Z[t],\quad c_V=1.
$$


The map from the n+1 coefficients of V to w_n,...,w_(2n) is an integer triangular matrix with diagonal (-1)^n. Its inverse is also integral. Those first coefficients therefore have gcd one.

For each n<=k<=2n, k!/n! divides R_n. If c_Q divides every (k!/n!)w_k, it also divides every R_n w_k. An integer Bezout combination of the first n+1 w_k then proves c_Q|R_n. This is an integer divisibility argument, not a bound obtained by dividing unspecified small-prime units.

Similarly,


$$
W(1+t)=t^n(1+t)^nV(1+t)=\sum a_kt^k
$$


and exact reversal of the finite exponential Taylor convolution gives


$$
P(z)=\sum_{k=n}^{3n}(k!/n!)a_kz^{3n-k}.
$$


Translation by 1 preserves primitive integer content. The triangular factor (1+t)^n proves gcd(a_n,...,a_(2n))=1, and the same Bezout argument proves c_P|R_n. No value V(1) is assumed nonzero.

Stirling's formula gives log R_n=n log n+O(n), so the displayed global integer carrier has logarithm 3n log n+O(n), as claimed.

## 7. Exact frozen controls

The independent checker raw_dual_quadratic_content_independent_checks.py and its JSON use only the previously saved n=1,2 triples. They verify the full rational identity, all six top coefficients, both factorial-content divisors, the exact content equality, and the endpoint divisor.

They give:

| n | c_Q | c_P | c_E=c_K | sigma |
|---|---:|---:|---:|---:|
| 1 | 2 | 1 | 4 | 0 |
| 2 | 4 | 1 | 64 | 1 |

The dyadic upper bound is attained in these two controls. This is a normalization check only; no assertion of equality at other degrees follows.

## 8. Scope retained

The theorem controls the common divisor of Q(1),P(1),T(1), and the actual coefficient content of K. It does not control


$$
G_4=\gcd(Z,P(1)+4T(1)).
$$


In particular, G_4 can have a prime factor while T(1) is a unit, so replacing G_4 by the simultaneous endpoint content would be invalid. The proof correctly preserves this main arithmetic obstruction and makes no irrationality claim.

