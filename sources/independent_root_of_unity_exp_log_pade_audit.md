> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the root-of-unity exponential--logarithm Padé branch

Date: 2026-08-26

## Verdict

**ACCEPT the revised checkpoint, with exactly the limited scope stated in
the source.**

The audited source is

    sources/root_of_unity_exp_log_pade_audit.md

at SHA-256

    8a5dc774a64c754cea228c7a7cf323213a4fc6965c7d59cc98a26ee8a3e6e5d2

I independently checked the author-corrected source statement, reconstructed
the reversal at the origin, checked every factorial and least-common-multiple
factor in the denominator clearing, derived both integral remainders and
their bounds, reconstructed the conditional algebraic integer, and checked
the field-degree, norm, branch, and nonvanishing arguments.  I also wrote an
independent exact-rational implementation of the finite formal tests and an
independent high-precision implementation of the numerical diagnostics.

No substantive mathematical error remains in the revised checkpoint.  Two
scope restrictions are essential:

1. Under the bare hypothesis that $s=e+\pi$ is algebraic, an integer
   $\delta>0$ for which $\delta s$ is integral exists, but neither
   $\delta$, the minimal polynomial of $s$, nor the house
   $S_\delta$ is effectively known.  The Padé factor $d!^2G$ is
   completely explicit.  The algebraic integer and the global embedding
   bound are explicit only relative to a choice of $\delta$ and, for the
   latter, the conjugates of $\delta s$.  The source now says this
   explicitly.
2. The cyclotomic norm calculation exactly neutralizes or worsens the
   isolated factor $(1-\zeta)^M$.  It does not calculate the norm of the
   full additive form $X$, and it does not rule out accidental
   cancellation among its summands.  The source states this limitation and
   therefore does not promote the calculation to an impossibility theorem.

The branch consequently gives a valid conditional algebraic-integer
reduction and rigorous obstructions to the naive proof strategy.  It does
not prove algebraicity, irrationality, or transcendence of $e+\pi$.

## 1. Primary-source verification

I independently downloaded the published paper from the journal and the
author-maintained corrected manuscript.  Their SHA-256 hashes are,
respectively,

    936877cc2a199163e1301c0e73abf8ba1cf2f58f878a9f05292aa33bb387dc3d
    fefdfc7dbca65c33ffc83c2d1d88b798af1f0d43ec53c412b1dfad6552b642c9

The journal version is T. Rivoal, “Simultaneous Padé approximants to the
Euler, exponential and logarithmic functions,” Journal de Théorie des
Nombres de Bordeaux 27 (2015), 565--589, DOI
[10.5802/jtnb.914](https://doi.org/10.5802/jtnb.914).  The corrected file is
the author's
[April 2021 manuscript](https://rivoal.perso.math.cnrs.fr/articles/explog.pdf).

The corrected PDF itself verifies every source caveat in the audited note:

- page 5 says that misprints in the published paper were corrected,
  especially in Theorem 3;
- corrected Theorem 3 on page 7 assumes
  $d\geq2c$ and $f\geq c$;
- its exponential identity contains the factor $z^{d-f-c}$ and has
  remainder order $O(z^{-(f-c+1)})$;
- the proof of Theorem 3 is said to be similar to the preceding proofs and
  is omitted;
- the footnote on page 7 says that the published Theorem 4 was removed
  after correction of another misprint because the corrected result had
  little practical interest;
- the theorem numbered 4 in the corrected manuscript is instead a theorem
  about the logarithm and Euler's divergent series.

The published PDF has the erroneous condition $c\geq d$, a different
exponential factor and order, and an undefined exponent $n$ in its
formula (2.18).  The audited source is therefore correct not to use the
published Theorems 3 or 4 as printed.

The corrected manuscript is an author-maintained primary source, not a
separately published journal erratum, and it omits the proof of the corrected
Theorem 3.  This audit verifies the corrected statement's formal
consequences and supplies finite corroboration; it does not claim that the
finite tests replace a missing all-parameter proof in the source.

## 2. Reversal of corrected Theorem 3

Put



$$
C=c+d,\qquad F=f+2c.
$$



Corrected Theorem 3 gives



$$
\begin{aligned}
P(z)\log(1-1/z)-Q_1(z)&=O(z^{-c-1}),\\
P(z)e^{1/z}-z^{d-f-c}Q_2(z)&=O(z^{-(f-c+1)}),
\end{aligned}
$$



with $\deg P,\deg Q_1\leq C$ and $\deg Q_2\leq F$.  Define



$$
A(x)=x^CP(1/x),\qquad
B(x)=x^CQ_1(1/x),\qquad
E(x)=x^FQ_2(1/x).
$$



Substituting $z=1/x$ and multiplying the logarithmic identity by $x^C$
gives



$$
A(x)\log(1-x)-B(x)
=O(x^{C+c+1})
=O(x^{2c+d+1}).
$$



For the exponential identity, the polynomial term becomes



$$
x^C x^{f+c-d}Q_2(1/x)
=x^{f+2c}Q_2(1/x)
=E(x),
$$



while the remainder becomes



$$
O(x^{C+f-c+1})=O(x^{f+d+1}).
$$



This verifies both identities and every exponent in source equation (8).
No rescaling or informal identification is being used.

Reversing the explicit polynomial gives



$$
[x^m]A
=\sum_{\substack{0\leq j\leq d,\ 0\leq k\leq c\\c+j-k=m}}
(-1)^{d-j+k}
\binom ck\binom{c+d-j+k}{c}\binom{d+f-j}{f}\frac1{j!}.
$$



At $m=0$, the constraints force $j=0,k=c$, so



$$
[x^0]A=(-1)^{c+d}
\binom{d+2c}{c}\binom{d+f}{f}\ne0.
$$



Thus $A$ is nonzero for every admissible triple.

The use of the identities at different points is legitimate.  The
exponential identity is evaluated at $x=1$, while the logarithmic identity
is evaluated at $x=\eta$.  Cross-multiplication by $A(1)$ and
$A(\eta)$ then synchronizes the two coefficients; no theorem with
independently rescaled functional arguments is being assumed.

## 3. Exact denominator clearing

Every denominator in $A$ is a $j!$ with $0\leq j\leq d$.  Therefore



$$
A^*=d!A\in\mathbb Z[x].
$$



The logarithmic order is



$$
2c+d+1=C+c+1>C.
$$



Since $\deg B\leq C$, $B$ is exactly the degree-$C$ truncation of
$A(x)\log(1-x)$.  If $A(x)=\sum_m a_mx^m$, then



$$
[x^n]B=-\sum_{m=0}^{n-1}\frac{a_m}{n-m}
\qquad(0\leq n\leq C).
$$



Every integer $n-m$ here lies in $\{1,\ldots,C\}$.  Hence, with
$\ell_C=\operatorname{lcm}(1,\ldots,C)$ and $\ell_0=1$,



$$
B^*=d!\ell_CB\in\mathbb Z[x].
$$



Similarly,



$$
f+d+1>f+2c=F
$$



because $d\geq2c$.  Thus $E$ is exactly the degree-$F$ truncation of
$A(x)e^x$:



$$
[x^n]E=\sum_{m=0}^{\min(n,C)}\frac{a_m}{(n-m)!}
\qquad(0\leq n\leq F).
$$



Every factorial denominator divides $F!$, so



$$
E^*=d!F!E\in\mathbb Z[x].
$$



Consequently



$$
G=\operatorname{lcm}(\ell_C,F!)
$$



makes both $G/\ell_C$ and $G/F!$ integers.  The product of two Padé
polynomial values requires the factor $d!^2$, so the safe common Padé
clearing is exactly



$$
\mathcal D=d!^2G.
$$



The source does not claim that this is always minimal.  The edge cases
$C=0$ and $F=0$ are covered by $\ell_0=1$ and $0!=1$.

## 4. Coefficient and conjugate-height estimates

For $a_m^*=d![x^m]A$, each summand is bounded by



$$
d!\,2^c
\binom{d+2c}{c}\binom{d+f}{f},
$$



and there are at most $(c+1)(d+1)$ summands.  This proves



$$
H(A^*)\leq H_0
$$



with exactly the $H_0$ in source equation (15).

The convolution formulas above give



$$
H(B^*)\leq\ell_CH_0\mathcal H_C
$$



and



$$
H(E^*)\leq F!H_0\sum_{r=0}^{F}\frac1{r!}
<eF!H_0<3F!H_0.
$$



For every primitive cyclotomic conjugate
$\eta_a=1-\zeta^a$, $|\eta_a|\leq2$.  Summing coefficient bounds gives
the four quantities $U_A,U_B,V_A,V_E$ in source equation (17), with no
missing factor.  Since $\eta$ is integral and all its conjugates have
modulus at most $2$, $h(\eta)\leq\log2$.  The standard polynomial
evaluation inequality then gives source equation (18).

Thus no rational denominator is hidden in the root-of-unity evaluation.
The arithmetic cost moves into coefficient heights, factorial clearing,
field degree, and the other conjugates.

## 5. Conditional algebraic integer and embedding bound

Let



$$
\Lambda=2iA(\eta)R_{\exp}(1)+NA(1)R_{\log}(\eta).
$$



Because the Taylor branch at the distinguished point has
$\log(1-\eta)=2\pi i/N$, direct expansion gives



$$
\Lambda=
2iA(1)A(\eta)(e+\pi)
-2iA(\eta)E(1)
-NA(1)B(\eta).
$$



Assume $s=e+\pi$ is algebraic and choose an integer $\delta>0$ for which
$\delta s$ is an algebraic integer.  Substituting



$$
A=A^*/d!,\qquad
B=B^*/(d!\ell_C),\qquad
E=E^*/(d!F!)
$$



and multiplying by $\delta d!^2G$ gives exactly



$$
\begin{aligned}
X={}&2iG A^*(1)A^*(\eta)(\delta s)\\
&-2i\delta\frac{G}{F!}A^*(\eta)E^*(1)
-\delta N\frac{G}{\ell_C}A^*(1)B^*(\eta).
\end{aligned}
$$



Every displayed integer quotient is integral.  Also $i$, $\eta$, and
$\delta s$ are algebraic integers; evaluating an integer polynomial at
$\eta$ preserves integrality.  Hence



$$
X\in\mathcal O_{\mathbb Q(s,i,\zeta)}.
$$



This proves the conditional algebraic-integer claim.

The qualification about effectivity is indispensable.  Bare algebraicity
of $s$ proves that some $\delta$ exists, but does not identify it or the
conjugate size



$$
S_\delta=\max_\tau|\tau(\delta s)|.
$$



The revised source now distinguishes this existential algebraic
denominator from the completely explicit Padé factor $d!^2G$.

For an embedding $\sigma$ of
$K_N=\mathbb Q(s,i,\zeta)$, one has



$$
\sigma(\zeta)=\zeta^a,\qquad
|\sigma(\eta)|=|1-\zeta^a|\leq2,\qquad
|\sigma(i)|=1.
$$



The restriction of $\sigma$ to $\mathbb Q(s)$ is among those used in
$S_\delta$.  Applying the coefficient bounds to the three summands of
$X$ gives exactly the quantity $\mathcal B$ in source equation (24).
No independence between the restrictions to the cyclotomic and $s$-fields
is assumed; taking maxima makes their possible coupling irrelevant.

If $X\ne0$, its norm is a nonzero rational integer.  Isolating the chosen
complex embedding and bounding all other embeddings by $\mathcal B$
therefore gives



$$
1\leq|\operatorname{Norm}_{K_N/\mathbb Q}(X)|
\leq|X|\mathcal B^{D_N-1}.
$$



Both certified nonvanishing and the strict inequality
$|X|\mathcal B^{D_N-1}<1$ are necessary for a contradiction.  A small
value at one complex embedding alone is insufficient.

## 6. Exact exponential remainder

At $z=1$ in corrected equation (2.12), the factor
$(1-z)^c$ has a zero of order $c$.  In the $c$-th derivative, only
the term in which all $c$ derivatives hit this factor survives.  The
outer and inner exponentials cancel, and after writing
$k=d+f+1+n$ the result is



$$
\frac{(-1)^c}{d!}
\sum_{n=0}^{\infty}
\frac{(n+d)!}{n!(n+d+f+1)!}.
$$



Expanding $e^t$ and using the beta integral gives



$$
R_{\exp}(1)=
\frac{(-1)^c}{d!f!}
\int_0^1t^d(1-t)^fe^t\,dt.
$$



The integral is positive.  Bounding $1\leq e^t\leq e$ and evaluating the
beta integral proves



$$
\frac1{(d+f+1)!}
\leq|R_{\exp}(1)|
\leq\frac e{(d+f+1)!}.
$$



Thus the individual exponential remainder is nonzero.  This fact does not
prove that the combined form $\Lambda$ is nonzero.

## 7. Exact logarithmic remainder

Let the integration variable in corrected equation (2.11) be $u$.
The reversed remainder is



$$
R_{\log}(x)=x^C L(1/x).
$$



Since



$$
(1/x-u)^{-(c+1)}
=x^{c+1}(1-xu)^{-(c+1)},
$$



specializing $x=\eta$ gives exactly



$$
\begin{aligned}
R_{\log}(\eta)
={}&\frac{(-1)^{c-1}\eta^{2c+d+1}}{d!f!}\\
&\times\int_0^1\int_0^\infty
\frac{u^c(1-u)^cy^f(1-uy)^d}
     {(1-\eta u)^{c+1}}e^{-y}\,dy\,du.
\end{aligned}
$$



For $\eta=1-\zeta$, the denominator traces the chord from $1$ to
$\zeta$:



$$
1-\eta u=(1-u)+u\zeta.
$$



The minimum distance of this chord from the origin is
$\cos(\pi/N)$, proving source equation (29).  Expanding
$(1+uy)^d$ after taking absolute values gives



$$
\int_0^1u^{c+r}(1-u)^c\,du
=\frac{(c+r)!c!}{(2c+r+1)!}
$$



and



$$
\int_0^\infty y^{f+r}e^{-y}\,dy=(f+r)!.
$$



These evaluations give exactly $\mathcal K$ in source equation (31) and
the bound



$$
|R_{\log}(\eta)|
\leq|\eta|^{2c+d+1}\mathcal K.
$$



Combining the two remainder bounds with
$X=\delta d!^2G\Lambda$ gives source equation (32), including its factor
$\delta d!G$.  Before height majorization,



$$
d!^2G\,A(\eta)R_{\exp}(1)
=(-1)^c\frac G{f!}A^*(\eta)
\int_0^1t^d(1-t)^fe^t\,dt,
$$



and the logarithmic term has the same factor $G/f!$.  Since
$F!=(f+2c)!\mid G$, the factorially small analytic remainder is coupled
to factorial arithmetic clearing exactly as the source states.

## 8. Cyclotomic norm and field degree

Since



$$
\Phi_N(T)=
\prod_{a\in(\mathbb Z/N\mathbb Z)^\times}(T-\zeta^a),
$$



evaluation at $T=1$ gives



$$
\operatorname{Norm}_{\mathbb Q(\zeta)/\mathbb Q}(1-\zeta)
=\Phi_N(1).
$$



The elementary value is



$$
\Phi_N(1)=
\begin{cases}
p,&N=p^r,\\
1,&N>1\text{ is not a prime power}.
\end{cases}
$$



For $N=p^r$, this follows from the geometric-sum expression for
$\Phi_{p^r}$.  If $N$ has at least two prime divisors, the standard
cyclotomic identities
$\Phi_{pm}(x)=\Phi_m(x^p)/\Phi_m(x)$, after separating the full
$p$-power, give the value $1$ at $x=1$.

Writing $\rho=|1-\zeta|$ and $M=2c+d+1$, taking moduli and isolating the
distinguished embedding gives



$$
\prod_{a\ne1}|1-\zeta^a|^M
=\frac{\Phi_N(1)^M}{\rho^M}.
$$



For the full conditional field $K_N$, the relative norm of
$\eta\in\mathbb Q(\zeta)$ is
$\eta^{[K_N:\mathbb Q(\zeta)]}$.  The norm tower therefore gives



$$
\prod_{\sigma:K_N\hookrightarrow\mathbb C}|\sigma(\eta)|^M
=\Phi_N(1)^{M[K_N:\mathbb Q(\zeta)]}.
$$



No assumption that $K_N/\mathbb Q$ is Galois is needed.

Thus the small factor $\rho^M$ is exactly compensated at other primitive
cyclotomic embeddings when $N$ is not a prime power, and is
overcompensated by $p^M$ for a prime power.  This is a theorem about the
isolated cyclotomic factor.  Since $X$ is an additive combination, it is
not a factorization or lower bound for $\operatorname{Norm}(X)$.

For the degree statement, put



$$
h=[\mathbb Q(s):\mathbb Q],\qquad F_s=\mathbb Q(s,i).
$$



Because $\mathbb Q(\zeta)/\mathbb Q$ is Galois,



$$
[F_s(\zeta):F_s]
=\frac{\varphi(N)}
       {[F_s\cap\mathbb Q(\zeta):\mathbb Q]}.
$$



The intersection degree is at most
$[F_s:\mathbb Q]\leq2h$, giving



$$
[F_s(\zeta):F_s]\geq\frac{\varphi(N)}{2h}.
$$



Adjoining the fixed hypothetical algebraic number $s$ therefore cannot
remove the growth in the number of cyclotomic embeddings.

## 9. Branch and Galois restrictions

For $N\geq7$,



$$
|\eta|=2\sin(\pi/N)<1.
$$



The Taylor branch of $\log(1-x)$ at $x=0$ is therefore valid at
$\eta$.  Because $2\pi/N\in(0,\pi)$,



$$
\log(1-\eta)=\log\zeta=\frac{2\pi i}{N}
$$



on this branch.

For a general primitive conjugate
$\eta_a=1-\zeta^a$, $|\eta_a|$ may exceed $1$, so the Taylor
evaluation need not apply.  Analytic continuation would introduce
branch-dependent representatives of $\log(\zeta^a)$.  More fundamentally,
an algebraic embedding sends the hypothetical algebraic number $s$ to an
algebraic conjugate.  It has no analytic action that separately sends the
transcendental constants $e$ and $\pi$ while preserving their original
functional interpretation.  Thus one may not apply the distinguished
analytic remainder estimate independently at every $\eta_a$ and call the
results the conjugates of $X$.  Equations (23)--(24), derived purely from
the algebraic expression (22), are the legitimate all-conjugate bound.

## 10. Nonvanishing and alternative substitutions

Since $\mathbb Q(\eta)=\mathbb Q(\zeta)$, the algebraic degree of
$\eta$ is $\varphi(N)$.  Therefore



$$
\varphi(N)>C\quad\Longrightarrow\quad A(\eta)\ne0.
$$



This does not control $A(1)$.  At the admissible triple
$(c,d,f)=(0,1,0)$, direct calculation gives



$$
A(x)=x-1,\qquad A(1)=0.
$$



Even when $A(1)A(\eta)\ne0$, one has



$$
X=0
\quad\Longleftrightarrow\quad
s=\frac{E(1)}{A(1)}
 +\frac{NB(\eta)}{2iA(\eta)}.
$$



The right side is algebraic.  This equality is entirely compatible with
the hypothesis that $s$ is algebraic.  The corrected theorem supplies no
determinant or adjacent-parameter relation excluding it.  The nonzero
individual exponential remainder cannot exclude cancellation against the
complex logarithmic remainder.

Two provably distinct right sides can ensure that at least one of two forms
is nonzero, but the strict global norm inequality must still be proved for
the form that is nonzero.  This finite device does not repair the global
height problem.

The discussion of alternative substitutions also checks:

- original $z=2$ gives $e^{1/2}$ and $-\log2$;
- reversed $x=2$, after a chosen analytic continuation, gives $e^2$
  and $\log(-1)=i\pi$, but lies beyond the Taylor singularity, while the
  reversed logarithmic integral has a pole at $u=1/2$;
- replacing only $e^x$ by $e^{x/2}$ is not obtained by a common
  substitution in corrected Theorem 3, since the same change also replaces
  $\log(1-x)$ by $\log(1-x/2)$.

The withdrawn published Theorem 4 cannot supply the missing independently
scaled theorem.

## 11. Independent finite corroboration

No branch-specific verifier or result file was present in the archive, so I
constructed the checks independently rather than relying on the reported
output.

For all 125 triples



$$
0\leq c\leq4,\qquad
2c\leq d\leq2c+4,\qquad
c\leq f\leq c+4,
$$



exact rational arithmetic verified:

- the reversed coefficient formula;
- every zero coefficient required by both orders in equation (8);
- the degree bounds for $B$ and $E$;
- integrality of $d!A$, $d!\ell_CB$, and $d!F!E$;
- the constant coefficient of $A$;
- the exponential integral (26), represented exactly as a rational
  coefficient of $e$ plus a rational constant.

Five independent 80-digit quadrature checks of the logarithmic integral,
including $c=0$ and $c=4$, agreed with direct polynomial evaluation to
absolute errors between approximately $10^{-77}$ and $10^{-81}$, and
each satisfied the rigorous majorant (30)--(31).

An independent scan of the same 4,212 cases reported in the source
reproduced:

- no $c\geq1$ cleared distinguished value below $1$;
- minimum $42.4557426546\ldots$ in that class at
  $(c,d,f,N)=(1,2,1,10)$;
- exactly two $c=0$ values below $1$;
- minimum $0.2066736904\ldots$ at $(0,2,1,20)$;
- strict increase of the base-10 cleared magnitude along
  $d=2c,f=c$, $1\leq c\leq12$, for
  $N=7,10,20,100$.

These computations are corroboration only.  None is used to establish an
all-parameter identity, nonvanishing theorem, or asymptotic no-go result.

## 12. Final logical scope

The revised source rigorously proves or records the following:

- the formal specialization of corrected Theorem 3 at the two selected
  points;
- exact Padé denominator clearing and coefficient bounds;
- a conditional algebraic integer after an existential choice of
  $\delta$;
- exact local integral formulas and distinguished-place bounds;
- the necessary norm inequality if $X\ne0$;
- exact compensation of the isolated root-of-unity factor over all
  cyclotomic embeddings;
- growth of the cyclotomic extension degree; and
- the absence, in the cited theorem, of the nonvanishing input needed for a
  contradiction.

It does not prove:

- an effective $\delta$, minimal polynomial, or conjugate house for the
  hypothetical algebraic number $s$;
- nonvanishing of $X$ for an infinite parameter family;
- the strict inequality $|X|\mathcal B^{D_N-1}<1$;
- that the norm of the full additive $X$ is large merely because the norm
  of $\eta^M$ is at least $1$;
- an impossibility theorem for all refined cyclotomic combinations; or
- any algebraicity, irrationality, or transcendence statement about
  $e+\pi$.

Subject to these explicit limitations and to the source-status caveat for
the author-corrected Theorem 3, the revised checkpoint is accepted.
