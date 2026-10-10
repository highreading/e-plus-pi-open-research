> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3, Turn 15 — Explicit backward defects, an actual-seed reduction of order, and a joint saturated-resonance divisor

## Executive summary

The irrationality of $e+\pi$ remains unresolved.

This turn advances the two outstanding arithmetic interfaces, but does **not** prove either required subfactorial estimate.

The new results are:

1. **An explicit two-step backward reference defect.** Both coordinates are evaluated below as rational expressions in the actual reference coefficients. Their denominators have prime support at most $n+4$. A degree-$11$ polynomial bounds their common large-prime content. This is a fixed-block result, not a multiplicative-block estimate.

2. **An exact composition law retaining the reference directions and their scalar multipliers.** For $n<u<t$,
   

$$
\boxed{
   \boldsymbol\delta_{n,t}
   =
   \boldsymbol\delta_{n,u}\,\alpha_{u,t}
   +\mathsf D_{n,u}\boldsymbol\delta_{u,t}.
   }
$$


   The multiplier $\alpha_{u,t}$ is related explicitly to the actual fixed-seed scalars $\sigma_u,\sigma_t$. It is a unit on common alignment, but not automatically on terminal alignment alone. The two summands can cancel. Consequently, fixed-block isolation bounds cannot simply be added.

3. **A reduction of order using the actual moment solution.** On an actual nonzero-coordinate chart, the transported terminal reference is recovered from a two-dimensional recurrence and a scalar telescoping sum. On a nondegenerate scalar chart, the two-dimensional recurrence becomes an explicit second-order scalar recurrence. All additional scalar denominators are displayed and charged. This is not an arbitrary companion replacement.

   The reduction also exposes a precise fixed-seed obstruction: the exterior state used in this reduction has large-prime content **exactly $\mathcal I_t$** at every point of the backward block. Primitive normalization of that exterior state therefore requires the very alignment divisor one is trying to bound.

4. **A contact-independent, completely evaluated affine invariant.** The Green formula and the two final-source identities give an explicit finite expression for
   

$$
\mathscr K_n^\circ
   =\widehat h B^\circ-\widehat\ell A^\circ,
$$


   including both final moment-source contributions. The homogeneous seed boundary cancels in this transverse scalar, but the complete $\kappa$ does not.

5. **A joint divisor theorem for the two saturated endpoint charts.** Let
   

$$
g=\gcd(|F|,|CM|),\qquad
   T_{\mathrm{aff}}=\frac{CM+F(\kappa-\mathscr K_n^\circ)}{g}.
$$


   Let $\lambda_{\mathrm{ct}}$ be the actual integral contact cross-product scalar defined in Section 6. Then
   

$$
\boxed{
   \gcd(\mathfrak S_0,\mathfrak S_3)
   \mid
   \left(
   \frac{|\lambda_{\mathrm{ct}}|}
   {\gcd\!\left(|\lambda_{\mathrm{ct}}|,\ |F|/\mathcal I_n\right)}
   \right)_{>N}.
   }
$$


   Moreover, the least common multiple of the two saturation factors is one explicit gcd involving $T_{\mathrm{aff}}$. This bounds simultaneous resonance by the **actual contact collision scalar after paying the saturated overlap**. It is a divisibility theorem, not a bound on its height.

Neither the multiplicative-block cofactor nor the remaining joint resonance gcd is proved subfactorial. No additional alignment sample is requested or used.

---

# 1. Domain, retained results, and notation

The approximation domain remains exactly


$$
\boxed{
n=15^r\quad\text{or}\quad n=105^r,\qquad r\ge2.
}
$$


As before,


$$
m=n+1,\qquad N=n+2,\qquad L=2^{m/2}.
$$



Consecutive auxiliary indices are used only in the proved index recurrence. They do not enlarge the approximation domain, alter the finite contact matrix, or add a physical forcing row.

I retain


$$
z_n=(P_n,Q_n,F_n)^T,
\qquad
\overline M_n=Q_n\tau_n-P_n\tau_{n+1},
\qquad
M_n=L_n\overline M_n
$$


at original indices, and


$$
\mathcal I_n=\gcd(|F_n|,|M_n|)_{>n+2}.
$$



The following results are reused at their proved scope:

- the natural observation transfer and its determinant;
- the genuine seed $z_2=(0,10,-66)^T$;
- the evaluated block-remainder identity and its actual-unit property;
- adjacent isolation;
- $F_n\equiv-2\pmod n$, hence $F_n\ne0$, on the original domain;
- the full factorization
  

$$
\mathfrak X_j=\mathfrak S_j\mathfrak U_j,
  \qquad \mathfrak U_j\mid\mathcal I_n;
$$


- the integral finite Green formula;
- the two exact final-source identities;
- the actual primitive contact rows and their coordinate-content payment;
- the full saturation theorem.

The binary assertions in A4 are not imported into this endpoint family.

The accepted computations at $3375$ and $11025$ remain finite facts. None is rerun.

---

# 2. The inverse transfer and an explicit two-step defect

Write, temporarily,


$$
m=n+1,\quad N=n+2,\quad J=n+3,\quad K=n+4,
$$




$$
H=n^2+3n+1,\qquad c=2n+3.
$$



The natural transfer is $z_{n+1}=\mathsf U_nz_n$. Direct solution of its three equations gives a useful polynomial numerator for its inverse.

## Proposition 2.1 — Paid inverse transfer



$$
\boxed{
\mathsf U_n^{-1}
=
\frac1{mNJ}
\begin{pmatrix}
2H&3mN&m\\
N^2&cN&N\\
-2mH&-2mcN&-2mN
\end{pmatrix}.
}
\tag{2.1}
$$



Thus every denominator in this inverse has prime support at most $n+3$.

### Derivation

The already proved identities give


$$
P_{n+1}=mNZ_n,
$$




$$
Q_{n+1}=NP_n-HZ_n+\frac12F_n,
$$




$$
Z_{n+1}=\frac12P_n-\frac H2Z_n-\frac14F_n.
$$


Since


$$
Z_{n+1}=Q_{n+1}+\frac{F_{n+1}}{2N},
$$


adding $2Z_{n+1}$ to $Q_{n+1}$ yields


$$
JP_n=3Q_{n+1}+\frac{F_{n+1}}N+\frac{2H}{mN}P_{n+1}.
$$


Substitution then gives the other two rows of (2.1). ∎

## 2.1 The actual two-step terminal reference

Put


$$
h_2=\tau_{n+2},\qquad \ell_2=\tau_{n+3},
$$


and define


$$
r_n^{[2]}
=
\mathsf U_n^{-1}\mathsf U_{n+1}^{-1}
(h_2,\ell_2,0)^T.
$$


Write its coordinates as


$$
r_n^{[2]}=(p^{[2]},q^{[2]},f^{[2]})^T.
$$



Introduce the polynomials


$$
A=(n+1)(2n^2+9n+8),
$$




$$
B=3n^2+7n-2,
$$




$$
A_P=5n^3+28n^2+43n+18,
\qquad
B_P=8n^2+25n+11.
$$



## Theorem 2.2 — Exact two-step backward reference

For every auxiliary $n\ge2$,


$$
\boxed{
p^{[2]}
=
\frac{A_Ph_2+NB_P\ell_2}{mN^2JK},
}
\tag{2.2}
$$




$$
\boxed{
q^{[2]}
=
\frac{cJh_2+m(3n+7)\ell_2}{mNJK},
}
\tag{2.3}
$$


and


$$
\boxed{
f^{[2]}
=
-\frac{2(Ah_2+NB\ell_2)}{N^2JK}.
}
\tag{2.4}
$$



Consequently, the two coordinates of the actual two-step defect are


$$
\boxed{
\delta_{n,n+2,1}
=
-\frac{2(Ah_2+NB\ell_2)}{N^2JK},
}
\tag{2.5}
$$


and


$$
\boxed{
\delta_{n,n+2,2}
=
\frac{
N\tau_n\!\left(cJh_2+m(3n+7)\ell_2\right)
-\tau_{n+1}\!\left(A_Ph_2+NB_P\ell_2\right)
}{
mN^2JK
}.
}
\tag{2.6}
$$



These are the actual reference coefficients, not free terminal variables.

### Proof

Multiply the two explicit matrices (2.1), evaluate at $(h_2,\ell_2,0)^T$, and cancel the displayed scalar factors. For example, the coefficient of $h_2$ in the resulting $F$-coordinate reduces to


$$
-\frac{2}{JN^2K}
\left(cJN-2(n^2+5n+5)\right),
$$


and


$$
cJN-2(n^2+5n+5)
=(n+1)(2n^2+9n+8)=A.
$$


The coefficient of $\ell_2$ reduces to $-2B/(NJK)$. The other two coordinates follow similarly.

Finally,


$$
\mathsf O_n(p,q,f)^T=(f,\tau_nq-\tau_{n+1}p)^T.
$$


This gives (2.5)–(2.6). ∎

The first coordinate is strictly negative over $\mathbb Q$ for $n\ge2$, since $A,B,h_2,\ell_2>0$. Thus this reference defect is not identically zero.

---

# 3. A paid common-content theorem for the two-step defect

This section gives a genuine fixed-block support theorem. Its limitation is stated explicitly afterward.

Set


$$
c'=2n+5,\qquad D=5n^2+20n+19,\qquad E=3n+7.
$$


The reference recurrence gives


$$
\tau_{n+1}=\frac{J\ell_2-c'h_2}{N},
$$




$$
\tau_n=\frac{Dh_2-cJ\ell_2}{mN}.
\tag{3.1}
$$



After substitution in (2.6), define the homogeneous quadratic


$$
\begin{aligned}
G(X,Y)={}&
N(DX-cJY)(cJX+mEY)\\
&-m(JY-c'X)(A_PX+NB_PY).
\end{aligned}
\tag{3.2}
$$


Then


$$
\boxed{
\delta_{n,n+2,2}
=
\frac{G(h_2,\ell_2)}{m^2N^3JK}.
}
\tag{3.3}
$$



The first coordinate, up to a paid unit, is the linear form


$$
AX+NBY.
$$



Define


$$
K_1=7n^3+54n^2+127n+92,
$$




$$
K_2=n^5+19n^4+118n^3+311n^2+347n+124
$$


and


$$
\boxed{
\begin{aligned}
\mathscr R_2(n)={}&
N(DNB+cJA)K_1\\
&+mN(JA+c'NB)K_2.
\end{aligned}}
\tag{3.4}
$$


This is a positive polynomial for $n\ge2$, of degree $11$ and leading coefficient $8$.

## Theorem 3.1 — Two-step defect content

For every prime $p>n+4$,


$$
\boxed{
\min_i v_p(\delta_{n,n+2,i})
\le v_p(\mathscr R_2(n)).
}
\tag{3.5}
$$



In particular, the common large-prime alignment at $n$ and $n+2$ divides


$$
\boxed{\mathscr R_2(n)_{>n+4}.}
\tag{3.6}
$$



### Proof

A direct calculation gives


$$
G(-NB,A)=-\mathscr R_2(n).
$$


The simplifications used here are


$$
mEA-cJNB=K_1,
$$




$$
B_PA-A_PB=K_2.
$$



For a linear form $aX+bY$ and a quadratic


$$
uX^2+vXY+wY^2,
$$


their homogeneous resultant is


$$
a^2w-abv+b^2u.
$$


Integral Bézout identities put the resultant times $X^2$, and the resultant times $Y^2$, in the ideal generated by the two forms.

At $p>n+4$, all displayed scalar denominators are units, and the actual pair $(h_2,\ell_2)$ is primitive. Hence at least one of $h_2,\ell_2$ is a unit, proving (3.5).

The fixed-seed block-remainder identity then bounds common alignment by the common defect valuation, proving (3.6). ∎

### Exact limitation

This proves an $O(\log n)$ bound for **two-step common alignment**.

It does not bound alignment at either endpoint individually. Nor does it bound alignment after $14n$ or $104n$ intervening steps. The composition law below explains exactly why.

---

# 4. Exact block composition, terminal multipliers, and the cofactor valuation

Let


$$
n<u<t,\qquad
\mathscr R_t=\mathbb Z[1/p:p\le t+2].
$$



For every $s\le t$, choose an actual reference frame


$$
\mathsf V_s=(v_s,w_s,e_3),
$$


where


$$
v_s=(\tau_s,\tau_{s+1},0)^T,
$$




$$
w_s=(-v_s^\flat,u_s,0)^T,
\qquad
u_s\tau_s+v_s^\flat\tau_{s+1}=1.
$$


Thus $\det\mathsf V_s=1$.

These choices can be made with denominators supported at primes at most $t+2$. For example, clear the dyadic reference denominators, take an ordinary integer Bézout relation, and divide by the gcd of the cleared pair. Reference primitivity implies that this gcd has no prime factor exceeding $t+2$.

Define


$$
\mathsf G_{s,t}
=
\mathsf V_s^{-1}\mathsf W_{s,t}^{-1}\mathsf V_t
=
\begin{pmatrix}
\alpha_{s,t}&\boldsymbol\beta_{s,t}\\
\boldsymbol\delta_{s,t}&\mathsf D_{s,t}
\end{pmatrix}.
\tag{4.1}
$$


The lower coordinates are ordered as $(\overline M,F)$; exchanging them recovers the ordering used in Turn 14.

## Theorem 4.1 — Reference-preserving composition



$$
\boxed{
\boldsymbol\delta_{n,t}
=
\boldsymbol\delta_{n,u}\alpha_{u,t}
+
\mathsf D_{n,u}\boldsymbol\delta_{u,t},
}
\tag{4.2}
$$


and


$$
\boxed{
\alpha_{n,t}
=
\alpha_{n,u}\alpha_{u,t}
+
\boldsymbol\beta_{n,u}\boldsymbol\delta_{u,t}.
}
\tag{4.3}
$$



Every coefficient belongs to $\mathscr R_t$.

### Proof

The actual block transfers satisfy


$$
\mathsf G_{n,t}=\mathsf G_{n,u}\mathsf G_{u,t}.
$$


Equations (4.2)–(4.3) are the first block column of this equality. ∎

This applies in particular to multiplicative compositions


$$
n\longrightarrow bn\longrightarrow b^2n,
\qquad b\in\{15,105\}.
$$



## 4.1 Which scalar is a unit?

The actual state has frame coordinates


$$
\mathsf V_s^{-1}z_s
=
(\sigma_s,\overline M_s,F_s)^T.
$$


Therefore


$$
\boxed{
\sigma_u
=
\alpha_{u,t}\sigma_t
+
\boldsymbol\beta_{u,t}
\binom{\overline M_t}{F_t}.
}
\tag{4.4}
$$



At a prime $p>t+2$ with terminal alignment depth $a_t>0$, $\sigma_t$ is a unit.

If $u$ is also aligned modulo $p$, then $\sigma_u$ is a unit, and (4.4) implies that $\alpha_{u,t}$ is a unit. But terminal alignment alone does not imply this: the intermediate state may be unaligned, and $\sigma_u$ need not be a unit in the chosen reference chart.

Even when $\alpha_{u,t}$ is a unit, the two terms in (4.2) may cancel. Thus


$$
\sum_s\log|\mathscr R_2(s)|
$$


is not a bound for the multiplicative-block defect or its cofactor.

## 4.2 Exact control of the compulsory cofactor

For $p>t+2$, set


$$
a_s=\min\{v_p(F_s),v_p(M_s)\},
\qquad
d_{n,t}=\min_i v_p(\delta_{n,t,i}).
$$


The evaluated remainder and the actual-unit assertion give


$$
\min(a_n,a_t)=\min(d_{n,t},a_t).
$$


Hence


$$
\boxed{
(a_t-d_{n,t})_+=(a_t-a_n)_+.
}
\tag{4.5}
$$



More precisely:

- if $d_{n,t}<a_t$, then $a_n=d_{n,t}$;
- if $d_{n,t}\ge a_t$, then $a_n\ge a_t$.

Thus the compulsory payment is exactly the **new terminal alignment depth not already present at the initial index**. A small common-defect valuation does not make this payment small; it can force almost all terminal alignment to be paid.

Let


$$
\mathcal I_{n\mid t}
=
\prod_{p>t+2}p^{\min(v_p(F_n),v_p(M_n))}.
$$


The least large-prime cofactor allowing both initial observations to belong to the terminal observation ideal is


$$
\boxed{
c^{\min}_{n,t}
=
\frac{\mathcal I_t}
{\gcd(\mathcal I_t,\mathcal I_{n\mid t})}.
}
\tag{4.6}
$$


This is an exact ideal-theoretic statement in $\mathscr R_t$, not a height estimate.

### Moving thresholds and medium primes

The old-threshold alignment splits exactly as


$$
\boxed{
\mathcal I_n
=
\mathcal I_{n\mid t}\,
\mathcal M_{n,t},
}
\tag{4.7}
$$


where


$$
\boxed{
\mathcal M_{n,t}
=
\prod_{n+2<p\le t+2}
p^{\min(v_p(F_n),v_p(M_n))}.
}
\tag{4.8}
$$



No bound for this medium-prime factor is asserted.

Since $\mathcal I_t$ has support strictly above $t+2$,


$$
\gcd(\mathcal I_t,\mathcal I_n)
=
\gcd(\mathcal I_t,\mathcal I_{n\mid t}).
$$


Thus medium primes do not obstruct the valid divisibility


$$
\mathcal I_t\mid c^{\min}_{n,t}\mathcal I_n.
$$


They must, however, be retained whenever $\mathcal I_n$ itself is reconstructed from a calculation localized at $t+2$.

The missing multiplicative-block theorem is still


$$
\log c^{\min}_{n,bn}=o(n\log n),
$$


or a sufficiently strong alternative. It is not proved here.

---

# 5. Reduction of order using the actual fixed-seed moment solution

The explicit block formulas can be extended without retaining a free three-dimensional homogeneous state. The reduction uses the **actual solution $z_s$**, not a substitute companion.

Fix $t=bn$, and let


$$
r_s=\mathsf W_{s,t}^{-1}v_t.
$$


Then $r_{s+1}=\mathsf U_sr_s$.

First work on an interval where $F_s\ne0$. Write


$$
r_s=\lambda_sz_s+(x_s,y_s,0)^T,
\qquad
\lambda_s=\frac{(r_s)_3}{F_s}.
\tag{5.1}
$$



Let $\mathsf U_s=(u_{ij,s})$. Direct substitution gives


$$
\boxed{
\binom{x_{s+1}}{y_{s+1}}
=
\mathsf A_s\binom{x_s}{y_s},
}
\tag{5.2}
$$


where


$$
\boxed{
\mathsf A_s
=
\begin{pmatrix}
u_{11,s}&u_{12,s}\\
u_{21,s}&u_{22,s}
\end{pmatrix}
-
\frac1{F_{s+1}}
\binom{P_{s+1}}{Q_{s+1}}
\begin{pmatrix}u_{31,s}&u_{32,s}\end{pmatrix}.
}
\tag{5.3}
$$


The scalar coordinate satisfies


$$
\boxed{
\lambda_{s+1}-\lambda_s
=
\frac{u_{31,s}x_s+u_{32,s}y_s}{F_{s+1}}.
}
\tag{5.4}
$$



Since $r_t=v_t$,


$$
\boxed{
(x_t,y_t)=(\tau_t,\tau_{t+1}),\qquad \lambda_t=0.
}
\tag{5.5}
$$



Therefore


$$
\boxed{
\lambda_n
=
-\sum_{s=n}^{t-1}
\frac{u_{31,s}x_s+u_{32,s}y_s}{F_{s+1}},
}
\tag{5.6}
$$


and the two required defect coordinates are


$$
\boxed{
\delta_{n,t,1}=F_n\lambda_n,
}
\tag{5.7}
$$




$$
\boxed{
\delta_{n,t,2}
=
\overline M_n\lambda_n+\tau_ny_n-\tau_{n+1}x_n.
}
\tag{5.8}
$$



Equations (5.2), (5.5)–(5.8) are an actual-seed reduction and telescoping expression for $\boldsymbol\delta_{b,n}$.

## 5.1 Explicit second-order scalar recurrence

Write


$$
\mathsf A_s=
\begin{pmatrix}a_s&b_s\\c_s&d_s\end{pmatrix}.
$$


With $m=s+1,\ N=s+2,\ H=s^2+3s+1,\ c=2s+3$, its entries are


$$
a_s=\frac{NcP_{s+1}}{F_{s+1}},
$$




$$
b_s=mN-\frac{NHP_{s+1}}{F_{s+1}},
$$




$$
c_s=N+\frac{NcQ_{s+1}}{F_{s+1}},
$$




$$
d_s=-H-\frac{NHQ_{s+1}}{F_{s+1}}.
\tag{5.9}
$$


Its determinant is


$$
\boxed{
\det\mathsf A_s
=
\det\mathsf U_s\,\frac{F_s}{F_{s+1}}.
}
\tag{5.10}
$$



When $b_s\ne0$, elimination of $y_s$ gives


$$
\boxed{
\begin{aligned}
b_sx_{s+2}
&-(a_{s+1}b_s+b_{s+1}d_s)x_{s+1}\\
&+b_{s+1}\det(\mathsf A_s)x_s=0.
\end{aligned}}
\tag{5.11}
$$


The missing coordinate is


$$
\boxed{
y_s=\frac{x_{s+1}-a_sx_s}{b_s}.
}
\tag{5.12}
$$



A useful exact numerator is


$$
\boxed{
b_s
=
-\frac{(s+1)(s+2)^2\bigl(2(2s+3)P_s+3F_s\bigr)}
{2F_{s+1}}.
}
\tag{5.13}
$$


Thus the scalarization denominators are not hidden: besides the displayed small factors, they involve actual $F_{s+1}$ and, when (5.12) is used, the actual numerator of $b_s$.

### Proof of the determinant identity

The change-of-coordinate matrix in (5.1) has columns


$$
z_s,e_1,e_2
$$


and determinant $F_s$. In these coordinates the transfer is block upper triangular, with diagonal blocks $1,\mathsf A_s$. Taking determinants gives (5.10). ∎

## 5.2 Zeros and paid chart changes

The source proves $F_n\ne0$ at original odd indices. It does not, by itself, prove $F_s\ne0$ at every auxiliary index in a block.

The reduction therefore must not silently divide by every intermediate $F_s$.

For a complete block, choose at each auxiliary $s$ a nonzero actual coordinate $q_s$ of $z_s$, permute it into the third position, and apply (5.1)–(5.4) to the permuted actual transfer. This gives an unconditional patched two-dimensional recurrence and scalar telescope. On scalar charts where an off-diagonal entry vanishes, retain the two-coordinate recurrence or switch scalar coordinate.

The additional denominators are explicitly payable. A safe clearer for the backward chart calculation is


$$
\boxed{
2^{t+1}
\prod_{s=n}^{t-1}
|q_s|(s+1)(s+2)(s+3).
}
\tag{5.14}
$$


If scalar reconstruction divides by $b_s$, multiply additionally by the nonzero numerator of $b_s$ in lowest terms at every such use.

This is a finite exact denominator payment. It is **not** subfactorial. Moreover, these chart denominators are partly artifacts: the complete expression equals the original defect in $\mathscr R_t^2$, so its large-prime chart denominators cancel in the whole evaluation. Such cancellation cannot be assumed term by term in (5.6).

## 5.3 The intrinsic fixed-seed obstruction in the exterior reduction

There is a denominator/content obstruction that does not depend on a choice of pivot.

Define


$$
\omega_s=z_s\times r_s.
$$


Since both vectors follow the same actual transfer,


$$
\omega_{s+1}
=
\det(\mathsf U_s)\mathsf U_s^{-T}\omega_s.
\tag{5.15}
$$


At every $p>t+2$, this is an invertible integral transfer.

At the terminal,


$$
\boxed{
\omega_t
=
(-F_t\tau_{t+1},\ F_t\tau_t,\ -\overline M_t)^T.
}
\tag{5.16}
$$


Reference primitivity therefore gives


$$
\min_i v_p(\omega_{t,i})
=
\min(v_p(F_t),v_p(M_t))=a_t.
$$


Invertibility of (5.15) now proves:

## Theorem 5.1 — Exact exterior content of the actual reduction

For every $n\le s\le t$ and every $p>t+2$,


$$
\boxed{
\min_i v_p(\omega_{s,i})=a_t.
}
\tag{5.17}
$$



Thus the large-prime content of the entire backward exterior state is exactly


$$
\boxed{\mathcal I_t.}
\tag{5.18}
$$



This is a fixed-seed statement about the actual terminal reference and actual moment state.

### Consequence and scope

A proof that first makes this exterior state primitive must divide out $\mathcal I_t$. It cannot then use its primitivity to prove that $\mathcal I_t$ is small without additional arithmetic.

This is a precise obstruction to an **uncharged primitive exterior reduction**. It is not a proof that $c^{\min}_{n,bn}$ has factorial size, and it does not disprove the desired subfactorial cofactor theorem.

The new scalar recurrence and telescope therefore improve the explicit interface, but do not close the arithmetic target.

---

# 6. A completely evaluated transverse affine invariant

Return to an original index and put


$$
C=mZ,
\qquad
\mathscr K_n^\circ=\widehat hB^\circ-\widehat\ell A^\circ,
\qquad
\Xi_n=\kappa-\mathscr K_n^\circ.
$$


Then


$$
\Theta=CM+F\Xi_n.
\tag{6.1}
$$



To avoid confusing the physical source with the alignment scalar $F$, denote the original physical source coefficient by $\mathfrak f_i$:


$$
\mathfrak f_i
=
(n+1)a_i-ni\,a_{i-1}
+\frac{(n-1)i(i-1)}2a_{i-2}
+\frac{i(i-1)(i-2)}2a_{i-3}.
$$



The retained Green formula is


$$
b_k=-h_k+\sum_{i=0}^{k-1}\mathsf G_{k,i}\mathfrak f_i,
$$


with


$$
\mathsf G_{k,k-1}=1,\qquad
\mathsf G_{k,k-2}=2k-1.
$$



Since


$$
A^\circ=\frac m2b_n,\qquad
B^\circ=b_{n+1}-\frac m2b_n,
$$


we have


$$
\mathscr K_n^\circ
=
\widehat h b_{n+1}
-\frac m2(\widehat h+\widehat\ell)b_n.
\tag{6.2}
$$



The homogeneous boundary cancels because


$$
h_n=n!\tau_n,\qquad
h_{n+1}=\frac m2n!(\tau_n+\tau_{n+1}).
$$



## Proposition 6.1 — Finite Wronskian-source expression



$$
\boxed{
\begin{aligned}
\mathscr K_n^\circ={}&
\sum_{i=0}^{n-2}
\left[
\widehat h\,\mathsf G_{n+1,i}
-\frac m2(\widehat h+\widehat\ell)\mathsf G_{n,i}
\right]\mathfrak f_i\\
&+\frac{(3n+1)\widehat h-m\widehat\ell}{2}
\frac{Y-X+Z}{n}\\
&+\frac{\widehat h}{2}(3X-Y-Z).
\end{aligned}}
\tag{6.3}
$$



All displayed divisions evaluate exactly on the actual source.

### Proof

Insert the two Green formulas in (6.2). The homogeneous terms cancel exactly. The coefficient of $\mathfrak f_n$ is $\widehat h$, while that of $\mathfrak f_{n-1}$ is


$$
(2n+1)\widehat h-\frac m2(\widehat h+\widehat\ell)
=
\frac{(3n+1)\widehat h-m\widehat\ell}{2}.
$$


Now use the retained exact identities


$$
\mathfrak f_{n-1}=\frac{Y-X+Z}{n},
\qquad
\mathfrak f_n=\frac{3X-Y-Z}{2}.
$$


∎

This evaluates the contact-independent transverse force, including both final moment-source terms.

It does **not** remove $\kappa$:


$$
\boxed{
\Xi_n
=
2L(n!)^2-\mathscr K_n^\circ.
}
\tag{6.4}
$$



Nor does (6.3) truncate the physical producer. It is an identity for the coefficients entering this invariant. The physical source still runs through $2n+2$, and the retained terminal return remains unchanged.

---

# 7. A joint divisor theorem for the two saturated endpoint charts

Let


$$
c_j=(\alpha_j,\beta_j,\gamma_j),\qquad j=0,3,
$$


be the coordinates of the two **actual primitive contact rows**. They satisfy


$$
c_j\cdot(P,Q,F)=0,
$$




$$
\widehat R_j=c_j\cdot(\widehat h,\widehat\ell,0),
$$




$$
\mathcal E_j^\circ=c_j\cdot(A^\circ,B^\circ,C).
$$



## 7.1 The actual integral contact cross-product scalar

Set


$$
g_z=\gcd(|P|,|Q|,|F|),
\qquad
z^*=\frac1{g_z}(P,Q,F).
$$


The actual seed and transfer prove that $g_z$ has no prime factor exceeding $N$.

Since $z^*$ is primitive and $c_0\times c_3$ is an integral vector parallel to $z^*$, there is an integer $\lambda_{\mathrm{ct}}$ such that


$$
\boxed{
c_0\times c_3=\lambda_{\mathrm{ct}}z^*.
}
\tag{7.1}
$$



This scalar includes the actual contact-row normalizations. It is not obtained from raw adjugate rows.

It may be computed without division by $F$: choose integers $a,b,c$ with


$$
aP^*+bQ^*+cF^*=1,
$$


and contract $(a,b,c)$ with $c_0\times c_3$.

For the nondegenerate retained endpoint construction the two contact rows are independent, so $\lambda_{\mathrm{ct}}\ne0$. If independence were absent in another construction, the resulting divisibility by zero would be uninformative; that hypothesis cannot be suppressed in a height application.

## Proposition 7.1 — Complete cross-affine identity



$$
\boxed{
\widehat R_0\mathcal E_3^\circ
-\widehat R_3\mathcal E_0^\circ
=
\frac{\lambda_{\mathrm{ct}}}{g_z}
(\kappa F-\Theta).
}
\tag{7.2}
$$



### Proof

The left side equals


$$
(c_0\times c_3)\cdot
\left((\widehat h,\widehat\ell,0)
\times(A^\circ,B^\circ,C)\right).
$$


Using (7.1), the remaining scalar is


$$
PC\widehat\ell-QC\widehat h
+F(\widehat hB^\circ-\widehat\ell A^\circ)
=
-CM+F\mathscr K_n^\circ
=
\kappa F-\Theta.
$$


∎

This identity retains the complete $\kappa$. It is the basis of the joint resonance bound.

## 7.2 Primitive numerator of the auxiliary affine ratio

Define the all-prime gcd


$$
g=\gcd(|F|,|CM|),
$$


and set


$$
\boxed{
T_{\mathrm{aff}}=\frac{\Theta}{g}
=\frac{CM}{g}+\frac Fg\,\Xi_n,
\qquad
d_{\mathrm{aff}}=\frac{|F|}{g}.
}
\tag{7.3}
$$


Then


$$
\boxed{\gcd(|T_{\mathrm{aff}}|,d_{\mathrm{aff}})=1.}
\tag{7.4}
$$



Thus these are the primitive numerator and denominator of the **auxiliary ratio $\Theta/F$**, up to sign. They are not the endpoint or weighted approximation denominator.

The identity follows from


$$
\gcd(F,\Theta)=\gcd(F,CM).
$$



For each endpoint, put


$$
D_j=\frac{|\widehat R_j|}
{\gcd(|\widehat R_j|,|F|)}.
\tag{7.5}
$$


Then the saturation factor has the exact integer description


$$
\boxed{
\mathfrak S_j
=
\gcd(|T_{\mathrm{aff}}|,D_j)_{>N}.
}
\tag{7.6}
$$



This equality follows prime by prime from


$$
v_p(\mathfrak S_j)
=
\left(\min(v_p(\Theta),v_p(\widehat R_j))-v_p(F)\right)_+.
$$



The individual equality (7.6) is an exact normalization. The new restriction is the two-endpoint theorem next.

## Theorem 7.2 — Simultaneous saturation pays reduced contact collision

Define


$$
\boxed{
C_{\mathrm{sat}}
=
\left(
\frac{|\lambda_{\mathrm{ct}}|}
{\gcd\!\left(|\lambda_{\mathrm{ct}}|,\ |F|/\mathcal I_n\right)}
\right)_{>N}.
}
\tag{7.7}
$$


Then


$$
\boxed{
\gcd(\mathfrak S_0,\mathfrak S_3)\mid C_{\mathrm{sat}}.
}
\tag{7.8}
$$



### Proof

Fix $p>N$. Write


$$
f=v_p(F),\qquad a=v_p(\mathcal I_n),
\qquad s_j=v_p(\mathfrak S_j).
$$



If one of $s_0,s_3$ is zero, there is nothing to prove. Suppose both are positive.

The full saturation theorem gives, for both endpoints,


$$
v_p(\mathcal E_j^\circ)=f-a.
\tag{7.9}
$$


Also,


$$
v_p(\widehat R_j)\ge f+s_j,
\qquad
v_p(\Theta)>f.
$$


Since $\kappa$ is a unit,


$$
v_p(\kappa F-\Theta)=f.
$$


The right side of (7.2) therefore has valuation


$$
v_p(\lambda_{\mathrm{ct}})+f,
$$


because $g_z$ is a unit at $p$.

The left side has valuation at least


$$
f+\min(s_0,s_3)+(f-a).
$$


Consequently,


$$
\min(s_0,s_3)
\le
v_p(\lambda_{\mathrm{ct}})-(f-a).
$$


The exponent of $p$ in $C_{\mathrm{sat}}$ is precisely


$$
\bigl(v_p(\lambda_{\mathrm{ct}})-(f-a)\bigr)_+.
$$


This proves (7.8). ∎

This is a target-specific divisor restriction on the **evaluated saturated charts**. In particular, if $\lambda_{\mathrm{ct}}$ is a unit at $p>N$, both endpoints cannot have positive saturated excess at that prime.

## 7.3 One joint resonance gcd, not two unrestricted resonance factors

Set


$$
H_{\mathrm{ref}}=\operatorname{lcm}(D_0,D_3),
$$




$$
\boxed{
J_{\mathrm{res}}
=
\gcd(|T_{\mathrm{aff}}|,H_{\mathrm{ref}})_{>N}.
}
\tag{7.10}
$$


Equation (7.6) gives


$$
\operatorname{lcm}(\mathfrak S_0,\mathfrak S_3)=J_{\mathrm{res}}.
$$


Combining this with Theorem 7.2,


$$
\boxed{
\mathfrak S_0\mathfrak S_3
\mid J_{\mathrm{res}}\,C_{\mathrm{sat}}.
}
\tag{7.11}
$$



Finally, the retained full excess factorization yields


$$
\boxed{
\mathfrak X_0\mathfrak X_3
\mid
\mathcal I_n^2\,J_{\mathrm{res}}\,C_{\mathrm{sat}}.
}
\tag{7.12}
$$


Likewise,


$$
\boxed{
\Delta_0\Delta_3
\mid
\mathcal I_n^2\mathcal Z_0\mathcal Z_3
J_{\mathrm{res}}C_{\mathrm{sat}}.
}
\tag{7.13}
$$



### What has improved

The two saturated endpoint costs cannot overlap freely. Their overlap must be paid by the actual contact cross-product scalar, after subtracting the already saturated force-overlap depth $f-a$.

This is not obtained by renaming $\sum v_p(1+\Omega)$. It is an additional divisibility constraint relating the two actual evaluated charts.

### What remains unproved

No subfactorial estimate is proved for either


$$
J_{\mathrm{res}}
\quad\text{or}\quad
C_{\mathrm{sat}}.
$$



The existing source and collision filters remain in force. Theorem 7.2 does not authorize removing them again, replacing their full valuations by radicals, or claiming a second saving already contained in an accepted stronger certificate.

A concrete sufficient next lemma is now


$$
\boxed{
\log J_{\mathrm{res}}+\log C_{\mathrm{sat}}
=o(n\log n)
}
\tag{7.14}
$$


on a suitable infinite original subsequence, with $T_{\mathrm{aff}}$ evaluated by (6.3)–(6.4).

The fixed-$C$ absorption obstruction remains exactly a height obstruction to that particular repair. It supplies no estimate for (7.14).

---

# 8. Construction, forcing, contents, and final normalization

None of the preceding reductions changes the producer.

## 8.1 Complete physical forcing and terminal

The physical source remains


$$
\mathfrak f_k
=
(n+1)a_k-nk\,a_{k-1}
+\frac{(n-1)k(k-1)}2a_{k-2}
+\frac{k(k-1)(k-2)}2a_{k-3}
$$


through


$$
\boxed{K=2n+2.}
$$



The Green solution through $b_{K+1}$ retains $\mathfrak f_K$ with coefficient $1$. The original terminal-return functional is unchanged.

The complete endpoint residual remains


$$
\boxed{
C_j^{\mathrm{complete}}
=
\mathcal E_j^\circ+
2n!m!(\alpha_j\rho_n+\beta_j\rho_{n+1}).
}
\tag{8.1}
$$


It is not replaced by $\mathcal E_j^\circ$, $\mathscr K_n^\circ$, or $T_{\mathrm{aff}}$.

The fixed-seed exponential boundary $E_n$ remains in the actual endpoint numerator. Its cancellation in the transverse identity (6.3) is not a deletion from the producer.

## 8.2 Both corrected columns and all row contents

Retain


$$
x=T^{-1}(n!t),\qquad y=T^{-1}\widehat w,
$$




$$
S=
\begin{pmatrix}
1&-n&n(n+1)\\
0&1&-2n\\
0&0&1
\end{pmatrix},
\qquad sx=Sx,\quad sy=Sy,
$$




$$
u=(-sx_0,\ sx_0-sx_1,\ sx_1-sx_2,\ sx_2),
$$




$$
v=(1-sy_0,\ sy_0-sy_1,\ sy_1-sy_2,\ sy_2).
$$



The exterior $+1$ remains. The least simultaneous clearer is taken over all eight entries, followed by the actual two-entry row-content divisions.

The accepted $3375$ contents remain


$$
(113940000,\ 9780750,\ 10125,\ 1).
$$


They are not replaced by $\lambda_{\mathrm{ct}}$, $\eta_j$, $\mathcal Z_j$, or a large-prime gcd.

## 8.3 Actual all-prime endpoint denominator



$$
\boxed{
d_j=
\frac{|n!R_j|}
{\gcd(|n!R_j|,\ |E_nR_j+C_j^{\mathrm{complete}}|)}.
}
\tag{8.2}
$$



Every prime remains in this gcd.

## 8.4 Actual all-prime weighted primitive pair

For the retained reduced weight $\lambda=a/k_{\mathrm{wt}}$, keep


$$
J_{\mathrm{wt}}
=
B_{\mathrm{wt}}\widetilde v_0
-A_{\mathrm{wt}}\widetilde v_3,
$$




$$
T_{\mathrm{wt}}
=
aJ_{\mathrm{wt}}
+k_{\mathrm{wt}}A_{\mathrm{wt}}\widetilde v_3,
$$




$$
F_{\mathrm{gcd}}
=
\gcd(|A_{\mathrm{wt}}|,|a|)
\gcd(|B_{\mathrm{wt}}|,|a-k_{\mathrm{wt}}|),
$$




$$
G_{\mathrm{wt}}
=
\gcd(k_{\mathrm{wt}},|J_{\mathrm{wt}}|),
$$




$$
H_{\mathrm{gcd}}
=
\gcd\!\left(
h_{\mathrm{end}},
\frac{|T_{\mathrm{wt}}|}
{F_{\mathrm{gcd}}G_{\mathrm{wt}}}
\right).
$$



The actual primitive pair remains


$$
\boxed{
q_\lambda=
\frac{k_{\mathrm{wt}}h_{\mathrm{end}}
|A_{\mathrm{wt}}B_{\mathrm{wt}}|}
{F_{\mathrm{gcd}}G_{\mathrm{wt}}H_{\mathrm{gcd}}},
}
$$




$$
\boxed{
p_\lambda=
\operatorname{sgn}(A_{\mathrm{wt}}B_{\mathrm{wt}})
\frac{T_{\mathrm{wt}}}
{F_{\mathrm{gcd}}G_{\mathrm{wt}}H_{\mathrm{gcd}}}.
}
\tag{8.3}
$$



No auxiliary affine denominator replaces this one.

## 8.5 Whole nonzero same-index error

The whole error remains


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda e_3\alpha_{n,2}
(\lambda-\Lambda_{n,2}).
}
\tag{8.4}
$$



The five accepted $3375$ whole forms remain nonzero and have absolute value greater than $1$. Nothing here changes those finite evaluations.

---

# 9. Proof ledger and exact-arithmetic status

| Statement | Status |
|---|---|
| Natural transfer, determinant, actual-unit remainder | Reused proved results |
| Explicit inverse transfer | Proved |
| Both coordinates of the two-step defect | Proved |
| Degree-$11$ two-step common-content bound | Proved, fixed-block scope |
| Reference-preserving block composition | Proved |
| Exact cofactor valuation $(a_t-d)_+=(a_t-a_n)_+$ | Proved |
| Medium-prime decomposition | Exact; no bound asserted |
| Actual-seed two-dimensional reduction and telescope | Proved with explicit chart payments |
| Second-order scalar recurrence | Proved on stated scalar charts |
| Exterior content equals terminal $\mathcal I_t$ | Proved |
| Subfactorial multiplicative-block cofactor | **Not proved** |
| Evaluated Wronskian-source formula for $\mathscr K_n^\circ$ | Proved |
| Joint saturated-chart divisor theorem | Proved |
| Subfactorial $J_{\mathrm{res}}C_{\mathrm{sat}}$ | **Not proved** |
| Favorable infinite primitive whole forms | **Not established** |
| Irrationality or rationality of $e+\pi$ | **Unresolved** |

## Bounded exact arithmetic

No numerical computation was executed. No accepted bounded computation is requested again.

No new numerical calculation is needed for the proofs above. A bounded symbolic audit of the genuinely new formulas would have these inputs:

- the displayed $\mathsf U_n^{-1}$;
- the actual reference recurrence;
- symbolic $z_{s+1}=\mathsf U_sz_s$;
- the finite Green kernel and the two retained final-source identities;
- two integral contact coordinate rows satisfying the actual syzygy.

Its expected verifiable outputs are:

1. the differences between the two-step matrix product and (2.2)–(2.4) are zero;
2. $G(-NB,A)+\mathscr R_2(n)=0$;
3. $\det\mathsf A_s-\det\mathsf U_s\,F_s/F_{s+1}=0$;
4. the numerator identity (5.13);
5. the difference between (6.2) and (6.3) is zero after the stated source substitutions;
6. the complete cross-affine identity (7.2), including the sign of $\kappa F-\Theta$.

These are finite rational-polynomial identities. They are not alignment samples and cannot establish either remaining infinite-family estimate.

---

# Conclusion

The backward defect is now more explicit than a transported-vector specification:

- its two-step value is evaluated;
- its block composition retains the actual reference directions and scalar multipliers;
- for $t=15n$ and $t=105n$, it has an actual-seed reduction to a two-dimensional recurrence plus a scalar telescope;
- all scalarization denominators are displayed;
- the intrinsic exterior content of that reduction is exactly the terminal alignment divisor.

The last point identifies the precise obstruction to obtaining a free primitivity argument from reduction of order:


$$
\boxed{
\text{primitive normalization of the actual exterior reduction costs }\mathcal I_t.
}
$$


It does not prove that a subfactorial cofactor is impossible.

On the affine side, the actual Green source gives a completely evaluated transverse scalar, and the two saturated endpoint charts satisfy the joint restriction


$$
\boxed{
\mathfrak S_0\mathfrak S_3
\mid J_{\mathrm{res}}C_{\mathrm{sat}},
}
$$


where simultaneous resonance is paid by the actual contact cross-product scalar after removal of the already saturated overlap.

The exact remaining mathematical bottlenecks are:

1. **Alignment:** bound the newly acquired terminal depth
   

$$
\sum_{p>bn+2}(a_{bn}-a_n)_+\log p
$$


   subfactorially, using the actual scalar/telescoping system without circular primitive normalization.

2. **Saturation:** bound the explicit joint gcd
   

$$
J_{\mathrm{res}}
   =
   \gcd\!\left(
   |T_{\mathrm{aff}}|,
   \operatorname{lcm}(D_0,D_3)
   \right)_{>N}
$$


   together with the reduced actual collision factor $C_{\mathrm{sat}}$, with the complete $\kappa$, source prefix, final source terms, and terminal retained.

3. **Approximation:** control the actual all-prime final gcd, the resulting primitive denominator, and the whole nonzero same-index error.



$$
\boxed{
\text{No unconditional proof or disproof of the irrationality of }e+\pi
\text{ has been obtained.}
}
$$


