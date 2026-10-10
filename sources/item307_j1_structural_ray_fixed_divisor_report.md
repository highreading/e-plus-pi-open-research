> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 307 — fixed Gaussian divisors for the pinned $j=1$ orbit on the three structural rays

Date: 2026-08-31

## 1. Exact outcome

Let



$$
p=4h+6s+3,\qquad s\in\{2,4,6\},\qquad h\geq1,\qquad3\nmid h,
 \qquad p\text{ prime}.                                      \tag{1.1}
$$



Retain Item 222's pinned eliminant $E_h^*$, Item 237's algebraic
coefficient $c_h^*$, and the proved Item 243 gauge
$c_h^*=\mathcal G_hE_h^*$.  Item 288 proves that
$\mathcal G_h$ is a $p$-unit on every actual row.

Put



$$
w_h=(-1)^{\lfloor h/2\rfloor}2^h.       \tag{1.2}
$$



This item proves the following exact residue table:



$$
\boxed{c_h^*\equiv\gamma_s(a_{s,\epsilon}+b_{s,\epsilon}w_h)\pmod p},
\qquad \epsilon=h\bmod2,                                   \tag{1.3}
$$



where



$$
\begin{array}{c|c|r|r|c}
s&\epsilon&a_{s,\epsilon}&b_{s,\epsilon}&\gamma_s\\ \hline
2&0&6517&-55363&2\\
2&1&6517&28357&2\\
4&0&-160741235&2209797565&1/4\\
4&1&-160741235&12326545165&1/4\\
6&0&6164597613027&4266522023635179&1/64\\
6&1&6164597613027&492022610178771&1/64.
\end{array}                                                 \tag{1.4}
$$



Every $\gamma_s$ is a $p$-unit.  Hence (1.3), the all-$h$ gauge,
and Item 288's unit audit give



$$
E_h^*\equiv0\pmod p
 \quad\Longleftrightarrow\quad
 a_{s,\epsilon}+b_{s,\epsilon}w_h\equiv0\pmod p.           \tag{1.5}
$$



Euler's criterion then puts every collision prime into one fixed nonzero
integer.  Define



$$
\delta_{s,\epsilon}=(-1)^{\epsilon+s/2+1},\qquad
 D_{s,\epsilon}=2^{3s+1}a_{s,\epsilon}^2
                    -\delta_{s,\epsilon}b_{s,\epsilon}^2.  \tag{1.6}
$$



The six exact values are



$$
\begin{array}{c|c|r}
s&\epsilon&D_{s,\epsilon}\\ \hline
2&0&2371263223\\
2&1&6240444441\\
4&0&216546009281712172425\\
4&1&59719088298647365975\\
6&0&1720920668592381569095693219911\\
6&1&20166217095683535330649958652393.
\end{array}                                                 \tag{1.7}
$$



All six integers are positive.  The exact necessary-divisor theorem is



$$
\boxed{E_h^*\equiv0\pmod p\quad\Longrightarrow\quad
        p\mid D_{s,h\bmod2}.}                               \tag{1.8}
$$



Consequently, if $\mathcal W_{\rm str}(H)$ denotes the logarithmic
mass of pinned collisions on the three structural rays with $h\leq H$,
counted with their ray multiplicity, then



$$
\boxed{
 \mathcal W_{\rm str}(H)
 \leq\sum_{s\in\{2,4,6\}}\sum_{\epsilon=0}^1
          \log\operatorname {rad}|D_{s,\epsilon}|
 \leq\log\prod_{s,\epsilon}|D_{s,\epsilon}|=O(1)=o(H).}   \tag{1.9}
$$



This is a weighted zero-density theorem for the actual pinned orbit, not
a theorem about unrestricted recurrence states.  It does not require or
claim universal nonvanishing.  In fact the preselected exact control
$(h,s,p)=(8,2,47)$ has $E_8^*\equiv0\pmod {47}$, so universal
nonvanishing on the structural union is false.  This single symbolic
control is immediate from (1.3):


$$
w_8=256\equiv21,\qquad
6517-55363w_8\equiv31-44\cdot21\equiv0\pmod {47}.           \tag{1.9a}
$$


It is not a scan inference.  No factorization of the six containers and
no actual-prime scan enters the proof.

### The actual ordinary gate and the $p$-unit gauge

Let $\sigma$ denote Item 222's ordinary row parameter and put
$\sigma_*=-(4h+3)/6$.  On an actual structural row $\sigma=s$,



$$
6(s-\sigma_*)=4h+6s+3=p.            \tag{1.10}
$$



Item 222 proves that every denominator in its ordinary eliminant is a
$p$-unit and that an ordinary fixed-$j=1$ collision forces
$E_h(s)\equiv0\pmod p$.  Equation (1.10) therefore gives



$$
E_h(s)\equiv E_h(\sigma_*)=E_h^*\pmod p. \tag{1.11}
$$



This is a necessary gate for the original collision; no converse from
$E_h^*=0$ to the full original collision is used or claimed.

The proved Item 243 gauge is fixed by



$$
\mathcal G_1=-\frac{49}{18},\qquad
\mathcal G_2=\frac{4235}{1944},\qquad
\frac{\mathcal G_{a+3}}{\mathcal G_a}=
\frac{a(4a+1)(4a+5)(4a+7)(4a+9)(4a+11)(4a+15)^2}
{864(a+1)(a+2)(2a+1)^2(2a+3)(2a+5)^2(4a+3)}.              \tag{1.12}
$$



For every step $a\leq h-3$, all nonzero linear factors in (1.12) are
at most $4h+3$; the largest is $4a+15\leq4h+3$.  The two bases and
the constant $864$ have prime support at most $11$.  Every structural
ray prime satisfies



$$
p=4h+6s+3\geq4h+15>4h+3.           \tag{1.13}
$$



Thus neither the reduced numerator nor denominator of $\mathcal G_h$
is divisible by $p$, and



$$
\boxed{\mathcal G_h\in\mathbb F_p^\times,\qquad
        E_h^*\equiv0\pmod p\iff c_h^*\equiv0\pmod p.}       \tag{1.14}
$$



Equations (1.10)--(1.14) explicitly connect the rational-coefficient
calculation below to the actual pinned ordinary collision gate.

## 2. Frobenius removes the moving algebraic exponent

Item 237 proves, with



$$
Q(y)=1+y+y^2/2,\quad
 A(y)=(20+14y+4y^2)/3,\quad B(y)=2-5y-3y^2,
$$



that



$$
c_h^*=[y^{2h}](1+y)^{-2h-1}Q(y)^{(4h+3)/3}
                         (hA(y)+B(y)).                       \tag{2.1}
$$



On (1.1), $(4h+3)/3=p/3-2s$.  In
$\mathbb F_p[[y]]$, let $R(y)=Q(y)^{1/3}$ be the unique branch with
constant term one.  Since $p>3$, this branch is defined, and Frobenius
gives



$$
Q(y)^{p/3}=R(y)^p=R(y^p).                                  \tag{2.2}
$$



Because $2h<p$, the factor $R(y^p)$ contributes only its constant
term to the target coefficient.  Thus



$$
c_h^*\equiv[y^{2h}](1+y)^{-2h-1}Q(y)^{-2s}
                         (hA(y)+B(y))\pmod p.                \tag{2.3}
$$



This is the first sequence-specific step.  The algebraic series has become
a fixed rational kernel on each structural ray.

## 3. A fixed rational coefficient source

Put $n=2h$, $t=y/(1+y)$, and



$$
D(t)=t^2-2t+2,\qquad
 R_1(t)=\frac{10-13t+5t^2}{3},qquad
 R_0(t)=2-9t+4t^2.                                         \tag{3.1}
$$



Residue substitution $y=t/(1-t)$ in (2.3) gives



$$
c_h^*\equiv2^{2s}[t^n]
 \frac{(1-t)^{2n+4s-2}(nR_1(t)+R_0(t))}{D(t)^{2s}}\pmod p. \tag{3.2}
$$



Since $2n+4s-2=p-2s-5$, Frobenius gives, below degree $p$,



$$
(1-t)^{p-2s-5}\equiv(1-t)^{-2s-5}.                       \tag{3.3}
$$



The coefficient identity
$n[t^n]F=[t^n]tF'$ now removes the last moving parameter.  Define



$$
G_s(t)=t\frac d{dt}\left(
     \frac{R_1(t)}{(1-t)^{2s+5}D(t)^{2s}}\right)
 +\frac{R_0(t)}{(1-t)^{2s+5}D(t)^{2s}}.                    \tag{3.4}
$$



Then



$$
c_h^*\equiv2^{2s}[t^{2h}]G_s(t)\pmod p. \tag{3.5}
$$



Exact simplification gives the compact all-$s$ rational function



$$
G_s(t)=\frac{N_s(t)}{(1-t)^{2s+6}D(t)^{2s+1}},             \tag{3.6}
$$



where



$$
\begin{aligned}
3N_s(t)={}&12+(80s-4)t-(224s+8)t^2+(256s+16)t^3\\
          &-(138s+9)t^4+(30s+3)t^5.                        \tag{3.7}
\end{aligned}
$$



Thus every ray is governed by one fixed rational generating function.

## 4. Exact Gaussian partial fractions

Let



$$
\lambda=(1+i)/2,qquad D(t)=2(1-\lambda t)(1-\bar\lambda t). \tag{4.1}
$$



The unique partial fraction decomposition of (3.6) has the form



$$
G_s(t)=\sum_{k=1}^{2s+6}\frac{A_{s,k}}{(1-t)^k}
 +\sum_{k=1}^{2s+1}\left(
   \frac{B_{s,k}}{(1-\lambda t)^k}
  +\frac{\bar B_{s,k}}{(1-\bar\lambda t)^k}\right),        \tag{4.2}
$$



with $A_{s,k}\in\mathbb Q$, $B_{s,k}\in\mathbb Q(i)$.  Hence



$$
[t^n]G_s(t)=\mathcal A_s(n)
       +2\operatorname {Re}(\mathcal B_s(n)\lambda^n),      \tag{4.3}
$$



where



$$
\mathcal A_s(n)=\sum_kA_{s,k}{n+k-1\choose k-1},\qquad
\mathcal B_s(n)=\sum_kB_{s,k}{n+k-1\choose k-1}.            \tag{4.4}
$$



Modulo $p$, $n=2h\equiv n_s:=-(6s+3)/2$.  Every factorial
denominator in the binomial polynomials (4.4) is a $p$-unit: their
orders are at most $2s+5$, while an actual ray prime is at least
$19,31,43$ for $s=2,4,6$, respectively.  Exact rational partial
fractions give



$$
\begin{array}{c|r|r|r}
s&\mathcal A_s(n_s)&\operatorname {Re}\mathcal B_s(n_s)
 &\operatorname {Im}\mathcal B_s(n_s)\\ \hline
2&6517/8&-55363/2048&28357/2048\\
4&-160741235/1024&-2209797565/16777216&-12326545165/16777216\\
6&6164597613027/262144&4266522023635179/274877906944
 &492022610178771/274877906944.
\end{array}                                                 \tag{4.5}
$$



The deterministic checker constructs all coefficients in (4.2) with
exact rational arithmetic.  The number of unknown rational coordinates is
$(2s+6)+2(2s+1)=6s+8$, exactly the degree of the denominator in
(3.6).  It matches that many Taylor coefficients, so after multiplication
by the common denominator the difference is a polynomial of degree below
$6s+8$ with $6s+8$ initial zero coefficients; it is identically zero.
This is an exact rational-function certificate, not interpolation of the
target sequence.

## 5. Specialization of the Gaussian power

Since $n=2h$,



$$
\lambda^n=(i/2)^h.                  \tag{5.1}
$$



Also



$$
2^{2h}=2^{(p-1)/2}2^{-(3s+1)}
 \equiv\delta_{s,\epsilon}2^{-(3s+1)}\pmod p,              \tag{5.2}
$$



because Euler's criterion and $p\bmod8$ give
$(2/p)=\delta_{s,\epsilon}$.  Therefore



$$
\begin{array}{c|cc|cc}
 &\multicolumn{2}{c|}{h\ {\rm even}}&
  \multicolumn{2}{c}{h\ {\rm odd}}\\
s&p\bmod8&\delta_{s,0}&p\bmod8&\delta_{s,1}\\ \hline
2&7& 1&3&-1\\
4&3&-1&7& 1\\
6&7& 1&3&-1.
\end{array}                                                \tag{5.2a}
$$





$$
\lambda^{2h}\equiv
\begin{cases}
 \delta_{s,0}2^{3s+1}w_h,&h\text{ even},\\
 i\delta_{s,1}2^{3s+1}w_h,&h\text{ odd}.
\end{cases}                                                \tag{5.3}
$$



Substitution of (4.5) into (4.3), followed by (3.5), is exactly the table
(1.3)--(1.4).

Finally, (5.2) says



$$
2^{3s+1}w_h^2\equiv\delta_{s,\epsilon}\pmod p. \tag{5.4}
$$



If the linear form in (1.5) vanishes, squaring and using (5.4) proves
$p\mid D_{s,\epsilon}$.  The checker evaluates (1.6) exactly and obtains
the six nonzero integers (1.7), completing (1.8)--(1.9).

## 6. Capacity consequence and strict scope

Along the varying-$h$ sequence, Item 297's structural-ray union has
Chebyshev mass asymptotic to $2H$, and (1.9) closes its pinned
arithmetic to $O(1)$.  This is not the master-capacity normalization.
The Route-1 ledger is fixed-$M$, where Item 264 gives



$$
M=3h+4s+2,\qquad
 \mathcal S_M=\{s\geq1:4s\leq M-5,\ s\equiv M+1\pmod3\}.    \tag{6.1}
$$



At fixed $M$, each of $s=2,4,6$ supplies at most one candidate, so
their complete raw logarithmic support is at most



$$
3\log((3M-1)/2)=O(\log M)=o(M).           \tag{6.2}
$$



Thus the structural rays were already a zero-rate fixed-width boundary in
Item 264.  The exact master-ledger consequence of this item is



$$
\boxed{\text{new linear log rate}=0,\qquad
       \text{new fixed-\(j=1\) capacity reduction}=0.}      \tag{6.3}
$$



The conditional fixed-$j=1$ ceiling remains $1/36$ per $6M$.
Equation (1.9) is an exact structural-ray arithmetic closure, not a
strategic capacity closer.

The three rays exhaust the infinite **coefficient-singular rays** of the
Item 293 recurrence, but they do not exhaust the fixed-$j=1$ cell:
ordinary rows exist for every $s\geq1$.  Ray multiplicity is retained
in (1.9), including the shifted-diagonal overlaps recorded by Item 297.

For $s\in\mathcal S_M$, put



$$
p_s=\frac{4M+2s+1}{3},\qquad
 h_s=\frac{M-4s-2}{3}.                                    \tag{6.4}
$$



With $N_E(h)$ the reduced numerator of $E_h^*$, the smallest remaining
sequence-specific fixed-$j=1$ weighted lemma in the correct normalization
is



$$
\boxed{
\mathcal W_{\rm off}(M):=
\sum_{\substack{s\in\mathcal S_M\setminus\{2,4,6\}\\
                 p_s\ {\rm prime}\\
                 p_s\mid N_E(h_s)}}\log p_s=o(M).}          \tag{6.5}
$$



The off-ray set in (6.5), with $s$ varying through an interval of length
$\asymp M$, is the actual $1/36$ reservoir.  Equation (6.5) would give
the full Item 293 fixed-$j=1$ weighted target.  There is no unresolved
structural-ray arithmetic lemma left, but closing that thin boundary does
not change master capacity.

No canonical ledger is edited by this research package.  In particular:

- it does **not** prove universal nonvanishing on any ray;
- it does **not** factor the six fixed containers or classify their actual
  prime zeros;
- it does **not** address $s\notin\{2,4,6\}$, isolated off-ray fixed-
  $j=1$ mass, the fixed-$j=2$ cell, or the remaining moving cells;
- it does **not** prove Route 1 or any conclusion about $e+\pi$.

The theorem is precisely weighted zero density on the three structural
rays, with no inference from a prime scan.

## 7. Deterministic replay

From the archive root, run

~~~text
python scripts/item307_j1_structural_ray_fixed_divisor_certificate.py --output results/item307_j1_structural_ray_fixed_divisor_certificate_replay.json
~~~

The checker uses only standard-library exact integer, `Fraction`, and
Gaussian-rational arithmetic.  It pins Items 222, 229, 237, 243, 264, and 288;
constructs (3.6)--(3.7); solves and certifies the exact partial fractions;
recomputes (4.5), (1.4), and (1.7); and replays a fixed list of small
control rows.  It performs no actual-prime scan and no factorization of
the fixed containers.

- **PROVED:** (1.3)--(1.9), including $\mathcal W_{\rm str}(H)=O(1)$.
- **OPEN:** off-ray weighted density, the full fixed-$j=1$ closer, Route 1,
  and every conclusion about $e+\pi$.
- **NOT CLAIMED:** universal ray nonvanishing, a complete zero list, or a
  positive master-capacity reduction from this thin support.


