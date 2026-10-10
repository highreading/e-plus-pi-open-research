> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## Audit verdict

The beta identity and the geometric inverse are valid. They do **not**, by themselves, produce a fifth-depth kernel of the complete weighted matrix. The precise obstruction is an actual HIGH force: even after geometric cancellation of the linear core, certain HIGH pairings have valuation **exactly $2$** in the full scaled matrix.

Below I give:

* an exact rational-moment formula contracting every pole layer at once;
* a uniform precision estimate, including the polynomial remainder;
* the complete HIGH and LOW correction formula for the proposed columns;
* an explicit family of nonzero HIGH forces.

This is a raw-moment and corrected-lift audit, **not an evaluated fifth-carry theorem**. I reuse the established support law and fourth-carry result.

## 1. Domain, actual form, and normalization

Work on the assigned domain


$$
n=4^j+1,\qquad 81\mid j,\qquad
0<D=H-(n-2)<H/324,
$$


where


$$
H=3^{h-1},\quad A=n-2=H-D,\quad
d=\frac{3D}{2}-1,\quad
\nu=\frac D2-1,\quad m=\frac{A+1}{2}.
$$


The actual columns are $1,y,\ldots,y^m$, partitioned into LOW $0\le a<d$ and HIGH $d\le a\le m$. The bilinear form is the supplied complete rational moment form, not a positive replacement metric.

Write


$$
Q_n=\lambda Q_n^{\rm loc},\qquad
\lambda=L_n/3\in\mathbb Z_3^\times.
$$


For the calculation only, remove $\lambda$.

Put $M=(4^j-1)/3$, and set


$$
t=v_3(j)+2\ge6,\qquad \beta=-71-3M.
$$


The established polynomial law gives the exact decomposition


$$
Q_n^{\rm loc}=(y+1)(y-1)^A(\beta+3y)+3^tR(y),
\qquad R\in\mathbb Z_3[y],\quad \deg R\le n.
\tag{1}
$$



Use the complete functional


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+3^h\sum_{v\ge0}\frac{[y^v]C_F}{2v+1},
\quad
C_F=\frac{F-F(-1)}{y+1},
\quad
\mathfrak f(y^s)=(2s)!.
\tag{2}
$$


For products in the actual column space, $\deg F\le2n-1$; hence the denominators in (2) have exactly the original cutoff


$$
2v+1\le4n-3.
$$


This is the all-pole functional, including endpoint subtraction and the factorial contribution.

## 2. Exact beta valuations: the proposal passes in its stated range

Define


$$
B_H(s)=\int_0^1x^{2s}(x^2-1)^H\,dx
=\frac{(-1)^H2^H H!}
{\prod_{a=0}^{H}(2s+2a+1)}
\qquad(s\ge0).
\tag{3}
$$



Let $H=3^u$, $u\ge1$. If


$$
0\le s\le(H-3)/2,
$$


the first $H$ factors in the denominator of (3) contain exactly $H/3^q$ multiples of $3^q$, for $1\le q\le u$. None is divisible by $3^{u+1}$: their largest possible value is $3H-4$. Therefore their total valuation is $v_3(H!)$.

The extra factor $2s+2H+1$ lies between $2H+1$ and $3H-2$, so its valuation is at most $u-1$. Consequently


$$
\boxed{
v_3(B_H(s))=-v_3(2s+2H+1),
\qquad
v_3(3^hB_H(s))\ge2,
}
\tag{4}
$$


where $h=u+1$.

Thus the coordinator’s valuation statement is correct. It is a depth-two statement, not a fifth-depth assertion.

For shifts outside this interval, the exact valuation remains available without any cycle assumption:


$$
v_3(B_H(s))
=v_3(H!)
-\sum_{a=0}^{H}v_3(2s+2a+1).
\tag{5}
$$


In particular, no extrapolation of (4) to all HIGH shifts is justified.

## 3. Exact geometric contraction, including both remainders

For $r\ge1$, put


$$
T_r(y)=\sum_{a=0}^{r-1}(-3y/\beta)^a,
\qquad
k_i(y)=y^i(y-1)^DT_r(y).
$$


These are admissible actual columns only when


$$
D+i+r-1\le m.
\tag{6}
$$


Their exact geometric identity is


$$
(\beta+3y)T_r(y)
=\beta-(-3)^r\beta^{1-r}y^r.
\tag{7}
$$



For any actual test polynomial $g(y)=\sum_b g_by^b$, equations (1)–(3) give


$$
\boxed{
\begin{aligned}
\mathcal M(Q_n^{\rm loc}k_i g)
={}&-\frac{3^h}{4}\mathfrak f(Q_n^{\rm loc}k_i g)\\
&+3^h\beta\sum_b g_bB_H(i+b)\\
&-3^h(-3)^r\beta^{1-r}
       \sum_b g_bB_H(i+b+r)\\
&+3^{h+t}\sum_{v\ge0}
 \frac{[y^v]C_{Rk_i g}}{2v+1}.
\end{aligned}}
\tag{8}
$$


Every term is an exact rational number. The last line retains endpoint subtraction; the factorial in the first line is the factorial functional, not the derangement functional.

### Uniform precision

On this domain $4n-3<3^{h+1}$. Thus every admissible denominator has valuation at most $h$, and


$$
\mathcal M\bigl(3^a\mathbb Z_3[y]_{\le2n-1}\bigr)
\subseteq3^a\mathbb Z_3.
\tag{9}
$$


The geometric-remainder polynomial in (7), after multiplication by the other factors, is divisible coefficientwise by $3^r$. Hence its contribution is in $3^r\mathbb Z_3$. The $R$-contribution is in $3^t\mathbb Z_3$, and the factorial contribution is in $3^h\mathbb Z_3$.

Therefore


$$
\boxed{
\mathcal M(Q_n^{\rm loc}k_i g)
\equiv 3^h\beta\sum_b g_bB_H(i+b)
\pmod{3^{\min(r,t,h)}}.
}
\tag{10}
$$


This estimate is uniform in the admissible columns and includes all poles.

Taking $r=6$ gives sufficient **full-matrix** precision modulo $3^6$ for a fifth LOW digit, since the LOW normalization divides by $3$. It does not say that the surviving beta term vanishes to that precision.

## 4. A genuine obstruction: geometric cancellation leaves exact depth-two HIGH forces

Take $r\ge3$, with (6), and $0\le i<\nu$. Set


$$
r_2=\frac{H/3-1}{2},\qquad b=r_2-i.
$$


The assigned inequality $D<H/324$ ensures


$$
d\le b\le m.
$$


Thus $y^b$ is an actual HIGH column.

Here $i+b=r_2$, and


$$
2r_2+2H+1=\frac{7H}{3},
\qquad
v_3(7H/3)=h-2.
$$


Equation (4) gives


$$
v_3(3^h\beta B_H(r_2))=2.
$$


The geometric remainder has depth at least $3$, the true-polynomial remainder has depth at least $6$, and the factorial contribution has depth $h>2$. Consequently


$$
\boxed{
v_3\!\left(
\mathcal M(Q_n^{\rm loc}k_i y^{\,r_2-i})
\right)=2.
}
\tag{11}
$$



This is an exact nonvanishing statement for the complete rational pairing. It is not a selected-pole calculation.

**Therefore the proposed geometric columns are not full kernels modulo $27$, let alone modulo $729$, before HIGH elimination.** The degree increase is not merely a bookkeeping issue: an actual nonzero HIGH force remains.

## 5. Complete correction formula and what still has to be evaluated

Here is an exact bounded correction procedure retaining all forces.

Let $\mathscr B(f,g)=\mathcal M(Q_n^{\rm loc}fg)$. Let $Y$ be the column list $y^d,\ldots,y^m$, and $U$ the column list $1,\ldots,y^{D-1}$. Define


$$
E=\mathscr B(Y,Y),\qquad
J=\mathscr B(Y,U),\qquad
G=\mathscr B(U,U)-J^TE^{-1}J.
\tag{12}
$$


The established block structure gives


$$
E\in\mathrm{GL}(\mathbb Z_3),\qquad
G=3G_1,\qquad G_1\in\mathrm{GL}(\mathbb Z_3).
$$



For the geometric columns $K=(k_i)_{i<\nu}$, retain the complete force matrices


$$
P=\mathscr B(Y,K),\qquad
Q=\mathscr B(U,K)-J^TE^{-1}P.
\tag{13}
$$


Define


$$
\widehat U=U-YE^{-1}J,
\qquad
\boxed{\widehat K=K-YE^{-1}P-\widehat U\,G^{-1}Q.}
\tag{14}
$$


These columns annihilate both eliminated blocks exactly. Their complete remaining form is


$$
\boxed{
\mathscr B(\widehat K,\widehat K)
=\mathscr B(K,K)-P^TE^{-1}P-Q^TG^{-1}Q.
}
\tag{15}
$$



All entries in (12)–(15) are evaluated by the full rational moments (2), and the $K$-forces can be evaluated directly by (8). No HIGH term or LOW correction has been omitted.

The inverse $G^{-1}=G_1^{-1}/3$ is the explicit precision loss. Here $Q\in3\mathbb Z_3$, so (14) remains integral. In the quadratic term of (15), the division by $3$ is accompanied by two divisible forces. This provides a stable finite-precision calculation, but **does not evaluate its fifth digit**.

The transported endpoint is likewise exactly


$$
\boxed{
\widehat K(-1)
=K(-1)-Y(-1)E^{-1}P
-\widehat U(-1)G^{-1}Q.
}
\tag{16}
$$


It cannot be replaced by the uncorrected values $k_i(-1)$ at higher precision.

Equations (8), (12)–(16) give a complete computational lift interface. They are not an evaluated rank theorem: the unresolved quantity is the residue of (15), after its LOW division and the four established powers of $3$. In particular, (11) shows why one cannot discard $P^TE^{-1}P$.

## 6. Final denominator and whole-error interface

No new fifth-depth gcd bound follows from this audit. Retain the established fourth-depth bound and the actual primitive scalar $\lambda$.

For the complete integer pair,


$$
g=\gcd(|A_{\rm det}|,|B_{\rm det}|),\qquad
q=\frac{|B_{\rm det}|}{g},\qquad
p=-\frac{\operatorname{sgn}(B_{\rm det})A_{\rm det}}g.
$$


Where $B_{\rm det}\ne0$,


$$
\boxed{
q(e+\pi)-p
=\frac{\operatorname{sgn}(B_{\rm det})\ell^k}{g}
\det H_{\rm complete},
\qquad k=(n+1)/2.
}
$$


The primitive multiplier is the full clearer $\ell^k$ divided by the **final** gcd. The denominator still depends on the transported endpoint cofactor:


$$
v_3(q)=\max\!\left\{0,\,
h+2v_3((n-1)!)-1+
v_3(\operatorname{adj}(S)_{\rm endpoint})
-v_3(\det S)\right\},
$$


where the displayed valuation expression is used when its terms are defined.

Neither polynomial endpoint nonvanishing nor the raw beta valuation proves complete-response nonvanishing, whole-determinant nonvanishing, or decay of the whole primitive error.

### Closing ledger

1. **New result and proof status.** Proved: the uniform exact-beta contraction (8)–(10), the actual depth-two HIGH force (11), and the complete correction/endpoint formulas (12)–(16). The geometric proposal is valid as a raw-moment reduction, but not as an uncorrected full kernel. No fifth rank or all-depth recurrence is asserted.

2. **Exact remaining bottleneck.** Evaluate the fifth residue of the full expression (15), including both inverse contractions, and its transported endpoint (16). More globally, compatible control of the actual reduced denominator and nonzero whole primitive errors tending to zero remains missing. Irrationality of $e+\pi$ is not decided.

3. **Computation request.** None. The obstruction (11) and the precision bounds are symbolic and uniform; no finite rank scan is needed to establish them.
