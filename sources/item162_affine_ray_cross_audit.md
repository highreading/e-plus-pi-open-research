> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent cross-audit: affine/congruence-slab square divisor

Date: 2026-08-28

## Verdict

**PROVED.** The proposed affine ray is correct, and the same proof gives a
stronger congruence-slab theorem. Let



$$
p\equiv19\pmod {20}\ \text{be prime},\qquad
m_0={9p-1\over10},\qquad m=m_0+\ell p\quad(\ell\ge0),
$$



and assume that the top denominator layer is $q_p=p$, equivalently



$$
p\le4m+1<p^2.                                                \tag{1}
$$



Then $p\in\mathcal H_m$, $p\notin\mathcal P_m$, both first Cartier
scalars vanish, and



$$
\boxed{p^2\mid c_m}.                                         \tag{2}
$$



The original ray is the case


$$
p=20k+19,\qquad m=18k+17\qquad(\ell=0).
$$


Dirichlet's theorem makes that ray infinite. The result nevertheless adds
only $O(\log m)$, not positive linear logarithmic mass.

## 1. Algebraic audit

Write $p=20k+19$. Direct division for every admissible $\ell$ gives



$$
\begin{aligned}
6m&=(5+6\ell)p+r,       &r&=8k+7,\\
4m+1&=(3+4\ell)p+t,     &t&=12k+12.
\end{aligned}                                                   \tag{3}
$$



Thus $p-t=r$ and $t+1<p$. In the item-149 $e_p=1$ notation,



$$
F={u^{5+6\ell}\over Q^{4+4\ell}},\qquad
P_0=u^rQ^r,\qquad P_1=u^rQ^{r-1}.                            \tag{4}
$$



Because


$$
uQ=x(1-x)(1+x)(1+x^2)=x(1-x^4),
$$


the two Cartier polynomials are


$$
P_0=x^r(1-x^4)^r,\qquad
P_1=x^r(1-x)(1-x^4)^{r-1}.                                  \tag{5}
$$



The coefficient selected by Cartier is $[x^{p-1}]$. Relative to the
initial $x^r$, its required offset is


$$
p-1-r=12k+11\equiv3\pmod4.                                  \tag{6}
$$


The offsets in $P_0$ are $0\pmod4$, and those in $P_1$ are $0$ or
$1\pmod4$. Hence


$$
\gamma_0=[x^{p-1}]P_0=0,\qquad
\gamma_1=[x^{p-1}]P_1=0.                                    \tag{7}
$$



The degree and normalization conditions also hold uniformly:


$$
\deg P_0=5r=2p-3,\qquad \deg P_1=5r-3=2p-6.                 \tag{8}
$$


Both degrees are at most $2p-2$, so $p\in\mathcal H_m$. But
$2p-3>p-2$, so $p\notin\mathcal P_m$ and
$\delta_{m,p}=0$. Also $p<2m$ already at $m=m_0$, while (1) is
exactly $e_p=1$. These checks close the possible normalization gaps.

## 2. Bridge to $p^2\mid c_m$

Item 149's relative Cartier congruence sends each zero image in (7) to


$$
(pR_s,L_s,E_s)\equiv(0,0,0)\pmod p\qquad(s=0,1).             \tag{9}
$$


Every product in


$$
pA_m=L_1(pR_0)-L_0(pR_1)
$$


is therefore divisible by $p^2$, so


$$
v_p(pA_m)\ge2.                                               \tag{10}
$$



Item 160's exact one-coordinate bridge, with $q_p=p$ and
$\delta_{m,p}=0$, says


$$
p^2\mid c_m\quad\Longleftrightarrow\quad v_p(pA_m)\ge2.
$$


This proves (2). Item 149 also gives $v_p(V_m)\ge e_p+1=2$; indeed (9)
sharpens the local bounds to $v_p(U_m)\ge2$ and $v_p(V_m)\ge3$.

## 3. Hasse/Bockstein compatibility

**PROVED.** Equation (7) gives


$$
\Theta=\gamma_1P_0-\gamma_0P_1=0,\qquad T=0.
$$


The determinant Bockstein therefore gives $A_m\equiv0\pmod p$, exactly
(10). The item-161 Hasse digit in this non-rank-zero $e_p=1$ branch is


$$
\eta_{m,p}={pA_m\over p}=A_m\pmod p,
$$


so it also vanishes.

The Bockstein pole-order qualification is harmless. From (1),
$3+4\ell\le p-1$; equality is impossible modulo $4$. Thus the pole
order $4+4\ell$ of $F$ is at most $p-1$.

## 4. Exact finite replay

**EXACT FINITE AUDIT ONLY.**

- Replaying affine_prime_ray_p2_certificate.py through $p\le5000$
  reproduced 84 prime records and checked all 48,511 members of their
  complete $e_p=1$ slabs, with every serialized identity true.
- The independent Hasse replay through $p\le500,\ m\le500$ was
  byte-identical to the canonical JSON: 33/33 slab digits vanished, including
  13 points on the original $\ell=0$ ray.
- Sixteen additional slab points with
  $p\in\{19,59,79,139\}$ and $0\le\ell\le3$, whenever (1) held, all
  had $(e_p,\delta_{m,p},\eta)=(1,0,0)$.
- Frozen exact coordinates for the six slab points with $m\le100$ give



$$
\begin{array}{c|c}
(m,p)&(v_p(U_m),v_p(V_m),v_p(c_m))\\ \hline
(17,19)&(2,3,2)\\
(36,19)&(3,3,3)\\
(55,19)&(2,3,2)\\
(74,19)&(3,5,3)\\
(53,59)&(2,3,2)\\
(71,79)&(2,3,2)
\end{array}
$$



- The ten neighboring $p\equiv9\pmod {20}$ controls all had nonzero
  Hasse digit. This is a finite contrast, not a uniform nonvanishing
  theorem for the neighboring class.

## 5. Exact mass ceiling

For fixed $m$, define


$$
\mathcal S_m=\{p:\ p\text{ prime},\ p\equiv19\pmod {20},\
p\mid10m+1,\ p\le4m+1<p^2\}.
$$


The congruence $p\mid10m+1$ is equivalent to
$m=m_0+\ell p$ with $\ell\ge0$. Therefore


$$
\prod_{p\in\mathcal S_m}p\mid10m+1,\qquad
\sum_{p\in\mathcal S_m}\log p\le\log(10m+1).                 \tag{11}
$$


Equation (2) supplies one extra copy of each $p\in\mathcal S_m$, but
(11) proves that this mechanism cannot add positive linear logarithmic
mass.

## 6. Packaging audit

**RESOLVED.** An initial JSON predated the final extended-certificate edit.
The builder regenerated it. The current JSON records the current dependency
hash and an independent full replay is byte-identical. Current package
hashes at audit completion are

    5bb0be3bcc30e47238042c7150b4b5a63bb6ff7b2b7109c71b367af76504dcdd  affine_prime_ray_p2_certificate.py
    9a831b0a3fb092caece2245e3307319a4f1bef79f4128f778b0bb98496d21476  affine_prime_ray_p2_certificate_p5000.json
    583734adcf32ee945725c1da6ae4277b0a51a7aecace0672a5d8116b53952902  lifted_endpoint_hasse_extended_certificate.py

## 7. Classification

- **PROVED:** the congruence-slab theorem (2), its bridge through items 149
  and 160, Hasse/Bockstein compatibility, and the mass ceiling (11).
- **EXPERIMENTAL:** only the finite replay counts and neighboring controls.
- **OPEN:** a lifted-prime family with positive weighted mass. This slab
  does not decide the arithmetic nature of $e+\pi$.
