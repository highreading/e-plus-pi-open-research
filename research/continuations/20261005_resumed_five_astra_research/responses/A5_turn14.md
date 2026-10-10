> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, Turn 14 — A variable-precision reduction of the complete second force

## Executive conclusion

The supplied complete contact/force excerpt permits a substantial reduction that does **not** require enumerating the $b$ contact coordinates.

The reduction applies directly to the excerpt’s exact finite system


$$
\widetilde N\,y^{(2)}=h^e+h^F,\qquad
V_w=e_0+\mathcal T y^{(2)}.
$$


It retains the factorial/exponential force, the logarithmic/arctangent force, and the exterior $+1$.

The main results are:

1. **A whole-input binary budget for the complete logarithmic force.** Put
   

$$
L(r)=v_2(r!),\qquad
   K_F(n,b)=1+L(n/2)-\left\lfloor\log_2(2n+b-1)\right\rfloor.
$$


   On every original index,
   

$$
\boxed{
   h^F\in 2^{K_F(n,b)}\mathbb Z_2^b.
   }
$$


   The actual finite inverse $\widetilde N^{-1}$ and the actual reconstruction $\mathcal T$ are $2$-integral. Consequently,
   

$$
\boxed{
   \mathcal T\widetilde N^{-1}h^F
   \in2^{K_F(n,b)}\mathbb Z_2^{b+1}.
   }
$$


   Thus the logarithmic force can be omitted **only** at raw precisions $P\le K_F(n,b)$, or after accounting for any additional normalization loss.

2. **An endpoint-preserving, bounded-degree recurrence for the complete second column at those precisions.** For $P\le K_F(n,b)$, its finite contact inverse can be computed using Newton polynomials of degree at most
   

$$
\boxed{4P-3}
$$


   rather than vectors of length $b$. All actual binomial units are retained. The recurrence uses exact translations, multiplication, and a finite-boundary interpolation operator.

3. **A sparse-support consequence in the excerpt’s divided-contact coordinates.** Modulo $2^P$, the complete weighted second column is supported in
   

$$
\boxed{0\le j\le \min(b,4P-2).}
$$


   This statement includes the exterior $e_0$. When the actual endpoint $j=b$ lies in this range, it is computed exactly by the same recurrence; when it lies outside, its vanishing modulo $2^P$ is proved, not assumed.

These results provide the requested **second-force budget and a finite-state reduction of that force**. They do **not** prove the complete norm law or norm/mixed relative alignment. In particular, transferring these raw second-column congruences to the $4Y_j$ normalization requires the exact normalization map and its binary valuation; an unspecified rescaling cannot be treated as a unit.

The full all-prime gcd and the primitive-denominator/whole-error comparison remain open. No proof or disproof of irrationality of $e+\pi$ follows.

---

## 1. Domain, exact finite boundaries, and proof status

The original family is unchanged:


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0,
$$


with


$$
b=128D+81,\qquad n=128C+66,\qquad C=4002D+2532,
$$


and


$$
k=2C+1,\qquad h=32k+1,\qquad n=64k+2.
$$



The contact system has indices


$$
0\le i,r<b.
$$


Reconstructed coordinates have indices


$$
0\le j\le b.
$$



If coordinates are grouped into $128$-blocks, the exact partition remains


$$
0\le t<D,\quad 0\le\rho<128;
\qquad
t=D,\quad 0\le\rho\le80;
$$


followed by the separate endpoint $j=b$. Nothing below completes the shortened block artificially.

### Status of the preceding weighted theorem

The factorial scalar argument in A5 Turn 13 is valid:


$$
v_2\!\left(\binom i\ell
 \left\lceil\frac\ell2\right\rceil!(i-\ell)!\right)
\ge L(\lfloor i/2\rfloor).
$$


It survives telescoping differences because it is parameter-independent. Given the stated complete-symbol integrality and the accepted endpoint-preserving contact transport, the subsequent one-logarithmic-loss word estimate is also consistent.

The content-relative conclusion is then a direct consequence of the absolute tail congruence and the **actual** nonzero content. It does not require, and does not prove,


$$
a\le\mu
$$


for any model content $\mu$.

These observations audit the logical mechanism of Turn 13. They do not supply an omitted reconstruction normalization or independently replace source formulas that are only referred to there.

For the new results below, the main inputs are the explicit complete formulas in the supplied contact/force excerpt. The closed negative-root/high-tail compensation is retained without repeating its calculation.

---

## 2. Exact normalization of the new calculation

Write


$$
\phi(z)=1-z+\frac{z^2}{2},\qquad
F(z)=4\arctan\frac{z}{2-z},
$$


and define


$$
\lambda_s=s![z^s]\phi(z)^n.
$$



The exact contact matrix is


$$
\widetilde N_{ir}
=
\sum_{s=0}^{\min(2n,n+i)}
\lambda_s
\binom{n+i}{s}\binom{n+i-s}{r}.
\tag{2.1}
$$



The complete second forcing is


$$
h^e_i=
\sum_s\lambda_s\binom{n+i}{s}\mathcal D_{2n+i-s},
\tag{2.2}
$$




$$
h^F_i=
\sum_s\lambda_s\binom{n+i}{s}
(2n+i-s)!\,\mathcal F_{2n+i-s},
\tag{2.3}
$$


where


$$
\mathcal D_m=m!\sum_{r=0}^m\frac1{r!},
\qquad
\mathcal F_m=[z^m]\frac{F(z)}{1-z}.
$$



The actual weighted reconstruction is


$$
\mathcal T_{jr}
=
\binom{n+2}{j}
\left[
j\binom{-n}{r-j+1}
-\binom{-n}{r-j}
\right],
\tag{2.4}
$$


with a negative lower binomial index interpreted as zero.

Since $\omega_0=1$, the exterior vector in this normalization is exactly $e_0$:


$$
\boxed{
V_w=e_0+\mathcal T\widetilde N^{-1}(h^e+h^F).
}
\tag{2.5}
$$



This is the normalization in which the new congruences are proved.

---

## 3. The complete contact symbol is even away from its constant term

Because $n=2h$, put


$$
U(z)=-z+z^2-\frac{z^3}{2}+\frac{z^4}{8}.
$$


Then


$$
\phi(z)^n=(1+2U(z))^h
=\sum_{a=0}^{h}2^a\binom ha U(z)^a.
\tag{3.1}
$$



The divided-power coefficients of $U$ are integral:


$$
U=-z^{[1]}+2z^{[2]}-3z^{[3]}+3z^{[4]}.
$$


Products preserve divided-power integrality. Hence, writing


$$
\lambda_s=\sum_a\lambda_s^{(a)},\qquad
\lambda_s^{(a)}
=2^a\binom ha [z^{[s]}]U^a,
$$


we have


$$
\boxed{
v_2(\lambda_s^{(a)})\ge a,\qquad s\le4a.
}
\tag{3.2}
$$


For $s>0$, only $a\ge1$ contributes. In particular,


$$
\boxed{\lambda_0=1,\qquad \lambda_s\in2\mathbb Z_2\quad(s>0).}
\tag{3.3}
$$



This uses the complete symbol, not a fixed-depth replacement.

### Integral invertibility of the actual finite contact matrix

Modulo $2$,


$$
\widetilde N_{ir}\equiv \binom{n+i}{r}.
$$


Let


$$
P_{ir}=\binom{n+i}{r}.
$$


Vandermonde gives


$$
P_{ir}=\sum_{t=0}^r\binom it\binom n{r-t}.
$$


Thus $P$ is the product of a lower-triangular Pascal matrix and an upper-triangular matrix, both with diagonal $1$. Therefore


$$
\det P=1.
$$


Consequently,


$$
\boxed{
\widetilde N\in\operatorname{GL}_b(\mathbb Z_2).
}
\tag{3.4}
$$



Together with the integer entries of $\mathcal T$, this proves that neither contact inversion nor weighted reconstruction loses binary precision in the normalization (2.5).

---

## 4. A complete logarithmic-force budget

This section budgets every term of $h^F$.

### 4.1 Coefficients of the arctangent input

Direct differentiation gives


$$
F'(z)=\frac2{\phi(z)}.
$$


Write


$$
\frac1{\phi(z)}=\sum_{r\ge0}\alpha_rz^r.
$$


The recurrence


$$
\alpha_0=1,\qquad \alpha_1=1,\qquad
\alpha_r=\alpha_{r-1}-\frac12\alpha_{r-2}
$$


proves inductively


$$
\boxed{
v_2(\alpha_r)\ge-\left\lfloor\frac r2\right\rfloor.
}
\tag{4.1}
$$



Since $F(0)=0$,


$$
\mathcal F_m
=\sum_{r=1}^m\frac{2\alpha_{r-1}}r.
$$


For $m\ge1$, each summand satisfies


$$
v_2\!\left(m!\frac{2\alpha_{r-1}}r\right)
\ge
L(m)+1-\left\lfloor\frac{r-1}{2}\right\rfloor-v_2(r).
$$


It follows that


$$
\boxed{
v_2(m!\mathcal F_m)
\ge
L(m)+1-\left\lfloor\frac{m-1}{2}\right\rfloor
-\lfloor\log_2m\rfloor.
}
\tag{4.2}
$$



This is a bound for the whole coefficient, including all $r=1,\ldots,m$.

### 4.2 A useful factorial identity

For $m=2v$,


$$
L(m)-\left\lfloor\frac{m-1}{2}\right\rfloor=L(v)+1;
$$


for $m=2v+1$,


$$
L(m)-\left\lfloor\frac{m-1}{2}\right\rfloor=L(v).
$$


Thus


$$
L(m)-\left\lfloor\frac{m-1}{2}\right\rfloor
\ge L(\lfloor m/2\rfloor).
\tag{4.3}
$$



In a valid actual summand of (2.3),


$$
m=2n+i-s,\qquad
0\le s\le\min(2n,n+i),
$$


so


$$
n\le m\le2n+b-1.
$$


Since $n$ is even, (4.2)–(4.3) yield


$$
v_2(m!\mathcal F_m)
\ge
1+L(n/2)-\lfloor\log_2(2n+b-1)\rfloor.
$$



The other factor in each summand,


$$
\lambda_s\binom{n+i}{s},
$$


is integral. We have therefore proved:

### Theorem 1 — Whole logarithmic-input estimate

Define


$$
\boxed{
K_F(n,b)=1+L(n/2)-\lfloor\log_2(2n+b-1)\rfloor.
}
\tag{4.4}
$$


Then, on every original index,


$$
\boxed{
h^F\in2^{K_F(n,b)}\mathbb Z_2^b,
\qquad
\mathcal T\widetilde N^{-1}h^F
\in2^{K_F(n,b)}\mathbb Z_2^{b+1}.
}
\tag{4.5}
$$



No logarithmic term has been deleted in the proof. Its eventual omission modulo $2^P$ is justified precisely when $P\le K_F(n,b)$.

### Scope after rescaling

If another column normalization is obtained by multiplying this column by a scalar of valuation $-\delta$, the surviving logarithmic depth is only


$$
K_F(n,b)-\delta.
$$


The source excerpt by itself does not authorize treating an unspecified normalization factor as a binary unit.

---

## 5. Factorial/exponential forcing at variable precision

The exponential part is not highly divisible as a whole. Its low factorial terms must be retained.

For $m\ge0$,


$$
\mathcal D_m
=\sum_{q=0}^m(m)_{\underline q}.
\tag{5.1}
$$


Indeed, substitute $q=m-r$ in its defining sum.

For every nonnegative integer $m$,


$$
(m)_{\underline q}=q!\binom mq.
$$


Hence


$$
v_2((m)_{\underline q})\ge L(q).
$$


At precision $P$,


$$
\boxed{
\mathcal D_m\equiv
\sum_{\substack{q\ge0\\L(q)<P}}(m)_{\underline q}
\pmod{2^P}.
}
\tag{5.2}
$$


The sum is finite, uniformly in $m$; $q<2P$ is a sufficient range.

This includes the $q=0$ term $1$. It is precisely the term that would be lost by treating the whole exponential forcing as near-factorial.

### A bounded-degree retained forcing polynomial

Let $x$ denote the row variable. Define


$$
G_P(x)=
\sum_{\substack{a\ge0,\ q\ge0\\a+L(q)<P}}
\ \sum_{s=0}^{4a}
\lambda_s^{(a)}
\binom{n+x}{s}
(2n+x-s)_{\underline q}.
\tag{5.3}
$$


Zero symbol coefficients are understood as zero.

At every actual row $0\le i<b$,


$$
\boxed{
G_P(i)\equiv h_i^e\pmod{2^P}.
}
\tag{5.4}
$$


Terms with $s>n+i$ vanish because $\binom{n+i}{s}=0$; they are not assigned factorials with negative arguments.

Every summand in (5.3) is an integer-valued polynomial. If it has weight


$$
w=a+L(q),
$$


its degree is at most


$$
s+q\le4a+q.
$$


The elementary estimate


$$
q\le2L(q)+1
$$


gives


$$
s+q\le4w+1.
$$


Since retained weights satisfy $w\le P-1$,


$$
\boxed{\deg G_P\le4P-3.}
\tag{5.5}
$$



This is a degree bound for the **actual complete exponential forcing modulo $2^P$**, not an inference from low shift labels.

---

## 6. An exact finite-boundary contact recurrence

The divided-contact matrix admits a particularly direct polynomial realization.

For a vector $y=(y_0,\ldots,y_{b-1})$, define


$$
Q(x)=\sum_{r=0}^{b-1}y_r\binom{n+x}{r}.
\tag{6.1}
$$


Then (2.1) gives, at every actual row,


$$
(\widetilde Ny)_i
=
\sum_s\lambda_s\binom{n+i}{s}Q(i-s).
\tag{6.2}
$$



Define


$$
(\mathcal H Q)(x)
=
\sum_s\lambda_s\binom{n+x}{s}Q(x-s)
=Q(x)+(\mathcal KQ)(x).
\tag{6.3}
$$



Unlike a formal replacement by an infinite matrix, this identity still requires the actual $b$-row boundary. We enforce it explicitly.

### 6.1 The finite-boundary interpolation operator

Expand an integer-valued polynomial in the Newton basis at $0$:


$$
R(x)=\sum_{r\ge0}c_r\binom xr.
$$


Set


$$
\boxed{
\Pi_bR(x)=\sum_{r=0}^{b-1}c_r\binom xr.
}
\tag{6.4}
$$


Because $\binom ir=0$ when $r>i$,


$$
(\Pi_bR)(i)=R(i)\qquad(0\le i<b).
$$


The map is integral and never increases degree. It is the exact interpolation remainder on the original row set, not an approximation.

The finite contact equation is therefore equivalent to


$$
\boxed{
Q+\Pi_b\mathcal KQ=\Pi_bG,
\qquad \deg Q<b.
}
\tag{6.5}
$$



### 6.2 Precision-safe iteration

Let $\mathcal K_P$ retain complete symbol expansion orders $1\le a<P$. Then


$$
\mathcal K_P:
\operatorname{Int}(\mathbb Z)\longrightarrow
2\operatorname{Int}(\mathbb Z).
$$


Translations by the integers $n,s$, multiplication, and $\Pi_b$ preserve the integral Newton lattice.

For $P\le K_F(n,b)$, initialize


$$
Q^{(0)}=0
$$


and iterate


$$
\boxed{
Q^{(r+1)}
=
\Pi_bG_P-\Pi_b\mathcal K_PQ^{(r)}
\pmod{2^P},
\qquad 0\le r<P.
}
\tag{6.6}
$$


The operator is even, so $P$ iterations suffice. Its result $Q_P$ represents


$$
\widetilde N^{-1}(h^e+h^F)\pmod{2^P}.
$$



### 6.3 Degree bound through inversion

A force summand of weight $w$ has degree at most $4w+1$. A subsequent contact of expansion order $a$ adds:

- at least $a$ to the valuation;
- at most $4a$ to the degree.

A word of total weight $W$ therefore has degree at most $4W+1$. Only $W<P$ survives. Interpolation can only reduce degree.

Thus


$$
\boxed{
\deg Q_P\le\min(b-1,4P-3).
}
\tag{6.7}
$$



Intermediate translations and products must be completed before precision/degree pruning. The bound does not license deleting an intermediate term before its full contact operation has been formed.

---

## 7. Reconstruction, exterior $+1$, and exact support

To recover the actual divided-contact coordinates, expand


$$
Q_P(X-n)=\sum_r y^{(2)}_{r,P}\binom Xr.
\tag{7.1}
$$


This is an integral change of Newton basis by an integer translation. It loses no precision.

From (6.7),


$$
y^{(2)}_{r,P}=0
\qquad
\left(r>\min(b-1,4P-3)\right).
$$


The reconstruction formula (2.4) satisfies


$$
\mathcal T_{jr}=0\qquad(j>r+1).
$$


Consequently:

### Theorem 2 — Complete second-column support at raw precision

For every original index and every integer


$$
1\le P\le K_F(n,b),
$$


the complete column in (2.5) satisfies


$$
\boxed{
(V_w)_j\equiv0\pmod{2^P}
\qquad(j>4P-2).
}
\tag{7.2}
$$


The retained entries are obtained from


$$
\boxed{
(V_w)_{j,P}
=
\delta_{j0}
+
\binom{n+2}{j}
\sum_{r=0}^{\min(b-1,4P-3)}
y^{(2)}_{r,P}
\left[
j\binom{-n}{r-j+1}
-\binom{-n}{r-j}
\right].
}
\tag{7.3}
$$



The exterior $+1$ is explicit in $\delta_{j0}$.

### Boundary clarification

This is a result in the excerpt’s coordinate convention. The earlier formula


$$
4Y_b=W_b(1+b\eta_{b-1})
$$


must still be retained in its own convention. One must not identify its $+1$ with a different coordinate’s $+1$ without the exact coordinate/normalization map.

Within (7.3), the actual endpoint is completely accounted for:

- if $b\le4P-2$, evaluate $j=b$ by the displayed formula;
- if $b>4P-2$, its zero residue follows from the proved support theorem.

No extra terminal-block coordinates are introduced.

---

## 8. Complexity and precision loss

This is a genuine bounded-state reduction, not a renamed sum over $b$ rows.

### Inputs

The recurrence requires:

- the actual integers $n=128C+66$, $b=128D+81$, $h=n/2$;
- the requested raw precision $P$;
- the symbol coefficients from (3.1), for expansion orders $a<P$;
- the factorial terms with $a+L(q)<P$;
- binomial values with lower indices $O(P)$.

The exact units of all these binomials are retained.

### State size

The polynomial state has at most


$$
\min(b,4P-2)
$$


Newton coefficients. If $b$ is enormous, this is $O(P)$. If $b$ is smaller, then $b=O(P)$ already.

A conservative dense implementation of the translations, products, and $P$ iterations has polynomial arithmetic cost, for example $O(P^5)$. This is an arithmetic-operation bound, not a measured runtime claim.

There is **no modular precision loss** in the integral Newton operations. Even denominators in binomial evaluations must be handled by exact cancellation or valuation stripping, never by attempting to invert them modulo $2^P$.

The bit cost also includes reading or generating the required actual parameter residues. No claim is made that an astronomically long integer input can be read in constant time.

### Precision beyond $K_F$

The logarithmic force has not become unavailable when $P>K_F$. It is explicitly defined by (2.3), and must then be included. What has been proved here is a reduced recurrence for the complete column in the stated range


$$
P\le K_F(n,b).
$$


A bounded-degree logarithmic producer beyond that threshold is a further obligation.

---

## 9. Consequences—and nonconsequences—for mixed alignment

Let


$$
Z_w=\mathcal T\widetilde N^{-1}f^0,
\qquad
\mathfrak C=Z_w^TV_w.
$$


Since $f^0$ is integral and the finite inverse is $2$-integral,


$$
Z_w\in\mathbb Z_2^{b+1}.
$$


For $P\le K_F(n,b)$, Theorem 2 gives


$$
\boxed{
\mathfrak C
\equiv
\sum_{j=0}^{\min(b,4P-2)}
(Z_w)_j(V_w)_{j,P}
\pmod{2^P}.
}
\tag{9.1}
$$



Thus the second-force side of the mixed contraction needs only $O(P)$ reconstructed coordinates. Its contribution from the exterior term is specifically


$$
(Z_w)_0,
$$


not zero.

However, (9.1) is **not yet a complete mixed-contraction algorithm**: the needed first-column entries $(Z_w)_j$ must themselves be evaluated in the same normalization without an original-sized inverse. The first-column tail theorem is useful, but it does not automatically supply that missing normalization-aware coordinate evaluation.

Likewise, nothing in Theorem 2 evaluates


$$
Z_w^TZ_w,
$$


or proves the proposed raw norm congruence


$$
\sum_{j=0}^b A_j^2-8S(C,D)
\equiv0\pmod{2^{2\mu+6}}.
$$



### Why relative alignment still does not follow

Three distinctions remain essential:

1. A second-column support theorem is not a scalar cancellation identity.
2. Raw precision is not relative precision until the actual contents and normalization losses are included.
3. Binary scalar alignment is not control of the full primitive denominator.

The certified first-column content must remain the actual value $a$. It cannot be replaced by a model value $\mu$ without a proof.

---

## 10. A concrete next lemma

The new reduction narrows the mixed problem substantially.

> **Normalization-aware first-coordinate lemma.**  
> For the actual first column $Z_w$, evaluate
> 

$$
> (Z_w)_0,\ldots,(Z_w)_{\min(b,4P-2)}
> \pmod{2^P}
>
$$


> by a recurrence of state dimension polynomial in $P$, using the accepted complete first-force filtration and actual endpoint reconstruction. Give explicitly the map between this normalization and the raw $2X_j$ normalization, including every binary valuation loss.

Combined with Theorem 2, this would produce a genuine complete mixed scalar residue without enumerating all $b$ coordinates.

For the norm, a separate unit-sensitive contraction is still needed. A proof of the mixed-coordinate lemma would not, by itself, evaluate the sum of all first-column squares.

### Minimal additional data for applying the new result to the stated raw targets

The missing data are not the second force. It is now explicitly budgeted and reduced.

The additional interface needed is:

- the exact coordinate/scalar map from the excerpt’s $Z_w,V_w$ to the reports’ $2X,4Y$;
- its binary valuation losses;
- the certified actual first-column content and the requested scalar precision;
- an evaluation mechanism for the required first-column coordinates in that normalization.

These are concrete mathematical interfaces, not a request for an original-sized column enumeration.

---

## 11. Bounded exact arithmetic for independent inspection

No tools were executed. No $p_{380}$ calculation is proposed.

Two bounded audits would test the new mechanism directly.

### Audit A: exact finite-system comparison

Use


$$
b\in\{1,3,5\},\qquad n=4002b,\qquad P\in\{2,4,8\}.
$$


These are positive finite systems on the same $n=4002b$ line, but are **not** claimed to lie in the original exponential family.

For each pair:

1. Build the exact matrix $\widetilde N$ from (2.1).
2. Build the complete $h^e+h^F$ from (2.2)–(2.3).
3. Solve the finite system exactly or modulo $2^P$ after valuation-safe cancellation.
4. Independently compute (6.6) and reconstruct with (7.3).

**Expected verifiable outputs:**


$$
\widetilde Ny^{(2)}-(h^e+h^F)\equiv0\pmod{2^P},
$$


agreement of the two reconstructed columns at **every** coordinate $0,\ldots,b$, and an explicit check of the exterior $+1$.

This certifies only those finite cases.

### Audit B: bounded-state calculation on an original index

Use


$$
u=0,\qquad b=9^{18},\qquad n=4002b,\qquad P=8.
$$


First certify from (4.4) that $P\le K_F(n,b)$.

Then compute only the polynomial state of degree at most


$$
4P-3=29.
$$


The expected output is:

- the $30$ Newton coefficients of $Q_P$ modulo $256$;
- the complete polynomial residual in (6.5) modulo $256$;
- the retained values $(V_w)_j\bmod256$ for $0\le j\le30$;
- the theorem-backed certificate
  

$$
(V_w)_j\equiv0\pmod{256}\qquad(31\le j\le b).
$$



This is an original-index calculation with a genuinely precision-sized state. It does not require constructing the $b\times b$ matrix.

---

## 12. Full primitive arithmetic and the whole nonzero error

The final arithmetic remains exactly


$$
N_B=d_B[u,v],
$$




$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2}\ne0,
$$


with


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=\frac{A_B}{g_B},\qquad
p_n=\frac{H_B}{g_B}.
}
$$


The gcd includes **all primes**, and the primitive multiplier remains


$$
\frac{d_B^2}{g_B}.
$$



The whole evaluated error is


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n>0
\quad\text{eventually},
}
$$


where


$$
\log|\epsilon_n|
=
-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$



To obtain irrationality from this construction, one still needs a same-index estimate forcing this entire nonzero quantity to tend to zero. A sufficient condition would be an upper bound for $\log q_n$ with exponential rate strictly below the displayed decay rate. The new second-force theorem supplies no such bound.

---

## Final proof-status ledger

### New results proved

1. The actual finite divided-contact inverse is $2$-integral.
2. The complete logarithmic force, after finite inversion and weighted reconstruction, has depth at least
   

$$
K_F(n,b)=1+v_2((n/2)!)-\lfloor\log_2(2n+b-1)\rfloor.
$$


3. At every raw precision $P\le K_F(n,b)$, the complete second column—including the factorial/exponential force and exterior $+1$—is computable by an endpoint-preserving Newton recurrence of degree at most $4P-3$.
4. In the excerpt’s exact normalization, that column is supported modulo $2^P$ in $0\le j\le4P-2$.
5. The corresponding mixed contraction reduces to $O(P)$ first-column coordinate evaluations, but those evaluations and their normalization bridge remain to be supplied.

### Exact remaining bottleneck

The immediate remaining task is a **normalization-aware, unit-sensitive evaluation of the requisite first-column coordinates and the complete norm contraction**, with actual contents and scalar precision losses included. Beyond that remain the full all-prime gcd and the actual primitive-denominator bound against the whole nonzero evaluated error.



$$
\boxed{\text{The irrationality of }e+\pi\text{ remains unresolved.}}
$$


