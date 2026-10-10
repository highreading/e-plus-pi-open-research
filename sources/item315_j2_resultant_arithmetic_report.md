> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 315 — arithmetic of the ordinary-$j=2$ endpoint resultant

Checked: 2026-08-31 (Beijing time)

## 1. Scope and strict verdict

Keep Item 314's two algebraic branch coefficients



$$
\mathcal A(X)=\sum_{r\ge0}a_rX^r,
 \qquad C_+(x)=\sum_{r\ge0}b_rx^r,
$$



on the two actual rays



$$
r=6n+e,\qquad e\in\{1,5\},\qquad n\ge0.
$$



The endpoint resultant is



$$
N_r=18^3a_r^3+11^3\,2^{2r+2}b_r^3.                \tag{1.1}
$$



Item 314 proved that this is exactly Item 250's old resultant after an
all-row $p$-unit cube.  This item does not rebook it.

> **PROVED — all-ray sign and characteristic-zero nonvanishing.**  On
> both actual rays and for every $n\ge0$,
> 

$$
>                 a_{6n+e}<0,\qquad b_{6n+e}<0,
>                 \qquad N_{6n+e}<0.                \tag{1.2}
>
$$


> Thus the exact characteristic-zero zero-row question left open in
> Item 314 is now closed: there are no such rows.

> **PROVED — exact raywise norm and diagonal structure.**  The
> $e=1$ ray is a pure-cubic norm from $\mathbb Q(\sqrt[3]2)$; the
> $e=5$ ray factors as a rational sum of cubes.  The full sequence
> $(N_r)$ is an explicit Hadamard diagonal of the two algebraic
> branches, hence is P-recursive, as are its two ray subsequences.

> **PROVED — scoped arithmetic no-go.**  The direct primitive odd norm
> fails the standard strong-divisibility law on both rays.  Moreover,
> P-recursiveness, nonvanishing, and individual height $O(r)$ alone
> cannot imply thin support in the freely varying tied family.  This is
> not a fixed-$M$ capacity statement.

These are global structural results, but they supply neither a new
divisor nor a weighted zero-density theorem.  Therefore



$$
\boxed{\text{new booking}=0},\qquad
 \boxed{\text{ordinary-}j=2\text{ ceiling remains }1/105\text{ per }6M}.
$$



## 2. One recurrence proves all signs

Item 237's exact differential certificate gives, for every coefficient
index $r>0$,



$$
\sum_{m=0}^3p_m(r/2)b_{r+6m}=0.                  \tag{2.1}
$$



The four degree-16 recurrence polynomials are stored in completely
factored form.  Every displayed linear factor is positive at $h>0$,
and every coefficient of each residual core polynomial is positive.
Their four scalar signs are



$$
p_0(h)<0,\quad p_1(h)<0,
                 \quad p_2(h)<0,\quad p_3(h)>0
                 \qquad(h>0).                     \tag{2.2}
$$



Item 309 proved the exact branch scaling



$$
[x^{6n+e}]C_-(x)=-2^{-2e/3}16^{-n}a_{6n+e}.
$$



Substitution into the same differential recurrence yields



$$
\sum_{m=0}^3p_m(r/2)16^{-m}a_{r+6m}=0.           \tag{2.3}
$$



All powers $16^{-m}$ are positive.  Hence both (2.1) and (2.3)
have the same sign-preserving form: if three successive values on a
ray are negative, the fourth is negative.

The six required initial values for each branch are exact.  For
example, on the $e=1$ ray,



$$
\begin{aligned}
(a_1,a_7,a_{13})
 &=\left(-\frac{20}{3},-\frac{22625504}{243},
         -\frac{21018613593436}{19683}\right),\\
(b_1,b_7,b_{13})
 &=\left(-\frac{40}{9},-\frac{216470078}{59049},
         -\frac{48866357392007231}{18596183472}\right).
\end{aligned}                                      \tag{2.4}
$$



On the $e=5$ ray,



$$
\begin{aligned}
(a_5,a_{11},a_{17})
 &=\left(-4004,-\frac{11636170000}{243},
         -\frac{3408994513794100}{6561}\right),\\
(b_5,b_{11},b_{17})
 &=\left(-\frac{868777}{2187},
         -\frac{25563514068625}{86093442},
         -\frac{227485167464197286875}{1129718145924}\right).
\end{aligned}                                      \tag{2.5}
$$



Equations (2.2)--(2.5) prove (1.2) by induction.  This is not a sign
conjecture inferred from a long table.

## 3. Exact norm splitting on the two rays

Put



$$
A_r=18a_r.                 \tag{3.1}
$$



### The $e=1$ ray

For $r=6n+1$, set



$$
k=\frac{2r+1}{3}=4n+1,
 \qquad B_r=11\,2^k b_r.                          \tag{3.2}
$$



Since $2r+2=3k+1$, (1.1) becomes



$$
\boxed{N_r=A_r^3+2B_r^3
       =\operatorname {Norm}_{\mathbb Q(\sqrt[3]2)/\mathbb Q}
          (A_r+B_r\sqrt[3]2).}                    \tag{3.3}
$$



### The $e=5$ ray

For $r=6n+5$, set



$$
k=\frac{2r+2}{3}=4n+4,
 \qquad B_r=11\,2^k b_r.                          \tag{3.4}
$$



Now $2r+2=3k$, so



$$
\boxed{
 N_r=A_r^3+B_r^3
     =(A_r+B_r)(A_r^2-A_rB_r+B_r^2).}              \tag{3.5}
$$



The signs from Section 2 give $A_r,B_r<0$.  Thus the first factor in
(3.5) is negative, while



$$
A_r^2-A_rB_r+B_r^2
 =\left(A_r-\frac{B_r}{2}\right)^2+\frac34B_r^2>0.
$$



This independently makes the nonvanishing in (1.2) transparent on the
split ray.

## 4. Actual cubic-character projection

On an actual row put



$$
p=2r+6s+3,\qquad c=2^{2s},\qquad
 G_{r,s}=18ca_r+11b_r.                             \tag{4.1}
$$



With $k,B_r$ as in Section 3, define



$$
t=2^{k+2s}.                \tag{4.2}
$$



Then exactly



$$
2^kG_{r,s}=A_rt+B_r.             \tag{4.3}
$$



On the $e=1$ ray,



$$
3(k+2s)=p-2,\qquad t^3=2^{p-2}=\frac12\pmod p.   \tag{4.4}
$$



Here $p\equiv5\pmod6$, so cubing is bijective on
$\mathbb F_p^*$, and $t$ is the unique cube root of $1/2$.

On the $e=5$ ray,



$$
k+2s=\frac{p-1}{3},qquad t^3=1\pmod p.           \tag{4.5}
$$



Thus $t=2^{(p-1)/3}$ is the cubic-character value of $2$.  If
$t=1$, an actual gate zero forces the rational linear factor
$A_r+B_r$ to vanish.  If $t\ne1$, it selects one of the two
conjugate factors inside



$$
A_r^2-A_rB_r+B_r^2.        \tag{4.6}
$$



This explains exactly why the old cubic resultant has false positives:
it is the product of all three endpoint components, whereas the actual
row selects only one.

The bounded Item 250 census through $p\le401$ contains nine resultant
hits.  Replaying (4.2)--(4.6) finds only three selected gate hits and six
non-selected components.  This count is **EXACT FINITE ONLY** and is not
a density theorem.

### 4.1 Separate compulsory-content and support audit

Write



$$
\sigma_{e,n}=\frac{g_n\kappa_e}{16^n}.
$$



Item 314 proves that $\sigma_{e,n}$ is a $p$-unit on every actual
row.  On the split $e=5$ ray the two old-resultant factors satisfy
separately



$$
\begin{aligned}
L_r+2^kM_r
 &=\sigma_{5,n}(A_r+B_r),\\
L_r^2-2^kL_rM_r+2^{2k}M_r^2
 &=\sigma_{5,n}^2(A_r^2-A_rB_r+B_r^2).
\end{aligned}                                      \tag{4.7}
$$



On the $e=1$ ray, in $\mathbb Q(\sqrt[3]2)$,



$$
L_r+2^kM_r\sqrt[3]2
 =\sigma_{1,n}(A_r+B_r\sqrt[3]2),                  \tag{4.8}
$$



so taking the field norm multiplies by exactly $\sigma_{1,n}^3$.
Thus the certified compulsory hypergeometric content is removed factor
by factor, not merely after multiplying the factors together.

There is also an all-row integer clearing.  With



$$
H_r=6^{r+3}r!,
$$



Item 314 gives $p\nmid H_r$, and



$$
\begin{aligned}
H_r(A_r+B_r)&\in\mathbb Z,\\
H_r^2(A_r^2-A_rB_r+B_r^2)&\in\mathbb Z,\\
H_r^3(A_r^3+2B_r^3)&\in\mathbb Z.
\end{aligned}                                      \tag{4.9}
$$



No further same-index numerator gcd is known to be a $p$-unit, so no
additional content is divided or credited.

Neither rational $e=5$ factor has empty actual selected support.  Two
exact rows are shown below; all factor entries in the table are residues
modulo $p$:



$$
\begin{array}{c|c|c|c|c|c}
(p,s,r)&t&A_r+B_r&A_r^2-A_rB_r+B_r^2&A_rt+B_r
&\text{selected component}\\ \hline
(2281,378,5)&1&0&447&0&\text{linear}\\
(271,7,113)&242&269&0&0&\text{quadratic conjugate}.
\end{array}                                        \tag{4.10}
$$



The $e=1$ norm also has an actual selected example
$(p,s,r)=(383,27,109)$.  These exact counterexamples rule out only a
universal exclusion of one displayed factor.  They prove no positive
density or positive Chebyshev mass.

## 5. The full sequence is an exact Hadamard diagonal

Let



$$
\mathscr N(z)=\sum_{r\ge0}N_rz^r.
$$



Writing $\odot$ for coefficientwise product gives the exact identity



$$
\boxed{
\mathscr N(z)=18^3(\mathcal A\odot\mathcal A\odot\mathcal A)(z)
 +4\,11^3(C_+\odot C_+\odot C_+)(4z).}             \tag{5.1}
$$



Equivalently,



$$
\boxed{
\begin{aligned}
\mathscr N(z)={}&18^3\operatorname {CT}_{u,v}
  \mathcal A(u)\mathcal A(v)\mathcal A\!\left(\frac z{uv}\right)\\
&+4\,11^3\operatorname {CT}_{u,v}
  C_+(u)C_+(v)C_+\!\left(\frac{4z}{uv}\right).
\end{aligned}}                                      \tag{5.2}
$$



Indeed, the constant term forces the three coefficient indices to be
equal.  The extra $4^{r+1}$ in the second term is exactly
$2^{2r+2}$.

Both branch series are algebraic.  Algebraic series are D-finite, finite
products and diagonals of D-finite series are D-finite, and arithmetic
subsequences of a D-finite series are D-finite.  Consequently



$$
(N_r),\qquad(N_{6n+1}),\qquad(N_{6n+5})
$$



are all P-recursive.  This is a global exact closure theorem; no fitted
recurrence is promoted.

## 6. Compulsory content and the primitive-division warning

Item 314 already proved



$$
L_r^3+2^{2r+2}M_r^3
 =\left(\frac{g_n\kappa_e}{16^n}\right)^3N_r,       \tag{6.1}
$$



and proved that the displayed multiplier is a $p$-unit on every
actual row.  Equation (6.1) is the complete certified hypergeometric
content removal relevant here.  The endpoint norm is therefore not a
new condition and is not booked twice.

One may clear the denominators of $(a_r,b_r)$ and divide their integer
gcd to obtain a visually primitive coefficient pair.  But no theorem
currently proves that this additional same-index gcd is a $p$-unit on
every actual row.  Dividing it in the collision gate could erase exactly
a target prime.  Item 315 therefore uses that primitive pair only for a
diagnostic no-go and never for capacity accounting.

## 7. The direct strong-divisibility ansatz fails

For a fixed ray, let $d_r$ clear the common denominator of
$(a_r,b_r)$, put



$$
g_r=\gcd(d_ra_r,d_rb_r),\qquad
 u_r=\frac{d_ra_r}{g_r},\qquad
 v_r=\frac{d_rb_r}{g_r},                           \tag{7.1}
$$



and let $S_{e,n}$ be the odd part of



$$
18^3u_r^3+11^3\,2^{2r+2}v_r^3,\qquad r=6n+e.    \tag{7.2}
$$



This is the most direct primitive odd norm.  Exact values give, on the
$e=1$ ray,



$$
\begin{aligned}
S_{1,1}&=157687237927307311,\\
S_{1,2}&=28573544608814224381754119965356584948303213,\\
\gcd(S_{1,1},S_{1,2})&=1.
\end{aligned}                                      \tag{7.3}
$$



On the $e=5$ ray,



$$
\begin{aligned}
S_{5,1}&=101313950522307097175192402759017,\\
S_{5,2}&=932597871644442001279944106904019983534303308529,\\
\gcd(S_{5,1},S_{5,2})&=1.
\end{aligned}                                      \tag{7.4}
$$



The standard strong-divisibility law would require



$$
\gcd(S_{e,1},S_{e,2})=S_{e,\gcd(1,2)}=S_{e,1},
$$



so (7.3)--(7.4) are exact counterexamples on both rays.  This proves a
scoped no-go for that ansatz; it does not rule out every possible
congruence or divisibility law.

## 8. What P-recursiveness and height do—and do not—show

The new nonvanishing theorem makes every fixed-$r$ numerator genuine,
but Item 314's individual height bound is only



$$
h(N_r)=O(r).               \tag{8.1}
$$



Summing this over linearly many $r$ gives $O(M^2)$, weaker than the
existing $O(M)$ raw cell ceiling.

There is also a direct tied-prime comparison.  The nonzero
first-order-hypergeometric sequence



$$
H_r=\binom{7r}{r}           \tag{8.2}
$$



is P-recursive and has $\log H_r=O(r)$.  Every prime



$$
6r<p\le7r                  \tag{8.3}
$$



divides $H_r$ exactly once.  Restricting further to



$$
p\equiv2r+3\pmod6          \tag{8.4}
$$



makes every such prime an actual tied-form prime
$p=2r+6s+3$.  On either fixed ray, the prime-number theorem in
arithmetic progressions gives positive linear Chebyshev mass in
(8.3)--(8.4).

Therefore abstract P-recursiveness, exact nonvanishing, and exponential
height cannot by themselves imply thin support in the freely varying
tied family $(r,s)$.  This comparison does **not** impose the master
fixed-$M$ normalization



$$
2M=5r+14s+7,               \tag{8.5}
$$



and is not evidence that the fixed-$M$ ceiling $1/105$ is sharp.  The
only fixed-$M$ method no-go retained here is Item 314's rigorous
observation that summing the available individual height estimates gives
$O(M^2)$, weaker than the existing $O(M)$ ceiling.  A successful
continuation needs sequence-specific modular information together with
the actual fixed-$M$ geometry.

## 9. Capacity effect and remaining theorem

The all-ray nonvanishing theorem closes one explicit open line from Item
314, and the cubic-character projection identifies which endpoint factor
the actual row selects.  Neither statement bounds the weighted set of
selected primes.

The smallest live arithmetic target remains



$$
\boxed{
\sum_{\substack{
r=6n+e,\ p=2r+6s+3\ {\rm prime}\\
2M=5r+14s+7\\
18\,2^{2s}a_r+11b_r\equiv0\pmod p}}
\log p=o(M).}                                      \tag{9.1}
$$



Even (9.1) concerns only the necessary rank-drop gate; actual residual
period incidence is stronger.  Item 315 books zero and leaves the
ordinary-$j=2$ ceiling at $1/105$ per $6M$.

## 10. Deterministic replay and strict labels

From the portable archive root:

~~~text
python scripts/item315_j2_resultant_arithmetic_certificate.py
python scripts/item315_j2_resultant_arithmetic_certificate.py \
  --output results/item315_j2_resultant_arithmetic_certificate_replay.json
~~~

At the declared bound $r\le131$, the finite sign/factorization replay
contains 44 ray rows and no failures.  The row-stream SHA-256 is

~~~text
c6d4cb53829e55ecdf8d74ae53521ea89216a39f6c8beab4542a738219721fb5
~~~

The nine-row character-projection stream has SHA-256

~~~text
e330b8e80d60deb2f575f42500ae941eb8bdb798d7069a085764709361b41d85
~~~

### PROVED

* The recurrence sign pattern and all-$n$ inequalities (1.2).
* Strict characteristic-zero nonvanishing $N_{6n+e}<0$.
* The two raywise cubic norm factorizations (3.3), (3.5).
* The actual cubic-character projection (4.3)--(4.6).
* The Hadamard/constant-term diagonal and P-recursiveness.
* Failure of the displayed primitive strong-divisibility ansatz.
* The scoped P-recursiveness/nonvanishing/height method no-go.

### EXACT FINITE ONLY

* The declared $r\le131$ sign and factorization replay.
* The nine old-resultant hits through $p\le401$, including the three
  selected gate components.

### OPEN

* Weighted zero density for $N_r$, or for the stronger selected gate
  (9.1).
* Any sequence-specific thin-support, congruence, or average Frobenius
  theorem.
* Actual residual-period incidence on selected gate rows.
* Any ordinary-$j=2$ capacity reduction, Route-1 completion, or
  conclusion about $e+\pi$.
