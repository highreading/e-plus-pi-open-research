> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 — next $29$-adic defect and audit of the third saturation

No conclusion about the rationality or irrationality of $e+\pi$ follows.

I obtain two new results.

1. **The previously uncomputed part of the normalized $Q$-column can be evaluated.** Besides the established triples, there is an additional carry term at coordinates $29^2v-2$. Including this term proves
   

$$
\boxed{
   Z_w\in29^2\mathbb Z_{29}^{b+1},
   \qquad
   V_w/b!\in29^3\mathbb Z_{29}^{b+1}
   }
$$


   on
   

$$
a\equiv432827\pmod{682892}.
$$


   In particular, the next defect satisfies $E_1\equiv0\pmod{29}$ on that entire original-index class. This is a new whole-$Q$-column conclusion, not an inference from its triple projection.

2. **A4 turn 13’s third-saturation cancellation passes, with one proof repair.** Its particular asserted modulo-$27$ constant $10-9u$ need not be assumed. A weaker modulo-$27$ core, sufficient for every cancellation, follows from A1 turn 9’s actual divided-basis normalization. The extension of the first Hankel rank statement to the extra coordinate $y^d$ also needs—and admits—an explicit recurrence check. The actual final-gcd lower bound is then
   

$$
\boxed{v_3(g)\ge3D-4.}
$$



I do **not** obtain an all-depth equality of the $29$-adic norm and mixed valuations, or an $O(b)$ relative-loss bound.

---

## I. The full first normalized $Q$-digit

Throughout this section,


$$
p=29,\quad b=3^a,\quad n=2001b,\quad
a\ge1,\quad a\equiv31\pmod{812},\quad m_w=1.
$$


Write


$$
n=pN,\qquad b=pB+27,\qquad
B+1=pK.
$$


Thus


$$
N\equiv7\pmod p,\quad B\equiv28\pmod p,\quad B\ \text{is even}.
$$


Also put


$$
N=7+pN_1,\qquad N_1\equiv24\pmod p.
$$



Retain the exact integers


$$
T_q=\frac1p\binom Nq\binom{2N+B-q}{B-q},
\qquad 0\le q\le B,
$$


and set


$$
t_q=(-1)^qT_q,\qquad t_{B+1}=0.
$$


The divisions by $p$ are those already justified on this original class.

The actual normalized columns are


$$
P=\frac{Z_w}{p},\qquad
Q=\frac{Y}{p^2},\qquad Y=\frac{V_w}{b!}.
$$



### 1. New full-column formula

The established triple formula is


$$
(Q_{pq},Q_{pq+1},Q_{pq+2})
\equiv6t_q(1,2,-2)\pmod p.
$$



The remaining coordinates satisfy


$$
\boxed{
Q_{pq+27}\equiv R_q\pmod p,\qquad 0\le q\le B,
}
\tag{1}
$$


where


$$
\boxed{
R_q=
-6t_{q+1}
-\frac K{12}\,
\mathbf1_{p\mid q+1}
\binom{N_1}{(q+1)/p}
\binom{-2N_1-1}{K-(q+1)/p}
\quad\pmod p.
}
\tag{2}
$$


Every coordinate outside these triples and these residue-$27$ positions is zero modulo $p$.

The case $q=B$ in (1) is the actual endpoint $j=b$. Thus the endpoint is included, not discarded.

The extra term in (2) is invisible at the interior residue-$27$ coordinates of the auxiliary $b=839$ example, because there $B=28$. It does occur at that example’s endpoint.

### 2. Why the genuine contact correction does not alter these coordinates

Use the combined finite-boundary correction from A2 turn 11:


$$
\theta-\theta_{\rm base}
\equiv pT(-2n)F_1\pmod{p^2},
$$


where, modulo $p$,


$$
F_1(k)=(-1)^k A(k),\qquad
\deg A\le p-1,
$$


and $F_1$ is supported on low residues $27,28$.

For either $s=27$ or $28$, the actual finite upper boundary is $q\le B-1$. Consequently


$$
(T(-2n)F_1)_{pq+s}
\equiv
(-1)^{q+s}A(s)
\binom{2N+H-1}{H-1}\pmod p,
\qquad H=B-q.
\tag{3}
$$


There is no $q=B$ row of low residue $27$ or $28$ in the length-$b$ inverse.

For $3\le s\le28$, a unit first weight digit


$$
W_{pq+s}/p
$$


requires $q\bmod p\le6$. Then $H\bmod p\ge22$, and the binomial in (3) vanishes by its next digit. If the first weight digit is nonunit, the weight already supplies a second factor of $p$.

Thus the contact correction contributes zero to the weighted column modulo $p^3$ outside the established triples. This uses the actual finite correction equation; it does not replace the inverse by the base inverse.

### 3. Evaluation at residue $27$

Let


$$
X=-2N,\qquad j=pq+27,\qquad H=B-q.
$$


For $q<B$, the unit factorial block gives, to the needed precision,


$$
\theta_j=f_{pH+1}-(1+pX)f_{pH},
\qquad f_r=\binom{pX}{r}.
$$


The second factorial block is divisible by $p^2$; multiplication by $W_j\in p\mathbb Z_p$ makes it zero modulo $p^3$.

Using the adjacent binomial ratios in the reconstruction,


$$
j\theta_{j-1}-\theta_j
=f_{pH}(1+p\,\text{\(p\)-integral quantity})
\pmod{p^2}.
$$


Moreover,


$$
v_p(W_jf_{pH})\ge2.
$$


Indeed, if $W_j/p$ is a unit, the low digit of $H$ is at least $22$, whereas $X\bmod p=15$. Otherwise the weight supplies the second factor. Hence


$$
Y_{pq+27}\equiv W_{pq+27}\binom{pX}{pH}\pmod{p^3}.
\tag{4}
$$



Put $r=q+1$. The exact factorial ratio is


$$
\frac{\binom{pN+2}{pr-2}}{\binom{pN}{pr}}
=
\frac{(pN+2)(pN+1)\,pr(pr-1)}
{\prod_{\ell=1}^{4}(p(N-r)+\ell)}.
$$


After using the divisibility just established, only its first digit is needed:


$$
W_{pq+27}\binom{pX}{pH}
\equiv
-\frac{pr}{12}\binom Nr\binom XH
\pmod{p^3}.
\tag{5}
$$


The prime-block congruences are applied modulo $p^2$, before the final division.

Since $r+H=pK$,


$$
r\binom XH
=pK\binom XH-X\binom{X-1}{H-1}.
$$


Dividing (5) by $p^2$ therefore gives


$$
Q_{pq+27}
\equiv
-\frac N6(-1)^{q+1}T_{q+1}
-\frac K{12}\binom N{q+1}\binom{-2N}{B-q}
\pmod p.
\tag{6}
$$


Here $-N/6\equiv-6\pmod{29}$.

The product in the second term can be nonzero modulo $p$ only if $q+1\equiv0\pmod p$. Lucas reduction then gives exactly the second term in (2).

At $q=B$, direct evaluation of the endpoint weight gives


$$
\frac{W_b}{p^2}
\equiv-\frac K{12}\binom{N_1}{K}\pmod p,
$$


which is again (2), with $t_{B+1}=0$.

### 4. The other low residues

For $3\le s\le26$, the base solution after division by $p$ is a unit rational multiple of


$$
\binom{-2N-1}{B-q}.
$$


At a unit first weight digit, its lower low digit is at least $22$, giving zero. The contact correction was handled above.

For $s=28$, the leading reconstructed term cancels. More explicitly, its base reconstruction is divisible by $p$, and at a unit first weight digit its remaining binomial is again zero. Thus $Q_{pq+28}=0\pmod p$.

This completes the full-column formula.

---

## II. Evaluation of the orthogonal contribution and $E_1\bmod29$

Let


$$
J=C_n=\operatorname{CT}(t^{-1}+2+2t)^n,
\qquad c=\frac1{6J},
$$


with $J$ the actual $29$-adic unit, not a residue representative.

On every triple define


$$
e=(-1,2,-1)^T,\qquad
g=(11,2,-7)^T.
$$


Then


$$
e^Te=6,\qquad e^Tg=0,
$$


and


$$
6(1,2,-2)^T=5e+g.
$$



Choose the following exact $p$-integral reference columns:

* $P_0$ has triple $Jt_qe$, and is zero elsewhere;
* $Q_0$ has triple $t_q(g+e/6)$;
* at $pq+27$, $Q_0$ has the exact $p$-integral lift $R_q$ defined by the right side of (2);
* $Q_0$ is zero elsewhere.

Since $5\equiv1/6\pmod{29}$, the full-column theorem implies that


$$
\mathcal A=\frac{P-P_0}{p},\qquad
\mathcal B=\frac{Q-Q_0}{p}
$$


are actual integral $p$-adic columns.

Importantly,


$$
P_0^TQ_0=cP_0^TP_0
$$


holds **exactly**, not just modulo $p$.

### 1. Explicit next-defect residue

Expanding the actual contractions gives


$$
\boxed{
\begin{aligned}
E_1\equiv{}&
J\sum_{q=0}^{B}t_q\,e^T\mathcal B_{[q]}\\
&+\sum_{q=0}^{B}t_q\,(g-e/6)^T\mathcal A_{[q]}
+\sum_{q=0}^{B}R_q\,\mathcal A_{pq+27}
\pmod p.
\end{aligned}}
\tag{7}
$$


Here $[q]$ denotes the triple $pq,pq+1,pq+2$. Every endpoint contribution is in the last sum.

This is the coordinate form of


$$
E_1=\frac{P^TQ-cP^TP}{p}.
$$



### 2. The orthogonal contraction is no longer an unspecified scalar

With the exact orthogonal idempotent from A2 turn 11,


$$
U_\perp=(I-\Pi)P/p,
$$


the full $Q$-digit gives


$$
\boxed{
U_\perp^TQ_\perp
\equiv
\sum_{q=0}^{B}t_q\,g^T\mathcal A_{[q]}
+\sum_{q=0}^{B}R_q\,\mathcal A_{pq+27}
\pmod p.
}
\tag{8}
$$


Thus the missing orthogonal term consists of:

* the explicit triple direction $g$;
* the explicitly evaluated carry term (2);
* the next actual $P$-digit.

There is no unknown $Q_\perp$-scalar left in (8). Nevertheless, evaluating the next $P$-digit at all original indices remains necessary. Formula (8) alone is not a Gram-divisibility theorem.

---

## III. Specialization to the whole-column-zero class

Now impose


$$
a\equiv432827\pmod{682892}.
$$


Use the established low digits


$$
b\equiv(27,28,5,28)_{29}\pmod{29^4}.
$$


Write


$$
B=28+pC,\quad C=5+pD_0,\quad D_0\equiv28\pmod p.
$$


Then


$$
K=C+1=6+pD_0,
$$


and


$$
N_1=24+pN_2,\qquad N_2=68+69C\equiv7\pmod p.
$$



The established $P$-column theorem gives $t_q\equiv0\pmod p$ for every $q$. What remains in (2) is


$$
\binom{N_1}{v}\binom{-2N_1-1}{K-v}.
\tag{9}
$$



### 1. The extra $Q$-carry term also vanishes

The two low upper digits in (9) are $24$ and $9$. Since $K\bmod p=6$, an addition carry would require a digit sum $35$, exceeding $24+9=33$. Thus every nonzero term must have no carry in this digit.

After removing it, the two upper indices are


$$
N_2,\qquad -2N_2-2.
$$


Their low digits are $7$ and $13$, while the required lower digit sum is $D_0\bmod p=28$. Neither a no-carry sum $28$ nor a carry sum $57$ is possible from digits bounded by $7,13$.

Therefore (9) is zero for every $0\le v\le K$. This includes the endpoint $v=K$.

The full-column result is consequently


$$
\boxed{
Q=Y/p^2\in p\mathbb Z_p^{b+1}.
}
\tag{10}
$$



Together with the established $P$-column divisibility:


$$
\boxed{
P\in p\mathbb Z_p^{b+1},\qquad
Q\in p\mathbb Z_p^{b+1}.
}
\tag{11}
$$



### 2. Consequences for the actual defect and first possible scalar digits

Equation (11) proves


$$
\boxed{E_1\equiv0\pmod p}
\tag{12}
$$


on the entire stated original exponent class.

Define the exact columns


$$
\widehat P=\frac{Z_w}{p^2},\qquad
\widehat Q=\frac{Y}{p^3}.
$$


Then


$$
\boxed{
\mathfrak D=p^4\widehat P^T\widehat P,\qquad
\Xi=p^5\widehat P^T\widehat Q.
}
\tag{13}
$$



Thus the first potentially nonzero scalar digits are


$$
\widehat P^T\widehat P\pmod p,\qquad
\widehat P^T\widehat Q\pmod p,
$$


not the earlier $\mathfrak D/p^4,\Xi/p^4$ pair.

For a completely explicit next-digit expression, write $t_q=ps_q$ and $R_q=pr_q$. Then


$$
\widehat P_{[q]}\equiv Js_qe+\mathcal A_{[q]},
\qquad
\widehat Q_{[q]}\equiv s_q(g+e/6)+\mathcal B_{[q]},
$$


and, at residue $27$,


$$
\widehat P_{pq+27}\equiv\mathcal A_{pq+27},
\qquad
\widehat Q_{pq+27}\equiv r_q+\mathcal B_{pq+27}.
\tag{14}
$$


All other coordinates use the corresponding $\mathcal A,\mathcal B$ entries.

Equations (14), followed by the complete coordinate sums, determine the two scalar digits. **I have not simplified those sums to a unit/zero law on this exponent class.** In particular, (12) is proved, but Gram-divisibility of $E_1$ is not.

---

## IV. Complete precision-four input for (7) and (14)

The following retains both earlier factorial blocks, the next block, and the actual cubic inverse.

Put


$$
d_s=s![z^s](1-z+z^2/2)^n,\qquad
F_d=\frac{(b+d)!}{b!}.
$$


The proved bound


$$
v_p(d_s)\ge1+v_p((s-1)!)
$$


permits the cutoff $s\le87$ modulo $p^4$.

Because $b+2=p^2K$,

* $F_0,F_1$ are units;
* $v_p(F_d)\ge2$ for $2\le d\le30$;
* $v_p(F_d)\ge3$ for $31\le d\le59$;
* $v_p(F_d)\ge4$ for $d\ge60$.

Moreover,


$$
\boxed{
F_d/p^3\equiv K(d-31)!\pmod p,
\qquad31\le d\le59.
}
\tag{15}
$$



The complete residual is therefore


$$
\boxed{
\begin{aligned}
r_i^{(4)}\equiv{}&
\sum_{s=0}^{87}d_s\binom{n+i}{s}
 \left[
 \binom{2n+i-s}{b}
 +(b+1)\binom{2n+i-s}{b+1}
 \right]\\
&+\sum_{d=2}^{30}F_d
 \sum_{s=0}^{29}d_s\binom{n+i}{s}
                  \binom{2n+i-s}{b+d}\\
&+p^3K\sum_{d=31}^{59}(d-31)!
                  \binom{2n+i}{b+d}
\pmod{p^4}.
\end{aligned}}
\tag{16}
$$


The middle block must retain its exact factorial quotients to the required precision. Replacing it only by its leading $p^2$-digit would not compute $E_1$.

For the complete logarithmic forcing, retain


$$
v_p(h_i^F/b!)
\ge F_n-F_b-\lfloor\log_p(2n+b-1)\rfloor.
\tag{17}
$$


This is at least $4$ throughout the assigned class. For example,


$$
F_n\ge69b,\quad F_b\le b/28,\quad
\lfloor\log_{29}(4003b-1)\rfloor\le b
$$


for $b\ge4$, more than suffices. Thus it is the **whole** logarithmic forcing, with its bound (17), that is omitted modulo $p^4$.

Define the actual finite matrix


$$
E^*_{kj}
=\sum_{s=1}^{87}\frac{d_s}{p}
 \binom{j+s}{s}\binom n{j+s-k}\pmod{p^3},
\qquad0\le k,j<b,
$$


and $\mathcal E=E^*T(-n)$. Then


$$
\boxed{
T(-n)\widetilde N^{-1}
\equiv
T(-2n)
\bigl(I-p\mathcal E+p^2\mathcal E^2-p^3\mathcal E^3\bigr)P_{\rm Pascal}^{-1}
\pmod{p^4}.
}
\tag{18}
$$


The matrix order and the cubic term are essential.

Applying (18) to the actual $P$-forcing and to (16), then applying the weighted reconstruction and the endpoint, supplies precisely the digits in (7) and (14).

These formulas admit an exact digit-recursive implementation: factorial valuations satisfy


$$
V(m)=\lfloor m/p\rfloor+V(\lfloor m/p\rfloor),
$$


and stripped factorial units satisfy


$$
U_k(m)=
\left(\prod_{\substack{1\le r\le m\\p\nmid r}}r\right)
U_k(\lfloor m/p\rfloor)\pmod{p^k}.
$$


The unit product is periodic in blocks of length $p^k$, with complete-block product $-1$. Negative-upper binomials are first converted to positive-upper binomials.

This is an exact, growing-dimensional carry evaluation, not a proved bounded-state scalar recurrence in the digits of $a$. That latter simplification remains open.

---

## V. Audit of A4 turn 13

### 1. A sufficient modulo-$27$ core follows from A1 turn 9

A4 turn 13 uses


$$
Q^{\rm loc}\equiv(y+1)(y-1)^A(3y+10-9u)\pmod{27}.
$$


The supplied A1 turn 9 does not derive that particular constant uniformly. Fortunately, the rank-zero proof needs only


$$
\boxed{
Q^{\rm loc}=3P_n
\equiv(y+1)(y-1)^A(3y+\beta)\pmod{27},
\qquad \beta\equiv1\pmod3.
}
\tag{19}
$$



Here is a derivation from its actual normalization.

Write


$$
N=4^j,\quad A=N-1=3M,\quad 3\mid j.
$$


Then $3\mid M$ and $v_3(A)\ge2$. A1’s actual projection coefficients satisfy $3\eta_i\in\mathbb Z_3$. Its tensor elimination also gives:

* the reduction of the eliminated last-column vector is supported at divided indices $3q$;
* at its final such index $3M-3$, the coefficient is a unit multiple of
  

$$
(B_M^{-1}k)_{M-1}=M,
$$


  hence is zero modulo $3$.

In


$$
3P_n
=3h_n-3N!\eta_{\rm const}
-\sum_{d=0}^{N-1}\frac{N!}{d!}(3\eta_{d+1})h_{d+1},
$$


all terms with $d\le N-2$ vanish modulo $27$:

* for $d=N-2,N-3$, the tensor support supplies the additional factor $3$;
* for $d=N-4$, the coefficient $M\equiv0\pmod3$ supplies it;
* for $d\le N-5$, the factorial quotient contains both $A$ and $A-3$, and already has valuation at least $3$.

The constant term vanishes by A1’s proved deep endpoint divisibility. Thus, with $\theta=3\eta_{\rm last}$,


$$
3P_n\equiv(y+1)(y-1)^A\bigl(3(y-1)-N\theta\bigr)\pmod{27}.
$$


Since $\theta\equiv2\pmod3$ and $N\equiv1\pmod3$, (19) follows.

Every cancellation below is independent of $\beta\bmod27$. This removes the need to assume the stronger, unevaluated constant law.

### 2. Frobenius grid: passed

For $H=3^s$, $s\ge2$, and $K_0=H/9$,


$$
\begin{aligned}
(y-1)^H\equiv{}&
y^H-1+9y^{K_0}-9y^{2K_0}
+3y^{3K_0}+9y^{4K_0}\\
&-9y^{5K_0}-3y^{6K_0}
+9y^{7K_0}-9y^{8K_0}\pmod{27}.
\end{aligned}
\tag{20}
$$


A direct proof of the reduction to the degree-nine polynomial is


$$
(y-1)^{3t}
=\bigl((y^3-1)-3y(y-1)\bigr)^t
\equiv(y^3-1)^t\pmod{27}
$$


when $9\mid t$. Iterate until $t=9$, then expand $(x-1)^9$.

Thus both the grid support and all displayed coefficients pass.

### 3. All pole cuts: passed

On the strong subclass


$$
D<H/36,\quad A=H-D,\quad h\ge5,
$$


the actual cutoff is


$$
4n-3=4H-4D+5.
$$


The surviving pole-unit lists are:



$$
\begin{array}{c|c}
\text{denominator scale}&\text{units}\\ \hline
3H&1\\
H&1\\
H/3&1,5,7,11\\
H/9&1,5,7,11,13,17,19,23,25,29,31,35.
\end{array}
\tag{21}
$$


Lower levels vanish modulo $27$ after the LOW division. The factorial term likewise vanishes because its valuation there is at least $h-1\ge4$.

The top pole is identically absent from LOW–LOW by degree; this is why modulo $27$, rather than modulo $81$, is sufficient for that block.

Endpoint subtraction remains part of the exact functional. Dividing the endpoint-subtracted difference of two polynomial cores by $y+1$ preserves its coefficientwise divisibility.

### 4. Direct LOW annihilation: passed

For $z_i=y^i(y-1)^D$ and a LOW monomial $y^a$,


$$
(y-1)^Az_i y^a=y^{i+a}(y-1)^H,
\qquad i+a\le2D-4.
$$


The strict inequality $D<H/36$ excludes:

* every $H/9$-grid contribution at the first pole;
* every $H/3$-grid contribution at all $h-2$ poles;
* both $0,H$ support positions at every $h-3$ pole.

The extra factor $3y+\beta$ in (19) does not change the conclusion. Hence


$$
Z^TL\equiv0\pmod{27}.
\tag{22}
$$



### 5. Exact HIGH inverse perturbation: passed

With A4’s notation,


$$
V=Z^TX\equiv-2ee_m^T+3K\pmod9.
\tag{23}
$$


The top pole contributes the corner $ee_m^T$. The first lower pole contributes $3K-3ee_m^T$. The $h-2$ pole contributions cancel in the $1,7$ pair, while $5,11$ lie outside the coefficient range.

The value of $\beta\bmod9$ does not alter (23): the $K$-term has a factor $3$, and $\beta\equiv1\pmod3$.

For the integral anti-triangular representative $E_0$,


$$
E_0^{-1}e_m=e_d,\qquad(E_0^{-1})_{mm}=0
$$


hold exactly. If $E=E_0+3E_1$, degree excludes the top-pole lift from $(E_1)_{dd}$, giving


$$
(E_1)_{dd}\equiv L_{dd}\pmod3.
$$


Therefore


$$
\frac{(E^{-1})_{mm}}3\equiv-L_{dd}\pmod3.
$$


Since $Ke_d=0$, the inherited HIGH correction is


$$
\boxed{
-\frac{VE^{-1}V^T}{3}
\equiv L_{dd}ee^T\pmod3.
}
\tag{24}
$$


It is not separately zero.

### 6. First-LOW correction and the extra-coordinate issue

The mixed block satisfies


$$
B/3\equiv-le^T\pmod3,
$$


so the third saturation is


$$
T_3=
\bigl(\overline L_{dd}-l^TG_0^{-1}l\bigr)ee^T.
\tag{25}
$$



A4’s statement that the rank-$D$ recurrence persists when $y^d$ is added requires a check. It is valid:

the additional recurrence vector is


$$
y^\nu(y-1)^D,\qquad D+\nu=d.
$$


For every $0\le a\le d$,


$$
\nu+a\le\nu+d=2D-2<r_1.
$$


Thus


$$
[y^{r_1}]\,y^{\nu+a}(y^H-1)=0.
$$


So this additional vector is indeed radical for the extended first-residue form. With the established invertible leading $D$-block $G_0$, the extension still has rank $D$, and


$$
\overline L_{dd}=l^TG_0^{-1}l.
$$


Consequently


$$
\boxed{T_3=0\pmod3.}
\tag{26}
$$



This explicitly verifies the cancellation between (24) and the first-LOW Schur correction.

---

## VI. Actual normalization and the final weighted gcd

A1 turn 9’s endpoint argument uses the actual divided-basis lattice. Its geometric remainder gives exact factorial divisibility, and the last Pascal complement gives a unit after that division. Its primitive-leading step therefore yields


$$
\boxed{
v_3(L_n)=1,\qquad
v_3(Q_n(-1))=2v_3(N!).
}
\tag{27}
$$


In particular $Q_n(-1)\ne0$. Put


$$
\lambda=L_n/3\in\mathbb Z_3^\times.
$$


Restoring $\lambda$, and the unit $4\ell/3^h$, does not change any of the following valuations.

After HIGH elimination, the original integral matrix has:

* the HIGH unit factors;
* $D$ factors divisible by $3$;
* $\nu$ factors divisible by $3^4$.

Hence


$$
v_3(A_{\rm det})\ge D+4\nu=d+3\nu.
\tag{28}
$$


Every codimension-one minor has valuation at least


$$
D+4\nu-4=d+3\nu-4.
\tag{29}
$$


This all-minor statement is useful because a monomial HIGH/LOW change need not leave the endpoint cofactor literally at coordinate $00$. It avoids misidentifying that cofactor after a basis change.

Using the actual identity


$$
B_{\rm det}=\ell Q_n(-1)\det K,
$$


equations (27)–(29) give


$$
v_3(B_{\rm det})
\ge h+2v_3(N!)+d+3\nu-4
\ge d+3\nu.
$$


Therefore, for the **final coefficient-pair gcd**


$$
g=\gcd(|A_{\rm det}|,|B_{\rm det}|),
$$




$$
\boxed{
v_3(g)\ge d+3\nu=3D-4.
}
\tag{30}
$$



This is a proved lower bound, not an exact denominator law.

Where $B_{\rm det}\ne0$, retain


$$
q=\frac{|B_{\rm det}|}{g},\qquad
p=-\frac{\operatorname{sgn}(B_{\rm det})A_{\rm det}}g,
$$


and the whole evaluated error


$$
\boxed{
q(e+\pi)-p
=\frac{\operatorname{sgn}(B_{\rm det})}{g}
 \bigl(A_{\rm det}+B_{\rm det}(e+\pi)\bigr)
=\frac{\operatorname{sgn}(B_{\rm det})\ell^k}{g}
 \det H_{\rm complete}.
}
\tag{31}
$$



Complete-matrix nonvanishing and the “at most one zero whole error” assertion still use the inherited regular-family nonvanishing and distinct-center theorems. The endpoint unit in (27) alone proves neither assertion.

---

## VII. Actual odd-family denominator and whole error

Return to the original $29$-adic class. Retain


$$
N_B=d_B[u,v],\quad
A_B=N_{B,1}^T\Omega N_{B,1}>0,\quad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
p_n=H_B/g_B,\qquad q_n=A_B/g_B.
$$


The supplied local least-denominator interface gives $v_{29}(d_B)=0$.

On the stronger exponent class define


$$
\delta=v_{29}(\widehat P^T\widehat P),\qquad
\mu=v_{29}(\widehat P^T\widehat Q).
$$


Then the exact local identities become


$$
\boxed{
v_{29}(g_B)
=\min\{4F_n+4+\delta,\;2F_n+F_b+5+\mu\},
}
\tag{32}
$$




$$
\boxed{
v_{29}(q_n)
=\max\{0,\;2F_n-F_b-1+\delta-\mu\}.
}
\tag{33}
$$


The norm is positive. Finiteness of the mixed valuation retains the supplied original-family $3$-adic nonvanishing dependency.

At the dependency status of the complete signed-rate theorem,


$$
\epsilon_n=c_n-(e+\pi)>0\quad\text{eventually},
$$




$$
\log|\epsilon_n|
=-\left(2+\frac1{2001}\right)\log(1+\sqrt2)\,n+o(n),
$$


and the actual primitive evaluated form is


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n<0
\quad\text{eventually}.
}
\tag{34}
$$


All other prime contributions remain in $q_n$. Neither (30) nor the new $29$-adic whole-column divisibility establishes a favorable global denominator rate.

---

# Concluding ledger

## (1) New result and proof status

**Proved here**

* The full normalized $Q$-digit, including the extra carry term (2) and the endpoint.
* The coordinate evaluation (8) of $U_\perp^TQ_\perp\bmod29$.
* The next-defect formula (7), with complete precision-four forcing and genuine cubic inverse inputs.
* On
  

$$
a\equiv432827\pmod{682892},
$$


  the stronger whole-column divisibility
  

$$
V_w/b!\in29^3\mathbb Z_{29}^{b+1},
$$


  and hence $E_1\equiv0\pmod{29}$.
* A sufficient actual modulo-$27$ polynomial core derived from A1’s normalization, without assuming A4’s particular constant digit.
* A4 turn 13’s grid, all pole cuts, HIGH inverse perturbation, and cancellation with the first-LOW correction.
* The actual final-gcd lower bound $v_3(g)\ge3D-4$, with the endpoint normalization restored.

**Not proved**

* A simplified all-index scalar law for (7).
* Unit/zero evaluation of the two new scalar digits in (13) on the stronger original class.
* Gram-divisibility at all depths, an explicit $O(b)$ relative-loss bound, or an exact reduced-denominator law.
* Irrationality or rationality of $e+\pi$.

## (2) Exact remaining bottleneck

On the stronger original class, the local problem is now


$$
\boxed{
\mu-\delta
=
v_{29}(\widehat P^T\widehat Q)
-
v_{29}(\widehat P^T\widehat P),
\qquad
\widehat P=Z_w/29^2,\quad
\widehat Q=V_w/(29^3b!).
}
$$


Both columns must genuinely be lifted; the previous $Q$-digit is now zero as a whole.

For the weighted route, the next task is a fourth actual saturation with inherited unit corrections. The third-saturation cancellation is not an induction in pole depth.

## (3) Bounded computation request

The coordinator’s pending precision-four $b=839$ computation already supplies the data needed to test (7). No duplicate run is requested.

An optional, genuinely new bounded test of the interior carry term is:



$$
\boxed{
p=29,\quad b=2521,\quad n=2001b=5044521,
\quad\text{precision }3.
}
$$


This is auxiliary, not an original power-$3$ index. Here


$$
B=86,\quad K=3,\quad N_1=5998\equiv24\pmod{29}.
$$



With the complete construction and forcing, return the normalized $Q$-entries at $839,1680,2521$, together with $t_{29},t_{58}$. The verifiable predictions are


$$
\boxed{
Q_{839}\equiv-6t_{29}+16,\qquad
Q_{1680}\equiv-6t_{58}+17,\qquad
Q_{2521}\equiv16\pmod{29}.
}
$$


These test the new interior $29^2v-2$ carry term and the endpoint separately. Any result would have only its stated finite auxiliary scope.
