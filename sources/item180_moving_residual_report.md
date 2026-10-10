> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 180 — the moving residual determinant: an exact sub-prime recurrence and the remaining root-count barrier

Date: 2026-08-29

## 1. Scope and verdict

This item stays inside the Item 174 rank-two cell $e=1,\kappa=0$.  Thus



$$
2m=jp+s,\qquad p\ge 7\text{ prime},\qquad
 0\le s\le {p-1\over3},
\tag{1.1}
$$



with the parity condition $s\equiv j\pmod2$ on an actual $m$-row.  The
determinant depends only on $(p,s)$, and every admissible $s$ occurs for
some choice of $j$ of the required parity.

**PROVED — exact moving recurrence.**  Every determinant $\Delta_{p,s}$,
including the genuinely moving range $s\asymp p$, is reconstructed from
the coefficients below index $p$ of one rational series.  Those coefficients
satisfy the four-term recurrence (2.9), whose only division is by
$1,2,\ldots,p-1$.  This is an exact $O(p)$ finite-field algorithm for one
moving pair and does not form the degree-$\asymp p$ polynomial of Item 174.

**PROVED — positive-lift sector and an archimedean obstruction.**  In the
lower sector $p\ge5s+2$, every needed coefficient has a nonnegative integer
lift.  On every compact ratio interval inside $(0,1/5)$, at least one of
these lifts has exponential height in $p$.  Four exact off-ray examples have
a nonzero lifted integer determinant, with nonzero rows, yet that determinant
is divisible by $p$.  Consequently positivity, real nonvanishing, or saddle
size by itself cannot prove finite-field nonvanishing; a successful argument
must control the residue or its $p$-adic cancellation.

**PROVED — mean-mass transference.**  Let $r_p$ be the number of admissible
roots $s$ for a fixed prime.  If



$$
{r_p\over p}\longrightarrow0,
\tag{1.2}
$$



then the determinant-zero primes have mean logarithmic weight $o(M)$ on
$m\le M$; see (4.4).  Thus a positive order-$m$ mass on average would
force a genuinely linear root population in aggregate.  This is a
conditional implication: (1.2) is not proved here.

**PROVED COMPUTATION — finite diagnostic.**  For every prime
$7\le p\le1000$ and all $0\le s\le(p-1)/3$, exact recurrence evaluation
finds 169 roots among 25,454 pairs.  There are at most four roots for any
one prime in this range.  Forty-six roots are off the three known affine
rays; 32 of those have $p\ge200$ and
$1/20<s/p<8/25$.  This disproves localization of all finite zeros to the
known rays, but it is not a density theorem and the bound four is not
extrapolated.

**OPEN.**  No uniform proof of $r_p=o(p)$, no pointwise zero-rate theorem,
and no positive-mass family is obtained.  The arithmetic nature of
$e+\pi$ remains undecided.

## 2. Exact reduction to coefficients below $p$

Retain the Item 174 notation



$$
Q=1+x+x^2+x^3,\qquad
 P=x^{3s}J,\qquad
 J=(1-x)^{3s}Q^{p-2s-2}.
\tag{2.1}
$$



Introduce the formal power series



$$
A_s={ (1-x)^{3s}\over Q^{2s+2}}
     ={(1-x)^{5s+2}\over(1-x^4)^{2s+2}}
     =\sum_{n\ge0}a_nx^n.
\tag{2.2}
$$



Since $J=Q^pA_s$ and



$$
Q^p\equiv1+x^p+x^{2p}+x^{3p}\pmod p,
\tag{2.3}
$$



comparison below degree $p$ gives



$$
[x^n]J\equiv a_n\pmod p
             \qquad(0\le n<p).                         \tag{2.4}
$$



The degree of $J$ is



$$
D=3p-3s-6=2p+d-6,qquad d=p-3s,
\tag{2.5}
$$



and reciprocity gives



$$
x^DJ(1/x)=(-1)^sJ(x).           \tag{2.6}
$$



Applying (2.4) at the low end and (2.6) at the high end yields the two
Cartier rows exactly in $\mathbf F_p$:



$$
\begin{aligned}
 (\alpha_1,\beta_1)
   &=\bigl(a_{d-1},\;(-1)^sa_{p-5}\bigr),\\
 (\alpha_0,\beta_0)
   &=\left(\sum_{k=0}^3a_{d-1-k},\;
       (-1)^s\sum_{k=0}^3a_{p-5+k}\right).
\end{aligned}                                            \tag{2.7}
$$



Here and below a negative-index coefficient is zero.  The common
$a_{d-1}a_{p-5}$ term cancels, so



$$
\boxed{
 \Delta_{p,s}=(-1)^s\left[
 (a_{d-2}+a_{d-3}+a_{d-4})a_{p-5}
 -(a_{p-4}+a_{p-3}+a_{p-2})a_{d-1}
 \right]\pmod p.}                                      \tag{2.8}
$$



Logarithmic differentiation of (2.2), followed by coefficient comparison,
gives



$$
\boxed{
 (n+1)a_{n+1}=(n-5s-2)a_n+(n+8s+5)a_{n-3}
               -(n+3s+2)a_{n-4}.}                      \tag{2.9}
$$



Starting from $a_0=1$, (2.9) determines every coefficient needed in
(2.8) for $0\le n\le p-2$.  Its divisor $n+1$ is a unit modulo $p$.
This proves the claimed exact moving algorithm.

The certificate independently constructs the original polynomial $P$ and
checks both rows against (2.7) for all 395 admissible pairs with
$p\le101$.  This cross-check is not needed for the algebraic proof, but it
guards all shifts, signs, and endpoint indices.

## 3. The positive lift and why real asymptotics do not close the problem

Assume



$$
b=p-5s-2\ge0.                  \tag{3.1}
$$



In $\mathbf F_p[[x]]/(x^p)$, the freshman's-dream congruence gives



$$
(1-x)^{5s+2}=(1-x)^{p-b}
 \equiv(1-x)^{-b}\pmod{x^p}.
\tag{3.2}
$$



Therefore, for every $0\le n<p$,



$$
a_n\equiv g_n\pmod p,
 \qquad
 {1\over(1-x)^b(1-x^4)^{2s+2}}=\sum_{n\ge0}g_nx^n,
 \qquad g_n\in\mathbf Z_{\ge0}.                         \tag{3.3}
$$



The certificate verifies (3.3) coefficient by coefficient for 236 pairs
with $p\le101$.  It uses the independent exact integer recurrence



$$
\begin{aligned}
 (n+1)g_{n+1}={}&(n+b)g_n+(n-3+4c)g_{n-3}\\
                &-(n-4+b+4c)g_{n-4},\qquad c=2s+2,
\end{aligned}                                            \tag{3.4}
$$



and checks every displayed division in $\mathbf Z$.

This positive lift has exponential rather than polynomial height in the
moving interior.  Indeed,



$$
g_{d-1}\ge [x^{d-1}](1-x)^{-b}
            ={b+d-2\choose d-1}.                        \tag{3.5}
$$



On a fixed compact interval $K\subset(0,1/5)$ for $s/p$, both $b$
and $d-1$ are bounded below by positive multiples of $p$.  Uniform
Stirling bounds applied to (3.5) give constants $c_K>0,p_K$ such that



$$
g_{d-1}\ge e^{c_Kp}
                         \qquad(p\ge p_K).              \tag{3.6}
$$



Thus an archimedean saddle estimate does not put the relevant integer into
the interval $(-p,p)$; reduction wraps around many times.

For a sharper exact obstruction, define the lifted determinant



$$
E_{p,s}=(g_{d-2}+g_{d-3}+g_{d-4})g_{p-5}
        -(g_{p-4}+g_{p-3}+g_{p-2})g_{d-1}.              \tag{3.7}
$$



Equation (3.3) proves $\Delta_{p,s}\equiv(-1)^sE_{p,s}\pmod p$.
The following are exact integer computations; each pair is off every known
ray and lies in $1/20<s/p<1/5$:



$$
\begin{array}{c|r|r|r|r|r}
p&s&b&\operatorname{bits}|E_{p,s}|&v_p(E_{p,s})&E_{p,s}/p\pmod p\\ \hline
337&52&75&586&1&107\\
751&83&334&1847&1&412\\
797&140&95&1119&1&388\\
857&71&500&2458&1&99
\end{array}                                              \tag{3.8}
$$



All four integers are negative and nonzero.  In all four cases both
finite-field rows in (2.7) are nonzero, so the zero is genuine
proportionality rather than a zero-row convention.  The certificate stores
the two rows and a SHA-256 digest of every full integer.  These witnesses
do not obstruct a future $p$-adic saddle argument.  They do prove that a
real sign, real nonvanishing, total positivity of individual coefficients,
or an exponential-size estimate alone is insufficient.

## 4. Root counts and logarithmic mass

Let



$$
r_p=\#\left\{0\le s\le{p-1\over3}:\Delta_{p,s}=0\right\}. \tag{4.1}
$$



For a positive integer $m$, let $L(m)$ be the sum of $\log p$ over
the determinant-zero primes occurring in the actual $\kappa=0$ slice at
that $m$, counting each prime once.  Every such row satisfies



$$
2m\equiv s\pmod p.          \tag{4.2}
$$



For fixed $(p,s)$, since $p$ is odd, at most $M/p+1$ integers
$m\le M$ satisfy (4.2).  Also an actual prime obeys $p\le4M+1$.
Discarding the other cell restrictions can only enlarge the count, and
hence



$$
\boxed{
 \sum_{m\le M}L(m)
 \le\sum_{p\le4M+1}r_p\left({M\over p}+1\right)\log p.} \tag{4.3}
$$



Suppose $r_p/p\to0$.  Given $\varepsilon>0$, all sufficiently large
primes have $r_p\le\varepsilon p$.  Chebyshev's bound
$\sum_{p\le X}\log p=O(X)$, together with
$\sum_{p\le X}p\log p\le X\sum_{p\le X}\log p=O(X^2)$,
applied to (4.3) gives



$$
{1\over M}\sum_{m\le M}L(m)=o(M).   \tag{4.4}
$$



The finitely many omitted small primes contribute $o(M)$ to the left
side of (4.4).  This proves the mean-mass transference theorem.  It neither
proves (1.2) nor bounds an exceptional individual $m$.

## 5. Finite moving diagnostics

The deterministic scan covers all 25,454 admissible pairs for the 165
primes $7\le p\le1000$.  Its exact counts are



$$
\begin{array}{l|r}
\text{determinant-zero pairs}&169\\
\text{primes with at least one zero}&117\\
\text{off-known-ray zero pairs}&46\\
\text{off-ray pairs with }p\ge200,\ 1/20<s/p<8/25&32.
\end{array}                                              \tag{5.1}
$$



The root-count histogram by prime is



$$
\begin{array}{c|rrrrr}
r_p&0&1&2&3&4\\ \hline
\#p&48&78&28&9&2.
\end{array}                                              \tag{5.2}
$$



The two four-root examples are



$$
(p;s\text{-roots})=(337;25,45,52,111),\qquad
                     (661;102,107,180,219).              \tag{5.3}
$$



The 169-pair ordered list has digest

```
a36e3c999d809284c2b16cc22be4d5656d3b8362113b502ed5a45787b59a1907
```

and is stored in full in the JSON.  The count at most four is consistent
with the desired $r_p=o(p)$, but a finite bounded scan cannot prove even
sublinearity.  Conversely, the 32 interior off-ray pairs show that no
argument may simply replace the moving zero set by the three structural
lines.

## 6. Replay, dependencies, and status

The standard-library script
`scripts/item180_moving_residual_certificate.py` writes
`results/item180_moving_residual_certificate.json` by default after archive
installation.  In the staging directory it writes beside itself.  A replay
with the same limits must be byte-identical.  The certificate contains no
randomness, external package, network call, or floating-point proof step.

The exact Item 174 dependencies are pinned in the JSON.  In particular, the
Item 174 report, certificate, and canonical JSON hashes are respectively

```
9c5be8adfc33252de0d4c49153b7633f7b6dbe0ee5e03d0aeab7dda5d083e7c2
4c3e64285d41b936ea8c61ad1f99194330b8f64d910ecb63676d482fa5f6c891
125fec0cd9d2444c9296302a884845d2a8d6880a54072d09c0d8e1f7778cc019
```

Final separation:

* **PROVED:** (2.7)–(2.9), the positive lift (3.3), the exponential-height
  obstruction (3.5)–(3.6), the exact divisibility witnesses (3.8), and the
  conditional mean-mass implication (4.3)–(4.4).
* **EXPERIMENTAL FINITE:** the complete $p\le1000$ root counts (5.1)–(5.3).
* **OPEN:** a uniform sublinear bound for $r_p$, a pointwise mass theorem,
  and any consequence for the irrationality problem.
