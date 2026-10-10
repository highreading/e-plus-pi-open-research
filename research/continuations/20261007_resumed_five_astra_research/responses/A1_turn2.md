> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The next complete quadratic digit: an exact reduction and the unresolved boundary terms

## 1. Scope and outcome

This report retains the original progression


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$


and the original definitions


$$
m=2^{2j-1},\quad n=4^j+1,\quad A=n-2,\quad
H=3^{h-1},\quad D=H-A,
$$


with


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$


In particular, on the sufficiently large retained tuples,


$$
v_3(A)=v_3(D)=5,\qquad D\ge486.
$$



The finite coordinates remain


$$
U_u=x^u\ (0\le u<D),\qquad
z_i=x^Dy^i\ (0\le i<\nu),\qquad
Y_b=y^b\ (d\le b\le m),
$$


where


$$
x=y-1,\qquad d=\frac{3D}{2}-1,\qquad \nu=\frac D2-1.
$$


No finite interval is enlarged.

**The requested evaluation of $K_{18}$, its full radical, and its nondegenerate complement is not completed here.** In particular, I do not claim either


$$
\mathcal Q\in3^6M
$$


or a nonzero value of $\mathcal Q/243\bmod3$.

There is, however, a new exact reduction of that digit. Starting with the complete sources of turn22, it:

* retains the actual inverse and complete LOW feedback;
* removes one entire second-order HIGH inverse contribution;
* replaces the remaining first-order inverse feedback by the single original row $d+1$;
* identifies precisely which higher source and boundary residues have not yet been evaluated.

This is a proved reduction, not an evaluated finite-rank formula. The distinction matters: the outstanding term includes the complete leading HIGH source, not just its lower-edge row.

The stronger support and depth-$18$ normalization asserted in turn1 are treated as **conditional pending review**, as required. The retained complete theorem


$$
\mathcal Q\in3^5M_\nu(\mathbb Z_3)
$$


is used without repeating its two lower digit calculations.

---

## 2. Complete objects and normalization

The functional is unchanged:


$$
\mathcal M(G)=
-\frac{3^h}{4}\mathfrak f(G)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](G-G(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^s)=(2s)!.
$$


Thus both the factorial contribution and every denominator through $4n-3$ remain in all exact matrices.

Let


$$
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=-71-A,
$$


and let $F_i$ be the complete core-orthogonal columns


$$
F=Z-WE_c^{-1}C_c,\qquad W=[U\ Y].
$$


The producer is not replaced by a model polynomial. Put


$$
\mathscr R=R_{\rm prod}/3.
$$



Use the complete actual eliminated blocks


$$
E_{\rm act}=
\begin{pmatrix}
3L&3X\\
3X^T&E_Y
\end{pmatrix},
\qquad
\widehat E=E_Y-3X^TL^{-1}X.
$$


Here $L,X,E_Y,\widehat E$ are actual blocks; no core block is silently substituted.

Define the exact source by


$$
T(\mathscr R)=
\bigl(\mathcal M(\mathscr R\,wF_i)\bigr)_{w,i}
=3\binom{\alpha}{\beta_s}.
$$


The turn22 divisibility permits the exact definitions


$$
\alpha=3a,\qquad
\widetilde\beta_s=\beta_s-X^TL^{-1}\alpha
=-\kappa e_m\tau^T+3B,
\tag{2.1}
$$


where $\tau=e_{\nu-1}$, $e_m$ denotes the physical HIGH terminal coordinate, and $\kappa$ is a fixed integral lift of its established residue.

The matrices $a$ and $B$ are integral. Their definitions include the whole functional, the complete columns, and LOW-to-HIGH feedback.

The exact quadratic identity is


$$
\mathcal Q
=81a^TL^{-1}a+
27\widetilde\beta_s^{\,T}\widehat E^{-1}\widetilde\beta_s.
\tag{2.2}
$$


Consequently, to determine $\mathcal Q\bmod729$, it suffices to determine


$$
N:=3a^TL^{-1}a+
\widetilde\beta_s^{\,T}\widehat E^{-1}\widetilde\beta_s
\pmod{27},
\qquad
K_{18}=N/9\bmod3.
\tag{2.3}
$$


The division by $9$ is justified by the retained theorem $\mathcal Q\in243M$.

---

## 3. A new reduction of the complete digit

### 3.1 Exact finite HIGH lift

Use turn21’s finite anti-triangular lift $K_0$, and write


$$
R=K_0^{-1},\qquad \widehat E=K_0+3V.
$$


The exact inverse entries are


$$
R_{bc}=
\begin{cases}
\displaystyle\binom{A+m+d-b-c-1}{m+d-b-c},
&b+c\le m+d,\\
0,&b+c>m+d.
\end{cases}
\tag{3.1}
$$


In particular,


$$
Re_m=e_d,\qquad
Re_{m-1}=e_{d+1}+Ae_d.
\tag{3.2}
$$



The established actual boundary calculation gives


$$
Ve_d\equiv e_{m-1}-e_m\pmod3.
\tag{3.3}
$$


It includes the next pole and LOW feedback. It implies $V_{dd}\in3\mathbb Z_3$.

Turn22 also gives


$$
B_d\in3M_{1,\nu}(\mathbb Z_3)
\tag{3.4}
$$


and


$$
a^TL^{-1}a\in3M_\nu(\mathbb Z_3).
\tag{3.5}
$$


For (3.5), only the already established six-row support of $a\bmod3$ and the leading LOW inverse are needed.

### 3.2 Expansion with every charge retained

Since $\widehat E$ is a unit matrix over $\mathbb Z_3$,


$$
\widehat E^{-1}
\equiv R-3RVR+9RVRVR\pmod{27}.
\tag{3.6}
$$


For a row vector $r$, define


$$
\operatorname{Sym}_\tau(r)=\tau r+r^T\tau^T.
$$


Substitution of (2.1) into (2.3) gives


$$
\begin{aligned}
N\equiv{}&
3a^TL^{-1}a
-3\kappa\operatorname{Sym}_\tau(B_d)
+9\kappa\operatorname{Sym}_\tau((VRB)_d)\\
&+9B^TRB
-3\kappa^2V_{dd}\tau\tau^T
+9\kappa^2(VRV)_{dd}\tau\tau^T
\pmod{27}.
\end{aligned}
\tag{3.7}
$$


This includes the terminal-terminal, terminal-source, source-source, and LOW contributions. No unknown source has been set to zero.

### 3.3 Two finite-boundary simplifications

From (3.3), symmetry, and (3.2),


$$
\begin{aligned}
(VRB)_d
&\equiv(e_{m-1}-e_m)^TRB\\
&=B_{d+1}+(A-1)B_d\\
&\equiv B_{d+1}\pmod3.
\end{aligned}
\tag{3.8}
$$



There is also an exact support reason for


$$
(VRV)_{dd}\equiv0\pmod3.
\tag{3.9}
$$


Indeed, by (3.3) its residue is


$$
(e_{m-1}-e_m)^TR(e_{m-1}-e_m).
$$


All three relevant upper-corner entries of $R$ vanish by (3.1), because


$$
2(m-1)>m+d
$$


on the original window. This is a finite-matrix boundary calculation, not an infinite-inverse approximation.

### Proposition — Complete next-digit reduction

On the retained original family,


$$
\boxed{
\begin{aligned}
K_{18}\equiv{}&
\frac{a^TL^{-1}a}{3}
-\kappa\operatorname{Sym}_\tau\!\left(\frac{B_d}{3}\right)
-\kappa^2\frac{V_{dd}}3\,\tau\tau^T\\
&+\kappa\operatorname{Sym}_\tau(B_{d+1})
+B^TRB
\pmod3.
\end{aligned}}
\tag{3.10}
$$


Each displayed division is separately legitimate by (3.4)–(3.5) and (3.3).

**Proof.** Divide (3.7) by $9$, using those divisibilities, and apply (3.8)–(3.9). ∎

The term removed in (3.9) is the entire second-order terminal inverse contribution. The remaining row $B_{d+1}$ is the actual next lower-edge row.

---

## 4. What (3.10) does—and does not—evaluate

Formula (3.10) exposes a sharper obstruction than “compute the actual inverse.”

The required observed data are:

| Observed quantity | Sufficient precision before division |
|---|---:|
| $a^TL^{-1}a$ | modulo $9$ |
| $B_d$ | modulo $9$ |
| $V_{dd}$ | modulo $9$ |
| $B_{d+1}$ | modulo $3$ |
| $B^TRB$ | modulo $3$ |
| $\kappa$ | modulo $3$, with a fixed lift used in defining $B$ |

These are sufficient observed precisions, **not a proved list of least producer-jet precisions**.

In particular, the six-row formula for $a\bmod3$ does not determine


$$
a^TL^{-1}a/3\bmod3.
$$


To see the missing information explicitly, choose a lift $a_0$ supported in LOW rows $0,\ldots,5$, and write


$$
a=a_0+3a_1.
$$


Choose an integral symmetric lift $L_0^{-1}$ of $L^{-1}\bmod3$ whose entries vanish when the row indices sum to less than $D-1$, and write


$$
L^{-1}=L_0^{-1}+3L_1.
$$


Then


$$
\frac{a^TL^{-1}a}{3}
\equiv
a_0^TL_1a_0+
a_1^TL_0^{-1}a_0+
a_0^TL_0^{-1}a_1
\pmod3.
\tag{4.1}
$$


The second and third terms observe higher LOW source digits at the opposite edge. Their cancellation requires proof in the actual source; it does not follow from six-row support modulo $3$.

Similarly, the proved equality of the source and its LOW feedback at row $d$ gives $B_d\bmod3=0$, but does not evaluate


$$
B_d/3\bmod3.
$$


Finally, the scalar row $B_{d+1}$ does not determine the complete Gram term


$$
B^TRB\bmod3.
$$



Thus (3.10) is not yet a complete short-support identity. Its right-hand side cannot presently be replaced by a zero matrix, a fixed-rank matrix, or a matrix depending only on the six $J_t$.

### Concrete next lemma

The next useful obligation is the following **observed feedback lemma**, in the original finite objects:

> Evaluate jointly
> 

$$
> \frac{a^TL^{-1}a}{3}+B^TRB
>
$$


> and
> 

$$
> \frac{B_d}{3}-B_{d+1}
>
$$


> modulo $3$, together with $V_{dd}/3\bmod3$. Prove which higher producer jets cancel from these combined observations, rather than evaluating the sources independently.

This targets precisely the combinations in (3.10). It also avoids assuming that a higher source vanishes merely because its preceding digit does.

Until this lemma is proved, there is no justified least-precision producer interface and no established fixed residue modulus in $j,h$ for $K_{18}$. I therefore do **not** commission the huge original-tuple computation proposed in turn1, nor the higher endpoint interface of turn22 merely on speculation that its outputs suffice. Neither closed receipt is reopened.

---

## 5. Endpoint, diagonal observation, and relative determinant protection

The actual endpoint and diagonal observation remain


$$
e_{\rm act}=Z(-1)^T-C_{\rm act}^TE_{\rm act}^{-1}w,
\qquad
d_{\rm act}=w^TE_{\rm act}^{-1}w,
\qquad w=W(-1)^T.
\tag{5.1}
$$


The possible loss


$$
d_{\rm act}\in3^{-1}\mathbb Z_3
$$


is retained.

At the established leading precision,


$$
(e_{\rm act})_i\equiv(-1)^i\pmod3.
$$


The stronger observation from turn22 remains an unevaluated formula:


$$
\frac{(e_{\rm act}-e_c)_i}{3^8}
\equiv
-\sum_{t=0}^{5}J_t\sum_{v=0}^{5-t}\binom iv
+\kappa\,\mathbf1_{i=\nu-1}\Pi_D
\pmod3.
\tag{5.2}
$$


Here $\Pi_D$ is evaluated from the actual ternary digits of $D/2$, not a fixed residue of $n$. The physical terminal term is not discarded.

There is an exact target-specific complement identity that explains how one could avoid paying a worst whole-core inverse loss. It does not establish the required original-core congruence.

Suppose an integral normalized residual matrix $U$ has, in a unimodular basis,


$$
U=\begin{pmatrix}A&B\\B^T&C\end{pmatrix},
\qquad A\in\operatorname{GL}_r(\mathbb Z_3),
\qquad e=\binom{u}{v}.
$$


Set


$$
T=C-B^TA^{-1}B,\qquad
f=v-B^TA^{-1}u,\qquad
\gamma=u^TA^{-1}u.
$$


For any scalar $t$ for which $td$ is integral,


$$
\boxed{
e^T\operatorname{adj}(U)e-td\det U
=
\det A\left[
f^T\operatorname{adj}(T)f+
(\gamma-td)\det T
\right].
}
\tag{5.3}
$$


This follows by eliminating the $A$-block in


$$
\begin{pmatrix}U&e\\e^T&td\end{pmatrix};
$$


its determinant is the negative of the left-hand side. The identity holds even when $T$ is singular.

Only the unit complement $A$ is inverted. Nevertheless, protecting the distinguished expression requires control of the complete reduced triple


$$
(T,f,\gamma-td),
$$


not just a congruence for $T$. Cancellation between the two terms in brackets must also be controlled.

For the present objects, no radical/complement decomposition of $K_{18}$ has been established. Accordingly, (5.3) does not yet validate a relative original-core congruence or prove distinguished-cofactor nonvanishing. It identifies the exact target that such a congruence would have to preserve.

---

## 6. Conditional normalization and primitive arithmetic

Only if the reviewed stronger bounds


$$
S_c\in3^{21}M,\qquad \Phi_R\in3^{20}M
$$


hold may one presently infer


$$
\Upsilon_{18}=-S_{\rm act}/3^{18}\in M,
\qquad
\Upsilon_{18}\equiv K_{18}\pmod3.
$$


The unconditional existence of $K_{18}=\mathcal Q/243\bmod3$ does not depend on that stronger normalization.

Under an admissible normalization, retain the whole distinguished pair


$$
\mathcal D_0=\det\Upsilon_{18},
$$




$$
\mathcal D_1=
e_{\rm act}^T\operatorname{adj}(\Upsilon_{18})e_{\rm act}
-3^{18}d_{\rm act}\det\Upsilon_{18}.
$$


Neither determinant nor cofactor has been evaluated here.

For the original rational determinant pair, after the **actual** row contents, actual multiplier, and least simultaneous clearer,


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
\qquad
g_\ell=\gcd(|A_\ell|,|B_\ell|)
$$


with the gcd taken over **all primes**. If $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
$$


and the complete same-index error is


$$
\boxed{
q(e+\pi)-p=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{g_\ell}
\det H_{\rm complete}.
}
\tag{6.1}
$$



These are preserved definitions, not evaluations of the actual contents, clearer, gcd, or primitive denominator.

The complete exponential boundary columns, logarithmic forcing, exterior constant, and physical terminal equation are not removed. In particular, the retained terminal closure remains


$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
$$



---

## 7. Status and next verifiable output

| Item | Status |
|---|---|
| Complete $\mathcal Q\in3^5M$ theorem | Retained at its established original scope |
| Stronger turn1 core support and depth-$18$ normalization | Conditional pending review |
| Formula (3.10) for the next complete digit | Newly derived |
| Vanishing of the second-order terminal inverse term | Proved from exact finite boundaries |
| Reduction of first inverse feedback to $B_{d+1}$ | Proved |
| Evaluation of all terms in (3.10) | Open |
| Full radical and nondegenerate complement of $K_{18}$ | Open |
| Actual endpoint on that decomposition and diagonal observation | Open |
| Original-core relative protection of the bordered determinant | Open |
| Actual contents, least clearer, all-prime gcd, primitive $q$ | Unevaluated |
| Nonzero whole error tending to zero at the same infinite indices | Open |

No bounded producer calculation is yet justified as sufficient for the missing digit. The next expected verifiable output should first be a symbolic certificate for the observed feedback lemma in §4: explicit edge-jet formulas, their paid precisions, and their exact dependence on the original $j,h$. Only if that certificate leaves a genuine bounded producer residue should a numerical interface be specified.

The new result is therefore a complete algebraic reduction of the next digit with two evaluated feedback simplifications—not its requested final evaluation. The local bottleneck is the combined higher LOW/HIGH observation in (3.10). Beyond it remain distinguished-cofactor nonvanishing and the all-prime, whole-error argument on an infinite original sequence.



$$
\boxed{\text{No unconditional proof of rationality or irrationality of }e+\pi
\text{ is obtained.}}
$$


