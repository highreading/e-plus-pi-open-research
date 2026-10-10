> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A contiguous extremal-content inequality at full prime-power depth

Date: 2026-09-13. Original bounded arithmetic continuation by audit_results.
Independent audit: raw_contiguous_extremal_content_independent_review.md
passes the full-depth argument and localized gcd identity.

This note proves a new neighboring-degree relation for the actual
extremal contents. With the notation below, for every N>=2 and
every prime p>3N,



$$
\boxed{
\min\{v_p(F_{N-1}),v_p(F_N)\}
\le v_p(D_{N-1})\le v_p(F_{N-1}).}
\tag{1}
$$



The right inequality is the previously reviewed high-to-extremal
content theorem. The left inequality is new and keeps all prime-power
exponents. Equivalently, in Z[1/(3N)!],



$$
\boxed{\gcd(F_{N-1},F_N)\mid D_{N-1}.}
\tag{2}
$$



This is an actual contiguous determinantal-content relation, not a
recurrence for individual matrix entries. It does not prove saturation
of any one F_N or give a reverse inequality. No degree or prime scan
is used.

There is also an exact gcd identity in that same localization:



$$
\boxed{
\gcd(F_{N-1},F_N)=\gcd(D_{N-1},F_N)
\quad\text{up to units in }\mathbb Z[1/(3N)!].}
\tag{2a}
$$



Indeed (1) and e<=f imply min(f,g)=min(e,g) at each such
prime. This equality identifies the entire common large-prime
content, including its multiplicities, with the preceding high
content's contribution.

## 1. Actual matrices and reviewed inputs

For r>=1 let H_r have rows k=r+1,...,3r and B,C coefficient
columns of degrees at most r. Let X_r have rows k=r,...,3r and
columns of degrees at most r−1. Their actual integer entries are
(k)_j and k!tau_(k−j), where tau_s=[z^s]arctan(z).
Write D_r,F_r for their respective positive maximal-minor contents.
Characteristic-zero full row rank of H_r and full column rank of
X_r are already proved.

The following exact inputs are retained from the reviewed notes:

1. At p>3r, the degree-at-most-r−1 Taylor solution space at order
   3r+1 has dimension at most1. In matrix terms, X_r loses at
   most one column rank modulo p. Thus it has at most one nonunit
   Smith invariant over Z_p, whose valuation is v_p(F_r).
2. Any nonzero such extremal triple has B_(r−1) nonzero modulo p.
   Its cleared Wronskian numerator is nonzero, has degree at most
   3r−1, and has origin order at least3r−1.
3. More generally the same polynomial numerator has origin order
   at least nu−2 when the remainder has order at least nu, so
   long as the finite Taylor jets used in that assertion are below p.
4. The previous theorem gives v_p(D_r)<=v_p(F_r).

These are in raw_large_prime_nullity_and_smith.md,
raw_large_prime_endpoint_gcd_independent_review.md, and
raw_high_content_extremal_valuation_bound.md. The argument below
uses p>3(r+1), so all jets through degree3r+3 and all their row
factorials are units. The characteristic boundary is consequently
strictly inside the allowed range; no division by p is introduced.

The same finite-difference reductions as before give
v_p(D_r)=v_p(eta_r), v_p(F_r)=v_p(theta_r) at the relevant large
primes. Thus (1) also reads



$$
\min\{v_p(\theta_{N-1}),v_p(\theta_N)\}
\le v_p(\eta_{N-1})\le v_p(\theta_{N-1}),\qquad p>3N.
\tag{3}
$$



## 2. An extremal triple has a unit first omitted remainder coefficient

Fix r>=1 and p>3r+3. Let T=(A,B,C) be a nonzero triple over
F_p with degree at most r−1 and



$$
A+BE_T+CF_T=O(z^{3r+1}),
\tag{4}
$$



where E_T,F_T now mean the actual Taylor jets through degree3r+3.
All these jets are well defined over F_p. The reviewed leading
coefficient identity gives B_(r−1)!=0 and a nonzero cleared
numerator of degree at most3r−1.

Put M=3r+1 and let a_0,a_1 be the remainder coefficients at
degrees M,M+1. Then



$$
\boxed{a_0\ne0\quad\text{in }\mathbb F_p.}
\tag{5}
$$



If a_0 were zero, the same triple would have order at least M+1.
Its numerator would then have order at least M−1=3r, contradicting
its nonzero value and degree at most3r−1. The order assertion uses
the same determinant expression with the remainder column and its
first two derivatives; replacing that column by a remainder of
higher order raises the bound by exactly the needed amount.
The extra jets here are still strictly below p.

Consequently, the first two omitted Taylor rows on the pair T,zT
give the exact matrix



$$
\begin{pmatrix}a_0&0\\a_1&a_0\end{pmatrix},
\tag{6}
$$



whose determinant is a unit. The equations of degree at most r
in these triples, including the low A coefficients, are included
in (4); they are not reconstructed with a larger allowed degree
in this step.

## 3. Primitive approximate kernels at the full Smith depth

For this fixed r,p set



$$
f=v_p(F_r),\qquad g=v_p(F_{r+1}),\qquad e=v_p(D_r).
\tag{7}
$$



Suppose, towards a contradiction, that f>e and g>e. In particular
both f and g are positive. Because X_r has just one nonunit Smith
invariant when f>0, its Smith form supplies an integral primitive
column vector t in its B,C coordinates such that



$$
X_rt\equiv0\pmod{p^f}.
\tag{8}
$$



Likewise X_(r+1) supplies a primitive integral vector s with



$$
X_{r+1}s\equiv0\pmod{p^g}.
\tag{9}
$$



This is an assertion at the full content valuations f and g,
not merely modulo p. It follows by taking the last column of
the invertible Smith column transformation. Its reduction is
nonzero because that column is primitive.

Divide all matrix rows by k!, which are units over Z_p in the
whole range. Denote the unscaled Taylor high matrix by H. Embed
t in the degree-at-most-r B,C coordinates, calling that vector
t_0, and let t_1 denote multiplication of both polynomials by z.
Then



$$
Ht_0,\ Ht_1\in p^f\mathbb Z_p^{2r}.
\tag{10}
$$



For t_0 these are the overlapping rows of X_r. For t_1, row k
is row k−1 of X_r. The latter runs down to k−1=r, exactly the
lowest row of X_r. Omitting that row would invalidate (10).

Modulo p, reconstruct A with degree at most r−1 from t. The
vector is a nonzero extremal triple as in (4), so its coefficient
b=B_(r−1) is a unit. In the two B coordinates r−1,r, the pair
t_0,t_1 has matrix



$$
\begin{pmatrix}b&B_{r-2}\\0&b\end{pmatrix}\pmod p.
\tag{11}
$$



For r=1, B_(−1)=0. Thus this pair has a unit 2-by-2 minor and
extends to an invertible integral coordinate matrix P over Z_p.

## 4. The high content controls the loss in eliminating the other coordinates

Choose P with first two columns t_0,t_1 and complete them by
coordinate columns outside the unit minor in (11). Its determinant
is that unit minor up to sign. In these coordinates (10) says



$$
HP=[\,p^f U\mid A\,],
\tag{12}
$$



where U is integral and A is a square 2r-by-2r integral matrix.
The maximal-minor content of HP still has valuation e. Any
maximal minor using at least one of the first two columns is
divisible by p^f. Since f>e, the unique maximal minor using
neither must have valuation e. Therefore



$$
\boxed{v_p(\det A)=e,
\qquad A^{-1}\in p^{-e}\operatorname{Mat}_{2r}(\mathbb Z_p).}
\tag{13}
$$



The inverse bound is the integral adjugate formula; it does not
assume that A is unimodular or lose an unspecified valuation.

Write the primitive vector from (9) as s=P(c,y), with c in Z_p²
and y in Z_p^(2r). The row set of X_(r+1) is r+1,...,3r+3;
its first2r rows are exactly H, with the same degree-at-most-r
coefficient columns. Hence (9) implies



$$
p^fUc+Ay\in p^g\mathbb Z_p^{2r}.
$$



Let h=min(f,g)>e. Then Ay belongs to p^h Z_p^(2r), and (13)
gives



$$
\boxed{y\in p^{h-e}\mathbb Z_p^{2r}\subset p\mathbb Z_p^{2r}.}
\tag{14}
$$



It follows that, modulo p, the entire degree-at-most-r coefficient
vector s lies in the span of t_0,t_1. Since P is invertible and s
is primitive, the remaining pair c cannot vanish modulo p.

## 5. The next two actual rows give the contradiction

The next two rows of X_(r+1), after H, have degrees
M=3r+1 and M+1=3r+2. They both annihilate s modulo p by (9).
By (14), their values on s are their values on c_0t_0+c_1t_1.
For these high degrees the A polynomial contributes zero.
Therefore their two values are precisely the matrix in (6)
times (c_0,c_1)^T.

Its determinant a_0² is a unit by (5), so c_0=c_1=0 modulo p.
Together with (14), this contradicts primitivity of s. Thus f
and g cannot both exceed e, proving



$$
\min(f,g)\le e.
\tag{15}
$$



The unused final row of X_(r+1), of degree3r+3, is retained in
the matrix and in the primitive-vector hypothesis (9). The proof
needs only its first two new rows for the contradiction; it does
not replace the actual matrix by one with that last row deleted.

Combining (15) with the reviewed e<=f and setting N=r+1 proves
(1)–(3). Because these inequalities hold at every p>3N, they give
the stated divisibility in Z[1/(3N)!]. There is no multiplier
with prime support above3N hidden in that reformulation.

## 6. Exact consequences and limits

The inequality can also be read as



$$
v_p(F_r)>v_p(D_r)
\quad\Longrightarrow\quad
v_p(F_{r+1})\le v_p(D_r),\qquad p>3r+3.
\tag{16}
$$



Thus excess extremal-content depth at one degree cannot persist
at the next degree beyond the intervening high-content depth.
In particular if D_r is a unit at p, the two neighboring extremal
contents cannot both be divisible by p. Conversely, neighboring
extremal defects force an actual unbordered high defect at degree r.

This does not exclude isolated extremal defects, does not bound
their exponent or size, and does not establish equality in (15).
The third additional Taylor row, not needed for the contradiction,
is one reason the argument provides no reverse construction of an
X_(r+1) defect from an H_r defect. The inequality is a constraint
on consecutive actual contents rather than a closed scalar
recurrence determining them from initial values.

The earlier primitive-dual factorization remains compatible:
E_r=(-1)^rF_rZ_r. The new relation concerns the F factors of two
neighboring degrees directly; it is not obtained by comparing
ordinary Legendre entries or assuming their basis changes are
large-prime units. A useful next arithmetic problem is to combine
this contiguous inequality with a bound or coprimality identity
for one of the actual intervening D_r or dual Z_r factors. Such
a further bound has not been proved here.
