> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 — relative-law audit, same-center CRT consequence, and the fourth-saturation obstruction

## Summary

- **The strengthened analytic argument passes:** with the exact reconstruction and complete-residual identities supplied in the archive, it proves the relative law on $3\le b=o(\sqrt n)$, uniformly in every actual coordinate and every positive diagonal metric in those coordinates.
- **The variable-$k$ ternary calculation passes.** In particular, the $b+2$ factorial tail is necessary, the factorial unit is $(-1)^a$, and the endpoint does not cancel the coordinate-zero contribution.
- Combining these results with the audited dyadic law gives an **unconditional exclusion of shrinking of the specified primitive CRT center forms**, not an exclusion of other approximation routes.
- For the separate weighted family, I derive the exact modulo-$81$ binomial grid, prove annihilation by the complete direct pole form on $27\mid j,\ D<H/108$, and give a **new explicit fourth-carry formula** retaining the HIGH inverse and the first LOW unit-block correction. **I do not obtain an evaluated fourth rank.** Direct pole annihilation alone does not justify rank zero.

These statements do not decide irrationality of $e+\pi$.

---

## 1. Independent audit of the strengthened relative law

Write


$$
\sigma=\sqrt2,\quad M=1+\sqrt2,\quad d=b-1,\quad S=e+\pi.
$$



### 1.1 Same-$n,d$ moments and boundary terms

For the positive principal ensemble in A3 turn 13, the ordered chamber is convex. Its one-particle potential after a bounded $Q$-tilt is


$$
V_\tau(t)=-n\log(1+\sigma\cos t)+\sigma\cos t-\tau t^2.
$$


The displayed curvature computation gives, uniformly for bounded $\tau$,


$$
V_\tau''(t)\ge cn,\qquad tV_\tau'(t)\ge cn t^2
$$


for sufficiently large $n$. The second inequality follows from the first and $V_\tau'(0)=0$.

The virial identity has the correct pair coefficient:


$$
\mathbb E_\tau\sum_i\theta_iV_\tau'(\theta_i)
=d+\mathbb E_\tau\sum_{i<j}
(\theta_i-\theta_j)\cot\frac{\theta_i-\theta_j}{2}.
$$


Since each pair term is at most $2$, the right side is at most $d^2$.

The boundary justification is valid. Endpoint density vanishes like a positive integer power of distance; collision density vanishes quadratically. The boundary fluxes tend to zero, while the differentiated collision singularity is integrable. Multiplication by $Q$, or by $e^{\tau Q}$ for fixed $\tau$, does not change this conclusion on the bounded chamber.

Thus, at the **same $n,d$**,


$$
\mathbb E_\tau Q\ll d^2/n,\qquad
\mathbb E_\tau Q^2\ll d^4/n^2.
$$


Integrating the $Q$-tilt derivative gives the exponential moment bounds used by A3.

### 1.2 Real trace tilts and the complex disks

A real tilt $e^{tX}$, $X=\sum_i\theta_i$, changes the potential only by a linear term. Its Hessian is unchanged, so Brascamp–Lieb applies for every real $t$:


$$
\operatorname{Var}_tX\ll d/n.
$$


Reflection gives $\mathbb EX=0$ at $t=0$, not at every tilt. Integrating the log-mgf second derivative therefore gives


$$
\mathbb Ee^{tX}\le e^{Ct^2d/n}.
$$


This is precisely the concentration statement required; no complex probability measure is being used.

Both closed $q$-disks avoid $|q|=1$. Hence the logarithm anchored at $t=0$ has uniformly bounded second $t$-derivative on the whole principal interval. The expansion


$$
\log\frac{e^{-it}+q}{1+q}
=-\frac{i}{1+q}t+O(t^2)
$$


is consequently valid in **complex modulus**, uniformly throughout both disks.

The gamma estimate also checks:


$$
|S_j-1|
\le \sum_{\ell=1}^{d}\binom d\ell(\sigma/n)^\ell
\le e^{\sigma d/n}-1.
$$


The actual middle-coordinate references are positive combinations, so this bound is uniform in $0\le j\le b$.

Combining these facts gives


$$
\frac{A_j^{\rm pr}(q)}
{s_jB_jZ_d(0)(1+q)^d}
=1+O(d^2/n)
$$


when $d^2/n\to0$. The Cauchy–Schwarz step uses the $Q^2e^{KQ}$ estimate, not merely an unweighted second moment.

The same-$n$ adjacent-norm estimate controls every outer sector. Passing to $Z_d(0)|1+q|^d$ costs only $e^{O(d)}$; thus the omitted signed contribution is $e^{-cn+O(d)}$. This includes the actual odd-$n$ signs.

### 1.3 Scalar normalization and the complete error

The saddle displacement is $O(d/n)$; its change in the exponent is $O(d^2/n)$. The limiting angular curvatures are


$$
\lambda_+=\sigma/M,\qquad \lambda_-=\sigma M.
$$


The ratio of scalar prefactors is exactly


$$
\frac{2n!}{n!/(2\pi)}=4\pi.
$$


The characteristic ratio contributes $M^{-d}$, and the Gaussian ratio contributes $M^{-1}$. Therefore


$$
\frac{F_j}{P_j}
=4\pi M^{-2n-b}
\left(1+O(b^2/n+n^{-1/5})\right).
$$



Both minus connectors must be retained; the supplied scalar bounds make both exponentially negligible. The complete residual and endpoint remain


$$
c_j-S=\frac{E_j}{P_j}
+(-1)^{n+1}\frac{F_j}{P_j}
+(-1)^n\delta_{j0}\frac{D}{P_j}.
$$


Their bounds are factorially smaller than the displayed main term. Consequently


$$
\boxed{
c_W-S=(-1)^{n+1}4\pi M^{-2n-b}
\left(1+O(b^2/n+n^{-1/5})\right)
}
$$


on $3\le b=o(\sqrt n)$, with an absolute uniform error over all actual coordinates and positive diagonal metrics.

The determinant and every $u_j$ are eventually nonzero, and the **whole** error has the stated nonzero sign. This audit finds no new defect in A3 turn 13.

---

## 2. Audit of the variable-$k$ CRT arithmetic

Here


$$
b=3^a=9^r,\quad a=2r,\quad n=2h,\quad k=v_3(n)\ge a+1,
$$


and


$$
\beta=k+F_b-a,\qquad F_t=v_3(t!).
$$



The principal delicate steps check as follows.

1. **Whole Frobenius support.** The modulo-$9$ polynomial congruence applies to the full polynomial, including coefficients near degree $n$. Its support spacing is $3^{k-1}$, a multiple of $b$. There is no assumption $k=a+1$.

2. **Central unit.** Digitwise constant-term factorization is legitimate because the lowest remaining Laurent exponent lies in $[-2,2]$; divisibility by $3$ forces it to be zero. Thus
   

$$
J\equiv(-1)^{\nu_3(n)}\pmod3.
$$



3. **Factorial units.** For $P_i=(2n+i)_{\underline b}$, the nonzero shifts have their ordinary shift valuations. Lucas gives
   

$$
\binom{b-1}{i}\equiv(-1)^i\pmod3.
$$


   These signs cancel the negative-shift signs. The unit of $(3^a-1)!$ is $(-1)^a$, giving
   

$$
3^{-\beta}P_i\equiv2u(-1)^a\pmod3.
$$



4. **The $b+2$ tail.** It cannot be discarded:
   

$$
P_i+P_ix_i+P_ix_i(x_i-1)=P_i(1+x_i^2).
$$


   All later tails contain three consecutive additional factors. Therefore
   

$$
3^{-\beta}\rho_i\equiv2u(-1)^a(1+i^2)\pmod3.
$$



5. **Inverse precision.** Applying an $O(3^k)$ inverse correction to $\rho\in3^\beta\mathbb Z_3^b$ produces $O(3^{\beta+k})$, regardless of whether $k<\beta$.

6. **Endpoint and ordinary lift.** The endpoint has unit
   

$$
3^{-\beta}\omega_b\equiv u(-1)^a,
$$


   while its mixed contraction is deeper because $3\mid Z_{w,b}$. Also $\beta\ge F_b+1$, so ordinary factorial divisions preserve integrality of the $Q$-correction. The $P$-scalar supplies more than the required factorial depth.

Thus


$$
v_3(\mathfrak D)=1,\quad v_3(\mathfrak C)=\beta,\quad v_3(d_B)=0
$$


and the mixed contraction is genuinely nonzero.

The dyadic boundary truncation and precision-transfer argument likewise give the required units; in particular, the coefficient $90$ accounts for the removed out-of-range row. Its use is not an extrapolation from the finite control record.

Retaining the actual least lift and final Gram gcd,


$$
A_B=N_{B,1}^{T}\Omega N_{B,1},\quad
H_B=N_{B,1}^{T}\Omega N_{B,2},\quad
g_B=\gcd(A_B,|H_B|),\quad q=A_B/g_B,
$$


the exact local denominator laws are


$$
v_2(q)=\frac32n-v_2(b!)-s_2(n)-1,
$$




$$
v_3(q)=n-s_3(n)+1-\beta.
$$



### Same-center exclusion

For the prescribed least CRT representatives,


$$
n=2b^3+O(b^2),\qquad b=o(\sqrt n).
$$


The audited relative law therefore applies to these **same centers and the same actual factorial metric**. With $p=H_B/g_B$,


$$
qS-p=4\pi qM^{-2n-b}(1+o(1))>0
$$


eventually, since $n$ is even. Hence


$$
\boxed{
\liminf\frac{\log|qS-p|}{n}
\ge \frac32\log2+\log3-2\log M>0.
}
$$


This excludes shrinking of this selected primitive center form on this CRT sequence. It says nothing about the weighted family below or other endpoint directions.

---

## 3. Fourth saturation: exact modulo-$81$ grid

Now return to the **different** weighted family. Retain A4’s notation


$$
A=4^j-1,\quad H=3^{h-1},\quad D=H-A,\quad
d=\frac{3D}{2}-1,\quad \nu=\frac D2-1.
$$


Restrict to


$$
\boxed{27\mid j,\qquad D<H/108.}
$$


A1’s corrected ray then gives


$$
Q_n^{\rm loc}\equiv(y+1)(y-1)^A(3y+10)\pmod{81}.
$$



Put $H=3^s$, $s\ge3$, and $K=H/27$. Then


$$
\boxed{(y-1)^H\equiv (y^K-1)^{27}\pmod{81}.}
$$



Here is an elementary precision proof. Since


$$
(y-1)^3=(y^3-1)-3y(y-1),
$$


the difference between its $3^{t-1}$-st power and $(y^3-1)^{3^{t-1}}$ has terms of valuation at least


$$
v_3\binom{3^{t-1}}{\ell}+\ell
=t-1-v_3(\ell)+\ell\ge t.
$$


For $t\ge4$, the difference vanishes modulo $81$. Iteration reduces to exponent $27$.

Moreover,


$$
v_3\binom Hr=s-v_3(r),\qquad 0<r<H,
$$


so the interior support modulo $81$ is **exactly** the $H/27$ grid.

Writing the coefficient of $y^{rK}$ as $c_r$, the first half is


$$
(c_1,\ldots,c_{13})
=(27,-27,9,27,-27,-36,27,-27,3,27,-27,36,27)
\pmod{81},
$$


with


$$
c_0=-1,\quad c_{27}=1,\quad c_{27-r}=-c_r.
$$


This is an actual degree-$27$ coefficient calculation, not a guessed next-depth pattern.

---

## 4. All direct poles annihilate the lifted radical

Let


$$
P(y)=(y-1)^A(3y+10),\qquad z_i=y^i(y-1)^D.
$$


The LOW block modulo $81$ retains all four pole layers:


$$
\begin{aligned}
L_{ab}\equiv {}&
[y^{(H-1)/2}]Py^{a+b}\\
&+3\sum_c c^{-1}[y^{(cH/3-1)/2}]Py^{a+b}\\
&+9\sum_c c^{-1}[y^{(cH/9-1)/2}]Py^{a+b}\\
&+27\sum_c c^{-1}[y^{(cH/27-1)/2}]Py^{a+b}\pmod{81}.
\end{aligned}
$$


Each sum runs over **every** positive odd $3$-adic unit $c$ satisfying the original cutoff. In particular, no $h-4$ unit has been omitted.

For a radical vector paired with a LOW monomial,


$$
(y-1)^Az_i y^a=y^{i+a}(y-1)^H,
\qquad i+a\le2D-4.
$$


Including the linear core raises this shift by at most one.

At successive layers the requisite grids are $H/27,H/9,H/3,H$. Every relevant pole index is a half-grid index; its distance from the grid is at least


$$
\frac{H/27-1}{2}.
$$


Since $2D-3<H/54$, no permitted shift reaches a coefficient.

The inherited factorial and endpoint-depth bounds remain beyond this precision on the stated large-index domain. Thus


$$
\boxed{Z^TL\equiv0\pmod{81}.}
$$


This is a proved fourth-depth direct-pole statement. It is **not** yet the fourth saturation.

---

## 5. New bounded lemma: an explicit fourth HIGH/LOW carry

The following formula records exactly what still needs evaluation.

Let $U$ select LOW monomials of degrees $0,\ldots,D-1$, and set


$$
L_U=U^TLU,\qquad X_U=U^TX,\qquad V=Z^TX.
$$


The matrix $L_U$ is a unit matrix over $\mathbb Z_3$. Eliminate this block **before** HIGH and define


$$
\widehat E=E-3X_U^TL_U^{-1}X_U.
$$


Associativity of Schur complements gives the same final radical form as eliminating HIGH first.

Let $E_0$ be A4’s exact anti-triangular top-pole representative, and put


$$
R=E_0^{-1},\qquad
F=\frac{\widehat E-E_0}{3}.
$$


Thus $F$ retains the first LOW unit-block correction; it is not merely $(E-E_0)/3$.

From the previous mixed-block computation,


$$
V=-2ee_m^T+3K+9J
$$


for an integral matrix $J$, where


$$
K_{ib}=\mathbf1_{i+b=(H/3-1)/2}.
$$


Here $Re_m=e_d$, $R_{mm}=0$, and $Ke_d=0$.

The already proved third saturation, together with direct annihilation, implies


$$
F_{dd}\in3\mathbb Z_3.
$$


Expand the HIGH inverse through both additional digits:


$$
\widehat E^{-1}
\equiv R-3RFR+9RFRFR\pmod{27}.
$$



Define $\operatorname{Sym}(e,v)=ev^T+ve^T$. Direct multiplication now gives


$$
\boxed{
\begin{aligned}
\frac{V\widehat E^{-1}V^T}{9}\equiv {}&
KRK^T
-2\operatorname{Sym}(e,Je_d)\\
&+2\operatorname{Sym}(e,KRF e_d)\\
&+\left(4(FRF)_{dd}-4F_{dd}/3\right)ee^T
\pmod3.
\end{aligned}}
\tag{*}
$$



To see why this is the fourth saturation, the radical form after LOW-first elimination is, modulo $81$,


$$
\mathcal R\equiv-3V\widehat E^{-1}V^T.
$$


The terms involving $Z^TLU$ vanish to higher precision because $Z^TL\equiv0\pmod{81}$. Consequently


$$
\boxed{T_4=\mathcal R/27\equiv-\text{right side of (*)}\pmod3.}
$$



This identity is the new bounded follow-on result. It explicitly retains:

- the $V\bmod27$ correction $J$;
- the HIGH inverse through its quadratic correction;
- the first LOW unit-block correction inside $F$;
- the carry $F_{dd}/3$, which cannot be inferred from $F_{dd}\bmod3$.

### Exact obstruction

Neither direct-pole annihilation nor the third-rank recurrence evaluates the four terms in (*). In particular, the third-rank identity only proves $3\mid F_{dd}$; it does **not** evaluate $F_{dd}/3\bmod3$.

I therefore do not assert that $T_4=0$, give a fourth rank, or claim an endpoint-image exclusion. The actual endpoint residue remains


$$
\bigl((-1)^i\bigr)_{0\le i<\nu}\ne0,
$$


but whether it belongs to $\operatorname{im}T_4$ is unresolved.

The subclass is infinite by irrational rotation on the progression $27\mid j$, using any closed ratio interval strictly inside $1<H/A<108/107$.

---

## 6. Primitive scalar, gcd, and complete weighted error

Restore the actual primitive polynomial scalar


$$
\lambda=L_n/3\in\mathbb Z_3^\times.
$$


It multiplies the final Schur form, so the actual fourth matrix is $\lambda T_4$; ranks are unchanged.

Without an evaluated fourth rank, the established bound remains


$$
v_3(g)\ge d+3\nu=3D-4.
$$


**If** $T_4=0$ were proved, the closed normalization would instead give


$$
v_3(g)\ge d+4\nu=\frac{7D}{2}-5.
$$


This last assertion is conditional, not a new gcd theorem.

In either case retain the exact pair


$$
g=\gcd(|A_{\rm det}|,|B_{\rm det}|),\quad
q=\frac{|B_{\rm det}|}{g},\quad
p=-\frac{\operatorname{sgn}(B_{\rm det})A_{\rm det}}g.
$$


On the stated regular nonvanishing domain,


$$
qS-p
=\frac{\operatorname{sgn}(B_{\rm det})\ell^k}{g}
\det H_{\rm complete}.
$$


The exact local denominator interface remains


$$
v_3(q)=\max\!\left\{0,\,
h+2F_{n-1}-1+
v_3(\operatorname{adj}(S)_{\rm endpoint})
-v_3(\det S)\right\}.
$$


The cofactor is endpoint-transported. Lower Smith bounds cannot be subtracted to evaluate this expression.

---

## Closing ledger

### (1) New result and proof status

- **Audited:** the strengthened relative whole-error law and the variable-$k$ same-center CRT arithmetic.
- **Unconditional scoped consequence:** the specified primitive CRT forms grow exponentially and therefore do not supply shrinking forms.
- **Proved weighted follow-on:** exact modulo-$81$ binomial support and coefficients; complete direct-pole annihilation on $27\mid j,\ D<H/108$; explicit fourth-carry identity (*).
- **Not proved:** an evaluated fourth saturation rank or endpoint image.

### (2) Exact remaining bottleneck

For the weighted fourth saturation, evaluate the actual correction terms in (*), especially $F_{dd}/3\bmod3$ together with $Je_d$ and the quadratic HIGH carry. A cancellation identity linking these quantities would finish this step.

For irrationality, the larger unresolved requirement remains control of the **actual final denominator and nonzero whole evaluated error on one compatible family**. The CRT exclusion and weighted Smith divisibility do not supply that requirement.

### (3) Computation request

None at this stage. The outstanding task is a symbolic evaluation of (*); the coordinator’s prescribed $(4482,9)$ certificate is separate finite corroboration of the CRT arithmetic, not evidence for the weighted fourth rank.
