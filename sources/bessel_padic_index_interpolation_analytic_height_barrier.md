> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Canonical $p$-adic index interpolation of the Bessel denominator

Checked: 2026-08-27 UTC.

## 1. Verdict

Let



$$
q_0=q_1=1,\qquad q_n=(4n-2)q_{n-1}+q_{n-2},
\tag{1}
$$



and put



$$
f(n)=(-1)^nq_n\qquad(n\geq0).
\tag{2}
$$



For every prime $p$, the period congruences make $f$ a
$1$-Lipschitz function on the nonnegative integers.  It therefore has a
unique canonical extension



$$
f_p:\mathbb Z_p\longrightarrow\mathbb Z_p.
\tag{3}
$$



This extension is substantially more regular than continuity alone.  Its
Mahler expansion



$$
f_p(x)=\sum_{j=0}^{\infty}A_j\binom{x}{j}
\tag{4}
$$



has coefficients independent of $p$, with the exact formula



$$
\boxed{
 A_j=(-1)^j j!\sum_{m=0}^{\lfloor j/2\rfloor}
       \frac{(-1)^m}{m!}\binom{2j-2m}{j}.}
\tag{5}
$$



In particular,



$$
\boxed{\frac{j!}{\lfloor j/2\rfloor!}\mid A_j.}
\tag{6}
$$



For every fixed prime,



$$
\boxed{\liminf_{j\to\infty}\frac{v_p(A_j)}j
       =\frac{1}{2(p-1)}.}
\tag{7}
$$



Amice's coefficient criterion then determines the exact integral
analyticity order:

- for every odd $p$, $f_p$ is analytic on each disk
  $r+p\mathbb Z_p$, but is not analytic on the whole disk
  $\mathbb Z_p$;
- for $p=2$, it is analytic on each disk $r+4\mathbb Z_2$, but not on
  every disk $r+2\mathbb Z_2$.

Thus the best uniform statement over all primes is analytic order $2$;
for the odd primes relevant to the Bessel denominator tail, the exact
order is $1$.

The interpolation also satisfies the global difference equation



$$
\boxed{
 f_p(x+2)+(4x+6)f_p(x+1)-f_p(x)=0
 \qquad(x\in\mathbb Z_p).}
\tag{8}
$$



For an ordinary root class $r\bmod p$, the unique compatible
prime-power roots converge to a simple zero
$\rho_{p,r}\in r+p\mathbb Z_p$.  For every nonnegative integer
$n\equiv r\pmod p$,



$$
\boxed{v_p(q_n)=v_p(n-\rho_{p,r}).}
\tag{9}
$$



Equation (9) is the strongest exact height reduction obtained here.  It
does **not** bound the right side.  Neither local analyticity,
Strassmann's theorem, nor simple-root Hensel lifting controls how small the
standard integer representative of a deep truncation of
$\rho_{p,r}$ can be.  The still-missing input is a quantitative,
uniform rational-integer approximation theorem for these particular zeros
of (4) and (8):



$$
v_p(n-\rho_{p,r})\log p=o(n\log n).
\tag{10}
$$



No such estimate is proved below.  The note isolates (10) without treating
$\rho_{p,r}$ as an arbitrary analytic root and without confusing a
root-count statement with a height statement.

## 2. Canonical $1$-Lipschitz extension

The all-modulus period theorem gives



$$
q_{n+M}\equiv(-1)^M q_n\pmod M
\tag{11}
$$



for every $M\geq1$.  Therefore



$$
\begin{aligned}
 f(n+M)
 &=(-1)^{n+M}q_{n+M}\\
 &\equiv(-1)^{n+2M}q_n=f(n)\pmod M.
\end{aligned}
\tag{12}
$$



Taking $M=p^a$ and iterating (12) shows



$$
n\equiv m\pmod {p^a}
 \quad\Longrightarrow\quad
 f(n)\equiv f(m)\pmod {p^a}.
\tag{13}
$$



Thus $f:\mathbb N\to\mathbb Z_p$ is $1$-Lipschitz.  Since
$\mathbb N$ is dense in $\mathbb Z_p$ and $\mathbb Z_p$ is
complete, (3) exists and is unique.  This construction is canonical; it
does not choose a parity function on $\mathbb Z_p$.  For odd $p$, the
two factors $(-1)^n$ and $q_n$ are individually anti-periodic and need
not interpolate continuously, while their product does.

The recurrence for the normalized values is



$$
f(n+2)+(4n+6)f(n+1)-f(n)=0.
\tag{14}
$$



Both sides are continuous functions of a $p$-adic variable after using
(3).  Equality on the dense set of nonnegative integers proves (8).

## 3. Mahler recurrence and formal generating function

Let



$$
A_j=\Delta^j f(0)
 =\sum_{k=0}^j(-1)^{j-k}\binom jk f(k).
\tag{15}
$$



Mahler's theorem and continuity give (4).  Since
$f(k)=(-1)^kq_k$,



$$
A_j=(-1)^j\sum_{k=0}^j\binom jk q_k.
\tag{16}
$$



In particular, $A_j\neq0$ and has sign $(-1)^j$.

Write $A_{-1}=0$.  Replacing shifts in (8) by forward differences gives



$$
\Delta^2 f+(4x+8)\Delta f+(4x+6)f=0.
\tag{17}
$$



Using



$$
\Delta\binom{x}{j}=\binom{x}{j-1},\qquad
 x\binom{x}{j}=j\binom{x}{j}+(j+1)\binom{x}{j+1},
\tag{18}
$$



comparison of Mahler coefficients gives



$$
\boxed{
 A_{j+2}+4(j+2)A_{j+1}+(8j+6)A_j+4jA_{j-1}=0,}
\tag{19}
$$



with $A_0=1,A_1=-2$.

There is also a closed formal generating function.  Put



$$
F(z)=\sum_{n=0}^{\infty}f(n)\frac{z^n}{n!}.
\tag{20}
$$



Equation (14) gives



$$
(1+4z)F''(z)+6F'(z)-F(z)=0,\qquad
 F(0)=1,\quad F'(0)=-1.
\tag{21}
$$



The unique formal solution is



$$
F(z)=
 \frac{\exp\bigl((\sqrt{1+4z}-1)/2\bigr)}
      {\sqrt{1+4z}}.
\tag{22}
$$



The exponential binomial transform between $f(n)$ and $A_j$ says



$$
\mathcal A(z):=\sum_{j=0}^{\infty}A_j\frac{z^j}{j!}
 =e^{-z}F(z).
\tag{23}
$$



If



$$
w=\frac{\sqrt{1+4z}-1}{2},\qquad z=w+w^2,
\tag{24}
$$



then



$$
\boxed{\mathcal A(z)=\frac{e^{-w^2}}{1+2w}.}
\tag{25}
$$



All identities in this section are formal power-series identities over
$\mathbb Q$; no complex convergence is being imported into the
$p$-adic argument.

## 4. Exact coefficient formula and divisibility

Let $H'(w)=e^{-w^2}$ and $H(0)=0$.  Since
$dw/dz=(1+2w)^{-1}$, equation (25) is



$$
\mathcal A(z)=\frac{d}{dz}H(w(z)).
\tag{26}
$$



The relation $w=z/(1+w)$ and Lagrange inversion give



$$
\begin{aligned}
 [z^j]\mathcal A(z)
 &=(j+1)[z^{j+1}]H(w(z))\\
 &=[u^j]e^{-u^2}(1+u)^{-j-1}.
\end{aligned}
\tag{27}
$$



Expanding the two factors on the last line yields



$$
\frac{A_j}{j!}
 =(-1)^j\sum_{m=0}^{\lfloor j/2\rfloor}
   \frac{(-1)^m}{m!}\binom{2j-2m}{j},
\tag{28}
$$



which proves (5).

Put $h=\lfloor j/2\rfloor$.  Multiplying the sum in (28) by $h!$
gives an integer:



$$
\frac{A_j}{j!/h!}
 =(-1)^j\sum_{m=0}^{h}
   (-1)^m\frac{h!}{m!}\binom{2j-2m}{j}\in\mathbb Z.
\tag{29}
$$



This proves (6).

The divisibility is sharp on an infinite subsequence.  If $j=2h$ and
$p\mid h$, every summand in (29) with $m<h$ contains the factor $h$
inside $h!/m!$.  Only $m=h$ survives modulo $p$, and hence



$$
\boxed{
 \frac{A_{2h}}{(2h)!/h!}\equiv(-1)^h\pmod p
 \qquad(p\mid h).}
\tag{30}
$$



Legendre's formula applied to (6) gives



$$
\liminf_{j\to\infty}\frac{v_p(A_j)}j
 \geq\frac{1}{2(p-1)}.
\tag{31}
$$



Taking $h=p^k$ in (30) gives equality asymptotically, proving (7).

## 5. Exact local analyticity class

For clarity, a function on $\mathbb Z_p$ has analytic order $s$ if
its restriction to every disk $r+p^s\mathbb Z_p$ is represented by a
convergent power series.  Amice's Mahler-coefficient criterion says that
a continuous function with coefficients $A_j$ has analytic order $s$
if and only if



$$
v_p(A_j)-
 v_p\left(\left\lfloor\frac{j}{p^s}\right\rfloor!\right)
 \longrightarrow+\infty.
\tag{32}
$$



This is the orthonormal-basis theorem for
$\lfloor j/p^s\rfloor!\binom{x}{j}$.  A primary reference is Y. Amice,
“Interpolation $p$-adique,” *Bulletin de la Société Mathématique de
France* **92** (1964), 117–180,
<https://www.numdam.org/articles/10.24033/bsmf.1606/>.

From (6),



$$
\begin{aligned}
 v_p(A_j)-
 v_p\left(\left\lfloor\frac{j}{p^s}\right\rfloor!\right)
 \geq{}&
 v_p(j!)-v_p(\lfloor j/2\rfloor!)\\
 &-v_p(\lfloor j/p^s\rfloor!).
\end{aligned}
\tag{33}
$$



The right side tends linearly to $+\infty$ whenever $p^s>2$.
For example, using the base-$p$ digit form of Legendre's formula gives
the explicit lower estimate



$$
\frac{j}{p-1}\left(\frac12-\frac1{p^s}\right)
 -1-\log_p(j+1).
\tag{34}
$$



Thus order $1$ works for odd $p$, and order $2$ works for $p=2$.

These orders are minimal.  For odd $p$, take $j=2p^k$ in (30).  Then



$$
v_p(A_j)-v_p(j!)=-v_p(p^k!)\longrightarrow-\infty,
\tag{35}
$$



so order $0$ fails.  For $p=2$, the same subsequence gives



$$
v_2(A_{2^{k+1}})
 -v_2((2^k)!)=1,
\tag{36}
$$



so the order-$1$ criterion does not tend to $+\infty$.  This proves
the exact analyticity assertions in Section 1.

## 6. Ordinary roots are simple analytic zeros

Now let $p$ be odd.  For $M=p^a$, define the integral index slope



$$
\delta_M(n)=\frac{-q_{n+M}-q_n}{M}.
\tag{37}
$$



The previously proved prime-power slope theorem is



$$
\delta_{p^a}(n)\equiv\delta_p(n)-q_n\pmod p
 \qquad(a\geq2).
\tag{38}
$$



Since $M$ is odd,



$$
\frac{f(n+M)-f(n)}M=(-1)^n\delta_M(n).
\tag{39}
$$



Analyticity on $n+p\mathbb Z_p$ makes the left side converge to
$f_p'(n)$ as $a\to\infty$.  If $p\mid q_n$, equations (38) and
(39) give



$$
f_p'(n)\equiv(-1)^n\delta_p(n)\pmod p.
\tag{40}
$$



Let $r$ be a root modulo $p$.  If $n=r+tp$, the first-level affine
law gives



$$
\delta_p(n)\equiv(-1)^t\delta_p(r)\pmod p.
\tag{41}
$$



Because $p$ is odd, the two parity factors in (40) and (41) cancel.
By density and continuity of the derivative,



$$
\boxed{
 f_p'(x)\equiv(-1)^r\delta_p(r)\pmod p
 \quad\text{for every }x\in r+p\mathbb Z_p.}
\tag{42}
$$



If $\delta_p(r)\neq0$, the class is ordinary and (42) is a unit.
The exact one-exponent lift law gives one compatible root $r_a\bmod p^a$
at every level.  Their inverse limit is a zero



$$
\rho_{p,r}=\lim_{a\to\infty}r_a\in r+p\mathbb Z_p,
\tag{43}
$$



and (42) makes it simple.  The same lift law proves it is the only zero in
that disk.

If $n\equiv r\pmod p$, put
$b=v_p(n-\rho_{p,r})$.  Then $n$ is the root class modulo $p^b$
but, by uniqueness, not modulo $p^{b+1}$.  The period theorem therefore
gives



$$
p^b\mid q_n,\qquad p^{b+1}\nmid q_n.
\tag{44}
$$



This proves (9).  It is the arithmetic version of the local analytic
factorization



$$
f_p(x)=(x-\rho_{p,r})U_{p,r}(x),
\qquad U_{p,r}(\rho_{p,r})\in\mathbb Z_p^\times.
\tag{45}
$$



## 7. What Strassmann proves, and what it cannot prove

For a fixed $p$, each restriction of $f_p$ to a residue disk of its
analyticity order is a nonzero analytic function.  Strassmann's theorem
therefore gives finitely many $p$-adic zeros on each disk.  On an
ordinary disk the preceding section is stronger: there is exactly one
simple zero.

These are **root-count** statements.  They control how many compatible
classes can survive.  They do not control the ordinary integer
representative



$$
0\leq r_a<p^a,\qquad
 r_a\equiv\rho_{p,r}\pmod {p^a}.
\tag{46}
$$



A single simple zero has exactly one truncation at every level whether
those truncations grow comparably to $p^a$ or remain exceptionally small
through many digits.  For example, certified ordinary branches begin



$$
\begin{array}{c|c|c}
p&r_a\text{ for successive }a&\text{new digits}\\ \hline
7&4,18,18,361,5163,106005,576601&2,0,1,2,6,4\\
11&6,28,28,1359,1359,1289767&2,0,1,0,8\\
13&8,8,346,6937,206864&0,2,3,7.
\end{array}
\tag{47}
$$



The zero digits in (47) are harmless finite examples, but they show
concretely why uniqueness does not force geometric growth of the standard
representative.

Equation (9) converts the required Bessel height estimate into the
specific approximation problem (10).  The elementary product formula only
recovers



$$
v_p(n-\rho_{p,r})\log p
 =v_p(q_n)\log p
 \leq\log q_n=n\log n+O(n),
\tag{48}
$$



which is exactly the forbidden main scale.

If the zeros $\rho_{p,r}$ were known to be algebraic with suitably
uniform degree and height, a Liouville-type estimate would give a much
stronger rational-integer approximation bound.  Their algebraicity is not
known and is not implied by (8), (25), local analyticity, or simplicity.
Conversely, merely proving that a zero is irrational or transcendental
would not exclude a $p$-adic Liouville approximation pattern.

The missing theorem is therefore not another Strassmann or Hensel
statement.  It must exploit the particular Mahler coefficients (5), the
difference equation (8), or additional arithmetic structure to prove a
uniform irrationality measure of the form (10).  This note finds no such
measure and does not assume that the roots of this specific interpolation
behave like arbitrary analytic roots.

Nothing here proves irrationality or transcendence of $e+\pi$.

## 8. Exact certificate

The companion script

    scripts/bessel_padic_index_interpolation_certificate.py

checks the period-Lipschitz congruences, the Mahler recurrence (19), the
finite-difference and closed formulas (15) and (5), the divisibility (6),
the sharp subsequence (30), the Amice valuation gaps, and the ordinary
root truncations in (47).  It also checks finite instances of the exact
distance identity (9).

Run

    python -m py_compile scripts/bessel_padic_index_interpolation_certificate.py
    python scripts/bessel_padic_index_interpolation_certificate.py

For a byte-identical replay, use

    python scripts/bessel_padic_index_interpolation_certificate.py \
      --output /tmp/bessel_padic_index_interpolation_certificate.json
    cmp results/bessel_padic_index_interpolation_certificate.json \
      /tmp/bessel_padic_index_interpolation_certificate.json

The computation is a finite diagnostic.  The all-$p$, all-index proofs
are in Sections 2--7.
