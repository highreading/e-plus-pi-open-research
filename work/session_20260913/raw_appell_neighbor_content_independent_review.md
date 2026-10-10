> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: integral content congruences modulo n+1

Date: 2026-09-13. Reviewer: audit_computations.

**FULL PASS.** This is an independent symbolic audit of
`raw_appell_neighbor_content_and_denominator.md`, Sections 1–8. No
mathematical correction is required. No new canonical degree, prime,
determinant, or root scan was performed. The review checks the integral
representation-theoretic input against the published primary source,
then independently reconstructs the content counts, coefficient
divisibility, primitive normalization, and actual denominator conclusion.

The conclusion concerns all sufficiently large indices in the residue
class minus one at each fixed odd prime. It does not assert the same
bound in the other residue classes, nor exclude every even subsequence.

## 1. The primary input is integral at fixed group size

The source inspected directly is Christopher Ryba, *Stable centres of
wreath products*, Algebraic Combinatorics 6 (2023), 413–455, in particular
Proposition 3.11 and Theorem 3.14 on printed pages 426–428, with the
integral interpretation of Theorem 3.8 and its evaluation diagram.
[Published primary paper](https://alco.centre-mersenne.org/item/10.5802/alco.264.pdf).
The locally retained published PDF and text are
`literature_special_polynomial_mapping/ryba_2023_stable_centres.pdf`
and `.txt`.

Proposition 3.11 gives a monomial symmetric function of the
Jucys–Murphy elements as its corresponding class sum, with leading
coefficient one, plus integer combinations of earlier class sums.
The order first decreases reduced-cycle size, then the number of parts.
Theorem 3.14 evaluates a class sum's scalar on the box contents of a
partition, at the fixed symmetric-group size. These are the integral
statements needed here; ordinary equality of prime blocks alone would
not suffice.

Here is the fixed-size deduction in full. In $\mathbb Z S_s$, every
valid reduced-cycle class is reached by the above finite triangular
induction. The coefficients in that induction are integers because the
JM products have integer group-algebra coefficients and centrality makes
the coefficients constant on classes. Invalid reduced-cycle types are
zero and do not require division or a new induction step. Thus for each
class $\mathcal C$ there is a symmetric polynomial
$F_{\mathcal C,s}\in\mathbb Z[x_1,\ldots,x_s]$ whose JM evaluation is
that class sum. This also follows from the published integral
Farahat–Higman formulation: integer-valued size polynomials are evaluated
at the same integer $s$, so their values are integers.

If $\lambda,\eta\vdash s$ have matching content multisets modulo an
arbitrary integer $q$, then after a permutation their individual
contents agree modulo $q$. Consequently



$$
F_{\mathcal C,s}(\operatorname{cont}\lambda)
 \equiv F_{\mathcal C,s}(\operatorname{cont}\eta)\pmod q.
$$



No prime reduction or subsequent lifting occurs. Frobenius's formula and
$H_\lambda=s!/f^\lambda$ give



$$
H_\lambda s_\lambda
 =\sum_{\mu\vdash s}
 \frac{s!}{z_\mu}\frac{\chi^\lambda(\mu)}{f^\lambda}p_\mu
 =\sum_{\mu\vdash s}\omega_\lambda(\mathcal C_\mu)p_\mu.
$$



It follows that the augmented Schur polynomials agree coefficientwise in
$\mathbb Z[p_1,p_2,\ldots]$ modulo the entire $q$. The same-size
hypothesis is essential and is satisfied by both comparisons in the
target note.

There is also no rational-specialization gap. For
$a_k(x)=[t^k]e^{xt}(1+t^2)^n$, the power sums are



$$
p_1=x,\qquad p_{2h}=2n(-1)^{h-1}\ (h\ge1),\qquad
 p_{2h+1}=0\ (h\ge1).
$$



Thus the power-sum specialization is a homomorphism to $\mathbb Z[x]$.
Although individual complete functions $a_k$ have rational
coefficients, the augmented expressions and their congruences are
integer polynomials.

## 2. Both content comparisons have the required multiplicities

Write $q=n+1$. The full shape $\lambda_D=(n^q)$ has $q$ boxes
per column. Their contents are consecutive integers, so each of the
$n$ columns contributes one copy of every residue. The row partition
of the same size $N=nq$ also has $n$ copies of every residue. This
justifies comparison with $N!h_N$, not with a smaller row partition.

For the square $(n^n)$, let row and column indices range over the
nonzero residues modulo $q$. There are $q-1$ pairs with prescribed
difference zero and $q-2$ pairs with any prescribed nonzero
difference. Hence its content multiset consists of $q-2$ complete
residue blocks and one additional zero.

The shape
$\lambda_j=((n+1)^j,n^{n-j})$ adds the boxes in column $q$, rows
$1,\ldots,j$. Their contents are $-1,\ldots,-j$ modulo $q$.
The resulting multiset is



$$
(q-2)\text{ full residue blocks},\quad 0,-1,\ldots,-j.
$$



Its total size is $s=N_j=q(q-2)+(j+1)=n^2+j$. The same-size column
partition has contents $0,-1,\ldots,-(s-1)$, with exactly this
multiset. The counts also work for $q=2$, when the complete-block
multiplicity is zero, and for $j=n=q-1$, when the final list itself
is one full block. In particular no missing or surplus zero residue is
hidden at either endpoint.

## 3. The full composite-modulus coefficient calculation

The row comparison is



$$
M_D(x)\equiv
 \sum_{h=0}^{\min(n,\lfloor N/2\rfloor)}
 \binom nh(N)_{2h}x^{N-2h}\pmod q.
$$



Every nonconstant correction has $h\ge1$, and its falling factorial
contains $N=nq$. Its other factors are integers, proving
$M_D(x)\equiv x^N\pmod q$.

The column comparison uses elementary functions. Their generating series
is exactly



$$
\sum_{k\ge0}e_k t^k
 =\bigl(e^{-xt}(1+t^2)^n\bigr)^{-1}
 =e^{xt}(1+t^2)^{-n}.
$$



Therefore



$$
M_j(x)\equiv\sum_{h=0}^{\lfloor s/2\rfloor}
 (-1)^h\binom{n+h-1}{h}(s)_{2h}x^{s-2h}\pmod q.
$$



For $h\ge2$, the coefficient factors as



$$
(-1)^h n(n+1)\cdots(n+h-1)
 \frac{(s)_{2h}}{h!}.
$$



Since the summation has $2h\le s$,
$(s)_{2h}/h!=[(2h)!/h!]\binom{s}{2h}$ is an integer.
This is the point that preserves every prime-power factor of $n+1$
even when $h!$ is divisible by the same prime. All terms with
$h\ge2$ vanish modulo $q$. The remaining correction is



$$
-n s(s-1)\equiv (j+1)j\pmod q,
$$



because $n\equiv-1$ and $s\equiv j+1$. This proves both stated
polynomial congruences. When $s<2$, the correction is absent; its
claimed coefficient is zero. At $j=0,n$, the correction vanishes
modulo $q$, proving the three endpoint unit congruences. Intermediate
minor units are neither needed nor generally true.

## 4. The primitive normalization and cofactor indices

The already reviewed exact normalizations can be checked independently
at the level needed here. Deleting row zero and column $j$ from the
actual $A_n$, then transposing, gives the Jacobi–Trudi determinant
for $\lambda_j$, with cofactor sign $(-1)^j$. Its hook ratio is



$$
r_j=\frac{H_D}{H_j}=\frac{(2n-j)!}{j!(n-j)!}.
$$



Thus $v_j=(-1)^j r_j M_j(1)/M_D(1)$. The exact polynomial relation
$z^nU(1/z)=n!V(1)v(z)$ yields



$$
\frac{U_j}{(n+j)!}
 =(-1)^{n-j}\binom nj V(1)\frac{M_{n-j}(1)}{M_D(1)}.
 \tag{A}
$$



The complementary index $n-j$, sign, and binomial factor are all
necessary; they are correctly retained in the target.

Let $b_j=U_j/(n+j)!$. The transformation from primitive $V$ to
the high coefficients $w_{2n},\ldots,w_{3n}$ of
$t^n(t-1)^nV$ is integral triangular with diagonal one. The reversed
division from these coefficients to $b_j$ is also integral
triangular with diagonal one, because its off-diagonal terms are



$$
(-1)^h\binom{n+h-1}{h}
 \frac{(n+j+2h)!}{(n+j)!}w_{2n+j+2h}.
$$



Both inverse transformations are integral. Consequently the $b_j$
are integers with gcd one, independently of any new local assertion.

For $p\mid n+1$, $M_D(1)$ is a unit. Formula (A) shows that a
positive valuation of $V(1)$ would divide every $b_j$, which is
impossible. Taking $j=n$ then gives
$b_n=V_{\rm lead}=V(1)M_0(1)/M_D(1)$. The quotient is congruent to
one in the localization away from $n+1$; multiplying by the integer
$V(1)$ proves the full integer congruence
$V_{\rm lead}\equiv V(1)\pmod{n+1}$. This retains actual primitive
scaling and all valuations dividing the composite modulus.

## 5. Content and the actual reduced denominator

Because $U_j=(n+j)!b_j$, all $U_j$ are divisible by $n!$
globally. Multiplication by the primitive polynomial $(1+t^2)^n$
preserves integer content, so $S=(1+t^2)^nU$ has the same content as
$U$. In



$$
\widehat Q(z)=z^{2n}S^{(n)}(1/z)/n!,
$$



the coefficient obtained from $S_k$ is
$\binom{k}{n}S_k$. Every such binomial is an integer; omitted
coefficients with $k<n$ do not weaken divisibility. Therefore
$n!\mid\operatorname{cont}U\mid\operatorname{cont}\widehat Q$
and $n!\mid Z=\widehat Q(1)$, without localization.

At $p\mid n+1$, equation (A) at $j=0$ has binomial one and the
unit $M_n(1)/M_D(1)$. Thus $b_0$ is a unit and
$v_p(U_0)=v_p(n!)$. This proves equality for the valuation of
$\operatorname{cont}U$, but only the stated lower bounds for
$\operatorname{cont}\widehat Q$ and $Z$. Possible extra
endpoint factors have not been discarded.

The exponential endpoint formula has the correct positive orientation:



$$
\widehat P_e(1)=\sum_rV_r D_{n,r},\qquad
 D_{n,r}=\sum_{j=0}^{n+r}\binom{n+j}{j}(n+r)_j.
$$



For $j\ge1$, the summand equals



$$
(n+1)(j-1)!\binom{n+j}{j-1}\binom{n+r}{j},
$$



as follows by direct cancellation of factorials. It is an integer
multiple of $n+1$, so $\widehat P_e(1)\equiv V(1)\pmod{n+1}$
and is a unit at every prime dividing that modulus.

All denominators in the arctangent Taylor coefficients through degree
$2n$ divide $\operatorname{lcm}(1,\ldots,2n)$. The global
factorial divisor therefore gives



$$
v_p(\widehat P_a(1))\ge
 v_p(n!)-\lfloor\log_p(2n)\rfloor.
$$



Whenever the right side is positive, the actual integer numerator
$N=\widehat P_e(1)+4\widehat P_a(1)$ is a $p$-unit. In the
actual reduction $q=|Z|/\gcd(|Z|,|N|)$, none of the $p$-part of
$Z$ can cancel. Hence



$$
v_p(q)=v_p(Z)\ge v_p(n!).
$$



The prime-two exception to the threshold is justified by the separately
reviewed all-degree oddness of $\widehat P_e(1)$ and integrality of
$\widehat P_a$: the factor four makes $N$ odd. The fixed odd-prime
asymptotic follows from Legendre's formula, whose digit-sum error is
$O_p(\log n)$. No unproved bound on the weighted-minor defect is
used, and the actual endpoint gcd has been explicitly accounted for.

## 6. Consequences, dependencies, and retained scope

The prior $2n$ theorem and the new $n+1$ theorem combine without
a lifting argument, giving the stated unit and lcm congruences. On
$n=p^\nu-1$, the earlier identity
$d_p+v_p(V(1))=\nu$ now gives $d_p=\nu$; the exponential unit
gives $e_p=0$. This is a consequence of the new proof, not an input
to it.

For each of $p=3,5,7,11$, the established factorial bound applies
at both residues zero and minus one, for all sufficiently large indices.
The four choices are independent by CRT. With even parity imposed,
they give exactly $2^4=16$ classes modulo $2310$. Combining the
finite set of valuation lower bounds with the exact dyadic rate and the
accepted even error asymptotic proves growth of the absolute primitive
forms on those classes. The strict rate comparison used in the target
is the independently proved one in
`raw_appell_column_endpoint_independent_review.md`; it is independent
of the new JM step.

The last section correctly identifies a remaining obstruction: removing
uniform content blocks generally changes the symmetric-group size.
The class-sum polynomials can depend on that size, so the present lemma
cannot automatically reduce an arbitrary residue class to a smaller
partition. Neither a whole-polynomial monomial congruence for $V$
modulo $n+1$, nor a universal denominator bound at other residues,
has been proved here.

**Audit conclusion:** all stated all-index congruences, primitive unit
claims, content valuations, thresholded actual-denominator bounds, and
the sixteen-class consequence pass. No finite data are used in the proof.
