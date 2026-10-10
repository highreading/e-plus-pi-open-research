> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 327 — moving dyadic witnesses and all-degree projective collapse of the beta transducer

Checked: 2026-09-01 (Beijing time)

## 1. Strict verdict and admission audit

Retain



$$
q_0=q_1=1,
\qquad
q_n=(4n-2)q_{n-1}+q_{n-2}\quad(n\ge2),
\tag{1.1}
$$



and, for $n\ge5$, put



$$
A=4n-2,
\qquad
B=A-4=4n-6,
\qquad
a=q_{n-1},\quad b=q_n,\quad c=q_{n-2},\quad d=q_{n-3},
\qquad m=n-2.
\tag{1.2}
$$



Item 316 proves that an actual centered half-bound failure is equivalent
to a canonical word with



$$
\frac{a}{2c}\le R<\frac a2,
\qquad
0<|E|<c,
\qquad
U=(-1)^n\operatorname{sgn}(E)a.
\tag{1.3}
$$



Item 323 supplies, for every canonical word, the exact all-depth suffix
transducer



$$
L_j=RH_j-bN_j,
\qquad
s_j=\frac{L_j}{b},
\qquad
-1<s_j<1.
\tag{1.4}
$$



This item first audits two candidate mechanisms before crediting them.

* A dyadic target congruence with $2^s=O(n)$ is genuinely forced by
  (1.3), but its entire raw logarithmic mass is only
  $s\log2=O(\log n)=o(n)$.  It fails the positive-linear-mass
  admission threshold even under perfect use.
* An odd-modulus nonlinear invariant of the whole residual vector may use
  the full modulus $b$, so it is not thin and passes the raw-capacity
  screen.  However, the exact transducer makes every residue-state vector
  projectively rank one.  Arbitrarily many depths and arbitrarily high
  homogeneous degree add no new condition.

Both conclusions are global and exact.

> **PROVED — UNIFORM MOVING-DYADIC INFORMATION-CLASS NO-GO.**
> For every $n\ge6$ and every integer $s\ge1$ satisfying
>
> 

$$
> \boxed{2^s\le2n-3,}
> \tag{1.5}
>
$$


>
> there is an explicit canonical word satisfying the exact continued-
> fraction data, the intermediate window, the correct positive-target
> sign, $0<|E|<c$, the complete universal Item-323 transducer, and
>
> 

$$
> \boxed{U\equiv a\pmod{2^s},}
> \tag{1.6}
>
$$


>
> while $U\ne a$.  Thus even a precision growing like $\log_2 n$
> bits does not imply the exact target.

This strictly strengthens the declared fixed-precision scope of Item 316:
the quantifiers in (1.5) allow $s=s(n)$ to grow.  It does not treat
$2^s>2n-3$, full dyadic equality, or a congruence coupled to new odd
arithmetic.

> **PROVED — ALL-DEGREE PROJECTIVE-COLLAPSE THEOREM.**
> Let a canonical $0<R<a$ word have $\gcd(R,b)=1$, as every
> hypothetical actual target does.  For every divisor $D\mid b$, every
> collection of depths, and every homogeneous integer polynomial $F$ of
> arbitrary degree $e$ whose coefficients are independent of the digit
> word,
>
> 

$$
> \boxed{F(L_0,\ldots,L_m)
> \equiv R^eF(H_0,\ldots,H_m)\pmod D.}
> \tag{1.7}
>
$$


>
> Hence
>
> 

$$
> D\mid F(L_0,\ldots,L_m)
> \iff
> D\mid F(H_0,\ldots,H_m).
> \tag{1.8}
>
$$


>
> In particular, every minor, Pluecker coordinate, cross-ratio, norm, or
> other projectively homogeneous vanishing test on the residual tower is
> independent of the digit word and of the half-window target.

For a general, not necessarily homogeneous polynomial, decomposition into
homogeneous pieces reduces the whole tower to the one scalar $R$.
Under an actual target that scalar already satisfies



$$
R\equiv\epsilon a^2\pmod D,
\qquad
\epsilon=\operatorname{sgn}(a^2-\kappa b).
\tag{1.9}
$$



Thus the multi-depth residue tower by itself has no algebraic codimension beyond the
original signed square ray.  This is a scoped no-go for nonlinear
**projective residue tests**.  It does not cover the divided quotients
after removing $b$, congruences modulo $b^2$, integer-size estimates,
or canonical redigitization of a complement.

Neither theorem excludes (1.3).  Neither theorem reduces beta capacity or
changes the Route-1 ledger.  Booking is zero.

## 2. Actual-family implication and sign audit

Let



$$
r_{\rm act}=a^2-\kappa b,
\qquad
R_{\rm act}=|r_{\rm act}|,
\qquad
\epsilon=\operatorname{sgn}(r_{\rm act}).
\tag{2.1}
$$



Adjacent beta denominators are coprime, so



$$
\gcd(R_{\rm act},b)=\gcd(a^2,b)=1.
\tag{2.2}
$$



If the open half-bound failed, then $R=R_{\rm act}<a/2<a$, so its
canonical Ostrowski word and the Item-323 transducer are defined without
any reduction or invented state.  Item 316 gives



$$
E=(-1)^n\epsilon\kappa,
\qquad
U=\epsilon a.
\tag{2.3}
$$



Consequently every target implies, for every $s\ge1$,



$$
U\equiv\epsilon a\pmod{2^s}.
\tag{2.4}
$$



It also implies (1.9) for every $D\mid b$, since



$$
\epsilon R=a^2-\kappa b\equiv a^2\pmod D.
\tag{2.5}
$$



Thus both candidate invariants are genuinely inherited from the original
actual target.  No auxiliary period, modified seed, or ambient polynomial
state is substituted for it.

The witnesses in Section 3 are deliberately information-class
countermodels, not actual centered-square rows.  They prove that the
listed truncated data do not imply equality.  They are never promoted to
counterexamples to the half-bound.  The projective theorem in Sections
4-6 is conditional on the actual-target coprimality (2.2) whenever a unit
is inverted.

## 3. Uniform logarithmically growing dyadic witnesses

Fix $n\ge6$, and let $s\ge1$ satisfy (1.5).  Put



$$
M=2^{s-1}.
\tag{3.1}
$$



The integer interval



$$
I_n=\left\{\frac B2+1,\frac B2+2,\ldots,B\right\}
\tag{3.2}
$$



has exactly



$$
|I_n|=\frac B2=2n-3\ge2M
\tag{3.3}
$$



consecutive elements.  Since



$$
\frac A2=2n-1
\tag{3.4}
$$



is odd, the congruence



$$
\frac A2\kappa_*
\equiv\frac{a-1}{2}\pmod M
\tag{3.5}
$$



has one residue class modulo $M$.  Every residue class occurs at least
twice in $I_n$ by (3.3).  At most one integer can satisfy



$$
A\kappa_*+1=a.
\tag{3.6}
$$



Choose a solution of (3.5) in $I_n$ which does not satisfy (3.6), and
put



$$
g=B-\kappa_*.
\tag{3.7}
$$



Then



$$
0\le g\le\frac B2-1.
\tag{3.8}
$$



Use the two-top-digit word



$$
\delta_{m-1}=1,
\qquad
\delta_m=g,
\qquad
\delta_j=0\quad(j\ne m-1,m).
\tag{3.9}
$$



It is canonical: $1<w_{m-1}=B-4$, while $g<B=w_m$, so no maximal
digit and no Markov carry occurs.  Direct continuant evaluation gives



$$
\boxed{
R_*=gc+d,
\qquad
E_*=(-1)^n(B-g)=(-1)^n\kappa_*,
\qquad
U_*=A\kappa_*+1.}
\tag{3.10}
$$



All inequalities are uniform.  Since $n\ge6$,



$$
d>\frac B2+\frac12>\frac{a}{2c},
\tag{3.11}
$$



where the second inequality follows from
$a/c=B+d/c<B+1$.  The first holds at $n=6$, where
$d=71>19/2$, and propagates because the beta recurrence increases
$q_{n-3}$ by more than $2$ when $n$ increases by one.  Also, using
(3.8) and $d<c$,



$$
R_*=gc+d
\le\left(\frac B2-1\right)c+d
<\frac{Bc+d}{2}=\frac a2.
\tag{3.12}
$$



Furthermore,



$$
0<\kappa_*\le B<c,
\tag{3.13}
$$



and



$$
(-1)^n\operatorname{sgn}(E_*)=1.
\tag{3.14}
$$



Thus the witness lies in the positive-target branch of every inequality
and sign condition in Item 316.

Multiplying (3.5) by $2$ yields



$$
A\kappa_*\equiv a-1\pmod{2M},
\tag{3.15}
$$



so (3.10) gives



$$
\boxed{U_*\equiv a\pmod{2^s}.}
\tag{3.16}
$$



But the choice excluding (3.6) gives



$$
\boxed{U_*\ne a.}
\tag{3.17}
$$



Finally, Item 323 applies to every canonical word, so the witness has its
complete suffix-load transducer in the strict unit strip at every depth.
The construction does not merely preserve a bounded prefix of that state.

The quantifier is genuinely moving: one may take, for example,



$$
s(n)=\left\lfloor\log_2(2n-3)\right\rfloor.
\tag{3.18}
$$



This proves the claimed growing-precision information-class no-go.

There are two deliberate scope boundaries.  First, the constructed word
need not satisfy the independent odd condition $\gcd(R_*,b)=1$; an
argument coupling the dyadic target to new odd arithmetic is not covered.
Second, (3.3) gives no witness guarantee once $2^s>2n-3$.  Neither
boundary is silently promoted.

## 4. Exact projective rank one at every depth

Retain Item 323's suffix data



$$
H_m=1,
\qquad H_{m+1}=0,
\qquad
N_m=N_{m+1}=0,
\tag{4.1}
$$





$$
H_{j-1}=w_{j+1}H_j+H_{j+1},
\qquad
N_{j-1}=w_{j+1}N_j+N_{j+1}+\delta_{j+1},
\tag{4.2}
$$



and



$$
L_j=RH_j-bN_j.
\tag{4.3}
$$



Because $L_m=R$, equation (4.3) has the exact normalized form



$$
\boxed{L_j-H_jL_m=-bN_j\qquad(0\le j\le m).}
\tag{4.4}
$$



More symmetrically, every two-depth minor has the exact lift



$$
\boxed{
H_iL_j-H_jL_i
=-b\bigl(H_iN_j-H_jN_i\bigr)
\qquad(0\le i,j\le m).}
\tag{4.5}
$$



Let $D\mid b$.  Reducing (4.4) gives



$$
L_j\equiv H_jL_m\equiv RH_j\pmod D.
\tag{4.6}
$$



If $\gcd(R,D)=1$, then $L_m$ is a unit and



$$
\boxed{L_jL_m^{-1}\equiv H_j\pmod D.}
\tag{4.7}
$$



Since $H_m=1$, both vectors are nonzero.  Over every field
$\mathbb F_p$ with $p\mid D$,



$$
\boxed{[L_0:\cdots:L_m]=[H_0:\cdots:H_m].}
\tag{4.8}
$$



This is exact projective equality, not merely a bound on the rank.
Adding more depths can never enlarge its projective span.

Under an actual target, (2.2) supplies $\gcd(R,D)=1$ for every
$D\mid b$, so no extra unit assumption has been inserted into the
actual-family conclusion.

## 5. Arbitrary-degree polynomial collapse

Let



$$
F\in\mathbb Z[X_0,\ldots,X_m]
\tag{5.1}
$$



be homogeneous of any degree $e\ge0$.  Its coefficients may depend on
$n$, the selected depths, and the fixed suffix continuants, but not on
the digit word or the suffix loads; neither its degree nor the number of
variables is assumed bounded.  Substitution of (4.6) gives



$$
F(L_0,\ldots,L_m)
\equiv F(RH_0,\ldots,RH_m)
=R^eF(H_0,\ldots,H_m)\pmod D.
\tag{5.2}
$$



When $R$ is a unit modulo $D$, multiplication by $R^e$ preserves
vanishing.  This proves (1.7)-(1.8).

The conclusion includes, without separate cases:

* every pairwise and higher determinantal test;
* every Pluecker or Grassmann coordinate formed from repeated depth
  vectors;
* every homogeneous norm form;
* every projective rational invariant whose displayed denominator is a
  unit; and
* every portfolio whose number of depths or homogeneous degree grows with
  $n$.

For a general polynomial, write its exact homogeneous decomposition



$$
F=\sum_{e=0}^{E}F_e.
\tag{5.3}
$$



Then



$$
\boxed{
F(L_0,\ldots,L_m)
\equiv
\sum_{e=0}^{E}R^eF_e(H_0,\ldots,H_m)
\pmod D.}
\tag{5.4}
$$



Thus every polynomial residue test on the entire tower reduces to one
scalar.  If the original actual target is imposed, (1.9) further gives



$$
F(L)
\equiv
\sum_{e=0}^{E}(\epsilon a^2)^eF_e(H)
\pmod D.
\tag{5.5}
$$



No digit coordinate remains.  An inhomogeneous test may still use the
one-dimensional signed scalar ray; this is exactly original square-residue
information, not a new transverse multi-depth condition.  The theorem
does not claim that every scalar congruence is useless.

## 6. A universal non-target comparator and the exact no-go scope

The projective blindness has an exact comparator at every $n\ge5$.
Take



$$
R_0=1,
\qquad
\delta_1=1,
\qquad
\delta_j=0\quad(j\ge2).
\tag{6.1}
$$



This is canonical and coprime to every $b$.  All suffix loads vanish,
so



$$
\boxed{L_j^{(0)}=H_j\quad(0\le j\le m).}
\tag{6.2}
$$



On the other hand,



$$
R_0=1<\frac{a}{2c},
\tag{6.3}
$$



because $a/c=B+d/c>B\ge14$.  It is therefore outside the actual
intermediate target window.  Nevertheless it has exactly the same
projective residual point (4.8) as every hypothetical target.

Consequently no digit-independent projectively homogeneous congruence test on the residual
tower, even at all depths and unbounded degree, can distinguish the
target window from this explicit non-target state.  This proves the
scoped nonlinear information-class no-go.

Equations (4.4)-(4.5) also show exactly where information can re-enter.
Dividing a minor by $b$ exposes



$$
H_iN_j-H_jN_i,
\tag{6.4}
$$



and reducing modulo $b^2$ can see the same quotient.  Integer magnitude
estimates can use $|L_j|<b$, and canonical redigitization can replace
the state itself.  These mechanisms are outside the projective residue
class and remain open.

## 7. Capacity and proper-target audit

The moving dyadic construction has



$$
s\log2\le\log(2n-3)=o(n).
\tag{7.1}
$$



Thus even if every available dyadic digit were converted into a gcd or
valuation gain, its logarithmic mass would be sublinear.  It cannot change
a positive linear Route-1 deficit.  This is a raw-capacity failure, not a
claim that the congruence is false or uninteresting.

For the projective theorem, $D$ may be the full $b$, so thin support is
not the reason for closure.  The reason is exact algebraic rank one:
the full tower supplies no condition independent of $R$, and its
projective part supplies none at all.

For a proper de-overlapped target $Q\mid b$, equations (4.4)-(5.5)
remain valid with $D=Q$, provided $R$ is a unit modulo $Q$.  Under
an actual full target this follows from (2.2).  The result still does not
give a lower bound for the centered reduction modulo $Q$; it only closes
the declared projective-residue invariant class.

No common coefficient/product baseline from Item 282 is divided out,
rebooked, or counted.  No positive prime mass is obtained.

## 8. Strict labels

### PROVED

* The uniform moving-precision construction (3.1)-(3.17) for every
  $n\ge6$ and every $s$ with $2^s\le2n-3$.
* Its exact canonicality, intermediate window, sign, small dual error,
  all-depth universal transducer, target congruence, and failure of exact
  equality.
* The exact normalized and two-depth transducer lifts (4.4)-(4.5).
* Projective rank one modulo every $D\mid b$ when $R$ is a unit.
* The arbitrary-depth, arbitrary-degree homogeneous polynomial collapse
  (5.2), and the general homogeneous-piece reduction (5.4).
* Conditional on the actual target, the signed square specialization
  (5.5).
* The canonical non-target comparator $R_0=1$.

### PROVED SCOPED INFORMATION-CLASS NO-GO

* Exact CF/Ostrowski/window/sign data, the entire universal Item-323
  transducer, and a positive-target congruence modulo any moving
  $2^s\le2n-3$ do not imply exact target equality.
* Every digit-independent projectively homogeneous residue test on the
  all-depth residual tower collapses to the fixed suffix point and cannot
  distinguish the target window from $R_0=1$.
* Adding arbitrarily many depths or arbitrary homogeneous degree does not
  increase residue-state codimension.

### EXACT FINITE ONLY

* The deterministic replay's declared moving-precision rows, transducer
  minors, polynomial substitutions, and comparator rows.
* They replay the symbolic identities and are not promoted into an actual
  half-bound proof or counterexample search.

### OPEN

* The original all-digit exclusion (1.3) and the centered half-bound.
* Dyadic precision with $2^s>2n-3$, full dyadic equality, and any
  dyadic/odd coupling using actual coprimality.
* Divided transducer minors, suffix-load quotients, or congruences modulo
  $b^2$ and higher.
* Inhomogeneous scalar conditions that add genuinely new information about
  the centered representative $R$.
* Canonical redigitization of a complement and integer-size nonlinear
  invariants.
* Every proper-target lower bound, beta capacity reduction, Route 1, and
  every conclusion about $e+\pi$.

### BOOKING



$$
\boxed{
\text{new beta capacity reduction}=0,
\qquad
\text{new Route-1 rate}=0.}
\tag{8.1}
$$



No canonical, master, status, checkpoint, or research-log file is edited
by this work package.

## 9. Deterministic replay

From the archive root:

~~~text
python work/item327_beta_transducer_congruence_no_go_certificate.py ^
  --output work/item327_beta_transducer_congruence_no_go_certificate.replay.json
~~~

The checker uses only the Python standard library and exact integer
arithmetic.  It performs no half-bound scan and promotes no bounded row.
