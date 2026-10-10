> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## A1 turn 6: a growing arctangent-pole content theorem, but not the growing polynomial endpoint lift

I do not prove


$$
v_3(c\xi_{\rm const}-b\xi_{\rm last})=v_3((n-1)!)
$$


on an infinite regular class. The supplied $n=65$ computation is consistent with that equality, but it does not supply its missing induction or saturation argument.

There is, however, a substantive consequence of the primitive polynomial ray for the **actual rational-arctangent matrix**. On an explicitly specified infinite subclass, its highest $3$-power pole has an exactly computable rank. This forces growing content in the **final endpoint gcd**, not just polynomial coefficient content.

In particular, at $n=65$ I prove


$$
\boxed{v_3(A)\ge26,\qquad v_3(\det K)\ge25,\qquad v_3(g)\ge26.}
$$


These statements require no new degree computation and do not use the conjectural endpoint depth $60$.

The result also explains why the $n=17$ finding $v_3(A)=0$ cannot extend uniformly to the regular sequence.

---

## 1. Normalize the actual highest arctangent pole

Let


$$
n=4^j+1,\qquad j\ge1,\qquad
m=\frac{n-1}{2},\qquad k=m+1,
$$


and let $Q=Q_n$ be the actual primitive integer matching polynomial. Reuse the turn-5 primitive-ray result:


$$
\overline Q(y)=u(y+1)(y-1)^{n-2},
\qquad u\in\mathbb F_3^\times.
\tag{1}
$$



Use the endpoint basis


$$
f_0(y)=1,\qquad f_i(y)=(y+1)y^{i-1}\quad(1\le i\le m).
\tag{2}
$$


This is an integral unit-triangular change from the monomial basis.

For an integer polynomial $F$, write its complete rational endpoint functional as


$$
\mathcal R(F)
=-\sum_s [y^s]F\,(2s)!
+4\int_0^1
\frac{F(x^2)-F(-1)}{1+x^2}\,dx.
\tag{3}
$$


The integrand in the second term is polynomial. Thus this identity retains every rational arctangent term without introducing a period or omitting an endpoint correction.

Set


$$
\ell=\operatorname{lcm}(1,3,\ldots,4n-3),\qquad
h=\left\lfloor\log_3(4n-3)\right\rfloor,\qquad
r=\frac{3^h-1}{2}.
\tag{4}
$$


The maximum degree of $Qf_if_j$ is $2n-1$, so the quotient polynomial in (3) has degree at most $2n-2$. Its integration denominators are precisely among the odd integers at most $4n-3$.

**There is exactly one such denominator having valuation $h$: $3^h$.** Indeed, an odd multiple $a3^h\le4n-3<3^{h+1}$, with $3\nmid a$, must have $a=1$.

Consequently, with


$$
\lambda=\overline{\ell/3^h}\in\mathbb F_3^\times,
$$


the exact highest-pole reduction is


$$
\boxed{
\overline{\ell\mathcal R(F)}
=
4\lambda\,[y^r]\,
\overline{\frac{F(y)-F(-1)}{y+1}}.
}
\tag{5}
$$


The exponential factorial contribution disappears modulo $3$ because $h\ge1$. Every lower arctangent pole also disappears. No assumption about its cancellation is needed.

Applying (5) to $F=Qf_if_j$, and using (1), gives the actual normalized endpoint matrix


$$
T=\ell R_{\rm end}
$$


the residue formula


$$
\boxed{
\overline T_{ij}
=
4\lambda u\,[y^r]\,(y-1)^{n-2}f_i(y)f_j(y),
\qquad 0\le i,j\le m.
}
\tag{6}
$$



Thus $Q\bmod3$ does determine the complete matrix after its highest logarithmic pole has been cleared. It does **not** determine the next digits.

---

## 2. Exact rank on a growing-index subclass

Define


$$
\tau=r-(n-2).
\tag{7}
$$


Since $f_i$ is monic of degree $i$, the polynomial on the right of (6) has degree


$$
n-2+i+j.
$$


It follows that


$$
\overline T_{ij}=0\quad\text{if }i+j<\tau,
\tag{8}
$$


whereas


$$
\overline T_{ij}=4\lambda u\ne0
\quad\text{if }i+j=\tau.
\tag{9}
$$



Consider the explicit index class


$$
\mathcal J
=
\left\{
j\ge1:
3^{\lfloor\log_3(4n-3)\rfloor}\ge3n-2,\quad n=4^j+1
\right\}.
\tag{10}
$$


On this class,


$$
m+1\le\tau\le2m+1.
$$



Put


$$
s=\max(0,\,2m-\tau+1)
=\max\left(0,\,2n-2-r\right).
\tag{11}
$$



### Exact-rank theorem

For every $j\in\mathcal J$,


$$
\boxed{
\operatorname{rank}_{\mathbb F_3}\overline T=s,
\qquad
\operatorname{rank}_{\mathbb F_3}\overline K=s,
}
\tag{12}
$$


where $K$ is the lower $m\times m$ block of $T$.

### Proof

If $\tau=2m+1$, every entry vanishes by (8), and $s=0$.

Otherwise, each row with index


$$
i<\tau-m
$$


vanishes entirely. Hence the full matrix has rank at most


$$
m-(\tau-m)+1=2m-\tau+1=s.
$$



Restrict both rows and columns to


$$
\tau-m,\ \tau-m+1,\ldots,m.
$$


This is an $s\times s$ block. Reverse its columns. Equations (8)–(9) make the resulting matrix triangular with diagonal entries $4\lambda u$. Its determinant is a unit. Thus its rank is $s$.

Because $\tau-m\ge1$, the same unit minor lies entirely in $K$. The zero-row bound applies to $K$ as well, proving both equalities. ∎

### The class is infinite

Choose any fixed real interval


$$
\frac14<a<b<\frac13.
$$


Since $\log_3 4$ is irrational, its positive integer multiples are dense modulo $1$. Therefore there are infinitely many $j$ and integers $H$ with


$$
a<\frac{4^j}{3^H}<b.
$$


For all sufficiently large such $j$,


$$
3^H\le4(4^j+1)-3<3^{H+1},
\qquad
3^H\ge3(4^j+1)-2.
$$


Thus $h=H$ and $j\in\mathcal J$. This establishes an infinite-index theorem, not an extrapolation from $n=65$.

---

## 3. Transfer to the actual final gcd

Retain exactly the endpoint pair


$$
T=
\begin{pmatrix}
t&z^T\\ z&K
\end{pmatrix},
\qquad
A=t\det K-z^T\operatorname{adj}(K)z=\det T,
\qquad
B=\ell Q(-1)\det K.
\tag{13}
$$


All these quantities are integers.

An integral $d\times d$ matrix of residue rank $s$ has determinant divisible by $3^{d-s}$. This follows, for example, by lifting invertible residue row operations and factoring $3$ from each of the remaining $d-s$ rows.

Hence (12) gives


$$
\boxed{
v_3(A)\ge k-s,\qquad
v_3(\det K)\ge m-s.
}
\tag{14}
$$


The convention $v_3(0)=+\infty$ applies if necessary.

Set


$$
d_j=k-s.
\tag{15}
$$


On the class (10), this can be written


$$
\boxed{
d_j=\frac{3^h-3n+4}{2}\ge1.
}
\tag{16}
$$



The established nonzero endpoint bound is


$$
v_3(Q(-1))\ge v_3((n-1)!)+1.
$$


Therefore


$$
v_3(B)
=h+v_3(Q(-1))+v_3(\det K)
\ge h+v_3(Q(-1))+d_j-1
\ge d_j.
\tag{17}
$$


For the actual final gcd,


$$
g=\gcd(|A|,|B|),
$$


we obtain


$$
\boxed{v_3(g)\ge d_j.}
\tag{18}
$$



This is a proved content divisor of the **complete endpoint pair**. It is not a row-clearer estimate substituted for the final gcd.

### The supplied next index $n=65$

Here


$$
m=32,\quad k=33,\quad h=5,\quad r=121,\quad\tau=58,
$$


so


$$
s=7,\qquad d_j=26.
$$


Consequently,


$$
v_3(A)\ge26,\qquad
v_3(\det K)\ge25,\qquad
v_3(g)\ge26.
\tag{19}
$$



If one also uses the supplied finite endpoint depth $v_3(Q_{65}(-1))=60$, as justified by the turn-5 leading-content theorem and the reported coupled computation, then


$$
v_3(B)\ge5+60+25=90.
\tag{20}
$$


Equation (20) remains a lower bound; it does not determine $v_3(q)$.

---

## 4. What fails, and what remains genuinely unknown

The proposed growing coupled-endpoint pattern is not disproved. Its exact obstruction remains the absence of a uniform evaluation of


$$
b,\qquad \xi_{\rm const}
$$


at precision comparable to $v_3((n-1)!)$. The first radical lift supplies only fixed precision. The Pascal residue inverse does not, by itself, control the successive inverse corrections to that growing depth.

The new endpoint theorem identifies a separate, concrete obstruction to extrapolating the $n=17$ actual denominator behavior:

* The $n=17$ highest-pole matrix is reported to have unit determinant.
* At $n=65$, its determinant necessarily has depth at least $26$.
* On the infinite class (10), a growing number of rows vanish at the highest-pole residue level.

Thus **uniform $v_3(A)=0$ is false** on the regular family. The mechanism is a degree cutoff at the highest arctangent pole, not coefficient nonprimitivity.

The replacement statement is (12)–(18). Exact determinant valuations require further pole layers and further digits of $Q$. Knowing the residue rank tells us the minimum number of nonunit Smith factors, but not their depths.

---

## 5. Actual denominator, whole error, and nonvanishing

No reduction is omitted:


$$
q=\frac{|B|}{g},\qquad
p=-\frac{\operatorname{sgn}(B)A}{g},
\qquad
v_3(q)=\max\{0,v_3(B)-v_3(A)\}.
\tag{21}
$$


In particular, the lower bounds for both valuations in (14) and (17) cannot be subtracted to obtain a bound for $v_3(q)$.

With $S=e+\pi$, the whole evaluated error is


$$
\boxed{
qS-p
=
\frac{\operatorname{sgn}(B)}g(A+BS)
=
\frac{\operatorname{sgn}(B)\ell^k}{g}
\det H_{\rm complete}.
}
\tag{22}
$$


The full exponential and arctangent contributions remain present.

Reusing the supplied regular dyadic theorem gives $B\ne0$ and pairwise distinct reduced centers on $n=4^j+1$. Hence (22) is nonzero apart from at most one regular index, without assuming irrationality. No shrinking-error conclusion follows here.

---

## Closing ledger

### (1) New result and proof status

**Proved:** the highest-pole formula (5)–(6), exact ranks (12), determinant divisibility (14), and actual final-gcd divisor (18), on the explicit infinite regular subclass (10).

**Concrete proved consequence:** at $n=65$, the complete endpoint gcd contains $3^{26}$. Uniform extrapolation of the $n=17$ unit-$A$ behavior is impossible.

**Not proved:** the growing coupled-endpoint equality, an exact actual-$q$ law, or irrationality of $e+\pi$.

### (2) Exact remaining bottleneck

Two distinct growing lifts remain:

1. Evaluate $c\xi_{\rm const}-b\xi_{\rm last}$ beyond the first radical precision.
2. Lift the explicitly identified rank-$s$ highest-pole endpoint matrix far enough to determine the relative depths of $A$ and $B$, rather than just common divisibility.

The second problem is now localized to the nonunit Smith factors of a matrix with an explicit unit minor.

### (3) Computation request

**None this turn.** The $n=65$ endpoint rank and content conclusions above follow symbolically from the established primitive ray. A further degree scan would not settle either growing lift.
