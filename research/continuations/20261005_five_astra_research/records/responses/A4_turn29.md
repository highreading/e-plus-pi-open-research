> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 audit report: actual polynomial precision and the complete fifth binary input

## 1. Verdict and source scope

**Both construction audits pass at their stated dependencies.**

1. **A1turn28 closes the actual force-and-coordinate interface.** The support formula is for the original factorial-divided $\psi$-coordinates, with the correct sign
   

$$
\theta=3\eta_N\equiv2\pmod3.
$$


   The three dangerous lower coordinates are $\eta_{N-1},\eta_{N-2},\eta_{N-3}$, not $\eta_N$. The latter supplies the retained leading correction.

2. **The new $m=1$ coefficient lemma also passes**, after explicitly checking the effect of the polynomial prefactors in the complete moment formula. Its conclusion is an ordinary-coefficient congruence, not an inference from unrestricted integer-value congruences.

3. **A5turn20 closes the complete central forcing and $P_{64}$ transfer.** The central-index tail, forcing-index tail, finite inverse iterates, weighted parameter losses, and surviving contact correction are all accounted for.

4. With the previously audited $Q_{128}$ transfer retained, **the whole mixed reduction to 31 potential residue classes passes**. This includes the overflow classes $96,100$, their shorter ranges, and the actual endpoint.

What remains unproved is the evaluation of the resulting unit-sensitive bilinear convolution on the original power-$9$ domain. The supplied 32 auxiliary evaluations do not resolve it.

### Verification gate

I compared the supplied reports and controls, including the corrected coordinator support proof and the fixed polynomial and moment certificates. No external archive or primary-literature search facility is available here; I therefore do not claim a fresh external search or independent execution of the attached computations. The archive’s recorded literature searches remain source statements. The arguments below use classical factorial divisibility, Pascal inversion, Schur elimination, Newton polynomials, and Lucas–Kummer arithmetic; no global novelty claim is made.

The exact endpoint and dyadic-center theorems are separate dependencies. Their absence from this packet neither proves nor disproves them. In particular, I do not restore the unsupported assertion $v_2(q)=n+2$ found in earlier A1 reports.

---

## 2. A1: the actual forcing and original-coordinate support

Set


$$
n=4^j+1,\qquad N=n-1=3M+1,\qquad L=3M=N-1.
$$


The finite Gram system has indices $0\le i,k<n$, with


$$
\psi_0=1,\qquad
\psi_{d+1}=\frac{(y+1)(y-1)^d}{d!},
\qquad
\psi_n=\frac{h_n}{N!},
$$


and


$$
G_{ik}=\rho(\psi_i\psi_k),\qquad
\omega_i=\rho(\psi_i\psi_n),\qquad
\eta=G^{-1}\omega.
$$



### 2.1 Complete force: pass

Under $y=(1-t)^2$,


$$
y-1=t(t-2).
$$


For integral $F$, the integral $\mu((y-1)^sF)$ is therefore an integer combination of factorials $(s+a)!$, and is divisible by $s!$.

Consequently the complete force is integral:


$$
\omega_0=\frac{\mu((y+1)(y-1)^N)}{N!}\in\mathbb Z,
$$




$$
\omega_{d+1}
=\frac{\mu((y+1)^2(y-1)^{d+N})}{d!\,N!}\in\mathbb Z,
\qquad 0\le d\le L.
$$


The last assertion uses


$$
\frac{(d+N)!}{d!\,N!}\in\mathbb Z.
$$


No factorial summand has been discarded. The negative mass contributes zero to these forces because $\psi_n(-1)=0$, whereas the constant Gram entry remains the signed value $G_{00}=0$.

### 2.2 Exceptional column and sign: pass

The regular block consists of precisely $d=0,\ldots,L-1$. Its reduction is


$$
\bar E=B_M\otimes A,\qquad
A=\begin{pmatrix}0&2&1\\2&2&0\\1&0&0\end{pmatrix},
\qquad
B_M(D,E)=\binom{D+E}{D}.
$$


Both factors are invertible modulo $3$, so $E^{-1}$ is integral over $\mathbb Z_3$.

The exact Pascal inversion


$$
(B_M^{-1}b)_D=(-1)^{M-1-D}\binom MD,
\qquad b_D=\binom{M+D}{D},
$$


identifies the reduction of the eliminated exceptional column in the original $\psi$-coordinates.

Retaining both Schur forces, the actual solve is


$$
\eta_N=\frac{\xi_L-(\beta/a)\xi_0}{\delta},
\qquad
\eta_{\rm const}=\frac{\xi_0-\beta\eta_N}{a},
$$




$$
\eta_E=E^{-1}\omega_E-E^{-1}u\,\eta_{\rm const}
                     -E^{-1}x\,\eta_N.
$$


The audited first lift gives


$$
a\equiv2,\quad \beta\equiv0,\quad
\delta/3\equiv1,\quad \xi_L\equiv2,\quad\xi_0\equiv0\pmod3.
$$


Hence


$$
\theta=3\eta_N\equiv2\pmod3,\qquad
\eta_{\rm const}\in\mathbb Z_3,
$$


and


$$
\boxed{
3\eta_{d+1}\equiv
\begin{cases}
\theta(-1)^{M-D}\binom MD,&d=3D,\quad 0\le D\le M,\\
0,&3\nmid d
\end{cases}
\pmod3.}
$$



The positive sign relative to the radical vector is correct: the minus sign in $-E^{-1}x\,\eta_N$ changes $(-1)^{M-1-D}$ into $(-1)^{M-D}$. A separate minus sign appears in the polynomial expansion.

### 2.3 Last-three factorial terms: pass

The exact monic polynomial is


$$
P_n=h_n-N!\eta_{\rm const}
-\sum_{d=0}^{N-1}\frac{N!}{d!}\eta_{d+1}h_{d+1}.
$$


Assume $m=v_3(M)=v_3(j)\ge1$. After retaining $d=L$, the next three terms in $3P_n$ are


$$
-NL(3\eta_L)h_L,
$$




$$
-NL(L-1)(3\eta_{L-1})h_{L-1},
$$




$$
-NL(L-1)(L-2)(3\eta_{L-2})h_{L-2}.
$$


Their $\eta$-labels are exactly $N-1,N-2,N-3$.

Each factorial quotient has depth $m+1$. The support formula gives respective residues


$$
0,\qquad0,\qquad-M\theta
$$


for their $3\eta$-factors. Thus all three terms have depth at least $m+2$.

Every lower quotient contains both $L$ and $L-3$, whose valuations are $m+1$ and $1$. The constant term has depth at least


$$
1+v_3(N!)\ge m+2.
$$


Therefore, without using the separate doubled-factorial endpoint theorem,


$$
3P_n\equiv
(y+1)(y-1)^L\bigl(3(y-1)-N\theta\bigr)
\pmod{3^{m+2}}.
$$



**The formerly missing actual support application is now closed.**

---

## 3. Independent audit of the $m=1$ coefficient lemma

The point requiring care is that a value congruence on integers does not ordinarily imply an ordinary-coefficient congruence. Here the degree restriction makes the conversion valid.

### 3.1 The $\ell\ge6$ coefficient cutoff

For the summands


$$
P_\ell(s)=\frac{(-1)^\ell}{2^\ell\ell!}
\prod_{a=-\ell+1}^{\ell}(s+a),
$$


the retained bound is


$$
v_3([T^k]P_\ell(3T+r))
\ge
\max\{k,\lfloor2\ell/3\rfloor\}-v_3(\ell!).
$$


For every $\ell\ge6$,


$$
\lfloor2\ell/3\rfloor-v_3(\ell!)\ge2.
$$


For instance, the general lower bound $\ell/6-1$ handles $\ell\ge18$, and the finite range $6\le\ell\le17$ verifies directly.

For $0\le\ell\le5$:

* every nonconstant coefficient has depth at least one;
* every coefficient of degree at least three has depth at least two.

Also


$$
(-8)^T\equiv1\pmod{9\mathbb Z_3[[T]]},
$$


since $v_3(\log(-8))=2$. Thus each $B_r(T)=b_{3T+r}$, modulo $9$, has degree at most two and nonconstant coefficients divisible by $3$.

### 3.2 Complete moment prefactors: pass

This must be checked before claiming the same degree bound for $e_{3T}$. Its formula is


$$
e_{3T}
=4B_0(T)+4(3T+1)B_1(T)
 +(3T+1)(3T+2)B_2(T).
$$


Modulo $9$,


$$
(3T+1)(3T+2)\equiv2.
$$


Moreover, multiplying the nonconstant coefficients of $B_1$ by $3T$ produces multiples of $9$. Hence the complete expression still has degree at most two modulo $9$.

An explicit coefficient certificate, deduced from these bounds and the proven value formulas, is


$$
\begin{aligned}
B_0(T)&\equiv1+6T+6T^2,\\
B_1(T)&\equiv0,\\
B_2(T)&\equiv4+6T+6T^2,\\
B_3(T)&\equiv4+6T^2
\end{aligned}
\pmod9.
$$


To justify this conversion, subtract the proposed polynomial. Its coefficients are divisible by $3$; after dividing by $3$, it has degree at most two over $\mathbb F_3$ and vanishes at all three residues. It is therefore zero.

Substitution into the complete moment formula yields


$$
\boxed{e_{3T}\equiv3\pmod9}
$$


coefficientwise. Similarly,


$$
\boxed{e_{3T+1}\equiv2\pmod3}
$$


coefficientwise.

### 3.3 Contraction and nonlinear inversion

The raw contraction is not being assumed multiplicative. What is used is that it is integral, Gauss-norm nonincreasing, and sends the constant input $1$ to $1$. Together with $J\equiv1\pmod3$ and the adjacent multiplier’s reduction, this gives


$$
H(T)\equiv1,\qquad G(T)\equiv2
\pmod{3\mathbb Z_3[[T]]}.
$$



The nonlinear step is then legitimate: $H(0)=4$ is a unit, its formal inverse has integral coefficients, and


$$
G/H\equiv2\pmod3.
$$


Evaluation at $M\in3\mathbb Z_3$ converges. Every nonconstant coefficient of $(1+3T)G/H$ is divisible by $3$.

Using the retained true jet,


$$
(1+3M)\Theta_{\rm raw}(M)
=68+a_1M+\sum_{r\ge2}a_rM^r,
$$


where


$$
a_1\equiv3\pmod{27},\qquad a_r\in3\mathbb Z_3.
$$


Thus


$$
v_3(a_rM^r)\ge1+2m\ge m+2
$$


for all $m\ge1$. With turn17’s projection theorem at its stated hypotheses,


$$
N\theta\equiv68+3M\pmod{3^{m+2}}.
$$



Consequently,


$$
\boxed{
3P_n\equiv
(y+1)(y-1)^{n-2}\bigl(3y-71-(n-2)\bigr)
\pmod{3^{v_3(j)+2}},
\qquad 3\mid j.}
$$



This closes the actual polynomial-precision input, including $m=1$, **relative to the independently retained jet/projection theorem**. It is a lower bound on precision, not a claim that the difference always has exactly that valuation.

For the primitive polynomial one must retain


$$
Q_n=\lambda_n(3P_n),\qquad
\lambda_n=\operatorname{lc}(Q_n)/3\in\mathbb Z_3^\times.
$$


The unit is not removable from actual matrix contractions.

---

## 4. A5: complete central force and $P_{64}$ transfer

Here the domain remains


$$
b=9^r,\quad n=4002b,\quad r=18+32u,\quad u\ge0,
$$




$$
b=128D+81,\quad n=128C+66,\quad C=4002D+2532.
$$


In particular,


$$
h=n/2\equiv161\pmod{256},\quad
n\equiv322\pmod{512},\quad b\equiv209\pmod{256}.
$$



### 4.1 Both central truncations: pass

The scalar coefficients in the complete central sums have valuation


$$
v_2\!\left(\frac{2^s(s!)^2}{(2s)!}\right)
=
v_2\!\left(\frac{2^s(s!)^2}{(2s+1)!}\right)
=v_2(s!).
$$


After extracting the power of two, division is by an odd unit. Thus $s\ge8$ vanishes modulo $64$.

For central index $\ell\ge7$, the relevant falling factorial contains $h-1$ and $h-3$, of depths $5$ and $1$. This proves the entire central-index tail vanishes modulo $64$.

There is a minor wording correction: $v_2(h-1)=5$ follows from $h\equiv161\pmod{256}$, not from $h\equiv1\pmod{32}$ alone. The actual domain supplies the stronger congruence.

The binomial parameter estimate


$$
v_2\!\left(\binom{x+\delta}{k}-\binom{x}{k}\right)
\ge v_2(\delta)-\lfloor\log_2k\rfloor
$$


then transfers every retained complete central sum to $h=161$. The attached finite evaluation supplies


$$
B^{\rm cen}_{0:6}\equiv(2,3,3,32,0,32,32)\pmod{64}.
$$



### 4.2 Complete forcing tail: pass

The force remains


$$
\frac{f_i^0}{R}
=\sum_{\ell=0}^{i}\binom i\ell
 \prod_{t=\ell+1}^{i}(n+t)\,B^{\rm cen}_\ell.
$$


At $i=8$, the product depths for $\ell=0,\ldots,6$ are


$$
(7,7,5,5,4,4,1).
$$


Combined with the central depths, only $\ell=2$ needs an additional argument. At $i=8,9$, $\binom i2$ has depth two; for $i\ge10$, the product itself has sufficient depth. Therefore


$$
f_i^0/R\equiv0\pmod{64}\qquad(i\ge8).
$$



The supplied bounded evaluation consequently gives the **complete** forcing and Newton polynomial:


$$
f^0/R\equiv(2,9,51,57,12,36,48,16,0,\ldots),
$$




$$
g_{64}=(2,55,51,7,12,28,48,48)
$$


in Newton coordinates modulo $64$.

### 4.3 Finite inverse and weighted losses: pass

The integral operator raises degree by at most four. Splitting the forcing into pieces of coefficient depths $0,2,4$, with degrees at most $3,5,7$, gives retained iterate bounds $5,3,1$, respectively. Hence


$$
\deg P_{64}\le23.
$$


The weighted $b$-parameter estimates in A5turn20 meet every required precision; the reference $b=209$, rather than $81$, is essential at the first iterate.

The $n$-parameter correction relative to $n=2$ is retained:


$$
P_{64}\equiv
\sum_{\ell=0}^{5}(-2\mathscr E_{2,209})^\ell g_{64}
+32\left(\binom x5+\binom x6+\binom x7\right)
\pmod{64}.
$$


The supplied coefficient certificate through the proved degree bound therefore establishes


$$
\boxed{
P_{64}=(34,31,7,5,48,12,4,4,32,8,56,8)
\pmod{64},}
$$


with all higher Newton coefficients zero.

The reconstruction still uses the actual $T(-2n)$, actual range $0\le i<b$, and


$$
2X_j\equiv W_j(j\theta_{j-1}-\theta_j)\pmod{64}.
$$


No large kernel has been replaced by its reference value.

---

## 5. Whole mixed support: precision, endpoint, and overflow

Retain the audited $Q_{128}$, all seven exterior values, and the complete logarithmic-force bound. The latter removes the whole logarithmic force at this precision, not selected terms.

With $U_s,V_s$ defined in A5turn20, the actual interior reconstruction is


$$
2X_j\equiv(-1)^{j+1}W_j\mathcal F_j\pmod{64},
$$




$$
4(Y_j-X_j)\equiv(-1)^{j+1}W_j\mathcal G_j\pmod{128}.
$$


The negative moment indices $-8\le s<0$ in $\mathcal G_j$ retain the complete exterior force.

### 5.1 Raw precision and division: pass

The correct raw modulus is $512$:


$$
8X_j(Y_j-X_j)\equiv W_j^2\mathcal F_j\mathcal G_j\pmod{512}.
$$


Errors in $\mathcal F_j\bmod64$ are harmless because


$$
W_j\mathcal G_j\in8\mathbb Z_2;
$$


errors in $\mathcal G_j\bmod128$ are harmless because


$$
W_j\mathcal F_j\in4\mathbb Z_2.
$$


These follow from the retained actual evenness of $X,Y$.

Division by $256$ is made only after forming the complete raw sum. Individual terms need not permit that division.

### 5.2 High-weight mixed exclusion: pass

For $w=v_2(W_j)\ge5$, the raw product already vanishes modulo $512$. At $w=4$, one further parity factor is needed.

The displayed parity formulas provide it:

* even $j$: $\mathcal M_{-1}(j)$ is even;
* $j\equiv3\pmod4$: $\mathcal M_{-2}(j)$ is even;
* $j=4k+1$: the exact weight formula forces $k$ even when $w=4$, and then Lucas forces $\mathcal M_0(j)$ even.

Thus


$$
v_2(W_j)\ge4
\Longrightarrow X_j(Y_j-X_j)\equiv0\pmod{64}.
$$


This is a mixed-product argument. Norm support alone would not suffice.

### 5.3 Exhaustive surviving ranges: pass

For $0\le\rho\le68$, the potential residues are


$$
\begin{array}{c|l}
v_2\binom{68}{\rho}&\rho\\ \hline
0&0,4,64,68\\
1&2,32,36,66\\
2&1,3,16,20,34,48,52,65,67\\
3&8,12,18,24,28,33,35,40,44,50,56,60.
\end{array}
$$


Their range is $0\le t\le D$, subject to


$$
v_2\binom Ct\le3-v_2\binom{68}{\rho}.
$$



For $\rho>68$, the borrow gives


$$
v_2(W_{128t+\rho})
=v_2\binom{196}{\rho}
 +1+v_2\binom{C-1}{t}.
$$


The only additional potential residues are


$$
\boxed{\rho=96,100,}
$$


both with


$$
0\le t\le D-1,\qquad \binom{C-1}{t}\text{ odd}.
$$


No other overflow residue survives. There are exactly $29+2=31$ potential classes.

At the actual endpoint,


$$
X_b=\frac{W_b b\theta_{b-1}}2,\qquad
Y_b=\frac{W_b(1+b\eta_{b-1})}{4}.
$$


Retaining the $+1$, the established $v_2(W_b)\ge6$ gives


$$
X_b(Y_b-X_b)\in2^9\mathbb Z_2.
$$


It contributes zero at the fifth discrepancy.

---

## 6. The exact unresolved arithmetic identity

The complete remaining scalar is A5turn20’s $\mathscr S$, using


$$
M_s(\rho,t)=
\binom{128(2C+1+D-t)+84-\rho}
      {128(D-t)+80-\rho-s},
$$




$$
F_\rho(t)=\sum_{s=-1}^{11}U_s(\rho)M_s(\rho,t),\qquad
G_\rho(t)=\sum_{s=-8}^{11}V_s(\rho)M_s(\rho,t),
$$


and the 31 classes with precisely the restrictions above. It satisfies


$$
\boxed{\mathscr S\equiv8(H-N)\pmod{512}.}
$$



The immediate target is therefore the following **unproved identity**:


$$
\boxed{\mathscr S\equiv0\pmod{512}}
$$


on


$$
C=4002D+2532,\qquad
D=\frac{9^{18+32u}-81}{128},
\qquad
\left\lfloor D/4\right\rfloor\mathbin{\&}
\left(\frac{C-2}{4}+1\right)\ne0.
$$


It would prove $\Delta_5=0$ on the actual common-zero locus.

The auxiliary receipt establishes this zero only for the stated 32 odd integers $1\le D\le63$, including 21 cases satisfying the bit condition. None is an original power-$9$ exponent. Coefficient periodicity does not make the actual large binomial kernels periodic in $D$; hence the receipt supplies no infinite conclusion.

### Concrete follow-on lemma for denominator control

A stronger, directly useful target is a relative-alignment lemma:


$$
\boxed{v_2(H-N)>v_2(N).}
$$


If it holds at an index, then


$$
H=N+(H-N)
$$


has the same valuation as $N$, so $\gamma=\alpha$.

More generally, a uniform upper bound


$$
\gamma-\alpha\le C_0
$$


would immediately give the genuine denominator lower bound


$$
v_2(q_n)\ge
\max\left\{0,\frac{3n}{2}-v_2(b!)-s_2(n)-1-C_0\right\}.
$$


This is actual denominator control, not an irrationality proof. A fifth-digit identity alone gives $\gamma=\alpha=5$ where $N\equiv32\pmod{64}$; where $N\equiv0\pmod{64}$, it merely moves the unresolved comparison to greater depth.

---

## 7. Primitive normalization and the whole evaluated error

For the paired-polynomial construction, retain the complete rational matrix


$$
R_{ij}=\sum_{t=0}^n Q_{n,t}
\left(-(2(i+j+t))!
+4\sum_{a=1}^{i+j+t}\frac{(-1)^{i+j+t-a}}{2a-1}\right),
\quad 0\le i,j<k.
$$


If


$$
\det H_{\rm complete}=\beta_0+\beta_1(e+\pi),
$$


and $d_*$ is the least coefficient clearer with final content $g_*$, then the primitive multiplier is $d_*/g_*$. Equivalently, with the full integer pair $A_\ell,B_\ell$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
$$




$$
q(e+\pi)-p
=\frac{\operatorname{sgn}(B_\ell)\ell^k}{g_\ell}
 \det H_{\rm complete}.
$$


The new polynomial congruence does not evaluate this final gcd.

For the binary construction, preserve the original metric


$$
\Omega=\operatorname{diag}\bigl((n+2)_{\underline j}^{\,2}\bigr)_{0\le j\le b},
$$


the least actual clearer $d_B$, and


$$
A_B=N_{B,1}^T\Omega N_{B,1},\quad
H_B=N_{B,1}^T\Omega N_{B,2},\quad
g_B=\gcd(A_B,|H_B|).
$$


Then


$$
q_n=A_B/g_B,\qquad p_n=H_B/g_B,
$$


with primitive multiplier $d_B^2/g_B$, and


$$
v_2(q_n)=
\max\left\{0,\frac{3n}{2}-v_2(b!)-s_2(n)-1-(\gamma-\alpha)\right\}.
$$



At the retained scope of the complete signed-error theorem,


$$
q_n(e+\pi)-p_n=-q_n\epsilon_n>0
$$


eventually. The complete error, including exponential residual, logarithmic force, finite boundary, and endpoint, must be multiplied by the actual reduced denominator. Neither audit proves that this whole primitive error tends to zero.

---

## 8. Closing ledger and bounded calculation

### New result and proof status

The independent audit closes:

* the actual regular forcing and original-coordinate radical support;
* the corrected last-three factorial-tail argument;
* ordinary-coefficient precision for $m=1$, including the nonlinear inversion step;
* the complete central-force and $P_{64}$ transfer;
* the whole fifth mixed reduction, with all 31 potential residue classes and the actual endpoint.

The actual polynomial congruence is now available at the stated jet/projection dependencies. The fifth binary **input** is complete; the fifth binary **convolution evaluation** is not.

### Exact remaining bottleneck

Locally, the unresolved arithmetic is the evaluation of $\mathscr S\bmod512$ with actual higher-digit binomial units and finite ranges. Beyond fixed precision, actual denominator control requires an unrestricted relative-valuation estimate and the final gcd. Irrationality requires a same-index estimate for the whole nonzero primitive error.

### Bounded exact-arithmetic calculation

No repeat degree scan is needed. A small independent certificate for the only new A1 coefficient step has inputs


$$
P_\ell(3T+r),\qquad 0\le\ell\le5,\quad 0\le r\le3.
$$


Using exact rational arithmetic before reduction, it should output


$$
(B_0,B_1,B_2,B_3)
\equiv
(1+6T+6T^2,\ 0,\ 4+6T+6T^2,\ 4+6T^2)\pmod9,
$$


followed by


$$
e_{3T}\equiv3\pmod9,\qquad e_{3T+1}\equiv2\pmod3
$$


coefficientwise. The proved $\ell\ge6$ bound certifies the omitted tail.

For the binary problem, further auxiliary samples would remain samples. A proof-producing next step must supply a carry-and-unit recurrence for the complete raw convolution, including its terminal boundary conditions, and prove that recurrence before using any finite state certificate.

**No unconditional proof or disproof of the irrationality of $e+\pi$ follows. The construction interfaces advance, but the decisive arithmetic bottleneck remains unresolved.**
