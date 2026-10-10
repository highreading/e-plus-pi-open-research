> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 — audit of the third-defect reduction, with a two-parameter low-polynomial control

## Status

I can justify the proposed third-defect contraction, including the required precision-three polynomial representation. One correction is essential: **the unit-boundary coefficient $j$ cannot be frozen at $x$ at this precision**. Its first omitted term is nonzero as a low polynomial. It enters the second residual polynomial, however, and its leading contraction is killed by $T=0$. Thus it does **not** invalidate the coordinator’s proposed reduction.

I do **not** yet have the numerical low-polynomial coefficients needed to declare the third defect zero or nonzero. I reduce their evaluation to **two coefficient functions on $d=0,\ldots,24$**—50 field elements in total—rather than a collection of independent central-moment parameters or an unevaluated large scalar contraction. The bounded exact computation requested at the end would complete this coefficient evaluation.

The new reduction is


$$
\boxed{
\frac{M-(6C_n)^{-1}D}{29^2}
=
U\bigl(C_n\Gamma_0(d)+J_{29}\Gamma_1(d)\bigr)
\pmod{29}
}
\tag{A}
$$


on the stated locus $d\le24,\ T=0,\ D_1=0$. Here the two functions $\Gamma_0,\Gamma_1$ are specified by a bounded polynomial calculation below, but have **not been computed in this answer**.

No irrationality or rationality conclusion follows.

---

## 1. Domain, actual columns, and the audited interface

Throughout,


$$
p=29,\qquad b=3^a,\qquad n=2001b,\qquad m_w=1,
$$




$$
a\ge1,\qquad a\equiv432827\pmod{682892}.
$$


All actual coordinates satisfy $0\le j\le b$, and all contact inverses retain the finite range $0\le i,j<b$.

The metric is **falling**:


$$
\omega_j=j!\binom{n+2}{j}=(n+2)_{\underline j},
\qquad
\Omega=\operatorname{diag}(\omega_j^2).
$$


For the already weighted coordinates, write


$$
P=\frac{Z_w}{p^2},\qquad
Q=\frac{Y}{p^3},\qquad
Y=\frac{V_w}{b!},
\qquad
D=P^TP,\quad M=P^TQ.
$$



Set


$$
L=p^4,\quad b_*=687936,\quad b=b_*+Lh,
$$




$$
n=191110+LN,\qquad N=2001h+1946=3+pA,
$$




$$
h=pH+d,\qquad A=69h+67.
$$


These parameters are extracted from the original $3^a$; they are not independent cylinder variables.

Retain


$$
F(J)=\binom NJ\binom{2N+h-J}{h-J},
\qquad 0\le J\le h,
$$


and


$$
X_k=\binom Ak\binom{2A+H-k}{H-k},
\qquad 0\le k\le H.
$$


Thus


$$
\mathcal T=\sum_{k=0}^{H}X_k^2,\qquad T=\mathcal T\bmod p.
$$


On $T=0$,


$$
T_1=\frac{\mathcal T}{p}\bmod p,\qquad
U=\sum_{k=0}^{H}kX_k^2\bmod p.
$$



I use the supplied original-family fact that $C_n=J_0$ is a $p$-adic unit. The finite receipts


$$
(\kappa_0,\kappa_1)=(11,18),\qquad(g_0,g_1)=(26,3)
$$


remain supplied finite arithmetic inputs; I have not independently recomputed them.

### Construction-level audit of the missing kernel definitions

The definitions supplied in turns13/15 are sufficient to verify the previously missing graded-kernel step of A4’s audit.

Let $U_0=T(n)$, and let


$$
(D_sv)_{j+s}=\binom{j+s}{s}v_j.
$$


The exact conjugated kernel is


$$
C_s(k,l)=
\sum_{v=0}^{s}
\binom{k}{s-v}\binom nv
\binom{-v}{l-k+s-v}.
\tag{1.1}
$$


Indeed its row generating function is


$$
\frac1{s!}\frac{d^s}{dz^s}
\bigl(z^k(1+z)^n\bigr)(1+z)^{-n}.
$$


The finite matrix identity is legitimate: in the multiplication by $T(-n)$, the intermediate index is at most the final column index $l<b$. No enlarged inverse is being substituted.

For signed Newton inputs, the required finite summation is


$$
\sum_{t=0}^{L_0}
\binom{t+v-1}{v-1}\binom ti
=
\binom{v+i-1}{i}\binom{L_0+v}{v+i}.
\tag{1.2}
$$


It proves the displayed operator $\mathscr L_{s,b}$ in turn13, including its upper boundary. Each term is integer-valued on integers, so its Newton coefficients are integral. Moreover,


$$
\deg \mathscr L_{s,b}h\le \deg h+s.
\tag{1.3}
$$



The contact coefficient bound follows directly, rather than being an additional assumption. With


$$
A_0(z)=1-z+z^2/2,\qquad
d_s=s![z^s]A_0(z)^n,
$$


differentiation gives


$$
d_s=n(s-1)![z^{s-1}]A_0(z)^{n-1}(-1+z).
$$


Since $v_p(n)=1$,


$$
v_p(d_s)\ge1+v_p((s-1)!).
\tag{1.4}
$$



The boundary-force construction also checks. If


$$
e_{\rm tail}=\sum_r\frac{(b+r)!}{b!}e_{b+r},
\qquad w=U_0^2e_{\rm tail},
$$


then the finite base solution removes $w_{<b}$, leaving precisely


$$
(Vw_{\ge b})_{<b}
$$


as the contact boundary force. This produces turn13’s coefficients


$$
c_s=\sum_{r\ge s}\frac{(b+r)!}{b!}\binom{2n}{r-s}
\tag{1.5}
$$


and its polynomial $a_Q$, with the stated sign.

Finally, the valuation/degree filtration is valid:

* an initial $P$-Newton row $i$ costs at least $\lfloor i/29\rfloor$;
* a contact index $s$ increases degree by at most $s$, and costs at least $\lceil s/29\rceil$;
* a $Q$-boundary contact of index $s$ has degree at most $s-1$.

Consequently the effective degree bounds used below follow from the actual finite operators, not merely from a statement about their coordinate values.

**Audit conclusion.** The missing integral-Newton/graded-degree portion of A4turn26’s MAIN29 interface is verified from turns13/15. This does not independently reprove the supplied original forcing identities, the finite low constants, or the global signed-error theorem. I do not promote turn21’s shifted-class assertions beyond their retained source-interface status.

---

## 2. Adequate precision-three representations without a new full-force expansion

To determine $P,Q\bmod p^3$, we need


$$
Z_w\bmod p^5,\qquad Y\bmod p^6.
$$



The safe cutoffs in turn19 may be used first. The established carry argument applies throughout those safe supports:


$$
W_jB_q(j)\in p^2\mathbb Z_p\quad(0\le q\le145),
$$




$$
W_jB_q(j)\in p\mathbb Z_p\quad(-118\le q\le0),
$$


where


$$
W_j=\binom{n+2}{j},\qquad
B_q(j)=\binom{2n+b-j-1}{b-j-q}.
$$


The special unit-boundary bounds remain


$$
W_jB_0(j),\quad W_jB_{-1}(j),\quad
jW_jB_{-2}(j)\in p^3\mathbb Z_p.
\tag{2.1}
$$



After these reconstruction factors have been applied, the necessary inputs are much smaller:

| Contribution | Precision and support actually needed |
|---|---|
| Positive $P$-kernel | $h_P\bmod p^3$, Newton degree $\le86$, Laurent support $0\le q\le87$ |
| Positive $Q$-contact kernel | $h_Q\bmod p^4$, Newton degree $\le86$, Laurent support $0\le q\le87$ |
| Complete $Q$-factorial boundary | $c_s\bmod p^5$, $0\le s\le88$, Laurent support $-89\le q\le0$ |
| Factorial inputs $r\ge89$ | Coefficient valuation at least $5$, hence killed modulo $p^6$ after negative-power reconstruction |

Thus the existing turn13 polynomials suffice:


$$
h_P=(I-\mathscr V_{58}+\mathscr V_{58}^{\,2})g_P
\pmod{p^3},
\tag{2.2}
$$




$$
h_Q=(I-\mathscr V_{87}+\mathscr V_{87}^{\,2})a_Q
\pmod{p^4}.
\tag{2.3}
$$


Only the scalar boundary coefficients need the additional block:


$$
\boxed{
c_s=\sum_{r=s}^{88}\frac{(b+r)!}{b!}\binom{2n}{r-s}
\pmod{p^5},\qquad 0\le s\le88.
}
\tag{2.4}
$$



The inputs $r\ge60$ do not affect $a_Q\bmod p^4$: their valuation is at least four before the extra contact factor $p$. They must nevertheless be retained in the raw boundary (2.4).

The complete logarithmic forcing is absent only by the whole-force estimate


$$
v_p(h_i^F/b!)
\ge v_p(n!)-v_p(b!)
-\lfloor\log_p(2n+b-1)\rfloor\ge6.
\tag{2.5}
$$


The actual endpoint remains


$$
Z_{w,b}=W_b\,b\theta^P_{b-1},\qquad
Y_b=W_b(1+b\theta^Q_{b-1}).
\tag{2.6}
$$



---

## 3. Four-level factorial stripping modulo $p^3$

### 3.1 The required $p$-free factorial formula

Let


$$
U_p(pm+s)=\prod_{\substack{1\le i\le pm+s\\p\nmid i}}i,
\qquad 0\le s<p,
$$


and put


$$
H_s=\sum_{i=1}^s\frac1i,\qquad
H_s^{(2)}=\sum_{i=1}^s\frac1{i^2}.
$$


For $p=29$,


$$
\boxed{
U_p(pm+s)\equiv
((p-1)!)^m s!
\left[
1+pmH_s+
\frac{p^2m^2}{2}\bigl(H_s^2-H_s^{(2)}\bigr)
\right]\pmod{p^3}.
}
\tag{3.1}
$$



To justify the full-block part, first


$$
H_{p-1}^{(2)}\equiv0\pmod p.
$$


Pairing $i$ with $p-i$ then gives


$$
H_{p-1}\equiv0\pmod{p^2}.
$$


Hence every full block satisfies


$$
\prod_{i=1}^{p-1}(pt+i)\equiv(p-1)!\pmod{p^3}.
$$


The partial block gives (3.1).

**The factor $((p-1)!)^m$ is retained at full required precision.** It is not replaced by $(-1)^m$.

### 3.2 Natural polynomial multipliers

Write


$$
j=LJ+x,\qquad 0\le x<L,\qquad v=b_*-x,
$$


and define


$$
e=\mathbf1_{x>191112},\qquad
u=\left\lfloor\frac{382219+v}{L}\right\rfloor,\qquad
r_q=\mathbf1_{v-q<0}.
$$


For every retained Laurent exponent, $e,u,r_q\in\{0,1\}$. Four exact factorial-stripping steps leave


$$
\boxed{
F(J)(N-J)^e(2N+h-J+1)^u(h-J)^{r_q}.
}
\tag{3.2}
$$



In the low-unit factor, the exponent of $(p-1)!$ at each level is a fixed low carry. Formula (3.1) shows that, after the fixed low power of $p$ is removed, the remaining unit is a polynomial in $J$ of degree at most two modulo $p^3$. At this precision:

* the first two levels have no surviving $J$-dependence;
* the third level can contribute a $p^2J$-term;
* the fourth can contribute $pJ$ and $p^2J^2$.

Thus multiplication by (3.2) gives a bounded, ordinary polynomial—not a function interpolation.

### 3.3 Positive-kernel coefficients may still be frozen

For $r\le87$,


$$
\binom{x+LJ}{r}-\binom xr\in p^3\mathbb Z_p.
\tag{3.3}
$$


This follows by Vandermonde, since


$$
v_p\binom{LJ}{i}\ge4-v_p(i)\ge3
\quad(1\le i\le87).
$$



Therefore:

* the positive $P$-kernel may be frozen at $x$ modulo $p^3$;
* every positive $Q$-coefficient already has a factor $p$, so its freezing error lies in $p^4$, sufficient after its two reconstruction carries.

The boundary coefficient $j$ requires different treatment.

---

## 4. The first nonzero term lost by freezing the unit boundary

The complete raw boundary is


$$
-\sum_s(-1)^{b+s}c_s
\frac{(1+r)^s}{r^s}(1+j+jr^{-1}).
$$


For $s=0,1$, replacing $j=x+LJ$ by $x$ changes it by


$$
LJ\left[
(c_0-c_1)+(c_0-2c_1)r^{-1}-c_1r^{-2}
\right].
\tag{4.1}
$$


The $B_0$ and $B_{-1}$ parts are too highly divisible to matter modulo $p^6$. But $c_1\equiv-1\pmod p$, and the remaining term is


$$
\boxed{
\delta Y_{LJ+x}
\equiv(-1)^{j+1}LJ\,W_jB_{-2}(j)\pmod{p^6}.
}
\tag{4.2}
$$


It can have valuation exactly five. Therefore freezing all boundary coefficients at $x$ is invalid for $Q\bmod p^3$.

### An explicit evaluated coefficient

At $x=0$, the low addition for $B_{-2}$ has exactly one carry. Its divided low unit is


$$
-\frac{26!\,13!\,25!\,14!}
{6!\,28!\,26!\,13!\,19!\,15!}
=
\frac{\binom{25}{6}}{15}
\equiv23\pmod{29}.
$$


Consequently the natural multiplier has the correction


$$
\boxed{
\delta Q_0(J)=23p^2J\,\ell_0(J)\pmod{p^3},
\qquad \ell_0(J)=2N+h-J+1.
}
\tag{4.3}
$$



The leading $P$-low unit at $x=0$ is


$$
\frac{13!\,25!}{5!\,19!\,15!}\equiv14\pmod{29}.
$$


Thus this single low fibre contributes the nonzero residual-polynomial term


$$
\boxed{
3C_n p^2J\,\ell_0(J)^2
}
\tag{4.4}
$$


to the mixed kernel.

This is a **polynomial contribution**, not a claim that the whole scalar defect is nonzero. Its leading scalar contraction is a multiple of $T$, so it disappears on the assigned locus $T=0$.

### Adequate representation

Keeping (4.1), rather than freezing it, produces natural polynomials


$$
P_x(J),Q_x(J)\in(\mathbb Z/p^3\mathbb Z)[J]
$$


such that


$$
P_{LJ+x}\equiv(-1)^{j+1}F(J)P_x(J)\pmod{p^3},
$$




$$
Q_{LJ+x}\equiv(-1)^{j+1}F(J)Q_x(J)\pmod{p^3}.
\tag{4.5}
$$


A safe degree bound is six. Their reductions modulo $p^2$ are the degree-at-most-four representatives audited in turn20.

For $x>b_*$, every positive $P$-power still has $r_q=1$. Hence $P_x$ contains $h-J$. The exact ranges


$$
0\le J\le h\quad(x\le b_*),\qquad
0\le J\le h-1\quad(x>b_*)
$$


can therefore be extended to $0\le J\le h$ in both contractions, adding zero.

---

## 5. Proof of the coordinator’s proposed third-defect formula

Put


$$
c_0=(6C_n)^{-1}.
$$


The supplied leading low constants give coefficientwise divisibility


$$
\sum_x(P_xQ_x-c_0P_x^2)\in p(\mathbb Z/p^3\mathbb Z)[J].
$$


Using the natural representatives just constructed, write


$$
\sum_x(P_xQ_x-c_0P_x^2)
=p\widetilde R(J)+p^2\widetilde S(J)\pmod{p^3},
\tag{5.1}
$$


where


$$
R=\widetilde R\bmod p
$$


is obtained from the degree-at-most-four column representatives modulo $p^2$. In particular,


$$
\deg R\le8<29.
\tag{5.2}
$$



The exact finite-range contraction gives


$$
M-c_0D\equiv
p\sum_{J=0}^{h}F(J)^2\widetilde R(J)
+p^2\sum_{J=0}^{h}F(J)^2\widetilde S(J)
\pmod{p^3}.
\tag{5.3}
$$


The second sum is zero modulo $p$ on $T=0$, by the already justified Lucas contraction. This includes the unfrozen-boundary correction (4.4).

For admissible $t$, put


$$
v=d-t,\qquad
w_t=\binom3t^2B_v^2,
\qquad B_v=\binom{v+6}{6}\pmod p,
$$


where admissibility means


$$
0\le t\le3,\qquad 0\le v\le22.
$$


Retain


$$
r_t=H_{3-t}-H_t+H_v-H_{v+6}.
\tag{5.4}
$$



At an admissible $t$, the exact remaining range is $0\le k\le H$, and


$$
F(pk+t)\equiv
\binom3t\binom{v+6}{6}X_k
\bigl(1+p(E_t+kr_t)\bigr)\pmod{p^2},
\tag{5.5}
$$


with $E_t$ independent of $k$. Also


$$
\widetilde R(pk+t)
\equiv\widetilde R(t)+pk\widetilde R'(t)\pmod{p^2}.
\tag{5.6}
$$


Nonadmissible $t$-terms have $p\mid F(pk+t)$, so their squares vanish modulo $p^2$. This also handles their shorter terminal ranges.

On $T=0$, the $E_t$-terms multiply $\mathcal T\in p\mathbb Z$ and disappear at the required precision. Therefore


$$
\frac1p\sum_{J=0}^{h}F(J)^2\widetilde R(J)
=
r_0T_1+r_1U\pmod p,
\tag{5.7}
$$


where


$$
\boxed{
r_0=\sum_{\rm adm.\ t}w_tR(t),\qquad
r_1=\sum_{\rm adm.\ t}w_t\bigl(R'(t)+2r_tR(t)\bigr).
}
\tag{5.8}
$$



Combining (5.3)–(5.8) proves


$$
\boxed{
\frac{M-c_0D}{p^2}=r_0T_1+r_1U\pmod p
\qquad(T=0).
}
\tag{5.9}
$$


On the additional locus $D_1=0$,


$$
T_1=-\frac{\beta(d)}{f(d)}U,
$$


and hence


$$
\boxed{
\frac{M-c_0D}{p^2}
=
U\left(r_1-r_0\frac{\beta(d)}{f(d)}\right)\pmod p.
}
\tag{5.10}
$$



Thus the proposed reduction **passes**, with the boundary correction retained.

There is no reduction modulo $J^p-J$ in this proof. The derivative is that of the actual degree-at-most-eight polynomial. Replacing $R$ by an arbitrary polynomial representing the same function on $\mathbb F_p$ would not preserve (5.8).

---

## 6. A new bounded lemma: only $C_n$ and $J_{29}$ can occur

The coefficient in (5.10) does not require independent inputs


$$
J_1/p,\ldots,J_{28}/p.
$$


They reduce explicitly to two actual moments.

Let


$$
J_t=[z^{n-t}](1+2z+2z^2)^n,\qquad C=J_0,
\qquad m=n/p\bmod p=7.
$$



### Lemma: the first off-central block

For $1\le t\le28$, put $K_t=J_t/p\bmod p$. Then


$$
\boxed{
K_t=a_tC+b_tJ_{29}\pmod p,
}
\tag{6.1}
$$


where


$$
\boxed{
a_t=
\frac{m(8\cdot20^t-20\cdot8^t)}{12t},
\qquad
b_t=
\frac{(m+1)(20^t-8^t)}{12t}
\quad\text{in }\mathbb F_{29}.
}
\tag{6.2}
$$


In particular,


$$
\boxed{J_1/p=8J_{29}\pmod{29}.}
\tag{6.3}
$$



#### Proof

Frobenius gives $p\mid J_t$ when $1\le t\le28$. Differentiating the generating polynomial gives the exact recurrence


$$
(n-t+1)J_{t-1}
=
2tJ_t+2(n+t+1)J_{t+1}.
\tag{6.4}
$$


At $t=1$,


$$
mC=2K_1+4K_2.
$$


For $2\le t\le27$, setting $L_t=tK_t$ gives


$$
L_{t+1}=-L_t-\frac12L_{t-1}.
\tag{6.5}
$$


The same recurrence starts at $t=1$ if $L_0=-mC$.

Its distinct characteristic roots in $\mathbb F_{29}$ are $20$ and $8$. Hence


$$
L_t=
\frac{(20^t-8^t)K_1
+m(8\cdot20^t-20\cdot8^t)C}{12}.
\tag{6.6}
$$



At $t=28$, (6.4), divided by $p$, gives


$$
-L_{27}=2L_{28}+2(m+1)J_{29}.
$$


Thus the recurrence continuation satisfies


$$
L_{29}=(m+1)J_{29}.
$$


Since $20^{28}=8^{28}=1$, (6.6) gives $L_{29}=L_1=K_1$. Substituting $K_1=(m+1)J_{29}$ proves (6.1)–(6.3). ∎

### Consequence for the low $P$-polynomial

Only $i\le57$ is needed in $g_P\bmod p^2$.

* For $i\le28$, (6.1) supplies all off-central moments.
* For $29\le i\le57$, the factorial coefficient already has a factor $p$; Frobenius leaves only $J_0$ and $J_{29}$ modulo $p$.
* Every contact correction at this precision acts on the leading $C$-multiple.

Therefore there are explicitly constructible low polynomials $h_A,h_B$ such that


$$
\boxed{
h_P=C\,h_A+pJ_{29}h_B\pmod{p^2}.
}
\tag{6.7}
$$


Here $h_A\bmod p^2$ and $h_B\bmod p$ depend only on the fixed low construction parameters, not on additional central moments.

After natural four-level stripping, write correspondingly


$$
P_x=C A_x+pJ_{29}B_x\pmod{p^2}.
\tag{6.8}
$$


The complete $Q_x\bmod p^2$ is independent of the central moments. Expanding the scalar low polynomial gives


$$
\begin{aligned}
\sum_x(P_xQ_x-c_0P_x^2)
={}&C\sum_x\left(A_xQ_x-\frac16A_x^2\right)\\
&+pJ_{29}\sum_xB_x\left(Q_x-\frac13A_x\right)
\pmod{p^2}.
\end{aligned}
$$


Thus


$$
\boxed{
R(J)=C\,R_C(d,J)+J_{29}\,R_{29}(d,J)\pmod p,
}
\tag{6.9}
$$


with


$$
\boxed{
R_C=\frac1p\sum_x\left(A_xQ_x-\frac16A_x^2\right)\bmod p,
}
\tag{6.10}
$$




$$
\boxed{
R_{29}=\sum_x B_x\left(Q_x-\frac13A_x\right)\bmod p.
}
\tag{6.11}
$$


The division in (6.10) is coefficientwise exact by the leading low-constant relation.

### Why the coefficient functions depend only on $d$

At the precision defining $R$:

* all bounded contact/Newton coefficients depend on $n,b$ only through their fixed residues modulo $p^4$, with the original odd parity retained;
* the first-order low-unit corrections depend on $N,h$ only modulo $p$, namely $N\equiv3$, $h\equiv d$;
* the leading polynomial cancellation is a combination of $\ell_0^2,\ell_1^2$ with constant coefficients divisible by $p$.

Consequently higher digits of $N,h$ do not survive the coefficientwise division defining $R_C\bmod p$. Both polynomials in (6.9) are functions only of $d$ and $J$, with degree at most eight in $J$.

This is an algebraic parameter reduction, not an inference from auxiliary samples.

---

## 7. The exact remaining coefficient and the bounded control

Define the linear functional


$$
\mathcal L_d(V)=
\sum_{\rm adm.\ t}w_t\bigl(V'(t)+2r_tV(t)\bigr)
-\frac{\beta(d)}{f(d)}
\sum_{\rm adm.\ t}w_tV(t).
\tag{7.1}
$$


Then


$$
\Gamma_0(d)=\mathcal L_d(R_C(d,\cdot)),
\qquad
\Gamma_1(d)=\mathcal L_d(R_{29}(d,\cdot)).
\tag{7.2}
$$


Equations (5.10) and (6.9) prove formula (A).

A useful check is that the known norm polynomial is actually linear:


$$
\begin{aligned}
K_d(J)
&=11(d+7-J)^2+18(3-J)^2\\
&=\boxed{11(d+4)(d+10-2J)}\pmod{29}.
\end{aligned}
\tag{7.3}
$$


Its two contractions are $f(d)$ and $\beta(d)$, so


$$
\mathcal L_d(K_d)=0.
\tag{7.4}
$$


This checks the normalization and also shows that changing the lift of $c_0$ by $p$ times a unit cannot change the third defect on $D_1=0$: the induced change is a multiple of the leading norm polynomial.

I have not evaluated the 50 quantities in (7.2). In particular, neither


$$
\Gamma_0(d)=\Gamma_1(d)=0
$$


nor a nonzero original-domain third defect is established.

---

## 8. Actual primitive arithmetic and whole signed error

Retain the actual least two-column denominator


$$
N_B=d_B[u,v],\qquad v_{29}(d_B)=0.
$$


With the falling metric,


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
p_n=H_B/g_B,\qquad q_n=A_B/g_B>0.
$$


The primitive multiplier is $1/g_B$ on the integer Gram pair, or $d_B^2/g_B$ on the rational Gram pair. The actual reduced denominator is $q_n$, not a row-clearer.

For


$$
\delta=v_{29}(D),\qquad \mu=v_{29}(M),
$$


the retained arithmetic interface is


$$
v_{29}(g_B)
=
\min\{4F_n+4+\delta,\ 2F_n+F_b+5+\mu\},
$$




$$
v_{29}(q_n)
=
\max\{0,\ 2F_n-F_b-1+\delta-\mu\},
$$


where $F_n=v_{29}(n!)$, $F_b=v_{29}(b!)$.

Norm nonvanishing follows from positivity. Finiteness of the mixed valuation retains the supplied original-family nonvanishing dependency.

For the whole real error


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


the exact evaluated primitive form remains


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
$$


At the supplied status of the complete signed-error theorem,


$$
\epsilon_n>0\quad\text{eventually},\qquad
\log|\epsilon_n|
=
-\left(2+\frac1{2001}\right)n\log(1+\sqrt2)+o(n).
$$


Thus the whole form is eventually negative and nonzero under that retained dependency. The complete exponential residual, logarithmic force, factorial/contact boundary, and endpoint remain included.

---

# Concluding ledger

## (1) New result and proof status

**Proved from the supplied construction formulas, retaining the stated original-force and finite-constant inputs:**

1. The missing integral-Newton/graded-degree interface in A4’s MAIN29 audit is verified explicitly.
2. Existing $h_P\bmod p^3$ and $h_Q\bmod p^4$, together with the complete boundary through $r=88$, suffice for $P,Q\bmod p^3$.
3. Four-level $p$-free factorial stripping gives adequate natural polynomial representatives modulo $p^3$.
4. Freezing the unit-boundary coefficient $j$ would miss the explicit term
   

$$
\delta Q_0=23p^2J\ell_0.
$$


   Its mixed low-fibre contribution is $3C_np^2J\ell_0^2$; its leading scalar contraction is killed by $T=0$.
5. The coordinator’s reduction is valid:
   

$$
\frac{M-c_0D}{p^2}
   =
   U\left(r_1-r_0\frac{\beta(d)}{f(d)}\right)
   \pmod p
   \quad(T=0,\ D_1=0).
$$


6. The first off-central moment block reduces explicitly to $C_n,J_{29}$. Hence the outstanding coefficient has the form
   

$$
C_n\Gamma_0(d)+J_{29}\Gamma_1(d).
$$



**Not proved or computed:** the values of $\Gamma_0,\Gamma_1$, third-depth alignment, an original-power-$3$ counterexample, an all-depth relative valuation bound, or irrationality/rationality of $e+\pi$.

## (2) Exact remaining bottleneck

The immediate missing evaluation is the pair of 25-entry tables


$$
\bigl(\Gamma_0(d)\bigr)_{d=0}^{24},
\qquad
\bigl(\Gamma_1(d)\bigr)_{d=0}^{24}.
$$



If both tables vanish, formula (A) proves third-depth alignment on the entire stated original locus.

If either table does not vanish, that alone is not a counterexample: one must still determine whether


$$
U\bigl(C_n\Gamma_0(d)+J_{29}\Gamma_1(d)\bigr)
$$


can be nonzero for actual $3^a$ indices satisfying $T=0,D_1=0$. In either event, all-depth arithmetic and the final denominator across all primes remain separate obstacles to an irrationality argument.

## (3) Bounded exact computation request

**Request:** evaluate the two low-polynomial coefficient functions in (7.2), not another large contact inverse.

For each $d=0,\ldots,24$, one may use the odd auxiliary parameter


$$
h_d=
\begin{cases}
d,&d\text{ odd},\\
d+29,&d\text{ even},
\end{cases}
\qquad
b_d=b_*+p^4h_d,\qquad n_d=2001b_d.
$$


These are only convenient representatives for the proved finite low-parameter dependence; they are not original power-$3$ test indices.

### Explicit polynomial inputs

Construct $h_A\bmod p^2$ from the turn13 $P$-forcing and contact operator with formal moments


$$
J_0=1,\quad J_{29}=0,\quad
J_t=p\,a_t\ (1\le t\le28),\quad
J_t=0\ (30\le t\le57),
$$


using (6.2).

Construct $h_B\bmod p$ by taking the same formal $P$-construction with


$$
J_0=0,\quad J_{29}=1,\quad
J_t=p\,b_t\ (1\le t\le28),\quad
J_t=0\ (30\le t\le57),
$$


and dividing its resulting $h_P$ by $p$.

Use the complete $Q$-kernel for the already audited precision


$$
Q\bmod p^2:
$$


positive contact polynomial modulo $p^3$, boundary coefficients through $s=59$ at the required precision, and the endpoint-absorbed reconstruction.

Apply the natural four-level stripping modulo $p^2$ to obtain $A_x,B_x,Q_x$, then form (6.10)–(6.11) **as polynomials in $J$**.

### Expected verifiable output

For each $d$:

1. the at-most-nine coefficients of each polynomial
   

$$
R_C(d,J),\quad R_{29}(d,J);
$$


2. a coefficientwise divisibility receipt for the numerator in (6.10);
3. the two residues
   

$$
\Gamma_0(d),\quad\Gamma_1(d)
$$


   obtained from (7.1), using the ordinary polynomial derivative.

This is at most **500 returned field coefficients**, plus divisibility flags. The low-coordinate loop is bounded by $29^4$, independent of $b$; no length-$b$ inverse is required.

The output would evaluate a proved finite coefficient identity underlying the infinite reduction. It would not, by itself, settle reachability of any nonzero defect on the original powers, all-depth valuation alignment, or irrationality of $e+\pi$.
