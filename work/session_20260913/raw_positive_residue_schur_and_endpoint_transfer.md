> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Small positive residues: same-size Schur reduction and actual endpoint transfer

Date: 2026-09-13. Original derivation by audit_sources, incorporating
root's proposed same-size comparison and exact differential transfer.
Independent review: **FULL PASS** by audit_computations, recorded in
raw_positive_residue_transfer_independent_review.md.
No new canonical degree or prime scan is used.

The integral same-size content comparison is the reviewed lemma in
raw_appell_neighbor_content_and_denominator.md, with its full passing
audit raw_appell_neighbor_content_independent_review.md. The normalized
Wronskian identity is elementary from Jacobi--Trudi and the hook product;
it is also the Appell framework of Bonneux--Hamaker--Stembridge--Stevens,
[arXiv:1812.01864v2](https://arxiv.org/pdf/1812.01864v2), Theorem 4.1.
We keep same-size comparison separate from the subsequent Wronskian
calculation; no unproved change of symmetric-group size is made.

## 1. Statement in the original normalization

For an integer background $b$, define the integral monic Appell
polynomials


$$
\mathcal A_\ell^{[b]}(x)=
 \ell![t^\ell]e^{xt}(1+t^2)^b
 =\sum_{h=0}^{\lfloor\ell/2\rfloor}
       \binom bh(\ell)_{\underline{2h}}x^{\ell-2h}.
 \tag{1}
$$


Negative $b$ is allowed in the two elementary lemmas below; the
application here uses nonnegative $n,k$. For a partition $\lambda$,
write $M_\lambda^{[b]}=H_\lambda s_\lambda$ under this complete-function
specialization. These are integer polynomials: the universal augmented
Schur polynomial has integer coefficients in the power sums, here
$p_1=x,\ p_{2j}=2b(-1)^{j+1},\ p_{2j+1}=0$ for $j\ge1$.

The actual full and cofactor polynomials are


$$
M_D^{[n]}=M_{(n^{n+1})}^{[n]},\qquad
 M_j^{[n]}=M_{((n+1)^j,n^{n-j})}^{[n]},\quad0\le j\le n.
 \tag{2}
$$


Let $p$ be an odd prime, $0\le k<p/2$, and $n\equiv k\pmod p$.
Then the following polynomial congruences hold:


$$
\boxed{
 M_D^{[n]}(x)\equiv
 x^{\,n(n+1)-k(k+1)}M_D^{[k]}(x)\pmod p.}
 \tag{3}
$$


For $j\equiv a\pmod p$ with $0\le a\le k$,


$$
\boxed{
 M_j^{[n]}(x)\equiv
 x^{\,n^2+j-k^2-a}M_a^{[k]}(x)\pmod p.}
 \tag{4}
$$


No congruence for the remaining cofactor residues $a>k$ is
asserted. Those are not needed in the weighted primitive-coefficient
formula, by Lucas's theorem.

For $k=0$, use the empty-partition conventions


$$
M_D^{[0]}=M_0^{[0]}=1,\quad V_0(t)=b_0(t)=1,\quad
 \widehat P_{e,0}(1)=1.
 \tag{5}
$$


Suppose in addition $p\nmid M_D^{[k]}(1)$. Then the actual primitive
polynomials have unit values $V_n(1),V_k(1)$ in $\mathbb Z_p$.
Writing $c=V_n(1)/V_k(1)\in\mathbb Z_p^\times$, their polynomial
and endpoint reductions are


$$
\boxed{b_n(t)\equiv c(t-1)^{n-k}b_k(t)\pmod p,}       \tag{6}
$$




$$
\boxed{V_n(t)\equiv c\,t^{n-k}V_k(t)\pmod p,}         \tag{7}
$$




$$
\boxed{\widehat P_{e,n}(1)
       \equiv c\,\widehat P_{e,k}(1)\pmod p.}          \tag{8}
$$


Here $b_{n,j}=U_{n,j}/(n+j)!$ and $b_n(t)=\sum_jb_{n,j}t^j$
are the original integral primitive normalized coefficients; these
are not coefficients of an arbitrarily rescaled solution.

Consequently, if


$$
p\nmid M_D^{[k]}(1)\widehat P_{e,k}(1),\qquad
 v_p(n!)>\lfloor\log_p(2n)\rfloor,                    \tag{9}
$$


then the actual reduced denominator satisfies


$$
\boxed{v_p(q_n)=v_p(Z_n)\ge v_p(n!).}                \tag{10}
$$


For fixed $p,k$ meeting the seed condition, the factorial threshold
holds eventually on the whole residue class $n\equiv k\pmod p$.
The argument proves only the displayed prime-level seed congruences;
no lift modulo $p^h$ is asserted here.

## 2. Ordinary Appell reduction and an inflation lemma

For every nonnegative $\ell$, write $\bar\ell=\ell\bmod p$,
with $0\le\bar\ell<p$. If integer backgrounds $b,c$ satisfy
$b\equiv c\pmod p$, then


$$
\boxed{
 \mathcal A_\ell^{[b]}(x)\equiv
 x^{\ell-\bar\ell}\mathcal A_{\bar\ell}^{[c]}(x)
 \pmod p.}                                         \tag{11}
$$


In (1), terms with $2h\ge p$ vanish modulo $p$, because their
falling factorial contains $p$ consecutive integers. A term with
$2h>\ell$ is already zero. For $2h<p$, $h!$ is a unit, so
$\binom bh\equiv\binom ch$ and


$$
(\ell)_{\underline{2h}}\equiv
(\bar\ell)_{\underline{2h}}
$$

. If $2h>\bar\ell$ the latter
vanishes. The remaining terms give (11), with a nonnegative
factor $x^{\ell-\bar\ell}$. All coefficients being reduced are
integers before reduction.

Let $\lambda$ have length $r$, and use its increasing degree set


$$
d_i=\lambda_{r-i}+i,\qquad 0\le i<r.
$$


Jacobi--Trudi and 

$$
H_\lambda=\prod_i d_i!/
\prod_{i<j}(d_j-d_i)
$$

 give


$$
M_\lambda^{[b]}(x)=
 \frac{\det\bigl((\mathcal A_{d_i}^{[b]})^{(j)}(x)\bigr)
              _{0\le i,j<r}}
      {\prod_{i<j}(d_j-d_i)}.                        \tag{12}
$$


The orientation is fixed by increasing degrees and increasing derivative
orders. The leading determinant is the Vandermonde, so the quotient
is monic, with no additional sign.

Assume $d_{r-1}<p$, and enlarge the first row of $\lambda$ by
$\Delta\ge0$, where $p\mid\Delta$. The largest degree becomes
$d_{r-1}+\Delta$, and all other degrees stay fixed. Both
Vandermondes are $p$-units, and they are congruent. Equation (11)
makes the changed Appell polynomial
$x^\Delta\mathcal A_{d_{r-1}}^{[c]}$ modulo $p$;
the others become their background-$c$ polynomials. Since
$(x^\Delta)'=0$ in $\mathbb F_p[x]$, every derivative of the
changed row retains the common factor $x^\Delta$. Thus


$$
\boxed{
 M_{\lambda+\Delta e_1}^{[b]}(x)
 \equiv x^\Delta M_\lambda^{[c]}(x)\pmod p,
 \qquad b\equiv c\pmod p.}                           \tag{13}
$$


Only the maximum degree, not the partition's size, is required to
be less than $p$. In particular no denominator associated with
the potentially very large group size is inverted in this step.
The lemma works unchanged for negative integer $c$.

## 3. Same-size content comparison for the full determinant

Write $n=up+k$, $u\ge0$. In the rectangle of width $n$ and
height $n+1$, split the column residues into $u$ full blocks
plus $k$ residues, and the row residues into $u$ full blocks
plus $k+1$ residues. The content multiset modulo $p$ consists of


$$
pu^2+u(2k+1)
$$


copies of every residue, together with the contents of
$\lambda_D^{[k]}=(k^{k+1})$.

Put $N=n(n+1)$, $\Delta=N-k(k+1)$. For $k\ge1$, enlarge the
first row of that small rectangle by $\Delta$, giving


$$
\mu=(N-k^2,k^k).
 \tag{14}
$$


The number $\Delta$ is a nonnegative multiple of $p$.
The added row segment contains exactly $\Delta/p$ copies of
each residue, so $\mu$ and the actual large rectangle have
the same content multiset modulo $p$ and the same size $N$.
The reviewed integral central-character lemma therefore gives


$$
M_D^{[n]}\equiv M_\mu^{[n]}\pmod p.                  \tag{15}
$$



The small degree set is $\{k,k+1,\ldots,2k\}$.
The enlarged degree set is


$$
\{k,k+1,\ldots,2k-1,L\},\qquad
 L=N-k(k-1)\equiv2k\pmod p.
 \tag{16}
$$


The bound $2k<p$ makes its Vandermonde a unit.
The inflation lemma with background representative $k$ now
proves (3).

If $k=0$, the actual rectangle's content multiset is uniform.
Compare it to the same-size row partition $(N)$, whose contents
are also uniform, and apply (11) with $N\equiv0\pmod p$.
The result is $x^N$, proving (3) with convention (5).
No first row of an empty partition is informally enlarged.

## 4. The cofactor comparison, including its boundary cases

Let $j=vp+a$, with $0\le a\le k$. The square $(n^n)$
has $pu^2+2uk$ uniform content copies, plus the square
$(k^k)$. Its extra $j$ boxes in column $n+1$ have
residues $k,k-1,\ldots,k+1-j$: $v$ uniform blocks,
followed by precisely the $a$ extra contents in


$$
\lambda_a^{[k]}=((k+1)^a,k^{k-a}).
 \tag{17}
$$


Set $\Delta_j=n^2+j-k^2-a$, a nonnegative multiple of $p$.
Enlarging the first row of (17) by $\Delta_j$ therefore gives a
same-size partition with exactly the actual cofactor's content
multiset modulo $p$. The integral content lemma applies.

For $k\ge1$ its small degree set is


$$
\{k,k+1,\ldots,2k\}\setminus\{2k-a\}.               \tag{18}
$$


For $a=0$, its maximum is $2k-1$; for $a\ge1$, its
maximum is $2k$. In all cases the largest degree is below $p$,
and first-row enlargement changes only that degree by $\Delta_j$.
The inflation lemma proves (4). This includes $a=k$, where
the omitted degree is $k$, and $k=1$, where the Wronskian
has just one row and an empty Vandermonde.

For $k=0,a=0$, all actual cofactor contents are uniform.
The same-size single row $(n^2+j)$ is the comparison partition,
and (11) gives $x^{n^2+j}$, again agreeing with (4)--(5).

## 5. Actual primitive coefficients and Lucas factorization

The exact reviewed cofactor formula is


$$
b_{n,j}=(-1)^{n-j}\binom nj V_n(1)
          \frac{M_{n-j}^{[n]}(1)}{M_D^{[n]}(1)},\qquad
 b_{n,j}\in\mathbb Z,\quad \gcd_j b_{n,j}=1.
 \tag{19}
$$


If $p\nmid M_D^{[k]}(1)$, equation (3) makes the denominator
in (19) a unit. If $V_n(1)$ were divisible by $p$, every
primitive $b_{n,j}$ would be divisible by $p$. Thus $V_n(1)$
is a unit. The same argument at the seed degree $k$ proves the
unit claim for $V_k(1)$; the $k=0$ convention is already one.

Write $j=vp+s$. If $s>k$, Lucas makes $\binom nj$ zero
modulo $p$; no assertion about its cofactor is needed, since
that cofactor is integral and the denominator is a unit. For
$s\le k$, the index $n-j$ has residue $k-s$, and (4) applies.
The remaining coefficient factors are


$$
\binom nj\equiv\binom uv\binom ks,\qquad
 (-1)^{n-j}=(-1)^{u-v}(-1)^{k-s}\quad(p\ {\rm odd}).
 \tag{20}
$$


Summing gives the polynomial product


$$
b_n(t)\equiv \frac{V_n(1)}{V_k(1)}
 \left[\sum_v(-1)^{u-v}\binom uv t^{pv}\right]b_k(t)
 =c(t-1)^{up}b_k(t),
$$


which is (6). All denominators used here are established units.

## 6. Exact differential identity and the V transfer

The original polynomials satisfy


$$
W=t^n(t-1)^nV,\qquad S=(1+t^2)^nU,\qquad
 w_\ell=S_\ell/(\ell-n)!\quad(\ell\ge n).
 \tag{21}
$$


The last identity, including its factorial, is equation (2) of the
reviewed raw_joint_dual_hankel_and_even_root_product.md.
The exact differential identity below is also proved in root's
raw_factorial_b_exact_differential_identity.md, independently reviewed
in raw_factorial_b_differential_independent_review.md.
Since $U_j=(n+j)!b_{n,j}$, direct coefficient comparison proves
the exact integer-polynomial identity


$$
\boxed{(t-1)^nV_n(t)
        =(1+\partial_t^2)^n[t^n b_n(t)].}             \tag{22}
$$


Indeed the coefficient of $t^\ell$ on the left is


$$
w_{n+\ell}
 =\frac1{\ell!}\sum_h\binom nh U_{n+\ell-2h}.
$$


On the right it is
$\ell!^{-1}\sum_h\binom nh U_{\ell-n+2h}$.
Replacing $h$ by $n-h$ makes these sums identical, with
coefficients outside the actual range taken as zero. This derivation
does not confuse the two different raw Rodrigues derivatives.

Over $\mathbb F_p[t]$, $\partial_t^p=0$, because a derivative
of order $p$ of every monomial vanishes. Therefore


$$
(1+\partial_t^2)^n=(1+\partial_t^2)^k.
$$


Using (6),


$$
t^n b_n(t)\equiv
 c[t(t-1)]^{up}t^k b_k(t).
$$


The factor $[t(t-1)]^{up}$ has zero derivative, so (22) at the
two degrees gives


$$
(t-1)^nV_n(t)
 \equiv c\,t^{up}(t-1)^nV_k(t).
$$


Cancellation of the nonzero polynomial $(t-1)^n$ in
$\mathbb F_p[t]$ proves (7). No evaluation at $t=1$ is used
to justify this cancellation.

## 7. Exponential endpoint and actual denominator criterion

The original integer border is


$$
\widehat P_{e,n}(1)=\sum_{r=0}^nV_{n,r}D_{n,r},\qquad
 D_{n,r}=\sum_{j=0}^{n+r}\binom{n+j}j(n+r)_{\underline j}.
 \tag{23}
$$


For $r=n-k+s=up+s$, $0\le s\le k$,


$$
\boxed{D_{n,up+s}\equiv D_{k,s}\pmod p.}             \tag{24}
$$


Terms with $j\ge p$ vanish through the falling factorial.
For $j<p$, its denominator $j!$ is a unit, and the two
factors reduce to
$\binom{k+j}j$ and $(k+s)_{\underline j}$.
Because $k+s\le2k<p$, terms with $j>k+s$ vanish and the
surviving sum is exactly $D_{k,s}$. Substituting (7) into (23)
therefore proves (8), with the original common orientation intact.

Finally, the globally reviewed $n!\mid\operatorname{cont}\widehat Q_n$
implies


$$
v_p(\widehat P_{a,n}(1))
 \ge v_p(n!)-\lfloor\log_p(2n)\rfloor.
$$


Under (9), equation (8) makes the exponential endpoint a unit,
and this arctangent term has positive valuation. As $p$ is odd,
the actual numerator $N_n=\widehat P_{e,n}(1)+4\widehat P_{a,n}(1)$
is a unit. Reducing $N_n/Z_n$, rather than a different cofactor
pair, gives (10).

The boundary seeds match previously proved cases:
$k=0$ gives the prime-dividing-degree unit, while $k=1$ has
$M_D^{[1]}(1)=-1$, $V_1(t)=2-t$,
$\widehat P_{e,1}(1)=-5$. Thus this general prime-level theorem
recovers the genuine exceptional prime five on $n\equiv1\pmod p$.
It makes no claim to remove an exceptional seed prime or to give
higher-depth control there.
