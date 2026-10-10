> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 — a sharper graded reduction and a single contracted constant term

**Status.** I do not establish alignment of the lifted scalar zeros on the original exponent class. I do obtain a substantially smaller reduction than the $643$-fold product construction:

1. The degree-$202/260$ ambient reduction has a valuation filtration that reduces **both effective Newton degrees to $86$**.
2. The complete boundary, including the endpoint, can be absorbed into one Laurent kernel. This permits contraction of the squared-binomial weights **before** any digit-state construction.
3. The actual defect is one explicit five-variable constant term, or, after the central coefficients are evaluated separately, one three-variable coefficient extraction.
4. Some rows can be eliminated unconditionally. In particular, the actual endpoint contributes zero to both lifted scalar digits on the assigned class.
5. The complete defect boundary is not the zero Laurent polynomial: its extreme Laurent coefficient has the evaluated divided residue $6$. This is **not** a nonzero scalar defect and is not a counterexample to zero-norm alignment.

The outstanding step is cancellation in the contracted constant term. I give a bounded computation request for that reduced problem, rather than another growing-dimensional inverse.

---

## 1. Domain and actual quantities

Throughout the original-index assertions,


$$
p=29,\qquad b=3^a,\qquad n=2001b,\qquad
a\ge1,\qquad a\equiv432827\pmod{682892},
$$


and the factorial depth is $m_w=1$. Thus


$$
b\equiv(27,28,5,28)_{29}\pmod{p^4}.
$$



Retain the actual columns and their established whole-column divisibilities:


$$
Z_w\in p^2\mathbb Z_p^{b+1},\qquad
Y=\frac{V_w}{b!}\in p^3\mathbb Z_p^{b+1}.
$$


Write


$$
\widehat P=\frac{Z_w}{p^2},\qquad
\widehat Q=\frac{Y}{p^3},
$$




$$
D_0=\widehat P^T\widehat P\bmod p,\qquad
M_0=\widehat P^T\widehat Q\bmod p,
$$


and


$$
C_n=\operatorname{CT}_u(u^{-1}+2+2u)^n,\qquad
c=(6C_n)^{-1}.
$$


The supplied original-family result makes $C_n$ a $p$-adic unit.

All contractions below use the actual weighted coordinates


$$
W_j=\binom{n+2}{j},\qquad 0\le j\le b.
$$



---

## 2. Audit of turn13

### 2.1 Signed closure (3): passed

The finite sum used there is


$$
\sum_{t=0}^{L}
 \binom{t+v-1}{v-1}\binom ti
=
\binom{v+i-1}{i}\binom{L+v}{v+i}.
$$


It follows by writing the summand as


$$
\binom{v+i-1}{i}\binom{t+v-1}{v+i-1}
$$


and applying the finite hockey-stick identity. Consequently, the upper boundary


$$
L=b-1-k+s-v
$$


really is retained in turn13’s operator $\mathscr L_{s,b}$.

The signs also agree:


$$
(-1)^l\binom{-v}{l-k+s-v}
=(-1)^{k-s+v}\binom{l-k+s-1}{v-1}.
$$


The $v=0$ contribution is exactly


$$
(-1)^s\binom{k}{s}h(k-s).
$$



Thus the operator acts on the actual length-$b$ restriction, not on an enlarged inverse. Its coefficients are integer-valued polynomials, hence have integral Newton coefficients.

### 2.2 Boundary cancellation (15): passed

Let $U=T(n)$, and let $V$ denote the complete nonconstant contact operator after conjugation by $U$. With


$$
e_{\rm tail}=\sum_{d=0}^{59}F_de_{b+d},\qquad
F_d=\frac{(b+d)!}{b!},
$$


put $w=U^2e_{\rm tail}$.

The complete transformed residual is the restriction of $(I+V)w$. The finite base solution uses $w_{<b}$. Therefore the difference between the complete residual and the contact matrix applied to that base solution is precisely


$$
(Vw_{\ge b})_{<b}.
$$


Since


$$
w_{\ge b}=\sum_{h=0}^{59}c_he_{b+h},\qquad
c_h=\sum_{d=h}^{59}F_d\binom{2n}{d-h},
$$


this gives turn13’s boundary force


$$
F_k^{\rm bdry}
=\sum_{s=1}^{87}d_s\sum_{h=0}^{59}c_hC_s(k,b+h).
$$



This argument verifies both the sign and the finite restriction.

### 2.3 Precision cutoffs: passed

For $1\le s\le87$,


$$
v_p(d_s)\ge1+v_p((s-1)!)
=\left\lceil\frac{s}{29}\right\rceil.
$$


Hence $s\le58$ suffices modulo $p^3$, and $s\le87$ modulo $p^4$.

Since $b+2=p^2K$, $K\equiv6\pmod p$,


$$
v_p(F_d)=
\begin{cases}
0,&d=0,1,\\
2,&2\le d\le30,\\
3,&31\le d\le59,
\end{cases}
\qquad
v_p(F_d)\ge4\quad(d\ge60).
$$


The complete factorial-tail endpoint is therefore $b+60$, exclusive.

The whole logarithmic force is omitted only through its retained bound


$$
v_p(h_i^F/b!)\ge
F_n-F_b-\lfloor\log_p(2n+b-1)\rfloor\ge4.
$$


No selected logarithmic summand is substituted for that bound.

Finally, after forming the boundary force, that force is divisible by $p$. Its cubic contact action is consequently divisible by $p^4$. Thus turn13 does account for the cubic inverse on the original residual.

### 2.4 Endpoint: passed, and it admits a useful stronger formulation

Turn13’s endpoint is


$$
z_b=W_b\,b\theta^P_{b-1},\qquad
y_b=W_b(1+b\theta^Q_{b-1}).
$$


The $1$ in the second formula is essential. Section 4 below absorbs it exactly into the boundary kernel.

---

## 3. New graded-degree lemma: both effective degrees are $86$

The degree $202/260$ bounds remain valid ambient bounds. But all their higher Newton rows vanish at the precision actually used.

Write


$$
h_P(X)=\sum_r\alpha_r\binom Xr,\qquad
h_Q(X)=\sum_r\beta_r\binom Xr.
$$



### Proposition 1

At the precisions of turn13,


$$
\boxed{
\alpha_r\equiv0\pmod{p^3}\quad(r\ge87),\qquad
\beta_r\equiv0\pmod{p^4}\quad(r\ge87).
}
\tag{1}
$$


More precisely, for $0\le r\le86$,


$$
\boxed{
v_p(\alpha_r)\ge\left\lfloor\frac r{29}\right\rfloor,\qquad
v_p(\beta_r)\ge1+\left\lfloor\frac r{29}\right\rfloor.
}
\tag{2}
$$



These assertions also hold coefficientwise when the $P$-forcing is kept as a polynomial in its central-coefficient marker.

### Proof

The coefficient of $\binom Xi$ in the initial $P$-polynomial has valuation at least


$$
\left\lfloor\frac i{29}\right\rfloor,
$$


because $(n+i)!/n!$ contains at least that many multiples of $29$.

A contact action with index $s$ raises polynomial degree by at most $s$, and costs at least


$$
w(s)=\left\lceil\frac s{29}\right\rceil
$$


powers of $p$. In particular $s\le29w(s)$.

A term of $h_P$ obtained from initial index $i$ and contact indices $s_1,\ldots,s_t$ therefore has


$$
\deg\le i+s_1+\cdots+s_t
$$


and valuation at least


$$
\left\lfloor\frac i{29}\right\rfloor+
w(s_1)+\cdots+w(s_t).
$$


If that valuation is $w$, its degree is at most $29(w+1)-1$. Modulo $p^3$, $w\le2$, so the degree is at most $86$.

For $Q$, a boundary term of contact index $s$ has degree at most $s-1$ and valuation at least $w(s)$. Subsequent contact actions add degree at most $29$ times their valuation cost. A term of total valuation $w$ has degree at most $29w-1$. Modulo $p^4$, $w\le3$, again giving degree at most $86$.

The same inequalities give (2). ∎

This is a genuine contraction of the polynomial calculation: the $203$- and $261$-coordinate ambient Newton vectors can both be replaced by $87$-coordinate vectors, without dropping a boundary or inverse term.

---

## 4. Complete Laurent boundary and endpoint absorption

Put


$$
a_t=\binom{2n+t-1}{t}.
$$


For a Newton polynomial


$$
h(X)=\sum_{r=0}^{86}\eta_r\binom Xr,
$$


define


$$
B_h(j,x)=
\sum_{r=0}^{86}\eta_r
\sum_{t=0}^{r}
a_t\binom j{r-t}
\frac{x^{t+1}}{(1-x)^{t+1}}.
\tag{3}
$$


The finite kernel identity of turn13 gives


$$
(T(-2n)\mathcal S_bh)_j
=
(-1)^j[x^{b-j}](1-x)^{-2n}B_h(j,x),
\qquad 0\le j<b.
$$



The complete $Q$-boundary is


$$
B_Q(j,x)=B_{h_Q}(j,x)
-\sum_{h=0}^{59}(-1)^{b+h}c_hx^{-h}.
\tag{4}
$$


Let $B_P=B_{h_P}$, and define reconstructed kernels


$$
R_A(j,x)=B_A(j,x)+\frac jxB_A(j-1,x),
\qquad A=P,Q.
\tag{5}
$$


Then


$$
z_j=(-1)^{j+1}W_j[x^{b-j}](1-x)^{-2n}R_P(j,x),
\tag{6}
$$


and the analogous formula with $R_Q$ gives the complete $y_j$, including the endpoint.

Here is why no endpoint correction is missing.

Extend the base formula temporarily beyond $b-1$. For $r\ge0$,


$$
-\sum_{h=0}^{59}c_h\binom{-2n}{h-r}
=-F_r,
\tag{7}
$$


where $F_r=0$ for $r>59$ in the truncated formula. This follows from


$$
\sum_{h=r}^{d}\binom{2n}{d-h}\binom{-2n}{h-r}
=\mathbf1_{d=r}.
$$


Thus the extended base value at $j=b$ is $-F_0=-1$. Using it in the reconstruction supplies exactly the required endpoint $+W_b$.

For $1\le r\le59$,


$$
(b+r)(-F_{r-1})-(-F_r)=0.
$$


At $r=60$, the possible discrepancy is $-F_{60}$, which is zero modulo $p^4$. All later values vanish.

Consequently (6) and its $Q$-analogue may be summed over


$$
0\le j\le n+2
$$


without changing the actual contractions modulo the required precision. Terms $j>b$ vanish; the endpoint $j=b$ is already complete.

---

## 5. Removing all rational kernels

Make the formal substitution


$$
x=\frac r{1+r}.
$$


The constant-term change of variables has Jacobian $1/(1+r)$.

Under this substitution, (5) becomes a bounded Laurent polynomial. Explicitly,


$$
\begin{aligned}
\mathcal R_h(j,r)
=\sum_{a=0}^{86}\eta_a\sum_{t=0}^{a}a_t
\bigg[
&r^{t+1}\binom j{a-t}\\
&+(a-t+1)(1+r)r^t\binom j{a-t+1}
\bigg].
\end{aligned}
\tag{8}
$$


Here I used the exact identity


$$
j\binom{j-1}{k}=(k+1)\binom j{k+1}.
$$



Set


$$
\mathcal P(j,r)=\mathcal R_{h_P}(j,r),
$$




$$
\mathcal Q(j,r)=\mathcal R_{h_Q}(j,r)+\mathcal T(j,r),
\tag{9}
$$


where the **complete boundary polynomial** is


$$
\boxed{
\mathcal T(j,r)=
-\sum_{h=0}^{59}(-1)^{b+h}c_h
\frac{(1+r)^h}{r^h}
\left(1+j\frac{1+r}{r}\right).
}
\tag{10}
$$



The exact support bounds are


$$
\deg_j\mathcal P,\deg_j\mathcal Q\le87,
$$




$$
\operatorname{supp}_r\mathcal P\subseteq[0,87],\qquad
\operatorname{supp}_r\mathcal Q\subseteq[-60,87].
\tag{11}
$$



### Aligned and defect parts

With the actual unit $c=(6C_n)^{-1}$, define


$$
\mathcal Q_{\rm al}=pc\,\mathcal P,
$$




$$
\boxed{
\mathcal Q_{\rm def}
=\mathcal R_{\,h_Q-pc\,h_P}+\mathcal T.
}
\tag{12}
$$


Thus $\mathcal Q=\mathcal Q_{\rm al}+\mathcal Q_{\rm def}$ exactly at the working precisions.

The scalar defect is the contraction of $\mathcal P$ with (12), not just with the polynomial contact correction. In particular, none of $\mathcal T$ may be removed before contraction.

---

## 6. Contracting the squared binomials first

For any nonnegative integers $a,c$,


$$
\binom ja\binom jc
=
\sum_{k=\max(a,c)}^{a+c}
\frac{k!}{(k-a)!(k-c)!(a+c-k)!}\binom jk.
\tag{13}
$$


This contracts every product in (8)–(12) into one Newton polynomial of degree at most $174$.

The remaining weighted identity is


$$
\boxed{
\sum_{j=0}^{N}\binom Nj^2\binom jk\,t^j
=
\binom Nk\operatorname{CT}_z
z^k(1+z)^{N-k}(1+t/z)^N.
}
\tag{14}
$$


Indeed,


$$
\binom Nj\binom jk
=\binom Nk\binom{N-k}{j-k},
$$


and extraction of the constant term proves (14).

Equations (13)–(14) eliminate the individual binomial-product states.

### 6.1 Keeping all central coefficients inside one constant term

Let


$$
A(u)=u^{-1}+2+2u.
$$


Construct the universal $P$-polynomial by replacing


$$
J_t\quad\text{with}\quad u^t
$$


in its initial forcing, and then applying the same graded contact operators. Denote the resulting kernel by $\mathcal P(j,r;u)$. It has degree at most $86$ in $u$, and


$$
\operatorname{CT}_u A(u)^n\mathcal P(j,r;u)
=\mathcal P(j,r).
$$



Define the explicit Newton coefficients $H_k$ by


$$
\boxed{
6\mathcal P(j,r;u)\mathcal Q(j,s)
-p\mathcal P(j,r;u)\mathcal P(j,s;v)
=
\sum_{k=0}^{174}H_k(r,s,u,v)\binom jk.
}
\tag{15}
$$


They are obtained by the finite integer formula (13), not by a product automaton.

Set


$$
U=z(1+r)(1+s)+rs
$$


and


$$
\mathcal H=
s^{60}\sum_{k=0}^{174}
\binom{n+2}{k}H_k(r,s,u,v)\,
z^k(1+z)^{174-k}.
\tag{16}
$$


This is an ordinary polynomial, with coordinatewise degree bounds


$$
\boxed{
\deg_{r,s,z,u,v}\mathcal H
\le(87,147,174,86,86).
}
\tag{17}
$$



### Proposition 2: a single explicit coefficient identity

Let


$$
\begin{aligned}
\mathcal E(n,b)=
[r^b s^{b+60}z^{n+2}u^nv^n]\;&
\mathcal H\,
(1+2u+2u^2)^n(1+2v+2v^2)^n\\
&\times(1+r)^{n+b-3}(1+s)^{n+b-3}\\
&\times U^{n+2}(1+z)^{n-172}.
\end{aligned}
\tag{18}
$$


Then, using arbitrary integral representatives of the prescribed column residues,


$$
\boxed{
\mathcal E(n,b)
\equiv
6C_n Z_w^TY-p\,Z_w^TZ_w
\pmod{p^6}.
}
\tag{19}
$$


Consequently,


$$
\boxed{
M_0-(6C_n)^{-1}D_0
=
(6C_n)^{-1}\frac{\mathcal E(n,b)}{p^5}
\pmod p.
}
\tag{20}
$$



### Proof

Use the complete reconstruction of Section 4 in the two factors. The signs square to one. Apply the constant-term substitutions $x=r/(1+r)$, $y=s/(1+s)$, including both Jacobians, and then use (13)–(14).

The two Jacobians and the two powers $n+2$ in the weights leave the factors


$$
(1+r)^{n+b-3}(1+s)^{n+b-3}.
$$


The common $(1+z)$-power is $n+2-174=n-172$. Multiplication by $s^{60}$ clears exactly the Laurent boundary.

Finally, the two central extractions produce $C_n\mathcal P$ in the first term of (15), and two actual $P$-kernels in the second.

Only $Z_w\bmod p^3$ and $Y\bmod p^4$ are needed in (19): their errors paired with the actual divisibilities $p^2,p^3$ contribute only multiples of $p^6$. ∎

Equation (20) is a terminal scalar identity for the **whole actual defect**. It does not yet evaluate that identity to zero.

### 6.2 A bounded Laurent numerator

For completeness, (18) can also be written as


$$
\mathcal E(n,b)=\operatorname{CT}_{r,s,z,u,v}
F^{\,b-1}\mathcal N,
\tag{21}
$$


where


$$
F=
A(u)^{2001}A(v)^{2001}
\frac{(1+r)^{2002}(1+s)^{2002}(1+z)^{2001}U^{2001}}
{rsz^{2001}},
$$


and


$$
\boxed{
\mathcal N=
\frac{A(u)^{2001}A(v)^{2001}}{rs}
(1+r)^{1999}(1+s)^{1999}U^{2003}
\sum_{k=0}^{174}
\binom{n+2}{k}H_kz^{k-2003}(1+z)^{2003-k}.
}
\tag{22}
$$


Both $F$ and $\mathcal N$ are Laurent polynomials. In particular, no rational denominator remains in the constant-term bases.

---

## 7. What really vanishes after the four fixed digits

There are two distinct kinds of proven row elimination.

### 7.1 Newton rows

Proposition 1 eliminates


$$
87\le r\le202
$$


from the $P$-reduction modulo $p^3$, and


$$
87\le r\le260
$$


from the $Q$-reduction modulo $p^4$.

These rows vanish before scalar contraction; no support heuristic is involved.

### 7.2 Actual coordinate rows, including the endpoint

The four low digits of $n+2$ are


$$
(n+2)\bmod p^4=(2,7,24,7)_{29}.
$$


For $j=(j_0,j_1,j_2,j_3,\ldots)_{29}$, define the first four subtraction borrows by


$$
\varepsilon_{-1}=0,\qquad
\varepsilon_i=
\mathbf1_{\,j_i+\varepsilon_{i-1}>(2,7,24,7)_i}.
$$


If


$$
\varepsilon_0+\varepsilon_1+\varepsilon_2+\varepsilon_3\ge3,
$$


Kummer’s theorem gives $v_p(W_j)\ge3$. Since the reconstructed $P$-solution is integral,


$$
\boxed{\widehat P_j\equiv0\pmod p.}
\tag{23}
$$


Such a row contributes zero to both $D_0$ and $M_0$, independently of every higher digit.

At the actual endpoint $j=b$, the borrows are


$$
(1,1,0,1).
$$


Therefore


$$
\boxed{
\widehat P_b=0\pmod p,\qquad
\widehat P_b^2=\widehat P_b\widehat Q_b=0\pmod p.
}
\tag{24}
$$


The endpoint has been retained and then proved irrelevant to these particular scalar digits. It was not deleted from the $Q$-column.

---

## 8. An evaluated surviving defect-boundary coefficient

The Laurent boundary itself does not disappear.

Because $b$ is odd, the $h=59$ term in (10) has sign $(-1)^{b+59}=1$. Also


$$
c_{59}=F_{59},
\qquad
\frac{F_{59}}{p^3}
\equiv K\,28!\equiv-K\equiv-6\pmod p.
$$


No polynomial-contact term, aligned or otherwise, has a negative Laurent exponent.

It follows that the extreme Laurent coefficient of the **complete defect kernel** is


$$
[r^{-60}]\mathcal Q_{\rm def}(j,r)=-j\,c_{59},
$$


and therefore


$$
\boxed{
p^{-3}[r^{-60}]\mathcal Q_{\rm def}(j,r)
\equiv6j\pmod{29}.
}
\tag{25}
$$


Equivalently, its Newton-$j$ row $1$ has divided coefficient $6$.

This is an evaluated surviving coefficient on the original class. It pinpoints why a proof that simply discards the final factorial block cannot work.

It does **not** show that (20) is nonzero. Other Laurent coefficients can cancel it after the complete squared-binomial contraction.

---

## 9. A compressed linear/scaling scheme for (18)

Here is an explicit recurrence on the already-contracted polynomial, rather than a Cartesian product of binomial automata.

For a polynomial $f$, define its integral Frobenius defect


$$
G_f(X)=\frac{f(X)^p-f(X^p)}p.
$$


For exponents $e_\nu=pq_\nu+d_\nu$, $0\le d_\nu<p$, and precision $p^k$,


$$
\begin{aligned}
[X^m]N(X)\prod_\nu f_\nu(X)^{e_\nu}
\equiv
\sum_{\substack{i_\nu\ge0\\ \sum i_\nu<k}}
&p^{\sum i_\nu}\prod_\nu\binom{q_\nu}{i_\nu}\\
{}\times [X^{\lfloor m/p\rfloor}]
&\Lambda_{m\bmod p}
\left(
N\prod_\nu f_\nu^{d_\nu}G_{f_\nu}^{i_\nu}
\right)
\prod_\nu f_\nu^{q_\nu-i_\nu}
\pmod{p^k}.
\end{aligned}
\tag{26}
$$


Terms with $i_\nu>q_\nu$ are zero. Each branch reduces precision by $\sum i_\nu$. At terminal exponent vector zero, the output is simply $[X^m]N$.

For (18), the six bases are


$$
1+2u+2u^2,\quad 1+2v+2v^2,\quad
1+r,\quad1+s,\quad U,\quad1+z.
$$



If the $87$ central coefficients are first evaluated by their single univariate scheme, only the last four bases remain. Then:

* the initial numerator degrees are at most $(87,147,174)$;
* after two section steps, every branch numerator has degrees at most $(7,7,7)$;
* this bound is preserved thereafter.

For example, in the $r$-coordinate the two relevant bases have degree one. A step at total carry cost at most five gives


$$
D'_r\le
\left\lfloor\frac{D_r+56+145}{29}\right\rfloor.
$$


The same estimate applies to $s,z$.

At precision $p^6$, merging branches with the same residual exponent offsets and remaining precision leaves at most


$$
\sum_{t=0}^{5}\binom{t+4}{4}
=\binom{10}{5}=252
$$


such offset/precision classes per layer. After the second step their dense numerator storage is at most


$$
252\cdot8^3=129024
$$


residues.

This is substantially smaller than the previous product construction. It is nevertheless a recurrence, not an already-proved vanishing invariant.

**Higher-digit caution.** In particular, coefficients such as


$$
\binom{n+2}{k}\pmod{p^6},\qquad k\le174,
$$


must be retained with sufficient parameter precision; they are not determined by the four displayed low digits alone. Formula (26) retains the complete residual exponents. No higher digit is truncated.

---

## 10. The supplied zero-norm control

The new auxiliary control is consistent with alignment at its stated layer:


$$
D_1=87=29\cdot3\pmod{841},\qquad
M_1=464=29\cdot16\pmod{841},
$$


and $C_n\equiv10\pmod{29}$. Since


$$
(6\cdot10)^{-1}=2^{-1}=15\pmod{29},
$$




$$
16-15\cdot3\equiv0\pmod{29}.
$$



Thus it genuinely checks alignment after a scalar zero, unlike the unit-norm $b=839$ example. It remains finite auxiliary evidence. Neither example evaluates (20) throughout the original class.

I have no original-class or justified zero-norm-cylinder counterexample to report.

---

## 11. Primitive arithmetic interface and whole real error

Retain the actual least two-column denominator $d_B$, with


$$
N_B=d_B[u,v],\qquad v_{29}(d_B)=0.
$$


For the actual factorial metric,


$$
\Omega=\operatorname{diag}\bigl((n+2)_j^2\bigr),
$$




$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2}.
$$


The final gcd and primitive pair are


$$
g_B=\gcd(A_B,|H_B|),\qquad
p_n=\frac{H_B}{g_B},\qquad
q_n=\frac{A_B}{g_B}>0.
$$


Thus the primitive multiplier is $1/g_B$ on the actual integer coefficient pair; neither $d_B$ nor a raw contact determinant is substituted for $q_n$.

Let


$$
\delta=v_{29}(\widehat P^T\widehat P),\qquad
\mu=v_{29}(\widehat P^T\widehat Q).
$$


The exact interface remains


$$
\boxed{
v_{29}(g_B)
=\min\{4F_n+4+\delta,\;2F_n+F_b+5+\mu\},
}
$$




$$
\boxed{
v_{29}(q_n)
=\max\{0,\;2F_n-F_b-1+\delta-\mu\}.
}
$$


Positivity gives nonvanishing of the norm. Finiteness of the mixed valuation retains the supplied original-family $3$-adic nonvanishing dependency.

At the supplied status of the complete signed-rate theorem,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi)>0
\quad\text{eventually},
$$




$$
\log|\epsilon_n|
=-\left(2+\frac1{2001}\right)\log(1+\sqrt2)\,n+o(n).
$$


The whole primitive evaluated form is


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n<0
\quad\text{eventually}.
}
$$


The complete exponential residual, logarithmic force, and endpoint remain part of that error. No denominator-rate or irrationality conclusion follows here.

---

# Concluding ledger

## (1) New result and proof status

**Proved:**

* The effective Newton degrees in turn13 are both $86$, with the graded coefficient bounds (1)–(2).
* The complete endpoint can be absorbed into the Laurent boundary, permitting an unrestricted weighted-binomial contraction.
* Equations (18)–(20) give one explicit contracted scalar identity for the actual lifted defect.
* Equation (22) supplies a bounded Laurent numerator.
* The endpoint and every row satisfying the stated three-borrow criterion vanish in both lifted scalar contractions.
* The extreme complete defect-boundary coefficient has divided residue $6j$, not zero.
* The signed closure, finite boundary cancellation, precision cutoffs, and endpoint formulas of turn13 pass the independent algebraic audit.

**Not proved:** cancellation of the contracted scalar defect, zero alignment on the original class, control of $\mu-\delta$, or irrationality/rationality of $e+\pi$.

## (2) Exact remaining bottleneck

The immediate obligation is now the explicit coefficient assertion


$$
\boxed{\mathcal E(n,b)\equiv0\pmod{29^6}}
$$


if full first-digit alignment is sought, or a weaker evaluated relation sufficient to prove zero alignment on the norm-zero part of the original class.

The surviving boundary coefficient (25) shows that this cannot be replaced by coefficientwise vanishing of the complete boundary kernel. A genuine contraction identity or a verified invariant of the small residual scheme is still required.

Even successful first-digit alignment would not establish all-depth valuation alignment or the global primitive denominator rate.

## (3) Bounded computation request

A useful new diagnostic is the odd four-digit cylinder representative


$$
\boxed{
b=1395217=687936+29^4,\qquad
n=2791829217=2001b.
}
$$


It has exactly the assigned four low digits and the original parity, but is **not** a power-$3$ index.

Use the $87$-row graded polynomials, all $60$ boundary coefficients, and the three-variable version of (18), evaluated by (26). Do not construct a length-$b$ inverse.

**Requested verifiable outputs:**

1. $C_n\bmod29$, and verification of the whole-column divisibility conditions needed for normalization;
2. $D_0,M_0$, when $C_n$ is a unit;
3. $\mathcal E(n,b)\bmod29^6$, verifying
   

$$
\mathcal E/29^5\equiv6C_nM_0-D_0\pmod{29};
$$


4. the checks
   

$$
\alpha_r=0\pmod{29^3}\ (r\ge87),\quad
   \beta_r=0\pmod{29^4}\ (r\ge87),\quad
   p^{-3}[r^{-60}]\mathcal Q_{\rm def}=6j\pmod{29}.
$$



The contracted three-variable numerator has at most


$$
88\cdot148\cdot175=2279200
$$


initial coefficient positions. After two sections, at most $129024$ residues are needed for the merged offset/precision classes described above. Factored section multiplication should be retained to avoid dense ghost-polynomial products; these are storage bounds, not a claimed running-time measurement.

A nonzero defect with unit $D_0$ would only diagnose failure of a stronger proportionality identity on this auxiliary cylinder. It would **not** disprove alignment restricted to zero norms. A zero-norm mismatch would be a justified cylinder counterexample, but still not an original-power-$3$ counterexample without an additional reachability argument.
