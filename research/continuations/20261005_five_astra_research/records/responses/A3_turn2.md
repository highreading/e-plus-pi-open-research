> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## A3 continuation: a common finite-state recurrence and an obstruction for positive endpoint-weighted filters

I obtain a common finite-dimensional rational recurrence for the **unnormalized complete endpoint forms**, and a uniform obstruction for a concrete growing-order filter in a specified canonical cofactor normalization. This changes the construction from averages of individually normalized centers: the filter is applied before division by the endpoint.

The obstruction is particularly direct. In this normalization, the complete unnormalized remainders eventually have **one common sign**, while the rational endpoints alternate in sign. Consequently, positive endpoint weights do not cancel the complete remainder. For the concrete filter below, every order $m=o(n^2)$—including $m\asymp n$—leaves the normalized error asymptotically unchanged.

This is not an exclusion of signed endpoint filters, and it does not decide irrationality of $e+\pi$.

---

## 1. Canonical normalization

For each integer $n\ge2$, use exactly the **integer-$L$ raw cofactor normalization** in the contiguous endpoint source:



$$
L_k(t)=2^ki^kP_k(-i(2t-1)),
\qquad
a_j=\ell_j(L_{n+1}),\qquad
t_j=\ell_j(K_n(t,1)),
$$



and take the coefficient vector of the exponential polynomial to be



$$
(B_0,B_1,B_2)
=
\bigl(
a_1(1+t_2)-a_2(1+t_1),\,
a_2(1+t_0)-a_0(1+t_2),\,
a_0(1+t_1)-a_1(1+t_0)
\bigr).
$$



There is no division by $B_0$, by a row content, or by $Y_n$. Taylor reconstruction specifies $A_n,C_n$ at the same scale. Write



$$
X_n=A_n(1),\qquad Y_n=B_n(1)=C_n(1),\qquad
R_n=X_n+(e+\pi)Y_n.
$$



The inherited eventual-normality theorem supplies an unspecified integer $N_*$ such that these forms are nonzero and $Y_n\ne0$ for every $n\ge N_*$.

This scale matters for combinations across indices. Replacing each form by a different projective multiple changes the filter.

---

## 2. Exact common finite-state representation

Here is a finite-state construction retaining the complete rational numerator, including the partial-exponential contractions.

Put $t=n+1$, and let



$$
f_n=\frac{2^n}{(n!)^2},
\qquad
G_n=\frac{(-1)^n2^{2n+3}}{n+1}.
$$



Use the five contraction coordinates



$$
(h_n,u_n,v_n,\mathcal A_n,\mathcal M_n)
$$



from the supplied five-state recurrence, and set



$$
\mathcal B_n=\mathcal M_n+h_n-u_n.
$$



Also introduce the four adjacent endpoint coordinates



$$
A_n^{L}=L_n(1),\quad B_n^{L}=L_{n+1}(1),
\quad w_n,\quad w_{n+1}.
$$



These superscripts distinguish the Legendre endpoints from the approximating polynomial $A_n$.

### 2.1 The nine-coordinate base system

The first five coordinates satisfy the supplied rational linear recurrence. The other four satisfy the same adjacent Legendre recurrence:



$$
L_{n+2}(1)
=
\frac{2(2n+3)}{n+2}L_{n+1}(1)
+\frac{4(n+1)}{n+2}L_n(1),
\tag{1}
$$





$$
w_{n+2}
=
\frac{2(2n+3)}{n+2}w_{n+1}
+\frac{4(n+1)}{n+2}w_n.
\tag{2}
$$



For (2), start from the polynomial recurrence



$$
(k+1)L_{k+1}(y)
=
2(2k+1)(2y-1)L_k(y)+4kL_{k-1}(y).
$$



Subtract its endpoint value, divide by $y-1$, and apply $\mathcal L$. The extra term is a multiple of $\mathcal L(L_k)$, which vanishes for $k\ge1$. Thus (2) is valid in the present domain.

Consequently the nine-vector



$$
z_n=
(h_n,u_n,v_n,\mathcal A_n,\mathcal M_n,
 A_n^{L},B_n^{L},w_n,w_{n+1})^T
$$



has an exact transition



$$
z_{n+1}=M(n)z_n,\qquad M(n)\in\operatorname{Mat}_{9}(\mathbb Q(n)).
\tag{3}
$$



No evaluated transcendental number occurs in this transition.

### 2.2 Complete endpoint outputs

Recover $H_{n+1},J_{n+1},K_{n+1}$ linearly from the first three coordinates and their one-step transition. Define, as in the contiguous source,



$$
S_n=J_{n+1}^2-H_{n+1}K_{n+1},
$$





$$
C_n=(J_{n+1}-H_{n+1})J_n
-(K_{n+1}-J_{n+1})H_n,
$$





$$
W_n=J_{n+1}J_n-K_{n+1}H_n.
$$



Each is a homogeneous quadratic expression in the first three coordinates, with coefficients in $\mathbb Q(n)$. Put



$$
D_n=t^2B_n^{L}C_n-2A_n^{L}S_n,
\tag{4}
$$





$$
Q_n=2w_nS_n-t^2w_{n+1}C_n,
\tag{5}
$$





$$
V_n=\mathcal A_nS_n-t\mathcal B_nC_n-H_{n+1}W_n.
\tag{6}
$$



All three are homogeneous cubic expressions in $z_n$. The complete quotient formulas give



$$
\mathscr X_n=Q_n+2f_nV_n.
\tag{7}
$$



Indeed,



$$
T_P=f_n\mathcal A_n,\qquad
T_U=\frac{2f_n}{t}\mathcal B_n,
$$



so substituting these into the full numerator in the contiguous source gives (7), including the term $-H_{n+1}W_n$.

At the specified raw cofactor scale, set



$$
s_n=\frac{2f_n^2}{G_nt^4}.
$$



Then the exact endpoints are



$$
\boxed{
Y_n=s_nD_n,\qquad
X_n=s_nQ_n+2s_nf_nV_n.
}
\tag{8}
$$



The scale transitions simplify to



$$
\boxed{
\frac{s_{n+1}}{s_n}
=-\frac1{(n+1)(n+2)^3},
\qquad
\frac{s_{n+1}f_{n+1}}{s_nf_n}
=-\frac2{(n+1)^3(n+2)^3}.
}
\tag{9}
$$



Thus all projective scales used here are explicit.

### 2.3 A common recurrence of bounded order

Let $\operatorname{Sym}^3(z_n)$ denote the vector of all degree-three monomials in the nine entries of $z_n$. Its dimension is



$$
\binom{11}{3}=165.
$$



Equations (3) and (9) give an exact rational linear transition for the 330-dimensional vector



$$
\mathcal Z_n=
\begin{pmatrix}
s_n\operatorname{Sym}^3(z_n)\\
s_nf_n\operatorname{Sym}^3(z_n)
\end{pmatrix}.
\tag{10}
$$



Both $X_n$ and $Y_n$ are rational row outputs of this one system.

This supplies a constructive finite-order recurrence, without guessing from numerical values. For example, transport the output rows for $X_{n+j}$ and $Y_{n+j}$ back to $\mathcal Z_n$, and stack the two rows into a vector of length 660. Among the 661 resulting vectors for $0\le j\le660$, there is a nontrivial dependence over $\mathbb Q(n)$. Clearing denominators gives polynomials $c_j(n)$, not all zero, such that



$$
\boxed{
\sum_{j=0}^{660}c_j(n)X_{n+j}=0,
\qquad
\sum_{j=0}^{660}c_j(n)Y_{n+j}=0.
}
\tag{11}
$$



After excluding the finitely many poles used during rational elimination, these are exact identities. The coefficient vector can be specified by maximal minors of the transported-row matrix; a numerical degree scan is unnecessary.

The bound 660 is deliberately nonminimal.

**Important limitation.** Equation (11) also annihilates $R_n$, and its filtered endpoint is zero. It supplies no approximation. Its value is that it establishes a common finite-state structure for the actual unnormalized forms, rather than postulating a density for $R_n/Y_n$.

---

## 3. The sign reversal that obstructs positive endpoint filters

The raw normalization produces a different sign pattern from the normalized errors.

Let



$$
U_n=L_{n+1},\qquad V_n^{K}=K_n(\,\cdot\,,1).
$$



The inherited determinant asymptotics, multiplied by the positive leading coefficient converting the monic $U_n$ into $L_{n+1}$, give



$$
Y_n
\sim
\frac{d_Ve^{-2\sqrt2}}{n(n!)^2}
L_{n+1}(0)K_n(0,1),
\qquad d_V=1+\frac1{\sqrt2}>0.
\tag{12}
$$



Now



$$
\operatorname{sgn}L_{n+1}(0)=(-1)^{n+1},
\qquad K_n(0,1)>0.
$$



Therefore



$$
\operatorname{sgn}Y_n=(-1)^{n+1}
\quad\text{eventually}.
\tag{13}
$$



On the other hand, the whole-error theorem gives



$$
\frac{R_n}{Y_n}
\sim (-1)^n(\sqrt2-1)^2\epsilon_n,
\qquad \epsilon_n>0.
$$



Combining this with (13),



$$
\boxed{R_n<0\quad\text{for all sufficiently large }n.}
\tag{14}
$$



This is the **whole evaluated remainder**, not its first omitted Taylor coefficient.

### General positive-weight obstruction

Take any finite nonnegative weights $a_j$, not all zero, supported on sufficiently large indices, and suppose $\sum_j a_jY_{n+j}\ne0$. Then



$$
\left|
\frac{\sum_j a_jR_{n+j}}{\sum_j a_jY_{n+j}}
\right|
=
\frac{\sum_j a_j|R_{n+j}|}
{\left|\sum_j a_jY_{n+j}\right|}
\ge
\min_{j:a_j>0}\left|\frac{R_{n+j}}{Y_{n+j}}\right|.
\tag{15}
$$



The numerator cannot cancel. Cancellation in the denominator can only worsen this inequality.

This does not prohibit obtaining the accuracy of the largest index in the window. It does prohibit positive weights from manufacturing a complete-error cancellation beyond the best individual error in that window.

---

## 4. A concrete growing filter: uniformly no gain for $m=o(n^2)$

Use the rational polynomial



$$
g(T)=1+6T+T^2,\qquad
g(T)^m=\sum_{j=0}^{2m}a_{m,j}T^j.
$$



Unlike the earlier normalized-center filters, define



$$
\boxed{
c_{n,m}
=
-\frac{\sum_{j=0}^{2m}a_{m,j}X_{n+j}}
{\sum_{j=0}^{2m}a_{m,j}Y_{n+j}}.
}
\tag{16}
$$



All coefficients are positive integers and $a_{m,0}=1$.

### 4.1 Uniform adjacent-ratio bounds

Equation (12), the Legendre endpoint ratio limits, and the explicit norm formula show that



$$
\left|\frac{Y_{k+1}}{Y_k}\right|=O(k^{-2}).
\tag{17}
$$



For clarity, $L_{k+2}(0)/L_{k+1}(0)$ is bounded, and $K_{k+1}(0,1)/K_k(0,1)$ is bounded: both follow from the endpoint ratios and the exact Christoffel–Darboux expression for $K_k(0,1)$. The factorial quotient in (12) contributes $(k+1)^{-2}$.

Also



$$
\left|\frac{(R_{k+1}/Y_{k+1})}{(R_k/Y_k)}\right|
\longrightarrow 3-2\sqrt2,
$$



because the inherited error asymptotic and the reference $\epsilon$-ratio both have nonzero limits. Hence



$$
\left|\frac{R_{k+1}}{R_k}\right|=O(k^{-2}).
\tag{18}
$$



Thus there are fixed $C,N>0$ such that, for $k\ge N$,



$$
|Y_{k+1}/Y_k|\le C/k^2,\qquad
|R_{k+1}/R_k|\le C/k^2.
$$



Iterating gives, for every $j\ge0$,



$$
\left|\frac{Y_{n+j}}{Y_n}\right|,
\left|\frac{R_{n+j}}{R_n}\right|
\le \left(\frac C{n^2}\right)^j,
\qquad n\ge N.
\tag{19}
$$



The constants do not depend on the filter order.

### 4.2 Filter estimate

Set $x=C/n^2$. Positivity of the filter coefficients gives



$$
\left|
\frac{\sum_j a_{m,j}Y_{n+j}}{Y_n}-1
\right|
\le g(x)^m-1,
\tag{20}
$$



and the identical bound holds with $Y$ replaced by $R$.

If $m=o(n^2)$, then



$$
g(C/n^2)^m-1=O(m/n^2)=o(1).
$$



Consequently the denominator in (16) is nonzero for all sufficiently large $n$, uniformly along every such order sequence, and



$$
\boxed{
e+\pi-c_{n,m}
=
\frac{R_n}{Y_n}
\left(1+O\!\left(\frac m{n^2}\right)\right),
\qquad m=o(n^2).
}
\tag{21}
$$



In particular, the complete filtered error is nonzero, and



$$
\boxed{
\log|e+\pi-c_{n,m}|
=-2n\log(1+\sqrt2)+o(n).
}
\tag{22}
$$



For $m\asymp n$, the relative change is only $O(1/n)$.

This is a proved obstruction for the specified canonical normalization and concrete growing filter. The order may grow proportionally to $n$, but the raw factorial decay makes the first form dominate the entire combination. The polynomial $g$ that was designed around the geometric ratio of the *normalized* errors does not target the scale of the raw forms.

It is not a statement about filters with factorially compensating or signed weights.

---

## 5. Actual primitive denominator, with all scales retained

For the filter (16), form the rational numbers



$$
\mathcal X_{n,m}
=\sum_j a_{m,j}s_{n+j}\bigl(Q_{n+j}+2f_{n+j}V_{n+j}\bigr),
$$





$$
\mathcal Y_{n,m}
=\sum_j a_{m,j}s_{n+j}D_{n+j}.
\tag{23}
$$



Choose the explicit common clearer



$$
L_{n,m}
=
\operatorname{lcm}_{0\le j\le2m}
\bigl(\operatorname{den}(X_{n+j}),
      \operatorname{den}(Y_{n+j})\bigr).
$$



Set



$$
U_{n,m}=L_{n,m}\mathcal X_{n,m},\qquad
Z_{n,m}=L_{n,m}\mathcal Y_{n,m},
$$



and retain the **final** gcd



$$
d_{n,m}=\gcd(|U_{n,m}|,|Z_{n,m}|).
$$



On $Z_{n,m}\ne0$, the actual primitive pair is



$$
\boxed{
P_{n,m}
=-\operatorname{sgn}(Z_{n,m})\frac{U_{n,m}}{d_{n,m}},
\qquad
Q_{n,m}=\frac{|Z_{n,m}|}{d_{n,m}}>0.
}
\tag{24}
$$



Thus



$$
\boxed{
Q_{n,m}(e+\pi)-P_{n,m}
=
Q_{n,m}
\frac{\sum_j a_{m,j}R_{n+j}}
{\sum_j a_{m,j}Y_{n+j}}.
}
\tag{25}
$$



The $s_{n+j}$ in (23) cannot be canceled separately across the sum. A common scalar multiplying the entire sum does cancel through (24). Formula (24) also includes any coefficient-content cancellation automatically.

Combining (21) with (25),



$$
\log|Q_{n,m}(e+\pi)-P_{n,m}|
=
\log Q_{n,m}
-2n\log(1+\sqrt2)+o(n)
$$



in the proved window. No useful estimate for this final $Q_{n,m}$ has been established.

---

## 6. Independent check of A1

### First literal issue: its factorial upper bound is false

A1 writes



$$
D_{2r}+D_{2r+2}\le (2r)!+(2r+2)!.
$$



With the supplied convention



$$
D_j=j!\sum_{a=0}^{j}\frac1{a!},
$$



one instead has $D_j>j!$ for $j\ge1$; for example, $D_2=5>2$.

This is the first issue in the displayed determinacy proof. It is harmless to the conclusion: replace the bound by



$$
D_{2r}+D_{2r+2}
\le e\bigl((2r)!+(2r+2)!\bigr)
\le2e(2r+2)!.
$$



The same Stieltjes Carleman series then diverges.

### No subsequent misuse of Stieltjes determinacy or Gaussian weak convergence found

After that constant-factor repair:

* the condition uses $m_r^{-1/(2r)}$, as required for the Stieltjes problem;
* tightness follows from the common first moment;
* the next exact moment supplies uniform integrability of every fixed power;
* every weak subsequential limit is supported on $[0,\infty)$ and has all the prescribed moments;
* Stieltjes determinacy identifies that limit with $\nu$;
* positive mass in finitely many disjoint open intervals forces nodes in all of them eventually.

The quasi-orthogonality and interlacing argument then proves the compact-root conclusion at its stated, ineffective scope.

### Signed stationary bound

I also find the signed stationary estimate correct, conditional on the stated nonsingularity of $H$. In particular,



$$
\mathcal J(F^2)=\mathcal J(P^2)-h^TH^{-1}h
$$



and



$$
h^TG^{-1}h\le\mathcal M(P^2)
$$



give exactly



$$
|\mathcal J(F^2)|
\le(1+\theta_n^{-1})\mathcal M(P^2).
$$



No minimization of the signed form is used. The estimate remains an upper bound only; it does not establish the required spectral gap or whole-error nonvanishing independently of the inherited arithmetic argument.

---

## 7. Handoff

### (1) New result and proof status

**Proved here, using the supplied endpoint identities and five-state transition:**

1. A 330-dimensional rational linear system for the complete raw $b=2$ endpoint pair, and a constructive common scalar recurrence of order at most 660.
2. Eventual one-sign behavior of the complete raw remainders in the specified integer-$L$ cofactor normalization.
3. The positive-weight inequality (15).
4. For the concrete endpoint filter $g(T)^m$, uniform asymptotic invariance of the normalized whole error whenever $m=o(n^2)$, including denominator nonvanishing and error nonvanishing.
5. The exact primitive denominator formula (24), retaining all cross-index scales and the final gcd.

**A1 audit:** one incorrect factorial bound, repaired by a fixed factor $e$; no resulting failure of its compact-root proof or signed stationary inequality found.

### (2) Exact remaining bottleneck

The present positive filter cannot exploit cancellation: raw remainders have one sign and raw factorial decay makes the first term dominate.

A genuinely different next filter must compensate this factorial scale and use signed weights, while **not** falling into the common annihilator (11). The common recurrence now makes that a finite-state question: separate a small remainder output from a surviving endpoint output, uniformly under growing products of rational transitions. After that, the final gcd in (24), rather than any individual-form denominator, still controls primitive shrinking.

No signed separation estimate or corresponding primitive-denominator bound is proved here.

### (3) Computation request

**None required for the results above.** In particular, constructing a large explicit scalar annihilator would add bulk without producing a new approximation. The useful next step is analytic separation of the two outputs of the displayed finite-state system, not a degree scan or an extrapolation from finite values.
