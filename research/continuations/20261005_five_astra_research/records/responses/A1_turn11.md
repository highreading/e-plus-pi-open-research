> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## Audit verdict

The coordinator’s modulo-$27$ proposal is correct, including the factor $1/2$, the adjacent-binomial sign, and both projection precisions. Two further simplifications are available:

1. **The higher binomial corrections disappear after contraction when $3\mid M$.**
2. **The fixed contraction identity holds for every integer $M\ge0$**, not just for $M$ exceeding its degree. Thus $M=21$ needs no exceptional contraction formula.

Using the supplied exact $\mathcal H$-coefficient certificate gives the sharper norm digit


$$
\boxed{\frac c3\equiv4+3M\pmod{27}\qquad(3\mid M,\ M\ge3).}
$$


The remaining mixed digit reduces to one fixed polynomial of degree at most $20$, defined explicitly below. This gives a bounded, evaluated polynomial rule for the entire local primitive ray modulo $27$; a single bounded symbolic contraction can simplify that rule further.

No irrationality conclusion follows.

---

## 1. Direct check of the factorial quotient

For $a=b+c$, with $a,b,c\ge0$, put


$$
U(a)=\prod_{r=0}^{a-1}(3r+1)(3r+2).
$$


Exactly,


$$
(3r+1)(3r+2)
=2\left(1+\frac92r(r+1)\right).
$$


Since products of two $9$-terms vanish modulo $27$,


$$
U(a)\equiv
2^a\left(1+\frac92\sum_{r=0}^{a-1}r(r+1)\right)\pmod{27}.
$$


The sum is $a(a^2-1)/3$, and


$$
\frac{a(a^2-1)-b(b^2-1)-c(c^2-1)}3=abc.
$$


Separating the multiples of $3$ in the factorials therefore gives


$$
\boxed{
\binom{3a}{3b}
\equiv\binom ab\left(1+\frac92abc\right)\pmod{27}.}
\tag{1}
$$


Only unit factorial products are inverted. No unit hypothesis on $\binom ab$ is needed.

Also,


$$
\frac{3a+1}{3c+1}
=1+\frac{3b}{1+3c}
\equiv1+3b-9bc\pmod{27}.
$$


Multiplication by (1) proves


$$
\boxed{
\binom{3a+1}{3b}
\equiv\binom ab
\left(1+3b-9bc+\frac92abc\right)\pmod{27}.}
\tag{2}
$$


Thus the proposed $1/2$ and negative adjacent correction are both correct.

---

## 2. Moment and projection precisions

Retain the fixed polynomial


$$
f(s)=\sum_{\ell=0}^{8}
\frac{(-1)^\ell}{2^\ell\ell!}
(s)_\ell(s+1)^{\overline\ell}.
$$


The exact factorial-moment expansion has terms


$$
\binom{s}{\ell}(-2)^{s-\ell}(s+1)^{\overline\ell}.
$$


For $\ell\ge9$, the rising factorial has valuation at least


$$
v_3(\ell!)\ge v_3(9!)=4.
$$


Consequently,


$$
b_s^{\rm mom}\equiv(-2)^sf(s)\pmod{81}
\qquad(s\ge0).
$$



Define


$$
\begin{aligned}
F_0(t)={}&4f(3t)-8(3t+1)f(3t+1)\\
&+4(3t+1)(3t+2)f(3t+2),\\
F_1(t)={}&-8f(3t+1)+16(3t+2)f(3t+2)\\
&-8(3t+2)(3t+3)f(3t+3),
\end{aligned}
$$


and


$$
E_0(t)=\frac{(1-9t)F_0(t)}3,\qquad
E_1(t)=(1-9t)F_1(t).
\tag{3}
$$


Because


$$
(-8)^t=(1-9)^t\equiv1-9t\pmod{81},
$$


these satisfy


$$
\boxed{
E_0(t)\equiv e_{3t}/3\pmod{27},\qquad
E_1(t)\equiv e_{3t+1}\pmod{27}}
\tag{4}
$$


for every integer $t\ge0$. In particular,


$$
E_0(t)\equiv1,\qquad E_1(t)\equiv2\pmod3.
\tag{5}
$$



For the actual residuals, the already established $3\mid M$ support calculation gives


$$
v=9u',\qquad w\in3\mathbb Z_3^L,\qquad E^{-1}\in M_L(\mathbb Z_3).
$$


Hence


$$
v^TE^{-1}v\in81\mathbb Z_3,\qquad
v^TE^{-1}w\in27\mathbb Z_3.
$$


It follows, at exactly the required precisions, that


$$
\boxed{c/3\equiv R/3\pmod{27},\qquad
\xi_{\rm last}\equiv X\pmod{27}.}
\tag{6}
$$


The negative Schur signs remain present in the exact identities; their terms vanish only after these divisibility checks.

---

## 3. The contraction identity has no small-$M$ exception

Define


$$
C_{a,t}(M)=
\sum_{h=t}^{a}
\left\{\begin{matrix}a\\h\end{matrix}\right\}
(M)_h\binom ht,
\qquad
\mathcal I_{ab}(M)=
\sum_{t=0}^{\min(a,b)}C_{a,t}(M)C_{b,t}(M).
\tag{7}
$$



Then, for **all integers $M\ge0$** and $a,b\ge0$,


$$
\boxed{
\mathcal I_{ab}(M)
=
\sum_{D,E=0}^{M}
\tau_D\tau_E D^aE^b\binom{D+E}{D}.}
\tag{8}
$$



Indeed,


$$
\sum_D\tau_D(1+z)^D=z^M,
$$


and applying $((1+z)\partial_z)^a$ gives


$$
\sum_D\tau_DD^a(1+z)^D
=
\sum_{h=0}^{a}
\left\{\begin{matrix}a\\h\end{matrix}\right\}
(M)_h(1+z)^hz^{M-h}.
$$


When $h>M$, the falling factorial $(M)_h$ is exactly zero. Thus all surviving powers are nonnegative, and the coefficient at $z^{M-t}$ is $C_{a,t}(M)$. Also $C_{a,t}(M)=0$ when $t>M$.

Taking the Pascal Gram product proves (8). The earlier restriction $M\ge a+b$ was sufficient but unnecessary.

For a fixed polynomial $P(D,E)=\sum p_{ab}D^aE^b$, write


$$
\mathscr C_M(P)=\sum_{a,b}p_{ab}\mathcal I_{ab}(M).
\tag{9}
$$


This is an explicit finite rational-polynomial operation, with bounds determined by the degree of $P$, not by $M$.

---

## 4. The cubic binomial corrections vanish on $3\mid M$

The few contractions needed here are


$$
\mathcal I_{11}=2M^2,\qquad
\mathcal I_{21}=\mathcal I_{12}=3M^3-M^2.
\tag{10}
$$


For example,


$$
(C_{1,0},C_{1,1})=(M,M),
$$




$$
(C_{2,0},C_{2,1},C_{2,2})
=(M^2,\,2M^2-M,\,M^2-M),
$$


which proves the second identity.

Let $t=D+E$. Equations (1)–(6) give


$$
c/3\equiv
\mathscr C_M\!\left(\left(1+\frac92tDE\right)E_0(t)\right)
\pmod{27}.
$$


By (5), the added term reduces to


$$
\frac92\mathscr C_M(tDE)
=\frac92(6M^3-2M^2)
=27M^3-9M^2.
$$


This vanishes modulo $27$ whenever $3\mid M$. Therefore


$$
\boxed{c/3\equiv\mathscr C_M(E_0(D+E))=\mathcal H(M)\pmod{27}.}
\tag{11}
$$



Similarly,


$$
\xi_{\rm last}\equiv
\mathscr C_M\!\left(
\left(1+3D-9DE+\frac92tDE\right)E_1(t)
\right)\pmod{27}.
$$


The last two corrections, using $E_1\equiv2\pmod3$, contract to


$$
-18\mathcal I_{11}+9\mathscr C_M(tDE)
=54M^3-54M^2,
$$


which is divisible by $27$ for every $M$. Thus


$$
\xi_{\rm last}\equiv
\mathscr C_M((1+3D)E_1(D+E))\pmod{27}.
$$


Symmetry in $D,E$ gives the exact simplification


$$
\boxed{
\xi_{\rm last}\equiv\mathcal G(M)\pmod{27},\qquad
\mathcal G(M)=
\mathscr C_M\!\left(
\left(1+\frac32(D+E)\right)E_1(D+E)
\right).}
\tag{12}
$$



This removes all cubic two-variable factors from the computation.

---

## 5. Audit and simplification of the supplied $\mathcal H$ certificate

The supplied source implements exactly (3), (7), and (9): its falling-factorial construction, Stirling recurrence, and Pascal inner product agree with the displayed definitions. Its reported coefficient list has a common denominator $143360$, a $3$-adic unit.

From that list,


$$
\mathcal H(M)
=4-\frac{3801}{2}M
+\frac{141742858592988073848411}{560}M^2
+\sum_{h=3}^{19}h_hM^h,
$$


where every $h_h\in\mathbb Z_3$. Moreover,


$$
3\mid141742858592988073848411.
$$


Consequently, substituting $M=3T$,

- the linear term is
  

$$
-\frac{11403}{2}T\equiv9T\pmod{27};
$$


- the quadratic term is divisible by $27$;
- every higher term is divisible by $27$.

The supplied exact coefficient certificate therefore yields


$$
\boxed{\mathcal H(3T)\equiv4+9T\pmod{27}.}
\tag{13}
$$


In particular,


$$
\boxed{\mathcal H(3T)\equiv4\pmod9.}
$$



This is a coefficientwise polynomial implication, not an extrapolation from finitely many values of $T$. The expanded coefficients themselves are supported by the supplied exact symbolic certificate; I have audited its defining algebra and source, not independently executed its arithmetic.

Combining (11) and (13),


$$
\boxed{c/3\equiv4+3M\pmod{27}\qquad(3\mid M,\ M\ge3).}
\tag{14}
$$



---

## 6. Explicit bounded rule for the whole local polynomial modulo $27$

For a completely specified univariate version of (12), expand


$$
\left(1+\frac32t\right)(1-9t)F_1(t)
=\sum_{h=0}^{20}\gamma_ht^h.
$$


Then


$$
\boxed{
\mathcal G(M)=
\sum_{h=0}^{20}\gamma_h
\sum_{a=0}^{h}\binom ha
\sum_{t=0}^{\min(a,h-a)}
C_{a,t}(M)C_{h-a,t}(M).}
\tag{15}
$$


Every range is at most $20$. There is no unresolved matrix inverse or Schur scalar.

The coefficient denominator bounds are:

- $f,F_0,F_1$: $3$-depth at most $2$, since $v_3(8!)=2$;
- $E_0$: depth at most $3$;
- $\mathcal G$: depth at most $2$.

Thus


$$
\mathcal G(M+243)\equiv\mathcal G(M)\pmod{27}.
\tag{16}
$$


Although coefficients may have denominators divisible by $3$, its values at nonnegative integers are $3$-integral by the exact contraction representation and (4). Evaluation should therefore be done exactly before reduction, or with sufficient guard precision.

Now take


$$
j\ge1,\qquad3\mid j,\qquad
N=4^j,\quad M=(N-1)/3,\quad n=N+1.
$$


The established factorial-tail elimination and deep endpoint correction bounds give


$$
3\eta_{\rm last}
\equiv
\mathcal G(M)(4+3M)^{-1}\pmod{27}.
$$


Because $3\mid M$,


$$
(4+3M)^{-1}\equiv7-12M\pmod{27}.
$$


Hence the entire local primitive ray has the explicit fixed-polynomial rule


$$
\boxed{
Q^{\rm loc}(y)=3P_n(y)
\equiv
(y+1)(y-1)^{N-1}
\left[
3(y-1)-N(7-12M)\mathcal G(M)
\right]\pmod{27}.}
\tag{17}
$$



This is an infinite-class theorem with an explicitly evaluated fixed contraction, rather than an unspecified $\Theta_M$. Its input depends on at most $M\bmod243$. Simplifying $\mathcal G(3T)$ further is the remaining bounded arithmetic task.

### The index $j=3$

Formula (17) already includes $M=21$, by Section 3. The supplied finite lift receipt reduces to


$$
c/3\equiv13,\qquad \xi_{\rm last}\equiv11\pmod{27}.
$$


Thus


$$
3\eta_{\rm last}\equiv11\cdot13^{-1}\equiv5\pmod{27},
$$


and


$$
3P_{65}(y)\equiv(y+1)(y-1)^{63}(3y+1)\pmod{27}.
$$


These numerical residues remain finite evidence from the supplied lift receipt; no infinite pattern is inferred from them.

For the actual primitive integer polynomial,


$$
\boxed{Q_n=(L_n/3)Q^{\rm loc},\qquad L_n/3\in\mathbb Z_3^\times.}
$$


The global primitive unit must not be discarded.

---

## 7. Actual denominator, whole error, and nonvanishing

The polynomial digits do not replace the complete determinant normalization. With the integer coefficient pair obtained from the complete matrix, retain


$$
g=\gcd(|A|,|B|),\qquad
q=\frac{|B|}{g},\qquad
p=-\frac{\operatorname{sgn}(B)A}{g}.
$$


On indices where $B\ne0$,


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B)}g\bigl(A+B(e+\pi)\bigr)
=
\frac{\operatorname{sgn}(B)\ell^k}{g}\det H_{\rm complete},
\qquad k=(n+1)/2.}
$$


This retains the entire rational arctangent contribution and both periods.

The supplied responses attribute $B\ne0$ and distinct centers on the regular family to inherited results not proved in the documents here. Conditional on those results, the whole errors are nonzero except possibly at one index. The present polynomial calculation independently establishes neither those complete-matrix assertions nor decay of the whole primitive error.

---

## Closing ledger

### (1) New result and proof status

**Proved by explicit identities:**

- The coordinator’s modulo-$27$ factorial and adjacent-factor formulas, with correct signs and $1/2$.
- The exact projection precisions $c\equiv R\pmod{81}$, $\xi_{\rm last}\equiv X\pmod{27}$ on $3\mid M$.
- The fixed contraction formula for every $M\ge0$, eliminating the proposed $M=21$ exception.
- Cancellation of the higher binomial corrections and reduction to the degree-$20$ polynomial $\mathcal G$.
- The explicit infinite-class local polynomial rule (17), with a modulus-$243$ input bound.

**Using the supplied exact $\mathcal H$ expansion, whose construction has been audited:**


$$
c/3\equiv4+3M\pmod{27}\quad(3\mid M),
$$


and therefore the clean earlier law $c/3=4,\ \xi_{\rm last}=2,\ 3\eta_{\rm last}=5\pmod9$.

### (2) Exact remaining bottleneck

For a simpler modulo-$27$ law, reduce the single explicitly defined polynomial $\mathcal G(3T)$.

For irrationality, the bottleneck remains substantially stronger: control the actual complete-center higher lifts, the final gcd, the actual reduced denominator, and the nonzero whole evaluated errors. The local polynomial theorem alone does not supply this.

### (3) One bounded symbolic computation request

**Input:** equations (3), (7), and (15), with maximum degree $20$.

**Requested verifiable output:**

1. Exact rational coefficients of $\mathcal G(M)$, with common denominator and its $3$-valuation.
2. Exact coefficients of $\mathcal G(3T)$, reduced coefficientwise modulo $27$ if individually $3$-integral.
3. If not coefficientwise integral, its exact Newton coefficients modulo $27$, retaining sufficient denominator precision.
4. The checks
   

$$
\mathcal G(21)\equiv11\pmod{27},\qquad
   \mathcal G(3T)\equiv2\pmod9.
$$


5. The resulting reduction of
   

$$
(7-36T)\mathcal G(3T)\pmod{27}.
$$



This is one fixed symbolic contraction, not a growing-degree scan.
