> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 208 — the first off-ray rank-one common-content prime

Date: 2026-08-30

## 1. Scope and verdict

This item tests the classification suggested by Item 205:



$$
p>3s+2,\qquad p\mid\gcd(g_0(s),g_1(s))
 \stackrel{?}{\Longrightarrow}
 p=5s+4,\qquad s\equiv3\pmod4.                      \tag{1.1}
$$



The classification is false.

**PROVED — exact counterexample.**  The first off-ray pair in the frozen
scan is



$$
\boxed{s=299,qquad k=899,qquad p=2399=8s+7.}        \tag{1.2}
$$



Both actual resonant integers vanish modulo this prime:



$$
g_0(299)\equiv g_1(299)\equiv0\pmod {2399}. \tag{1.3}
$$



The structural prime $1499=5s+4$ is present at the same $s$.  After every
prime-power factor supported on primes at most $k=899$ is removed from the
exact integer gcd, the residual is



$$
3{,}596{,}101=1499\cdot2399.             \tag{1.4}
$$



No factorization of the large gcd is used to obtain (1.4).

**PROVED — universal Frobenius-phase reduction.**  For every odd prime
$p>k$, put



$$
q=\begin{cases}1,&p\ge5s+4,\\2,&p<5s+4,\end{cases}
 \qquad b=qp-5s-4.                                    \tag{1.5}
$$



Then $b\ge0$, and the common-content question is exactly a pair of
coefficients of one finite polynomial; see (4.5).  The old ray $p=5s+4$
is the support-gap phase $b=0$.  The new pair has



$$
q=1,qquad b=900=k+1,                                \tag{1.6}
$$



and is a genuine cancellation inside that finite polynomial, not a support
gap.

**PROVED — the old structural ray remains exact.**  If $p=5s+4$ is prime,
then $p$ divides both $g_0,g_1$ exactly when $s\equiv3\pmod4$.  This ray
still has total log-prime weight $O(\log m)$ on the $m$-th cell row.

**FINITE — exhaustive large-factor audit through $s=1500$.**  Exact
integer coefficient formulas and repeated gcd with $(3s+2)!$ remove the
complete small-prime support without factoring the remaining integer.
Through $s=1500$, (1.2) is the only off-structural pair.  There are 120
structural pairs in this range.

**FINITE — targeted modular recurrence through $s=5000$.**  On all 1,061
prime nodes of the tempting line $p=8s+7$ through $s=5000$, the exact
modular coefficient recurrence finds only (1.2).  Thus $p=8s+7$ is not
promoted to an all-$s$ ray.

**OPEN.**  No all-$s$ classification of the off-ray common-content primes
is proved.  In particular, no finite union of affine rays is established,
and no total moving-prime zero count follows.  Primitive contraction zeros,
the digit $A_1$, and the joint gate $A_0=A_1=B_0=0$ remain separate.  No
Route-1 exponent and no conclusion about $e+\pi$ is claimed.

## 2. Definitions and the common-content consequence

As in Item 196, put



$$
u=x(1-x),\qquad Q=(1+x)(1+x^2)=1+x+x^2+x^3,qquad k=3s+2, \tag{2.1}
$$





$$
g_0(s)=[x^k]\frac{Q^{2s+1}}{(1-x)^{k+1}},qquad
 g_1(s)=[x^k]\frac{Q^{2s}}{(1-x)^{k+1}}.              \tag{2.2}
$$



The normalized primitive $G_s=B_s/u^k$ satisfies



$$
uB_s'-ku'B_s=Q^{2s}(g_1Q-g_0),qquad
 \deg B_s=6s+2.                                       \tag{2.3}
$$



Write



$$
V_{s,1}(-1)=a_s,qquad V_{s,1}(i)=b_s+ic_s.          \tag{2.4}
$$



For



$$
\Lambda_s=2^{k-1}\operatorname {lcm}(1,\ldots,k),qquad
 (X_s,Y_s,Z_s)=\Lambda_s(a_s,b_s,c_s),                \tag{2.5}
$$



Item 205 proved the prime-power localized identity



$$
v_p\gcd(X_s,Y_s,Z_s)
 =\min\{v_p(g_0(s)),v_p(g_1(s))\}qquad(p>k).          \tag{2.6}
$$



For completeness, its converse follows directly from (2.3).  If all three
values vanish modulo $p^e$, then $Q\mid B_s$ over
$(\mathbb Z/p^e\mathbb Z)[x]$.  If $Q^r\mid B_s$ with $1\le r\le2s$,
monic cancellation in (2.3), followed by reduction modulo $Q$, gives



$$
ruQ'C\equiv0\pmod Q.
$$



Since $uQ'\equiv-4\pmod Q$ and $p>3s+2>2s$, this forces another factor
of $Q$.  Hence $Q^{2s+1}\mid B_s$.  But
$\deg Q^{2s+1}=6s+3>\deg B_s$, so $B_s=0$ modulo $p^e$, and (2.3) gives
$g_0=g_1=0$.  The forward implication uses only the denominators
$1,\ldots,k$, which are $p$-units.

Thus (1.3) forces the entire moving vector to vanish modulo $2399$.
Both first gates $A_0,B_0$ vanish for every admissible $j$ at this
$(s,p)$ pair.  This says nothing about $A_1$.

## 3. Exact coefficient recurrence and factor-free finite audit

Using $Q=(1-x^4)/(1-x)$, define



$$
F_s(x)=\frac{(1-x^4)^{2s}}{(1-x)^{5s+3}}
        =\sum_{n\ge0}A_n(s)x^n.                       \tag{3.1}
$$



Logarithmic differentiation gives



$$
\boxed{
 (n+1)A_{n+1}
 =(5s+3)(A_n+A_{n-1}+A_{n-2})+(n-3s)A_{n-3},}         \tag{3.2}
$$



where $A_n=0$ for $n<0$ and $A_0=1$.  The resonant integers are



$$
g_1=A_k,qquad g_0=A_k+A_{k-1}+A_{k-2}+A_{k-3}.      \tag{3.3}
$$



The checker also computes them independently from the terminating formula



$$
[x^k]\frac{Q^e}{(1-x)^{k+1}}
 =\sum_{0\le t\le k/4}(-1)^t
   {e\choose t}{e+2k-4t\choose k-4t},                \tag{3.4}
$$



using $e=2s+1$ and $e=2s$.

For the finite all-prime-divisor audit, put



$$
\delta_s=\gcd(g_0(s),g_1(s)).                        \tag{3.5}
$$



Starting with $\delta_s$, repeatedly replace it by



$$
\frac{\delta_s}{\gcd(\delta_s,(3s+2)!)}              \tag{3.6}
$$



until the gcd is one.  The prime support of $(3s+2)!$ is exactly the set of
primes at most $k$.  Therefore (3.6) removes every such prime to its full
valuation and leaves the complete prime-power part supported on $p>k$.
No factorization of $\delta_s$ or of the residual is required.

For $0\le s\le1500$, the residual is



$$
\begin{cases}
 5s+4,&s\equiv3\pmod4\text{ and }5s+4\text{ is prime},\\
 1499\cdot2399,&s=299,\\
 1,&\text{otherwise},
 \end{cases}                                          \tag{3.7}
$$



where the second line includes the structural factor $1499$.  Equation
(3.7) is an exact **FINITE** theorem only on the displayed interval.

## 4. Universal Frobenius phase

The two coefficient forms are



$$
g_0=[x^k](1-x^4)^{2s+1}(1-x)^{-5s-4},               \tag{4.1}
$$





$$
g_1=[x^k](1-x^4)^{2s}(1-x)^{-5s-3}.                 \tag{4.2}
$$



Because $p>3s+2$, one has $5s+4<2p$.  Thus $q$ in (1.5) is either one or
two, and $b\ge0$.  In characteristic $p$,



$$
(1-x)^{-5s-4}
 =(1-x)^b(1-x)^{-qp}
 \equiv(1-x)^b(1-x^p)^{-q}.                           \tag{4.3}
$$



Since $k<p$, the factor $(1-x^p)^{-q}$ contributes only its constant term
to $[x^k]$.  Therefore, modulo $p$,



$$
g_0\equiv[x^k](1-x^4)^{2s+1}(1-x)^b,                \tag{4.4}
$$





$$
g_1\equiv[x^k](1-x^4)^{2s}(1-x)^{b+1}.              \tag{4.5}
$$



Let



$$
P_{s,b}(x)=(1-x^4)^{2s}(1-x)^{b+1}
            =\sum_n c_nx^n.                           \tag{4.6}
$$



Since $(1-x^4)/(1-x)=Q$, equations (4.4)--(4.5) become



$$
\boxed{g_1\equiv c_k,qquad
 g_0\equiv c_k+c_{k-1}+c_{k-2}+c_{k-3}\pmod p.}      \tag{4.7}
$$



This is the promised all-prime Frobenius-phase reduction.  It is exact for
every $p>k$ and contains both the support-gap and cancellation mechanisms.

## 5. The structural phase $b=0$

Suppose $p=5s+4$ is prime.  Then $b=0$.  Primality makes $s$ odd.

If $s\equiv3\pmod4$, then $k\equiv3\pmod4$.  Equation (4.4) has support
only in degrees $0\pmod4$, and (4.5) has support only in degrees
$0,1\pmod4$.  Hence both coefficients vanish.

If $s\equiv1\pmod4$, then $k\equiv1\pmod4$.  The first coefficient still
vanishes, but the second is



$$
(-1)^{(k-1)/4+1}{2s\choose(k-1)/4},                  \tag{5.1}
$$



up to the displayed sign.  Its binomial parameters lie strictly between
zero and $p$, so it is nonzero modulo $p$.  Consequently



$$
p=5s+4\text{ prime}\qquad\Longrightarrow\qquad
 p\mid g_0,g_1\iff s\equiv3\pmod4.                   \tag{5.2}
$$



This is an all-$s$ theorem, not a scan.

## 6. The off-ray cancellation at $(299,2399)$

At (1.2), the Frobenius phase is



$$
q=1,qquad b=2399-(5\cdot299+4)=900=k+1.             \tag{6.1}
$$



Thus



$$
P_{299,900}(x)=(1-x^4)^{598}(1-x)^{901}.             \tag{6.2}
$$



The exact modular recurrence gives



$$
(c_{k-3},c_{k-2},c_{k-1},c_k)
 \equiv(7,-7,0,0)\pmod {2399}.                        \tag{6.3}
$$



Equation (4.7) now proves (1.3).  In contrast to $b=0$, all relevant
residue classes occur in (6.2); the zero comes from cancellation.

The relation $p=8s+7$ explains why $b=k+1$, but it does not make the zero
automatic.  The certificate scans every prime value of $8s+7$ through
$s=5000$ by (3.2) modulo $p$.  Among 1,061 prime nodes, only
$(s,p)=(299,2399)$ vanishes.  This is **FINITE** evidence that the affine
relation is a useful phase locator, not a proved second ray.

At the same $s$, the structural prime gives



$$
(c_{k-3},c_{k-2},c_{k-1},c_k)
 \equiv(468,-468,0,0)\pmod {1499}.                    \tag{6.4}
$$



Both (6.3) and (6.4) land on Item 205's one-dimensional terminal survivor.

## 7. Transfer-kernel obstruction

Let $T_n$ be the four-state transfer from (3.2).  Its determinant is



$$
\det T_n={3s-n\over n+1}.     \tag{7.1}
$$



It has one exact rank drop at $n=3s$.  For every prime $p>k$, common
terminal zeros imply



$$
(A_k,A_{k-1},A_{k-2},A_{k-3},A_{k-4})
 =t(0,0,-1,1,0).                                      \tag{7.2}
$$



The two values of $t$ in (6.3)--(6.4) are nonzero.  Thus the off-ray
counterexample is also an exact witness that the local determinant defect
is arithmetically occupied, not merely a formal kernel.  A naive product of
local determinants or two-output terminal resultant cannot classify the
actual initial-state orbit.  A global recurrence, a cancellation theorem
for (4.7), or another $p$-adic invariant would be required.

## 8. Row log-weight

The structural ray remains harmless.  If $p=5s+4$ and



$$
2m+1=(j+1)p-s,                \tag{8.1}
$$



then



$$
10m+1=(5j+4)p.                \tag{8.2}
$$



For fixed $m$, all distinct structural primes divide $10m+1$, so their
total log-prime weight is at most $\log(10m+1)=O(\log m)$.

More generally, on any fixed affine ray $p=as+b$, equation (8.1) gives



$$
2am+a-b=(a(j+1)-1)p.          \tag{8.3}
$$



A fixed finite union of affine rays would therefore have total weight
$O(\log m)$.  This is conditional because no such union is proved.

For the isolated counterexample, choosing $j=1$ gives



$$
(m,p,j,s)=(2249,2399,1,299),qquad
 16m+1=(8j+7)p=35985.                                 \tag{8.4}
$$



There are only 599 admissible odd values of $j$ for this fixed $(s,p)$,
so this single pair has finite support and zero asymptotic rate.  The
counterexample refutes the classification but does not by itself create
positive mass.  Unknown further off-ray pairs prevent a total rate bound.

## 9. Certificate, replay, and status

The self-contained standard-library checker

    work/item208_rankone_content_classification_certificate.py

performs the following exact tasks:

1. constructs $g_0,g_1$ from the terminating binomial formula;
2. independently reconstructs selected rows from the coefficient recurrence;
3. removes the complete small-prime support through repeated gcd with $k!$,
   without integer factorization;
4. proves the exact residual statement through $s=1500$;
5. verifies the Frobenius normal form in both $q$-regimes;
6. reproduces both terminal states at $s=299$;
7. scans the 1,061 prime nodes on $p=8s+7$ through $s=5000$ by exact modular
   recurrence;
8. checks the affine row identities and support counts.

Canonical and replay JSON files are required to be byte-identical.  The
portable work artifacts are

    work/item208_rankone_content_classification_report.md
    work/item208_rankone_content_classification_certificate.py
    work/item208_rankone_content_classification_certificate.json
    work/item208_rankone_content_classification_certificate_replay.json
    work/item208_rankone_content_classification_hashes.sha256

Status summary:

- **PROVED:** the proposed classification (1.1) is false.
- **PROVED:** the exact counterexample (1.2)--(1.4).
- **PROVED:** the universal Frobenius phase (4.7), the exact structural-ray
  theorem (5.2), and the affine-ray rate identity (8.3).
- **FINITE:** the complete large-factor audit through $s=1500$ and the
  targeted modular scan through $s=5000$.
- **OPEN:** an all-$s$ description or sublinear count of off-ray primes.
- **OPEN:** primitive first-gate contractions, $A_1$, their joint gate, any
  improved Route-1 exponent, and the arithmetic nature of $e+\pi$.
