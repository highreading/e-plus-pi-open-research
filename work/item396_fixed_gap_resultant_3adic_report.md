> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 396 — A logarithmically growing fresh-prime gap corridor and the zero-capacity fixed-gap-height barrier

Date: 2026-09-01  
Status: **WORK-ONLY, UNAUDITED, NO CENTRAL EDIT, NO BOOKING**

## 1. Capacity first, and provenance

For a fresh prime write



$$
p=6m+q,\qquad q>0.
$$



Since $p>3$ is prime, $q$ is odd and $3\nmid q$.  A theorem for
only finitely many fixed gaps, finitely many affine rays, or even
$o(m/\log m)$ gap values has zero normalized Chebyshev capacity: at a
fixed row there are at most that many candidate primes, each with
$\log p=O(\log m)$ in a linear window.

The frozen fixed-gap construction gives a rational determinant



$$
\mathcal R_q=C_0(q)T_1(q)-C_1(q)T_0(q).
 \tag{1.1}
$$



The following valuation and nonvanishing theorem are **inherited from
canonical Item 148**, not new Item-396 credit:



$$
\boxed{
 v_3(\mathcal R_q)
 =1-(q-1)-v_3((q-1)!)
 -\frac{q-1}{2}
 -v_3\!\left(\left(\frac{q-1}{2}\right)!\right).}
 \tag{1.2}
$$



In particular, Item 148 already proves



$$
\boxed{\mathcal R_q\ne0
 \quad\text{for every odd }q\ge1\text{ with }3\nmid q.}
 \tag{1.3}
$$



Combining canonical Item 148 with the frozen Item-146 numerator-height
estimate gives the unconditional implication



$$
\boxed{
 p=6m+q>129q^3\,62208^q
 \quad\Longrightarrow\quad
 p\nmid\gcd(\lambda_{0,m},\lambda_{1,m}).}
 \tag{1.4}
$$



The new Item-396 content is the following global method-class conclusion.

**Fixed-gap carrier/ordinary-height no-go.**  Suppose a proof method assigns
to every gap $q$ a nonzero integer carrier $N_q$, proves



$$
|N_q|\le A q^C B^q
 \qquad(A>0,\ C\ge0,\ B>1),
 \tag{1.5}
$$



and obtains exclusions only from the sufficient ordinary-height comparison
$p>Aq^CB^q$ (hence $p>|N_q|$).  Apart from finitely many $q$, this
height comparison can operate at a given row only for $q=O(\log m)$.
Consequently, even perfect success inside its available window controls only



$$
O((\log m)^2)=o(m)
 \tag{1.6}
$$



logarithmic prime mass.  Its normalized Chebyshev capacity is zero.

For the actual carrier in (1.4), no exceptional small gaps are needed.
Indeed, (1.4) is impossible when $q>m$, since then



$$
p=6m+q<7q<129q^3\,62208^q.
$$



When $q\le m$, one has $p\le7m$, and (1.4) can hold only if



$$
q<\frac{\log(7m/129)}{\log62208}=O(\log m).
 \tag{1.7}
$$



There are only $O(\log m)$ such gaps, proving (1.6).  More generally,
the same proof applied to (1.5) gives



$$
q<\frac{\log(7m/A)}{\log B}
$$



whenever $q\le m$; while for $q>m$, the inequality
$Aq^CB^q\ge7q>p$ holds for all sufficiently large $q$.  This proves
the stated method-class theorem.

There is also a genuinely moving, albeit zero-capacity, exclusion corridor.
Put $B=62208$, and whenever the numerator is positive define



$$
Q_m=\left\lfloor
 \frac{\log m-4\log\log m-\log129}{\log B}
 \right\rfloor.
 \tag{1.8}
$$



For every admissible $1\le q\le Q_m$, one has



$$
B^q\le\frac{m}{129(\log m)^4},
 \qquad q^3\le(\log m)^3,
$$



and hence



$$
129q^3B^q\le\frac m{\log m}<6m<p.
$$



Therefore



$$
\boxed{
 6m<p\le6m+Q_m
 \quad\Longrightarrow\quad
 p\nmid\gcd(\lambda_{0,m},\lambda_{1,m})}
 \tag{1.9}
$$



for every prime in the interval once $Q_m\ge1$.  Since
$Q_m=(\log m-4\log\log m+O(1))/\log62208$, this improves the finite
fixed-gap list to a logarithmically widening interval, but its total
possible logarithmic mass remains



$$
O((\log m)^2)=o(m).
 \tag{1.10}
$$



Therefore the result has two complementary consequences.

1. Canonical Item 148 closes the global nonvanishing problem for the
   intermediate fixed-gap determinant; Sections 3--6 below give an
   independent replay, not a second booking.
2. Item 396 supplies the growing corridor (1.9) and proves the scoped
   no-go: any fixed-gap carrier plus an ordinary exponential height
   comparison alone has zero capacity.  A positive-rate support theorem
   must use the final power-of-two condition, a genuinely moving-gap
   finite-field invariant, or an equivalent additional input.

## 2. Exact fixed-gap system

Put



$$
n=q-1,
 \qquad
 N=\frac{q-1}{2},
 \qquad
 \alpha=\frac{2q}{3}-1.
$$



The four frozen coefficients may be written as



$$
C_0(q)=[z^n](2+z)
 \bigl((1+z)(1+z+z^2/2)\bigr)^\alpha,
 \tag{2.1}
$$





$$
C_1(q)=\frac12[z^n](2+z)^4
 \bigl((1+z)(1+z+z^2/2)\bigr)^{\alpha-1},
 \tag{2.2}
$$





$$
T_0(q)=[z^n]
 \frac{(1+z)(1+z^2)^\alpha}{(1-z)^q},
 \tag{2.3}
$$





$$
T_1(q)=[z^n]
 \frac{(1+z)^4(1+z^2)^{\alpha-1}}{(1-z)^q}.
 \tag{2.4}
$$



For every $p=6m+q$, the actual integral log residues satisfy



$$
\lambda_{0,m}\equiv C_0(q)X-T_0(q),
 \qquad
 \lambda_{1,m}\equiv C_1(q)X-T_1(q)\pmod p,
 \tag{2.5}
$$



where



$$
X=2^{2m+q-1}.
$$



All denominators in (2.1)–(2.5) are products of powers of $2$ and $3$,
and hence are units modulo the present prime $p\ge7$.  Simultaneous
vanishing in (2.5) necessarily gives



$$
p\mid\operatorname{num}\mathcal R_q.
 \tag{2.6}
$$



In the original Item-146 stage, (2.6) was useful for a general $q$ only
conditionally on $\mathcal R_q\ne0$; canonical Item 148 removed that
condition.

## 3. A binomial 3-adic lemma

If



$$
\gamma=a+\frac{s}{3},
 \qquad a\in\mathbb Z,
 \qquad3\nmid s,
$$



then for every $k\ge0$,



$$
\boxed{
 v_3\binom\gamma k=-k-v_3(k!).}
 \tag{3.1}
$$



Indeed,



$$
\binom\gamma k
 =\frac{\prod_{j=0}^{k-1}(3(a-j)+s)}{3^k k!},
$$



and every numerator factor is a $3$-adic unit.

This elementary observation makes the connection determinant rigid.  It
also explains why a relative computation modulo $27$, rather than a
large symbolic resultant, is enough.

## 4. Finite-defect expansion of the full coefficients

The exact identity



$$
\bigl((1+z)(1+z+z^2/2)\bigr)^\alpha
 =\sum_{h\ge0}\binom\alpha h2^{-h}z^{2h}(1+z)^{2\alpha-h}
 \tag{4.1}
$$



turns (2.1)–(2.2) into explicit binomial sums.  In a term indexed by $h$
and by a selected monomial $z^a$ from $(2+z)$ or $(2+z)^4$, let



$$
d=n-2h-a.
$$



Relative to the leading binomial $\binom{2\alpha}{n}$, equation (3.1)
gives the valuation defect



$$
h+a+v_3\!\left(\frac{n!}{h!d!}\right)\ge h+a.
 \tag{4.2}
$$



Consequently, after scaling by the leading binomial, every term with
$h+a\ge3$ vanishes modulo $27$.  Only the finite set



$$
h+a\le2
 \tag{4.3}
$$



survives.

For the tail coefficients (2.3)–(2.4), write the selected power of
$z^2$ as $N-h$.  Relative to $\binom\alpha N$, its defect is



$$
h+v_3\!\left(\frac{N!}{(N-h)!}\right)\ge h.
 \tag{4.4}
$$



Thus only $h=0,1,2$ survives modulo relative precision $27$.

Equations (4.2) and (4.4) are uniform in $q$.  This is the theorem-level
reason the calculation below is finite; it is not extrapolation from a
bounded list of gaps.

## 5. The two exact ratio functions modulo 27

Evaluating the surviving terms in (4.3) gives



$$
\frac{C_0(q)}{\binom{2\alpha}{n}}
 \equiv
 \frac{Q_C(q)}{4q(q+3)(4q-9)}\pmod{27},
 \tag{5.1}
$$





$$
\frac{C_1(q)}{\binom{2\alpha}{n}}
 \equiv
 \frac{P_C(q)}{4(2q-3)(4q-15)(4q-9)}\pmod{27},
 \tag{5.2}
$$



where



$$
\begin{aligned}
 P_C(q)={}&18q^5+75q^4-524q^3-2103q^2+10278q-9504,\\
 Q_C(q)={}&9q^5-57q^4+314q^3-669q^2+405q-162.
\end{aligned}
\tag{5.3}
$$



Similarly, (4.4) gives



$$
\frac{T_0(q)}{\binom\alpha N}
 \equiv
 \frac{Q_T(q)}{8(q+3)(q+9)}\pmod{27},
 \tag{5.4}
$$





$$
\frac{T_1(q)}{\binom\alpha N}
 \equiv
 \frac{P_T(q)}{16(q+3)(2q-3)}\pmod{27},
 \tag{5.5}
$$



where



$$
\begin{aligned}
 P_T(q)={}&3q^6+54q^5+150q^4-624q^3-889q^2+1530q-288,\\
 Q_T(q)={}&3q^6+18q^5-30q^4-12q^3+227q^2-102q+216.
\end{aligned}
\tag{5.6}
$$



For $3\nmid q$, every denominator displayed in (5.1)–(5.5) is a
$3$-adic unit.  The numerators are units as well:



$$
Q_C(q)\equiv2q^3,\quad P_C(q)\equiv q^3,\quad
 Q_T(q)\equiv2q^2,\quad P_T(q)\equiv2q^2\pmod3.
$$



It follows that



$$
v_3(C_0)=v_3(C_1)=-n-v_3(n!),
 \tag{5.7}
$$





$$
v_3(T_0)=v_3(T_1)=-N-v_3(N!).
 \tag{5.8}
$$



After canceling the common leading binomials, put



$$
\mathscr C(q)=
 \frac{q(q+3)P_C(q)}{(2q-3)(4q-15)Q_C(q)},
 \tag{5.9}
$$





$$
\mathscr T(q)=
 \frac{(q+9)P_T(q)}{2(2q-3)Q_T(q)}.
 \tag{5.10}
$$



Then



$$
\frac{C_1}{C_0}\equiv\mathscr C(q),
 \qquad
 \frac{T_1}{T_0}\equiv\mathscr T(q)\pmod{27}.
 \tag{5.11}
$$



## 6. Uniform separation in the six admissible classes

Exact polynomial cross-multiplication proves



$$
\mathscr C(q+18)\equiv\mathscr C(q)\pmod{27},
 \qquad
 \mathscr T(q+18)\equiv\mathscr T(q)\pmod{27}.
 \tag{6.1}
$$



The replay verifies (6.1) by showing every coefficient of both cross
differences is divisible by $27$; it does not sample values of $q$.
The denominators reduce to units for both $q\equiv1,2\pmod3$.

It remains to evaluate the six admissible classes modulo $18$:



$$
\begin{array}{c|c|c|c}
q\bmod18&\mathscr C(q)&\mathscr T(q)&\mathscr T(q)-\mathscr C(q)\pmod{27}\\ \hline
1&4&1&24\\
5&19&4&12\\
7&22&10&15\\
11&10&13&3\\
13&13&19&6\\
17&1&22&21
\end{array}
\tag{6.2}
$$



Every entry in the last column is divisible by $3$ and not by $9$.
Therefore



$$
v_3\left(\frac{T_1}{T_0}-\frac{C_1}{C_0}\right)=1.
 \tag{6.3}
$$



Since



$$
\mathcal R_q=C_0T_0
 \left(\frac{T_1}{T_0}-\frac{C_1}{C_0}\right),
$$



equations (5.7), (5.8), and (6.3) prove (1.2) for every $q\ge5$.
For $q=1$, the frozen formulas give $\mathcal R_1=-6$, and (1.2)
again gives $v_3=1$.  This completes the proof of (1.2)–(1.3).

## 7. Unconditional moving-gap corollary and sharp information-class boundary

The frozen coefficient majorization proves, whenever $\mathcal R_q\ne0$,



$$
|\operatorname{num}\mathcal R_q|
 \le129q^3\,62208^q.
 \tag{7.1}
$$



Canonical Item 148 discharges the only condition in that sentence.  If both
residues vanished, (2.6) would make $p$ a divisor of the nonzero numerator,
and
therefore



$$
p\le129q^3\,62208^q.
$$



This proves (1.4).  In particular, for every fixed admissible $q$, all
sufficiently large primes $p=6m+q$ are excluded without factorization.
The family is infinite by Dirichlet's theorem for either admissible residue
class modulo $6$.  Item 396 adds the simultaneous moving corridor (1.9)
and proves that no argument using only an exponential-in-gap carrier height
can enlarge this to a positive-capacity window.

However, (1.5)–(1.6) prove that all exclusions obtainable from this ordinary
height comparison occupy only a zero-rate gap window.  Extending exact
factorizations from $q<49$ to $q<10^6$ would remain strategically
irrelevant unless accompanied by a moving-gap theorem with linear
Chebyshev capacity.

## 8. Exact remaining support problem

The all-depth Item-390 reduction says



$$
c_m^{>}>1
 \quad\Longleftrightarrow\quad
 \text{some }p>6m\text{ divides both }\lambda_{0,m},\lambda_{1,m}.
$$



The combined Items 146, 148, and 390 reduce every such possible prime to the
exact finite system



$$
p\mid\operatorname{num}\mathcal R_q,
 \qquad p=6m+q,
 \tag{8.1}
$$





$$
C_0(q)2^{2m+q-1}\equiv T_0(q),
 \qquad
 C_1(q)2^{2m+q-1}\equiv T_1(q)\pmod p.
 \tag{8.2}
$$



There is no longer a possible zero determinant hiding an entire gap ray.
The sole remaining obstruction is the actual power-of-two position in
(8.2) at prime divisors of the nonzero connection determinant.

The frozen cubic carrier makes that position algebraic.  With



$$
E=2m+q-1=\frac{p+2q-3}{3},
 \qquad X=2^E,
$$



Fermat's theorem gives



$$
X^3=2^{p-1}4^{q-1}\equiv4^{q-1}\pmod p.
 \tag{8.3}
$$



Hence, on putting



$$
U_s(q)=T_s(q)^3-4^{q-1}C_s(q)^3,
$$



every common zero satisfies



$$
\mathcal R_q\equiv U_0(q)\equiv U_1(q)\equiv0\pmod p.
 \tag{8.4}
$$



For $q\equiv5\pmod6$, one has $p\equiv2\pmod3$, so the cube map on
$\mathbb F_p$ is bijective.  In that half of the admissible classes,
$U_0=U_1=0$ is already equivalent to the two equations (8.2), including
the cases in which one of the $C_s$ vanishes; the connection determinant
is then redundant.  For $q\equiv1\pmod6$, it is needed to select one
common cube-root branch.

There is an exact primitive integer version.  Choose a common clearing
$D$, supported only at $2,3$, put



$$
c_s=DC_s,qquad t_s=DT_s,qquad g_s=\gcd(c_s,t_s),
$$



and define



$$
W_s(q)=\frac{t_s^3-4^{q-1}c_s^3}{g_s^2}\in\mathbb Z.
 \tag{8.5}
$$



Then, for every compatible $q\equiv5\pmod6$,



$$
\boxed{
 p\mid\lambda_{s,m}\iff p\mid W_s(q),
 \qquad
 p\mid\lambda_{0,m},\lambda_{1,m}
 \iff p\mid\gcd(W_0(q),W_1(q)).}
 \tag{8.6}
$$



Indeed, $D$ is a $p$-unit, and (8.2) says
$D\lambda_s\equiv c_sX-t_s\pmod p$.  Since cubing is an automorphism of
$\mathbb F_p$, the equality $t_s^3=4^{q-1}c_s^3=X^3c_s^3$ is
equivalent to $t_s=Xc_s$, including the zero-coordinate cases.  Dividing
by $g_s^2$ does not change this radical condition: if
$h=\min(v_p(c_s),v_p(t_s))$, the cubic numerator contains $p^{3h}$,
whereas $g_s^2$ removes exactly $p^{2h}$.  This is a first-digit
saturation theorem, not an all-depth identity for
$v_p(\lambda_{s,m})$; the fixed-gap formula (8.2) is only modulo $p$.

This carrier reduction is sharp in three separate senses.

1. The determinant alone is insufficient.  At
   $(q,p,m)=(5,11,1)$, one has
   $\mathcal R_5=77/729\equiv0\pmod {11}$, but
   $(\lambda_0,\lambda_1)=(9,8)\pmod {11}$.
2. One cubic row is insufficient even in the bijective-cube class.  At
   $(q,p,m)=(5,677,112)$, the exact fixed-gap data reduce to
   

$$
(C_0,T_0,C_1,T_1,X)=(589,78,232,75,353)\pmod {677}.
$$


   Therefore
   

$$
(\lambda_0,\lambda_1)=(0,581),\qquad
   (U_0,U_1,\mathcal R_5)=(0,564,353)\pmod {677}.
$$


3. The two cubic rows are insufficient in the nonbijective class.  At
   $(q,p,m)=(1,7,1)$,
   

$$
(C_0,T_0,C_1,T_1,X)=(2,1,1,1,4)\pmod7,
$$


   so $U_0=U_1=0$, while
   $(\lambda_0,\lambda_1)=(0,3)$ and
   $\mathcal R_1=1\pmod7$.  The two rows chose distinct cube roots.

Thus, within the frozen direct carrier set
$\{\mathcal R_q,U_0,U_1\}$, the minimal radical carrier is exactly
$(U_0,U_1)$ on the $q\equiv5\pmod6$ half and
$(\mathcal R_q,U_0,U_1)$ on the $q\equiv1\pmod6$ half.  These are
minimality/no-go examples, not common-zero counterexamples.

Canonical Item 157 packages (8.4) in a $3\times6$ cubic multiplication
matrix.  Its still-open uniform target is



$$
d_3(q)\mid P_q,
 \qquad
 P_q=\prod_{j=0}^{q-2}(2q-3-3j).
 \tag{8.7}
$$



For an actual compatible prime $p=6m+q$, one has $p\nmid P_q$: each
factor lies strictly between $-p$ and $2p$, and a factor equal to
$0$ or $p$ would force $3\mid q$.  Thus (8.7), or the weaker
primewise radical support statement sufficient for (8.4), would prove the
full large-prime support conjecture.  Item 396 does not prove (8.7); the
existing verification through $q\le1001$ remains finite evidence.

A full support proof must therefore establish one of the following uniform
statements:

1. every compatible prime divisor in (8.1) fails (8.2);
2. the primes satisfying both (8.1) and (8.2) have weighted mass $o(m)$;
3. an independent Hasse--Witt or multiplicative-character invariant
   excludes the same power-of-two position on a positive-capacity moving
   gap set;
4. the uniform Smith-support statement (8.7), or its compatible-prime
   radical weakening.

The intermediate-resultant nonvanishing problem is closed and should not be
reopened by further finite scans.

## 9. Ledger effect and scope

### Proved

* The logarithmically widening interval theorem (1.9).
* The general zero-capacity theorem for every carrier satisfying (1.5) and
  used only through ordinary height comparison.
* The exact minimal direct cubic-carrier classification in the two
  admissible congruence classes, including three irreducibility witnesses.
* A second exact replay of canonical Item 148's formula (1.2), with no new
  credit or booking for that inherited theorem.
* Unconditional height exclusion (1.4), inherited by combining Items
  146 and 148.
* Exact localization of the remaining support conjecture to (8.1)–(8.2).

### Not proved

* $c_m^{>}=1$ or the full support conjecture.
* Failure of the final power-of-two congruence for every candidate divisor.
* The uniform cubic Smith-support divisibility (8.7).
* Weighted zero density across proportional moving gaps.
* Any positive Route-1 divisor or ledger rate.
* Route-1 closure or irrationality of $e+\pi$.

Thus



$$
\boxed{\Delta r_{\rm booked}=0.}
$$



The result closes the ordinary exponential-height comparison as a
positive-capacity method and supplies a growing exclusion corridor.  It
does not alter the numerical Route-1 ledger, and it does not rebook the
already canonical Item-148 nonvanishing theorem.

## 10. Replay and dependencies

Deterministic replay:

```text
python work/item396_fixed_gap_resultant_3adic_certificate.py \
  --output work/item396_fixed_gap_resultant_3adic_certificate.replay.json
```

The replay verifies:

1. the exact finite-defect ratio formulas;
2. polynomial period $18$ modulo $27$ by coefficient divisibility;
3. all six admissible residue classes;
4. the valuation formula against the frozen coefficient definitions on
   normalization rows only;
5. exact sample inequalities for the closed-form moving corridor;
6. the ordinary-height capacity calculation and method-class statement.

The finite normalization rows are not the proof of all-gap nonvanishing;
that inherited Item-148 theorem is also independently recovered here by
the defect lemma and symbolic period certificate.  The corridor and
capacity statements rest on the displayed inequalities, not on sample
rows.

Primary dependencies:

* `sources/mixed_cubic_large_prime_log_residue_theorem.md`;
* `sources/mixed_cubic_large_prime_two_pole_obstruction.md`;
* `sources/mixed_cubic_connection_determinant_3adic_nonvanishing.md`;
* `sources/mixed_cubic_cube_smith_reduction.md`;
* `sources/mixed_cubic_fresh_prime_coprimality_supplement.md`;
* `work/item390_mixed_cubic_fresh_primitive_saturation_report.md`.

All Item-396 artifacts are confined to `work/`.  No central document is
edited and no mass is booked.
