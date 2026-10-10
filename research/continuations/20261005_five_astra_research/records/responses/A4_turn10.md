> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 — bounded-rounding audit, finite saturation, and an infinite residue-block reduction

## Summary

- **A3’s bounded-rounding theorem at $c_0$ passes**, with the inherited analytic and arithmetic dependencies specified below. Its Gaussian constant and sign are correct. It does not establish nonvanishing for arbitrary approaches to zeros of the transition profile.
- **The $n=65$ scalar is a unit.** The supplied all-pole assembly has the correct precision, signs, and saturation divisions. Direct multiplication in the displayed $W\bmod9$ verifies the decisive scalar. With the supplied intermediate matrix receipt, the finite conclusions are
  

$$
v_3(A)=35,\qquad v_3(B)=97,\qquad v_3(g)=35,\qquad v_3(q)=62.
$$


- I do **not** obtain an infinite actual-center saturation law. I obtain instead an exact infinite-class reduction of the **first actual residue rank and endpoint projection** to three substantially smaller binomial matrices. It also gives a corresponding lower bound for the actual distinguished cofactor and final gcd. Unlike using an integer binomial representative as a lift, this result uses that representative only where it is valid: modulo $3$.

The remaining obstruction is the actual higher-digit radical form, not the now-resolved polynomial endpoint.

---

## 1. Audit of A3 turn 9

### 1.1 Gaussian constant and sign

Retain A3’s notation


$$
h=5-r,\qquad c_0=h/r,\qquad
a=\frac1{r^2}+\frac{c_0}{h^2}=\frac5{r^2h}>0.
$$


For $m=c_0n+\beta$, $|\beta|\le B$, and $s=x/\sqrt n$, the exact endpoint normalization is


$$
T^n(5+T)^m
=(-1)^nr^nh^m
e^{n(\phi(-r+s)-\phi(-r))}
(1+s/h)^\beta .
$$


Thus bounded rounding changes the first correction, not the endpoint multiplier $r^nh^m$.

The leading contribution comes from $f_3(s)=AKs^{1/2}+O(s^{3/2})$, with


$$
A=-2\sqrt2(1+\sqrt2)<0,\qquad K>0.
$$


Its Gaussian integral is


$$
\begin{aligned}
I_0
&=\int_0^\infty x^{1/2}
(3a^2x-a^3x^3)e^{-ax^2/2}\,dx\\
&=\left(3a^2-\frac52a^2\right)
\int_0^\infty x^{3/2}e^{-ax^2/2}\,dx\\
&=2^{-3/4}a^{3/4}\Gamma(5/4)>0.
\end{aligned}
$$


Both $(-r)^3$ and $A$ are negative. Consequently


$$
C_0=(-r)^3AKI_0>0,
$$


and the numerator sign is indeed $(-1)^n$, not $(-1)^{n+1}$.

### 1.2 All local remainder orders

For a density $s^\alpha$, the leading $\ell$-th Euler derivative has scale


$$
n^{\ell/2-(\alpha+1)/2}.
$$


This gives the respective scales


$$
n^{3/4},\quad n^{1/4},\quad n^{1/4},
\quad n^{-1/4},\quad n^{-3/4}
$$


for the leading $f_3,f_4,f_2,f_1,f_0$ contributions.

The following each lose at least $n^{-1/2}$ relative to the $f_3$ main term:

1. replacing $T^3$ by $(-r)^3$;
2. the lower ordinary derivatives in $D^3$;
3. replacing the leading $s^{1/2}$ density by its $O(s^{3/2})$ remainder;
4. the cubic phase correction;
5. the bounded-rounding factor.

The fixed-neighborhood estimate


$$
\phi(-r+s)-\phi(-r)\le-\kappa s^2
$$


allows these Taylor remainders, after differentiation through order four, to be integrated against a polynomial times a Gaussian. This justifies the claimed absolute remainder


$$
O_B(n^{1/4}r^nh^m).
$$



### 1.3 Global and exponential terms

On the negative branch,


$$
\frac{d^2}{dT^2}\bigl(\log(-T)+c_0\log(5+T)\bigr)<0.
$$


The endpoint stationary point is therefore the unique negative-branch maximum. This establishes the negative off-endpoint gap directly.

The positive-support gap uses the previously audited support and phase comparison; it is not a consequence merely of the local density expansion.

The supplied **whole** exponential estimate gives


$$
\log|\mathcal Z^{\rm exp}_{n,m}|
\le -n\log n+O_B(n),
$$


whereas $\log(r^nh^m)=O_B(n)$. Hence the complete correction is negligible; no individual exponential deficit needs to be dropped.

Thus


$$
\boxed{
\mathcal Z_{n,m}
=(-1)^nC_0n^{3/4}r^nh^m
\bigl(1+O_B(n^{-1/2})\bigr)
}
$$


passes, uniformly for integer $n\to\infty$, $m\ge0$, $|m-c_0n|\le B$.

### 1.4 Exact dependencies and scope

The audit uses these inherited inputs:

- the exact five-measure representation;
- the actual total density expansions and their analytic remainders;
- finite total variations and the support description;
- the positive-support phase gap;
- the bound for the entire exponential correction;
- for the primitive-error sign, the actual denominator-transform sign $\mathcal J<0$;
- for the primorial exclusion, the denominator lower bound for the **same reduced pair**.

With


$$
U=L_N\mathcal H,\quad V=L_N\mathcal J,\quad
g=\gcd(|U|,|V|),\quad
P=-\operatorname{sgn}(V)U/g,\quad q=|V|/g,
$$


the identity is


$$
q(e+\pi)-P=q\frac{\mathcal Z}{\mathcal J}.
$$


Its eventual sign is therefore $(-1)^{n+1}$, and it is nonzero on the stated bounded-rounding domain.

No extension to arbitrary approaching orders follows: near a zero of $\Psi$, lattice spacing and the first omitted asymptotic term have the same scale.

---

## 2. The $n=65$ all-pole and saturation audit

### 2.1 Pole completeness

Here the largest possible odd denominator is $257$, and the highest $3$-power is $243$.

For the first LOW Schur matrix modulo $27$, after its initial division by $3$, precisely these pole levels can survive:


$$
81;\qquad 27,135,189;\qquad
9a,\quad a\in\{1,5,7,11,13,17,19,23,25\}.
$$


The $243$-pole is absent from LOW–LOW by exact degree. In LOW–HIGH it contributes only at $(25,32)$, where division by $3$ exposes


$$
\operatorname{lc}(Q^{\rm loc})/3=1.
$$



The code retains:

- $Q^{\rm loc}\bmod27$ at the $81$-pole;
- $Q^{\rm loc}\bmod9$ at the $27$-poles;
- $Q^{\rm loc}\bmod3$ at the $9$-poles;
- $X,E\bmod9$ in the correction $-3XE^{-1}X^T$.

These precisions are sufficient and correctly aligned. The factorial part has at least depth $5$ before the LOW division, so it vanishes at the requested precision. The endpoint subtraction is also much deeper than required.

Thus the assembly formula and its negative Schur-correction sign pass. This uses the previously audited finite polynomial congruence


$$
Q^{\rm loc}=3P_{65}
\equiv(y+1)(y-1)^{63}(3y+1)\pmod{27}.
$$



### 2.2 First and second saturation boundaries

The first LOW residue has rank $18$ and dimension $26$. The displayed rank certificate and eight independent kernel vectors establish this without inferring rank from a determinant valuation.

The leading $18$-coordinate block is a unit block. Eliminating it gives a block divisible by $3$; division produces the displayed $8\times8$ matrix $W\bmod9$.

For


$$
k=(1,2,1,2,1,2,0,0)^T,
$$


direct multiplication in the displayed matrix gives


$$
Wk\equiv(3,6,3,3,6,0,6,0)^T\pmod9,
$$


and hence


$$
k^TWk\equiv3+12+3+6+6=30\equiv3\pmod9.
$$


The principal minor on coordinates $1,\ldots,7$ has determinant $2\bmod3$. Thus the residue radical is exactly one-dimensional.

Writing that unit block as $J$, the scalar after its elimination is


$$
3\tau=k^TWk-k^TWCJ^{-1}C^TWk.
$$


Every entry of $C^TWk$ is divisible by $3$, so the correction is divisible by $9$. Therefore


$$
\boxed{\tau\equiv(k^TWk)/3\equiv1\pmod3.}
$$


The last saturation boundary is genuinely a unit boundary.

The endpoint residual has reduction $e_0$, and


$$
e_0^Tk=1.
$$


Thus the deepest scalar pole cannot cancel against the shallower unit-block contributions.

### 2.3 Finite valuations and final gcd

The resulting local congruence decomposition has the valuation pattern


$$
S\sim E_{18}\oplus3J_7\oplus9\tau,
$$


with all three displayed unit factors nonzero. Consequently


$$
v_3(\det S)=7+2=9,\qquad
v_3((S^{-1})_{00})=-2,
$$


and


$$
v_3(\operatorname{adj}(S)_{00})=7.
$$



Using $d=26$, $h=5$, and the established endpoint depth $60$,


$$
v_3(A)=26+9=35,
$$




$$
v_3(B)=5+60+25+7=97.
$$


Therefore


$$
\boxed{v_3(g)=35,\qquad v_3(q)=97-35=62.}
$$



The direct last-scalar arithmetic is independently checked above. Identification of every entry of the $26\times26$ matrix with its all-pole expression remains supported by the supplied finite computation and the audited assembly formula; I have not claimed a separate manual recomputation of all those entries.

This resolves the finite scalar obligation. No deeper $n=65$ scalar is requested.

---

## 3. New infinite-class rank reduction

The following provides an exact, smaller description of the first actual residue—not an assumed lift of it.

### 3.1 Domain and parameters

Use the infinite class


$$
\mathcal J_*=
\left\{
j\ge1:\ 3\mid j,\quad
3^{\lfloor\log_3(4n-3)\rfloor}\ge3n-2,\quad n=4^j+1
\right\}.
$$


Retain


$$
H=3^{h-1},\quad A=n-2,\quad
r_1=(H-1)/2,\quad
d=(3H-3n+4)/2.
$$


Set


$$
t=3^{v_3(A)},\qquad A=tC,\qquad c=(t-1)/2.
$$


By LTE,


$$
t=3^{1+v_3(j)}\le3j.
$$


On this domain $j\ge3$, and


$$
H\ge n-\frac23>3j.
$$


Thus $t\mid H$, and we can write


$$
r_1=tR+c,\qquad d=tb+t-1.
$$



### 3.2 Three small matrices

Over $\mathbb F_3$, define


$$
(H_0)_{uv}=[z^{R-u-v}](z-1)^C,
\qquad 0\le u,v\le b,
$$




$$
(H_1)_{uv}=[z^{R-1-u-v}](z-1)^C,
\qquad 0\le u,v\le b,
$$


and the rectangular matrix


$$
J_{uv}=[z^{R-1-u-v}](z-1)^C,
\qquad 0\le u\le b,\quad0\le v<b.
$$


Out-of-range coefficients are zero.

Write their ranks as $\rho_0,\rho_1,\rho_J$.

### Theorem: exact first-residue rank

For the actual first LOW Schur residue,


$$
\boxed{
\operatorname{rank}\bar S
=(c+1)\rho_0+(c-2)\rho_1+2\rho_J.
}
\tag{1}
$$



#### Proof

The endpoint basis is unimodularly equivalent to monomials. Up to a nonzero scalar, its residue form is


$$
\mathsf M_{ij}=[y^{r_1-i-j}](y-1)^A.
$$


In characteristic $3$,


$$
(y-1)^A=(y^t-1)^C.
$$



Write $i=tu+r$, $j=tv+s$, with $0\le r,s<t$. A matrix entry vanishes unless


$$
r+s\equiv c\pmod t.
$$



For $0\le r\le c$, the paired residue is $s=c-r$, and the corresponding block is $H_0$. There are $c+1$ such residue classes.

For $c<r<t$, the pairing satisfies $r+s=c+t$, and the block is $H_1$, except for the pair


$$
r=c+1,\qquad s=t-1.
$$


Every residue class has $b+1$ coordinates except $t-1$, which has $b$. This exceptional pair therefore contributes


$$
\begin{pmatrix}0&J\\J^T&0\end{pmatrix},
$$


of rank $2\rho_J$.

The remaining $c-2$ residue classes contribute square $H_1$ blocks. A two-class pairing contributes twice the block rank; a self-pairing contributes once. Summing proves (1). ∎

This reduces dimension $d$ to three matrices of dimensions at most $b+1$, approximately $d/t$. Since $t\ge9$ on $\mathcal J_*$, it is at least a ninefold first reduction.

### 3.3 Exact endpoint-projection test

Let


$$
a_s=(1,-1,\ldots,(-1)^{s-1})^T.
$$


In a residue class $i=tu+r$, endpoint evaluation is


$$
(-1)^i=(-1)^r(-1)^u,
$$


because $t$ is odd.

Therefore the endpoint functional annihilates the entire first radical **if and only if**


$$
\boxed{
\begin{aligned}
a_{b+1}&\in\operatorname{im}H_0,\\
a_{b+1}&\in\operatorname{im}H_1,\\
a_{b+1}&\in\operatorname{im}J,\\
a_b&\in\operatorname{im}J^T.
\end{aligned}}
\tag{2}
$$


For example, on the exceptional pair the kernels are
$\ker J^T$ and $\ker J$, and their annihilators are respectively
$\operatorname{im}J$ and $\operatorname{im}J^T$. The square-block assertions follow identically.

These are finite rank tests on explicit coefficient matrices, not unresolved inverse contractions. They retain the actual endpoint coordinate.

---

## 4. Consequences for the actual cofactor and gcd

Define the exactly determined residue nullity


$$
\nu=d-(c+1)\rho_0-(c-2)\rho_1-2\rho_J.
$$


The rectangular exceptional pair already ensures $\nu\ge1$.

For any integral lift of a matrix of residue nullity $\nu$, every minor of size $d-1$ is divisible by $3^{\nu-1}$, and its determinant is divisible by $3^\nu$. One way to see this is to eliminate a maximal residue-unit block: the remaining $\nu\times\nu$ block is entrywise divisible by $3$. Equivalently, at least $\nu$ Smith factors are nonunits.

Applied to the **actual** $S$,


$$
\boxed{
v_3(\det S)\ge\nu,\qquad
v_3(\operatorname{adj}(S)_{00})\ge\nu-1.
}
\tag{3}
$$


Consequently


$$
v_3(A)\ge d+\nu,
$$


and, using the established polynomial endpoint law,


$$
v_3(B)\ge h+2v_3((n-1)!)+d+\nu-2.
$$


The latter bound exceeds $d+\nu$ on the stated domain. Thus


$$
\boxed{v_3(g)\ge d+\nu.}
\tag{4}
$$



This sharpens the earlier $d+1$ gcd bound whenever the explicit smaller matrices certify $\nu>1$. It also supplies a uniform distinguished-cofactor lower bound, with no assumption on the higher polynomial digits.

It does **not** justify subtracting these lower bounds to obtain $v_3(q)$.

---

## 5. Why this does not yet give infinite saturation

The new decomposition is exact modulo $3$. After eliminating its unit blocks, however, the divided radical matrix receives three inseparable contributions:

1. the next digit of the actual $Q^{\rm loc}$;
2. the next pole levels;
3. the actual unit-block Schur correction.

Only the first residue enjoys the simple Frobenius block decomposition above. Applying that decomposition to an integer binomial representative at the next level would silently replace the actual matrix.

A1’s explicit digit sums provide a legitimate route to the first contribution. They do not yet prove that the combined radical form has a uniform rank, a surviving endpoint projection, or a bounded final scalar depth on an infinite subclass.

In particular, the finite pattern


$$
18\ \longrightarrow\ 7\ \longrightarrow\ 1
$$


at $n=65$ is not a recurrence in $j$.

---

## 6. Actual primitive pair, whole error, and nonvanishing

For the weighted construction the normalization remains


$$
g=\gcd(|A|,|B|),\qquad
q=\frac{|B|}{g},\qquad
p=-\frac{\operatorname{sgn}(B)A}{g}.
$$


The complete evaluated error is


$$
\boxed{
q(e+\pi)-p
=\frac{\operatorname{sgn}(B)}g\bigl(A+B(e+\pi)\bigr)
=\frac{\operatorname{sgn}(B)\ell^k}{g}\det H_{\rm complete},
\qquad k=(n+1)/2.
}
$$


Both periods and the entire rational arctangent part remain present.

On the supplied regular family $n=4^j+1$, the inherited nonvanishing theorem gives $B\ne0$; inherited distinctness gives nonzero whole errors except possibly at one index. The new residue theorem neither strengthens that analytic conclusion nor proves decay of the primitive errors.

## Closing ledger

### (1) New result and proof status

**Audited:** A3’s complete bounded-rounding law, including sign, Gaussian constant, all local remainder orders, and the whole exponential correction, with the listed inherited dependencies.

**Finite obligation resolved:** the displayed $W\bmod9$ gives $\tau=1\bmod3$; with the supplied intermediate assembly receipt,


$$
v_3(A)=35,\quad v_3(B)=97,\quad v_3(g)=35,\quad v_3(q)=62
$$


at $n=65$.

**New infinite-class theorem proved:** equations (1)–(2) reduce the first actual residue rank and endpoint projection to three explicit smaller coefficient matrices. Equations (3)–(4) transfer their exact nullity to the actual distinguished-cofactor and final-gcd lower bounds.

No irrationality or rationality conclusion for $e+\pi$ is obtained.

### (2) Exact remaining bottleneck

Prove a higher-digit saturation and endpoint-projection rule for the **actual** radical forms on an infinite regular subclass, combining A1’s polynomial digits with every surviving pole and Schur correction. The first-residue rank reduction alone does not control


$$
v_3(B)-v_3(A),
$$


which is the quantity needed for the actual reduced denominator.

### (3) Computation request

**None.** No further $n=65$ scalar is needed. The next obligation is an infinite higher-digit identity, not another finite extension of the resolved scalar chain.
