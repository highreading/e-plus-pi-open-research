> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# An exact ternary cofactor family outside saturation

Date: 2026-09-13. Bounded original continuation by audit_computations.
Subsequent continuation: raw_ternary_factorial_denominator_subsequence.md
closes the logarithmic loss and the actual reduced-denominator valuation
on this family. The first-layer argument below is retained as a separate
exact derivation; its then-missing higher-depth target is no longer the
current status of the family.
The all-index statements below concern the infinite even digit family
$n=3^\nu-1$, $\nu\ge1$. No degree was constructed or scanned.
They determine the ordinary cofactor content and endpoint excess exactly,
and give one exact deeper cofactor layer. They do not yet bound the actual
reduced denominator by a fixed-prime factorial divisor.

## 1. Definitions and conclusions

Use the integer matrix from the passed fixed-prime gate:



$$
\mathsf Z_{rj}=L\sum_{s=0}^n(-1)^s\binom ns
 \frac{(n+r+s)!}{(n+r)!}\tau_{n+r+s-j},
 \quad 0\le r\le n,\quad0\le j<n,
\tag{1}
$$



where $L=\operatorname{lcm}(1,\ldots,3n)$,
$\tau_k=(-1)^{(k-1)/2}/k$ for positive odd $k$, and zero for
positive even $k$. The displayed sign uses that $n$ is even.
Let



$$
\delta_r=\det\mathsf Z[\widehat r,:],\quad
 \Theta=\gcd_r|\delta_r|,\quad
 c_r=(2n)!/(n+r)!,\quad
 h=\gcd_r|c_r\delta_r|,
$$




$$
R=(2n)!/n!,\quad
 v_r=\sum_{s=0}^n(-1)^s\binom ns\frac{(n+r+s)!}{(n+r)!},
 \quad K=\sum_{r=0}^n(-1)^r\delta_rv_r.
\tag{2}
$$



The actual identities are $hZ_n=RK$ and
$d_n^{II}=|K|/\Theta$. Put $d=v_3(h/\Theta)$ and
$\kappa=v_3(K/\Theta)$.

**Theorem.** For every $n=3^\nu-1$,



$$
\boxed{v_3(\Theta)=0,\quad v_3(\delta_0)=0,
 \quad3\mid\delta_r\ (r>0),\quad\kappa=0.}
\tag{3}
$$



For $\nu\ge2$, put $H=3^{\nu-1}$, so $n=3H-1$. Then



$$
\boxed{\delta_{2H}\equiv3\delta_0\pmod9,
 \qquad\delta_r\equiv0\pmod9\quad(r>0,\ r\ne2H).}
\tag{4}
$$



In particular,



$$
\boxed{2\le d\le(H+1)/2,\qquad
 v_3(Z_n)=n/2-d\ge H-1\quad(\nu\ge2).}
\tag{5}
$$



The lower bound in (5) is for the **unreduced** endpoint $Z_n$.
Equation (3) proves there is no positive $\kappa$ compensation on
this family. The numerator gcd is still required to pass to $q_n$.
For the particular already studied degree $n=8$, the all-index
bounds give exactly $d=2,\kappa=0$, without constructing its dual.

## 2. The exact finite-field matrix

Write $T=3^\nu=n+1$. Since $T\le3n<3T$,
$v_3(L)=\nu$. The only positive odd Taylor index at most $3n$
for which $L\tau_k$ is nonzero modulo 3 is $k=T$: the other
possible multiple $2T$ is even. Set



$$
\lambda=L\tau_T\in\mathbb Z_3^\times.
\tag{6}
$$



For $s\ge3$, the integer rising factorial
$(n+r+s)!/(n+r)!$ contains three consecutive factors and is
divisible by 3. Every $L\tau_k$ is integral. Thus only $s=0,1,2$
can contribute to (1) modulo 3. Since $n\equiv-1\pmod3$, their
coefficients are respectively



$$
1,\qquad r,\qquad r(r+1)\pmod3.
$$



The condition $n+r+s-j=T$ gives $j=r+s-1$. Therefore



$$
\boxed{\lambda^{-1}\mathsf Z_{rj}
 \equiv\mathbf1_{j=r-1}+r\mathbf1_{j=r}
       +r(r+1)\mathbf1_{j=r+1}\pmod3.}
\tag{7}
$$



All indicators outside the actual column range are zero. In particular
row 0 vanishes. The square matrix $A$ formed by rows $1,\ldots,n$
is $\lambda$ times an upper triangular matrix $U$ with diagonal
one. Hence $\delta_0=\det A$ is a unit, and every other maximal
minor contains row 0 and is divisible by 3. This proves the first three
claims in (3), including full column rank of the original matrix.

For later use, the complete repeating diagonal blocks of $U$ and its
inverse are



$$
U_3=\begin{pmatrix}1&1&2\\0&1&2\\0&0&1\end{pmatrix},
 \qquad
 U_3^{-1}=\begin{pmatrix}1&2&0\\0&1&1\\0&0&1\end{pmatrix}
 \quad\text{over }\mathbb F_3.
\tag{8}
$$



The final block has size two, since $n\equiv2\pmod3$; it is
$\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)$.
There are no couplings across these blocks in (7).

The same truncation $s=0,1,2$, now without the Taylor moment, gives



$$
v_r\equiv1+r+r(r+1)=(r+1)^2\pmod3.
\tag{9}
$$



Thus $K\equiv\delta_0v_0\equiv\delta_0\not\equiv0\pmod3$,
proving $\kappa=0$ and completing (3).

## 3. The first deeper cofactor layer

Assume $\nu\ge2$, so $H=T/3$ is divisible by 3. In row 0,
every $s\ge1$ term of (1) contains the factor $n+1=T$. It is
therefore zero modulo 9, without dividing any of its integer factors.
The remaining row is $L\tau_{n-j}$. Its indices lie between 1 and
$T-1$. The only one with exactly $\nu-1$ powers of 3 and a
nonzero odd Taylor moment is $H$. Hence, writing
$j_0=n-H=2H-1$,



$$
\mathsf Z_{0,:}/3\equiv-\lambda e_{j_0}^{\mathsf T}\pmod3.
\tag{10}
$$



The sign is exact: $L\tau_H/(3L\tau_T)=(-1)^{-H}=-1$.

The cofactor identity is



$$
\mathsf Z_{0,:}
 +\sum_{r=1}^n(-1)^r(\delta_r/\delta_0)\mathsf Z_{r,:}=0.
$$



Since $A$ is invertible over $\mathbb Z_3$, the vector of the
last $n$ coefficients is exactly $-\mathsf Z_{0,:}A^{-1}$.
Divide by 3 and use (7), (10). Now $j_0\equiv2\pmod3$, so row
$j_0$ of $U^{-1}$ is just $e_{j_0}^{\mathsf T}$, by (8).
It follows that



$$
(-1)^r\frac{\delta_r}{3\delta_0}
 \equiv\mathbf1_{r=j_0+1}=\mathbf1_{r=2H}\pmod3.
\tag{11}
$$



As $2H$ is even, (11) is exactly (4). This proof uses only the
inverse modulo 3 to propagate a row divisible by 3; it makes no
assumption about later inverse coefficients or an indefinitely repeating
digit recursion.

## 4. The weighted minimum and the remaining numerator

Legendre's factorial formula gives



$$
v_3(R)=n/2,
\tag{12}
$$



because $n=3^\nu-1$ and $2n=2\cdot3^\nu-2$ both have base-three
digit sum $2\nu$. Similarly $2n=6H-2$ and $n+2H=5H-1$
have the same base-three digit sum, so



$$
v_3(c_{2H})=(H-1)/2.
\tag{13}
$$



The minor at $r=2H$ has valuation one by (4); hence
$d\le1+(H-1)/2$. All other nonzero-index minors have valuation at
least two, while the $r=0$ weighted term has valuation $n/2\ge4$.
The selected term also has valuation at least two. This proves $d\ge2$
and all of (5).

There is a convenient exact translation into the actual primitive
Rodrigues polynomial $V_n(t)=\sum_{r=0}^nV_rt^r$. Comparing the
already established identities for
$W=t^n(t-1)^nV$ and its cofactor transport gives



$$
V_r=(-1)^{n+r}c_r\delta_r/h.
\tag{14}
$$



The new exponential border is therefore



$$
\widehat P_e(1)=\sum_{r=0}^nV_rD_{n,r}.
\tag{15}
$$



For $n\equiv2\pmod3$, the finite border formula in the preceding
note has only its constant term, so $D_{n,r}\equiv1\pmod3$ for
every $r$. Consequently



$$
\boxed{\widehat P_e(1)\equiv V_n(1)\pmod3.}
\tag{16}
$$



No unit assertion about $V_n(1)$ is inferred from its nonzero real
value or the positivity of a normalized real Toeplitz quadratic form.

For $\nu\ge3$, (5) and the arctangent bound in the passed gate give



$$
v_3(\widehat P_a(1))\ge H-1-\nu>0.
\tag{17}
$$



Thus a proof that $V_n(1)$ is a 3-unit on this family would make
$N_n$ a unit and immediately transfer the linear bound (5) to
$q_n$. A factorial-depth bound would additionally need
$d=O(\nu)$, or a suitable direct estimate on
$v_3(Z_n)-v_3(N_n)$. Neither assertion is established here.

The exact next deeper target is the coefficient of the last row in
$-\mathsf Z_{0,:}A^{-1}$ beyond (11), together with the weighted
sum (15). A tempting pattern would place a unit at valuation $s$
near row $T-T/3^s$, eventually reaching row $n$. The proof above
establishes only $s=1$. At later precision, corrections to the full
matrix inverse interact with earlier layers; dropping those corrections
would be an unjustified extrapolation.

## 5. Scope relative to the main objective

This family is outside every odd-prime saturation theorem at $p=3$,
because $3\nmid n$. Nevertheless its normalized cofactor matrix has
full column rank modulo 3, and its simultaneous endpoint denominator is
a 3-unit. These are new exact statements, distinct from the known
rank formula for primes dividing $n$.

They do not prove shrinking or nonshrinking of the actual primitive
linear forms. In particular, the lower bound for $Z_n$ in (5) must
not be reported as a lower bound for $q_n$ without a numerator bound.
The next arithmetic task is now a specified higher residue-state and
endpoint-value problem, rather than a guessed transfer of a factorial
clearing factor.

That target was subsequently bypassed by the exact row-difference
determinant in raw_ternary_factorial_denominator_subsequence.md, proving
$d_3+e_3=\nu$ and $v_3(q_{3^\nu-1})=(3^\nu-1)/2-\nu$.
