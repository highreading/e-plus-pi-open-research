> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent cross-audit of the modulo-$p^2$ adversary package

Date: 2026-08-28

Audited without modifying either adversary file:

- `work/modp2_bounded_jet_and_sequential_mass_adversary.md`
- `work/modp2_bounded_jet_sequential_mass_check.py`

## Verdict

**PASS, with one presentation-only precision note.**  The bounded-jet
construction, three actual-coordinate counterexamples, exact sequential
$c_m\Delta_mg_m$ exponent formula, global divisor safeguard, and optimal
weighted threshold are correct.  The package is compatible with the builder's
new Hasse-band formula: that formula uses precision $p^{2+\delta}$ and a
number of Hasse coefficients growing with $K_s$, so it lies explicitly
outside the adversary theorem's fixed-precision/bounded-jet no-go.

## 1. Bounded-jet construction

Direct integration gives



$$
q\int_0^1x^{q-1}dx=1,
\quad
\int_0^1{dx\over4(1+x)}={\log2\over4},
\quad
\int_0^1{dx\over2(1+x^2)}={\pi\over8}.
$$



Thus the three displayed differentials have endpoint triples
$(1,0,0),(0,1,0),(0,0,1)$ exactly.  Their poles are simple and contained in
the separable divisor $Q=(1+x)(1+x^2)$, while the polynomial degree is
$q-1\le pq-2$.  Hence the top-layer lemma's structural hypotheses really
are satisfied.

For



$$
z_0=(1,1,1),\qquad z_1=(1+p^r,1,1+p^s),
$$



the minors are exactly



$$
L_1(qR_0)-L_0(qR_1)=-p^r,
\qquad
L_1E_0-L_0E_1=-p^s.
$$



Multiplication of the base triple by $p$ gives the rank-zero valuations
$(r+1,s+1)$, and division by one squarefree $G$-digit leaves $(r,s)$.
The fixed-precision comparison differs by the polynomial differential
$(p^J-p^{J+k})x^{q-1}dx$; its finite-pole principal parts agree integrally,
and every coefficient agrees modulo $p^J$, including at infinity.  The
determinant valuations are nevertheless $J$ and $J+k$.  The stated scope
of the limitation theorem is therefore exact.

## 2. Actual-coordinate rows

The checker pins and replays the frozen rows



$$
\begin{array}{c|c|c|c}
(m,p)&v_p(U_m)&v_p(V_m)&v_p(c_m)\\ \hline
(3,3)&1&3&1\\
(9,13)&1&2&1\\
(4,7)&1&2&1.
\end{array}
$$



An independent degree calculation also confirms that the first row has
$q_3=9$ but is not first-Cartier rank zero, while the second row is
first-Cartier rank zero.  The item-151 JSON independently records determinant
zero at $(4,7)$.  These examples refute precisely the three universal
$p^2$-lift claims listed in the note.

## 3. Sequential exponent formula

Write



$$
\kappa=\min(v_p(U),v_p(V)),\qquad
\beta=v_p(V)-\kappa,\qquad t=v_p(q_N).
$$



Then primitive reduction gives $v_p(b)=\beta$, and



$$
d=v_p(\Delta)=\min(\beta,t).
$$



If $0<t<\beta$, the normalized $q_0a$-term in $P^*$ is a unit; if
$0<\beta<t$, the normalized $b_0p_N$-term is a unit.  Therefore



$$
\gamma=v_p(g)=0\quad(\beta\ne t),
$$



while for $\beta=t=r>0$,



$$
\gamma=\min(r,v_p(P^*)).
$$



It follows exactly that



$$
v_p(c\Delta g)=\kappa+d+\gamma
\le v_p(V)+v_p(q_N).
$$



The global divisibility $c\Delta g\mid |V|q_N$ also follows immediately
from



$$
|V|=c\Delta b_0,\qquad q_N=\Delta q_0,qquad g\mid\Delta.
$$



Beyond the checker's exhaustive 2,401 exponent states, this audit
independently recomputed both archived selected matches for every
$1\le m\le100$: all 200 records reproduced their stored $(\Delta,g)$, and
all satisfied $c\Delta g\mid |V|q_N$.

## 4. Weighted threshold

Independent 80-digit decimal evaluation gives



$$
r_1={-4\log2+6\log3-3\over6}
=0.13651416829481281845042382261707465926382380158257928\ldots
$$



and



$$
h-d/2-r_1
=1.0196329836694317938803064012400587396329010690452963\ldots .
$$



The checker's certified endpoints differ by exactly $10^{-52}$, and both
enclose this value.  The optimization at $\theta=d/2$ follows from equality
of $h-\theta$ and $h-d+\theta$.  Thus the threshold in (5.6) is correct
as the sufficient remaining sequential weight within the frozen matching
criterion.

### Presentation-only correction

At audit time, the two rounded numbers printed in (5.7) differed by
$2\times10^{-52}$, although the checker output had the advertised width
$10^{-52}$.  The archived source now prints the checker's full endpoints.
This correction does not affect the enclosure, theorem, or quoted threshold.

## 5. Reproduction

The adversary checker returned `PASS` with:

- 12 arbitrary-valuation models;
- 6 fixed-precision indistinguishable models;
- 2,401 sequential exponent states;
- all 3 actual sharp counterexamples;
- the exact $(m,N,p)=(6,4,7)$ overlap.

Hashes at audit time:

```text
931650c54a498901d4a13f2784f876bf14c5ced32ea5440f39d836b6bc594bd9  modp2_bounded_jet_and_sequential_mass_adversary.md
dab6f60059aa532fb086814fc3ad5ce4e2513d88591dfc45216dee5894cbc65d  modp2_bounded_jet_sequential_mass_check.py
```
