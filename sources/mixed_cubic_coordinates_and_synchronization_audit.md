> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Actual item-133 mixed-cubic coordinates: exact residue formulas, content bounds, and beta synchronization

Date: 2026-08-28

## 1. Scope and verdict

This note studies the actual item-133 pair, not an abstract countermodel.  Put



$$
n=6m,\qquad M=M_{4m+1},\qquad
 T=\prod_{2m<p<3m}p,\qquad K=M/T,
$$



and let $G=\mathcal G_m$ be the squarefree Cartier product.  Thus



$$
D_m^\sharp=2^{9m+5}K,\qquad
 U_m=\frac{D_m^\sharp A_m}{G},\qquad
 V_m=\frac{D_m^\sharp B_m}{G},\qquad
 c_m=\gcd(U_m,V_m).
$$



The main new exact conclusions are:

1. the $\pi$-coordinate is an explicit Gaussian-integer coefficient
   determinant and has an explicit rational-diagonal generating function;
2. every $v_p(c_m)$ has an exact formula in terms of two integral raw
   coordinates and the already known $M,T,G$;
3. the published irrationality measure of $\pi$, combined with the frozen
   saddle theorem, gives a rigorous upper bound
   

$$
\limsup_{m\to\infty}\frac{\log c_m}{6m}
   \le h-\frac d{\mu_*}\simeq1.99566316,
$$


   where $\mu_*=7.103205334137\ldots$; the safe rational exponent
   $36/5$ gives the fully explicit bound $2.000086342704984\ldots$;
4. the final beta matching content is supported only at primes for which
   $v_p(b_m)=v_p(q_N)>0$, a strictly stronger restriction than
   $g_m\mid\gcd(b_m,q_N)$.

These results do **not** determine a positive lower bound for
$\liminf (6m)^{-1}\log c_m$, do not prove an upper bound below the required
$1.156147151964\ldots$, and do not close the $e+\pi$ problem.

## 2. Exact Gaussian residue coordinates

Let coefficient conjugation act only on $\mathbb Q(i)$, not on the formal
variable, and define



$$
\Psi(v)=
 \frac{(1+2v)^6(1+(1-i)v)^6}{v^4(1+v)^4},
$$





$$
a_0(v)=\frac{1+(1+i)v}{1+v},\qquad
 a_1(v)=\frac{(1-i)(1+(1+i)v)^4}{v(1+v)^2}.
$$



Define Gaussian integers



$$
J_{0,m}=\operatorname {CT}_v a_0(v)\Psi(v)^m,
 \qquad
 J_{1,m}=\operatorname {CT}_v a_1(v)\Psi(v)^m.                 \tag{2.1}
$$



They are exactly the item-133 contour coefficients $I_{0,m}$ and
$8I_{1,m}$.  If $c_{0,1},c_{1,1}$ denote the simple residues at $i$,
then



$$
C_m=\frac{1-i}{4}\left(\frac{-i}{128}\right)^m,
 \qquad c_{0,1}=C_mJ_{0,m},\qquad c_{1,1}=\frac{C_mJ_{1,m}}8.   \tag{2.2}
$$



Since item 133 proves



$$
B_m=2\operatorname {Im}(c_{1,1}\overline {c_{0,1}}),
$$



(2.2) gives the exact determinant



$$
\boxed{
 B_m=\frac{\operatorname {Im}(J_{1,m}\overline {J_{0,m}})}
                 {2^{14m+5}}.}                                    \tag{2.3}
$$



Consequently



$$
\widehat B_m:=2^{9m+5}B_m
 =2^{-5m}\operatorname {Im}(J_{1,m}\overline {J_{0,m}})\in\mathbb Z. \tag{2.4}
$$



The integrality in (2.4) is equivalent to the already proved dyadic
integrality of $B_m$; it is not inferred from finite data.

For an entirely explicit finite sum, (2.1) says



$$
\begin{split}
J_{0,m}={}&
 \sum_{\substack{j,k\ge0,\ e\in\{0,1\}\\t=4m-j-k-e\ge0}}
 \binom{6m}{j}\binom{6m}{k}
 2^j(1-i)^k(1+i)^e
 (-1)^t\binom{4m+t}{t},\\
J_{1,m}={}&(1-i)
 \sum_{\substack{j,k\ge0,\ 0\le e\le4\\t=4m+1-j-k-e\ge0}}
 \binom{6m}{j}\binom{6m}{k}\binom4e
 2^j(1-i)^k(1+i)^e
 (-1)^t\binom{4m+1+t}{t}.
                                                               \tag{2.5}
\end{split}
$$



### Generating functions and recurrences

The two residue generating functions are the explicit constant terms



$$
\mathcal J_s(z)=\sum_{m\ge0}J_{s,m}z^m
 =\operatorname {CT}_v\frac{a_s(v)}{1-z\Psi(v)}.                \tag{2.6}
$$



They are algebraic functions (equivalently, diagonals of rational functions
in two variables), hence their real and imaginary coefficient sequences are
P-recursive.

Taking the Hadamard product in (2.4) gives an explicit generating function
for the integral $\pi$-coordinate:



$$
\boxed{
 \sum_{m\ge0}\widehat B_mz^m
 =\operatorname {Im}\operatorname {CT}_{v,w}
 \frac{a_1(v)\overline {a_0(w)}}
 {1-(z/32)\Psi(v)\overline {\Psi(w)}}.}                          \tag{2.7}
$$



This is a rational diagonal, so $(\widehat B_m)$ is rigorously D-finite
and P-recursive.  Formula (2.7), rather than a guessed finite recurrence, is
the cleanest exact recurrence certificate currently available.

The rational coordinates $R_s$, and therefore $A_m$, are also finite
hypergeometric/Hermite sums.  An explicit algorithm is the frozen Hermite
reduction: at denominator level $j$, reduce the current numerator modulo
$Q$, multiply by $(Q')^{-1}=(x^2-x)/4\pmod Q$, divide by $-(j-1)$,
subtract the corresponding exact derivative, and continue at level $j-1$.
The endpoint increments are



$$
S_j(1)/4^{j-1}-S_j(0),
$$



and the final polynomial quotient contributes its coefficient of $x^r$
divided by $r+1$.  This is an exact finite recurrence for $R_s$; it does
not by itself yield a useful recurrence for the normalized gcd $c_m$.

## 3. Exact valuation reduction for $U_m,V_m,c_m$

Define the integral rational coordinate



$$
\widehat A_m:=2^{9m+4}M A_m\in\mathbb Z.                         \tag{3.1}
$$



Equations (2.4), (3.1), and $D_m^\sharp=2^{9m+5}M/T$ give



$$
\boxed{
 U_m=\frac{2\widehat A_m}{TG},\qquad
 V_m=\frac{K\widehat B_m}{G}.}                                   \tag{3.2}
$$



Both quotients are integers by item 133.  Therefore, with $v_p(0)=+\infty$
if ever needed,



$$
\boxed{
\begin{split}
 v_p(U_m)&={\bf1}_{p=2}+v_p(\widehat A_m)-v_p(T)-v_p(G),\\
 v_p(V_m)&=v_p(K)+v_p(\widehat B_m)-v_p(G),\\
 v_p(c_m)&=\min\{v_p(U_m),v_p(V_m)\}.
                                                               \tag{3.3}
\end{split}}
$$



This is a complete exact local formula.  It isolates the unresolved part:
one must control simultaneous $p$-adic zeros of the two actual integral
sequences $\widehat A_m,\widehat B_m$.  D-finiteness alone supplies no
such common-zero estimate.

### A large-prime reduction to the two logarithmic residues

There is a sharper exact statement for fresh primes.  Write



$$
\omega_s=\frac{u^{6m}}{Q^{4m+1+s}}\,dx\qquad(s=0,1).
$$



For every prime $p>6m$, all coordinate denominators are $p$-units and



$$
\boxed{
 p\mid \widehat A_m,\widehat B_m
 \quad\Longleftrightarrow\quad
 L_0\equiv L_1\equiv0\pmod p.}                                  \tag{3.4}
$$



The reverse implication is immediate from the definitions of $A_m,B_m$.
For the forward implication, suppose first that $(L_0,L_1)\ne(0,0)$ in
$\mathbb F_p^2$ and consider



$$
\Omega=L_1\omega_0-L_0\omega_1
 =\frac{u^{6m}(L_1Q-L_0)}{Q^{4m+2}}\,dx.                         \tag{3.5}
$$



Its logarithmic coordinate vanishes identically.  The congruences
$A_m\equiv B_m\equiv0\pmod p$ say that its other two definite-integral
coordinates vanish.  Since $Q$ is separable, the pole orders are less
than $p$, and (3.5) is proper at infinity, its vanishing simple residues
make it an exact rational differential $dF$; the rational coordinate says
$F(0)=F(1)$.

If $p=6m+1$, local differentiation at $0$ and $1$ forces respectively
$L_1-L_0=0$ and $4L_1-L_0=0$, already a contradiction.  If
$p>6m+1$, subtracting the common endpoint value shows



$$
F-C=\frac{u^{6m+1}(ax+b)}{Q^{4m+1}}.                            \tag{3.6}
$$



The numerator has the stated form because (3.5) is $O(x^{-3})dx$ at
infinity.  Differentiating (3.6), the polynomial multiplying
$u^{6m}/Q^{4m+2}$ is



$$
D=(6m+1)u'(ax+b)Q+uaQ-(4m+1)u(ax+b)Q'.                         \tag{3.7}
$$



For $D=L_1Q-L_0$, its $x^4$-coefficient gives
$b=(10m+2)a$, while equality of its $x$- and $x^2$-coefficients gives



$$
4a(4m+1)=0.
$$



Because $p>6m$, this forces $a=b=0$, and then $L_0=L_1=0$, the
desired contradiction.  This proves (3.4).

Thus the experimentally observed support statement has been reduced to the
cleaner assertion that the two adjacent log-residue coefficients never have
a common prime divisor greater than $6m$.  That last assertion remains
unproved.

As a small unconditional consequence, $TG$ is odd, while $K$ contains
a positive power of two.  Thus (3.2) shows $2\mid U_m,V_m$, so
$c_m\ge2$.  This still gives only



$$
\liminf_{m\to\infty}\frac{\log c_m}{6m}\ge0.                    \tag{3.8}
$$



## 4. A rigorous upper bound from the irrationality measure of $\pi$

Put



$$
a_m=U_m/c_m,\qquad b_m=|V_m|/c_m.
$$



For every rational $\tau>\mu_*$, where
$\mu_*=7.103205334137\ldots$ is the Zeilberger--Zudilin upper bound for
the irrationality measure of $\pi$, there is $C_\tau>0$ such that



$$
|a+b\pi|\ge C_\tau b^{1-\tau}
$$



for all integral $a$ and positive integral $b$.  Applying this to the
primitive item-133 pair gives



$$
c_m^\tau
 \le C_\tau^{-1}|U_m+V_m\pi|\,|V_m|^{\tau-1}.                 \tag{4.1}
$$



The frozen analytic theorem proves



$$
\frac1{6m}\log|V_m|\longrightarrow h,
 \qquad
 \limsup\frac1{6m}\log|U_m+V_m\pi|\le h-d.
$$



Taking limsups in (4.1) yields



$$
\limsup_{m\to\infty}\frac{\log c_m}{6m}
 \le h-\frac d\tau.                                                \tag{4.2}
$$



Letting $\tau\downarrow\mu_*$ gives



$$
\boxed{
 0\le\liminf\frac{\log c_m}{6m}
 \le\limsup\frac{\log c_m}{6m}
 \le h-\frac d{\mu_*}\simeq1.99566316016.}                       \tag{4.3}
$$



If only the rational exponent $\tau=36/5$ is used, the explicit right
side is



$$
h-\frac{5d}{36}=2.0000863427049848608\ldots .                    \tag{4.4}
$$



The matching threshold is



$$
h-d/2=1.1561471519642446123\ldots .                              \tag{4.5}
$$



Thus (4.3) is a genuine theorem but is far too weak to decide whether the
content lies above or below the required threshold.  No positive
exponential lower bound for $c_m$ follows from the current Cartier theorem:
that Cartier product has already been divided out in the definition of
$U_m,V_m$.

## 5. Exact beta synchronization and an equal-valuation theorem

Let



$$
L_m=a_m+\varepsilon b_m\pi>0,\qquad \gcd(a_m,b_m)=1,
$$



and let $p_N,q_N$ be the primitive beta pair.  Put



$$
\Delta=\gcd(b_m,q_N),\qquad b_m=\Delta b_0,
 \qquad q_N=\Delta q_0,
$$





$$
P^*=b_0p_N-\varepsilon q_0a_m,\qquad
 g=\gcd(P^*,\Delta).                                                \tag{5.1}
$$



For a prime $p$, set



$$
r=v_p(b_m),\qquad s=v_p(q_N).
$$



Then



$$
\boxed{
v_p(g)=
\begin{cases}
0,&r\ne s,\\
\min\{r,v_p(P^*)\},&r=s>0,\\
0,&r=s=0.
\end{cases}}                                                       \tag{5.2}
$$



Indeed, if $r>s$, then $p\mid b_0$, while $q_0a_m$ is a unit because
$\gcd(a_m,b_m)=1$; hence $P^*$ is a unit.  If $s>r$, then
$p\mid q_0$, while $b_0p_N$ is a unit because
$\gcd(p_N,q_N)=1$.  The equal case follows directly from (5.1).

Thus the archive bound $g\mid\Delta$ can be sharpened to



$$
\boxed{g\mid
 \prod_{p:\ v_p(b_m)=v_p(q_N)>0}p^{v_p(q_N)}.}                    \tag{5.3}
$$



The beta recurrence also gives, for every odd prime power $p^a$,



$$
q_{N+p^a}\equiv-q_N\pmod {p^a},
$$



and therefore



$$
v_p(q_N)=
 \max\{a\ge0:q_{N\bmod p^a}\equiv0\pmod {p^a}\}.               \tag{5.4}
$$



Every $q_N$ is odd, so neither $\Delta$ nor $g$ can use any dyadic
part of the mixed-cubic coordinates.

Equations (3.3), (5.2), and (5.4) are a complete prime-by-prime reduction
of the synchronization question.  At the optimal scale



$$
\frac{N\log N}{6m}\longrightarrow\frac d2,
 \qquad
 N\sim\frac{(d/2)6m}{\log m},                                     \tag{5.5}
$$



the required inequality becomes



$$
\begin{split}
 &\frac{\log c_m}{6m}
 +\frac1{6m}\sum_p\min\{r_{p,m},s_{p,N}\}\log p\\
 &\quad+\frac1{6m}\sum_{p:r_{p,m}=s_{p,N}>0}
       \min\{r_{p,m},v_p(P^*)\}\log p
 >h-d/2.                                                          \tag{5.6}
\end{split}
$$



No archived theorem controls either sum in (5.6) for the moving index
(5.5).  The period congruence makes the problem finite-state prime by prime,
but it does not bound the number or total logarithmic mass of the relevant
root classes.

## 6. Exact finite diagnostics (not asymptotic claims)

The item-140 certificate and the companion scripts in `scripts/` recompute all coordinates by exact rational
Hermite reduction.

* The exact $m\le100$, parity-compatible $N\le6m$ scan proves that every
  tested positive matched form has an exact rational lower bound greater
  than one.  For $m\ge80$, the largest tested
  $(6m)^{-1}\log(c_m\Delta_mg_m)$ is
  $0.257894809399\ldots$, attained at $(m,N)=(100,141)$, far below
  (4.5).  This is windowed finite data only.
* Trial division of the exact $c_m$ values from that scan found no prime
  factor larger than $6m$ for every $1\le m\le100$.  Independent exact
  checks at $m=150$ and $m=200$ also left cofactor one after division by
  primes at most $6m$.  This suggests the concrete support conjecture
  $p\mid c_m\Rightarrow p\le6m$, but proves it only for those indices.
* The exact content rates at the two isolated larger checks are
  $0.172286833139\ldots$ at $m=150$ and
  $0.164995723146\ldots$ at $m=200$.  They are diagnostics, not evidence
  for a limit theorem.
* Exact terms through $m=180$ found no polynomial recurrence modulo
  $10^9+7$ of order at most 16 and degree at most 8 (or order at most 20
  and degree at most 6) for any of
  $\Re J_0,\Im J_0,\Re J_1,\Im J_1,\widehat B$.  This only rules out that
  low-complexity search box; (2.7) proves that a P-recurrence exists.

## 7. Strongest next steps and decisive obstruction

1. Prove or refute the observed support statement
   $p>6m\Rightarrow p\nmid\gcd(\widehat A_m,\widehat B_m)$.  A proof must
   establish nondegeneracy of the two Hermite coordinates modulo $p$; the
   finite factorizations are not a substitute.
2. Support alone is insufficient.  One also needs a valuation-mass bound,
   for example a divisor of a fixed power of an explicit lcm, strong enough
   to put $(6m)^{-1}\log c_m$ on one side of (4.5).
3. Use (2.7) and the analogous Hermite multisum for $\widehat A_m$ to
   obtain creative-telescoping certificates, then compute a resultant or
   Casoratian whose prime divisors control simultaneous zeros.  The failed
   low-order search warns that this recurrence may be large.
4. For synchronization, the target is not merely $p\mid b_m,q_N$: the
   last content requires the exact equality
   $v_p(b_m)=v_p(q_N)$ plus the normalized congruence in (5.2).  Any claimed
   gain for $g_m$ that omits this condition is invalid.

The decisive present obstruction is therefore precise: the analytic side is
closed, and the residue sequences are holonomic, but no theorem bounds the
total mass of simultaneous $p$-adic zeros of the actual normalized
coordinates, either internally (for $c_m$) or against the moving beta root
classes (for $\Delta_m,g_m$).

