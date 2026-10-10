> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Rational-gauge obstruction and paid actual-contact projections

## Abstract

The rationality or irrationality of $e+\pi$ remains unresolved.

This report closes the unrestricted rational-gauge question posed in the assignment. For the actual matrices $\mathsf U_n,\mathsf R_n$ and the complete forcing row $\gamma_n$, the equation


$$
\ell(n+1)(\mathsf U_n\otimes\mathsf R_n)+(n+1)^2\ell(n)=\gamma_n
$$


has **no solution in $\mathbb Q(n)^6$**.

The proof is not another bounded-degree guess. It correctly homogenizes the inhomogeneous equation, proves invertibility, applies the forward/backward pole-propagation method underlying rational shift-system denominator bounds, and obtains a universal denominator


$$
(n+1)^2(n+2).
$$


A rational change of coordinates then supplies a sufficient degree bound. Four explicitly calculated Laurent coefficients contradict the necessary partial-fraction form. Thus no additional parent calculation is needed to decide this rational-gauge class.

Using the recovered **actual** contact rows, the report also derives explicit integral contact directions


$$
W_3=(X,Z,Y-X-(2n+1)Z)^T
$$


and an explicitly evaluated $W_0$. These give paid contact projections and a source-specific identity


$$
\varepsilon_j\kappa_j W_{j,3}g_{\rm aff}T_{\rm aff}
-C h_j\widehat R_j
=
\varepsilon_j\kappa_j F\,\widehat{\mathcal B}_j.
$$


Here every content factor is retained, and


$$
\widehat{\mathcal B}_j
=
W_{j,3}\bigl(2L_n(n!)^2-\mathscr K_n^\circ\bigr)
-C\bigl(W_{j,1}\widehat\ell-W_{j,2}\widehat h\bigr)
$$


is an evaluated expression involving the complete seeded transverse response.

In particular,


$$
\gcd(|T_{\rm aff}|,D_j)_{>n+2}
\mid
\gcd\!\left(
D_j,\left|\frac{F}{g_{\rm aff}}\widehat{\mathcal B}_j\right|
\right)_{>n+2}.
$$


This restriction retains the branch $p\nmid F$; it does not use $F$ as an extra vanishing generator.

The new contact identity is not a subfactorial gcd theorem. The remaining bottlenecks are the actual seeded large-prime correlation in these evaluated contact projections, alignment acquisition with moving thresholds, and a nonzero whole-error estimate using the actual all-prime primitive denominator at the same infinite original indices.

---

## 1. Scope, domain, and status of the supplied evidence

The approximation domain remains exactly


$$
\boxed{n=15^r\quad\text{or}\quad n=105^r,\qquad r\ge2.}
$$


Consecutive integers used in rational-function identities and recurrence arguments are auxiliary indices. They do not enlarge the approximation domain.

Write


$$
m=n+1,\qquad N=n+2,\qquad L_n=2^{(n+1)/2}
$$


at original indices. No integral meaning is assigned here to $L_n$ at even auxiliary indices.

The supplied finite certificate establishes:

* the stated $42$-unknown class, with denominator $n(n+1)(n+2)$ and numerator degree at most $6$, is inconsistent;
* the $21$ stated auxiliary recurrence comparisons passed.

Those finite statements are accepted at exactly that scope. They are not used as an unrestricted nonexistence theorem, and neither calculation is repeated below.

The existing denominator-bound method is the shift-system method of Mark van Hoeij, Moulay Barkatou, and Johannes Middeke, *A Family of Denominator Bounds for First Order Linear Recurrence Systems*, arXiv:2007.02926. Its relevant setting is a shift automorphism of $\mathbb Q[n]$ and an invertible matrix over $\mathbb Q(n)$. Sections 3–5 verify those hypotheses and explicitly evaluate the required bounds for the present system.

The recovered finite producer and contact construction are reused, not claimed as new. The new results are:

1. unrestricted nonexistence of the specified rational system gauge;
2. explicit actual-contact directions in moment coordinates;
3. a paid, source-specific contact identity and its large-prime support consequence.

---

## 2. The actual seeded system

Let


$$
q(z)=1-z+\frac{z^2}{2},\qquad
a_k(n)=k![z^k]e^zq(z)^n.
$$


Retain


$$
X=ma_n,\qquad Y=mn\,a_{n-1},\qquad Z=2a_{n+1}-ma_n,
$$




$$
P=nX+Y,\qquad Q=nZ+2X-Y,
$$




$$
F=2m\bigl(Y-2X-(n-1)Z\bigr)=2m(Z-Q).
$$



The moment state $z_n=(P_n,Q_n,F_n)^T$ satisfies


$$
z_{n+1}=\mathsf U_nz_n,
$$


where


$$
\mathsf U_n=
\begin{pmatrix}
0&mN&N/2\\
N&-(n^2+3n+1)&-\dfrac{nN}{2m}\\
-N(2n+3)&N(n^2+3n+1)&\dfrac{N(n^2-2)}{2m}
\end{pmatrix}.
$$


Its genuine seed is


$$
z_2=(0,10,-66)^T.
$$



The reference pair satisfies


$$
y_{n+1}=\mathsf R_ny_n,\qquad
y_n=(\tau_n,\tau_{n+1})^T,
$$


with


$$
\mathsf R_n=
\begin{pmatrix}
0&1\\
m/N&(2n+3)/N
\end{pmatrix},
\qquad
y_2=(2,4)^T.
$$



Order the six tensor coordinates as


$$
\mathbf Y_n=
(P_n\tau_n,P_n\tau_{n+1},
 Q_n\tau_n,Q_n\tau_{n+1},
 F_n\tau_n,F_n\tau_{n+1})^T.
$$


Then


$$
\mathbf Y_{n+1}=\mathsf A_n\mathbf Y_n,
\qquad
\mathsf A_n=\mathsf U_n\otimes\mathsf R_n.
$$



The retained complete transverse recurrence is


$$
\mathcal K_{n+1}=-m^2\mathcal K_n+\gamma_n\mathbf Y_n,
\qquad \mathcal K_2=14,
$$


where


$$
\gamma_n=
\left(
0,\frac N2,
-\frac{m^2}{2},\frac{m^2+1}{2},
-\frac m4,\frac{n^2+3n+3}{4m}
\right).
$$


At original indices,


$$
\mathscr K_n^\circ=L_n\mathcal K_n.
$$



The question settled below is precisely whether


$$
\boxed{\ell(n+1)\mathsf A_n+m^2\ell(n)=\gamma_n}
\tag{2.1}
$$


has a rational row solution.

---

# Part I. Complete rational-gauge decision

## 3. Correct homogenization and invertibility

Put $h(n)=\ell(n)^T$. Equation (2.1) is equivalent to


$$
h(n+1)=-m^2\mathsf A_n^{-T}h(n)
+\mathsf A_n^{-T}\gamma_n^T.
$$


Thus the correct homogeneous system is


$$
\binom{h(n+1)}{1}
=
\mathsf M_n\binom{h(n)}{1},
$$


with


$$
\boxed{
\mathsf M_n=
\begin{pmatrix}
-m^2\mathsf A_n^{-T}&\mathsf A_n^{-T}\gamma_n^T\\
0&1
\end{pmatrix}.
}
\tag{3.1}
$$



The last coordinate is $1$, not $0$. Omitting this coordinate or homogenizing only the six homogeneous coefficients would lose the actual forcing.

### 3.1 Explicit inverses

For brevity set


$$
h_0=n^2+3n+1,\qquad t=2n+3,\qquad k=n+3.
$$


Direct elimination gives


$$
\boxed{
\mathsf U_n^{-1}=
\begin{pmatrix}
\dfrac{2h_0}{mNk}&\dfrac3k&\dfrac1{Nk}\\[2mm]
\dfrac N{mk}&\dfrac t{mk}&\dfrac1{mk}\\[2mm]
-\dfrac{2h_0}{Nk}&-\dfrac{2t}{k}&-\dfrac2k
\end{pmatrix},
}
\tag{3.2}
$$


and


$$
\boxed{
\mathsf R_n^{-1}=
\begin{pmatrix}
-t/m&N/m\\
1&0
\end{pmatrix}.
}
\tag{3.3}
$$



For example, adding $t$ times the second row of $\mathsf U_n$ to its third row gives


$$
(0,-mh_0,-N^2/2),
$$


from which


$$
\det\mathsf U_n=\frac{mN^2k}{2}.
$$


Also


$$
\det\mathsf R_n=-\frac mN.
$$


Consequently


$$
\det\mathsf A_n
=(\det\mathsf U_n)^2(\det\mathsf R_n)^3
=-\frac{m^5Nk^2}{4},
$$


and


$$
\boxed{
\det\mathsf M_n=-\frac{4m^7}{Nk^2}\ne0
\quad\text{in }\mathbb Q(n).
}
\tag{3.4}
$$



This verifies the invertibility hypothesis required by the rational shift-system denominator method.

### 3.2 The homogenized forcing simplifies substantially

Multiplication using (3.2)–(3.3) yields


$$
\boxed{
\gamma_n\mathsf A_n^{-1}
=
\left(\frac tN,-\frac12,\frac12,0,0,0\right).
}
\tag{3.5}
$$


This cancellation is important for the denominator bound: the forcing in the forward homogenized system has no pole at $n=-1$.

The inverse homogenized matrix is


$$
\boxed{
\mathsf M_n^{-1}=
\begin{pmatrix}
-\mathsf A_n^T/m^2&\gamma_n^T/m^2\\
0&1
\end{pmatrix}.
}
\tag{3.6}
$$



The following denominator bounds are therefore valid:


$$
\operatorname{den}(\mathsf M_n)\mid(n+2)(n+3),
\tag{3.7}
$$




$$
\operatorname{den}(\mathsf M_n^{-1})
\mid(n+1)^3(n+2).
\tag{3.8}
$$


Only rational-number coefficient denominators are suppressed in this polynomial divisibility notation.

---

## 4. A universal denominator bound

This section explicitly specializes the forward/backward pole-propagation method for invertible rational shift systems. It is not a new general denominator algorithm.

### Proposition 4.1

Every rational solution of (2.1) has component denominators dividing


$$
\boxed{D_*(n)=(n+1)^2(n+2).}
\tag{4.1}
$$



### Proof

Let


$$
w(n)=\binom{h(n)}1.
$$


Consider its finite poles over an algebraic closure of $\mathbb Q$, grouped into orbits under translation by integers.

Suppose an orbit contains poles of $w$, and let $\alpha$ be the first pole in that orbit. Then $w$ is regular at $\alpha-1$. From


$$
w(n+1)=\mathsf M_nw(n),
$$


$\mathsf M_n$ must have a pole at $n=\alpha-1$. By (3.7),


$$
\alpha\in\{-2,-1\}.
$$



Similarly, let $\beta$ be the last pole in its orbit. The inverse equation


$$
w(n)=\mathsf M_n^{-1}w(n+1)
$$


shows that $\mathsf M_n^{-1}$ must have a pole at $n=\beta$. By (3.8),


$$
\beta\in\{-2,-1\}.
$$



Hence the only possible finite poles of $w$ are $-2$ and $-1$.

At $-2$, the preceding value $w(-3)$ is regular, while $\mathsf M_n$ has at most a simple pole at $-3$. Thus the pole order at $-2$ is at most $1$.

At $-1$, the preceding value has pole order at most $1$, and $\mathsf M_n$ has at most a simple pole at $-2$. Thus the pole order at $-1$ is at most $2$.

This proves (4.1). ∎

This bound is genuinely universal for the rational equation. It contains a possible double pole at $n=-1$, which the previously rejected denominator $n(n+1)(n+2)$ did not permit. Therefore the old finite inconsistency certificate alone did not settle this question.

---

## 5. A sufficient degree bound at infinity

Define


$$
S_n=\operatorname{diag}(1,1,m),
\qquad
\widetilde\ell(n)=\ell(n)(S_n\otimes I_2).
$$


Then (2.1) becomes


$$
\widetilde\ell(n+1)(B_n\otimes\mathsf R_n)
+m^2\widetilde\ell(n)
=\widetilde\gamma_n,
\tag{5.1}
$$


where


$$
B_n=S_{n+1}^{-1}\mathsf U_nS_n
=
\begin{pmatrix}
0&mN&mN/2\\
N&-h_0&-nN/2\\
-t&h_0&(n^2-2)/2
\end{pmatrix}.
$$



Using $m=n+1$, write


$$
B_n=m^2B_2+mB_1+B_0,
$$


with


$$
B_2=
\begin{pmatrix}
0&1&1/2\\
0&-1&-1/2\\
0&1&1/2
\end{pmatrix},
$$




$$
B_1=
\begin{pmatrix}
0&1&1/2\\
1&-1&0\\
-2&1&-1
\end{pmatrix},
\qquad
B_0=
\begin{pmatrix}
0&0&0\\
1&1&1/2\\
-1&-1&-1/2
\end{pmatrix}.
\tag{5.2}
$$



Also


$$
\mathsf R_n=R_\infty+\frac{J}{m+1},
\qquad
R_\infty=
\begin{pmatrix}0&1\\1&2\end{pmatrix},
\quad
J=
\begin{pmatrix}0&0\\-1&-1\end{pmatrix}.
\tag{5.3}
$$



The matrix $B_2$ has rank one:


$$
B_2=uv^T,\qquad
u=(1,-1,1)^T,\quad v=(0,1,1/2)^T,
$$


and


$$
v^Tu=-\frac12.
$$


Therefore


$$
\det(I_6+B_2\otimes R_\infty)
=\det(I_2-R_\infty/2)
=-\frac14\ne0.
\tag{5.4}
$$



### Proposition 5.1

Every rational solution of (2.1) satisfies


$$
\widetilde\ell(n)=O(1)\qquad(n\to\infty).
\tag{5.5}
$$



### Proof

Let $d$ be the largest degree at infinity among the components of $\widetilde\ell$. If $d>0$, the leading term on the left side of (5.1) has degree $d+2$. Its coefficient is a nonzero row multiplied by


$$
I_6+B_2\otimes R_\infty,
$$


so it cannot vanish by (5.4).

But the right side has degree $2$. This is impossible. Hence $d\le0$. ∎

Together with Proposition 4.1, this gives a complete polynomial search bound:


$$
\ell_i(n)=\frac{A_i(n)}{(n+1)^2(n+2)},
$$


where


$$
\deg A_i\le3\quad(1\le i\le4),
\qquad
\deg A_i\le2\quad(i=5,6).
\tag{5.6}
$$


Thus, if a linear-system decision were desired, a universal class of only


$$
4\cdot4+2\cdot3=22
$$


rational coefficients would suffice. No unsupported degree guess remains.

The next section decides this class without requiring that computation.

---

## 6. An explicit Laurent obstruction

Represent the transformed row $\widetilde\ell$ as a $3\times2$ matrix $G(m)$, preserving the tensor order:


$$
G(m)=
\begin{pmatrix}
\widetilde\ell_1&\widetilde\ell_2\\
\widetilde\ell_3&\widetilde\ell_4\\
\widetilde\ell_5&\widetilde\ell_6
\end{pmatrix}.
$$


Equation (5.1) is exactly


$$
m^2G(m)+B(m)^TG(m+1)R(m)=\Gamma(m),
\tag{6.1}
$$


where


$$
\Gamma(m)=m^2\Gamma_2+m\Gamma_1+\Gamma_0
$$


and


$$
\Gamma_2=
\begin{pmatrix}
0&0\\
-1/2&1/2\\
-1/4&1/4
\end{pmatrix},
\quad
\Gamma_1=
\begin{pmatrix}
0&1/2\\
0&0\\
0&1/4
\end{pmatrix},
\quad
\Gamma_0=
\begin{pmatrix}
0&1/2\\
0&1/2\\
0&1/4
\end{pmatrix}.
\tag{6.2}
$$



By Proposition 5.1,


$$
G(m)=G_0+\frac{G_1}{m}+\frac{G_2}{m^2}
+\frac{G_3}{m^3}+O(m^{-4}).
\tag{6.3}
$$



### 6.1 The coefficient operator is invertible

Define


$$
\mathcal L(G)=G+B_2^TGR_\infty.
$$


If $K$ has rows $k_P,k_Q,k_F$, set


$$
d=k_P-k_Q+k_F=(d_1,d_2).
$$


Then the solution of $\mathcal L(G)=K$ has rows


$$
\begin{aligned}
g_P&=k_P,\\
g_Q&=k_Q+(2d_1+4d_2,\;4d_1+10d_2),\\
g_F&=k_F+(d_1+2d_2,\;2d_1+5d_2).
\end{aligned}
\tag{6.4}
$$


This follows by first solving


$$
(u^TG)(I_2-R_\infty/2)=u^TK,
$$


using


$$
(I_2-R_\infty/2)^{-1}
=
\begin{pmatrix}0&-2\\-2&-4\end{pmatrix}.
$$



Thus every Laurent coefficient in (6.3) is uniquely determined.

### 6.2 Explicit coefficient equations

Expanding


$$
G(m+1)
=
G_0+\frac{G_1}{m}
+\frac{G_2-G_1}{m^2}
+\frac{G_3-2G_2+G_1}{m^3}+O(m^{-4})
$$


and


$$
R(m)=R_\infty+\frac Jm-\frac J{m^2}
+\frac J{m^3}+O(m^{-4}),
$$


one obtains


$$
\mathcal L(G_0)=\Gamma_2,
$$




$$
\mathcal L(G_1)
=\Gamma_1-B_1^TG_0R_\infty-B_2^TG_0J,
\tag{6.5}
$$




$$
\begin{aligned}
\mathcal L(G_2)=\Gamma_0
&-B_2^T(-G_1R_\infty+G_1J-G_0J)\\
&-B_1^T(G_1R_\infty+G_0J)
-B_0^TG_0R_\infty,
\end{aligned}
\tag{6.6}
$$


and


$$
\begin{aligned}
\mathcal L(G_3)=
&-B_2^T\bigl((-2G_2+G_1)R_\infty
 +(G_2-2G_1+G_0)J\bigr)\\
&-B_1^T\bigl((G_2-G_1)R_\infty+(G_1-G_0)J\bigr)\\
&-B_0^T(G_1R_\infty+G_0J).
\end{aligned}
\tag{6.7}
$$



Applying (6.4) gives:


$$
\boxed{
\begin{array}{c|ccc}
 &P\text{-row}&Q\text{-row}&F\text{-row}\\ \hline
G_0&(0,0)&(-1,-1)&(-1/2,-1/2)\\
G_1&(0,1/2)&(3/2,3)&(1/2,1)\\
G_2&(-1/2,-1/2)&(-5/2,-7/2)&(-1,-3/2)\\
G_3&(0,-1/2)&(-25/2,-33)&(-7,-18)
\end{array}
}
\tag{6.8}
$$



For an additional direct check, the right sides of the equations for $G_1,G_2,G_3$ are respectively


$$
\begin{pmatrix}
0&1/2\\0&-1\\-1/4&-1
\end{pmatrix},
\qquad
\begin{pmatrix}
-1/2&-1/2\\-1&1/2\\-1/4&1/2
\end{pmatrix},
\qquad
\begin{pmatrix}
0&-1/2\\2&3/2\\1/4&-3/4
\end{pmatrix}.
\tag{6.9}
$$



These are small rational matrix calculations, not unevaluated recurrence sums.

### 6.3 Contradiction with the universal denominator

The last two components of $\widetilde\ell$ equal $m$ times the last two components of $\ell$. Proposition 4.1 therefore implies that the $F$-row of $G(m)$ has at most simple poles at $m=0$ and $m=-1$.

Since it is bounded at infinity, it must have the form


$$
g_F(m)=a+\frac b m+\frac c{m+1},
\qquad a,b,c\in\mathbb Q^{1\times2}.
\tag{6.10}
$$


Its Laurent coefficients necessarily satisfy


$$
(G_3)_F=-(G_2)_F.
\tag{6.11}
$$


But (6.8) gives


$$
(G_3)_F+(G_2)_F
=
\boxed{\left(-8,-\frac{39}{2}\right)\ne(0,0).}
\tag{6.12}
$$



This is the required obstruction.

### Theorem 6.1 — Unrestricted rational-gauge nonexistence

For the actual matrices and complete forcing row in Section 2,


$$
\boxed{
\ell(n+1)(\mathsf U_n\otimes\mathsf R_n)
+(n+1)^2\ell(n)=\gamma_n
}
$$


has no solution in $\mathbb Q(n)^6$. ∎

### Scope of the theorem

This proves that the displayed difference-module extension does not split by this rational row gauge.

It does **not** prove:

* that every possible bounded endpoint identity is impossible;
* that the six actual tensor sequences are rationally independent;
* that a sequence-specific relation not satisfying the matrix identity is impossible;
* any estimate for contact gcds;
* irrationality of $e+\pi$.

In particular, nonsplitting is an obstruction to the proposed elimination route, not a transcendence theorem.

---

# Part II. Actual paid contact projections

## 7. Recovering the contact directions in moment coordinates

The original finite matrix remains


$$
T=
\begin{pmatrix}
c&b&a\\
d&c&b\\
e_*&d&c
\end{pmatrix},
$$


where


$$
a=c_{n-2},\quad b=c_{n-1},\quad c=c_n,\quad
d=c_{n+1},\quad e_*=c_{n+2},
\qquad
c_k=[z^k]e^zq(z)^n.
$$



The actual endpoint rows are


$$
R_j=\ell_j\operatorname{adj}(T),
\qquad
\ell_0=(-1,n,-nm),\quad \ell_3=(0,0,1).
$$


Each actual primitive row $r_j$ is obtained from $R_j$ by its least coordinate denominator, followed by the gcd of the resulting three integer coordinates, with the recorded sign convention.

No arbitrary syzygy row is substituted below.

Define


$$
V=
\begin{pmatrix}
2N&0&0\\
N&N&0\\
m&t&1
\end{pmatrix}
=[v',w',e_2],
\qquad
\det V=2N^2.
\tag{7.1}
$$


Then the actual contact-coordinate row is


$$
\mathbf c_j=r_jV.
$$



Let $T_0,T_1,T_2$ be the columns of $T$. The shared kernel column is


$$
k=T_1+nT_0.
$$


The second kernel columns are


$$
k_3=T_0,\qquad k_0=T_2-nmT_0.
\tag{7.2}
$$


These follow directly from


$$
R_jT=(\det T)\ell_j.
$$



The five-moment reduction gives


$$
a=2md-2c-(n-1)b,
\qquad
e_*=\frac{4d+(n-2)c+b}{2N}.
\tag{7.3}
$$


Substitution into the moment definitions proves


$$
\boxed{Vz=2N(n+1)!\,k.}
\tag{7.4}
$$



Define the actual second directions


$$
W_j=2N(n+1)!\,V^{-1}k_j.
\tag{7.5}
$$


They are integral, and their explicit evaluations are as follows.

### Proposition 7.1 — Evaluated actual-contact directions

For $j=3$,


$$
\boxed{
W_3=
\begin{pmatrix}
X\\
Z\\
Y-X-(2n+1)Z
\end{pmatrix}.
}
\tag{7.6}
$$



For $j=0$,


$$
\boxed{
W_0=
\begin{pmatrix}
mZ-(n^2+1)X-(n-1)Y\\
mY+(1-n)X-m^2Z\\
2m\bigl(mX+(n^2+n+1)Z-NY\bigr)
\end{pmatrix}.
}
\tag{7.7}
$$



Moreover,


$$
\mathbf c_jz=0,\qquad \mathbf c_jW_j=0.
\tag{7.8}
$$



### Derivation

For an arbitrary column $l=(l_1,l_2,l_3)^T$,


$$
2NV^{-1}l
=
\begin{pmatrix}
l_1\\
2l_2-l_1\\
2Nl_3+Nl_1-2tl_2
\end{pmatrix}.
\tag{7.9}
$$


For $l=T_0$, use (7.3) and multiply by $(n+1)!$. The first two coordinates become $X,Z$; the third becomes


$$
Y-X-(2n+1)Z.
$$


This proves (7.6).

For $l=T_2-nmT_0$, use the first identity in (7.3) in the first two coordinates and both identities in the third. The resulting coordinates are exactly (7.7).

Finally,


$$
r_jk=r_jk_j=0,
$$


so (7.4)–(7.5) prove (7.8). ∎

The nonvanishing of the relevant cross products follows wherever $\det T\ne0$, because the corresponding pairs of kernel columns are independent. At original indices, this uses the retained finite-producer nonvanishing theorem.

---

## 8. All contact contents are retained

Put


$$
A_j=z\times W_j,
\qquad
h_j=\gcd(|A_{j,1}|,|A_{j,2}|,|A_{j,3}|),
\tag{8.1}
$$


and


$$
\kappa_j=\gcd(|c_{j,1}|,|c_{j,2}|,|c_{j,3}|).
\tag{8.2}
$$


These are distinct from:

* the content used to obtain $r_j$ from $R_j$;
* the least eight-entry clearer;
* the later two-entry reconstruction-row contents;
* the final weight gcds.

Since $r_j$ is primitive and


$$
\mathbf c_j\operatorname{adj}(V)=(\det V)r_j,
$$


we have


$$
\boxed{\kappa_j\mid 2N^2.}
\tag{8.3}
$$


Thus $\kappa_j$ is a unit at every $p>N$, but it must not be omitted from an all-prime identity.

The rows $\mathbf c_j$ and $A_j^T$ span the same rational line. Therefore, for the sign $\varepsilon_j\in\{1,-1\}$ determined by the actual row convention,


$$
\boxed{
\mathbf c_j=\varepsilon_j\kappa_j\,\frac{A_j^T}{h_j}.
}
\tag{8.4}
$$



This is an identity for the actual contacts, not a replacement normalization.

Let


$$
\widehat h=L_n\tau_n,\qquad
\widehat\ell=L_n\tau_{n+1},
\qquad
M=Q\widehat h-P\widehat\ell.
$$


Then


$$
\widehat R_j
=\mathbf c_j(\widehat h,\widehat\ell,0)^T.
$$


Expanding the cross product in (8.4) gives the paid reference projection


$$
\boxed{
h_j\widehat R_j
=
\varepsilon_j\kappa_j
\left[
W_{j,3}M+
F\bigl(W_{j,1}\widehat\ell-W_{j,2}\widehat h\bigr)
\right].
}
\tag{8.5}
$$



All factors in this identity are actual evaluated objects.

---

## 9. A complete source-specific Bézout identity

Retain


$$
C=mZ,\qquad
g_{\rm aff}=\gcd(|F|,|CM|),
$$


and


$$
\Theta
=
CM+F\bigl(2L_n(n!)^2-\mathscr K_n^\circ\bigr),
\qquad
T_{\rm aff}=\frac{\Theta}{g_{\rm aff}}.
\tag{9.1}
$$



Define the evaluated contact residual


$$
\boxed{
\widehat{\mathcal B}_j
=
W_{j,3}\bigl(2L_n(n!)^2-\mathscr K_n^\circ\bigr)
-C\bigl(W_{j,1}\widehat\ell-W_{j,2}\widehat h\bigr).
}
\tag{9.2}
$$


At original indices this is integral. In particular, the complete term


$$
2L_n(n!)^2
$$


has not been shortened or removed.

### Theorem 9.1 — Paid actual-contact identity

For $j=0,3$,


$$
\boxed{
\varepsilon_j\kappa_jW_{j,3}g_{\rm aff}T_{\rm aff}
-C h_j\widehat R_j
=
\varepsilon_j\kappa_jF\widehat{\mathcal B}_j.
}
\tag{9.3}
$$



### Proof

Multiply (9.1) by $\varepsilon_j\kappa_jW_{j,3}$, and subtract $C$ times (8.5). The terms involving $CMW_{j,3}$ cancel. The remaining terms are exactly the right side of (9.3). ∎

This is a source-specific contact projection: the directions $W_0,W_3$ come from the actual finite contact kernels, and $\mathscr K_n^\circ$ is the complete seeded transverse response.

It is not merely an additional holonomic state or a named Green sum.

---

## 10. Large-prime support, including the unit-force branch

The actual paid reference denominator is


$$
D_j=\frac{|\widehat R_j|}
{\gcd(|\widehat R_j|,|F|)}.
\tag{10.1}
$$


Let


$$
\mathfrak S_j=\gcd(|T_{\rm aff}|,D_j)_{>N}.
$$



### Corollary 10.1

With the usual interpretation that divisibility into $0$ is vacuous,


$$
\boxed{
\mathfrak S_j
\mid
\gcd\!\left(
D_j,\left|\frac{F}{g_{\rm aff}}\widehat{\mathcal B}_j\right|
\right)_{>N}.
}
\tag{10.2}
$$



### Proof

Fix $p>N$. Put


$$
f=v_p(F),\quad g=v_p(g_{\rm aff}),\quad
r=v_p(\widehat R_j),\quad t_0=v_p(T_{\rm aff}),
$$


so $0\le g\le f$, and


$$
v_p(D_j)=d=\max(r-f,0).
$$


Let


$$
e=\min(t_0,d).
$$



If $d=0$, the desired inequality is immediate. Otherwise $r=d+f$, so $r\ge e+f$, while $t_0\ge e$.

In (9.3), $\varepsilon_j\kappa_j$ is a $p$-adic unit by (8.3), and all other displayed coefficients are integral. Therefore


$$
f+v_p(\widehat{\mathcal B}_j)
\ge
\min(t_0+g,r)
\ge e+g.
$$


Hence


$$
e\le f-g+v_p(\widehat{\mathcal B}_j),
$$


which proves (10.2). ∎

### 10.1 The unit-force branch is explicitly retained

If $p>N$ and $p\nmid F$, then


$$
v_p(D_j)=v_p(\widehat R_j),\qquad
v_p(g_{\rm aff})=0,
$$


and (10.2) becomes


$$
\boxed{
\min\{v_p(T_{\rm aff}),v_p(\widehat R_j)\}
\le v_p(\widehat{\mathcal B}_j).
}
\tag{10.3}
$$


If also $p\nmid W_{j,3}$, reducing (9.3) modulo powers of $\widehat R_j$ gives the sharper equality


$$
\boxed{
\min\{v_p(T_{\rm aff}),v_p(\widehat R_j)\}
=
\min\{v_p(\widehat{\mathcal B}_j),v_p(\widehat R_j)\}.
}
\tag{10.4}
$$



Thus the branch $v_p(F)=0$ has not been discarded. A resultant formed after adding $F$ as a vanishing generator would not supply this information.

### 10.2 What this does not yet bound

The expressions $\widehat{\mathcal B}_j$ may have large prime factors. Their explicit evaluation is not a proof that those factors are rare, small, or weakly correlated with $\widehat R_j$.

The retained resonance quantity is


$$
J_{\rm res}=\operatorname{lcm}(\mathfrak S_0,\mathfrak S_3).
$$


Consequently (10.2) gives a genuine support restriction for $J_{\rm res}$, but not


$$
\log J_{\rm res}=o(n\log n).
$$



The previously established saturation simplification remains valid:


$$
\mathfrak S_0\mathfrak S_3\mid J_{\rm res}^2,
$$


so a separate bound for all unselected contact collision is unnecessary for that budget.

---

## 11. The precise contact obstruction and a follow-on lemma

The rational-gauge obstruction explains why the complete transverse coordinate cannot be eliminated by the proposed rational six-tensor splitting.

There is also a precise limitation on a source-blind elimination argument. On the branch $F\ne0$, the equation


$$
\Theta=0
$$


formally permits


$$
\mathcal K_n
=
2(n!)^2+\frac{CM}{L_nF}.
$$


If $\mathcal K_n$ is treated as an independent algebraic coordinate, this absorbs the affine equation rather than imposing a small-prime restriction on the contact reference. The missing ingredient is a property of the **actual seeded solution**, not another formal elimination with a free transverse variable.

A concrete sufficient follow-on lemma is now available.

### Proposed follow-on lemma — evaluated paid-contact correlation

Prove, on an infinite subset of one of the original geometric families, that the nonzero evaluated integers in (9.2) satisfy


$$
\log\operatorname{lcm}_{j=0,3}
\gcd\!\left(
D_j,\left|\frac{F}{g_{\rm aff}}\widehat{\mathcal B}_j\right|
\right)_{>n+2}
=o(n\log n).
\tag{11.1}
$$



By Corollary 10.1, this would imply the desired resonance estimate.

This is an **open obligation**, not a proved bound. Its value over the previous formulation is that its contact projections are now explicitly evaluated from the actual paid finite rows, with both the unit-force and nonunit-force branches present. No unknown contact producer remains.

A proof of (11.1) must use the actual seed and recurrence correlations. Direct height bounds for the displayed integers generally provide only an $O(n\log n)$ scale and are insufficient.

---

# Part III. Preservation of the original producer and final arithmetic

## 12. Finite boundaries, complete forcing, and physical return

The contact matrix remains $3\times3$, with indices $0,1,2$. Reconstruction remains four-dimensional, with coordinates $0,1,2,3$.

The complete force is retained in its original finite form. Put


$$
q_j=[z^j]q(z)^n,
$$




$$
\alpha_0=\alpha_1=1,\qquad
\alpha_j=\alpha_{j-1}-\frac12\alpha_{j-2},
$$




$$
\eta_L=\sum_{r=0}^{L}\frac1{r!}
+\sum_{r=1}^{L}\frac{2\alpha_{r-1}}r,
\qquad
\mathcal W_L=L!\eta_L.
$$


Then


$$
\boxed{
w_i=
\sum_{j=0}^{\min(2n,n+i)}
q_j(n+i)^{\underline j}\mathcal W_{2n+i-j},
\qquad 0\le i\le2.
}
\tag{12.1}
$$


The largest force index remains exactly $2n+2$. Both exponential and logarithmic terms remain.

Equivalently, the retained exponential differential source has coefficients


$$
\mathfrak f_k
=
(n+1)a_k-nk\,a_{k-1}
+\frac{(n-1)k(k-1)}2a_{k-2}
+\frac{k(k-1)(k-2)}2a_{k-3},
$$


through


$$
K=2n+2.
$$


The coefficient of $\mathfrak f_K$ in $b_{K+1}$ remains $1$. No terminal source term is discarded, and no finite inverse is extended beyond its physical boundary.

The complete normalized force is


$$
\widehat w_i=\frac{w_i}{(n+i)!}.
$$


With the actual raw endpoint rows,


$$
N_0=\det T+R_0\widehat w,\qquad
N_3=R_3\widehat w.
\tag{12.2}
$$


Thus the physical return is retained through the complete evaluated finite force, including the exterior contribution $\det T$.

The complete logarithmic normalization remains


$$
N_j=N_j^{\exp}
+4n!(\alpha_j\rho_n+\beta_j\rho_{n+1}),
$$


with


$$
N_0^{\exp}=\det T+R_0\widehat w^{\exp},
\qquad
N_3^{\exp}=R_3\widehat w^{\exp}.
$$


It is not replaced by the transverse response alone.

---

## 13. Both corrected columns and the least eight-entry clearer

Retain


$$
x=T^{-1}(n!t),\qquad y=T^{-1}\widehat w,
$$


where


$$
t=
\begin{pmatrix}
\tau_n\\
(\tau_n+\tau_{n+1})/2\\
\tau_{n+2}/2
\end{pmatrix}.
$$


Set


$$
S=
\begin{pmatrix}
1&-n&nm\\
0&1&-2n\\
0&0&1
\end{pmatrix},
\qquad sx=Sx,\quad sy=Sy.
$$


The complete corrected columns are


$$
u=(-sx_0,\ sx_0-sx_1,\ sx_1-sx_2,\ sx_2),
$$




$$
\boxed{
v=(1-sy_0,\ sy_0-sy_1,\ sy_1-sy_2,\ sy_2).
}
\tag{13.1}
$$


The exterior $+1$ remains explicit.

The least simultaneous clearer is


$$
D_8=
\operatorname{lcm}_{0\le j\le3}
\bigl(\operatorname{den}(u_j),\operatorname{den}(v_j)\bigr).
\tag{13.2}
$$


For each reconstruction row,


$$
g_j^{(8)}=\gcd(|D_8u_j|,|D_8v_j|),
$$


and


$$
\widetilde u_j=\frac{D_8u_j}{g_j^{(8)}},
\qquad
\widetilde v_j=\frac{D_8v_j}{g_j^{(8)}}.
\tag{13.3}
$$


These are all-prime contents.

The accepted $n=3375$ contents remain


$$
(113940000,\ 9780750,\ 10125,\ 1).
$$


They are not recomputed or extrapolated.

When $u_j\ne0$, the endpoint center has actual primitive denominator


$$
d_j=|\widetilde u_j|.
$$


Equivalently, in the retained scalar endpoint normalization,


$$
d_j=
\frac{|n!R_j^{\rm scalar}|}
{\gcd\bigl(|n!R_j^{\rm scalar}|,
|E_nR_j^{\rm scalar}+C_j^{\rm complete}|\bigr)}.
$$


The complete residual is required in this gcd.

---

## 14. Alignment acquisition remains an independent obligation

The rational-gauge theorem and contact identity do not estimate new terminal alignment.

For an original block $t=bn$, $b\in\{15,105\}$, retain the moving-threshold inventory


$$
\boxed{
\mathcal I_t
=
\frac{\mathcal I_n\,c^{\min}_{n,t}}
{\mathcal M_{n,t}\mathcal L_{n,t}},
}
$$


where


$$
\mathcal M_{n,t}
=
\prod_{n+2<p\le t+2}
p^{\min(v_p(F_n),v_p(M_n))}
$$


and


$$
\mathcal L_{n,t}
=
\prod_{p>t+2}p^{(a_n-a_t)_+}.
$$


Neither the medium-prime contribution nor loss of terminal depth may be suppressed.

The retained whole-telescope congruence applies under its original hypotheses:


$$
-\sum_{s=n}^{t-1}
\frac{u_{31,s}x_s+u_{32,s}y_s}{F_{s+1}}
\equiv\eta_t
\pmod{p^{a_t-v_p(F_n)}},
$$


when $p>t+2$, $a_t>v_p(F_n)$, and the actual seeded chart is used.

This is a congruence for the complete evaluated sum, not for its summands. All intermediate divisions and the primitive exterior payment $\mathcal I_t$ remain paid.

The outstanding acquisition target includes controlling


$$
\sum_{p>t+2}(a_t-a_n)_+\log p
$$


at a subfactorial scale on suitable original blocks. No such estimate is proved here.

---

## 15. The actual all-prime final denominator and whole error

Let


$$
h_{\rm end}=\gcd(|\widetilde u_0|,|\widetilde u_3|),
\qquad
\widetilde u_0=h_{\rm end}A_{\rm wt},
\quad
\widetilde u_3=h_{\rm end}B_{\rm wt}.
$$


For a reduced weight


$$
\lambda=\frac a{k_{\rm wt}},
\qquad k_{\rm wt}>0,
$$


retain


$$
J_{\rm wt}
=B_{\rm wt}\widetilde v_0-A_{\rm wt}\widetilde v_3,
$$




$$
T_{\rm wt}
=aJ_{\rm wt}+k_{\rm wt}A_{\rm wt}\widetilde v_3,
$$




$$
F_{\rm gcd}
=
\gcd(|A_{\rm wt}|,|a|)
\gcd(|B_{\rm wt}|,|a-k_{\rm wt}|),
$$




$$
G_{\rm wt}=\gcd(k_{\rm wt},|J_{\rm wt}|),
$$




$$
H_{\rm gcd}
=
\gcd\!\left(
h_{\rm end},
\frac{|T_{\rm wt}|}{F_{\rm gcd}G_{\rm wt}}
\right).
$$


The actual primitive numerator and denominator are


$$
\boxed{
q_\lambda=
\frac{k_{\rm wt}h_{\rm end}|A_{\rm wt}B_{\rm wt}|}
{F_{\rm gcd}G_{\rm wt}H_{\rm gcd}},
}
$$




$$
\boxed{
p_\lambda=
\operatorname{sgn}(A_{\rm wt}B_{\rm wt})
\frac{T_{\rm wt}}
{F_{\rm gcd}G_{\rm wt}H_{\rm gcd}}.
}
\tag{15.1}
$$


Every gcd here is all-prime.

Neither $D_*(n)$, the contact denominator $D_j$, nor a primitive denominator associated only with $\Theta/F$ replaces $q_\lambda$.

The required whole error remains


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda e_3\alpha_{n,2}
(\lambda-\Lambda_{n,2}),
}
\tag{15.2}
$$


with the retained meanings of the endpoint-error factors.

An irrationality proof still requires


$$
0<|q_\lambda(e+\pi)-p_\lambda|\longrightarrow0
$$


on the **same infinite original index set** on which the arithmetic bounds hold. None of the new results proves this nonvanishing or decay.

---

## 16. Bounded exact-arithmetic audit

No tools or computations were executed for this report. The proofs above give a full rational-gauge decision, so no new large linear-system solve is needed.

A coordinator may inspect the following bounded symbolic audit. It is auxiliary verification, not a substitute for an infinite-index theorem.

### Inputs

1. The displayed $3\times3$ matrices $\mathsf U_n,\mathsf U_n^{-1}$.
2. The displayed $2\times2$ matrices $\mathsf R_n,\mathsf R_n^{-1}$.
3. The six-entry row $\gamma_n$.
4. The three matrices $B_2,B_1,B_0$, the two matrices $R_\infty,J$, and the three forcing matrices $\Gamma_2,\Gamma_1,\Gamma_0$.
5. The four rational matrices $G_0,G_1,G_2,G_3$ in (6.8).
6. For the contact identities, independent indeterminates $n,X,Y,Z$, with $P,Q,F$ defined as in Section 2 and $W_0,W_3$ as in (7.6)–(7.7).

### Expected verifiable outputs

* $\mathsf U_n\mathsf U_n^{-1}=I_3$ and $\mathsf R_n\mathsf R_n^{-1}=I_2$;
* the determinant formulas (3.4);
* the exact row identity (3.5);
* zero residuals in the four Laurent coefficient equations (6.5)–(6.7) and the leading equation;
* the nonzero obstruction
  

$$
(G_3)_F+(G_2)_F=(-8,-39/2);
$$


* zero polynomial residuals in the evaluated contact-direction formulas after substituting (7.3);
* zero residual in the paid identity (9.3), treating the recorded content factors as explicit multiplicative factors.

This audit uses only fixed-size rational matrices and polynomial identities. It does not request a new $3375$, $11025$, or other expensive producer calculation. The closed $42$-variable test and the $21$ recurrence checks should not be repeated.

---

## 17. Proof ledger and conclusion

| Statement | Status |
|---|---|
| Correct invertible homogenization of the gauge equation | **Proved** |
| Universal rational denominator $(n+1)^2(n+2)$ | **Proved** |
| Sufficient numerator degree bounds | **Proved** |
| Unrestricted rational gauge for the displayed six-tensor system | **Does not exist; proved** |
| Actual contact directions $W_0,W_3$ | **Explicitly evaluated and proved** |
| Retention of actual primitive-contact contents | **Proved in the displayed identities** |
| Paid contact identity (9.3) | **Proved** |
| Large-prime support restriction retaining $p\nmid F$ | **Proved** |
| Subfactorial paid-contact correlation | **Open** |
| Subfactorial alignment acquisition | **Open** |
| Favorable all-prime primitive whole forms at the same indices | **Open** |
| Rationality or irrationality of $e+\pi$ | **Unresolved** |

The main new result is the complete rational-gauge obstruction:


$$
\boxed{
\ell(n+1)(\mathsf U_n\otimes\mathsf R_n)
+(n+1)^2\ell(n)=\gamma_n
\quad\text{has no rational solution.}
}
$$



The precise obstruction is not merely a failed ansatz. Every rational solution would have denominator dividing $(n+1)^2(n+2)$, would satisfy the proved degree bounds, and would therefore force a Laurent relation contradicted by


$$
(-8,-39/2).
$$



The second advance is the actual paid contact projection


$$
\boxed{
\varepsilon_j\kappa_j W_{j,3}g_{\rm aff}T_{\rm aff}
-C h_j\widehat R_j
=
\varepsilon_j\kappa_jF\widehat{\mathcal B}_j,
}
$$


with explicitly evaluated $W_0,W_3$. This supplies a valid resonance-support restriction without dropping the unit-force branch.

The remaining mathematical bottleneck is now specific: prove a subfactorial large-prime correlation bound for the **actual seeded values** of these contact projections, together with controlled alignment acquisition. Those estimates must then survive every prescribed content division and the all-prime final gcd, and must coincide with a nonzero whole-error estimate on the same infinite original geometric subsequence.

No unconditional proof of rationality or irrationality of $e+\pi$ follows from the present results.
