> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Positive integer CRT interpolation can cancel an entire prime window

Checked: 2026-08-27 UTC.

## 1. Verdict

Put



$$
u=1+x^2.
$$



For



$$
h\in\mathbb Z[x],\qquad h\equiv1\pmod {u^2},\qquad h(0)=0,
$$



write



$$
n=\operatorname {ord}_0h,\qquad d=\deg h,\qquad
 r=\frac{h-1}{u},
$$



and define



$$
I_0(h)=\int_0^1r(x)\,dx,\qquad
 I_1(h)=\int_0^1xr(x)\,dx.                               \tag{1}
$$



The preceding note found one positive nonsymmetric $h$ for which a
single prime in $d/3<p<n$ is absent from both moment denominators.
The present construction is an aggregate barrier: one positive integral
polynomial cancels **every prime** in a 17-prime window.

Let



$$
\begin{aligned}
 a(x)&=2x^4-x^8,\\
 m&=115,\qquad L=75,\qquad w(x)=x^L(1-x)^L,\\
 c_0&=139574584508098815002244647712452355913710915,\\
 c_1&= 92665357687907045832657432294875741514399515,      \tag{2}\\
 C(x)&=1-u^2w(x)(c_0+c_1x),\\
 h(x)&=a(x)^mC(x).
\end{aligned}
$$



Then



$$
\boxed{
 h\in\mathbb Z[x],\quad h\equiv1\pmod {u^2},\quad h(0)=0,
 \quad 0\leq h(x)\leq1\ (0\leq x\leq1),}                 \tag{3}
$$



and



$$
n=460,\qquad d=1075.             \tag{4}
$$



The complete prime interval $d/3<p<n$ is



$$
\begin{aligned}
 {\cal S}=\{&
 359,367,373,379,383,389,397,401,409,\\
 &419,421,431,433,439,443,449,457\}.                     \tag{5}
\end{aligned}
$$



For every $p\in{\cal S}$,



$$
\boxed{
 2r_{p-1}+r_{2p-1}\equiv0\pmod p,\qquad
 r_{2p-2}\equiv0\pmod p.}                                \tag{6}
$$



The exact two-moment criterion therefore gives



$$
I_0(h),I_1(h)\in\mathbb Z_{(p)}
                         \quad(p\in{\cal S}).             \tag{7}
$$



Equivalently, if $D(h)$ is the least positive common clearing
denominator of $I_0,I_1$, then



$$
\boxed{
 \gcd\!\left(D(h),
 \prod_{1075/3<p<460}p\right)=1.}                         \tag{8}
$$



The window product is



$$
P=\prod_{p\in{\cal S}}p
 =237359812447644832129693355690076072498951997,          \tag{9}
$$



with



$$
\log P=102.1781510915\ldots.     \tag{10}
$$



Thus neither positivity nor $h\equiv1\pmod {u^2}$ bounds the cancelled
Chebyshev mass by forcing even one prime of this particular window to
survive.  In particular, a prime-by-prime or fixed finite-window
subproduct argument cannot be the missing aggregate lemma.

This is a rigorous finite all-window counterexample, not an infinite
positive-density family.  It does not disprove an asymptotic theorem
which permits exceptional parameter values or obtains a denominator
from other primes or other output channels.

This package proves neither irrationality nor transcendence of
$e+\pi$.

## 2. The exact two-moment conditions

For an odd prime $d/3<p<n$, the preceding theorem gives



$$
\begin{aligned}
 I_0(h)\in\mathbb Z_{(p)}
 &\iff 2r_{p-1}+r_{2p-1}\equiv0\pmod p,\\
 I_1(h)\in\mathbb Z_{(p)}
 &\iff r_{2p-2}\equiv0\pmod p.                            \tag{11}
\end{aligned}
$$



The forced coefficients below $n$ give



$$
r_{p-1}=\varepsilon_p:=(-1)^{(p+1)/2},\qquad r_{p-2}=0.  \tag{12}
$$



The purpose of the CRT construction is therefore to impose



$$
r_{2p-1}=-2\varepsilon_p,\qquad
                         r_{2p-2}=0\pmod p                \tag{13}
$$



simultaneously for several distinct primes.

## 3. A conditional all-parameter CRT construction lemma

The following lemma separates the algebra, the CRT step, and positivity.
It is useful beyond the numerical instance in Section 5.

Let



$$
\begin{aligned}
 A_m(x)&=a(x)^m,\\
 R_m(x)&=\frac{A_m(x)-1}{u},\\
 w_L(x)&=x^L(1-x)^L,\\
 G_{m,L}(x)&=A_m(x)u\,w_L(x),                             \tag{14}
\end{aligned}
$$



where $m,L\geq1$.  These are integer polynomials because



$$
a-1=-u^2(1-x^2)^2.              \tag{15}
$$



For an odd prime $p<4m$, set



$$
E_p=2p-2,\qquad O_p=2p-1,
$$



and form the matrix



$$
M_p=
 \begin{pmatrix}
 [x^{E_p}]G_{m,L}&[x^{E_p-1}]G_{m,L}\\
 [x^{O_p}]G_{m,L}&[x^{O_p-1}]G_{m,L}
 \end{pmatrix}.                                          \tag{16}
$$



Suppose ${\cal P}$ is a finite set of distinct odd primes such that



$$
\det M_p\not\equiv0\pmod p\qquad(p\in{\cal P}).           \tag{17}
$$



For each $p$, solve



$$
M_p
 \binom{\gamma_{0,p}}{\gamma_{1,p}}
 \equiv
 \binom{[x^{E_p}]R_m}{2\varepsilon_p}\pmod p.             \tag{18}
$$



Let



$$
P_{\cal P}=\prod_{p\in{\cal P}}p.
$$



The ordinary integer CRT gives unique residue classes



$$
c_j\equiv\gamma_{j,p}\pmod p\quad(p\in{\cal P}),\qquad
 0\leq c_j<P_{\cal P}\quad(j=0,1).                       \tag{19}
$$



Assume in addition that



$$
c_0+c_1\leq4^{L-1}.              \tag{20}
$$



Then



$$
\boxed{
 h_{m,L,{\cal P}}
 =A_m\left(1-u^2w_L(c_0+c_1x)\right)}                    \tag{21}
$$



is an integral polynomial satisfying



$$
h_{m,L,{\cal P}}\equiv1\pmod {u^2},\qquad
 h_{m,L,{\cal P}}(0)=0,\qquad
 0\leq h_{m,L,{\cal P}}\leq1\quad\hbox{on }[0,1],         \tag{22}
$$



and both congruences in (6) hold for every $p\in{\cal P}$, provided
the primes also lie in the actual interval $d/3<p<n$.

### Proof

Put



$$
s=w_L(c_0+c_1x),\qquad C=1-u^2s.
$$



Since $L\geq1$, $C(0)=1$.  Because $A_m$ has order $4m$,



$$
\operatorname {ord}_0(A_mC)=4m. \tag{23}
$$



Both $A_m$ and $C$ are congruent to one modulo $u^2$, proving the
integral congruence in (22).

On $[0,1]$,



$$
0\leq w_L\leq4^{-L},\qquad
 0\leq c_0+c_1x\leq c_0+c_1,\qquad u^2\leq4.             \tag{24}
$$



Condition (20) therefore gives



$$
0\leq u^2s\leq
                         4\cdot4^{-L}(c_0+c_1)\leq1.      \tag{25}
$$



Hence $0\leq C\leq1$.  Also



$$
A_m=\bigl(1-(1-x^4)^2\bigr)^m
$$



lies in $[0,1]$, proving the sign assertion in (22).

Finally, division by $u$ in (21) gives the exact identity



$$
\boxed{
 \frac{h_{m,L,{\cal P}}-1}{u}
 =R_m-G_{m,L}(c_0+c_1x).}                                \tag{26}
$$



The polynomial $R_m$ is even.  Extracting degrees $E_p,O_p$ in
(26) shows that (18)--(19) are exactly



$$
r_{E_p}\equiv0,\qquad r_{O_p}\equiv-2\varepsilon_p
 \pmod p.                                                \tag{27}
$$



Equations (11)--(13) finish the proof.

This lemma uses no rational scaling.  The CRT representatives $c_0,c_1$
are nonnegative ordinary integers.  Their potentially large size is
controlled analytically by the integral padding $x^L(1-x)^L$; no
denominator is introduced.  The factor has value one at zero, so the
localization order of $A_m$ is preserved exactly.

## 4. Degree and window bookkeeping

When $c_1\ne0$, the polynomial $s=w_L(c_0+c_1x)$ has degree
$2L+1$, and hence



$$
\deg C=2L+5,\qquad
 \deg h=8m+2L+5.                                         \tag{28}
$$



For the parameters (2),



$$
\begin{aligned}
 n&=4m=460,\\
 d&=8m+2L+5=920+150+5=1075.                              \tag{29}
\end{aligned}
$$



Thus the prime interval is



$$
358\frac13<p<460.                \tag{30}
$$



Deterministic trial division through each square root verifies that the
complete list of primes in (30) is exactly (5).

The positivity capacity is checked entirely in integers:



$$
\begin{aligned}
 c_0+c_1
 &=232239942196005860834902080007328097428110430,\\
 4^{L-1}=4^{74}
 &=356811923176489970264571492362373784095686656,         \tag{31}\\
 4^{74}-(c_0+c_1)
 &=124571980980484109429669412355045686667576226>0.
\end{aligned}
$$



This proves (20) with a substantial exact margin.

## 5. Exact CRT certificate for all 17 primes

For the parameters $m=115,L=75$, the following table lists



$$
p,\qquad \det M_p\bmod p,\qquad c_0\bmod p,\qquad c_1\bmod p.
$$





$$
\begin{array}{c|r|r|r}
p&\det M_p&c_0&c_1\\ \hline
359&257&3&278\\
367&180&306&133\\
373&325&75&321\\
379&1&27&326\\
383&171&318&92\\
389&127&254&8\\
397&208&391&12\\
401&362&137&15\\
409&172&51&29\\
419&167&401&192\\
421&260&335&254\\
431&253&89&239\\
433&251&90&361\\
439&286&43&15\\
443&92&347&380\\
449&227&143&77\\
457&368&303&394
\end{array}                                               \tag{32}
$$



Every determinant is nonzero.  Direct substitution in (18) verifies
that the final two columns solve the required two equations for their
row prime.  The two integers in (2) are the simultaneous least
nonnegative CRT representatives.  They satisfy



$$
0\leq c_0,c_1<P,                 \tag{33}
$$



where $P$ is (9).

Equations (26), (18), and (32) prove all 34 congruences in (6).
As an independent check, exact rational reduction of both moments gives
a common denominator $D(h)$ satisfying



$$
D(h)\not\equiv0\pmod p
                         \quad(p\in{\cal S}),             \tag{34}
$$



which is equivalent to (8).

The table is a finite exact certificate for this explicit $h$.  It is
not extrapolated to unlisted primes, larger $m$, or a positive-density
sequence of windows.

## 6. What the construction does and does not show

The example cancels a product of 17 primes with logarithmic mass greater
than $102$, and those primes comprise 100 percent of its natural
one-third window.  It therefore rules out each of the following
unqualified statements:

* every positive admissible $h$ retains at least one prime from
  $d/3<p<n$ in the two-moment denominator;
* positivity makes the two exceptional congruences mutually
  incompatible for several primes;
* CRT interpolation necessarily introduces rational coefficients or
  destroys $h(0)=0$; or
* large CRT representatives necessarily violate $0\leq h\leq1$.

The padding mechanism explains the last point: integer residues of size
below $P$ cost only $L\asymp\log P$ in endpoint vanishing.

The example does **not** prove:

* an infinite family cancelling a positive-density set of primes;
* that every large prime window can be cancelled;
* that an asymptotic upper bound on total cancelled Chebyshev mass is
  impossible;
* that a third moment or the full correction output cannot recover the
  missing product; or
* any arithmetic classification of $e+\pi$.

The remaining aggregate problem must use information absent from the
two isolated moments and sign/congruence constraints, or prove a
genuinely asymptotic restriction on the CRT matrices or the required
padding degree.

## 7. Replay and status

From the research directory run

    python3 scripts/common_kernel_positive_crt_all_window_cancellation_certificate.py
    sha256sum -c results/common_kernel_positive_crt_all_window_cancellation_hashes.sha256

The deterministic replay:

1. reconstructs $A_m,R_m,w_L,G_{m,L},C,h,r$ exactly;
2. independently enumerates every prime in (30);
3. recomputes every determinant and CRT residue in (32);
4. verifies the CRT reconstruction of the integers in (2);
5. checks all 34 moment residues;
6. checks the exact positivity capacity (31);
7. reduces both rational moments and verifies (34); and
8. records coefficient and rational hashes without printing the
   thousand-degree polynomial.

All computations use exact integer and rational CPU arithmetic.  Finite
checks certify only the explicit counterexample.  No hardware accelerator
is useful, and the replay uses only a negligible fraction of the
available Colab RAM.
