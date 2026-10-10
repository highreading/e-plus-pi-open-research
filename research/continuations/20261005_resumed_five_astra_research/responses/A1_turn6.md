> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1, Turn 6 — Elimination of the terminal producer jet from the complete force, and the actual depth-eight operator

## Executive conclusion

There is a way to advance the actual residual without first finding a closed formula for the ten-coefficient producer jet.

The decisive new result is a **corrected-column localization theorem**. With the hypotheses of Turn 5 retained exactly, it gives


$$
\boxed{\Phi_R\equiv0\pmod{27}}
$$


on the entire original domain


$$
n=4^j+1,\qquad j>0,\qquad81\mid j,\qquad
A=n-2=H-D,\qquad 0<D<H/972.
$$


Here


$$
(\Phi_R)_{ij}
=\mathcal M\!\left(R\widehat z_i^{\,c}\widehat z_j^{\,c}\right)
$$


uses the **complete core-corrected columns**, not the uncorrected $z_i$. The proof retains the endpoint subtraction, every pole contributing modulo $27$, the finite column boundaries, and the complete LOW correction.

Consequently,


$$
\boxed{\mathscr R_{\rm act}\equiv\mathscr R_c\pmod{3^9}.}
$$


This is a finite-precision assertion about the actual producer. It does not assert $R\equiv0\pmod{27}$, or that the exact force $\Phi_R$ is zero.

On the sharply specified whole-zero branch


$$
\boxed{0<D<H/2916,}
$$


the LOW and HIGH terms can also be evaluated at the next required precision:


$$
\boxed{B\in3^7M,\qquad
V\widehat E^{-1}V^T\in3^7M.}
$$


Thus the complete actual residual satisfies


$$
\boxed{
\mathscr R_{\rm act}\equiv G_c(Z,Z)\pmod{3^9}.
}
$$


Its next digit is therefore explicitly


$$
\boxed{
\frac{\mathscr R_{\rm act}}{3^8}\equiv\mathcal C_8\pmod3,
\qquad
(\mathcal C_8)_{ij}
=[y^{\varrho_8-i-j}](y-1)^D,
\quad
\varrho_8=\frac{H/2187-1}{2},
}
$$


on the **original index range**


$$
0\le i,j<\nu,\qquad \nu=D/2-1.
$$



Since the actual depth-seven digit is wholly zero on this branch, its radical is the entire residual space. Hence $\mathcal C_8$ is the next operator on the **actual radical**, not merely a core candidate. Its transported endpoint is


$$
\boxed{\overline e_8=\bigl((-1)^i\bigr)_{0\le i<\nu}.}
$$



The true shortened endpoint again forces singularity:


$$
\boxed{\mathcal C_8\ \text{is singular on }D<H/2916.}
$$


In particular, this advance does not produce an invertible depth-eight denominator branch.

A separate result below gives an explicit finite Pascal digit-lifting algorithm for the normalized producer system. Given the exact scalar response, it evaluates the terminal jet uniformly in finite $n$. It does **not** establish a bounded-state algorithm in $n$, nor a uniform precision bound for computing the rank-one scalar quotient. The force-localization theorem avoids that unresolved scalar-computation issue entirely.

No tools were used. No original-index computation or new infinitude claim is made. The irrationality or rationality of $e+\pi$ remains unresolved.

---

# 1. Exact scope and retained hypotheses

Retain


$$
n=4^j+1,\qquad j>0,\qquad81\mid j,
$$




$$
A=n-2=H-D,\qquad H=3^{h-1},\qquad 0<D<H/972,
$$


and


$$
m=\frac{A+1}{2},\qquad
d=\frac{3D}{2}-1,\qquad
\nu=\frac D2-1.
$$



The finite columns remain


$$
U_a=(y-1)^a\quad(0\le a<D),
$$




$$
z_i=y^i(y-1)^D\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m).
$$



Write $x=y-1$. The actual producer and its correction are


$$
Q_n^{\rm loc}=3P_n=Q_c+729R,
$$




$$
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=-71-A.
$$


The retained order-six interface is


$$
R\in\mathbb Z_3[y].
$$


Because the leading coefficients cancel,


$$
\boxed{\deg R\le n-1=A+1.}
\tag{1.1}
$$



The complete functional is unchanged:


$$
\boxed{
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\!\!\sum_{\substack{v\ge0\\2v+1\le4n-3}}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^s)=(2s)!.
}
\tag{1.2}
$$



All reductions below are reductions of this functional at its original finite cutoff.

## 1.1 What is reused

The following are retained at their supplied scope:

- the order-six actual-producer interface;
- the finite LOW/HIGH block identities and loss-one perturbation estimate;
- $B\in3^6M(\mathbb Z_3)$;
- the complete formula modulo $3^9$
  

$$
\mathscr R_{\rm act}\equiv
  G_c(Z,Z)-9V\widehat E^{-1}V^T
  +3^8\mathcal K_{\rm LOW}+3^6\Phi_R
  \pmod{3^9};
  \tag{1.3}
$$


- the finite-boundary inverse and complete-$F$ propagation proved in Turn 4;
- the independently audited algebraic decomposition of the binomial residue matrix, including its shortened terminal class.

Turn 5 is still pending independent review. I do not label that review completed here. The new argument uses precisely its factorial-saturation conclusion and its explicit hypotheses. Sections 2–3 also expose the part of that producer calculation needed for the present application.

---

# 2. The exact producer denominator and terminal jet

Let


$$
F_n=(n-1)!,
\qquad
u_a=\frac{F_n(-2)^a}{a!},
\qquad 0\le a<n,
$$


and let


$$
\mathsf T_n
=
\left(\binom{a+b}{a}\gamma_{a+b}\right)_{0\le a,b<n},
$$


where


$$
\gamma_0=1,\qquad \gamma_1=0,\qquad
\gamma_{r+1}=(4r+2)\gamma_r+4\gamma_{r-1}.
$$



The signed rank-one denominator remains


$$
\boxed{\eta_n=F_n^2-u^T\mathsf T_n^{-1}u.}
\tag{2.1}
$$


It is nonzero; it is not assumed to be a $3$-adic unit.

With the complete normalized force $\tau$ from Turn 5, set


$$
\mathbf t=\mathsf T_n^{-1}\tau,\qquad
\mathbf v=\mathsf T_n^{-1}u,
$$




$$
\chi_n=u^T\mathbf t,\qquad
\xi_n=\frac{\chi_n}{\eta_n}.
$$


For


$$
3P_n-Q_c=\sum_{a=0}^{n-1}e_a x^a,
$$


the exact coefficient and endpoint formulas are


$$
\boxed{
e_a=-\frac{F_n}{a!}\bigl(t_a+\xi_n v_a\bigr),
\qquad
(3P_n-Q_c)(-1)=-F_n^2\xi_n.
}
\tag{2.2}
$$



The relevant Turn 5 implications are:

1. $\mathsf T_n\in\operatorname{GL}_n(\mathbb Z_3)$;
2. $v_{n-1}\equiv2\pmod3$;
3. integrality of $e_{n-1}$, together with (2.2), gives $\xi_n\in\mathbb Z_3$;
4. therefore
   

$$
v_3(e_a)\ge v_3(F_n/a!),
   \qquad
   v_3((3P_n-Q_c)(-1))\ge2v_3(F_n).
   \tag{2.3}
$$



This reasoning does not replace $\eta_n$ by a unit and does not infer extra producer precision solely from $v_3(j)$.

The producer determinant is still


$$
\boxed{
\det C_n
=
\left(\prod_{a=0}^{n-1}(a!)^2\right)
\det\mathsf T_n\,\frac{\eta_n}{F_n^2}.
}
\tag{2.4}
$$



## 2.1 The exact ten-coefficient jet modulo $27$

Put


$$
t=v_3(A)=1+v_3(j)\ge5.
$$


Define


$$
\kappa=
\begin{cases}
9,&t=5\text{ or }6,\\
6,&t=7,\\
3,&t=8,\\
0,&t\ge9.
\end{cases}
\tag{2.5}
$$


These are exactly $\ell_9-2$ from Turn 5, not enlarged degree bounds.

Factorial saturation and the endpoint divisibility give


$$
\boxed{
R(y)\equiv(y+1)x^{A-\kappa}B_3(x)\pmod{27},
\qquad \deg B_3\le\kappa.
}
\tag{2.6}
$$


Thus $B_3$ has at most ten coefficients.

Both features of (2.6) matter:

- the lower exponent is exactly $A-\kappa=n-\ell_9$;
- the endpoint factor is legitimate because $R(-1)\equiv0\pmod{27}$ and $x=-2$ is a unit.

No value of a coefficient of $B_3$ is presumed below.

---

# 3. Uniform finite Pascal evaluation of the normalized system

There is an explicit finite digit-lifting procedure for $\mathbf t$ and $\mathbf v$. It is useful to distinguish this from a bounded-state evaluation of the scalar $\xi_n$.

## 3.1 An explicit inverse action modulo $3$

Group the original indices $0,\ldots,n-1$ by their residues $r=0,1,2$, retaining the exact sizes


$$
m_r=\#\{a<n:a\equiv r\pmod3\}.
$$


Let


$$
(P_q)_{ij}=\binom ij,\qquad 0\le i,j<q,
$$


and let


$$
E:\mathbb F_3^{m_2}\longrightarrow\mathbb F_3^{m_0}
$$


be the initial-coordinate embedding. Here $m_0=m_2$ or $m_2+1$.

After the finite Pascal congruence transformation, $\mathsf T_n\bmod3$ becomes


$$
\mathsf M=
\begin{pmatrix}
I_{m_0}&0&E\\
0&2I_{m_1}&0\\
E^T&0&0
\end{pmatrix}.
\tag{3.1}
$$



For a right-hand side $b$, first group it into $b_0,b_1,b_2$, and put


$$
d_r=P_{m_r}^{-1}b_r.
$$


The inverse Pascal matrix is explicit:


$$
(P_q^{-1})_{ij}=(-1)^{i-j}\binom ij.
$$



Solve $\mathsf Mw=d$ by


$$
w_1=2d_1,
$$




$$
(w_0)_i=(d_2)_i,\qquad
(w_2)_i=(d_0)_i-(d_2)_i
\quad(0\le i<m_2),
$$


and, if $m_0=m_2+1$,


$$
(w_0)_{m_2}=(d_0)_{m_2}.
$$


Finally,


$$
z_r=P_{m_r}^{-T}w_r,
$$


followed by the inverse residue permutation.

This gives an explicit operator


$$
\mathscr L_n:b\longmapsto\mathsf T_n^{-1}b\pmod3
$$


at every finite order, with the original endpoint retained.

## 3.2 Nine-digit lifting

For any $b\in\mathbb Z_3^n$, solve $\mathsf T_nz=b$ modulo $3^M$ as follows:


$$
z^{(0)}=0,
$$




$$
d^{(r)}
=
\frac{b-\mathsf T_nz^{(r)}}{3^r}\pmod3,
$$




$$
z^{(r+1)}
=
z^{(r)}+3^r\operatorname{lift}\!\left(\mathscr L_n d^{(r)}\right),
\qquad 0\le r<M.
\tag{3.2}
$$


The divisibility in the middle line follows inductively.

Taking $M=9$ computes $\mathbf t,\mathbf v\bmod3^9$. If the exact scalar response supplies $\xi_n\bmod3^9$, formula (2.2) then gives every required $e_a\bmod3^9$. Only after that multiplication is division by $729$ performed.

The last synthetic division is also explicit. Write


$$
x^{-(A-\kappa)}R
\equiv\sum_{j=0}^{\kappa+1}w_jx^j\pmod{27}.
$$


If $B_3=\sum_{j=0}^{\kappa}b_jx^j$, then


$$
b_0=2^{-1}w_0,
\qquad
b_j=2^{-1}(w_j-b_{j-1})\quad(1\le j\le\kappa),
\tag{3.3}
$$


and the terminal check is


$$
w_{\kappa+1}=b_\kappa.
$$


That last equality is the endpoint divisibility check; it must not be omitted.

## 3.3 What this does not resolve

If


$$
s_n=v_3(\eta_n),
$$


computing $\xi_n\bmod3^9$ from $\chi_n/\eta_n$ generally requires $\chi_n,\eta_n$ modulo $3^{s_n+9}$, together with a certified value of $s_n$. Integrality of $\xi_n$ does not bound $s_n$.

Thus:

- **proved:** a uniform finite Pascal algorithm, with nine unit-matrix digit lifts once the scalar response is supplied;
- **not proved:** an $n$-independent bound on the work or precision needed to obtain that scalar response;
- **not claimed:** a closed formula for the ten coefficients depending on only a bounded collection of digits of $n$.

The next theorem makes their explicit evaluation unnecessary for the actual residual through modulus $3^9$.

---

# 4. The complete corrected-column force loses the terminal jet

Set


$$
\Omega=\frac H{243}.
$$


For a width $W$, use the finite-support classes


$$
I_\Omega(W)=\{a\Omega+u:a\in\mathbb Z,\ |u|\le W\},
$$




$$
J_\Omega(W)=
\left\{\frac{(2a+1)\Omega-1}{2}+u:
a\in\mathbb Z,\ |u|\le W\right\}.
$$


The retained domain gives


$$
\Omega>4D,\qquad \Omega-4D\ge27.
\tag{4.1}
$$


Hence


$$
I_\Omega(2D)\cap J_\Omega(0)=\varnothing.
\tag{4.2}
$$



## 4.1 Exact core-corrected columns

Let


$$
\widetilde V=V-B^TL^{-1}X,
\qquad
p_i=3\widehat E^{-1}\widetilde V_i^{\,T}.
$$


The exact core-corrected column is


$$
\boxed{
\widehat z_i^{\,c}
=
z_i-Yp_i
+U L^{-1}Xp_i-U L^{-1}B_i.
}
\tag{4.3}
$$



This formula displays the complete LOW correction.

Put


$$
\mathsf F_H=\frac{\widehat E-E_0}{3}.
$$


Since $B\in3^6M$, the finite inverse expansion gives


$$
p_i\equiv
3R_HV_i^T
-9R_H\mathsf F_HR_HV_i^T
\pmod{27}.
\tag{4.4}
$$



The accepted finite-boundary propagation gives


$$
R_HV_i^T\in\mathcal C(\nu),
$$




$$
R_H\mathsf F_HR_HV_i^T\in\mathcal C(\nu+1)
$$


at more than the precision required in (4.4). Recall that $p\in\mathcal C(W)$ means


$$
\pi(p):=p-\operatorname{rem}_{x^D}p=x^Dq,
\qquad
\operatorname{supp}q\subseteq I_\Omega(W).
$$



Therefore


$$
p_i\in\mathcal C(\nu+1)\pmod{27}.
\tag{4.5}
$$



The complete-$F$ proof also gives


$$
L^{-1}Xp_i
\equiv \operatorname{coeff}_U\!\left(\operatorname{rem}_{x^D}p_i\right)
\pmod{27}.
\tag{4.6}
$$


Its width hypothesis holds because


$$
(\nu+1)+D=\frac{3D}{2}<\frac{\Omega-1}{2}.
$$



Substituting (4.6) into (4.3), and using $B\equiv0\pmod{27}$, proves


$$
\boxed{
\widehat z_i^{\,c}\equiv x^D\psi_i(y)\pmod{27},
\quad
\deg\psi_i\le m-D,
\quad
\operatorname{supp}\psi_i\subseteq I_\Omega(\nu+1).
}
\tag{4.7}
$$



The degree bound is the original finite one. No HIGH coordinate beyond $m$ has been introduced.

## 4.2 Incorporating the actual producer jet

Use (2.6). Since $D\ge2\cdot3^t>\kappa$, the exponent $D-\kappa$ is nonnegative. From (4.7),


$$
\frac{
R\widehat z_i^{\,c}\widehat z_j^{\,c}
-
R(-1)\widehat z_i^{\,c}(-1)\widehat z_j^{\,c}(-1)
}{y+1}
$$


is congruent modulo $27$ to


$$
x^{A-\kappa+2D}B_3(x)\psi_i(y)\psi_j(y)
=
x^H\,x^{D-\kappa}B_3(x)\psi_i(y)\psi_j(y).
\tag{4.8}
$$



The endpoint subtraction has not been suppressed without justification: it vanishes modulo $27$ because $R(-1)\equiv0\pmod{27}$. Monic division by $y+1$ commutes with reduction.

Now


$$
\deg\!\left(x^{D-\kappa}B_3(x)\right)\le D.
$$


Also,


$$
2(\nu+1)=D.
$$


Consequently,


$$
\operatorname{supp}\!\left(
x^{D-\kappa}B_3(x)\psi_i\psi_j
\right)
\subseteq I_\Omega(2D).
\tag{4.9}
$$



Finally,


$$
x^H=(y-1)^H
\equiv (y^{H/9}-1)^9\pmod{27},
\tag{4.10}
$$


and $H/9=27\Omega$. Multiplication by (4.10) preserves the support class $I_\Omega(2D)$.

Thus the complete quotient in (4.8) has no coefficient on $J_\Omega(0)$.

## 4.3 Every pole modulo $27$

For the present finite cutoff, the complete evaluation is


$$
\begin{aligned}
\mathcal M(F)\equiv{}&
[y^{r_*}]C_F
+3[y^{r_1}]C_F\\
&+9\sum_{c\in\{1,5,7,11\}}
c^{-1}[y^{(cH/3-1)/2}]C_F
\pmod{27},
\end{aligned}
\tag{4.11}
$$


where


$$
C_F=\frac{F-F(-1)}{y+1},
\quad
r_*=\frac{3H-1}{2},
\quad
r_1=\frac{H-1}{2}.
$$



All six coefficient positions in (4.11) belong to $J_\Omega(0)$:

- $3H/\Omega=729$ is odd;
- $H/\Omega=243$ is odd;
- $cH/(3\Omega)=81c$ is odd for each listed $c$.

Every one of these coefficients therefore vanishes modulo $27$ by (4.2), (4.8)–(4.10). The factorial part of the exact functional vanishes at this modulus by its established valuation.

We have proved:

### Theorem 4.1 — Complete corrected-column force localization

Under the retained original-domain and Turn 5 producer hypotheses,


$$
\boxed{
\mathcal M\!\left(R\widehat z_i^{\,c}\widehat z_j^{\,c}\right)
\equiv0\pmod{27},
\qquad 0\le i,j<\nu.
}
\tag{4.12}
$$



This theorem holds for every admissible value of the actual terminal jet. It removes that jet from the residual force at the required precision.

Using the retained Schur perturbation estimate,


$$
\boxed{\mathscr R_{\rm act}\equiv\mathscr R_c\pmod{3^9}.}
\tag{4.13}
$$



### Scope of the cancellation

The theorem does **not** establish any of the following stronger assertions:


$$
R\equiv0\pmod{27},\qquad
B_3=0,\qquad
\Phi_R=0\text{ exactly}.
$$


It establishes precisely the finite-precision disappearance of the complete evaluated force needed here.

---

# 5. Evaluating the remaining LOW and HIGH contributions on the whole-zero branch

Now impose the sharper real window


$$
\boxed{D<H/2916.}
\tag{5.1}
$$


No extra restricted-digit hypothesis is introduced.

Set


$$
\Omega'=\frac H{729}.
$$


Then


$$
\Omega'>4D.
$$


On this domain, $D$ and $\Omega'$ are both divisible by $3^t$, so


$$
\boxed{\Omega'-4D\ge3^t\ge243.}
\tag{5.2}
$$



This margin supports one additional finite return depth.

## 5.1 The LOW coupling gains one power

For $0\le a<D$ and $0\le i<\nu$, the arctangent polynomial in


$$
B_{ai}=\frac{G_c(U_a,z_i)}3
$$


is


$$
x^H x^a y^i(\beta+3y).
\tag{5.3}
$$



Its degree is at most


$$
H+D+\nu-1=H+\frac{3D}{2}-2<r_*.
$$


Thus the top pole, which could otherwise cause an additional division loss, is absent **by exact degree**.

Modulo $3^7$,


$$
x^H\equiv (y^{\Omega'}-1)^{729}.
\tag{5.4}
$$


The support of (5.3) is therefore contained in


$$
I_{\Omega'}(a+i+1)
\subseteq I_{\Omega'}(D+\nu-1).
$$


Every remaining pole capable of contributing to $G_c(U_a,z_i)/3$ modulo $3^7$ lies in $J_{\Omega'}(0)$. Moreover,


$$
D+\nu-1=\frac{3D}{2}-2<\frac{\Omega'-1}{2}.
$$


The factorial term is also zero at this precision.

Hence


$$
\boxed{B\in3^7M(\mathbb Z_3).}
\tag{5.5}
$$



In particular,


$$
J_B=B/729\equiv0\pmod3,
$$


so the **whole** LOW cross term satisfies


$$
\boxed{\mathcal K_{\rm LOW}\equiv0\pmod3.}
\tag{5.6}
$$



This is an evaluation of the LOW term, not its omission.

## 5.2 The finite HIGH return gains one power

The beta valuation, including the separately retained exceptional shifted endpoint, gives


$$
\operatorname{supp}(V_{i,\bullet}\bmod3^7)
\subseteq J_{\Omega'}(\nu).
\tag{5.7}
$$



At the required precision,


$$
(1-z)^{-A}
\equiv
(1-z)^D S(z^{\Omega'})
\pmod{3^7}.
$$


Therefore the same finite inverse formula


$$
(R_H)_{ab}=[z^{d+m-a-b}](1-z)^{-A},
\qquad d\le a,b\le m,
$$


maps the supported input into $\mathcal C(\nu)$, retaining both original boundaries.

The complete-$\mathsf F_H$ propagation now works modulo $3^6$:


$$
R_H\mathsf F_H:\mathcal C(W)\longrightarrow\mathcal C(W+1).
\tag{5.8}
$$


The precision accounting is exactly one level higher than in Turn 4:

- polynomial support is used modulo $3^7$;
- division by $3$ leaves modulus $3^6$;
- all surviving poles lie on the $\Omega'$ half-grid;
- the LOW subtraction restores the actual remainder;
- factorial terms remain beyond this precision.

For $0\le\ell\le6$, the final contraction has total width


$$
\nu+(\nu+\ell+D)=2D-2+\ell\le2D+4.
$$


By (5.2),


$$
2D+4<\frac{\Omega'-1}{2}.
$$


Thus


$$
V(R_H\mathsf F_H)^\ell R_HV^T\equiv0\pmod{3^6}
\quad(0\le\ell\le6).
\tag{5.9}
$$


For $\ell=0$, the direct inverse argument supplies the stronger modulus $3^7$.

The finite seven-term inverse expansion consequently proves


$$
\boxed{V\widehat E^{-1}V^T\equiv0\pmod{3^7}.}
\tag{5.10}
$$



Every omitted inverse term already carries a factor $3^7$. The finite upper and lower HIGH boundaries are the same as in the retained propagation lemma.

## 5.3 The whole numerator and its carries

Substitute (4.12), (5.6), and (5.10) into the complete formula (1.3):


$$
\begin{aligned}
\mathscr R_{\rm act}
\equiv{}&
G_c(Z,Z)
-9V\widehat E^{-1}V^T\\
&+3^8\mathcal K_{\rm LOW}
+3^6\Phi_R
\pmod{3^9}.
\end{aligned}
$$


Each of the last three terms is now separately proved divisible by $3^9$. Hence


$$
\boxed{\mathscr R_{\rm act}\equiv G_c(Z,Z)\pmod{3^9}.}
\tag{5.11}
$$



This stronger termwise divisibility is why division by $3^8$ is now safe. No uncomputed depth-seven carry has been discarded.

---

# 6. The actual depth-eight digit

Expand the direct core term using the exact beta moments:


$$
\begin{aligned}
G_c(z_i,z_j)\equiv
3^h\sum_{u=0}^{D}
(-1)^{D-u}\binom Du
\bigl[
\beta B_H(i+j+u)
+3B_H(i+j+u+1)
\bigr]
\pmod{3^9}.
\end{aligned}
\tag{6.1}
$$


The factorial contribution vanishes at this stated precision, not from the exact definition.

The exact residual endpoint gives


$$
i+j\le D-4.
$$


Therefore


$$
2(i+j+u)+1\le4D-7<\frac H{729},
$$


and the shifted extra-$3$ argument satisfies


$$
2(i+j+u)+3\le4D-5<\frac H{729}.
\tag{6.2}
$$



For the first beta summand to survive modulo $3^9$, its odd denominator parameter must have valuation at least $h-8$. Below $H/729=3^{h-7}$, the only positive odd multiple of $3^{h-8}$ is


$$
3^{h-8}=\frac H{2187}.
$$


Hence the only surviving shift is


$$
i+j+u=\varrho_8,\qquad
\varrho_8=\frac{H/2187-1}{2}.
\tag{6.3}
$$



The normalized beta unit is $1\pmod3$, by the retained factorial-stripping calculation reducing it to $B_{2187}(0)$. Also $\beta\equiv1\pmod3$.

The extra-$3$ beta summand has valuation at least $9$, so it does not contribute to this digit.

It follows that


$$
\boxed{
\frac{G_c(z_i,z_j)}{3^8}
\equiv
[y^{\varrho_8-i-j}](y-1)^D
\pmod3.
}
\tag{6.4}
$$



Combining (5.11) and (6.4) proves the main actual-operator statement.

### Theorem 6.1 — Actual next operator on the whole depth-seven radical

On the original indices satisfying $D<H/2916$,


$$
\mathscr R_{\rm act}\in3^8M_\nu(\mathbb Z_3),
$$


and


$$
\boxed{
\mathscr R_{\rm act}/3^8\equiv\mathcal C_8\pmod3,
\qquad
(\mathcal C_8)_{ij}
=[y^{(H/2187-1)/2-i-j}](y-1)^D,
\quad 0\le i,j<\nu.
}
\tag{6.5}
$$



The actual depth-seven radical on this branch is all of $\mathbb F_3^\nu$. Thus (6.5) evaluates its next operator without a further change of residual coordinates.

---

# 7. Transported endpoint and the true depth-eight radical

Let $W=[U\ Y]$. In the original normalization, write the actual eliminated block and coupling as


$$
E_{\rm act}=G_{\rm act}(W,W),\qquad
C_{\rm act}=G_{\rm act}(W,Z).
$$


The exact residual endpoint is


$$
\boxed{
e_{\rm res}
=
Z(-1)^T-C_{\rm act}^TE_{\rm act}^{-1}W(-1)^T.
}
\tag{7.1}
$$


This retains the actual endpoint transport.

There is no nondegenerate depth-seven complement to eliminate on the whole-zero branch. Therefore


$$
e_8=e_{\rm res},
\qquad
\boxed{e_8\bmod3=\bigl((-1)^i\bigr)_{0\le i<\nu}.}
\tag{7.2}
$$



## 7.1 Applying the accepted residue algebra at the new scale

Put


$$
g=3^t,\qquad D=2gs,\qquad
L_8=\frac H{2187g},
$$




$$
a_0=\frac{g-1}{2},\qquad
\eta_8=\frac{L_8-1}{2}.
$$


The branch $D<H/2916$ ensures that $L_8$ is a power of $3$ at least $3$, and


$$
2s<\frac{3L_8}{4}.
$$


Also


$$
\varrho_8=g\eta_8+a_0,\qquad \nu=gs-1.
$$



The actual residue classes therefore have the same exact sizes as before:


$$
n_r=s\quad(0\le r\le g-2),
\qquad
n_{g-1}=s-1.
\tag{7.3}
$$



Define


$$
(H_{0,8})_{ab}
=[z^{\eta_8-a-b}](z-1)^{2s},
$$




$$
(H_{1,8})_{ab}
=[z^{\eta_8-1-a-b}](z-1)^{2s},
\qquad 0\le a,b<s,
$$


and


$$
J_8=H_{1,8}[:,0,\ldots,s-2].
\tag{7.4}
$$



The exceptional classes $a_0+1$ and $g-1$ are coupled by the genuine


$$
s\times(s-1)
$$


matrix $J_8$. Consequently,


$$
\boxed{\mathcal C_8\text{ is singular}.}
\tag{7.5}
$$



If


$$
\rho_{0,8}=\operatorname{rank}H_{0,8},\quad
\rho_{1,8}=\operatorname{rank}H_{1,8},\quad
\rho_{J,8}=\operatorname{rank}J_8,
$$


then the accepted algebraic rank formula now describes the **actual** digit:


$$
\boxed{
\operatorname{rank}\mathcal C_8
=
\frac{g+1}{2}\rho_{0,8}
+
\left(\frac{g-1}{2}-2\right)\rho_{1,8}
+
2\rho_{J,8}.
}
\tag{7.6}
$$



The endpoint pairing on a kernel polynomial $f$ in class $r$ is


$$
\boxed{(-1)^r f(-1).}
\tag{7.7}
$$


Thus the endpoint on the next radical is explicitly transported by evaluation, not replaced by a generic nonzero vector.

## 7.2 Exact further degeneration thresholds

The same accepted finite coefficient argument gives


$$
\boxed{
\mathcal C_8=0
\quad\Longleftrightarrow\quad
D<H/8748.
}
\tag{7.8}
$$


Accordingly, on this narrower branch,


$$
\boxed{\mathscr R_{\rm act}\in3^9M.}
\tag{7.9}
$$



On


$$
D<H/6561,
$$


the trailing triangular blocks give the explicit radical and


$$
\boxed{e_8\bmod3\notin\operatorname{im}\mathcal C_8.}
\tag{7.10}
$$



These conclusions concern the stated original indices when they satisfy the displayed windows. No assertion about infinitude of any newly restricted branch is needed or made.

---

# 8. What is learned about determinants, primitive denominators, and errors

The producer scalar $\eta_n$ and the residual endpoint contraction are different quantities. The new force cancellation does not identify either with a unit.

On $D<H/2916$, the eliminated actual block still has determinant valuation $D$, by the retained LOW-unit/HIGH-unit structure and perturbation protection. If $G_{\rm act}$ is nonsingular, then


$$
v_3(\det G_{\rm act})
=
D+8\nu+v_3\det(\mathscr R_{\rm act}/3^8).
$$


Since $\mathcal C_8$ is singular,


$$
\boxed{
v_3(\det G_{\rm act})\ge D+8\nu+1
\quad\text{when }\det G_{\rm act}\ne0.
}
\tag{8.1}
$$



This is a determinant lower bound, not a primitive-denominator formula.

Restore


$$
Q_n=\lambda Q_n^{\rm loc},
\qquad \lambda\in\mathbb Z_3^\times,
$$


and


$$
R_{\rm rat}=\frac{4\lambda}{3^h}G_{\rm act},
$$




$$
H_{\rm complete}
=
R_{\rm rat}+(e+\pi)Q_n(-1)vv^T.
$$


Without assuming nonsingularity, retain the determinant pair


$$
\boxed{
\beta_0=\det R_{\rm rat},\qquad
\beta_1=Q_n(-1)v^T\operatorname{adj}(R_{\rm rat})v.
}
\tag{8.2}
$$



When $G_{\rm act}$ is nonsingular,


$$
\frac{\beta_1}{\beta_0}
=
\frac{3^hQ_n^{\rm loc}(-1)}4\,
v^TG_{\rm act}^{-1}v.
\tag{8.3}
$$


The results here do not evaluate that full inverse contraction.

For a clearing integer $\ell$, with $k=m+1$, retain


$$
A_\ell=\ell^k\beta_0,\qquad
B_\ell=\ell^k\beta_1,
$$




$$
\boxed{g_\ell=\gcd(|A_\ell|,|B_\ell|),}
\tag{8.4}
$$


including every prime.

When $B_\ell\ne0$, the actual primitive pair is


$$
q=\frac{|B_\ell|}{g_\ell},
\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


Its whole evaluated error is exactly


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell^k}{g_\ell}
\det H_{\rm complete}.
}
\tag{8.5}
$$



### No promotion beyond the proved precision

The new results do not:

- prove $B_\ell\ne0$;
- prove nonvanishing of $\det H_{\rm complete}$;
- determine $g_\ell$;
- determine $q$, even just its exact $3$-part;
- establish nonzero whole primitive errors tending to zero.

Producer nonvanishing—such as $\eta_n\ne0$ and $P_n(-1)\ne0$—does not imply any of these residual or complete-determinant nonvanishing statements.

---

# 9. The next concrete mathematical bottleneck

Two obstructions have now been separated.

## 9.1 The terminal jet is no longer the obstruction at this precision

Through modulus $3^9$, the actual producer perturbation has been removed from the complete residual by Theorem 4.1. This applies on the full $D<H/972$ domain.

Outside $D<H/2916$, the next actual operator on $\ker\mathcal C_7$ still requires evaluation of the complete core return and LOW terms. The present report does not claim to have evaluated that operator on the entire larger domain.

## 9.2 On the whole-zero branch, the next obstruction is the depth-eight radical

On $D<H/2916$, the actual depth-eight operator and endpoint are now evaluated. Since $\mathcal C_8$ is singular, the next local question is the depth-nine operator on its actual radical.

A concrete follow-on lemma can be stated without returning to an arbitrary producer polynomial.

Let $K_8$ be the integral lift of a kernel basis obtained from (7.3)–(7.4), and set


$$
J_7=B/3^7,
$$




$$
\mathcal K_{\rm LOW}^{(7)}
=
J_7^TL^{-1}X\widehat E^{-1}V^T
+
V\widehat E^{-1}X^TL^{-1}J_7.
$$


At the next precision the required complete numerator is


$$
G_c(Z,Z)-9V\widehat E^{-1}V^T
+3^9\mathcal K_{\rm LOW}^{(7)}
+3^6\Phi_R
\pmod{3^{10}}.
\tag{9.1}
$$



The immediate follow-on task is:

> **Depth-nine actual-radical lemma.**  
> Evaluate (9.1) on the finite columns $K_8$, through modulus $3^{10}$, including $\Phi_R\bmod81$, and determine the resulting operator after division by $3^9$, together with the endpoint $K_8^T\overline e_8$.

The already proved divisibilities make


$$
\frac{V\widehat E^{-1}V^T}{3^7},
\qquad
\frac{\Phi_R}{27}
$$


integral. Their next residues are not determined by the present modulus-$27$ force theorem or modulus-$3^7$ return theorem.

The challenge is no longer to guess ten producer coefficients. It is to evaluate the next complete finite operator on a now explicitly identified actual radical. A further localization argument may simplify the new force precision, but it must be proved at that precision rather than inferred from the theorem above.

Globally, even a successful local continuation would still have to be combined with same-index all-prime gcd control and a complete nonzero real-error estimate.

---

# 10. Bounded exact arithmetic for independent inspection

No finite computation is required to complete the symbolic proofs above. Two bounded certificates would nevertheless be useful. Neither is an original-index theorem.

## 10.1 Nine-digit Pascal solver certificate

### Inputs

For each $2\le n\le32$:

1. Generate $\gamma_0,\ldots,\gamma_{2n-1}$ by the exact recurrence.
2. Construct $\mathsf T_n$, $u$, and the complete force $\tau$ where applicable.
3. Compute $\mathsf T_n^{-1}u$ and $\mathsf T_n^{-1}\tau$:
   - by exact rational elimination;
   - independently by the explicit residue-Pascal action and nine lifts in (3.2).

### Expected verifiable output

- Equality of the two solutions modulo $3^9$.
- Exact preservation of the finite class sizes $m_0,m_1,m_2$.
- For $n\equiv2\pmod3$,
  

$$
(\mathsf T_n^{-1}u)_{n-1}\equiv2\pmod3.
$$


- Where the exact scalar quotient is also computed, agreement with (2.2).

No original-domain order-six congruence is to be imposed on these auxiliary small values of $n$. In particular, division by $729$ is not to be performed unless its divisibility has actually been verified for that input.

## 10.2 A complete six-pole localization certificate

This certificate tests the new force-support mechanism rather than repeating the accepted radical assembly.

### Auxiliary inputs

Take


$$
H=19683,\qquad \Omega=81,\qquad D=18,\qquad \kappa=9.
$$


Then


$$
\Omega>4D,\qquad
\nu=8,\qquad W=\nu+1=9.
$$


Set


$$
A=H-D,\quad n=A+2,\quad m=(A+1)/2.
$$


Use


$$
S=\{0,9,72,81,90,9792,9801,9810\}.
$$


Every element of $S$ lies in $I_\Omega(9)\cap[0,m-D]$.

For every


$$
0\le b\le9,\qquad s,t\in S,
$$


form the quotient polynomial


$$
C_{b,s,t}(y)
=(y-1)^{H+D-\kappa+b}y^{s+t}.
$$



### Expected verifiable output

At each of the six pole positions


$$
r_*=\frac{3H-1}{2},\quad
r_1=\frac{H-1}{2},\quad
\frac{cH/3-1}{2}\quad(c=1,5,7,11),
$$


return


$$
[y^r]C_{b,s,t}(y)\equiv0\pmod{27}.
$$



These coefficients can be computed directly as signed binomial coefficients; no large Gram matrix is needed.

The certificate has finite auxiliary scope only. It verifies the stated polynomial identities for its $640$ input triples and their six coefficient positions. It does not verify the actual producer, original-index infinitude, or a denominator/error law.

---

# 11. Final proof ledger

| Statement | Status |
|---|---|
| Turn 5 factorial saturation and exact scalar denominator | Retained with their stated hypotheses; independent review still pending |
| Explicit finite Pascal inverse action modulo $3$ | Derived here |
| Uniform finite digit lifting for the normalized system | Proved |
| Uniform bounded-state evaluation of $\xi_n$ or the terminal jet | Not proved |
| Exact original ten-coefficient jet bound modulo $27$ | Preserved |
| Complete corrected-column localization modulo $27$ | Proved from the retained inputs |
| $\Phi_R\equiv0\pmod{27}$ on $D<H/972$ | Proved |
| $\mathscr R_{\rm act}\equiv\mathscr R_c\pmod{3^9}$ | Proved |
| $B\in3^7M$ and $V\widehat E^{-1}V^T\in3^7M$ on $D<H/2916$ | Proved |
| Actual depth-eight operator $\mathcal C_8$, with original boundaries | Evaluated |
| Actual transported endpoint at depth eight | Retained exactly and evaluated modulo $3$ |
| Singularity of the actual $\mathcal C_8$ | Follows from the accepted finite residue algebra |
| First nonzero nonsingular actual residual depth | Not established |
| Actual primitive denominator and all-prime gcd | Not determined |
| Nonzero whole primitive errors tending to zero | Not established |

## Closing conclusion

The new advance is not another isolated core rank statement. It is the removal of the **actual terminal producer jet from the complete corrected-column force**, followed by an evaluation of the **actual next operator** on the whole depth-seven radical in the branch $D<H/2916$.

The resulting actual operator is $\mathcal C_8$, with the true endpoint and shortened terminal residue class retained. It is still singular. The exact remaining local bottleneck is the next complete operator on that actual depth-eight radical; the global bottleneck remains control of the actual primitive determinant pair, its full gcd, and the whole nonzero evaluated error on the same original indices.



$$
\boxed{\text{An unconditional proof or disproof of irrationality of }e+\pi
\text{ remains unresolved.}}
$$


