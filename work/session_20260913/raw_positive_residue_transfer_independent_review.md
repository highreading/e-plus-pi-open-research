> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the general positive-residue seed transfer

Date: 2026-09-13. Reviewer: audit_computations.

**FULL PASS.** This review covers every section of
`raw_positive_residue_schur_and_endpoint_transfer.md`, including the
empty seed, all cofactor boundary cases, primitive coefficient transfer,
and the actual reduced denominator conclusion. No mathematical correction
is required. The separate selected modular controls below stay inside
the already declared seed range $0\le k\le6$; they are finite inputs
to the proved theorem, not evidence for an extrapolation.

## 1. Integral ordinary Appell reduction

For any integer background $b$, including negative $b$,
$\binom bh$ is an integer. Thus



$$
\mathcal A_\ell^{[b]}(x)
 =\sum_h\binom bh(\ell)_{\underline{2h}}x^{\ell-2h}
$$



has integer coefficients. In a nonzero term with $2h\ge p$, the
falling factorial contains $p$ consecutive integers, so its
coefficient vanishes modulo $p$. This argument does not divide by
$h!$; it uses the already integral binomial coefficient. If
$2h<p$, then $h!$ is a unit and both the binomial and falling
factorial may be reduced by their integer arguments modulo $p$.
If $2h>\bar\ell$, the reduced falling factorial is zero. These
observations prove exactly



$$
\mathcal A_\ell^{[b]}(x)
 \equiv x^{\ell-\bar\ell}\mathcal A_{\bar\ell}^{[c]}(x)
 \pmod p\quad(b\equiv c\pmod p).
$$



The exponent extracted is nonnegative, and the surviving exponents on
both sides coincide. There is no reduction of rational Taylor
coefficients before clearing their factorials.

## 2. Wronskian normalization and the inflation lemma

For increasing degrees $d_i=\lambda_{r-i}+i$,
$(\mathcal A_{d_i})^{(j)}=d_i!a_{d_i-j}$. Reverse both rows and
columns of the resulting determinant to obtain Jacobi–Trudi; the two
reversal signs cancel. The hook formula is



$$
H_\lambda=\frac{\prod_i d_i!}{\prod_{i<j}(d_j-d_i)}.
$$



Consequently the normalized Wronskian in the target is exactly
$M_\lambda$, with no extra sign or factorial. The leading determinant
is the Vandermonde in the increasing degrees. I also checked this
normalization directly against Bonneux–Hamaker–Stembridge–Stevens,
*Wronskian Appell Polynomials and Symmetric Functions*, Theorem 4.1,
in the retained primary text `literature_special_polynomial_mapping/appell_2019.txt`.
[Primary paper](https://arxiv.org/pdf/1812.01864v2).

If the maximum original degree is less than $p$, the original
Vandermonde is a unit. Increasing only that degree by a nonnegative
multiple $\Delta$ of $p$ keeps every difference congruent to its
old, nonzero residue. The new Vandermonde is therefore a unit with the
same residue. Ordinary Appell reduction changes the corresponding row
polynomial to $x^\Delta\mathcal A_{d_{r-1}}^{[c]}$. In
$\mathbb F_p[x]$, every positive derivative of $x^\Delta$
vanishes, so the same factor can be extracted from the whole row of
derivatives. This proves the inflation lemma at its claimed strength.

In particular the large partition size need not be less than $p$.
No factorial involving that group size is inverted modulo $p$;
only the explicitly unit degree Vandermondes are divided out.

## 3. Same-size comparison for the actual full determinant

Write $n=up+k$, $0\le k<p/2$. Splitting the column and row
residue multisets into full blocks and residual lengths $k,k+1$
gives precisely



$$
pu^2+u(2k+1)
$$



uniform content copies, followed by the small rectangle
$(k^{k+1})$. The difference of partition sizes is
$\Delta=n(n+1)-k(k+1)$, whose quotient by $p$ is this same
uniform multiplicity. Appending $\Delta$ boxes to the first row of
the small rectangle therefore gives a partition of the actual large
size and with its exact content multiset modulo $p$.

The already independently reviewed integral central-character lemma
applies at that unchanged group size. The subsequent inflation step
uses the small degree set $k,k+1,\ldots,2k$, with maximum
$2k<p$. Its enlarged maximum is
$L=n(n+1)-k(k-1)\equiv2k\pmod p$, exactly as stated. This proves
the full-determinant congruence (3).

At $k=0$, the residual rectangle is empty. Comparing the uniform
actual content multiset to the single row of the same size, then
applying ordinary Appell reduction, gives $x^{n(n+1)}$. The source
handles this separately and does not attempt to enlarge an empty
partition's nonexistent first row.

## 4. Actual cofactors and every boundary case

The square $(n^n)$ has $pu^2+2uk$ uniform content copies plus
the residual square $(k^k)$. If $j=vp+a$, $0\le a\le k$,
its added column has $v$ complete residue sets and residual sequence
$k,k-1,\ldots,k+1-a$. These are exactly the extra boxes in
$((k+1)^a,k^{k-a})$. The size difference
$\Delta_j=n^2+j-k^2-a$ is nonnegative and divisible by $p$.
The same first-row enlargement thus compares partitions of the same
size before any inflation reduction.

The degree set is



$$
\{k,k+1,\ldots,2k\}\setminus\{2k-a\}.
$$



At $a=0$, its maximum is $2k-1$; at $a\ge1$, it is
$2k$. At $a=k$, the omitted degree is $k$. All maxima are
less than $p$. At $k=1$, the determinant is one by one and its
Vandermonde is the empty product one. At $k=0,a=0$, the separate
same-size row comparison again proves the claim. These cover all
boundary cases, with the correct nonnegative powers of $x$.

The proof does not assert a comparison at the unneeded residues
$a>k$, and no such assertion is used later.

## 5. Primitive units and the Lucas product

The exact coefficient formula uses the complementary cofactor index:



$$
b_{n,j}=(-1)^{n-j}\binom nj V_n(1)
 \frac{M_{n-j}^{[n]}(1)}{M_D^{[n]}(1)}.
$$



If the seed full determinant is a unit, the proved congruence makes
the actual full determinant a unit. Since the integer vector $b_n$
is primitive, divisibility of $V_n(1)$ by $p$ would contradict
the gcd of its coefficients. The same argument at degree $k$ gives
the seed endpoint unit. Hence the ratio
$c=V_n(1)/V_k(1)$ is defined and is a unit, without an unspecified
common scale. The formal seed at zero has the explicitly stated unit
normalization.

For $j=vp+s$, Lucas gives
$\binom nj\equiv\binom uv\binom ks\pmod p$. If $s>k$,
the coefficient vanishes: its cofactor is integral and the full
determinant is a unit. If $s\le k$, then $n-j\equiv k-s$,
which is precisely one of the cofactor residues already proved.
For odd $p$, the sign is
$(-1)^{u-v}(-1)^{k-s}$. Summing gives



$$
b_n(t)\equiv
 c\left(\sum_v(-1)^{u-v}\binom uv t^{pv}\right)b_k(t)
 =c(t-1)^{up}b_k(t).
$$



Every division in this step is by an established unit. No unit
assumption on the individual cofactors or on the seed's leading
coefficient is required.

## 6. Exact differential transfer to V and the endpoint

The crucial differential identity is an equality of integer
polynomials before reduction:



$$
(t-1)^nV_n(t)=(1+\partial_t^2)^n[t^n b_n(t)].
$$



For the coefficient of $t^\ell$, the two sides are respectively
$\ell!^{-1}\sum_h\binom nh U_{n+\ell-2h}$ and
$\ell!^{-1}\sum_h\binom nh U_{\ell-n+2h}$; replacing $h$
by $n-h$ makes the finite sums identical. Coefficients outside the
actual degree range are zero. This independently verifies the
factorial and the index reversal, without interchanging the two
different Rodrigues derivatives.

Over $\mathbb F_p[t]$, $\partial_t^p=0$, so the operator
reduces to $(1+\partial_t^2)^k$. The product
$[t(t-1)]^{up}$ is a $p$-th power and has zero derivative; it
commutes through every derivative in the reduced operator. Applying
the identity at the seed degree gives



$$
(t-1)^n V_n(t)
 =c\,t^{up}(t-1)^n V_k(t)\quad\text{in }\mathbb F_p[t].
$$



Cancellation in this integral domain proves (7). Evaluation at $t=1$
is not used to cancel the vanishing factor. The argument is expressly
prime-level; it does not establish a congruence modulo $p^h$.

In the exact endpoint border, only the shifted coefficients
$r=up+s$, $0\le s\le k$, remain after (7). Terms of its inner
sum with $j\ge p$ vanish by the falling factorial. For $j<p$,
$j!$ is a unit and the factors reduce to
$\binom{k+j}{j}(k+s)_{\underline j}$. Since $k+s\le2k<p$,
the surviving finite sum is exactly the seed border $D_{k,s}$.
This proves (8) with the actual common orientation.

If both seed quantities in (9) are units, the actual exponential
endpoint is a unit. The positive arctangent valuation under the stated
factorial threshold then makes the actual combined numerator a unit.
The exact reduction by $\gcd(Z_n,N_n)$ consequently gives
$v_p(q_n)=v_p(Z_n)\ge v_p(n!)$. No cofactor ratio has been
substituted for the actual endpoint rational.

## 7. Selected exact seed controls

The following fixed pairs were independently checked, all within the
already declared degrees $0\le k\le6$:

| $k$ | $p$ | $M_D^{[k]}(1)\bmod p$ | $\widehat P_{e,k}(1)\bmod p$ | Seed condition |
|---:|---:|---:|---:|:---|
| 1 | 5 | 4 | 0 | Fails at the endpoint |
| 2 | 5 | 0 | 1 | Fails at the determinant |
| 2 | 7 | 1 | 2 | Holds |
| 3 | 7 | 5 | 3 | Holds |
| 3 | 13 | 1 | 0 | Fails at the endpoint |
| 4 | 11 | 7 | 4 | Holds |
| 5 | 11 | 6 | 0 | Fails at the endpoint |
| 6 | 13 | 0 | 9 | Fails at the determinant |

The independent checker constructs the full and cofactor values from
integer Appell Wronskians modulo the indicated prime, with unit
Vandermondes. It then reconstructs the polynomial through the exact
differential identity. The endpoint is computed both from the integer
border and independently by reconstructing $U,S,\widehat Q$ and
evaluating the truncation of $\widehat Q e^z$. In this second
calculation $2k<p$, so every exponential Taylor denominator used
is a unit. All results agree with the saved seed atlas.

Files:
`check_positive_residue_selected_seeds_independent.py` and
`positive_residue_selected_seeds_independent_checks.json`.
No large integer was factored, and no larger seed degree was examined.
The global factorizations printed elsewhere in the atlas are outside
the scope of these modular checks and are not needed for the conclusions.

The requested $p=7,k=3$ case is especially informative. Its cofactor
residues are $(0,2,2,5)$, and its seed polynomial has coefficient
vector $(2,2,1,0)$ modulo seven. Its leading coefficient drops, but
its value at one is five and its exponential endpoint is three. Thus
the theorem's unit condition holds exactly as stated, without a hidden
normality condition modulo seven. The degree-two seed modulo seven
also satisfies the unit condition. Both positive residue classes
therefore have the asserted eventual factorial denominator lower bound.

The atlas uses the opposite common primitive sign at degree one from
the illustrative $V_1=2-t$ convention in the source. Both $V_1(1)$
and $\widehat P_{e,1}(1)$ change sign together, so the ratio $c$,
the transfer identity, and every seed-unit condition are unchanged.
This is not a normalization discrepancy.

## 8. Conclusion and retained limits

The general theorem passes for every odd prime and every seed residue
$0\le k<p/2$ at the stated seed-unit condition. The finite seed
controls are exact checks of selected inputs to that all-index theorem.
Neither a vanishing determinant seed nor a vanishing endpoint seed is
silently bypassed, and no higher prime-power lift is inferred. These
arithmetic extensions do not by themselves establish the original
irrationality objective or a shrinking primitive subsequence.
