> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## Verdict

On the weighted index domain


$$
\boxed{n=4^j+1,\qquad 27\mid j,\qquad 0<D=H-(n-2)<H/108,}
$$


with the definitions of $H,h,d,m,\nu$ in the question, **the fourth carry is zero**. In fact, the actual entries give the more explicit identity


$$
\boxed{Fe_d=e_{m-1}+2e_m\pmod3.}
$$


Thus the coordinator’s corrected two-edge statement is sufficient, whereas the earlier one-edge statement is false for these stripped-unit matrices.

The resulting fourth-depth conclusions are


$$
\boxed{
T_4=0,\qquad
\overline e_{\rm rad}=((-1)^i)_{0\le i<\nu}\notin\operatorname{im}T_4,
}
$$


and


$$
\boxed{
v_3(g)\ge d+4\nu=\frac{7D}{2}-5.
}
$$


This is a lower bound for the **final coefficient-pair gcd**, not an evaluation of the reduced denominator.

The independent audit of A3 turn16 also passes on its stated domain $3\le b=o(n^{2/3})$, for the actual columns and positive diagonal metrics specified there. No assertion at $b\asymp n^{2/3}$, or beyond, is needed for that audit.

---

## 1. Full divided-coordinate force: the normalization agrees

For this paragraph only, use A1’s notation


$$
L=3M,\qquad N=L+1,\qquad
\phi_d=(y+1)(y-1)^d/d!.
$$


The target in the divided-coordinate projection is indeed $\phi_N$: dividing A1’s monic expansion by $N!$ gives exactly


$$
\frac{P_n}{N!}
=\phi_N-\eta_{\rm const}
-\sum_{d=0}^{L}\eta_{d+1}\phi_d.
$$


There is no additional factorial in the force or in its solution coordinates.

The full regular block on


$$
1,\phi_0,\ldots,\phi_{L-1}
$$


has an integral inverse: eliminating the integral unit matrix $E$ leaves the unit constant pivot $a$. Its full $\phi_N$-force is integral, including the constant row, because


$$
\rho(\phi_N)=\mu(\phi_N)=t_N\in\mathbb Z_3
$$


and all divided Gram entries are integral.

Replace $\phi_L$ by


$$
r=\sum_{D'=0}^{M}\tau_{D'}\phi_{3D'},
\qquad
\tau_{D'}=(-1)^{M-D'}\binom M{D'}.
$$


This is unimodular in the divided lattice since $\tau_M=1$. Its couplings to the regular $\phi$-coordinates vanish modulo $3$, by the Pascal residual identity supplied in A1. Its constant coupling also vanishes:


$$
\rho(r)=\mu(r)
\equiv2\sum_{D'=0}^{M}\tau_{D'}=0\pmod3.
$$


Consequently the **entire** regular-to-exceptional column is divisible by $3$.

If the exceptional solution coordinate is $\theta/3$, the regular solution is


$$
x=A_{\rm reg}^{-1}(f-u\theta/3)\in\mathbb Z_3.
$$


Transforming back therefore proves, for every $0\le d\le L$,


$$
3\eta_{d+1}\equiv
\begin{cases}
\theta(-1)^{M-D'}\binom M{D'},&d=3D',\\
0,&3\nmid d
\end{cases}
\pmod3.
$$


This closes the full-force coordinate interface.

In particular, for $v_3(M)\ge2$, the three dangerous factorial-tail coordinates are killed as stated in A1 turn17: two are off support and the third has coefficient $-M\theta$. Together with the supplied jet and projection bounds, this gives the sharpened local ray


$$
Q_n^{\rm loc}=3P_n
\equiv(y+1)(y-1)^{n-2}(3y-71-3M)
\pmod{3^{v_3(M)+2}}.
$$


On $27\mid j$, $v_3(M)=v_3(j)\ge3$, so in particular


$$
\boxed{Q_n^{\rm loc}\equiv(y+1)(y-1)^A(3y+10)\pmod{81}.}
$$


The actual primitive polynomial remains


$$
Q_n=\lambda Q_n^{\rm loc},\qquad
\lambda=L_n/3\in\mathbb Z_3^\times.
$$



---

## 2. Actual block entries and precision after division

Return to A4’s notation


$$
A=n-2=H-D,\quad
d=\frac{3D}{2}-1,\quad
\nu=\frac D2-1,\quad
m=\frac{A+1}{2},
$$


and strip only $\lambda$. Let


$$
C_{ab}(y)=
\frac{Q_n^{\rm loc}(y)y^{a+b}
-Q_n^{\rm loc}(-1)(-1)^{a+b}}{y+1}.
$$


The full matrix is given by the exact functional in the question:


$$
\mathcal M(Q_n^{\rm loc}y^{a+b})
=-\frac{3^h}{4}\mathfrak f(Q_n^{\rm loc}y^{a+b})
+\sum_{r=0}^{h}\ 
\sum_{\substack{c\ge1\ {\rm odd}\\3\nmid c\\c3^r\le4n-3}}
3^{h-r}c^{-1}[y^{(c3^r-1)/2}]C_{ab}.
$$


Every cutoff here is the original $c3^r\le4n-3$.

Define $L_{\rm ext}$ by removing the top-pole contribution and dividing the remainder by $3$. Modulo $81$, its four lower layers have weights $1,3,9,27$, and use respectively the complete admissible poles at depths $h-1,h-2,h-3,h-4$. The factorial term has depth $h-1\ge4$ after division on the present domain.

The top layer has only $c=1$. Put


$$
r_*=(3H-1)/2,\qquad P=(y-1)^A(3y+10).
$$


Endpoint-subtracted division preserves the congruence $C_{ab}\equiv Py^{a+b}\pmod{81}$.

An important precision point is that the top contribution is **identically absent**, by degree, in the pairs


$$
(U,d),\quad(Z,d),\quad(d,d).
$$


Thus no division of an unknown modulo-$81$ top coefficient is being performed. The exact identities are


$$
X_{U,d}=L_{\rm ext}(U,d),\qquad
V_d=Z^TX_d=L_{\rm ext}(Z,d),\qquad
E_{dd}/3=L_{\rm ext}(d,d).
$$


Also, the top contribution is absent in every $U$-HIGH pair: here $a\le D-1\le d-2$, so


$$
A+1+a+b<r_*,\qquad b\le m.
$$


Hence $X_U=L_{\rm ext}(U,\mathrm{HIGH})$.

These identities retain both the exact endpoint subtraction and the complete factorial contribution.

---

## 3. Extended annihilation evaluates $F_{dd}/3$ and $Je_d$

Set


$$
w_\nu=y^\nu(y-1)^D.
$$


For $0\le a\le d$,


$$
(y-1)^Aw_\nu y^a=y^{\nu+a}(y-1)^H,
\qquad \nu+a\le2D-2.
$$


Including the linear core raises the maximum shift to $2D-1$.

At the four retained lower layers, the required binomial grids are


$$
H/27,\quad H/9,\quad H/3,\quad H.
$$


Every admissible pole index is separated from the relevant grid by at least


$$
(H/27-1)/2.
$$


The strict inequality $D<H/108$, with integer shifts, excludes all these coefficients. This argument treats every admissible pole, not just the nearest ones. Therefore


$$
L_{\rm ext}(w_\nu,y^a)=0\pmod{81},
\qquad 0\le a\le d.
$$


The same holds with $w_\nu$ replaced by every $z_i$, $i<\nu$.

The monic polynomial $w_\nu$ can be written


$$
w_\nu=y^d+u+Zc,\qquad u\in U.
$$


Let $l=L_{\rm ext}(U,d)$. Pairing with $U$ gives


$$
u=-L_U^{-1}l\pmod{81},
$$


because $Z$ annihilates $U$. Pairing with $y^d$ now yields


$$
L_{\rm ext}(d,d)-l^TL_U^{-1}l=0\pmod{81}.
$$


Since $(E_0)_{dd}=0$,


$$
F_{dd}
=\frac{\widehat E_{dd}}3
=L_{\rm ext}(d,d)-l^TL_U^{-1}l.
$$


In particular,


$$
\boxed{F_{dd}/3=0\pmod3.}
$$



Likewise the direct extended annihilation gives


$$
V_d=0\pmod{81}.
$$


In


$$
V=-2ee_m^T+3K+9J
$$


both $e_m^Te_d$ and $Ke_d$ vanish. Thus $9Je_d=V_d$, and


$$
\boxed{Je_d=0\pmod3.}
$$



---

## 4. Actual two-edge support, with its coefficients

Here only modulo $3$ is required.

### 4.1 Lower contribution

Modulo $3$, the extended lower functional is


$$
L_{\rm ext}(f,g)
=[y^{r_1}](y-1)^Afg,\qquad r_1=(H-1)/2.
$$


For $b\le m-1$,


$$
\nu+b\le r_1-1,
$$


and therefore


$$
L_{\rm ext}(w_\nu,y^b)=0.
$$


For every $i<\nu$, the same argument gives


$$
L_{\rm ext}(z_i,y^b)=0,\qquad b\le m,
$$


because $i+m\le r_1-1$.

At $b=m$, however, $\nu+m=r_1$, so


$$
L_{\rm ext}(w_\nu,y^m)
=[y^{r_1}]y^{r_1}(y^H-1)=-1.
$$


Using $w_\nu=y^d+u+Zc$ and the previously determined $u$, this evaluates the lower Schur response:


$$
\left(
L_{\rm ext}(\mathrm{HIGH},d)
-X_U^TL_U^{-1}l
\right)
=-e_m\pmod3.
$$



### 4.2 Top contribution

The actual top perturbation is


$$
\frac{E_{\rm top}-E_0}{3}
=[y^{r_*}](y-1)^A(y+3)y^{a+b}\pmod3.
$$


At column $d$, degree excludes all rows below $m-1$. At the last two rows its values are


$$
1\quad(a=m-1),\qquad -A\quad(a=m).
$$


Combining top and lower contributions gives


$$
Fe_d=e_{m-1}+(-A-1)e_m\pmod3.
$$


Since $3\mid A=4^j-1$,


$$
\boxed{Fe_d=e_{m-1}+2e_m\pmod3.}
$$


Thus a genuine $m-1$ edge survives in $Fe_d$, but it does not survive in the fourth carry.

---

## 5. Inverse orientation and all four terms in $(*)$

Let


$$
(E_0)_{ab}=[y^{r_*}](y-1)^Ay^{a+b},
\qquad d\le a,b\le m.
$$


Because $r_*-A=d+m$, its reversed triangular coefficient sequence is that of $(1-z)^A$. Multiplication of triangular coefficient matrices therefore gives the exact inverse formula


$$
\boxed{
R_{ab}=[z^{d+m-a-b}](1-z)^{-A},
}
$$


with negative degrees interpreted as zero.

In particular,


$$
Re_m=e_d,\qquad
Re_{m-1}=e_{d+1}+Ae_d.
$$


Modulo $3$, $A=0$, hence the two-edge space maps into
$\langle e_d,e_{d+1}\rangle$. The index bound


$$
i+d+1\le2D-2<r_2,\qquad r_2=(H/3-1)/2,
$$


shows that $K$ annihilates both these coordinates. Therefore


$$
\boxed{KRFe_d=0.}
$$



All entries of $R$ among rows and columns $m-1,m$ vanish: their coefficient degrees are negative, since $m-d>2$ here. By symmetry of $F$,


$$
(FRF)_{dd}=(Fe_d)^TR(Fe_d)=0.
$$



Finally, a potentially nonzero entry of $KRK^T$ has coefficient degree


$$
t=d+m-2r_2+i+j
=\frac{H+3}{6}+D+i+j.
$$


For $0\le i,j<\nu$, this lies strictly between $D$ and $H$. In characteristic $3$,


$$
(1-z)^{-A}
=\frac{(1-z)^D}{1-z^H},
$$


whose coefficients in that interval vanish. Hence


$$
\boxed{KRK^T=0.}
$$



Every term of $(*)$ is now evaluated:


$$
KRK^T=0,\qquad
Je_d=0,\qquad
KRFe_d=0,\qquad
(FRF)_{dd}=F_{dd}/3=0.
$$


Consequently


$$
\boxed{T_4=0.}
$$



---

## 6. Endpoint, primitive unit, final gcd, and whole error

The elimination corrections to the radical endpoint vector are divisible by $3$. Thus its actual residue remains


$$
\overline e_{\rm rad}
=\bigl(z_i(-1)\bigr)_{i<\nu}
=\bigl((-1)^i(-2)^D\bigr)_{i<\nu}
=\bigl((-1)^i\bigr)_{i<\nu}\ne0.
$$


Since $T_4=0$, this vector is outside its image. Restoring $\lambda$ multiplies the carry by a unit and changes neither conclusion.

All $\nu$ residual Smith factors of the LOW Schur matrix are now divisible by $81$. Hence


$$
v_3(\det S)\ge4\nu,\qquad
v_3(\operatorname{adj}(S)_{ab})\ge4(\nu-1).
$$


The supplied complete determinant normalization, including


$$
v_3(Q_n(-1))=2v_3((n-1)!),\qquad Q_n(-1)\ne0,
$$


then gives


$$
\boxed{v_3(g)\ge d+4\nu=\frac{7D}{2}-5.}
$$



Explicitly, retain


$$
A_{\rm det}=\det T,\qquad
B_{\rm det}=\ell Q_n(-1)\det K,
$$




$$
g=\gcd(|A_{\rm det}|,|B_{\rm det}|),\quad
q=\frac{|B_{\rm det}|}{g},\quad
p=-\frac{\operatorname{sgn}(B_{\rm det})A_{\rm det}}g.
$$


On the complete-response nonvanishing domain $B_{\rm det}\ne0$,


$$
\boxed{
q(e+\pi)-p
=\frac{\operatorname{sgn}(B_{\rm det})\ell^k}{g}
\det H_{\rm complete},\qquad k=(n+1)/2.
}
$$


The exact denominator interface still involves the **transported endpoint cofactor**:


$$
v_3(q)=\max\!\left\{0,\,
h+2v_3((n-1)!)-1+
v_3(\operatorname{adj}(S)_{\rm endpoint})
-v_3(\det S)\right\}.
$$


The new lower bounds cannot be subtracted to evaluate it. Complete-response and whole-error nonvanishing are inherited regular-family inputs, not consequences of rank zero.

The stated subclass is infinite by irrational rotation restricted to $27\mid j$, using a closed ratio interval inside $1<H/A<108/107$.

---

## 7. Independent audit of A3 turn16

The crucial new steps pass:

* The exact gamma normalization gives $\sup|S_j-1|=O(d/n)$, uniformly in every actual coordinate and on all circle sectors.
* At each positive real anchor, reflection gives zero mean phase. Together with the actual Hessian bound, it yields
  

$$
\mathbb E_q[S_je^{i\Phi_q}]=1+O(d/n).
$$


  Thus the logarithmic-derivative denominator is genuinely bounded away from zero.
* The pointwise identity
  

$$
|e^{-it}+M|=M|e^{-it}+\rho|
$$


  cancels the absolute partition exactly. No $e^{O(d^2/n)}$ comparison loss enters.
* In the differentiated integral, the constant term cancels against the entire denominator. The trace term is $O(d/n)$, by covariance with the retained phase; the quadratic remainder is $O(d^2/n)$. This proves the stated anchor derivative estimate.
* Substitution into the scalar saddle expansion incurs $O(d^3/n^2)$. The leading quadratic corrections cancel because
  

$$
(1+M)^2\alpha_+=(1+\rho)^2\alpha_-.
$$


* The outer sectors, remote scalar arcs, and both minus connectors retain their supplied exponential bounds. The complete exponential residual and the coordinate-zero endpoint remain factorially smaller than the main error.

Accordingly, on $3\le b=o(n^{2/3})$,


$$
c_W-(e+\pi)
=(-1)^{n+1}4\pi M^{-2n-b}
\left[1+O\!\left(\frac{b^3}{n^2}+\frac bn+n^{-1/5}\right)\right],
$$


uniformly for every positive diagonal metric in the **actual coordinates**. The actual determinant, first-column coordinates, and whole errors are eventually nonzero.

For rational metrics, retain the least two-column clearing multiplier $d_B$, the integral metric $\Omega$, and


$$
A_B=N_{B,1}^T\Omega N_{B,1},\quad
H_B=N_{B,1}^T\Omega N_{B,2},\quad
g_B=\gcd(A_B,|H_B|),
$$




$$
q_B=A_B/g_B,\qquad p_B=H_B/g_B.
$$


The primitive multiplier is $d_B^2/g_B$, and the whole error is


$$
q_B(e+\pi)-p_B
=(-1)^n4\pi q_BM^{-2n-b}(1+o(1))\ne0.
$$


This audit does not extend the law to the critical $2/3$ scale; that would require the sharper derivative remainder estimates proposed in the coordinator note.

## Closing ledger

1. **New result and proof status.** The actual fourth carry is proved zero on $27\mid j,\ D<H/108$. Its endpoint image is evaluated, and the final-gcd lower bound improves to $d+4\nu$. The actual two-edge force is explicitly $e_{m-1}+2e_m\pmod3$. A3 turn16 passes within its stated metric and index scope.

2. **Exact remaining bottleneck.** Rank zero forces further saturation; it does not determine the relative distinguished-cofactor depth or the actual primitive denominator. Irrationality requires compatible control of that denominator and nonzero whole evaluated errors on one infinite family. Neither construction currently supplies it. No proof or disproof of irrationality of $e+\pi$ follows.

3. **Computation request.** None. The fourth carry has been evaluated symbolically from the complete actual entries; no finite rank calculation is needed.
