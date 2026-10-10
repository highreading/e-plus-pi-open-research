> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Diagonal local review and pairing research, stage 8

Status: limited independent review of Main's new Stage 10 implications; separate original differential moment and endpoint identities. No infinite-range modular nonvanishing theorem is established. S denotes the actual e+pi.

## Scope and source

Primary source read in full in the supplied controller receipt: work/parallel_batch_01/main/DIAGONAL_LOCAL_CONTENT_REDUCTION_STAGE10.md (9874 bytes). Historical complete moment and insertion identities are inherited inputs. Earlier endpoint research and Stage 9 are not reviewed again. No computation or numerical evidence is claimed in this stage.

Throughout k>=2, h=y+1, and p>6k is prime. Use exactly Main's matrices M,G,J,B,D,C=M-J. In particular B is the complete low rational block, not a polynomial-integral replacement valid only at high degree.

## Limited review

Block normalization: VALID. Changing each row polynomial from y^i to h^i and the full column list from y^j to h^j uses monic triangular matrices of determinant one. The high columns have factors h^k, so their full period jets vanish. The resulting pencil is exactly [C,G;B+TJ,D]. Its leading coefficient is (-1)^k det J det G: swapping the two k-row blocks contributes (-1)^(k^2)=(-1)^k. The anti-diagonal of J is the normalized Taylor weight (k-1)!/(1/2)_(k-1), with no omitted derivative factorial. The displayed leading coefficient agrees with that normalization.

Large-prime hypotheses: VALID. The specified complete clearer has prime support at most 6k, and det J is a p-adic unit for p>6k. All entries are p-integral. Thus the full physical clearer has valuation zero and v_p(A)=v_p(det G)-v_p(g). This is a statement at the indicated primes, not at small primes or for an unspecified enlarged clearer containing p.

Symmetric congruence: VALID. Over the residue field the radical has an arbitrary vector-space complement on which the symmetric form is nondegenerate. Lift a basis, then eliminate the cross block using the inverse of its unit leading block. This gives W^T G W=diag(G0,E), with E entrywise divisible by p. Nonsingularity over Q_p follows from det G nonzero. The proof covers full nullity r=k by empty-block conventions. The minimum entry valuation of E equals its first determinantal-divisor valuation, hence the smallest nonunit Smith depth; v_p(det E)=v_p(det G) because det W and det G0 are units. No nonunit pivot is canceled.

Reversed-polynomial signs: VALID. Multiplying the lower rows by z and swapping row blocks yields (-1)^k det(J+zB) det(G-z C(J+zB)^(-1)D). Applying the congruence W contributes (det W)^(-2). The second Schur complement has E-zK11-z^2 K10(G0-zK00)^(-1)K01, hence precisely E-zQ with Main's plus sign in Q. No symmetry of C(J+zB)^(-1)D is needed.

Formal inverses and units: VALID. Both J+zB and G0-zK00 have invertible constant matrices over Z_p. Their inverse series are p-integral and their determinant factors are units in Z_p[[z]]. The full-nullity convention gives Q=K and the empty determinant one.

Finite cutoff: VALID. Multiplication by the unit u(z) induces an invertible lower triangular map on coefficients through degree k. It preserves their generated ideal. Since chi is a polynomial of degree at most k, these coefficients give the complete physical coefficient ideal, even though det(E-zQ) can be an infinite series. Coefficients after degree k need not vanish, but cannot lower the content because det(E-zQ)=u^(-1)chi has p-integral series multiplier. The cutoff is therefore justified.

Smallest-pivot congruence: VALID. Every determinant term not entirely from -zQ contains an entry of E and is divisible by p^alpha. Thus coefficients below r vanish modulo p^alpha, and those from r through k agree, up to the common sign (-1)^r, with coefficients zero through k-r of det Q. Taking capped valuations proves the displayed formula. In nullity one E is scalar and alpha=a, so the cap gives the exact content valuation since d<=a. This does not assert that only the constant coefficient of Q matters.

First survival coefficient: VALID. If det Q(0) is a unit, the coefficient of z^r in chi equals (-1)^(k+r)(det W)^(-2) det J det G0 det Q(0) modulo p. Thus beta_(k-r) is a p-adic unit. If it vanishes, later coefficients can still survive. Kernel-basis congruence preserves nonsingularity modulo p; this does not require a globally integral unimodular W.

Physical gcd interpretation: VALID. At the specified primes delta is a unit, so the local coefficient ideal is that of the actual integers I_j. The least clearer of beta/beta_k is the positive primitive leading coefficient A, by Bezout for the complete primitive vector. The conditional prime sum is a lower bound on log A and says nothing about the weight of primes failing the survival condition. No replacement of the full gcd by a block content occurs.

Endpoint formula (12): its new implication is VALID under the inherited moment definitions. On h^(k+i+j), the period vanishes and the normalized rational kernel becomes (1+x^2)^(i+j). The exponential rational remainder is minus the binomial factorial sum. Both contributions are retained. This formula does not extend unchanged to the low block B.

No correction to the assigned Stage 10 conclusions is required.

## Original research: an actual differential moment identity

Define the differential operator

 L P=4y P''+2P'-P.

Let F be the factorial functional F(y^n)=(2n)!, and retain mu(y^n)=D_(2n). Then, for every polynomial P over Q,

 mu(LP)=2P'(1)-P(1),                                      (A)
 F(LP)=-P(0).                                             (B)

Proof. The derangement recurrence gives

 D_(2n)=2n(2n-1)D_(2n-2)-(2n-1), n>=1.

For P=y^n, LP=2n(2n-1)y^(n-1)-y^n, so (A) follows for n>=1. For P=1 both sides are -1. The factorial recurrence gives zero in (B) for n>=1, while P=1 gives -1. Linearity proves both statements.

These are identities of the actual moments, not assumptions about a positive modular form. They hold integrally for integral P and therefore modulo p as well. In h-coordinates L=4(h-1)d^2/dh^2+2d/dh-1; the endpoint y=1 is h=2 and y=0 is h=1. Confusing these endpoints with h=0 would give a different identity.

Let rho=mu-nu_k. If P is divisible by h^(k+2), then LP is divisible by h^k and its entire order-(k-1) jet vanishes. Consequently

 rho(LP)=mu(LP)=2P'(1)-P(1).                              (C)

The stronger divisibility h^(k+2), rather than h^k, is needed because the second derivative can lower the h-adic order by two.

## Original research: rational endpoint identity with all terms

Let R_k be the complete rational functional used in B and D, and c=c_k. If P is divisible by h^(k+2), then

 R_k(LP)=P(0)+c 2^(-k)[2P'(1)+kP(1)]
   +c integral_0^1 P(x^2)[-h_x^(-k)-2k h_x^(-k-1)
                              +4k(k+1)x^2 h_x^(-k-2)] dx,             (D)

where h_x=1+x^2.

Every integrand in (D) is a polynomial because of the stipulated divisibility. Thus its integral is rational, with no concealed period term.

Proof. Since LP is divisible by h^k, the inherited complete rational moment formula gives

 R_k(LP)=-F(LP)+c integral_0^1 (LP)(x^2)h_x^(-k) dx.

For u(x)=P(x^2), one has (LP)(x^2)=u''(x)-u(x). Twice integrating by parts with w(x)=h_x^(-k) yields

 integral (u''-u)w=[u'w-u w']_0^1+integral u(w''-w).

At zero both u' and w' vanish. At one, u'=2P'(1), w=2^(-k), and w'=-k2^(-k), giving the displayed boundary expression. Finally

 w''=-2k h_x^(-k-1)+4k(k+1)x^2 h_x^(-k-2),

and (B) supplies P(0). This proves (D).

For integral P of degree at most 3k-1 satisfying the divisibility premise, all denominators in (D) are p-units when p>6k. Indeed the polynomial integrands have y-degree at most deg P-k<=2k-1, so their integrations introduce odd denominators at most 4k-1. The factors in c and powers of two also have prime support below p. Thus this bounded-degree endpoint identity can legitimately be reduced modulo p. For k=2 the divisibility and degree range may be vacuous; the identity itself remains valid in its general rational form.

## Application attempt to the nullity-one pairing

Assume det G is divisible by p and G modulo p has nullity exactly one. Write W=[U,zeta], where U has k-1 columns, and

 W^T G W=diag(G0,epsilon), v_p(epsilon)=a>=1.

The vector zeta modulo p spans the radical. Its polynomial is

 zeta(h)=sum_(j=0)^(k-1) zeta_j h^j,

and its actual moment equations are

 mu(h^(k+i) zeta(h))=0 mod p, 0<=i<k.                     (E)

Set H=C J^(-1)D, where this H is a matrix and not the polynomial variable h. Then the scalar constant pairing is

 q0=zeta^T H zeta=zeta^T C J^(-1)D zeta.                   (F)

The next coefficient, obtained by retaining B in the inverse expansion, is exactly

 q1=-zeta^T C J^(-1)B J^(-1)D zeta
       +zeta^T H U G0^(-1)U^T H zeta.                    (G)

This formula is stated to expose the remaining actual obstruction, not as a new generic Schur theorem. All its inverses are p-integral unit inverses. The nonunit epsilon is still present in the scalar determinant epsilon-zQ(z).

Equations (A)-(D) give additional actual endpoint information, but do not prove (F) nonzero modulo p. The null equations (E) apply only to a particular k-dimensional set of tests. Applying L to a product with zeta creates both zeta' and zeta'' and changes the multiplier's degree and h-adic order. These extra terms are not among (E) without further relations. In particular one cannot apply the null equations to LP merely because P has high h-adic order: the resulting quotient must still lie in the appropriate span of zeta times the allowed tests. No such closure has been proved.

Likewise, (D) is a high-divisibility identity. It does not evaluate the low block B appearing in (G), and substituting its high-block expression into B would delete the low rational endpoint terms. The unit operator J^(-1) connects these low coordinates with D zeta; nothing in (A)-(E) makes that connection nondegenerate modulo p.

Therefore no actual relation forcing q0 to vanish identically is established either. The present argument proves neither universal survival nor universal vanishing. If q0=0 modulo p, it also does not prove q1 nonzero: the two explicitly displayed terms in (G) could cancel. Positivity of G over the reals does not exclude any of these modular cancellations.

## Exact remaining content obstruction and stopping point

For this nullity-one case, retain the full scalar series Q(z)=sum q_j z^j and epsilon of valuation a. Main's reviewed formula gives

 v_p(g)=min(a,v_p(q0),...,v_p(q_(k-1))),
 v_p(A)=a-v_p(g).

Thus q0 a unit implies v_p(g)=0; if q0 vanishes modulo p but q1 is a unit, the same conclusion follows through the next coefficient. If both vanish modulo p, later coefficients must still be checked. Neither vanishing proves positive complete content by itself.

The unresolved actual arithmetic assertion is: on an explicitly justified infinite family of pairs (k,p) with p>6k, p dividing F*_k and nullity one, prove nonvanishing of (F), or, conditional on its vanishing, prove nonvanishing of (G) or a later coefficient. No such infinite family with a survival theorem is obtained here. No existence claim for infinitely many eligible primes is implicit.

The original stage contribution is the exact actual differential identities (A)-(D), including their endpoints, degree restrictions, and modular validity. They do not close the pairing obstruction. Since further progress along this calculation would only restate the generic Schur criterion without an additional actual moment relation, this bounded branch stops here as requested.

The complete low block B, the nonunit epsilon, the unit congruence factor, the physical clearer, and the final gcd all remain accounted for. No degree or prime atlas, factorization scan, network access, or code execution was performed. The irrationality question remains open.
