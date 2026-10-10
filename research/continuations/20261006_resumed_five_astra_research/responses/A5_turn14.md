> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, turn 14 — Explicit finite Gram kernels, a target-specific carry quotient, and a full-rank obstruction to the natural Green reduction

## Executive conclusions

I do **not** obtain a newly evaluated primitive exponential digit, an original-family bound for the excess norm valuation, or an unconditional irrationality result for $e+\pi$.

There are, however, two concrete advances on the assigned finite-response problem.

1. **Both finite inverse factors and the exterior correction can be eliminated from the remaining long sums.** At paid precision $2^L$, the actual Gram head and complete exponential-response head reduce to a polynomially bounded collection of explicit finite sums of the form
   

$$
\boxed{
   \sum_{j=0}^{b-1}
   \binom{n+2}{j}^{\!2}
   \binom jr
   \binom{\alpha n+b+\eta-j}{b+\varepsilon-j}
   \binom{\alpha'n+b+\eta'-j}{b+\varepsilon'-j},
   }
   \tag{E1}
$$


   where $\alpha,\alpha'\in\{1,2\}$, all offsets and $r$ are precision-sized, and the physical $j=b$ term is evaluated separately and exactly.

   This is more than another matrix expression for $\mathcal B$: the formulas below remove every original-length inner convolution and every original-size inverse. What remains is a specified family of **one-dimensional, finite, weighted binomial kernels**.

2. **The natural source-ladder Green identity does not turn the actual Gram observation into bounded-rank boundary data.** For the exact source-ladder matrix $J$ derived below and the actual
   

$$
G=\mathcal R^T\mathcal R,
$$


   including its physical final diagonal term,
   

$$
\boxed{\operatorname{rank}_{\mathbb Q}(GJ-J^TG)\ge b-2.}
   \tag{E2}
$$


   Thus this particular Green reduction has a bulk defect of essentially full rank, not a fixed collection of endpoint charges. This does **not** rule out a target-specific congruence or a different telescoper, but it identifies a precise obstruction to the most immediate two-boundary argument.

For the kernels in (E1), I also give a direct carry/window quotient, using stripped factorials and four binomial carry channels. Its proved resource bound is exponential in the paid precision and linear in the length of the actual original parameter word. It therefore does **not** yet furnish a feasible new primitive-digit calculation. In particular, it does not inherit the normalized force’s $O(\log(u+2))$-cost residue interface.

The remaining bottleneck is now narrower:

> Compress or evaluate this explicit weighted-binomial kernel family at norm-sensitive precision, while preserving the finite cutoff and the physical terminal. A successful quotient must improve both the present precision-state bound and, for large original exponents, the dependence on the full word of $b=9^{18+32u}$.

No accepted computation is proposed for repetition.

---

## 1. Preserved objects, precision, and scope of reuse

Throughout,


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
$$


The contact space is exactly $0\le i,j<b$, and reconstruction has exactly the physical rows $0\le j\le b$.

Retain


$$
\phi(z)=1-z+\frac{z^2}{2},\qquad
\lambda_s=s![z^s]\phi(z)^n,\qquad
W_j=\binom{n+2}{j},
$$


and


$$
(\mathcal Rz)_j=W_j(jz_{j-1}-z_j),
\qquad z_{-1}=z_b=0.
$$



The two corrected columns remain


$$
x=\frac{\mathcal RA^{-1}f^0}{2R},
\qquad
y=\frac{\mathcal RA^{-1}(h^e+h^F)+e_0}{4b!}.
$$


Write


$$
\mathfrak f=f^0/R,\qquad x=2^ax_0,
$$


and retain


$$
\mathcal B=A^{-T}\mathcal R^T\mathcal RA^{-1},
\qquad
v_{\rm term}=bW_b^2A^{-T}e_{b-1}.
$$



The complete finite factorial subtraction is


$$
k=\frac{h^e-A(j!)_{0\le j<b}}{b!},
$$


so


$$
y^E=\frac14\left(\mathcal RA^{-1}k+W_be_b\right).
$$


Consequently,


$$
Q=x_0^Tx_0
 =2^{-2a-2}\mathfrak f^T\mathcal B\mathfrak f,
$$


and


$$
\boxed{
E=x_0^Ty^E
 =2^{-a-3}\mathfrak f^T(\mathcal Bk+v_{\rm term}).
}
\tag{1.1}
$$



I reuse turn 13’s explicitly derived recurrence, integrality, and filtration:


$$
\mathfrak f_i\in\mathbb Z_2,\qquad
v_2(\mathfrak f_i)\ge\left\lfloor\frac{i+1}{8}\right\rfloor.
$$


I do not describe the separately pending A4 audit as completed.

At raw precision $2^L$, the relevant head is therefore


$$
I=\min\{b-1,8L-2\}.
\tag{1.2}
$$


For primitive output precision $2^K$, the whole divisions require


$$
L=K+2a+2\quad\text{for }Q,
\qquad
L=K+a+3\quad\text{for }E.
\tag{1.3}
$$



The supplied 32-bit operator/Schur receipt is retained only at its stated finite scope: it evaluates the original $u=0$ operator and finite endpoint solve, not the force/head/Gram numerators. I do not rerun it or promote it to a Gram certificate.

---

## 2. A finite factorization suitable for the actual Gram calculation

This section gives explicit definitions for the factors used below, so the kernel derivation does not depend on an ambiguous infinite-matrix convention.

Work modulo $2^L$, and put


$$
m=4(L-1),\qquad d=\min(m,b).
$$


The established symbol and inverse-symbol filtrations give


$$
\lambda_s\equiv c_s\equiv0\pmod{2^L}\qquad(s>m),
$$


where


$$
c_0=1,\qquad
c_s=-\sum_{r=1}^s\binom sr\lambda_rc_{s-r}.
\tag{2.1}
$$



Define the finite matrices


$$
P_{ij}=\binom ij,\qquad
U_{ij}=\binom n{j-i},\qquad
T_{ij}=\binom{n+i}{j},
$$


in their respective triangular ranges, and


$$
H_{rj}=
\begin{cases}
\lambda_{r-j}\binom rj,&r\ge j,\\
0,&r<j.
\end{cases}
$$


Finite Vandermonde gives


$$
T=PU.
\tag{2.2}
$$


The finite inverse of $H$ is


$$
(H^{-1})_{rj}=c_{r-j}\binom rj.
\tag{2.3}
$$



Let $E_{\rm tail}$ inject the final $d$ contact coordinates. For $0\le r<m$, $0\le t<d$, define


$$
K_{rt}
=
\lambda_{d+r-t}\binom{b+r}{d+r-t}.
\tag{2.4}
$$


A coefficient outside $0,\ldots,m$ is zero modulo $2^L$. In particular,


$$
K\equiv0\pmod2.
$$



The exterior Pascal columns are


$$
(T_{\rm ext})_{i,r}=\binom{n+i}{b+r}.
$$


Directly expanding the source formula gives the finite identity


$$
\boxed{
A\equiv
\left(TH+T_{\rm ext}KE_{\rm tail}^T\right)U
\pmod{2^L}.
}
\tag{2.5}
$$


No row or contact column has been added.

### 2.1 Explicit exterior columns after the first inverse factor

For every auxiliary exterior label $v\ge0$, set


$$
F_{jv}
=
-\sum_{q=0}^v
\binom{-n}{b+q-j}\binom n{v-q},
\qquad 0\le j<b.
\tag{2.6}
$$


Then


$$
F_{\cdot v}=T^{-1}\left(\binom{n+i}{b+v}\right)_{0\le i<b}.
$$



Indeed, applying $P^{-1}$ first gives $\binom n{b+v-i}$, and the complete convolution of $(1+z)^{-n}$ with $(1+z)^n$ is zero at positive degree. The omitted part is exactly the finite sum in (2.6).

Let $F^{(m)}=(F_{\cdot0},\ldots,F_{\cdot,m-1})$, and put


$$
G_{\rm end}=E_{\rm tail}^TH^{-1}F^{(m)},\qquad
S=I_d+G_{\rm end}K.
\tag{2.7}
$$


Since $K$ is even, $S\equiv I_d\pmod2$. Thus the Schur inverse is legitimate at every paid precision.

The complete finite inverse is


$$
\boxed{
A^{-1}\equiv
U^{-1}
\left[
H^{-1}
-H^{-1}F^{(m)}KS^{-1}E_{\rm tail}^TH^{-1}
\right]
U^{-1}P^{-1}
\pmod{2^L}.
}
\tag{2.8}
$$



This retains both inverse binomial factors, the inverse contact factor, and the finite exterior correction.

When $m\ge b$, $d=b$: the formula remains finite and correct, but the Schur space has already reached the full contact dimension. No smallness is claimed in that regime.

---

## 3. Explicit inverse-column profiles without original-length inner sums

All binomial coefficients below use the ordinary zero convention for a negative lower index or a lower index exceeding a nonnegative upper index. Negative upper indices occur only in the explicitly displayed generalized binomials such as $\binom{-n}{r}$.

### 3.1 One inverse binomial factor

For $N>0$, define


$$
V^{(N)}_{ji}
=
(-1)^{j-i}
\sum_{q=0}^i
\binom j{i-q}
\binom{N+q-1}{q}
\binom{N+b-j-1}{b-1-j-q}.
\tag{3.1}
$$


Then


$$
V^{(N)}_{ji}=(U_N^{-1}P^{-1})_{ji},
\qquad
(U_N)_{jr}=\binom N{r-j}.
$$



To verify this, start from


$$
\sum_{t=0}^{b-1-j}
\binom{-N}{t}(-1)^{j+t-i}\binom{j+t}{i}.
$$


Use


$$
\binom{j+t}{i}
=\sum_{q=0}^i\binom j{i-q}\binom tq,
$$




$$
\binom{N+t-1}{t}\binom tq
=
\binom{N+q-1}{q}
\binom{N+t-1}{t-q},
$$


and the finite hockey-stick identity. This evaluates the entire original-length sum.

### 3.2 The bulk profile with both inverse factors

Let


$$
B_j=b-1-j.
$$


Define


$$
\begin{aligned}
\mathcal C_{j;s,q,p}
={}&
\binom{2n+B_j+s}{B_j+s-q-p}\\
&-
\sum_{v=1}^{(s-q)_+}
\binom{n+B_j+v-1}{B_j+v-p}
\binom{n+s-v}{s-q-v}.
\end{aligned}
\tag{3.2}
$$



Then the bulk inverse-column profile


$$
Z^{\rm bulk}_{ji}
=(U^{-1}H^{-1}U^{-1}P^{-1})_{ji}
$$


is


$$
\boxed{
\begin{aligned}
Z^{\rm bulk}_{ji}
={}&(-1)^{j-i}
\sum_{s=0}^m(-1)^sc_s
\sum_{q=0}^i
\binom{n+q-1}{q}\binom{s+i-q}{s}\\
&\hspace{12mm}\cdot
\sum_{p=0}^{s+i-q}
\binom j{s+i-q-p}
\binom{n+p-1}{p}
\mathcal C_{j;s,q,p}.
\end{aligned}}
\tag{3.3}
$$



The correction sum in (3.2) is essential. It is the part beyond the actual upper limit $b-1$ that would be incorrectly introduced by an unrestricted convolution.

#### Derivation

Insert (3.1) with $N=n$ into $U^{-1}H^{-1}V^{(n)}$. The polynomial factors combine through


$$
\binom rs\binom{r-s}{i-q}
=
\binom{s+i-q}{s}\binom r{s+i-q}.
$$


Writing $r=j+t$, expand the last binomial in $\binom tp$. The full convolution is the first term of (3.2). Its excess terms have


$$
t=B_j+v,\qquad 1\le v\le(s-q)_+,
$$


and are precisely the displayed correction.

Thus (3.3) contains no original-length inner sum.

### 3.3 Explicit exterior profiles through both factors

For $a\ge0$, define


$$
\begin{aligned}
\mathcal D_{j;a,s,p}
={}&
\binom{2n+B_j+a+s}{B_j+a+s+1-p}\\
&-
\sum_{v=1}^{a+s+1}
\binom{n+B_j+v-1}{B_j+v-p}
\binom{n+a+s-v}{a+s+1-v},
\end{aligned}
\tag{3.4}
$$


and


$$
\boxed{
M_{j,a}
=
(-1)^{b+a-j}
\sum_{s=0}^m(-1)^sc_s
\sum_{p=0}^s
\binom j{s-p}\binom{n+p-1}{p}
\mathcal D_{j;a,s,p}.
}
\tag{3.5}
$$


This is


$$
M_{\cdot,a}
=
U^{-1}H^{-1}
\left(\binom{-n}{b+a-r}\right)_{0\le r<b}.
$$


The proof is the same finite convolution calculation as above.

Consequently,


$$
\boxed{
X_{jv}:=(U^{-1}H^{-1}F_{\cdot v})_j
=
-\sum_{a=0}^v\binom n{v-a}M_{j,a}.
}
\tag{3.6}
$$



For a head column $i$, define the short endpoint vector


$$
D_i
=
E_{\rm tail}^TH^{-1}V^{(n)}_{\cdot i}.
\tag{3.7}
$$


Only $d$ terminal coordinates and at most $m+1$ inverse-symbol shifts are used.

The complete inverse-column profile is therefore


$$
\boxed{
z^{(i)}_j:=(A^{-1}e_i)_j
=
Z^{\rm bulk}_{ji}
-
X_{j,0:m-1}\,KS^{-1}D_i.
}
\tag{3.8}
$$



Equations (3.2)–(3.8) explicitly include both inverse factors and the exterior correction. They do not substitute the infinite inverse for the finite solve.

---

## 4. Complete exponential response from a paid source prefix

The complete factorial subtraction gives


$$
k=\sum_{t=0}^{2n-1}\frac{(b+t)!}{b!}\,\mathbf a_{b+t}.
\tag{4.1}
$$


Every source column remains an auxiliary source column, not an added contact column.

Since


$$
v_2\!\left(\frac{(b+t)!}{b!}\right)\ge v_2(t!)
\ge\left\lfloor\frac t2\right\rfloor,
$$


putting


$$
T_L=\min(2L-1,2n-1)
$$


gives the paid congruence


$$
\boxed{
k\equiv
\sum_{t=0}^{T_L}a_t\mathbf a_{b+t}\pmod{2^L},
\qquad
a_t=\frac{(b+t)!}{b!}.
}
\tag{4.2}
$$



This reuses the complete factorial tail; it does not truncate the aligned residual coefficientwise.

### 4.1 Solving an exterior source column

For $v\ge0$, set


$$
G_v=E_{\rm tail}^TH^{-1}F_{\cdot v},
$$


and


$$
Y_{\cdot v}
=
X_{\cdot v}
-
X_{\cdot,0:m-1}KS^{-1}G_v.
\tag{4.3}
$$


Then $Y_{\cdot v}=A^{-1}T_{\rm ext,\cdot v}$.

Splitting the source convolution at the actual contact boundary gives


$$
\boxed{
(A^{-1}\mathbf a_{b+t})_j
=
F_{jt}
+
\sum_{r=0}^t\binom n{t-r}
\sum_{s=0}^m
\lambda_s\binom{b+r+s}{s}\,Y_{j,r+s}.
}
\tag{4.4}
$$



Here the first term is not optional. It is the finite return from the source indices below $b$:


$$
(U^{-1}U_{\cdot,b+t})_j=F_{jt}.
$$



Combining (4.2) and (4.4) gives an explicit profile


$$
z^k=A^{-1}k\pmod{2^L}
\tag{4.5}
$$


using only the bounded exterior labels


$$
0\le v\le T_L+m.
$$



The coefficients of the $X_{\cdot v}$ can be accumulated before evaluating any weighted sum. Thus the complete response does not require one separate long calculation for every pair $(t,r,s)$.

### 4.2 What has and has not been compressed

At this point:

- the normalized first force has its proved $8L$-prefix;
- the complete exponential source has its paid $2L$-prefix;
- both finite inverse factors and the exterior correction have explicit profiles;
- the remaining original-length operation is the actual weighted reconstruction pairing.

That last operation is addressed next. It has not been silently identified with source compression.

---

## 5. The actual finite weighted-binomial kernels

For a contact profile $z$, define


$$
\Delta_jz=jz_{j-1}-z_j,
\qquad z_{-1}=z_b=0.
$$


Then, exactly,


$$
\boxed{
\mathcal B_{ir}
=
\sum_{j=0}^{b}W_j^2
(\Delta_jz^{(i)})(\Delta_jz^{(r)}),
}
\tag{5.1}
$$


and


$$
\boxed{
(\mathcal Bk+v_{\rm term})_i
=
\sum_{j=0}^{b}W_j^2
(\Delta_jz^{(i)})
\left(\Delta_jz^k+\mathbf1_{j=b}\right).
}
\tag{5.2}
$$



The terminal contribution in (5.2) is exactly


$$
bW_b^2z^{(i)}_{b-1}.
\tag{5.3}
$$


The terminal Gram contribution is


$$
b^2W_b^2z^{(i)}_{b-1}z^{(r)}_{b-1}.
\tag{5.4}
$$



### 5.1 A bounded atom family

Every bulk profile in §§3–4 is a linear combination of atoms


$$
(-1)^j
\binom jd
\binom{\alpha n+b+\eta-j}{b+\varepsilon-j},
\qquad \alpha\in\{1,2\},
\tag{5.5}
$$


with precision-sized $d,\eta,\varepsilon$. All other signs are scalar coefficients.

The reconstruction preserves this form. In particular,


$$
j\binom{j-1}{d}=(d+1)\binom j{d+1},
\tag{5.6}
$$


while replacing $j$ by $j-1$ increases both large-binomial offsets by one.

Products of the polynomial factors reduce integrally:


$$
\binom jd\binom je
=
\sum_{r=\max(d,e)}^{d+e}
\frac{r!}{(r-d)!(r-e)!(d+e-r)!}\binom jr.
\tag{5.7}
$$


No division by a nonunit is needed to evaluate the integer coefficients in (5.7).

The $(-1)^j$ signs cancel in the pairings.

### 5.2 Explicit support bound

Let


$$
D_0=I+2m+T_L+4.
\tag{5.8}
$$


A sufficient common bound for all reconstructed atoms is


$$
|\eta|,|\varepsilon|\le D_0,\qquad d\le D_0.
$$


After multiplying two profiles, $r\le2D_0$.

Hence every required head entry reduces to scalar coefficients, the explicitly evaluated terminal terms, and kernels


$$
\boxed{
\begin{aligned}
\mathcal K^{\alpha,\alpha'}_{\eta,\varepsilon,\eta',\varepsilon';r}
={}&
\sum_{j=0}^{b-1}
\binom{n+2}{j}^{\!2}\binom jr\\
&\quad\cdot
\binom{\alpha n+b+\eta-j}{b+\varepsilon-j}
\binom{\alpha'n+b+\eta'-j}{b+\varepsilon'-j}.
\end{aligned}}
\tag{5.9}
$$



A sufficient bound on the number of distinct kernels is


$$
\boxed{
4(2D_0+1)^5.
}
\tag{5.10}
$$


This bound is deliberately conservative; many coefficients and kernels coincide or vanish.

The original cutoff is still $j<b$, and the actual $W_j^2$ remains in every kernel. Negative lower indices near the endpoint contribute zero, not a continued polynomial value.

### Theorem 5.1 — Explicit finite Gram-head reduction

At precision $2^L$, the actual


$$
\mathcal B_{0:I,0:I},
\qquad
(\mathcal Bk+v_{\rm term})_{0:I}
$$


are determined by:

1. the short symbol and inverse-symbol arrays;
2. a $d\times d$ unit Schur solve;
3. short-lower-index binomial coefficients;
4. the kernel family (5.9);
5. the physical terminal terms (5.3)–(5.4).

All original-length inner convolutions and original-size inverses have been eliminated.

This is a proved reduction to a particular finite summation problem. It is **not yet** a low-cost evaluation theorem for those sums.

---

## 6. Parameter dependence before the weighted sums

The coefficients outside (5.9) are built from short-lower-index binomials.

A sufficient common lower-index bound is


$$
D_*=\max\{3m+T_L+1,\ m+I+1\}.
$$


They are determined modulo $2^L$ by the parameter residue


$$
b\bmod2^P,
\qquad
P=\max\{3L,\ L+v_2(D_*!)\}.
\tag{6.1}
$$


The first term pays the normalized-force interface; the second pays the short binomials.

Since $n=4002b$ and $h=2001b$, this also supplies their required residues. A sufficient original exponent period for these **coefficient data** is


$$
u\longmapsto u+2^{\max(P-8,0)}.
\tag{6.2}
$$



This statement does not include the weighted sums (5.9). Their large lower indices are still present, and their evaluation is the remaining high-word issue.

---

## 7. A target-specific carry/window quotient for the kernels

I now give a direct quotient for (5.9), rather than appeal to generic automaticity.

It establishes an effective bound and exact input dependence. Its present bound is not practically adequate at the desired paid precisions.

### 7.1 Integral prime-power binomial evaluation

Assume $L\ge3$; smaller precisions can be obtained by reduction.

Let


$$
O_L(t)=\prod_{\substack{1\le r\le t\\r\ {\rm odd}}}r
\pmod{2^L}.
$$


The product of all odd residues modulo $2^L$ is $1$, so


$$
O_L(t+2^L)=O_L(t).
\tag{7.1}
$$



The odd part of $N!$ is


$$
\operatorname{odd}(N!)
\equiv
\prod_{a\ge0}O_L\!\left(\left\lfloor\frac N{2^a}\right\rfloor\right)
\pmod{2^L}.
\tag{7.2}
$$


Therefore, for $0\le K\le N$,


$$
\binom NK
\equiv
2^e
\prod_{a\ge0}
\frac{
O_L(\lfloor N/2^a\rfloor)
}{
O_L(\lfloor K/2^a\rfloor)
O_L(\lfloor(N-K)/2^a\rfloor)
}
\pmod{2^L},
\tag{7.3}
$$


where $e$ is the number of binary carries in $K+(N-K)$. Every denominator in (7.3) is odd.

Each unit factor depends on an $L$-bit window. No inverse of $2$, factorial construction, or unproved recurrence is used.

### 7.2 The four actual binomial channels

A kernel term has four distinct binomial channels:

1. $\binom{n+2}{j}$, with multiplicity two;
2. $\binom{\alpha n+b+\eta-j}{b+\varepsilon-j}$;
3. $\binom{\alpha'n+b+\eta'-j}{b+\varepsilon'-j}$;
4. $\binom jr$.

Their complementary lower arguments are respectively


$$
n+2-j,\quad
\alpha n+\eta-\varepsilon,\quad
\alpha'n+\eta'-\varepsilon',\quad
j-r.
$$



Thus only the following variable digit streams occur:


$$
j,\ n+2-j,\ A-j,\ B-j,\ C-j,\ D-j,\ j-r,
$$


together with the cutoff test $b-1-j\ge0$. Here $A,B,C,D$ abbreviate the four fixed large-binomial parameters.

### 7.3 State and transition

Process the bits of $j$ from low to high.

A sufficient state consists of:

- the last $L-1$ bits of $j$;
- seven subtraction/inequality borrow bits;
- four addition-carry bits;
- the accumulated weighted valuation $e\in\{0,\ldots,L-1\}$.

A path reaching valuation $L$ contributes zero and is discarded.

One need not store separate $L$-bit windows for all seven affine streams. The buffered $j$-word, the borrow entering its low end, and the corresponding known parameter window reconstruct each such word. The carry and borrow states then advance by one digit.

For each completed window, multiply the state weight by the four odd-unit ratios from (7.3), squaring the first channel’s ratio. Increase the valuation by the weighted outgoing carries. At the end:

- reject invalid binomial ranges or a failed cutoff;
- multiply the accumulated unit by $2^e$;
- sum all surviving state weights.

This computes exactly (5.9) modulo $2^L$.

### 7.4 Effective resource bound

A sufficient state bound is


$$
\boxed{
S_L\le L\,2^{L+10}.
}
\tag{7.4}
$$


The extra $2^{10}$ is a conservative allowance for the seven borrow and four carry bits after the $L-1$-bit buffer is counted.

If


$$
J_{\rm bit}=O(\log(n+b+D_0)+L),
$$


a direct evaluation of one kernel requires


$$
O(S_LJ_{\rm bit})
$$


residue-ring transitions, with an $O(2^L)$-size odd-prefix table if constant-time window factors are desired.

Together with (5.10), this gives an explicit, albeit excessive, bound for the complete head calculation. The coefficient construction and assembly are polynomial in $I+L$; a conservative direct bound is $O((I+L)^9)$ ring operations outside the digit sums.

### 7.5 Exact original-input dependence

This quotient reads the actual binary parameter windows in $b,n$ and their bounded shifts. For


$$
b=9^{18+32u},
$$


their word length is $\Theta(u+1)$, not $O(\log(u+2))$.

Accordingly:

- the short coefficient data have the residue dependence in §6;
- the weighted kernels presently have a full-word transfer dependence;
- no period in $u$ has been proved for their final values;
- modular exponentiation at $O(L)$-bit precision alone does not supply this quotient’s input.

This does not prove that every kernel intrinsically needs every high bit. It proves that the displayed quotient has not removed that dependence.

### Practical verdict

At $L=32$, even the conservative single-kernel state bound is already far too large. Primitive observation precision may require substantially larger $L$ because of (1.3).

Therefore this is a **proved target-specific quotient with an inadequate resource bound**, not a commissioned scalar algorithm. I do not propose allocating its full state space or rerunning the old producer.

---

## 8. The two-boundary force and the exact adjoint pairing

Turn 13’s complete source identity is retained:


$$
\mathscr L_n
\left(
\frac{\phi^ng_n-e^z\phi^nU_b}{b!}
\right)
=
e^z\phi^{n+1}(C_{b-1}+C_b),
$$


and hence


$$
k_{i+2}-\alpha_i k_{i+1}+\beta_i k_i-\chi_i k_{i-1}
=\Gamma_i,
\qquad 0\le i\le b-3.
\tag{8.1}
$$


Both $C_{b-1}$ and $C_b$ remain present.

Let $D$ denote the $(b-2)\times b$ operator in (8.1), and let $g\in\mathbb Q^b$ be any actual observation vector.

Set $\lambda_i=0$ outside $0\le i\le b-3$, and solve backward


$$
\lambda_{j-2}
=
g_j+\alpha_{j-1}\lambda_{j-1}
-\beta_j\lambda_j+\chi_{j+1}\lambda_{j+1},
\qquad j=b-1,\ldots,2.
\tag{8.2}
$$


Define


$$
\gamma_0=g_0-\beta_0\lambda_0+\chi_1\lambda_1,
$$




$$
\gamma_1=g_1+\alpha_0\lambda_0-\beta_1\lambda_1+\chi_2\lambda_2.
\tag{8.3}
$$


Then


$$
g=D^T\lambda+\gamma_0e_0+\gamma_1e_1,
$$


so the exact finite Green pairing is


$$
\boxed{
g^Tk
=
\gamma_0k_0+\gamma_1k_1
+\sum_{i=0}^{b-3}\lambda_i\Gamma_i.
}
\tag{8.4}
$$



For the actual exponential observation, take $g=\mathcal B\mathfrak f$ and add


$$
\mathfrak f^Tv_{\rm term}.
$$


Thus


$$
\boxed{
2^{a+3}E
=
\gamma_0k_0+\gamma_1k_1
+\sum_{i=0}^{b-3}\lambda_i\Gamma_i
+\mathfrak f^Tv_{\rm term}.
}
\tag{8.5}
$$



This pays the complete forcing and the physical terminal.

Because $D\mathfrak f=0$,


$$
\boxed{
\mathfrak f^T\mathcal B\mathfrak f
=
\gamma_0\mathfrak f_0+\gamma_1\mathfrak f_1.
}
\tag{8.6}
$$


Equation (8.6) is a two-charge representation of the norm, but computing those charges still requires the actual backward response. It is not a new norm bound.

The homogeneous eight-step contraction does not delete the sum in (8.5): $g=\mathcal B\mathfrak f$ is not known to have a short response support, and the new forcing values continue throughout the physical range.

---

## 9. Why the natural Gram Green identity has a bulk obstruction

There is an exact source-ladder identity that tests whether the two source boundaries can remove the observation-size problem.

The source polynomials satisfy


$$
C_j'=C_{j-1},
$$




$$
(j+1)C_{j+1}=(n+z-j)C_j+zC_{j-1}.
$$


Therefore


$$
\boxed{
(1-z)C_j'-(n+z)C_j
=
C_{j-1}-jC_j-(j+1)C_{j+1}.
}
\tag{9.1}
$$



On the contact coefficient vector, the corresponding interior ladder is


$$
(Jz)_\ell=z_{\ell+1}-\ell z_\ell-\ell z_{\ell-1}.
\tag{9.2}
$$


At the finite ends, the omitted terms are precisely boundary terms. Applied to the factorial vector, this is the source of the two columns $C_{b-1},C_b$.

A Green argument using the actual Gram metric would need the defect


$$
GJ-J^TG
$$


to be boundary-supported or otherwise compressible.

But the actual Gram matrix is


$$
G_{ii}=W_i^2+(i+1)^2W_{i+1}^2,
\qquad
G_{i,i+1}=-(i+1)W_{i+1}^2,
\tag{9.3}
$$


including $b^2W_b^2$ in its final diagonal entry.

For $0\le i\le b-3$,


$$
\boxed{
(GJ-J^TG)_{i,i+2}
=
-(i+1)\left(W_{i+1}^2+(i+2)W_{i+2}^2\right).
}
\tag{9.4}
$$


This is nonzero over $\mathbb Q$.

The defect has bandwidth two. Its submatrix with rows $0,\ldots,b-3$ and columns $2,\ldots,b-1$ is lower triangular with the nonzero entries (9.4) on its diagonal. Hence:

### Theorem 9.1 — Full-rank bulk defect of the natural Gram ladder

On every original index,


$$
\boxed{
\operatorname{rank}_{\mathbb Q}(GJ-J^TG)\ge b-2.
}
\tag{9.5}
$$



### Exact obstruction and limitation

This proves that the natural source-ladder integration-by-parts identity does **not** have a bounded-rank Gram boundary defect. The complete squared-binomial metric cannot be treated as a compatible full classical measure merely because the source has a short ladder.

It does not prove:

- that the defect has the same rank modulo $2^L$;
- that its pairing with the particular forced profiles cannot simplify;
- that another, higher-order telescoper cannot exist;
- that a bounded-precision observable quotient is impossible.

Those are separate target-specific questions.

The outstanding Green lemma must therefore control the **actual forced pairing of this bulk defect**, or replace the ladder by a demonstrably compatible telescoper with all finite charges paid. Merely invoking the two source columns or the homogeneous contraction is insufficient.

---

## 10. The new follow-on lemma

The finite-response problem can now be stated without unspecified matrix inverses.

### Weighted-kernel response lemma

For the kernels (5.9), at the paid precision


$$
L=K+a+3
$$


and the actual head $I=\min(b-1,8L-2)$, prove one of the following:

1. **A small observable carry quotient:** identify reachable/observable state identifications that reduce the bound (7.4) to a feasible size, and specify whether the final output depends only on an explicit residue of $u$ or on an additional compressed high-word invariant.

2. **A paid finite telescoper:** evaluate the kernels through a bounded collection of endpoint charges, with every interior defect and every prime-power division explicitly controlled.

3. **An original forced-pairing estimate:** prove a norm-excess or complete-resonance bound directly for the particular linear combination of kernels occurring in (5.1)–(5.2).

The first option is now a finite, concrete quotient problem. It is not a request to close an unrestricted formal automaton.

The second must overcome the full-rank defect (9.5); it cannot assume the natural ladder is Gram-self-adjoint.

The third must use the actual forced coefficients. Bounds for arbitrary primitive vectors or individual summands remain insufficient.

A nonzero result obtained this way would feed the already closed conditional half-length theorem. That conditional theorem is not claimed as a new result here.

---

## 11. Primitive normalization, logarithmic forcing, and whole error

Nothing above changes the producer or its final reduction.

Retain


$$
\omega_j=j!W_j,\qquad
u_j=\frac{2\Lambda R\,x_j}{\omega_j},\qquad
v_j=\frac{4b!\,y_j}{\omega_j},
$$


and the actual least simultaneous clearer


$$
d_B=
\operatorname{lcm}_{0\le j\le b}
\{\operatorname{den}(u_j),\operatorname{den}(v_j)\}.
$$


No reconstructed row content is divided out.

The final integers and all-prime gcd remain


$$
A_B=d_B^2\,4\Lambda^2R^2N,
\qquad
H_B=d_B^2\,8\Lambda Rb!H,
$$




$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
}
\tag{11.1}
$$


For every prime,


$$
v_p(q_n)
=
\max\{v_p(\mathscr D_n)+v_p(N)-v_p(H),0\}.
\tag{11.2}
$$



The logarithmic source remains


$$
\mathcal L_m=m![z^m]\frac{F(z)}{1-z}.
$$


Its omission is justified only at the audited guard


$$
B_*=n-v_2(b!)-1-2s_2(n)-\ell.
$$


A requested primitive digit beyond that guard requires the complete original logarithmic contribution. The exponential kernels above are not a replacement for it.

Finally, the evaluated expression remains


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n,
\qquad
\epsilon_n=\frac{p_n}{q_n}-(e+\pi).
}
\tag{11.3}
$$


Any asymptotic conclusion still requires the whole same-index error, its stated eventual nonvanishing, and every prime in the actual primitive denominator.

No new result here supplies that final comparison.

---

## 12. Arithmetic status and exact next calculation

### What has been proved without a new computation

No bounded arithmetic calculation is needed to establish:

- the explicit inverse profiles (3.3), (3.5), and (3.8);
- the complete boundary-source response (4.4);
- the finite weighted-kernel reduction (5.9);
- its support bound;
- the carry/window evaluation rule and resource bound;
- the exact Green pairing;
- the rank obstruction (9.5).

These are symbolic finite identities and explicit bounds.

### What has not been evaluated

No new value is asserted for:

- $a$;
- a primitive norm digit;
- a primitive exponential digit;
- a half-length observation;
- a final gcd or denominator;
- a whole primitive error.

### Exact inputs and expected output of the unresolved arithmetic layer

For a genuinely new primitive exponential layer, the inputs would be:

1. an original index $u$;
2. a certified actual content $a$;
3. a chosen new output depth $K$;
4. $L=K+a+3$ and $I=\min(b-1,8L-2)$;
5. the short coefficient data of §§2–6;
6. the actual kernels (5.9) at modulus $2^L$, including the separate terminal.

The verifiable output would be


$$
\mathcal E_i=(\mathcal Bk+v_{\rm term})_i
\pmod{2^L},
\qquad 0\le i\le I,
$$


followed by the **whole** paid division


$$
\boxed{
E\bmod2^K
=
2^{-a-3}
\sum_{i=0}^I\mathfrak f_i\mathcal E_i
\bmod2^K.
}
\tag{12.1}
$$


If nonzero, the output must include its first nonzero digit. If zero, it establishes only that new finite layer.

The present carry bound does not justify commissioning this calculation at useful paid precision. Accordingly, (12.1) is an **unevaluated specification**, not a receipt or a claim of practical feasibility.

No old 32-bit producer, accepted operator/Schur calculation, optional logarithmic zero, final gcd, or whole-error computation is requested again.

---

## 13. Proof-status ledger

| Statement | Status |
|---|---|
| Normalized first-force recurrence and $8L$-prefix | Reused from turn 13; no claim that the separate audit is complete |
| Complete factorial subtraction and both boundary source columns | Retained exactly |
| Finite inverse with both binomial factors and exterior correction | Explicitly derived |
| Original-length inner inverse convolutions eliminated | Proved by finite binomial summation |
| Complete exponential response from paid source prefix | Proved |
| Actual $W_j^2$, finite cutoff, and physical terminal retained | Yes |
| Polynomially bounded family of explicit weighted-binomial kernels | Proved |
| Target-specific carry/window quotient | Proved |
| Feasible state bound at useful paid precision | Not obtained |
| Compressed original-$u$ dependence for the weighted kernels | Not obtained |
| Exact adjoint Green pairing with complete $\Gamma$ | Proved |
| Natural Gram-ladder defect has rank at least $b-2$ | New original-family obstruction |
| A different paid telescoper or forced defect cancellation | Open |
| Newly evaluated primitive $E$ digit | Not obtained |
| Original-family norm-excess or resonance theorem | Open |
| All-prime denominator versus whole nonzero same-index error | Unresolved |
| Irrationality or rationality of $e+\pi$ | Unresolved |

---

## Conclusion

The finite Gram-response obligation has advanced from an unspecified inverse problem to an explicit finite weighted-binomial summation problem.

The new constructive result is:


$$
\boxed{
\begin{gathered}
\text{both inverse factors and the complete exterior correction}\\
\text{reduce the actual Gram and exponential-response heads to (5.9),}\\
\text{with precision-sized offsets and the true physical terminal.}
\end{gathered}}
$$



The new obstruction is:


$$
\boxed{
\operatorname{rank}_{\mathbb Q}
\bigl((\mathcal R^T\mathcal R)J-J^T(\mathcal R^T\mathcal R)\bigr)
\ge b-2.
}
$$


Thus the immediate source-ladder Green argument does not replace the complete exponential observation by a fixed set of true boundary charges. Its bulk defect must still be paid.

The exact remaining bottleneck is the evaluation or further quotienting of the explicit kernels (5.9), including their high-word dependence. The direct carry quotient is rigorous but too large; it does not yet justify a new primitive-digit computation.

**No new primitive exponential digit or linear norm/resonance bound is claimed. The unconditional proof or disproof of irrationality of $e+\pi$ remains open.**
