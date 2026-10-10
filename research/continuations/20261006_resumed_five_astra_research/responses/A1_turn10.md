> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1 turn10 — A rational diagonal for the actual adjacent endpoints, with certified common-content removal

## Executive conclusion

The coordinator’s split-form deduction is correct under A4turn7’s retained normalization hypotheses. The coefficient-only anisotropy alternative is closed: the complete scalar form has two distinct $3$-adic root lines, of depths $3$ and $4$, with first unit digit $-1$. I reuse that conclusion and do **not** propose another scalar-coefficient test.

The new result is an explicit, common-denominator rational representation of the **actual adjacent Jacobi endpoint pair**, followed by a proved ternary coefficient-extraction recurrence. It gives:

1. the two actual endpoints as diagonal coefficients of rational functions with one common denominator of bidegree at most $(1,14)$;
2. an explicit integral prime-power transition module;
3. a certified procedure that returns the endpoint pair modulo $3^5$ **after removing its actual common endpoint content**;
4. a precision budget expressed in terms of that common content, together with a crude unconditional termination bound.

This is more than an unevaluated appeal to rational-diagonal methods: the rational functions, initialization, transitions, degree bounds, terminal functional, and normalization test are supplied and proved below. It does not expand either degree-$m$ endpoint polynomial.

However, it does **not** yet certify a nonexceptional original tuple or an infinite original subbranch. In particular, the termination bound is not a uniform small valuation budget. No normalized periodicity, short description of the ternary digits of the original power, or infinite-family line avoidance is inferred.

Thus the advance is a rigorous normalized endpoint evaluator and a sharper formulation of the remaining approach bound—not a completed irrationality argument.

---

## 1. Scope and the now-closed scalar alternative

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



The scalar-preservation conclusions continue to require the established normalized branch:


$$
m\equiv851\pmod{6561},
$$




$$
r=\operatorname{cont}_3(J_m)
=\operatorname{cont}_3(J_{m-1}),\qquad
s=h-2-2r,
$$




$$
\mathfrak a=a_m/3\equiv25\pmod{27},\qquad
N_m\in\mathbb Z_3^\times.
$$


The parameter $A$ is held fixed in the adjacent polynomial $J_{m-1}$.

Write


$$
J=3^{-r}J_m,\qquad D_-=3^{-r}J_{m-1},
$$


and let


$$
J_e=J(-1),\qquad D_e=D_-(-1).
$$



A4’s complete scalar formula is


$$
K_J=3^{-s}\frac{L}{(A+74)^2}
\left(FJ_e^2+GJ_eD_e+H_qD_e^2\right),
\qquad L=\frac2{\mathfrak a N_m},
\tag{1.1}
$$


where I write $H_q$ for the quadratic coefficient to distinguish it from the window parameter. The audited coefficient data are


$$
v_3(F,G,H_q)=(1,4,8),
\qquad
F/3\equiv G/3^4\equiv H_q/3^8\equiv1\pmod3.
\tag{1.2}
$$



These coefficients belong to the **whole** Christoffel scalar, including its endpoint derivative subtraction.

### 1.1 Verification of the split consequence

Put


$$
\Delta=G^2-4FH_q.
$$


The two terms have valuations $8$ and $9$, respectively. Hence


$$
v_3(\Delta)=8,\qquad \Delta/3^8\equiv1\pmod3.
$$


Hensel’s lemma applied to $X^2-\Delta/3^8$ at $X=1$ proves that $\Delta$ is a square in $\mathbb Q_3$.

The Newton polygon of


$$
Ft^2+Gt+H_q
$$


has vertices


$$
(0,8),\quad(1,4),\quad(2,1),
$$


and slopes $-4,-3$. Its two roots, denoted by $\alpha,\beta$, satisfy


$$
v_3(\alpha)=3,\qquad v_3(\beta)=4.
$$


Substituting $t=27u$, and dividing by $3^7$, gives at the first digit


$$
u^2+u=0.
$$


For a unit root this forces $u=-1$. Substituting $t=81u$, and dividing by $3^8$, gives


$$
u+1=0.
$$


Therefore


$$
\boxed{
\alpha/27\equiv-1\pmod3,\qquad
\beta/81\equiv-1\pmod3.
}
\tag{1.3}
$$



These are precisely A4’s exceptional projective classes. They are roots of the scalar form; they are **not** a statement that the original endpoints attain those roots.

A universal anisotropic upper valuation bound for arbitrary primitive pairs is consequently unavailable.

---

## 2. The actual generating coefficients

For this section use the unnormalized endpoints


$$
a_m:=J_m(-1),\qquad b_m^{\mathrm{end}}:=J_{m-1}(-1).
$$


The symbol $b_m^{\mathrm{end}}$ is an endpoint, not the Jacobi recurrence coefficient $b_m$.

The actual Bernstein expansion gives


$$
\boxed{
a_m=[t^m](1-t)^{3m-1}(1-2t)^{m-\frac12}.
}
\tag{2.1}
$$


Indeed, expansion of the right side gives


$$
(-1)^m
\sum_{k=0}^m
\binom{3m-1}{k}
\binom{m-\frac12}{m-k}2^{m-k},
$$


which is exactly the Bernstein evaluation at $-1$.

With $A=2m-1$ held fixed, the adjacent expansion similarly gives


$$
\boxed{
b_m^{\mathrm{end}}
=[t^{m-1}](1-t)^{3m-2}(1-2t)^{m-\frac32}.
}
\tag{2.2}
$$



The signs in these formulas are part of the actual normalization. On the original family $m$ is even, so $a_m>0$ and $b_m^{\mathrm{end}}<0$.

---

## 3. Rationalizing both endpoints simultaneously

The half-integral powers in (2.1)–(2.2) can be removed without changing the selected coefficient.

Make the formal substitution


$$
t=\frac{2z}{(1+z)^2}.
\tag{3.1}
$$


It has invertible linear coefficient over $\mathbb Z_{(3)}$, and


$$
1-t=\frac{1+z^2}{(1+z)^2},\qquad
1-2t=\frac{(1-z)^2}{(1+z)^2},
$$




$$
\frac{dt}{t}=\frac{1-z}{1+z}\frac{dz}{z}.
\tag{3.2}
$$


The square root is the formal branch with constant term $1$.

Define


$$
P(z)=(1+z^2)^3(1-z)^2,
\qquad
B(z)=\frac{P(z)}{2(1+z)^6},
\tag{3.3}
$$


and


$$
C_1(z)=\frac{(1+z)^2}{1+z^2},
\qquad
C_2(z)=
\frac{2z(1+z)^4}{(1+z^2)^2(1-z)^2}.
\tag{3.4}
$$



### Theorem 3.1 — Exact rational coefficient formulas

For every positive integer $m$, with the adjacent parameter held fixed as above,


$$
\boxed{
a_m=[z^m]\,C_1(z)B(z)^m,
\qquad
b_m^{\mathrm{end}}=[z^m]\,C_2(z)B(z)^m.
}
\tag{3.5}
$$



#### Proof

For the first endpoint, express coefficient extraction as a formal residue:


$$
a_m=\operatorname{Res}_{t=0}
t^{-m}(1-t)^{3m-1}(1-2t)^{m-\frac12}\frac{dt}{t}.
$$


After (3.1), the factors depending exponentially on $m$ combine to


$$
\left(\frac{P(z)}{2z(1+z)^6}\right)^m
=z^{-m}B(z)^m.
$$


The remaining factors combine to


$$
(1-t)^{-1}(1-2t)^{-1/2}
\frac{1-z}{1+z}
=\frac{(1+z)^2}{1+z^2}=C_1(z).
$$


This proves the first identity.

Relative to this first residue integrand, the adjacent endpoint integrand has the additional factor


$$
\frac{t}{(1-t)(1-2t)}
=
\frac{2z(1+z)^2}{(1+z^2)(1-z)^2}.
$$


Multiplying it by $C_1$ gives $C_2$, proving the second identity. ∎

This calculation preserves the actual adjacent solution. It does not substitute an independently chosen polynomial family.

---

## 4. A common rational diagonal of bidegree $(1,14)$

Introduce an auxiliary variable $u$. Set


$$
\boxed{
Q(u,z)=
(1+z^2)^2(1-z)^2
\left((1+z)^6-\frac u2 P(z)\right).
}
\tag{4.1}
$$


Its constant coefficient is $1$, and its coefficients belong to $\mathbb Z_{(3)}$.

Define


$$
\boxed{
N_1(z)=(1+z)^8(1+z^2)(1-z)^2,
\qquad
N_2(z)=2z(1+z)^{10}.
}
\tag{4.2}
$$



Then


$$
\frac{N_i}{Q}=\frac{C_i(z)}{1-uB(z)},
$$


so Theorem 3.1 yields


$$
\boxed{
a_m=[u^m z^m]\frac{N_1}{Q},
\qquad
b_m^{\mathrm{end}}=[u^m z^m]\frac{N_2}{Q}.
}
\tag{4.3}
$$



The coordinatewise degrees satisfy


$$
\deg Q\le(1,14),\qquad
\deg N_1\le(1,14),\qquad
\deg N_2\le(1,14).
\tag{4.4}
$$



The use of rational-diagonal coefficient methods is established background. The target-specific result here is the explicit common pair (4.1)–(4.3), including the adjacent normalization and the small two-variable degree bound.

---

## 5. An explicit ternary prime-power recurrence

This section supplies a proved evaluator for (4.3), not an assumed normalized period.

For $d\in\{0,1,2\}$, define


$$
\Lambda_d\!\left(\sum_{a,b\ge0}c_{a,b}u^az^b\right)
=
\sum_{a,b\ge0}c_{3a+d,\,3b+d}u^az^b.
\tag{5.1}
$$


Only equal digit pairs are needed, because the target is $(m,m)$.

Put


$$
E_Q(u,z)=\frac{Q(u,z)^3-Q(u^3,z^3)}3.
\tag{5.2}
$$


Reduction modulo $3$ proves


$$
E_Q\in\mathbb Z_{(3)}[u,z].
$$



At precision $3^K$, represent a rational state in layered form


$$
\boxed{
\mathcal S=
\sum_{\tau=0}^{K-1}
3^\tau\frac{P_\tau}{Q^{\tau+1}},
}
\tag{5.3}
$$


where $P_\tau$ is needed modulo $3^{K-\tau}$.

### Theorem 5.1 — Integral transition and degree closure

For $e=\tau+1$,


$$
\boxed{
\Lambda_d\left(3^\tau\frac{P_\tau}{Q^e}\right)
\equiv
\sum_{k=0}^{K-1-\tau}
3^{\tau+k}(-1)^k
\binom{e+k-1}{k}
\frac{\Lambda_d(P_\tau Q^{2e}E_Q^k)}
     {Q^{e+k}}
\pmod{3^K}.
}
\tag{5.4}
$$



The module specified by


$$
\deg_u P_\tau\le\tau+1,\qquad
\deg_z P_\tau\le14(\tau+1)
\tag{5.5}
$$


is invariant under all three transitions.

#### Proof

Write


$$
\frac1{Q^e}=\frac{Q^{2e}}{Q^{3e}}.
$$


Since


$$
Q^3=Q(u^3,z^3)+3E_Q,
$$


the negative-binomial expansion gives


$$
\frac1{Q^{3e}}
=
\sum_{k\ge0}
(-1)^k\binom{e+k-1}{k}
\frac{3^kE_Q^k}{Q(u^3,z^3)^{e+k}}.
$$


Terms with $\tau+k\ge K$ vanish at the requested precision. Cartier extraction satisfies


$$
\Lambda_d\bigl(R(u,z)S(u^3,z^3)\bigr)
=\Lambda_d(R)S(u,z),
$$


which proves (5.4).

Let $\mathbf q=(1,14)$. If $\deg P_\tau\le e\mathbf q$, then


$$
\deg(P_\tau Q^{2e}E_Q^k)
\le3(e+k)\mathbf q.
$$


After extraction, the degree is at most $(e+k)\mathbf q$, exactly the required bound at layer $\tau+k$. ∎

There is no division by $3$ in the transition applied to state data. The polynomial $E_Q$ is a fixed, exactly defined integral input; all other scalar divisions involve units at $3$.

A sufficient ambient coefficient count for one state is


$$
\boxed{
B_K=\sum_{e=1}^K(e+1)(14e+1).
}
\tag{5.6}
$$


In particular, this is a two-variable module of size $O(K^3)$, independent of $m$. This is an ambient bound, not a claim that its reachable part has been minimized.

---

## 6. Exact initialization and terminal evaluation

Write the actual integer $m$ in base $3$:


$$
m=d_0+3d_1+\cdots+3^{L-1}d_{L-1}.
$$



For the first endpoint initialize


$$
P_0=N_1,\qquad P_\tau=0\quad(\tau>0);
$$


for the second initialize


$$
P_0=N_2,\qquad P_\tau=0\quad(\tau>0).
$$



Apply (5.4) successively for


$$
d_0,d_1,\ldots,d_{L-1}.
$$


Because $Q(0,0)=1$, the terminal functional is


$$
\boxed{
\operatorname{Term}(\mathcal S)
=\sum_{\tau=0}^{K-1}3^\tau P_\tau(0,0)
\pmod{3^K}.
}
\tag{6.1}
$$



The two terminal values are exactly


$$
a_m\bmod3^K,\qquad b_m^{\mathrm{end}}\bmod3^K.
\tag{6.2}
$$



This takes $L$ digit transitions at fixed precision; it does not sum $m$ Bernstein terms or expand a degree-$m$ endpoint polynomial.

There is an important limitation: the digit word is the word of the **actual**


$$
m=2^{2j-1}.
$$


No periodicity of the normalized answer, and no shortcut from a few digits of $j$, has been proved. Exact production of this word remains part of the input cost.

---

## 7. Certified common-content removal

A raw congruence pair is not a projective endpoint certificate. The following theorem makes the normalization test explicit.

Let


$$
c_m=\min\{v_3(a_m),v_3(b_m^{\mathrm{end}})\}.
\tag{7.1}
$$


Both endpoints are $3$-integral: generalized binomial coefficients with $3$-adic integral upper parameter are $3$-integral.

### Theorem 7.1 — Normalized five-digit endpoint certificate

Evaluate (4.3) modulo $3^K$. Suppose the resulting residues have a common valuation


$$
\widehat c<K,
$$


meaning that at least one residue is nonzero modulo $3^{\widehat c+1}$, both are divisible by $3^{\widehat c}$, and


$$
\widehat c\le K-5.
\tag{7.2}
$$


Then


$$
\widehat c=c_m,
$$


and division of the two residues by $3^{\widehat c}$ returns the actual primitive pair


$$
\boxed{
\left(
3^{-c_m}J_m(-1),\
3^{-c_m}J_{m-1}(-1)
\right)\pmod{3^5}.
}
\tag{7.3}
$$



#### Proof

Changing a residue modulo $3^K$ changes either endpoint only by an element of $3^K\mathbb Z_3$. A nonzero digit at depth $\widehat c<K$ therefore proves that the minimum actual valuation is exactly $\widehat c$. After division, the remaining uncertainty has valuation at least $K-\widehat c\ge5$. ∎

The polynomial-content normalization $3^{-r}$ does not need to be computed for this projective task:


$$
\min\{v_3(J_e),v_3(D_e)\}=c_m-r,
$$


and removing that common factor gives exactly the pair in (7.3).

### An adaptive procedure

Start with $K=5$, and increase precision until (7.2) holds. For example, use


$$
K=5,10,20,40,\ldots.
$$


A stage returning two zero residues does not normalize anything; it only proves $c_m\ge K$. A stage revealing the first common-content digit but fewer than five subsequent digits is also insufficient.

The first successful doubling stage has


$$
K<2(c_m+5)
$$


unless success occurs at the initial stage. Thus the required precision is controlled by the **actual common endpoint content**, not by an assumed polynomial content or a raw endpoint modulus.

---

## 8. Unconditional termination, and its precise limitation

The adaptive procedure terminates for every positive $m$. One can prove this without evaluating an endpoint.

First,


$$
2^m a_m\in\mathbb Z.
\tag{8.1}
$$


Indeed,


$$
4^\ell\binom{m-\frac12}{\ell}\in\mathbb Z,
$$


and the $\ell=m-k$ summand in (2.1) contains the additional factor $2^\ell$.

All absolute Bernstein summands for $a_m$ are positive, and


$$
\binom{m-\frac12}{\ell}\le\binom m\ell
\qquad(0\le\ell\le m).
$$


Consequently,


$$
|a_m|
\le
\left(\sum_{k=0}^{3m-1}\binom{3m-1}{k}\right)
\left(\sum_{\ell=0}^m\binom m\ell2^\ell\right)
=
2^{3m-1}3^m.
$$


Thus


$$
0<|2^ma_m|<48^m<3^{4m}.
$$


Because multiplication by $2^m$ does not change the $3$-adic valuation,


$$
\boxed{c_m\le v_3(a_m)<4m.}
\tag{8.2}
$$



Therefore precision $K=4m+5$ certainly suffices.

This bound is deliberately identified as **crude**. It proves termination, not practical feasibility for an original index. It does not meet the stronger objective of a small, closed valuation budget on an infinite original subbranch.

The distinction is:

- the number of coefficient-extraction stages at a fixed precision is logarithmic in $m$;
- the precision needed for normalization is $c_m+5$;
- no bound $c_m=O(\log m)$, much less a uniform bound on the retained branch, has been proved here.

The construction avoids an $O(m)$ endpoint expansion. It does not establish an overall polylogarithmic-cost normalized evaluator.

---

## 9. Classification from the certified primitive pair

Let the output of Theorem 7.1 be


$$
(X,Y)\pmod{243},
\qquad \min\{v_3(X),v_3(Y)\}=0.
$$



If $X$ is a unit, the pair is nonexceptional. Otherwise $Y$ is a unit, and compute


$$
T=XY^{-1}\pmod{243}.
$$



The two exceptional classes are exactly


$$
\boxed{T\equiv54\pmod{81}}
\tag{9.1}
$$


and


$$
\boxed{T\equiv162\pmod{243}.}
\tag{9.2}
$$


The first is $v_3(T)=3$ with $T/27\equiv-1\pmod3$; the second is $v_3(T)=4$ with $T/81\equiv-1\pmod3$.

Every other certified primitive output is nonexceptional. In that case A4’s theorem applies, under the retained scalar hypotheses:


$$
\boxed{\frac{K_c}{K_J}\in1+3^9\mathbb Z_3.}
\tag{9.3}
$$



No original endpoint pair has been evaluated in this report. Equations (9.1)–(9.2) are a proved classification rule, not a reported classification outcome.

---

## 10. A sharper approach-bound target in the exceptional classes

The split form also gives a useful exact version of the outstanding approach condition.

Put


$$
t=\frac{J_e}{D_e},\qquad y=v_3(D_e),
$$


and factor


$$
Ft^2+Gt+H_q=F(t-\alpha)(t-\beta),
$$


with roots as in (1.3). Since their depths differ,


$$
v_3(\alpha-\beta)=3.
$$



Let


$$
e_*=\min\{v_3(J_e),\,4+v_3(D_e)\},
\qquad
\mathcal B=2(r+g).
$$


The retained whole factorial-response bound is


$$
v_3(K_c-K_J)\ge -s+\mathcal B+2e_*.
\tag{10.1}
$$



### Depth-three exceptional class

If


$$
v_3(t)=3,\qquad t/27\equiv-1\pmod3,
$$


then


$$
v_3(t-\beta)=3,\qquad e_*=y+3.
$$


Writing $q_\alpha=v_3(t-\alpha)$, the complete quadratic has valuation


$$
v_3(FJ_e^2+GJ_eD_e+H_qD_e^2)
=4+2y+q_\alpha.
$$


Hence


$$
\boxed{
v_3(K_J)=-s+2e_*+q_\alpha-2.
}
\tag{10.2}
$$


A sufficient strict-preservation condition is therefore


$$
\boxed{q_\alpha<2(r+g)+2.}
\tag{10.3}
$$



### Depth-four exceptional class

If


$$
v_3(t)=4,\qquad t/81\equiv-1\pmod3,
$$


then


$$
v_3(t-\alpha)=3,\qquad e_*=y+4.
$$


Writing $q_\beta=v_3(t-\beta)$,


$$
\boxed{
v_3(K_J)=-s+2e_*+q_\beta-4,
}
\tag{10.4}
$$


and a sufficient condition is


$$
\boxed{q_\beta<2(r+g)+4.}
\tag{10.5}
$$



These formulas expose the exact remaining loss: it is the depth of approach of the **actual rational endpoint ratio** to one of two $3$-adic algebraic lines.

The inequalities are conditional deductions, not proved bounds on the original ratio.

---

## 11. What the new recurrence does—and does not—settle

The new recurrence addresses an actual obstacle in the previous reports: it extracts the two endpoints together, at their original index, and provides a correct test for removing their common endpoint factor.

It does not yet prove either of the following stronger statements.

### Outstanding lemma A: controlled normalization

On a specified infinite subset of the retained original branch, prove a sufficiently small bound for


$$
c_m=\min\{v_3(J_m(-1)),v_3(J_{m-1}(-1))\},
$$


or prove a statewise extraction of common powers of $3$ with an exact cumulative valuation budget.

The present prime-power transition is integral, but it is not an integral $2\times2$ transfer for a primitive endpoint vector. Dividing a current state by a common factor is not automatically justified by divisibility of its two eventual terminal outputs.

### Outstanding lemma B: original endpoint avoidance

Using the actual digit word of $m=2^{2j-1}$, prove that the normalized terminal pair avoids (9.1)–(9.2) on an infinite original subbranch; alternatively prove (10.3) or (10.5) there.

A finite-state description at each fixed $K$ does not prove a period for normalized outputs when $K$ must grow with $c_m$. Nor does it prove that the ternary digit words of the original powers enter a favorable terminal class.

These are precise mathematical obstructions, not merely implementation details.

---

## 12. Full-producer and primitive-arithmetic boundaries remain unchanged

The endpoint theorem concerns the pure/core scalar comparison only. It does not replace the actual producer analysis.

The original pole cutoff remains


$$
0\le v\le2n-2.
$$


The finite columns remain


$$
U_u=x^u\quad(0\le u<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m),
\qquad
d=\frac{3D}{2}-1,\qquad \nu=\frac D2-1.
$$



Both corrected columns and the nonlinear correction remain


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
Q_{\mathrm{act}}=Q_c+3^6R,\qquad
R=R_{25}+3^{25}\Delta_{25}.
$$


All $\Delta_H$ layers, unpaired cutoff contributions, exterior terms, both corrected factors, and nonlinear elimination remain required.

The complete force still includes both leading extractions, every permitted lower pole, factorial forcing, and LOW subtraction. The terminal return is still


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

All row contents, the actual multiplier, and the least actual clearer must precede


$$
A_\ell=\ell_{\mathrm{clr}}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\mathrm{clr}}^{m+1}\beta_1,
$$




$$
g_\ell=\gcd(|A_\ell|,|B_\ell|)
$$


over **all primes**.

For $B_\ell\ne0$, the actual primitive pair and same-index whole error remain


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
$$




$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\mathrm{clr}}^{m+1}}{g_\ell}
\det H_{\mathrm{complete}}.
}
\tag{12.1}
$$


No claim about nonvanishing or decay of this whole error follows from the new diagonal representation.

---

## 13. New bounded exact-arithmetic certificate

No computation was executed. No accepted bounded computation is proposed for repetition.

The new calculation is the target-specific endpoint evaluation just proved.

### Inputs

1. A certified original tuple satisfying the retained branch and window hypotheses.
2. Its exact integer $m=2^{2j-1}$, or its certified complete ternary digit word.
3. The fixed rational polynomials $Q,N_1,N_2$ in (4.1)–(4.2).
4. A stated precision $K$.

### Exact calculation

Apply the three explicitly defined digit maps (5.4), with the two initial states from §6, along the actual digits of $m$. Evaluate the terminal functional (6.1).

### Expected verifiable output

- the two endpoint residues modulo $3^K$;
- either a certificate that precision is insufficient for normalization, or the exact common endpoint valuation $c_m$;
- if $K-c_m\ge5$, the primitive pair modulo $243$;
- classification as nonexceptional, depth-three exceptional, or depth-four exceptional;
- only in the nonexceptional case, the conclusion $K_c/K_J\in1+3^9\mathbb Z_3$.

For an exceptional output, further lifting concerns (10.3) or (10.5), with the actual scalar coefficients at certified precision. It is not another square-class test: splitting is already decided.

For any fixed input and fixed $K$, this is a bounded exact calculation. A successful result for one tuple establishes only that tuple’s classification.

---

## 14. Proof-status ledger and conclusion

| Statement | Status |
|---|---|
| Correct factor $2$ in the whole factorial-response residue | Reused, independently audited |
| Complete scalar coefficient depths $1,4,8$, units all $1$ | Reused at retained scope |
| Split discriminant and root depths $3,4$, units $-1$ | Verified |
| Coefficient-only anisotropy alternative | Closed negatively |
| Actual adjacent generating-coefficient formulas | Derived from Bernstein normalization |
| Common two-variable rational diagonal | **Proved here** |
| Explicit ternary prime-power recurrence and degree closure | **Proved here** |
| Certified common-content removal and primitive five-digit output | **Proved here** |
| Unconditional termination of adaptive precision | **Proved here**, with crude $c_m<4m$ bound |
| Uniform small normalization budget | Not proved |
| Original normalized endpoint periodicity | Not claimed |
| An evaluated original endpoint pair | Not supplied |
| Infinite original nonexceptional subbranch | Not proved |
| Exact exceptional approach-loss formulas | **Proved here** |
| Full actual-producer preservation | Open |
| All-prime primitive denominator and whole-error decay | Open |

### Final result

The new exact reduction is


$$
\boxed{
\bigl(J_m(-1),J_{m-1}(-1)\bigr)
=
[u^mz^m]\left(\frac{N_1}{Q},\frac{N_2}{Q}\right),
}
$$


with one explicit denominator of bidegree at most $(1,14)$, together with a proved integral digit recurrence and a correct common-content normalization certificate.

The immediate bottleneck is now explicit: **control the normalization precision and the terminal projective class along the actual ternary digit words of the original powers**, or bound their approach to the two scalar root lines by (10.3)–(10.5). The rational-diagonal construction does not itself prove that avoidance.

Beyond that local problem remain the complete actual producer, the all-prime final gcd, the actual primitive denominator, and the whole same-index error.



$$
\boxed{\text{An unconditional proof or disproof of irrationality of }e+\pi
\text{ remains unresolved by this work.}}
$$


