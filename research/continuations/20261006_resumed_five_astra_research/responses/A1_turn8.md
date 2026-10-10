> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1turn8 — The fixed-coefficient gap is valid; a weighted-jet theorem gives at least eight factorial digits

## Executive conclusion

The coordinator’s proposed fixed-path argument is valid on


$$
m\equiv851\pmod{6561}.
$$


It proves, for the **actual Jacobi normalization** in the sources,


$$
\boxed{g:=v_3(J_m(0))-\operatorname{cont}_3(J_m)\ge5.}
$$



In particular, the first possible residue displayed in A1turn7 is now decided:


$$
\boxed{
2u_0\left(\frac{u_1}{3}+u_2\right)\equiv0\pmod3.
}
$$


This is a proof, not merely acceptance of the certificate’s label.

There is also a stronger advance. On the established controlled-growth normalized branch, write


$$
r=\operatorname{cont}_3(J_m)=\operatorname{cont}_3(J_{m-1}),
\qquad s=h-2-2r,
\qquad U=3^sP_J.
$$


Then the exact quotient-free Bezout identity yields a factorial-weighted jet bound which controls **every coefficient**, without expanding the endpoint kernel:


$$
\boxed{
v_3\!\left(\mathfrak f(Q_cU^2)\right)\ge2g-2\ge8.
}
$$


All higher factorial corrections obey a strictly deeper bound. Consequently,


$$
\boxed{
v_3(K_c-K_J)\ge h-2s+2g-2\ge h-2s+8.
}
$$



Moreover, the first digit at this improved threshold has an explicit evaluation. Define


$$
J=3^{-r}J_m,\qquad Z=3^{-r}Z_{\rm source},\qquad
L=\frac{2}{\mathfrak a N_m},
\qquad
\zeta=\frac{Z(0)}{3^{g-1}}\in\mathbb Z_3^\times .
$$


Then


$$
\boxed{
\frac{K_c-K_J}{3^{h-2s+2g-2}}
\equiv L^2\zeta^2J(-1)^2
\pmod3.
}
\tag{1}
$$


Thus, if $J(-1)$ is a unit, the improved lower bound is exact. If $J(-1)\equiv0\pmod3$, that digit also vanishes.

This does **not** yet prove scalar preservation against the complete $K_J$ subtraction. The remaining local obstruction is now sharply concentrated in correlated endpoint values and the complete pure scalar—not an original-size Schur solve.

---

## 1. Scope and retained hypotheses

The original domain and finite window remain


$$
j>0,\qquad j\equiv81\pmod{243},\qquad
m=2^{2j-1},\qquad A=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A,\qquad
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$



The new fixed-coefficient argument applies on the synchronized cylinder


$$
m\equiv851\pmod{6561}.
\tag{2}
$$


I do not infer that cylinder merely from an unrelated finite check or extend its conclusions to indices outside it.

The inverse-kernel conclusions below use the established normalized branch, with


$$
r=\operatorname{cont}_3(J_m)=\operatorname{cont}_3(J_{m-1}),
\quad
s=h-2-2r,
\quad
h-s=2+2r\ge2,
\tag{3}
$$


and


$$
\mathfrak a=a_m/3\equiv25\pmod{27},\qquad
N_m\in\mathbb Z_3^\times,
$$




$$
v_3(b_m)=v_3(a_m)=1,\qquad v_3(\rho)=4.
\tag{4}
$$


These hypotheses are not silently promoted to the entire original window.

The accepted suffix exclusion and exact-window intersection are left closed. No accepted computation is proposed for repetition.

---

## 2. Independent proof of the fixed-coefficient gap

Write the actual Bernstein-type expansion as


$$
J_m(y)=\sum_{k=0}^m B_k\,y^k(y-1)^{m-k},
$$


where


$$
B_k=\binom{3m-1}{k}\binom{m-\tfrac12}{m-k}.
\tag{5}
$$



### 2.1 Signs and the actual constant coefficient

Only $k=0$ contributes to the monomial constant:


$$
J_m(0)=(-1)^mB_0.
\tag{6}
$$


On the original family $m$ is even, so the sign is actually positive. In either case it has valuation zero.

If one instead uses $y^k(1-y)^{m-k}$, the Bernstein coefficients acquire factors $(-1)^{m-k}$. Those signs likewise do not change valuations.

The basis change from $y^k(y-1)^{m-k}$ to monomials is triangular, with diagonal entries $(-1)^{m-k}$. Therefore it is unimodular over $\mathbb Z$, and


$$
r=\min_{0\le k\le m}v_3(B_k).
\tag{7}
$$



### 2.2 What the eight low digits say

Put $m=851+6561M$, $M\ge0$. Reading ternary digits from low to high, the relevant eight-digit streams are


$$
m_{\rm low}=(2,1,1,1,1,0,1,0),
$$




$$
(3m-1)_{\rm low}=(2,1,1,1,1,1,0,1),
$$




$$
(m-\tfrac12)_{\rm low}=(0,0,0,0,0,2,2,1).
\tag{8}
$$



For $k=0$, the lower stream in the half-integral binomial is $m$. The half-integral subtraction incurs outgoing borrows at precisely the first five positions and then clears. The integral subtraction has no borrow. The low cost is therefore $5$.

For $k=122$,


$$
122=(2,1,1,1,1,0,0,0)_3
$$


in low-to-high notation, and


$$
m-122=729+6561M,
$$


whose low stream is


$$
(0,0,0,0,0,0,1,0).
$$


Both subtractions are borrow-free through all eight positions. The low cost is $0$.

In both cases the addition constraint $k+(m-k)=m$ also ends with zero carry. Thus both paths reach the same state $000$.

### 2.3 Why the future costs agree for every $M$

This is the essential universal step.

Above the first eight positions:

* both $k$-streams are zero;
* both $(m-k)$-streams equal the actual ternary stream of $M$;
* the upper stream of $3m-1$ is the same in both comparisons;
* the upper $3$-adic stream of $m-\tfrac12$ is the same in both comparisons;
* the incoming addition carry and both incoming borrows are zero.

In particular, the half-integral upper stream is determined by


$$
m-\frac12
=4131+6561\left(M-\frac12\right);
$$


it is not necessary, or correct, to replace it by an arbitrary integer stream.

Every future transition and every future cost is consequently identical. The eventual clearing of the half-integral borrow is also identical. Hence


$$
\boxed{v_3(B_{122})=v_3(B_0)-5.}
\tag{9}
$$



Combining (6), (7), and (9),


$$
\boxed{g:=v_3(J_m(0))-r\ge5.}
\tag{10}
$$



This proves the certificate’s proposed universal conclusion. It does not claim that $B_{122}$ is a content-minimizing coefficient, nor that $g=5$.

---

## 3. Immediate resolution of the A1turn7 residue

Set


$$
J(y)=3^{-r}J_m(y)=\sum_i c_i y^i.
$$


The exact coefficient recurrence is


$$
\frac{c_{i+1}}{c_i}
=
\frac{(i-m)(6m-1+2i)}{(i+1)(2i+1)}.
\tag{11}
$$


Thus


$$
v_3(c_0)=g,\qquad v_3(c_1)=g,\qquad v_3(c_2)=g-1.
\tag{12}
$$


For the last equality, on (2), all numerator factors in $c_2/c_0$ are units and its denominator has valuation one.

Therefore


$$
c_0,c_1\in3^5\mathbb Z_3,\qquad c_2\in3^4\mathbb Z_3.
$$



The retained inverse reduction gives


$$
U(y)\equiv
-\frac{2}{\mathfrak a N_m}(y+1)J(y)J(-1)\pmod3.
$$


Its constant coefficient is zero modulo $3$, irrespective of $J(-1)$. Hence $u_0\equiv0\pmod3$, and the previously proved $u_1\in3\mathbb Z_3$ gives


$$
\boxed{
2u_0\left(\frac{u_1}{3}+u_2\right)=0\quad\text{in }\mathbb F_3.
}
\tag{13}
$$



The first possible residue in A1turn7 is therefore **computed and zero**.

---

## 4. Exact adjacent-coefficient control

A stronger result follows without stopping at reduction modulo $3$.

Define


$$
D(y)=3^{-r}J_{m-1}(y).
$$


Here the parameter $A=2m-1$ is held fixed, as in the source.

The exact constant ratio, including its sign, is


$$
\frac{D(0)}{J(0)}
=-\frac{2m}{2m-1}
=-\frac{2m}{A}.
\tag{14}
$$


On the original domain $v_3(A)=5$, so


$$
v_3(D(0))=g-5,
\qquad
v_3(\rho D(0))=g-1.
\tag{15}
$$



Let


$$
w_i=v_3((2i)!).
$$


The hypergeometric coefficient formulas give


$$
v_3(c_i)+w_i\ge g.
\tag{16}
$$


Indeed,


$$
\frac{c_i}{c_0}
=
\frac{2^i(-m)_i\prod_{t=0}^{i-1}(6m-1+2t)}{(2i)!},
$$


and its numerator is $3$-integral.

For the adjacent polynomial,


$$
\frac{[y^i]D}{D(0)}
=
\frac{2^i(-(m-1))_i
\prod_{t=0}^{i-1}(6m-3+2t)}{(2i)!}.
\tag{17}
$$


For every $i\ge1$, the numerator contains


$$
6m-3=3A,\qquad v_3(3A)=6.
$$


Consequently,


$$
\boxed{
v_3([y^i](\rho D))+w_i\ge g+5
\quad(i\ge1).
}
\tag{18}
$$



Equations (15) and (18) exhibit a useful distinction: the normalized adjacent contribution has an unusually shallow constant, but its positive-degree coefficients are much deeper in factorial-weighted precision.

---

## 5. The normalized Christoffel polynomial

Use the actual source polynomial, normalized only by $3^r$:


$$
Z(y)=3^{-r}Z_{\rm source}(y).
$$


Its exact identity is


$$
(3y-\eta)Z(y)
=(y-b_m-a_m)J(y)-\rho D(y),
\qquad \eta=A+71.
\tag{19}
$$


Since $\eta$ is a unit, this is a unit-denominator recurrence at $y=0$. No Christoffel scalar has been discarded.

Write $Z=\sum z_i y^i$, and put $b=b_m+a_m$, so $v_3(b)\ge1$. The constant equation gives


$$
z_0=\frac{b c_0+\rho D(0)}{\eta}.
$$


The two summands have valuations at least $g+1$ and exactly $g-1$. Thus


$$
\boxed{v_3(z_0)=g-1.}
\tag{20}
$$



For $i\ge1$, (19) gives


$$
\eta z_i
=3z_{i-1}-c_{i-1}+bc_i+\rho[y^i]D.
\tag{21}
$$


Using (16), (18), and monotonicity of $w_i$, induction yields


$$
\boxed{
v_3(z_i)+w_i\ge g\quad(i\ge1).
}
\tag{22}
$$



The first two positive-degree bounds can be sharpened directly:


$$
v_3(z_1)\ge g,\qquad v_3(z_2)\ge g.
\tag{23}
$$


For $z_2$, use $v_3(c_1)=g$, $v_3(bc_2)\ge g$, and (18).

Thus the actual normalized Christoffel low jet has


$$
v_3(z_0)=g-1,\qquad v_3(z_1),v_3(z_2)\ge g.
$$


This conclusion retains both terms in its defining numerator and the actual $a_m,b_m,\rho,\eta$.

---

## 6. Quotient-free endpoint identity and weighted low jets

The exact normalized inverse identity is


$$
U(y)
=L\left[
Z(y)Z(-1)
+\mathfrak a\,
\frac{J(y)Z(-1)-Z(y)J(-1)}{y+1}
\right],
\quad L=\frac2{\mathfrak a N_m}.
\tag{24}
$$


Equivalently, without division,


$$
\boxed{
(y+1)U(y)
=L\left[
Z(y)\bigl(B+yZ(-1)\bigr)
+\mathfrak a J(y)Z(-1)
\right],
}
\tag{25}
$$


where


$$
B=Z(-1)-\mathfrak a J(-1).
\tag{26}
$$



All endpoint factors here are the actual ones.

From (20)–(23) and the integral power series for $(1+y)^{-1}$, one obtains


$$
\boxed{
v_3(u_0),v_3(u_1),v_3(u_2)\ge g-1\ge4.
}
\tag{27}
$$


More importantly, the same recurrence proves the all-degree weighted statement


$$
\boxed{
v_3(u_i)+w_i\ge g-1\quad(i\ge0),
\qquad
v_3(u_i)+w_i\ge g\quad(i\ge2).
}
\tag{28}
$$



For clarity, the only term on the right of (25) capable of weighted valuation $g-1$ is the constant $z_0B$, together with its propagation through division by $1+y$ and the degree-one term $yz_0Z(-1)$. At degrees at least two, their factorial weight is already positive. Every other term has weighted valuation at least $g$.

At the first two degrees, modulo one digit after division by $3^{g-1}$,


$$
\frac{u_0}{3^{g-1}}\equiv L\zeta B,
\qquad
\frac{u_1}{3^{g-1}}
\equiv L\zeta\bigl(Z(-1)-B\bigr)
=L\zeta\mathfrak a J(-1),
\tag{29}
$$


where $\zeta=z_0/3^{g-1}$ is a unit.

Finally, the retained noncollision reduction gives


$$
Z(y)\equiv yJ(y)\pmod3.
$$


Since $\mathfrak a\equiv1\pmod3$,


$$
B\equiv-2J(-1)\equiv J(-1)\pmod3.
$$


Thus


$$
\boxed{
\frac{u_0}{3^{g-1}}
\equiv
\frac{u_1}{3^{g-1}}
\equiv L\zeta J(-1)\pmod3.
}
\tag{30}
$$



In particular, if $J(-1)$ is a unit, both $u_0$ and $u_1$ have valuation exactly $g-1$. This sign-sensitive conclusion uses the $yZ(-1)$ term in (25); dropping that term would give the wrong first-jet relation.

---

## 7. The whole factorial contraction: eight digits and an evaluated leading residue

For nonnegative integers $i,j,k$,


$$
w_{i+j+k}\ge w_i+w_j,
\tag{31}
$$


because the corresponding factorial quotient is an integer.

Expand $Q_c=\sum q_k y^k$. Each term in the complete finite contraction is


$$
q_k u_i u_j(2(i+j+k))!.
$$


By (28) and (31), its valuation is at least $2g-2$. Therefore


$$
\boxed{\mathfrak f(Q_cU^2)\in3^{2g-2}\mathbb Z_3.}
\tag{32}
$$



This is not a low-degree truncation assumed in advance. It bounds the entire factorial functional.

To compute its first digit, (28) shows that a term containing $u_i$ with $i\ge2$ is one digit deeper. If $i,j\in\{0,1\}$, any term of total degree at least two is also one digit deeper, since $w_2=1$. Only total degrees zero and one survive.

Modulo $3$,


$$
q_0\equiv q_1\equiv2.
$$


Writing


$$
a=\frac{u_0}{3^{g-1}}\pmod3,\qquad
b=\frac{u_1}{3^{g-1}}\pmod3,
$$


we obtain


$$
\frac{\mathfrak f(Q_cU^2)}{3^{2g-2}}
\equiv(q_0+2q_1)a^2+4q_0ab
\equiv2ab.
$$


By (30), $a=b=L\zeta J(-1)$. Hence


$$
\boxed{
\frac{\mathfrak f(Q_cU^2)}{3^{2g-2}}
\equiv2L^2\zeta^2J(-1)^2\pmod3.
}
\tag{33}
$$



This is an evaluated symbolic residue, not an unevaluated kernel specification. Its remaining original-family input is the endpoint class $J(-1)\bmod3$.

---

## 8. Every higher factorial correction remains controlled

Retain


$$
G_c=G_J+3^h\mathcal F,\qquad
\mathcal F_{ab}=-\frac14\mathfrak f(Q_cy^{a+b}),
$$


and


$$
C=3^sG_J^{-1}\in M_{m+1}(\mathbb Z_3),
\qquad \epsilon=3^{h-s}\in9\mathbb Z_3.
$$



The exact resolvent identity from A1turn7 is


$$
K_c-K_J
=\frac{3^{h-2s}}4\mathfrak f(Q_cU^2)
+3^{2h-3s}
u^T\mathcal F(I+\epsilon C\mathcal F)^{-1}C\mathcal Fu.
\tag{34}
$$



The weighted bound also controls the factorial force vector. Indeed,


$$
v_3((\mathcal Fu)_a)\ge g-1+w_a,
\tag{35}
$$


using


$$
w_{a+i+k}\ge w_a+w_i.
$$


In particular $\mathcal Fu\in3^{g-1}\mathbb Z_3^{m+1}$. The second term of (34) therefore has valuation at least


$$
2h-3s+2g-2
=(h-2s+2g-2)+(h-s).
\tag{36}
$$


It is at least two digits deeper than the improved first-variation threshold.

Consequently,


$$
\boxed{
v_3(K_c-K_J)\ge h-2s+2g-2\ge h-2s+8.
}
\tag{37}
$$


Since $1/4\equiv1\pmod3$, the correct leading residue is


$$
\boxed{
\frac{K_c-K_J}{3^{h-2s+2g-2}}
\equiv2L^2\zeta^2J(-1)^2\pmod3.
}
\tag{38}
$$



**Correction to the executive formula:** the coefficient in (1) is $2$, as established by the complete contraction calculation (33). Thus (38), not the coefficient-free version of (1), is the exact residue formula. The valuation and nonvanishing conclusions stated there are unchanged.

In particular,


$$
J(-1)\in\mathbb Z_3^\times
\quad\Longrightarrow\quad
\boxed{v_3(K_c-K_J)=h-2s+2g-2.}
\tag{39}
$$



---

## 9. What this does not yet prove

The complete pure scalar remains


$$
K_J=
\frac{
\mathscr K_m(-1,-1)
-\mathscr K_m(r_0,-1)J_{m+1}(-1)/J_{m+1}(r_0)
}{3c(-1-r_0)}.
\tag{40}
$$


Its subtraction has not been replaced by either summand.

Scalar preservation would follow from


$$
v_3(K_J)<h-2s+2g-2.
\tag{41}
$$


No such upper bound has been proved here. In particular, lower bounds on both sides do not establish a strict comparison.

Even the endpoint-unit case (39) supplies an exact factorial-response valuation, not an upper bound for the correlated pure scalar.

### Concrete follow-on lemma

The next local target can now be stated without requesting a large matrix:

> **Correlated endpoint comparison lemma.**  
> On the same normalized original-family branch, determine $J(-1)\bmod3$, and bound the valuation of the complete endpoint subtraction (40) sharply enough to decide (41). If $J(-1)\equiv0\pmod3$, lift the correlated endpoint pair $J(-1),Z(-1)$ in the exact identity (25), rather than treating their valuations independently.

This is the remaining local bottleneck. The present report proves a stronger bounded symbolic-jet theorem, but does not claim to have completed that comparison.

---

## 10. Original finite system and arithmetic normalization are unchanged

Nothing above changes the original pole cutoff


$$
0\le v\le2n-2
$$


or the finite columns


$$
U_u=x^u\quad(0\le u<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),\qquad
Y_b=y^b\quad(d\le b\le m),
$$


where


$$
d=\frac{3D}{2}-1,\qquad \nu=\frac D2-1.
$$



Both corrected representatives remain, with


$$
\widehat Z^{\,\mathrm{act}}
=\widehat Z^{\,c}-3^6WE_{\mathrm{act}}^{-1}T_R,
$$




$$
S_{\mathrm{act}}-S_c
=3^6K_Z-3^{12}T_R^TE_{\mathrm{act}}^{-1}T_R.
$$


The full producer correction


$$
Q_{\mathrm{act}}=Q_c+3^6R,\qquad
R=R_{25}+3^{25}\Delta_{25}
$$


still requires its complete directional analysis, including all $\Delta_H$ layers, both corrected factors, unpaired cutoff terms, and nonlinear elimination.

The complete forcing retains both leading extractions, every permitted lower pole, factorial forcing, and LOW subtraction. The terminal system retains


$$
\mu_{i+\nu}^{\langle26\rangle}
+\sum_{k=0}^{\nu-1}f_k\mu_{i+k}^{\langle26\rangle}
=b_i^{\langle26\rangle},
\qquad0\le i\le\nu-2,
$$




$$
J^T\varepsilon+\omega
=-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
$$


There is no added moment beyond $D-4$, and $\omega_{\nu-1}$ remains.

Finally, all row contents, the actual multiplier, and the least actual clearer must precede


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,\qquad
g_\ell=\gcd(|A_\ell|,|B_\ell|)
$$


over **all primes**. The primitive pair remains


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
$$


and the same-index whole error remains


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{g_\ell}
\det H_{\rm complete}.
}
$$


No nonvanishing or decay claim for this evaluated whole error follows from the local factorial theorem alone.

---

## 11. Bounded arithmetic and proof status

No remote computation was executed. No accepted bounded computation needs rerunning.

The new arithmetic needed for the symbolic theorem is already displayed:

1. The eight low digit streams (8), with costs $5$ and $0$ and common terminal state.
2. The exact constant ratio $-2m/A$.
3. The valuations
   

$$
v_3(A)=5,\quad v_3(3A)=6,\quad v_3(\rho)=4.
$$


4. The factorial-weight inequalities (31).
5. The two-coefficient contraction
   

$$
(q_0+2q_1)a^2+4q_0ab
   \equiv2ab\pmod3,
$$


   followed by $a=b=L\zeta J(-1)$.

An optional constant-size arithmetic verification would take


$$
q_0=q_1=2,\quad a=b
\quad\text{in }\mathbb F_3
$$


and return $2a^2$. It would verify only the displayed leading-residue arithmetic, not evaluate the unresolved original-family endpoint.

| Claim | Status |
|---|---|
| Fixed $k=122$ coefficient lies exactly five valuation digits below the constant | Proved on $m\equiv851\pmod{6561}$ |
| $g\ge5$ for the actual normalization | Proved |
| A1turn7 three-jet residue is zero | Proved |
| Exact normalized Christoffel constant valuation $g-1$ | Proved under retained scalar hypotheses |
| Actual endpoint coefficients $u_0,u_1,u_2\in3^{g-1}\mathbb Z_3$ | Proved |
| All-degree factorial-weighted endpoint bounds | Proved |
| Complete factorial response has at least $2g-2\ge8$ extra digits | Proved, including higher corrections |
| Leading residue at that threshold | Formula (38), proved |
| Exact response valuation when $J(-1)$ is a unit | Proved conditionally |
| Original-family endpoint-unit decision and complete pure-scalar comparison | Unresolved |
| Full actual-producer alignment, primitive denominator, and whole-error decay | Unresolved |

## Conclusion

The fixed-path proposal closes the previously unevaluated residue. The stronger new result is


$$
\boxed{
v_3(K_c-K_J)\ge h-2s+2g-2\ge h-2s+8,
}
$$


with the exact threshold residue


$$
\boxed{
\frac{K_c-K_J}{3^{h-2s+2g-2}}
\equiv2L^2\zeta^2J(-1)^2\pmod3.
}
$$



The outstanding mathematical bottleneck is a sharp valuation comparison with the **complete** pure Christoffel subtraction, followed by the full actual-producer response and the original primitive-error obligations.



$$
\boxed{\text{The irrationality of }e+\pi\text{ remains unresolved by this work.}}
$$


