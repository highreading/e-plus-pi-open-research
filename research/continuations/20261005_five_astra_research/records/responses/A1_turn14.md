> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## Result: the projection vanishes, but the proposed constant ray needs an index correction

The stronger residual lemma does hold:


$$
\boxed{v\in27\mathbb Z_3^L\qquad(9\mid M).}
$$


Consequently the combined projection correction is zero modulo $3$. The entire lower factorial tail also vanishes modulo $81$ on the assigned class.

However, there is a valuation error in the assignment’s proposed specialization. For


$$
M=\frac{4^j-1}{3},
$$


LTE gives


$$
\boxed{v_3(M)=v_3(j),\qquad v_3(L)=1+v_3(j),\quad L=3M.}
$$


Thus $9\mid j$ implies $9\mid M$, **not necessarily $27\mid M$**. In particular $V=M/9$ need not be divisible by $3$, and $N=1+27V$ need not equal $1\bmod81$.

Using the supplied exact raw-contraction certificate, the resulting projected ray is


$$
\boxed{
Q^{\rm loc}_n(y)=3P_n(y)
\equiv
(y+1)(y-1)^{n-2}\bigl(3y+10-27w\bigr)\pmod{81},
\quad j=9w,\ w\ge1,\quad n=4^j+1.
}
$$


The proposed factor $3y+10$ is therefore valid on the narrower class $27\mid j$. The extra term on the full assigned class is $-27w$; it comes from the raw digit and $N$, not from projection or a surviving tail.

### 1. A bounded moment-polynomial lemma

Here is a direct one-digit extension of the finite-difference support argument, retaining all moment terms required modulo $27$.

For $r=0,1,2$, there exists a polynomial $p_r(t)\in\mathbb Z_3[t]$, of degree at most $4$, such that


$$
e_{3t+r}\equiv p_r(t)\pmod{27}\qquad(t\ge0).
$$


Its coefficients satisfy


$$
[p_r]_{t^k}\in3\mathbb Z_3\quad(k\ge1),
\qquad
v_3([p_r]_{t^k})\ge k-2.
\tag{1}
$$



To prove this without dropping moment contributions, use the full nine-term residue


$$
f(s)=\sum_{\ell=0}^{8}
\frac{(-1)^\ell}{2^\ell\ell!}
\prod_{a=-\ell+1}^{\ell}(s+a).
$$


The omitted moment terms are divisible by $81$, hence certainly by $27$.

Fix any nonnegative integer $b$. In the $\ell$-th product evaluated at $s=3t+b$, let $z$ be the number of constant factors divisible by $3$. Then


$$
z\ge\lfloor2\ell/3\rfloor.
$$


Every contribution to its coefficient of $t^k$ has valuation at least


$$
\max(k,z)-v_3(\ell!).
\tag{2}
$$


Indeed, selecting $k$ variable terms supplies $3^k$; among the other factors, at least $z-k$ of the divisible constant factors remain, if $z>k$.

For $0\le\ell\le8$, $v_3(\ell!)\le2$, so (2) gives the bound $k-2$. For $\ell\ge3$,


$$
\lfloor2\ell/3\rfloor-v_3(\ell!)\ge1;
$$


thus all coefficients of those summands are divisible by $3$. For $\ell=0,1,2$, every nonconstant coefficient is divisible by $3$ directly, since the factorial denominator is a unit. This proves the coefficient assertions for $f(3t+b)$.

Now insert these polynomials into


$$
e_s=4b_s^{\rm mom}+4(s+1)b_{s+1}^{\rm mom}
 +(s+1)(s+2)b_{s+2}^{\rm mom},
$$


using


$$
b_{3t+b}^{\rm mom}
\equiv(-2)^b(1-9t)f(3t+b)\pmod{27}.
$$


Multiplication by $3t+b+1$, $3t+b+2$, and $1-9t$ preserves both coefficient bounds. Every coefficient of degree at least $5$ is divisible by $27$. Truncating those coefficients proves (1).

This argument includes all nine moment terms; it does not infer the next digit from previously vanishing residues.

### 2. Every residual entry vanishes modulo $27$ when $9\mid M$

Write $i=3q+r$, $0\le q<M$, $0\le r<3$, and


$$
B(q,D)=\binom{q+D}{D}.
$$


The block-factorial formula modulo $27$ gives


$$
\binom{3(q+D)}{3D}
\equiv B(q,D)\left(1+\frac92qD(q+D)\right).
$$


For $r=1,2$, multiply this by


$$
\prod_{a=1}^{r}\frac{3(q+D)+a}{3q+a}.
$$


All denominators are units. As a polynomial in $D$, the resulting multiplier modulo $27$ has the form


$$
1+a_1(q)D+a_2(q)D^2,
\qquad
a_1(q)\in3\mathbb Z_3,\quad a_2(q)\in9\mathbb Z_3.
\tag{3}
$$


Terms of higher degree are divisible by $27$.

Combine (1) and (3). For every fixed $q,r$, there is a polynomial


$$
K_{q,r}(D)=\sum_{h=0}^{4}\kappa_h(q,r)(D)_h
$$


such that


$$
\binom{i+3D}{i}e_{i+3D}
\equiv B(q,D)K_{q,r}(D)\pmod{27},
$$


and


$$
\boxed{\kappa_h(q,r)\in3\mathbb Z_3\qquad(1\le h\le4).}
\tag{4}
$$


The degree bound follows explicitly: a degree-$4$ moment coefficient has depth at least $2$, so multiplication by the linear correction in (3) kills degree $5$; a degree-$3$ coefficient has depth at least $1$, so multiplication by the quadratic correction also kills degree $5$. Conversion from powers to falling factorials uses integer Stirling numbers and preserves (4).

Now apply the exact finite-difference identity


$$
\sum_{D=0}^{M}(-1)^{M-D}\binom MD(D)_hB(q,D)
=(M)_h\binom{q+h}{M}.
$$


The constant term is zero because $q<M$. Hence


$$
v_{3q+r}\equiv
\sum_{h=1}^{4}\kappa_h(q,r)(M)_h\binom{q+h}{M}
\pmod{27}.
\tag{5}
$$


This exhibits explicit support only in the last four Pascal blocks: if $q<M-4$, every term is zero.

If $9\mid M$, each $(M)_h$, $1\le h\le4$, contains $M$ and is divisible by $9$. Equation (4) therefore makes every term in (5) divisible by $27$. Thus


$$
\boxed{v\in27\mathbb Z_3^L\qquad(9\mid M).}
$$



In the notation $v=9v_0,\ w=3w_0$, this proves $v_0\equiv0\pmod3$. Since $E^{-1}$ is integral,


$$
\boxed{v_0^TE^{-1}(2v_0-w_0)\equiv0\pmod3.}
$$


No unevaluated inverse response remains: the entire left vector vanishes. More strongly,


$$
v^TE^{-1}v/3\in243\mathbb Z_3,\qquad
v^TE^{-1}w\in81\mathbb Z_3.
$$


Therefore the supplied raw contractions are the actual projected norm and mixed scalar modulo $81$.

### 3. The complete lower factorial tail

Let $j=9w$, $w\ge1$. Then


$$
v_3(L)\ge3,\qquad v_3(L-3)=1.
$$


In


$$
3P_n
=3h_n-3N!\eta_{\rm const}
-\sum_{d=0}^{L}\frac{N!}{d!}(3\eta_{d+1})h_{d+1},
$$


all $3\eta_{d+1}$ are integral.

Here are every dangerous lower index and the remaining range:

| Index $d$ | Factorial depth | Additional coefficient information |
|---|---:|---|
| $L-1$ | at least $3$ | $3\eta_{d+1}\equiv0\pmod3$, since $d\equiv2\pmod3$ |
| $L-2$ | at least $3$ | $3\eta_{d+1}\equiv0\pmod3$, since $d\equiv1\pmod3$ |
| $L-3$ | at least $3$ | its radical coefficient is a unit multiple of $M$, hence zero modulo $3$ |
| $d\le L-4$ | at least $4$ | $N!/d!$ contains both $L$ and $L-3$ |

Thus every lower nonconstant term vanishes modulo $81$. The first three coefficient statements are exactly the first radical support: only $d=3D$ survives, with last-Pascal coefficients proportional to $(-1)^{M-D}\binom MD$.

The constant contribution is $3P_n(-1)$. The normalized endpoint argument of A1 turn 9 gives


$$
v_3(P_n(-1))=2v_3(N!)-1,
$$


so its depth after multiplication by $3$ is $2v_3(N!)>4$ throughout this domain. The endpoint terms in the Schur ratio likewise have far more than the required depth.

There is therefore **no surviving thin tail**.

### 4. Evaluation of the actual ray

Put $M=9V$. The supplied exact coefficient certificate gives


$$
c/3\equiv4+27V,\qquad
\xi_{\rm last}\equiv29+27V\pmod{81}.
$$


These are now projected identities, by Section 2. Thus


$$
3\eta_{\rm last}\equiv68+54V\pmod{81}.
$$


But $N=1+27V$, so


$$
N(3\eta_{\rm last})
\equiv68+27V\pmod{81}.
$$


Consequently


$$
Q^{\rm loc}_n(y)
\equiv(y+1)(y-1)^L(3y+10-27V)\pmod{81}.
$$


Finally,


$$
4^{9w}\equiv(1+27)^w\equiv1+27w\pmod{81},
$$


which gives $V\equiv w\pmod3$ and proves the stated ray.

The raw coefficient expansion is used here as supplied exact symbolic data; I have not independently executed its arithmetic. The new projection and tail arguments are explicit proofs.

For the actual primitive integer polynomial, retain


$$
\boxed{
Q_n=\frac{L_n}{3}Q^{\rm loc}_n,\qquad L_n/3\in\mathbb Z_3^\times.
}
$$


Writing $F_m=v_3(m!)$, its nonzero endpoint satisfies


$$
\boxed{e_Q=v_3(Q_n(-1))=2F_{n-1}.}
$$



### 5. Actual final gcd and whole error remain separate

For the complete cleared pair, retain


$$
A=t\det K-z^T\operatorname{adj}(K)z,\qquad
B=\ell Q_n(-1)\det K,
$$




$$
g=\gcd(|A|,|B|),\qquad
q=\frac{|B|}{g},\qquad
p=-\frac{\operatorname{sgn}(B)A}{g}.
$$


Where $B\ne0$,


$$
\boxed{
q(e+\pi)-p
=\frac{\operatorname{sgn}(B)}g\bigl(A+B(e+\pi)\bigr)
=\frac{\operatorname{sgn}(B)\ell^k}{g}\det H_{\rm complete},
\quad k=(n+1)/2.
}
$$



A4’s displayed Schur normalization gives, on its specified unit-minor domain,


$$
v_3(q)=
\max\!\left\{0,\,
h+2F_{n-1}-1+
v_3(\operatorname{adj}(S)_{00})-v_3(\det S)
\right\}.
$$


This remains an exact relative-valuation interface, not an evaluated denominator theorem. Polynomial endpoint nonvanishing is proved; complete response nonvanishing and the distinct-center assertion are cited inherited results, not independently proved by the supplied local calculations.

## Closing ledger

1. **New result and proof status.** Proved $v\in27\mathbb Z_3^L$ for $9\mid M$, evaluated the combined projection as zero, and eliminated every lower factorial term modulo $81$. Using the supplied raw certificate, the completed ray is
   

$$
Q^{\rm loc}_n\equiv(y+1)(y-1)^{n-2}(3y+10-27w),
   \qquad j=9w,\ w\ge1.
$$


   The constant proposed ray holds when $27\mid j$.

2. **Exact remaining bottleneck.** This completes the requested polynomial digit, with the corrected index dependence. Irrationality still requires control of the actual final gcd and nonzero **whole primitive errors**, sufficiently strong to obtain errors tending to zero. No irrationality or rationality conclusion follows here.

3. **Computation request.** None. No further raw contraction or large-degree polynomial computation is needed for this digit.
