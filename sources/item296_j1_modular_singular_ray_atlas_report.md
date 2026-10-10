> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 296 — exact modular singular-ray atlas for the $E_h^*$ recurrence

Date: 2026-08-31

## 1. Outcome

Item 293 proves the primitive joint-content-one recurrence



$$
\sum_{k=0}^{3}Q_k(h)E_{h+3k}^*=0.           \tag{1.1}
$$



Actual rows have



$$
p=4h+6s+3,\qquad h,s\geq1,\qquad3\nmid h,\qquad p\text{ prime}. \tag{1.2}
$$



This item gives a complete exact atlas of the ways in which a coefficient
of (1.1) can vanish modulo its actual row prime.

The linear factors have exactly three infinite actual singular rays:



$$
\boxed{
\begin{array}{c|c|c}
s&p&\text{vanishing coefficient and factor}\\ \hline
2&4h+15&Q_1:\ 4h+15\\
4&4h+27&Q_2:\ 4h+27\\
6&4h+39&Q_3:\ 4h+39.
\end{array}}                                                \tag{1.3}
$$



Here and below a ray contains precisely those $h\geq1$, $3\nmid h$,
for which the displayed $p$ is prime. Apart from these rays, the
complete finite actual-prime list is



$$
\begin{array}{c|c|c|l}
h&s&p&\text{linear factors divisible by }p\\ \hline
1&1&13&2h+11\text{ in }Q_0,Q_1;\quad4h+35=3p\text{ in }Q_3\\
2&1&17&2h+13\text{ in }Q_0,Q_1,Q_2\\
1&2&19&2h+17\text{ in }Q_0,Q_1,Q_2.
\end{array}                                                 \tag{1.4}
$$



The last row overlaps the $s=2$ ray, so $4h+15$ also vanishes in
$Q_1$ there. The only further positive equality solution is
$(h,s,p)=(4,1,25)$, which is not a prime row.

The nonlinear positive cores reduce exactly to four primitive polynomials
$\widehat R_k(s)$ of degrees $5,9,9,5$:



$$
p\mid q_k(h)\quad\Longleftrightarrow\quad
              p\mid\widehat R_k(s).                         \tag{1.5}
$$



Every $\widehat R_k$ is irreducible over $\mathbb Q$. Thus these are
genuine varying-prime congruences, not hidden additional fixed-$s$
rays.

Finally, in the interior $s\geq7$, (1.1) gives exact
same-characteristic three-state transport along



$$
(h,s)\longmapsto(h+3,s-2).           \tag{1.6}
$$



Off the two endpoint-core loci, this transport is invertible. It does
not propagate a scalar zero: among unrestricted valid recurrence states,
vanishing of any selected coordinate is a two-dimensional hyperplane.
This is an operator-specific modular obstruction only. It makes no claim
that the pinned actual $E_h^*$ initial orbit meets such a hyperplane.

No weighted-density bound follows. The retained conditional $j=1$
ceiling is $1/36$ per $6m$, and the new booking is zero.

## 2. Complete linear factor record

Write $Q_k=\kappa_kF_kq_k$, with



$$
(\kappa_0,\kappa_1,\kappa_2,\kappa_3)
                       =(-4096,-512,-4,27).                  \tag{2.1}
$$



The complete linear products, including multiplicities, are



$$
\begin{aligned}
F_0={}&(h+1)(h+3)(h+5)(h+6)(2h+1)^2(2h+3)^2(2h+5)^2\\
 &\cdot(2h+7)(2h+9)^2(2h+11)(2h+13)(2h+17)(4h+3),\\
F_1={}&h(h+6)(2h+7)(2h+9)^2(2h+11)(2h+13)(2h+17)\\
 &\cdot(4h+1)(4h+5)(4h+7)(4h+11)(4h+15),\\
F_2={}&h(h+3)(2h+13)(2h+17)(4h+1)(4h+5)(4h+7)(4h+11)\\
 &\cdot(4h+13)(4h+17)(4h+19)(4h+23)(4h+27),\\
F_3={}&h(h+3)(h+6)(h+9)(4h+1)(4h+5)(4h+7)(4h+11)\\
 &\cdot(4h+13)(4h+17)(4h+19)(4h+23)(4h+25)(4h+29)\\
 &\cdot(4h+31)(4h+35)(4h+39).
\end{aligned}                                                \tag{2.2}
$$



Every prime in the four scalars is $2$ or $3$, whereas every actual
prime is at least $13$. Hence the scalars are always units.

## 3. Exhaustive divisibility proof for the linear factors

All factors in (2.2) have the form $ah+c$, with
$a\in\{1,2,4\}$. The following size and parity argument audits every
possible multiple of $p$, rather than merely solving equality.

For $a=1$, the largest factor is $h+9<p$, so no factor is singular.
For $a=2$,



$$
0<2h+c<2p.                          \tag{3.1}
$$



Thus divisibility forces $2h+c=p$, or



$$
c=2h+6s+3.                          \tag{3.2}
$$



Solving (3.2) over the constants occurring in (2.2) gives



$$
\begin{array}{c|c|c|c}
c&h&s&p\\ \hline
11&1&1&13\\
13&2&1&17\\
17&1&2&19\\
17&4&1&25.
\end{array}                                                  \tag{3.3}
$$



The first three rows give (1.4); the last is composite. Since (3.1)
excludes $2p$ and every higher multiple, this list is complete for all
slope-two factors.

For $a=4$, every constant in (2.2) is odd and at most $39$, and



$$
0<4h+c<4p.                          \tag{3.4}
$$



If $p\mid4h+c$, the quotient is odd. Consequently the complete list
of possible multiples is $p$ or $3p$; $2p$ is excluded by parity.
The equality $4h+c=p$ gives



$$
c=6s+3.                             \tag{3.5}
$$



Among the displayed constants, positive $s$ in (3.5) gives exactly
$c=15,27,39$, hence exactly the three rays (1.3). The alternative
$4h+c=3p$ gives



$$
c=8h+18s+9.                         \tag{3.6}
$$



Since $c\leq39$ and $h,s\geq1$, (3.6) has the unique solution
$(h,s,c)=(1,1,35)$, producing $4h+35=39=3\cdot13$. This is the
exceptional entry in (1.4). Equations (3.1)--(3.6) prove completeness,
including all possible $p,2p,3p$ multiples.

## 4. Exact reduction of the positive cores

Let $q_k(h)$ be the positive-coefficient core from Item 293 and let
$d_k=\deg q_k$. Define the integral degree-$d_k$ polynomial



$$
R_k(s)=4^{d_k}q_k\!\left(-\frac{6s+3}{4}\right),\qquad
 c_k=\operatorname {cont}(R_k),\qquad
 \widehat R_k=R_k/c_k.                                     \tag{4.1}
$$



Thus $R_k$ is the raw integral polynomial and $\widehat R_k$ is its
primitive part. Their contents are



$$
\begin{array}{c|c|c|c}
k&d_k&c_k&\text{factorization of }c_k\\ \hline
0&5&432&2^4 3^3\\
1&9&62208&2^8 3^5\\
2&9&139968&2^6 3^7\\
3&5&432&2^4 3^3.
\end{array}                                                  \tag{4.2}
$$



The coefficient lists of the primitive parts, low-to-high, are



$$
\begin{array}{c|l}
0&[8020237269,-10999028534,5908858568,-1554373296,
200453520,-10153440]\\
1&[170697572048619,-1014517816488354,2244006801245080,
-2578054557696720,1747502374047296,-737602478969472,
196061674014336,-31894686229248,2898116686080,-112581342720]\\
2&[274738685610467925,-1331677272537780630,2585017656107807648,
-2653425641634319872,1618162491397819040,-617758458754567104,
149363074051844096,-22241272046251008,1862398419237120,
-67131783544320]\\
3&[104974345,-413836374,581228072,-356882736,98919120,-10153440].
\end{array}                                                  \tag{4.3}
$$



On an actual row, $4h\equiv-(6s+3)\pmod p$. Therefore (4.1) gives



$$
4^{d_k}q_k(h)\equiv
                  c_k\widehat R_k(s)\pmod p.                \tag{4.4}
$$



All primes in $4c_k$ are $2$ or $3$, and $p\geq13$. Every
scaling factor in (4.4) is consequently a $p$-unit, proving the iff in
(1.5). In particular, primes dividing a content have been isolated and
cannot be actual row primes.

The checker applies Rabin's exact finite-field irreducibility criterion.
The witnesses are



$$
\begin{array}{c|c|c}
k&\deg\widehat R_k&\text{prime modulus with irreducible reduction}\\ \hline
0&5&17\\
1&9&53\\
2&9&157\\
3&5&17.
\end{array}                                                  \tag{4.5}
$$



The leading coefficients remain nonzero in the witness characteristics.
Gauss's lemma therefore proves that all four primitive polynomials are
irreducible over $\mathbb Q$, hence have no integer root. For each
fixed positive $s$, $\widehat R_k(s)$ is a fixed nonzero integer, so
only finitely many primes on that fixed $s$-line can be core-singular.
This fixed-line finiteness is not uniform as $s$ varies and gives no
weighted-density estimate.

There is one exact adjacent-cell identity:



$$
q_0(h)=q_3(h+3),\qquad
 \widehat R_0(s)=\widehat R_3(s-2).                         \tag{4.6}
$$



Thus a trailing core singularity is the next diagonal cell's leading
core singularity. It aligns the singular cells but does not remove them.

Combining Sections 2--4 gives the complete criterion



$$
\boxed{p\mid Q_k(h)\quad\Longleftrightarrow\quad
\begin{array}{l}
p\text{ divides one of the completely classified linear factors of }F_k,\\
\text{or }p\mid\widehat R_k(s).
\end{array}}                                                 \tag{4.7}
$$



Overlaps are allowed and are explicitly recorded in (1.4).

## 5. Same-characteristic diagonal transport

For $0\leq j\leq3$, the shifted index $h+3j$ lies on the same prime
with row parameter $s-2j$, because



$$
4(h+3j)+6(s-2j)+3=p.                                      \tag{5.1}
$$



If $s\geq7$, all four row parameters are positive. Moreover,



$$
p-\bigl(4(h+3j)+3\bigr)=6(s-2j)>0.                        \tag{5.2}
$$



The Item 288 localization therefore makes every $E_{h+3j}^*$ in
(1.1) $p$-integral. The recurrence is an exact relation over
$\mathbb F_p$ on the actual diagonal.

With the state



$$
v_h=(E_h^*,E_{h+3}^*,E_{h+6}^*)^{\mathsf T},
$$



forward transport is



$$
v_{h+3}=T_hv_h,\qquad
T_h=
\begin{pmatrix}
0&1&0\\
0&0&1\\
-Q_0/Q_3&-Q_1/Q_3&-Q_2/Q_3
\end{pmatrix},\qquad
\det T_h=-\frac{Q_0(h)}{Q_3(h)}.                            \tag{5.3}
$$



Every linear factor of $Q_0$ and $Q_3$ is a unit in the interior
$s\geq7$, by the complete atlas. Hence



$$
T_h\text{ is defined and invertible}\quad\Longleftrightarrow\quad
 p\nmid\widehat R_0(s)\widehat R_3(s).                     \tag{5.4}
$$



This is the natural exact three-state same-characteristic transport
supplied by the recurrence. The three structural rays in (1.3) lie at the boundary
$s\leq6$; core singularities are the only possible loss of invertibility
on an interior cell.

## 6. Exact recurrence-only obstruction

Consider a finite diagonal interval on which (5.4) holds. The
unrestricted solution states of (1.1) form $\mathbb F_p^3$, and every
transport matrix is invertible. Evaluation of any selected scalar term
is a nonzero linear functional on this state space. Its zero set is
therefore a dimension-two hyperplane containing exactly $p^2$ valid
recurrence states. Pullback by any product of the $T_h$ remains a
dimension-two hyperplane.

Consequently, the recurrence operator and its regularity alone provide
no implication of the form



$$
E_h^*\equiv0\pmod p
               \quad\Longrightarrow\quad
               \text{a forced zero or contradiction elsewhere}.     \tag{6.1}
$$



This is not a no-go for the actual sequence. The Item 293 initials pick
one particular orbit in the three-dimensional solution module; that
orbit may avoid the hyperplanes for an additional, sequence-specific
reason. Evaluating that initial orbit, or using congruence, monodromy,
Cartier, fixed-diagonal, or auxiliary-local structure beyond the bare
recurrence, remains open.

Thus Item 296 proves a sharply scoped recurrence-only obstruction, not a
moving-prime nonvanishing theorem and not a density theorem.

## 7. Capacity audit and strict scope

The atlas removes no actual $E_h^*$ gate. The three infinite rays are
coefficient singularities, not divisibility of $E_h^*$, and their
possible prime mass is not booked. The finite rows have zero asymptotic
weight. Fixed-$s$ core finiteness is not uniform over the moving set of
$s$ and supplies no collective radical saving.

Therefore



$$
\boxed{\text{new linear log rate}=0,\quad
       \text{new divisibility exponent}=0,\quad
       \text{capacity booked}=0.}                            \tag{7.1}
$$



The conditional $j=1$ ceiling remains $1/6$ per $m$, equivalently
$1/36$ per $6m$. Route 1 and every conclusion about $e+\pi$ remain
open.

## 8. Reproducibility

From the archive root, run

~~~text
python scripts/item296_j1_modular_singular_ray_atlas_certificate.py --output results/item296_j1_modular_singular_ray_atlas_certificate.replay.json
~~~

The checker uses exact standard-library integer and finite-field
polynomial arithmetic. It pins Item 293, solves the finite Diophantine
factor equations, verifies all $p,2p,3p$ cases, constructs (4.1), and
checks the four Rabin witnesses. It performs no scan of actual primes.

- **PROVED:** the complete linear atlas (1.3)--(1.4), the exact core iff
  (1.5), irreducibility (4.5), the adjacent identity (4.6), and the
  regular transport and unrestricted-state hyperplane theorem.
- **OPEN:** nonvanishing or weighted density for the pinned actual
  $E_h^*$ orbit, every new capacity saving, and Route 1.
- **NOT CLAIMED:** that any unrestricted zero state belongs to the actual
  $E_h^*$ orbit, or that a coefficient singularity is an $E_h^*$
  zero.
