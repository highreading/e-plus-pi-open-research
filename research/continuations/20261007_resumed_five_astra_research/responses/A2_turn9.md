> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 Turn 9 — An evaluated factorial determinant in the complete force channel

## Abstract and proof status

The global objective remains unresolved. This report proves neither rationality nor irrationality of $e+\pi$.

I move directly to the arithmetic force channel. I do not repeat the closed source recurrence, rank-three reduction, finite inverse audit, or Hahn-defect calculation.

The new evaluated scalar is the determinant of the first source and the **two complete logarithmic initial charges**. Write


$$
r_i=r_i^{e}+r_i^{F},
\qquad
r_i^{F}
=\frac1{b!}\sum_s a_s(n)(n+i)_{\underline s}L_{2n+i-s}.
$$


Then


$$
\boxed{
f_0^0r_1^{F}-f_1^0r_0^{F}
=
\frac{2(-2)^n(n!)^2}{b!}.
}
\tag{A}
$$


Every original $n$ is odd. Consequently, on the entire unchanged original family,


$$
\boxed{
f_0^0r_1^{F}-f_1^0r_0^{F}
=-G_n,
\qquad
G_n:=\frac{2^{n+1}(n!)^2}{b!}>0.
}
\tag{B}
$$



This is an exact evaluation, not a finite-data conjecture. It has three consequences.

1. The logarithmic response, although homogeneous in the interior recurrence, is **not** a scalar multiple of the first source. A proposed complete-source simplification that absorbs both logarithmic initial charges into one first-source multiple is therefore impossible.

2. The complete reconstructed columns satisfy the exact, division-free identity
   

$$
\boxed{
   f_0^0Y-r_0^{F}Z_w
   =
   f_0^0Y^{e}-G_n B_1,
   \qquad
   B_1:=\mathcal RA^{-1}h^{(1)}.
   }
   \tag{C}
$$


   Here $Y^{e}$ contains **every factorial source row, both finite returns, and the physical endpoint**. Thus (C) is an identity for the complete finite producer, not for a freely matched approximation.

3. In the established reduced adjoint force channel, the logarithmic part of the defect is evaluated exactly:
   

$$
\boxed{
   \mathcal E_{\mathrm{force}}^{F}
   =-\frac{\eta_1}{f_0^0}G_n.
   }
   \tag{D}
$$


   At $29$, this removes the logarithmic loss in the earlier general lower estimate for this particular reduced defect.

The factor $G_n$ has factorial scale at all primes. Nevertheless, (C) does **not** make $G_n$ a divisor of the actual final gcd. I prove a paid content-transfer lemma specifying exactly what additional complete exponential-channel divisibility would be sufficient, and exactly what survives the auxiliary divisions and actual contents.

No upper bound for $\nu$, no new divisor of the actual $g_B$, and no improved asymptotic bound for the actual $q_n$ is established. Those limitations are explicit below.

---

## 1. Original objects and retained scope

Throughout,


$$
p=29,\qquad
b=3^{249005515+574312172u},\qquad
n=2001b,
$$


where


$$
u\ge0,\qquad u\equiv2\pmod{29^9}.
$$


Equivalently, the original infinite index set is


$$
u=2+29^9t,\qquad t\in\mathbb Z_{\ge0}.
$$



Put


$$
N=n+2,\qquad W_j=\binom Nj,
$$


and retain


$$
(Cv)_j=jv_{j-1}-v_j,\qquad v_{-1}=v_b=0,
\qquad
\mathcal R=\operatorname{diag}(W_j)C.
$$



The domains remain:

- contact coordinates $0\le j<b$;
- source recurrence rows $1\le i\le b-2$;
- reconstructed coordinates $0\le j\le b$.

No finite block is extended. In particular, the retained split


$$
b=29^3B+5044,\qquad j=\ell+29^3J<b
$$


still has upper endpoint $B$ for $\ell<5044$ and $B-1$ otherwise.

Let


$$
Q(z)=1-z+\frac{z^2}{2},
\qquad
a_s(n)=[z^s]Q(z)^n.
$$


The actual extended matrix is


$$
A_{\mathrm{ext}}(i,j)
=
\sum_s a_s(n)(n+i)_{\underline s}
\binom{2n+i-s}{j},
$$


and $A$ is its original square interior restriction.

The first source is


$$
f_i^0
=
\frac{(n+i)!}{n!}
[z^n](1+2z+2z^2)^n(1+z)^i.
$$


Write


$$
f_0=f_0^0,\qquad f_1=f_1^0
$$


when no ambiguity is possible.

The complete second source is split only by its already specified components:


$$
r_i=r_i^{e}+r_i^{F},
$$


where


$$
r_i^{e}
=
\sum_s a_s(n)(n+i)_{\underline s}T_{2n+i-s},
$$




$$
r_i^{F}
=
\frac1{b!}\sum_s a_s(n)(n+i)_{\underline s}L_{2n+i-s},
$$




$$
T_m=\frac1{b!}\sum_{q=b}^m(m)_{\underline q},
$$


and


$$
L_0=0,\qquad
L_m=mL_{m-1}+2(m-1)![z^{m-1}]Q(z)^{-1}.
$$



The actual reconstructed columns are


$$
Z_w=\mathcal RA^{-1}f^0,
\qquad
Y=\mathcal RA^{-1}r+W_be_b.
$$


Define the complete exponential response by


$$
\boxed{
Y^{e}:=\mathcal RA^{-1}r^{e}+W_be_b.
}
\tag{1.1}
$$


Thus the physical terminal is assigned to $Y^{e}$, not discarded.

### Results reused

The recovered source and rank-three identities are old and are used at their stated scope:


$$
\mathcal Df^0=0,\qquad
\mathcal Dr^{F}=0,\qquad
\mathcal Dr^{e}=\mathcal H,
$$




$$
\mathcal DA=-\mathcal VC,\qquad
\mathcal H=\mathcal Ve_b.
$$


The homogeneous source space has the two initial-value solutions


$$
h^{(0)},h^{(1)},\qquad
(h_0^{(0)},h_1^{(0)})=(1,0),\quad
(h_0^{(1)},h_1^{(1)})=(0,1).
$$



In particular,


$$
f^0=f_0h^{(0)}+f_1h^{(1)},\qquad
r^{F}=r_0^{F}h^{(0)}+r_1^{F}h^{(1)}.
\tag{1.2}
$$


The second equality retains both logarithmic charges. It follows from the proved homogeneous interior recurrence and its leading coefficient $1$; no division is introduced.

I also retain the original-family unit theorem


$$
f_0\in\mathbb Z_{29}^{\times},
$$


the established adjoint reduction, and the signed whole-error theorem, without claiming to reconstruct their omitted archived proofs here.

---

## 2. Literature gate and the representation question

The supplied literature gate supports the following methodological statements, and no stronger ones.

- Identical normalized hypergeometric linear forms can sometimes acquire stronger arithmetic divisors by combining parameter-permuted representations.
- A rational-difference argument requires an exact cancellation of the irrational coefficient before a smallness-versus-denominator comparison can be used.
- The cited constructions concern their stated $\zeta(2)$ families. They do not establish a transformation for the present producer.

No complete terminating-hypergeometric transformation of the original norm/mixed pair is obtained in this report.

There is, however, a source-level simplification that must be tested before such a transformation can be proposed: can the homogeneous logarithmic response be absorbed into a multiple of the first source? The answer is **no**, and the obstruction can be evaluated exactly.

The proof below also produces a factorial-scale replacement identity. Unlike a generic three-dimensional Gram representation, its new coefficient is explicitly evaluated.

---

## 3. Evaluation of the logarithmic initial-charge determinant

### 3.1 An exact polynomial integral for the logarithmic moments

Let


$$
\zeta_\pm=\frac{1\pm \mathrm i}{2},
\qquad \mathrm i^2=-1.
$$


Since


$$
Q(z)=(1-\zeta_+z)(1-\zeta_-z),
$$


we have


$$
[z^{m-1}]Q(z)^{-1}
=
\frac{\zeta_+^m-\zeta_-^m}{\mathrm i}.
$$


Solving the defining recurrence for $L_m$ gives


$$
\frac{L_m}{m!}
=
2\sum_{k=1}^m
\frac{\zeta_+^k-\zeta_-^k}{\mathrm i\,k}.
$$


Therefore


$$
\boxed{
\frac{L_m}{m!}
=
\frac2{\mathrm i}
\int_{\zeta_-}^{\zeta_+}
\frac{1-t^m}{1-t}\,dt.
}
\tag{3.1}
$$



For integer $m\ge0$, the integrand in (3.1) is a polynomial. The identity is consequently just an exact polynomial-antiderivative calculation. It invokes no assertion about the irrationality of $\pi$, and no branch choice is needed.

The vertical segment from $\zeta_-$ to $\zeta_+$ will be used throughout this section.

---

### 3.2 Rodrigues polynomials adapted to the actual source

Put


$$
R(t)=t^2-t+\frac12=t^2Q(1/t),
$$


and define


$$
p_n(t)=\frac1{n!}\frac{d^n}{dt^n}R(t)^n.
\tag{3.2}
$$


For the two initial source positions, also put


$$
p_{n,i}(t)
=
\frac1{n!}\frac{d^n}{dt^n}\bigl(t^iR(t)^n\bigr),
\qquad i=0,1.
$$


Thus $p_{n,0}=p_n$.

A useful exact relation is


$$
\boxed{
p_{n,1}(t)=\frac{p_{n+1}(t)+p_n(t)}2.
}
\tag{3.3}
$$


Indeed,


$$
tR(t)^n
=
\frac1{2(n+1)}\frac d{dt}R(t)^{n+1}
+\frac12R(t)^n,
$$


because $R'(t)=2t-1$. Applying $n!^{-1}d^n/dt^n$ proves (3.3).

These polynomials have the segment orthogonality


$$
\boxed{
\int_{\zeta_-}^{\zeta_+}p_n(t)t^k\,dt=0
\qquad(0\le k<n).
}
\tag{3.4}
$$


To prove it, integrate by parts $n$ times in (3.2). At each endpoint $R(t)^n$ has a zero of order $n$, so every endpoint term vanishes. The final derivative of $t^k$ is zero.

This is an auxiliary exact polynomial identity on a fixed complex segment. It does not replace the original coordinate interval $0,\ldots,b$ by a full Hahn support.

---

### 3.3 Identification of the actual first charges

Taylor expansion at $t=1$ gives


$$
p_{n,i}(1)
=
[z^n](1+z)^iR(1+z)^n.
$$


Since


$$
R(1+z)=\frac12(1+2z+2z^2),
$$


we obtain


$$
\boxed{
f_i^0
=
2^n\frac{(n+i)!}{n!}p_{n,i}(1),
\qquad i=0,1.
}
\tag{3.5}
$$



Set


$$
e_n=p_n(1).
$$


Equations (3.3)–(3.5) give


$$
\boxed{
f_0=2^ne_n,\qquad
f_1=2^{n-1}(n+1)(e_{n+1}+e_n).
}
\tag{3.6}
$$



These are identities for the printed first-source coefficients, not a replacement first force.

---

### 3.4 Identification of both actual logarithmic charges

Define the unscaled logarithmic charges


$$
\ell_i:=b!\,r_i^{F},
\qquad i=0,1.
$$


Expansion of $R(t)^n=t^{2n}Q(1/t)^n$ gives


$$
t^np_{n,i}(t)
=
\sum_s a_s(n)
\binom{2n+i-s}{n}t^{2n+i-s}.
$$


Multiplication by $(n+i)!n!$ shows that the coefficient of
$t^{2n+i-s}$ is exactly


$$
a_s(n)(n+i)_{\underline s}(2n+i-s)!.
$$


Applying (3.1) term by term therefore yields


$$
\ell_i
=
(n+i)!n!\,\frac2{\mathrm i}
\int_{\zeta_-}^{\zeta_+}
\frac{p_{n,i}(1)-t^np_{n,i}(t)}{1-t}\,dt.
\tag{3.7}
$$



For $i=0,1$, orthogonality removes the factor $t^n$ in this formula:


$$
\int_{\zeta_-}^{\zeta_+}
\frac{(1-t^n)p_{n,i}(t)}{1-t}\,dt=0.
$$


For $i=0$, this follows from (3.4). For $i=1$, use (3.3) and apply (3.4) to both $p_n$ and $p_{n+1}$.

Define


$$
d_n
=
\frac2{\mathrm i}
\int_{\zeta_-}^{\zeta_+}
\frac{p_n(1)-p_n(t)}{1-t}\,dt.
\tag{3.8}
$$


Again, the integrand is polynomial, so $d_n$ is an exactly specified rational number. Equations (3.3) and (3.7) now give


$$
\boxed{
\ell_0=(n!)^2d_n,
}
\tag{3.9}
$$




$$
\boxed{
\ell_1
=
\frac{(n!)^2(n+1)}2(d_{n+1}+d_n).
}
\tag{3.10}
$$



Thus both logarithmic charges have been identified in the original moment formula.

---

### 3.5 A two-solution recurrence and its evaluated Casoratian

The generating function of $p_n(t)$ is


$$
\sum_{n\ge0}p_n(t)s^n
=
\bigl(1-2(2t-1)s-s^2\bigr)^{-1/2}.
\tag{3.11}
$$



For a direct check, Taylor’s formula gives


$$
p_n(t)=[z^n]\bigl(R(t)+(2t-1)z+z^2\bigr)^n.
$$


Expanding the central coefficient and summing in $n$ gives (3.11), using


$$
(2t-1)^2-4R(t)=-1.
$$


Differentiating (3.11) in $s$ and comparing coefficients yields


$$
(n+1)p_{n+1}(t)
=
(2n+1)(2t-1)p_n(t)+np_{n-1}(t).
\tag{3.12}
$$



At $t=1$,


$$
(n+1)e_{n+1}
=
(2n+1)e_n+ne_{n-1},
\qquad
e_0=e_1=1.
\tag{3.13}
$$



Apply the functional in (3.8) to (3.12). The extra term created by $2t-1$ is a multiple of
$\int p_n(t)\,dt$, which is zero for $n\ge1$ by (3.4). Hence


$$
(n+1)d_{n+1}
=
(2n+1)d_n+nd_{n-1},
\qquad n\ge1,
\tag{3.14}
$$


with


$$
d_0=0,\qquad d_1=4.
$$



Let


$$
\mathcal W_n=e_nd_{n+1}-e_{n+1}d_n.
$$


Equations (3.13)–(3.14) imply


$$
\mathcal W_n=-\frac n{n+1}\mathcal W_{n-1},
\qquad
\mathcal W_0=4.
$$


Therefore


$$
\boxed{
\mathcal W_n=\frac{4(-1)^n}{n+1}.
}
\tag{3.15}
$$



This is the evaluated scalar that closes the initial-charge calculation.

---

### Theorem 3.1 — Exact factorial determinant

For every $n\ge0$ for which the displayed source formulas are formed,


$$
\boxed{
f_0\ell_1-f_1\ell_0
=
2(-2)^n(n!)^2.
}
\tag{3.16}
$$


Consequently, at every original index,


$$
\boxed{
f_0r_1^{F}-f_1r_0^{F}
=
-G_n,\qquad
G_n=\frac{2^{n+1}(n!)^2}{b!}.
}
\tag{3.17}
$$



#### Proof

Substitute (3.6), (3.9), and (3.10):


$$
\begin{aligned}
f_0\ell_1-f_1\ell_0
&=
2^{n-1}(n!)^2(n+1)
\bigl(e_nd_{n+1}-e_{n+1}d_n\bigr)\\
&=
2^{n-1}(n!)^2(n+1)
\frac{4(-1)^n}{n+1}\\
&=2(-2)^n(n!)^2.
\end{aligned}
$$


Divide by the retained $b!$. Since $b$ and $2001$ are odd, every original $n=2001b$ is odd. This gives (3.17). ∎

---

## 4. Complete-source consequence and the precise obstruction

### 4.1 A proposed simplification that cannot hold

The identity


$$
r^{F}=\rho f^0
\tag{4.1}
$$


for a rational scalar $\rho$ would force


$$
f_0r_1^{F}-f_1r_0^{F}=0.
$$


Theorem 3.1 shows that this determinant is instead $-G_n\ne0$.

Thus:

> The vanishing of logarithmic interior forcing does not permit both logarithmic initial charges to be absorbed into one multiple of the first source.

This obstruction applies at every original index. It is stronger than a mismatch found at a small auxiliary value.

Its scope is also limited. It does **not** disprove a transformation that mixes both homogeneous directions, changes parameters with a proved complete-source rule, or produces a scalar cancellation after contraction. Those mechanisms require additional identities.

---

### 4.2 An exact identity on all original source rows

Using (1.2) and (3.17),


$$
\boxed{
f_0r^{F}-r_0^{F}f^0=-G_nh^{(1)}.
}
\tag{4.2}
$$


This holds on every contact row $0\le i<b$.

Adding the complete exponential source gives


$$
\boxed{
f_0r-r_0^{F}f^0=f_0r^{e}-G_nh^{(1)}.
}
\tag{4.3}
$$



No row has been omitted. In particular, the recurrence forcing on the right remains


$$
f_0\mathcal H_i,\qquad 1\le i\le b-2.
$$


The two initial logarithmic charges have not been set to zero; they have been eliminated by the evaluated determinant.

Apply the actual finite inverse and reconstruction. With


$$
B_1=\mathcal RA^{-1}h^{(1)}
$$


and $Y^{e}$ from (1.1),


$$
\boxed{
f_0Y-r_0^{F}Z_w=f_0Y^{e}-G_nB_1.
}
\tag{4.4}
$$


The physical $W_be_b$ occurs on both complete second-column sides with coefficient $f_0$.

Equation (4.4) uses the same finite $A^{-1}$. Thus any returns in an implementation of that inverse remain exactly those of the original problem. Nothing has been replaced by an infinite inverse or a full-support orthogonality formula.

Contracting with $Z_w$ gives the complete scalar identity


$$
\boxed{
f_0Z_w^TY-r_0^{F}Z_w^TZ_w
=
f_0Z_w^TY^{e}-G_nZ_w^TB_1.
}
\tag{4.5}
$$



The new content of (4.5) is the evaluated factorial coefficient $G_n$. The other contractions in (4.5) have not been evaluated, so (4.5) alone is not a norm-divisibility theorem.

---

## 5. Evaluation in the established adjoint force channel

Retain the original saturated adjoint data and its proved identity


$$
\mathcal E_{\mathrm{force}}
=
\eta_1\left(r_1-\frac{f_1}{f_0}r_0\right)
+\lambda^T\mathcal H
+W_b(\Pi d)_b.
\tag{5.1}
$$


Split this exactly as


$$
\mathcal E_{\mathrm{force}}
=
\mathcal E_{\mathrm{force}}^{e}
+\mathcal E_{\mathrm{force}}^{F},
$$


where


$$
\mathcal E_{\mathrm{force}}^{e}
=
\eta_1\left(r_1^{e}-\frac{f_1}{f_0}r_0^{e}\right)
+\lambda^T\mathcal H
+W_b(\Pi d)_b,
\tag{5.2}
$$


and


$$
\mathcal E_{\mathrm{force}}^{F}
=
\eta_1\left(r_1^{F}-\frac{f_1}{f_0}r_0^{F}\right).
$$


Theorem 3.1 evaluates the latter:


$$
\boxed{
\mathcal E_{\mathrm{force}}
=
\mathcal E_{\mathrm{force}}^{e}
-\frac{\eta_1}{f_0}G_n.
}
\tag{5.3}
$$



This is not an omission of the logarithm at a fixed precision. It is an exact identity at every depth.

### 5.1 Exact valuation and scale

For every prime $\ell$,


$$
\boxed{
v_\ell(G_n)
=
(n+1)\mathbf1_{\ell=2}
+2v_\ell(n!)-v_\ell(b!).
}
\tag{5.4}
$$


At $29$, the established integrality of $\eta_1$ and the unit property of $f_0$ give


$$
\boxed{
v_{29}\!\left(\mathcal E_{\mathrm{force}}^{F}\right)
\ge 2v_{29}(n!)-v_{29}(b!).
}
\tag{5.5}
$$


If $\eta_1\ne0$, its exact valuation is


$$
2v_{29}(n!)-v_{29}(b!)+v_{29}(\eta_1).
$$



In particular,


$$
2v_{29}(n!)-v_{29}(b!)
=
\frac{4001}{28}b+O(\log n).
\tag{5.6}
$$


Unlike the earlier general estimate for individual logarithmic moment entries, (5.5) contains no subtraction of $\lfloor\log_{29}(2n+b-1)\rfloor$.

The all-prime size is


$$
\boxed{
\log G_n
=
\left(2-\frac1{2001}\right)n\log n
+
\left(
\log2-2+\frac{1+\log2001}{2001}
\right)n
+O(\log n).
}
\tag{5.7}
$$



Thus the evaluated coefficient has factorial scale, not merely fixed-digit $29$-adic scale.

### 5.2 What remains unknown locally

The reduced force obligation is still


$$
\mathcal E_{\mathrm{force}}\in29^3\mathfrak b\,\mathbb Z_{29}.
$$


Equation (5.3) turns it into the exact condition


$$
\boxed{
\mathcal E_{\mathrm{force}}^{e}
\equiv
\frac{\eta_1}{f_0}G_n
\pmod{29^3\mathfrak b}.
}
\tag{5.8}
$$



If


$$
3+v_{29}(\mathfrak b)
\le
2v_{29}(n!)-v_{29}(b!),
$$


then the logarithmic term is zero at that modulus, and (5.8) reduces to divisibility of the complete exponential channel. This is a **conditional simplification**, not a bound on $v_{29}(\mathfrak b)$.

No upper bound for $\nu$ follows from (5.5).

---

## 6. A paid all-prime content-transfer lemma

The factor $G_n$ is potentially useful only if its contribution survives:

1. the complete exponential response;
2. all rational scalar divisions;
3. the actual least simultaneous clearer;
4. both actual weighted contents;
5. the all-prime final gcd.

The following formulation keeps these issues separate.

### 6.1 Actual scalar responses, with the original clearer fixed

Let


$$
V_1=\operatorname{diag}(\omega_j)N_{B,1},
\qquad
V_2=\operatorname{diag}(\omega_j)N_{B,2},
$$


where


$$
\omega_j=\frac{(n+2)!}{(n+2-j)!},
\qquad
N_B=d_B[\mathbf u_B,\mathbf v_B]
$$


uses the actual least simultaneous clearer.

Keep this actual $d_B$ fixed. The complete second-column construction is affine-linear in its force: the source response is linear, and the physical endpoint is fixed. Therefore contraction against the fixed actual $V_1$ defines a rational linear functional $\mathcal L_B$ on contact forces, together with a fixed endpoint contribution.

Define, independently of any proposed gcd or primitive quotient,


$$
J_B:=\mathcal L_B(f^0),\qquad
U_B:=\mathcal L_B(h^{(1)}),
$$


and let $H_{E,B}$ be the actual mixed response to the complete exponential source, including the actual endpoint contribution and all original column-normalization factors.

Applying (4.2) through this same linear map gives


$$
\boxed{
f_0H_B-r_0^{F}J_B
=
f_0H_{E,B}-G_nU_B.
}
\tag{6.1}
$$



No identification of a raw physical contraction with $H_B$ is made here. The original normalization is part of $\mathcal L_B$, and $d_B$ is not re-minimized after the source is split.

Let $m_B$ be the least positive integer simultaneously clearing the three rational scalars


$$
r_0^{F}J_B,\qquad f_0H_{E,B},\qquad U_B.
$$


Set


$$
I_B=m_Br_0^{F}J_B,\qquad
C_B=m_Bf_0H_{E,B},\qquad
D_B=m_BU_B.
$$


These are integers, and (6.1) becomes


$$
\boxed{
m_Bf_0H_B=I_B+C_B-G_nD_B.
}
\tag{6.2}
$$



The auxiliary clearer $m_B$ is an additional arithmetic payment. It does not replace the actual $d_B$.

---

### Theorem 6.1 — Paid factorial-content transfer

Let $\mathcal F_n$ be a positive integer specified independently of $q_n$. Suppose, at an original index, that


$$
\mathcal F_n\mid G_n,\qquad
\mathcal F_n\mid A_B,\qquad
\mathcal F_n\mid I_B+C_B.
\tag{6.3}
$$


Then


$$
\boxed{
\frac{\mathcal F_n}
{\gcd(\mathcal F_n,m_Bf_0)}
\ \mid\ g_B.
}
\tag{6.4}
$$



#### Proof

By (6.2) and the first and third conditions in (6.3),


$$
\mathcal F_n\mid m_Bf_0H_B.
$$


For positive integers $F,a$, the implication


$$
F\mid aH
\quad\Longrightarrow\quad
\frac{F}{\gcd(F,a)}\mid H
$$


follows prime by prime. Hence the integer in (6.4) divides $H_B$. It also divides $A_B$, by the second condition in (6.3). Therefore it divides


$$
g_B=\gcd(A_B,|H_B|).
$$


∎

This is a proved transfer lemma. Its hypotheses (6.3) have **not** been proved for a factorial-scale $\mathcal F_n$ on the original infinite family.

---

### 6.2 A precise follow-on arithmetic lemma

A concrete next target is now:

> **Complete exponential-residue transfer lemma — open.**  
> Specify an explicit factorial-floor product
> 

$$
> \mathcal F_n=\prod_{\ell\le n}\ell^{\,\theta_\ell(n)},
> \qquad
> 0\le\theta_\ell(n)\le v_\ell(G_n),
>
$$


> on an explicitly stated infinite subfamily
> 

$$
> u=2+29^9t,
>
$$


> and prove
> 

$$
> \mathcal F_n\mid A_B,\qquad
> I_B+C_B\equiv0\pmod{\mathcal F_n}.
>
$$


> Simultaneously bound the actual losses from $m_Bf_0$ and from factors already present in the known gcd.

This differs from the old unevaluated three-column Gram problem in two specific ways:

- the logarithmic contribution has been eliminated with the **evaluated** coefficient $G_n$;
- the remaining residue $I_B+C_B$ is the complete exponential response plus the explicitly retained norm-direction contribution, in actual final normalization.

The condition is still open. Naming this residue does not evaluate it.

---

### 6.3 Direction and scale after actual contents

Write the actual weighted contents as


$$
V_i=k_iv_i,\qquad k_i>0,\quad v_i\ \text{primitive},
$$


and put


$$
S=v_1^Tv_1,\qquad T=v_1^Tv_2.
$$


Then


$$
A_B=k_1^2S,\qquad H_B=k_1k_2T.
$$



For a prime $\ell$, let


$$
t_\ell=v_\ell(\mathcal F_n),\qquad
z_\ell=v_\ell(m_Bf_0).
$$


The restored factor in Theorem 6.1 has exponent


$$
\boxed{
\beta_\ell=[t_\ell-z_\ell]_+.
}
\tag{6.5}
$$



It is not legitimate to count all of $\sum\beta_\ell\log\ell$ as a *new* saving. Since $k_1\mid g_B$ already, its additional contribution beyond this content factor is at most—and is guaranteed by the lcm bound in the amount—


$$
\boxed{
\sum_\ell[\beta_\ell-v_\ell(k_1)]_+\log\ell.
}
\tag{6.6}
$$


More generally, relative to any previously proved divisor $g_0\mid g_B$, the guaranteed additional factor is


$$
\frac{\operatorname{lcm}(g_0,\prod_\ell\ell^{\beta_\ell})}{g_0}.
$$



The final positive-part formula remains


$$
\boxed{
v_\ell(q_n)
=
\left[
v_\ell(k_1)-v_\ell(k_2)+v_\ell(S)-v_\ell(T)
\right]_+.
}
\tag{6.7}
$$


Thus a restored factor matters only where it raises the actual mixed valuation enough to decrease this positive part.

There is one elementary bound on a payment:


$$
0<f_0=[z^n](1+2z+2z^2)^n\le5^n,
$$


so


$$
\log f_0\le n\log5.
\tag{6.8}
$$


The multiplication by $f_0$ alone cannot consume the $n\log n$ scale in (5.7). But the actual auxiliary denominator $m_B$, the actual contents, and the unproved exponential residue may consume or prevent that scale. None has been bounded sufficiently here.

Accordingly, the established new improvement in $\log q_n$ is **zero**.

---

## 7. What has and has not been learned about a second representation

The present calculation supplies an exact second description of the logarithmic part of the finite producer:


$$
r^{F}
=
\frac{r_0^{F}}{f_0}f^0-\frac{G_n}{f_0}h^{(1)},
$$


with the division-free form (4.2) preferred at all primes.

It does **not** supply a parameter permutation of the complete norm/mixed pair of the kind needed to invoke the identical-form arithmetic-divisor method.

The precise source obstruction is now evaluated:

- one homogeneous logarithmic direction cannot suffice;
- the missing second direction has coefficient $-G_n/f_0$;
- its all-prime factorial numerator is known exactly;
- its contraction and interaction with the complete exponential channel remain to be controlled.

This neither proves the existence nor proves the impossibility of a more elaborate hypergeometric transformation. In particular, the fixed-parameter scalar-antidifference obstruction from Turn 7 remains valid at its stated scope, but is not enlarged into an unsupported general impossibility claim.

---

## 8. Actual primitive normalization and the whole same-index error

The final arithmetic objects are unchanged:


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
\Omega=\operatorname{diag}(\omega_0^2,\ldots,\omega_b^2),
$$




$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=\frac{A_B}{g_B},\qquad
p_n=\frac{H_B}{g_B}.
}
\tag{8.1}
$$


The gcd is over **all primes**. The actual primitive multiplier remains


$$
d_B^2/g_B.
$$



No auxiliary source division, complex polynomial representation, or scalar clearer introduced above changes these definitions.

At the same original indices,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


and the whole error is


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n.
}
\tag{8.2}
$$


Under the retained signed whole-error theorem,


$$
\epsilon_n\ne0\quad\text{eventually},
$$


and


$$
\log|\epsilon_n|
=
-\lambda n+o(n),
\qquad
\lambda=
\left(2+\frac1{2001}\right)\log(1+\sqrt2).
\tag{8.3}
$$



An irrationality conclusion requires


$$
0<|q_n\epsilon_n|\longrightarrow0
$$


on an infinite subset of these same original indices.

Neither the evaluated factor $G_n$ nor Theorem 6.1 presently supplies the needed estimate for the **actual** $q_n$. In particular, the known logarithmic bound for $c+2$ is still not a bound for $\nu$.

---

## 9. Bounded exact verification

No tools were used. No original-size matrix computation, old rank audit, arbitrary mask enumeration, or repeated recurrence audit is proposed.

A small bounded calculation can independently check the new determinant identity.

### Inputs

For


$$
n=0,1,2,3,4,
$$


form exactly


$$
a_s(n)=[z^s]Q(z)^n,
$$


and generate $L_m$ only for


$$
0\le m\le9.
$$


Compute


$$
f_i^0
=
\frac{(n+i)!}{n!}
[z^n](1+2z+2z^2)^n(1+z)^i,
\qquad i=0,1,
$$


and


$$
\ell_i
=
\sum_s a_s(n)(n+i)_{\underline s}L_{2n+i-s}.
$$



All arithmetic is rational or integral, with bounded polynomial degrees and bounded moment indices.

### Expected verifiable output



$$
\begin{array}{c|r|r|r|r|r}
n&f_0&f_1&\ell_0&\ell_1&f_0\ell_1-f_1\ell_0\\ \hline
0&1&1&0&2&2\\
1&2&6&4&10&-4\\
2&8&36&24&112&32\\
3&32&200&456&2832&-576\\
4&136&1080&15360&122112&18432
\end{array}
$$


The last column must equal


$$
2(-2)^n(n!)^2.
$$



This check verifies only these five auxiliary instances. The infinite-family theorem rests on the derivation in §3, not on extrapolation from the table.

### What should not yet be commissioned

There is not yet a bounded-size accepting-state representation for the actual quantities $I_B+C_B$, $m_B$, or the required factorial-floor exponents $\theta_\ell(n)$. An original-size evaluation of them is not requested.

The next computational request should follow a mathematical reduction of that complete exponential residue, rather than precede it.

---

## 10. Proof-status ledger

| Statement | Status |
|---|---|
| Complete source recurrence, logarithmic homogeneity, rank-three reduction | Reused established results |
| A complete hypergeometric/permutation identity for the original norm/mixed pair | Not obtained |
| $f_0r_1^{F}-f_1r_0^{F}=-2^{n+1}(n!)^2/b!$ on every original index | **New proved evaluation** |
| The logarithmic response is a scalar multiple of the first source | **Disproved** |
| Complete reconstructed identity (4.4), including factorial forcing and endpoint | **Proved** |
| Exact logarithmic reduced-adjoint defect (5.3) | **Proved** |
| Factorial-scale valuation formula for $G_n$ at all primes | **Proved** |
| Paid content-transfer theorem (6.4) | **Proved under its explicit divisibility hypotheses** |
| Those hypotheses for a useful factorial-scale $\mathcal F_n$ on an infinite original subfamily | Open |
| An upper bound for the actual $\nu$ | Open |
| A new divisor of the actual $g_B$ | Not established |
| An improved actual denominator/error comparison | Not established |
| Rationality or irrationality of $e+\pi$ | Unresolved |

---

## Conclusion

The new proved result is the exact original-source determinant


$$
\boxed{
f_0^0r_1^{F}-f_1^0r_0^{F}
=
-\frac{2^{n+1}(n!)^2}{b!}
}
$$


on every unchanged original index.

It evaluates a previously unevaluated interaction of the two logarithmic charges, proves that a one-direction logarithmic absorption cannot hold, and yields the complete finite-producer identity


$$
\boxed{
f_0^0Y-r_0^{F}Z_w
=
f_0^0Y^{e}
-\frac{2^{n+1}(n!)^2}{b!}\,
\mathcal RA^{-1}h^{(1)}.
}
$$


All factorial source rows, finite inverse returns, and the physical endpoint remain present.

The exact remaining arithmetic bottleneck is to prove a factorial-scale divisibility statement for the **complete exponential residue in actual normalization**, while bounding the auxiliary clearing loss and distinguishing restored factors from contents already present in the gcd. The paid transfer theorem states what such a result would imply; its decisive hypotheses remain open.

The bounded verification needed for the new algebra is only the five-instance exact determinant check in §9. No finite check of that kind establishes an infinite-family denominator gain.

Thus this turn produces an evaluated factorial scalar and a precise, paid follow-on transfer lemma, but it does not yet produce the requested bound for $\nu$ or an actual aggregate denominator improvement. The unconditional problem for $e+\pi$ remains unresolved.
