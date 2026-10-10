> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the nonproportional small-root classification

Checked: 2026-08-26 UTC

## Snapshot and verdict

This audit concerns the final candidate
`sources/nonproportional_small_root_classification.md`, SHA-256

```text
58e800337a182eec76cd26efb6e0134f0b6fc1a0ad6efe6e765407c07c3f6af9
```

and the associated reproducible diagnostics

```text
scripts/nonproportional_small_root_diagnostics.py
077c9abf58ec20c93201fc569dbfb2ef175cc8329a4c2f8c90cd5e7a63dbef89

results/nonproportional_small_root_diagnostics.json
125508dd27fa218024dda2ad56f455bc5249535c940c4d9fc0dfd6043e615ec3
```

The result file embeds the same theorem and script hashes.  I accept the
classification theorem in that snapshot.  In particular, for the exact
coefficientwise clearing used there, every unbounded admissible sequence
diverges for $N=3,4$, while for $N=6$ the cleared liminf is at least
$6/e^2$.

This verdict was not true of the first snapshot presented for audit.  The
review found and repaired three proof gaps:

1. the original endpoint-saddle proof controlled fixed compact scaled
   intervals but omitted a moving transition band near $u=0$;
2. the exponential-remainder comparison was stated before the required
   separate lower estimate for the logarithmic summand; and
3. the subsequence exhaustion incorrectly said that the raw form diverged
   on the edge $c=d=0,\ f\to\infty$, although its displayed raw limit is
   $2\pi i$.

The final snapshot contains uniform estimates for the first two points and
an exact denominator argument for the third.  The details are checked
below.  No numerical diagnostic is used as a proof.

## 1. Uniform auxiliary-polynomial estimate

Write



$$
T_{d,f}(u)=\sum_{q=0}^d\frac{(-1)^q}{q!u^q}R_q,
 \qquad
 R_q=\frac{d^{\underline q}}{(d+f)^{\underline q}},
 \qquad
 \beta=\frac d{d+f}.
$$



For $q\le d/2$, every factor in $R_q$ lies in $[0,\beta]$, and



$$
0\leq\beta-\frac{d-j}{d+f-j}
 =\frac{jf}{(d+f)(d+f-j)}\leq\frac{2j}{d}.
$$



The telescoping product identity therefore gives



$$
|R_q-\beta^q|\leq Cq^2/d
$$



with a constant independent of $f$.  After division by $q!|u|^q$,
this is summable uniformly on every compact set separated from $u=0$.
The tails $q>d/2$ are bounded by factorial tails because $0\le R_q\le1$.
Consequently



$$
T_{d,f}(u)=e^{-\beta/u}(1+O_K(d^{-1}))
$$



uniformly for all $f\ge0$.  The relative form is legitimate because
$e^{-\beta/u}$ is bounded away from zero on the relevant compact union as
$0\le\beta\le1$.  This proves the uniformity claimed in Lemma 1, including
the $f/d\to\infty$ edge.

## 2. Runckel's theorem is applied within its hypotheses

The fixed integral is



$$
I_{c,d,N}=B(c+d+1,c+1)
 {}_2F_1(c+1,c+d+1;2c+d+2;\eta_N).
$$



In the notation of [DLMF 15.13](https://dlmf.nist.gov/15.13), take



$$
a=c+1,\qquad b=c+d+1,\qquad C=2c+d+2=a+b.
$$



Then $a,b,C,C-a,C-b$ are positive integers, $b\ge a$, and the allowed
condition $C\ge a+b$ holds with equality.  Thus the zero-balanced case is
not excluded.  Since $a>0$, DLMF 15.13.1 gives zero zeros in



$$
|\operatorname{ph}(1-z)|<\pi.
$$



At $z=\eta_N$, $1-z=\zeta_N$ has argument $2\pi/N\in(0,\pi)$.
The Euler denominator



$$
1-\eta_Nu=(1-u)+u\zeta_N
$$



is the nonzero chord from $1$ to $\zeta_N$ and stays on the principal
branch.  Hence the hypergeometric value and $I_{c,d,N}$ are nonzero for
every admissible integer pair.  This validates Lemma 2 without a numerical
nonvanishing assumption.

## 3. Uniform endpoint saddle for $c=o(d)$

The delicate case is $c\to\infty$, $\lambda=d/c\to\infty$, uniformly
for all $f\ge c$.  With



$$
\psi_{N,\lambda}(u)
 = (\lambda+1)\Log u+\Log(1-u)-\Log(1-\eta_Nu),
 \qquad r=\frac{u}{1-u},
$$



the lower saddle is on the ray $r=xe^{i\theta}$, where



$$
r_*=
 \frac{\lambda+\sqrt{\lambda^2+4(\lambda+1)\overline{\zeta_N}}}{2}
 =Re^{i\theta},
 \qquad -\frac\pi N<\theta<0.
$$



The previously audited Descartes calculation gives exactly one maximum of
the phase modulus on this ray, at $r_*$.  The ray deformation crosses
neither $r=-1$ nor the pole $r=-\overline{\zeta_N}$.

### 3.1 The moving transition band

Scale the ray by $r=\lambda xe^{i\theta}$ and put



$$
G_\lambda(x)=
 \Re\psi_{N,\lambda}(u(\lambda xe^{i\theta}))+\log\lambda.
$$



The exact expression, not merely a compact-limit expansion, is



$$
G_\lambda(x)=
 -(\lambda+1)\log\left|1+
 \frac{e^{-i\theta}}{\lambda x}\right|
 -\log|1+\zeta_N\lambda xe^{i\theta}|+\log\lambda.
$$



Set



$$
\kappa_N=\cos(\pi/N)>0,
 \qquad
 s_N=\min_{\phi\in[\pi/N,2\pi/N]}\sin\phi>0.
$$



The angle bounds imply
$\cos\theta\ge\kappa_N$ and
$\sin(2\pi/N+\theta)\ge s_N$.  Taking the real part of the first
modulus and the imaginary part of the second yields the global inequality



$$
G_\lambda(x)\le
 -(\lambda+1)\log\left(1+\frac{\kappa_N}{\lambda x}\right)
 -\log(s_Nx).                                      \tag{A1}
$$



Let $t=\lambda x$.  If $t\ge1$, then



$$
G_\lambda(x)\le-K_N/x+\log(1/x)+O_N(1),           \tag{A2}
$$



because
$\log(1+\kappa_N/t)\ge\kappa_N/((1+\kappa_N)t)$.
If $1/3\le t\le1$, (A1) instead gives



$$
G_\lambda(x)\le-K_N'\lambda+O_N(\log\lambda).    \tag{A3}
$$



Finally, $|u|\ge1/2$ implies $t\ge1/3$: from
$2t\ge|1+r|\ge1-t$ one obtains $3t\ge1$.  Thus (A2)--(A3) cover the
entire formerly missing regime in which $x\to0$ while $\lambda x$
moves between a constant and infinity.  For large $x$, (A1) gives
$G_\lambda(x)\le-\log(s_Nx)$.

On every fixed compact $0<a\le x\le b<\infty$, the exact formula and all
of its fixed-order $x$-derivatives converge uniformly to



$$
h(x)=-x^{-1}-\log x.
$$



This function has its unique nondegenerate maximum at $x=1$.  The exact
saddle satisfies $R/\lambda=1+O_N(\lambda^{-1})$, so Taylor expansion at
the actual saddle has a uniform quadratic real-part loss outside its
$O(c^{-1/2})$ neighborhood.  This supplies the uniform local/tail link;
pointwise convergence alone would not have supplied it.

The length of the complete deformed contour is uniformly bounded:



$$
\int|du|
 =\int_0^\infty
 \frac{\lambda\,dx}{|1+\lambda xe^{i\theta}|^2}
 \le\int_0^\infty\frac{dt}{1+2\kappa_Nt+t^2}=O_N(1). \tag{A4}
$$



### 3.2 The genuine $u=0$ endpoint

The approximation of Lemma 1 is not used at $u=0$.  Directly from the
finite sum and $0\le R_q\le1$,



$$
|u^dT_{d,f}(u)|\le |u|^d e^{1/|u|}
 \le e^{-d\log2+2}
 \quad(d^{-1}\le|u|\le1/2),                         \tag{A5}
$$



and, after putting $k=d-q$,



$$
|u^dT_{d,f}(u)|
 \le\sum_{k=0}^d\frac{|u|^k}{(d-k)!}
 \le\frac{d+1}{d!}
 \quad(|u|\le d^{-1}).                              \tag{A6}
$$



The last inequality follows termwise from
$d^{-k}/(d-k)!\le1/d!$.  The remaining factor on $|u|\le1/2$ is at
most $C_N^{c+1}$, and (A4) controls the length.  Thus these two pieces
have logarithms



$$
-\Omega_N(d)+O_N(c),\qquad
 -d\log d+O_N(d+c),
$$



whereas the saddle logarithm is



$$
-c(1+\log\lambda)+O_N(c/\lambda+\log d)=-o(d).
$$



Both endpoint pieces are uniformly negligible for every $c=o(d)$.

### 3.3 Local coefficient and the stated error

At the saddle,



$$
r_*=\lambda+\overline{\zeta_N}+O_N(\lambda^{-1}),
 \quad
 u_*=1-\lambda^{-1}+O_N(\lambda^{-2}),
 \quad
 \psi''(u_*)=-\lambda^2(1+O_N(\lambda^{-1})).
$$



Lemma 1 supplies the amplitude



$$
\frac{e^{-\beta/u_*}}{1-\eta_Nu_*}
 =\frac{e^{-\beta}}{\zeta_N}
 (1+O_N(\lambda^{-1})),
 \qquad 0\le\beta\le1,
$$



which is uniformly nonzero for all $f\ge c$.  The normalized higher
derivatives in the scaled $x$-coordinate are uniformly bounded.  The
one-saddle Gaussian therefore has a nonzero coefficient and no conjugate
saddle on the contour with which it could cancel.  Expanding its modulus
and applying Stirling gives



$$
\log|J_N|
 =\log(c!)-(c+1)\log d-\beta
 +O_N(1+c/\lambda)
 =\log(c!)-(c+1)\log d-\beta
 +O_N(1+c^2/d).                                      \tag{A7}
$$



For bounded $c$, the real endpoint substitution $t=d(1-u)$, dominated
by a fixed polynomial times $e^{-t/2}$, gives the stronger relative
equivalent



$$
J_N=\zeta_N^{-c-1}e^{-\beta}
 \frac{c!}{d^{c+1}}(1+O_{N,c}(d^{-1})),              \tag{A8}
$$



again uniformly in $f$.  Equations (A7)--(A8), together with the exact
outside factors, give precisely Lemma 3.

## 4. The exponential remainder is compared noncircularly

The final proof first estimates $A(1)R_{\log}(\eta_N)$ and only then
compares the exponential summand.

* On $c/d\ge\epsilon>0$, the compact-slope and $f$-dominant saddles give
  
  

$$
\log|A(1)R_{\log}|=2\log\binom{d+f}{d}+O_{N,\epsilon}(d),
$$


  
  while the coefficient bound gives
  $\log|A(\eta_N)|\le\log\binom{d+f}{d}+O_N(d)$.  The factorial
  remainder leaves a ratio logarithm at most
  $-d\log d+O_{N,\epsilon}(d)$.

* On $c=o(d)$, (A7)--(A8) give the denominator separately.  After the
  coefficient bound, the ratio logarithm is at most
  
  

$$
-\log((d+f+1)!)+
  O_N\bigl(c\log(d/c+2)+c+\log d+c^2/d\bigr).
$$


  
  The error is $o(d\log d)$, uniformly in $f\ge c$.

* If $d$ is fixed and $f\to\infty$, the coefficient factors are
  polynomial and the exponential remainder is factorially small.

Thus the assertion



$$
\Lambda_N\sim N A(1)R_{\log}(\eta_N)
$$



is a consequence of independent numerator and denominator estimates, not
an assumption used to derive them.

## 5. The missing $c=d=0$ clearing edge

When $c=d=0$, the exact coefficient formula gives



$$
A(x)=1,\qquad B(x)=0,\qquad
 E_f(x)=S_f(x):=\sum_{n=0}^f\frac{x^n}{n!}.
$$



Hence, for every $N\in\{3,4,6\}$,



$$
\Lambda_N(0,0,f)=2i(e+\pi-S_f(1))\longrightarrow2\pi i.
$$



The raw form therefore does **not** diverge.  In the integral bases used to
define coefficientwise clearing,



$$
U_N=2i,\qquad V_N=-2iS_f(1),\qquad
 q_N(0,0,f)=\operatorname{den}(2S_f(1)).              \tag{A9}
$$



The rationals $2S_f(1)$ are strictly increasing and bounded.  For every
fixed $M$, a bounded interval contains only finitely many rationals whose
reduced denominator is at most $M$.  Therefore the denominators in (A9)
tend to infinity, and



$$
q_N(0,0,f)|\Lambda_N(0,0,f)|\longrightarrow\infty.  \tag{A10}
$$



This exact argument repairs the only bounded-$d$ branch on which raw
divergence was unavailable.

## 6. Consequences, subsequences, and the $N=6$ boundary

For $N=3,4$, $|\eta_N|>1$; the $d\log|\eta_N|$ term in Lemma 3
dominates $O(c^2/d)$ whenever $c=o(d)$.  Thus the raw form diverges on
that endpoint edge.

For $N=6$, $|\eta_6|=1$.  If $c\to\infty$ and $c=o(d)$, the lower
bound is



$$
(c-1)\log(d/c)-\log c-O(c^2/d),
$$



which tends to infinity because



$$
\frac{c^2/d}{c\log(d/c)}
 =\frac1{(d/c)\log(d/c)}\longrightarrow0.
$$



For bounded $c$, the uniform equivalent (A8) leaves exactly the listed
possibilities:

* $c=f=0$: the raw form is asymptotic to $6e^{-2}/d$, while the already
  audited exact bound $q_6\ge d^2/2$ makes the cleared form diverge;
* $c=f=1$: the raw form tends to $6/e^2$, so $q_6\ge1$ gives the
  claimed lower edge;
* $c=0,f\ge1$, $c=1,f\ge2$, or fixed $c\ge2$: the binomial factor in
  the equivalent forces divergence.

The subsequence exhaustion is complete.  If $d$ is bounded, then $c,d$
may be fixed on a further subsequence and $f\to\infty$; Lemma 2 gives
raw polynomial growth for $d\ge1$, while (A10) handles $d=0$.  If
$d\to\infty$, every subsequence has a further subsequence on which either

1. $c/d\to0$;
2. $c/d\ge\epsilon>0$ and $f/d$ is bounded; or
3. $c/d\ge\epsilon>0$ and $f/d\to\infty$.

Lemma 3 handles the first, the compact-slope estimate handles the second,
and the uniform $f$-dominant estimate handles the third.  The usual
subsequence principle then proves the two divergence statements and the
$N=6$ liminf statement for arbitrary, rather than merely pointwise,
parameter sequences.

## 7. Diagnostic audit

The original diagnostic used many direct high-precision calls to
`mpmath.hyp2f1` in the zero-balanced complex case and was prohibitively slow
to reproduce.  The frozen script instead evaluates the same sampled factor
by the nonsingular Euler integral divided by its beta factor.  Selected
values are independently evaluated with Gauss--Legendre and tanh--sinh
quadrature.  This is only a performance and reproducibility change; the
proof of nonvanishing remains Runckel's theorem.

At 90-decimal working precision, the rerun records:

* matching embedded theorem and script hashes;
* maximum absolute endpoint logarithmic residual
  $0.5407271501694232$;
* maximum absolute compact-slope $f$-dominant residual
  $1.262225200033681$;
* zero serialized relative difference in all nine independent quadrature
  comparisons; and
* the same sampled hypergeometric minima as the earlier diagnostic.

These finite values are consistent with the asymptotics but are not used
to pass any limit or nonvanishing claim.

## Final scope

The accepted theorem closes the stated nonproportional small-root Rivoal
family.  It does not control all algebraic conjugates of $e+\pi$, and it
does not prove either algebraicity or transcendence of $e+\pi$.
