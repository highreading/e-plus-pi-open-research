> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the actual-seed gauge and its arithmetic consequences

## Abstract

The proposed universal rational-solution denominator


$$
D_*(n)=(n+1)^2(n+2)
$$


is valid for the actual homogenized seven-dimensional gauge system. The pole-orbit argument has the correct shift orientation: its forward boundary is governed by poles of $N(n)$ one step to the left, whereas its backward boundary is governed by poles of $N(n)^{-1}$ at the right endpoint itself.

There is also a sufficient degree bound at infinity. After scaling the third moment coordinate by $n$, the leading tensor transfer has no eigenvalue $-1$. Consequently every rational gauge $\ell$ satisfies


$$
\deg_\infty \ell_i\le0\quad(1\le i\le4),\qquad
\deg_\infty\ell_i\le-1\quad(i=5,6).
$$


Combined with $D_*$, this reduces the **unrestricted rational-gauge question** to a finite linear problem with only $22$ rational unknowns. Unlike the previous $42$-variable test, a negative certificate for this new problem would exclude every rational gauge of the stated tensor type.

The source integration, endpoint recurrence, tensor forcing, and factorial-growth seed argument survive the audit, with the qualification that their identification with the complete finite producer uses the retained physical-source and return theorems.

For the ternary construction, depth $21$ contributes only one factor $3^{-21}$ to the primitive determinant ratio. It does not yield a $21\nu$-digit primitive-denominator improvement. A useful new arithmetic target is an upper bound for the **relative bordered-cofactor valuation**, together with the corresponding all-prime bound for the actual producer pair. None of the accepted local results currently establishes that target.

No rationality or irrationality conclusion for $e+\pi$ follows.

---

## 1. Scope, domains, and proof status

Three different original families occur in the sources. They must remain separate.

1. **Seeded endpoint family**
   

$$
n=15^r\quad\text{or}\quad n=105^r,\qquad r\ge2.
$$


   Consecutive integers $n\ge2$ below are auxiliary recurrence indices. The normalization
   

$$
L_n=2^{(n+1)/2}
$$


   is used as the original integral normalization only at the original odd indices.

2. **Ternary determinant family**
   

$$
j>0,\qquad j\equiv84645\pmod{531441},
$$


   

$$
m=2^{2j-1},\quad n=4^j+1,\quad A=2m-1,\quad
   H=3^{h-1},\quad D=H-A,
$$


   with
   

$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
   \qquad C_{16}=147968\,3^{15}.
$$



3. **The separate $29$-adic weighted family**
   

$$
b=3^{249005515+574312172u},\quad n=2001b,\quad
   u\ge0,\quad u\equiv2\pmod{29^9}.
$$



No favorable conclusion on one family is transferred to another.

The supplied finite certificates are retained at their stated scope. In particular:

- the $21$ recurrence checks concern auxiliary indices $2,\ldots,22$;
- the old $42$-variable inconsistency concerns only denominator $n(n+1)(n+2)$ and numerator degree at most $6$;
- the structural certificate concerns matrix identities and entry denominators, not by itself universal solution denominators;
- no expensive producer calculation is repeated here.

The general denominator-bound framework is established mathematics: van Hoeij, Barkatou, and Middeke, *A Family of Denominator Bounds for First Order Linear Recurrence Systems*, arXiv:2007.02926. The argument below applies its ordinary-shift setting to the actual invertible matrix; it is not a new general denominator algorithm.

---

# Part I. Audit of the actual-seed recurrence

## 2. Exact integration of the physical exponential source

Let


$$
q(z)=1-z+\frac{z^2}{2},\qquad A_n(z)=e^zq(z)^n.
$$


The retained seed-subtracted response satisfies


$$
\begin{aligned}
&(1-z)qB_n'
-\bigl(n(1-z)q'+(n+1)q\bigr)B_n\\
&\hspace{25mm}
=\left(n+1-nz+\frac{n-1}{2}z^2+\frac12z^3\right)A_n,
\end{aligned}
$$


with $B_n(0)=-1$.

Direct multiplication gives


$$
q(z)(n+1+z)
=n+1-nz+\frac{n-1}{2}z^2+\frac12z^3.
$$


Also, since $A_n'=A_n+nq'A_n/q$, the differential operator applied to $A_n$ equals


$$
-(n+z)qA_n.
$$


Thus $V_n=B_n+A_n$, followed by $V_n=q^nU_n$, gives exactly


$$
(1-z)U_n'-(n+1)U_n=e^z,\qquad U_n(0)=0.
$$



Multiplication by $(1-z)^n$ yields


$$
\frac{d}{dz}\bigl((1-z)^{n+1}U_n\bigr)=e^z(1-z)^n.
$$


For


$$
S_n(z)=n!\sum_{k=0}^n\frac{(1-z)^k}{k!},
\qquad E_n=S_n(0),
$$


termwise differentiation shows


$$
S_n'+S_n=(1-z)^n.
$$


Therefore


$$
\boxed{
B_n(z)=-e^zq(z)^n+
\frac{q(z)^n}{(1-z)^{n+1}}\bigl(e^zS_n(z)-E_n\bigr).
}
$$



This is a rigorous formal-series identity under the retained physical differential equation. It is not a uniformly bounded endpoint representation: $S_n$ has degree $n$.

The complete physical source still runs through


$$
K=2n+2.
$$


Neither its terminal return nor its logarithmic and exponential boundary data has been deleted. The endpoint extraction below does not authorize changing that finite producer.

---

## 3. Endpoint recurrence and its seed

The identities


$$
S_{n+1}=(n+1)S_n+(1-z)^{n+1},\qquad
E_{n+1}=(n+1)E_n+1
$$


give


$$
(1-z)U_{n+1}
=(n+1)U_n+e^z-(1-z)^{-n-1}.
$$


Combining this with the differential equation proves


$$
V_{n+1}=qV_n'-nq'V_n-H_{n+1},
\qquad
H_n=\frac{q^n}{(1-z)^{n+1}}.
$$


The power in $H_{n+1}$ is indispensable.

Put


$$
v_n=[z^n]V_n,\quad w_n=[z^{n+1}]V_n,\quad
d_n=[z^n]A_n,\quad e_n=[z^{n+1}]A_n.
$$


Coefficient comparison in the differential equation gives


$$
\begin{aligned}
(k+1)[z^{k+1}]V_n
={}&(2k+1)[z^k]V_n\\
&+\frac{2n+1-3k}{2}[z^{k-1}]V_n
+\frac{k-n-1}{2}[z^{k-2}]V_n
+[z^k]A_{n+1}.
\end{aligned}
$$


In particular,


$$
(n+2)[z^{n+2}]V_n
=(2n+3)w_n-\frac{n+2}{2}v_n+d_{n+1}.
$$


Substitution in the parameter identity yields the two formulas reported in A3:


$$
v_{n+1}=-(n+1)v_n+2(n+1)w_n+d_{n+1}-\tau_{n+1},
$$




$$
\begin{aligned}
w_{n+1}={}&-(n+1)v_n+
\frac{(n+1)(3n+5)}{n+2}w_n\\
&+\frac{2n+3}{n+2}d_{n+1}+e_{n+1}
-\frac{\tau_{n+1}+\tau_{n+2}}2.
\end{aligned}
$$


Here the homogeneous endpoint identities are the retained ones for $H_n$.

The coefficient recurrence


$$
u_{k+1}(n)=(n+k+1)u_k(n)+1,\qquad u_0(n)=0
$$


gives, at $n=2$, $u_1=1,u_2=5,u_3=26$. Multiplication by $q^2$ proves


$$
(v_2,w_2)=\left(\frac12,\frac43\right).
$$


Since $a_2(2)=a_3(2)=1$, this gives $b_2=0,b_3=7$, and hence


$$
\boxed{\mathcal K_2=14.}
$$



---

## 4. Transverse forcing and automatic actual-seed matching

Use the actual tensor ordering


$$
\mathbf Y_n=
(P_n\tau_n,P_n\tau_{n+1},
Q_n\tau_n,Q_n\tau_{n+1},
F_n\tau_n,F_n\tau_{n+1})^T
$$


and


$$
K(n)=\mathsf U_n\otimes\mathsf R_n.
$$


The determinant calculation in A3 is valid: the term $-y_{n+1}$ vanishes only because it is paired with $y_{n+1}$ in an alternating determinant, not because it was omitted from the response.

The resulting recurrence is


$$
\mathcal K_{n+1}=-(n+1)^2\mathcal K_n+\gamma(n)\mathbf Y_n,
$$


where


$$
\gamma(n)=
\left(
0,\frac{n+2}{2},
-\frac{(n+1)^2}{2},
\frac{(n+1)^2+1}{2},
-\frac{n+1}{4},
\frac{n^2+3n+3}{4(n+1)}
\right).
$$


For example, the coefficient of $P_n\tau_{n+1}$ obtained before simplification is


$$
\frac{2n+3}{2}
-\frac{(2n+3)(n+1)}{2(n+2)}
+\frac{(n+1)^2}{2(n+2)}
=\frac{n+2}{2},
$$


consistent with the displayed row. The remaining coefficients follow by the same substitution of the stated formulas for $X_n,Z_n$.

The actual tensor seed is


$$
\mathbf Y_2=(0,0,20,40,-132,-264)^T.
$$



A rational gauge must solve


$$
\boxed{\ell(n+1)K(n)+(n+1)^2\ell(n)=\gamma(n).}
\tag{4.1}
$$


If it does, its discrepancy from the actual response satisfies


$$
d_{n+1}=-(n+1)^2d_n.
$$



The factorial-growth argument is sound. On any fixed circle $|z|=\rho<1$,


$$
V_n(z)=\frac{q(z)^n}{(1-z)^{n+1}}
\int_0^z e^w(1-w)^n\,dw
$$


has supremum at most $e^{C_\rho n}$, and so does $A_n$. Cauchy estimates give


$$
|b_n|+|b_{n+1}|\le n!e^{Cn}.
$$


The reference endpoints grow at most exponentially, as follows either from their generating functions or the bounded-coefficient two-dimensional recurrence. Thus


$$
|\mathcal K_n|+\|\mathbf Y_n\|\le n!e^{C'n}.
$$


A fixed rational gauge adds at most a polynomial factor for all sufficiently large positive integers. A nonzero discrepancy, however, grows as a nonzero constant times $(n!)^2$. Therefore it must vanish.

Hence every rational solution of (4.1) automatically matches the actual seed wherever propagation is regular. The denominator theorem below shows regularity at every $n\ge2$, so it also gives


$$
\ell(2)\mathbf Y_2=14.
$$



This conclusion concerns the actual endpoint identity. It does not establish any contact gcd estimate.

---

# Part II. Universal denominator and a complete finite gauge problem

## 5. Correct homogenization and matrix hypotheses

Let


$$
\mathcal Y(n)=\binom{\ell(n)^T}{1}.
$$


Transposing (4.1) gives


$$
\mathcal Y(n+1)=N(n)\mathcal Y(n),
$$


where


$$
N(n)=
\begin{pmatrix}
-(n+1)^2K(n)^{-T}&K(n)^{-T}\gamma(n)^T\\
0&1
\end{pmatrix}.
\tag{5.1}
$$


Its inverse is


$$
N(n)^{-1}=
\begin{pmatrix}
-(n+1)^{-2}K(n)^T&(n+1)^{-2}\gamma(n)^T\\
0&1
\end{pmatrix}.
\tag{5.2}
$$


Multiplying these two block matrices verifies the inverse identity, including the affine column and its sign.

For the displayed actual matrices,


$$
\det\mathsf U_n=\frac{(n+1)(n+2)^2(n+3)}2,\qquad
\det\mathsf R_n=-\frac{n+1}{n+2}.
$$


Thus $K$, and hence $N$, is invertible over $\mathbb Q(n)$. In particular,


$$
\det N=-\frac{4(n+1)^7}{(n+2)(n+3)^2}.
$$



The retained structural certificate verifies, for these very matrices,


$$
\operatorname{den}N=(n+2)(n+3),\qquad
\operatorname{den}N^{-1}=(n+1)^3(n+2).
\tag{5.3}
$$


Only the corresponding upper bounds are needed below. These are algebraic matrix facts, not assertions about arbitrary guessed gauge denominators. Formula (5.2) also directly exhibits the possible inverse poles and their orders.

Thus the hypotheses of the ordinary-shift denominator framework are met in $\mathbb Q[n]$ with $n\mapsto n+1$.

---

## 6. Pole-orbit audit

Work over the algebraic closure. For a rational vector, define its pole order at a point as the maximum coordinate pole order.

Consider a shift orbit $a+\mathbb Z$ containing a pole of $\mathcal Y$. Its poles form a finite subset, so there are leftmost and rightmost poles, denoted $r$ and $R$.

### Left boundary

At $n=r-1$, the vector $\mathcal Y(n)$ is regular while $\mathcal Y(n+1)$ has a pole. Therefore $N(n)$ must have a pole at $r-1$.

By (5.3),


$$
r-1\in\{-3,-2\},\qquad r\in\{-2,-1\}.
$$



### Right boundary

Use


$$
\mathcal Y(n)=N(n)^{-1}\mathcal Y(n+1).
$$


At $n=R$, the vector $\mathcal Y(n+1)$ is regular. Hence $N^{-1}$ must have a pole at $R$, so


$$
R\in\{-2,-1\}.
$$



These arguments exclude all other shift orbits, including nonintegral algebraic ones. The only possible poles are $-2,-1$.

### Orders

At $n=-3$, $\mathcal Y(n)$ is regular and $N(n)$ has at most a simple pole. Therefore $\mathcal Y$ has pole order at most $1$ at $-2$.

At $n=-2$, multiplication by $N(n)$ can add at most one further pole order. Thus the order at $-1$ is at most $2$.

Cancellations can only lower these bounds. Consequently


$$
\boxed{D_*(n)\ell(n)\in\mathbb Q[n]^6,\qquad
D_*(n)=(n+1)^2(n+2).}
\tag{6.1}
$$



The parent's proposed denominator is therefore accepted. The use of $N(n-1)^{-1}$ instead of $N(n)^{-1}$ at the right boundary would have changed the argument incorrectly; no such orientation error occurs here.

---

## 7. New theorem: a sufficient degree bound at infinity

A raw entrywise degree estimate for $\mathsf U_n$ is too weak because its third coordinate has a different natural size. The following scaling removes that difficulty.

Set


$$
S(n)=\operatorname{diag}(1,1,n),\qquad
\widetilde{\mathsf U}(n)=S(n+1)^{-1}\mathsf U_nS(n).
$$


Direct division of the displayed entries by $n^2$ gives


$$
n^{-2}\widetilde{\mathsf U}(n)\longrightarrow
U_\infty=
\begin{pmatrix}
0&1&1/2\\
0&-1&-1/2\\
0&1&1/2
\end{pmatrix}.
\tag{7.1}
$$


Also


$$
\mathsf R_n\longrightarrow
R_\infty=
\begin{pmatrix}0&1\\1&2\end{pmatrix}.
$$



Define the transformed row


$$
h(n)=\ell(n)(S(n)\otimes I_2).
$$


Multiplying the gauge equation on the right by $S(n)\otimes I_2$ gives


$$
h(n+1)\bigl(\widetilde{\mathsf U}(n)\otimes\mathsf R_n\bigr)
+(n+1)^2h(n)
=\widetilde\gamma(n),
\tag{7.2}
$$


where


$$
\widetilde\gamma(n)=\gamma(n)(S(n)\otimes I_2).
$$


Every entry of $\widetilde\gamma$ has degree at infinity at most $2$.

The matrix $U_\infty$ has eigenvalues


$$
0,\quad0,\quad-\frac12,
$$


while $R_\infty$ has eigenvalues $1\pm\sqrt2$. Hence


$$
I_6+U_\infty\otimes R_\infty
$$


is invertible. More explicitly, its determinant is


$$
\left(1-\frac{1+\sqrt2}{2}\right)
\left(1-\frac{1-\sqrt2}{2}\right)
=-\frac14\ne0.
\tag{7.3}
$$



Suppose a nonzero rational row $h$ has degree at infinity $d>0$, and write


$$
h(n)=n^dh_d+O(n^{d-1}),\qquad h_d\ne0.
$$


The coefficient of $n^{d+2}$ in (7.2) is


$$
h_d(I_6+U_\infty\otimes R_\infty).
$$


The right side has degree at most $2$, so this coefficient must vanish. Invertibility contradicts $h_d\ne0$.

Thus $d\le0$. Returning to $\ell$,


$$
\boxed{
\deg_\infty\ell_i\le0\ (i=1,\ldots,4),\qquad
\deg_\infty\ell_i\le-1\ (i=5,6).
}
\tag{7.4}
$$



There is no unbounded positive-degree branch.

Combining (6.1) and (7.4) proves:

> **Complete rational-gauge bound.** Every rational solution of (4.1) has the form
> 

$$
> \ell_i(n)=\frac{A_i(n)}{(n+1)^2(n+2)},
>
$$


> with
> 

$$
> \deg A_i\le3\quad(i\le4),\qquad
> \deg A_i\le2\quad(i=5,6).
>
$$



This is the principal new proved result of the report.

---

## 8. A finite certificate problem that decides all rational gauges

Write


$$
A_i(n)=\sum_{j=0}^3a_{ij}n^j\quad(i=1,\ldots,4),
$$




$$
A_i(n)=\sum_{j=0}^2a_{ij}n^j\quad(i=5,6).
$$


There are


$$
4\cdot4+2\cdot3=22
$$


rational unknowns.

Substitute $\ell=A/D_*$ into (4.1). A sufficient common polynomial multiplier is


$$
C(n)=4(n+1)(n+2)D_*(n)D_*(n+1),
$$


of degree $8$. Form the six polynomials


$$
C(n)\left(
\frac{A(n+1)}{D_*(n+1)}K(n)
+(n+1)^2\frac{A(n)}{D_*(n)}
-\gamma(n)
\right).
\tag{8.1}
$$


A safe degree bound is $11$: $K(n)$ has degree at infinity at most $3$, and the remaining terms have degree at most $2$ before multiplication by $C$. Thus coefficients in degrees $0,\ldots,11$ suffice.

The seed equation can be included as an independently checkable redundant condition:


$$
A(2)\mathbf Y_2=14D_*(2)=504.
\tag{8.2}
$$



### Expected exact outputs

A coordinator-authorized calculation should return either:

- **A solution:** the six polynomials $A_i$, their least common coefficient denominator $\delta$, six zero residual polynomials in (8.1), and seed residual zero; or
- **An inconsistency certificate:** an exact rational left-null vector for the coefficient system whose product with the coefficient matrix is zero and whose product with the right-hand side is $1$.

A negative result settles nonexistence of every rational gauge in (4.1), not merely a guessed class. A positive result proves the actual-seed identity, with all denominator payments recorded.

No such calculation has been performed here. It does not repeat the old $42$-variable calculation.

---

# Part III. Bridge to actual final arithmetic

## 9. What a gauge answer would and would not settle

If the gauge exists and $\delta A_i\in\mathbb Z[n]$, then the paid identity is


$$
\delta D_*(n)\mathscr K_n^\circ
=L_n\,\delta A(n)\mathbf Y_n.
$$


The complete affine expression becomes


$$
\begin{aligned}
\delta D_*\Theta
={}&\delta D_*CM\\
&+F\left(\delta D_*\,2L_n(n!)^2
-L_n\,\delta A(n)\mathbf Y_n\right).
\end{aligned}
\tag{9.1}
$$


The factorial term is not removed. Nor are primes dividing $\delta D_*$ cancelled without proof.

The recovered actual contacts now give concrete objects for the subsequent arithmetic task. With


$$
T=\begin{pmatrix}c&b&a\\d&c&b\\e^*&d&c\end{pmatrix},
\qquad
R_j=\ell_j\operatorname{adj}(T),
$$


the actual integer row $r_j$ is obtained by its prescribed least denominator and three-coordinate content division. Then


$$
c_j=(r_jv',r_jw',r_je_2),
\qquad
\widehat R_j=c_j\cdot(L_n\tau_n,L_n\tau_{n+1},0).
$$


These are not arbitrary syzygy rows. Their coordinate contents remain distinct from the later eight-entry clearer and row contents.

The arithmetic target is still a paid certificate against


$$
D_j=\frac{|\widehat R_j|}{\gcd(|\widehat R_j|,|F|)}.
$$


It must cover primes with $v_p(F)=0$. Adding $F$ as an extra generator can discard precisely this unit-force branch.

A sufficient follow-on target remains an actual-contact Bézout/support bound implying


$$
\log J_{\rm res}=o(n\log n)
$$


on an infinite original subsequence. The gauge theorem does not imply it.

Likewise, the moving-threshold inventory must remain


$$
\mathcal I_t=
\frac{\mathcal I_n c^{\min}_{n,t}}
{\mathcal M_{n,t}\mathcal L_{n,t}},
$$


with


$$
\mathcal M_{n,t}
=\prod_{n+2<p\le t+2}p^{\min(v_p(F_n),v_p(M_n))},
\qquad
\mathcal L_{n,t}
=\prod_{p>t+2}p^{(a_n-a_t)_+}.
$$


The new gauge bound removes neither factor.

---

## 10. Depth $21$: reuse of the primitive ternary ratio

Retain the actual finite space


$$
\mathbb Z_3[y]_{\le m},
$$


the LOW, residual, and HIGH boundaries from A4, and the physical terminal $Y_m$. The complete functional is


$$
\mathcal M(G)=
-\frac{3^h}{4}\mathfrak f(G)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](G-G(-1))/(y+1)}{2v+1}.
$$


Neither its factorial term nor its endpoint-subtracted rational term is replaced.

The accepted depth result, under its retained producer/source hypotheses, is


$$
S_{\rm act}\in3^{21}M,\qquad
\Upsilon_{21}=-S_{\rm act}/3^{21},
$$




$$
\Upsilon_{21}\equiv-S_c/3^{21}\pmod{3^5}.
$$


It retains the corrected core columns $F=Z-WE_c^{-1}C_c$, the actual inverse loss, and the complete return


$$
J^T\varepsilon+\omega
=-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
$$



Define


$$
D_0=\det\Upsilon_{21},
$$




$$
D_1=e_{\rm act}^T\operatorname{adj}(\Upsilon_{21})e_{\rm act}
-3^{21}d_{\rm act}D_0.
\tag{10.1}
$$


The old exact ratio theorem, applied at depth $21$, gives


$$
\boxed{
\frac{\beta_1}{\beta_0}
=-\frac{3^{h-21}Q_n^{\rm loc}(-1)}4\,\frac{D_1}{D_0}.
}
\tag{10.2}
$$


Thus, when the quantities are nonzero,


$$
\boxed{
v_3(q)=
\max\{0,h-21+v_3(Q_n^{\rm loc}(-1))
+v_3(D_1)-v_3(D_0)\}.
}
\tag{10.3}
$$



The common factor involving $\det E_{\rm act}$ and $3^{21(\nu-1)}$ cancels in the ratio. It is not a $21\nu$-digit primitive gain.

Indeed, if the same Schur complement is normalized at depths $15$ and $21$, then


$$
\Upsilon_{15}=3^6\Upsilon_{21}.
$$


Consequently


$$
D_{0,15}=3^{6\nu}D_0,\qquad
D_{1,15}=3^{6(\nu-1)}D_1.
$$


Substitution in the old depth-$15$ formula gives exactly (10.2). Increasing normalization depth does not, by itself, change the actual primitive denominator.

---

## 11. A concrete relative-cofactor and final-gcd target

Put


$$
c=h-21+v_3(Q_n^{\rm loc}(-1)),\quad
a=v_3(D_0),\quad b=v_3(D_1).
$$


Then


$$
v_3(q)=\max(0,c+b-a).
\tag{11.1}
$$



A useful sufficient target is therefore:

> **Relative-cofactor target.** Prove, on the original ternary family,
> 

$$
> D_0D_1\ne0,\qquad b-a\le-c+T
>
$$


> for an explicit $T\ge0$. Then $v_3(q)\le T$.

For complete elimination of the ternary part, it suffices to prove


$$
b-a\le-c.
$$


Large common valuations of $D_0,D_1$ are irrelevant unless their difference is controlled.

The retained sufficient noncancellation condition


$$
v_3\!\left(e_{\rm act}^T\operatorname{adj}(\Upsilon_{21})e_{\rm act}\right)
<a+20
$$


identifies $b$ with the first term's valuation, because $d_{\rm act}\in3^{-1}\mathbb Z_3$. It does not by itself give a useful bound for $b-a$, and it has not been evaluated on the actual residual.

To connect this to the actual all-prime integers, retain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,\qquad
g_\ell=\gcd(|A_\ell|,|B_\ell|).
$$


For every prime,


$$
v_p(q)=\max(0,v_p(B_\ell)-v_p(A_\ell)),
$$


so exactly


$$
\log q
=\sum_p\max(0,v_p(B_\ell)-v_p(A_\ell))\log p.
\tag{11.2}
$$



A concrete sufficient all-prime improvement is a bound


$$
\sum_{p\ne3}\max(0,v_p(B_\ell)-v_p(A_\ell))\log p\le R_j
$$


together with the relative-cofactor target above. Then


$$
\boxed{\log q\le R_j+T\log3.}
\tag{11.3}
$$


Equivalently,


$$
g_\ell\ge |B_\ell|\,e^{-R_j}3^{-T}.
$$



This states precisely what must be gained in the **actual final gcd**, after the actual contents, multiplier, and least clearer. No accepted local result currently supplies $R_j$, nor the required relative-cofactor bound.

---

## 12. Primitive normalization and the whole same-index error remain unchanged

For the endpoint family, preserve the complete reconstruction


$$
x=T^{-1}(n!t),\qquad y=T^{-1}\widehat w,
$$


the stated triangular matrix $S$, and


$$
u=(-sx_0,sx_0-sx_1,sx_1-sx_2,sx_2),
$$




$$
v=(1-sy_0,sy_0-sy_1,sy_1-sy_2,sy_2).
$$


The exterior $+1$ is essential. The clearer is the least simultaneous clearer of all eight entries,


$$
D_8=\operatorname{lcm}_{0\le j\le3}
\{\operatorname{den}(u_j),\operatorname{den}(v_j)\},
$$


followed by the actual all-prime row contents


$$
g_j=\gcd(|D_8u_j|,|D_8v_j|).
$$


The accepted contents at $3375$,


$$
(113940000,\ 9780750,\ 10125,\ 1),
$$


are not recomputed or altered.

The complete endpoint residual is still


$$
C_j^{\rm complete}
=\mathcal E_j^\circ+
2n!(n+1)!\bigl(\alpha_j\rho_n+\beta_j\rho_{n+1}\bigr),
$$


and


$$
d_j=
\frac{|n!R_j|}
{\gcd(|n!R_j|,|E_nR_j+C_j^{\rm complete}|)}.
$$


For the retained weight, the actual denominator remains


$$
q_\lambda=
\frac{k_{\rm wt}h_{\rm end}|A_{\rm wt}B_{\rm wt}|}
{F_{\rm gcd}G_{\rm wt}H_{\rm gcd}},
$$


with every prescribed gcd over all primes. It is not replaced by the denominator of a gauge or of $\Theta/F$.

The whole error remains


$$
q_\lambda(e+\pi)-p_\lambda
=q_\lambda e_3\alpha_{n,2}(\lambda-\Lambda_{n,2}).
\tag{12.1}
$$



For the ternary determinant pair,


$$
q(e+\pi)-p
=\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{g_\ell}
\det H_{\rm complete}.
\tag{12.2}
$$


For example, when $B_\ell\ne0$, (11.3) would give the concrete bound


$$
|q(e+\pi)-p|
\le
e^{R_j}3^T
\left|\frac{\det H_{\rm complete}}{\beta_1}\right|.
$$


An irrationality proof would still require the right side to tend to zero and the complete determinant to be nonzero on the same infinite original indices.

Finally, the separate $29$-adic conclusions remain finite-depth statements. The normalized $29^7$-tail in the next feedback digit, the original split at $5044$, both cutoffs, the complete returns, and the separate physical terminal remain necessary. Its actual primitive denominator is still $A_B/\gcd(A_B,|H_B|)$, with the actual least simultaneous clearer and the whole error $-q_n\epsilon_n$. Fixed-depth local identities do not establish the needed unbounded primitive-depth alignment.

---

## 13. Conclusion and exact next task

### New proved result

For the actual endpoint tensor equation, every rational gauge has denominator dividing


$$
(n+1)^2(n+2)
$$


and numerators of degrees at most $3,3,3,3,2,2$. Thus the unrestricted rational-gauge question is reduced to the explicit $22$-unknown exact linear system in Section 8.

### Conditional deductions

A solution of that system automatically matches the actual seed and yields a paid endpoint identity. It would not prove contact resonance bounds, alignment acquisition bounds, or final gcd growth.

For the ternary producer, a proved relative-cofactor bound together with the all-prime deficit estimate in Section 11 would bound the actual primitive denominator. Depth $21$ alone does neither.

### Exact bounded calculation requested

Only the following new calculation is needed to settle the gauge question:

- **Inputs:** the displayed $\mathsf U_n,\mathsf R_n,\gamma(n)$, $D_*=(n+1)^2(n+2)$, numerator degree bounds $3,3,3,3,2,2$, and the actual seed.
- **Equations:** the six cleared polynomial identities (8.1), with coefficient degrees $0,\ldots,11$, optionally supplemented by (8.2).
- **Verifiable output:** either explicit rational numerator polynomials and zero residuals, or an exact inconsistency witness.

No tools were used and this calculation has not been executed.

### Remaining mathematical bottleneck

Even after the gauge is decided, the global obstruction remains arithmetic: a bound for the actual, fully paid all-prime primitive denominator against a nonzero whole error on the same infinite original indices. The recovered contacts make the subsequent Bézout target concrete, but no accepted result yet controls its unit-force branch or proves the necessary subfactorial resonance/acquisition estimates.



$$
\boxed{\text{The rationality or irrationality of }e+\pi\text{ remains unresolved.}}
$$


