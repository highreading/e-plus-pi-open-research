> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1 turn11 — An algebraic endpoint connection and an obstruction to fixed-rank exact digit normalization

## Executive conclusion

The outstanding normalization problem is not resolved. There is, however, a sharper structural conclusion than the prime-power ambient bound in turn10:

> **The exact joint endpoint sequence has infinite observable rank under unrestricted ternary digit extraction in characteristic zero.**  
> Consequently, an exact, fixed finite-rank saturated observable lattice, stable under all three digit maps up to fixed controlled scalars, cannot represent these endpoints.

This is not a statement about the rank at a fixed modulus, and it does not exclude a nonlinear normalized construction with additional valuation data. It also does not exclude a construction restricted to a genuinely smaller language of original-power inputs. Those distinctions are essential.

I also derive an explicit algebraic generating function for **both actual adjacent endpoints**, with a common degree-eight algebraic parameter. It gives:

- a fixed seed;
- the correct varying-$m$ family, with $A=2m-1$ held fixed in each adjacent pair;
- an explicit rational differential connection of rank at most eight;
- a fixed quartic controlling the nontrivial critical positions of its algebraic parameter;
- a bounded symbolic calculation that can determine the actual differential rank and an exact coefficient recurrence.

The differential rank bound is not a digit-observable rank bound. Nor does it yet bound common endpoint content. The central remaining issue is the integral behavior of the coefficient recurrence at its critical integer positions.

No original tuple is evaluated here. No accepted finite computation, split classification, real-window construction, or square-class test is repeated.

---

## 1. Scope and notation

The original domain remains


$$
j>0,\qquad j\equiv81\pmod{243},\qquad
m=2^{2j-1},\qquad A=2m-1,
$$


with


$$
H_{\mathrm{win}}=3^{h-1},\qquad D=H_{\mathrm{win}}-A,
$$


and


$$
\frac1{2C_{16}}<\frac{D}{H_{\mathrm{win}}}<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$



For the scalar comparison I retain, without extending their scope,


$$
m\equiv851\pmod{6561},\qquad
r=\operatorname{cont}_3(J_m)=\operatorname{cont}_3(J_{m-1}),
$$




$$
s=h-2-2r,\qquad
\mathfrak a\equiv25\pmod{27},\qquad
N_m\in\mathbb Z_3^\times.
$$



To avoid confusing endpoint values with Jacobi recurrence coefficients, write


$$
a_m^{\mathrm{end}}=J_m(-1),\qquad
b_m^{\mathrm{end}}=J_{m-1}(-1).
$$



The adjacent polynomial in this definition has parameter $A=2m-1$, **not** $2(m-1)-1$.

The common endpoint content is


$$
c_m=\min\{v_3(a_m^{\mathrm{end}}),v_3(b_m^{\mathrm{end}})\}.
$$



The algebraic constructions below are identities for every positive integer $m$. Applying them to such auxiliary integers does not assert the original window or normalized inverse hypotheses.

---

## 2. Closed results reused at their stated scope

Turn10 supplies the exact formulas


$$
a_m^{\mathrm{end}}=[z^m]C_1(z)B(z)^m,\qquad
b_m^{\mathrm{end}}=[z^m]C_2(z)B(z)^m,
\tag{2.1}
$$


where


$$
B(z)=\frac{(1+z^2)^3(1-z)^2}{2(1+z)^6},
$$




$$
C_1(z)=\frac{(1+z)^2}{1+z^2},\qquad
C_2(z)=\frac{2z(1+z)^4}{(1+z^2)^2(1-z)^2}.
\tag{2.2}
$$



These identities follow from formal residue substitution and preserve both actual endpoint signs. They are not fixed-parameter recurrences applied across $m$.

The complete scalar splitting and its approach thresholds are also closed. With


$$
t=\frac{J_e}{D_e},
$$


the two scalar root lines satisfy


$$
v_3(\alpha)=3,\qquad v_3(\beta)=4,
$$


with first unit digit $-1$. On the retained scalar branch:

- outside the two exceptional projective classes,
  

$$
K_c/K_J\in1+3^9\mathbb Z_3;
$$


- in the depth-three class, a sufficient strict-preservation condition is
  

$$
v_3(t-\alpha)<2(r+g)+2;
  \tag{2.3}
$$


- in the depth-four class, it is
  

$$
v_3(t-\beta)<2(r+g)+4.
  \tag{2.4}
$$



No new discriminant computation is needed.

---

## 3. Joint algebraic generating functions

Introduce the formal algebraic series $Z=Z(x)$ specified by


$$
Z=xB(Z),\qquad Z(0)=0.
\tag{3.1}
$$


Since $B(0)=1/2$, this equation has a unique solution in $x\mathbb Q[[x]]$.

For the generating functions only, extend the endpoint sequences by


$$
a_0^{\mathrm{end}}=1,\qquad b_0^{\mathrm{end}}=0.
$$


The latter is a formal seed, not an assertion about a degree-$(-1)$ Jacobi polynomial.

Set


$$
\mathcal A(x)=\sum_{m\ge0}a_m^{\mathrm{end}}x^m,\qquad
\mathcal B(x)=\sum_{m\ge0}b_m^{\mathrm{end}}x^m.
$$



### Theorem 3.1 — Exact common algebraic parameter

Define


$$
R(z)=1+8z-10z^2+8z^3+z^4.
\tag{3.2}
$$


Then


$$
\boxed{
\mathcal A(x)=\frac{(1+Z)^3(1-Z)}{R(Z)},
}
\tag{3.3}
$$


and


$$
\boxed{
\mathcal B(x)=
\frac{2Z(1+Z)^5}{(1+Z^2)(1-Z)R(Z)}.
}
\tag{3.4}
$$



The parameter satisfies the degree-eight polynomial equation


$$
\boxed{
F(x,Z)=2Z(1+Z)^6
-x(1+Z^2)^3(1-Z)^2=0.
}
\tag{3.5}
$$



#### Proof

For any formal power series $C$, the Lagrange residue identity gives


$$
\sum_{m\ge0}x^m[z^m]C(z)B(z)^m
=
\frac{C(Z)}{1-xB'(Z)}.
\tag{3.6}
$$


Indeed, the left side is the formal residue


$$
\operatorname{Res}_{z=0}
\frac{C(z)}{z-xB(z)}\,dz,
$$


and the distinguished root $z=Z(x)$ contributes the right side.

At that root,


$$
xB'(Z)=Z\frac{B'(Z)}{B(Z)}.
$$


Logarithmic differentiation gives


$$
\frac{B'}B=
\frac{6z}{1+z^2}-\frac2{1-z}-\frac6{1+z}.
$$


Hence


$$
1-z\frac{B'}B
=
\frac{R(z)}{(1+z^2)(1-z)(1+z)}.
\tag{3.7}
$$


Substituting $C_1,C_2$ from (2.2) proves (3.3)–(3.4). Clearing the denominator in (3.1) proves (3.5). ∎

### Fixed seed and initial checks

The branch is fixed by


$$
Z(0)=0,\qquad Z'(0)=\frac12.
$$


Consequently,


$$
\mathcal A(0)=1,\qquad \mathcal B(0)=0.
$$



Directly from the original coefficient formulas,


$$
(a_1^{\mathrm{end}},b_1^{\mathrm{end}})=(-3,1),
$$




$$
(a_2^{\mathrm{end}},b_2^{\mathrm{end}})
=\left(\frac{53}{2},-5\right).
\tag{3.8}
$$



These are exact small-index identities used to identify the formal solution. They are not original-power calibrations and carry none of the real-window hypotheses.

### Why varying $A$ has been handled correctly

The generating functions were formed from (2.1), whose $m$-th adjacent value already has the fixed-in-that-pair parameter $A=2m-1$. Thus coefficient extraction in $x$ moves between the intended varying-parameter pairs.

No standard fixed-$A$ Jacobi recurrence has been used across $m$.

---

## 4. A rational differential connection and its critical positions

The algebraic parameter admits a particularly explicit connection:


$$
\boxed{
Z'(x)=
\frac{B(Z)(1+Z^2)(1-Z)(1+Z)}{R(Z)}.
}
\tag{4.1}
$$



This follows by differentiating $Z=xB(Z)$ and using (3.7).

Equivalently, for


$$
x(z)=\frac{2z(1+z)^6}{(1+z^2)^3(1-z)^2},
$$


one has


$$
\boxed{
\frac{dx}{dz}
=
\frac{2(1+z)^5R(z)}
{(1+z^2)^4(1-z)^3}.
}
\tag{4.2}
$$



Thus $R$ identifies the nontrivial finite critical positions away from the explicitly displayed zeros and poles of the parametrization.

The positions $z=-1,\pm i,1$ cannot simply be discarded: they govern ramification or poles over $x=0,\infty$, although the distinguished branch $Z(0)=0$ is regular.

### Theorem 4.1 — Rank-at-most-eight differential realization

The joint generating functions belong to a degree-eight extension of $\mathbb Q(x)$, and their derivatives admit an explicit rational connection in the basis


$$
1,Z,\ldots,Z^7.
$$



#### Proof

The numerator and denominator of $x(z)$ are coprime, with respective degrees seven and eight. Therefore the rational map $z\mapsto x(z)$ has degree eight, and


$$
[\mathbb Q(z):\mathbb Q(x(z))]=8.
$$


Consequently (3.5) is the minimal polynomial of $Z$ over $\mathbb Q(x)$.

In


$$
\mathscr E=\mathbb Q(x)[z]/(F),
$$


the derivative $F_z$ is invertible: the extension is separable in characteristic zero. Put


$$
P(z)=(1+z^2)^3(1-z)^2,\qquad
G(x,z)=P(z)F_z(x,z)^{-1}\pmod F.
$$


Implicit differentiation gives $Z'=G(x,Z)$.

For $0\le k\le7$, reduce


$$
kz^{k-1}G(x,z)
$$


modulo $F$. Its coefficients form the $k$-th row of a rational matrix $M(x)$, giving


$$
\frac d{dx}
\begin{pmatrix}
1\\ Z\\ \vdots\\ Z^7
\end{pmatrix}
=
M(x)
\begin{pmatrix}
1\\ Z\\ \vdots\\ Z^7
\end{pmatrix}.
\tag{4.3}
$$


The rational functions in (3.3)–(3.4) likewise have unique reduced representatives in this basis. ∎

This is an explicit algebraic construction of a connection, not a computed minimal differential system.

In particular:

- eight is the degree of the parameter field;
- the minimal differential rank generated by the two output functions may be smaller;
- neither number is the exact ternary digit-observable rank.

The last distinction leads to a definite obstruction.

---

## 5. Exact finite-rank digit closure fails

For a rational sequence $u=(u_n)_{n\ge0}$, define


$$
S_d u=(u_{3n+d})_{n\ge0},\qquad d=0,1,2.
$$


Its exact ternary observable space is the span of all iterated sections


$$
u_{3^k n+r},\qquad k\ge0,\quad 0\le r<3^k.
$$



### Lemma 5.1 — Finite exact section rank forces polynomial real growth

If a rational sequence has finite-dimensional ternary section span over $\mathbb Q_3$, then


$$
|u_n|\le C(n+1)^D
$$


for some real constants $C,D$.

#### Proof

Finite rank over $\mathbb Q_3$ of a matrix with rational entries is the same as finite rank over $\mathbb Q$: both ranks are determined by its finite minors.

Choose a basis of the section span consisting of rational section sequences. A finite collection of evaluation coordinates separates these basis sequences. Solving the resulting nonsingular rational linear system shows that the coefficients of every digit transition in this basis are rational.

Thus there are fixed rational matrices $M_0,M_1,M_2$, a fixed initial vector, and a fixed terminal functional expressing $u_n$ by a product of $O(\log n)$ such matrices.

Using an ordinary real matrix norm, that product is bounded by $C_0^{O(\log n)}$, which is polynomial in $n$. ∎

### Theorem 5.2 — Infinite exact observable rank for the actual endpoint pair

The exact ternary section span of $a_m^{\mathrm{end}}$, and hence of the joint endpoint pair, is infinite-dimensional over $\mathbb Q_3$.

#### Proof

The actual Bernstein expansion gives


$$
a_m^{\mathrm{end}}
=
(-1)^m
\sum_{k=0}^m
\binom{3m-1}{k}
\binom{m-\frac12}{m-k}2^{m-k}.
$$


Every summand inside the sum is positive. In particular,


$$
|a_m^{\mathrm{end}}|
\ge \binom{3m-1}{m}.
$$


Moreover,


$$
\binom{3m-1}{m}
=
\prod_{i=1}^m\frac{2m-1+i}{i}
\ge2^m.
$$


Thus the real growth is exponential, contradicting Lemma 5.1 if the exact section span were finite-dimensional. ∎

### Corollary 5.3 — No fixed finite-rank exact observable lattice

There is no fixed finitely generated $\mathbb Z_3$-module with:

1. linear digit transitions realizing all three exact sections;
2. the actual endpoint sequences among its outputs;
3. a fixed linear terminal evaluation;

even if each digit operator is allowed a fixed nonzero scalar denominator.

Indeed, tensoring such a module with $\mathbb Q_3$ would give the finite-dimensional space excluded by Theorem 5.2.

The conclusion also holds after prescribing any fixed finite ternary prefix: the sequence


$$
a_{3^k n+r}^{\mathrm{end}}
$$


still has exponential real growth.

### Exact scope of this obstruction

This proves that the actual minimal rank for **unrestricted exact linear digit observability** is infinite, not two or eight.

It does **not** prove impossibility for:

- fixed precision modulo $3^K$;
- a nonlinear projective normalization with path-dependent content;
- an infinite family of valuation-indexed lattices;
- a digit language restricted to actual original powers and their admissible continuations.

A normalized construction can evade the theorem only by using structure outside a fixed exact linear finite-rank realization. That is a precise restriction on the proposed method, not a general impossibility theorem for normalization.

---

## 6. What a normalization theorem must now add

The small rational denominator cannot, by itself, yield the requested exact fixed-rank digit lattice. The preceding obstruction explains why the prime-power layers in turn10 cannot simply be replaced by a fixed characteristic-zero linear observable space.

The algebraic connection offers a different route: a coefficient recurrence in $m$. But its arithmetic requires a separate theorem.

Suppose a joint recurrence is converted to a finite companion state


$$
V_{n+1}=T(n)V_n,\qquad T(n)\in\operatorname{GL}_r(\mathbb Q_3)
\tag{6.1}
$$


away from explicitly listed exceptional positions.

For


$$
c(V)=\min_i v_3(V_i),
$$


one has


$$
c(T(n)V)\ge c(V)+\min_{i,j}v_3(T(n)_{ij}).
\tag{6.2}
$$


If $T(n)^{-1}$ exists, then also


$$
c(T(n)V)
\le c(V)-\min_{i,j}v_3(T(n)^{-1}_{ij}).
\tag{6.3}
$$



These elementary bounds are rigorous, but a useful result needs much more:

1. a saturated integral lattice appropriate to the actual recurrence;
2. its Smith exponents at every critical integer position;
3. control of cancellation in the initial solution;
4. control of projection from the recurrence state to the two endpoints.

The last point is important. Even if $V_n$ is primitive, both endpoint coordinates can vanish deeply. Primitive state content is not automatically endpoint content.

### Concrete follow-on lemma

A suitable next target is:

> **Integral coefficient-connection lemma.**  
> For the joint algebraic functions (3.3)–(3.5), construct an exact coefficient recurrence and a finite companion state containing the actual solution. Give all exceptional nonnegative integer steps and their continuation identities. Construct saturated lattices for which the local Smith exponents admit an explicit cumulative bound, and prove an observability inequality bounding
> 

$$
> c_m-\min_i v_3((V_m)_i)
>
$$


> independently of uncomputed endpoint residues.

A bound $O(\log m)$ for the combined transition and observability loss would materially improve turn10. A recurrence without these two bounds would not.

No such bound is proved here.

---

## 7. Why the algebraic connection does not yet decide the projective class

The generating-function identities preserve the actual pair, but do not evaluate


$$
3^{-c_m}(a_m^{\mathrm{end}},b_m^{\mathrm{end}})\pmod{243}.
$$



In particular, they do not establish avoidance of


$$
T\equiv54\pmod{81},
\qquad
T\equiv162\pmod{243},
$$


where $T$ is the primitive first coordinate divided by the primitive second coordinate when the latter is a unit.

Nor do they bound the actual rational endpoint ratio’s approach to $\alpha$ or $\beta$ in (2.3)–(2.4).

The critical-position polynomial $R$ concerns singularities of the algebraic generating parameter. It is **not** a substitute for the scalar root lines. No line-avoidance statement follows merely from $R$, algebraicity, or finite differential rank.

---

## 8. New bounded symbolic calculation

No computation has been executed. The following is new and does not repeat the accepted endpoint rationalization, prime-power transition, or scalar classification.

### Inputs

The fixed polynomials and rational functions


$$
F(x,z)=2z(1+z)^6-x(1+z^2)^3(1-z)^2,
$$




$$
R(z)=1+8z-10z^2+8z^3+z^4,
$$




$$
h_1(z)=\frac{(1+z)^3(1-z)}{R(z)},
\qquad
h_2(z)=\frac{2z(1+z)^5}{(1+z^2)(1-z)R(z)}.
$$



No original integer $m$, large modulus, endpoint expansion, or original-power digit word is an input.

### Exact arithmetic

1. In $\mathbb Q(x)[z]/(F)$, compute $F_z^{-1}$, hence the connection (4.3).
2. Reduce $h_1,h_2$ to vectors of length eight.
3. Starting with these vectors, close their span under
   

$$
w\longmapsto w'+wM.
$$


   At most eight independent vectors can occur.
4. Supply rational rank certificates and differential identities for the resulting stable span.
5. Clear denominators without discarding factors.
6. Extract the exact coefficient recurrence, including every low-index boundary term.
7. List the nonnegative integer zeros of its leading coefficient and derive the continuation identities needed at those exceptional steps.

### Expected verifiable output

- the actual minimal joint differential rank;
- a rational connection or annihilating system;
- a complete polynomial-coefficient recurrence in $m$;
- its fixed seed and every exceptional step;
- factorized denominator and leading-coefficient polynomials;
- polynomial identity certificates verifying the recurrence.

This is a fixed-degree bounded symbolic problem. Its output would establish an exact recurrence, not automatically a normalization bound.

The next arithmetic analysis would concern the $3$-adic Smith behavior of that **specific** recurrence and its endpoint observation map. It should not be replaced by a generic recurrence-existence citation.

---

## 9. Full-producer and primitive-arithmetic boundaries

Nothing above changes the original finite spaces:


$$
0\le v\le2n-2,
$$




$$
U_u=x^u\quad(0\le u<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m),
\qquad d=\frac{3D}{2}-1,\qquad \nu=\frac D2-1.
$$



Both corrected columns and the nonlinear elimination term remain


$$
\widehat Z^{\,\mathrm{act}}
=\widehat Z^{\,c}-3^6WE_{\mathrm{act}}^{-1}T_R,
$$




$$
S_{\mathrm{act}}-S_c
=3^6K_Z-3^{12}T_R^TE_{\mathrm{act}}^{-1}T_R,
$$


with


$$
Q_{\mathrm{act}}=Q_c+3^6R_{\mathrm{prod}},
\qquad
R_{\mathrm{prod}}=R_{25}+3^{25}\Delta_{25}.
$$


Here $R_{\mathrm{prod}}$ is distinct from the quartic $R(z)$.

All $\Delta_H$ layers, unpaired cutoff terms, exterior contributions, both corrected factors, and the nonlinear correction remain required.

The complete force retains both leading extractions, every permitted lower pole, factorial forcing, and LOW subtraction. The terminal return remains


$$
\mu_{i+\nu}^{\langle26\rangle}
+\sum_{k=0}^{\nu-1}f_k\mu_{i+k}^{\langle26\rangle}
=b_i^{\langle26\rangle},
\qquad0\le i\le\nu-2,
$$




$$
J^T\varepsilon+\omega
=-\varepsilon-s_{\mathrm{ret}}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
$$


No moment beyond $D-4$ is introduced, and $\omega_{\nu-1}$ is retained.

All row contents, the actual multiplier, and the least actual clearer precede


$$
A_\ell=\ell_{\mathrm{clr}}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\mathrm{clr}}^{m+1}\beta_1,
$$




$$
g_\ell=\gcd(|A_\ell|,|B_\ell|)
$$


over all primes.

For $B_\ell\ne0$, the actual primitive denominator and numerator are


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
$$


and the whole same-index error is still


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\mathrm{clr}}^{m+1}}{g_\ell}
\det H_{\mathrm{complete}}.
}
$$



Neither new theorem evaluates this expression, proves its nonvanishing, or establishes its decay after the all-prime gcd.

---

## 10. Proof-status ledger and conclusion

| Statement | Status |
|---|---|
| Split scalar classification and exact approach thresholds | Reused, closed |
| Actual endpoint rational coefficient formulas | Reused with correct adjacent parameter |
| Joint algebraic generating functions (3.3)–(3.5) | **Proved here** |
| Fixed formal seed and initial endpoint checks | **Derived here** |
| Degree-eight parameter field | **Proved here** |
| Explicit rank-at-most-eight differential connection | **Proved here** |
| Quartic critical-position identity | **Proved here** |
| Minimal joint differential rank | Not computed |
| Complete coefficient recurrence and exceptional steps | Bounded symbolic calculation specified, not executed |
| Infinite unrestricted exact ternary observable rank | **Proved here** |
| Fixed finite-rank exact linear digit lattice | Excluded at the stated scope |
| Nonlinear or original-power-restricted normalization scheme | Not excluded; not constructed |
| Small bound for actual common endpoint content | Not proved |
| Actual primitive endpoint class on an original tuple | Not evaluated |
| Original endpoint line avoidance or approach bound | Open |
| Full actual producer and all-prime whole-error analysis | Open |

### Final result

The new positive result is the exact joint algebraic representation


$$
\boxed{
\mathcal A(x)=\frac{(1+Z)^3(1-Z)}{R(Z)},\qquad
\mathcal B(x)=
\frac{2Z(1+Z)^5}{(1+Z^2)(1-Z)R(Z)},
}
$$


with


$$
2Z(1+Z)^6=x(1+Z^2)^3(1-Z)^2.
$$



The new obstruction is equally definite:



$$
\boxed{
\text{The unrestricted exact ternary observable rank is infinite.}
}
$$



Thus the small common rational denominator does not support the proposed fixed finite-rank exact linear digit normalization. A successful digit method must use nonlinear normalization, a genuinely valuation-indexed structure, or proved restrictions on the original-power language.

The concrete alternative is now a fixed-degree algebraic coefficient connection. Its unresolved arithmetic bottleneck is **a cumulative $3$-adic normalization bound, including endpoint observability loss, through every exceptional integer step of the actual joint recurrence**.

Even after that local bottleneck is overcome, the complete producer, final all-prime gcd, actual primitive denominator, and whole same-index error remain indispensable.



$$
\boxed{\text{An unconditional proof or disproof of irrationality of }e+\pi
\text{ remains unresolved by this work.}}
$$


