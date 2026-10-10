> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5 — the fourth norm digit reduces to a new, explicit carry test

On the unchanged original domain


$$
\boxed{b=9^r,\qquad n=4002b,\qquad r=18+32u,\quad u\ge0,}
$$


write, as before,


$$
b=128D+81,\qquad n=128C+66,\qquad C=4002D+2532.
$$


Thus $D$ is odd and $C\equiv2\pmod4$. Define


$$
\boxed{a=\frac{C-2}{4},\qquad v=\left\lfloor\frac D4\right\rfloor.}
$$



The actual fourth norm digit is


$$
\boxed{\frac{N}{16}\equiv
\binom{a+v+1}{v}\pmod2.}
\tag{1}
$$


Equivalently,


$$
\boxed{N\equiv16\binom{a+v+1}{v}\pmod{32}.}
\tag{2}
$$



Consequently its exact zero/nonzero criterion is


$$
\boxed{\frac N{16}=1\pmod2
\iff v\mathbin{\&}(a+1)=0.}
\tag{3}
$$



This test retains the unrestricted higher digits of the **actual** $9^r$. It is not a condition on independently chosen cylinder parameters.

There are genuine common-zero subclasses in the original exponent domain. In particular,


$$
\boxed{r=50+128w,\quad w\ge0
\quad\Longrightarrow\quad N\equiv0\pmod{32}.}
\tag{4}
$$


Combining this with the retained fourth-discrepancy congruence $H\equiv N\pmod{32}$ gives


$$
\boxed{\alpha,\gamma\ge5\qquad(r=50+128w).}
\tag{5}
$$


Thus $\alpha=\gamma=4$ does **not** hold everywhere on $r\equiv18\pmod{32}$.

The norm proof below is independent of the fourth mixed-discrepancy calculation. In particular, it does not use the new $Q^\#$-coefficients or the value $K(16)=48$.

---

## 1. Actual columns, metric, finite ranges, and precision

Retain


$$
h=\frac n2,\qquad R=2^h\binom{2h}{h},
\qquad \lambda=\frac{(n!)^2}{2^n},
$$


and the actual normalized weighted columns


$$
X=\frac{Z_w}{2R},\qquad Y=\frac{V_w}{4b!}.
$$


The metric remains


$$
W_j=\binom{n+2}{j},\qquad
\omega_j=j!W_j=(n+2)_{\underline j},
\qquad
\Omega=\operatorname{diag}(\omega_j^2),
\quad 0\le j\le b.
$$


Every contact inverse has its actual finite range $0\le i,j<b$.

Set


$$
N=X^TX>0,\qquad H=X^TY,\qquad
\alpha=v_2(N),\qquad \gamma=v_2(H).
$$


The supplied original-family mixed nonvanishing is retained; it is not inferred from the residue calculation.

Both columns are even on this domain. For an even $X_j$,


$$
(X_j+8z)^2-X_j^2=16zX_j+64z^2\in32\mathbb Z_2.
$$


Therefore $X\bmod8$, equivalently the complete raw representative $2X\bmod16$, suffices for $N\bmod32$.

### Complete lower lift retained

Use the accepted complete $P\bmod16$:


$$
\begin{aligned}
P(X)\equiv{}&
2+15\binom X1+7\binom X2+5\binom X3
+12\binom X5+4\binom X6+4\binom X7\\
&+8\binom X9+8\binom X{10}+8\binom X{11}
\pmod{16}.
\end{aligned}
\tag{6}
$$


Its actual finite solution and reconstruction are


$$
\theta=T(-2n)\mathcal S_bP\pmod{16},
\qquad
2X_j\equiv W_j(j\theta_{j-1}-\theta_j)\pmod{16},
\tag{7}
$$


with $\theta_{-1}=\theta_b=0$.

For completeness, the accompanying lower $Q$-lift still uses all seven exterior values


$$
(B_0^+,\ldots,B_6^+)
=(5,10,22,24,24,16,16)\pmod{32},
$$


and


$$
\eta_i\equiv
-\sum_{a=0}^6B_a^+\binom{-2n}{b+a-i}
+(T(-2n)\mathcal S_bQ)_i\pmod{32}.
$$


Its full endpoint is


$$
4Y_j\equiv
W_b\mathbf1_{j=b}+W_j(j\eta_{j-1}-\eta_j)\pmod{32}.
$$


No endpoint or factorial boundary is replaced in this calculation.

The accepted lift incorporates the complete normalized $P$-forcing and the finite inverse correction. The complete logarithmic force is absent at this precision only through the supplied whole-force bound


$$
v_2(h_i^F/b!)
\ge h+1-2\lfloor\log_2(2n+b-1)\rfloor-v_2(b!)>5.
$$


The norm argument does not introduce a new forcing cutoff.

---

## 2. Which coordinates can contribute to $N\bmod32$?

The previously audited lower lift gives


$$
8\mid X_j\quad(j\text{ odd}),
$$


and


$$
4\mid X_j\quad(j\text{ even and }64\nmid j).
$$


To compute the norm, the latter statement must be sharpened: a coordinate of depth exactly two contributes $16\bmod32$.

The needed refinement is


$$
\boxed{8\mid X_j\qquad(j\text{ even},\ 32\nmid j).}
\tag{8}
$$


I record its first-column justification so that the norm does not depend on deleting off-pair coordinates by a defect argument.

Put


$$
m=\frac{b-1}{4}=32D+20,\qquad
M=\frac{n+2}{4}=32C+17.
$$



### 2.1 Positions $j=4k+2$

Let $\ell=m-k$, and set


$$
\mathcal M_s=\binom{2n+b-1-j}{b-1-j-s},
\qquad
B=\mathcal M_0
=\binom{4(h+\ell)-2}{4\ell-2}.
$$


The retained finite moment reduction is


$$
j\theta_{j-1}-\theta_j\equiv(1-2k)B\pmod4,
\tag{9}
$$


and


$$
v_2(W_j)=1+v_2\binom{M-1}{k}.
\tag{10}
$$



If $v_2(W_j)=1$, Lucas forces


$$
k=32t\ \text{or}\ 32t+16,\qquad \binom Ct\text{ odd}.
$$


Hence $t$ is even, $d=D-t$ is odd, and


$$
\ell=32d+20\quad\text{or}\quad32d+4.
$$


Kummer gives $v_2(B)\ge3$: in the reduced binomial, the overlaps at low positions $0,1$ and at position $5$ supply three carries.

At these residues $j\equiv2\pmod{64}$, direct finite moment expansion of (6) modulo $8$ gives


$$
j\theta_{j-1}-\theta_j
\equiv-
\left(2\mathcal M_{-1}+\mathcal M_0
+2\mathcal M_2+4\mathcal M_3+4\mathcal M_4\right)
\pmod8.
\tag{11}
$$


The same low digits give


$$
v_2(\mathcal M_{-1}),v_2(\mathcal M_2)\ge3,\qquad
v_2(\mathcal M_3)\ge3,\qquad
v_2(\mathcal M_4)\ge2.
$$


Thus (11) vanishes modulo $8$.

If $v_2(W_j)=2$, the possible low residues of $k$ are $0,8,16\bmod32$. Then $\ell-1\equiv3\pmod4$, so $4\mid B$, and (9) suffices. If $v_2(W_j)=3$, $k$ is even, so $B$ is even. Larger weight valuations are immediate.

Therefore


$$
8\mid X_{4k+2}\qquad(0\le k<m).
\tag{12}
$$



### 2.2 Positions $j=4k$

Set


$$
B=\binom{4(h+m-k)}{4(m-k)},\qquad
w=v_2(W_{4k})=v_2\binom Mk.
$$


The retained reconstruction is


$$
4k\theta_{4k-1}-\theta_{4k}
\equiv-2(k+1)B\pmod8.
\tag{13}
$$



For $w=1$, the only even low residue that can survive in $X_{4k}/4$ is $k\equiv8\pmod{32}$. Odd $k$ are eliminated by the factors in $(k+1)B$.

For $w=2$, the other even low residues requiring attention are $k\equiv4,12\pmod{32}$. Their higher weight binomial is odd, forcing its higher index even. Since $D$ is odd, the resulting overlap at bit $5$ makes $B$ even. Thus these coordinates have depth at least three. Residues $k\equiv8,24\pmod{32}$ correspond to $32\mid j$, and are retained below.

For $w\ge3$, the reconstruction difference is even, which suffices.

Finally, when $w=0$ off the prescribed pairs,


$$
k=32t+1\quad\text{or}\quad32t+17,\qquad \binom Ct\text{ odd}.
$$


Here $t$ is even and $D-t$ is odd. In the finite moment expansion of (6) at $j\equiv4\pmod{64}$, all coefficients of $\mathcal M_s$, $-1\le s\le11$, are even. The low-digit carries give


$$
v_2(\mathcal M_s)\ge3\quad(s\ne4),\qquad
v_2(\mathcal M_4)\ge2.
$$


The coefficient of $\mathcal M_4$ is divisible by $8$. For its unshifted part this follows explicitly from


$$
35(4\cdot12+6\cdot4+4\cdot4)=35\cdot88;
$$


the reconstruction terms multiplied by $j$ have the same required divisibility. Thus the reconstruction difference vanishes modulo $16$.

This proves (8).

The actual endpoint satisfies the retained bounds


$$
X_b=\frac{W_b\,b\theta_{b-1}}2,\qquad
v_2(W_b)\ge6,\qquad v_2(X_b)\ge5.
$$


It contributes zero.

Consequently,


$$
\boxed{\text{Only coordinates }j\equiv0\pmod{32}\text{ can contribute to }N\bmod32.}
\tag{14}
$$



---

## 3. A complete $P$-convolution at every surviving coordinate

This is the additional formula needed to audit the units in the coordinator’s proposal.

Put


$$
e=2C+1,\qquad 2n=4+128e.
$$


For $32\mid j<b$, let


$$
L=b-1-j=16q.
$$


Because $b-1=128D+80$, every such $q$ is positive and odd.

### 3.1 Remove only bounded translations

The coefficients in (6) imply


$$
P(j+x)\equiv P(x)\pmod{16}\qquad(32\mid j).
$$


For example, the odd coefficients have degree at most three, where the binary translation losses are at most one bit; all higher coefficients carry the additional factors displayed in (6).

The exact finite moment identity therefore gives


$$
\theta_j\equiv
\sum_{s=0}^{11}p_s
\binom{2n+s-1}{s}
\binom{2n+L}{L-s}
\pmod{16}.
\tag{15}
$$


Since $v_2(2n-4)=7$, replacing the bounded factor


$$
\binom{2n+s-1}{s}
\quad\text{by}\quad
\binom{s+3}{3}
$$


is valid modulo $16$ for $s\le11$. The actual large binomial remains unchanged.

At this precision, the only nonzero products
$p_s\binom{s+3}{3}$ are


$$
2,\quad12,\quad6,\quad4
\qquad(s=0,1,2,3).
$$


Define


$$
J(L)=
2\binom{L+4}{4}
+12\binom{L+4}{5}
+6\binom{L+4}{6}
+4\binom{L+4}{7}\pmod{16}.
\tag{16}
$$



### 3.2 Evaluate the sampled polynomial and its actual convolution

Vandermonde gives, for every integer $s\ge0$,


$$
\binom{16s+4}{4}\equiv1+4s\pmod8,
$$


while


$$
16\mid\binom{16s+4}{5},\qquad
8\mid\binom{16s+4}{6},\qquad
4\mid\binom{16s+4}{7}.
$$


Hence


$$
\boxed{J(16s)\equiv2+8s\pmod{16}.}
\tag{17}
$$



The binary power congruence


$$
(1-z)^{-128e}\equiv(1-z^{16})^{-8e}\pmod{16}
$$


now yields the actual finite convolution


$$
\theta_j\equiv
\sum_{t=0}^{q}
\binom{8e+t-1}{t}\,[2+8(q-t)]
\pmod{16}.
\tag{18}
$$


There are no Laurent boundary terms in this first-column calculation.

Write


$$
T_q=\binom{8e+q}{q}.
$$


The unweighted sum in (18) is $T_q$. Modulo $2$, its kernel is supported only on multiples of $8$, so


$$
\sum_{t=0}^{q}(q-t)\binom{8e+t-1}{t}
\equiv qT_q\pmod2.
$$


Therefore


$$
\theta_j\equiv(2+8q)T_q\equiv10T_q\pmod{16},
\tag{19}
$$


because $q$ is odd.

The term $j\theta_{j-1}/2$ vanishes modulo $8$. Thus


$$
\boxed{
X_j\equiv-5W_j\binom{8e+q}{q}\pmod8,
\qquad
q=\frac{b-1-j}{16},
\quad32\mid j<b.
}
\tag{20}
$$



This formula supplies an odd unit multiplier and controls every valuation case through depth two. The earlier modulo-$4$ formula alone did not provide that control.

---

## 4. Audit of the paired squares, and evaluation of the residual squares

Define the actual positive integers


$$
E_t=\binom Ct\binom{2C+1+D-t}{D-t},
\qquad 0\le t\le D,
$$


and the finite count


$$
\mathcal C=\#\{\,0\le t\le D:v_2(E_t)=1\,\}.
\tag{21}
$$


Every $E_t$ is even on this domain.

### 4.1 Prescribed pairs

At


$$
j_0=128t,\qquad j_1=128t+64,
$$


put $d=D-t$. The two $q$-values in (20) are


$$
8d+5,\qquad8d+1.
$$


Kummer gives, exactly,


$$
v_2(W_{j_0})=v_2(W_{j_1})=v_2\binom Ct,
$$


and


$$
v_2\binom{8e+8d+5}{8d+5}
=
v_2\binom{8e+8d+1}{8d+1}
=
v_2\binom{e+d}{d}.
$$


Thus (20) proves the required truncated valuation agreement:

* If $v_2(E_t)=1$, both actual coordinates have depth one.
* If $v_2(E_t)=2$, both actual coordinates have depth two.
* If $v_2(E_t)\ge3$, both actual coordinates vanish modulo $8$.

An even number of depth one has square $4\bmod32$, independently of its odd unit. A number of depth two has square $16\bmod32$. Therefore


$$
\boxed{
\sum_{j\in\mathcal P}X_j^2
\equiv8\mathcal C\pmod{32},
\qquad
\mathcal P=\{128t,128t+64:0\le t\le D\}.
}
\tag{22}
$$


Equivalently,


$$
\sum_{j\in\mathcal P}X_j^2
\equiv2\sum_{t=0}^{D}E_t^2\pmod{32}.
$$



So the coordinator’s proposed paired expression is correct, but its justification requires (20), not just equality of the lower valuation pattern modulo $4$.

### 4.2 Residues $j=128t+32$

These coordinates have the complete range $0\le t\le D$. Here


$$
q=8(D-t)+3,
$$


and Kummer gives


$$
v_2(W_j)=1+v_2\binom Ct,
\qquad
v_2(T_q)=v_2\binom{e+D-t}{D-t}.
$$


Consequently $X_j$ has depth two precisely when $v_2(E_t)=1$, and otherwise has depth at least three. Thus


$$
\boxed{
\sum_{t=0}^{D}X_{128t+32}^{\,2}
\equiv16\mathcal C\pmod{32}.
}
\tag{23}
$$



These are real residual norm contributions. They cannot be discarded using the earlier defect argument.

### 4.3 Residues $j=128t+96$

The actual finite range is now


$$
0\le t\le D-1,
$$


not $0\le t\le D$. One has


$$
v_2(W_j)
=
2+v_2\!\left((C-t)\binom Ct\right).
$$


But


$$
(C-t)\binom Ct=C\binom{C-1}{t},
$$


and $C$ is even. Hence $v_2(W_j)\ge3$. Formula (20) makes all these coordinates zero modulo $8$, so


$$
\boxed{\sum_{t=0}^{D-1}X_{128t+96}^{\,2}\equiv0\pmod{32}.}
\tag{24}
$$



Combining all coordinate classes,


$$
\boxed{N\equiv24\mathcal C\pmod{32}.}
\tag{25}
$$



---

## 5. Evaluate the valuation-one count with all higher digits retained

It remains to evaluate $\mathcal C\bmod4$. This can be done exactly by separating the lowest two binary digits.

Write


$$
C=2c,\qquad c=2a+1,\qquad D=2d+1,
\qquad d=2v+\varepsilon,\quad\varepsilon\in\{0,1\}.
$$


These definitions agree with


$$
a=\frac{C-2}{4},\qquad v=\left\lfloor\frac D4\right\rfloor.
$$



### 5.1 Even indices $t=2s$

For $0\le s\le d$, binary scaling and an adjacent-binomial ratio give


$$
v_2(E_{2s})
=
1+
v_2\left[
\binom cs
\binom{2c+d-s+1}{d-s}
\right].
\tag{26}
$$


Thus $v_2(E_{2s})=1$ exactly when the bracket is odd.

Since $2c+1$ is odd, the second binomial can be odd only when $d-s$ is even. Write


$$
s=2i+\varepsilon,\qquad 0\le i\le v.
$$


Lucas/Kummer then give the two conditions


$$
\binom ai\text{ odd},\qquad
\binom{2a+1+v-i}{v-i}\text{ odd}.
\tag{27}
$$



### 5.2 Odd indices $t=2s+1$

Similarly,


$$
v_2(E_{2s+1})
=
1+
v_2\left[
(c-s)\binom cs
\binom{2c+d-s}{d-s}
\right].
\tag{28}
$$


Because $c$ is odd and


$$
(c-s)\binom cs=c\binom{c-1}{s},
$$


the bracket is odd precisely when


$$
\binom{c-1}{s}
\binom{2c+d-s}{d-s}
$$


is odd.

Now $c-1=2a$, so $s=2i$, with $0\le i\le v$. Reducing the other parity condition gives exactly (27), independently of $\varepsilon$.

Therefore the two counts are equal as **ordinary finite integer counts**, not merely modulo $2$:


$$
\boxed{\mathcal C=2\mathcal T,}
\tag{29}
$$


where


$$
\mathcal T=
\#\left\{
0\le i\le v:
\binom ai\text{ odd and }
\binom{2a+1+v-i}{v-i}\text{ odd}
\right\}.
\tag{30}
$$



In particular, the residual sum (23) is zero modulo $32$ after its actual evaluation, since $\mathcal C$ is even. It was not zero coordinatewise.

### 5.3 The remaining parity convolution

Modulo $2$, the indicator count (30) is


$$
\begin{aligned}
\mathcal T
&\equiv
\sum_{i=0}^{v}
\binom ai\binom{2a+1+v-i}{v-i}\\
&=[z^v](1+z)^a(1-z)^{-2a-2}\\
&\equiv[z^v](1+z)^{-a-2}\\
&=\binom{a+v+1}{v}\pmod2.
\end{aligned}
\tag{31}
$$


This is an evaluated finite-binomial convolution, with its actual upper endpoint $v$. No higher digit has been truncated.

Finally, (25) and (29) give


$$
N\equiv48\mathcal T\equiv16\mathcal T\pmod{32}.
$$


Together with (31), this proves (1)–(2). Kummer gives the equivalent carry test (3).

---

## 6. Original-domain subclasses and what is—and is not—claimed about them

Write $D=4v+\delta$, with $\delta=1$ or $3$. Then


$$
a+1=
\begin{cases}
4002v+1634,&\delta=1,\\
4002v+3635,&\delta=3.
\end{cases}
\tag{32}
$$


Thus (3) is a fully explicit test on the original integer $D=(9^r-81)/128$.

### An infinite original common-zero subclass

For $r=18+32u$,


$$
9^{18}\equiv721\pmod{1024},
\qquad
9^{32}\equiv257\pmod{1024}.
$$


Consequently


$$
9^{18+32u}\equiv721+256u\pmod{1024},
$$


and hence


$$
\boxed{D\equiv5+2u\pmod8.}
\tag{33}
$$



If $u\equiv1\pmod4$, equivalently $r\equiv50\pmod{128}$, then


$$
D\equiv7\pmod8.
$$


In this case $\delta=3$, $v$ is odd, and (32) shows that $a+1$ is odd. The bit-zero overlap forces


$$
v\mathbin{\&}(a+1)\ne0.
$$


Therefore $N/16=0\bmod2$, proving (4).

Every exponent $r=50+128w$, $w\ge0$, is an allowed original exponent and belongs to this common-zero subclass. No existence claim about an independently chosen $C,D$ is being substituted for that statement.

For the remaining original exponents, (3) is the exact criterion. I do **not** assert that the norm-nonzero branch is populated merely because analogous freely chosen integer parameters satisfy its carry test.

Using the retained fourth-discrepancy result,


$$
H\equiv N\pmod{32},
$$


the complete alternatives are now


$$
\boxed{
v\mathbin{\&}(a+1)=0
\quad\Longrightarrow\quad
\alpha=\gamma=4,
}
\tag{34}
$$


and


$$
\boxed{
v\mathbin{\&}(a+1)\ne0
\quad\Longrightarrow\quad
\alpha,\gamma\ge5.
}
\tag{35}
$$


The norm derivation itself does not depend on that separate discrepancy proof or its pending audit.

---

## 7. The first genuine residuals, and the precision required for a fifth discrepancy

On the common-zero locus (35), the next genuine quantities are


$$
\boxed{\frac N{32}\pmod2,\qquad
\frac{H-N}{32}\pmod2.}
\tag{36}
$$


Neither is evaluated by the fourth-digit formula.

There is an important difference in their precision requirements.

* To determine $N\bmod64$, $X\bmod16$ suffices. Thus the already supplied raw $2X\bmod32$ can support the next norm calculation.
* To determine $H-N\bmod64$ using only the established common evenness, one needs $X,Y\bmod32$, hence raw
  

$$
\boxed{2X\bmod64,\qquad4Y\bmod128.}
  \tag{37}
$$



Indeed, replacing $X,Y$ by $X+16a,Y+16c$ changes the defect by


$$
16a^T(Y-2X)+16X^Tc+256(a^Tc-a^Ta),
$$


which is necessarily divisible by $32$, but not necessarily by $64$. Thus the previous raw $32/64$ lift cannot simply be reused for the fifth discrepancy.

### A bounded follow-on lemma: the next contact congruence

There is a genuine contact change at the required $Q$-precision. In the integral divided-power ring, let


$$
\phi^2=1+2U,\qquad h=1+32e,\quad e\text{ odd}.
$$


Every coefficient of $U^2$ is even: cross terms have a factor $2$, and each square term has the even central binomial multiplier $\binom{2j}{j}$.

Expanding $(1+2U)^h$, the terms of degree at least two in $U$ vanish modulo $128$. For the quadratic term, its scalar has depth six and $U^2$ supplies the seventh bit; the remaining terms have sufficient scalar or divided-power divisibility. Therefore


$$
\boxed{\phi^{2h}\equiv1+2hU\equiv1+66U\pmod{128}.}
\tag{38}
$$


So the contact correction $64U$ must be retained at the fifth $Q$-precision.

The factorial cutoff itself does not yet enlarge: $v_2((b+7)!/b!)=7$, so the tails beginning at $b+7$ vanish modulo $128$. The same seven boundary values must nevertheless be recomputed at that precision, and the normalized $P$-forcing modulo $64$ must be derived separately. Formula (38) does not determine that forcing.

This is a bounded next-lift lemma, not a fifth-discrepancy evaluation.

---

## 8. Final gcd, actual primitive denominator, and whole evaluated error

No column normalization or metric has changed. The actual center is


$$
c_n=\frac{2b!}{\lambda R}\frac HN.
$$



Let $d_B$ be the least common denominator of the actual two-column lift and put


$$
N_B=d_B[u,v].
$$


With the specified falling-factorial metric, retain


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
p_n=\frac{H_B}{g_B},\qquad
q_n=\frac{A_B}{g_B}>0.
$$


Thus $1/g_B$ is the final primitive normalization of the integer coefficient pair, and $q_n$—not a row-clearer, contact determinant, or $d_B$—is the actual reduced denominator and multiplier of $S=e+\pi$.

For $s=s_2(n)$, the exact binary interface remains


$$
v_2(g_B)=
\min\left\{
3n-2s+2+\alpha,\,
\frac{3n}{2}-s+v_2(b!)+3+\gamma
\right\},
$$




$$
\boxed{
v_2(q_n)=
\max\left\{
0,\frac{3n}{2}-v_2(b!)-s-1-(\gamma-\alpha)
\right\}.
}
\tag{39}
$$



On the branch (34), $\gamma-\alpha=0$. On the common-zero branch, including every $r=50+128w$, the new lower bounds cannot be subtracted to control that difference.

The retained whole signed-error theorem gives, eventually,


$$
\epsilon_n=c_n-(e+\pi)<0,
$$




$$
\log|\epsilon_n|
=-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$


The complete primitive evaluated form remains


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n>0}
$$


eventually, and is nonzero. This is the whole real error, retaining the complete exponential residual, logarithmic forcing, finite boundary, endpoint, actual columns, and actual falling metric.

No proof or disproof of irrationality of $e+\pi$ follows.

---

# Concluding ledger

## (1) New result and proof status

**Proved from the accepted complete $P\bmod16$ lift, on every original exponent $r=18+32u$:**


$$
\boxed{
\frac N{16}\equiv
\binom{(C-2)/4+\lfloor D/4\rfloor+1}{\lfloor D/4\rfloor}
\pmod2.
}
$$



The proof includes:

- a complete first-column convolution at every $32$-divisible coordinate;
- the unit-sensitive audit of all paired valuation cases;
- the residual $j\equiv32\pmod{64}$ squares, with their correct finite boundaries;
- an exact doubling identity for the valuation-one count;
- evaluation of its remaining higher-digit convolution;
- an infinite **original-exponent** common-zero subclass $r=50+128w$.

Also proved is the bounded next-contact identity (38). No finite growing-index calculation is used as an infinite proof.

## (2) Exact remaining bottleneck

On the explicit carry-zero locus,


$$
\lfloor D/4\rfloor\mathbin{\&}\bigl((C+2)/4\bigr)\ne0,
$$


the first residuals are $N/32\bmod2$ and $(H-N)/32\bmod2$. The latter requires a complete raw $64/128$ lift unless additional precision-saving identities are proved.

Beyond these digits, the substantive arithmetic bottleneck remains a justified all-depth estimate on $\gamma-\alpha$, or another sufficient bound on the actual primitive denominator after the final gcd. The present exact fourth-digit classification does not supply such an estimate.

## (3) Computation request

**None is required for the result above.** The supplied $P\bmod16$ certificate suffices; the new sampled identity, finite convolutions, carry classification, and original-exponent subclass have explicit derivations.
