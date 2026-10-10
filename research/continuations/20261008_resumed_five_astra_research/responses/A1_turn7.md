> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The actual second radical on the endpoint annihilator

## Abstract and proof status

The rationality or irrationality of $e+\pi$ remains unresolved.

This report advances the local original-family problem in four ways.

1. **The actual endpoint-annihilating operator is evaluated.** After exact endpoint lifts and an endpoint-adapted first complement, its leading matrix is
   

$$
\boxed{
   -\left(
   [y^{(P/3-1)/2-u-v}](1-y)^{2\chi}(1+y)^2
   \right)_{0\le u,v<\delta-1}.
   }
$$


   The minus sign and both shifts are essential. All physical returns at this digit are retained.

2. **The remaining rank range is closed.** In the previously unresolved range
   

$$
B_1>\delta,\qquad \varepsilon\le0,
$$


   put
   

$$
\Pi=P/3,\qquad
   \zeta=4\chi-\Pi,\qquad \Delta=|\zeta|.
$$


   Let $\mathfrak q$ be the least power of $3$ strictly greater than $\Delta$, and set
   

$$
e_*=\log_3(\Pi/\mathfrak q),\qquad
   \omega_*=(-1)^{e_*},\qquad
   \epsilon_*=\operatorname{sgn}(\zeta).
$$


   Then the nullity of the full divided radical matrix is exactly
   

$$
\boxed{
   k_2=
   \frac{\Delta+\omega_*
   -|2\Delta-\mathfrak q-5\epsilon_*|}{4}.
   }
$$


   This is an evaluated integer formula, not an unevaluated syzygy-gap function.

3. **The actual endpoint is nonzero on the complete second radical in every range.** In the remaining range, this follows from an explicit binomial construction of the minimal syzygy and a symmetry that applies because its two last exponents are equal. Complete kernels, saturated integer lifts, and unit complements are given below.

4. **An additional exact adapted elimination is paid.** Its physical inverse costs $3^{-5}$, its matrix return begins at $3^7$, and it makes no new endpoint or diagonal return. The original directional problem is reduced, with its $3^{-1}$ allowance preserved, to the actual residual layer at $3^6$. This is not a solution through all later singular layers.

The $3^5$ digit is protected by the known leading endpoint. The $3^6$ digit is **not** declared protected: exact endpoint lifts and the first adapted-complement return can affect it.

---

## 1. Original objects and the scope of reuse

All statements concern sufficiently large members of exactly the original family


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




$$
m=2^{2j-1},\qquad n=4^j+1=2m+1,\qquad A=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$


with


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15},
$$


and


$$
\frac{103}{1000}<\frac{N_0}{P_0}<\frac{104}{1000}.
$$



The arithmetic identities remain


$$
P_0=243P=3^{h-27},\qquad N_0=243r,\qquad D=P_0+N_0,
$$




$$
P=3^{h-32},\qquad r\equiv2\pmod9,\qquad r\ \text{odd},
$$




$$
4^j=243(3^{26}-1)P-243r+1.
$$


Write


$$
x=y-1,\qquad Q=27P,\qquad b=Q-N_0,\qquad R=b/2,\qquad \chi=P-R.
$$


In particular,


$$
\chi=\frac{243r-25P}{2},
\qquad
.0145<\frac{\chi}{P}<.136.
$$



For sufficiently large original indices,


$$
\boxed{
v_3(\chi)=5,\qquad \chi/243\equiv1\pmod9.
}
\tag{1.1}
$$


Thus


$$
\chi\equiv243\pmod{2187}.
\tag{1.2}
$$


These restrictions will be used in the rank proof. The parameters are not freely chosen auxiliary integers.

### 1.1 Finite coordinates and the physical terminal

Retain


$$
U_s=x^s\quad(0\le s<D),
$$




$$
z_i=x^Dy^i\quad(0\le i<\nu),\qquad \nu=D/2-1,
$$




$$
Y_t=y^t\quad(d\le t\le m),\qquad d=D+\nu,\qquad W=[U\ Y].
$$



The physical HIGH terminal is $Y_m$, not $z_{\nu-1}$.

The finite prefix and tail boundaries remain


$$
R_*=\frac{9Q+1}{2},\qquad a_0=R_*-1,
$$




$$
\tau=\frac{N_0-3}{2},\qquad \ell=3R+1,
$$




$$
K=\{0,\ldots,\ell-1\},\qquad
J=\{\ell,\ldots,\tau-1\},
$$




$$
n_J=\frac{Q-4b-5}{2},\qquad R_*+\tau=\nu.
$$


In particular, the last middle column stays in the actual finite $J$-block.

### 1.2 Complete source and corrected columns

The complete functional is


$$
\mathcal M(P)=
-\frac{3^h}{4}\mathfrak f(P)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](P-P(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^t)=(2t)!.
$$


The largest physical pole denominator is


$$
4H-4D+5<3^{h+1}.
$$



The complete core is


$$
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=-71-A,
$$




$$
G_c(f,g)=\mathcal M(Q_cfg),
$$


and its corrected columns are exactly


$$
E_c=G_c(W,W),\qquad
F_i=z_i-WE_c^{-1}G_c(W,z_i).
$$



The one-lift inputs remain


$$
\Psi_a=x^{D+b}y^{k_0+a}(y^{3Q}+3),
\qquad k_0=\frac{3Q+1}{2},
\qquad 0\le a\le R,
$$


with $\mathcal F_a$ their complete-core corrections against the same $W$.

The actual producer is


$$
Q_{\mathrm{act}}=Q_c+3^7\mathscr R,
$$


where


$$
[x^a](3^7\mathscr R)
=-\frac{(n-1)!}{a!}(t_a+\xi v_a),
\qquad 0\le a\le n-1,
$$


and the complete force is


$$
t=
3nh_{\mathrm{vec}}
+(b_{\mathrm{force}}+6)e_{n-1}
+\frac{2b_{\mathrm{force}}}{n-1}e_{n-2},
\qquad b_{\mathrm{force}}=-n-66.
\tag{1.3}
$$


Here


$$
v=T_n^{-1}u,\qquad
u_a=\frac{(n-1)!(-2)^a}{a!},
$$




$$
h_{\mathrm{vec}}
=T_n^{-1}
\left(\binom{n+a}{a}\gamma_{n+a}\right)_{a=0}^{n-1},
$$




$$
T_n(a,b)=\binom{a+b}{a}\gamma_{a+b},
$$




$$
\gamma_{r+1}=(4r+2)\gamma_r+4\gamma_{r-1},
\qquad \gamma_0=1,\quad\gamma_1=0.
$$


The signed, paid $\xi$ is unchanged. In particular,


$$
\mathscr R(-1)=-\frac{\xi((n-1)!)^2}{3^7}.
$$



No term of $t+\xi v$ is discarded. Likewise, the source-return identity remains


$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\mathrm{ret}}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
\tag{1.4}
$$



### 1.3 Established inputs used here

The new proof uses the following supplied results only at their stated scope.

- A1 Turn 6 evaluates the complete-core first divided radical matrix, including its second-prefix and $J$-matrix returns.
- A3 Turn 7 proves
  

$$
\boxed{
  T_{\mathrm{act},\mathrm{red}}-T_{c,\mathrm{red}}\in3^7M.
  }
  \tag{1.5}
$$


  This is a matrix comparison on the entire retained amplitude space. It is not an endpoint comparison.
- The recovered H2 endpoint theorem gives
  

$$
\boxed{
  \overline f_{\mathrm{act},\mathrm{new}}(a)
  =(-1)^{R_*}a(-1)
  }
  \tag{1.6}
$$


  on the actual degree-$\le R$ amplitude space.
- The endpoint-adapted complement theorem and the rank-preservation principle from the archived work are reused, not presented as new general theorems.

The statements in the later reports that left the lowest endpoint samples open are superseded by (1.6). Higher endpoint digits remain separate obligations.

---

## 2. The actual $3^5$ operator on the endpoint annihilator

Put


$$
\Pi=P/3,\qquad
\kappa_1=\frac{\Pi-1}{2},\qquad
L_*=\frac{P-1}{2},
$$




$$
\delta=\min\left\{\chi-1,\frac{P+3}{2}-3\chi\right\}.
$$


The complete first radical is


$$
g_{L_*+u}(y)=(1-y)^{2\chi}y^{L_*+u},
\qquad 0\le u<\delta.
$$



In the polynomial coordinate $p(y)=\sum_{u=0}^{\delta-1}p_u y^u$, write


$$
\mathcal G[p]=(1-y)^{2\chi}y^{L_*}p(y).
$$


The actual leading endpoint is


$$
\overline f(\mathcal G[p])=\sigma p(-1),
\qquad
\sigma=(-1)^{R_*+L_*}.
\tag{2.1}
$$



The supplied evaluated matrix is


$$
\frac{\widehat{\mathscr G}^{\,T}
T_{\mathrm{act},\mathrm{red}}\widehat{\mathscr G}}{3^5}
\equiv-\mathsf D\pmod3,
$$


where


$$
\mathsf D_{uv}
=[y^{\kappa_1-u-v}](1-y)^{2\chi},
\qquad 0\le u,v<\delta.
\tag{2.2}
$$


The transfer from core to actual follows from (1.5), with the already paid $3^{-4}$ complementary inverse.

### 2.1 Exact endpoint lifts

The endpoint-annihilating leading vectors are


$$
h_u=g_{L_*+u}+g_{L_*+u+1},
\qquad 0\le u<\delta-1.
\tag{2.3}
$$


Choose an exact endpoint-unit radical vector $v$, normalized by $f(v)=1$. For example, one may start from the appropriate lifted $g_{L_*}$, whose endpoint is a unit by (2.1).

Set


$$
h_u^{\mathrm{ex}}=h_u-vf(h_u).
\tag{2.4}
$$


Then


$$
f(h_u^{\mathrm{ex}})=0,\qquad
h_u^{\mathrm{ex}}-h_u\in3\mathbb Z_3^{R+1}.
$$



Choose the first complement inside the exact endpoint kernel, as in the archived adapted-complement theorem. Its physical block and cross block have the form


$$
A_4=3^4A_{4,0},\qquad A_{4,0}\in\operatorname{GL}(\mathbb Z_3),
$$




$$
X_4\in3^5M.
$$


Thus


$$
A_4^{-1}=3^{-4}A_{4,0}^{-1},
\qquad
X_4^TA_4^{-1}X_4\in3^6M.
\tag{2.5}
$$


The eliminated endpoint coordinates are exactly zero. Consequently this elimination makes **no new endpoint or diagonal Schur correction**.

### 2.2 Why the $3^5$ digit is protected, but the next digit is not

If $r,s$ reduce to the first radical, then


$$
T_{\mathrm{act},\mathrm{red}}(r,z)\in3^5\mathbb Z_3
$$


for every integral $z$. Hence replacing $r,s$ by $r+3a,s+3b$ changes their pairing by


$$
3T(a,s)+3T(r,b)+9T(a,b)\in3^6\mathbb Z_3.
\tag{2.6}
$$


This pays the exact endpoint lifts at the $3^5$ digit.

It also shows the limitation: the changes in (2.6) can be nonzero at $3^6$. The first adapted-complement return (2.5) can contribute at the same digit. Agreement of the core and actual matrices modulo $3^7$ in a common monomial frame does not, by itself, identify separately endpoint-adapted $3^6$ digits.

### Theorem 2.1 — Evaluated actual endpoint-annihilating operator

Let $\mathcal T_H$ be the actual restricted matrix after the exact endpoint lifts and the endpoint-adapted first complement. Then


$$
\boxed{
\frac{\mathcal T_H}{3^5}
\equiv-\mathsf H_+\pmod3,
}
\tag{2.7}
$$


where


$$
\boxed{
(\mathsf H_+)_{uv}
=[y^{\kappa_1-u-v}]
(1-y)^{2\chi}(1+y)^2,
\qquad 0\le u,v<\delta-1.
}
\tag{2.8}
$$



#### Proof

The leading coordinate map is $p\mapsto(1+y)p$. Thus


$$
\begin{aligned}
(\mathsf H_+)_{uv}
&=\mathsf D_{uv}+\mathsf D_{u+1,v}
+\mathsf D_{u,v+1}+\mathsf D_{u+1,v+1}\\
&=[y^{\kappa_1-u-v}]
(1-y)^{2\chi}(1+2y+y^2).
\end{aligned}
$$


The overall sign is the minus sign in (2.2). Equations (2.5)–(2.6) show that neither the exact lifts nor the adapted first return changes this digit. ∎

### 2.3 Entry evaluation and original support

Write $c_j=[y^j](1-y)^{2\chi}$, with $c_j=0$ outside $0\le j\le2\chi$. Then


$$
(\mathsf H_+)_{uv}
=c_{\kappa_1-u-v}
+2c_{\kappa_1-u-v-1}
+c_{\kappa_1-u-v-2}.
\tag{2.9}
$$


Each $c_j$ is evaluated by Lucas’s rule:


$$
c_j=(-1)^j\prod_i\binom{(2\chi)_i}{j_i}
\quad\text{in }\mathbb F_3.
$$



Since $243\mid\chi$, at most one of the three terms in (2.9) can be nonzero. In particular,


$$
\boxed{
(\mathsf H_+)_{uv}=0
\quad\text{unless}\quad
u+v\equiv119,120,121\pmod{243}.
}
\tag{2.10}
$$


This is an evaluation of the actual restricted matrix, not a separately selected binomial experiment.

All vectors used above are combinations of amplitudes of degree at most $R$. No column beyond the finite middle space is introduced, and no compression formula is extended to the last middle column.

---

## 3. Reused rank ranges and the remaining graded map

Let


$$
B_1=2\chi+2\delta-1-\kappa_1,\qquad
\varepsilon=2\chi+\delta-\Pi.
$$


Denote the nullity of $\mathsf D$ by $k_2$.

The already proved Ranges I–III give:

| Range | $k_2$ | A complete kernel of $\mathsf D$ |
|---|---:|---|
| I: $B_1\le0$ | $\delta$ | $\mathbb F_3[y]_{<\delta}$ |
| II: $0<B_1\le\delta$ | $\delta-B_1$ | $\mathbb F_3[y]_{<k_2}$ |
| III: $\varepsilon>0$ | $\varepsilon$ | $(1-y)^{\Pi-2\chi}\mathbb F_3[y]_{<k_2}$ |

Here and below, a polynomial space with a negative degree bound means zero.

The original congruences exclude the small equalities that could otherwise obscure the range boundaries. On sufficiently large original indices these ranges, and the remaining range, are respectively


$$
\chi<\Pi/8,
$$




$$
\Pi/8<\chi<\Pi/6,
$$




$$
\chi>\Pi/3,
$$


and


$$
\boxed{\Pi/6<\chi<\Pi/3.}
\tag{3.1}
$$


In the remaining range,


$$
\delta=\chi-1.
\tag{3.2}
$$



For example, the equality $\chi=\Pi/3$ is impossible because $v_3(\chi)=5$, whereas $\Pi$ has arbitrarily large ternary valuation. The other boundaries are excluded similarly, using the original multiples of $243$, not asymptotic notation.

### 3.1 Validation of the original selected-degree map

In the remaining range put


$$
a_H=\frac{\Pi+1}{2},\qquad
b_H=4\chi-\frac{\Pi+5}{2},\qquad
c_H=2\chi.
\tag{3.3}
$$


Let


$$
S=\mathbb F_3[X,Y],\qquad Z_h=Y-X.
$$


Homogenizing $p(y)$ to degree $\delta-1=\chi-2$, the matrix $\mathsf D$, up to row order, is multiplication by $Z_h^{c_H}$:


$$
S_{\chi-2}
\longrightarrow
\bigl(S/(X^{a_H},Y^{b_H})\bigr)_{3\chi-2}.
\tag{3.4}
$$



Indeed, the surviving target exponents of $X$ are exactly


$$
\kappa_1-\delta+1,\ldots,\kappa_1.
$$


There are exactly $\delta$ of them, and the corresponding coefficient matrix is (2.2).

The source degree is not truncated by the quotient:


$$
a_H>\chi-2,\qquad b_H>\chi-2.
$$


Moreover,


$$
a_H+b_H=4\chi-2,\qquad
a_H+b_H+c_H=6\chi-2.
\tag{3.5}
$$


A syzygy involving only $X^{a_H},Y^{b_H}$ has total degree at least


$$
a_H+b_H=4\chi-2>3\chi-2.
$$


Therefore taking the third component gives an injective correspondence between syzygies of total degree $3\chi-2$ and the kernel of (3.4).

The strict triangle inequalities are


$$
a_H+b_H-c_H=2\chi-2>0,
$$




$$
a_H+c_H-b_H=\Pi+3-2\chi>0,
$$




$$
b_H+c_H-a_H=6\chi-\Pi-3>0.
\tag{3.6}
$$


The last inequality follows from (3.1) with the original arithmetic buffer.

Thus the supplied Han–Monsky theorem applies to the **specified original graded map**.

---

## 4. Exact rank in the remaining range

Set


$$
\zeta=4\chi-\Pi,\qquad \Delta=|\zeta|.
$$


By (1.1),


$$
\frac{\zeta}{243}\equiv4\pmod9,\qquad v_3(\zeta)=5.
\tag{4.1}
$$


In particular $\zeta\ne0$, and $\Delta$ is not a power of $3$.

Let $\mathfrak q$ be the least power of $3$ greater than $\Delta$. Then


$$
\boxed{
\Delta<\mathfrak q<3\Delta,\qquad
2187\le\mathfrak q\le\Pi/3.
}
\tag{4.2}
$$


Define


$$
e_*=\log_3(\Pi/\mathfrak q),\qquad
\omega_*=(-1)^{e_*},\qquad
\epsilon_*=\operatorname{sgn}(\zeta),
$$


and


$$
M_*=\Pi/\mathfrak q,
$$




$$
a_\circ=\frac{M_*+\omega_*}{2},\qquad
c_\circ=\frac{M_*+\epsilon_*}{2}.
\tag{4.3}
$$


The integer $a_\circ$ is odd. The relevant odd lattice point is


$$
z_\circ=(a_\circ,c_\circ,c_\circ).
\tag{4.4}
$$



### 4.1 The distance is evaluated, not left as a gap function

The three differences between the original triple and $\mathfrak q z_\circ$ are


$$
d_a=a_H-\mathfrak q a_\circ
=\frac{1-\omega_*\mathfrak q}{2},
$$




$$
d_b=b_H-\mathfrak q c_\circ
=\epsilon_*\Delta-\frac{\epsilon_*\mathfrak q+5}{2},
$$




$$
d_c=c_H-\mathfrak q c_\circ
=\frac{\epsilon_*(\Delta-\mathfrak q)}2.
\tag{4.5}
$$


Consequently


$$
\begin{aligned}
g_*
&=\mathfrak q-\bigl(|d_a|+|d_b|+|d_c|\bigr)\\
&=
\boxed{
\frac{\Delta+\omega_*
-|2\Delta-\mathfrak q-5\epsilon_*|}{2}.
}
\end{aligned}
\tag{4.6}
$$


The inequalities in (4.2), together with the original multiples of $243$, imply $g_*>0$. More explicitly,


$$
g_*=2\min\left\{
\frac{\mathfrak q-\Delta+\omega_*+5\epsilon_*}{4},
\frac{3\Delta-\mathfrak q+\omega_*-5\epsilon_*}{4}
\right\},
$$


and both quantities inside the minimum are positive.

### 4.2 Why $\mathfrak q$ is the largest admissible scale

This point is needed; merely finding one odd lattice point would not evaluate the gap.

Let $Q_3$ be any power of $3$ dividing $\Pi$, with $Q_3>\Delta$, and put $M=\Pi/Q_3$. The normalized coordinates are


$$
\frac{a_H}{Q_3}
=\frac M2+\frac1{2Q_3},
$$




$$
\frac{b_H}{Q_3}
=\frac M2+\frac{\zeta-5/2}{Q_3},
$$




$$
\frac{c_H}{Q_3}
=\frac M2+\frac{\zeta}{2Q_3}.
\tag{4.7}
$$



Because $M$ is odd, these lie near a half-integer. The nearest integers for the second and third coordinates are both


$$
\frac{M+\epsilon_*}{2}.
$$


Their uniqueness follows from $\Delta\ge972$ and $Q_3-\Delta\ge486$; the constants $1/2$ and $5/2$ cannot change the rounding.

Their sum is even. Hence the first coordinate of an odd lattice point must be the odd member of


$$
(M-1)/2,\quad (M+1)/2.
$$


That member is


$$
\frac{M+(-1)^{\log_3 M}}2.
$$



Changing the rounding of either the second or third coordinate costs more than $1/Q_3$, whereas changing the first rounding can save only $1/Q_3$. Thus this is the nearest odd lattice point.

Its distance deficit is the formula (4.6), with $Q_3$ in place of $\mathfrak q$. If $Q_3>\mathfrak q$, then


$$
Q_3\ge3\mathfrak q>3\Delta.
$$


The resulting deficit is


$$
\frac{3\Delta-Q_3+(-1)^{\log_3(\Pi/Q_3)}-5\epsilon_*}{2}<0.
$$


The original arithmetic buffer makes the inequality strict.

For scales $Q_3\ge3\Pi$, all normalized coordinates lie in $(0,1)$. The strict triangle inequalities exclude the odd vertices with one coordinate $1$, and


$$
a_H+b_H+c_H<2\Pi
$$


excludes $(1,1,1)$. More distant lattice points cannot have taxicab distance below $1$.

Therefore $\mathfrak q$ is exactly the largest admissible scale in the supplied gap theorem.

### Theorem 4.1 — Closed remaining-range rank

In the range (3.1),


$$
\boxed{
k_2=\operatorname{nullity}\mathsf D
=
\frac{\Delta+\omega_*
-|2\Delta-\mathfrak q-5\epsilon_*|}{4},
}
\tag{4.8}
$$


and


$$
\boxed{\operatorname{rank}\mathsf D=\delta-k_2.}
\tag{4.9}
$$



#### Proof

The two syzygy generator degrees have sum $6\chi-2$ and gap $g_*$. Hence


$$
d_1=3\chi-1-g_*/2,\qquad
d_2=3\chi-1+g_*/2.
$$


At the selected total degree $3\chi-2$, only the first generator contributes, and its contribution has dimension $g_*/2$. The correspondence in §3.1 is injective at this degree. Thus $k_2=g_*/2$, giving (4.8). ∎

This proof closes the rank obligation without substituting an ungraded Jordan type for the selected map.

---

## 5. A complete, explicitly constructible kernel in the remaining range

The rank count alone is not enough for the endpoint question. We now construct the complete kernel.

### 5.1 The smaller triple has gap exactly one

The triple


$$
(a_\circ,c_\circ,c_\circ)
\tag{5.1}
$$


is positive and satisfies the strict triangle inequalities.

It also has syzygy gap exactly $1$. To see this, suppose it had an admissible scale $3^e\ge3$. Since its coordinates are integers, an odd-lattice distance below $1$ at that scale is at most $1-3^{-e}$. Combining this with


$$
\left\|
\frac{(a_H,b_H,c_H)}{\mathfrak q}-z_\circ
\right\|_1
=1-\frac{g_*}{\mathfrak q}
$$


would produce an admissible scale $\mathfrak q3^e>\mathfrak q$ for the original triple, a contradiction.

At scale $1$, (5.1) itself is an odd lattice point. Its gap is therefore $1$.

Put


$$
n_\circ=\frac{a_\circ-1}{2},
\qquad
d_\circ=n_\circ+c_\circ.
\tag{5.2}
$$


There is a unique, up to a nonzero scalar, minimal syzygy of total degree $d_\circ$.

### 5.2 Explicit integer coefficients

For $0\le i\le n_\circ$, define the positive integers


$$
\boxed{
J_i=
\binom{2n_\circ-i}{n_\circ-i}
\binom{c_\circ-n_\circ-1+i}{i}.
}
\tag{5.3}
$$


Let


$$
\nu_\circ=\min_{0\le i\le n_\circ}v_3(J_i).
\tag{5.4}
$$


The auxiliary polynomial


$$
J^\flat(y)=\sum_{i=0}^{n_\circ}\frac{J_i}{3^{\nu_\circ}}y^i
\tag{5.5}
$$


is integral and has nonzero reduction modulo $3$.

This auxiliary division is paid coefficientwise by (5.4). It is not a new division of any original column content or distinguished cofactor.

Every coefficient in (5.5) is explicitly evaluable. For each binomial factor one uses the finite Legendre sums for its valuation and the factorial-unit formula for its normalized residue. Thus:

- a coefficient is zero modulo $3$ if its total binomial valuation exceeds $\nu_\circ$;
- otherwise its residue is the product of the two normalized binomial units.

No matrix-rank calculation is hidden in (5.3)–(5.5).

### 5.3 Why these coefficients give a syzygy

Let $a=a_\circ$, $c=c_\circ$, and $n=n_\circ$. The polynomial


$$
J(y)=\sum_{i=0}^{n}J_i y^i
$$


has the exact coefficient vanishing


$$
\boxed{
[y^{n+1}],\ldots,[y^{2n}]
\quad\text{of}\quad (1-y)^cJ(y)
\quad\text{all equal zero}.
}
\tag{5.6}
$$



One direct derivation uses the formal Rodrigues expression


$$
\frac{y^a}{n!(1-y)^c}
\frac{d^n}{dy^n}
\left(y^{n-a}(1-y)^{n+c}\right).
$$


Its coefficient of $y^i$ is $(-1)^nJ_i$, by the binomial convolution identity. For $0\le u<n$, the coefficient at $y^{a-1-u}$ after multiplication by $(1-y)^c$ is a formal residue of


$$
y^u\frac{d^n}{dy^n}
\left(y^{n-a}(1-y)^{n+c}\right).
$$


Formal integration by parts makes it zero because $d^n(y^u)/dy^n=0$. This proves (5.6) over the integers.

After homogenization, (5.6) says


$$
X^{a_\circ}U_\circ
+Y^{c_\circ}V_\circ
+Z_h^{c_\circ}W_\circ=0,
\tag{5.7}
$$


where $W_\circ$ is the homogeneous form corresponding to $J^\flat\bmod3$. The other two components are obtained by the exact low/high coefficient split in (5.6).

Division by $3^{\nu_\circ}$ is valid for the whole syzygy: divisibility of $J$ implies the same divisibility of the product and of both quotient pieces.

The total degree is $d_\circ$, the proved minimal degree. Hence the resulting syzygy is primitive and spans the complete minimal syzygy line.

### 5.4 The endpoint does not vanish on this minimal coefficient

This is the crucial endpoint step.

Consider the involution


$$
\iota(X,Y)=(-X,Y-X).
\tag{5.8}
$$


It sends


$$
X^{a_\circ}\mapsto(-1)^{a_\circ}X^{a_\circ},
\qquad
Y^{c_\circ}\longleftrightarrow Z_h^{c_\circ}.
$$


Because the minimal syzygy line is one-dimensional, applying $\iota$, with the corresponding interchange of the last two components, multiplies the minimal syzygy by a nonzero scalar.

At the point


$$
p=(-1,1),
$$


one has


$$
\iota(p)=-p.
$$


The last two components have the same homogeneous degree $n_\circ$. Therefore


$$
W_\circ(p)=0\quad\Longrightarrow\quad V_\circ(p)=0.
$$


Equation (5.7), whose three forms are all nonzero at $p$, would then give


$$
U_\circ(p)=0.
$$


All three components would have the common linear factor $X+Y$, contradicting primitivity.

Thus


$$
\boxed{W_\circ(-1,1)\ne0.}
\tag{5.9}
$$



Normalize the minimal coefficient by this ternary unit, so that its dehomogenization $W_\circ(y)$ satisfies


$$
W_\circ(-1)=1.
\tag{5.10}
$$


This normalization uses only a unit and involves no unknown original endpoint residue.

### 5.5 Frobenius transport to the original triple

Use the differences (4.5), and put


$$
\alpha=\max(d_a,0),\qquad
\beta_+=\max(d_b,0),\qquad
\gamma_+=\max(d_c,0),
$$




$$
\gamma_-=\max(-d_c,0).
\tag{5.11}
$$


Raise (5.7) to the $\mathfrak q$-th power and multiply by


$$
X^\alpha Y^{\beta_+}Z_h^{\gamma_+}.
$$


This produces a syzygy of the original triple. Its third component is


$$
X^\alpha Y^{\beta_+}Z_h^{\gamma_-}
W_\circ(X,Y)^{\mathfrak q}.
\tag{5.12}
$$



Its total syzygy degree is


$$
\mathfrak qd_\circ+\alpha+\beta_++\gamma_+
=
\frac{a_H+b_H+c_H-g_*}{2}
=d_1.
\tag{5.13}
$$


Thus it is a minimal syzygy, not merely a higher-degree relation.

Dehomogenize:


$$
\boxed{
W_2(y)=
y^\alpha(1-y)^{\gamma_-}W_\circ(y^{\mathfrak q}).
}
\tag{5.14}
$$


Its degree is at most


$$
d_1-c_H=\chi-1-k_2=\delta-k_2.
\tag{5.15}
$$



### Theorem 5.1 — Complete remaining-range radical and endpoint

In the remaining range,


$$
\boxed{
\ker\mathsf D
=
W_2(y)\,\mathbb F_3[y]_{<k_2}.
}
\tag{5.16}
$$


Moreover,


$$
\boxed{
W_2(-1)=(-1)^{\alpha+\gamma_-}\ne0.
}
\tag{5.17}
$$



#### Proof

At total degree $3\chi-2$, the second syzygy generator contributes nothing. Every syzygy is therefore a homogeneous multiplier of degree $k_2-1$ times the minimal syzygy (5.12). Its third components are exactly (5.16).

Equation (5.17) follows from (5.10), the oddness of $\mathfrak q$, and $2=-1$ in $\mathbb F_3$. ∎

This evaluates the needed endpoint hypothesis on the **complete** second radical.

---

## 6. Complete kernel and rank of the actual annihilator form

For all ranges, choose $W_2$ as follows:


$$
\begin{array}{c|c|c}
\text{range}&k_2&W_2\\ \hline
\mathrm I&\delta&1\\
\mathrm {II}&\delta-B_1&1\\
\mathrm {III}&\varepsilon&(1-y)^{\Pi-2\chi}\\
\mathrm {IV}&\text{formula \((4.8)\)}&\text{formula \((5.14)\)}.
\end{array}
\tag{6.1}
$$


Then, in every range,


$$
\ker\mathsf D=W_2\mathbb F_3[y]_{<k_2},
\qquad W_2(-1)\ne0.
\tag{6.2}
$$



The actual endpoint on these complete radical generators is


$$
\boxed{
\overline f\bigl(\mathcal G[W_2y^i]\bigr)
=\sigma W_2(-1)(-1)^i\ne0,
\qquad 0\le i<k_2.
}
\tag{6.3}
$$


This is the original actual endpoint (1.6), not a freely selected primitive functional.

### Theorem 6.1 — Complete actual second-radical annihilator

The actual leading endpoint-annihilating form has


$$
\boxed{
\operatorname{rank}\mathsf H_+=\delta-k_2,
\qquad
\operatorname{nullity}\mathsf H_+=k_2-1.
}
\tag{6.4}
$$


In the $h_u$-coordinate polynomial space its complete kernel is


$$
\boxed{
\ker\mathsf H_+
=
W_2(y)\mathbb F_3[y]_{<k_2-1}.
}
\tag{6.5}
$$



In the original amplitude space, its complete radical is


$$
\boxed{
(1-y)^{2\chi}y^{L_*}(1+y)W_2(y)
\mathbb F_3[y]_{<k_2-1}.
}
\tag{6.6}
$$



#### Proof

The functional $p\mapsto\sigma p(-1)$ is nonzero on the complete radical (6.2). By the already established rank-preservation principle, restricting to its kernel preserves the rank of $\mathsf D$, and the new radical is its intersection with $\ker p(-1)$.

Since $W_2(-1)\ne0$,


$$
W_2q\in\ker p(-1)
\quad\Longleftrightarrow\quad
q(-1)=0
\quad\Longleftrightarrow\quad
q=(1+y)r.
$$


Passing through the coordinate map $r\mapsto(1+y)r$ gives (6.5)–(6.6). ∎

### 6.1 Saturated integer lifts and a unit complement

Lift the coefficients of the normalized $W_\circ$ to $0,\pm1$, and use the literal integer polynomial in (5.14). For Ranges I–III use the literal polynomials in (6.1).

Let $j_2$ be the least nonzero coefficient index of this $W_2$. Its coefficient there is $\pm1$. The columns


$$
W_2,\ yW_2,\ldots,y^{k_2-2}W_2
\tag{6.7}
$$


have a triangular coefficient block on rows


$$
j_2,\ldots,j_2+k_2-2
$$


with diagonal entries $\pm1$. Therefore they are saturated integer lifts.

An explicit complementary set in the $h$-coordinates is


$$
\boxed{
\{y^u:0\le u\le\delta-2\}
\setminus
\{y^{j_2},\ldots,y^{j_2+k_2-2}\}.
}
\tag{6.8}
$$


The corresponding full coefficient change has determinant $\pm1$. Since (6.5) is the complete radical, the restriction to (6.8) is nondegenerate over $\mathbb F_3$, hence a unit block over $\mathbb Z_3$ after its physical $3^5$ factor.

These are coordinate constructions in the retained finite amplitude lattice. They do not redefine the original column contents or the least simultaneous clearer.

### 6.2 A uniform source-specific obstruction to nonsingularity

The exact formulas imply that this new annihilator digit is never nonsingular on the original family.

A useful uniform bound is


$$
\boxed{k_2\ge242,\qquad \operatorname{nullity}\mathsf H_+\ge241.}
\tag{6.9}
$$



For the remaining range, use


$$
k_2=
\min\left\{
\frac{\mathfrak q-\Delta+\omega_*+5\epsilon_*}{4},
\frac{3\Delta-\mathfrak q+\omega_*-5\epsilon_*}{4}
\right\}.
\tag{6.10}
$$


Here $\mathfrak q\equiv2187\pmod{4374}$. If $\epsilon_*=1$, then


$$
\Delta\equiv3159\pmod{4374};
$$


if $\epsilon_*=-1$, then


$$
\Delta\equiv1215\pmod{4374}.
$$


The positive differences in (6.10) consequently give $k_2\ge242$.

In the other ranges, (1.2) gives respectively


$$
\delta\ge242,
$$




$$
\delta-B_1\equiv366\pmod{2187},
$$


and, in the two branches of Range III,


$$
\varepsilon\equiv728\quad\text{or}\quad852\pmod{2187}.
$$


Their positive values are at least $242$.

This is a genuine obstruction to a “the next annihilator digit is nonsingular” argument. It is not a primitive-denominator estimate.

---

## 7. Paid directional consequences

We now connect the new matrix to the actual directional force, rather than choosing an unrelated force after the rank calculation.

### 7.1 The leading force in the fixed first pivot frame

Normalize the first endpoint pivot so that its reduction in the $p$-coordinates is $\sigma$. In the basis consisting of this pivot and the $h_u$, the first returned matrix has the form


$$
3^5
\begin{pmatrix}
a_5&w_5^T\\
w_5&B_5
\end{pmatrix}.
$$


Its leading entries are


$$
\overline B_5=-\mathsf H_+,
$$




$$
\boxed{
(\overline w_5)_u
=
-\sigma[y^{\kappa_1-u}]
(1-y)^{2\chi}(1+y).
}
\tag{7.1}
$$


This is the actual mixed column of the returned original matrix.

In particular,


$$
(\overline w_5)_u=0
\quad\text{unless}\quad
u\equiv120,121\pmod{243}.
\tag{7.2}
$$


Also


$$
\boxed{\overline a_5=0,}
\tag{7.3}
$$


because $\kappa_1\equiv121\pmod{243}$, whereas $(1-y)^{2\chi}$ has support only in multiples of $243$.

### 7.2 An evaluated leading solution for this original force

Put


$$
N_2(y)=\frac{\sigma W_2(y)}{W_2(-1)}.
$$


Then $N_2\in\ker\mathsf D$, and its endpoint equals $1$. Since


$$
N_2(-1)=\sigma,
$$


the polynomial


$$
\boxed{
x_0(y)=\frac{\sigma-N_2(y)}{1+y}
}
\tag{7.4}
$$


belongs to the actual $h$-coordinate space.

The leading mixed equation is solved by


$$
\boxed{\overline B_5x_0=\overline w_5.}
\tag{7.5}
$$


Indeed, $N_2$ is the first pivot plus an endpoint-annihilating vector and is in the complete radical of $\mathsf D$. Pairing it with every $h_u$ gives exactly (7.5), with the sign in (7.4).

Examples include:

- Ranges I–II: $W_2=1$, so $x_0=0$.
- Range III:
  

$$
x_0=
  \sigma\frac{1+(1-y)^{\Pi-2\chi}}{1+y}
  \quad\text{in }\mathbb F_3[y].
$$



Thus the actual leading force is not merely known to satisfy an abstract compatibility condition; a source-specific solution is displayed.

### 7.3 The additional exact adapted elimination

Use the exact lift of the endpoint-unit complete second-radical vector $N_2$, normalized to exact endpoint $1$. Its difference from the old pivot lies in the exact endpoint kernel.

Choose the new complement inside that kernel, using (6.8), and lift the complete radical (6.6). The archived adapted-complement theorem now applies at $k=5$, because its endpoint hypothesis has been proved in §6.

The blocks satisfy


$$
A_5=3^5A_{5,0},\qquad
A_{5,0}\in\operatorname{GL}_{\delta-k_2}(\mathbb Z_3),
$$




$$
X_5\in3^6M.
$$


Therefore


$$
\boxed{
A_5^{-1}=3^{-5}A_{5,0}^{-1},
\qquad
X_5^TA_5^{-1}X_5\in3^7M.
}
\tag{7.6}
$$


The retained matrix has dimension $k_2$ and belongs to $3^6M$.

The endpoint remains exactly $e_0$, and the complete current diagonal remains exactly the same $\lambda$. This does not erase any previously incurred $1/3$ or $1/9$ return.

Consequently the actual matrix has:

- exactly $R+1-\delta$ elementary divisors of valuation $4$;
- exactly $\delta-k_2$ elementary divisors of valuation $5$;
- all remaining elementary divisors of valuation at least $6$, or zero.

The count $\delta-k_2$ is now evaluated in every original range.

---

## 8. The complete border, $\lambda$, and the $3^{-1}$ directional allowance

The complete endpoint and diagonal are retained as


$$
f_{\mathrm{act}}^{(2)}
=f_{\mathrm{act},K}
-3L_{\mathrm{act}}B_{\mathrm{act}}^{-1}f_{\mathrm{act},J},
$$




$$
\lambda_{\mathrm{act}}^{(2)}
=\lambda_{\mathrm{act}}
-\frac13f_{\mathrm{act},J}^TB_{\mathrm{act}}^{-1}f_{\mathrm{act},J},
$$




$$
f_{\mathrm{act},\mathrm{new}}
=G_0^Tf_{\mathrm{act}}^{(2)}
-3M_{b,\mathrm{act}}^TA_{b,\mathrm{act}}^{-1}f_{\mathrm{act},b},
$$




$$
\boxed{
\lambda
=\lambda_{\mathrm{act},\mathrm{new}}
=\lambda_{\mathrm{act}}^{(2)}
-\frac19f_{\mathrm{act},b}^TA_{b,\mathrm{act}}^{-1}f_{\mathrm{act},b}.
}
\tag{8.1}
$$



For the scalar estimates below, use the retained complete-border normalization


$$
\lambda=\eta/3,\qquad \eta\in\mathbb Z_3^\times.
\tag{8.2}
$$


The elementary H2 valuation of $\lambda^{(2)}$, by itself, would not authorize deleting the $1/9$ term in (8.1). No such deletion is made. The matrix and endpoint theorems above do not require the numerical value of $\eta$.

### 8.1 Exact endpoint-pivot inverse

Suppose the current matrix is


$$
3^k
\begin{pmatrix}
\alpha&w^T\\
w&B
\end{pmatrix},
\qquad f=e_0.
$$


The endpoint-pivot block of the complete bordered matrix is


$$
P_{\mathrm{ep}}=
\begin{pmatrix}
\lambda&1\\
1&3^k\alpha
\end{pmatrix}.
$$


Put


$$
u=1-3^k\lambda\alpha.
$$


Then, exactly,


$$
\boxed{
P_{\mathrm{ep}}^{-1}
=
\begin{pmatrix}
-3^k\alpha/u&1/u\\
1/u&-\lambda/u
\end{pmatrix}.
}
\tag{8.3}
$$


The $-\lambda/u$ entry has valuation $-1$; the physical inverse is not being treated as wholly integral.

The Schur complement is


$$
3^k B^\sharp,
$$


where


$$
\boxed{
B^\sharp=B+\frac{3^k\lambda}{u}ww^T.
}
\tag{8.4}
$$


At the original $k=4$ normalization, this is precisely


$$
B^\sharp=B+\frac{27\eta}{u}ww^T,
\qquad u=1-27\eta\alpha.
$$



At the first new radical normalization $k=5$, the border correction starts at physical valuation $9$. At the next normalization $k=6$, it starts at physical valuation $11$.

Thus:

- the matrix digits at physical valuations $5,6,7,8$ after the first adapted reduction require only the valuation of $\lambda$, not its unit value;
- the numerical residue of $\eta$ can first enter that border matrix return at physical valuation $9$;
- this observation does not protect the $3^6$ digit from endpoint-lift and complementary-matrix returns.

### 8.2 The rank-one border does not create a new $3^{-1}$ solvability obstruction

For the actual integral $\alpha,w,B$, and $k\ge4$,


$$
\boxed{
B^\sharp v=w,\quad v\in3^{-1}\mathbb Z_3^s
\quad\Longleftrightarrow\quad
Bx=w,\quad x\in3^{-1}\mathbb Z_3^s.
}
\tag{8.5}
$$



To prove this, put $c=3^k\lambda/u$, so $v_3(c)\ge3$.

If $Bx=w$, then


$$
v=\frac{x}{1+c\,w^Tx}
$$


satisfies $B^\sharp v=w$. The denominator is a unit because


$$
c\,w^Tx\in3^2\mathbb Z_3.
$$


Conversely, from $B^\sharp v=w$,


$$
Bv=(1-c\,w^Tv)w,
$$


and the factor on the right is again a unit. Division gives the required $x$.

The exact value of $\lambda$ determines the exact scalar in this conversion, but its valuation suffices for the existence of a solution with the stated denominator allowance.

### 8.3 Pivot changes and complement elimination preserve that allowance

An exact endpoint-pivot change


$$
v_{\mathrm{pivot}}\mapsto
v_{\mathrm{pivot}}+H t,\qquad t\in\mathbb Z_3^s,
$$


changes the unbordered force from $w$ to $w+Bt$. Thus


$$
Bx=w
\quad\Longleftrightarrow\quad
Bx'=w+Bt,\qquad x'=x+t.
$$


The condition $x\in3^{-1}\mathbb Z_3^s$ is unchanged.

For a paid complementary elimination,


$$
B_{\mathrm{phys}}=
\begin{pmatrix}A&X\\X^T&V\end{pmatrix},
\qquad
c_{\mathrm{phys}}=\binom{c_C}{c_R},
$$


with


$$
A=3^kA_0,\qquad
X,c_C\in3^{k+1}M,
$$


the eliminated coordinates are


$$
x_C=A^{-1}(c_C-Xx_R).
$$


If $x_R\in3^{-1}\mathbb Z_3$, then $x_C$ is integral. The exact retained equation is


$$
\boxed{
(V-X^TA^{-1}X)x_R
=
c_R-X^TA^{-1}c_C.
}
\tag{8.6}
$$


Both the matrix and force returns in (8.6) are retained. Their valuations are at least $k+2$.

Applying this at $k=4$ and then $k=5$ proves the following paid directional reduction.

### Theorem 8.1 — Paid original directional reduction through the new layer

After the two exact endpoint-adapted complements, the original problem


$$
B^\sharp v=w,\qquad v\in3^{-1}\mathbb Z_3^{\,R},
$$


is equivalent, by the explicit unit and paid transformations above, to an equation


$$
\boxed{
B_6x=w_6,\qquad
x\in3^{-1}\mathbb Z_3^{\,k_2-1},
}
\tag{8.7}
$$


where $B_6,w_6$ are the actual matrix and mixed force obtained from the retained $3^6$ block.

They are not freely chosen data. They include the complete producer, the exact endpoint lifts, the first adapted-complement return, and all earlier returns.

Equation (7.4) evaluates the leading pivot adjustment that makes this reduction possible. The existence of the additional exact adapted elimination is now proved on every sufficiently large original index.

The remaining equation (8.7) is not solved in this report.

---

## 9. What remains active at the next digit

The exact core identity being reused is


$$
\begin{aligned}
T_{c,\mathrm{red}}
={}&-\frac{G_c(\mathcal F,\mathcal F)}{3^{26}}
-81Z^T\mathsf A Z\\
&-27G^TL_cB_c^{-1}L_c^TG
-81M_{b,c}^TA_{b,c}^{-1}M_{b,c}.
\end{aligned}
\tag{9.1}
$$


A1 Turn 6 pays the $3^5$ digit of its double-radical contraction. A3 Turn 7 pays the actual/core comparison (1.5).

At $3^6$, the following can be active:

- the next complete moment coefficient;
- the second-prefix contraction divided by $9$;
- the first $J$-return divided by its additional $3$;
- the rank-$b$ return with its physical $3^{-2}$ inverse;
- the first $3^{-4}$ complementary return;
- the changes caused by higher exact endpoint lifts.

The new $3^{-5}$ complementary return starts only at $3^7$, but this does not remove the earlier $3^6$ terms.

A concrete next local obligation is therefore:

> **Actual $3^6$ directional lemma.** Evaluate the actual returned $B_6$ and $w_6$, including the higher endpoint lifts and all active $3^6$ returns, and decide whether the paid equation (8.7) has a solution.

A finite necessary test for (8.7) is explicit. Write $z=3x$; then


$$
B_6z=3w_6.
$$


Modulo $9$, with $z=z_0+3z_1$, one must have


$$
\overline B_6\,\overline z_0=0,
$$


and


$$
\overline B_6\,\overline z_1+
\overline{\frac{B_6z_0}{3}}
=\overline w_6.
\tag{9.2}
$$


The division in (9.2) is paid by the first congruence. Thus a nonzero cokernel class of $\overline w_6$ outside the image of the induced divided map on $\ker\overline B_6$ would be an original directional obstruction.

This is a specified next test on the actual returned force, not a replacement by an arbitrary diagonal or endpoint.

---

## 10. Global normalization and the unchanged irrationality objective

No new global content division is asserted.

The local saturated bases and ternary-unit normalizations do not replace the actual column contents or the least simultaneous clearer $\ell_{\mathrm{clr}}$. The complete source recurrence remains


$$
\mu_{t+1}+\mu_t
=
\frac{3^h}{2t+1}
-\frac{3^h}{4}\bigl((2t+2)!+(2t)!\bigr),
\qquad 0\le t\le2n-2,
$$


with its genuine resonance


$$
t_*=\frac{3^h-5}{2}.
$$


The associated $3^h$ division is not removed by this local analysis.

Retain the actual integers


$$
A_\ell=\ell_{\mathrm{clr}}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\mathrm{clr}}^{m+1}\beta_1,
$$


and the gcd over **all primes**


$$
\boxed{g_\ell=\gcd(|A_\ell|,|B_\ell|).}
$$


For $B_\ell\ne0$, the actual primitive denominator and numerator are


$$
\boxed{
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
}
\tag{10.1}
$$



The whole error is exactly


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\mathrm{clr}}^{m+1}}
{g_\ell}\det H_{\mathrm{complete}}.
}
\tag{10.2}
$$



An irrationality proof would follow from


$$
B_\ell\ne0,\qquad
\det H_{\mathrm{complete}}\ne0,
$$


and


$$
\boxed{
\log g_\ell-(m+1)\log\ell_{\mathrm{clr}}
-\log|\det H_{\mathrm{complete}}|
\longrightarrow+\infty
}
\tag{10.3}
$$


at the **same infinite original indices**.

Indeed, these conditions make the nonzero whole errors tend to zero. If $e+\pi=a/b$ were rational, every nonzero error $q(e+\pi)-p$ would have absolute value at least $1/b$.

This remains a conditional implication. The local Smith counts proved here do not establish growing savings in the final primitive denominator. Common determinant factors can occur in both distinguished cofactors and disappear under the final all-prime gcd.

---

## 11. Bounded exact-arithmetic receipt

No tool computation was performed. No closed pole calculation, terminal constant, dense original determinant, or previously completed content calculation needs to be repeated for the proofs above.

An optional bounded receipt checks the first nontrivial instances of the new auxiliary coefficient construction.

### Inputs

Work over the integers and then reduce modulo $3$. Use


$$
(a_\circ,c_\circ)=(1,1),(1,2),(5,4),(5,5),
$$


and formula (5.3).

### Expected outputs



$$
\begin{array}{c|c|c|c}
(a_\circ,c_\circ)&(J_0,\ldots,J_{n_\circ})&
\nu_\circ&W_\circ(y)\pmod3\\ \hline
(1,1)&(1)&0&1\\
(1,2)&(1)&0&1\\
(5,4)&(6,6,3)&1&2+2y+y^2\\
(5,5)&(6,9,6)&1&2+2y^2
\end{array}
$$


All four displayed $W_\circ$ have value $1$ at $y=-1$.

The two nontrivial product vectors should be


$$
(1-y)^4(2+2y+y^2)
\equiv
2+2y^2+y^5+y^6,
$$




$$
(1-y)^5(2+2y^2)
\equiv
2+2y+y^2+2y^5+y^6+y^7.
$$


In both cases the coefficients at $y^3,y^4$ vanish.

The corresponding $2\times3$ selected coefficient matrices have rank $2$; for example, their first two columns have determinants $1$ and $2$, respectively.

This receipt has degree at most $7$. It verifies only those bounded constants. The uniform original-family result follows from the graded-map, largest-scale, Rodrigues, and symmetry proofs, not from extrapolating these examples.

For a future finite check of (9.2), the coordinator would need to supply a particular admissible original index and the actual returned data at the required precision. A conservative sufficient input specification is $T_{\mathrm{act},\mathrm{red}}\bmod3^8$ and the actual endpoint modulo $3^4$, together with the fixed finite bases. The expected output is the literal returned $B_6\bmod9$, $w_6\bmod3$, and either a certificate for (9.2) or an explicit cokernel obstruction. That calculation is not claimed to have been performed, and a successful finite check would establish only its finite scope.

---

## 12. Conclusion

### New proved statements

On the same sufficiently large original indices:

1. The actual endpoint-annihilating $3^5$ operator is
   

$$
\boxed{
   -\left(
   [y^{(P/3-1)/2-u-v}]
   (1-y)^{2\chi}(1+y)^2
   \right)_{0\le u,v<\delta-1}.
   }
$$



2. The previously unresolved full divided-radical rank is evaluated by
   

$$
\boxed{
   k_2=
   \frac{|4\chi-\Pi|+\omega_*
   -|2|4\chi-\Pi|-\mathfrak q-5\epsilon_*|}{4},
   }
$$


   with $\mathfrak q,\omega_*,\epsilon_*$ defined in §4.

3. A complete radical, saturated integer lifts, and a unit complement are constructed in every range.

4. The actual endpoint is nonzero on the **complete** second radical in every range. Hence
   

$$
\operatorname{rank}\mathsf H_+=\delta-k_2,\qquad
   \operatorname{nullity}\mathsf H_+=k_2-1\ge241.
$$



5. An additional exact endpoint-adapted elimination is paid:
   

$$
\text{inverse cost }3^{-5},\qquad
   \text{new matrix return in }3^7M,
$$


   with no new endpoint or diagonal Schur return.

6. The original $3^{-1}$-allowed directional problem is reduced to the actual $3^6$ residual equation (8.7). Its leading force adjustment is explicitly evaluated by (7.4).

### Exact remaining bottlenecks

The next local bottleneck is the **actual returned $3^6$ matrix and force**, including higher endpoint lifts and all earlier returns that first become active there. The complete diagonal is retained exactly; its numerical unit is not needed merely to preserve the directional denominator allowance.

The global bottleneck remains same-index nonvanishing and decay of the **whole** error after the actual contents, least simultaneous clearer, all-prime gcd, and primitive denominator are used.



$$
\boxed{
\text{No unconditional proof of rationality or irrationality of }e+\pi
\text{ is obtained.}
}
$$


