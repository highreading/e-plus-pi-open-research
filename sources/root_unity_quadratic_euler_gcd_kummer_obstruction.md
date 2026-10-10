> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The quadratic Euler gcd: an exact Kummer-period obstruction

## Separating the elementary index factor from adjacent Euler-irregular branches

Checked: 2026-08-27 UTC

## 1. Scope and conclusion

Let the secant Euler numbers be defined by



$$
\operatorname {sech}z
       =\sum_{j\geq0}E_j\frac {z^j}{j!},
       \qquad E_{2j+1}=0,                                    \tag{1}
$$



and put



$$
A_N=(2N+2)(2N+1),\qquad
 G_N=\gcd\bigl(A_N|E_{2N}|,|E_{2N+2}|\bigr).                 \tag{2}
$$



This is the exact primitive-content datum in the quadratic closer-root
construction.  This note does **not** prove the hoped-for estimate
$\log G_N=o(N\log N)$.  It proves a sharp reduction explaining precisely
what remains.

Define first



$$
H_N=\gcd(|E_{2N}|,|E_{2N+2}|).               \tag{3}
$$



Then



$$
\boxed{
 G_N=H_N\gcd\left(A_N,\frac {|E_{2N+2}|}{H_N}\right),
 \qquad H_N\mid G_N\mid A_NH_N.}                             \tag{4}
$$



Thus the factor in (2) coming only from $A_N$ has logarithm
$O(\log N)$.  It is not the difficult part.

For an odd prime $p$, let



$$
a_p(N)=\max\{a\geq1:\ \varphi(p^a)\leq 2N+2\},             \tag{5}
$$



with $a_p(N)=0$ if the set is empty.  Split $H_N$ primewise as



$$
S_N=\prod_{p\ \mathrm{odd}}p^{\min(v_p(H_N),a_p(N))},
 \qquad J_N=\frac {H_N}{S_N}.                                \tag{6}
$$



The main theorem is



$$
\boxed{
 S_N\mid\operatorname {lcm}(1,2,\ldots,3N+3),\qquad
 J_N\mid G_N\mid A_N\operatorname {lcm}(1,\ldots,3N+3)J_N.} \tag{7}
$$



Consequently, by the standard Chebyshev estimate
$\log\operatorname {lcm}(1,\ldots,x)=\psi(x)=O(x)$,



$$
\boxed{\log G_N=\log J_N+O(N).}                 \tag{8}
$$



Every prime-power layer counted by $J_N$ is a simultaneous pair



$$
p^a\mid E_{2N},\qquad p^a\mid E_{2N+2},
       \qquad 2N+2<\varphi(p^a),                              \tag{9}
$$



so both indices lie strictly inside the first $p^a$-Kummer period.
Conversely, every excess layer in such a pair occurs in $J_N$.  Hence



$$
\boxed{
 \log G_N=o(N\log N)
 \quad\Longleftrightarrow\quad
 \log J_N=o(N\log N).}                                      \tag{10}
$$



This quarantines all ordinary periodic lifts, including the observed
$149$ and $241$ endpoint branches, in the harmless factor $S_N$.
The missing arithmetic input is a quantitative bound for simultaneous
**adjacent, first-period, higher-order Euler-irregular pairs**.  Kummer
periodicity by itself gives no such bound.

Nothing in this note classifies $e+\pi$.

## 2. Exact separation of the index factor

Write



$$
|E_{2N}|=H_Nu_N,\qquad |E_{2N+2}|=H_Nv_N,
 \qquad \gcd(u_N,v_N)=1.                                    \tag{11}
$$



Then



$$
\begin{aligned}
 G_N
   &=H_N\gcd(A_Nu_N,v_N)\\
   &=H_N\gcd(A_N,v_N),
 \end{aligned}                                               \tag{12}
$$



which proves (4).  In particular, even a complete classification of
$\gcd(A_N,E_{2N+2})$ would change $\log G_N$ by only $O(\log N)$.
Finite grids do show several primes in this easy quotient, not only $5$;
that observation is arithmetically harmless because the quotient always
divides $A_N$.

## 3. Prime-power Kummer divisibility

The needed input is the prime-power Euler congruence



$$
E_{\varphi(p^a)+2k}
   \equiv
   \left(1-(-1)^{(p-1)/2}p^{2k}\right)E_{2k}pmod {p^a},      \tag{13}
$$



valid for every odd prime $p$, $a\geq1$, and $k\geq1$.
It is equation (2.2) in J. B. Cosgrave and K. Dilcher,
*On a congruence of Emma Lehmer related to Euler numbers*, Acta
Arith. 161 (2013), 47--67.  Their paper cites the earlier
prime-power Kummer sources and also gives the power-sum congruence used
below.

The multiplier in parentheses in (13) is congruent to $1\pmod p$, hence
is a $p$-adic unit.  Therefore



$$
p^a\mid E_{\varphi(p^a)+2k}
       \quad\Longleftrightarrow\quad
 p^a\mid E_{2k}.                                             \tag{14}
$$



Iterating (14) upward, or reversing an upward step, proves the following
exact divisibility-period lemma.

**Lemma 3.1.**  If $u,v$ are positive even integers and
$u\equiv v\pmod {\varphi(p^a)}$, then



$$
p^a\mid E_u\quad\Longleftrightarrow\quad
                  p^a\mid E_v.                               \tag{15}
$$



The positivity restriction matters: residue zero is represented by
$\varphi(p^a)$, not by $0$, because (13) starts with $k\geq1$.

For a positive even integer $u$, let



$$
[u]_{p^a}\in\{2,4,\ldots,\varphi(p^a)\}                    \tag{16}
$$



be its unique representative modulo $\varphi(p^a)$.  Put
$r_{p,a}(N)=[2N]_{p^a}$.  Lemma 3.1 gives the exact criterion



$$
p^a\mid H_N
 \quad\Longleftrightarrow\quad
 \begin{cases}
 r_{p,a}(N)\leq\varphi(p^a)-2,\\
 p^a\mid E_{r_{p,a}(N)},\\
 p^a\mid E_{r_{p,a}(N)+2}.
 \end{cases}                                                  \tag{17}
$$



Indeed, if $r_{p,a}(N)=\varphi(p^a)$, then the next representative is
$2$, and $E_2=-1$, so simultaneous divisibility is impossible.
Equation (17) is an exact all-parameter description; it is not a finite
diagnostic.

It also proves prime-power propagation.  If a seed



$$
p^a\mid E_r,E_{r+2},qquad
               2\leq r\leq\varphi(p^a)-2,                    \tag{18}
$$



exists, then



$$
p^a\mid H_N\quad\text{for every}\quad
 N\equiv r/2\pmod {\varphi(p^a)/2}.                           \tag{19}
$$



Thus periodic recurrence of a factor is expected once a seed exists; it
does not make the seed small or bound its valuation.

## 4. The complete mod-$p$ boundary classification

At level $a=1$, criterion (17) becomes especially transparent.  If



$$
r=[2N]_p\in\{2,4,\ldots,p-1\},                              \tag{20}
$$



where the notation means the representative modulo $p-1$, then a common
prime divisor is possible only for $r\leq p-3$.

For $2\leq r\leq p-5$, one has



$$
p\mid H_N
 \quad\Longleftrightarrow\quad
 p\mid E_r\ \text{and}\ p\mid E_{r+2}.                      \tag{21}
$$



This is a pair of adjacent ordinary Euler-irregular indices inside the
first period.

The endpoint $r=p-3$ has a structural second zero for one congruence
class of primes.  Cosgrave--Dilcher's power-sum congruence is



$$
E_m\equiv\sum_{j=0}^{p-1}(-1)^j(2j+1)^m\pmod p,
 \qquad m\geq1.                                               \tag{22}
$$



Set $m=p-1$.  Fermat's theorem makes every summand $1$, except
the unique zero base at $j=(p-1)/2$.  Since
$\sum_{j=0}^{p-1}(-1)^j=1$,



$$
E_{p-1}\equiv
             1-(-1)^{(p-1)/2}\pmod p.                         \tag{23}
$$



Consequently



$$
\boxed{
 p\mid E_{p-3},E_{p-1}
 \quad\Longleftrightarrow\quad
 p\equiv1\pmod4\ \text{and}\ p\mid E_{p-3}.}              \tag{24}
$$



For such a prime, (19) gives



$$
p\mid H_N\quad\text{whenever}\quad
 N\equiv\frac {p-3}{2}\pmod {\frac {p-1}{2}}.               \tag{25}
$$



The examples in the deterministic replay are



$$
\begin{array}{c|c|c}
 p&N\text{ in the first period}&\text{next occurrences}\ \\ \hline
 149&73&147,221,295,\ldots\\
 241&119&239,359,479,\ldots
 \end{array}                                                   \tag{26}
$$



In particular,



$$
\gcd(E_{146},E_{148})=149,\qquad
 \gcd(E_{294},E_{296})=149,                                  \tag{27}
$$



so consecutive secant Euler numbers are not generally coprime, and the
factor need not be tied only to the first occurrence.

## 5. Proof of the Kummer-period decomposition

Let $X=2N+2$.  If $a_p(N)\geq1$, then



$$
p^{a_p(N)}
   =\frac p{p-1}\varphi\bigl(p^{a_p(N)}\bigr)
   \leq\frac32X=3N+3,                                        \tag{28}
$$



because $p\geq3$.  Hence every prime-power factor in $S_N$ is at most
$3N+3$, proving



$$
S_N\mid\operatorname {lcm}(1,\ldots,3N+3). \tag{29}
$$



Combining this with (4) gives (7), and the Chebyshev estimate gives (8).

Now suppose a layer $p^a$ occurs in $J_N$.  Then
$a>a_p(N)$, so



$$
\varphi(p^a)>2N+2.                      \tag{30}
$$



Thus the representatives in (17) are the actual indices $2N$ and
$2N+2$, proving (9).  Conversely, every valuation layer of $H_N$ above
$a_p(N)$ is included in $J_N$ by definition.  This proves the claimed
exact reduction and (10).

It is useful to emphasize what (30) removes.  The endpoint seed
$(p,p-3)$, followed by the structural zero at $p-1$, has period
$p-1\leq2N+2$ at every occurrence (25); its first-power contribution is
therefore in $S_N$, not $J_N$.  A large $J_N$ requires either an
ordinary adjacent irregular pair with $p>2N+3$, or an adjacent
higher-order pair $p^a$ beyond all periods that fit below $2N+2$.

## 6. Consequence for the primitive quadratic height

The closer-root audit gives the primitive endpoint polynomial



$$
\mathscr C_N(T)
   =\frac {4A_N|E_{2N}|-|E_{2N+2}|T^2}{G_N},
 \qquad
 H(\mathscr C_N)=\frac {4A_N|E_{2N}|}{G_N}.                   \tag{31}
$$



The beta-value formula for Euler numbers and Stirling's formula give



$$
\log\bigl(4A_N|E_{2N}|\bigr)
                         =2N\log N+O(N).                      \tag{32}
$$



Using (8), one obtains the exact arithmetic ledger



$$
\boxed{
       \log H(\mathscr C_N)
           =2N\log N-\log J_N+O(N).}                          \tag{33}
$$



Thus the desired estimate $\log G_N=o(N\log N)$ would imply



$$
\log H(\mathscr C_N)=(2+o(1))N\log N.            \tag{34}
$$



Since the analytic relative gain is only



$$
-\log\frac {|\mathscr C_N(\pi)|}{H(\mathscr C_N)}
       =2N\log3+O(1),                                        \tag{35}
$$



(34) would put this fixed-degree family firmly on the factorial-height
side of the polynomial $e$-measure comparison.  Without a bound for
$J_N$, finite factorizations cannot justify (34).

## 7. What a direct resultant does and does not give

There is a natural elimination formulation.  Let



$$
\mathcal F_m(T)=\sum_{j=0}^m\binom mjE_jT^{m-j}
                =2^mE_m\left(\frac {T+1}{2}\right),          \tag{36}
$$



where the last $E_m(x)$ is the Euler polynomial.  For even $m\geq2$,
$\mathcal F_m(T)$ is divisible in $\mathbb Z[T]$ by $T^2-1$.  Put



$$
\mathcal U_m(T)=\frac {\mathcal F_m(T)}{T^2-1}. \tag{37}
$$



Then



$$
\mathcal U_m(0)=-E_m,                       \tag{38}
$$



so every common Euler divisor divides both specialized values of
$\mathcal U_{2N}$ and $\mathcal U_{2N+2}$.  If the reduced Sylvester
resultant



$$
\mathcal R_N=\operatorname {Res}_T
          (\mathcal U_{2N}(T),\mathcal U_{2N+2}(T))            \tag{39}
$$



is nonzero, the Bezout identity gives $H_N\mid\mathcal R_N$.

This is not a useful uniform bound at the required scale.  Indeed
$\deg\mathcal U_m=m-2$.  The coefficient of $T^{m-j}$ in
$\mathcal F_m$ has modulus at most
$\binom mjj!\leq m!$, since $|E_j|\leq j!$.  Synthetic division by
$T^2-1$ expresses each coefficient of $\mathcal U_m$ as a sum of at
most $m/2$ such coefficients.  Hence
$H(\mathcal U_m)\leq m\,m!$, which is
$\exp(O(m\log m))$.  Hadamard's inequality on the Sylvester determinant
therefore gives only



$$
\log|\mathcal R_N|=O(N^2\log N)           \tag{40}
$$



when the resultant is nonzero.  This is larger, not smaller, than the
entire $O(N\log N)$ Euler-number scale.  The small exact resultants in the
certificate verify the normalization and the forced reflection square,
but they are not extrapolated.  A useful resultant argument would still
need a new factor isolation that removes precisely the first-period
adjacent irregular component $J_N$.

## 8. Arithmetic status and precise obstruction

The reduction (7)--(10) is unconditional.  What is not proved here is a
uniform estimate for the product of all simultaneous first-period adjacent
irregular layers.  Ordinary Kummer congruences explain how a known layer
recurs; they do not bound how many adjacent seed pairs exist, how large
their primes can be relative to the indices, or how high their
prime-power lifts can be.

Equivalently, in the language of the $p$-adic Dirichlet $L$-functions
attached to the mod-$4$ character, the two adjacent indices belong to
two neighboring Kummer branches.  Standard one-branch lifting theory does
not supply the simultaneous quantitative bound required for $J_N$.
This note uses that interpretation only to identify the missing lemma; no
unproved statistical model for irregular pairs enters any theorem.

The deterministic replay checks the exact recurrence through $N=1000$,
the prime-power Kummer formula on a stated finite grid, the factorization
(4), the endpoint classification, the $149/241$ periodic examples, the
decomposition (6)--(7), and small centered resultants.  Those computations
are certificates of the displayed identities and counterexamples, not a
classification of irregular pairs.

## 9. Primary references

1. J. B. Cosgrave and K. Dilcher, *On a congruence of Emma Lehmer related
   to Euler numbers*, Acta Arith. 161 (2013), 47--67,
   <https://www.impan.pl/shop/publication/transaction/download/product/82378>.
   Equations (2.1)--(2.3) contain the mod-$p$, prime-power, and power-sum
   congruences used here.

2. R. Meštrović, *A search for primes $p$ such that Euler number
   $E_{p-3}$ is divisible by $p$*, Math. Comp. 83 (2014), 2967--2976,
   <https://arxiv.org/abs/1212.3602>.  This is cited only for context on the
   endpoint seeds; the all-parameter reduction above does not rely on a
   finite search.
