> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1, Turn 12 — Vanishing of the actual leading moments and a depth-$18$ coefficient-window law

## Executive conclusion

On the accepted sufficiently large original depth-$16$ window, the complete leading Hankel form is **zero modulo $3$**. In fact, one more normalized layer is also zero:



$$
\boxed{\Psi\in 9M_\nu(\mathbb Z_3),\qquad
\mathsf H\in9M_\nu(\mathbb Z_3).}
$$



Consequently, for **all the actual moments**, including those determined by the complete last-column forcing,


$$
\boxed{\mu_k\equiv0\pmod9
\qquad(0\le k\le2\nu-2).}
$$



This is not inferred from the unit normalizer or from a selected subset of the twenty features. It follows from a finite polynomial transfer applied to the **whole Schur complement**, followed by restoration of the complete producer remainder.

The conclusions are:

1. **Actual leading radical and endpoint action.**
   

$$
\operatorname{rad}(\mathsf H\bmod3)=\mathbb F_3^\nu,
   \qquad \operatorname{rank}(\mathsf H\bmod3)=0.
$$


   On this radical the actual endpoint is
   

$$
x\longmapsto\sum_{i=0}^{\nu-1}(-1)^ix_i,
$$


   a nonzero functional with kernel of dimension $\nu-1$.

2. **The next induced form is also zero.**
   Since the first radical is the whole space, its next normalized induced form is simply $\mathsf H/3\bmod3$. It too is zero, with the same endpoint action.

3. **The first layer not settled here is depth $18$.** Define
   

$$
S_{\rm act}=-3^{18}\Theta,\qquad
   \mathsf H^{[2]}=\mathsf H/9=\mathsf V^T\Theta\mathsf V.
$$


   Its leading moments are reduced to an explicit coefficient window of **one further actual producer digit**:
   

$$
\boxed{
   \mu_k^{[2]}
   \equiv
   -[y^{r_1-k}]
   (y-1)^{2D}\,
   \overline{\frac{\Delta(y)}{y+1}}
   \pmod3,
   \quad
   0\le k\le D-4,
   }
$$


   where
   

$$
r_1=\frac{H-1}{2},\qquad
   \Delta=\frac{R-(y+1)(y-1)^{A-27}B_{11}(y-1)}{3^{11}},
$$


   and $B_{11}$ is any integral lift of the accepted actual precision-$11$ saturated jet.

4. **The complete boundary subtraction changes with the normalization.**
   

$$
\boxed{
   \begin{aligned}
   \delta_0&=3^{2\nu}\det\Theta,\\
   \delta_1&=3^{2\nu-2}
   \left(
   e_{\rm act}^T\operatorname{adj}(\Theta)e_{\rm act}
   -3^{18}d_{\rm act}\det\Theta
   \right).
   \end{aligned}}
$$


   There is no dimension-multiplied gain in the primitive denominator.

These results settle the requested leading radical classification, and its next induced layer, rather than presuming unit pivots. They do **not** establish rational nonvanishing of the residual determinant or a relative valuation theorem.

No tools were used. No numerical producer digits or receipts were independently regenerated.



$$
\boxed{\text{The irrationality or rationality of }e+\pi\text{ remains unresolved.}}
$$



---

## 1. Scope and proof dependencies

Retain exactly


$$
n=4^j+1,\qquad j>0,\qquad81\mid j,
$$




$$
A=n-2=H-D,\qquad H=3^{h-1},
$$


and the accepted sufficiently large window


$$
j\equiv81\pmod{243},
\qquad
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad
C_{16}=512\cdot17^2\,3^{15}.
\tag{1.1}
$$



Thus $t=v_3(A)=5$. The finite spaces remain


$$
m=\frac{A+1}{2},\qquad
d=\frac{3D}{2}-1,\qquad
\nu=\frac D2-1,
$$




$$
U_u=(y-1)^u\quad(0\le u<D),
$$




$$
z_i=(y-1)^Dy^i\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m).
\tag{1.2}
$$



No residual coordinate is added or deleted. No HIGH coordinate beyond $m$ is introduced.

Write $x=y-1$, $W=[U\ Y]$, and retain the complete functional


$$
\boxed{
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h
\sum_{\substack{v\ge0\\2v+1\le4n-3}}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^r)=(2r)!.
}
\tag{1.3}
$$



The producer is


$$
Q_{\rm act}=Q_c+3^6R,
\qquad
Q_c=(y+1)x^A(\beta+3y),
\qquad
\beta=-71-A.
\tag{1.4}
$$



The following accepted results are used at their stated scopes:

- the finite LOW/HIGH block inverses and complete supported-return formulas;
- the corrected-column congruence modulo $9$;
- the exact Schur perturbation identity;
- the actual saturated jet at precision $11$, with $\kappa_{11}=27$;
- the complete endpoint law
  

$$
Q_{\rm act}(-1)=-F^2\xi_n,\qquad F=(n-1)!,
  \qquad \xi_n\in1+3\mathbb Z_3;
$$


- the depth-$16$ reduction and twenty-feature identity.

A4 Turn 18 audits Turn 10, not the entirety of Turn 11. The result below concerning $\Psi$ is independent of the pending Hankel-transfer audit. The few Turn 11 algebraic facts needed to translate it into moment language are identified separately in §7.

The finite receipts establish only their stated auxiliary cases. None is used as an original-family determinant theorem.

---

## 2. A stronger finite core-support statement at the required precision

The accepted window has substantial unused separation. This permits a fixed-precision statement stronger than the previously quoted core depth $17$.

### Proposition 2.1 — Core corrected columns with an upper-degree gap

Let $P\ge1$, and put


$$
\Omega=\frac{H}{3^{P-1}}.
$$


Suppose $\Omega$ is integral,


$$
h-1\ge P,
\qquad
\Omega>4D+2P+3.
\tag{2.1}
$$



Then the exact core corrected columns admit polynomial representatives


$$
\widehat z_i^{\,c}\equiv\phi_i=x^D\psi_i\pmod{3^P}
\tag{2.2}
$$


such that

- $\deg\phi_i\le m$;
- $\operatorname{supp}\psi_i\subseteq I_\Omega(\nu+P)$;
- $\phi_i\equiv z_i\pmod3$;
- their distance from the upper degree boundary satisfies the conservative bound
  

$$
\boxed{
  m-\deg\phi_i\ge
  \frac{\Omega-4D-2P-3}{2}.
  }
  \tag{2.3}
$$



Moreover,


$$
\boxed{S_c\in3^{P+1}M_\nu(\mathbb Z_3).}
\tag{2.4}
$$



Here a negative coefficient index remains zero, and all HIGH returns are on the original interval $d,\ldots,m$.

### Proof

The proof uses the complete normalized lower-pole form $\Lambda$ from Turn 8:


$$
G_c=\beta H_0+3H_1+3\Lambda.
\tag{2.5}
$$



Modulo $3^P$, the binomial valuation identity


$$
v_3\binom Hk=h-1-v_3(k)\qquad(0<k<H)
$$


shows that $x^H$ is supported on multiples of $\Omega$.

Every lower-pole term surviving in $\Lambda\bmod3^P$ has


$$
a\ge h-P,
$$


so its extraction index


$$
\frac{c3^a-1}{2}
$$


lies on the $\Omega$ half-grid. The factorial term in $\Lambda$ vanishes modulo $3^P$, because its coefficient contains $3^{h-1}$. This is a valuation-based omission from the **complete** functional.

For the LOW coupling with $z_i$, the relevant polynomial is


$$
x^Hx^uy^i(\beta+3y).
$$


Its nongrid width is at most


$$
u+i+1\le D+\nu-1.
$$


By (2.1), it misses every surviving half-grid extraction. Therefore


$$
\Lambda(U,Z)\equiv0\pmod{3^P}.
\tag{2.6}
$$



The normalized HIGH right-hand side is, modulo $3^P$, supported on


$$
J_\Omega(\nu).
$$


The exact finite inverse $R_H$ carries this to $\mathcal C_\Omega(\nu)$. Each complete return


$$
R_H\mathsf F_H
$$


increases the width by at most one, provided the LOW-separation condition holds. For every term needed in the finite inverse expansion modulo $3^P$, the width is at most $\nu+P$, and


$$
(\nu+P)+D<\frac{\Omega-1}{2}.
$$


Thus the complete LOW subtraction is zero at the working precision, exactly as in the accepted supported-return proof.

The $P$-term Neumann expansion therefore gives (2.2), with support width $\nu+P$. Its constant term is $z_i$; all HIGH corrections contain a factor $3$, so $\phi_i\equiv z_i\pmod3$.

To obtain the upper-degree gap, note that


$$
m-D=\frac H2-\frac{3D}{2}+\frac12.
$$


Because $H/\Omega$ is odd, the nearest grid centers around $H/2$ are


$$
\frac{H-\Omega}{2},
\qquad
\frac{H+\Omega}{2}.
$$


Condition (2.1) separates the upper center, including its width $\nu+P$, from the permitted quotient degrees. Hence


$$
\deg\psi_i\le\frac{H-\Omega}{2}+\nu+P,
$$


which implies the conservative bound (2.3).

Finally,


$$
(S_c)_{ij}=G_c(z_i,\widehat z_j^{\,c}).
$$


On the entire original degree space,


$$
g\longmapsto G_c(z_i,g)/3
$$


is integral: the $H_0$ top coefficient is absent, the possible $H_1$ coefficient already has its factor $3$, and every remaining term has that factor. Consequently


$$
\frac{(S_c)_{ij}}3
\equiv
\frac{G_c(z_i,\phi_j)}3
\pmod{3^P}.
\tag{2.7}
$$



The upper-degree gap removes the top coefficient altogether. The remaining complete normalized lower-pole polynomial is


$$
x^H x^D y^i\psi_j(\beta+3y).
$$


Its nongrid width is at most


$$
D+i+1+(\nu+P)\le2D-2+P,
$$


which is less than $(\Omega-1)/2$. All surviving extractions vanish. The factorial term has already been accounted for. Equation (2.7) proves (2.4). ∎

### Application at $P=19$

On (1.1),


$$
\frac{\Omega}{D}
=\frac{H}{3^{18}D}
>
\frac{C_{16}}{3^{18}}
=\frac{147968}{27}
>5480.
\tag{2.8}
$$



Also $D\ge486$. Thus all inequalities in Proposition 2.1 hold, and its upper-degree gap is much larger than $36$.

We obtain representatives


$$
\boxed{
\widehat z_i^{\,c}\equiv\phi_i=x^D\psi_i\pmod{3^{19}},
\qquad
\deg\phi_i\le m-36,
}
\tag{2.9}
$$


and


$$
\boxed{S_c\in3^{20}M_\nu(\mathbb Z_3).}
\tag{2.10}
$$



This uses the original window, not a narrower cylinder or a larger polynomial space.

---

## 3. Transfer through the actual precision-$11$ producer jet

The accepted factorial-saturation theorem supplies


$$
R\equiv
R_{11}:=(y+1)x^{A-27}B_{11}(x)
\pmod{3^{11}},
\qquad \deg B_{11}\le27.
\tag{3.1}
$$



Choose any integral coefficient lift of $B_{11}$, and define


$$
Q_*:=Q_c+3^6R_{11}.
\tag{3.2}
$$



This auxiliary producer is used only inside an exact comparison. Its zero endpoint is **not** substituted for the actual endpoint.

Put


$$
c(y)=\beta+3y.
$$


Since $\beta$ is a $3$-adic unit, the polynomial


$$
L(y)=\beta^{-1}\sum_{a=0}^{12}
\left(-\frac{3y}{\beta}\right)^a
\tag{3.3}
$$


satisfies


$$
c(y)L(y)\equiv1\pmod{3^{13}},
\qquad \deg L\le12.
$$



For each core representative in (2.9), define the finite polynomial


$$
\boxed{
f_i=
\phi_i
\sum_{a=0}^{3}
\left(-3^6x^{-27}B_{11}(x)L(y)\right)^a.
}
\tag{3.4}
$$



Despite the displayed Laurent notation, every term in (3.4) is a polynomial: $\phi_i$ is divisible by $x^D$, and


$$
D\ge486>3\cdot27.
$$


Furthermore,


$$
\deg f_i\le\deg\phi_i+36\le m.
\tag{3.5}
$$


Thus the construction stays inside the original finite polynomial space.

### Lemma 3.1 — Polynomial inverse transfer

Coefficientwise,


$$
\boxed{Q_*f_i\equiv Q_c\phi_i\pmod{3^{19}}.}
\tag{3.6}
$$



### Proof

Write formally $a=x^{-27}B_{11}(x)$. Then


$$
Q_*=(y+1)x^A(c+3^6a).
$$


The truncated geometric product in (3.4) has two sources of error:

- replacing $c^{-1}$ by $L$, whose error is divisible by $3^{13}$, multiplied by at least $3^6$;
- the first omitted geometric term, divisible by $3^{24}$.

Both are divisible by $3^{19}$. After multiplication by $x^A\phi_i$, all coefficients are integral. This proves (3.6). ∎

### Proposition 3.2 — The saturated-jet Schur complement vanishes modulo $3^{19}$

Let $S_*$ be the Schur complement for $Q_*$, eliminating the same $W=[U\ Y]$. Then


$$
\boxed{S_*\in3^{19}M_\nu(\mathbb Z_3).}
\tag{3.7}
$$



### Proof

The normalized eliminated blocks remain units: $Q_*-Q_c$ has the factor $3^6$, and all relevant coefficient maps are integral after the accepted LOW normalization. In particular, the corrected columns $\widehat Z^*$ are integral and


$$
\widehat z_i^*\equiv z_i\pmod3.
\tag{3.8}
$$



By (3.6), for every integral polynomial $g$ of degree at most $m$,


$$
G_*(f_i,g)\equiv G_c(\phi_i,g)\pmod{3^{19}}.
\tag{3.9}
$$


All product degrees remain within the original cutoff.

Take $g$ to be a corrected column $\widehat z_j^*$. The difference


$$
\phi_i-\widehat z_i^{\,c}
$$


has coefficients in $3^{19}\mathbb Z_3$, while the exact core corrected column pairs with any degree-$\le m$ polynomial through $S_c$. By (2.10), the right side of (3.9) is zero modulo $3^{19}$.

The residual coordinate matrix of the $f_i$ is congruent to the identity modulo $3$, because $f_i\equiv z_i\pmod3$. Orthogonality of $\widehat Z^*$ to $W$ therefore turns (3.9) into a unit left multiple of $S_*$. This proves (3.7), without any inverse of $S_*$. ∎

---

## 4. Restore the complete producer remainder before normalization

Define the actual integral remainder


$$
\boxed{
\Delta=\frac{R-R_{11}}{3^{11}},
\qquad \deg\Delta\le A+1.
}
\tag{4.1}
$$


Then, exactly,


$$
Q_{\rm act}=Q_*+3^{17}\Delta.
\tag{4.2}
$$



Let


$$
K_\Delta(f,g)=\mathcal M(\Delta fg),
$$




$$
\Phi_\Delta=K_\Delta(\widehat Z^*,\widehat Z^*),
\qquad
T_\Delta=K_\Delta(W,\widehat Z^*).
$$



The exact Schur perturbation identity gives


$$
\boxed{
S_{\rm act}
=
S_*+3^{17}\Phi_\Delta
-3^{34}T_\Delta^TE_{\rm act}^{-1}T_\Delta.
}
\tag{4.3}
$$



This restores the whole actual correction. It does not retain only the selected jet.

The accepted eliminated-block estimate is


$$
E_{\rm act}^{-1}\in3^{-1}M(\mathbb Z_3),
$$


so the last term in (4.3) belongs to $3^{33}M$.

For every integral $g$ of degree at most $m$,


$$
\boxed{K_\Delta(z_i,g)/3\in\mathbb Z_3.}
\tag{4.4}
$$


Indeed,


$$
\deg(\Delta z_i g)\le A+d+m=r_*,
\qquad r_*=\frac{3H-1}{2},
$$


so the endpoint-subtracted quotient has degree below the unique valuation-zero pole.

Write


$$
\widehat Z^*=Z+3V_*,
$$


with $V_*$ integral. Equation (4.4) implies


$$
\Phi_\Delta
\equiv K_\Delta(Z,Z)\pmod9,
\qquad
\Phi_\Delta\in3M.
\tag{4.5}
$$



Combining (3.7), (4.3), and (4.5) yields the main divisibility result.

### Theorem 4.1 — Actual depth-$18$ divisibility

On the original window (1.1),


$$
\boxed{S_{\rm act}\in3^{18}M_\nu(\mathbb Z_3).}
\tag{4.6}
$$



Since $S_{\rm act}=-3^{16}\Psi$,


$$
\boxed{\Psi\in9M_\nu(\mathbb Z_3).}
\tag{4.7}
$$



More precisely, with


$$
\Theta=-S_{\rm act}/3^{18},
$$


one has


$$
\boxed{
\Theta_{ij}
\equiv
-\frac{\mathcal M(\Delta z_i z_j)}3
\pmod3.
}
\tag{4.8}
$$



This is a statement about the complete actual form.

---

## 5. Explicit evaluation of the first unsettled normalized layer

Formula (4.8) can be evaluated further without a residual inverse.

For $0\le i,j<\nu$,


$$
\deg(\Delta z_i z_j)\le H+2D-3<r_*.
\tag{5.1}
$$


Thus the top pole is absent.

Modulo $9$, the only remaining pole that can contribute is the denominator $H$, at


$$
r_1=\frac{H-1}{2}.
$$


All other poles have weights divisible by $9$, and the factorial term is divisible by $9$.

Therefore the complete expression is


$$
\boxed{
\Theta_{ij}\equiv
-[y^{r_1}]
\frac{
\Delta(y)x^{2D}y^{i+j}
-\Delta(-1)(-2)^{2D}(-1)^{i+j}
}{y+1}
\pmod3.
}
\tag{5.2}
$$



The endpoint subtraction has not been omitted.

For the actual remainder,


$$
\Delta(-1)
=\frac{Q_{\rm act}(-1)}{3^{17}}
=-\frac{F^2\xi_n}{3^{17}}.
\tag{5.3}
$$


For sufficiently large original indices this is divisible by $3$. Hence


$$
\overline\Delta(y)=(y+1)D_{\rm next}(y)
\quad\text{in }\mathbb F_3[y],
\tag{5.4}
$$


where $\deg D_{\rm next}\le A$.

Define the actual polynomial


$$
P_{\rm next}(y)=x^{2D}D_{\rm next}(y)\in\mathbb F_3[y].
\tag{5.5}
$$



Then (5.2) becomes


$$
\boxed{
\Theta_{ij}\equiv-[y^{r_1-i-j}]P_{\rm next}(y)\pmod3.
}
\tag{5.6}
$$



Thus the entire next normalized leading form is determined by the consecutive coefficient window


$$
\boxed{
[y^{r_1-(D-4)}]P_{\rm next},
\ldots,
[y^{r_1}]P_{\rm next}.
}
\tag{5.7}
$$



This is a specific actual-producer coefficient law. It is not a general Hankel determinant representation.

### Independence of the chosen lift

Replacing $B_{11}$ by $B_{11}+3^{11}C$, with $\deg C\le27$, changes $\Delta$ by


$$
-(y+1)x^{A-27}C.
$$


The resulting change in $P_{\rm next}$ is


$$
-x^{H+D-27}C.
$$


Modulo $3$,


$$
x^{H+D-27}C=(y^H-1)x^{D-27}C.
$$


Its low-degree part has degree at most $D$, while its high-degree part begins at degree $H$. Neither reaches the window (5.7). Thus the evaluated moment window is independent of the integral lift.

---

## 6. All twenty features are included in the cancellation

The accepted exact identity is


$$
\Psi=
\mathcal B^TH_{\rm inv}\mathcal B
+27a_1^TMa_1
+\mathcal F^T\mathcal J\mathcal F
-\frac{\Phi_R}{3^{10}}
-\frac{S_c}{3^{16}},
\tag{6.1}
$$


where $\mathcal F$ has all twenty slots on this window.

Theorem 4.1 proves the actual cancellation


$$
\boxed{
\mathcal B^TH_{\rm inv}\mathcal B
+27a_1^TMa_1
+\mathcal F^T\mathcal J\mathcal F
-\frac{\Phi_R}{3^{10}}
-\frac{S_c}{3^{16}}
\equiv0\pmod9.
}
\tag{6.2}
$$



No individual term in (6.2) has been presumed divisible by $9$. In particular, the proof does not separately discard

- the HIGH bulk;
- any of the eighteen LOW feature slots;
- either terminal feature;
- the complete linear force;
- the core contribution.

Their **whole sum** vanishes. This is why working through the complete producer and Schur complement is useful here.

---

## 7. Consequences for the actual Hankel moments and complete forcing

The relevant algebra in Turn 11 is division-safe:

- the Krylov matrix has determinant $1$;
- $r_{\rm act}\equiv e_{\nu-1}\pmod3$;
- the actual normalizing polynomial satisfies $\mathsf R\equiv1\pmod3$;
- hence
  

$$
\mathsf V\in\mathrm{GL}_\nu(\mathbb Z_3),
  \qquad \mathsf V\equiv I\pmod3.
$$



The interior companion displacement then gives the Hankel law


$$
\mathsf H=\mathsf V^T\Psi\mathsf V,
\qquad
\mathsf H_{ij}=\mu_{i+j}.
\tag{7.1}
$$



These facts use no residual inverse and no simple-root hypothesis. The repeated-root factorization of $f\bmod3$ remains an obstruction to an étale argument, but it is irrelevant to the coefficient-support proof above.

### Corollary 7.1 — Evaluation of all leading moments



$$
\boxed{
\mu_k\equiv0\pmod9
\qquad(0\le k\le2\nu-2).
}
\tag{7.2}
$$



This includes both the initial moments and those obtained from the complete forced recurrence.

The sheared displacement vector also gains two digits. Since


$$
t_{\rm act}-\theta r_{\rm act}
$$


has zero last coordinate, the displacement identity and $S_{\rm act}\in3^{18}M$ imply


$$
a^{[2]}:=
\frac{t_{\rm act}-\theta r_{\rm act}}{3^{18}}
\in\mathbb Z_3^\nu.
\tag{7.3}
$$


Thus the old vector $a$, and hence the old forcing $b=\mathsf V^Ta$, are divisible by $9$.

Put


$$
b^{[2]}=\mathsf V^Ta^{[2]}=b/9,
\qquad
\mu_k^{[2]}=\mu_k/9.
$$


Then the entire normalized recurrence is


$$
\boxed{
\mu_{i+\nu}^{[2]}
+\sum_{k=0}^{\nu-1}f_k\mu_{i+k}^{[2]}
=b_i^{[2]},
\qquad0\le i\le\nu-2.
}
\tag{7.4}
$$



Modulo $3$, (5.6) evaluates its moments:


$$
\boxed{
\mu_k^{[2]}
\equiv-[y^{r_1-k}]P_{\rm next}(y).
}
\tag{7.5}
$$



Since $f\bmod3=q_d$, its interior forcing is explicitly


$$
\boxed{
b_i^{[2]}
\equiv-[y^{r_1-i}]P_{\rm next}(y)q_d(y)
\pmod3,
\quad0\le i\le\nu-2.
}
\tag{7.6}
$$


The final component satisfies


$$
b_{\nu-1}^{[2]}\equiv0\pmod3,
\tag{7.7}
$$


because $a_{\nu-1}^{[2]}=0$ exactly and $\mathsf V\equiv I\pmod3$.

No moment outside $0,\ldots,2\nu-2$ is introduced.

---

## 8. Actual radicals and the endpoint return

### Theorem 8.1 — Leading and next induced radical classification

Over $\mathbb F_3$,


$$
\boxed{
\operatorname{rank}(\mathsf H\bmod3)=0,
\qquad
\operatorname{rad}(\mathsf H\bmod3)=\mathbb F_3^\nu.
}
\tag{8.1}
$$



The induced next normalized form on this radical is


$$
\mathsf H/3\bmod3=0.
\tag{8.2}
$$


It again has rank zero and radical $\mathbb F_3^\nu$.

At both levels, the actual endpoint functional is


$$
\boxed{
\overline\varepsilon(x)
=\sum_{i=0}^{\nu-1}(-1)^ix_i.
}
\tag{8.3}
$$


It is surjective onto $\mathbb F_3$, and its kernel has dimension $\nu-1$.

### Proof

The two zero-form statements follow from $\mathsf H\in9M$.

The endpoint congruence follows from the actual corrected columns and $\mathsf V\equiv I\pmod3$:


$$
\varepsilon_i\equiv z_i(-1)\equiv(-1)^i.
$$


Its first coordinate is $1$, so the functional is nonzero and has the stated kernel dimension. ∎

This is a radical theorem for the actual leading finite forms. It is **not** a statement that the characteristic-zero radical has dimension $\nu$.

### Complete endpoint transport after renormalization

The endpoint identity becomes


$$
\boxed{
J^T\varepsilon+\omega
=
-\varepsilon
-s\bigl(\theta e_{\nu-1}+3^{18}b^{[2]}\bigr),
}
\tag{8.4}
$$


where


$$
\omega=(B_{WZ}\mathsf V)^TW(-1).
$$


The full return block $B_{WZ}$ remains present.

Modulo $3$,


$$
\omega_i=0\quad(0\le i<\nu-1),
$$


but its final component is


$$
\boxed{\omega_{\nu-1}\equiv q_d(-1)\pmod3.}
\tag{8.5}
$$


It must not be set to zero without evaluating $q_d(-1)$. Thus even at the zero leading-form layers, the endpoint closure retains its actual terminal return.

---

## 9. Exact determinant-pair renormalization

Define


$$
\Delta_0=\det\Theta,
$$




$$
\boxed{
\Delta_1=
e_{\rm act}^T\operatorname{adj}(\Theta)e_{\rm act}
-3^{18}d_{\rm act}\det\Theta.
}
\tag{9.1}
$$



Since $\Psi=9\Theta$,


$$
\boxed{
\delta_0=3^{2\nu}\Delta_0,
\qquad
\delta_1=3^{2\nu-2}\Delta_1.
}
\tag{9.2}
$$



In particular,


$$
v_3(\delta_0)\ge2\nu,\qquad
v_3(\delta_1)\ge2\nu-2,
\tag{9.3}
$$


with the convention $v_3(0)=+\infty$.

If both pairs are nonzero, then


$$
\boxed{
v_3(\delta_1)-v_3(\delta_0)
=-2+v_3(\Delta_1)-v_3(\Delta_0).
}
\tag{9.4}
$$



The actual boundary subtraction is now $3^{18}d_{\rm act}$, not $3^{16}d_{\rm act}$. Since


$$
d_{\rm act}\in3^{-1}\mathbb Z_3,
$$


its normalized coefficient is in $3^{17}\mathbb Z_3$.

The unit-resultant transfer gives the equivalent complete Hankel pair


$$
\Delta_0=\mathfrak u^2\det\mathsf H^{[2]},
$$




$$
\boxed{
\Delta_1=\mathfrak u^2
\left(
\varepsilon_0^2\det\mathsf H_{\partial}^{[2]}
-3^{18}d_{\rm act}\det\mathsf H^{[2]}
\right).
}
\tag{9.5}
$$



The unknown is still the valuation of the **whole difference** in (9.5).

---

## 10. A concrete next producer lemma

The depth-$18$ formula identifies a smaller, specific next obligation.

> **Next-digit saturation lemma.**  
> Establish from the actual precision-$12$ producer formula that, modulo $3$,
> 

$$
> \Delta(y)\in
> (y+1)x^{A-\kappa}\mathbb F_3[y]
>
$$


> for some $27\le\kappa\le D$, with the quotient of degree at most $\kappa$.

If this lemma holds, then


$$
P_{\rm next}
=x^{H+D-\kappa}C
=(y^H-1)x^{D-\kappa}C
\quad\text{in }\mathbb F_3[y],
$$


with $\deg C\le\kappa$. Its support is contained in


$$
[0,D]\ \cup\ [H,H+D].
$$


That support misses every index in (5.7). Hence


$$
\Theta\equiv0\pmod3.
$$



This deduction is rigorous, but the required actual precision-$12$ tail bound is **not explicitly supplied in the attached text**. The attachment supplies $\kappa_{11}=27$, not the next complete jet or its exact tail calculation. I therefore do not silently promote the last conditional deduction to an evaluated depth-$19$ theorem.

This is a different next obligation from the previous unevaluated determinant lemma: it concerns one specified producer digit and one specified coefficient window. It is also only an intermediate obligation. Additional zero layers would still not prove determinant nonvanishing or a useful relative valuation.

---

## 11. Bounded exact arithmetic: original inputs, precision, and output

No computation is needed for Theorems 4.1 and 8.1. Their conclusions are symbolic original-family results.

A next finite calculation can evaluate (5.7) without constructing a residual matrix or presuming any residual pivot.

### 11.1 Original inputs

Use a **certified original** tuple


$$
(j,n,H,D,h)
$$


satisfying (1.1), including the accepted sufficiently-large conditions.

Do not substitute auxiliary values for $n=4^j+1$.

The producer input required is


$$
R\bmod3^{12}.
$$


By the accepted producer-precision theorem, a sufficient upstream producer-input modulus is


$$
\boxed{3^{19}.}
\tag{11.1}
$$



The complete definitions of the upstream Pascal matrix and complete force used to generate those digits are not reproduced in the attachments. Accordingly, this report does not claim that an end-to-end producer implementation is reproducible from these attachments alone. That original generator must be inspected personally before accepting a numerical output.

### 11.2 Deterministic arithmetic once the actual producer coefficients are supplied

1. Reduce $R\bmod3^{11}$.

2. Divide by the monic polynomial
   

$$
(y+1)x^{A-27}
$$


   over $\mathbb Z/3^{11}\mathbb Z$.  
   The accepted saturation theorem requires zero remainder and quotient degree at most $27$.

3. Choose coefficient representatives for that quotient and form $R_{11}$.

4. Compute
   

$$
\overline\Delta
   =
   (R-R_{11})/3^{11}\pmod3.
$$


   The division is performed only after verifying the whole coefficientwise difference is divisible by $3^{11}$.

5. Verify
   

$$
\overline\Delta(-1)=0.
$$


   Divide by $y+1$ in $\mathbb F_3[y]$ to obtain $D_{\rm next}$.

6. Evaluate the $D-3$ coefficients
   

$$
c_k=[y^{r_1-k}]x^{2D}D_{\rm next},
   \qquad0\le k\le D-4.
   \tag{11.2}
$$



7. Report the actual leading moment vector
   

$$
(\mu_k^{[2]}\bmod3)_{k=0}^{D-4}=(-c_k)_{k=0}^{D-4}.
$$



### 11.3 Explicit coefficient evaluation and bounded storage

If


$$
D_{\rm next}(y)=\sum_{a=0}^{A}d_ay^a,
$$


then


$$
\boxed{
c_k=
\sum_{\substack{0\le a\le A\\0\le r_1-k-a\le2D}}
d_a
(-1)^{\,2D-(r_1-k-a)}
\binom{2D}{r_1-k-a}
\pmod3.
}
\tag{11.3}
$$



Each binomial is evaluated by Lucas’s theorem on the ternary digits of its two nonnegative indices. No simple-root hypothesis is involved.

A direct implementation has:

- coefficient storage bounded by $A+2$ field elements;
- output length $D-3$;
- indices bounded by $A+2D$;
- Lucas digit depth at most
  

$$
1+\lfloor\log_3(2D)\rfloor.
$$



These are explicit finite bounds, but they grow with the original index. Practical execution for a very large original index is **not** established here.

### 11.4 Expected verifiable output

The report should contain:

- the exact original-index certificate;
- the producer modulus and provenance;
- zero saturation remainder at precision $11$;
- zero endpoint remainder modulo $3$;
- the complete coefficient vector (11.2);
- optionally, the first nonzero Taylor coefficient of $\overline\Delta/(y+1)$ at $y=1$, certifying the next tail length;
- the complete forcing residues from (7.6), including the final component check (7.7).

No particular nonzero coefficient is predicted here. If the vector is zero, that proves only the stated finite input’s next zero layer unless the tail-length argument is proved uniformly.

This is an original-data calculation, not a synthetic matrix identity check.

---

## 12. Primitive denominator and the whole evaluated error

The same archived rational approximant is retained.

When $\Delta_0\ne0$,


$$
\boxed{
\frac{\beta_1}{\beta_0}
=
\frac{3^{h-18}F^2\xi_n}{4}
\frac{\Delta_1}{\Delta_0}.
}
\tag{12.1}
$$



If both members are nonzero,


$$
\boxed{
v_3(q)=
\max\left\{
0,\,
h-18+2v_3(F)
+v_3(\Delta_1)-v_3(\Delta_0)
\right\}.
}
\tag{12.2}
$$



The common powers proportional to $\nu$ cancel. The new divisibility is not a gain of $2\nu$ in the primitive denominator.

Restore


$$
Q_n=\lambda Q_{\rm act},
\qquad
R_{\rm rat}=\frac{4\lambda}{3^h}G_{\rm act},
$$




$$
H_{\rm complete}
=
R_{\rm rat}+(e+\pi)Q_n(-1)vv^T.
$$



Retain


$$
\beta_0=\det R_{\rm rat},
\qquad
\beta_1=Q_n(-1)v^T\operatorname{adj}(R_{\rm rat})v.
$$



Let $\ell_{\rm clr}$ be the least actual original clearing integer, and $k_0=m+1$. Define


$$
A_\ell=\ell_{\rm clr}^{k_0}\beta_0,
\qquad
B_\ell=\ell_{\rm clr}^{k_0}\beta_1,
$$




$$
\boxed{g_\ell=\gcd(|A_\ell|,|B_\ell|).}
\tag{12.3}
$$



Every prime remains in this gcd. When $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},
\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$



The whole same-index error is still


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{k_0}}{g_\ell}
\det H_{\rm complete}.
}
\tag{12.4}
$$



Nothing proved here establishes the least clearer, the all-prime gcd, nonvanishing of this whole error, or its decay.

---

## 13. Proof-status ledger and final bottleneck

| Statement | Status |
|---|---|
| Complete finite core representatives modulo $3^{19}$, with an upper-degree gap | Proved here using the accepted complete return formulas |
| Saturated-jet Schur complement $S_*\in3^{19}M$ | Proved here by finite polynomial inverse transfer |
| Restoration of the full actual producer remainder | Exact Schur identity, retained |
| Actual $S_{\rm act}\in3^{18}M$ | Proved here |
| Actual $\Psi,\mathsf H\in9M$ | Proved here |
| All original complete moments $\mu_k\equiv0\pmod9$ | Proved here |
| Complete forcing $b\in9\mathbb Z_3^\nu$ | Proved here |
| Leading radical and next induced radical are the whole original residual space | Proved over $\mathbb F_3$ |
| Actual endpoint action on both radicals | Evaluated explicitly |
| Complete endpoint return $B_{WZ}$ | Retained; terminal residue is not discarded |
| Depth-$18$ leading moments as one actual producer coefficient window | Derived explicitly |
| Numerical evaluation of that next producer window | Not performed |
| Uniform next-digit saturation bound | Outstanding in the supplied data |
| Characteristic-zero residual nonvanishing and relative valuation | Unresolved |
| Least clearer, full gcd, primitive denominator, and whole-error comparison | Unresolved |

### New result

The leading normalized actual moment problem is no longer unevaluated:


$$
\boxed{
\mathsf H\bmod3=0,\qquad
(\mathsf H/3)\bmod3=0.
}
$$



Both radicals are exactly the entire original residual space, and the actual endpoint is explicitly nonzero on them. The first unsettled normalized form has been reduced to the concrete actual coefficient window (5.7), with its complete forcing given by (7.6).

### Exact remaining mathematical bottleneck

There are now two distinct remaining stages:

1. **Local arithmetic:** evaluate the depth-$18$ producer window, continue normalization only with proved precision, and ultimately determine nonvanishing and the relative valuation of
   

$$
\det\Theta,\qquad
   e_{\rm act}^T\operatorname{adj}(\Theta)e_{\rm act}
   -3^{18}d_{\rm act}\det\Theta.
$$



2. **Global irrationality argument:** control the least clearer, the full all-prime gcd, the actual primitive denominator, and the whole nonzero error (12.4).

The unit normalizer solves neither stage by itself. Nor does a large radical modulo $3$ imply a characteristic-zero radical.



$$
\boxed{\text{No unconditional proof or disproof of irrationality of }e+\pi
\text{ has been obtained.}}
$$


