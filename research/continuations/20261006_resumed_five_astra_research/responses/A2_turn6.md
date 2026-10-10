> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2, Turn 6 — A compatible second lower lift, a next-norm radical, and unbounded actual content on every original arithmetic progression

## Executive conclusion

The complete residue


$$
\frac{Z_w}{29^3}\pmod{841}
$$


and its first divided norm are **not fully evaluated in this report**. In particular, I do not claim either that the next norm digit is identically zero or that it is nonzero at a genuine original index.

There are, however, three concrete advances beyond Turn 5.

1. **The compatible second lower correction is determined explicitly.**  
   For a specified lift of $\mathsf D_1$, I derive the entire $\mathsf D_2\bmod29$, including the previously consequential range $30\le s\le58$. Among its evaluated coefficients are
   

$$
\boxed{
   d_{29}=4,\quad d_{30}=9,\quad d_{31}=18,\quad
   d_{32}=27,\quad d_{57}=11,\quad d_{58}=20.
   }
$$


   The conversion to Turn 5’s literal coefficient lift is also explicit.

2. **A new evaluated contraction eliminates the complete next first-force head from the next norm—not from the next column.**  
   If $B=\mathcal R\mathsf R_{2n}\mathsf P_-$, and $S$ is the established normalized leading actual column with its scalar $A_0$ removed, then
   

$$
\boxed{
   S^T\left(\frac{Ba}{29^3}\right)=0\pmod{29}
   }
$$


   for every integral head $a$ of length at most $292$. After checking the compatible lower and first-return terms, this implies
   

$$
\boxed{
   \eta=A_0^2\eta_{\mathrm{short}},
   }
$$


   where $\eta_{\mathrm{short}}$ is computed using the **complete finite inverse**, but with the fixed first-force head $h_i^{[0]}=i!\bmod29$, $0\le i<29$. This does not remove the second lower correction or second endpoint return.

   The physical terminal coordinate at the requested next precision is also evaluated:
   

$$
\boxed{
   \frac{Z_{w,b}}{29^3}
   \equiv
   14\cdot29\,A_0\,\frac{W_b}{29^4}
   \pmod{841}.
   }
$$


   Thus it must not be replaced by zero in the complete next column.

3. **Actual output content is unbounded on every original arithmetic progression.**  
   Using repeated six-digit blocks and the established precision-dependent finite normal form, I prove:
   

$$
\boxed{
   \text{For every }u_0\ge0,\ h\ge1,\text{ and }R,
   \text{ infinitely many }u\equiv u_0\pmod h
   \text{ satisfy }c\ge R.
   }
$$


   This is a statement about the complete corrected first column, not merely its leading atom. Consequently, there is **no nonconstant original arithmetic progression on which $c=1$ holds eventually**.

The last theorem resolves one of the assignment’s alternatives: $c$ is unbounded on the power orbit, in fact on every arithmetic progression within it. It does **not** establish unbounded primitive norm loss $\nu$.

---

## 1. Scope and retained definitions

Throughout,


$$
p=29,\qquad
b=3^{249005515+574312172u},\qquad n=2001b,\qquad u\ge0.
$$



The finite domains remain


$$
0\le j<b,\qquad 1\le i\le b-2,\qquad 0\le j\le b.
$$


The corrected columns are


$$
Z_w=\mathcal RA^{-1}f^0,\qquad
Y=\mathcal RA^{-1}\mathbf r+W_be_b,
$$


with


$$
W_j=\binom{n+2}{j},\qquad
P=\frac{Z_w}{p^2}=p^cx,\qquad Q=\frac{Y}{p^3}.
$$


Here $x$ is $p$-primitive and


$$
\nu=v_p(x^Tx),\qquad d=2c+4+\nu.
$$



I reuse, without repeating their calculations, the established results


$$
g=0,\qquad \frac{f_1^0}{f_0^0}\equiv465\pmod{841},
$$


the complete Turn 5 leading-column formula, its support, and the exact high-sum symmetry.

Write


$$
T=\frac{Z_w}{p^3},\qquad
\eta=\frac{T^TT}{p}\pmod p.
$$


Turn 5 proves that this whole division is legitimate. If $T$ is primitive and $\eta\ne0$, then


$$
c=1,\qquad \nu=1,\qquad d=7.
$$


Without primitivity, $\eta$ is not a primitive norm invariant.

No accepted prefix, auxiliary Gram, binary exterior, or original binary contraction is requested again.

---

# Part I. The complete compatible second lower correction

## 2. Fixing the lift matters

Recall


$$
c_s(n)=s![z^s]\phi(z)^{-n},
\qquad
\phi(z)=1-z+\frac{z^2}{2},
$$


and


$$
\mathsf D=\sum_{s\ge0}c_s(n)\mathsf D_s.
$$



On the original phase,


$$
n=p(7+24p)\pmod{p^3}.
$$



Define the rational sequence


$$
a_0=2,\qquad a_1=1,\qquad
a_s=a_{s-1}-\frac12a_{s-2}.
$$


Its denominators are powers of two, hence units at $29$. Equivalently,


$$
a_s=\alpha^s+\beta^s,\qquad
\alpha+\beta=1,\quad \alpha\beta=\frac12.
$$



For $1\le s<29$, put


$$
q_s=(s-1)!a_s.
$$


I first use the compatible lift


$$
\mathsf D_1^\ast
=
\sum_{s=1}^{28}7q_s\mathsf D_s-7\mathsf D_{29}.
$$



This has the required reduction modulo $29$, but specifies an actual $29$-integral lift. Relative to it, write


$$
\mathsf D
=
I+p\mathsf D_1^\ast+p^2\mathsf D_2^\ast
\pmod{p^3}.
$$



### Theorem 2.1 — Explicit second lower lift

Let $d_s$ denote the coefficient of $\mathsf D_s$ in $\mathsf D_2^\ast\bmod p$. Then


$$
\boxed{
d_s=
24q_s+
\frac{49}{2}s!
\sum_{r=1}^{s-1}
\frac{a_ra_{s-r}}{r(s-r)}
\pmod{29},
\qquad 1\le s\le28,
}
\tag{2.1}
$$


with an empty sum equal to zero,


$$
\boxed{d_{29}=4,}
\tag{2.2}
$$


and


$$
\boxed{
d_{29+r}
=
(r-1)!\bigl(7\cdot21^r+4\cdot9^r\bigr)
\pmod{29},
\qquad1\le r\le29.
}
\tag{2.3}
$$


Finally,


$$
\boxed{d_s=0\qquad(s\ge59).}
\tag{2.4}
$$



Thus the complete second correction has support through $58$, not merely through $29$.

Some evaluated coefficients are


$$
\begin{array}{c|rrrrrrrrrr}
s&1&2&3&4&29&30&31&32&57&58\\ \hline
d_s&24&20&5&22&4&9&18&27&11&20.
\end{array}
\tag{2.5}
$$



### Proof

Since


$$
-\log\phi(z)=\sum_{r\ge1}\frac{a_r}{r}z^r,
$$


expansion of $\exp(-n\log\phi)$, for $s<29$, gives


$$
c_s(n)
=
nq_s+
\frac{n^2}{2}s!
\sum_{r=1}^{s-1}\frac{a_ra_{s-r}}{r(s-r)}
\pmod{p^3}.
$$


Substituting $n=p(7+24p)$ proves (2.1).

For $s=29$, every nonlinear term in the exponential expansion contributes a multiple of $p^3$. Therefore


$$
c_{29}(n)\equiv n\,28!\,a_{29}\pmod{p^3}.
$$


The following bounded residues are directly evaluable:


$$
28!\equiv521=-1+18p\pmod{p^2},
$$




$$
\alpha\equiv21,\qquad \beta\equiv-20\pmod{p^2},
$$


and


$$
a_{29}\equiv21^{29}+(-20)^{29}\equiv407=1+14p\pmod{p^2}.
$$


Consequently,


$$
28!a_{29}\equiv-1+4p\pmod{p^2},
$$


and hence


$$
\frac{c_{29}(n)}p
\equiv
(7+24p)(-1+4p)
=-7+4p\pmod{p^2}.
$$


This proves $d_{29}=4$.

The exact coefficient recurrence is


$$
\boxed{
c_{s+1}(n)
=
(s+n)c_s(n)
-
s\left(n+\frac{s-1}{2}\right)c_{s-1}(n).
}
\tag{2.6}
$$


It follows from $\phi(\phi^{-n})'=n(1-z)\phi^{-n}$.

Using


$$
\frac{c_{28}}p\equiv14,\qquad
\frac{c_{29}}p\equiv-7,
$$


equation (2.6) gives


$$
\frac{c_{30}}{p^2}\equiv9,\qquad
\frac{c_{31}}{p^2}\equiv18.
$$


For $c_{29+r}/p^2$, the subsequent recurrence modulo $p$ has the solution


$$
(r-1)!\bigl(7\cdot21^r+4\cdot9^r\bigr),
$$


with precisely these initial values. It remains valid through $r=29$, giving $d_{58}=20$.

For completeness, modulo $p$,


$$
\phi(z)^{-n}\equiv\phi(z^p)^{-n/p}.
$$


For $59\le s\le86$, $v_p(s!)=2$, but $s$ is not divisible by $29$, so its power-series coefficient supplies another factor $p$. For $s\ge87$, the established factorial bound already gives $v_p(c_s)\ge3$. This proves (2.4). ∎

---

## 3. Conversion to Turn 5’s literal $\mathsf D_1$

Turn 5 displayed the integer representatives


$$
k_s=7(s-1)!(21^s+9^s),\qquad 1\le s<29,
\qquad k_{29}=-7.
$$



If these are used literally as the lift, rather than only as residues modulo $29$, the compatible second coefficients are


$$
\boxed{
d_s^{\rm old}
=
d_s-7s!\,9^{s-1}\pmod{29},
\qquad1\le s<29.
}
\tag{3.1}
$$


The coefficients at and above $29$ remain those in (2.2)–(2.4).

Indeed,


$$
(-20)^s\equiv9^s-29s9^{s-1}\pmod{841},
$$


so


$$
\frac{7q_s-k_s}{29}\equiv-7s!9^{s-1}\pmod{29}.
$$



For example,


$$
d_1^{\rm old}=17,\qquad d_2^{\rm old}=10.
$$


Using $d_1=24,d_2=20$ together with the literal old lift would therefore be incompatible.

This is an explicit correction rule, not permission to choose $\mathsf D_2$ independently of $\mathsf D_1$.

---

# Part II. An evaluated terminal coefficient and a new next-norm radical

## 4. The physical terminal row at the requested precision

At $j=b$, the reconstruction is


$$
Z_{w,b}=bW_b\theta_{b-1},
\qquad \theta=A^{-1}f^0.
$$


Since $v_p(W_b)\ge4$, only $\theta_{b-1}\bmod p$ is required to obtain $Z_{w,b}\bmod p^5$.

Normalize the input by $f_0^0$, and use the established leading head


$$
h_i^{[0]}=i!\pmod p,\qquad0\le i<29.
$$


The finite baseline identity at $j=b-1$ gives


$$
\frac{\theta_{b-1}}{f_0^0}
\equiv
\sum_{i=0}^{28}(-1)^ii!\binom{b-1}{i}
=F_{26}\pmod p,
$$


because $b-1\equiv26\pmod p$. Here


$$
F_d=1-dF_{d-1},\qquad F_0=1.
$$


The recurrence gives


$$
F_{24}=16,\qquad F_{25}=7,\qquad F_{26}=22.
$$


As $b\equiv27\pmod p$,


$$
bF_{26}\equiv27\cdot22\equiv14\pmod p.
$$



Therefore


$$
\boxed{
\frac{Z_{w,b}}{p^3}
\equiv
14pA_0\frac{W_b}{p^4}\pmod{p^2}.
}
\tag{4.1}
$$



The quotient $W_b/p^4$ is integral; its residue is allowed to be zero. Formula (4.1) retains the terminal coordinate without assuming that its weight has exact valuation four.

Its square is zero modulo $p^2$, so this terminal coordinate does not contribute to $\eta$. That is a norm-precision observation, not a deletion from the next column.

---

## 5. Extending the short-head divisibility to length $292$

Set


$$
B=\mathcal R\mathsf R_{2n}\mathsf P_-.
$$



The baseline short-head argument extends from Turn 5’s range to


$$
0\le r\le291.
$$


Indeed, in the first two digits the relevant lower minuends are


$$
838-r,\qquad839-r,
$$


which remain greater than $205$, while the upper addend is $406+r$. A no-borrow weight index therefore still forces an addition carry. The fixed digits $3,4,5$ supply the other two events.

Thus


$$
\boxed{
Ba\in p^3\mathbb Z_p^{\,b+1}
\quad\text{for every integral head }a
\text{ supported in }0,\ldots,291.
}
\tag{5.1}
$$



A further extension is needed to control how such a head enters the next lift.

### Lemma 5.1 — The first lower correction has a third factor for every such head

For every head in (5.1),


$$
\boxed{
\mathcal R\mathsf R_n\mathsf D_1^\ast
\mathsf R_n\mathsf P_-a
\in p^3\mathbb Z_p^{\,b+1}.
}
\tag{5.2}
$$



### Proof

Reduce the coefficient-weighted normal ordering modulo $p$. The terms with $1\le t<29$ have an extra factor from $\binom{-n}{t}$.

For $t=0,29$, a surviving head coefficient requires $r\equiv0\pmod{29}$, so write


$$
r=29k,\qquad0\le k\le10.
$$



There are already two forced events in digits $3,4,5$. To test the absence of a third one, it suffices to consider


$$
j_0\le2,\qquad j_1\le7.
$$



For $s<29$, a nonzero reconstruction row factor restricts $s$ to the same small cases $s\le j_0$, or $s+1\le j_0$, as before. Adding $29k$ to the upper addend and subtracting $29k$ from the lower minuend preserves their sum and still forces the low addition carry.

For $s=29,t=0$, $k\ge1$ again forces that carry. When $k=0$, its possible absence forces $j_1=0$, and the row factor vanishes.

For $s=t=29$, the two-digit upper addend is $435+29k$, and the lower minuends are $838-29k,839-29k$. Their sums again force the carry.

Terms whose head or normal-order coefficient vanishes modulo $p$ already have the needed third factor. ∎

This proof uses the actual row factors. It does not assign three factors to arbitrary positive-offset atoms.

---

## 6. The short-head radical identity

Remove the nonzero scalar $A_0$ from the established leading actual column, and write


$$
S_j=
(-1)^{j+1}
\frac{W_j\binom{2n+b-1-j}{b-1-j}}{p^3}\pmod p,
\qquad j<b,
\qquad S_b=0.
$$



### Theorem 6.1 — Evaluated short-head contraction

For every integral head $a$ supported in $0,\ldots,291$,


$$
\boxed{
S^T\left(\frac{Ba}{p^3}\right)=0\pmod p.
}
\tag{6.1}
$$



This is a new contraction identity for arbitrary short-head perturbations, rather than a reevaluation of the old leading norm.

### Proof

Let


$$
K=b-1-j,\qquad
P_j=\binom{2n+b-1-j}{K}.
$$


The exact finite-head formula can be rewritten using


$$
\binom{2n+r-1}{r}
\binom{2n+b-1-j}{K-r}
=
P_j\,\frac{2n}{2n+r}\binom Kr.
\tag{6.2}
$$


The quotient is interpreted as $1$ for $r=0$.

For $0\le r\le291$, $2n/(2n+r)$ is $29$-integral. If $r\not\equiv0\pmod{29}$, it vanishes modulo $29$; if $r=29k$, $0\le k\le10$, it reduces to


$$
\frac{14}{14+k}.
$$



On the support of $S$, write $j_0=d,j_1=e$. The finite-head multiplier therefore depends only on $d,e$. More explicitly, define


$$
E_a(d,e)=
\sum_{i=0}^{291}(-1)^ia_i
\sum_{k=0}^{\lfloor i/29\rfloor}
\frac{14}{14+k}
\binom{d+29e}{i-29k}
\binom{28-e}{k}
\pmod{29}.
\tag{6.3}
$$


All denominators $14+k$ are units.

Since $d\in\{0,1,2\}$ on the support of $S$, $b-j$ is a unit and


$$
\frac{P_{j-1}}{P_j}
=1+\frac{2n}{b-j}\equiv1\pmod p.
$$


Thus, wherever $S_j\ne0$,


$$
\left(\frac{Ba}{p^3}\right)_j
=
S_jH_a(d,e),
\tag{6.4}
$$


where


$$
H_a(d,e)=E_a(d,e)+dE_a(d-1,e),
$$


and the second term is omitted for $d=0$.

Now use the established digit factorization of $S_j$. Inserting $H_a(d,e)$ changes only the contraction over digits $0,1,2$. It does not change the digit-$5$ interface coefficients or either high observable. Consequently the contraction has the form


$$
K_a\,K_{34}
\left(10\mathscr T_{\mathrm I}
      +19\mathscr T_{\mathrm{II}}\right)
\pmod{29}
$$


for a finite low scalar $K_a$. The already proved exact high identity is


$$
\mathscr T_{\mathrm I}=\mathscr T_{\mathrm{II}}\pmod{29}.
$$


Because $10+19=0\pmod{29}$, the displayed contraction is zero independently of $K_a$. This evaluates (6.1). ∎

---

## 7. Consequence for the complete first-force head

Let


$$
h=\frac{f^0}{f_0^0}
=h^{[0]}+pa
$$


at the guarded head precision, with the complete actual $a$ retained.

At output precision $p^5$:

- the baseline perturbation is $pBa$;
- Lemma 5.1 makes the corresponding first-lower perturbation zero modulo $p^5$;
- the first crossed return of $a$ has the retained support $b,b+1$, and the established weighted third-factor lemma makes its perturbation zero modulo $p^5$;
- coefficient-order-two and higher perturbations carry at least $p^5$ by the weighted two-factor safeguard.

Therefore


$$
\boxed{
\mathcal RA^{-1}(h^{[0]}+pa)
\equiv
\mathcal RA^{-1}h^{[0]}+pBa
\pmod{p^5}.
}
\tag{7.1}
$$



In particular, $a$ generally changes the next column. It has not been set equal to zero.

Define


$$
T_{\mathrm{short}}
=
p^{-3}\mathcal RA^{-1}h^{[0]}.
$$


Then


$$
\frac{T}{f_0^0}
\equiv
T_{\mathrm{short}}+
p\frac{Ba}{p^3}
\pmod{p^2}.
$$


Forming the whole squared norm and using Theorem 6.1 gives


$$
\boxed{
\eta
=
A_0^2
\left(
\frac{T_{\mathrm{short}}^TT_{\mathrm{short}}}{p}
\right)
\pmod p.
}
\tag{7.2}
$$



This is the promised reduction


$$
\boxed{\eta=A_0^2\eta_{\mathrm{short}}.}
$$



**What it removes:** the complete actual head modulo $841$, including the next initial digit $16$, from this particular divided norm.

**What it does not remove:** the compatible $\mathsf D_2$, the next effects of $\mathsf D_1$, or the actual second finite endpoint return in $T_{\mathrm{short}}$.

Those remaining contributions have not been evaluated here.

---

# Part III. Actual content is unbounded on every original progression

## 8. A repeatable block that forces valuation

Put


$$
\Lambda=29^6,\qquad \beta=410910916.
$$


The relevant exact products are


$$
2001\beta=1382\Lambda+186913294,
$$




$$
4002\beta=2764\Lambda+373826588.
$$



The last three digits of these low blocks are


$$
\beta_{3,4,5}=(28,0,20),
$$




$$
(186913294)_{3,4,5}=(7,3,9),
$$




$$
(373826588)_{3,4,5}=(15,6,18).
$$



These digits are stable under every incoming multiplication carry that can occur:

- the lower three-digit remainder $20387$ in $2001\beta$ remains below $29^3$ after adding any carry up to $2001$;
- the corresponding remainder $16385$ in $4002\beta$ remains below $29^3$ after adding any carry up to $4002$.

Hence a block of six digits of $b$ equal to $\beta$ forces the same digit-$3,4,5$ configuration in $n+2$ and $2n+a-1$, provided the fixed small offset $a$ has been absorbed below the block.

The addition of a possible incoming $-1,0,1$ to the $b+v$ block changes only its low digits, not digits $3,4,5$.

### Lemma 8.1 — Two events per repeated block

For each such block, every supported weighted atom


$$
W_j\binom{-2n-a}{b+v-j}
$$


acquires at least two valuation events in that block, independently of all incoming subtraction and addition interface bits.

### Proof

The proof uses precisely the stable digits


$$
W:(7,3,9),\qquad
b+v:(28,0,20),\qquad
2n+a-1:(15,6,18).
$$



At the first of these positions, absence of a weight borrow forces an addition carry.

If the following two positions both contributed zero events, absence of the weight borrow at the middle position would prevent a lower-index borrow from surviving into the last position; the last position would then force an addition carry. This is a contradiction.

Thus the first position contributes at least one event and the following two contribute at least one more. ∎

The lemma is independent of the atom’s positive or negative offset. It uses its actual digits and incoming interfaces.

---

## 9. Passing from atoms to the complete corrected column

Fix a desired output precision $p^K$. Reuse the established relative finite-memory bound and full finite normal form:


$$
M=29K-1,\qquad L=58K+2.
$$


The head and exterior atoms after reconstruction satisfy


$$
a\le M+L=87K+1,
$$




$$
-L\le v\le M
$$


for head terms, and


$$
0\le a\le M,\qquad0\le v\le2M
$$


for exterior terms.

Choose $m\ge6$ large enough that


$$
29^m>87K+2.
$$


Prescribe $r$ consecutive $\beta$-blocks above digit $m-1$:


$$
b\equiv
b_{\rm low}
+
29^m\beta(1+\Lambda+\cdots+\Lambda^{r-1})
\pmod{29^{m+6r}}.
\tag{9.1}
$$


Here $b_{\rm low}$ is any admissible fixed lower prefix.

All bounded offsets are absorbed below these blocks, except for harmless incoming unit carries. Lemma 8.1 therefore gives


$$
v_p\!\left(
W_j\binom{-2n-a}{b+v-j}
\right)\ge2r
\tag{9.2}
$$


for every reconstructed atom in the complete precision-$K$ normal form.

All coefficients and solved endpoint charges in that form are $p$-integral. Therefore, if $K\le2r$,


$$
Z_{w,j}\equiv0\pmod{p^K},\qquad j<b.
$$



At the physical terminal row, each prescribed block itself forces weight borrows at positions corresponding to digits $3$ and $5$. Thus


$$
v_p(W_b)\ge2r,
$$


and the integral terminal contact coordinate gives the same conclusion at $j=b$.

Consequently,


$$
\boxed{
\text{the prefix in (9.1), with }2r\ge K,
\quad\Longrightarrow\quad
Z_w\in p^K\mathbb Z_p^{\,b+1}.
}
\tag{9.3}
$$


This is a complete-column statement, including the finite return and terminal reconstruction.

In the retained normalization,


$$
\boxed{c\ge K-2.}
\tag{9.4}
$$



---

## 10. Realization inside every original arithmetic progression

The established principal-unit result says that the original map


$$
u\longmapsto C(u)
=\frac{3^{249005515+574312172u}-\beta}{29^6}
$$


is a bijection modulo $29^k$ for every finite $k$.

Fix an original arithmetic progression


$$
u\equiv u_0\pmod h,\qquad h\ge1.
$$


Choose


$$
m\ge6+v_{29}(h)
$$


and retain the lower $m$ digits of $b(u_0)$. Append the repeated blocks in (9.1).

The principal-unit bijection gives one residue class for $u$ modulo


$$
29^{m+6r-6}
$$


realizing that prescribed finite prefix. It agrees with $u_0$ modulo $29^{v_{29}(h)}$. The Chinese remainder theorem therefore makes it compatible with $u\equiv u_0\pmod h$.

The intersection is an infinite arithmetic progression of nonnegative original indices. Taking its sufficiently large members ensures all finite-memory lengths are below the original cutoff.

### Theorem 10.1 — Unbounded actual content on every progression

For every $u_0\ge0$, $h\ge1$, and integer $R\ge0$, infinitely many original indices satisfy


$$
u\equiv u_0\pmod h,\qquad c\ge R.
$$



### Proof

Choose $K\ge R+2$, choose $r$ with $2r\ge K$, and apply (9.3)–(9.4) to the compatible progression just constructed. ∎

### Consequences

1. The content $c$ is unbounded on the original power orbit.
2. It is unbounded on every original arithmetic progression.
3. No nonconstant original arithmetic progression is eventually primitive at $c=1$.
4. This does **not** imply that $\nu$ is unbounded.
5. It does **not** determine how frequently $c=1$ occurs outside arithmetic-progression assertions.

The use of the principal-unit bijection is entirely finite-prefix use. No high word of an original $b$ has been presumed available or scanned.

---

# Part IV. What this says about a digit-free next norm law

## 11. A rigidity obstruction for low-prefix evaluation

Whenever $c\ge2$,


$$
T=\frac{Z_w}{p^3}\in p\mathbb Z_p^{\,b+1},
$$


so


$$
\eta=\frac{T^TT}{p}\equiv0\pmod p.
$$



Theorem 10.1 therefore gives zeros of $\eta$ in every original arithmetic progression.

### Corollary 11.1 — Finite-prefix rigidity

Suppose a proposed identity proves that $\eta(u)\bmod29$ depends only on $u\bmod m$, for some fixed positive integer $m$. Then


$$
\boxed{\eta(u)=0\pmod{29}\quad\text{for every original }u.}
\tag{11.1}
$$



### Proof

Every class modulo $m$ contains original indices with $c\ge2$. On those indices $\eta=0$. Constancy on the class forces the same value everywhere in it. ∎

Thus a successful elimination of all high-word dependence for this next norm would necessarily prove an **identical zero**, not a nonzero low-digit class.

This is not a proof that such elimination exists. It distinguishes the alternatives sharply:

- a genuinely finite-prefix formula for $\eta$ must vanish;
- a nonzero $\eta$ must retain information not determined by any fixed original prefix.

A fixed-dimensional observable transport can still depend on an arbitrarily long input word. The theorem does not identify fixed dimension with finite-prefix dependence.

---

## 12. The new binary receipt

The supplied binary source and receipt concern the complete original finite range


$$
0\le j\le b,
$$


with the physical exterior retained. Their reported values are


$$
D_{\rm raw}\equiv E_{\rm raw}\equiv0\pmod{2^{20}}.
$$



At their stated scope these give


$$
v_2(D_{\rm raw})\ge20,\qquad
v_2(E_{\rm raw})\ge20,
$$


not exact depths and not a ratio. The receipt correctly marks both depths as lower bounds.

The odd-factorial closure used there is target-specific arithmetic. It is not automatically a $29$-adic closure theorem. In particular, even an odd-prime analogue of its state transport would not, by itself, eliminate the original high-word input cost.

The new results above provide two more specific facts relevant to such a transport:

- the actual next head can be removed from the next norm by the proved radical identity;
- any resulting finite-prefix-only next norm must be zero.

No binary regeneration is needed.

---

# Part V. Complete second force and global normalization

## 13. The second-force obligation remains whole

The corrected second column remains


$$
Y=\mathcal RA^{-1}\mathbf r+W_be_b.
$$



With the original homogeneous columns


$$
U_a=\frac{\mathcal RA^{-1}h^{(a)}}{p^3},
\qquad
G^{(3)}_{ab}=U_a^TU_b,
$$


retain the complete finite identity


$$
\boxed{
p^3U_a^TQ
=
p^3(r_0G^{(3)}_{a0}+r_1G^{(3)}_{a1})
+\sum_{\ell=1}^{b-2}\mathcal H_\ell\lambda'_{a,\ell}
+W_bU_{a,b}.
}
\tag{13.1}
$$



The initial charges are still


$$
r_i=
\sum_s a_s(n)(n+i)_{\underline s}
\left(
T_{2n+i-s}+\frac{L_{2n+i-s}}{b!}
\right),\qquad i=0,1,
$$


and the source rows are still


$$
\mathcal H_i=
\sum_s a_s(n+1)(n+i)_{\underline s}
\binom{2n+i-s+1}{b},
\qquad1\le i\le b-2.
$$



There is no source row at $b-1$. The physical exterior at $b$ is not a recurrence step. Division by $p^3$ in (13.1) applies to its whole right-hand side.

The target remains


$$
\boxed{
x^TQ-p^c\rho_nx^Tx
\equiv0\pmod{p^{c+\nu+1}},
}
\tag{13.2}
$$


with independently defined $\rho_n$, and the logarithmic guard remains


$$
\boxed{N_{\log}\ge c+4+\nu.}
\tag{13.3}
$$



The unbounded-content theorem makes a fixed absolute-precision calculation still less suitable as a substitute for this norm-relative obligation. It does not justify any logarithmic omission.

---

## 14. All-prime gcd and the whole same-index error

No row contents, least actual two-column clearer, or row metric have been changed.

Retain


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
p_n=\frac{H_B}{g_B},\qquad
q_n=\frac{A_B}{g_B}>0.
$$



The actual primitive denominator is


$$
\boxed{
\log q_n=
\sum_\ell
\max\{v_\ell(A_B)-v_\ell(H_B),0\}\log\ell.
}
\tag{14.1}
$$



For


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


the evaluated form is always


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n
}
\tag{14.2}
$$


at the same original index.

The retained signed-error theorem, at its stated scope, does not control (14.1). Neither unbounded $29$-adic content nor a future evaluation of $\eta_{\mathrm{short}}$ replaces the all-prime denominator comparison.

---

# Part VI. Exact remaining work

## 15. What is now a smaller, genuinely new bounded calculation

The full next-column assembly has not been completed here. The new norm reduction does, however, remove one of its inputs from the next **norm** calculation.

### Inputs

For the remaining next-norm coefficient contraction:

1. The fixed phase of $b,n$, with original cutoff $j<b$.
2. The short head
   

$$
h_i^{[0]}=i!\bmod29,\qquad0\le i<29.
$$


3. The compatible $\mathsf D_1,\mathsf D_2$ from Sections 2–3.
4. The complete finite endpoint equation expanded through second order.
5. The guarded precision-$p^5$ bounds
   

$$
M=144,\qquad L=292,
$$


   including the original terminal row.
6. The established leading support of $S$, since only its pairing with the next lift contributes to the first divided norm.

### Expected verifiable output

A genuinely new bounded contraction should return:

- the solved second endpoint charges at the needed precision;
- the evaluated pairing of $S$ with the complete next short-input lift;
- the carry from forming the whole leading squared norm modulo $p^2$;
- their combined value
  

$$
\eta_{\mathrm{short}}
  =
  \frac{T_{\mathrm{short}}^TT_{\mathrm{short}}}{p}\pmod p;
$$


- either a symbolic zero valid for every compatible high continuation, or explicit surviving high observables with evaluated low coefficients.

If a surviving observable is claimed nonzero at an original index, that claim still requires a genuine original-index evaluation or a proved evaluation identity. An auxiliary high word is not sufficient.

The calculation is new: it concerns the complete next norm and second finite return, not any accepted leading Gram or prefix control.

For the **complete next column**, the actual head modulo $841$ still has to be inserted through the explicitly retained term $pBa$, and the terminal value (4.1) must be included. The norm radical does not authorize omitting that term from the column itself.

---

## 16. Proof-status ledger

| Statement | Status |
|---|---|
| $g=0$, ratio $465\bmod841$ | Reused closed results |
| Turn 5 leading column and exact high symmetry | Reused, not recomputed |
| Complete compatible $\mathsf D_2\bmod29$ | **Derived explicitly** |
| Conversion between first-order lifts | **Derived explicitly** |
| Next terminal coefficient $14$ | **Evaluated and proved** |
| Short-head baseline divisibility through length $292$ | **Proved** |
| First-lower third-factor bound for those heads | **Proved with row factors retained** |
| Short-head radical contraction | **Evaluated: identically zero** |
| Removal of the complete next head from $\eta$ | **Proved for the norm only** |
| Complete $Z_w/29^3\bmod841$ | Not fully evaluated |
| Second finite endpoint return | Not evaluated |
| $\eta_{\mathrm{short}}$: zero or nonzero | Open |
| Actual $c$ unbounded on the power orbit | **Proved** |
| Actual $c$ unbounded on every original arithmetic progression | **Proved** |
| Eventually $c=1$ on an original arithmetic progression | **Disproved** |
| Uniform or stratified bound on primitive norm loss $\nu$ | Open |
| Complete second-force relative alignment | Open |
| New binary complete contraction pair | Supplied finite result: both zero modulo $2^{20}$ |
| All-prime denominator versus whole error | Open |

---

## Conclusion

The main new content result is stronger than the earlier $C\equiv814$ obstruction:


$$
\boxed{
c\text{ is unbounded on every nonconstant original arithmetic progression.}
}
$$


It follows from repeatable valuation-forcing blocks applied to the **complete finite normal form**, including endpoint and terminal reconstruction. Thus an eventual $c=1$ arithmetic progression is not a viable target.

At the requested next norm level, the complete next first-force head has now been removed by an evaluated radical contraction:


$$
\boxed{\eta=A_0^2\eta_{\mathrm{short}}.}
$$


The compatible second lower correction and the next terminal coefficient are explicit. The precise unresolved local calculation is the whole $\eta_{\mathrm{short}}$, retaining the actual second finite endpoint return. If its high-word dependence can be eliminated to a fixed original prefix, the resulting value must be zero; a nonzero result cannot be certified by fixed low digits alone.

No bound on primitive norm loss, complete mixed alignment at the true relative depth, or all-prime denominator comparison follows yet. Consequently,


$$
\boxed{
\text{An unconditional proof or disproof of the irrationality of }e+\pi
\text{ remains unresolved.}
}
$$


