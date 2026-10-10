> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 313 — an all-n 2-adic exclusion for the Item-311 divisor branch

Checked: 2026-08-31 (Beijing time)

## 1. Strict verdict and scope

Let



$$
q_0=q_1=1,\qquad q_s=(4s-2)q_{s-1}+q_{s-2}\quad(s\ge2),
\tag{1.1}
$$



and, for $n\ge2$, put



$$
A=4n-2,\qquad a=q_{n-1},\quad b=q_n,\quad c=q_{n-2},
\tag{1.2}
$$





$$
\kappa=\operatorname{nint}(a^2/b),\qquad
r_{\rm act}=a^2-\kappa b,\qquad R_{\rm act}=|r_{\rm act}|.
\tag{1.3}
$$



This item proves the exact missing implication from Item 311:



$$
\boxed{
\widehat D_k>2cQ_k\quad\Longrightarrow\quad
\widehat D_k\nmid a
}
\qquad(n\ge5,\ 1\le k<n-2).
\tag{1.4}
$$



Combined with Item 311's already proved equivalence, this gives



$$
\boxed{R_{\rm act}\ge \frac{a}{2c}\qquad(n\ge2).}
\tag{1.5}
$$



The conclusion is deliberately scoped.  It eliminates only the
Item-305/Item-311 Legendre-classified multiplier window.  It does **not**
prove



$$
R_{\rm act}\ge \frac a2,
\tag{1.6}
$$



and it does not treat the still-open intermediate window



$$
\frac{a}{2c}\le R_{\rm act}<\frac a2.
\tag{1.7}
$$



Accordingly, the new beta capacity reduction and the booking are both zero.

## 2. Continuant notation and the hypothetical branch

Write



$$
B_s=4s-2,
\qquad
K(\varnothing)=1,
\qquad
K(z_1,\ldots,z_m)=z_mK(z_1,\ldots,z_{m-1})
 +K(z_1,\ldots,z_{m-2}).
\tag{2.1}
$$



Fix $n\ge5$ and $1\le k<n-2$, and set



$$
j=k+1,\qquad V=q_j=Q_k,\qquad U=q_{j+1},
\qquad L=n-j-1=n-k-2.
\tag{2.2}
$$



The appended tail from Item 311 is



$$
C=\widehat D_k=K(B_{j+2},B_{j+3},\ldots,B_n).
\tag{2.3}
$$



Suppose, for a contradiction, that



$$
C\mid a,\qquad C>2cV,
\qquad g=\frac aC\in\mathbb Z_{>0}.
\tag{2.4}
$$



Every $B_s$ is even, and a continuant of even entries is odd exactly
when its word length is even.  Since $a$ is odd and $C\mid a$,



$$
L\equiv0\pmod2.
\tag{2.5}
$$



The case $L=2$ is excluded directly by the size condition.  Here



$$
C=B_{n-1}B_n+1,qquad c=q_{n-2}=U,qquad V=q_{n-3}.
\tag{2.6}
$$



For $n=5$, $C=253<994=2cV$.  For $n\ge6$, put
$x=B_{n-3}=4n-14\ge10$.  Since



$$
U>B_{n-2}V,qquad V>B_{n-3}=x,
\tag{2.7}
$$



one has



$$
2cV=2UV>2(x+4)x^2>(x+12)(x+8)+1=C.
\tag{2.8}
$$



The last strict inequality follows from



$$
2x^3+7x^2-20x-97>0\qquad(x\ge10);
\tag{2.9}
$$



its value at $10$ is $2403$, and its forward difference is
$6x^2+20x-11>0$.  Hence the hypothetical branch has



$$
L\ge4.
\tag{2.10}
$$



## 3. Exact Legendre descent, including the rational endpoint

Define the overlap coordinates



$$
\begin{aligned}
X&=K(B_{j+2},\ldots,B_{n-1}),
&Y&=K(B_{j+2},\ldots,B_{n-2}),\\
Z&=K(B_{j+3},\ldots,B_{n-1}),
&W&=K(B_{j+3},\ldots,B_{n-2}).
\end{aligned}
\tag{3.1}
$$



The exact transfer matrix gives



$$
a=UX+VZ,\qquad c=UY+VW,\qquad C=B_nX+Y.
\tag{3.2}
$$



Set



$$
\eta=B_ng-U.
\tag{3.3}
$$



Using $a=gC$ in (3.2) yields



$$
VZ=gY+\eta X.
\tag{3.4}
$$



There are no sign assumptions hidden here.  Indeed,



$$
\eta C=B_nVZ-UY>0,
\tag{3.5}
$$



because $Z\ge Y$ and



$$
U=B_{j+1}V+q_{j-1}<(B_{j+1}+1)V<B_nV.
\tag{3.6}
$$



Also (3.4), $gY>0$, and $Z<X$ give



$$
0<\eta<V.
\tag{3.7}
$$



The size hypothesis gives



$$
g=\frac aC<\frac{a}{2cV}<\frac{B_n-3}{2V},
\tag{3.8}
$$



because $a/c<B_{n-1}+1=B_n-3$.  Since $2gV$ is even,



$$
2gV\le B_n-4=B_{n-1}.
\tag{3.9}
$$



As $L\ge4$, appending $B_{n-1}$ gives the strict inequality



$$
X>B_{n-1}Y\ge2gVY.
\tag{3.10}
$$



Consequently,



$$
0<\frac ZX-\frac\eta V
=\frac{gY}{VX}<\frac1{2V^2}.
\tag{3.11}
$$



Reduce $\eta/V=\nu/H$ using



$$
d=\gcd(\eta,V),\qquad \eta=d\nu,\qquad V=dH.
\tag{3.12}
$$



Then (3.11) is stronger than $|Z/X-\nu/H|<1/(2H^2)$.
Legendre's theorem therefore makes $\nu/H$ a convergent of the exact
rational continued fraction



$$
\frac ZX=[0;B_{j+2},B_{j+3},\ldots,B_{n-1}].
\tag{3.13}
$$



The endpoint audit is exact:

* $0/1$ is excluded by $\eta>0$;
* the terminal convergent is excluded by the strict positive error in
  (3.11);
* the sole extra proper convergent from the alternate finite expansion is
  also excluded.  If the canonical terminal denominators are $X>X_-$,
  its denominator is $X-X_-$, and its error is
  $1/(X(X-X_-))$.  Legendre's strict inequality would require
  $2(X-X_-)<X$, whereas the last partial quotient
  $B_{n-1}\ge14$ gives $X>2X_-$.

Thus there is a canonical proper prefix of even length $\ell$, with



$$
2\le\ell\le L-2,
\tag{3.14}
$$



such that



$$
H=K(B_{j+2},\ldots,B_{j+\ell+1}),
\qquad
\nu=K(B_{j+3},\ldots,B_{j+\ell+1}).
\tag{3.15}
$$



The parity of $\ell$ follows from the exact Euler determinant and the
positive sign in (3.11).  Define the complementary tail without reusing
the symbol $R_{\rm act}$:



$$
\Theta=K(B_{j+\ell+3},\ldots,B_{n-1}).
\tag{3.16}
$$



The word in (3.16) is allowed to be empty.  Euler's identity is



$$
HZ-\nu X=(-1)^\ell\Theta.
\tag{3.17}
$$



Dividing (3.4) by $d$ shows that the left side is $gY/d>0$.
Therefore $\ell$ is even and



$$
gY=d\Theta.
\tag{3.18}
$$



Together with $a=gC$ and $V=dH$, this gives the exact cross-multiplied
identity



$$
\boxed{aHY=VC\Theta.}
\tag{3.19}
$$



All four continuants $C,H,Y,\Theta$ have even word length and are odd.

## 4. The bridge from even $L$ to $4\mid L$

If every entry of a word is even, induction in the continuant recurrence
gives



$$
K(\text{even word of even length})\equiv1\pmod4.
\tag{4.1}
$$



Also (1.1) gives the exact period-four residue table



$$
q_s\equiv
\begin{cases}
1\pmod8,&s\equiv0,1\pmod4,\\
-1\pmod8,&s\equiv2,3\pmod4.
\end{cases}
\tag{4.2}
$$



Suppose $L\equiv2\pmod4$.  Since $a=q_{j+L}$ and $V=q_j$,
(4.2) gives



$$
aV^{-1}\equiv-1\equiv7\pmod8.
\tag{4.3}
$$



But (3.19) and (4.1) give



$$
aV^{-1}\equiv C\Theta(HY)^{-1}\in\{1,5\}\pmod8,
\tag{4.4}
$$



a contradiction.  Combining this with (2.5) proves that every hypothetical
branch must satisfy



$$
\boxed{4\mid L.}
\tag{4.5}
$$



This is the complete parity bridge.  It uses only the true congruence
(4.1); it does not use the false shortcut that every nonempty even-length
block is $5\pmod8$.

## 5. The all-length transfer-matrix congruence

Put



$$
M(x)=\begin{pmatrix}x&1\\1&0\end{pmatrix},
\qquad
F_L(r)=M(B_r)M(B_{r+1})\cdots M(B_{r+L-1}).
\tag{5.1}
$$



For $4\mid L$, let



$$
\lambda=2^{v_2(L)},\qquad u=L/\lambda\quad(u\text{ odd}),
\tag{5.2}
$$



and



$$
N_r=
\begin{pmatrix}
1&(-1)^{r+1}\\
(-1)^r&-1
\end{pmatrix}.
\tag{5.3}
$$



Then



$$
N_r^2=0
\tag{5.4}
$$



and the exact all-length congruence is



$$
\boxed{F_L(r)\equiv I+L N_r\pmod{4\lambda}.}
\tag{5.5}
$$



Here is a complete induction proof.

For $\lambda=4$, direct multiplication modulo $16$ gives



$$
F_4(r)\equiv
\begin{cases}
\begin{pmatrix}5&12\\4&13\end{pmatrix},&r\text{ even},\\[4pt]
\begin{pmatrix}5&4\\12&13\end{pmatrix},&r\text{ odd},
\end{cases}
=I+4N_r\pmod{16}.
\tag{5.6}
$$



For a power of two $\lambda\ge4$, shifting every index by $\lambda$
adds $4\lambda$ to every coefficient.  With



$$
J=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad E=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\tag{5.7}
$$



multilinearity of the matrix product gives, modulo $8\lambda$,



$$
F_\lambda(r+\lambda)-F_\lambda(r)
\equiv4\lambda
\sum_{i=0}^{\lambda-1}J^iEJ^{\lambda-1-i}.
\tag{5.8}
$$



There are $\lambda/2$ copies of each of $E_{12}$ and $E_{21}$
in the sum.  Since $4\mid\lambda$, both multiplicities are even, so



$$
F_\lambda(r+\lambda)\equiv F_\lambda(r)\pmod{8\lambda}.
\tag{5.9}
$$



If $F_\lambda(r)=I+\lambda N_r+4\lambda E_r\pmod{8\lambda}$,
then (5.4) and (5.9) give



$$
F_{2\lambda}(r)
=F_\lambda(r)F_\lambda(r+\lambda)
\equiv I+2\lambda N_r\pmod{8\lambda}.
\tag{5.10}
$$



This proves (5.5) for every power-of-two length.  Finally, split a length
$L=u\lambda$ word into $u$ blocks of length $\lambda$.
Their starts differ by multiples of $\lambda$, so they have the same
parity and the same coefficients modulo $4\lambda$.  Hence



$$
F_L(r)\equiv(I+\lambda N_r)^u
=I+u\lambda N_r=I+LN_r\pmod{4\lambda},
\tag{5.11}
$$



again using $N_r^2=0$.  This proves (5.5) without a finite fit.

## 6. Two exact valuation lemmas

### 6.1 The beta denominator shift

The recurrence vector satisfies



$$
\binom{q_{j+L}}{q_{j+L-1}}
=F_L(j+1)^T\binom{q_j}{q_{j-1}}.
\tag{6.1}
$$



Using (5.5),



$$
q_{j+L}-q_j
\equiv L\bigl(q_j+(-1)^{j+1}q_{j-1}\bigr)
\pmod{4\lambda}.
\tag{6.2}
$$



The recurrence modulo $4$ gives



$$
q_j+(-1)^{j+1}q_{j-1}\equiv2\pmod4.
\tag{6.3}
$$



Since $L/\lambda$ is odd, (6.2) proves



$$
\boxed{v_2(q_{j+L}-q_j)=v_2(L)+1.}
\tag{6.4}
$$



### 6.2 The four-continuant difference

For an arbitrary start $r$, even $\ell$ with
$2\le\ell\le L-2$, and $4\mid L$, define



$$
\begin{aligned}
C_L&=K(B_r,\ldots,B_{r+L-1}),\\
H_\ell&=K(B_r,\ldots,B_{r+\ell-1}),\\
Y_L&=K(B_r,\ldots,B_{r+L-3}),\\
\Theta_\ell&=K(B_{r+\ell+1},\ldots,B_{r+L-2}).
\end{aligned}
\tag{6.5}
$$



The last word may be empty.  Reducing (5.5) modulo $2\lambda$ gives



$$
F_L(r)\equiv
\begin{pmatrix}1+\lambda&\lambda\\
\lambda&1+\lambda\end{pmatrix}
\pmod{2\lambda}.
\tag{6.6}
$$



Thus $C_L\equiv1+\lambda\pmod{2\lambda}$.  Since



$$
C_L=B_{r+L-1}(F_L(r))_{12}+Y_L
\tag{6.7}
$$



and $B_{r+L-1}$ is even,



$$
Y_L\equiv1+\lambda\pmod{2\lambda}.
\tag{6.8}
$$



Let $A=F_\ell(r)$, $D=F_{L-\ell-2}(r+\ell+1)$,
and let the two omitted one-letter matrices be
$M(B_{r+\ell})$ and $M(B_{r+L-1})$.  From



$$
F_L(r)=A\,M(B_{r+\ell})\,D\,M(B_{r+L-1})
\tag{6.9}
$$



and $\det A=1$, taking the $(1,1)$ entry after inversion gives



$$
\Theta_\ell
=H_\ell(F_L(r))_{22}-A_{21}(F_L(r))_{12}.
\tag{6.10}
$$



Here $H_\ell$ is odd and $A_{21}$ is even.  Therefore



$$
\Theta_\ell\equiv H_\ell+\lambda\pmod{2\lambda}.
\tag{6.11}
$$



Combining (6.6), (6.8), and (6.11),



$$
C_L\Theta_\ell-H_\ell Y_L
\equiv\lambda\pmod{2\lambda}.
\tag{6.12}
$$



Hence



$$
\boxed{
v_2(C_L\Theta_\ell-H_\ell Y_L)=v_2(L).
}
\tag{6.13}
$$



The empty-tail endpoint $\ell=L-2$ is included: then $D=I$ and
$\Theta_\ell=1$.  No negative-index continuant is used.

## 7. Final contradiction and the actual bound

Return to the hypothetical divisor branch.  Section 4 proves $4\mid L$.
Apply (6.4) with $a=q_{j+L}$, $V=q_j$, and apply (6.13) to the four
continuants in (3.19).  Rearranging that identity gives



$$
(a-V)HY=V(C\Theta-HY).
\tag{7.1}
$$



All of $V,H,Y$ are odd.  The left side of (7.1) has 2-adic valuation



$$
v_2(L)+1,
\tag{7.2}
$$



while the right side has valuation



$$
v_2(L).
\tag{7.3}
$$



This is impossible.  Therefore (1.4) is proved for every permitted
$(n,k)$.

Item 311 proved, for $n\ge5$,



$$
R_{\rm act}<\frac a{2c}
\iff
\exists k:\ C\mid a\text{ and }C>2cQ_k.
\tag{7.4}
$$



The right side is now empty, proving (1.5) for $n\ge5$.  The exact bases
are



$$
\begin{array}{c|ccc}
n&a&c&R_{\rm act}\\ \hline
2&1&1&1\\
3&7&1&22\\
4&71&7&36
\end{array}
\tag{7.5}
$$



and each satisfies (1.5).  Thus (1.5) holds for every $n\ge2$.

## 8. Domain, sign, pole, and index audit

There are no analytic functions and no poles in this proof.  Every division
is by a positive integer:

* $C\mid a$ is assumed only inside the contradiction branch, so
  $g=a/C$ is a positive integer;
* $0<\eta<V$, so $d,H,\nu$ in (3.12) are positive;
* $X,V,H,C,Y$ are positive, and the strict approximation in (3.11)
  has no zero denominator;
* all modular divisions occur only by odd integers;
* the canonical finite continued fraction has every partial quotient at
  least $14$, and its terminal and alternate-terminal cases were audited
  explicitly;
* $L=2$ is handled before Legendre; $L\ge4$ makes (3.10) strict;
* $2\le\ell\le L-2$ contains no negative index, and
  $\ell=L-2$ uses $K(\varnothing)=1$.

The proof uses $R_{\rm act}$ only for the centered square remainder and
$\Theta$ only for the complementary continuant, so there is no symbol or
sign collision.

## 9. Strict labels and booking

### PROVED

* The all-length transfer congruence (5.5).
* The denominator-shift valuation (6.4).
* The four-continuant valuation (6.13), including the empty-tail endpoint.
* The all-$n$ divisor exclusion (1.4).
* The weaker actual-seed bound $R_{\rm act}\ge a/(2c)$ for $n\ge2$.

### EXACT FINITE ONLY

* The deterministic replay's declared base residue classes and control rows.
  They replay the algebra but are not used as finite evidence for an
  all-length assertion.

### OPEN

* The centered half-bound $R_{\rm act}\ge a/2$.
* The intermediate region (1.7).
* Any modular-square or Ostrowski bridge outside the Item-305 Legendre
  window.
* Any beta capacity reduction, Route 1, or conclusion about $e+\pi$.

### BOOKING



$$
\boxed{
\text{new beta capacity reduction}=0,
\qquad
\text{new Route-1 rate}=0.
}
\tag{9.1}
$$



No canonical, master, status, or research-log file is edited by this work
package.

## 10. Deterministic replay

From the archive root:

~~~text
python work/item313_beta_divisor_2adic_no_go_certificate.py ^
  --output work/item313_beta_divisor_2adic_no_go_certificate.replay.json
~~~

The checker uses only the Python standard library and exact integer
arithmetic.  It emits no search result and promotes no finite scan.
