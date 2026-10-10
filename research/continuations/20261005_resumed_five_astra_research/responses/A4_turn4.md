> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 Turn 4 — Independent audit and a precision-safe interface for the next carry

## 1. Executive conclusion

**The arbitrary-monomial finite transport and the coefficient-sensitive parameter cylinder in A5 turn2 pass this audit, at the retained contact-conjugation interface.** In particular, I find no missing factorial, transpose, lower-boundary term, exterior column, or surviving mixed insertion in its formulas for $P_{128}$ and $Q_{256}$.

The coordinator’s supplied certificate supplies the bounded arithmetic evaluation; the mathematical transport and cylinder arguments supply its original-domain applicability. These are different contributions, and neither is a substitute for the other.

There is, however, a precise reconstruction trap that must be corrected before the high carry:

> **The old coordinate-coefficient period $128$ cannot be reused at the new raw precisions.**  
> With the new certified coefficients,
> 

$$
> U_0(128)-U_0(0)\equiv64\pmod{128},
> \qquad
> V_{-2}(x+128)-V_{-2}(x)\equiv128\pmod{256}.
>
$$


> Thus replacing all new coefficient values at $j=128t+\rho$ by their values at $\rho$ is invalid.

A safe corrected interface uses **coefficient period $256$**, or equivalently retains the parity of $t$ when working in $128$-blocks. The actual weights, moments, and finite ranges remain unchanged.

The other main conclusions are:

* $X,Y\bmod64$ determine $N\bmod256$ and $H\bmod128$, but not generally $H\bmod256$.
* Raw divisions by $2$, $4$, and the scalar divisions below are exact divisions of divisible residue classes, **not inversions of even numbers**.
* Weight-depth-four coordinates must be retained. Their norm contributions can be $64\bmod256$, and their mixed-defect contributions can be $64\bmod128$.
* A hypothetical $H\equiv N\pmod{128}$ gives $\gamma=\alpha$ if $\alpha\le6$. If $\alpha\ge7$, it gives only $\gamma\ge7$, with the resulting one-sided denominator bound stated in §8.

No new alignment modulo $128$, unrestricted relative-valuation theorem, or irrationality result is proved here.

I have used no tools and performed no fresh execution or recomputation of the completed certificate.

---

## 2. Scope and fixed arithmetic inputs

Throughout, retain exactly


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0,
$$


and


$$
b=128D+81,\qquad n=128C+66,\qquad C=4002D+2532.
$$


All actual contact matrices have interior indices


$$
0\le i,j<b.
$$



I reuse the accepted whole-parent result


$$
H\equiv N\pmod{64}
$$


and the established integrality


$$
X,Y\in2\mathbb Z_2^{b+1}.
$$



The supplied coordinator certificate gives the following complete nonzero coefficient ranges, with zeros thereafter through the proved degree bound:


$$
\begin{aligned}
p_{0:15}={}&
(34,31,71,69,48,12,4,4,96,72,120,72,0,64,64,64)
\pmod{128},\\
q_{0:15}={}&
(180,164,152,6,112,48,192,8,32,160,64,240,0,0,0,128)
\pmod{256},\\
d_{0:15}={}&q-2p\\
={}&(112,102,10,124,16,24,184,0,96,16,80,96,0,128,128,0)
\pmod{256}.
\end{aligned}
$$


The boundary polynomial has Newton coefficients


$$
\mathscr A=(106,2,88,47)\pmod{128}.
$$



These are bounded exact arithmetic inputs. Their applicability for arbitrary original $b$ follows from the argument audited next—not from the three finite shifted-reference checks.

---

## 3. Audit of arbitrary-monomial finite transport

### 3.1 Divided derivatives and row conventions

The correct convention is


$$
\partial^{[s]}=\frac1{s!}\frac{d^s}{dz^s}.
$$


Divided Leibniz differentiation gives


$$
(1+z)^{-n}\partial^{[s]}\!\left(z^i(1+z)^n\right)
=
\sum_{v=0}^{s}
\binom{i}{s-v}\binom nv
z^{i-s+v}(1+z)^{-v}.
$$


Consequently the row-$i$, column-$j$ kernel is


$$
C_s(i,j)=
\sum_{v=0}^{s}
\binom{i}{s-v}\binom nv
\binom{-v}{j-i+s-v}.
$$



This agrees with the retained degree-four matrix when multiplied by the divided-power coefficients


$$
(u_1,u_2,u_3,u_4)=(-1,2,-3,3).
$$


There is no additional $s!$, and the matrix is not transposed.

This agreement establishes the extension **within the retained contact-row convention**. It is not an independent reconstruction of original matrices absent from the packet.

### 3.2 Lower and upper boundaries

Put $y=i-s+v$. For $v\ge1$, signing the input and output converts the negative-binomial kernel to


$$
(-1)^{s-v}\binom{i}{s-v}\binom nv
\sum_{j=y}^{b-1}
\binom{v+j-y-1}{v-1}f(j).
$$



There are two exhaustive cases:

* If $i<s-v$, then $\binom{i}{s-v}=0$. No negative-index value is inserted into the actual matrix action.
* Otherwise $0\le y\le i<b$, and the suffix is exactly from $y$ to $b-1$.

For $v=0$, only the shifted entry $j=i-s$ survives, again killed when $i<s$.

Thus


$$
\mathscr C_sf(x)=
\sum_{v=0}^{s}(-1)^{s-v}
\binom{x}{s-v}\binom nv
\mathscr T_{v,b}f(x-s+v)
$$


is correct on every actual interior row. Its polynomial continuation does not enlarge the finite matrix.

### 3.3 All nine exterior entries

For a column $b+a$, $0\le a\le8$, the $v=0$ condition would require $b+a=x-s$, impossible on $x<b$. The remaining terms give exactly


$$
\mathscr A_s(x)=
\sum_{a=0}^{8}\sum_{v=1}^{s}
(-1)^{b+a+s-v}B_a
\binom{x}{s-v}\binom nv
\binom{b+a-x+s-1}{v-1}.
$$


Its degree is at most $s-1$.

All nine values


$$
B=(197,234,54,56,248,208,112,128,128)\pmod{256}
$$


must remain in the complete reconstruction. Some entries may disappear from a particular weighted contact insertion, but that does not remove them from the exterior solution.

The whole exponential tail and whole logarithmic force are omitted only under their retained complete-tail bounds.

### 3.4 The $128V$ insertion

The transported correction is


$$
K^{II}=66E^{II}+128F^{II}\pmod{256},
$$


where


$$
F=C_2+C_5+C_7+C_8.
$$


All entries are integral. Therefore every word containing a $128F$ insertion and any additional $66E$ insertion is divisible by


$$
128\cdot66\in256\mathbb Z.
$$


Words containing two $128F$ insertions also vanish. This is a statement about actual finite matrix products; it does not require the false substitution $F=E^2/2$.

For the exterior insertion, modulo $2$, only $B_0$ and $v=2$ survive. Hence


$$
\mathscr J(x)\equiv
x+(1+x)\binom x3+(1+x)\binom x5+x\binom x6
\equiv x+\binom x7\pmod2.
$$


Thus the surviving term is correctly


$$
128\mathscr J=128\left(x+\binom x7\right)\pmod{256}.
$$



**Transport verdict:** the finite block formulas and insertion accounting pass.

---

## 4. Audit of degree bounds and the sufficient parameter cylinder

### 4.1 Coefficient-valued suffix estimates

For fixed integer evaluation argument $y$,


$$
\binom{v+k-y-1}{v-1}f(k)
$$


is an integer-valued polynomial in $k$, of degree at most $d+v-1$ if $\deg f=d$. Its Newton coefficients in $k$ are integers. Summing that expansion gives endpoint terms involving only


$$
\binom br,\qquad r\le d+v.
$$



This proves the endpoint loss bound uniformly at every integer $y$. Taking finite differences in the evaluation variable then proves the corresponding Newton-coefficient divisibility. There is no hidden rational-coefficient loss.

In particular,


$$
\deg\mathscr C_sf\le d+s,
\qquad
\deg\mathscr Ef\le d+4.
$$



### 4.2 Graded inverse truncation

The certified forcing has a decomposition with depth-degree pairs


$$
(a,d_a)=(0,3),(2,5),(4,7),(6,11).
$$


Modulo $128$, the retained iteration counts are respectively


$$
6,\quad4,\quad2,\quad0.
$$


Therefore the four degree bounds are


$$
27,\quad21,\quad15,\quad11.
$$


This justifies


$$
P_{128}=\sum_{\ell=0}^{6}(-66)^\ell\mathscr E^\ell g
\pmod{128},
\qquad \deg P_{128}\le27.
$$



For $Q$, the exterior $U$-insertion already supplies one factor $66$. Thus


$$
Q_{256}
=
66\sum_{\ell=0}^{6}(-66)^\ell\mathscr E^\ell\mathscr A
+128\mathscr J
\pmod{256}
$$


contains every surviving term, and has degree at most $27$.

The certificate’s zeros in degrees $16,\ldots,27$ consequently certify a complete reduction, not an unexplained truncation.

### 4.3 Weighted $b$-shift losses

For the $P$-term of depth $a+\ell$, a $256$-shift of $b$ gives the coefficientwise lower bound


$$
a+\ell+8-\lfloor\log_2(d_a+4\ell)\rfloor.
$$


For every retained $\ell\ge1$, this is at least $7$. The initial limiting case is


$$
1+8-\lfloor\log_2 7\rfloor=7.
$$



For a $Q$-term with $m$ total $U$-insertions, the endpoint index is at most $4m-1$, and the corresponding bound is


$$
m+8-\lfloor\log_2(4m-1)\rfloor\ge8,
\qquad1\le m\le7.
$$


The exterior sign is unchanged under $b\mapsto b+256z$.

A $512$-shift of $n$ loses at most two bits in a $U$-operator. The weighted bounds therefore also meet the required precisions. The $128V$ insertion requires only parity.

Accordingly,


$$
P_{128}(n,b)=P_{128}(322,209)\pmod{128},
$$




$$
Q_{256}(n,b)=Q_{256}(322,209)\pmod{256}
$$


hold coefficientwise on the original domain, using the supplied uniform forcing class.

**Cylinder verdict:** $n=322,b=209$ is legitimate for the bounded coefficients. It is not legitimate as a replacement for the actual $T(-2n)$, weights, moment kernels, or matrix dimensions.

---

## 5. Corrected moment reconstruction: the new coefficient period is not $128$

Let


$$
A=2n,\qquad L_j=b-1-j,\qquad
\mathcal M_s(j)=\binom{A+L_j}{L_j-s}.
$$


Use the complete certified coefficients and define


$$
F_s(x)=\binom{A+s-1}{s}
\sum_{r=s}^{15}p_r\binom{x}{r-s},
$$




$$
G_s(x)=\binom{A+s-1}{s}
\sum_{r=s}^{15}d_r\binom{x}{r-s}.
$$


Put


$$
Z_{-k}=\beta_k,\quad1\le k\le9,
\qquad
Z_s=G_s\quad(s\ge0),
$$


where


$$
\beta=(113,202,78,200,248,80,240,128,128).
$$


Zero-extend unspecified indices, and set


$$
U_s(x)=F_s(x)+xF_s(x-1)+xF_{s+1}(x-1),
$$




$$
V_s(x)=Z_s(x)+xZ_s(x-1)+xZ_{s+1}(x-1).
$$



The safe complete ranges are


$$
-1\le s\le15\quad\text{for }U,
\qquad
-10\le s\le15\quad\text{for }V.
$$



### 5.1 A safe bounded factor replacement

Here $A-644$ is divisible by $1024$. Since $s\le15$,


$$
v_2\!\left(
\binom{A+s-1}{s}-\binom{644+s-1}{s}
\right)\ge7.
$$


This suffices directly for $F\pmod{128}$. Every $d_r$ is even, so it also suffices for $G\pmod{256}$.

Thus one may use


$$
\boxed{\binom{644+s-1}{s}}
$$


in these bounded coefficient polynomials. This does not replace the actual moments.

### 5.2 Explicit failure of period $128$

Since $F_0=P$,


$$
U_0(128)-U_0(0)\equiv P(128)-P(0)\pmod{128}.
$$


The certified vector gives


$$
P(128)-P(0)\equiv
71\binom{128}{2}\equiv64\pmod{128};
$$


the other terms vanish at this precision.

Independently, the complete exterior reconstruction gives


$$
V_{-2}(x)=202+59x\pmod{256},
$$


so


$$
V_{-2}(x+128)-V_{-2}(x)\equiv128\pmod{256}.
$$



These are concrete counterexamples to reusing the lower-precision coordinate period.

### 5.3 Corrected period

Binomial translation by $256$, combined with the displayed coefficient depths, proves


$$
F_s(x+256)\equiv F_s(x)\pmod{128},
\qquad
G_s(x+256)\equiv G_s(x)\pmod{256}.
$$


For example, the odd $p_r$ occur only through degree three, so the worst loss is one bit; the higher coefficients supply the extra divisibility. For $d_r$, the depth-one coefficients occur only through degree two, and the remaining coefficients again provide sufficient margin.

Reconstruction preserves these congruences. Hence


$$
\boxed{
U_s(x+256)\equiv U_s(x)\pmod{128},\qquad
V_s(x+256)\equiv V_s(x)\pmod{256}.
}
$$



In $128$-block notation, the correct coefficient evaluation is therefore at


$$
\rho+128(t\bmod2),
$$


not necessarily at $\rho$.

The original interior ranges remain


$$
j=128t+\rho<b:
\quad
\begin{cases}
0\le t\le D,&0\le\rho\le80,\\
0\le t\le D-1,&81\le\rho\le127.
\end{cases}
$$


The endpoint remains separate. No terminal audit is repeated here.

---

## 6. A division-safe scalar interface for the next carry

For interior coordinates, write


$$
\mathcal F_j=\sum_{s=-1}^{15}U_s(j)\mathcal M_s(j),
\qquad
\mathcal G_j=\sum_{s=-10}^{15}V_s(j)\mathcal M_s(j).
$$


Then


$$
2X_j\equiv(-1)^{j+1}W_j\mathcal F_j\pmod{128},
$$




$$
4(Y_j-X_j)\equiv(-1)^{j+1}W_j\mathcal G_j\pmod{256}.
$$



### 6.1 Dividing raw columns

The map


$$
2\mathbb Z/128\mathbb Z\longrightarrow\mathbb Z/64\mathbb Z,
\qquad [a]\longmapsto[a/2]
$$


is well-defined by exact division. Likewise,


$$
4\mathbb Z/256\mathbb Z\longrightarrow\mathbb Z/64\mathbb Z.
$$



Thus the raw columns determine $X,Y\bmod64$. No inverse of $2$ or $4$ is taken.

For even $x,y$,


$$
(x+64a)^2-x^2\in256\mathbb Z_2,
$$


and


$$
(x+64a)(y+64b)-xy\in128\mathbb Z_2.
$$


Consequently


$$
\boxed{X,Y\bmod64\ \Longrightarrow\ N\bmod256,\ H\bmod128.}
$$


The corresponding mixed difference need not vanish modulo $256$.

### 6.2 Raw whole-sum formulas

Define


$$
S=\sum_{j<b}W_j^2\mathcal F_j^2\pmod{1024},
\qquad
T=\sum_{j<b}W_j^2\mathcal F_j\mathcal G_j\pmod{1024}.
$$


Using the retained endpoint vanishing at these scalar precisions,


$$
\boxed{
N\equiv S/4\pmod{256},\qquad
H-N\equiv T/8\pmod{128}.
}
$$



The precision is sufficient because the actual raw first factor lies in $4\mathbb Z_2$, while the raw difference factor lies in $8\mathbb Z_2$. Thus changing them by $128$ and $256$, respectively, changes their product by a multiple of $1024$.

The accepted parent alignment implies


$$
T\equiv0\pmod{512}.
$$


Therefore the next discrepancy bit is exactly


$$
\boxed{
\frac{H-N}{64}\equiv\frac{T}{512}\pmod2.
}
$$


This division is made **after the complete contraction**, not termwise.

---

## 7. Exactly what weight-depth four can contribute

Let


$$
w=v_2(W_j)=4,\qquad W_j=16u_j,\quad u_j\ \text{odd},
$$


and abbreviate $f=\mathcal F_j$, $g=\mathcal G_j$.

The retained lower-precision parity argument gives


$$
fg\equiv0\pmod2
$$


at weight depth four. It does not generally give $fg\equiv0\pmod4$.

The scalar formulas become


$$
X_j^2\equiv64u_j^2f^2\equiv64f^2\pmod{256},
$$


and


$$
X_j(Y_j-X_j)\equiv32u_j^2fg\pmod{256}.
$$


Since odd squares are $1\bmod8$,


$$
\boxed{
X_j^2\equiv
\begin{cases}
64,&f\text{ odd},\\
0,&f\text{ even}
\end{cases}
\pmod{256},
}
$$


and


$$
\boxed{
X_j(Y_j-X_j)\equiv32fg\pmod{128}.
}
$$


Because $fg$ is even, the latter is either $0$ or $64\bmod128$.

Thus


$$
X_jY_j\equiv64f^2+32fg\pmod{128}.
$$



The relevant precision ledger is:

| Target at $w=4$ | Required information |
|---|---|
| $N\bmod128$ or $N\bmod256$ | $f\bmod2$ |
| $H-N\bmod128$ | $fg\bmod4$ |
| $H\bmod128$ | $f\bmod2$ and $fg\bmod4$ |
| Coordinate defect modulo $256$ | $fg\bmod8$ |

The established $w\ge5$ exclusion remains valid at its stated scope. It does **not** justify discarding $w=4$, nor restoring the old 31-class support.

---

## 8. Strongest primitive denominator consequence of hypothetical alignment

Retain


$$
\alpha=v_2(N),\qquad \gamma=v_2(H),
$$


with $N>0$ and the established original-family mixed nonvanishing. Write


$$
L_n=\frac{3n}{2}-v_2(b!)-s_2(n)-1.
$$


The exact primitive interface is


$$
v_2(q_n)=\max\{0,L_n-(\gamma-\alpha)\}.
$$



Suppose, hypothetically, that


$$
H\equiv N\pmod{128}.
$$



### If $\alpha\le6$

Then $H=N+128z$ has the same valuation as $N$, so


$$
\boxed{\gamma=\alpha,\qquad v_2(q_n)=\max\{0,L_n\}.}
$$


On the original domain $L_n>0$, hence this is $L_n$. In particular, $N\equiv64\pmod{128}$ would give $\alpha=\gamma=6$.

### If $\alpha\ge7$

The congruence gives only $\gamma\ge7$. Therefore


$$
\boxed{
0\le v_2(q_n)\le\max\{0,L_n+\alpha-7\}.
}
$$


For known $\alpha=7$, this sharpens to


$$
0\le v_2(q_n)\le L_n.
$$


There is no positive lower bound from alignment alone: $\gamma$ could be sufficiently large to remove the entire dyadic denominator contribution.

If only $\alpha\ge7$ is known, with no upper bound on $\alpha$, there is no uniform upper bound supplied by this congruence alone. These distinctions cannot be replaced by an assertion of unrestricted $\gamma-\alpha$ control.

---

## 9. Remaining arithmetic task and bounded follow-on certificate

The local contact obstruction is closed. The next task is the actual high-binomial contraction of $S,T$, retaining:

* the complete nine-entry exterior force;
* moments through $-10$;
* the certified higher coefficient terms;
* coefficient values depending on $j\bmod256$;
* all weight-depth-four coordinates;
* actual overflow factorial patterns and exact finite ranges.

That unbounded contraction remains assigned to A5 and is not reproduced here.

A useful **new bounded certificate**, not a repetition of the completed contact calculation, is:

**Inputs:** the certified $p,d,\beta$; bounded factors $\binom{644+s-1}{s}$; the definitions of $U_s,V_s$.

**Expected verifiable output:**


$$
U_s(x+256)-U_s(x)\equiv0\pmod{128},
$$




$$
V_s(x+256)-V_s(x)\equiv0\pmod{256},
$$


coefficientwise in the Newton basis, together with


$$
U_0(128)-U_0(0)=64\pmod{128},
\quad
V_{-2}(128)-V_{-2}(0)=128\pmod{256}.
$$


Degree $16$ is a safe bound for these reconstructed polynomials. There are at most $43$ coefficient polynomials and $17$ coefficients per polynomial. This is a small fixed exact-arithmetic check; it does not evaluate the high carry.

---

## 10. Final gcd, whole error, and research status

The actual primitive pair remains


$$
N_B=d_B[u,v],\qquad
A_B=N_{B,1}^{T}\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^{T}\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
$$


The primitive multiplier remains $d_B^2/g_B$. No binary congruence controls the odd-prime part of this final gcd.

At the retained scope of the whole-error theorem,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi)<0
\quad\text{eventually},
$$




$$
\log|\epsilon_n|
=
-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n),
$$


and the whole nonzero evaluated form is


$$
q_n(e+\pi)-p_n=-q_n\epsilon_n>0
\quad\text{eventually}.
$$


Nothing proved here shows that this whole form tends to zero.

**Final result:** the new finite transport and coefficient-cylinder proof pass; the next reconstruction interface is now precision-safe, with a demonstrated correction from period $128$ to period $256$. The remaining local bottleneck is the actual complete high carry. Beyond it remain unrestricted relative valuation, full primitive-denominator control, and the same-index whole-error comparison.

**An unconditional proof or disproof of irrationality of $e+\pi$ remains unresolved.**
