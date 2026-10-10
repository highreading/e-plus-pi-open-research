> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 — third-defect closure and an unconditional infinite population of the required higher-convolution locus

## Main results

The supplied independent computations close the outstanding low-polynomial calculation. I reuse them without requesting a rerun:


$$
R_C(d,J)=27K_d(J),\qquad R_{29}(d,J)=20K_d(J),
$$


and consequently


$$
\Gamma _0(d)=\Gamma _1(d)=0\qquad(0\le d\le24).
$$



After checking the reconstruction dependencies, this proves the following conditional theorem for the **actual** family:


$$
\boxed{
0\le d\le24,\quad T=0,\quad D_1=0
\quad\Longrightarrow\quad
M-(6C_n)^{-1}D\in29^3\mathbb Z_{29}.
}
\tag{A}
$$



The population condition can now be settled affirmatively. It does **not** require evaluating the higher convolutions at a growing list of original indices.

I prove that at least **100 residue classes of the original parameter $t$ modulo $841$** satisfy


$$
0\le d\le24,\qquad T=0,\qquad D_1=0.
$$


On these classes there is the stronger, termwise statement


$$
29\mid X_k\qquad(0\le k\le H),
$$


and therefore


$$
\mathcal T\equiv0\pmod{841},\qquad U\equiv0\pmod{29}.
$$



In particular, one sufficient original-index condition is


$$
\boxed{
3^{432827+682892t}\equiv410910916\pmod{594823321}.
}
\tag{B}
$$


This congruence specifies one nonempty residue class of $t\bmod841$, proved below. Every index in that class has


$$
d=0,\qquad H\equiv20\pmod{29},
$$


and satisfies the hypotheses of (A).

I also give an exact, bounded-state recurrence for


$$
\mathcal T\bmod841,\qquad U\bmod29,
$$


and hence for the two conditions $T=0,D_1=0$. Its state dimension is independent of $H$. The population proof uses an absorbing zero at its **first digit**, so it does not require executing that recurrence on the enormous original indices.

These results do **not** settle irrationality or rationality of $e+\pi$. In particular, the congruence in (A) does not control the relative valuations of $M$ and $D$ once $D$ is deeper than $29^3$, and it does not determine the final gcd or the global primitive denominator.

---

## 1. Domain and notation

Throughout,


$$
p=29,\qquad L=p^4=707281,\qquad b_*=687936,
$$


and the original domain is


$$
a=432827+682892t,\qquad t\ge0,\qquad
b=3^a,\qquad n=2001b,\qquad m_w=1.
\tag{1.1}
$$


Thus $a\ge1$ is preserved. No auxiliary cylinder parameter is substituted for an original index.

Every contact inverse has its actual finite range


$$
0\le i,j<b,
$$


and the actual weighted columns have coordinates


$$
0\le j\le b.
$$



The metric is the falling-factorial metric


$$
\omega_j=j!\binom{n+2}{j}=(n+2)_{\underline j},
\qquad
\Omega=\operatorname{diag}(\omega_j^2).
\tag{1.2}
$$


The earlier description of this expression as “rising” is not used.

Retain the actual normalized columns


$$
P=\frac{Z_w}{p^2},\qquad
Q=\frac{Y}{p^3},\qquad
Y=\frac{V_w}{b!},
$$


and their contractions


$$
D=P^TP,\qquad M=P^TQ,\qquad r=(6C_n)^{-1}.
\tag{1.3}
$$


The supplied original-family unit statement $C_n\in\mathbb Z_p^\times$ is used at this scope.

Extract the higher parameters from the actual $b$:


$$
b=b_*+Lh,\qquad h=pH+d,\qquad 0\le d<p,
$$




$$
n=191110+LN,\qquad
N=2001h+1946=3+pA,
$$




$$
\boxed{A=69h+67=2001H+69d+67.}
\tag{1.4}
$$



Define


$$
F(J)=\binom NJ\binom{2N+h-J}{h-J},
\qquad 0\le J\le h,
\tag{1.5}
$$


and


$$
X_k=\binom Ak\binom{2A+H-k}{H-k},
\qquad 0\le k\le H.
\tag{1.6}
$$


The higher convolution quantities are


$$
\mathcal T=\sum_{k=0}^{H}X_k^2,\qquad
T=\mathcal T\bmod p,\qquad
U=\sum_{k=0}^{H}kX_k^2\bmod p.
\tag{1.7}
$$


On $T=0$, put


$$
T_1=\frac{\mathcal T}{p}\bmod p.
$$


On the corresponding norm-zero locus, $D_1$ means


$$
D_1=\frac Dp\bmod p.
\tag{1.8}
$$



For $0\le d\le24$, let


$$
K_d(J)=11(d+7-J)^2+18(3-J)^2
      =11(d+4)(d+10-2J)\quad\text{in }\mathbb F_p[J].
\tag{1.9}
$$


Admissible fifth digits are


$$
0\le s\le3,\qquad 0\le d-s\le22.
$$


For such $s$, set


$$
w_s=\binom3s^2\binom{d-s+6}{6}^2,
$$




$$
\rho_s=H_{3-s}-H_s+H_{d-s}-H_{d-s+6},
\qquad H_j=\sum_{i=1}^{j}i^{-1}\in\mathbb F_p.
\tag{1.10}
$$


Then


$$
f(d)=\sum_{\rm adm.\ s}w_sK_d(s),
$$




$$
\beta(d)=
\sum_{\rm adm.\ s}w_s\bigl(K_d'(s)+2\rho_sK_d(s)\bigr).
\tag{1.11}
$$


The supplied exact table gives $f(d)\ne0$ for every $0\le d\le24$.

---

## 2. What the completed finite certificate establishes

The completed universal pass has shape order


$$
(0,1),(1,1),(1,0),
$$


and gives


$$
T^{(0)}=(203,0,0,0,0,0,638,0,0)\pmod{841},
$$


with all eighteen harmonic entries zero.

The two nonzero exact divisions are


$$
203/29=7,\qquad638/29=22.
$$


Therefore the supplied ordinary-polynomial reconstruction is


$$
R_C(D,J)=7(D+7-J)^2+22(3-J)^2.
\tag{2.1}
$$


Since


$$
27\cdot11=7,\qquad27\cdot18=22\pmod{29},
$$


this is the ordinary polynomial identity


$$
\boxed{R_C(D,J)=27K_D(J)\pmod{29}.}
\tag{2.2}
$$


Its expanded coefficients are indeed


$$
R_C(D,J)=7D^2+15DJ+11D+2J+19.
$$



The established $J_{29}$-calculation gives


$$
\boxed{R_{29}(d,J)=20K_d(J).}
\tag{2.3}
$$



These are identities of the actual reconstructed polynomials. They are not identities merely of functions on $\mathbb F_{29}$. In particular, ordinary differentiation is legitimate, and no quotient by $J^{29}-J$ is involved.

It follows algebraically that both functional contractions vanish:


$$
\mathcal L_d(R_C)=27\mathcal L_d(K_d)=0,
\qquad
\mathcal L_d(R_{29})=20\mathcal L_d(K_d)=0.
\tag{2.4}
$$


Thus the numerical output and the ordinary-polynomial contraction agree for a structural reason after the finite constants have been established.

The finite certificate alone does not prove the infinite transfer. That transfer is checked next.

---

## 3. Reconstruction audit at the precision actually needed

I reuse the retained finite contact and reconstruction identities, rather than repeat their completed coefficient calculations. The following points are necessary for their application to the actual family.

### 3.1 Finite contact range

The conjugated contact kernel is


$$
C_s(k,l)=
\sum_{v=0}^{s}
\binom{k}{s-v}\binom nv
\binom{-v}{l-k+s-v}.
\tag{3.1}
$$


Its multiplication by the actual upper-triangular inverse uses intermediate indices at most $l<b$. Consequently the finite restriction is exact; no larger inverse is being substituted.

The signed Newton operator retains its boundary factor


$$
\binom{b-1-X+s}{v+i}.
$$


That factor is what records the actual endpoint of the finite summation.

The coefficient estimate


$$
v_p(d_s)\ge1+v_p((s-1)!)
\tag{3.2}
$$


and the degree estimate


$$
\deg \mathscr L_{s,b}h\le\deg h+s
\tag{3.3}
$$


give the retained graded precision reductions.

### 3.2 Safe truncation before reconstruction

For determining


$$
P,Q\bmod p^3,
$$


the raw requirements are


$$
Z_w\bmod p^5,\qquad Y\bmod p^6.
$$



One first truncates at these safe raw precisions. The retained graded bounds give positive Laurent support within $0,\ldots,145$, and the safe raw factorial boundary extends through factorial index $117$, hence through Laurent power $-118$.

On those safe supports the low carry bounds are


$$
W_jB_q(j)\in p^2\mathbb Z_p\qquad(0\le q\le145),
$$




$$
W_jB_q(j)\in p\mathbb Z_p\qquad(-118\le q\le0),
\tag{3.4}
$$


where


$$
W_j=\binom{n+2}{j},\qquad
B_q(j)=\binom{2n+b-j-1}{b-j-q}.
$$



Only **after** these reconstruction factors are applied may the inputs be shortened to:

| Contribution | Required input |
|---|---|
| Positive $P$-kernel | $h_P\bmod p^3$, degree at most $86$ |
| Positive $Q$-contact kernel | $h_Q\bmod p^4$, degree at most $86$ |
| Raw factorial boundary | $c_s\bmod p^5$, $0\le s\le88$ |
| Negative Laurent support retained | $-89,\ldots,0$ |

Here


$$
c_s=\sum_{u=s}^{88}\frac{(b+u)!}{b!}\binom{2n}{u-s}\pmod{p^5}.
\tag{3.5}
$$


The omitted factorial indices $u\ge89$ have coefficient valuation at least five and obtain one additional reconstruction factor. Hence they are zero modulo $p^6$ in $Y$.

This is not the same truncation as the shorter $R_C$ table calculation. The latter uses only $P,Q\bmod p^2$, whereas the proof of the third-defect congruence needs the stronger representation above.

### 3.3 Complete logarithmic force

The complete logarithmic force is removed at this precision only by the retained whole-force estimate


$$
v_p(h_i^F/b!)
\ge v_p(n!)-v_p(b!)
-\lfloor\log_p(2n+b-1)\rfloor\ge6.
\tag{3.6}
$$


No cancellation of selected logarithmic summands is substituted for this bound.

### 3.4 Endpoint and finite high-index range

The actual endpoint remains


$$
Z_{w,b}=W_b\,b\theta^P_{b-1},
\qquad
Y_b=W_b(1+b\theta^Q_{b-1}).
\tag{3.7}
$$


The $1$ is included by the absorbed boundary formula.

Writing $j=LJ+x$, the actual high-index ranges are


$$
0\le J\le h\quad(x\le b_*),\qquad
0\le J\le h-1\quad(x>b_*).
\tag{3.8}
$$


For $x>b_*$, every positive $P$-power contributes the factor $h-J$ to its natural multiplier. Thus extending the contractions to $J=h$ adds zero. This is a proved endpoint extension, not an unqualified replacement of the finite range.

### 3.5 Natural polynomial representation and the unfrozen boundary term

Four-level factorial stripping gives natural ordinary polynomials $P_x(J),Q_x(J)$, with integral coefficients at the required precision, such that


$$
P_{LJ+x}\equiv(-1)^{j+1}F(J)P_x(J)\pmod{p^3},
$$




$$
Q_{LJ+x}\equiv(-1)^{j+1}F(J)Q_x(J)\pmod{p^3}.
\tag{3.9}
$$



The positive coefficients can be frozen at $x$ at the precisions stated in the sources. The unit-boundary coefficient cannot be frozen throughout the stronger precision-three reconstruction. The retained correction is


$$
\delta Y_{LJ+x}
\equiv(-1)^{j+1}LJ\,W_jB_{-2}(j)\pmod{p^6}.
\tag{3.10}
$$


It contributes to $Q_x$ at order $p^2$, and hence to the second residual polynomial below. Its scalar contraction is killed by $T=0$; it is not deleted before that contraction.

### 3.6 Transfer from the fixed representative

The low table is transferred only after the leading contracted polynomial has been formed. Before specializing $N\bmod p=3$ and $h\bmod p=d$, its two leading coefficients are


$$
g_e-\kappa_e/6\in p\mathbb Z_p.
$$


Changing $N,h$ by multiples of $p$ changes their associated squares by multiples of $p$, so the whole change is in $p^2$.

The harmonic corrections already contain $p$. Their residual dependence uses only $N,h\bmod p$.

This is the required aggregate lifted-polynomial argument. It does **not** claim that each column separately is independent of higher parameter digits.

These checks supply the infinite reconstruction transfer used in the next theorem. The unrelated global signed-error theorem is not needed for this local result.

---

## 4. Conditional third-defect theorem for the actual family

### Theorem 1

For the actual family (1.1), suppose


$$
0\le d\le24,\qquad T=0.
$$


Then


$$
\boxed{
D_1=C_n^2\bigl(f(d)T_1+\beta(d)U\bigr)\pmod p,
}
\tag{4.1}
$$


and


$$
\boxed{
\frac{M-rD}{p^2}
=
(27C_n+20J_{29})
\bigl(f(d)T_1+\beta(d)U\bigr)
\pmod p.
}
\tag{4.2}
$$


In particular,


$$
\boxed{
T=0,\quad D_1=0
\quad\Longrightarrow\quad
M-rD\in p^3\mathbb Z_p.
}
\tag{4.3}
$$



#### Proof

The natural low-polynomial reconstruction gives


$$
\sum_x(P_xQ_x-rP_x^2)
=
p\widetilde R(J)+p^2\widetilde S(J)\pmod{p^3},
\tag{4.4}
$$


where the leading residual polynomial is


$$
R:=\widetilde R\bmod p
=C_nR_C+J_{29}R_{29}.
$$


By the completed finite identities,


$$
\boxed{R=(27C_n+20J_{29})K_d.}
\tag{4.5}
$$



The complete contraction is


$$
M-rD\equiv
p\sum_{J=0}^{h}F(J)^2\widetilde R(J)
+p^2\sum_{J=0}^{h}F(J)^2\widetilde S(J)
\pmod{p^3}.
\tag{4.6}
$$


For any integral polynomial $V$, the leading Lucas contraction is


$$
\sum_{J=0}^{h}F(J)^2V(J)
\equiv
T\sum_{\rm adm.\ s}w_sV(s)\pmod p.
\tag{4.7}
$$


Therefore $T=0$ kills the second sum in (4.6), including the contribution of the unfrozen boundary correction.

To evaluate the first sum one order further, write $J=pk+s$. On admissible $s$, with $v=d-s$,


$$
F(pk+s)\equiv
\binom3s\binom{v+6}{6}X_k
\bigl(1+p(E_s+k\rho_s)\bigr)\pmod{p^2},
\tag{4.8}
$$


where $E_s$ is independent of $k$. This follows directly by stripping the first factorial level in both binomials. Explicitly, one may take


$$
E_s=
A(H_3-H_{3-s})
+(2A+H)H_{v+6}-HH_v-2AH_6
\pmod p.
\tag{4.9}
$$


The coefficient of $k$ is exactly $\rho_s$ from (1.10).

Nonadmissible $s$ give $p\mid F(pk+s)$, and their squares vanish modulo $p^2$. On admissible $s$, the remaining finite range is exactly $0\le k\le H$.

For an ordinary polynomial lift $\widetilde V$,


$$
\widetilde V(pk+s)
\equiv\widetilde V(s)+pkV'(s)\pmod{p^2}.
\tag{4.10}
$$


On $T=0$, the terms containing $E_s\mathcal T$ vanish at this precision. Hence


$$
\frac1p\sum_{J=0}^{h}F(J)^2\widetilde V(J)
\equiv
\left(\sum_{\rm adm.\ s}w_sV(s)\right)T_1
+
\left(\sum_{\rm adm.\ s}w_s
 [V'(s)+2\rho_sV(s)]\right)U
\pmod p.
\tag{4.11}
$$



Apply this with $V=R$, use (4.5), and substitute into (4.6). This proves (4.2).

For the norm, its leading low polynomial is $C_n^2K_d$:


$$
\sum_xP_x(J)^2=C_n^2\widetilde K_d(J)+pV_1(J)\pmod{p^2}.
\tag{4.12}
$$


The contraction of $pV_1$ vanishes modulo $p^2$ on $T=0$, by (4.7). Applying (4.11) to $K_d$ proves (4.1).

Finally $C_n$ is a unit. Thus $D_1=0$ implies


$$
f(d)T_1+\beta(d)U=0,
$$


which makes the right side of (4.2) zero. ∎

### A slightly stronger slope statement

Let


$$
\lambda=\frac{27C_n+20J_{29}}{C_n^2}\pmod p.
$$


Equations (4.1)–(4.2) also show that, on $T=0$,


$$
\boxed{M\equiv(r+p\lambda)D\pmod{p^3}.}
\tag{4.13}
$$


Here any integral lift of $\lambda$ may be used: $D\in p\mathbb Z_p$ on $T=0$, so changing that lift by a multiple of $p$ changes the right side only modulo $p^3$.

On the deeper locus $D_1=0$, the added slope term $p\lambda D$ is itself in $p^3$, recovering (4.3).

---

## 5. A finite recurrence for the two higher convolution conditions

The outstanding conditions can be evaluated through


$$
\mathcal T\bmod p^2,\qquad U\bmod p,
$$


because on $T=0$, (4.1) gives $D_1$.

There is an important simplification:

> Any $k$ for which $p\mid X_k$ contributes zero to $\mathcal T\bmod p^2$, not merely to $T\bmod p$.

Consequently only paths with **no carries in either binomial defining $X_k$** need be retained.

### 5.1 Carry-free digit paths

Fix $d$, and put


$$
c_d=69d+67,\qquad A=2001H+c_d.
$$


Write


$$
H=\sum_i\eta_i p^i,\qquad
A=\sum_i a_i p^i,\qquad
2A=\sum_i c_i p^i.
$$



Generate the digits of $A$ from those of $H$ using


$$
a_i\equiv2001\eta_i+\kappa_i\pmod p,
\qquad
\kappa_{i+1}
=\left\lfloor\frac{2001\eta_i+\kappa_i}{p}\right\rfloor,
\qquad
\kappa_0=c_d.
\tag{5.1}
$$


For $0\le d\le24$, the carry range


$$
0\le\kappa_i\le2000
\tag{5.2}
$$


is invariant.

Generate $2A$ by a doubling carry:


$$
c_i\equiv2a_i+\varepsilon_i\pmod p,\qquad
\varepsilon_{i+1}
=\left\lfloor\frac{2a_i+\varepsilon_i}{p}\right\rfloor,
\qquad\varepsilon_0=0,
\tag{5.3}
$$


with $\varepsilon_i\in\{0,1\}$.

Let $k_i,l_i$ be the digits of $k$ and $H-k$. Their sum carries satisfy


$$
k_i+l_i+\sigma_i=\eta_i+p\sigma_{i+1},
\qquad \sigma_0=0,\qquad \sigma_i\in\{0,1\}.
\tag{5.4}
$$


A path contributes to $\mathcal T\bmod p^2$ only if


$$
\boxed{
0\le k_i\le a_i,\qquad
0\le l_i\le p-1-c_i
}
\tag{5.5}
$$


at every digit. These conditions respectively forbid carries in


$$
k+(A-k)=A,\qquad 2A+(H-k).
$$



Conversely, every path satisfying (5.4)–(5.5), terminating with zero carries, corresponds to exactly one $0\le k\le H$ for which $X_k$ is a unit.

For fixed $\eta_i,\sigma_i,k_i$, the candidate $l_i$ is determined modulo $p$, so each state has at most $29$ outgoing digit choices.

### 5.2 Unit weight through precision $p^2$

For a legal local tuple $\tau=(a,c,k,l)$, define


$$
g(\tau)=
\binom ak^2\binom{c+l}{l}^2\pmod{p^2}.
\tag{5.6}
$$


All factorial denominators here are units, since the upper indices are at most $28$.

For two adjacent legal tuples


$$
\tau=(a,c,k,l),\qquad \tau'=(a',c',k',l'),
$$


the first harmonic correction for $X_k$ is


$$
\begin{aligned}
E(\tau,\tau')={}&
a'H_a-k'H_k-(a'-k')H_{a-k}\\
&+(c'+l')H_{c+l}-c'H_c-l'H_l.
\end{aligned}
\tag{5.7}
$$


Thus a complete carry-free path has squared weight


$$
\boxed{
X_k^2\equiv
\prod_i g(\tau_i)
\prod_i\bigl(1+2pE(\tau_i,\tau_{i+1})\bigr)
\pmod{p^2},
}
\tag{5.8}
$$


where the terminal next tuple is zero.

To verify (5.8), apply at each factorial level


$$
U_p(pm+s)\equiv(28!)^m s!(1+pmH_s)\pmod{p^2}.
$$


On a carry-free binomial path, the exponents of $28!$ cancel. The remaining factorial ratios give (5.6); the next digits in the harmonic terms give (5.7). Squaring introduces the factor $2$.

This use of prime-power binomial machinery stays within its finite integer hypotheses.

### 5.3 Compression to six accumulated residues per carry state

There is no need to retain the entire previous tuple. Define


$$
v(\tau)=
\left(
H_a-H_{a-k},\;
H_{a-k}-H_k,\;
H_{c+l}-H_c,\;
H_{c+l}-H_l
\right)\in\mathbb F_p^4.
\tag{5.9}
$$


Then


$$
E(\tau,\tau')
=a'v_1(\tau)+k'v_2(\tau)+c'v_3(\tau)+l'v_4(\tau).
\tag{5.10}
$$



For each carry state


$$
(\kappa,\varepsilon,\sigma)
\in\{0,\ldots,2000\}\times\{0,1\}^2,
$$


store:

* $W\in\mathbb Z/p^2\mathbb Z$, the total prefix weight;
* $Z_1,\ldots,Z_4\in\mathbb F_p$, the weighted previous harmonic vector;
* $V\in\mathbb F_p$, the prefix weight multiplied by the first digit $k_0$.

Initially,


$$
W=1,\qquad Z_1=\cdots=Z_4=V=0
$$


at $(c_d,0,0)$, and all other states are zero.

For a legal current tuple $(a,c,k,l)$, let $g=g(a,c,k,l)$. Add to its next carry state:


$$
\boxed{
W_{\rm new}\;{+}{=}\;
g\left[W+2p(aZ_1+kZ_2+cZ_3+lZ_4)\right]\pmod{p^2},
}
\tag{5.11}
$$




$$
\boxed{
(Z_r)_{\rm new}\;{+}{=}\;
(g\bmod p)(W\bmod p)v_r(a,c,k,l)\pmod p.
}
\tag{5.12}
$$


For $V$, the first digit uses


$$
V_{\rm new}\;{+}{=}\;(g\bmod p)\,k,
\tag{5.13}
$$


and every later digit uses


$$
V_{\rm new}\;{+}{=}\;(g\bmod p)V.
\tag{5.14}
$$



After processing the digits of $H$, append four zero digits and accept only zero terminal carries. Three zero digits drain the multiplier carry; the fourth also closes the adjacent-digit harmonic term.

The terminal outputs are exactly


$$
\boxed{
W_{\rm terminal}=\mathcal T\bmod p^2,\qquad
V_{\rm terminal}=U\bmod p.
}
\tag{5.15}
$$



The recurrence has at most


$$
2001\cdot2\cdot2=8004
$$


carry states, each holding six residues. Two dense layers require less than one MiB with ordinary machine-word storage. A digit has at most


$$
8004\cdot29=232116
$$


candidate transitions.

This is a uniform recurrence with the actual finite endpoint enforced by terminal carries. It is not a finite table extrapolated to unrestricted higher digits.

---

## 6. A first-digit obstruction that forces both higher conditions

The recurrence above exposes an especially simple absorbing zero.

### Lemma 2 — one-digit annihilation of every summand

Let


$$
a_0=A\bmod29,\qquad z=H\bmod29.
$$


If


$$
\boxed{
1\le a_0\le14,\qquad 29-a_0\le z\le28,
}
\tag{6.1}
$$


then


$$
\boxed{29\mid X_k\quad\text{for every }0\le k\le H.}
\tag{6.2}
$$


Consequently


$$
\boxed{
\mathcal T\equiv0\pmod{841},\qquad
T=0,\qquad T_1=0,\qquad U=0.
}
\tag{6.3}
$$



#### Proof

Since $a_0\le14$, the units digit of $2A$ is $2a_0$, without a carry from doubling.

Suppose $X_k$ were a unit. The first binomial would require


$$
0\le k_0\le a_0.
$$


The second would require


$$
0\le l_0\le28-2a_0,
$$


where $l_0$ is the units digit of $H-k$.

The units-digit sum condition is


$$
k_0+l_0=z+29\sigma_1.
$$


But


$$
k_0+l_0\le a_0+(28-2a_0)=28-a_0<z,
$$


so neither $\sigma_1=0$ nor $\sigma_1=1$ is possible.

Thus there is no carry-free first-digit path. Every $X_k$ is divisible by $29$. Squaring proves the congruence modulo $841$, and the other conclusions follow. ∎

The obstruction is termwise. It does not rely on cancellation in $\mathcal T$.

### Eligible $d$-classes

From (1.4),


$$
A\bmod29=(69d+67)\bmod29=(11d+9)\bmod29.
\tag{6.4}
$$


For $0\le d\le24$, the eligible cases are:



$$
\begin{array}{c|rrrrrrrrrrrrr}
d&0&2&3&5&8&10&11&13&16&18&21&23&24\\ \hline
a_0&9&2&13&6&10&3&14&7&11&4&8&1&12
\end{array}
\tag{6.5}
$$



For each displayed $d$, any


$$
H\bmod29\in\{29-a_0,\ldots,28\}
\tag{6.6}
$$


satisfies Lemma 2.

The total number of pairs $(d,H\bmod29)$ is


$$
9+2+13+6+10+3+14+7+11+4+8+1+12
=\boxed{100}.
\tag{6.7}
$$



By (4.1), every such pair gives $D_1=0$. Thus these are explicit sufficient conditions for the third-defect locus.

---

## 7. Original-parameter transfer: all 100 pairs occur infinitely often

The supplied fifth-digit formula


$$
d(t)=16-t\pmod{29}
$$


is only the first layer of a stronger transfer.

Let


$$
P_0=682892=28p^3,\qquad R=3^{P_0}.
$$


The retained modular calculation


$$
3^{28}\equiv1+15p\pmod{p^2}
$$


gives


$$
v_p(R-1)=4.
\tag{7.1}
$$



### Lemma 3 — higher-digit bijection on the original progression

For every $m\ge1$, the map


$$
t\bmod p^m\longmapsto
\frac{3^{432827+P_0t}-b_*}{p^4}\bmod p^m
\tag{7.2}
$$


is a bijection.

#### Proof

For distinct integers $t_1,t_2$,


$$
3^{432827+P_0t_2}-3^{432827+P_0t_1}
=
3^{432827+P_0t_1}(R^{t_2-t_1}-1).
$$


Since $p$ is odd and $v_p(R-1)=4$, elementary binomial lifting gives


$$
v_p(R^u-1)=4+v_p(u)
$$


for every nonzero integer $u$. Therefore


$$
v_p\left(
\frac{3^{432827+P_0t_2}-3^{432827+P_0t_1}}{p^4}
\right)=v_p(t_2-t_1).
\tag{7.3}
$$


Thus (7.2) is injective modulo $p^m$, and hence bijective on the finite set of $p^m$ residues. ∎

No $p$-adic logarithm estimate or coefficient-height theorem is needed here.

Taking $m=2$, every pair


$$
(d,H\bmod29)
$$


occurs in exactly one residue class of $t\bmod841$. Therefore:

### Theorem 4 — unconditional infinite population

The original progression contains at least 100 distinct residue classes of $t\bmod841$ on which


$$
0\le d\le24,\qquad
T=0,\qquad
D_1=0.
\tag{7.4}
$$


Each class contains infinitely many nonnegative $t$. In particular, the set satisfying these conditions has lower natural density at least


$$
\boxed{\frac{100}{841}}
$$


relative to the original $t$-parameter.

#### Proof

Apply Lemma 3 to the 100 distinct residues


$$
h\equiv d+29z\pmod{841}
$$


listed by (6.5)–(6.6). Lemma 2 and (4.1) then give (7.4). ∎

This proves the requested infinite population. It is unnecessary to assume, or to prove, that the two conditions hold automatically at every point of the original progression.

### One explicit sufficient cylinder

Choose


$$
d=0,\qquad H\equiv20\pmod{29}.
$$


Then


$$
h\equiv580\pmod{841},
$$


so


$$
b\equiv b_*+L\cdot580
=410910916\pmod{p^6},
$$


where


$$
p^6=594823321.
$$


Thus condition (B) is sufficient.

If $t_*\in\{0,\ldots,840\}$ is its unique parameter residue, the resulting original exponent subprogression is


$$
\boxed{
a=432827+682892t_*+574312172\,s,\qquad s\ge0,
}
\tag{7.5}
$$


because


$$
682892\cdot841=574312172.
$$



This is an original power-$3$ subprogression, not an auxiliary family.

---

## 8. Stronger actual-column consequence on the populated subprogressions

The termwise condition also has a useful reconstruction consequence.

By Lucas reduction of (1.5), nonadmissible fifth digits make $F(J)$ divisible by $p$. On admissible digits,


$$
F(pk+s)\equiv
\binom3s\binom{d-s+6}{6}X_k\pmod p.
$$


Thus Lemma 2 implies


$$
F(J)\equiv0\pmod p\qquad(0\le J\le h).
\tag{8.1}
$$



Using the integral natural multipliers in (3.9), with the finite boundary and endpoint treatment already checked,


$$
\boxed{P,Q\in p\mathbb Z_p^{\,b+1}.}
\tag{8.2}
$$


Equivalently,


$$
\boxed{
Z_w\in p^3\mathbb Z_p^{\,b+1},
\qquad
Y\in p^4\mathbb Z_p^{\,b+1}.
}
\tag{8.3}
$$



Therefore on these original subprogressions,


$$
D,M\in p^2\mathbb Z_p.
$$


Theorem 1 adds the stronger scalar relation


$$
\boxed{M-rD\in p^3\mathbb Z_p.}
\tag{8.4}
$$



The population proof therefore does not exploit accidental isotropy of a nonzero vector modulo $29$: it forces an additional whole-column factor first.

---

## 9. What the third-defect relation actually says about $\gamma-\alpha$

To make the valuation issue explicit, write


$$
\alpha=v_p(D),\qquad\gamma=v_p(M).
$$


These are the quantities denoted $\delta,\mu$ in the retained MAIN29 gcd interface.

On the populated locus,


$$
\alpha,\gamma\ge2,\qquad M=rD+p^3E,\qquad E\in\mathbb Z_p,
\tag{9.1}
$$


and $r$ is a unit.

### 9.1 If the norm has exact depth two

If


$$
\alpha=2,
$$


then $rD$ has valuation two and $p^3E$ has larger valuation. Hence


$$
\boxed{\gamma=2,\qquad\gamma-\alpha=0.}
\tag{9.2}
$$



This is an exact valuation conclusion.

### 9.2 If the norm is deeper

If $\alpha\ge3$, the congruence proves only $\gamma\ge3$, unless the next defect $E$ is also controlled.

Put


$$
s=3+v_p(E),
$$


with $s=\infty$ if $E=0$. Then:

* if $\alpha<s$, $\gamma=\alpha$;
* if $\alpha>s$, $\gamma=s$;
* if $\alpha=s$, cancellation can give $\gamma\ge\alpha$, with no upper bound supplied by the congruence.

For example, as a matter of valuation logic, if $E$ is a unit and $\alpha\ge4$, then


$$
\boxed{\gamma=3,\qquad\gamma-\alpha=3-\alpha.}
\tag{9.3}
$$


Thus a deep norm does not turn the third-defect congruence into favorable mixed valuation alignment.

Conversely, when $\alpha=3$, cancellation between the two order-three terms can make $\gamma$ arbitrarily larger, unless further information is available.

These examples describe what the congruence permits; they are not asserted to be realized by the actual family.

### 9.3 Exact limitation

The completed result is


$$
M-rD\equiv0\pmod{p^3},
$$


not


$$
v_p(M-rD)\ge v_p(D)+1
$$


and not


$$
v_p(M)=v_p(D)
$$


at all depths.

The next relevant lemma would have to control the normalized fourth defect


$$
\frac{M-rD}{p^3}
$$


on the subset where $D\in p^3\mathbb Z_p$, or provide a different all-depth relative-valuation argument.

---

## 10. Final gcd, actual primitive denominator, and whole error

Retain the actual least two-column denominator


$$
N_B=d_B[u,v],\qquad v_{29}(d_B)=0.
$$


For the actual falling metric,


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2}.
$$


The final gcd and primitive pair are


$$
g_B=\gcd(A_B,|H_B|),\qquad
p_n=\frac{H_B}{g_B},\qquad
q_n=\frac{A_B}{g_B}>0.
\tag{10.1}
$$


Thus the primitive multiplier is $1/g_B$ on the integer Gram pair, or $d_B^2/g_B$ on the rational Gram pair.

With


$$
F_n=v_{29}(n!),\qquad F_b=v_{29}(b!),
$$


the retained exact interface is


$$
\boxed{
v_{29}(g_B)
=
\min\{4F_n+4+\alpha,\;2F_n+F_b+5+\gamma\},
}
\tag{10.2}
$$




$$
\boxed{
v_{29}(q_n)
=
\max\{0,\;2F_n-F_b-1+\alpha-\gamma\}.
}
\tag{10.3}
$$



If $\alpha=2$, the new theorem gives $\alpha-\gamma=0$. If $\alpha$ is deeper, Section 9 explains why that difference remains uncontrolled.

No contribution from another prime has been determined by this local argument. In particular, neither the extra whole-column factors nor the third mixed defect may be credited as an unproved global gcd improvement.

For


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


the exact whole evaluated form remains


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
\tag{10.4}
$$


At the retained status of the complete signed-error theorem,


$$
\epsilon_n>0\quad\text{eventually},
$$




$$
\log|\epsilon_n|
=
-\left(2+\frac1{2001}\right)n\log(1+\sqrt2)+o(n).
\tag{10.5}
$$


That theorem retains its source hypotheses and proof status. The complete exponential residual, logarithmic force, factorial/contact boundary, and endpoint remain part of $\epsilon_n$.

Norm nonvanishing follows from positivity. Mixed nonvanishing retains the supplied original-family dependency. The new modular calculation does not replace either the complete real-error theorem or the final denominator calculation.

---

## 11. Bounded exact arithmetic certificate for the new population result

**No further computation is needed to prove infinitude.** Lemmas 2–3 already do so.

For convenient archival verification, however, a very small calculation can return the actual 100 parameter residues $t\bmod841$, including $t_*$ in (7.5). It does not rerun any universal $\Gamma$-calculation.

### Inputs and exact divisions

Let


$$
m=p^6,\qquad
B_0=3^{432827}\bmod m,\qquad
R_0=3^{682892}\bmod m.
$$


Compute


$$
h_0=\frac{B_0-b_*}{L},\qquad
u=\frac{R_0-1}{L}.
\tag{11.1}
$$


Both divisions are exact. Then


$$
s=B_0u\bmod841
$$


is a unit, and


$$
h(t)\equiv h_0+st\pmod{841}.
\tag{11.2}
$$


Indeed,


$$
(1+Lu)^t\equiv1+Lut\pmod{p^6},
$$


because $L^2=p^8$.

For a target pair $(d,z)$,


$$
\boxed{
t_{d,z}\equiv(d+29z-h_0)s^{-1}\pmod{841}.
}
\tag{11.3}
$$



### Complete short certificate generator

```python
import json

p = 29
L = p**4
modulus = p**6
bstar = 687936
abase = 432827
aperiod = 682892

B0 = pow(3, abase, modulus)
R0 = pow(3, aperiod, modulus)

assert (B0 - bstar) % L == 0
assert (R0 - 1) % L == 0

h0 = (B0 - bstar) // L
u = (R0 - 1) // L

assert h0 % p == 16       # retained fifth-digit receipt
assert u % p == 15

s = (B0 * u) % (p*p)
assert s % p == p-1
sinv = pow(s, -1, p*p)

rows = []
for d in range(25):
    a0 = (11*d + 9) % p
    if not (1 <= a0 <= 14):
        continue

    for z in range(p-a0, p):
        target_h = d + p*z
        target_b = bstar + L*target_h
        tclass = ((target_h - h0) * sinv) % (p*p)

        # Original-index transfer, with no construction of the huge b.
        assert pow(3, abase + aperiod*tclass, modulus) == target_b

        # Exact first-digit obstruction:
        # k0 <= a0, l0 <= 28-2*a0 cannot sum to z or z+29.
        assert a0 + (p-1-2*a0) < z

        rows.append({
            "d": d,
            "H_mod29": z,
            "A_mod29": a0,
            "t_mod841": tclass,
            "b_mod29pow6": target_b
        })

assert len(rows) == 100
assert len({r["t_mod841"] for r in rows}) == 100

chosen = next(r for r in rows if r["d"] == 0 and r["H_mod29"] == 20)
assert chosen["b_mod29pow6"] == 410910916

print(json.dumps({
    "status": "PASS",
    "scope": (
        "Exact residue representatives for the proved first-digit "
        "population obstruction. No Gamma table recomputed."
    ),
    "B0_mod29pow6": B0,
    "R0_mod29pow6": R0,
    "h0_mod841": h0,
    "slope_mod841": s,
    "number_of_original_t_classes": 100,
    "chosen_class": chosen,
    "original_a_step": aperiod * p*p,
    "classes": rows
}, indent=2))
```

### Expected verifiable output

A successful receipt returns:

1. the two modular powers $B_0,R_0$;
2. both exact-division checks in (11.1);
3. the unit slope $s\bmod841$;
4. 100 distinct $t$-classes;
5. an original modular-power verification for every class;
6. the selected $t_*$ for $d=0,H\equiv20\pmod{29}$;
7. the exponent step $574312172$.

The predicted number of classes, the target residue $410910916$, and the annihilation inequalities are proved above; they are not empirical expectations.

This calculation uses only modular exponentiation with modulus $594823321$, unit inversion modulo $841$, and small loops. A conservative allocation is one CPU, 64 MiB memory, and one minute. It does not construct any length-$b$ vector or inverse.

The general recurrence of Section 5 can be audited separately on small $H$ by comparison with the direct finite sums, but such an audit is not required for the first-digit population proof.

---

# Conclusion and proof-status ledger

## New established results

Using the retained actual reconstruction identities and the independently completed finite constants:

1. The conditional third-defect theorem is proved:
   

$$
d\le24,\quad T=0,\quad D_1=0
   \Longrightarrow
   M-(6C_n)^{-1}D\in29^3\mathbb Z_{29}.
$$



2. A bounded carry recurrence computes the genuine higher quantities
   

$$
\mathcal T\bmod841,\qquad U\bmod29,
$$


   with the full finite range and all higher digits preserved.

3. A first-digit obstruction forces every $X_k$ to be divisible by $29$.

4. Exactly 100 explicitly described low pairs $(d,H\bmod29)$, with $d\le24$, satisfy that obstruction.

5. Every one of those pairs transfers to a distinct residue class of the **original** $t\bmod841$. Hence the required simultaneous population is infinite, with relative lower density at least $100/841$.

6. On those classes,
   

$$
P,Q\in29\mathbb Z_{29}^{b+1},
   \qquad
   D,M\in29^2\mathbb Z_{29},
   \qquad
   M-(6C_n)^{-1}D\in29^3\mathbb Z_{29}.
$$



## Exact remaining mathematical bottleneck

The population condition is no longer the immediate obstruction.

The next local obstruction is **relative valuation control beyond the established third defect**, especially on


$$
D\in29^3\mathbb Z_{29}.
$$


The congruence proved here does not bound $\gamma-\alpha$ there.

For irrationality, a further and separate bottleneck remains: control of the **actual final primitive denominator**


$$
q_n=A_B/\gcd(A_B,|H_B|)
$$


across all primes, together with the complete nonzero evaluated error


$$
q_n(e+\pi)-p_n.
$$



Accordingly, the new result is an unconditional infinite population theorem and a completed conditional third-defect theorem—not a proof or disproof of irrationality of $e+\pi$.
