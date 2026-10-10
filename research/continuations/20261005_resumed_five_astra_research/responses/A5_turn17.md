> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, Turn 17 — Divided-power adjoints, the finite-translation obstruction, and a bounded replacement test

## Executive conclusion

The suggested divided-power route has an exact algebraic simplification:

> **The interior adjoint contact inverse is a single constant-coefficient divided-power differential operator of degree at most $4(M-1)$ modulo $2^M$. Its coefficients can be computed in $O(M^2)$ residue-ring operations, without enumerating contact words or allocating a vector of length $b$.**

This statement concerns the **contact factor**, not the complete adjoint. The distinction is decisive. The two binomial transforms surrounding that factor act on polynomial generating functions by truncated multiplication and translation. Translation does not respect the truncation ideal. Consequently, a small differential operator does **not** by itself yield a small quotient for the complete adjoint moments.

I prove below:

1. exact polynomial realizations of both transpose binomial transforms;
2. a compressed integral divided-power inverse for the interior contact factor;
3. an explicit finite-endpoint commutator formula;
4. a genuine obstruction to compressing the calculation by ordinary low-degree jets, even modulo $2$.

These results do **not** evaluate an original norm/mixed pair, and do not prove an invariant under


$$
b\longmapsto9^{32}b.
$$


The replacement proposed here is a specific **boundary-aware binomial-product moment module**, with explicit required closure operations and a bounded first closure test. Its closure and practical size remain unproved; it is not represented as a completed feasible scalar algorithm.

Thus this turn advances the operator analysis but **does not complete Assignment A5’s requested original scalar certificate**. In particular, I do not substitute the previously reported initial zeros or mod-$128$ data for such a certificate.

No tools were executed.

---

## 1. Domain, normalization, and scope of reuse

The original family remains exactly


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
$$


Contact coordinates are $0\le i,j<b$, and reconstructed coordinates are $0\le j\le b$.

With


$$
b=128D+81,\qquad n=128C+66,\qquad C=4002D+2532,
$$


the retained coordinate domain is:

- $0\le t<D,\ 0\le\rho<128$;
- $t=D,\ 0\le\rho\le80$;
- the separate endpoint $j=b$.

Use the exact normalization bridge


$$
\mathsf a=2X=\mathcal RA^{-1}f,
\qquad
\mathsf b=4Y=\mathcal RA^{-1}r+W_be_b,
$$


where


$$
W_j=\binom{n+2}{j},\qquad
(Cx)_j=jx_{j-1}-x_j,\qquad
\mathcal R=\operatorname{diag}(W_j)C,
$$


and


$$
r=\frac{h^e+h^F-A(j!)_{0\le j<b}}{b!}.
$$


In particular,


$$
\mathsf a^T\mathsf a=4N,\qquad
\mathsf a^T\mathsf b=8H.
$$



The audited normalized-force truncation and logarithmic budget are reused at their stated scope. Turn 16’s complete adjoint construction remains pending its separate audit. The elementary operator identities proved here do not assume that audit has been completed.

The accepted classical Legendre and second-kind results are not reproved or claimed as new. Neither fast polynomial XGCD nor general prime-power automata supply the missing specialized relative-output theorem.

---

## 2. Exact polynomial forms of the finite binomial transforms

Let


$$
R_M=\mathbb Z/2^M\mathbb Z,
\qquad
V_b=R_M[x]_{<b}.
$$


For a vector $z=(z_0,\ldots,z_{b-1})$, write


$$
Z(x)=\sum_{j=0}^{b-1}z_jx^j.
$$


Let $P_b$ mean coefficient truncation to degrees $<b$.

The matrices are


$$
L_{ij}=\binom ij,\qquad
U_{ij}=\binom n{j-i}
$$


in their respective triangular ranges.

### Proposition 1 — The two transpose transforms

On $V_b$,


$$
\boxed{
U^{-T}:Z(x)\longmapsto P_b\!\left((1+x)^{-n}Z(x)\right),
}
\tag{2.1}
$$


and


$$
\boxed{
L^{-T}:Z(x)\longmapsto Z(x-1).
}
\tag{2.2}
$$



#### Proof

The coefficient of $x^j$ in the right side of (2.1) is


$$
\sum_{i=0}^j\binom{-n}{j-i}z_i,
$$


which is the $j$-th coordinate of $U^{-T}z$.

For (2.2),


$$
Z(x-1)
=\sum_{j=0}^{b-1}z_j
 \sum_{i=0}^j(-1)^{j-i}\binom ji x^i.
$$


Its coefficient of $x^i$ is precisely $(L^{-T}z)_i$. ∎

Thus, even with no contact correction, the complete adjoint contains


$$
\boxed{
Z(x)\longmapsto
\left[
P_b\!\left((1+x)^{-2n}Z(x)\right)
\right]_{x\mapsto x-1}.
}
\tag{2.3}
$$


Here the two truncated multiplications may be combined because multiplication by a power series preserves the ideal $(x^b)$. The final translation may **not** be moved through $P_b$.

This is the first essential distinction between a formal differential simplification and a finite-matrix compression.

---

## 3. A genuinely compressed interior contact inverse

Define the integral divided derivative


$$
\partial^{[s]}x^k=\binom ks x^{k-s}.
$$


This is an endomorphism of $\mathbb Z[x]$; no modular division by $s!$ is involved.

For the lower-triangular contact factor


$$
H_{kj}=\lambda_{k-j}\binom{k}{k-j},
$$


the transpose acts as


$$
\boxed{
H^T=\sum_{s\ge0}\lambda_s\partial^{[s]}
}
\tag{3.1}
$$


on $V_b$.

The complete-symbol filtration gives


$$
v_2(\lambda_s)\ge \left\lceil\frac s4\right\rceil
\quad(s>0),
\qquad \lambda_0=1.
\tag{3.2}
$$


At precision $2^M$, coefficients with $s>4(M-1)$ can therefore be omitted.

### Theorem 2 — Precision-sized divided-power inverse

Set


$$
m=4(M-1).
$$


There are integral coefficients $c_0,\ldots,c_m$, with


$$
c_0=1,\qquad
v_2(c_k)\ge\left\lceil\frac k4\right\rceil,
$$


such that, on every $V_b$,


$$
\boxed{
(H^T)^{-1}\equiv
\sum_{k=0}^{m}c_k\partial^{[k]}
\pmod{2^M}.
}
\tag{3.3}
$$


They are determined recursively by


$$
\boxed{
c_k=-\sum_{s=1}^{k}\binom ks\lambda_s c_{k-s}.
}
\tag{3.4}
$$



#### Proof

The divided derivatives satisfy


$$
\partial^{[s]}\partial^{[t]}
=\binom{s+t}{s}\partial^{[s+t]}.
$$


Hence the coefficient of $\partial^{[k]}$ in the product of (3.1) and (3.3) is


$$
\sum_{s=0}^k\binom ks\lambda_sc_{k-s}.
$$


Equation (3.4) makes this coefficient zero for $k>0$, and the constant coefficient is one.

Inductively, every summand in (3.4) has valuation at least


$$
\left\lceil\frac s4\right\rceil+
\left\lceil\frac{k-s}{4}\right\rceil
\ge \left\lceil\frac k4\right\rceil.
$$


Thus coefficients of order $k>m$ vanish modulo $2^M$.

All operations are integral. Restriction to $V_b$ is valid because divided differentiation lowers degree. ∎

### Complexity and precision

Computing (3.4) requires $O(m^2)=O(M^2)$ additions and multiplications modulo $2^M$, and $O(M)$ stored residues.

There are:

- no factorial divisions;
- no nonunit inversions;
- no contact-word enumeration;
- no loss of working precision.

This is a real compression of the **interior contact inverse**. It is stronger than merely observing that only $M$ offidentity factors survive.

It does not yet compress the vector to which the operator is applied.

---

## 4. Finite endpoints: what differentiating a truncation actually does

Divided differentiation and coefficient truncation do not commute.

### Proposition 3 — Exact endpoint commutator

For a formal power series


$$
F(x)=\sum_{k\ge0}f_kx^k
$$


and $s\ge1$,


$$
\boxed{
P_b\partial^{[s]}F-\partial^{[s]}P_bF
=
\sum_{r=0}^{s-1}
\binom{b+r}{s}f_{b+r}x^{b+r-s}.
}
\tag{4.1}
$$



#### Proof

The terms omitted by $P_bF$ have indices $k\ge b$. After applying $\partial^{[s]}$, precisely those with $b\le k<b+s$ return to degrees $<b$. Writing $k=b+r$ gives (4.1). ∎

Thus a differential operator of degree $m$ creates a correction supported in the last $m$ contact degrees, determined by $m$ exterior coefficients. This is compatible with the bounded endpoint correction in the finite contact factorization.

However, after applying $L^{-T}$, the correction becomes a linear combination of


$$
(x-1)^{b-m},\ldots,(x-1)^{b-1},
$$


which are generally dense in the coefficient basis.

**Bounded boundary rank survives; bounded coordinate support does not.**

A compressed implementation should retain these boundary polynomials symbolically. Expanding them into $b$ coefficients would discard the benefit of the rank bound.

---

## 5. A true obstruction: low-degree jets cannot carry the final translation

The simplest proposed quotient would retain only a precision-sized initial coefficient segment, together with the contact differential operator. That quotient cannot support the actual translation.

### Theorem 4 — Translation does not descend to the jet quotient

For every $d\ge1$, the translation


$$
T_{-1}F(x)=F(x-1)
$$


does not induce an endomorphism of


$$
R_M[x]/(x^d).
$$


The failure occurs already modulo $2$.

#### Proof

The polynomials $0$ and $x^d$ have the same image in the quotient. But


$$
T_{-1}(x^d)=(x-1)^d
$$


has constant coefficient $(-1)^d$, a unit in $R_M$. Its image is therefore nonzero. ∎

A stronger output formulation is useful. For every $k$,


$$
[x^0]\,T_{-1}(x^k)=(-1)^k.
$$


Thus arbitrarily high input coefficients can contribute a unit to the lowest output coefficient. No depth estimate based solely on input degree can remove them.

### Consequence for the proposed closure argument

The following inference is invalid:


$$
\text{small first-force producer}
+\text{small differential contact inverse}
\Longrightarrow
\text{small complete adjoint jet}.
$$



The missing information lies in high-degree coefficients exposed by the finite translation. Even the contact-free operator (2.3) has this issue.

This proves failure of the **ordinary jet quotient**, not impossibility of every compressed moment representation. In particular, it does not rule out a boundary-aware binomial-product module.

---

## 6. The replacement should compress functionals, not translated coefficient rows

The right object is not the complete polynomial $\mathscr W$ in expanded form. It is the collection of linear functionals needed by the two scalar outputs.

For a coefficient sequence $z_j$, consider finite moments


$$
\mathcal M_{\kappa}(z)
=
\sum_{j=0}^{b-1}\kappa(j)z_j,
$$


with kernels built from:

- $\binom{j}{r}$ and $\binom{n+j}{r}$, for precision-sized $r$;
- the genuine large-index kernels
  

$$
\binom{2n+j-s}{b+t};
$$


- reconstructed weights $W_j$, including the adjacent-coordinate terms;
- symbolic boundary polynomials and their pairings.

The large lower indices $b+t$ must remain.

### Exact adjoint operation for the divided derivatives

For every kernel $\kappa$,


$$
\begin{aligned}
\mathcal M_\kappa(\partial^{[s]}Z)
&=\sum_{j=0}^{b-1-s}
 \kappa(j)\binom{j+s}{s}z_{j+s}\\
&=\sum_{k=s}^{b-1}
 \binom ks\kappa(k-s)z_k.
\end{aligned}
$$


Therefore the kernel transfer is


$$
\boxed{
\kappa(k)\longmapsto
\mathbf1_{k\ge s}\binom ks\kappa(k-s).
}
\tag{6.1}
$$



For the compressed inverse, sum (6.1) with weights $c_s$. This operation has only $O(M)$ shift labels.

### Exact operations still needing compression

The two binomial transforms induce


$$
\boxed{
\kappa(i)\longmapsto
\sum_{j=i}^{b-1}
\kappa(j)\binom{-n}{j-i}
}
\tag{6.2}
$$


and


$$
\boxed{
\kappa(j)\longmapsto
\sum_{i=0}^{j}
\kappa(i)(-1)^{j-i}\binom ji.
}
\tag{6.3}
$$



These formulas specify the missing closure obligation precisely. Writing them down is not an algorithm: their displayed summation lengths are still original-length.

### Concrete follow-on lemma

A sufficient next result is:

> **Boundary-aware binomial-product moment closure.**  
> Construct an integral kernel module containing the actual norm and complete mixed-output kernels, closed under (6.1)–(6.3), multiplication by the actual reconstruction weights, and the endpoint injections in (4.1). Give an explicit basis and transfer matrices whose sizes are feasible at $M=20$, together with a bound for arbitrary $M$.

The module must distinguish:

1. bulk kernels;
2. lower-end evaluation functionals;
3. upper-end binomial-product kernels;
4. the separate reconstructed endpoint $j=b$.

A successful proof must evaluate the finite sums in (6.2)–(6.3), rather than rename them as new basis elements indefinitely.

This replacement is more specific than generic digit-transfer existence. Its feasibility, however, is **not yet established**.

---

## 7. Complete forcing and scalar precision remain unchanged

The normalized exponential force is


$$
r_i^e\equiv
\sum_{\substack{a,t\ge0\\a+v_2(t!)<M}}
\sum_{s=0}^{4a}
\lambda_s^{(a)}
\binom{n+i}{s}
t!\binom{b+t}{t}
\binom{2n+i-s}{b+t}
\pmod{2^M}.
$$


This is not replaced by a bounded-degree polynomial in $i$.

The complete logarithmic part may be omitted only if


$$
M\le K_{\rm norm}
=
1+v_2((n/2)!)-v_2(b!)
-\lfloor\log_2(2n+b-1)\rfloor.
$$


Otherwise $h^F/b!$ remains part of the calculation.

For


$$
q=\mathcal R^T\mathsf a,\qquad w=A^{-T}q,
$$


finite-dimensional duality gives


$$
4N=w^Tf,
\qquad
8H=w^Tr+W_b\mathsf a_b.
$$


In particular, neither the exterior endpoint nor the inhomogeneous third column is removed by the operator simplification.

If


$$
\mathsf a=f_0B_0+f_1B_1,\qquad
\mathsf b=r_0B_0+r_1B_1+B_*,
$$


then $B_*$ is still


$$
B_*=\mathcal RA^{-1}\tau+W_be_b,
$$


with the actual complete finite source.

### Norm cancellation must be paid

Write


$$
d=v_2(\mathsf a^T\mathsf a),\qquad
e=v_2(\mathsf a^T\mathsf b).
$$


For a desired ratio precision $2^s$, a sufficient common raw precision is


$$
M\ge
\max\{s+d+1,\ s+2d+1-e\},
$$


with $M>d,e$.

The assignment’s smallest original case has $\mu=7$, so the baseline raw target is


$$
M\ge2\mu+6=20
$$


before additional norm loss. The operator theorem above works at that precision, but it does not certify $d$, $e$, or the scalar residues.

---

## 8. A safe bounded arithmetic test

The next calculation should test the new operator compression and its endpoint interaction. It should not be described as an original norm calculation.

### Inputs

Use the actual smallest original parameters


$$
b=150094635296999121,\qquad
n=600678730458590482242,
$$


with


$$
M=20,\qquad m=76.
$$



Required inputs are the complete-symbol coefficients


$$
\lambda_0,\ldots,\lambda_{76}\pmod{2^{20}},
$$


computed using the accepted normalized symbol filtration.

No length-$b$ vector is required.

### Calculation A: compressed inverse

1. Compute $c_0,\ldots,c_{76}$ by (3.4).
2. Verify
   

$$
\sum_{s=0}^k\binom ks\lambda_sc_{k-s}
   \equiv\mathbf1_{k=0}\pmod{2^{20}}
$$


   for $0\le k\le152$, setting coefficients beyond $76$ to zero.
3. Verify the depth bounds for $\lambda_k$ and $c_k$.

**Expected output:** all inverse residuals vanish. Terms of order $k\ge77$ vanish by the proved filtration.

### Calculation B: endpoint commutator

Take


$$
F(x)=(1+x)^{-n}.
$$


For $1\le s\le76$, compute the coefficients in


$$
\sum_{r=0}^{s-1}
\binom{b+r}{s}\binom{-n}{b+r}x^{b+r-s}.
$$


The large binomials must be evaluated by a valuation-and-odd-unit algorithm, not by factorial construction.

Independently verify (4.1) coefficientwise on its at most $s$ nonzero positions.

**Expected output:** zero commutator residuals, with all large indices retained.

This uses fewer than $76^2$ endpoint coefficient comparisons. It is a bounded exact operator audit, not a scalar-family theorem.

### Calculation C: first closure gate

Before building any large state system, derive symbolic reductions for (6.2)–(6.3) on:

- the actual low-degree first-force kernels;
- one complete mixed kernel with $s=t=0$;
- one endpoint kernel from Calculation B;
- their products with the actual reconstruction weights.

The required output is a finite list of basis kernels, exact reduction identities, and matrix dimensions. An unevaluated finite sum is not an accepted reduction.

**Stop criterion:** if the basis list grows with $b$, or if closure introduces unrestricted products with an increasing number of factors, record failure rather than allocate a $b$-row array.

No numerical output for these proposed calculations is claimed here.

---

## 9. Final gcd, primitive denominator, and whole error

The operator compression does not alter the final arithmetic.

Retain the least actual two-column clearer $d_B$, the integer Gram pair


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,
\qquad
H_B=N_{B,1}^T\Omega N_{B,2}\ne0,
$$


with nonvanishing reused only at its accepted scope.

The full reduction is


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=\frac{A_B}{g_B},\qquad
p_n=\frac{H_B}{g_B}.
}
$$


Every prime is included. The primitive multiplier remains $d_B^2/g_B$.

Under the retained complete signed-error theorem,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


and


$$
\log|\epsilon_n|
=
-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$


The relevant evaluated expression is the whole quantity


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n,
}
$$


not an isolated force component or an unscaled approximation error.

Irrationality by this route still requires a same-index estimate making this nonzero expression tend to zero. No result above supplies the necessary all-prime primitive-denominator bound.

---

## Conclusion and proof-status ledger

| Statement | Status |
|---|---|
| Exact polynomial realizations of $U^{-T}$ and $L^{-T}$ | Proved |
| $O(M)$-coefficient divided-power inverse of the interior contact factor | Proved |
| Integral arithmetic with no factorial precision loss in that inverse | Proved |
| Exact bounded endpoint commutator | Proved |
| Ordinary low-degree jet quotient supports the complete adjoint | Disproved |
| Boundary-aware binomial-product moment module closes at feasible size | Open |
| Actual original norm/mixed pair at $20$ or more raw bits | Not evaluated |
| Preserved relative-output law under $b\mapsto9^{32}b$ | Not proved |
| Full gcd and whole-error comparison | Open |

The new result is a genuine compression of the **interior adjoint operator**, together with a precise obstruction to promoting it to a complete adjoint-moment quotient by low-degree truncation.

The immediate remaining bottleneck is now explicit: **evaluate and close the two finite binomial-kernel transforms (6.2)–(6.3) on the actual weighted moment channels, including the symbolic upper boundary and the separate endpoint, at norm-sensitive precision.** The bounded calculations above can certify the new operator layer and test the first closure identities, but cannot replace that proof.



$$
\boxed{\text{An unconditional proof or disproof of the irrationality of }e+\pi
\text{ remains unresolved.}}
$$


