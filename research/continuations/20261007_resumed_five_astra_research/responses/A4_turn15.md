> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of A1 Turn 14 and A5 Turn 8

## Executive conclusions

**Neither report proves that $e+\pi$ is rational or irrational.** The new local theorems are nevertheless substantial, and their principal claims survive audit at the scopes specified below.

1. **A1’s nine-period producer annihilation is valid.** It uses the actual producer coefficients, the complete functional, all pole layers relevant modulo $27$, and the exact complete-core corrected columns. Its transfer to
   

$$
G^T(S_{\rm act}-S_c)G\in3^{30}M
$$


   is correctly paid.

2. **A1’s finite terminal inverse direction and first returns are valid.**
   

$$
\bar B^{-1}\delta_J=-e_0,\qquad
   \delta_J^T\bar B^{-1}\delta_J=0,
$$


   but
   

$$
\delta_J^T\bar B^{-1}\bar f_J=-\varepsilon_0
$$


   is a unit. Thus the quadratic matrix return disappears at the stated digit, while the endpoint and diagonal returns do not.

3. **H2 is already accepted.** A1’s repeated “pending” designation is outdated. Its rank, radical, endpoint, and complete-diagonal consequences may be used at the original scope validated in A4 Turn 12.

4. **A further original-object boundary calculation closes A1’s proposed boundary-column lemma.** On the same sufficiently large original subfamily,
   

$$
(\bar L_ce_0)_u
   =[y^{E-\ell-u}](1-y)^{-b},
   \qquad 0\le u<\ell,
$$


   and therefore
   

$$
G^T\bar L_ce_0=0.
$$


   Consequently the complete first matrix return, not merely its direct producer part, satisfies
   

$$
\boxed{
   G^T\bigl(\mathcal S^{(2)}_{\rm act}
             -\mathcal S^{(2)}_c\bigr)G\in81M.
   }
$$


   The endpoint and diagonal differences remain active.

5. **A1’s resonant recurrence obstruction is valid.** At an actual moment index within the original finite range, solving for the highest moment requires division by $3^h$, and the recurrence coefficients have no common factor $3$ that removes that cost. This obstructs an *unpaid uniformly stable forward solve*, not the desired directional inverse bound itself.

6. **A5’s complete binomial-divisibility theorem is valid.**
   

$$
\boxed{
   v_2(S)\ge 1+\chi,\qquad
   \chi=v_2\binom{n+b-1}{b-1}.
   }
$$


   The potentially large head denominators $n+r$ are canceled by the actual force recurrence. The whole finite exterior/Schur return has the same divisor. The small $\lambda_k$ exceptions are correctly handled.

7. **A5’s variable precision is admissible at every original index.** An explicit bound below verifies the hypotheses for
   

$$
L=\max(2,\chi+1);
$$


   an asymptotic assertion $L=O(\log n)$ is not needed.

8. **The supplied $u=0$ certificate can now be promoted to an unconditional finite consequence of the accepted theorem.**
   

$$
\chi(0)=27,\qquad A_{\rm end}(0)=21,
$$


   hence
   

$$
v_2(S(0))\ge28,\qquad
   v_2\!\left(\frac{S(0)}{2^{a(0)+1}}\right)\ge6,
   \qquad Q(0)\equiv0\pmod2.
$$


   Reusing the stronger previously accepted witness $a(0)\le10$ improves the paid linear bound to $17$. This does **not** imply $2^{17}\mid Q(0)$.

9. **The infinite binary conclusions remain carefully separated.** Unbounded raw divisibility is proved on specified original residue classes. Positive paid excess on infinitely many original indices is not proved.

No closed modulo-$8$ calculation, original dense producer calculation, completed finite certificate, or depth-$12$ Schur solve is repeated here.

---

# 1. Scope and accepted dependencies

The two constructions use different original index families. They are not combined.

## 1.1 Ternary family

Retain


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




$$
m=2^{2j-1},\qquad n=4^j+1=2m+1,\qquad A=n-2,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$


and the original window


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$



The finite coordinates remain


$$
U_u=(y-1)^u\quad(0\le u<D),
$$




$$
z_i=(y-1)^Dy^i\quad(0\le i<\nu),
\qquad \nu=D/2-1,
$$




$$
Y_a=y^a\quad(d\le a\le m),
\qquad d=D+\nu.
$$


The physical HIGH terminal is $Y_m$.

For A1 Turn 14 retain the fixed interior window


$$
\frac{103}{1000}<\rho=\frac{N_0}{P_0}<\frac{104}{1000},
$$


with


$$
P_0=243P=3^{h-27},\quad N_0=243r,\quad D=P_0+N_0,
$$




$$
P=3^{h-32},\qquad r\equiv2\pmod9,\qquad r\ \text{odd},
$$




$$
4^j=243(3^{26}-1)P-243r+1.
$$



The accepted density theorem supplies infinitely many **original** indices in this fixed window. It does not authorize replacing $(j,h)$ by arbitrary auxiliary pairs $(P,r)$.

Put


$$
Q=P_0/9,\qquad b=Q-N_0,\qquad
\ell=3b/2+1,
$$




$$
R_*=(P_0+1)/2,\qquad
\tau=(N_0-3)/2,\qquad
n_J=\tau-\ell=\frac{Q-4b-5}{2}.
$$


Then


$$
K=\{0,\ldots,\ell-1\},\qquad
J=\{\ell,\ldots,\tau-1\}.
$$



On this window,


$$
\boxed{\frac{64}{1000}<\frac bQ<\frac{73}{1000}.}
\tag{1.1}
$$


In particular all strict inequalities used below have growing positive margins.

### Accepted ternary dependencies

The following are reused at their previously proved sufficiently-large original scope:

- the integral unimodular complete-core basis and exact orthogonality;
- the precision-$20$ corrected-column representatives, their degree gap, and their support bounds;
- the original inverse bounds $E_c^{-1},E_{\rm act}^{-1}\in3^{-1}M$;
- the exact perturbation identity and first producer return;
- the finite prefix and first-radical blocks;
- **H2, including the full second radical and the complete diagonal valuation**;
- the endpoint-adapted rank-$b$ elimination and its $3^{-2}$ payment.

## 1.2 Binary family

Retain


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
$$


Contact indices are $0\le i,j<b$; physical reconstruction has $0\le j\le b$.

Write


$$
h=n/2,\qquad d=(b-1)/4,\qquad g=(n+2)/4,
$$




$$
W_j=\binom{n+2}{j},\qquad
\Delta_jz=jz_{j-1}-z_j,\qquad z_{-1}=z_b=0.
$$



The complete columns remain


$$
x=\frac12\mathcal RA^{-1}\mathfrak f,\qquad
y=\frac{\mathcal RA^{-1}(h^e+h^F)+e_0}{4b!}.
$$


The logarithmic force $h^F$ is not removed.

Retain


$$
z^f=A^{-1}\mathfrak f,\qquad x=2^ax_0,
\qquad
a=\min_{0\le j\le b}v_2(x_j).
$$



The old conclusions retained without recalculation are:

- $a\ge1$ universally;
- the exact endpoint valuation
  

$$
v_2(x_{b-1})=A_{\rm end}:=v_2\binom gd;
$$


- the complete force recurrence and force modulo $8$;
- the finite short adjoint and finite Schur completion;
- $a\ge2$ on $u\equiv1\pmod4$;
- the complete exponential-source result $E\in2\mathbb Z_2$, at its stated channel and guard scope;
- the coprimality of the actual all-prime column contents.

A5 Turn 8’s “pending review” labels for these already accepted results are outdated.

---

# 2. Audit of A1’s complete mixed observation

## 2.1 Complete functional and actual source

Set $x=y-1$. The functional is exactly


$$
\mathcal M(P)=
-\frac{3^h}{4}\mathfrak f(P)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](P-P(-1))/(y+1)}{2v+1},
\qquad \mathfrak f(y^t)=(2t)!,
$$


on $\deg P\le2n-1$.

Its largest pole denominator is


$$
4n-3=4H-4D+5<3^{h+1}.
$$


Thus $3^h$ pays every ternary pole denominator, and


$$
\mathcal M(\mathbb Z_3[y]_{\le2n-1})\subseteq\mathbb Z_3.
\tag{2.1}
$$



The source remains


$$
Q_{\rm act}=Q_c+3^7\mathscr R,
\qquad
Q_c=(y+1)x^A(\beta+3y),\quad \beta=-71-A,
$$


where


$$
3^7\mathscr R=\sum_{a=0}^{A+1}e_ax^a,\qquad
e_a=-\frac{(A+1)!}{a!}(t_a+\xi v_a),
$$


and


$$
t=3nh_{\rm vec}
 +(b_{\rm force}+6)e_{n-1}
 +\frac{2b_{\rm force}}{n-1}e_{n-2},
\qquad b_{\rm force}=-n-66.
$$


The signed scalar $\xi$ retains its previously paid normalization.

The complete return also remains


$$
J^T\varepsilon+\omega
=-\varepsilon-s_{\rm ret}
  \left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
\tag{2.2}
$$



## 2.2 Producer cutoffs and their divisions

With $F=(A+1)!=(n-1)!$, the endpoint charge is


$$
\mathscr R(-1)=-\frac{\xi F^2}{3^7}.
$$


Since $\xi$ is a unit,


$$
v_3(\mathscr R(-1))
=2v_3(F)-7
=n-8-s_3(n-1).
\tag{2.3}
$$


It exceeds every fixed precision used here on sufficiently large original indices.

Define


$$
D_{\rm prod}=\frac{\mathscr R-\mathscr R(-1)}{y+1},
\qquad
B_1=\frac{D_{\rm prod}-\kappa x^A}{3}.
$$


The first division is monic; the second is paid by the accepted producer reset.

For $a\le A-10$,


$$
v_3(F/a!)\ge5+v_3(9!)=9.
$$


After the original division by $3^7$, this gives


$$
[x^a]\mathscr R\in9\mathbb Z_3.
$$


Because $x+2$ is invertible relative to the factor $x$ modulo $9$, division by $y+1=x+2$ preserves the asserted low-coefficient vanishing. Hence


$$
\bar B_1=\sum_{k=0}^{9}\eta_kx^{A-k}.
\tag{2.4}
$$


The ten coefficients are actual producer coefficients, with the complete numerator


$$
\eta_k=
\overline{
\frac{
\sum_{a=A-k+1}^{A+1}(-2)^{a-A+k-1}e_a
-3^7\kappa\mathbf1_{\{k=0\}}
}{3^8}
}.
\tag{2.5}
$$


There is no termwise unpaid division.

Similarly, for $a\le A-55$,


$$
v_3(F/a!)\ge5+v_3(54!)=31.
$$


Thus


$$
\mathscr R\equiv
(y+1)x^{A-54}q_{24}(x)\pmod{3^{24}},
\qquad \deg q_{24}\le54.
\tag{2.6}
$$



**Decision:** both cutoffs and all associated divisions are valid.

## 2.3 All pole layers modulo $27$

For a nonterminal middle index $i\le\nu-2$, the accepted exact-column jet is


$$
F_i\equiv x^D(y^i-9y^{H/3+i})\pmod{27}.
$$


Consequently, for integral $\deg\Delta\le m$, the endpoint-zero quotient is


$$
\kappa x^Hy^i\Delta
+3B_1x^Dy^i\Delta
-9\kappa x^Hy^{H/3+i}\Delta
\pmod{27}.
\tag{2.7}
$$


All terms stay within the original functional cutoff.

Let


$$
r_H=(H-1)/2.
$$


The identity $m+\nu=r_H$ gives


$$
i+m\le r_H-2.
\tag{2.8}
$$



The complete surviving pole layers are:

- denominator $3H$, weight valuation $0$;
- denominator $H$, weight valuation $1$;
- denominators
  

$$
H/3,\quad5H/3,\quad7H/3,\quad11H/3,
$$


  weight valuation $2$.

At $3H$, only the upper $y^H$ term of the last summand of (2.7) contributes. Its contribution is


$$
-9\kappa[y^{(H/3-1)/2-i}]\Delta.
$$


At $H$, the identity


$$
x^H\equiv y^H-1+3y^{H/3}-3y^{2H/3}\pmod9
$$


produces the opposite contribution.

At $H/3$ and $7H/3$, the two leading-source contributions cancel modulo $27$, since $7^{-1}\equiv1\pmod3$. The other two weight-$9$ extractions are excluded by (2.8).

The factorial part is zero modulo $27$ because its retained prefactor is $3^h$, not because it has been deleted from the source.

Therefore


$$
\boxed{
\mathcal M(\mathscr R F_i\Delta)
\equiv
9[y^{r_H-i}]B_1x^D\Delta\pmod{27}.
}
\tag{2.9}
$$



This audit confirms that the cancellation needs the complete corrected jet and all four weight-$9$ poles.

---

# 3. Nine-period annihilation and precision-$30$ transfer

For $i=R_*+u$, $u\in K$,


$$
r_H-i-m=\tau-u\ge n_J+1.
$$


For sufficiently large original indices this is at least $9$.

Since $A+D=H$, the terms of $B_1x^D$ are $\eta_kx^{H-k}$. Below degree $H$,


$$
x^{H-k}
\equiv(-1)^{k+1}(1-y)^{-k}\quad(1\le k\le9).
$$


In characteristic $3$,


$$
(1-y)^{-k}=\frac{(1-y)^{9-k}}{1-y^9}.
$$


Define the evaluated numerator


$$
\mathcal B_9(y)=
\sum_{k=1}^9(-1)^{k+1}\eta_k(1-y)^{9-k},
\qquad \deg\mathcal B_9\le8.
$$


The $k=0$ term contributes nothing because the extraction is above $\deg\Delta$ and below $H$.

Equation (2.9) becomes


$$
\frac{\mathcal M(\mathscr R F_i\Delta)}9
\equiv
[y^{r_H-i\bmod9}]
\bigl(\mathcal B_9\bar\Delta\bmod(y^9-1)\bigr)
\pmod3.
\tag{3.1}
$$



Thus if


$$
g(y)=\sum_{u<\ell}g_uy^u,\qquad
\bar g\equiv0\pmod{y^9-1},
$$


then, for the **exact corrected combination**


$$
F_g=\sum_{u<\ell}g_uF_{R_*+u},
$$


one has


$$
\boxed{
\mathcal M(\mathscr R F_g\Delta)\in27\mathbb Z_3
\quad(\deg\Delta\le m).
}
\tag{3.2}
$$



The columns


$$
g_a=(y-1)^by^a,\qquad 0\le a\le b/2,
$$


have degree at most $\ell-1$, and are divisible modulo $3$ by


$$
y^9-1=(y-1)^9.
$$


They therefore lie in the original finite $K$-space and satisfy (3.2).

## 3.1 Model precision

Using (2.6) and the accepted representatives $F_i^*=x^D\psi_i$,


$$
\mathscr R F_i^*F_j^*
\equiv
(y+1)x^H
\bigl(x^{D-54}q_{24}\psi_i\psi_j\bigr)
\pmod{3^{23}}.
$$


The retained support envelope is


$$
\Omega_{20}\mathbb Z+[-21D,21D].
$$


At precision $23$,


$$
\Lambda_{23}=H/3^{22}=81P_0,\qquad
\Omega_{20}=27\Lambda_{23}.
$$


The binomial support of $x^H$ modulo $3^{23}$ lies on the $\Lambda_{23}$-grid: for $0<k<H$,


$$
v_3\binom Hk=h-1-v_3(k).
$$


Moreover,


$$
\frac{\Lambda_{23}}D=\frac{81}{1+\rho}>73,
$$


so


$$
21D<(\Lambda_{23}-1)/2.
$$


Every pole extraction that can survive lies on an odd half-grid and misses this support. Therefore


$$
\mathcal M(\mathscr R F_i^*F_j^*)\in3^{23}\mathbb Z_3.
\tag{3.3}
$$



## 3.2 Transfer to exact columns

Write


$$
F_g^*=F_g+3^{20}\Delta_g.
$$


The division is paid by the accepted congruence. Expanding the bilinear product, the two linear error terms gain $3^{20}\cdot27=3^{23}$ by (3.2); the quadratic term is paid by complete integrality. Hence


$$
\mathcal M(\mathscr R F_gF_h)\in3^{23}\mathbb Z_3.
$$



The exact perturbation formula is


$$
S_{\rm act}-S_c=3^7\Phi_{\mathscr R}-3^{13}\mathcal Q,
\qquad \mathcal Q\in3^{21}M.
$$


It gives


$$
\boxed{
G^T(S_{\rm act}-S_c)G\in3^{30}M,
}
\tag{3.4}
$$


or, for $U=-S/3^{26}$,


$$
G^T(U_{\rm act}-U_c)G\in81M.
$$



**Decision:** accepted. This is a fixed-depth direct-source improvement, not a primitive factor $3^b$.

---

# 4. Finite terminal inverse and complete first returns

After the unit-prefix elimination, retain


$$
\mathcal R_{\alpha,JJ}=3B_\alpha,\qquad
\mathcal R_{\alpha,KJ}=9L_\alpha,
\quad \alpha\in\{c,{\rm act}\}.
$$


The exact reductions are


$$
\mathcal S^{(2)}_\alpha
=\mathcal R_{\alpha,KK}
-27L_\alpha B_\alpha^{-1}L_\alpha^T,
\tag{4.1}
$$




$$
f^{(2)}_\alpha=f_{\alpha,K}
-3L_\alpha B_\alpha^{-1}f_{\alpha,J},
\tag{4.2}
$$




$$
\lambda^{(2)}_\alpha=\lambda_\alpha
-\frac13f_{\alpha,J}^TB_\alpha^{-1}f_{\alpha,J}.
\tag{4.3}
$$


The $3^{-1}$ inverse cost remains explicit.

## 4.1 Actual terminal direction

Reindex $J$ by $0,\ldots,n_J-1$. The accepted finite matrix is


$$
\bar B=-V,\qquad
V_{\alpha\beta}
=[y^{\alpha+\beta-(n_J-1)}](1-y)^{N_0}.
$$


Its first column is exactly $e_{n_J-1}$. Since the physical terminal direction is


$$
\delta_J=e_{n_J-1},
$$


one gets


$$
\boxed{\bar B^{-1}\delta_J=-e_0.}
\tag{4.4}
$$


For $n_J>1$,


$$
\boxed{\delta_J^T\bar B^{-1}\delta_J=0.}
\tag{4.5}
$$



With


$$
\varepsilon_0=(-1)^{R_*+\ell},
\qquad \bar f_{J,0}=\varepsilon_0,
$$


symmetry gives


$$
\boxed{\delta_J^T\bar B^{-1}\bar f_J=-\varepsilon_0.}
\tag{4.6}
$$



The zero in (4.5) and the unit in (4.6) are compatible. The terminal has not disappeared.

## 4.2 Matrix, endpoint, and diagonal differences

The accepted producer digit yields


$$
\bar L_{\rm act}
=\bar L_c+\bar\kappa\,\bar t_K\delta_J^T.
$$


The unit-prefix correction preserves the direct $81$-divisibility: its old prefix-to-$K$ block is in $3M$, its producer change is in $27M$, and the prefix inverse is integral.

Writing


$$
\widehat t=G^T\bar t_K,\qquad
\widehat l=G^T\bar L_ce_0,
$$


expansion of (4.1) gives


$$
\frac{
G^T(\mathcal S^{(2)}_{\rm act}-\mathcal S^{(2)}_c)G
}{27}
\equiv
\bar\kappa(\widehat t\widehat l^T+
            \widehat l\widehat t^T)
\pmod3.
\tag{4.7}
$$


The quadratic term is absent precisely because of (4.5).

For the other channels, the accepted difference bounds and the inverse expansion give


$$
\boxed{
f^{(2)}_{\rm act}-f^{(2)}_c
\equiv3\bar\kappa\varepsilon_0\bar t_K\pmod9,
}
\tag{4.8}
$$


and, with $u_0=\bar B^{-1}\bar f_J$,


$$
\boxed{
\lambda^{(2)}_{\rm act}-\lambda^{(2)}_c
\equiv-2\bar\kappa\varepsilon_0(\bar t_J^Tu_0)
\pmod3.
}
\tag{4.9}
$$



For example, the sign in (4.9) follows from


$$
B_{\rm act}-B_c
\equiv3\kappa(\delta_Jt_J^T+t_J\delta_J^T)\pmod9
$$


and


$$
B_{\rm act}^{-1}-B_c^{-1}
\equiv
-3\kappa B_c^{-1}
(\delta_Jt_J^T+t_J\delta_J^T)B_c^{-1}\pmod9.
$$


The outer factor $-1/3$ in (4.3) cancels the displayed $3$, leaving the contraction (4.6).

**Decision:** all three returning formulas are accepted.

---

# 5. New result: evaluation of the missing complete-core boundary column

This section proves the boundary lemma proposed, but not proved, in A1 Turn 14. It does **not** infer an extra column merely from the rank or radical in H2.

Let


$$
E=(Q-3)/2.
$$



## Theorem 5.1 — Actual first boundary column

On the same sufficiently large original subfamily,


$$
\boxed{
(\bar L_ce_0)_u
=[y^{E-\ell-u}](1-y)^{-b},
\qquad 0\le u<\ell.
}
\tag{5.1}
$$



### 5.1 Extending the corrected-column calculation by one actual column

The first column of $J$ has original index


$$
j_0=R_*+\ell.
$$


Since


$$
\nu-1=R_*+\tau-1,
$$


the condition $n_J\ge2$ gives


$$
j_0\le\nu-2.
\tag{5.2}
$$


Thus this is still a nonterminal column, with the same zero order-one jet and the same order-two jet used in the accepted H2 calculation.

Consider the slightly enlarged index set $0\le u,v\le\ell$. The low polynomial to which the accepted complete moment formula is applied has degree


$$
D+(R_*+u)+(R_*+v)+1
\le19Q+2b+4.
$$


This is at most $2D=20Q-2b$ for sufficiently large indices, because $4b+4<Q$ follows from (1.1).

The accepted corrected-column substitution remains paid by exact orthogonality:


$$
G_c(F^*,F^*)-G_c(F,F)\in3^{40}M.
$$


For the digit expansion:

- the order-one jet is zero;
- the order-two term uses the same shifted moment formula as H2;
- its remaining coefficient of $x^D$ lies strictly between $N_0$ and $P_0$, where that polynomial is zero modulo $3$;
- the order-three unit-pole exclusion remains valid by (5.2);
- the support inequalities remain strict, even allowing a bounded enlargement:
  

$$
\frac72D+3<\frac{9P_0-1}{2},\qquad
  4D+3<\frac{9P_0-1}{2};
$$


- higher-order grids grow as in the accepted calculation.

These inequalities follow directly from $D/P_0<1.104$. They verify the extra column in the original objects rather than postulating an extension of H2.

Consequently, on the required strip,


$$
(S_c)_{R_*+u,R_*+\ell}
\equiv G_c(z_{R_*+u},z_{R_*+\ell})
\pmod{3^{29}}.
\tag{5.3}
$$



### 5.2 The complete core extraction on the strip

For the enlarged set, the principal extraction index is


$$
k_{uv}=\frac{9Q-3}{2}-u-v.
$$


Its lower bound is


$$
k_{uv}\ge\frac{9Q-6b-7}{2}.
$$


Hence


$$
4Q-b<k_{uv}<6Q
$$


for sufficiently large original indices.

In the complete moment formula:

- the $a=1,3,5$ extractions are below the polynomial’s support;
- the $a=7$ extraction lies above $N_0$ and below $P_0$;
- the $a=11$ extraction lies in the same large gap;
- the $a=13$ extraction is above degree $D$.

The pertinent margin for the latter exclusions is


$$
Q/2-2b-O(1)>0.
$$


At the remaining extraction, only the band beginning at $4Q=4P_0/9$ survives after division by $9$. The accepted binomial digit therefore gives


$$
\boxed{
\frac{(S_c)_{R_*+u,R_*+\ell}}{3^{28}}
\equiv[y^{E-u-\ell}]x^{N_0}\pmod3.
}
\tag{5.4}
$$



### 5.3 The prefix-to-boundary digit

This part must also be checked; it is not supplied by the $K\times K$ form.

Let the prefix index be $0\le i\le a$, where


$$
a=(P_0-1)/2,\qquad J_0=P_0/3-1.
$$


At the needed precision, the same corrected-column estimates give the raw-core cross digit. The order-two correction already carries $3^2$, and its shifted moment is in $3^{26}\mathbb Z_3$; higher orders are paid by the support grids. Thus the comparison is valid modulo $3^{28}$.

For a residual index $R_*+v$, $0\le v\le\ell$, the leading extraction from $x^D$ is at


$$
P_0-1-i-v.
$$


It lies above $P_0/3+N_0$ and below $P_0$. Using


$$
x^{P_0}
\equiv y^{P_0}-1+3y^{P_0/3}-3y^{2P_0/3}\pmod9,
$$


only the band beginning at $2P_0/3$ can contribute. The weight-$3$ pole has negative extraction index, and the $3y$ part of the core is zero at this digit.

Since the normalized matrix is $U_c=-S_c/3^{26}$, the result is


$$
\boxed{
(\mathsf B_1)_{i,v}
=[y^{J_0-i-v}]x^{N_0},
\qquad 0\le v\le\ell.
}
\tag{5.5}
$$


This explicitly includes the first $J$-column.

### 5.4 The finite prefix correction is zero on the strip

The accepted prefix inverse is


$$
(\mathsf A_0^{-1})_{ij}
=[y^{i+j-a}](1-y)^{-N_0}.
$$


Set


$$
C=\frac{P_0/3-3}{2}=\frac{3Q-3}{2}.
$$


Substitution into the finite convolution, with the same verified finite bounds as in H2, gives


$$
(\mathsf B_1^T\mathsf A_0^{-1}\mathsf B_1)_{u,\ell}
=[y^{C-u-\ell}](1-y)^{N_0}.
\tag{5.6}
$$



No infinite extension changes this sum: nonnegative coefficient indices imply the prefix indices lie in their original range.

For $0\le u<\ell$,


$$
C-u-\ell\ge C-(2\ell-1)=N_0+n_J>N_0.
$$


Therefore (5.6) is zero.

Combining this with (5.4) and the sign $U_c=-S_c/3^{26}$,


$$
(\bar L_ce_0)_u
=-[y^{E-u-\ell}]x^{N_0}.
$$


Since $N_0$ is odd, this equals


$$
[y^{E-u-\ell}](1-y)^{N_0}.
$$


Finally,


$$
(1-y)^{N_0}
=(1-y^Q)(1-y)^{-b}
\quad\text{over }\mathbb F_3,
$$


and every relevant extraction is below $Q$. This proves (5.1). ∎

## Corollary 5.2 — Boundary contraction and complete matrix-return cancellation

For $g_a=(y-1)^by^a$, $0\le a\le b/2$,


$$
\begin{aligned}
g_a^T\bar L_ce_0
&=[y^{E-\ell}](1-y)^{-b}(y-1)^by^a\\
&=[y^{E-\ell}]y^a.
\end{aligned}
$$


Here $b$ is even, and


$$
E-\ell=n_J+b/2>b/2.
$$


Thus


$$
\boxed{G^T\bar L_ce_0=0.}
\tag{5.7}
$$



Equation (4.7) now gives the new complete matrix statement


$$
\boxed{
G^T(\mathcal S^{(2)}_{\rm act}
-\mathcal S^{(2)}_c)G\in81M.
}
\tag{5.8}
$$



This closes the proposed boundary-column lemma. It does **not** set $G^Tt_K$ to zero, remove (4.8)–(4.9), evaluate the next complete-core digit, or solve the eventual endpoint-annihilating inverse problem.

---

# 6. Audit of the resonant recurrence and directional bottleneck

The exact moments satisfy


$$
\mu_{t+1}+\mu_t
=\frac{3^h}{2t+1}
-\frac{3^h}{4}\bigl((2t+2)!+(2t)!\bigr),
$$


with $\mu_0=-3^h/4$.

Put


$$
q_t=(2t+2)(2t+1),
$$




$$
L_t=(2t+3)\mu_{t+2}+2\mu_{t+1}-(2t+1)\mu_t,
$$




$$
C_t=(2t+3)q_tq_{t+1}+2q_t-(2t+1).
$$


The pole parts cancel exactly, giving


$$
L_t=-\frac{3^h}{4}(2t)!\,C_t.
$$


Therefore


$$
C_tL_{t+1}-q_tC_{t+1}L_t=0.
\tag{6.1}
$$



With $s=2t+3$,


$$
C_t=(s-2)(s^4-s^2+2s-3).
$$


At


$$
t_*=(3^h-5)/2,\qquad T=t_*+3=(3H+1)/2,
$$


one has


$$
C_{t_*}\equiv1\pmod3,
$$


so the coefficient of $\mu_T$ has valuation exactly $h$.

Moreover,


$$
v_3(q_{t_*})=1,\qquad v_3(C_{t_*+1})=1.
$$


The coefficient


$$
2C_{t_*}-(2t_*+3)q_{t_*}C_{t_*+1}
$$


is a unit. There is no common factor $3$ among all recurrence coefficients.

The original window gives $T\le2n-1$. Before $T$, no denominator $3^h$ has appeared, so $\mu_t\in3\mathbb Z_3$. At $T$, its first appearance has coefficient one:


$$
\mu_T\equiv1\pmod3.
$$



**Decision:** the claimed $3^h$ forward-solve divisor is genuine and occurs inside the physical moment range.

## 6.1 What remains for the relative cofactor

Using accepted H2 and the paid endpoint-adapted elimination, retain


$$
T=
\begin{pmatrix}a&z^T\\z&C\end{pmatrix}\in27M,
\qquad f_T=e_0,\qquad v_3(\lambda)=-1,
$$


and


$$
D_0=\det T,\qquad D_1=\det C-\lambda\det T.
$$



If the **actual** $C$ is nonsingular and


$$
C^{-1}z\in3^{-1}\mathbb Z_3^{b/2},
$$


then


$$
\sigma=a-z^TC^{-1}z\in9\mathbb Z_3,
$$


and


$$
D_0=\det C\,\sigma,\qquad
D_1=\det C(1-\lambda\sigma).
$$


Since $\lambda\sigma\in3\mathbb Z_3$, the second factor is a unit. Thus, when $D_0\ne0$,


$$
v_3D_1=v_3\det C,\qquad
v_3D_0-v_3D_1\ge2.
$$



Neither A1’s theorem nor the new boundary cancellation proves the required nonsingularity or directional bound.

The complete alternative determinant pair remains


$$
\Delta=\det(\zeta_{i+j})_{0\le i,j\le m},
\qquad
\zeta_t=\sum_{s=0}^{n}[y^s]Q_{\rm act}\,\mu_{s+t},
$$




$$
K=
\det(\zeta_{i+j+2}+2\zeta_{i+j+1}+\zeta_{i+j})_{0\le i,j<m}.
$$


Its largest moment is exactly $2n-1$, and


$$
v_3\mathcal D_0-v_3\mathcal D_1
=v_3\Delta-v_3K-26.
$$


Those actual determinant valuations remain unevaluated.

---

# 7. Audit of A5’s head: cancellation of unbounded $n+r$ denominators

Set


$$
B=b-1,\qquad M=n+B,\qquad \beta=\binom MB,\qquad \chi=v_2(\beta).
$$


On the original family,


$$
v_2(n)=1,\quad v_2(B)=4,\quad v_2(M)=1,\quad M-1\ \text{odd}.
\tag{7.1}
$$



At precision $L$, retain


$$
I=8L-2,\qquad m_{\rm aux}=4(L-1),\qquad T=2L-1.
$$


The accepted complete short adjoint is


$$
\sum_{j\ge0}\mu_jt^j=((n+1)-nt-t^2)(1+t)^{-n},
$$


and


$$
S\equiv
\sum_{i=0}^{I}(-1)^i\mathfrak f_i\mathcal H_i(B)
+\mu_{\rm ext}^TU_n^{(m_{\rm aux})}K\Sigma^{-1}D_f
\pmod{2^L}.
\tag{7.2}
$$



The finite Schur inverse is integral. It is not an inverse of an unrestricted infinite matrix.

## 7.1 Regrouping

The factorial identity


$$
\mathcal F_r(B)=
\beta\frac n{n+r}\binom Br
$$


and its $B-1,B-2$ analogues yield the regrouped head


$$
\beta\sum_{r=0}^{I}(-1)^r\frac n{n+r}\mathcal T_r,
$$


where


$$
\begin{aligned}
\mathcal T_r={}&(n+1)\mathfrak f_r\binom Br\\
&+\frac{nB}{M}
(\mathfrak f_r-\mathfrak f_{r+1})\binom{B-1}{r}\\
&-\frac{B(B-1)}{M(M-1)}
(\mathfrak f_r-2\mathfrak f_{r+1}+\mathfrak f_{r+2})
\binom{B-2}{r}.
\end{aligned}
\tag{7.3}
$$



The replacement of zero extensions by the actual entries
$\mathfrak f_{I+1},\mathfrak f_{I+2}$ is legitimate modulo $2^L$: before rewriting as rational factors, their coefficients are the original integral $\mathcal F_r$, and the force truncation pays both entries.

## 7.2 The high-valuation case

Let $s=n+r$.

- If $s$ is odd, $n/s$ is even.
- If $v_2(s)=1$, then $r\equiv0\pmod4$. The accepted whole-force parity makes $\mathfrak f_r$ even, while the other prefactors in (7.3) have valuations at least $4$ and $3$. Thus $\mathcal T_r$ is even.
- If $t=v_2(s)\ge2$, then $r\equiv2\pmod4$, so $r\ge2$ and $v_2(r)=1$.

In the last case,


$$
\mathcal T_r=\binom Br\,\mathcal J_r,
$$


with


$$
\mathcal J_r
=2n\mathfrak f_r+(2-n)\mathfrak f_{r+1}
-\mathfrak f_{r+2}+s\mathcal E_r,
\qquad \mathcal E_r\in2^{-1}\mathbb Z_2.
\tag{7.4}
$$


This follows by substituting $B-r=M-s$; all possible denominators come from the single factor $M$, whose valuation is $1$.

The actual integral recurrence gives


$$
\mathfrak f_{r+1}-\mathfrak f_r
=s\left(
2\mathfrak f_r
-\frac{3r+n-1}{2}\mathfrak f_{r-1}
+\frac{(r-1)(s-1)}2\mathfrak f_{r-2}
\right),
$$


and


$$
\mathfrak f_{r+2}
=3\mathfrak f_{r+1}+(n-1)\mathfrak f_r
+s\mathcal E'_r,
\qquad \mathcal E'_r\in2^{-1}\mathbb Z_2.
$$


Therefore


$$
v_2(\mathcal J_r)\ge t-1.
$$


Also


$$
\binom Br=\frac Br\binom{B-1}{r-1}
$$


has valuation at least $3$. Hence


$$
v_2\!\left(\frac n{n+r}\mathcal T_r\right)
\ge(1-t)+3+(t-1)=3.
\tag{7.5}
$$



Thus every regrouped term is in $2\mathbb Z_2$, without any upper bound on $v_2(n+r)$.

**Decision:** the whole head lies in


$$
2\beta\mathbb Z_2+2^L\mathbb Z_2.
$$


The dangerous denominator is genuinely canceled, not bounded away.

---

# 8. Audit of the complete finite exterior/Schur return

## 8.1 Tail convolution

Let


$$
C_j=(-1)^j\binom{n+j-1}{j}.
$$


For $q>0$,


$$
\sum_{w=0}^{v}C_{q+w}\binom n{v-w}
=
(-1)^q\frac n{q+v}
\binom{n+q-1}{q-1}\binom{n-1}{v}.
\tag{8.1}
$$


The differential-equation proof in A5 is valid: it is coefficientwise finite and divides only by the nonzero integer $q+v$ in an exact rational identity.

Applying (8.1) to the three adjoint terms gives


$$
\begin{aligned}
\gamma_v={}&(-1)^b\beta n\binom{n-1}{v}\\
&\times\left[
\frac{n+1}{b+v}
+\frac{nB}{M(b+v-1)}
-\frac{B(B-1)}{M(M-1)(b+v-2)}
\right].
\end{aligned}
\tag{8.2}
$$


The complete return is


$$
\gamma^TK\Sigma^{-1}D_f.
\tag{8.3}
$$



The supplied 2,800 checks corroborate (8.1) only on their finite ranges. The displayed proof, not that finite count, establishes the general identity.

## 8.2 Symbol valuations, including the exceptions

The actual exterior matrix is


$$
K_{vt}=\lambda_k\binom{b+v}{k},
\qquad k=m_{\rm aux}+v-t.
$$


For every retained nonzero entry,


$$
k\ge v+1.
\tag{8.4}
$$


This is the relevant finite-boundary restriction.

The coefficient denominator estimate gives


$$
v_2\!\left(\frac{\lambda_k}{k(k-1)}\right)\ge-1,
\qquad
v_2\!\left(\frac{\lambda_k}{k(k-1)(k-2)}\right)\ge-2.
\tag{8.5}
$$


To make these inequalities explicit, use


$$
\frac{\lambda_k}{k^{\underline j}}
=(k-j)![z^k]\phi(z)^n.
$$


The lower bound is


$$
v_2((k-j)!)-\lfloor k/2\rfloor.
$$


For fixed parity it is nondecreasing when $k$ increases by two, because two consecutive integers contribute at least one factor $2$. The starting values give $-1$ for $j=2$ and at worst $-2$ for $j=3$.

A useful proof of the other stated estimate is the expansion


$$
\lambda_k=(-1)^k
\sum_{0\le j\le k/2}
(n)_{k-j}\,
\frac{k!}{2^j j!(k-2j)!}.
$$


The second factor is an integer counting partial matchings, while
$(n)_{k-j}$ is divisible by $(k-j)!$. Thus


$$
v_2(\lambda_k)\ge v_2(\lfloor k/2\rfloor!).
\tag{8.6}
$$


For even $k=2d\ge6$,


$$
v_2(d!)=v_2(d)+v_2((d-1)!)\ge v_2(d)+1=v_2(k).
$$


For odd $k$, division by $k$ is a unit operation. Hence $\lambda_k/k$ is integral for $k\ge5$, and also for $k=3$.

The actual exceptions are


$$
\lambda_1=-n,\qquad \lambda_2=n^2,\qquad
\lambda_4=n(n-1)(n^2+n-3),
$$


with valuations $1,2,1$, respectively.

## 8.3 Payment of the row

Put $X=b+v$. For $k\ge3$,


$$
\frac{\binom Xk}{X}=\frac1k\binom{X-1}{k-1},
$$




$$
\frac{\binom Xk}{X-1}
=\frac{X}{k(k-1)}\binom{X-2}{k-2},
$$




$$
\frac{\binom Xk}{X-2}
=\frac{X(X-1)}{k(k-1)(k-2)}
\binom{X-3}{k-3}.
$$


After dividing by $\beta$, the second and third terms of (8.2) have fixed prefactor valuations $5$ and $4$. Equations (8.5) leave them even.

The first term is even except potentially for $k=4$. By (8.4), that exception has only $v=0,1,2,3$. Its remaining product is


$$
\binom{n-1}{v}\binom{b+v-1}{3}.
$$


For $v=0,1,2$, the second factor is even because its upper argument is $0,1,2\pmod4$. For $v=3$, the first factor is even because $n-1\equiv1\pmod4$.

For $k=1,2$, the only possibilities are


$$
(k,v)=(1,0),(2,0),(2,1).
$$


The apparent denominator $B$ cancels its displayed numerator in (8.2); the exact $\lambda_1,\lambda_2$ valuations pay the remaining terms.

Thus


$$
\gamma^TK\in2\beta\mathbb Z_2^{m_{\rm aux}}.
$$


Since $\Sigma^{-1}D_f$ is integral,


$$
\boxed{\gamma^TK\Sigma^{-1}D_f\in2\beta\mathbb Z_2.}
\tag{8.7}
$$



**Decision:** the entire finite Schur return is included and has the claimed divisor.

---

# 9. Precision scope and the all-original binary theorem

At an admissible precision, the preceding results give


$$
S\in2\beta\mathbb Z_2+2^L\mathbb Z_2.
\tag{9.1}
$$



It remains to validate, rather than merely assert, admissibility for


$$
L=\max(2,\chi+1).
$$



Write $v=18+32u$, so $b=9^v$. Since


$$
M=4003b-1<4096b<2^{12+4v},
$$


Kummer’s carry count gives


$$
\chi\le12+4v,\qquad L\le13+4v.
$$


Therefore


$$
I+2=8L\le104+32v.
$$


For every $v\ge18$,


$$
104+32v<9^v=b.
$$


This inequality holds at $v=18$, and multiplication by $9$ grows faster than the linear right-hand increment.

Likewise,


$$
72L-26\le910+288v<4002\cdot9^v=n.
$$


Thus both original completion conditions hold at every original $u\ge0$.

Taking this $L$ in (9.1) proves


$$
\boxed{v_2(S)\ge\chi+1}
\tag{9.2}
$$


for every original index.

No uniform fixed precision has been substituted for the variable one.

---

# 10. Actual content payment, $u=0$, and infinite orbit classes

## 10.1 Physical telescope and paid acceptance

The physical terminal $z_b=0$ gives


$$
\sum_{j=0}^{b}(\mathcal Rz)_j
=\sum_{j=0}^{b-1}(n+1-j)W_jz_j.
$$


Indeed,


$$
(j+1)W_{j+1}-W_j=(n+1-j)W_j.
$$


The contribution from $j=b$ is necessary for this telescope.

Hence


$$
\mathscr A:=\frac{S}{2^{a+1}}
=\sum_{j=0}^{b}(x_0)_j\in\mathbb Z_2,
$$


and


$$
\boxed{
v_2(\mathscr A)\ge\max(0,\chi-a)
\ge\max(0,\chi-A_{\rm end}).
}
\tag{10.1}
$$


Since $t^2\equiv t\pmod2$,


$$
Q=x_0^Tx_0\equiv\mathscr A\pmod2.
\tag{10.2}
$$



This transfers only parity. It does not transfer the full valuation of the linear sum to the quadratic norm.

## 10.2 Exact consequence at $u=0$

The supplied finite certificate has


$$
s_2(B)=26,\quad s_2(n)=30,\quad s_2(n+B)=29,
$$


so


$$
\chi(0)=27.
$$


It also has


$$
s_2(d)=26,\quad s_2(g-d)=25,\quad s_2(g)=30,
$$


so


$$
A_{\rm end}(0)=21.
$$



The accepted theorem now proves, at this one original index,


$$
v_2(S(0))\ge28,
\qquad
v_2(\mathscr A(0))\ge6,
\qquad
Q(0)\equiv0\pmod2.
\tag{10.3}
$$



The stronger old witness, already accepted in A4 Turn 12, gives


$$
2\le a(0)\le10.
$$


Using it without recomputation,


$$
\boxed{v_2(\mathscr A(0))\ge17.}
\tag{10.4}
$$


Neither (10.3) nor (10.4) determines the exact content $a(0)$, the exact valuation of $Q(0)$, or a final scalar gcd.

The depth-$12$ solve is unnecessary. In fact the theorem proves $S(0)\equiv0\pmod{2^{28}}$.

## 10.3 Original orbit classes and growing raw divisibility

For $K\ge10$, impose


$$
4003b\equiv275\pmod{2^K}.
$$


The order


$$
\operatorname{ord}_{2^K}(9^{32})=2^{K-8}
$$


and the original coset $b\equiv209\pmod{256}$ show that this is one nonempty original class


$$
u\equiv u_K\pmod{2^{K-8}}.
$$


Modulo $1024$, its residue is $b\equiv977$, so every class lies in


$$
u\equiv1\pmod4.
$$


The already accepted $a\ge2$ theorem applies there, but supplies no upper content bound.

At ten bits,


$$
n\equiv322,\qquad B\equiv976,\qquad n+B\equiv274.
$$


A1’s stated argument—an outgoing carry at bit $9$, followed by zero result bits—is valid.

There is a small strengthening available without any new computation. The displayed ten-bit addition has carries at bits $6,7,8,9$:


$$
322=256+64+2,\qquad
976=512+256+128+64+16.
$$


Each zero result bit from $10$ through $K-1$ propagates the incoming carry. Thus


$$
\boxed{\chi\ge K-6,\qquad v_2(S)\ge K-5.}
\tag{10.5}
$$


This strengthens the report’s weaker lower bounds but remains a **raw** divisibility theorem.

Selecting increasing original representatives proves unbounded raw divisibility on infinitely many original indices. It does not prove $\chi>a$ infinitely often.

## 10.4 Exact paid bottleneck

Kummer’s formula gives


$$
A_{\rm end}
=s_2(B)+s_2(n-B+2)-s_2(n+2).
$$


Because $n\equiv2\pmod{64}$,


$$
s_2(n+2)=s_2(n).
$$


Therefore


$$
\boxed{
\chi-A_{\rm end}
=
2s_2(4002b)-s_2(4003b-1)-s_2(4001b+3).
}
\tag{10.6}
$$



The concrete sufficient infinite lemma remains:

> Prove that the right side of (10.6) is at least $1$ on a specified infinite set of original nonnegative indices $u$.

The low-bit carry classes do not control all high bits in the last digit sum. They therefore do not prove this lemma.

---

# 11. Complete source, contents, denominators, and whole errors

## 11.1 Binary source completion is unchanged

The theorem concerns $S$, hence the force column $x$. It does not remove either source from $y$.

At precision $2^L$, retain


$$
a_t=(b+t)!/b!,\qquad 0\le t\le T,
$$




$$
\xi_v=
\sum_{t=0}^{T}a_t
\sum_{\substack{0\le r\le t\\0\le v-r\le m_{\rm aux}}}
\binom n{t-r}\lambda_{v-r}\binom{b+v}{v-r},
$$




$$
\delta=K\Sigma^{-1}G^{[V]}\xi-\xi,\qquad
\theta_v=\sum_{w=v}^{V}\binom n{w-v}\delta_w,
\qquad V=T+m_{\rm aux}.
$$


The physical source terminal remains


$$
\tau_b=W_b(bz^k_{b-1}+1),\qquad z_b^k=0.
$$


No completed exterior value is substituted for that physical condition.

The complete raw observations retain both terminal terms:


$$
\mathcal U=
\sum_{j<b}W_j^2(\Delta_jz^f)^2
+b^2W_b^2(z^f_{b-1})^2,
$$




$$
\mathcal V=
\sum_{j<b}W_j^2(\Delta_jz^f)(\Delta_jz^k)
+W_b^2bz^f_{b-1}(bz^k_{b-1}+1).
$$


For a relative assertion,


$$
E-r(u)Q
=2^{-2a-2}\bigl(2^{a-1}\mathcal V-r(u)\mathcal U\bigr).
$$


All those divisions and the original logarithmic guard remain necessary.

## 11.2 Actual binary clearer and all-prime gcd

Retain


$$
\omega_j=j!W_j,\qquad
u_j=\frac{2\Lambda R\,x_j}{\omega_j},\qquad
v_j=\frac{4b!\,y_j}{\omega_j},
$$




$$
d_B=\operatorname{lcm}_{0\le j\le b}
\{\operatorname{den}(u_j),\operatorname{den}(v_j)\}.
$$


For the actual integral columns $U=d_Bu,V=d_Bv$, their actual contents satisfy the accepted identities


$$
d_B=\operatorname{lcm}(D_\zeta,D_\rho),
$$




$$
c_U=(d_B/D_\zeta)c_\zeta,\qquad
c_V=d_B/D_\rho,\qquad
\gcd(c_U,c_V)=1.
$$


The binomial factor in $S$ authorizes no new column-content division.

With $\mathcal N=x^Tx,\ \mathcal H=x^Ty$,


$$
A_B=d_B^2\,4\Lambda^2R^2\mathcal N,\qquad
H_B=d_B^2\,8\Lambda Rb!\mathcal H,
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
$$


This gcd is over **all primes**.

The actual primitive denominator still has the exact scalar-cofactor expression


$$
q_n=
\frac{c_U}{\delta_{\rm sc}}\,
\frac{N^\circ}
{\gcd\!\left(N^\circ,\left|c_VH^\circ/\delta_{\rm sc}\right|\right)},
\qquad
\delta_{\rm sc}=\gcd(c_U,|H^\circ|).
$$


No new bound for these scalar cofactors has been proved.

In particular, the retained original-family law remains


$$
\boxed{v_3(q_n)=n-\frac{b+15}{2}.}
$$


The whole error is still


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
\tag{11.1}
$$



## 11.3 Actual ternary clearer and whole error

Retain the actual least simultaneous clearer and actual contents used in


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$




$$
g_\ell=\gcd(|A_\ell|,|B_\ell|).
$$


For $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


The exact whole error remains


$$
\boxed{
q(e+\pi)-p=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
{g_\ell}\det H_{\rm complete}.
}
\tag{11.2}
$$



A sufficient irrationality criterion still requires, at the **same infinite original indices**,


$$
B_\ell\ne0,\qquad \det H_{\rm complete}\ne0,
$$


and


$$
\log g_\ell-(m+1)\log\ell_{\rm clr}
-\log|\det H_{\rm complete}|\longrightarrow+\infty.
$$



Neither a common determinant factor nor the fixed-depth matrix cancellation proved here establishes that comparison.

---

# 12. Proof-acceptance ledger

| Claim | Audit decision and exact scope |
|---|---|
| H2, second rank/radical, endpoint, complete diagonal | Already accepted; pending label removed |
| Actual producer coefficient cutoffs modulo $9$ and $3^{24}$ | Accepted on sufficiently large original ternary indices |
| Complete mixed observation modulo $27$ | Accepted; all relevant poles and factorial payment included |
| Nine-period annihilation | Accepted for the stated exact corrected combinations |
| Precision-$30$ direct producer transfer | Accepted on the fixed infinite original subfamily |
| Finite terminal inverse $-e_0$ | Accepted using the actual finite first column |
| Quadratic matrix return at order $27$ | Zero at that digit |
| Endpoint and diagonal returns | Accepted and retained; not zero in general |
| First complete-core boundary-column formula | **Newly proved in §5** |
| $G^T(\mathcal S^{(2)}_{\rm act}-\mathcal S^{(2)}_c)G\in81M$ | **New proved consequence** |
| Actual resonant coefficient divisor $3^h$ | Accepted; inside the original moment range |
| Actual $C^{-1}z\in3^{-1}\mathbb Z_3^{b/2}$ | Open |
| Actual complete relative determinant valuations | Open |
| A5 head denominator cancellation | Accepted without bounding $v_2(n+r)$ |
| Complete finite exterior/Schur return divisor | Accepted, including all small-$k$ exceptions |
| Precision $L=\max(2,\chi+1)$ | Explicitly validated for every original $u\ge0$ |
| $v_2(S)\ge\chi+1$ | Accepted all-original theorem |
| Actual-content-paid inequality | Accepted |
| $u=0:\chi=27,\ A_{\rm end}=21$ | Supplied finite certificate; no rerun |
| $u=0: v_2(S)\ge28,\ Q$ even | Now an unconditional finite consequence of the theorem |
| $u=0$ paid linear valuation at least $17$ | Uses accepted old witness $a(0)\le10$ |
| Infinite $a\ge2$ on $u\equiv1\pmod4$ | Retained accepted result |
| Original carry classes and unbounded raw divisibility | Accepted; strengthened in (10.5) |
| Positive paid excess infinitely often | Open |
| Coprime actual all-prime column contents | Retained at accepted scope |
| New all-prime scalar-cofactor or whole-error bound | Not obtained |
| Rationality or irrationality of $e+\pi$ | Unresolved |

---

# 13. Literature gate

No full mathematical source for Family017, Family005, or Family022 is included in this packet. I have not inspected any numbered section of those manuscripts here, and no theorem from them is adopted.

The supplied acquisition inventory and catalogue summaries establish neither their mathematical correctness nor applicability:

- a bound for the irrationality exponent of $\pi$ alone supplies no mixed exponential/logarithmic transfer to $e+\pi$;
- a Catalan-constant kernel cannot replace the present full factorial functional without a new compatible identity and arithmetic analysis;
- an almost-everywhere metric theorem supplies no deterministic conclusion at the fixed value $e+\pi$.

The present report therefore relies only on the attached mathematical sources and the explicitly accepted prior results.

---

# 14. Bounded arithmetic follow-up and final bottleneck

No further computation is needed to accept the audited theorems or the supplied $u=0$ conclusion. In particular, the depth-$12$ solve should not be repeated.

A bounded, optional next calculation directed at the remaining binary bottleneck is:

### Inputs

For exactly $1\le u\le64$, form


$$
b_u=9^{18+32u},
\quad n_u=4002b_u,
\quad M_u=4003b_u-1,
\quad N_u=4001b_u+3.
$$


All these integers have fewer than $8300$ bits. Successive $b_u$ can be formed by multiplication by the fixed integer $9^{32}$.

### Expected verifiable output

For each of the 64 original indices, output:

1. the exact integers, in hexadecimal or decimal;
2. their binary digit sums;
3.
   

$$
\chi_u=s_2(b_u-1)+s_2(n_u)-s_2(M_u);
$$


4.
   

$$
A_{{\rm end},u}
   =s_2(b_u-1)+s_2(N_u)-s_2(n_u);
$$


5. the exact excess
   

$$
\chi_u-A_{{\rm end},u}
   =2s_2(n_u)-s_2(M_u)-s_2(N_u);
$$


6. the resulting finite yes/no conclusion for the sufficient condition $Q(u)$ even.

No outcome is asserted in advance. Such a calculation would establish only 64 finite facts and could guide, but not prove, an infinite digit-sum lemma.

## Final conclusion

The audit accepts the two principal new source theorems and advances the ternary calculation by proving the missing original boundary-column identity. The resulting new matrix statement is


$$
\boxed{
G^T(\mathcal S^{(2)}_{\rm act}
-\mathcal S^{(2)}_c)G\in81M
}
$$


on the same sufficiently large infinite original ternary subfamily.

The exact local bottlenecks are now:

- **ternary:** evaluate the next complete-core residual together with the actual endpoint and diagonal, sufficiently to prove the actual directional inverse bound or the complete relative determinant valuation;
- **binary:** prove positive actual-content-paid acceptance on infinitely many original indices, for example through the explicit digit-sum excess (10.6).

Beyond both lies the unchanged global obligation: control the **actual all-prime final gcd, actual primitive denominator, and nonzero whole evaluated error at the same infinite original indices**.



$$
\boxed{\text{No claim audited or proved here establishes the rationality or irrationality of }e+\pi.}
$$


