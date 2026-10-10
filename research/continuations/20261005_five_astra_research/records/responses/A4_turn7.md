> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 independent audit: both new reports pass; a next-pole cofactor interface is proved

## Audit conclusions

| Item | Verdict |
|---|---|
| A3 turn 6: five weights, corner analysis, and total adjoint density | **PASS** |
| A3 turn 6: localized signed asymptotic for the complete numerator | **PASS** |
| A3 turn 6: exclusion of the stated proportional-order odd-primorial subfamily | **PASS**, with the actual reduced denominator |
| A1 turn 6: highest-pole identity and exact ranks | **PASS** |
| A1 turn 6: determinant and actual common-gcd divisibility | **PASS** |
| A1 turn 6: an exact odd-denominator law | **Not established or implied** |

The new follow-on result below expresses the next pole layer explicitly in terms of $Q\bmod 9$, then identifies the **same distinguished cofactor** governing both endpoint determinants. This is stronger than a further rank bound, but does not determine its growing relative valuation.

No conclusion here decides irrationality of $e+\pi$.

---

# I. Audit of the signed interior-density argument

I use $b=\sqrt2$, $M=1+b$, $r=2M$, and the notation of A3.

## 1. All five weights agree with the original endpoint contractions

From the original $b=2$ endpoint identities and A3 turn 5,


$$
\frac{C_k}{(k!)^2}=(k+1)(kF+G),\qquad
\frac{S_k}{(k!)^2}=(k+1)^2\bigl((k+1)B+D\bigr),
$$


where product integrations are understood. Thus the complete arctangent amplitude is


$$
u(k+1)^3(kF+G)-2(k+1)^2\bigl((k+1)B+D\bigr).
$$


Expanding this expression gives, in descending degree,


$$
\begin{aligned}
A_4&=uF,\\
A_3&=u(3F+G)-2B,\\
A_2&=u(3F+3G)-2(3B+D),\\
A_1&=u(F+3G)-2(3B+2D),\\
A_0&=uG-2(B+D).
\end{aligned}
$$


These are exactly A3 turn 6’s five weights.

The symmetric formulas also have the correct orientation. In particular,


$$
B_0A_1-B_1A_0
$$


has symmetrized relative weight


$$
\frac12(v_1-v_2)(q_2-q_1),
$$


not its negative.

The ratios $q=w_1/w_0$ and $h=w_2/w_0$ are only needed near the corner, where $w_0>0$. Their possible failure as global coordinates causes no problem: outside that neighborhood one retains the original finite signed measures.

## 2. Corner uniqueness, Hessian, and the complete local pushforward

The product $v_1v_2$ lies in $[-1,M^2]$, and its positive maximum $M^2$ occurs only when both circle variables equal $-M$. Since $u\in[-2/M,0)$, the only point attaining $T=-r$ is


$$
\theta_1=\theta_2=y=0
$$


on the two circles and the Heine half-line.

Expansion gives


$$
v_i=-M+\frac b2\theta_i^2+O(\theta_i^4),\qquad
u=-\frac2M+\frac b{M^2}y^2+O(y^4),
$$


and consequently


$$
T+r=b(\theta_1^2+\theta_2^2+y^2)+O(|(\theta_1,\theta_2,y)|^4).
$$


The Hessian is therefore $2bI_3$.

The absence of remote preimages is justified, not assumed. Since


$$
|T|\le M^2|u(y)|\longrightarrow0\qquad(y\to\infty),
$$


a neighborhood of $-r$ has bounded $y$-preimages. Compactness and uniqueness of the minimum then separate the complement of any fixed corner neighborhood from $-r$.

Extend evenly in $y$, apply analytic Morse coordinates, and divide the full-space integral by two. Spherical averaging of the transformed analytic amplitudes gives


$$
f_j(-r+s)=s^{1/2}a_j(s),
$$


with $a_j$ analytic at zero. This argument applies to the **entire actual pushforward density** sufficiently near $-r$. It also justifies differentiating the expansions.

The corner measure weight is


$$
\frac{e^{-2b}}{\pi^2M}.
$$


The half-space pushforward under $s=b|x|^2$ has density


$$
\frac{\pi}{b^{3/2}}s^{1/2}.
$$


Hence


$$
K=\frac{e^{-2b}}{\pi M b^{3/2}},
$$


as claimed.

## 3. Fourth-order vanishing and constants

Writing $a=v+1$ and $\beta^2=2-a^2$,


$$
q(v)=a-\beta\tan\beta
$$


is analytic near $v=-M$. Its corner data are


$$
q(-M)=-b,\qquad h(-M)=b^2,\qquad q'(-M)=1-2b.
$$


Thus


$$
F=-\frac{1-2b}{2}(v_1-v_2)^2+O\bigl((|v_1+M|+|v_2+M|)^3\bigr).
$$


This really is fourth-order angular vanishing.

Using


$$
(v_1-v_2)^2=\frac{b^2}{4}(\theta_1^2-\theta_2^2)^2+O(|\theta|^6)
$$


and


$$
\operatorname{avg}_{S^2}(\omega_1^2-\omega_2^2)^2=\frac4{15},
$$


one obtains


$$
f_4(-r+s)=K\frac{1-2b}{15M}s^{5/2}+O(s^{7/2}).
$$


The factor $u(0)=-2/M$ is essential to this coefficient and is correctly included.

At the corner,


$$
F=0,\quad G=-M^2,\quad B=M^2,\quad D=0.
$$


Putting $A=-2bM$, all lower-degree values are


$$
(A_0,A_1,A_2,A_3)=(A,3A,3A,A).
$$


In particular,


$$
f_3(-r+s)=AKs^{1/2}+O(s^{3/2}).
$$



## 4. The total adjoint density is nonzero

For Lebesgue density,


$$
D^*f=-(Tf)',\qquad D^*=(r-s)\partial_s-1.
$$


Since


$$
\partial_s^3s^{1/2}=\frac38s^{-5/2},
$$


the degree-three term contributes


$$
\frac38r^3AKs^{-5/2}.
$$


The fourth derivative of $f_4=O(s^{5/2})$ contributes only $O(s^{-3/2})$. The degree-two term and every lower-derivative correction also contribute at most that order. Therefore


$$
\boxed{
\sum_{j=0}^4(D^*)^jf_j(-r+s)
=-\frac34bMr^3K\,s^{-5/2}+O(s^{-3/2}).
}
$$


This verifies noncancellation in the **total** density.

This density is not integrable up to $s=0$, and no such assertion is needed. Its use is confined to compactly supported interior localization.

## 5. Cutoffs, outside contributions, and rounding

At


$$
c_0=\frac5r-1
$$


the negative support endpoint strictly dominates the positive branch. A3’s rational inequalities prove this directly. For fixed $c>c_0$ sufficiently close to $c_0$, the unique negative saddle


$$
T_c=-\frac5{1+c}
$$


lies where the total adjoint density is negative, and remains strictly dominant globally.

Choose a smooth cutoff supported inside this density interval and equal to one on a fixed neighborhood of $T_c$. For $c_n=m/n\to c$, the same neighborhood contains $T_{c_n}$ eventually.

There are two distinct error controls:

* On the complement of that neighborhood, the original finite measures and the uniform Euler bound give a polynomial factor times an exponentially smaller phase maximum.
* Every term containing a derivative of the cutoff has compact support away from the saddle. Its density and derivatives are bounded there, so the same exponential gap applies.

Thus no endpoint integration by parts is hidden in the argument.

The curvature is


$$
-\phi_c''(T_c)=\frac{(1+c)^3}{25c}.
$$


Uniform interior Laplace asymptotics yield exactly A3’s formula (15), including its parity and arbitrary integer sequences with $m/n\to c$.

The complete exponential correction is bounded by


$$
C(N+1)^4\frac{(2M^3)^n}{n!}
\left(5+\frac{2M^3}{n+1}\right)^m.
$$


Its logarithm is $-n\log n+O_c(n)$, so it cannot cancel the exponential-scale saddle contribution. This includes both the adjacent truncation correction and the separate $H_{k+1}W_k$ term.

## 6. Eventual denominator sign

The supplied accepted endpoint result gives the required eventual common sign and ratio. The negative sign asserted in A3 turn 6 is also consistent directly with the present moment representation.

Indeed, in the two-circle integral, the unique dominant corner has


$$
G=-M^2,\qquad F=O(|\theta|^4).
$$


Under its Gaussian concentration, the $kF$ contribution is smaller by $O(k^{-1})$ than the nonzero $G$ contribution. Hence $C_k<0$ eventually. Similarly, the $(k+1)B$ contribution dominates the bounded $D$ contribution, giving $S_k>0$ eventually.

Moreover $L_k(1)>0$: the Legendre generating function gives


$$
\sum_{k\ge0}L_k(1)t^k=(1-4t-4t^2)^{-1/2},
$$


whose coefficients are positive. Thus


$$
\mathscr D_k=(k+1)^2L_{k+1}(1)C_k-2L_k(1)S_k<0
$$


eventually, and positive filter weights give $\mathcal J_{n,m}<0$.

Consequently the complete transformed numerator has eventual sign $(-1)^{n+1}$, and the primitive error has sign $(-1)^n$.

## 7. Final gcd and scoped primorial exclusion

Retain


$$
U=L_N\mathcal H_{n,m},\quad V=L_N\mathcal J_{n,m},\quad
L_N=2^{N+1}(2N+2)!(N!)^4,
$$


and


$$
g=\gcd(|U|,|V|),\qquad
P=-\operatorname{sgn}(V)U/g,\qquad q=|V|/g.
$$


Then


$$
\boxed{
q(e+\pi)-P=q\,\frac{\mathcal Z_{n,m}}{\mathcal J_{n,m}}.
}
$$



For a fixed $c$ in the proved existence interval and


$$
N_x=\prod_{\substack{p\le x\\p\text{ odd}}}p,\qquad
n_x=\left\lfloor\frac{N_x}{1+c}\right\rfloor,\quad m_x=N_x-n_x,
$$


the complete center error has finite logarithmic rate $O(N_x)$, while the accepted actual-denominator bound is


$$
\liminf\frac{\log q}{N_x\log\log N_x}\ge2.
$$


Therefore


$$
\boxed{
\liminf\frac{\log|q(e+\pi)-P|}{N_x\log\log N_x}\ge2.
}
$$


This is a valid exclusion of precisely this filtered primorial subfamily. It is not an exclusion of all proportional orders or all filtered indices.

---

# II. Audit of the highest-pole content theorem

## 1. Highest coefficient and denominator uniqueness

For


$$
C_F(y)=\frac{F(y)-F(-1)}{y+1},
$$


the exact rational functional is


$$
\mathcal R(F)=-\sum_s[y^s]F(2s)!
+4\sum_a\frac{[y^a]C_F}{2a+1}.
$$


Here $\deg(Qf_if_j)\le2n-1$, so $\deg C_F\le2n-2$, and all odd denominators are at most $4n-3$.

If $h=\lfloor\log_3(4n-3)\rfloor$, the only denominator in this range with valuation $h$ is $3^h$: the next odd multiple is $3^{h+1}$, outside the range.

Thus A1’s highest-pole formula is correct. Reduction of the exact quotient is legitimate even though $Q(-1)\ne0$: modulo $3$, the primitive ray has the factor $y+1$, and hence


$$
\overline{C_{Qf_if_j}}
=u(y-1)^{n-2}f_if_j.
$$



## 2. Rank, edge cases, and saturation

With


$$
\tau=r-(n-2),\qquad r=(3^h-1)/2,
$$


the entries vanish for $i+j<\tau$, and equal the same unit on $i+j=\tau$.

For $m+1\le\tau\le2m$, set $a=\tau-m$. Rows $0,\ldots,a-1$ vanish modulo $3$, while the trailing block indexed by $a,\ldots,m$ becomes triangular with unit diagonal after column reversal. Both $T$ and $K$ therefore have rank


$$
s=m-a+1.
$$



At $\tau=2m$, only the final diagonal entry survives, giving rank one for both matrices. At $\tau=2m+1$, both matrices vanish modulo $3$, giving rank zero. The stated formulas cover both edges.

The basis


$$
1,(y+1),(y+1)y,\ldots,(y+1)y^{m-1}
$$


is integral unit-triangular. In particular, its nonconstant part is a saturated basis of the integral endpoint-zero submodule. No factorial-divided or nonsaturated basis is substituted in the rank-to-determinant step.

## 3. Infinite class and actual gcd

The irrationality of $\log_3 4$ follows from unique prime factorization. Density of its integer multiples modulo one supplies infinitely many ratios


$$
a<4^j/3^H<b,\qquad \frac14<a<b<\frac13.
$$


The strict margins absorb the additive constants in $4n-3$ and $3n-2$. Hence the asserted infinite class is valid. On any such fixed ratio interval, the defect $d_j$ grows linearly in $n$; this is not merely finite evidence of growth.

The rank deficits give


$$
v_3(A)\ge d_j,\qquad v_3(\det K)\ge d_j-1,
$$


and the nonzero primitive endpoint bound gives $v_3(B)\ge d_j$. Therefore


$$
v_3\gcd(A,B)\ge d_j.
$$



At $n=65$,


$$
(m,h,r,\tau,s,d_j)=(32,5,121,58,7,26).
$$


Thus the three bounds $26,25,26$ pass without using the reported endpoint depth $60$.

That depth remains a finite input, not an infinite law. Neither pair of lower bounds can be subtracted to bound $v_3(q)$.

---

# III. New result: explicit next-pole layer and a shared cofactor/Smith interface

This result applies on the same infinite class. All local algebra below is over $\mathbb Z_3$.

Write


$$
u_\ell=\ell/3^h,\qquad
C_{ij}(y)=\frac{Q(y)f_i(y)f_j(y)-Q(-1)f_i(-1)f_j(-1)}{y+1}.
$$



## 1. The next pole layer, with complete $Q$-dependence

Define


$$
\mathcal A_h=
\{a\in\{1,5,7\}:a3^{h-1}\le4n-3\},\qquad
r_a=\frac{a3^{h-1}-1}{2}.
$$


The numbers $a3^{h-1}$, $a\in\mathcal A_h$, are exactly the denominators of valuation $h-1$.

On this regular family $h\ge2$. Consequently the exponential factorial term is zero modulo $9$ after multiplication by $\ell$. All poles below valuation $h-1$ likewise disappear modulo $9$. Therefore


$$
\boxed{
T_{ij}\equiv
4u_\ell\left(
[y^r]C_{ij}
+3\sum_{a\in\mathcal A_h}a^{-1}[y^{r_a}]C_{ij}
\right)\pmod9.
}
\tag{1}
$$


Here $a^{-1}$ is interpreted in $\mathbb Z_3$.

Formula (1) retains the full coefficient dependence on $Q\bmod9$. The primitive ray alone does not determine the first term divided by $3$.

## 2. Exact elimination using the known unit minor

Let


$$
d=k-s.
$$


Partition indices into


$$
L=\{0,\ldots,d-1\},\qquad H=\{d,\ldots,m\}.
$$


The trailing block $E=T_{HH}$ is a unit matrix in the sense that $\det E\in\mathbb Z_3^\times$. The blocks $T_{LL}$ and $T_{LH}$ are divisible by $3$.

Define the exact integral symmetric matrix


$$
\boxed{
S=\frac{T_{LL}-T_{LH}E^{-1}T_{HL}}3\in M_d(\mathbb Z_3).
}
\tag{2}
$$


If $s=0$, take $E$ empty with determinant one and set $S=T/3$.

Since $T_{LH}$ is divisible by $3$, the cross correction vanishes after division by $3$ and reduction modulo $3$. Thus, for $i,j\in L$,


$$
\boxed{
\overline S_{ij}
=
4\overline{u_\ell}\left(
\overline{\frac{[y^r]C_{ij}}3}
+\sum_{a\in\mathcal A_h}\overline{a}^{-1}
\,\overline{[y^{r_a}]C_{ij}}
\right).
}
\tag{3}
$$


The division by $3$ is valid because these low-block highest-pole coefficients vanish modulo $3$.

This is an explicit next-layer matrix, not just its rank. It requires $Q\bmod9$ for the divided highest coefficient and $Q\bmod3$ for the lower-pole coefficients.

## 3. Both endpoint determinants reduce to one matrix and one cofactor

Let $S^{(0)}$ denote $S$ with row and column zero removed. Schur elimination yields


$$
\boxed{
A=3^d\det E\,\det S,\qquad
\det K=3^{d-1}\det E\,\det S^{(0)}.
}
\tag{4}
$$


Thus


$$
\det S^{(0)}=\operatorname{adj}(S)_{00}
$$


is the precise cofactor linking the two endpoint determinants.

Put $e_Q=v_3(Q(-1))$. The actual local common content is exactly


$$
\boxed{
v_3(g)=
d+\min\!\left\{
v_3(\det S),\
h+e_Q-1+v_3(\operatorname{adj}(S)_{00})
\right\}.
}
\tag{5}
$$


Accordingly,


$$
\boxed{
v_3(q)=
\max\!\left\{0,\
h+e_Q-1+
v_3(\operatorname{adj}(S)_{00})-v_3(\det S)
\right\}.
}
\tag{6}
$$


Unlike subtracting two lower bounds, (6) is an exact relative-valuation identity.

The accepted dyadic theorem ensures $A,B\ne0$ on the regular domain, so both determinants in (4) are nonzero. Equivalently,


$$
\boxed{
v_3(q)=
\max\{0,h+e_Q-1+v_3((S^{-1})_{00})\}.
}
\tag{7}
$$



## 4. What Smith data must include

Suppose


$$
USV=\operatorname{diag}(3^{a_1},\ldots,3^{a_d}),
\qquad U,V\in\mathrm{GL}_d(\mathbb Z_3),
$$


with unit factors absorbed into $U,V$. Then


$$
(S^{-1})_{00}
=\sum_{\nu=1}^dV_{0\nu}U_{\nu0}\,3^{-a_\nu}.
\tag{8}
$$


Therefore the Smith exponents alone are insufficient. One also needs the transformed distinguished endpoint coordinate and its cancellation in (8).

For example, if both $\overline S$ and its principal minor $\overline{S^{(0)}}$ are nonsingular, then (6) gives the exact conditional law


$$
v_3(q)=h+e_Q-1.
$$


If only $\overline S$ is nonsingular, the remaining extra depth is exactly the cofactor depth. If $\overline S$ is singular, further lifting is needed.

This identifies a sharper obstruction: **the relative endpoint depth is a distinguished inverse entry of the first lifted Schur matrix**, not the difference of independently estimated determinant depths.

---

# Closing ledger

## (1) New result and proof status

**Proved in this audit:**

* A3 turn 6’s local density, total adjoint amplitude, complete signed asymptotic, and scoped primorial exclusion pass.
* A1 turn 6’s highest-pole ranks and actual common-gcd divisibility pass.
* Equations (1)–(3) give the explicit next pole layer with complete $Q\bmod9$ dependence.
* Equations (4)–(8) give an exact common-cofactor and Smith-coordinate interface for the actual reduced denominator.

The weighted primitive pair remains


$$
g=\gcd(|A|,|B|),\qquad
q=|B|/g,\qquad p=-\operatorname{sgn}(B)A/g,
$$


with the whole evaluated error


$$
\boxed{
q(e+\pi)-p
=\frac{\operatorname{sgn}(B)}g(A+B(e+\pi))
=\frac{\operatorname{sgn}(B)\ell^k}{g}\det H_{\rm complete}.
}
$$


On $n=4^j+1$, $j\ge1$, $B\ne0$, and this error is nonzero except possibly at one index, by the established distinct-center theorem.

## (2) Exact remaining bottleneck

For the weighted route, one must control both:

1. The actual endpoint depth $e_Q$, beyond its established lower bound.
2. The distinguished inverse entry $(S^{-1})_{00}$, including cancellation between Smith-coordinate contributions.

The explicit next-pole formula does not yet evaluate these uniformly. For the filtered route, the stated primorial subfamily is excluded, but other orders and index families remain outside that conclusion.

## (3) Computation request

**None.** The new interface is an exact algebraic lemma. A finite computation of $\overline S$ could test a particular index, but would not establish the missing growing-index relative-valuation law.
