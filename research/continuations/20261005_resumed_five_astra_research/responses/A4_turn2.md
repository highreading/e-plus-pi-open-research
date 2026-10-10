> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 independent audit: original prime-$29$ population and terminal Jacobi norm valuations

## Executive conclusions

The two specialized constructions have different outcomes.

1. **The prime-$29$ population construction is valid.** Its one-digit Lucas argument forces
   

$$
29\mid X_k\qquad(0\le k\le H)
$$


   on exactly the stated 100 sufficient residue classes of the original progression parameter $t\bmod841$. It includes both endpoints and imposes no condition on higher digits. These are **component-common-content classes**, not classes carrying a nonzero isotropic residual vector.

2. **The former conditional norm–mixed theorem consequently has an infinite original-index application.** On those classes, at the retained complete-force and finite-reconstruction interfaces,
   

$$
D,M\in29^2\mathbb Z_{29},\qquad
   M-(6C_n)^{-1}D\in29^3\mathbb Z_{29}.
$$


   The construction does **not** evaluate $D/29^2\bmod29$, does not prove that either valuation is exactly two, and does not control their difference at greater depth.

3. **The Jacobi factorial and digit-sum identities are correct, with one necessary scope qualification.** On the whole original resonance domain,
   

$$
v_3(A)=1+v_3(j)\ge5,
$$


   not necessarily $5$. The formulas through the complement identity remain valid throughout that domain. The specialization $D=3^5e$ with $3\nmid e$ applies specifically when $v_3(j)=4$. A uniform version uses $w=v_3(A)=v_3(D)$.

4. **The explicit terminal norm valuation simplifies a scalar factor; it does not resolve the original monomial-coordinate inverse or endpoint losses.** In particular, it does not repair the accepted precision obstruction at $v_3(j)=4$: the first transported residual block divided by $3^6$, modulo $3$, remains undetermined by the core approximation.

Neither result proves rationality or irrationality of $e+\pi$.

---

## 1. Review scope and overlap gate

I use the supplied prior results at their stated scopes:

- A2 turn19’s component-common-content implication and exact second norm digit;
- the completed conditional third-defect theorem reviewed in A4 turn1;
- A1 turn21’s exact base Jacobi norm, core endpoint formula, complete perturbation formula, and precision obstruction.

I do not replay the completed universal $\Gamma_0,\Gamma_1$ calculation or infer its infinite transfer solely from a finite receipt.

No external calculation, filesystem search, hash verification, or browsing has been executed in this response. The attached search descriptions and receipts are source data. In particular, the supplied account that the primary Rowland–Yassawi paper was opened before the six-state application is retained as provenance, not represented as an action independently performed here.

The overlap assessment is correspondingly bounded:

- the common-content implication is already in A2 turn19;
- Lucas factorization, Jacobi norms, and Legendre valuations are classical;
- the items audited here are the particular sufficient cylinders, their original-exponent reachability, and the terminal specialization of the norm formula;
- no exhaustive novelty claim is made.

---

# Part I. The prime-$29$ construction

## 2. Original domain and notation

Throughout this part,


$$
p=29,\qquad L=p^4,\qquad
a=432827+682892t,\quad t\ge0,
$$




$$
b=3^a,\qquad n=2001b.
$$


The actual coordinates remain $0\le j\le b$, and every contact inverse remains on the finite range $0\le i,j<b$.

Write


$$
b=687936+Lh,\qquad h=pH+d,\qquad 0\le d<p,
$$


and


$$
A=69h+67=2001H+69d+67.
$$


The residual components are the actual integers


$$
X_k=\binom Ak\binom{2A+H-k}{H-k},
\qquad 0\le k\le H.
$$


Since $A>H$, both binomial coefficients have nonnegative, legitimate arguments throughout this range.

Set


$$
\mathcal T=\sum_{k=0}^{H}X_k^2,\qquad
T=\mathcal T\bmod p,\qquad
U=\sum_{k=0}^{H}kX_k^2\bmod p,
$$


and, when $T=0$,


$$
T_1=\frac{\mathcal T}{p}\bmod p.
$$



The actual weighted columns and scalar contractions are


$$
P=\frac{Z_w}{p^2},\qquad Q=\frac{Y}{p^3},\qquad
D=P^TP,\qquad M=P^TQ,
$$


with the falling metric already absorbed into the coordinates.

The letter $A$ in this part is unrelated to the Jacobi parameter in Part II.

---

## 3. Complete one-digit Lucas proof

Let


$$
\alpha=(11d+9)\bmod29,\qquad 0\le\alpha\le28,
$$


and


$$
r=H\bmod29,\qquad 0\le r\le28.
$$


Indeed,


$$
A=2001H+69d+67\equiv11d+9\pmod{29},
$$


because $2001=69\cdot29$.

Assume


$$
\boxed{1\le\alpha\le14,\qquad29-\alpha\le r\le28.}
\tag{3.1}
$$



### Proposition 3.1

Under (3.1),


$$
29\mid X_k
$$


for every actual $k\in\{0,\ldots,H\}$.

### Proof

Write $k_0=k\bmod29$.

**Case 1: $k_0>\alpha$.** Lucas’s theorem gives


$$
\binom Ak\equiv0\pmod{29}.
$$


Therefore $29\mid X_k$.

**Case 2: $k_0\le\alpha$.** Since


$$
r\ge29-\alpha>\alpha
$$


for $\alpha\le14$, we have $k_0<r$. Thus subtraction of $k$ from $H$ produces no units-digit borrow. The units digit of $H-k$ is


$$
j_0=r-k_0.
$$



Also $2\alpha\le28$, so the units digit of $2A$ is exactly $2\alpha$, with no doubling carry out of this digit before the addition of $H-k$.

The units sum in $2A+(H-k)$ satisfies


$$
29\le\alpha+r
\le2\alpha+r-k_0
\le2\alpha+r
\le56.
$$


It therefore produces exactly one carry, and its reduced units digit is


$$
s_0=2\alpha+r-k_0-29.
$$


Comparing with the lower binomial digit,


$$
s_0-j_0=2\alpha-29<0.
$$


Hence $s_0<j_0$, and Lucas gives


$$
\binom{2A+H-k}{H-k}\equiv0\pmod{29}.
$$


Again $29\mid X_k$.

The two cases exhaust the original finite summation range. ∎

### Endpoint audit

No endpoint is omitted.

- At $k=0$, the second case applies. The carry proves
  

$$
29\mid \binom{2A+H}{H}=X_0.
$$


- At $k=H$, $k_0=r>\alpha$, so the first case applies:
  

$$
29\mid\binom AH=X_H.
$$



Higher-digit borrows and carries cannot reverse either units-digit Lucas zero. No hypothesis on the higher digits is needed.

### Consequence

By the already established common-content implication,


$$
\boxed{
\mathcal T\in29^2\mathbb Z,\qquad
T=T_1=U=0.
}
\tag{3.2}
$$


For $0\le d\le24$, the retained exact formula


$$
D_1=C_n^2\bigl(f(d)T_1+\beta(d)U\bigr)\pmod{29}
$$


then gives


$$
\boxed{D_1=0.}
\tag{3.3}
$$



This is stronger than merely obtaining $T=0$, but in a specific way: the entire residual vector is zero modulo $29$. It does not populate the locus of nonzero isotropic vectors.

---

## 4. All eligible $d$, and the exact count of sufficient classes

For completeness, the units digits for every $d\in\{0,\ldots,24\}$ are


$$
\begin{array}{c|rrrrrrrrrrrrr}
d&0&1&2&3&4&5&6&7&8&9&10&11&12\\ \hline
\alpha&9&20&2&13&24&6&17&28&10&21&3&14&25
\end{array}
$$


and


$$
\begin{array}{c|rrrrrrrrrrrr}
d&13&14&15&16&17&18&19&20&21&22&23&24\\ \hline
\alpha&7&18&0&11&22&4&15&26&8&19&1&12.
\end{array}
$$



Thus precisely the following $d$ are selected by condition (3.1):


$$
\begin{array}{c|r|c|r}
d&\alpha&r\text{ range}&\text{number}\\ \hline
0&9&20,\ldots,28&9\\
2&2&27,\ldots,28&2\\
3&13&16,\ldots,28&13\\
5&6&23,\ldots,28&6\\
8&10&19,\ldots,28&10\\
10&3&26,\ldots,28&3\\
11&14&15,\ldots,28&14\\
13&7&22,\ldots,28&7\\
16&11&18,\ldots,28&11\\
18&4&25,\ldots,28&4\\
21&8&21,\ldots,28&8\\
23&1&28&1\\
24&12&17,\ldots,28&12
\end{array}
$$


The total is


$$
9+2+13+6+10+3+14+7+11+4+8+1+12=100.
$$



Each pair $(d,r)$ defines a different class


$$
h\equiv d+29r\pmod{841}.
$$



These are exactly 100 classes **selected by this sufficient condition**. This is not a classification of all classes on which the residual components vanish.

---

## 5. Original-exponent reachability

### 5.1 The finite modular inputs

The source receipt reports


$$
3^{432827}\equiv687936+29^4\cdot741\pmod{29^6},
\tag{5.1}
$$




$$
3^{682892}\equiv1+29^4\cdot73\pmod{29^6}.
\tag{5.2}
$$



The explicit residues are


$$
29^4=707281,\qquad29^6=594823321,
$$




$$
687936+707281\cdot741=524783157,
$$




$$
1+707281\cdot73=51631514.
$$



These are bounded modular-exponentiation identities, not asymptotic statements. Their source computation is supplied; I have not rerun modular exponentiation. A short independent verification procedure is specified in §15.

The remaining reachability argument is exact algebra from (5.1)–(5.2).

### 5.2 Affine evolution of $h$

For every nonnegative integer $t$,


$$
(1+73\cdot29^4)^t
\equiv1+73t\cdot29^4\pmod{29^6},
$$


because all terms of order at least two contain $29^8$.

Consequently


$$
h(t)\equiv741+695t\pmod{841},
\tag{5.3}
$$


where


$$
687936\equiv-2\pmod{841},
\qquad
73(-2)\equiv695\pmod{841}.
$$



The slope is a unit. More explicitly,


$$
695=-1-5\cdot29,\qquad
695^{-1}\equiv144\pmod{841},
$$


since


$$
695\cdot144=100080=119\cdot841+1.
$$



The exponent class corresponding to $h=d+29r$ is therefore


$$
\boxed{
t\equiv144(d+29r-741)
\equiv144d-29r+103\pmod{841}.
}
\tag{5.4}
$$



This formula gives a compact exact audit of all 100 certificate rows.

For example, at $d=0,r=20$,


$$
t\equiv-580+103\equiv364\pmod{841}.
$$


Increasing $r$ by one decreases $t$ by $29$, exactly as in the receipt.

Reduction of (5.3) modulo $29$ recovers


$$
d(t)\equiv16-t\pmod{29}.
$$



### 5.3 Order and infinitude

Equation (5.2), with $29\nmid73$, proves


$$
v_{29}(3^{682892}-1)=4.
$$


For a positive integer $s$, LTE gives


$$
v_{29}\bigl((3^{682892})^s-1\bigr)=4+v_{29}(s).
$$


Hence the order of $3^{682892}$ modulo $29^6$ is exactly $29^2$.

Equivalently, (5.3) is a bijection from $t\bmod841$ to $h\bmod841$. The 100 selected $h$-classes therefore give 100 distinct original $t$-classes. Each contains infinitely many nonnegative integers.

The resulting indices are actual


$$
b=3^{432827+682892t},
$$


not auxiliary choices of $H,A$, or $h$.

---

## 6. Auxiliary six-state recursion: audit and scope

The six-state recursion is consistent with the direct Lucas proof.

A state records:

- the borrow in computing $H-k$, belonging to $\{0,1\}$;
- the carry in computing $2A+(H-k)$, belonging to $\{0,1,2\}$.

The latter range is closed because


$$
0\le2a_i+j_i+c_i\le2\cdot28+28+2=86.
$$



For fixed digits of $A,H$, each path chooses the digits of $k$, and its weight is precisely


$$
\prod_i
\binom{a_i}{k_i}^{\!2}
\binom{s_i}{j_i}^{\!2}\pmod{29}.
$$


Lucas identifies this with $X_k^2\bmod29$.

Rejecting final borrow $1$ preserves $k\le H$. After all digits of $A,H$ have been processed, the upper-binomial carry may be accepted in any of its three states: its remaining lower digit is zero, so the final factor is


$$
\binom c0=1.
$$



For the first moment $U$, weighting only the first transition by $k_0$ is correct because


$$
k\equiv k_0\pmod{29}.
$$



The supplied 2525-case comparison has only its reported finite scope. The infinite meaning of the recursion follows from this path factorization, not the comparison. It is also unnecessary for the direct sufficient-cylinder proof.

A recursion modulo $841$ would need additional factorial-unit and carry information; the six-state recursion modulo $29$ does not supply it.

---

## 7. Exact infinite norm–mixed consequence

Let $\mathcal C\subset\mathbb Z/841\mathbb Z$ be the 100 classes defined by (3.1) and (5.4).

### Theorem 7.1 — populated same-index third-depth alignment

For every original index


$$
a=432827+682892t,\qquad t\ge0,\qquad t\bmod841\in\mathcal C,
$$


the sufficient Lucas construction gives


$$
T=T_1=U=D_1=0,\qquad d\le24.
$$


At the retained original-force and finite-reconstruction interfaces,


$$
\boxed{
D,M\in29^2\mathbb Z_{29},\qquad
\frac{M}{29^2}
\equiv(6C_n)^{-1}\frac{D}{29^2}\pmod{29}.
}
\tag{7.1}
$$


There are infinitely many such original indices.

### Proof

The population assertions were proved above. They meet the exact hypotheses of the accepted conditional theorem. ∎

Because $C_n$ is a unit, precisely the following finite-depth alternatives follow:

- If
  

$$
D/29^2\not\equiv0\pmod{29},
$$


  then
  

$$
v_{29}(D)=v_{29}(M)=2.
$$


- If
  

$$
D/29^2\equiv0\pmod{29},
$$


  then
  

$$
v_{29}(D),v_{29}(M)\ge3.
$$



**The value of $D/29^2\bmod29$ has not been evaluated.**

On these particular classes, $T_1=U=0$ already kills the earlier contraction $r_0T_1+r_1U$. Thus the completed universal $\Gamma_0$ identity is not necessary for this special population argument, although it remains useful on the larger conditional locus.

### What has improved?

The construction closes the former **nonvacuity and infinite-population gap**. It gives an explicit infinite same-index application of the conditional theorem.

It does not add an all-depth relative-valuation theorem. Simultaneously increasing two lower bounds does not control their difference.

---

## 8. The next actual-force obligation at $29$

The next relevant scalar is


$$
\mathscr D_2=\frac D{29^2}\bmod29.
$$


On the constructed classes, evaluating $\mathscr D_2$ would distinguish exact depth two from simultaneous passage to depth three.

It must be evaluated from the actual columns. It is not justified to replace the full third norm digit by an expression involving only


$$
\sum_k(X_k/29)^2.
$$


Higher kernel corrections, newly contributing low support, and finite-boundary terms have not been shown to disappear at this depth.

A concrete follow-on lemma is:

> **Actual third norm digit lemma on the common-content classes.**  
> Starting from the complete finite reconstruction of $P=Z_w/29^2$, derive $D/29^2\bmod29$ on the 100 original classes, retaining all corrected support and the endpoint. Give its dependence on the original higher digits and actual force parameters, and determine whether it is nonzero on an explicitly reachable infinite subclass.

Since $P\bmod29^3$ determines $P^TP\bmod29^3$, the previously audited precision-three representation is an appropriate starting point. The task is a new contraction, not a new assertion about Lucas population.

If that digit vanishes, further alignment requires actual information about


$$
\frac{M-(6C_n)^{-1}D}{29^3}\pmod{29},
$$


not another application of the same one-digit common-content argument.

---

# Part II. Terminal Jacobi norm identity

## 9. Original resonance domain and a scope correction

In this part retain


$$
j>0,\qquad81\mid j,\qquad n=4^j+1,
$$




$$
H=3^N,\qquad A=n-2=H-D,\qquad0<D<H/972,
$$




$$
m=\frac{A+1}{2}.
$$


The original columns are the monomials $1,y,\ldots,y^m$.

Here $A=4^j-1$ is odd, and LTE gives


$$
\boxed{v_3(A)=1+v_3(j).}
\tag{9.1}
$$


Thus $v_3(A)\ge5$ throughout the stated domain, and


$$
v_3(A)=5\iff v_3(j)=4.
$$



Accordingly, the coordinator’s phrase “the actual family has $v_3(A)=5$” requires restriction to this latter subdomain. The weaker statement $3^5\mid A$, sufficient for the earlier norm identities, holds on the entire domain.

---

## 10. Exact factorial cancellation

The accepted base norm is


$$
h_s=
\frac{\Gamma(s+A+1)\Gamma(s+\tfrac12)}
{(2s+A+\tfrac12)s!\Gamma(s+A+\tfrac12)L_s^2},
$$


where


$$
L_s=
\frac{\Gamma(2s+A+\tfrac12)}
{\Gamma(s+A+\tfrac12)s!}.
$$


Substitution first gives


$$
h_s=
\frac{\Gamma(s+A+1)\Gamma(s+\tfrac12)
      \Gamma(s+A+\tfrac12)s!}
{(2s+A+\tfrac12)\Gamma(2s+A+\tfrac12)^2}.
\tag{10.1}
$$



Using


$$
\Gamma(q+\tfrac12)=\frac{(2q)!\sqrt\pi}{4^q q!},
$$


the factors $\pi$, $s!$, and $(s+A)!$ cancel. The remaining power of $4$ is $4^{2s+A}$, and


$$
(2s+A+\tfrac12)^{-1}=\frac2{4s+2A+1}.
$$


Therefore


$$
\boxed{
h_s=
\frac{
2\,4^{2s+A}(2s)!(2s+2A)!((2s+A)!)^2
}{
(4s+2A+1)((4s+2A)!)^2
}.
}
\tag{10.2}
$$



This is an exact rational identity. No valuation estimate has been substituted for an equality.

At $s=m=(A+1)/2$,


$$
2m=A+1,\quad2m+2A=3A+1,\quad
2m+A=2A+1,\quad4m+2A=4A+2.
$$


Since $2$ and $4$ are $3$-adic units,


$$
\boxed{
v_3(h_m)=
v_3((A+1)!)+v_3((3A+1)!)
+2v_3((2A+1)!)
-2v_3((4A+2)!)
-v_3(4A+3).
}
\tag{10.3}
$$



All stated factorial cancellations pass.

---

## 11. Legendre reduction and exact hypotheses

Let $s_3(q)$ denote the ternary digit sum. Legendre’s formula gives


$$
v_3(q!)=\frac{q-s_3(q)}2.
$$


The linear terms in (10.3) cancel because


$$
(A+1)+(3A+1)+2(2A+1)-2(4A+2)=0.
$$



For $3\mid A$, the last ternary digit of each of $A,2A,4A$ is zero. Therefore


$$
s_3(A+1)=s_3(A)+1,
$$




$$
s_3(3A+1)=s_3(A)+1,
$$




$$
s_3(2A+1)=s_3(2A)+1,
$$




$$
s_3(4A+2)=s_3(4A)+2.
$$


It follows that


$$
\boxed{
v_3(h_m)
=s_3(4A)-s_3(A)-s_3(2A)-v_3(4A+3).
}
\tag{11.1}
$$



If $9\mid A$, then


$$
4A+3=3(1+4A/3),\qquad1+4A/3\equiv1\pmod3,
$$


so $v_3(4A+3)=1$. In particular, throughout the original domain,


$$
\boxed{
v_3(h_m)=s_3(4A)-s_3(A)-s_3(2A)-1.
}
\tag{11.2}
$$



Merely assuming $3\mid A$ would not suffice to replace the last valuation by $1$. The source’s auxiliary warning at $A=15$ is correct:


$$
4A+3=63,\qquad v_3(63)=2.
$$



---

## 12. Complement digits for $A=3^N-D$

The inequality $D<H/972$ ensures $qD<H$ for $q=1,2,4$. For every integer $x$ with $1\le x\le3^N$,


$$
s_3(3^N-x)=2N-s_3(x-1),
\tag{12.1}
$$


because


$$
3^N-x=(3^N-1)-(x-1),
$$


and $3^N-1$ consists of $N$ digits equal to $2$.

Thus


$$
s_3(A)=2N-s_3(D-1).
$$


Also,


$$
2A=H+(H-2D),
$$


where the second summand is strictly below $H$. The two blocks do not overlap, so


$$
s_3(2A)=1+2N-s_3(2D-1).
$$


Finally,


$$
4A=3H+(H-4D).
$$


Here $3H=3^{N+1}$ contributes a single digit $1$, the digit at position $N$ is zero, and the complement block lies below position $N$. Therefore


$$
s_3(4A)=1+2N-s_3(4D-1).
$$



Substitution into (11.2) proves


$$
\boxed{
v_3(h_m)
=-2N-1+s_3(D-1)+s_3(2D-1)-s_3(4D-1).
}
\tag{12.2}
$$



The leading-digit contributions and the final constant are all correct.

### Uniform valuation specialization

Put


$$
w=v_3(A).
$$


Since $0<A<H=3^N$, we have $w<N$, and hence


$$
v_3(D)=v_3(H-A)=w.
$$


Write


$$
D=3^w e,\qquad3\nmid e.
$$


For $q=1,2,4$,


$$
qD-1=3^w(qe-1)+(3^w-1),
$$


so


$$
s_3(qD-1)=s_3(qe-1)+2w.
$$


The uniform formula is therefore


$$
\boxed{
v_3(h_m)=
-2N+2w-1+
s_3(e-1)+s_3(2e-1)-s_3(4e-1),
\quad w=1+v_3(j).
}
\tag{12.3}
$$



When $v_3(j)=4$, this becomes exactly


$$
\boxed{
v_3(h_m)=
-2N+9+s_3(e-1)+s_3(2e-1)-s_3(4e-1).
}
\tag{12.4}
$$



Thus the terminal specialization passes after making its exact scope explicit.

---

## 13. What the norm valuation does—and does not—control

The accepted core endpoint formula is


$$
\mathscr K_{\rm core}
=
\left.
\frac{
F_{m+1}'(t)F_m(t)-F_m'(t)F_{m+1}(t)
}{
-3c\,a_mh_m(t-r)^2
}
\right|_{t=-1}.
$$


The new identity evaluates the valuation of the factor $h_m$.

It does not evaluate:

- the Wronskian numerator;
- $a_m=p_{m+1}(r)/p_m(r)$;
- cancellations in endpoint values;
- the original monomial-coordinate inverse entries;
- the transported endpoint solution.

Those are distinct quantities.

### Exact basis bookkeeping

Let $B$ have as columns the monomial coefficients of the monic Christoffel polynomials $q_0,\ldots,q_m$. Then over $\mathbb Q_3$,


$$
B^TG_{\rm core}B
=\operatorname{diag}(c h_0^c,\ldots,c h_m^c),
$$


and hence


$$
G_{\rm core}^{-1}
=
B\,\operatorname{diag}\bigl((c h_s^c)^{-1}\bigr)B^T.
\tag{13.1}
$$



This identity makes the missing hypotheses explicit. To bound original-coordinate inverse loss from it, one needs bounds on **all relevant coefficients of $B$** and the modified norms $h_s^c=-3a_sh_s$, not merely $h_m$.

For example, if


$$
\gamma_s=\min_i v_3(B_{is}),\qquad
\eta_s=v_3(c h_s^c),
$$


then termwise valuation gives the rigorous, but conditional, bound


$$
\min_{i,j}v_3((G_{\rm core}^{-1})_{ij})
\ge\min_s(2\gamma_s-\eta_s).
\tag{13.2}
$$


The new scalar identity supplies neither the $\gamma_s$ nor all the $\eta_s$. Thus it does not turn (13.2) into a new effective original-coordinate loss bound.

There is no Smith-integrality conclusion here. A rational triangular change of basis, even one with diagonal entries $1$, need not be integral over $\mathbb Z_3$.

### Accepted precision obstruction remains decisive

At


$$
v_3(j)=4,
$$


the actual polynomial precision is only $3^6$. By the accepted integral-elimination result, the first transported residual block


$$
3^{-6}G_{\rm residual}\pmod3
$$


is undetermined, and the transported endpoint has nonzero residue in those directions.

The new evaluation of $v_3(h_m)$ does not determine this missing actual block. It therefore cannot justify transferring the core endpoint valuation to the actual matrix.

**Verdict:** the terminal norm identity simplifies one exact scalar factor. No new useful bound on the original monomial inverse/endpoint loss follows from it alone.

---

## 14. Concrete actual-force obligation at $3$

Retain the complete functional and perturbation from A1 turn21:


$$
G_{\rm act}=G_{\rm core}+\Delta,
$$


where


$$
\begin{aligned}
\Delta_{ab}={}&
-\frac{3^h}{4}\mathfrak f(Q_n^{\rm loc}y^{a+b})\\
&+
3^{h+\tau}
\sum_{v\ge0}
\frac{
[y^v]\bigl(Ry^{a+b}-(-1)^{a+b}R(-1)\bigr)/(y+1)
}{2v+1}.
\end{aligned}
\tag{14.1}
$$


Every denominator retains the actual cutoff $2v+1\le4n-3$.

The next useful lemma is not another core norm identity:

> **Actual first residual-force lemma.**  
> On the subdomain $v_3(j)=4$, compute the complete actual matrix one residual digit beyond the accepted $3^6$ precision, transport it through the established integral eliminations, and determine
> 

$$
> 3^{-6}G_{\rm residual}\pmod3
>
$$


> together with the corresponding endpoint data. Retain the full factorial term and the endpoint-subtracted arctangent force in (14.1).

If the resulting block is nonsingular, its inverse and endpoint contraction can be evaluated at that level. If it is singular, the calculation must identify its radical and the endpoint’s component there before attempting another digit.

An extra polynomial digit alone must not be assumed sufficient without auditing the division by the actual denominators $2v+1$. The needed object is the **complete transported matrix digit**.

---

# Part III. Primitive arithmetic, verification, and research status

## 15. Bounded exact arithmetic verification

No automatic execution is requested or performed here.

### 15.1 Minimal prime-$29$ reachability check

The only substantial finite arithmetic inputs to the direct reachability proof are (5.1)–(5.2). They can be independently checked without the auxiliary recurrence pass.

**Inputs**


$$
p=29,\quad a_0=432827,\quad P=682892,\quad b_*=687936.
$$



**Expected exact output**


$$
\operatorname{pow}(3,a_0,29^6)=524783157,
$$




$$
\operatorname{pow}(3,P,29^6)=51631514,
$$




$$
h_0=741,\qquad z=73,\qquad \text{slope}=695,
$$


followed by 100 distinct classes generated by


$$
t=(144d-29r+103)\bmod841.
$$



A compact verification-only calculation is:

```python
p = 29
L, modulus = p**4, p**6
base = pow(3, 432827, modulus)
g = pow(3, 682892, modulus)

assert base == 524783157
assert g == 51631514
assert base == 687936 + L*741
assert g == 1 + L*73
assert (695*144) % 841 == 1

classes = set()
for d in range(25):
    alpha = (11*d + 9) % 29
    if 1 <= alpha <= 14:
        for r in range(29-alpha, 29):
            t = (144*d - 29*r + 103) % 841
            assert (741 + 695*t) % 841 == d + 29*r
            assert pow(3, 432827 + 682892*t, modulus) \
                   == 687936 + L*(d + 29*r)
            classes.add(t)

assert len(classes) == 100
```

This is a bounded small-integer check. Its output verifies the modular inputs and all selected classes; the Lucas proof, not this computation, proves component divisibility for every original $k$.

### 15.2 Jacobi verification

No finite calculation is required for the identities proved in §§10–12. The attached auxiliary checks at $A=9,27,45$ support implementation only.

An optional symbolic check can compare (10.1) with (10.2), or compare (10.3) with (11.1) at a bounded list of odd multiples of $3$. It should include $A=15$ to prevent silently replacing $v_3(4A+3)$ by $1$ under the insufficient hypothesis $3\mid A$.

### 15.3 Research calculation versus verification

The next research calculations require new actual-force reductions:

- at $29$, the complete third norm digit on the populated classes;
- at $3$, the first complete transported residual digit.

A bounded auxiliary table cannot substitute for proving that those reductions retain original higher-digit dependence, exact boundaries, and all forcing terms.

---

## 16. Final gcd and whole evaluated error

### 16.1 Prime-$29$ family

Retain


$$
N_B=d_B[u,v],
$$




$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_B=A_B/g_B,\qquad p_B=H_B/g_B.
$$



For


$$
\delta=v_{29}(D),\qquad\mu=v_{29}(M),
$$


the actual denominator satisfies


$$
\boxed{
v_{29}(q_B)=
\max\{0,\ 2v_{29}(n!)-v_{29}(b!)-1+\delta-\mu\}.
}
\tag{16.1}
$$


The population result does not control the final difference $\delta-\mu$ beyond the alternatives in §7.

All primes remain:


$$
\log q_B
=
\sum_\ell
\max\{0,v_\ell(A_B)-v_\ell(H_B)\}\log\ell.
\tag{16.2}
$$



At the retained fixed-ratio whole-error interface,


$$
\epsilon_n=\frac{p_B}{q_B}-(e+\pi)>0
$$


eventually, and


$$
\log|\epsilon_n|
=
-\left(2+\frac1{2001}\right)n\log(1+\sqrt2)+o(n).
$$


The whole primitive evaluated form is


$$
\boxed{q_B(e+\pi)-p_B=-q_B\epsilon_n.}
\tag{16.3}
$$



The complete exponential residual, logarithmic force, factorial/contact boundary, and actual endpoint remain included. Norm positivity gives norm nonvanishing; any finite mixed valuation retains the original mixed-nonvanishing dependency.

### 16.2 Resonance determinant family

For the other family, retain the separate actual integer pair and its final gcd:


$$
g=\gcd(|A_{\rm det}|,|B_{\rm det}|).
$$


When $B_{\rm det}\ne0$,


$$
q=\frac{|B_{\rm det}|}{g},\qquad
p=-\frac{\operatorname{sgn}(B_{\rm det})A_{\rm det}}g,
$$


and


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_{\rm det})\ell^k}{g}
\det H_{\rm complete}.
}
\tag{16.4}
$$



The base Jacobi norm is not this denominator, and core positivity does not prove actual response nonvanishing or decay of (16.4).

---

## 17. Final research ledger

### New results and proof status

**Established by the direct mathematical audit, with the displayed finite modular identities retained as supplied arithmetic inputs:**

1. The one-digit Lucas construction includes every actual $k$, both endpoints, and all selected eligible $d$.
2. It selects exactly 100 sufficient original exponent classes modulo $841$.
3. These classes give infinitely many same-index instances of
   

$$
D,M\in29^2\mathbb Z_{29},\qquad
   M-(6C_n)^{-1}D\in29^3\mathbb Z_{29}.
$$


4. The construction closes the population gap but does **not** evaluate $D/29^2$.
5. The exact terminal Jacobi norm factorial and complement-digit formulas are valid.
6. The uniform specialization is (12.3); the displayed constant $+9$ specialization belongs to $v_3(j)=4$.

### Exact remaining mathematical bottlenecks

- **At $29$:** evaluate the actual third norm digit, and then, where necessary, the next complete mixed defect. Common residual content alone does not control deeper relative valuation.
- **At $3$:** determine the first actual transported residual-force digit and its endpoint contraction. The available core precision does not determine it.
- **Globally:** control the actual denominator after the final gcd across all primes, on the same indices as a nonzero whole error.

The required irrationality mechanism remains an infinite original sequence satisfying


$$
0<|q(e+\pi)-p|\longrightarrow0
$$


with $p,q\in\mathbb Z$. Neither audited construction establishes that condition.



$$
\boxed{\text{The irrationality or rationality of }e+\pi\text{ remains unresolved.}}
$$


