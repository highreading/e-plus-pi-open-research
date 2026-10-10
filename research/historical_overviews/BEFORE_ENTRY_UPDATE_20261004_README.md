> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Archive status on October 3 2026

This research session is closed at the user's request. No researcher was restarted after the software update. The main mathematical problem remains unresolved. Read research-results navigation (historical reference; see the publication coverage notes) and the [current closeout overview](../withdrawn_route_materials/RESULTS_OVERVIEW.md) for the latest results, evidence versions, and unfinished work.

The original README below describes inherited research checkpoints. Its previous contents are preserved byte for byte in the closeout's previous_indexes directory. Historical ACTIVE wording does not authorize restarting this session.

# Research program: the arithmetic nature of e + pi

Started: 2026-08-26 UTC

## Objective

Determine rigorously whether $e+\pi$ is algebraic or transcendental. The user
requested a proof of algebraicity, but the research is allowed to conclude in the
opposite direction if a correct proof of transcendence is found.

No numerical coincidence, heuristic, unproved conjecture, or unchecked model
output will be represented as a proof.

## Current established baseline

1. $e$ is transcendental (Hermite, 1873).
2. $\pi$ is transcendental (Lindemann, 1882).
3. It is not presently known unconditionally whether $e+\pi$ is rational,
   irrational algebraic, or transcendental; in particular, even its
   irrationality is open.
4. At least one of $e+\pi$ and $e\pi$ is transcendental: if both were
   algebraic, then $e$ and $\pi$ would be roots of
   $X^2-(e+\pi)X+e\pi$, hence algebraic over the algebraic numbers, a
   contradiction.
5. Schanuel's conjecture implies that $e$ and $\pi$ are algebraically
   independent, hence implies that $e+\pi$ is transcendental. This is
   conditional and cannot be used as an unconditional proof.

## Status at the latest checkpoint

The current theorem DAG, de-overlapped mass ledger, and branch-admission rules
are summarized in `ROUTE1_MASTER_CAPACITY.md`.

No proof in either direction has been obtained. In particular, nothing in
this archive proves that $e+\pi$ is algebraic, irrational, or transcendental.
The requested assertion of algebraicity is opposed by every strong conjectural
framework examined: Schanuel's conjecture, the conjecture
$\mathbf E\cap\mathbf G=\overline{\mathbb Q}$, and the exponential period
conjecture all imply that $e+\pi$ is transcendental.

Latest resumption (through audited Item 269): no proof in either direction was
found. Route 1 now has exact rank-one, off-ray phase, higher-terminal, and
normalized common-log reductions.  The common $j=1$ residual is algebraic
and P-recursive; its Witt defect has a proved ten-level full phase module.
The corrected $j=2$ carry has been reduced to explicit harmonic states and
one canonical actual-family bulk residual.  Item 246 gives exact factor and
reciprocity recurrences for that residual and disproves universal individual
nonvanishing by the exact moving-prime zero $(p,s,\nu)=(37,4,0)$; simultaneous
vanishing of the two companion residuals remains open.  Item 247 eliminates
their common parity state, isolates the admissible singular line, and reduces
the remaining simultaneous condition to an explicit moving-prime gcd, without
proving that gcd is a unit.  Item 249 puts the singular line itself into one
fixed algebraic-hypergeometric recurrence: its surviving scalar is
$\Theta_{(p-2)/3}\bmod p$.  The exact excluded-boundary zero at $p=11$
shows that the recurrence permits genuine cancellation, while all-prime
nonvanishing on the admissible rows remains open.  Late-frozen Item 248 gives
exact local-tail and Wronskian formulas for the $j=1$ leading factors, but
also supplies exact split-root counterexamples to the simplest universal
Wronskian-unit strategy; joint all-row nonvanishing remains open.  Item 250
returns to the ordinary $j=2$, $p^2$ gate and proves an exact fixed-$r$
affine localization with the unique Frobenius residue retained.  A rank-one
identity gives determinant-free linear and cubic necessary eliminants, but
exact rows at $p=67,367,953$ show that those eliminants are not sufficient;
the actual residual period on their exceptional locus remains open.  Item 251
now determines that period exactly through one integer diagonal $A_s$, proves
its algebraic generating function and order-two telescoping recurrence, and
states the rank-aware second condition.  Exact zeros of both $A_s$ and its
hypergeometric increment rule out the first scalar shortcuts; the remaining
rowwise half-binomial prefix is still uncontrolled.  Item 252 proves the exact
Frobenius reduction to that single prefix and shows that any scalar rational
antidifference over $\overline{\mathbb F}_p$ needs reduced-denominator degree
at least $(p-1)/2$.  This blocks uniformly fixed-degree scalar Gosper
closure, but leaves phase-specific and higher-rank identities open.  Item 253
specializes the remaining prefix to the actual phase, gives an exact integer
diagonal and hypergeometric increment, and proves that terminal-increment zeros
for fixed $r$ divide the fixed integer $2r^2+21r+81$.  Exact witnesses
separate that terminal condition from prefix vanishing, and sixth-root values
have an explicit ambient kernel, so the incomplete prefix remains open.  Item
254 gives exact Mellin, Greene, incomplete-beta, fixed-cutoff, and punctured
genus-one forms, plus a rigorous numerator container whose positive ceiling is
too large to book.  Items 255--256 prove that reciprocal beta reflection is
rank one and remains rank two after adjoining the first squared-denominator
jet; its first Hasse digit is a moving harmonic interval with an exact
admissible zero.  Neither ordinary
simultaneous $p^2$ gate has been excluded for all primes or at zero weighted
rate, and none of these results adds the missing divisibility exponent. Route 2
remains queued under the user's route-order rule. These are rigorous reductions
and scoped obstructions, not a proof of irrationality. See
`active_checkpoint_20260828.md` and `ROUTE_STATUS.md` for the authoritative
current frontier.

Concrete progress in this archive consists of:

- a complete three-way reconciliation of the original archive: all 124 source
  notes, 104 Python programs, one C++ program, and 108 JSON certificates were
  covered; every Python file parsed, every JSON file parsed, and the C++ file
  passed a syntax check.  This audit found no proof that $e+\pi$ is
  irrational, algebraic, or transcendental;
- a denominator-free common-kernel identity.  For
  $f=a+(1+x^2)H'$ with $H\in\mathbb Z[x]$ and
  $A((1+x^2)H')=0$,
  $$
  \int_0^1 f(x)\left(e^x+\frac4{1+x^2}\right)\,dx
  =a(e+\pi)-B(f)+4(H(1)-H(0)).
  $$
  After correcting an unsaturated-nullspace search, the endpoint-zero lattice
  has exact useful image $8\mathbb Z\times2\mathbb Z$.  It yields certified
  finite forms as small as
  $5.12\ldots\times10^{-7}$, but its rank-two quotient has the ordinary
  Dirichlet/Minkowski capacity balance: determinant arguments alone reach
  linear-form exponent one, not a Roth-breaking exponent.  Exceptional vectors
  and uniform nonvanishing remain open;
- a full-norm no-go theorem for the fixed cyclotomic two-log unit edge and a
  compatible full-orbit multi-log obstruction.  Under the temporary
  algebraicity hypothesis, the full absolute norm grows exponentially; traces
  collapse or vanish; centered Galois matching forces a zero target, while
  asymmetric centered weights have an expanding conjugate and pure-monodromy
  targets have nonzero conjugate limits.  These results leave varying conductors,
  unequal degree allocations, and genuinely new multipoint Padé systems open;
- an unconditional counterexample to the conjectured fixed $19$-support of
  the $n=5$ two-log coordinate ideal.  At
  $(p,d)=(109321,6219)$, the prescribed first jet vanishes at an explicit
  prime ideal, and an independent characteristic-zero Smith calculation gives
  ideal norm exactly $109321$.  Thus neither support only over $19$ nor
  $361\in\mathfrak J_d$ holds in every degree;
- a Bessel block/resultant dichotomy.  Unit transition minors are blind to
  singleton prime powers, while the first invariant seeing every singleton is
  already at product scale.  The exact reflection
  $P_{2n+1}(-n-1)=(-1)^np_nq_n$ merely reproduces the full $q_n$-depth at
  primes dividing $q_n$.  The sharp sufficient remaining estimate is
  $\max v_p(q_n)\log p=o(N\log N)$ in the relevant smooth block; the exact
  lift $v_{11}(q_{1359})=5$ shows that the high singleton tail is genuine;
- a completed dyadic valuation theorem for the first odd quartic boundary
  coordinate,
  $v_2(S_m)=m+s_2(m)+v_2(m)+1$, after repairing and independently replaying
  two checker defects.  This does not control the remaining odd endpoint
  content;

- a rigorous denominator bound for the rationality hypothesis, obtained from
  1180 certified continued-fraction coefficients;
- an exact exclusion of a finite degree/height box of algebraic relations;
- a finite exact audit of endpoint-matched mixed Hermite--Padé systems;
- an independently audited all-degree $2$-adic rank theorem for the
  raw-arctangent endpoint-matched system;
- an independently audited all-degree $2$-adic rank theorem for the
  endpoint-matched Machin system
  $1,e^z,16\arctan(z/5)-4\arctan(z/239)$, including nonvanishing of its
  endpoint coefficient in every degree;
- a new rational-coefficient pullback
  $F(z)=4\arctan(z/(2-z))$ with $F(1)=\pi$, exact Taylor radius $\sqrt2$,
  and integral derivative jets in every order.  For its diagonal
  endpoint-matched high-jet matrix, an independently audited all-degree
  theorem proves that every maximal cofactor contains the explicit factor
  $\Xi_n$ with
  $\log\Xi_n=2n^2\log n+O(n^2)$; this separates forced determinant content
  from primitive height and sharpens the conditional kernel bound to
  $\log H\le(3/2)n^2\log n+O(n^2)$.  A fixed-prime exact certificate proves
  full rank, exact first-free order, and nonzero endpoint coordinates for
  every $2\le n\le100$, but the primitive endpoint values grow through the
  tested range (reaching the decade $10^{293}$ at $n=15$), so no decay
  theorem results;
- an independently audited polynomial reparametrization of that pullback,
  with
  $\phi(z)=z-z^3/6+5z^4/24-z^5/24$ and
  $G(z)=F(\phi(z))$.  The derivative jets of $\phi$, and hence those of
  $G$, are integers in every order.  An exact five-step Schur--Cohn
  certificate proves that every genuine pulled-back singularity lies beyond
  $\sqrt2$, so $\rho(G)>\sqrt2$; numerical roots place the nearest one at
  $1.4597454685\ldots$ only as a diagnostic.  This is a rigorous analytic
  improvement without a jet-denominator penalty, but all $15$ exact
  diagonal endpoint-matched forms grow, reaching the decade $10^{439}$;
- a stronger independently audited integral-Hurwitz composition
  $\phi_8(z)=z+(z^7-z^8)/140$.  Its only nonzero derivative jets are
  $1,36,-288$, it fixes $0$ and $1$, and an eight-step exact rational
  Schur--Cohn certificate proves
  $\rho(F\circ\phi_8)>3/2$.  The nearest singularity is numerically
  $1.5598556036\ldots$, explicitly as a diagnostic.  The diagonal
  endpoint form at $n=1$ is identically zero; every system through $n=15$
  otherwise has full row rank and a nonzero first-free coefficient, but
  the nonzero primitive endpoint decades
  $0,7,15,26,44,64,89,119,150,191,233,281,331,385$ again grow;
- a further independently audited sparse integral-Hurwitz polynomial
  composition
  

$$
\phi(z)=z+\frac{46z^7(1-z)}{7!}
  +\frac{213z^9(1-z)}{9!}
  -\frac{763z^{10}(1-z)}{10!}
  +\frac{20078z^{11}(1-z)}{11!}.
$$


  An exact twelve-step Schur--Cohn certificate proves
  $\rho(F\circ\phi)>1747/1000$.  The smallest computed preimage modulus,
  $1.7472752090\ldots$, is retained only as a diagnostic.  An independent
  implementation reproduces every Gaussian-rational Schur constant and
  gap, the exact unique pass in the neighboring $3^4$ lattice box, all
  derivative jets through order $46$, and all diagonal Hermite--Padé
  records through $n=15$.  Those primitive diagonal forms still grow,
  reaching the decade $10^{458}$;
- a nonpolynomial entire integral-Hurwitz pullback which improves the
  analytic radius almost to its first computed singularity.  It adds three
  terms of the form
  

$$
\frac{k}{m!}z^m(z-1)e^{\pm z}
$$


  to a sparse endpoint-fixed polynomial.  A closed all-order formula proves
  that every derivative jet of the resulting $\phi$ is integral, and the
  integral-jet recurrence for $F$ plus Faà di Bruno proves the same for
  $G=F\circ\phi$, with $G(1)=\pi$.  An exact degree-$65$
  Schur--Cohn--Rouché certificate, using a degree-$24$ exponential
  truncation and $256$-bit rational dyadic reflection bounds, proves
  

$$
\rho(G)>\frac{17679119}{10000000}=1.7679119.
$$


  All $65$ Schur gaps are strictly positive and the exact squared
  boundary-to-tail ratio is $67.6644544\ldots>1$.  The smallest computed
  root modulus $1.7679119968\ldots$ remains diagnostic.  A separate
  implementation independently audited the Schur orientation, recursive
  boundary product, tail bound, Rouché step, both conjugate targets, and
  all-order jet proof at the earlier radius; the strengthened certificate
  uses the same exact primitives and was separately rerun byte-identically.
  Exact diagonal endpoint forms through $n=15$ nevertheless grow to decade
  $10^{464}$;
- an exact non-diagonal audit of the $\phi_8$ pullback over all $1330$
  degree triples $a+b+c\le18$.  Every matrix has full row rank and nullity
  one; the global nonzero minimum is already
  

$$
0.082761394925<129-22(e+\pi)<0.082761394926
$$


  at $(a,b,c)=(0,5,0)$, and no total budget $6,\ldots,18$ improves it.
  The exact continuation of that edge through degree $250$ isolates an
  unresolved endpoint gcd.  In contrast, a general all-degree theorem
  proves that the constant-$B=C$ ray diverges like
  $\exp(\tfrac12a\log a-O(a))$ whenever the fixed $\pi$-function has
  exponentially bounded Taylor-truncation denominators; this includes
  every polynomial pullback studied here;
- an independently audited canonical factorial-digit construction.  With
  $d_n=\lfloor n!\pi\rfloor-n\lfloor(n-1)!\pi\rfloor$ and
  $G(z)=3+\sum_{n\ge2}d_nz^n/n!$, the function $G$ is entire, has integral
  derivative jets, and satisfies $G(1)=\pi$.  Every endpoint-matched
  Hermite--Padé system with constant $G$ coefficient and degree parameters
  $a\ge\max(1,b-1)$ reduces exactly, after full-triple primitivization and
  endpoint gcd removal, to
  $$
  L_{a,b}=\frac{\Delta^b(a!)(e+\pi)-\Delta^b C_a}
                 {\gcd(\Delta^b(a!),\Delta^b C_a)}
         =\frac{\Delta^b x_a}{H_{a,b}},
  $$
  where $C_a=\lfloor a!e\rfloor+\lfloor a!\pi\rfloor$ and
  $0<x_a=a!(e+\pi)-C_a<2$.  Hence
  $|L_{a,b}|<2^{b+1}/H_{a,b}$ in every degree, and any single zero forces
  $e+\pi\in\mathbb Q$.  A separate implementation reconstructed all
  $15{,}094$ cases with $a\le500,b\le30$; the unique minimum is
  $(a,b)=(346,3)$, with $H=2{,}875{,}602{,}586{,}336$ and
  $|L|=2.94268312399908\ldots\times10^{-14}$.  Its gcd is nevertheless
  far below the square-root scale required by Roth's theorem.  Fixed $b$
  and general varying-$b$ gcd growth therefore remain open;
- a completed all-degree analysis of the same factorial-digit forms when
  the difference order varies as far as $b=a+1$.  Writing
  $W=a!D$ and $Z=DC_a+K$, where $K$ is a positive combination of only the
  next $b$ canonical digits, the endpoint gcd factors exactly as
  $$
  H=gJ,\qquad g=(D,K),\qquad
  J=(a!,D'C_a+K').
  $$
  The local future-digit factor satisfies
  $\limsup\log g/\log W\le1/2$ uniformly, and has upper exponent
  $\lambda/(1+\lambda)$ when $b/a\to\lambda$.  Hence the elementary
  Roth route needs a positive power of $W$ from the residual past factor
  $J$, or a separate exceptional finite-difference estimate.  Canonical
  digit ranges alone provably cannot control $J$.  A byte-reproducible
  rational certificate checks all $71{,}019$ admissible pairs
  $a+b\le530$: every endpoint is nonzero, but none reaches even the
  square-root threshold.  This is finite evidence only.  The canonical
  integral-Hurwitz interpolant also has exponential type exactly $1$, the
  minimum possible in its coefficient class;
- an independent reconstruction of the full polynomial-$C$
  factorial-digit Hermite--Padé family.  For
  $A+Be^z+CG=O(z^{a+b+c+1})$ and $B(1)=C(1)$, normalization
  $B(1)=C(1)=1$ reduces all high jets to an explicit $(b+c)$-square
  integer matrix $\mathcal H$.  Whenever $D=\det\mathcal H\ne0$, the
  primitive endpoint is obtained from the exact adjugate formula
  $$
  W=a!D,\qquad Z=P_aD+w\operatorname{adj}(\mathcal H)y,\qquad
  L=\frac{W(e+\pi)-Z}{(W,Z)}.
  $$
  A Schur complement separates the known positive fixed-$b$ determinant
  from a genuinely digit-dependent $c$ by $c$ determinant.  All $1330$
  systems with $a+b+c\le18$ have full row rank and nullity one.  There
  are six singular high blocks, of which five have zero endpoint pair;
  the global nonzero minimum remains the $c=0$ form
  $3504(e+\pi)-20533$, while the best $c>0$ form is
  $12669120(e+\pi)-74239453$.  If $e+\pi$ were rational, eventual
  factorial digits would create polynomial syzygies of unbounded
  dimension, so a universal full-rank theorem would already prove the
  open irrationality statement;
- an all-degree solution of the first genuinely digit-dependent case
  $\deg C\le1$.  After removing the universal determinant factor
  $\kappa_b=\prod_{j<b}j!$, the high-block determinant is the primitive
  integer form
  $$
  F_{a,b}=\sum_{r=0}^b(-1)^rA_{a,b,r}v(a+1+r)
           =\sum_{s=0}^{b+1}(-1)^sB_{a,b,s}d_{a+s},
  $$
  where every $A_{a,b,r}$ and $B_{a,b,s}$ is positive and
  $\gcd_s B_{a,b,s}=1$.  The auxiliary cofactors are shifted-gamma
  moments with an explicit Jacobi continued fraction, and $F_{a,b}$
  obeys a first-order recurrence in $b$.  Nevertheless the elementary
  digit bounds $0\le d_n\le n-1$ permit both signs and determinant zeros
  at arbitrarily large locations; indeed the eventual digit pattern that
  would follow from rationality of $e+\pi$ forces $F_{a,b}=0$ for every
  $b\ge2$.  An independently certified scan of all $71{,}019$ pairs
  $a+b\le530$ finds only the initial zeros $(1,0),(1,1),(2,0)$ for the
  actual digits of $\pi$, but this finite observation does not prove
  eventual nonvanishing;
- an all-degree integral quotient for every polynomial degree $c\ge1$.
  The full $(b+c)$-square high block factors exactly as
  $$
  \det\mathcal H_{a,b,c}
  =(-1)^b\left(\prod_{j=0}^{b-1}j!\right)
    \det\widetilde Q_{a,b,c},
  $$
  where $\widetilde Q$ is only $c$ by $c$ and its rows are an explicit
  Poisson-moment functional followed by the forward differences of orders
  $b+1,\ldots,b+c-1$.  All entries are integers without hidden clearing.
  The same basis change gives
  $\operatorname{rank}\mathcal H=b+\operatorname{rank}\widetilde Q$ and an
  exact augmented-rank formula for the full nullity.  The specialization
  $c=1$ recovers the primitive determinant recurrence above.  Exact checks
  of all $1{,}140$ positive-$c$ triples through total degree $18$ find five
  singular high blocks but no rank-deficient full bordered matrix; this is
  a diagnostic, not a universal nonvanishing theorem;
- an independently audited universal analytic ceiling for this polynomial
  reparametrization strategy.  Schwarz--Pick on the twice-punctured plane,
  evaluated through the modular lambda covering, proves that every
  endpoint-fixing holomorphic map which avoids $1\pm i$ on $|z|<R$
  satisfies
  $R\le R_*<5.262410788162386$.  Here
  $R_*=\sqrt{(1+y)/(1-y)}$ and
  $y=\operatorname{Im}\!\left(iK((1-i)/2)/K((1+i)/2)\right)$.
  The quotient-distance minimization is exact, and an independent rational
  elliptic-series enclosure certifies the decimal bound.  The constant is
  sharp for unrestricted holomorphic maps, though not known to be
  approachable under integral-Hurwitz polynomial constraints;
- an independently audited softened-singularity subfamily built from the
  same pullback, with $C=D^n$, $D=z^2-2z+2$, a constant $A$, and a
  maximally cancelling polynomial $B$ of degree $b$.  Its endpoint is the
  exact integer form
  $L_{n,b}={!b}(e+\pi)-b!(1+H_{n,b})$.  The fully primitive forms diverge
  for every fixed $b\ge2$, every proportional ray $b/n\to\lambda$ with
  $0<\lambda<2$, every fixed critical offset $b=2n+d$, and the growing
  window
  $0\le b-2n\le(2-\delta)\sqrt{2n}/\log\sqrt{2n}$ for fixed
  $0<\delta<2$.  The critical asymptotic is
  $H_{n,2n+d}\sim(-1)^{d+1}(\sqrt\pi/2)
  e^{2\sqrt{2n}}(\sqrt{2n})^{-d-3/2}$.
  General approaches to $b/n=2$ outside that window and all
  threshold-and-beyond regimes still require a uniform upper bound for
  $\gcd({!b},b!(1+H_{n,b}))$;
- an independently audited higher-radius quadratic pullback family
  $F_p(z)=4\arctan((p-1)z/(p-z^2))$, with $F_p(1)=\pi$.
  Its singular radius is $\sqrt p$ for $p=2,3,4,5$ and is uniquely
  maximized at $\sqrt5$ by $p=5$ among integral $p\ge2$.  This analytic
  gain has an exact arithmetic cost: for odd prime $p$, the denominator
  of $F_p^{(2m+1)}(0)$ is
  $p^{2m+1-v_p((2m)!)}$; analogous exact formulas hold for $p=2,4$.
  All $32$ diagonal endpoint-matched systems with $p=2,3,4,5$ and
  $1\le n\le8$ have full row rank and nonzero first-free coefficients,
  but their fully reduced endpoint forms grow.  A separate reduced
  quadratic search tests $53{,}036$ exact candidates and finds no
  radius improvement among the $16{,}158$ candidates integral through
  jet order $25$; the final root-radius ranking is explicitly retained
  as a finite floating diagnostic, not a classification theorem;
- an independently audited all-degree obstruction for the constant
  $B=C=1$ ray in every quadratic pullback $F_p$: after clearing all
  polynomial coefficients and removing the entire endpoint gcd, the
  primitive form satisfies
  $|\mathcal L_{p,a}|\ge
  \exp(\tfrac12a\log a-O_p(a))$ and diverges.  The proof transfers the
  superexponential reduced denominator of the Taylor truncation of $e$
  through the merely exponential denominator of the $F_p$ truncation,
  then uses the finite irrationality measure of $\pi$ to rule out
  cancellation between their two analytic tails;
- an independently audited first-free-coefficient theorem for the diagonal
  endpoint-matched Machin family: on every positive degree
  $n\equiv0$ or $1\pmod4$ its Taylor remainder has exact order $3n+1$;
  the accompanying quantitative audit shows that current uniform
  algebraic-independence measures for the conditional pair
  $(ie,e^{i(e+\pi)})$ are vastly too weak to turn the nested exponential
  Padé forms into a contradiction;
- an independently audited exact signed-tail theorem for that Machin
  function, arbitrary-degree endpoint and height formulas, and a rigorous
  no-decay theorem for the non-diagonal ray $(a,b,c)=(N-1,1,1)$: its fully
  primitive forms diverge along $N=1+2\cdot239^k$, so the full odd-index
  ray cannot tend to zero;
- an independently audited refinement of that ray's exceptional
  $239$-adic arithmetic: the two leading-residue exceptions below $239^3$
  lose only one further $239$-adic digit, a much later exception behaves the
  same way, and an exact recurrence proves that at least one member of every
  adjacent odd-degree pair has endpoint denominator exponent
  $j-O(\log j)$; hence the primitive values have a quantitatively divergent
  member in every sufficiently large adjacent pair, although the pointwise
  bound at every odd degree remains open;
- an all-degree proof that the raw-arctangent endpoint coefficient
  $B_n(1)$ is nonzero, together with exact real-integral and contour formulas
  for its still-uncontrolled endpoint remainder;
- an independently audited exact Wronskian obstruction to a tempting
  endpoint shortcut: the full endpoint-constrained Machin coefficient
  space is not uniformly an extended Chebyshev space (already at $n=1$
  its basis-invariant full Wronskian changes sign on $[0,1]$), so endpoint
  nonvanishing cannot be obtained by asserting that whole-space property;
- an exact all-degree formula for the large $2$-adic valuation of the raw
  endpoint cofactor, together with a cofactor/gcd identity proving that this
  divisibility need not survive primitive endpoint normalization;
- an exact degree-65 counterexample to a tempting $239$-adic endpoint
  valuation pattern seen at low degrees;
- a quantitative no-go theorem for translating rational approximants to $e$
  into algebraic approximants to $\pi$: reduced height and the exact
  continued fraction of $e$ cap this entire strategy at approximation
  exponent $2+o(1)$, far short of known measures for $\pi$;
- a factorial-recurrence block theorem: if $e+\pi$ were algebraic irrational,
  Roth's theorem would forbid infinitely many blocks with
  $\log(v!)/\log(u!)>2+\varepsilon$, as well as a finite-prefix universality
  theorem showing why no finite digit or congruence audit can decide the
  arithmetic class;
- an explicit surjectivity obstruction for the mixed polynomial-kernel map;
- a theorem-by-theorem audit explaining why Lindemann--Weierstrass, Baker,
  Nesterenko, E/G-function theory, and exponential-period theory do not yet
  settle the problem;
- a primary-source audit of the 2026 Fischler--Rivoal theorem on logarithms
  of $E$-function values.  If a Siegel $E$-function satisfies
  $F(x)=e^\eta$ for nonzero algebraic $x,\eta$, Delaygue's
  Lindemann--Weierstrass theorem forces
  $$
  x/\eta\in\mathfrak S(F),
  $$
  where $\mathfrak S(F)$ is the finite singularity set of its Borel
  $G$-function.  Hence every exact algebraic logarithm is automatically at
  one of the theorem's exceptional points.  In particular, assuming
  $\alpha=e+\pi$ algebraic, no perturbation
  $e^{\beta z}+(z-x)H(z)$ with $\beta x=\alpha$ can remove the responsible
  Borel singularity.  A separate 2026 interpolation theorem can make $x$
  regular for the minimal differential equations, but that controls a
  different singularity notion and leaves the forced Borel singularity in
  place;
- an exact mixed-$E/G$ zero-removal obstruction.  For every algebraic
  $\alpha$, the holonomic germ
  $$
  Q_\alpha(z)=\frac{\alpha-e^z-4\arctan z}{z-1}
  $$
  does **not** belong to the function class $\mathcal E+\mathcal G$.
  Indeed, a decomposition $Q_\alpha=E+G$ would put
  $$
  (\alpha-e^z)-(z-1)E=(z-1)G+4\arctan z
  $$
  in $\mathcal E\cap\mathcal G=\overline{\mathbb Q}[z]$; evaluation at
  $1$ would make $\alpha-e$ algebraic.  Under the target hypothesis,
  $Q_{e+\pi}$ is nevertheless holomorphic at $1$, so a general
  zero-removal theorem for the mixed orders $-1$ and $0$ is explicitly
  false.  The minimal order-three operator of
  $\alpha-e^z-4\arctan z$, and hence the gauge operator of $Q_\alpha$, is
  independent of $\alpha$; regularity at $1$ is a numerical connection
  condition invisible to its order, slopes, and differential module.
  Equivalently,
  $$
  F_\alpha(z)=\alpha(1-e^{-z})-2\operatorname {Si}(z)
  $$
  is an $E$-function with finite limit $\alpha-\pi$ at $+\infty$, landing
  the hypothesis exactly in the still-conjectural value-ring intersection
  $\mathbf E\cap\mathbf G=\overline{\mathbb Q}$.  Exponential-period
  normality would exclude the hypothesis, but current comparison,
  o-minimality, and $E$-period representation theorems do not prove that
  injectivity statement;
- new conditional consequences of algebraicity: Baker's theorem would force
  $\exp(qe+r\pi)$ to be transcendental whenever $q\ne0$ is algebraic, while
  Brownawell--Waldschmidt would force $\exp(\pi^2)$ to be transcendental;
- an independently audited diagonal exponential-Padé construction producing
  exact nonzero forms of size
  $\asymp e^{2n+1}n!/(2n+1)!$ under the algebraicity hypothesis, together
  with the rigorous height calculation showing why qualitative
  Lindemann--Weierstrass supplies no contradiction;
- a fully primitive-invariant direct-integral barrier for every symmetric
  log-free beta kernel $x^n(1-x)^n$ ($4\mid n$): after matching the
  exponential and $\pi$ coefficients and removing even the new content
  created by that match, the resulting integer forms have explicit lower
  bounds tending to infinity; this eliminates both sign congruence classes
  of this natural common-kernel family;
- an independently audited extension of that barrier to every single fixed
  real rational kernel $K(x)$, including sign-changing kernels, whose
  symmetric beta moments lie in $\mathbb Q+\mathbb Q\pi$: rational long
  division gives only exponential arithmetic complexity, while an exact
  midpoint beta asymptotic supplies a fixed-sign lower bound and the fully
  primitive matched form retains factorial growth;
- an independently audited variable-numerator extension for every fixed
  rational denominator $Q$ with no zero on $[0,1]$: after projectively
  primitive normalization, every numerator family with
  $n+\deg P_n+\log\|P_n\|_1=o(n\log n)$ has only subfactorial
  $\pi$-coordinate height, and Salikhov's finite irrationality measure,
  exact minimal matching, and complete content removal force the resulting
  primitive forms to diverge; any bounded escape in this class therefore
  requires primitive coefficient complexity $\Omega(n\log n)$;
- an independently audited positive derivative-kernel construction that
  enforces the two Machin-pole evaluations exactly and thereby removes every
  logarithmic coordinate.  Even after separately reducing both input pairs,
  least coefficient matching, and unrestricted final content removal, its
  primitive forms satisfy the lower bound
  $\exp((4/3)n\log n-O(n))$ and diverge.  Euler's continued fraction controls
  the otherwise unknown exponential-pair gcd, while the primitive
  $\pi$-coefficient remains only exponential;
- an independently audited treatment of the varying powers
  $(1+x^2)^{-k}$: the moments generally contain a $\log2$ coordinate
  (contrary to the naive two-coordinate premise), exact Gaussian residues
  classify the log-free indices and give coordinate height
  $\exp(O(n+k))$, and every log-free nonzero-$\pi$ sequence with
  $k=o(n\log n)$ diverges after full primitive matching; for even $n$ and
  $k>n$ the moment is automatically log-free with a positive
  $\pi$-coordinate, so no finite slope above one escapes;
- an independently audited critical-scale refinement in that automatic
  Fourier region: the common factor $2^{2k-2}$ cancels exactly in the
  primitive $\pi$-pair, leaving
  $B_{n,k}\le64^{k-1}((1+\sqrt2)/2)^n$; this extends the rigorous
  divergence barrier to the explicit slice
  $n<k\le n\log n/35$.  The sharpened constant uses
  Zeilberger--Zudilin's current irrationality measure for $\pi$, weakened
  safely to $36/5$, and a separately audited all-sign primitive-matching
  calculation;
- an exact forced-prime theorem for the content of that Fourier pair.  If
  $h_{n,k}=\gcd(4T_{n,k},L_kC_0)$, then
  $$
  \prod_{(k-1)/2<p\le2(k-n-1)/3}p\mid h_{n,k},
  $$
  where the product is over primes.  A characteristic-$p$ gap in three
  Fourier coefficients proves the divisibility.  Hence
  $\log h_{n,k}=\Theta(k)$ whenever $n=o(k)$, refuting the hoped-for
  unrestricted bound $O(n\log n)$.  The same analysis proves
  $2^{k-1}\mid T_{n,k}$ by a $\mathbb Q_2(i)$ line integral and shows that
  the complete $2$-part cancels from the primitive $\pi$ coefficient;
- an independently audited exact high-region $2$-adic theorem.  For
  $n=2r$, $K=k-1\ge2r$,
  $$
  v_2(C_0)=r+s_2(K)+(r\bmod2)v_2(K),
  \qquad
  v_2(R_{n,k})\ge-k-\lfloor\log_2K\rfloor.
  $$
  The first identity follows from a super-Catalan sum and the polynomial
  factorization
  $N_r(K)=2^rK^{r\bmod2}P_r(K)$ with $P_r$ odd-valued.  Exact even-moment
  reflection and odd incomplete-beta formulas prove the second inequality.
  Together with an elementary lower bound for $J_{n,k}$, these imply that
  the primitive $\pi$-form $A+B\pi$ diverges uniformly for
  $k\ge n\log n/35$ whenever its rational coordinate is nonzero; if that
  coordinate is zero, the primitive form is exactly $\pi$.  This does
  **not** close the fully matched $e+\pi$ family: its final content is
  exactly $\gcd(M,d)$ with $d=\gcd(q_n,B)$, whose odd part is uncontrolled.
  The exact example $n=2,k=10$ has matching gcd $d=7$ and final content
  $g=\gcd(M,d)=7$, ruling out a parity shortcut.  A subsequent exact
  odd-prime localization proves that, for
  $\alpha=v_\ell(q_n)$ and $\beta=v_\ell(B)$,
  $$
  \alpha\ne\beta\Longrightarrow v_\ell(g)=0,
  $$
  while if $\alpha=\beta=a>0$, then
  $$
  v_\ell(g)=\min\{a,\,v_\ell(q_nA-p_nB)-a\}.
  $$
  Equivalently, survival requires an explicit normalized Fourier
  congruence in addition to exact valuation matching.  This is a strict
  localization, not yet a useful uniform bound: exact examples have
  $g=11\cdot13$, $13^2$, and $7^3$, and other examples contain surviving
  primes $227,647,937$ larger than $K=k-1$.  Nevertheless, a worst-content
  estimate closes the very high tail.  The elementary beta bound
  $q_n<2(2n)^n$, positivity, and $d,g\le q_n$ give
  $$
  \Lambda_{n,k}^{\rm prim}\ge \frac{\mathcal L_{n,k}}{q_n}.
  $$
  Inserting the high-region Fourier lower bound proves uniform divergence
  for every $k\ge c n\log n$ with $c>1/\log2$, and hence explicitly for
  $k\ge(3/2)n\log n$.  Together with the accepted low-region theorem, the
  first resulting unresolved band was
  $$
  \frac1{35}n\log n<k<\frac32n\log n;
  $$
- an exact period congruence for the exponential beta coefficients.  If
  $p_n,q_n$ are the two Bessel endpoint sequences, then for every
  $m\ge1,n\ge0$,
  $$
  p_{n+m}\equiv p_n\pmod m,
  \qquad q_{n+m}\equiv(-1)^m q_n\pmod m.
  $$
  Hence, for every odd prime power $\ell^a$,
  $\ell^a\mid q_n$ if and only if
  $\ell^a\mid q_{n\bmod\ell^a}$.  This turns the Bessel side of every
  surviving odd matching prime into a finite root-class problem, but is not
  a valuation bound: exact examples include $7^4\mid q_{361}$ and
  $11^5\mid q_{1359}$;
- a generalized ladder of forced odd-prime bands in the same Fourier
  content.  Put $K=k-1$ and $\ell=K-n$.  If $p>\sqrt K$ is prime and, for
  an odd $a\ge3$,
  $$
  \frac{2K}{a+1}<p\le\frac{2\ell}{a},
  $$
  then every Fourier coefficient $C_{mp}$ in range is zero modulo $p$;
  consequently $p\mid C_0,T_{n,k},h_{n,k}$.  The resulting disjoint bands
  $$
  \frac K{j+1}<p\le\frac{2(K-n)}{2j+1},\qquad j\ge1,
  $$
  have total logarithmic mass
  $(2\log2-1+o(1))K$ whenever $n=o(K)$.  Thus their squarefree product
  divides $h_{n,k}$ and the actual primitive coefficient satisfies
  $$
  \log B_{n,k}\le(2+o(1))K+O(n).
  $$
  Combining this with positivity, exact primitive matching, the lower
  bound $q_n\ge n^n$, and the all-degree $2$-adic component bound proves
  uniform divergence for every $k\le c n\log n$ with
  $c<1/(4-\log2)$, explicitly for $k\le(3/10)n\log n$.  Together with
  the very-high theorem, the only unresolved band for this fully matched
  family is now
  $$
  \frac3{10}n\log n<k<\frac32n\log n;
  $$
- a top-prime-power extension of those forced bands.  For any odd prime
  $p$, let $Q=p^{\lfloor\log_pK\rfloor}$ be its largest power not exceeding
  $K$.  If an odd $a\ge3$ satisfies
  $$
  \frac{2K}{a+1}<Q\le\frac{2(K-n)}a,
  $$
  then $p\mid C_{mQ}$ for every shift in range and hence
  $p\mid C_0,T_{n,k},h_{n,k}$.  This rigorously adds primes
  $p\le\sqrt K$, but their total logarithmic mass is at most
  $\vartheta(\sqrt K)=o(K)$.  Therefore the one-copy prime-power theorem
  retains the leading constant $2\log2-1$ and by itself cannot improve the
  $3/10$ endpoint;
- an exact first-$p$-adic-digit filter for the surviving primes larger
  than the Fourier radius.  In the forced band
  $K<p\le2(K-n)$, write
  $$
  R(y)=P_n(y)(1+y)^{2(K-n)-p}=\sum\rho_ty^t,
  $$
  and define two explicit residues $D$ and $U$ by the truncated logarithm
  coefficient and the rational Fourier coordinate, respectively.  Then
  $$
  C_0/p\equiv D\pmod p,\qquad S_{n,k}\equiv U\pmod p.
  $$
  On the generic branch $D\ne0$, the complete matching criterion is
  $$
  p\mid g_{n,k}\Longleftrightarrow
  v_p(q_n)=1,\quad U\ne0,\quad
  4(q_n/p)U\equiv p_nD\pmod p.
  $$
  The complementary branch $D=0$ is exactly $p^2\mid C_0$.  A reflection
  identity also gives
  $p_{M-1-r}\equiv p_r$ and $q_{M-1-r}\equiv q_r\pmod M$ for every odd
  modulus $M$.  The filter certifies, but does not exclude, the known
  survivors $227,647,937>K$; coincidence of its Bessel and Fourier
  conditions remains a genuine obstruction;
- an exact polynomial classification of the filter's exceptional branch.
  For $n$ even there is an explicit positive-coefficient polynomial
  $\Phi_n\in\mathbb Z[X]$ of degree $n/2$ such that, throughout
  $K<p\le2(K-n)$,
  $$
  D\equiv-\frac{s!}{n!(K-n)!K!}\Phi_n(s)\pmod p,
  \qquad s=2(K-n)-p.
  $$
  Hence $D=0$ exactly when
  $p\mid\Phi_n(2(K-n))$, and for fixed $(n,p)$ there are at most $n/2$
  exceptional $K$-values.  The squarefree product of exceptional primes
  surviving the final match divides
  $\gcd(q_n,\Phi_n(2(K-n)))$.  Its present elementary size bound is still
  $\exp(O(n\log(n+K)))$, so this rigorous localization remains too large
  to close the strip, and it does not address the generic branch;
- a sharp obstruction to two elementary attacks on that generic branch.
  At $(n,p)=(64,937)$, the exact survival residue over all $404$
  admissible values $K=533,\ldots,936$ has interpolation degree exactly
  $403$; its only generic zero is the known survivor $K=797$.  Thus no raw
  polynomial-in-$K$ description of degree at most $402$ (in particular,
  no universal degree bound $6n$) can encode it.  On the other hand, if
  $\mathcal G^{\rm gen}$ is the squarefree product of simultaneous generic
  survivors, then
  $$
  \mathcal G^{\rm gen}\mid q_n,
  \qquad(\mathcal G^{\rm gen})^2
    \mid4q_nT_{n,k}-p_nL_KC_0.
  $$
  The direct CRT size estimate is
  $|4q_nT-p_nL_KC_0|\le15q_nL_K2^{2K+n/2}$; in the upper part of the open
  strip its square root is no better at leading order than the original
  bound by $q_n$.  Low-order rational or hypergeometric normalization is
  not ruled out;
- an exact factorial normalization and three-dimensional recurrence for
  every admissible generic digit at fixed $(n,p)$.  If
  $c=(p-2n-1)/2$, $s=2v+1$, and
  $$
  A(z)=P_n(z)(1+z)z^{c-1},\qquad
  w(z)=\frac{(1+z)^2}{z},
  $$
  put
  $$
  I_v=\int_1^iA(z)w(z)^v\,dz,\qquad
  J_v=\int_1^izA(z)w(z)^v\,dz.
  $$
  Two exact integration-by-parts identities, with all endpoint terms and
  characteristic-$p$ degree bounds audited, give a first-order rational
  transition
  $$
  (I_v,I_{v+1},J_v)\longmapsto(I_{v+1},I_{v+2},J_{v+1})
  $$
  for $0\le v\le c-3$.  Its pivots are the units
  $c+2n+v+3$ and $i(c-v-2)$ even when
  $\mathbb F_p[i]$ is a split ring.  Dividing by
  $$
  \kappa_v=-\frac{(2v+1)!}{n!\ell_v!K_v!}
  $$
  turns the matching condition into
  $$
  4(q_n/p)\operatorname {Im}(\kappa_v^{-1}I_v)
   =p_n\Phi_n(2v+1)\pmod p.
  $$
  This does not itself bound the number of returns.  The independently
  reconstructed split-field example $(n,p)=(82,953)$ has exactly two
  isolated generic zeros, at $(v,K)=(55,614)$ and $(281,840)$, disproving
  an at-most-one shortcut.  A scalar adjoint, Wronskian, or bounded-order
  zero theorem remained possible at that stage;
- an exact endpoint-period and Casoratian refinement of that recurrence.
  The central digit is itself the companion endpoint period
  $$
  D_v=\int_{-1}^{0}z^{c-v-1}P_n(z)(1+z)^{2v+1}\,dz,
  $$
  so $D_v,\operatorname {Re}I_v,\operatorname {Im}I_v$ obey the same
  scalar order-three equation
  $$
  \begin{aligned}
  &(2n+2v+5)(2n+2v+7)X_{v+3}\\
  &\quad=64(v+1)(2v+3)X_v
  -8Q_vX_{v+1}
  +2(2n+2v+5)(4n+10v+23)X_{v+2},
  \end{aligned}
  $$
  where
  $Q_v=n^2+12nv+21n+16v^2+58v+53$.  Its forward and backward
  pivots are units throughout the admissible range.  More decisively, the
  initial three-period Casoratian has the explicit nonzero product
  $$
  (-1)^{n/2+1+c(c+1)/2}
  \frac{2^{24}}{3^4 5^2 7^2}
  \prod_{j=1}^{n/2-1}
  \frac{2^{14}(j+1)^3(2j+1)^2}
  {j(4j+5)(4j+7)^2(4j+9)}
  \pmod p.
  $$
  Exact Hermite reduction under $(n,c)\mapsto(n+2,c-2)$ proves the
  product, and every displayed factor is a unit when $c\ge3$.  Therefore,
  on the branch $v_p(q_n)=1$, the actual matching residual
  $F_v=4(q_n/p)\operatorname {Im}I_v-p_nD_v$ is not the zero solution and
  cannot vanish at three consecutive $v$ (equivalently, three consecutive
  $K$-forms in one block).  This is only an adjacent-zero theorem: the
  target has exact separated double returns, and the abstract recurrence
  has the nonzero solution $(1,9,0,0,2,0)\bmod17$.  It does not yet control
  small primes, exceptional digits, prime powers, or all separated returns;
- an exact refutation of the next two total-zero shortcuts.  On the simple
  Bessel-root branch, the actual nonzero target has four isolated generic
  returns for
  $$
  (n,p)=(3996,291869),\qquad
  \{v:F_v=0\}=\{34071,69843,112900,121346\}.
  $$
  Here $c=141938$, $v_p(q_n)=1$, and both endpoint digits are nonzero at
  every return.  The complete target was reconstructed from the defining
  degree-$7993$ polynomial, from the independent $n\mapsto n+2$
  contiguity matrices, and once more by a direct repeated-quadratic
  multiplication; all three calculations give the same transcript hash.
  Thus universal bounds of two and three total returns are false.  The
  global $k$-recurrence for
  $J_{n,k}=\int_0^1x^n(1-x)^n(1+x^2)^{-k}\,dx$ specializes exactly to the
  endpoint operator and loses a pivot at each band edge.  Its generating
  function satisfies an order-two equation only with an injectively
  determined quadratic forcing term, and the Ore-reduced adjacent minor
  already vanishes at $v=18,22,42$ for $(n,p)=(2,109)$.  These facts close
  the obvious recurrence-order reductions, but do not prove that the
  number of returns is unbounded or exclude a weighted-product estimate;
- an exact three-adjacent-form consequence, including the exceptional and
  prime-power branches.  For $K_i=K+i$, let $d_i$ be the initial
  coefficient-matching gcd, $g_i$ the final content, $h_i=d_i g_i$, and
  $G_3=\gcd(g_0,g_1,g_2)$.  Primewise valuation counting always gives
  $$
  \prod_{i=0}^2h_i\le q_n^5G_3.
  $$
  If $p^a\parallel q_n$ lies in the common one-block band
  $$
  K+2<p\le2(K-n),
  $$
  then the Casoratian theorem sharpens its local contribution to
  $\sum_i v_p(h_i)\le5a$: for $a=1$, survival in all three forms would
  force three consecutive zeros of the nonzero target $F_v$; for $a\ge2$,
  it would force three consecutive zeros of the nonzero central period
  $D_v$.  Hence no common-band prime divides $G_3$.  If $q_{\rm out}$ is
  the full $q_n$-primary factor outside that band, then
  $$
  G_3\mid q_{\rm out},\qquad
  \prod_{i=0}^2h_i\le q_n^5G_3\le q_n^5q_{\rm out},
  $$
  and at least one adjacent form obeys
  $$
  \Lambda_i^{\rm prim}\ge
  \frac{\min_j\mathcal L_j}{q_n^{2/3}G_3^{1/3}}.
  $$
  The complementary factor is a real obstruction, not a bookkeeping
  artifact: at $n=2$ and $K=9,10,11$, one has
  $q_2=d_i=g_i=7$ in all three forms, so the product is exactly
  $7^6=q_2^5G_3$.  Thus the theorem conditionally improves the high-region
  threshold to $(2+\theta)/(3\log2)$ if
  $\log G_3\le(\theta+o(1))\log q_n$, but the currently unconditional
  value $\theta=1$ returns the old $1/\log2$ threshold;
- a new all-prime sparsity theorem for the Bessel denominator roots.  If
  $$
  \mathcal R_p=\{0\le r<p:p\mid q_r\},\qquad R_p=|\mathcal R_p|,
  $$
  then for every odd prime $p$ and $1\le D\le p$,
  $$
  R_p\le\frac{D(D-1)}2+\frac p{D+1}\le2p^{2/3}
  $$
  after optimizing $D$.  A gap $d$ between cyclic root classes makes its
  starting class a root of a nonzero polynomial of degree $d-1$, while all
  gaps sum to $p$.  Consequently, for
  $\operatorname {rad}_{\le X}(q_n)=\prod_{p\le X,\ p\mid q_n}p$,
  $$
  \sum_{n=N}^{2N-1}\log\operatorname {rad}_{\le X}(q_n)
  \le3NX^{2/3}\log X+2X^{5/3}\log X.
  $$
  At $X=C N\log N$ the dyadic average is $o(N\log N)$.  This controls only
  the squarefree smooth radical and only on average.  The exact missing
  term is
  $\sum_{p\le X}(v_p(q_n)-1)_+\log p$; examples
  $7^4\mid q_{361}$ and $11^5\mid q_{1359}$ show it is real.  Moreover,
  the exact second anti-period law
  $$
  q_{n+2p}+2q_{n+p}+q_n\equiv2p q_n\pmod {p^2}
  $$
  makes $(-1)^tq_{r+tp}$ affine modulo $p^2$ above every root class
  $r\bmod p$.  Thus a first lift is unique, absent, or fully $p$-fold.
  Reflection forces every central root $r=(p-1)/2$ into the singular
  branch: it dies unless $p^2\mid q_r$, in which case all $p$ lifts
  survive.  The first such root is $(p,r)=(79,39)$ and it dies modulo
  $79^2$.  More precisely, if $m=(p-1)/2$, factor pairing at the center
  gives the exact obstruction
  $$
  q_m\equiv(-1)^m\sum_{j=0}^m\frac{(1/2)_j^2}{j!}\pmod {p^2}.
  $$
  Thus the fully branching central case is exactly a truncated
  hypergeometric Wieferich congruence, not merely an analogy.
  Unconditionally, for every $a\ge1$,
  $$
  R_{p^a}\le p^{a-1}R_p\le2p^{a-1/3}.
  $$
  This controls every valuation level whose period fits inside a dyadic
  averaging interval: uniformly in $X$,
  $$
  \frac1N\sum_{n=N}^{2N-1}
  \sum_{p\le X}\sum_{\substack{a\ge2\\p^a\le N}}
  {\bf1}_{p^a\mid q_n}\log p
  \le6N^{1/3}\log N=o(N\log N).
  $$
  The exact remaining tail is $p^a>N$; the density argument has no
  averaging gain there.  An exhaustive scan of all $18{,}013$ roots over
  the $17{,}983$ odd primes $p\le200000$ finds no fully branching root.
  Its only singular root is $(79,39)$, which dies, while $(13,8)$ is the
  only base representative divisible by $p^2$ and has ordinary slope.
  These are finite diagnostics only.  The possible fully branching
  alternative and the high-level tail rule out both a blanket
  simple-Hensel argument and a complete valuation bound from the present
  lifting laws.  Pairwise occurrences admit a further exact reduction.
  With
  $$
  P_0(X)=0,\quad P_1(X)=1,\quad
  P_{d+2}(X)=(4X+4d+6)P_{d+1}(X)+P_d(X),
  $$
  one has
  $$
  q_{n+d}=P_d(n)q_{n+1}+P_{d-1}(n+1)q_n,\qquad
  \gcd(q_n,q_{n+d})=\gcd(q_n,P_d(n)).
  $$
  Hence every repeated high-power occurrence can be charged to an
  explicit gap polynomial.  The full high tail splits exactly into one
  deepest occurrence per prime plus pairwise truncated-high-gcd terms.
  The singleton-max part is invisible to every gap argument.  This is a
  real obstruction even without singular branching:
  $v_{11}(q_{1359})=5$, the lift has a unique child at every tested level,
  and $1359$ is the only index in $[1359,2717]$ with
  $11^4\mid q_n$.  Its two high levels lie wholly in the singleton term.
  Thus even an all-prime exclusion of full branching would leave an
  isolated ordinary-lift problem at the required main scale.  In the
  matching problem, the exact triple at $n=18$, $k=1004,1005,1006$ reduces
  the three $7$-adic content valuations to $(3,2,1)$, but no uniform
  prime-power theorem is yet known.  The exceptional central lift now has
  a further exact classical reduction.  For $p=2m+1$, put
  $$
  A_m=m!L_m(-1)=\sum_{j=0}^m j!\binom mj^2,\qquad
  C_m=m!\left.\partial_\alpha L_m^{(\alpha)}(-1)
       \right|_{\alpha=0}.
  $$
  Then
  $$
  q_m=(-1)^m m!L_m^{(-p)}(-1),\qquad
  q_m\equiv(-1)^m(A_m-pC_m)\pmod {p^2},
  $$
  where
  $$
  C_m=\sum_{r=1}^m\frac{(m)_r}{r}A_{m-r}
     =\sum_{j=0}^m j!\binom mj^2(H_m-H_{m-j}).
  $$
  Conditional on the central root, its all-$p$ branch is therefore exactly
  $A_m/p\equiv C_m\pmod p$.  The Padé Wronskian
  $$
  P_m'Q_m-P_mQ_m'-P_mQ_m=(-1)^{m+1}x^{2m}
  $$
  proves that $x=1$ is a simple root of $Q_m(x)$ modulo $p$, but this is
  an argument lift and does not decide the Laguerre parameter quotient.
  An exact remainder-tree scan of all $148{,}932$ odd primes through
  $2{,}000{,}001$ finds only $p=79$, where
  $A_{39}/79\equiv45$, $C_{39}\equiv57$, and
  $q_{39}/79\equiv12\pmod {79}$; this is finite evidence, not a universal
  exclusion.  The same three quantities also lie in one monic Charlier
  polynomial
  $$
  F_m(a)=\sum_{j=0}^m\binom mj(a)_{\underline j}:
  \qquad
  F_m(m)=A_m,\quad F'_m(m)=C_m,\quad
  F_m(m-p)=(-1)^mq_m.
  $$
  Hence the all-$p$ branch is exactly the assertion that the root
  $a=m\pmod p$ has Hensel digit $-1$.  The generating function
  $\sum F_n(a)z^n/n!=e^z(1+z)^a$ supplies exact Newton, Wilson, and
  Frobenius reformulations.  Their apparent new terms cancel: the
  $p$-step harmonic correction is ordinary Taylor expansion, the Wilson
  quotient is multiplied by the vanishing central value, and the first
  two Frobenius orders are derivatives of the same identity
  $G(z)^t=(1+G(z)-1)^t$.  These are rigorous no-go results for those
  shortcuts, not a proof that the digit $-1$ is impossible.  A separate
  index-Frobenius analysis now gives the exact identity
  $$
  F_{p+n}(a)=\sum_{r=0}^p\binom pr(a)_{\underline r}F_n(a-r)
  $$
  and an explicit correction polynomial
  $F_{p+n}-F_pF_n\equiv p\mathcal E_{p,n}\pmod {p^2}$.
  Thus a simultaneous value/derivative zero propagates by $p$ only modulo
  $p$; its two next digits contain genuinely new correction residues.  At
  the central parameter the same obstruction is a resonance condition for
  a first-order polynomial ODE.  If $K$ is its degree-$(m-1)$ solution and
  $B_m$ its leading coefficient, the exact finite-field energy identity is
  $$
  \beta_m=2\int_0^1zK(z)^2\,dz-B_m^2\pmod p.
  $$
  The top-coefficient term is essential: it is the Frobenius anomaly lost
  by naive integration by parts.  The symmetric terminating ${}_2F_0$
  form also yields an exact next-block congruence involving Wilson, Fermat,
  and harmonic quotients, but its left side is a new uncontrolled block
  residue.  These corrected identities sharpen the obstruction without
  proving that the forbidden digit is impossible;
- an exact Hermite reduction for the quartic power kernels
  $$
  J_{n,k}^{(4)}=\int_0^1\frac{x^n(1-x)^n}{(1+x^4)^k}\,dx.
  $$
  If the reduced numerator is $a+bx+cx^2+dx^3$, then
  $$
  J_{n,k}^{(4)}=R_{n,k}
  +\frac{a-c}{2\sqrt2}\log(1+\sqrt2)+\frac d4\log2
  +\left(\frac{a+c}{4\sqrt2}+\frac b8\right)\pi.
  $$
  Actual log cancellation is exactly $d=0$, $a=c$.  Uniformly proved
  log-free cases are $k=1$, $n\equiv6\pmod8$; the inversion-balanced ray
  $(n,k)=(4j+2,3j+2)$; and $(n,k)=(3,2)$.  An exact scan through
  $n,k\le160$ finds no others, but completeness remains conjectural.  The
  universal non-polynomial denominator is
  $2^{3(k-1)-s_2(k-1)}$.  The balanced ray has only exponential decay and
  its matched primitive forms diverge even after full algebraic-content
  removal, so that ray is closed.  Two neighboring powers always cancel
  the remaining logarithm.  Exact beta-integral coordinates and a
  pole-avoiding saddle analysis show that their complex saddle multiplier
  is
  $$
  -(1+i)r^5-\frac32r^6+O(r^7),\qquad
  r=(4k/n)^{-1/4},
  $$
  but its real projection contains a moving cosine.  The phase mesh between
  neighboring integer powers is $r^5(1+o(1))$, so no lower bound by a fixed
  positive fraction of the saddle envelope can hold uniformly in every
  power.  Three adjacent powers remove this phase obstruction: if
  $L_s=L_{n,k+s}$, then, uniformly for
  $n\to\infty$, $r\to0$, and $nr^{10}\to\infty$,
  $$
  L_1^2-L_0L_2
  =\frac8{\pi^2}\mathcal I_{n,k}^2\rho^2
    \left(r^{10}+O(r^{12}+n^{-1})\right)>0.
  $$
  This includes every fixed window $k\asymp n\log n$.  It yields an exact
  primitive integer quadratic $P(Q)>0$ with
  $\max|C_j|=O(Hr^{-5})$ and
  $\sum_{s=0}^2C_sL_s=0$, hence a positive log-free three-power form.
  Whole-line integration proves its $\pi$-coordinate is nonzero.
  Symmetrization cancels the odd coordinate and gives the exact
  scale-invariant identity
  $$
  \frac{\Lambda^{\rm sym}}{B^{\rm sym}}
  =2\pi\frac{\int_{-1}^1F(x)\,dx}
              {\int_{-\infty}^{\infty}F(x)\,dx}
  =2\pi(1+o(1)).
  $$
  Thus this positive branch has no analytic smallness after its
  $\pi$-coefficient is normalized.  An adversarial audit repaired two
  proof gaps—the infinite-tail bound now retains its decisive $2^{-k}$
  factor, and the $c=0$ kernel case is handled separately—without changing
  the theorem.  The final coefficient pair lies over
  $\mathbb Q(\sqrt2)$, so the ratio is an analytic obstruction rather than
  a complete primitive ideal-content theorem; the two-power arithmetic
  phase separation and the quadratic-field content question remain open.
  three-power elimination also has a complementary rational version.
  The exact odd coordinate is
  $$
  b_j=-\frac1\pi\left(A_{+,j}-A_{-,j}
       +2(-1)^{n/2}\operatorname {Im}I_j\right).
  $$
  Therefore the cross product $C=L\times E$ cancels both even period rows
  and leaves
  $$
  C\cdot J=C\cdot R+\frac{C\cdot b}{8}\pi,
  \qquad
  C\cdot b\sim-\frac{16}{\pi^3}A_+|I|^2r^{15}<0.
  $$
  This is a genuine rational $1,\pi$ form, and its normalized error is at
  most $\exp\{-nr+O(nr^2)\}$ at the critical scale.  Its primitive endpoint
  height remains uncontrolled.  At fixed slope $k/n\to\kappa>1/2$, the
  same rational cross product has the conditional projected-saddle rate
  $$
  \left|\pi+\frac AB\right|
  \le\exp\{n(j(\kappa)-\ell(\kappa))+o(n)\};
  $$
  the transition exponent is
  $\ell(1/2)-j(1/2)=1.388912660352581880\ldots$.
  Under the same non-exponential phase condition, the fully cleared form has rate
  $G(1/2)=10.643873127064585\ldots$, so any primitive escape must lie in
  the exact endpoint content $\gcd(8U,V)$ of
  $8\Delta_0\Delta_1\Delta_2\Lambda=8U+V\pi$.  On the boundary
  $n=4m,k=2m+1$, an unconditional calculation in
  $\mathbb Z[x]/(x^4+1)$ proves
  $$
  v_2(a_K-c_K)=v_2(a_K+c_K)=m,
  $$
  $$
  v_2\det(v_K,v_{K+1})=2m+2+v_2(m),\qquad
  v_2\det(v_K,v_{K+2})=2m+3+v_2(m),
  $$
  and hence the primitive cross-vector law
  $$
  (v_2(C_0),v_2(C_1),v_2(C_2))
  =(0,3,5+v_2(m+1)).
  $$
  The proof retains the required modulo-$32$ Bell correction before
  division by $4m$.  The remaining odd endpoint coordinate is an exact
  terminating sum $S_m$; its conjectured denominator law is equivalent
  to
  $v_2(S_m)=m+s_2(m)+v_2(m)+1$, which is not yet proved.  The odd
  endpoint content and final determinant gcd are also uncontrolled.
  Four powers remove the remaining real
  phase, but their cubic kernel
  $(g_+-t)(t-g_i)(t-\overline g_i)$ simultaneously annihilates the leading
  $b$ saddle.  For a cleared $2\times m$ matrix $A=(L;E)$ and full
  coordinate matrix $M=(L;E;R;b/8)$, the exact lattice invariants are
  $$
  \det\ker_{\mathbb Z}A
   =\frac{\sqrt{\det(AA^T)}}{\delta_2(A)},\qquad
  [\mathbb Z^2:\Gamma]=\frac{\delta_4(M)}{\delta_2(A)}.
  $$
  When $m\ge5$, $\ker_{\mathbb Z}M$ has rank $m-4$, so short vectors can
  be exact zero forms; a generic Siegel lemma does not control a useful
  endpoint pair.  Finally, proportional finite differences optimize at
  order $s/k=1/7$ but improve the dyadic-cleared base only from $8$ to
  $7$, never to decay.  All leading saddle multipliers satisfy the same
  degree-five integer equation, so exact leading-saddle annihilation is
  inherently nonselective.  The minor gcds and endpoint-lift height remain
  the precise open arithmetic quantities.  A next-order audit of the
  four-power kernel makes this obstruction sharper.  All linear-in-power
  saddle corrections and all first positive-row corrections cancel, but
  the quadratic complex-saddle correction survives.  If
  $\Phi=\arg I+\pi/4+2r+O(r^2)$, then, uniformly on subsequences with
  $|\sin\Phi|$ bounded below and $nr^{45}\to\infty$,
  $$
  c\cdot b\sim
  -\frac{4096(-1)^{n/2}}{\pi^6}
   \frac{A_+|I|^5}{n}r^{43}\sin\Phi.
  $$
  The phase drops by $\asymp r^5$ between adjacent powers, so every
  sufficiently long critical window contains both signs with
  $|\sin\Phi|>1/2$.  The resulting normalized rational form still obeys
  $$
  \pi+\frac{8c\cdot R}{c\cdot b}
  \sim\frac{(-1)^{n/2}\sqrt2\,\pi\,nr^2}{\sin\Phi}\frac{J}{|I|},
  $$
  and is exponentially small before primitive normalization.  Its raw
  kernel height is at most $24H^5$.  No bound presently prevents the
  coefficient gcd or endpoint-pair content from absorbing this gain, so
  the calculation supplies a nonvanishing analytic subsequence but not
  yet a primitive integer approximation theorem.  The raw four-power
  coefficient content and endpoint quotient have now been reduced exactly.
  If $q=g_qq^*$ is the primitive quadratic Hankel annihilator,
  $\widehat e_s=\sum_{j=0}^2q_j^*\epsilon_{j+s}$, and
  $h=\gcd(\widehat e_0,\widehat e_1)$, then
  $$
  \operatorname {cont}(c)=g_q^2h,\qquad
  \delta_2(A)\mid\gcd(e_0,e_1)\mid\operatorname {cont}(c).
  $$
  Thus much of the raw content is forced saturation content and disappears
  under primitive normalization.  For the saturated kernel
  $K=\ker_{\mathbb Z}A$, jointly cleared endpoint map $B$, and Smith
  invariants $s_1\mid s_2$ of $B(K)$,
  $$
  s_1s_2=\frac{|\det(A;B)|}{\delta_2(A)},\qquad
  \gcd(Bv)=s_1\gcd\!\left(u,\frac{s_2}{s_1}\right)
  $$
  for every primitive kernel vector with first Smith coordinate $u$.
  Hence a large quotient determinant proves that some directions have
  large content but says nothing decisive about the canonical direction.
  Its exact remaining obstruction is the selected gcd
  $\gcd(u_c,s_2/s_1)$, after separately removing the common block-clearing
  factor.  No asymptotic bound for this selected gcd is presently known;
- an independently audited root-of-unity specialization of the corrected
  Rivoal exponential--logarithm Padé forms: under the hypothetical
  algebraicity of $e+\pi$ it gives a genuine algebraic integer after exact
  denominator clearing, but the construction supplies neither a theorem
  excluding its vanishing nor the strict global norm bound needed for a
  contradiction; moreover, the norm identity
  $N_{\mathbb Q(\zeta_N)/\mathbb Q}(1-\zeta_N)=\Phi_N(1)$ shows that the
  isolated small root-of-unity factor is globally neutral for non-prime-power
  $N$ and adverse for prime-power $N$;
- an independently audited analytic continuation and complete
  nonproportional classification of those forms at the small roots
  $N=3,4,6$, together with the boundary result at $N=2$.  Exact
  Sokhotski--Plemelj analysis proves that every nonzero
  coefficientwise-cleared $N=2$ value has modulus at least one.  For every
  admissible unbounded parameter sequence at $N=3,4$, the fully cleared
  values tend to infinity; at $N=6$ their liminf is at least $6/e^2$, and
  this constant is attained by the unscaled edge
  $(c,f)=(1,1)$, $d\to\infty$.  The proof exhausts compact slopes,
  $f$-dominant limits, the moving endpoint band, and fixed-$d$ edges; the
  formerly open sparse nonproportional cone is therefore closed for this
  local family.  The argument still does not control all conjugates of the
  hypothetical algebraic number $e+\pi$, which is the global-norm
  obstruction;
- an independently audited two-conjugate-log extension of the corrected
  Rivoal construction.  A one-log specialization can isolate $\pi$ with an
  algebraic coefficient only when its logarithmic argument is a root of
  unity, by Gelfond--Schneider; thus arbitrary Pisot or Salem units do not
  supply a new one-log parameter.  There is, however, a genuine paired
  family for every odd $n\ge5$:
  $$
  \eta=(1+\zeta_n)^{-1},\qquad \bar\eta=1-\eta,
  \qquad
  \operatorname{Log}(1-\eta)-\operatorname{Log}(1-\bar\eta)
  =\frac{2\pi i}{n}.
  $$
  On the edge $c=f=0$, its distinguished form is eventually nonzero and
  has size $\asymp_n|\eta|^d/d$.  Every coefficient-field embedding was
  then tracked with its correct logarithmic branch: the raw product grows
  with a base $B_n>1$.  For $n=5$, multiplication by $-i$ places the form
  in $K=\mathbb Q(\zeta_{20})^+$ and its degree-$4$ product is
  $\asymp\varphi^d d^{-3}$.  Exact Smith forms compute the full primitive
  coordinate ideal through $d=200$; apart from $d=1$, its norm is
  $$
  \left(5^{[d\equiv2\ ({\rm mod}\ 5)]}
        19^{[d\equiv15\ ({\rm mod}\ 19)]}\right)^2,
  $$
  and is strictly below $\varphi^d$ for every $3\le d\le200$.  The
  first extrapolation failure occurs at $d=205$: an independent exact
  determinantal-divisor calculation gives Smith invariants
  $(1,1,361,361)$ and the ideal identity
  $$
  \mathfrak c_{205}=(4-t)^2\mathcal O_K,
  \qquad t=\zeta _5+\zeta _5^{-1},
  \qquad N(\mathfrak c_{205})=19^4.
  $$
  Thus the displayed formula remains a theorem only through degree $200$;
  it is not an all-degree pattern.  No prime other than $5$ or $19$ occurs
  in the exact scan through $500$, and $d=205$ is its only additional
  lift, but those are finite diagnostics.  A subsequent finite-state local
  theorem does classify these two primes in every degree:
  $$
  v_{(2-t)\mathcal O_K}(\mathfrak c_d)=[d\equiv2\pmod5],
  \qquad
  v_{(4-t)\mathcal O_K}(\mathfrak c_d)
   =[d\equiv15\pmod {19}]+[d\equiv205\pmod {361}].
  $$
  Exact periods $20$ and $32490$, together with an invariant
  $C\mapsto C+\lambda P$ shift at the period endpoints, make this an
  all-degree result rather than an extrapolation.  It caps the contribution
  of $5$ and $19$, but does not exclude varying new primes.  The full
  all-degree ideal-content rate, nontrivial intersections with a
  hypothetical target field, and the target's unknown conjugates remain
  uncontrolled, so this is a locally contracting diagnostic family and a
  precise norm obstruction, not a proof about $e+\pi$;
- a general-prime finite-state obstruction for that same $n=5$ ideal
  content.  With the integral polynomials $P_r,C_r$, put
  $a_r=P_r(1)$ and, in $F=\mathbb Q(\sqrt5)$,
  $$
  \mathfrak J_r=(N_r,a_rT_r),\qquad
  N_r=P_r(\eta)P_r(\bar\eta),\qquad
  T_r=\frac{P_r(\eta)C_r(\bar\eta)
                 -P_r(\bar\eta)C_r(\eta)}{\zeta_5-\zeta_5^{-1}}.
  $$
  For every odd prime $p\ne5$, if $r\equiv d\pmod p$ and $p$ occurs in
  the coordinate-content ideal $\mathfrak c_d$, then
  $p\mid N_{F/\mathbb Q}(\mathfrak J_r)$.  Conversely, for the base
  representative $0\le r<p$, this norm divisibility is equivalent to
  occurrence of $p$ in $\mathfrak c_r$.  The proof uses the exact block
  congruences $P_d\equiv X^{mp}P_r$ and
  $C_d\equiv X^{mp}(C_r+mL_pP_r)\pmod p$; the determinant is unchanged
  by the resulting $C\mapsto C+\lambda P$ shift.  An exact probe of every
  prime $p\le1000$ finds only $(p,r)=(19,15)$.  This reduces each fixed
  prime to a finite common-zero problem, but it supplies no uniform
  exclusion as $p$ varies;
- an exact truncated-exponential reduction of all three base-representative
  common-zero alternatives in that ideal.  Put
  $x=\eta$, $y=\bar\eta=\zeta_5x$,
  $A=2+\zeta_5+\zeta_5^{-1}$, and
  $$
  K_d(X)=P_d(\zeta_5X)-\zeta_5^{d+1}P_d(X),\qquad
  h_d=\frac{K_d(x)}{(1-\zeta_5)y^d}.
  $$
  For $p>d$, $p\ne5$,
  $P_d(x)=P_d(y)=0$ is equivalent to
  $h_d=h_{d-1}=0$, while
  $$
  \sum_{d\ge0}h_d\frac{z^d}{d!}
   =\frac{e^z}{1+Az+Az^2}.
  $$
  Hence the same condition is exactly
  $(1+Az+Az^2)\mid E_d(z)$.  The reciprocal denominator has the
  five-step factorization
  $$
  (1+Az+Az^2)
  \{1-Az+(2A-1)z^2+(1-2A)z^3\}
  =1-(5A-2)z^5,
  $$
  producing an exact first-order recurrence in each residue class modulo
  five.  The alternative $P_d(1)=P_d(x)=0$ is similarly equivalent to
  $(1+z)(1+(1+\zeta_5)z)\mid E_d(z)$.  Finally,
  $P_d(x)=C_d(x)=0$ is exactly the assertion that $\lambda=0$ is a
  multiple root of the explicit monic polynomial
  $$
  \mathcal F_d(\lambda,1+\zeta_5)
   =d![z^d]\frac{e^z(1+z)^\lambda}
                    {1+(1+\zeta_5)z}.
  $$
  These three cases exhaust the ideal obstruction after the exact
  $d\mapsto d\bmod p$ block reduction.  They localize the problem but do
  not prove that only $19$ occurs;
- an exact proof that the most direct $p$-boundary continuation of that
  five-step recurrence loses, rather than constrains, its endpoint data.
  The sequence has period $p$ modulo $p$, but at
  $p,p+1,\ldots,p+4$ every five-step multiplier contains $p$ and resets
  directly to $h_0,\ldots,h_4$.  Thus matching the five residue chains
  across the boundary supplies no terminal equation.  If
  $m=p-1-d$, the simultaneous $P$-zero is instead equivalent to the exact
  weighted left-factorial pair
  $$
  \sum_{j=0}^d(m+j)!(1+\zeta_5)^j=0,\qquad
  \sum_{j=0}^d(m+j)!(1+\zeta_5^{-1})^j=0\pmod p.
  $$
  Wilson formulas identify the two free pre-boundary values as five-block
  weighted left-factorial sums.  Frobenius adds no equation for
  $p\equiv1\pmod5$, swaps the two for $p\equiv4\pmod5$, and supplies the
  other two cyclotomic conjugates for $p\equiv2,3\pmod5$.  None of these
  exact identities proves uniform zero avoidance; the sole hit
  $(19,15)$ in the certified finite box is explicitly diagnostic;
- an exact coupling of the two weighted left-factorial equations.  With
  $m=p-1-d$ and
  $$
  W_m(Z)=\sum_{j=0}^d(m+j)!Z^j,
  $$
  one has
  $$
  Z^2W_m'+((m+1)Z-1)W_m=-m!\pmod p.
  $$
  Reducing modulo
  $Z^2-AZ+A=(Z-u)(Z-v)$ gives a linear remainder
  $a_m+b_mZ$; the true simultaneous zero is exactly
  $a_m=b_m=0$.  Its product resultant
  $a_m^2+Aa_mb_m+Ab_m^2$ has the same radical only after adjoining
  $b_m$.  Indeed, at $(p,d)=(11,4)$ one weighted value is zero and the
  other is not, rigorously refuting use of the product alone.  The
  remainder vector obeys a complementary recursion whose matrix satisfies
  $M^5=-(5A-2)I$.  More sharply,
  $$
  H_m(Z)=W_m(\zeta_5^{-1}Z)-\zeta_5W_m(Z)
  $$
  omits every coefficient with index $4\bmod5$, and the localized ideal
  identity
  $$
  (W_m(u),W_m(v))=(H_m(u),H_m'(u))
  $$
  turns the true pair into a prescribed double-root problem.  This is an
  exact compression, not a proof that only the prime $19$ occurs;
- a single prescribed-first-jet trichotomy for all three common-zero
  branches.  For any unit $c$ with $c^{-1}-1$ a unit,
  $$
  H_{m,c}(Z)=W_m(cZ)-c^{-1}W_m(Z)
  $$
  satisfies an exact differential identity yielding
  $$
  (W_m(r),W_m(cr))=(H_{m,c}(r),H_{m,c}'(r)).
  $$
  The choices $(r,c)=(u,\zeta_5^{-1})$ and $(1,u)$ give respectively
  the $P_d(\eta),P_d(\bar\eta)$ and $P_d(1),P_d(\eta)$ branches; the
  $P_d(\eta),C_d(\eta)$ branch is the prescribed double root
  $\lambda=0$ of $\mathcal F_d(\lambda,u)$.  These alternatives exhaust
  the general-prime ideal after $d\mapsto d\bmod p$.  In every row the
  first-jet ideal $(f(s),f'(s))$ is the remainder-content ideal modulo
  $(X-s)^2$, and adjoining $f'(s)$ to
  $\operatorname {Res}((X-s)^2,f)=f(s)^2$ recovers the same radical.
  Full discriminants are strictly too coarse: certified examples in all
  three rows have an unrelated multiple root but a nonzero prescribed
  first jet.  Thus even the shared subresultant form does not classify its
  prime support;
- a rational-trace analysis of the $n=5$ two-log edge.  For
  $K=\mathbb Q(\zeta_{20})^+$ and $F=\mathbb Q(\sqrt5)$, the real
  algebraic-coefficient form decomposes exactly as $\Theta_d=X_d+Y_d$
  with $X_d$ fixed and $Y_d$ anti-fixed under $K/F$,
  $|\nu_1(Y_d)|\asymp\varphi^d/d$.  Every multiplier in $F$ annihilates
  $Y_d$ and, after rational primitivization, collapses to the same
  divergent reduced derangement form.  If
  $\theta_d\in\mathcal O_K^\times\setminus F$ and
  $H(\theta_d)=\max_\sigma|\sigma(\theta_d)|$, the integral norm of
  $\theta_d-\tau\theta_d$ gives
  $$
  |L_d|\gg\frac{\varphi^d}{dH(\theta_d)^2}
  $$
  throughout the range where the growing embedding dominates.  Thus every
  unit-trace family with sublinear exponent vector is excluded, and any
  primitive trace tending to zero must have
  $H(\theta_d)\gg\varphi^{d/2}/\sqrt d$.  The remaining exponentially
  large-height trace-cancellation and exact-gcd regime is still open;
- an exact rational-ray tropical classification for those three standard
  cyclotomic units.  If
  $(m_3,m_7,m_9)=d\mathbf r+O(1)$ with
  $\mathbf r\in\mathbb Q^3$, every pairwise equality of endpoint rates lies
  on the quadratic-subfield line
  $\mathbf r=(c,c,-c)$.  Off that line there is one uniquely dominant
  embedding and the raw rational trace grows exponentially.  On the line,
  the fixed/anti-fixed decomposition resolves the only upper-wall tie: a
  non-subfield bounded offset leaves a nonzero anti-fixed leading term,
  while a subfield offset reduces to the fixed component.  Thus the raw
  trace is eventually bounded away from zero on every rational ray.  This
  statement alone does not control rational coordinate content;
- a gcd-free primitive completion on every one of those resonant quadratic
  rays.  For the uncleared trace
  $T_d=a_d(e+\pi)+b_d$ and the fully primitive form $L_d$, whenever
  $a_d\ne0$ one has the exact invariant quotient
  $$
  \frac{L_d}{A_d/g_d}=\frac{T_d}{a_d},
  $$
  so $|L_d|\ge|T_d/a_d|$ independently of denominator clearing and the
  unknown coordinate gcd.  For slopes $(c,c,-c)$ with a fixed non-subfield
  offset this quotient diverges when $c<1/4$ and, when $c\ge1/4$, tends to
  the nonzero constant
  $$
  \frac{2\pi\,\sigma_9(\xi)}
       {\sigma_1(\xi)+\sigma_9(\xi)}.
  $$
  No generated unit monomial is anti-fixed, so the denominator cannot
  vanish.  Subfield offsets are the already classified divergent reduced
  derangement forms.  An exact trace-dual description and a two-dimensional
  Smith formula further reduce the selected gcd to one primitive Lucas-type
  coordinate, but no gcd estimate is needed for this ray theorem.  Exact
  relative-trace and Smith checks through $d=200$ were rerun byte-for-byte;
- an exact primitive chamber theorem for all remaining rational slopes in
  the same cyclotomic-unit family.  If $\mu_k(\mathbf r)$ are the four
  unit-height rates, the value/coefficient quotient can decay only in the
  explicit open cone
  $$
  \mu_1-\mu_3>\log\varphi,
  \qquad \mu_1-\mu_7>\log\varphi,
  \qquad \mu_1>\mu_9,
  $$
  away from the quadratic line.  Outside that cone, a positive rate gap
  makes every nonzero primitive trace diverge.  An exact solution of all
  sixteen rational zero-gap systems proves that the only off-line zero-gap
  case has embedding $9$ dominant in both the value and its $e+\pi$
  coefficient, so their quotient tends to $2\pi$ and the primitive form is
  bounded away from zero.  Thus only the displayed coefficient-dominant
  cone remains; closing it requires a genuinely new traced-coordinate gcd
  bound;
- an exact denominator-transfer theorem inside that remaining cone.  For
  the concrete edge multiplier $\theta_d=u_7^d$, a safe integral trace
  pair is
  $$
  (D_dC_d,-d!C_d+D_dE_d),\qquad D_d={!d},
  $$
  and, with $\delta_d=(D_d,d!)$ and $D_{0,d}=D_d/\delta_d$, its selected
  Smith gcd forces
  $$
  \frac{D_{0,d}}{(D_{0,d},C_d)}\ \bigm|\ \frac{\mathcal A_d}{g_d}.
  $$
  Here $\log D_{0,d}\ge\tfrac12d\log d-O(d)$, while the primitive value
  on this ray is asymptotic, up to fixed factors, to
  $|\mathcal A_d/g_d|/(d\varphi^d)$.  Thus a subfactorial upper bound for
  $(D_{0,d},C_d)$ would close the ray.  Exact data through $d=200$ show
  only the exceptional degrees $4,8,12,28,199$ (with gcd $277$ at
  $d=199$), but this finite evidence is not the missing uniform bound;
- an exact all-prime reduction of that missing gcd on the fixed linear ray.
  Writing
  $$
  X_d=\operatorname {Tr}_{K/\mathbb Q}
       \bigl(u_7^dP_d(\eta)P_d(\bar\eta)\bigr),
  \qquad C_d=2\operatorname {lcm}(1,\ldots,d)X_d,
  $$
  one has, in every degree,
  $$
  (D_{0,d},X_d)\mid(D_{0,d},C_d)
       \mid2\operatorname {lcm}(1,\ldots,d)(D_{0,d},X_d).
  $$
  Thus the lcm changes the logarithm by only $O(d)$ and may be removed
  from the desired $o(d\log d)$ estimate.  The derangement state
  $A_d=(-1)^d {!d}$ satisfies $A_d=1-dA_{d-1}$ and has exact period $m$
  modulo every $m$.  Together with the recurrences for $P_d(\eta)$,
  $P_d(\bar\eta)$ and the three unit powers, this gives a finite joint
  state modulo every modulus.  If $p\nmid20$ and
  $f_p=\operatorname {ord}_{20}(p)$, then
  $$
  T_{p,k}=p^k(p^{f_p}-1)
  $$
  is a simultaneous period modulo $p^k$, and the common roots form an
  exact nested $p$-ary lift tree.  For $p>d$, the contribution is
  equivalent, without denominator clearing, to the two congruences
  $$
  E_d(-1)=0,\qquad
  \operatorname {Tr}_{K/\mathbb Q}
   \bigl(u_7^dE_d(-\eta)E_d(-\bar\eta)\bigr)=0\pmod {p^a}.
  $$
  The exact scan through $d=1000$ finds
  $(D_{0,d},X_d)>1$ only at $(d,p)=(8,13),(28,31),(199,277)$.
  Those records are diagnostic: periodicity makes every local question
  finite, but does not uniformly bound the total branch depth as $p,d$
  vary, so the required subfactorial gcd theorem remains open;
- an exact factorial-tail and quadratic-resultant transformation of the
  large-prime branch of that fixed ray.  With $r=p-1-d$ and
  $$
  S_{p,r}(Y)=\sum_{k=r}^{p-1}k!Y^k,
  $$
  Wilson's theorem gives
  $E_d(-x)=-x^{p-1}S_{p,r}(x^{-1})$.  The first congruence above is
  $S_{p,r}(1)=0$; writing
  $S_{p,r}=(Y-1)Q_{p,r}$ gives the simple-root identity
  $Q_{p,r}(1)=-r!\ne0$.  If $q=\eta\bar\eta$ and $z=q^{-1}$, then
  $$
  E_d(-\eta)E_d(-\bar\eta)
   =q^{p-1}\operatorname {Res}_Y
     (Y^2-zY+z,Q_{p,r})\pmod p.
  $$
  Frobenius also replaces
  $u_7^d$ by $\sigma_p(u_7)u_7^{-r-1}$.  Consequently the remaining
  condition is one trace over
  $\mathcal O_{\mathbb Q(\sqrt5)}/p$, not the vanishing of two conjugate
  factors.  In split classes it is $y_++y_-=0$; in inert classes it is
  $y+y^p=0$.  Certified nonzero cancellation witnesses occur in all four
  quotient Frobenius classes, at
  $$
  (p,d)=(13,8),(31,28),(277,199),(1879,1427).
  $$
  When all factors are nonzero the exact residue equation is a norm-one
  ratio between the two conjugates of the moving resultant and the unit
  trace.  Its factorial coefficients and characteristic both vary, so it
  is not yet a fixed-target $S$-unit equation or a uniform gcd bound;
- an exact normalization of that norm-one equation by the full visible
  factorial scalar.  If
  $$
  R_{p,r}(Y)=\sum_{k=r}^{p-1}\frac{k!}{r!}
                    \frac{Y^k-1}{Y-1},
  $$
  then the moving resultant is multiplied by $(r!)^2$, which cancels
  identically from its conjugate ratio.  The primitive polynomials obey
  $$
  R_{p,p}=0,\qquad
  R_{p,r}=L_r+(r+1)R_{p,r+1}.
  $$
  Their coefficient content is exactly one: for $r\ge1$ two adjacent
  coefficients differ by one, and the same holds at $r=0$.  Moreover
  $$
  \frac{(p-1)!}{r!}\le H(R_{p,r})
   \le(p-r)\frac{(p-1)!}{r!}.
  $$
  Hence the factorial removal leaves a primitive moving coefficient
  family of height $\Theta(p\log p)$ in proportional regimes.  This is
  only a coefficient-height statement; no comparable lower bound for the
  evaluated resultant's intrinsic height is assumed.  The map
  $x\mapsto\iota(x)/x$ is surjective onto the fixed norm-one torus in both
  split and inert residue classes, so torus membership alone imposes no
  restriction.  The remaining problem is to exploit the specific
  evaluated factorial recurrence together with the derangement root;
- an exact evaluation of that primitive factorial recurrence, showing
  that its large coefficient height disappears completely after
  specialization.  Under the derangement root,
  $$
  R_{p,r}(\eta^{-1})
   =\eta^{-(p-1)}
      \frac{P_d(\eta)}{\eta^{-1}-1},
  $$
  and likewise at $\bar\eta^{-1}$.  Therefore
  $$
  \mathcal M_{p,r}=q^{-(p-1)}Z_d,\qquad
  Z_d=P_d(\eta)P_d(\bar\eta).
  $$
  The Frobenius scalar cancels from the norm-one equation, leaving exactly
  $$
  \operatorname {Tr}_{\mathbb Q(\sqrt5)/\mathbb Q}
   \bigl(Z_dT_d\bigr)=0\pmod p,\qquad
  T_d=\operatorname {Tr}_{K/\mathbb Q(\sqrt5)}(u_7^d).
  $$
  In coordinates for $t=\zeta_5+\zeta_5^{-1}$ this is the fixed graph
  $$
  2z_0w_0-z_0w_1-z_1w_0+3z_1w_1=0.
  $$
  Its pairing determinant is $5$, so it places no ambient restriction:
  every projective $Z$ has a unique trace-orthogonal projective $T$.
  The sequence $Z_d$ has an explicit fixed order-four polynomial
  recurrence and $T_d$ a fixed order-two recurrence, but their
  prime-intersection with the derangement sequence remains uncontrolled.
  At the endpoint $d=p-1$, even excluding the derangement root alone is
  precisely the prime case of Kurepa's left-factorial conjecture; the
  additional trace condition is stronger, but cannot be discarded;
- a rigorous completion for accelerated versions of that edge.  If
  $\theta_d=u_7^{t_d}$ with
  $t_d/(d\log d)\to\infty$, a projectively normalized $S$-unit gcd
  argument proves
  $$
  \log g_d=o(t_d),
  $$
  after separately controlling both the outside-$S$ and $S$-parts and
  excluding the character-degeneracy alternatives by multiplicative
  independence.  The resulting primitive trace diverges exponentially.
  This closes every such accelerated ray, but not the arithmetically
  sharper linear ray $t_d=d$, where the moving derangement coefficient has
  height comparable with the unit exponent;
- an exact classification of what happens if the unit restriction in that
  trace construction is dropped.  For the minimally cleared pair
  $u_d(e+\pi)+v_d$ in $\mathcal O_K[e+\pi]$, the trace map
  $\theta\mapsto(\operatorname{Tr}(\theta u_d),
  \operatorname{Tr}(\theta v_d))$ has rank two for every $d\ge2$.
  Consequently its image is a finite-index lattice in $\mathbb Z^2$ and,
  after coordinate gcd division, it realizes every primitive rational
  form.  This is already explicit at $d=2$: a multiplier with integral
  coordinates $(5P,0,Q+2P,0)$ maps to $(50P,50Q)$.  Thus unrestricted
  algebraic-integer multiplication is projectively universal and imports
  the original rational-approximation/nonvanishing problem rather than
  solving it.  Exact Smith invariants through $d=200$ confirm the lattice
  calculation; the all-degree rank proof uses the fixed/anti-fixed
  decomposition and a uniform logarithmic-remainder bound;
- an exact adjoint and Hilbert-determinant audit of the central Bessel
  obstruction.  If $T$ is the lower-triangular coefficient matrix of the
  resonant ODE, $k$ its recurrence solution, and $c_j=1/(j+1)$, then
  

$$
\det\begin{pmatrix}T&e_0\\c^t&0\end{pmatrix}
  =-(\det T)\beta_m.
$$


  The corrected energy matrix
  $R=2(1/(i+j+2))_{i,j}-e_{m-1}e_{m-1}^t$ has the exact determinant
  

$$
\det R=2^m\det C
  \left(1-m\binom{2m-1}{m-1}^{2}\right),
$$


  whose last factor is $9/8\pmod p$ for $p=2m+1$.  Thus $R$ is
  nondegenerate for every $p\ge5$.  This does not settle the branch:
  retaining the degree-$p$ Frobenius anomaly gives
  

$$
k^tRk=\beta_m+(2m-1)D_mJ_m,
$$


  and, conditional on the resonance $D_m=0$, the determinant of the
  restriction to the one-dimensional solution line is an explicit unit
  square times $\beta_m$.  The Schur complement therefore loops exactly
  to the original forbidden condition; ambient Cauchy nondegeneracy is not
  anisotropy and supplies no independent exclusion;
- an exact field classification for cubic power kernels.  For
  $Q=1+x^3$, every reduced integral has the form
  

$$
R+\frac L3\log2+\frac E{3\sqrt3}\pi,\qquad R,L,E\in\mathbb Q.
$$


  Hence a rational log-cancelling combination lies in
  $\mathbb Q+\mathbb Q\,\pi/\sqrt3$, and cannot have a nonzero rational
  $\pi$-coefficient.  Even allowing coefficients in
  $\mathbb Q(\sqrt3)$ does not create an approximation: for three
  adjacent powers, all coefficientwise
  $\mathbb Q+\mathbb Q\pi$ solutions are generated by two free external
  scalars and equal $D(\alpha-\beta\pi/3)$, where the common determinant
  $D$ disappears on primitive normalization.  The mixed denominator
  $Q=(1+x)(1+x^2)$, in contrast, gives
  

$$
H=R+\frac L4\log2+\frac E8\pi.
$$


  Two neighboring powers therefore give a genuine rational $1,\pi$
  form.  If $\Delta_0,\Delta_1$ clear their three coordinates, its exact
  primitive pair is
  

$$
(p,q)=\frac{(8U,V)}{\gcd(8U,V)}.
$$


  The inversion balance is favorable for $2/3<k/n<1$, and the boundary
  ray $n=6m,k=4m+1$ has shrinking primitive values through $n=60$.
  Those values are diagnostics only.  A rational Hermite boundary survives
  on the whole half-line—for example the $n=k=2$ half-line integral is
  $1-\pi/4$—so positivity does not identify the $\pi$-coordinate.
  Accessible complex saddles and the endpoint determinant gcd remain open;
- an algebraicity-directed audit identifying the exact relation ideal and the
  collateral conjectures that a positive proof would refute;
- explicit refutations of recent manuscripts that incorrectly claim a solution.

Independent line-by-line audits accepted every claim currently labeled
proved, including both all-degree rank theorems, the nested-exponential Padé
identity and estimates, and the degree-65 $239$-adic counterexample.  They also
reconfirmed that none of these results proves algebraicity, irrationality, or
transcendence of $e+\pi$.

A subsequent exact audit of the common-kernel quotient isolates why the
tempting two-successive-minima argument is not automatic.  Two
nonproportional integer forms that tend to zero simultaneously would indeed
prove irrationality.  In the genuine real quotient norm, however, Minkowski's
second theorem says that the needed assertion is

$$
\frac{\lambda_1(D)}{\Delta_D}\longrightarrow\infty,
$$

where $\Delta_D$ is the normalized quotient covolume.  If
$e+\pi=p/q$, the exact image $8\mathbb Z\times2\mathbb Z$ contains the zero
direction $(8q,-8p)$, while every independent direction has form value at
least $1/q$.  Consequently $\lambda_2\ge1/(5q)$ and
$\lambda_1\le20q\Delta_D$.  Thus the desired first-minimum estimate already
excludes rationality and cannot be obtained from volume or transference alone.
The finite ellipsoid reductions are in fact recovering continued-fraction
convergents of $e+\pi$.

The same audit closes the two most obvious positivity repairs.  If
$(1-x)^r\mid f$ and $A(f)=f(i)=a\ne0$, then $r!\mid a$, giving a factorial
lower bound on the interval norm when $r$ is proportional to the degree.  If
$f=P^2$, Laguerre orthogonality gives $A(P^2)\ge(\deg P)!^2$, again forcing
growth under the common-kernel equality.  These are exact no-go theorems for
those ansatzes, not a no-go theorem for every nonnegative polynomial.

The replayed files are

    4fcf62e0cf809aa22a7141ba90d02eee0a221c50901f2b7cf5fa0b7ef23f0033  sources/common_kernel_two_form_quotient_audit.md
    cb15028325b9033a6e304ffc308e2aa2ba44ea7257190ff36ef5cd30b740590a  scripts/common_kernel_two_form_certificate.py
    4d6a8dd6a677bcffa7d74c4742ef5a5719477542d25c7b120f8b08ec29ba4f78  results/common_kernel_two_form_certificate.json
    61ce9226bdeaedf6e804d564f3240b96d4e07c2b18017161b23ab34235bfd5c7  scripts/common_kernel_quotient_ellipsoid_diagnostic.py
    4229e190aeba7cabe88fcf0d75377c497c1a98536b01a808c1701546162d438e  results/common_kernel_quotient_ellipsoid_diagnostic.json

There is now also a precise prime-support amplification theorem.  For
primitive pairs $(P_\nu,Q_\nu)$, $Q_\nu\to\infty$, a fixed finite prime set
$\mathcal S$, and a fixed $\eta>0$, the inequality

$$
|Q_\nu(e+\pi)-P_\nu|
(P_\nu)_{\mathcal S^c}(Q_\nu)_{\mathcal S^c}
\le Q_\nu^{1-\eta}
$$

along infinitely many pairs implies that $e+\pi$ is transcendental.  The
proof uses the exact local product

$$
\prod_v|L_{1,v}(P,Q)L_{2,v}(P,Q)|_v
=\frac{|Q(e+\pi)-P|P_{\mathcal S^c}Q_{\mathcal S^c}}{|P|}
$$

and the $p$-adic Subspace Theorem; it excludes rational and algebraic
irrational values alike.  A quantitative moving-support version applies to
blocks of $M_j$ distinct primitive points when their common number of places
$s_j$ satisfies

$$
s_j^6\log(s_j+2)=o(\log M_j).
$$

For the factorial-digit family the real-size part is already sufficient:
uniformly for every admissible $0\le b\le a+1$, the primitive form eventually
satisfies $|\Lambda_{a,b}|\le Q_{a,b}^{1/2}$.  The missing statement is now
purely arithmetic—unbounded distinct primitive heights together with support
concentration for both coefficients.  Existing Bessel radical bounds,
cyclotomic selected-gcd results, common-kernel divisibility, and quartic dyadic
denominators do not provide that two-coefficient support theorem.

The source was checked against Schlickewei's primary quantitative theorem;
two damaged TeX escapes found during integration were repaired.  Its current
hash is

    384c195a8e113a817f9bbc08ad68b9eca1733491a99508cbfc53d76d8d7c637c  sources/padic_subspace_prime_support_transcendence_criterion.md

The saturated fixed-$(N,m)$ multi-exponential Hermite--Padé construction has
also now been closed exactly.  With $U=(m+1)(n+1)$ and $L=U-1$, its type-I
remainder is

$$
R_{m,n}(z)=\sum_{j=0}^m A_{j,n}(z)e^{jz}
={z^L\over L!}\mathbb E(e^{zT}),
$$

where $T$ is an explicit Dirichlet average.  At $z=ie/N$, primitive
coefficient clearing therefore gives

$$
\log H=n\log n+O(n),\qquad \log|R|=-mn\log n+O(n).
$$

This genuine exponent-$m$ gain is not an algebraic norm.  Under a hypothetical
algebraic value $s=e+\pi$, Lindemann--Weierstrass shows that
$e$ and $Y=e^{is/N}$ are algebraically independent, so every nonconstant
form in $(e,Y)$ remains transcendental.  Fourier projection leaves one of
those generators, a Sylvester resultant leaves a polynomial in $e$, and an
$(m+1)$-row elimination consumes exactly the $m$ gained height powers.  The
canonical adjacent determinant is the exact monomial

$$
\det \mathcal A(z)=
{(-1)^{(n+1)m(m+1)/2}z^U\over
 (n+1)!^{m+1}(\prod_{k=0}^m k!)^{2(n+1)}}.
$$

After integral clearing at $ie/N$, every power of $N$ cancels and the value is
a positive integer multiple of $e^U$; at the algebraic endpoint it has full
norm at least one.  General multi-index normality and the type-II ranks follow
from the same arbitrary-pole-multiplicity residue determinant.  Thus the
fixed-$(N,m)$ type-I/type-II, norm, projection, and resultant variants do not
classify $e+\pi$.  The exact package was replayed byte-identically:

    679e8587e94f1563920bb6635b387c00732480deb1ac14d79df22df31aec6529  sources/nested_multi_exponential_hp_norm_barrier.md
    79fd558addcb9818c0138241ccdbb7eb2b660405bea4a2b31bf94ff5c3f3ce01  scripts/nested_multi_exponential_hp_certificate.py
    d04d2cedf77de24e65feaa8ded28aa15539f0fd2153d62ca17e407e6f3adc63e  results/nested_multi_exponential_hp_certificate.json

The nonnegative cone inside the denominator-free common-kernel construction
has now also been audited uniformly.  Put

$$
R=4.611581789\ldots,\qquad C_R={R\over R-1},
$$

and, for an integer polynomial $f$ of exact degree $n$ with
$A(f)=f(i)=a\ne0$, define

$$
\mathcal D_{n,r}=
\max\left\{1,\max_{1\le k<r}
 {2^{k+1}(n+1)n^{2k}\over(2k-1)!!}\right\}.
$$

An endpoint-derivative bootstrap and Bernstein--Walsh give the exact lower
bound

$$
\|f\|_{[0,1]}\ge
\max_{1\le r\le n}
\min\left\{\mathcal D_{n,r}^{-1},{r!\over C_RR^n}\right\},
$$

and hence

$$
\liminf_{n\to\infty}\|f\|_{[0,1]}^{1/n}
\ge R^{-1/2}=0.4656665\ldots .
$$

For every nonnegative polynomial satisfying the common-kernel equality this
also yields an exponential lower bound for the unnormalized positive
integral.  In particular, if its decay exponent is $\gamma>0$, the
unnormalized target coefficient must grow with exponent at least $\gamma$,
so this cone cannot beat linear-form exponent one before content removal.
The conclusion is deliberately not asserted after primitive normalization:
division by $\gcd(a,b)$ is an uncontrolled arithmetic operation, and a
primitive no-go would itself require a new gcd theorem.  Exact positive
witnesses exist, and a finite beta-cone scan through degree 40 confirms this
normalization caveat rather than removing it.  The package compiled and
replayed byte-identically:

    596e21e493f16447307764b100bae383f5a639c7ad466150a50932b4a878d487  sources/common_kernel_positive_cone_endpoint_bootstrap_barrier.md
    ca1db0bc142979bb9e566d5a93664ae3bcb914c9ec7aaa698e3f36c3b2171d4e  scripts/common_kernel_positive_cone_endpoint_bootstrap_certificate.py
    35cf99fe9eb6e4a2203d2c357a3a04b36478628bce686a4907bb3dcd6e248a3d  results/common_kernel_positive_cone_endpoint_bootstrap_certificate.json

The factorial-digit coefficient-combination route has likewise been reduced
to an exact rank-two statement.  If $V_n=(C_n,n!)^{\mathsf T}$ and
$g=\gcd(c_{a+1},\ldots,c_{a+B})$, then

$$
\operatorname{span}_{\mathbb Z}\{V_a,\ldots,V_{a+B}\}
=\operatorname{span}_{\mathbb Z}\{V_a,(g,0)^{\mathsf T}\}.
$$

Its Smith invariants are
$r=\gcd(C_a,a!,g)$ and $ga!/r$, and its projective saturation contains
every primitive rational pair.  Already two consecutive forms satisfy the
explicit identity

$$
(cQ-aT)F_{a,0}+TF_{a,1}=ca!(P,Q)^{\mathsf T},
\qquad T=a!P-QC_a.
$$

Thus unrestricted combinations can manufacture any desired prime support
only by canceling the whole factorial gain: after primitization the value is
the original $Q(e+\pi)-P$.  Coefficient boxes and sign or congruence
restrictions still have only $O(H^2)$ distinct endpoint images; their
apparent higher-dimensional collisions are exact zero forms.

For the untouched reduced denominators
$q_n=n!/\gcd(C_n,n!)$, the exact determinant identity gives, for $n<m$,

$$
m!\mid K_{n,m}q_nq_m,
\qquad 0<K_{n,m}<\frac{m!}{n!}\left(1+\frac1n\right).
$$

This proves support dispersion and forces every fixed-support survivor to be
multiplicatively lacunary.  It also isolates a particularly sharp positive
criterion: if, for some $\varepsilon>0$, infinitely many $n$ satisfy

$$
\sum_{p\mid q_n}\frac{\log p}{p-1}
\le\left(\frac12-\varepsilon\right)\log n,
$$

then the truncations violate Roth's theorem for every algebraic irrational
value, while the rational case is excluded separately, and hence $e+\pi$ is
transcendental.  In particular, infinitely many
$P^+(q_n)\le n^\theta$ with any fixed $\theta<1/2$ would suffice.  No such
friability theorem is known; this is a proved conditional criterion, not the
requested classification.  The 1,122 lattice, 495 combination, and 4,950 gap
checks replayed byte-identically:

    f245c5fa5dc9b8a673f7dd6456bfc9266913a8edb138fb40929153ee9975dae5  sources/factorial_digit_integer_combination_support_barrier.md
    ed44a627bc0cf05a7471d1db5bfe12c0c5988fa731696d8c47226b5920cf4fc9  scripts/factorial_digit_combination_support_certificate.py
    d0d684d487c13a8f533dd97f628b070ef0f622166f5f7aab34413a4732755c4b  results/factorial_digit_combination_support_certificate.json

The Bessel high-prime-power branch now has two additional uniform
structural theorems.  For

$$
q_0=q_1=1,\qquad q_n=(4n-2)q_{n-1}+q_{n-2},
$$

every odd prime $p$, $a\ge1$, and $M=p^a$ satisfy

$$
q_{n+2M}+2q_{n+M}+q_n
\equiv2p^{2a-1}q_n\pmod {p^{2a}}.
$$

Thus a root $r\bmod M$ has the exact affine lift law

$$
(-1)^tq_{r+tM}\equiv q_r+tM\delta_M(r)\pmod {M^2},
\qquad
\delta_M(r)=\frac{-q_{r+M}-q_r}{M}.
$$

If $d_M(r)=\gcd(\delta_M(r),M)$, it has exactly $d_M(r)$ children
modulo $M^2$ when $d_M(r)\mid q_r/M$, and none otherwise.  More strongly,
for $a\ge2$,

$$
\delta_{p^a}(n)\equiv\delta_p(n)-q_n\pmod p.
$$

Hence slope simplicity is inherited from level $p$: every ordinary root
has one descendant forever, whereas each singular descendant either dies or
has all $p$ children at the next exponent.  If $O_p,S_p$ count the ordinary
and singular first-level roots, then

$$
O_p\le R_{p^a}\le O_p+p^{a-1}S_p.
$$

This controls branching but not valuation height.  Even a unique compatible
$p$-adic index root can have a very long initial zero digit string, so its
least residue can be much smaller than $p^a$.  The known
$11^5\mid q_{1359}$ branch is ordinary and already exhibits why root count
and integer height are different questions.

A complementary Padé-polynomial audit proves

$$
P_n(1)Q_n'(1)\equiv(-1)^n\pmod {Q_n(1)}.
$$

Thus every argument root near $x=1$ is Hensel-simple and its distance is
exactly $p^{-v_p(q_n)}$, but
$\operatorname{Res}(x-1,Q_n)=q_n$ and
$\log H(Q_n)=n\log n+O(n)$.  Argument-root simplicity therefore merely
repackages the same main-scale integer and cannot bound the distinct index
root.  Both exact certificates replayed byte-identically:

    f08816f9bbbe96f6ea5ba09efed8d6f4dd84d69e282d699ff56622afcd06933d  sources/bessel_pade_argument_hensel_exact_no_go.md
    d25ce8aaba60055fde8a27503b4223b11f634b95e23e761761ae380e930633e7  scripts/bessel_pade_argument_hensel_certificate.py
    59f3437099aa2a483ffbb683102690009e4c1f7f39157f89d71a926a2281939f  results/bessel_pade_argument_hensel_certificate.json
    95f68e65b3a7458b869cdf610a28e77a9062e1467d78747dc2809563e84a2ee1  sources/bessel_prime_power_second_antiperiod_double_lift.md
    3ddb35fe31696478d46321b71bdf90d0b64a21ae92f4a6fbde0f286b48f19396  scripts/bessel_prime_power_second_antiperiod_certificate.py
    c9145c3911f04010a68707a5cbbf3da4f6a420e24888c173205d885e48b58115  results/bessel_prime_power_second_antiperiod_certificate.json

The index sequence has since been interpolated exactly on every
ℚ_p. For (f(n)=(-1)^nq_n), its Mahler expansion is (1)-Lipschitz,
has exact coefficient-valuation slope (1/(2(p-1))), and satisfies the
continued Bessel difference equation. On every ordinary root branch,



$$
v_p(q_n)=v_p(n-\rho).
$$



It also has the uniformly convergent hypergeometric representation



$$
f_p(x)={}_2F_0(-x,x+1;;1)
      =\sum_{k\ge0}\frac{(-x)_k(x+1)_k}{k!},
$$



with a uniform factorial valuation bound, reflection symmetry, and a
quadratic Newton coordinate. Exact truncation estimates show that this
representation cannot recover the required digit depth below the full
(n\log n) archimedean scale. Thus the remaining ordinary-root problem is
now a precise (p)-adic non-Liouville problem, rather than a missing Hensel
or Strassmann argument.

A separate root-of-unity constrained Hermite–Padé construction repairs the
endpoint generator defect. It enforces



$$
R(z)=S(z)+(1+e^z)B(z),\qquad R(i\pi)=S(i\pi),
$$



so under (s=e+\pi\in\overline{\mathbb Q}), the endpoint is a polynomial in
(e) over the fixed field ℚ(s,i). For one exponential block this is the
Padé problem for (1/(1+e^z)). All-degree moment arguments give, for fixed
(D) and (d=\lfloor D/2\rfloor),



$$
\frac{|S(i\pi)|}{H(S)}=\Theta_D((2d+1)^{-n}).
$$



For (D=2) the primitive denominator is an exact consecutive-tangent-number
quotient; on the diagonal (D=n), primitive height and inverse endpoint
value both have logarithm (n\log n+O(n)). A separately audited polynomial
lower bound at (e) shows that neither regime contradicts algebraicity of
(s): fixed degree retains factorial endpoint height, while growing degree
incurs a lower-bound exponent at least linear in the degree. These packages,
their exact hashes, and their live successor questions are frozen in
`active_checkpoint_20260827.md`.

Three subsequent reductions sharpen that picture. First, even a hypothetical
fixed ordinary Bessel root carrying almost all of (q_n) at one prime cannot
rescue the fully matched Fourier form through the (p)-adic Subspace theorem.
After primitive normalization both outside-(p) cofactors are explicit; a
singleton support set forces the real form itself to decay by a negative power
of its final height. Nonresonant valuations instead force divergence. The
previously apparent exact-resonance strip is now closed as well: a positive
super-Catalan factorization and Legendre's digit-sum formula prove



$$
v_p(B_{n,k})\log p\le \frac n2\log(8(k-1))+O_p(\log k)
  =\left(\frac12+o(1)\right)n\log n
$$



throughout every critical window. This cannot equal the
((1+o(1))n\log n) fixed-prime depth of a hypothetical main-scale Bessel
root. Together with the accepted outer-range theorems, the fully matched
critical-Fourier conversion is therefore ruled out for every (k>n). This does
not rule out genuinely non-raw auxiliary families.

Second, for every (m\ge1,n\ge2), the fixed-(D=2) root-of-unity endpoint is
an explicit nonzero quadratic governed by an equal-multiplicity multiset
Eulerian polynomial. Simion's simple-root theorem proves all-parameter
nonvanishing, and an exact pole quotient cancels the first poles
(\pm i\pi). A fixed-degree algebraic approximation measure for π then
proves that increasing (m,n) cannot make the primitive endpoint exponent
unbounded while (D) remains fixed. Coupled growing degree and determinants
of several endpoints are not covered by that obstruction.

Third, a current primary-source audit of (E)-, (G)-, logarithm-value, and
(E)-period results proves a forced-support theorem. If (e+\pi) were
algebraic, every exact pair of (E)-function representations of (e) and
π would have intersecting scaled inverse-Borel singularity sets; otherwise
Delaygue's theorem would contradict the relation immediately. Every exact
algebraic logarithm likewise lies in the exceptional branch of the current
Fischler–Rivoal theorem. The hypothesis would put both (e) and π in the
still-conjectural value-ring intersection (\mathbf E\cap\mathbf G), while
the known functional intersection does not decide that value statement. The
full reductions and authoritative hashes are in the active checkpoint.

Three later audits close the most immediate successors. The canonical
exterior Wronskian of $\nu$ independent root-of-unity endpoint polynomials
has actual degree at most $\nu(D-\nu+1)$, but the original factor
$1+e^z$ transfers smallness into only one endpoint-value column. Hence
$\nu$ small scalar values give one small determinant factor, not $\nu$;
at top exterior rank the primitive Wronskian is exactly $\pm1$. Higher
endpoint multiplicity supplies additional inherited jets, but under natural
noncollapse scales it still pays at least the linear-in-$D$ polynomial
measure cost.

On the Bessel side, the factorial-growth index sequence is excluded from
Rivoal's $\Sigma$-operator class, every finite polynomial shift form reduces
to two boundary values, and every shift determinant at an ordinary root
reduces to an ordinary residual polynomial evaluated there. Formal root
preservation pays the full $n\log n$ Bessel height; parameter jets already
contain Euler's unresolved fixed-prime factorial constant. Thus any survivor
must introduce genuinely new tail or transform arithmetic.

Finally, the explicit pair $(e^z,s-4\arctan z)$ has been reduced to a
rational rank-three system with algebraic initial data, ordinary target
point, algebraically independent functional coordinates, and differential
Galois group $\mathbb G_m\times\mathbb G_a$. Under algebraic
$s=e+\pi$, the coordinates nevertheless coincide at $1$. The companion
$E$-function construction places $\pi$ only in a Stokes/limit constant,
and its inverse Borel transform differs from the arctangent interpolant by a
rational function vanishing at the target. The missing statement is exactly
a mixed numerical connection-period injectivity theorem, not another
functional-independence calculation.

The next reduction pass identifies four exact survivors. First, the whole
integer common-kernel plane is parameterized by the Stein operator
$\mathcal TP=(1-x)P'-xP$ and one explicit Robin lattice. This even gives
positive integral Taylor residuals $(1-x)^N$ whose weighted integrals tend
to zero before the two endpoint conditions are imposed. The missing positive
construction is now precisely an all-degree Robin correction preserving that
decay. A real-part argument also rules out every nonconstant positive
combination of the Taylor blocks, so the correction must use signed monomial
coefficients while remaining nonnegative on the interval.

Second, noncanonical two-column endpoint inheritance is equivalent to the
vanishing of one explicit correction polynomial. A zero estimate forces every
such vanishing to be a polynomial-multiple degeneracy throughout the natural
range covering $m\le3$; the complete $m=1$ exception is just the square
of the old one-column remainder. Only the high-frequency regime
$m\ge4,\ n<(m-2)D$ remains.

Third, global Mahler, residue-grid Newton, diagonal Amice, and polynomial
quadratic-invariant versions of the Bessel residual problem have matching
exact barriers: the first basis term that sees the target integer already
pays the full Bessel scale, while the certified local order reaches only half
the desired depth. The live problem is a genuinely nontriangular residual
with high $p$-adic value and sub-main primitive $\ell^1$-height.
Even that residual, if constrained only by one root congruence, is exactly
circular: its coefficient lattice has determinant $p^a$, but all short
directions vanish at the target integer and the quotient is precisely
$p^a\mathbb Z$. The optimal usable weighted norm is
$p^a+O(1)$. Any remaining Bessel route must therefore add several related
places, genuinely new local equations, or structure beyond coefficient
capacity.

Fourth, every tensor, exterior, split stabilization, and endpoint-regular
rational gauge of the explicit mixed system preserves the same connection
field $\overline{\mathbb Q}(e,\pi)$. Pure $E$-coordinates forget the
logarithmic block and pure $G$-coordinates forget the exponential block.
Only genuinely non-split extensions, which introduce new iterated integrals
and enlarge the Picard--Vessiot field, remain outside this no-go. Full proofs,
certificates, and hashes are in the active checkpoint.

The next exact pass narrows those last three structural escapes. In the
high-frequency two-column problem, a hypothetical inherited pair produces a
secondary exponential polynomial in an order kernel of exact dimension
$(m-2)D-n$. This confirms that the surviving range is not removable by
variable counting. Good reduction nevertheless proves nonvanishing of the
correction polynomial for 1,762 triples through $m=20,n=16,D=12$; what is
missing is an all-parameter normality or total-positivity theorem, not more
finite rank data.

The smallest genuinely nonsplit rank-three extension can also be written
explicitly. Its monodromy has a nonzero Heisenberg commutator and its four
functional generators are algebraically independent, but its selected
connection entry is $e+\pi+K(1)$, with a new strictly positive iterated
exponential/logarithmic period $K(1)$. The uncontaminated member is exactly
the split one. Thus a larger differential Galois group alone does not provide
the missing numerical specialization theorem.

Finally, simultaneous ordinary Bessel-root congruences at any finite set of
primes collapse exactly to the single CRT condition $Q\mid B(n)$. For every
additive recurrence-special residual group, its congruence index and its
pre-existing evaluation ideal multiply to at least $Q$. Adjacent recurrence
shifts are unimodular and generate every residual polynomial. Hence neither
multi-prime CRT nor a linear recurrence sublattice discounts the primitive
height cost. The complete proofs, byte-identical certificates, and hashes are
recorded in `active_checkpoint_20260827.md`.

Two further Bessel reductions are now all-degree. First, a polynomial in the
index and one recurrence state cannot be a nonconstant first integral,
anti-invariant, or any other constant-multiplier invariant. The proof pulls a
fixed state backward through the unimodular Pad\'e fundamental matrix and uses
the transcendental limiting direction $(1-(e-1)/2,(e-1)/2)$ against the
superpolynomial growth of $q_n$. Second, the coefficient lattice for local
conditions at $n$ and $n+h$ has exact index
$PR/\gcd(P,R,h)$. The exceptionally small Bessel cross-determinant records
only common prime support; at unequal depths its valuation is the minimum,
not the sum. Thus a surviving cross-center route needs two genuinely
independent small residuals. Exact proofs and hashes are in the active
checkpoint.

The mixed-extension kernel has since been reduced to an adjoint cohomology
problem. Rational splitting is exactly
$r=(D-1)(D+q'/q-1)\phi$, and every endpoint value produced by such a
coboundary lies in—and exhausts—the span


$$
\overline{\mathbb Q}+\overline{\mathbb Q}e+
\overline{\mathbb Q}\pi
$$

. A local exponential-residue functional completely
detects whether a rational kernel is $(D-1)$-exact. Single-pole and
constant-sign kernels cannot have zero moment. All finite-pole survivors are
therefore explicit algebraic relations among two core periods, a Stieltjes
transform and its derivatives, and $1,e,\pi$; those relations remain
unproved.

The Bessel invariant result also extends to rational functions. The
recurrence substitution is a polynomial automorphism, and its transfer
growth excludes every nonconstant polynomial Darboux factor with polynomial
multiplier. Unique factorization then reduces any rational first integral to
two such factors, proving that the rational fixed field of one state is just
$\mathbb Q$. Any nonlinear survivor must use several states, a genuinely
nonlocal transform, or structure not expressible as a rational one-state
invariant. The exact packages are in the active checkpoint.

The high-frequency root-of-unity endpoint rank is no longer conjectural.
After centering, its exact endpoint matrix decomposes into
$\operatorname{sech}$- or $\operatorname{csch}$-weighted parity blocks;
Andreief's identity proves the required initial minors nonzero for all
$m\ge1$ and $n\ge D\ge2$. The two-dimensional endpoint kernel has the
predicted parity in every case. Coefficients of the remaining two-column
correction are now exact bordered minors involving alternating
Hermite-cardinal rows. A concrete negative nonconsecutive minor shows why
full total positivity cannot finish the argument. The live statement is a
sharply specified augmented-cardinal Chebyshev determinant, followed by a
primitive endpoint-height estimate. The proof, exact replay, and hashes are
frozen in the active checkpoint.

Two positive common-kernel subclasses are now sharply separated. All
Laguerre squares are rationally parameterized; integer clearing forces a
factorial endpoint coefficient, and primitive decay can occur only if the
rational output numerator absorbs a factorial-square gcd beyond the
exponential Bernstein--Walsh scale. More generally, if the endpoint target
is any fixed nonzero integer $a$, positivity of the exponential component
alone gives a uniform primitive gap $\{ae\}/|a|$. Thus fixed-target
localization is impossible even outside the square ansatz. Any remaining
positive construction must use growing targets and exceptional cross-content.

The identity $e^{i(e+\pi-r)}+1=1-e^{i(e-r)}$ also gives an exact
quantitative alternative. Under algebraicity of $e+\pi$, the left side is
a small exponential at bounded algebraic degree and height $\log q+O(1)$.
Convergents of $e$ force the sharp height exponent two. Existing uniform
Hermite--Lindemann estimates are far weaker, so this route now asks for a new
uniform endpoint exponent-two lower bound rather than another rational
approximant to $e$. Exact details and hashes are in the active checkpoint.

For growing positive common-kernel targets, primitive normalization now
splits exactly into two positive one-sided approximation errors for $e$
and $\pi$, coupled by one explicit content congruence. The continued
fraction of $e$ supplies an effective universal lower bound and shows
that any Roth-breaking family needs exceptional synchronized content. Such
content can grow linearly even when the polynomial itself is primitive: an
explicit positive family demonstrates this, but remains on one fixed
primitive ray. The unresolved positive problem is therefore not generic
positivity or denominator clearing; it is to make large synchronized content
move through genuinely improving primitive rays.

The sharpest constructive open subproblems identified are now to control,
after integer normalization, the endpoint-matched Hermite--Padé families for



$$
1,\quad e^z,\quad
16\arctan(z/5)-4\arctan(z/239),
$$



and



$$
1,\quad e^z,\quad
4\arctan\frac{\phi_8(z)}{2-\phi_8(z)},
\qquad
\phi_8(z)=z+\frac{z^7-z^8}{140}.
$$



For the Machin family, all-degree nondegeneracy and endpoint-coefficient
nonvanishing are proved, and the first unconstrained Taylor coefficient is
nonzero on the two classes $n\equiv0,1\pmod4$.  The explicit non-diagonal
slope $(N-1,1,1)$ has been eliminated, but no effective diagonal height
asymptotic, endpoint-gcd estimate, or endpoint-remainder lower bound is known.
For the original pullback, high-jet denominator clearing and two leading
layers of raw determinant content are now controlled, but all-degree rank,
endpoint nonvanishing, the full Smith divisor, and a primitive endpoint-tail
estimate remain open.  For the higher-radius composition, all-order
integrality and the analytic radius are exact, while the full
non-diagonal degree cone, all-degree determinant content, and primitive
endpoint asymptotics remain open.  A July 2026 repository preprint reports a
computer-assisted result only for ordinary diagonal normality (without
endpoint matching or the decisive size bounds); its large external certificate
was not independently rerun in this archive.

## Proof standard

A candidate proof is accepted only after:

- every external theorem has been checked with its exact hypotheses;
- no assertion equivalent to an open algebraic-independence statement is hidden
  in an intermediate lemma;
- every limiting, analytic-continuation, and zero-estimate argument is justified;
- an independent proof audit has failed to locate a gap;
- computational evidence is used only for statements with a finite certificate.

## Files

- `research_log.md`: dated derivations, candidate routes, and obstructions.
- `sources/`: literature notes, exact proofs, route audits, and the independent
  archive-wide audit.
- `scripts/`: reproducible high-precision and symbolic experiments.
- `results/`: machine-generated experiment outputs and checksums.

To resume after a Colab disconnect, read `research_log.md` and
`sources/literature_status.md`, then rerun the scripts from this directory.
The corrected simultaneous exponential--logarithm construction, its exact
arithmetic clearing and norm audit, and the independent reconstruction are in
`sources/root_of_unity_exp_log_pade_audit.md` and
`sources/independent_root_of_unity_exp_log_pade_audit.md`.

The proposed two-column root-of-unity gain has also been normalized at the
correct endpoint. The inherited object is



$$
\Delta=W(C,D)-(C\beta_D-D\beta_C),
\qquad
W(R_C,R_D)(i\pi)=\Delta(i\pi),
$$



not the correction polynomial or bare Wronskian separately. A uniform
confluent-Vandermonde denominator, the saturated endpoint Pluecker vector,
and the exact integer coefficient map for $\Delta$ are now available. Its
Smith invariants cap corrected content only when that ambient map has full
column rank; otherwise the endpoint-specific decomposable locus must be used.
Exact examples show that large correction content can disappear completely
after subtraction. The optimized Schwarz estimate doubles both analytic gain
and coefficient height, so without corrected-content, degree-collapse, or
extra-cancellation input it has the same relative exponent as one column.
The proof and replay are frozen in `active_checkpoint_20260827.md`; this is a
normalization/capacity theorem, not a transcendence proof.

The positive factor-endpoint cone has also been computed exactly through degree
seven: its unconstrained output lattice is
$4\mathbb Z\times\mathbb Z\times(1/210)\mathbb Z$. Exact Bernstein
interpolation realizes fourteen different primitive positive rays, the best
giving a rigorously positive form of size about $3.274\cdot10^{-13}$, while
the realizing integer polynomial stays monic and primitive. This demonstrates
that very large cross-content can coexist with positivity and changing rays,
but the list is finite; it is not an irrationality proof.

For the root-of-unity branch, the shifted-coordinate minor obtained after
deleting the constant column is now proved nonzero for every parameter. The
other bordered factor has been reduced exactly to strict complete monotonicity
of explicit rational Hermite-cardinal functions. Ordered repeated-node Newton
positivity proves this criterion on a substantial exact finite grid, but its
all-parameter form remains open. Moreover, nonvanishing of the correction
polynomial would still not by itself settle nonvanishing or primitive height of
the corrected endpoint polynomial. The full statements, limitations, replays,
and hashes are in `active_checkpoint_20260827.md`.

The positive factor-endpoint cone is now classified completely. Its real output
is the origin together with the strict half-plane
$(e+\pi)a+c>0$, and every primitive lattice point in that half-plane is
realized by a primitive positive integer polynomial. Therefore a shrinking
sequence in this whole cone exists exactly when $e+\pi$ is irrational. This
turns the route into an exact universality/circularity theorem: cone density,
positivity, and realizability alone cannot establish the missing irrationality.
The proof and replay are frozen in `active_checkpoint_20260827.md`.

The missing all-parameter cardinal positivity theorem has now been proved by a
canonical-product pole-truncation argument. It gives strictly positive ordered
Newton coefficients for the cosine, sinc, and parity-defect cardinal families,
and hence proves $\Gamma\ne0$ for every $m\ge2,n\ge D\ge2$. This closes
the correction-border nonvanishing question. It does not yet prove that the
corrected polynomial $\Delta=W-\Gamma$ survives cancellation, nor does it
provide the primitive height/value inequality required for transcendence. The
proof, exact replay, and logical boundary are frozen in the active checkpoint.

The top cardinal row also determines the exact leading degree whenever parity
permits it. In those regimes $[z^{n+D}]\Gamma\ne0$, so the shorter bare
Wronskian cannot cancel it and $\deg\Delta=n+D$. Only two parity-forced
families remain outside this degree theorem; their next coefficient is a sum of
two bordered minors with a genuine comparison issue. The proof, primary-source
check, exact replay, and precise parity classification are in the active
checkpoint. Corrected nonvanishing by itself still does not meet the required
primitive-height/value threshold.

The cardinal Newton coefficients now also have a complete arithmetic audit.
Their least denominators are trapped between explicit local-jet and confluent-
Vandermonde factors, while primitive numerator height is at least the least
denominator. Intrinsic content is at most two in the integer-rate coordinates,
but the even-family return to the endpoint variable can restore a dyadic factor
as large as $2^{2(k(n+1)-1)}$; an exact row has content $2^{32}$. These
facts rule out treating cardinal denominator clearing as the missing corrected
content. They do not control the saturated Pluecker vector or $W-\Gamma$.

Corrected nonvanishing is now proved for every even $m$. The constant border
replaces the centered cardinal numerator $N$ by $N+2$; its ordered Newton
expansion remains a nonzero positive reciprocal-suffix sum, even when its first
coefficient becomes zero. Combined with the top-degree theorem, the only
unresolved universal nonvanishing family for $m\ge2$ is $m$ odd, $n$
even, $D$ odd. This sharpens the analytic construction but does not resolve
its primitive-height/content barrier.

The last odd-frequency family now has an unconditional all-parameter solution
at endpoint degree $D=3$. A phase rederivation changes the relevant identity
to $V\sigma=V\psi-\mathcal E(V\rho_+)$ and shows that the two normalized
borders carry opposite prefactors. At $D=3$, their difference is exactly a
covariance between the strictly increasing Euler density ratio and the strictly
decreasing first csch derivative polynomial. Its sign reinforces the strictly
positive Stieltjes border, proving $[z^{n+2}]\Gamma\ne0$, and hence
$[z^{n+2}]\Delta\ne0$, for every odd $m\ge3$ and even $n\ge4$. Odd
endpoint degrees $D\ge5$, as well as corrected primitive height/content,
remain open; the proof and exact replay are frozen in the active checkpoint.

The same parity-forced family is now completely resolved for three frequencies.
For $m=3$, every even $n\ge4$, and every admissible odd $3\le D\le n$,
a special one-border total-nonnegativity factorization proves
$[z^{n+D-1}]\Gamma\ne0$, hence $\deg\Delta=n+D-1$. The proof factors the
two endpoint coefficient matrices into elementary TN blocks, interpolates the
actual factorial residue parameter through the single border row, composes with
an exact reverse-TP csch moment kernel, and compares the two normalized borders
by a terminal-flag ratio lemma. The phase was also checked directly against the
original Hermite-cardinal determinants. This closes all endpoint degrees only
for $m=3$; odd $m\ge5$ and the decisive corrected primitive-height/content
estimate remain open. The theorem, replay, and hashes are frozen in the active
checkpoint.

The remaining odd-frequency, even-$n$, odd-$D$ family is now closed for
all frequencies and endpoint degrees. A new external-node reproducing-kernel
lemma proves the strict polewise comparison



$$
\operatorname{NB}_A\!\left(\mathcal E\frac{V}{x+a}\right)
 <\operatorname{NB}_G\!\left(\mathcal E\frac{V}{x+a}\right)
 \qquad(a\ge0).
$$



The proof represents the difference polynomial as a negative sum of evaluation
kernels at $-1^2,\ldots,-k^2$; an explicit Schur/Andreief determinant shows
that every kernel has a positive Stieltjes transform, including at the central
Laurent pole. Positive cardinal residues then give
$[z^{n+D-1}]\Gamma\ne0$ and $\deg\Delta=n+D-1$ throughout the forced
family. Together with the preceding parity theorems, corrected exterior
nonvanishing is proved for every $m\ge2,n\ge D\ge2$. The remaining obstacle
to a classification of $e+\pi$ is arithmetic rather than nonvanishing: the
construction still lacks the required corrected primitive-content,
saturated-height, and endpoint-value inequality. The reduction, theorem,
independent audit, exact replays, and hashes are frozen in the active checkpoint.

The certified leading/next-leading coefficients now also give a
rank-independent arithmetic consequence. If $N=q_E\Delta$, then the gcd
$G_{\rm cert}$ of the certified high tail (together with the certified
constant coefficient when $m$ is even) is nonzero and satisfies



$$
\operatorname{cont}(N)\mid G_{\rm cert},\qquad
 H\!\left(N/\operatorname{cont}(N)\right)
 \ge \frac{H(N)}{G_{\rm cert}}.
$$



Each selected coordinate has an exact saturated augmented-determinant formula,
so the cap remains valid when the ambient corrected map is rank deficient.
After universal clearing it yields a necessary, rank-independent test for the
item-39 primitive-content threshold. It does not improve the asymptotic
error-versus-height exponent: exact examples show that $G_{\rm cert}$ can
still exceed the true content by factors $729$ and $128$. Thus the result
sharpens a failure certificate but neither proves the threshold nor classifies
$e+\pi$. The proof, exact replay, and manifest are
`sources/root_unity_certified_coefficient_content_cap.md`,
`scripts/root_unity_certified_coefficient_content_cap_certificate.py`, and
`results/root_unity_certified_coefficient_content_cap_hashes.sha256`.

## Root-of-unity checkpoint items 52--57

Item 52 gives an infinite dyadic arithmetic theorem on
$m=3,D=2,n+1=2^q$. The saturated exterior vector is
$e_0\wedge e_2$, and the leading corrected coefficient has exact valuation



$$
v_2([z^{n+2}]\Delta)=-2(n+1).
$$



Consequently the intrinsic denominator contains $2^{2(n+1)}$, while the
minimal-clearing corrected content is odd and divides an explicit numerator of
logarithmic size $O(n\log n)$. This is a real corrected-content cap, but a
single coefficient can remain primitive of size one; a second-coefficient gcd
or full intrinsic-content theorem is still missing.

Item 53 supplies the basis-free corrected asymptotic ledger: universal
Wronskian and endpoint-height majorants linear in the primitive Pluecker height,
the exact corrected-content threshold, and the conditional
$\binom\nu2>n+D-d$ exterior/Siegel regime. Its arithmetic height, content,
degree, and dimension bookkeeping remains current. Its uncentered analytic
gain is superseded by item 55 and must now be replaced by



$$
\mathcal G_{\rm ctr}
  =(L-n)\log\frac{2(L-n)}{e\pi m}-n\log\pi.
$$



The larger centered gain still does not overcome the universal denominator or
the $n^2\log n$ Cramer interpolation scale.

Item 54 identifies unconstrained odd/even endpoint collapse as an exact Segre
section. Reflection makes
$\widehat\beta=\beta+(m/2)I$ parity reversing, and high corrected
coefficients are hyperplanes on
$\mathbb P^{d-1}\times\mathbb P^d$. At $m=2$, the complete quadratic
sections have closed-point degrees $1+2$, $4+6$, and $15+20$ for
$n=4,6,8$. Thus the rational quadratic branch at $n=4$ already fails at
$n=6$. Quartic output yields a rational line at $n=6$ and a rational point
on a genus-six component at $n=8$, but no infinite rational descent or small
primitive endpoint family.

Item 55 corrects the exterior Schwarz estimate by centering frequencies:
$e^{-mz}F$ has frequencies $-m,\ldots,m$, unchanged coefficient height and
origin order, and endpoint multiplier $(-1)^m$. The stationary radius doubles
to $2(L-n)/m$, adding $2(L-n)\log2$ to the total exterior gain. An
all-parameter proof nevertheless gives



$$
2\mathcal G_{\nu,{\rm ctr}}<\log Q_{m,n},
$$



so centering improves finite constants but not the leading obstruction.

Item 56 proves the exact centered reflection reciprocity



$$
e^{mz}R_C(-z)=(-1)^m\sigma_CR_C(z),\qquad
 G_p(-z)=-\tau G_p(z).
$$



It pairs opposite frequencies into explicit hyperbolic terms and adds one
uniform origin zero in same-parity exterior blocks, or three in the favorable
single block. The resulting factor remains asymptotic to $e^{mR}$, however;
reflection improves only finite prefactors and $O(\log n)$ origin-order terms,
not exponential type or leading capacity.

Item 57 validates genuinely nondecomposable exterior sums. For arbitrary
$p\in\bigwedge^2E_\nu$, the endpoint identity and order



$$
\mathcal W_p(i\pi)=\Delta_p(i\pi),\qquad
 \operatorname{ord}_0\mathcal W_p\ge2L_\nu
$$



remain exact. A usable fixed-degree endpoint exists precisely when the full
corrected-map rank exceeds the high-tail rank. Dimension counting fails
exactly at $(m,n,D,\nu,d)=(2,11,11,7,2)$, while $\nu=8$ rescues the
gap. Universal parity-maximality is also false at $(m,n,D)=(2,21,7)$, though
that tuple retains a rank gap of three. The selected skew ranks $4,6,8$
prove that these are not hidden single wedges. Full-endpoint basis height one
removes one lattice cost, but the current interpolation majorant remains on the
$n^2\log n$ scale and every certified centered finite margin is negative.

All six sources, deterministic certificates, JSON results, replay metadata,
and SHA-256 manifests are recorded as items 52--57 in
`active_checkpoint_20260827.md`. The manifests have been reverified. These
items sharpen the surviving rank and intrinsic-height questions; none proves
that $e+\pi$ is rational, irrational, algebraic, or transcendental.

## Root-of-unity checkpoint items 58--61

Item 58 proves the endpoint-displacement square/product theorem. For every
$m\ge2$ and $n\ge m+1$, it constructs a primitive polynomial
$C_{m,n}$ of degree $m$, except degree $m-1$ when $m$ is odd and
$n$ is even, with



$$
R_{zC_{m,n}}=zR_{C_{m,n}},\qquad
 W(R_{C_{m,n}},R_{zC_{m,n}})=R_{C_{m,n}}^2,\qquad
 \Delta(C_{m,n},zC_{m,n})=C_{m,n}^2.
$$



The corrected endpoint is primitive of degree at most $2m$, the analytic
square has order at least $2m(n+1)$, and polarization proves an
all-parameter product-space rank gap at target degree $2m$. Intrinsic
normalization cancels the universal $Q^2$ clearing exactly. The current
cofactor/remainder height bounds remain too large, however, and all fourteen
finite $m=2,3$ measure margins are negative. The conservative replay took
about 31.5 seconds and used 971,304 KiB (about 948.54 MiB) peak RSS.

Item 59 derives the exact endpoint map for arbitrary, genuinely
nondecomposable third exterior sums. The corrected jet is



$$
\Delta^{(3)}
  =\det(\mathbf C,\mathbf C'-\boldsymbol\beta,
        \mathbf C''-\boldsymbol\beta-2\boldsymbol\theta),
$$



with endpoint identity
$\mathcal W^{(3)}_p(i\pi)=\Delta^{(3)}_p(i\pi)$, origin order at least
$3L_\nu$, and centered type $3m/2$. The domain has dimension
${\nu\choose3}$, so fixed-degree tail elimination permits
$\nu=\Theta(n^{1/3})$, but a strict full-versus-tail rank gap is still
required. The exact normalization is



$$
Q^2\Delta^{(3)}_p\in\mathbb Z[z],\qquad
 \overline{\mathcal W}^{(3)}_p=Q^3\mathcal W^{(3)}_p.
$$



Thus the present universal height majorant retains two copies of $Q$;
tripling the analytic gain does not improve the matched per-column threshold.
The four replayed rank gaps are finite diagnostics only. Replay took 8.574
seconds and 70.887 MiB peak RSS.

Item 60 gives an exact saturation theorem for the complete global $k=2$
Wronskian image. If $UR^t=[H_0;0]$ is a transformed tall HNF, then



$$
S=(U^{-1}_{[:,0:r]})^t,\qquad
 R=H_0^tS,\qquad
 [L_{\rm sat}:L_{\rm raw}]=|\det H_0|.
$$



The index also equals the product of the nonzero Smith invariants, the gcd of
the maximal minors, and the raw-to-saturated covolume ratio. If $g$ is the
common entry content, the index factors as $g^rI_{\rm cross}$. The exact
compatibility $\mathcal E(Gx)=Q\,Nx$ proves that saturation preserves
high-tail cancellation. On the ten-row representative grid, the repeated
scalar accounts for at least $96.3970\%$ of the logarithmic index, and the
saturated LLL scales are consistent with $O(n\log n)$. This is finite
evidence, not a uniform height theorem or SVP certificate. Two deterministic
runs produced byte-identical JSON; the conservative run took 32.004 seconds
and 240.594 MiB peak RSS.

Item 61 proves that Gaussian mixing of the even and odd endpoint blocks is an
exact real phase descent but not an exponent gain. If
$\widetilde N=N_{\rm e}-iN_{\rm o}$, then



$$
\widetilde N(z)=A(-iz),\qquad \widetilde N(i\pi)=A(\pi)
$$



for an ordinary integer polynomial $A$ with exactly the same primitive
content and height. Under the temporary assumption that $e+\pi$ is
algebraic of degree $r$, the fixed-degree measure cost remains
$r^2d+r-1$, with strict relative threshold $r^2d+r$. Full-rank
Dirichlet approximation reaches only relative exponent $d+1$: equality,
not contradiction, when $r=1$, and a strict deficit when $r>1$. The
26 exact lattice rows confirm finite joint-rank enlargement but prove no
all-parameter rank or height statement. Replay took 1.122126 seconds and
73,280 KiB (71.5625 MiB) peak RSS.

The frozen item-58 through item-61 SHA-256 records are:

~~~
1883582877ed7f9b7fb6fdf7c99d66fa933bb9040f165cfdbab3bbcb2ca44e8b  sources/root_unity_endpoint_displacement_square_theorem.md
4bda9773163ec63cd4df868d1f0032cade310ea1525952540b1806aef214cb25  scripts/root_unity_endpoint_displacement_square_certificate.py
68be9373f11cef9a734a18412b091f4ec555c6aed582301e41c777dc9acd885a  results/root_unity_endpoint_displacement_square_certificate.json
84d6549d8293ddd022ff875b2bae47921b1db547a64b15606b1528e26d30d964  results/root_unity_endpoint_displacement_square_hashes.sha256
6f0b2d7908da9f6b67135468e5e8744bbd9f1785963361dcd21a8d8e0923a281  sources/root_unity_third_exterior_sum_endpoint_audit.md
94623603b6bbe14dbdd736e04c595408d3af28dd1db71d31aa17f8178c64faac  scripts/root_unity_third_exterior_sum_certificate.py
3d09b003816d84ba655e2de8f497494e6115e15bb995c93da2975cf0a07b370c  results/root_unity_third_exterior_sum_certificate.json
16f8e44aa10be4345aae9de08b3c179d9ec381f30c8f9194d0faa6f709eb0492  results/root_unity_third_exterior_sum_hashes.sha256
cc56e51aa5ce1f7f1dadb2c10edf96fbdacadb2ca660f20130f2b57dec4f13ab  sources/root_unity_k2_global_image_saturation_audit.md
588393ba1cb273d13034cc069cca7b3f507c8b9adf62f13a8d6e8e71bb15d470  scripts/root_unity_k2_global_image_saturation_certificate.py
b66a378153646894f7bc923892f8ee50bb2dc8a665a56030a545d6d0488f1c92  results/root_unity_k2_global_image_saturation_certificate.json
72f63950f3e197f921bb256e84f6938fb7713a253183bf46e83a381cd2942e4f  results/root_unity_k2_global_image_saturation_hashes.sha256
fbfb6fba663768b80364462608d0267d233d1828924b9d25f12dd9a7a1ea4b6d  sources/root_unity_gaussian_parity_mixing_barrier.md
a338633131005b021bd8acd0a1edf9ca69fa21fc2af2ae2f0ba517be1e843143  scripts/root_unity_gaussian_parity_mixing_certificate.py
70a4df592056f424a481ca6da7a8d6b6c803f43d8c59c8103a24b5f3a0317c02  results/root_unity_gaussian_parity_mixing_certificate.json
74c2d5fab03af9520d7f7cb480c6ce3fd490ce2b26a0769c337672605d4eb280  results/root_unity_gaussian_parity_mixing_hashes.sha256
~~~

All four manifests have been reverified. These items sharpen the available
construction, normalization, and obstruction theorems, but none proves that
$e+\pi$ is rational, irrational, algebraic, or transcendental.

## Root-of-unity checkpoint items 62--64

Item 62 proves an explicit all-parameter quadratic survivor for $m=2$.
For every $n\ge5$, three lower-excess-kernel endpoints



$$
E_0=B-Az^2,\qquad E_1=C-Az^4,\qquad O=g_3z-g_1z^3
$$



combine as



$$
P_n=(2Ag_1g_3-Bg_1^2)E_0^2-Ag_1^2E_0E_1+A^3O^2
     =p_{0,n}+p_{2,n}z^2,qquad p_{0,n}p_{2,n}>0.
$$



The global image has frequencies $0,\ldots,4$, degree at most $2n-2$,
and order at least $4n+4$. Hyperbolic-secant covariance and an exact Fourier
anchor prove nonvanishing uniformly. An explicit integral representative has
$\log H\le16n\log n+O(n)$, establishing the intrinsic $O(n\log n)$ scale
without a gcd hypothesis. If $\chi_n$ measures the exact endpoint content,
the current leading ledger is $(10-\chi_n)$ for endpoint height,
$(14-\chi_n)$ for normalized analytic height, and only $2$ for analytic
gain. Even formally maximal content leaves a deficit of $2n\log n$; this is
a limitation of the proved majorant, not of the true saturated lattice.

Item 63 proves that the unphased even/odd saturation has only $2$-primary
glue, while the phase-aligned Gaussian fixed lattice is exactly



$$
S_{\mathbb G}^{\sigma=1}=S_+\oplus iS_-
$$



with index one. A $(1+i)$-cleared glue vector becomes projectively identical
to the separately aligned doubled vector after endpoint-content normalization.
Moreover every rigorous coefficientwise centered majorant for a genuine mix
dominates each component, joint content is their gcd, and joint height and
degree cannot decrease. Thus Gaussian global saturation adds exactly zero
optimized coefficientwise measure margin beyond the better separate parity
block. Whole-function interference and exceptional successive minima inside
one block are not ruled out.

Item 64 supplies the exact Hardy--$H^2$ replacement



$$
\langle z^ae^{rz},z^be^{sz}\rangle_R
 =\sum_{\ell\ge\max(a,b)}
 {R^{2\ell}r^{\ell-a}s^{\ell-b}\over(\ell-a)!(\ell-b)!},
$$





$$
|F(i\pi)|\le{\pi^K\|F/z^K\|_{2,R}\over\sqrt{1-\pi^2/R^2}}.
$$



On an endpoint fiber $B^tx=p$, its exact real quadratic minimum is the
Schur complement $p^t(B^tA^{-1}B)^{-1}p$. Rational points have the same
infimum, but this gives no denominator bound. At $n=5,8,10$, the finite
Hardy diagnostics improve the coefficientwise bound for the same functions by
15.48, 30.13, and 36.05 log units. The best $n=8$ relative exponent is only
$1.21038<3$, and the observed savings do not prove a changed $n\log n$
leading constant.

The frozen item-62 through item-64 SHA-256 records are:

~~~
47045420f729a14eb7eaf655988add44332db26091b837a9d24dfaed7d39c868  sources/root_unity_m2_quadratic_saturated_survivor_theorem.md
1ec66622c212bb27d7729e1b9e2d7519d355bbe755f40b239343172926b8a7fe  scripts/root_unity_m2_quadratic_saturated_survivor_certificate.py
9a44bea7db63f8f994a01bcaf284a9319f05050bc28c84c7c71fb889ee483274  results/root_unity_m2_quadratic_saturated_survivor_certificate.json
d5faaf65094d19b9a20fd178ee35de76a0fb37b8aa6399c8ec76491c87967880  results/root_unity_m2_quadratic_saturated_survivor_hashes.sha256
08c282e9ebd933b8b4def6806f9d6db1fb13e445c6b9ce1f6d57690c92162b9a  sources/root_unity_gaussian_global_saturation_no_gain.md
89004cd7c35e890803f486f3a69036d21980497c718b75ad78be4441335e4f5a  scripts/root_unity_gaussian_global_saturation_certificate.py
607cf35c54cf16f6da870b0b933c217388b8eb551132e07a8500ae95f0a78837  results/root_unity_gaussian_global_saturation_certificate.json
49d4d2e40a9cb421be3f409ca94129c487b5de3c685e8fe88fe6c39dd7fabbb7  results/root_unity_gaussian_global_saturation_hashes.sha256
24bc6c1e633118bec00659ed625d52266079555559c567e123d5d55943bc8a81  sources/root_unity_hardy_h2_saturated_circle_audit.md
8cd98734331b75ea26990759c5d13a8d022065340feb1ef5cea4871452912b6b  scripts/root_unity_hardy_h2_saturated_circle_certificate.py
a14b1af4b11b6760839b9237eaeb854156be6cc4588ffc83f656d9ed97347db2  results/root_unity_hardy_h2_saturated_circle_certificate.json
f5d80a9962ed914662be782301319b7d786aa6874510b876a5d24a54d9f3cbd4  results/root_unity_hardy_h2_saturated_circle_hashes.sha256
~~~

All three manifests were independently reverified before this central update.
These packages improve the construction, intrinsic arithmetic scale, and
analytic norm, but none proves that $e+\pi$ is rational, irrational,
algebraic, or transcendental.

## Root-of-unity checkpoint item 65

Item 65 gives the exact rational quotient formulation of fixed-endpoint
coefficientwise optimization. For a rational right inverse $\Lambda$ of
the endpoint map and a rational row basis $K$ of its kernel, the fiber is
$b+tK$, and its weighted-$\ell^1$ infimum is the corresponding rational
linear-program infimum. Rational points are dense in the real fiber, but
this theorem gives no denominator bound and does not turn a merely feasible
rational point into a certified optimum without an exact dual witness.

For the exact finite instance $(m,n,D,d,R)=(2,8,7,2,13)$, endpoint
$(5441060864,0,551294727)$, the saturated global image has rank $11$ and
the endpoint-zero kernel has rank $8$. An exact kernel direction disproves
the temporary optimum claim through the negative one-sided derivative



$$
-{39710900240730900314101\over17036837675827200}.
$$



The descended feasible point still has degree-two margin
$-60.72193402085388\ldots$. More importantly, clearing its rational global
coordinates forces endpoint multipliers
$6518378303365776642144000$ and
$645319452033211887572256000$ in the two audited representatives; their
cleared global contents are both one. This is an exact finite demonstration
of integral clearing cost, not an asymptotic theorem. Item 69 proves that
this cost is irrelevant to endpoint-only Hardy and weighted-$\ell^1$
Schwarz quotient bounds; it matters only if global integrality is required
for a separate reason.

The frozen item-65 SHA-256 records are:

~~~
070aa86143f9970c7925a07377fe1ff8f795992c8057e98505c6fc137f83f5e9  sources/root_unity_k2_exact_quotient_lp_audit.md
1f9ef63de854211c31bde2575cdc20d2271aae33e59f45d8810099c94af84a6c  scripts/root_unity_k2_exact_quotient_lp_certificate.py
a0e2a8d3d3c5db6904c713913ab5a441d72785931cb4e62c77fe7bfdae9fac1a  results/root_unity_k2_exact_quotient_lp_certificate.json
cebc31286ee464728467d9584ef729c667111cb2b69e1f6f9bb10ed5488065a4  results/root_unity_k2_exact_quotient_lp_hashes.sha256
~~~

The repaired package was independently checked for payload hashes and stray
control bytes. It supplies an exact optimization framework and concrete
integral-clearing data. Its former endpoint-obstruction interpretation is
superseded by item 69, and it gives no classification of $e+\pi$.

## Root-of-unity checkpoint items 66--67

Item 66 develops the half-phase centered-cosh lift. Multiplication by $z$
has exact rank-one displacement,



$$
P_n[zC]-zP_n[C]=[z^n](C/(2\cosh z))z^{n+1}.
$$



On its kernel, $R_n[zC]=zR_n[C]$, so the exterior Wronskian is the exact
square $R_n[C]^2$; polarization gives symmetric products. Killing $t+1$
tail jets guarantees a nonzero product endpoint of degree at most $2t+2$.
The stronger quadratic pattern $t=\lfloor(n-1)/3\rfloor$ is certified only
for $5\le n\le20$. Its optimistic asymptotic ledger still requires an
unproved survivor-specific quotient/Smith theorem and content constant
$\chi>13/9$.

Item 67 closes the whole-circle interference caveat for Gaussian parity
mixing. If $U,V$ have opposite reflection parity and $W=U-iV$, then



$$
|W(z)|^2+|W(-z)|^2=2(|U(z)|^2+|V(z)|^2).
$$



Thus $\|W\|_\infty$ dominates both component suprema, while
$\|W\|_2^2=\|U\|_2^2+\|V\|_2^2$. This remains true after division by any
common origin zero, and different component orders only strengthen the
comparison. Joint content, height, and degree then prove exact supremum- and
Hardy-margin no-gain across parity blocks. Single-parity minima remain open.

The frozen item-66 and item-67 SHA-256 records are:

~~~
8794eaeb7a8cf5f0c7e749c85afc67b2403b3dc6e3e752353bbf0ab020059581  sources/centered_cosh_lower_lift_product_audit.md
da827921d2621821553ed8bee069428638539fa5bb6b952c4636782d2b5aef71  scripts/centered_cosh_lower_lift_product_certificate.py
f3425385637efaa329f67a133c89844ac8a2a3a92603838ffe0e92c8ca1844bf  results/centered_cosh_lower_lift_product_certificate.json
51e0523cf8ce702885deb20d703ddd615cc15e645fe96fba2c35ce0c2ec54a92  results/centered_cosh_lower_lift_product_hashes.sha256
6e979114a2d4a043e41fe6dcf6031d3c98eb86c434b3c8825c3b8aa1589ba412  sources/root_unity_gaussian_antipodal_no_gain_theorem.md
880e284b923fbeb911509bc2970d79b37434781d7eb002454408294661d81d79  scripts/root_unity_gaussian_antipodal_no_gain_certificate.py
1fa52598c244019d9892255d54deccbeb56ef0ed86b9d7c6496c2647049ebe8f  results/root_unity_gaussian_antipodal_no_gain_certificate.json
e6df57e7016a60e0154fba90a849ec34d707d691135d8bc04142c06a2abca15c  results/root_unity_gaussian_antipodal_no_gain_hashes.sha256
~~~

Both manifests were independently replayed and reverified before this central
update. These theorems narrow the surviving arithmetic problem but do not
classify $e+\pi$.

## Root-of-unity checkpoint item 68

The closer-root family $R=C+2\cosh zP$, evaluated at $i\pi/2$, is normal
for every $n,D$. Writing $N=\lfloor n/2\rfloor$,
$K=\lfloor D/2\rfloor$, its endpoint is, up to the forced parity monomial,
the $[N/K]$ Padé denominator of $1/(2\cosh\sqrt x)$. Positive Schur
minors prove all-parameter normality and the exact remainder order.

For fixed $K$, the primitive relative endpoint is



$$
c_K(2K+1)^{-2N}\{1+O_K(((2K+1)/(2K+3))^{2N})\},
$$



with explicit rational $c_K>0$. The quadratic case has an exact
Euler-number/gcd formula and beta quotient asymptotic
$8/3^{2N+3}$. On the diagonal, Dzyadyk gives relative gain
$4N\log N+O(N)$, but a Catalan-Hankel 2-adic theorem proves that mandatory
clearing is primitive with height at least $16^N$. The resulting exponent
is only $O(\log N)$ against endpoint degree $2N+O(1)$. Integer-frequency
dilation is neutral after primitive clearing; the genuinely new centered
class has half-integral frequency.

Frozen hashes:

~~~
f837e5be64de4985e721f9e5d3731e6d13e01c41fa973a937c4bc1dce0977ecf  sources/root_unity_closer_root_sech_pade_audit.md
8a97f86cc74314ead643e34a8ccc7d1d7bd0c2502122c3da1143862d686c64b6  scripts/root_unity_closer_root_sech_pade_certificate.py
f16f21e3ebf0a52b66a201f29ebe6875e0b094c65077b0e800ce14278d7bba5e  results/root_unity_closer_root_sech_pade_certificate.json
53d611d1478c66290b05a683d9eb7ff3936f88228cc45bac36628b3019f7d117  results/root_unity_closer_root_sech_pade_hashes.sha256
~~~

The package was independently replayed and reverified. It does not classify
$e+\pi$.

## Root-of-unity checkpoint item 69

Item 69 corrects the denominator interpretation of items 64--65. A real
Hardy minimizer in an exact primitive endpoint fiber is a valid entire
auxiliary function: the common zero and endpoint identity are complex-linear,
and the conditional lower bound sees only the primitive integer endpoint
polynomial. Rational fiber points are dense, so insisting on rational
auxiliary coefficients introduces no denominator term. The same observation
applies to the homogeneous weighted-$\ell^1$ Schwarz quotient.

The exact binary quotient geometry is



$$
{Q_R(p_0,p_2)\over a}
 =(p_0-\pi^2p_2+\eta p_2)^2+\tau p_2^2,
$$



and therefore



$$
\left|{\sqrt{Q_R(p)}\over\sqrt a\,|p_2|}
 -\left|\pi^2-{p_0\over p_2}\right|\right|
 \le\sqrt{\eta^2+\tau}.
$$



Thus collapse of the quotient form to evaluation does not itself create a
new Diophantine exponent: it reduces endpoint selection to rational
approximation of $\pi^2$, up to the collapse floor. Continued-fraction
balance reaches exponent two, while the rational-$e+\pi$, degree-two
contradiction needs a strict approximation exponent above three. The finite
collapse floors through $n=12$, and the separate $n=14$ Hardy row, are
very small/tight but prove no asymptotic or exceptional approximation theorem.

Frozen hashes:

~~~
5bd489df02183a374145d889ca96a6d2f3940ba141af0592962920021fc3a901  sources/root_unity_hardy_endpoint_quotient_geometry_correction.md
1b99140f9a2d36731364847254e578526cbfafeca12c19aed992704c8231cac9  scripts/root_unity_hardy_endpoint_quotient_geometry_certificate.py
14019a29cd3af0e41130ddfc71f927ab9969be394e98ca7903571118d97cdcec  results/root_unity_hardy_endpoint_quotient_geometry_certificate.json
88b5cef191c3231286d4a9160986e797000869d7ee0e897d6ff252e053562469  results/root_unity_hardy_endpoint_quotient_geometry_hashes.sha256
fe388e4445efd3e1ee961707c0c230768d6e2d3745da3b44831ca53e22294fc5  scripts/root_unity_hardy_h2_even_n14_diagnostic.py
3472669cf21abc9cc0edcc41a1bb18c061b58b6fc62f490bddd3c739b7128a3c  results/root_unity_hardy_h2_even_n14_diagnostic.json
36c2727e4f971663811439f5920381483d30d5ec154e3946c9c45b8226d785b2  results/root_unity_hardy_h2_even_n14_diagnostic_hashes.sha256
~~~

The main certificate was replayed twice byte-identically and independently
reverified. Item 69 removes an irrelevant arithmetic charge but leaves the
genuine endpoint-approximation problem unresolved.

## Root-of-unity checkpoint item 70

Let $Q_q$ be the diagonal $[q/q]$ Pade denominator of
$F(x)=1/(2\cosh\sqrt x)$. For the balanced centered-cosh product images at
$n=3q+r$, $D=n-1$, the following inclusions now hold for every parameter
in their stated ranges:



$$
Q_q\mathbb Q[x]_{\le2q}\subseteq{\cal E}_{q,1}\quad(q\ge2),
 \qquad
 xQ_q\mathbb Q[x]_{\le2q}\subseteq{\cal E}_{q,2}\quad(q\ge1).
$$



Dualizing gives an exact $Q_q$-recurrence for every annihilator of the
product image. The proof uses Pade division and controllability in
$\mathbb Q[x]/(Q_q)$, certified for all $q$ by a positive rectangular
Schur minor. It also isolates the sharp exception
${\cal E}_{1,1}=Q_1^2\mathbb Q[x]_{\le1}$.

This theorem lowers the recurrence certificate from a generic ambient
cofactor scale to a degree-$q$ Pade scale. It deliberately does not infer
from the finite ranks that the residual quotient is one-dimensional or
saturated, and it gives no primitive-survivor height bound. Those are the
remaining steps before the improved recurrence can affect the final
Diophantine exponent.

Frozen hashes:

~~~
a4e1fa3f9562f876bc5dafec817373238298d6565ad34c291f0a3a70513cad84  sources/centered_cosh_pade_ideal_recurrence_theorem.md
f20223fb9bb9f524db7532c1fe1f8aad22b6e01245564d4b55b3ddf6795e1a20  scripts/centered_cosh_pade_ideal_recurrence_certificate.py
a6a99505f1cef3c1499be9a331cf452c76c1fc7f7d9f0b66b1e6baf56efaa48d  results/centered_cosh_pade_ideal_recurrence_certificate.json
ef1345491b9747c118e1e8a9c1a5c34160923bfe6fdea8a2aed9e4b5dd0a7c1c  results/centered_cosh_pade_ideal_recurrence_hashes.sha256
~~~

The manifest was independently verified and a fresh exact replay reproduced
the certificate in about one second using about 67 MiB RSS. Item 70 is an
all-parameter structural theorem, but it does not classify $e+\pi$.

## Root-of-unity checkpoint item 71

The quadratic Euler content now has an exact Kummer-period decomposition.
Writing



$$
H_N=\gcd(|E_{2N}|,|E_{2N+2}|),\qquad
 G_N=\gcd((2N+2)(2N+1)|E_{2N}|,|E_{2N+2}|),
$$



one first has



$$
G_N=H_N\gcd\left((2N+2)(2N+1),{|E_{2N+2}|\over H_N}\right).
$$



For each odd prime, remove from $H_N$ all valuation layers whose
prime-power Kummer period fits below $2N+2$, calling their product $S_N$
and the remaining quotient $J_N$. Prime-power Kummer periodicity then gives



$$
S_N\mid\operatorname {lcm}(1,\ldots,3N+3),\qquad
 \log G_N=\log J_N+O(N).
$$



The factor $J_N$ consists exactly of simultaneous adjacent Euler-number
prime-power divisibility before the first corresponding Kummer period. Thus



$$
\log G_N=o(N\log N)\iff\log J_N=o(N\log N).
$$



This places the recurring $149$ and $241$ branches in the harmless
periodic factor and localizes the primitive endpoint height to



$$
\log H(\mathscr C_N)=2N\log N-\log J_N+O(N).
$$



No known Kummer or direct resultant estimate bounds $J_N$ at the required
scale; the unreduced Sylvester bound is only $O(N^2\log N)$. The surviving
problem is an adjacent first-period higher-order Euler-irregularity theorem.

Frozen hashes:

~~~
a720ef166a3b772d85c32934782fcfa4d41797b274ea964259973a216bb369ca  sources/root_unity_quadratic_euler_gcd_kummer_obstruction.md
5685471a82b294cd77b60d3079067274f23e14f30e3317f2373c87ffcb2770d4  scripts/root_unity_quadratic_euler_gcd_kummer_certificate.py
89521c6ec34e3ff7c75d7845ab22de10562814a3cbe8d256bbd7769a9e2cb53d  results/root_unity_quadratic_euler_gcd_kummer_certificate.json
74b79cee3b86e5fe37700e1db68ed91976a56c01a783c1e10d5e13651d82ba49  results/root_unity_quadratic_euler_gcd_kummer_hashes.sha256
~~~

The primary-source formula, manifest, bytes, syntax, and deterministic replay
were independently checked; the replay used about 75 MiB. Item 71 is a sharp
arithmetic reduction, not a classification of $e+\pi$.

## Root-of-unity checkpoint item 72

For every endpoint degree $d$, a positive Hardy quotient form has an exact
evaluation/transverse normal form. In coordinates
$u=A_p(\pi)$, $v=(p_1,\ldots,p_d)$,



$$
{Q_n(p)\over a_n}=(u+\eta_n^tv)^2+v^t{\cal T}_nv,
$$



and therefore



$$
\left|\sqrt{Q_n(p)/a_n}-|A_p(\pi)|\right|
 \le\varepsilon_n\|v\|_\infty.
$$



Primitive minima through height $H$ differ by at most
$\varepsilon_nH$. Consequently, transferring absolute exponent $\mu$
requires $\varepsilon_nH_n=o(H_n^{-\mu})$; qualitative rank-one collapse
alone has no exponent content.

The aligned dimension-only Dirichlet exponent is $d$, and an algebraic-norm
example proves this is sharp without special information about $\pi$. The
conditional threshold under $\deg_{\mathbb Q}(e+\pi)=r$ is
$r^2d+r-1$. At $r=1$, ordinary Dirichlet reaches equality but not the
strict improvement needed for contradiction; for $r>1$, it is farther
below. Gaussian phase alignment preserves the full $d+1$ coordinates.
Unaligned real coefficients split into orthogonal parity blocks and achieve
only $\lfloor d/2\rfloor$, without halving the measure degree after
substitution $\pi=s-e$.

Frozen hashes:

~~~
6201f479c27e16afe4fdf515e24d860c0c360ea0be29c31d12feb97da0831687  sources/root_unity_hardy_all_degree_endpoint_collapse_theorem.md
e29f72af7515d0cf65bab00f65019de6d0ac366e96290c84a26f300bc070eeca  scripts/root_unity_hardy_all_degree_endpoint_collapse_certificate.py
09ab52efda354fc909d0dc7f8de063fde054a9b9fc0c8bc272dad21c7d236a6d  results/root_unity_hardy_all_degree_endpoint_collapse_certificate.json
cbfd5640107565c87c1bc4a7657f064a6842685ccdb0fb711d6c1a9bccad118c  results/root_unity_hardy_all_degree_endpoint_collapse_hashes.sha256
~~~

The dependency pins, manifest, syntax, bytes, exact block identities, parity
counts, and deterministic replays were independently verified. Item 72 is a
geometry theorem and barrier statement, not a classification of $e+\pi$.

## Root-of-unity checkpoint item 73

The uncontrolled factor $J_N$ isolated in item 71 is genuinely nontrivial.
The first exact occurrence in the scan through $N=1643$ is



$$
p=151483,\qquad
 \gcd(E_{3286},E_{3288})=151483.
$$



Both valuations are exactly one. A complete reciprocal-cosh inversion modulo
$p$ proves that the entire first-period $E$-irregular set is precisely



$$
\{3286,3288\}.
$$



Because $p-1=151482>3288$, this is an interior first-period pair, not a
periodic endpoint branch. Consequently



$$
H_{1643}=J_{1643}=G_{1643}=151483,\qquad S_{1643}=1.
$$



This exact example rules out both universal incompatibility of adjacent
Euler-irregular branches and any general implication that adjacency forces a
large total irregularity index. It does not give an asymptotic estimate for
$J_N$; the quantitative product problem remains open.

Frozen hashes:

~~~
c9ed43839126af9542ec0c0891cb5a48023a7cb17ba21dca34cb83bc629b6078  sources/root_unity_adjacent_euler_irregular_seed_counterexample.md
a92019c257e7c985fdec00d5bb88b70154a67c8c8e0e9b2184dd0bb7f2c88542  scripts/root_unity_adjacent_euler_irregular_seed_certificate.py
4468c09210ac6a72303980f4cf27070c914a717bab474a8e7f86d4bd4fab3aaf  results/root_unity_adjacent_euler_irregular_seed_certificate.json
c4e0b694a4f57130370e1f66869f5d862536e21708a78a0fa1c8655463525f0f  results/root_unity_adjacent_euler_irregular_seed_hashes.sha256
~~~

The exact integer-gcd, mod-$p^2$, complete first-period, finite-scan,
manifest, and strict-byte checks replay deterministically. The independent
run used about 85 MiB and left approximately 48 GiB RAM available. Item 73
does not classify $e+\pi$.

## Root-of-unity checkpoint item 74

Successive Hardy minima and exterior powers do not supply a separate
Diophantine gain. In evaluation/transverse coordinates, the endpoint lattice
has covolume one and



$$
{1\over(d+1)!EH^d}\le\prod_{j=1}^{d+1}\lambda_j(H,E)
 \le {1\over EH^d}.
$$



A full independent set obeys $1\le|\det P|\le(d+1)!EH^d$. For $k\le d$,
dividing a $k$-row exterior vector by its content $g$ and contracting
with evaluation produces ordinary integer polynomials $R_J$ satisfying



$$
\max_JH(R_J)=W,\qquad |R_J(\pi)|\le{k!EH^{k-1}\over g}.
$$



If $e+\pi$ were algebraic and
$\kappa=r^2d+r-1$, the Dirichlet scale forces



$$
\limsup{\log g\over\log H}
 \le k-{d+1\over\kappa+1}.
$$



An exterior construction beats the conditional measure only under the
strict reverse inequality. In the rational case this is exactly the
boundary $k-1$. Thus every useful determinant discount is itself an
exceptional single-polynomial approximation, rather than an amortization
over several vectors. Product and translated-resultant variants likewise
pay their added degree/height and contain only one small evaluation column.

Frozen hashes:

~~~
84ed2c28661846171d414529b6ed764646f47df1028b5c54590af5b15a65b9fe  sources/root_unity_hardy_successive_minima_exterior_no_go.md
b1a553637874fa957f781b8be2044377d8d2e80195a07fe7a99a1d7257f5f134  scripts/root_unity_hardy_successive_minima_exterior_certificate.py
7bc241179c63ac9fc0b6124c9279944c710243e06954a8c9508adf17fc11ea08  results/root_unity_hardy_successive_minima_exterior_certificate.json
2f13c98db67eb4dff21f6a442a1285207157ee08db712e410d53ddf213425e3b  results/root_unity_hardy_successive_minima_exterior_hashes.sha256
~~~

The exact exterior, determinant, threshold, resultant, phase, parity,
dependency, and byte audits replay deterministically. Item 74 is a
no-amortization theorem, not a classification of $e+\pi$.

## Root-of-unity checkpoint item 75

The all-parameter rational quotient left open by item 70 is now exact. For
the diagonal $[q/q]$ Padé pair $P,Q$ of
$F(x)=1/(2\cosh\sqrt x)$, and the adjacent $[q+1/q-1]$ pair $R,G$,



$$
RQ-PG=\kappa x^{2q+1},\qquad \gcd(Q,G)=1.
$$



Reduction modulo $Q$ gives



$$
\rho_Q({\cal E}_{q,1})=G^2\mathbb Q[x]_{\le q-2}\quad(q\ge2).
$$



For the second family, the canonical quotient map



$$
\Phi(T)=\left(T(0),\rho_Q\left({T-T(0)\over x}\right)\right)
$$



satisfies



$$
\Phi({\cal E}_{q,2})=
 \mathbb Q\Phi(E^2)\oplus
 \bigl(\{0\}\oplus G^2\mathbb Q[x]_{\le q-2}\bigr)\quad(q\ge1).
$$



Thus both product images have rational codimension exactly one in every
nonexceptional parameter; $(q,r)=(1,1)$ has codimension two. Exact
$G$-Krylov remainder spaces and the syzygy $E=GH+QK$ prove these
statements without finite-rank extrapolation. The unique first-family
annihilator is



$$
\lambda([T])=[x^{q-1}]\rho_Q(G^{-2}T),
$$



and one also obtains an exact product formula for
$\operatorname {Res}(Q,P)\operatorname {Res}(Q,G)$.

Frozen hashes:

~~~
1173dfd585050ef192cf0c71be8c6e14f6357a14e56e81d7f2afadf35d3f0afd  sources/centered_cosh_pade_residual_quotient_theorem.md
867b154754477d7e9e196f939dc5b5bf9e584d15d28fe3baa255505882dfd76e  scripts/centered_cosh_pade_residual_quotient_certificate.py
be9ed129087a44bb2d1d315efa8e19e3069682475a76b52a2c0410a5ec40d026  results/centered_cosh_pade_residual_quotient_certificate.json
eb10284c8cda928182de8b5f86f230a1bc708e8c3617391265c4f55849b77b13  results/centered_cosh_pade_residual_quotient_hashes.sha256
~~~

The package passes independent exact replay and strict source/manifest
audits. It is a rational codimension theorem, not an integral Smith or
primitive-height theorem, and does not classify $e+\pi$.

## Root-of-unity checkpoint item 76

For the reduced quadratic Euler ratio



$$
{P_N\over Q_N}
 ={\,|E_{2N+2}|/G_N\over
   (2N+2)(2N+1)|E_{2N}|/G_N},
$$



the beta-value formula gives



$$
{P_N\over Q_N}-{4\over\pi^2}
 ={32\over\pi^2\,3^{2N+3}}
  \left(1+O\left((3/5)^{2N+1}\right)\right).
$$



Explicit tail intervals prove that these fractions strictly decrease. The
adjacent integer determinant has the exact parity



$$
D_N=P_NQ_{N+1}-P_{N+1}Q_N>0,\qquad v_2(D_N)=1,
$$



and therefore



$$
Q_NQ_{N+1}>{13\pi^2\over216}\,3^{2N+3}.
$$



This yields an unconditional adjacent-product exponent $2\log3$ and an
individual limsup exponent $\log3$. Independently, Zudilin's published
irrationality measure for $\pi^2$ gives



$$
\liminf{\log Q_N\over N}
 \ge {2\log3\over5.095412}=0.4312162740\ldots.
$$



Frozen hashes:

~~~
8b22a86eea520400245e5529809da2dcce56cbfb26c9836677e23ccd0a197a0a  sources/root_unity_quadratic_euler_beta_denominator_floor.md
c9fd42d69521b2faaba8166c5495d25e75318a13a31327c9eaf41ea40ca18d1e  scripts/root_unity_quadratic_euler_beta_denominator_certificate.py
c36e90fdcd023c940ea525b98b5c4786e610061435d2aa8b913fb0200f4cfe97  results/root_unity_quadratic_euler_beta_denominator_certificate.json
22fba2af00e25aa5a956b923e490d2a853dd170ab2292178190bb5a1507d6f1d  results/root_unity_quadratic_euler_beta_denominator_hashes.sha256
~~~

The exact adjacent theorem and the fixed-measure transfer improve the gcd
ledger only by $O(N)$, not the required $N\log N$. Item 76 therefore
does not control $J_N$ at leading order and does not classify $e+\pi$.

## Root-of-unity checkpoint item 77

The proposed complementary quadratic dichotomy has now been tested exactly.
The original row



$$
C_N(T)=4Q_N-P_NT^2
$$



has relative error $3^{-2N+O(1)}$. Under hypothetical algebraicity degree
$r$ for $e+\pi$, it succeeds only if



$$
{\log Q_N\over N}<
 {2\log3\over2r^2+r}
$$



with a strict linear margin. A fixed-field coefficient-content lemma proves
that translating $C_N(\pi)$ to a polynomial at $e$ leaves absolute
projective height $\asymp Q_N$; finite-place normalization cannot absorb a
large reduced denominator.

Adjacent determinant and Bezout elimination reduce to a monomial or a
constant after primitive normalization. The adjacent product has relative
exponent at most two, below the degree-four conditional threshold. The only
fixed two-row affine combination cancelling the nearest base-$3$ pole is
the Richardson combination



$$
{9P_{N+1}/Q_{N+1}-P_N/Q_N\over8},
$$



whose relative error has leading term $48/5^{2N+5}$.

Write $h_N=\gcd(Q_N,Q_{N+1})$. Exact reduction of the Richardson
denominator gives



$$
{16Q_NQ_{N+1}\over9h_N^2}
 \le\widehat Q_N
 \le{8Q_NQ_{N+1}\over h_N}.
$$



It therefore requires



$$
\log h_N\ge
 \left(\log3-{\log5\over2r^2+r}\right)N+o(N);
$$



the rational-case constant is $0.5621329845\ldots$. Primewise Euler
valuation identities show that failure of the first branch supplies no
automatic survival into this neighboring gcd. The complementary construction
has traded the original two-Euler obstruction for a precise three-Euler
obstruction.

Frozen hashes:

~~~
697f3b29d899a3dd229b6b7b9748ec77c74d60d603fb67ea5e7f10fef56cfdb3  sources/root_unity_quadratic_two_regime_canonical_no_go.md
b4508adf4f4235ccb65de8a17a7e24fc815434a67e35b8daf3ed8afd62f763e8  scripts/root_unity_quadratic_two_regime_canonical_certificate.py
05a48e1954f7999da7f042fccefb794c95c5eff65c66a82622d5168ab8060567  results/root_unity_quadratic_two_regime_canonical_certificate.json
398c9b03759673e2e0cce91e52abe74bf2a70b098f546158c8e972fba6de4398  results/root_unity_quadratic_two_regime_canonical_hashes.sha256
~~~

The package passes independent replay, source, and manifest audits. It
excludes the canonical two-regime shortcuts but supplies no classification
of $e+\pi$.

## Centered-cosh checkpoint item 78

The balanced quadratic Padé branch now has an exact primitive border-content
description.  For



$$
F={1\over2\cosh\sqrt{x}},\qquad P_q/Q_q=[q/q]_F,
$$



write $a_m=[x^m]P_q^2/Q_q$.  A residual/resultant calculation proves that
the two first residue moments are fixed nonzero multiples of
$a_{4q+1}$ and $a_{4q}$.  Hence, whenever the pair is nonzero, the
primitive quadratic direction is



$$
\operatorname{prim}(a_{4q}-a_{4q+1}x).
$$



After factorially clearing the Toeplitz Padé rows, let $c_q$ be their
primitive cofactor kernel, $b_m$ the cleared coefficient border, and
$u_m=b_mc_q$.  Then the only endpoint content is



$$
K_q=\gcd(u_{4q},u_{4q+1}),
$$



and each $u_m$ is an augmented determinant divided by the gcd of the
maximal Padé minors.  At primes of full Padé row rank, divisibility by $p$
is exactly simultaneous membership of both borders in the Padé row space.
Hadamard's inequality gives



$$
\log H(C_q^{\rm prim})\le(3+o(1))q^2\log q,
$$



improving the previous generic cubic cofactor bound.  This is not a height
lower bound, and neither all-index first-moment nonvanishing nor sufficiently
large border content has been proved.

Frozen hashes:

~~~
a7db026c1ebc792ab30a8674897d48ddbedce71da350a730966fdfee5c6132a8  sources/centered_cosh_balanced_quadratic_border_content_theorem.md
e0c2e1b22bf916242ce685d1c43a1b88477b5052858fe26221d17bfaefb7d3bd  scripts/centered_cosh_balanced_quadratic_border_content_certificate.py
8272e59ac346044fcc23a76321ccf4252596c4b942dd3fc714228b6a694f3a27  results/centered_cosh_balanced_quadratic_border_content_certificate.json
c06ea9b875ba072de9bf250526538f6639afd7fa0131719febb5df9f36067eb3  results/centered_cosh_balanced_quadratic_border_content_hashes.sha256
~~~

Independent exact replay and proof audits pass.  The replay peaked at about
1.36 GiB RSS; the 2-GiB value in the certificate is a local safety guard on a
50-GiB machine.  Item 78 supplies a sharper target for a local-prime theorem,
not a classification of $e+\pi$.

## Root-of-unity checkpoint item 79

The complete beta ratio, rather than only its leading base-3 tail, has the
signed Dirichlet expansion



$$
r_N={4\over\pi^2}\sum_{q\ \mathrm{odd}}b_qq^{-2N},
 \qquad
 b_q=(-1)^{\omega(q)}\chi_4(q)
 {\prod_{p\mid q}(p^2-1)\over q^3}.
$$



The optimal filter on $h$ consecutive ratios is uniquely



$$
(X-1)\prod_{j=1}^{h-2}((2j+1)^2X-1).
$$



It cancels the atoms through $(2h-3)^{-2}$, has coefficient height
$\exp(2h\log h+O(h))$, and is explicitly nonzero once
$N\ge N_0(h)=O(h^2)$.  Its analytic gain per universal denominator copy
obeys



$$
{2\log(2h-1)\over h}\le\log3,
$$



with equality only for the original adjacent pair $h=2$.

All-size Vandermonde, fixed-size signed Hankel, and simultaneous
higher-ratio determinants have likewise been audited.  Their analytic decay
is spread over respectively $h(h-1)$, $h^2$, and $h(h-1)$ universal
denominator copies.  An exact negative $3$-by-$3$ Hankel minor rules out
ordinary total positivity.  Thus none of these canonical higher-order
constructions upgrades the known linear denominator floor to the required
individual $N\log N$ scale.

Frozen hashes:

~~~
e921fcb73e8c3fc4d62848008cc34d1f9ff0ee482fcba1e8ef5123462df1bca6  sources/root_unity_beta_higher_determinant_multiplicity_barrier.md
936b03be9dc6c63d17616d9e38c0c0c9a67755e1f8e20a746b2fe4fceaebaca7  scripts/root_unity_beta_higher_determinant_certificate.py
2f53dd329f9eef44bdd22868ec558da0a6f9c9f874d88cb077e3e53ddf9830ba  results/root_unity_beta_higher_determinant_certificate.json
abf5aae37871defe5a5fb0237506b0830fca17d94a6dd914bdf3994b086cf5c9  results/root_unity_beta_higher_determinant_hashes.sha256
~~~

Independent replay and all dependency checks pass at about 37 MiB peak RSS.
The surviving escape is explicitly arithmetic: prove a very large reduction
of the actual lcm/common content, or find a genuinely stronger growing-size
signed determinant.  Item 79 is a no-go theorem for canonical upgrades, not
a classification of $e+\pi$.

## Root-of-unity checkpoint item 80

The neighboring reduced-denominator gcd now has an exact three-Euler
valuation descent.  If $h_N=\gcd(Q_N,Q_{N+1})$, then prime by prime



$$
v_p(h_N)=\min((b+x-y)_+,(c+y-z)_+),
$$



where $b,c$ are the two index-factor valuations and $x,y,z$ are the
valuations of $E_{2N},E_{2N+2},E_{2N+4}$.  Off the index factors, support
is exactly the strict descent $x>y>z$.  Consequently



$$
(h_N^{\rm off})^2\mid |E_{2N}|,
 \qquad h_N^2\mid A_NA_{N+1}|E_{2N}|,
 \qquad v_2(h_N)=1.
$$



This squarefull restriction is exact but still allows
$\log h_N=N\log N+O(N)$, so it does not close the Richardson branch.

For even $M$, common divisibility of $E_M,E_{M-2}$ makes zero a
fourth-order root modulo the common divisor of the centered Euler polynomial
$\mathcal F_M(T)=f_M(T^2)$.  It follows exactly that



$$
d^3\mid\operatorname{Disc}(\mathcal F_M).
$$



The full discriminant nevertheless has logarithmic height
$O(M^2\log M)$, versus the already-trivial $O(M\log M)$ bound for
$d$.  The parallel level-4 modular-form construction also fails to shrink
the ledger: Euler divisibility kills its constant coefficient only, adjacent
weights have different residual eigenpackets, and the Sturm determinant has
the same quadratic-dimensional cost.

Frozen hashes:

~~~
28696128629ac4828d492dc5736545c8558e4546a3b566dfc2ecf7aa85170d13  sources/root_unity_adjacent_euler_descent_discriminant_barrier.md
8d1a5c5577389fb009eb3a1596c77d1cffc5183526515440db8f2f7553a9adf2  scripts/root_unity_adjacent_euler_descent_discriminant_certificate.py
2a62637288d4f807e4d34c17bdeaa64b5a03164f0303b18c27373bd7e47b1890  results/root_unity_adjacent_euler_descent_discriminant_certificate.json
57de6b30c8efc92532d3d7c8292e2467d176983baeb20443d7f17cfecf4f7f14  results/root_unity_adjacent_euler_descent_discriminant_hashes.sha256
~~~

Independent exact replay and the three dependency manifests pass.  Item 80
isolates a strict valuation pattern and rules out two natural ways of
globalizing it, but it does not classify $e+\pi$.

## 2026-08-27 continuation: actual beta block lcm and balanced nonvanishing

The optimal higher beta filter can be cleared by the actual least common
multiple



$$
{\cal Q}_{N,h}=\operatorname{lcm}(Q_N,\ldots,Q_{N+h-1}),
$$



not merely by the product of its denominators.  For $N\ge N_0(h)$,
where $N_0(h)\le2h^2+2$, the exact bound is



$$
{\cal Q}_{N,h}\ge
 \frac{(2h-1)^{2N}}
 {(4/\pi^2)((2h-1)^{-1}+(2N)^{-1})}.
$$



Taking $h=\lfloor\sqrt{(N-2)/2}\rfloor$ proves
$\log{\cal Q}_{N,h}\ge N\log N-O(N)$.  Removing the elementary
index factors preserves this scale.  The Kummer-visible portion is only
$\exp(O(N))$; the remaining $N\log N-O(N)$ mass consists of
adjacent Euler valuation drops whose prime-power periods exceed the
whole block.  Canonical Kummer periodicity therefore cannot concentrate
that mass into one denominator.  The generic lcm-to-maximum step is still
optimized at the original two-term filter and has rate at most
$N\log3$.

Frozen hashes:

~~~
a0f3811a353cf19778bf0b262f20190de3735dccf8c2081a35d0b8c19035af28  sources/root_unity_beta_actual_lcm_kummer_barrier.md
fa9cda18584bbbb71cf5b12652ffd5c839468cc49886274a3e724d2b4205fdaf  scripts/root_unity_beta_actual_lcm_kummer_certificate.py
ae75d93ca1373db85dd704f8d20dabe0053797aac980efcee40b57f12dc92a13  results/root_unity_beta_actual_lcm_kummer_certificate.json
df801458d310f255dc59862dca63abedb3976eefc9edb680e9a75fc4662ec6ec  results/root_unity_beta_actual_lcm_kummer_hashes.sha256
~~~

Separately, the balanced centered-cosh Padé survivor is now proved
nonzero in every order.  If



$$
a_m=[x^m]\frac{P_q(x)^2}{Q_q(x)},
$$



then



$$
a_{4q}>0,\qquad a_{4q+1}<0\qquad(q\ge1).
$$



The proof is an all-parameter Jacobi--Trudi sign theorem for the secant
alphabet, plus a forced-column tableau bound using
$e_j=1/(2j)!$.  It proves that the primitive balanced endpoint has
exact quadratic degree for every $q$, superseding the conditional
nonvanishing sentence in item 78.  It does not control its primitive
two-border content or global lift height.

Frozen hashes:

~~~
6531d74029b442f3893425ef056af1dd2536988a2b508801439ab8e208493139  sources/centered_cosh_balanced_quadratic_nonvanishing_theorem.md
8d5ba5f486e8d5b422a9685d2665b70085a12152ee986b0832495ab770d85558  scripts/centered_cosh_balanced_quadratic_nonvanishing_certificate.py
3886c53959e0d263b6f803ec25b55facdea77aa6d7738b65a91f6385f0cb83e9  results/centered_cosh_balanced_quadratic_nonvanishing_certificate.json
f5d5ef9179b0386e259aac0c95969461c1244ed756c5b38b2c75ca94bc4e3f82  results/centered_cosh_balanced_quadratic_nonvanishing_hashes.sha256
~~~

Independent replays used about $40.8$ MiB and $72.9$ MiB,
respectively, with roughly $47$ GiB still available.  These are new
structural theorems, but neither one classifies $e+\pi$.

## 2026-08-27 continuation: normalized Euler eliminant and Pascal height

The ordinary even Euler polynomial has the exact integral normalization



$$
{\cal E}_{2m}(X)=X(X-1)P_m(X(X-1)),
$$



where $P_m$ is monic of degree $m-1$.  Every common divisor
$d\mid E_{2m},E_{2m-2}$ makes $-1/4$ a double root of $P_m$
modulo $d$, so $d\mid\operatorname{Disc}(P_m)$.  This removes
permanent roots and artificial powers of four, but its Sylvester ledger
is still $O(M^2\log M)$.  At the exact seed
$(M,p)=(3288,151483)$, $P_{1644}$ has precisely one double root
and all other roots are simple modulo $p$; a universal next-
subdiscriminant shortcut is therefore false.

~~~
8cecdea69be6432aac7f3dee4e8851e31977b2a9dce00f44620931e249353550  sources/root_unity_adjacent_euler_bounded_eliminant_no_go.md
2fd8c166a342e368bfc56d2c8391fd2b7dcae11eb9ef8897c02d41084da6475b  scripts/root_unity_adjacent_euler_bounded_eliminant_certificate.py
6792b17675377119323f546a61776fe533a5baefcdc5248725c65b76b50b0eab  results/root_unity_adjacent_euler_bounded_eliminant_certificate.json
6c451189b41e7ddaa3563da40a4c119a159c2442a873c6451c2bda8665c53dfe  results/root_unity_adjacent_euler_bounded_eliminant_hashes.sha256
~~~

For the balanced secant Padé survivor, changing to the even-factorial
basis turns the defining system into a signed Pascal matrix.  Exact
integer endpoint convolutions and Hadamard give



$$
\log H(C_q^{\rm prim})\le3(\log2)q^2+O(q\log q),
$$



improving the former $O(q^2\log q)$ bound.  The exact $q=13$ to
$100$ continuation shows no content collapse; at $q=100$, the
primitive height has 22,538 bits and endpoint content only 861 bits.
Sampled contents are $(8q+2)$-smooth, but no universal support theorem
has yet been proved.

~~~
5e1fdadfd00705921fa05f97472af266d5eaf86ed9c70c67bab7547f47729c07  sources/centered_cosh_factorial_pascal_height_theorem.md
50086d13c37301566fa2e500d495b49bbfa7ee116d02b52a9cb298936b898e28  scripts/centered_cosh_factorial_pascal_height_certificate.py
aa27ea7ef6ba580a76947d4e50f287ee921f40bea751c5f8ef0d19ecf2620e2d  results/centered_cosh_factorial_pascal_height_certificate.json
9c607dca829bbb5b9f7255a8a5c37563c41523fea6524643c4ea893add5956a4  results/centered_cosh_factorial_pascal_height_hashes.sha256
0b7bb1ab95581ec660d5b1c4445e5d2e3a45247521500e4d450e0e66499b12e2  sources/centered_cosh_factorial_pascal_extended_scan.md
a43d49d009a1aa6a976097f42fecfd2ec8903538518ccff7c8abd860b73d39c9  scripts/centered_cosh_factorial_pascal_extended_scan.py
5b562dc109f2a247ba4094bea8078826c7cc5ac3c04fe75f9452ae93387359f6  results/centered_cosh_factorial_pascal_extended_scan.json
00c68385ad3fbcbf61f821cf9c5fb47b5a0a841cfd28667849c86dfbbbdb5249  results/centered_cosh_factorial_pascal_extended_scan_hashes.sha256
~~~

These computations remained below $1.6$ GiB RSS with roughly $47$
GiB available.  The local endpoint bound is still quadratic in $q$,
whereas the analytic gain is only $2q\log q+O(q)$; neither result
classifies $e+\pi$.

## 2026-08-27 continuation: first-period Euler moment complexity

The strict first-period factors left by the beta-denominator lcm theorem
now have an exact all-prime finite-field model.  For odd $p$, with
$r=(p-1)/2$,



$$
E_{2n}\equiv
 2\sum_{j=0}^{r-1}(-1)^j\bigl((2j+1)^2\bigr)^n\pmod p.
$$



The support is the complete group of nonzero quadratic residues and all
weights are nonzero.  Consequently the minimal constant-coefficient
linear recurrence has exact order $r$, the weight interpolant has exact
degree $r-1$, and every full moment Hankel determinant is a nonzero
weighted Vandermonde square.  More explicitly,



$$
W_p(X)=-2\sum_{k=1}^{r}E_{2k}X^{r-k},\qquad
 W_p^2\equiv4\pmod{X^r-1}.
$$



The actual adjacent seed $(N,p)=(1643,151483)$ simultaneously has two
zero moments, full support, recurrence order $75741$, and nonsingular
full Hankel rank.  This rules out the canonical bounded-recurrence,
bounded-interpolant, and moment-rank shortcuts, but supplies no upper
bound for the first-period prime product.  A new coupling of these
deterministic square roots across varying primes is still required.

~~~
4b24dbecf01e1a06690d4b75b620beb741c6825d6c1e1729cc28c333f020cd4e  sources/root_unity_adjacent_euler_first_period_moment_obstruction.md
46af6d5b3f93744f96eb023ddcb40b5085f956304b7f70a7700f29c99c1b6341  scripts/root_unity_adjacent_euler_first_period_moment_certificate.py
9abd8499467b5e0bc6830045195ba454b6dda212d449d3029d4dbe0b40260002  results/root_unity_adjacent_euler_first_period_moment_certificate.json
af340ed10de55eb9587fdb3167d475b7f5cda405367fedb3ca00244ed1b23adf  results/root_unity_adjacent_euler_first_period_moment_hashes.sha256
~~~

Independent replay used only about $27.6$ MiB.  This is a precise
route-specific obstruction, not a classification of $e+\pi$.

## 2026-08-27 continuation: direct normalized centered-cosh lift

The balanced endpoint image now has a direct Padé basis, eliminating the
previous ambient Cramer-lift loss:



$$
{\cal E}_{q,1}=Q^2{\cal P}_q\oplus QG{\cal P}_{q-1}
                         \oplus G^2{\cal P}_{q-2}.
$$



For the primitive two-border endpoint
$T_q=(u_{4q}-u_{4q+1}x)/K_q$, two successive reductions modulo $Q$
give unique polynomials $A,B,C$ with



$$
T_q=Q^2A+QGB+G^2C,qquad
 \deg A,\deg C\le q-2,quad\deg B\le q-1.
$$



Replacing $Q,G$ by their exact centered-cosh remainders produces a
five-frequency global form of polynomial degree at most $6q$, origin
order at least $8q+4$, and endpoint $T_q(-\pi^2/4)$.  The construction
is linear, so division by $K_q$ is preserved coefficient by coefficient.

A universal primewise Schur clearing has logarithm
$2q^2\log q+O(q^2)$, while the $q$ forced tableau columns contribute
the cancelling factorial $((2q)!)^{-q}$.  Stable negative-power bounds
in $\mathbb Q[x]/(Q)$ and a normalized Schur lower bound for the Padé
cross coefficient then prove



$$
\log H(T_q)=O(q^2),\qquad
 \log H_{\rm an}({\cal L}_q)=O(q^2).
$$



The rational global coefficients are needed only in the analytic Schwarz
majorant; no integral global denominator claim is made.  This result
proves that the former quotient/Cramer cost was artificial, but the
remaining $q^2$ scale is still larger than the available
$2q\log q+O(q)$ gain.

~~~
b5448650b31b887a163ba95f593e38fc5c45195b61800f8c834ecb7ed2369d9f  sources/centered_cosh_balanced_quadratic_normalized_global_lift_theorem.md
46dd6f87dbec2927c81a870225b8bee9542684ab48ceb391514d3aaab1c1e092  scripts/centered_cosh_balanced_quadratic_normalized_global_lift_certificate.py
d9fa114ca1047846654015ff5353631db481269a40f7c48414f918a956d9481c  results/centered_cosh_balanced_quadratic_normalized_global_lift_certificate.json
90c432faf5130880664ffa561aff0faa7d574dde8c1f50c265a13dc3002591c8  results/centered_cosh_balanced_quadratic_normalized_global_lift_hashes.sha256
~~~

The independent exact replay includes the $q=2$ edge and used about
$75.8$ MiB RSS.  It does not classify $e+\pi$.

## 2026-08-27 continuation: cyclic Euler window section

The nonlinear square-root identity for a first-period Euler prime is



$$
A_p(X)^2\equiv1\pmod{X^r-1},\qquad r=(p-1)/2.
$$



Writing its coefficient equations as cyclic convolutions $F_t$, an
explicit anchor construction now proves that any sufficiently short
coefficient/equation window has a polynomial section over arbitrary low
data.  For initial windows $S\subseteq[0,L]$, $T\subseteq[0,K]$,
the anchor $u=L+K+1$ works whenever



$$
r>2L+3K+2.
$$



It assigns one anchor coefficient and one independent far partner per
selected equation.  Algebraically, the convolution ideal then has zero
intersection with the prescribed low-data ring.  This remains true after
imposing the adjacent conditions $E_{2N}=E_{2N+2}=0$.

With $L=K=N+1$, the section applies for every $p>10N+15$.  The
smaller primes have total log-mass only $O(N)$, so a bounded-window
eliminant is nonrestrictive precisely in the far-prime range requiring
control.  The exact seed $(N,p)=(1643,151483)$ admits a synthetic
completion of the first 1,645 convolution equations; its next equation
fails, cleanly separating this local theorem from the full global system.

~~~
e783aeb445472e0630e7945931a5978b9a0a15180dee03e1409cb59693f8b1b8  sources/root_unity_adjacent_euler_cyclic_window_section_no_go.md
cb8301f80b2c5d3b57d6f8b6901d00c9c7d2484cd2f424a5ec55581c938a1ff0  scripts/root_unity_adjacent_euler_cyclic_window_section_certificate.py
9614598edb4ecb125e73696e38615df0b3e56466e7468f69630c581fb3988276  results/root_unity_adjacent_euler_cyclic_window_section_certificate.json
f955bf4e71a080d0622e314352a3784b93cc772a3146e66bdb258c35e1ce3904  results/root_unity_adjacent_euler_cyclic_window_section_hashes.sha256
~~~

This theorem excludes only formal bounded-window elimination.  A global
use of all $r$ equations or new cross-prime arithmetic remains open; no
classification of $e+\pi$ follows.

## 2026-08-27 continuation: exact factorial-Pascal/border normalization

The natural factorial normalization of the centered-cosh Pade denominator
has now been related exactly to the primitive ordinary normalization in the
bordered determinant.  For the primitive signed-Pascal vector $d$, its
lower-unitriangular binomial transform



$$
e_k=\sum_{i=0}^k(-1)^{k-i}\binom{2k}{2i}d_i
$$



is again primitive.  With



$$
g_{B,q}=\gcd_k\left(e_k\frac{(2q)!}{(2k)!}\right),
 \qquad s_q=(2q)!/g_{B,q},
$$



Bezout proves $g_{B,q}\mid(2q)!$, and $s_qB_d(-x)$ is the primitive
ordinary integer denominator.  The two endpoint contents consequently obey
the exact all-parameter bridge



$$
(u_{4q},u_{4q+1})=(s_qL_q,-s_qR_q),\qquad
 K_q^{\rm border}=s_qG_q^{\rm Pascal}.
$$



The replay through $q=30$ finds that $G_q^{\rm Pascal}$ is supported on
primes at most $8q+2$, and that it divides
$\operatorname{lcm}(1,\ldots,8q+2)^2$ for $2\le q\le30$.  Neither
pattern is promoted to an all-parameter theorem; $q=1$ already needs a
higher lcm power.  Initial canonical Jacobi-fraction coefficients also show
irregular prime factors, so that standard recurrence does not yet explain
the finite smoothness.

~~~
6841a257ef7123c0080469335b5bd9a35c3f54ea36701a3894a95a447b6763cb  sources/centered_cosh_pascal_border_normalization_theorem.md
04e9f875ed419e1b3ba03595cf3a01dd3eb9cf0ed101254d2f6a2172822d813a  scripts/centered_cosh_pascal_border_normalization_certificate.py
01639485ade5a8b3b349a725861d436294a389e621d23a2da9c16dffadd3ad1c  results/centered_cosh_pascal_border_normalization_certificate.json
6b828f9c0a0b1aff69e598969cc9f2da3da7665307c99295136ba0b08fe3cb23  results/centered_cosh_pascal_border_normalization_hashes.sha256
~~~

The manifest pins the older bordered certificate as a dependency.  A clean
root replay, compilation, and hash check pass.  This resolves normalization,
not the missing content estimate, and does not classify $e+\pi$.

## 2026-08-27 continuation: exact positive quadratic Robin repair

The Stein--Robin Taylor near-solution can always be corrected by an integral
quadratic without losing positivity.  With $t=1-x$,
$(1-i)^N=R_N+iI_N$, and $M_N=N!-R_N$, every such correction is



$$
C_{N,q}=I_N-4q+(q-M_N/2)t-qt^2,
$$



and its residual is



$$
F_{N,q}=t^N+M_Nt(1-t/2)-I_N(1-t)
          +q(4-6t+4t^2-t^3).
$$



Choosing $q=0$ for $I_N\le0$ and
$q=\lceil I_N/3\rceil$ otherwise gives
$F_{N,q}\ge M_Nt(1-t/2)\ge0$.  This closes the qualitative local
repair question, but the exact output ledger shows that it cannot yield a
shrinking primitive form:



$$
\liminf\Lambda_{N,q}\ge\pi-\frac32.
$$



The rational denominator and output gcd are treated exactly, so the bound
survives both antiderivative clearing and primitive normalization.  A
Bernstein--Walsh and Markov argument further gives a positive primitive gap
for every uniformly bounded correction degree.  Growing-degree corrections
remain open.

~~~
1611c4976a64836a20209871a55b92e09bcb6c0c9cb18701cd800567b1a0ac21  sources/common_kernel_stein_robin_quadratic_correction_barrier.md
f814471c0c627ff2fb9c4da2f99a4a37ebf6380316d030796c7ddc946c4921dc  scripts/common_kernel_stein_robin_quadratic_correction_certificate.py
4641657f345e13bde4ed84b4642ffd4942d3f6b8448f9c9a60ecbe573dbf216d  results/common_kernel_stein_robin_quadratic_correction_certificate.json
208982ad388c02ba42c79726b6eaefa8acd1ed7d5a2fad6de5c138a44483038a  results/common_kernel_stein_robin_quadratic_correction_hashes.sha256
~~~

The exact replay and all pinned dependencies pass.  This result forces the
common-kernel search into growing-degree/nonlocal repairs; it does not
classify $e+\pi$.

## 2026-08-27 continuation: unbalanced centered-cosh slope theorem

For one parity block, write $B=2M+\sigma$, $d=M+r$, and let
$V$ be the degree-at-most-$d$ factors with the tail coefficients
$d+1,\ldots,B$ killed.  The exact neighboring anti-diagonal Padé entries
give



$$
V=Q{\cal P}_{r-\sigma}\oplus G{\cal P}_{r-1}.
$$



When $M\ge2r-\sigma$, its product image is the direct sum



$$
Q^2{\cal P}_{2r-2\sigma}\oplus
 QG{\cal P}_{2r-\sigma-1}\oplus
 G^2{\cal P}_{2r-2},
$$



of dimension $6r-3\sigma$.  Its codimension is exactly



$$
\delta=2M-4r+3\sigma+1=3(B-d)-d+1.
$$



The original parameters give $\delta=(3t-n)/2+O(1)$, proving that
one third is the exact single-block codimension transition.  Reversal
reduces exact minimum degree to a square jet determinant for a ratio of
neighboring Padé denominators.  Its bounded exact grid is nonzero, but no
all-parameter determinant or coupled two-parity theorem is claimed.

Uniform Schur clearing gives Padé input log-height $O(M^2)$; even this
optimistic structured scale exceeds the available $2t\log n+O(n)$
analytic gain when $t$ is linear.  Thus simple unbalancing does not close
the current height ledger.

~~~
a9e1d82af845b01150b4075c26a45425d7907fbc1b48862d9b1ca70bb2e08f00  sources/centered_cosh_unbalanced_pade_slope_obstruction.md
193cda9b3eace30006c4ca839dac379212bf340dd5063e0b204a0a12cb81de0b  scripts/centered_cosh_unbalanced_pade_slope_obstruction_certificate.py
1699b6167fc69c3858fccb33abbdd9c27590a64ee14aa290b7eecfdf0d04db79  results/centered_cosh_unbalanced_pade_slope_obstruction_certificate.json
343a7a07d9a7b706caf7752a423b29e4b10be40f3c31cce0bfadc9d7ef978dd5  results/centered_cosh_unbalanced_pade_slope_obstruction_hashes.sha256
~~~

The corrected odd-parity allocation and all exact decompositions passed two
independent audits.  This is not a classification of $e+\pi$.

## 2026-08-27 continuation: an optimal Robin localizer and its denominator

The growing-degree Robin search admits an exact integer boundary layer:



$$
h_m=x^{4m}(m+1-mx^4),\qquad h_m\equiv1\pmod{(1+x^2)^2}.
$$



It is monotone from zero to one on $[0,1]$, has the smallest possible
sup norm, and has $L^1$ mass asymptotic to $1/(2m)$.  Multiplication
by $h_m$ therefore preserves the two Robin jets while localizing every
fixed correction in $L^1$.

The exact application audit reveals two failures.  Gaussian congruences
prove for every $N$ that a Taylor-defect correction cannot vanish to
order $N$ at $x=1$; the resulting boundary profile changes sign for
all sufficiently large localization parameters.  Independently, the
non-Robin remainder injects a dense harmonic channel into the complete
rational output.  Every prime $5m/2<p<3m$ not dividing the fixed defect
coefficient occurs exactly once in the reduced denominator, so its logarithm
is at least $(1/2+o(1))m$.

Even if positivity were imposed conditionally, exact primitive content can
remove at most $N!$, leaving a lower bound



$$
\frac{3q_{N,K}(m)}{N!(\deg F+1)^2}.
$$



It grows exponentially on the intended localizing diagonals.  This closes
the explicit sparse multiplier, while leaving rapidly varying moderate
diagonals and genuinely nonlocal corrections open.

~~~
5eb2a69842edfa4d6b8f88390834179e3e3cba65881af44120bc5161d1555ec8  sources/common_kernel_integer_robin_localizer_barrier.md
252ecc1e461d5572102a0ed784811815d537efdcb75afeb96571d038d102aa4a  scripts/common_kernel_integer_robin_localizer_certificate.py
2bcab0e6031398337afc7b2797c08e949f7fae546b34d695386838dc07059468  results/common_kernel_integer_robin_localizer_certificate.json
1754bcceff930fe5ed44b67282f666970aeabb5616886dfb1e5cab3eb19c4a07  results/common_kernel_integer_robin_localizer_hashes.sha256
~~~

The all-$N$ proof, exact denominator formula, prime-isolation theorem,
and pinned replay pass independently.  No classification of $e+\pi$
follows.

## 2026-08-27 continuation: all high-order Robin localizers force a prime window

The denominator mechanism of the sparse Robin multiplier extends to every
integral high-order localizer.  Let $u=1+x^2$,
${\cal T}P=(1-x)P'-xP$, and
${\cal T}K=uG+(\alpha+\beta x)$.  For
$h\equiv1\pmod{u^2}$, $h(0)=0$, put
$n=\operatorname{ord}_0h$, $d=\deg h$, and



$$
S_h=\frac{{\cal T}(hK)-{\cal T}K}{u}.
$$



The quotient $r=(h-1)/u$ has the forced prefix
$r_{2j}=(-1)^{j+1}$, $r_{2j+1}=0$ below degree $n$.  It follows
from the full product identity—not merely from isolated defect moments—that
every odd prime



$$
p>(\deg S_h+1)/2,\quad p-1>\deg G,\quad p<n,\quad p\nmid\alpha
$$



occurs to valuation exactly $-1$ in
$4\int_0^1S_h$.  Thus a family with
$n\ge(1/2+\varepsilon)d$ has output-denominator logarithm at least
$\varepsilon d+o(d)$, after the exact fixed base and primitive-content
ledger.

If $0\le h\le1$, the endpoint congruence forces $h(1)=1$.  The first
nonzero endpoint jet of ${\cal T}(hK)$ is then independent of $h$, so
its weighted $L^1$ norm cannot decay faster than polynomially.  The
denominator-cleared norm consequently diverges exponentially in the same
high-order regime.  A signed exact zero-moment witness shows why the theorem
cannot be extended from congruence data alone to arbitrary nonlocal
multipliers of degree at least about twice their initial order.

~~~
65b31f7df68551e35ecab50fb0f09026dbb87bd7e596075c13703367ac5a90c1  sources/common_kernel_robin_localizer_moment_denominator_barrier.md
84f878fe9f0e1cafecd32cb0661f760564ccf86018579e83ad4833b74bd0284f  scripts/common_kernel_robin_localizer_moment_denominator_certificate.py
c457c0aee6cdc289707c610083957a55c84b724205926930b694e8023a072fe0  results/common_kernel_robin_localizer_moment_denominator_certificate.json
1a523213cd86f5b3865bf86a7b35a4f0bd682df262af920cc7b02623f0560c03  results/common_kernel_robin_localizer_moment_denominator_hashes.sha256
~~~

The clean replay, manifest verification, Python compilation, and source
audit pass.  This rules out the local high-order multiplier regime; it does
not classify $e+\pi$.

## 2026-08-27 continuation: the universal centered-cosh prime interval

The conspicuous upper prime band in the centered-cosh endpoint gcd is no
longer merely experimental.  For the primitive factorial-Pascal endpoint
integers,



$$
\prod_{4q<\ell\le8q+2\atop \ell\ {\mathrm{prime}}}\ell
 \mid
 \gcd\!\left((8q+2)(8q+1)w_{4q},w_{4q+1}\right)
$$



for every $q\ge1$.

The proof first obtains exact half-period congruences for the secant and
tangent factorial coefficients from Euler-polynomial power sums.  Lucas
reduction then turns each endpoint modulo a prime in the band into an
odd-top border $J_r$.  That border vanishes identically because



$$
rJ_r=-(2r)![y^r],2(BH-p)yH'
$$



and the Padé error $BH-p$ starts in degree $2q+1$.  Separate digit
arguments cover the midpoint prime $4q+1$ and the possible explicit
prefactor prime $8q+1$.

This proves one squarefree copy of every prime in the interval.  It leaves
open all large exceptional primes and every uniform prime-power upper bound,
so it is a content lower theorem rather than the missing height theorem.

~~~
9e1a951e63b05455db4e6ade95f4b1a99b0c6330ff8680327f204b5e54f0b27d  sources/centered_cosh_pascal_universal_interval_content_theorem.md
cab278c79d3332e0d8f112fdaad0757fd309a5fcb24b120dad0ca384b67917a4  scripts/centered_cosh_pascal_universal_interval_content_certificate.py
18173a8bd0e455ac35bd3d2cebe3e0d73293f3ebe559381e63cb4e2531901384  results/centered_cosh_pascal_universal_interval_content_certificate.json
66e20c910ef2e167d8f52f57380086b0b97cfa473c0699901ad8c7f3f936ef78  results/centered_cosh_pascal_universal_interval_content_hashes.sha256
~~~

The all-parameter congruence proof and independent exact replay pass.  The
result does not classify $e+\pi$.

## 2026-08-27 continuation: nonlocal one-third window and coupled terminal band

Two all-parameter obstruction theorems extend the latest frontier.  First,
if an even integral multiplier satisfies



$$
h\equiv1\pmod{(1+x^2)^2},\qquad h(0)=0,qquad
 n=\operatorname{ord}_0h,\quad d=\deg h,
$$



then every odd prime $d/3<p\leq n$ occurs to exact exponent one in the
reduced denominator of
$\int_0^1(h-1)/(1+x^2)$.  If $0\leq h\leq1$, the least common clearing
$D(h)$ of the first two defect moments satisfies



$$
D(h)\max(|I_0|,|I_1|)
 \geq{1\over16d^2}\prod_{d/3<p\leq n\atop p>2}p.
$$



This includes the positive family $(2x^4-x^8)^k$, of degree/order ratio
two, for which the denominator-cleared localization grows exponentially.
The theorem also isolates the exact high-coefficient residue that prevents
automatic extension to a non-even or full Robin channel, and gives a
positive ratio-four witness outside its range.

Second, for the two unbalanced centered-cosh parity blocks, the exact
coupled identity is



$$
\dim((V_0^2+xV_1^2)\cap\mathbb Q[x]_{\leq1})
 =\operatorname{rank}C-\operatorname{rank}J.
$$



It proves uniformly that this intersection is zero whenever
$n\geq5$ and $n-3\leq t\leq n-1$.  In the wider range $3t>n$, the
equal-block problem is reduced to explicit $6r$ and $6r+3$
Hermite--Padé jets in $1,K,K^2$ or $1,H,H^2$.  Their general
nonvanishing is still open; the complete 248-pair grid through $n=28$ is
finite evidence only.

~~~
df2657ebe8e241d6f14b8c8628ba5c085662301936efc869f69669818749bb49  sources/common_kernel_even_nonlocal_moment_denominator_barrier.md
82e1828ef3f4ed22ffe7d60abcb9fbe9e709c6bf75df0fbcecb793b67bc632e6  scripts/common_kernel_even_nonlocal_moment_denominator_certificate.py
c53c46ce84fb9ea035020d24fbc876bc96136a03327188108e4212c08f21a842  results/common_kernel_even_nonlocal_moment_denominator_certificate.json
bc6aae22ca67cb7e04678432e3befdd33b7072ab3cc67b1d656134fd7e0a1806  results/common_kernel_even_nonlocal_moment_denominator_hashes.sha256
3aea77c0901bcf1d1209ee57c18dec01cc2c15c37c454249a8bb45af9b91d52d  sources/centered_cosh_unbalanced_coupled_parity_obstruction.md
d517a9033881398e4cef117ef57f3e6e5601c8f3aabd1f68dd43cffc1304ecda  scripts/centered_cosh_unbalanced_coupled_parity_certificate.py
6bd9b5f1d9c2046e2847718b35140789c08581913710d080c710d062fd6ab0cc  results/centered_cosh_unbalanced_coupled_parity_certificate.json
985a4a111319321868b17e526f0ecf6e41896708a92fc1db2256402188b7580a  results/centered_cosh_unbalanced_coupled_parity_hashes.sha256
~~~

Independent replays used about $21.5$ MiB and $39.0$ MiB peak RSS,
respectively, with roughly $47$ GiB still available.  These results rule
out additional construction ranges; neither classifies $e+\pi$.

The parity hypothesis in the one-third theorem is essential at the local
prime level.  For arbitrary $h$, simultaneous $p$-integrality of the
two moments is equivalent to



$$
2r_{p-1}+r_{2p-1}\equiv0,qquad r_{2p-2}\equiv0\pmod p.
$$



The positive polynomial



$$
(2x^4-x^8)^6
 \left(1-(1+x^2)^2x^3(1-x)^2\right)^2
$$



has $(n,d)=(24,66)$ and cancels both residues at $p=23$, even though
$d/3<23<n$.  Its two reduced moment denominators are exactly prime to
23.  This disproves a prime-by-prime arbitrary-parity extension, but leaves
open an aggregate bound allowing exceptional primes.

~~~
d91d09a05d767e31ef968f72813191421803e766c20c0407c0c69f39152b80fb  sources/common_kernel_nonsymmetric_two_moment_residue_counterexample.md
ab2712dcad3901dc5b0352338f34975347dc4bc4136c97ea1d7e0f4585e64629  scripts/common_kernel_nonsymmetric_two_moment_residue_certificate.py
d6452400a3014be7d59abdbed03ff2bd66f26c68692fa94f57090959212f57df  results/common_kernel_nonsymmetric_two_moment_residue_certificate.json
14edc755bb18e6726f6e1e5f6006afcc76950e2d3206dd3d2b942e10ee471081  results/common_kernel_nonsymmetric_two_moment_residue_hashes.sha256
~~~

The exact replay used about $20.7$ MiB peak RSS.  This is a rigorous
scope barrier, not a result about the arithmetic nature of $e+\pi$.

The aggregate two-moment extension is also false for a substantial finite
window.  There is an explicit positive integral polynomial



$$
h=(2x^4-x^8)^{115}\left(1-(1+x^2)^2x^{75}(1-x)^{75}
 (c_0+c_1x)\right),
$$



where
$c_0=139574584508098815002244647712452355913710915$ and
$c_1=92665357687907045832657432294875741514399515$, with
$(n,d)=(460,1075)$, for which all 17 primes in $d/3<p<n$ cancel
from both reduced moment denominators.  Their product is
$237359812447644832129693355690076072498951997$.  An exact CRT lemma
explains the cancellation, while the strict inequality
$c_0+c_1<4^{74}$ proves positivity without sampling.  This is a finite
all-window obstruction; scalability remains open.

~~~
271a0184572a5e203f56564c9db789410dc34eec18488c28f880d31bbfc015e2  sources/common_kernel_positive_crt_all_window_cancellation_barrier.md
b533da632f07a6887f225638b55ff67b1fd465fc09920f1da5ab5df4171b94ff  scripts/common_kernel_positive_crt_all_window_cancellation_certificate.py
32d4df4cba3eece31dd0d202f80db95495da3b02be0256155406bedea9be961b  results/common_kernel_positive_crt_all_window_cancellation_certificate.json
fd2a96672780209dcca4fd2ea4cf2d437fb491432667ed9fd32db0cc154f16b4  results/common_kernel_positive_crt_all_window_cancellation_hashes.sha256
~~~

The independent replay and a separate polynomial reconstruction pass.  This
barrier does not classify $e+\pi$.

The scalability question left open by that finite example has now been
resolved.  For every fixed
$2/(2+\log4)<\lambda<1$, a sparse positive base and a one-variable CRT
produce, for all sufficiently large $m$, admissible polynomials with
$(n,d)=(4m,4m+8\lfloor\lambda m\rfloor+11)$ that cancel both residues
for a prime set of log-mass $2(1-\lambda)m+o(m)$.  Since the full natural
window has mass $(8/3)(1-\lambda)m+o(m)$, this erases asymptotically
three quarters of its Chebyshev mass.  The local matrices are diagonal, their
only failures divide the explicit integer
$2mL+6m+4L+5$, and the positivity capacity has an exponential margin.

~~~
211fa36d058cfedb242e8dc732cac2ce9bb354e81e241fa6799f6f063a5715f5  sources/common_kernel_positive_crt_asymptotic_three_quarter_cancellation.md
01795ba68c3a16760f78f1913ed17821155b49c0e9e4591b8239a2ebd0a4b690  scripts/common_kernel_positive_crt_asymptotic_three_quarter_certificate.py
f4411917f17e2ba40f593ead5da578cbaf2fee1b2ee3b658343e957c5d1f531a  results/common_kernel_positive_crt_asymptotic_three_quarter_certificate.json
e5e497408f8b6a1ad6c4fc28634e2c5e8805754e3c10bf52e700325033d2625c  results/common_kernel_positive_crt_asymptotic_three_quarter_hashes.sha256
~~~

This is an unconditional asymptotic obstruction for the two isolated moments;
it does not control an additional/full correction channel and does not classify
$e+\pi$.

The proposed sharp Bessel valuation estimate
$v_p(q_n)\leq1+\lceil\log_p n\rceil$, suggested by nearly 1.4 million
finite root hits, is false.  On the ordinary $7$-adic branch through 2,



$$
n=464838342618219576262104570205987685961890202821
$$



lies between $7^{56}$ and $7^{57}$ but satisfies $v_7(q_n)=59$.
An exact Mahler expansion modulo $7^{60}$ proves the valuation; factorial
divisibility makes the cutoff at $j=868$ rigorous.  The branch has zero lift
digits at positions 57 and 58.  The weaker sufficient target is now a uniform
sublinear bound for terminal zero-run lengths across every surviving branch.

~~~
2e34ff5b30e658088d882568f83493c4c09582ccdbf921bb6337005b2c213abf  sources/bessel_padic_index_double_zero_counterexample.md
f0733a1493311401ceb6a0f59194012db20ee04ddf50203ecce601b4280eccf8  scripts/bessel_padic_index_double_zero_counterexample_certificate.py
c06353984f883dc02b441492fb5f414a8f0cd750378f86f4978bf8bde3db7a5d  results/bessel_padic_index_double_zero_counterexample_certificate.json
ee1b2591676f6721a1b133ffb8374c3e35de0a0f983ca930271603df6708f58a  results/bessel_padic_index_double_zero_counterexample_hashes.sha256
~~~

The exact replay and an independent closed-sum evaluation pass.  This is a
counterexample to one proposed bound, not an arithmetic classification of
$e+\pi$.

The shifted CRT padding can in fact cancel asymptotically the whole natural
one-third prime window, improving the intermediate three-quarter theorem.
For every sufficiently large $q$, there is a positive admissible integer
polynomial of order $20q$ and degree $48q+11$ whose two-moment common
denominator is coprime to every prime in
$(48q+11)/3<p<20q$, except possible divisors of
$K_q=40q^2+44q+5$.  The whole window has log-mass $4q+o(q)$, while
the exceptional mass is at most $\log K_q=O(\log q)$.

The construction uses
$x^{12q}(1-x^4)^{4q}(1-x^2)$; its exact capacity maximum is
$(3/7)^{3q}(4/7)^{4q}$, and
$7\log7-3\log3-4\log4-4>0$ supplies an exponential CRT margin.

~~~
e8cbb912fd801e83d31917ccbe24ff40dc936509e45bd4751ef11b2c7a454215  sources/common_kernel_positive_crt_asymptotic_full_window_cancellation.md
7f22f68204fbd302bdf73d1e07c32e6f487a814ef4d28f3a7aed986c96fa1e29  scripts/common_kernel_positive_crt_asymptotic_full_window_certificate.py
1328ed4a8d8eaf42f36e11752a3449df9a0db31edbb9aca7a2bd3f1a5d872a39  results/common_kernel_positive_crt_asymptotic_full_window_certificate.json
0d4277f69ba4fc92e7b0ebc9222cceb9172994f03dadfabfd169ad7b23fff008  results/common_kernel_positive_crt_asymptotic_full_window_hashes.sha256
~~~

This closes the aggregate two-moment window question in the negative.  A full
correction output or a genuinely different arithmetic constraint remains
necessary; the theorem itself does not classify $e+\pi$.

The Bessel index-lift obstruction is stronger than the first double-zero
example indicated.  On the ordinary $7$-adic branch through $2$, a
certified $987$-digit index between $7^{1167}$ and $7^{1168}$ has
$v_7(q_n)=1171$.  Its lift digits at positions $1168,1169,1170$ are all
zero, followed by the nonzero digit $4$.  A finite Mahler evaluation modulo
$7^{1172}$, with a rigorously justified coefficient cutoff, proves the
claim.  Hence even the additive $+2$ valuation repair is false; the weaker
uniform sublinear zero-run target remains open.

~~~
3295664e80c0e3ee8a6b871fa73303de555548491b70a39077e7387a04dde2cf  sources/bessel_padic_index_triple_zero_counterexample.md
63be13d66517f6fdabed177a229626f215faa086356437fcc8520b336aae600d  scripts/bessel_padic_index_triple_zero_counterexample_certificate.py
c90fb481e9641c1c066280719a044675ed087acf868a891ade0bf4a0dfb09857  results/bessel_padic_index_triple_zero_counterexample_certificate.json
8088bcc99328176637a83dec7ce9139bc8bb02f394b96b323313954aaf0f6922  results/bessel_padic_index_triple_zero_counterexample_hashes.sha256
~~~

The exact replay and a separate modular implementation agree.  This new
counterexample does not prove that terminal zero runs are unbounded and does
not classify $e+\pi$.

The presently available local $p$-adic structure cannot, by itself, repair
that failure.  An explicit analytic, $1$-Lipschitz, reflection-symmetric
comparison polynomial with a simple root and an exact affine lift law can be
made to have arbitrarily prescribed zero-digit gaps.  With a suitable choice
of gaps its valuation at integer prefixes reaches the full $n\log n$ scale.
Its coefficient is generally a nonrational $p$-adic integer and it does not
satisfy the Bessel difference equation; consequently the theorem is a sharp
method barrier and redirects the live problem to global rational-height or
recurrence-specific input.

~~~
4372ccae9160d501a1c72631c1b4ce43865d29e6d36d88b11b192a7f7626ef03  sources/bessel_padic_local_zero_run_no_go.md
a3de0204026e19b10da91039d0347341d15367c33bd5c7e07b78c9c808c788a7  scripts/bessel_padic_local_zero_run_no_go_certificate.py
bec3c0854ba91906ca12e6827388b5f626d4e088b758bf7ba95c1629e94722de  results/bessel_padic_local_zero_run_no_go_certificate.json
2673e830c57748ec85d37d22ada1279e1d932cf11ca98b7790cd906ccda50e13  results/bessel_padic_local_zero_run_no_go_hashes.sha256
~~~

This no-go theorem does not establish long zero runs for the actual Bessel
sequence and does not classify $e+\pi$.

The full fixed-correction output does not rescue the positive common-kernel
prime-window strategy.  For every fixed $K\in\mathbb Z[x]$, finitely many
nonnegative integer CRT channels produce admissible polynomials of order
$20q$ and degree $48q+O_K(1)$ for which the common denominator of both
defect moments and the complete $K$-correction output is coprime to every
prime in $(48q+C_K)/3<p<20q$, apart from divisors of the explicit
$O_K(q^2)$ integer $\Delta_K(40q^2+44q+5)$.  Hence the canceled window
mass is $4q+o(q)$ and the possible surviving mass is only $O_K(\log q)$.

The key response is



$$
\delta s_{2p-1}\equiv-[x^{2p-1}]V_q(1+x)(1-x^2)^2K C_q\pmod p.
$$



A finite coefficient-block lemma supplies the required ranks.  Its sole
structurally proportional case is
$K=x(1-x)(1+x^2)^3R(x^4)$, where the full target vanishes automatically.
The non-even class-three channel needed for $K=1-x$ also resolves the
apparent conflict with an older identity that assumed an even localizer.

~~~
1071a65d0e799dd27754c6a117c573eee7170d7b430593c17da15fae0b1bc104  sources/common_kernel_positive_crt_full_correction_cancellation.md
64fd00d3c07ed7685362ee0df7c3872be7815c03360b9b6e67ae461d41644207  scripts/common_kernel_positive_crt_full_correction_certificate.py
20b7709fe330087fc44716c010950500d35ee5686c5787e281d09e2ff4bbbd53  results/common_kernel_positive_crt_full_correction_certificate.json
227318fce04df7c79dafb4a570ede3f0767c1c75b084aaaefe746b55a7c1a99a  results/common_kernel_positive_crt_full_correction_hashes.sha256
~~~

The exact replay and an independent structural calculation pass.  This theorem
is restricted to fixed $K$; it neither controls native growing-degree
corrections nor classifies $e+\pi$.

Ordinary condensation and scalar continued-fraction transfer do not settle the
two equal-parity centered-secant jets.  The canonical Padé pair obeys an exact
degree-one transfer with constant nonzero determinant, but its symmetric square
leaves a six-dimensional boundary quotient.  The equal jet embeds in the
opposite flagged parity with codimension three and explicit basis determinant
$\pm b_M^{3m}$.  The associated two-block Toeplitz minors satisfy a full
Desnanot--Jacobi lattice identity, but it shifts away from the preceding equal
jet and introduces four off-diagonal minors of nonfixed sign.

A generic positive-node obstruction is exact:



$$
K_t(y)=y\left(\frac1{1-y}+\frac1{1-2y}+\frac{t}{1-3y}\right),\qquad
 \Delta_2(K_t)=(4t-1)(t^3-25t^2-13t+1).
$$



At $t=1/4$, the equal jet is singular even though the three nodes and
weights are positive and the coprime rational representation has resultant
$-4096$.  Thus generic Markov positivity and ordinary resultants are
insufficient; a special secant boundary identity is needed.  A modular scan
rigorously certifies all 7,081 admissible special determinants through
$M=120$, but is not extrapolated.

~~~
4304030a5efa878aea3751bffb15f957a6dcec0b39e8ea24c80b3e7254812504  sources/centered_cosh_equal_jet_condensation_barrier.md
dcecfa5bcf000028eb994973b4a98618ac66ea50bbfd13e68e995c6bbfb8bbee  scripts/centered_cosh_equal_jet_condensation_barrier_certificate.py
6d4f4231ed0b4623289ede62bcea47b8ace626960b375f0727cc3c22dd280952  results/centered_cosh_equal_jet_condensation_barrier_certificate.json
c2e38c053485920cb7fb35d75d49fe9d5752eb36708b1138dbf8c0d786fac7b0  results/centered_cosh_equal_jet_condensation_barrier_hashes.sha256
~~~

The all-parameter algebraic identities and generic counterexample are proved;
the special secant nonvanishing theorem and the classification of $e+\pi$
remain open.

## Bessel checkpoint item 105: all-integer jet identity and Euler-series obstruction

For



$$
q_0=q_1=1,\quad q_n=(4n-2)q_{n-1}+q_{n-2},
$$



let $p_0=1,p_1=3$ obey the same recurrence, and let
$b_0=0,b_1=4$,



$$
b_{n+2}=(4n+6)b_{n+1}+b_n+4q_{n+1}.
$$



The frozen item-105 package proves for every prime $p$ and integer
$n\ge0$



$$
f_p'(n)=(-1)^{n+1}(p_n{\cal K}_p-b_n),\qquad
 {\cal K}_p=\sum_{m\ge0}m!\in\mathbb Z_p,
$$



with termwise differentiation justified in the appropriate local Tate
algebra.  It also proves $0\le b_n\le4(n+1)p_n$ and the exact ordinary
one-digit root-lift law



$$
t\equiv(q_n/p^a)(p_n{\cal K}_p-b_n)^{-1}\pmod p.
$$



Thus every integer jet carries the still-open fixed-prime Euler-series
constant; no stronger lifting modulus or zero-run bound follows.

~~~
fb68cec8ec01ca9dcfa39eb86af61f76a9bba07f18a6e955668ef2e90f89696e  sources/bessel_padic_all_integer_jet_euler_obstruction.md
0ede4cd80a7b343ca5c2e90c741d7b2629e41acb2b895aa27a10073da12f2755  scripts/bessel_padic_all_integer_jet_euler_obstruction_certificate.py
586de99873f278dce9af079db895937e8c1ffaadf48873027544d671c0466ea5  results/bessel_padic_all_integer_jet_euler_obstruction_certificate.json
b55fd4214f4207d6d4698b6a83ebb4bb474b09509cb42ac45e93beb8021520cf  results/bessel_padic_all_integer_jet_euler_obstruction_hashes.sha256
~~~

The deterministic replay and manifest pass.  This is an exact obstruction,
not a classification of $e+\pi$.

## Bessel checkpoint item 106: central singular paths

For every odd prime, reflection about $-1/2$ gives an exact dichotomy along
$n_a=(p^a-1)/2$.  If the central value of the canonical interpolation is
nonzero, $v_p(q_{n_a})$ is eventually constant.  If the central value is
zero, its local multiplicity is even, say $\mu\ge2$, and



$$
v_p(q_{n_a})=\mu a+h\qquad(a\gg1).
$$



The second case would create a terminal zero run proportional to the digit
depth, but no prime is proved to realize it; even then its fixed-prime
contribution is only $O(\log n_a)$.

~~~
f61c7e3005ee08d218bdc4150c0e34e9dcecc85119b74901f687aff9459d40e8  sources/bessel_padic_central_singular_zero_run_dichotomy.md
e36a44346586129d07691ccbf9a8e6a8f2247caf2b5bae94bac2314c371cccf4  scripts/bessel_padic_central_singular_zero_run_dichotomy_certificate.py
ee5417445c5bac26e8ffd710d36b8c1024dda1ebaa93a926496143eae681edcd  results/bessel_padic_central_singular_zero_run_dichotomy_certificate.json
7110154f392dd435ba554a6ec2f4239cebc766bc1eb933e01604bb0f81028e46  results/bessel_padic_central_singular_zero_run_dichotomy_hashes.sha256
~~~

The analytic proof, manifest, and deterministic replay pass.  This remains a
conditional local mechanism, not a classification of $e+\pi$.

## Common-kernel checkpoint item 107: complete growing-correction cancellation

For every sufficiently large $q$ and every nonzero integer polynomial
$K_q$ of degree at most $12q-10$, with arbitrary coefficient height and
content, the frozen item-107 theorem constructs an integral positive localizer
$h_q$ with



$$
h_q\equiv1\pmod{(1+x^2)^2},\quad
 \operatorname {ord}_0h_q=20q,\quad \deg h_q=48q+13,
 \quad0\le h_q\le1\text{ on }[0,1].
$$



All three common-kernel correction integrals are simultaneously integral at
every prime



$$
\frac{48q+\deg K_q+13}{3}<p<20q.
$$



The result includes the complete nonempty degree range and the native
factorial-height Taylor--Robin correction.  Its localized polynomial is
primitive, so neither coefficient height nor common polynomial content restores
the discarded window obstruction.  Analytic sign and decay remain open.

~~~
d1cd0012c8457ced0f064f23a8bf3256e91ff26730b8eaf5bcd7d984836f6ca7  sources/common_kernel_growing_correction_full_window_cancellation.md
8509d260b7d3ceaa879d88035a6b54802a08514dafe587be01694cb6d9c544f1  scripts/common_kernel_growing_correction_full_window_certificate.py
43e0146200996bcbc67fee8d47598abb6da10a6c32051f021afdbead43fb1f30  results/common_kernel_growing_correction_full_window_certificate.json
ef4c51baa0a9a2660be5e1360682f4bcb522354e1af8a6c87c6d3b9bfa057fc6  results/common_kernel_growing_correction_full_window_hashes.sha256
~~~

The frozen replay, manifest, independent determinant audit, and endpoint case
all pass.  This is a definitive no-go for that denominator mechanism, not a
classification of $e+\pi$.

## Bessel checkpoint item 108: aggregate shift--jet product-formula no-go

Every polynomial or determinant built from finitely many Bessel parameter
shifts and first jets reduces over $\mathbb Z[x]$ to the four boundary
symbols $F,G,X,Y$.  If order $s$ at a zero of $F$ is forced solely by
the recurrence, its derivative, and $F=0$, the reduced expression is
divisible by $F^s$.  At an integer center, cancellation of the Euler-series
indeterminate therefore leaves an integer divisible by $q_n^s$, of height at
least $s\log q_n$.

Hence this finite formal algebra merely repackages the Bessel factor that the
aggregate product formula was meant to bound.  Noncancelling jets retain the
prime-dependent constants ${\cal K}_p$.  The theorem does not exclude a new
transform, infinite-tail identity, or special actual-root auxiliary.

~~~
90f69f0589392c84c4205ac2b95b5375a86e212ae7e33490708186d9a6aef45a  sources/bessel_aggregate_shift_jet_product_formula_no_go.md
8b7f1368de6a442a95cae1bc1c3d4762c43317af81c3d7a478e33f2921e45c7c  scripts/bessel_aggregate_shift_jet_product_formula_no_go_certificate.py
c94bf05c654c1fa272b80d9ebddedc7ed2bb70d88c2be044a774fdb34a20fe52  results/bessel_aggregate_shift_jet_product_formula_no_go_certificate.json
11ee42a3940770707892dba303e502b8f4e9000d02f1db39767e9e41b82bf617  results/bessel_aggregate_shift_jet_product_formula_no_go_hashes.sha256
~~~

The proof, manifest, deterministic replay, negative-shift checks, and
coefficientwise divisibility audit pass.  No classification follows.

## Secant checkpoint item 109: actual-kernel sign barrier

For the genuine Padé denominators of $1/(2\cosh\sqrt x)$, the fixed
block-size equal quadratic-jet determinant $\Theta_6(X_M,Y_M)$ has exact
signs $+,-,-,+$ at $M=6,7,14,15$.  The corresponding lower
$\Theta_4(X_{M-1},Y_{M-1})$ determinants are positive, so the canonical
six-dimensional condensation quotient also changes sign.

This rules out a uniformly positive resultant, Gram, Cauchy--Binet, or
fixed-sign multiple-orthogonality factor under the canonical normalization.
It does not rule out a sign-changing prefactor and does not settle
nonvanishing.

~~~
45bfb6497840dc9f9e0a997091c56d104d66157a992c57f598c31bd1001da218  sources/centered_cosh_equal_jet_actual_sign_barrier.md
5c5b94902e124fa52fdbd9e5d7141a3355313091aeb4828e03375f63dce5c701  scripts/centered_cosh_equal_jet_actual_sign_barrier_certificate.py
179d8366d87d48b9cd25761f1be71cbdc027b4f22fb0ad6dd7cb25b07c6cbd79  results/centered_cosh_equal_jet_actual_sign_barrier_certificate.json
dda7ad5eb73c802a0688d4cddea9a294ff943c29575ebc3f8a43f44d765148c0  results/centered_cosh_equal_jet_actual_sign_barrier_hashes.sha256
~~~

The replay and manifest pass, and a separate exact reconstruction reproduces
the decisive signed hashes.  This is a proof-strategy barrier only.

## Bessel checkpoint item 110: large-prime cancellation tower

The frozen large-prime theorem proves



$$
p>2n\Longrightarrow v_p(q_n)\le n-1,
$$



but also shows why termwise factorial valuations cannot improve it: every
terminating summand is a $p$-adic unit.  At $p=2m+1$, an exact expansion



$$
(-1)^m q_m=\sum_{\ell=0}^m(-p^2)^\ell S_{m,\ell}
$$



turns depth $A$ into a finite congruence involving one new symmetric
harmonic layer every two powers.  No nonvanishing law for those layers is
known.  The example $q_8=13^2\cdot1846921$ also rules out exponent one in
the wider range $n/2<p$.

~~~
baa384012e6f56f3437de42eb7614e0475763a883529fbfda97120497c97b11d  sources/bessel_large_prime_unit_cancellation_frontier.md
f7044fb57a01c7ea1198441833ce10d5e1c0c8613d72a3463da745ce50f0d29c  scripts/bessel_large_prime_unit_cancellation_frontier_certificate.py
58dda46677fc6c1fee1c30e2d865f055a9a3c94af9c74fac88845ea55fa81005  results/bessel_large_prime_unit_cancellation_frontier_certificate.json
e1c425fea9ab46f11686b52126ea76dcf70720704d949cec9d070f0bb2d93291  results/bessel_large_prime_unit_cancellation_frontier_hashes.sha256
~~~

The replay, manifest, and independent central expansions pass.  The required
little-oh estimate remains open.

## Common-kernel checkpoint item 111: native sign and Roth thresholds

Every one-signed admissible native Taylor--Robin residual is nonnegative and
forces the localizer degree $d$ to satisfy



$$
d^4\ge\frac{(N!-\Re(1-i)^N)(N+1)}{54e}.
$$



Thus sign control requires factorial-quarter-root degree.  Nevertheless its
raw weighted integral is exactly $\Theta(1/N)$.  After reduction, the
associated rational approximation to $e+\pi$ has error
$\Theta((N!N)^{-1})$.  If its denominator were at most
$(N!)^{1/2-\delta}$ infinitely often, Roth would prove
$e+\pi$ transcendental.  This is equivalent to the unproved output-content
condition $g/D\ge(N!)^{1/2+\delta}$.

~~~
7a06684887367ce114e0c613e58c5dc1db688678099b0d3ed02b35c9c4b789e2  sources/common_kernel_native_sign_endpoint_degree_barrier.md
16f125838a585724b1e312b8bb6d0f8a7808c24883052c4773e33851b4438675  scripts/common_kernel_native_sign_endpoint_degree_certificate.py
4a9604b3f3adb787b66ce9733dc7de91c74226380734a42bc2e6fa687af15384  results/common_kernel_native_sign_endpoint_degree_certificate.json
400b4e5ae612683394a657c69f6aee4e1e2369b0d518f8c6027d51aa26c3efc3  results/common_kernel_native_sign_endpoint_degree_hashes.sha256
~~~

The proof and replay pass.  Existence and the Roth-scale content estimate are
the surviving requirements.

## Root-of-unity checkpoint item 112: tangent-survivor exponential no-go

For the reduced tangent-number ratio



$$
\frac{8r(2r+1)\tau_r}{\tau_{r+1}}=\frac{P_r}{Q_r},
$$



an exact odd-zeta formula gives a strictly decreasing rational approximation
to $\pi^2$ with error asymptotic to
$(8\pi^2/9)9^{-r}$.  Transferring Zudilin's published
irrationality-measure bound for $\pi^2$ proves



$$
\liminf_{r\to\infty}\frac{\log Q_r}{r}
 \ge\frac{\log9}{5.095412}=0.4312162740\ldots.
$$



Hence no subsequence can satisfy the archived activation condition
$\log Q_r=o(r)$.  A measure-free adjacent determinant has exact
2-adic valuation one and yields
$Q_rQ_{r+1}>4\,9^r/(5\pi^2)$.  Adjacent irregular Bernoulli pairs at
$(r,p)=(45,587)$ and $(168,491)$ also block a naive odd-coprimality
argument.  No factorial-scale denominator floor or classification follows.

~~~
8dc9acde0025c4038b1b7e486ee327b6f077dae737e828c111ec066e7fcf0439  sources/root_unity_tangent_survivor_exponential_no_go.md
59dbabc81c1e784ade8115a1cec509a9fb4a5eba37909237d2854e1384db19b2  scripts/root_unity_tangent_survivor_exponential_no_go_certificate.py
1e4e1b379087e37938918802a5040ab54841540b158acff537f64ca6ed594378  results/root_unity_tangent_survivor_exponential_no_go_certificate.json
71e0b42a14b2bbcc3dbfc104824048a51f75a1c9c97296da6f2c7c33acbd2e33  results/root_unity_tangent_survivor_exponential_no_go_hashes.sha256
~~~

The analytic proof, primary constant, manifest, deterministic replay, and
control-byte scan pass.  This closes one proposed sufficient condition, not
the classification of $e+\pi$.

## Common-kernel checkpoint item 113: high-order Roth-content no-go

For any sign-controlled native localizer of degree $d$ and origin order
$r$, every prime



$$
\max\!\left\{N,\frac{d+1}{2}\right\}<p<r,\qquad
 p\nmid N!-\Re(1-i)^N,
$$



survives to exact exponent one in the reduced rational denominator $D$.
Consequently, whenever $r\ge(1/2+\eta)d$,



$$
\log D\ge(\eta-o(1))d,\qquad
 \log(g/D)\le-(\eta-o(1))d.
$$



This is exponentially opposite to the content threshold that would activate
Roth.  It includes the sparse localizer
$x^{4m}(m+1-mx^4)$, but not the nonlocal CRT family with limiting
order/degree ratio $5/12$; the latter remains the live common-kernel branch.

~~~
d6d46ba4d8f87268062e027c76ae90b71e45e6e9c80685770e9517aafe741685  sources/common_kernel_roth_high_order_content_obstruction.md
0b0e139df870e3f262f334c0efd278a28a065c3fb85d87326db43bfd96729b8e  scripts/common_kernel_roth_high_order_content_obstruction_certificate.py
272cd4b67284f46d810ff9193b37abc0356848196e1f0e8203d9a9bd3d69516e  results/common_kernel_roth_high_order_content_obstruction_certificate.json
6fe2ebc3013eb81eb2284f44b8e07d03784d048ce76938877e6363b91386686b  results/common_kernel_roth_high_order_content_obstruction_hashes.sha256
~~~

The proof, replay, manifest, and an independent perturbed-localizer audit pass.
This is a scoped obstruction, not a classification.

## Common-kernel checkpoint item 114: critical CRT sign obstruction

The algebraically successful order-$20q$, degree-$48q+13$ CRT localizer
cannot satisfy the native sign condition.  At $t=1/(5q)$, its beta-type
base has logarithmic slope $3\le t\lambda\le5$, forcing a negative native
residual uniformly in every $N\ge2$.  The padded CRT correction is only
$\exp(-4q\log q+O(q))$ on that layer, even after one derivative, and is
too small to change the sign.  Since the residual is $1$ at $x=0$, every
member changes sign for sufficiently large $q$.

~~~
2abd83feaca1058a0c8a6723a4a66e55bfcbddc152985fb3ddebb1722a7693d1  sources/common_kernel_native_crt_endpoint_layer_sign_obstruction.md
0b77e84e1afa44993878dec140db7c6146d28efbeace227d92282c0466cca535  scripts/common_kernel_native_crt_endpoint_layer_sign_obstruction_certificate.py
ffa71b6f020e5fd6efdb3188feecf3b16992aa38c93a5ffdb21b621549bc280b  results/common_kernel_native_crt_endpoint_layer_sign_obstruction_certificate.json
35618f77fbf3a922cfb8ec1309950ac908a0daf901c4498c707d17c938e827ee  results/common_kernel_native_crt_endpoint_layer_sign_obstruction_hashes.sha256
~~~

The theorem and replay pass.  It closes this particular CRT construction,
not every possible localizer in the critical order/degree regime.

## Common-kernel checkpoint item 115: native sign existence is classified

For every $N\ge2$, an admissible integral localizer with nonnegative native
residual exists exactly when



$$
N\bmod8\in\{0,1,2,3,4\}.
$$



The construction joins an explicit increasing endpoint profile to a transformed
incomplete-gamma tail, smooths their transverse crossing without losing the
differential inequality, and arranges integral endpoint jets through order
three.  Draganov's simultaneous nearest-integer Bernstein theorem then
converts the smooth profile into an ordinary $\mathbb Z[x]$ polynomial while
preserving sign and interval bounds.  The excluded classes $5,6,7$ are
exactly those already ruled out by the endpoint value.

~~~
283641248f64788c69516874407882efebd5393871ebc23a98a71bd66f30ffbc  sources/common_kernel_native_sign_integer_bernstein_existence.md
e927357755a9449cf1898bd682c75e6d9ae86a08ea24ce04756daf62d5a5b1e8  scripts/common_kernel_native_sign_integer_bernstein_certificate.py
0a6abc5d0c8b11c344cf9c74df93381fd60bc14215848b2ca8949d612891d4ab  results/common_kernel_native_sign_integer_bernstein_certificate.json
337f9276d17304927c34427277fbc62f8bb99642cf525a69aa01c6eed818a2f9  results/common_kernel_native_sign_integer_bernstein_hashes.sha256
~~~

The primary theorem audit, analytic proof, exact replay, and manifest pass.
The degree can be enormous and the rational output denominator/content remains
uncontrolled, so this is not yet a transcendence proof.

## Bessel checkpoint item 116: large-prime four-point exclusivity

For every prime $p\ge5$, the full $n<2p$ window decomposes into
reflection/anti-period orbits.  If $r+s=p-1$, $p\mid q_r$, and
$c,\delta$ denote the base quotient and affine lift slope, then



$$
(q_r/p,q_s/p,q_{r+p}/p,q_{s+p}/p)
 \equiv(c,c-\delta,-c-\delta,-c+2\delta)\pmod p.
$$



When $\delta\ne0$, at most one representative can have valuation at least
two; the other three have valuation exactly one.  When $\delta=0$, the
orbit is all-or-none at the square threshold.  Central orbits are necessarily
singular and have the corresponding two-point dichotomy.  One exceptional
valuation per orbit remains unbounded.

~~~
1e8fed0a5ab04c97c4e0749d40304d6398f9fd32d55c7b49085fb4b4ecca4e41  sources/bessel_large_prime_four_point_exclusivity.md
9a30c35da6a3132406bc5998c10a05f9ed2f4a47510e61cdce4ba7dabd9c29e3  scripts/bessel_large_prime_four_point_exclusivity_certificate.py
ce0a028b2170b8291e3bc42dd088c5bfdcfda2a89b4cf055b550a60623d1c190  results/bessel_large_prime_four_point_exclusivity_certificate.json
a13749e329b3f14381f0c5d9db8ca5239fe9ef7735ffdd071fd40c3531704eea  results/bessel_large_prime_four_point_exclusivity_hashes.sha256
~~~

The symbolic proof, dependency hashes, manifest, and replay pass.  The
exceptional exponent and singular branch remain open.

## Common-kernel checkpoint item 117: exact output ledger and isolated candidate

Every admissible native localizer $h=1+(1+x^2)^2q$ has a rational output
coordinate depending on $Q(t)=q(1-t)$ through exactly one moment:



$$
\rho_{N,h}=\rho_{N,1}-5(a+b)
 -4\int_0^1(a+bt)t(2-t)^2Q(t)\,dt.
$$



For raw Bernstein channels, the four beta moments give explicit rational
responses, all cleared by $\operatorname {lcm}(1,\ldots,n+5)$.  The resulting
integer ledger performs reduced-denominator cancellation before primitive
content removal and is exact in every degree.

Arbitrary coefficientwise residue rounding modulo $m_n$ preserves $C^3$
approximation uniformly at the sharp scale $m_n=o(n)$.  The full clearing
LCM grows exponentially, so this rules out the naive all-channel full-modulus
rounding strategy, but not adaptive sparse or correlated channels.

There is also an intrinsic isolation result: for $N\ge14$, the complete
sign-output interval contains at most one reduced rational with denominator
at most $\sqrt{N!}$, equivalently at most one candidate with
$g/D\ge\sqrt{N!}$.  Every Roth-scale candidate lies inside this singleton.
The theorem neither constructs nor excludes that candidate.

~~~
ebb50316d59ff22aa49512372547311fd5f36d24dd88825fcdf6b5ee0090b529  sources/common_kernel_native_output_bernstein_congruence_isolation.md
b5d97041916bf6401df95dbed4427fa910810a6f984f4b977bc6800a587ebca7  scripts/common_kernel_native_output_bernstein_congruence_certificate.py
d9e9defc6276f6efc9777511de9a3f779f893b65a38de7a4bf448dd8e5669762  results/common_kernel_native_output_bernstein_congruence_certificate.json
559cc412db81ed449d4255654ad370f44a8ceb4d8acdce234a7f607d448ffcb7  results/common_kernel_native_output_bernstein_congruence_hashes.sha256
~~~

The source proof, exact replay, dependency manifest, and control-byte audit
pass.  This sharpens the arithmetic target but does not establish primitive
decay, irrationality, or transcendence of $e+\pi$.

## Bessel checkpoint item 118: cube-threshold fibre law

The Bessel denominator now satisfies, for every $p\ge5$,



$$
\sum_{j=0}^4\binom4j q_{n+jp}
 \equiv12p^2q_n\pmod {p^3}.
$$



This fourth anti-period congruence makes the signed values on every root fibre
a cubic Newton polynomial modulo $p^3$.  Ordinary fibres have only one
possible cube representative.  On an all-square singular fibre, cube
divisibility is governed by an explicit degree-three polynomial over
$\mathbf F_p$: at most three representatives survive unless all four
Newton coefficients vanish and the complete fibre survives.

Reflection sends that polynomial to $P(-1-T)$.  Hence a paired noncentral
fibre has at most six cubes among $2p$ representatives unless it is wholly
singular; in the original $n<2p$ window, at most three of the four
representatives are cubes unless all four force the full branch.  The central
polynomial has degree at most two.  The exceptional/full-fibre alternatives
remain open.

~~~
7fe7bd5b2cef3dcb2a12f49c0c620d8d173d818774701a06f1527d80d574a6be  sources/bessel_prime_cube_fourth_antiperiod_exclusivity.md
6e4f612c0d1485de3858d1a9a13320cad766416737f281179c08860eddb30a6f  scripts/bessel_prime_cube_fourth_antiperiod_exclusivity_certificate.py
b60d7edd95835764161553ea68d377f2edafdda321b81137b0d19b45eb139dec  results/bessel_prime_cube_fourth_antiperiod_exclusivity_certificate.json
a46f0ca172db4ff4a8e41cae15bf32b9d61b95f7a71644bfe59b6c4594a854e6  results/bessel_prime_cube_fourth_antiperiod_exclusivity_hashes.sha256
~~~

The symbolic proof, dependency hashes, manifest, and replay pass.  The
remaining branches still prevent a little-oh valuation theorem and any
classification of $e+\pi$.

## Common-kernel checkpoint item 119: quantitative sign construction

The integer-Bernstein realization of every sign-possible native class is now
effective.  Optimizing the right endpoint with



$$
\ell=\frac{A}{\gcd(A,b)},\qquad \epsilon=(eA\ell)^{-1}
$$



preserves integral endpoint jets and gives $\ell=1$ whenever $a=0$.  An
explicit nearest-integer estimate and one-sided smooth crossing produce a
certified sufficient degree with



$$
\log n_{\rm suff}
 \le\frac N2\log A+O(N\log N)
 =\left(\frac12+o(1)\right)N^2\log N.
$$



The corresponding height satisfies
$\log H(h)\le n\log6+O(N\log N)$.  Its rational coordinate is an exact sum
of four beta moments, so the reduced denominator divides
$\operatorname {lcm}(1,\ldots,n+5)$.  No lower denominator bound and no
useful estimate for $\gcd(N!,c)$ follows, leaving primitive normalization
completely open.

~~~
0f5f69dcfd1ce4c2258c0333fe60f20275b1e21591c0e5e0c55bcea05a7acbbb  sources/common_kernel_integer_bernstein_quantitative_arithmetic_audit.md
17fcb7a1ff987981934c3852b7620af38073046de4a233ef613004e1af80c805  scripts/common_kernel_integer_bernstein_quantitative_arithmetic_certificate.py
5ff1c6949bca45a7d4f3bd5c0eb107bf356ab52107949c7aa83a7dec061a895d  results/common_kernel_integer_bernstein_quantitative_arithmetic_certificate.json
80ac4f4e108fd87b7549499abe702e0ddee83c45450ba338e820d18a5ab8437d  results/common_kernel_integer_bernstein_quantitative_arithmetic_hashes.sha256
~~~

The full constant audit, deterministic replay, and manifest pass.  Effectivity
does not supply the arithmetic cancellation needed for irrationality or
transcendence.

## Bessel checkpoint item 120: all higher anti-period layers

The second- and fourth-order congruences extend uniformly: whenever $p>2k$,



$$
\sum_{j=0}^{2k}\binom{2k}{j}q_{n+jp}
 \equiv\frac{(2k)!}{k!}p^kq_n\pmod {p^{k+1}},
$$



and the adjacent odd sum is zero modulo $p^k$.  The proof includes all
factorial valuations and the exact pair of Mahler endpoint constants.

On a root fibre this gives a Newton polynomial of degree $2k-1$ modulo
$p^{k+1}$.  After a fibre has survived completely through $p^k$, at most
$2k-1$ representatives reach the next threshold unless the whole divided
polynomial vanishes.  Reflection doubles the full-pair count, while central
symmetry lowers the degree by one.  This hierarchy controls branching fibres
but not the single ordinary lift path.

~~~
c0c834ca8851ddc8dba9edbc9ec74461c0d3aa1b553f79c2320b3d083a0c37de  sources/bessel_all_even_antiperiod_higher_threshold_exclusivity.md
b2f83c96c0166785d491ee0b2d776e67408e0b74f1211b6ea4e862216868c1f3  scripts/bessel_all_even_antiperiod_higher_threshold_exclusivity_certificate.py
53034eebf24139553ad006adedb9afab004e371558844166b1864a106cdce4dc  results/bessel_all_even_antiperiod_higher_threshold_exclusivity_certificate.json
a2ca08905562be561617da55d19620f829bef02ee303473fdb39bebe84f2d899  results/bessel_all_even_antiperiod_higher_threshold_exclusivity_hashes.sha256
~~~

The all-parameter proof, manifest, and exact replay pass.  The ordinary path
and full-fibre zero alternative still prevent the needed valuation theorem.

## Common-kernel checkpoint item 121: exact-moment approximation

For the native weight $W=(a+bt)t(2-t)^2$, every smooth function with
integral endpoint jets through order three and a rational $W$-moment can be
approximated in $C^3$ by integer polynomials with both the jets and that
moment preserved exactly.  In fact,



$$
4\int_0^1WB\mathbb Z[t]\,dt=\mathbb Q
$$



for every nonzero $B\in\mathbb Z[t]$.

The zero-moment kernel is parametrized by
${\cal D}S=2W'S+WS'$, for which
$\ell({\cal D}U)=4[W^2U]_0^1$.  Weighted integer-Bernstein estimates handle
both possible vanishing orders of $W$ at zero and retain four zero endpoint
jets after applying ${\cal D}$.

This means any rational point in a strict real output interval can be
realized exactly by an integer localizer.  However, the entire native output
range has width only $O(1/N)$, and such a width alone need not contain a
rational of sublinear denominator; an explicit one-sided Farey gap shows why.

~~~
61e396ba87dd73f66a5e7f322c13498aab2b9d0bcd6479895016753014e1e18e  sources/common_kernel_native_exact_moment_integer_approximation.md
9abb9e47a0719f0c0d2b64aa13c7d95c7f3579919e96630c89ab8e5e17fba1e5  scripts/common_kernel_native_exact_moment_integer_approximation_certificate.py
343a71d530acb7dd3681f38d26213f60dd8b8da8a4eb7216eaf6b482a2fc53ae  results/common_kernel_native_exact_moment_integer_approximation_certificate.json
aa35956007909d980f86d43909eaad180d56b9c80a654059425513a1debbb6b9  results/common_kernel_native_exact_moment_integer_approximation_hashes.sha256
~~~

The image theorem, weighted approximation proof, manifest, and replay pass.
The surviving obstruction is the arithmetic position of the small output
interval, not qualitative integer approximation.

## Common-kernel checkpoint item 122: sharp output width

The native sign output is a fixed-mass weighted average



$$
{\cal L}_N(G)=\int_0^1
 \left(e+\frac{4e^t}{t^2-2t+2}\right)(w+G')\,dt.
$$



It therefore lies strictly between $(e+2)B_N$ and $5eB_N$.
An explicit same-endpoint-germ mass-transfer family proves that the supremal
diameter has



$$
N{\cal W}_N\longrightarrow4-\frac2e,
$$



and supplies a fixed positive $c_*/N$ lower bound for every admissible
$N\ge8$.  This is also a sharp width-only obstruction: $Nw_N\to\infty$
is impossible, and the best width constant is too small relative to the raw
positive-output upper constant to force a rational-case contradiction.

~~~
7d4e9c5dc30c449ca369d52a3fb06e52ff681aedeb47b0dce45b2fc5239f36cc  sources/common_kernel_native_sign_output_range_sharp_width.md
1ee9c9572e165934294a0c5bd32fb4521f7dde406eaeae73b4d970a7870c1615  scripts/common_kernel_native_sign_output_range_sharp_width_certificate.py
25848e5590758fa622d14d45cb32b30a5e29d7c3022aff99de776f6946ec368b  results/common_kernel_native_sign_output_range_sharp_width_certificate.json
de1348caca545595e79ddc00929ece5d0ef7f18fb7eeb3f979beb26f2b766677  results/common_kernel_native_sign_output_range_sharp_width_hashes.sha256
~~~

## Bessel checkpoint item 123: ordinary harmonic layers

Every one of the four large-prime reflection-window evaluations now has an
exact terminating expansion in powers of $p$, whose coefficients are
explicit $p$-integral elementary symmetric harmonic sums.  The $j$-th
coefficient polynomial has degree at most $j+1$; the zeroth is $q_r$, and
the first reduces to the ordinary unit-slope law.  Thus the exceptional
valuation is reduced to a concrete recurrence-specific noncancellation
problem.

A linear countermodel satisfies reflection, unit slope, every proved
finite-difference hierarchy, permitted layer degrees, four-point
exclusivity, and the natural factorial height scale while retaining
valuation $\asymp p$.  Hence those structural inputs cannot by themselves
prove the required $o(p)$ bound.

~~~
28a91596edafac946448ea68f4c95dfdcd94e63bcf7586394c464a69d6a76e3d  sources/bessel_large_prime_ordinary_harmonic_expansion_barrier.md
6d0416020a1d1b1f1cfd9093c305b3826b6a32a13f20aea70a72a1017e4ff2c9  scripts/bessel_large_prime_ordinary_harmonic_expansion_barrier_certificate.py
35d48aa29c9ed42a00ab07f407a03f2193cfef72c2109891874a0f2e831a2ade  results/bessel_large_prime_ordinary_harmonic_expansion_barrier_certificate.json
8b3762971ff913e67e26e2cf82baffc4ecfb41b9bcbd79d23cbcad167b6d5348  results/bessel_large_prime_ordinary_harmonic_expansion_barrier_hashes.sha256
~~~

## Common-kernel checkpoint item 124: simultaneous exact moments

For every finite list of integer polynomial weights,
${\boldsymbol L}(\mathbb Z[t])={\boldsymbol L}(\mathbb Q[t])$; independent
weights have full rational moment image even in endpoint-zero ideals.  For
two independent native weights, a double differential kernel and weighted
integer Bernstein approximation preserve both rational moments and all
endpoint jets exactly in $C^3$.

A common strict profile exists for every finite sign-possible native system.
Compact interior bump directions rationalize both moments for an independent
pair before integer approximation.  Nevertheless, the two moments are
locally freely variable and factorial-ratio elimination destroys smallness,
so sharing one localizer supplies no primitive-content gain by itself.

~~~
73704b5408699aaff3c3254f8e6f8c10c321d22ad06952135aba192591c77d5a  sources/common_kernel_finite_multimoment_exact_approximation.md
738aa3a7ad75ffaea71fdefc95ebed2fa038696c887af57bf3e56e1e7c15ca86  scripts/common_kernel_finite_multimoment_exact_approximation_certificate.py
a50ae12cc7b9e137b5e50745e1d50b8700d1ce36e31d2be0425ed2d994c6a89a  results/common_kernel_finite_multimoment_exact_approximation_certificate.json
b53b8e6f1855fe3eb7ef1b1eae1c303fad3b9cd5344462616606794fd0d9ce6d  results/common_kernel_finite_multimoment_exact_approximation_hashes.sha256
~~~

All three packages were independently line-audited, replayed, and
manifest-verified.  They sharpen the frontier but do not prove that
$e+\pi$ is rational, irrational, algebraic, or transcendental.

## Common-kernel checkpoint item 125: exact fixed-index closure

The derivative constraint supplies a second pointwise obstacle that the
global mass range misses.  For
$J(t)=\int_t^1e^{-s}s^Nds$, every strict native profile obeys
$0<G<\min(\mu,J)$.  The increasing function $\mu$ and decreasing
function $J$ have a unique crossing, and the exact attainable output set is



$$
({\cal L}^{\min}_N,{\cal L}^{0}_N),\qquad
 {\cal L}^{\min}_N={\cal L}^{0}_N-
                    \int_0^1R'\min(\mu,J).
$$



Its closure includes both endpoints, even with fixed integral endpoint
germs, and ${\cal L}^{\min}_N>(e+2)B_N$ for every fixed admissible index.

For arithmetic use, a translated coordinate $c/D$ induces denominator
$Q=N!D/\gcd(N!,|c|)$, not generally $D$.  The old coordinate-grid hits
all fail the corresponding square-root bound on $Q$.  A separate exact
scan does certify genuine square-root-denominator hits at six indices
$25,33,43,88,164,331$, but no infinite pattern or strict approximation
exponent has been proved.

~~~
c9a018f47b54ed565c958da3dbd53b38b912238b63e56234dfb8a9e68ec99d42  sources/common_kernel_native_fixed_N_output_closure.md
75631e0c53a5851bc36f77d592c2c4737cdd4b4ebe8bc5a637062781e93be875  scripts/common_kernel_native_fixed_N_output_closure_certificate.py
a1bb13e6083592872cc0b90d466153e5cb5e76b0f3d685d218ca18cfb4b5ee45  results/common_kernel_native_fixed_N_output_closure_certificate.json
a5c167be7be4ee5924131c4e0dfa2f97ac64232b5a8c90242e6fb064c2d8fcab  results/common_kernel_native_fixed_N_output_closure_hashes.sha256
~~~

The theorem, exact replay, and frozen manifest pass.  This closes the
fixed-index geometric question without proving irrationality or
transcendence of $e+\pi$.

## Common-kernel checkpoint item 126: adjacent thin strips

For a common profile at sign-possible indices $N<M$, the normal coordinate
$T={\cal L}_N-(b_N/b_M){\cal L}_M$ has a sharp all-parameter split bound.
In the adjacent case it is factorially thinner than the broad output
coordinate, and the joint area has one additional factor $1/N$.

The arithmetic normalization reverses the apparent gain.  The inequality
$b_{N+1}\ge(7/2)b_N$ gives the universal positional separation



$$
T>\frac57B_N\ge\frac5{7e(N+1)}.
$$



After multiplying by the primitive integer factor
$b_M/\gcd(b_N,b_M)$, this normal is factorially far from zero for adjacent
indices.  The adjacent difference on the monotone residue classes has exact
infimum $D_N^0\sim5/N^2$, but under temporary rationality that one-sided
gap forces denominator $\Omega(N^2)$.  The unique factorial-cancelling
integer direction is likewise bounded away from zero.

~~~
a20afd820c91b4feef14479bb82b15dab1599a109b2463a6c5c97fc6edb5a8aa  sources/common_kernel_adjacent_joint_output_thin_strip_no_go.md
a26660b7b067571c348d221cf6e01ee9489903d4e7fbb9920caf30ef95970c72  scripts/common_kernel_adjacent_joint_output_thin_strip_certificate.py
8869c862afbe471cae5cf78694bbdaea812603ded1d87b8dba1f7aac5de466ae  results/common_kernel_adjacent_joint_output_thin_strip_certificate.json
df1f67b6f612402a0877ca937dc9494581f8ec3b58634f54abc418b475ec5ef6  results/common_kernel_adjacent_joint_output_thin_strip_hashes.sha256
~~~

The proof and replay pass independent audit.  The result rules out the
natural pairwise width, area, adjacent-difference, primitive-normal, and
factorial-cancel arguments; it leaves genuinely new numerator-content or
higher-output identities open.

## Bessel checkpoint item 127: Wilson-reduced layers and the first carry

The first three coefficient polynomials in the exact ordinary Bessel lift
are now reduced to three finite factorial-harmonic families by an all-prime
five-block Wilson reflection.  This gives a closed formula for the ordinary
slope, a four-endpoint table for the second and third raw layers, and an
explicit formula for the actual carried second digit.

The result identifies a hard obstruction that raw-layer arguments miss:



$$
{\cal C}_{p,r,j}(0)=0\quad\text{exactly for every }j\ge1.
$$



At the base endpoint the positive layers contain no information about the
valuation of $q_r$; at every other endpoint a raw layer can cancel against
the lower-layer carry.  Hence the next target is a recurrence-specific
noncancellation theorem for the carried combination, or an independent
exclusion of base-endpoint squares.

The exact formula detects a new finite square at
$(p,n)=(52453,66831)$, of valuation exactly two.  A duplicate exhaustive
CPU scan through $p<500000$ found no other square above $p=10000$, no
singular orbit, and no cube.  This finite evidence is not promoted to a
uniform theorem.

~~~
af171d428ac26019c3d98af3cd46a72cfa64db5a305857f369b05a6cfd5fa44f  sources/bessel_ordinary_first_three_layer_wilson_carry.md
6284b8afcbfed1349df814a7be0f4e507c59a9202308684ab7f706fbb366ad2a  scripts/bessel_ordinary_first_three_layer_wilson_carry_certificate.py
fde48d5d77ab0aa33fccdd6a9e229305e5e2c8c92a43fd8ec2ce5135b635bd86  scripts/bessel_ordinary_large_prime_scan.cpp
d27210380697091ae0e1f37573d1035c8c228885839c1d4720babaa4b3a2ef48  results/bessel_ordinary_first_three_layer_wilson_carry_certificate.json
76a9244467bac4c6b9ca35b534c8bbd73ae774e6e732fb298e85255b44035b54  results/bessel_ordinary_large_prime_scan_certificate.json
8404b4b76df36a327e29f7b444572326bf344b9691e2d522969723407956efa7  results/bessel_ordinary_first_three_layer_wilson_carry_hashes.sha256
~~~

The symbolic proof, carried witnesses, duplicate finite scan, and frozen
manifest all pass independent audit.  They sharpen the valuation frontier
without classifying $e+\pi$.

## Common-kernel checkpoint item 128: native continued-fraction windows

The exact fixed-index closure has the sharper endpoint expansions



$$
\begin{aligned}
 {\cal L}^{0}_N
 &=\frac5N-\frac4{N^2}-\frac5{N^3}+\frac{45}{N^4}+O(N^{-5}),\\
 {\cal L}^{\min}_N
 &=\left(1+\frac2e\right)
   \left(\frac1N-\frac1{N^3}+\frac1{N^4}+O(N^{-5})\right).
\end{aligned}
$$



Every reduced native hit with $N\ge10$ and $Q^2\le N!$ is therefore a
principal continued-fraction convergent of $e+\pi$, and necessarily lies
in the normalized window



$$
1<N\,N!\left(e+\pi-\frac PQ\right)<5.
$$



An outward-rounded exact rational enclosure at 5,856 decimal places certifies
the common continued-fraction prefix through the first denominator exceeding
$\lfloor\sqrt{2000!}\rfloor$.  The broad candidates for
$10\le N\le2000$ are
$25,33,43,86,88,164,331,351,1477$; the last three new candidates are in
forbidden native residue classes.  Combining this exhaustion with the pinned
fixed-index membership certificate proves that the complete admissible hit
set through 2000 is



$$
\{25,33,43,88,164,331\}.
$$



This is a finite theorem only.  Infinitely many admissible matches would be
needed even for irrationality; a fixed square-root power saving in $Q$ would
be needed for the recorded Roth route to transcendence.

~~~
c7464fc9dbcbd5bd26146a500da797abdaf8b25ea04f3444994ec46097088e16  sources/common_kernel_native_cf_window_scan.md
d127322e0362aa179a5358d4ca54116929666ddc77e41acc33859ae026ec6a03  scripts/common_kernel_native_cf_window_scan_certificate.py
051f52f528a9835fc33938e99952fa483ae32ca9d5bf4b2d0c862c829fa94d9f  results/common_kernel_native_cf_window_scan_certificate.json
45c9253a4d4572806c0650345f2e47e4d8953618daf5c87512a1d62e0e1cd958  results/common_kernel_native_cf_window_scan_hashes.sha256
~~~

The proof was line-audited, the exact replay was repeated independently, and
the frozen manifest passes.  No infinite continued-fraction pattern or
arithmetic classification is inferred from the finite scan.

## Common-kernel checkpoint item 129: multi-output Smith obstruction

After clearing beta moments, the simultaneous native response matrix factors
through only the two Gaussian columns $a_i,b_i$.  Thus arbitrarily many
shared outputs have only two variable moment directions; all higher minors
factor through the corresponding two-column Smith data.

For five consecutive sign-possible indices beginning at $N\equiv0\pmod8$,
there is a primitive integer relation annihilating the factorial, Gaussian
real, and Gaussian imaginary columns whose exact invariant is



$$
\delta_N=\frac{2\eta_N}{(N+2)(N+3)},
 \qquad
 \eta_N=
 \begin{cases}
 71,&N\equiv16\pmod{71},\\
 1,&\text{otherwise}.
 \end{cases}
$$



This is a genuine $O(N^{-2})$ primitive combination, but its reduced
denominator is exactly



$$
Q_N=\frac{(N+2)(N+3)}2,
$$



and $Q_N$ divides every common denominator of the five rational correction
coordinates.  Hence denominator clearing turns $\delta_N$ into a nonzero
integer rather than a contradiction.  Four outputs give an invariant of size
$\asymp N^2$; five and higher outputs also carry exact-zero relations.

~~~
ea090145c760599bd1eb4a85192aa330da72cc8f6bebaebaff25b827e28c0367  sources/common_kernel_multioutput_smith_quadratic_denominator_obstruction.md
a346881d779d2c272a8a342bd3a16099134d3ba68e00f807672609192728df43  scripts/common_kernel_multioutput_smith_quadratic_denominator_certificate.py
cc8740eee8eb4c470cfca2ae1cb91c7898b0722a14b8a37eadb6b76e7c606e1e  results/common_kernel_multioutput_smith_quadratic_denominator_certificate.json
786c6e2c2f25aa1cd11a0b0b480277eaaacd1a8bda54b70af2ad9f6d46939fe5  results/common_kernel_multioutput_smith_quadratic_denominator_hashes.sha256
~~~

The symbolic identities, Smith generators, resultants, denominator divisors,
markup, and pinned dependencies passed independent replay.  The theorem
closes this higher-output shortcut but does not classify $e+\pi$.

## Bessel checkpoint item 130: symmetric transfer and base carry

For an ordinary Bessel root $p\mid q_r$, $s=p-1-r$, the exact reflection
transfer is



$$
M_{p,r}\equiv
 \begin{pmatrix}1&0\\4r+2&1\end{pmatrix}\pmod p.
$$



Writing $h=(p-3)/2-r$ and letting ${\cal K}_h$ be the continuant of the
odd symmetric list centered at $X$, the ordinary slope separates as



$$
\delta\equiv-2{\cal K}'_h(0)q_{r-1}\pmod p.
$$



The base quotient $q_r/p\bmod p$ does not occur.  A positive Charlier
connection makes the missing datum explicit: ordinary simplicity compares
two lift derivatives, whereas base squarefreeness compares a partial-injection
quotient with one derivative.  Neither congruence implies the other.

At the next threshold, if $q_r/p\equiv c+pd\pmod{p^2}$, the carried digit
has the exact form



$$
\frac{F_{p,r}(Z_0)}{p^2}\equiv d+\Psi_{p,r}(Z_0)\pmod p.
$$



The new base digit $d$ has unit coefficient, so a resultant involving only
the previously isolated raw layers cannot exclude the next cancellation.
Exact altered-initial-value countermodels show why the recurrence and ordinary
slope alone cannot restore this missing information.

~~~
769c886c1c8e5a6e406bd2018c71846e2831170359c2e97b43939e200a108c6e  sources/bessel_ordinary_symmetric_transfer_base_carry_barrier.md
7dbe32fb6ab59c001724543ea4a7e3657e9a5b6bb24ad918e363b549d285c9ec  scripts/bessel_ordinary_symmetric_transfer_base_carry_certificate.py
7f964cbbd5d0cdc749959614ae3e54e92bc8914227005fc9f4acf168a127512b  results/bessel_ordinary_symmetric_transfer_base_carry_certificate.json
bda724f3790cda56b5bc67fb99ccc854c693da1a2c7d53c85108e4cda394b5e6  results/bessel_ordinary_symmetric_transfer_base_carry_hashes.sha256
~~~

The transfer signs, Charlier signs, carry representatives, countermodels,
dependencies, and deterministic replay passed audit.  This isolates a new
recurrence-specific proof obligation; it supplies no valuation bound or
classification of $e+\pi$.

## Common-kernel checkpoint item 131: factorial-entry CF dichotomy

For an irrational $x$, let $p_k/q_k<x$ be a below-side principal
continued-fraction convergent, retaining its index in the full convergent
sequence.  For a fixed $0\leq\delta<1/2$, put



$$
\tau=\frac{2}{1-2\delta}
$$



and take the first native-admissible $N$ for which
$q_k^\tau\leq N!$.  The maximum gap four in the admissible residue set
gives the exact entry-phase bound



$$
1\leq\frac{N!}{q_k^\tau}<N^4.
$$



If the normalized error


$$
Z_k=N\,N!\left(x-\frac{p_k}{q_k}\right)
$$


misses the native interval $1<A_N<B_N<5$, the two possible misses have
opposite continued-fraction consequences:



$$
\begin{aligned}
 Z_k\leq A_N
 &\Longrightarrow
 a_{k+1}>\frac{N}{5}\frac{N!}{q_k^2}-2,\\
 Z_k\geq B_N
 &\Longrightarrow
 a_{k+1}<N\frac{N!}{q_k^2}.
\end{aligned}
$$



Thus infinitely many low misses at any fixed $\delta>0$ force the
below-side irrationality exponent to be at least
$\tau>2$, while eventual high misses give the upper bound
$\mu_-(x)\leq\tau$.  At $\delta=0$, the low case supplies only a
logarithmic improvement over exponent two.

The golden ratio is an exact countermodel to any stronger abstract
miss-to-large-partial-quotient inference: it has no sufficiently large
factorial-window hits, even after completing all residue classes, although
all its partial quotients are one.  More generally, catching a badly
approximable number at the square-root cutoff requires a largest window
scale of order $N$.  Independently, connected coverage of the factorial
jump by fixed-ratio windows requires $\Omega(\log N)$ copies; this latter
count controls relative span only and does not locate the absolute scale.

~~~
572ae7a426a22e1775a774732629c71d005dc0d1214288231bb8dd1456db3714  sources/common_kernel_factorial_window_cf_entry_dichotomy.md
d61d0617f8d1322d07d13f13b01e87366b1a7175b086128cc0096406b38aa3d4  scripts/common_kernel_factorial_window_cf_entry_dichotomy_certificate.py
401ef6b199eacf4f72ab41f7bd673e440f3c6dc7e0ce84b28571b2611d67f99e  results/common_kernel_factorial_window_cf_entry_dichotomy_certificate.json
e020e4c07067054101c4755b0a3899b79d93c7db468b0162daf2d946e1e944bc  results/common_kernel_factorial_window_cf_entry_dichotomy_hashes.sha256
~~~

Two independent deterministic replays, the pinned dependency, markup and
control-byte audits, and the frozen manifest pass.  This theorem sharply
classifies what entry misses imply, but it proves no irrationality or
transcendence result for $e+\pi$.

## Bessel checkpoint item 132: symmetric-continuant derivative theorem

For the symmetric plus-sign continuant



$$
{\cal K}_h(X)=[X-4h,X-4h+4,\ldots,X+4h],
$$



let



$$
P_{h,j}=[4(j+1),4(j+2),\ldots,4h].
$$



An all-parameter cofactor calculation now gives



$$
{\cal K}'_h(0)=(-1)^h\left(
 P_{h,0}^2+2\sum_{j=1}^h(-1)^jP_{h,j}^2\right),
$$



with the independent terminating formula



$$
{\cal K}'_h(0)=
 \sum_{a=0}^h(-16)^a(a!)^2
 \binom{h+a+1}{2a+1}.
$$



The tail recurrence proves the strict uniform bounds



$$
\frac{13}{15}P_{h,0}^2
 <(-1)^h{\cal K}'_h(0)
 <\frac{17}{15}P_{h,0}^2.
$$



Hence the derivative is a nonzero integer with sign $(-1)^h$.  The same
quantity is the determinant of an explicit pentadiagonal matrix obtained
from the even--odd block decomposition of the symmetric continuant.

This real/integer nonvanishing is not the required modular theorem:
${\cal K}'_2(0)=963=3^2\cdot107$.  The ordinary Bessel root condition
still requires nonvanishing of this determinant modulo $p$, and the
separate base-square congruence remains uncoupled.

~~~
9d553e597f353915d16279031f4d0415342f8dfde628c925bcabd51e442f0d57  sources/bessel_symmetric_continuant_lommel_derivative_theorem.md
7e6816a4fbd63b818d1ea1acd370c274df1eeb2516ff2c5b5881a78f4619569c  scripts/bessel_symmetric_continuant_lommel_derivative_certificate.py
3b78a0cd61d0bf701db017a4a0a71fe59399aaa2e87e98e01c44c3baa2c5227e  results/bessel_symmetric_continuant_lommel_derivative_certificate.json
711d2f95dc6a8acee83b8a92b472d668f5aafcb4020197fe96ecfe3d8ea09bcf  results/bessel_symmetric_continuant_lommel_derivative_hashes.sha256
~~~

The two independent formulas, tail inequalities, block signs,
Cauchy--Binet minors, frozen dependency, and manifest passed root replay.
The package sharpens the finite-field target without proving a valuation
bound or classifying $e+\pi$.

## Mixed-cubic checkpoint item 133: Cartier content and sharp denominator

On the boundary ray



$$
H_s=\int_0^1
 \frac{\{x(1-x)\}^{6m}}
 {\{(1+x)(1+x^2)\}^{4m+1+s}}\,dx
 \quad(s=0,1,2),
$$



write



$$
H_s=R_s+\frac{L_s}{4}\log2+\frac{E_s}{8}\pi
$$



and form
$\Lambda_{01}=L_1H_0-L_0H_1=A_m+B_m\pi$.
Exact partial fractions first give the clearing



$$
2^{9m+5}M_{4m+1}.
$$



A new relative-Cartier endpoint lemma then proves that every prime
$2m<p<3m$ cancels from the rational determinant denominator.  Thus the
strictly sharper all-parameter clearing is



$$
{\cal D}^{\sharp}_m=
 \frac{2^{9m+5}M_{4m+1}}
 {\displaystyle\prod_{2m<p<3m}p}.
$$



Independently, an exact-differential Cartier criterion supplies a disjoint
common-content product whose logarithm is



$$
\left(-4\log2+\frac{\pi}{\sqrt3}+3\log3\right)m+o(m).
$$



The middle-band cancellation follows because, after Frobenius extraction,
both transformed residual differentials have only the two simple poles
$\pm i$, are regular at infinity, and therefore lie in one common
one-dimensional differential space.  Their relative rational/logarithmic/
$\pi$ coordinate vectors are proportional modulo $p$.

There are two further exact structural identities.  A derivative
coboundary gives



$$
a_mH_0+b_mH_1+c_mH_2=0,
$$



so the next adjacent log-cancelled form is merely
$(a_m/c_m)\Lambda_{01}$.  A contour integration by parts removes the
leading residue ratio $5/8$ and identifies the first nonzero candidate
determinant amplitude.

The arithmetic improvement is decisive but not yet a proof.  Conditional
on the explicitly unproved assertion that the accessible complex saddle
$\tau=0.3933435869\ldots+0.2348766139\ldots i$ uniquely dominates both
coefficient contours, the certified decay and height rates would satisfy



$$
d=2.3370623743\ldots,\qquad
 h_{\rm cert}=2.3246783391\ldots,\qquad
 \frac d{h_{\rm cert}}=1.0053272038\ldots>1.
$$



This numerical margin was originally described as sufficient for a positive
$e$-form matching route.  The later exact audit in item 137 corrects that
statement: without a separately proved exponential matching-content gain, the
generic threshold is $d>2h$, not $d>h$.  Thus even after the saddle
dominance and uniform asymptotic were proved in items 135--136, this branch did
not establish irrationality of $e+\pi$.

~~~
286d9cf4d3591a1a9b9fefc6dd3ee3dcc9f7c2ba49a73310909491814544d9e8  sources/mixed_cubic_boundary_cartier_content_and_recurrence.md
81d9fa515ba39719d17a5f35456e3749d34f8d857a0411b97fff228c39a36d6d  scripts/mixed_cubic_boundary_cartier_content_and_recurrence_certificate.py
3a060ecf43afe8a5047401cfed9ac2208345b5f2636ef88c14ce959324dace29  results/mixed_cubic_boundary_cartier_content_and_recurrence_certificate.json
34e61497fa2df8dd4dfcaf143be574bd3ada434977d41e6be75b590ba927a14c  results/mixed_cubic_boundary_cartier_content_and_recurrence_hashes.sha256
~~~

The dyadic count, quotient degrees, relative-Cartier lemma, prime products,
recurrence, contour identities, dependency, controls, and deterministic
replay passed independent audit.  The contour theorem was the next analytic
gap at item 133.  It was subsequently closed in items 135--136, after which
item 137 identified the independent factor-of-two matching barrier.

## Common-kernel checkpoint item 134: rational-case denominator saturation

Assume temporarily that $s=e+\pi=u/v$ and $v\mid N!$, so
$M=N!s$ is an integer.  The exact fixed-index closure and exact-moment
integer approximation theorems then imply that the strict native integer
outputs are precisely



$$
\mathbb Q\cap({\cal L}^{\min}_N,{\cal L}^{0}_N).
$$



Integer translation preserves reduced denominators: if an output is
$m/D>0$ in lowest terms, its coordinate is



$$
\rho=\frac{m-MD}{D},\qquad (m-MD,D)=1.
$$



Consequently every strict integer localizer satisfies



$$
D{\cal L}^{0}_N>m\geq1.
$$



Thus the proposed positive-integer contradiction
$D{\cal L}^{0}_N<1$ cannot be obtained merely by selecting a rational
point in the exact real-output interval under the same rationality
hypothesis.

The obstruction is asymptotically sharp.  For every admissible
$N\geq1246$, put $D_N=\lfloor N/5\rfloor+1$.  Exact beta bounds and
the certified output width give



$$
{\cal L}^{\min}_N<\frac1{D_N}<{\cal L}^{0}_N,
\qquad
 1<D_N{\cal L}^{0}_N<1+\frac5N.
$$



Under the rationality hypothesis, exact-moment approximation realizes the
output $1/D_N$ with coordinate denominator exactly $D_N$, so
$D_N{\cal L}_{N,h}=1$.  This closes the qualitative interval-selection
shortcut, not the possibility of a separate arithmetic construction that
would itself contradict rationality.

~~~
52a554fd8c39d2caa641fafbbb43ad572b5e736e70c230793d5ece365da30332  sources/common_kernel_rational_case_denominator_saturation_barrier.md
d96c493f3af8e62638a23562ae096f732bcaf4306bcdee2e98ab05713fde0905  scripts/common_kernel_rational_case_denominator_saturation_certificate.py
c51ba0bdc55ac3ebc2220dcdfb44c7a728b8c80059f1cac99aa395d5cfb78371  results/common_kernel_rational_case_denominator_saturation_certificate.json
a90239b6de95a344d41728ee404dfde0d3a5c8ab8f6368e7bfdd1316c5c9dadf  results/common_kernel_rational_case_denominator_saturation_hashes.sha256
~~~

The five pinned dependencies, exact constant bounds, denominator
minimality, strict threshold, controls, markup, repeated replay, and frozen
manifest pass.  The theorem is conditional and proves no classification of
$e+\pi$.

## Temporary research pause — 2026-08-27 UTC

The user requested a durable handoff and a temporary stop.  All active workers
have stopped.  No proof that $e+\pi$ is algebraic, irrational, or
transcendental has been obtained.

The latest frozen packages are items 131--134 in
`active_checkpoint_20260827.md`.  The unfinished mixed-cubic saddle work is
preserved separately in:

- `sources/mixed_cubic_boundary_saddle_handoff.md`;
- `sources/mixed_cubic_accessible_saddle_handoff_20260827.md`.

The immediate resumable task is an exact Sturm/interval certificate proving
that the proposed saddle is the unique maximum of $|\Psi|$ on its valid
fixed coefficient circle, followed by a uniform two-amplitude complex-Laplace
argument.  The second handoff note contains the exact algebraic
parametrization and a six-step replay plan.  The current numerical sign table
is evidence only.  Completing this branch is designed to prove irrationality,
not yet the requested algebraic/transcendental classification.

The authoritative detailed state, hashes, inventory, and theorem/evidence
boundary are in `active_checkpoint_20260827.md`.

## Resumed mixed-cubic completion and temporary pause — 2026-08-28 UTC

The two unfinished analytic tasks from the prior handoff are now closed.  Item
135 gives an exact algebraic/Sturm certificate that the selected accessible
saddle is the unique global maximum on its valid fixed coefficient circle.
Item 136 proves the uniform two-amplitude complex-Laplace expansion and the
eventual nonzero determinant coefficient.  Together with item 133, these
packages unconditionally give shrinking integer forms in $1,\pi$, whose
nonvanishing uses the independently known irrationality of $\pi$.

A downstream audit then corrected an important error in the old handoff.  With



$$
h=2.324678339143731110\ldots,
 \qquad d=2.337062374358972996\ldots,
$$



generic positive matching with the standard beta form for $e$ balances at
$t=d/2$, leaving



$$
h-d/2=1.156147151964244612\ldots>0.
$$



Thus the no-extra-content threshold is $d>2h$, not $d>h$.  Item 137
proves the exact minimal matching and shows that irrationality via this route
requires a new exponential content rate $\Gamma>h-d/2$, while a Roth-level
transcendence result requires $\Gamma>h$.  Item 138 computes the exact
outside-prime product and proves that the existing clearing/Cartier statements
alone imply neither a fixed-support nor a moving-support Subspace-Theorem
hypothesis.  This is an insufficiency result; it does not show that the actual
mixed-cubic coordinates lack additional useful structure.

No proof that $e+\pi$ is irrational, algebraic, or transcendental has been
obtained.  Research is temporarily stopped at the user's request.  The new
authoritative handoff, exact hashes, audit status, and continuation targets are
in `active_checkpoint_20260828.md`.  A fresh external backup is stored at
`/content/drive/MyDrive/e_pi_research_20260826_backup_20260828T001000Z_handoff_item138.tar.gz`
with an adjacent SHA-256 sidecar.

The final-stop addendum in `active_checkpoint_20260828.md` records a brief
automatic continuation and its immediate termination at the user's reiterated
deadline.  No new theorem package resulted.  The last backup, including that
addendum, is
`/content/drive/MyDrive/e_pi_research_20260826_backup_20260828T001900Z_final_pause_item138.tar.gz`.

## Active continuation — items 139--162

The temporary pause above has been superseded.  Research is active again.
Item 139 proves a cross-order factorial determinant and support-dispersion
theorem, excluding bounded multiplicative base windows with genuinely
subdiagonal orders.  Item 140 gives a replayed exact audit of all 15,150
canonical positive mixed-cubic/beta matches with $m\le100$ and
parity-compatible $N\le6m$; every certified lower bound remains greater
than one.

Item 141 reduces the beta synchronization gcd to equal prime-valuation CRT
classes and isolates the unresolved small-representative/Wieferich problem.
Item 142 proves, uniformly for every $m\ge1$, that no prime in
$6m<p<6m+49$ divides both raw mixed-cubic coordinates.  Item 143 records
exact Gaussian, valuation, recurrence, and hypergeometric reductions, plus
deterministic finite scans: no fresh log-residue gcd prime through $m=2000$
and no exceptional-ray common zero through $m=10000$.

Item 144 upgrades the exceptional-ray evidence to a uniform theorem: whenever
$p=10m+3$ is prime, the two mixed-cubic logarithmic residues cannot both
vanish modulo $p$.  Its proof uses an exact residue recurrence for
$y^5-y$ and a nonzero global-residue binomial anchor.

Item 145 identifies the factorial diagonal denominator exactly with the beta
denominator $q_n$, eliminates the beta numerator from the selected gcd, and
proves conditional harmonic-support and short-block dispersion theorems for
the near-diagonal regime.

Item 146 reduces every nonexceptional fresh prime to two adjacent
coefficients of a two-pole rational function.  It proves 16 infinite fixed-gap
families and a conditional moving-gap height exclusion; at that stage,
uniform nonvanishing of the resulting connection determinant remained open.

Item 147 extends the $y^5-y$ residue mechanism from the exceptional ray
$p=10m+3$ to every prime ray $p=10m+b$ with
$b\in\{1,3,7,9,11,13,17,19,21,23\}$.  A two-state residue reduction,
nonzero global binomial anchor, exact fixed determinant, complete factorization,
and nine direct replays prove that the two logarithmic residues never vanish
simultaneously on any of these ten infinite rays.  Nine rays are new.

Item 148 proves the exact 3-adic valuation
$v_3(\mathcal R_q)=1-D(q-1)-D((q-1)/2)$ for every positive odd
$q$ with $3\nmid q$.  Hence every admissible connection determinant is
nonzero.  This removes the characteristic-zero determinant obstruction
uniformly, while leaving the final numerator-prime/power-of-two congruence.

Item 149 proves the first unconditional positive exponential lower bound for
the actual post-Cartier mixed-cubic content.  A prime-power-layer Cartier
argument forces $\prod_{p\in\mathcal H_m}p\mid c_m$ and gives
$\liminf\log c_m/(6m)\ge0.13651416829481281845\ldots$.  The required rate is
$1.1561471519642446\ldots$, so an explicit
$1.01963298366943179388\ldots$ per-$6m$ deficit remains.

Item 150 extends the uniform slope-10 theorem to every admissible odd
intercept $b\le57$.  It supplies closed terminating Pochhammer formulas for
the two parity determinants and sparse one-binomial formulas for the two
surviving states.  Exact factorization and replay close 13 new infinite rays;
a separate modular certificate proves determinant nonvanishing for all 1,600
parity rows with admissible $b\le2001$, without claiming full ray closure
beyond 57.

Item 151 classifies the next, rank-two Cartier layer by one exact
$2\times2$ coefficient determinant and proves that every vanishing row
contributes an additional squarefree prime to the actual post-$G_m$ content.
Three uniform zero rays are proved, but for fixed $m$ their product is only
polynomial in $m$, hence has zero exponential rate.  More decisively, even
the hypothetical radical contribution from every rank-two floor cell is at
most $(6-\pi/\sqrt3-3\log3)m+o(m)$, leaving a normalized deficit of at least
$0.87123902204252294801\ldots$.  Thus higher prime-power multiplicity or a
substantially deeper mechanism is unavoidable.

Item 152 isolates two uniform slope-10 targets without overstating either.
An exact audit verifies a conjectural 2-adic deflation law for both parities
and all 79 admissible odd intercepts $7\le b\le201$ (158 rows), while an
independent reconstruction checks representative determinants and the full
cyclic identities.  The proved moment recurrence and cyclic product reduce
simultaneous vanishing to the $T^0$ and $T^4$ coefficients of one explicit
product.  The 2-adic pattern would prove only formal determinant
nonvanishing; odd numerator primes would still require replay or a separate
support theorem.

Item 153 corrects and closes the attempted fresh-prime m-ray reduction.  The
missing factor $z^{p-q}$ invalidates the discarded same-A window; with the
correct A/B windows, exact finite-pole projection proves that the two
conditions are precisely the old $(\Lambda_1,\Lambda_2)$ obstruction up to
powers of two.  Exact replay passes all 14 direct samples, and a finite scan
through $m=1000$ finds only 2-power denominators and a scaled gcd dividing
$(6m)!$; this is evidence, not a uniform divisibility theorem.  Two exact
recurrence analyses then delimit shortcuts: the complete nonresonant
simple-pole three-term system fails at its next row, while an independent
inverse-cubic model has generic differential order three but an eight-term
coefficient recurrence.  At the target row the known triple zero does not
give an immediate one-row pivot; multi-row/global propagation remains open.

Item 154 closes that scalar-recurrence question globally.  The sum of the
three inverse-cubic branches is the $t^2$-coefficient of a cubic remainder,
hence an integer polynomial of degree $4m-1$ with leading coefficient
$-10m$.  It is nonzero modulo every prime $p>6m$, satisfies every row of
the same eight-term recurrence, and has an identically zero tail from degree
$4m$ onward.  Thus no recurrence-only argument, even using the full tail,
can force a contradiction.  Quotienting by this trace line is also
insufficient: at the exact fresh prime $(m,p)=(2,112291)$, the target map
has rank one and a two-dimensional kernel, although the distinguished branch
itself has a nonzero target.  Branch-specific Cartier/Frobenius information
is therefore essential.

Item 155 proves that the distinguished inverse branch is uniformly transverse
to the trace line.  After removing a power of two, its initial vector is
$V=(32,32-24n,9n^2-41n+36)$, and the exact gcd of the three minors of
$\tau\wedge V$ is $2^{3m}$ for odd $m$, or
$3\,2^{3m+4}m(3m-1)$ for even $m$.  No prime $p>6m$ divides this gcd.
Thus a hypothetical zero target triple would place two independent genuine
branch series in the target kernel and force intrinsic target rank at most one.
This statement remains valid on $p=12m-1$, where the rational
arbitrary-initial-coordinate transfer itself cannot be reduced.  Rank one is
not contradictory, so the final branch-specific support obstruction remains.

Item 156 computes the exact determinant of the first-three-coefficient matrix
of all three genuine inverse branches:


$$
-i\,2^{2n-7}n(n-2)(2n-1),\qquad n=6m.
$$


For a prime $p>n$, the branch initial coordinates are therefore invertible
except precisely when $p=2n-1=12m-1$.  This explains the exceptional
denominator in the rational transfer and independently confirms why item 155
must use its intrinsic branch-span formulation there.

Item 157 gives a uniform Smith-normal-form reduction of the remaining
fixed-gap cube obstruction.  Away from $2$ and $3$, a complete expansion
of all twenty maximal minors and a DVR lemma prove



$$
G_q\mid\Delta_3(q)\mid d_3(q)^3
$$



for the explicit $3\times6$ cubic multiplication matrix.  Exact replay for
all 334 admissible odd $q\le1001$ verifies $d_3(q)\mid P_q$, and hence
$G_q\mid P_q^3$, only in that finite range.  The uniform divisibility
$d_3(q)\mid P_q$, and therefore the unconditional compatible-fresh-prime
exclusion, remain open.

Item 158 identifies a characteristic-$p$ infinity resonance missed by a
proposed Cartier/Hermite closure.  The valid reduction gives
$D_A(V)=c_1Q-c_0$ with $\deg V\le2p$, and the exact monomial action
forces



$$
\deg V\le1\quad\text{or}\quad\deg V=p+1.
$$



Exact degree-$p+1$ witnesses occur at
$(p,q)=(11,5),(31,13),(97,13)$ and match the actual residue ratios.  None
has $B_0=B_1=0$, so these witnesses refute only the bounded-primitive step;
they are neither common-zero counterexamples nor a proof of fresh-prime
nonvanishing.

Item 159 gives an exact endpoint/Kummer formulation of the fixed-gap pair.
The two rows are contiguous residues of one differential, with



$$
\lambda_s=-\mathcal L_\xi(\omega_s),\qquad
 \xi^3=2,\qquad
 \frac{\omega_{s+1}}{\omega_s}=\frac{(1+t)^3}{1+t^2}.
$$



The actual transform between the $T_s$ and $C_s$ endpoints is the
involution $z\mapsto2/z$.  The genuine order-three automorphisms of
$y^3=1+t^2$ instead move the poles $0,1$ into two distinct three-point
orbits, so the two-residue problem is not closed under that symmetry.  The
coordinate $S=2/(1+t)$ bridges this formulation exactly to the existing
inverse cubic; it does not produce an independent closure.

The identity



$$
P_q=3^{q-1}(q-1)!\binom{(2q-3)/3}{q-1}
$$



supplies necessary Pochhammer nonresonance away from $6P_q$, but no
jet/Bezout reduction.  The exact $q\le301$ replay is finite control for the
symbolic identities.  Item 159 does not prove $d_3(q)\mid P_q$,
fresh-prime nonvanishing, or any classification of $e+\pi$.

Item 160 begins the requested higher-prime-power Cartier continuation with an
independent exact ledger audit.  **PROVED:** the corrected constants are



$$
T=1.1561471519642446123307302239\ldots,
 \qquad r_1=0.1365141682948128184504238226\ldots,
$$



so the currently proved deficit is
$T-r_1=1.0196329836694317938803064012\ldots$ per $6m$.  The old
binary64-style decimal tails in the mutable overviews were corrected; no
symbolic formula, sign, or theorem changed.  For every prime forced by the
item-149 rank-one set or item-151 rank-two zero set, and
$1\le r\le e_p+1$, item 160 proves the exact bridge



$$
p^r\mid c_m
 \iff v_p(q_pA_m)\ge r+\delta_{m,p}.
$$



This reduces higher divisibility to one lifted coordinate but does not force
an additional digit.  Exact actual-coordinate counterexamples show that a
top layer $q_p=p^2$, a previously removed $G_m$-digit, and a vanishing
rank-two determinant can each leave $v_p(c_m)=1$.  The matching factors
$c_m,\Delta_m,g_m$ remain legitimate only in their frozen sequential
normalization; computing $\Delta_m$ from raw $V_m$ can overcount it.

**EXPERIMENTAL:** for $m\le100$, 725 of 928 forced rank-one pairs and 63
of 120 vanishing rank-two pairs are sharp at one digit.  Two simple lift
patterns fail on the exact frozen grid, but these counts imply no asymptotic
frequency theorem.  **OPEN:** obtain a genuine modulo-$p^2$, Witt, Dwork,
or equivalent endpoint formula that vanishes on a family of positive weighted
mass.  Standard inversion of the selected comparison matrix is unavailable
on its singular content locus; no ambient Hasse--Witt no-go theorem is
claimed.  The authoritative manifest is
`results/higher_power_cartier_actual_valuation_hashes.sha256` (SHA-256
`e50b59c2823a6d07375f6d8f05d363499f0e58a948bb541a6b98d57a41ff1e14`).
Item 160 does not classify $e+\pi$.

Item 161 replaces the vague request for an integral lift by two compatible
exact formulas.  At the three finite poles $\alpha\in\{-1,i,-i\}$, let



$$
C_{s,\alpha}(r)=[t^r]\,
 {u(\alpha+t)^{6m}\over Q_\alpha(\alpha+t)^{4m+1+s}}.
$$



If $q=p^e$, $D=1+\delta_{m,p}$, and



$$
\mathcal B_{s,h}=
\sum_\alpha\sum_{\substack{k\ge1,\ p\nmid k\\
p^{e-h}k\le4m+s}}
 {C_{s,\alpha}(4m+s-p^{e-h}k)\over k}
 H_\alpha(p^{e-h}k),
$$



then the exact endpoint lift is



$$
qR_s\equiv
\sum_{h=0}^{\min(e,D)}p^h\mathcal B_{s,h}
\pmod {p^{D+1}},
$$



and substitution into
$qA_m=L_1(qR_0)-L_0(qR_1)$ gives the next digit
$\eta_{m,p}=qA_m/p^D\bmod p$.  Thus the non-rank-zero branch is a genuine
modulo-$p^2$ formula and the already-divided rank-zero branch is a
modulo-$p^3$ formula.

On every fixed positive-mass rank-one band, a second derivation proves the
Bockstein collapse



$$
{L_1X_0-L_0X_1\over p}
\equiv V_L\bigl(B-pR(\eta)\bigr)+V_RL(\eta)\pmod p,
\qquad
\eta=F^{p-1}F'T\,dx,
$$



where $T'=\gamma_1P_0-\gamma_0P_1$.  The cancellation of the
$x^{p-1}$ coefficient makes $T$ $p$-integral; no division by a
possibly zero Cartier scalar occurs.  A direct universal formula is required
on the sharp pole-order edge $h=p$.

**PROVED obstruction:** literal truncation to the top $q$-band fails at
$(m,p)=(6,7)$: it gives $3$, while the full lift and frozen coordinate
give $4\bmod7$.  Fixed-precision bounded local jets cannot determine the
next valuation in the ambient differential class.  The exact sequential
primewise ledger for $c_m\Delta_mg_m$ is also proved, as is the divisor
safeguard $c_m\Delta_mg_m\mid |V_m|q_N$.

**EXPERIMENTAL:** the exact replay agrees on all 118 forced rows with
$m\le30$; removing lower bands changes 64 digits and 45 complete digits
vanish.  A separate $(46,11)$ spot check exercises the third band.  These
finite counts imply no positive logarithmic mass.

**OPEN:** prove enough weighted vanishing or deeper/matching mass to exceed
the exact remaining sequential threshold
$1.0196329836694317938803064012400587396\ldots$ per $6m$.
The authoritative manifest is
results/lifted_endpoint_hasse_bockstein_and_sequential_mass_hashes.sha256
(SHA-256
0eaa6eb73068d776797425d15d13c4800dcc9452f09eac3e06bf2b3cd8214ada).
Item 161 does not classify $e+\pi$.

Item 162 extends the exact lifted-digit census to every forced row with
$m\le100$: 1,048 unique rows, 260 zeros, zero frozen-coordinate
mismatches, and 734 digits changed by deleting lower Hasse bands.  These
counts are exact finite diagnostics, not density statements.

More importantly, item 162 proves a uniform square-divisor congruence slab.
If $p\equiv19\pmod {20}$ is prime and



$$
p\mid10m+1,\qquad p\le4m+1<p^2,
$$



then $q_p=p$, $\delta_{m,p}=0$, both first Cartier scalars vanish, and



$$
\boxed{\eta_{m,p}=0,\qquad p^2\mid c_m.}
$$



Equivalently,



$$
p=20k+19,\qquad m=18k+17+\ell p,\qquad \ell\ge0,
$$



inside the $e_p=1$ band.  The subray $\ell=0$, or
$9p=10m+1$, is infinite by Dirichlet's theorem.  The proof is an exact
support calculation:



$$
P_0=x^r(1-x^4)^r,\qquad
P_1=x^r(1-x)(1-x^4)^{r-1},
\qquad
p-1-r\equiv3\pmod4,
$$



so both selected coefficients vanish.

This new divisor theorem is rigorously thin.  At fixed $m$, every selected
prime divides $10m+1$, hence



$$
\sum_{p\in\mathcal S_m}\log p\le\log(10m+1)=o(m).
$$



Item 162 also proves a broader capacity obstruction.  Even if every possible
item-149/item-151 prime had both its first and second forced digits, their
absolute optimistic rate would be at most



$$
2\left(r_1+{C_2\over6}\right)
=0.5698162598434433286409096558\ldots<T,
$$



leaving at least
$0.5863308921208012836898205681\ldots$ per $6m$.
Even four complete forced digits have ceiling
$1.1396325196868866572818193115\ldots<T$; five are the first layer count
not excluded by this support ceiling.  These are ceilings on the current
certification mechanism, not upper bounds for the actual $c_m$.

**OPEN:** obtain positive linear-scale mass from deeper digits or prove a
sequential matching lower bound after division by the full actual content.
The authoritative manifest is
results/lifted_endpoint_hasse_congruence_slab_and_capacity_hashes.sha256
(SHA-256
a7be9bf216788457bf48c5b29862386bd31750c505621144123d390e09ee0670).
Item 162 does not classify $e+\pi$.

All theorem/evidence boundaries, hashes, and continuation targets are in
`active_checkpoint_20260828.md`.  None of items 139--162 proves that
$e+\pi$ is irrational or transcendental.

## Item 163: all-depth determinant digits and sequential matching audit

Item 163 replaces the first-lift-only description by an exact all-depth
two-minor gate.  Put



$$
D=1+\delta_{m,p},\qquad
 \mathscr A=q_pA_m,\qquad \mathscr B=8B_m,
$$



and expand



$$
{\mathscr A\over p^D}=\sum_{j\ge0}a_jp^j,
 \qquad
 {\mathscr B\over p^D}=\sum_{j\ge0}b_jp^j.
$$



Then, exactly,



$$
v_p(U_m)=1+v_p(\mathscr A/p^D),\qquad
 v_p(V_m)=e_p+1+v_p(\mathscr B/p^D).
$$



Consequently, for every $r\ge2$,



$$
p^r\mid c_m
 \iff
 a_0=\cdots=a_{r-2}=0
 \quad\hbox{and}\quad
 b_0=\cdots=b_{r-e_p-2}=0,
$$



with the second string empty when $r\le e_p+1$.  The digits are produced
without dividing by a Cartier scalar, by an exact determinant
convolution-and-carry tower seeded by the first Bockstein.

**EXPERIMENTAL:** in the exact $e_p=1$, $m\le100$ census, the survival
counts for $p,p^2,p^3,p^4,p^5\mid c_m$ are respectively
$784,58,5,0,0$.  The five $p^3$ rows are
$(36,19),(67,17),(74,19),(89,19),(100,23)$.  These finite counts are not
density statements.

The sequential matching audit proves the exact primewise ledger



$$
v_p(c_m\Delta g)=\kappa_p+
 \min(\beta_p,t_p)+\gamma_p,
$$



where $\kappa_p=v_p(c_m)$, $\beta_p=v_p(V_m)-\kappa_p$,
$t_p=v_p(q_N)$, and $\gamma_p$ can be nonzero only on the positive
equal-valuation diagonal $\beta_p=t_p$.  It follows that
$\Delta g\mid q_N^2$; hence every family with
$N_m\log N_m=o(m)$ has zero matching rate.  A separate distinct-prime
antiperiod stacking theorem also has zero rate under saddle-compatible
shift span.

**PROVED, SCOPED NO-GO:** even granting both $\Delta$ and $g$ a full copy
of the entire known denominator-clearing reservoir and then adding the
proved rank-one content rate gives only



$$
1+r_1=1.1365141682948128184504238226\ldots<T,
$$



leaving $0.0196329836694317938803064012\ldots$ per $6m$.  This rules out
certificates booked only from the rank-one radical and that reservoir; it is
not an upper bound for the actual $c_m\Delta g$.

**OPEN:** prove positive linear-scale deeper-digit mass, or a synchronized
moving-index matching lower bound from sources outside that scoped ceiling.
A dated 2026-08-29 literature recheck found no primary result changing the
open status of $e+\pi$.  The authoritative item-163 manifest is
results/item163_deeper_digits_and_sequential_matching_hashes.sha256
(SHA-256
786ea03268a7e86ef11f7cdcff6a9fb20d07b28ec3bacc69c3493acc364ec2fe).
Item 163 does not classify $e+\pi$.

## Item 164: an infinite third layer and singular matching law

Item 164 proves that the item-162 slab has an infinite third-content-layer
tail.  If



$$
p=20k+19\text{ is prime},\qquad
 m=18k+17+\ell p,
$$





$$
0\le\ell\le5k+3,
 \qquad 6\ell+4\ge p,
$$



then



$$
\boxed{p^3\mid c_m.}
$$



The proof constructs the exact second-Cartier differentials



$$
\Phi_s={u^{4+6\ell}H_s\over Q^{5+4\ell}}\,dx,
 \qquad \deg H_s\le5,
$$



and identifies the next normalized determinant digit with their endpoint
minor.  In the displayed tail, each $\Phi_s$ is a characteristic-$p$
exact differential because its residual polynomial has degree at most
$p-2$.  The subray $\ell=5k+3$ is equivalently



$$
20m=5p^2-17p-2,
$$



so Dirichlet's theorem supplies infinitely many rows.  This refutes a
uniform large-prime third-layer nondivisibility claim.

The theorem is still thin: every selected prime divides $10m+1$, and the
product at fixed $m$ is at most $10m+1$.  Its additional logarithmic
mass is therefore $o(m)$.

**EXPERIMENTAL:** the exact $e_p=1$ census through $m=250$ contains
4,535 forced rows, 196 square-layer candidates, and 14 cubic survivors.
All 14 are rank one and have $p\le31$.  The proved tail has one in-range
row, $(m,p)=(74,19)$, with zero misses.  The next eligible prime is
$p=59$, whose first tail row is $m=643$; hence the absence of
$p\ge37$ survivors through $m=250$ is only a finite observation.

Item 164 also isolates an exact singular sequential-matching mechanism.  On
a dead singular beta root with $v_p(b_m)=v_p(q_N)=1$, the final matching
condition is independent of the lift parameter: either every
parity-compatible lift contributes $p^2\mid\Delta g$, or none does.  Thus
the singular fibre can double a radical while costing only a class modulo
$2p$, rather than $2p^2$.

**PROVED, SCOPED NO-GO:** central singular primes occurring at one index have
product dividing $2N+1$, so their doubled first-level mass is $o(m)$ at
the saddle scale.  More generally, even optimistically doubling every prime
$p\le3m$ gives rate at most one; after adding the proved rank-one rate the
total is again only



$$
1+r_1=1.1365141682948128184504238226\ldots<T.
$$



**OPEN:** the first-level singular escape requires positive logarithmic mass
from synchronized noncentral dead singular primes beyond the support cutoff,
or deeper all-lift powers or another source.  Finite scans find only the
central dead root $(p,r)=(79,39)$ through $p=200000$; that is experimental
and not an all-prime theorem.

The authoritative manifest is
results/item164_third_layer_and_singular_matching_hashes.sha256
(SHA-256
47b388115ff0c7f61dbac00d0cb01792b6f8abcc3973e510c94e37cfacd73a00).
Item 164 does not classify $e+\pi$.

## Item 165: exact noncentral singularity and the moving-resultant barrier

Item 165 gives an exact arithmetic test for every noncentral singular beta
root.  Let $p=2c+1\ge5$, $1\le r<c$, and



$$
h={p-3\over2}-r.
$$



For the odd symmetric plus-continuant



$$
\mathcal K_h(X)=[X-4h,X-4h+4,\ldots,X+4h]
                 =X\mathcal L_h(X^2),
 \qquad D_h=\mathcal K_h'(0),
$$



the first index slope satisfies, whenever $p\mid q_r$,



$$
{q_r-q_{p-1-r}\over p}
 \equiv-2D_hq_{r-1}\pmod p.
$$



Since adjacent beta denominators are coprime, the root is noncentral
singular exactly when



$$
\boxed{p\mid q_r\quad\hbox{and}\quad p\mid D_h.}
$$



The local factor is intrinsic:



$$
\operatorname {Res}_X(X,\mathcal L_h(X^2))=D_h,
$$





$$
\operatorname {Disc}_X(\mathcal K_h)
 =(-1)^h4^hD_h^3\operatorname {Disc}_T(\mathcal L_h)^2.
$$



An exact Lommel sum, alternating cofactor-square formula, and five-lag
recurrence compute $D_h$.  They also give



$$
\log|D_h|=2h\log h+O(h).
$$



**PROVED, SCOPED NO-GO:** at a saddle-compatible index and a prime
$p>3m$, one has $r=N$ and $h=(p-3)/2-N\asymp p$.  Thus the eliminant
$D_h$ changes with $p$ and has height $\Theta(p\log p)$, too large for
the $m$-scale ledger.  The product $R_{m,N}^{>}$ of distinct noncentral
dead singular primes above $3m$ satisfies only



$$
R_{m,N}^{>}\mid q_N.
$$



Closing the residual rate gap would consume merely
$0.0084007101\ldots$ of the available $\log q_N$ budget, so this radical
bound is quantitatively far too weak.  This proves a limitation of the
direct resultant-height argument, not absence of the required primes.

The recurrence and reflection structure alone cannot exclude them: modified
initial data give an exact dead-singular comparison at
$(p,h,N)=(107,2,50)$.  This is explicitly not the Bessel seed $(1,1)$.

**EXPERIMENTAL:** an exact replay finds no noncentral singular root among 146
roots for $p\le2000$, and none among 40 certified large-prime divisors
$p\mid q_N$, $N\le80$, reaching $p=65{,}676{,}881$.  The latter is a
targeted list, not an exhaustive scan of the interval.

The authoritative manifest is
results/item165_noncentral_singular_hashes.sha256
(SHA-256
2b84fe9ebe7f2e5a3520a5b5d5a9a4873fe3ba74f785649aff256e808647e066).
Item 165 does not classify $e+\pi$.

## Item 166: actual-seed left-factorial bridge (2026-08-29)

**PROVED.**  Let $P_0=1,P_1=3$ satisfy the beta-denominator recurrence,
and let $b_0=0,b_1=4$ satisfy



$$
b_n=(4n-2)b_{n-1}+b_{n-2}+4q_{n-1}.
$$



For a prime $p=2r+2h+3$ with $p\mid q_r$, the actual Bessel seed obeys



$$
P_r\bigl(P_r(!p)-b_r\bigr)
 \equiv4(-1)^{r-1}D_h\pmod p,
$$



where $!p=\sum_{j=0}^{p-1}j!\pmod p$.  Consequently the noncentral root
is singular exactly when



$$
\boxed{!p\equiv b_rP_r^{-1}\pmod p.}
$$



This is an exact fixed-seed reduction to a prescribed left-factorial
residue.  It is Kurepa-type, but it is neither Kurepa's zero-residue
conjecture nor a known avoidance or product theorem.  At a saddle index the
available consequence remains only that the dead-singular radical divides
$q_N$, so no new exponential-rate bound follows.

**EXPERIMENTAL:** the deterministic certificate finds no singular case
among 344 roots through $p\le5000$, nor among five certified sparse
factors reaching $p=3{,}092{,}690{,}659$.  A composite tied-index example
at $79\mid q_{39},D_{78}$ shows why primality in the bridge is essential.

The authoritative manifest is
results/item166_actual_singular_hashes.sha256
(SHA-256
e36888428aa5f6ec8ff6477d8c4fc0501c063377c91baf866a2099975a1dfa18).
Item 166 does not classify $e+\pi$.

## Item 167: exact cubic valuation on the square ray (2026-08-29)

**PROVED.**  For every prime $p=20k+19$, at



$$
m={p^2-1\over10}
 \qquad(10m+1=p^2),
$$



the content has the exact valuation



$$
\boxed{v_p(c_m)=3.}
$$



The missing relative-endpoint term vanishes by an exact Hermite-primitive
comparison; its two endpoint section sums cancel under a fixed-point-free
involution.  The next period digit is nonzero, proving both $p^3\mid c_m$
and $p^4\nmid c_m$.

**PROVED, SCOPED NO-GO:** every selected prime still divides $10m+1$.
The family therefore contributes only $O(\log m)$, not positive
linear-scale logarithmic mass.

**EXPERIMENTAL:** 38 primes through $p=1999$ pass the deterministic
certificate, with six small direct Hasse computations agreeing exactly.

The authoritative manifest is results/item167_p2_ray_hashes.sha256
(SHA-256
e4d338df527a709878eea4da5dbe9fa65fc98844597e9e5c6c8dabb36b21fd1a).
Item 167 does not classify $e+\pi$.

## Item 168: complete $e=1$ cells and the automatic-tail barrier (2026-08-29)

**PROVED.**  Every top-layer $e=1$, rank-at-most-two row with nonzero
remainder belongs to one of three explicit floor cells
$\kappa=2a-3b\in\{0,1,2\}$: rank two, rank one, or rank zero.  Their
prime-number-theorem interval masses are



$$
C_0=0.3370475079987658\ldots,
 \quad C_1=0.4820375017701113\ldots,
 \quad C_2\le0.8903637697614535\ldots.
$$



Here $C_2$ is an absolute rank-two ceiling.  Even granting
$p^3\mid c_m$ on the entire combined support gives only



$$
{3(C_0+C_1+C_2)\over6}
 =0.8547243897651653\ldots
 <1.1561471519642446\ldots.
$$



**PROVED, SCOPED NO-GO.**  Any item-164-style second-Cartier proof which
gets exactness only by extracting a fresh $(u/Q)^p$ and imposing residual
degree at most $p-2$ must satisfy



$$
p(p+1)\le6m.
$$



Its accessible primes therefore have only $O(\sqrt m)=o(m)$ logarithmic
weight.  This covers the automatic degree-tail mechanism, not non-scalar
endpoint cancellation.  The rank-one version conditionally gives a cubic
layer; the rank-zero analogue stops at the second layer in the exact
normalized-minor ledger.

**OPEN:** positive weighted mass can still come from the scalar-free lifted
digit equations in any of the three cells.  At least a substantial fourth
or fifth layer, internal primes, or sequential matching gain is still
needed.

The authoritative manifest is results/item168_positive_mass_hashes.sha256
(SHA-256
4d64a5c573ecc91119897d09d9b1de4fcb602120c3753d5770c921e234272559).
Item 168 does not classify $e+\pi$.

## Item 169: the second divided-index law on all-lift beta fibres (2026-08-29)

**PROVED, CONDITIONAL LOCAL THEOREM.**  Let $p\ge7$ and let an actual-seed
root $r$ satisfy



$$
\lambda_p(r)=q_r/p\equiv0,
 \qquad
 \delta_p(r)=(-q_{r+p}-q_r)/p\equiv0\pmod p.
$$



Writing $a_x=(-1)^xq_{r+xp}$, the divided differences define a cubic



$$
P_r(T)=\sum_{j=0}^3{\Delta^ja_0\over p^2}{T\choose j}\pmod p.
$$



For $N=r+tp+up^2$,



$$
p^3\mid q_N\iff P_r(t)=0.
$$



At a root, the next digit is affine in $u$:



$$
{(-1)^{t+u}q_N\over p^3}
 \equiv\kappa_t+uP_r'(t)\pmod p.
$$



This gives the exact ordinary/dead/all-lift trichotomy through $p^4$,
plus matching polynomials at exact common valuations two and three.  A
level-two matched prime contributes $p^3\mid\Delta g$ at generic modulus
cost $p^2$; the valuation-three branch contributes $p^4$ at generic
cost $p^3$.  The product ceilings leave enough formal capacity to fill
the remaining rate gap, so they are not a no-go theorem.

**EXPERIMENTAL:** a deterministic scan through $p\le20{,}000$ finds no
noncentral singular or all-lift actual-seed root.  Its sole singular row is
the central dead case $(p,r,\lambda)=(79,39,12)$, which does not satisfy
the theorem's hypothesis.

**OPEN:** existence of even one noncentral actual-seed all-lift orbit,
positive-mass occurrence in the primitive coefficient, and synchronization
of the resulting moving CRT classes.

The authoritative manifest is
results/item169_deeper_all_lift_hashes.sha256
(SHA-256
06931148ac57dabfeb35b6b200727b728a15b228166dbc2a2a97dd9cda93b3a3).
Item 169 does not classify $e+\pi$.

## Item 170: complete prime-square valuation table (2026-08-29)

**PROVED.**  For every prime on the locus $10m+1=p^2$, the complete
residue-class law is



$$
\begin{array}{c|cccc}
p\bmod20&1&9&11&19\\ \hline
\dim\langle\mathcal C\omega_0,\mathcal C\omega_1\rangle&2&1&1&0\\
v_p(c_m)&1&2&2&3.
\end{array}
$$



The proof reconciles these actual ranks with Item 168's floor cells, closes
the relative endpoint in every class, and gives a nonzero leading period
digit proving each upper valuation.  Hence class $19$ is uniquely cubic
and no fourth layer occurs on this locus.

**PROVED, SCOPED NO-GO.**  At fixed $m$ the equation supplies at most one
prime, so even the cubic class contributes only $O(\log m)=o(m)$.  The
Route-1 exponential constant is unchanged.

**EXPERIMENTAL.**  All 146 admissible primes through $p\le2000$ pass the
symbolic replay, and 20 primes through $p\le200$ pass independent full
Hasse-coordinate checks.  The two JSON runs are byte-identical.

The authoritative manifest is results/item170_square_ray_hashes.sha256
(SHA-256
43084691d5d2c1ceffe7a761d2c61e01763650f82098af1606f7f7d014223395).
Item 170 does not classify $e+\pi$.

## Item 171: all higher prime-power top loci (2026-08-29)

**PROVED.**  For every odd prime $p\ne5$ and every admissible exponent
$a\ge3$,



$$
10m+1=p^a\quad\Longrightarrow\quad p\mid c_m.
$$



After $a-1$ Cartier iterations the two rows have universal sparse
polynomials



$$
P_0=x^\rho(1-x^4)^\rho,\qquad
P_1=x^\rho(1-x)(1-x^4)^{\rho-1}.
$$



An explicit Lucas carry argument classifies their rank for every exponent.
The sole rank-two class $p\equiv1\pmod {20}$ is closed by a proper-
primitive endpoint identity; the lower-rank classes follow from the frozen
normalization.  Classes $7,17,19\pmod {20}$, together with
$p=3,a\ge8$, have the stronger lower bound $v_p(c_m)\ge2$.

**PROVED, SCOPED NO-GO.**  At fixed $m$ the locus has at most one base
prime.  Its radical and all $a-1$ top-exponent copies therefore weigh only
$O(\log m)=o(m)$, so the Route-1 constant is unchanged.

**DISPROVED / EXPERIMENTAL FINITE.**  Exact rows such as
$(p,a,v_p(c_m))=(11,3,1),(3,4,3),(7,4,5)$ disprove the universal guess
$v_p(c_m)=a+1$.  Eight full-coordinate rows are diagnostics only.

The authoritative manifest is
results/item171_prime_power_loci_hashes.sha256
(SHA-256
34f537abd6bc05e10634bad88d52009a04f7f9ef66423b00df12c497605166e4).
Item 171 does not classify $e+\pi$.

## Item 172: scalar-free rank-one cubic gates (2026-08-29)

**PROVED.**  On the positive-mass $e=1,\kappa=1$ cell, exact coordinate
convolutions and carries give



$$
p^3\mid c_m
 \iff A_0=A_1=B_0=0
$$



without dividing by a Cartier scalar.  The first Bockstein expresses
$A_0,B_0$ as two five-divisor Frobenius-semilinear forms in the values of
one reduced primitive at $0,1,-1,i,-i$.  The next digit $A_1$ still
requires the genuine modulo-$p^3$ Hasse lift.

**PROVED — scalar data are insufficient.**  The exact rows
$(m,p,j,s)=(99,107,1,15)$ and $(206,107,3,15)$ have the same
$(p,s)$, the same exact Cartier coefficients, and the same reduced pair
$(2,75)$, but $A_0=0$ and $65$, respectively.

**PROVED, SCOPED NO-GO.**  If, band by fixed band $j$, a proposed zero
family is contained in finitely many fixed nonzero polynomial congruences
in $s$, then its total log-prime weight is $o(m)$.  Fixed affine rays
are included.  This theorem does not place the actual high-degree moving
Hasse/Bockstein zero set in that class.

**EXPERIMENTAL.**  Through $m\le250$, 104 of 119 $A_0$-zeros are
genuinely non-scalar and eight of ten cubic gates are non-scalar.  These
counts are finite-only.

The authoritative manifest is
results/item172_rankone_nonscalar_hashes.sha256
(SHA-256
2ba8bcc7bd15832b2615509ac68c146a4b143d3aba2d6001cde51b8eb9019d2c).
Item 172 does not classify $e+\pi$.

## Item 173: rank-zero missing digit and extended tail (2026-08-29)

**PROVED.**  On the regular $e=1,\kappa=2$ cell, the first Cartier
images vanish separately and the normalized minors have exact scalar-free
determinant carries.  In particular the formerly opaque digit is



$$
A_1\equiv S_1+{S_0-A_0\over p}\pmod p.
$$



The automatic second-Cartier mechanism extends from $3j\ge p$ to the
sharp boundary



$$
3j+1\ge p,\qquad 2j+2\le p.
$$



At $3j+1=p$, the identity
$H_s(1)=-4(3j+1)T_s(1)$ supplies an extra factor of $u$ modulo $p$,
leaving residual degree at most $p-2$.  Hence $A_0=B_0=0$ and
$p^2\mid c_m$ throughout the enlarged tail.

**PROVED, SCOPED NO-GO.**  The same conditions imply $p^2\le6m$, so the
whole mechanism has only $O(\sqrt m)=o(m)$ prime weight.  Exact rows
inside it realize both $A_1\ne0$ and $A_1=0$; the tail hypotheses force
neither cubic failure nor cubic survival.

**EXPERIMENTAL.**  Through $p\le43$, all 84 tail rows have
$A_0=B_0=0$, while five have $A_1=0$ and 79 do not.  These are finite
diagnostics only.

The authoritative manifest is
results/item173_rankzero_nonscalar_hashes.sha256
(SHA-256
83aac60f69a4e40d52de23b08364e7e2b6ae07f0d3fa8719041bb69d7f64d7e2).
Item 173 does not classify $e+\pi$.

## Item 174: rank-two determinant reduction and scalar-free lifts (2026-08-29)

**PROVED.**  On the regular $e=1,\kappa=0$ cell the exact first-Cartier
determinant $\Delta_{p,s}$ is the entry gate.  Once it vanishes, exact
coordinate carries give



$$
p^2\mid c_m\iff A_0=0,
\qquad
p^3\mid c_m\iff A_0=A_1=B_0=0.
$$



First-order proportionality alone does not determine any of these lift
digits; this is proved as an ambient statement and is not asserted to
realize arbitrary lifts in the actual coefficient family.

**PROVED — fixed-band reduction.**  For fixed $s$, residue class
$\rho=p\bmod4$, and $p\ge8s+3$,



$$
\Delta_{p,s}\equiv C_{s,\rho}\pmod p
$$



for an explicit rational constant.  Exact modular certification proves
$C_{s,1}C_{s,3}\ne0$ for $0\le s\le256$.  Determinant-zero primes in
any strip $s\le S(m)=o(m/\log m)$, or on finitely many affine rays, have
only $o(m)$ log-prime weight.

**EXPERIMENTAL.**  Through $m\le500$, 295 of 18,147 rows vanish, giving
127 distinct $(p,s)$ pairs.  In the lifted census through $m\le100$,
46 rows supply the first content layer, eight the second, and none a third.
These counts do not establish a density.

**OPEN.**  The moving linear-scale determinant-zero locus, positive-mass
solutions of $A_0=A_1=B_0=0$, and any improved Route-1 exponent remain
unproved.

The authoritative manifest is
results/item174_ranktwo_nonscalar_hashes.sha256
(SHA-256
c33d20f2844c0163e9eda86c5a94c4437119fe29cf2ea11c395fef62b18e5aa4).
Item 174 does not classify $e+\pi$.

## Item 175: no fixed-band collapse of the circular gate (2026-08-29)

**PROVED.**  On the rank-one $\kappa=1$ cell, let


$$
F_j={u^{3j+2}\over Q^{2j+2}},\qquad j\ge1.
$$


The exact residue-coordinate weight of the $a=1$ divisor satisfies


$$
w^B_{j,1}\ne0
$$


for every $j$.  Thus, outside a finite $j$-dependent set of primes,
the five-divisor formula for $B_0$ is a genuinely nonzero formal linear
constraint.  There is no fixed-band structural degeneration of this
circular functional.

**PROVED — scalar convention.**  The Bockstein primitive must be formed
using the exact integer Cartier coefficients before reducing modulo $p$.
Arbitrary congruent lifts introduce an $x^p$ correction; omitting it can
change the displayed gate.

**EXPERIMENTAL.**  All $A/B$ weights at all five divisors are nonzero
through $j=12$, and the $a=0,1$ weights are nonzero through $j=24$.
Only the all-$j$ statement for $w^B_{j,1}$ is proved.

**OPEN.**  The actual values $\bar T(a)$ are constrained and moving.
The theorem proves formal nonidentity, not nonvanishing or thinness on
that actual locus, and it gives no new Route-1 exponent.

The authoritative manifest is
results/item175_fixed_band_hashes.sha256
(SHA-256
433f859f58d0676ac88893c1d00999c99c3438183afb1479a2d3da3fe22111b7).
Item 175 does not classify $e+\pi$.

## Item 176: native common-polynomial reciprocal Padé ray (2026-08-29)

Put


$$
F(z)=4\arctan {z\over2-z},\qquad S(z)=e^z+F(z),\qquad S(1)=e+\pi.
$$


Let $Q_n$ be the degree-$n$ Taylor truncation of $1/S$.  Then


$$
R_n(z)=-1+Q_n(z)e^z+Q_n(z)F(z)=O(z^{n+1})
$$


is the unique common-polynomial ray with maximal cancellation.

**PROVED — no decay.**  Exact Rouché bounds show that $S$ has one simple
zero $r\in(-1/2,-2/5)$ in $|z|<3/5$.  Darboux asymptotics therefore give


$$
|R_n(1)|\asymp |r|^{-n}\longrightarrow\infty.
$$


After exact denominator clearing and complete endpoint gcd reduction, the
primitive integer form


$$
L_n={W_n\over g_n}(e+\pi)-{n!\over g_n}
$$


still diverges and satisfies $|L_n|/H_n\to e+\pi$.  Thus gcd cancellation
cannot rescue this ray.

**OPEN.**  The theorem covers $B_n=C_n=Q_n$ as polynomials.  It does not
cover genuinely independent $B_n,C_n$, even if $B_n(1)=C_n(1)$.

The authoritative manifest is
results/item176_route2_native_reciprocal_hashes.sha256
(SHA-256
d4278012ff8984bf625d909c6e96c4ce44300214ce850d75292d1228dcb21710).
Item 176 does not classify $e+\pi$.

## Item 177: actual constrained $B_0$ on two fixed bands (2026-08-29)

**PROVED.**  On the actual rank-one slice $(j,s)=(1,1)$, $m=p-1$,


$$
B_0\equiv
\begin{cases}
2735/4,&p\equiv1\pmod4,\\
-5295/4,&p\equiv3\pmod4,
\end{cases}
\pmod p,
$$


and $B_0\ne0$ for every prime $p\ge7$.  On
$(j,s)=(2,0)$, $m=(3p-1)/2$,


$$
B_0\equiv
\begin{cases}
-918897/128,&p\equiv1\pmod4,\\
59829/128,&p\equiv3\pmod4,
\end{cases}
\pmod p,
$$


whose only zeros are $p=7,11$; hence $B_0\ne0$ for $p\ge13$.
These are symbolic all-prime formulas on the constrained primitive locus,
not finite interpolation.

**PROVED — integrated sign correction.**  Under the archive circular
coordinate convention, the five-divisor $B_0$ contraction has the unit
factor $\chi_4(p)=(-1)^{(p-1)/2}$.  Items 172 (4.11) and 175 (4.1)/(4.3)
now include it.  It negates old signed contractions for
$p\equiv3\pmod4$, but changes no zero statement, finite count, survivor,
or direct-Hasse digit.

**SCOPED NO-GO.**  Both slices are fixed rays and have zero log-prime rate,
so their cubic exclusion does not improve the Route-1 exponent.

The authoritative manifest is
results/item177_actual_fixed_band_hashes.sha256
(SHA-256
ba275161b2954148ab716e82e73689eea55c4bc2cd39d940b50da09cec24fcb8).
Item 177 does not classify $e+\pi$.

## Item 178: all minimal-parity fixed bands (2026-08-29)

On the rank-one cell take


$$
\epsilon_j=j\pmod2,\qquad s=\epsilon_j,\qquad
m={(j+1)p-\epsilon_j-1\over2}.
$$



**PROVED — all-band actual nonidentity.**  For every $j\ge1$ and both
$\rho=p\bmod4$, the actual constrained $B_0$ value is the reduction
of a nonzero rational constant $C_{j,\rho}$.  An exact Cayley obstruction
has the uniform sign


$$
\operatorname {sgn}\Omega^\#_{j,\rho}=(-1)^j.
$$


The last sign case follows from


$$
(2+4t+3t^2+t^3)^L
=\sum_{r=0}^L\binom Lr(1+t)^{L+2r}
$$


and a strict adjacent central-binomial inequality.  Consequently
$B_0\ne0$ for every sufficiently large admissible prime in every fixed
minimal-parity band.

**PROVED — zero-rate scope.**  At fixed $m$, the even-$j$ primes divide
$2m+1$ and the odd-$j$ primes divide $2m+2$.  The union over all bands
therefore has at most


$$
\log((2m+1)(2m+2))=O(\log m)
$$


log-prime weight.

The authoritative manifest is
results/item178_minimal_parity_hashes.sha256
(SHA-256
7473dd09c8ac514522045ad8f94d2e0f2191c0ddec819d93862d6e6435abd2ea).
Item 178 does not classify $e+\pi$.

## Item 179: independent diagonal forms and the endpoint tax (2026-08-29)

Let $A,B,C\in\mathbb Q[z]$ have degree at most $n$, and put


$$
F(z)=4\arctan {z\over2-z}.
$$



**PROVED — all-degree compatibility identity.**  The maximally cancelling
independent family


$$
A+Be^z+CF=O(z^{3n+2})
$$


has $B(1)=C(1)$ exactly when one explicit square determinant
$\det K_n$ vanishes.  Equivalently, the endpoint-matched family of
generic order $3n+1$ then gains one additional Taylor zero.  This
equivalence holds in every degree.

**PROVED COMPUTATION.**  Exact arithmetic modulo the proved prime $65521$
shows for every $1\le n\le256$ that $\det K_n\ne0$: the maximal family
is unique but not endpoint-matched, while the endpoint-matched family is
unique and loses exactly one cancellation order.  Independent rational
reconstruction through $n=30$ agrees projectively.

After full polynomial content and endpoint gcd reduction, every
nondegenerate endpoint-matched form for $2\le n\le30$ has certified
$|L_n|>1$; the $n=30$ value lies in decade $10^{1421}$.
This finite growth is not extrapolated.

**OPEN.**  All-degree nonvanishing of $\det K_n$, endpoint-gcd
asymptotics, and unequal-degree or multipoint families remain unresolved.

The authoritative manifest is
results/item179_independent_diagonal_hashes.sha256
(SHA-256
bb52e1bd256eeca881be05d32b2697b507a2afaa3d790a9ef6d021c587fb3763).
Item 179 does not classify $e+\pi$.

## Item 180: moving $\kappa=0$ determinant and residual roots (2026-08-29)

**PROVED — exact moving determinant law.**  Put


$$
A_s(x)={(1-x)^{5s+2}\over(1-x^4)^{2s+2}}
      =\sum_{n\ge0}a_nx^n,
\qquad d=p-3s.
$$


The rank-two determinant on the moving $\kappa=0$ cell is


$$
(-1)^s\bigl[(a_{d-2}+a_{d-3}+a_{d-4})a_{p-5}
 -(a_{p-4}+a_{p-3}+a_{p-2})a_{d-1}\bigr]\pmod p.
$$


A four-term coefficient recurrence gives an exact $O(p)$ finite-field
test for every pair $(p,s)$.

**PROVED — positivity is not an arithmetic escape.**  In the sector
$p\ge5s+2$, the determinant has a nonnegative-coefficient integer lift
with exponential real size.  Nevertheless four explicit off-ray pairs,
including $(p,s)=(337,52)$, have a nonzero lifted integer determinant
divisible by $p$, while the associated content witness has exactly
$v_p(E)=1$.  Thus real positivity or size alone cannot rule out the
moving modular roots.

**PROVED CONDITIONAL TRANSFERENCE.**  If the number $r_p$ of residual
roots satisfies $r_p=o(p)$, their mean log-prime mass is $o(m)$.
Proving that root-count hypothesis remains open.  The exact census through
$p\le1000$ finds 169 roots among 25,454 admissible pairs, with at most
four roots for any one prime; this is finite evidence only.

The authoritative manifest is
results/item180_moving_residual_hashes.sha256
(SHA-256
5a7bb46b73de560e8896b673411947cc5df77f9272de58139ac93739468e2689).
Item 180 does not classify $e+\pi$.

## Item 181: all next-parity fixed bands (2026-08-29)

On the rank-one cell let


$$
\epsilon_j=j\pmod2,\qquad s=\epsilon_j+2.
$$



**PROVED — all-band actual nonidentity.**  For every $j\ge1$ and both
prime residue classes, the actual constrained $B_0$ value is the
reduction of a nonzero rational constant.  The exact obstruction has
uniform sign


$$
\operatorname {sgn}\Omega^{(2),\#}_{j,\rho}=(-1)^{j+1}.
$$


Consequently $B_0\ne0$ for every sufficiently large admissible prime
in every next-parity fixed band.

**PROVED — zero-rate scope.**  At fixed $m$, the relevant primes divide
$(2m+3)(2m+4)$, so their total log-prime weight is $O(\log m)$.
The theorem extends actual constrained nonvanishing but does not supply
positive linear-scale prime mass.

The authoritative manifest is
results/item181_next_layer_hashes.sha256
(SHA-256
1cbf15dc8e65068e09643c48bc6d8ef487f9ae846c632fe1e5e314ef7bd770ef).
Item 181 does not classify $e+\pi$.

## Item 182: endpoint tails and the gcd bottleneck (2026-08-29)

**PROVED — exact all-degree endpoint tail.**  For the endpoint-matched
diagonal family of Item 179, the value at one is exactly a sum of
exponential tails and two conjugate logarithmic tails.  If
$H_{BC}$ is the coefficient height, then


$$
|R_n(1)|\le H_{BC}(n+1)\left{
{2n+2\over(2n+1)(2n+1)!}+{12\over(2n+1)2^n}
\right}.
$$


After full-content and endpoint-gcd reduction this is still multiplied by
the uncontrolled effective height $H_{BC}/d$; the gcd cancels from the
relative ratio.

**PROVED COMPUTATION.**  Exact rational reconstruction and rigorous
intervals through $n=45$ give $|L_n|>1$ in every nondegenerate degree
$2\le n\le45$.  At $n=45$, the primitive height has 3581 digits and
the value lies in decade $10^{3529}$.  This finite nondecay is not
extrapolated.

The authoritative manifest is
results/item182_endpoint_asymptotic_hashes.sha256
(SHA-256
c33197afe0e00d10be4e3d6a4ee11205d14b2036103d07be3e932d919a961e2c).
Item 182 does not classify $e+\pi$.

## Item 184: reverse-polynomial tails and projective height (2026-08-29)

**PROVED — sharper all-degree bound.**  An exact reverse-polynomial
integral removes the factor $n+1$ from the logarithmic-tail estimate.  For
$q=2n+1$,


$$
|R_n(1)|\le H_{BC}\left{
{(q+1)^2\over q^2q!}+{16+12\sqrt2\over q2^n}
\right}.
$$


Its rational majorant obtained by replacing $16+12\sqrt2$ with 33 is
strictly sharper than the Item 182 bound for every $n\ge2$.

**PROVED — normalization obstruction.**  Full-content reduction,
endpoint-gcd reduction, and common rescaling leave both $H_{BC}/d$ and
$H_{BC}/H_{\rm end}$ unchanged.  Thus normalization cannot repair the
coefficient-to-endpoint height loss; the projective kernel direction must
be controlled.  On the exact rays, $H_{BC}/H_{\rm end}\ge4^n$ for
$7\le n\le30$, so even the sharper generic bound remains above one in
that finite range.

The authoritative manifest is
results/item184_endpoint_height_hashes.sha256
(SHA-256
4da022fb579a75a065d79bb798ea5d7a6183ddf3c03582f443236b89565b764c).
Item 184 does not classify $e+\pi$.

## Item 185: moving roots, fixed rational maps, and a sign theorem (2026-08-29)

**PROVED — structural reformulation.**  The moving determinant is a
two-by-two coefficient determinant built from powers of the fixed rational
maps


$$
H={(1-x)^5\over(1-x^4)^2},\qquad K=x^3H.
$$


Its moving-parameter generating functions are exact coefficient
extractions of $A_0/(1-yH)$ and $A_0/(1-yK)$, and every entry also has
a terminating binomial formula.

**PROVED — complete real-sign theorem in the positive-lift sector.**  Put
$b=p-5s-2$.  The lifted integer determinant satisfies $E_{p,s}<0$
for $b\ge1$.  At $b=0$, it vanishes exactly when
$s\equiv1\pmod4$, and is positive when $s\equiv3\pmod4$.  This does
not prevent a nonzero integer from vanishing modulo $p$.

**FINITE ONLY / OPEN.**  Exact tests show that structural-factor,
factorial/gamma, and endpoint-pivot normalizations retain growing
interpolation complexity.  The census through $p\le2000$ finds 322 roots
among 92,496 pairs, with maximum five at $p=1471$.  The central lemma
$r_p=o(p)$ remains unproved.

The authoritative manifest is
results/item185_moving_root_count_hashes.sha256
(SHA-256
cc069e5ba0530ab9f708ac67b0b94fd57f00fb2816d9a4352014c9d49d36edfe).
Item 185 does not classify $e+\pi$.

## Route-priority correction and Items 189, 191--193 (2026-08-30)

Route 1 remains active.  It has not succeeded, but no route-wide theorem
proves it impossible.  The exploratory Route-2 packages are retained as
checkpoints only and are not being used to bypass the required route order.

**Item 189 — moving-root collision frontier.**  If every positive difference
between roots of the moving rank-two determinant has multiplicity at most
$B$, then $r_p=O(\sqrt p)$; a short-shift bound $C_p(h)=O(h)$ would
already give $r_p=O(p^{2/3})$.  The complete exact scan through
$p\le5000$ is Sidon, but no uniform collision theorem is proved.  The
manifest is results/item189_collision_route_hashes.sha256 (SHA-256
ce9134b4aa61be7f5f60292b28f54877f5d08c441721099fd387904043dacbdd).

**Item 191 — actual moving lift gates.**  Conditional on a determinant-zero
entry, the regular tail


$$
3j-1\ge p,\qquad2j+2\le p
$$


has $A_0=B_0=0$, hence $p^2\mid c_m$, including zero-row cases.
The same inequalities force $p(p+1)\le6m$, so this automatic family has
zero exponential rate; $A_1$ is not forced.  The manifest is
results/item191_moving_gate_hashes.sha256 (SHA-256
4fbaeeca285422536295624a058a4857b7c446acba564b5fb283e4500c91d0da).

**Item 192 — beta-seed rigidity.**  First-Witt seed lifts preserve
$I=\delta+2\lambda$, so a dead singular actual fibre cannot be converted
into an all-lift fibre.  The higher tunable branch has degree $p-1$ and
does not preserve the fixed-degree Newton architecture.  This rules out
local seed engineering, not useful primes of the actual seed.  The manifest
is results/item192_beta_frobenius_seed_hashes.sha256 (SHA-256
45f73e25ed308f47bca1115e81c768543bb19b4e9ad9c4a25bf4a480efa37a09).

**Item 193 — paired actual-seed invariant.**  For reflected roots,


$$
I_r=3\lambda_r-\lambda_s,\qquad I_s=3\lambda_s-\lambda_r.
$$


Both vanish exactly when the actual pair is already all-lift.  A one-sided
zero is possible, so the shifted left-factorial criterion obtained here is
an exact reduction rather than an avoidance or density theorem.  The
manifest is results/item193_actual_seed_invariant_hashes.sha256 (SHA-256
198669dca9e4e42cd1702b01c1cc0b466d773ee437b8cfa534429733feaa46f5).

All four packages have byte-identical canonical/replay outputs and validated
dependency manifests.  None proves the required positive Route-1 mass or
changes the open status of $e+\pi$.

## Items 194--195: remaining PNT gates and two-point moments (2026-08-30)

**Item 194 — rank-zero coupled-gate exclusion.**  On every PNT-side
$\kappa=2$ row,


$$
A_0=B_0=0
\iff \ell_{0,0}=\ell_{1,0}=0,
$$


and hence $p^3\mid c_m$ exactly when the two leading logarithmic
coordinates and the carry-corrected $A_1$ all vanish.  A uniform
polynomial elimination rules out every nonzero-log proportionality branch.
The common-log locus still has no proved mass bound.  The manifest is
results/item194_rankzero_pnt_hashes.sha256 (SHA-256
c17d194cd9de1e985cb8c3056a7db1d5059f4aeed72d0ebea5e409541e1c0faf).

**Item 195 — exact two-point moment representation.**  Four Hasse jets
express the moving determinant through a fixed rational map and bounded
six-puncture Kummer sums.  After removing the forced interpolation tail,
the collision problem reduces exactly to the common roots of
$G_p(S)$ and $G_p(S+h)$.  A bounded-conductor Jacobi family with a
linear interval of modular zeros proves that conductor bounds and complex
square-root cancellation alone cannot supply the desired root count.
Determinant-specific $p$-adic noncancellation remains open.  The manifest
is results/item195_twopoint_moment_hashes.sha256 (SHA-256
cae69f328f9b13512efb3d35d0550b6b8f3746b9c8c020317ca8e8d6c334a769).

Both packages were independently replayed in the archived layout.  They
narrow Route 1 but do not complete it or prove it impossible.

## Item 196: all-moving rank-one gate map (2026-08-30)

The positive-mass $\kappa=1$ cell now has a prime-independent rational
primitive for every moving residual coordinate $s$, together with exact
separated formulas for the first gates $A_0$ and $B_0$.  Its numerator
has degree $6s+2$, and its denominators are automatically units at every
admissible cell prime.

The package also isolates a genuine obstruction to the former sign
strategy: at the exact row $(m,p,j,s)=(11,13,1,3)$, the rational
$B_0$-contraction is nonzero but its numerator is divisible by $13$.
Consequently an all-moving rational sign theorem alone cannot yield a
uniform modular zero bound.  The first-gate zero count and the separate
second-lift digit $A_1$ remain open.  The manifest is
results/item196_rankone_moving_gate_hashes.sha256 (SHA-256
26b324f0f16a68b40e46e6fff66cb4331a6e703022611473e4cfc9c8a365e2d1).

The canonical and replay certificates are byte-identical and were checked
again in the archived layout.  Item 196 changes neither the Route-1 ledger
nor the open status of $e+\pi$.

## Item 197: exact common-log integer locus (2026-08-30)

Item 197 converts the exceptional rank-zero common-log condition exactly
into simultaneous square divisibility of two fixed integer coefficients:


$$
\ell_{0,0}=\ell_{1,0}=0
\iff p^2\mid C_0(m),C_1(m).
$$


The exceptional radical therefore satisfies
$R_m^2\mid\gcd(C_0(m),C_1(m))$.  The gcd is the first Smith divisor of the
existing log row, not a new independent reservoir, and its direct height
bound is weaker than the raw support ceiling.  No sublinear or
positive-mass theorem follows.  The manifest is
results/item197_common_log_locus_hashes.sha256 (SHA-256
5e340b9f3233b28385a95eb8254ba67ca0e2cc0c7ea587011c6b44cea83414e7).

The certificate was made host-path independent, replayed with the bundled
runtime, and replayed again from the archived layout with byte-identical
output.  Its zero counts are finite evidence only.

## Items 198--199: actual all-lift pairs and matching reuse (2026-08-30)

**Item 198 — exact actual-pair valuation criterion.**  For a reflected
noncentral beta pair, the common valuation is carried exactly by the
symmetric transfer continuant.  Paired $p^2$-divisibility occurs exactly
when $p^2\mid q_r$ and $p\mid D_h$; the analogous $p^3$ criterion is
also exact.  The prescribed-index radical ceiling $R_N^2\mid q_N$ has no
known positive lower mass, and a non-actual-seed countermodel proves that
the standard transfer/Wronskian data cannot sharpen it alone.  The manifest
is results/item198_actual_all_lift_pair_hashes.sha256 (SHA-256
69e68538bb03b44bd27e2f57325311f52a879a1a5202dc7d257728d5036fe4d8).

**Item 199 — recycled matching barrier.**  Any common exact sequential
factor at beta indices $N,N+h$ divides their transfer continuant
$C_h(N)$.  Hence every $h=o(N)$ has zero common rate at the frozen
saddle, and three consecutive parity-compatible indices have common gcd
exactly one.  Comparable gaps, one-index matching, and disjoint supports
remain open.  The manifest is results/item199_matching_gain_hashes.sha256
(SHA-256
a0ac355f5ecb9de7794366169c40a8b43cd3bdb344a423cb24a1a9448951d281).

Both packages were replayed with the bundled runtime and again from the
archived layout; canonical and replay outputs are byte-identical.

## Item 200: forced Cartier layer and normalized common-log target (2026-08-30)

The raw Item-197 coefficients share the entire already-known Cartier
product $F_m=G_m$.  Its interval subproduct
$\prod_{4m+1<p\le6m}p$ has logarithm $2m+o(m)$, and along powers of
two the coefficient pair is nonzero; therefore no subexponential theorem
for the raw gcd or its radical is possible.  The correct open target is


$$
R_m\mid\gcd(C_0/F_m,C_1/F_m).
$$



Every relevant PNT row overlaps Item 149's booked prime set.  The exact
coefficient recurrence has a rank-three local matrix with kernel
$(0,2,2,1)$ modulo $p^2$, so the two-row local-resultant strategy
cannot exclude normalized common zeros.  Global transfer or Frobenius
control remains open.  The corrected cell mass is
$0.33704750799\ldots$ per $m$, or $0.05617458467\ldots$ per $6m$.
The manifest is results/item200_common_log_gcd_hashes.sha256 (SHA-256
9d6e37e4ed1ba429eae81ac54431a8758f4df5648b1f9f75b2d7c596173a5d5c).

Canonical, replay, and archived-layout outputs are byte-identical.

## Item 202: canonical actual-seed Euler filter (2026-08-30)

The actual normalization defines a unique residue
$P_NT_N\equiv b_N\pmod {q_N}$.  At a prescribed lower root
$p=2N+2h+3$, the transfer derivative satisfies


$$
4(-1)^{N-1}D_h\equiv P_N^2(L_p-T_N)\pmod p.
$$


Consequently paired all-lift is exactly the conjunction
$p^2\mid q_N$ and $L_p\equiv T_N\pmod p$.  The first lifted quotient
depends on $(L_p-T_N)/p\pmod p$, and the two-digit Euler identity
$\mathcal E_p\equiv(1-p)L_p\pmod {p^2}$ introduces no Wilson/Fermat
quotient at this precision.

This is a genuine actual-seed filter, but no existence, density, or product
bound is proved.  A formal local-data countermodel is explicitly not an
actual left-factorial or recurrence example.  The finite scan through
$p\le20000$ finds no lower square or all-lift row and is recorded only as
FINITE evidence.  The manifest is
results/item202_actual_squarefull_filter_hashes.sha256 (SHA-256
f4dd46852de8cb18f498522f659ff718be00c80e261e3521f7880441c4a9579c).

The bundled and archived-layout replays match the canonical output exactly.

## Item 201: sharp comparable-gap transfer and packing boundary (2026-08-30)

The exact transfer continuant is asymptotic, uniformly for $h\le AN$, to


$$
4^{h-1}\frac{\Gamma(N+h+\tfrac12)}{\Gamma(N+\tfrac32)}.
$$


At $h/N\to\alpha$, its frozen-saddle rate is exactly $\theta\alpha$.
A single reused block therefore lacks capacity below
$G/\theta=0.01680142035\ldots$.  At every gap it is also strictly
smaller than the beta-denominator cost of moving the endpoint, so a pure
two-index or one-parent-forest recycling ledger has at most zero net
linear rate and an exact polynomial loss.

Three-transfer continuants satisfy a common-gcd/lcm law, and globally
triple-free reuse never exceeds the unique CRT modulus.  But local
three-index coprimality does not control multi-parent pair-specific packing;
that branch remains open.  The manifest is
results/item201_comparable_gap_hashes.sha256 (SHA-256
81f2fcc58251e66a80e563a716bdaa61dd81affb280a93ed6df07e14fb85ce98).
Canonical, bundled, and archived-layout replays are byte-identical.

## Items 203--204: global common-log transfer and squarefull discriminant (2026-08-30)

**Item 203 — cancellation-aware common-log transfer.**  The five target
coefficients vanish modulo $p$; after division by $p$, an exact
Frobenius defect supplies their unique global values despite singular
recurrence steps.  Common-log is precisely a fixed-line condition on this
five-vector.  The direct defect still has moving degree at least $2p-1$
and truncated-log data, so no zero-count theorem follows.  The manifest is
results/item203_common_log_global_hashes.sha256 (SHA-256
42b89332e456e0073e8f92bcdb512e8cb7a83fea903ab3d20c74cee5fa6db317).

**Item 204 — reverse-Bessel discriminant boundary.**  The actual denominator
is $A_N(-1)$ for a monic reverse-Bessel polynomial with an explicit
derivative, adjacent resultant, and discriminant.  Every target-range root
is simple, but $p^2\mid q_N$ is exactly the independent zero condition on
its Hensel digit $-2(q_N/p)q_{N-1}^{-1}$.  A target-range witness also
shows that multiplicity for the natural coefficient-shift polynomial is
not sufficient.  The manifest is
results/item204_squarefull_discriminant_hashes.sha256 (SHA-256
bae25031b654585747f0ca75d2d6e184934998c2d1dcaff773325c22635b0a5a).

Both packages passed bundled and archived-layout replay.  Neither supplies
new Route-1 mass or a route-wide no-go.

Route-order checkpoint: Route 1 remains ACTIVE because it has neither
succeeded nor been proved impossible; Route 2 remains QUEUED.

## Items 205--209: rank-one content, universal kernel, and separate lifts (2026-08-31)

**Item 205 — localized moving content.**  With the canonical integral moving
vector $(X_s,Y_s,Z_s)$, every odd admissible prime $p>3s+2$ satisfies


$$
v_p\gcd(X_s,Y_s,Z_s)=\min\{v_p(g_0(s)),v_p(g_1(s))\}.
$$


The structural ray $s\equiv3\pmod4$, $p=5s+4$ gives common first-gate
content, but all its row primes divide $10m+1$, so its total log weight is
$O(\log m)$.  Height and the singular local transfer do not bound the
remaining moving zeros.  Manifest: `results/item205_rankone_numerator_hashes.sha256`
(SHA-256 `c60be0b169843a14dcf088d987a329a6473e32d5a792f73665fbcf08ad7c199d`).

**Item 206 — universal projective kernel.**  For every $j$, the two exact
first-gate weight rows annihilate $(2,-1,-1)$; all proposed cross-$j$
three-row eliminants therefore vanish identically.  On every rank-two row,


$$
A_0=B_0=0\iff p\mid g_0(s),g_1(s).
$$


The automatic rank-zero interval $2j+3\le p\le3j+2$ satisfies
$p^2\le6m$ and has zero rate.  Genuine rank-one primes above that interval
exist and remain open.  Manifest: `results/item206_moving_prime_collision_hashes.sha256`
(SHA-256 `783a62ee29a362e390445ae0b196aa286078478fe575f3d4b14fa741171ca6b2`).

**Item 207 — Hensel/Euler coordinates.**  At a prescribed beta root, the
Hensel digit and continuant/Euler coordinate are related to the two actual
first-Witt coordinates by an invertible diagonal map of determinant
$-P_N^3/4$.  Hence combining the two filters does not create a third
relation or a new valuation copy.  The actual row $(p,N,h)=(7,2,0)$
shows that the known scalar invariant can vanish by nonzero cancellation.
Manifest: `results/item207_coupled_hensel_euler_hashes.sha256`
(SHA-256 `a9263ea56ef80a13d2233ae841f71c7c734b16956c1cc676731560a66f746b14`).

**Item 208 — first off-ray common-content prime.**  The conjecture that every
large common-content prime lies on $p=5s+4$ is refuted by


$$
(s,k,p)=(299,899,2399),\qquad p=8s+7,
$$


where both actual resonant integers vanish.  The universal Frobenius-phase
reduction is exact, and any fixed finite union of affine rays would have only
$O(\log m)$ row weight; however, no finite-union classification is proved.
The exhaustive residual audit through $s=1500$ and the targeted
$p=8s+7$ scan through $s=5000$ are finite evidence only.  Manifest:
`results/item208_rankone_content_classification_hashes.sha256`
(SHA-256 `de273ec2361c79c0a2891edaef830457b57a17d1cf311acf7961dc37339f2cd7`).

**Item 209 — the separate second-lift digit.**  After the rank-one division
and the additional condition $A_0=0$, the next digit is exactly


$$
A_1\equiv\frac{L_1X_0-L_0X_1}{p^2}\pmod p.
$$


Actual common-content controls have $A_1=16$ at $(s,p,j)=(3,19,1)$,
$A_1=925$ at $(299,1499,1)$, and $A_1=404$ at
$(299,2399,1)$; at the same $(s,p)=(3,19)$, $j=3$ instead has
$A_1=0$.  Thus first-gate content does not determine the second lift.
The automatic rank-zero interval remains rate-zero regardless of $A_1$.
Manifest: `results/item209_second_lift_digit_hashes.sha256`
(SHA-256 `f2318068e9721274699af36189c036cd87c938de4cf286030bb164a17ae41b6b`).

All five packages passed independent canonical, replay, manifest, and
archive-layout checks.  They add no positive Route-1 exponent.  Route 1
remains ACTIVE; Route 2 remains QUEUED.

## Items 210--212: rank-one ceiling, structural lift, and off-ray phases (2026-08-31)

**Item 210 — exact endpoint-anchor ceiling.**  Put $K=2j+2$ and
$A=3j+2$.  The two first-gate rows have rank zero exactly for
$K<p\le A$; above $A$, rank zero is impossible and rank one is
equivalent to divisibility of one explicit rational anchor $\mu_j$.  The
factorization


$$
\mu_j=L_jH_j,\qquad H_j\ne0,\qquad
L_j=2^{-j}[y^{2j+1}]{(y-1)^{3j+2}\over(1+y^2)^{2j+2}}
$$


reduces rationally singular bands to one integer coefficient sequence.  An
exact telescoper and finite nonzero verification through $j=20000$ imply,
without extrapolation, that the entire unresolved rank-one tail has
coefficient below $1/180009=0.00000555527779\ldots$ per $6m$.  This is
only $0.0283\%$ of the missing amount, so the family cannot close the gap
alone.  Isolated coefficient zeros beyond the verified prefix remain open.
Manifest: `results/item210_rankone_anchor_hashes.sha256` (SHA-256
`9b9ef4f7bd43e51db82a3c70b75be81992b31471dd1382f19399dc1e3c17e47d`).

**Item 211 — second lift on the structural ray.**  On
$s\equiv3\pmod4$, $p=5s+4$, at the regular anchor $j=1$, the
second digit has the exact sparse-sum form


$$
A_1\equiv {5\over24}\Phi_s\pmod p.
$$


All 285 ray primes through $p\le20000$ give nonzero $A_1$ at this
anchor, but this is finite evidence only.  The actual row
$(s,p,j,m)=(3,19,3,36)$ has $A_1=0$, so the behavior depends on the
anchor.  The whole ray still divides $10m+1$ and has only $O(\log m)$
weight.  Manifest: `results/item211_a1_structural_ray_hashes.sha256`
(SHA-256 `a998db95bb6f64a1f2253e4bd7b5045a792d1c01fed343df8d1551891572d383`).

**Item 212 — normalized off-ray phase eliminants.**  Every admissible prime
has an exact two-coefficient Frobenius-phase formula.  The structural ray is
the only prime-feasible simultaneous support gap; all off-ray zeros are
genuine cancellations.  In the stable band $b\le k+2$, common content is
equivalent to one prime dividing two explicit integers depending only on
$(b,k\bmod4)$; this retains the exact cancellation
$(s,p,b)=(299,2399,900)$.  The identity


$$
10m+1-b=(5j+5-q)p
$$


proves zero normalized weight for every collection
$b=o(m/\log m)$.  Far moving-$b$ cancellations remain open.  Manifest:
`results/item212_offray_phase_eliminant_hashes.sha256`
(SHA-256 `d37131ffcab02836545b739dce7c86d934957381499549349617f75efb2751df`).

All three packages passed canonical, independent replay, manifest, and
archive-layout verification.  They narrow Route 1 but add no positive
exponent.  Route 1 remains ACTIVE; Route 2 remains QUEUED.

## Items 213--214: actual beta phase and stable eliminant gcd (2026-08-31)

**Item 213 — actual Charlier carry-minus-slope phase.**  The actual beta
denominator has the exact polynomial realization


$$
\mathscr C_N(X)=\sum_{j=0}^N{N\choose j}X^{\underline j},\qquad
\mathscr C_N(-N-1)=(-1)^Nq_N.
$$


For $p>2N+1$, $p\mid q_N$, $s=p-1-N$, and
$\kappa=\mathscr C_N(s)/p$,


$$
{q_N\over p}\equiv(-1)^N\bigl(\kappa-\mathscr C_N'(s)\bigr)\pmod p.
$$


Thus lower squarefreeness is exactly the noncollision of one actual carry
and slope; the Wilson quotient cancels and supplies no independent first
digit.  The mirrored slope difference factors through the old moving
resultant $D_h$, so the coupled-square obstruction also remains.  The
prescribed-root scan through $p\le20000$ has no collision, but is finite
only.  Manifest: `results/item213_beta_hensel_phase_hashes.sha256`
(SHA-256 `a9c25ccce16db5e30d6178c3f4f48ef4549d598047ecaadb50c4c953e65e074d`).

**Item 214 — joint stable-phase gcd.**  The two Item-212 eliminants share an
exact hypergeometric common-term recurrence, and every feasible prime obeys


$$
qp\equiv b+4+5\sigma_r\pmod {20}.
$$


At $(b,r)=(900,3)$, the gcd factors completely as


$$
2^{449}\cdot911\cdot971\cdot991\cdot1031\cdot1051\cdot1091
\cdot1151\cdot1171\cdot1231\cdot1291\cdot2399.
$$


The first ten odd factors have the wrong phase class; $2399$ is the sole
feasible factor.  Complete exact factorization for every $b\le900$ finds
no other feasible node, but this is finite evidence.  The proved
$O(b\log b)$ numerator-height bound is globally too large and yields no
rate gain.  Manifest: `results/item214_stable_eliminant_gcd_hashes.sha256`
(SHA-256 `c2682dabe34875747826c381670850b10ab34c6b42252fc2d2116adcc7c2f29c`).

Both packages passed independent and archive-layout replay.  No new
Route-1 exponent or route-wide impossibility theorem follows.  Route 1
remains ACTIVE; Route 2 remains QUEUED.

## Items 215--216: diagonal zero spacing and the Gosper boundary (2026-08-31)

**Item 215 — diagonal-anchor candidate classification.**  The remaining
rank-one anchor coefficient has the exact 2-adic expansion


$$
\ell_j=(-1)^j\sum_{k=0}^{2j+1}(-1)^k2^k
 {2j+1+k\choose k}{3j+2+k\choose2j+1-k}.
$$


A unique least-valuation summand proves $\ell_j\ne0$, while every possible
zero is confined to an explicit tied-minimum binary-carry class.  Moreover,
$\ell_j\equiv(-1)^j{3j+2\choose j+1}\pmod4$, giving infinite carry-one
nonvanishing families.  The order-three recurrence forbids three consecutive
zeros, so the unresolved rank-one tail is now bounded by


$$
0.00000370388881791465827658443659\ldots\quad\hbox{per }6m,
$$


about one third below the Item-210 ceiling and still negligible compared with
the gap.  All-index nonvanishing remains open.  Ledger:
`results/item215_diagonal_nonvanishing_hashes.sha256` (SHA-256
`003fd02f81e9d3d41b0b3c54b1e2d69643edac10cb9ea2a2f747452ef9aa31d3`).

**Item 216 — unique contiguous residual and Gosper obstruction.**  The only
summation-index-independent combination cancelling the linear common weight is


$$
R_{b,r}=(r-b-2)\Phi_{g_1}+(b+1)\Phi_{g_0}.
$$


Its term quotient is a reduced quartic-over-quartic rational function.  On
every actual non-gap stable phase with $p>5$ and $b\ge5$, Gosper normal
form would require a polynomial of degree $(3b-8)/5$; the sole possible
collision class $b\equiv1\pmod5$ would force $p=5$.  Thus the direct
first-order hypergeometric telescoping route is closed.  The exact
$(b,p)=(900,2399)$ cancellation nevertheless survives in the residual, so
this is a method obstruction with zero rate credit, not a common-prime bound.
Ledger: `results/item216_gosper_phase_obstruction_hashes.sha256` (SHA-256
`17d23a86929aec0bdf88f5925b28fbff23b959c8eb139b53550104fa3e1e8913`).

Both packages passed canonical, independent, and archive-layout replay.  They
sharpen Route 1 without completing it or proving it globally impossible.
Route 1 remains ACTIVE; Route 2 remains QUEUED.

## Item 217: retained-state common-log invariant (2026-08-31)

The normalized common-log obstruction now has an exact retained five-coordinate
incidence matrix.  In the frozen Item-197 coordinates, the first two fixed
cells are common-log exactly when


$$
j=1:\quad 2Y'_0-Y_0=2Y'_1-Y_1=0,
$$


and


$$
j=2:\quad 9X_0-10Y_0+Y'_0=9X_1-10Y_1+Y'_1=0.
$$


An all-$m$ rational constant-term telescoper gives one contiguous relation,
and exact resultants show why it supplies only one projective condition rather
than zero propagation.  The relation fails after division by the moving
Cartier product.  Thin lower and upper phase edges have zero linear rate, but
no all-prime exclusion of either fixed cell is proved.

Conditionally excluding both cells would lower the remaining common-log mass
to $0.0188729973648737\ldots$ per $6m$, below the optimistic Route-1 gap by
$0.0007599863045581\ldots$.  This is a sharp sufficient target, not booked
progress.  Ledger: `results/item217_common_log_invariant_hashes.sha256`
(SHA-256 `7e120c1c0b367cbfd28797ff9366f7df35e2431893606bbe52e0cb48593e54d0`).

The canonical, independent, and archive-layout outputs are byte-identical.
Route 1 remains ACTIVE; Route 2 remains QUEUED.

## Item 219: the fixed $j=2$ common-log cell (2026-08-31)

For every admissible $j=2$ row, the two common-log quotients are now exactly
two four-residue beta-period sums $S_0(p,s),S_1(p,s)$, with all denominators
audited as units modulo $p$.  Thus the cell is exceptional exactly when


$$
S_0(p,s)=S_1(p,s)=0\pmod p.
$$


A boundary-free scalar Hermite reduction below Frobenius degree would force an
inconsistent six-equation system: its augmented determinant is


$$
2304s(2s+1)^2,
$$


a unit on every admissible row.  This closes that scalar mechanism only.
Frobenius-resonant $z^p$ primitives and non-scalar cohomology remainders remain
open, as does all-prime nonvanishing of the pair.

The exact finite replay covers 1,153 rows through $p\le401$, with separate
coordinate zeros but no simultaneous zero; this is not extrapolated.  Ledger:
`results/item219_common_log_j2_hashes.sha256` (SHA-256
`9b2292ff6345a14835b2369f9bf2137d467f4bdb2b513f462442ccac8dec5813`).
The package passed canonical, independent, and archive-layout replay.  No rate
is booked; Route 1 remains ACTIVE and Route 2 remains QUEUED.

## Items 218, 220--221: fixed-cell endpoint reductions (2026-08-31)

**Item 218 — the $j=1$ tail.**  Every row has
$p=4h+6s+3$, and the two primitive coordinates are explicit rational
tails of $\log(1+z^2)$.  The unique bounded-degree twisted-de-Rham identity
transfers the $\nu=1$ tail to four adjacent $\nu=0$ tails.  Fully factored
eliminants and phase resultants exclude every prime for all $s\ge1$ on
$0\le h\le8$.  Unbounded $h$ and its moving factorial residue remain open.
Ledger: `results/item218_j1_common_log_hashes.sha256` (SHA-256
`2c818db44c3a96487a8fbb4023ceddf2694766301d9d9c2b130d471006a1994a`).

**Item 220 — common endpoint coordinates.**  Exact Euler integration by parts
removes the finite logarithm entirely and leaves the incomplete endpoint vector
$(E_\nu,C_\nu,S_\nu)$.  One-good-prime full-rank certificates rule out all
polynomial-coefficient linear covectors and affine Bezout identities of total
degree at most eight in the stated ansatz.  This is an exact bounded-ansatz
no-go, not all-prime nonvanishing.  Ledger:
`results/item220_twisted_derham_fixed_cells_hashes.sha256` (SHA-256
`5c6ac428861db650941a6cfda3742371f1555b91f4857f6dc78fe1217f04b318`).

**Item 221 — first resonance and $j=2$ cohomology.**  Under the common gate,
the first scalar $z^p$ resonance is forced to zero.  A non-scalar exact
reduction survives with a genuine three-dimensional quadratic remainder and
reduces the cell to


$$
T_0=0,\qquad(5-2s)T_1+2(2s-1)T_2=0.
$$


An all-row determinant proves that the three remainder classes cannot be
collapsed by the same sub-Frobenius exact-form mechanism.  Higher resonances
and arithmetic nonvanishing of the residual pair remain open.  Ledger:
`results/item221_j2_twisted_cohomology_hashes.sha256` (SHA-256
`77495f72e0a3d9d2ead616824e3909959b83e0a29549ce10e4d3db6cbe2bd46d`).

All three packages passed canonical, independent, and archive-layout replay.
Their finite scans are evidence only.  No positive rate or divisibility
exponent is booked; Route 1 remains ACTIVE and Route 2 remains QUEUED.

## Item 224: inhomogeneous Cartier terminals for fixed $j=2$ (2026-08-31)

For the one-polynomial period sequence left by Item 221, Item 224 proves the
exact five-term moment recurrence and audits every forward and backward pivot.
Its first upper and lower Frobenius terminals are genuinely inhomogeneous:


$$
\tau(T)=7(-1)^r,\qquad \beta(T)=11.
$$


For $s\ge2$, an exact $z^3$-reduction confines every hypothetical
common-log collision to a one-dimensional initial line.  Propagation to both
terminals then gives the necessary condition


$$
\beta\ne0,\qquad \tau\ne0,\qquad
\Omega_{p,s}=7(-1)^r\beta-11\tau=0\pmod p.
$$



This is not sufficient.  In the exact finite classification through
$p\le401$, $\Omega\ne0$ excludes 1,108 of the 1,115 admissible
$s\ge2$ rows, but seven rows are formally compatible; direct evaluation
shows all seven are actual non-collisions.  They disprove any claim that this
single terminal compatibility always supplies a contradiction.  The $s=1$
family and all-prime or zero-rate control of $\Omega=0$ remain open.

The canonical, root, and archive-layout replays are byte-identical.  Ledger:
`results/item224_j2_cartier_terminal_hashes.sha256` (SHA-256
`0736a76f50c7151b2cc2200dd06803f2fb533d464841e36e31136e70027618fc`).
No capacity reduction is booked; Route 1 remains ACTIVE and Route 2 remains
QUEUED.

## Item 225: second Cartier condition for fixed $j=2$ (2026-08-31)

Item 225 regularizes every shifted primitive by deleting precisely its
$p$-multiple exponents.  This gives an exact inhomogeneous recurrence whose
first two Cartier-terminal weights are


$$
W_{\mathcal L}(p)=7,\qquad W_{\mathcal L}(2p)=29.
$$


The free mode introduced by the first resonance is exactly the coefficient
sequence of $g=(1-z)^r(1+z)(1+z^2)^{2s}$.  Since
$\deg g=(p+2s-1)/2<p-4$ for $s\ge2$, its four entries at the second
terminal vanish identically.  The second terminal therefore supplies a new
necessary collision condition $\Psi_{p,s}=0$, independent of that free
finite part.  Every collision must now satisfy


$$
\beta\tau\ne0,\qquad \Omega_{p,s}=\Psi_{p,s}=0\pmod p.
$$



All seven Item-224 $\Omega$-zeros through $p\le401$ have nonzero
$\Psi$, so the joint finite census is empty.  This is exact finite evidence,
not an all-prime theorem.  Simultaneous-zero control and $s=1$ remain open;
no rate is booked.  The audit explicitly retained the exact $-2p$ second
pivot, and canonical, root, and archive-layout replays agree byte-for-byte.
Ledger: `results/item225_j2_second_cartier_hashes.sha256` (SHA-256
`12cf4c62c058a5f22e4cd8089c042caad75a3ebf86e189e7ecb905001534b44d`).

## Items 222--223: uniform $j=1$ phase and corrected Frobenius transfer (2026-08-31)

Item 222 specializes the Item-218 eliminant on the actual prime phase
$p=6s+4h+3$. After a complete unit audit it gives one integer sequence
$A_h$, independent of $s$, such that every $j=1$ collision must satisfy


$$
p\mid A_h.
$$


The explicit height is $O(h\log h)$ when $A_h\ne0$, which is too large
after summing over moving $h$. Two exact 81-by-81 determinants rule out only
polynomial recurrences of order and coefficient degree at most eight. The
diagonal coefficient bridge and its parity pattern are retained with
finite/open labels; they book no rate. Ledger:
`results/item222_j1_phase_resultant_hashes.sha256` (SHA-256
`4f4f5b9365cea832b579f09113db0d4931576267df2fdf11f734fb43b4a0855b`).

Item 223 reduces the two $j=1$ endpoint conditions to the common moment line
$(u_0,u_1,u_2)=\lambda(1,1,-1)$ and transports it to the first lower and
upper Frobenius poles. The exact terminal multipliers are $p$ and $2p$,
so the sources are respectively $-2\epsilon$ and $-4\epsilon$. The
initial version that omitted this factor of two was withdrawn before archive
integration. The corrected necessary condition is


$$
\Delta_+=2\Delta_-\ne0\pmod p.
$$


On $r=2s$, an exact involution instead gives
$\Delta_+=\Delta_-$, proving all-prime noncollision on the entire diagonal.
The exact finite replay through $p\le2000$ leaves 22 off-diagonal transfer
survivors, none a direct paired zero; no all-prime or density conclusion is
drawn. Ledger: `results/item223_j1_frobenius_transfer_hashes.sha256`
(SHA-256
`be0a308756bf75b8a658e4c25bc957672737364fd61ab03ddd5875baaa045895`).

Both corrected packages have byte-identical root and archive-layout replays.
Neither changes the Route-1 exponent. Route 1 remains ACTIVE and Route 2
remains QUEUED.

## Item 226: exact four-phase closure for fixed $j=2$ (2026-08-31)

The regularized $j=2$ state now transfers across every Cartier phase by one
exact affine map


$$
Y_{q+1}=MY_q+bW(qp),\qquad W(p),W(2p),W(3p),W(4p)=7,29,11,-11.
$$


The terminal coefficient is exactly $-qp$, so it cancels the denominator
$qp$ before reduction. Coefficientwise $4p$-periodicity then gives an
affine fixed-point equation. Combining its four coordinates with the bottom
condition and four terminal conditions produces nine equations in the one
candidate scalar. Their consistency is exactly an augmented-rank, or 36-minor,
criterion. When $\det(I-M^4)\ne0$, closure on the candidate line is
equivalent to the original common-log gate, not merely necessary.

The exact finite census through $p\le401$ finds the nine-equation system
inconsistent on all 1,115 admissible $s\ge2$ rows. Fifteen rows have
$\det(I-M^4)=0$, and each is still inconsistent; individual closure minors
also have explicit zeros, so no uniform-minor claim is made. The all-prime
augmented-rank theorem and $s=1$ remain open. Canonical, root, extended
identity, and archive-layout checks pass. Ledger:
`results/item226_j2_four_phase_closure_hashes.sha256` (SHA-256
`159847718ff612390da807443af21f550875e49308b4e31b9e372a735259cf0d`).
No rate is booked; Route 1 remains ACTIVE and Route 2 remains QUEUED.

## Items 231--233: explicit second coefficient, algebraic diagonal, and phase ceiling (2026-08-31)

Item 231 eliminates the propagated $j=1$ auxiliary scalars in favor of two
coefficients of one generating series.  With


$$
D(x)=\frac1{(1-x)^{r+1}(1+x^2)^{2s}},\quad
 R(x)=2r+4s-1+(r+1)x-(r+8s)x^2,
 \quad g_n=[x^n]R(x)D(x),
$$


every collision must satisfy


$$
g_a=2\Delta_-\ne0,\qquad g_{a+p}=-\Delta_-,\qquad a=2s+4.
$$


The defect $g_{a+p}-g_a$ is one exact Cartier coefficient and one exact
same-row reciprocal sum.  Its Gosper reduction still contains a fixed-$s$
incomplete-binomial coordinate.  The extended root census through
$p\le2500$ has 34,882 rows and no joint $\Theta=\Psi=0$ row, but this is
finite evidence only.  Ledger:
`results/item231_j1_second_phase_coefficient_hashes.sha256` (SHA-256
`6abb90712e85fa15f10c0e3d11fcd63630bf304b0dbbd0910f7f8c3bdccd5e6a`).

Item 232 proves that the diagonal incomplete-binomial sequence


$$
S_n=\sum_{j=0}^n(-1)^j\binom{2n+j-1}{j}
$$


has algebraic generating function


$$
(16+104z-27z^2)G^3-(16+108z)G^2+21zG-z=0
$$


and an exact factored order-two recurrence.  This sequence was already
recorded as OEIS A371813, so the package makes no novelty claim.  More
importantly, its adjacent recurrence changes both the endpoint and binomial
parameter and therefore does not eliminate Item 231's fixed-parameter sum.
Ledger: `results/item232_incomplete_binomial_gf_hashes.sha256` (SHA-256
`f339e1eeea01214478a4444b426f224b57af6e178bc1ef13631acfe84b4fdc6a`).

Item 233 completely classifies the remaining antiperiod closure coordinates.
The endpoint map is conjugate to the modes $1,i,-i$, and


$$
\det(I+M^2)=(h_0-h_1)^2+(1-h_0)^2.
$$


Every singular affine closure is consistent.  A coefficientwise residual
identity then proves, without dividing by this determinant, that all six
Item-230 phase equations are formally equivalent to the already known
$\Delta_+\ne0,\Theta=\Psi=0$ terminal system.  Thus continuing the same
functional through extra phases supplies no third invariant.  This is a
scoped structural no-go, not an all-prime exclusion of the $j=1$ cell.
Ledger: `results/item233_j1_antiperiod_determinant_hashes.sha256` (SHA-256
`0a1d1114afe0ef83ae970413fe719cf63c7b56e942e3a0285d0bc27ac8d145f4`).

All three packages passed independent root audit and byte-identical canonical
replay.  No rate is booked; Route 1 remains ACTIVE and Route 2 remains QUEUED.

## Item 229: fixed-$h$ decomposition of the $j=1$ determinant (2026-08-31)

The corrected first-transfer determinant has an exact all-$h$ polynomial
Gosper decomposition


$$
\Theta_h(s)=c_h(s)S_s+t_{s+1}G_h(s)-2\Delta_-(h,s),
 \qquad S_s=\sum_{j=0}^s(-1)^j\binom{2s+j-1}{j}.
$$


Here $\deg_s c_h=2h+1$ and
$[s^{2h+1}]c_h=-2^{4h+2}/(2h)!$, so this displayed direct ansatz genuinely
retains the incomplete-binomial coordinate. This is not a non-rationality or
independence theorem: another holonomic or arithmetic identity could still
control it. The attractive phase proportionality through $h\le80$ and the
empty joint $\Theta/E$ census through $p\le2000$ remain EXACT FINITE only.
Ledger: `results/item229_j1_fixed_h_theta_hashes.sha256` (SHA-256
`97f9f71541904e7c17357a7d6fe95c6cf3bfcce349387f954f4aed3910edc798`).

## Item 227: exact order-four control and phase-redundancy no-go for $j=2$ (2026-08-31)

For the fixed $j=2$ transfer, the feedback matrix $N=M+\epsilon ba$ is
conjugate to the four-cycle: $N^4=I$, its observability matrix is invertible,
and


$$
\det(I-M^4)=F_1F_{-1}F_i=\det(O)\det(U).
$$


Every singular left null vector kills the forcing column, so a singular
closure determinant is never itself an affine contradiction. Exact endpoint
Fourier identities also give $E_4=0$ and $E_3=E_2-E_1$; phases 3 and 4
therefore add no invariant beyond the existing $\Omega,\Psi$ pair. This is
a scoped structural no-go, not an exclusion of the cell. The finite factor
census through $p\le401$ is not extrapolated. Ledger:
`results/item227_j2_phase_control_hashes.sha256` (SHA-256
`6a514c043253ddcced0102bd7ef912b158880c8fc537da90efd6b26159d72db2`).

## Item 230: antiperiodic phase closure for fixed $j=1$ (2026-08-31)

The corrected $j=1$ recurrence has one exact phase-independent affine map.
The terminal multiplier at phase $a$ is $ap$, whose factor $a$ cancels
the resonant denominator before reduction. Coefficientwise the regularized
moments are $2p$-antiperiodic and $4p$-periodic, with normalized source
cycle $(-4,2,4,-2)$. A collision must solve six scalar equations in one
normalization parameter; formal solvability is exactly a rank-one augmented
matrix condition. When $\det(I+M^2)\ne0$, that condition is equivalent to
the original common-log gate.

The exact finite census through $p\le601$ finds all 2,435 rows inconsistent,
including the three determinant-zero rows. This is finite evidence only;
all-prime augmented-rank inconsistency and the singular locus remain open.
Ledger: `results/item230_j1_phase_closure_hashes.sha256` (SHA-256
`462e696313e0570835db202e10e23cc3c6a8242c731817b766bbfcf2c380052d`).
No rate is booked; Route 1 remains ACTIVE and Route 2 remains QUEUED.

## Item 228: second Frobenius condition for off-diagonal $j=1$ (2026-08-31)

Regularizing the Item-223 Pearson moments by deleting exactly the primitive
denominators divisible by $p$ gives an explicit deleted-derivative forcing.
At the next pole the unreduced primitive has denominator $3p$, the exact
recurrence multiplier is $3p$, and the audited terminal source is
$+2\epsilon$. The free mode born at the preceding $2p$ pole is exactly
$W=(1-z)^r(1+z^2)^{2s-1}$; its support ends before the next three terminal
entries. Therefore every collision must satisfy


$$
\Delta_+=2\Delta_-\ne0,\qquad
\Psi=\Delta_+(\rho_0-2\epsilon)-4\epsilon\rho_1=0\pmod p.
$$


This is a necessary condition only. All 22 corrected Item-223 survivors
through $p\le2000$ have $\Psi\ne0$, an exact finite result with no
all-prime or density inference. Root audit extended the source/sign replay
through $p\le401$, covering 1,151 rows and 304,599 forcing steps. Ledger:
`results/item228_j1_second_frobenius_hashes.sha256` (SHA-256
`c3cd3faa3d18e884806697fb9db55c8715993e97db79fb289b6477ff31afd8de`).
No rate is booked; Route 1 remains ACTIVE and Route 2 remains QUEUED.

## Item 236: all-$h$ phase-cokernel identity (2026-08-31)

The finite phase coincidence observed in Item 231 is now an all-$h$ theorem.
For the Gosper operator


$$
\mathcal L_sU(j)=-(2s+j)U(j+1)-jU(j),
$$


the finite falling-moment functional


$$
\Phi_s(j^n)=\sum_{k=0}^n {n\brace k}
              \frac{(-2s)^{\underline k}}{2^k}
$$


annihilates $\mathcal L_s$ and returns the unique cokernel residual.  Its
exact binomial reflection, specialized at
$s_*=-(4h+3)/6$, proves


$$
c_h^+(s_*)=c_h^-(s_*)\qquad(h\ge1).
$$


The proof is entirely coefficientwise and uses no infinite-series evaluation.
It synchronizes the two residuals but neither makes their common value vanish
nor relates it all-$h$ to Item 222's eliminant.  Ledger:
`results/item236_j1_phase_cokernel_hashes.sha256` (SHA-256
`412ff18e0b6aa86c30a0b83cc292d9fe02889804e77a4381f27086f6fb9478ab`).
No rate is booked; Route 1 remains ACTIVE and Route 2 remains QUEUED.

## Item 234: actual coefficient-level $j=1$ Witt digit (2026-08-31)

For each original Item-197 coordinate, an exact support zero first proves
$p\mid C_\nu$.  Expanding the two Frobenius factors through the next order
gives a harmonic linear correction and the quadratic square


$$
6U^2V^{-5}(VA-UB)^2.
$$


On the original per-coordinate gate $p^2\mid C_\nu$, the first true Witt
digit is


$$
\frac{C_\nu}{p^2}\equiv
\Omega_\nu^W
=6\frac{Q_\nu}{p}+12R_\nu+E_\nu
=-6\epsilon\frac{M_\nu}{p}+6J_\nu+E_\nu\pmod p.
$$


Thus $p^3\mid C_\nu$ is equivalent to $\Omega_\nu^W=0$, coordinate by
coordinate.  This does not prove that a simultaneous first-gate row exists or
is excluded all-prime.  A separate exact calculation shows that lifted
antiperiodicity has a squared-denominator carry, so naive mod-$p^2$ phase
closure is invalid.  Ledger: `results/item234_j1_first_witt_hashes.sha256`
(SHA-256
`200951439ccc70066cbb47c0b33d6a3ecfae9018f2bd7df586f6cb1325cbb80e`).

## Item 235: canonical $j=2$ terminal lift and actual-bridge barrier (2026-08-31)

The localized beta periods have exact $q p$ terminal multipliers over
$\mathbb Z/p^2\mathbb Z$, a nonzero harmonic $4p$ carry, and a canonical
Witt/Hensel row system.  Corrected four-phase closure is exactly generated by
the terminal rows and therefore adds no invariant inside that model.

Crucially, this canonical lift is not yet the lift of the original integer
common-log quotient.  At $(p,s,\nu)=(17,2,0)$,


$$
C_0/p\equiv224\pmod{17^2},\qquad
\text{naive beta lift}\equiv173\pmod{17^2},
$$


a difference of $3p$.  The missing digit contains both harmonic Frobenius
terms and a quadratic correction.  Hence neither an ordinary collision nor an
extra $p^3$ digit is yet proved to force the canonical Witt rows.  Ledger:
`results/item235_j2_witt_terminal_hashes.sha256` (SHA-256
`239f044dbea93a39ca5ec75325b86c8b7ea8e491196a9de5ba2139fdf44ad58e`).

Both packages passed root and archive-layout replay.  They book no capacity,
rate, or divisibility exponent; Route 1 remains ACTIVE and Route 2 QUEUED.

## Item 238: squared-denominator recurrence and corrected lifted closure (2026-08-31)

The squared-denominator coordinate forced by Item 234 satisfies the exact
coupled recurrence


$$
\bar B_tv_t-\bar C_tv_{t+1}+\bar D_tv_{t+2}-\bar A_tv_{t+3}
 =u_t-u_{t+1}+u_{t+2}-u_{t+3}.
$$


Coefficientwise expansion of each retained denominator gives the corrected
phase closures


$$
Y_{a+2}+Y_a=2pK\overline Y_a,\qquad
 Y_{a+4}-Y_a=-4pK\overline Y_a\pmod {p^2},
$$


where the all-row isomorphism $\Phi$ identifies
$K=\Psi\Phi^{-1}$ on the three endpoint modes $1,i,-i$.  Thus this
carry adds neither a fourth first-digit endpoint mode nor a new scalar at one
terminal.  Whether the same closure is redundant after imposing the actual
coefficient-level $p^3/\Omega^W$ gate remains open.  Ledger:
`results/item238_j1_squared_carry_hashes.sha256` (SHA-256
`bc115a3ee321257ba78e9f153765c2b18546be15e6f7644cffca69daf2e7758d`).

Canonical, root, extended, and archive-layout replays pass.  No common-log
exclusion or rate is booked; Route 1 remains ACTIVE and Route 2 QUEUED.

## Item 239: corrected actual $j=2$ Witt bridge (2026-08-31)

The original integer quotient in the fixed $j=2$, $s\ge2$ cell now has a
complete expansion modulo $p^2$:


$$
\frac{C_\nu}{p}\equiv
 -35(-1)^{r+1}\bigl(S_\nu^{(2)}+pK_\nu\bigr)\pmod {p^2}.
$$


Here $S_\nu^{(2)}\bmod p$ is exactly the ordinary Item-219 beta period,
and $K_\nu$ is an explicit depth-one harmonic/inverse-square carry plus a
depth-two quadratic convolution coordinate.  Consequently


$$
p^3\mid C_\nu\iff S_\nu^{(2)}+pK_\nu=0\pmod {p^2}.
$$


The corrected coefficient kernel is not four-periodic: on the supported
$(p,s,\nu)=(17,2,0)$ row, denominators 2 and 6 have corrected derivative
weights 12 and 199 modulo $17^2$.  This proves coefficientwise nonmembership
in the old $1,i,-i$ endpoint span, but does not exclude aggregate
cancellation on the restricted $P_\nu$ family.

The ordinary common-log gate asks only for $p^2\mid C_0,C_1$, so the exact
extra-digit criterion does not exclude that cell.  The finite census and its
single individual $p^3$ row are not extrapolated.  Ledger:
`results/item239_j2_actual_witt_bridge_hashes.sha256` (SHA-256
`280c63107defad5498e5e7c335966a1bb122a115e80cedbf27347814b56594f4`).
No rate or capacity is booked; Route 1 remains ACTIVE and Route 2 QUEUED.

## Item 240: the $j=1$ Witt digit and endpoint tower (2026-08-31)

Item 234's Hermite carry is exactly a squared-denominator endpoint
functional:


$$
\begin{aligned}
 J_0&=2\epsilon(v_0^{\sin}+v_1^{\sin}+v_2^{\sin}+v_3^{\sin}),\\
 J_1&=2\epsilon(v_0^{\sin}+4v_1^{\sin}+6v_2^{\sin}
                         +4v_3^{\sin}+v_4^{\sin}).
\end{aligned}
$$


Therefore, conditional on the original coordinate gate $p^2\mid C_\nu$,


$$
\Omega_\nu^W=-6\epsilon M_\nu^{(1)}
               +12\epsilon V_\nu^{\sin}+E_\nu,
\qquad
 p^3\mid C_\nu
 \iff M_\nu^{(1)}
      =2V_\nu^{\sin}+(6\epsilon)^{-1}E_\nu\pmod p.
$$



For every denominator power $k\ge2$, the endpoint moments satisfy an exact
coupled recurrence to level $k-1$; the terminal maps all factor through the
same three Fourier modes.  Hence increasing the denominator power adds no
fourth endpoint mode or one-terminal scalar.  The remaining Frobenius defect
$E_\nu$, however, is not a universal linear functional of the level-one
and level-two endpoint state: an exact rank witness over $\mathbb F_{29}$
raises the functional rank from six to seven.  This obstruction is only to a
universal linear formula; actual-family identities and finite enlarged
recurrences remain open.

Canonical, root, extended, and archive-layout replays pass.  The $p=109$,
$k\le12$ tower experiment is finite-only.  Ledger:
`results/item240_j1_witt_endpoint_bridge_hashes.sha256` (SHA-256
`08865168c4dfab2904db2d115988d36376a305770871ce9f565d69249737435a`).
No common-log exclusion or rate is booked; Route 1 remains ACTIVE and Route 2
QUEUED.

## Item 237: algebraic common $j=1$ residual (late freeze, 2026-08-31)

The common phase residual left by Items 229, 231, and 236 is now an exact
algebraic coefficient:


$$
c_h^*=[x^{2h}]C(x),\qquad
 C(x(y))=\frac{N(y)}{D(y)^3},\qquad
 x=\frac{y(1+y)}{(1+y+y^2/2)^{2/3}}.
$$


Eliminating $y$ gives a primitive equation
$\mathscr P(x^3,C(x))=0$ of bidegree $(9,6)$.  A symbolically certified
order-three, step-three recurrence


$$
\sum_{k=0}^3p_k(h)c_{h+3k}^*=0,\qquad \deg p_k=16,
$$


holds for every $h\ge1$.

The observed factorization $c_h^*=\mathcal R_hE_h^*$ is not promoted:
it is exact through the stated finite range, and its predicted gauged
recurrence passes two-prime checks, but a symbolic bivariate
WZ/Hermite certificate is still missing.  A separate rank calculation rules
out only first-order rational recurrences of degree at most five for the
specified $K_h/E_h^*$ subsequences.

After correcting one omitted displayed $(-1)^j$, canonical, root,
independent-series, and archive-layout checks pass.  Ledger:
`results/item237_j1_algebraic_residual_hashes.sha256` (SHA-256
`0283a7468863ea0ca05f92a96eb07d7ef4d0c0857cec86bd944196370bea89c8`).
No all-prime nonvanishing or rate follows; Route 1 remains ACTIVE and Route 2
QUEUED.

## Item 241: character-harmonic collapse of the corrected $j=2$ kernel (2026-08-31)

Every quadratic convolution section in Item 239 collapses for all
$p\ge17$ and $1\le n<p$ to ordinary harmonic prefixes and the single
mod-$4$ character prefix


$$
\mathcal O_u=\sum_{j=0}^{u-1}\frac{(-1)^j}{2j+1}.
$$


The full corrected kernel has explicit even/odd formulas and, on each parity,
is the output of a seven-coordinate rational first-order state.  For odd
$n=2u+1$, the genuinely new coordinate


$$
R_u=(-1)^u\mathcal O_u,\qquad
 R_{u+1}=-R_u-\frac1{2u+1},
$$


enters with the $p$-unit coefficient $90/(2u+1)$.

This proves a finite coefficient-state theorem, not a boundary-only terminal
recurrence.  After summation against the actual $P_\nu$ coefficients, the
nonzero source leaves a bulk moment unless a further restricted-family
telescoping identity removes it.  Moreover, $K_\nu$ belongs only to the
stronger $p^3$ test of Item 239; it does not strengthen the ordinary
$p^2$ common-log gate.

Canonical, root, independent-convolution, and archive-layout checks pass,
including independent primes through $1009$.  Ledger:
`results/item241_j2_character_harmonic_collapse_hashes.sha256`
(SHA-256
`886799c094467ffa2e35093e6a21318cbfd41fc01ebcb45cef34199365665437`).
No rate or capacity is booked; Route 1 remains ACTIVE and Route 2 QUEUED.

## Item 242: finite phase module of the $j=1$ Frobenius kernel (2026-08-31)

The remaining Item-240 functional has one common rational kernel for both
coordinates,


$$
\mathcal H_E(z)=\frac{R_E(z)}{(1+z^{2p})^5},
$$


and every $p$-section obeys the exact phase recurrence


$$
(S_p^2+1)^5e=0.
$$


Rootwise multiplicity proves that the least common multiple of all reduced
section denominators is $(1+Z^2)^5$.  Thus the full section module has
minimal eventual phase polynomial $(X^2+1)^5$: relative to the old
semisimple $\pm i$ pair, it contains eight additional generalized
$\pm i$ directions.  When $1+Z^2$ splits, different sections may witness
the two fifth powers; no single coprime section is asserted.

Both actual observations are short convolutions of this common state:


$$
E_0=e_0+e_1+e_2+e_3,\qquad
 E_1=e_0+4e_1+6e_2+4e_3+e_4.
$$


On the full degree-$12$ input space over $\mathbb F_{29}$, adjoining
$E_0,E_1$ raises the old endpoint rank from six to seven to eight.  This
is a universal-linear no-go, not an actual-binomial-family independence
theorem.

Root audit corrected the split-factor scope, then independently matched the
rootwise module proof and the exact rank matrix.  Ledger:
`results/item242_j1_E_kernel_state_hashes.sha256` (SHA-256
`a9ec3ee470196e0eeeced7c8955fa29c819b3e323b5e6c334cab6cfbc0ec12da`).
No common-log exclusion or rate is booked; Route 1 remains ACTIVE and Route 2
QUEUED.

## Item 244: Abel reduction of the actual $j=2$ character bulk (2026-08-31)

The odd-denominator projection of the actual row polynomial has the exact
factorization


$$
D_\nu(t)=\sigma(1-t)^{\min(r,1+3\nu)}
 (1+t)^{2s-\nu}
 \sum_j\binom{|r-(1+3\nu)|}{2j+(r\bmod2)}t^j.
$$


It vanishes exactly on the line $\nu=0,r=1$, where $P_0$ is even.
For every nonempty projection, exact Abel summation reduces Item 241's
character contribution to


$$
K_\nu=K_\nu^{\rm base}
+90\mathcal O_L\mathsf S_\nu-90\mathsf B_\nu.
$$


The boundary term $\mathsf S_\nu$ is an already known sine endpoint;
$\mathsf B_\nu$ is one uniquely terminal-normalized bulk residual.

The residual is not identically zero, and a $p=19$ two-coordinate witness
rules out a common coordinate-independent multiple of $\mathsf S_\nu$.
This is a one-residual normal form, not a proof of independence from every
larger harmonic state.  Canonical, root, independent, and archive-layout
checks pass; the extension through $p\le1009$ is finite-only.  Ledger:
`results/item244_j2_actual_character_bulk_hashes.sha256` (SHA-256
`f302e55adeba8f5fddf558381444c5c0adec15f5f4d152c34cf0fa6895f3d9cd`).
The identity concerns only the stronger $p^3$ carry.  No ordinary
common-log capacity or rate is booked.

## Item 245: actual-family generalized $\pm i$ observations (2026-08-31)

For each of the two actual $j=1$ target sections, the row identity and
$\deg R_E\le8p-1$ force the section numerator to have degree at most seven.
Its fifth $(1+Z^2)$-adic digit therefore vanishes identically: the old
simple-pole $\pm i$ pair is not separately excited.  After the canonical
one-factor recurrence-module normalization, the surviving state is


$$
\mathbb F_p[Z]/(1+Z^2)^4.
$$



If the leading digit is $\alpha_\nu+\beta_\nu Z$, the exact normalized
eight-phase determinant is


$$
\det\mathcal T_\nu=(\alpha_\nu^2+\beta_\nu^2)^4.
$$


Both entries have explicit finite alternating formulas in coefficients of
$B_0^2P_\nu$.  Reciprocity aligns the two target residues to one reflected
residue, and local root valuations give exact individual and stacked-rank
formulas; it does not identify the two coordinate factors.

The census through $p\le601$ has coordinate-rank counts
$4851,18,1$ at ranks $8,7,6$, respectively, and no joint rank drop, but
all of those counts are finite-only.  Root independently reconstructed 368
coordinates through $p\le151$, checked the determinant on all 195 leading
pairs over $\mathbb F_5,\mathbb F_7,\mathbb F_{11}$, and reproduced the
archive replay byte-for-byte.  Ledger:
`results/item245_j1_generalized_phase_observation_hashes.sha256` (SHA-256
`86466cd2091d02c5006a15f78605f1212f399afadbfc94e7541c6ecc6c2064ef`).
Uniform joint nonvanishing and any $p^3$ terminal obstruction remain open;
no ordinary common-log rate is booked.

## Item 246: structure of the $j=2$ bulk residual (2026-08-31)

For $D(t)=\sum_vd_vt^v$ and $N_v=2(L+v)+1$, Item 244's residual has
the closed form


$$
\mathcal B_L[D]
 =\sum_{0\le k<v\le d}
 \frac{(-1)^{v-k-1}d_v}{N_kN_v},
$$


equivalently an exact polynomial double integral.  Multiplication by
$1+\epsilon t$ acts through an explicit recurrence coupling
$\mathcal B_L$ and the old alternating endpoint $\mathcal S_L$, giving
a finite recurrence in the actual row parameters.

Coefficient reversal relates $\mathcal B_L$ to the distinct pole
$L^\vee=-L-d-1$; the proved inequality $0<2L+d+1<p$ excludes a
one-pole reciprocity closure.  Likewise, the two actual coordinates require a
nonzero companion parity, so neither visible symmetry eliminates the
residual.

Individual modular nonvanishing is false: the exact rational value at
$(p,s,\nu)=(37,4,0)$ is nonzero but its numerator has $37$-adic
valuation one.  The absence of simultaneous residual zeros through
$p\le401$ remains finite-only.  Canonical, root, independent, and
archive-layout checks pass.  Ledger:
`results/item246_j2_bulk_residual_structure_hashes.sha256` (SHA-256
`b0a8895f8753f341fa4c33328bef98b36a1fc5e600294685e7248e737262fd24`).
This still concerns only the stronger $p^3$ carry; no ordinary rate or
capacity is booked.

## Item 247: eliminant for the two $j=2$ bulk residuals (2026-08-31)

On the actual fixed-$j=2$ locus, write
$r=(p-6s-3)/2$.  Admissibility forces this $r$ to be positive and odd;
it is unrelated to the even parameter used in the separate $j=1$ branch.
The common selected-parity state in the two residuals is eliminated by


$$
\binom{\mathsf B_0}{\mathsf B_1-Z}
 =\begin{pmatrix}1&1\\1&3\end{pmatrix}\binom{X}{Y},
 \qquad\det=2.
$$


Writing $R=r-1$ and decomposing
$(1-z)^R=E(z^2)-zO(z^2)$, the exact identity


$$
R E=[1+(R-1)t]O+2t(1-t)O'
$$


reduces the regular coordinate pair to two explicit functionals of the one
odd seed $O$.  The bookkeeping determinant of the two algebraic elimination
steps is $2(r-1)$, a $p$-unit on every regular row.  Its only singular
line is the genuinely admissible family $r=1$, where $D_0=0$ and one
explicit scalar $\mathcal B_1[(1-t)(1+t)^{2s-1}(3+t)]$ remains.

After clearing one specified $p$-unit denominator, simultaneous vanishing is
exactly the moving-prime condition $p\mid\gcd(I_0,I_1)$.  No factorization
or nondivisibility theorem for this content is known.  Root independently
verified the polynomial and rational identities on 169 rows through
$p\le151$, including the exact $(127,11)$ witness where the eliminated
scalar vanishes without either coordinate vanishing.  The empty pair census
through $p\le401$ and singular scan through $p\le20000$ are finite-only.
Ledger: `results/item247_j2_bulk_pair_eliminant_hashes.sha256` (SHA-256
`a989d4120b6b8a4a709db4b65d7f5ccdb98d328c1422152abe7811c73e92c385`).
This remains a stronger-$p^3$ reduction and books no ordinary rate.

## Late-frozen Item 248: local $j=1$ tails and Wronskian no-go (2026-08-31)

At a root $I^2=-1$, the two Item-245 leading factors now have exact local
$u$-tail formulas.  The square of the local truncated logarithm satisfies
$[u^k]A_p(u)^2=8H_{k+1}/(k+2)$, and the remaining four-linear-factor
polynomial has a fourth-order Pearson recurrence with only $p$-unit pivots.
This replaces the large global convolution by a short exact local state.

Each leading coefficient is a second parameter derivative of a coefficient
$F_\nu(\lambda)$ with forced factor
$\lambda^{\underline{r+1}}$.  A common leading root therefore forces one
division-free two-by-two logarithmic-moment Wronskian to vanish.  That
necessary Wronskian is not universally a rootwise unit: exact split-root
zeros occur at $(p,h,s)=(109,4,15)$ and $(149,26,7)$.  Division by an
individual seed also fails at $(41,2,5)$, and individual leading-pair
nonvanishing is false at $(59,2,8,\nu=1)$.

The corrected census through $p\le601$ finds no common leading root, but
all 2,435 rows and all zero counts are finite-only.  Root independently
reconstructed 66 local/global coordinates through $p\le61$, the three
types of exact counterexample, and the generic falling-factor determinant
identity.  Ledger: `results/item248_j1_joint_root_reduction_hashes.sha256`
(SHA-256 `e9297510d48f7b319102d4834bfdfcf661908eb08ecbf091d894251f291ed3fd`).
The Wronskian no-go does not disprove joint nonvanishing.  No rate or capacity
is booked.

## Item 249: the singular $j=2$ bulk recurrence (2026-08-31)

On Item 247's singular line $r=1$, put


$$
M=2s+1=(p-2)/3,\qquad n=M-2.
$$


The surviving polynomial is
$D_1=(3-2t-t^2)(1+t)^n=\sum_vd_vt^v$, and its residual is exactly


$$
\mathsf B_1=\sum_{v=1}^{M}
 \frac{(-1)^{v-1}d_v}{2v+3}
 \sum_{k=0}^{v-1}\frac{(-1)^k}{2k+3}.
$$


The coefficients obey a proved order-three recurrence.  Since
$n\equiv-8/3\pmod p$, they agree through degree $M$ modulo $p$ with
the coefficients $c_v$ of the fixed series
$(1-t)(3+t)(1+t)^{-8/3}$.  Thus
$\mathsf B_1\equiv\Theta_M\pmod p$, where $\Theta_m$ is a
$p$-independent rational recurrence and every denominator through the
moving endpoint is a $p$-unit.

The criterion is exact: singular-row vanishing is equivalent to $p$
dividing the reduced numerator of $\Theta_{(p-2)/3}$.  At the excluded
boundary $(p,s,M)=(11,1,3)$, both the actual value $88/945$ and the
universal value $-49676/25515$ vanish modulo $11$, so the recurrence has
no automatic unit invariant.  No admissible zero occurs through
$p\le20000$, but that is finite-only.  Root independently replayed the
polynomial identity, recurrence, triangular sum, universal reduction, unit
range, endpoints, and 84 prime rows through $p\le1000$.  Ledger:
`results/item249_j2_singular_bulk_hypergeometric_hashes.sha256` (SHA-256
`33d463871b00d794ab9aa5c9ac5fb61c7cb5f6dc3ac72d420cc0731c358cfbdc`).
This scalar still belongs only to the stronger $p^3$ carry.  No rate or
capacity is booked; Route 1 remains ACTIVE and Route 2 QUEUED.

## Item 250: affine localization of the ordinary $j=2$ gate (2026-08-31)

On the ordinary Item-219 cell


$$
p=2r+6s+3,\qquad r\ge1\text{ odd},\qquad Q=2s,
$$


the moving beta sums are controlled by


$$
J_k=\sum_{t=0}^{Q-1}\binom{Q-1}{t}\frac1{Q+k+2t},\qquad
 (3Q+k)J_{k+2}=2^Q-(Q+k)J_k.
$$


At the first Frobenius pivot, the terminal summand has denominator exactly
$p$; retaining it gives the inhomogeneous identity


$$
J_{2r+3}=\frac{2^Q-1}{Q+2r+3}\pmod p.
$$


Consequently both lower logarithmic tails are affine in one common period
$e=J_0$ and $c=2^Q$.  Exact coefficient reversal identifies the
$e$-coefficients with the two upper factorial-tail coefficients:
$\mathsf a_\nu=\kappa_rf_\nu$.  Thus the gates have the rank-one form


$$
G_\nu=f_\nu Z+P_\nu^\flat c+H_\nu^\flat,
$$


and every simultaneous collision satisfies the division-free conditions


$$
L_rc+M_r=0,\qquad
 \mathcal R_r=L_r^3+2^{2r+2}M_r^3=0\pmod p.
$$



The lower factorial range $N_a=r+Q+1$ and the distinct upper ranges
$D=(r+Q+1)/2$, $R=Q+D$ are all proved to be below $p$; the sole
Frobenius denominator is retained rather than inverted.  The eliminants are
necessary only.  At $(p,s,r)=(367,39,65)$, both vanish while
$(G_0,G_1)=(238,354)$; $p=67$ is a cubic-only false positive, and at
$p=953$ one gate vanishes without the other.  The census through
$p\le401$ is EXACT FINITE ONLY.

Two isolated root replays are byte-identical to the canonical output, and a
dependency-free root implementation reproduces 510 coordinates on 85 rows
plus the critical witnesses.  Ledger:
`results/item250_j2_ordinary_phase_hashes.sha256` (SHA-256
`80102d28cecd07226c15b17d9b728a14f06eeb1f4f4b6371c17f83cabab402c7`).
Control of the actual period $Z$ on eliminant-zero rows, all-prime or
weighted control of $\mathcal R_r$, and every rate consequence remain
OPEN.  Item 250 books zero capacity and zero exponent; Route 1 remains ACTIVE
and Route 2 remains QUEUED.

## Item 251: the surviving ordinary $j=2$ period (2026-08-31)

After Item 250's rank-one elimination, write


$$
B_s=\frac{(2s-1)!(s-1)!}{(3s-1)!},\qquad
 A_s=\sum_{j=0}^{2s-1}\binom{3s-1}{s+j}\binom{s+j-1}{j}.
$$


The common period and factorial tail are exactly


$$
e=\frac{B_s}{2}A_s,\qquad
 \mathfrak f=B_s\tau_{r,s},\qquad
 \tau_{r,s}=(-1)^{s+h}\frac23\frac{(s)_{h+1}}{(3s+1)_{h+1}},
$$


so the missing gate coordinate is


$$
Z=B_s\left(\frac{9\kappa_r}{2}A_s-\tau_{r,s}\right).
$$


All displayed denominators are proved $p$-units on every actual row.

The integer $A_s$ is a diagonal of
$((2+x)^{3s-1}-1)/(1+x)$.  Its algebraic generating function is obtained
from $w=t(2+w)^3$, and an endpoint-vanishing bivariate telescoper proves an
exact order-two recurrence.  The increment
$\Delta_s=A_{s+1}+A_s$ is hypergeometric, leaving $A_s$ as one
alternating incomplete sum.  On the linear eliminant locus, a collision is
equivalent to one residual equation whenever $(f_0,f_1)\ne(0,0)$; the
separate rank-zero branch $U_0=U_1=0$ is retained.

Naive scalar nonvanishing is false:
$A_3=1023=33\cdot31$ on $(p,s,r)=(31,3,5)$, and
$\Delta_4=577280=14080\cdot41$ on $(41,4,7)$.  These are not gate
collisions.  Root independently verified the telescoper, 1,153 period
normalizations through $p\le401$, and both counterexamples; two isolated
full replays are byte-identical.  Ledger:
`results/item251_j2_exceptional_period_hashes.sha256` (SHA-256
`1888b488bfbb3e2a056902ace14abca4b2e131610395f0b7d3a361d7a1411b16`).
The 1,763,142-row scalar scan through $p\le20000$ is EXACT FINITE ONLY.
All-prime or sufficient zero-density control of the second residual remains
OPEN.  Item 251 books zero rate; Route 1 remains ACTIVE and Route 2 QUEUED.

## Item 252: one half-binomial period and a scalar degree barrier (2026-08-31)

Put


$$
m=s-1,\qquad d=r+2,\qquad
 h_j=\frac{(1/2)_j}{j!2^j},\qquad H_m=\sum_{j=0}^m h_j,
$$


and


$$
P_d(m)=\sum_{k=1}^d2^{-k}\frac{(m+1/2)_k}{(1/2)_k}.
$$


Using $3s-1=(p-1)/2-d$, exact Frobenius reduction and finite contiguous
descent give


$$
A_s=(-1)^m\left\{\left(\frac2p\right)
 [H_m-h_mP_d(m)]-1\right\}\pmod p.
$$


The fixed-$r$ shifts have therefore been removed; one universal moving
prefix $H_m$ remains.  Every denominator is a unit because
$2d-1=p-6s<p$ and $2m+2d-1=p-4s-2<p$, with every finite endpoint retained.

A scalar hypergeometric antidifference would require


$$
\frac{2x+1}{4x+4}R(x+1)-R(x)=1.
$$


There is no rational solution in characteristic zero.  In characteristic
$p\ge5$, the zero $-1/2$ and pole $-1$ lie $(p-1)/2$ translation
steps apart.  Pole cancellation forces at least that many poles in every
reduced denominator of a solution, if one exists; nonexceptional pole orbits
cost $p$ poles.  Thus no uniformly fixed-degree scalar rational telescoper
can remove $H_m$.

This is a scoped method barrier, not a nonvanishing theorem.  Phase-only,
higher-rank Cartier, and nonlinear relations remain OPEN.  Root independently
checked 357 exact contiguous identities, all 1,153 rows through $p\le401$,
the pole-orbit proof, and two isolated portable replays.  The package census
of 2,440 rows through $p\le601$, including eight $A_s$-zeros, is EXACT
FINITE ONLY.  Ledger: `results/item252_diagonal_modp_hashes.sha256`
(SHA-256 `1e281d9b86b668fdeef3eca216f0a2ee05ebe81908eea3851dda954c761cea03`).
Item 252 books zero rate; Route 1 remains ACTIVE and Route 2 QUEUED.

## Item 253: actual-phase diagonal, terminal invariant, and six-section barrier (2026-08-31)

Put $\delta=r+4$, $m=s-1$, and $n=3m+\delta=(p-1)/2$.  The universal
prefix from Item 252 is congruent on every actual row to



$$
K_{\delta,m}=\sum_{k=0}^m\binom{3m+\delta}{k}\left(-\frac12\right)^k.
$$



For the exact integer $B_{\delta,m}=2^{3m+\delta}K_{\delta,m}-1$, the
increment $B_{\delta,m+1}-B_{\delta,m}$ is one explicit hypergeometric
term with quadratic



$$
Q_\delta(m)=28m^2+(21\delta+25)m+4\delta^2+9\delta+5.
$$



All non-$Q$ factors are $p$-units, and exact multiples-of-$p$ identities
give



$$
\Delta_{\delta,m}\equiv0\pmod p
 \iff p\mid 2m^2-m+3
 \iff p\mid 2r^2+21r+81.
$$



This is an all-prime fixed-$r$ theorem for the terminal increment only.
At $p=43$, the prefix vanishes while every increment is nonzero; at
$p=127$, the terminal increment vanishes while the prefix is $109$.
The exact Cartier polynomial determines six residue-class sums, but the
ambient kernel $z^m-z^{m+6}$ proves that sixth-root values alone cannot
isolate the target coefficient.

Root reproduced the phase and terminal identities on 1,153 rows through
$p\le401$, checked the Cartier identity through $p\le101$, and obtained
two byte-identical isolated replays.  The 2,440-row census through
$p\le601$ is EXACT FINITE ONLY.  Ledger:
`results/item253_half_binomial_phase_hashes.sha256` (SHA-256
`2278812ad0260bdcecea68359407dbffa4f68105b38affac076106723d5af703`).
The incomplete prefix and the actual gate collision remain OPEN.  Item 253
books zero rate; Route 1 remains ACTIVE and Route 2 remains QUEUED.

## Item 254: arithmetic forms and the numerator container (2026-08-31)

The remaining prefix $H_m$ now has exact finite-field Mellin and
Teichmuller/Greene representations.  Its Jacobi component is the explicit
unit $n-m+1$, but the other component retains a full-order cutoff character.
Splitting $p\bmod6$ localizes the unweighted factor to genus-one curves; for
$p\equiv5\pmod6$ the curve is birational to $Y^2=X^3-1/2$ and its
unweighted trace is zero, while the required punctured rational weight remains.
Thus the trace calculation does not evaluate the prefix.

The same prefix has an exact incomplete-beta form and a fixed-$r$ shift from
the natural $\lfloor p/6\rfloor$ cutoff.  In lowest terms,



$$
H_m=\frac{N_m}{2^{3m-s_2(m)}},\qquad
 \sum_{p\mid N_m}\log p<\left(3m-s_2(m)+\frac12\right)\log2.
$$



The normalized ceiling tends to $(\log2)/2$ per $6m$, which is positive
and larger than the raw ordinary-$j=2$ cell capacity; it is therefore not a
zero-rate theorem.  Exact prefix zeros occur at $p=43$ and $p=47$.
Root independently checked 1,153 beta/cutoff rows, 85 character rows, and 257
numerator valuations.  Ledger:
`results/item254_half_binomial_arithmetic_hashes.sha256` (SHA-256
`617a54d939170fe025a927f45262df7f06003029b1493925188ca3ef07317b28`).

## Items 255--256: reciprocal beta resonance through the first jet (2026-08-31)

Item 255 proves that $H_m=0$ is equivalent to vanishing of one finite
incomplete-beta moment.  Endpoint-retaining contiguous iteration and exact
denominator complementation pair the target parameter $-2$ with $-1/2$.
The resulting reciprocal two-moment matrix has rank one on every actual row;
its first determinant digit is



$$
2\sum_{t=0}^m\frac1{2m+d+t}.
$$



This harmonic interval vanishes on the admissible row $(p,r,s)=(23,1,3)$,
where the exact determinant numerator has $23$-adic valuation two.

Item 256 adjoins the squared-denominator jet and proves the correct
mod-$p^2$ reflection and differentiated contiguous recurrence.  The
augmented four-by-four matrix has rank exactly two on every actual row, with
compatible affine endpoints, so the first jet gives no independent condition
on the target moment or the Item-251 affine gate.  Root independently checked
both rank theorems on 1,153 rows; all larger counts are EXACT FINITE ONLY.
Ledgers: `results/item255_incomplete_beta_orbit_hashes.sha256` (SHA-256
`caf00928644667b57874fae1d11237b54d03aa5af5bca4fa53f798a1a21756a2`)
and `results/item256_beta_first_jet_hashes.sha256` (SHA-256
`f5033ac88e0fe67083d0878b32e9a4556693a16733a9cb8f0bdcead1824588d5`).
Items 254--256 book zero rate.  Route 1 remains ACTIVE and Route 2 remains
QUEUED.

## Item 257: global row reindex and the numerator-height ceiling (2026-08-31)

The ordinary-$j=2$ cell has been reindexed globally by
$4M+1=5p-2s$, with actual primes exactly in
$(4M+3)/5\le p\le6M/7$.  The apparent congruence restrictions are automatic
on actual rows and supply no density saving.  For
$H_k=N_k/2^{3k-s_2(k)}$, both the individual numerator bound and the
aggregate product/lcm containers are too large to beat the raw cell capacity
$2/35$; moreover, the Item-251 condition is affine rather than $H_k=0$.
Thus height plus residue filtering cannot prove the needed zero-rate theorem.
The finite census is EXACT FINITE ONLY.  Ledger:
`results/item257_j2_weighted_numerator_hashes.sha256` (SHA-256
`2c52b6e5af9d7508084718bdf53cc13994e5f1b0dc3c37fa879d732b7cc4b28b`).

## Items 258--259: second jet and the all-finite-jet theorem (2026-08-31)

Item 258 proves exact second-jet reflection and contiguous transfer, including
all affine endpoints.  The augmented six-by-six system has rank exactly three
on every actual row.  Item 259 replaces order-by-order study with the formal
resolvent $\mathscr M_q(C;z)$ and proves that, at every finite Hasse level,
the reciprocal rows remain the same rank-one relation module.  Consequently
the entire same-parameter denominator-jet tower is resonant: no finite jet
adds an independent target condition.  This is the requested global no-go for
that tower, not a no-go for Route 1.

Root independently reproduced the rank-three rows and the all-jet functional
identities; Item 259 also passed the sole sub-agent audit.  Ledgers:
`results/item258_beta_second_jet_hashes.sha256` (SHA-256
`15544afd5ecc44df8342cc2f446c04f44643afb9127592894af690210ba4d671`)
and `results/item259_all_jet_resolvent_hashes.sha256` (SHA-256
`26707689707ed235e26c699adfbb992951cc760fd8fdb4da12bae273fd0ff399`).

## Items 260--261: punctured elliptic normal forms (2026-08-31)

Both residue classes modulo six now have exact Hermite reductions on the
elliptic curve $Y^2=X^3-1/2$, with the finite-field endpoint contribution
retained.  The surviving prefix reduces to a second-kind coordinate and a
logarithmic coordinate with nonzero puncture residues.  In the
$p\equiv1\pmod6$ class, the full Item-251 affine gate reduces to this same
pair.  Compact or ordinary-trace cohomology has zero residues and therefore
cannot determine the logarithmic class.  Exact zeros at $p=47$ and at
$p=43,193,241$ also rule out universal prefix nonvanishing.

Root independently checked the Hermite identities, endpoint corrections,
normal forms, gate reductions, and witnesses.  Every bounded count is EXACT
FINITE ONLY.  Ledgers:
`results/item260_p5_punctured_cohomology_hashes.sha256` (SHA-256
`910e7a7d00dd1163823461dfcd8fef9b4795ad516ebd20d5e90e2b6d088b6578`)
and `results/item261_p1_punctured_cohomology_hashes.sha256` (SHA-256
`f06a71ebc7fcfa67af9a27bfefd946ef6366e78f4ede3b79b4b0c382d4b5dcfd`).
Items 257--261 book zero rate.  Route 1 remains ACTIVE and Route 2 remains
QUEUED.

## Item 262: arithmetic of the $p\equiv5\pmod6$ boundary coefficient (2026-08-31)

The fixed cutoff coefficient $K_\delta$ has an exact minimal order-two
recurrence, a hypergeometric generating function, exact $2$- and $3$-adic
information, linear fixed-ray height, and a large-prime numerator-gcd
restriction.  But $K_\delta$-numerator divisibility is neither necessary nor
sufficient for the prefix zero, as exact $p=47$ and $p=59$ rows show.  The
full Item-251 gate still retains $(H_q,h_q)$, and the fixed-ray height sums to
$O(M^2)$, not a linear saving.

Root independently checked 127 recurrence/valuation/support rows, 125 gcd
instances, 605 actual phase rows, and 2,420 localization equalities.  Every
bounded count is EXACT FINITE ONLY.  Ledgers:
`results/item262_p5_boundary_coefficient_hashes.sha256` and
`results/item262_root_audit_hashes.sha256`.  Item 262 books zero rate.

## Item 263: exact punctured Cartier module and endpoint non-descent (2026-08-31)

The five-dimensional odd part of $H^1(E\setminus D)$ now has an exact
Cartier matrix in both prime classes.  Scalar trace and determinant invariants
do not see $H_q$; the noncompact extension entry that sees it is precisely
the original moving prefix.  The finite endpoint functional is nonzero on
exact differentials in every actual phase, so even the order-two class
relation in the $p\equiv5\pmod6$ case does not descend to a new finite
period relation.  Reattaching the endpoints recovers only the old pair
$(H_q,h_q)$, and the full Item-251 affine gate remains unchanged.

Root independently rebuilt the Cartier-selected quotient coefficients,
compact coefficients, endpoint identities, 1,153 actual cutoff rows, and the
named witnesses through $p\le401$.  The package replay is byte-identical;
all bounded rows are EXACT FINITE ONLY.  Ledger:
`results/item263_punctured_frobenius_hashes.sha256`; root audit:
`results/item263_root_audit_hashes.sha256`.  Item 263 books zero rate.  Route 1
remains ACTIVE and Route 2 remains QUEUED.

## Item 264: global $j=1$ support and the inherited-height ceiling (2026-08-31)

The actual $j=1$ rows are exactly the primes in
$(4M+3)/3\le p\le(3M-1)/2$, giving raw mass $1/36$ per $6M$.  A full
collision contributes a square divisor to both fixed gate integers, but the
inherited Cauchy estimate is much weaker than the raw interval.  The same
componentwise estimate cannot be improved merely by bounded-degree
recombination; a separately proved low-height cancellation remains possible.
Exact seed and Wronskian witnesses are not full-gate collisions, and the only
all-prime fixed-edge exclusion has zero linear mass.

Root independently verified 4,631 row bijections, 1,000 adjacent-interval
checks, the three gate witnesses, and the height constants without performing
a collision scan.  A bare carriage return and an initially overbroad scope
claim were repaired before resealing.  Ledgers:
`results/item264_j1_weighted_gate_hashes.sha256` and
`results/item264_root_audit_hashes.sha256`.  Item 264 books zero rate.

## Item 265: beta squarefull capacity and the high-singleton barrier (2026-08-31)

For the fixed beta denominator
$q_0=q_1=1,\ q_N=(4N-2)q_{N-1}+q_{N-2}$, Item 265 proves the exact
two-copy overlap normalization.  After removing the clearing divisor
$D_m$, the residual matching quotient divides
$(q_N/\gcd(q_N,D_m))^2$, so squarefull depth on those same primes cannot
be added again to the optimistic two-copy reservoir.

Writing $E(n)=n/\operatorname{rad}(n)$, one has
$E(n)\mid\operatorname{sqfull}(n)\mid E(n)^2$.  Thus the desired
squarefull little-oh theorem is exactly an excess-valuation theorem.  The
low prime-power levels $p^a\le N$ have average $o(N\log N)$ per term,
but the complementary $p^a>N$ singleton tail remains uncontrolled.
Pairwise gcds measure reuse and are provably blind to that tail.  The current
uniform height bound stays on the full $N\log N$ saddle scale, so it gives
no capacity reduction.

Root independently replayed the sequence, reverse-Bessel, transfer/gcd,
overlap, powerful-part, and singleton-envelope identities.  The canonical
replay is byte-identical and every dependency hash matches.  All bounded
checks are EXACT FINITE ONLY; no exceptional-prime scan was performed.
Ledgers: `results/item265_beta_squarefull_capacity_hashes.sha256` and
`results/item265_root_audit_hashes.sha256`.  Item 265 books zero rate and
zero capacity reduction.

### Targeted literature checkpoint after Item 265

The adjacent primary literature on incomplete $A$-hypergeometric systems,
Dwork Frobenius, central-binomial congruences, Picard 1-motives, Frobenius
large sieves, and elliptic Wieferich phenomena has been triaged in
sources/route1_targeted_literature_note_items259_265.md.  It supplies the
right structural frameworks but no theorem presently applies directly to
the actual moving affine gate or the beta high-singleton tail.  This is a
targeted search result, not a novelty claim or a proof of impossibility.

## Item 266: stable off-ray capacity and the inherited-height barrier (2026-08-31)

The stable rank-one off-ray rows now have an exact global description.  Apart
from the fixed primes below $11$, the two phase families are



$$
(8j+7)p\ge16M,\qquad(5j+4)p\le10M+1
$$



and



$$
(4j+3)p\ge8M,\qquad(3j+2)p\le6M.
$$



Their total raw weight is $0.239111014698\ldots$ per $M$, or
$0.039851835783\ldots$ per $6M$.  The finite-$j$ far subcell
$b\ge M/5$ alone has raw ceiling $0.020905487992\ldots$ per $6M$,
which still exceeds the scoped optimistic gap $0.019632983669\ldots$.
Thus removing only thin or slowly growing layers cannot close this branch.

The exact moving-$b$ eliminants retain an actual witness at
$(M,s,p,j,q,b,r)=(2249,299,2399,1,1,900,3)$.  The inherited layer-divisor
and numerator-height bounds cannot improve the raw ceiling: a mock fixed
sequence consistent with those containers saturates the far rows on a
geometric subsequence.  This is a sharply scoped information barrier, not a
no-go theorem for the actual hypergeometric family.  Item 149 already books
the first rank-one copy, and Item 266 proves neither positive mass for the
candidate extra copy nor an upper bound below the gap.

Root independently reconstructed 3,003 stable rows through $M\le360$, the
exact far coefficient, gap comparison, full witness factorization, and all
declared package hashes.  No common-zero scan was performed; bounded rows are
EXACT FINITE ONLY.  Ledgers:
`results/item266_far_offray_weighted_barrier_hashes.sha256` and
`results/item266_root_audit_hashes.sha256`.  Item 266 books zero rate and zero
capacity reduction.  Route 1 remains ACTIVE and Route 2 remains QUEUED.

## Item 267: fixed Picard 1-motive recognition and conjugacy no-go (2026-08-31)

The punctured $j=2$ period now has a fixed global home.  For
$U=E\setminus D$, where $E:Y^2=X^3-1/2$ and $D=E\cap\{X^3=1\}$,
the five-dimensional odd de Rham module is the realization of the Picard
1-motive



$$
M_U^-=[L^-\longrightarrow E],\qquad
 d_k=[P_k]-[-P_k]\longmapsto2P_k .
$$



The pair $(H_q,h_q)$, every cutoff $H_q-K_\delta h_q$, and the full
affine period $H_q-D_rh_q$ are exact Cartier matrix coefficients of this
one fixed mixed object, with a row-dependent input vector.

The residue direction of the logarithmic class is not an algebraic-unit
direction.  The complete odd unit kernel is
$\mathbf Z(d_0+d_1+d_2)$, whereas the target residue character is
$(1,\zeta^2,\zeta)$.  Its point maps to $P=(2,2)$ on
$y^2=x^3-4$; since $3P=(106/9,1090/27)$, Nagell--Lutz proves that
$P$ is non-torsion.  The target is therefore a genuine elliptic
third-kind direction.

This positive recognition does not provide the needed arithmetic invariant.
In the $p\equiv5\pmod6$ phase a $p$-dependent frame change puts the
abstract Cartier module into a normal form independent of $H_q,h_q$; in
the $p\equiv1\pmod6$ phase the relevant extension splits off resonance.
The finite endpoint still does not descend, so the canonical fixed-frame
period survives while scalar and conjugacy invariants remain blind to it.
No equivalence with an elliptic-Wieferich or $p$-adic elliptic-logarithm
condition is claimed.

Root independently replayed the sealed checker byte for byte and separately
verified 95 prime phases, 1,834 cutoff identities, 95 endpoint identities,
the residue/unit algebra, and the non-torsion group law.  No exceptional-zero
scan was performed.  Item 267 books zero rate and zero capacity reduction;
the fixed-Frobenius-divisor and weighted-density problem remains OPEN.

## Item 268: exact adjacent off-ray relation and nonpropagation (2026-08-31)

The capacity-relevant off-ray pair has a genuine all-$s$ contiguous
identity.  With



$$
\begin{aligned}
a&=75s^2+100s+3,& b_0&=6s^2+11s+4,\\
c&=575s^2+1525s+998,& d&=46s^2+123s+81,
\end{aligned}
$$



one has



$$
\begin{aligned}
&16(s+1)(2s+3)(ag_0(s)-20b_0g_1(s))\\
&\quad+3(3s+4)(3s+5)(cg_0(s+1)-20dg_1(s+1))=0.
\end{aligned}
$$



An exact constant-term telescoper proves this identity for every $s$.
The phase step is $b\mapsto b-5$, $r\mapsto r+3\pmod4$, with an
actual cross-$j$ realization.  It covers the full Item-266 far coefficient
$1139587/9085230$ per $M$, apart from a zero-rate boundary.

The relation does not propagate the common gate.  If
$g_0(s)=g_1(s)=0\pmod p$, it forces only one adjacent line.  At the exact
$p=2399$ witness, the adjacent pair is
$(g_0(300),g_1(300))=(2105,1694)\ne(0,0)$, satisfying only
$966g_0+128g_1=0$.  The adjacent coefficient resultant is
$1564=2^2\cdot17\cdot23$.

The displayed relation is unique only within the explicitly declared
four-polynomial degree-$\le4$ adjacent ansatz.  Its transported line is
dependent on a current-layer combination and retains exponential height, so
it gives no new divisor copy or weighted ceiling.  Root independently rebuilt
82 integer sequence rows by two formulas, verified 81 identity rows, the
rank-19 uniqueness matrix, 1,483 far phase rows, and the mandatory witness.
All bounded checks are EXACT FINITE ONLY.  Item 268 books zero rate and leaves
the far raw ceiling unchanged.

## Item 269: fixed-divisor admission and the moving-slope obstruction (2026-08-31)

The complete ordinary-$j=2$ collision is now written exactly as the fixed
bilinear incidence



$$
R_{r,s}(1,H_q,h_q)^{\mathsf T}=0
$$



with two rows, so it retains both affine gates and the separate rank-zero
branch.  This is an exact representation, but $R_{r,s}$ is external moving
row data rather than Frobenius data of the fixed Item-267 motive.

The full slopes have a decisive exact arithmetic feature.  If
$D_\delta=A_\delta/B_\delta$ is reduced, then



$$
v_3(A_\delta)=0,\qquad
v_3(B_\delta)=L+v_3((2L-1)!!),
$$



where $L=3\delta$ in the $p\equiv5\pmod6$ phase and
$L=3\delta-2$ in the companion phase.  The slopes are therefore pairwise
distinct.  More strongly, no nonzero fixed polynomial
$P(\delta,D_\delta)$ can vanish on an unbounded set of actual cutoffs:
the rational-root denominator bound is $O(\log\delta)$, while the exact
$3$-adic denominator grows linearly.

The sealed Cartier conjugacy class also cannot detect the framed period:
its normal form erases the relevant coefficient, and pulling the fixed motive
back to a row line gives trivial row monodromy.  Hence the present
fixed-algebraic-divisor and conjugacy-stable large-sieve admission fails.
This does not rule out a genuinely new auxiliary lisse, crystalline, or
autonomous dynamical system.

Root independently reconstructed 35 reduced slopes, all strict valuation
steps, 12 normal-form parameter sets, 16 full-incidence identities, and the
four exact $p=47$ row cutoffs.  No exceptional-prime scan was performed.
Item 269 books zero rate, leaves the raw $2/35$-per-$M$ cell unchanged,
and moves the live question to new auxiliary dynamics.

## Item 270: the all-shift contiguous module is globally rank three (2026-08-31)

The full linear shift tower of the stable off-ray pair is now settled.  Exact
twisted-de-Rham reduction gives the minimal state



$$
X_s=(g_0(s),g_1(s),g_0(s+1))^{\mathsf T}
$$



of rank three over $\mathbb Q(s)$.  The infinity audit is essential:
retaining certificate numerator degrees $12$ and $13$ gives the two
relations needed for an exact invertible $3\times3$ transfer; the earlier
degree-$11$ truncation has certified nullity zero.

A current common gate leaves $X_s=(0,0,u)^{\mathsf T}$.  Every fixed or
uniformly bounded forward, and every defined backward, shift window is an
invertible image of this same line.  It therefore adds no
collision-forced scalar condition.  The actual $p=2399$ row has
$u=2105\ne0$, so the surviving line is occupied by the actual family.
All determinant and chart exceptions lie in explicit fixed-$M$ containers
of total logarithmic weight $O_L(\log M)$.

Root independently recomputed the two three-layer syzygies, 25 transfers and
determinants, 2,772 container identities, the far coefficient, and the
nonpropagation witness.  Item 270 closes every fixed or uniformly bounded
linear contiguous window as a source of extra codimension.  Unbounded,
nonlinear, and external cross-parameter mechanisms remain open.  The far raw
ceiling and Route-1 booking are unchanged.

## Item 271: exact rank-three dynamics for the moving $j=2$ slope (2026-08-31)

For each prime phase, the actual odd slopes satisfy an exact degree-seven
order-two recurrence.  With
$\Delta_\delta=D_{\delta+2}-D_\delta$, it reduces to



$$
\Delta_{\delta+2}=\rho_e(\delta)\Delta_\delta,\qquad
 T_e(\delta,D,\Delta)
 =(\delta+2,D+\Delta,\rho_e(\delta)\Delta).
$$



Thus $D_\delta$ has a genuine rank-three autonomous rational
translation-difference realization.  An exact WZ certificate proves the
recurrence, including both moving-upper-bound defects; it is not fitted from
finite data.  Actual rows at $(p,e,\delta)=(167,5,7)$ and
$(241,1,11)$ meet the forward pole divisor modulo $p$, so the rational
chart is not regular on every actual reduction.

Translation by two is not arithmetic Frobenius, and this dynamics updates
only the slope.  It does not update every entry of the complete two-row
matrix $R_{r,s}$, construct a compatible lisse/crystalline family, or
prove monodromy or local density.  Root's independent replay reproduced 47
recurrence and orbit rows, both pole witnesses, and the iterate-factor
audit.  Item 271 books zero rate and leaves the raw $2/35$-per-$M$ cell
unchanged.

The booked rate therefore remains
$r_1=0.1365141682948128184504238226\ldots$, with deficit
$1.0196329836694317938803064012\ldots$ per $6m$.  Route 1 remains
ACTIVE and Route 2 remains QUEUED.

## Item 272: partial complete-row dynamics and the residual hard block (2026-08-31)

The ordinary fixed-$j=2$ row has now been tested under its natural
same-prime shift



$$
\delta\mapsto\delta+2,\qquad r\mapsto r+6,\qquad
 s\mapsto s-2.
$$



Seven exact coordinates close under one rational translation-difference
module:



$$
(1,c,B_s,\kappa_r,\tau_{r,s},D_\delta,\Delta_\delta),
 \qquad \Delta_\delta=D_{\delta+2}-D_\delta.
$$



The scalar factors are obtained by direct factorial and Pochhammer
cancellation, while the $(D,\Delta)$ block is Item 271's proved
rank-three update.  All new scalar denominators are actual $p$-units on
the forward range.  The slope block retains its separately proved actual
pole rows.

The complete matrix still depends on



$$
W=(f_0,f_1,U_0,U_1),
$$



or its six coefficient refinement
$(f_0,f_1,P_0^\flat,P_1^\flat,H_0^\flat,H_1^\flat)$.  In both phases,
none of these six sequences satisfies a nonzero first-order rational
relation whose two polynomial coefficients have degree at most seven.
This is an exact scoped no-go: each of the twelve $27\times16$ evaluation
matrices has rank 16 over two certificate primes, with all evaluated
denominators units.  The literal Item-250 affine basis also grows with
$r$ and is not invariant under the shift.

Higher-degree, higher-rank, or creative-telescoping compression of $W$
remains OPEN.  No complete-row lisse/crystalline realization or density
theorem follows.  Root reproduced the certificate byte for byte, checked all
six package hashes and six frozen dependencies, and audited the normalization.
Item 272 retains $2/35$ per $M$, equivalently $1/105$ per $6M$,
and books zero rate.

## Item 273: fixed $j=1$ incidence and the scalar-divisor barrier (2026-08-31)

The full fixed-$j=1$ gate is now an exact rank-two incidence on the
eight-coordinate endpoint state



$$
Y=(S_T,S_E),\qquad
 S_n=(f_{n+1},f_n,f_{n-1},f_{n-2})^{\mathsf T}.
$$



The logarithmic coefficients satisfy an exact rank-four tail recurrence.
Its forcing term vanishes throughout the actual endpoint corridor, whose
transfer is homogeneous, invertible, and free of mod-$p$ pivots.  The
kernel identities



$$
F_{h+1,s}=(1-z)^2F_{h,s},\qquad
 F_{h,s+1}=(1+z^2)^2F_{h,s}
$$



therefore give a rational parameter realization of rank at most eight.
Four exact shift determinants were proved by a $25\times25$ rational grid
together with a cleared bidegree bound of 24.  Every fixed-window singular
factor lies in a fixed-$M$ integer container of total logarithmic weight
$O_L(\log M)$.

On the generic reduced rank-two chart, however, the collision ideal is
generated by two independent linear forms in four graph-state variables.
It has height two and is nonprincipal, so no single polynomial hypersurface
has exactly the collision zero set on that algebraically closed chart.  This
does not exclude finite-field norms, exterior-square or determinantal
encodings, sheaves, or a weighted theorem for a larger necessary divisor.

Root independently replayed the checker byte for byte, verified all seven
package hashes and five dependencies, and checked the repaired report's
control bytes and TeX delimiters.  The rank census through $p\le1000$ is
EXACT FINITE ONLY and is not extrapolated.  Item 273 leaves the fixed-$j=1$
ceiling at $1/36$ per $6M$, books zero rate, and moves the next admission
test to exterior-square/determinantal arithmetic.

The only booked rate remains
$r_1=0.1365141682948128184504238226\ldots$, and the rigorous deficit
remains $1.0196329836694317938803064012\ldots$ per $6m$.  Route 1 is
ACTIVE; Route 2 is QUEUED.

## Item 274: fixed reverse-Bessel determinant singleton no-go

Item 274 tests whether the remaining beta high-singleton valuation can be
controlled by fixed index shifts, denominator jets, ordinary Wronskians, or
the exponential Padé determinant.  For



$$
Z_{i,j}(N)=2^jA_{N+i}^{(j)}(-1),
$$



the exact differential identity gives



$$
Z_{i,j+1}=Z_{i,j}+Z_{i-1,j}-2jZ_{i-1,j-1}.
$$



Every fixed jet and shift therefore reduces over $\mathbb Z[N]$ to
$(q_N,q_{N+1})$.  Every fixed-size determinant in the declared class has
the exact homogeneous expansion



$$
\mathscr D_N=\sum_{k=0}^s C_k(N)q_N^kq_{N+1}^{s-k},
 \qquad \deg C_k\le s(d+L+J).
$$



At an isolated deep prime power, the first nonzero coefficient gives a sharp
dichotomy: $k=0$ sees only a fixed-polynomial $O(\log N)$ contribution,
whereas $k\ge1$ contains $q_N^k$ and any nonzero integer value already
has height at least $kN\log N+O(N)$.  The Padé Wronskian is exactly a unit
modulo the full $q_N$.  Item 265's overlap normalization also survives:
the forced branch remains divisible by
$(q_N/\gcd(q_N,D_m))^k$, so it is not fresh capacity.

Root independently reproduced the certificate byte for byte, verified six
package hashes and six frozen dependencies, parsed five JSON files, and
checked the repaired report's controls and balanced delimiters.  This is a
PROVED SCOPED NO-GO for fixed-length determinant height arguments only.
Growing-length auxiliaries, direct prime-power bounds, and uniform
approximation of the canonical $p$-adic index zeros remain OPEN.  Item 274
books zero rate and zero beta-capacity reduction; Route 1 remains ACTIVE and
Route 2 remains QUEUED.

## Item 275: fixed flag incidence and non-flat Plücker line

On the rank-two fixed-$j=1$ chart, the signed maximal minors of the gate
matrix give the kernel Plücker vector



$$
K=(\Delta_{34},-\Delta_{24},\Delta_{23},
    \Delta_{14},-\Delta_{13},\Delta_{12}).
$$



It lies on $\operatorname{Gr}(2,4)\subset\mathbb P^5$, and the original
collision is exactly the fixed flag incidence $x\wedge K=0$.  Although
this has four displayed bilinear coordinates, only two are independent on a
nonzero decomposable plane.  It is therefore a uniform codimension-two
determinantal condition, not a hypersurface divisor.

The exact rank-four parameter transports induce a rank-six exterior-square
module satisfying $\det(\wedge^2U)=\det(U)^3$, with no new singular
support.  However, exact stacked-plane determinants prove that the natural
kernel line is non-horizontal under both $h$- and $s$-transport and under
an actual fixed-$M$ step.  The latter compares primes $29$ and $31$, so
it is not misused as a same-field collision exclusion.  Rank-one, rank-zero,
and $x=0$ branches are retained separately.

Root's independent replay is byte-identical, and all seven package hashes,
three dependencies, six JSON files, controls, and delimiters pass.  Item 275
closes the natural flat Plücker-eigenline shortcut only; enlarged modules,
different arithmetic connections, and weighted incidence remain OPEN.  The
raw $1/36$-per-$6M$ ceiling, Item-149 overlap, booked rate, and deficit
are unchanged.  Route 1 remains ACTIVE and Route 2 remains QUEUED.

## Item 276: one growing beta Casoratian transports depth

For the exact gap continuant $P_h(n)$ and primitive scalar Casoratian
$\mathcal C_h(n)$, every level $p^s\mid q_n$ satisfies



$$
p^s\mid\mathcal C_h(n)
 \Longleftrightarrow p^s\mid P_h(n)
 \Longleftrightarrow p^s\mid q_{n+h}.
$$



Thus a single growing two-state minor reaches an in-window singleton level
only by finding a second zero of the same level.  Exact continuant bounds show
that its residual height is $O(n)$ exactly when
$h=O(n/\log n)$; the universal anti-period gap $h=p^a$ for a high level
$p^a>N$ already costs at least $N\log(4N+6)$.  The same equivalence holds
after Item-265 overlap normalization.

Root's independent replay is byte-identical, with six package hashes, six
dependencies, five JSON parses, and a clean format audit.  This closes one
primitive growing minor only.  Products, growing collections, arbitrary block
determinants, and short-return arithmetic remain OPEN.  Item 276 books zero.

## Item 277: neighboring fixed-$j=1$ collisions have zero cluster mass

Neighboring fixed-$M$ rows have primes $p$ and $p+2$.  A double
collision yields only the already known divisibility
$[p(p+2)]^2\mid\gcd(C_0,C_1)$.  CRT splits the mixed state conditions into
separate kernels over $\mathbb F_p$ and $\mathbb F_{p+2}$, so a nonzero
rational stacked determinant produces no product-field state divisor.

The possible neighbor edges are twin-prime positions.  The classical
Brun/Selberg upper-bound sieve gives total endpoint logarithmic weight
$O(M/\log M)=o(M)$; even perfect exclusion of every neighbor pair has zero
linear capacity.  Root reproduced the exact certificate, verified seven
package hashes and five dependencies, parsed six JSON files, and checked the
repaired boundary and delimiters.  Isolated collisions remain OPEN.  Item 277
leaves the $1/36$-per-$6M$ ceiling unchanged and books zero.  The booked
rate and deficit remain unchanged; Route 1 is ACTIVE and Route 2 is QUEUED.

## Completed Item 243: actual-family order-six gauge closure

The formerly open actual-family gauge bridge is now proved for every
$h\ge1$ with $3\nmid h$:



$$
c_h^*=\mathcal R_hE_h^*.
$$



For each residue class $h=3n+r$, the transported defect satisfies an exact
order-six recurrence.  Its cleared coordinate degree is at most 2240, so
2241 consecutive regular exact specializations prove the ambient transported
relation.  The forward cofactor has degree at most 1806; its Newton
coefficients are all nonpositive and its constant coefficient is strictly
negative in both residues, proving nonvanishing for every $n\ge0$.  Twelve
defect initials and six distinct gauge initials finish propagation.

Root reproduced both the final closure certificate and the initial-layer
certificate byte for byte, verified 38 manifest files, six dependencies, and
23 JSON files, and audited controls and delimiters.  The original one-step
ambient defect is nonzero, so the transported closure is essential.  The
result proves no prime nonvanishing, weighted density, divisor, or positive
linear mass; it books zero and leaves Route 1 ACTIVE.

## Item 278: bounded beta portfolios have a sharp height-depth barrier

For a weighted product of primitive gap continuants, put
$L=\sum_iw_i(h_i-1)$ and $H=\log\prod_iP_{h_i}(n)^{w_i}$.  Then



$$
L\log(4n+6)\le H\le L\log(4(n+L+1)),
$$



so linear height is equivalent to $L=O(n/\log n)$.  The product valuation
is exactly the weighted sum of the truncated return depths, including after
the Item-265 clearing reservoir is removed.  At fixed total multiplicity
$K$, full depth forces one short return at level
$p^{\lceil s/K\rceil}$.  The canonical anti-period optimizer shows that
linear height reaches only $s\log p=O_K(\log n)$.

Root's replay is byte-identical and all five package hashes, seven
dependencies, four JSON files, controls, and delimiters pass.  This closes
bounded-multiplicity canonical products only.  Actual short returns,
unbounded independent portfolios, sums with cancellation, and growing block
determinants remain OPEN.  Item 278 books zero.

## Item 279: every fixed-diameter non-singleton $j=1$ cluster is zero-rate

For every fixed diameter $D$ and anchored pattern
$J\subset\{0,\ldots,D\}$, the collision rows lie over distinct primes
$p+2j$.  CRT therefore gives a product of local kernel modules.  Every
natural mixed maximal minor vanishes over the product ring even when the
rational gate planes are transverse, and a cluster supplies only the already
known square-radical factor.

The fixed-tuple Selberg upper-bound sieve gives
$O_{D,t}(M/\log^tM)$ clusters of size $t$, hence
$O_{D,t}(M/\log^{t-1}M)=o(M)$ endpoint log weight.  The union of every
non-singleton pattern of diameter at most $D$ is
$O_D(M/\log M)=o(M)$.

Root independently reproduced the certificate, verified six package hashes,
six dependencies, five JSON files, and the report format.  Isolated collision
primes and diameter growing with $M$ remain OPEN.  The raw
$1/36$-per-$6M$ ceiling and booking are unchanged; Route 1 remains ACTIVE
and Route 2 remains QUEUED.

## Item 282: unbounded beta products reduce to one efficient return

For every de-overlapped target $Q\mid q_n/\gcd(q_n,D_m)$, arbitrary finite
weighted product $A=\prod_hP_h(n)^{w_h}$, and corresponding scalar
Casoratian product $D$, Item 282 proves



$$
\gcd(Q,D)=\gcd(Q,A),\qquad
 {\log\gcd(Q,A)\over\log A}
 \le\max_h{\log\gcd(Q,P_h(n))\over\log P_h(n)}.
$$



Thus even unbounded formal powering cannot improve captured depth per unit
height over the best primitive return.  Positive-linear capture at
$O(n)$ height forces one genuine high-efficiency short return.  The exact
unrestricted anti-period optimizer has gap cost $s(p-1)$ for certified
depth $s$, so its capacity is only $O(n/\log n)=o(n)$, uniformly over
odd primes and multi-prime assignments.

Homogeneous sums are separated correctly: a unique least $p$-adic term
cannot add depth, while tied minima can create a genuinely new cancellation
quotient.  Root reproduced the certificate byte for byte and verified five
package hashes, seven dependencies, four JSON files, and the report format.
Actual high-efficiency returns and prime-independent target-cancelling sums
remain OPEN.  Item 282 books zero; Route 1 remains ACTIVE and Route 2 remains
QUEUED.

## Item 281: the isolated $j=1$ Fitting scalar is the target gcd

After removing the squarefree forced Cartier product, the positive generator



$$
g_M=\gcd(\overline C_0(M),\overline C_1(M))
$$



is exactly the specialized Smith/Fitting generator, and an actual $j=1$
prime collides precisely when it divides $g_M$.  This recognizes the
isolated arithmetic target but does not simplify it.  On the generic rank-two
chart, eliminating the state from two linear equations in four variables
produces no parameter resultant.

Quadratic anisotropic norms are locally optimal, but Chebotarev proves that
every finite fixed library of integral homogeneous forms has nonzero
projective zeros at infinitely many actual phase primes.  The normalized
inherited height coefficient is
$H-\kappa=3.99058003744209\ldots>1/6$, so bounded-degree scalar height
does not beat the raw support ceiling.

Root reproduced the certificate byte for byte, verified six package hashes,
eight dependencies, five JSON files, and all report checks.  Parameter-
dependent scalars and weighted bounds for the actual isolated gcd remain
OPEN.  The $1/36$-per-$6M$ ceiling and booking are unchanged.

## Item 283: bounded homogeneous beta sums have zero sum-only rate

For a prime-independent homogeneous residual sum $R=\sum_jc_jA_j$, let
$B=\gcd_j|c_jA_j|$, and let $S$ be the corresponding scalar-Casoratian
sum.  In the fixed-sparsity, fixed-degree moving-gap class of Item 283, every
normalized target $Q$ satisfies



$$
\gcd(Q,S)=\gcd(Q,R),\qquad
 {\gcd(Q,R)\over\gcd(Q,B)}\mid {R\over B}.
$$



The quotient on the left is the entire genuinely additive cancellation
factor.  Its logarithmic height is $O(n)=o(n\log n)$, so it has zero global
Route-1 rate.  A nonzero residual cannot force full $q_n$-divisibility for
all large $n$; an identically zero residual provides no nonzero height
certificate.

Root's replay is byte-identical, with five package hashes, eight dependencies,
four JSON files, and clean format checks.  The Item-282 product baseline,
nonhomogeneous sums, unbounded degree or sparsity, and arbitrary block
determinants remain OPEN.  Item 283 books zero and changes no retained ceiling.

## Item 284: one CRT norm recognizes every $j=1$ candidate gate

Using the complete known candidate-prime set for each $M$, CRT constructs an
integer $1\le d_M<B_M$ which is a quadratic nonresidue at every candidate,
without using the unknown collision set.  The normalized norm then satisfies



$$
p\mid\overline C_0(M)^2-d_M\overline C_1(M)^2
 \quad\Longleftrightarrow\quad
 \text{the full fixed-}j=1\text{ gate collides at }p.
$$



This is an exact one-scalar recognition theorem.  Quantitatively, however,
$\log d_M\le M/6+o(M)$, and the inherited raw norm ratio is
$H/2+1/24=3.20548043938709\ldots$, far above the raw $1/6$-per-$M$
support.  Even a subexponential simultaneous nonresidue would only recover the
already inadequate $H/2$ barrier.

Root reproduced the certificate byte for byte, verified six package hashes,
seven dependencies, five JSON files, and the report format.  A cancellation
or prime-factor localization theorem for the exact norm remains OPEN.  Item
284 leaves the $1/36$-per-$6M$ ceiling unchanged and books zero.

## Item 285: arbitrary sums and the nonhomogeneous boundary unit

The cancellation-divisor theorem does not actually require bounded sparsity
or bounded degree.  For every finite nonzero sum $R=\sum_jT_j$, with
$B=\gcd_j|T_j|$,



$$
{\gcd(Q,R)\over\gcd(Q,B)}\mid {R\over B}.
$$



Thus an explicit normalized bound
$\log(\sum_j|T_j|/B)=O(n)$ closes the entire additive quotient at zero
global rate, even for growing collections.  The product baseline
$\gcd(Q,B)$ remains the separate Item-282 problem.

For unequal Casoratian degrees, the exact residual is $F(u)$ at
$u=-q_{n+1}^2\bmod Q$.  A factorization-independent $O(n)$-height unit
lift, or a monic annihilator with nonzero $O(n)$-height resultant, would
close this additive branch.  The canonical lift and tautological annihilator
cost $2n\log n+O(n)$, while $\mathcal C_1$-homogenization changes the
condition from $F(u)$ to a different $F(1)$ condition.  No admissible
low-height relation is yet known.

Root reproduced the certificate byte for byte, verified six package hashes,
ten frozen dependencies, five JSON files, and clean report formatting.  Item
285 books zero and changes neither the beta ceiling nor the Route-1 ledger.

## Completed Item 280: the gauge localizes the endpoint gate to two integers

The all-$h$ Item-243 gauge now enters the original fixed-$j=1$ collision
exactly.  A division-free combination of the two endpoint equations proves



$$
p\mid\gcd\bigl(N_E(h),N_K(h)\bigr)
$$



for every actual collision, with all rational denominators verified to be
$p$-units.  Here $N_E$ is the phase-eliminant numerator and $N_K$ is
the natural endpoint-scalar numerator.

This is a localization theorem, not yet a density theorem.  It remains open
whether $K_h$ is redundant at every moving prime dividing $N_E(h)$, or
whether the pair creates useful arithmetic codimension.  The available
pointwise height bound sums to $O(H^2\log H)$, far too large for the needed
$o(H)$ prime-log mass.  Root reproduced the certificate byte for byte and
verified six package files, six frozen dependencies, five JSON files, and
clean formatting.  Item 280 books zero.

## Item 286: the standard Frobenius large sieve does not yet apply

The isolated fixed-$j=1$ collision is a diagonal congruence: the same prime
$p$ both varies the residue characteristic and divides the normalized pair.
Kowalski's cited Frobenius large sieve instead works over one fixed
$U/\mathbf F_q$ with auxiliary primes 

$$
\ell\ne\operatorname{char}
\mathbf F_q
$$

, compatible lisse systems, controlled cohomology, monodromy,
cross-$\ell$ independence, and conjugacy-stable local sets.  None of those
inputs follows from the archive's rational translation module, Pluecker
incidence, gcd, or CRT norm.

This is a scoped applicability result, not a theorem that horizontal or
sheaf methods can never work.  A new bridge making collisions visible at
auxiliary primes, together with an applicable horizontal theorem, remains
admissible.  Quantitatively, a collision count
$N(M)=o(M/\log M)$ would imply $o(M)$ log mass and remove the retained
$1/36$-per-$6M$ ceiling.

Root checked the primary theorem, reproduced the certificate byte for byte,
and verified six package files, nine dependencies, six JSON files, and clean
formatting.  No horizontal bound is proved; Item 286 books zero.

## Item 287: recurrence-universal beta annihilators are tautological

For generic beta state variables $X=q_n$, $Y=q_{n+1}$, the exact kernel
after imposing the target and boundary relation is



$$
\ker\bigl(A[X,Y,U]\to A[Y]\bigr)=(X,U+Y^2).
$$



Therefore no positive-degree monic polynomial with polynomial or rational
coefficients in $n$ can annihilate the boundary unit by the recurrence
alone.  Fixed recurrence windows add no formal state coordinate, and every
state-dependent universal relation retains $q_n$ or $q_{n+1}$.  For a
proper target the corresponding kernel is $(Q,U+Y^2)$; a degree-one
annihilator is exactly an integer lift of the boundary unit.

This does not exclude arithmetic special to the seed $q_0=q_1=1$.  The
least-height actual lift and every orbit-specific higher-degree annihilator
remain open.  Root reproduced the certificate byte for byte, checked six
package hashes, six dependencies, five JSON files, and clean formatting.
Item 287 books zero.

## Item 289: fixed-class CRT representative balancing is exhausted

For a fixed simultaneous-nonresidue class $d_0\bmod B$, all integer
representatives $d=d_0+kB$ give the affine norm lattice



$$
x^2-(d_0+kB)y^2.
$$



Item 289 computes its exact nearest-to-zero element.  More importantly, if
$c=\gcd(|x|,|y|)$, every representative is $c^2$ times a cofactor
coprime to the complete candidate product $B$, and the ideal generated by
all representatives is exactly $c^2\mathbf Z$.  Thus the candidate-prime
valuations are independent of representative choice, while powers and
natural same-class products preserve the same divisor-to-height ratio.

Root reproduced the certificate byte for byte and verified six package
hashes, six frozen dependencies, six JSON files, all boundary branches, and
clean report formatting.  The result does not optimize over distinct CRT
classes and proves no actual-family phase or state-gcd bound.  The retained
$1/36$-per-$6M$ ceiling and the Route-1 booking are unchanged.

## Item 288: the second fixed-$j=1$ endpoint condition is globally redundant

Two all-$h$ Gosper telescopings give the fraction-free identity



$$
K_h=c_h\bigl(2d_hY_h-L_hX_h\bigr).
$$



Every factor on the right is localized away from primes larger than
$4h+3$.  Combining this with the completed Item-243 gauge proves, in the
one required direction,



$$
q>4h+3,\quad q\mid N_E(h)\Longrightarrow q\mid N_K(h).
$$



Every actual row prime is at least $4h+9$, so $K_h$ never supplies an
independent condition after $E_h^*$ on the actual family.  Root reproduced
the certificate byte for byte and verified six package files, six frozen
dependencies, seven hash-list entries, five JSON files, every localization
boundary, and clean report formatting.  The surviving $E_h^*$ gate has no
weighted-density theorem, so the fixed-cell ceiling and booking are
unchanged.

## Item 290: the beta degree-one lift is one exact Bessel-seed residue

For the full beta target, the smallest coefficient of a monic linear
annihilator is exactly



$$
\rho_n=\min_{k\in\mathbf Z}|q_{n+1}^2-kq_n|.
$$



Item 290 gives its centered Euclidean formula, the exact descending
arithmetic-progression continued fraction, and an equivalent constrained
cross-determinant.  It also proves a sharp generic-method barrier:
palindromic positive continuant words of arbitrary size have least numerator
square residue $1$.  Therefore generic positivity and continuant growth
cannot decide the actual sequence.

The report now treats the $n=2$ singleton word separately after root caught
that boundary ambiguity.  The repaired certificate replays byte-identically;
five package files, eight dependencies, six hash-list entries, five JSON
files, and report formatting pass.  An upper bound $\log\rho_n=O(n)$ and a
superlinear lower bound are both open for the explicit Bessel seed, while
proper targets and the Item-282 product baseline remain separate.  Item 290
books zero.

## Item 291: the ordinary-$j=2$ hard block has an exact connection-plane form

The lower $B$-tail satisfies $Y_\nu=2d_\nu$ term by term, so
$H_\nu^\flat=-11d_\nu$ and the existing compatibility determinant becomes



$$
D=9c\det(f,b)-11\det(f,d).
$$



The row coordinate $z_1$ is a unit on every actual row.  Therefore the
two-row matrix has rank two exactly when $D\ne0$; all rank-one and rank-zero
charts are classified.  A collision forces $D=0$, but rank drop alone does
not impose the remaining actual-period incidence.  The reconstructed shared
order-three operator is explicitly finite-only and has no symbolic all-$n$
certificate.  Root reproduced the certificate byte for byte, checked six
package files, four dependencies, seven hash-list entries, five JSON files,
and clean formatting.  The retained $1/105$-per-$6M$ ceiling and booking
are unchanged.

## Item 292: the beta least lift is an inhomogeneous $e$-Padé determinant

The exact seed satisfies



$$
q_n=(-1)^ny_n(-2),\qquad p_n=y_n(2),
$$



and $p_n/q_n$ is the regular continued-fraction convergent to $e$ of
zero-based index $3n-2$.  The least lift $\rho_n$ is exactly the minimum
$|\beta|$ in one fixed-Wronskian equation, and every solution has the
centered square-residue form from Item 290.  Its exact $e$-coordinate keeps
a moving inhomogeneous center.  If that center is discarded, fixed-power
homogeneous irrationality estimates yield only polynomial lower scale, far
below $n\log n$.

Root required and verified the reduction of a possibly nonprimitive
$(J,\beta)$ pair before applying the standard rational-approximation bound.
The repaired replay is byte-identical; five package files, four dependencies,
six hash-list entries, five JSON files, and report formatting pass.  The
inhomogeneous/Ostrowski route, the all-$n$ half-bound, proper targets, and
the Item-282 product baseline remain open.  Item 292 books zero.

## Item 293: the sole fixed-$j=1$ gate has an integral recurrence but no generic density theorem

After Item 288 removes $K_h$, Item 293 derives a primitive integral
order-three, step-three recurrence for $E_h^*$.  Its coefficient signs and
six exact initials prove



$$
E_h^*<0\ (h\equiv1\bmod3),\qquad
 E_h^*>0\ (h\equiv2\bmod3).
$$



At primes larger than $4h+3$, the reduced numerator is exactly the relevant
part of $[x^{2h}]C(x)$ for Item 237's fixed algebraic series.  This gives
only individual exponential height and a collective $O(H^2)$ radical
bound.  The comparison sequence $4h+9$ proves rigorously that generic
algebraicity, fixed-order holonomy, integrality, and height alone cannot imply
the required tied-prime $o(H)$ theorem; its prime values have logarithmic
mass $\sim2H$.  Also, $4h+39$ is a forward coefficient factor and equals
the actual prime on $s=6$, so uniform modular propagation fails.

Root reproduced the certificate byte for byte and verified six package
files, eight frozen dependencies, seven hash-list entries, four JSON files,
and clean formatting.  The no-go is strictly information-class scoped;
sequence-specific horizontal arithmetic remains open.  The retained
$1/36$-per-$6m$ ceiling and booking are unchanged.

## Item 294: the ordinary-$j=2$ candidate is an exact half-integer gauge

The four fitted Item-291 coefficient polynomials are exactly the Item-237
algebraic-coefficient operator evaluated at
$h=3n+1/2$ and $h=3n+5/2$, after the explicit hypergeometric gauge



$$
\mathcal R(r)=
 \frac{r(r+6)(2r+9)^2(2r+15)^2}
 {78732(r+1)^2(r+2)(r+4)(r+5)^2}.
$$



Six cleared polynomial identities prove this operator conjugacy exactly.
They do not prove that either connection minor is a solution.  The observed
bridge from normalized $16^nM_n$ to the Item-237 coefficient line remains
finite-only, while two nonzero determinant witnesses show only that
normalized $L_n$ is not that same line.  The gauge is singular on actual
layers $s=1,2$, and the primitive forward coefficient is singular on
$s=1,\ldots,6$ plus possible quintic loci.

Root reproduced the certificate byte for byte and verified all package and
dependency hashes.  Sequence annihilation, Frobenius transport, and weighted
density remain open; the retained $1/105$-per-$6M$ ceiling and booking
are unchanged.

## Item 295: the beta nearest window has an exact moving descent defect

For $a=q_{n-1}$, $b=q_n=Aa+c$, Item 295 proves that



$$
\rho_n<a/2
 \iff H_n\equiv a\pmod A
 \quad\hbox{and}\quad
 |H_n-ac/b|<Aa/(2b),
$$



where $H_n$ is the unique nearest integer to $ac/b$.  The congruence by
itself is only equivalent to the weaker threshold
$\rho_n<b/(2A)=a/2+c/(2A)$.

The exact Euclidean step preserves the determinant but misses the previous
square-residue slice by $t_n=c-\kappa_n$.  With
$T_n=bc-a^2$, it proves
$t_n=\operatorname{nint}(T_n/b)$ and
$T_n+T_{n-1}=4ac$.  Projection introduces the moving term $ct_n$ and
returns only the preceding centered residue, so minimality alone does not
close the descent.  Root reproduced the certificate byte for byte and
verified every package and dependency hash.  Coupled descent, the all-$n$
half-bound, proper targets, and the Item-282 baseline remain open; booking is
zero.

## Item 296: complete singular-ray atlas for the fixed-$j=1$ recurrence

The linear factors of the Item-293 recurrence have exactly three infinite
actual singular rays:



$$
s=2,\qquad s=4,\qquad s=6,
$$



plus the finite prime rows $(h,s,p)=(1,1,13),(2,1,17),(1,2,19)$.
Every nonlinear core is reduced to an explicit irreducible primitive
polynomial in $s$ of degree 5 or 9.  On $s\ge7$, away from the two
endpoint-core loci, the recurrence gives invertible three-state transport in
the same characteristic.

This still does not control the actual sequence: a scalar zero is a
dimension-two hyperplane among unrestricted recurrence states, and the
pinned $E_h^*$ orbit needs additional sequence-specific arithmetic.  Root
reproduced the certificate byte for byte and verified every package and
dependency hash.  No weighted-density theorem follows; the retained
$1/36$-per-$6m$ ceiling and booking are unchanged.

## Item 297: structural coefficient zeros are canceled by a boundary pole

The three infinite singular rays $s=2,4,6$ are shifts of the same prime
diagonal $p=4H+3$.  Their union therefore has logarithmic mass asymptotic
to $2H$, rather than three independent copies.  On that diagonal the
apparently absent recurrence term has a possible simple pole.  After the
exact renormalization $B_H=pE_H^*$, all four terminating Pochhammer sums
reduce for arbitrary $H$, and



$$
B_H\equiv-\frac34XV-9UY\pmod p.
$$



The full gauge-valuation audit proves that every other recurrence value is
integral, including the exceptional $(H,p)=(4,19)$ row.  Thus the vanished
coefficient is generically canceled by the boundary pole and does not lower
the recurrence order.  The complete fixed-core drop table yields no
one-term nonzero constraint on the target.  Root independently reproduced
SHA-256
$aa84dde588a119c67b868266ca536699b3675d2e53cb62ad8f1df66705ca7e6b$
and audited the repaired all-$H$ proof.  Pinned-orbit boundary arithmetic
and weighted zero density remain open; the $1/36$ ceiling is unchanged.

## Item 298: exact centered beta dynamics defeat phase-blind contraction

The beta Turan pair is carried by one rational state
$w_n=T_n/q_n$.  Nearest-integer centering gives an exact bijection between
the moving centered strips and an explicit inverse.  The natural actual
forward carry is not a bounded rounding error: it equals $-6$ at $n=6$,
is negative thereafter, and tends to $-\infty$.

There are also exact primitive-denominator ambient states for which a nearly
maximal preceding centered remainder maps to current remainder $-1$, and
the unscaled pair maps have no row-uniform fixed-norm contraction.  These
witnesses are not the actual Turan orbit; they close only arguments using
the affine recurrence, coprimality, and ordinary real contraction while
discarding the actual short-branch phase.  Root independently reproduced
SHA-256
$c2c1466482faee7ff6d98ebf2e42097306466841024c94b27988298120b1cb97$.
The all-$n$ half-bound, proper-target transfer, and Item-282 product
baseline remain open.  Booking is zero.

## Item 300: every sublinear-depth phase-blind beta strip remains ambiguous

Let $I_n$ be the exact Item-295 interval containing the actual Turan state,
and let $F_n$ be its exact affine update.  Item 300 proves
$F_n(I_{n-1})\subsetneq I_n$ by explicit endpoint differences.  At backward
depth $L$, the transported strip has exact width



$$
|J_{n,L}|=
 \frac{q_{n-L}q_{n-L-1}}
 {q_n(4(n-L)-2)(4(n-L)-1)}.
$$



An explicit product bound shows that this width tends to infinity for every
$L(n)=o(n)$.  The same propagated strip and all its moving denominator
grids therefore admit one model orbit with current remainder $-1$ and
another with remainder $-(q_n-1)/2$.  They have opposite half-bound
behavior.

This is not an actual-orbit counterexample: the witnesses do not retain the
fixed Turan seed numerator and need not have primitive denominators at all
earlier levels.  It closes exactly the declared sublinear-depth,
phase-blind affine-strip class.  Base-reaching histories, seed congruences,
nonlinear arithmetic invariants, proper targets, and the product baseline
remain open.  Root reproduced SHA-256
$eda21ac33bb2570f4fbeaea721a0cebf70776bc07185ecf9c990c35dd0cde161$
byte for byte and independently audited the theorem.  Booking is zero.

## Item 301: the structural boundary scalar has one residual moment

Root-of-unity filters evaluate $U_H,V_H$, and a weighted odd-filter
integral evaluates $X_H$, for every $H$.  The scalar $B_H$ therefore
reduces to one Gaussian moment $Y_H$:



$$
B_H=6(2e_H-1)Y_H\quad(H\text{ even}),
 \qquad
 B_H=-6(Y_H+4+6d_H)\quad(H\text{ odd})
 \pmod p.
$$



The even multiplier is always a unit.  The exact moment has a first-order
recurrence, but no nonvanishing or weighted-density theorem is inferred.
Moreover, the entire boundary-neighbor combination in the actual recurrence
is identically $-Q_0(h)E_h^*$.  When $Q_0$ is a unit this is exactly the
old target gate; at every finite $Q_0$-drop row it is automatic.  Thus the
boundary construction adds no independent codimension.  Root reproduced
SHA-256
$f25813facfe8befb751fdbcd1c5f521c23379162bd44244356c8b2568d9fc784$
byte for byte.  The $1/36$ ceiling is unchanged and booking is zero.

## Item 302: full beta affine elimination recovers only the Turan relation

Let $\mathcal I_n$ be generated over
$\mathbb Z[X_2,\ldots,X_n]$ by the fixed base equation and every exact
affine beta update.  Item 302 proves the endpoint elimination identity



$$
\mathcal I_n\cap\mathbb Z[X_n]
 =\langle q_nX_n-T_n\rangle.
$$



Thus even a base-reaching polynomial elimination produces no second endpoint
identity.  The continuant matrix also gives a square-inverse congruence, and
the centered residue is a square unit modulo every divisor $Q\mid q_n$.
This proves only $|r_{n,Q}|\ge1$, a zero-rate bound.

The no-go is limited to the affine-elimination ideal.  Nearest-integer or
Ostrowski digits, modular-square distribution, nonlinear inequalities,
proper-target constructions, and the product baseline remain open.  Root
reproduced SHA-256
$1cc2de524522d9720cf475ac5836b6d5148edb285f09cf5759d54e5dde6a37dc$
byte for byte.  Booking is zero.

## Item 304: the structural boundary residue is universally nonzero

The remaining Gaussian moment from Item 301 has an exact Gaussian-integer
numerator.  At $n=2H$, Wilson's theorem, the central-binomial congruence,
the binomial theorem, and Frobenius collapse it completely.  For every actual
boundary prime $p=4H+3$,



$$
B_H\equiv-24\left(1+(-1)^{\lfloor H/2\rfloor}2^H\right)\ne0\pmod p.
$$



Euler's criterion proves the final nonvanishing without exceptions.  This is
a genuine all-prime theorem, but it has zero capacity value: Item 301 proves
that $B_H$ is not an independent necessary-zero gate for the pinned
collision.  It only forces compensation among neighboring recurrence terms.
Root reproduced SHA-256
$df1cff1ceb904984ce37db8e76b31d95696610b019df92849d8646eb510e1274$
byte for byte and independently audited the Gaussian, Wilson, Frobenius, and
capacity arguments.  The fixed-$j=1$ ceiling remains $1/36$; booking is
zero.

## Item 305: the beta dual window contains essential convergent multiples

For the exact beta continuant word, Item 305 proves that every small
compatible residue is classified by



$$
R=gQ_k,\qquad \kappa=gD_k,
$$



where $Q_k$ is a prefix-convergent denominator and $D_k$ is the
complementary tail continuant.  Legendre's theorem determines the reduced
convergent but does not force $g=1$.

Two symbolic infinite families make the obstruction sharp: compatible
remainders $R=2Q_k$ occur below the proposed threshold although every
prefix denominator is odd, and a second family has simultaneously
$Q_k<a/(2c)$ and $D_k<c$.  Hence the denominator-only classification and
the proposed tail lower bound are false, not merely unproved.

This closes only that continued-fraction shortcut.  Seed-specific control of
the actual multiplier or nearest quotient, other modular-square or Ostrowski
invariants, proper targets, and the product baseline remain open.  Root
reproduced SHA-256
$10d6989341d0e9c6416fe7a3a26be054ffab39e3df56f82b4e3fa1d42d79bcaf$
byte for byte and independently audited the symbolic families.  Booking is
zero.

## Item 306: the normalized ordinary-$j=2$ $M$ line is algebraic for all $n$

Eight exact Hermite reductions, a meromorphic-beta endpoint identity, and
all nine restored plus/minus tensor coordinates prove that, on
$r=6n+e$, $e\in\{1,5\}$,



$$
\frac{16^nM_{6n+e}}{g_n}
 =\lambda_e[x^{6n+e}]C(x),
 \qquad
 \lambda_1=-\frac{891}{100},\quad
 \lambda_5=\frac{3897234}{41405}.
$$



This is an all-$n$ theorem, not a promoted fit.  The exact terms are killed
by meromorphic continuation of Euler's beta recurrence; no divergent
endpoint is discarded.  Root reproduced SHA-256
$cd48ec7f4cec273c72371d554c9a4ec55ed3cacde0108f4dc92975ba93dbbc55$
byte for byte and audited the normalization, full tensor restoration,
initial-value propagation, and complete actual-ray pole list.

Only $M=-11\det(f,d)$ is realized.  The full necessary determinant remains
$D=cL+M$, with the independent $L=9\det(f,b)$ open.  The ordinary
$j=2$ ceiling therefore remains $1/105$ per $6M$, and booking is zero.

## Item 307: fixed Gaussian divisors close all three singular $j=1$ rays

For each $s\in\{2,4,6\}$ and parity $\epsilon=h\bmod2$, Item 307 proves



$$
c_h^*\equiv\gamma_s(a_{s,\epsilon}+b_{s,\epsilon}w_h)\pmod p,
 \qquad w_h=(-1)^{\lfloor h/2\rfloor}2^h,
$$



with an actual $p$-unit gauge to the pinned $E_h^*$ gate.  Euler's
criterion then forces every collision prime to divide one of six explicit
positive nonzero integers.  Thus the varying-$h$ collision mass on the
three coefficient-singular rays is $O(1)$, with ray multiplicity retained.
Universal nonvanishing is false: $(h,s,p)=(8,2,47)$ is an exact zero.

The master ledger is fixed-$M$.  There the three fixed $s$-values supply
at most three candidates and already have $O(\log M)=o(M)$ raw support.
Consequently this is an exact boundary arithmetic closure but not a
master-capacity saving; the off-ray $s$-varying reservoir remains open and
the $1/36$ ceiling is unchanged.  Root reproduced SHA-256
$7b4850b49b3b1615187936168e6f29ad8cd241aabfb9b7766d618d42a3376613$
byte for byte.  Booking is zero.

## Item 308: the all-$s$ divisor tower is explicit, but height alone cannot close it

For every $s\geq1$, Item 308 turns the pinned ordinary-$j=1$ gate into
an explicit parity form



$$
c_h^*\equiv\Lambda_s^{-1}(a_s+b_{s,\epsilon}w_h)\pmod p
$$



and proves that every actual collision prime divides



$$
D_{s,\epsilon}=2^{3s+1}a_s^2-
 \delta_{s,\epsilon}b_{s,\epsilon}^2.
$$



The clearing factor is a $p$-unit, the $D_{s,\epsilon}$ are explicit
quadratic norms, and their logarithmic height is $O(s)$.  Thus the
fixed-divisor construction now covers the entire moving $s$-family, not
only the three structural rays.

The fixed-$M$ audit is negative.  A fixed-in-$s$ comparison family of
the same norm and linear-height type retains prime mass arbitrarily close to
the raw $1/36$-per-$6M$ ceiling.  Therefore container existence, norm
shape, and height alone cannot yield a strict capacity saving.  This does
not refute sequence-specific factor localization: the exact targets
$W_D(M)=o(M)$ and $W_{\rm off}(M)=o(M)$ remain open.  Root reproduced
SHA-256
$4efff9ca2fb1bc11cc6030e260ff73aae89c28bd157bb41fa6bbc3b32e41e5cf$
byte for byte.  Booking is zero.

## Item 309: the independent ordinary-$j=2$ $L$ line is the $y=-1$ branch

The second connection minor is now global rather than finite-only.  Exact
tail inversion puts the two actual phase forms on the $y=-1$ local branch
of Item 237's algebraic curve.  A common beta normalization makes $L$ a
two-cycle period determinant; all shifted Hermite primitives have zero
finite part at every endpoint, so Item 306's full tensor cancellation proves
recurrence membership.  Three original-tail initials per ray give



$$
\frac{16^nL_{6n+e}}{g_n}=\mu_ea_{6n+e},
 \qquad
 \mu_1=-\frac{729}{50},\quad
 \mu_5=\frac{6377292}{41405}.
$$



Together with Item 306, the full determinant is an exact tied combination
of the $y=0$ and $y=-1$ coefficient branches.  Singular-layer clearing
and weighted zero density remain open, so the $1/105$ ceiling and booking
are unchanged.  Root reproduced SHA-256
$b44200c2e3fe16fca4518e45b40540230db43deee496d84c43336907ef304c5a$
byte for byte.

## Item 310: P-recursiveness does not localize the $j=1$ container primes

Two exact generalized-diagonal formulas prove that the all-$s$
coefficients and both Item 308 container sequences are P-recursive.
The quadratic norm splitting condition is automatic in all eight actual
prime classes, so it excludes no candidate.

A nonzero first-order hypergeometric comparison family of exponential
height contains every prime in $6s<p\leq Ks$ and, as $K$ grows, retains
mass arbitrarily close to the full $1/36$ cell.  Therefore qualitative
P-recursiveness, nonvanishing, exponential height, and norm shape alone
cannot lower the ceiling.  The exact annihilator coefficients, moving-prime
gcd, factor localization, and $W_D(M)=o(M)$ remain open.  Root reproduced
SHA-256
$025ac9ae87cbec544877e072dc5c79fad82039d4d85e4d1abe73d0ffadc77d16$
byte for byte.  Booking is zero.

## Item 311: exact beta multiplier reduction, still an OPEN checkpoint

For the actual beta seed, the Legendre-window event now has the exact
equivalence



$$
R<\frac{a}{2c}
 \iff
 \exists k:\ \widehat D_k\mid a,\quad \widehat D_k>2cQ_k.
$$



Every such branch would have positive odd $R$ and even nearest quotient.
The earlier tempting first-tail/last-tail split is false and is quarantined
by an exact counterexample.  The remaining divisibility implication is
OPEN; even proving it would control only $R<a/(2c)$, leaving the entire
intermediate interval $a/(2c)\leq R<a/2$.  Thus this checkpoint changes no
beta capacity and books zero.  Root reproduced SHA-256
$a4d6aecd652c7f975ebac327840bc178d8a87ffc4e973e9a128f9eb2b4112814$
byte for byte.

## Item 312: an exact all-$s$ fixed-$j=1$ telescoper

The rational aggregate $A_s$ now has a proved all-$s$, order-three,
coefficient-degree-seven recurrence.  An explicit rational Gosper
certificate closes the lower boundary, all three removable endpoint poles,
and the terminal boundary; this is a symbolic theorem, not a fitted
recurrence.

Every actual prime at which the leading or trailing pivot vanishes divides
one of two explicit nonzero degree-seven integers in the fixed master
parameter $M$.  These singular pivots therefore have total logarithmic
mass $O(\log M)=o(M)$.  This does not localize zeros on regular rows.
A $\binom{7s}{s}$ comparison also proves that bounded order/degree,
integrality, nonvanishing, and exponential height alone cannot give the
needed closer theorem.  Root reproduced SHA-256
$21373d42a41590895112b4567bd3eae988166db8d84d55db9514be0e59e8f7f9$
byte for byte.  The $1/36$ ceiling and booking are unchanged.


## Item 322: period-retaining fixed-$M$ transfer and conic barrier

The actual ordinary-$j=2$ period state
$(Z_{r,s},\mathfrak f_{r,s},4^s)$ has an exact triangular first-order
system.  On a fixed-$M$ slice its primitive same-ray step is



$$
(r,s,p)\longmapsto(r-42,s+15,p+6),
$$



with a division-free transfer for the actual exterior residual.  All zero
charts are retained.  On the nondegenerate chart, collision is exactly one
affine half-binomial condition $H_{s-1}=\Theta_{r,s}$, equivalently a
rationally weighted quadratic-character moment on a fixed conic.

The moving exponent satisfies $p/3<q\leq(p-1)/2$; every reduced pointwise
rational representation of its weight has degree at least $(p-3)/4$.
Moreover, rows with both $p$ and $p+6$ prime already have zero
logarithmic rate.  Thus neither bounded-degree conic compression nor
adjacent-prime propagation controls isolated collisions.  Root reproduced
SHA-256
$5266eab4b8856e4c4e3c78e261f85ff11977e06ff64169f602c474f83f06e5cf$
byte for byte.  The $1/105$ ceiling and booking are unchanged.

## Item 313: the Item-311 beta divisor branch is impossible

An exact all-length transfer congruence for the reverse-Bessel continuants
proves two valuations differing by one on the two sides of the hypothetical
Item-311 divisor identity.  A complete rational-convergent endpoint audit
and a mod-eight bridge force the relevant segment length to be divisible by
four, making the valuation contradiction global.  Hence



$$
R_{\rm act}\ge\frac{q_{n-1}}{2q_{n-2}}\qquad(n\ge2).
$$



The desired bound $R_{\rm act}\ge q_{n-1}/2$ remains OPEN throughout the
intermediate window.  Root reproduced SHA-256
$ba2e32e504e69681c2c253033d8f44624feca815dda7b51085bf15f067699a9a$
byte for byte.  Beta capacity and booking remain unchanged.

## Item 314: the ordinary-$j=2$ gate is cleared on every actual layer

Items 306 and 309 combine with the residue-independent ratio
$\mu_e:\lambda_e=18:11$ to give, for every actual row,



$$
D_{r,s}=\frac{g_n\kappa_e}{16^n}
 \left(18\,2^{2s}a_r+11b_r\right).
$$



The outside scale and the global clearer $H_r=6^{r+3}r!$ are
$p$-units.  Thus the original determinant vanishes modulo $p$ exactly
when the displayed two-branch coefficient vanishes, including all six
apparent forward-recurrence singular layers $s=1,\ldots,6$.

The forced cubic endpoint norm is exactly Item 250's old resultant up to
the same unit cube.  It is not an independent divisor and cannot be counted
again.  Algebraic-series norms produce convolutions, while the individual
$O(r)$ height bound sums only to $O(M^2)$; these generic routes are
closed scoped.  Weighted zero density for the cleared coefficient and
actual-period incidence remain OPEN.  Root reproduced SHA-256
$77de2dd46726a5a48e9adc4e40f96341d5da6c8db304d79f0ef8eeb7807245b1$
byte for byte.  The $1/105$ ceiling is unchanged and booking is zero.

## Item 315: the old ordinary-$j=2$ resultant never vanishes over $\mathbb Q$

The certified branch recurrence has three negative coefficients and one
positive forward coefficient.  Three exact negative initials on each ray
therefore prove



$$
a_{6n+e}<0,qquad b_{6n+e}<0,qquad N_{6n+e}<0
 \quad(e=1,5; n\ge0).
$$



Thus the characteristic-zero zero-row question is closed.  The $e=1$
ray is a pure-cubic norm over $\mathbb Q(\sqrt[3]2)$; the $e=5$ ray
splits into linear and quadratic factors, with the actual row selecting a
component through the cubic character of 2.  Neither factor is universally
absent, and the entire norm is still exactly Item 250's old resultant.
The Hadamard diagonal proves P-recursiveness but no fixed-$M$ density
theorem.  Root reproduced SHA-256
$09fdd67a6535a043bcbd1e2a46c4b14a633b9928a5f1c65618c34fab65cfabb6$
byte for byte.  The $1/105$ ceiling and booking remain unchanged.

## Item 316: the remaining beta half-window is one exact all-digit target

For every $n\geq5$, write a candidate remainder in its canonical
Ostrowski digits and form the two signed dual sums $E(\delta)$ and
$U(\delta)$.  Item 316 proves the strict error interval



$$
-S<E(\delta)<a-S
$$



and removes every hidden endpoint carry.  An actual intermediate-window
failure is equivalent in both directions to



$$
\frac{a}{2c}\leq R<\frac a2,\qquad 0<|E|<c,\qquad
 U=(-1)^n\operatorname{sgn}(E)a,
$$



with the nearest quotient exactly $\kappa=|E|$.  For every fixed
$2$-adic precision, an explicit infinite top-two-digit family satisfies
the corresponding target congruence while missing the exact equality.
This closes only fixed-precision truncations, not the exact all-digit target.
Root reproduced SHA-256
$5167e9d160fcecac86791944e41a176d3400f2a6856090de7cf78d55984e7aa4$
byte for byte.  The half-bound, beta capacity, and booking remain OPEN/zero.

## Item 317: exact Gaussian operator and coupled fixed-$j=1$ container

One exact differential telescoper proves that the rational aggregate
$A_s$ and the rescaled Gaussian aggregate
$Z_s=(-2(1+i))^sB_s$ satisfy the same order-three operator from Item 312.
The actual container $D_{s,\epsilon}$ is an exact period-four quadratic
readout of $A_s,Z_s,\overline Z_s$, giving a 24-dimensional all-$s$
system and a six-dimensional step-four system on each residue class.

All four-step forward/backward pivots localize to eight explicit nonzero
degree-seven fixed-$M$ integers, so their prime mass is
$O(\log M)=o(M)$.  On every regular row, however, the operator admits a
nonzero local state with zero quadratic readout.  Thus operator coefficients,
pivots, and regularity alone cannot control off-pivot zeros; the witness is
not the actual initial state.  Root reproduced SHA-256
$334165a7e3a40f043aedd3ea2d221786569aa91262481c2347c436cf10890e44$
byte for byte.  The $1/36$ ceiling and booking are unchanged.

## Item 318: exact actual-period incidence beyond the $j=2$ determinant

With $g=fZ+9cb-11d$, set



$$
\ell=\det(f,b),\quad m=\det(f,d),\quad C=\det(b,d).
$$



The old gate and the two transverse residuals satisfy



$$
D=9c\ell-11m,\quad E_b=\ell Z+11C,\quad
 E_d=mZ+9cC,\quad 11E_d-9cE_b=-DZ.
$$



On $D=0$ and $\ell\ne0$, the original collision is equivalent to the
single division-free actual-period condition



$$
\ell B_s\left(\frac{9\kappa_r}{2}A_s-\tau_{r,s}\right)+11C=0;
$$



the $m$-chart gives the corresponding formula and covers characteristic
11.  Rank-two data has at most one transverse exterior condition after
$D=0$; every determinant tower is blind on rank-at-most-one data.  This is
a genuine formal condition but not a fixed-$M$ weighted-density theorem.
Root reproduced SHA-256
$75e84016af2c7580f1954f795ed080d25083345578558aae49f6df4253891fd7$
byte for byte.  The $1/105$ ceiling and booking remain unchanged.

## Item 319: eliminating the period collapses to the old determinant

The third connection minor has the exact all-$r$ factorization



$$
C_r=\beta_rK_r,\qquad
 \beta_r=-\frac{3(r+1)!}{2(2r+3)(-r/3)_{r+1}},
$$



where $K_r$ is independently constructed from canonical connection
chains.  The factor $\beta_r$ is a $p$-unit on every actual row, so its
removal changes no prime support.  Moreover,



$$
\ell E_d-mE_b=CD.
$$



On either nondegenerate Laurent chart, eliminating the actual period $Z$
from $(D,E_b,E_d)$ gives exactly the old ideal $(D)$.  Thus no further
coefficient minor or resultant can supply the required second arithmetic
condition; the actual incomplete-beta/logarithmic period must be retained.
Root reproduced SHA-256
$c4ce360823dd2d781bebc492e79b65d6ea183a7dada1d4cbee1b1c37334ec194$
byte for byte.  Fixed-$M$ weighted gcd control remains OPEN, and the
$1/105$ ceiling and booking are unchanged.

## Item 320: sub-half-linear beta complement descent stays resonant

Starting from the exact Item-316 all-digit target, every canonical prefix
determinant satisfies an exact forced recurrence with its boundary digit
retained.  Its continuous center is a normalized beta Casoratian.  For every
rational $\lambda<1/2$, an explicit threshold $N_\lambda$ proves that
all truncation depths $r\leq\lfloor\lambda n\rfloor$ stay strictly inside
both target endpoints by more than every allowed digit.  Hence literal
prefix/complement descent cannot close by inheriting an exact earlier target
at any depth whose limsup ratio is below one half.

This does not cover critical or larger depth, full descent, complement
redigitization, nonlinear invariants, or the original exact equality.  Root
reproduced SHA-256
$89755de7ea6ee90a4d91195d2aef7685fc9d47231a6937d3b73a5c9b8d4637e8$
byte for byte.  The centered half-bound and booking remain OPEN/zero.

## Item 321: actual fixed-$j=1$ basis and operator-elimination no-go

The actual rational and Gaussian residue solutions have an exact all-$s$
Casoratian.  On the fixed-$M$ slice its failure set has only
$O(\log M)=o(M)$ prime mass.  Each of the eight actual period quadrics
factors into two genuine solutions of the same operator, with a $p$-unit
change of basis, but the norm is split modulo every actual prime.

Every transported quadratic invariant is therefore a coordinate pullback,
and regular single-row common-operator elimination has the zero ideal by an
explicit invertible isotropic state.  That state is not the actual initial
state: actual factor arithmetic and a sublinear fixed-$M$ gcd/resultant
remain open.  Root reproduced SHA-256
$c196625c48a6e1f154cbbed29bc938eff53a318f172bb7679ade099aa5da3c35$
byte for byte.  The $1/36$ ceiling and booking are unchanged.

## Item 323: all-depth beta dual transducer and literal-inheritance no-go

An exact reversed suffix transducer now replaces Item 320's crude
depth-dependent deviation bound.  For every canonical Ostrowski word and
every depth,



$$
-1<\frac{RH_j-bN_j}{b}<1.
$$



Conditional on the actual Item-316 target, this is exactly the signed
deviation of the prefix determinant from $aQ_j/b$.  A division-free
inequality closes every interior depth, while the two bottom cells are
excluded symbolically by the Markov carry.  Thus literal prefix truncation
cannot inherit an earlier exact target at any depth, including critical,
supercritical, and base-reaching depths.

The original all-digit equality, redigitized or nonlinear invariants, the
centered half-bound, and every capacity consequence remain OPEN.  Root
reproduced SHA-256
$680c7e2c3d5dfdeae2b61e37e38a81a363cf3aa25a5229062e3620c727c77bc6$
byte for byte.  Booking remains zero.

## Item 324: same-row cross-parity resultant and selected-slice no-go

The two actual fixed-$j=1$ parity quadrics satisfy, in every phase,



$$
\operatorname{Res}_A(q_{r,0},q_{r,1})
 =64(X^2+Y^2)^2.
$$



For even $s$, a simultaneous two-parity zero lies in Item 321's
Casoratian exceptional support and has only $O(\log M)=o(M)$ fixed-$M$
mass.  For odd $s$, the two quadrics have four explicit nonzero
projective intersection lines.  Crucially, the actual fixed-$M$ gate
selects one constant parity and does not force the unused one; an exact
preselected $p=47$ eliminant control demonstrates this without being
promoted to a full collision.

Therefore same-row cross-parity gcd/resultant arguments are closed unless a
new bridge forces the unused parity.  Selected-factor arithmetic and
weighted density remain OPEN.  Root reproduced SHA-256
$e479b217fe07ab9d79d4355b992511febc331fc671e2d64bd9456c9b2e82b28a$
byte for byte.  The $1/36$ ceiling and booking are unchanged.

## Item 325: actual fixed-$j=2$ conic involution and rank-two recurrence

On the actual tied phase, the involution $x\mapsto2-x$ removes the
puncture after summation.  The complete character sum is reduced to an
explicit centered binomial convolution and then to the initialized
rank-two system



$$
Y_{q+1}=Y_q+T_q,\qquad
 T_{q+1}={2q+1\over q+1}T_q.
$$



The resulting sequence has full Fourier support, its orbit polynomial has
minimal degree $q-1>p/3-1$, and any rational rank-one gauge has denominator
degree at least $(p-1)/2$; no characteristic-zero rational gauge exists.
Thus bounded-support, fixed-degree, and rank-one gauge shortcuts are closed
for this actual family.  Root reproduced SHA-256
$6ff7d4e393a70cd44b143cae227e7a04452c0c5af2ab7a3a287a2074d6275fde$
byte for byte and independently stressed all identities.  Weighted zero
density remains OPEN; booking stays zero and the $1/105$ ceiling is
unchanged.

## Item 326: actual selected fixed-$j=1$ step-12 recurrence no-go

The four interlaced actual selected-factor phases satisfy exact
determinant-form order-three recurrences under the step $s\mapsto s+3$,
equivalently $p\mapsto p+8$.  The four determinant pairs are nonzero for
every positive integer $s$.  Candidate collision rows separated by any
fixed bounded gap have weighted mass $O(M/\log M)=o(M)$, whereas isolated
candidate rows retain raw capacity $M/6+o(M)$.

Consequently bounded-gap cross-row resultants are closed unless a new
propagation bridge forces a second actual row.  Root reproduced SHA-256
$9378b4078db1385f60a5128617f6e99c75cd282b6be3e5b0be95410da979450f$
byte for byte.  Single-row selected-factor arithmetic and weighted density
remain OPEN; booking stays zero and the $1/36$ ceiling is unchanged.

## Item 327: moving dyadic and all-degree beta projective no-go

For every $n\ge6$ and every $2^s\le2n-3$, there is an explicit
canonical intermediate-window word satisfying the positive target
congruence modulo $2^s$ but not the exact target.  The total available
dyadic mass is only $O(\log n)=o(n)$.

At every suffix depth,



$$
L_j-H_jL_m=-bN_j.
$$



Consequently, for every divisor $D\mid b$ and every homogeneous
digit-independent polynomial $F$ of arbitrary depth and degree $e$,
$F(L)\equiv R^eF(H)\pmod D$.  Thus the whole projective residue tower
adds no target codimension.  Root reproduced SHA-256
$12fadf2ad2b9703cb369cc7e0859bfdf68425f5267581aa6c4d76d9a7b33012a$
byte for byte.  Divided quotients, modulus $b^2$ and higher, nonlinear
integer-size information, redigitization, and the original all-digit target
remain OPEN.  Booking and beta capacity reduction are zero.

## Item 328: actual fixed-$j=2$ Cartier digit and Frobenius break

For



$$
(1-x)^n(1+x)^{n+q}=\sum_k c_kx^k,
$$



the actual residual period satisfies



$$
S_{n,q}=(-1)^nc_p=c_{q-1},\qquad
 H_m=\epsilon(1-c_p)\pmod p.
$$



On the nondegenerate chart the original collision is therefore exactly
$c_p=1-\epsilon\Theta_{r,s}$.  The coefficient recurrence has one
Frobenius break at $k=p-1$, where $c_p$ becomes a free continuation
parameter.  Its endpoint is $q>p/3$ steps away with a nonzero multiplier,
so every bounded- or $o(p)$-depth local recurrence method is blind to the
digit.  Root reproduced SHA-256
$5b372bd499c433695ab0dd487c78b6426386c500aaf249fe9944431d6e363b46$
byte for byte.  Global target arithmetic and weighted zero density remain
OPEN; booking stays zero and the $1/105$ ceiling is unchanged.

## Item 329: actual fixed-$j=1$ cubic Cartier carrier

For $M=3h+4s+2$, $p=4h+6s+3$, and
$P(t)=2-4t+3t^2-t^3$, the factor selected by the actual collision is a
$p$-unit multiple of



$$
K_{M,2h}=[t^{2h}]P(t)^{4M},\qquad 2h=6M-4p.
$$



A dual carrier represents the opposite factor, so the full container
vanishes exactly on the union of the two carrier-zero sets.  The array has a
fixed rational generating function, Laurent Cartier readout, and exact
recurrence.  Degree, alternating sign, integrality, and exponential height
alone cannot reduce the raw capacity.  Root reproduced SHA-256
$4c89f82c9f83dccfb3a32540532e5c986bff1043ec7bfd6f5584500bd7ecc7fc$
byte for byte and checked 113 further actual rows.  Weighted zero density for
the specific carriers remains OPEN; booking stays zero and the $1/36$
ceiling is unchanged.

## Item 330: all-depth beta divided-quotient resonance

Writing $\Delta=k_{m+1}-a$ for the old exact-target defect, every
divided-quotient bridge residual factors as $R_j=\Delta G_j$.  Since
$G_{m-1}=1$ and adjacent companion values are coprime, the complete bridge
ideal is exactly $(\Delta)$.  The normalized same-state $b$-adic lift
also terminates after its first quotient on target, while the suffix-load
tower is only a triangular re-encoding of the original digits.

Thus arbitrary-depth divided quotients and repeated same-state lifts add no
new formal target condition.  Root reproduced SHA-256
$331dcf86a9a2c283d92085e8ebec6da91a1f8dd042fa4149db4b580cc53ebcf0$
byte for byte.  Nonlinear arithmetic, complement redigitization, and external
periods remain OPEN; booking and beta capacity reduction are zero.

## Item 331: global ordinary-$j=2$ coefficient concentration

With



$$
A_m=\sum_{j=0}^m8^{m-j}\binom{2j}{j},
$$



the actual Cartier coefficient obeys
$8^mc_p\equiv8^m-\epsilon A_m\pmod p$.  For fixed $m$, its two sign
fibres lie in explicit residue classes modulo 8, each with positive
Chebyshev mass.  Every fixed rational target has an exact integer-divisor
dichotomy; at $m=0$, full prime progressions already give constant values
0 and 2.  Consequently coefficient-only fixed-target nonconcentration cannot
solve the actual moving-target equation.

Root reproduced SHA-256
$08739a4a4061d5b9d78328aa52b6355711657d75259a133660a3181404f640b2$
byte for byte and independently stressed 1,792 actual and 3,669 fixed-ray
rows.  The determinant-coupled moving target remains OPEN; booking stays zero
and the $1/105$ ceiling is unchanged.

## Item 332: global collapse of the fixed-$j=1$ Cartier carriers

After exact exponent reduction on the actual row, the normalized cubic
carrier is



$$
2^{-4M}K_{M,2h}\equiv b_h,
 \qquad b_h=[t^{2h}](P(t)/2)^{4h/3}\pmod p,
$$



and the characteristic-zero identity
$c_h^*=2(4h+3)b_h/3$ identifies it with the old selected residual.  Its
diagonal generating function lies on exactly the old Item-237 degree-six
curve.  The dual $J/L$ carrier similarly collapses to the old opposite
factor.  Root reproduced SHA-256
$d544609c7ccc08f2ed0c661533939de60d97d2ab75509692925638420f789f68$
byte for byte.  The carriers add no codimension; sequence-specific weighted
zero density remains OPEN, booking stays zero, and the $1/36$ ceiling is
unchanged.

## Item 333: all-modulus nonlinear beta-state saturation

In either sign chamber, the exact target defect is an integral polynomial
coordinate: its top two digit coefficients have an explicit Bezout
combination equal to one.  The target quotient is therefore a polynomial
ring over $\mathbb Z$, and for every modulus $Q$ the specialization kernel
is exactly $(Q,\Delta)$.

Consequently every recurrence-only polynomial in arbitrarily many suffix
loads and first quotients, at arbitrary degree and modulus, is either a
universal syzygy or an old-defect multiple.  Root reproduced SHA-256
$933120c05e0f67663608e9e53354407f4593718c149941942d070f4af3c0a76a$
byte for byte.  Arithmetic of canonical cofactors and complement
redigitization remain OPEN; booking and beta capacity reduction are zero.

## Item 334: target-retaining ordinary-$j=2$ integer carrier

The exact Cartier digit and moving affine target combine into a rational
representative $W^{\rm C}$ congruent to the actual period.  Two chart-free
coordinates $T_0,T_1$ then satisfy



$$
\text{original collision}\Longleftrightarrow T_0=T_1=0\pmod p.
$$



Thus the primitive integer


$$
\mathfrak G_{r,s}=\gcd(|\operatorname{num}D|,
|\operatorname{num}T_0|,|\operatorname{num}T_1|)
$$

 has exactly the original
tied-prime support on every row and every connection chart.  Root reproduced
SHA-256
$238046186f90bdffb2e9b4c72994bac4f0c2ba7e377b42f04753b5502ea861e2$
byte for byte and stressed 1,153 rows.  The required fixed-$M$ theorem is
$\sum\log\operatorname{rad}\mathfrak G_{r,s}=o(M)$; it remains OPEN.
Booking stays zero and the $1/105$ ceiling is unchanged.

## Items 335--339: global cofactor capacity and fixed-cell arithmetic

Item 335 proves that the first canonical beta boundary cofactor, and every
fixed-complexity portfolio of such cofactors, has zero divisor rate.  Item 337
then settles the genuinely different growing-depth question: repeated prime
powers must be de-overlapped by
(Lambda=operatorname{lcm}|z_j|), and one target captures exactly
(Gamma_Q=loggcd(Q,Lambda)).  An explicit canonical intermediate-window
family has ambient LCM rate at least (1/2), so this global tower is the first
beta cofactor invariant that passes the raw capacity screen.  Its overlap with
the actual Item-316 target is still OPEN and no mass is booked.

For ordinary fixed (j=2), Items 336 and 338 prove the exact fixed-(M) prime
interval, the collapse of every affine resultant to the old determinant, the
global two-state Cartier factorization, its diagonal collapse to the original
unknown coefficient, and tied-prime-safe saturation of the first foreign
carrier mechanisms.  The live theorem is weighted control of the joint moving
diagonal target; the (1/105) ceiling is unchanged.

For fixed (j=1), Item 339 reduces the actual selected factor to an integral
positive hypergeometric prefix.  Complete Lucas termwise forcing occurs only
on the zero-rate ray (h=s) odd; positive-rate support retains genuine
growing-length cancellation.  The (1/36) ceiling is unchanged.

All five packages have byte-identical root replays and independent scope
audits.  The booked rate remains
(0.1365141682948128184504238226\ldots), the deficit remains
(1.0196329836694317938803064012\ldots), Route 1 remains ACTIVE, and Route 2
remains QUEUED.

## Items 340--341: complement-loop resonance and affine-state exhaustion

Item 340 settles the full canonical beta complement-inverse loop at once.  On
an actual target it returns the original residue, canonical digit word, every
adjacent cofactor, and therefore the same global LCM.  Its off-target defect
has zero beta rate, while its undivided congruence modulo (Q) collapses to the
old signed-square ray.  New information can first occur in the (bQ)-quotient
lift.  The exact target overlap splits into complement-covered and
valuation-excess factors; neither is yet bounded asymptotically.

Item 341 gives the safely saturated ordinary fixed-(j=2) collision exact
centered affine coordinates.  Their Jacobian is a unit and their localized
ideal contains no hidden third condition.  The degenerate chart is confined
to a triple-minor carrier, and the actual state (4^(m+1),H_m) is Zariski dense
over characteristic zero on every unbounded subsequence.  Thus fixed-curve
compression is closed, but moving finite-field correlation remains OPEN.

Both packages have byte-identical root replays and independent scope audits.
They book zero, leave the (1/105) ceiling and beta capacity unchanged, and do
not alter the booked rate or deficit.  Route 1 remains ACTIVE and Route 2
QUEUED.

## Items 342--345 and 347: chosen-prime and moving-cutoff barriers

For fixed (j=1), Item 342 turns the actual selected coefficient into an exact
finite-field object.  Three Euler moments remove the base-field aliases and
produce a four-sum Teichmuller Kummer lift with a (21 sqrt(p)) conjugate
bound.  Item 345 then proves why ordinary descent does not convert this into
a unit theorem: (p) splits completely, additive projections lose the chosen
coordinate, and relative norms keep both the gate and the full growing-field
height.  The remaining input must be genuinely chosen-prime (p)-adic, or use
special arithmetic not forced by the formal lift.

For beta matching, Item 343 factors the residual target overlap into the
(t)-avoiding squarefree layer (Xi_Q) and a repeated-valuation factor dividing
(Q/rad(Q)).  The latter is already part of the Item-265 squarefull barrier.
All higher quotient lifts encode the same (Q)-adic scalar, so they cannot be
booked as independent conditions.

For ordinary fixed (j=2), Items 344 and 347 give both an exact quadratic
Frobenius model and an exact target-retaining complete character sum.  The
sharp cutoff nevertheless has maximal finite-field degree, full Fourier
support, and minimal semisimple Kummer rank (m+1).  Sublinear rank occurs only
on zero-rate edges.  A nonlinear/nonsemisimple chosen-prime theorem or a
weighted theorem uniform in linear conductor remains OPEN.

All five packages have byte-identical root replays and independent scope
audits.  They book zero, leave the (1/36) and (1/105) ceilings unchanged, and
do not alter the beta capacity, booked rate, or deficit.  Route 1 remains
ACTIVE and Route 2 QUEUED.

## Controlling synthesis through independently audited Item 383

The Item-257 decision phase is now consolidated in
`ROUTE1_MASTER_CAPACITY.md`; later item count is not being used as a progress
metric.  Items 346 and 348--383 produce scoped structural closures but no new
positive linear logarithmic mass.

For beta matching, exact first-hit, incidence, singleton-saturation, content,
and top-symmetric theorems close fixed-depth, bounded-degree, same-sign,
reciprocal-positive, definite-quadratic, and normalized-Newton mechanisms.
The first genuinely live low-degree statistics are now actual rational
split-line correlations, primitive coordinate gcds and Pell/norm values, or
indefinite-conic isotropy.  None has yet been connected to the Item-316 target
by a sub-beta weighted carrier.

For fixed (j=1), the actual ordinary collision retains two independent
coordinates: the selected Hasse value and the transverse period.  A minimal
rank-two filtered Frobenius realization exists, but accepts every Hasse value.
The standard Frobenius lift gives a lacunary connection; another valid lift
makes it rational with one logarithmic boundary pole.  What is invariant is
the absence of any bounded simultaneous splitting and of a dagger horizontal
connection on the full moment disc.  Primitive reduction is invisible to the
selected prime, and same-ray order-three recurrence windows do not align two
actual fixed-(M) rows.  These local models therefore supply no cross-prime
weighted theorem.

For ordinary (j=2), the degenerate triple-minor chart, nonsemisimple transfer,
moment energies, rational kernel, and matched Cartier reduction all return the
same target-retaining cell.  The required theorem remains an aggregate
moving-modulus/average-gcd bound across both charts.

The booked rate and deficit remain



$$
r_1=0.1365141682948128184504238226\ldots,
\qquad
T-r_1=1.0196329836694317938803064012\ldots .
$$



The fixed-cell ceilings remain (1/36) and (1/105), and every audited package
through Item 383 books zero.  The present upper bounds are not exhaustive:
higher-digit and fresh/multi-parent mechanisms still lack compatible global
ceilings.  Route 1 therefore remains **ACTIVE** and Route 2 remains
**QUEUED**.  The targeted filtered-Hasse literature checkpoint is in
`sources/route1_filtered_hasse_literature_note_20260901.md`.
