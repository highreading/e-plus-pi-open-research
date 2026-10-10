> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4, Turn 7 — Audit of the factorial theorem, a sharper complete-scalar criterion, and a certified cross-scale interface

## Executive conclusions

I find the substantive derivation in A1turn8 correct **under its retained normalization hypotheses**. In particular:



$$
g=v_3(J_m(0))-\operatorname{cont}_3(J_m)\ge5,
$$





$$
v_3(z_0)=g-1,
$$



and the all-degree factorial-weighted estimates do control the **complete** factorial contraction and its higher resolvent corrections. The correct leading coefficient is the repaired one:



$$
\boxed{
\frac{K_c-K_J}{3^{h-2s+2g-2}}
\equiv
2L^2\zeta^2J(-1)^2\pmod3.
}
$$



The factor $2$ cannot be dropped.

I obtain two further results.

1. **A complete pure-scalar formula in the correlated adjacent endpoint pair.**  
   The entire Christoffel subtraction can be written as an explicit binary quadratic form in
   

$$
J(-1),\qquad D(-1),\qquad D=3^{-r}J_{m-1},
$$


   retaining the actual recurrence coefficients and Christoffel normalizer. Its three coefficient valuations are exactly
   

$$
\boxed{1,\quad4,\quad8.}
$$


   This is an evaluation of the complete pure scalar, not a bound on either summand of the kernel subtraction.

2. **An endpoint-content improvement of the whole factorial-response bound.**  
   Put
   

$$
e_*=\min\{v_3(J(-1)),\,4+v_3(D(-1))\}.
$$


   Then
   

$$
\boxed{
   v_3(K_c-K_J)\ge h-2s+2g-2+2e_*.
   }
$$


   Combining this with the quadratic formula proves scalar preservation outside two explicit projective endpoint residue classes. On that nonexceptional part of the stated normalized original family,
   

$$
\boxed{\frac{K_c}{K_J}\in1+3^9\mathbb Z_3.}
$$


   This is a rigorous conditional classification of original tuples. The supplied sources do **not** yet certify that an original tuple, or an infinite original subbranch, lies outside the two exceptional classes. I do not replace that missing endpoint result by a claim of generic nonvanishing.

For the binary target, I give an exact rational coefficient representation of the original finite observable, followed by a directly proved prime-power Cartier invariant bound. It transports the **three specified observables**, but does not assume that their fixed-degree saturated quotient remains rank three under digit changes. A5 can use either:

- the explicit invariant ambient module below; or
- a smaller, verifiable cross-scale closure certificate inside it.

The coordinator’s one $163\times160$ relation-matrix/payload postprocessing remains pending. I neither regenerate it nor report a Smith result.

No computation was executed for this report.

---

# Part I. Independent audit of A1turn7–8

## 1. Scope and normalization

Throughout this part I retain



$$
j>0,\qquad j\equiv81\pmod{243},\qquad
m=2^{2j-1},\qquad A=2m-1,
$$



and the original real window and finite pole cutoff. The conclusions requiring normalized inverse integrality apply only on the established controlled-growth normalized branch, with



$$
r=\operatorname{cont}_3(J_m)
 =\operatorname{cont}_3(J_{m-1}),
$$





$$
s=h-2-2r,\qquad h-s=2+2r\ge2,
$$





$$
\mathfrak a=a_m/3\equiv25\pmod{27},
\qquad N_m\in\mathbb Z_3^\times,
$$





$$
v_3(a_m)=v_3(b_m)=1,\qquad v_3(\rho)=4.
$$



The gap argument additionally uses the synchronized cylinder



$$
m\equiv851\pmod{6561}.
$$



I do not extend those normalization hypotheses to arbitrary original powers.

### Exact valuation of $A$

Here the asserted valuation is particularly straightforward. Since



$$
A=4^j-1,\qquad
j=81(1+3q),
$$



LTE gives



$$
\boxed{v_3(A)=v_3(4-1)+v_3(j)=1+4=5.}
$$



Moreover,



$$
\boxed{\frac{A}{3^5}\equiv1\pmod3.}
\tag{1.1}
$$



This last unit will also enter the new scalar calculation.

---

## 2. The actual Bernstein gap is proved

The actual source normalization is



$$
J_m(y)=\sum_{k=0}^m
B_k\,y^k(y-1)^{m-k},
\qquad
B_k=\binom{3m-1}{k}\binom{m-\tfrac12}{m-k}.
$$



The change from this basis to monomials is triangular with diagonal entries $(-1)^{m-k}$, hence unimodular. Therefore



$$
r=\min_k v_3(B_k).
$$



Also,



$$
J_m(0)=(-1)^mB_0.
$$



On the original family $m$ is even, so this endpoint sign is positive.

For



$$
m=851+6561M,
$$



the two paths $k=0$ and $k=122$ have respective low-eight-digit costs $5$ and $0$, and both finish in state $000$. Above those digits:

- both $k$-streams are zero;
- both remaining $m-k$ streams are $M$;
- the integral upper streams agree;
- the half-integral upper streams agree, with the actual continuation $M-\tfrac12$;
- all incoming carries and borrows agree.

Thus the entire future costs agree, not merely their first eight terms. Consequently,



$$
v_3(B_{122})=v_3(B_0)-5,
$$



and



$$
\boxed{g:=v_3(J_m(0))-r\ge5.}
$$



This does not prove that $B_{122}$ is content-minimizing, or that $g=5$.

---

## 3. Adjacent constants and the normalized Christoffel constant

Write



$$
J=3^{-r}J_m,\qquad D=3^{-r}J_{m-1},
$$



with the parameter $A=2m-1$ held fixed in both polynomials.

The constants in the actual Jacobi normalization satisfy



$$
\boxed{\frac{D(0)}{J(0)}=-\frac{2m}{A}.}
\tag{3.1}
$$



The negative sign is essential. It comes from the change in polynomial degree, not from a freely chosen normalization.

Since $v_3(A)=5$, $m$ is a unit, and $v_3(\rho)=4$,



$$
v_3(D(0))=g-5,
\qquad
v_3(\rho D(0))=g-1.
$$



Now retain the exact source identity



$$
(3y-\eta)Z(y)
=(y-b_m-a_m)J(y)-\rho D(y),
\qquad \eta=A+71.
\tag{3.2}
$$



Put $b_\Sigma=b_m+a_m$. The constant equation is



$$
z_0=\frac{b_\Sigma J(0)+\rho D(0)}{\eta}.
$$



Here $\eta$ is a unit. The first numerator term has valuation at least $g+1$, and the second has valuation exactly $g-1$. Hence there is no cancellation at the shallower valuation:



$$
\boxed{v_3(z_0)=g-1.}
$$



This conclusion retains the actual Christoffel scale.

---

## 4. The all-degree weighted estimates are valid

Let



$$
w_i=v_3((2i)!).
$$



The exact coefficient recurrence gives



$$
\frac{[y^i]J}{J(0)}
=
\frac{
2^i(-m)_i\prod_{t=0}^{i-1}(6m-1+2t)
}{(2i)!}.
$$



Its numerator is $3$-integral, so



$$
v_3([y^i]J)+w_i\ge g.
\tag{4.1}
$$



For $D$, the corresponding numerator contains, for every $i\ge1$,



$$
6m-3=3A,
\qquad v_3(3A)=6.
$$



Together with (3.1), this gives



$$
v_3([y^i](\rho D))+w_i\ge g+5
\qquad(i\ge1).
\tag{4.2}
$$



The recurrence obtained from (3.2) then proves



$$
v_3(z_i)+w_i\ge g\qquad(i\ge1),
$$



with the stronger low-degree bounds



$$
v_3(z_1),v_3(z_2)\ge g.
$$



There is no unproved truncation here: these are coefficientwise statements over all degrees.

---

## 5. Endpoint signs and the factor $2$

Set



$$
L=\frac{2}{\mathfrak a N_m}.
$$



The exact normalized endpoint identity is



$$
U(y)=L\left[
Z(y)Z(-1)
+\mathfrak a
\frac{J(y)Z(-1)-Z(y)J(-1)}{y+1}
\right].
\tag{5.1}
$$



Equivalently,



$$
(y+1)U(y)
=
L\left[
Z(y)\bigl(B+yZ(-1)\bigr)
+\mathfrak a J(y)Z(-1)
\right],
$$



where



$$
B=Z(-1)-\mathfrak a J(-1).
$$



The degree-one term $yZ(-1)$ must be retained. With



$$
\zeta=z_0/3^{g-1},
$$



the first two coefficients satisfy



$$
\frac{u_0}{3^{g-1}}\equiv L\zeta B,
$$





$$
\frac{u_1}{3^{g-1}}
\equiv L\zeta\mathfrak a J(-1)
\pmod3.
$$



The retained reduction $Z(y)\equiv yJ(y)\pmod3$, together with $\mathfrak a\equiv1\pmod3$, gives



$$
B\equiv J(-1)\pmod3.
$$



Thus both normalized coefficients have the same residue:



$$
\frac{u_0}{3^{g-1}}
\equiv
\frac{u_1}{3^{g-1}}
\equiv L\zeta J(-1)\pmod3.
\tag{5.2}
$$



The weighted estimates imply



$$
v_3(u_i)+w_i\ge g-1
$$



for all $i$, with the extra digit



$$
v_3(u_i)+w_i\ge g\qquad(i\ge2).
$$



In the first possible digit of the complete factorial contraction, only total degrees zero and one survive. Since the actual $Q_c$ has



$$
q_0\equiv q_1\equiv2\pmod3,
$$



writing $a=u_0/3^{g-1}$, $b=u_1/3^{g-1}$ gives



$$
(q_0+2q_1)a^2+4q_0ab
\equiv2ab\pmod3.
$$



Using (5.2),



$$
\boxed{
\frac{\mathfrak f(Q_cU^2)}{3^{2g-2}}
\equiv
2L^2\zeta^2J(-1)^2\pmod3.
}
$$



Thus A1turn8’s formula (38), not its executive formula (1), is correct.

---

## 6. The higher resolvent remainder is also controlled

The exact remainder is



$$
K_c-K_J
=
\frac{3^{h-2s}}4\mathfrak f(Q_cU^2)
+
3^{2h-3s}
u^T\mathcal F(I+\epsilon C\mathcal F)^{-1}C\mathcal Fu,
$$



where



$$
C=3^sG_J^{-1}\in M_{m+1}(\mathbb Z_3),
\qquad
\epsilon=3^{h-s}\in9\mathbb Z_3.
$$



The factorial-weight inequality



$$
w_{a+i+k}\ge w_a+w_i
$$



gives



$$
v_3((\mathcal Fu)_a)\ge g-1+w_a.
$$



Both outer force vectors therefore contribute $g-1$. The higher remainder has valuation at least



$$
2h-3s+2g-2,
$$



which is $h-s\ge2$ digits deeper than the first-variation threshold.

Accordingly,



$$
\boxed{
v_3(K_c-K_J)\ge h-2s+2g-2,
}
$$



and the repaired leading residue controls the **whole** response.

---

# Part II. A new complete pure-scalar calculation

## 7. Recovering the actual recurrence coefficients

The source’s Jacobi normalization satisfies



$$
yJ_m
=
\alpha_mJ_{m+1}+b_mJ_m+\rho J_{m-1}.
$$



At $A=2m-1$, the coefficients are



$$
\alpha_m=
\frac{2(m+1)(6m+1)}{(8m-1)(8m+1)},
$$





$$
\boxed{
b_m=
\frac12+
\frac{1-4A^2}{2(8m-3)(8m+1)},
}
\tag{7.1}
$$





$$
\boxed{
\rho=
\frac{2(3m-1)A}{(8m-3)(8m-1)}.
}
\tag{7.2}
$$



These are the coefficients for the actual $J_m$, not for an independently rescaled monic family. In particular,



$$
(y-b_m-a_m)J_m-\rho J_{m-1}
=
\alpha_mJ_{m+1}-a_mJ_m,
$$



which matches the retained Christoffel numerator.

Using $A\equiv0\pmod{27}$,



$$
8m-3=4A+1,\qquad 8m+1=4A+5,
$$



so



$$
b_m\equiv\frac12+\frac1{10}
=\frac35\equiv6\pmod{27}.
$$



Since $a_m=3\mathfrak a\equiv21\pmod{27}$,



$$
\boxed{b_\Sigma=b_m+a_m\equiv0\pmod{27}.}
\tag{7.3}
$$



This is stronger than the $v_3(b_\Sigma)\ge1$ used in A1turn8.

Also, (1.1) and (7.2) give



$$
\boxed{\rho/3^4\equiv1\pmod3.}
\tag{7.4}
$$



---

## 8. Exact endpoint derivative relations

Let



$$
J_e=J(-1),\qquad D_e=D(-1).
$$



The standard lowering and raising identities, specialized without changing normalization, yield



$$
J'(-1)=\lambda J_e+\mu D_e,
$$





$$
D'(-1)=\gamma J_e+\delta D_e,
\tag{8.1}
$$



where



$$
\lambda=-\frac{m(14m-5)}{2(8m-3)},
$$





$$
\mu=-\frac{(3m-1)A}{2(8m-3)},
$$





$$
\gamma=\frac{3mA}{2(8m-3)},
$$





$$
\delta=\frac{3A(5m-2)}{2(8m-3)}.
\tag{8.2}
$$



For completeness, the first identity follows from



$$
T\,y(1-y)J'
=
m\bigl((m+A)-Ty\bigr)J
+(m+A)(m-\tfrac12)D,
$$



with $T=2m+A-\tfrac12$, evaluated at $y=-1$. The raising identity for $D$ gives the second.

Their relevant valuations and residues are



$$
\boxed{
v_3(\lambda)=0,\quad
v_3(\mu)=5,\quad
v_3(\gamma)=v_3(\delta)=6,
\quad
\lambda\equiv1\pmod3.
}
\tag{8.3}
$$



No derivative of an enormous expanded polynomial is needed to establish these identities.

---

## 9. The whole scalar as an explicit quadratic form

Put



$$
E=\eta+3=A+74.
$$



At $y=-1$, the Christoffel identity gives



$$
Z(-1)=\frac{(1+b_\Sigma)J_e+\rho D_e}{E}.
\tag{9.1}
$$



Taking the removable value of (5.1) at $y=-1$ gives



$$
U(-1)
=
L\left[
Z(-1)^2+
\mathfrak a\bigl(J'(-1)Z(-1)-Z'(-1)J_e\bigr)
\right].
\tag{9.2}
$$



This is already the complete scalar: $K_J=3^{-s}U(-1)$.

Substitute (8.1) and differentiate (3.2). Direct simplification gives



$$
\boxed{
U(-1)=\frac{L}{E^2}
\left(FJ_e^2+GJ_eD_e+HD_e^2\right),
}
\tag{9.3}
$$



where



$$
\boxed{
F=(1+b_\Sigma)^2
+\mathfrak a(\eta-3b_\Sigma)
-\mathfrak a\rho E\gamma,
}
\tag{9.4}
$$





$$
\boxed{
G=\rho\left[
2(1+b_\Sigma)-3\mathfrak a
+\mathfrak a E(\lambda-\delta)
\right],
}
\tag{9.5}
$$





$$
\boxed{
H=\rho^2+\mathfrak a\rho E\mu.
}
\tag{9.6}
$$



Every term in the endpoint Wronskian and in $Z(-1)^2$ is present.

### Exact coefficient depths

Using (7.3), $\mathfrak a\equiv25\pmod{27}$, and $\eta\equiv17\pmod{27}$,



$$
F\equiv1+25\cdot17=426\equiv21\pmod{27}.
$$



Thus



$$
v_3(F)=1,\qquad F/3\equiv1\pmod3.
$$



For $G$, the bracket in (9.5) is



$$
2+1\cdot2\cdot1\equiv1\pmod3.
$$



For $H$, the second term is one digit deeper than $\rho^2$. Therefore



$$
\boxed{
v_3(F)=1,\qquad v_3(G)=4,\qquad v_3(H)=8,
}
\tag{9.7}
$$



and more precisely,



$$
\boxed{
F/3\equiv G/3^4\equiv H/3^8\equiv1\pmod3.
}
\tag{9.8}
$$



This supplies a sharper analysis of the **complete** pure scalar than separate lower bounds on the two terms in the Christoffel kernel subtraction.

---

# Part III. Endpoint-sensitive factorial preservation

## 10. A stronger bound for the complete factorial response

Let



$$
x=v_3(J_e),\qquad y=v_3(D_e).
$$



Both are finite: the real Jacobi zeros lie in $(0,1)$, so neither polynomial vanishes at $-1$.

Equation (9.1), with unit $E$, gives the exact equality of ideals



$$
(J_e,Z(-1))=(J_e,\rho D_e)
$$



over $\mathbb Z_3$. Hence



$$
\boxed{
e_*:=\min\{v_3(J_e),v_3(Z(-1))\}
=\min\{x,4+y\}.
}
\tag{10.1}
$$



In the quotient-free endpoint identity, every endpoint multiplier is now divisible by $3^{e_*}$. Repeating the weighted-coefficient proof with this retained factor yields



$$
v_3(u_i)+w_i\ge g-1+e_*
$$



for every $i$, and



$$
v_3(u_i)+w_i\ge g+e_*
\qquad(i\ge2).
$$



Consequently,



$$
\mathfrak f(Q_cU^2)\in3^{2g-2+2e_*}\mathbb Z_3,
$$



and



$$
(\mathcal Fu)_a\in
3^{g-1+e_*+w_a}\mathbb Z_3.
$$



The same exact resolvent identity therefore proves:

### Theorem 10.1 — Endpoint-content refinement



$$
\boxed{
v_3(K_c-K_J)\ge
h-2s+2g-2+2e_*.
}
\tag{10.2}
$$



The higher remainder remains at least $h-s\ge2$ digits deeper.

This theorem does not assume an endpoint unit. It retains the complete factorial contraction and every higher correction.

---

## 11. Exact pure-scalar depths outside two endpoint classes

Let



$$
d=x-y.
$$



The three terms in (9.3) have valuations



$$
1+2x,\qquad 4+x+y,\qquad 8+2y.
\tag{11.1}
$$



Since $L/E^2$ is a unit, these determine the valuation of $U(-1)$ whenever the minimum is unique, and (9.8) resolves the first tied digit.

### Case 1: $d\le2$

The first term is uniquely shallowest:



$$
\boxed{v_3(U(-1))=1+2x=1+2e_*.}
\tag{11.2}
$$



### Case 2: $d\ge5$

The last term is uniquely shallowest:



$$
\boxed{v_3(U(-1))=8+2y=2e_*.}
\tag{11.3}
$$



### Case 3: $d=3$

Set



$$
t=\frac{J_e}{27D_e}\in\mathbb Z_3^\times.
$$



At valuation $7+2y$, the leading residue is a unit square times



$$
t^2+t.
$$



Thus, if $t\equiv1\pmod3$,



$$
\boxed{v_3(U(-1))=7+2y=1+2e_*.}
\tag{11.4}
$$



The exceptional residue is $t\equiv-1\pmod3$.

### Case 4: $d=4$

Set



$$
t=\frac{J_e}{81D_e}\in\mathbb Z_3^\times.
$$



At valuation $8+2y$, the leading residue is a unit square times



$$
t+1.
$$



Thus, if $t\equiv1\pmod3$,



$$
\boxed{v_3(U(-1))=8+2y=2e_*.}
\tag{11.5}
$$



Again, the exceptional residue is $t\equiv-1\pmod3$.

### The precise exceptional set

The only unresolved first-digit configurations are



$$
\boxed{
x-y=3,\qquad
\frac{J_e}{27D_e}\equiv-1\pmod3,
}
\tag{11.6}
$$



or



$$
\boxed{
x-y=4,\qquad
\frac{J_e}{81D_e}\equiv-1\pmod3.
}
\tag{11.7}
$$



These are correlated endpoint conditions. Estimating $J_e$ and $D_e$ independently would not identify them.

---

## 12. A nine-digit scalar-preservation theorem

Because



$$
h-s+2g-2=2r+2g,
$$



the bound (10.2), compared with $K_J=3^{-s}U(-1)$, gives



$$
v_3(K_c-K_J)-v_3(K_J)
\ge
2r+2g+2e_*-v_3(U(-1)).
$$



Outside (11.6)–(11.7), the last valuation is either $2e_*$ or $1+2e_*$. Since $g\ge5$,



$$
v_3(K_c-K_J)-v_3(K_J)\ge9.
$$



### Theorem 12.1 — Complete factorial preservation on nonexceptional original tuples

On the stated normalized original-family branch, if the endpoint pair does not satisfy either (11.6) or (11.7), then



$$
\boxed{
v_3(K_c)=v_3(K_J),
\qquad
\frac{K_c}{K_J}\in1+3^9\mathbb Z_3.
}
\tag{12.1}
$$



This concerns the whole scalar $K_J$ and the whole factorial response $K_c-K_J$.

### What is and is not decided

This theorem provides a concrete, low-precision classification for **genuine original tuples**. It is not based on replacing $m$ by an auxiliary integer.

However, the attached work does not supply the projective endpoint residues needed to certify a nonempty or infinite nonexceptional original subbranch. I therefore do **not** claim that such a subbranch has been constructed here.

The new outstanding endpoint lemma is:

> **Original projective endpoint lemma.**  
> For the established normalized original family, certify the primitive pair obtained from
> 

$$
> \bigl(J_m(-1),J_{m-1}(-1)\bigr)
>
$$


> modulo $3^5$, and prove that an original tuple—or an infinite original subbranch—avoids (11.6) and (11.7).

Five projective digits suffice to classify the nonexceptional cases. Indeed, after dividing both endpoints by their common valuation:

- a unit first coordinate is immediately nonexceptional;
- if the second coordinate is a unit, the first five digits distinguish depths $1,2,3,4,\ge5$;
- at depths $3,4$, the first nonzero unit digit decides the displayed residue condition.

Certifying that projective normalization is part of the obligation. Merely printing two residues modulo $3^5$ before removing a potentially large common endpoint factor would not suffice.

If an endpoint pair is exceptional, the exact quadratic (9.3) supplies the next lift target. A sufficient preservation test is



$$
v_3(FJ_e^2+GJ_eD_e+HD_e^2)
<
2(r+g)+2e_*.
\tag{12.2}
$$



No favorable outcome is assumed in those exceptional cases.

---

# Part IV. Binary observables under simultaneous digit changes

## 13. Why the integral rank-three quotient does not itself transport

For the original binary input,



$$
b=150094635296999121,
\qquad
n=4002b=600678730458590482242,
$$



the exact functional is



$$
\mathscr L_{n,b}(P)
=
\sum_{j=0}^{b}
\binom{n+2}{j}^{\!2}
\binom{2n+b-j-1}{b-j}^{\!2}P(j).
\tag{13.1}
$$



The telescoping relation has zero flux because its coefficient contains $(b-j)^2$. Its saturated degree-$162$ quotient is free of rank three.

But a digit split $j=2k+d$ changes:

- the weight;
- the two binomial upper parameters;
- the cutoff;
- the parity-dependent endpoint;
- and generally the polynomial or rational factor multiplying the daughter weight.

Moreover,



$$
\left\lfloor\frac n2\right\rfloor
\ne4002\left\lfloor\frac b2\right\rfloor
$$



when $b$ is odd. Thus a quotient theorem at one fixed $(n,b)$ does not prove a cross-scale rank-three theorem.

The correct response is to supply an exact transport representation and then certify whatever observable compression it actually admits.

---

## 14. An exact rational representation of the original finite sum

Introduce variables $x,y,u,v$, and set



$$
A_0=(1+x)^2(1+y)^2,
$$





$$
U_0=(1+x)(1+y),
\qquad
V_0=(1-u)^2(1-v)^2.
$$



For $n,b\ge0$, constant-term extraction gives



$$
\mathscr L_{n,b}(P)
=
\operatorname{CT}_{x,y,u,v}
A_0\left(\frac{U_0}{V_0}\right)^n
\sum_{j+k=b}P(j)(xy)^{-j}(uv)^{-k}.
\tag{14.1}
$$



The equality is termwise:



$$
[x^j](1+x)^{n+2}=\binom{n+2}{j},
$$





$$
[u^k](1-u)^{-2n}=\binom{2n+k-1}{k}.
$$



In particular, $j+k=b$ enforces exactly $0\le j\le b$. The terminal term $j=b$ is present.

Let



$$
\mathcal E_\ell(z)=
(1-z)^{\ell+1}\sum_{j\ge0}j^\ell z^j.
$$



For $\ell=0$, use $\mathcal E_0=1$; for $\ell>0$, this is the usual integral Eulerian numerator.

Take $D=162$, and define the common denominator



$$
\boxed{
Q=
(V_0-txyuvU_0)
(1-zuv)^{D+1}
(1-zxy).
}
\tag{14.2}
$$



It has constant coefficient $1$.

For $P(j)=\sum_{\ell=0}^D p_\ell j^\ell$, set



$$
\boxed{
N_P=
A_0V_0
\sum_{\ell=0}^D
p_\ell\,
\mathcal E_\ell(zuv)
(1-zuv)^{D-\ell}.
}
\tag{14.3}
$$



Then the exact observable is the six-variable coefficient



$$
\boxed{
\mathscr L_{n,b}(P)
=
[t^n z^b x^{n+b}y^{n+b}u^{n+b}v^{n+b}]
\frac{N_P}{Q}.
}
\tag{14.4}
$$



### Derivation of the exponent $n+b$

Before clearing Laurent monomials, the generating function is



$$
A_0
\frac{1}{1-tU_0/V_0}
\frac{\mathcal E_\ell(z/(xy))}
     {(1-z/(xy))^{\ell+1}}
\frac{1}{1-z/(uv)}.
$$



Replacing both $t$ and $z$ by their product with $xyuv$ converts constant-term extraction into the coefficient with all four auxiliary exponents equal to $n+b$. This produces exactly (14.2)–(14.4).

Thus this representation is specific to the complete original squared-binomial summand and its finite convolution. It is not an appeal to generic automaticity.

---

## 15. Simultaneous digit changes and the carry states

For a uniform description along $n=4002b$, let the remaining high parts satisfy



$$
n^{(r)}=4002b^{(r)}+c_r.
$$



Initially $c_0=0$. If the next binary digit of $b$ is $\delta$, then



$$
\epsilon=c_r\bmod2
$$



is the next digit of $n$, and



$$
\boxed{
c_{r+1}=2001\delta+\left\lfloor c_r/2\right\rfloor.
}
\tag{15.1}
$$



The finite range



$$
0\le c_r\le4001
$$



is invariant.

To obtain the digit of $n+b$, retain the usual addition carry $a_r\in\{0,1\}$:



$$
\sigma=(\epsilon+\delta+a_r)\bmod2,
$$





$$
\boxed{
a_{r+1}=\left\lfloor
\frac{\epsilon+\delta+a_r}{2}
\right\rfloor.
}
\tag{15.2}
$$



The relevant Cartier digit vector in the variable order
$(t,z,x,y,u,v)$ is therefore



$$
\boxed{(\epsilon,\delta,\sigma,\sigma,\sigma,\sigma).}
\tag{15.3}
$$



These formulas explicitly retain the simultaneous changes in $n$ and $b$.

One must flush the remaining $n$-carry and addition carry after the last nonzero digit of $b$; stopping at the binary length of $b$ is incorrect. For the fixed input, all six target exponents in (14.4) have at most $70$ binary digits.

---

## 16. A directly proved prime-power invariant bound

Let $\Lambda_{\mathbf d}$ denote multivariate binary Cartier extraction:



$$
\Lambda_{\mathbf d}
\left(\sum_{\mathbf a}c_{\mathbf a}X^{\mathbf a}\right)
=
\sum_{\mathbf a}c_{2\mathbf a+\mathbf d}X^{\mathbf a}.
$$



Put



$$
E_Q=\frac{Q(X)^2-Q(X^2)}2\in\mathbb Z[X].
\tag{16.1}
$$



For precision $2^K$, consider layered rational states



$$
\boxed{
\sum_{\tau=0}^{K-1}
2^\tau\frac{P_\tau}{Q^{\tau+1}},
}
\tag{16.2}
$$



where the coefficients of $P_\tau$ are needed only modulo $2^{K-\tau}$.

### Exact transition modulo $2^K$

For $e=\tau+1$,



$$
\frac{1}{Q^{2e}}
=
\frac{1}{Q(X^2)^e}
\left(1+\frac{2E_Q}{Q(X^2)}\right)^{-e}.
$$



Expanding only to the required finite precision gives



$$
\boxed{
\Lambda_{\mathbf d}\left(
2^\tau\frac{P_\tau}{Q^e}
\right)
\equiv
\sum_{k=0}^{K-1-\tau}
2^{\tau+k}(-1)^k
\binom{e+k-1}{k}
\frac{
\Lambda_{\mathbf d}(P_\tau Q^e E_Q^k)
}{Q^{e+k}}
\pmod{2^K}.
}
\tag{16.3}
$$



This is an explicit cross-scale identity. No inversion of an even scalar is used.

### Degree invariance

The multidegree of $Q$, in the six variables above, is bounded by



$$
\boxed{
\mathbf d_Q=(1,164,3,3,165,165).
}
\tag{16.4}
$$



The numerator $N_P$ has coordinatewise degree at most $\mathbf d_Q$.

Suppose



$$
\deg_{X_i}P_\tau\le(\tau+1)(\mathbf d_Q)_i.
$$



Since



$$
\deg E_Q\le2\mathbf d_Q,
$$



the numerator inside Cartier extraction in (16.3) has degree at most



$$
2(e+k)\mathbf d_Q.
$$



After extraction it has degree at most



$$
(e+k)\mathbf d_Q,
$$



which is precisely the bound for layer $\tau+k$.

Therefore the layered module is invariant.

### Explicit finite ambient bound

A sufficient number of polynomial coefficient generators is



$$
\boxed{
B_K=
\sum_{e=1}^{K}
(e+1)(164e+1)(3e+1)^2(165e+1)^2.
}
\tag{16.5}
$$



This is a rigorous bound depending on the requested precision and payload degree, not on the enormous summation length $b$.

It is not a claim of practical feasibility: the box bound is large. Its value is that it supplies a precise invariant ambient module in which smaller reachable/observable certificates can be tested. Newton-support restrictions and actual reachable spans may reduce it substantially, but no reduction is asserted without its certificate.

---

## 17. How the three certified observables should be transported

Suppose the coordinator’s pending saturation supplies integral generators



$$
S_1,S_2,S_3\in\mathbb Z_{(2)}[j]_{\le162}.
$$



Map each to the rational state



$$
H_i=N_{S_i}/Q.
$$



Then transport these states by (16.3) along the actual digit vectors (15.3). At the end, the required coefficient is the constant coefficient of the resulting rational state. Since $Q(0)=1$, a state (16.2) has terminal value



$$
\boxed{
\sum_{\tau=0}^{K-1}2^\tau P_\tau(0)\pmod{2^K}.
}
\tag{17.1}
$$



This evaluates the original observables without asserting that the daughter states are again polynomial classes in the same rank-three telescoping quotient.

### A sufficient smaller cross-scale certificate

A5 can replace the ambient module by states $H_1,\ldots,H_R$, provided the following are certified.

1. **Initialization.**  
   Each actual $N_{S_i}/Q$ has a stated integral coordinate vector in the proposed state module.

2. **Digit closure.**  
   For every required digit vector—either all eight possible triples $(\epsilon,\delta,\sigma)$, or the explicitly reachable carry-state transitions—
   

$$
\Lambda_{\mathbf d}H_i
   \equiv\sum_j M_{\mathbf d,ij}H_j
   \pmod{2^K}.
$$



3. **Verification of the congruences.**  
   These are formal rational-function congruences, verified after multiplication by the common denominator $Q^K$. Because $Q(0)=1$, this multiplication loses no precision.

4. **Terminal functional.**  
   The constant-coefficient functional is supplied on every state.

5. **Carries and flushing.**  
   The multiplication carry (15.1), addition carry (15.2), and final zero-digit flush are included.

If a rank-three transport is claimed, these conditions must actually hold with $R=3$, or modulo a separately certified invariant unobservable submodule. Such a submodule must be stable under all required digit maps and annihilated by the terminal functional. Merely having three classes in one fixed-degree quotient proves neither condition.

This is the exact distinction between:

- three observables at the original index; and
- a three-dimensional cross-scale evaluator.

---

## 18. Precision and the coordinator’s pending calculation

The one pending $163\times160$ relation-matrix/payload calculation should provide



$$
[P_f]=\sum_i c_{f,i}[S_i],
\qquad
[P_m]=\sum_i c_{m,i}[S_i],
$$



and their certified free-coordinate contents $s_f,s_m$.

The sufficient pure-observable precisions remain



$$
K_f=\max(0,180-s_f),
\qquad
K_m=\max(0,177-s_m).
$$



The cross-scale evaluator can work at their maximum, or evaluate the two combinations at separate certified precisions.

Nothing here requests:

- a regenerated producer;
- a new physical force at $180$ bits;
- a rerun of the old formal boundary matrix;
- or an unguarded division by a nonunit Smith pivot.

The physical numerator data remain twenty-bit data. The larger precisions concern evaluation of exact integral observables for chosen lifts.

The physical $j=b$ contribution remains in (13.1) and (14.1). Zero telescoping flux has not been confused with deletion of the terminal summand.

---

# Part V. Outstanding full-producer and arithmetic obligations

## 19. The new scalar theorem does not settle the actual producer perturbation

The proof above compares $G_J$ with $G_c$. It does not evaluate the complete change



$$
Q_{\rm act}=Q_c+3^6R,
\qquad
R=R_{25}+3^{25}\Delta_{25}.
$$



For that comparison, both corrected representatives and the exact nonlinear term remain:



$$
\widehat Z^{\,\rm act}
=
\widehat Z^{\,c}-3^6WE_{\rm act}^{-1}T_R,
$$





$$
S_{\rm act}-S_c
=
3^6K_Z-3^{12}T_R^TE_{\rm act}^{-1}T_R.
$$



The actual directional pairing still uses the full endpoint solution. It must retain:

- all $\Delta_H$ layers;
- unpaired finite-cutoff terms;
- the $3^{25}\Delta_{25}$ remainder;
- both corrected factors;
- LOW/HIGH endpoint contributions;
- the nonlinear elimination term.

The original pole cutoff remains



$$
0\le v\le2n-2.
$$



The complete forcing remains both leading extractions, every permitted lower pole, factorial forcing, and LOW subtraction.

The terminal return remains



$$
\mu_{i+\nu}^{\langle26\rangle}
+\sum_{k=0}^{\nu-1}f_k\mu_{i+k}^{\langle26\rangle}
=b_i^{\langle26\rangle},
\qquad0\le i\le\nu-2,
$$





$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
$$



No moment beyond $D-4$ is added, and $\omega_{\nu-1}$ is retained.

---

## 20. All-prime reduction and the whole same-index error

Selected-prime improvements do not replace the actual arithmetic normalization.

For the A1 determinant pair, all row contents, the actual multiplier, and the least actual clearer must be restored before forming



$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,
\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$





$$
\boxed{g_\ell=\gcd(|A_\ell|,|B_\ell|)}
$$



over all primes. For $B_\ell\ne0$,



$$
q=\frac{|B_\ell|}{g_\ell},
\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
$$



and the relevant complete error is



$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{g_\ell}
\det H_{\rm complete}.
}
$$



For the A4 Gram normalization, likewise,



$$
A_B=N_{B,1}^T\Omega N_{B,1},
\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$





$$
g_B=\gcd(A_B,|H_B|),
\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
$$



The same-index whole error is



$$
q_n(e+\pi)-p_n=-q_n\epsilon_n.
$$



Neither the new $3$-adic scalar classification nor a completed binary observable evaluation proves nonvanishing and decay of these whole forms after the all-prime gcd.

---

# Part VI. Exact next certificates and proof status

## 21. New bounded arithmetic interfaces

No accepted bounded computation needs to be rerun.

### 21.1 The new projective endpoint certificate

**Input**

- one certified original tuple on the established normalized branch;
- the actual adjacent Jacobi normalization;
- a certified common endpoint valuation for
  

$$
J_m(-1),\ J_{m-1}(-1);
$$


- the resulting primitive endpoint pair modulo $3^5$.

**Expected verifiable output**

- classification into the nonexceptional cases or one of (11.6)–(11.7);
- in a nonexceptional case, the exact formula
  

$$
v_3(K_J)=-s+2e_*
  \quad\text{or}\quad
  -s+2e_*+1;
$$


- the certified conclusion
  

$$
K_c/K_J\in1+3^9\mathbb Z_3.
$$



If the pair is exceptional, the output must say so and supply the next required quadratic precision from (12.2). The five-digit interface does not by itself provide a bounded-cost algorithm for computing the original-family endpoint pair; constructing that compressed evaluator remains a concrete mathematical obligation.

### 21.2 The binary cross-scale certificate

**Input**

- the coordinator’s actual three integral quotient generators;
- the certified $K_f,K_m$;
- the fixed original $n,b$;
- the explicit $Q,N_{S_i}$ from (14.2)–(14.3).

**Expected verifiable output**

- initialization vectors;
- certified digit-transition identities at the stated precision;
- the actual reachable state dimension, not a presumed value three;
- the multiplication and addition carry transitions;
- the terminal functional;
- the resulting three observable residues, if evaluation is completed;
- separately, the two reconstructed contractions after their actual denominator guards.

The coordinator’s Smith/payload output and A5’s observable evaluation remain distinct certificates.

---

## 22. Proof-status ledger

| Statement | Status |
|---|---|
| Closed reachability, no-overlap, and deep-family inverse exclusion | Reused; not reopened |
| Actual Bernstein gap $g\ge5$ | Independently verified proof |
| Adjacent constant ratio and $v_3(A)=5$ | Independently derived |
| Normalized Christoffel constant valuation $g-1$ | Verified under retained hypotheses |
| A1turn8 all-degree weighted jets | Verified |
| Whole factorial-response bound and higher remainder | Verified |
| Correct leading coefficient $2L^2\zeta^2J(-1)^2$ | Verified |
| Actual recurrence normalizers $b_m,\rho$ in the scalar calculation | Explicitly retained |
| Complete pure scalar as (9.3) | **New exact derivation** |
| Quadratic coefficient valuations $1,4,8$ | **New proof** |
| Endpoint-content response gain $2e_*$ | **New proof** |
| Nine-digit scalar preservation outside two endpoint classes | **New conditional theorem on original tuples** |
| Certified nonempty/infinite original nonexceptional subbranch | Not yet established |
| Original binary finite-sum rational representation | **New exact derivation** |
| Simultaneous $n,b$ carry interface | **New exact derivation** |
| Prime-power layered Cartier invariant bound | **New proof** |
| Rank-three cross-scale closure | Not assumed; requires certificate |
| Coordinator’s $163\times160$ Smith/payload output | Pending |
| Original three binary observables | Not evaluated here |
| Full actual-producer perturbation | Open |
| All-prime primitive denominator and whole-error decay | Open |
| Irrationality or rationality of $e+\pi$ | Unresolved |

---

## Conclusion

The A1turn8 factorial theorem survives independent review, with its explicitly repaired factor $2$.

The new scalar result is the exact correlated endpoint formula



$$
\boxed{
K_J=
3^{-s}\frac{L}{(A+74)^2}
\left(FJ(-1)^2+GJ(-1)D(-1)+HD(-1)^2\right),
}
$$



with



$$
\boxed{v_3(F),v_3(G),v_3(H)=(1,4,8).}
$$



Together with the stronger whole-response bound



$$
\boxed{
v_3(K_c-K_J)\ge h-2s+2g-2+2e_*,
}
$$



it proves nine-digit preservation outside two precisely stated projective endpoint classes. The remaining pure/core bottleneck is no longer an unspecified complete-kernel subtraction: it is a certified original-family projective endpoint calculation, followed by additional lifts only in the two exceptional classes.

For the binary target, the new contribution is an exact cross-scale representation of the **original finite observable**, including its terminal term, and a proved prime-power invariant module. This gives A5 a concrete closure test rather than an assumption that fixed-degree saturation commutes with Cartier.

Beyond these local advances remain the complete actual-producer perturbation, complete forcing and terminal return, all row contents, the all-prime final gcd, the actual primitive denominator, and the whole same-index error.



$$
\boxed{\text{An unconditional proof or disproof of irrationality of }e+\pi
\text{ remains unresolved.}}
$$


