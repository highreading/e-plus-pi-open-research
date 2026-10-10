> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact finite refutation of the proposed compact content envelope

The parent evaluated the complete compact pencil at k=32, using every moment
through index94 and every factorial through188!, retaining the arctangent
corrections and the last odd denominator187. This is a finite auxiliary compact
index, not an index of the separate original binary producer.

For each s=0,1,2, the parent formed the entire64-by64 integer matrix. It divided
each contact column by2 and cleared right column j with its own
Lambda_(32,j)=lcm(1,3,...,125+2j). Every division was checked to be integral.
The exact determinant scalar relative to the original polynomial is
2^32 E_32, where E_32=Lambda_32^32/product_j Lambda_(32,j).
Thus no column payment is omitted from the reconstructed original H.

Three fraction-free Bareiss calculations checked every one of the85344 exact
divisions per determinant. The certificate stores all pivots, row swaps,
matrix hashes and exact determinants. Independently implemented modular
elimination checked each determinant at three trial-division-verified primes.
The evaluations satisfy H(2)=2H(1)-H(0), as required by the rank-one pencil.
An extended Euclidean identity U H0+V H1=G, along with both coefficient
divisibilities, certifies the actual ALL-prime gcd without any factorization
assumption. The primitive pair has gcd1 and positive q.

Results:

- q_32 has6437 decimal digits; G_32 has2054 decimal digits.
- The independently evaluated D_31 E_32 divides G_32, agreeing with the new
  symbolic product-divisor claim at this one index.
- v2(G_32)=3375 and v2(D_31)=780.
- The proposed B_32=D_31 E_32 2^2048 Lambda_32^64 has v2(B_32)=2828.
- Exactly G_32/gcd(G_32,B_32)=2^547. Hence G_32 does NOT divide B_32.
- After trial division by EVERY prime<=187, the remaining factor of G_32 is1.
  At this index, the envelope fails solely through excess binary depth.

This disproves A3turn14's all-k>=32 envelope. Its large-prime support assertion
and odd-prime depth assertions are not refuted by this instance, but are not
proved uniformly by it either. A corrected allowance C k^2 for the binary
depth could still be compatible with a leading k^2 log k upper bound for G;
no such corrected infinite-domain theorem is established here.

Using the independently accepted SAME-H analytic lower bound in A4turn19,
equation8.6, and this actual G_32 gives the exact rational comparison



$$
q_{32}(e+\pi)-p_{32}\ge
\frac{(\Lambda_{32}/512)^{32}
 (32^2(32^2-1)/3)^{1024}\mathfrak h_{32}^{\,2}}{G_{32}}
\ge10^{4857}>1.
$$



The last comparison uses integer arithmetic, not a floating-point estimate of
e+pi or a cancellation-prone numerical determinant. It rigorously certifies a
large primitive whole error at this ONE index. It proves neither infinite
divergence nor rationality/irrationality of e+pi.

Evidence:

- [Complete exact certificate](compact_k32_content_envelope_certificate.json).
- [Finite consequence certificate](compact_k32_content_consequence_certificate.json).

The parent authored and inspected the bounded arithmetic programs. They ran
with network and credential reads denied, and writes confined to controls.
No external agent or downloaded verification program was executed.

