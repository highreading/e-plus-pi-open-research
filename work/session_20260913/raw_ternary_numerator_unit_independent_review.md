> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the ternary numerator-unit extension

Date: 2026-09-13. Reviewer: audit_computations.

**FULL PASS, supplementary independent derivation.** The stable target
`raw_appell_minus_one_hook_and_endpoint_residue.md` has now been audited
in full, including its stronger all-prime and full-modulus extension;
see `raw_appell_minus_one_residue_independent_review.md`. The present
note retains the independently reconstructed ternary proof, using only
the cofactor indices divisible by three. No new degree, prime, or
determinant scan is used.

## 1. Integral representation-theoretic input and specialization

The integral central-character lemma has just been independently audited
in `raw_appell_neighbor_content_independent_review.md`, against Ryba's
published Proposition 3.11 and Theorem 3.14. At a fixed symmetric-group
size, matching content multisets modulo three imply coefficientwise
congruence of augmented Schur functions in the integral power sums.
Here their specialization is integral:



$$
p_1=x,\qquad p_{2h}=2n(-1)^{h-1},\qquad
 p_{2h+1}=0\quad(h\ge1).
$$



All comparisons below are explicitly between partitions of the same
size. No deletion of uniform content blocks or change of group size is
performed.

Let $n=3m+1$, $m\ge0$, and retain
$\lambda_D=(n^{n+1})$,
$\lambda_j=((n+1)^j,n^{n-j})$, and
$M_\lambda=H_\lambda s_\lambda(a(x))$, where
$a_k=[t^k]e^{xt}(1+t^2)^n$.

For the full rectangle, the row indices contain $m,m+1,m+1$ copies
of residues $0,1,2$; the column indices contain $m,m+1,m$.
Consequently the three content multiplicities are



$$
(3m^2+3m+1,\quad3m^2+3m,\quad3m^2+3m+1).
$$



This is a number of complete residue blocks followed by the two residues
$0,-1$, exactly the multiset for the column partition of size
$N=n(n+1)\equiv2\pmod3$. The elementary-function comparison gives



$$
M_D(x)\equiv N![t^N]e^{xt}(1+t^2)^{-n}\pmod3.
$$



Every falling factorial $(N)_{2h}$ with $h\ge2$ contains a
multiple of three. Its coefficient $\binom{n+h-1}{h}$ is an integer,
so these terms vanish modulo three. The $h=1$ coefficient is
$-nN(N-1)\equiv1$. Thus



$$
M_D(x)\equiv x^N+x^{N-2},\qquad M_D(1)\equiv-1\pmod3.
 \tag{1}
$$



For a cofactor index $j=3h$, the square $(n^n)$ has
$3m^2+2m$ copies of each content residue and one extra zero.
The added column boxes have $h$ full residue blocks. The resulting
content multiset agrees with that of the row of size $s=n^2+j$,
which is $1$ modulo three. Hence



$$
M_j(x)\equiv s![t^s]e^{xt}(1+t^2)^n\equiv x^s\pmod3
 \qquad(j\equiv0\pmod3).
 \tag{2}
$$



In this last congruence the $h=1$ falling factorial already contains
$s-1$, and higher ones contain a multiple of three. In particular,
$M_j(1)\equiv1$ for precisely the cofactor indices needed below.
The proof does not require such a statement for all other indices.

## 2. Primitive scaling is retained

The exact primitive coordinate identity is



$$
b_j:=\frac{U_j}{(n+j)!}
 =(-1)^{n-j}\binom nj V(1)
   \frac{M_{n-j}(1)}{M_D(1)}.
 \tag{3}
$$



The integer vector $b$ has gcd one. This follows from the two
integral triangular transformations with diagonal one from primitive
$V$ to the high coefficients of $W=t^n(t-1)^nV$, and then to
$b$. It is independent of the new local comparison.

Equation (1) makes the denominator in (3) a three-adic unit. If
$V(1)$ were divisible by three, all $b_j$ would be divisible by
three, contradicting their gcd. Thus $V(1)$ is a unit modulo three.
This uses integrality of all augmented minors; no unit assertion for
the intermediate minors is needed.

## 3. The high-tail inverse and derivative functional

Write $w_j^{\mathrm{hi}}=[t^{2n+j}]W(t)$. The exact high-tail
relation and its inverse are



$$
w_j^{\mathrm{hi}}
 =\sum_{r=j}^n(-1)^{r-j}\binom n{r-j}V_r,
 \qquad
 V_r=\sum_{j=r}^n\binom{n+j-r-1}{j-r}w_j^{\mathrm{hi}}.
 \tag{4}
$$



They are the coefficient relations for multiplication by
$(1-z)^n$ and its inverse, truncated at degree $n$, in reversed
polynomial coordinates. Summing the second relation with weight $r$
gives



$$
V'(1)=\sum_{j=0}^n\binom{n+j}{n+1}w_j^{\mathrm{hi}}.
 \tag{5}
$$



For completeness, the coefficient identity used here is



$$
\sum_{r=0}^j r\binom{n+j-r-1}{j-r}
 =\binom{n+j}{n+1}.
$$



Its generating series in $j$ is
$(\sum_{r\ge0}rz^r)(1-z)^{-n}=z(1-z)^{-n-2}$.
This also covers $j=0$, when both sides vanish.

The exact inverse factorial-tail relation is



$$
w_j^{\mathrm{hi}}=
 \sum_{h\ge0,\ j+2h\le n}
 \binom nh\frac{(n+j+2h)!}{(n+j)!}\,b_{j+2h}.
 \tag{6}
$$



One can obtain (6) directly by multiplying
$S=(1+t^2)^nU$ and using
$S^{(n)}=\sum_r(n+r)!w_{n+r}t^r$.
Thus the signs and factorials are independently fixed, rather than
inferred by reversing a congruence.

Lucas's theorem at the units digit in (5) leaves only $j\equiv1$
modulo three. Indeed $n+1\equiv2$, whereas $n+j$ has units digit
two only in that case. If $j\equiv1$, then $n+j+1\equiv0$;
this is the first factor in every nontrivial factorial quotient in
(6). Therefore



$$
w_j^{\mathrm{hi}}\equiv b_j\pmod3\quad(j\equiv1\pmod3).
 \tag{7}
$$



No estimate of a factorial quotient's denominator is hidden here:
the quotient is the product of $2h$ consecutive positive integers.

## 4. The remaining finite sum is exactly one

Write $j=3k+1$, $0\le k\le m$. Lucas gives



$$
\binom nj\equiv\binom mk,qquad
 \binom{n+j}{n+1}\equiv\binom{m+k}{m}\pmod3.
$$



The relevant cofactor index is $n-j=3(m-k)$, so equation (2) applies.
Equations (1), (3), (5), and (7) imply



$$
\frac{V'(1)}{V(1)}
 \equiv-\sum_{k=0}^m(-1)^{m-k}
     \binom mk\binom{m+k}{m}\pmod3.
 \tag{8}
$$



The sum in (8) is exactly one over the integers. The polynomial
$\binom{m+x}{m}$ has degree $m$ and leading coefficient $1/m!$;
its $m$-th forward difference is therefore the constant one.
Equivalently the sum is the generalized Vandermonde identity
$(-1)^m\binom{-1}{m}=1$. This is valid also at $m=0$.
Consequently



$$
V'(1)\equiv-V(1)\pmod3.
 \tag{9}
$$



## 5. The actual exponential endpoint is a unit

The exact evaluated border has the positive orientation



$$
\widehat P_e(1)=\sum_rV_r D_{n,r},\qquad
 D_{n,r}=\sum_{j=0}^{n+r}\binom{n+j}{j}(n+r)_j.
$$



For $n\equiv1\pmod3$, the $j=2$ binomial is a multiple of
three, and every falling factorial for $j\ge3$ contains a multiple
of three. The terms $j=0,1$ give



$$
D_{n,r}\equiv1+(n+1)(n+r)\equiv2r\pmod3.
$$



Thus $\widehat P_e(1)\equiv2V'(1)\equiv V(1)\not\equiv0\pmod3$.
The actual endpoint numerator, not merely an individual cofactor, is
therefore a unit whenever the arctangent contribution is divisible by
three.

The already established global divisor 

$$
n!\mid\operatorname{cont}
\widehat Q
$$

 gives



$$
v_3(\widehat P_a(1))\ge
 v_3(n!)-\lfloor\log_3(2n)\rfloor.
$$



Under the strict positivity threshold, the actual
$N=\widehat P_e(1)+4\widehat P_a(1)$ is a three-adic unit. Hence



$$
v_3(q_n)=v_3(Z_n)\ge v_3(n!).
 \tag{10}
$$



For an elementary sufficient uniform threshold, every $n\ge9$
satisfies $v_3(n!)>\lfloor\log_3(2n)\rfloor$. Put
$k=\lfloor n/3\rfloor\ge3$; then $2n\le6k+4<3^k$, where the
last inequality follows from $22<27$ and induction. Thus the right
side is at most $k-1$, while $v_3(n!)\ge k$.

Combining (10) with the already reviewed residue-zero and residue-minus-
one theorems gives the factorial lower bound for all $n\ge9$,
without a residue restriction. No conclusion about primes beyond three
or every shrinking subsequence follows from this single-prime bound.
