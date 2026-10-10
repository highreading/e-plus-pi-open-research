> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 163: exact sequential matching mass audit

Date: 2026-08-29

## 1. Verdict

For the item-140 mixed-cubic/beta data, write



$$
c_m=\gcd(U_m,V_m),\qquad b_m=|V_m|/c_m,
$$





$$
\Delta_{m,N}=\gcd(b_m,q_N),\qquad
g_{m,N}=\gcd(P^*_{m,N},\Delta_{m,N}).
$$



The audit gives four conclusions.

1. **PROVED FINITE.** Every one of the 15,150 parity-compatible candidates
   with $1\le m\le100$ and $1\le N\le6m$ was replayed.  The stored
   maximizer, all factors $c_m,\Delta_{m,N},g_{m,N}$, and the exact local
   sequential valuation law agree.  The canonical exact ledger has SHA-256
   `9ef61a6d4ebea6652466edd7208ddc43748acbf84a7afb3d4aa6007cbb013f35`.
2. **PROVED GENERAL.** If $N_m=o(m/\log m)$, then
   $\log(\Delta_{m,N_m}g_{m,N_m})/(6m)\to0$.  Thus bounded or recycled
   beta indices can never give theorem-scale matching mass.
3. **PROVED SCOPED NO-GO.** There is a deterministic clearing reservoir of
   rate at most $1/2$ per $6m$.  A single-copy booking of that entire
   reservoir, together with the proved rank-one rate, gives at most
   

$$
0.1365141682948128\ldots+0.5
   =0.6365141682948128\ldots,
$$


   still $0.5196329836694318\ldots$ below the target.  More importantly,
   even granting the most optimistic primewise doubling through both
   $\Delta$ and $g$, the ceiling is
   

$$
0.1365141682948128\ldots+1
   =1.1365141682948128\ldots,
$$


   which remains $0.0196329836694318\ldots$ below the target
   $1.1561471519642446\ldots$.  Hence this built-in clearing reservoir
   cannot close the route by itself, even with full matching doubling.
4. **EXPERIMENTAL.** In the saddle-compatible scans, the actual matching
   increment decreases from a mean $0.0284700\ldots$ per $6m$ for
   $81\le m\le100$ to $0.0176456\ldots$ on
   $m=105,110,\ldots,200$.  This is far below theorem scale, but it is not
   an asymptotic upper bound.

No lower-bound mechanism of the required exponential size was found.  The
remaining problem is an exact correlation problem between the moving
primitive coefficient $b_m$ and the Bessel zero classes of $q_N$, plus
the transverse condition defining $g$.

## 2. Exact primewise decomposition

For a prime $p$, put



$$
\kappa_p=\min\{v_p(U_m),v_p(V_m)\}=v_p(c_m),
\qquad
\beta_p=v_p(V_m)-\kappa_p=v_p(b_m),
$$





$$
t_p=v_p(q_N),\qquad d_p=v_p(\Delta_{m,N}).
$$



Then, exactly,



$$
d_p=\min\{\beta_p,t_p\},
$$



and



$$
\gamma_p:=v_p(g_{m,N})=
\begin{cases}
\min\{\beta_p,v_p(P^*_{m,N})\},&\beta_p=t_p>0,\\
0,&\text{otherwise}.
\end{cases}
$$



Therefore



$$
v_p(c_m\Delta_{m,N}g_{m,N})=\kappa_p+d_p+\gamma_p. \tag{2.1}
$$



The replay verifies (2.1) for both distinguished stored candidates at every
$m$: the unrestricted content maximizer and the minimum positive match.
It also verifies for every one of the 15,150 candidates that



$$
\boxed{\Delta_{m,N}g_{m,N}\mid q_N^2},\qquad
\boxed{c_m\Delta_{m,N}g_{m,N}\mid |V_m|q_N}. \tag{2.2}
$$



All $c_m$ in the finite scope factor completely over primes $p\le6m$.
That is an exact finite fact, not an all-$m$ support theorem.

As an example, at the saddle-compatible maximizer $(m,N)=(100,141)$,



$$
\Delta=3{,}060{,}971=31\cdot293\cdot337,
\qquad g=31.
$$



The three shared primes have equal positive valuations
$v_p(b)=v_p(q_N)=1$, but only $p=31$ passes the final transverse
congruence and enters $g$.  Thus the matching contribution is



$$
\frac{\log(\Delta g)}{600}=0.0306137165805662\ldots,
$$



while the full rate including $c_{100}$ is
$0.2578948093990459\ldots$.

## 3. A deterministic clearing reservoir

Let



$$
K_m=\frac{M_{4m+1}}{\prod_{2m<p<3m}p},
$$



let $G_m$ be the frozen Cartier divisor, and use the exact coordinate



$$
V_m=\frac{K_m\widehat B_m}{G_m},\qquad \widehat B_m\in\mathbb Z.
$$



Define



$$
K_m^{(0)}=\frac{K_m}{\gcd(K_m,G_m)},
\qquad
D_m=\frac{K_m^{(0)}}{\gcd(K_m^{(0)},c_m)}. \tag{3.1}
$$



Primewise valuation immediately proves



$$
\boxed{K_m^{(0)}\mid V_m,\qquad D_m\mid b_m.} \tag{3.2}
$$



There is also an exact recovery identity useful for matching:



$$
\boxed{\gcd(K_m^{(0)},c_mq_N)\mid c_m\Delta_{m,N}.} \tag{3.3}
$$



Indeed, if $k\le\kappa_p+\beta_p$ is the local exponent of
$K_m^{(0)}$, then



$$
\min(k,\kappa_p+t_p)
\le \kappa_p+\min(\beta_p,t_p).
$$



Thus (3.1) is a genuine positive-mass reservoir distributed across $c$
and the primitive coefficient $b$, and (3.3) states exactly how $q_N$
would have to recover its residual part.  The deterministic divisor
$D_m\mid b$ has positive rate in the finite replay, but no positive
asymptotic lower bound for that rate is proved.
The prime number theorem and the archived Cartier-product rate give



$$
\frac{\log K_m}{6m}\longrightarrow\frac12,
$$



and, with


$$
\mathfrak C=-4\log2+\pi/\sqrt3+3\log3
=2.3370475079987657\ldots
$$

,



$$
\liminf\frac{\log K_m^{(0)}}{6m}
\ge\frac{3-\mathfrak C}{6}
=0.1104920820002057\ldots. \tag{3.4}
$$



Equation (3.4) does not give matching mass: after division by $c_m$, the
remaining divisor $D_m$ still has to meet $q_N$.  Conversely the full
reservoir has rate at most $1/2$.

The full sequential product contains both $\Delta$ and $g$, so its most
optimistic reservoir accounting must allow doubling.  This still gives a
rigorous scoped no-go.  Fix $p$, let



$$
k_p=v_p(K_m^{(0)}),\qquad \kappa_p=v_p(c_m),
\qquad r_p=\max\{k_p-\kappa_p,0\}.
$$



At most $\min(k_p,\kappa_p)$ reservoir digits have already entered
$c_m$.  Only the remaining $r_p$ digits can be recovered from $b_m$
by $\Delta$, and $g\mid\Delta$ can contribute at most one further copy
of those same digits.  Hence the total exponent traceable to this reservoir,
including its part already in $c_m$, is at most



$$
\min(k_p,\kappa_p)+2r_p\le2k_p. \tag{3.5}
$$



Summing (3.5) gives an optimistic doubled reservoir rate at most $1$ per
$6m$.  Adding the rank-one radical rate separately, even though this may
overcount overlap and therefore only enlarges the ceiling, gives



$$
r_1+1
=1.1365141682948128\ldots
<1.1561471519642446\ldots. \tag{3.6}
$$



The residual gap is



$$
0.0196329836694318\ldots. \tag{3.7}
$$



Equations (3.5)--(3.7) bound only a certificate whose booked sources are the
rank-one radical and factors traceable to $K_m^{(0)}$.  They are not an
upper bound on the actual $c_m\Delta_{m,N}g_{m,N}$, which can contain
arithmetic mass from other sources.

For $81\le m\le100$, the unrestricted-window finite means were



$$
\begin{array}{c|c}
\text{quantity}&\text{mean rate per }6m\\ \hline
K_m^{(0)}&0.4626258610508912\\
D_m\mid b_m&0.3398082625277489\\
\gcd(K_m^{(0)},c_mq_N)\text{ at the maximizer}&0.1389485878741525
\end{array}
$$



so most of this visible reservoir was not recovered by the selected
$q_N$.  These three numbers are finite diagnostics only; (3.2)--(3.4)
are the theorem-level statements.

## 4. A general subcritical-index no-go

The beta denominators satisfy



$$
q_0=q_1=1,\qquad q_N=(4N-2)q_{N-1}+q_{N-2}.
$$



They are positive and increasing, so for $N\ge2$,



$$
q_N<4Nq_{N-1}<4^{N-1}N!\le(4N)^N.
$$



Combining this with (2.2) gives



$$
\boxed{
\frac{\log(\Delta_{m,N}g_{m,N})}{6m}
\le \frac{N\log(4N)}{3m}.} \tag{4.1}
$$



Consequently every choice $N_m=o(m/\log m)$ has zero matching rate.
In particular, each fixed index that recurs as a finite maximizer is
asymptotically irrelevant.  A positive matching rate necessarily requires
the saddle scale $N_m=\Omega(m/\log m)$, consistent with the analytic
condition



$$
\frac{N_m\log N_m}{6m}\longrightarrow\frac d2.
$$



This is only a necessary scale condition.  At that scale (4.1) no longer
excludes positive rate.

## 5. Exact finite census

### 5.1 Unrestricted window $N\le6m$

The exact replay found

- 15,150 candidates;
- 10,190 with $\Delta>1$;
- only 234 with $g>1$;
- only 18 of the 100 stored content maximizers with $g>1$;
- largest final content anywhere: $g=1133$ at
  $(m,N,\Delta)=(91,455,12463)$.

The dominant maximizing indices are strongly recycled:



$$
\begin{array}{c|rrrrrrrr}
N&41&312&138&37&121&4&234&59\\ \hline
\#\text{ rows}&19&13&12&10&8&7&6&5.
\end{array}
$$



For example, $N=41$ repeatedly contributes



$$
\Delta=157\cdot283\cdot373=16{,}572{,}763.
$$



This is a fixed integer and hence has zero rate as $m\to\infty$, exactly
as (4.1) predicts.

Block means for the unrestricted content maximizer are



$$
\begin{array}{c|ccc}
m&\log c/(6m)&\log(\Delta g)/(6m)&\log(c\Delta g)/(6m)\\ \hline
1\text{--}20&0.4087043&0.1480359&0.5567402\\
21\text{--}40&0.2456064&0.0717475&0.3173539\\
41\text{--}60&0.2179168&0.0497977&0.2677145\\
61\text{--}80&0.2022969&0.0394349&0.2417319\\
81\text{--}100&0.1845734&0.0320235&0.2165968
\end{array}
$$



These maximizers are generally not analytically usable: only 13 of 100,
and only 5 of the last 20, lie in and equal the corresponding
20%-wide saddle-window maximizer.

### 5.2 Saddle-compatible window

The pinned saddle scans give the applicable finite comparison:



$$
\begin{array}{c|ccccc}
\text{sample}&\log c&\log\Delta&\log g&\log(\Delta g)&\log(c\Delta g)\\
&\multicolumn{5}{c}{\text{mean per }6m}\\ \hline
m=81,\ldots,100
&0.1845734&0.0264237&0.0020463&0.0284700&0.2130434\\
m=105,110,\ldots,200
&0.1746552&0.0171328&0.0005128&0.0176456&0.1923007
\end{array}
$$



The largest actual total rates in these samples are respectively
$0.2578948093990459\ldots$ and
$0.2132678726196217\ldots$.  Even replacing the actual $g$ by its full
equal-valuation ceiling gives maxima only
$0.2770619019646617\ldots$ and
$0.2340098764305308\ldots$.

### 5.3 What the primitive coefficient does and does not suggest

At $m=10,20,30,40,50,60,80,100$, the pinned primitive-coefficient probe
finds almost every odd prime $p\le6m$ in $b_m$; the missing lists are



$$
\{41\},\varnothing,\{19,67\},\varnothing,\varnothing,
\varnothing,\{353\},\{577\}.
$$



The small-prime part has observed rate about $0.90$ to $1.01$, so the
coefficient contains a theorem-scale *candidate reservoir*.  But after all
primes $p\le6m$ are removed, a large cofactor remains at every selected
index, with observed rate $1.088$ to $1.155$.

Neither fact supplies synchronization.  A prime contributes to $\Delta$
only when the moving beta index lands on a root class of $q_N$, and it
contributes to $g$ only at equal valuation plus one further transverse
congruence.  The finite data therefore isolate a correlation problem, not a
shortage of primes in $b_m$.

## 6. The structural obstruction at saddle scale

On ordinary Bessel root branches, the archived transverse matching theorem
puts indices with prescribed local $\Delta g$ data into at most



$$
\prod_{p\mid\Delta}R_p
$$



parity-compatible residue classes modulo



$$
2\Delta g,
$$



where $R_p\le2p^{2/3}$ is the number of base roots modulo $p$.  If
$\log(\Delta g)/(6m)\to\kappa>0$, this modulus is exponential in $m$,
whereas the saddle index is only of order $m/\log m$.  Thus a successful
ordinary-branch lower bound must prove that the *actual moving CRT class* has
an exponentially small positive representative.  CRT itself supplies no
such theorem.

The singular alternative is not easier.  Positive mass from distinct
first-level singular roots, potentially synchronized with the transverse
$g$-condition, is logically possible and remains open.  Repeated deeper
lifts at a fixed singular prime additionally face the all-lift/Wieferich
obstruction and excess prime-power valuations.  The finite replay saw
$g>1$ in only 234 of 15,150 candidates, but that rarity cannot be promoted
to an asymptotic theorem.

This gives the present dichotomy.

- **OPEN, ordinary branch:** prove exceptional small representatives for
  actual moving coefficient classes, with positive total logarithmic mass.
- **OPEN, singular branch:** prove abundance and synchronization of distinct
  first-level singular roots; separately, control deeper all-lifts and
  excess valuations if higher powers are needed.
- **OPEN, alternative:** obtain the missing mass from deeper internal
  Cartier digits or a different construction.

## 7. Reproduction and hashes

Run

```text
python work/item163_match_audit/sequential_matching_primewise_audit.py --output work/item163_match_audit/sequential_matching_primewise_audit_m100_N6m.json

python work/item163_match_audit/sequential_matching_context_audit.py --output work/item163_match_audit/sequential_matching_context_audit.json
```

The scripts pin all Desktop inputs and do not modify the research archive.
The companion SHA-256 manifest records the staged scripts, results, and this
report.  This item proves no irrationality or rationality statement about
$e+\pi$.
