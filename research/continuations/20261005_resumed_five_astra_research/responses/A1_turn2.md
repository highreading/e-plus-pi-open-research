> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The first actual residual digit: a structured-force reduction in the original polynomial lattice

## Executive conclusion

I do not use the provisional terminal inverse formula, reopen the moving-base logarithm argument, or impose a restricted-digit condition on $2^{2j-1}$.

The new result is a **uniform characterization of the actual residual block after division by $3^6$, modulo $3$**, on the original domain


$$
\boxed{
n=4^j+1,\qquad 81\mid j,\qquad
0<D=H-(n-2)<H/972,\qquad H=3^{h-1}.
}
$$



The characterization has two parts.

1. **The unspecified polynomial correction of order $3^6$ does not contribute to this particular transported digit.** This is not a consequence of entrywise matrix precision alone. It follows from the original endpoint-subtracted functional, the finite top-pole index, and the degrees of the actual integral residual columns.

2. **The remaining digit is an explicitly specified, finite-ring HIGH-return operator.** It can be assembled from beta moments, two integral triangular coefficient matrices, and Neumann polynomials of lengths four and five. Its inputs are $j,H,D$; it requires neither an unknown inverse nor the coefficients of the actual orthogonal polynomial.

Writing $\mathscr R_{\mathrm{act}}$ for the residual block in the **full scaled-matrix normalization**, the result is


$$
\boxed{
\frac{\mathscr R_{\mathrm{act}}}{3^6}
\equiv
-\frac{V\,\mathcal I_H\,V^T}{81}
\pmod3,
}
\tag{A}
$$


where $V$ and the explicit polynomial $\mathcal I_H$ are defined below, modulo $243$. The numerator on the right is divisible by $81$; the quotient is taken before reduction modulo $3$.

The actual transported endpoint is


$$
\boxed{
\overline e_{\mathrm{res}}
=\bigl((-1)^i\bigr)_{0\le i<\nu},
\qquad
\nu=D/2-1.
}
\tag{B}
$$



This gives a rigorous symbolic reduction of the requested block and endpoint. **I have not evaluated its rank uniformly or proved that it is nonzero.** Consequently, it gives no new unconditional value for the actual determinant ratio or primitive denominator.

There is also a useful further localization of the genuine polynomial force. At the next digit, its contribution is an explicit Hankel strip of the actual correction polynomial, derived in §7. Thus the nonunit branches and the actual force remain in the problem; they are not replaced by a core-only endpoint condition.

---

## 1. Exact domain, normalization, and complete functional

Put


$$
A=n-2=H-D,\qquad
m=\frac{A+1}{2},\qquad
k=m+1,
$$




$$
d=\frac{3D}{2}-1,\qquad
\nu=\frac D2-1,
$$


and


$$
r_1=\frac{H-1}{2},\qquad
r_*=\frac{3H-1}{2}.
$$



The original column indices remain


$$
0\le a\le m,
$$


with LOW indices $0,\ldots,d-1$ and HIGH indices $d,\ldots,m$.

Here $D$ is a positive multiple of $6$. In particular,


$$
D\ge6,\qquad \nu\ge2.
$$


Since $H>972D$, we have $H>5832$, hence


$$
\boxed{h\ge9.}
\tag{1.1}
$$


This elementary bound will justify, at stated precisions, the disappearance of factorial contributions—not their deletion from the defining functional.

### 1.1 The polynomial is the original paired-derangement polynomial

Let


$$
\rho(y^r)=D_{2r}-(-1)^r,
$$


where $D_s$ is the derangement sequence. The monic polynomial $P_n$ is the unique degree-$n$ polynomial satisfying


$$
\rho(y^aP_n)=0,\qquad 0\le a<n.
$$



Equivalently, with


$$
C_n=\bigl(\rho(y^{a+b})\bigr)_{0\le a,b<n},
\qquad
f_n=\bigl(\rho(y^{n+a})\bigr)_{0\le a<n},
$$


one has


$$
P_n(y)=y^n-\sum_{a=0}^{n-1}(C_n^{-1}f_n)_a y^a.
\tag{1.2}
$$


The nonsingularity used here is the established one for this specific signed moment functional.

Retain


$$
Q_n^{\mathrm{loc}}=3P_n,\qquad
Q_n=\lambda Q_n^{\mathrm{loc}},
\qquad
\lambda=L_n/3\in\mathbb Z_3^\times.
\tag{1.3}
$$



The accepted full-force congruence gives


$$
Q_n^{\mathrm{loc}}
=Q_c+3^6R,
\qquad R\in\mathbb Z_3[y],\qquad \deg R\le n,
\tag{1.4}
$$


where


$$
Q_c=(y+1)(y-1)^A(\beta+3y),
\qquad
\beta=-71-A.
\tag{1.5}
$$


If $v_3(j)>4$, the polynomial $R$ in (1.4) has the corresponding extra divisibility. No restriction to $v_3(j)=4$ is needed for the results below.

Thus $R$ is fixed by (1.2)–(1.5). It is not an arbitrary perturbation.

### 1.2 The complete rational functional

For every polynomial of the required degree, define


$$
C_F(y)=\frac{F(y)-F(-1)}{y+1},
$$


and


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
\sum_{r=0}^{h}
\ \sum_{\substack{c\ge1\ {\rm odd}\\3\nmid c\\c3^r\le4n-3}}
3^{h-r}c^{-1}
[y^{(c3^r-1)/2}]C_F,
\tag{1.6}
$$


where


$$
\mathfrak f(y^s)=(2s)!.
$$



The actual and reference matrices are


$$
G_{\mathrm{act}}
=\bigl(\mathcal M(Q_n^{\mathrm{loc}}y^{a+b})\bigr)_{0\le a,b\le m},
$$




$$
G_c
=\bigl(\mathcal M(Q_cy^{a+b})\bigr)_{0\le a,b\le m}.
\tag{1.7}
$$


In particular, $G_c$ here still includes its factorial term. It is not defined by a positive substitute metric.

Because


$$
4n-3<3^{h+1},
$$


all coefficients in (1.6) are $3$-integral. At the highest depth there is exactly one admissible pole, namely $3^h=3H$. Therefore


$$
\boxed{
\mathcal M(F)\equiv[y^{r_*}]C_F\pmod3.
}
\tag{1.8}
$$



Equation (1.8), with its exact finite index $r_*$, is the structural fact that improves the transported precision.

---

## 2. An integral polynomial/difference lattice

Use the LOW basis


$$
U_a(y)=(y-1)^a,\qquad 0\le a<D,
\tag{2.1}
$$


followed by the original radical lifts


$$
z_i(y)=y^i(y-1)^D,\qquad 0\le i<\nu.
\tag{2.2}
$$


Together these form an integral unit-triangular basis of the original LOW space: their successive leading degrees are


$$
0,\ldots,D-1,D,\ldots,d-1.
$$



The HIGH columns remain exactly


$$
Y_b(y)=y^b,\qquad d\le b\le m.
\tag{2.3}
$$



Thus this change of basis loses no $3$-adic coordinate precision. In particular, it is unlike a rational Jacobi orthogonalization whose denominators require separate analysis.

For either $G_{\mathrm{act}}$ or $G_c$, write


$$
G(U,U)=3L,\qquad
G(U,Y)=3X,\qquad
G(Z,Y)=3V,
\tag{2.4}
$$




$$
G(U,Z)=3B,\qquad G(Y,Y)=E.
$$


Here $Z$ denotes the list of polynomials (2.2). The retained block results give


$$
L\in\operatorname{GL}_D(\mathbb Z_3),
\qquad
\widehat E:=E-3X^TL^{-1}X
\in\operatorname{GL}_{m-d+1}(\mathbb Z_3).
\tag{2.5}
$$



Define


$$
C=L^{-1}B,\qquad
\widetilde V=V-B^TL^{-1}X.
$$


The exact corrected residual columns are


$$
\widehat Z
=
Z-UC
-
3\bigl(Y-UL^{-1}X\bigr)\widehat E^{-1}\widetilde V^T.
\tag{2.6}
$$


Their exact full-normalization residual form is


$$
\boxed{
\mathscr R
=
G(Z,Z)-3B^TL^{-1}B
-9\widetilde V\widehat E^{-1}\widetilde V^T.
}
\tag{2.7}
$$



All transformations in (2.6) and their inverses are integral over $\mathbb Z_3$. The only inverse loss in the combined eliminated block is the single factor $3^{-1}$ from the block $3L$.

---

## 3. Why the unknown $3^6$ polynomial force misses this residual digit

The earlier congruence-only precision obstruction remains valid: an arbitrary matrix perturbation in $3^6M_k(\mathbb Z_3)$ need not preserve an endpoint inverse contraction.

The present improvement uses information not present in that generic assertion.

### 3.1 A stable Schur perturbation lemma

Suppose an integral change of columns puts a reference matrix into the form


$$
\begin{pmatrix}
A_0&0\\
0&\mathscr R_0
\end{pmatrix},
$$


where


$$
A_0^{-1}\in3^{-1}M(\mathbb Z_3).
$$


Suppose the actual matrix differs by $3^P T$, with $T$ integral and $P\ge2$.

Then its residual Schur block satisfies


$$
\boxed{
\mathscr R_{\mathrm{act}}
=
\mathscr R_0
+
3^P T_{\mathrm{res,res}}
+
O(3^{2P-1}).
}
\tag{3.1}
$$



Indeed, the off-diagonal perturbation has a factor $3^P$ on each side of the inverse of the perturbed eliminated block. That inverse still belongs to $3^{-1}M(\mathbb Z_3)$, so the quadratic correction has valuation at least $2P-1$.

This lemma needs no inverse of the residual block and therefore applies on its singular branches.

### 3.2 Application to the actual polynomial force

From (1.4),


$$
G_{\mathrm{act}}-G_c
=
3^6\bigl(\mathcal M(Ry^{a+b})\bigr)_{a,b}.
\tag{3.2}
$$



The accepted eliminations give


$$
\widehat z_i^{\,c}\equiv z_i\pmod3.
$$


Consequently, by (1.8),


$$
\mathcal M(R\widehat z_i^{\,c}\widehat z_j^{\,c})
\equiv
[y^{r_*}]
\frac{Rz_iz_j-R(-1)z_i(-1)z_j(-1)}{y+1}
\pmod3.
\tag{3.3}
$$



But


$$
\deg z_i,\deg z_j\le d-1,
$$


so the polynomial on the right has degree at most


$$
n+2(d-1)-1
=A+2d-1
=H+2D-3
<r_*.
\tag{3.4}
$$


Its selected coefficient is therefore exactly zero.

Apply (3.1) with $P=6$. The quadratic perturbation is in $3^{11}$, while the linear term has gained one power of $3$ by (3.3)–(3.4). Hence


$$
\boxed{
\mathscr R_{\mathrm{act}}
\equiv\mathscr R_c\pmod{3^7}.
}
\tag{3.5}
$$



This proves that the actual $3^6$-divided residual digit is determined by the reference polynomial $Q_c$.

**What has been proved is specifically (3.5), not transfer of the full inverse or the full endpoint ratio.** The large inverse losses from the terminal analysis are not contradicted or bypassed by an unjustified Neumann expansion of the full matrix.

---

## 4. A stronger direct annihilation at the present domain

The smaller domain $D<H/972$ supplies one additional useful direct digit.

Define


$$
B_p(s)=\int_0^1x^{2s}(x^2-1)^p\,dx.
$$


Its exact rational value is


$$
B_p(s)
=
\frac{(-1)^p2^p p!}{\prod_{a=0}^{p}(2s+2a+1)}.
\tag{4.1}
$$



For $H=3^{h-1}$ and


$$
0\le s\le(H-3)/2,
$$


the accepted exact beta valuation gives


$$
v_3(B_H(s))=-v_3(2s+1).
\tag{4.2}
$$



For the pairings $Z$-$Z$ and $U$-$Z$, expansion of the remaining factor $(y-1)^D$, or of $U_a$, reduces the arctangent contribution to integral combinations of


$$
3^h\beta B_H(s),\qquad 3^{h+1}B_H(s+1),
$$


with the largest necessary shift at most $2D-3$. Therefore


$$
2s+1\le4D-5<H/243=3^{h-6},
$$


and


$$
v_3(2s+1)\le h-7.
$$


Thus these complete core pairings are divisible by $3^7$. Their factorial parts have valuation at least $h\ge9$.

For the actual correction $3^6R$, the top pole is absent in the same pairings by degree, giving the same divisibility.

We have proved


$$
\boxed{
G_{\mathrm{act}}(Z,Z),\ G_c(Z,Z)\in3^7M(\mathbb Z_3),
}
\tag{4.3}
$$




$$
\boxed{
G_{\mathrm{act}}(U,Z),\ G_c(U,Z)\in3^7M(\mathbb Z_3).
}
\tag{4.4}
$$


In the notation of §2,


$$
B,C\in3^6M(\mathbb Z_3).
$$



Substituting into (2.7) gives


$$
\boxed{
\mathscr R_c
\equiv-9V\widehat E^{-1}V^T\pmod{3^7},
}
\tag{4.5}
$$


and hence, using (3.5),


$$
\boxed{
\mathscr R_{\mathrm{act}}
\equiv-9V\widehat E^{-1}V^T\pmod{3^7}.
}
\tag{4.6}
$$



Here and below $L,X,V,E$ may be computed using $Q_c$. All omitted terms have now been assigned explicit depths.

The accepted fifth-carry theorem says that $\mathscr R_{\mathrm{act}}$ is divisible by $3^6$. Consequently,


$$
\boxed{
V\widehat E^{-1}V^T\in81M_\nu(\mathbb Z_3).
}
\tag{4.7}
$$



The remaining defect is therefore precisely the next digit of this **actual HIGH-return contraction**, not an unevaluated direct LOW force.

---

## 5. An explicit symbolic operator with no unresolved inverses

This section turns (4.6) into a finite-ring formula whose entries are completely specified.

All arrays below have their original finite sizes:


$$
L:\ D\times D,\quad
X:\ D\times(m-d+1),
$$




$$
V:\ \nu\times(m-d+1),\quad
E:\ (m-d+1)\times(m-d+1).
$$



### 5.1 Beta-moment entries

At the precisions needed here, the factorial contribution vanishes after the indicated divisions because $h\ge9$. Its omission in the following evaluation formulas is therefore justified by valuation.

In the basis (2.1)–(2.3),


$$
\boxed{
L_{ab}
\equiv
3^{h-1}
\left[
\beta B_{A+a+b}(0)
+3B_{A+a+b}(1)
\right]
\pmod{81},
}
\quad 0\le a,b<D,
\tag{5.1}
$$




$$
\boxed{
X_{ab}
\equiv
3^{h-1}
\left[
\beta B_{A+a}(b)
+3B_{A+a}(b+1)
\right]
\pmod{81},
}
\quad 0\le a<D,\ d\le b\le m,
\tag{5.2}
$$




$$
\boxed{
V_{ib}
\equiv
3^{h-1}
\left[
\beta B_H(i+b)
+3B_H(i+b+1)
\right]
\pmod{243},
}
\quad 0\le i<\nu,\ d\le b\le m,
\tag{5.3}
$$


and


$$
\boxed{
E_{ab}
\equiv
3^h
\left[
\beta B_A(a+b)
+3B_A(a+b+1)
\right]
\pmod{243},
}
\quad d\le a,b\le m.
\tag{5.4}
$$



These formulas evaluate all arctangent poles together. They do not select a favorable subset of pole units.

The apparent denominators in the beta expressions must be canceled against their displayed powers of $3$ before reduction. The resulting entries are integral. In (5.3), for example, the possible top-pole contribution is supplied by the term with the explicit extra factor $3$; it is not lost by treating both summands at the same unscaled precision.

### 5.2 An integral inverse representative for the LOW unit block

Define


$$
h_t=(-1)^t\binom{r_1+t}{t},\qquad t\ge0,
$$


and set


$$
(L_0)_{ab}=
\begin{cases}
h_{D-1-a-b},&a+b\le D-1,\\
0,&a+b>D-1.
\end{cases}
\tag{5.5}
$$



Then


$$
\boxed{L\equiv L_0\pmod3.}
\tag{5.6}
$$



To verify this, the lower residue form in the difference basis is


$$
[y^{r_1}](y-1)^{H-D+a+b}.
$$


If $a+b\ge D$, the identity


$$
(y-1)^H=y^H-1\quad\text{over }\mathbb F_3
$$


makes this coefficient zero. If


$$
t=D-1-a-b\ge0,
$$


then, through degrees below $H$,


$$
(y-1)^{H-1-t}
\equiv
(-1)^t(1-y)^{-t}\sum_{q=0}^{H-1}y^q.
$$


Its $y^{r_1}$-coefficient is exactly $h_t$.

The matrix $L_0$ is anti-triangular with anti-diagonal entries $1$. Its exact integral inverse is


$$
\boxed{
(R_L)_{ab}
=
[z^{a+b-D+1}](1+z)^{r_1+1},
}
\tag{5.7}
$$


where coefficients of negative degree are zero.

This follows from the reciprocal generating functions


$$
\sum_{t\ge0}h_tz^t=(1+z)^{-(r_1+1)}.
$$



Put


$$
T_L=L-L_0\in3M_D(\mathbb Z_3).
$$


The four-term polynomial


$$
\boxed{
\mathcal I_L
=
\sum_{\ell=0}^{3}(-R_LT_L)^\ell R_L
}
\tag{5.8}
$$


satisfies


$$
\mathcal I_L\equiv L^{-1}\pmod{81}.
\tag{5.9}
$$



There is no unresolved LOW inverse in (5.8).

### 5.3 The HIGH inverse representative and its five-term lift

Define


$$
(E_0)_{ab}
=[y^{r_*}](y-1)^Ay^{a+b},
\qquad d\le a,b\le m.
\tag{5.10}
$$


It is the retained integral anti-triangular top-pole matrix. Its exact inverse is


$$
\boxed{
(R_H)_{ab}
=
[z^{d+m-a-b}](1-z)^{-A}.
}
\tag{5.11}
$$



This is the elementary finite triangular-coefficient inverse, not the provisional terminal Jacobi inverse.

Compute, modulo $243$,


$$
\widehat E_*
=
E-3X^T\mathcal I_LX.
\tag{5.12}
$$


Then


$$
\widehat E_*\equiv\widehat E\pmod{243},
\qquad
\widehat E_*\equiv E_0\pmod3.
$$


Define


$$
F_*=\frac{\widehat E_*-E_0}{3}\pmod{81}.
\tag{5.13}
$$



Now set


$$
\boxed{
\mathcal I_H
=
\sum_{\ell=0}^{4}
(-3R_HF_*)^\ell R_H
\pmod{243}.
}
\tag{5.14}
$$


Thus


$$
\mathcal I_H\equiv\widehat E^{-1}\pmod{243}.
\tag{5.15}
$$



The inverse word length is uniformly five, independently of $j,H,D$.

### 5.4 The requested residual matrix

Define


$$
N_*=V\mathcal I_HV^T\pmod{243}.
\tag{5.16}
$$


By (4.7), every entry is $0$ modulo $81$. Therefore the following is well-defined:


$$
\boxed{
\mathcal D_6
:=
-\frac{N_*}{81}\pmod3.
}
\tag{5.17}
$$



Combining the preceding sections proves


$$
\boxed{
\mathscr R_{\mathrm{act}}=3^6\mathcal T,
\qquad
\mathcal T\bmod3=\mathcal D_6.
}
\tag{5.18}
$$



Equations (5.1)–(5.17) are a complete symbolic characterization of the requested matrix. They contain:

- no unknown correction polynomial;
- no discarded factorial term without a depth bound;
- no missing endpoint subtraction;
- no unresolved matrix inverse;
- no enlarged or infinite HIGH matrix;
- no unit-branch hypothesis about a Jacobi endpoint.

The potentially surviving digit is the complete five-term HIGH return


$$
-\frac1{81}
V\left(
R_H-3R_HF_*R_H
+9R_HF_*R_HF_*R_H
-27R_HF_*R_HF_*R_HF_*R_H
+81R_HF_*R_HF_*R_HF_*R_HF_*R_H
\right)V^T
\pmod3.
\tag{5.19}
$$



**The carries in the first four summands must be retained.** The fifth summand alone is not the defect. Nor has any summand in (5.19) been proved nonzero here.

---

## 6. Uniform bounded arithmetic for the symbolic entries

The beta moments in §5 do not require constructing factorials of size comparable to $n$.

From (4.1),


$$
\boxed{
B_p(s)=
(-1)^p2^{2p+1}
\frac{p!\,(s+p+1)!\,(2s)!}
{(2s+2p+2)!\,s!}.
}
\tag{6.1}
$$



For fixed modulus $3^5=243$, define


$$
U_5(N)=\frac{N!}{3^{v_3(N!)}}\pmod{243},
$$


and


$$
P_5(r)=\prod_{\substack{1\le a\le r\\3\nmid a}}a\pmod{243},
\qquad 0\le r<243.
$$



The exact recursion is


$$
\boxed{
U_5(N)
=
(-1)^{\lfloor N/243\rfloor}
P_5(N\bmod243)\,
U_5(\lfloor N/3\rfloor)
\pmod{243}.
}
\tag{6.2}
$$


The sign comes from the product of all units modulo $243$, which is $-1$.

The valuation is separately computed by


$$
v_3(N!)=\sum_{\ell\ge1}\left\lfloor\frac N{3^\ell}\right\rfloor.
\tag{6.3}
$$



Thus each scaled beta entry is evaluated by:

1. its exact integer valuation from (6.3);
2. factorial units from the fixed table of $243$ residues and recursion (6.2);
3. unit inversion modulo $243$;
4. restoration of its remaining power of $3$.

The same procedure evaluates the binomial coefficients in (5.5), (5.7), and (5.11).

This is a fixed-modulus digit recursion with explicit valuation counters. I do **not** claim that the entire growing matrix has a fixed number of states. Rather, the result is a uniform bounded symbolic reduction:

- fixed arithmetic modulus $243$;
- a fixed table of $243$ entries;
- four LOW inverse terms;
- five HIGH inverse terms;
- exactly the original finite index ranges.

A direct implementation uses a number of modular operations bounded in terms of the displayed matrix dimensions, for example $O(k^3+k^2\log n)$ with ordinary matrix multiplication. That bound may be impractical at original indices; its purpose is to specify a complete finite procedure and a route to a more compressed support analysis, not to represent an enormous scan as a completed computation.

---

## 7. The genuine polynomial force reappears in a precise next-digit Hankel strip

The disappearance of $R$ from $\mathcal D_6$ is only a one-digit statement.

There is a useful exact description of its next contribution.

Let $\mathscr R_{\mathrm{act}}$ and $\mathscr R_c$ be the Schur blocks in the same raw $Z$-coordinate labels. Then


$$
\boxed{
\frac{\mathscr R_{\mathrm{act}}-\mathscr R_c}{3^7}
\equiv \mathcal F_R\pmod3,
}
\tag{7.1}
$$


where


$$
\boxed{
(\mathcal F_R)_{ij}
=
[y^{r_1}]
\frac{Rz_iz_j-R(-1)z_i(-1)z_j(-1)}{y+1},
\qquad 0\le i,j<\nu.
}
\tag{7.2}
$$



### Proof of the extra precision

Modulo $9$, the core residual columns have the form


$$
\widehat z_i^{\,c}=z_i+3w_i,
$$


where


$$
w_i\equiv
2\delta_{i,\nu-1}
\left(y^d-UL^{-1}X_{\cdot,d}\right)
\pmod3.
\tag{7.3}
$$


Indeed, use


$$
V\equiv-2e_{\nu-1}e_m^T\pmod3,
\qquad
R_He_m=e_d,
$$


in (2.6), while $C\in3^6M(\mathbb Z_3)$.

Every $w_i$ in (7.3) has degree at most $d$. Consequently the top-pole coefficient of


$$
C_{Rz_iw_j}
$$


is still zero by degree. In the linear Schur perturbation, the first surviving coefficient is therefore the pole at $r_1$, whose weight in $\mathcal M$ is $3$. All lower layers are multiples of $9$, and the quadratic perturbation remains in $3^{11}$. This proves (7.1)–(7.2). ∎

There is an equivalent Hankel-strip description. Set


$$
W_R(y)=
\frac{R(y)(y-1)^{2D}-R(-1)(-2)^{2D}}{y+1}.
\tag{7.4}
$$


Since $i+j\le D-4<r_1$, multiplication by $y^{i+j}$ introduces no additional endpoint-division term at degree $r_1$. Hence


$$
\boxed{
(\mathcal F_R)_{ij}
=[y^{r_1-i-j}]W_R(y).
}
\tag{7.5}
$$



Only the coefficient strip


$$
r_1-(D-4),\ldots,r_1
$$


is needed for this first genuine polynomial-force contribution.

This is a concrete follow-on obligation on a singular branch of $\mathcal D_6$: evaluate this strip for the **actual**


$$
R=\frac{3P_n-Q_c}{729},
$$


with $P_n$ defined by the original derangement constraints (1.2). It is not permissible to substitute a rank-one perturbation or a generic polynomial with the same content.

---

## 8. Endpoint transport and its coupling to the defect

Let


$$
u_a=U_a(-1)=(-2)^a,
\qquad
v_b=Y_b(-1)=(-1)^b,
$$


and


$$
z_i(-1)=(-1)^i(-2)^D.
$$



Evaluation of the entire corrected column formula (2.6) gives


$$
\boxed{
e_{\mathrm{res}}
=
z(-1)-B^TL^{-1}u
-
3\widetilde V\widehat E^{-1}
\bigl(v-X^TL^{-1}u\bigr).
}
\tag{8.1}
$$


This is the actual endpoint vector, not an endpoint assigned to uncorrected columns.

Since $B\in3^6M(\mathbb Z_3)$,


$$
\boxed{
e_{\mathrm{res}}\equiv
\bigl((-1)^i\bigr)_{0\le i<\nu}\pmod3.
}
\tag{8.2}
$$



Factoring $3^6$ out of the residual **form** does not divide the endpoint vector by $3^6$. The endpoint remains the covector (8.1).

The first finite coupling tests are therefore


$$
\operatorname{rank}_{\mathbb F_3}\mathcal D_6,
\qquad
\overline e_{\mathrm{res}}\in\operatorname{im}\mathcal D_6,
\tag{8.3}
$$


and, on the invertible branch,


$$
\boxed{
\kappa_0
=
\overline e_{\mathrm{res}}^{\,T}
\mathcal D_6^{-1}
\overline e_{\mathrm{res}}
\in\mathbb F_3.
}
\tag{8.4}
$$



These distinguish three genuinely different situations:

1. $\mathcal D_6$ invertible and $\kappa_0\ne0$;
2. $\mathcal D_6$ invertible but $\kappa_0=0$;
3. $\mathcal D_6$ singular, requiring its radical and the endpoint component there.

A nonzero endpoint vector alone does not exclude the second situation. A finite-field symmetric form can have nonzero isotropic vectors.

No one of these branches has been uniformly selected by the present proof.

---

## 9. Exact consequences for the determinant ratio and primitive denominator

The normalization can now be obtained directly from the original paired construction.

Let $R_{\mathrm{rat}}$ denote its complete rational matrix, using the primitive polynomial $Q_n$. Then


$$
R_{\mathrm{rat}}=\frac{4\lambda}{3^h}G_{\mathrm{act}}.
\tag{9.1}
$$


The complete moment matrix is


$$
H_{\mathrm{complete}}
=
R_{\mathrm{rat}}
+(e+\pi)Q_n(-1)vv^T.
\tag{9.2}
$$



Thus, without any nonsingularity assumption,


$$
\beta_0=\det R_{\mathrm{rat}},
\qquad
\beta_1=Q_n(-1)\,v^T\operatorname{adj}(R_{\mathrm{rat}})v.
\tag{9.3}
$$



When $G_{\mathrm{act}}$ is nonsingular,


$$
\boxed{
\frac{\beta_1}{\beta_0}
=
\frac{3^hQ_n(-1)}{4\lambda}
\,v^TG_{\mathrm{act}}^{-1}v
=
\frac{3^hQ_n^{\mathrm{loc}}(-1)}4
\,v^TG_{\mathrm{act}}^{-1}v.
}
\tag{9.4}
$$


The cancellation of $\lambda$ here is an exact consequence of its occurrences in both the polynomial response and rational matrix. It is not permission to omit it from either matrix or the global coefficient pair.

### 9.1 A precise conditional denominator consequence

Under the exact block diagonalization,


$$
G_{\mathrm{act}}
\sim
\operatorname{diag}(3L,\widehat E,3^6\mathcal T),
\qquad
\mathcal T\bmod3=\mathcal D_6.
$$


Therefore


$$
v^TG_{\mathrm{act}}^{-1}v
=
K_{\mathrm{elim}}
+
3^{-6}e_{\mathrm{res}}^T\mathcal T^{-1}e_{\mathrm{res}},
\tag{9.5}
$$


where


$$
K_{\mathrm{elim}}\in3^{-1}\mathbb Z_3.
$$



If


$$
\det\mathcal D_6\ne0,
\qquad
\kappa_0\ne0,
\tag{9.6}
$$


then


$$
v_3(\det G_{\mathrm{act}})=D+6\nu,
$$




$$
\boxed{
v_3\!\left(v^TG_{\mathrm{act}}^{-1}v\right)=-6.
}
\tag{9.7}
$$


In particular, both the actual rational determinant and its endpoint response are nonzero on this branch.

Using the retained endpoint law


$$
v_3(Q_n(-1))
=
v_3(Q_n^{\mathrm{loc}}(-1))
=
2v_3((n-1)!),
$$


equation (9.4) yields the conditional exact law


$$
\boxed{
v_3(q)
=
\max\left\{
0,\,
h+2v_3((n-1)!)-6
\right\}.
}
\tag{9.8}
$$



This is a consequence **if and only insofar as** the sufficient branch conditions (9.6) are established. They have not been established here.

If $\mathcal D_6$ is singular, or if $\kappa_0=0$, no exact denominator depth follows from (5.18) alone. In particular, lower Smith bounds still cannot be subtracted to evaluate $v_3(q)$.

### 9.2 What is unconditional at present

The new result does not improve the accepted gcd lower bound without a rank or endpoint-contraction evaluation. The established bound


$$
v_3(g)\ge d+5\nu
$$


therefore remains the available lower bound at that interface.

For the actual cleared pair retain


$$
A_\ell=\ell^k\beta_0,\qquad
B_\ell=\ell^k\beta_1,
$$




$$
g_\ell=\gcd(|A_\ell|,|B_\ell|).
$$


When $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},
\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


The whole evaluated error remains exactly


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell^k}{g_\ell}
\det H_{\mathrm{complete}}.
}
\tag{9.9}
$$



No result above controls the full all-prime gcd, proves nonvanishing of (9.9), or proves its decay.

---

## 10. Bounded exact checks and the remaining research calculation

No tools have been executed. No original-index rank calculation is claimed.

### 10.1 Small implementation certificate

The symbolic proof does not depend on a finite receipt. A bounded certificate useful for checking an implementation of §5 would have the following inputs and outputs.

**Inputs**

- modulus $243$;
- the table $P_5(r)$, $0\le r<243$;
- beta parameters $0\le p,s\le40$;
- LOW inverse tests $1\le D\le8$, $20\le r_1\le28$;
- HIGH inverse tests $1\le A\le12$, $0\le d\le4$, $d\le m\le d+8$, with the test index $r_*=A+d+m$.

**Expected verifiable output**

1. Recursion (6.2) agrees with direct factorial-unit extraction on the required bounded arguments.
2. Formula (6.1) agrees exactly with the product formula (4.1).
3. The scaled residues of the beta moments agree modulo $243$.
4. The matrices (5.5) and (5.7) multiply to the identity over the integers.
5. The finite matrices (5.10) and (5.11) multiply to the identity over the integers.
6. The four- and five-term Neumann polynomials have inverse remainders divisible by $81$ and $243$, respectively.

These tests involve only small matrices and bounded factorials. They verify algebra and implementation, not rank behavior on the original infinite family.

### 10.2 The actual next research calculation

The substantive remaining calculation is now sharply specified:

> Evaluate the finite-ring operator $\mathcal D_6$ of (5.17), uniformly on the original family, and determine its radical and coupling to the endpoint (8.2).

The present reduction removes the unspecified $3^6$ polynomial digit from that task. It leaves a concrete beta-moment return operator with controlled integral coordinates.

If that operator is singular, the next actual-force calculation must retain the strip $\mathcal F_R$ in (7.5), together with the next core return digit and the transported endpoint. The formula for $R$ must come from (1.2), not from an independently chosen perturbation.

---

## 11. Closing ledger

### New result and proof status

**Proved, using the accepted full-force congruence and fifth-carry theorem at their stated scopes:**

1. The actual residual block and the complete reference-core residual block agree modulo $3^7$:
   

$$
\mathscr R_{\mathrm{act}}\equiv\mathscr R_c\pmod{3^7}.
$$


2. The actual direct $Z$-$Z$ and $U$-$Z$ pairings are divisible by $3^7$ on $D<H/972$.
3. The first $3^6$-divided actual residual is the explicit finite-ring operator (5.17).
4. Its endpoint is the nonzero vector $\bigl((-1)^i\bigr)$ modulo $3$.
5. The genuine polynomial correction first contributes at the next digit through the actual Hankel strip (7.5).
6. The determinant-ratio normalization (9.4) follows directly from the paired-derangement construction.
7. The exact denominator formula (9.8) is a **conditional deduction**, requiring the explicitly stated invertibility and nonisotropy conditions.

**Not proved:** a uniform rank, a nonzero entry of $\mathcal D_6$, a uniform endpoint-image result for it, or a new unconditional primitive-denominator depth.

### Exact remaining mathematical bottleneck

The immediate bottleneck is no longer an unspecified matrix perturbation of order $3^6$. It is the rank and endpoint behavior of the explicitly specified operator


$$
-\frac{V\mathcal I_HV^T}{81}\pmod3.
$$


On its nonunit branches, the actual next polynomial force is the strip (7.5), fixed by the original derangement orthogonality equations.

No restricted-digit infinitude assertion has been introduced.

### Overall research status

This is an unconditional **actual-force reduction**, not an irrationality proof. The required global mechanism still needs same-index control of the final primitive denominator and nonzero whole errors tending to zero:


$$
0<|q(e+\pi)-p|\longrightarrow0.
$$





$$
\boxed{\text{The rationality or irrationality of }e+\pi\text{ remains unresolved.}}
$$


