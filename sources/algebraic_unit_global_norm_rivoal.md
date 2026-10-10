> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Algebraic-unit and two-conjugate-log tests for the corrected Rivoal forms

Checked: 2026-08-26 UTC

## Verdict

Let $A,B,E$ be the reversed polynomials in the accepted audit of
Rivoal's corrected simultaneous exponential--logarithm construction, and
put



$$
C=c+d,\qquad M=2c+d+1=C+c+1,\qquad F=f+2c,
 \tag{1}
$$



where $d\geq2c$ and $f\geq c$.  Thus



$$
R_{\exp}(x)=A(x)e^x-E(x),\qquad
 R_{\log}(x)=A(x)\operatorname {Log}(1-x)-B(x).
 \tag{2}
$$



This note answers the proposed algebraic-unit escape in three layers.

1. **A single algebraic logarithm gives no new parameter.**  If an
   algebraic multiplier converts $\operatorname {Log}(1-\eta)$ into
   $\pi$, then Gelfond--Schneider forces $1-\eta$ to be a root of
   unity.  Hence the single-log specialization is already the cyclotomic
   specialization $\eta=1-\zeta$.  In particular a real Pisot or Salem
   unit, or its inverse at a small real embedding, cannot isolate
   $e+\pi$ in this construction.

2. **The substitution factor of an algebraic unit is globally neutral.**
   If $q\eta$ is an algebraic integer, then the exact archimedean product
   of the degree-$C$-cleared leading factor is

   

$$
\prod_{\sigma:K\hookrightarrow\mathbb C}
    \left|bq^C\sigma(\eta)^M\right|
   =b^{[K:\mathbb Q]}
     \frac{|N_{K/\mathbb Q}(q\eta)|^M}
          {q^{[K:\mathbb Q](M-C)}}.
   \tag{3}
$$



   For an algebraic-integer unit $\eta$, this is exactly
   $b^{[K:\mathbb Q]}\geq1$.  A small Pisot/Salem embedding is paid for
   by its other embeddings.  Integral nonunits are adverse.  A
   nonintegral parameter can leave the formal denominator factor
   $q^{-[K:\mathbb Q](c+1)}$, but target compatibility rules it out:
   every single-log parameter for $\pi$ is $1-\zeta$, hence integral.

3. **There is a genuine two-log algebraic extension, but it does not evade
   the global obstruction on its sharpest elementary edge.**  If

   

$$
\frac{1-\eta}{1-\overline\eta}
   \quad\hbox{is a root of unity},
   \tag{4}
$$



   the real logarithms at $\eta$ and $\overline\eta$ cancel.  This
   gives an exact three-remainder form for $e+\pi$, displayed in (20).
   There is an infinite nontrivial unit family: for every odd $n\geq5$,

   

$$
\xi=\zeta_n,\qquad \eta=\frac1{1+\xi},\qquad
   \overline\eta=1-\eta,
   \tag{5}
$$



   and $\eta$ is a cyclotomic unit with
   $|\eta|=(2\cos(\pi/n))^{-1}<1$.  The source of $\pi$ is still the
   root-of-unity quotient $\overline\eta/\eta=\xi$; the radial unit is a
   new Padé evaluation parameter, not a new logarithmic identity.

   On the admissible edge $c=f=0$, $d\to\infty$, the distinguished
   two-log form is eventually nonzero and is locally exponentially small:

   

$$
|\Lambda_{n,d}|\asymp_n
      \frac{|\eta|^d}{d}.
   \tag{6}
$$



   Thus this is a genuine new local form and must not be dismissed by the
   single-log argument.  Nevertheless, when the coefficient field
   $L_n=\mathbb Q(\zeta_n,i)$ is disjoint from the hypothetical
   $\mathbb Q(e+\pi)$, its full relative norm already grows before any
   denominator clearing:

   

$$
\prod_{\sigma:L_n\hookrightarrow\mathbb C}
       |\sigma(\Lambda_{n,d})|
    \asymp_n B_n^d d^{-2(1+|\mathcal T_n|)},\qquad B_n>1.
   \tag{7}
$$



   The exact sets and base are given in (40)--(42).  For $n=5$,

   

$$
B_5=\left(\frac{1+\sqrt5}{2}\right)^2,
      \qquad
      \prod_\sigma|\sigma(\Lambda_{5,d})|
      \asymp \left(\frac{1+\sqrt5}{2}\right)^{2d}d^{-6}.
   \tag{8}
$$



   Every positive-integer rational-denominator clearing only increases this
   relative product.  A subsequent division by a common
   algebraic coordinate factor is a different operation and would require
   an independent all-degree content theorem.  Section 8 gives an exact
   ideal-content computation through $d=200$ for $n=5$, but no
   all-degree bound is assumed here.  If
   the coefficient field intersects
   $\mathbb Q(e+\pi)$, some coefficient-field maps necessarily move the
   hypothetical number to uncontrolled conjugates, so (7) is no longer a
   relative norm fixing the distinguished value; this is an
   all-conjugate-control gap, not a contraction.

The results distinguish three logically different requirements.  The
two-log family has certified local smallness and eventual local
nonvanishing on (6).  It has no global norm contraction on that edge in the
disjoint-field case.  No all-parameter theorem about every two-log degree
sequence is claimed, and no bound for unknown conjugates of a hypothetical
algebraic $e+\pi$ is imported.  Nothing here proves either algebraicity or
transcendence of $e+\pi$.

## 1. Corrected Padé data and exact rational clearing

The accepted source audit proves



$$
d!A\in\mathbb Z[x],\qquad
 d!\ell_C B\in\mathbb Z[x],\qquad
 d!F!E\in\mathbb Z[x],
 \tag{9}
$$



where $\ell_C=\operatorname {lcm}(1,\ldots,C)$, with $\ell_0=1$.
The two remainder orders are



$$
R_{\log}(x)=O(x^M),\qquad
 R_{\exp}(x)=O(x^{d+f+1}).
 \tag{10}
$$



The logarithmic identity is continued on
$\mathbb C\setminus[1,\infty)$ by the exact integral



$$
R_{\log}(x)=(-1)^{c-1}x^M
 \int_0^1
 \frac{u^c(1-u)^cH_{d,f}(u)}{(1-xu)^{c+1}}\,du,
 \tag{11}
$$



where



$$
H_{d,f}(u)=\sum_{r=0}^d(-1)^r
 \binom{f+r}{f}\frac{u^r}{(d-r)!}.
 \tag{12}
$$



In particular, if $|x|<1$, (11) is an ordinary absolutely convergent
integral and its explicit leading factor is $x^M$.

## 2. One logarithm: target compatibility forces a root of unity

The following elementary consequence of Gelfond--Schneider closes the
single-log algebraic-unit proposal.

**Proposition 1.**  Let $\eta\in\overline{\mathbb Q}$, $\eta\ne1$,
and let $L$ be any logarithm of $1-\eta$.  If



$$
L=i\pi\alpha,
       \qquad \alpha\in\overline{\mathbb Q},
 \tag{13}
$$



then $\alpha\in\mathbb Q$ and $1-\eta$ is a root of unity.

**Proof.**  Exponentiating (13) gives



$$
1-\eta=e^{i\pi\alpha},
$$



which is the value of $(-1)^\alpha$ obtained from the logarithm
$i\pi$ of $-1$.  If $\alpha$ were algebraic irrational,
Gelfond--Schneider would make every value of $(-1)^\alpha$
transcendental.  The left side is algebraic, so
$\alpha\in\mathbb Q$.  Its exponential is therefore a root of unity.
$\square$

If a single Rivoal logarithm is to combine with the exponential remainder
using algebraic coefficients and isolate $e+\pi$, its logarithm must
satisfy (13): the ratio of its coefficient to the coefficient of $e$
is algebraic.  Proposition 1 is therefore a target-compatibility theorem,
not merely a height estimate.

Write $\alpha=a/b$ in lowest terms, where $b>0$.  The integral
combination



$$
iaA(\eta)R_{\exp}(1)+bA(1)R_{\log}(\eta)
 \tag{14}
$$



has coefficient $iaA(1)A(\eta)$ on $e+\pi$.  If
$\xi=1-\eta$ has order $N>1$, then $\eta=1-\xi$ is an algebraic
integer and



$$
|N_{\mathbb Q(\xi)/\mathbb Q}(\eta)|=\Phi_N(1).
 \tag{15}
$$



It is a unit precisely when $N$ is not a prime power.  Such units were
already present in the root-of-unity specialization.  If $\eta$ is
real, then $\xi$ is a real root of unity, so $\eta\in\{0,2\}$; neither
is an algebraic unit.  This excludes real Pisot and Salem units and their
inverses from the one-log target.

## 3. Exact product identity with substitution denominators

Let $K$ contain $\eta$, put $r=[K:\mathbb Q]$, and choose an
integer $q\geq1$ such that



$$
q\eta\in\mathcal O_K.
 \tag{16}
$$



For every $P\in\mathbb Z[x]$ of degree at most $C$,



$$
q^CP(\eta)=\sum_{k=0}^C p_kq^{C-k}(q\eta)^k
 \in\mathcal O_K.
 \tag{17}
$$



Thus $q^C$, rather than $q^M$, is a sufficient substitution clearing
for every coefficient in (14).  Nevertheless the exact archimedean
product of the leading logarithmic factor is



$$
\begin{aligned}
 \prod_{\sigma:K\hookrightarrow\mathbb C}
 |bq^C\sigma(\eta)^M|
 &=b^rq^{Cr}|N_{K/\mathbb Q}(\eta)|^M\\
 &=b^r\frac{|N_{K/\mathbb Q}(q\eta)|^M}
                 {q^{r(M-C)}}.
\end{aligned}
 \tag{18}
$$



This is (3).  Since $M-C=c+1$, a nonintegral parameter may leave a
formal factor $q^{-r(c+1)}$.  For an algebraic integer, $q=1$ and the
right side is at least $b^r$.  For a unit it is exactly $b^r$.

For a nonzero target-compatible parameter, the right side is in fact
strictly greater than one.  If $b>1$, this is immediate.  If $b=1$,
then $e^{i\pi a}=\pm1$.  The value $+1$ gives the unusable
$\eta=0$, while $-1$ gives $\eta=2$, whose norm is $2$.  Hence a
small unit embedding never supplies a strict global gain in (18).

The same statement in a compositum follows by norm transitivity: every
factor in (18) is raised to the degree over $K$.  Formula (18) concerns
the proposed leading-factor mechanism.  It does not exclude common
algebraic content in all coordinates, nor cancellation of the two
remainders.  Those are separate arithmetic and nonvanishing questions.

## 4. Two conjugate logarithms

Let $\eta$ be nonreal algebraic and let the bar denote the distinguished
complex conjugation.  Put



$$
L_\eta=\operatorname {Log}(1-\eta),\qquad
 L_{\bar\eta}=\operatorname {Log}(1-\bar\eta),
 \tag{19}
$$



using branches reached by the prescribed continuations.  Suppose



$$
L_\eta-L_{\bar\eta}=i\pi\frac ab,
 \qquad a\in\mathbb Z\setminus\{0\},\quad
 b\in\mathbb Z_{>0},\quad (a,b)=1.
 \tag{19a}
$$



Then the exact paired form is



$$
\boxed{\begin{aligned}
 \Lambda^{(2)}_{a,b}(\eta)
 ={}&iaA(\eta)A(\bar\eta)R_{\exp}(1)\\
 &+bA(1)\{A(\bar\eta)R_{\log}(\eta)
             -A(\eta)R_{\log}(\bar\eta)\}\\
 ={}&iaA(1)A(\eta)A(\bar\eta)(e+\pi)
       -iaA(\eta)A(\bar\eta)E(1)\\
 &-bA(1)A(\bar\eta)B(\eta)
       +bA(1)A(\eta)B(\bar\eta).
\end{aligned}}
 \tag{20}
$$



Thus (20) really is a new $e+\pi$ form, not an analogy.

Exponentiating (19a) and applying Proposition 1 to the quotient shows that
(19a) holds with an algebraic coefficient if and only if



$$
\frac{1-\eta}{1-\bar\eta}
 \quad\hbox{is a root of unity},
 \tag{21}
$$



with the usual integral multiple of $2\pi i$ allowed by the branch.
There is a useful exact parametrization.  Choose a root of unity $\omega$
whose square is the quotient in (21), and put



$$
r=\frac{1-\eta}{\omega}.
 \tag{22}
$$



Then (21) is equivalent to $r=\bar r$, and



$$
\eta=1-r\omega.
 \tag{23}
$$



Conversely, (23) with real algebraic $r$ gives the quotient $\omega^2$.
This proves that the paired construction is a root-of-unity angle with an
algebraic radial parameter.

For completeness, let



$$
F=\mathbb Q(r,\omega+\omega^{-1}),\qquad L=F(\omega),
$$



and assume $r\in\mathcal O_F$.  Then $\eta\in\mathcal O_L$ and



$$
N_{L/F}(\eta)
 =(1-r\omega)(1-r\omega^{-1})
 =1-(\omega+\omega^{-1})r+r^2=:u.
 \tag{24}
$$



Consequently



$$
\eta\in\mathcal O_L^\times
 \quad\Longleftrightarrow\quad
 u\in\mathcal O_F^\times.
 \tag{25}
$$



At the distinguished embedding $u=|\eta|^2$.  If it is below one, the
other embeddings of the real unit $u$ compensate it:



$$
\prod_{\nu:F\hookrightarrow\mathbb C}
                    |\nu(u)|^M=1.
 \tag{26}
$$



This is the paired version of norm neutrality.  The two summands in braces
in (20) can still cancel, so (26) by itself is not a nonvanishing theorem.

## 5. An infinite unit family

Let $n\geq5$ be odd, let $\xi=e^{2\pi i/n}$ be primitive, and set



$$
\eta=\frac1{1+\xi}.
 \tag{27}
$$



For odd $n>1$,



$$
N_{\mathbb Q(\xi)/\mathbb Q}(1+\xi)=\Phi_n(-1)=1.
 \tag{28}
$$



Hence $1+\xi$ and $\eta$ are algebraic-integer units.  Directly,



$$
\bar\eta=\frac1{1+\xi^{-1}}
          =\frac{\xi}{1+\xi}=1-\eta,
 \qquad
 \frac{1-\eta}{1-\bar\eta}=\frac{\bar\eta}{\eta}=\xi.
 \tag{29}
$$



At the distinguished embedding,



$$
\eta=\rho_ne^{-\pi i/n},\qquad
 \bar\eta=\rho_ne^{\pi i/n},\qquad
 \rho_n=\frac1{2\cos(\pi/n)}<1.
 \tag{30}
$$



The principal logarithms therefore satisfy



$$
\operatorname {Log}(1-\eta)
 -\operatorname {Log}(1-\bar\eta)
 =\operatorname {Log}(\bar\eta)-\operatorname {Log}(\eta)
 =\frac{2\pi i}{n}.
 \tag{31}
$$



Equations (20) and (31) give



$$
\boxed{\begin{aligned}
 \Lambda_{n}(c,d,f)
={}&2iA(\eta)A(\bar\eta)R_{\exp}(1)\\
 &+nA(1)\{A(\bar\eta)R_{\log}(\eta)
            -A(\eta)R_{\log}(\bar\eta)\}.
\end{aligned}}
 \tag{32}
$$



It has coefficient $2iA(1)A(\eta)A(\bar\eta)$ on $e+\pi$.

There is no substitution denominator because $\eta,\bar\eta$ are
units.  From (9), a safe rational clearing for all four coordinates in
(20) is



$$
\mathcal D_2=d!^3\operatorname {lcm}(\ell_C,F!).
 \tag{33}
$$



Indeed the four products have respective denominators dividing
$d!^3$, $d!^3F!$, and $d!^3\ell_C$.  Under the temporary hypothesis
$s=e+\pi\in\overline{\mathbb Q}$, choose $\delta\geq1$ with
$\delta s$ integral.  Then



$$
X_{n,c,d,f}=\delta\mathcal D_2\Lambda_n(c,d,f)
       \in\mathcal O_{\mathbb Q(\xi,i,s)}.
 \tag{34}
$$



The least coefficientwise rational multiplier divides $\mathcal D_2$,
but may be much smaller.  It is still a positive integer and therefore
cannot improve the raw relative product on the edge proved next.  Division
afterward by a common algebraic coordinate factor is not included in that
statement and remains a separate content question.

## 6. The locally contracting edge $c=f=0$

Put $c=f=0$ and write $A_d,B_d,E_d,R_d$ for the corresponding
objects.  Directly from the coefficient formula,



$$
A_d(x)=(-1)^d\sum_{j=0}^d\frac{(-x)^j}{j!}
        =(-1)^d\left\{e^{-x}
           +O_x\!\left(\frac{|x|^{d+1}}{(d+1)!}\right)\right\}.
 \tag{35}
$$



The exact integral (11) and endpoint Laplace expansion give, uniformly on
every fixed finite set in $\mathbb C\setminus[1,\infty)$,



$$
R_d(x)=\frac{(-1)^{d-1}}{ed}
       \frac{x^{d+1}}{1-x}\{1+O_x(d^{-1})\}.
 \tag{36}
$$



For reference, (36) follows without a saddle theorem.  Here



$$
H_{d,0}(u)=(-1)^du^d
       \sum_{q=0}^d\frac{(-1)^q}{q!u^q};
$$



on every interval $1-\epsilon\leq u\leq1$, the sum tends uniformly to
$e^{-1/u}$, with a factorially small tail.  On
$0\leq u\leq1-\epsilon$, termwise integration, split at
$r=d/2$, bounds the terms with $r\leq d/2$ factorially and the terms
with $r>d/2$ by $(1-\epsilon)^{d/2}$ times a polynomial factor.
Thus the complementary interval is exponentially smaller.  Watson's
endpoint estimate for $\int_0^1u^d g(u)\,du$ gives (36), with one
further endpoint expansion giving the stated $O(d^{-1})$ error.

For a residue $k\in(\mathbb Z/n\mathbb Z)^\times$, choose its
representative $-n/2<k<n/2$, and put



$$
x_k=\frac1{1+\xi^k}
     =\rho_ke^{-\pi ik/n},\qquad
 \rho_k=\frac1{2\cos(\pi k/n)}.
 \tag{37}
$$



Let $y_k=1-x_k=\bar x_k$.  Substitution of (35)--(36) gives



$$
\begin{aligned}
 D_{d,k}:={}&A_d(y_k)R_d(x_k)-A_d(x_k)R_d(y_k)\\
 ={}&\frac{2i e^{-3/2}}d\rho_k^d
 \left\{
  \sin\!\left(\frac{(d+2)\pi k}{n}
          +\frac12\tan\frac{\pi k}{n}\right)
       +O_n(d^{-1})
 \right\}.
\end{aligned}
 \tag{38}
$$



The leading sine never vanishes.  Its first term is a rational multiple of
$\pi$, while $\tfrac12\tan(\pi k/n)$ is a nonzero algebraic number.
If the sine vanished, a nonzero algebraic number would be a rational
multiple of the transcendental number $\pi$.  As $d$ varies, only
finitely many first terms occur modulo $2\pi$; their sine moduli therefore
have a positive minimum.  It follows that



$$
|D_{d,k}|\asymp_n\frac{\rho_k^d}{d},
 \tag{39}
$$



and every $D_{d,k}$ is nonzero for all sufficiently large $d$.
The exponential remainder is $O(1/(d!d))$, whereas
$A_d(1)=(-1)^d(e^{-1}+o(1))$.  Hence the analytic form in (32) at
$k=1$ is eventually nonzero and satisfies (6).

This proves genuine local smallness and nonvanishing.  It says nothing yet
about a field norm.

## 7. Every coefficient-field embedding and the norm exponent

Set



$$
\mathcal S_n=\{k\in(\mathbb Z/n\mathbb Z)^\times:\rho_k<1\},
 \qquad
 \mathcal T_n=\{k\in(\mathbb Z/n\mathbb Z)^\times:\rho_k>1\}.
 \tag{40}
$$



There is no equality case for odd $n\geq5$: equality would require
$|k|=n/3$, which is not coprime to $n$ unless $n=3$.  Also
$\pm1\in\mathcal S_n$.

Let $L_n=\mathbb Q(\xi,i)$.  Since $n$ is odd, its embeddings are
indexed by $(k,\epsilon)$, where



$$
\xi\longmapsto\xi^k,qquad
                  i\longmapsto\epsilon i,qquad
                  \epsilon\in\{1,-1\}.
$$



At the $k$-th logarithmic pair, the principal logarithm difference is
$2\pi ik/n$.  The algebraic form (32), however, retains the rational
coefficient $2\epsilon i$ on $s$.  Exact expansion therefore gives



$$
\sigma_{k,\epsilon}(\Lambda_{n,d})
 =\widetilde\Lambda_{d,k,\epsilon}
 +2i(\epsilon-k)\pi
       A_d(1)A_d(x_k)A_d(y_k),
 \tag{41}
$$



where



$$
\widetilde\Lambda_{d,k,\epsilon}
 =2\epsilon iA_d(x_k)A_d(y_k)R_{\exp}(1)
   +nA_d(1)D_{d,k}.
$$



Equation (41) is the all-embedding point that a purely local argument
misses.  The correction vanishes only for
$(k,\epsilon)=(1,1),(-1,-1)$.  If $k\in\mathcal S_n$ and the pair is
not one of those two, (39) tends to zero while



$$
|2i(\epsilon-k)\pi A_d(1)A_d(x_k)A_d(y_k)|
 \longrightarrow 2|\epsilon-k|\pi e^{-2}>0.
$$



If $k\in\mathcal T_n$, (39) grows exponentially and dominates the
constant correction for both choices of $\epsilon$.  Consequently



$$
\prod_{k,\epsilon}
   |\sigma_{k,\epsilon}(\Lambda_{n,d})|
 \asymp_n
 \left(\rho_1^2\prod_{k\in\mathcal T_n}\rho_k^2\right)^d
 d^{-2(1+|\mathcal T_n|)}.
 \tag{42}
$$



Because $\eta$ is a unit,



$$
\prod_k\rho_k=1.
 \tag{43}
$$



Using (43), the exponential base in (42) is



$$
\boxed{
 B_n=\rho_1^2\prod_{k\in\mathcal T_n}\rho_k^2
 =\left(\rho_1
       \prod_{k\in\mathcal S_n\setminus\{1,-1\}}\rho_k
   \right)^{-2}>1.}
 \tag{44}
$$



This proves (7).  For $n=5$,



$$
\rho_{\pm1}=\varphi^{-1},\qquad
 \rho_{\pm2}=\varphi,qquad
 \varphi=\frac{1+\sqrt5}{2},
$$



so $|\mathcal T_5|=2$ and (8) follows.

Suppose now, conditionally, that $s=e+\pi$ is algebraic.  If



$$
L_n\cap\mathbb Q(s)=\mathbb Q,
 \tag{45}
$$



then every embedding in (42) extends while fixing the distinguished
$s$, and the left side of (42) is the modulus of the relative norm from
$L_n(s)$ to $\mathbb Q(s)$.  It tends to infinity.  Multiplication by
the least positive-integer coordinate multiplier, by the safe clearing
(33), or by the fixed integrality multiplier $\delta$, raises the
  product by the corresponding nonnegative integral power and cannot reverse
  this growth.  This rules out obtaining a contraction from the direct
  coefficient-field relative-norm block.  It does not control the remaining
  target-conjugate blocks in a full absolute norm, and it does not rule out a
  quotient by a common algebraic factor unless the norm of the full
  coordinate-content ideal is also controlled.

If (45) fails, only embeddings agreeing on the intersection extend while
fixing $s$.  The remaining maps must be paired with embeddings that move
$s$ to unknown algebraic conjugates.  The analytic remainder estimate at
the distinguished $e+\pi$ gives no bound at those places.  Therefore the
intersection case supplies no certified global contraction; it is not
legitimate to multiply (39) over all formal conjugate evaluation points
while continuing to hold $s$ fixed.

## 8. Exact ideal-content computation for $n=5$

The ordinary gcd of the rational-basis coordinates is not the correct
algebraic content.  This matters already in small degrees.  Here is an exact
finite computation of the full ideal content, together with the precise
all-degree condition that would be needed to finish the obstruction.

Put $L=\mathbb Q(\zeta _5,i)=\mathbb Q(\zeta _{20})$ and let $K=L^+$
be its maximal real subfield.  The discriminants of
$\mathbb Q(\zeta _5)$ and $\mathbb Q(i)$ are $125$ and $-4$, so
they are coprime and
$\mathcal O_L=\mathbb Z[\zeta _5,i]$.  Taking the fixed lattice under
complex conjugation gives the integral basis



$$
1,\quad \zeta _5+\zeta _5^{-1},\quad
  i(\zeta _5-\zeta _5^{-1}),\quad
  i(\zeta _5^2-\zeta _5^{-2})
  \tag{46}
$$



of $\mathcal O_K$.  Multiplication of (32) by the common unit $-i$
puts every coefficient in $K$.  If $q_d$ is the least positive rational
integer for which all coefficients are integral, write



$$
q_d(-i\Lambda_{5,d})=u_d s+v_d,\qquad
             \mathfrak c_d=(u_d,v_d)\subset\mathcal O_K.
 \tag{47}
$$



This ideal is intrinsic under changes of integral basis and multiplication
of the form by a unit.  If an algebraic integer $\gamma\in\mathcal O_K$
divides both coordinates, then
$\mathfrak c_d\subseteq(\gamma)$, and hence



$$
|N_{K/\mathbb Q}(\gamma)|\leq N(\mathfrak c_d).
 \tag{48}
$$



More generally, a common divisor in $\mathcal O_L$ is bounded by
$N(\mathfrak c_d\mathcal O_L)=N(\mathfrak c_d)^2$.  The degree-eight
product (8) is likewise the square of the degree-four real-subfield product



$$
\prod_{\tau:K\hookrightarrow\mathbb R}
          |\tau(-i\Lambda_{5,d})|\asymp \varphi^d d^{-3}.
 \tag{49}
$$



Thus a common-coordinate quotient can cancel its exponential factor only if



$$
\limsup_{d\to\infty}\frac1d\log N(\mathfrak c_d)\geq\log\varphi.
 \tag{50}
$$



This is the exact missing content question; a rational-coordinate gcd equal
to one does not answer it.

For reproducibility, the coordinates can be reconstructed without rational
arithmetic.  Let



$$
h=d!,\quad \ell=\operatorname {lcm}(1,\ldots,d),\quad
 P_d=hA_d,\quad Q_d=h\ell B_d,\quad a_d=P_d(1).
 \tag{51}
$$



Then



$$
P_0(X)=1,\qquad P_d(X)=X^d-dP_{d-1}(X),\qquad
 [X^m]Q_d=-\sum_{j<m}[X^j]P_d\,\frac{\ell}{m-j}.
 \tag{52}
$$



Put $p=P_d(\eta)$, $\bar p=P_d(\bar\eta)$,
$r=Q_d(\eta)$, and $\bar r=Q_d(\bar\eta)$.  With
$\mathcal D=h^3\ell$, the three coefficient blocks of
$\mathcal D\Lambda_{5,d}=i\mathcal U_ds+\mathcal V_d+i\mathcal W_d$
are exactly



$$
\begin{aligned}
 \mathcal U_d&=2\ell a_d p\bar p,\\
 \mathcal W_d&=-2(-1)^dh\ell p\bar p,\\
 \mathcal V_d&=-5a_d\bar p\,r+5a_dp\,\bar r.
\end{aligned}
 \tag{53}
$$



Taking the gcd of $\mathcal D$ and all twelve
$\mathbb Z[\zeta _5]$-coordinates in (53) gives
$\mathcal D/q_d$.  After this division, the $4$ by $8$ integer matrix
whose columns are multiplication by $u_d$ and $v_d$ in the basis (46)
has image $\mathfrak c_d$; the product of its four Smith invariants is
exactly $N(\mathfrak c_d)$.

The archived exact computation gives, for every $1\leq d\leq200$,



$$
N(\mathfrak c_1)=16,\qquad
 N(\mathfrak c_d)=
 \left(5^{[d\equiv2\ ({\rm mod}\ 5)]}
       19^{[d\equiv15\ ({\rm mod}\ 19)]}
 \right)^2\quad(2\leq d\leq200).
 \tag{54}
$$



For example, the Smith diagonals are
$(1,1,5,5)$ at $d=7$, $(1,1,19,19)$ at $d=15$, and
$(1,1,95,95)$ at $d=72$.  In each of these cases the ordinary integer
coordinate gcd is one, demonstrating why ideal content was necessary.  A
separate $8$ by $16$ Smith calculation at selected degrees gives the
square of (54), as predicted by extension from $K$ to $L$.

The same certificate checks the exact strict inequality



$$
N(\mathfrak c_d)<\varphi^d
                    \qquad(3\leq d\leq200).
 \tag{55}
$$



No floating-point comparison is used: from
$\varphi^d=F_d\varphi+F_{d-1}$ and $\varphi>3/2$, the script verifies
$2N(\mathfrak c_d)<3F_d+2F_{d-1}$.  Equations (52)--(55) are an exact
finite certificate, not a proof that only the primes $5$ and $19$ can
occur at later degrees.  In particular, (50) remains open.  The recurrence
(52) reduces that problem to controlling simultaneous ideal divisors of
explicit integral recurrence values, but the finite residue pattern alone
does not supply such control.

The exact implementation and its complete degree-$200$ record are
<scripts/algebraic_unit_two_log_n5_ideal_content.py> and
<results/algebraic_unit_two_log_n5_ideal_content_d200.json>.  The earlier
branch, clearing, and asymptotic checks remain in
<scripts/algebraic_unit_two_log_rivoal_certificate.py> and its result file.

## 9. What is and is not ruled out

The exact conclusions are:

* arbitrary algebraic units, including Pisot and Salem units, cannot enter
  a one-log form for $e+\pi$ unless they are already $1-\zeta$;
* their leading $\eta^M$ factor is neutral by (18), and angle clearing is
  adverse;
* two conjugate logarithms do yield the new exact family (32);
* on $c=f=0$, this family is locally contracting and eventually nonzero;
* on the same edge its full coefficient-field relative norm grows
  exponentially whenever the coefficient field is disjoint from the
  hypothetical field of $s$;
* for $n=5$, the exact full ideal content through $d=200$ is given by
  (54) and is smaller than $\varphi^d$ for every tested $d\geq3$, but
  an all-degree bound strong enough for (50) is not proved;
* in a nontrivial intersection, unknown conjugates of $s$ remain
  uncontrolled.

No theorem here excludes every admissible sequence
$(c,d,f,n)$, especially one with varying $n$, exceptional coordinate
content, and nontrivial field intersections.  Any surviving proposal must
simultaneously prove:

1. nonvanishing of the *combined* form, not just of an individual
   remainder;
2. exact primitive denominator/content control;
3. a strict absolute-norm upper bound at every embedding, including those
   moving a hypothetical algebraic $s$.

The algebraic-unit leading factor alone supplies none of these.  In
particular, the local contraction (6) is a useful new diagnostic family,
not a proof about $e+\pi$.
