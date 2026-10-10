> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact precision of the h1 logarithmic connection

Author result L17,2026-10-02. This is arithmetic for the scalar h1 connection in H1_LOGARITHMIC_MOMENT_INTEGER_JETS.md, not a new prime atlas or a theorem about deeper final Gram gcd content. Root's distinct gauged pullback M15 has a related one-digit carry mechanism; its endpoint arrays and proofs are not repeated here. The standard Mahler/Amice criteria are credited to O'Desky–Richman's primary exposition, §2, Theorem2.2, https://arxiv.org/html/2012.04615v4 .

Retain q0=1-z+z²/2, alpha=1/q0, L'=alpha,L(0)=0, and

    S_n=(e^z alpha)^(n)(0),
    D_n=(e^z/(1-z))^(n)(0),
    T_n=(e^z L/(1-z))^(n)(0).

These are the integer sequences in L16. Fix ANY odd prime p and chi=(-1|p). The result is:

1. S,D have congruence-preserving continuous interpolations to Z_p. T has a continuous, locally analytic interpolation to Z_p with Lipschitz constant p. The function pT is congruence-preserving. T is not globally1-Lipschitz.
2. At EVERY depth k>=1 and nonnegative integer indices n,n+p^k t,

       T_(n+p^k t)-T_n = -p^(k-1)t chi D_n mod p^k.       (1)

   The same identity holds for the interpolated functions at p-adic arguments. For a residue cell r+pZ_p with D_r a unit, every nonzero shift inside the cell loses exactly ONE digit:

       v_p(T(x)-T(y))=v_p(x-y)-1.                       (2)

   On a cell with D_r=0 mod p, T is1-Lipschitz. Thus the precision classification is exact at every cell, not an extrapolation from finite depths.
3. On a unit-D cell, z↦T(r+pz) is an isometric bijection Z_p→Z_p. In particular every prescribed connection value has one preimage in that cell. This is a statement about the index interpolation, not independence of the prime-index values T_(p−1) as p varies.

## 1. The explicit Mahler coefficients

Write alpha(z)=sum a_j^ord z^j; all a_j^ord belong to Z[1/2]. The coefficients of the Mahler expansion T(x)=sum c_j binom(x,j) are exactly

    c_0=0,
    c_j=j![z^j]L(z)/(1-z)
       =j! sum_(t=0)^(j-1) a_t^ord/(t+1), j>=1.          (3)

Indeed the exponential generating function of the forward differences of an integer sequence is e^(−z) times that sequence's EGF. The c_j are integers since T_n is an integer sequence. Formula(3) gives

    v_p(c_j)>=v_p(j!)-floor(log_p j).                     (4)

The right side grows linearly in j, proving uniform convergence of the Mahler series and continuous Z_p-valued interpolation. The same bound has liminf v_p(c_j)/j>=1/(p−1)>0, so the standard Amice criterion gives local analyticity. A loss of a fixed one digit NEVER obstructs continuity.

For S and D the respective Mahler coefficients are j!a_j^ord and j!, so their factorial-polynomial expansions are1-Lipschitz. One may prove this directly by truncating their sums of integral falling-factorial polynomials; no analytic interpolation of n! itself is assumed.

The Gaussian root computation from L16 gives a_(p−1)^ord=chi mod p. In the interval p<=j<2p, the only denominator in(3) divisible by p is t+1=p. Wilson therefore gives the precise exceptional block

    c_(p+r)=-chi r! mod p, 0<=r<p.                       (5)

For j<p, v_p(c_j)>=0=floor(log_p j). For j>=2p,

    v_p(j!)>=2 floor(log_p j),

so(4) implies v_p(c_j)>=floor(log_p j). To see this factorial bound, when floor(log_p j)=1 use j>=2p; when the logarithm is s>=2, use j>=p^s and

    v_p((p^s)!)=1+p+...+p^(s−1)>=2s,

valid for every odd p. Thus every Mahler coefficient outside the SINGLE block p,...,2p−1 satisfies the usual metric-map bound. Multiplication by p repairs this block as well. Conversely c_p=-chi is a unit, so T cannot be1-Lipschitz: T_p−T_0=-chi mod p although p−0 is divisible by p.

## 2. All-depth carry from the exceptional block

Let R(x) be the sum of all Mahler terms with j<p or j>=2p. The preceding bounds make R1-Lipschitz. Hence its change under delta=p^k t is0 mod p^k. Only the finite exceptional block contributes.

For1<=ell<=2p−1,

    ell binom(delta,ell)=delta binom(delta−1,ell−1).

Consequently binom(delta,ell)=0 mod p^k except possibly ell=p. In that case

    binom(delta,p)=p^(k−1)t mod p^k,

because binom(delta−1,p−1)=1 mod p. These identities also hold for negative integral shifts via the integral generalized binomial polynomial.

Vandermonde now gives

    binom(n+delta,p+r)-binom(n,p+r)
      =p^(k−1)t binom(n,r) mod p^k.

Combine this with(5):

    T_(n+delta)-T_n
      =-p^(k−1)t chi sum_(r=0)^(p−1)binom(n,r)r! mod p^k.

The last finite sum is D_n modulo p since all higher falling-factorial terms contain p. This proves(1) for every depth, including the first. Density and continuity extend the congruence to Z_p. If t is a unit, its leading coefficient is nonzero precisely when D_n is a unit, proving(2). If D_n=0 mod p it instead gives v_p(T(x)-T(y))>=v_p(x-y), proving the stated metric property on that entire residue cell.

## 3. A precise arithmetic elimination obstruction

S(x),D(x),and their integral shifts are1-Lipschitz. Any polynomial over Z_p in x and finitely many such companions is1-Lipschitz, as is any1-Lipschitz composition of them. On a unit-D cell such an expression cannot equal T, by(2). Rational expressions give the same obstruction whenever their denominators are units throughout the cell. Expressions with an explicit p denominator are outside this statement, and continuous expressions in general are not excluded.

The cell map z↦T(r+pz) preserves distances by(2). At every finite residue level its distinct domain classes have distinct image classes; their equal cardinality p^s makes the map bijective at that level. Compactness and completeness then give an isometric bijection on Z_p. No distribution of values obtained by varying p is inferred.

## 4. Complete numerator and the actual-q boundary

For the actual h1 prime-index quotient put C=D_(p−1) mod p. The previously proved complete gateways are

    nu4/4=-85T_(p−1)+(156−194C)S_(p−1)
              +(163−97C)S_(p−2)+(12−85chi)C−78,

    nu5/384=-93T_(p−1)+(24C+90)S_(p−1)
              +(155−31C)S_(p−2)−(148+93chi)C−28 mod p.

When C is a unit, the logarithmic connection has the exact precision defect on the index cell −1+pZ_p. In b4 with p>8,p!=17, or b5 with p>10,p!=31, its coefficient in the displayed complete numerator is a unit. Thus it cannot be eliminated on that cell by an integral congruence-preserving expression in the rational factorial companions. This identifies a normalized arithmetic obstruction, without pretending that it proves modular independence at the single index p−1.

The higher-index interpolation here is NOT the actual Gram center after division by its boundary content. The existing normalized transfer still yields actual v_p(q_n)=2v_p(n!) only when the displayed prime-index nu is a unit and all endpoint digits are units, with full beta/kappa and the final evaluated gcd retained. If nu=0 mod p, neither(1) nor the existence of an interpolated connection zero proves any additional cancellation in q_n. A valid deeper center analysis must derive that separate interface. No full-sequence primitive gain or irrationality of e+pi is asserted.

## 5. Supporting receipt

h1_logarithmic_mahler_precision.py verifies the exact Mahler formula and its exceptional block through4p, and the derived carry through three depths at the two already used receipt primes11 and13. It saves all bounded rows in H1_LOGARITHMIC_MAHLER_PRECISION_RECEIPT.json. These checks support the identities; the all-depth theorem is proved above. They are not a prime scan, a repeated Gram atlas, or an independent audit.
