> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, turn 3: a saturated five-tail calculation, an explicit scalar obstruction, and the normalized $b=4$ implication

I do not obtain an irrationality decision for $e+\pi$, or a global denominator estimate strong enough to decide the proportional-center route.

The new arithmetic results are:

1. An exact **bordered-maximal-minor formula for $h/\gamma$**, retaining the genuine high block, matching row, and both endpoint rows.
2. At $p=n+2$, an explicit **saturated high-row system on five tail variables**, together with the matching row, both endpoint rows, and the restricted falling metric.
3. A two-residue obstruction to a uniform matching chart. Away from that obstruction, $h$ is a $p$-unit. At the obstruction, a second calculation shows that—unless the matching row itself requires further saturation—$p$ actually divides $h/\gamma$. Thus endpoint integrality alone cannot replace this calculation.
4. A proof of the **infinite implication** of the coordinator’s normalized four-prime $b=4$ certificate, conditional on the supplied scalar-transfer and complete-error theorems. The global contraction gcd causes no difficulty for that implication because only valuations, not globally normalized residues, are used.

There is an important domain issue:

> On the selected family $n=P-1,\ b=(P-1)/2001$, with $P$ an odd prime, $n$ is even. Therefore $n+2$ is not prime. The requested $d=2$ calculation is a useful auxiliary local model, but it cannot remove an additional prime at those same indices. The next possible offset on that family is $d=3$.

I keep that distinction throughout.

---

## 1. A global bordered-minor identity for the scalar factor

Fix a finite normal index $n\ge b\ge3$. Put $N=b+1$, and let


$$
\mathcal W=\ker_{\mathbb Q}\begin{bmatrix}R\\ \boldsymbol s\end{bmatrix},
\qquad
\boldsymbol s=\boldsymbol e+\boldsymbol t,
$$


where $R$ consists of the **actual** $b-2$ retained high rows. Thus $\dim\mathcal W=2$.

Choose any integer matrix $A_0$ of size $(N-2)\times N$, of full row rank, with the same rational row space as $[R;\boldsymbol s]$. It may contain nonprimitive row factors.

For a full-row-rank integer matrix $M$, write


$$
\Delta(M)=\gcd\{|\text{maximal minors of }M|\}.
$$


Set


$$
\Delta_A=\Delta(A_0),\qquad
\Delta_e=\Delta\begin{bmatrix}A_0\\ \boldsymbol e\end{bmatrix}.
$$



Let


$$
\mathscr L=\mathcal W\cap\mathbb Z^N,
\qquad
\boldsymbol e(\mathscr L)=h\mathbb Z.
$$


Retain the adapted basis and endpoint notation


$$
\mathscr L=\mathbb Zz_0\oplus\mathbb Zz_1,\quad
\boldsymbol ez_0=0,\quad \boldsymbol ez_1=h,
$$




$$
D_0\boldsymbol xz_0=a,\qquad
D_0\boldsymbol xz_1=b_{\rm end},\qquad
\gamma=\gcd(h,a,b_{\rm end}).
$$



Because $\mathscr L$ is saturated, the integer-valued functional


$$
D_0\boldsymbol x:\mathscr L\longrightarrow\mathbb Z
$$


has an extension to an integer row $X_0\in\mathbb Z^N$. Define


$$
\Delta_x=\Delta\begin{bmatrix}A_0\\ X_0\end{bmatrix}.
$$



### Proposition 1.1 — exact scalar support formula

One has


$$
\boxed{
h=\frac{\Delta_e}{\Delta_A},\qquad
\gcd(|a|,|b_{\rm end}|)=\frac{\Delta_x}{\Delta_A},
}
\tag{1.1}
$$


and therefore


$$
\boxed{
\frac h\gamma=
\frac{\Delta_e}{\gcd(\Delta_e,\Delta_x)}.
}
\tag{1.2}
$$



In particular, at every prime,


$$
\boxed{
v_p(h/\gamma)=
\max\{0,v_p(\Delta_e)-v_p(\Delta_x)\}.
}
\tag{1.3}
$$



#### Proof

Apply Smith reduction to $A_0$:


$$
U A_0 V=[D\;0\;0],
$$


where $U,V$ are unimodular and $D$ is a nonsingular diagonal matrix of size $N-2$. Then


$$
|\det D|=\Delta_A,
$$


and the last two columns of $V$ form a basis of the saturated kernel.

For any appended integer row $r$, all nonzero maximal minors of $[A_0;r]$, after these unimodular operations, are $\det D$ times one of the last two coordinates of $rV$. Consequently


$$
\frac{\Delta([A_0;r])}{\Delta_A}
=\gcd r(\mathscr L).
$$


Apply this first to $r=\boldsymbol e$, and then to $r=X_0$. Formula (1.2) follows by taking the gcd. ∎

This identity is independent of the chosen integer row clearers and of the integer extension $X_0$.

At a prime $p>n$, where the whole endpoint row $\boldsymbol x$ is $p$-integral and $D_0$ is a unit, the same calculation can be performed locally using $\boldsymbol x$ itself. Thus the support of $h/\gamma$ above $n$ is determined by a comparison of the two genuine bordered-minor ideals, not by endpoint denominators.

A corresponding, but presently too weak, intrinsic size bound is


$$
\boxed{
\frac h\gamma\le h
\le
\sqrt{N}\,
\frac{\sqrt{\det(A_0A_0^T)}}{\Delta_A}.
}
\tag{1.4}
$$


Indeed, the gcd of the coordinates of the exterior product is at most its Euclidean norm, and


$$
\|(\wedge A_0)\wedge\boldsymbol e\|
\le \|\wedge A_0\|\,\|\boldsymbol e\|.
$$


The quotient on the right is the covolume of the saturated row lattice, so arbitrary row scaling has canceled.

**Limitation.** Neither (1.2) nor (1.4) proves that $h/\gamma$ is $n$-smooth, or gives an $O(n)$ logarithmic bound. The local calculation below identifies precisely what a usable matching-chart certificate must establish.

---

# 2. The auxiliary $d=2$ domain

For Sections 2–8 assume


$$
\boxed{
n=p-2,\qquad p\text{ odd prime},\qquad b\ge6,\qquad 2b-3<p,\qquad m=1.
}
\tag{2.1}
$$


The last condition ensures all derivative orders used below are $<p$. Put


$$
s=b-4.
$$


There will be five tail variables, indexed by


$$
j=s,s+1,s+2,s+3,s+4=b.
$$



Use the actual rows


$$
R_{lj}=E_{p-2+l,l+j-1},
\qquad 1\le l\le b-2,\quad 0\le j\le b.
\tag{2.2}
$$



Let $R_H$ be the rows $l=3,\ldots,b-2$. Split its columns into the first $b-4$ and last five:


$$
R_H=[B\;C].
$$



For $l=a+2$, $1\le a\le b-4$, the Rodrigues reduction gives


$$
R_{a+2,j}
\equiv
\left.\frac{d^{a+j+1}}{dx^{a+j+1}}\bigl(x^aH_a(x)\bigr)\right|_{x=1}
\pmod p.
$$


This vanishes for $j>a-1$, and at $j=a-1$ equals $(2a)!$, a unit. Thus


$$
\boxed{B\in\operatorname{GL}_{b-4}(\mathbb Z_p),\qquad C\equiv0\pmod p.}
\tag{2.3}
$$



The exact unit-pivot chart for these rows is


$$
z=Jy,\qquad
J=\begin{pmatrix}-B^{-1}C\\ I_5\end{pmatrix},
\qquad y\in\mathbb Z_p^5.
\tag{2.4}
$$


In particular every preceding coordinate of $z$ is divisible by $p$.

No factorial or nonunit division has been used in this elimination.

---

## 3. Both remaining high rows, with exact $p$-content removed

Define


$$
E_j=E_{p-1,j}\pmod p,\qquad
c_j=(-1)^j j!\pmod p.
\tag{3.1}
$$


All $c_j$ occurring here are units.

The first remaining row is $R_1$. Its Schur row reduces to


$$
R_1J\equiv(E_s,E_{s+1},\ldots,E_{s+4}).
\tag{3.2}
$$



The second remaining row is $R_2=(E_{p,j+1})_j$. It is divisible by $p$ over the integers, before any Schur elimination. The already justified positive-derivative congruence gives


$$
\frac{E_{p,j+1}}p\equiv2(-1)^j j!=2c_j\pmod p.
$$


Hence


$$
\boxed{
\frac{R_2J}{p}\equiv2(c_s,c_{s+1},\ldots,c_{s+4}).
}
\tag{3.3}
$$



There is no further hidden content in these two residual high equations.

### Proposition 3.1 — complete saturation of the high block

The reductions of (3.2) and (3.3) are linearly independent. Consequently the following equations define the saturated high-row kernel over $\mathbb Z_p$:


$$
R_Hz=0,\qquad R_1z=0,\qquad (R_2/p)z=0.
\tag{3.4}
$$



#### Proof

The exact adjacent differential identity


$$
\frac{\mathscr F_p'}p=B_{p-1}\mathscr F_{p-1},
\qquad \mathscr F_k=x^kH_k,
$$


gives, after reduction,


$$
\boxed{
E_{j+2}+jE_{j+1}-2jE_j+2jE_{j-1}=2c_j.
}
\tag{3.5}
$$


For $j\ge1$, the same left-hand operator applied to $c_j$ is zero:


$$
c_{j+2}+jc_{j+1}-2jc_j+2jc_{j-1}=0.
\tag{3.6}
$$


If $E_j$ were proportional to $c_j$ on the five tail positions, applying (3.5) at $j=s+1$ would contradict $2c_{s+1}\ne0$.

Thus the two residual rows have rank two modulo $p$. Together with the unit block $B$, the normalized high block has full row rank modulo $p$, so its row lattice is saturated. ∎

This proves exact removal of the relevant high-row $p$-content:

- the first Schur row has content exponent $0$;
- the second raw Schur row has content exponent exactly $1$;
- after that division, their combined rank is already saturated.

---

# 4. The actual endpoint rows at $d=2$

Put


$$
P=L_{p-2},\qquad U=L_{p-1},\qquad
\varepsilon=\left(\frac{-1}{p}\right).
$$


The Legendre reflection congruences give


$$
P(y)\equiv\varepsilon(1/2-y),\qquad
U(y)\equiv\varepsilon\pmod p.
\tag{4.1}
$$


Consequently


$$
P(1)\equiv-\varepsilon/2,\qquad U(1)\equiv\varepsilon.
$$



The relevant second-kind moments have $p$-unit denominators. Therefore


$$
w_P\equiv-2\varepsilon,\qquad w_U\equiv0\pmod p.
\tag{4.2}
$$


Also


$$
G=\frac{(-1)^{p-2}2^{2p-1}}{p-1}\equiv2\pmod p.
\tag{4.3}
$$



Write


$$
T_{P,j}=T_j(P),\qquad T_{U,j}=T_j(U).
$$


These are $p$-integral: the surviving terms in (4.1) have factorial indices below $p$, and every other coefficient supplies the factor $p$ needed to cancel the sole possible factorial pole.

Substitution into the **whole endpoint formulas** yields


$$
\boxed{
t_j\equiv-\frac{\varepsilon}{2}
       \left(T_{P,j}+\frac12T_{U,j}\right),
\qquad
x_j\equiv-\varepsilon T_{U,j}
\pmod p.
}
\tag{4.4}
$$


Thus $D_0$ is a $p$-unit here, independently of any assertion about $h$.

---

## 5. Eliminating the partial-sum constants that actually cancel

We next simplify the matching row without discarding constants that survive.

Since $2^{p-1}/((p-1)!)^2\equiv1$, Rodrigues gives


$$
T_{U,j-1}-T_{U,j}\equiv E_j.
\tag{5.1}
$$



The exact Legendre derivative relation


$$
Q(y)U'(y)=(p-1)\bigl((y-\tfrac12)U(y)+P(y)\bigr),
\qquad Q(y)=y^2-y+\tfrac12,
$$


combined with (3.5), gives


$$
\boxed{
\ell_j(P)\equiv\tfrac12E_j-E_{j-1}-c_j.
}
\tag{5.2}
$$


For clarity, applying $\ell_j$ to the derivative relation first gives


$$
\ell_j(P)\equiv
(j+\tfrac12)E_j-(j+1)E_{j-1}
-\tfrac j2E_{j+1}-\tfrac12E_{j+2};
$$


equation (3.5) reduces this to (5.2).

Set


$$
W_j=T_{P,j}+\tfrac12T_{U,j}.
$$


Equations (5.1)–(5.2) imply


$$
W_j-W_{j-1}\equiv-E_j+E_{j-1}+c_j.
$$


Therefore, for $0\le r\le4$,


$$
\boxed{
W_{s+r}\equiv W_s+E_s-E_{s+r}
+\sum_{i=1}^r c_{s+i}.
}
\tag{5.3}
$$



Normalize the five rows by the unit $c_s$:


$$
d_r=\frac{c_{s+r}}{c_s}
=(-1)^r(s+1)(s+2)\cdots(s+r),
$$




$$
e_r=\frac{E_{s+r}}{c_s},\qquad
f_r=\sum_{i=1}^r d_i,\qquad
g_r=\sum_{i=1}^r e_i,
\tag{5.4}
$$


with $d_0=1,\ f_0=g_0=0$. Finally put


$$
\boxed{
\Theta=\frac{2\varepsilon-W_s-E_s}{c_s}.
}
\tag{5.5}
$$



After the proved high-row saturation, the reduced five-tail system is


$$
\boxed{
\begin{aligned}
\boldsymbol d\,y&=0,\\
\boldsymbol e_E\,y&=0,\\
(\boldsymbol f-\Theta\boldsymbol 1)y&=0,
\end{aligned}}
\tag{5.6}
$$


where $\boldsymbol e_E=(e_0,\ldots,e_4)$ and $\boldsymbol1=(1,\ldots,1)$.

The two endpoint rows are


$$
\boxed{
B(1)\equiv\boldsymbol1\,y,
}
\tag{5.7}
$$




$$
\boxed{
A(1)\equiv
-\varepsilon T_{U,s}\,\boldsymbol1\,y
+\varepsilon c_s\,\boldsymbol g\,y.
}
\tag{5.8}
$$



These formulas have the requested cancellation boundary:

- $W_s$ survives in the nonzero-endpoint matching parameter $\Theta$.
- $T_{U,s}$ survives in the general $A$-endpoint row.
- Both constants cancel from the zero-$B(1)$ direction.
- The jet residues $E_s,E_{s+1},E_{s+2}$ do **not** disappear. They are the remaining factorial-function obstruction.

In particular the zero-endpoint direction is cut out modulo $p$ by


$$
\boxed{
\boldsymbol1\,y=\boldsymbol d\,y
=\boldsymbol f\,y=\boldsymbol e_E\,y=0.
}
\tag{5.9}
$$



---

# 6. A uniform matching chart and its first exact obstruction

The rows $\boldsymbol1,\boldsymbol d,\boldsymbol f$ are always independent in this domain. Indeed, their minor on columns $0,1,2$ is


$$
\boxed{
\det
\begin{pmatrix}
1&1&1\\
1&-(s+1)&(s+1)(s+2)\\
0&-(s+1)&(s+1)^2
\end{pmatrix}
=-(s+1)\ne0.
}
\tag{6.1}
$$



Define the coefficients fitting $\boldsymbol e_E$ on its first three positions:


$$
A=e_2+(s+1)(e_1-e_0),
$$




$$
C=\frac{(s+2)A-e_1-(s+1)e_0}{s+1},
\qquad B=e_0-A.
\tag{6.2}
$$


Thus


$$
e_r=A+B d_r+C f_r\qquad(r=0,1,2).
$$



Put


$$
H=s^2+5s+8.
$$


The recurrence (3.5), at the two interior positions, proves the following exact criterion.

### Proposition 6.1 — two-residue matching-chart obstruction

The rank of


$$
[\boldsymbol1;\boldsymbol d;\boldsymbol f;\boldsymbol e_E]
$$


is three, rather than four, **if and only if**


$$
\boxed{
HA=2(s+1)(s+3),\qquad HC=2(H-1).
}
\tag{6.3}
$$


If $H=0$, these equations are impossible, because the second would read $0=-2$. Thus rank four is automatic when $H=0$.

#### Derivation

The fitted row satisfies the required recurrence at the two interior positions precisely when


$$
(s+2)A-2(s+1)C=-2(s+1),
$$




$$
(s+3)A+(s+1)^2C=2(s+1)(s+2).
\tag{6.4}
$$


The determinant of this two-equation system is $(s+1)H$. Solving it gives (6.3). Conversely, these equations make the fitted row satisfy the recurrence, whose leading coefficient is one, so they force agreement at positions $3$ and $4$ as well. ∎

### Consequence away from the obstruction

If at least one equation in (6.3) fails, then


$$
\operatorname{rank}
[\boldsymbol e_E;\boldsymbol d;\boldsymbol f-\Theta\boldsymbol1]=3,
$$


and appending $\boldsymbol1$ raises the rank to four.

Thus the matching row is already saturated, and the endpoint sum maps the local rank-two kernel onto $\mathbb Z_p$. Hence


$$
\boxed{
v_p(h)=v_p(D_0)=v_p(\gamma)=v_p(k)=0
}
\tag{6.5}
$$


at every finite normal index satisfying this chart condition.

This conclusion is independent of $\Theta$ and $T_{U,s}$. It comes from an actual matching chart, not from endpoint integrality.

---

## 7. What happens at the obstruction

Suppose now that (6.3) holds. Then $H\ne0$, and


$$
\boldsymbol e_E=A\boldsymbol1+B\boldsymbol d+C\boldsymbol f,
$$


with


$$
A=\frac{2(s+1)(s+3)}H,\qquad
C=\frac{2(H-1)}H.
\tag{7.1}
$$



There are two distinct cases.

### 7.1 Matching does not require further saturation

Assume


$$
\boxed{A+C\Theta\ne0.}
\tag{7.2}
$$


Then the three constraint rows in (5.6) span exactly


$$
\operatorname{span}\{\boldsymbol1,\boldsymbol d,\boldsymbol f\}.
$$


They have rank three, so this is a saturated matching chart, but the endpoint sum vanishes on its reduction. Therefore $p\mid h$.

More can be proved: $p$ does **not** divide $\gamma$.

On this kernel, (5.8) reduces to $\varepsilon c_s\boldsymbol g$. The constant $T_{U,s}$ has canceled. Moreover


$$
\boldsymbol g=A\boldsymbol r+B\boldsymbol f+C\boldsymbol k,
$$


where


$$
r_j=j,\qquad k_j=\sum_{i=1}^j f_i.
$$


A direct $4\times4$ minor gives


$$
\boxed{
\det[\boldsymbol1;\boldsymbol d;\boldsymbol f;\boldsymbol g]_{\{0,1,2,4\}}
=-\frac{4(s+1)^2(s+2)}H\ne0.
}
\tag{7.3}
$$


Thus the actual $A$-endpoint takes a unit value on the local kernel.

For an explicit check of the algebra, put $u=s+1$, so $H=u^2+3u+4$. On these four columns,


$$
\det[\boldsymbol1;\boldsymbol d;\boldsymbol f;\boldsymbol r]
=2u(u^3+4u^2+5u+1),
$$




$$
\det[\boldsymbol1;\boldsymbol d;\boldsymbol f;\boldsymbol k]
=-2u^2(u^2+3u+1).
$$


Insert


$$
A=\frac{2u(u+2)}H,\qquad C=\frac{2(u^2+3u+3)}H
$$


to obtain (7.3).

Since $D_0$ is a unit, the existence of an $A$-endpoint unit implies $v_p(\gamma)=0$. We have proved


$$
\boxed{
v_p(h/\gamma)=v_p(h)\ge1
}
\tag{7.4}
$$


under (6.3) and (7.2).

This is a useful obstruction statement: a uniform proof that $h/\gamma$ is a unit must exclude the explicit factorial congruences (6.3), or handle their scalar contribution. The integrality of both endpoint rows does not exclude them.

I have not proved that these exceptional congruences occur at actual indices. Equation (7.4) is a **conditional local consequence**, not finite evidence of occurrence.

### 7.2 Matching requires further saturation

If instead


$$
A+C\Theta=0,
\tag{7.5}
$$


the matching row reduces into the saturated high-row span. Its next $p$-adic digit is indispensable.

There is an exact saturation procedure, but no uniform depth bound proved here:

1. Use a unit $2\times2$ minor of the two saturated residual high rows to parametrize their kernel by three variables.
2. Pull back the exact matching row to a row $m\in\mathbb Z_p^3$.
3. Divide it by
   

$$
p^\mu,\qquad \mu=\min_i v_p(m_i).
$$


4. Append the actual endpoint-sum and $A$-endpoint rows in this chart.

The divided matching row is primitive and gives the complete saturated local system. However, in case (7.5), neither $\mu$ nor its primitive reduction has been bounded by the preceding modulo-$p$ calculation.

Thus the high block is completely saturated in Sections 2–3, and the full matching chart is completely resolved except at the explicit condition (7.5). I do not label the unsaturated reduction there as the actual lattice reduction.

---

# 8. The restricted falling metric on the five-tail system

Here


$$
\ell=n+2=p,\qquad
\omega_j=\frac{p!}{(p-j)!}.
$$


For $j\ge1$,


$$
\frac{\omega_j}{p}\equiv(-1)^{j-1}(j-1)!\pmod p.
\tag{8.1}
$$



Let $z=Jy$ satisfy the high rows and put


$$
D_j=(-1)^{j-1}(j-1)!\,y_{j-s},
\qquad s\le j\le s+4.
$$


Every weighted coordinate of $\operatorname{diag}(\omega_j)z$ is divisible by $p$.

The first unit-pivot high row, $l=3$, supplies the one additional coordinate needed after this division. Using


$$
E_{p+1,2}\equiv2,\qquad
\frac{E_{p+1,j+2}}p
\equiv2(j+2)(-1)^{j-1}(j-1)!
\quad(j\ge1),
$$


one obtains


$$
\boxed{
\frac{z_0}{p}\equiv-\sum_{j=s}^{s+4}(j+2)D_j.
}
\tag{8.2}
$$


All other preceding weighted coordinates vanish after division by $p$ and reduction.

Therefore, for any two high-kernel vectors $z,z'$,


$$
\boxed{
\frac{z^T\Omega z'}{p^2}
\equiv
\sum_{j=s}^{s+4}D_jD_j'
+
\left(\sum_{j=s}^{s+4}(j+2)D_j\right)
\left(\sum_{j=s}^{s+4}(j+2)D_j'\right).
}
\tag{8.3}
$$


Equivalently, in scaled tail coordinates the restricted matrix is


$$
\boxed{
I_5+\boldsymbol a\boldsymbol a^T,\qquad
\boldsymbol a=(s+2,s+3,s+4,s+5,s+6)^T.
}
\tag{8.4}
$$



This is the restriction of the **actual falling metric**, not a substituted positive form.

Away from the obstruction (6.3), let $v\ne0$ be the cofactor kernel vector of


$$
[\boldsymbol1;\boldsymbol d;\boldsymbol f;\boldsymbol e_E].
$$


Its entries specify the reduction of the actual primitive zero-endpoint direction up to a unit. If the quadratic form (8.3) is nonzero on that vector, then


$$
v_p(T)=2,\qquad v_p(\delta)=2.
$$


Together with (6.5), this proves


$$
\boxed{p\nmid q_n.}
\tag{8.5}
$$



The nonvanishing of this restricted norm is an additional condition; it is not implied merely by rank four. In particular I do not infer a valuation upper bound from the forced divisibility $p^2\mid T$.

---

# 9. Implications for the same proportional family

The retained exact factorization is


$$
q_n=
\frac{t}{\alpha}\,
\frac{k}{\gcd(k,|r|)},
\qquad
k=\frac{hD_0}{\gamma},
$$


with final Gram gcd


$$
g_B=k\delta\alpha\gcd(k,|r|).
\tag{9.1}
$$



The new bordered-minor identity controls $h/\gamma$, not the final scalar cancellation $\gcd(k,r)$. In particular, even the conditional conclusion $p\mid h/\gamma$ in (7.4) does **not** by itself imply $p\mid q_n$.

For the selected family


$$
n=P-1,\qquad b=(P-1)/2001,\qquad m=1,
$$


the solved prime $P=n+1$ is not revisited here. The $d=2$ model contributes no additional prime because of parity.

The next feasible local problem is $p=n+3$. The same unit elimination leaves seven tail variables. Its four low high rows are, before any further saturation,


$$
\boxed{
E_{p-2,j},\quad
E_{p-1,j+1},\quad
\frac{E_{p,j+2}}p,\quad
\frac{E_{p+1,j+3}}p.
}
\tag{9.2}
$$


The two displayed divisions are exact; their residual independence and the matching chart still require proof.

There is one simplifying difference: at $d=3$,


$$
\ell=n+2=p-1,
$$


so every falling weight in the allowed column range is a $p$-unit:


$$
\omega_j\equiv(-1)^j j!\pmod p.
\tag{9.3}
$$


Thus the seven-tail metric has no universal $p^2$ factor to remove. This is the bounded next block on the actual even-$n$ family.

For a block $d$ extending to a positive fraction of $b$, the residual dimension $2d+1$ grows. The five-tail obstruction above already shows why endpoint integrality is insufficient: the relevant chart depends on factorial jet residues, and at an exceptional chart the matching row can require higher-depth saturation.

---

# 10. Secondary audit: the normalized $b=4$ infinite implication

This part concerns the **endpoint-matched cofactor family**, not the proportional Gram family and not the old fixed-$b$ Gram theorem.

I use the following supplied inputs with their existing status:

- the exact integral normalization by $12(2n+5)$;
- all-depth scalar transfer for the normalized polynomials at $p\ge5$;
- the coordinator’s two-algorithm certificate that all $46$ normalized $\widehat V$-residues are nonzero for
  

$$
\mathcal P=\{5,11,13,17\};
$$


- the inherited fixed-$b=4$ theorem for eventual matched-endpoint nonvanishing and the complete signed error.

I have not regenerated those $46$ residues. The following is a proof of their infinite implication, not a new seed scan.

Let


$$
d_n=\gcd(\widehat\sigma_n,\widehat\chi_n,\widehat\kappa_n),
\qquad
V_n^*=\widehat V_n/d_n.
$$


For $p\in\mathcal P$, transfer and the complete residue certificate give


$$
\widehat V_n\not\equiv0\pmod p
\qquad\text{for every }n\ge0.
$$


If all three hatted contractions were divisible by $p$, their defining linear combination $\widehat V_n$ would be divisible by $p$. Therefore


$$
v_p(d_n)=0,\qquad
\boxed{v_p(V_n^*)=0\quad(n\ge0,\ p\in\mathcal P).}
\tag{10.1}
$$



This is exactly where local projective normalization suffices. The prime-to-$p$ part of $d_n$ can vary arbitrarily; it does not affect (10.1).

Retain the complete quotient


$$
\frac{X_n}{Y_n}
=
\frac{Q_n^*+2^{n+1}V_n^*/(n!)^2}{D_n^*},
\qquad n\ge4,\quad D_n^*\ne0.
\tag{10.2}
$$


At each $p\in\mathcal P$,


$$
v_p(Q_n^*)\ge-\lfloor\log_p(n+1)\rfloor.
$$


For all sufficiently large $n$,


$$
2v_p(n!)>\lfloor\log_p(n+1)\rfloor.
$$


The two terms in the **whole numerator** of (10.2) consequently have distinct valuations, and


$$
v_p\!\left(Q_n^*+\frac{2^{n+1}}{(n!)^2}V_n^*\right)
=-2v_p(n!).
\tag{10.3}
$$


In particular this whole numerator is nonzero.

For any valid common clearer $\lambda_n$, set


$$
N_n=\lambda_n\left(Q_n^*+\frac{2^{n+1}}{(n!)^2}V_n^*\right),
\quad Z_n=\lambda_nD_n^*,
\quad g_n=\gcd(|N_n|,|Z_n|).
$$


The actual denominator remains


$$
q_n=\frac{|Z_n|}{g_n}.
$$


Equation (10.3), and the integrality of $D_n^*$, give


$$
\boxed{
v_p(q_n)=2v_p(n!)+v_p(D_n^*)\ge2v_p(n!)
\quad(p\in\mathcal P).
}
\tag{10.4}
$$


Thus


$$
\log q_n\ge W_4n-O(\log n),
\qquad
W_4=2\sum_{p\in\mathcal P}\frac{\log p}{p-1}.
\tag{10.5}
$$



Let the actual matched center be $c_n=p_n/q_n=-X_n/Y_n$, in lowest terms. Under the inherited complete-error theorem,


$$
e+\pi-c_n\ne0
$$


eventually and


$$
\log|e+\pi-c_n|=-\tau n+o(n).
$$


The whole primitive form is therefore


$$
\boxed{
L_n=q_n(e+\pi)-p_n=q_n(e+\pi-c_n)\ne0,
}
\tag{10.6}
$$


and


$$
\boxed{
\liminf_{n\to\infty}\frac1n\log|L_n|
\ge W_4-\tau>0.30319406432.
}
\tag{10.7}
$$



So the four-prime certificate upgrades the earlier positive-density exclusion to an **all-sufficiently-large-index exclusion for this matched-$b=4$ primitive-form sequence**, conditional on the stated inherited transfer and analytic inputs.

It does not prove anything about the rationality of $e+\pi$, and it must not be substituted for a Gram-center denominator theorem.

---

# 11. Whole proportional error and the unresolved aggregate budget

For the proportional family, retain


$$
\mathfrak c_n=\frac{p_n}{q_n},\qquad
\gcd(p_n,q_n)=1,\quad q_n>0.
$$


If the supplied proportional analytic theorem is accepted with its stated dependencies, then


$$
\epsilon_n=\mathfrak c_n-(e+\pi)\ne0
$$


eventually, with


$$
\log|\epsilon_n|
=-\left(2+\frac1{2001}\right)\log(1+\sqrt2)\,n+o(n).
$$


The whole primitive evaluated error is exactly


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n\ne0.
}
\tag{11.1}
$$



The missing estimate remains one for the actual final denominator:


$$
\log q_n=
\log\frac t\alpha+
\log\frac{k}{\gcd(k,|r|)}.
\tag{11.2}
$$


Neither the bordered-minor identity nor the auxiliary five-tail calculation establishes a sufficient aggregate rate for this sum.

---

## (1) New result and proof status

**Proved by finite algebra on the stated normality domains:**

- The global bordered-minor formula
  

$$
h/\gamma=\Delta_e/\gcd(\Delta_e,\Delta_x),
$$


  with all high-row and matching-row scales canceled.
- At $p=n+2$, complete saturation of the genuine high block, leaving the five-tail equations (5.6).
- The matching and endpoint reductions (5.5)–(5.8), including an explicit account of which partial-sum constants cancel.
- The restricted actual falling metric (8.3).
- The exact two-residue chart obstruction (6.3).
- Away from that obstruction, $h$ is a $p$-unit.
- At the obstruction, if matching has rank three modulo $p$, then $p\mid h/\gamma$, proved using the nonzero endpoint minor (7.3).

**Conditional infinite consequence:**

- The coordinator’s normalized four-prime certificate, together with the supplied transfer and whole-error theorems, implies the all-index matched-$b=4$ exclusion (10.7). Global gcd normalization is needed only projectively and does not invalidate this implication.

No assertion about the irrationality of $e+\pi$ has been proved.

## (2) Exact remaining bottleneck

For the same proportional family, the next feasible offset is $d=3$, not $d=2$. The immediate bounded obligation is to saturate the four residual rows (9.2), retain the actual matching and endpoint rows, and control their seven-tail metric.

Globally, enough such local information must be accumulated at the **same index** to bound


$$
\log\frac t\alpha+
\log\frac{k}{\gcd(k,|r|)}
$$


relative to the complete signed rate.

The five-tail calculation identifies a genuine first obstruction to a blanket chart argument: the two factorial congruences (6.3), and, within them, the possible higher matching-content condition $A+C\Theta=0$. No uniform avoidance or depth bound has been proved.

## (3) Bounded computation request

If the coordinator elects to arrange it, I request one auxiliary normalization audit, not a scan.

**Input**


$$
p=17,\qquad n=15,\qquad b=6,\qquad m=1.
$$


Use the defining Rodrigues rows, the complete endpoint formulas, and falling weights. Here the unit block is formed by high rows $l=3,4$ and columns $0,1$; the five tails are columns $2,\ldots,6$.

**Expected verifiable output**

1. Exact unit-Schur reduction modulo $17^2$, with the second low high row divided by $17$ before reduction.
2. Verification of both residual high rows and their rank two.
3. The five matching and endpoint residues, compared with (5.5)–(5.8), retaining $W_s$ and $T_{U,s}$.
4. Verification of the metric identity (8.3).
5. The two obstruction residues in (6.3), and the actual rank of the matching-plus-endpoint-sum chart.
6. If the endpoint system is nonsingular, the fully reduced rational Gram center and $v_{17}(q_n)$, not merely a row-clearer denominator.

A separate small symbolic check may verify


$$
\det[\boldsymbol1;\boldsymbol d;\boldsymbol f;\boldsymbol g]_{\{0,1,2,4\}}
=-4(s+1)^2(s+2)/(s^2+5s+8)
$$


under the exceptional substitutions (7.1).

These outputs would audit the new normalization and determinant algebra only. They would not prove a global denominator rate or settle the main irrationality question.
