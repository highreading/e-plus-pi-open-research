> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 — the corrected norm multiplier is zero, and the first defect vanishes on the actual norm-zero locus

The remaining $K_{01}$ does not require a moment calculation. A stronger, coordinatewise carry lemma kills the entire first corrected $P$-column at the normalization relevant here.

On the original MAIN29 class I obtain


$$
\boxed{K_{01}=0,}
$$


and therefore


$$
\boxed{\Lambda(n,b;d)=J_0^2 f(d),}
$$


where $J_0=C_n$ is the actual central coefficient and


$$
\begin{aligned}
(f(0),\ldots,f(28))={}&
(5,25,21,14,23,15,7,9,9,28,6,9,6,9,6,\\
&\qquad 28,9,9,7,15,23,14,21,25,5,0,0,0,0).
\end{aligned}
$$


Thus no $J_{29}$, $J_{58}$, or other moment parameter survives in the corrected norm multiplier.

I also prove


$$
\boxed{D_0=0\ \Longrightarrow\ M_0=0}
$$


on this original class, including $d=25,26,27,28$. Equivalently, the complete first defect vanishes on the **actual** norm-zero locus. This is a first-digit statement, not an all-depth valuation estimate.

The independent audit of A5turn16 passes: with its supplied complete fixed lift, its conclusions


$$
\Delta_3=0,\qquad \alpha,\gamma\ge4
$$


hold on the same class $r=18+32u$, without a further restriction.

---

## 1. Domain, coordinates, and the new carry lemma

Throughout the MAIN29 argument,


$$
p=29,\qquad b=3^a,\qquad n=2001b,
$$




$$
a\ge1,\qquad a\equiv432827\pmod{682892},\qquad m_w=1.
$$


All coordinate indices remain


$$
0\le j\le b,
$$


and every contact inverse has indices $0\le i,j<b$.

Retain


$$
W_j=\binom{n+2}{j},\qquad
\widehat P=\frac{Z_w}{p^2},\qquad
\widehat Q=\frac{Y}{p^3},\qquad Y=\frac{V_w}{b!},
$$


and


$$
D_0=\widehat P^T\widehat P\bmod p,\qquad
M_0=\widehat P^T\widehat Q\bmod p.
$$



For an integer $q$, define


$$
B_q(j)=
\binom{2n+b-j-1}{b-j-q},
$$


with the zero convention for an invalid lower index. The Laurent reconstruction used in the supplied sources is exactly


$$
\mathscr R(F)_j
=
(-1)^{j+1}W_j\sum_q A_q(j)B_q(j)
\quad\text{if}\quad
F(j,r)=\sum_q A_q(j)r^q.
\tag{1.1}
$$


Indeed, $r^q=x^q(1-x)^{-q}$, so coefficient extraction gives $B_q(j)$. This identity includes the already absorbed complete $Q$-endpoint.

The four fixed low digits are


$$
b=(27,28,5,28,\ldots)_{29},
$$




$$
n+2=(2,7,24,7,\ldots)_{29},
\qquad
2n=(0,14,19,15,\ldots)_{29}.
$$



### Lemma 1 — uniform annihilation of all needed nonnegative Laurent powers

For every $0\le q\le87$ and every $0\le j\le b$,


$$
\boxed{W_jB_q(j)\in p^2\mathbb Z_p.}
\tag{1.2}
$$


The two factors are forced at digit positions $1$ and $3$.

#### Proof

An invalid binomial is zero, so suppose its lower index is valid. Apply Kummer to the weight and to the addition


$$
(2n+q-1)+(b-j-q).
$$



Write $q=29Q+q_0$, $0\le q_0<29$, and put


$$
\beta=\mathbf1_{q_0=28}.
$$


The digit at position $1$ of $b-q$ is $28-Q-\beta$. If the weight has no borrow at position $1$, then $j_1\le7$. If $\eta\in\{0,1\}$ is the incoming borrow when subtracting $j$ from $b-q$, the lower binomial index has digit


$$
28-Q-\beta-j_1-\eta.
$$


It is nonnegative for $q\le87$. The digit at position $1$ of $2n+q-1$ is


$$
13+Q+\mathbf1_{q_0>0}.
$$


Their sum is at least


$$
41+\mathbf1_{q_0>0}-\beta-j_1-\eta\ge32>28.
$$


Thus, if the weight does not borrow at digit $1$, the second binomial carries there.

For digit $3$, adding or subtracting $q\le87$ changes neither the relevant digit $28$ of $b-q$ nor the digit $15$ of $2n+q-1$. If the weight does not borrow at digit $3$, then $j_3\le7$. The lower index consequently has digit at least


$$
28-j_3-1\ge20.
$$


Adding $15$ forces a carry.

The two positions are distinct, proving (1.2). ∎

### Direct proof of the requested $\tau=-1$ improvement

The $\tau=-1$ product in turn17 is $W_jB_0(j)$. Lemma 1 already forces carries across the two binomials at positions $1$ and $3$.

At position $0$, if the weight does not borrow, $j_0\le2$. Then $b-j$ has digit $27-j_0\ge25$, while $2n-1$ has digit $28$. Their addition carries. Hence


$$
\boxed{W_jB_0(j)\in p^3\mathbb Z_p}
\tag{1.3}
$$


uniformly, proving directly


$$
\boxed{\mu_{-1}(x)=0.}
$$



This is an infinite carry proof; it does not depend on the $707281$-case enumeration.

---

## 2. Evaluation of $K_{01}$: every coefficient is zero

The supplied bounded reconstruction has nonnegative Laurent support


$$
\operatorname{supp}_r\mathcal P\subseteq[0,87],
$$


with $p$-integral integer-valued coefficients in $j$.

Let


$$
C=J_0=C_n,\qquad
h_0(j)=\sum_{i=0}^{28}(-1)^ii!\binom ji.
$$


Frobenius gives $J_t=0\bmod p$ for $1\le t\le28$, and therefore


$$
\mathcal P\equiv C(r+1-h_0(j))\pmod p.
$$


Use the integral representative


$$
\mathcal P_0=C(r+1-h_0(j)).
$$


The identity


$$
h_0(j)+jh_0(j-1)=1+29!\binom j{29}
$$


ensures that this congruence holds coefficientwise in the integral Newton–Laurent representation, not merely at selected coordinates.

Consequently


$$
\mathcal P-\mathcal P_0=pF
$$


for a kernel $F$ still supported in $0\le q\le87$. Lemma 1 now gives


$$
\boxed{Z_w-Z^{(0)}\in p^3\mathbb Z_p^{b+1}.}
\tag{2.1}
$$


This is stronger than the earlier scalar grade elimination.

In particular, the actual first corrected kernel $\mathcal P_1$, whose support is contained in $0\le q\le58$, satisfies


$$
\boxed{Z^{(1)}\in p^2\mathbb Z_p^{b+1},}
\tag{2.2}
$$


not just $p\mathbb Z_p^{b+1}$. Hence


$$
\frac{(Z^{(0)})^TZ^{(1)}}{p^3}
\in p\mathbb Z_p,
$$


and the requested multiplier is


$$
\boxed{K_{01}=0\in\mathbb F_{29}.}
\tag{2.3}
$$



Thus the explicit finite polynomial in the actual moments is the zero polynomial: every coefficient of $J_0^2,J_0J_{29},J_{29}^2$, and of any additional moment monomial, is zero. No contiguous-moment reduction is needed because the entire corrected column has been annihilated before contraction.

---

## 3. The explicit norm multiplier and its complete zero locus

Equation (1.3) also removes the $h_0$-term from the normalized base column:


$$
\boxed{
\widehat P_j
\equiv
(-1)^{j+1}C\,p^{-2}W_j
\binom{2n+b-j}{b-j}
\pmod p.
}
\tag{3.1}
$$



Retain the original higher digits


$$
L=29^4,\qquad b=687936+Lh,\qquad h=29H+d,\quad 0\le d<29,
$$




$$
N=2001h+1946=3+29N_1,\qquad N_1=69h+67.
$$


They are the digits of the original $3^a$, not independently selected cylinder parameters.

The genuine residual norm remains


$$
T(N_1,H)=
\sum_{k=0}^{H}
\binom{N_1}{k}^{2}
\binom{2N_1+H-k}{H-k}^{2}\pmod{29}.
\tag{3.2}
$$



Using the coordinator’s exact fixed constants


$$
\kappa_0=11,\qquad \kappa_1=18,
$$


the corrected multiplier is now fully evaluated:


$$
\boxed{
D_0=C^2 f(d)\,T(N_1,H),
\qquad
f(d)=11\psi_0(d)+18\psi_1(d).
}
\tag{3.3}
$$



For an explicit coefficient formula, put


$$
B_v=
\begin{cases}
\binom{v+6}{6}\pmod{29},&0\le v\le22,\\
0,&\text{otherwise}.
\end{cases}
$$


Then every coefficient of $f$ is given by


$$
\boxed{
\begin{aligned}
f(d)={}&
\bigl(11(d+7)^2+17\bigr)B_d^2\\
&+\bigl(12(d+6)^2+10\bigr)B_{d-1}^2\\
&+\bigl(12(d+5)^2+17\bigr)B_{d-2}^2\\
&+11(d+4)^2B_{d-3}^2.
\end{aligned}}
\tag{3.4}
$$


For example, the second coefficient is


$$
9\bigl(11(d+6)^2+18\cdot4\bigr)
=12(d+6)^2+10\pmod{29}.
$$


The other three follow in the same way from the four terms $t=0,1,2,3$ in the previously defined $\psi_e$.

Evaluation of (3.4) gives the vector displayed at the beginning. Thus, using the supplied original-family fact that $C$ is a unit,


$$
\boxed{
0\le d\le24:\quad D_0=0\iff T(N_1,H)=0.
}
\tag{3.5}
$$



For $25\le d\le28$, the earlier base-column argument together with (2.1) gives the stronger actual-column assertion


$$
\boxed{
Z_w\in p^3\mathbb Z_p^{b+1},
\qquad
\widehat P\in p\mathbb Z_p^{b+1}.
}
\tag{3.6}
$$


Therefore


$$
\boxed{
25\le d\le28:\quad D_0=M_0=0.
}
\tag{3.7}
$$


In fact $\delta=v_{29}(\widehat P^T\widehat P)\ge2$ on these four digit classes.

This resolves the extra norm-zero locus that could not previously be replaced by $T=0$.

---

## 4. A bounded evaluation of the relevant complete $Q$-forcing

The next argument evaluates the defect on $T=0$ without a ghost-path enumeration. It uses the actual complete Laurent boundary and a termwise low-block divisibility.

### 4.1 Two additional carry facts

Besides (1.3), one has


$$
W_jB_{-1}(j)\in p^3\mathbb Z_p.
\tag{4.1}
$$


At digit $0$, absence of a weight borrow gives $j_0\le2$, and the second addition has digits $28-j_0$ and $27$, forcing a carry. Digits $1,3$ work as in Lemma 1.

Also,


$$
\boxed{jW_jB_{-2}(j)\in p^3\mathbb Z_p.}
\tag{4.2}
$$


Here the relevant addition is


$$
(2n-3)+(b+2-j).
$$



* If $j_0\ne0$, positions $0,1,3$ force three carries across the binomials.
* If $j_0=0$, $j_1\ne0$, the coefficient $j$ supplies one factor of $p$, while positions $1,3$ supply two more.
* If $j_0=j_1=0$, $j$ supplies $p^2$, and position $3$ supplies the third factor.

All these factors are determined within the four-digit block. Finally, for every $-60\le q\le0$, digit $3$ alone proves


$$
W_jB_q(j)\in p\mathbb Z_p.
\tag{4.3}
$$



### 4.2 The first contact polynomial is explicit

Let $m=n/p\bmod p=7$. At precision $p^2$, only the $s=29,v=29$ term contributes to the first $Q$-boundary contact polynomial:

* for $s<29$, $\binom nv$ supplies an extra $p$;
* $d_{29}/p=m$;
* $\binom n{29}=m\bmod p$;
* the unit boundary coefficients are $c_0=1,c_1=-1\bmod p$.

Consequently


$$
\frac{h_Q(X)}p
\equiv
-m^2\left[
\binom{b-X+28}{28}+
\binom{b-X+29}{28}
\right]\pmod p.
$$


Since $-m^2=9\bmod29$, this is


$$
\boxed{
a(X)=9\bigl(\mathbf1_{X\equiv27}+\mathbf1_{X\equiv28}\bigr)
\pmod{29}.
}
\tag{4.4}
$$


The right side is represented by the displayed degree-$28$ integer-valued polynomial.

Its reconstructed first-digit kernel is


$$
\boxed{
\mathcal R_a(j,r)=r\,a(j)+(1+r)j\,a(j-1).
}
\tag{4.5}
$$



A nonzero coordinate in (3.1) must have $j_0\le2$: otherwise the weight has a digit-$0$ borrow in addition to the compulsory digit-$1$ and digit-$3$ carries. At these residues,


$$
a(j)=j\,a(j-1)=0\pmod p.
$$


Thus


$$
\boxed{
\text{the first \(Q\)-contact correction contributes zero to }M_0.
}
\tag{4.6}
$$



This evaluates that contact contribution, rather than merely bounding its degree.

### 4.3 The remaining factorial boundary at this digit

The unit boundary gives exactly


$$
\boxed{
\mathcal Q_0(j,r)=(2+r^{-1})(1+j+jr^{-1}).
}
\tag{4.7}
$$


Its three reconstructed monomials are covered by (1.3), (4.1), and (4.2), so


$$
\mathscr R(\mathcal Q_0)\in p^3\mathbb Z_p^{b+1}.
\tag{4.8}
$$



For $2\le h\le30$,


$$
\frac{c_h}{p^2}\equiv\frac{F_h}{p^2}
\equiv-6(h-2)!\pmod p.
\tag{4.9}
$$


Indeed, in


$$
c_h=\sum_{d=h}^{59}F_d\binom{2n}{d-h},
$$


the terms $h<d\le30$ have $1\le d-h\le28$ and hence an extra factor $p$; the $d\ge31$ terms already have valuation at least three. Moreover


$$
F_h/p^2\equiv(-1)\cdot6\cdot(h-2)!.
$$



Thus the entire relevant grade-two boundary is the explicit finite polynomial


$$
\boxed{
\mathcal T_2(j,r)=
-6\sum_{h=2}^{30}(-1)^h(h-2)!
\frac{(1+r)^h}{r^h}
(1+j+jr^{-1}).
}
\tag{4.10}
$$


Its support is $[-31,0]$, and (4.3) gives


$$
p^2\mathscr R(\mathcal T_2)\in p^3\mathbb Z_p^{b+1}.
$$



The complete $31\le d\le59$ factorial block has coefficient valuation at least three and Laurent support within $[-60,0]$. Equation (4.3) therefore kills its reconstructed contribution modulo $p^4$. Higher contact coefficients have valuation at least two and nonnegative Laurent support within $[0,87]$; Lemma 1 kills those modulo $p^4$.

Accordingly, after reconstruction—not as an unsupported deletion of raw forces—


$$
\boxed{
Y\equiv
\mathscr R(\mathcal Q_0)
+p\,\mathscr R(\mathcal R_a)
+p^2\mathscr R(\mathcal T_2)
\pmod{p^4}.
}
\tag{4.11}
$$


The complete logarithmic force remains absent only through the supplied whole-force bound


$$
v_{29}(h_i^F/b!)\ge4.
$$


The endpoint remains included through (1.1).

---

## 5. Evaluation of the defect on the true norm-zero locus

The essential point is that the surviving boundary terms have the **same higher-index factor** as the normalized $P$-column. No higher-digit truncation is needed.

Write


$$
j=LJ+x,\qquad 0\le x<L.
$$


Only the low indices


$$
\mathcal X=\{0\le x\le687936:\nu_0(x)=2\}
$$


can contribute to $\widehat P\bmod p$. On this set $x_0\le2$, and put


$$
v=687936-x,\qquad
e=\mathbf1_{x>191112}.
$$


Define


$$
F(J)=\binom NJ\binom{2N+h-J}{h-J},
$$




$$
\ell_0(J)=2N+h-J+1,\qquad
\ell_1(J)=N-J.
$$



The normalized $P$-coordinate is


$$
\widehat P_{LJ+x}
\equiv
(-1)^{j+1}C\,c(x)\,\ell_e(J)F(J)\pmod p.
\tag{5.1}
$$



### Lemma 2 — the surviving boundary has the same high factor

For each $x\in\mathcal X$, there is a low-block scalar $\xi(x)\in\mathbb F_{29}$, independent of $J$ and of all higher digits, such that


$$
\boxed{
p^{-3}\mathscr R(\mathcal Q_0+p^2\mathcal T_2)_{LJ+x}
\equiv
(-1)^{j+1}\xi(x)\ell_e(J)F(J)\pmod p.
}
\tag{5.2}
$$


The statement is valid throughout the actual finite range $0\le J\le h$, including its endpoints.

#### Proof

Every boundary monomial has $-31\le q\le0$ and a coefficient linear in $j$. Modulo $p^4$, that coefficient may be evaluated at $x$, because $j-x=LJ$.

Also


$$
0\le v-q<L;
$$


there is no borrow in the high part of the second binomial’s lower index. Its upper high part is


$$
2N+h-J+u,\qquad
u=\left\lfloor\frac{382219+v}{L}\right\rfloor.
$$



Separate the first four factorial levels in the two binomials. Their remaining high factorial ratio is


$$
\frac{N!}{J!(N-J-e)!}
\frac{(2N+h-J+u)!}{(h-J)!(2N)!}
=
F(J)(N-J)^e(2N+h-J+1)^u.
\tag{5.3}
$$



For $x\in\mathcal X$, exactly one of the two original binomials has the final low-block carry. Thus $e+u=1$. The possible one-unit difference between $382219+v$ and $382220+v$ cannot change this on $\mathcal X$: the exceptional $v=L-382220$ has $v_0=0$, whereas here $v_0=27-x_0\in\{25,26,27\}$.

Each boundary summand has at least three low factors, including its explicit coefficient factors, by Section 4. Terms with more than three disappear. For a term with exactly three, the divided low factorial units and the coefficient depend only on $x$; its remaining high ratio is exactly (5.3), namely $\ell_e(J)F(J)$.

This also preserves the finite boundary $J=h$; no negative high lower index was introduced. ∎

By (4.6), the contact term does not contribute to the mixed scalar. Squaring the common high factor in (5.1)–(5.2), and then writing $J=29k+t$, gives the same fifth-digit separation as for the norm:


$$
\sum_{J=0}^{h}\ell_e(J)^2F(J)^2
\equiv\psi_e(d)\,T(N_1,H)\pmod p.
\tag{5.4}
$$


The only surviving low terms satisfy


$$
0\le t\le3,\qquad 0\le d-t\le22.
$$


Their remaining high indices are precisely $0\le k\le H$, with the zero-binomial convention in (3.2). Thus every higher digit remains in $T$.

It follows, without needing to evaluate a mixed multiplier away from the zero locus, that


$$
\boxed{T(N_1,H)=0\ \Longrightarrow\ M_0=0.}
\tag{5.5}
$$



Combining (3.5), (3.7), and (5.5),


$$
\boxed{
D_0=0\ \Longrightarrow\
M_0-(6C_n)^{-1}D_0=0.
}
\tag{5.6}
$$



### The requested lowest-grade defect

For grades $0+1$, the term


$$
p\,\mathscr B(\mathcal P_1,\mathcal Q_0)
$$


is divisible by $p^6$, because $Z^{(1)}\in p^2$ and $\mathscr R(\mathcal Q_0)\in p^3$. The first $Q$-contact term has zero mixed contribution by (4.6). Thus the surviving lowest-grade defect is controlled by the $\mathcal Q_0$ version of Lemma 2 and the base norm.

Hence


$$
\boxed{
D_0=0
\quad\Longrightarrow\quad
\frac{E_{[0]}+E_{[1]}}{p^5}=0\pmod p.
}
\tag{5.7}
$$



For $0\le d\le24$, this follows from $T=0$. For $25\le d\le28$, it follows directly from the actual whole-column divisibility (3.6). Thus the four additional norm-zero digit classes are included, not replaced by $T=0$.

This proves the assigned first-depth vanishing. It does **not** evaluate the next normalized discrepancy or establish an all-depth bound for $\mu-\delta$.

---

## 6. Independent audit of A5turn16

The audited binary domain is exactly


$$
b=9^r,\qquad n=4002b,\qquad r=18+32u,\quad u\ge0.
$$


Use its actual columns and metric:


$$
X=\frac{Z_w}{2R},\qquad Y=\frac{V_w}{4b!},
\qquad
R=2^{n/2}\binom n{n/2},
$$




$$
\omega_j=j!\binom{n+2}{j}=(n+2)_{\underline j},
\qquad
\Omega=\operatorname{diag}(\omega_j^2).
$$


All coordinates are $0\le j\le b$. The seven boundary coefficients and the complete force bound are retained as supplied.

### 6.1 Off-pair support: passed

For $4k+2$, the two cases used in A5 are exhaustive:

* $4\nmid k$ gives at least three factors in $\binom{M-1}{k}$;
* $4\mid k$ gives two low carries in the other binomial.

Thus $4\mid X_{4k+2},Y_{4k+2}$.

For $4k$, outside $k\equiv0,16\bmod32$, the only possible valuation-one low pattern of $\binom Mk$ is $k\equiv8\bmod32$. Its remaining high binomial forces $t$ even; since $D$ is odd, the second binomial then carries at bit $5$. The odd-$k$ cases also have the additional carry stated in A5. Therefore every off-pair even coordinate has $4\mid X_j,Y_j$.

The odd-coordinate refinement also checks. In the unit-weight case, the finite moment coefficients modulo $4$ are


$$
\binom{2n+v-1}{v}\equiv(1,0,2,0),\qquad 0\le v\le3,
$$


and substituting the supplied $P\bmod4$ gives exactly A5’s formulas (20)–(21). The adjacent-binomial ratios used at $j=4k+1$ have odd denominators after cancellation. At $j=4k+3$, the displayed lower residues $14,13,12,11\bmod16$ give the required carries.

Hence


$$
8\mid X_j\quad(j\text{ odd}).
$$


The actual endpoint, including $1+b\eta_{b-1}$, satisfies the stronger supplied bounds $v_2(X_b)\ge5$, $v_2(Y_b)\ge4$.

### 6.2 The sampled polynomial: passed

Direct Vandermonde expansion of all seven boundary terms gives


$$
(1440,572,142,17).
$$


At $L=16s$, its constant and linear contributions vanish modulo $32$, while


$$
142\binom{16s}{2}\equiv16s,\qquad
17\binom{16s}{3}\equiv16s\pmod{32}.
$$


The boundary contribution is therefore zero.

The polynomial contribution reduces to


$$
16\binom{16s+4}{4}
+24\binom{16s+4}{5}
+4\binom{16s+4}{6}
+16\binom{16s+4}{7}
+16\binom{16s+4}{8}.
$$


The first binomial is odd; the remaining four have valuations at least $2,3,1,1$, respectively. Therefore


$$
\boxed{K(16s)\equiv16\pmod{32}}
$$


for every $s\ge0$. Also $K(8s)$ is even, as claimed. These are polynomial congruences, not inferences from finitely sampled values.

### 6.3 Unrestricted convolution and boundary: passed

The power congruence


$$
(1-z)^{-128E}\equiv(1-z^8)^{-16E}\pmod{32}
$$


has the required precision. The negative support of the complete boundary is only $-7,\ldots,-1$, so no negative boundary exponent lies among the sampled multiples of $8$.

Odd kernel indices have coefficients divisible by $16$ and multiply even $K(8s)$. For even indices, $K(16s)=16$ reduces the remaining calculation to the parity kernel. The resulting finite hockey-stick sum is


$$
\frac{\eta_j-2\theta_j}{16}
\equiv
\binom{2C+1+\lfloor L/128\rfloor}{\lfloor L/128\rfloor}
\pmod2.
$$


Thus A5’s paired-coordinate result


$$
8\mid X_j-Y_j
$$


holds with the actual large kernel and every higher digit retained.

Together with the off-pair support, every summand $X_j(Y_j-X_j)$ is divisible by $16$. Hence


$$
H-N\equiv0\pmod{16}.
$$



### 6.4 The next norm parity: passed

At paired coordinates the low blocks introduce no carries, so the exact valuation reduction to


$$
E_t=\binom Ct\binom{2C+1+D-t}{D-t}
$$


is valid. Since every $E_t$ is even,


$$
N\equiv8\sum_{t=0}^{D}E_t/2\pmod{16}.
$$


The convolution is exactly


$$
\sum_{t=0}^{D}E_t
=[z^D](1+z)^C(1-z)^{-2C-2}.
$$


Putting $C=2c$, its odd part modulo $4$ is


$$
2(3c+1)z(1+z^2)^{-c-2}.
$$


Here $c$ is odd on every assigned index, so this odd part is zero modulo $4$. Since $D$ is odd,


$$
N\equiv0\pmod{16}.
$$


Consequently


$$
\boxed{\Delta_3=0,\qquad N\equiv H\equiv0\pmod{16},\qquad
\alpha,\gamma\ge4.}
$$



No new subclass or omitted endpoint is needed.

---

## 7. Primitive arithmetic and the whole evaluated errors

For each family separately, retain the least common denominator $d_B$ of the actual two-column lift:


$$
N_B=d_B[u,v].
$$


Using that family’s actual metric,


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
p_n=H_B/g_B,\qquad q_n=A_B/g_B>0.
$$


The final primitive multiplier on the integer coefficient pair is $1/g_B$. The actual reduced denominator is $q_n$, not $d_B$, a row-clearer, or a raw contact determinant.

For MAIN29, retaining its supplied rising-factorial metric


$$
\Omega=\operatorname{diag}\bigl((n+2)_j^2\bigr)
$$


and $v_{29}(d_B)=0$, put


$$
F_n=v_{29}(n!),\qquad F_b=v_{29}(b!),
$$




$$
\delta=v_{29}(\widehat P^T\widehat P),\qquad
\mu=v_{29}(\widehat P^T\widehat Q).
$$


The exact interface is unchanged:


$$
v_{29}(g_B)=
\min\{4F_n+4+\delta,\;2F_n+F_b+5+\mu\},
$$




$$
v_{29}(q_n)=
\max\{0,\;2F_n-F_b-1+\delta-\mu\}.
$$


The new first-digit alignment does not bound $\mu-\delta$ at subsequent depths.

For the binary falling-factorial metric, with $s=s_2(n)$,


$$
v_2(g_B)=
\min\left\{
3n-2s+2+\alpha,\,
\frac{3n}{2}-s+v_2(b!)+3+\gamma
\right\},
$$




$$
v_2(q_n)=
\max\left\{
0,\frac{3n}{2}-v_2(b!)-s-1-(\gamma-\alpha)
\right\}.
$$


The audited $\alpha,\gamma\ge4$ does not control their difference.

Norm nonvanishing follows from positivity. Mixed nonvanishing retains the supplied original-family dependency; it is not inferred from a finite residue calculation.

At the supplied status of the complete signed-error theorems,


$$
q_n(e+\pi)-p_n=-q_n\epsilon_n,
$$


with the MAIN29 form eventually negative and the binary form eventually positive, both nonzero. Their complete rates are respectively


$$
\log|\epsilon_n|
=-\left(2+\frac1{2001}\right)n\log(1+\sqrt2)+o(n),
$$




$$
\log|\epsilon_n|
=-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$


These are whole evaluated errors, retaining the exponential residual, logarithmic force, finite boundary, endpoint, actual columns, and actual metric.

No global denominator-rate conclusion, and no proof or disproof of irrationality of $e+\pi$, follows from the present finite-depth results.

---

# Concluding ledger

## (1) New result and proof status

**Proved here, using the supplied complete bounded kernels and fixed constants:**

- The $\tau=-1$ product has three forced low carries, so $\mu_{-1}=0$.
- Every nonnegative Laurent monomial needed for the $P$-lift has two forced low carries.
- Consequently
  

$$
K_{01}=0,\qquad
  \Lambda=J_0^2f(d),
$$


  with the explicit coefficient formula (3.4) and complete numerical vector above.
- No moment beyond the actual $J_0$ survives.
- The actual norm-zero locus is
  

$$
T=0\quad(0\le d\le24),
$$


  together with all four classes $d=25,\ldots,28$.
- The complete first defect, and separately its remaining grades $0+1$, vanish on that true norm-zero locus.
- A5turn16’s off-pair support, sampled-polynomial identity, unrestricted convolution, endpoint treatment, and next norm parity pass the audit.

These are uniform proofs on the stated original domains, not extrapolations from finite calculations.

## (2) Exact remaining bottleneck

The remaining arithmetic problem is at greater valuation depth:

- MAIN29: control the next discrepancy after a common scalar zero and ultimately obtain a justified bound on $\mu-\delta$.
- Binary: evaluate $(H-N)/16\bmod2$ and obtain a justified all-depth bound on $\gamma-\alpha$.
- For irrationality, combine such arithmetic control with the **actual final gcd and full primitive denominator**, across all primes, so that the whole nonzero integer linear form becomes small.

First-depth zero alignment does not itself supply that denominator bound.

## (3) Computation request

**None.** The new norm-multiplier evaluation and norm-zero defect vanishing follow from the bounded-support carry lemmas and exact finite-boundary factorization above. The coordinator’s already completed low-constant computation is sufficient.
