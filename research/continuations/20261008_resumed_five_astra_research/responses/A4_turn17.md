> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audits of the precision-local producer and the weighted complete-source period

## Executive conclusions

The rationality or irrationality of $e+\pi$ remains unresolved.

The two requested audits have different outcomes and must not be combined into a single unqualified “PASS.”

1. **Precision-local producer theorem: PASS.**  
   Subject to the explicitly reused finite modulo-$3$ block law and the already established scalar theorem, the parent’s mathematical localization argument is correct. Below I supply the Newton-coefficient valuation proof, the literal finite block inverses, the weighted Neumann-path argument, the complete next-column embedding, the top Pascal reconstruction, and the scalar precision accounting.

2. **Supplied implementation on its entire advertised input domain: FAIL, with a local repair.**  
   The program accepts
   

$$
4\le M\le33,\qquad 1\le L\le72,
$$


   but allocates certain binomial rows only through $H=6M-1$. If $L\ge6M$, the reconstruction can access an unallocated entry. For example, the accepted input
   

$$
(M,n_{\rm res},L)=(4,200,24)
$$


   reaches `nchoose[24]` although that vector has indices only $0,\ldots,23$.

   The repair is to generate the Pascal rows through
   

$$
K=\max\{6M-1,L,3M\}.
$$


   This preserves the advertised domain and does not change the matrix, window, forcing, scalar calculation, or output formulas.

   **The actual saved case $M=33,L=72$ is unaffected:** there $H=197$ and the largest required top index is $99$. Its implementation passes the static mathematical audit. No repeat of its $620$-coordinate solve is needed.

3. **Weighted complete-source period corollary: PASS as a conditional deduction.**  
   All new steps in that corollary are valid, including the complete next-column force, the dense known part of $h$, and all $99$ coordinates used by the scalar at $M=33$.

   The deduction still depends on the every-precision finite block theorem for **all finite sizes**, including $n+1$. Its separately assigned different audit is not supplied here. I therefore do not mark that dependency as independently passed.

4. **No actual $\mathcal N_{00}$ value is obtained.**  
   The saved producer jet is sufficient for a paid source replacement. It is not sufficient, by itself, to evaluate the complete $W$-return or the physical-seventh Schur contraction. The actual $W$, its highest column $Y_m$, the complete corrected columns, and the source exponents remain unfrozen.

5. **A further proved certificate lemma is given below.**  
   It identifies a concrete sufficient residual certificate for the outstanding complete $W$-return: integral approximate return vectors with residuals modulo $3^{17}$, together with a complete aggregate contraction modulo $3^{32}$. This is a proved precision reduction, not an evaluation of the required contraction.

No code was executed in preparing this report. Existing arithmetic receipts are reused at their stated finite scope.

---

# 1. Original domain and exact objects

## 1.1 The original index family

The research family remains


$$
j>0,\qquad j\equiv84645\pmod{531441},
\qquad 531441=3^{12},
$$


with


$$
m=2^{2j-1},\qquad n=4^j+1=2m+1,\qquad A=n-2=4^j-1.
$$



The other original parameters remain


$$
H_{\rm phys}=3^{h-1},\qquad D=H_{\rm phys}-A,
$$




$$
\frac1{2C_{16}}<\frac{D}{H_{\rm phys}}<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15},
$$


and


$$
\frac{103}{1000}<\frac{N_0}{P_0}<\frac{104}{1000}.
$$



They satisfy


$$
P_0=243P=3^{h-27},\qquad N_0=243r,\qquad D=P_0+N_0,
$$




$$
P=3^{h-32},\qquad r\equiv2\pmod9,\qquad r\ \text{odd},
$$




$$
4^j=243(3^{26}-1)P-243r+1.
$$



To distinguish the real residual parameter from the producer scalar, I write


$$
\chi_{\rm range}=P-R,
$$


where


$$
x=y-1,\qquad Q=27P,\qquad b=Q-N_0=2R,\qquad c=2\chi_{\rm range}.
$$


Thus


$$
N_0=25P+c,\qquad D=268P+c,\qquad D+b=270P.
$$



The density-paid Range III subwindow is


$$
\boxed{\frac3{25}<\frac{\chi_{\rm range}}P<\frac{31}{250}.}
$$


It is not a condition on the producer scalar defined below.

No auxiliary matrix-size example in this report is substituted for an original index in a global irrationality argument.

## 1.2 Producer definitions and established reuse

Set


$$
N=n-1,\qquad F_{\rm fac}=N!,
$$


and retain the exact recurrence


$$
\gamma_0=1,\qquad \gamma_1=0,\qquad
\gamma_{r+1}=(4r+2)\gamma_r+4\gamma_{r-1}\quad(r\ge1).
$$



The finite matrices and vectors are


$$
T_n[a,b]=\binom{a+b}{a}\gamma_{a+b},
\qquad 0\le a,b<n,
$$




$$
P_n[a,b]=\binom ab,\qquad
\widehat T_n=P_n^{-1}T_nP_n^{-T},
$$




$$
u_a=\frac{F_{\rm fac}(-2)^a}{a!},\qquad
v=T_n^{-1}u,
$$




$$
k_a=\binom{n+a}{a}\gamma_{n+a},\qquad
h_{\rm vec}=T_n^{-1}k.
$$



The complete force is, by the established notation bridge,


$$
t=3n h_{\rm vec}
 +(b_c+6)e_{n-1}
 +\frac{2b_c}{n-1}e_{n-2},
\qquad b_c=-n-66.
$$


Both affine terminal terms are retained.

Define


$$
\Xi=F_{\rm fac}^2-u^Tv,
\qquad
\chi_{\rm prod}=u^Tt,
\qquad
\xi=\frac{\chi_{\rm prod}}{\Xi}.
$$



The reused scalar theorem applies to every


$$
n\ge5,\qquad n\equiv2\pmod3,
$$


and gives


$$
\boxed{\Xi\equiv\chi_{\rm prod}\equiv3\pmod9,}
$$


hence


$$
v_3(\Xi)=v_3(\chi_{\rm prod})=1,
\qquad \xi\in1+3\mathbb Z_3.
$$



The original family satisfies these hypotheses. This scalar theorem, its old audit, and its old arithmetic receipt are not reopened here.

The complete correction coefficients are exactly


$$
\boxed{
q_a=-\frac{F_{\rm fac}}{a!}
\left(
3n(h_{\rm vec})_a
 +(b_c+6)\delta_{a,n-1}
 +\frac{2b_c}{n-1}\delta_{a,n-2}
 +\xi v_a
\right).
}
\tag{1.1}
$$


The denominator $n-1$ is an actual ternary unit. It is not replaced by $1$, and neither affine term is omitted.

---

# 2. Audit of the precision-local mathematical theorem

## 2.1 Formal generating function and the Newton valuation

Let


$$
F(t)=\sum_{r\ge0}\gamma_r\frac{t^r}{r!}.
$$


The recurrence is equivalent to


$$
(1-4t)F''=6F'+4F,
\qquad F(0)=1,\quad F'(0)=0.
$$



Put $s=\sqrt{1-4t}$. For


$$
F(t)=\frac{e^{s-1}}s,
$$


formal differentiation gives


$$
F'=-\frac{2e^{s-1}(s-1)}{s^3},
$$




$$
F''=\frac{4e^{s-1}(s^2-3s+3)}{s^5}.
$$


Consequently


$$
s^2F''=6F'+4F,
$$


and the initial conditions hold. Since the differential equation recursively determines every coefficient, this proves


$$
\boxed{
F(t)=(1-4t)^{-1/2}\exp(\sqrt{1-4t}-1).
}
\tag{2.1}
$$



Here “formal rational solution” in the source must mean a formal solution **with rational coefficients**, not a rational function of $t$.

Let


$$
g_h=\Delta^h\gamma_0.
$$


The exponential generating function of the binomial difference transform is


$$
\sum_{h\ge0}g_h\frac{t^h}{h!}=e^{-t}F(t).
$$


The Catalan expansion gives


$$
\sqrt{1-4t}=1-2t+t^2R(t),
\qquad R(t)\in\mathbb Z[[t]],
$$


so


$$
\sum_{h\ge0}g_h\frac{t^h}{h!}
=(1-4t)^{-1/2}e^{-3t}\exp(t^2R(t)).
\tag{2.2}
$$



Each coefficient of $(1-4t)^{-1/2}$ is integral. Also


$$
v_3\!\left(\frac{3^a}{a!}\right)=a-v_3(a!)\ge0,
$$


so $e^{-3t}\in\mathbb Z_3[[t]]$.

In degree $h$, a term from $\exp(t^2R(t))$ has denominator $a!$ with


$$
a\le\lfloor h/2\rfloor.
$$


Therefore


$$
v_3(g_h)\ge
v_3(h!)-v_3(\lfloor h/2\rfloor!).
$$


The interval


$$
\lfloor h/2\rfloor+1,\ldots,h
$$


contains at least $\lfloor h/6\rfloor$ multiples of $3$. Thus


$$
\boxed{
v_3(g_h)\ge
v_3(h!)-v_3(\lfloor h/2\rfloor!)
\ge\lfloor h/6\rfloor.
}
\tag{2.3}
$$



This is an all-degree proof. The finite list of checked Newton valuations is corroboration only.

The optional integer recurrence in the source is also consistent. Indeed, coefficient comparison in


$$
4z^2(1+z)^2G'
=(1-9z^2-4z^3)G+z-1
$$


gives


$$
g_h=4(h-1)g_{h-1}+(8h-7)g_{h-2}+4(h-2)g_{h-3},
$$


with $g_0=1,g_1=-1,g_2=5$.

## 2.2 Literal finite Pascal transformation

Let


$$
\Gamma(z)=\sum_{r\ge0}\gamma_rz^r,
\qquad G(z)=\sum_{h\ge0}g_hz^h.
$$


The raw bivariate generating function is


$$
\sum_{a,b\ge0}T[a,b]x^ay^b=\Gamma(x+y).
$$



Applying inverse Pascal transforms in both variables gives


$$
\frac1{(1+x)(1+y)}
\Gamma\!\left(\frac{x}{1+x}+\frac{y}{1+y}\right).
$$


Using


$$
\Gamma(z)=\frac1{1-z}G\!\left(\frac z{1-z}\right)
$$


yields


$$
\boxed{
\sum_{a,b\ge0}\widehat T[a,b]x^ay^b
=
\sum_{h\ge0}g_h
\frac{(x+y+2xy)^h}{(1-xy)^{h+1}}.
}
\tag{2.4}
$$



This formal calculation does not introduce an infinite inverse. For $a,b<n$, the transformed entry uses only raw row indices at most $a$ and raw column indices at most $b$. It is therefore exactly the entry of the literal finite matrix


$$
P_n^{-1}T_nP_n^{-T}.
$$



Expanding the numerator, put


$$
p+q+c=h,\qquad p-q=a-b.
$$


If the denominator contributes $(xy)^t$, then


$$
a=p+c+t,\qquad h+t=a+q.
$$


Hence


$$
\boxed{
\widehat T[a,b]
=
\sum_{h\ge0}g_h
\sum_{\substack{p,q,c\ge0\\p+q+c=h\\p-q=a-b}}
\frac{h!}{p!q!c!}\,2^c\binom{a+q}{h}.
}
\tag{2.5}
$$



The convention $\binom{a+q}{h}=0$ for $a+q<h$ enforces $t\ge0$. Every multinomial coefficient is an integer.

Every contribution has $h\ge|a-b|$. Equation (2.3) therefore proves


$$
\boxed{
v_3(\widehat T[a,b])\ge\lfloor |a-b|/6\rfloor.
}
\tag{2.6}
$$


In particular, modulo $3^M$, the matrix has half-bandwidth at most


$$
H_M=6M-1.
$$



## 2.3 All finite block types and their actual inverses

The established modulo-$3$ block law uses


$$
B_3=
\begin{pmatrix}
1&2&2\\
2&0&0\\
2&0&2
\end{pmatrix},
\quad
B_2=
\begin{pmatrix}
1&2\\
2&0
\end{pmatrix},
\quad B_1=(1).
$$



Their literal inverses over $\mathbb Z_3$ are


$$
\boxed{
B_3^{-1}=
\begin{pmatrix}
0&1/2&0\\
1/2&1/4&-1/2\\
0&-1/2&1/2
\end{pmatrix},
}
\tag{2.7}
$$




$$
\boxed{
B_2^{-1}=
\begin{pmatrix}
0&1/2\\
1/2&-1/4
\end{pmatrix},
\qquad B_1^{-1}=(1).
}
\tag{2.8}
$$



For example, solving $B_3x=(u,v,w)^T$ gives


$$
x_0=v/2,\qquad
x_2=(w-v)/2,\qquad
x_1=u/2+v/4-w/2.
$$


Thus every displayed denominator is a ternary unit. The determinants are


$$
\det B_3=-8,\qquad \det B_2=-4,\qquad \det B_1=1.
$$



Modulo $3$, the corresponding digit solves are


$$
x_0=2v,\qquad x_1=2u+v+w,\qquad x_2=v+2w,
$$


and


$$
x_0=2u_1,\qquad x_1=2u_0+2u_1
$$


for a final block of size two. These are exactly the formulas now present in the supplied program.

The actual original size satisfies $n\equiv2\pmod3$, so its last block is $B_2$, not an artificially completed $B_3$.

## 2.4 Weighted Neumann paths and maximum excursion

Let $B$ be the literal block-diagonal lift with the actual final block, and write


$$
\widehat T_n=B+E.
$$


Then


$$
E\in3\operatorname{Mat}_n(\mathbb Z_3),
$$


and


$$
v_3(E[a,b])\ge
\max\{1,\lfloor |a-b|/6\rfloor\}.
$$



If an $E$-entry has finite valuation $\nu\ge1$, its jump satisfies


$$
|a-b|\le6\nu+5.
$$


A multiplication by $B^{-1}$ adds a jump of at most $2$.

At precision $3^M$,


$$
\widehat T_n^{-1}
\equiv
\sum_{r=0}^{M-1}(-B^{-1}E)^rB^{-1}
\pmod{3^M}.
\tag{2.9}
$$


This is a finite identity modulo $3^M$, because $B^{-1}E$ is divisible by $3$.

Consider a fully expanded product path with $r$ correction entries of valuations


$$
\nu_1,\ldots,\nu_r,\qquad W=\nu_1+\cdots+\nu_r<M.
$$


Its total absolute path length is at most


$$
\sum_{\ell=1}^r(6\nu_\ell+5)+2(r+1)
=6W+7r+2
\le13W+2.
$$


Therefore every surviving path has total absolute length at most


$$
\boxed{w_M=13(M-1)+2.}
\tag{2.10}
$$



This controls every intermediate excursion, not merely the net displacement between the two endpoints. That distinction is essential for a finite-window argument.

## 2.5 The true end window

For requested top length $L$, put


$$
S_M=\max\{L,6M\}.
$$


Choose


$$
R_{\rm loc}\ge S_M+13(M-1)+4=S_M+w_M+2,
$$


and increase it by at most two so that


$$
R_{\rm loc}\equiv n\pmod3.
$$


Then


$$
\ell_{\rm loc}=n-R_{\rm loc}
$$


is a true modulo-$3$ block boundary.

Every relevant observed coordinate lies among the last $S_M$ coordinates. Its distance from the left edge is at least $w_M+2$. A surviving Neumann path therefore cannot leave the window. The right edge remains the actual coordinate $n-1$.

Because the window contains complete leading $3$-blocks and the actual final short block, its modulo-$3$ inverse is the restriction of the same block inverse. Its solve agrees with the original finite solve on every required top coordinate.

For small $n$, the mathematical construction may use the whole finite matrix instead. The supplied residue-only program is intended for sufficiently large $n$; it is not a small-$n$ fallback implementation.

For the original application,


$$
M=33,\qquad L=72,
$$


so


$$
H_M=197,\qquad w_M=418,
$$


and the unrounded length is


$$
198+416+4=618.
$$


Alignment to $n\equiv2\pmod3$ gives


$$
\boxed{R_{\rm loc}=620.}
$$


The parent’s stated upper bound $622$ is conservative and valid.

---

# 3. Complete forces, raw reconstruction, and scalar precision

## 3.1 Complete raw $u$-force

For an offset $r\ge1$, define


$$
A_r(n)=\prod_{j=1}^{r-1}(n-j).
$$


Then the exact raw force is


$$
\boxed{u_{n-r}=A_r(n)(-2)^{n-r}.}
\tag{3.1}
$$



If $r-1\ge3M$, the product contains at least $M$ multiples of $3$. Hence $u$ is supported modulo $3^M$ within its last $3M$ coordinates.

Since $P_n^{-1}$ is lower triangular and integral,


$$
\widehat u=P_n^{-1}u
$$


has the same end-support bound. Explicitly,


$$
\widehat u_b
=
\sum_{a\le b}(-1)^{b-a}\binom ba u_a.
\tag{3.2}
$$



The complete power $(-2)^{n-r}$ is retained. It is not replaced by its first ternary digit.

## 3.2 The actual next column through $T_{n+1}$

Write


$$
P_{n+1}=
\begin{pmatrix}
P_n&0\\
r^T&1
\end{pmatrix},
\qquad r_b=\binom nb.
$$


Let $\widehat k$ be the first $n$ entries of column $n$ of the actual matrix $\widehat T_{n+1}$.

The upper-right block of


$$
T_{n+1}=P_{n+1}\widehat T_{n+1}P_{n+1}^T
$$


gives the exact finite identity


$$
P_n^{-1}k=\widehat T_n r+\widehat k.
$$


Consequently


$$
\boxed{
h_{\rm vec}
=P_n^{-T}r+P_n^{-T}\widehat T_n^{-1}\widehat k.
}
\tag{3.3}
$$



No new unknown coordinate is introduced into the $n$-dimensional producer solve. The matrix $T_{n+1}$ is used only to identify its genuine next-column forcing.

For $a<n$,


$$
\begin{aligned}
(P_n^{-T}r)_a
&=\sum_{b=a}^{n-1}(-1)^{b-a}\binom ba\binom nb\\
&=\binom na
\sum_{s=0}^{n-a-1}(-1)^s\binom{n-a}s\\
&=(-1)^{n-a-1}\binom na.
\end{aligned}
$$


Thus


$$
\boxed{
(h_{\rm known})_{n-r}=(-1)^{r-1}\binom nr.
}
\tag{3.4}
$$



Equation (2.6), now applied to column $n$ of $\widehat T_{n+1}$, proves that $\widehat k$ is supported modulo $3^M$ in the last $6M-1$ coordinates.

The dense known term (3.4) is not discarded.

## 3.3 Returning to raw coordinates

Set


$$
z_u=\widehat T_n^{-1}\widehat u,
\qquad
z_k=\widehat T_n^{-1}\widehat k.
$$


The second of these is the locally solved part of $h_{\rm vec}$; it is not the whole vector $P_n^Th_{\rm vec}$.

For $a=n-r$,


$$
\boxed{
v_{n-r}
=
\sum_{s=0}^{r-1}
(-1)^s\binom{n-r+s}{s}(z_u)_{n-r+s},
}
\tag{3.5}
$$


and


$$
\boxed{
(h_{\rm vec})_{n-r}
=
(-1)^{r-1}\binom nr
+
\sum_{s=0}^{r-1}
(-1)^s\binom{n-r+s}{s}(z_k)_{n-r+s}.
}
\tag{3.6}
$$



Only coordinates at or above the requested raw coordinate occur. Therefore computing the top


$$
\max\{L,3M\}
$$


raw coordinates is sufficient both for the $L$ coefficients and for the scalar.

## 3.4 Complete scalar and both affine constants

The finite change of basis gives


$$
\Xi
=F_{\rm fac}^2-\widehat u^Tz_u.
\tag{3.7}
$$



The two affine terms cancel in the scalar only after both are included:


$$
\begin{aligned}
u^Tt
={}&3n\,u^Th_{\rm vec}
 +(b_c+6)(-2)^{n-1}
 +\frac{2b_c}{n-1}(n-1)(-2)^{n-2}\\
={}&3n\,u^Th_{\rm vec}+6u_{n-1}.
\end{aligned}
$$


Hence


$$
\boxed{
\chi_{\rm prod}=3n\,u^Th_{\rm vec}+6u_{n-1}.
}
\tag{3.8}
$$



This scalar cancellation does **not** justify omitting either affine term from the individual coefficients (1.1).

For $n\ge R_{\rm loc}$, the original factorial is sufficiently deep that


$$
F_{\rm fac}^2\equiv0\pmod{3^M}.
$$


For example $R_{\rm loc}\ge6M$, so


$$
v_3((n-1)!)\ge\left\lfloor\frac{n-1}{3}\right\rfloor
\ge2M-1.
$$


The factorial term is thus omitted only in this paid modular calculation, not from the exact definition of $\Xi$.

To obtain $\xi\bmod3^{M-1}$, compute both scalars modulo $3^M$. The reused depth-one law permits


$$
\frac{\Xi}{3},\quad\frac{\chi_{\rm prod}}3
\pmod{3^{M-1}},
$$


after which $\Xi/3$ is inverted as a unit. Therefore


$$
\boxed{
\xi=
\frac{\chi_{\rm prod}/3}{\Xi/3}
\pmod{3^{M-1}}.
}
\tag{3.9}
$$



One digit is genuinely spent. Nothing in this audit promotes the output to precision $3^M$.

## 3.5 Conservative residue input for the local algorithm

For $1\le s<3^E$,


$$
v_3\binom{3^E}{s}=E-v_3(s).
$$


Vandermonde therefore gives


$$
\binom{a+3^E}{s}\equiv\binom as
\pmod{3^{E-\lfloor\log_3s\rfloor}}.
\tag{3.10}
$$



Every lower binomial index used in the matrix entries, raw reconstruction, transformed force, and dense known part is bounded by the admitted local lengths. Thus


$$
E=M+\lfloor\log_3R_{\rm loc}\rfloor+1
$$


is a safe common exponent.

The remaining input dependence is also paid:

- $A_r(n)$ is an integer polynomial in $n$;
- the last block type depends on $n\bmod3$;
- $(-2)^a=(1-3)^a$ has period dividing $3^{M-1}$ modulo $3^M$;
- $n-1$ remains a ternary unit;
- both affine constants are evaluated from the same $n$-residue.

At $M=33,L=72$, this gives the conservative input modulus


$$
\boxed{3^{39}.}
$$


This establishes the first local theorem independently of the stronger period corollary.

---

# 4. Static audit of the supplied implementation

## 4.1 Index correspondence

The program uses the following exact correspondence.

| Program object | Original object |
|---|---|
| local row `i` | $a=n-R_{\rm loc}+i$ |
| `entry(i,i-j)` | $\widehat T_n[a,b]$, $b=n-R_{\rm loc}+j$ |
| `entry(i,i-R)` | $\widehat T_{n+1}[a,n]$ |
| `i=R-r` | original coordinate $n-r$ |
| `ratios[R-r]` | $A_r(n)\bmod3^M$ |
| `u[R-r]` | $A_r(n)(-2)^{n-r}\bmod3^M$ |
| `vh` | $z_u$ in the local window |
| `hh` | $z_k$ in the local window |
| `q[L-r]` | $q_{n-r}\bmod3^{M-1}$ |

In particular, the next-column call uses column $n$, not column $n+1$, and the unknown-vector boundary remains $n-1$.

## 4.2 Diagonal Newton interpolation is proved, not empirical

At precision $3^M$, let $H=6M-1$. For a fixed displacement $d=a-b$, formula (2.5), truncated at $h\le H$, is an integer-valued polynomial in $a$ of degree at most $H$.

When $d>0$ and $0\le a<d$, every contributing term has $p\ge d>a$, so


$$
a+q<h=p+q+c.
$$


It is therefore zero. The program’s zero values at samples with $b=a-d<0$ are the correct polynomial values, not an invented extension.

The samples $a=0,\ldots,H$ determine the degree-$H$ Newton polynomial. For $-H\le d\le H$, the required sample columns satisfy $b\le2H$, so all raw moments needed for these literal small transforms have index at most $3H$.

At $M=33$, this is exactly


$$
H=197,\qquad 3H=591.
$$


The program’s moment endpoint $591$ is therefore correct. It is distinct from the alternative direct-$g_h$ generator, which would need only $g_0,\ldots,g_{197}$.

Forward differences of the finite samples produce the correct Newton coefficients modulo $3^M$. Evaluation at the true row residue is justified by (3.10). No inverse is being extrapolated from a finite numerical pattern.

## 4.3 Digit solve and paid digit division

Suppose the current approximation satisfies


$$
Ax\equiv f\pmod{3^r}.
$$


The program forms


$$
\frac{f-Ax}{3^r}\pmod3.
$$


Its divisibility test explicitly verifies the division by $3^r$.

Solving with the modulo-$3$ block inverse gives $d$ such that


$$
Ad\equiv\frac{f-Ax}{3^r}\pmod3.
$$


Then


$$
x\leftarrow x+3^rd
$$


solves the system modulo $3^{r+1}$.

The three block formulas are exactly those derived in §2.3. The final full local residual check verifies the computed local equation modulo $3^M$. The mathematical locality theorem, rather than that residual check alone, identifies the required top entries with the original finite solve.

## 4.4 Scalar, force, and monic quotient

The implementation correctly:

- forms the complete force $A_r(n)(-2)^{n-r}$;
- retains the dense known term $(-1)^{r-1}\binom nr$;
- reconstructs all $\max\{L,3M\}$ top raw entries;
- computes $-\widehat u^Tz_u$ only after the factorial-square valuation has been paid;
- includes $6u_{n-1}$ in $\chi_{\rm prod}$;
- divides both depth-one scalars by $3$;
- inverts $\Xi/3$ only modulo $3^{M-1}$;
- retains $b_c+6$ and $2b_c/(n-1)$ in the top coefficients.

For


$$
P_{L-1}(x)=\sum_{a=0}^{L-1}q_{n-L+a}x^a,
$$


the program’s quotient coefficients are


$$
[V]_{b}
=
\sum_{a=b+1}^{L-1}(-2)^{a-b-1}q_{n-L+a}.
$$


Thus


$$
P_{L-1}(x)=(x+2)V(x)+P_{L-1}(-2).
$$


This is monic division, with no loss of ternary precision. The remainder is printed rather than silently discarded.

## 4.5 Arithmetic-width audit

On the stated numerical domain,


$$
3^{33}<2^{53},\qquad 3^{39}<2^{62}.
$$


Consequently:

- `nr+period` is below $2^{63}$;
- additions of two residues modulo $3^M$ fit in 64 bits;
- every unreduced dot product has fewer than $2^{10}$ terms, each below $2^{106}$;
- those sums are below $2^{116}$, well within unsigned 128-bit arithmetic.

In `binomial_row`, the test $s>a$ prevents a zero numerator from entering the loop that removes factors of $3$. The accumulated depth is the actual valuation of the integer binomial coefficient; stripped denominators are units. The hard-coded zero threshold $33$ is valid because $M\le33$, although expressing it through the requested precision would be clearer.

This audit assumes the intended compiler support for the displayed signed and unsigned 128-bit integer types.

## 4.6 The implementation defect

The program creates
```cpp
V nchoose=binomial_row(nr,H);
```
but later reads
```cpp
nchoose[r]
```
for $r\le\max\{L,3M\}$.

For the accepted input


$$
M=4,\quad L=24,\quad n_{\rm res}=200,
$$


one has


$$
H=23,\qquad \max\{L,3M\}=24.
$$


The access at $r=24$ is out of bounds.

For still larger $L$, the same problem also affects the Pascal reconstruction rows `endchoose`, because their required lower index can exceed $H$.

The fact that some of these output coordinates are subsequently multiplied by a factorial quotient that vanishes modulo $3^M$ does not cure an out-of-bounds memory access.

### Repair preserving the advertised domain

Move the top-length definition before allocation and use


$$
K=\max\{H,\max(L,3M)\}.
$$


Generate
```cpp
endchoose[i] = binomial_row(actual_row_residue, K);
nchoose      = binomial_row(nr, K);
```
while retaining the matrix-entry interpolation loops through $H$.

No further matrix moments are needed: only the auxiliary Pascal rows become longer. The conservative input exponent already pays these indices because $K<R_{\rm loc}$.

For offsets $r>3M$, the unfilled `ratios` entries being zero are correct modulo $3^M$: the actual factorial quotient has length at least $3M$.

At $M=33,L=72$,


$$
K=H=197.
$$


The repair changes nothing whatsoever in that calculation.

### First-audit verdict



$$
\boxed{\text{Mathematical precision-local theorem: PASS.}}
$$




$$
\boxed{\text{Program on its whole advertised domain: FAIL until the allocation repair.}}
$$




$$
\boxed{\text{Program at }M=33,L=72\text{, and throughout }L\le3M\text{: PASS in this static audit.}}
$$



---

# 5. Audit of the weighted complete-source period corollary

## 5.1 Exact remaining dependency

The additional hypothesis is the every-precision finite block law:

> For every finite size $s$, every $M\ge1$, and $q_M=3^M$, the literal matrix $\widehat T_s$ modulo $3^M$ is block diagonal in blocks of length $q_M$, with repeated full blocks $\widehat T_{q_M}$ and the actual final leading incomplete block.

The supplied A4 theorem states this for all finite sizes, not only original $n\equiv2\pmod3$. That scope is necessary: the corollary also applies it to $s=n+1$.

Its separately assigned different audit remains an explicit dependency of this report.

## 5.2 Precise conditional result

Assume that block law and the precision-local theorem proved above. Let


$$
M\ge4,\qquad 1\le L\le3M,
$$


and let $n,n'$ be sufficiently large, with


$$
n\equiv n'\equiv2\pmod3,\qquad n'\equiv n\pmod{3^M}.
$$



Then


$$
\boxed{\Xi(n')\equiv\Xi(n),\quad
\chi_{\rm prod}(n')\equiv\chi_{\rm prod}(n)\pmod{3^M},}
\tag{5.1}
$$




$$
\boxed{\xi(n')\equiv\xi(n)\pmod{3^{M-1}},}
\tag{5.2}
$$


and, for $1\le r\le L$,


$$
\boxed{q_{n'-r}(n')\equiv q_{n-r}(n)\pmod{3^{M-1}}.}
\tag{5.3}
$$



The proof also gives, for every $1\le r\le3M$,


$$
\boxed{
A_r(n')v_{n'-r}(n')\equiv A_r(n)v_{n-r}(n)\pmod{3^M},
}
\tag{5.4}
$$


and the analogous statement for $A_rh_{\rm vec}$.

This asserts a period, not that $3^M$ is the least possible period.

## 5.3 All matrix positions, including crossings and the next column

First compare $n$ and $n+q_M$. At fixed offsets $i,j$ from the right edge,


$$
a=n-i,\qquad b=n-j
$$


become


$$
a+q_M,\qquad b+q_M.
$$



Their within-block residues are unchanged, and their block numbers both increase by one.

- If $a,b$ are in the same $q_M$-block, the corresponding entries are equal modulo $3^M$.
- If they lie in different blocks, both entries are zero modulo $3^M$.
- If one lies in the actual incomplete final block, its within-block coordinates remain the same, and the leading incomplete block has the same size because $n\bmod q_M$ is unchanged.

Thus the entire corresponding local matrix is unchanged modulo $3^M$.

For the force $\widehat k$, use the **same theorem at size $n+1$**:


$$
\widehat k_{n-i}=\widehat T_{n+1}[n-i,n].
$$


Under $n\mapsto n+q_M$, both indices again shift by $q_M$. This covers the real next column, including a crossing between two $q_M$-blocks and a final full block when $n+1$ is divisible by $q_M$.

Because $q_M$ is divisible by $3$,

- $R_{\rm loc}$ is unchanged;
- the actual left edge shifts by $q_M$;
- left alignment remains a genuine modulo-$3$ block boundary;
- the final short modulo-$3$ block is unchanged.

The local matrices are units over $\mathbb Z_3$. If $A'\equiv A\pmod{3^M}$, then


$$
A'^{-1}-A^{-1}=A'^{-1}(A-A')A^{-1}\in3^M\operatorname{Mat}(\mathbb Z_3).
$$


Thus their local inverses are also unchanged.

No finite matrix is replaced by a matrix whose dimension is merely its residue.

## 5.4 The factorial weight pays every continuity loss

For $n\equiv2\pmod3$, the factors $n-j$ divisible by $3$ in


$$
A_r(n)=\prod_{j=1}^{r-1}(n-j)
$$


are precisely those with


$$
j=2,5,8,\ldots,r-1.
$$


There are exactly $\lfloor r/3\rfloor$ of them. Hence


$$
v_3(A_r(n))\ge\lfloor r/3\rfloor.
$$



For $r=1,2$, $\lfloor\log_3r\rfloor=0$. For $r\ge3$, choose $s\ge1$ with


$$
3^s\le r<3^{s+1}.
$$


Then


$$
\lfloor r/3\rfloor\ge3^{s-1}\ge s.
$$


Therefore


$$
\boxed{
v_3(A_r(n))\ge\lfloor r/3\rfloor
\ge\lfloor\log_3r\rfloor.
}
\tag{5.5}
$$



Also, $A_r(n)$ is an integer polynomial. It therefore has period $3^M$ modulo $3^M$.

For $1\le s<3^M$, Vandermonde gives


$$
\binom{a+3^M}{s}-\binom as
=
\sum_{j=1}^s\binom{3^M}{j}\binom a{s-j},
$$


so


$$
\boxed{
\binom{a+3^M}{s}-\binom as
\in3^{M-\lfloor\log_3s\rfloor}\mathbb Z.
}
\tag{5.6}
$$


For $s=0$, the difference is exactly zero.

### Transformed $u$-force

A term contributing from input coordinate $n-r$ to output coordinate $n-r+s$ in $P_n^{-1}u$ is


$$
(-1)^s\binom{n-r+s}{s}
A_r(n)(-2)^{n-r},
\qquad 0\le s\le r-1.
$$


The power has period dividing $3^{M-1}$, and $A_r$ itself is periodic modulo $3^M$. The possible binomial loss is at most $\lfloor\log_3s\rfloor$, which is paid by (5.5).

Notice that the weight here is the weight $A_r$ of the **input force coordinate**, not the weight of the transformed output coordinate.

Thus the complete $\widehat u$ is periodic modulo $3^M$. The local solutions $z_u,z_k$ are consequently periodic on the corresponding window.

### Weighted raw reconstruction

For the raw coordinate $n-r$, equations (3.5)–(3.6) use


$$
\binom{n-r+s}{s},\qquad 0\le s\le r-1.
$$


Multiplying the entire raw coordinate by $A_r(n)$ pays every such binomial continuity loss. Hence


$$
A_r(n)v_{n-r}
$$


and


$$
A_r(n)\bigl((h_{\rm vec})_{n-r}-(h_{\rm known})_{n-r}\bigr)
$$


are periodic modulo $3^M$.

The dense known part is


$$
(h_{\rm known})_{n-r}=(-1)^{r-1}\binom nr.
$$


Its possible loss is $\lfloor\log_3r\rfloor$, again paid by (5.5). Thus the complete


$$
A_r(n)(h_{\rm vec})_{n-r}
$$


is periodic modulo $3^M$.

All these lower indices satisfy


$$
r\le3M<3^M.
$$



At no point is $A_r$ cancelled out of a congruence. Such cancellation would generally be invalid. The argument proves weighted raw periodicity, not periodicity of unweighted $v$, unweighted $h_{\rm vec}$, or the full Pascal matrix.

## 5.5 Scalars and complete top coefficients

The contraction


$$
\widehat u^Tz_u
$$


uses only the last $3M$ entries of $\widehat u$. Both factors there are periodic. The factorial square is zero at the admitted precision, so $\Xi$ is periodic modulo $3^M$.

For the numerator,


$$
u_{n-r}(h_{\rm vec})_{n-r}
=(-2)^{n-r}
\bigl(A_r(n)(h_{\rm vec})_{n-r}\bigr)
$$


is periodic modulo $3^M$. Therefore the complete expression


$$
\chi_{\rm prod}
=
3n\sum_{r=1}^{3M}u_{n-r}(h_{\rm vec})_{n-r}
+6u_{n-1}
$$


is periodic modulo $3^M$.

The depth-one scalar law then gives $\xi$ only modulo $3^{M-1}$, exactly as in (3.9).

Finally,


$$
q_{n-r}
=-A_r(n)\left[
3n(h_{\rm vec})_{n-r}
 +(b_c+6)\mathbf1_{r=1}
 +\frac{2b_c}{n-1}\mathbf1_{r=2}
 +\xi v_{n-r}
\right].
$$


Every factor other than $\xi$ is unchanged at sufficient precision. Since $n-1$ is a unit,


$$
(n'-1)^{-1}-(n-1)^{-1}
=
-\frac{n'-n}{(n'-1)(n-1)}
\in3^M\mathbb Z_3.
$$


Both affine terms therefore remain periodic as complete terms. The $\xi$-term is periodic at the required target precision $3^{M-1}$.

This proves (5.1)–(5.4).

### Endpoint scope

The quotient and remainder of $P_{L-1}$ on division by $x+2$ are both periodic whenever its coefficients are periodic.

However, arbitrary $L\le3M$ does **not** imply that the remainder is zero modulo $3^{M-1}$. Dropping the remainder requires a separate tail-and-endpoint payment. That payment is available for the actual original $72$-coefficient reduction in §7 below.

### Second-audit verdict



$$
\boxed{
\text{Weighted complete-source period deduction: PASS, conditional on the full finite block law.}
}
$$



The first mathematical dependency has now passed this audit. The separately assigned audit of the second dependency remains outstanding.

---

# 6. The $M=33,L=72$ original family and the saved arithmetic

## 6.1 Actual input period

At $M=33,L=72$, the conditional corollary gives


$$
\boxed{\text{input period }3^{33},\qquad\text{output precision }3^{32}.}
$$



The supplied residues are


$$
3^{33}=5\,559\,060\,566\,555\,523,
$$




$$
n_{\rm old}=2\,323\,594\,735\,168\,358\,765,
$$




$$
n_{\rm new}=5\,466\,478\,914\,705\,674.
$$


They satisfy the directly checkable identity


$$
n_{\rm old}=417\cdot3^{33}+n_{\rm new}.
$$


Thus the two supplied input representatives do differ by a multiple of the claimed period.

The compatibility receipt reports:

- $4950$ weighted Pascal identities;
- $99$ weighted dense-known-$h$ identities;
- $99$ complete raw-force identities;
- $1964$ failures of the corresponding unweighted Pascal identities.

The count


$$
4950=\sum_{r=1}^{99}r
$$


matches all pairs $0\le s\le r-1$ needed for the top $99=3M$ coordinates. It is not merely a check of the $72$ output coordinates.

These are finite corroborations. They neither prove the block law nor replace the proof in §5.

## 6.2 Frozen original progression

Since


$$
84645=3^4\cdot1045,\qquad 3\nmid1045,
$$


every original $j$ has $v_3(j)=4$. In particular


$$
v_3(4^j-1)=1+v_3(j)=5.
\tag{6.1}
$$



For


$$
\boxed{j=84645+3^{32}t,\qquad t\ge0,}
\tag{6.2}
$$


LTE gives


$$
4^{j}-4^{84645}\equiv0\pmod{3^{33}}.
$$


Thus $n=4^j+1$ is fixed modulo $3^{33}$.

This progression lies inside the original congruence class modulo $3^{12}$. Conditional on the remaining block-law dependency, its entire complete $72$-coefficient jet modulo $3^{32}$ is the same as the saved $j=84645$ jet.

As arithmetic progressions in $j$, its density is $729$ times that of the step-$3^{38}$ progression, and $81$ times that of the step-$3^{36}$ progression. This arithmetic comparison does not replace the separate real-window argument.

## 6.3 The real Range III condition is still separately imposed

The number


$$
3^{32}\log_3 4
$$


is irrational: otherwise a positive power of $4$ would equal a power of $3$, contrary to unique prime factorization.

Therefore the established irrational-rotation argument continues to give infinitely many visits along (6.2) to the same strict Range III subwindow. The vanishing perturbation between $\log_3(4^j)$ and $\log_3(4^j-1)$ does not remove infinitely many visits to a fixed smaller open subinterval.

The original parameters remain actual parameters. For example,


$$
\frac{N_0}{P_0}
=\frac{25+2\chi_{\rm range}/P}{243},
\qquad
\frac{D}{H_{\rm phys}}
=\frac{268+2\chi_{\rm range}/P}{3^{31}}.
$$


The stated Range III interval lies within the retained real inequalities.

The base index $j=84645$ is **not** asserted to satisfy that real interval. It is a valid producer reference index; real residual admission is a separate condition.

Neither $A$, $m$, $h$, $D$, $P$, the monomial exponents, $W$, $Y_m$, nor the physical Schur matrix is frozen by coefficient periodicity.

## 6.4 Status of the saved jet

The existing receipt reports


$$
\Xi\bmod3^{33}=2\,351\,121\,613\,771\,125,
$$




$$
\chi_{\rm prod}\bmod3^{33}=1\,698\,009\,081\,480\,966,
$$




$$
\xi\bmod3^{32}=1\,046\,879\,413\,177\,189.
$$


It also reports:

- the complete $72$-entry $q$-array;
- the complete $71$-entry monic quotient;
- minimum capped top-$q$ depth $7$;
- $P_{71}(-2)=0\bmod3^{32}$.

The static audit validates the algorithm used for this parameter case. It does not constitute a new execution or authentication of the receipt’s runtime history. The receipt remains a finite arithmetic record, not a proof of periodicity or a physical-return calculation.

Zeros in its arrays mean zero modulo $3^{32}$, not exact zero.

---

# 7. The usable complete-source reduction

## 7.1 Exact endpoint and the $3^{37}$ tail

The reused scalar unit and the finite unit matrix imply that every bracket in (1.1) lies in $\mathbb Z_3$. Hence all $q_a$ are ternary integral.

The complete force gives the exact endpoint identity


$$
\begin{aligned}
\delta Q(-1)
&=-u^Tt-\xi u^Tv\\
&=-\xi(\Xi+u^Tv)\\
&=\boxed{-\xi F_{\rm fac}^2}.
\end{aligned}
\tag{7.1}
$$


This is nonzero. It is not the zero endpoint of the uncorrected core.

By (6.1), for $2\le r\le71$,


$$
v_3(N-r)=v_3(r-1).
$$


Therefore


$$
\begin{aligned}
v_3\!\left(\frac{N!}{(N-72)!}\right)
&=v_3(N-1)+v_3(70!)\\
&=5+(23+7+2)\\
&=37.
\end{aligned}
$$


Thus


$$
q_a\in3^{37}\mathbb Z_3
\qquad(a\le n-73).
$$



Define the complete top polynomial


$$
P_{71}(x)=\sum_{r=0}^{71}q_{n-72+r}x^r.
$$


Then


$$
\delta Q=x^{n-72}P_{71}(x)+L_{\rm tail}(x),
\qquad L_{\rm tail}\in3^{37}\mathbb Z_3[x].
$$


The exact endpoint (7.1), together with the sufficiently deep factorial square, gives


$$
P_{71}(-2)\in3^{37}\mathbb Z_3.
$$



Monic division yields


$$
P_{71}(x)=(x+2)V_{70}(x)+P_{71}(-2),
$$


where


$$
\boxed{
[x^b]V_{70}
=
\sum_{r=b+1}^{71}(-2)^{r-b-1}q_{n-72+r},
\qquad 0\le b\le70.
}
\tag{7.2}
$$


Consequently


$$
\boxed{
\delta Q-(y+1)x^{A-70}V_{70}\in3^{37}\mathbb Z_3[x].
}
\tag{7.3}
$$



This is the source-tail valuation, not the separately assigned weaker $E37$ input-period corollary. No audit of that separate input-period result is duplicated here.

## 7.2 Complete physical columns and finite boundaries

The physical objects remain


$$
U_s=x^s\quad(0\le s<D),
$$




$$
z_i=x^Dy^i\quad(0\le i<\nu),\qquad \nu=D/2-1,
$$




$$
Y_t=y^t\quad(d\le t\le m),\qquad d=D+\nu,
\qquad W=[U\ Y].
$$


The highest physical HIGH column is $Y_m$, inclusively.

The complete functional remains


$$
\mathcal M(P)=
-\frac{3^h}{4}\mathfrak f(P)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](P-P(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^t)=(2t)!.
\tag{7.4}
$$


Its physical cutoff is


$$
K_{\rm phys}=2n-2,
\qquad
2K_{\rm phys}+1=4H_{\rm phys}-4D+5<3^{h+1}.
$$



For $\alpha=c,\mathrm{act}$,


$$
G_\alpha(f,g)=\mathcal M(Q_\alpha fg),
\qquad E_\alpha=G_\alpha(W,W),
$$




$$
F_\alpha[p]
=x^Dp-WE_\alpha^{-1}G_\alpha(W,x^Dp).
\tag{7.5}
$$



The core is


$$
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=-71-A,
$$


and $\beta+3y=b_c+3x$, consistent with the producer bridge.

The finite prefix boundaries remain


$$
R_*=\frac{9Q+1}{2},\qquad
a_0=R_*-1=121P+\frac{P-1}{2},
$$




$$
\tau=\frac{N_0-3}{2},\qquad
\ell=3R+1,
$$




$$
K=\{0,\ldots,\ell-1\},\qquad
J=\{\ell,\ldots,\tau-1\},\qquad
R_*+\tau=\nu.
$$


No last middle or highest HIGH coordinate is deleted.

The supplied original projection bound


$$
E_\alpha^{-1}\in3^{-1}\operatorname{Mat}(\mathbb Z_3)
\tag{7.6}
$$


is reused at its stated scope.

The degree hypotheses are compatible with the physical functional. The columns of $W$, and admitted corrected columns, have degree at most $m$. Since $\deg Q_{\rm act}\le n$,


$$
\deg(Q_{\rm act}fg)\le n+2m=2n-1.
$$


After subtraction of the endpoint and division by $y+1$, the degree is at most the actual cutoff $2n-2$.

Every retained denominator $2v+1$ has ternary valuation at most $h$, so $\mathcal M$ maps the admitted integral polynomials to $\mathbb Z_3$. Thus


$$
F_\alpha[p]\in3^{-1}\mathbb Z_3[y].
$$



## 7.3 Complete return payment with $E_{\rm act}^{-1}$ unchanged

Put


$$
\alpha_\alpha[p]
=E_\alpha^{-1}G_\alpha(W,x^Dp).
$$


For


$$
b_p^\delta=\mathcal M(\delta Q\,W F_c[p]),
$$


finite orthogonality gives


$$
G_{\rm act}(W,F_c[p])
=E_{\rm act}(\alpha_{\rm act}[p]-\alpha_c[p])
=b_p^\delta.
$$


Therefore


$$
\boxed{
E_{\rm act}^{-1}b_p^\delta
=\alpha_{\rm act}[p]-\alpha_c[p]\in3^{-1}M.
}
\tag{7.7}
$$



Now replace $\delta Q$ by $\delta Q+\epsilon$, with


$$
\epsilon\in3^s\mathbb Z_3[x].
$$


The direct term changes by


$$
\mathcal M(\epsilon F_c[p]F_c[q])\in3^{s-2}\mathbb Z_3.
$$


The cross-vector change


$$
c_p=\mathcal M(\epsilon W F_c[p])
$$


lies in $3^{s-1}M$. Using (7.7), the two linear return changes lie in $3^{s-2}$, and the quadratic change lies in


$$
3^{2s-3}\mathbb Z_3.
$$


Thus, for $s\ge2$, the **whole** direct-minus-return expression changes by $3^{s-2}$.

Accordingly:

- the exact tail replacement (7.3) changes the whole expression by $3^{35}$;
- using any coefficient lift of the actual $V_{70}\bmod3^{32}$ changes it by $3^{30}$.

After division by $3^{29}$, the latter change is zero modulo $3$.

This proves the usable reduction:


$$
\boxed{
V_{70}\bmod3^{32}\text{ suffices for the original complete normalized correction modulo }3,
}
$$


with the original $E_{\rm act}^{-1}$, $W$, and physical terminal retained.

---

# 8. Exact remaining $W$-return and a concrete certificate lemma

## 8.1 The actual observed inputs

Retain the nine established bands


$$
\mathcal S=\{14,15,16,41,42,43,95,96,97\}.
$$


In Range III put


$$
\Pi=P/3,\qquad \eta=\Pi-c,
$$


and use the actual integral lift


$$
g_i(y)=2y^i(1-y)^\eta\sum_{r\in\mathcal S}y^{rP}.
$$


Its admitted degree is below $a_0$. Define


$$
\widehat F_i=F_c[g_i].
$$



The outstanding complete correction is


$$
\boxed{
\begin{aligned}
\mathcal N_{ij}={}&
\mathcal M\!\left(
(y+1)x^{A-70}V_{70}\,\widehat F_i\widehat F_j
\right)\\
&-
\mathcal M\!\left(
(y+1)x^{A-70}V_{70}\,W\widehat F_i
\right)^T
E_{\rm act}^{-1}
\mathcal M\!\left(
(y+1)x^{A-70}V_{70}\,W\widehat F_j
\right).
\end{aligned}
}
\tag{8.1}
$$



At the original scope where the complete comparison supplies the $3^{29}$ divisibility, the desired value is


$$
\mathcal N_{ij}/3^{29}\pmod3.
$$



For $i=j=0$, the input is exactly


$$
g_0=2(1-y)^\eta\sum_{r\in\mathcal S}y^{rP}.
$$


All $9\times9$ band pairs are present. The established divisibility is a divisibility of the complete aggregate; it does not permit division of each individual band-pair summand by $3^{29}$.

The component


$$
\mathcal M\!\left(
(y+1)x^{A-70}V_{70}\,Y_m\,\widehat F_0
\right)
$$


remains part of the return vector.

## 8.2 Why the producer jet does not evaluate this expression

Producer localization concerns $\widehat T_n$. It supplies no corresponding locality theorem for $E_{\rm act}^{-1}$.

A short raw producer does not establish short support for


$$
\widehat F_i
=x^Dg_i-WE_c^{-1}G_c(W,x^Dg_i).
$$


The correction may acquire LOW feedback and HIGH components extending to the actual terminal $Y_m$. Its original monomial exponents and the active physical poles of $\mathcal M$ also change with the original index.

The packet therefore does not contain a bounded, complete evaluation of the projected-column observations and return needed in (8.1). The coefficient jet cannot be used to manufacture a value for $\mathcal N_{00}$.

## 8.3 New proved lemma: a paid complete-return residual certificate

The following gives a concrete next certificate target.

Let $\widetilde V_{70}$ be an integral lift of the actual quotient modulo $3^{32}$, and put


$$
Q_s=(y+1)x^{A-70}\widetilde V_{70}.
$$


Define


$$
\Phi_i=3\widehat F_i\in\mathbb Z_3[y],
$$




$$
B_i=\mathcal M(Q_sW\Phi_i)\in\mathbb Z_3^{\dim W},
$$




$$
D_{ij}=\mathcal M(Q_s\Phi_i\Phi_j)\in\mathbb Z_3.
$$


Set $E=E_{\rm act}$.

Then


$$
9\mathcal N_{ij}^{\,s}=D_{ij}-B_i^TE^{-1}B_j.
\tag{8.2}
$$



Moreover,


$$
E^{-1}B_i\in\mathbb Z_3^{\dim W}.
\tag{8.3}
$$


For the exact source this follows from (7.7):


$$
E^{-1}B_i
=3(\alpha_{\rm act}[g_i]-\alpha_c[g_i]).
$$


Replacing the source by $Q_s$ changes $B_i$ by $3^{32}$, and therefore changes $E^{-1}B_i$ by $3^{31}$, preserving integrality.

### Certificate statement

Suppose integral vectors $z_i$ satisfy the **complete finite residual equations**


$$
\rho_i:=B_i-Ez_i\in3^{17}\mathbb Z_3^{\dim W}.
\tag{8.4}
$$


Then


$$
\boxed{
\Theta_{ij}
=
D_{ij}-B_i^Tz_j-z_i^TB_j+z_i^TEz_j
}
\tag{8.5}
$$


satisfies


$$
\Theta_{ij}\equiv9\mathcal N_{ij}^{\,s}\pmod{3^{32}}.
\tag{8.6}
$$



#### Proof

The exact bilinear completion identity is


$$
B_i^TE^{-1}B_j
=
B_i^Tz_j+z_i^TB_j-z_i^TEz_j
+\rho_i^TE^{-1}\rho_j.
$$


By (7.6) and (8.4),


$$
\rho_i^TE^{-1}\rho_j\in3^{17+17-1}\mathbb Z_3
=3^{33}\mathbb Z_3.
$$


Substituting into (8.2) proves (8.6). ∎

For $i=j=0$,


$$
\Theta_{00}=D_{00}-2B_0^Tz_0+z_0^TEz_0.
$$


If the original complete comparison supplies $\mathcal N_{00}\in3^{29}\mathbb Z_3$, then the source replacement in §7 gives


$$
\boxed{
\frac{\mathcal N_{00}}{3^{29}}
\equiv
\frac{\Theta_{00}}{3^{31}}\pmod3.
}
\tag{8.7}
$$


The division by $3^{31}$ is made only after forming the complete aggregate $\Theta_{00}$.

### What this advances—and what it does not

This is a proved precision certificate in the original complete objects:

- residual precision $3^{17}$;
- complete aggregate precision $3^{32}$;
- final paid division by $3^{31}$.

It does **not** provide the vectors $z_0$, their complete residual certificate, or the evaluated aggregate. A precision-sized construction of those complete observations, including the LOW feedback and $Y_m$ return, remains the concrete follow-on obligation.

Thus this lemma does not close $\mathcal N_{00}$ merely by renaming an unevaluated sum.

---

# 9. Other complete returns and global arithmetic remain unchanged

The separate complete forcing identity remains


$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
$$


The physical terminal component is retained.

The complete source recurrence remains


$$
\mu_{t+1}+\mu_t
=
\frac{3^h}{2t+1}
-\frac{3^h}{4}\bigl((2t+2)!+(2t)!\bigr),
\qquad 0\le t\le2n-2,
$$


with


$$
t_*=\frac{3^h-5}{2}.
$$



The distinct diagonal frames are not exchanged:


$$
\lambda_{\rm new}
=
\lambda^{\rm pref}
-\frac13f_J^TB^{-1}f_J
-\frac19f_b^TA_b^{-1}f_b
\in3^{-2}\mathbb Z_3,
$$


whereas


$$
\lambda_4
=
\lambda_{\rm new}
-\frac1{81}f_C^TA_4^{-1}f_C
\in3^{-4}\mathbb Z_3.
$$


The physical-$5$ complementary returns remain active at order $7$. No whole physical-seventh assembly is certified by this report.

## 9.1 Contents, least clearer, and all-prime final gcd

No local result here changes or evaluates the actual integer column contents or the least simultaneous clearer $\ell_{\rm clr}$.

Retain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


and the gcd over **all primes**


$$
g_\ell=\gcd(|A_\ell|,|B_\ell|).
$$


For $B_\ell\ne0$, the actual primitive pair is


$$
q_{\rm prim}=\frac{|B_\ell|}{g_\ell},
\qquad
p_{\rm prim}
=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$



The whole evaluated error remains


$$
\boxed{
q_{\rm prim}(e+\pi)-p_{\rm prim}
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
{g_\ell}\det H_{\rm complete}.
}
\tag{9.1}
$$



An irrationality proof still requires, at the **same infinite original indices** satisfying the real residual conditions,


$$
B_\ell\ne0,\qquad \det H_{\rm complete}\ne0,
$$


and


$$
\boxed{
\log g_\ell-(m+1)\log\ell_{\rm clr}
-\log|\det H_{\rm complete}|
\longrightarrow+\infty.
}
\tag{9.2}
$$



These conditions would make the nonzero whole integer linear forms tend to zero. If $e+\pi=a/b$ were rational, every such nonzero form would have absolute value at least $1/|b|$.

The producer fact $\Xi\ne0$ is not nonvanishing of the whole determinant. A ternary coefficient depth is not an all-prime content or primitive-denominator estimate.

---

# 10. Status ledger and indispensable bounded check

| Item | Status after this report |
|---|---|
| Old scalar unit/depth theorem and complete notation bridge | **REUSED; not reopened** |
| Formal generating function and all-degree Newton valuation | **PROVED in this audit** |
| Literal finite Pascal identity and entry admission | **PROVED in this audit** |
| All finite modulo-$3$ block inverses | **Explicitly verified** |
| Weighted Neumann paths, maximum excursion, actual end window | **PASS** |
| Complete force, next column, raw reconstruction, scalar division | **PASS** |
| Program on all accepted $M,L$ | **FAIL until Pascal-row allocation repair** |
| Program at $M=33,L=72$ | **PASS in static audit; saved solve not repeated** |
| Every-precision finite block law | **Separate different audit still pending** |
| Weighted $3^M$ complete-source period | **PASS conditional on that law** |
| Six direct/local comparisons and generator receipt | **Finite corroboration only; not rerun** |
| $4950/99/99$ weighted compatibility receipt | **Finite corroboration only; not a theorem** |
| Saved $j=84645$ producer jet | **Reused finite arithmetic record; no real-window admission implied** |
| Actual $72$-coefficient source replacement and two-digit projection payment | **Available at stated original scope** |
| Complete residual-certificate lemma of §8.3 | **New proved statement** |
| Actual $\mathcal N_{00}$ and complete physical-$7$ return | **OPEN** |
| Actual contents, least clearer, all-prime gcd, primitive denominator, whole nonzero-error decay | **OPEN** |
| Rationality or irrationality of $e+\pi$ | **UNRESOLVED** |

## 10.1 One new bounded helper check for the implementation repair

No original matrix solve and none of the six old direct/local comparisons needs to be repeated.

If the allocation repair is adopted, the indispensable new regression concerns only the previously unallocated Pascal entry.

### Bounded inputs



$$
M=4,\qquad L=24,\qquad n_{\rm res}=200,
$$


so


$$
H=23,\quad \text{top}=24,\quad K=24,\quad
R_{\rm loc}=68,\quad E=8.
$$



Test only the repaired binomial-row helper at


$$
a=200,\qquad 0\le s\le24,\qquad \text{modulus }81.
$$



### Expected verifiable output

- the row has length $25$;
- its entry at index $24$ exists;
- that entry is
  

$$
\boxed{\binom{200}{24}\equiv63\pmod{81};}
$$


- every Pascal index used by the $L=24$ reconstruction is within the repaired allocation.

For an independent arithmetic check,


$$
v_3\binom{200}{24}
=(66+22+7+2)-(8+2)-(58+19+6+2)=2.
$$


The $3$-free factorial units modulo $9$ are


$$
U(200!)=8,\qquad U(24!)=1,\qquad U(176!)=5.
$$


Hence the binomial unit is $8/5\equiv7\pmod9$, giving $9\cdot7=63\pmod{81}$.

This is a small new helper regression, not a rerun of a matrix comparison.

No bounded arithmetic gate for an actual $\mathcal N_{00}$ value is justified from this packet alone. The complete projected-column/return reduction identified in §8 must first be supplied.

---

# Conclusion

The principal new outcome is a complete independent proof audit of the parent’s precision-local producer theorem. Its mathematical localization is valid. The supplied implementation has one precise domain-level indexing defect, with a repair that preserves its advertised inputs and leaves the saved $M=33,L=72$ computation unchanged.

The stronger weighted complete-source period has also been fully checked as a deduction. It preserves the actual complete force, both affine constants, the true next column, the $n-1$ unit denominator, all scalar coordinates, and the one-digit scalar division. It yields the frozen original progression


$$
j=84645+3^{32}t
$$


only conditionally on the separately audited every-precision finite block law.

The usable consequence is a frozen coefficient source modulo $3^{32}$, not a frozen physical return. The exact remaining local bottleneck is the complete original $\mathcal N_{00}$ evaluation, including the full corrected column and $Y_m$ return. The residual-certificate lemma above gives a concrete paid target for that next step.

No primitive-content saving, no retirement of a physical return, and no unconditional rationality or irrationality conclusion for $e+\pi$ follows.
