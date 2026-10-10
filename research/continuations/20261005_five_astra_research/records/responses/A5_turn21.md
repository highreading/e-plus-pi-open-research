> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5 — the fifth mixed digit vanishes on the populated subclass $r\equiv50\pmod{128}$

## Result and scope

On the unchanged original domain


$$
b=9^r,\qquad n=4002b,\qquad r=18+32u,\quad u\ge0,
$$


write


$$
b=128D+81,\qquad n=128C+66,\qquad C=4002D+2532.
$$



I obtain the following fifth-precision result:


$$
\boxed{
r=50+128w,\quad w\ge0
\quad\Longrightarrow\quad
H\equiv N\equiv0\pmod{64}.
}
\tag{1}
$$



More precisely, on this subclass **every actual coordinate defect vanishes individually**:


$$
\boxed{
X_j(Y_j-X_j)\in64\mathbb Z_2
\qquad(0\le j\le b).
}
\tag{2}
$$



The proof uses seven-level factorial stripping to expose the common higher binomial in every retained moment and weight. Once that common factor is retained, the exact identity $T=0$ eliminates all but two potentially unit-sensitive residue classes. The required two remaining unit bits are evaluated by the already proved, complete second-column convolution—not by the norm.

The argument actually proves the slightly broader implication


$$
\boxed{
T=0\ \text{as an ordinary integer count}
\quad\Longrightarrow\quad H\equiv N\pmod{64}
}
\tag{3}
$$


for original exponents in the parent domain.

This does **not** evaluate the fifth discrepancy on the entire common-zero locus, where $T$ can be positive and even. In particular, no all-zero-locus alignment or unrestricted relative-valuation bound is asserted.

---

## 1. Source checks and precise dependencies

The bounded source comparison used here has the following outcome.

* The $P_{64}$ vector in turn20 agrees with the supplied fixed $P$-control. Its use on the original domain rests on turn20’s central truncation, forcing-tail proof, parameter transfer and degree bound—not on the finite receipt alone.
* The $Q_{128}$ vector and its contact correction agree with the supplied $Q$-control and the audit in A4turn27.
* The moment-control file supplies exactly the coefficients obtained from $p,d,\beta$ by the displayed $U_s,V_s$ formulas. Its periodicity certificates concern bounded Newton polynomials, not periodicity of the large binomial kernels.
* I reuse
  

$$
C_1=2T,\qquad N\equiv48T+32\chi\pmod{64}
  \tag{4}
$$


  at the audited scope of A4turn27.
* The tests on 401 auxiliary values of $D$ and 64 original exponents remain finite checks. They are not used to prove (1).

The paired-derangement determinant construction is a separate family. Its primitive determinant pair and its analytic error are not substituted for the present columns or metric.

No external archive or primary-literature search facility is available in this response, so I do not claim a fresh search or independent verification of the supplied file hashes. The stripping argument below is derived directly. It is classical prime-power factorial arithmetic of the type underlying Kummer’s carry theorem and binomial congruences modulo prime powers; no global novelty claim is made.

---

## 2. Actual quantities, forces and finite boundaries

Retain


$$
h=\frac n2,\qquad R=2^h\binom{2h}{h},
\qquad \lambda=\frac{(n!)^2}{2^n},
$$




$$
X=\frac{Z_w}{2R},\qquad Y=\frac{V_w}{4b!},
\qquad N=X^TX,\qquad H=X^TY.
$$



The metric and coordinate range are unchanged:


$$
W_j=\binom{n+2}{j},\qquad
\omega_j=j!W_j=(n+2)_{\underline j},
$$




$$
\Omega=\operatorname{diag}(\omega_j^2)_{0\le j\le b}.
$$


Every contact inverse still has its actual range $0\le i,j<b$.

The complete fifth-precision inputs are


$$
p=(34,31,7,5,48,12,4,4,32,8,56,8)\pmod{64},
$$




$$
d=q-2p=(112,102,10,124,16,24,56,0,96,16,80,96)
\pmod{128},
$$


and the complete exterior-difference coefficients are


$$
(\beta_1,\ldots,\beta_7)
=(113,74,78,72,120,80,112)\pmod{128}.
\tag{5}
$$



These retain all seven factorial boundary values


$$
(B_0,\ldots,B_6)
=(69,106,54,56,120,80,112)\pmod{128}.
$$


The later factorial tails vanish because $v_2((b+7)!/b!)=7$. The logarithmic force is absent at this precision only through the supplied **whole-force** estimate


$$
v_2(h_i^F/b!)
\ge2000b+2-2\lfloor\log_2(8005b-1)\rfloor>7.
\tag{6}
$$



For completeness, the bounded coefficients used below are defined by


$$
F_s(x)=\binom{s+3}{3}
       \sum_{r=s}^{11}p_r\binom{x}{r-s},
\qquad 0\le s\le11,
$$




$$
G_s(x)=\binom{s+3}{3}
       \sum_{r=s}^{11}d_r\binom{x}{r-s}.
$$


Put


$$
Z_{-k}(x)=\beta_k\quad(1\le k\le7),\qquad
Z_s(x)=G_s(x)\quad(0\le s\le11),
$$


and extend unspecified coefficients by zero. Then


$$
U_s(x)=F_s(x)+xF_s(x-1)+xF_{s+1}(x-1),
\tag{7}
$$




$$
V_s(x)=Z_s(x)+xZ_s(x-1)+xZ_{s+1}(x-1).
\tag{8}
$$



Thus every mixed coefficient below comes from $V_s$, including its negative-moment terms.

For an interior coordinate,


$$
2X_j\equiv(-1)^{j+1}W_j\mathcal F_j\pmod{64},
$$




$$
4(Y_j-X_j)\equiv(-1)^{j+1}W_j\mathcal G_j\pmod{128},
\tag{9}
$$


where


$$
\mathcal F_j=\sum_{s=-1}^{11}U_s(j)\mathcal M_s(j),\qquad
\mathcal G_j=\sum_{s=-8}^{11}V_s(j)\mathcal M_s(j).
$$


Consequently


$$
8X_j(Y_j-X_j)\equiv W_j^2\mathcal F_j\mathcal G_j
\pmod{512}.
\tag{10}
$$



The established coefficient periodicity permits $U_s(j),V_s(j)$ to be evaluated at $j\bmod128$. It does not replace the actual moments.

---

# Part I. Seven-level stripping with every borrow retained

## 3. An exact factorial identity

Define the odd factorial


$$
O(m)=\prod_{\substack{1\le a\le m\\a\text{ odd}}}a,\qquad O(0)=1,
$$


and


$$
L_7(m)=\prod_{i=0}^{6}O\!\left(\left\lfloor\frac m{2^i}\right\rfloor\right).
$$



Repeatedly separating even and odd factors gives the exact identity


$$
m!
=
2^{\sum_{i=1}^{7}\lfloor m/2^i\rfloor}
\left\lfloor\frac m{128}\right\rfloor!
L_7(m).
\tag{11}
$$



For $m=128q+a$, $0\le a<128$,


$$
\sum_{i=1}^{7}\left\lfloor\frac m{2^i}\right\rfloor
=127q+v_2(a!).
\tag{12}
$$



All quotients of $L_7$-factors appearing below have odd numerator and denominator. They are genuine $2$-adic units.

For any required modulus $2^p$, $p\ge3$,


$$
O(m+2^p)\equiv O(m)\pmod{2^p},
\tag{13}
$$


because the product of all odd residue classes modulo $2^p$ is $1$. Thus these units have fixed finite residue descriptions. No unbounded factorial product needs to be numerically evaluated to obtain their required bits.

---

## 4. Strip every retained moment into one shared higher kernel

Write


$$
j=128t+\rho,\qquad d=D-t,\qquad k=2C+1,\qquad K=k+d.
$$


Here $k$ is odd.

The actual moment is


$$
M_s(\rho,t)=
\binom{128K+84-\rho}{128d+80-\rho-s}.
\tag{14}
$$



For the 29 retained residues $\rho\le68$, put $\varepsilon_\rho=0$. For $\rho=96,100$, put $\varepsilon_\rho=1$. Define


$$
a_\rho=84-\rho+128\varepsilon_\rho,
$$




$$
\ell_{\rho s}=80-\rho-s+128\varepsilon_\rho,
$$




$$
\delta_s=
\begin{cases}
1,&s<-4,\\
0,&s\ge-4,
\end{cases}
\qquad
c_s=4+s+128\delta_s.
\tag{15}
$$


All three low arguments lie in $[0,127]$ for the retained ranges.

The complete low stripping exponent is


$$
m_{\rho s}
=
127\delta_s+
v_2(a_\rho!)
-v_2(\ell_{\rho s}!)
-v_2(c_s!).
\tag{16}
$$


Equivalently,


$$
m_{\rho s}
=s_2(\ell_{\rho s})+s_2(c_s)-s_2(a_\rho)-\delta_s.
$$



Let


$$
u_{\rho s}
=
\frac{
L_7(128K+84-\rho)
}{
L_7(128d+80-\rho-s)\,L_7(128k+4+s)
}.
\tag{17}
$$


This is an odd rational unit. Applying (11) to all three factorials gives


$$
M_s(\rho,t)
=
2^{m_{\rho s}}u_{\rho s}
\frac{(K-\varepsilon_\rho)!}
{(d-\varepsilon_\rho)!\,(k-\delta_s)!}.
\tag{18}
$$



Now introduce the single shared higher binomial


$$
J_d=\binom{k+d-1}{d}.
$$


Then (18) becomes


$$
\boxed{
M_s(\rho,t)
=
\frac{J_d}{k}\,
P_{\varepsilon_\rho}\,
k^{\delta_s}\,
2^{m_{\rho s}}u_{\rho s},
\qquad
P_0=K,\quad P_1=d.
}
\tag{19}
$$



This retains all borrow polynomials:

* $K$ for the non-overflow residues;
* $d$ for the overflow residues;
* $k$ for every negative-complement borrow $s<-4$.

Only the odd number $k$ is inverted. No even higher-index factor has been cancelled.

For $\rho=96,100$, the condition $t\le D-1$ gives $d\ge1$, so all factorials in (18) remain within their actual nonnegative ranges.

---

## 5. Strip every weight

The weight is


$$
W_{\rho,t}=\binom{128C+68}{128t+\rho}.
$$


Put


$$
z_\rho=68-\rho+128\varepsilon_\rho,
$$




$$
b_\rho=
127\varepsilon_\rho+
v_2(68!)-v_2(\rho!)-v_2(z_\rho!),
\tag{20}
$$


and define the odd unit


$$
w_\rho=
\frac{L_7(128C+68)}
{L_7(128t+\rho)\,L_7(128(C-t)+68-\rho)}.
$$


Then


$$
\boxed{
W_{\rho,t}
=
2^{b_\rho}w_\rho
\binom Ct(C-t)^{\varepsilon_\rho}.
}
\tag{21}
$$



For $\rho\le68$, $b_\rho=v_2\binom{68}{\rho}$, giving the four rows in turn20. For $\rho=96,100$, $b_\rho=2$.

Equations (19) and (21) perform the requested seven-level stripping on every retained moment and weight, with a common higher kernel and all borrows present.

---

# Part II. Coefficientwise contraction and its required precision

## 6. The normalized low factors

Define


$$
\mathfrak f_\rho
=
\sum_{s=-1}^{11}
U_s(\rho)\,k^{\delta_s}2^{m_{\rho s}}u_{\rho s},
$$




$$
\mathfrak g_\rho
=
\sum_{s=-8}^{11}
V_s(\rho)\,k^{\delta_s}2^{m_{\rho s}}u_{\rho s}.
\tag{22}
$$



Because the $U$-range starts at $s=-1$, its borrow factor is always $1$. It is nevertheless important to retain the $k^{\delta_s}$ factors in $\mathfrak g_\rho$.

Let


$$
B_d=\binom{k+d}{d},\qquad
E_t=\binom Ct B_d.
\tag{23}
$$


For the non-overflow residues, (19)–(21) give the exact common-kernel form


$$
\boxed{
W_{\rho,t}^2\mathcal F_{\rho,t}\mathcal G_{\rho,t}
=
2^{2b_\rho}w_\rho^2 E_t^2
\mathfrak f_\rho\mathfrak g_\rho.
}
\tag{24}
$$



For the overflow residues, use


$$
B_d^-=\binom{k+d-1}{d-1}.
$$


Then


$$
\boxed{
W_{\rho,t}^2\mathcal F_{\rho,t}\mathcal G_{\rho,t}
=
2^{2b_\rho}w_\rho^2
\left((C-t)\binom Ct B_d^-\right)^2
\mathfrak f_\rho\mathfrak g_\rho.
}
\tag{25}
$$



These are not independently chosen higher binomials: both are the specializations of the shared formula (19).

### Exact product precision

For an individual bilinear term indexed by $s,\ell$, let $w=v_2(W_{\rho,t})$, and let $\nu$ be the valuation of $B_d$, or $B_d^-$ in the overflow case. Its normalized odd product is required modulo


$$
2^{p_{\rho,s,\ell}},\qquad
p_{\rho,s,\ell}
=
\max\!\left\{
0,\,
9-2w-2\nu
-m_{\rho s}-m_{\rho\ell}
-v_2(U_s(\rho))-v_2(V_\ell(\rho))
\right\}.
\tag{26}
$$


A zero coefficient requires no precision.

Thus the needed unit precision is determined by the actual weight depth and the retained moment depths. It is not uniformly seven or nine bits. In particular, many apparently unit-sensitive terms require no unit data at all after the common higher kernel is exposed.

---

## 7. The fixed low-coefficient divisibilities

The following bounds hold coefficientwise in (22), before any higher-index sum:


$$
\mathfrak f_\rho\in2^{f_\rho}\mathbb Z_2,\qquad
\mathfrak g_\rho\in2^{g_\rho}\mathbb Z_2.
$$





$$
\begin{array}{c|c|c|c}
\rho&b_\rho&f_\rho&g_\rho\\ \hline
0,64&0&1&2\\
4,68&0&4&4\\
2,66&1&2&2\\
32&1&1&2\\
36&1&4&4\\
1,3,16,20,34,48,52,65,67&2&1&0\\
8,12,18,24,28,33,35,40,44,50,56,60&3&0&0\\
96&2&1&2\\
100&2&4&4
\end{array}
\tag{27}
$$



These are sufficient bounds, not claims that every displayed valuation is exact.

### Verification of the nontrivial rows

The bounds follow from the explicit finite inequalities


$$
v_2(U_s(\rho))+m_{\rho s}\ge f_\rho,
\qquad
v_2(V_s(\rho))+m_{\rho s}\ge g_\rho.
\tag{28}
$$


The odd units and the odd borrow factor $k$ do not affect them.

Some useful simplifications make this audit transparent.

* For $\rho=4,36,68,100$, the low upper argument is respectively
  

$$
80,\ 48,\ 16,\ 112.
$$


  For $1\le c\le15$,
  

$$
v_2\binom{a_\rho}{c}=4-v_2(c).
$$


  Combining this with the supplied $U,V$ coefficients gives $f_\rho,g_\rho\ge4$. The negative-complement terms have the additional stripping exponent (16) and do not lower these bounds.

* For $\rho=2,66$, the only $U$-coefficients not visibly divisible by $4$ occur at $s=-1,0,2$. Their low complementary indices are $3,4,6$; the corresponding binomial depths are $4,2,2$. This proves $f_\rho\ge2$. In the $V$-column, the potentially smaller coefficients likewise acquire enough low depth to give $g_\rho\ge2$.

* For $\rho=0,32,64,96$, all $U$-coefficients are even. In the $V$-column the odd coefficient occurs at complementary index $3$, whose low binomial has depth $2$. The complementary-index-$2$ coefficient is even and its low binomial has depth $1$. All remaining terms have depth at least $2$. Hence $f_\rho\ge1,g_\rho\ge2$.

* In the nine $b_\rho=2$ classes, every $U$-coefficient is even except for the explicitly visible possibilities at $s=-1$ or $s=0$. Their associated low binomials are even. Thus $f_\rho\ge1$.

This verifies (27) without assuming favorable cancellation among units.

---

## 8. Contract the 31 residues before summing over $t$

Write


$$
e_t=v_2(E_t).
$$



For the non-overflow residues, (24) and (27) give


$$
v_2\!\left(
W_{\rho,t}^2\mathcal F_{\rho,t}\mathcal G_{\rho,t}
\right)
\ge
2b_\rho+2e_t+f_\rho+g_\rho.
\tag{29}
$$



Suppose now that $e_t\ge2$. Every non-overflow residue except $0,64$ vanishes modulo $512$, coefficientwise:



$$
\begin{array}{c|c}
\rho&\text{lower bound from (29)}\\ \hline
4,68&12\\
2,66&10\\
32&9\\
36&14\\
1,3,16,20,34,48,52,65,67&9\\
8,12,18,24,28,33,35,40,44,50,56,60&10
\end{array}
\tag{30}
$$



The overflow classes vanish for every parent-domain index, independently of $e_t$. Indeed,


$$
v_2\!\left((C-t)\binom Ct\right)
=
v_2\!\left(C\binom{C-1}{t}\right)\ge1,
$$


so $v_2(W_{\rho,t})\ge3$. Equation (27) then gives


$$
\rho=96:\quad 2v_2(W_{\rho,t})+f_\rho+g_\rho\ge9,
$$


and a stronger bound for $\rho=100$.

Consequently, **before any high-index summation**, the complete 31-residue contraction at an index with $e_t\ge2$ reduces to just


$$
E_t^2\left(
w_0^2\mathfrak f_0\mathfrak g_0+
w_{64}^2\mathfrak f_{64}\mathfrak g_{64}
\right)\pmod{512}.
\tag{31}
$$



There is no remaining contribution from an off-pair depth-$3$/depth-$2$ term: those terms were included in (24)–(30), rather than discarded because their squares vanish.

For the two remaining residues:

* if $e_t\ge3$, (29) already gives depth at least $9$;
* if $e_t=2$, the baseline depth is $7$, so exactly two further normalized product bits remain to be controlled.

The next section evaluates those two bits.

---

# Part III. The remaining paired unit bits

## 9. The required second-column unit identity

This step uses the complete mixed column, not $N$.

Let


$$
\zeta=\eta-2\theta.
$$


The complete fourth-precision convolution in turn17 gives, at the two actual coordinates


$$
j_0=128t,\qquad j_1=128t+64,
$$


the congruences


$$
\zeta_{j_0}\equiv48\kappa_0 B_d\pmod{64},
\qquad
\zeta_{j_1}\equiv16\kappa_0 B_d\pmod{64},
\tag{32}
$$


where $\kappa_0$ is odd.

For clarity, the content of this identity is stronger than the scalar statement $H\equiv N\pmod{32}$. It comes from the evaluated sampled kernel


$$
K(16s+64)\equiv K(16s)\pmod{64},
\qquad K(16)=16\kappa_0,
$$


and its unrestricted binomial convolution. The two higher-binomial multipliers reduce modulo $4$ to $3B_d$ and $B_d$, respectively.

The actual weights satisfy


$$
W_{128t}\equiv W_{128t+64}\equiv\binom Ct\pmod4.
\tag{33}
$$


Since $64\mid j_0,j_1$, the reconstructed term $j\zeta_{j-1}$ vanishes modulo $64$. Combining (32)–(33) with the reconstruction therefore yields


$$
\boxed{
W_{128t}\mathcal G_{128t}
\equiv48\kappa_0E_t\pmod{64},
}
$$




$$
\boxed{
W_{128t+64}\mathcal G_{128t+64}
\equiv16\kappa_0E_t\pmod{64}.
}
\tag{34}
$$



These formulas are obtained from the exterior terms and $Q-2P$, equivalently from the $V_s$-column. No coefficient is inferred from a norm count.

If $4\mid E_t$, both right-hand sides in (34) vanish. Hence


$$
W_j\mathcal G_j\in64\mathbb Z_2
\qquad(j=128t,128t+64).
\tag{35}
$$



On the other hand, seven-level stripping and $f_0,f_{64}\ge1$ give


$$
W_j\mathcal F_j\in2E_t\mathbb Z_2\subset8\mathbb Z_2.
\tag{36}
$$


Thus


$$
W_j^2\mathcal F_j\mathcal G_j\in512\mathbb Z_2.
\tag{37}
$$



In the precise $e_t=2$ case, (34) says that the normalized low factor $\mathfrak g_\rho/4$ is zero modulo $4$. This evaluates exactly the two bits left after (31). The value of the odd constant $\kappa_0$ is unnecessary.

We have therefore obtained the evaluated contraction


$$
\boxed{
4\mid E_t
\quad\Longrightarrow\quad
\text{the complete 31-residue raw contraction at }t
\equiv0\pmod{512}.
}
\tag{38}
$$


In fact, each of its coordinate contributions is zero separately.

---

## 10. Why the populated subclass has $4\mid E_t$ for every $t$

Recall


$$
a=\frac{C-2}{4},\qquad v=\left\lfloor\frac D4\right\rfloor,
$$


and the ordinary finite count


$$
T=
\#\left\{
0\le i\le v:
\binom ai\text{ odd},\
\binom{2a+1+v-i}{v-i}\text{ odd}
\right\}.
\tag{39}
$$



The audited exact identity is


$$
\#\{0\le t\le D:v_2(E_t)=1\}=2T.
\tag{40}
$$


Every $E_t$ is even on the parent domain.

For


$$
r=50+128w
$$


the original exponent congruence gives


$$
D\equiv7\pmod8.
$$


Indeed,


$$
9^{18+32u}\equiv721+256u\pmod{1024},
$$


so $D\equiv5+2u\pmod8$, and here $u\equiv1\pmod4$.

Consequently $v$ is odd and $a$ is even. In (39), an admissible $i$ must be even. An admissible $q=v-i$ must also be even, since


$$
q\mathbin{\&}(2a+1)=0
$$


and $2a+1$ is odd. Their sum cannot equal the odd integer $v$. Therefore


$$
T=0
\tag{41}
$$


as an ordinary integer count.

Equations (40)–(41), together with the evenness of every $E_t$, prove


$$
\boxed{4\mid E_t\qquad(0\le t\le D).}
\tag{42}
$$



This is the additional higher-kernel divisibility that makes the fifth contraction collapse. Merely knowing $T\equiv0\pmod2$ would not suffice.

---

## 11. Actual endpoint and completion

The actual endpoint remains


$$
X_b=\frac{W_b\,b\theta_{b-1}}2,\qquad
Y_b=\frac{W_b(1+b\eta_{b-1})}{4}.
$$


The $+1$ has not been removed. The retained endpoint bounds give


$$
v_2(X_b)\ge5,\qquad v_2(Y_b)\ge4,
$$


so


$$
X_b(Y_b-X_b)\in2^9\mathbb Z_2.
$$



The already established $v_2(W_j)\ge4$ exclusion covers every interior coordinate outside the 31 retained residue classes. Equations (30), (37), and (42) cover all retained coordinates, with the actual ranges


$$
0\le t\le D
$$


for the 29 non-overflow classes and


$$
0\le t\le D-1
$$


for $96,100$.

Therefore


$$
X_j(Y_j-X_j)\equiv0\pmod{64}
\qquad(0\le j\le b),
$$


and hence


$$
H-N\equiv0\pmod{64}.
\tag{43}
$$



Finally, on this subclass $T=0$ and $\chi=0$. The audited norm formula gives


$$
N\equiv48T+32\chi\equiv0\pmod{64}.
$$


Combining with (43),


$$
\boxed{
r=50+128w,\quad w\ge0
\quad\Longrightarrow\quad
N\equiv H\equiv0\pmod{64}.
}
$$



Thus the complete fifth mixed digit on this populated subclass is


$$
\boxed{\frac{H}{32}\equiv0\pmod2,}
\qquad
\boxed{\frac{H-N}{32}\equiv0\pmod2.}
\tag{44}
$$



---

# Part IV. What remains outside this subclass

## 12. The exact surviving obstruction

The proof identifies a sharper obstruction on the parent domain:

> A fifth-discrepancy contribution can survive only at a higher index $t$ for which $v_2(E_t)=1$.

The overflow residues are already zero, and all indices with $v_2(E_t)\ge2$ have just been evaluated to zero.

For $v_2(E_t)=1$, the coefficientwise bounds leave the following working precisions for the normalized low product:



$$
\begin{array}{c|c}
\rho&\text{remaining product precision}\\ \hline
0,64&\bmod16\\
2,66&\bmod2\\
32&\bmod4\\
1,3,16,20,34,48,52,65,67&\bmod4\\
8,12,18,24,28,33,35,40,44,50,56,60&\bmod2
\end{array}
\tag{45}
$$


The classes $4,36,68,96,100$ are already zero.

The exact number of potentially relevant higher indices is $2T$. On the full true common-zero locus, $T$ is even but need not be zero. Therefore the next concrete follow-on lemma is:

**Remaining unit-contraction lemma.**  
Evaluate the stripped residue contraction at $v_2(E_t)=1$, with the precisions in (45), and prove its total parity for the actual relation


$$
C=4002D+2532,\qquad D=\frac{9^r-81}{128}.
$$



This is a substantially smaller task than the former unrestricted 31-residue convolution. It still requires mixed units from $V_s$; the count $2T$ alone does not evaluate it.

---

## 13. Final gcd, actual denominator and whole error

No normalization or metric has changed.

Let $d_B$ be the least common denominator of the actual two-column lift, and set


$$
N_B=d_B[u,v].
$$


Retain


$$
A_B=N_{B,1}^{T}\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^{T}\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),
\qquad
p_n=\frac{H_B}{g_B},\qquad
q_n=\frac{A_B}{g_B}>0.
$$


The primitive multiplier on the uncleared quadratic pair is


$$
\frac{d_B^2}{g_B},
$$


and the actual center is


$$
c_n=\frac{p_n}{q_n}
=\frac{2b!}{\lambda R}\frac HN.
$$



With $s=s_2(n)$, $\alpha=v_2(N)$, and $\gamma=v_2(H)$, the exact interface remains


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
\tag{46}
$$



The new result gives


$$
\alpha,\gamma\ge6
\qquad(r\equiv50\pmod{128}),
$$


but it does not bound $\gamma-\alpha$.

At the retained status of the complete signed-error theorem,


$$
\epsilon_n=c_n-(e+\pi)<0
\quad\text{eventually},
$$




$$
\log|\epsilon_n|
=
-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$


The whole primitive evaluated error is still


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n>0
}
\quad\text{eventually}.
\tag{47}
$$


No selected residual, row-clearer or unreduced denominator replaces this expression.

---

# Concluding ledger

### 1. New result and proof status

Using the supplied complete transfers and the proved fourth paired second-column convolution, the argument above proves


$$
\boxed{
r=50+128w,\ w\ge0
\Longrightarrow H\equiv N\equiv0\pmod{64}.
}
$$



The proof includes:

* seven-level stripping of every retained moment and weight;
* one shared higher kernel, with the $K,d,k,C-t$ borrow factors retained;
* coefficientwise low-factor bounds for all 31 residues;
* elimination of the off-pair mixed terms before any high-index sum;
* evaluation of the two remaining paired unit bits;
* the actual overflow ranges and full endpoint.

More generally, $T=0$ implies $H\equiv N\pmod{64}$. No conclusion is extended to positive even $T$.

### 2. Exact remaining mathematical bottleneck

At fifth precision, only the $v_2(E_t)=1$ higher-index sector remains unevaluated. Its required unit precisions are now explicitly listed in (45).

Beyond fifth precision, the substantive arithmetic obstruction is unchanged: there is no unrestricted estimate controlling $\gamma-\alpha$, or another sufficient same-index estimate for the actual primitive denominator after the final gcd.

Accordingly, **irrationality of $e+\pi$ remains unresolved**.

### 3. Bounded exact arithmetic audit

No growing-index computation is needed for the subclass proof.

A useful small independent certificate has:

**Inputs**


$$
p,d,\beta\ \text{from (5)},\quad U,V\ \text{from (7)–(8)},
$$


the 31 retained residues, and the stripping exponents (15)–(16).

**Expected verifiable output**

For every retained coefficient, verify


$$
v_2(U_s(\rho))+m_{\rho s}\ge f_\rho,\qquad
v_2(V_s(\rho))+m_{\rho s}\ge g_\rho
$$


with the bounds in (27). This requires at most


$$
31(13+20)=1023
$$


fixed coefficient-depth comparisons, with zeros assigned infinite valuation.

A passing certificate verifies the bounded arithmetic used in the universal stripping proof. It is not evidence for an unproved population claim, and it does not by itself settle the remaining $v_2(E_t)=1$ contraction.
