> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 171 — higher prime-power loci $10m+1=p^a$

Date: 2026-08-29

## 1. Scope and verdict

Put



$$
u=x(1-x),\qquad Q=(1+x)(1+x^2),\qquad
 \omega_s={u^{6m}\over Q^{4m+1+s}}\,dx\quad(s=0,1),
$$



and retain the frozen primitive content $c_m=\gcd(U_m,V_m)$.  This
item treats



$$
10m+1=p^a,\qquad a\ge3,              \tag{1.1}
$$



for an odd prime $p\ne5$.  Write $q=p^{a-1}$.  Then $q$ is exactly
the top denominator prime power:



$$
q\le4m+1={2p^a+3\over5}<p^a.              \tag{1.2}
$$



The conclusions are as follows.

**PROVED — universal sparse top-Cartier normal form.**  After $a-1$
Cartier iterations, both rows are controlled by



$$
P_0=x^\rho(1-x^4)^\rho,\qquad
 P_1=x^\rho(1-x)(1-x^4)^{\rho-1}.                       \tag{1.3}
$$



The exact value of $\rho$, and the exact rank of the two selected
coefficient rows, are classified in Sections 2--3.  The rank depends on
$p\bmod20$, with one small exception $(p,a)=(3,4)$; it is not a
universal rank-zero phenomenon.

**PROVED — an all-prime radical law on the locus.**  Every admissible
pair in (1.1) satisfies



$$
\boxed{p\mid c_m}.               \tag{1.4}
$$



Most residue classes follow directly from rank at most one in (1.3).
The only rank-two class is $p\equiv1\pmod {20}$.  There the relevant
rational/logarithmic endpoint minor still vanishes: a relative exactness
lemma reduces it to



$$
\sum_{r=0}^{(p-3)/2}{1\over4r+3}=0\pmod p. \tag{1.5}
$$



The terms in (1.5) cancel under a fixed-point-free involution.

**PROVED — sharp first-layer valuation ledger.**  The top rank and the
already removed first-Cartier factor give the unconditional lower bounds



$$
\begin{array}{c|c|c|c}
p\bmod20&\text{allowed }a&\text{top rank}&\text{proved }v_p(c_m)\ge\\ \hline
1&\text{all }a&2&1\\
11&\text{all }a&1&1\\
3, p>3&4\mid a&0&1\\
13&4\mid a&0&1\\
7,17&4\mid a&0&2\\
9&2\mid a&1&1\\
19&2\mid a&0&2.
\end{array}                                               \tag{1.6}
$$



For $p=3$, the rank is one at $a=4$, giving the lower bound one;
for every allowed $a\ge8$ it is zero, giving the lower bound two.

**PROVED — zero weighted mass.**  At a fixed $m$, (1.1) determines at
most one base prime.  Hence its radical contribution is



$$
\log p={1\over a}\log(10m+1)\le {1\over3}\log(10m+1)=o(m). \tag{1.7}
$$



Even all $a-1$ top-exponent copies have weight at most
$(a-1)\log p<\log(10m+1)=o(m)$.  Thus every divisor obtained solely
from this top-exponent mechanism has zero Route-1 exponential mass.

**DISPROVED — naive exact valuation law.**  The claim
$v_p(c_m)=a+1$ on all higher-power loci is false.  Exact modular rows
include



$$
(p,a,m,v_p(c_m))=(11,3,133,1),(3,4,8,3),(7,4,240,5).   \tag{1.8}
$$



The $p=7$ row happens to equal $a+1$; no all-prime theorem for its
residue class follows.

**EXPERIMENTAL FINITE.**  Section 6 records exact modular valuations for
eight rows, including $p=17,a=4$ and two further $a=3$ primes.  These
rows distinguish deeper lift behavior from the proved top-rank table.

**OPEN.**  There is no all-prime formula for the exact valuation beyond
(1.6), no positive-mass higher layer, no improved Route-1 constant, and
no conclusion about $e+\pi$.

## 2. Exact floor decomposition

Let



$$
M=p^a,\quad N=6m={3(M-1)\over5},\quad
 K=4m+1={2M+3\over5},\quad q=p^{a-1}.                   \tag{2.1}
$$



Write



$$
N=Aq+\rho,\qquad K=Bq+\tau,qquad0\le\rho,\tau<q,
 \qquad\kappa=2A-3B.                                    \tag{2.2}
$$



Direct Euclidean division gives the complete table



$$
\begin{array}{c|c|c|c|c|c}
p\bmod5&A&B&\kappa&\rho&\tau\\ \hline
1&(3p-3)/5&(2p-2)/5&0&3(q-1)/5&(2q+3)/5\\
2&(3p-1)/5&(2p-4)/5&2&(q-3)/5&(4q+3)/5\\
3&(3p-4)/5&(2p-1)/5&-1&(4q-3)/5&(q+3)/5\\
4&(3p-2)/5&(2p-3)/5&1&(2q-3)/5&(3q+3)/5.
\end{array}                                               \tag{2.3}
$$



In every row



$$
q-\tau=\rho.                 \tag{2.4}
$$



In characteristic $p$, put



$$
F={u^A\over Q^{B+1}}.
$$



Equations (2.2)--(2.4) give, without approximation,



$$
\omega_0=F^qP_0\,dx,\qquad\omega_1=F^qP_1\,dx,        \tag{2.5}
$$



with $P_0,P_1$ exactly as in (1.3).  Thus



$$
\mathcal C^{a-1}(\omega_s)
 =F\sum_{j\ge1}[x^{jq-1}]P_s\,x^{j-1}\,dx.             \tag{2.6}
$$



This is the promised frozen-normalization formula.  Notice that
$10m+1=p^a$ does not mean that the top layer is $p^a$; it is
$p^{a-1}$.

The first-Cartier squarefree normalization is also explicit.  If



$$
\epsilon={\bf1}_{p\in\mathcal P_m},                    \tag{2.7}
$$



then



$$
\boxed{\epsilon=1\iff p\equiv3\pmod5\text{ and }p>3.} \tag{2.8}
$$



Indeed, direct substitution in the two first-Cartier degrees gives
$d_p(N,K)=p-3,\ d_p(N,K+1)=p-6$ in that class; the other three
classes lie above the rank-zero cutoff.  The value $p=3$ is the sole
rollover exception.

## 3. Exact top-Cartier rank

The two coefficient formulas following from (1.3) are



$$
[x^{\rho+4j}]P_0=(-1)^j{\rho\choose j},                \tag{3.1}
$$





$$
[x^{\rho+4j}]P_1=(-1)^j{\rho-1\choose j},\qquad
 [x^{\rho+1+4j}]P_1=-(-1)^j{\rho-1\choose j}.          \tag{3.2}
$$



All other coefficients vanish.  Applying Lucas' theorem to the selected
indices $q-1,2q-1,3q-1$ gives



$$
\begin{array}{c|c|c|c}
p\bmod20&q\bmod20&
([x^{jq-1}]P_0)_j&([x^{jq-1}]P_1)_j\\ \hline
1&1&(*,0)&(*,*)\\
11&1\text{ or }11&(*,0)&(*,0)\\
3&7&(0,0,0)&(0,0,0)\\
13&17&(0,0,0)&(0,0,0)\\
7&3&()&()\\
17&13&()&()\\
9&9&(0)&(*)\\
19&19&(0)&(0).
\end{array}                                               \tag{3.3}
$$



Here every star is nonzero and an empty tuple means that
$\deg P_s<q-1$.  The entry in the $p\equiv3$ row has the single
exception



$$
(p,a)=(3,4):\qquad (P_0)_\mathrm{sel}=(0,0,0),\quad
 (P_1)_\mathrm{sel}=(2,0,0).                            \tag{3.4}
$$



Here is the all-exponent Lucas proof, made explicit.  Lucas says that
${N\choose J}\ne0\pmod p$ exactly when every base-$p$ digit of $J$
is at most the corresponding digit of $N$.  If $5s+c=p^e$, compute
the digits from low to high by



$$
c_0=c,\qquad 5s_j+c_j=c_{j+1}p,\qquad
 0\le s_j<p,\quad1\le c_{j+1}\le4.                       \tag{3.5}
$$



For $p=20h+r$, this is a literal four-state carry automaton.  The only
non-structural comparisons needed in (3.3) reduce to the following
table; an inequality in the last column is a Lucas-zero witness at the
displayed digit.



$$
\begin{array}{c|c|c|c}
p\bmod20&\text{coefficient}&(N,J)&\text{digit check}\\ \hline
1&P_0[q-1]&(\rho,(q-1)/10)&2h\le12h\\
1&P_1[q-1]&(\rho-1,(q-1)/10)&2h\le12h-1\\
1&P_1[2q-1]&(\rho-1,7(q-1)/20)&7h\le12h-1\\
11&P_0[q-1],P_1[q-1]&(\rho\text{ or }\rho-1,(q-1)/10)
 &(2h+1)\le12h+5\\
11,\ e\text{ even}&P_1[2q-1]&(\rho-1,7(q-1)/20)
 &(17h+9)>(12h+5)\quad(j=0)\\
3,\ p>3&P_0[2q-1]&(\rho,(2q-1-\rho)/4)
 &(14h+2)>4h\quad(j=0)\\
3,\ p>3&P_1[q-1]&(\rho-1,(q-2-\rho)/4)
 &(9h+1)>(4h-1)\quad(j=0)\\
3,\ p>3&P_1[2q-1]&(\rho-1,(2q-1-\rho)/4)
 &(14h+2)>(4h-1)\quad(j=0)\\
13&P_0[2q-1]&(\rho,(2q-1-\rho)/4)
 &(14h+9)>(4h+2)\quad(j=0)\\
13&P_1[2q-1]&(\rho-1,(2q-1-\rho)/4)
 &(14h+9)>(4h+1)\quad(j=0)\\
13&P_1[3q-1]&(\rho-1,(3q-2-\rho)/4)
 &(19h+12)>(4h+1)\quad(j=0).
\end{array}                                               \tag{3.6}
$$



For the nonzero $p\equiv9\pmod {20}$ entry, write
$p=20h+9$ and $q=5s+4$.  The base-$p$ digits of the upper index
$2s=\rho-1$ are



$$
8h+2,\ 12h+5,\ 8h+3,\ 12h+5,\ldots ,
$$



whereas those of the lower index $(3s+1)/4$ are



$$
3h+1,\ 7h+3,\ 3h+1,\ 7h+3,\ldots .                    \tag{3.7}
$$



They are digitwise dominated.  In the $p\equiv11$ row, the second
coefficient is structurally absent when $e$ is odd; when $e$ is
even, the fifth row of (3.6) kills it.  For $p=3,e=3$, direct Lucas
digits give the exceptional coefficient $2$ in (3.4); for every
allowed $e\ge7$, the repeated carry block has upper/lower digit
$0<1$ at position four.  Degree and residue-section incompatibility
supplies every remaining zero in (3.3).  Thus (3.5)--(3.7), not a finite
prime scan, prove the table for all admissible exponents.

The deterministic certificate independently reconstructs the same table
for 479 admissible $(p,a)$ rows with $p\le500,\ a\le12$.

Taking the row rank in (3.3) proves the rank column of (1.6).

## 4. The rank-two relative endpoint lemma

Only $p\equiv1\pmod {20}$ has rank two.  Put



$$
h={p-1\over20},\qquad n=12h,\qquad K=8h+1,qquad n+K=p, \tag{4.1}
$$



and



$$
G={u^n\over Q^K}\,dx,\qquad X=xG.                     \tag{4.2}
$$



Since $u^nQ^n=\mathfrak D^n$, where
$\mathfrak D=uQ=x(1-x^4)$, coefficient selection gives



$$
\mathcal C(G)=\gamma{dx\over Q},\qquad
 \mathcal C(X)=\delta{x\,dx\over Q},                  \tag{4.3}
$$



with



$$
\gamma={n\choose2h}\ne0,\qquad
 \delta=(-1)^{7h}{n\choose7h}\ne0\pmod p.             \tag{4.4}
$$



Because $p\equiv1\pmod4$,



$$
\mathcal C\left({dx\over1+x^2}\right)={dx\over1+x^2}.
$$



Hence



$$
W=\delta G+\gamma X-\gamma\delta{dx\over1+x^2}       \tag{4.5}
$$



is exact.  As in item 167, absolute exactness alone is not enough; the
endpoint must be controlled.

Raise (4.5) to denominator $Q^p$.  Its numerator is



$$
P_*=(\delta+\gamma x)\mathfrak D^n
 -\gamma\delta(1+x)^p(1+x^2)^{p-1}.                    \tag{4.6}
$$



The two Cartier resonances vanish.  Its zero-constant primitive $T$
can therefore be compared with the unique proper Hermite primitive
$A/Q^{K-1}$:



$$
T=AQ^{n+1}+J^p,\qquad\deg J\le2.   \tag{4.7}
$$



Frobenius fixes all three roots of $Q$, so $J$ is the quadratic
interpolant of $T$ there.  If $S_r$ is the sum of the coefficients
of $T$ in exponent class $r\pmod4$, polynomial reduction modulo
$Q$ gives



$$
J(0)=S_0-S_3,\qquad T(1)-J(1)=4S_3.                   \tag{4.8}
$$



The first summand of (4.6), after integration, occupies only sections
one and two.  The second summand gives



$$
S_0=S_3=\gamma\delta
 \sum_{r=0}^{(p-3)/2}{1\over4r+3}.                     \tag{4.9}
$$



The involution



$$
r\longmapsto {p-3\over2}-r                            \tag{4.10}
$$



pairs each denominator with its negative modulo $p$.  It has no fixed
point because $p-3\not\equiv0\pmod4$.  Thus (4.9) is zero.  Equations
(4.7)--(4.8) give $A(0)=A(1)=0$, and therefore



$$
R(W)=0,\qquad
 \delta R(G)+\gamma R(X)=0.                            \tag{4.11}
$$



In the rank-two row, one transformed form is a nonzero multiple of $G$
and the other has a nonzero $X$-component.  Equation (4.11) says exactly
that their rational/logarithmic minor vanishes.  By the top relative
Cartier identity,



$$
qA_m\equiv0\pmod p.             \tag{4.12}
$$



This closes the only class not settled by proportional top images.

## 5. Primitive valuation ledger and proof of the radical law

Retain the frozen minors



$$
\mathscr A=qA_m=L_1(qR_0)-L_0(qR_1),\qquad
 \mathscr B=8B_m=L_1E_0-L_0E_1.                        \tag{5.1}
$$



The exact primitive normalization gives



$$
v_p(U_m)=v_p(\mathscr A)-\epsilon,\qquad
 v_p(V_m)=(a-1)+v_p(\mathscr B)-\epsilon.               \tag{5.2}
$$



If the top rank is zero, both transformed endpoint vectors vanish modulo
$p$, so



$$
v_p(\mathscr A),v_p(\mathscr B)\ge2.                  \tag{5.3}
$$



If the top rank is one, their two minors are divisible by $p$.  In the
rank-two class, (4.12) supplies the required $A$-minor copy, while
$v_p(V_m)\ge a-1\ge2$ follows directly from (5.2).  Finally (2.8)
shows that the only squarefree normalization loss occurs in a rank-zero
class.  Substitution in (5.2) proves every entry of (1.6), hence (1.4).

This ledger is deliberately a lower-bound theorem.  Rank zero modulo
$p$ does not determine the next Witt/Hasse digit, so (5.3) must not be
iterated without new lifted information.

## 6. Exact finite valuation diagnostics

The deterministic evaluator computes $L_s,qR_s,E_s$ modulo $p^9$
from the integral local Hasse recurrence, forms both minors in (5.1), and
then applies (5.2).  The current rows are



$$
\begin{array}{c|c|r|c|c|c|c}
p&a&m&\epsilon&v_p(qA_m)&v_p(8B_m)&v_p(c_m)\\ \hline
3&4&8&0&3&2&3\\
7&4&240&0&5&3&5\\
11&3&133&0&1&3&1\\
13&4&2856&1&4&3&3\\
17&4&8352&0&4&3&4\\
11&4&1464&0&4&2&4\\
31&3&2979&0&1&2&1\\
41&3&6892&0&1&0&1.
\end{array}                                               \tag{6.1}
$$



For example, the $p=7$ and $p=17$ rows have the same exponent and
the same top rank zero, but their actual content valuations are five and
four.  This is a concrete warning that the characteristic-$p$ rank
table does not determine the deeper valuation.  Likewise, the two
$p\equiv11\pmod {20}$, $a=3$ rows both stop at valuation one, while
the $p=11,a=4$ row reaches valuation four.

All values in (6.1) are exact because they are strictly below the working
precision nine.  They are finite diagnostics, not density statements.

## 7. Zero-mass theorem and research consequence

Equality (1.1) is much thinner than merely requiring $p\mid10m+1$.
The integer $10m+1$, if it is a prime power, has a unique base prime.
Thus (1.7) proves zero radical mass without any distribution theorem.
More generally, for each fixed constant $C$, any divisor law of the form



$$
p^{Ca+O(1)}\mid c_m             \tag{7.1}
$$



on this locus contributes only $O(\log m)$.  A putative exact law such
as $v_p(c_m)=a+1$, even if it had been true, could not improve the
Route-1 exponential constant.

No bound of the form $v_p(c_m)=O(a)$ for the *actual unforced excess*
is claimed here.  Therefore the zero-mass statement applies to the proved
radical/top-exponent mechanisms, not to an unknown arbitrarily large
valuation.

## 8. Deterministic certificate

From the archive root, the intended replay is

    python scripts/item171_prime_power_loci_certificate.py --prime-bound 500 --max-exponent 12 --precision 9 --actual-mode full --output results/item171_prime_power_loci_certificate.json

In the staging workspace, replace `scripts` and `results` by `work`.
The checker:

1. reconstructs (2.3)--(2.6) for every admissible row;
2. evaluates every selected coefficient through Lucas' theorem and checks
   the exact rank table (3.3);
3. checks the first-Cartier normalization (2.8);
4. checks the reciprocal cancellation (4.9) for every sampled
   $p\equiv1\pmod {20}$; and
5. independently recomputes all eight finite valuations in (6.1).

The companion SHA-256 manifest pins the report, checker, both JSON
outputs, and both archived Hasse dependencies.

## 9. Status ledger

### PROVED

- The universal sparse polynomials (1.3).
- The all-exponent rank table (3.3), including the sole small exception.
- The rank-two relative endpoint lemma (4.11).
- The radical divisor $p\mid c_m$ and the lower bounds (1.6).
- Zero radical and top-exponent weighted mass.

### DISPROVED

- The universal exact law $v_p(c_m)=a+1$.
- Any inference of exact deeper valuation from top Cartier rank alone.

### EXPERIMENTAL FINITE

- The eight exact rows in (6.1).

### OPEN

- Exact all-prime valuations beyond (1.6), including the apparent
  $p\equiv7\pmod {20}$ behavior suggested by $p=7,a=4$.
- Any positive-mass deeper divisor theorem or Route-1 improvement.
- Any conclusion about $e+\pi$.
