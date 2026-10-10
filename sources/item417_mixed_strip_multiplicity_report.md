> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 417 — multiplicity audit of the marked-selector Cartier strip

Date: 2026-09-01  
Status: **CANONICAL, ROOT-AUDITED, ZERO ASYMPTOTIC DELTA**

## 1. Capacity-first verdict

Retain the exact Item-390/415 residue integers



$$
\lambda_{0,m}=[y^{4m}]
 \frac{(1-y)^{6m}(1+y)}{(1+y^2)^{4m+1}},
 \qquad
 \lambda_{1,m}=[y^{4m+1}]
 \frac{(1-y)^{6m}(1+y)^4}{(1+y^2)^{4m+2}}.          \tag{1.1}
$$



Canonical Item 200 already proves that its squarefree first-Cartier product



$$
F_m=\prod_{p\in\mathcal P_m}p=G_m                         \tag{1.2}
$$



divides both integers.  Canonical Item 415 combines (1.2) with Item 390 and
first obtained the normalized strictly-large component ceiling



$$
C_{415}=\frac{\log136-\mathfrak C_F}{6}
 =0.4292678962895477202317242499\ldots,                 \tag{1.3}
$$



where



$$
\mathfrak C_F=-4\log2+\frac{\pi}{\sqrt3}+3\log3.
$$



Canonical Item 418 subsequently sharpened only the analytic base, from
$136$ to



$$
\rho_*=135.5974839008548212502\ldots,
 \qquad
 C_{418}=\frac{\log\rho_* -\mathfrak C_F}{6}
 =0.4287738853386578689\ldots .                         \tag{1.3a}
$$



This item asks whether the same characteristic-
$p$ mechanism supplies either another uniform copy of $F_m$, or an
additional positive-rate squarefree strip.

The answer is decisive within that scope.

> **PROVED — no uniform multiplicity upgrade.**  The actual row
> $(m,p)=(2,11)$ has
> 

$$
>  (\lambda_{0,2},\lambda_{1,2})=(2475,6952),
>  \qquad
>  v_{11}(\lambda_{0,2})=v_{11}(\lambda_{1,2})=1.       \tag{1.4}
>
$$


> Thus $F_m^2\mid\gcd(\lambda_{0,m},\lambda_{1,m})$ is false as an
> all-$m$ theorem.  The rank-one-overlap row $(m,p)=(9,13)$ also has
> exact common valuation one, so adjoining Item 149's proportionality does
> not repair this failure.

> **PROVED — the entire degree-forced Cartier-zero tower adds only a thin
> squarefree factor.**  Let $E_m$ be the de-overlapped product of odd
> primes not in $F_m$ for which each row has a zero Cartier image at
> some prime-power level (the two levels need not be equal).  Then
> 

$$
>                    \boxed{F_mE_m\mid\lambda_{0,m},\lambda_{1,m}.} \tag{1.5}
>
$$


> Every prime in $E_m$ is at most $\sqrt{6m}$, and therefore
> 

$$
>                         \boxed{\log E_m=o(m).}          \tag{1.6}
>
$$



> **PROVED SCOPED NO-GO — levels cannot be counted as digits.**  Once a
> Cartier iterate is zero, every later iterate is zero.  Several
> prime-power degree certificates therefore give nested copies of the same
> characteristic-$p$ congruence, not independent congruences modulo
> $p^2,p^3,\ldots$.  In the actual extra-tower row $(m,p)=(5,5)$, the
> level $q=25$ is rank zero while $q=5$ is not, yet
> 

$$
>  v_5(\lambda_{0,5})=v_5(\lambda_{1,5})=1.             \tag{1.7}
>
$$


> Thus even a genuinely new higher-level zero need not supply a second
> digit.

Consequently the extra tower normalization improves finite carriers but has
zero linear exponent.  The current Item-418 component ceiling (1.3a), the
booked rate, the global content ceiling, and the frozen deficit all remain
unchanged.  This closes the pure degree-zero Cartier-tower multiplicity
shortcut; it does not rule out a new integral/Witt lift.

## 2. The all-level squarefree tower

Put



$$
N=6m,\qquad K_0=4m+1,\qquad K_1=4m+2.
$$



For every positive prime power $q$, retain Item 200's defect



$$
d_q(N,K)=
 \begin{cases}
  2r,&K\equiv0\pmod q,\\
  2r+3(q-t),&K\equiv t\pmod q,\quad1\le t<q,
 \end{cases}                                             \tag{2.1}
$$



where $r\equiv N\pmod q$ and $0\le r<q$.  Define



$$
\mathcal T_m=
 \left\{p\text{ odd prime}:\begin{array}{l}
  \text{for each }s\in\{0,1\}\text{ there is an }e_s\ge1,\\
  q_s=p^{e_s}\le6m,\quad d_{q_s}(N,K_s)\le q_s-2
 \end{array}\right\}.                                  \tag{2.2}
$$



The restriction $q\le6m$ loses nothing.  If $q>6m$, then
$r=N$, while $t=K_s$ for both rows, and



$$
\begin{aligned}
 d_q(N,K_0)&=2(6m)+3(q-4m-1)=3q-3>q-2,\\
 d_q(N,K_1)&=2(6m)+3(q-4m-2)=3q-6>q-2.
 \end{aligned}                                      \tag{2.3}
$$



The second inequality uses $q>2$, automatic for the odd prime powers in
$\mathcal T_m$.

The level $e=1$ in (2.2) is exactly canonical Item 200's set
$\mathcal P_m$.  Put



$$
\mathcal E_m=\mathcal T_m\setminus\mathcal P_m,
 \qquad
 E_m=\prod_{p\in\mathcal E_m}p.                       \tag{2.4}
$$



Thus (2.4) removes every factor already present in $F_m$ before assigning
any new label.

## 3. Proof of the tower divisor

Let



$$
\omega_s=\frac{u^N}{Q^{K_s}}\,dx,
 \qquad u=x(1-x),\quad Q=(1+x)(1+x^2).
$$



Fix $s$ and its witness $q_s=p^{e_s}$ from (2.2).  In
characteristic $p$, write



$$
\omega_s=F_s(x)^{q_s}P_s(x)\,dx,                     \tag{3.1}
$$



using the usual quotient/remainder decomposition of $N$ and $K_s$
by $q_s$.  Exactly as in Items 149 and 200,



$$
\deg P_s=d_{q_s}(N,K_s).      \tag{3.2}
$$



The $e_s$-fold Cartier operator selects exponents congruent to
$q_s-1$ modulo $q_s$.  If (3.2) is at most $q_s-2$, there is no
eligible exponent, so



$$
\mathcal C^{e_s}(\bar\omega_s)
 =F_s\mathcal C^{e_s}(P_s\,dx)=0.                     \tag{3.3}
$$



Cartier preserves each simple residue up to Frobenius.  In particular, a
zero image in (3.3) forces the simple residue at $-1$, and hence the log
coordinate $L_s$, to vanish modulo $p$.  The exact integers in (1.1)
are



$$
\lambda_{0,m}=2^{2m}L_0,
 \qquad
 \lambda_{1,m}=2^{2m+2}L_1.                           \tag{3.4}
$$



Since $p$ is odd, the dyadic factors in (3.4) are units.  Therefore



$$
p\mid\lambda_{0,m},\lambda_{1,m}\qquad(p\in\mathcal T_m). \tag{3.5}
$$



Multiplying (3.5) over the distinct primes, and using the disjoint
definition (2.4), proves (1.5).  The same product also divides Item 415's
integral marked representatives because they are integral linear
combinations of the two $\lambda$'s.

This theorem is squarefree.  It does not attach one copy of $p$ to each
witnessing exponent $e$.

## 4. Capacity of the de-overlapped factor

If $p\in\mathcal E_m$, the two first-level conditions do not both hold.
Thus at least one of the two row witnesses has $e_s\ge2$.  From
$p^{e_s}\le6m$,



$$
p\le\sqrt{6m}.            \tag{4.1}
$$



The elementary estimate obtained by bounding the number and size of these
distinct primes gives



$$
0\le\log E_m
 \le\sqrt{6m}\log\sqrt{6m}
 =O(\sqrt m\log m)=o(m).                               \tag{4.2}
$$



Set



$$
\nu_{s,m}=\frac{\lambda_{s,m}}{F_mE_m}\in\mathbb Z.  \tag{4.3}
$$



Every target prime in Item 390 is larger than $6m$, so division by
$F_mE_m$ preserves its full valuation.  The exact all-depth carrier may
therefore be written with the $\nu_s$'s.  Its finite height bound becomes



$$
c_m^><\frac{21\rho_*^m}{F_mE_m},                       \tag{4.4}
$$



but (4.2) and Item 200's
$\log F_m=\mathfrak C_Fm+o(m)$ give only



$$
\limsup\frac{\log c_m^>}{6m}
 \le\frac{\log\rho_*-\mathfrak C_F}{6}.             \tag{4.5}
$$



Equation (4.5) is exactly Item 418's ceiling, not a new decrease.  In the
requested de-overlapped ledger,



$$
\boxed{
 \Delta C_{>}=0,\quad
 \Delta r_{\rm booked}=0,\quad
 \Delta C_{\rm global}=0,\quad
 \Delta(T-r_1)=0.}                                     \tag{4.6}
$$



## 5. Why the tower does not prove multiplicity

There are two separate obstructions.

First, Cartier iteration is nested:



$$
\mathcal C^{e_0}(\bar\omega_s)=0
 \quad\Longrightarrow\quad
 \mathcal C^e(\bar\omega_s)=0\quad(e\ge e_0).          \tag{5.1}
$$



Thus several degree tests may certify several true statements of the form
"this later iterate is zero," but after the first zero those statements
carry no new residue information.  They remain characteristic-
$p$ statements and cannot be reinterpreted as congruences modulo
$p^e$.

Second, the failure occurs in the actual family, not merely in an ambient
coordinate model.  The following exact rows suffice:



$$
\begin{array}{c|c|c|c|c|c}
 m&p&\text{qualifying levels}&p\in\mathcal P_m
 &v_p(\lambda_0)&v_p(\lambda_1)\\ \hline
 2&11&11&\text{yes}&1&1\\
 9&13&13&\text{yes}&1&1\\
 5&5&25&\text{no}&1&1
\end{array}                                             \tag{5.2}
$$



For the last row the defects are



$$
(d_5(N,K_0),d_5(N,K_1))=(12,9),
 \qquad
 (d_{25}(N,K_0),d_{25}(N,K_1))=(22,19).                \tag{5.3}
$$



Thus the first level is not rank zero, the second level is rank zero, and
the common valuation is nevertheless exactly one.  This is an exact
counterexample to the rule "a level $p^e$ supplies $e$ copies of
$p$."

The row $(9,13)$ also lies in Item 149's rank-one support: its top layer
is $q=13$, $p<2m$, and both defects satisfy the weaker
$2q-2$ threshold.  Hence first-level rank zero plus the rank-one
determinant theorem still does not raise the common multiplicity of the
two log-residue coordinates.

These counterexamples rule out uniform upgrades.  They do not say that
higher valuations never occur, nor do they prove an upper bound on their
weighted mass.

## 6. Admission decision and remaining live lemma

The pure degree-zero tower fails the admission threshold for a main Route-1
mechanism:

1. after removing $F_m$, its new support is at most $\sqrt{6m}$;
2. its raw logarithmic capacity is $o(m)$;
3. repeated levels are nested and cannot be booked as extra digits; and
4. actual exact-one rows refute a uniform multiplicity conclusion.

It should therefore be closed as a Closer branch.  Any future multiplicity
attack must introduce genuinely integral information—for example a
modulo-$p^2$ endpoint formula, a Witt/Dwork error term, or an aggregate
valuation theorem.  Merely evaluating $d_{p^e}$ at more levels cannot
improve the positive-linear ledger.

The smallest live large-carrier target remains



$$
\log\left(
 \gcd(|\lambda_{0,m}/F_m|,|\lambda_{1,m}/F_m|)_{p>6m}
 \right)=o(m),                                         \tag{6.1}
$$



equivalently with $F_mE_m$ in place of $F_m$.  The two formulations
have the same exponential rate by (4.2).

## 7. Strict claim ledger

### PROVED

* The squarefree all-level Cartier-zero divisor (1.5).
* Exact de-overlap from canonical $F_m$.
* The support and zero-rate bound (4.1)--(4.2).
* The nested-iterate no-go (5.1).
* Actual exact-one counterexamples (5.2), including a genuine higher-level
  extra factor.
* Zero change to every asymptotic and central ledger quantity.

### EXACT FINITE ONLY

The replay checks $1\le m\le160$.  It finds 4,787 ordinary
$F_m$-prime incidences and 359 de-overlapped extra tower incidences; 265
of the latter have exact common valuation one.  These counts check
normalization only and are not used to prove (1.5) or (1.6).

### OPEN

* Any positive-linear weighted higher-multiplicity theorem from integral
  rather than characteristic-$p$ data.
* Arithmetic common factors not forced by a degree-zero Cartier image.
* The weighted zero-density target (6.1).
* Route-1 completion and the irrationality of $e+\pi$.

### NOT CLAIMED

* Completeness among all possible common factors of the residue pair.
* One digit per qualifying prime-power level.
* A new booked divisor, a global ceiling subtraction, or an irrationality
  proof.

## 8. Replay

Run

```text
python scripts/item417_mixed_strip_multiplicity_certificate.py \
  --output results/item417_mixed_strip_multiplicity_certificate_replay.json \
  --replay results/item417_mixed_strip_multiplicity_certificate.json
```

The standard-library replay pins canonical Items 149, 200, 390, 415, and
418;
reconstructs (1.1) exactly; enumerates every prime-power level in (2.2);
verifies $F_mE_m$-divisibility and the support cutoff through
$m=160$; and reproduces the three exact counterexamples.  It contains no
external numeric backend, random sampling, timestamp, or host-dependent
field.
