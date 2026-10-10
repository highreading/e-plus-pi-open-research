> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Root-of-unity specialization of Rivoal's exponential--logarithm Padé forms

Checked: 2026-08-26 UTC

## Verdict

The specialization is mathematically well defined, after using the
author-corrected version of Theorem 3 and not the misprinted 2015 statement.
For $N\geq 7$, put



$$
\zeta=\exp(2\pi i/N),\qquad \eta=1-\zeta .
$$



Then $|\eta|<1$ and the Taylor branch gives



$$
\log(1-\eta)=\log\zeta=\frac{2\pi i}{N}.                 \tag{1}
$$



Evaluating the corrected Padé exponential form at $1$, the logarithmic
form at $\eta$, and cross-multiplying their denominator polynomials does
produce, under



$$
s=e+\pi\in\overline{\mathbb Q},          \tag{H}
$$



and after choosing an integer $\delta>0$ for which $\delta s$ is
integral, a conditional algebraic integer $X$.  The Padé denominator
factor $d!^2G$ is completely explicit; bare (H) gives only the existence
of $\delta$ and does not effectively determine $\delta$, the minimal
polynomial of $s$, or the house $S_\delta$.  This is the positive
result.

It does **not** prove (H), or contradict (H), for two independent and
rigorous reasons.

1. The corrected theorem supplies no nonvanishing result for $X$.  Its
   vanishing would merely say that the hypothetical algebraic number $s$
   equals one particular algebraic Padé approximant.  The source has no
   determinant theorem excluding this.
2. Even conditional on $X\ne0$, the small distinguished factor
   $|1-\zeta|^M$, $M=2c+d+1$, is not a global product-formula gain:

   

$$
\prod_{a\in(\mathbb Z/N\mathbb Z)^\times}
       |1-\zeta^a|^M=\Phi_N(1)^M
       =
       \begin{cases}
        p^M,&N=p^r,\\
        1,&N\text{ has at least two distinct prime factors}.
       \end{cases}                                        \tag{2}
$$



   Thus the local gain is exactly paid back by the other cyclotomic
   conjugates when $N$ is not a prime power, and is globally adverse for a
   prime power.  The remaining exponential remainder also incurs the
   factorial denominator clearing displayed below.

Consequently, this construction is a valid conditional algebraic-form
reduction, but the primary theorem and the displayed conditional estimates below do not
yield a parameter regime satisfying both certified nonvanishing and the
strict norm inequality required for a contradiction.

## 1. Primary source and the correction that must be used

The published source is:

T. Rivoal, “Simultaneous Padé approximants to the Euler, exponential and
logarithmic functions,” *Journal de Théorie des Nombres de Bordeaux* 27
(2015), no. 2, 565--589,
[DOI 10.5802/jtnb.914](https://jtnb.centre-mersenne.org/articles/10.5802/jtnb.914/).

The relevant authoritative correction is Rivoal's
[author-maintained April 2021 manuscript](https://rivoal.perso.math.cnrs.fr/articles/explog.pdf).
Its page 5 says that misprints in the published paper were corrected,
especially in Theorem 3.  Its footnote on page 7 says that the published
Theorem 4 had another misprint and was removed after correction because the
corrected result had little practical interest.

This matters here:

- printed Theorem 3 says $c\geq d$, whereas corrected Theorem 3 requires
  $d\geq2c$ and $f\geq c$;
- the printed exponential identity has different powers from the corrected
  identity;
- printed formula (2.18), used for printed Theorem 4, even contains an
  undefined exponent $n$;
- the theorem numbered 4 later in the corrected manuscript is a different
  theorem, concerning the logarithm and Euler's divergent series, not the
  printed simultaneous $\exp/\log$ construction.

Accordingly, no claim below uses printed Theorem 4.  The two source files
used during this audit had SHA-256 digests

    936877cc2a199163e1301c0e73abf8ba1cf2f58f878a9f05292aa33bb387dc3d  published PDF
    fefdfc7dbca65c33ffc83c2d1d88b798af1f0d43ec53c412b1dfad6552b642c9  author-corrected PDF

Residual source caveat: the 2021 file is an author-maintained corrected
manuscript, not a separately published journal erratum, and it says that the
proof of Theorem 3 is similar to the preceding proofs and omits it.  This
audit therefore cites the corrected primary statement exactly and checks its
formal consequences independently; the finite checks in Section 10 are not
presented as a substitute for a general proof of Rivoal's theorem.

## 2. Corrected Theorem 3, reversed to the origin

Let $c,d,f$ be nonnegative integers satisfying



$$
d\geq2c,\qquad f\geq c.            \tag{3}
$$



The polynomial in corrected equation (2.13) is



$$
P(z)=
 \sum_{j=0}^{d}\sum_{k=0}^{c}
 (-1)^{d-j+k}
 \binom ck
 \binom{c+d-j+k}{c}
 \binom{d+f-j}{f}
 \frac{z^{d-j+k}}{j!}.                                    \tag{4}
$$



Corrected Theorem 3 states that there are polynomials $Q_1,Q_2$, of
respective degrees at most $c+d$ and $2c+f$, for which



$$
\begin{aligned}
 P(z)\log(1-1/z)-Q_1(z)&=O(z^{-c-1}),\\
 P(z)e^{1/z}-z^{d-f-c}Q_2(z)&=O(z^{-(f-c+1)})
 \end{aligned}                                             \tag{5}
$$



at infinity.  Set



$$
C=c+d,\qquad F=f+2c                                      \tag{6}
$$



and reverse the three polynomials:



$$
A(x)=x^C P(1/x),\quad
 B(x)=x^C Q_1(1/x),\quad
 E(x)=x^F Q_2(1/x).                                       \tag{7}
$$



Then (5) becomes the simultaneous pair at the origin



$$
\begin{aligned}
 R_{\log}(x)&=A(x)\log(1-x)-B(x)
              =O(x^{2c+d+1}),\\
 R_{\exp}(x)&=A(x)e^x-E(x)
              =O(x^{f+d+1}).
 \end{aligned}                                             \tag{8}
$$



Here



$$
[x^m]A=
 \sum_{\substack{0\leq j\leq d,\ 0\leq k\leq c\\c+j-k=m}}
 (-1)^{d-j+k}
 \binom ck\binom{c+d-j+k}{c}\binom{d+f-j}{f}\frac1{j!}.
                                                               \tag{9}
$$



In particular,



$$
[x^0]A=(-1)^{c+d}
          \binom{d+2c}{c}\binom{d+f}{f}\ne0,                \tag{10}
$$



so $A$ is not the zero polynomial.

Equation (8), rather than an informal appeal to a rescaled theorem, is what
justifies viewing the construction as a pair



$$
e^z,\qquad \log(1-\eta z)
$$



at $z=1$: use the first identity in (8) at $x=\eta z$ and
the second at $x=z$.

## 3. Exact denominator clearing

Write



$$
\ell_r=\operatorname{lcm}(1,2,\ldots,r),\qquad \ell_0=1.
$$



The coefficient formula (9) immediately gives



$$
A^*=d!A\in\mathbb Z[x].            \tag{11}
$$



Because $2c+d+1>C$, the polynomial $B$ is exactly the truncation
through degree $C$ of $A(x)\log(1-x)$.  Thus, if
$A(x)=\sum_m a_mx^m$, then



$$
[x^n]B=-\sum_{m=0}^{n-1}\frac{a_m}{n-m}\quad(0\leq n\leq C),
$$



and consequently



$$
B^*=d!\ell_C B\in\mathbb Z[x].     \tag{12}
$$



Similarly, $f+d+1>F$ follows from $d\geq2c$.  Hence $E$ is the
truncation through degree $F$ of $A(x)e^x$, so



$$
[x^n]E=\sum_{m=0}^{n}\frac{a_m}{(n-m)!}\quad(0\leq n\leq F)
$$



and



$$
E^*=d!F!E\in\mathbb Z[x].          \tag{13}
$$



A safe common clearing factor is therefore



$$
G=\operatorname{lcm}(\ell_C,F!),\qquad
 \mathcal D=d!^2G.                                         \tag{14}
$$



This is a certified common denominator; it is not asserted to be the least
common denominator for every parameter triple.

## 4. Explicit coefficient and conjugate-height bounds

There is no ambiguity about the finite coefficient heights.  With
$a_m^*=d![x^m]A$, the exact integer heights are



$$
\begin{aligned}
 H(A^*)&=\max_{0\leq m\leq C}|a_m^*|,\\
 H(B^*)&=\max_{0\leq n\leq C}
 \left|\ell_C\sum_{m=0}^{n-1}\frac{a_m^*}{n-m}\right|,\\
 H(E^*)&=\max_{0\leq n\leq F}
 \left|F!\sum_{m=0}^{\min(n,C)}
                    \frac{a_m^*}{(n-m)!}\right|.
 \end{aligned}                                             \tag{14a}
$$



Together with (9), these are finite exact formulas in $c,d,f$, not
asymptotic descriptions.  For uniform all-parameter estimates, define



$$
H_0=d!(c+1)(d+1)2^c
      \binom{d+2c}{c}\binom{d+f}{f}.                       \tag{15}
$$



Termwise use of (9) gives the deliberately safe bounds



$$
\begin{aligned}
 H(A^*)&\leq H_0,\\
 H(B^*)&\leq \ell_C H_0\,\mathcal H_C,\\
 H(E^*)&<eF!H_0<3F!H_0,
 \end{aligned}                                             \tag{16}
$$



where $\mathcal H_C=\sum_{r=1}^C1/r$, with
$\mathcal H_0=0$.  The first bound uses $d!/j!\leq d!$, the binomial
maxima visible in (9), $\binom ck\leq2^c$, and at most
$(c+1)(d+1)$ summands.  The second follows from the displayed convolution
for $B$, and the third from
$\sum_{r=0}^F1/r!<e$.

For any primitive cyclotomic conjugate
$\eta_a=1-\zeta^a$, one has $|\eta_a|\leq2$.  It follows that



$$
\begin{aligned}
 |A^*(\eta_a)|&\leq U_A:=(C+1)2^C H_0,\\
 |B^*(\eta_a)|&\leq U_B:=(C+1)2^C\ell_C H_0\mathcal H_C,\\
 |A^*(1)|&\leq V_A:=(C+1)H_0,\\
 |E^*(1)|&<V_E:=3(F+1)F!H_0.
 \end{aligned}                                             \tag{17}
$$



In Weil-height language, since $\eta$ is an algebraic integer and
$h(\eta)\leq\log2$,



$$
h(A^*(\eta))
 \leq\log(C+1)+\log H_0+C\log2.                            \tag{18}
$$



Thus the root-of-unity substitution does not have hidden coefficient
denominators.  Its cost appears instead in the conjugates and in the degree
of the cyclotomic field.

## 5. The conditional algebraic integer

Use (8) at $x=1$ for the exponential and at $x=\eta$ for the logarithm.
By (1), define



$$
\Lambda=
 2iA(\eta)R_{\exp}(1)+NA(1)R_{\log}(\eta).                 \tag{19}
$$



Expanding the two remainders gives the exact cancellation of $e$ and
$\pi$ into their sum:



$$
\Lambda=
 2iA(1)A(\eta)s-2iA(\eta)E(1)-NA(1)B(\eta).                \tag{20}
$$



Under (H), choose a positive integer $\delta$ such that
$\delta s$ is an algebraic integer, and let



$$
K_N=\mathbb Q(s,i,\zeta).
$$



Equations (11)--(14) show that



$$
X:=\delta d!^2G\Lambda\in\mathcal O_{K_N},                \tag{21}
$$



more explicitly



$$
\begin{aligned}
 X={}&2iG A^*(1)A^*(\eta)(\delta s)\\
    &-2i\delta\frac{G}{F!}A^*(\eta)E^*(1)
      -\delta N\frac{G}{\ell_C}A^*(1)B^*(\eta).
 \end{aligned}                                             \tag{22}
$$



This proves the arithmetic well-definedness of the proposed specialization.

If $D_N=[K_N:\mathbb Q]$ and



$$
S_\delta=\max_{\sigma:\mathbb Q(s)\hookrightarrow\mathbb C}
                 |\sigma(\delta s)|,
$$



then every embedding of $K_N$ satisfies, by (17),



$$
|\sigma X|\leq\mathcal B,                                 \tag{23}
$$



where



$$
\mathcal B=
 2GV_AU_AS_\delta
 +2\delta\frac{G}{F!}U_AV_E
 +\delta N\frac{G}{\ell_C}V_AU_B.                          \tag{24}
$$



The bound $\mathcal B$ is explicit once $\delta$ and the conjugates of
$\delta s$ are specified.  Under bare (H), it is a fixed but ineffective
conditional constant because $S_\delta$ is unknown.

Therefore, **if $X\ne0$**, the product formula gives



$$
1\leq |\operatorname{Norm}_{K_N/\mathbb Q}(X)|
 \leq |X|\,\mathcal B^{D_N-1}.                             \tag{25}
$$



A contradiction requires a rigorous strict upper bound
$|X|\mathcal B^{D_N-1}<1$, not merely a small complex remainder at the
distinguished embedding.

## 6. Exact local remainders

The corrected source's equations (2.11)--(2.12), after reversal, give at
$x=1$



$$
R_{\exp}(1)=
 \frac{(-1)^c}{d!f!}
 \int_0^1t^d(1-t)^f e^t\,dt.                              \tag{26}
$$



For clarity, this is also a direct check on the corrected power in (5).
At $z=1$ in corrected equation (2.12), only the term in which all $c$
derivatives hit $(1-z)^c$ survives.  After writing
$k=d+f+1+n$, the resulting series is



$$
\frac{(-1)^c}{d!}
 \sum_{n=0}^{\infty}\frac{(n+d)!}{n!(n+d+f+1)!},
$$



which is (26) after expanding $e^t$ and evaluating the beta integrals.

In particular this remainder is nonzero and



$$
\frac1{(d+f+1)!}
 \leq |R_{\exp}(1)|
 \leq\frac e{(d+f+1)!}.                                   \tag{27}
$$



Reversing the double integral in corrected equation (2.11) gives



$$
\begin{aligned}
 R_{\log}(\eta)
 ={}&\frac{(-1)^{c-1}\eta^{2c+d+1}}{d!f!}\\
 &\times
 \int_0^1\int_0^\infty
 \frac{u^c(1-u)^c y^f(1-uy)^d}
      {(1-\eta u)^{c+1}}e^{-y}\,dy\,du.                    \tag{28}
 \end{aligned}
$$



For the distinguished root,



$$
|1-\eta u|=|(1-u)+u\zeta|\geq\cos(\pi/N)
 \quad(0\leq u\leq1).                                     \tag{29}
$$



Using $|1-uy|^d\leq(1+uy)^d$, expanding, and evaluating the beta and
gamma integrals yields



$$
|R_{\log}(\eta)|\leq|\eta|^{2c+d+1}\mathcal K,            \tag{30}
$$



where



$$
\mathcal K=
 \frac{\sec^{c+1}(\pi/N)}{d!f!}
 \sum_{r=0}^{d}\binom dr
 \frac{(f+r)!(c+r)!c!}{(2c+r+1)!}.                         \tag{31}
$$



Combining (19), (27), and (30) gives the following distinguished-place
bound, explicit in $c,d,f,N$ once $\delta$ has been chosen:



$$
|X|\leq
 \delta d!G\left(
 \frac{2eU_A}{(d+f+1)!}
 +NV_A|\eta|^{2c+d+1}\mathcal K
 \right).                                                  \tag{32}
$$



The denominator/remainder balance is clearer before replacing coefficients
by heights:



$$
\begin{aligned}
 d!^2G\,A(\eta)R_{\exp}(1)
 &=(-1)^c\frac G{f!}A^*(\eta)
   \int_0^1t^d(1-t)^fe^t\,dt,\\
 d!^2G\,A(1)R_{\log}(\eta)
 &=(-1)^{c-1}\frac G{f!}A^*(1)\eta^{2c+d+1}\mathcal I,
 \end{aligned}                                             \tag{33}
$$



with $\mathcal I$ the double integral in (28).  Since
$G$ is a multiple of $F!=(f+2c)!$, the factorially small unscaled
remainders cannot be separated from the factorial arithmetic clearing.

## 7. The cyclotomic norm barrier

The exact identity



$$
\operatorname{Norm}_{\mathbb Q(\zeta)/\mathbb Q}(1-\zeta)
 =\prod_{a\in(\mathbb Z/N\mathbb Z)^\times}(1-\zeta^a)
 =\Phi_N(1)                                                \tag{34}
$$



follows simply by evaluating the cyclotomic polynomial at $1$.  The
standard elementary evaluation is



$$
\Phi_N(1)=
 \begin{cases}
 p,&N=p^r,\\
 1,&N>1\text{ is not a prime power}.
 \end{cases}                                               \tag{35}
$$



Let $\rho=|1-\zeta|=2\sin(\pi/N)$ and $M=2c+d+1$.  Isolating the
distinguished factor in (34) gives



$$
\prod_{\substack{a\in(\mathbb Z/N\mathbb Z)^\times\\a\ne1}}
 |1-\zeta^a|^M
 =\frac{\Phi_N(1)^M}{\rho^M}.                              \tag{36}
$$



The same accounting holds in the full conditional field.  By the tower
formula for norms,



$$
\prod_{\sigma:K_N\hookrightarrow\mathbb C}|\sigma(\eta)|^M
 =\Phi_N(1)^{M[K_N:\mathbb Q(\zeta)]}.                     \tag{36a}
$$



Thus taking $N$ large makes one logarithmic remainder spectacularly
small, but forces reciprocal growth among the other cyclotomic conjugates.
For non-prime-powers the product is exactly neutral; for prime powers it
has the additional adverse factor $p^M$.  This statement concerns the
cyclotomic factor itself; it does not rule out accidental cancellation
between the two summands in (19), and no such cancellation is claimed.

Growing $N$ also grows the number of embeddings.  If
$h=[\mathbb Q(s):\mathbb Q]$ and $F_s=\mathbb Q(s,i)$, then



$$
[F_s(\zeta):F_s]
 =[\mathbb Q(\zeta):F_s\cap\mathbb Q(\zeta)]
 \geq\frac{\varphi(N)}{2h}.                                \tag{37}
$$



Therefore the many-conjugate cost cannot be removed by adjoining the fixed
hypothetical number $s$.

There is also a logical trap here.  One may use the analytic estimate (30)
at the distinguished embedding.  One may **not** assert the same estimate
with $\eta$ replaced by every $\eta_a$ and simultaneously regard those
values as the Galois conjugates of (20): an embedding sends the hypothetical
algebraic $s$ to one of its algebraic conjugates, whereas it does not send
the transcendental pair $(e,\pi)$ analytically.  The legitimate
all-conjugate estimate is the algebraic coefficient bound (23)--(24).

## 8. Nonvanishing is not supplied

The polynomial $A$ is nonzero by (10).  Moreover, if
$\varphi(N)>C$, then $A(\eta)\ne0$, since $\eta$ has degree
$\varphi(N)$ and $\deg A\leq C$.

That does not settle all coefficient degeneracies.  For example, the
admissible triple



$$
(c,d,f)=(0,1,0)
$$



has $A(x)=x-1$, hence $A(1)=0$.  More importantly, even when
$A(1)A(\eta)\ne0$, equation $X=0$ is equivalent under (H) to



$$
s=\frac{E(1)}{A(1)}
   +\frac{N B(\eta)}{2iA(\eta)},                            \tag{38}
$$



an equality between algebraic numbers.  It creates no contradiction with
(H).  Corrected Theorem 3 gives neither a determinant for a sequence of
such approximants nor an all-parameter statement excluding (38).

One can in principle compare two explicitly distinct right sides of (38)
to ensure that at least one of the corresponding forms is nonzero.  That
finite device does not alter the product-formula requirement (25), and the
source supplies no adjacent-parameter determinant whose size could be
combined with (32).  Accordingly, nonvanishing must not be silently
imported from the nonzero individual remainder (26): $\Lambda$ is a sum
of two remainders and can cancel.

## 9. Why $z=2$ and one-sided scaling do not repair the construction

There are three distinct substitutions, none of which gives the desired
small algebraic-integer form.

1. In the original variable of corrected Theorem 3, $z=2$ produces
   $e^{1/2}$ and $\log(1/2)=-\log2$, not $e$ and $\pi$.
2. In the reversed identities (8), $x=2$ produces $e^2$ and, after
   analytic continuation around $x=1$,
   $\log(1-2)=\log(-1)=i\pi$.  Combining this log identity with the
   exponential identity at $x=1$ does algebraically isolate $e+\pi$:

   

$$
iA(2)R_{\exp}(1)+A(1)R_{\log}(2)
   =iA(1)A(2)s-iA(2)E(1)-A(1)B(2).                         \tag{39}
$$



   But $x=2$ lies outside the Taylor disk and beyond the singularity at
   $x=1$.  The local order in (8) supplies no smallness there; its formal
   factor $2^{2c+d+1}$ grows.  The integral (28) has a pole at $u=1/2$
   for $\eta=2$, so the bound (29)--(31) is unavailable without a separate
   analytic-continuation analysis.
3. Replacing only $e^x$ by $e^{x/2}$, while retaining
   $\log(1-x)$, is not a substitution in corrected Theorem 3.  The change
   $x\mapsto x/2$ changes both members to
   $e^{x/2}$ and $\log(1-x/2)$.  A construction that scales only one
   function would require a new Padé theorem.  The withdrawn printed
   Theorem 4 cannot be used to supply it.

## 10. Exact and numerical checks

An independent exact-rational reconstruction was run for all 125 triples



$$
0\leq c\leq4,\quad 2c\leq d\leq2c+4,\quad c\leq f\leq c+4.
$$



For every triple it verified:

- the coefficient formula (9);
- all zero coefficients required by both orders in (8);
- the degree bounds for $B,E$;
- integrality of $d!A$, $d!\ell_CB$, and $d!F!E$.

The regenerated exact check reported:

    CORRECTED_THEOREM3_FORMAL_DENOMINATOR_AND_EXP_INTEGRAL_PASS 125

Numerical quadrature independently checked (26) and (28)--(31) on sample
triples.  A finite scan over



$$
c\leq8,\quad 2c\leq d\leq2c+8,\quad c\leq f\leq c+12,
 \quad N\in\{7,10,20,100\}
$$



comprised 4,212 cases.  For the natural clearing $d!^2G$ (that is,
$\delta=1$), it found no $c\geq1$ distinguished value below $1$;
the minimum in that class was approximately $42.45574265$, at
$(c,d,f,N)=(1,2,1,10)$.  Exactly two $c=0$ values were below $1$;
the smallest was approximately $0.2066736904$, at $(0,2,1,20)$, and
it did not meet the nonvanishing and all-conjugate norm criterion.  Along
the ray $d=2c,f=c$, the base-10 logarithm of the cleared local magnitude
was strictly increasing in the tested range $1\leq c\leq12$, for each
listed $N$.

These finite computations are diagnostics only.  The negative verdict rests
on the exact source correction, the conditional nonvanishing gap, the
necessary norm inequality (25), and the exact cyclotomic balance (34)--(36),
not on extrapolation from the scan.

## Conclusion

Rivoal's corrected Theorem 3 does support the proposed root-of-unity
specialization and yields the conditional algebraic integer (21)--(22),
explicit relative to a choice of $\delta$.  The Padé clearing $d!^2G$,
coefficient heights, local remainders, and conjugate formulas are exact; no
effective $\delta$ or $S_\delta$ follows from bare (H).  The method
does not currently decide whether $e+\pi$ is algebraic or transcendental:
the combined form lacks certified nonvanishing, and the apparent
$|1-\zeta_N|^M$ gain is neutral or adverse after the cyclotomic product
formula.  Direct $z=2$ and one-sided scaling do not evade those defects.
