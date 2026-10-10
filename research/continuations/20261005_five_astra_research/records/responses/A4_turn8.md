> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 turn 8 — arithmetic audits and a first-lift correction

## Summary of conclusions

1. **A3 turn 7’s new scoped exclusion passes**, using its stated inherited normalization and second-kind moment bound. The all-residue scalar transfer, including the potentially exceptional residue $p-1$, can be checked directly from its scalar formulas. The conclusion concerns the **actual reduced denominator**, not a factorial clearer.

2. **A1 turn 7’s factorial–Pascal locality theorem passes.** Its finite-block identities and uniform tail estimate are valid. It supplies no inverse estimate. The relevant asymptotic inversion of the factorial precision is $L_H\sim2H$.

3. **The coordinator’s lower-pole simplification is correct.** On the stated highest-pole class, the highest-pole coefficient in the LOW–LOW block is zero **over $\mathbb Z$, by degree**. Thus $Q\bmod9$ is unnecessary for the first lifted residue matrix.

4. I do **not** obtain the requested exact rank and endpoint cofactor on an infinite class. I obtain instead a new, proved infinite-class singularity theorem from Lucas support. It improves the previous actual-gcd divisor by one power of $3$:
   

$$
\boxed{v_3(g)\ge d+1}
$$


   on an explicit infinite subclass.

5. I identify the next saturated Schur block and the polynomial digits genuinely entering it. A useful additional simplification is that the highest-pole contribution to the divided LOW–HIGH block depends only on
   

$$
\operatorname{lc}(Q)/3\bmod3,
$$


   at one corner—not on arbitrary $Q\bmod9$ coefficients.

No conclusion here decides irrationality of $e+\pi$.

---

## I. Audit of A3 turn 7

### 1. Scalar transfer at every residue

Use A3’s notation


$$
a_j(x)=[z^j](1-z+z^2/2)^x,\qquad
D_j=\sum_{u=0}^j(j)_u.
$$


For every odd prime $p$,


$$
D_j\equiv D_{j\bmod p}\pmod p.
$$


Indeed, terms with $u\ge p$ vanish modulo $p$, and each remaining falling factorial depends only on $j\bmod p$.

Write $x=bp+s$, $0\le s<p$. For $j<p$,


$$
a_j(x)\equiv a_j(s)\pmod p,
$$


by the characteristic-$p$ identity


$$
(1-z+z^2/2)^x
\equiv
(1-z+z^2/2)^s(1-z^p+z^{2p}/2)^b.
$$


The factors $(x)_j$ make all terms with $j>s$ vanish modulo $p$. These observations prove the asserted transfer for $h,u,v,\mathcal A$, and hence for all their displayed polynomial combinations.

The only boundary requiring extra attention is $\mathcal B$, whose sum contains $(x)_{j-1}a_j(x+1)$. Here:

- terms with $j>s+1$ vanish;
- for $s<p-1$, the remaining coefficient indices are below $p$;
- for $s=p-1$, the exceptional possible index is $j=p$, but its factor
  

$$
2x+2-j\equiv0\pmod p
$$


  kills that term.

Thus $\mathcal B$ also transfers at $s=p-1$. Consequently the scalar formula (6) proves


$$
\boxed{\widetilde V_x\equiv\widetilde V_s\pmod p}
$$


at **every** residue.

Direct substitution gives


$$
\widetilde V_0=4,\qquad \widetilde V_1=16.
$$


For example, at $x=1$, the intermediate quantities are


$$
h=0,\quad u=1,\quad v=0,\quad
a=1,\quad b=0,\quad l=-2,
$$




$$
\sigma=2,\quad C=-1,\quad\omega=0,\quad
\mathcal A=3,\quad\mathcal B=10,
$$


giving $2\cdot3+10=16$.

### 2. Whole last-block residue and second-kind separation

The reversal $r=m-j$ gives exactly A3’s normalization


$$
A_{N,m}=\frac{(N!)^4}{2^{N+1}}\mathcal H.
$$


The retained raw multiplier is $N-r+1$, so its last-block formula is


$$
A_{N,m}\equiv
\sum_{r=0}^{s}\binom tr(5/2)^r(s)_r^4
(s-r+1)\widetilde V_{s-r}\pmod p.
$$



For $r>s$, $(N)_r$ contains a multiple of $p$. Since the scalar formulas make $\widetilde V_k$ $p$-integral for odd $p$, those terms vanish. For $r<p$, Lucas gives $\binom mr\equiv\binom tr$.

Using the report’s inherited bound


$$
v_p(\widetilde Q_k)\ge-\lfloor\log_p(k+1)\rfloor,
$$


the complete second-kind contribution satisfies


$$
v_p(E_{N,m})\ge2v_p(N!)-\lfloor\log_p(N+1)\rfloor\ge1
\qquad(N\ge p).
$$


Thus its omission **from the residue**, not from the complete numerator, is justified.

### 3. Actual denominator and simultaneous primes

When $B_p(s,t)\ne0$,


$$
v_p(\mathcal H)=-4v_p(N!),\qquad
v_p(\mathcal J)\ge-2v_p(N!).
$$


For the actual primitive pair


$$
U=L_N\mathcal H,\quad T=L_N\mathcal J,\quad
g=\gcd(|U|,|T|),
$$




$$
P=-\operatorname{sgn}(T)U/g,\qquad q=|T|/g,
$$


one therefore has


$$
v_p(q)=\max\{0,v_p(\mathcal J)-v_p(\mathcal H)\}
\ge2v_p(N!).
$$


One valuation is exact here, so this is not an impermissible subtraction of two lower bounds.

On


$$
N=3^{30a},\qquad m\equiv0\pmod{77},
$$


the three residue conditions are


$$
(N\bmod3)=0,\qquad
(N\bmod7,m\bmod7)=(1,0),
$$




$$
(N\bmod11,m\bmod11)=(1,0).
$$


Their residues are respectively $1,32,32$, all units at the relevant primes. The rounding


$$
m=77\left\lfloor\frac{cN}{77(1+c)}\right\rfloor,\qquad n=N-m
$$


has $m/n\to c$ and $n\to\infty$.

Hence


$$
\log q\ge
\left(\log3+\frac{\log7}{3}+\frac{\log11}{5}\right)N-O(\log N).
$$


A3’s elementary strict comparison


$$
\Gamma(c_0)<\log9<
\log3+\frac{\log7}{3}+\frac{\log11}{5}
$$


is valid. Continuity gives the asserted nonempty subinterval.

**Verdict:** using the already accepted signed analytic theorem, the new scoped exclusion passes. On its eventual nonvanishing domain,


$$
q(e+\pi)-P
=q\,\frac{\mathcal Z}{\mathcal J},
$$


with the **whole** numerator $\mathcal Z$, and


$$
\liminf\frac{\log|q(e+\pi)-P|}{N}>0.
$$


This does not exclude other filtered index families.

---

## II. Audit of A1 turn 7

The actual moment identity follows directly by expanding


$$
(y-1)^s=(t^2-2t)^s
$$


inside the defining integral:


$$
b_s=\sum_{\ell=0}^s
\binom{s}{\ell}(-2)^{s-\ell}\frac{(s+\ell)!}{s!}.
$$


Thus its polynomial $F_\ell(s)$ representation is exact.

Since


$$
F_\ell(s)=\binom{s}{\ell}(s+1)\cdots(s+\ell),
$$




$$
v_3(F_\ell(s))\ge v_3(\ell!).
$$


Terms with $\ell>s$ are identically zero. The claimed uniform factorial tail therefore includes all boundary indices.

For every finite block,


$$
B=PP^T,\qquad P^{-1}JP=J+N.
$$


These are finite identities: neither needs an infinite Pascal matrix or a discarded boundary term. Consequently


$$
P^{-1}(B_{ij}i^uj^v)P^{-T}
=(J+N)^u(J+N^T)^v
$$


has the asserted bandwidth.

The degree bounds for the truncated coupling and Gram sequences then prove A1’s displayed locality bounds. They are valid over $\mathbb Q$ before the independently established integral tail estimate is applied.

**Verdict:** PASS as an entrywise theorem. No inverse decay follows. The precise asymptotic scale is


$$
L_H\sim2H,
$$


which supports, rather than repairs away, the stated obstruction: at factorial endpoint precision the resulting bandwidth is already too large.

---

## III. The first lifted LOW block: correction confirmed

Retain


$$
n=4^j+1,\quad m=(n-1)/2,\quad
h=\lfloor\log_3(4n-3)\rfloor,
$$


on the class


$$
3^h\ge3n-2.
$$


Put


$$
H=3^{h-1},\quad r=(3H-1)/2,\quad
s=2n-2-r,\quad d=m+1-s,
$$


and $r_1=(H-1)/2$.

The endpoint basis is


$$
f_0=1,\qquad f_i=(y+1)y^{i-1}.
$$


Write


$$
C_{ij}(y)=
\frac{Q(y)f_i(y)f_j(y)-Q(-1)f_i(-1)f_j(-1)}{y+1}.
$$



### 1. Exact degree vanishing

The equality $s=0$ would give


$$
3^h=4n-3=4^{j+1}+1,
$$


impossible modulo $3$. Thus $s\ge1$.

For $0\le i,j<d$,


$$
\deg C_{ij}\le n+i+j-1\le n+2d-3=r-s<r.
$$


Therefore


$$
\boxed{[y^r]C_{ij}=0\quad\text{exactly}.}
$$



Also $5H>4n-3$ on this class. Hence $H$ is the only denominator of valuation $h-1$.

Let $u_\ell=\ell/3^h$ and


$$
\bar Q=u(y+1)(y-1)^{n-2}.
$$


For the exact first Schur matrix $S$ defined in A4 turn 7,


$$
\boxed{
\bar S_{ij}
=4\bar u_\ell u\,[y^{r_1}](y-1)^{n-2}f_if_j.
}
$$


The prior assertion that this LOW–LOW residue required $Q\bmod9$ was too general. On this class it does not.

### 2. Monomial matrix and endpoint coordinate

In monomial coordinates the residue matrix, up to the displayed scalar unit, is


$$
\mathsf M_{ij}
=[y^{r_1-i-j}](y-1)^A,\qquad
A=n-2,\quad 0\le i,j<d.
$$


Equivalently,


$$
\mathsf M_{ij}
=(-1)^{A-r_1+i+j}\binom A{r_1-i-j},
$$


with out-of-range coefficients zero.

Reversing rows yields the classical binomial Toeplitz determinant, with


$$
L=r_1-d+1=\frac{3n-2H-3}{2}.
$$


Here $0\le L\le A$, so all factorials in


$$
\prod_{i=0}^{d-1}
\frac{(A+i)!\,i!}{(L+i)!\,(A-L+i)!}
$$


are in their legitimate nonnegative range. This is the classical product, not a new determinant theorem.

The distinguished endpoint coordinate is


$$
\boxed{v_i=(-1)^i.}
$$


Thus the relevant inverse contraction is $v^T\mathsf M^{-1}v$, not $(\mathsf M^{-1})_{00}$. The cofactor comes from the endpoint-zero subspace, equivalently the modified weight $(y+1)^2(y-1)^A$.

---

## IV. New infinite-class singularity and a sharper actual gcd

Define the explicit subclass


$$
\mathcal J_*=
\{j\ge1:3\mid j,\quad 3^{\lfloor\log_3(4n-3)\rfloor}\ge3n-2,\quad n=4^j+1\}.
$$



This class is infinite. The usual density argument applies along $j=3b$, since $\log_3(4^3)$ is irrational; a fixed ratio interval strictly inside $(1/4,1/3)$ supplies infinitely many such indices.

### Theorem

For every $j\in\mathcal J_*$,


$$
\det\bar S=0,\qquad
v_3(A_{\mathrm{endpoint}})\ge d+1,
\qquad
\boxed{v_3(g)\ge d+1.}
$$



### Proof

Since $3\mid j$,


$$
4^j\equiv1\pmod9,
$$


so $9\mid A=n-2$. In characteristic $3$,


$$
(y-1)^A=(y^9-1)^{A/9}.
$$


Consequently


$$
\mathsf M_{ij}=0\quad\text{unless}\quad i+j\equiv r_1\pmod9.
$$



On this subclass $h\ge5$. Thus


$$
r_1\equiv4\pmod9,\qquad d\equiv8\pmod9.
$$


Write $d=9b+8$. Among $0,\ldots,d-1$, residue classes $0,\ldots,7$ have $b+1$ members, whereas residue $8$ has $b$.

Rows in residue class $5$ can couple only to columns in residue class $8$, because $5+8\equiv4\pmod9$. There are $b+1$ such rows but only $b$ possible columns. Therefore the matrix has a nonzero left kernel:


$$
\operatorname{rank}\bar S\le d-1.
$$



The exact first Schur identities remain


$$
A_{\mathrm{endpoint}}=3^d\det E\,\det S,
\qquad
B=\ell Q(-1)\,3^{d-1}\det E\,\operatorname{adj}(S)_{00},
$$


where $\det E$ is a $3$-adic unit. Thus


$$
v_3(A_{\mathrm{endpoint}})\ge d+1.
$$


Also


$$
v_3(B)\ge d-1+h+v_3(Q(-1))\ge d+1.
$$


Taking the actual gcd proves the result. $\square$

This is an infinite theorem, but it is **not** an exact rank theorem. In particular, it neither proves rank $d-1$ nor determines the distinguished cofactor.

---

## V. Which digits enter the next lift?

The following reduces the next computation more substantially than the earlier generic $Q\bmod9$ prescription.

Let $X=T_{LH}/3$, and retain the unit highest-pole block $E=T_{HH}$. Then


$$
S=T_{LL}/3-3XE^{-1}X^T.
$$



### 1. LOW–HIGH highest pole has only one possible coefficient

For $i<d$, $j\in\{d,\ldots,m\}$,


$$
\deg C_{ij}\le n+i+j-1\le n+d+m-2=r.
$$


Equality occurs only at


$$
(i,j)=(d-1,m).
$$


Because $f_i,f_j$ are monic, at that corner


$$
[y^r]C_{d-1,m}=\operatorname{lc}(Q).
$$


Every other LOW–HIGH highest-pole coefficient is exactly zero.

Hence the highest-pole portion of $\bar X$ requires only


$$
\boxed{\operatorname{lc}(Q)/3\bmod3}
$$


at this single corner. The remaining portion of $\bar X$ comes from the $H$-pole and is determined by the primitive ray.

### 2. Exact precision needed for $S\bmod9$

For $h\ge3$, define


$$
\mathcal A_2=
\{a\in\{1,5,7,11\}:a3^{h-2}\le4n-3\},
\qquad r_a=(a3^{h-2}-1)/2.
$$


These are exactly the possible denominators of valuation $h-2$ on this class. Then


$$
\boxed{
S_{ij}\equiv
4u_\ell\left(
[y^{r_1}]C_{ij}
+3\sum_{a\in\mathcal A_2}a^{-1}[y^{r_a}]C_{ij}
\right)
-3(XE^{-1}X^T)_{ij}\pmod9.
}
$$



Therefore the next lift uses:

- $Q\bmod9$ in the $H$-pole LOW–LOW coefficients;
- $Q\bmod3$ at the lower poles;
- the single normalized leading digit $\operatorname{lc}(Q)/3\bmod3$ in $\bar X$;
- only $\bar E^{-1}$ in the cross correction.

No $Q\bmod27$ digit is required for this stage.

### 3. Saturated next Schur block and a relative-valuation criterion

Over $\mathbb Z_3$, choose a unimodular congruence separating a nondegenerate lift of the residue form from its radical:


$$
U^TSU=
\begin{pmatrix}E_1&F\\F^T&D_1\end{pmatrix},
\qquad
\det E_1\in\mathbb Z_3^\times,\quad F,D_1\equiv0\pmod3.
$$


The correctly saturated next block is


$$
W=\frac{D_1-F^TE_1^{-1}F}{3}.
$$


Let $w=U^Te_0=(w_E,w_R)$. Then exactly


$$
(S^{-1})_{00}
=w_E^TE_1^{-1}w_E+
\frac13
\bigl(w_R-F^TE_1^{-1}w_E\bigr)^T
W^{-1}
\bigl(w_R-F^TE_1^{-1}w_E\bigr).
$$



This supplies a concrete relative-valuation criterion:

> If the radical has dimension one, $W$ is a unit, and $\bar w_R\ne0$, then
> 

$$
> v_3((S^{-1})_{00})=-1,
> \qquad
> \boxed{v_3(q)=h+v_3(Q(-1))-2.}
>
$$



The criterion is conditional; its hypotheses have not been proved on an infinite class. It illustrates precisely why residue rank alone is insufficient: the endpoint projection onto the radical must also be retained.

---

## VI. Actual normalization and whole error

For the weighted family, retain without change


$$
g=\gcd(|A_{\mathrm{endpoint}}|,|B|),\qquad
q=\frac{|B|}{g},\qquad
p=-\frac{\operatorname{sgn}(B)A_{\mathrm{endpoint}}}{g}.
$$


The exact local interface is


$$
v_3(q)=
\max\{0,h+v_3(Q(-1))-1+v_3((S^{-1})_{00})\}.
$$


The new lower bounds on common content are **not** subtracted to infer this valuation.

The whole evaluated error remains


$$
\boxed{
q(e+\pi)-p
=\frac{\operatorname{sgn}(B)}g
\bigl(A_{\mathrm{endpoint}}+B(e+\pi)\bigr)
=\frac{\operatorname{sgn}(B)\ell^k}{g}\det H_{\mathrm{complete}}.
}
$$


On the supplied regular domain, $B\ne0$; the accepted distinct-center theorem gives nonzero whole errors except possibly at one index. Nothing above proves their decay.

---

## Closing ledger

### (1) New result and proof status

**Proved:**

- A3 turn 7’s arithmetic and scoped power-of-three exclusion pass, with the stated inherited arithmetic and analytic dependencies.
- A1 turn 7’s finite-block locality theorem passes.
- The first lifted LOW residue is independent of $Q\bmod9$.
- On the explicit infinite subclass $\mathcal J_*$, Lucas support forces that residue singular and gives the stronger actual divisor $3^{d+1}\mid g$.
- The next lift requires the polynomial digits specified in Section V; its LOW–HIGH highest-pole correction has only one possible corner.
- The one-dimensional radical criterion gives a conditional exact relative-denominator law.

**Not proved:** exact infinite-class residue rank/cofactor, an unconditional next-lift valuation law, or irrationality of $e+\pi$.

### (2) Exact remaining bottleneck

Determine the rank and **endpoint projection** of the Lucas-structured binomial residue form, then prove saturation of its next radical block. The polynomial endpoint depth $v_3(Q(-1))$ remains a separate unresolved growing-depth input.

The reported valuation $9$ of the classical product at $n=65$ is not the valuation of the actual $S$.

### (3) Bounded computation request

For the single index


$$
n=65,\quad d=26,\quad A=63,\quad r_1=40,
$$


form over $\mathbb F_3$


$$
\mathsf M_{ij}=[y^{40-i-j}](y-1)^{63},
\qquad v_i=(-1)^i,\qquad0\le i,j<26.
$$



Request:

1. Exact rank and a kernel basis, verified by multiplication.
2. The restriction of $v^T$ to that kernel.
3. The value of $v^T\operatorname{adj}(\mathsf M)v$, or an equivalent certified endpoint-zero minor.
4. A nonsingular minor certifying the reported rank.

This tests the first missing rank/cofactor mechanism without reconstructing $Q_{65}$ or a large rational center. Its output would be finite evidence only, not an infinite-class proof.
