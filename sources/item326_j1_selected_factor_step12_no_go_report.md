> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 326 — actual selected factors, the exact four-phase step-12 recurrence, and a bounded-gap overlap no-go

Date: 2026-09-01

## 1. Outcome and capacity first

Item 324 shows that the actual fixed-$M$ gate selects one constant parity
$\epsilon_M$; the unused parity is not available.  This item therefore
works only with the two genuine Item-321 factors of that selected container,
with their actual Item-308 initial values.

For every fixed phase $r=s\bmod4$, parity $\epsilon$, and sign
$\sigma\in\{+,-\}$, define the all-index scalar solution



$$
Y^\sigma_{r,\epsilon}(n)
 =A_n+\sigma i\bigl(\alpha_{r,\epsilon}Z_n+
                         \beta_{r,\epsilon}\overline Z_n\bigr).       \tag{1.1}
$$



On the matching phase $n\equiv r\pmod4$, Item 321's factorization is



$$
{D_{n,\epsilon}\over9\,2^{27n+21}}
 =Y^+_{r,\epsilon}(n)Y^-_{r,\epsilon}(n).                \tag{1.2}
$$



This item proves a single exact determinant recurrence, independent of
$(r,\epsilon,\sigma)$,



$$
\boxed{\sum_{j=0}^3\Delta_j(s)
 Y^\sigma_{r,\epsilon}(s+12j)=0,\qquad \Delta_j(s)\in\mathbb Q(s),}    \tag{1.3}
$$



and proves that every $\Delta_j(s)$ is nonzero for every integer
$s\geq1$.  The recurrence is derived from the true Item-317 companion
matrix, and all 16 factor sequences are pinned by the true Item-308 values
at indices $1,2,3$; no free or abstract state is introduced.

The fixed-$M$ capacity audit is nevertheless negative.  Consecutive rows
have



$$
s\mapsto s+3,qquad p\mapsto p+2,qquad h\mapsto h-4,                  \tag{1.4}
$$



so one step-12 phase window sees candidate-prime gaps $0,8,16,24$.
For every fixed nonzero gap, the standard two-dimensional upper-bound sieve
gives weighted prime-pair mass $O(M/\log M)=o(M)$.  Thus a cross-row gcd
or resultant whose hypotheses require selected collisions at two
bounded-offset actual rows can touch only zero-rate overlap.  It does not
control isolated rows, which retain the full raw first-order candidate mass
$M/6+o(M)$.

No theorem forcing every original collision to propagate to another prime
row is proved.  Consequently



$$
\boxed{\text{new linear log rate}=0,\qquad
        \text{new fixed-}j=1\text{ capacity reduction}=0.}            \tag{1.5}
$$



The fixed-$j=1$ ceiling remains $1/36$ per $6M$.

## 2. The actual selected factor sequences

Retain



$$
Z_n=(-2(1+i))^nB_n.                                      \tag{2.1}
$$



The coefficient table in (1.1) is



$$
\begin{array}{c|c|cc}
r&\epsilon&\alpha_{r,\epsilon}&\beta_{r,\epsilon}\\ \hline
0&0&\sqrt2&\sqrt2\\
0&1&\sqrt2&-\sqrt2\\
1&0&1+i&-1+i\\
1&1&1+i&1-i\\
2&0&\sqrt2&-\sqrt2\\
2&1&\sqrt2&\sqrt2\\
3&0&1+i&1-i\\
3&1&1+i&-1+i.
\end{array}                                                \tag{2.2}
$$



Exact multiplication, reduced only by $(\sqrt2)^2=2$, gives (1.2) in
all eight rows.  The coefficient field is



$$
L=\mathbb Q(i,\sqrt2).             \tag{2.3}
$$



Every actual prime is at least 13, while the field discriminants and all
discarded denominator factors are supported at 2 and 3.  Hence reduction
at a prime of $L$ above an actual $p$ is legitimate.  If the selected
container vanishes, one of the two factors in (1.2) vanishes at that prime
of $L$.  The sign and prime above $p$ need not be constant across rows;
both signs are retained throughout.

The factor solutions are not initialized formally.  The exact starting
rows are the Item-308/321 values



$$
\begin{array}{c|ccc}
n&A_n&Z_n&\overline Z_n\\ \hline
1&-11&-91/8+(33/4)i&-91/8-(33/4)i\\[1mm]
2&6517/8&-28357/256-(55363/256)i&-28357/256+(55363/256)i\\[1mm]
3&-103389/128&13678665/4096-(9202479/8192)i&
                  13678665/4096+(9202479/8192)i.
\end{array}                                                \tag{2.4}
$$



Substitution of (2.4) into (1.1) gives the exact initial triple of each of
the 16 sequences.  The replay recomputes and hashes all 16 triples; it does
not substitute a generic solution state.

## 3. Exact determinant construction of the step-12 recurrence

Let $P_0(s),\ldots,P_3(s)$ be the exact Item-317 operator coefficients,
so every sequence in (1.1) satisfies



$$
\sum_{k=0}^3P_k(s)y_{s+k}=0.             \tag{3.1}
$$



Write the scalar state as $(y_s,y_{s+1},y_{s+2})^T$ and put



$$
T_s=
 \begin{pmatrix}
 0&1&0\\0&0&1\\
 -P_0(s)/P_3(s)&-P_1(s)/P_3(s)&-P_2(s)/P_3(s)
 \end{pmatrix}.                                           \tag{3.2}
$$



With $e_0^T=(1,0,0)$, define four rows over $\mathbb Q(s)$:



$$
R_0(s)=e_0^T,qquad
 R_j(s)=e_0^TT_{s+12j-1}\cdots T_s,\quad 1\leq j\leq3.   \tag{3.3}
$$



For $0\leq j\leq3$, let



$$
\Delta_j(s)=(-1)^j
 \det\bigl(R_0(s),\ldots,\widehat{R_j(s)},\ldots,R_3(s)\bigr).        \tag{3.4}
$$



Laplace expansion of the $4$-by-$3$ row matrix gives the exact vector
identity



$$
\sum_{j=0}^3\Delta_j(s)R_j(s)=0. \tag{3.5}
$$



Applying (3.5) to the actual state at index $s$ proves (1.3) for every
factor solution.  This is an all-index linear-algebra identity, not a
recurrence fitted to a finite value list.

The exact fraction-field computation produces the following reduced
degrees and signs:



$$
\begin{array}{c|cc|cc}
j&\deg\operatorname{num}\Delta_j&
  \deg\operatorname{den}\Delta_j&
  \text{numerator coefficients}&\text{denominator coefficients}\\ \hline
0&117&117&\text{all positive}&\text{all nonnegative}\\
1&116&116&\text{all negative}&\text{all positive}\\
2& 92& 92&\text{all negative}&\text{all positive}\\
3& 68& 68&\text{all negative}&\text{all positive}.
\end{array}                                                \tag{3.6}
$$



The only zero coefficient in (3.6) is the constant coefficient of the
first denominator.  Therefore every numerator and denominator is nonzero
at every integer $s\geq1$.  In particular, the universal sampled
solution space has exact order three over $\mathbb Q(s)$.  A particular
factor could satisfy an additional arithmetic relation; none is asserted
or excluded here.

The replay reconstructs all eight primitive coefficient lists, checks
their signs, degrees, and exact SHA-256 fingerprints, verifies (3.5) in
$\mathbb Q(s)^3$, and independently substitutes the actual coefficient
formulas in all four phases, both parities, and both signs.  The 16 direct
substitutions through index 40 are replay controls for the all-index
identity, not a finite-fit inference.

## 4. Why four phases, not an adjacent-row scalar recurrence

For a fixed $M$, write



$$
\mathcal S_M=\{s\geq1:4s\leq M-5,\ s\equiv M+1\pmod3\},
 \quad p_s={4M+2s+1\over3},
 \quad h_s={M-4s-2\over3}.                               \tag{4.1}
$$



If $s$ advances by three, then



$$
p_{s+3}=p_s+2,qquad h_{s+3}=h_s-4.                     \tag{4.2}
$$



Thus $\epsilon_M=h_s\bmod2$ is constant, as required, but
$s\bmod4$ cycles through four values.  After four fixed-$M$ rows,



$$
s\mapsto s+12,qquad p\mapsto p+8,                      \tag{4.3}
$$



and the same coefficient pair in (2.2) returns.  Equation (1.3) is
therefore an exact order-three recurrence on each of the four interlaced
actual phases.  Its four terms correspond to candidate-prime gaps



$$
0, 8, 16, 24.             \tag{4.4}
$$



No unused parity, norm splitting argument, generic state, or adjacent-row
prime assumption enters this derivation.

## 5. Capacity audit for every bounded-gap cross-row overlap

Parameterize one fixed-$M$ slice by $s=s_0+3k$.  Then



$$
p_s=p_0+2k.                  \tag{5.1}
$$



Fix any nonzero integer $d$.  The standard Brun/Selberg
two-dimensional upper-bound sieve gives



$$
\#\{k\ll M:p_0+2k\text{ and }p_0+2(k+d)\text{ are prime}\}
 \ll_d {M\over(\log M)^2}.                               \tag{5.2}
$$



Since every candidate prime is $O(M)$, (5.2) implies



$$
\boxed{
 \sum_{\substack{s\in\mathcal S_M\\
                  p_s,\ p_{s+3d}\text{ prime}}}\log p_s
 \ll_d {M\over\log M}=o(M).}                            \tag{5.3}
$$



A finite union over bounded nonzero $d$'s is still $o(M)$.  This
applies both to adjacent fixed-$M$ rows and to every pair in the
step-12 recurrence window.

On the other hand, the prime number theorem in the candidate interval
gives total mass



$$
\sum_{\substack{s\in\mathcal S_M\\p_s\text{ prime}}}\log p_s
 ={M\over6}+o(M).                                        \tag{5.4}
$$



Removing every row having another prime at any prescribed finite set of
bounded offsets removes only $o(M)$ by (5.3).  Thus bounded-window
isolated primes still carry the full mass in (5.4).

This proves the exact scoped no-go:



$$
\boxed{
 \begin{gathered}
 \text{a cross-row gcd or resultant that requires selected collisions}\
 \text{at two bounded-offset actual prime rows controls only }o(M)\text{ overlap;}\\
 \text{it supplies no bound for isolated selected collisions.}
 \end{gathered}}                                         \tag{5.5}
$$



Equation (5.5) does not rule out a new theorem showing that every original
collision must propagate to a second prime row.  Such a theorem would be
powerful precisely because (5.3) would then close the weighted target.
The recurrence (1.3) alone does not provide that bridge: one factor zero
at one modulus gives one linear condition and neither makes a neighboring
candidate prime nor makes another factor value zero.

## 6. Declared actual-value control at $p=47$

Retain Item 324's preselected selected-eliminant row



$$
(M,s,h,p,\epsilon)=(34,2,8,47,0). \tag{6.1}
$$



For the prime of $L$ with $\sqrt2=7\pmod{47}$, direct evaluation of
the actual Item-308 coefficients gives



$$
\begin{array}{c|rrrr}
n&2&14&26&38\\ \hline
Y^+_{2,0}(n)&43&0&44&13\\
Y^-_{2,0}(n)& 0&0&35&44
\end{array}\pmod{47}.                                    \tag{6.2}
$$



Thus the selected factor is genuinely the actual factor sequence, not an
abstract recurrence state.  Even two displayed step-12 zeros do not
persist to the third term.  At fixed $M=34$, the next row is $s=5$
with candidate $49$, which is composite.

Equation (6.2) is **EXACT FINITE ONLY**.  The row (6.1) is an exact
Item-308 eliminant/container event, but it is not asserted to be a full
Item-264 two-coordinate collision.  It is not used to infer a zero density
or to disprove propagation from the stronger original gate.

## 7. Capacity, strict labels, and the remaining lemma

The live sufficient selected-container target remains



$$
\mathcal W_D(M)=
 \sum_{\substack{s\in\mathcal S_M\setminus\{2,4,6\}\\
                  p_s\text{ prime},\ p_s\mid D_{s,\epsilon_M}}}
 \log p_s=o(M).                                           \tag{7.1}
$$



Item 326 proves an exact recurrence for each actual factor but no
single-row prime-factor localization.  The next admissible lemma must use
the actual initial values to prove one of the following:



$$
\begin{gathered}
 \text{weighted zero density for one selected factor at its matching}\
 \text{prime ideals, a sublinear-height one-row divisor, or a genuine}\
 \text{bridge forcing every original collision into a bounded-gap pair.}
 \end{gathered}                                           \tag{7.2}
$$



- **PROVED:** the exact eight selected factorizations; actual initial
  triples; the determinant-form four-phase step-12 recurrence; nonvanishing
  of all four characteristic-zero recurrence coefficients at every positive
  index; fixed-$M$ phase arithmetic; and the bounded-gap weighted
  prime-pair estimate (5.3).

- **SCOPED BOUNDED-GAP NO-GO:** cross-row gcd/resultant methods whose
  hypotheses require two bounded-offset actual candidate-prime collision
  rows see only $o(M)$ overlap and do not control isolated rows.

- **EXACT FINITE ONLY:** the declared $p=47$ selected-factor replay and
  the 16 direct recurrence substitutions.  No scan or finite census is
  promoted.

- **OPEN:** a one-row arithmetic theorem for the actual selected factors;
  a propagation bridge from every original collision; (7.1);
  $\mathcal W_{\rm off}(M)=o(M)$; fixed-$j=1$ closure; Route 1; and
  every conclusion about $e+\pi$.

- **NOT CLAIMED:** that a factor sign or prime above $p$ is uniform; that
  the $p=47$ row is a full Item-264 collision; that the recurrence alone
  proves propagation or zero density; that bounded prime tuples have
  positive capacity; a prime scan; or positive ledger credit.

The ledger remains



$$
\boxed{\text{capacity booked}=0,\qquad
        \text{fixed-}j=1\text{ ceiling}={1\over36}
        \text{ per }6M.}                                  \tag{7.3}
$$



No canonical, master, or status file is edited by this research package.

## 8. Deterministic replay

From the archive root, run

~~~text
python work/item326_j1_selected_factor_step12_no_go_certificate.py --output work/item326_j1_selected_factor_step12_no_go_certificate.replay.json
~~~

The checker pins the canonical Items 308, 317, and 321 packages.  It
constructs the 36 exact companion transfers in $\mathbb Q(s)$, verifies
the Laplace identity, recomputes the primitive numerator and denominator
coefficient fingerprints and sign patterns, checks all eight
factorizations, rebuilds every actual initial triple, performs all 16
direct phase/parity/sign substitutions, and replays the declared
$p=47$ values.  It performs no prime scan.
