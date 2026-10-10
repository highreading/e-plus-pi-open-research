> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 366 — the joint fixed-$j=1$ pair as a framed divided-Frobenius moment

Date: 2026-09-01

## 1. Outcome and capacity first

The only family studied here is the actual fixed-$j=1$ selector



$$
p=4h+6s+3,\qquad M=3h+4s+2,\qquad h,s\geq1.             \tag{1.1}
$$



Put



$$
n=2h,\qquad r=2s+1.                                      \tag{1.2}
$$



Item 360 proved that every full ordinary common-log collision forces the
joint pair



$$
a_{r,n}=0,\qquad Q_0(h,s)=0\pmod p,                       \tag{1.3}
$$



where $a_{r,n}$ is the selected Hasse coefficient and $Q_0$ is the
first original, transverse common-log coordinate.  The converse in (1.3)
is not claimed.

This item gives one exact finite-field object containing both coordinates.
Over $\mathbb F_{p^2}$, they are two linearly independent *framed matrix
coefficients* of one natural rank-five moment: a scalar Hasse block together
with two rank-two unipotent divided-Frobenius blocks.  Its summed matrix is



$$
\boxed{
\mathcal S_{h,s}=
\operatorname {diag}\!\left(
-a_{r,n},
\begin{bmatrix}0&-2c_T\\0&0\end{bmatrix},
\begin{bmatrix}0&c_L\\0&0\end{bmatrix}
\right),}                                                \tag{1.4}
$$



with



$$
Q_0=2c_T-c_L.                                             \tag{1.5}
$$



Thus



$$
(\mathcal S_{h,s})_{11}=-a_{r,n},\qquad
(\mathcal S_{h,s})_{23}+(\mathcal S_{h,s})_{45}=-Q_0.   \tag{1.6}
$$



The two functionals in (1.6) are independent on the framed matrix space;
no claim of statistical independence is made.

The representation also gives a sharp obstruction to the most immediate
trace strategy:



$$
\boxed{
\det\mathcal S_{h,s}=0,\qquad
\chi_{\mathcal S}(X)=X^4(X+a_{r,n}),\qquad
\operatorname {tr}(\mathcal S^k)=(-a_{r,n})^k.}          \tag{1.7}
$$



Every ordinary trace, determinant, and characteristic-polynomial invariant
for this moment forgets the transverse coordinate.  It lies entirely in a
nilpotent extension slot.  Consequently the joint collision cannot be
replaced by a trace-zero or determinant-zero condition without new framed
extension-class information.

There is a second obstruction.  The literal Kummerization of the finite-log
factor appearing in the transverse block has at least $p-2$ distinct
zeros after the substitution $w=z^2$.  Hence that direct construction has
linearly growing singular support, rather than the fixed support enjoyed by
Item 342's selected-Hasse Kummer sums.

These results hold on every actual row and therefore reach the full raw
fixed-$j=1$ mass



$$
{M\over6}+o(M),\qquad {1\over36}\text{ per }6M.           \tag{1.8}
$$



But no selector-aware horizontal nonconcentration theorem is proved.  Thus



$$
\boxed{
\text{new linear log rate}=0,\quad
\text{new fixed-}j=1\text{ capacity reduction}=0,\quad
\text{booking}=0.}                                       \tag{1.9}
$$



The $1/36$ ceiling is retained and Route 1 remains ACTIVE.

## 2. The selected Hasse block

Set



$$
G(u)=1-4u+6u^2-4u^3=(1-u)^4-u^4.                        \tag{2.1}
$$



Items 339 and 342 give



$$
a_{r,n}=[u^n]G(u)^{-r}\in\mathbb Z.                      \tag{2.2}
$$



Since $n<p$, the positive-power Frobenius chart is



$$
a_{r,n}\equiv[u^n]G(u)^{p-r}\pmod p.                    \tag{2.3}
$$



Let $q=p^2$ and $E=p-r$.  Item 342's degree audit gives



$$
\deg G^E=2p+2n<3p<q-1.                                  \tag{2.4}
$$



Multiplicative orthogonality over $\mathbb F_q^\times$ therefore isolates
the selected coefficient exactly:



$$
\boxed{
\sum_{x\in\mathbb F_q^\times}x^{-n}G(x)^E=-a_{r,n}.}    \tag{2.5}
$$



This is the scalar block in (1.4).  As throughout the fixed-$j=1$
branch, its vanishing is necessary for the original collision; it is not
used as a converse.

## 3. The transverse coordinate is an exact divided-Frobenius coefficient

Define the finite logarithm



$$
\mathscr L_p(w)
={ (1+w)^p-1-w^p\over p}pmod p
=\sum_{k=1}^{p-1}{1\over p}{p\choose k}w^k
\in\mathbb F_p[w].                                       \tag{3.1}
$$



For $1\leq k<p$,



$$
{1\over p}{p\choose k}
\equiv {(-1)^{k-1}\over k}\pmod p.                      \tag{3.2}
$$



Thus $\mathscr L_p$ is exactly the relevant truncation of
$\log(1+w)$, and (3.1) is the first divided-Frobenius defect of
$1+w$:



$$
(1+w)^p=1+w^p+p\mathscr L_p(w).                          \tag{3.3}
$$



Put



$$
P_0(z)=(1-z)^{2h}(1+z)(1+z^2)^{2s},                     \tag{3.4}
$$



and



$$
T=2h+6s+2,\qquad L=4h+4s+2.                             \tag{3.5}
$$



Both $T$ and $L$ are strictly below $p$.  Hence Item 360's
logarithmic parameter derivative reduces coefficientwise to (3.1).  If



$$
F_Q(z)=P_0(z)\mathscr L_p(z^2),\qquad
c_N=[z^N]F_Q(z),                                         \tag{3.6}
$$



then the exact actual-family congruence is



$$
\boxed{Q_0(h,s)=2c_T-c_L\pmod p.}                        \tag{3.7}
$$



No numerator moment has been introduced: (3.7) is the first original
common-log coordinate reconstructed in Item 360.

Write



$$
d=\deg P_0=2h+4s+1.                                      \tag{3.8}
$$



On (1.1),



$$
\deg F_Q=d+2(p-1)<3p<q-1.                               \tag{3.9}
$$



Therefore the same extension field isolates each transverse coefficient:



$$
\boxed{
-\sum_{x\in\mathbb F_q^\times}x^{-N}F_Q(x)=c_N,
\qquad N=T,L.}                                           \tag{3.10}
$$



## 4. One rank-five framed moment

The divided-Frobenius defect has the natural unipotent frame



$$
U_p(z)=
\begin{bmatrix}1&\mathscr L_p(z^2)\\0&1\end{bmatrix}.  \tag{4.1}
$$



For $x\in\mathbb F_q^\times$, define the block-diagonal local object



$$
\mathcal F_{h,s}(x)=
\bigl(x^{-n}G(x)^E\bigr)
\ \oplus\ 
\bigl(2x^{-T}P_0(x)U_p(x)\bigr)
\ \oplus\ 
\bigl(-x^{-L}P_0(x)U_p(x)\bigr).                        \tag{4.2}
$$



The last block has scalar weight $-x^{-L}P_0(x)$.  Define



$$
\mathcal S_{h,s}=\sum_{x\in\mathbb F_q^\times}
\mathcal F_{h,s}(x).                                     \tag{4.3}
$$



Because



$$
\deg P_0=d<T,L,                                          \tag{4.4}
$$



the two diagonal moments of each unipotent block vanish.  Equations
(2.5) and (3.10) then give (1.4) exactly.

Let



$$
\lambda_H(A)=A_{11},\qquad
\lambda_Q(A)=A_{23}+A_{45}.                              \tag{4.5}
$$



These are linearly independent framed functionals on $M_5$, and



$$
\lambda_H(\mathcal S)=-a_{r,n},\qquad
\lambda_Q(\mathcal S)=-Q_0.                             \tag{4.6}
$$



Thus the answer to the representation question is precise:



$$
\boxed{
\begin{gathered}
\text{the actual pair is one rank-five framed divided-Frobenius moment}\
\text{with two independent matrix-coefficient selectors,}\
\text{but no irreducible lisse or compatible Frobenius system is proved.}
\end{gathered}}                                          \tag{4.7}
$$



The direct sum in (4.2) is not being promoted to a monodromy theorem.
Its value is that it preserves both exact collision-forced coordinates and
exhibits where the transverse one lives: in a unipotent extension slot,
not in the semisimple Hasse block.

## 5. Exact trace/determinant no-go for this representation

The matrix (1.4) is upper triangular, with diagonal



$$
(-a_{r,n},0,0,0,0).                                      \tag{5.1}
$$



It follows for every $k\geq1$ that



$$
\operatorname {tr}(\mathcal S^k)=(-a_{r,n})^k,           \tag{5.2}
$$



and its determinant and characteristic polynomial are those in (1.7).
In particular, setting $Q_0=0$ changes neither invariant.  Indeed,
$Q_0=0$ is the cancellation $c_L=2c_T$; it does not require either
nilpotent block entry to vanish.

For one matrix, the universal polynomial conjugacy-invariant ring is
generated by the characteristic coefficients.  Hence every ordinary
universal polynomial
conjugacy-invariant of this rank-five moment factors through the selected
Hasse coordinate and forgets the transverse selector.

This is a scoped no-go.  It closes trace, determinant, characteristic
polynomial, and their polynomial combinations for the exact moment
(4.3).  It does **not** rule out:

1. a different bounded-conductor Frobenius object in which the pair occurs
   semisimply;
2. framed extension-class equidistribution;
3. a non-conjugacy-invariant selector-aware matrix coefficient theorem; or
4. a horizontal chosen-prime or average-gcd theorem.

No ambient block entry is required to vanish.  In particular, replacing
the actual equation $c_L=2c_T$ by $c_T=c_L=0$ would strengthen the
gate illegitimately and receives no credit.

## 6. Exact base-field de-aliasing of the transverse blocks

The extension field is not essential for exactness.  Let



$$
\vartheta=z{d\over dz},\qquad
S_{N,j}=\sum_{x\in\mathbb F_p^\times}
x^{-N}(\vartheta^jF_Q)(x),\quad j=0,1.                  \tag{6.1}
$$



For each $N=T,L$, the degree identities on (1.1) show that the only
indices congruent to $N\pmod{p-1}$ in $F_Q$ are



$$
N,\qquad N+p-1.                                          \tag{6.2}
$$



Orthogonality gives



$$
\begin{aligned}
-S_{N,0}&=c_N+c_{N+p-1},\\
-S_{N,1}&=Nc_N+(N-1)c_{N+p-1}.
\end{aligned}                                            \tag{6.3}
$$



Therefore



$$
\boxed{c_N=(N-1)S_{N,0}-S_{N,1}.}                       \tag{6.4}
$$



So $Q_0$ is an exact linear combination of four base-field framed
moments.  This neither loses the target nor creates an additional forced
coordinate.  It also does not change Section 5: ordinary traces still see
only the diagonal Hasse block.

## 7. Why literal finite-log Kummerization is not fixed support

Differentiate (3.1):



$$
\mathscr L_p'(w)
=\sum_{j=0}^{p-2}(-w)^j
={1-w^{p-1}\over1+w}.                                    \tag{7.1}
$$



If $a$ is a repeated root of $\mathscr L_p$, then
$a\in\mathbb F_p^\times\setminus\{-1\}$.  At such a root,



$$
\mathscr L_p''(a)={a^{-1}\over1+a}\ne0.                 \tag{7.2}
$$



Thus every root of $\mathscr L_p$ has multiplicity at most two.  Since
its degree is $p-1$, it has at least



$$
{p-1\over2}                                               \tag{7.3}
$$



distinct roots over the algebraic closure.  The root at zero is simple;
after substituting $w=z^2$, every nonzero root has two square roots.
Consequently



$$
\boxed{\mathscr L_p(z^2)\text{ has at least }p-2
\text{ distinct roots}.}                                \tag{7.4}
$$



Therefore a literal full-order Kummer character applied to the polynomial
$\mathscr L_p(z^2)$ has conductor support growing at least linearly with
$p$.  The fixed-support $O(\sqrt p)$ architecture of Item 342 cannot
be copied verbatim for the transverse block.

The word *literal* is essential.  Section 7 does not rule out a different
unipotent $F$-crystal, an Artin--Schreier reformulation, cancellation of
apparent singularities, or another bounded-conductor compression.

## 8. Declared exact controls

The deterministic certificate uses only four rows predeclared in Items
218, 342, and 360.  It performs no prime or collision scan.

| $(h,s,p)$ | $(M,n,r)$ | $a_{r,n}$ | $Q_0$ | finite-log root count |
|---|---|---:|---:|---:|
| $(1,1,13)$ | $(9,2,3)$ | $0$ | $9$ | $10$ |
| $(2,1,17)$ | $(12,4,3)$ | $8$ | $14$ | $16$ |
| $(8,2,47)$ | $(34,16,5)$ | $0$ | $30$ | $46$ |
| $(10,11,109)$ | $(76,20,23)$ | $70$ | $0$ | $106$ |

The first and third rows show that selected-Hasse vanishing does not force
the transverse equation on the actual orbit.  The fourth shows the reverse
non-implication.  None is asserted to be a full collision or used as
asymptotic evidence.

For each row the certificate independently verifies:

1. the actual selector relations (1.1)--(1.2);
2. the integer selected-Hasse prefix;
3. the finite-log convolution and (3.7);
4. the $\mathbb F_{p^2}$ rank-five moment, entry by entry;
5. both base-field two-alias inversions; and
6. the exact algebraic-closure root count and bound (7.4).

## 9. Capacity audit and missing global input

Define the selector-aware joint envelope



$$
\mathcal W_{H,Q}(M)
=\sum_{\substack{s\in\mathcal S_M,\ p_s\ \mathrm{prime}\\
a_{2s+1,2h_s}=0\ (\mathrm{mod}\ p_s)\\
Q_0(h_s,s)=0\ (\mathrm{mod}\ p_s)}}\log p_s.             \tag{9.1}
$$



Item 360 gives



$$
\mathcal W_{\rm full}(M)\leq\mathcal W_{H,Q}(M).         \tag{9.2}
$$



All transforms above apply to every actual row, so their raw reach is the
full



$$
\mathcal W_{H,Q}(M)\leq {M\over6}+o(M).                  \tag{9.3}
$$



A proof of $\mathcal W_{H,Q}(M)=o(M)$ would remove the entire $1/36$
ceiling.  A strict constant below $M/6$ would already be ledger-relevant.

The exact representation does not supply either bound.  A useful next
theorem must control the two *framed* functionals horizontally as the chosen
prime and selector move.  Ordinary Frobenius trace distribution is
insufficient because (1.7) erases $Q_0$; literal Kummerization has growing
support by (7.4).  The remaining admissible inputs include:

- a genuine bounded-conductor lisse or crystalline joint system;
- selector-aware extension-class equidistribution;
- a chosen-prime nonconcentration theorem for the framed nilpotent slot; or
- an average-gcd theorem for the two exact integer carriers.

No such input is proved here.  Algebraic encoding receives no mass credit.

## 10. Strict decision

### PROVED

- the exact $\mathbb F_{p^2}$ rank-five framed divided-Frobenius moment
  for the actual pair;
- two independent framed matrix coefficients equal to $-a_{r,n}$ and
  $-Q_0$;
- the base-field two-alias and two-Euler-moment theorem for each transverse
  coefficient;
- trace, determinant, characteristic-polynomial, and polynomial
  conjugacy-invariant blindness to the transverse extension slot;
- a linear distinct-root lower bound for literal finite-log Kummerization;
- zero booking.

### EXACT FINITE ONLY

- four predeclared separation/control rows;
- no row is promoted to a full collision or density statement;
- no prime scan.

### OPEN

- a genuine bounded-conductor lisse or crystalline joint system;
- framed extension-class equidistribution or horizontal chosen-prime
  nonconcentration;
- any selector-aware trace replacement that does not impose ambient zeros;
- weighted joint-zero density, any fixed-$j=1$ ceiling reduction, Route 1,
  and every conclusion about $e+\pi$.

## 11. Ledger consequence



$$
\begin{array}{c|c}
\text{quantity}&\text{Item 366 value}\\ \hline
\text{actual rows reached}&\text{all}\\
\text{exact framed target coordinates}&2\\
\text{new proved excluded log mass}&0\\
\text{new fixed-}j=1\text{ capacity reduction}&0\\
\text{retained fixed-}j=1\text{ ceiling per }6M&1/36
\end{array}                                               \tag{11.1}
$$



Item 366 is a representation theorem and a scoped trace/Kummer no-go.  It
identifies the missing input as framed, selector-aware, and horizontal.  It
does not turn the new codimension from Item 360 into weighted mass.
