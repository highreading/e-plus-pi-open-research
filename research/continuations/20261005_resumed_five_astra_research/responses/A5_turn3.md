> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5 — Complete modulus-$128$ joint reduction with all floor cases retained

## Executive conclusion

I reuse the coordinator’s completed contact calculation, including the full residuals, all eight finite contact matrices on $209$ rows, the exterior checks, and the lower-precision checks. **None of those calculations is requested again.**

The new result of this report is a complete, division-safe reduction of the joint problem to:

1. one actual higher-binomial kernel
   

$$
\mathcal B_t=\binom Ct\binom{k+D-t-1}{D-t},
   \qquad k=2C+1;
$$


2. six elementary floor-case factors;
3. two explicitly defined finite low-state coefficient functions, one for the norm and one for the mixed defect;
4. a separate terminal coefficient function for the shortened final block.

The reduction includes **all $128$ residues**, every weight-depth-four coordinate, the negative moments $-10,\ldots,-1$, both original $t$-ranges, and the actual exterior $+1$.

**I do not obtain an evaluated new carry in this report.** In particular, I do not claim


$$
H-N\equiv0\pmod{128}.
$$


What I supply is an explicit finite coefficient test which, if it passes, would prove that congruence without evaluating an unbounded higher-binomial convolution. If that stronger coefficient test fails, the formulas below identify exactly the remaining convolution; an abstract low-state failure would not itself disprove original-family alignment.

Thus the completed contact certificate is advanced to a complete joint reduction, but not to a proved new modulus-$128$ alignment.

---

## 1. Accepted inputs and exact scope

The original family is unchanged:


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0,
$$


with


$$
b=128D+81,\qquad n=128C+66,\qquad C=4002D+2532.
$$


In particular,


$$
D\text{ is odd},\qquad C\equiv2\pmod4.
$$



Keep


$$
X=\frac{Z_w}{2R},\qquad Y=\frac{V_w}{4b!},\qquad
N=X^TX>0,\qquad H=X^TY,
$$


and


$$
W_j=\binom{n+2}{j},\qquad
\Omega=\operatorname{diag}\bigl((n+2)_{\underline j}^{\,2}\bigr)_{0\le j\le b}.
$$


Every actual contact inverse has range $0\le i,j<b$.

I reuse the accepted results


$$
X,Y\in2\mathbb Z_2^{b+1},
\qquad H-N\in64\mathbb Z_2,
$$


and the original-family mixed nonvanishing which makes $v_2(H)$ finite.

The methods below are classical finite Newton summation, factorial stripping, and prime-power binomial arithmetic. No exhaustive novelty or archival claim is made.

### 1.1 Completed coefficient data

Suppressing the certified zero tail after degree $15$, the coordinator’s vectors are


$$
\begin{aligned}
p={}&(34,31,71,69,48,12,4,4,96,72,120,72,0,64,64,64)
          \pmod{128},\\
q={}&(180,164,152,6,112,48,192,8,32,160,64,240,0,0,0,128)
          \pmod{256}.
\end{aligned}
$$


Their difference is


$$
\delta=q-2p
=(112,102,10,124,16,24,184,0,96,16,80,96,0,128,128,0)
\pmod{256}.
$$



The complete exterior vectors are


$$
B=(197,234,54,56,248,208,112,128,128)\pmod{256},
$$




$$
\beta=(113,202,78,200,248,80,240,128,128)\pmod{256}.
$$



The actual degree is therefore at most $15$, within the previously proved safe bound $27$. The certificate establishes these finite coefficients; their original-family use also relies on the supplied coefficient-valued transfer proof. It does not make the actual high kernels periodic.

---

## 2. Correctly normalized factors from the actual $T(-2n)$

Set


$$
A=2n=128k+4,\qquad k=2C+1.
$$


The number $k$ is odd.

For $0\le s\le15$, define the **actual bounded binomial multiplier**


$$
a_s(A)=\binom{A+s-1}{s}.
$$


Do not replace it by $\binom{s+3}{3}$ without a new weighted congruence proof.

Define


$$
F_s(x;A)=a_s(A)\sum_{r=s}^{15}p_r\binom{x}{r-s},
$$




$$
G_s(x;A)=a_s(A)\sum_{r=s}^{15}\delta_r\binom{x}{r-s}.
$$


Extend $F_s=0$ outside $0\le s\le15$. Put


$$
Z_{-i}(x;A)=\beta_i\quad(1\le i\le9),\qquad
Z_s(x;A)=G_s(x;A)\quad(0\le s\le15),
$$


with zero extension elsewhere.

The reconstructed coefficients are


$$
U_s(x;A)=F_s(x;A)+xF_s(x-1;A)+xF_{s+1}(x-1;A),
\tag{2.1}
$$




$$
V_s(x;A)=Z_s(x;A)+xZ_s(x-1;A)+xZ_{s+1}(x-1;A).
\tag{2.2}
$$


Their ranges are


$$
-1\le s\le15\quad\text{for }U,\qquad
-10\le s\le15\quad\text{for }V.
$$



### 2.1 Derivation from the finite inverse

For an interior index $j$, write $L=b-1-j$. The exact finite identity


$$
\sum_{v=0}^{L}
\binom{A+v-1}{v}\binom{v}{s}
=
\binom{A+s-1}{s}\binom{A+L}{L-s}
\tag{2.3}
$$


follows by extracting $\binom{A+s-1}{s}$ and applying the hockey-stick identity.

Expanding


$$
\binom{j+v}{r}=\sum_{s=0}^{r}\binom{j}{r-s}\binom{v}{s}
$$


in the actual finite $T(-A)$ reconstruction yields the $F_s,G_s$ above. Thus these are not low-residue factors inferred from an old norm formula.

Put


$$
\mathcal M_s(j)=\binom{A+b-1-j}{b-1-j-s}.
$$


The identity


$$
\mathcal M_s(j-1)=\mathcal M_s(j)+\mathcal M_{s-1}(j)
$$


then gives (2.1)–(2.2).

Consequently, for $0\le j<b$,


$$
2X_j\equiv(-1)^{j+1}W_j\mathcal F_j\pmod{128},
\tag{2.4}
$$




$$
4(Y_j-X_j)\equiv(-1)^{j+1}W_j\mathcal G_j\pmod{256},
\tag{2.5}
$$


where


$$
\mathcal F_j=\sum_{s=-1}^{15}U_s(j;A)\mathcal M_s(j),
\qquad
\mathcal G_j=\sum_{s=-10}^{15}V_s(j;A)\mathcal M_s(j).
\tag{2.6}
$$



### 2.2 Complete negative part

In particular,


$$
\begin{array}{c|l}
s&V_s(x;A)\pmod{256}\\ \hline
-10&128x\\
-9&128\\
-8&128+112x\\
-7&240+64x\\
-6&80+72x\\
-5&248+192x\\
-4&200+22x\\
-3&78+24x\\
-2&202+59x\\
-1&113+113x+xG_0(x-1;A).
\end{array}
\tag{2.7}
$$


None of these terms is removed before the new scalar contraction.

The entire logarithmic force is absent only by its retained whole-force estimate. The exponential tail is absent only after the complete cutoff at exterior index $9$. These are not selected-term omissions.

---

## 3. Scalar precision: what the complete lifted columns determine

For the chosen coefficient representatives, (2.4)–(2.5) imply


$$
4X_j^2\equiv W_j^2\mathcal F_j^2\pmod{1024},
\tag{3.1}
$$




$$
8X_j(Y_j-X_j)\equiv W_j^2\mathcal F_j\mathcal G_j
\pmod{1024}.
\tag{3.2}
$$



Here the precision is sufficient despite using only $P\bmod128$ and $Q\bmod256$. Indeed,


$$
W_j\mathcal F_j\equiv2X_j\in4\mathbb Z_2,
\qquad
W_j\mathcal G_j\equiv4(Y_j-X_j)\in8\mathbb Z_2.
$$


Changing the first reconstructed raw column by $128a$ changes its square by a multiple of $1024$, and changes the raw mixed product by a multiple of $1024$. Changing the second raw column by $256b$ also changes that product by a multiple of $1024$.

Therefore the present data determine


$$
\boxed{N\bmod256,\qquad H-N\bmod128,\qquad H\bmod128.}
$$


They do **not** determine $H\bmod256$.

---

## 4. All original coordinate ranges

Write


$$
j=128t+\rho,\qquad 0\le\rho<128,\qquad d=D-t,\qquad K=k+d.
$$


Then


$$
\mathcal M_s(j)
=
\binom{128K+84-\rho}{128d+80-\rho-s}.
\tag{4.1}
$$



The exact interior ranges are


$$
\begin{cases}
0\le t\le D,&0\le\rho\le80,\\
0\le t\le D-1,&81\le\rho\le127.
\end{cases}
\tag{4.2}
$$


The point $j=b=128D+81$ is separate.

Equivalently, there are full blocks $0\le t<D$, followed by the partial block $t=D,\ 0\le\rho\le80$. This terminal distinction will remain explicit.

---

## 5. Six floor cases: a small division-safe basis

Define


$$
a_0=\left\lfloor\frac{84-\rho}{128}\right\rfloor,\qquad
\ell_0=\left\lfloor\frac{80-\rho-s}{128}\right\rfloor,\qquad
c_0=\left\lfloor\frac{4+s}{128}\right\rfloor,
$$


and remainders


$$
a=84-\rho-128a_0,\quad
\ell=80-\rho-s-128\ell_0,\quad
c=4+s-128c_0.
$$


For the complete range $-10\le s\le15$,


$$
a_0,\ell_0,c_0\in\{-1,0\}.
$$



Because the low arguments satisfy $a\equiv\ell+c\pmod{128}$,


$$
a_0-\ell_0-c_0\in\{0,1\}.
$$


Thus exactly the following six patterns are possible:



$$
\begin{array}{c|c|c}
(a_0,\ell_0,c_0)&
\dfrac{(K+a_0)!}{(d+\ell_0)!(k+c_0)!}
&
\text{factor relative to }J_d/k\\ \hline
(0,0,0)&KJ_d/k&K\\
(0,-1,0)&KdJ_d/k&Kd\\
(0,0,-1)&KJ_d&Kk\\
(-1,-1,0)&dJ_d/k&d\\
(-1,0,-1)&J_d&k\\
(-1,-1,-1)&dJ_d&dk
\end{array}
\tag{5.1}
$$


where


$$
\boxed{J_d=\binom{K-1}{d}.}
$$



This is the required small basis. Only the odd number $k$ is inverted.

In particular, the genuinely new case


$$
\rho=85,\quad s=-10
$$


has pattern $(-1,0,-1)$, and its high quotient is $J_d$, not
$\binom{K-1}{d-1}$.

Another new issue occurs when $\rho\le84$ but $80-\rho-s<0$: then the upper block has not overflowed while the lower block has. Its factor is $Kd$, not $K$.

### 5.1 Negative actual lower arguments

If $d=0$ and $\ell_0=-1$, the actual lower argument in (4.1) is negative, so the moment is zero.

The corresponding factors in (5.1) all contain $d$. Thus the polynomial basis has the correct zero continuation at this boundary. This is a justification of the continuation, not permission to form a negative factorial.

---

## 6. Exact factorial stripping and normalized low factors

Define


$$
O(m)=\prod_{\substack{1\le v\le m\\v\ \mathrm{odd}}}v,
\qquad
L_7(m)=\prod_{i=0}^{6}O\!\left(\left\lfloor\frac m{2^i}\right\rfloor\right).
$$


For nonnegative $m$,


$$
m!=2^{\sum_{i=1}^{7}\lfloor m/2^i\rfloor}
\left\lfloor\frac m{128}\right\rfloor!L_7(m).
\tag{6.1}
$$



For each valid moment, put


$$
m_{\rho s}
=
127(a_0-\ell_0-c_0)
+v_2(a!)-v_2(\ell!)-v_2(c!),
\tag{6.2}
$$


and


$$
u_{\rho s}
=
\frac{L_7(128K+84-\rho)}
{L_7(128d+80-\rho-s)L_7(128k+4+s)}.
\tag{6.3}
$$


This is an odd rational unit.

Let $P_{\rho s}(K,d,k)$ be the corresponding factor in the last column of (5.1). Then


$$
\boxed{
\mathcal M_s(128t+\rho)
=
\frac{J_d}{k}\,
P_{\rho s}(K,d,k)\,
2^{m_{\rho s}}u_{\rho s}.
}
\tag{6.4}
$$



The exponent $m_{\rho s}$ is nonnegative. It counts the carries internal to the low seven-bit block, excluding the carry already represented in the high factorial quotient.

Define the complete normalized factors


$$
f_{\rho,t}
=
\sum_{s=-1}^{15}
U_s(128t+\rho;A)\,
P_{\rho s}(K,d,k)\,
2^{m_{\rho s}}u_{\rho s},
\tag{6.5}
$$




$$
g_{\rho,t}
=
\sum_{s=-10}^{15}
V_s(128t+\rho;A)\,
P_{\rho s}(K,d,k)\,
2^{m_{\rho s}}u_{\rho s}.
\tag{6.6}
$$


Then


$$
\mathcal F_{128t+\rho}=\frac{J_d}{k}f_{\rho,t},
\qquad
\mathcal G_{128t+\rho}=\frac{J_d}{k}g_{\rho,t}.
\tag{6.7}
$$



These formulas preserve the entire negative range and all new overflow cases. They do not rely on the old $31$-class support.

---

## 7. Every weight, including depth four

Let


$$
\varepsilon_\rho=
\begin{cases}
0,&\rho\le68,\\
1,&\rho\ge69,
\end{cases}
\qquad
z_\rho=68-\rho+128\varepsilon_\rho,
$$


and put


$$
b_\rho=
127\varepsilon_\rho+
v_2(68!)-v_2(\rho!)-v_2(z_\rho!).
\tag{7.1}
$$


Define


$$
w_{\rho,t}
=
\frac{L_7(128C+68)}
{L_7(128t+\rho)L_7(128(C-t)+68-\rho)}.
\tag{7.2}
$$


Exact stripping gives


$$
\boxed{
W_{128t+\rho}
=
2^{b_\rho}w_{\rho,t}
\binom Ct(C-t)^{\varepsilon_\rho}.
}
\tag{7.3}
$$



Consequently the exact weight depth is


$$
v_2(W_{128t+\rho})=
\begin{cases}
b_\rho+v_2\binom Ct,&\rho\le68,\\[2mm]
b_\rho+v_2\!\left((C-t)\binom Ct\right),&\rho\ge69.
\end{cases}
\tag{7.4}
$$



Formula (7.4) is an exhaustive classification rule for all $128$ residues. In particular, **every coordinate with actual weight depth four remains included**.

The accepted sufficient exclusion


$$
v_2(W_j)\ge5
\Longrightarrow X_j^2\equiv X_jY_j\equiv0\pmod{256}
$$


may be applied after this classification. It is not necessary to apply it in the universal coefficient calculation: retaining all residues is safer and still bounded.

---

## 8. Complete joint contraction on one high kernel

Define


$$
\boxed{\mathcal B_t=\binom CtJ_{D-t}.}
\tag{8.1}
$$


This retains the actual $C,D,t$, hence the actual $n,b$.

Using (6.7) and (7.3), define low coefficients


$$
\mathcal A_{\rho}(D,t)
=
2^{2b_\rho}w_{\rho,t}^{\,2}
(C-t)^{2\varepsilon_\rho}k^{-2}f_{\rho,t}^{\,2},
\tag{8.2}
$$




$$
\mathcal D_{\rho}(D,t)
=
2^{2b_\rho}w_{\rho,t}^{\,2}
(C-t)^{2\varepsilon_\rho}k^{-2}f_{\rho,t}g_{\rho,t}.
\tag{8.3}
$$


All inversions are of odd elements.

Then


$$
W_{128t+\rho}^2\mathcal F_{128t+\rho}^2
=\mathcal B_t^2\mathcal A_\rho(D,t),
\tag{8.4}
$$




$$
W_{128t+\rho}^2\mathcal F_{128t+\rho}\mathcal G_{128t+\rho}
=\mathcal B_t^2\mathcal D_\rho(D,t).
\tag{8.5}
$$



Set


$$
\mathcal A_{\rm full}=\sum_{\rho=0}^{127}\mathcal A_\rho,
\qquad
\mathcal D_{\rm full}=\sum_{\rho=0}^{127}\mathcal D_\rho,
\tag{8.6}
$$


and retain separate terminal functions


$$
\mathcal A_{\rm end}(D)=\sum_{\rho=0}^{80}\mathcal A_\rho(D,D),
$$




$$
\mathcal D_{\rm end}(D)=\sum_{\rho=0}^{80}\mathcal D_\rho(D,D).
\tag{8.7}
$$



The complete reductions are therefore


$$
\boxed{
4N\equiv
\sum_{t=0}^{D-1}\mathcal B_t^2\mathcal A_{\rm full}(D,t)
+\mathcal B_D^2\mathcal A_{\rm end}(D)
\pmod{1024},
}
\tag{8.8}
$$




$$
\boxed{
8(H-N)\equiv
\sum_{t=0}^{D-1}\mathcal B_t^2\mathcal D_{\rm full}(D,t)
+\mathcal B_D^2\mathcal D_{\rm end}(D)
\pmod{1024}.
}
\tag{8.9}
$$



Dividing the **whole** right side of (8.8) by $4$ determines $N\bmod256$. Dividing the whole right side of (8.9) by $8$ determines $H-N\bmod128$. Individual residue or block coefficients need not admit those divisions.

This is a complete joint reduction, not an evaluated carry.

---

## 9. The actual exterior endpoint

The endpoint remains


$$
X_b=\frac{W_b\,b\theta_{b-1}}2,\qquad
Y_b=\frac{W_b(1+b\eta_{b-1})}{4}.
\tag{9.1}
$$


The exterior $+1$ has been retained.

The accepted bounds


$$
v_2(X_b)\ge5,\qquad v_2(Y_b)\ge4
$$


imply


$$
4X_b^2\in2^{12}\mathbb Z_2,
\qquad
8X_b(Y_b-X_b)\in2^{12}\mathbb Z_2.
$$


Thus the endpoint contributes zero to (8.8)–(8.9), after its actual formula has been included.

---

## 10. A proved finite low-state modulus

The coefficient functions in (8.2)–(8.7), modulo $1024$, have a finite description.

For $p\ge3$, the product of all odd residues modulo $2^p$ is $1$, so


$$
O(m+2^p)\equiv O(m)\pmod{2^p}.
$$


Hence


$$
L_7(m+2^{p+6})\equiv L_7(m)\pmod{2^p}.
\tag{10.1}
$$


At $p=10$, a value $L_7(128q+a)\bmod1024$ depends only on


$$
q\bmod512,\qquad a.
$$



The remaining ingredients also have this sufficient period:

* $K,d,k,C-t\bmod1024$ are controlled by $D,t\bmod512$ on the fixed affine relation. For example, changing $D$ by $512$ changes $C$ by $4002\cdot512$, divisible by $1024$.
* Changing $t$ by $512$ changes $j$ by $2^{16}$. The binomial translation loss for the degree-$\le16$ coefficient polynomials is at most $4$, still leaving more than ten bits.
* Changing $D$ by $512$ changes $A$ by a multiple of $2^{18}$. For the bounded factors with lower index at most $15$, the loss is at most $3$.

Therefore


$$
\boxed{
\mathcal A_{\rm full}(D,t),\ \mathcal D_{\rm full}(D,t)\pmod{1024}
\text{ depend only on }D,t\bmod512.
}
\tag{10.2}
$$


The terminal functions depend only on $D\bmod512$.

This statement concerns the **low coefficient functions only**. The high kernel $\mathcal B_t$ in (8.8)–(8.9) has not been made periodic.

### Boundary implementation

For low-state evaluation, use nonnegative representatives with sufficiently large $D,t,d$, preserving $D,t\bmod512$, for the full-block functions. For the terminal function set $t=D,d=0$ explicitly. Terms with negative actual lower argument are zero; equivalently their basis factor contains $d=0$.

One must not evaluate a factorial at a negative argument and then appeal to periodicity.

---

## 11. The independent finite identity that would settle alignment

The following is now a fully specified sufficient lemma.

> **Universal low-coefficient alignment lemma.**
> For every odd $D\bmod512$ and every $t\bmod512$,
> 

$$
> \mathcal D_{\rm full}(D,t)\equiv0\pmod{1024},
> \tag{11.1}
>
$$


> and for every odd $D\bmod512$,
> 

$$
> \mathcal D_{\rm end}(D)\equiv0\pmod{1024}.
> \tag{11.2}
>
$$



### Why this would prove the original-family theorem

If (11.1)–(11.2) hold, every summand on the right side of (8.9) vanishes modulo $1024$, regardless of the actual high kernel. Therefore


$$
8(H-N)\equiv0\pmod{1024},
$$


hence


$$
H-N\equiv0\pmod{128}.
$$



This derivation requires no high-$t$ truncation, no binomial-kernel substitution, no old support shortcut, and no division by an even high parameter.

### What a failed identity would mean

A nonzero coefficient in (11.1) does **not** establish an original-family counterexample. It leaves three possibilities:

1. the actual $\mathcal B_t^2$ always annihilates that coefficient at the relevant reachable indices;
2. different $t$-terms cancel;
3. the new alignment fails.

These are distinguished only by the complete weighted sum (8.9). The proposed universal identity is sufficient, not asserted necessary.

I have not evaluated (11.1)–(11.2), and therefore do not label them as true identities.

---

## 12. Norm residues and the unresolved carry

The same finite calculation should output $\mathcal A_{\rm full}$ and $\mathcal A_{\rm end}$, not merely the mixed defect.

At present the exact norm reduction is (8.8). Without its coefficient evaluation or a high-kernel contraction, the new norm digit is not assigned.

At the retained scope of the old norm formula


$$
N\equiv48T+32\chi\pmod{64},
$$


one obtains the necessary parent-domain restriction


$$
N\bmod128\in\{0,16,32,48,64,80,96,112\}.
\tag{12.1}
$$


This is a containing set, not a claim that all eight residues occur.

On


$$
\mathcal Z_{64}=\{u:N\equiv0\pmod{64}\},
$$


the possibilities are


$$
N\bmod128\in\{0,64\}.
\tag{12.2}
$$


Because the accepted alignment is only modulo $64$, before the new carry is evaluated the joint possibilities there are


$$
(N,H)\bmod128\in
\{(0,0),(0,64),(64,0),(64,64)\}.
\tag{12.3}
$$



The calculation in §§8–11 is precisely what must determine whether the off-diagonal possibilities disappear.

---

## 13. Abstract low states versus original-family reachability

The supplied reachability proof establishes that


$$
D(u)=\frac{9^{18+32u}-81}{128}
$$


reaches every odd residue modulo every fixed power of two, infinitely often.

Thus every odd $D\bmod512$ in the proposed coefficient calculation is relevant to the original family. Moreover, for sufficiently large original $D$, its interval $0\le t<D$ contains representatives of every $t\bmod512$.

However, this does not make the high kernel arbitrary. The values


$$
\binom Ct,\qquad J_{D-t}
$$


retain their actual higher carry structure and normalized units.

Accordingly:

* a universal low-coefficient identity transfers immediately to the original family;
* a table of low coefficients does not evaluate the high-kernel sum unless an identity removes that dependence;
* an auxiliary full sum at a small $D$ does not transfer merely because that $D$-residue is reachable;
* a nonzero abstract coefficient is not a reachable nonzero complete carry.

This is the exact local-to-global distinction required at this stage.

---

## 14. Bounded exact arithmetic now appropriate

This is a **new joint coefficient calculation**, not a repetition of the completed contact calculation.

### Inputs

1. The $16$-entry vectors $p,\delta$ in §1.
2. The nine entries of $\beta$.
3. Equations (2.1)–(2.2), with the actual bounded multiplier
   

$$
\binom{128k+3+s}{s}.
$$


4. All residues $0\le\rho<128$.
5. All moments $-10\le s\le15$, with the first-column range beginning at $-1$.
6. The six floor factors in (5.1).
7. The stripping exponents and odd-unit quotients in §§6–7.
8. All odd $D\bmod512$, all $t\bmod512$, and the affine relation
   

$$
C=4002D+2532,\qquad k=2C+1.
$$


9. Separate terminal evaluation at $t=D,d=0$.

### Required arithmetic

All calculations may be performed modulo $1024$, except for extracting the explicitly bounded factorial valuations and computing exact small binomials.

Only odd denominators are inverted. In particular:

* do not invert $K$, $d$, or $C-t$;
* do not use $\binom{K-1}{d-1}$ as a universal high kernel;
* do not divide partial contractions by $4$ or $8$;
* do not drop weight-depth-four coordinates.

A table of $L_7(m)\bmod1024$ for $0\le m<2^{16}$ suffices.

### Expected verifiable output

For each of


$$
256\cdot512=131{,}072
$$


full low states, output the pair


$$
\bigl(\mathcal A_{\rm full}(D,t),\mathcal D_{\rm full}(D,t)\bigr)
\pmod{1024}.
$$


For the $256$ terminal states, output


$$
\bigl(\mathcal A_{\rm end}(D),\mathcal D_{\rm end}(D)\bigr)
\pmod{1024}.
$$



The decisive mixed assertion to test is (11.1)–(11.2). Its expected certificate format is:

* either an all-zero mixed coefficient vector, proving the universal lemma;
* or the complete exceptional-state list with the nonzero residues.

**An all-zero result is a target to test, not an asserted prediction.**

For the norm, output its residue image and any observed compact coefficient formula. An observed formula must then be checked over this entire proved finite state space before being used universally.

A straightforward implementation has roughly $16.8$ million residue-state rows before the bounded moment contractions. That is a bounded modular computation, but not a tiny one. Streaming the two block sums avoids storing all residue rows; coefficient-depth pruning can reduce the work, provided every omitted term receives an explicit valuation certificate.

No enormous original $b$, original factorial, or growing high-$t$ convolution is required for this coefficient test.

---

## 15. Consequences for valuations and the primitive denominator

Let


$$
\alpha=v_2(N),\qquad\gamma=v_2(H).
$$



If the new alignment is proved, then at every index with


$$
N\not\equiv0\pmod{128}
$$


one has


$$
\alpha=\gamma.
$$


In particular, on a proved original subfamily with


$$
N\equiv64\pmod{128},
$$


it would give


$$
\boxed{\alpha=\gamma=6.}
$$


If instead


$$
N\equiv H\equiv0\pmod{128},
$$


it gives only


$$
\alpha,\gamma\ge7,
$$


not a bound on $\gamma-\alpha$.

No such new conclusion is asserted before the carry is evaluated.

### 15.1 Full gcd and actual primitive pair

Retain the least actual clearer $d_B$, and set


$$
N_B=d_B[u,v].
$$


The integer contractions are


$$
A_B=N_{B,1}^{T}\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^{T}\Omega N_{B,2}.
$$


The final full gcd and primitive pair are


$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=\frac{A_B}{g_B}>0,\qquad
p_n=\frac{H_B}{g_B}.
$$


The primitive multiplier is $d_B^2/g_B$.

With $s=s_2(n)$, the retained exact interfaces are


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
0,\frac{3n}{2}-v_2(b!)-s_2(n)-1-(\gamma-\alpha)
\right\}.
}
\tag{15.1}
$$



A proved equality $\alpha=\gamma=6$ would permit substituting $\gamma-\alpha=0$ at those indices. It would not settle any odd-prime contribution to $g_B$ or $q_n$, nor provide unrestricted relative-depth control.

---

## 16. Whole error and the irrationality objective

The center remains


$$
c_n=\frac{p_n}{q_n}
=\frac{2b!}{\lambda R}\frac HN.
$$


At the retained scope of the complete signed-error theorem,


$$
\epsilon_n=c_n-(e+\pi)<0
\quad\text{eventually},
$$




$$
\log|\epsilon_n|
=
-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$


The whole primitive evaluated error is


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n>0
}
\quad\text{eventually}.
$$



The present reduction does not prove that this complete nonzero form tends to zero. Even a successful modulus-$128$ alignment would leave the same-index primitive-denominator and whole-error comparison unresolved.

---

# Final ledger

### New result proved

The complete lifted reconstruction admits a division-safe six-case reduction through


$$
J_d=\binom{k+d-1}{d},\qquad k\text{ odd},
$$


and the joint scalars reduce exactly to (8.8)–(8.9), with:

* all $128$ residues;
* all weight-depth-four coordinates;
* actual high kernels and original parameters;
* negative moments through $-10$;
* both original $t$-ranges;
* the shortened terminal block;
* the actual endpoint $+1$.

The low coefficient functions have the proved sufficient state space


$$
D\text{ odd}\pmod{512},\qquad t\pmod{512}.
$$



### Not proved

The finite low coefficients have not been evaluated here. Consequently:

* $H-N\equiv0\pmod{128}$ is not proved or disproved;
* the new norm residue image is not determined;
* no new original-family equality $\alpha=\gamma=6$ is claimed;
* no new primitive-denominator estimate follows.

### Exact remaining bottleneck

First evaluate the explicit low coefficient functions. If the universal mixed coefficient identity vanishes, it closes the new alignment immediately. If it does not, the remaining obligation is exactly the actual weighted convolution (8.9), including its terminal term—not another contact calculation.

Beyond this digit, unrestricted relative valuation, odd-prime gcd control, and the whole primitive-error comparison remain open.



$$
\boxed{\text{No unconditional proof or disproof of irrationality of }e+\pi\text{ is obtained.}}
$$


