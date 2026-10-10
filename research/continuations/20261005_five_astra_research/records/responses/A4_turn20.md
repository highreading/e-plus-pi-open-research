> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 — fifth carry evaluation and independent signed-cubic audit

## Verdict

On the smaller weighted domain


$$
\boxed{
n=4^j+1,\qquad j>0,\qquad81\mid j,\qquad
0<D=H-(n-2)<H/972,
}
\tag{1}
$$


the proposed contractions do close:


$$
\boxed{A_9/3=0\pmod3,\qquad A_{27}=0\pmod3,\qquad T_5=0.}
\tag{2}
$$


The support arguments require the actual lower functional, including paired poles. Below I evaluate those supports rather than imposing them as hypotheses.

The independent audit of A3turn18 also passes: its signed $C_3$ estimate and algebraic derivative covariance retain the actual insertion and the actual complex denominator. Its subcritical conclusion remains scoped to


$$
3\le b=o(n^{3/4})
$$


and positive diagonal metrics in the actual coordinates.

I additionally check the proposed critical-scale virial coefficients and their moment errors. These checks do not use a presumed critical-$3/4$ theorem. I distinguish them from the complete critical-scale scalar-contour conclusion.

Neither result determines the actual primitive denominator or decides irrationality of $e+\pi$.

---

# 1. Weighted domain, precision, and small-index qualifications

Throughout the arithmetic calculation set


$$
A=n-2=H-D,\quad H=3^{h-1},\quad
d=\frac{3D}{2}-1,\quad \nu=\frac D2-1,\quad
m=\frac{A+1}{2},
$$


and


$$
r_1=\frac{H-1}{2},\qquad
r_2=\frac{H/3-1}{2},\qquad
r_*=\frac{3H-1}{2}.
$$


The actual columns are


$$
1,y,\ldots,y^m,
$$


with LOW indices $0\le a<d$, HIGH indices $d\le a\le m$, unit LOW space


$$
U=\langle1,\ldots,y^{D-1}\rangle,
$$


and radical lifts


$$
z_i=y^i(y-1)^D,\qquad0\le i<\nu.
$$



Here $D$ is even. There is no empty-radical exception on (1). Indeed $j\ge81$, and


$$
v_3(A)=1+v_3(j)\ge5.
$$


Also $H>A$ is much larger than $3^5$. Thus $3^5\mid D$, and, since $D>0$ is even,


$$
D\ge486,\qquad \nu>0.
\tag{3}
$$


In particular all HIGH edge coordinates used below exist and are distinct.

The stronger margin needed for extended tests is automatic:


$$
4D+5<H/81.
\tag{4}
$$


For $D<H/972$, the difference between $H/81$ and $4D$ is greater than $2H/243$; (3) makes this greater than $5$. We will also use


$$
2D+3<H/6,\qquad m-d>4.
\tag{5}
$$



The domain is infinite. On $j=81k$, irrational rotation by $81\log_3 4$ visits every fixed nonempty interval of fractional parts infinitely often. Taking a closed ratio interval inside


$$
1<H/A<972/971
$$


gives (1) for infinitely many $k$; the distinction between $4^j$ and $4^j-1$ tends to zero and does not affect an interior interval.

Strip only the primitive unit


$$
Q_n=\lambda Q_n^{\rm loc},\qquad
\lambda=L_n/3\in\mathbb Z_3^\times.
$$


Write


$$
\beta=-71-3M_0,\qquad M_0=(4^j-1)/3.
$$


The available actual core remains


$$
Q_n^{\rm loc}
=(y+1)(y-1)^A(\beta+3y)+729R_0,
\qquad R_0\in\mathbb Z_3[y].
\tag{6}
$$


It is this congruence, not a prematurely reduced core, that is used before any division.

The complete functional is the supplied factorial-and-all-pole functional, with endpoint subtraction and cutoff $c3^r\le4n-3$. All following congruences refer to that functional, not a selected-pole form.

---

# 2. Extended annihilation and negligible LOW-force corrections

Introduce


$$
w_i=y^i(y-1)^D,\qquad0\le i\le\nu+2.
$$


For $0\le a\le d+2$,


$$
i+a\le2D+2
$$


at the largest rectangular corner. For the divisions of $y^d,y^{d+1},y^{d+2}$, the relevant triangular test ranges require shifts at most $2D+1$ before the linear core, and at most $2D+2$ after it. Both are covered by (4).

The accepted beta valuation therefore extends to these tests. Explicitly, for the largest shift $s\le2D+2$,


$$
2s+1\le4D+5<H/81,
$$


so the divided rational beta contribution lies in $243\mathbb Z_3$. The divided factorial term is equally deep. The error in (6), including its endpoint-subtracted quotient, loses at most one power of $3$, and hence is still in $243\mathbb Z_3$.

The top pole is absent in the extended small-index pairings: even at $d+2,d+2$, the degree after endpoint-subtracted division is at most


$$
A+1+2(d+2)=H+2D+3<r_*.
$$


Consequently the required extended lower pairings vanish modulo $243$.

Monic division by $(y-1)^D$ now gives, for $k=0,1,2$,


$$
y^{d+k}=r_k(y)+(y-1)^Dq_k(y),
\qquad \deg r_k<D,\quad\deg q_k=\nu+k.
\tag{7}
$$


Pairing (7) with $U$ identifies the lower projection modulo $243$. Pairing again with the first three HIGH coordinates yields a zero lower Schur corner modulo $243$. In particular,


$$
F_{dd}\in243\mathbb Z_3,\qquad
F_{\{d,d+1\},\{d,d+1\}}=0\pmod3.
\tag{8}
$$


Likewise,


$$
V_d,V_{d+1},V_{d+2}\in243\mathbb Z_3^\nu.
\tag{9}
$$


Since the endpoint corner and $K$ vanish in these columns,


$$
Je_d,Je_{d+1}\in27\mathbb Z_3^\nu.
\tag{10}
$$



For completeness, let


$$
B=Z^TLU,\qquad C=Z^TLZ.
$$


Then $B,C$ have entries in $243\mathbb Z_3$. LOW-first elimination gives the exact residual expression


$$
C-BL_U^{-1}B^T
-3\bigl(V-BL_U^{-1}X_U\bigr)
\widehat E^{-1}
\bigl(V-BL_U^{-1}X_U\bigr)^T.
\tag{11}
$$


The first quadratic correction is in $3^{10}\mathbb Z_3$. Changes to the HIGH quadratic expression contain the additional factor $3B$, and are in $729\mathbb Z_3$. Thus, at the fifth precision,


$$
\boxed{\mathcal R\equiv-3V\widehat E^{-1}V^T\pmod{243}.}
\tag{12}
$$


This proves, rather than presumes, that the $Z^TLU$ corrections are negligible.

---

# 3. Independent inverse expansion

Use the exact definitions


$$
\widehat E=E_0+3F,\qquad R=E_0^{-1},
$$


and


$$
V=-2ee_m^T+3K+9J,
\tag{13}
$$


where $e$ is the **last standard radical vector**, not the endpoint vector.

The inverse expansion needed modulo $81$ is


$$
\widehat E^{-1}
=R-3RFR+9RFRFR-27RFRFRFR\pmod{81}.
\tag{14}
$$


Using


$$
Re_m=e_d,\quad R_{mm}=0,\quad Ke_d=0,
$$


direct multiplication gives


$$
V\widehat E^{-1}V^T
=9A_9+27A_{27}-12F_{dd}ee^T\pmod{81},
$$


with exactly the two expressions in the question. The last term vanishes by (8).

In particular, the signs and coefficients


$$
+2\operatorname{Sym}(e,KRF e_d),\quad
-2\operatorname{Sym}(e,KRFRF e_d),\quad
-4(FRFRF)_{dd}ee^T
$$


are correct. No independent coupling array is needed: all further coupling digits are already in the actual integral $J$.

Together with (12),


$$
T_5=-\bigl(A_9/3+A_{27}\bigr)\pmod3.
\tag{15}
$$



---

# 4. Evaluation of $A_9/3$

## 4.1 $KRK^T=0\pmod9$

The exact inverse orientation is


$$
R_{ab}=[z^{d+m-a-b}](1-z)^{-A}.
\tag{16}
$$


Below degree $H$,


$$
(1-z)^{-A}
\equiv(1-z)^D
\left(1+3z^{H/3}-3z^{2H/3}\right)\pmod9.
\tag{17}
$$


The degrees selected by $KRK^T$ are


$$
t=D+\frac{H+3}{6}+i+j,\qquad0\le i,j<\nu.
$$


They satisfy


$$
D<t<H/3.
$$


Indeed $t\le H/6+2D-7/2<H/3$. Equation (17) has no coefficient in that interval. Hence


$$
\boxed{KRK^T=0\pmod9.}
\tag{18}
$$



## 4.2 Actual modulo-$9$ support of $Fe_d$

Put $w=Fe_d$. The top perturbation in this column has support only at $m-1,m$, modulo $9$: the core is linear, and (6) controls the divided error.

It remains to check the full lower Schur column. By (7), modulo $243$ it is a linear combination of


$$
L_{\rm ext}(w_i,y^b),\qquad0\le i\le\nu.
\tag{19}
$$


Modulo $9$, put $s=i+b$. The first pole uses


$$
(y-1)^H=y^H-1+3y^{H/3}-3y^{2H/3}\pmod9.
$$


Since $s\le\nu+m=r_1$, its only possible lower contributions have


$$
s=r_1,\quad r_1-1,\quad r_2.
\tag{20}
$$


Here the $r_1-1$ term comes from the linear core; its product with an interior coefficient already divisible by $3$ is zero modulo $9$.

At depth $h-2$, the weight is $3$, so only the endpoint grid $y^H-1$ is needed. The only possible lower shift in the present range is $r_2$, represented by $c=1$ and $c=7$. Both poles are within the original cutoff, and their opposite coefficient signs cancel because


$$
7^{-1}-1=0\pmod3.
$$


No other unit index reaches the range. Thus (20) is a covering support for the **complete** lower contribution.

Translating back to HIGH indices, (19) has support only at


$$
m-1,m,\qquad b=r_2-i,\quad0\le i\le\nu.
\tag{21}
$$


The two upper shifts in (20) give only the two stated edges, because $r_1=\nu+m$.

Choose an integral edge-supported $u$ with


$$
w=u+3v.
$$


The established $w\bmod3$ ensures this is possible. The calculation above proves that $v\bmod3$ is supported in (21); it is not an assumption about a lift.

For an edge vector, $KRu=0$ exactly, since its inverse images lie in $d,d+1$, which $K$ kills. For a nonedge band $b=r_2-t$, the coefficient degrees selected by $KR$ are


$$
D+\frac{H+3}{6}+i+t,\qquad0\le t\le\nu.
$$


These lie strictly between $D$ and $H$; the characteristic-$3$ inverse has zero coefficients there. Hence


$$
KRv=0\pmod3,
\qquad
\boxed{KRFe_d/3=0\pmod3.}
\tag{22}
$$



The support (21) is disjoint from $d,d+1$, apart from the already separated far edges; thus $v_d=v_{d+1}=0\pmod3$. Since $Ru$ is supported at $d,d+1$, and $R$ vanishes among its last two coordinates,


$$
w^TRw
=6u^TRv+9v^TRv
$$


is divisible by $9$. Therefore


$$
\boxed{(FRF)_{dd}/3=0\pmod3.}
\tag{23}
$$



Finally (10) makes $Je_d/3=0\pmod3$. Equations (18), (22), and (23) evaluate every term:


$$
\boxed{A_9/3=0\pmod3.}
\tag{24}
$$



---

# 5. Evaluation of $A_{27}$

## 5.1 Actual support of $J\bmod3$

Compute $V$ modulo $27$ using the actual core. At this precision


$$
\beta=10\pmod{27}.
$$


The error from (6), after the coupling division, is in $243\mathbb Z_3$ and cannot affect the calculation.

For $s=i+b$, $i<\nu$, we have $s\le r_1-1$.

* **Top pole:** it gives precisely $ee_m^T$. Only the leading linear-core term can reach $r_*$.
* **First lower pole:** the complete modulo-$27$ grid has spacing $H/9$. The $k=0$ linear-core term gives $-3ee_m^T$. The $k=3,a=0$ term gives $3\beta K=3K\pmod{27}$. All other possible contributions are supported at
  

$$
b=r_1-kH/9-i-a,\quad k=1,2,3,4,\quad a=0,1.
  \tag{25}
$$


  Grids with $k\ge5$ would require a negative shift.
* **Depth $h-2$:** modulo $9$, include both endpoints and both interior $H/3$-grid points. Endpoint contributions pair $c,c+6$; the surviving possible divided residues are at $s=r_2$. Interior contributions can reach $r_2$ or $r_1$; the latter is outside $s\le r_1-1$. Multiplication by the extra $3y$ is either already zero at this precision or remains within (25).
* **Depth $h-3$:** only $y^H-1\bmod3$ is needed. Possible shifts have $c=1,5,7$, paired with $c+18$. Both members are admissible: the largest is $25$, whereas the cutoff in these units exceeds $35$. Their inverse units agree modulo $3$, so all these contributions cancel.

Deeper poles have weight divisible by $27$. Therefore the claimed covering support is proved:


$$
\boxed{
\operatorname{supp}(J\bmod3)
\subseteq
\{\text{last two HIGH coordinates}\}
\cup
\{r_1-kH/9-i-a:1\le k\le4,\ a=0,1\}.
}
\tag{26}
$$


Some bands in this cover indeed have zero coefficient.

For a row $i$ of $K$ and a band from row $t$ of $J$, the degree selected in $R$ is


$$
D+(k/9-1/6)H+\frac12+i+t+a.
\tag{27}
$$


For $k=1$ this is negative by (5). For $k=2,3,4$ it is strictly between $D$ and $H$. The edge terms are killed exactly by $KRe_m=KRe_{m-1}=0$. Consequently


$$
\boxed{KRJ^T=JRK^T=0\pmod3.}
\tag{28}
$$



## 5.2 $KRFRK^T=0\pmod3$, including LOW correction

Equation (16) gives the useful polynomial interpretation


$$
RK^Te_i
\longleftrightarrow
p_i(y)=y^{H/3+i}(y-1)^D
\pmod3.
\tag{29}
$$


These polynomials lie entirely in the actual HIGH space by (5).

The lower first-pole pairing of $p_i,p_j$ vanishes because its initial shift $2H/3+i+j$ already exceeds $r_1$.

The top perturbation modulo $3$ is multiplication by $y$: indeed


$$
(\beta-1)/3=-24-M_0=0\pmod3.
$$


Its pairing is the coefficient at $r_*$ of


$$
y^{2H/3+i+j+1}(y^H-1)(y-1)^D.
$$


The low branch requires a degree approximately $5H/6$, greater than $D$; the high branch requires a negative degree. Both are excluded with the margins (5).

Finally the LOW coupling of $p_i$ with $y^a$, $a<D$, is the coefficient at $r_1$ of


$$
y^{H/3+i+a}(y^H-1).
$$


The required equality is excluded by the gap between $H/3+i+a$ and $r_1$. Thus $X_Up_i=0\pmod3$. This kills the actual correction


$$
X_U^TL_U^{-1}X_U
$$


inside $F$, rather than dropping it.

Therefore


$$
\boxed{KRFRK^T=0\pmod3.}
\tag{30}
$$



## 5.3 Remaining edge contractions

Modulo $3$, $RFe_d$ is supported at $d,d+1$. Equations (10) give


$$
\boxed{JRF e_d=0\pmod3.}
\tag{31}
$$



Apply the same monic-division argument to $y^{d+1}$. Modulo $3$, its lower Schur response is supported in the last two HIGH coordinates, and its top perturbation in the last three. Hence


$$
Fe_{d+1}\in
\langle e_{m-2},e_{m-1},e_m\rangle\pmod3.
\tag{32}
$$


The inverse of these edge vectors is supported within $d,d+1,d+2$, all killed by $K$. Therefore


$$
\boxed{KRFRF e_d=0\pmod3.}
\tag{33}
$$



Finally,


$$
(FRFRF)_{dd}=(RFe_d)^TF(RFe_d)=0\pmod3
\tag{34}
$$


by the first $2\times2$ zero corner in (8).

Equations (28), (30), (31), (33), and (34) evaluate every term in $A_{27}$:


$$
\boxed{A_{27}=0\pmod3.}
$$


Together with (24) and (15), this proves (2).

---

# 6. Endpoint, primitive unit, final gcd, and denominator

Restoring $\lambda$ multiplies the residual Schur form by that unit. It does not change $T_5=0$.

The elimination maps are integral, and their changes to the radical endpoint are divisible by $3$. The transported endpoint therefore retains residue


$$
\overline e_{\rm rad}
=\bigl((-1)^i\bigr)_{0\le i<\nu}\ne0.
$$


It is not the vector $e$ used in the coupling expansion. Since $T_5=0$,


$$
\overline e_{\rm rad}\notin\operatorname{im}T_5.
$$



All $\nu$ residual LOW Smith factors are now divisible by $243$. Thus


$$
v_3(\det S_{\rm LOW})\ge5\nu,\qquad
v_3(\operatorname{adj}(S_{\rm LOW})_{ab})\ge5(\nu-1).
$$


Under the supplied complete-determinant normalization, this gives


$$
\boxed{v_3(g)\ge d+5\nu=4D-6.}
\tag{35}
$$



Retain the actual integer pair


$$
A_{\rm det}=\det T,\qquad
B_{\rm det}=\ell Q_n(-1)\det K,
$$


and its **final** gcd


$$
g=\gcd(|A_{\rm det}|,|B_{\rm det}|).
$$


Where $B_{\rm det}\ne0$,


$$
q=\frac{|B_{\rm det}|}{g},\qquad
p=-\frac{\operatorname{sgn}(B_{\rm det})A_{\rm det}}g,
$$


and the whole evaluated error is


$$
\boxed{
q(e+\pi)-p
=\frac{\operatorname{sgn}(B_{\rm det})\ell^k}{g}
\det H_{\rm complete},\qquad k=(n+1)/2.
}
\tag{36}
$$


The primitive multiplier is $\ell^k/g$.

The transported-cofactor denominator interface remains


$$
v_3(q)=
\max\!\left\{0,\,
h+2v_3((n-1)!)-1+
v_3(\operatorname{adj}(S_{\rm LOW})_{\rm endpoint})
-v_3(\det S_{\rm LOW})\right\},
\tag{37}
$$


when the displayed valuations are defined. The lower bounds above cannot be subtracted to evaluate (37). Neither $B_{\rm det}\ne0$ nor nonvanishing of (36) follows from this fifth-rank calculation alone.

---

# 7. Independent audit of A3turn18

## 7.1 Signed cubic concentration: pass

In the actual $q$-tilted principal ensemble, reflection gives


$$
\mathbb EC_3=0,
\qquad C_3=\sum_i\theta_i^3.
$$


On the ordered chamber,


$$
\nabla C_3=(3\theta_i^2)_i,\qquad
\|\nabla C_3\|^2=9Q_4.
$$


The Hessian bound therefore yields


$$
\mathbb EC_3^2\le Cn^{-1}\mathbb EQ_4
=O(d^3/n^3).
$$


This use of reflection is valid on a chamber after reversing particle order.

Crucially, with


$$
W_j=S_je^{i\Phi_q},\qquad N_j=\mathbb EW_j,
$$


the insertion defect is not discarded:


$$
\begin{aligned}
|\mathbb E(W_jC_3)|
&\le
\sqrt{\mathbb EC_3^2\,\mathbb E\Phi_q^2}
+\|S_j-1\|_\infty\sqrt{\mathbb EC_3^2}\\
&=O(d^2/n^2)+O(d^{5/2}/n^{5/2}).
\end{aligned}
$$


Since $N_j=1+O(d/n)$, division by the actual denominator proves


$$
\boxed{\langle C_3\rangle_j=O(d^2/n^2).}
$$


No reflection symmetry of $S_j$ is needed.

## 7.2 Actual derivative covariance: pass

For


$$
H_q=\sum_i(e^{-i\theta_i}+q)^{-1},
$$


center at the positive-measure mean $m_H=\mathbb EH_q$. Brascamp–Lieb on real and imaginary parts gives


$$
\mathbb E|H_q-m_H|^2=O(d/n).
$$


The algebraic complex covariance is exactly


$$
\langle(H_q-m_H)^2\rangle_j
-\langle H_q-m_H\rangle_j^2.
$$


Bounded $W_j$ and the lower bound on $|N_j|$ imply that its modulus is $O(d/n)$. It is not a positive variance, but the claimed bound remains valid.

Similarly, centering $Q$ before weighting gives an error $O(d/n)$, not an error proportional to its possibly large mean. These are the two points necessary to justify A3’s improved derivative expansion.

Thus the new steps in A3turn18 pass. With its stated exact reconstruction, full-sector, scalar-contour, and complete-residual interfaces, the resulting whole law is


$$
c_W-(e+\pi)
=(-1)^{n+1}4\pi M^{-2n-b}
\left[1+O\!\left(\frac bn+\frac{b^4}{n^3}+n^{-1/5}\right)\right]
\tag{38}
$$


on $3\le b=o(n^{3/4})$, uniformly for positive diagonal metrics in the actual coordinates. This is not a claim for nondiagonal metrics.

---

# 8. Critical-$3/4$ virial audit

The proposed sharp moment coefficients are consistent with the **circular**, rather than line, ensemble. Here is a direct derivation of the delicate coefficient.

Put $a=\alpha_0=\sigma/M$. Preliminary moments follow without Taylor-expanding the singular endpoint derivative: integration by parts with $t^{2r-1}$, the coercivity $tV_q'(t)\ge cn t^2$, and


$$
(x-y)\cot((x-y)/2)\le2
$$


give recursively


$$
\mathbb EQ_{2r}\le C_r(d/n)\mathbb EQ_{2r-2}.
$$


Thus


$$
\mathbb EQ_4=O(d^3/n^2),\qquad
\mathbb EQ_6=O(d^4/n^3).
\tag{39}
$$


The endpoint density vanishes to order $n$, and collision density quadratically, so these fluxes vanish. The differentiated singularities are integrable.

For the safe field $v(t)=tg(t)/M$,


$$
v(t)=t-\frac a2t^3+O(t^5),
$$


and


$$
(v(x)-v(y))\cot((x-y)/2)
=
2-a(x^2+xy+y^2)-\frac{(x-y)^2}{6}
+O(x^4+y^4).
\tag{40}
$$


The cotangent correction is essential. Using


$$
\sum_{i<j}(\theta_i^2+\theta_i\theta_j+\theta_j^2)
=(d-\tfrac32)Q+\tfrac12X^2,
$$


and


$$
\sum_{i<j}(\theta_i-\theta_j)^2=dQ-X^2,
$$


the safe-field identity becomes


$$
an\left(\mathbb EQ-\frac16\mathbb EQ_4\right)
=d^2-(a+\tfrac16)d\,\mathbb EQ
+(\tfrac16-\tfrac a2)\mathbb EX^2
+O(n\mathbb EQ_6+d\mathbb EQ_4+\mathbb EQ).
\tag{41}
$$



For $t^3g(t)/M$, the leading derivative and pair terms combine to


$$
3\mathbb EQ+
2\mathbb E\sum_{i<j}(\theta_i^2+\theta_i\theta_j+\theta_j^2)
=2d\,\mathbb EQ+\mathbb EX^2.
$$


Consequently


$$
an\mathbb EQ_4
=2d\,\mathbb EQ+\mathbb EX^2
+O(n\mathbb EQ_6+d\mathbb EQ_4+\mathbb EQ_4).
\tag{42}
$$


Since $\mathbb EX^2=O(d/n)$, (39)–(42) give


$$
\boxed{
\begin{aligned}
\mathbb EQ_6&=O(d^4/n^3),\\
\mathbb EQ_4&=\frac{2d^3}{a^2n^2}
+O(d^2/n^2+d^4/n^3),\\
\mathbb EQ&=\frac{d^2}{an}
+\left(\frac16-a\right)\frac{d^3}{a^2n^2}
+O(d^2/n^2+d^4/n^3).
\end{aligned}}
\tag{43}
$$


These establish the proposed sharp moment inputs independently of a critical-scale conclusion.

The centered weighted corrections are also of the required orders:


$$
\operatorname{sd}(Q)=O(d/n),\qquad
\operatorname{sd}(Q_4)
\le C\sqrt{\mathbb EQ_6/n}=O(d^2/n^2).
$$


Moreover


$$
\mathbb E\sum_i|\theta_i|^5
\le\sqrt{\mathbb EQ_4\,\mathbb EQ_6}
=O(d^{7/2}/n^{5/2}).
$$


With the actual denominator retained, these estimates justify the proposed first-derivative expansion and its required critical-scale remainder: after multiplication by $d/n$, every omitted term tends to zero at $d\asymp n^{3/4}$.

The quadratic coefficient of $-\sum(e^{-i\theta_i}+q)^{-2}$ is


$$
\frac{2-q}{(1+q)^4},
$$


and the same centered covariance estimate remains $O(d/n)$. Thus the proposed second-derivative expansion has the required remainder after multiplication by $d^2/n^2$.

These are moment and derivative checks, not a substitution of a large absolute partition correction by $1+o(1)$. The reciprocal-anchor identity must still be used exactly in the scalar comparison. The supplied algebraic quartic cancellation can be combined with these inputs, but a complete critical-scale whole-error theorem also requires the same uniform scalar remainder and contour interfaces at that precision. I do not infer any $o(n^{4/5})$ range.

---

# 9. Analytic primitive error remains separate from the weighted gcd gain

For the audited subcritical analytic centers, retain the least actual two-column clearer $d_B$, integral positive diagonal metric $\Omega$, and


$$
N_B=d_B[u,v],
$$




$$
A_B=N_{B,1}^T\Omega N_{B,1},\qquad
H_B=N_{B,1}^T\Omega N_{B,2},\qquad
g_B=\gcd(A_B,|H_B|).
$$


Then


$$
q_B=A_B/g_B>0,\qquad p_B=H_B/g_B,
$$


and the primitive multiplier is $d_B^2/g_B$. The whole evaluated real error is


$$
\boxed{
q_B(e+\pi)-p_B
=(-1)^n4\pi q_BM^{-2n-b}
\left[1+O\!\left(\frac bn+\frac{b^4}{n^3}+n^{-1/5}\right)\right]\ne0
}
\tag{44}
$$


eventually on the stated subcritical domain, using the complete residual and endpoint interfaces.

The fifth weighted gcd estimate (35) belongs to a different construction. It cannot be transferred to $g_B$ or used to estimate $q_B$.

---

## Closing ledger

### (1) New result and proof status

**Proved on (1):**

* Extended lower annihilation through the necessary first three HIGH tests, with available $729$-precision retained before division.
* Negligibility of the actual $Z^TLU$ corrections at fifth precision.
* Correctness of the proposed inverse expansion.
* Actual covering supports of $Fe_d\bmod9$ and $J\bmod3$, including all relevant pole pairs.
* Every contraction in $A_9/3$ and $A_{27}$ vanishes modulo $3$.
* Hence $T_5=0$, the transported endpoint has nonzero residue outside its image, and the supplied normalization gives $v_3(g)\ge4D-6$.

**Independent analytic audit:** A3turn18’s signed cubic and actual derivative covariance steps pass. The sharp critical virial moments (43) and the specified first- and second-derivative remainder scales are also verified independently. No stronger growing-degree range is asserted.

### (2) Exact remaining bottleneck

The weighted fifth carry is no longer the obstruction. Its vanishing forces a further saturation if one seeks exact local depths. More importantly, the relative depth of the **transported endpoint cofactor and determinant**, hence the actual denominator after the final gcd, remains unknown.

For irrationality one still needs a single compatible infinite family with a controlled actual primitive denominator and nonzero whole primitive errors tending to zero. Neither fifth-order divisibility nor the signed relative law supplies that missing arithmetic comparison.

### (3) Computation request

None. The fifth-carry evaluation and the virial checks above are symbolic. A finite rank scan would not strengthen their infinite scope, nor would it evaluate the unresolved primitive-denominator comparison.
