> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, turn 11 — A logarithmic-guard correction, a first-column content bound, and an exact exponential nonresonance theorem

## Executive conclusions

The stronger logarithmic guard is valid for the **original complete source**, with one coefficient-identity correction that matters for the audit:



$$
\mathcal L_m=m\mathcal L_{m-1}+g_m
\quad\Longrightarrow\quad
\mathcal L_m=m![z^m]\frac{F(z)}{1-z},
$$


not $m![z^m](e^zF(z))$. The coordinator’s valuation proof uses the former, correct recurrence and its correct finite sum. Thus its conclusion survives this correction:



$$
\boxed{
y^F\in 2^{B_n}\mathbb Z_2^{b+1},
\qquad
B_n=n-v_2(b!)-2-3\ell,
\qquad
\ell=\lfloor\log_2(2n+b-1)\rfloor.
}
$$



The earlier assertion that the available logarithmic guard necessarily falls below the required $0.54109n$-scale is therefore superseded. The new guard protects that target unless the actual first-column content plus primitive norm loss is itself linear.

This turn supplies two further arithmetic results.

### 1. The actual first-column content is logarithmically bounded

On the original family, write


$$
x=2^a x_0,\qquad x_0\in\mathbb Z_2^{b+1}\ \text{primitive},
\qquad
\nu=v_2(x_0^Tx_0).
$$


Then


$$
\boxed{
0\le a\le \lfloor\log_2(n+2)\rfloor-1.
}
\tag{E1}
$$



This is a bound for the **actual corrected first column**, not for a homogeneous reference polynomial. Its proof uses the exact first-force row $i=1$, the actual finite inverse, and the finite reconstruction.

Consequently, failure of the new logarithmic target guard cannot be attributed to a linear first-column content. At $k\sim\eta n$, it requires a genuine primitive norm loss


$$
\boxed{
\nu\ge
\left(1-\frac1{4002}-\eta\right)n+O(\log n)
\approx 0.45866\,n+O(\log n).
}
\tag{E2}
$$



### 2. The complete exponential source has an exact factorial alignment

Let


$$
\sigma_n=\sum_{r=0}^{n}\frac1{r!}=\frac{\mathcal D_n}{n!},
$$


where $\mathcal D_m=m\mathcal D_{m-1}+1$, and let $\mathscr D_n$ be the retained final scalar. There is an exact integer


$$
c_n=\mathscr D_n\sigma_n
$$


with


$$
\boxed{
v_2(c_n)=d_n^{E}:=\frac n2-v_2(b!)-1.
}
\tag{E3}
$$



The complete exponential column admits the exact decomposition


$$
\boxed{
y^E=c_nx+z^E,
}
\tag{E4}
$$


where $z^E$ is given below by a complete finite tail source and the actual terminal return. No row or force term is omitted.

Put


$$
Q=x_0^Tx_0,\qquad
\Psi=x_0^Tz^E,\qquad
L=x_0^T(2^{-B_n}y^F).
$$


Then


$$
\boxed{
\delta_2
=
v_2\!\left(c_n2^aQ+\Psi+2^{B_n}L\right)-a-\nu.
}
\tag{E5}
$$



This yields a genuine relative-depth theorem. If


$$
a+\nu+d_n^{E}<B_n
$$


and


$$
v_2(\Psi)\ne a+\nu+d_n^{E},
$$


then


$$
\boxed{\delta_2\le d_n^{E}.}
\tag{E6}
$$


The first inequality has the particularly simple exact form


$$
\boxed{
a+\nu<\frac n2-1-3\ell.
}
\tag{E7}
$$



Thus every index outside the half-linear deep-norm regime is excluded unless a specifically identified **complete exponential residual** resonates with the factorial-aligned norm term.

Under the retained whole-error theorem, (E6) implies


$$
v_2(q_n)\ge n-s_2(n)
$$


and


$$
\boxed{
|q_n\epsilon_n|\longrightarrow\infty
}
$$


along every infinite original sequence satisfying these nonresonance hypotheses. The exponential growth margin is


$$
\log2+\left(1-\frac1{8004}\right)\log3-\beta
=0.02865\ldots>0.
$$



This is not a uniform exclusion of the original family. The unresolved cases are now explicit:

1. an original-power primitive norm loss of approximately half-linear size; or
2. a precisely paid exponential resonance, followed where necessary by complete logarithmic cancellation.

No new computation was executed or requested. In particular, the $b=9,\ K=20000$ logarithmic diagnostic is unnecessary and is not proposed.

---

## 1. Original domain, finite objects, and retained denominator

Throughout,


$$
\boxed{
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
}
$$


The contact indices remain


$$
0\le i,j<b,
$$


and reconstructed rows remain


$$
\boxed{0\le j\le b.}
$$



Set


$$
h=\frac n2,\qquad
R=2^h\binom nh,\qquad
\Lambda=\frac{(n!)^2}{2^n}.
$$


Here $\Lambda$ denotes the scalar called $\lambda$ in turn 10; the symbol coefficients retain the notation


$$
\lambda_s=s![z^s]\left(1-z+\frac{z^2}{2}\right)^n.
$$



The actual matrix and first force are


$$
A_{ij}
=
\sum_{s=0}^{n+i}
\lambda_s\binom{n+i}{s}\binom{2n+i-s}{j},
\tag{1.1}
$$




$$
f_i^0
=
\frac{(n+i)!}{n!}
[t^n](1+2t+2t^2)^n(1+t)^i.
\tag{1.2}
$$



The reconstruction is


$$
(\mathcal Rz)_j=W_j(jz_{j-1}-z_j),
\qquad
W_j=\binom{n+2}{j},
\qquad z_{-1}=z_b=0.
\tag{1.3}
$$


Thus


$$
Z_w=\mathcal RA^{-1}f^0,
\qquad
V_w=\mathcal RA^{-1}(h^e+h^F)+e_0,
$$


and


$$
x=\frac{Z_w}{2R},\qquad
y=\frac{V_w}{4b!},\qquad
N=x^Tx,\qquad H=x^Ty.
\tag{1.4}
$$



All subsequent decompositions are identities for these columns.

The final weighted producer is unchanged:


$$
A_B=d_B^2\,4\Lambda^2R^2N,\qquad
H_B=d_B^2\,8\Lambda Rb!H,
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
\tag{1.5}
$$


No independent row primitivization is made.

The retained scalar is


$$
\mathscr D_n=\frac{\Lambda R}{2b!}
=\frac{(n!)^2\binom n{n/2}}{2^{n/2+1}b!}\in\mathbb Z_{>0}.
$$


Hence


$$
\frac{p_n}{q_n}=\frac{H}{\mathscr D_nN},
$$


and at every prime $p$,


$$
v_p(q_n)
=
\max\{v_p(\mathscr D_n)+v_p(N)-v_p(H),0\}.
\tag{1.6}
$$



In particular,


$$
v_2(q_n)=\max\{C_n-\delta_2,0\},
$$


where


$$
C_n=\frac{3n}{2}-v_2(b!)-s_2(n)-1,
\qquad
\delta_2=v_2(H)-v_2(N).
\tag{1.7}
$$



The historical ternary theorem is reused:


$$
\boxed{
v_3(q_n)=n-\frac{b+15}{2}=\frac{8003b-15}{2}.
}
\tag{1.8}
$$


It is not re-established by a new finite calculation.

---

## 2. Independent audit of the stronger complete logarithmic guard

### 2.1 A coefficient-label correction

The original source defines


$$
\mathcal L_0=0,\qquad
\mathcal L_m=m\mathcal L_{m-1}+g_m,
\qquad
g_m=F^{(m)}(0).
$$


Dividing the recurrence by $m!$ gives


$$
\frac{\mathcal L_m}{m!}
=
\sum_{r=1}^{m}\frac{g_r}{r!}.
$$


Therefore


$$
\boxed{
\mathcal L_m
=
\sum_{r=1}^{m}\frac{m!}{r!}g_r
=
m![z^m]\frac{F(z)}{1-z}.
}
\tag{2.1}
$$



It is not generally equal to $m![z^m](e^zF(z))$. The latter equals


$$
\sum_{r=1}^{m}\binom mr g_r.
$$


For example, $g_1=g_2=g_3=2$, so the two expressions at $m=3$ are respectively $20$ and $14$.

This does not invalidate the proposed guard for the original producer: the coordinator’s proof uses exactly the correct finite sum in (2.1). It does mean that the displayed $e^zF(z)$ identification must not be retained as a source identity.

### 2.2 Symbol coefficient payment

The ordinary coefficient expansion is


$$
[z^s]\phi(z)^n
=
\sum_{r=0}^{\lfloor s/2\rfloor}
(-1)^{s-2r}
\binom n{s-r}\binom{s-r}{r}2^{-r},
\qquad
\phi(z)=1-z+\frac{z^2}{2}.
$$


Consequently,


$$
\boxed{
v_2(\lambda_s)
\ge v_2(s!)-\lfloor s/2\rfloor
=\lceil s/2\rceil-s_2(s).
}
\tag{2.2}
$$


This is a valuation inequality obtained before any modular reduction. No inverse of a nonunit factorial is used.

For the even producer, integrality and the stronger small-index parity properties are already available from


$$
\phi(z)^2=1+2V(z)
$$


in divided-power coordinates. The estimate (2.2) is compatible with those facts; it need not replace them.

### 2.3 Complete logarithmic scalar payment

The rational identity


$$
\frac1{\phi(z)}
=
\frac{1+z+z^2/2}{1+z^4/4}
$$


is exact. It gives


$$
v_2([z^k]\phi(z)^{-1})\ge-\lfloor k/2\rfloor.
$$


Since


$$
g_r=2(r-1)![z^{r-1}]\phi(z)^{-1},
$$


we obtain


$$
v_2(g_r)
\ge
1+v_2((r-1)!)-\lfloor(r-1)/2\rfloor.
\tag{2.3}
$$



For a summand in (2.1),


$$
\begin{aligned}
v_2\!\left(\frac{m!}{r!}g_r\right)
&\ge
1+v_2(m!)-v_2(r)-\lfloor(r-1)/2\rfloor\\
&\ge
1+v_2(m!)
-\lfloor\log_2m\rfloor-\lfloor(m-1)/2\rfloor.
\end{aligned}
$$


Thus


$$
\boxed{
v_2(\mathcal L_m)
\ge
\lfloor m/2\rfloor+2-s_2(m)-\lfloor\log_2m\rfloor.
}
\tag{2.4}
$$



The whole finite convolution is retained.

### 2.4 Joint payment in each original source summand

The actual complete source is


$$
h_i^F
=
\sum_{s=0}^{n+i}
\lambda_s\binom{n+i}{s}\mathcal L_{2n+i-s}.
$$


Write


$$
m=2n+i-s.
$$


Then


$$
n\le m\le 2n+b-1,\qquad s+m=2n+i.
$$


Combining (2.2) and (2.4),


$$
\begin{aligned}
v_2\!\left(\lambda_s\binom{n+i}{s}\mathcal L_m\right)
&\ge
\lceil s/2\rceil+\lfloor m/2\rfloor
+2-s_2(s)-s_2(m)-\lfloor\log_2m\rfloor\\
&\ge
n+\lfloor i/2\rfloor-3\ell,
\end{aligned}
$$


where


$$
\ell=\lfloor\log_2(2n+b-1)\rfloor.
$$


Therefore


$$
\boxed{
v_2(h_i^F)\ge n+\lfloor i/2\rfloor-3\ell.
}
\tag{2.5}
$$



The matrix $A^{-1}$ and reconstruction $\mathcal R$ are integral over $\mathbb Z_2$. After the actual division by $4b!$,


$$
\boxed{
y^F=\frac{\mathcal RA^{-1}h^F}{4b!}
\in2^{B_n}\mathbb Z_2^{b+1},
\qquad
B_n=n-v_2(b!)-2-3\ell.
}
\tag{2.6}
$$



This proves the stronger guard for the original complete source.

### Audit conclusion

The new valuation theorem passes after correcting the coefficient label in §2.1. Its linear coefficient is


$$
B_n=\left(1-\frac1{4002}\right)n+O(\log n).
$$



The old $0.49975n$-scale logarithmic-precision obstruction in A5 turn 10 and A4 turn 15 is superseded. At the auxiliary input $b=9,n=36018$, the formula gives $B_n=35961$; that is a proved guard, not an unexecuted receipt.

---

## 3. New theorem: a logarithmic bound for actual first-column content

The next result addresses one of the two losses in the target guard.

### Theorem 3.1 — Actual content bound

For every original index,


$$
\boxed{
a:=\min_{0\le j\le b}v_2(x_j)
\le \lfloor\log_2(n+2)\rfloor-1.
}
\tag{3.1}
$$



The retained integrality of $x$ gives $a\ge0$.

### Proof

Write $n=2h$. On the original family,


$$
h=2001b
$$


is odd.

Let


$$
c_k=[t^k](1+2t+2t^2)^{2h}.
$$


Then the first two contact coefficients are


$$
J_0=c_{2h},\qquad
J_1=c_{2h}+c_{2h-1},
$$


and


$$
f_1^0=(n+1)J_1.
\tag{3.2}
$$



We first prove


$$
\frac{c_{2h}}R\in2\mathbb Z_2,
\qquad
\frac{c_{2h-1}}R\in\mathbb Z_2^\times.
\tag{3.3}
$$



Define


$$
T_r=
\frac{2^r(h!)^2}{(h-r)!^2(2r)!}
=
\frac{2^r(r!)^2}{(2r)!}\binom hr^2.
$$


The central coefficient expansion gives


$$
\frac{c_{2h}}R=\sum_{r=0}^{h}T_r.
$$


Its summands satisfy


$$
v_2(T_r)=r-s_2(r)+2v_2\binom hr.
\tag{3.4}
$$


Here


$$
T_0=1,\qquad T_1=h^2,
$$


both odd, while $r-s_2(r)\ge1$ for $r\ge2$. Hence $c_{2h}/R$ is even.

Similarly,


$$
\frac{c_{2h-1}}R
=
\sum_{r=0}^{h-1}\frac{h-r}{2r+1}T_r.
\tag{3.5}
$$


The $r=0$ term is the odd integer $h$. The $r=1$ term is even because $h-1$ is even. Every term with $r\ge2$ is even by (3.4); $2r+1$ is an odd denominator. Thus the second assertion in (3.3) follows.

It follows from (3.2) that


$$
\boxed{
v_2(f_1^0)=v_2(R).
}
\tag{3.6}
$$


In particular,


$$
v_2\!\left(\frac{f_1^0}{2R}\right)=-1.
\tag{3.7}
$$



This half-integral contact coordinate is important: the normalized contact force is not being assumed integral.

Set


$$
z=A^{-1}\frac{f^0}{2R}.
$$


Because $A\in\operatorname{GL}_b(\mathbb Z_2)$, multiplication by $A^{-1}$ preserves the minimum coordinate valuation. Consequently,


$$
\min_jv_2(z_j)
=
\min_i v_2\!\left(\frac{f_i^0}{2R}\right)
\le-1.
\tag{3.8}
$$



Now restrict reconstruction temporarily to its first $b$ rows. The map


$$
z\longmapsto (jz_{j-1}-z_j)_{0\le j<b}
$$


is lower triangular with diagonal $-1$, hence belongs to $\operatorname{GL}_b(\mathbb Z_2)$. It also preserves minimum coordinate valuation. Multiplication of row $j$ by $W_j$ can increase that valuation by at most


$$
\max_{0\le j<b}v_2\binom{n+2}{j}.
$$


The binary borrow formula gives


$$
v_2\binom{n+2}{j}\le\lfloor\log_2(n+2)\rfloor.
$$


Therefore at least one of these actual reconstructed rows has valuation at most


$$
-1+\lfloor\log_2(n+2)\rfloor.
$$


Adding the physical row $j=b$ cannot increase the minimum. This proves (3.1). ∎

### Consequence for the new target guard

For any integer $k$, failure of the strict target guard


$$
B_n>a+\nu+k
$$


implies


$$
\boxed{
\nu\ge B_n-k-\lfloor\log_2(n+2)\rfloor+1.
}
\tag{3.9}
$$



Thus at $k\sim\eta n$, the exceptional regime is a **primitive norm** regime. Linear first-column content has been ruled out.

---

## 4. Exact factorial alignment of the complete finite force

The next identity is the source of the relative-depth theorem.

### Lemma 4.1 — Complete factorial moment identity

For every contact row $0\le i<b$,


$$
\boxed{
\sum_{s=0}^{n+i}
\lambda_s\binom{n+i}{s}(2n+i-s)!
=
\Lambda f_i^0.
}
\tag{4.1}
$$



### Proof

Put $d=n+i$. Since


$$
\lambda_s=s![z^s]\phi(z)^n,
$$


the left side is


$$
d!\sum_{s=0}^{d}
[z^s]\phi(z)^n\frac{(n+d-s)!}{(d-s)!}.
$$


Using


$$
(1-z)^{-n-1}
=
\sum_{k\ge0}\frac{(n+k)!}{n!\,k!}z^k,
$$


this equals


$$
n!d![z^d]\phi(z)^n(1-z)^{-n-1}.
\tag{4.2}
$$



Under the formal coefficient substitution $z=t/(1+t)$,


$$
[z^d]G(z)
=
[t^d](1+t)^{d-1}G\!\left(\frac{t}{1+t}\right).
$$


Also,


$$
\phi\!\left(\frac{t}{1+t}\right)
=
\frac{1+t+t^2/2}{(1+t)^2}.
$$


Thus the coefficient in (4.2) is


$$
[t^{n+i}](1+t+t^2/2)^n(1+t)^i.
$$


Reciprocating this polynomial of degree $2n+i$ gives


$$
2^{-n}[t^n](1+2t+2t^2)^n(1+t)^i.
$$


Therefore (4.2) is


$$
\frac{n!(n+i)!}{2^n}
[t^n](1+2t+2t^2)^n(1+t)^i
=
\Lambda f_i^0.
$$


∎

This is a complete source identity with the original $s$-range. It is not a short-symbol congruence.

---

## 5. A complete exponential residual with its finite terminal

The exponential scalar satisfies


$$
\mathcal D_m
=
m!\sum_{r=0}^{m}\frac1{r!}.
$$


Every factorial index in the force is at least $n$. Therefore, with


$$
\sigma_n=\sum_{r=0}^{n}\frac1{r!},
$$


we have the exact split


$$
\mathcal D_m
=
\sigma_n m!+\sum_{r=n+1}^{m}\frac{m!}{r!}.
$$



Define the full tail source


$$
\boxed{
\rho_i
=
\sum_{s=0}^{n+i}
\lambda_s\binom{n+i}{s}
\sum_{r=n+1}^{\,2n+i-s}
\frac{(2n+i-s)!}{r!},
\qquad 0\le i<b.
}
\tag{5.1}
$$


An inner sum is empty when its upper endpoint is $n$.

Every factorial quotient in (5.1) is an integer. By Lemma 4.1,


$$
\boxed{
h^e=\sigma_n\Lambda f^0+\rho.
}
\tag{5.2}
$$



Consequently,


$$
y^E
=
\frac{\mathcal RA^{-1}h^e+e_0}{4b!}
=
\mathscr D_n\sigma_n x
+
\frac{\mathcal RA^{-1}\rho+e_0}{4b!}.
\tag{5.3}
$$



Set


$$
c_n=\mathscr D_n\sigma_n,
\qquad
z^E=\frac{\mathcal RA^{-1}\rho+e_0}{4b!}.
\tag{5.4}
$$


Then


$$
\boxed{y^E=c_nx+z^E.}
\tag{5.5}
$$



### 5.1 The scalar and every division are paid

Since $n$ is even,


$$
\mathcal D_n=n\mathcal D_{n-1}+1
$$


is odd. Thus


$$
\begin{aligned}
v_2(c_n)
&=v_2(\mathscr D_n)-v_2(n!)\\
&=\frac n2-v_2(b!)-1.
\end{aligned}
$$


Write


$$
\boxed{
d_n^{E}=\frac n2-v_2(b!)-1,
\qquad
c_n=2^{d_n^{E}}u_n,\quad u_n\in\mathbb Z_2^\times.
}
\tag{5.6}
$$



In fact $c_n$ is an ordinary integer on the original family. Indeed,


$$
c_n
=
\mathcal D_n\,
\frac{(n!/b!)\binom n{n/2}}{2^{n/2+1}}.
$$


The numerator before the power-of-two division is an integer, and its binary valuation is at least the required exponent. No odd-prime denominator remains.

Since $y^E,x\in\mathbb Z_2^{b+1}$ and $c_n\in\mathbb Z$, equation (5.5) proves


$$
z^E\in\mathbb Z_2^{b+1}.
$$


This pays the $4b!$-division in (5.4); it is not being performed as an invalid modular inversion.

### 5.2 Equivalent form with the physical terminal visible

Let


$$
t=(j!)_{0\le j<b}.
$$


The exact finite identity is


$$
\mathcal Rt=-e_0+b!W_be_b.
$$


Hence


$$
\boxed{
z^E
=
\frac{
\mathcal RA^{-1}(\rho-At)+b!W_be_b
}{4b!}.
}
\tag{5.7}
$$



This expression retains:

- all $b$ contact rows;
- the full matrix $A$, not an infinite extension;
- the complete source $\rho$;
- the actual subtraction $At$;
- the physical row $b$;
- the terminal $b!W_be_b$.

The terminal has not been moved into an invented additional contact equation.

---

## 6. Exact relative depth and a nonresonance theorem

Write


$$
x=2^a x_0,\qquad
Q=x_0^Tx_0=2^\nu Q_*,\qquad Q_*\in\mathbb Z_2^\times,
$$


and put


$$
z=a+\nu.
$$


Define


$$
\Psi=x_0^Tz^E,\qquad
L=x_0^T(2^{-B_n}y^F).
$$


Both are in $\mathbb Z_2$.

Equations (2.6) and (5.5) give


$$
H
=
c_nN+2^a\Psi+2^{a+B_n}L.
$$


Therefore


$$
\boxed{
\delta_2
=
v_2\!\left(
2^{z+d_n^{E}}u_nQ_*+\Psi+2^{B_n}L
\right)-z.
}
\tag{6.1}
$$



For clarity, $\Psi$ itself is the exact finite contraction


$$
\boxed{
\Psi
=
\frac{
w^T(\rho-At)+b!W_bx_{0,b}
}{4b!},
\qquad
w=A^{-T}\mathcal R^Tx_0.
}
\tag{6.2}
$$



### Theorem 6.1 — Complete exponential nonresonance

Suppose


$$
z+d_n^{E}<B_n.
\tag{6.3}
$$


If


$$
v_2(\Psi)\ne z+d_n^{E},
\tag{6.4}
$$


then


$$
\boxed{
\delta_2
=
\min\{d_n^{E},\,v_2(\Psi)-z\}
\le d_n^{E}.
}
\tag{6.5}
$$



#### Proof

The logarithmic term in (6.1) has valuation strictly greater than $z+d_n^{E}$. The two remaining displayed terms have distinct valuations by (6.4), so their sum has the smaller valuation. That smaller valuation is still below $B_n$, and the logarithmic term cannot alter it. Subtracting $z$ proves (6.5). ∎

The guard (6.3) simplifies exactly:


$$
B_n-d_n^{E}
=
\frac n2-1-3\ell.
$$


Thus the theorem applies whenever


$$
\boxed{
a+\nu<\frac n2-1-3\ell
}
\tag{6.6}
$$


and the complete residual fails to resonate at the specified depth.

This is stronger than merely saying that “only the exponential source matters.” It identifies:

1. an explicit norm-aligned exponential term;
2. its exact valuation;
3. the exact complete residual that must match that valuation;
4. the nonresonance alternative and its resulting bound for $\delta_2$.

It does **not** prove that (6.4) holds on every original index.

---

## 7. The necessary linear gap becomes an explicit exponential congruence

Let $k>d_n^{E}$ be an integer.

### Theorem 7.1 — Target-specific protected congruence

If


$$
B_n>z+k,
\tag{7.1}
$$


then $\delta_2\ge k$ is equivalent to


$$
\boxed{
v_2(\Psi)=z+d_n^{E}
}
\tag{7.2}
$$


and


$$
\boxed{
u_nQ_*+\frac{\Psi}{2^{z+d_n^{E}}}
\equiv0\pmod{2^{\,k-d_n^{E}}}.
}
\tag{7.3}
$$



#### Proof

The logarithmic term in (6.1) vanishes modulo $2^{z+k}$. Since $k>d_n^{E}$, divisibility of the remaining sum by $2^{z+k}$ requires $\Psi$ to have exactly the valuation of the norm-aligned term. After this paid division, the remaining requirement is (7.3). ∎

The strict inequality in (7.1) also protects the digit at depth $z+k$. For the divisibility test alone, $B_n\ge z+k$ is sufficient.

At the denominator-relevant scale $k\sim\eta n$,


$$
k-d_n^{E}
=
\left(\eta-\frac12+\frac1{4002}\right)n+o(n)
\approx0.04134\,n+o(n).
\tag{7.4}
$$



This number reappears, but with a different mathematical meaning from turn 10:

- **Old, now superseded claim:** the available logarithmic guard did not reach the target.
- **New proved reduction:** under the stronger guard, the complete exponential residual must first match a known norm-aligned term, then cancel it through approximately another $0.04134n$ digits.

It would be incorrect to describe (7.4) as a remaining defect in the new logarithmic estimate.

---

## 8. Whole-error consequence of nonresonance

The retained whole-error theorem is


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
\qquad
\log|\epsilon_n|=-\beta n+o(n),
$$


where


$$
\beta=\left(2+\frac1{4002}\right)\log(1+\sqrt2),
$$


with the retained eventual nonvanishing.

If $\delta_2\le d_n^{E}$, then


$$
v_2(q_n)
\ge C_n-d_n^{E}
=n-s_2(n).
\tag{8.1}
$$


Combining this with the actual ternary denominator gives


$$
q_n
\ge
2^{\,n-s_2(n)}
3^{\,n-(b+15)/2}.
\tag{8.2}
$$



This is a lower bound for the **actual all-prime primitive denominator**. Other primes can only increase it.

Consequently,


$$
\begin{aligned}
\log|q_n\epsilon_n|
&\ge
\left[
\log2+
\left(1-\frac1{8004}\right)\log3-\beta
\right]n+o(n)\\
&=
(0.02865\ldots)n+o(n).
\end{aligned}
\tag{8.3}
$$



### Corollary 8.1

Under the retained whole-error theorem, every infinite original sequence satisfying the hypotheses of Theorem 6.1 has


$$
\boxed{|q_n\epsilon_n|\to\infty.}
$$



This excludes a precisely stated nonresonant portion of the original family. It is not a selected-prime success argument for irrationality, and it does not replace the whole error by its exponential part.

The complete evaluated error remains


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n.
}
$$



---

## 9. The actual deep-norm regime is not discarded

There are two distinct thresholds.

### 9.1 Target-protection threshold

Failure of $B_n>z+k$ requires


$$
\nu\ge B_n-k-a.
$$


By Theorem 3.1, at $k\sim\eta n$ this requires


$$
\nu\ge0.45866\ldots\,n+O(\log n).
$$



### 9.2 First-resonance threshold

Failure of $B_n>z+d_n^{E}$ requires


$$
\boxed{
\nu\ge\frac n2-1-3\ell-a.
}
\tag{9.1}
$$


Again using Theorem 3.1,


$$
\nu\ge\frac n2-O(\log n).
$$



Thus there is an intermediate range in which the logarithmic force can affect the final target congruence but cannot affect the first required exponential resonance.

### Proposition 9.1 — Intermediate deep-norm criterion

Suppose


$$
z+d_n^{E}<B_n\le z+k.
$$


Then $\delta_2\ge k$ holds if and only if


$$
v_2(\Psi)=z+d_n^{E}
$$


and


$$
\boxed{
u_nQ_*
+\frac{\Psi}{2^{z+d_n^{E}}}
+2^{B_n-z-d_n^{E}}L
\equiv0\pmod{2^{\,k-d_n^{E}}}.
}
\tag{9.2}
$$



Every displayed division is paid by the required first-resonance valuation.

### Proposition 9.2 — Half-linear deep-norm criterion

Suppose


$$
B_n\le z+d_n^{E}.
$$


For $k>d_n^{E}$, the condition $\delta_2\ge k$ is equivalent to


$$
\Psi\in2^{B_n}\mathbb Z_2
$$


and


$$
\boxed{
\frac{\Psi}{2^{B_n}}
+L
+2^{z+d_n^{E}-B_n}u_nQ_*
\equiv0\pmod{2^{\,z+k-B_n}}.
}
\tag{9.3}
$$



Both propositions follow directly from (6.1), reducing first at the lowest displayed depth and only then dividing.

These formulas do not assert that either deep regime is populated on the original powers. They also do not assume it is empty. They specify exactly what the actual original producer must satisfy there, including the whole logarithmic contribution.

---

## 10. A boundary-preserving examination of primitive norm exceptions

There is an additional exact structural fact about the original norm. It explains why a content bound alone cannot close the deep-norm branch.

Recall


$$
\omega_j=j!W_j=(n+2)_{\underline j}.
$$


For every reconstructed first column,


$$
\sum_{j=0}^{b}\frac{x_j}{\omega_j}=0.
\tag{10.1}
$$


Indeed, after division by $j!W_j$, reconstruction telescopes using $z_{-1}=z_b=0$.

Multiplying by $\omega_b$,


$$
\boxed{
x_b=-\sum_{j=0}^{b-1}t_jx_j,
\qquad
t_j=\frac{\omega_b}{\omega_j}\in\mathbb Z.
}
\tag{10.2}
$$


This is the actual finite endpoint relation.

Every $t_j$, $j<b$, contains the factor


$$
n+3-b=4001b+3.
$$


The original powers satisfy $b\equiv1\pmod8$, so


$$
v_2(4001b+3)=2.
$$


Thus


$$
t_j\in4\mathbb Z,
\qquad
x_{0,b}\in4\mathbb Z_2.
\tag{10.3}
$$



If


$$
\zeta=(x_{0,0},\ldots,x_{0,b-1})^T,
\qquad
t=(t_0,\ldots,t_{b-1})^T,
$$


then $\zeta$ is primitive and


$$
\boxed{
Q=\zeta^T(I+tt^T)\zeta.
}
\tag{10.4}
$$



The matrix $I+tt^T$ is unimodular over $\mathbb Z_2$. More precisely, it is integrally equivalent to the standard sum-of-squares form. Since $t^Tt\in16\mathbb Z_2$, choose


$$
s=\sqrt{1+t^Tt}\equiv1\pmod8.
$$


Then


$$
M=I+\frac{tt^T}{1+s}\in\operatorname{GL}_b(\mathbb Z_2),
$$


because $v_2(1+s)=1$ while every entry of $tt^T$ is divisible by $16$, and


$$
M^TM=M^2=I+tt^T.
$$


Therefore


$$
Q=(M\zeta)^T(M\zeta).
\tag{10.5}
$$



This proves two useful limitations precisely.

1. The physical endpoint does not introduce a hidden nonunit determinant that by itself bounds $\nu$.
2. Primitivity and positivity do not furnish a uniform upper bound for $\nu$. Standard primitive sum-of-squares forms in sufficiently many variables admit arbitrarily deep binary zeros.

The second observation is **not** an original-domain counterexample. The actual vector $\zeta$ is fixed by the complete force and matrix; it cannot be chosen freely. What remains to be proved is an arithmetic restriction on that forced vector along


$$
b=9^{18+32u}.
$$



The accepted finite and separator results remain evidence only at their stated depths. They do not supply a half-linear bound for this actual norm.

---

## 11. What has and has not been proved about the linear gap

The following implications are now rigorous.

### A. Content cannot create the linear exception



$$
a=O(\log n)
$$


has been proved for the actual corrected first column.

### B. A favorable original index must exhibit a specific exceptional mechanism

For any target $k>d_n^{E}$, one of the following must occur if $\delta_2\ge k$:

1. **Protected exponential resonance:** equations (7.2)–(7.3);
2. **Intermediate deep-norm resonance:** equation (9.2);
3. **Half-linear deep-norm complete-source cancellation:** equation (9.3).

The sources, matrices, row ranges, terminal and divisions in all three systems are explicit.

### C. Nonresonance has a denominator-relevant consequence

Outside the half-linear deep-norm regime, failure of the first exponential resonance gives


$$
\delta_2\le d_n^{E},
$$


which is already below the necessary gap by a fixed linear margin. Under the retained error theorem, that portion of the original route fails exponentially.

### D. The unresolved statement is genuinely arithmetic

I have not proved any of the following:

- $\nu=o(n)$ on the original powers;
- a uniform bound $\nu<0.45866n+o(n)$;
- absence of the exact resonance (7.2);
- a sublinear bound for the additional cancellation in (7.3);
- existence of an original sequence satisfying the favorable congruences.

In particular, Theorem 6.1 must not be relabeled as an unconditional uniform bound for $\delta_2$.

---

## 12. Concrete follow-on lemma

The new decomposition gives a more specific next target than an unspecified higher-precision Gram calculation.

Let


$$
d=d_n^{E},\qquad z=a+\nu,
$$


and retain the exact complete tail source $\rho$ from (5.1).

> **Original-power exponential-resonance lemma.**  
> For some fixed $\varepsilon>0$, prove on the original powers that, whenever
> 

$$
> z+d<B_n,\qquad v_2(\Psi)=z+d,
>
$$


> the complete normalized residue
> 

$$
> u_nQ_*+\frac{\Psi}{2^{z+d}}
> +2^{B_n-z-d}L
>
$$


> has valuation less than
> 

$$
> \left(\eta-\frac12+\frac1{4002}-\varepsilon\right)n
>
$$


> for all sufficiently large original indices in that regime.

Where $B_n>z+k$, the logarithmic term is automatically invisible at the specified target and can be removed from this lemma with the proved guard. Where it is not invisible, it must remain.

A separate necessary branch is now sharply identified:

> **Original forced-norm exception lemma.**  
> Bound, or construct and analyze, original indices satisfying
> 

$$
> \nu\ge\frac n2-1-3\ell-a,
>
$$


> using the actual vector determined by (1.1)–(1.4), not arbitrary primitive vectors in the quadratic lattice.

These are not assertions proved in this turn. The first is the remaining relative exponential cancellation problem; the second is the remaining genuinely deep original norm problem.

If instead a favorable sequence is constructed, the all-prime denominator budget still has to be met. The exact identity remains


$$
\log|q_n\epsilon_n|
=
(\kappa-\beta)n
-\min(\delta_2,C_n)\log2
+\sum_{p\ne2,3}v_p(q_n)\log p
+o(n).
$$


Binary success alone does not control the nonnegative last sum.

---

## 13. Computation status and proof ledger

### No new bounded computation is required for the results above

The proofs use exact coefficient identities, finite matrix integrality, and valuation comparisons.

I do not propose:

- a $b=9$ ternary rerun;
- the $b=9,\ K=20000$ logarithmic diagnostic;
- an accepted high-counter or high-block rerun;
- regeneration of an accepted producer, final gcd, denominator, or whole error.

There is no claimed finite output for an unexecuted calculation.

For independent symbolic verification, the relevant exact inputs are:

- the complete matrix formula (1.1);
- the first-force formula (1.2);
- the original scalar recurrences;
- the full tail source (5.1);
- the finite endpoint identity $\mathcal Rt=-e_0+b!W_be_b$.

The verifiable outputs are the identities (3.6), (4.1), (5.5), and (6.1). No bounded scan is needed to establish them.

| Statement | Status |
|---|---|
| Historical ternary denominator law | Reused at its original scope |
| Stronger complete logarithmic guard | **Proved after correcting the coefficient label** |
| $m![z^m](e^zF)=\mathcal L_m$ | **False for the stated recurrence; corrected in §2.1** |
| Actual first-column content $a\le\lfloor\log_2(n+2)\rfloor-1$ | **New proof** |
| Complete factorial-force identity | **New explicit proof** |
| Complete exponential split $y^E=c_nx+z^E$ | **New exact identity** |
| Exact valuation $v_2(c_n)=n/2-v_2(b!)-1$ | **Proved** |
| Relative exponential nonresonance theorem | **Proved with explicit hypotheses** |
| Protected and deep-regime congruence criteria | **Proved equivalences** |
| Whole-error divergence in the nonresonant regime | **Deduction under the retained whole-error theorem** |
| Uniform exclusion of all original deep norms or resonances | Open |
| Favorable original infinite sequence with sufficient all-prime cancellation | Open |
| Irrationality or rationality of $e+\pi$ | Unresolved |

---

## Conclusion

The stronger logarithmic estimate changes the precision picture materially. For the original complete recurrence it proves


$$
\boxed{
B_n=n-v_2(b!)-2-3\ell,
}
$$


so logarithmic omission is justified at the necessary linear target except in a precisely defined deep-norm regime. The erroneous $e^zF(z)$ coefficient label has been corrected rather than silently adopted.

The new unconditional arithmetic advances are:



$$
\boxed{
a=O(\log n)
}
$$


for the actual corrected first column, and


$$
\boxed{
y^E=c_nx+z^E,\qquad
v_2(c_n)=\frac n2-v_2(b!)-1,
}
$$


with an explicit complete finite residual and the physical terminal retained.

These yield the exact relative nonresonance theorem:


$$
\boxed{
\begin{gathered}
a+\nu<\frac n2-1-3\ell,\\
v_2(x_0^Tz^E)\ne a+\nu+\frac n2-v_2(b!)-1
\end{gathered}
\quad\Longrightarrow\quad
\delta_2\le\frac n2-v_2(b!)-1.
}
$$


Under the retained whole-error theorem, that bound already forces the actual primitive whole error to diverge.

The remaining mathematical bottleneck is therefore narrower but not closed: **actual original-power primitive norm exceptions and exact complete exponential resonance**, with logarithmic terms retained whenever their proved guard no longer protects the required digit. A favorable resolution would still require control of every remaining prime in the genuine final denominator.

No unconditional proof or disproof of the irrationality of $e+\pi$ follows.
