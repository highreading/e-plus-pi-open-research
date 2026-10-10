> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## Verdict

The two analytic/local arguments pass their **new derivations**, with the normalization dependencies stated below. However, the supplied material does **not** determine the fourth saturation on the requested domain. There are two precise gaps:

1. The independently audited A1 all-depth theorem supplies the asserted core modulo $81$ when $81\mid j$, but supplies it only modulo $27$ on the full requested domain $27\mid j$. The attached raw derivative control does not close that projected, coefficientwise precision gap.
2. The supplied sources do not contain the full entry formulas and index cutoffs for the actual HIGH and mixed blocks needed to verify the proposed extended-functional identifications. In particular, the equation identifying $X_{U,d}$ with an extended lower-functional pairing, including its factor of $3$, is not supplied or derived.

I can evaluate the proposed $KRK^{T}$ cancellation **conditional on the stated inverse and support**, and prove a rank-at-most-two reduction for the remaining carry. I cannot honestly evaluate the other three terms, assert $T_4=0$, or improve the actual gcd lower bound.

These conclusions concern separate constructions. No analytic result for a positive diagonal actual-coordinate metric is transferred to the weighted determinant center.

---

## 1. Independent audit of A1 turn 15

### 1.1 Restricted moment interpolation: pass

For the $\ell$-th factorial-moment summand after $s=3T+r$, the coefficient bound


$$
v_3([T^k]\text{summand})
\ge \max\{k,\lfloor2\ell/3\rfloor\}-v_3(\ell!)
$$


is valid. Choosing $k$ variable factors supplies $3^k$, and leaves at least $\max(0,z-k)$ divisible constant factors, where $z\ge\lfloor2\ell/3\rfloor$.

The bounds tending to infinity both with $\ell$ and with $k$ justify convergence in the restricted power-series ring. The exponential interpolation of $(-2)^{3T+r}$ is legitimate because


$$
(-2)^3=1-9,\qquad v_3(\log(1-9))=2.
$$


Thus the branch assertions, including


$$
e_{3T}/3\in\mathbb Z_3\langle T\rangle,
$$


pass without discarding moment terms.

### 1.2 Factorial quotient and residual: pass

The ordinary coefficient denominator bound for the power sum follows from


$$
\sum_{v<A}(v)_h=\frac{(A)_{h+1}}{h+1}.
$$


It gives the stated convergent logarithm $F$ and restricted unit quotient $J$.

The crucial finite-difference identity is correct:


$$
\sum_{D=0}^{M}(-1)^{M-D}\binom MD
 \binom{q+D}{D}(D)_h
=(M)_h\binom{q+h}{M}.
$$


For example, shifting $D=h+t$ reduces the left side to


$$
(M)_h
\sum_{t=0}^{M-h}(-1)^{M-h-t}\binom{M-h}{t}
\binom{q+h+t}{q},
$$


which is the displayed right side by the ordinary binomial difference identity.

Since $q<M$, the $h=0$ term vanishes. For $h\ge1$, $\kappa_h\in3\mathbb Z_3$ and $M\mid(M)_h$. Therefore


$$
v\in3M\mathbb Z_3^{3M}.
$$


The normalized tail assertion also passes: dividing by $3M$ loses no additional dimension-dependent precision.

### 1.3 Raw contraction interpolation: pass

Formula (17) in A1 can be checked by expanding monomials into falling factorials and using


$$
\binom{D+E}{D}=\sum_k\binom Dk\binom Ek.
$$


The output coefficients are integral; its coefficient Gauss norm is at most one. Consequently extension to restricted series is justified.

In particular,


$$
H(M)-4\in M\mathbb Z_3,\qquad
G(M)-272\in M\mathbb Z_3
$$


are genuine all-depth assertions, not numerical extrapolations.

### 1.4 Projection and primitive normalization: pass with explicit dependencies

The projection estimates follow from the stated inputs


$$
E^{-1}\in M_L(\mathbb Z_3),\quad w\in\mathbb Z_3^L,
\quad a\in\mathbb Z_3^\times,\quad
b,\xi_{\rm const}\in L!\mathbb Z_3.
$$


They prove


$$
\Theta_M\equiv68\pmod{3^{v_3(M)}}.
$$


The factorial quotient estimate for every $d\le L-1$ is correct: $N!/d!$ contains $L=3M$.

Thus, using those previously supplied elimination and endpoint inputs, the new all-depth derivation establishes exactly


$$
3P_n\equiv
(y+1)(y-1)^{n-2}(3y-71)\pmod{3^K},
\quad
K\ge1,\ j\ge1,\ 3^K\mid j.
$$


It retains


$$
Q_n=\lambda_n(3P_n),\qquad \lambda_n\in\mathbb Z_3^\times.
$$



### 1.5 Important precision limitation for this assignment

For $v_3(j)=3$, this theorem gives precision $27$, **not $81$**. Although


$$
3y-71\equiv3y+10\pmod{81},
$$


that arithmetic identity does not improve the modulus of the polynomial congruence.

Therefore the modulo-$81$ core used in A4 turn 15 on **all** $27\mid j$ requires an additional argument. A1’s theorem alone proves that core on $81\mid j$.

The raw derivative receipt suggests why an improvement may hold, but expressly does not prove projection and factorial-tail transfer. I do not use that transfer here.

---

## 2. Independent audit of A3 turn 14

The critical-square-root derivation passes, using the exact reconstruction and whole-residual input recorded in the supplied archive.

The essential checks are as follows.

* The ordered-chamber Hessian remains bounded below by $cnI$ under bounded real quadratic and linear tilts.
* The $t^3$ vector-field argument correctly gives
  

$$
\mathbb E_{\tau,\ell}Q_4=O(d^3/n^2).
$$


  The sign of the cotangent causes no reversal because its polynomial multiplier is nonnegative.
* The repaired field
  

$$
v(t)=t\,g(t)/M
$$


  cancels the endpoint pole exactly. Its pair estimate is uniform: differences lie in $[-3\pi/2,3\pi/2]$, away from the next cotangent poles.
* Consequently
  

$$
\mathbb E_{\tau,0}Q
  =\frac{d^2}{\alpha n}(1+O(d/n)),\qquad
  \operatorname{Var}_{\tau,0}Q=O(d^2/n^2).
$$


* Real tilts, rather than complex probability measures, justify the exponentially weighted remainder bounds. On $d=O(\sqrt n)$, the weighted cubic error is $O(n^{-1/4})$.
* The actual reconstruction satisfies $S_j=1+O(d/n)$ uniformly in every coordinate. The odd outer sectors remain included through their absolute comparison.
* Both order-one corrections cancel:
  

$$
C(M)=C(M^{-1}),
$$


  and
  

$$
(1+M)^2\alpha_+
   =(1+M^{-1})^2\alpha_-.
$$



The scalar normalization and curvature ratio therefore give


$$
\frac{F_j}{P_j}=4\pi M^{-2n-b}(1+o(1)).
$$


The complete forcing and endpoint remain in


$$
c_j-S=\frac{E_j}{P_j}
 +(-1)^{n+1}\frac{F_j}{P_j}
 +(-1)^n\delta_{j0}\frac{D}{P_j}.
$$


Their supplied factorial bounds are negligible relative to the main term.

Hence, uniformly for


$$
\kappa_0\sqrt n\le b\le\kappa_1\sqrt n,
$$


the coordinate and positive diagonal actual-coordinate metric conclusions pass:


$$
c_W-S=(-1)^{n+1}4\pi M^{-2n-b}(1+o(1)).
$$


The determinant, actual first-column coordinates, and whole errors are eventually nonzero.

For a rational metric, this means precisely


$$
qS-p=(-1)^n4\pi qM^{-2n-b}(1+o(1)),
\quad
q=\frac{A_B}{\gcd(A_B,|H_B|)}.
$$


It supplies no bound on this final primitive denominator.

---

## 3. Fourth carry: what can actually be evaluated

### 3.1 The proposed inverse-support cancellation

Assume the stated HIGH index orientation and unit normalization have been verified, so that


$$
R_{ab}=[z^{d+m-a-b}](1-z)^{-A}\pmod3,
\qquad A=H-D.
$$


Since $H$ is a power of $3$,


$$
(1-z)^{-A}
=\frac{(1-z)^D}{(1-z)^H}
=\frac{(1-z)^D}{1-z^H}
\quad\text{in }\mathbb F_3[[z]].
$$


It follows rigorously that


$$
[z^t](1-z)^{-A}=0\qquad(D<t<H).
$$



If each row of $K$ has precisely the stated possible nonzero entry at $a=r_2-i$, then every potentially nonzero entry of $KRK^T$ is the coefficient with degree


$$
t=\frac{H+3}{6}+D+i+j.
$$


Whenever the stated index bounds put this degree strictly between $D$ and $H$, it vanishes. Thus


$$
\boxed{KRK^T=0}
$$


follows from those exact support and orientation hypotheses.

This verifies the coefficient cancellation, not the missing identification of the actual inverse with that representative. The supplied archive labels $E_0$ an “exact anti-triangular top-pole representative,” but does not provide its entries, HIGH index range, or defining units from which to verify the inverse orientation independently.

### 3.2 Extended lower recurrence

The coefficient-gap argument does extend to the proposed degree-$d$ polynomial at the **lower-functional level**.

Indeed,


$$
w_\nu=y^\nu(y-1)^D,\qquad \nu+D=d,
$$


and multiplication by $(y-1)^A$ gives


$$
(y-1)^Aw_\nu y^a=y^{\nu+a}(y-1)^H.
$$


For $0\le a\le d$,


$$
\nu+a\le2D-2.
$$


Including the linear core increases the maximum shift to $2D-1$. Since $D<H/108$ and the indices are integral,


$$
2D-1<\frac{H/27-1}{2}.
$$


Thus the same half-grid exclusion applies to every retained lower-pole layer, **provided the modulo-$81$ core and the stated lower-pole expression are valid**.

This proves the suggested extension of lower-functional annihilation under those hypotheses. It does not prove that the actual HIGH diagonal or mixed column is that lower functional with the proposed normalization.

### 3.3 Why this does not evaluate the remaining terms

The required identities concern


$$
F=\frac{E-3X_U^TL_U^{-1}X_U-E_0}{3},
\qquad
J=\frac{V+2ee_m^T-3K}{9}.
$$


To deduce $F_{dd}/3=0\pmod3$, one needs the actual diagonal relation through the corresponding additional digit. To deduce $Je_d=0$, one needs the actual mixed column through modulus $27$. Lower-functional annihilation alone supplies neither identification.

Likewise, no displayed all-layer formula establishes


$$
Fe_d\in\mathbb F_3 e_m.
$$


This support assertion is stronger than the lower recurrence and is exactly where an unrecorded upper-edge contribution could survive.

Accordingly, three terms of (*) remain unevaluated. Calling them zero would assume the central obligation.

---

## 4. New bounded reduction: the remaining carry has rank at most two

There is a useful algebraic conclusion once the verified inverse-support hypotheses give $KRK^T=0$.

Work over $\mathbb F_3$, and set


$$
a=Je_d,\qquad b=KRFe_d,\qquad
c=4(FRF)_{dd}-4F_{dd}/3.
$$


The remaining right side of (*) is


$$
\operatorname{Sym}(e,v)+cee^T,
\qquad v=-2a+2b.
$$


Since $2$ is invertible, put


$$
w=v+\frac c2e.
$$


Then the carry is simply


$$
\boxed{T_4=-\operatorname{Sym}(e,w).}
$$



For $e\ne0$, this gives the complete conditional classification:

* If $w=0$, then $T_4=0$.
* If $w=\gamma e$, $\gamma\ne0$, then $T_4=-2\gamma ee^T$, of rank one and image $\langle e\rangle$.
* If $e,w$ are independent, then $T_4$ has rank two and image $\langle e,w\rangle$.

For the last assertion, the independent linear functionals $e^Tx,w^Tx$ map onto $\mathbb F_3^2$, and


$$
\operatorname{Sym}(e,w)x=e(w^Tx)+w(e^Tx).
$$



The actual endpoint residue


$$
t=\bigl((-1)^i\bigr)_{0\le i<\nu}
$$


must be tested against the corresponding image above. It must not be silently identified with $e$.

This reduction is not an evaluation of $w$, but it limits any surviving fourth carry to rank at most two and gives its exact image once that single vector is evaluated.

---

## 5. Normalization and whole weighted error

Retain the actual primitive unit $\lambda=L_n/3$. The actual carry is $\lambda T_4$; its rank and image are unchanged.

No fourth-depth gcd improvement is established here. The prior bound remains


$$
v_3(g)\ge d+3\nu.
$$


If the missing identities prove $T_4=0$, the established adjugate normalization gives only the valid lower bound


$$
v_3(g)\ge d+4\nu.
$$



In all cases,


$$
g=\gcd(|A_{\rm det}|,|B_{\rm det}|),\qquad
q=\frac{|B_{\rm det}|}{g},\qquad
p=-\frac{\operatorname{sgn}(B_{\rm det})A_{\rm det}}g,
$$


and, when $B_{\rm det}\ne0$,


$$
qS-p
=\frac{\operatorname{sgn}(B_{\rm det})\ell^k}{g}
  \det H_{\rm complete}.
$$


Neither nonvanishing of this evaluated determinant nor its decay follows from the carry calculation. Lower determinant and cofactor bounds cannot be subtracted to determine $q$.

The $n=4482,b=9$ certificate is separate finite corroboration of the CRT construction; it supplies no weighted fourth-carry information.

---

## Closing ledger

### (1) New result and proof status

* **Audit passes:** A1’s new all-depth interpolation and residual arguments, with its stated elimination dependencies; A3’s critical-square-root relative asymptotic in the actual positive diagonal metrics.
* **Precision repair identified:** A1 alone does not supply the modulo-$81$ core on every $27\mid j$.
* **Proved conditional cancellations:** the inverse-coefficient gap gives $KRK^T=0$; the lower-functional half-grid argument extends to degree $d$.
* **New bounded lemma:** after that cancellation, the fourth carry has rank at most two, with the image classification above.
* **Not proved:** $T_4=0$, its actual endpoint image, or the improved gcd lower bound.

### (2) Exact remaining bottleneck

Supply and verify the full actual HIGH/mixed pole formulas, their index cutoffs and units, and the modulo-$81$ core on $v_3(j)=3$. These must establish or refute the actual identities for $F_{dd}/3$, $Je_d$, and $Fe_d$, not merely their lower-functional analogues.

Irrationality of $e+\pi$ remains unresolved; the final primitive denominator and nonzero whole real error still require compatible control.

### (3) Computation request

None. The present obstruction is missing symbolic precision and block-identification information, not a finite matrix rank calculation.
