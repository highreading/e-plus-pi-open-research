> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Mixed-cubic minimal matching: exact outside-prime ledger and a Cartier-support obstruction

Date: 2026-08-28.

## 1. Scope and verdict

Let



$$
\alpha=e+\pi.
$$



This note asks whether the now-rigorous mixed-cubic forms, after minimal
matching with the standard beta form for $e$, already satisfy the
fixed-support or moving-support criterion in
`sources/padic_subspace_prime_support_transcendence_criterion.md`.

The answer supplied by the currently proved arithmetic is negative in a
precise, limited sense.

* The final primitive pair and its outside-prime product are computed
  exactly in Theorem 3.1 below.
* The item-133 clearing, dyadic-coordinate statement, and certified
  Cartier divisor do not impose any upper bound on that outside-prime
  product.  Theorem 5.1 constructs integral data satisfying all three
  statements, with no extra content after the certified Cartier divisor,
  for which an arbitrarily prescribed fresh prime survives in the final
  target denominator.
* Blocks of these exact arithmetic countermodels force at least one new
  support prime per point.  Thus the same three item-133 statements do not
  imply the quantitative moving-support hypothesis either.

This is an insufficiency theorem about the presently certified
denominator/content information.  The countermodels are not the actual
mixed-cubic period integrals and do not satisfy their saddle-size
asymptotic.  Consequently this note does **not** prove that the actual
forms fail a support criterion.  A new theorem about the actual primitive
coordinates, the matching gcd, or the final content could still succeed.
No conclusion about the arithmetic nature of $e+\pi$ is asserted.

## 2. The exact mixed-cubic arithmetic input

For $m\geq1$, put



$$
M_j=\operatorname {lcm}(1,\ldots,j),\qquad
 T_m=\prod_{2m<p<3m}p,
 \qquad K_m=\frac{M_{4m+1}}{T_m},                                  \tag{1}
$$



where products indexed by $p$ are over primes.  The quotient $K_m$
is an integer because every prime in the displayed interval occurs to the
first power in $M_{4m+1}$.  The sharpened clearing from item 133 is



$$
\mathcal D_m^\sharp=2^{9m+5}K_m.                                  \tag{2}
$$



Write the mixed-cubic form as



$$
\Lambda_m^{(\pi)}=A_m+B_m\pi
$$



and define



$$
X_m=\mathcal D_m^\sharp A_m,\qquad
 Y_m=\mathcal D_m^\sharp B_m,
 \qquad
 \mathcal G_m=\prod_{p\in\mathcal P_m}p.                           \tag{3}
$$



The frozen Cartier theorem proves



$$
X_m,Y_m\in\mathbb Z,qquad
 \mathcal G_m\mid\gcd(X_m,Y_m).                                   \tag{4}
$$



It also proves the stronger dyadic statement



$$
2^{9m+5}B_m\in\mathbb Z.                                          \tag{5}
$$



In the notation (1)--(3), (5) is exactly



$$
K_m\mid Y_m.                               \tag{6}
$$



Indeed, $Y_m=K_m(2^{9m+5}B_m)$.  No converse minimal-denominator
claim is being used.

Remove the certified Cartier divisor, then remove the still-unknown extra
content:



$$
U_m=\frac{X_m}{\mathcal G_m},\qquad
 V_m=\frac{Y_m}{\mathcal G_m},\qquad
 c_m=\gcd(U_m,V_m).                                                  \tag{7}
$$



After an overall sign choice, the primitive $\pi$-form has the shape



$$
L=a+\varepsilon b\pi>0,qquad
 a\in\mathbb Z,quad b\in\mathbb Z_{>0},quad
 \varepsilon\in\{1,-1\},quad\gcd(a,b)=1,                          \tag{8}
$$



where



$$
a=\frac{\sigma U_m}{c_m},\qquad
 \varepsilon b=\frac{\sigma V_m}{c_m}
 \quad(\sigma\in\{1,-1\}).                                      \tag{9}
$$



The now-rigorous fixed-circle saddle theorem supplies analytic size and
nonvanishing information for the actual $A_m,B_m$.  It supplies no
prime-support statement for the integers in (7)--(9).

## 3. Exact minimal matching and primitive reduction

Choose the parity of $N$ so that the standard positive beta form is



$$
E_N=\varepsilon(q_Ne-p_N)>0,qquad
 p_N,q_N\in\mathbb Z,quad q_N>0,quad\gcd(p_N,q_N)=1.              \tag{10}
$$



To simplify notation in this section, write $p=p_N$ and $q=q_N$.
Set



$$
\Delta=\gcd(b,q),\qquad b=\Delta b_0,qquad q=\Delta q_0.          \tag{11}
$$



Then $\gcd(b_0,q_0)=1$, and the minimally matched positive form is



$$
W=b_0E_N+q_0L>0.                                                   \tag{12}
$$



Define



$$
P^*=b_0p-\varepsilon q_0a,qquad
 Q^*=\Delta b_0q_0=\frac{bq}{\Delta}.                              \tag{13}
$$



Direct expansion gives



$$
\varepsilon W=Q^*\alpha-P^*.               \tag{14}
$$



The next theorem makes the final content and every outside-prime
multiplicity explicit.

**Theorem 3.1 (exact final primitive pair and outside product).**  With
the notation above,



$$
\gcd(P^*,b_0q_0)=1,                                                \tag{15}
$$



and hence



$$
g:=\gcd(P^*,Q^*)=\gcd(P^*,\Delta),
 \qquad g\mid\Delta.                                                \tag{16}
$$



The final primitive pair is



$$
\boxed{
   P=\frac{P^*}{g},\qquad
   Q=\frac{Q^*}{g}=\frac{bq}{\Delta g},\qquad
   Q\alpha-P=\frac{\varepsilon W}{g}.}                             \tag{17}
$$



For a finite set $\mathcal S$ of primes and



$$
z_{\mathcal S^c}=\prod_{\ell\notin\mathcal S}
                         \ell^{v_\ell(z)}
 \quad(z\in\mathbb Z\setminus\{0\}),                             \tag{18}
$$



one has the exact multiplicity-sensitive identity



$$
\boxed{
 P_{\mathcal S^c}Q_{\mathcal S^c}
 =\frac{(P^*)_{\mathcal S^c}(Q^*)_{\mathcal S^c}}
        {g_{\mathcal S^c}^{2}}
 =\frac{(b_0p-\varepsilon q_0a)_{\mathcal S^c}
          (\Delta b_0q_0)_{\mathcal S^c}}
        {g_{\mathcal S^c}^{2}}.}                                  \tag{19}
$$



Consequently the fixed-support hypothesis for this matched form is
exactly



$$
\frac{b_0E_N+q_0L}{g}\,
 \frac{(b_0p-\varepsilon q_0a)_{\mathcal S^c}
       (\Delta b_0q_0)_{\mathcal S^c}}
      {g_{\mathcal S^c}^{2}}
 \leq
 \left(\frac{\Delta b_0q_0}{g}\right)^{1-\eta}.                   \tag{20}
$$



Here and below the outside part of a negative integer means the outside
part of its absolute value.

**Proof.**  If a prime $\ell$ divides $b_0$, then it divides $b$
and therefore does not divide $a$.  It also does not divide $q_0$.
Reduction of $P^*$ modulo $\ell$ gives the nonzero term
$-\varepsilon q_0a$.  Thus $\gcd(P^*,b_0)=1$.  Similarly, if
$\ell\mid q_0$, then $\ell\nmid p$ and $\ell\nmid b_0$, so
$P^*\equiv b_0p\not\equiv0\pmod\ell$.  This proves (15), including
prime-power multiplicities because it first proves that no common prime
exists.  Equations (13), (15) give (16).  Division by the full gcd gives
(17).  Finally, because $g\mid P^*,Q^*$, valuation by valuation,



$$
(P^*/g)_{\mathcal S^c}
   =(P^*)_{\mathcal S^c}/g_{\mathcal S^c},\qquad
 (Q^*/g)_{\mathcal S^c}
   =(Q^*)_{\mathcal S^c}/g_{\mathcal S^c}.
$$



Multiplying proves (19), and substitution into the criterion proves
(20). $\square$

Formula (19) is the relevant endpoint of the exact algebra.  The
certified Cartier product $\mathcal G_m$ has already been divided out
before $a,b$ are formed.  It is not a divisor of $\Delta$ or $g$
unless an additional synchronization theorem proves such a relation.

## 4. What a support proof would still have to control

The fixed-support theorem quoted in the companion source would prove
transcendence of $\alpha$ if, for one fixed finite $\mathcal S$, one
fixed $\eta>0$, and infinitely many actual matched forms with
$Q\to\infty$, inequality (20) held.

Thus an applicable theorem must control, with their full valuations,



$$
(b_0p_N-\varepsilon q_0a)_{\mathcal S^c},
 \qquad
 (\Delta b_0q_0)_{\mathcal S^c},                                   \tag{21}
$$



after the two exact cancellations by $g_{\mathcal S^c}$.  A radical
bound is not enough.  Neither (4), (5), nor (6) gives an upper bound for
either integer in (21).  In particular:

* $\mathcal G_m$ is common content before the primitive pair (8) is
  formed;
* the extra content $c_m$ is not determined by the Cartier theorem;
* $\Delta$ measures overlap of the *primitive* $\pi$-coefficient
  with $q_N$, an overlap not addressed by item 133;
* the final content $g$ is the residue-class condition (16), again not
  addressed by item 133.

The next theorem shows that this is a logical gap rather than merely a
missing estimate in the present proof.

## 5. Exact arithmetic countermodels

Fix $m$, abbreviate $K=K_m$, $\mathcal G=\mathcal G_m$, and
$D=\mathcal D_m^\sharp=2^{9m+5}K$.  Let $r$ be any prime satisfying



$$
r\nmid K\mathcal G q_N.                    \tag{22}
$$



Define rational coordinates by prescribing their cleared integers:



$$
X=\mathcal G,qquad Y=\mathcal GKr,qquad
 A=\frac XD,qquad B=\frac YD.                                    \tag{23}
$$



**Theorem 5.1 (fresh-prime realization).**  The data (23) satisfy every
denominator/content assertion (4)--(6), and in fact



$$
\gcd(X,Y)=\mathcal G,qquad
 2^{9m+5}B=\mathcal G r\in\mathbb Z.                               \tag{24}
$$



After removal of $\mathcal G$, their extra content is exactly one and
their primitive positive $\pi$-form is



$$
L=1+Kr\pi.                                 \tag{25}
$$



Match (25) with an even-index beta form $E_N=q_Ne-p_N>0$.  Put



$$
\Delta_0=\gcd(K,q_N).
$$



Then $\Delta=\Delta_0$, the final pair is given by (17), and



$$
r\mid Q,qquad r\nmid P.                    \tag{26}
$$



Therefore the item-133 arithmetic assertions alone permit an arbitrary
fresh prime to survive in the final primitive target coefficient.

**Proof.**  Equations (23) immediately give $D A=X\in\mathbb Z$,
$D B=Y\in\mathbb Z$, $\mathcal G\mid X,Y$, and (24).  After
division by $\mathcal G$, the pair is $(1,Kr)$, whose gcd is one.
This proves (25).

Condition (22) gives



$$
\Delta=\gcd(Kr,q_N)=\gcd(K,q_N)=\Delta_0.
$$



Thus $r\mid b_0=Kr/\Delta_0$, while $r\nmid q_0\Delta_0$.  With
$a=1$ and $\varepsilon=1$,



$$
P^*=b_0p_N-q_0\equiv-q_0\not\equiv0\pmod r,
 \qquad r\mid Q^*.
$$



Since $g\mid\Delta_0$, division by $g$ neither removes $r$ from
$Q^*$ nor inserts it into $P^*$.  This proves (26). $\square$

This construction also gives sharp fixed- and moving-support
countermodels for deductions based only on (4)--(6).

**Corollary 5.2 (fixed-support nonimplication).**  Fix a finite prime set
$\mathcal S$, an even beta index $N$, and $0<\eta\leq1$.  Among
the data (23), there are arbitrarily large primes $r\notin\mathcal S$
for which (20) fails.

**Proof.**  Here $\Delta_0,K,p_N,q_N$ are fixed and $g\leq\Delta_0$.
Because $r\notin\mathcal S$, (26) gives
$Q_{\mathcal S^c}\geq r$, while
$P_{\mathcal S^c}\geq1$.  From (12) and (25), using $\pi>3$,



$$
|Q\alpha-P|=\frac Wg
 >\frac{q_NK}{\Delta_0^2}\,3r.                                    \tag{27}
$$



On the other hand,



$$
Q=\frac{Kq_N}{\Delta_0g}r
 \leq\frac{Kq_N}{\Delta_0}r.                                      \tag{28}
$$



The left side of the support inequality is therefore bounded below by a
positive fixed constant times $r^2$, whereas its right side is bounded
above by a fixed constant times $r^{1-\eta}$.  It fails for all
sufficiently large allowed primes $r$. $\square$

**Corollary 5.3 (moving-support nonimplication).**  One can choose a
sequence of countermodels (23), at arbitrary indices $m_j,N_j$, with
pairwise distinct fresh primes $r_j$, so large that any selected support
set for which the support inequality holds for all $M$ points in a
block must contain all $M$ of the primes $r_j$.  Hence its number of
places $s$ satisfies



$$
s\geq M+1,
 \qquad
 \frac{s^6\log(s+2)}{\log M}\longrightarrow\infty.                 \tag{29}
$$



In particular, the quantitative moving-support condition
$s^6\log(s+2)=o(\log M)$ is not a consequence of (4)--(6).

**Proof.**  Choose the $r_j$ recursively, avoiding the finitely many
primes already used and the finitely many divisors excluded in (22).
Corollary 5.2, with its explicit comparison (27)--(28), lets each
$r_j$ be chosen so large that omission of $r_j$ makes the desired
support inequality fail for that point.  A support set valid for the
whole block must therefore contain every $r_j$.  The two conclusions
in (29) follow. $\square$

## 6. Exact conclusion and the missing lemma

For the actual mixed-cubic/beta match, Theorem 3.1 reduces the
classification-level support problem to the exact inequality (20).  No
proved item-133 statement bounds its outside factor (19).

The concrete missing input is one of the following genuinely new kinds
of theorem about the **actual** primitive coordinates:

1. a fixed finite $\mathcal S$ and a full-valuation upper bound for
   (19) strong enough to give (20) with a fixed margin;
2. an equivalent denominator-only estimate strong enough for the
   Ridout-style corollary;
3. blocks of distinct actual primitive pairs together with a bound for
   the union of their coefficient-prime supports satisfying the
   quantitative scale in (29); or
4. a synchronization lower bound for $\Delta g$, accompanied by the
   necessary support control for the other primitive coordinate.

The Cartier product $\mathcal G_m$ is valuable common content and is
already used in the rigorous mixed-cubic height.  Theorems 5.1--5.3 show
why that fact, by itself, cannot be reinterpreted as any of the four
missing statements.  They do not rule out proving one of them from new
identities specific to the actual period residues.

## 7. Replay

Run

```bash
python scripts/mixed_cubic_padic_support_matching_obstruction_certificate.py
sha256sum -c results/mixed_cubic_padic_support_matching_obstruction_hashes.sha256
```

The deterministic checker verifies the pinned dependency hashes, the
matching/gcd/outside-product identities on an exact table of mixed-cubic
indices, the fresh-prime construction, the support-forcing inequality,
and basic TeX delimiter/tag consistency.  The finite table is a replay of
the algebra, not evidence extrapolated to the actual period forms.
