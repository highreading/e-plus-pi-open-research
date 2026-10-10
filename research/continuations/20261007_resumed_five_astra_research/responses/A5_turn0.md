> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5 — A paid polynomial-adjoint reduction of the complete binary pairing

**Research round: 7 October 2026**

## Executive conclusion

I do not obtain a nonzero paid exponential bracket, an original-family valuation bound for that bracket, or a proof of rationality or irrationality of $e+\pi$.

I obtain a new exact reduction of the weighted-binomial kernels in A5 turn 14:

> At bounded precision, all the required kernels can be expressed using **ten common finite moments**, three explicitly paid endpoint charges, and precision-sized polynomial arithmetic.

This replaces the precision-sized family of up to $4(2D+1)^5$ distinct sums by ten common sums. The reduction uses a polynomial adjoint for the **actual hypergeometric summand**, not the source ladder whose Gram defect has rank at least $b-2$.

The result includes:

* the unchanged cutoff $0\le j<b$;
* an explicit telescoping charge at $j=b$;
* the separate, complete physical reconstruction terminal;
* an explicit common computational denominator and its binary loss;
* an obstruction showing that one exceptional master moment cannot simply be dropped.

The limitation is substantial: the ten master moments remain unevaluated at the required precision and retain the full original parameter


$$
b=9^{18+32u}.
$$


Moreover, the new reduction can increase the required working precision. It is a structural compression, **not yet a practical primitive-digit algorithm**.

---

## 1. Scope of reuse and two corrections affecting the response

Throughout,


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0,
$$


with contact indices $0\le i,j<b$ and physical reconstruction indices $0\le j\le b$.

I reuse the following established identities at their stated scope:



$$
\mathfrak f=f^0/R\in\mathbb Z_2^b,\qquad
v_2(\mathfrak f_i)\ge \left\lfloor\frac{i+1}{8}\right\rfloor,
$$




$$
\mathcal B=A^{-T}\mathcal R^T\mathcal R A^{-1},
\qquad
v_{\mathrm{term}}=bW_b^2A^{-T}e_{b-1},
$$




$$
Q=2^{-2a-2}\mathfrak f^T\mathcal B\mathfrak f,
\qquad
E=2^{-a-3}\mathfrak f^T(\mathcal Bk+v_{\mathrm{term}}),
$$


where


$$
W_j=\binom{n+2}{j},
\qquad
k=\frac{h^e-A(j!)_{0\le j<b}}{b!}.
$$



The finite inverse-profile reduction in turn 14 is used with its exterior correction and its explicit finite-convolution subtraction terms. None of those terms is replaced by an infinite convolution.

### 1.1 The complete physical terminal

There is a potentially consequential wording error in turn 14, §5. Its equation (5.3),


$$
bW_b^2z^{(i)}_{b-1},
$$


is the contribution of the **additional terminal $+1$**, not the entire $j=b$ contribution to its equation (5.2).

The complete response terminal is


$$
\boxed{
W_b^2\,b z^{(i)}_{b-1}
\bigl(bz^k_{b-1}+1\bigr).
}
\tag{1.1}
$$


Thus it consists of both


$$
b^2W_b^2z^{(i)}_{b-1}z^k_{b-1}
\quad\text{and}\quad
bW_b^2z^{(i)}_{b-1}.
$$



Turn 14’s full equation (5.2) is correct. Any implementation retaining only its displayed (5.3) would not be correct.

### 1.2 The terminal binomial is not short-lower-index data

Turn 14’s short-parameter argument does not by itself cover


$$
W_b^2=\binom{n+2}{b}^{\!2}.
$$


This is a large-lower-index binomial. Consequently, the statement that coefficients outside the kernel sums are determined by short-lower-index binomials must exclude this separately retained terminal factor.

I keep $W_b^2$ explicit below. I claim no bounded-residue dependence for it from the short-binomial argument.

These corrections do not invalidate the kernel reduction itself. They do affect a complete response certificate.

---

## 2. The new common-summand reduction

At raw precision $2^L$, retain turn 14’s bounds


$$
I=\min(b-1,8L-2),\qquad
m=4(L-1),\qquad
T_L=\min(2L-1,2n-1),
$$


and choose


$$
D=I+2m+T_L+4.
\tag{2.1}
$$



The kernels to be evaluated have the form


$$
\begin{aligned}
\mathcal K
={}&\sum_{j=0}^{b-1}\binom{n+2}{j}^{\!2}\binom jr\\
&\qquad\cdot
\binom{\alpha n+b+\eta-j}{b+\varepsilon-j}
\binom{\beta n+b+\eta'-j}{b+\varepsilon'-j},
\end{aligned}
\tag{2.2}
$$


where


$$
\alpha,\beta\in\{1,2\},\qquad
|\eta|,|\varepsilon|,|\eta'|,|\varepsilon'|\le D,\qquad
0\le r\le2D.
$$



The theorem below applies when


$$
\boxed{n>4D+2.}
\tag{2.3}
$$


This is an explicit precision restriction, not a replacement of the original index domain. It holds throughout the intended bounded-precision regime for the original family. No extension to half-length precision is inferred.

Put


$$
N=n+2,\qquad B=b+D,\qquad
A_\alpha=\alpha n+b-D,\qquad
\Delta_\alpha=A_\alpha-B=\alpha n-2D.
\tag{2.4}
$$



For $\alpha,\beta\in\{1,2\}$, define the common summand


$$
\boxed{
t_{\alpha\beta}(j)=
\binom Nj^{\!2}
\binom{A_\alpha-j}{B-j}
\binom{A_\beta-j}{B-j}.
}
\tag{2.5}
$$


We use it only at the finite indices $0\le j\le b$.

Define its moments


$$
M_s^{\alpha\beta}
=\sum_{j=0}^{b-1}j^s t_{\alpha\beta}(j).
\tag{2.6}
$$



### 2.1 Integral polynomial conversion of every offset

For an offset pair $(\eta,\varepsilon)$, set


$$
h=D+\eta,\qquad \ell=D-\varepsilon.
$$


Thus $0\le h,\ell\le2D$. With rising and falling factorial notation,


$$
(x)^{\overline q}=x(x+1)\cdots(x+q-1),\qquad
(x)_{\underline q}=x(x-1)\cdots(x-q+1),
$$


we have


$$
\boxed{
\binom{A_\alpha+h-j}{B-\ell-j}
=
\binom{A_\alpha-j}{B-j}
\frac{(A_\alpha+1-j)^{\overline h}
      (B-j)_{\underline\ell}}
     {(\Delta_\alpha+1)^{\overline{h+\ell}}}.
}
\tag{2.7}
$$



For a nonnegative lower index, this is immediate from factorial cancellation. If $B-\ell-j<0$, then $\ell>B-j$, and the falling factorial on the right contains zero. Thus (2.7) also preserves the required zero convention near the physical endpoint.

In particular, it does not continue the original binomial polynomially through a forbidden lower index.

Since


$$
\binom jr=\frac{(j)_{\underline r}}{r!},
$$


each kernel is exactly


$$
\mathcal K=\frac1c\sum_{j=0}^{b-1}P(j)t_{\alpha\beta}(j),
\tag{2.8}
$$


where $P\in\mathbb Z[j]$,


$$
\deg P\le r+h+\ell+h'+\ell'\le10D,
\tag{2.9}
$$


and


$$
c=r!\,
(\Delta_\alpha+1)^{\overline{h+\ell}}
(\Delta_\beta+1)^{\overline{h'+\ell'}}.
\tag{2.10}
$$



A common integral computational clearer is


$$
\boxed{
C_{\alpha\beta}
=(2D)!\,
(\Delta_\alpha+1)^{\overline{4D}}
(\Delta_\beta+1)^{\overline{4D}}.
}
\tag{2.11}
$$


Indeed, $c\mid C_{\alpha\beta}$. Consequently every kernel has a representation


$$
\boxed{
C_{\alpha\beta}\mathcal K
=\sum_{j=0}^{b-1}\widetilde P(j)t_{\alpha\beta}(j),
\qquad
\widetilde P\in\mathbb Z[j],\quad \deg\widetilde P\le10D.
}
\tag{2.12}
$$



The clearer $C_{\alpha\beta}$ is only an arithmetic device for this reduction. It is **not** the producer’s least simultaneous clearer $d_B$, and it induces no row-content operation.

---

## 3. A polynomial adjoint for the actual summand

The ratio of successive summands in (2.5) gives the exact Pearson identity


$$
v_{\alpha\beta}(j+1)t_{\alpha\beta}(j+1)
=u(j)t_{\alpha\beta}(j),
\tag{3.1}
$$


where


$$
u(j)=(N-j)^2(B-j)^2,
$$




$$
v_{\alpha\beta}(j)
=j^2(A_\alpha+1-j)(A_\beta+1-j).
\tag{3.2}
$$



No division is required to state or sum (3.1).

Define the polynomial operator


$$
\boxed{
\mathscr T_{\alpha\beta}Q(j)
=u(j)Q(j+1)-v_{\alpha\beta}(j)Q(j).
}
\tag{3.3}
$$



For every polynomial $Q$, finite summation gives


$$
\begin{aligned}
\sum_{j=0}^{b-1}t_{\alpha\beta}(j)
 \mathscr T_{\alpha\beta}Q(j)
&=\sum_{j=0}^{b-1}
 \bigl[v_{\alpha\beta}(j+1)t_{\alpha\beta}(j+1)Q(j+1)\\
&\hspace{38mm}-v_{\alpha\beta}(j)t_{\alpha\beta}(j)Q(j)\bigr]\\
&=v_{\alpha\beta}(b)t_{\alpha\beta}(b)Q(b).
\end{aligned}
$$


The lower charge is zero because $v_{\alpha\beta}(0)=0$. Thus


$$
\boxed{
\sum_{j=0}^{b-1}t_{\alpha\beta}(j)
 \mathscr T_{\alpha\beta}Q(j)
=\mathcal T_{\alpha\beta}Q(b),
}
\tag{3.4}
$$


with the complete telescoping charge


$$
\boxed{
\begin{aligned}
\mathcal T_{\alpha\beta}
={}&b^2(\alpha n-D+1)(\beta n-D+1)W_b^2\\
&\quad\cdot
\binom{\alpha n-D}{D}
\binom{\beta n-D}{D}.
\end{aligned}
}
\tag{3.5}
$$



This is an introduced summation charge at the genuine cutoff. It does not replace the physical terminal (1.1). Both must be retained.

### 3.1 Leading coefficient and the exceptional degree

The degree-four leading terms of $u$ and $v_{\alpha\beta}$ cancel in $\mathscr T_{\alpha\beta}j^s$. A direct expansion gives


$$
\boxed{
\mathscr T_{\alpha\beta}j^s
=(s+\sigma_{\alpha\beta})j^{s+3}
+\text{terms of degree at most }s+2,
}
\tag{3.6}
$$


where


$$
\boxed{
\sigma_{\alpha\beta}
=(\alpha+\beta-2)n-4D-2.
}
\tag{3.7}
$$



For checking the expansion, write


$$
u(j)=j^4+u_3j^3+u_2j^2+u_1j+u_0,
$$


where


$$
u_3=-2(N+B),\quad
u_2=N^2+4NB+B^2,\quad
u_1=-2NB(N+B),\quad
u_0=N^2B^2.
$$


Also


$$
v_{\alpha\beta}(j)
=j^4-(A_\alpha+A_\beta+2)j^3
 +(A_\alpha+1)(A_\beta+1)j^2.
$$


The coefficient in (3.6) is therefore


$$
s-2(N+B)+A_\alpha+A_\beta+2
=s+\sigma_{\alpha\beta}.
$$



Under (2.3),


$$
\sigma_{12}>0,\qquad \sigma_{22}>0.
$$


For $(\alpha,\beta)=(1,1)$,


$$
\sigma_{11}=-4D-2.
$$


There is exactly one exceptional step,


$$
s=4D+2,
$$


at which the degree-$(s+3)$ coefficient vanishes.

---

## 4. The ten-master theorem

Set $H=10D$, and define


$$
\Pi_{\alpha\beta}
=\prod_{\substack{0\le s\le H-3\\s+\sigma_{\alpha\beta}\ne0}}
(s+\sigma_{\alpha\beta}).
\tag{4.1}
$$



For $D\ge1$, these are explicitly


$$
\boxed{
\Pi_{11}=(4D+2)!\,(6D-5)!,
}
\tag{4.2}
$$




$$
\boxed{
\Pi_{12}=(n-4D-2)^{\overline{10D-2}},
\qquad
\Pi_{22}=(2n-4D-2)^{\overline{10D-2}}.
}
\tag{4.3}
$$



### Theorem 4.1 — Paid finite polynomial reduction

For every $P\in\mathbb Z[j]$ of degree at most $H$, there are integral coefficients and an integral polynomial $Q$ such that

* for $(\alpha,\beta)=(1,2)$ or $(2,2)$,
  

$$
\boxed{
  \Pi_{\alpha\beta}P(j)
  =c_0+c_1j+c_2j^2+
  \mathscr T_{\alpha\beta}Q(j);
  }
  \tag{4.4}
$$


* for $(\alpha,\beta)=(1,1)$,
  

$$
\boxed{
  \Pi_{11}P(j)
  =c_0+c_1j+c_2j^2+c_*j^{4D+5}
  +\mathscr T_{11}Q(j).
  }
  \tag{4.5}
$$



One may take $\deg Q\le H-3$. The coefficients are obtained by descending polynomial reduction.

#### Proof

Work first over $\mathbb Q$.

For a current leading degree $k\ge3$, put $s=k-3$. If $s+\sigma_{\alpha\beta}\ne0$, subtract the appropriate multiple of


$$
\mathscr T_{\alpha\beta}j^s
$$


to eliminate the leading term. Equation (3.6) ensures that all newly introduced terms have smaller degree.

For type $11$, if $k=4D+5$, retain that monomial rather than divide by zero. All other degrees $k\ge3$ are eliminated. This gives (4.4) or (4.5) with rational coefficients.

Each nonzero factor $s+\sigma_{\alpha\beta}$ is used at most once as a divisor in this descending process. Inductively, all resulting denominators divide their product $\Pi_{\alpha\beta}$. Multiplying by that product makes every coefficient integral. ∎

Summing (4.4)–(4.5) using (3.4) yields a complete boundary-paid expression.

### Corollary 4.2 — Ten common finite moments suffice

Every kernel (2.2) is determined by the following ten moments:


$$
\boxed{
M_0^{11},\ M_1^{11},\ M_2^{11},\ M_{4D+5}^{11},
}
\tag{4.6}
$$




$$
\boxed{
M_0^{12},\ M_1^{12},\ M_2^{12},
\qquad
M_0^{22},\ M_1^{22},\ M_2^{22},
}
\tag{4.7}
$$


together with the three charges $\mathcal T_{11},\mathcal T_{12},\mathcal T_{22}$.

More explicitly, there are integers $c_s$ and an integral polynomial $Q$ such that


$$
\boxed{
C_{\alpha\beta}\Pi_{\alpha\beta}\mathcal K
=
\sum_{s\in\mathcal S_{\alpha\beta}}
 c_sM_s^{\alpha\beta}
+\mathcal T_{\alpha\beta}Q(b),
}
\tag{4.8}
$$


where


$$
\mathcal S_{11}=\{0,1,2,4D+5\},
\qquad
\mathcal S_{12}=\mathcal S_{22}=\{0,1,2\}.
$$



The symmetry $t_{12}=t_{21}$ removes the fourth ordered type.

This theorem concerns the actual finite weighted-binomial summands. It is not a generic automaton-existence assertion.

---

## 5. All nonunit losses are explicit

Let


$$
\kappa_{\alpha\beta}
=C_{\alpha\beta}\Pi_{\alpha\beta},
\qquad
e_{\alpha\beta}=v_2(\kappa_{\alpha\beta}).
\tag{5.1}
$$



To obtain a kernel modulo $2^L$ from (4.8), its **whole right-hand side** must be evaluated modulo


$$
\boxed{2^{L+e_{\alpha\beta}}.}
\tag{5.2}
$$


Only afterward may one divide by $2^{e_{\alpha\beta}}$ and invert the odd part of $\kappa_{\alpha\beta}$.

There is no claim that the individual master-moment terms are separately divisible by $2^{e_{\alpha\beta}}$.

The loss is exactly computable from the short products


$$
\begin{aligned}
e_{\alpha\beta}
={}&v_2((2D)!)
+v_2\!\left((\alpha n-2D+1)^{\overline{4D}}\right)\\
&+v_2\!\left((\beta n-2D+1)^{\overline{4D}}\right)
+v_2(\Pi_{\alpha\beta}).
\end{aligned}
\tag{5.3}
$$



For an explicit coarse bound, a product of $k$ consecutive positive integers, all at most $X$, has valuation at most


$$
k-1+\lfloor\log_2X\rfloor.
$$


This follows by counting multiples of each $2^a$:


$$
\#\{2^a\text{-multiples in the interval}\}
\le\left\lfloor\frac{k-1}{2^a}\right\rfloor+1.
$$


Consequently a sufficient common estimate here is


$$
\boxed{
e_{\alpha\beta}
\le20D+3\left\lceil\log_2(2n+10D)\right\rceil.
}
\tag{5.4}
$$



This is deliberately conservative. The exact value (5.3), or a smaller denominator found in the actual polynomial reduction, should be used in any calculation.

### Practical significance—and limitation

The number of long sums has fallen to ten. But the direct carry evaluation of those sums would now be needed at precision $L+e_{\alpha\beta}$, not merely $L$.

Thus the new theorem does **not** make the turn-14 carry construction practical. Combining an exponential-in-precision carry bound with an additional $O(D+\log n)$ precision payment can be worse than evaluating more kernels at the original precision.

What has improved is the algebraic target: one now needs congruences for ten common moments, rather than a large family of separately shifted kernels.

---

## 6. Transfer to the complete Gram and exponential response

The reduction may be applied either to each required head entry or after assembling the actual scalar linear combination. The latter avoids needless separate reductions.

At raw precision $2^L$, turn 14 supplies reconstructed profiles as finite combinations of


$$
(-1)^j\binom jd
\binom{\alpha n+b+\eta-j}{b+\varepsilon-j}.
$$


Their products have the kernel form (2.2). Therefore:

* every head Gram entry;
* every head entry of $\mathcal Bk+v_{\mathrm{term}}$;
* the complete raw norm numerator;
* the complete raw exponential numerator

are expressible through the same ten moments, with different precision-sized coefficients.

All coefficient assembly can be performed before evaluating the moments.

### 6.1 The exponential source remains complete

The source used here is still


$$
k=\sum_{t=0}^{2n-1}\frac{(b+t)!}{b!}\,\mathbf a_{b+t}.
$$


Its paid reduction modulo $2^L$ is


$$
k\equiv
\sum_{t=0}^{T_L}\frac{(b+t)!}{b!}\,\mathbf a_{b+t}
\pmod{2^L}.
$$



This is the established complete factorial subtraction, not a truncation of the aligned residual.

The exact differential identity underlying it remains


$$
\mathscr L_n
\left(
\frac{\phi^ng_n-e^z\phi^nU_b}{b!}
\right)
=e^z\phi^{n+1}(C_{b-1}+C_b).
$$


Both exponential boundary source columns are therefore present in the response to which the new reduction is applied.

The exterior $+1$ in the corrected second column remains accounted for by


$$
y^E=\frac14\left(\mathcal RA^{-1}k+W_be_b\right),
$$


and by the full physical terminal (1.1).

### 6.2 Primitive precision remains separately paid

For primitive output modulo $2^K$, the raw precision remains


$$
L_Q=K+2a+2
\quad\text{for }Q,
\qquad
L_E=K+a+3
\quad\text{for }E.
$$



The master-moment reduction then requires the additional payment (5.2). It does not replace these outer divisions.

Thus, schematically, the exponential route is


$$
\boxed{
\begin{gathered}
\text{master moments at }2^{L_E+e_{\alpha\beta}}
\\
\longrightarrow
\text{whole kernel divisions}
\\
\longrightarrow
\mathfrak f^T(\mathcal Bk+v_{\mathrm{term}})
 \bmod2^{L_E}
\\
\longrightarrow
E\bmod2^K.
\end{gathered}}
\tag{6.1}
$$



No entrywise inversion of a power of two is involved.

### 6.3 Logarithmic forcing

The corrected source is still


$$
\mathcal L_m=m![z^m]\frac{F(z)}{1-z}.
$$


The accepted guard is


$$
B_*=n-v_2(b!)-1-2s_2(n)-\ell.
$$



The present theorem reduces the exponential contribution. It does not erase the logarithmic source. Any requested digit beyond its protected range must include the complete original logarithmic contribution.

---

## 7. An exceptional master really survives this polynomial reduction

The exceptional type-$11$ moment is not merely an artifact that can always be omitted.

Here is an exact low-degree witness on the original parameter family.

Take $D=1$, type $11$, and the extreme kernel offsets


$$
\eta=\eta'=1,\qquad
\varepsilon=\varepsilon'=-1,\qquad r=2.
$$


Its polynomial numerator in (2.8) is


$$
\boxed{
P(j)=j(j-1)
\bigl[(n+b-j)(n+b+1-j)(b+1-j)(b-j)\bigr]^2.
}
\tag{7.1}
$$



Now


$$
\sigma_{11}=-6,\qquad H=10,\qquad
\Pi_{11}=6!=720,
$$


and the master degrees are $0,1,2,9$.

The polynomial $P$ is monic of degree ten. Its degree-nine coefficient is


$$
-[4n+8b+5].
\tag{7.2}
$$



For this case,


$$
u(j)=(n+2-j)^2(b+1-j)^2,\qquad
v(j)=j^2(n+b-j)^2.
$$


The degree-ten coefficient of $\mathscr Tj^7$ is $7-6=1$, and its degree-nine coefficient is


$$
2nb-6n-4b-8.
\tag{7.3}
$$



After eliminating the degree-ten term, the remaining degree-nine coefficient is therefore


$$
\boxed{
R_9=-2nb+2n-4b+3.
}
\tag{7.4}
$$



On every original index, $n$ is even and $b$ is odd, so


$$
R_9\equiv1\pmod2.
\tag{7.5}
$$



No lower-degree reduction changes this coefficient:

* $\mathscr Tj^s$ has degree at most eight for $s\le5$;
* the resonant polynomial $\mathscr Tj^6$ also has degree at most eight.

Moreover, allowing a polynomial adjoint of degree at least eight cannot help: its nonzero highest term would produce degree at least eleven.

Hence:

### Proposition 7.1 — Necessary exceptional class for this reduction

The polynomial (7.1) cannot be written


$$
P=c_0+c_1j+c_2j^2+\mathscr TQ
$$


with a polynomial $Q$ over $\mathbb Q$ on the original family.

The degree-nine master has a nonzero, indeed odd, coefficient before denominator clearing.

This obstructs dropping that master from the displayed Pearson reduction. It does not obstruct every possible identity between finite sums, nor every other telescoper.

Most importantly, the odd coefficient in (7.5) is **not a nonzero exponential bracket**. The master itself and the other terms can still cancel in the actual complete response.

---

## 8. Why this does not contradict the source-ladder rank obstruction

Turn 14 proved


$$
\operatorname{rank}_{\mathbb Q}
\bigl((\mathcal R^T\mathcal R)J-J^T(\mathcal R^T\mathcal R)\bigr)
\ge b-2.
$$



That result concerns the source ladder $J$ acting with the full Gram metric. The present operator $\mathscr T_{\alpha\beta}$ instead acts on polynomial weights multiplying one explicitly specified hypergeometric summand.

Its finite-dimensional quotient is the quotient of precision-bounded polynomial weights by the image of $\mathscr T_{\alpha\beta}$. It is not a bounded-rank representation of the Gram matrix.

Accordingly, both results can hold:

* the natural source-ladder Green defect has essentially full rank;
* the explicit kernel family admits a ten-master polynomial-adjoint reduction.

This is a different telescoping mechanism, with its own nonunit losses and its own boundary charge.

The underlying hypergeometric and summation-by-parts methods are classical. Paule–Schneider supplies creative-telescoping machinery, but not the specific paid finite certificate above. Likewise, the cited Rowland–Yassawi results provide automatic-congruence machinery and complexity results at their stated hypotheses; they do not evaluate these ten complete master moments. No external search or priority claim is made here.

---

## 9. The narrowed follow-on lemma

The next target can now be stated more concretely.

### Complete master-response lemma — still open

For the original family, derive a useful congruence or valuation theorem for the **actual assembled linear combination** of


$$
M_0^{11},M_1^{11},M_2^{11},M_{4D+5}^{11},
\quad
M_0^{12},M_1^{12},M_2^{12},
\quad
M_0^{22},M_1^{22},M_2^{22},
$$


with:

1. the exact coefficients produced by the finite inverse profiles and the complete source;
2. the three telescoping charges (3.5);
3. the separate full physical terminal (1.1);
4. the losses $v_2(C_{\alpha\beta}\Pi_{\alpha\beta})$;
5. the subsequent division by $2^{a+3}$.

Two concrete possibilities remain worth distinguishing.

**Coefficient-side source-response duality.** Assemble the actual complete response before reduction and prove that some master coefficients vanish, or acquire sufficient valuation, because of the specific first force and complete exponential source. Proposition 7.1 shows that this cannot be presumed for arbitrary kernels.

**Master-side congruence.** Prove a relation among these particular moments at paid precision, preserving the full cutoff and original word. A relation for an infinite sum, a short residue substituted for $b$, or an unpaid extension through $j=b$ would not suffice.

The ten-master theorem makes these finite targets explicit. It does not establish either one.

---

## 10. A small bounded exact certificate

No computation was executed. None is required for the proofs above.

A useful optional independent check of the new algebra is the following **polynomial certificate**, not a response-digit calculation.

### Inputs

Keep $b$ symbolic and set $n=4002b$. Use the $D=1$ polynomials in §7:


$$
P(j),\qquad
u(j)=(n+2-j)^2(b+1-j)^2,\qquad
v(j)=j^2(n+b-j)^2.
$$



### Expected verifiable output

Produce


$$
C_0,C_1,C_2,C_9\in\mathbb Z[b],
\qquad Q(j)\in\mathbb Z[b][j],\quad \deg_jQ\le7,
$$


satisfying the polynomial identity


$$
\boxed{
720P(j)=
C_0+C_1j+C_2j^2+C_9j^9
+u(j)Q(j+1)-v(j)Q(j),
}
\tag{10.1}
$$


with


$$
\boxed{
C_9=720(-8004b^2+8000b+3).
}
\tag{10.2}
$$


The descending reduction may choose the coefficient of $j^6$ in $Q$ to be zero.

Verification requires only expansion of a degree-ten polynomial identity. It does not scan any original-size matrix or summation range.

For this kernel the offset denominator is


$$
c=2[(n-1)n(n+1)(n+2)]^2.
$$


On the original family,


$$
v_2(n)=1,\qquad v_2(n+2)=2,
$$


so


$$
v_2(c)=7,\qquad v_2(720)=4.
$$


Thus the displayed certificate has an explicitly paid eleven-bit kernel division.

The certificate would validate a genuinely new finite identity. It would not evaluate the master moments, a primitive exponential digit, a final gcd, or a whole error. No completed expensive ternary or endpoint calculation is requested again.

---

## 11. Actual normalization, all-prime reduction, and whole error

Nothing in this report changes the corrected columns


$$
x=\frac{\mathcal RA^{-1}f^0}{2R},
\qquad
y=\frac{\mathcal RA^{-1}(h^e+h^F)+e_0}{4b!}.
$$



Retain


$$
\omega_j=j!W_j,\qquad
u_j=\frac{2\Lambda R\,x_j}{\omega_j},
\qquad
v_j=\frac{4b!\,y_j}{\omega_j},
$$


and the actual least simultaneous clearer


$$
d_B=
\operatorname{lcm}_{0\le j\le b}
\{\operatorname{den}(u_j),\operatorname{den}(v_j)\}.
$$



No actual row contents are removed. The final integer forms and all-prime gcd remain


$$
A_B=d_B^2\,4\Lambda^2R^2N,\qquad
H_B=d_B^2\,8\Lambda Rb!H,
$$




$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
}
\tag{11.1}
$$



For every prime $p$,


$$
v_p(q_n)
=
\max\{v_p(\mathscr D_n)+v_p(N)-v_p(H),0\},
\qquad
\mathscr D_n=\frac{\Lambda R}{2b!}.
$$



The closed ternary law is reused:


$$
\boxed{v_3(q_n)=n-\frac{b+15}{2}.}
\tag{11.2}
$$


It is not reproposed as a computational target.

The final evaluated form remains


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n,
\qquad
\epsilon_n=\frac{p_n}{q_n}-(e+\pi).
}
\tag{11.3}
$$



A favorable irrationality argument still requires the actual all-prime denominator and a nonzero whole error at the same infinitely many original indices. This report supplies neither that comparison nor a newly evaluated nonzero exponential digit.

---

## Conclusion and proof status

The new proved result is a **boundary-paid ten-master reduction**:


$$
\boxed{
\begin{gathered}
\text{all actual turn-14 weighted-binomial kernels}\\
\text{reduce to ten common finite moments,}\\
\text{three explicit cutoff charges, and polynomial arithmetic.}
\end{gathered}}
$$



The proof identifies every division and retains the large terminal factor $W_b^2$. It also corrects the distinction between the terminal $+1$ contribution and the complete physical response terminal.

A second new result shows that the exceptional type-$11$ master cannot generally be discarded within this polynomial-adjoint reduction: an explicit degree-ten kernel has an odd exceptional coefficient on every original index.

The precise remaining bottleneck is now:

> Evaluate, or prove a useful congruence for, the actual assembled combination of these ten master moments at the increased paid precision, including both kinds of terminal charge and the complete source.

The master moments still contain the full original word of $b$. No compressed high-word invariant, practical evaluation theorem, nonzero paid exponential bracket, or same-index all-prime/whole-error certificate has been obtained.

**The new reduction is rigorous. Its valuation application remains open. The rationality or irrationality of $e+\pi$ remains unresolved.**
