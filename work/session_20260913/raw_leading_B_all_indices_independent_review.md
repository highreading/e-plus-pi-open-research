> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent verification of all-degree leading-B nonvanishing

Date: 2026-09-13. Reviewed `raw_leading_B_dyadic_all_indices.md`, its
two preceding partial notes, and the original determinant convention.
The all-index theorem passes. The verification below supplies a
shorter alternative proof of the uniform interpolation divisibility
and independently reconstructs the critical moment determinants.
No new degree sample or HP construction is used.

## 1. Verified conclusion and exact scope

For the actual canonical raw family normalized by B_n(1)=1,C_n(1)=4,
the leading coefficient is nonzero in every degree n>=1, with



$$
v_2(B_{n,n})=
\begin{cases}
3,&n=1,\\
v_2(n-1),&n\ge5,\ n\equiv1\pmod4,\\
0,&\text{otherwise}.
\end{cases}
$$



The first and last cases are the previously audited results. The new
argument closes the remaining class. Its determinant is the one
appending the coordinate row B_(n,n), with no extra factorial, and
the final quotient is by the actual B(1) determinant. It establishes
no Archimedean lower bound, signed modal noncancellation, or nonzero
cross-minor Xi by itself.

## 2. Interpolation coordinates and integrality

Let n>=5,n=1 mod4, a=v_2(n-1)>=2, and c=2n+1. Lower high rows are
indexed c-d, 1<=d<=n, while the top block has nodes c+i,
0<=i<=n-1. Interpolation in the monic falling-factorial basis gives
exactly



$$
M_{d,i}=(-1)^i\frac{(c+i)!}{(c-d)!}
\frac{(d)_{\overline n}}{(d+i)i!(n-1-i)!}.
$$



The unsigned cardinal factor equals
$\binom{d+i-1}{i}\binom{d+n-1}{n-1-i}$, so every entry is an
integer. The factorial ratio is also an integer: all its arguments
are positive in the stated ranges. This integrality is needed for
the subsequent minor divisibility and is explicitly proved.

I checked the source's split proof at k=i+1=2^a, both exact row
ratios, and the bound for the entire range k>2^a. All are correct.
Here is an independent argument avoiding that split.

## 3. Short alternative proof of the uniform divisibility

Put F_(d,i)=(c+i)!/(c-d)!. It is a product of d+i consecutive
integers, so v_2(F_(d,i))>=v_2((d+i)!).

For d>=4 the product contains both 2n-2 and2n. Their valuations are
a+1 and1, respectively. Hence every such row is divisible by2^(a+2).

For d=1,2,3 and i>=1, let C_i=binom(n-2,i-1), an integer throughout
the entire index range. The three cardinal factors, ignoring sign,
are exactly



$$
L_{1,i}=\frac{n(n-1)}{i(i+1)}C_i,
$$




$$
L_{2,i}=\frac{(n+1)n(n-1)}{i(i+2)}C_i,
$$




$$
L_{3,i}=\frac{(n+2)(n+1)n(n-1)}{2i(i+3)}C_i.
\tag{A}
$$



Since n and n+2 are odd and v_2(n+1)=1, these give lower bounds
a-v_2(i)-v_2(i+1), a+1-v_2(i)-v_2(i+2), and
a-v_2(i)-v_2(i+3), respectively.

For d=1 and i>=3, the factorial (i+1)! contains i, i+1, and the
even factor in (i-1)!, so it supplies at least
1+v_2(i)+v_2(i+1). At i=1 or2, F_(1,i) itself contains c+1=2n+2,
of valuation2, which supplies the same required bound. Thus every
first-row entry with i>=1 has valuation at least a+1.

For d=2, (i+2)! contains the two distinct factors i and i+2, so it
supplies at least v_2(i)+v_2(i+2). For d=3, (i+3)! contains i and
i+3 and also an even member of the intervening pair i+1,i+2. It
supplies at least1+v_2(i)+v_2(i+3). Combining with (A) proves
valuation at least a+1 in both remaining rows, uniformly up to i=n-1.

This independently proves the two suppression assertions. Directly
at i=0 the three unsuppressed entries are



$$
M_{1,0}=n(2n+1),\quad
M_{2,0}=n^2(n+1)(2n+1),
$$




$$
M_{3,0}=\frac{n^2(n+1)(n+2)(2n-1)(2n+1)}3,
$$



with valuations0,1,1. The denominator3 is a dyadic unit and the
displayed expression is an integer.

## 4. Every row-exchange determinant is covered

Any size-n exponential high-row minor is obtained from the top
consecutive block by replacing a set I of its rows with an equally
large set of lower rows. After normalizing by the top block, its
determinant ratio is, up to sign, the square minor M_(D,I). If at
least two rows are replaced, distinctness of the deleted columns
forces at least one i>=1. Factoring2^(a+1) from that entire column
and using integrality of all other entries suppresses the minor to
the required precision. This argument includes all multiple
exchanges, regardless of their factorial-sum loss.

For a single exchange, only column0 and rows d=1,2,3 can survive.
Thus the full classification contains the original row set and
exactly three exchanges. No unenumerated family can contribute
below the claimed error modulus. Complementary C minors have
valuation at least L_n, while the reference C minor has exactly
L_n, so their ratios cannot remove any of this divisibility.

## 5. Independent three-by-three and four-by-four C blocks

Let q_j=Q_j(1) for the raw monic orthogonal polynomials, not the
accessory cubic, and beta_j=j²/(4j²-1). Their norms satisfy
h_j/h_(j-1)=-beta_j. Set s_j=j(j-1)/(2(2j-1)).

For the d=2 exchange, after eliminating the common lowest moments,
the remaining block in columns Q_(n-2),Q_(n-1),Q_n is



$$
\begin{pmatrix}
0&h_{n-1}&0\\
-s_nh_{n-2}&0&h_n\\
q_{n-2}&q_{n-1}&q_n
\end{pmatrix}.
$$



Dividing its determinant by h_(n-2)h_(n-1)q_n gives
s_n+beta_n beta_(n-1)q_(n-2)/q_n, with the positive sign stated in
the source note.

For d=3 the last four columns start at Q_(n-3). The three moment
rows and final evaluation row are



$$
\begin{pmatrix}
0&h_{n-2}&0&0\\
-s_{n-1}h_{n-3}&0&h_{n-1}&0\\
0&-s_nh_{n-2}&0&h_n\\
q_{n-3}&q_{n-2}&q_{n-1}&q_n
\end{pmatrix}.
$$



Its normalized determinant is
beta_n[s_(n-1)q_(n-1)+beta_(n-1)beta_(n-2)q_(n-3)]/q_n.
The s_n entry disappears in the elimination; replacing s_(n-1) by
s_n in the final expression would be incorrect. The source retains
the right coefficient and sign.

Writing n=4r+1, the earlier Cauchy equality cases give
v_2(q_n)=v_2(q_(n-1))=v_2(q_(n-3))=2r and
v_2(q_(n-2))>=2r+1. In particular the n-3 index is even of the
class4r-2, whose exact endpoint valuation is2r. Therefore each
displayed C ratio has a unique term of valuation a-1; the other
term is at least2a+1 or2a. Multiplication by its exponential factor
of valuation1 gives exactly a in both cases.

## 6. Three units, the other border, and conclusion

The independently audited sum of the original and d=1 exchange
terms has valuation baseline+a. Each of the d=2 and d=3 terms has
that valuation as well. After dividing by2^(baseline+a), the three
contributions are units and hence each has residue1 modulo2.
Their sum is1, irrespective of their signs. All other C-border
terms are zero modulo2 at this scale by Section4. There is no
remaining equal-valuation cancellation to check.

The other border assignment has gap
(n+5)/2+2v_2(n!) above the baseline. Since n-1>=2^a>=2a, this is
strictly larger than a. It cannot change the leading residue.
Restoring precisely the high-row factorials and dividing by the
separate actual Delta_B proves v_2(B_(n,n))=a.

All arguments are valid for the full indicated range n>=5,n=1mod4;
the n=1 exception is handled by its explicit canonical polynomial.
The proof closes the former quarter-class obstruction without
assuming a finite residue scan extends to all indices.

## 7. Symbolic verification

`check_raw_leading_B_interpolation_symbolic.py` checks the two exact
row-ratio identities, the first-row binomial form, both displayed
moment-block determinants, and the tied-pair polynomial factorization
with symbolic variables. All pass. The certificate is
`raw_leading_B_interpolation_symbolic_checks.json`. No new degree
sample is used; the earlier saved-data checks remain consistent.
