> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4, Turn 21 — Independent audit of the depth-$18$ residual, nilpotent recurrence memory, and finite weighted binary transforms

## Executive conclusions

The supplied packets do **not** prove or disprove the irrationality of


$$
e+\pi.
$$


They do contain several valid advances, provided their scopes are kept distinct.

1. **A1turn12:** On the accepted sufficiently large original depth-$16$ window, the proof of
   

$$
S_{\rm act}\in3^{18}M_\nu(\mathbb Z_3)
$$


   survives audit, using the previously accepted finite LOW/HIGH support-return results and precision-$11$ producer saturation at their stated scopes. Consequently,
   

$$
\Psi,\mathsf H\in9M_\nu(\mathbb Z_3).
$$


   The crucial point is that **support separation is used for the core corrected columns, not asserted for the jet-multiplied columns**. The latter are handled by a finite polynomial inverse-transfer identity. Its degree bound and precision are sufficient. Restoration of the complete producer remainder is division-safe.

2. **A2turn9:** The all-phase monodromy calculation is valid:
   

$$
\begin{array}{c|c|c}
   \text{starting phase modulo }29&\text{rank}&\text{nilpotence index}\\ \hline
   1&2&3\\
   0,2,\ldots,28&1&2.
   \end{array}
$$


   Both forgetting bounds are justified:
   

$$
59K
   \quad\text{from the coordinator’s all-phase \(59\)-step identity,}
$$


   and the sharper
   

$$
\boxed{58K+1}
$$


   from the phase-sensitive square-zero block argument. They agree at $K=1$; the second is stronger for $K>1$. Neither establishes Gram alignment.

3. **A5turn18:** The finite binomial transforms, weighted constant-term representations, and boundary-polynomial pairings are correct with the stated expansion conventions. The actual reconstruction matrix retains
   

$$
Q_{b-1,b-1}=W_{b-1}^2+b^2W_b^2.
$$


   The characteristic-zero Vandermonde obstruction is valid, but supplies **no corresponding full-rank theorem modulo $2^M$**.

4. **Coordinator binary receipt:** The source implements a bounded original-$u=0$, $M=20$ **operator and selected endpoint-identity audit**. It does not compute an original norm/mixed pair. In particular, its $2926$ endpoint comparisons concern the rational-series input $(1+x)^{-n}$; they do not independently test every possible boundary input or prove that all complete endpoint corrections vanish.

No tools were executed. I inspected only the supplied mathematical text and program listings. The reported PASS receipts are supplied finite evidence, not independently rerun computations or independently verified hashes.

---

## 1. Domains, dependencies, and overlap

The three original families must remain separate.

### A1: $3$-adic residual family

Retain


$$
n=4^j+1,\qquad j>0,\qquad81\mid j,
$$


and, for the new depth conclusions,


$$
j\equiv81\pmod{243},\qquad
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad
C_{16}=512\cdot17^2\,3^{15},
$$


with the accepted sufficiently-large qualifications. Here


$$
A=n-2=H-D,\qquad H=3^{h-1},
$$




$$
m=\frac{A+1}{2},\qquad d=\frac{3D}{2}-1,\qquad \nu=\frac D2-1.
$$


The finite basis remains


$$
U_u=(y-1)^u\quad(0\le u<D),
$$




$$
z_i=(y-1)^Dy^i\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m).
$$



### A2: $29$-adic family

Retain


$$
b=3^{249005515+574312172u},\qquad n=2001b,\qquad u\ge0.
$$


Contact coordinates are $0,\ldots,b-1$, recurrence rows are $1,\ldots,b-2$, and reconstruction includes $j=b$.

### A5: binary family

Retain


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
$$


Writing $b=128D+81$, the terminal contact block contains only residues $0,\ldots,80$, followed by the separate reconstructed endpoint $j=b$.

### Accepted results and literature scope

A4turn20’s acceptance of A1turn11 is preserved: determinant-one Krylov normalization, the unit resultant, integral Hankel transfer, complete endpoint transport, and the stated producer precision budget are not reopened or extended.

Likewise, established prime-power digit and rational-diagonal methods are reused as background. The cited work of Rowland–Yassawi, Bostan–Christol–Dumas, and the newer prime-power state-complexity paper does not, merely by its existence, provide a feasible state bound for the present parameter-dependent contact-inverted weighted kernels.

No archive search or external literature inspection was performed. Thus this report makes no exhaustive overlap or novelty claim.

---

# Part I. A1turn12

## 2. The complete functional and why the transfer loses no hidden digit

The functional remains


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\sum_{\substack{v\ge0\\2v+1\le4n-3}}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^r)=(2r)!.
$$



On the retained window, $4n-3<3^{h+1}=9H$. Every denominator in the displayed finite sum therefore has $3$-adic valuation at most $h$. Division of $F-F(-1)$ by the monic polynomial $y+1$ is integral. Consequently, on the bounded polynomial spaces in use,


$$
\mathcal M:\mathbb Z_3[y]\longrightarrow\mathbb Z_3
$$


is coefficientwise integral.

This matters twice:

- a coefficientwise congruence modulo $3^{19}$ can be passed through $\mathcal M$ without losing a digit;
- integrality of a Schur perturbation term must be established **before** a later normalization by $3^{18}$.

The source respects both requirements.

---

## 3. The $P=19$ core support-gap argument

### 3.1 What is being reused

Proposition 2.1 invokes the accepted finite supported-return formulas, including the original HIGH interval $d,\ldots,m$. The definitions of the support sets $I_\Omega,J_\Omega,\mathcal C_\Omega$ are not reproduced in the current packet; their previously accepted scope is therefore a dependency, not a new result independently reconstructed here.

The added support-width and upper-boundary estimates are internally consistent with those results.

For


$$
\Omega=\frac{H}{3^{P-1}},
$$


the binomial valuation identity


$$
v_3\binom Hk=h-1-v_3(k)
$$


implies the asserted grid support modulo $3^P$. The stated grid is conservative and sufficient.

The surviving lower-pole extraction indices lie on the corresponding half-grid. The width conditions separate the relevant supports from those extractions. The factorial term is omitted only after its coefficient $3^{h-1}$ is shown to vanish at the working precision.

### 3.2 Numerical separation on the original window

At $P=19$,


$$
\frac{\Omega}{D}>
\frac{C_{16}}{3^{18}}
=\frac{147968}{27}>5480.
$$


Thus the required inequalities have very substantial slack. In particular, with the retained $D\ge486$,


$$
\Omega>4D+2P+3
$$


and the upper-degree gap is much larger than $36$.

Accordingly, the finite core representatives satisfy


$$
\widehat z_i^{\,c}\equiv\phi_i=(y-1)^D\psi_i\pmod{3^{19}},
\qquad
\deg\phi_i\le m-36.
$$



### 3.3 Why the extra factor in $S_c$ is justified

The source uses


$$
g\longmapsto G_c(z_i,g)/3
$$


as an integral functional on the original degree-$\le m$ space. This is not an arbitrary division of an integral pairing:

- the potential unit-weight top contribution from $H_0$ is absent;
- the $H_1$ contribution already has its explicit factor $3$;
- the remaining normalized lower-pole terms have that factor.

Therefore


$$
\frac{G_c(z_i,\widehat z_j^{\,c})}{3}
\equiv
\frac{G_c(z_i,\phi_j)}{3}
\pmod{3^{19}}.
$$


The support-gap argument annihilates the right side at the stated precision, giving


$$
\boxed{S_c\in3^{20}M_\nu(\mathbb Z_3).}
$$



**Verdict:** valid at the accepted finite supported-return scope. No new HIGH coordinates or infinite-block inverse are introduced.

---

## 4. Does support separation survive actual jet multiplication?

Not necessarily—and the proof does not need it to.

This is the most important distinction in the A1 audit.

Let $x=y-1$ and


$$
R_{11}=(y+1)x^{A-27}B_{11}(x),\qquad \deg B_{11}\le27,
$$


with


$$
R\equiv R_{11}\pmod{3^{11}}.
$$


Define


$$
Q_*=Q_c+3^6R_{11},
\qquad c(y)=\beta+3y,
$$


and


$$
L(y)=\beta^{-1}\sum_{r=0}^{12}
\left(-\frac{3y}{\beta}\right)^r.
$$


Then


$$
cL-1\in3^{13}\mathbb Z_3[y].
$$



Put $a=x^{-27}B_{11}(x)$ formally and


$$
f_i=\phi_i\sum_{r=0}^{3}(-3^6aL)^r.
$$



### 4.1 Polynomiality and the actual finite upper boundary

Since $D\ge486>81$, each displayed term is a polynomial. Its degree is bounded by


$$
\deg\phi_i+r\bigl(\deg B_{11}-27+\deg L\bigr)
\le \deg\phi_i+12r.
$$


Hence


$$
\deg f_i\le\deg\phi_i+36\le m.
$$



The inverse transfer therefore remains inside the actual finite polynomial space. This is exactly where the strengthened upper-degree gap is needed.

### 4.2 Explicit error calculation

Set


$$
t=3^6aL,\qquad S=1-t+t^2-t^3.
$$


Then


$$
\begin{aligned}
(c+3^6a)S-c
&=c(1+t)S-c+(3^6a-ct)S\\
&=-ct^4+3^6a(1-cL)S.
\end{aligned}
$$


The first term has valuation at least $24$; the second at least $6+13=19$. After multiplication by $(y+1)x^A\phi_i$, all coefficients are integral. Thus


$$
\boxed{Q_*f_i\equiv Q_c\phi_i\pmod{3^{19}}.}
$$



The products involving $B_{11}$, $L$, or their truncated inverse need not retain the original half-grid support. The exact congruence transfers the calculation back to the core representative, where support separation has already been proved.

**Verdict:** the support concern is resolved by polynomial transfer, not by an unproved support claim about the actual inverse.

---

## 5. The saturated-jet Schur complement

The full ordered basis $[U,Z,Y]$ is an integral basis of polynomials of degree at most $m$: its elements are monic with successive degrees $0,\ldots,m$. Hence residual coordinate extraction is integral.

The accepted normalized eliminated-block estimates imply that the $Q_*$-corrected columns are integral and


$$
\widehat Z^*\equiv Z\pmod3.
$$


Also


$$
f_i\equiv z_i\pmod3.
$$


Thus the residual coordinate matrix $F_Z$ of the $f_i$ is a unit matrix modulo $3$.

For every degree-$\le m$ integral $g$,


$$
G_*(f_i,g)\equiv G_c(\phi_i,g)\pmod{3^{19}}.
$$


Taking $g=\widehat z_j^*$, the right side vanishes modulo $3^{19}$:

- replacing $\phi_i$ by $\widehat z_i^{\,c}$ costs only $3^{19}$;
- the exact core corrected column is orthogonal to $W$;
- its remaining pairing is through $S_c\in3^{20}M$.

Consequently,


$$
F_Z^TS_*\equiv0\pmod{3^{19}}.
$$


Since $F_Z$ is invertible over $\mathbb Z_3$,


$$
\boxed{S_*\in3^{19}M_\nu(\mathbb Z_3).}
$$



No inverse of the residual Schur complement is used. No inference of residual nonvanishing is made.

---

## 6. Restoration of the complete producer remainder

Define the whole integral remainder


$$
\Delta=\frac{R-R_{11}}{3^{11}},
\qquad
Q_{\rm act}=Q_*+3^{17}\Delta.
$$


The exact perturbation identity is


$$
S_{\rm act}
=
S_*+3^{17}\Phi_\Delta
-3^{34}T_\Delta^TE_{\rm act}^{-1}T_\Delta.
$$



This uses the actual eliminated block $E_{\rm act}$, not a truncated replacement.

### 6.1 The quadratic term

All entries of $T_\Delta$ are integral by the complete functional’s integrality. The accepted bound


$$
E_{\rm act}^{-1}\in3^{-1}M(\mathbb Z_3)
$$


therefore yields


$$
3^{34}T_\Delta^TE_{\rm act}^{-1}T_\Delta
\in3^{33}M.
$$



After division by $3^{18}$, it is still in $3^{15}M$. There is no unproved precision division here.

### 6.2 The linear term’s extra factor

For $0\le i<\nu$ and $\deg g\le m$,


$$
\deg(\Delta z_i g)\le
(A+1)+(d-1)+m
=\frac{3H-1}{2}=r_*.
$$


Its endpoint-subtracted quotient has degree at most $r_*-1$. The unique valuation-zero pole at extraction index $r_*$ is absent. Thus


$$
K_\Delta(z_i,g)\in3\mathbb Z_3.
$$



Writing


$$
\widehat Z^*=Z+3V_*,
$$


we obtain


$$
\begin{aligned}
\Phi_\Delta
&=K_\Delta(Z,Z)
+3K_\Delta(Z,V_*)
+3K_\Delta(V_*,Z)
+9K_\Delta(V_*,V_*)\\
&\equiv K_\Delta(Z,Z)\pmod9,
\end{aligned}
$$


and $\Phi_\Delta\in3M$.

Hence


$$
\boxed{S_{\rm act}\in3^{18}M_\nu(\mathbb Z_3).}
$$


Moreover,


$$
\boxed{
\Theta:=-S_{\rm act}/3^{18},
\qquad
\Theta_{ij}\equiv-\frac{\mathcal M(\Delta z_i z_j)}3\pmod3.
}
$$



Every division in this argument follows a demonstrated divisibility statement.

---

## 7. Exact coefficient window, all twenty features, and complete forcing

### 7.1 Evaluation of the first unsettled layer

For the residual products,


$$
\deg(\Delta z_i z_j)\le H+2D-3<r_*.
$$


Modulo $9$, the sole possible surviving pole below the top one is $H$, at


$$
r_1=\frac{H-1}{2}.
$$


It follows that


$$
\Theta_{ij}\equiv
-[y^{r_1}]
\frac{
\Delta(y)x^{2D}y^{i+j}
-\Delta(-1)(-2)^{2D}(-1)^{i+j}
}{y+1}
\pmod3.
$$



The endpoint subtraction is genuinely present at this stage.

Because


$$
\Delta(-1)=\frac{Q_{\rm act}(-1)}{3^{17}}
=-\frac{F^2\xi_n}{3^{17}},
$$


the accepted sufficiently-large condition gives $\Delta(-1)\equiv0\pmod3$. Define


$$
D_{\rm next}=\overline\Delta/(y+1)\in\mathbb F_3[y],
\qquad
P_{\rm next}=x^{2D}D_{\rm next}.
$$


Then


$$
\boxed{
\Theta_{ij}\equiv-[y^{r_1-i-j}]P_{\rm next}.
}
$$



There are exactly


$$
2\nu-1=D-3
$$


actual Hankel moments, indexed


$$
0\le k\le2\nu-2=D-4.
$$


The window is therefore exactly


$$
r_1-(D-4),\ldots,r_1.
$$



### 7.2 Independence of the lift

Changing $B_{11}$ by $3^{11}C$, $\deg C\le27$, changes $P_{\rm next}$ by


$$
-x^{H+D-27}C
=-(y^H-1)x^{D-27}C
\quad\text{over }\mathbb F_3.
$$


Its support lies below or at $D$, or at or above $H$, and misses the entire displayed window. The moment formula is lift-independent.

### 7.3 All twenty features

The accepted twenty-feature identity is an identity for the **whole**


$$
\Psi=-S_{\rm act}/3^{16}.
$$


Since $S_{\rm act}\in3^{18}M$,


$$
\Psi\equiv0\pmod9.
$$



This certifies cancellation of the full feature expression. It does not separately establish divisibility of any summand, and does not independently evaluate the twenty feature slots. In particular, no feature, terminal contribution, linear force, or core term may be dropped from the exact identity.

### 7.4 Hankel moments and forced recurrence

A1turn11’s accepted transfer has


$$
\mathsf H=\mathsf V^T\Psi\mathsf V,\qquad
\mathsf V\equiv I\pmod3.
$$


Therefore


$$
\boxed{\mathsf H\in9M,\qquad \mu_k\equiv0\pmod9
\quad(0\le k\le D-4).}
$$



The displacement identity, together with the unit last coordinate of $r_{\rm act}$, proves


$$
\frac{t_{\rm act}-\theta r_{\rm act}}{3^{18}}\in\mathbb Z_3^\nu.
$$


Thus the old complete forcing vector is divisible by $9$. The renormalized recurrence remains


$$
\mu_{i+\nu}^{[2]}+\sum_{k=0}^{\nu-1}f_k\mu_{i+k}^{[2]}
=b_i^{[2]},
\qquad0\le i\le\nu-2,
$$


with no extra final moment introduced.

Modulo $3$,


$$
\mu_k^{[2]}=-[y^{r_1-k}]P_{\rm next},
$$


and


$$
b_i^{[2]}=-[y^{r_1-i}]P_{\rm next}q_d,
\qquad0\le i\le\nu-2.
$$


The last component satisfies $b_{\nu-1}^{[2]}\equiv0\pmod3$ for the stated shear and normalization.

---

## 8. Endpoint action and determinant-pair rescaling

Since $\mathsf H\in9M$,


$$
\operatorname{rad}(\mathsf H\bmod3)
=\operatorname{rad}((\mathsf H/3)\bmod3)
=\mathbb F_3^\nu.
$$


At both layers the actual endpoint functional is


$$
x\longmapsto\sum_{i=0}^{\nu-1}(-1)^ix_i.
$$


Its first coordinate is $1$, so it is nonzero and its kernel has dimension $\nu-1$.

The full endpoint return is preserved:


$$
J^T\varepsilon+\omega
=
-\varepsilon-s\bigl(\theta e_{\nu-1}+3^{18}b^{[2]}\bigr).
$$


In particular,


$$
\omega_{\nu-1}\equiv q_d(-1)\pmod3
$$


must not be discarded.

For $\Psi=9\Theta$,


$$
\delta_0=3^{2\nu}\det\Theta,
$$


and


$$
\boxed{
\delta_1=3^{2\nu-2}
\left(
e_{\rm act}^T\operatorname{adj}(\Theta)e_{\rm act}
-3^{18}d_{\rm act}\det\Theta
\right).
}
$$


This follows from


$$
\operatorname{adj}(9\Theta)=9^{\nu-1}\operatorname{adj}(\Theta).
$$



When the relevant members are nonzero,


$$
v_3(\delta_1)-v_3(\delta_0)
=
-2+v_3(\Delta_1)-v_3(\Delta_0).
$$


The powers proportional to $\nu$ cancel in the ratio. Thus there is **no $2\nu$-digit primitive-denominator gain**.

### A1 status

The depth-$18$ divisibility and coefficient-window law are established at the accepted dependencies. What remains unproved is:

- the next actual producer digit or a uniform next-digit saturation bound;
- characteristic-zero residual nonvanishing;
- relative valuation of the complete determinant/cofactor difference.

A further zero layer alone would not solve the last two problems.

---

# Part II. A2turn9 and the coordinator’s $29$-adic certificate

## 9. All-phase monodromy

Modulo $29$, the transition matrices depend only on $i\bmod29$ whenever $29\mid n$. Their only singular phases are $0$ and $1$.

### 9.1 Phase $0$

The two-step reset gives the homogeneous state $(2,1,1)^Th_0$. Substitution verifies $h_r=r!h_0$ through the required block. Wilson’s theorem then gives


$$
B^{[0]}=
\begin{pmatrix}
0&0&0\\
-1&0&0\\
1&0&0
\end{pmatrix},
$$


which is nonzero, rank one, and square zero.

### 9.2 The exceptional phase $1$

The factorization


$$
1-z+\frac{z^2}{2}=(1-21z)(1-9z)
\quad\text{over }\mathbb F_{29}
$$


is correct. Thus


$$
u_r=\frac{21^{r+1}-9^{r+1}}{12},
\qquad
u_{27}=0,\quad u_{28}=1.
$$


The finite-logarithm identity used in the source gives


$$
\sum_{q=1}^{28}\frac{u_{q-1}}q=0.
$$



The exponential-generating-function argument should be understood as a characteristic-zero coefficient calculation followed by reduction of the resulting integral recurrence values. One must not define an unrestricted exponential generating function by dividing by $29!$ inside $\mathbb F_{29}$. With that interpretation, the calculation yields


$$
B^{[1]}=
\begin{pmatrix}
-1&1&0\\
-1&1&0\\
0&-1&0
\end{pmatrix},
$$


and


$$
(B^{[1]})^2=
\begin{pmatrix}
0&0&0\\
0&0&0\\
1&-1&0
\end{pmatrix}\ne0,\qquad
(B^{[1]})^3=0.
$$


Its rank is exactly two.

### 9.3 Phase $2$ and the remaining phases

The displayed phase-$2$ matrix is


$$
B^{[2]}=
\begin{pmatrix}
0&-2&2\\
0&-1&1\\
0&-1&1
\end{pmatrix}
=
\begin{pmatrix}2\\1\\1\end{pmatrix}(0,-1,1).
$$


The row annihilates the column, so it is square zero.

For phases $2,\ldots,28$, conjugation through the intervening invertible transitions is legitimate and proves rank one and square-zero monodromy. Together with phase $0$, this establishes the complete phase table.

---

## 10. Comparing $59K$ with $58K+1$

### 10.1 What the coordinator’s certificate proves

The program uses the correct multiplication orientation:


$$
T_{a+\ell-1}\cdots T_a.
$$


Its coefficients agree with the recurrence. The integer divisions by $2$ are exact because the relevant products have even numerators.

An exhaustive identity that every $59$-step word vanishes modulo $29$ proves, by grouping $K$ consecutive segments,


$$
\text{every word of length at least }59K
\text{ vanishes modulo }29^K.
$$


This is a uniform deduction from a finite exhaustive field identity, not an extrapolation from finitely many large original indices.

The reported $60$ higher-precision checks are corroboration only. They are not needed for this grouping proof.

### 10.2 Why the sharper bound is also valid

For a starting phase $a\ne1$, every consecutive $29$-step block reduces to the same square-zero matrix $B^{[a]}$. Actual higher-digit block matrices need not be equal; nevertheless each pair reduces to


$$
(B^{[a]})^2=0.
$$


Thus every $58$-step pair is divisible by $29$. Grouping $K$ such pairs gives zero modulo $29^K$ after $58K$ steps.

For starting phase $1$, remove the first step. The remaining interval starts at phase $2$, so $58K$ more steps suffice. Therefore


$$
\boxed{\text{every actual homogeneous word of length at least }58K+1
\text{ is zero modulo }29^K.}
$$



At $K=1$, length $58$ does not suffice uniformly because


$$
(B^{[1]})^2\ne0.
$$


Thus $59$ is the optimal uniform field-level bound. No optimality claim for $58K+1$ at every higher precision follows.

**Verdict:** the coordinator’s $59K$ bound is correct; A2’s sharper $58K+1$ bound is also proved.

---

## 11. Complete source at the actual $b=29B+27$

The source remains


$$
\mathcal H_i=
\sum_s a_s(n+1)(n+i)_{\underline s}
\binom{2n+i-s+1}{b}.
$$


Modulo $29$, falling-factorial divisibility removes $s\ge29$. For $s<29$, the coefficient identity


$$
\phi(z)^{n+1}\equiv\phi(z)\phi(z^{29})^{n/29}
\pmod{29}
$$


shows that only $s=0,1,2$ remain. Hence


$$
\mathcal H_i\equiv
\binom{2n+i+1}{b}
-i\binom{2n+i}{b}
+\frac{i(i-1)}2\binom{2n+i-1}{b}.
$$



Writing $n=29m$, $i=29q+t$, and $b=29B+27$, Lucas’s theorem gives:

- $t=26$: the first term contributes $\binom{2m+q}{B}$;
- $t=27$: the first two terms contribute $(-1)-27=1$ times that binomial;
- $t=28$: the second and third terms cancel;
- all other phases vanish.

Therefore


$$
\boxed{
\mathcal H_{29q+t}\equiv
\begin{cases}
\binom{2m+q}{B},&t=26,27,\\
0,&\text{otherwise}.
\end{cases}}
$$



The higher-digit dependence in this binomial is real. Substituting $n=203,b=839$ into the entire source would not preserve it.

The further condition $q\equiv14\pmod{29}$ follows from $m_0=7$ and $B_0=28$, but does not remove the remaining higher-digit binomial.

---

## 12. Affine blocks and the shortened endpoint

For a source-only phase-$0$ block, direct propagation of the equal impulses at phases $26,27$ gives


$$
(h_{29q+29},h_{29q+28},h_{29q+27})
=(0,-2\kappa_q,\kappa_q).
$$


The two reset steps annihilate this block-end state in the phase-$2$ organization. Thus the vanishing phase-$2$ affine contribution is correct.

It is not vanishing of the interior response:


$$
h_{29q+27}=\kappa_q,\qquad
h_{29q+28}=-2\kappa_q
$$


can remain nonzero.

The endpoint count is also correct:


$$
b-2=29B+25,\qquad
\#\{2,\ldots,b-2\}=29B+24.
$$


There are exactly $B$ complete phase-$2$ blocks and $24$ final steps. The last recurrence state reaches $h_{b-1}$, not $h_b$.

The reconstructed endpoint remains


$$
\boxed{Y_b=W_b(b\psi_{b-1}+1).}
$$



---

## 13. Rational kernels and finite-memory formula

The impulse weights


$$
q_d(j)=e_1^TT_{j-1}\cdots T_{j-d}e_1
$$


have the correct ordering and satisfy the stated recurrence. Their total degree in $n,j$ is at most $d$, because the transition coefficients have respective degrees $1,2,3$.

With


$$
H_K=58K+1,
$$


the source contribution is therefore


$$
\tau_j\equiv
\sum_{\ell=\max(1,j-H_K)}^{j-1}
q_{j-\ell-1}(j)\mathcal H_\ell
\pmod{29^K},
\qquad2\le j<b.
$$


This keeps exactly the possible nonzero propagator lengths $0,\ldots,H_K-1$.

The generating identity


$$
\sum_{i\ge0}\binom{n+i}s t^i
=
\sum_{k=0}^s\binom n{s-k}\frac{t^k}{(1-t)^{k+1}}
$$


is a direct Vandermonde consequence. It validates the source kernel and its pole-order bound $29K$.

The particular-input kernel applies a differential operator of degree at most $58K$, giving the stated bound


$$
87K.
$$



These are bounds on the indicated $z$-pole orders. They are **not** bounds on the complete reachable state dimension after parameter-dependent coefficient extraction, contact inversion, weighting, and summation.

The source’s warning about finite inversion is essential:


$$
\text{truncate the actual \(b\times b\) matrix first, then invert.}
$$


An inverse of an infinite generating kernel cannot silently replace that operation.

---

## 14. Actual weighted Gram and projection

The reconstruction gives


$$
L=\mathcal R^T\mathcal R,
$$


with


$$
L_{jj}=W_j^2+(j+1)^2W_{j+1}^2,
\qquad0\le j<b,
$$


and


$$
L_{j,j+1}=-(j+1)W_{j+1}^2,
\qquad0\le j<b-1.
$$


The last diagonal contains $b^2W_b^2$.

Also


$$
\mathcal R^T(W_be_b)=bW_b^2e_{b-1}.
$$


Consequently,


$$
\mathcal N=(f^0)^TA^{-T}LA^{-1}f^0,
$$




$$
\mathcal C=(f^0)^TA^{-T}LA^{-1}\mathbf r
+(f^0)^TbW_b^2A^{-T}e_{b-1}.
$$


These formulas retain the complete source and exterior endpoint.

The telescoping projection charges are correct:


$$
\ell^T\mathcal Rx=0,\qquad \ell^T(W_be_b)=W_b.
$$


Hence only the particular/particular Gram entry receives the subtraction


$$
W_b^2/\mathscr S.
$$



### The exact remaining local obstruction

The recurrence’s short memory does not make


$$
\Gamma=A^{-T}LA^{-1}
$$


local. The output sees interior source impulses through the full finite inverse.

The unresolved identity is therefore still


$$
\boxed{
\mathcal C-29\rho_n\mathcal N
\in29^2\mathcal N\mathbb Z_{29}.
}
$$


It must be tested at


$$
K=v_{29}(\mathcal N)+2,
$$


not merely at a fixed absolute modulus or from column content.

A concrete sufficient next lemma is A2’s endpoint-sensitive head-to-source kernel identity, with the shortened terminal lag range and exterior charge retained. The nilpotent homogeneous stable image cannot substitute for that lemma.

---

# Part III. A5turn18 and the original binary operator receipt

## 15. Finite transforms and weighted constant terms

The two transforms have different endpoints:


$$
(\mathcal T_U\kappa)(i)
=\sum_{j=i}^{b-1}\kappa(j)\binom{-n}{j-i},
$$




$$
(\mathcal T_L\kappa)(j)
=\sum_{i=0}^j(-1)^{j-i}\binom ji\kappa(i).
$$


The coordinate-kernel formulas follow immediately and are correct.

For


$$
K(i)=\binom{2n+i}{b},
$$


the finite binomial theorem gives


$$
\mathcal T_LK(j)
=[z^b](1+z)^{2n}z^j
=\binom{2n}{b-j}.
$$



For the other transform,


$$
\sum_{k=0}^{B}\binom{-n}{k}X^k
=[y^B]\frac{(1+Xy)^{-n}}{1-y},
$$


so


$$
\mathcal T_UK(i)
=
[z^by^{b-1-i}]
\frac{(1+z)^{2n+i}}
{(1-y)(1+(1+z)y)^n}.
$$


The factor $(1-y)^{-1}$ is indispensable.

For the weights,


$$
W_{j+a}W_{j+c}
=
\operatorname{CT}_{u,v}
(1+u)^{n+2}(1+v)^{n+2}u^{-a}v^{-c}(uv)^{-j}.
$$


This proves the weighted formulas upon finite summation.

The expansion convention should be stated explicitly: expand in the finite-target variable $y$ first; each requested coefficient is then a Laurent polynomial for which the indicated constant terms are unambiguous. No analytic evaluation of an infinite binomial series is involved.

---

## 16. Boundary-polynomial pairings and the original $Q$

For


$$
p_h(j)=(-1)^{h-j}\binom hj,
$$


with $0\le j\le h<b$,


$$
\sum_j\kappa(j)p_h(j)=\mathcal T_L\kappa(h).
$$


Thus the single-boundary formulas are exact.

For two boundary polynomials,


$$
p_h(j)p_k(j)=(-1)^{h+k}\binom hj\binom kj.
$$


The coefficient identity


$$
[t^k](1+t)^k(1+Xt)^h
=\sum_j\binom hj\binom kjX^j
$$


proves A5’s boundary-pair formula.

This pairing is the diagonal-weight pairing of the coefficient vectors. The full reconstruction Gram additionally has the stated tridiagonal structure:


$$
Q_{ii}=W_i^2+(i+1)^2W_{i+1}^2,
$$




$$
Q_{i,i+1}=-(i+1)W_{i+1}^2.
$$


In particular,


$$
\boxed{Q_{b-1,b-1}=W_{b-1}^2+b^2W_b^2.}
$$


Adjacent products $W_jW_{j+1}$ in an intermediate representation do not replace these squared weights.

No displayed A5 transform or boundary-pair identity fails under these conventions.

---

## 17. Vandermonde obstruction: exact scope

On the binary family, the positive binomials


$$
W_j=\binom{4002b+2}{j},\qquad0\le j<b,
$$


are strictly increasing. Thus $d_j=W_j^2$ are pairwise distinct.

If a rational vector space contains $v_j=(-1)^j$ and is closed under multiplication by $d_j$, it contains


$$
v,dv,\ldots,d^{b-1}v.
$$


Their determinant is a nonzero signed Vandermonde product. Therefore its dimension is $b$.

This rules out an unrestricted characteristic-zero closure of precision-sized rank.

It does **not** prove the analogous statement modulo $2^M$, because the Vandermonde determinant need not be a unit. The differences $d_j-d_i$ may have large binary valuations; distinct rational eigenvalues can become indistinguishable at finite precision.

The correct follow-on target remains a specialized modular, bounded-operation or output-compatible representation—not unrestricted exact closure under arbitrarily many weight multiplications.

---

## 18. What the original-$u=0$, $M=20$ program actually certifies

The input is genuinely original:


$$
b=9^{18}=150094635296999121,
$$




$$
n=4002b=600678730458590482242,
$$


with


$$
M=20,\qquad m=4(M-1)=76.
$$



### 18.1 Interior operator

The program constructs the symbol coefficients using divided-power convolution. It then computes the inverse coefficients through order $76$, verifies the filtration bounds, and checks the truncated product through order $152$.

There are


$$
2m+1=153
$$


inverse-product residual checks and


$$
2m=152
$$


filtration checks.

Calling these “153 inverse coefficients” would be inaccurate: the two stored coefficient lists each have $77$ entries. The number $153$ counts residual orders $0,\ldots,152$.

### 18.2 Endpoint identities

For $1\le s\le76$ and $0\le r<s$, put


$$
d=b+r-s.
$$


The comparison is


$$
\binom{b+r}{s}\binom{-n}{b+r}
=
\binom{-n}{s}\binom{-n-s}{d}.
$$


This is an exact generalized-binomial identity. Its signs and indices are correct.

The number of checks is


$$
\sum_{s=1}^{76}s=\frac{76\cdot77}{2}=2926.
$$



The program compares two routes to the high-index divided derivative coefficient of


$$
F(x)=(1+x)^{-n}.
$$


Thus the precise certified scope is:

> At the stated original input and modulus, the selected $2926$ boundary-return coefficients for this rational-series input agree under coefficientwise differentiation and the closed derivative formula.

The receipt reports that all these coefficients are zero modulo $2^{20}$.

That finite vanishing does **not** show that:

- the general endpoint commutator is zero;
- all boundary corrections for the complete adjoint input vanish;
- translation can be moved through truncation;
- the original norm or mixed scalar has been evaluated.

The general commutator remains the exact identity already accepted in Turn 20:


$$
P_b\partial^{[s]}F-\partial^{[s]}P_bF
=
\sum_{r=\max(0,s-b)}^{s-1}
\binom{b+r}{s}f_{b+r}x^{b+r-s}.
$$



### 18.3 Arithmetic implementation

The odd-factorial recursion and Legendre valuation formula in the listing provide a valid division-safe binomial evaluation modulo $2^{20}$: only odd units are inverted.

The largest declared residue table has $2^{20}+1=1{,}048{,}577$ entries. No original-length vector of size $b$ is allocated.

**Verdict:** a valid bounded operator/selected-endpoint implementation audit, not a norm-pair certificate.

---

# Part IV. Concrete next obligations and bounded calculations

## 19. A1: next producer digit and coefficient window

The next useful local lemma is:

> For the actual precision-$12$ producer, prove
> 

$$
> \overline\Delta=(y+1)(y-1)^{A-\kappa}C(y),
> \qquad
> 27\le\kappa\le D,\quad \deg C\le\kappa.
>
$$



If established, then


$$
P_{\rm next}
=(y^H-1)(y-1)^{D-\kappa}C
$$


has support in


$$
[0,D]\cup[H,H+D],
$$


which misses the whole moment window. This would prove one further zero layer. It would still not prove determinant nonvanishing or a favorable relative valuation.

### Bounded exact calculation

**Inputs:** a certified original tuple $(j,n,H,D,h)$ on the retained window, the actual $R\bmod3^{12}$, and the accepted precision-$11$ saturation data. Under the accepted producer budget, upstream precision $3^{19}$ suffices.

**Required output:**

1. zero remainder in the precision-$11$ saturation division;
2. coefficientwise divisibility before forming $(R-R_{11})/3^{11}$;
3. $\overline\Delta(-1)=0$;
4. the complete $D-3$ coefficient vector
   

$$
\left([y^{r_1-k}](y-1)^{2D}\frac{\overline\Delta}{y+1}\right)_{k=0}^{D-4};
$$


5. complete forcing residues, including the terminal component check.

No numerical result for that vector is predicted here. One original input establishes only that input’s next layer unless a uniform tail lemma is proved.

---

## 20. A2: a sharper implementation check and the actual output bottleneck

A small check can inspect the sharpened bound without pretending to evaluate source binomials.

**Inputs:**


$$
n\equiv203\pmod{841},\qquad K=2,
$$


and starting indices $a=0,\ldots,28$.

**Comparisons:**

- for $a\ne1$, products of length $116$ should be zero modulo $841$;
- for $a=1$, the product of length $117$ should be zero modulo $841$;
- retain the actual pair products modulo $841$, not merely their zero reductions modulo $29$.

These are bounded transition checks. They do not permit substituting small representatives for the actual high-index source.

The decisive calculation is still the actual pair


$$
\mathcal N,\mathcal C
$$


at a modulus that reaches the first nonzero norm digit. A declared $K_{\max}$ is legitimate, but if the norm remains zero at that modulus, the result is inconclusive.

A useful symbolic follow-on lemma would telescope the actual head-to-source kernel, including $A^{-1}$, $W_j^2$, the shortened last block, and the exterior endpoint, to establish or refute the relative congruence.

---

## 21. A5: weighted reductions versus the missing scalar evaluation

The proposed auxiliary checks at


$$
(b,n)=(81,324162),\qquad(209,836418),
$$


modulo $2^{20}$, are well specified as kernel tests.

**Expected output:** zero discrepancies for the finite transforms, weighted boundary pairings, and especially the terminal diagonal $b^2W_b^2$.

They do not replace the missing original-$u=0$ weighted state construction.

The next required lemma must provide:

- explicit modular states and transitions for the actual weighted coefficient extractions;
- a numerical reachable-state bound at $M=20$;
- closure under the required finite adjoint and boundary operations;
- preservation of all expansion conventions and endpoints;
- sufficient precision to detect the actual norm and mixed valuations.

The complete mixed force, not merely its $s=t=0$ channel, must enter. The logarithmic force may be omitted only under its proved budget. The exterior term


$$
W_b\mathsf a_b
$$


must remain in the mixed contraction.

---

# Part V. Primitive denominators and whole evaluated errors

## 22. A1 determinant route

Let


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


using the least actual clearer, and


$$
g_\ell=\gcd(|A_\ell|,|B_\ell|).
$$


When $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},
\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


The whole evaluated error is


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{g_\ell}
\det H_{\rm complete}.
}
$$



Every prime remains in the gcd. The depth-$18$ normalization does not establish the least clearer, the full gcd, or nonvanishing and decay of this whole expression.

---

## 23. A2 and A5 Gram routes

Retain the least actual two-column clearer $d_B$, the actual integer Gram pair, and


$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=\frac{A_B}{g_B},\qquad
p_n=\frac{H_B}{g_B}.
$$


The primitive multiplier is


$$
d_B^2/g_B.
$$



The local denominator interfaces remain, at their accepted scopes,


$$
v_{29}(q_n)
=
\max\{0,\ 2F_n-F_b-1+\delta-\mu\}
$$


for A2, and


$$
v_2(q_n)=
\max\left\{
0,\frac{3n}{2}-v_2(b!)-s_2(n)-1-(\gamma-\alpha)
\right\}
$$


for A5.

Neither new packet determines the needed original relative valuation. Even if it did, the other primes would remain.

For


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


the relevant quantity is always


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
$$


The accepted signed-error asymptotics concern $\epsilon_n$; irrationality by these routes requires a same-index bound on the actual primitive $q_n$ that forces the **whole nonzero evaluated error** to zero.

---

## 24. Final proof-status ledger

| Claim | Audit result |
|---|---|
| A1 $P=19$ core support gap | Valid using accepted complete finite return formulas |
| A1 support preserved under actual jet multiplication | Not needed and not asserted |
| A1 polynomial inverse transfer | Proved; degree $\le m$, precision $3^{19}$ |
| A1 saturated-jet Schur complement | $S_*\in3^{19}M$, division-safe |
| A1 complete producer restoration | Exact and retained |
| A1 actual depth-$18$ residual divisibility | Established at accepted dependencies |
| A1 all twenty features | Whole-expression cancellation; no termwise deletion |
| A1 exact next coefficient window and forcing | Correct |
| A1 endpoint action and terminal return | Correct and retained |
| A1 determinant-pair rescaling | Correct; no dimension-multiplied denominator gain |
| A1 residual nonvanishing/relative valuation | Open |
| A2 exceptional phase $1$ rank/index | Exactly rank $2$, index $3$ |
| A2 other phases | Rank $1$, square zero |
| Coordinator $59K$ forgetting | Justified |
| A2 $58K+1$ forgetting | Justified and sharper for $K>1$ |
| A2 complete source and shortened endpoint | Correct |
| A2 rational kernels and $87K$ pole bound | Correct at their stated kernel scope |
| A2 projected weighted Gram | Correct |
| Recurrence forgetting implies Gram alignment | Invalid inference |
| A5 finite transforms and constant terms | Correct |
| A5 boundary pairings and terminal $b^2W_b^2$ | Correct |
| A5 characteristic-zero rank obstruction | Proved |
| Same rank obstruction modulo $2^M$ | Not established and does not follow |
| Original binary $M=20$ receipt | Operator/selected-endpoint audit only |
| Original binary norm/mixed certificate | Not supplied |
| Full gcd, primitive denominator, whole-error comparison | Open |

## Conclusion

The principal new local result survives:


$$
\boxed{
S_{\rm act}\in3^{18}M_\nu(\mathbb Z_3),
\qquad
\mathsf H\bmod3=0,
\qquad
(\mathsf H/3)\bmod3=0.
}
$$


The first unsettled normalized residual form is explicitly the actual producer coefficient window described above.

Independently, the recurrence audit certifies


$$
\boxed{\text{uniform homogeneous forgetting after }58K+1\text{ steps modulo }29^K,}
$$


with a genuine rank-two/index-three exception at phase $1$. This sharpens memory, not weighted output alignment.

The binary packet establishes exact weighted transform identities and a useful characteristic-zero obstruction. The supplied original-$u=0$ computation reaches the interior operator and selected endpoint identities, not the original scalar pair.

The exact remaining bottlenecks are:

1. **A1:** evaluate or control the next actual producer digit, then establish nonvanishing and relative valuation of the complete determinant/cofactor difference.
2. **A2:** prove or refute the endpoint-sensitive weighted output congruence at the true first nonzero norm digit.
3. **A5:** construct and bound a usable modular weighted state system and evaluate the complete original raw outputs at norm-sensitive precision.
4. **Every route:** control the least clearer, final all-prime gcd, actual primitive denominator, and whole nonzero evaluated error on the same original indices.



$$
\boxed{\text{An unconditional proof or disproof of irrationality of }e+\pi
\text{ remains unresolved.}}
$$


