> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 353 — exact chosen-prime first digit and the maximal-degree Fermat-correction obstruction for fixed $j=1$

Date: 2026-09-01

## 1. Outcome and capacity first

Keep the actual family



$$
n=2h,\qquad r=2s+1,\qquad p=2n+3r,\qquad 2M=3n+4r,       \tag{1.1}
$$



and the selected coefficient



$$
a_{r,n}=[u^n]G(u)^{-r},\qquad
G(u)=1-4u+6u^2-4u^3.                                    \tag{1.2}
$$



The proved logical direction remains



$$
\boxed{
\text{ordinary fixed-}j=1\text{ collision}
\Longrightarrow p\mid a_{r,n}.}                         \tag{1.3}
$$



The converse is never used.

Item 342 constructed an exact four-coordinate Kummer lift



$$
\mathcal T_{p,r,n}\in\mathbb Z[\zeta_{p-1}]              \tag{1.4}
$$



such that, at one chosen prime $\mathfrak p\mid p$,



$$
\mathcal T_{p,r,n}\equiv a_{r,n}\pmod{\mathfrak p}.       \tag{1.5}
$$



Item 345 proved that $p$ splits completely and that ordinary
Galois descent does not control this chosen coordinate.  Items 348 and
351 then showed that the selected Hasse condition is one equation and
does not automatically force a companion.

This item computes the next chosen-prime digit exactly.  Because the
completion at $\mathfrak p$ is $\mathbb Q_p$, the Teichmüller lift
of the canonical residue $0\leq a<p$ satisfies



$$
\boxed{
[a]\equiv a+p\,\delta_p(a)\pmod{p^2},\qquad
\delta_p(a)={a^p-a\over p}\pmod p.}                      \tag{1.6}
$$



After absorbing all four Teichmüller scalar weights into their
summands, there are explicit residues $y_{\nu,x}\in\mathbb F_p$ such
that



$$
\boxed{
\mathcal T_{p,r,n}=\sum_{\nu,x}[y_{\nu,x}].}              \tag{1.7}
$$



Let $\langle y\rangle\in\{0,\ldots,p-1\}$ be the canonical integer
representative, and let



$$
\alpha=\sum_{\nu,x}\langle y_{\nu,x}\rangle,\qquad
\bar a=\alpha\bmod p,\quad 0\leq\bar a<p.                \tag{1.8}
$$



Then



$$
\boxed{
{\mathcal T_{p,r,n}-\bar a\over p}
\equiv
{\alpha-\bar a\over p}
+\sum_{\nu,x}\delta_p(\langle y_{\nu,x}\rangle)
\pmod p.}                                                \tag{1.9}
$$



Thus the first quotient digit is exactly



$$
\boxed{\text{ordinary carry}+\text{Fermat correction}.}  \tag{1.10}
$$



If the selected Hasse value vanishes, then $\bar a=0$, but neither
term on the right of (1.9) is forced to vanish.

The predeclared selected-zero row



$$
(h,s,p)=(8,2,47)                                         \tag{1.11}
$$



has four zeroth coordinate digits



$$
(41,31,13,9),\qquad41+31+13+9=2p,                        \tag{1.12}
$$



and



$$
{\mathcal T_{47,5,16}\over47}\equiv37\ne0\pmod{47}.      \tag{1.13}
$$



Hence this actual selected zero has



$$
v_{\mathfrak p}(\mathcal T_{47,5,16})=1.                 \tag{1.14}
$$



The predeclared $p=13$ selected-zero row also has valuation exactly
one.  Therefore



$$
\boxed{
H(1)=0\text{ does not force }v_{\mathfrak p}(\mathcal T)\geq2.}       \tag{1.15}
$$



There is a second global obstruction.  Regard $\delta_p$ as a
function $\mathbb F_p\to\mathbb F_p$.  Its unique polynomial
interpolant of degree at most $p-1$ has



$$
\boxed{
\deg\Delta_p=p-1,\qquad
[X^{p-1}]\Delta_p={p-1\over2}\ne0.}                      \tag{1.16}
$$



Thus a direct polynomial-phase treatment of the universal first
correction for the canonical integer residue section has linearly
growing degree; it is not a bounded-conductor replacement for the four
original Kummer coordinates in that presentation.  This statement
does not rule out a special rational compression, a special
Gauss-sum factorization, or cancellation after composition with the
four actual functions.

The construction reaches all actual rows, so its raw possible reach is
the entire retained fixed-$j=1$ ceiling $1/36$ per $6M$.
Nevertheless, (1.9) is a next-digit identity, not a nonconcentration
theorem for the zeroth digit.  Moreover the ordinary collision gate is
only modulo $p$, not modulo $p^2$.  Therefore



$$
\boxed{
\text{new forced condition}=0,\quad
\text{new linear log rate}=0,\quad
\text{new fixed-}j=1\text{ capacity reduction}=0.}       \tag{1.17}
$$



Booking is $0$, the $1/36$ ceiling is retained, and Route 1 remains
ACTIVE.

## 2. The chosen split prime and the Teichmüller digit

Let



$$
K_p=\mathbb Q(\zeta_{p-1}).                              \tag{2.1}
$$



Since $p\equiv1\pmod{p-1}$, $p$ splits completely in $K_p$.
Choose the same prime $\mathfrak p\mid p$ as Item 342.  Then



$$
(K_p)_{\mathfrak p}\cong\mathbb Q_p,\qquad
\mathcal O_{K_p,\mathfrak p}\cong\mathbb Z_p.            \tag{2.2}
$$



Under this identification, the chosen reduction of the full-order
character is the identity on $\mathbb F_p^\times$, and $[a]$ is the
unique $(p-1)$-st root of unity congruent to $a\pmod p$.

The other primes above $p$ correspond to the other Galois powers of
the full-order character.  Formula (1.9) concerns only the chosen
identity coordinate.  The ordinary collision supplies no congruence at
those other split coordinates, and no trace or norm over them is inserted
here.  This preserves the Item 345 descent obstruction.

Modulo $p^2$, one may take



$$
[a]\equiv a^p\pmod{p^2}.                                \tag{2.3}
$$



Indeed $a^p\equiv a\pmod p$, and Fermat's theorem gives



$$
(a^p)^{p-1}=(a^{p-1})^p\equiv1\pmod{p^2}.               \tag{2.4}
$$



Subtracting $a$ from (2.3) proves (1.6).  For $a\ne0$,



$$
\delta_p(a)=a\,q_p(a),\qquad
q_p(a)={a^{p-1}-1\over p}\pmod p,                        \tag{2.5}
$$



while $\delta_p(0)=0$.

This derivation is intrinsic to the chosen split prime and needs no
unjustified Gross–Koblitz invocation.

## 3. Absorbing the four Kummer weights

Put



$$
E=p-r.                                                   \tag{3.1}
$$



For $x\in\mathbb F_p^\times$, Item 342 uses



$$
\begin{aligned}
R_0(x)&=x^{-n}G(x)^E,\\
R_1(x)&=x^{-n}(\vartheta G)(x)G(x)^{E-1},\\
R_{2a}(x)&=x^{-n}(\vartheta^2G)(x)G(x)^{E-1},\\
R_{2b}(x)&=x^{-n}(\vartheta G)(x)^2G(x)^{E-2},
\end{aligned}                                            \tag{3.2}
$$



where $\vartheta=u\,d/du$.  Its exact lift is



$$
\begin{aligned}
\mathcal T=-[1/2]\bigl(&[E]\mathcal K(R_{2a})
+[E(E-1)]\mathcal K(R_{2b})\\
&+[(3-2n)E]\mathcal K(R_1)
+[(n-1)(n-2)]\mathcal K(R_0)\bigr).                     \tag{3.3}
\end{aligned}
$$



Teichmüller lifts are multiplicative.  Define in $\mathbb F_p$



$$
\begin{aligned}
b_0&=-{(n-1)(n-2)\over2},\\
b_1&=-{(3-2n)E\over2},\\
b_{2a}&=-{E\over2},\\
b_{2b}&=-{E(E-1)\over2},
\end{aligned}                                            \tag{3.4}
$$



and



$$
y_{\nu,x}=b_\nu R_\nu(x).                                \tag{3.5}
$$



At a zero of $R_\nu$, both sides are defined to be zero.  Otherwise,



$$
[b_\nu][R_\nu(x)]=[b_\nu R_\nu(x)].                      \tag{3.6}
$$



Distributing (3.3) therefore proves the exact identity (1.7).
No Galois trace, norm, or unselected split coordinate is introduced.

## 4. Carry plus Fermat correction

Apply (1.6) termwise to (1.7):



$$
\mathcal T
\equiv
\sum_{\nu,x}\langle y_{\nu,x}\rangle
+p\sum_{\nu,x}\delta_p(\langle y_{\nu,x}\rangle)
\pmod{p^2}.                                               \tag{4.1}
$$



Writing $\alpha=\bar a+pC$, where $\bar a$ is the least residue,
gives



$$
\mathcal T\equiv
\bar a+p\left(C+\sum_{\nu,x}\delta_p(\langle y_{\nu,x}\rangle)\right)
\pmod{p^2}.                                               \tag{4.2}
$$



This proves (1.9).

There is also a useful four-coordinate form.  For each $\nu$, write



$$
\mathcal T_\nu
=\sum_x[y_{\nu,x}]
\equiv t_{\nu,0}+p\,t_{\nu,1}\pmod{p^2},
\qquad0\leq t_{\nu,0}<p.                                 \tag{4.3}
$$



If



$$
\bar a=\sum_\nu t_{\nu,0}\bmod p,                        \tag{4.4}
$$



then



$$
{\mathcal T-\bar a\over p}
\equiv
{\sum_\nu t_{\nu,0}-\bar a\over p}
+\sum_\nu t_{\nu,1}
\pmod p.                                                  \tag{4.5}
$$



Thus even after each coordinate is lifted separately, a new
cross-coordinate carry remains.  The selected equation controls only
(4.4); it does not control either summand of (4.5).

## 5. The maximal-degree correction theorem

Let $\Delta_p(X)\in\mathbb F_p[X]$ be the unique polynomial of degree
at most $p-1$ representing $\delta_p$ on $\mathbb F_p$.
For any function $f:\mathbb F_p\to\mathbb F_p$, its interpolation
polynomial is



$$
P_f(X)=\sum_{a\in\mathbb F_p}
f(a)\bigl(1-(X-a)^{p-1}\bigr).                           \tag{5.1}
$$



The coefficient of $X^{p-1}$ is therefore



$$
[X^{p-1}]P_f=-\sum_{a\in\mathbb F_p}f(a).                \tag{5.2}
$$



For $f=\delta_p$,



$$
\sum_{a\in\mathbb F_p}\delta_p(a)
\equiv
{1\over p}
\left(\sum_{a=1}^{p-1}a^p-\sum_{a=1}^{p-1}a\right)
\pmod p.                                                  \tag{5.3}
$$



Pair $a$ with $p-a$.  Since $p$ is odd,



$$
(p-a)^p\equiv-a^p\pmod{p^2},                             \tag{5.4}
$$



so



$$
\sum_{a=1}^{p-1}a^p\equiv0\pmod{p^2}.                   \tag{5.5}
$$



Also



$$
\sum_{a=1}^{p-1}a={p(p-1)\over2}.                        \tag{5.6}
$$



Equations (5.2)--(5.6) yield



$$
\sum_a\delta_p(a)\equiv-{p-1\over2}\pmod p,\qquad
[X^{p-1}]\Delta_p={p-1\over2}\ne0.                       \tag{5.7}
$$



This proves (1.16) for every odd prime, not merely for the declared
controls.

### Scope of the degree obstruction

The theorem closes the following direct route:

> Using the canonical integer residue section, replace every first
> Teichmüller correction by a uniformly
> bounded-degree polynomial phase and apply a fixed-conductor
> character-sum estimate.

The universal correction already has degree $p-1$, so this route has
linearly growing polynomial complexity before composition with
$R_0,R_1,R_{2a},R_{2b}$.

The theorem does **not** prove that $\delta_p(R_\nu(x))$ has minimal
degree $p-1$ as a function of $x$, nor that no low-degree rational
description, special factorization, or cancellation exists for the
particular four-coordinate sum.  Those would be new actual-family
theorems.  Changing the residue section can also move complexity between
the correction term and the carry; only their total in (4.2) is
intrinsic.

## 6. Why Gross–Koblitz or Stickelberger is not yet a conclusion

Gross–Koblitz evaluates Gauss sums after an additive character and a
Gauss-sum decomposition have been specified.  The four objects in
(3.2)--(3.3) are general multiplicative Kummer sums of rational
functions, and Items 342--351 do not provide a bounded-length
Gauss/Jacobi factorization of their chosen linear combination.

One can introduce additive Fourier expansion, but that is a new
decomposition with moving frequency support.  Stickelberger valuations
of individual Gauss factors would then still have to survive:

1. recombination of those factors;
2. the four-coordinate linear combination;
3. the cross-coordinate carry in (4.5); and
4. specialization to the tied parameters (1.1).

No theorem proving those compatibilities is currently available.
Accordingly this item uses only the direct Teichmüller expansion, which
is exact and sufficient to expose the obstruction.  It does not claim
that a future specialized Gross–Koblitz argument is impossible.

## 7. Declared exact controls

The certificate reuses only the five rows predeclared in Item 342.
The coordinate order is



$$
(R_0,R_1,R_{2a},R_{2b}).                                 \tag{7.1}
$$



| $(h,s,p)$ | coordinate residue digits $t_{\nu,0}$ | coordinate quotient digits $t_{\nu,1}$ | target residue | cross carry | total quotient digit |
|---|---|---|---:|---:|---:|
| $(1,1,13)$ | $(0,2,0,11)$ | $(0,2,1,3)$ | $0$ | $1$ | $7$ |
| $(2,1,17)$ | $(9,12,2,2)$ | $(8,2,12,10)$ | $8$ | $1$ | $16$ |
| $(8,2,47)$ | $(41,31,13,9)$ | $(9,34,36,3)$ | $0$ | $2$ | $37$ |
| $(4,4,43)$ | $(19,24,31,14)$ | $(9,39,33,38)$ | $2$ | $2$ | $35$ |
| $(2,6,47)$ | $(10,37,30,6)$ | $(43,31,41,15)$ | $36$ | $1$ | $37$ |

For the two selected-zero controls,



$$
\mathcal T\equiv91=13\cdot7\pmod{13^2},                 \tag{7.2}
$$



and



$$
\mathcal T\equiv1739=47\cdot37\pmod{47^2}.              \tag{7.3}
$$



They prove only that the selected zero does not universally imply a
second digit.  Neither row is asserted to be a full original collision.

The certificate also evaluates the field function $\delta_p$ at all
residues for the four already declared primes



$$
p=13,17,43,47                                            \tag{7.4}
$$



and verifies degree $p-1$ and leading coefficient $(p-1)/2$.
This is an exact field-function replay, not a scan over primes and not
density evidence.

## 8. Capacity admission

The exact transform exists on every actual fixed-$j=1$ row.  Its raw
support therefore has mass



$$
{M\over6}+o(M),                                          \tag{8.1}
$$



large enough in principle to affect the ledger.  The admission failure
is not thin support.

It fails at the implication and arithmetic stages:

1. the ordinary collision gives only the zeroth condition
   $\mathcal T\in\mathfrak p$;
2. the quotient digit in (1.9) is not forced to vanish;
3. the $p=13$ and $p=47$ controls show it can be a unit;
4. a theorem that the quotient digit is always a unit would describe
   simple selected zeros, not exclude ordinary selected zeros;
5. the universal correction has maximal moving polynomial degree; and
6. no weighted nonconcentration theorem for the zeroth digit is proved.

Consequently the exact first-digit theorem has raw capacity but no
admissible booked capacity.  An eventual positive result would need one
of:

- chosen-prime nonconcentration for the *zeroth* sum;
- an additional $p^2$ gate genuinely forced by the full collision;
- a special bounded-complexity factorization of the actual composed
  correction; or
- a weighted valuation theorem that directly excludes the original
  collision set.

## 9. Strict decision

### PROVED

- the chosen split-prime identification with $\mathbb Z_p$;
- the Teichmüller expansion (1.6);
- absorption of all four scalar weights into the exact residues
  $y_{\nu,x}$;
- the global and four-coordinate carry-plus-Fermat formulas;
- the exact maximal interpolation degree $p-1$;
- the scoped bounded-degree polynomial-phase/conductor no-go;
- selected-factor vanishing does not formally force a second valuation
  digit;
- zero booking.

### EXACT FINITE ONLY

- five predeclared Kummer-coordinate digit controls;
- four exact field-function interpolation controls;
- the two valuation-one selected zeros;
- no prime scan, density extrapolation, or full-collision claim.

### OPEN

- chosen-prime nonconcentration of the zeroth Kummer combination;
- special cancellation after composition with the four actual
  functions;
- rational compression or a justified bounded-length
  Gross–Koblitz/Jacobi factorization;
- any extra $p^2$ gate forced by full-collision information;
- $W_b(M)=o(M)$, any fixed-$j=1$ ceiling reduction,
  Route 1, and every conclusion about $e+\pi$.

## 10. Ledger and self-audit



$$
\begin{array}{c|c}
\text{quantity}&\text{Item 353 value}\\ \hline
\text{actual rows reached}&\text{all}\\
\text{new forced independent condition}&0\\
\text{new proved linear log rate}&0\\
\text{new fixed-}j=1\text{ capacity reduction}&0\\
\text{retained fixed-}j=1\text{ ceiling per }6M&1/36
\end{array}                                               \tag{10.1}
$$



The self-audit records explicitly:

1. (1.3) is used only in its proved direction;
2. selected-factor zeros are not called full collisions;
3. a modulo-$p^2$ theorem is not credited toward the ordinary
   modulo-$p$ gate;
4. maximal polynomial degree is not promoted to a theorem against every
   rational or special composed representation;
5. the section-dependent carry/correction split is not called an
   invariant conductor theorem;
6. no Gross–Koblitz factorization is asserted without constructing it;
7. finite controls carry no density weight.
