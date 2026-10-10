> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1 research continuation: the logarithm step closes, but the terminal endpoint exposes a new digit obstruction and a genuine precision barrier

## 1. Results and proof status

The coordinator’s application of Bugeaud–Laurent Theorem 3 passes the parameter and constant checks against the theorem statement supplied in the packet. At the usual acceptance of that published theorem, it closes the moving-base logarithm dependency.

Combining it with the retained, already proved quantitative reachability and nested-residue estimates gives an **unconditional core continuation theorem** on an infinite family of original indices:


$$
\epsilon\,r_0^{-(m+b)}p_{m+b}(r_0)
 \equiv \mathcal R_b\pmod{3^{143}},
 \qquad b=0,1,2.
$$


Thus the corrected polar valuations and quotient units are now unconditional on that family.

The terminal analysis below gives four further results.

1. **The genuine monic norm is evaluated exactly**, including its factorial normalization and its unit-bearing relation to an integral Jacobi polynomial.

2. **The full terminal Wronskian is reduced to an explicitly normalized binary quadratic form.** Its three coefficient valuations are
   

$$
1,\quad 4,\quad 8.
$$


   This gives exact Wronskian valuations outside two explicitly identified cancellation bands. It does not assume that endpoint column units equal $1$.

3. **The true monomial-coordinate inverse and endpoint losses are evaluated on an explicitly characterized endpoint-unit branch.** On that branch,
   

$$
\boxed{
   v_3(\mathcal W(-1))=1-2v_3(\kappa_m),\quad
   v_3(\mathscr K_{\rm core})=3-h,\quad
   L=h-2,\quad \mu=2-h.
   }
$$


   Here $\kappa_m$ is the actual leading coefficient of the integral Jacobi normalization defined below. Both proposed $3^6$-transfer inequalities fail for the large indices under consideration.

4. **The endpoint-unit branch itself has an exact ternary-digit characterization.** On the resonant family,
   

$$
J_m(-1)\in\mathbb Z_3^\times
   \quad\Longleftrightarrow\quad
   m=2^{2j-1}
   \text{ has no ternary digit }2\text{ except its units digit}.
$$


   This follows from a small, explicitly proved digit recursion for the entire evaluated polynomial—not from sampling its coefficients. No infinitude assertion about those restricted-digit powers of $2$ is made.

Consequently, the local pole continuation is no longer the bottleneck. The outstanding terminal work is now sharply localized:

- evaluate the endpoint and coefficient contents on the nonunit branches;
- more importantly, use the **actual residual force**, not merely its $3^6$ congruence, to control the actual endpoint response.

No actual primitive-denominator depth, nonzero whole-error decay, or irrationality conclusion follows.

### Verification boundary

I have independently checked the supplied theorem application and the derivations below. I have not downloaded the author-hosted PostScript file or executed an external computation in this session. Thus the primary-source transcription and visual-source provenance are the coordinator’s supplied inputs; I do not claim a second independent visual inspection of the original page.

---

## 2. The moving-base logarithm application is valid

Write $J=j+1$. In the multiplicatively independent case, the supplied Bugeaud–Laurent theorem is applied with


$$
p=3,\qquad \alpha_1=4,\qquad \alpha_2=B,\qquad b_1=J,\qquad b_2=1.
$$


For $B\ge2$, $B\equiv1\pmod3$, and multiplicatively independent $4,B$:

- the field is $\mathbb Q$;
- the residue degree is $f=1$;
- $D=1$;
- both numbers are principal $3$-adic units, so $g=1$;
- $h(4)=\log4$ and $h(B)=\log B$;
- an independent $B$ in this residue class is at least $7$, so
  

$$
\log4,\log B\ge\log3;
$$


- the positive exponents are $J,1$;
- the difference is nonzero, both by independence and by the actual-index positivity already proved.

The displayed theorem therefore gives


$$
v_3(4^J-B)
\le
\frac{36\log4\log B}{(\log3)^4}
\max\left\{
\log\left(\frac{J}{\log B}+\frac1{\log4}\right)
+\log\log3+0.4,\,
10\log3,\,
10
\right\}^{2}.
$$



The coordinator’s deliberately loose simplification is valid. Indeed,


$$
\frac{J}{\log B}+\frac1{\log4}\le J+1,
$$


and the maximum is at most


$$
20(1+\log(J+1)).
$$


Using $1<\log3<2$ and $1<\log4<2$ gives


$$
\boxed{
v_3(4^J-B)
\le
30000(1+\log B)(1+\log(J+1))^2.
}
\tag{2.1}
$$


The constant is uniform in both moving parameters. Replacing $\log(J+1)$ by $\log J$, if desired for the literal earlier formulation of $(P_3)$, only enlarges the absolute constant.

The other cases remain exactly those settled in the retained report:

- $B\not\equiv1\pmod3$: valuation $0$;
- $B=4^d$, $d<J$:
  

$$
v_3(4^J-B)=1+v_3(J-d);
$$


- the finitely many nonpositive original $B$’s have the previously stated bounded valuations;
- throughout the actual finite denominator range,
  

$$
4A+1+4b-2i\ge3A+2+2b>0.
$$



There is therefore no remaining logarithm-theorem dependency in this continuation.

### Consequence, without repeating the reachability proof

Retain the established family with


$$
v_3(4^{j+1}-247)=t\to\infty,\qquad
v_3(j)=4,\qquad
\log(j+1)=O(t),
$$


and all the original real-window conditions.

For the actual later block,


$$
I_b+3^t+1\le u\le\min(m+b,2h-1),
$$


the nested-residue estimate and (2.1) give


$$
v_3(R_{b,u})
\ge 3^t+t-D(1+t)^3
$$


with a fixed effective $D$. Hence, for all sufficiently large $t$,


$$
B_b(A)\in3^{143}\mathbb Z_3.
$$



Together with the retained fixed-part, nonresonant-part and actual-tail bounds, this proves


$$
\boxed{
\epsilon T_b(A)\equiv\mathcal R_b\pmod{3^{143}},
\qquad
v_3(p_{m+b}(r_0))=-(m+b)+V_b-t,
}
\tag{2.2}
$$


where


$$
(V_0,V_1,V_2)=(133,135,134).
$$



In particular, putting


$$
a=a_m,\qquad \mathfrak a=\frac a3,
$$


the retained residue digits now give unconditionally


$$
\boxed{
v_3(a)=1,\qquad \mathfrak a\equiv25\pmod{27}.
}
\tag{2.3}
$$


The second quotient still satisfies


$$
v_3(a_{m+1})=-2,\qquad 9a_{m+1}\equiv5\pmod{27}.
$$



All statements from this point onward refer to this sufficiently large original-index family.

---

## 3. The true Jacobi normalization and monic norm

Use the Jacobi weight


$$
w(x)=x^{-1/2}(1-x)^A,\qquad 0<x<1.
$$


This is the unnormalized weight compatible with the retained scalar


$$
c=(-1)^A3^h/2
$$


and the retained Christoffel denominator


$$
-3c\,a_mh_m.
$$


In particular, the core Gram matrix in the original monomials is


$$
G_{ab}=3c\int_0^1 x^{a+b}(x-r_0)w(x)\,dx,
\qquad 0\le a,b\le m.
\tag{3.1}
$$


No probability normalization of the weight is inserted.

Define


$$
\kappa_s=\frac{(s+A+\tfrac12)_s}{s!},
\qquad
J_s(x)=\kappa_s p_s(x).
$$


An integral-at-$3$ formula is


$$
\boxed{
J_s(x)=
\sum_{k=0}^s
\binom{s+A}{k}
\binom{s-\tfrac12}{s-k}
x^k(x-1)^{s-k}.
}
\tag{3.2}
$$


Every coefficient belongs to $\mathbb Z_3$. These are actual column normalizations; their leading coefficients $\kappa_s$ are not generally units.

Let


$$
h_s=\int_0^1p_s(x)^2w(x)\,dx.
$$


The classical Jacobi norm, with the monic division performed, is


$$
h_s=
\frac{
s!\,\Gamma(s+\tfrac12)\Gamma(s+A+1)\Gamma(s+A+\tfrac12)
}{
(2s+A+\tfrac12)\Gamma(2s+A+\tfrac12)^2
}.
$$



At $2m=A+1$, this becomes the exact rational number


$$
\boxed{
h_m=
\frac{
2^{4A+3}(A+1)!(3A+1)!((2A+1)!)^2
}{
(4A+3)((4A+2)!)^2
}.
}
\tag{3.3}
$$



Writing $s_3(N)$ for the sum of the ternary digits of the nonnegative integer $N$, and using $v_3(A)=5$, Legendre’s formula gives


$$
\boxed{
v_3(h_m)
=s_3(4A)-s_3(2A)-s_3(A)-1.
}
\tag{3.4}
$$


Thus the monic norm does retain global digit information. It is not a fixed valuation determined merely by $A\bmod3^t$.

There is, however, a particularly useful cancellation after retaining the actual leading coefficient.

Set


$$
e_m=v_3(\kappa_m).
$$


Directly from its factorial formula,


$$
\boxed{
e_m=
\frac{s_3(A)+s_3(2A)-s_3(4A)-1}{2}.
}
\tag{3.5}
$$


Consequently


$$
\boxed{
v_3(\kappa_m^2h_m)=-2,
\qquad
v_3(h_m)=-2-2e_m.
}
\tag{3.6}
$$



This cancellation is important: the large monic denominator loss must not be counted again after passing to the integral Jacobi columns.

### The norm unit is retained explicitly

Define the unit


$$
N_m=9\kappa_m^2h_m\in\mathbb Z_3^\times.
\tag{3.7}
$$


For an exact formula, put


$$
U(m)=\frac{\binom{6m}{3m}}{\binom{2m}{m}}.
$$


The factorial valuation identity $v_3((3r)!)=r+v_3(r!)$ shows that $U(m)$ is a $3$-adic unit. Then


$$
\boxed{
N_m=
\frac{
2^{2A+3}(3A+2)
}{
(A+1)((4A+3)/3)\,U(m)
}.
}
\tag{3.8}
$$


This preserves the actual unit; it is not replaced by a generic unit symbol in subsequent exact identities.

In particular,


$$
U(m)\equiv1\pmod3,\qquad N_m\equiv1\pmod3.
\tag{3.9}
$$



---

## 4. The terminal Wronskian as a fully normalized quadratic form

Let


$$
P=p_m,\qquad Q=p_{m+1},\qquad U=p_{m-1}.
$$


The monic recurrence is


$$
Q(x)=(x-\beta)P(x)-\gamma U(x),
\tag{4.1}
$$


where, on $A=2m-1$,


$$
\boxed{
\beta=
\frac{3(2A^2+4A+1)}{(4A+1)(4A+5)},
}
\tag{4.2}
$$




$$
\boxed{
\gamma=
\frac{
3A^2(A+1)(3A+1)
}{
(4A+1)^2(4A-1)(4A+3)
}.
}
\tag{4.3}
$$


Thus


$$
v_3(\beta)=1,\qquad v_3(\gamma)=10.
$$



The ratio of actual leading coefficients is


$$
\frac{\kappa_m}{\kappa_{m-1}}
=
\frac{(4A-1)(4A+1)}{3A(A+1)},
$$


of valuation $-6$. Therefore the correction after integral normalization is not of depth $10$, but of depth $4$:


$$
\boxed{
\rho:=
\gamma\frac{\kappa_m}{\kappa_{m-1}}
=
\frac{A(3A+1)}{(4A+1)(4A+3)},
\qquad v_3(\rho)=4.
}
\tag{4.4}
$$



That is one of the precision losses that would be missed by treating monic and integral columns as interchangeable.

Put


$$
X=J_m(-1),\qquad Y=J_{m-1}(-1),
$$


and define


$$
z=\frac{4A+1}{2},\qquad
e=\frac{(A+1)(3A+1)}{2(4A+1)},\qquad
B=2A+2e,
$$




$$
q_0=-1-\beta,\qquad
k=a(r_0+1)=\mathfrak a(A+74).
$$



For the convention


$$
W(f,g)=f'g-g'f,
$$


the standard Jacobi differentiation relation gives


$$
W(P,U)(-1)
=
-\frac12\left[
(z+1)\gamma\,U(-1)^2
+B\,P(-1)U(-1)
+(z-1)P(-1)^2
\right].
\tag{4.5}
$$



The retained three-polynomial Christoffel correction is


$$
F_m=Q-aP,\qquad
F_{m+1}=p_{m+2}-a_{m+1}Q.
$$


Using the recurrence and its evaluation at $r_0$ gives, exactly,


$$
\mathcal W(-1)
=
Q(-1)^2-aP(-1)Q(-1)+k\,W(Q,P)(-1).
\tag{4.6}
$$


This elimination is an identity involving the full correction; it does not discard $p_{m+2}$ or assume its coefficient is negligible.

Substituting (4.1) and (4.5) yields


$$
\boxed{
\mathcal W(-1)=\kappa_m^{-2}\Phi(X,Y),
}
\tag{4.7}
$$


where


$$
\boxed{
\Phi(X,Y)=C X^2+\rho DXY+\rho^2 E Y^2
}
\tag{4.8}
$$


and


$$
C=q_0^2-aq_0+k-\frac{k\gamma(z-1)}2,
\tag{4.9}
$$




$$
D=a-2q_0-\frac{kB}{2},
\qquad
E=1-\frac{k(z+1)}2.
\tag{4.10}
$$



These formulas retain all coefficient units and all three terms of the correction.

### 4.1 The coefficient valuations are evaluated

Using $A/3^5\equiv1/4$ to the required precision and $\mathfrak a\equiv25\pmod{27}$, one obtains


$$
\boxed{
v_3(C)=1,\qquad v_3(D)=v_3(E)=0,\qquad v_3(\rho)=4.
}
\tag{4.11}
$$


More precisely,


$$
\boxed{
\frac C3\equiv7\pmod9,\quad
\frac{\rho}{3^4}\equiv7\pmod{27},\quad
D\equiv1\pmod{27},\quad
E\equiv4\pmod{27}.
}
\tag{4.12}
$$


Hence the normalized mixed and last coefficients satisfy


$$
\frac{\rho D}{3^4}\equiv7\pmod{27},
\qquad
\frac{\rho^2E}{3^8}\equiv7\pmod{27}.
\tag{4.13}
$$



For example, modulo $27$, the contribution determining $C$ is


$$
\frac{64}{25}+\frac{394}{5}\mathfrak a\equiv21\pmod{27};
$$


the omitted-looking term in (4.9) has in fact been retained and has valuation at least $10$. Thus $C/3\equiv7\pmod9$.

### 4.2 Exact valuation branches

Let


$$
x=v_3(X),\qquad y=v_3(Y).
$$


Both are finite nonnegative integers, since the Jacobi values at $-1$ are nonzero.

The three valuations in (4.8) are


$$
2x+1,\qquad x+y+4,\qquad 2y+8.
$$


Therefore:

- if $x-y\le2$,
  

$$
\boxed{
  v_3(\mathcal W(-1))=2x+1-2e_m;
  }
  \tag{4.14}
$$


- if $x-y\ge5$,
  

$$
\boxed{
  v_3(\mathcal W(-1))=2y+8-2e_m.
  }
  \tag{4.15}
$$



The only possible leading cancellations occur at


$$
\boxed{x-y=3\quad\text{or}\quad x-y=4.}
\tag{4.16}
$$



This is a genuine evaluation beyond a formal Wronskian: all other valuation branches are settled exactly.

For completeness, the two exceptional branches can be described without ambiguity. The discriminant of the quadratic in $X/Y$ is


$$
\rho^2(D^2-4CE).
$$


Since $D$ is a unit and $C\in3\mathbb Z_3$, the expression $D^2-4CE$ has a square root in $\mathbb Q_3$. Thus


$$
\Phi(X,Y)=C(X-r_3Y)(X-r_4Y)
\tag{4.17}
$$


for two actual $3$-adic roots satisfying


$$
v_3(r_3)=3,\qquad v_3(r_4)=4,
$$




$$
r_3/3^3\equiv-1\pmod3,\qquad
r_4/3^4\equiv-1\pmod3.
$$


The remaining cancellations are precisely the corresponding endpoint approximation depths. They are not determined by the polar residue digits.

### 4.3 The core endpoint contraction

Substituting the genuine norm into the retained scalar identity gives


$$
\boxed{
\mathscr K_{\rm core}
=
\frac{2\,3^{2-h}}{\mathfrak a N_m(A+74)^2}\,
\Phi(X,Y).
}
\tag{4.18}
$$


Thus


$$
\boxed{
v_3(\mathscr K_{\rm core})=2-h+v_3(\Phi(X,Y)).
}
\tag{4.19}
$$



In particular, if $X$ is a unit, then the first term in (4.8) is uniquely dominant:


$$
\boxed{
v_3(\mathcal W(-1))=1-2e_m,\qquad
v_3(\mathscr K_{\rm core})=3-h.
}
\tag{4.20}
$$



---

## 5. The true inverse kernel and the actual monomial losses

A scalar endpoint valuation alone does not evaluate the inverse loss. Here the original-coordinate inverse can also be normalized exactly.

Define the integral polynomial


$$
\widehat Q(x)=\kappa_m p_{m+1}(x)
=(x-\beta)J_m(x)-\rho J_{m-1}(x).
\tag{5.1}
$$


Let $\eta=A+71$, and put


$$
\boxed{
Z(x)=
\frac{\widehat Q(x)-aJ_m(x)}{3x-\eta}.
}
\tag{5.2}
$$


This quotient is a polynomial of degree $m$, and belongs to $\mathbb Z_3[x]$.

Indeed, it is a polynomial because the numerator vanishes at $r_0=\eta/3$. The divisor $3x-\eta$ has $3$-adic coefficient content $0$; Gauss’s content identity then proves integrality of the quotient.

The monic Christoffel polynomial is


$$
\frac{p_{m+1}(x)-ap_m(x)}{x-r_0}
=\frac{3Z(x)}{\kappa_m}.
\tag{5.3}
$$



Now define the symmetric integral polynomial


$$
\boxed{
\mathcal E(x,y)=
Z(x)Z(y)
+\mathfrak a\,
\frac{J_m(x)Z(y)-Z(x)J_m(y)}{x-y}.
}
\tag{5.4}
$$


The quotient is polynomial and integral. Its finite degrees are at most $m$ in each variable.

The Christoffel–Darboux identity, with the full three-polynomial correction retained, gives


$$
\boxed{
\sum_{a,b=0}^{m}(G^{-1})_{ab}x^ay^b
=
\frac{2\,3^{2-h}}{\mathfrak a N_m}\,
\mathcal E(x,y).
}
\tag{5.5}
$$



A useful check on both scalar and sign is


$$
\boxed{
\mathcal E(-1,-1)=\frac{\Phi(X,Y)}{(A+74)^2}.
}
\tag{5.6}
$$


Equations (5.5) and (5.6) recover (4.18).

### 5.1 Exact content formulas for the losses

For a nonzero polynomial $F$, write


$$
\operatorname{cont}_3(F)=\min v_3(\text{its coefficients}).
$$


Then the true monomial inverse loss is


$$
\boxed{
L=\max\{0,\ h-2-\operatorname{cont}_3(\mathcal E(x,y))\}.
}
\tag{5.7}
$$


For the actual endpoint vector


$$
v=(1,-1,\ldots,(-1)^m)^T,
$$


the endpoint-column loss is


$$
\boxed{
\mu
=
2-h+\operatorname{cont}_3(\mathcal E(x,-1)).
}
\tag{5.8}
$$


These formulas retain the actual matrix size and the original monomial basis. They are not losses in an artificially integral orthogonal basis.

### 5.2 Exact losses on the endpoint-unit branch

Modulo $3$,


$$
\widehat Q(x)\equiv xJ_m(x),\qquad
Z(x)\equiv xJ_m(x),
$$


and hence


$$
\boxed{
\mathcal E(x,y)\equiv
(xy-1)J_m(x)J_m(y)\pmod3.
}
\tag{5.9}
$$



If $X=J_m(-1)$ is a unit, then $J_m(x)\bmod3$ is nonzero, and


$$
\mathcal E(x,-1)\equiv
(-x-1)J_m(x)X\not\equiv0.
$$


Therefore both polynomial contents in (5.7)–(5.8) are zero. We obtain the true losses


$$
\boxed{
L=h-2,\qquad \mu=2-h.
}
\tag{5.10}
$$



The available transfer tests become


$$
6>h-2,
$$


and


$$
6+2(2-h)>3-h.
$$


They respectively require


$$
h<8,\qquad h<7.
$$


Neither holds on the large resonant family.

Thus, on this completely evaluated endpoint branch, the available $3^6$ precision is decisively insufficient.

---

## 6. A new exact endpoint digit theorem

The condition $J_m(-1)\in\mathbb Z_3^\times$ cannot simply be assumed. It has an exact digit characterization on the current family.

Here is a short derivation that evaluates the **whole endpoint value modulo $3$** without constructing a degree-$m$ polynomial.

For a varying integer $n\ge1$, specialize the Jacobi parameter to $A=2n-1$. Formula (3.2) gives


$$
J_n(-1)
=
(-1)^n[z^n](1+z)^{3n-1}(1+2z)^{n-1/2}.
$$


Over $\mathbb F_3$, set


$$
F(z)=(1+z)^3(1-z),
$$




$$
A_0(z)=(1+z)^{-1}(1-z)^{-1/2},
$$


where the square root has constant term $1$. Then


$$
(-1)^nJ_n(-1)
=[z^n]A_0(z)F(z)^n.
\tag{6.1}
$$


The algebraic series satisfies


$$
A_0(z)=G(z)A_0(z^3),
\qquad
G(z)=(1+z)^2(1-z).
\tag{6.2}
$$



For $d\in\{0,1,2\}$, let


$$
\mathcal C_d\!\left(\sum a_kz^k\right)
=\sum a_{3k+d}z^k.
$$


If


$$
H_S(n)=[z^n]S(z)A_0(z)F(z)^n,
$$


then, for $n=3q+d$,


$$
\boxed{
H_S(3q+d)=H_{\mathcal C_d(SGF^d)}(q).
}
\tag{6.3}
$$


Thus the ternary digits are read from low to high.

Put


$$
U(z)=1+z,\qquad V(z)=(1+z)^2.
$$


The needed polynomial identities are


$$
\mathcal C_2(GF^2)=G,
$$


and the following transition table:


$$
\begin{array}{c|ccc}
S&d=0&d=1&d=2\\ \hline
G&V&G&\text{not needed below}\\
U&U&V&0\\
V&U&2V&0.
\end{array}
\tag{6.4}
$$


Each is an identity in $\mathbb F_3[z]$. For example,


$$
UGF^2=(1+z)^9(1-z)^3
$$


contains only powers divisible by $3$, proving the zero in the $U,d=2$ entry.

### 6.1 The actual resonance fixes the starting state

On the original family,


$$
m=\frac{A+1}{2}
=\frac{247+\epsilon}{8},
\qquad v_3(\epsilon)=t.
$$


Therefore


$$
m\equiv247/8\pmod{3^t}.
$$


The low-to-high ternary digits of $247/8$ are


$$
\boxed{
2,1,1,1,\ \overline{1,0}.
}
\tag{6.5}
$$


For instance, the exact numerator recursion


$$
r_{k+1}=(r_k-8d_k)/3,\qquad
d_k\equiv2r_k\pmod3,\quad d_k\in\{0,1,2\},
$$


starts at $r_0=247$ and reaches the cycle $-1,-3$.

Starting from $S=1$, the first digit $2$ gives $G$, and the next three digits $1$ leave that state unchanged. After the periodic digits:

- for odd $t\ge7$, the state is $2V$;
- for even $t\ge8$, the state is $2U$.

Thereafter, (6.4) shows:

- digits $0$ and $1$ keep the state a nonzero scalar multiple of $U$ or $V$;
- a digit $2$ sends it permanently to $0$;
- at the end, both $U$ and $V$ have constant term $1$.

Since the actual $m=2^{2j-1}$ is even, the sign in (6.1) is $1$. We have proved:

> **Endpoint digit theorem.**  
> On the current original-index resonant family, for $t\ge7$,
> 

$$
> \boxed{
> J_m(-1)\not\equiv0\pmod3
> \quad\Longleftrightarrow\quad
> \text{every ternary digit of }m\text{ beyond the fixed low block is }0\text{ or }1.
> }
>
$$


> Equivalently, because the fixed low block has its only digit $2$ in the units position,
> 

$$
> \boxed{
> J_m(-1)\in\mathbb Z_3^\times
> \quad\Longleftrightarrow\quad
> m=2^{2j-1}\text{ has no ternary digit }2\text{ except its units digit}.
> }
> \tag{6.6}
>
$$



This is an exact theorem about the complete endpoint value modulo $3$. It does **not** establish infinitely many original indices with that digit property.

In particular, the pole-residue data do not imply endpoint units. The endpoint depends on the remaining ternary digits of an actual power of $2$, even after arbitrarily deep local resonance has been imposed.

---

## 7. What fails in the actual-polynomial transfer

The available actual approximation remains


$$
Q_n^{\rm loc}=Q_{\rm core}+3^6R,
$$


with no improvement from the logarithm argument.

The complete functional and finite cutoff remain


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\sum_{2v+1\le4n-3}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1}.
\tag{7.1}
$$


Thus the perturbation is still the complete expression


$$
\begin{aligned}
\Delta_{ad}
={}&-\frac{3^h}{4}
\mathfrak f(Q_n^{\rm loc}y^{a+d})\\
&+3^{h+6}
\sum_{2v+1\le4n-3}
\frac{
[y^v]\bigl(Ry^{a+d}-(-1)^{a+d}R(-1)\bigr)/(y+1)
}{2v+1},
\end{aligned}
\tag{7.2}
$$


for $0\le a,d\le m$, with the retained conclusion


$$
\Delta\in3^6M_{m+1}(\mathbb Z_3).
$$



The factorial force, endpoint subtraction, residual polynomial and finite cutoff cannot be removed.

### 7.1 The precision obstruction is genuine, not merely a failed estimate

On the endpoint-unit branch,


$$
v_3(\mathscr K_{\rm core})=3-h<-6
$$


for the large indices in question.

Consider, solely as a test of what a matrix congruence can imply, the symmetric Hankel perturbation


$$
G^\sharp=G+3^6vv^T,
\qquad v_a=(-1)^a.
$$


It satisfies exactly the same entrywise precision condition. Sherman–Morrison gives


$$
v^T(G^\sharp)^{-1}v
=
\frac{\mathscr K_{\rm core}}{1+3^6\mathscr K_{\rm core}}.
$$


When $v_3(\mathscr K_{\rm core})<-6$,


$$
\boxed{
v_3\!\left(v^T(G^\sharp)^{-1}v\right)=-6,
}
\tag{7.3}
$$


not $3-h$.

This is not asserted to be the actual residual force. It proves something more limited and essential:

> Entrywise congruence modulo $3^6$, even with symmetry and the Hankel pattern preserved, does not determine the actual endpoint valuation in this regime.

A successful transfer therefore needs a new statement about the structured residual in (7.2), or an exact resolvent/Schur-complement calculation involving that residual. A stronger estimate for the already controlled polar block cannot repair this obstruction.

### 7.2 The best actual endpoint $q$-depth statement currently justified

There is no proved nontrivial actual endpoint-denominator depth from the present core calculation.

For the actual complete coefficient pair, whenever $\beta_1\ne0$, the final gcd gives the exact identity


$$
\boxed{
v_3(q)=\max\{0,\ v_3(\beta_1)-v_3(\beta_0)\},
}
\tag{7.4}
$$


with the usual convention if $\beta_0=0$.

The work above does not evaluate the two actual valuations in (7.4), and it does not prove $\beta_1\ne0$. Thus no stronger numerical $q$-depth assertion is justified. In particular, $h-3$, the favorable-branch core endpoint depth, must not be assigned to the actual primitive denominator.

---

## 8. Exact remaining endpoint lemmas

Two distinct obligations should now be kept separate.

### 8.1 Core-only endpoint obligation

For the nonunit branches, determine the quantities


$$
v_3(J_m(-1)),\qquad v_3(J_{m-1}(-1)),
$$


and, in the two exceptional bands,


$$
v_3(X-r_3Y),\qquad v_3(X-r_4Y).
$$


For the inverse losses, determine


$$
\operatorname{cont}_3(\mathcal E(x,y)),
\qquad
\operatorname{cont}_3(\mathcal E(x,-1)).
$$



The modulo-$3$ digit theorem provides a concrete starting point for a higher-precision digit recursion. It does not supply those higher valuations.

### 8.2 Actual-force endpoint obligation

Even complete evaluation of the core quantities will not by itself solve the transfer problem. The necessary follow-on lemma is of the following form:

> **Structured residual endpoint lemma.**  
> For the actual residual $R$, complete force $\mathfrak f$, and exact finite matrix perturbation (7.2), evaluate or sharply control
> 

$$
> v^T(G+\Delta)^{-1}v
>
$$


> through the relevant structured resolvent or Schur complement, without replacing $\Delta$ by an arbitrary matrix of the same entrywise precision.

This statement must also prove the needed actual invertibility and response nonvanishing. The $3^6$ congruence alone cannot do so.

---

## 9. Primitive arithmetic and the whole error

For the complete determinant, retain


$$
\det H_{\rm complete}=\beta_0+\beta_1(e+\pi),
\qquad k=m+1.
$$


With an actual coefficient clearer $\ell^k$,


$$
A_\ell=\ell^k\beta_0,\qquad
B_\ell=\ell^k\beta_1,\qquad
g_\ell=\gcd(|A_\ell|,|B_\ell|).
$$


When $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


The whole evaluated error is


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell^k}{g_\ell}
\det H_{\rm complete}.
}
\tag{9.1}
$$


If $\delta$ is the least actual two-coefficient clearer and


$$
g_*=\gcd(|\delta\beta_0|,|\delta\beta_1|),
$$


then


$$
\frac{\delta}{g_*}=\frac{\ell^k}{g_\ell}.
$$



The actual polynomial multiplier $\lambda_n$ must likewise be restored: it multiplies the matrix and inversely scales its endpoint contraction. Its unit cannot be omitted from exact local values, and its full arithmetic cannot be omitted from the global gcd.

Nothing here replaces the all-prime gcd, proves actual response nonvanishing, or establishes decay and nonvanishing of (9.1).

---

## 10. Bounded exact-arithmetic certificates for inspection

No original-index Jacobi scan is requested. The following small checks certify the new fixed algebra, not an unproved infinite-family claim.

### Certificate A: terminal coefficient normalization

**Inputs**


$$
A_*=\frac{243}{4},\qquad \mathfrak a=25,\qquad a=75,
$$


and the rational formulas (4.2)–(4.4), (4.9)–(4.10).

**Operations**

1. Form all quantities as reduced rational numbers.
2. Extract the exact powers of $3$ from numerator and denominator.
3. Perform the normalization divisions by $3$, $3^4$, and $3^8$ before reducing units modulo $9$ or $27$.

**Expected outputs**


$$
\begin{array}{c|c|c}
\text{quantity}&v_3&\text{normalized residue}\\ \hline
C&1&C/3\equiv7\pmod9\\
\rho&4&\rho/3^4\equiv7\pmod{27}\\
D&0&D\equiv1\pmod{27}\\
E&0&E\equiv4\pmod{27}\\
\rho D&4&\rho D/3^4\equiv7\pmod{27}\\
\rho^2E&8&\rho^2E/3^8\equiv7\pmod{27}.
\end{array}
$$



The proof above explains why these residues transfer to the actual family at the stated precision. The calculation itself only checks these fixed rational inputs.

**Resources:** a few dozen rational operations; integers comfortably below a few thousand bits with straightforward unreduced intermediate arithmetic. A conservative allocation of $1$ MiB is ample.

### Certificate B: endpoint digit identities

**Inputs over $\mathbb F_3$**


$$
F=(1+z)^3(1-z),\quad
G=(1+z)^2(1-z),\quad
U=1+z,\quad
V=(1+z)^2.
$$



**Operations**

Compute


$$
\mathcal C_d(SGF^d)
$$


for the entries explicitly used in (6.4), together with the initial transition from $S=1,d=2$.

**Expected outputs**

Exactly the transition identities in (6.4), the initial output $G$, and the two alternating-depth states


$$
2V\quad(t\ge7\text{ odd}),\qquad
2U\quad(t\ge8\text{ even}).
$$



All polynomial degrees involved are at most $12$. This requires substantially fewer than $10^4$ small-field operations and less than $64$ KiB of storage.

This is an algebraic-identity certificate supporting the digit-recursion proof. It is not a finite sample of powers of $2$, and it does not establish that the restricted-digit branch occurs infinitely often.

---

## 11. Closing ledger

### New unconditional results

- The primary-source Bugeaud–Laurent application closes the moving-base logarithm input.
- The original-domain grouped continuation and corrected polar laws are now unconditional.
- The genuine monic norm is given by (3.3), with valuation (3.4) and exact unit-bearing normalization (3.8).
- The terminal Wronskian has the explicit normalized quadratic form (4.8), with coefficient depths $1,4,8$, exact valuations outside two cancellation bands, and a precise description of those bands.
- The actual-coordinate inverse kernel is (5.5).
- The whole endpoint value modulo $3$ has the exact ternary-digit criterion (6.6).

### Fully evaluated terminal branch

When $J_m(-1)$ is a unit,


$$
v_3(\mathcal W(-1))=1-2e_m,\quad
v_3(\mathscr K_{\rm core})=3-h,\quad
L=h-2,\quad
\mu=2-h.
$$


The $3^6$ transfer tests fail, and the rank-one example proves that entrywise precision alone genuinely cannot determine the endpoint response.

### Exact remaining bottleneck

The unresolved task is no longer logarithmic reachability or the later polar block. It is:

1. higher endpoint valuations and inverse contents on the nonunit digit branches; and
2. an actual-force structured endpoint lemma capable of overcoming the demonstrated $3^6$ precision barrier.

After that, the actual coefficient pair, final all-prime gcd, primitive denominator, and whole nonzero error still require control.

**Overall proof status:** the core continuation is closed and the terminal obstruction is substantially sharpened, but the actual denominator/error argument is not closed. No unconditional proof of rationality or irrationality of $e+\pi$ is obtained.
