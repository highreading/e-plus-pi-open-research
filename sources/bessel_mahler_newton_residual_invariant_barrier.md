> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Mahler/Newton residual polynomials and nonlinear invariants for the Bessel index zero

Checked: 2026-08-27 UTC.

## 1. Verdict

Let



$$
f_p(x)=\sum_{j=0}^{\infty}A_j\binom{x}{j},
\qquad
 A_j=(-1)^j\sum_{i=0}^{j}\binom ji q_i,
\tag{1}
$$



be the canonical $p$-adic interpolation of
$f(n)=(-1)^nq_n$, where



$$
q_0=q_1=1,\qquad q_n=(4n-2)q_{n-1}+q_{n-2}.
\tag{2}
$$



This note tests the surviving integer-polynomial problem from

    sources/bessel_parameter_hermite_pade_sigma_operator_barrier.md

in the global Mahler basis, the Newton basis on one $p$-adic residue
disk, diagonal Amice/Carlitz-type renormalizations, and polynomial
quadratic invariants of the recurrence.

The exact conclusions are:

1. The degree-$K$ Mahler truncation

   

$$
S_K(x)=\sum_{j=0}^{K}A_j\binom{x}{j}
   \tag{3}
$$



   obeys a rigorous termwise root estimate, but that estimate has the
   same half-depth ceiling as the raw hypergeometric truncation.
2. At every integer $n>K$, all apparent alternating cancellation in
   $S_K(n)$ disappears after binomial inversion:

   

$$
\boxed{
   S_K(n)=(-1)^K
   \sum_{i=0}^{K}
   \binom ni\binom{n-i-1}{K-i}q_i.}
   \tag{4}
$$



   In particular it is nonzero, and

   

$$
\boxed{
   \binom nKq_K
   \leq |S_K(n)|
   \leq2^K\binom nKq_K.}
   \tag{5}
$$



   For $K\geq n$, $S_K(n)=(-1)^nq_n$.  Thus the Mahler auxiliary
   has no hidden archimedean cancellation.
3. The same phenomenon holds on the natural $p$-step Newton grid in
   an ordinary root disk.  Its $J$-th coefficient already has
   archimedean size at least $q_{r+pJ}$, and the first basis term
   containing the factor $x-n$ has coefficient at least $q_{n+p}$.
4. Diagonal rescaling to an Amice analytic basis does not change a
   single summand or partial sum, so it cannot alter the order-to-height
   balance.  A genuinely nontriangular or root-adapted basis would
   require a new coefficient-height theorem.
5. The recurrence admits no nonzero polynomial quadratic invariant or
   anti-invariant.  The canonical nonlinear Hankel expression is a unit
   at every ordinary root.  Hence the first natural nonlinear
   recurrence invariants do not bound the residual polynomial at the
   root.

These are scoped no-go theorems.  They do not exclude cancellation in a
new nontriangular tail transform, a rational invariant with controlled
poles, or a higher-degree invariant.  No bound



$$
v_p(n-\rho_{p,r})\log p=o(n\log n)
\tag{6}
$$



is proved.

## 2. Global Mahler truncations

For completeness, this divisibility does not need to be imported from
another note.  The recurrence for $f(n)=(-1)^nq_n$ gives, as a formal
power-series identity,



$$
F(z):=\sum_{n\geq0}f(n)\frac{z^n}{n!}
 =\frac{\exp((\sqrt{1+4z}-1)/2)}{\sqrt{1+4z}}.
$$



The exponential binomial transform gives
$\mathcal A(z):=\sum_{j\geq0}A_jz^j/j!=e^{-z}F(z)$.
With $w=(\sqrt{1+4z}-1)/2$, so that $z=w+w^2$, this becomes



$$
\mathcal A(z)=\frac{e^{-w^2}}{1+2w}.
$$



If $H'(w)=e^{-w^2}$ and $H(0)=0$, then
$\mathcal A(z)=dH(w(z))/dz$.  Lagrange inversion applied to
$w=z/(1+w)$ now gives



$$
\frac{A_j}{j!}
 =[u^j]e^{-u^2}(1+u)^{-j-1}
 =(-1)^j
 \sum_{m=0}^{\lfloor j/2\rfloor}
 \frac{(-1)^m}{m!}\binom{2j-2m}{j},
$$


and hence



$$
A_j=(-1)^j j!
 \sum_{m=0}^{\lfloor j/2\rfloor}
 \frac{(-1)^m}{m!}\binom{2j-2m}{j}.
$$



If $h=\lfloor j/2\rfloor$, division by $j!/h!$ leaves the integer



$$
(-1)^j\sum_{m=0}^{h}
 (-1)^m\frac{h!}{m!}\binom{2j-2m}{j}.
$$



Thus, without any analytic input,



$$
\frac{j!}{\lfloor j/2\rfloor!}\mid A_j.
\tag{7}
$$



Put



$$
\begin{aligned}
 D_K&=
 v_p((K+1)!)
 -v_p\!\left(\left\lfloor\frac{K+1}{2}\right\rfloor!\right),\\
 V_K&=
 v_p\!\left(\left\lfloor\frac K2\right\rfloor!\right).
\end{aligned}
\tag{8}
$$



The function



$$
j\longmapsto v_p(j!)-v_p(\lfloor j/2\rfloor!)
\tag{9}
$$



is nondecreasing.  From $2h$ to $2h+1$ its increment is
$v_p(2h+1)$, and from $2h+1$ to $2h+2$ its increment is
$v_p(2)$.  Therefore (7) gives the uniform tail estimate



$$
v_p(f_p(x)-S_K(x))\geq D_K
 \qquad(x\in\mathbb Z_p).
\tag{10}
$$



Let $\rho$ be an ordinary zero and



$$
a=v_p(n-\rho).
\tag{11}
$$



The integral falling-factorial numerator gives



$$
v_p\left(\binom nj-\binom{\rho}{j}\right)
 \geq a-v_p(j!).
\tag{12}
$$



Combining (7) and (12), then summing through $K$, gives



$$
v_p(S_K(n)-S_K(\rho))\geq a-V_K.
\tag{13}
$$



Since $f_p(\rho)=0$, equations (10) and (13) prove



$$
\boxed{
 v_p(S_K(n))\geq\min\{D_K,a-V_K\}.}
\tag{14}
$$



This is the complete estimate obtained from coefficient divisibility,
termwise Lipschitz control, and the Mahler tail.  Cancellation inside the
tail could make $S_K(\rho)$ smaller; no such cancellation is assumed
or excluded here.

### 2.1 Exact half-depth ceiling

The imbalance $D_K-V_K$ is a central-binomial valuation.  If
$K=2h$, then



$$
D_K-V_K
 =v_p\left((2h+1)\binom{2h}{h}\right),
\tag{15}
$$



while if $K=2h+1$, then



$$
D_K-V_K
 =v_p\left((h+1)\binom{2h+2}{h+1}\right).
\tag{16}
$$



Kummer's carry theorem and the elementary valuation of the linear
factor give, uniformly in $p,K$,



$$
0\leq D_K-V_K
 \leq2\bigl(1+\lfloor\log_p(K+2)\rfloor\bigr).
\tag{17}
$$



For any real $a$,



$$
\begin{aligned}
 \min\{D_K,a-V_K\}
 &\leq\frac{D_K+a-V_K}{2}\\
 &\leq\frac a2+
 1+\lfloor\log_p(K+2)\rfloor.
\end{aligned}
\tag{18}
$$



Thus the particular termwise estimates leading to (14) can certify at
most half of a deep root distance, up to a logarithmic error.  This is
an estimate-method barrier, not an upper bound on the actual valuation
of $S_K(n)$.

### 2.2 Exact integer value and height

For $K<n$, substitute the finite-difference definition of $A_j$
into (3) and interchange sums.  The partial alternating-binomial
identity



$$
\sum_{j=i}^{K}(-1)^{j-i}\binom nj\binom ji
 =(-1)^{K-i}\binom ni\binom{n-i-1}{K-i}
\tag{19}
$$



and $f(i)=(-1)^iq_i$ prove (4).  Every summand on the right of
(4) has the same sign.  The term $i=K$ gives the lower bound in
(5).  For the upper bound, use $q_i\leq q_K$ and



$$
\binom ni\binom{n-i-1}{K-i}
 \leq\binom nK\binom Ki,
\tag{20}
$$



then sum over $i$.

When $K\geq n$, the binomial basis terminates and Mahler interpolation
gives



$$
S_K(n)=S_n(n)=f(n)=(-1)^nq_n.
\tag{21}
$$



There is also an exact visibility threshold.  The basis polynomial
$\binom{x}{j}$ contains $x-n$ as a factor exactly when



$$
j\geq n+1.
\tag{22}
$$



At the first such index, the coefficient has



$$
|A_{n+1}|
 =\sum_{i=0}^{n+1}\binom{n+1}{i}q_i
 \geq q_{n+1},
\tag{23}
$$



whose logarithmic size is $n\log n+O(n)$.  Thus the first individual
Mahler term that sees the full factor $x-n$ already imports the
Bessel main scale.

Finally, the Mahler coefficient sequence itself is not a hidden
$\Sigma$-operator sequence.  Equation (1) gives
$|A_j|\geq q_j$, so its ordinary generating series also has radius
zero.  Rivoal's $\Sigma$-operator purity theorem therefore excludes
any eventual $\Sigma$-operator annihilator for $(A_j)$, just as for
$(f(j))$.

## 3. The Newton basis on a root residue disk

The prime $2$ contributes no denominator valuation: induction in
(2) gives $q_n\equiv1\pmod 2$ for every $n$.  Thus only odd primes
can support a root relevant to the denominator-height problem.

Let $p$ be odd, fix $r\in\{0,\ldots,p-1\}$, and put



$$
g_{p,r}(z)=f_p(r+pz).
\tag{24}
$$



Its Mahler/Newton coefficients on $\mathbb Z_p$ are



$$
\begin{aligned}
 C_j^{(p,r)}
 &=\Delta^jg_{p,r}(0)\\
 &=\sum_{i=0}^{j}(-1)^{j-i}\binom ji f(r+pi)\\
 &=(-1)^{j+r}\sum_{i=0}^{j}\binom ji q_{r+pi}.
\end{aligned}
\tag{25}
$$



The last equality uses that $p$ is odd.  Hence



$$
\boxed{
 q_{r+pj}\leq|C_j^{(p,r)}|
 \leq2^jq_{r+pj}.}
\tag{26}
$$



For



$$
S_J^{(p,r)}(z)
 =\sum_{j=0}^{J}C_j^{(p,r)}\binom zj
\tag{27}
$$



and integers $m>J$, the same calculation as in Section 2 gives



$$
\boxed{
 S_J^{(p,r)}(m)
 =(-1)^{J+r}
 \sum_{i=0}^{J}
 \binom mi\binom{m-i-1}{J-i}q_{r+pi}.}
\tag{28}
$$



Consequently



$$
\boxed{
 \binom mJq_{r+pJ}
 \leq|S_J^{(p,r)}(m)|
 \leq2^J\binom mJq_{r+pJ}.}
\tag{29}
$$



For $J\geq m$, the value freezes at



$$
S_J^{(p,r)}(m)=f(r+pm).
\tag{30}
$$



If $n=r+pm$, the factor $x-n$ first appears in the $p$-grid
Newton polynomial



$$
\binom{(x-r)/p}{j}
\tag{31}
$$



at $j=m+1$.  Its coefficient then has size at least



$$
q_{r+p(m+1)}=q_{n+p}.
\tag{32}
$$



Thus adapting the nodes to the ordinary residue disk does not lower the
visibility cost; it moves the cost to a still larger Bessel index.
Equations (25)--(32) are archimedean statements.  They do not assert an
optimal $p$-adic divisibility law for $C_j^{(p,r)}$.

## 4. What a basis renormalization can and cannot change

Amice's analytic-order criterion uses normalized basis elements such as



$$
\left\lfloor\frac{j}{p^s}\right\rfloor!
 \binom{x}{j}.
\tag{33}
$$



Writing the same Mahler expansion in this basis divides $A_j$ by the
displayed factorial and multiplies the basis polynomial by it.  Their
product remains exactly



$$
A_j\binom{x}{j}.
\tag{34}
$$



Therefore every diagonal renormalization of this kind leaves the
partial sums (3), the root estimate (14), the integer formula (4), and
the visibility threshold (22) unchanged.  Grouping consecutive terms
without changing their total likewise cannot change the evaluated
auxiliary.

A nontriangular $p$-typical or Carlitz-style transform is not excluded
by this observation.  But it must prove two new facts simultaneously:
large $p$-adic order of the transformed tail at $\rho$, and
sub-main archimedean height after clearing all denominators.  A
root-adapted node ordering that inserts $n$ early is circular unless
its divided-difference coefficient can be controlled without importing
the value $f(n)=(-1)^nq_n$.

The quadratic Newton basis



$$
\frac{(-x)_j(x+1)_j}{j!}
\tag{35}
$$



is the other natural nontriangular coordinate already available.  Its
all-truncation half-depth and visibility barriers are proved in

    sources/bessel_padic_hypergeometric_zero_pade_barrier.md

and the quadratic coordinate preserves the exact ordinary-root distance.

## 5. A polynomial quadratic-invariant exclusion

Write the recurrence state as



$$
Y_x=\binom{f_p(x)}{f_p(x-1)},\qquad
 Y_{x+1}=T(x)Y_x,
\quad
 T(x)=
 \begin{pmatrix}
 -(4x+2)&1\\
 1&0
 \end{pmatrix}.
\tag{36}
$$



Consider a polynomial quadratic form



$$
Q_x(Y)=Y^{\mathsf T}S(x)Y,\qquad
 S(x)=
 \begin{pmatrix}
 u(x)&v(x)\\
 v(x)&w(x)
 \end{pmatrix},
\quad u,v,w\in\mathbb Q[x].
\tag{37}
$$



Suppose it is an invariant or anti-invariant:



$$
Q_{x+1}(T(x)Y)=\varepsilon Q_x(Y)
 \quad\text{for every }Y,\qquad
 \varepsilon\in\{1,-1\}.
\tag{38}
$$



Then



$$
T(x)^{\mathsf T}S(x+1)T(x)=\varepsilon S(x).
\tag{39}
$$



Taking determinants in (39), using $\det T=-1$, shows that
$\det S(x+1)=\det S(x)$.  Hence $\det S$ is constant.

The lower-right and off-diagonal entries of (39), with
$a(x)=4x+2$, are



$$
u(x+1)=\varepsilon w(x),\qquad
 v(x+1)-\varepsilon v(x)=a(x)u(x+1).
\tag{40}
$$



If $u\ne0$ has degree $d$, equation (40) gives



$$
\deg v=
 \begin{cases}
 d+2,&\varepsilon=1,\\
 d+1,&\varepsilon=-1.
 \end{cases}
\tag{41}
$$



But $w$ has degree $d$, so



$$
\det S=uw-v^2
\tag{42}
$$



has degree $2\deg v>2d$, contradicting its constancy.  If $u=0$,
equations (39)--(40) immediately force $v=w=0$.  Therefore



$$
\boxed{\text{there is no nonzero polynomial quadratic invariant or
 anti-invariant of the form (37)--(38).}}
\tag{43}
$$



This is an all-degree theorem.  It does not exclude rational forms with
poles or higher-degree polynomial first integrals.

The simplest nonlinear determinant confirms the same behavior:



$$
H(x)=f_p(x)f_p(x+2)-f_p(x+1)^2.
\tag{44}
$$



At an ordinary zero $\rho$, the boundary-unit theorem gives



$$
H(\rho)=-f_p(\rho+1)^2\in\mathbb Z_p^\times.
\tag{45}
$$



At integer indices the corresponding denominator expression satisfies



$$
q_{n-1}q_{n+1}-q_n^2
 \equiv q_{n-1}^2\pmod {q_n},
\tag{46}
$$



and consecutive denominators are coprime.  Hence



$$
\gcd(q_{n-1}q_{n+1}-q_n^2,q_n)=1.
\tag{47}
$$



The canonical quadratic determinant removes, rather than captures, every
prime power in $q_n$.

## 6. Exact survivor

The rigorous Mahler estimate (14) is saturated at half depth at the
level of the available termwise bounds.  The exact same-sign formulas
(4) and (28) rule out archimedean cancellation in the two canonical
Newton grids.  The quadratic invariant theorem (43) removes the first
natural nonlinear escape.

What remains is a precise nontriangular-cancellation problem:

> Construct integer polynomials
> $B_{p,r,n}(x)=\sum_j b_jx^j$, or a transformed tail
> with the same arithmetic effect, such that
> 

$$
> v_p(B_{p,r,n}(\rho_{p,r}))
> \geq v_p(n-\rho_{p,r}),
>
$$


> $B_{p,r,n}(n)\ne0$, and
> 

$$
> \log H_1(B_{p,r,n})
> +\deg(B_{p,r,n})\log(n+1)=o(n\log n),
>
$$


> uniformly in the relevant $p,r,n$, where
> $H_1(B)=\sum_j|b_j|$.

Indeed, integral polynomials are $1$-Lipschitz on
$\mathbb Z_p$, so the first displayed condition implies
$v_p(B_{p,r,n}(n))\geq v_p(n-\rho_{p,r})$.  Since the integer
$B_{p,r,n}(n)$ is nonzero,



$$
v_p(n-\rho_{p,r})\log p
 \leq\log|B_{p,r,n}(n)|
 \leq\log H_1(B_{p,r,n})
   +\deg(B_{p,r,n})\log(n+1).
\tag{48}
$$



In the determinant reduction of the preceding source, the same
criterion is applied to the residual integer polynomial
$B(x)=\det\mathcal B(x)$.

Any proof must use cancellation not present in (4) or (28), while also
proving its archimedean height after denominator clearing.  No such
transform or invariant is obtained here.

Nothing in this note proves irrationality or transcendence of a Bessel
zero, or of $e+\pi$.

## 7. Exact certificate

The companion script

    scripts/bessel_mahler_newton_residual_invariant_certificate.py

checks the Mahler coefficients, divisibility (7), tail exponents
(8)--(10), central-binomial identities (15)--(17), and the half-depth
ceiling (18) over exact finite boxes.  It checks the same-sign formulas
and bounds (4)--(5) and (25)--(29), the visibility thresholds, the
coprimality (47), and the absence of polynomial quadratic invariants
through independent finite-degree linear-algebra diagnostics.  The
all-degree invariant exclusion is the symbolic proof in Section 5.

Run

    python -m py_compile scripts/bessel_mahler_newton_residual_invariant_certificate.py
    python scripts/bessel_mahler_newton_residual_invariant_certificate.py

For byte-identical replay, use

    python scripts/bessel_mahler_newton_residual_invariant_certificate.py \
      --output /tmp/bessel_mahler_newton_residual_invariant_certificate.json
    cmp results/bessel_mahler_newton_residual_invariant_certificate.json \
      /tmp/bessel_mahler_newton_residual_invariant_certificate.json
