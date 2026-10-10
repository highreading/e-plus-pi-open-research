> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1, Turn 3 — Jacobi inverse stability, a linear-size content certificate, and the remaining original-window resonance issue

## Executive conclusion

The retained Jacobi inverse does give a more direct route to the core inverse-loss question. Two parts of that route can be closed rigorously.

1. **The complete core is exactly an integral $3^h$-perturbation of the pure-integral Jacobi matrix.** There is no missing pole-tail correction in this comparison: on the original finite matrix, the pole sum is the complete integral moment. The difference is precisely the factorial matrix.

2. **Whenever the retained unit-normalized inverse formula applies, that factorial perturbation preserves the inverse-loss invariant.** Its relative depth is at least two digits. After the original unimodular basis change and integral Schur correction, the full inverse loss equals the Schur inverse loss on the retained depth-$26$ window. More generally, it is the maximum of the eliminated and residual inverse losses.

There are two further advances.

3. **The content of $J_m$ has an exact constant-state ternary digit evaluator.** This uses the full polynomial content in the displayed Bernstein-type basis, not $J_m(-1)$. The basis really is unimodular over $\mathbb Z_3$. The evaluator accepts the actual
   

$$
m=2^{2j-1},
$$


   and does not replace its lower ternary digits by auxiliary ones.

4. **The bivariate content of the complete inverse numerator $\mathcal E$ reduces exactly to a two-column coefficient-content problem.** A unimodular Bezout map gives
   

$$
\boxed{
   \operatorname{cont}_3(\mathcal E)
   =
   \min_{i<k}v_3(t_i z_k-z_i t_k),
   \qquad
   T(X)=XZ(X)+\mathfrak a J_m(X).
   }
$$


   A single primitive pivot reduces these quadratic-many minors to a linear-size certificate, retaining all cancellation.

These results do **not** yet prove $s_c<32$ on the original fixed window, nor exclude it on a proved original subfamily. There is also a scope issue that must not be concealed: the supplied proof of the unit normalizer $\mathfrak a=a_m/3$ is on the earlier **resonant family**, not automatically on every index in the current fixed window. The algebraic inverse identity is reusable more broadly, but its asserted unit valuations require their own hypotheses.

Thus the direct comparison is now mathematically justified where its normalization hypotheses hold. The unresolved part is the original-family content and resonance calculation—not another return-annihilator argument.

No computation was executed, and no accepted bounded computation is proposed for repetition.

---

## 1. Original domain and notation

Retain


$$
n=4^j+1,\qquad j>0,\qquad 81\mid j,
$$


and the sufficiently large original window


$$
j\equiv81\pmod{243},\qquad
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$


As before,


$$
A=4^j-1=H-D,\qquad H=3^{h-1},
$$




$$
m=\frac{A+1}{2}=2^{2j-1},\qquad
d=\frac{3D}{2}-1,\qquad \nu=\frac D2-1.
$$



The original finite polynomial space is


$$
\mathcal P_m=\{P:\deg P\le m\},
$$


with columns


$$
U_u=(y-1)^u\quad(0\le u<D),
$$




$$
z_i=(y-1)^Dy^i\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m).
$$



I use $X,Y$ for the independent variables in inverse kernels, to avoid confusing them with the retained shorthand $x=y-1$.

The accepted results remain


$$
S_c\in3^{26}M_\nu(\mathbb Z_3),\qquad
S_{\rm act}-S_c\in3^{32}M_\nu(\mathbb Z_3),
$$


under all their simultaneous original support, saturation, and degree hypotheses.

---

## 2. Exact identification of the factorial perturbation

Write


$$
\beta_c=-71-A,\qquad
Q_c(y)=(y+1)(y-1)^A(\beta_c+3y).
$$


The subscript distinguishes this coefficient from the Jacobi recurrence coefficient.

The complete core form is


$$
G_c(P,Q)=\mathcal M(Q_cPQ),
$$


where


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\sum_{\substack{v\ge0\\2v+1\le4n-3}}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1}.
$$



Since $Q_c(-1)=0$,


$$
\frac{Q_c(y)P(y)Q(y)-Q_c(-1)P(-1)Q(-1)}{y+1}
=(y-1)^A(\beta_c+3y)P(y)Q(y).
$$



For $P,Q\in\mathcal P_m$, the degree of the right side is at most


$$
A+1+2m=2A+2=2n-2.
$$


This is exactly the original pole cutoff:


$$
v\le 2n-2
\iff 2v+1\le4n-3.
$$



Therefore **all** its coefficients occur in the original finite sum. Using


$$
\frac1{2v+1}=\frac12\int_0^1 t^{v-1/2}\,dt,
$$


the pole part is exactly


$$
\frac{3^h}{2}\int_0^1
t^{-1/2}(t-1)^A(\beta_c+3t)P(t)Q(t)\,dt.
$$



Put


$$
r_0=\frac{A+71}{3},\qquad
c=\frac{(-1)^A3^h}{2}.
$$


Then the pure-integral matrix $G_J$, in monomials $1,y,\ldots,y^m$, is


$$
(G_J)_{ab}
=
3c\int_0^1t^{a+b}(t-r_0)t^{-1/2}(1-t)^A\,dt.
$$



Consequently,


$$
\boxed{G_c=G_J+3^hF_c,}
\tag{2.1}
$$


where


$$
(F_c)_{ab}
=-\frac14\,\mathfrak f(Q_cy^{a+b}),
\qquad 0\le a,b\le m.
\tag{2.2}
$$


Because $Q_c\in\mathbb Z[y]$ and


$$
\mathfrak f(y^r)=(2r)!,
$$


we have


$$
F_c\in M_{m+1}(\mathbb Z_3).
$$



This proves the proposed perturbation statement at the **original size and cutoff**. It is an exact identity, not a high-precision omission of the factorial force.

Also, $r_0>1$ on the present domain, so the integral weight has constant nonzero sign on $(0,1)$. Hence $G_J$ is nonsingular over $\mathbb Q$.

---

## 3. Factorial perturbations preserve sufficiently shallow inverse loss

For a nonsingular matrix $M$ over $\mathbb Q_3$, define


$$
\lambda(M)=\max\left(0,-\min_{i,k}v_3((M^{-1})_{ik})\right).
$$



### Lemma 3.1 — Integral perturbation stability

Suppose


$$
M'=M+3^hF,\qquad F\in M_N(\mathbb Z_3),
$$


and


$$
\lambda(M)<h.
$$


Then $M'$ is nonsingular and


$$
\boxed{\lambda(M')=\lambda(M).}
\tag{3.1}
$$



Moreover,


$$
M^{-1}(M'-M)\in3^{h-\lambda(M)}M_N(\mathbb Z_3).
$$



#### Proof

Set


$$
K=M^{-1}3^hF.
$$


Then $K\in3M_N(\mathbb Z_3)$, so $I+K$ is unimodular and


$$
(M')^{-1}=(I+K)^{-1}M^{-1}.
$$


Multiplication on the left by a unimodular integral matrix preserves the minimum valuation of the entries: one inequality follows from integrality, and the reverse follows by multiplying by its integral inverse. ∎

### Application to the retained inverse kernel

The retained formula, when its stated unit hypotheses hold, is


$$
\sum_{a,b=0}^{m}(G_J^{-1})_{ab}X^aY^b
=
\frac{2\,3^{2-h}}{\mathfrak a N_m}\,
\mathcal E(X,Y),
$$


with


$$
\mathfrak a,N_m\in\mathbb Z_3^\times,\qquad
\mathcal E\in\mathbb Z_3[X,Y].
$$


Thus


$$
\lambda(G_J)
=
\max\{0,h-2-\operatorname{cont}_3(\mathcal E)\}
\le h-2.
$$


Equations (2.1) and (3.1) give


$$
\boxed{
\lambda(G_c)=\lambda(G_J)
=
\max\{0,h-2-\operatorname{cont}_3(\mathcal E)\}.
}
\tag{3.2}
$$


The relative factorial perturbation has depth at least


$$
h-\lambda(G_J)\ge2.
$$



This is the requested precise justification. The factorial term is retained in the matrix, but cannot change this inverse-loss invariant.

---

## 4. A necessary normalization-scope qualification

The supplied earlier inverse report establishes


$$
v_3(a_m)=1,\qquad
\mathfrak a=a_m/3\equiv25\pmod{27}
$$


on its constructed resonant family. Its later unit-normalized conclusions explicitly refer to that family.

The present fixed-window conditions imply


$$
v_3(A)=5,
$$


but do not, in the supplied proofs, independently imply the displayed valuation of $a_m$. Nor does the real window prove intersection with the earlier endpoint-unit digit branch.

Accordingly:

- the classical Jacobi identities are reusable;
- the exact factorial comparison (2.1) holds throughout the present window;
- the application (3.2) holds wherever the retained unit-normalized kernel hypotheses have been established;
- a blanket application of (3.2) to the entire current window needs the corresponding normalization proof.

This is not merely a question about the value of an unspecified unit. If $v_3(\mathfrak a)\ne0$, the scalar prefactor changes valuation, and integrality assertions involving the Christoffel quotient require rechecking.

A generally valid rational form of the same bookkeeping is


$$
\lambda(G_J)
=
\max\left\{
0,\,
h-2+v_3(\mathfrak a)+v_3(N_m)
-\operatorname{cont}_3(\mathcal E)
\right\},
\tag{4.1}
$$


whenever the algebraic kernel identity is used with its actual rational quantities. Only after their valuations are established may this be simplified.

The warning about resonance therefore remains relevant to the new depth-$32$ application.

---

## 5. Original basis changes and the full-versus-Schur loss

### 5.1 The original polynomial basis is unimodular

Order the columns as


$$
[U\ Z\ Y].
$$


Their degrees are, respectively,


$$
0,\ldots,D-1;\qquad
D,\ldots,d-1;\qquad
d,\ldots,m.
$$


Each is monic of its indicated degree. Thus its coefficient matrix in the monomial basis is triangular with diagonal entries $1$.

Hence


$$
[U\ Z\ Y]
$$


is a $\mathbb Z_3$-unimodular basis. Permuting the columns to $[W\ Z]$, with $W=[U\ Y]$, preserves unimodularity.

### 5.2 Integral Schur correction is also unimodular

Write the matrix in this basis as


$$
\begin{pmatrix}
E_c&B_c^{\rm mix}\\
(B_c^{\rm mix})^T&C_c
\end{pmatrix}.
$$


The retained integral corrected residual columns mean precisely that


$$
L_c=E_c^{-1}B_c^{\rm mix}
$$


is integral. The change


$$
\widehat Z^{\,c}=Z-WL_c
$$


is therefore represented by a block-unipotent matrix over $\mathbb Z_3$. It gives


$$
G_c\sim_{\mathbb Z_3}
\begin{pmatrix}
E_c&0\\
0&S_c
\end{pmatrix}.
$$



For nonsingular $S_c$,


$$
\boxed{
\lambda(G_c)=\max\{\lambda(E_c),\lambda(S_c)\}.
}
\tag{5.1}
$$



The accepted eliminated-block result supplies


$$
\lambda(E_c)\le1.
$$


It need not be strengthened to equality to settle the present comparison. Since


$$
S_c\in3^{26}M_\nu(\mathbb Z_3),\qquad \nu>0,
$$


nonsingularity implies


$$
s_c:=\lambda(S_c)\ge26.
$$


Therefore


$$
\boxed{\lambda(G_c)=s_c=\max(1,s_c).}
\tag{5.2}
$$



The precise general statement is (5.1). The formula with $1$ is justified here by $s_c\ge26$, not by silently upgrading an upper bound for the eliminated loss to an equality.

Combining the results, on the unit-normalized branch,


$$
\boxed{
s_c=h-2-\operatorname{cont}_3(\mathcal E).
}
\tag{5.3}
$$


In particular,


$$
\boxed{
s_c<32
\iff
\operatorname{cont}_3(\mathcal E)\ge h-33.
}
\tag{5.4}
$$


The accepted depth also yields the consistency bound


$$
\operatorname{cont}_3(\mathcal E)\le h-28.
\tag{5.5}
$$



Thus the new transfer asks for a content decision in a narrow, explicitly identified range.

---

## 6. Full polynomial content of $J_m$

The classical integral-at-$3$ normalization is


$$
J_s(X)=
\sum_{k=0}^{s}
\binom{s+A}{k}
\binom{s-\tfrac12}{s-k}
X^k(X-1)^{s-k}.
$$


For $s=m$, $A=2m-1$, this is exactly


$$
\boxed{
J_m(X)=
\sum_{k=0}^{m}
\binom{3m-1}{k}
\binom{m-\tfrac12}{m-k}
X^k(X-1)^{m-k}.
}
\tag{6.1}
$$



This is the supplied normalization, not an independently rescaled Jacobi polynomial. The background is classical Jacobi theory of the kind recorded in DLMF §§18.2, 18.3, and 18.5; no novelty is claimed for it.

### 6.1 The Bernstein-type basis is unimodular

Let


$$
b_k(X)=X^k(X-1)^{m-k}.
$$


The least degree occurring in $b_k$ is $k$, with coefficient


$$
(-1)^{m-k}.
$$


Therefore the coefficient matrix from $(b_0,\ldots,b_m)$ to monomials is triangular with diagonal entries $\pm1$. It is unimodular over $\mathbb Z$.

It follows that


$$
\boxed{
\operatorname{cont}_3(J_m)
=
\min_{0\le k\le m}
\left[
v_3\binom{3m-1}{k}
+
v_3\binom{m-\tfrac12}{m-k}
\right].
}
\tag{6.2}
$$



This is a polynomial-content formula. It neither evaluates nor assumes anything about $J_m(-1)$.

---

## 7. An exact small-state digit evaluator for (6.2)

Put


$$
N=3m-1,\qquad \alpha=m-\frac12,\qquad r=m-k.
$$



For nonnegative integer $k$,


$$
v_3\binom Nk
$$


is the number of borrows in ternary subtraction of $k$ from $N$.

For $r\ge0$, the same borrow rule applies to


$$
v_3\binom{\alpha}{r},
$$


with the ternary digits of the $3$-adic integer $\alpha$. One justification is to replace $\alpha$ by sufficiently long nonnegative integer truncations. The binomial values converge $3$-adically, while the finite subtraction borrows stabilize.

Here the digits of $\alpha$ are eventually all $1$, since


$$
-\frac12=(1111\cdots)_3
$$


as a $3$-adic integer. Once the digits of $r$ vanish, any incoming borrow clears at the next such digit $1$.

### Dynamic program

Read ternary digits from low to high. A state consists of three bits:

- the carry $c$ in $k+r=m$;
- the borrow $b$ in $N-k$;
- the borrow $e$ in $\alpha-r$.

At position $i$, choose $k_i,r_i\in\{0,1,2\}$, subject to


$$
k_i+r_i+c=m_i+3c'.
$$


Set


$$
b'=\mathbf1_{\{N_i-k_i-b<0\}},
\qquad
e'=\mathbf1_{\{\alpha_i-r_i-e<0\}}.
$$


The transition cost is


$$
b'+e'.
$$



Start at $(0,0,0)$, and minimize total cost over paths terminating with zero carry and zero borrows, with $k_i=r_i=0$ beyond the allowed finite integer lengths.

There are at most eight states and nine trial digit pairs per state per position. Processing through the finite digits and an eventual-$1$ clearing position gives the exact minimum (6.2).

Thus the content of $J_m$ is computable with a number of state transitions linear in the ternary digit length of $m$. The interface is the actual integer


$$
m=2^{2j-1}.
$$


Constructing or supplying those actual digits remains part of the input cost.

The same construction gives


$$
\operatorname{cont}_3(J_{m-1})
=
\min_{0\le k\le m-1}
\left[
v_3\binom{3m-2}{k}
+
v_3\binom{m-\tfrac32}{m-1-k}
\right].
\tag{7.1}
$$



No assertion about arbitrary auxiliary low digits is needed or made.

---

## 8. Incorporating $Z$, the adjacent Jacobi polynomial, and cancellation

Use the retained exact quantities


$$
\widehat Q(X)
=(X-b_m)J_m(X)-\rho J_{m-1}(X),
$$




$$
Z(X)=
\frac{(X-b_m-a_m)J_m(X)-\rho J_{m-1}(X)}
{3X-\eta},
\qquad \eta=A+71.
$$


On the retained resonant normalization,


$$
v_3(b_m)=1,\qquad v_3(a_m)=1,\qquad v_3(\rho)=4,
$$


and $3X-\eta$ has unit coefficient content.

Put


$$
r=\operatorname{cont}_3(J_m),\qquad
u=\operatorname{cont}_3(J_{m-1}),\qquad
z=\operatorname{cont}_3(Z).
$$



Gauss content multiplicativity gives the exact identity


$$
z=
\operatorname{cont}_3\!\left(
(X-b_m-a_m)J_m-\rho J_{m-1}
\right).
\tag{8.1}
$$


Therefore


$$
z\ge\min(r,4+u),
$$


with equality if $r\ne4+u$. At equality of the two candidate valuations, whole-polynomial cancellation must be retained.

### 8.1 Two nonresonant content branches are settled

Recall


$$
\mathcal E(X,Y)=
Z(X)Z(Y)+\mathfrak a
\frac{J_m(X)Z(Y)-Z(X)J_m(Y)}{X-Y}.
$$



On the retained normalization, $\mathfrak a$ is a unit.

#### Branch I: $r<4+u$

Here $z=r$, and reduction after division by $3^r$ gives


$$
\overline Z=X\overline J
$$


because $-\eta\equiv1\pmod3$, while $b_m+a_m\equiv0\pmod3$.

Consequently,


$$
3^{-2r}\mathcal E(X,Y)
\equiv
(XY-\overline{\mathfrak a})\overline J(X)\overline J(Y)
\pmod3.
$$


This is nonzero. Hence


$$
\boxed{\operatorname{cont}_3(\mathcal E)=2r
\qquad(r<4+u).}
\tag{8.2}
$$



#### Branch II: $r>4+u$

Now $z=4+u<r$. The product $Z(X)Z(Y)$ has content $2z$, whereas the Bezout term has content at least $r+z>2z$. Thus


$$
\boxed{\operatorname{cont}_3(\mathcal E)=2(4+u)
\qquad(r>4+u).}
\tag{8.3}
$$



These two branches incorporate the adjacent polynomial and all scalar valuations. They are stronger than a bound for $J_m$ alone.

#### Remaining collision branch

The unresolved branch is


$$
\boxed{r=4+u.}
\tag{8.4}
$$


Here both the construction of $Z$ and the two terms defining $\mathcal E$ can cancel. The next section gives an exact certificate for that cancellation rather than ignoring it.

---

## 9. A new exact reduction of the whole inverse content

Define


$$
T(X)=XZ(X)+\mathfrak a J_m(X).
$$


Then


$$
\boxed{
(X-Y)\mathcal E(X,Y)
=T(X)Z(Y)-Z(X)T(Y).
}
\tag{9.1}
$$



Write


$$
T(X)=\sum_{i=0}^{m+1}t_iX^i,\qquad
Z(X)=\sum_{i=0}^{m+1}z_iX^i,
$$


where $z_{m+1}=0$.

### Lemma 9.1 — Bezout-content identity

For these actual coefficient vectors,


$$
\boxed{
\operatorname{cont}_3(\mathcal E)
=
\min_{0\le i<k\le m+1}
v_3(t_i z_k-z_i t_k).
}
\tag{9.2}
$$



#### Proof

The numerator in (9.1) has coefficients


$$
t_i z_k-z_i t_k.
$$


Division of an antisymmetric polynomial by $X-Y$ is integral. Conversely, multiplication by $X-Y$, a polynomial of content zero, preserves content by Gauss’s lemma.

Hence the content of the quotient equals the content of the antisymmetric numerator, which is the displayed minimum. ∎

This keeps the whole Christoffel numerator and every cancellation. It does not substitute an endpoint value.

### 9.2 A single-pivot certificate

Let


$$
z=\min_i v_3(z_i),
$$


and choose $p$ attaining the minimum. Put


$$
\widetilde z_i=3^{-z}z_i,
\qquad \widetilde z_p\in\mathbb Z_3^\times.
$$


Define


$$
w_i=t_i-\frac{t_p}{\widetilde z_p}\widetilde z_i.
$$


Then $w_p=0$, and


$$
\boxed{
\operatorname{cont}_3(\mathcal E)
=
z+\min_i v_3(w_i).
}
\tag{9.3}
$$



Indeed, minors involving $p$ are a unit times $3^zw_i$; every other minor is an integral linear combination of those pivot minors.

Thus one need not construct the $(m+1)\times(m+1)$ inverse matrix or all its bivariate coefficients. Exact content can be certified from two coefficient streams and one primitive pivot.

**Complexity qualification.** This is a linear-size coefficient certificate, not yet a constant-state digit evaluator for the whole $\mathcal E$. A dense implementation still processes $O(m)$ coefficients. Calling it a small original-index computation would be unjustified.

---

## 10. What has and has not been decided about $s_c<32$

On every original input where the retained unit normalization is certified:

- compute $r$ and $u$ by the small-state digit programs;
- if $r<4+u$, then
  

$$
s_c=h-2-2r;
$$


- if $r>4+u$, then
  

$$
s_c=h-2-2(4+u);
$$


- if $r=4+u$, use the exact pivot certificate (9.3).

The first two cases are therefore exact digit decisions, with no endpoint-unit hypothesis:


$$
s_c<32
\iff
2\min(r,4+u)\ge h-33
\qquad(r\ne4+u).
\tag{10.1}
$$



What is not proved here is that a favorable inequality holds for all original indices, or that an unfavorable one holds on a specified infinite original subfamily. The actual high ternary digits and actual power-of-two low digits must both enter that claim.

The earlier endpoint-unit cylinder is not used to supply such a subfamily. Nor is an arbitrary low-digit construction an original-family counterexample.

### Concrete follow-on lemma

The next useful target is now:

> **Original-window Jacobi collision lemma.**  
> For the actual integers $m=2^{2j-1}$ in the retained window, determine the branch of
> 

$$
> r-\bigl(4+u\bigr).
>
$$


> On the collision branch, evaluate the pivot residual content in (9.3) at the threshold $h-33$, with the actual Christoffel scalar normalization certified on the same indices.

This is more direct than searching for a return annihilator. It targets precisely the quantity controlling the new $32$-digit transfer.

---

## 11. Directional and cofactor alternatives remain separate

Even a proof of $s_c<32$ would only protect the matrix comparison. It would not automatically protect the whole endpoint scalar.

Retain


$$
B_c=-S_c/3^{26},\qquad
\Theta=-S_{\rm act}/3^{26}.
$$


If the largest Smith exponent of $B_c$ is $a<6$, define


$$
u_{\rm end}
=\max\left(0,-\min_i v_3((B_c^{-1}e_c)_i)\right).
$$


The retained directional guard is


$$
\boxed{
v_3\!\left(e_c^TB_c^{-1}e_c-3^{26}d_c\right)
<6-2u_{\rm end}.
}
$$



Alternatively, retain the complete cofactor pair


$$
D_0=\det\Theta,
$$




$$
\boxed{
D_1=e_{\rm act}^T\operatorname{adj}(\Theta)e_{\rm act}
-3^{26}d_{\rm act}\det\Theta.
}
$$


The subtraction cannot be replaced by the first term.

Failure of $s_c<32$ would delimit this matrix-comparison method. It would not disprove an irrationality construction, and would not eliminate a directional or direct-cofactor argument.

---

## 12. Finite forcing, terminal return, and global normalization are unchanged

The Jacobi shortcut does not modify the complete finite forcing in A1 turn 2, equation (5.1): both leading extractions, every permitted lower pole, the factorial force, and the LOW subtraction remain part of the original system.

Likewise, the terminal equations remain


$$
\lambda_{i+\nu}
+\sum_{k=0}^{\nu-1}\bar f_k\lambda_{i+k}
=\bar b_i^{\langle26\rangle},
\qquad0\le i\le\nu-2,
$$


and


$$
J^T\varepsilon+\omega
=-\varepsilon-s\bigl(\theta e_{\nu-1}
+3^{26}b^{\langle26\rangle}\bigr).
$$


There is no added moment beyond $D-4$, and no deletion of $\omega_{\nu-1}$.

The support-only obstruction from the preceding report remains sharply scoped: it excludes bounded separate linear compression for arbitrary supported factors, not an actual return-specific or whole-functional compression.

All original row contents, the actual multiplier, and the least actual clearer remain unchanged. With


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


retain the all-prime gcd


$$
g_\ell=\gcd(|A_\ell|,|B_\ell|).
$$


When $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


When the determinant-pair members are nonzero,


$$
v_3(q)=
\max\left\{
0,\,
h-26+2v_3((n-1)!)
+v_3(D_1)-v_3(D_0)
\right\}.
$$



The same-index whole error is still


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{g_\ell}
\det H_{\rm complete}.
}
$$


No new estimate for its nonvanishing or decay has been proved here.

---

## 13. New bounded arithmetic interface

No previously accepted check needs to be rerun.

### A. Small-state original-input calculation

**Inputs**

A certified original tuple


$$
(j,h,H,D),\qquad m=2^{2j-1},
$$


satisfying the retained window, together with the actual ternary digits of $m$.

**Calculation**

Run the two eight-state minimum-cost digit programs for (6.2) and (7.1).

**Expected verifiable output**

- the original-index and window checks;
- exact integers
  

$$
r=\operatorname{cont}_3(J_m),\qquad
  u=\operatorname{cont}_3(J_{m-1});
$$


- a minimizing digit path for each value;
- the final state-cost tables;
- the branch comparison $r$ versus $4+u$.

These are exact expected types of output, not predictions of favorable values.

If the unit-normalization hypotheses are certified on that same tuple and $r\ne4+u$, this already gives the exact $s_c$ through (10.1).

### B. Collision-only content certificate

If $r=4+u$, supply the actual rational Christoffel scalar $a_m$, form $Z$ and


$$
T=XZ+\mathfrak a J_m,
$$


and use (9.3).

The required output is:

- the actual scalar valuations;
- the exact identity
  

$$
(3X-\eta)Z=(X-b_m-a_m)J_m-\rho J_{m-1};
$$


- a minimum-content pivot coefficient of $Z$;
- the pivot residual content, or its rigorous threshold comparison with $h-33$;
- the resulting exact inverse loss, or only a stated lower bound if precision is exhausted.

This second calculation is finite but not yet proved small in the original parameter. It is an **unevaluated specification**, not a completed original-family certificate.

---

## 14. Proof-status ledger and conclusion

| Statement | Status |
|---|---|
| Complete core equals pure-integral matrix plus an integral $3^h$ factorial matrix | Proved at the original finite cutoff |
| Factorial perturbation preserves inverse loss when the pure loss is $<h$ | Proved |
| Relative factorial depth is at least two under the retained unit-normalized kernel | Proved |
| Original monic basis is unimodular | Proved |
| Integral Schur correction is unimodular | Derived from the retained corrected-column integrality |
| Full loss equals $s_c$ on the depth-$26$ window | Proved when the core is nonsingular |
| Unit normalizers on every current-window index | Not established by the supplied resonant-family proof |
| Bernstein-type content formula for $J_m$ | Proved |
| Constant-state ternary evaluator for $J_m$ and $J_{m-1}$ contents | Proved |
| $\mathcal E$-content on the two noncollision branches | Proved under the stated scalar valuations |
| Whole $\mathcal E$-content as a two-column minor/pivot certificate | Proved |
| Small digit evaluator for collision-branch cancellation | Not yet established |
| Uniform $s_c<32$, or a proved original-subfamily exclusion | Not obtained |
| Whole scalar/cofactor protection and final primitive error decay | Unresolved |

### New result

The direct inverse route is now justified:


$$
\boxed{
G_c=G_J+3^hF_c,\qquad F_c\in M_{m+1}(\mathbb Z_3),
}
$$


and, under the retained unit normalization,


$$
\boxed{
s_c=h-2-\operatorname{cont}_3(\mathcal E).
}
$$



Moreover, the complete content is no longer only a formal bivariate object:


$$
\boxed{
\operatorname{cont}_3(\mathcal E)
=
\min_{i<k}v_3(t_i z_k-z_i t_k),
\qquad T=XZ+\mathfrak a J_m.
}
$$


Outside the explicitly identified collision branch, two small-state digit minima determine it exactly.

### Exact remaining bottleneck

The local bottleneck is the **same-index original-family normalization and content decision**, especially the collision


$$
\operatorname{cont}_3(J_m)
=
4+\operatorname{cont}_3(J_{m-1}),
$$


where the complete Christoffel cancellation must be evaluated.

Beyond that remain the directional whole scalar or complete cofactor pair, all row contents, the final all-prime gcd, the actual primitive denominator, and infinitely many same-index nonzero whole errors tending to zero.



$$
\boxed{\text{No unconditional proof or disproof of irrationality of }e+\pi
\text{ has been obtained.}}
$$


