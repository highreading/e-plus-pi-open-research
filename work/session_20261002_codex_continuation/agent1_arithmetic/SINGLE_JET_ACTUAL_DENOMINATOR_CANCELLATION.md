> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A single Hurwitz jet cancels the complete odd Taylor denominator

Status: original author construction, 2026-10-02; not independently reviewed. This provides exact actual-denominator cancellation in an index-dependent polynomial pullback. It does not supply shrinking primitive forms or prove irrationality of e+pi.

Let P be a fixed real rational integral-Hurwitz polynomial, P(0)=0, P(1)=1, whose composition G=F∘P has the specified analytic branch G(1)=pi. Let H=e^z+G, and define its N-th Taylor endpoint

    c_N=sum_{j=0}^N H^(j)(0)/j!,  Z_N=N!c_N∈Z.

At even N>=2, Z_N is odd because G has even derivative jets. Write

    f_N=v_2(N!), O_N=N!/2^f_N.

Thus O_N is odd. Choose the unique centered representative

    K_N ≡ -2^(-1)Z_N (mod O_N),
    |K_N| <= (O_N-1)/2.                           (1)

When O_N=1 take K_N=0. No computation of e or pi is needed for this exact integer operation.

## 1. Exact endpoint denominator after composition and final gcd

Define the endpoint-preserving polynomial

    P_N(z)=P(z)+(K_N/N!) z^N(1-z).                 (2)

Its two new derivative jets are K_N at order N and -(N+1)K_N at order N+1; all are integers. Its values at0 and1 remain0 and1. Since F'(0)=2,

    F(P_N(z))-F(P(z)) = (2K_N/N!)z^N+O(z^(N+1)).

Consequently the complete N-th Taylor sum of e^z+F∘P_N is exactly

    c_N^new = c_N+2K_N/N!
            = L_N/2^f_N,
    L_N=(Z_N+2K_N)/O_N ∈ 2Z+1.                  (3)

The numerator is odd, so the final evaluated gcd leaves the exact denominator

    den(c_N^new)=2^f_N.                            (4)

Every odd prime-power factor of N! has been cancelled in the complete e+G sum. This does not confuse a coefficient clearer with q or omit the changed logarithmic coefficient. It attains the smallest possible denominator allowed by the even-N parity law among this one-jet class.

The monomial-coefficient support of (2) grows with N. Thus the fixed-support factorial-core theorem does not apply to this construction. Different P_N have incompatible N-th shared jets, so the shared-prefix spacing theorem does not identify their endpoint differences with one common Taylor block.

## 2. The exact analytic cost has threshold radius2

Set alpha_N=|K_N|/O_N, so 0<=alpha_N<1/2. On the closed disk |z|<=r, the perturbation norm is exactly

    ||P_N-P||_r
      =(1+r)|K_N|r^N/N!
      =(1+r)alpha_N 2^s_2(N)(r/2)^N.              (5)

The maximum is attained at z=-r. Since 2^s_2(N)<=2N,

    ||P_N-P||_r <= (1+r)N(r/2)^N.                 (6)

For every fixed r<2 this tends to zero. If P avoids both punctures1±i on a larger closed disk, its positive minimum puncture distance and (6) imply that P_N also avoids them on |z|<=r for every sufficiently large even N. Therefore the varying polynomials retain analyticity of F∘P_N on every fixed disk r<min(2,R_base). Their endpoint branch remains pi. This proves a genuine analytic/arithmetic construction; a bounded receipt is unnecessary for the infinite assertion.

If r>2, the general centered-residue bound gives no small perturbation. Within this particular construction, uniform convergence to P on |z|<=r is equivalent to

    alpha_N 2^s_2(N)(r/2)^N -> 0.                 (7)

Thus radius2 is the exact threshold of the worst-case congruence cost, not a universal bound for all denominator-cancellation constructions. A specially small alpha_N may permit r>2.

## 3. What a small congruence residue actually asks about the target value

The integer L_N in (3) is the nearest odd integer to2^f_N c_N; uniqueness follows because Z_N/O_N is an odd-over-odd fraction and cannot lie at an even integer midpoint. Equivalently,

    alpha_N=dist(2^(f_N-1)c_N, Z+1/2).             (8)

Suppose the fixed base H is analytic on a disk of radius R_base>2 and H(1)=S=e+pi. For 2<r<R_base, Cauchy's tail bound implies

    2^f_N |S-c_N|=O_r((2/r)^N) -> 0.              (9)

Distance to the half-integer lattice is Lipschitz, so alpha_N differs from

    dist(2^(f_N-1)S, Z+1/2)

by a quantity tending to zero. More precisely the actual primitive error satisfies

    ||2^f_N S-L_N|-2alpha_N|
       <=2^f_N|S-c_N|=O_r((2/r)^N).               (10)

Hence the exact dyadic cancellation construction gives shrinking primitive forms along a sequence of even N if and only if alpha_N tends to zero along that sequence. In this R_base>2 domain that condition is precisely a restricted dyadic approximation condition on S, up to the displayed vanishing error. It is not implied by analytic radius or Hurwitz jets, or by irrationality of e and pi separately. No assertion that those residues become small is made.

For preserving a specified disk r>2 by small perturbation, (7) demands an exponential version of this condition, with the binary digit-sum factor retained. Proving it would itself produce nonzero shrinking forms: L_N is odd while 2^f_N has unbounded exponent, so under any rationality hypothesis on S the forms in (10) are eventually nonzero. The unresolved residue condition is therefore a substantive Diophantine input, not a harmless normalization choice.

## 4. General endpoint denominator control inside this one-jet family

For any odd divisor D of O_N, choose instead

    K ≡ -2^(-1)Z_N (mod D).

Then D divides the complete integer numerator Z_N+2K. The final denominator divides N!/D and still has the full dyadic part2^f_N. Centering modulo D costs at most D/(2N!) in the perturbation coefficient. Partial odd cancellation can therefore be budgeted by the same exact congruence and disk norm. The remaining odd denominator is decided by gcd(Z_N+2K,O_N), not by D alone. Formula (4) is the full-cancellation case D=O_N.

This is an algebraic control parameter with an exact height/denominator tradeoff. It does not prove that a useful partial cancellation simultaneously meets an error bound, and it does not convert arbitrary Hermite–Padé coefficients into this family.

## 5. Gate and novelty boundary

Archive searches before the target used Taylor/congruence, endpoint-preserving perturbation, one/single jet, dyadic cancellation, K z^N, odd factorial pullback and denominator prescription terms over sources and the canonical work sessions. Prior notes contain sparse endpoint-preserving Hurwitz perturbations and several dyadic selector/correction laws, but no all-even-N full odd Taylor denominator cancellation theorem for F∘P. Read sources/nonpolynomial_integral_hurwitz_pullback.md's exact perturbation jets and the sparse multijet source's lattice search scope. The perturbation basis itself is old; applying its triangular F'(0)=2 response to the final complete endpoint congruence, with the exact support/radius cost, is the author derivation here.

Primary search queries: `"Hurwitz series" "interpolation" "integer" polynomial`; `"entire" "integer derivatives" "interpolation" polynomial denominators`; `"Hurwitz" "factorial" "congruence" power series composition`; `Waldschmidt Hurwitz functions integer derivatives survey 2002.01223`. Opened Michel Waldschmidt's [Integer-valued functions, Hurwitz functions and related topics: a survey](https://arxiv.org/html/2002.01223v1), and Hongquan Yu's primary [A generalization of Stirling numbers](https://www.fq.math.ca/Scanned/36-3/yu.pdf) for Hurwitz composition background. Their integer-jet closure is established background; neither is invoked to supply the specific endpoint congruence or a small-residue theorem. No broad finite search or claim of new general Hurwitz interpolation is made.

Bounded author evidence is saved in single_jet_cancellation_receipt.py and SINGLE_JET_CANCELLATION_RECEIPT.json. It applies the exact congruence at N80,120,180,240 to root's degree61 polynomial, regenerates the modified composition jets directly, and retains the complete endpoint gcd and exact perturbation norms at19/10 and21/10. These four modified polynomials have no new analytic-radius certificate; the norms are exact arithmetic, not a finite claim that the root's puncture margin survives.
