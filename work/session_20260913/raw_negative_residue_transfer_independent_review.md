> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the negative-residue endpoint theorem

Date: 2026-09-13. Reviewer: audit_computations.

**FULL PASS after one corrected transcription.** This review covers
all sections of `raw_negative_residue_schur_and_endpoint_seeds.md`.
The author corrected the added-column residue sequence in Section 3:
it starts at $-k-1$, not $-k$. The subsequently used removed
interval $-k,\ldots,i$ and all theorem formulas were already the
ones produced by the corrected sequence, so no conclusion changed.
There are no remaining mathematical corrections.

The proof is uniform in the arbitrary prime-block count $a$.
The fixed symbolic seeds are only $k=1,2$, as predeclared; no new
canonical degree or prime scan was used. I independently reconstructed
their small arithmetic and also reran their exact symbolic checker.

## 1. Integral specialization and the inflation step

For negative integer background $b=-k-1$, all generalized binomial
coefficients $\binom bh$ are integers. The ordinary Appell
polynomials therefore have integral coefficients. In their reduction
modulo $p$, falling factorials of length at least $p$ vanish.
For length $2h<p$, the denominator $h!$ is a unit, so the
background can be reduced modulo $p$. This proves the stated
ordinary Appell reduction for negative as well as positive background.

The normalized Wronskian identity follows from Jacobi–Trudi and the
hook product. Increasing degrees fix its sign, and dividing by the
degree Vandermonde makes it monic. If the original maximum degree is
less than $p$, enlarging the first row by a multiple of $p$
keeps this Vandermonde a congruent unit. The changed Appell row acquires
a common factor $x^\Delta$, whose positive derivatives vanish
modulo $p$. Thus the inflation lemma applies exactly as in the
independently reviewed positive-residue theorem.

The integral central-character comparison is applied only to partitions
of the same size. The power-sum specialization is integral, including
its negative even values. There is no division by a large group-size
factorial and no change of complete-function convention hidden in the
negative background.

## 2. Full determinant and corrected cofactor content count

Write $n=ap-k-1$, $p>2k+1$, and
$B=a^2p-a(2k+1)$. Start with the $ap$-square, whose content
multiset consists of $a^2p$ copies of each residue. Removing the
last $k$ rows and $k+1$ columns subtracts
$a(2k+1)$ uniform copies. The overlap has contents
$u-v-1$, $0\le u\le k$, $0\le v<k$, which the given
bijection identifies with the contents of $(k^{k+1})$.
Thus the claimed multiset equality is exact. Its size is
$k(k+1)+pB=n(n+1)$, and $B>0$ under the stated hypothesis.
The same-size comparison and inflation have small degrees
$k,\ldots,2k<p$, proving (15).

For a surviving coefficient index $l=vp+i$, the actual cofactor
index is $j=n-l=(a-v)p-(k+1+i)$. The added boxes have contents
$n,n-1,\ldots,n-j+1$, hence residues



$$
-k-1,-k-2,\ldots,-k-j.
$$



Completing this list to $(a-v)p$ terms leaves a missing final list
$i,i-1,\ldots,-k$. This proves that the omitted interval is
exactly $-k,\ldots,i$. In the residual $(k+1)$-square, it is
the bottom row, with contents $-k,\ldots,0$, together with the
$i$ adjacent boxes above it in the rightmost column, with contents
$1,\ldots,i$. Removing it leaves
$\gamma_i=((k+1)^{k-i},k^i)$.

The uniform multiplicity becomes $B-v$, and the size is
$k(k+1)-i+p(B-v)=n(n+1)-l$. It is nonnegative throughout
$0\le v\le a-1$; for example
$B-(a-1)=a(ap-2k-2)+1>0$. The small degree set is precisely
$\{k,\ldots,2k\}\setminus\{k+i\}$, including both endpoints
$i=0,k$. Its maximum is less than $p$, so the same-size
comparison and inflation prove (18).

The corrected sequence is essential for this count, but the displayed
seed shapes and all later formulas are unchanged by the correction.

## 3. Primitive normalization is local only at the full determinant

The original primitive coefficient formula is



$$
b_{n,l}=(-1)^{n-l}\binom nl V_n(1)
       \frac{M_{n-l}^{[n]}(1)}{M_D^{[n]}(1)}.
$$



When $p\nmid D$, the full determinant is a unit by (15). Every
cofactor is integral. Therefore a positive valuation of $V_n(1)$
would divide every integral primitive coefficient $b_{n,l}$, a
contradiction. This proves the endpoint unit without requiring any
individual cofactor to be a unit. Restriction to the coefficient
residues in (16) then gives equation (20), with its original sign and
factorial normalization intact.

## 4. Derivative extraction and Lucas elimination for arbitrary a

The exact upper-tail identities (21)–(22) are correct. For (21),
the generating functions
$t^h/(1-t)^{h+1}$ and $(1-t)^{-n}$ give the coefficient
$\binom{n+l}{n+h}$. Thus this identity concerns
$V^{(h)}(1)/h!$, with the factor $h!$ restored in $J_{k,h}$.
For (22), extracting $S_{2n+l}$ in $(1+t^2)^nU$ and using
$S_{2n+l}=(n+l)!w_{2n+l}$ gives exactly the stated rising
factorial and positive binomial coefficient.

Put $r=p-k-1$, so $n=(a-1)p+r$. For $0\le h\le k$,
the low digit of $n+h$ is $r+h<p$. If
$l=vp+i$ with $i<h$, the numerator's low digit is too small.
If $i\ge k+1$, it carries and becomes $i-k-1<r+h$. Thus the
only survivors are $h\le i\le k$, as claimed. On them,



$$
\binom{n+l}{n+h}
 \equiv\binom{a+v-1}{a-1}\binom{r+i}{r+h}\pmod p.
$$



This is the first-digit Lucas factorization and is valid for arbitrary
large high digits. It does not require $a<p$. Since $k<r$,
all $v=0,\ldots,a-1$ occur in the actual index range for every
surviving $i$.

In the rising factorial in (22), the first multiple of $p$ occurs
in position $k-i+1$. Hence only $2u\le k-i$ can survive.
The input $l+2u$ still has residue at most $k$, so equation
(20) is available for every term that remains. Its Lucas and sign
factors are exactly



$$
\binom n{l+2u}\equiv\binom{a-1}v\binom r{i+2u},
 \quad
 (-1)^{n-l-2u}=(-1)^{a-1-v}(-1)^{k-i}.
$$



The parity equality follows from odd $p$ and
$r=p-k-1\equiv k\pmod2$. None of the surviving upper-tail
indices exceed $n$.

The entire high-digit dependence is the exact integer sum



$$
\sum_{v=0}^{a-1}(-1)^{a-1-v}
 \binom{a-1}v\binom{a+v-1}{a-1}=1.
$$



It is a finite-difference identity over the rationals whose value is
the integer one; equivalently it follows from generalized Vandermonde.
It is established before reducing modulo $p$, so the possible
divisibility of $(a-1)!$ introduces no modular division. This is
the crucial reason the theorem is uniform in an arbitrary number of
prime blocks.

All remaining binomial bottom indices are at most $k<p$.
Replacing $r$ and $n$ by $b=-k-1$ in those factors is
therefore legitimate. The remaining expression is exactly (3),
including its sign $(-1)^{k-i}$, rising factorial, and outer
factor $h!$. This proves the derivative congruence (6).

## 5. The actual endpoint is a finite derivative functional

In the integer border (26), every term with $s\ge p$ vanishes
through its falling factorial. For $s<p$, the factorial denominator
is a unit, and



$$
\binom{n+s}s\equiv\binom{-k-1+s}s
 =(-1)^s\binom ks\pmod p.
$$



The equality also explains the zero terms $k<s<p$, when the
nonnegative top on the left is smaller than its bottom. Consequently
the border has degree at most $k$ in the coefficient index. The
falling-factorial Vandermonde identity expands it in
$r_{\underline h}$, whose pairing with the actual coefficient
vector is $V_n^{(h)}(1)$. This gives precisely the coefficients
$A_{k,h}$, the sum $\mathcal E_k^-$, and equation (7).

The signs in this step use the actual positive orientation of
$\widehat P_e(1)$. There is no exterior factor $(-1)^n$.
Combining the two seed units with the factorial/Taylor bound makes
the actual numerator $\widehat P_e(1)+4\widehat P_a(1)$ a unit.
The gcd reduction of this numerator over $Z_n$ gives (9).
If a seed is zero, the source correctly stops at the corresponding
weaker statement; it does not infer an endpoint gcd or a small actual
denominator from a zero seed.

## 6. Independent fixed-seed reconstruction

For $k=1$, background $-2$ gives
$\mathcal A_1=x$, $\mathcal A_2=x^2-4$. The normalized
Wronskian is $D_1^-=x^2+4$, and the two cofactors are
$x^2-4,x$. Direct substitution gives
$J=(5,-2)$, $A=(3,-1)$, and $\mathcal E_1^-=17$.

For $k=2$, background $-3$ gives



$$
\mathcal A_2=x^2-6,\quad
 \mathcal A_3=x^3-18x,\quad
 \mathcal A_4=x^4-36x^2+144.
$$



Their three-row Wronskian divided by two is the displayed
$D_2^-$. The two-row Wronskians, with differences one, two, one
in their degree normalizations, give exactly the three displayed
cofactor polynomials. At one their values are
$D=-845$, $C=(2791,61,109)$.

An explicit reconstruction of the inner sums in (3) gives
$(-1133,-183,654)$. The outer binomial sums then give



$$
J_0=-1133-366+654=-845,
 \quad J_1=183-654=-471,
 \quad J_2=2\cdot654=1308.
$$



The endpoint coefficients are $(19,-8,1)$, so
$19(-845)-8(-471)+1308=-10979$. This independently checks
all derivative and endpoint normalization factors. Both seeds satisfy
the necessary zeroth-derivative identity $J_0=D$.

The existing exact symbolic checker was rerun and all of its polynomial
and integer checks passed. It examines only these two fixed partitions,
not actual growing Hermite–Padé systems. No new degree range or
factorization was introduced.

## 7. Uniform seventh-adic consequence and scope

Modulo seven, the first negative seed has
$(D,\mathcal E)=(5,3)$, and the second has $(2,4)$. Both
ratios are two, so the theorem supplies the missing residues five and
four, respectively. The reviewed positive seeds cover residues
$0,1,2,3$, and the reviewed $n+1$ theorem covers residue six.
Thus the exponential endpoint is a seventh-adic unit at every index
in all seven residue classes, with no condition on the number of
prime blocks.

There is an explicit sufficient common threshold for the actual
denominator conclusion. If $n\ge14$, put
$m=\lfloor n/7\rfloor\ge2$. Then
$2n\le14m+12<7^m$; the last inequality holds at $m=2$ and
persists by induction. Hence
$v_7(n!)\ge m>\lfloor\log_7(2n)\rfloor$. Combining the seven
unit cases gives



$$
\boxed{v_7(q_n)=v_7(Z_n)\ge v_7(n!)\qquad(n\ge14).}
$$



This is a uniform fixed-prime denominator theorem, not a claim about
all prime-power lifts or the final irrationality objective. The source's
exceptional determinant and endpoint seeds remain genuine obstructions
to applying its unit argument at the corresponding primes.
