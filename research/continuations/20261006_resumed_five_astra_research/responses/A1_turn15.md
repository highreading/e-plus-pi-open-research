> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1 turn15 — A paid modulo-$9$ endpoint module and the carry created at the first zero digit

## Executive conclusion

Two advances can be proved from the supplied sources.

1. **The proposed original-domain density consequence is valid.** On every nonempty, fixed-depth congruence class of the original $j$-domain, the exact real window has positive density. Lagarias’s stated Theorem 1.1, applied with $\lambda=3^{-8}$, removes only a sublinear number of indices whose middle word omits $2$. Consequently, infinitely many eligible original indices—and a relative-density-one subset of the eligible indices in each such class—have
   

$$
a_m\equiv b_m\equiv0\pmod3.
$$


   This is not a primitive-direction theorem.

2. **There is a concrete, bounded-degree modulo-$9$ lift for the actual four unit-branch outputs.** It has seventeen polynomial coordinates over $\mathbb Z/9\mathbb Z$, processes ternary digits least significant first with one-digit lookahead, and has an explicit invariant degree bound. No coefficient-by-coefficient expansion up to $x^m$ is required.

   More specifically, the carry created when the characteristic-three state $R$ or $P$ encounters the absorbing digit $2$ can be evaluated:
   

$$
\boxed{
   R\xrightarrow{\;2\;}\text{new divided carry }(1-u)^2,
   }
$$


   

$$
\boxed{
   P\xrightarrow{\;2\;}\text{new divided carry }
   (1-u)\bigl(1+q(1+u)\bigr),
   }
$$


   in the original seven-dimensional characteristic-three numerator normalization. Here $q\in\mathbb F_3$ is the next, more significant digit. These are **injected carries**; the previously accumulated carry must also be propagated and added.

The full modulo-$9$ prefix–suffix table and the actual primitive endpoint direction on an original infinite family are **not evaluated in this report**. The new transition formulas remove the specific obstruction that the absorbing mod-$3$ state had no defined quotient transition. They do not justify discarding the inherited carry.

The accepted coordinator computation is not repeated.

---

## 1. Scope, sources, and normalization

Retain


$$
j>0,\qquad j\equiv81\pmod{243},\qquad
m=2^{2j-1},\qquad A_{\mathrm{ind}}=2m-1,
$$


and


$$
H_{\mathrm{win}}=3^{h-1},\qquad D=H_{\mathrm{win}}-A_{\mathrm{ind}},
$$




$$
\frac1{2C_{16}}<\frac D{H_{\mathrm{win}}}<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
\tag{1.1}
$$



The accepted characteristic-three theorem supplies


$$
m=(1^{25}M01011112)_3
\quad\Longrightarrow\quad
(a_m,b_m)\equiv(2\eta(M),\eta(M))\pmod3.
\tag{1.2}
$$


The proofs in turn14, rather than the finite coefficient samples alone, establish its every-word scope. The new receipt corroborates exactly the finite checks it lists.

I use different notation for elementary factors and endpoint coefficients:


$$
a(u)=1+u,\qquad b(u)=1-u,\qquad Q(u)=1-u^2=a(u)b(u).
$$



Set $t=1+u$. The characteristic-zero equation gives the **exact**, not merely mod-$3$, parametrization


$$
x=\frac{u(1+u)^3}{1-u},
\qquad \sigma^2=1-u^2,\qquad \sigma(0)=1.
\tag{1.3}
$$


Moreover,


$$
d(t)=1+4u-3u^2,
\qquad
\frac{dx}{x}=\frac{d(t)}{u(1-u)(1+u)}\,du.
\tag{1.4}
$$



The actual outputs therefore satisfy the following exact differential identities:


$$
\begin{array}{c|c}
f&f\,dx/x\\ \hline
\mathcal A&\displaystyle \sigma\frac1{1-u}\frac{du}{u}\\[3pt]
\mathcal B&\displaystyle \sigma\frac{u(1+u)}{(1-u)^2}\frac{du}{u}\\[3pt]
W&\displaystyle \sigma\frac1{1+u}\frac{du}{u}\\[3pt]
S&\displaystyle \sigma\frac{du}{u}.
\end{array}
\tag{1.5}
$$


Here the state identities use the retained normalization


$$
W=\frac{\sigma t^2}{P_t},\qquad S=tW,
\qquad P_t=\frac{t^2d(t)}{2-t}.
$$



An important consequence is that the four polynomial numerators used in turn14 also work **integrally**:


$$
f\,\frac{dx}{x}
=\frac{\sigma H_f(u)}{u\,b(u)^2a(u)^4}\,du,
\tag{1.6}
$$


where


$$
H_{\mathcal A}=ba^4,\quad
H_{\mathcal B}=ua^5,\quad
H_W=b^2a^3,\quad
H_S=b^2a^4.
\tag{1.7}
$$



Thus the lift below concerns the actual coefficient endpoints, not an independently chosen algebraic branch.

---

## 2. Two modulo-$9$ identities

All congruences in this section are formal-series congruences over $\mathbb Z_3$.

### 2.1 The square-root correction

For an integral series $F$,


$$
F(u)^3\equiv F(u^3)\pmod3,
$$


and cubing this congruence gives


$$
F(u)^9\equiv F(u^3)^3\pmod9.
$$


Applying this to $\sigma$, and using $\sigma^2=Q$, yields


$$
\boxed{
\sigma(u)\equiv
\sigma(u^3)\frac{1-u^6}{(1-u^2)^4}\pmod9.
}
\tag{2.1}
$$


Every denominator here has constant term one.

### 2.2 The index-dependent Frobenius correction

From (1.3),


$$
\frac{x(u^3)}{x(u)^3}
=
\frac{(1+u^3)^3(1-u)^3}
{(1-u^3)(1+u)^9}.
$$


Since


$$
(1+u)^9\equiv(1+u^3)^3\pmod9,
$$


we obtain


$$
\frac{x(u^3)}{x(u)^3}
\equiv
\frac{(1-u)^3}{1-u^3}
=
1-\frac{3u(1-u)}{1-u^3}
\equiv1-\frac{3u}{(1-u)^2}\pmod9.
$$


Consequently, for every nonnegative integer $q$,


$$
\boxed{
x(u)^{-3q}
\equiv
x(u^3)^{-q}
\left(1-\frac{3q\,u}{(1-u)^2}\right)\pmod9.
}
\tag{2.2}
$$


Only $q\bmod3$ is needed. This is the source of the one-digit lookahead.

Neither identity divides a zero residue by $3$.

---

## 3. A seventeen-coordinate integral module

For a polynomial $N$, define


$$
\mathcal E_n(N)=
\operatorname{res}_{u=0}
x(u)^{-n}\sigma(u)\frac{N(u)}{Q(u)^8}\frac{du}{u}.
\tag{3.1}
$$



For the four actual outputs, the initial numerators are


$$
\boxed{
\begin{aligned}
N_{\mathcal A}&=b^7a^8,\\
N_{\mathcal B}&=u\,b^6a^9,\\
N_W&=b^8a^7,\\
N_S&=b^8a^8.
\end{aligned}}
\tag{3.2}
$$


Their degrees are at most $16$, and


$$
[x^n]f=\mathcal E_n(N_f).
$$



For a Laurent polynomial $G$, put


$$
\Lambda_0(G)(v)=\sum_k[u^{3k}]G(u)\,v^k.
$$



If $n=3q+r$, $0\le r\le2$, define


$$
\boxed{
\begin{aligned}
\mathcal T_{r,q}(N)(v)
=(1-v^2)^3\Lambda_0\Bigl(
&u^{-r}N(u)a(u)^{6-3r}b(u)^{6+r}\\
&-3q\,u^{1-r}N(u)a(u)^{6-3r}b(u)^{4+r}
\Bigr)\pmod9.
\end{aligned}}
\tag{3.3}
$$



### Theorem 3.1 — Exact paid digit reduction modulo $9$

For every $\deg N\le16$,


$$
\boxed{
\mathcal E_{3q+r}(N)\equiv
\mathcal E_q\bigl(\mathcal T_{r,q}(N)\bigr)\pmod9.
}
\tag{3.4}
$$


The right side depends on $q$ only modulo $3$ in its transition.

#### Proof

Insert (2.1) and (2.2) into (3.1). Before sectioning, the main denominator has exponents


$$
a^{12+3r}b^{12-r},
$$


and the correction has two additional factors of $b$ in the denominator. Both can be padded to $a^{18}b^{18}=Q^{18}$, giving precisely the two Laurent polynomials in (3.3).

Furthermore,


$$
Q(u)^{18}\equiv(1-u^6)^6\pmod9.
$$


All factors in $u^3$ can now be pulled through $\Lambda_0$. The numerator $1-u^6$ from (2.1) reduces the resulting denominator from $(1-v^2)^6$ to $(1-v^2)^5$. Multiplication of the numerator by $(1-v^2)^3$ restores the denominator $Q(v)^8$.

The formal identity


$$
\operatorname{res}G(u^3)F(u)\frac{du}{u}
=
\operatorname{res}G(v)\Lambda_0(F)(v)\frac{dv}{v}
$$


finishes the proof. ∎

### Degree and state bound

The largest exponent in the main Laurent polynomial is


$$
\deg N+12-3r.
$$


The correction has largest exponent $\deg N+11-3r$. The smallest exponents are at least $-2$; no negative multiple of $3$ occurs. Thus the sectioned expressions are polynomials, and


$$
\deg\mathcal T_{r,q}(N)
\le 6+\left\lfloor\frac{\deg N+12-3r}{3}\right\rfloor
\le15
\quad(\deg N\le16).
\tag{3.5}
$$



Therefore


$$
\boxed{
\mathscr N_9=(\mathbb Z/9\mathbb Z)[u]_{\le16}
}
\tag{3.6}
$$


is invariant.

This supplies nine explicit linear maps on seventeen coordinates. Processing an index of ternary length $L$ requires $L$ such transitions, with the next digit supplying $q\bmod3$. The terminal functional is


$$
\boxed{\mathcal E_0(N)=N(0).}
\tag{3.7}
$$



This is an original-index digit compression with a proved bound. It is not a claim that the entire reachable-state graph has been enumerated.

---

## 4. The actual carry at the absorbing digit

### 4.1 Embedding the accepted seven-dimensional module

Define


$$
\iota(H)=b^6a^4H.
\tag{4.1}
$$


Equation (1.6) shows that the initial numerators in (3.2) are exactly $\iota(H_f)$.

Reduction of (3.3) modulo $3$ satisfies


$$
\boxed{
\overline{\mathcal T}_{r}\bigl(\iota(H)\bigr)
=\iota\bigl(\Phi_r(H)\bigr),
}
\tag{4.2}
$$


where $\Phi_r$ is the accepted turn14 transition. This follows either from its differential extraction proof or by the same denominator clearing used above.

Use the integer representatives


$$
R=-1+u-u^3+u^4=-b(1+u^3),
$$




$$
P=1+u-u^2-u^3=a^2b.
\tag{4.3}
$$



Both are annihilated by $\Phi_2$. Hence $\mathcal T_{2,q}(\iota(R))$ and $\mathcal T_{2,q}(\iota(P))$ have coefficients divisible by $3$, making their divided residues modulo $3$ well-defined.

### Theorem 4.1 — Evaluated zero-digit injections

For $q\in\mathbb F_3$,


$$
\boxed{
\frac{\mathcal T_{2,q}(\iota(R))}{3}
\equiv \iota(b^2)\pmod3,
}
\tag{4.4}
$$




$$
\boxed{
\frac{\mathcal T_{2,q}(\iota(P))}{3}
\equiv
\iota\!\left(b(1+qa)\right)\pmod3.
}
\tag{4.5}
$$



#### Proof

Write


$$
C_s(F)(v)=\sum_{k\ge0}[u^{3k+s}]F(u)v^k.
$$


For $r=2$, (3.3) becomes


$$
\mathcal T_{2,q}(\iota(H))
=
Q(v)^3\left(
C_2(b^{14}a^4H)-3q\,C_1(b^{12}a^4H)
\right).
\tag{4.6}
$$



Put $A=1+u^3$, $B=1-u^3$. Modulo $9$,


$$
b^{15}\equiv B^5+3ubB^4,\qquad
a^6\equiv A^2+6uaA.
$$



For $H=P=a^2b$, the main polynomial is $b^{15}a^6$, whence


$$
\frac{C_2(b^{15}a^6)}3
\equiv-b(v)^4a(v)^2+2b(v)^5a(v)
=b(v)^4a(v)\pmod3.
$$


The correction is


$$
C_1(b^{13}a^6)\equiv-b(v)^4a(v)^2\pmod3.
$$


Multiplying by $Q(v)^3$ gives (4.5).

For $H=R=-bA$, the main polynomial is $-b^{15}a^4A$. Using


$$
a^4=Aa+3ua^2,
$$


its divided $C_2$-section is


$$
-2b(v)^5a(v)=b(v)^5a(v)\pmod3.
$$


The correction section vanishes:


$$
C_1(-b^{13}a^4A)\equiv0\pmod3.
$$


Multiplication by $Q(v)^3$ gives (4.4). ∎

### 4.2 The inherited carry cannot be omitted

Suppose the actual state immediately before the first absorbing $2$ is


$$
N\equiv s\,\iota(H)+3Z\pmod9,
\qquad H\in\{R,P\},\quad s\in\{1,-1\}.
$$


Then


$$
\boxed{
\frac{\mathcal T_{2,q}(N)}3
\equiv
s\,\iota(J_{H,q})+\overline{\mathcal T}_2(Z)\pmod3,
}
\tag{4.7}
$$


where


$$
J_{R,q}=b^2,\qquad J_{P,q}=b(1+qa).
$$



This is the requested target-specific carry transition. It explicitly distinguishes:

* the newly evaluated injection;
* the carry accumulated before the zero digit;
* the exact division by $3$, paid by having computed the state modulo $9$.

For example, the already evaluated leading functional


$$
L(H)=h_1-h_5
$$


gives


$$
L(J_{R,q})=1,\qquad L(J_{P,q})=2.
\tag{4.8}
$$


Thus a following block $1^{25}$ sees a nonzero injected contribution in either case, independently of $q$. **The inherited contribution may cancel it.** Equation (4.8) is not a nonvanishing theorem for the actual divided endpoint.

---

## 5. What happens after the first zero

Once the actual state is $3Z\pmod9$, subsequent transitions obey


$$
\mathcal T_{r,q}(3Z)/3
=\overline{\mathcal T}_r(Z)\pmod3.
\tag{5.1}
$$


The lookahead correction disappears at this layer. A zero first layer therefore does not require repeated modulo-$9$ carry injections.

There is also a useful reduction in state size.

### Lemma 5.1 — Two-digit return to the seven-dimensional module

Starting with any divided carry


$$
Z/Q^8,\qquad \deg Z\le16,
$$


two characteristic-three digit transitions put it in the form


$$
H/(b^2a^4),\qquad \deg H\le6.
$$



#### Proof

In characteristic three,


$$
\sigma(u)=\frac{\sigma(u^3)}{Q(u)}.
$$


After a digit $r$, padding denominators to multiples of $3$ gives


$$
\frac{L(v)}{a(v)^{3+r}b(v)^3},
\qquad
L=C_r(Zb^r),\qquad \deg L\le5.
$$


For a second digit $s$, pad the next denominator to


$$
a^{6+3s}b^6.
$$


The sectioned numerator is obtained from


$$
u^{-s}L(u)a(u)^{2-r}b(u)^{2+s}
$$


and has degree at most $3$. The new denominator is $a^{2+s}b^2$. Multiplying the numerator by $a^{2-s}$ gives denominator $a^4b^2$ and degree at most $5$, hence certainly at most $6$. ∎

Thus the higher-layer obstruction is now finite and explicit:

> Compute the inherited seventeen-coordinate carry up to the first $2$; inject (4.4) or (4.5); after two more digits, finish with the accepted seven-dimensional transitions.

The forced leading block provides enough remaining digits for this reduction whenever the first zero occurs in the middle word.

---

## 6. Density in the original domain

This section uses Lagarias’s Theorem 1.1 at the scope quoted in the supplied primary-literature gate: for fixed $\lambda>0$, the number of exponents $k\le X$ for which $\lfloor\lambda2^k\rfloor$ omits ternary digit $2$ is at most $25X^{0.9725}$ for sufficiently large $X$.

### 6.1 Fixed genuine congruences

The powers


$$
m=2^{-1}4^j
$$


parametrize the residue class $m\equiv2\pmod3$. Since $4$ has order $3^{t-1}$ modulo $3^t$, a compatible fixed congruence for $m\bmod3^t$ is a congruence for $j\bmod3^{t-1}$.

Intersecting it with $j\equiv81\pmod{243}$ either gives an empty class or a fixed arithmetic progression. “Genuine” means the latter. In particular, imposing the resonance


$$
m\equiv247/8\pmod{3^t}
$$


at fixed depth must retain this compatibility condition.

This argument does not cover a depth that increases with $j$, or conditions involving unknown contents or directions.

### 6.2 Exact real-window density

Write


$$
\alpha=\log_3 4,\qquad
a_0=\frac1{2C_{16}},\qquad b_0=\frac1{C_{16}}.
$$


Since $\alpha$ is irrational, $j\alpha$ is equidistributed modulo one on every fixed arithmetic progression.

For sufficiently large window indices, put $k=h-1=\lceil j\alpha\rceil$. Then


$$
\frac D{3^k}
=1-3^{\{j\alpha\}-1}+3^{-k}.
\tag{6.1}
$$


The limiting open interval for $\{j\alpha\}$ is


$$
I=
\left(
1+\log_3(1-b_0),\
1+\log_3(1-a_0)
\right),
$$


of positive length


$$
\boxed{
\delta=\log_3\frac{1-a_0}{1-b_0}>0.
}
\tag{6.2}
$$



The final $3^{-k}$ in (6.1) must not be deleted from the actual window. To prove the density statement, squeeze the exact condition between fixed inner and outer enlargements of $I$, then let their endpoint displacement tend to zero. Equidistribution gives density $\delta$ within each progression.

### 6.3 The leading twenty-five ones really follow

Because


$$
C_{16}>3^{25},
$$


the exact window gives, for sufficiently large $k$,


$$
\frac{1-3^{-25}}2
<
\frac m{3^k}
<
\frac12.
$$


This lies inside the ternary cylinder with first twenty-five digits equal to $1$. Thus the prefix is not an independent probabilistic assumption.

Retaining the suffix $m\equiv851\pmod{6561}$, every sufficiently large eligible index has the decomposition used in (1.2).

### 6.4 Removing omission exceptions

If $M$ contains no $2$, then


$$
\left\lfloor\frac m{3^8}\right\rfloor
=
\left\lfloor3^{-8}2^{2j-1}\right\rfloor
$$


has no ternary digit $2$: its digits are the leading ones followed by $M$.

For $j\le J$, Lagarias’s bound therefore gives at most


$$
25(2J)^{0.9725}
\tag{6.3}
$$


such exceptions for sufficiently large $J$, even before restriction to a congruence class or the real window.

### Theorem 6.1 — Original-family divisibility density

On every nonempty fixed-depth congruence class retaining the original congruence and the suffix, the exact real-window indices with $M$ containing $2$ have the same positive density as all real-window indices in that class. In particular, infinitely many satisfy


$$
\boxed{c_m=\min(v_3(a_m),v_3(b_m))\ge1.}
\tag{6.4}
$$



The alternating $1,0$ low digits of the deep resonance do not prove this theorem; equidistribution and the sublinear omission bound do. Conversely, the theorem does not select a primitive residue or bound $c_m$ above.

---

## 7. Observation loss and the scalar-normalization boundary

A4’s exact observation formula applies to these coefficient endpoints:


$$
a_m=3^{c_m}\bar a,\qquad b_m=3^{c_m}\bar b,
$$




$$
\boxed{
c(V_{m-1})-c_m
=
4+\min\{2,v_3(\bar b-3\bar a)\}.
}
\tag{7.1}
$$



Two consequences are justified now.

* In the digit-$2$-omitting case, $(a_m,b_m)\equiv(2\eta,\eta)$, so $c_m=0$, $\bar b$ is a unit, and
  

$$
\boxed{c(V_{m-1})=4.}
  \tag{7.2}
$$


* On the positive-density divisibility family from Theorem 6.1,
  

$$
\boxed{c(V_{m-1})\ge5.}
  \tag{7.3}
$$



A modulo-$9$ endpoint evaluation can decide whether $c_m=1$ and can then recover the primitive pair modulo $3$. If its second primitive coordinate is a unit, (7.1) gives loss $4$. If that coordinate vanishes, distinguishing loss $5$ from loss $6$ requires the primitive pair modulo $9$, hence endpoints modulo $27$ when $c_m=1$.

More generally, the retained precision bills remain


$$
\text{endpoint precision }3^{r+K},
\qquad
\text{state precision }3^{r+K+6}.
\tag{7.4}
$$



The present normalization has been reconciled with the actual generating-function coefficients through (1.5)–(1.7). It has **not** been reconciled with an integral Jacobi constant pair by an explicit common scalar or change-of-basis identity in the supplied material. In particular, I do not identify


$$
c_m,\qquad \operatorname{cont}_3(J_m),\qquad
\operatorname{cont}_3(J_{m-1})
$$


with one another.

Before transferring a new residue into the scalar root-line comparison, the required bridge must exhibit the exact integral Jacobi normalization, its scalar valuation and unit, and its action on projective directions. The additional hypotheses


$$
r=\operatorname{cont}_3(J_m)=\operatorname{cont}_3(J_{m-1}),\quad
s=h-2-2r,\quad \mathfrak a\equiv25\pmod{27},\quad N_m\in\mathbb Z_3^\times
$$


remain unproved for the density-selected family.

---

## 8. New bounded arithmetic still needed

No accepted modulo-$3$ computation needs to be rerun.

The next calculation is now small, concrete, and different.

### Inputs

1. The four degree-$16$ polynomials (3.2).
2. The nine maps (3.3).
3. The suffix processing digits
   

$$
2,1,1,1,1,0,1,0,
$$


   with the following middle digit providing the final lookahead.
4. The leading block $1^{25}$, whose final lookahead is $0$.
5. The embedding $\iota$ and carry identities (4.4)–(4.7).

### Expected verifiable output

* Three actual modulo-$9$ suffix states per output, indexed by the next digit $0,1,2$.
* The explicit $1^{25}$ output functional on the seventeen-coordinate module.
* The inherited carry polynomials attached to those suffix states.
* Their first-$2$ divided outputs, retaining both the injection and inherited terms.
* For any stated finite middle-word set, the actual four modulo-$9$ outputs and, where the first layer vanishes but the second does not, the primitive endpoint pair modulo $3$.

All polynomial degrees remain at most $16$. Suffix preparation requires only finitely many short-word transitions, not an original-length recurrence. These outputs have **not** been computed here; no unreported residue is used as a premise.

A particularly useful follow-on lemma is:

> **Inherited-carry observable lemma.** Determine the image of the actual suffix carries under the first-$2$ transition and the remaining prefix–middle functional. Prove either a surviving divided endpoint direction on an explicitly realizable original subfamily, or the exact cancellation condition that forces a third endpoint digit.

The new injection formulas make this a specified finite-module problem rather than a request to divide the absorbing zero state.

---

## 9. Complete finite producers and whole-error obligations

Nothing above changes the original finite spaces


$$
0\le v\le2n-2,\qquad
U_u=x^u\ (0\le u<D),\qquad
z_i=x^Dy^i\ (0\le i<\nu),
$$




$$
Y_b=y^b\ (d\le b\le m),\qquad
d=\frac{3D}{2}-1,\qquad \nu=\frac D2-1.
$$



Both corrected columns remain


$$
\widehat Z^{\,\mathrm{act}}
=\widehat Z^{\,c}-3^6WE_{\mathrm{act}}^{-1}T_R,
$$


with


$$
S_{\mathrm{act}}-S_c
=3^6K_Z-3^{12}T_R^TE_{\mathrm{act}}^{-1}T_R,
$$




$$
Q_{\mathrm{act}}=Q_c+3^6R_{\mathrm{prod}},
\qquad
R_{\mathrm{prod}}=R_{25}+3^{25}\Delta_{25}.
$$



The full pole pair, both leading extractions, every permitted lower pole, factorial forcing, LOW subtraction, all correction layers and unpaired boundary contributions remain required. The terminal return is still


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


No moment beyond $D-4$ is added, and $\omega_{\nu-1}$ is retained.

After all row contents, the actual multiplier and least actual clearer,


$$
A_\ell=\ell_{\mathrm{clr}}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\mathrm{clr}}^{m+1}\beta_1,
\qquad
g_\ell=\gcd(|A_\ell|,|B_\ell|)
$$


still use the gcd over **all primes**. For $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
$$


and


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\mathrm{clr}}^{m+1}}{g_\ell}
\det H_{\mathrm{complete}}.
}
$$



Likewise, the second producer retains


$$
A_B=N_{B,1}^T\Omega N_{B,1},\quad
H_B=N_{B,1}^T\Omega N_{B,2},\quad
g_B=\gcd(A_B,|H_B|),
$$




$$
q_n=A_B/g_B,\qquad p_n=H_B/g_B,\qquad
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
$$



Neither actual primitive denominator nor either whole same-index error is evaluated by the local endpoint module.

---

## 10. Proof status and conclusion

| Statement | Status |
|---|---|
| Accepted characteristic-three seven-dimensional table and five-state quotient | Reused; accepted finite corroboration not repeated |
| Exact integral output differentials (1.5)–(1.7) | Proved here |
| Modulo-$9$ square-root and index corrections | Proved here |
| Seventeen-coordinate, degree-bounded modulo-$9$ module | Proved here |
| Original-index logarithmic digit count for fixed modulo-$9$ precision | Proved here |
| First-$2$ injections from $R,P$ | Explicitly evaluated here |
| Propagation of inherited carry | Explicit transition proved; actual suffix carries not evaluated |
| Return of divided carry to seven dimensions after two digits | Proved here |
| Positive-density original-window divisibility family | Proved using the stated Lagarias theorem |
| Primitive direction on that family | Open |
| Jacobi/scalar normalization bridge | Not supplied; no transfer asserted |
| Complete producers, final all-prime gcds and whole errors | Unresolved |

The principal new local result is


$$
\boxed{
\begin{aligned}
\mathcal T_{2,q}(\iota(R))/3&\equiv\iota((1-u)^2),\\
\mathcal T_{2,q}(\iota(P))/3&\equiv
\iota((1-u)(1+q(1+u)))
\end{aligned}
\pmod3,
}
$$


together with the explicit inherited-carry term in (4.7).

The exact remaining local bottleneck is **not** generic prime-power automaticity and **not** the classical full-digit omission conjecture. It is the observable image of the actual inherited suffix carry, followed by primitive-direction control on a realizable original family and the exact Jacobi normalization bridge.

The global bottleneck remains control of the actual all-prime primitive denominator against the **whole nonzero same-index error** on an infinite original sequence.



$$
\boxed{\text{The irrationality or rationality of }e+\pi\text{ remains unresolved.}}
$$


