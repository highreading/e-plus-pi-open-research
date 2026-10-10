> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 audit: mesoscopic whole error and weighted determinant normalization

## Verdict

1. **The mesoscopic whole-error argument passes.** It uses the uniform zero-free theorem on $3\le b\le n/1000$, not a substitution $c=0$ into fixed-$c$ asymptotics. Its bounds are uniform over every actual coordinate and hence over arbitrary $n$-dependent positive diagonal metrics in those coordinates.

2. **There is a modest strengthening:** the analytic proof requires only
   

$$
3\le b=o(n),
$$


   rather than $b\log n=o(n)$. On that domain it gives
   

$$
\log|c_W-(e+\pi)|=-2n\log(1+\sqrt2)+O(b+1).
$$


   In particular, the requested $O(b+\log n)$ assertion holds.

3. **The weighted determinant gcd bounds follow from the supplied normalization formulas**, with an important coordinate qualification: the exact distinguished cofactor is $\operatorname{adj}(S)_{00}$ in an **endpoint-adapted** Schur basis. In a monomial or radical basis it must be transported with the endpoint vector. The lower bounds for all cofactors are basis-invariant, so this qualification does not invalidate the stated gcd lower bounds.

4. These conclusions do **not** decide irrationality of $e+\pi$. The CRT denominator consequence remains conditional on arithmetic at those same CRT centers, after their final gcd.

---

## I. Independent analytic audit

Write


$$
\sigma=\sqrt2,\qquad M=1+\sqrt2,\qquad d=b-1.
$$


All statements below concern the exact $R_j,A_j,P_j,F_j,E_j,D$ supplied in the Selberg formulas, with $0\le j\le b$.

### 1. Why the uniform zero-free input applies

The reconstruction gamma formula is an exact polynomial identity. For a degree-$k$ reference term,


$$
\frac1{\Gamma(n+k)}
 \int_0^\infty u^{n-1}e^{-u}(u+\sigma)^k\,du
\le (1+\sigma/n)^k.
$$


Indeed, expansion of $(u+\sigma)^k$ leaves gamma ratios whose denominator factors are all at least $n$. The middle coordinates are positive combinations of these reference terms. Thus their common normalization $B_j$ is retained, not approximated.

On $u\ge 19n/20$, the argument of a selected product is bounded by


$$
k\arcsin(\sigma/u).
$$


For $d\le n/1000$ this is eventually at most $0.0015$; the omitted gamma tail is exponentially small uniformly in $k\le d$. This verifies the sharpened insertion bounds used in the zero-free proof.

For the positive principal ensemble, the ordered chamber is convex and


$$
(-\log(1+\sigma\cos t))''\ge \sigma/M.
$$


The characteristic-log and bounded exponential-amplitude terms have uniformly bounded second derivatives on the stated $q$-regions. The pair-interaction Hessian is positive semidefinite. Therefore the Brascamp–Lieb hypothesis


$$
\operatorname{Hess}V\ge anI,\qquad a=1-\sigma/2>0,
$$


holds for sufficiently large $n$, uniformly in the allocation. The continuous characteristic phase on the principal interval has derivative bounded by $6$, yielding


$$
\operatorname{Var}\Phi\le \frac{36d}{an}.
$$


Mean-phase subtraction is necessary for complex $q$; reflection gives a zero mean for the chosen real branches at positive real $q$.

Finally, the adjacent monic-norm comparison controls the **same-$n$** outer sectors. Its sector sum is $O(e^{-n})$ throughout $d\le n/1000$. This bounds every sign $(-1)^{nk}$, including odd outer sectors, before any cancellation claim is made.

Consequently the supplied uniform conclusion is justified:


$$
\frac12 B_jZ_d(q)\le |A_j(q)|\le2B_jZ_d(q),
\qquad s_jA_j(q)>0\quad(q>0),
\tag{1}
$$


on the prescribed regions, and $D>0$. Since $b=o(n)$ is eventually inside $b\le n/1000$, there is no fixed-proportion limiting argument here.

### 2. Holomorphic branches and the actual phase

The disks


$$
|q-M|<1/5,\qquad |q-M^{-1}|<1/5
$$


have closures strictly inside the respective zero-free regions. On either disk,


$$
a_0\le |z^{-1}+q|\le a_1\qquad(|z|=1)
$$


for fixed positive constants. Hence


$$
a_0^d Z_d(0)\le Z_d(q)\le a_1^d Z_d(0).
$$



Define


$$
T_{j,\pm}(q)=
\Log\frac{A_j(q)}{s_jB_jZ_d(0)}
$$


with a real value at the appropriate real center. Existence follows from simple connectedness and zero-freeness; positivity in (1) fixes the real anchor.

The modulus bounds give


$$
|\Re T_{j,\pm}|\le Cb.
$$


On fixed interior disks, harmonic derivative estimates bound the gradient of this real part by $Cb$. Cauchy–Riemann then bounds the imaginary gradient; integration from the real anchor controls the otherwise undetermined imaginary constant. Cauchy estimates consequently give


$$
|T_{j,\pm}^{(k)}|\le C_kb
\tag{2}
$$


for each fixed $k$, uniformly in $j$.

Thus the passage from a log-modulus bound to phase control is valid. It would not be valid without the anchor.

### 3. Finite-$n$ saddles and uniform curvature

Set


$$
g(\zeta)=1+\frac{\sigma}{2}(\zeta+\zeta^{-1}),\qquad
h(\zeta)=\frac{\sigma}{2}(\zeta+\zeta^{-1})-1,
$$


and


$$
\Psi_{j,+}=\log g+\frac1nT_{j,+}(\sigma+\zeta),\qquad
\Psi_{j,-}=\log h+\frac1nT_{j,-}(\sigma-\zeta).
$$


The logarithms are local holomorphic branches, real near the positive real point $1$.

At $1$, the unperturbed first derivatives vanish and


$$
(\log g)''(1)=\frac{\sigma}{M},\qquad
(\log h)''(1)=\frac{\sigma}{\sigma-1}.
$$


Equation (2) supplies a real $C^3$ perturbation of size $O(b/n)$. Strict monotonicity of the real first derivative therefore gives unique nearby real saddles


$$
r_{j,\pm}=1+O(b/n)
$$


and uniform constants


$$
0<c\le r_{j,\pm}^2\Psi_{j,\pm}''(r_{j,\pm})\le C.
\tag{3}
$$



The angular arcs $|\theta|\le1/10$, once $r$ is sufficiently close to one, lie inside the log-control neighborhoods. The direct scalar negative-curvature bounds survive the $O(b/n)$ perturbation. Taylor expansion and (3) give the uniform local Gaussian formula.

The saddle values retain the characteristic insertion:


$$
n\Psi_{j,+}(r_{j,+})=n\log M+T_{j,+}(M)+O(b^2/n),
$$




$$
n\Psi_{j,-}(r_{j,-})=-n\log M+T_{j,-}(M^{-1})+O(b^2/n).
\tag{4}
$$



### 4. Full contour deformation, not just local arcs

The deformed scalar integrands are


$$
g(\zeta)^nA_j(\sigma+\zeta)\frac{d\zeta}{i\zeta},
\qquad
h(\zeta)^nA_j(\sigma-\zeta)\frac{d\zeta}{i\zeta}.
$$


They are single-valued and analytic on the intervening annuli: the powers are integers and $A_j$ is a polynomial. The local logarithms need not extend around those annuli.

The plus integral uses a closed circle. The minus integral uses an open arc and therefore requires **both radial connectors**.

For the remote circular pieces, the checked scalar inequalities give an $e^{-n/400}$ loss. The full absolute partition and the global insertion bound give


$$
|A_j(q)|\le CB_jZ_d(0)4^d.
$$


At the real saddle, (1) gives


$$
|A_j(q_s)|\ge cB_jZ_d(0)a^d
$$


for fixed $a>0$. Thus the remote/main ratio is at most


$$
C\sqrt n\,e^{-n/400+Cb}.
\tag{5}
$$


This tends to zero exponentially for $b=o(n)$.

At the original minus endpoints, $h=0$. Along the connectors,


$$
|h|\le0.002,\qquad h(r)\ge\sigma-1>0.4.
$$


Their characteristic factors obey the same absolute bound, so both connectors are exponentially negligible. This remains true whether the finite saddle radius is above or below one.

Combining these facts gives the full signed formulas


$$
P_j=\frac{n!}{2\pi}s_jB_jZ_d(0)
 e^{n\Psi_{j,+}(r_{j,+})}
 \sqrt{\frac{2\pi}{n\lambda_{j,+}}}(1+o(1)),
$$




$$
F_j=2n!s_jB_jZ_d(0)
 e^{n\Psi_{j,-}(r_{j,-})}
 \sqrt{\frac{2\pi}{n\lambda_{j,-}}}(1+o(1)),
\tag{6}
$$


uniformly in every coordinate. In particular,


$$
\operatorname{sign}P_j=\operatorname{sign}F_j=s_j,\qquad
\log(F_j/P_j)=-2n\log M+O(b+1).
\tag{7}
$$



### 5. Entire exponential residual and actual endpoint

Using the supplied bound for the **whole** residual,


$$
|eE_i|\le \frac{27M^n\sigma^{-i}}{n+1},
$$


the complete elementary-symmetric insertion satisfies


$$
\left|\sum_{i=0}^d\sigma^i e_{d-i}(z^{-1})eE_i\right|
\le \frac{27M^n2^d}{n+1}.
$$


The full absolute partition therefore gives


$$
|E_j|\le CB_jZ_d(0)\frac{M^n2^d}{n+1}.
$$


From (4)–(6),


$$
|E_j/P_j|\le \frac{e^{Cb}}{n!\sqrt n}.
\tag{8}
$$



For the endpoint, the adjacent partition identity has no missing factorial:


$$
Z_b(0)/Z_d(0)=h_d.
$$


The monic trial polynomial $z^d$ has modulus one on the circle, so


$$
h_d\le e^\sigma M^n.
$$


Together with $0<D\le2Z_b(0)$ and $B_0>1$ eventually, this gives


$$
|D/P_0|\le \frac{C\sqrt n\,e^{Cb}}{n!B_0}.
\tag{9}
$$


All other endpoint coordinates are exactly zero.

Both (8) and (9) are factorially smaller than the lower bound in (7). Consequently the **whole exact error**


$$
c_j-(e+\pi)=
\frac{E_j}{P_j}
+(-1)^{n+1}\frac{F_j}{P_j}
+(-1)^n\delta_{j0}\frac{D}{P_j}
\tag{10}
$$


is nonzero, has sign $(-1)^{n+1}$, and has logarithm


$$
-2n\log M+O(b+1).
\tag{11}
$$


Also $u_j=(-1)^nP_j/D\ne0$.

### 6. Arbitrarily varying positive metric weights

For $w_{j,n}>0$,


$$
c_W-(e+\pi)=
\sum_j
\frac{w_{j,n}u_j^2}{\sum_\ell w_{\ell,n}u_\ell^2}
\bigl(c_j-(e+\pi)\bigr).
$$


These are positive convex weights. Every coordinate error has the same eventual sign, with uniform two-sided bounds. Their minimum and maximum therefore bound the metric error independently of the sizes of the weights.

This proves the asserted theorem for **all positive diagonal actual-coordinate metrics**, including arbitrary $n$-dependence. No analogous assertion for general nondiagonal metrics is implied.

---

## II. Weighted determinant normalization after radical rank zero

This is a different construction and index family. Its arithmetic must not be combined with the CRT analytic theorem above.

### 1. Exact coefficient pair

On the regular weighted family


$$
n=4^j+1,\qquad j\ge1,\qquad k=(n+1)/2,
$$


use the integral endpoint-adapted basis


$$
f_0=1,\qquad f_i=(y+1)y^{i-1}\quad(1\le i<k).
$$


It is unit-triangular relative to monomials, and evaluation at $-1$ is exactly the vector $e_0$.

Let $T$ be the rational-part moment matrix after multiplication by the actual denominator-clearing integer $\ell$. In this basis,


$$
T=\begin{pmatrix}t_R&z^T\\z&K\end{pmatrix}.
$$


The complete period contribution is rank one:


$$
\ell H_{\rm complete}
=T+\ell Q_n(-1)(e+\pi)e_0e_0^T.
$$


Expanding the determinant in this single entry gives the exact polynomial identity


$$
\ell^k\det H_{\rm complete}
=A_{\rm det}+B_{\rm det}(e+\pi),
\tag{12}
$$


where


$$
A_{\rm det}=\det T
=t_R\det K-z^T\operatorname{adj}(K)z,
\qquad
B_{\rm det}=\ell Q_n(-1)\det K.
\tag{13}
$$


This explains the extra factor $\ell Q_n(-1)$ in $B_{\rm det}$. It is not an optional normalization.

### 2. Exact Schur depths and retained units

Suppose the known HIGH block $E$ is a unit block and the LOW block has size $d$, with endpoint coordinate $0$ in LOW. Define the **exact**


$$
S=\frac{T_{LL}-T_{LH}E^{-1}T_{HL}}3.
$$


Then


$$
A_{\rm det}=3^d\det E\,\det S,
$$




$$
\det K=3^{d-1}\det E\,\operatorname{adj}(S)_{00}.
\tag{14}
$$


Write


$$
\ell=3^h u_\ell,\quad
Q_n(-1)=3^{e_Q}u_Q,\quad
\det E=u_E,
$$


where all three displayed $u$'s are units. Thus


$$
B_{\rm det}
=3^{h+e_Q+d-1}u_\ell u_Qu_E\,
 \operatorname{adj}(S)_{00}.
\tag{15}
$$


In particular, whenever the relevant determinants are nonzero,


$$
\boxed{v_3(A_{\rm det})=d+v_3(\det S),}
$$




$$
\boxed{v_3(B_{\rm det})=
h+e_Q+d-1+v_3(\operatorname{adj}(S)_{00}).}
\tag{16}
$$



A global primitive-polynomial unit, such as $L_n/3$, scales the associated Schur matrices and remains in these unit factors. It does not change their valuations.

**Coordinate qualification.** In another LOW basis, the distinguished cofactor in (14) becomes the transported endpoint contraction of $\operatorname{adj}(S)$. One must not identify it with a literal monomial-basis $00$ entry without transporting the endpoint. The subsequent divisibility argument applies to every cofactor, so it is unaffected.

### 3. The exact endpoint depth

A1’s normalization argument supplies more than a lower bound. Put


$$
N=n-1=3M+1,\qquad L=N-1=3M.
$$


Its exact geometric remainder and Pascal complement give


$$
b/L!\equiv2,\qquad
(c\xi_{\rm const}-b\xi_{\rm last})/L!\equiv2\pmod3.
$$


With $a$ a unit and $v_3(\delta_S)=1$, the exact endpoint identity yields


$$
v_3(P_n(-1))
=v_3(N!)+v_3(L!)-1=2v_3(N!)-1.
$$


The coefficient of degree $n-1$ has valuation exactly $-1$, while $3P_n$ is integral locally. Hence the actual primitive leading multiplier has valuation exactly one. Therefore


$$
\boxed{e_Q=v_3(Q_n(-1))=2F_{n-1},\qquad
F_t:=v_3(t!).}
\tag{17}
$$


This also proves $Q_n(-1)\ne0$.

This verification uses A1’s supplied divided-moment residue and first-lift inputs; it does not replace them with a nonsaturated ordinary-coefficient lattice.

### 4. From the second/third radical depth to the actual gcd

No rank scan is needed. Suppose elimination of the first $D$ LOW unit coordinates leaves $\nu$ Smith factors divisible by $3^t$. Here $d=D+\nu$, and $t=2$ or $3$ denotes the supplied second- or third-depth conclusion.

Then


$$
v_3(\det S)\ge t\nu.
$$


Every $(d-1)$-minor has valuation at least the sum of the smallest $d-1$ Smith exponents, hence


$$
v_3(\operatorname{adj}(S)_{ab})\ge t(\nu-1).
\tag{18}
$$


Equations (16)–(18) imply


$$
v_3(A_{\rm det})\ge d+t\nu,
$$




$$
v_3(B_{\rm det})\ge d+t\nu+(h+e_Q-1-t).
$$


Thus, provided $h+e_Q\ge t+1$,


$$
\boxed{v_3\gcd(|A_{\rm det}|,|B_{\rm det}|)\ge d+t\nu.}
\tag{19}
$$


That hypothesis holds on the stated regular subclasses by (17); already at $n=5$, $h=2$ and $e_Q=2$.

For the third-depth subclass supplied in A4 turn 13,


$$
d=\frac{3D}{2}-1,\qquad \nu=\frac D2-1,
$$


so


$$
\boxed{v_3(g)\ge d+3\nu=3D-4.}
\tag{20}
$$


This closes the normalization dependency in that gcd claim, conditional only on its supplied third-radical divisibility result.

### 5. Final gcd, actual denominator, and whole evaluated error

Retain


$$
g=\gcd(|A_{\rm det}|,|B_{\rm det}|),\qquad
q=\frac{|B_{\rm det}|}{g},\qquad
p=-\frac{\operatorname{sgn}(B_{\rm det})A_{\rm det}}g.
$$


Then


$$
\boxed{
q(e+\pi)-p
=\frac{\operatorname{sgn}(B_{\rm det})}{g}
 \bigl(A_{\rm det}+B_{\rm det}(e+\pi)\bigr)
=\frac{\operatorname{sgn}(B_{\rm det})\ell^k}{g}
 \det H_{\rm complete}.
}
\tag{21}
$$



The exact local denominator law is


$$
v_3(q)=
\max\!\left\{0,\,
h+2F_{n-1}-1+
v_3(\operatorname{adj}(S)_{00})-v_3(\det S)
\right\}.
\tag{22}
$$


The lower bounds in (18) cannot be subtracted to evaluate (22).

Moreover, a nonzero formal polynomial $A_{\rm det}+B_{\rm det}X$ need not be nonzero at $X=e+\pi$. The supplied regular-family nonvanishing and distinct-center results give $B_{\rm det}\ne0$ and at most one vanishing evaluated error; the normalization argument alone does not prove those facts or error decay.

---

## III. Bounded follow-on lemma: a sharper saddle-displacement correction

The analytic audit also yields a useful refinement without any equilibrium limit.

Let $f=\log g$ or $\log h$, and let $U(\zeta)$ be the corresponding actual characteristic logarithm. Put


$$
\alpha=f''(1)>0,\qquad a=U'(1).
$$


Uniformly in every coordinate,


$$
r-1=-\frac{a}{n\alpha}+O(b^2/n^2),
$$


and


$$
\boxed{
nf(r)+U(r)
=nf(1)+U(1)-\frac{a^2}{2n\alpha}
+O(b^3/n^2).
}
\tag{23}
$$


Indeed, expand the stationary equation using $U^{(k)}=O(b)$, then substitute its solution into the quadratic expansion of $nf+U$.

For $n\sim2b^3$, the remainder in (23) is $O(b^{-3})$. This does not remove the characteristic value $U(1)$; it quantifies the actual recentering correction.

---

## Closing ledger

### (1) New result and proof status

- **Audited and proved from the supplied exact and uniform analytic inputs:** the complete signed-error theorem, in fact on $3\le b=o(n)$, with every coordinate nonzero and arbitrary positive diagonal actual-coordinate metrics.
- **Normalization closed:** exact determinant depths (16), endpoint depth $e_Q=2F_{n-1}$, and the second/third-depth actual gcd lower bounds, with all local unit factors retained.
- **New bounded refinement:** the actual saddle-displacement formula (23).

### (2) Exact remaining bottleneck

For the CRT centers $b=9^r,\ n=2b^3+O(b^2)$, the whole error is eventually negative and has rate $-2\log M$. If A5 proves the same centers’ final-gcd laws


$$
v_2(q)=\tfrac32n-o(n),\qquad v_3(q)\ge n-o(n),
$$


then their nonzero primitive forms grow at least at rate


$$
\tfrac32\log2+\log3-2\log M>0.
$$


That excludes only that route.

For the separate weighted determinant family, the obstruction remains the **relative distinguished-cofactor depth** in (22), together with suitable control of the whole evaluated error. Radical rank-zero lower bounds do not resolve it. Irrationality of $e+\pi$ remains undecided.

### (3) Computation request

None. No finite computation is needed for the analytic audit or the normalization and gcd implications above.
