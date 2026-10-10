> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## Audit conclusion

The full divided-coordinate interface is valid. In particular, the projection in A1turn9 is the projection of **$\phi_N$**, not of $h_n=N!\phi_N$. Its recorded factorial expansion uses precisely that normalization. Including the constant row closes the support argument and makes the sharpened polynomial law unconditional:


$$
\boxed{
Q_n^{\rm loc}(y)=3P_n(y)
\equiv (y+1)(y-1)^{n-2}(3y-71-3M)
\pmod{3^{m+2}},
}
$$


for


$$
\boxed{M\ge1,\quad m=v_3(M)\ge2,\quad n=3M+2.}
$$



The independent weighted-matrix audit also closes the fourth carry on the stated domain. The corrected **two-edge support**, rather than one-edge support, is sufficient. Details follow.

These are local arithmetic results, not an irrationality proof for $e+\pi$.

## 1. Full force and normalization audit

Throughout this section,


$$
L=3M,\qquad N=L+1,\qquad n=N+1,\qquad
\phi_d=\frac{(y+1)(y-1)^d}{d!}.
$$


All integrality statements concern $\mathbb Z_3$, not necessarily ordinary integral polynomial coefficients.

The regular basis is


$$
1,\phi_0,\ldots,\phi_{L-1}.
$$


Its actual $\rho$-Gram matrix is


$$
A_{\rm reg}=
\begin{pmatrix}
0&t^T\\
t&E
\end{pmatrix},
\qquad
t_i=\mu(\phi_i),\quad
E_{ij}=\mu(\phi_i\phi_j).
$$


The upper-left entry is $\rho(1)=0$, not $\mu(1)=1$. Eliminating $E$ leaves


$$
a=-t^TE^{-1}t.
$$


The recorded tensor reduction gives $a\equiv-1\pmod3$. Consequently


$$
A_{\rm reg}^{-1}\in M_{L+1}(\mathbb Z_3).
$$



The **complete target force** for $\phi_N$ is


$$
f=
\begin{pmatrix}
\rho(\phi_N)\\
(\rho(\phi_i\phi_N))_{i<L}
\end{pmatrix}
=
\begin{pmatrix}
t_N\\
\bigl(\binom{i+N}{i}e_{i+N}\bigr)_{i<L}
\end{pmatrix}
\in\mathbb Z_3^{L+1}.
$$


Thus its constant row is integral as well.

Replace $\phi_L$ by


$$
r=\sum_{D=0}^{M}\tau_D\phi_{3D},
\qquad
\tau_D=(-1)^{M-D}\binom MD.
$$


Since $\tau_M=1$, this is a unimodular change of the divided-coordinate lattice. Its full regular coupling is


$$
u=
\begin{pmatrix}
\mu(r)\\
v
\end{pmatrix}.
$$


The established all-depth residual theorem gives $v\in3M\mathbb Z_3^L$. For the missing constant coupling,


$$
\mu(r)=\sum_{D=0}^M\tau_Dt_{3D}
\equiv2\sum_{D=0}^M\tau_D=0\pmod3,
$$


because $M\ge1$. Therefore


$$
\boxed{u\in3\mathbb Z_3^{L+1}.}
$$



Let the exceptional solution coefficient be $\theta/3$. The regular solution is


$$
x=A_{\rm reg}^{-1}(f-u\theta/3)\in\mathbb Z_3^{L+1}.
$$


Transforming back proves, for **every** $0\le d\le L$,


$$
\boxed{
3\eta_{d+1}\equiv
\begin{cases}
\theta\,(-1)^{M-D}\binom MD,&d=3D,\\
0,&3\nmid d
\end{cases}
\pmod3.
}
\tag{1}
$$


The exceptional coefficient remains $\eta_{\rm last}$, since the coefficient of $\phi_L$ in $r$ is one; thus $\theta=3\eta_{\rm last}$.

Finally, the monic orthogonal polynomial is exactly


$$
P_n=N!\left(\phi_N-\eta_{\rm const}
-\sum_{d=0}^L\eta_{d+1}\phi_d\right).
$$


This gives the expansion in A1turn9 without an additional factorial:


$$
P_n=h_n-N!\eta_{\rm const}
-\sum_{d=0}^L\frac{N!}{d!}\eta_{d+1}h_{d+1}.
$$


The support map therefore applies to the actual coefficients used in the polynomial formula.

**Normalization qualification.** The Schur symbols $b,c,\xi_{\rm const},\xi_{\rm last}$ in A1turn9 agree with elimination of the $\phi$-block; the constant Schur pivot uses $\rho$, while couplings involving a polynomial vanishing at $-1$ use $\mu$. Also,


$$
Q_n=(L_n/3)Q_n^{\rm loc},
\qquad L_n/3\in\mathbb Z_3^\times.
$$


There is no justification for deleting this unit when reporting the literal primitive integer polynomial.

## 2. Unconditional sharpened polynomial law

Use the already proved true-jet and projection-transfer identities:


$$
N\Theta_M\equiv68+3M\pmod{3^{m+2}},
\qquad \Theta_M=3\eta_{\rm last},
\qquad m\ge2.
\tag{2}
$$


The remaining tail verification now follows from (1).

For $d=L-1,L-2,L-3$,


$$
v_3(N!/d!)=m+1.
$$


At the first two indices, (1) gives an additional factor $3$. At $d=L-3$, it gives


$$
3\eta_{L-2}\equiv-M\theta=0\pmod3.
$$


Every $d\le L-4$ has


$$
v_3(N!/d!)\ge m+2,
$$


because the quotient contains both $L$, of depth $m+1$, and $L-3$, of depth one.

The complete constant contribution is retained:


$$
-3N!\eta_{\rm const}=3P_n(-1).
$$


Its established depth is $2v_3(N!)\ge m+2$. Hence only the leading and last exceptional terms survive, and (2) yields the boxed law above.

On the regular family,


$$
n=4^j+1,\qquad M=\frac{4^j-1}{3},\qquad v_3(M)=v_3(j).
$$


In particular, for $j=3^K w$, $K\ge2$, $w\ge1$,


$$
Q_n^{\rm loc}\equiv
(y+1)(y-1)^{n-2}(3y-71-3^{K+1}w)
\pmod{3^{K+2}}.
$$


For $27\mid j$, this supplies the weighted core


$$
Q_n^{\rm loc}\equiv(y+1)(y-1)^{n-2}(3y+10)\pmod{81}.
$$



## 3. Independent fourth-carry audit

Here the notation changes to that of A4:


$$
A=n-2=H-D,\quad H=3^{h-1},\quad
d=\frac{3D}{2}-1,\quad
\nu=\frac D2-1,\quad
m_{\!H}=\frac{A+1}{2}.
$$


I write $m_{\!H}$ to distinguish the last HIGH index from $v_3(M)$.

The domain is


$$
27\mid j,\qquad D<H/108,
$$


within the specified weighted regular family. Strip only $\lambda=L_n/3$. Use the actual all-pole functional, including the factorial functional $\mathfrak f(y^s)=(2s)!$, endpoint-subtracted division, and every pole with


$$
a3^r\le4n-3.
$$


The monomial matrix and its partition are


$$
\begin{pmatrix}3L&3X\\3X^T&E\end{pmatrix}.
$$


No positive-metric replacement of this weighted form is being made.

### 3.1 Extended annihilation evaluates the previously missing scalar

Let $\mathcal L$ be the same lower-pole functional defining $L$, extended to all required monomial indices, and let


$$
w_\nu=y^\nu(y-1)^D.
$$


For $0\le a\le d$,


$$
(y-1)^Aw_\nu y^a=y^{\nu+a}(y-1)^H,
\qquad \nu+a\le2D-2.
$$


Including the linear core increases the shift to at most $2D-1$. The four-layer half-grid argument still applies, since


$$
2D-1<\frac{H/27-1}{2}.
$$


Thus


$$
\boxed{\mathcal L(w_\nu,y^a)\equiv0\pmod{81}\quad(0\le a\le d).}
\tag{3}
$$


The same statement holds for every $z_i=y^i(y-1)^D$, $i<\nu$, against these monomials.

The top pole is absent by degree in pairs $(U,d),(Z,d),(d,d)$, where $U=(1,\ldots,y^{D-1})$. Therefore, to the required precision,


$$
X_{U,d}=\mathcal L(U,y^d),\quad
X_{Z,d}=\mathcal L(Z,y^d),\quad
E_{dd}/3=\mathcal L(y^d,y^d).
\tag{4}
$$



Divide $y^d$ by the monic polynomial $(y-1)^D$. The quotient has degree $\nu$, so


$$
y^d=p+\sum_{i<\nu}\alpha_i z_i+w_\nu,
\qquad \deg p<D.
$$


Equations (3) imply that $y^d$ and $p$ have identical pairings modulo $81$ against every monomial through degree $d$. With $L_U$ the actual unit block, this proves


$$
\mathcal L(d,d)-\mathcal L(d,U)L_U^{-1}\mathcal L(U,d)
\equiv0\pmod{81}.
\tag{5}
$$


Since $(E_0)_{dd}=0$, (4)–(5) evaluate the actual carry:


$$
\boxed{F_{dd}/3\equiv0\pmod3.}
\tag{6}
$$



Also $V_d=Z^TX_d\equiv0\pmod{81}$. In


$$
V=-2ee_{m_{\!H}}^T+3K+9J,
$$


we have $Ke_d=0$, so


$$
\boxed{Je_d=0\pmod3.}
\tag{7}
$$



### 3.2 Actual two-edge support of $Fe_d$

The top perturbation is


$$
\frac{E_{\rm top}-E_0}{3}
\equiv [y^{r_*}](y-1)^A(y+3)y^{a+b}\pmod3.
$$


At $b=d$, its entry vanishes unless $a\ge m_{\!H}-1$, because


$$
r_*=A+d+m_{\!H}.
$$


Thus its support is contained in the last **two** HIGH coordinates.

For the lower contribution after eliminating $U$, use the same division of $y^d$. Modulo $3$,


$$
(y-1)^Az_i=y^i(y^H-1).
$$


For every HIGH $b\le m_{\!H}$ and $i<\nu$,


$$
i+b\le(H-3)/2<(H-1)/2,
$$


so $z_i$ annihilates the first lower-pole form. For $w_\nu$, equality with the first lower pole occurs only at $b=m_{\!H}$. All deeper lower layers vanish modulo $3$. Consequently the lower Schur contribution is supported only at $m_{\!H}$.

Together,


$$
\boxed{Fe_d\in
\operatorname{span}_{\mathbb F_3}(e_{m_{\!H}-1},e_{m_{\!H}}).}
\tag{8}
$$


The stronger one-edge statement is neither needed nor asserted.

### 3.3 Inverse orientation and the remaining contractions

The correctly oriented inverse is


$$
R_{ab}=[z^{d+m_{\!H}-a-b}](1-z)^{-A}.
\tag{9}
$$


In particular,


$$
Re_{m_{\!H}}=e_d,\qquad
Re_{m_{\!H}-1}=e_{d+1}+Ae_d.
$$


The index gap gives $Ke_d=Ke_{d+1}=0$. Hence (8) implies


$$
\boxed{KRFe_d=0\pmod3.}
\tag{10}
$$


All entries of $R$ among its last two indices are zero, by the negative-degree convention in (9). Since $F$ is symmetric,


$$
\boxed{(FRF)_{dd}=0\pmod3.}
\tag{11}
$$



Finally, the potentially selected coefficient in $KRK^T$ has degree


$$
\frac{H+3}{6}+D+i+j,\qquad 0\le i,j<\nu.
$$


It lies strictly between $D$ and $H$. But


$$
(1-z)^{-A}=\frac{(1-z)^D}{1-z^H}\quad\text{over }\mathbb F_3,
$$


whose coefficients in that interval vanish. Therefore


$$
\boxed{KRK^T=0.}
\tag{12}
$$



Substitution of (6), (7), (10), (11), and (12) into A4turn15’s fourth-carry formula gives


$$
\boxed{T_4=0\quad\text{over }\mathbb F_3.}
$$


The signs and inverse orientation in that formula are consistent. Restoring $\lambda$ multiplies the form by a unit and leaves rank zero unchanged.

## 4. Arithmetic consequences and limitations

The direct matrix consequence is


$$
v_3(\det S)\ge4\nu,\qquad
v_3(\operatorname{adj}(S)_{\rm endpoint})\ge4\nu-4.
$$


Under the recorded complete-pair normalization identity, this gives


$$
v_3(g)\ge d+4\nu=\frac{7D}{2}-5.
$$


It does **not** give an exact denominator.

For the actual cleared complete pair retain


$$
g=\gcd(|A_{\rm det}|,|B_{\rm det}|),\qquad
q=\frac{|B_{\rm det}|}{g},\qquad
p=-\frac{\operatorname{sgn}(B_{\rm det})A_{\rm det}}g.
$$


Where $B_{\rm det}\ne0$,


$$
q(e+\pi)-p
=\frac{\operatorname{sgn}(B_{\rm det})}{g}
\bigl(A_{\rm det}+B_{\rm det}(e+\pi)\bigr)
=\frac{\operatorname{sgn}(B_{\rm det})\ell^k}{g}
\det H_{\rm complete},
\qquad k=(n+1)/2.
$$


The primitive multiplier is the displayed full clearer divided by the **final** gcd. Polynomial endpoint nonvanishing is retained:


$$
Q_n(-1)\ne0,\qquad
v_3(Q_n(-1))=2v_3((n-1)!).
$$


Neither this fact nor fourth-rank zero independently proves complete-response nonvanishing, whole-error nonvanishing, or shrinking of the whole primitive error.

## Closing ledger

1. **New result and proof status.** The complete constant-row force and divided-coordinate normalization close the full support map. The sharpened polynomial law is unconditional for $v_3(M)\ge2$. Independent actual-entry calculations evaluate every fourth-carry term and prove $T_4=0$ on $27\mid j,\ D<H/108$.

2. **Exact remaining bottleneck.** The next weighted saturation requires a new actual digit and its unit-elimination corrections; fourth-rank zero is not an all-depth recurrence. For irrationality, the unresolved requirement remains compatible control of the final reduced denominator and nonzero **whole primitive errors tending to zero** on an infinite family.

3. **Computation request.** None. The new support and fourth-carry conclusions follow from symbolic identities and uniform precision bounds, not finite rank evidence.
