> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Research log

## 2026-08-26: initialization

Let $s=e+\pi$. The requested conclusion, "$e+\pi$ is not
transcendental," is exactly the assertion $s\in\overline{\mathbb Q}$, since
every complex number is either algebraic or transcendental over $\mathbb Q$.

### Immediate unconditional lemma

**Lemma.** At least one of $e+\pi$ and $e\pi$ is transcendental.

**Proof.** Suppose both $s=e+\pi$ and $p=e\pi$ were algebraic. Then both
$e$ and $\pi$ satisfy $X^2-sX+p=0$, so each is algebraic over
$\overline{\mathbb Q}$. Because the algebraic closure of $\mathbb Q$ is
algebraically closed, both would lie in $\overline{\mathbb Q}$, contradicting
the transcendence of $e$ and $\pi$. QED.

This disjunction does not identify which of the sum or product is
transcendental.

### Conditional consequence of Schanuel's conjecture

The complex numbers $1$ and $i\pi$ are linearly independent over
$\mathbb Q$. Schanuel's conjecture would imply



$$
\operatorname{trdeg}_{\mathbb Q}
  \mathbb Q(1,i\pi,e^1,e^{i\pi}) \ge 2.
$$



Since $1$ and $e^{i\pi}=-1$ are algebraic, this is
$\operatorname{trdeg}_{\mathbb Q}\mathbb Q(\pi,e)\ge2$. Thus $e$ and
$\pi$ would be algebraically independent. If $e+\pi$ were algebraic, the
nonzero polynomial $X+Y-s$ with algebraic coefficients would vanish at
$(e,\pi)$, contradicting that independence. Therefore Schanuel's conjecture
implies $e+\pi$ is transcendental, opposite to the requested direction.

### Core warning

Lindemann--Weierstrass concerns exponentials of *algebraic exponents*.
Neither $1$ and $i\pi$ as a pair nor expressions such as $e^e$,
$e^{e+\pi}$, or $e^{-\pi}$ automatically satisfy those hypotheses.
Any route that invokes the theorem on a transcendental exponent is invalid.

### Active routes

1. Audit consequences of assuming $s$ algebraic under all standard
   transcendence theorems.
2. Search for a valid reduction to linear forms in logarithms or exponential
   algebraic independence.
3. Explore Hermite--Lindemann auxiliary-function constructions specialized to
   the relation $e+\pi=s$.
4. Search for finite, certifiable consequences and numerical obstructions, while
   explicitly avoiding the fallacy that finite PSLQ failure proves
   transcendence.
5. Survey current literature and recent claimed progress.

## 2026-08-26: a structural observation about the mixed-kernel identity

The June 2026 no-go paper uses, for $P\in\mathbb Z[x]$,



$$
A(P)=\sum_{j\ge0}(-1)^jP^{(j)}(1),\qquad
B(P)=\sum_{j\ge0}(-1)^jP^{(j)}(0),
$$



and obtains the integer linear form $A(P)(e+\pi)-B(P)$.

The coefficient map $P\mapsto(A(P),B(P))$ is already surjective from the
linear polynomials in $\mathbb Z[x]$ onto $\mathbb Z^2$. Indeed, for
$P(x)=a+bx$,



$$
S_P(x)=P(x)-P'(x)=a+bx-b,
$$



so $A(P)=S_P(1)=a$ and $B(P)=S_P(0)=a-b$. Given arbitrary
$(A,B)\in\mathbb Z^2$, take $a=A$ and $b=A-B$.

Consequently, the kernel identity by itself imposes no arithmetic restriction
on the integer linear forms: it can encode every $A(e+\pi)-B$. Any proof
from it must obtain genuinely new, non-circular analytic control on a structured
sequence of polynomials; the endpoint arithmetic does not supply that control.

## 2026-08-26: consequences of the algebraicity hypothesis

Assume temporarily that $s=e+\pi\in\overline{\mathbb Q}$. The following are
rigorous consequences, but none is currently contradictory.

1. $e\pi=e(s-e)$ is transcendental. Otherwise $e$ would satisfy the
   quadratic $X^2-sX+e\pi=0$ over $\overline{\mathbb Q}$.
2. $\overline{\mathbb Q}(e)=\overline{\mathbb Q}(\pi)$, and the pair
   $(e,\pi)$ has transcendence degree one.
3. For every nonzero rational $r$,
   

$$
\exp(ire)=\exp(ir(s-\pi))=\exp(irs)\exp(-ir\pi).
$$


   The second factor is algebraic (a root of unity), while the first is
   transcendental by Lindemann--Weierstrass. Hence $\exp(ire)$ is
   transcendental. The same theorem, applied to the distinct algebraic
   exponents $0,irs,-irs$, shows that $\sin(re)$ and $\cos(re)$ are
   transcendental.
4. Nesterenko's algebraic independence of $\pi$ and $e^\pi$ transfers under
   $e=s-\pi$: the numbers $e$ and $e^\pi$ would be algebraically
   independent.
5. Since algebraic numbers and $\pi$ are periods and periods form a ring,
   algebraicity of $s$ would make $e=s-\pi$ a period. It is conjectured,
   but not proved, that $e$ is not a period.
6. The pair $e$ and $e^{ie}$ would nevertheless be algebraically independent.
   Indeed, $e^{ie}=-e^{is}$.  A polynomial relation between $e=e^1$ and
   $e^{is}$ would expand into an algebraic linear relation among numbers
   $e^{m+nis}$.  The exponents $m+nis$ are distinct algebraic numbers for
   distinct integer pairs $(m,n)$, so Lindemann--Weierstrass forbids the
   relation.  Thus the algebraicity hypothesis is compatible with a strong
   algebraic-independence statement; the missing issue is that $e^{ie}$ is a
   nested exponential value.
7. If the stronger special hypothesis $s\in\mathbb Q$ held, then $e$ and
   $e^e$ would be algebraically independent.  Nesterenko gives algebraic
   independence of $\pi$ and $e^\pi$, hence under $\pi=s-e$ of $e$ and
   $e^\pi$.  But $e^\pi=e^s/e^e$, and for rational $s$ the number $e^s$ is
   algebraic over $\overline{\mathbb Q}(e)$.  Dependence of $e$ and $e^e$
   would therefore force dependence of $e$ and $e^\pi$, a contradiction.
8. If instead $s$ were algebraic irrational, then $e$ and $e^s$ would be
   algebraically independent.  A polynomial relation would expand as an
   algebraic linear relation among $\exp(m+ns)$ for finitely many distinct
   pairs $(m,n)\in\mathbb Z_{\geq0}^2$.  Algebraic irrationality of $s$ makes
   all exponents $m+ns$ distinct algebraic numbers, so
   Lindemann--Weierstrass rules out the relation.  This again gives no
   contradiction: it illustrates how much algebraic independence can coexist
   with the single mixed relation $e+\pi=s$.

These consequences show why standard theorems do not immediately disprove the
algebraicity hypothesis: each resulting statement is compatible with present
knowledge. They also provide diagnostic tests for candidate arguments.

## 2026-08-26: bounded computation checkpoint

The exact-interval search in `scripts/bounded_algebraicity_search.py` excludes
every nonzero integer polynomial of degree at most 5 and naive coefficient
height at most 10 from vanishing at $e+\pi$. The exhaustive counts by exact
degree are 20, 420, 8,820, 185,220, and 3,889,620 nonconstant coefficient
vectors. A separate 500-decimal-digit PSLQ run found no relation through degree
5 with coefficient bound $10^{50}$.

The exhaustive bounded statement is rigorous, but mathematically tiny. The
PSLQ result is heuristic. Neither bears on unbounded degree or height and
neither proves transcendence.
## 2026-08-26 — exact continued-fraction certificate

Using only rational arithmetic, the script `scripts/certified_continued_fraction.py`
encloses $e$ by its factorial series and π by Machin's formula with alternating
arctangent-series bounds. The two rational endpoints for $e+π$ have a common
continued-fraction prefix of length 1180; their next partial quotients differ,
so this exhausts the information in the chosen exact interval. Their last
adjacent convergents bracket the entire interval (cross-determinant 1).  At
the stopping point, the transformed tail interval has endpoint floors 12 and
14 and contains the integer 13.  If a rational tail is $u/v$ in this interval,
then $u\geq13$ and $v\geq1$, and the inverse continued-fraction map gives the
reduced denominator $q_{1179}u+q_{1178}v$ because its matrix is unimodular.
Hence the appended tail 13 has the smallest possible
denominator in the exact open interval.  This gives the following
unconditional finite result.

If $e+π=p/q$ in lowest terms, then

```
q >= 229652245935628823900152681235597934424456018254041114668219963057865793021670217067316691665192645763309312489390880726505859323674474097058050439351371650240571213497715952693974552388206100073729160220592963787174430499617199613753645819197453948788388604896492171701037277279382131411757626518827163801625104917421612270031373061950633283613592877365088097951976289865272917242230191339170455146069147603113925747863361056322430261723038896282463755098894667324769513830145691536692785116112467277417647824126311007907464798835921859858678998679631043031001019142735931623773559097185983178788823.
```

The maximal machine-readable certificate for this interval is
`results/cf_maximal_current_interval.json`; its SHA-256 digest is
`5b55cdb6ed04362cee5ad4e4d9ca2678ccbb670f9eedab70a08aac1c0a3fee9c`.
The earlier 1000-coefficient certificate is retained separately for comparison.
This does **not** prove irrationality: every finite continued-fraction prefix is
also the prefix of infinitely many rational numbers.

## 2026-08-26 — a near-relation forced by the algebraicity hypothesis

Assume for this section that $s=e+π$ is algebraic.  Euler's identity gives

$$
e^{is}=-e^{ie}.
$$

For $N\geq 0$ define the finite exponential polynomial

$$
L_N=e^{is}+\sum_{m=0}^{N}\frac{i^m}{m!}e^m.
$$

The exponents $is,0,1,\ldots,N$ are distinct algebraic numbers.  Therefore
Lindemann--Weierstrass proves $L_N\ne0$.  On the other hand, the assumed
identity and the Taylor series of the exponential give

$$
L_N=-\sum_{m=N+1}^{\infty}\frac{(ie)^m}{m!},
$$

and, whenever $N+2>e$,

$$
0<|L_N|\leq
\frac{e^{N+1}}{(N+1)!}\left(1-\frac{e}{N+2}\right)^{-1}.
$$

Thus algebraicity of $s$ would force an explicit sequence of nonzero linear
forms in exponentials of algebraic numbers tending rapidly to zero.  This is
not a contradiction to the qualitative Lindemann--Weierstrass theorem.  The
arithmetic normalization explains the obstruction particularly clearly:
multiplication by $N!$ clears all rational coefficient denominators, but the
corresponding upper bound is of order $e^{N+1}/(N+1)$ and grows rather than
tends to zero.  A proof through this route would require a substantially
stronger quantitative mixed-exponential estimate.

## 2026-08-26 — exact mixed Hermite--Padé probe

The script `scripts/mixed_hermite_pade_probe.py` tests the most direct type-I
ansatz

$$
A_n(z)+B_n(z)e^z+C_n(z)F(z)=O(z^{3n+1}),
\qquad \deg A_n,\deg B_n,\deg C_n\leq n,
$$

together with an endpoint constraint that makes the value at $z=1$ an integer
linear form $A_n(1)+B_n(1)(e+π)$.  Two exact rational systems were tested:

1. $F(z)=\arctan z$ and $C_n(1)=4B_n(1)$;
2. $F(z)=16\arctan(z/5)-4\arctan(z/239)$ and
   $C_n(1)=B_n(1)$ (Machin's formula).

### Explicit all-degree bordered-minor formulation

The raw-arctangent constrained family can be written without solving an
opaque linear system.  Put $m=n+1$ and

$$
R(z)=A(z)+B(z)e^z+C(z)\arctan z,
\qquad \deg A,\deg B,\deg C<m.
$$

Write $(k)_a=k(k-1)\cdots(k-a+1)$ and

$$
\tau_r=\left.\frac{d^r}{dz^r}\arctan z\right|_{z=0}
=\begin{cases}
0,&r\text{ even},\\
(-1)^{(r-1)/2}(r-1)!,&r\text{ odd}.
\end{cases}
$$

After the first $m$ jet equations determine the coefficients of $A$, the
remaining vector

$$
v=(b_0,\ldots,b_{m-1},c_0,\ldots,c_{m-1})
$$

lies in the kernel of an explicit $(2m-1)\times2m$ matrix $D_m$.  Its jet rows,
indexed by $k=m,\ldots,3m-3$, are

$$
E_{k,a}=(k)_a,\qquad H_{k,a}=(k)_a\tau_{k-a},
$$

and its final endpoint row is

$$
(-4,\ldots,-4\mid1,\ldots,1).
$$

All entries are integers; for a nonzero arctangent entry,
$H_{k,a}=\pm k!/(k-a)$.  If $D_m$ has full row rank, its one-dimensional
kernel has the canonical signed-minor generator

$$
v_j=(-1)^j\det D_m^{(j)},
$$

where $D_m^{(j)}$ deletes column $j$.  The eliminated coefficients are

$$
a_k=-\frac1{k!}\left(
\sum_{a\leq k}(k)_ab_a+
\sum_{a\leq k}(k)_a\tau_{k-a}c_a\right),
\qquad 0\leq k<m.
$$

After rational scaling, this produces
$R(1)=A(1)+B(1)(e+\pi)$.  Thus the construction exists as an explicit
determinant family.

The proof in `sources/raw_arctan_bordered_rank_proof.md` discharges the
bordered-rank obligation in all degrees: $D_m$ has full row rank $2m-1$ for
every $m\geq1$ (indeed, the endpoint row may use any rational coefficient in
place of $-4$).  Rank failure would give a
nonzero kernel vector with $B(1)=C(1)=0$, reducing the problem to a square
coefficient determinant for $(z-1)e^z$ and $(z-1)\arctan z$.  Its
Laplace expansion has a unique summand of least $2$-adic valuation, using a
parity-split Cauchy block and an alternating endpoint border.  An independent
line-by-line audit checked the incidence determinant, both Cauchy formulas,
the factorial-moment parity and mod-$4$ equality cases, the two parity
minimizers, and the final $\mathbb Q_2$ noncancellation step, and found no
remaining gap.

The exact script `scripts/raw_arctan_rank_crosscheck.py` checks
the reduced determinant, its complete Laplace expansion, the predicted unique
least-valuation summand, and the rank of $D_m$ through $m=7$.  Its record is
`results/raw_arctan_rank_crosscheck_ell6.json`; a further run through $m=8$ is
in `results/raw_arctan_rank_crosscheck_ell7.json`.  These finite cross-checks
are independent corroboration, not substitutes for the all-degree valuation
lemmas.
The older modular audit in `scripts/constrained_rank_audit.py` remains an
independent finite check through $0\leq n\leq60$.

This rank theorem does **not** prove that the resulting specialized endpoint
form is nonzero or small.  The remaining obligations are endpoint-primitive
height, Archimedean smallness after normalization, and nonvanishing at $z=1$;
these are the parts relevant to irrationality.

### An infinite no-go for unaccelerated Taylor subtraction

The simplest automatically endpoint-matched function is

$$
f(z)=e^z+4\arctan z,
\qquad f(1)=e+\pi.
$$

Let $T_N$ be its degree-$N$ Taylor polynomial and put
$J=\lfloor(N-1)/2\rfloor$.  The arctangent remainder at 1 has the exact
integral representation

$$
\arctan(1)-\sum_{j=0}^{J}\frac{(-1)^j}{2j+1}
=(-1)^{J+1}\int_0^1\frac{x^{2J+2}}{1+x^2}\,dx.
$$

Since $1/2\leq(1+x^2)^{-1}\leq1$ on $[0,1]$, its magnitude lies between
$1/[2(2J+3)]$ and $1/(2J+3)$.  The exponential remainder is smaller than
$2/(N+1)!$.  It follows, allowing for the worst possible cancellation, that
for all sufficiently large $N$,

$$
\left|N!\bigl(f(1)-T_N(1)\bigr)\right|
\geq\frac{N!}{N+2}\longrightarrow\infty.
$$

The factor $N!$ clears every Taylor denominator at $z=1$.  Thus mere Taylor
truncation gives integer linear forms that diverge, not an irrationality
certificate.  This is an asymptotic obstruction to that specific
normalization; it is not a no-go theorem for Padé cancellation or for a
different endpoint gcd normalization.

For every $1\leq n\leq18$, the linear system has the expected one-dimensional
nullspace.  The polynomial vector is first reduced to primitive integer
coefficients; crucially, the gcd of the two endpoint coefficients is then
removed as well, because only those endpoint coefficients need to be integral
for an irrationality certificate.  Exact rational enclosures for $e+π$
certify that none of the 36 resulting primitive endpoint forms even has
absolute value below 1.  In the direct model the absolute values grow from
about $6.72$ at $n=1$ to $1.08\times10^{484}$ at $n=18$; in the Machin model
they grow from about $6.25\times10^{9}$ at $n=1$ to
$1.62\times10^{2040}$ at $n=18$.

The full exact endpoint coefficients and vector hashes are in
`results/mixed_hermite_pade_n18.json` (SHA-256
`fc0e8d85f822179ce7f1efea3f90b1fee806998c0740358e563e7d3e50b14aa3`).
The earlier degree-12 file is retained as a faster reproducibility check.
This is a bounded failure, not a no-go theorem for all Hermite--Padé choices.
It concretely exhibits the two anticipated losses: evaluation at the boundary
of the arctangent Taylor disk in the direct model, and destructive denominator
growth after rational rescaling in the Machin model.

The same exact calculation verifies that the first unconstrained Taylor
coefficient is nonzero in all 36 cases, so the enforced order $3n+1$ is the
exact vanishing order for each tested form rather than merely a lower bound.

The 239-adic data expose the latter loss sharply.  For every tested Machin
degree, the primitive endpoint coefficient $A_n(1)$ has 239-adic valuation
zero, while $B_n(1)$ has valuation

$$
1,1,3,3,5,5,\ldots,17,17
$$

for $n=1,2,\ldots,18$.  Thus the exact data fit
$v_{239}(B_n(1))$ equal to the largest odd integer not exceeding $n$.
This finite pattern does **not** extend to all degrees.  The exact bordered-
determinant audit in `sources/machin_239_endpoint_audit.md` gives a
counterexample at $n=65$, still in the clean range $3n=195<239$:

$$
v_{239}(A_{65}(1))=0,\qquad v_{239}(B_{65}(1))=66,
$$

after endpoint-gcd normalization, rather than the predicted value $65$.
The nominal leading determinant contains the integer sequence

$$
T_0=T_1=1,\qquad T_{m+1}=(4m+2)T_m+T_{m-1},
$$

and $T_{65}\equiv0\pmod{239}$.  A modular computation one digit farther
proves that the extra valuation is exactly one.  The executable exact
certificate is `scripts/machin_239_counterexample.py`.

This also corrects a potential logical overreach: even a true uniform
$239$-divisibility lower bound would be only a coefficient-height lower
bound.  It would not be an Archimedean lower bound for the actual endpoint
linear form, whose two real summands may cancel.  Thus neither the observed
finite pattern nor its exact failure proves an all-degree no-go theorem for
the Machin family.

### Relation to the July 2026 reported diagonal-normality theorem

Runlong Yu's July 2026 repository preprint studies exactly the unconstrained
Machin system $1,e^z,G(z)$ used above, with

$$
G(z)=16\arctan(z/5)-4\arctan(z/239),\qquad G(1)=\pi.
$$

The preprint reports, using a large external 239-adic computer-assisted
certificate, that the ordinary diagonal type-I problem has the
dimension-counting maximal order $3d+2$ for every
$0\leq d\leq1{,}087{,}602{,}879$.  This archive checked the manuscript's
statement and its relevance, but did not independently rerun its roughly
36-billion-inequality external certificate.  Taken at the scope claimed, this
is a substantial nondegeneracy result, but it does not make a linear form in
$e+\pi$.  Its
evaluation has three independent coefficients,

$$
P_0(1)+P_1(1)e+P_2(1)\pi.
$$

For the hypothesis $e+\pi\in\mathbb Q$ to create a discrete integer
contradiction, one needs the additional endpoint match $P_2(1)=P_1(1)$.
Our constrained ansatz imposes exactly this codimension-one condition and
therefore asks for order $3d+1$, one less than the unconstrained diagonal
order.  Yu's reported determinant result neither proves this endpoint functional is
nondegenerate for all $d$ nor supplies the required post-integerization
smallness.  The paper itself identifies denominator/height bounds and small,
provably nonzero evaluated forms as open next steps.

There is a simple quantitative target for the missing height estimate.  Write

$$
G(z)=\sum_{r\geq0}g_rz^r.
$$

For odd $r$,

$$
|g_r|\leq\frac{20}{r5^r},
$$

and $g_r=0$ for even $r$.  Suppose the endpoint-normalized rational
polynomials $A,B,C$ have degrees at most $d$, coefficient height at most $H$,
and

$$
R(z)=A(z)+B(z)e^z+C(z)G(z)=O(z^M).
$$

For $K=M-d\geq2$, summing the untouched Taylor tails gives the rigorous bound

$$
|R(1)|\leq H(d+1)
\left(\frac{K+1}{K\,K!}+\frac{25}{K5^K}\right).
$$

In the endpoint-matched diagonal construction $M=3d+1$, hence $K=2d+1$.
This elementary estimate would force $R(1)\to0$ if, roughly,
$H=o(5^{2d})$.  The exact low-degree systems instead show enormous
denominator-driven heights (already hundreds of decimal digits by $d=12$).
Normality controls rank, not this Archimedean/arithmetic balance.  A sharper
construction could conceivably exploit cancellation beyond this absolute
tail bound, but it would have to prove that cancellation uniformly.

Primary record:
https://ir.ua.edu/items/[session identifier removed]

### Functional independence does hold, but does not specialize

There is an unconditional functional statement behind this construction:
$e^z$ and $G(z)$ are algebraically independent over $\mathbb C(z)$.

Indeed, $e^z$ is transcendental over $\mathbb C(z)$.  If $G$ were algebraic
over $\mathbb C(z,e^z)$, it could have only finitely many analytic branches at
a regular base point.  But continuation around the logarithmic branch point
$z=5i$ leaves both $z$ and $e^z$ unchanged while adding a fixed nonzero
multiple of $\pi$ to $G$.  Repeating the loop gives infinitely many branches,
a contradiction.

This does not imply algebraic independence of $e=e^1$ and $\pi=G(1)$.
Functional algebraic-independence theorems need an arithmetic specialization
theorem to control values, and no theorem presently covers this mixed
E-function/G-function pair.  This is exactly why Siegel--Shidlovsky applies
to systems of E-functions but not to the present system.

## 2026-08-26 — conditional separation by E-values and G-values

Let $\mathbf E$ denote the ring of values of Siegel E-functions at algebraic
points and $\mathbf G$ the ring of values of analytic continuations of
G-functions at algebraic points.  We have

$$
e\in\mathbf E,\qquad \pi\in\mathbf G,
\qquad \overline{\mathbb Q}\subseteq\mathbf E\cap\mathbf G.
$$

If $s=e+\pi$ were algebraic, closure of the two rings would give

$$
\pi=s-e\in\mathbf E\cap\mathbf G,
\qquad e=s-\pi\in\mathbf E\cap\mathbf G.
$$

Consequently, the standard conjecture

$$
\mathbf E\cap\mathbf G=\overline{\mathbb Q}
$$

implies that $e+\pi$ is transcendental.  Fischler and Rivoal explicitly state
that this intersection conjecture is currently out of reach; an Oberwolfach
report says that only the trivial inclusion
$\overline{\mathbb Q}\subseteq\mathbf E\cap\mathbf G$ is known.  Recent
p-adic theorems on functional algebraic independence of selected E- and
G-functions do not specialize to complex values at $z=1$.  Thus this route
precisely reformulates, but does not solve, the missing mixed-value theorem.

## 2026-08-26 — the exponential-period formulation

Let $\mathcal P$ be the field generated by ordinary periods.  It contains
algebraic numbers and $\pi$.  Hence the algebraicity assumption
$s=e+\pi\in\overline{\mathbb Q}$ would imply

$$
e=s-\pi\in\mathcal P.
$$

Fresán and Jossen's exponential period conjecture predicts much more: their
Proposition 12.1.4 states, conditionally on that conjecture, that the
exponential of every nonzero algebraic number is transcendental over
$\mathcal P$.  With the algebraic exponent 1, it predicts that $e$ is
transcendental over $\mathcal P$, contradicting the displayed membership.
Thus

$$
\text{exponential period conjecture}
\quad\Longrightarrow\quad e+\pi\text{ is transcendental}.
$$

This is not an unconditional proof.  Modern comparison theorems for
exponential periods establish that several definitions of the period ring
coincide, but they do not prove the required mixed period conjecture.  The
primary manuscript is Javier Fresán and Peter Jossen, *Exponential motives*,
Conjectures 1.3.2 and 8.2.6 and Proposition 12.1.4:
https://javier.fresan.perso.math.cnrs.fr/expmot.pdf.

## 2026-08-26 — algebraicity-directed structural audit

It is important not to replace the requested direction by an exclusively
transcendence-directed search.  Put $K=\overline{\mathbb Q}$ and assume
$s=e+\pi\in K$.  Then the full ideal of polynomial relations is exactly

$$
\ker\bigl(K[X,Y]\longrightarrow\mathbb C,
          P\longmapsto P(e,\pi)\bigr)=(X+Y-s).
$$

The inclusion from right to left is immediate.  Conversely,

$$
K[X,Y]/(X+Y-s)\simeq K[X],\qquad Y\longmapsto s-X,
$$

and evaluation $X\mapsto e$ is injective because $e$ is transcendental.
Thus the algebraicity hypothesis is internally compatible with all known
individual transcendence facts: it creates exactly the one requested mixed
relation and no others.  In particular, every rational function in $e$ and
$\pi$ that becomes nonconstant after $\pi=s-e$ is transcendental over $K$.

In exponential predimension terms, take $z_1=1$ and $z_2=i\pi$.  These are
$\mathbb Q$-linearly independent, while $e^{z_1}=e$, $e^{z_2}=-1$, and the
algebraicity hypothesis gives $e-i z_2=s$.  Hence

$$
\operatorname{trdeg}_{\mathbb Q}
 \mathbb Q(z_1,z_2,e^{z_1},e^{z_2})=1<2
 =\dim_{\mathbb Q}\langle z_1,z_2\rangle,
$$

an explicit predimension $-1$ configuration.  This pinpoints why Schanuel's
conjecture predicts the opposite answer.  Exponential-algebraic closedness
does not support algebraicity here: its existence principles require the
appropriate dimension/rotundity conditions, whereas this configuration is
already one dimension too small.

A useful theorem strictly weaker than full Schanuel, but still completely
open, would be the following kernel--exponential separation statement.  If
$\omega=2\pi i$ generates the kernel of the complex exponential and
$a,b\in K$ are nonzero, then

$$
\exp(a)+b\omega\notin K.
$$

The case $a=1$, $b=1/(2i)$ is precisely $e+\pi\notin K$.  The complete
positive-direction analysis, including why finite numerical data can never
certify algebraicity and what an exact positive certificate would have to
contain, is in `sources/algebraicity_direction.md`.

## 2026-08-26 — exact endpoint reduction for the raw-arctangent family

The accepted all-degree bordered-rank theorem has two further consequences.
For the unique (up to rational scale) nonzero triple

$$
R_n(z)=A_n(z)+B_n(z)e^z+C_n(z)\arctan z,
\qquad R_n(z)=O(z^{3n+1}),\qquad C_n(1)=4B_n(1),
$$

one has

$$
B_n(1)\ne0
$$

for every $n\geq0$.  Otherwise both $B_n$ and $C_n$ would be divisible by
$z-1$, and the resulting reduced coefficient vector would lie in the kernel
of the square matrix $T_n$ whose nonzero determinant is the core of the rank
proof.

Writing $M=3n+1$, $B_n(z)=\sum b_jz^j$, and
$C_n(z)=\sum c_jz^j$, the endpoint value has the exact tail and integral
representations

$$
R_n(1)=\sum_{j=0}^n b_jE_{M-j}+\sum_{j=0}^n c_jT_{M-j}
=\int_0^1e^tP_n(t)\,dt+
 \int_0^1\frac{Q_n(t)}{1+t^2}\,dt,
$$

where

$$
E_L=\frac1{(L-1)!}\int_0^1e^t(1-t)^{L-1}\,dt,
\qquad
T_L=(-1)^{(o(L)-1)/2}\int_0^1\frac{t^{o(L)-1}}{1+t^2}\,dt,
$$

and the exact endpoint factors are

$$
P_n(t)=(1-t)^{2n}\widetilde P_n(t),
\qquad Q_n(t)=t^{2n}\widetilde Q_n(t^2).
$$

After choosing a primitive integral polynomial triple, let
$a_n=A_n(1)$, $b_n=B_n(1)$, and $g_n=\gcd(|a_n|,|b_n|)$.  The only
Diophantically meaningful normalization is

$$
\ell_n=\frac{a_n}{g_n}+\frac{b_n}{g_n}(e+\pi)
=\frac{R_n(1)}{g_n}.
$$

Rank proves that its second integer coefficient is nonzero; it does not prove
$\ell_n\ne0$ or control its size.  The exact formulas therefore reduce, but
do not solve, the remaining Archimedean and endpoint-gcd problem.  Full details
and the separately checked $n=0$ edge case are in
`sources/raw_arctan_endpoint_remainder.md`.

## 2026-08-26 — rational-translation approximation barrier

Assume conditionally that $s=e+\pi$ is algebraic of degree $d$, and let
$r=p/q\to e$ be reduced rational approximants.  Then
$\alpha=s-r$ has degree $d$ and

$$
\alpha-\pi=e-r,
\qquad h(\alpha)=\log q+O_s(1),
\qquad \log H_{\rm naive}(\alpha)=d\log q+O_{s,d}(1).
$$

Euler's exact continued fraction and Legendre's criterion give an absolute
constant $c>0$ such that

$$
\left|e-\frac pq\right|\geq\frac{c}{q^2\log(2q)}
$$

for every reduced rational $p/q$.  Thus *every* construction obtained by
translating Taylor, rational Padé, or continued-fraction approximants to $e$
has Weil-height approximation exponent at most $2+o(1)$.  Aleksentsev's
established algebraic-approximation measure for $\pi$ gives only the much
weaker exponent

$$
21.4708\,D d(1+\log D)
$$

after this substitution; even in degree one the bound
$\mu(\pi)\leq7.103205334137\ldots$ is too weak.  Multiplying over conjugates
does not repair the gap: for the translated minimal polynomial one gets

$$
|G_r(\pi)|\asymp_s q^d|e-r|
\gg_s\frac{q^{d-2}}{\log(2q)}.
$$

This is an all-sequence no-go for arguments using only degree, height, and
translation error, not a no-go for special numerator arithmetic.  The audited
derivation is in `sources/algebraic_translation_approximation_no_go.md`.

## 2026-08-26 — factorial-recurrence blocks and Roth's theorem

For a real $x$, set

$$
A_n(x)=\lceil n!x\rceil,\qquad
B_n=\lfloor n!e\rfloor,\qquad C_n(x)=A_n(x)+B_n.
$$

The recurrence event

$$
\mathcal R_n(x):\quad
A_{n+1}(x)=(n+1)A_n(x)-1
$$

is exactly the equality

$$
\frac{C_{n+1}(x)}{(n+1)!}=\frac{C_n(x)}{n!}.
$$

Consequently, a block $\mathcal R_u,\ldots,\mathcal R_{v-1}$ freezes these
rationals at a single $c_{u,v}$ whose reduced denominator is at most $u!$ and

$$
|(e+x)-c_{u,v}|<\frac1{v!}.
$$

If $e+x$ is algebraic irrational, Roth's theorem therefore implies that, for
every $\varepsilon>0$, only finitely many blocks can satisfy

$$
v!>(u!)^{2+\varepsilon}.
$$

For $x=\pi$, this gives a new conditional transcendence criterion: infinitely
many recurrence failures would exclude rationality, while infinitely many
superquadratic blocks would exclude algebraic irrationality; proving both
would force $e+\pi$ to be transcendental.  Neither all-index property is known.

The same audit proves that the complete eventual-recurrence exceptional set is
exactly $\mathbb Q-e$, a countable dense set of transcendental numbers, and
that every finite ceiling/digit prefix is compatible (after replacing the
fixed $\pi$ by a transcendental number with that prefix) with a rational,
algebraic-irrational, or transcendental sum with $e$.  Thus finite modular,
$p$-adic, or digit checks alone cannot decide the fixed problem.  See
`sources/factorial_recurrence_audit.md`.

## 2026-08-26 — independent archive audit

An independent line-by-line audit checked the continued-fraction certificate,
bounded polynomial exclusions, all conditional theorem applications, both
Hermite--Padé systems, the all-degree raw $2$-adic rank proof, the degree-65
$239$-adic counterexample, literature attributions, JSON integrity, and full
script reruns.  It found no remaining gap in any statement currently labeled
proved.  Its verdict is equally explicit that the archive contains no proof
of algebraicity, irrationality, or transcendence of $e+\pi$, and that the
large external certificate in the July 2026 repository preprint was not
rerun.  The report is `sources/independent_archive_audit.md`.

## 2026-08-26 — all-degree endpoint-matched Machin rank theorem

Let

$$
G(z)=16\arctan(z/5)-4\arctan(z/239),\qquad G(1)=\pi.
$$

For every $n\geq0$, consider the type-I endpoint system

$$
A(z)+B(z)e^z+C(z)G(z)=O(z^{3n+1}),\qquad C(1)=B(1),
$$

with all three polynomial degrees at most $n$.  The associated
$(2n+1)\times(2n+2)$ high-jet-plus-endpoint matrix has full row rank in every
degree.  Hence the solution line is one-dimensional and every nonzero
solution satisfies

$$
B(1)=C(1)\ne0.
$$

The proof factors a hypothetical vector with $B(1)=C(1)=0$ by $z-1$ and
reduces to a square determinant.  Its parity blocks contain, for odd $d$,

$$
K_d=\frac{4\,5^{-d}-239^{-d}}d.
$$

Writing $d=1+2t$, $R(t)=(1+2t)^{-1}$, and
$c=4/5-1/239$, the analytic kernel $F(t)=K_{1+2t}$ satisfies

$$
F-cR\in\mathcal A_4,
\qquad
\mathcal A_h=
\left\{\sum_{m\geq0}a_mt^m:a_m\in2^{m+h}\mathbb Z_2\right\}.
$$

A square-and-bordered determinant stability lemma shows that, after the exact
Vandermonde and finite-difference factors are removed, the Machin determinants
are congruent modulo $16$ to odd-unit multiples of the corresponding raw
Cauchy determinants.  This preserves the raw proof's unique least-$2$-adic
Laplace summand for every $n$.

An independent adversarial audit checked all normalizations, signs, parity
splittings, the $n=1$ empty-block convention, and the transfer of equality
cases.  It reproduced the archived exact determinants through $n=8$, extended
them through $n=20$, and ran 3,800 exact randomized stability tests without a
counterexample.  The proof and audit are
`sources/machin_bordered_rank_proof.md` and
`sources/independent_new_theorems_audit.md`.

This theorem settles nondegeneracy only.  It gives neither a primitive-height
bound strong enough for Diophantine use nor a small nonzero endpoint value
$A(1)+B(1)(e+\pi)$.

## 2026-08-26 — arithmetic normalization of the raw endpoint determinant

Let $J_n$ be the integral high-jet-plus-endpoint matrix for the raw
$\arctan z$ family and augment it by the row $B(1)$ to obtain the cofactor
$\Delta_{B,n}$.  The accepted unique-least-valuation proof gives an exact
closed formula for $v_2(\Delta_{B,n})$ in every degree; in particular,

$$
v_2(\Delta_{B,n})=3n^2+O(n\log n).
$$

This very large valuation does not automatically belong to the primitive
integer coefficient at the endpoint.  If $\Delta_{A,n}$ is obtained by
augmenting $J_n$ by the integral functional $n!A(1)$, then the primitive
endpoint pair is, up to a common sign,

$$
\alpha_n=\frac{\Delta_{A,n}}{h_n},\qquad
\beta_n=\frac{n!\Delta_{B,n}}{h_n},\qquad
h_n=\gcd\bigl(|\Delta_{A,n}|,n!|\Delta_{B,n}|\bigr).
$$

Thus for every prime $p$,

$$
v_p(\beta_n)=
\max\{0,v_p(n!\Delta_{B,n})-v_p(\Delta_{A,n})\}.
$$

At $n=18$, for example, the valuations of $\Delta_B$, $18!\Delta_B$, and
$\Delta_A$ are respectively $806$, $822$, and $794$, leaving only
$v_2(\beta_{18})=28$.  This is a rigorous obstruction to transferring rank
determinant divisibility through endpoint gcd reduction.

The same cofactor method represents the first unconstrained Taylor coefficient
by a third determinant $\Delta_{M,n}$, $M=3n+1$.  Its nonvanishing is certified
through $n=30$, not proved for all $n$.  Hadamard's inequality gives the valid
but coarse all-degree bound

$$
\max(|\alpha_n|,|\beta_n|)=\exp(O(n^2\log n)).
$$

The exact formulas, finite verifier, and explicit parity cases are in
`sources/raw_arctan_endpoint_arithmetic.md`.  A separate adversarial audit
rederived the determinant scaling, parity formulas, cofactor ratios, gcd
normalization, and Hadamard constant, extended direct determinant checks to
$n=16$, and reproduced the archived JSON byte for byte.  Its accepting report
is `sources/independent_raw_endpoint_arithmetic_audit.md`.

## 2026-08-26 — diagonal Padé forms for the nested exponential identity

Under the temporary hypothesis $s=e+\pi\in\overline{\mathbb Q}$, Euler's
identity gives $e^{ie}=-e^{is}$.  For

$$
P_n(z)=\sum_{k=0}^n\frac{(2n-k)!}{k!(n-k)!}z^k,
\qquad Q_n(z)=P_n(-z),
$$

the exact Padé identity is

$$
Q_n(z)e^z-P_n(z)
=\frac{(-1)^nz^{2n+1}}{n!}
  \int_0^1t^n(1-t)^ne^{tz}\,dt.
$$

At $z=ie$, put $\Lambda_n=Q_n(ie)e^{ie}-P_n(ie)$.  Symmetry of the beta
weight eliminates the sine part and proves the unconditional two-sided bound

$$
\cos(e/2)\frac{e^{2n+1}n!}{(2n+1)!}
\leq |\Lambda_n|\leq
\frac{e^{2n+1}n!}{(2n+1)!}.
$$

Thus every $\Lambda_n$ is nonzero and tends to zero.  Under algebraicity of
$s$, expansion of $-Q_n(ie)e^{is}-P_n(ie)$ is a Gaussian-integer linear form
in exponentials of the distinct algebraic exponents

$$
0,1,\ldots,n,\qquad is,1+is,\ldots,n+is,
$$

so Lindemann--Weierstrass independently proves nonvanishing.  The coefficient
height is exactly $H_n=(2n)!/n!$, and

$$
\lim_{n\to\infty}
\frac{-\log|\Lambda_n|}{\log H_n}=1,
\qquad
H_n|\Lambda_n|=\exp(2n+O(\log n)).
$$

The construction therefore repairs the denominator-growth defect of the
earlier Taylor forms but not their arithmetic defect: $\Lambda_n$ is a small
value at an algebraically independent transcendental point, not a nonzero
algebraic integer.  Qualitative Lindemann--Weierstrass supplies no uniform
lower bound.  `sources/nested_exponential_pade_audit.md` contains the proof,
and `sources/independent_new_theorems_audit.md` accepts it after independent
coefficient checks through degree $12$.

## 2026-08-26 — conditional exponential consequences of algebraicity

A full audit of Baker, Brownawell--Waldschmidt, Nesterenko, and Roy gives
several new consequences of the temporary hypothesis
$s=e+\pi\in\overline{\mathbb Q}$, but no contradiction.  Baker's
nonhomogeneous logarithm theorem yields

$$
\exp(qe+r\pi)\text{ transcendental}
\quad
(q,r\in\overline{\mathbb Q},\ q\ne0).
$$

Indeed, if $\lambda=qe+r\pi$ were a logarithm of an algebraic number and
$\ell=i\pi=\log(-1)$, then

$$
\lambda-i(q-r)\ell=q(e+\pi)=qs
$$

would be a nonzero algebraic linear form in logarithms of algebraic numbers,
contrary to Baker.  In particular, $e^e=\exp(e)$ and
$\exp(-2se)$ would be transcendental.

The Brownawell--Waldschmidt algebraic-independence theorem gives the
disjunction that $\exp(\pi^2)$ is transcendental or $e,\pi$ are algebraically
independent.  The hypothesis $s\in\overline{\mathbb Q}$ excludes the second
branch and hence forces $\exp(\pi^2)$ to be transcendental.  This remains
compatible with

$$
\exp(\pi^2)=
\exp(s^2)\exp(e^2)\exp(-2se),
$$

because $\exp(e^2)$ is uncontrolled and the other factors are transcendental.
Roy's strong six exponentials theorem likewise forces every block of four
consecutive powers of $e$ to contain an exponent outside the logarithmic
space $\widetilde{\mathcal L}$; it produces further nested transcendental
values rather than an upper-transcendence-degree contradiction.

The exact hypotheses, primary sources, and failed theorem combinations are
recorded in `sources/exponential_theorem_audit.md`.

## 2026-08-26 — fully primitive symmetric direct-integral barrier

For (4\mid n), put

$$
w_n(x)=x^n(1-x)^n,
$$

$$
E_n=\frac1{n!}\int_0^1w_n(x)e^x\,dx=q_ne-p_n,
$$

and

$$
J_n=\int_0^1\frac{w_n(x)}{1+x^2}\,dx
=r_n+(-1)^{n/4}\frac{2^{n/2}}4\pi.
$$

Repeated integration by parts, the Bessel-polynomial recurrence, and a
determinant identity prove that (p_n,q_n) are positive coprime integers.
Exact division of (w_n) by (1+x^2) proves the displayed sign and
π-coefficient.  After independently primitive-normalizing the two
component forms and matching their (e)- and π-coefficients, the raw
matched form satisfies

$$
|\Lambda_n|\ge
\begin{cases}
\displaystyle \frac{n!}{(2n+1)2^{n/2}},&n\equiv0\pmod8,\\[6pt]
\displaystyle \frac{n!}{2(2n+1)2^{n/2}},&n\equiv4\pmod8.
\end{cases}
$$

The second congruence class initially appears capable of cancellation, but
the exact comparison

$$
\frac{E_n/q_n}{J_n/(2^{n/2}/4)}
\le \frac{e\,2^{n/2}}{2n(2n-1)!}<\frac12
$$

fixes its sign for every (n\ge4).

A separate cross-content audit was necessary.  If (B_n) is the primitive
π-coefficient and (H_n) is the content acquired only after the two forms
are matched, prime-power valuation analysis gives

$$
H_n\mid\gcd(q_n,B_n).
$$

Writing (D_{2n-1}=\operatorname{lcm}(1,\ldots,2n-1)), the rational part of
(J_n) has denominator dividing (D_{2n-1}), and hence

$$
B_n\le D_{2n-1}\frac{2^{n/2}}4.
$$

Therefore the *final* primitive form obeys

$$
|\Lambda_n^{\rm prim}|\ge
\begin{cases}
\displaystyle
\frac{4n!}{D_{2n-1}(2n+1)2^n},&n\equiv0\pmod8,\\[8pt]
\displaystyle
\frac{2n!}{D_{2n-1}(2n+1)2^n},&n\equiv4\pmod8.
\end{cases}
$$

Both bounds tend to infinity because
(\log D_{2n-1}=2n+o(n)) while
(\log(n!)=n\log n-n+O(\log n)).  Thus every symmetric log-free
common-beta-kernel construction in this class fails even after all primitive
reductions.  This is a family-specific no-go theorem, not a statement about
non-diagonal or unrelated kernels and not a proof about (e+\pi) itself.

The proof, corrected-source audit of Rivoal's simultaneous approximants, and
exact verifier are in `sources/direct_integral_linear_forms_audit.md`,
`scripts/direct_integral_beta_probe.py`, and
`results/direct_integral_beta_probe_n64.json`.  The script compiles, the JSON
parses, and a fresh run reproduces the archived output byte for byte.

## 2026-08-26 — Machin endpoint tails and a non-diagonal no-decay ray

For

$$
G(z)=16\arctan(z/5)-4\arctan(z/239),\qquad G(1)=\pi,
$$

let $U_L$ be the Taylor tail at $z=1$ beginning at degree $L$, and
let $o(L)=2h+1$ be the least odd integer at least $L$.  An exact integral
representation proves

$$
(-1)^hU_L>0
$$

and

$$
\frac1{o(L)}
\left(\frac{200}{13}5^{-o(L)}-4\,239^{-o(L)}\right)
\le |U_L|
\le\frac{16}{o(L)5^{o(L)}}.
$$

Moreover,

$$
U_L=(-1)^h\frac{200}{13}\frac{5^{-o(L)}}{o(L)}
\left(1+O(1/o(L))+O((5/239)^{o(L)})\right).
$$

Thus a single combined Machin tail has a certified sign and nonzero leading
constant; its $5$- and $239$-parts cannot silently cancel.

For arbitrary polynomial degree bounds $(a,b,c)$ and
$M>\max\{a,b,c\}$, any endpoint-matched high-order form has the exact tail
identity

$$
R(1)=\sum_{j=0}^b b_jE_{M-j}+\sum_{j=0}^c c_jU_{M-j}.
$$

After division by the endpoint gcd, with effective coefficient heights
$H_B^*,H_C^*$, this yields

$$
|\ell|
\le H_B^*(b+1)\frac{K_E+1}{K_EK_E!}
 +H_C^*(c+1)\frac{16}{O_G5^{O_G}},
$$

where $K_E=M-b$, $K_G=M-c$, and $O_G=o(K_G)$.  In the diagonal
dimension-balanced family the sufficient Machin threshold is
$H_C^*=o(5^{2n})$, up to polynomial factors.  The only currently proved
general cofactor height is the much larger
$\exp(O(n^2\log n))$, and exact adjacent-coefficient cancellation prevents
turning the upper estimate into a converse.

The note also solves one non-diagonal ray exactly.  For every positive odd
$N$, take

$$
(a,b,c)=(N-1,1,1),\qquad D=N^2+N-1.
$$

The unique solution line has an explicit kernel vector, and its scale-free
endpoint error is

$$
\varepsilon_N
=E_{N+2}+U_{N+2}
 -\frac{g_N}{D}
 -\frac{N+2}{D(N+1)!}.
$$

It satisfies

$$
\varepsilon_N=(-1)^{(N+1)/2}\frac{200}{13}
\frac{5^{-(N+2)}}{N+2}\left(1+O(1/N)\right).
$$

On the infinite subsequence

$$
N=1+2\cdot239^k,
$$

the endpoint ratio has exact valuation

$$
v_{239}\!\left(\frac{A(1)}{B(1)}\right)=-N,
\qquad v_{239}(\beta_N)=N.
$$

Consequently the fully primitive forms satisfy

$$
|\alpha_N+\beta_N(e+\pi)|
\ge c\,\frac{(239/5)^N}{N}\longrightarrow\infty
$$

along that subsequence.  This proves that the full odd-$N$ ray cannot tend
to zero.  It does not claim divergence at every odd $N$.

For arbitrary odd $N$, an exact leading-residue criterion
$\mathcal C_N\in\mathbb F_{239}$ proves a nearly linear valuation lower
bound whenever $\mathcal C_N\ne0$.  The exceptional set is real rather
than hypothetical: at

$$
N=9\,196\,483
$$

the two dominant residues are $144$ and $95=-144\bmod239$, so
$\mathcal C_N=0$.  Subsequent $239$-adic digits are therefore the exact
remaining obstruction to a uniform all-odd-$N$ theorem.

The source, three exact verifiers, frozen results, and independent audit are
in sources/machin_endpoint_asymptotics.md,
scripts/machin_endpoint_tail_probe.py,
scripts/machin_nondiagonal_probe.py,
scripts/machin_fixed_bc1_ray.py, their corresponding JSON files, and
sources/independent_machin_endpoint_asymptotics_audit.md.  The independent
audit rederived every displayed constant and normalization, stress-tested
all odd $N\le501$, and reproduced all three archived outputs byte for byte.

## 2026-08-26 — fixed positive rational kernels cannot repair symmetric matching

The symmetric direct-integral obstruction extends beyond
$K(x)=1/(1+x^2)$.  Let a single fixed $K\in\mathbb Q(x)$ have no pole
on $[0,1]$ and satisfy $K(x)\ge\kappa>0$.  Suppose that for an infinite
set of even indices

$$
J_n(K)=\int_0^1x^n(1-x)^nK(x)\,dx
=r_n+\varepsilon_nc_n\pi,
$$

where $r_n,c_n\in\mathbb Q$, $c_n>0$, and
$\varepsilon_n\in\{1,-1\}$.

A reduced rational representation $K=P/Q$, fixed-denominator polynomial
long division, and an elementary exponential bound for
$\operatorname{lcm}(1,\ldots,O(n))$ prove that

$$
H(r_n),H(c_n)\le C_K^n.
$$

The only constants needed after division are the fixed finite set
$\int_0^1x^j/Q(x)\,dx$.  Extending $1,\pi$ to a basis of their finite
$\mathbb Q$-span makes the height statement rigorous even when the
individual integrals also involve logarithms or other fixed constants:
whenever those extra coordinates cancel and the result lies in
$\mathbb Q+\mathbb Q\pi$, its two remaining rational coordinates still
have exponential height.

If

$$
L_n=A_n+\varepsilon_nB_n\pi=m_nJ_n(K)
$$

is the primitive integer normalization, this implies

$$
c_nB_n\le C^n.
$$

The primitive exponential beta form satisfies

$$
q_n\ge\frac{n(2n-1)!}{n!},
\qquad
J_n(K)\ge\kappa\frac{(n!)^2}{(2n+1)!}.
$$

After minimal coefficient matching, a prime-power content lemma proves that
the new final gcd divides $\gcd(q_n,B_n)$, hence is at most $B_n$.
For the same-sign class this gives

$$
|\Lambda_n^{\rm prim}|
\ge\frac{\kappa n!}{2(2n+1)c_nB_n}.
$$

For the opposite-sign class,

$$
\frac{E_n/q_n}{J_n(K)/c_n}
\le\frac{e\,c_n}{\kappa n(2n-1)!}\longrightarrow0,
$$

so the matched difference eventually has a fixed sign and

$$
|\Lambda_n^{\rm prim}|
\ge\frac{\kappa n!}{4(2n+1)c_nB_n}.
$$

Both lower bounds tend to infinity because $c_nB_n$ is only exponential.
Thus no fixed positive rational kernel with the stated exact moment property
can produce a small primitive sequence through symmetric common-beta
matching.

The theorem does not cover a kernel depending on $n$, a sign-changing
kernel, different weights for the two component forms, or a nonrational
kernel.  The proof is in
sources/fixed_rational_kernel_barrier.md, and the independent reconstruction
is in sources/independent_fixed_rational_kernel_audit.md.  The audit found
and forced correction of a sign error and a removable-pole proof-hygiene
issue before accepting the frozen theorem.

## 2026-08-26 — corrected root-of-unity exponential--logarithm Padé audit

The author-corrected 2021 version of Rivoal's simultaneous Padé theorem was
specialized at

$$
\zeta=e^{2\pi i/N},\qquad \eta=1-\zeta,\qquad N\geq7,
$$

where the Taylor branch has

$$
\log(1-\eta)=\frac{2\pi i}{N}.
$$

For the corrected parameters $d\geq2c$, $f\geq c$, reversal of the two
Padé relations gives polynomials $A,B,E$ satisfying

$$
A(x)\log(1-x)-B(x)=O(x^{2c+d+1}),
$$

and

$$
A(x)e^x-E(x)=O(x^{f+d+1}).
$$

Writing $C=c+d$, $F=f+2c$,
$\ell_C=\operatorname{lcm}(1,\ldots,C)$, and
$G=\operatorname{lcm}(\ell_C,F!)$, exact coefficient reconstruction proves

$$
A^*=d!A\in\mathbb Z[x],\quad
B^*=d!\ell_CB\in\mathbb Z[x],\quad
E^*=d!F!E\in\mathbb Z[x].
$$

The cross-product

$$
\Lambda=
2iA(\eta)\bigl(A(1)e-E(1)\bigr)
+NA(1)\left(A(\eta)\frac{2\pi i}{N}-B(\eta)\right)
$$

is therefore a linear form in $1$ and $s=e+\pi$.  Under the hypothesis
$s\in\overline{\mathbb Q}$, choose an integer $\delta>0$ for which
$\delta s$ is integral.  Then

$$
X=\delta d!^2G\Lambda
$$

is an algebraic integer in $\mathbb Q(s,i,\zeta)$.  This is a valid new
conditional reduction.  The Padé clearing $d!^2G$ is explicit; bare
algebraicity supplies $\delta$, the minimal polynomial of $s$, and its
conjugate house only existentially.

The construction stops at two rigorous barriers.  First, the corrected Padé
theorem has no determinant statement proving $X\ne0$; cancellation of the
two remainders would merely identify the hypothetical algebraic $s$ with a
particular algebraic approximant.  Second, even if $X\ne0$, a contradiction
requires

$$
|X|\,\mathcal B^{[\mathbb Q(s,i,\zeta):\mathbb Q]-1}<1
$$

for a valid all-conjugate bound $\mathcal B$.  The small selected factor
$|1-\zeta|^{2c+d+1}$ does not itself yield such a gain, because

$$
N_{\mathbb Q(\zeta)/\mathbb Q}(1-\zeta)=\Phi_N(1)
=
\begin{cases}
p,&N=p^r,\\
1,&N\text{ has at least two distinct prime factors}.
\end{cases}
$$

Thus the other cyclotomic embeddings exactly compensate that isolated local
contraction when $N$ is not a prime power, and give an adverse factor when
$N$ is a prime power.  This norm identity concerns the isolated factor, not
the norm of the full additive form $X$, so it is not a universal no-go
theorem for every refined cyclotomic construction.

The source audit and a separate full reconstruction are in
sources/root_of_unity_exp_log_pade_audit.md and
sources/independent_root_of_unity_exp_log_pade_audit.md.  The independent
check rederived the reversal, every factorial and LCM clearing, both integral
remainders, the embedding bound, the norm-tower identities, and 4,212 finite
test cases.  It also confirmed that analytic remainder estimates at the
distinguished branch cannot be transported through arbitrary algebraic
embeddings of the hypothetical number $s$.

## 2026-08-26 — sign-changing fixed rational kernels also diverge

The positivity hypothesis in the preceding fixed-kernel theorem has now been
removed.  Let $K\in\mathbb Q(x)$ be any fixed real rational function with
no pole on $[0,1]$, and suppose that for infinitely many even $n$

$$
J_n(K)=\int_0^1x^n(1-x)^nK(x)\,dx
=r_n+\varepsilon_nc_n\pi,
\qquad c_n>0,\quad \varepsilon_n\in\{1,-1\}.
$$

Only the symmetric part

$$
K_{\rm s}(x)=\frac{K(x)+K(1-x)}2
$$

contributes.  It cannot vanish identically, because that would give a
nontrivial rational relation with $\pi$.  If its first nonzero midpoint term
is

$$
K_{\rm s}(1/2+t)=a t^{2m}+O(t^{2m+2}),
$$

then exact beta integrals give

$$
\int_{-1/2}^{1/2}(1-4t^2)^nt^{2j}\,dt
=\frac{1}{2\cdot4^j}B\left(j+\frac12,n+1\right)
$$

and consequently

$$
J_n(K)=
\frac{a\Gamma(m+1/2)}{2\cdot4^m}
4^{-n}n^{-m-1/2}\left(1+O_K(n^{-1})\right).
$$

Thus even a sign-changing fixed kernel has an eventual fixed sign and an
explicit exponential-scale lower bound.  Positivity was never needed for
the rational-coordinate height lemma, so primitive normalization still gives

$$
c_nB_n\leq C^n.
$$

After orienting the primitive $\pi$-form by the eventual sign, minimally
matching it with the primitive exponential beta form, and removing all new
content, the content divides $\gcd(q_n,B_n)$.  In either coefficient-sign
class the resulting form satisfies, for all sufficiently large relevant
indices,

$$
|\Lambda_n^{\rm prim}|
\geq
c\,\frac{n(2n-1)!}{n!}
\frac{4^{-n}n^{-m-1/2}}{C^n}
\longrightarrow\infty.
$$

This eliminates every single fixed rational common kernel, not merely the
positive ones.  The remaining direct-integral escape routes require a kernel
that depends on $n$, different weights for the two component constants, or
a nonrational kernel.

The accepted proof is in
sources/sign_changing_fixed_rational_kernel_barrier.md.  Its independent
audit, sources/independent_sign_changing_fixed_rational_kernel_audit.md,
rederived the asymptotic through the exact beta identity and checked the
antisymmetric case, sparse index sets, both sign orientations, all primitive
content cases, and the final factorial divergence.

## 2026-08-26 — exceptional $239$-adic digits and an adjacent-pair theorem

The leading-residue obstruction for the fixed-$(b,c)=(1,1)$ Machin ray has
now been continued to further $239$-adic digits.  With $p=239$,
$s_r=(-1)^{(r-1)/2}$, and $D_N=N^2+N-1$, the rational endpoint ratio has
the exact decomposition

$$
R_N=\frac{A(1)}{B(1)}=4h_N+Q_N,
$$

where its entire negative-$p$-power part is

$$
h_N=
\sum_{\substack{1\le r<N\\r\ {\rm odd}}}\frac{s_r}{rp^r}
+\frac{s_N(N+1)}{D_Np^N}.
$$

If $W_N$ is the maximal denominator exponent from Proposition 6.1, then
$\Sigma_N=p^{W_N}h_N$ is $p$-integral.  Modulo $p^k$, only indices
whose exponent lies within $k$ of $W_N$ contribute.  An explicit regular
gap $\Gamma_N$ separates the $5$-power and factorial terms, so whenever

$$
t=v_p(\Sigma_N)<\Gamma_N
$$

one has exactly

$$
v_p(R_N)=-W_N+t,\qquad v_p(\beta_N)=W_N-t.
$$

A direct case proof classifies every positive odd $N<p^3$.  There are
exactly $238$ leading ties and exactly two leading-residue zeros:

$$
N_B=4\,569\,679=p^2\cdot80-1,
\qquad
N_A=9\,196\,483=p^2\cdot161+2.
$$

Their next digits are nonzero:

$$
v_p(\beta_{N_B})=N_B-3=4\,569\,676,
\qquad
v_p(\beta_{N_A})=N_A-1=9\,196\,482.
$$

A third rigorously certified exception far beyond the enumerated range is

$$
N_C=p^4\cdot283+4=923\,374\,845\,407,
\qquad
v_p(\beta_{N_C})=N_C-1.
$$

Thus all three known leading cancellations lose only one additional
$239$-adic digit relative to their respective leading exponent.  This
finite behavior is not extrapolated to every exceptional index.

The stronger unconditional result comes from the scaled singular sum

$$
F_N=
\sum_{\substack{1\le r<N\\r\ {\rm odd}}}\frac{s_rp^{N-r}}r
+s_N\frac{N+1}{D_N},
$$

which satisfies

$$
F_{N+2}=p^2F_N-s_NH_N,
$$

with

$$
H_N=
\frac{p^2D_{N+2}+N(N+3)D_N}{ND_ND_{N+2}}.
$$

The positive numerator $P_N$ of $H_N$ has degree four.  Hence, with
$B_N=\lfloor\log_pP_N\rfloor$,

$$
\min\{v_p(F_N)+2,v_p(F_{N+2})\}\le B_N=O(\log N),
$$

including the cases in which one of the two $F$-values is zero.  Once the
regular terms are separated, this proves that for every sufficiently large
odd $N$, at least one $j\in\{N,N+2\}$ satisfies

$$
v_p(\beta_j)\ge j-B_N=j-O(\log N).
$$

Combining this with the already proved uniform endpoint-error asymptotic
$|\varepsilon_j|\asymp 5^{-j}/j$ gives a divergent member in every
sufficiently large adjacent pair:

$$
\max_{j\in\{N,N+2\}}
|\alpha_j+\beta_j(e+\pi)|
\ge
\frac{c\,(239/5)^N}{N^{O(1)}}
\longrightarrow\infty.
$$

The recurrence still permits an isolated index with an anomalously large
$v_p(F_N)$, flanked by controlled neighbors.  It therefore does not prove
the pointwise bound $v_p(\beta_N)\ge N-O(\log N)$ at every odd $N$.

The proof, exact verifier, and frozen result are in
sources/machin_fixed_bc1_exceptional_digits.md,
scripts/machin_fixed_bc1_exceptional_digits.py, and
results/machin_fixed_bc1_exceptional_digits.json.  The independent audit in
sources/independent_machin_fixed_bc1_exceptional_digits_audit.md reimplemented
the complete $6\,825\,959$-index enumeration, reproduced the result file
byte for byte, checked all three next-digit certificates, and forced explicit
handling of zero values in the recurrence before acceptance.

## 2026-08-26 — $n$-dependent numerators over a fixed denominator

The fixed-kernel obstruction has now been extended to numerator polynomials
that vary with $n$, without any sign or analytic noncancellation
assumption.  Fix $Q\in\mathbb Z[x]$ with no zero on $[0,1]$, and consider

$$
J_n=\int_0^1x^n(1-x)^n\frac{P_n(x)}{Q(x)}\,dx.
$$

Assume that, on an infinite set of positive even indices, this moment is a
nontrivial rational $\pi$-form.  Since rational rescaling of $P_n$ does
not change its eventual primitive integer coordinate direction, write

$$
P_n=\lambda_n\widehat P_n,
$$

where $\widehat P_n\in\mathbb Z[x]$ is primitive, and put

$$
d_n=\deg\widehat P_n,\qquad
\mathcal H_n=\max\{2,\|\widehat P_n\|_1\},\qquad
S_n=n+d_n+\log\mathcal H_n.
$$

The accepted theorem is

$$
S_n=o(n\log n)
\quad\Longrightarrow\quad
|\Lambda_n^{\rm prim}|\longrightarrow\infty
$$

for the fully primitive, minimally coefficient-matched forms in
$1,e+\pi$.

The proof first isolates a universal arithmetic mechanism.  Salikhov's
finite irrationality measure for $\pi$, weakened to exponent $8$, gives
a fixed $c_\pi>0$ such that

$$
|A\pm B\pi|\ge c_\pi B^{-7}
$$

for every $A\in\mathbb Z$ and $B\ge1$.  The primitive exponential beta
form

$$
E_n=\frac1{n!}\int_0^1x^n(1-x)^ne^x\,dx=q_ne-p_n>0
$$

satisfies

$$
\gcd(p_n,q_n)=1,\qquad
q_n\ge n^n,\qquad
\frac{E_n}{q_n}\le e\,n^{-2n-1}.
$$

If $L_n=A_n+\varepsilon_nB_n\pi$ is the primitive moment direction, let
$d=\gcd(q_n,B_n)$, $q_n=dq_0$, and $B_n=dB_0$.  The unique minimal
positive coefficient multipliers are $B_0$ and $q_0$.  A prime-power
calculation, using both primitive pairs, proves that the new content $g$
created by matching satisfies

$$
g\mid d.
$$

This includes a possible zero constant coefficient and both signs of the
$\pi$-coordinate.  In the same-sign case the matched value is a positive
sum.  In the opposite-sign case the only possible cancellation has ratio

$$
\frac{E_n/q_n}{|L_n|/B_n}
\le c_\pi^{-1}e\,B_n^8n^{-2n-1}.
$$

Consequently, whenever $\log B_n=o(n\log n)$, both signs obey the
eventual uniform bound

$$
|\Lambda_n^{\rm prim}|
\ge\frac{c_\pi}{2}\frac{q_n}{B_n^9}.
$$

For fixed $Q$, rational pseudo-division of
$\widehat P_n(x)x^n(1-x)^n$ by $Q$, followed by integration of the
polynomial quotient, costs only

$$
\exp\!\bigl(O_Q(n+d_n+\log\mathcal H_n)\bigr).
$$

The integrations introduce
$\operatorname{lcm}(1,\ldots,2n+d_n+1)$, not a factorial.  The fixed
proper-fraction remainder spans only finitely many fixed periods.  Choosing
a rational basis of their actual span, rather than assuming any unproved
independence, gives

$$
B_n\le
\exp\!\bigl(O_Q(n+d_n+\log\mathcal H_n)\bigr).
$$

This height bound and $q_n\ge n^n$ prove divergence under
$S_n=o(n\log n)$.  The midpoint analysis is compatible with the same
scale: if the first nonzero symmetric term has order $2m_n$, then
$2m_n\le d_n+\deg Q$, and the exact beta factor is

$$
4^{-n}M_{n,m}
=
\frac{2(2m)!\,n!\,(n+m+1)!}
     {4^m m!(2n+2m+2)!}.
$$

Thus midpoint vanishing of order $O(n)$ supplies only an exponential
penalty and cannot evade the arithmetic obstruction.

The proof also gives a necessary escape dichotomy.  Any bounded subsequence
in this fixed-denominator class must have at least

$$
B_n\ge n^{\,n/9-o(n)}.
$$

If genuine opposite-sign cancellation is doing the work, the stronger
scale $B_n\gtrsim n^{n/4}$ is necessary.  Hence a candidate outside the
barrier must have

$$
n+d_n+\log\mathcal H_n=\Omega_Q(n\log n).
$$

These are necessary scales, not evidence that such a high-complexity
family succeeds.

The accepted proof is in
sources/n_dependent_fixed_denominator_kernel_barrier.md.  The independent
audit in
sources/independent_n_dependent_fixed_denominator_kernel_barrier_audit.md
checked Salikhov's quantifiers, the exponential recurrence and gcd, all
prime-power content cases, both matching signs, the projective
pseudo-division height including constant $Q$, the beta identities, and
the sparse-index escape dichotomy.  It found only an $n=0$ wording issue
in a factorial lower bound; the final source explicitly restricts that
bound to positive even $n$.

## 2026-08-26 — varying powers of $1+x^2$

The next denominator family is

$$
J_{n,k}=
\int_0^1\frac{x^n(1-x)^n}{(1+x^2)^k}\,dx.
$$

The first exact calculation corrected the premise of this route: these
moments do not always belong to $\mathbb Q+\mathbb Q\pi$.  For example,

$$
\frac{x^2(1-x)^2}{1+x^2}
=x^2-2x+\frac{2x}{1+x^2},
\qquad
J_{2,1}=\log2-\frac23.
$$

In general there are three coordinates,

$$
J_{n,k}\in
\mathbb Q+\mathbb Q\log2+\mathbb Q\pi.
$$

They can be calculated exactly by Gaussian partial fractions.  If

$$
a_{n,k,j}
=[z^{\,k-j}]
\frac{(i+z)^n(1-i-z)^n}{(2i+z)^k}
$$

is the coefficient of $(x-i)^{-j}$ and
$a_{n,k,1}=u_{n,k}+iv_{n,k}$, then

$$
J_{n,k}
=R_{n,k}+u_{n,k}\log2-\frac{v_{n,k}}2\pi,
\qquad R_{n,k}\in\mathbb Q.
$$

Baker's theorem, with the algebraic-constant conclusion supplied by Part
III of his linear-forms series, proves the rational linear independence of
$1,\log2,\pi$.  Hence the moment is a genuine rational $\pi$-form
exactly when

$$
u_{n,k}=0,
$$

and its $\pi$-coordinate is nonzero exactly when $v_{n,k}\ne0$.

The local expansion at $i$ uses only powers of $2$ in its denominators:

$$
2^{2k}a_{n,k,j}\in\mathbb Z[i].
$$

Integrating the higher pole terms costs
$\operatorname{lcm}(1,\ldots,k-1)$, while the polynomial part costs
only $\operatorname{lcm}(1,\ldots,2n+1)$.  Exact coefficient-norm
bounds therefore put all three rational coordinates on one denominator
with numerator and denominator bounded by

$$
\exp(O(n+k)).
$$

At every log-free, nonzero-$\pi$ index, the primitive
$\pi$-coefficient consequently satisfies

$$
B_{n,k}\le\exp(O(n+k)).
$$

Combining this bound with the universal minimal-matching calculation from
the fixed-denominator theorem gives

$$
|\Lambda_{n,k}^{\rm prim}|
\ge\frac{c_\pi}{2}\frac{q_n}{B_{n,k}^9},
\qquad q_n\ge n^n.
$$

It follows that every log-free, nonzero-$\pi$ sequence with

$$
k=o(n\log n)
$$

has primitive matched values tending to infinity.

There is a large automatic log-free region.  For even $n$ and $k>n$,
the substitution $x=\tan t$ gives

$$
J_{n,k}
=
\int_0^{\pi/4}
\sin^nt\,(\cos t-\sin t)^n
\cos^{\,2(k-n-1)}t\,dt.
$$

The integrand is a nonnegative trigonometric polynomial of even total
degree.  Every nonconstant even Fourier frequency has a rational integral
over $[0,\pi/4]$, whereas the constant coefficient contributes a
positive rational multiple of $\pi$.  Thus all such pairs are
automatically log-free and have positive nonzero $\pi$-coordinate.
In particular, no finite slope $k/n\to\alpha>1$ escapes.  Log-free
indices at slopes at most one are also covered whenever they occur.

For completeness, the analytic moments themselves have only exponential
finite-slope size.  If $a=k/n$, the strictly concave phase

$$
f_a(x)=\log x+\log(1-x)-a\log(1+x^2)
$$

has a unique saddle $\xi(a)\in(0,1)$.  Uniformly for $0\le k\le An$,

$$
J_{n,k}
=
\left(
\frac{\xi(k/n)(1-\xi(k/n))}
     {(1+\xi(k/n)^2)^{k/n}}
\right)^n
\sqrt{\frac{2\pi}{n[-f_{k/n}''(\xi(k/n))]}}
\left(1+O_A(n^{-1})\right).
$$

Thus the obstruction is arithmetic, not a failure of elementary Laplace
decay.  The first scale left open by this coarse theorem is
$k\asymp n\log n$.

The accepted proof is in
sources/varying_quadratic_power_kernel_barrier.md.  The independent audit
in sources/independent_varying_quadratic_power_kernel_barrier_audit.md
rederived the Laurent signs and factors, the corrected Baker
specialization, simultaneous coordinate heights, Fourier positivity,
uniform saddle estimate, and both primitive matching signs.  Its exact
checks reconstructed $432$ Laurent decompositions and matched $200$
Fourier and residue computations.

## 2026-08-26 — an explicit critical-scale Fourier barrier

The automatic even-$n$, $k>n$ region admits a sharper normalization
than the general Gaussian height estimate.  Put

$$
D=2k-2,\qquad \ell=k-n-1,
$$

and define the Gaussian-integer polynomial

$$
\mathcal G_{n,k}(y)=
i^{-n}(y-1)^n
\bigl((1+i)y+1-i\bigr)^n
(y+1)^{2\ell}.
$$

Writing its coefficients around the center as

$$
\mathcal G_{n,k}(y)
=\sum_{m=-(k-1)}^{k-1}C_m y^{m+k-1},
\qquad C_m=A_m+iB_m,
$$

the trigonometric kernel has the exact expansion

$$
H_{n,k}(t)
=2^{-D}\left[
C_0+2\sum_{m=1}^{k-1}
\bigl(A_m\cos(2mt)-B_m\sin(2mt)\bigr)
\right].
$$

Set

$$
N_m=
A_m\sin\frac{m\pi}{2}
-B_m\left(1-\cos\frac{m\pi}{2}\right)\in\mathbb Z,
$$

$$
L_k=\operatorname{lcm}(1,\ldots,k-1),
\qquad
T_{n,k}=\sum_{m=1}^{k-1}\frac{L_k}{m}N_m.
$$

Termwise integration gives

$$
J_{n,k}
=2^{-D}\left(
\frac{C_0}{4}\pi+\frac{T_{n,k}}{L_k}
\right).
$$

Therefore, if

$$
h_{n,k}=\gcd(4T_{n,k},L_kC_0),
$$

the primitive integer pair is exactly

$$
\left(
\frac{4T_{n,k}}{h_{n,k}},
\frac{L_kC_0}{h_{n,k}}
\right).
$$

The apparent denominator $2^{2k-2}$ cancels completely before matching.
This is the normalization gain that the general three-coordinate bound
does not see.

The constant Fourier coefficient is positive.  The full-period
nonnegative kernel and the elementary bound

$$
\left|\sin t(\cos t-\sin t)\right|
\le\gamma,\qquad
\gamma=\frac{1+\sqrt2}{2},
$$

give

$$
0<C_0\le2^{2k-2}\gamma^n.
$$

Together with the elementary prime-power estimate

$$
L_k\le16^{k-1},
$$

this yields the explicit primitive-coordinate bound

$$
B_{n,k}\le64^{k-1}\gamma^n.
$$

Only same-sign matching occurs here.  Salikhov's bound and the exact final
content calculation therefore imply

$$
|\Lambda_{n,k}^{\rm prim}|
\ge c_\pi\frac{q_n}{B_{n,k}^9},
\qquad q_n\ge n^n.
$$

Consequently,

$$
\log|\Lambda_{n,k}^{\rm prim}|
\ge
n\log n-9(k-1)\log64-9n\log\gamma+O(1).
$$

The primitive forms diverge whenever the right side has a fixed positive
proportion of $n\log n$.  In particular, the completely explicit region

$$
n<k\le\frac1{40}n\log n
$$

is excluded for all sufficiently large even $n$.  The constant is
certified elementarily: $\log2<0.7$ gives
$9\log64=54\log2<37.8<40$, while the remaining
$9n\log\gamma$ is lower order.

The accepted proof is in
sources/critical_quadratic_power_fourier_barrier.md, with its exact probe
in scripts/critical_quadratic_power_fourier_probe.py and frozen output in
results/critical_quadratic_power_fourier_probe.json.  The independent
audit in
sources/independent_critical_quadratic_power_fourier_barrier_audit.md
rederived every Fourier shift and sign, the exact primitive pair including
zero cases, the mean-value bound, the prime-power LCM inequality, the
matching content and exponent $9$, and the constant $1/40$.  It also
reproduced all $37$ archived exact cases and ran a separate $28$-case
coordinate cross-check.

## 2026-08-26 — the whole-space Chebyshev shortcut fails

After imposing $C(1)=B(1)$, the diagonal Machin coefficient space has
dimension $3n+2$.  It was therefore natural to ask whether it is an
extended Chebyshev space on $[0,1]$: the Padé remainder already has a
zero of order at least $3n+1$ at the origin, and a Chebyshev zero count
could then constrain any further endpoint zero.

The proposed whole-space statement is false already at $n=1$.  A basis
of the five-dimensional constrained space is

$$
1,\quad x,\quad e^x+G(x),\quad
(x-1)e^x,\quad (x-1)G(x),
$$

where

$$
G(x)=16\arctan(x/5)-4\arctan(x/239).
$$

Let $W(x)$ be its full $5$-by-$5$ Wronskian.  Exact
differentiation gives

$$
W(0)=
-\frac{935059672726675656}
       {2912107693477515625}<0,
$$

whereas

$$
W(1)=
\frac{72e}{
 542800770374370512771595361}
\left(
50807650153010910313192727\,e
-55199386641542198623868748
\right)>0.
$$

The last sign is elementary because the displayed rational coefficient
ratio is less than $2<e$.  Continuity forces an interior Wronskian zero.
A basis change multiplies the full Wronskian by one fixed nonzero
determinant, so this zero cannot be removed by choosing different
coordinates.  The constrained $n=1$ space is therefore not an extended
Chebyshev space.

This does not rule out a theorem for the distinguished one-dimensional
Padé line, selected residue classes, or a different integral
representation.  It rules out only the blanket whole-space zero-count
shortcut.

The exact proof is in
sources/constrained_chebyshev_shortcut_no_go.md.  The independent audit in
sources/independent_constrained_chebyshev_shortcut_no_go_audit.md
reconstructed the constrained basis, both endpoint determinants, their
signs, basis invariance, and the precise extended-Chebyshev implication.

## 2026-08-26 — exact diagonal remainder order on two residue classes

For the endpoint-matched diagonal Machin family, write

$$
R_n(z)=A_n(z)+B_n(z)e^z+C_n(z)G(z),
\qquad
C_n(1)=B_n(1),
$$

with all three polynomial degrees at most $n$ and

$$
R_n(z)=O(z^{3n+1}).
$$

The all-degree bordered-rank theorem already proves that the solution line
is one-dimensional and that $B_n(1)=C_n(1)\ne0$.  The next question is
whether the first unconstrained coefficient

$$
q_{3n+1,n}
=[z^{3n+1}]\bigl(B_n(z)e^z+C_n(z)G(z)\bigr)
$$

can vanish.

Parametrize the endpoint hyperplane by

$$
B=x+(z-1)\widetilde B,\qquad
C=x+(z-1)\widetilde C,
$$

where the two tilded polynomials have degree below $n$.  Appending the
first-free coefficient equation to the high Taylor equations gives a
square matrix $\mathcal T_n$.  Successive column differences and one
block permutation yield the exact determinant identity

$$
\det\mathcal T_n
=4^n\bigl(D_E+4(-1)^nD_G\bigr),
$$

where

$$
D_E=\det(E\mid Q),\qquad
D_G=\det(P\mid\Gamma)
$$

are the exponential/Machin complementary block determinants.

For $n\equiv0\pmod4$, write $R=n/2$.  A Laplace expansion of $D_E$
has one unique term of least $2$-adic valuation.  Its exponential row set
is

$$
S_0=\{2n+1,2n+2,\ldots,3n+1\},
$$

and the complementary Machin row set is consecutive.  The only competing
row set with the same factorial sum replaces $2n+1$ by $2n$; its
Vandermonde quotient $n+1$ is odd, but its opposite parity orientation
costs $2+2v_2(R)>0$ in the Machin minor.  All remaining terms lose at
least one factorial valuation.  Hence

$$
v_2(D_E)=v_0
$$

exactly.  The competing determinant satisfies

$$
v_2(D_G)-v_0
\ge
\phi(2n+1)-\phi(n)+\frac n2+2\phi(n/2)>0,
$$

where $\phi(m)=v_2(m!)$.  Thus the $4D_G$ term cannot cancel $D_E$.

For $n\equiv1\pmod4$, put $R=(n+1)/2$, which is odd.  The consecutive
Machin complement contains a bordered block with $R-1$ ordinary rows.
Its even size gives the equality case in the bordered-kernel valuation
theorem.  The sole factorial-sum competitor now pays

$$
v_2(n+1)=1
$$

in its Vandermonde.  Again $D_E$ has a unique least term, say of
valuation $v_1$, while

$$
v_2(D_G)-v_1
\ge
\phi(2n+1)-\phi(n)+(R-1)+2\phi(R-1)>0.
$$

Therefore

$$
\boxed{
q_{3n+1,n}\ne0
\quad\text{for every positive }n\equiv0,1\pmod4.}
$$

Equivalently,

$$
\operatorname{ord}_{z=0}R_n=3n+1
$$

on these two infinite residue classes.

The exact coefficient theorem does not imply endpoint nonvanishing:
later Taylor coefficients can cancel at $z=1$.  Nor does its determinant
control the cofactor $\Delta_A$, the endpoint gcd, or the effective
primitive height.  The decisive sufficient target remains

$$
H_C^*=o(5^{2n}),
$$

together with a cancellation-sensitive endpoint estimate.

The same source audits whether current quantitative $E$-value theorems
can rescue the separate nested-exponential Padé construction under the
temporary hypothesis

$$
s=e+\pi\in\overline{\mathbb Q}.
$$

For

$$
\Lambda_n=-Q_n(ie)e^{is}-P_n(ie),
$$

the exact Padé estimates give

$$
|\Lambda_n|
\asymp\frac{e^{2n+1}n!}{(2n+1)!},
\qquad
H_n=\frac{(2n)!}{n!}.
$$

Adamczewski--Faverjon's effective algebraic-independence measure applies
uniformly to the fixed pair

$$
ie^z,\qquad e^{isz},
$$

but specializes only to

$$
\begin{aligned}
\log|\Lambda_n|\ge{}&
-\exp\!\left(C_3(n+1)^4\log(n+2)\right)\\
&-128\sqrt2\,d^3(n+1)^2\log H_n,
\end{aligned}
$$

where $d=[\mathbb Q(s):\mathbb Q]$.  This permits values immensely
smaller than the actual scale $\exp(-\Theta(n\log n))$.

Expanding $\Lambda_n$ into $2n+2$ exponential functions and applying
Fischler--Rivoal gives a height exponent that itself grows like
$(2n+2)^{2d}$.  Moreover, its multiplicative constant depends on the
entire varying function vector, so the cited theorem supplies no uniform
constant along the sequence.  Their one-variable measure for
$P(e^\alpha)$ is inapplicable because the form genuinely involves the
two algebraically independent variables $e$ and $e^{is}$.

The accepted proof and measure comparison are in
sources/diagonal_machin_free_coefficient_and_measure.md.  The independent
audit in
sources/independent_diagonal_machin_free_coefficient_audit.md rederived
the determinant sign and factor, both parity-block equality cases
including $n=1$, the unique least terms and valuation gaps, and all
quantitative theorem hypotheses.  A second implementation in
scripts/independent_diagonal_machin_audit.py used exact
Fraction/Bareiss arithmetic rather than SymPy and reproduced the archived
determinants and valuations.

## 2026-08-26 — current $\pi$-measure sharpening of the matching barriers

The accepted primitive-matching arguments were re-run with the current
published irrationality measure

$$
\mu(\pi)\le 7.1032053341370017\ldots
$$

of Zeilberger and Zudilin.  Using only the weaker rational exponent
$\tau=36/5$, there is a fixed $c_\pi>0$ such that

$$
|A\pm B\pi|\ge c_\pi B^{-31/5}
\qquad(A\in\mathbb Z,\ B\ge1).
$$

The quantifiers are uniform over every integer numerator.  Irrationality of
$\pi$ supplies one positive constant for the finitely many small
denominators.

For the exact minimal matching of the primitive exponential beta form
$E_n=q_ne-p_n$ against a primitive form $A\pm B\pi$, write

$$
d=\gcd(q_n,B),\qquad q_n=dq_0,\qquad B=dB_0.
$$

The matching multipliers are $B_0,q_0$.  A prime-by-prime congruence,
valid for either sign and also when the matched constant is zero, proves
that the final content $g$ divides $d$.  Consequently the same-sign
primitive form satisfies

$$
|\Lambda_n^{\rm prim}|
\ge c_\pi\frac{q_n}{B^{41/5}}.
$$

In the opposite-sign branch, the possible cancellation ratio satisfies

$$
\frac{E_n/q_n}{|A\pm B\pi|/B}
\le c_\pi^{-1}e\,B^{36/5}n^{-2n-1}.
$$

Thus bounded escape requires at least

$$
B\ge n^{\,5n/41-o(n)}
$$

in general, while competitive opposite-sign cancellation requires the
larger scale

$$
B\ge n^{\,5n/18-o(n)}.
$$

For the even-$n$, $k>n$ automatic Fourier family, the accepted exact
height estimate

$$
B_{n,k}\le64^{k-1}
\left(\frac{1+\sqrt2}{2}\right)^n
$$

now gives divergence throughout

$$
n<k\le\frac1{35}n\log n.
$$

Indeed,

$$
\frac{41}{5}\log64
=\frac{246}{5}\log2
<\frac{861}{25}
<35,
$$

leaving a positive multiple of $n\log n$; the remaining
$\left((1+\sqrt2)/2\right)^n$ contribution is only $O(n)$.

The accepted standalone derivation is
sources/improved_pi_measure_matching_sharpening.md, SHA-256
9db7e8432631cf102d913b18e3bc74db72bfee634ab008a489dacab3bc6ff040.
The independent audit is
sources/independent_improved_pi_measure_matching_sharpening_audit.md,
SHA-256
197abd5ceebd5314eb1ab7ed1c6463f11b6dcb5b934c733e5e88abfcbb9f2d22.
It independently checked the published theorem's quantifiers, both signs,
the zero-constant edge case, all exponents, and the explicit $1/35$
margin.  This is a stronger obstruction theorem, not a proof about the
arithmetic nature of $e+\pi$.

## 2026-08-26 — positive pole-interpolating derivative kernel

A new positive common-kernel attempt was constructed from

$$
G(x)=16\arctan(x/5)-4\arctan(x/239)
$$

and

$$
G'(x)=\frac{80}{x^2+25}-\frac{956}{x^2+57121}.
$$

For positive even $n$, write $m=n/2$ and set

$$
a_n=125494837^m,\qquad b_n=25^m,
$$

$$
L_n(y)=(a_n-b_n)y+57121a_n-25b_n.
$$

The exact content is

$$
\delta_n=
\begin{cases}
2196,&m\text{ odd},\\
4392,&m\text{ even}.
\end{cases}
$$

Writing

$$
\ell_n(y)=L_n(y)/\delta_n,
\qquad
P_n(x)=x^{2n}(1-x^2)^n\ell_n(x^2)^2,
$$

Gauss's lemma makes $P_n$ primitive, and evenness of $n$ makes it
nonnegative on the real axis.  The interpolation identities are exact:

$$
P_n(5i)=P_n(239i)
=650^n\left(\frac{57096a_n}{\delta_n}\right)^2=:T_n.
$$

Consequently

$$
\int_0^1P_n(x)G'(x)\,dx=\rho_n+T_n\pi
$$

has no logarithmic coordinate, while

$$
\int_0^1P_n(x)e^x\,dx=q_ne-p_n>0
$$

is an integer exponential form.

Both coordinate pairs were reduced separately before matching.  If
$\bar q_n$ is the resulting primitive $e$-coefficient, positivity and
the derangement integral formula give a rational approximation satisfying

$$
0<e-\frac{\bar p_n}{\bar q_n}
\le
\frac{57123^2\,2^ne^{4n+7}}{(4n+4)^{4n+4}}.
$$

Euler's continued fraction supplies the uniform reduced-rational bound

$$
\left|e-\frac pq\right|
\ge\frac{c_e}{q^2\log(2q)}
\ge\frac{c_e}{q^3}.
$$

It follows without any formula for the exponential-pair gcd that

$$
\log\bar q_n\ge\frac43n\log n-O(n).
$$

By contrast, the primitive $\pi$-coefficient $B_n$ satisfies

$$
B_n\le C_0C_1^n.
$$

Under least positive coefficient matching, put

$$
d_n=\gcd(\bar q_n,B_n).
$$

A full prime-power congruence, including the zero matched-constant edge
case, proves that the final content $g_n$ divides $d_n$.  Salikhov's
finite irrationality measure then yields

$$
|\Lambda_n^{\rm prim}|
\ge c_\pi\frac{\bar q_n}{B_n^9}
\ge c\exp\left(\frac43n\log n-Cn\right)
\longrightarrow+\infty.
$$

Thus exact pole interpolation and positivity succeed analytically, but
the primitive coefficient scales rigorously force divergence.

The accepted theorem is
sources/positive_derivative_kernel_divergence.md, current SHA-256
c3b1b0493a66b781324c28014058675f92bf529ec46ff1eff87ce64af1e3965b.
The independent audit is
sources/independent_positive_derivative_kernel_divergence_audit.md,
SHA-256
4a38783099572a27934b5794cb52b4f9d072873a8dbe961cb5870e08f67c1eb2.
Its separate SymPy expansion and Euclidean-division implementation is
scripts/independent_positive_derivative_kernel_audit.py, SHA-256
ae7c56a46371e636224a32088bdf8e7f2d5acbb1b9ed0bfde979e8d66308317a,
with exact result SHA-256
c1544c2ca8b09188221c21a47e400f3005b9aa87a240922e6f6866ed8e7804d4.
The two independent implementations agree at every even
$2\le n\le20$, including nontrivial coefficient-matching gcds $29$
and $53$; those finite values are regression checks, not inputs to the
all-degree proof.

## 2026-08-26 — small-root continuation and the exact $N=2$ boundary

The corrected Rivoal simultaneous exponential--logarithm forms were
continued from the earlier $|1-\zeta_N|<1$ region to

$$
N\in\{3,4,6\},\qquad \eta_N=1-\zeta_N,
$$

using the exact logarithmic remainder

$$
R_{\log}(x)=(-1)^{c-1}x^{2c+d+1}
\int_0^1
\frac{u^c(1-u)^cH_{d,f}(u)}{(1-xu)^{c+1}}\,du.
$$

On every admissible proportional ray

$$
c=n,\qquad d=\lambda n,\qquad f=\mu n,
\qquad \lambda\ge2,\quad\mu\ge1,
$$

the Möbius coordinate $r=u/(1-u)$ supplies an explicit circular contour
in the lower half-plane through the lower saddle.  If
$r_*=Re^{i\theta}$, then $-\pi/N<\theta<0$.  Along the ray
$r=te^{i\theta}$, the logarithmic derivative of the phase modulus has a
positive denominator and numerator

$$
\begin{aligned}
P(t)={}&(\lambda+1)
+\bigl((\lambda+1)a+(2\lambda+1)b\bigr)t
+\lambda(1+2ab)t^2\\
&+\bigl((\lambda-1)a-b\bigr)t^3-t^4,
\end{aligned}
$$

where $a=\cos\theta$ and $b=\cos(\theta+2\pi/N)$.  For
$N=3,4,6$, every coefficient except the leading $-1$ is strictly
positive.  Descartes' rule gives exactly one positive root, so this saddle
is the unique strict maximum and the upper saddle has contour coefficient
zero.  A separate $O(1/n)$ endpoint-disk estimate makes the neighborhood
of zero superexponentially small; $(1-u)^n$ suppresses the other endpoint.
The local complex Gaussian coefficient is nonzero.  Consequently the
combined unscaled forms are eventually nonzero and

$$
\frac1n\log|\Lambda_N|\longrightarrow\rho_N(\lambda,\mu)>0.
$$

The global minima occur at $(\lambda,\mu)=(2,1)$, with displayed rates

$$
\rho_3=4.1013834804\ldots,\qquad
\rho_4=3.1371417992\ldots,\qquad
\rho_6=1.6482803903\ldots.
$$

At the boundary root $N=2$, the lower-lip Sokhotski--Plemelj value is

$$
R_{\log}^{+}(2)=i\pi A(2)-B(2),
$$

which is exactly the branch isolating $e+\pi$.  Exact coefficientwise
clearing and a complete case split prove the all-index obstruction

$$
q_2\Lambda_2^+\ne0\quad\Longrightarrow\quad
|q_2\Lambda_2^+|\ge1.
$$

For $N=3,4,6$, a separate exact scan covers $441$ triples at each root.
Its only coefficientwise-cleared value below one is

$$
(N;c,d,f)=(6;0,3,0),\qquad q_6=9,
\qquad |9\Lambda_6|=0.6483138992\ldots.
$$

The off-diagonal cyclotomic factors prevent a norm contradiction: in the
field-disjoint case their exact four-place product is

$$
169s^4-2028s^3+6093s^2-54s+81
=187.5555998647\ldots>1,
\qquad s=e+\pi.
$$

If the intersection is $\mathbb Q(\sqrt3)$, the missing factors instead
contain uncontrolled conjugates of $s$.  The theorem also treats the main
fixed-parameter boundaries, including the valuation obstruction
$q_6(0,d,0)\ge d^2/2$, but deliberately leaves sparse coupled
non-proportional sequences open.

The accepted source is
`sources/small_root_of_unity_exp_log_continuation.md`, SHA-256
`c86638fbcc6fbd109d5852c3f04c2035df5c6f1636fe0c2c087b3c7e8d09753d`.
The independent audit is
`sources/independent_small_root_of_unity_exp_log_continuation_audit.md`,
SHA-256
`5733bb5c5f26a36089ad0d9e668a9439ade2e0ae15009583275dc34af2caf4fe`.
Its independent exact script and frozen output have SHA-256 values
`b548cc62d932ce7b01be88f13dbbc8e9d94bda4322ceade1dcbfdf377dc93c7f`
and
`7f0066d85679c11763e27a6a72d0283c061d04f123db22d04096c6c9c604eeeb`,
respectively.  This closes several natural root-of-unity regimes; it does
not prove any arithmetic classification of $e+\pi$.

## 2026-08-26 — integral-jet Möbius pullback and strong cofactor content

A new rational-coefficient period representation is

$$
F(z)=4\arctan\frac{z}{2-z}
=4\int_0^z\frac{dt}{t^2-2t+2},
\qquad F(1)=\pi.
$$

Its nearest singularities are $1\pm i$, so its exact Taylor radius is
$\sqrt2$.  More importantly, every derivative jet is integral:

$$
\tau_k=F^{(k)}(0)
=4(k-1)!2^{-k/2}\sin\frac{k\pi}{4}\in\mathbb Z.
$$

Equivalently,

$$
\begin{aligned}
\tau_{4q+1}&=(-1)^q\frac{2(4q)!}{4^q},&
\tau_{4q+2}&=(-1)^q\frac{2(4q+1)!}{4^q},\\
\tau_{4q+3}&=(-1)^q\frac{(4q+2)!}{4^q},&
\tau_{4q+4}&=0.
\end{aligned}
$$

For the diagonal endpoint-matched system

$$
A_n+B_ne^z+C_nF=O(z^{3n+1}),
\qquad C_n(1)=B_n(1),
\qquad \deg A_n,\deg B_n,\deg C_n\le n,
$$

the high-jet-plus-endpoint matrix is integral without any row clearing.
Order its columns as $B_0,\ldots,B_n,C_0,\ldots,C_n$.  Its high rows
$k=n+1,\ldots,3n$ contain $(k)_j$ and $(k)_j\tau_{k-j}$, and its endpoint
row is $(-1,\ldots,-1\mid1,\ldots,1)$.

The independently audited all-degree cofactor theorem defines

$$
\Lambda_n=\left(\prod_{j=0}^{n-1}j!\right)^2,
$$

$$
\Gamma_n=\prod_{t=0}^{n-2}
2^{\delta_t}\operatorname{odd}(t!),
\quad
\delta_t=2q_t+1-s_2(q_t),
\quad q_t=\left\lfloor\frac{t+1}{4}\right\rfloor,
$$

and

$$
\Omega_n^*=\prod_{s=1}^{n-1}
2^{\epsilon_s}\operatorname{odd}((s-1)!),
\quad
\epsilon_s=2d_s-s_2(d_s),
\quad d_s=\left\lfloor\frac{s-1}{4}\right\rfloor.
$$

Every signed maximal cofactor is divisible by

$$
\Xi_n=\Lambda_n\Gamma_n\Omega_n^*,
\qquad
\log\Xi_n=2n^2\log n+O(n^2).
$$

The proof expands along the endpoint row, so exactly two original columns
are omitted.  The factor $\Lambda_n$ comes from literal $j!$ column
factors, $\Gamma_n$ from the exact jet valuations in at least $n-1$
retained $C$-columns, and $\Omega_n^*$ from distinct residual row
assignments after those column factors have already been removed.  This
successive extraction is why the three factors multiply without a hidden
coprimality premise or double counting.

Hadamard's inequality gives the raw bound

$$
\log|\text{maximal cofactor}|
\le\frac72n^2\log n+O(n^2).
$$

Consequently, whenever the matrix has full row rank, its primitive high
kernel satisfies

$$
\log H(B_n,C_n)
\le\frac32n^2\log n+O(n^2).
$$

This is a genuine normalization improvement but remains much larger than
the fixed geometric decay available from radius $\sqrt2$.

A separate exact certificate at the prime $65521$ proves, for every
$1\le n\le100$, full row rank and a nonzero first unconstrained jet.  For
$2\le n\le100$, both endpoint coordinates are nonzero modulo that prime;
the degree-one triple is the exact endpoint-zero degeneracy

$$
A=2(1-z),\qquad B=-2(1-z),\qquad C=1-z.
$$

The finite primitive endpoint decades for $n=2,\ldots,15$ are

$$
0,4,10,18,31,47,65,87,112,141,174,210,249,293.
$$

At $n=15$, the exact common cofactor gcd has $263$ digits, the proved
$\Xi_{15}$ has $218$ digits, and the remaining quotient has $46$ digits.
Direct Smith computations through $n=14$ agree with the cofactor gcd, but
no all-degree Smith formula is claimed.

Among real Möbius pullbacks fixing $0$ and $1$, this choice uniquely
maximizes the singular radius: for

$$
u_a(z)=\frac{z}{a-(a-1)z},
$$

the radius of $4\arctan u_a(z)$ is

$$
\rho(a)=\frac{a}{\sqrt{(a-1)^2+1}}\le\sqrt2,
$$

with equality only at $a=2$.  A radius-$4$ hypergeometric representation
of $\pi$ was also identified, but its jets have exact valuation
$v_2(H^{(m)}(0))=-3m$, displaying the opposing denominator cost.

The main construction note is
`sources/pi_g_function_pullback_route.md`, SHA-256
`1db63fcc525063798c08650488dc28b0c1ba4bbae44c752fe1cc2aaa37908410`.
The focused endpoint analysis is
`sources/endpoint_matched_mobius_hp_rank_and_content.md`, SHA-256
`4be95f24d1a06fd93616e0ebe2c9564cde8826a8d9345a2ff82e9349f99c0111`.
The independent divisor audit is
`sources/independent_strong_pullback_cofactor_divisor_audit.md`, SHA-256
`8ca33ee5338a8be0b0571be1e91e0517d8e554b579c2375e06db683b6bafb0b1`.
The exact probe and degree-$15$ result have SHA-256 values
`d812595d92abff631366a889aa8c6e8a13402ace684c93c1fffe56b8032981b6`
and
`ff0405c94960eb27940b4684de0dcab05cab5b6dd0311abc27f5ed1d85a7691b`,
while the Smith probe and degree-$14$ result have SHA-256 values
`dcde8ac063fe704b5eaa3caaee3ef5a4bebf44d24192b7da9f4fd9e5901ee3fa`
and
`cfc05cc5782a14bc9ff427b60ce96276d34e44ea511e771c1907a500fde84213`.
These results remove a substantial arithmetic bottleneck; they do not make
the endpoint forms small and do not classify $e+\pi$.

## 2026-08-26 — softened singularity endpoint family

An explicit unbalanced subfamily of the integral-jet pullback was isolated.
Let

$$
F(z)=4\arctan\frac{z}{2-z},\qquad
D(z)=z^2-2z+2,
$$

and write

$$
e^{-z}D(z)^nF(z)=
\sum_{k\ge0}\eta_{n,k}\frac{z^k}{k!},\qquad
H_{n,b}=\sum_{k=0}^b\frac{\eta_{n,k}}{k!}.
$$

Taking $C=D^n$, taking $A$ constant, choosing $\deg B\le b$ for maximal
Taylor cancellation, and imposing $B(1)=C(1)=1$ gives the exact
integer-coordinate endpoint form

$$
L_{n,b}=U_b(e+\pi)-V_{n,b},
\qquad
U_b={!b},\qquad
V_{n,b}=b!(1+H_{n,b}).
$$

Every $\eta_{n,k}$ is integral.  If

$$
g_{n,b}=\gcd(U_b,V_{n,b}),
$$

then $L_{n,b}/g_{n,b}$ is the completely primitive form.  The exact tail
identity is

$$
L_{n,b}=b!\left(\rho_{n,b}-(e+\pi)\epsilon_b\right),
$$

where $\rho_{n,b}=\pi/e-H_{n,b}$ and
$\epsilon_b=e^{-1}-\sum_{k=0}^b(-1)^k/k!$.

The independently audited no-decay results are:

1. for every fixed $b\ge2$, the primitive form diverges at order
   $2^nn^{b-1}$;
2. for every proportional ray $b/n\to\lambda$ with $0<\lambda<2$, an
   explicit positive saddle and horizontal logarithmic cuts prove
   exponential growth, which survives unrestricted gcd removal;
3. for every fixed integer $d$,

   $$
   H_{n,2n+d}\sim
   (-1)^{d+1}\frac{\sqrt\pi}{2}
   e^{2\sqrt{2n}}(\sqrt{2n})^{-d-3/2};
   $$

4. for every fixed $0<\delta<2$, the same conclusion holds uniformly in

   $$
   0\le b-2n\le
   (2-\delta)\frac{\sqrt{2n}}{\log\sqrt{2n}}.
   $$

On the cuts $w=-1-x\pm i$, the decisive exact inequality is

$$
|w|^4-|w^2+2w+2|^2
=4(x^3+x^2+2x+1)>0.
$$

The audit explicitly checks the two cut jumps, contour orientations, the
pole at $w=-1$, branch/pole collisions, the moving saddle, its total
variance, and the constant and sign in the critical asymptotic.  Its
essential limitation is equally explicit: the cut gap tends to one as
$\lambda\uparrow2$.  Thus arbitrary approaches to the critical ratio
outside the displayed window, and the range $b/n>2$, remain open.  In those
regimes the unresolved arithmetic issue is a sufficiently strong uniform
upper bound for

$$
\gcd\!\left({!b},b!(1+H_{n,b})\right).
$$

An independent exact recomputation checks all $7{,}260$ pairs
$1\le n\le60$, $2\le b\le4n$ using a separate jet formula and directed
rational intervals.  The global finite minimum is at $b=2$ for every
$2\le n\le60$ (and at $b=3$ for $n=1$); this is a finite certificate, not
an asymptotic theorem.

The construction note is
sources/softened_singularity_endpoint_subfamily.md, SHA-256
1ff8ef74ebd60cc89416771a972d14ac52a235ef736808b7583217dbbf30d5ed.
The independent audit is
sources/independent_softened_singularity_endpoint_audit.md, SHA-256
d645d079907479112f3e52007384f768da95c1b3cfab1fc095576ab770c0c499.
The original and independent scripts have SHA-256 values
47e83965ecf8dc858732b8cf32e97a3904fa6fdf8df6e9f39714179939827b03
and
d874ea89a168a423ab48a64eb2f8e6e30add90ffcad16f92c14731a50f664404;
their JSON results have SHA-256 values
a5c18e1ddab42fff383a0f53899c2cb5d52c111f6423eba54d1ffdab57107c0d
and
7a0deb5a45916667894bd1f854ac5d4c35c8a8fbfbd37ee90c2b0350d3ed3ed3.
This eliminates a broad, explicit family but proves no classification of
$e+\pi$.

## 2026-08-26 — quadratic pullbacks and the radius/arithmetic tradeoff

A higher-degree rational substitution gives the explicit family

$$
u_p(z)=\frac{(p-1)z}{p-z^2},
\qquad
F_p(z)=4\arctan u_p(z),
\qquad F_p(1)=\pi.
$$

Its derivative is

$$
F_p'(z)=
\frac{4(p-1)(p+z^2)}
{z^4+(p^2-4p+1)z^2+p^2}.
$$

The singularities are the preimages of $\pm i$.  For $p=2,3,4,5$, all
nearest preimages have modulus $\sqrt p$.  For integral $p\ge6$, the
smaller squared radius is

$$
\rho(F_p)^2=
\frac{p^2-4p+1-
\sqrt{(p^2-4p+1)^2-4p^2}}2;
$$

it equals $4$ at $p=6$ and is below $4$ thereafter.  Consequently

$$
\max_{p\in\mathbb Z,\ p\ge2}\rho(F_p)=\sqrt5,
$$

uniquely at $p=5$.

The gain in radius is accompanied by exact prime-power jet denominators.
If

$$
c_{p,0}=1,\qquad c_{p,1}=-p^2+5p-1,
$$

$$
c_{p,m}=-(p^2-4p+1)c_{p,m-1}-p^2c_{p,m-2},
$$

then

$$
F_p^{(2m+1)}(0)
=\frac{4(p-1)(2m)!\,c_{p,m}}{p^{2m+1}},
\qquad
F_p^{(2m+2)}(0)=0.
$$

For every odd prime $p$, $c_{p,m}\equiv(-1)^m\pmod p$, so the exact
reduced jet denominator is

$$
p^{2m+1-v_p((2m)!)}.
$$

For the radius-maximizing $p=5$, its exponent is
$3m/2+O(\log m)$.  The exact exponents for $p=2$ and $p=4$ are,
respectively,

$$
\max(0,s_2(m)-1)
\quad\hbox{and}\quad
2m+s_2(m).
$$

An independent exact computation rederived all $32$ diagonal
endpoint-matched systems with $p=2,3,4,5$ and $1\le n\le8$.  Every matrix
has full row rank, every projective kernel is one-dimensional, and every
first unconstrained coefficient is nonzero.  All reduced endpoint forms
are certified nonzero, but their magnitudes grow rapidly; at $n=8$ their
base-ten decades are $90,105,91,118$ for $p=2,3,4,5$.

A second finite search considers reduced maps

$$
u(z)=\frac{z(A+Bz)}{C+Dz+Ez^2},
\qquad A+B=C+D+E,
$$

in the displayed coefficient box, with a nonvanishing denominator on
$[0,1]$.  It exactly tests $53{,}036$ primitive safe-path candidates,
skips $517$ reducible parameterizations, and finds $16{,}158$ candidates
with integral derivative jets through order $25$.  No computed radius
exceeds $\sqrt2$.  The combinatorial enumeration and integrality decisions
are exact and independently reproduced; the final ranking of algebraic
root moduli uses high-precision floating arithmetic and is therefore
recorded only as a finite diagnostic.

The construction note is
sources/quadratic_arctan_pullback_arithmetic_radius.md, SHA-256
9a0a4f3fdb7b86704b80b208350753ad1233af891480d4513903fccae0e21095.
The independent audit is
sources/independent_quadratic_arctan_pullback_audit.md, SHA-256
7251c62d2c59152af579e92c359c5af4a5d378cce51ada9bfe36a0043ab3f1b3.
The diagonal script/result hashes are
c7c4101104a7f91f74af197e1b530fbef36694e914a2b73768314d4eecaa2fa6
and
5d68f547b8e70ab98cbee54036df9ba2d14a5d0948cda54043d25cab89081720.
The broad-search script/result hashes are
9aedaafe9662866aa206aab84f58c863fb9714eeb28057a4b6e1da806e888b37
and
da45bdcbc7ae8959e0101bd18856f36617044d75d48ae77a449837ef39c44368.
The independent audit program/result hashes are
28a203d76a2ff9ec3ab71deea070a2de3bbfcf200846757a050ca6f248afb196
and
0d8be7d1cb1a1f45d8a72473a2012776feb5e94a4ca95297720bc998fc6b0697.
This gives a quantified analytic/arithmetic tradeoff, not a proof about
$e+\pi$.

## 2026-08-26 — constant-$B,C$ ray for every quadratic pullback

The non-diagonal degree ray

$$
\deg A\le a,\qquad B=C=1,
$$

admits a complete primitive no-decay theorem for every fixed integral
$p\ge2$.  With

$$
F_p(z)=4\arctan\frac{(p-1)z}{p-z^2},
$$

maximal cancellation forces

$$
A_a(z)=-T_a(e^z+F_p(z)).
$$

Put

$$
E_a=\sum_{k=0}^a\frac1{k!},\qquad
\Pi_{p,a}=T_aF_p(1),\qquad
R_{p,a}=E_a+\Pi_{p,a}=\frac{P_{p,a}}{Q_{p,a}}
$$

in lowest terms.  Clearing the entire polynomial triple and then removing
the complete endpoint gcd gives exactly

$$
\mathcal L_{p,a}=Q_{p,a}(e+\pi)-P_{p,a}.
$$

The proof has two separate arithmetic inputs.  First, the continued
fraction of $e$ and its Taylor-tail upper bound show that the reduced
denominator $q_a$ of $E_a$ satisfies

$$
\log q_a\ge\frac12a\log a-O(a).
$$

Second, the exact rational expansion

$$
F_p(z)=
\sum_{m\ge0}
\frac{4(p-1)c_{p,m}}{p^{2m+1}(2m+1)}z^{2m+1}
$$

shows that the reduced denominator $D_{p,a}$ of $\Pi_{p,a}$ has

$$
\log D_{p,a}=O_p(a).
$$

Because $E_a=R_{p,a}-\Pi_{p,a}$,

$$
q_a\mid\operatorname{lcm}(Q_{p,a},D_{p,a}),
$$

and therefore

$$
\log Q_{p,a}\ge\frac12a\log a-O_p(a).
$$

Finally, the exponent-$36/5$ rational approximation bound for $\pi$ gives

$$
|\pi-\Pi_{p,a}|\ge\exp(-O_p(a)),
$$

whereas the exponential Taylor tail is
$|e-E_a|=\exp(-a\log a+O(a))$.  The latter cannot cancel the former.
Consequently

$$
\boxed{
|\mathcal L_{p,a}|
\ge\exp\!\left(\frac12a\log a-O_p(a)\right)
\longrightarrow\infty.}
$$

The independent audit verifies the exact endpoint reduction, the
denominator-transfer divisibility, both irrationality-measure inputs, and
all $404$ supplemental cases with $p=2,3,4,5$ and $0\le a\le100$.

The theorem source is
sources/quadratic_arctan_constant_bc_ray.md, SHA-256
9c4b35483a592857f1eab25741fc8ae5b813a5110df0f7212d77b9ed658b091a.
The independent audit is
sources/independent_quadratic_arctan_constant_bc_ray_audit.md, SHA-256
9ec0a7522c1574ac5284f25acaeabd38c8656bfac140e4bb6fae5f80495a01cc.
Its independent script/result hashes are
9cbb4ea5d5571406b70ae8b9aa6cea1badb644bd0d26496759ac8921d23420e1
and
de96a55d12bc72c6da24b4838cc4fd53f4c86bc65d8e2f0dffc17c4109e5b58e.
This eliminates one complete non-diagonal ray, not the full quadratic
Hermite--Padé cone.

## 2026-08-26 — complete nonproportional small-root classification

The analytic-continuation theorem for the corrected Rivoal
exponential--logarithm forms now covers every admissible parameter sequence,
not only proportional rays.  In the notation of the preceding continuation
note,

$$
c,d,f\in\mathbb Z_{\ge0},\qquad d\ge2c,\qquad f\ge c,
$$

and $q_N(c,d,f)$ is the least positive rational integer which clears both
coordinates of

$$
\Lambda_N(c,d,f)=U_N(e+\pi)+V_N
$$

in the integral basis of $\mathbb Q(i,\zeta_N)$.  Along every admissible
sequence with $\max(c,d,f)\to\infty$, the independently audited theorem is

$$
q_3|\Lambda_3|\longrightarrow\infty,\qquad
q_4|\Lambda_4|\longrightarrow\infty,
$$

and

$$
\liminf q_6|\Lambda_6|\ge\frac6{e^2}.
$$

The last constant is sharp for the unscaled edge
$c=f=1$, $d\to\infty$.  The other apparently dangerous $N=6$ edge
$c=f=0$ has raw size asymptotic to $6/(e^2d)$, but exact clearing gives
$q_6\ge d^2/2$.

The proof exhausts compact projective slopes, $f/d\to\infty$ with
$c/d$ bounded away from zero, $c=o(d)$ including a moving saddle-to-endpoint
band, fixed $d\ge1$ with $f\to\infty$, and the exceptional fixed edge
$c=d=0$, $f\to\infty$.  Runckel's zero theorem supplies nonvanishing of the
fixed integral on the fixed-$d$ faces.  On the exceptional edge,

$$
\Lambda_N(0,0,f)
=2i\left(e+\pi-\sum_{n=0}^f\frac1{n!}\right)\longrightarrow2\pi i,
$$

while

$$
q_N(0,0,f)=
\operatorname{den}\left(2\sum_{n=0}^f\frac1{n!}\right)\longrightarrow\infty.
$$

The denominator limit follows because the displayed rationals are distinct,
strictly increasing, and bounded, whereas a bounded interval contains only
finitely many rationals whose reduced denominator is at most any fixed
constant.

Three draft gaps were found and repaired before acceptance: a missing moving
endpoint band, a circularly stated exponential-remainder comparison, and an
incorrect raw-divergence claim on the last exceptional edge.  The final
independent audit accepts the repaired source without a residual sparse cone.

The frozen theorem, audit, script, and result SHA-256 values are,
respectively,

$$
\begin{aligned}
&58e800337a182eec76cd26efb6e0134f0b6fc1a0ad6efe6e765407c07c3f6af9,\\
&e3e77d93203191d5fefaf5d6df54fc78a2613304368582dfc447b73611893f22,\\
&077c9abf58ec20c93201fc569dbfb2ef175cc8329a4c2f8c90cd5e7a63dbef89,\\
&125508dd27fa218024dda2ad56f455bc5249535c940c4d9fc0dfd6043e615ec3.
\end{aligned}
$$

The expanded $4096$-case-per-root scan has SHA-256
c4b64bba9b8572e8b0a5d46e467fd08382818d3a25afd0c054a7b189cabe9566.
This closes the distinguished local family, but does not bound all algebraic
conjugates of a hypothetical algebraic $e+\pi$ and therefore supplies no
global norm contradiction.

## 2026-08-26 — first larger-radius composition with integral jets

Let

$$
F(w)=4\arctan\frac{w}{2-w},\qquad
\phi(z)=z-\frac{z^3}{6}+\frac{5z^4}{24}-\frac{z^5}{24},
\qquad G=F\circ\phi.
$$

Then $\phi(0)=0$, $\phi(1)=1$, and its nonzero derivative jets at zero are
$1,-1,5,-5$, all integral.  Because every derivative jet of $F$ is also
integral, Faà di Bruno's formula proves

$$
G^{(n)}(0)\in\mathbb Z\qquad(n\ge0),
$$

while $G(1)=\pi$.

Every solution of $\phi(z)=1\pm i$ is a genuine logarithmic singularity:
if the relevant denominator factor in

$$
G'(z)=
\frac{4\phi'(z)}
 {(\phi(z)-(1+i))(\phi(z)-(1-i))}
$$

has multiplicity $m$, the numerator has multiplicity exactly $m-1$.
An exact Schur--Cohn recursion at radius $\sqrt2$ gives the five positive
gaps

$$
\frac{35}{18},\quad
\frac{919}{324},\quad
\frac{90755}{13122},\quad
\frac{31025233225}{816293376},\quad
\frac{20206728833189212829375}{60719765548297125888}.
$$

It follows rigorously that $\rho(G)>\sqrt2$.  High-precision roots place the
nearest singularity at
$1.4597454685987641723304\ldots$, but this decimal is diagnostic only.

The exact diagonal endpoint-matched systems have full row rank, nullity one,
and nonzero first-free coefficient for every $1\le n\le15$.  Their fully
reduced endpoint decades are

$$
0,2,9,19,34,53,77,106,138,176,219,263,318,374,439,
$$

so the analytic radius improvement does not produce small primitive forms in
this degree allocation.

The frozen source/certificate/result/HP-script/HP-result hashes are

$$
\begin{aligned}
&f16d9872d452af37e67f361c0435ac6197066680ed699281b2c8b96de95964eb,\\
&c0ac1d342c94f24796f2bc02ef996e12aa25816ebecbe157ffa7694e73cb8824,\\
&6118a7152c964d957bccb4342f59a24c5767eccebc70f7fb8980dc30787aee5d,\\
&62d4ed61ff7876319a39a5f9da691673fdbb717054c68fe063aca70c47e8e5a4,\\
&ec590212db0b7a3b40c896db7f9b822594c023c43e9c839d9e4f8644a5aa1bae.
\end{aligned}
$$

The independent audit/source-script/result hashes are

$$
\begin{aligned}
&4b965b6f5a2cde5a828a7e8da928871fffb5255355bff75e49a081e7cc7ac351,\\
&8bfa7cea37f8f3541e4e6243dd19658314aaa8cb6e57cffe52e5f623973389af,\\
&b66c92a9c3316a4adb6e2ef1edee4160242c0efbeb125403fbfc738843582455.
\end{aligned}
$$

This is a new exact analytic option, not a conclusion about the arithmetic
nature of $e+\pi$.

## 2026-08-26 — an integral-jet pullback with radius beyond $3/2$

A sparser endpoint-fixing composition improves the certified radius again:

$$
\phi_8(z)=z+\frac{z^7-z^8}{140},\qquad
G_8(z)=4\arctan\frac{\phi_8(z)}{2-\phi_8(z)}.
$$

The only nonzero derivative jets of $\phi_8$ at zero are

$$
\phi_8'(0)=1,\qquad
\phi_8^{(7)}(0)=36,\qquad
\phi_8^{(8)}(0)=-288.
$$

Thus Faà di Bruno proves all-order integrality of the derivative jets of
$G_8$, while $\phi_8(0)=0$, $\phi_8(1)=1$, and $G_8(1)=\pi$.

For $q(z)=\phi_8(z)-(1+i)$, reverse at the rational radius $r=3/2$:

$$
w^8q(r/w)
=-(1+i)w^8+\frac32w^7
 \frac{(3/2)^7}{140}w-\frac{(3/2)^8}{140}.
$$

An exact normalized Schur--Cohn recursion over $\mathbb Q(i)$ has eight
strictly positive rational gaps.  Consequently every preimage of $1+i$,
and by conjugation every preimage of $1-i$, lies outside $|z|=3/2$.
Multiplicity cannot cancel these points: the chain-rule derivative has a
simple pole over every preimage.  Hence

$$
\boxed{\rho(G_8)>\frac32.}
$$

The nearest-root modulus

$$
1.5598556036265734152460990842856358\ldots
$$

is a high-precision diagnostic only; the strict bound is entirely rational.

All exact diagonal endpoint-matched matrices through $n=15$ have full row
rank, nullity one, and a nonzero first-free coefficient.  The $n=1$ endpoint
form vanishes identically.  The base-ten decades of the nonzero fully reduced
forms for $n=2,\ldots,15$ are

$$
0,7,15,26,44,64,89,119,150,191,233,281,331,385.
$$

The analytic gain therefore remains insufficient in the diagonal degree
allocation.

The frozen source, exact radius script/result, and exact HP script/result
SHA-256 values are

    0f1a41bb40ec457e51f1b0c1fa5299de784f93a3c7f92bc372bcad2fff7e7b87
    ed1e0e6c92392f0fa27f5fbe6e00603151c22ed1ec05d3eaaed9e0211ae7fce4
    b3bbdda30c993a122dc056cc137689ee9281d4ecc11efabac69174891c348e23
    f7cb212ebb4b9e79cc08486c8d090e36e9245144e24ffc06aca120699149963d
    831626a38451e3a060f1e790038a27935c226210cb6fc4bf0c4fae448f6e772d

The independent audit note/script/result hashes are

    23d80774ad8946ace2031eec2330abc11b894c1cf0a41d787db89faaf3f45369
    3802bb756fe0c01b592e7547896cdb3eee8e1ba56088ff2b7d22ce26b4394f29
    08b1d5ef58f94624dad47773377bdc7dce822347adfe994f56811e68f13e55af

The audit independently reproduced all eight Schur constants and gaps, all
$15$ HP records, the exact endpoint intervals, and the numerical root
diagnostic.  No all-degree primitive-height or endpoint-decay result follows.

## 2026-08-26 — universal hyperbolic ceiling for holomorphic pullbacks

There is an absolute analytic limit on how far an endpoint-fixing
holomorphic reparametrization can push both singularities of

$$
F(w)=4\arctan\frac{w}{2-w}.
$$

Let $\Omega=\mathbb C\setminus\{1-i,1+i\}$.  The affine map

$$
T(w)=\frac{w-(1-i)}{2i}
$$

sends $\Omega$ to $\mathbb C\setminus\{0,1\}$ and sends the endpoint pair
$(1,0)$ to $(1/2,(1+i)/2)$.  Write

$$
\tau_1=i\frac{K((1-i)/2)}{K((1+i)/2)}=x+iy.
$$

The modular lambda function is the universal cover with deck group
$\Gamma(2)$.  Conjugation gives $|\tau_1|=1$.  If
$\gamma=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$ lies
in $\Gamma(2)$, then $a,d$ are odd and $b,c$ are even, and

$$
\cosh d_{\mathbb H}(i,\gamma\tau_1)
=\frac{|a\tau_1+b|^2+|c\tau_1+d|^2}{2y}.
$$

Each squared term in the numerator is at least one by parity and
$|\tau_1|=1$; the identity transformation attains their sum two.  Hence the
quotient distance $\delta$ satisfies

$$
\cosh\delta=\frac1y.
$$

If $\phi(0)=0$, $\phi(1)=1$, and $\phi$ avoids $1\pm i$ on $|z|<R$,
Schwarz--Pick with curvature $-1$ gives

$$
\delta\le2\operatorname{artanh}\frac1R.
$$

Therefore

$$
\boxed{
R\le R_*=\coth\frac\delta2
=\sqrt{\frac{1+y}{1-y}}.}
$$

The factor $\pi/2$ cancels from $K$, and the rational series

$$
\frac{2K(z)}\pi=
\sum_{n\ge0}\frac{\binom{2n}{n}^2}{16^n}z^n
$$

at $z=(1+i)/2$ has a geometric rational tail majorant because
$|z|=1/\sqrt2<71/100$.  Exact summation through index $180$ and rational
interval propagation prove

$$
0.930296508588526<y<0.930296508588527
$$

and

$$
\boxed{R_*<5.262410788162386.}
$$

The longer diagnostic value is

$$
R_*=5.2624107881623850775528279\ldots.
$$

The bound is sharp among unrestricted holomorphic maps by lifting the
endpoint pair to the universal disk cover and matching its hyperbolic
distance with a disk automorphism.  It is not known whether integral-Hurwitz
polynomials can approach it.  For polynomial compositions, every preimage is
a genuine logarithmic singularity, so the same constant bounds the Taylor
radius of $F\circ\phi$.

The frozen theorem/script/result hashes are

    eb753d610e81ffd909c97ae1e4c128f7cbdaa7fd90607edf2d9817ab37faac17
    f83f5d27a302c8fa74b4b0def2ada68037c1f0e555f1031410f1fd9eb10d3846
    f981094e58a95ad0070939bda6f2db0b6ea0b2bdef9ad33ba6b379971bef9993

The independent audit note/script/result hashes are

    c86a68e6d688ea3190e237e9ffb4938a3005152b87b05f7cace67322ca741a09
    6807d6d433220c3c177b833763db169b087d7a5f0e3c715e4a957b1e5f461d19
    7cd4793f1c259735ceccf16543778e00ac075979a225eda131800f0771a7e93e

This theorem shows that singularity radius is a finite resource.  It does
not estimate primitive determinant height or prove anything about the
arithmetic class of $e+\pi$.

## 2026-08-26 — sparse multijet polynomial with radius beyond $1.747$

The endpoint-fixed integral-Hurwitz polynomial

$$
\phi(z)=z+\frac{46z^7(1-z)}{7!}
+\frac{213z^9(1-z)}{9!}
-\frac{763z^{10}(1-z)}{10!}
+\frac{20078z^{11}(1-z)}{11!}
$$

gives another exact analytic improvement.  Its derivative jets through
order $12$ are

$$
1,0,0,0,0,0,46,-368,213,-2893,28471,-240936,
$$

and all later jets vanish.  The base function

$$
F(w)=4\arctan\frac{w}{2-w}
$$

has integral derivative jets, so Faà di Bruno's formula proves that
$G=F\circ\phi$ has integral derivative jets in every order.  Endpoint
fixing gives $G(1)=\pi$.

For $q(z)=\phi(z)-(1+i)$, an exact normalized Schur--Cohn recursion over
$\mathbb Q(i)$ applied to

$$
w^{12}q\!\left(\frac{1747}{1000w}\right)
$$

has twelve strictly positive gaps.  Conjugation handles $1-i$, and the
chain-rule quotient proves that every such preimage is a genuine
logarithmic singularity.  Therefore

$$
\boxed{\rho(G)>\frac{1747}{1000}.}
$$

The smallest computed root modulus,
$1.7472752090022395\ldots$, is explicitly diagnostic.  In the exact
neighboring box obtained by independently changing each of the four jet
parameters by $-1,0,1$, this candidate is the unique one of $81$ which
passes the same strict radius test.  This is only a local finite
classification.

The exact diagonal systems through $n=15$ all have full row rank and
nonzero first-free coefficient.  Apart from the zero endpoint at $n=1$,
their endpoint decades are

$$
0,7,17,30,51,74,102,137,177,222,274,334,393,458.
$$

Thus the radius gain again fails to overcome primitive determinant height
in the diagonal allocation.

The frozen source, exact certificate script/result, search script/result,
and HP script/result hashes are

    ea37af35ebfb97e0b8a79353eff5d6da4cbe49aebb1bd9ad0a7d6e9d1306163a
    b32190715af12fa82a223a5f8165e75efbf307f1f0bcfa813a8b524e4b1fed0c
    5b71cb31187d87037524a1932ea422ad3d757e68583ca84eadce9078549169db
    946e8e9df6177cdff848ffd668291c20eec8b91b41726373fb655b4b4010241c
    fa7ecd1590f01ce2b1185edea26e9bfd1889dd1168f18b855a89a1badc1568eb
    6ab090b23352b42f6c21126afda57cff52e1c5dbf50e719aa3c7407f218946c4
    1b64b42a0caaadd6e7670ec65305698af55e5ac1bf11f34856f42324d67bfedd

The independent audit note/script/result hashes are

    031f91ee8c443a36e9678c0b9e9a127c9c5222a52b7219f074b7c9bdf4f9304c
    2f5a13f9018ce6441fc6ff0ac2513920982fb63463cd8618cb9d55a61896fdac
    39e4ca71c5e19d5af215bcfbb272b2947172087348775e7efb91b96e0d3bf5be

That audit independently reconstructed the Schur recursion, the $81$-box
classification, the composition jets, every diagonal matrix and primitive
endpoint record, and separate rational endpoint intervals.  All frozen
scripts rerun byte-identically.

## 2026-08-26 — complete non-diagonal scan and a constant-ray theorem

For the earlier high-radius pullback

$$
\phi_8(z)=z+\frac{z^7-z^8}{140},
\qquad G_8=F\circ\phi_8,
$$

an exact scan now covers every dimension-balanced endpoint-matched system

$$
A+B e^z+C G_8=O(z^{a+b+c+1}),\qquad B(1)=C(1),
$$

with $a,b,c\ge0$ and $a+b+c\le18$.  All $1330$ integral high matrices have
full row rank and nullity one.  The only zero endpoint is $(1,1,1)$, and
the only vanishing advertised first-free coefficient is $(1,2,0)$; the
latter has exactly one extra vanishing order.

Exactly sixteen nonzero primitive endpoint values are below one, all at
total degree at most six.  The global minimum is already attained at
$(a,b,c)=(0,5,0)$:

$$
\frac{82761394925}{10^{12}}
<129-22(e+\pi)<
\frac{82761394926}{10^{12}}.
$$

No total budget $6,\ldots,18$ improves this value.  The apparent
unrestricted winners at later exact totals lie on $(0,0,c)$ and reduce
identically to the fixed form $\pm(e+\pi-1)$.

The best finite edge $(0,b,0)$ has the exact recurrence

$$
U_b=bU_{b-1}+(-1)^b,\qquad
V_b=bV_{b-1}+\eta_b,
$$

where $\eta_b=(e^{-z}G_8)^{(b)}(0)$, and its primitive endpoint is

$$
\frac{U_b(e+\pi)-V_b}{\gcd(U_b,V_b)}.
$$

The exact continuation through $b=250$ retains its unique minimum at
$b=5$ and reaches decade $441$, but no uniform upper bound for the gcd is
known; this edge therefore remains open all-degree.

A separate abstract theorem closes the constant-$B=C$ ray.  If a fixed
rational-coefficient germ $J$ satisfies $J(1)=\pi$ and the reduced
denominator of $T_aJ(1)$ is at most $\exp(O(a))$, then the fully reduced
constant-$B=C$ endpoint form obeys

$$
\log|L_a|\ge\frac12a\log a-O_J(a).
$$

The proof transfers the superexponential reduced denominator of
$T_ae(1)$ through the merely exponential denominator of $T_aJ(1)$, then
uses the finite irrationality measures of $e$ and $\pi$ to prevent
factorial-tail cancellation.  For $G_8$, the exact rational differential
equation gives

$$
\operatorname{den}(T_aG_8(1))
\mid39200^a\operatorname{lcm}(1,\ldots,a),
$$

so the theorem applies and this ray diverges.

The frozen source/script/result hashes are

    954308618a572a201a3ad43fee16cb63935a9de45ece6468e86da1677e326c51
    022444b3fc11d501c9f36369cb8d0f645fe1341e538df0736315b5e7814a04b8
    951ea7bff82ab32b0303655a2d71dc4b14c47b02ac6e6ee8dce4eb9500a697c6

An independent rerun of the entire $1330$-case artifact is byte-identical,
and a separate full-matrix implementation reproduces the two asymmetric
records $(0,5,0)$ and $(1,2,0)$.  The finite scan and the two all-degree
edge results still leave genuinely non-diagonal growing-degree regimes
uncontrolled.

## 2026-08-26 — entire integral-Hurwitz perturbation beyond $1.7679119$

The polynomial pullback restriction is not needed to preserve integral
derivative jets.  For integers $m,a,k$, the entire endpoint-fixed term

$$
H_{m,a,k}(z)=\frac{k}{m!}z^m(z-1)e^{az}
$$

has

$$
H_{m,a,k}^{(m)}(0)=-k
$$

and, for $n=m+r\ge m+1$,

$$
H_{m,a,k}^{(n)}(0)
=k\binom nm\left(ra^{r-1}-a^r\right)\in\mathbb Z.
$$

This permits a nonpolynomial integral-Hurwitz improvement.  Define

$$
\begin{aligned}
\phi(z)={}&z
+\frac{46}{7!}z^7(1-z)
+\frac{213}{9!}z^9(1-z)
-\frac{762}{10!}z^{10}(1-z)
+\frac{20073}{11!}z^{11}(1-z)\\
&+\frac{1215540}{15!}z^{15}(z-1)e^{-z}\\
&+\frac{65574371633155024}{26!}z^{26}(z-1)e^{-z}\\
&+\frac{40126919362525583214229456433446912}{40!}
z^{40}(z-1)e^z
\end{aligned}
$$

and $G=F\circ\phi$ for
$F(w)=4\arctan(w/(2-w))$.  Then $\phi(0)=0$, $\phi(1)=1$, and every
derivative jet of $\phi$ is an integer.  The identity

$$
(2-2w+w^2)F'(w)=4
$$

gives the integral recurrence

$$
F^{(n+1)}(0)
=nF^{(n)}(0)-\frac{n(n-1)}2F^{(n-1)}(0).
$$

Faà di Bruno therefore proves $G^{(n)}(0)\in\mathbb Z$ for every $n$,
while endpoint fixing gives $G(1)=\pi$.

For the radius proof, replace each exponential in $\phi$ by its Taylor
polynomial through degree $24$, producing a degree-$65$ polynomial
$q_{24}=\phi_{24}-(1+i)$.  At the exact radius

$$
r=\frac{17679119}{10000000}=1.7679119,
$$

the reciprocal polynomial $w^{65}q_{24}(r/w)$ passes all $65$ steps of a
fraction-free Schur--Cohn recursion over $\mathbb Z[i]$.  Rational
$256$-bit upper bounds for every reflection modulus give a recursive
boundary lower product $B$.  The exact exponential-tail upper bound $T$
satisfies

$$
2B^2>T^2,
\qquad
\frac{2B^2}{T^2}
=67.6644544557414472874566\ldots>1,
$$

where only the displayed decimal is diagnostic; the comparison is by
exact rational cross multiplication.  Rouché's theorem therefore excludes
$\phi(z)=1+i$ throughout the closed disk.  Real coefficients exclude
$1-i$ as well.  Every preimage is a genuine logarithmic singularity of
$F\circ\phi$, so

$$
\boxed{\rho(G)>1.7679119.}
$$

The first computed preimage modulus
$1.7679119968043893\ldots$ is not a certified root enclosure and is not
used in the theorem.

The exact diagonal HP diagnostic has full row rank, nullity one, and a
nonzero first-free coefficient for every $1\le n\le15$.  Its $n=1$
endpoint is zero, and the nonzero endpoint decades for $n=2,\ldots,15$
are

$$
0,7,17,29,50,72,99,134,173,217,268,328,391,464.
$$

Thus the stronger analytic radius again does not overcome primitive height
in the diagonal allocation.

The final proof note, generalized exact certificate script/result, retained
earlier certificate script/result, and HP note/script/result hashes are

    3ae2fb397de460360a589eec2c25bd30d96b7319cea501012763b7c9761dab56
    b9fc93179ef0def5a5214bd928d489744652215fbf49faab1e030032eeb6721d
    62ce908eef68dd3472f0841c6c20b09a94f8356465812aa19c204026d9dacdc0
    2e4ad9a01716d1e808b60ae04f5137d9d6020d46f52d22853c2415c105c41efd
    9d24c15e4f69fc5e8e1618f812e95ffa9d0351b401951795a023c4eaff9afb15
    aa93d76dea21a3d7ab24bd40362d6948c8586df11fc7e7138866247e6b79f78b
    27574fa09fc8a63231347776fa06f6a17b6fa8aafebec48224d5619ad29066b9
    ab01f6a7a731066f860c6f2f91423f30940b5cf9ecccb785c703fdfa867206fc

The independent audit of the exact primitives and the diagonal HP
calculation has note/script/result hashes

    45c417157e700f92e40413d92c7d3f10eb0ddd36354b74458b6dd2464c02ff09
    6640fb5ceec6327f3732bb2bbbb5f17205980c53e00f1343a8f5626ef6114ff6
    ad8a2b7ae447ba9e0236955ba9c7bd75acf3aa4374a6992b224d4ef4846867df

It independently reconstructed the Gaussian-integer Schur states, the
reflection-product inequality, the exponential-tail bound, both conjugate
targets, all-order jets, and every HP record at the earlier certified
radius.  The strengthened radius uses those same exact primitives with
larger truncation and dyadic precision and was rerun byte-identically.
This remains an auxiliary analytic advance, not a result on the arithmetic
class of $e+\pi$.

## 2026-08-26 — canonical factorial digits and exact fixed-$b$ endpoint rays

The canonical factorial digits

$$
d_n=\lfloor n!\pi\rfloor-n\lfloor(n-1)!\pi\rfloor,
\qquad
G(z)=3+\sum_{n\ge2}d_n\frac{z^n}{n!}
$$

give an entire integral-Hurwitz function with $G(1)=\pi$.  Write

$$
C_n=\lfloor n!e\rfloor+\lfloor n!\pi\rfloor,
\qquad
x_n=n!(e+\pi)-C_n.
$$

Then $0<x_n<2$.  For every $b\ge0$ and
$a\ge\max(1,b-1)$, solve the endpoint-matched system

$$
A+B e^z+\gamma G=O(z^{a+b+1}),
\qquad B(1)=\gamma,
$$

with $\deg A\le a$ and $\deg B\le b$.  The high-jet matrix has the exact
determinant

$$
\det M=\left(\prod_{j=0}^{b-1}j!\right)D_{a,b},
\qquad
D_{a,b}=\frac{\Delta^b(a!)}{a!}>0,
$$

where

$$
D_{a,0}=1,\quad D_{a,1}=a,\quad
D_{a,b}=(a+b-1)D_{a,b-1}+(b-1)D_{a,b-2}.
$$

An exact tail-interpolation calculation, followed by clearing the complete
polynomial triple, making it primitive, and finally removing the endpoint
gcd, gives

$$
\boxed{
L_{a,b}
=\frac{W_{a,b}(e+\pi)-Z_{a,b}}{H_{a,b}}
=\frac{\Delta^b x_a}{H_{a,b}},}
$$

with

$$
W_{a,b}=\Delta^b(a!),\qquad
Z_{a,b}=\Delta^bC_a,\qquad
H_{a,b}=\gcd(W_{a,b},Z_{a,b}).
$$

In particular,

$$
|L_{a,b}|<\frac{2^{b+1}}{H_{a,b}}.
$$

There is also an exact logical characterization: $e+\pi\in\mathbb Q$ if
and only if $d_n=n-2$ eventually.  Any one zero $L_{a,b}$ forces
rationality; conversely, if the target is rational then every fixed
$b\ge1$ ray is eventually zero, while the $b=0$ primitive value is
eventually one.  Thus eventual nonvanishing on a fixed positive-$b$ ray is
already equivalent to the open irrationality problem and cannot be silently
assumed.

The exact Roth-strength condition for the reduced approximant is

$$
|\Delta^b x_a|W_{a,b}^{1+\varepsilon}
<H_{a,b}^{2+\varepsilon}.
$$

A Machin-interval certificate computed every $\lfloor n!\pi\rfloor$ needed
for all $15{,}094$ pairs $1\le a\le500$, $0\le b\le30$.  Every resulting
interval excludes zero.  The unique global minimum is

$$
(a,b)=(346,3),\qquad
H_{346,3}=2{,}875{,}602{,}586{,}336,
\qquad
|L_{346,3}|=2.94268312399908\ldots\times10^{-14}.
$$

Here $\log H/\log W=0.0168921\ldots$, nowhere near the square-root scale
needed for Roth.  The theorem therefore identifies, but does not solve, the
remaining varying-$b$ gcd/finite-difference problem.

The accepted source, its generating script/result, and the wholly separate
audit note/script/result have SHA-256 hashes

    66e5e2f46ad10db1bd60ce5a93e7a85a9cb3e02d933b3da78bf09a2815b30f7d
    997127083235cafcef7d815feef587db3d4c6c02d56e4d62d749614a3b145c93
    84cb3eaafeba0887c8291883a0acb0e727217d0c3df509bab9ef9fe808522741
    a0c3164f85a679ca5b420d9a5c0d9bff9d0ea2c81b3ead738daa17828316e55f
    9a8af7c907e20d0b5fd565d026c292a8a091c23dcae291634f641b3f0b524e77
    a466d912b3e887eef1cc7e123aef8e9e2d93e5c180fc940a17391189104d5ac4

The independent implementation reconstructed the factorial digits, the
full $W,Z,H$ stream, every finite minimum and threshold count, nine complete
rational Hermite--Padé matrices (including the largest boundary case), and
the primitive endpoint pair $(-Z/H,W/H)$.  Both implementations rerun
byte-identically.  Nothing in this result proves rationality, algebraicity,
or transcendence of $e+\pi$.

## 2026-08-26 — algebraic units and a two-conjugate-log Rivoal family

The corrected simultaneous exponential--logarithm approximants satisfy

$$
R_{\exp}(x)=A(x)e^x-E(x),\qquad
R_{\log}(x)=A(x)\operatorname{Log}(1-x)-B(x).
$$

A single algebraic logarithm cannot introduce an arbitrary small algebraic
unit while preserving the $e+\pi$ target.  If
$\operatorname{Log}(1-\eta)=i\pi\alpha$ with algebraic $\eta,\alpha$, then
Gelfond--Schneider forces $\alpha\in\mathbb Q$ and $1-\eta$ to be a root
of unity.  The exact substitution-factor product likewise shows that an
integral unit is globally norm-neutral; a small distinguished embedding is
paid for by the remaining embeddings.

Two logarithms do give a genuinely new construction.  If

$$
\operatorname{Log}(1-\eta)-\operatorname{Log}(1-\bar\eta)
=i\pi\frac ab,
$$

then the exact form

$$
\begin{aligned}
\Lambda^{(2)}_{a,b}(\eta)
={}&iaA(\eta)A(\bar\eta)R_{\exp}(1)\\
&+bA(1)\{A(\bar\eta)R_{\log}(\eta)
          -A(\eta)R_{\log}(\bar\eta)\}
\end{aligned}
$$

has coefficient $iaA(1)A(\eta)A(\bar\eta)$ on $e+\pi$.  For every odd
$n\ge5$, take

$$
\eta=\frac1{1+\zeta_n},\qquad
\bar\eta=1-\eta,
\qquad
\frac{1-\eta}{1-\bar\eta}=\zeta_n.
$$

This is a cyclotomic unit and the principal logarithm difference is exactly
$2\pi i/n$.  On the admissible edge $c=f=0$, $d\to\infty$, endpoint
Laplace asymptotics give

$$
|\Lambda_{n,d}|\asymp_n\frac{\rho_1^d}{d},
\qquad
\rho_k=\frac1{2\cos(\pi k/n)},
$$

with eventual nonvanishing.  The phase is

$$
\sin\left(\frac{(d+2)\pi k}{n}
           +\frac12\tan\frac{\pi k}{n}\right),
$$

which never vanishes and has a positive minimum over the finitely many
residue classes of $d$.

The local estimate does not survive naively across the coefficient field.
For an embedding $(k,\varepsilon)$ of
$L_n=\mathbb Q(\zeta_n,i)$, exact branch bookkeeping gives the correction

$$
2i(\varepsilon-k)\pi A_d(1)A_d(x_k)A_d(1-x_k).
$$

It vanishes only at $(1,1)$ and $(-1,-1)$.  Consequently

$$
\prod_{\sigma:L_n\hookrightarrow\mathbb C}
|\sigma(\Lambda_{n,d})|
\asymp_n B_n^d d^{-2(1+|\mathcal T_n|)},
\qquad B_n>1.
$$

For $n=5$, $B_5=\varphi^2$.  More intrinsically,
$-i\Lambda_{5,d}$ lies in the maximal real subfield
$K=\mathbb Q(\zeta_{20})^+$, and

$$
\prod_{\tau:K\hookrightarrow\mathbb R}
|\tau(-i\Lambda_{5,d})|\asymp\varphi^d d^{-3}.
$$

The correct primitive content is an ideal, not the gcd of rational-basis
coordinates.  After the least rational clearing, write

$$
q_d(-i\Lambda_{5,d})=u_d(e+\pi)+v_d,
\qquad \mathfrak c_d=(u_d,v_d)\subset\mathcal O_K.
$$

An exact Smith-normal-form computation proves, for $2\le d\le200$,

$$
N(\mathfrak c_d)=
\left(5^{[d\equiv2\ ({\rm mod}\ 5)]}
      19^{[d\equiv15\ ({\rm mod}\ 19)]}\right)^2.
$$

The hidden ideals have Smith diagonals $(1,1,5,5)$ at $d=7$,
$(1,1,19,19)$ at $d=15$, and $(1,1,95,95)$ at $d=72$, even though the
ordinary coordinate gcd is one.  Exact Fibonacci arithmetic verifies

$$
N(\mathfrak c_d)<\varphi^d\qquad(3\le d\le200).
$$

To cancel the raw real-field exponential factor in unbounded degree, one
would necessarily need

$$
\limsup_{d\to\infty}\frac1d\log N(\mathfrak c_d)\ge\log\varphi.
$$

No such all-degree content bound is presently proved.  Moreover, even when
the coefficient field is disjoint from a hypothetical
$\mathbb Q(e+\pi)$, the relative-norm block does not control the remaining
absolute-norm blocks at the unknown conjugates of the target.  A nontrivial
field intersection is still less controlled.  Thus this work proves local
smallness, eventual local nonvanishing, and a sharp global arithmetic
obstruction, but no arithmetic classification of $e+\pi$.

The accepted source, two generator/result pairs, and the fully independent
audit note/script/result have SHA-256 hashes

    139dfecca71f4d0f980374d4955b330b779193e96c46f69455b680550fee7ff8
    6c1b40f677fb9191bad2e9cc7870812c819ae1c8a640d31796c902d5183e2738
    3d2264d6b0f3cae92677d3e7c827fff853615b49bf2159e49fed985e74e0f163
    120ea17e9c27a2b0ebaa48e3e651220bfe59f06bc028b6d764dcd0798570bb80
    d90be1fd2858a99df16c3c2b4efdac63f480c0578348cac0bb2eb1c37b3811f6
    b2051acc53534cdae3e2ca28650f4d2276b8ba1a384471d418f072e3caa1ab16
    a1ba583b9068d7debb595bd8fa904a8478f77c712aaa14992f6d9a9d47b47c96
    5e7371e06ec6c04fa7b15530405d405e5e0769cb4b2a42a9d0e01bfc121f7853

Both candidate generators and the wholly separate
$\mathbb Z[\zeta_{20}]/(\Phi_{20})$ audit rerun byte-identically.  The
independent calculation also proves that the displayed real-field basis has
discriminant $2000$ and reproduces the selected Smith ideals without using
the candidate's field implementation.

## 2026-08-26 — varying-order factorial-digit theorem

The fixed-order endpoint family has now been analyzed uniformly for every
admissible varying order $0\le b\le a+1$.  Put

$$
W_{a,b}=\Delta^b(a!),\qquad Z_{a,b}=\Delta^b C_a,
\qquad C_a=\lfloor a!e\rfloor+\lfloor a!\pi\rfloor.
$$

Writing the combined canonical digits as $c_0=4,c_1=1$ and
$c_n=d_n(\pi)+1$ for $n\ge2$, iteration of
$C_{n+1}=(n+1)C_n+c_{n+1}$ gives the exact local decomposition

$$
W_{a,b}=a!D_{a,b},\qquad
Z_{a,b}=D_{a,b}C_a+K_{a,b},
$$

where

$$
K_{a,b}=\sum_{j=1}^bE_{a,b,j}c_{a+j},
\qquad E_{a,b,j}>0,\qquad E_{a,b,b}=1.
$$

If $g=(D,K)$, $D'=D/g$, and $K'=K/g$, then the endpoint gcd has the
exact factorization

$$
H_{a,b}=g_{a,b}J_{a,b},\qquad
J_{a,b}=\gcd(a!,D'C_a+K').
$$

Thus $g$ is visible in the future digit block, whereas $J$ is a residual
divisor involving the past factorial numerator.  Alternating-series bounds
give

$$
\frac a{a+b}(a+b)!\le W_{a,b}<(a+b)!,
$$

and, if $b/a\to\lambda\in[0,1]$,

$$
\frac{W_{a,b}}{(a+b)!}\longrightarrow
e^{-\lambda/(1+\lambda)},\qquad
\frac{\log D_{a,b}}{\log W_{a,b}}
\longrightarrow\frac{\lambda}{1+\lambda}.
$$

It follows that the local factor has exponent at most $1/2$ uniformly.
With only the universal finite-difference estimate, any fixed Roth-strength
argument must therefore obtain a positive power of $W$ from $J$, except
where a separately proved exceptional cancellation is available.  A
canonical-digit adversary proves that the inequalities
$0\le d_n\le n-1$ alone cannot control $J$: $C_a$ can occupy every residue
modulo $a!$ independently of any prescribed finite future block.

The same work proves that the canonical entire integral-Hurwitz interpolant
has exponential type exactly one, which is minimal for a nonpolynomial
entire function with integral derivative jets.

The exact triangle $a+b\le530$ contains $71{,}019$ admissible pairs.
Directed rational intervals certify $35{,}716$ positive and $35{,}303$
negative endpoints.  No pair satisfies either the crude or sharpened
square-root gcd threshold.  At the two notable minima,

$$
(8,2):\quad H=840,\ g=1,\ J=840,
$$

and

$$
(346,3):\quad H=2{,}875{,}602{,}586{,}336,\quad
g=8,\quad J=359{,}450{,}323{,}292.
$$

The source, generator, and byte-reproduced result have SHA-256 hashes

    b21a8d0a62367e57048e6975da3fa8397a250be32595c23a3dfd673985ac412c
    003ed11dea46976e31c07e7eacac47c5c8b72c4eb802b45e768165fbb7955cac
    1cb54841219ab0925bb700035372ef5e98b939545a3f5858b1246f50f4a83238

## 2026-08-26 — full polynomial-C factorial-digit family

An independent implementation reconstructed the full endpoint-matched
systems

$$
A+Be^z+CG=O(z^{a+b+c+1}),\qquad B(1)=C(1),
$$

for every $a+b+c\le18$.  When the common endpoint coefficient is nonzero,
normalize it to one and write

$$
B=1+(z-1)T,\qquad C=1+(z-1)S.
$$

The high jets form an explicit $(b+c)$-square integer block
$\mathcal H_{a,b,c}$.  If $D=\det\mathcal H\ne0$, telescoping the endpoint
tails gives the exact adjugate formula

$$
W=a!D,\qquad
Z=P_aD+w\operatorname{adj}(\mathcal H)y,
$$

and the primitive endpoint is

$$
-\frac Z{(W,Z)}+\frac W{(W,Z)}(e+\pi).
$$

For $b\ge1$ a Schur complement factors off the known positive fixed-$b$
determinant; the remaining determinant is only $c$ by $c$ and contains the
actual factorial digits.  All $1330$ bordered matrices in the finite box
have full row rank and nullity one, and $597$ Schur identities were checked
exactly.  There are six singular high blocks.  Five have zero endpoint pair;
the sixth, $(0,1,0)$, has kernel $A=1,B=z-1,C=0$ and endpoint $(1,0)$.

The smallest nonzero form remains

$$
3504(e+\pi)-20533
$$

at $(8,2,0)$, of modulus $0.0001850991300\ldots$.  The best record with
$c>0$ is

$$
12669120(e+\pi)-74239453
$$

at $(8,3,1)$, of modulus $0.0019854195145\ldots$.

There is a sharp logical obstruction to extrapolating rank.  If $e+\pi$
were rational, then $d_n(\pi)=n-2$ eventually and
$P=G-(z-2)e^z$ would be a polynomial.  Multiples of the exact syzygy
$-P+(2-z)e^z+G=0$ would create kernel spaces of growing dimension.
Consequently a universal full-rank theorem for these bordered systems would
already prove the open irrationality statement.

The independently rerun note, script, and result have hashes

    9e320dafa77e281bc151e075d74c64962f2ecc78abbdb166d5d99f8bbd02203e
    547ab656935dade778720c1f08f00c84eb913f26bc44159a71ac83099c4794fc
    2f527c542af6f6ed4b06864e2c063443462ee781e911a387ff0776704b6ea470

## 2026-08-26 — rational traces of the n=5 two-log edge

Put $K=\mathbb Q(\zeta_{20})^+$, $F=\mathbb Q(\sqrt5)$, and
$\Theta_d=-i\Lambda_{5,d}$.  The form has the exact relative decomposition

$$
\Theta_d=X_d+Y_d,\qquad \tau(X_d)=X_d,\qquad \tau(Y_d)=-Y_d,
$$

with $X_d$ bounded at both embeddings of $F$, $Y_d$ bounded at the
distinguished embedding, and

$$
|\nu_1(Y_d)|\asymp\frac{\varphi^d}{d}.
$$

For a unit $\theta\in\mathcal O_K^\times$, taking
$\operatorname{Tr}_{K/\mathbb Q}(\theta\Theta_d)$ produces a rational
linear form in $e+\pi$.  Every $\theta\in F$ kills the anti-fixed part;
after rational primitivization every nonzero trace is exactly the same
reduced derangement form and diverges.

For $\theta\notin F$, the nonzero algebraic integer
$\delta=\theta-\tau\theta$ satisfies

$$
1\le|N_{K/\mathbb Q}(\delta)|
=|\delta_0\delta_1|^2.
$$

If $H(\theta)=\max_\sigma|\sigma(\theta)|$, this forces the anti-fixed
coordinate at the growing embedding to be at least $1/(4H(\theta))$.
After exact rational primitivization the resulting nonconstant form obeys

$$
|L_d|\gg\frac{\varphi^d}{dH(\theta)^2}
$$

whenever that term dominates.  Hence exponent triples $o(d)$ in the three
standard cyclotomic units are rigorously excluded.  Any primitive unit-trace
sequence tending to zero must eventually leave $F$ and satisfy
$H(\theta_d)\gg\varphi^{d/2}/\sqrt d$.  Tropical balancing is possible only
at still larger height, about $\varphi^{5d/4}$, and does not control signed
trace cancellation or the exact rational gcd.  That remaining regime is
open.

The source, exact probe, and byte-reproduced result have hashes

    88ecb9e55bf2f484cbf6c382ca7ddeb6f06b1dca1bec112379ae17528ee86245
    fd29f6e616ddc09ddb11ed842d2a64990406554aff0efb255534a4fe48c67eb1
    cd9402720e691f2246b8f2ee2d1bc661b8bfcca6daf4d0dd34e74b1674b8a4ed

All three additions above are obstructions or structural reductions.  None
proves rationality, algebraicity, irrationality, or transcendence of
$e+\pi$.

## 2026-08-26 — universality of unrestricted algebraic-integer traces

For the minimally cleared $n=5$ two-log edge, write

$$
q_d\Theta_d=u_d(e+\pi)+v_d,\qquad u_d,v_d\in\mathcal O_K,
\qquad K=\mathbb Q(\zeta_{20})^+.
$$

Allowing an arbitrary $\theta\in\mathcal O_K$ defines the integral trace map

$$
\Phi_d(\theta)=
\bigl(\operatorname{Tr}(\theta u_d),\operatorname{Tr}(\theta v_d)\bigr)
\in\mathbb Z^2.
$$

In the accepted integral basis, its matrix is obtained by multiplying the
coordinate columns of $u_d,v_d$ by the trace Gram matrix

$$
G=
\begin{pmatrix}
4&-2&0&0\\
-2&6&0&0\\
0&0&10&0\\
0&0&0&10
\end{pmatrix},
\qquad \det G=2000.
$$

The map has rank two for every $d\ge2$.  Indeed, the coefficient $u_d$ is
a nonzero element of $F=\mathbb Q(\sqrt5)$, while the anti-fixed component
of $v_d$ is a nonzero multiple of

$$
J_d=A_d(x)B_d(y)-A_d(y)B_d(x).
$$

Exact field arithmetic handles $2\le d\le19$.  For $d\ge20$, the main
logarithmic term in $J_d$ has modulus greater than $24/125$, whereas the
two remainders have total modulus at most $36(5/8)^d$; the latter is
smaller by the exact inequality

$$
375\cdot5^{20}<2\cdot8^{20}.
$$

Thus $v_d\notin F$, so $u_d,v_d$ are rationally independent and
nondegeneracy of the trace pairing proves rank two.

Every rank-two image lattice with Smith invariants
$\alpha_d\mid\beta_d$ contains $\beta_d\mathbb Z^2$.  It follows that,
after ordinary gcd primitivization, every coprime pair $(P,Q)$ occurs.
At $d=2$ this is completely explicit:

$$
[\Phi_2]=
\begin{pmatrix}
10&-10&0&0\\
-20&20&50&-50
\end{pmatrix},
$$

and the coordinate vector $(5P,0,Q+2P,0)$ maps to $(50P,50Q)$.

Therefore arbitrary algebraic-integer multipliers make the construction
projectively universal.  Choosing a small nonzero form would simply amount
to importing a rational approximation to $e+\pi$; proving it nonzero would
import the still-open irrationality question.  This closes the unrestricted
multiplier proposal as a source of Padé-specific arithmetic information,
while leaving the constrained unit-height problem open.

The exact Smith scan through $d=200$, including all low-degree rank checks,
was rerun byte-identically.  The frozen source, script, and result hashes are

    759764ca557c83c5aadc0c4c7e9fd4ccfa9997c089bd8913859d440d1317bf2f
    34a4a3cf412fdbb70e16be9942524fa8d129d7ec318ccbe4ff8e9f013fe89454
    cd76d458ab8d220ae0da65460557fc7d83e6073d41761c11a8f6c6e28d336917

This universality theorem is a rigorous no-go result for an overlarge
multiplier class.  It does not classify $e+\pi$.

## 2026-08-26 — exact determinant theorem for the $c=1$ factorial-digit ray

The first genuinely digit-dependent polynomial-$C$ case now has a complete
all-degree determinant reduction.  With

$$
u_j(k)=k^{\underline j}(k-j-1),\qquad
v(k)=kg_{k-1}-g_k,
$$

the high block is

$$
\mathcal H_{a,b,1}
=(u_0,\ldots,u_{b-1},v)|_{k=a+1,\ldots,a+b+1}.
$$

Define the positive integers

$$
D_{a,m}=\frac{\Delta^m(a!)}{a!},\qquad
D_{a,m}=(a+m-1)D_{a,m-1}+(m-1)D_{a,m-2}.
$$

They are the shifted-gamma moments with exponential generating function
$e^{-z}(1-z)^{-a-1}$ and have an explicit Jacobi continued fraction.  A
Poisson functional on the falling-factorial basis gives

$$
\det\mathcal H_{a,b,1}=(-1)^b\kappa_bF_{a,b},\qquad
\kappa_b=\prod_{j=0}^{b-1}j!,
$$

where

$$
F_{a,0}=v(a+1),\qquad
F_{a,b}=bF_{a,b-1}+(-1)^bD_{a,b}\Delta^bv(a+1).
$$

The exact cofactor expansion is

$$
F_{a,b}=\sum_{r=0}^b(-1)^rA_{a,b,r}v(a+1+r),
$$

with every $A_{a,b,r}$ a positive integer.  Substitution of
$v(a+1+r)=(a+r+1)d_{a+r}-d_{a+r+1}$ gives the direct digit form

$$
F_{a,b}=\sum_{s=0}^{b+1}(-1)^sB_{a,b,s}d_{a+s},
$$

again with every $B_{a,b,s}>0$.  The endpoint coefficients satisfy

$$
B_{a,b,0}=D_{a,b+1}+D_{a,b},\qquad
B_{a,b,b+1}=D_{a,b}.
$$

Since $D_{a,m}\equiv(-1)^m\pmod m$ and consecutive $D$ values are
coprime, the normalized digit vector has exact content one:

$$
\gcd_{0\le s\le b+1}B_{a,b,s}=1.
$$

This removes the possibility of a hidden universal factorial gcd.  It
also exposes the remaining obstruction sharply.  The digit box
$0\le d_n\le n-1$ permits both signs: a single nonzero digit in the first
or second position gives opposite signs.  It permits zeros arbitrarily
far out: a constant-one block duplicates the $u_0$ column for $b\ge1$,
and a zero pair handles $b=0$.  More specifically, the conditional
rationality tail $d_n=n-2$ gives

$$
v(k)=k^2-4k+2=k^{\underline2}-3k^{\underline1}+2,
$$

whose Poisson functional is zero, so every $b\ge2$ determinant wholly
inside that tail vanishes.  Thus digit ranges alone cannot yield an
eventual sign or nonvanishing theorem in fixed, subdiagonal, or diagonal
regimes.

An independent exact certificate extended the certified digit sequence to
$d_{531}=297$ and scanned all $71{,}019$ admissible pairs $a+b\le530$.
The recurrence, cofactor form, and direct digit form agree identically.
For the actual digits of $\pi$, the only determinant zeros are

$$
(a,b)=(1,0),(1,1),(2,0).
$$

There are $35{,}252$ negative, $35{,}764$ positive, and three zero
normalized determinants.  The smallest nonzero digit-box ratio is
$5.6157370861437\ldots\times10^{-7}$ at $(318,212)$.  These are finite
diagnostics only.

The frozen source, independently rerun certificate, and result hashes are

    0613909851f02d73ab4cc8328eba505f038ec11d1713c1caa696f5f797e5d026
    da614228b3a97ad1330d452a63690f075354f91c52e5b4029c745c2c650c87fe
    80f163658ab10039364f256cbc6439f9ba0cc3e650f6613c38579206f07824fb

The theorem is a structural reduction, not a proof of irrationality or
algebraicity of $e+\pi$.

The certificate hashes above supersede the initial draft.  A subsequent
reproducibility audit found that the draft had advanced the alternating
arctangent remainder ratio by one index.  The corrected first omitted term
after summing through index $L$ is

$$
|t_L|\frac{2L+1}{(2L+3)q^2},
$$

not $|t_L|(2L+3)/((2L+5)q^2)$.  After correction, all $71{,}019$
determinants, signs, zeros, minimizers, and digit hashes are unchanged; only
the stored rational enclosure endpoints and therefore the artifact hashes
changed.  A second run reproduced the corrected JSON byte-for-byte.

## 2026-08-26 — forced exceptional points for logarithms of E-values

A primary-source audit of Delaygue's Lindemann--Weierstrass theorem for
$E$-functions and the final 2026 Fischler--Rivoal logarithm theorem closes a
broad interpolation proposal.  If $F$ is a Siegel $E$-function and
$x,\eta\in\overline{\mathbb Q}^{*}$ satisfy

$$
F(x)=e^\eta,
$$

then Hermite--Lindemann makes this common value transcendental.  Apply the
different-point form of Delaygue's theorem to $F(x)$ and $e^z|_{z=\eta}$.
Since the Borel transform of $e^z$ has the sole finite singularity $1$, the
ratio theorem gives the exact forced-singularity statement

$$
\boxed{x/\eta\in\mathfrak S(F)}.
$$

Fischler--Rivoal's exact exceptional-point criterion therefore puts $x$ in
the exceptional set for every non-pure-exponential $F$: it has precisely the
form $F(x)=\exp(x/\rho)$ with $\rho=x/\eta\in\mathfrak S(F)$.  The case
$\eta=0$ is the separate exceptional value $F(x)=1$.

This immediately handles every endpoint-fixing perturbation

$$
F_+(z)=e^{\beta z}+(z-x)H(z),\qquad F_+(x)=e^{\beta x}.
$$

For $H\ne0$ it is not a pure exponential, and the forced singularity is
$\beta^{-1}\in\mathfrak S(F_+)$.  No choice of a vanishing $E$-function
perturbation can cancel it.  The apparent minus variant does not provide a
second algebraic logarithm: if an algebraic scalar $c$ and algebraic
$\beta,x,\eta$ satisfy $ce^{\beta x}=e^\eta$, Hermite--Lindemann forces
$c=1$ and $\eta=\beta x$.  Thus $-e^{\beta x}$ has no algebraic logarithm.

Under the hypothesis $\alpha=e+\pi\in\overline{\mathbb Q}$, the 2026
Fischler--Rivoal interpolation theorem does construct a non-exponential
$E$-function with

$$
F(1)=e^\alpha
$$

for which $1$ is regular for both the minimal homogeneous and inhomogeneous
differential equations.  The forced-singularity theorem simultaneously gives
$\alpha^{-1}\in\mathfrak S(F)$.  There is no contradiction: differential-
equation singularities in the original variable and singularities of the
Borel $G$-function are different objects.  Direct functions such as
$\exp(e^z+z-1)$ and, conditionally,
$\exp((\alpha-1)z-e^z+1)$ do attain $e^e$ and $e^\pi$, respectively, but
have infinite entire order and hence are not $E$-functions.

The audited note, including exact theorem hypotheses and the screened
2025--2026 primary literature, has SHA-256

    21fdd99e7df9cbc83bc4920cf2f0b16b6b5efd11112ce08afd8e798008ec2e33

This is an exact exceptional-set no-go theorem, not a classification of
$e+\pi$.

## 2026-08-26 — arbitrary-degree integral quotient for the factorial-digit family

The entire polynomial-$C$ high block now has an all-degree quotient theorem.
For $N=b+c$, define

$$
u_j(k)=k^{\underline j}(k-j-1),\qquad
v_j(k)=k^{\underline j}\bigl((k-j)g_{k-j-1}-g_{k-j}\bigr).
$$

The high matrix evaluates $u_0,\ldots,u_{b-1},v_0,\ldots,v_{c-1}$ at the
consecutive nodes $a+1,\ldots,a+N$.  For any integer sample column $h$, its
integral quotient column is

$$
\widetilde{\mathcal Q}(h)=
\begin{pmatrix}
\displaystyle\sum_{m=0}^b(-1)^m\frac{b!}{m!}D_{a,m}\Delta^mh(a+1)\\
\Delta^{b+1}h(a+1)\\
\vdots\\
\Delta^{b+c-1}h(a+1)
\end{pmatrix}.
$$

Let $\widetilde Q$ contain the quotient columns of the $v_j$.  A graded
monic basis consisting of

$$
(1,u_0,\ldots,u_{b-1},
 (k-a-1)^{\underline{b+1}},\ldots,(k-a-1)^{\underline{N-1}})
$$

turns the first quotient row into the Poisson functional and the remaining
rows into Newton differences.  Moving that first row past the $b$ identity
rows gives exactly $(-1)^b$.  Scaling the quotient rows by
$b!,(b+1)!,\ldots,(b+c-1)!$ cancels the corresponding tail of the
consecutive-node Vandermonde.  Consequently

$$
\boxed{
\det\mathcal H_{a,b,c}
=(-1)^b\left(\prod_{j=0}^{b-1}j!\right)\det\widetilde Q_{a,b,c}.}
$$

Every quotient entry is integral.  Since all transformations are invertible
over $\mathbb Q$, they also give

$$
\operatorname{rank}\mathcal H=b+\operatorname{rank}\widetilde Q,
$$

$$
\operatorname{rank}[\mathcal H\mid y]
=b+\operatorname{rank}[\widetilde Q\mid\widetilde q_y],
$$

and

$$
\operatorname{nullity}M^{\rm full}_{a,b,c}
=c+1-\operatorname{rank}[\widetilde Q\mid\widetilde q_y].
$$

Thus high-block nonsingularity and full bordered rank are distinct tests.
In particular, a singular quotient with augmented rank $c$ forces the common
endpoint coefficient $B(1)=C(1)$ to vanish but does not by itself force
$A(1)=0$.  For $c=1$ the quotient is exactly the previously accepted
$F_{a,b}$; the $c=0$ edge has the separately proved determinant
$\left(\prod_{j<b}j!\right)D_{a,b}$.

An independent exact scan checked determinant, rank, augmented rank, and
full nullity for all $1{,}140$ triples with $c>0$ and total degree at most
$18$, plus $220$ triples for an unrelated integral jet sequence.  There are
exactly five singular canonical high blocks,

$$
(1,0,1),(1,0,2),(1,1,1),(2,0,1),(2,0,2),
$$

but every full bordered matrix in the scan has full row rank.  A root rerun
reproduced the JSON byte-for-byte.  The source, corrected certificate, and
result hashes are

    51841a1e5f65fb334570f7a9ca00817bed001af5af69b57f2e53d745d4226669
    614c1f9e999d1760fec9e33227fa471cac2ad1bcf2fb8d64f9a413936052c536
    e3bae6381b2a3d2123d72d436fc7552d21b6519653c84772337ca5d59d3c0503

The certificate uses the corrected first-omitted arctangent term and its jet
vector agrees entrywise with both independent reference certificates.  This
is a structural dimension reduction, not a proof of universal nonvanishing.

## 2026-08-26 — rational cyclotomic-unit rays and primitive content

The standard-unit trace family on

$$
K=\mathbb Q(\zeta_{20})^+,
\qquad
\theta_d=u_3^{m_3(d)}u_7^{m_7(d)}u_9^{m_9(d)},
\qquad
T_d=\operatorname {Tr}_{K/\mathbb Q}(\theta_d\Theta_d)
$$

now has a complete raw classification on every fixed rational slope.  Exact
Galois action gives the four endpoint rates

$$
\lambda_k(\mathbf r)
=\boldsymbol\ell^t\left(A_k\mathbf r+
\frac{a_k}{2}(1,1,-1)^t\right),
\qquad (a_1,a_3,a_7,a_9)=(-1,1,1,0).
$$

Because the three distinguished logarithms are rationally independent,
solving a pairwise equality at a rational slope reduces to an exact vector
equation.  All six solutions lie on

$$
\mathcal F=\{(c,c,-c):c\in\mathbb Q\},
$$

and its upper-wall portion is exactly $c\le1/4$.  Off $\mathcal F$ there is
one uniquely dominant embedding and the raw trace grows exponentially.  On
$\mathcal F$, write

$$
\theta_d=\varphi^{2n_d}\xi,
\qquad n_d=cd+O(1).
$$

For $\xi\notin F=\mathbb Q(\sqrt5)$, the anti-fixed coefficient in the tied
$3,7$ pair is nonzero; for $\xi\in F$ it vanishes exactly and the fixed part
is nonzero.  This proves that every raw rational-ray trace is eventually
bounded away from zero.  The frozen raw-ray source, exact script, and result
have hashes

    cebada6f0121bd46f1a5b068844c169e73e88ffb1e7d255f621805cd947dc925
    bbb57891f41ff75da7b4eebabc67d2fac827ee272d41ffb6b20dc9eb74c765ae
    79e186bc751d4de1e74968a949e20bfa2621e9dc16c4b6c2964701c6dd6fab8f

The coordinate gcd on the resonant line can then be bypassed completely.
Write the uncleared rational trace and its minimally cleared integer pair as

$$
T_d=a_d(e+\pi)+b_d,
\qquad
q_dT_d=A_d(e+\pi)+B_d,
\qquad
g_d=(A_d,B_d).
$$

For the fully primitive form $L_d$, whenever $A_d\ne0$ one has exactly

$$
\frac{L_d}{A_d/g_d}=\frac{T_d}{a_d},
\qquad
|L_d|\ge\left|\frac{T_d}{a_d}\right|.
$$

For a non-subfield bounded offset, the endpoint estimates give

$$
\left|\frac{T_d}{a_d}\right|\gg_\xi
\begin{cases}
d^{-1}\varphi^d,&c<0,\\
d^{-1}\varphi^{(1-4c)d},&0\le c<1/4,
\end{cases}
$$

while for $c\ge1/4$ the quotient has the nonzero limit

$$
\frac{T_d}{a_d}\longrightarrow
\frac{2\pi\,\sigma_9(\xi)}{\sigma_1(\xi)+\sigma_9(\xi)}.
$$

The denominator cannot vanish: $\tau\xi=-\xi$ would force the exponent
vector to be $(b,b,-b)$, on which the exact signed action is instead
$\tau\xi=\xi$.  If the integer coefficient is zero, a nonzero primitive
form is an integer constant of modulus one.  Subfield offsets reduce to

$$
\frac{{!d}}{({!d},d!)}(e+\pi)
-\frac{d!}{({!d},d!)},
$$

whose modulus diverges because the reduced numerator tends to infinity and
the quotient by that numerator tends to $\pi$.  Hence every eventually
nonzero primitive form on every rational resonant ray is bounded away from
zero.

For completeness, the ordinary gcd also has the exact trace-dual formula

$$
g_d(\theta)=\max\{m\ge1:\theta/m\in
(\mathbb Zu_d+\mathbb Zv_d)^\vee\}.
$$

After relative trace to $F$, a rank-two coefficient matrix with Smith
invariants $\alpha\mid\beta$ yields

$$
g_d(\varphi^{2n}\xi)
=\alpha\gcd\left(z_1,\frac\beta\alpha\right),
$$

where $(z_1,z_2)$ is a primitive Lucas-type trace row.  The finite exact
diagnostic verifies the relative-trace identities, row primitivity, and every
rank-two Smith formula for four non-subfield offsets, six rational slopes,
and all admissible degrees through $200$.  A root rerun reproduced its JSON
byte-for-byte.  The primitive theorem, script, and result hashes are

    31adb6350e33e7efcecba1f25eabb19cddf08592f53472ae3993e278ea85962d
    3805dff476c59a5394e34e85c39efe6491a0b513bc83c80a4d128005ce59f22a
    5ebc847a2b81c44aac947cba2dd8722725293dc8ba7df4568bde88ed156addd0

This closes primitive content only on the rational upper-wall family.  It
does not yet control all primitive off-wall rational slopes, and it does not
classify $e+\pi$.

## 2026-08-26 — exact primitive chambers off the quadratic line

The quotient method also resolves most rational slopes away from the
quadratic line.  For a rational slope $\mathbf r$, let

$$
\mu_k(\mathbf r)=\boldsymbol\ell^tA_k\mathbf r,
\qquad
M=\max_k\mu_k,
$$

be the four exponential rates of the coefficient of $e+\pi$.  The endpoint
rates of the raw trace are

$$
(\lambda_1,\lambda_3,\lambda_7,\lambda_9)
=(\mu_1-\log\varphi,\mu_3+\log\varphi,
  \mu_7+\log\varphi,\mu_9),
\qquad
R=\max_k\lambda_k.
$$

Exact rational tie solving proves that both the $\mu$-maximum and the
$\lambda$-maximum are unique away from
$\mathcal F=\{(c,c,-c)\}$.  Thus, after separating bounded offsets and
residue classes,

$$
\left|\frac{T_d}{a_d}\right|
\asymp d^{-p_i}\exp\{d(R-M)\},
$$

where $i$ is the raw dominant embedding and $p_i=1$ for $i=1,3,7$ but
$p_9=0$.  The gap $R-M$ is negative if and only if the coefficient is
dominated by embedding $1$ and all three strict inequalities

$$
\mu_1-\mu_3>\log\varphi,
\qquad
\mu_1-\mu_7>\log\varphi,
\qquad
\mu_1>\mu_9
$$

hold.  This is the exact unresolved open cone $\mathcal C$, not merely a
sufficient subregion.

If $R-M>0$, the invariant primitive quotient makes every eventually nonzero
primitive trace diverge.  If $R-M=0$, solving the sixteen ordered equations

$$
\boldsymbol\ell^t\left((A_i-A_j)\mathbf r+
\frac{a_i}{2}(1,1,-1)^t\right)=0
$$

shows that, outside $\mathcal F$, only $(i,j)=(9,9)$ is possible.  The same
bounded unit offset then cancels between numerator and denominator, and the
endpoint constants give

$$
\frac{T_d}{a_d}\longrightarrow
\frac{4(-1)^d\pi e^{-2}}{2(-1)^de^{-2}}=2\pi.
$$

Consequently every rational slope outside
$\mathcal F\cup\mathcal C$ is now excluded after full rational
primitivization, while $\mathcal F$ was closed by the preceding quadratic-ray
theorem.  No conclusion is claimed inside $\mathcal C$; there the quotient
decays and a lower bound for the primitive coefficient, equivalently an upper
bound for the traced gcd, is still missing.

The source, exact symbolic certificate, and byte-reproduced result hashes are

    32b919f0b7168df458e9ef77540c4730969eb76c3dcf5747e232402ef7a82cca
    823b62087b2a875cf048b1902738dff3e49951455e3eb037f44e6a040cfedb1d
    229c31556f8419798b927d27c20419e4ecf483d1948a4b38cb037a633b7fe864

This is a sharp localization of the remaining arithmetic obstruction, not a
classification of $e+\pi$.

## 2026-08-26 — exact high-critical Fourier valuations and the odd-content obstruction

For the automatic log-free family

$$
J_{n,k}=\int_0^1\frac{x^n(1-x)^n}{(1+x^2)^k}\,dx,
\qquad n=2r,\quad K=k-1\ge2r,
$$

write its accepted Fourier coordinates as

$$
J_{n,k}=R_{n,k}+Q_{n,k}\pi,
\qquad Q_{n,k}=\frac{C_0}{2^{2k}}>0.
$$

The central coefficient now has the exact all-degree valuation

$$
\boxed{v_2(C_0)=r+s_2(K)+(r\bmod2)v_2(K).}
$$

The proof first expands the full-period mean as the positive super-Catalan
sum

$$
C_0=\sum_{j=0}^r\binom{2r}{2j}
\frac{(2r+2j)!(2K-2r-2j)!}
     {(r+j)!(K-r-j)!K!}.
$$

After a common odd denominator, its numerator is

$$
N_r(K)=2^rK^{\,r\bmod2}P_r(K),
$$

where $P_r\in\mathbb Z[K]$ is odd at every integer.  The decisive EGF
coefficient identity contains the essential odd factor $(2r-1)!!$; two
independent audits caught and corrected its omission in an early draft.
Reduction modulo two gives the constant parity when $r$ is even and the
$K$ factor when $r$ is odd; differentiating at $K=0$ proves that the
remaining quotient is odd even at even $K$.

The rational coordinate has the independent lower valuation

$$
\boxed{v_2(R_{n,k})\ge-k-\lfloor\log_2K\rfloor.}
$$

For even monomials, subtracting one quarter of the full beta moment gives
rational coordinates $E_{a,k}$ satisfying

$$
E_{a,k}=\frac{2a-1}{2k-2a-1}E_{a-1,k}
-\frac1{2^{k-1}(2k-2a-1)},
\qquad E_{a,k}+E_{K-a,k}=0,
$$

and hence $v_2(E_{a,k})\ge-k$.  For odd monomials, an exact incomplete-beta
tail gives

$$
I_{2a+1,k}=\frac12\left[
B(a+1,K-a)-\sum_{j=0}^a(-1)^j\binom aj
\frac{2^{-(K-a+j)}}{K-a+j}\right],
$$

which has valuation at least
$-k-\lfloor\log_2K\rfloor$.  Expanding the numerator of $J$ proves the
displayed rational-coordinate bound without any cancellation assumption.

If $R\ne0$, write $R/Q=A/B$ in lowest terms.  The two valuations force

$$
v_2(A/B)\ge k-r-3\lfloor\log_2K\rfloor-1
$$

conservatively.  On the interval
$[\frac14\sqrt{n/k},\frac12\sqrt{n/k}]$, one also has the elementary bound

$$
J_{n,k}\ge
\left(\frac14\sqrt{\frac nk}\right)^{n+1}
\exp\left(-n\sqrt{\frac nk}-\frac n4\right).
$$

Since $Q<((1+\sqrt2)/2)^n$, these estimates prove, uniformly without any
upper restriction on $k$,

$$
A+B\pi\longrightarrow+\infty
\qquad\left(k\ge\frac1{35}n\log n, R\ne0\right).
$$

If $R=0$, the primitive $\pi$-form is exactly $\pi$ rather than divergent;
matching that special form to the primitive beta $e$-form gives the already
primitive value $q_n(e+\pi)-p_n\ge\pi n^n$, so that exceptional branch also
cannot become small.

The theorem deliberately stops short of an all-$k$ conclusion for the fully
matched form when $R\ne0$.  If $(p_n,q_n)$ and $(A,B)$ are primitive, put

$$
d=(q_n,B),\quad q_n=dq_0,\quad B=dB_0,
\quad M=-B_0p_n+q_0A.
$$

The exact final content is

$$
\boxed{g=\gcd(M,d),}
$$

because $\gcd(M,q_0B_0)=1$.  All of $p_n,q_n,B,d,g$ are odd in the high
range, so the $2$-adic theorem supplies no bound for this last odd divisor.
The exact warning case

$$
n=2,\qquad k=10,\qquad
(A,B)=(-149056,135135),\qquad(p_2,q_2)=(19,7),\qquad d=g=7
$$

shows that final content one cannot be inferred from parity.

The frozen theorem, exact certificate, byte-reproduced result, and separate
audit hashes are

    8ac8fcf223ca5b0950d45308ae69b526484285fc43ed9a1e32ebbf57db9cde32
    4d02b9e471f281b0c6bc214b1ff5c496ffbc9c004c3f4e6627c2e7ccaf937b57
    4962773d41014e19d7ef8d7010a4a75f45bdb3ee93a65de348365bee61015663
    c393142d8031e44f75d182d0cbb3f38bcf11857ed48a08198b7a50947eb54f00

The main certificate covers $1{,}296$ central cases, $700$ rational-coordinate
cases, and nine direct Fourier cross-checks; these finite checks support but
are not used in the all-degree proof.

There is also an exact forced-prime theorem for the original Fourier content

$$
h_{n,k}=\gcd(4T_{n,k},L_kC_0).
$$

Characteristic-$p$ support gaps in the factorization
$G_{n,k}=P_n(1+y)^{2(k-n-1)}$ prove

$$
\boxed{
\prod_{\substack{p\ \mathrm{prime}\\(k-1)/2<p\le2(k-n-1)/3}}p
\mid h_{n,k}.}
$$

Therefore $\log h_{n,k}\ge(1/6+o(1))k$ and, with the existing exponential
upper bound, $\log h_{n,k}=\Theta(k)$ whenever $n=o(k)$.  This refutes every
unrestricted estimate $\log h=O(n\log n)$.  A complementary
$\mathbb Q_2(i)$ line integral from $1$ to $i$ proves the stronger exact
divisibility

$$
2^{k-1}\mid T_{n,k},
$$

and hence that the full power of two in $L_kC_0$ is removed from the
primitive $\pi$ coefficient.  Neither the forced odd prime band nor this
complete $2$-part determines the residual odd matching gcd.

The forced-prime source, exact probe, and byte-reproduced result hashes are

    fc9652c087f8b279c5ce0ff13ad7340d7623444d927054ac23c93d2331643895
    701760756938c3b61321950c33746ca3a7c196d0151c30f26a3221cdc0d3aeaf
    be7a3f2998171dc92c78d905be7dbff0f322da3f7569b58a2c52a4797cf2bad9

These results close the high-region primitive $\pi$ arithmetic but leave a
precise odd-content problem for the matched $e+\pi$ form.  They do not
classify $e+\pi$.

## 2026-08-26 — the first lift beyond the degree-200 ideal-content pattern

The finite $n=5$ two-log computation through degree $200$ had the exact
content-norm formula

$$
N(\mathfrak c_d)=
\left(5^{[d\equiv2\pmod5]}
19^{[d\equiv15\pmod {19}]}\right)^2
\qquad(2\le d\le200).
$$

That theorem remains correct in its stated range, but the formula is not an
all-degree identity.  Its first failure is $d=205$.  With
$t=\zeta _5+\zeta _5^{-1}$ and $\delta=4-t$, exact division in
$\mathbb Z[t]$ gives

$$
v_\delta(u_{205})=2,\qquad
v_\delta((v_{205})_{\mathbb Z[t]})=12,\qquad
v_\delta((v_{205})_{z\mathbb Z[t]})=3.
$$

The exhaustive determinantal divisors of the $4$ by $8$ multiplication
matrix are

$$
(\Delta_1,\Delta_2,\Delta_3,\Delta_4)
=(1,1,361,130321),
$$

so its Smith invariants are $(1,1,361,361)$.  Since
$\delta^2=17-9t$ generates a sublattice with the same determinantal
divisors, the inclusion supplied by the three valuations has equal index
and hence

$$
\boxed{\mathfrak c_{205}=\delta^2\mathcal O_K},
\qquad
N(\mathfrak c_{205})=19^4=130321.
$$

The old residue-class extrapolation predicts only $19^2$.  The exact scan
through $500$ has no new prime support and no other failure of the old
formula, but this is not an all-degree replacement: later primes or higher
lifts have not been excluded.  In particular, the calculation neither
proves nor refutes the subexponential content estimate needed by the norm
route.

The source, exact countercertificate, and byte-reproduced result hashes are

    03afd37171557543b6b2531eea057388947ed0da965579daf9532057f59e2f85
    2f1bb879e738c6e0b382b62f2e66950304c9a944a3b539ece1206d6626e1c700
    1a4eeb2f8de3bcbcfe349e529c19d9eaf1495d6bb44467b94834d60452418fbf

The script was rerun independently in a temporary directory and reproduced
the archived JSON byte for byte.

## 2026-08-26 — all-degree local content at (5) and (19)

The lift at degree (205) can be placed in an exact all-degree local law.
For

$$
P_d(X)=d!A_d(X),\qquad C_d(X)=d!B_d(X),\qquad
D_d=P_d(\eta)C_d(\bar\eta)-P_d(\bar\eta)C_d(\eta),
$$

direct coefficient comparison gives the integral recurrences

$$
P_d=X^d-dP_{d-1},\qquad
C_d=-dC_{d-1}+c_dX^d,\qquad
c_d=c_{d-1}+P_{d-1}(1).
$$

After the common least-common-multiple scalar is removed, the three blocks
that determine the local content are

$$
2P_d(1)P_d(\eta)P_d(\bar\eta),\qquad
-2(-1)^dd!P_d(\eta)P_d(\bar\eta),\qquad
5P_d(1)D_d.
$$

At (19), the root (t=4\pmod {19}) lifts to (t=42\pmod {361}),
so (\eta\bar\eta=320\pmod {361}).  In

$$
(\mathbb Z/361\mathbb Z)[X]/(X^2-X+320)
$$

both local units have order (1710); combining this with the coefficient
period (361) gives the exact state period (32490).  Over one full
period the two (P)-values have simple (19)-adic zeros precisely for
(d\equiv15\pmod {19}), and (D_d\equiv0\pmod {361}) inside that class
precisely for (d\equiv205\pmod {361}).  The (C)-state returns shifted
by (95P).  Because (D_d) is invariant under
(C\mapsto C+\lambda P), the checked period repeats for all degrees.
The conjugate prime (t=14\pmod {19}) has no (P)-zero, excluding a
hidden common rational (19)-factor.

At (5), calculation in
(\mathbb F_5[\varpi]/(\varpi^4)), (\varpi=\zeta _5-1), has period
(20).  It gives simple (\varpi)-zeros for both (P)-values exactly
when (d\equiv2\pmod5), while (D_d) also has exact
(\varpi)-valuation one.  The endpoint shift is (C\mapsto C+P), so
the same invariant proves all-degree periodicity.  Translating
(v_\varpi(2-t)=2), (v_\varpi(5)=4), and the anti-fixed basis factor
then yields

$$
\boxed{
v_{(2-t)\mathcal O_K}(\mathfrak c_d)=[d\equiv2\pmod5]},
$$

$$
\boxed{
v_{(4-t)\mathcal O_K}(\mathfrak c_d)
 =[d\equiv15\pmod {19}]+[d\equiv205\pmod {361}]}.
$$

These two bounded local contributions cannot supply the exponential
content required by the norm route.  This is not a global content theorem:
prime divisors of the recurrence values may vary with (d), and no later
prime has been excluded all-degree.

The source, exact finite-state certificate, and byte-reproduced result
hashes are

    21fd8e0ff23d82abf67528c5d408a5b73c4c248535d2298d970a9fceaf97b401
    32d79a8293d2d83f2688de23e57b82ccdaf3d06e50807789a4a282f18fe8f653
    b5893282a8b5c86a686d88c552b4f2c20d596dfbd283592e84fd226f7201bec7

An independent temporary-directory rerun reproduced the archived JSON byte
for byte.

## 2026-08-27 — exact localization of the residual odd Fourier matching content

For the critical Fourier form, retain

$$
\frac{4S_{n,k}}{C_0}=\frac AB,\qquad
E_n=q_ne-p_n,\qquad
d=(q_n,B),\quad q_n=dq_0,\quad B=dB_0,
$$

and put (M=q_0A-B_0p_n).  The final matched content is
(g=(M,d)).  If an odd prime (\ell\mid d) has

$$
\alpha=v_\ell(q_n),\qquad \beta=v_\ell(B),
$$

then reducing (M) modulo (\ell) gives the exact exclusion

$$
\boxed{\alpha\ne\beta\Longrightarrow v_\ell(g)=0}.
$$

Indeed, when (\alpha>\beta), the term (q_0A) vanishes modulo
(\ell) while (B_0p_n) is a unit; the roles reverse when
(\beta>\alpha).  In the only remaining case
(\alpha=\beta=a>0), both reduced factors are units and

$$
q_nA-p_nB=\ell^aM.
$$

Consequently

$$
\boxed{
v_\ell(g)=\min\{a,v_\ell(q_nA-p_nB)-a\}}.
$$

Using (A/B=4S/C_0), this is the intrinsic normalized condition

$$
v_\ell(g)=\min\left\{a,
v_\ell\left(4\frac{q_n}{\ell^a}
\frac{\ell^aS_{n,k}}{C_0}-p_n\right)\right\}.
$$

If (S=T/L_K), an entirely integral version is

$$
v_\ell(g)=\min\{a,
v_\ell(4q_nT-p_nL_KC_0)-v_\ell(L_K)-v_\ell(C_0)\},
$$

provided the two initial valuations both equal (a>0), and it is zero
otherwise.  The same calculation yields

$$
(g,q_0B_0)=1,\qquad dg\mid q_nA-p_nB,\qquad
g^2\mid q_nA-p_nB.
$$

This exact criterion rules out several possible shortcuts but does not yet
bound the surviving exact-match part.  The certificate gives, among other
cases,

$$
(n,k,d,g)=(4,40,1001,143),\quad(8,110,169,169),
\quad(18,1004,343,343),
$$

so (g) can have two distinct primes, can be nonsquarefree, and can equal
(7^3).  Further exact cases have surviving primes
(227>189=K), (647>442=K), and (937>797=K); therefore no cutoff
(\ell\le K) is available.  These are finite counterexamples to proposed
bounds, not evidence that no subtler asymptotic estimate exists.

The frozen source, exact certificate, and byte-reproduced result hashes are

    ab841f81e2453b703976f1162c5a11ad5dfee8d212746779d731df90eb8350dd
    f0df3b9d60db170baf21145d742fb7e6fe66626c2805ebf3bf61eac2b2e03000
    ce52870d2c31b90a389d52cc19f704133fd2325e632aa40b3f93104ae058bb42

An independent rerun reproduced the result byte for byte.  The surviving
prime-power congruence remains the exact high-region obstruction; no
classification of (e+\pi) follows.

## 2026-08-27 — fully primitive closure in the very high Fourier region

The residual odd-content problem can be bypassed once (k) is a large
enough multiple of (n\log n).  For the primitive exponential beta pair,

$$
p_n=\sum_{j=0}^n a_{n,j},\qquad
q_n=(-1)^n\sum_{j=0}^n(-1)^ja_{n,j},\qquad
a_{n,j}=\frac{(n+j)!}{j!(n-j)!}.
$$

The exact quotient

$$
\frac{a_{n,j+1}}{a_{n,j}}
=\frac{(n+j+1)(n-j)}{j+1}\ge2
$$

shows, by a geometric-sum bound, that

$$
0<q_n\le p_n<2\frac{(2n)!}{n!}\le2(2n)^n,
\qquad
\log q_n\le n\log n+n\log2+\log2.
$$

For minimal same-sign matching, write (d=(q_n,B)), (q_n=dq_0),
(B=dB_0).  If (g) is the complete final content, the exact matching
lemma gives (g\mid d).  Positivity therefore yields the worst-case bound

$$
\Lambda_{n,k}^{\rm prim}
\ge\frac{q_0\mathcal L_{n,k}}g
=\frac{q_n\mathcal L_{n,k}}{dg}
\ge\frac{\mathcal L_{n,k}}{q_n}.
$$

No estimate for the prime factors of (d) or (g) enters this inequality.
Combining it with the accepted all-degree Fourier estimate

$$
\begin{aligned}
\log\mathcal L_{n,k}\ge{}&(k-n/2-1)\log2-3\log(k-1)\\
&+(n+1)\left(\frac12\log\frac nk-\log4\right)
-n\sqrt{\frac nk}-\frac n4-n\log\frac{1+\sqrt2}{2}-\log\pi
\end{aligned}
$$

and substituting (k=c n\log n) gives

$$
\frac1n\log\Lambda_{n,k}^{\rm prim}
\ge(c\log2-1)\log n-\frac12\log\log n+O_c(1).
$$

The lower bound is increasing in (k) throughout this region for large
(n), so every fixed (c>1/\log2) proves uniform divergence for all
(k\ge c n\log n).  The explicit rational constant (c=3/2) works
because ((3/2)\log2>1).  If the rational Fourier coordinate vanishes,
the already primitive match (q_n(e+\pi)-p_n\ge\pi n^n) diverges as well.

Thus the fully primitive critical-Fourier construction is now excluded in

$$
n<k\le\frac1{35}n\log n
\qquad\text{and}\qquad
k\ge\frac32n\log n,
$$

leaving only

$$
\frac1{35}n\log n<k<\frac32n\log n.
$$

The frozen proof hash is

    1d7eb71129c27efdb783480766f73f72f488e3069ffd9ff358460b1266d096f6

This is a no-go theorem for the construction, not a classification of
(e+\pi).

## 2026-08-27 — exact period congruence for the Bessel endpoint pair

The integral exponential-beta approximants use the integer sequences

$$
q_ne-p_n,
$$

with the normalization

$$
\frac1{n!}\int_0^1x^n(1-x)^ne^x\,dx
 =(-1)^n(q_ne-p_n)>0.
$$

The exact coefficient recurrence gives, for every pair of integers
$m\ge1$ and $n\ge0$,

$$
\boxed{p_{n+m}\equiv p_n\pmod m},\qquad
\boxed{q_{n+m}\equiv(-1)^m q_n\pmod m}.
$$

In particular, for every odd prime power $M=\ell^a$,

$$
\ell^a\mid q_n\quad\Longleftrightarrow\quad
\ell^a\mid q_{n\bmod M}.
$$

This is a useful finite-state reduction for the Bessel coordinate of the
Fourier matching problem, but it is not a uniform valuation bound.  The
exact certificate includes the genuine high-power examples
$7^4\mid q_{361}$ and $11^5\mid q_{1359}$.

The frozen source, certificate, and byte-reproduced result hashes are

    5c6b05cd1d2d8f73f60c3bbff7de79af1e2c422409a8061ceeffd3625fec251f
    de7e1af5e99be4a4ab2a649b5db1b4537fd2a2f106fbf0157bf22296a027f968
    dadd929044550714de3fff197caf2d6c6ff59485bd0ee62beeb21977a408762c

After correcting the sign convention in the explanatory integral, an
independent temporary-directory run again reproduced the archived JSON
byte for byte.

## 2026-08-27 — PNT matching gain and the generalized forced-prime ladder

A first prime-number-theorem estimate combined $d,g\le B$, $q_n\ge n^n$,
and the accepted Fourier lower bound to obtain

$$
\Lambda_{n,k}^{\rm prim}\ge
\frac{q_n\mathcal L_{n,k}}{B_{n,k}^2}.
$$

Together with the previously isolated prime band, this already extended
the low-region no-go result to every
$c<1/(2+3\log2)$ for $k\le c n\log n$ (and explicitly to $c=6/25$).
The checked proof is retained as a valid intermediate artifact, with hash

    3cdaa52c54065cd5556273a55734af8ed5a870def32d234c95326af7af8edc0b

The stronger result comes from a complete ladder of disjoint bands.  Put
$K=k-1$ and $\ell=K-n$.  If $p>\sqrt K$ is prime, $a\ge3$ is odd, and

$$
\frac{2K}{a+1}<p\le\frac{2\ell}{a},
$$

then the residual polynomial after the Frobenius factorization has degree
strictly below $p$ and its support misses every exponent congruent to $K$
modulo $p$.  Hence

$$
p\mid C_{mp}\quad (|mp|\le K),
$$

and therefore $p\mid C_0,T_{n,k},h_{n,k}$.  In the parametrization
$a=2j+1$, these are the disjoint intervals

$$
\frac K{j+1}<p\le\frac{2(K-n)}{2j+1},\qquad j\ge1.
$$

Taking first a fixed number of bands, applying the PNT, and then letting
that number tend to infinity proves that their squarefree product $H$
satisfies

$$
\log H=(2\log2-1+o(1))K
$$

uniformly when $n=o(K)$.  Since $H\mid h_{n,k}$, the actual primitive
Fourier denominator now obeys

$$
\log B_{n,k}\le(2+o(1))K+O(n).
$$

The same exact matching inequality then proves divergence for every

$$
c<\frac1{4-\log2},\qquad k\le c n\log n,
$$

and in particular for $k\le(3/10)n\log n$.  Together with the accepted
very-high theorem, this leaves precisely the presently unresolved strip

$$
\frac3{10}n\log n<k<\frac32n\log n
$$

for this fully matched construction.

The frozen proof, executable certificate, and byte-reproduced result hashes
are

    7015236e061be55c7aad4e6cea479db051ee174a4dcf785ce9566a457db6bd47
    d4519918c381ccccc79fb423bcfe1faa77e532351ad2b778a7a43853094aee6c
    8d0382ec18909ac4ae996cd9ae99ad75090b8bfe6bc36cffa85c219d68d361d1

The certificate was independently rerun in a temporary directory and its
JSON matched byte for byte.  This is a substantially sharper obstruction
to the construction, not a classification of $e+\pi$.

## 2026-08-27 — a general-prime criterion for the fifth-root content ideal

For the $n=5$ two-log edge, let

$$
P_r=r!A_r,\qquad C_r=r!B_r,\qquad a_r=P_r(1),
$$

and define in $F=\mathbb Q(\sqrt5)$

$$
N_r=P_r(\eta)P_r(\bar\eta),
$$

$$
T_r=\frac{P_r(\eta)C_r(\bar\eta)
              -P_r(\bar\eta)C_r(\eta)}{\zeta_5-\zeta_5^{-1}},
\qquad
\mathfrak J_r=(N_r,a_rT_r).
$$

For every odd prime $p\ne5$ and $r\equiv d\pmod p$, occurrence of $p$ in
the coordinate-content ideal $\mathfrak c_d$ forces

$$
p\mid N_{F/\mathbb Q}(\mathfrak J_r).
$$

For the base representative $0\le r<p$, this condition is also sufficient
for occurrence of $p$ in $\mathfrak c_r$.  The block identities behind the
criterion are

$$
P_d\equiv X^{mp}P_r,\qquad a_d\equiv a_r,
$$

$$
C_d\equiv X^{mp}(C_r+mL_pP_r)\pmod p;
$$

the determinant defining $T_r$ is invariant under the resulting
$C\mapsto C+\lambda P$ shift.  Thus every fixed prime is reduced to a
finite residue-class/common-zero problem.  An exact scan of every prime
$p\le1000$ finds only $(p,r)=(19,15)$, but no argument yet excludes new
primes uniformly as $p$ grows.

The frozen source, certificate, and byte-reproduced result hashes are

    e336c35e9f9983b7fe51b2d74be8ac69c4cb603fbb714ce97affecc73ae521ef
    d27256f9b8f6035b6e4e1ddb4ea1bb00ed9469077955cd15a85359c2ea8ac871
    6ff90333718db3a609bd192d95812ea2ca513c85b346fc716156f50869a79a26

The corrected explanatory wording for the preceding local $5$/$19$
theorem now has source hash

    7b8d2ff515503396d00a451657247bc558506b2658417e825889c3418efac2c8

with its proof and certificate unchanged.

## 2026-08-27 — denominator transfer on the remaining cyclotomic cone

For a selected two-coordinate trace, the exact Smith calculation gives

$$
g_d=\alpha_d\gcd\!\left(z_{1,d},
             \frac{\beta_d}{\alpha_d}z_{2,d}\right).
$$

This also records why replacing the coordinate gcd by an algebraic norm is
unsafe.  On the concrete remaining edge $\theta_d=u_7^d$, a convenient
integral pair is a positive integer multiple of the minimally cleared
pair and has coordinates

$$
(D_dC_d,-d!C_d+D_dE_d),\qquad D_d={!d}.
$$

Writing $\delta_d=(D_d,d!)$ and $D_{0,d}=D_d/\delta_d$, the exact
primewise argument yields

$$
\boxed{
\frac{D_{0,d}}{(D_{0,d},C_d)}\mid\frac{\mathcal A_d}{g_d}}.
$$

Moreover,

$$
\log D_{0,d}\ge\frac12d\log d-O(d),
$$

whereas the primitive edge value is asymptotic, up to fixed nonzero
factors, to

$$
\frac{|\mathcal A_d/g_d|}{d\varphi^d}.
$$

Consequently, a subfactorial upper bound on $(D_{0,d},C_d)$ would close
this linear ray.  The exact scan through $d=200$ has exceptional gcd only
at $d=4,8,12,28,199$; the last is $277$, a $366$-digit divisor.  These are
finite diagnostics, not such a bound.

The frozen source, executable certificate, and byte-reproduced result
hashes are

    50410ae9392eb6bfd51391c4d3f79aafeabddf18b04c5a0f83402f78d526d9bb
    98958867bf0be9f68db599f23ac1cb5e493e53a6eddd9763c348996f2bfad0af
    dd21c96bef979522e62917f327e56f633f7e7a02b2c3d798cb92bf9ccf87be53

An independent temporary-directory rerun reproduced the JSON exactly.

## 2026-08-27 — accelerated $u_7$ rays closed by a normalized $S$-unit gcd

Let $\theta_d=u_7^{t_d}$ with

$$
\frac{t_d}{d\log d}\longrightarrow\infty.
$$

After dividing each trace polynomial by one of its own monomials, both
polynomials have constant coefficient one; this normalization is essential
because projective polynomial height does not see a common scalar.  The
outside-$S$ and $S$-part generalized gcd estimates, applied on nested
exceptional subsets, then imply

$$
\boxed{\log g_d=o(t_d)}.
$$

The two possible character-degeneracy alternatives are excluded by the
multiplicative independence of the three cyclotomic units and by the
distinct exponent supports.  The coefficient heights are only
$O(d\log d)=o(t_d)$, so the resulting primitive trace diverges
exponentially.  Hence every accelerated ray in this family is rigorously a
no-go.  The result does not cover the fixed linear ray $t_d=d$, precisely
where the moving coefficient height is comparable to the exponent.

The frozen source, executable certificate, and byte-reproduced result
hashes are

    bef061a7613f03cfca470189356626acc8b65d3334d0b3d795f940c60261f4c5
    70f8489d1491c9ab6717a4e2c559c7073342e5f492a33a9df88b6e2b2debd40f
    57fb13f749cf5ddd383b6ef47202a378073c672b3650db7167336ab2e78a735a

The result was independently reproduced byte for byte.  The theorem uses
the outside-$S$ and $S$-part statements of Grieve--Wang separately; the
archived audit does not infer a full-gcd assertion from either proposition
alone.

## 2026-08-27 — exact first digit for the large-prime Fourier survivors

Let $K=k-1$ and consider the forced large-prime band

$$
K<p\le2(K-n).
$$

Put

$$
s=2(K-n)-p,\qquad u=p-K,\qquad d=2K-p,
$$

and write

$$
R(y)=P_n(y)(1+y)^s=\sum_{t=0}^d\rho_ty^t.
$$

The congruence

$$
(1+y)^p\equiv1+y^p+pH_p(y)\pmod {p^2},
\qquad
H_p(y)=\sum_{j=1}^{p-1}\frac{(-1)^{j-1}}j y^j,
$$

gives the exact central digit

$$
D=[y^K]R(y)H_p(y)\equiv C_0/p\pmod p.
$$

The reduction modulo $p$ has only the two blocks $R+y^pR$, so the exact
rational-coordinate digit is

$$
U=\sum_{t=0}^d\frac{\nu_{u+t}(\rho_t)}{u+t}
 \equiv S_{n,k}\pmod p.
$$

If $D\ne0$, then $v_p(C_0)=1$, and the accepted denominator and matching
formulas reduce to the reversible criterion

$$
\boxed{
p\mid g_{n,k}\Longleftrightarrow
v_p(q_n)=1,\quad U\ne0,\quad
4(q_n/p)U\equiv p_nD\pmod p.}
$$

The exceptional branch $D=0$ is exactly $p^2\mid C_0$.  Independently,
running the Bessel recurrence backward from its exact period proves, for
every odd $M$,

$$
p_{M-1-r}\equiv p_r\pmod M,\qquad
q_{M-1-r}\equiv q_r\pmod M.
$$

All three known survivors larger than $K$, namely $227,647,937$, lie on
the generic branch and pass the displayed final congruence.  Thus the
theorem localizes them but supplies no unsupported density assertion.

The exact grid checks 12,223 prime instances, 83 exceptional digits,
51,840 reflection congruences, and all three large examples.  The frozen
source, executable certificate, and independently byte-reproduced result
hashes are

    d0399cb1b08b8323ac9fc84c543148e7c22d7c53c356277a33ccaf89ca836639
    678cfa0219adb99180e07f080cbcb96164cdadd632c2b39d5f4b3a7d9099d314
    6fe7088f2095e1bf0c682a0068b1d8e8d6206cd56e257878b7e7fc891fc72836

This is a finite-state obstruction theorem, not a classification of
$e+\pi$.

## 2026-08-27 — forced top-prime-power Fourier bands

For an odd prime $p$, let

$$
Q=p^{\lfloor\log_pK\rfloor},\qquad Q\le K<pQ.
$$

If some odd integer $a\ge3$ satisfies

$$
\frac{2K}{a+1}<Q\le\frac{2(K-n)}a,
$$

then writing $2(K-n)=aQ+s$ and applying Frobenius at the full power $Q$
gives

$$
G_{n,k}(y)\equiv P_n(y)(1+y)^s(1+y^Q)^a\pmod p.
$$

The residual degree is strictly below the residue of $K$ modulo $Q$.
Therefore every coefficient in the corresponding congruence class
vanishes:

$$
\boxed{p\mid C_{mQ}\quad (|mQ|\le K).}
$$

If $Q\nmid m$, the factor $L_K/m$ already contributes $p$; if $Q\mid m$,
the displayed Fourier gap contributes it.  It follows term by term that

$$
\boxed{p\mid C_0,T_{n,k},h_{n,k}.}
$$

This extends the preceding theorem to primes with $p^2\le K$.  However,
every newly added prime is at most $\sqrt K$, so its total possible
logarithmic contribution is bounded by
$\vartheta(\sqrt K)=O(\sqrt K)$.  Consequently the forced product still
has the same leading mass

$$
(2\log2-1+o(1))K
$$

when $n=o(K)$.  One copy of each top-power prime therefore cannot improve
the current low-region threshold; higher $p$-adic digits would be needed.

The exact certificate checks 5,010 instances, including 614 genuinely new
$p^2\le K$ cases, and reproduces all coefficient and full-content
divisibilities.  The frozen source, executable, and independently
byte-reproduced result hashes are

    f3d4ea3cf815677eb06edb909a74b7588c78c7ee20c72ca0bf41e56a062a0bd2
    d1e21f2206344d1e8f628bb76ce7f9bd9bb7b5c9b8a0309363559007e374c7ae
    3523fdb032ede58325ce5f8f33b65b5c1448dc4a498cfc7e3773bdf4ec08bbc3

## 2026-08-27 — the exceptional large-prime digit is a fixed polynomial

For even $n$ and $0\le h\le n/2$, define

$$
A_{n,h}=\binom n{2h}\frac{(2n-2h)!n!}{(n-h)!},
$$

and

$$
\Phi_n(X)=\sum_{h=0}^{n/2}A_{n,h}2^h
                 \prod_{t=1}^h(X+2t-1)\in\mathbb Z[X].
$$

In the one-block band $K<p\le2(K-n)$, put
$\ell=K-n$ and $s=2\ell-p$.  Reindexing the exact super-Catalan central
coefficient, applying Wilson's theorem to its unique factorial crossing
$p$, and canceling the even factors gives

$$
\boxed{
D_{n,K,p}\equiv\frac{C_0}{p}
 \equiv-\frac{s!}{n!\ell!K!}\Phi_n(s)\pmod p.}
$$

Every denominator is a unit because $p>2n$ and $K<p$.  Since
$s\equiv2\ell\pmod p$,

$$
D_{n,K,p}=0\Longleftrightarrow
p\mid\Phi_n(2\ell).
$$

The leading coefficient
$2^{n/2}(n!)^2/(n/2)!$ is nonzero modulo every prime in the band, so the
degree remains exactly $n/2$.  It follows rigorously that a fixed pair
$(n,p)$ has at most $n/2$ exceptional $K$-values.  If
$\mathcal E_{n,K}$ denotes the squarefree product of exceptional primes
which also survive the final matching, then

$$
\boxed{
\mathcal E_{n,K}\mid
\gcd(q_n,\Phi_n(2(K-n))).}
$$

The positive-coefficient estimate currently gives only

$$
\log\mathcal E_{n,K}=O(n\log(n+K)),
$$

which is still factorial scale in the target strip.  The theorem therefore
turns the second-order branch into a fixed resultant-style problem but
does not close it or control the generic congruence branch.

The frozen source, executable certificate, and independently
byte-reproduced result hashes are

    aa6d00034325363866bb74660447df7191630a01e41370bfc395b256e38a8027
    25ecfabd51ccef3f0e118a528d44fe93572f839141729d0d0936d0db54b8faa7
    15da2f34a23934d9361ad01ebbc22b528c1ad535578430399f181357e5d16347

The exact grid contains 77,063 prime instances and 287 exceptional
digits; those counts are diagnostics, not asymptotic density claims.

## 2026-08-27 — maximal generic interpolation degree and the CRT ceiling

For $(n,p)=(64,937)$, all one-block parameters are

$$
K=533,534,\ldots,936.
$$

Writing $x=K-533$, the exact generic residue

$$
f_x=4(q_{64}/937)U_{64,K,937}-p_{64}D_{64,K,937}pmod {937}
$$

satisfies

$$
\boxed{\Delta^{403}f_0=513\ne0\pmod {937}}.
$$

Therefore its unique interpolating polynomial on the $404$ admissible
points has the maximum possible degree $403$.  No raw polynomial in $K$
of degree at most $402$ represents the congruence there.  The only generic
zero is $K=797$, exactly the previously certified survivor.  This refutes
the proposed low-degree raw interpolation route, while leaving open a
relation after nontrivial factorial, character, rational, or
hypergeometric normalization.

There is also an all-parameter CRT statement.  Define

$$
Z_{n,K}=4q_nT_{n,k}-p_nL_KC_0.
$$

If $\mathcal G^{\rm gen}_{n,K}$ is the squarefree product of generic
large-prime survivors, exact local matching and the CRT give

$$
\boxed{
\mathcal G^{\rm gen}_{n,K}\mid q_n,
\qquad(\mathcal G^{\rm gen}_{n,K})^2\mid Z_{n,K}.}
$$

The coefficient one-norm supplies the explicit bound

$$
|Z_{n,K}|\le15q_nL_K2^{2K+n/2}.
$$

At $K\sim c n\log n$, its square root has leading logarithm

$$
\frac12\{1+c(1+2\log2)\}n\log n.
$$

For $c\ge1/(1+2\log2)$ this is no smaller than the existing
$\mathcal G^{\rm gen}\le q_n$ bound at leading order.  Thus the direct
CRT-plus-archimedean-size method cannot provide the needed subfactorial
control in the upper strip.  In all three known generic examples the
surviving prime has exactly $v_p(Z)=2$, so the square divisibility is not
silently being treated as a higher-power theorem.

The frozen source, executable certificate, and independently
byte-reproduced result hashes are

    f032fb826ae02d96e9ef7f559e583970af77d9351b657efc99b8aae238d41247
    d0570837cc06e518093b331fdb43554b2dd53b648332d7bfd37b92cddcc358c4
    c9a325f14cee396299afbda0b9adc8be306f599e9f1aa7cd6045834d3780ebcd

## 2026-08-27 — exact local reduction of the fixed $u_7^d$ selected gcd

For the denominator-transfer edge, set

$$
D_d={!d},\quad D_{0,d}=D_d/(D_d,d!),\quad
X_d=\operatorname {Tr}_{K/\mathbb Q}
 \bigl(u_7^dP_d(\eta)P_d(\bar\eta)\bigr),
\quad C_d=2\ell_dX_d,
$$

where $\ell_d=\operatorname {lcm}(1,\ldots,d)$.  Primewise valuation
comparison gives the all-degree separation

$$
\boxed{
(D_{0,d},X_d)\mid(D_{0,d},C_d)
\mid2\ell_d(D_{0,d},X_d).}
$$

Since $\log\ell_d=O(d)$, the desired
$o(d\log d)$ estimate is equivalent with or without the lcm factor.
The exact local formula is

$$
v_p(D_{0,d},C_d)=\min\!\left(
 \max\{v_p(D_d)-v_p(d!),0\},
 v_p(2)+\lfloor\log_p d\rfloor+v_p(X_d)\right).
$$

Writing $A_d=(-1)^dD_d$ gives $A_0=1$ and
$A_d=1-dA_{d-1}$, from which

$$
A_{d+m}\equiv A_d\pmod m
$$

follows in every modulus.  Combining this with
$P_d(X)=X^d-dP_{d-1}(X)$ and the powers of
$\eta,\bar\eta,u_7$ gives an exact finite joint state.  For
$p\nmid20$, $f_p=\operatorname {ord}_{20}(p)$, the universal period

$$
T_{p,k}=p^k(p^{f_p}-1)
$$

works modulo $p^k$.  The simultaneous $A,X$ roots therefore form an
exact nested $p$-ary lift tree.  The factorial offset is essential:

$$
p^a\mid(D_{0,d},X_d)
\Longleftrightarrow
p^{a+v_p(d!)}\mid A_d\ \hbox{ and }\ p^a\mid X_d.
$$

When $p>d$, this becomes the denominator-free pair

$$
E_d(-1)\equiv0,\qquad
\operatorname {Tr}_{K/\mathbb Q}
 \bigl(u_7^dE_d(-\eta)E_d(-\bar\eta)\bigr)\equiv0\pmod {p^a}.
$$

The exact diagnostic through $d=1000$ finds
$(D_{0,d},C_d)>1$ only at
$(4,3),(8,13),(12,11),(28,31),(199,277)$, and after removing the lcm
only at $(8,13),(28,31),(199,277)$.  These finite records are not
extrapolated.  The missing theorem is a uniform bound on the total depth
and size of the simultaneous branches as $p,d$ vary.

The original frozen source contained accidental control-character TeX
escapes and was rejected before integration.  After a complete raw-byte
repair, two precision corrections, Pandoc validation, a zero-control-byte
scan, and an independent byte-identical rerun, the accepted hashes are

    8b8e6d8bf552501f052caa06a134e3992415fe4eb4e2bb2eed6ce27c5b98cfc3
    890ce392e9c0473b70fd4b56d15b74ec36aad8dad97d3b5b74eed7beb128333d
    0050306982a3e0d37173d73f6b4583ba94c2e50b61de1551f577d4cffd53b1f4

## 2026-08-27 — exact common-zero reductions for the $n=5$ ideal content

The general-prime ideal-content obstruction was reduced to three
base-representative common-zero problems.  Let

$$
x=\eta,\qquad y=\bar\eta=\zeta_5x,\qquad
u=x^{-1}=1+\zeta_5,\qquad v=y^{-1}=1+\zeta_5^{-1},
$$

and put $A=u+v=uv$, so $A^2-3A+1=0$.  For

$$
K_d(X)=P_d(\zeta_5X)-\zeta_5^{d+1}P_d(X),\qquad
h_d=\frac{K_d(x)}{(1-\zeta_5)y^d},
$$

the recurrence for $P_d$ proves, for $p>d$ and $p\ne5$,

$$
P_d(x)=P_d(y)=0
\quad\Longleftrightarrow\quad
h_d=h_{d-1}=0.
$$

The exact exponential generating function is

$$
\sum_{d\ge0}h_d\frac{z^d}{d!}
 =\frac{e^z}{1+Az+Az^2}.
$$

Consequently the simultaneous zero condition is equivalent to
$(1+Az+Az^2)\mid E_d(z)$, where
$E_d(z)=\sum_{j=0}^dz^j/j!$.  The denominator admits the five-step
identity

$$
(1+Az+Az^2)
\left(1-Az+(2A-1)z^2+(1-2A)z^3\right)
 =1-(5A-2)z^5,
$$

and $N_{\mathbb Q(\sqrt5)/\mathbb Q}(5A-2)=-1$.  This yields an
exact first-order recurrence along the five residue classes.

The other two alternatives also have exact truncated-exponential
descriptions:

$$
P_d(1)=P_d(x)=0
\quad\Longleftrightarrow\quad
(1+z)(1+uz)\mid E_d(z),
$$

and

$$
P_d(x)=C_d(x)=0
\quad\Longleftrightarrow\quad
\lambda=0\ \hbox{is a multiple root of}\
\mathcal F_d(\lambda,u)
 =d![z^d]\frac{e^z(1+z)^\lambda}{1+uz}.
$$

Together with the exact block reduction $d\mapsto d\bmod p$, these
three cases exhaust the prime-ideal obstruction.  They are genuine
finite algebraic reductions, but none presently proves uniform
nonvanishing as $p$ varies.  The finite scan is retained only as a
diagnostic.

The source underwent a full line-by-line proof audit.  During review an
overbroad degree quantifier was narrowed to the base representative, the
block equalities were correctly stated as congruences, and an unmatched
display delimiter was repaired.  The final program was then rerun
independently and reproduced its archived JSON byte for byte.  Accepted
SHA-256 hashes:

    e95917203a9dcc6f6de309c520c1f972574d4a6c57279f24e07e02005c43b5dd
    c7e011200c3eb117f01657e31d580c393e80683247bae282a5a904db489b709f
    2ad88018f712662af1084d291def3c3e3d6602f59fd27f2286db089df45cac4f

## 2026-08-27 — the five-step $p$-boundary is an exact reset

Writing

$$
\frac1{1+Az+Az^2}=\sum_{j\ge0}q_jz^j,
$$

the coefficients $q_j$ satisfy a five-step geometric relation, and
convolution with the truncated exponential gives an exact formula for
$h_d$.  Modulo $p$, the sequence $h_d$ is $p$-periodic.  However,
at the five indices $p,p+1,\ldots,p+4$, the multiplier in every
five-step recurrence contains $p$.  Each chain is therefore reset
directly to its initial value.  The pre-boundary data are erased, so
matching across $p$ supplies no additional terminal equation.

Wilson's theorem makes the two free endpoint values explicit:

$$
h_{p-1}=\sum_{j=0}^{p-1}(-1)^jj!q_j,\qquad
h_{p-2}=\sum_{j=0}^{p-2}(-1)^j(j+1)!q_j.
$$

More generally, if $m=p-1-d$, then

$$
P_d(x)=\frac{x^d}{m!}\sum_{j=0}^d(m+j)!u^j,\qquad
P_d(y)=\frac{y^d}{m!}\sum_{j=0}^d(m+j)!v^j.
$$

Thus the simultaneous $P$-zero condition is precisely a pair of
weighted left-factorial congruences.  Frobenius supplies no new equation
when $p\equiv1\pmod5$, swaps the pair when $p\equiv4\pmod5$, and
supplies all four cyclotomic conjugates when $p\equiv2,3\pmod5$.
These are exact identities, but they do not classify their zero sets.
In the certified finite box the only hit is $(p,d)=(19,15)$; this is
not extrapolated.

Every displayed recurrence, Wilson conversion, boundary value, and
finite certificate was checked independently.  The script reproduced
the archived output byte for byte.  Accepted SHA-256 hashes:

    ce1384d383a4a184456536ab16871faf5d6129c3e869f7a8ccf82be3ea272582
    54a74d69f15835727b0d8ca5073205f2b3ff3691afa49be06d89b0edb532a38a
    46325a91dbd4c2dadb6a95313fe769d50a432922398043e2383c0b026b1cee86

## 2026-08-27 — factorial tails and the large-prime trace obstruction

For the fixed ray $\theta_d=u_7^d$, let $p>d$ and
$r=p-1-d$.  Define

$$
S_{p,r}(Y)=\sum_{k=r}^{p-1}k!Y^k.
$$

Wilson's theorem gives the exact congruence

$$
E_d(-x)=-x^{p-1}S_{p,r}(x^{-1})\pmod p.
$$

The first large-prime congruence is $S_{p,r}(1)=0$.  The differential
identity

$$
Y^2S'_{p,r}(Y)+(Y-1)S_{p,r}(Y)=-r!Y^r
$$

shows that this root is simple.  Hence, writing
$S_{p,r}(Y)=(Y-1)Q_{p,r}(Y)$, one has
$Q_{p,r}(1)=-r!\ne0$.

Set $q=\eta\bar\eta$, $z=q^{-1}$.  Since
$\eta^{-1}$ and $\bar\eta^{-1}$ are the roots of
$Y^2-zY+z$,

$$
E_d(-\eta)E_d(-\bar\eta)
 =q^{p-1}\operatorname {Res}_Y
   \left(Y^2-zY+z,Q_{p,r}(Y)\right)\pmod p.
$$

Frobenius also gives

$$
u_7^d=\sigma_p(u_7)u_7^{-r-1}.
$$

The remaining condition is therefore one trace over
$\mathcal O_{\mathbb Q(\sqrt5)}/p$, rather than the separate
vanishing of the two conjugate resultant factors.  In split residue
classes it has the form $y_++y_-=0$; in inert classes it is
$y+y^p=0$.  Neither implies that an individual factor vanishes.
The certified nonzero cancellation witnesses

$$
(p,d)=(13,8),(31,28),(277,199),(1879,1427)
$$

cover every quotient Frobenius class.  When the factors are nonzero, the
trace equation can also be written as an exact norm-one ratio between
the two conjugates of the unit coefficient and the moving resultant.
Because the latter is a factorial sum with moving degree and moving
quadratic characteristic, this is not a fixed-target $S$-unit
equation.  The reduction is therefore exact but not a uniform gcd
theorem.

The full derivation and every finite witness were audited, and an
independent rerun reproduced the archived JSON byte for byte.  Accepted
SHA-256 hashes:

    b1bc06b4915b0e014cb5bd52433345aa130834b09ec6d932cf968504fc880838
    d7f8a2e191f04f2ff5a677954087cb7cba2b5ba4eed1d3baaf385e0822a624d0
    ef9ae8f082329c5024d370f92b138f78f6389a444fbc0c0019b73ad558bf06fe

## 2026-08-27 — normalized three-state recurrence for the Fourier digit

Fix even $n\ge2$, an odd prime $p>2n+1$, and

$$
c=\frac{p-2n-1}{2},\qquad
s_v=2v+1,\qquad
K_v=n+\frac{p+s_v}{2},\qquad
u_v=c-v.
$$

For $0\le v\le c-1$, write

$$
P_n(z)=(1-i)^n(z-1)^n(z-i)^n,\qquad
R_v(z)=P_n(z)(1+z)^{2v+1},
$$

and define the formal endpoint moments

$$
I_v=\int_1^iz^{u_v-1}R_v(z)\,dz,\qquad
J_v=\int_1^iz^{u_v}R_v(z)\,dz.
$$

Their degrees are at most $p-2$, so every formal integration
denominator is a nonzero scalar modulo $p$.  Direct coefficient
comparison gives

$$
U_{n,K_v,p}=\operatorname {Im}I_v.
$$

Set

$$
A(z)=P_n(z)(1+z)z^{c-1},\qquad
w(z)=\frac{(1+z)^2}{z},\qquad
\Delta=z(z+1)(z-1)(z-i).
$$

Integrating the derivatives of
$(\Delta/z)Aw^v$ and $(\Delta/z^2)Aw^v$ gives two exact linear
relations among

$$
I_v,\ I_{v+1},\ I_{v+2},\ J_v,\ J_{v+1}.
$$

The endpoint terms vanish because of the factors
$(z-1)^{n+1}(z-i)^{n+1}$; the characteristic-$p$ degree bounds were
checked separately.  Solving the first relation for $J_{v+1}$ and the
second for $I_{v+2}$ yields

$$
(I_v,I_{v+1},J_v)\longmapsto
(I_{v+1},I_{v+2},J_{v+1})
$$

for $0\le v\le c-3$.  The two pivots are

$$
c+2n+v+3,\qquad i(c-v-2).
$$

Their scalar factors lie respectively in
$[c+2n+3,p-1]$ and $[1,c-2]$, so both are units even when
$\mathbb F_p[i]$ splits.

The exceptional-digit theorem supplies

$$
D_{n,K_v,p}=\kappa_v\Phi_n(2v+1),\qquad
\kappa_v=-\frac{(2v+1)!}{n!\ell_v!K_v!}.
$$

Every factorial is a unit.  After setting
$\widetilde I_v=\kappa_v^{-1}I_v$ and
$\widetilde J_v=\kappa_v^{-1}J_v$, the same recurrence has explicit
rational transition coefficients, and the generic matching equation is

$$
4(q_n/p)\operatorname {Im}\widetilde I_v
 =p_n\Phi_n(2v+1)\pmod p.
$$

This normalization does not force a unique return.  For
$(n,p)=(82,953)$,

$$
q_{82}\equiv953\cdot149\pmod {953^2},\qquad
p_{82}\equiv662\pmod {953},
$$

and the target residual vanishes at exactly

$$
(v,K)=(55,614),\qquad(281,840).
$$

Both points are generic: their $(D,U)$ pairs are respectively
$(405,210)$ and $(402,632)$, with neither coordinate zero.
I independently reconstructed the entire $394$-point target sequence
through the two split-field embeddings
$i\mapsto442,511\in\mathbb F_{953}$; it had precisely those two zeros.
The two rational-function identities underlying the recurrence were also
expanded symbolically over
$\mathbb Q(i,n,c,v,z)$ and reduced identically to zero.

The first frozen source, hash

    111a834d75698bef8e348be752e35fc5930ea60bbe9ef78bccae71e000859cef

contained literal control-byte TeX escapes and is rejected.  The source
was rebuilt, scanned bytewise, parsed through Pandoc with warnings made
fatal, and the certificate was independently rerun byte for byte.  The
accepted SHA-256 hashes are

    39b294088c33eacfcd08db22a8ee6537c55971ec65a574c9440fe5c366f02461
    6a758d9a304d78220ad19dbf9c47af20e61d8d8e103ac00a2aac8a84feaee482
    f761dd82e80ffe1ff76f972cc2a32210ae07402075a81974d14735b5a71c3023

The result supplies a compact holonomic description and rules out an
at-most-one argument.  It does not prove a bounded zero count, a useful
product bound for surviving primes, or any classification of $e+\pi$.

## 2026-08-27 — primitive norm-one formulation of the large-prime ray

The nonzero large-prime cancellation had already been reduced to

$$
\frac{\iota(\mathcal N_{p,r})}{\mathcal N_{p,r}}
 =-\frac{\chi_pW_{c,r}}
         {\iota(\chi_p)\iota(W_{c,r})}
\quad\hbox{in }\mathcal O_{\mathbb Q(\sqrt5)}/p.
$$

To remove its visible factorial scalar canonically, define

$$
\widehat Q_{p,r}(Y)
 =\sum_{k=r}^{p-1}k!\frac{Y^k-1}{Y-1},
\qquad
R_{p,r}(Y)=\frac{\widehat Q_{p,r}(Y)}{r!}.
$$

Under the derangement root
$\sum_{k=r}^{p-1}k!=0\pmod p$, the first polynomial reduces to the
quotient $Q_{p,r}$ from the boundary theorem.  Since the characteristic
polynomial is quadratic,

$$
\mathcal N_{p,r}=(r!)^2\mathcal M_{p,r},\qquad
\mathcal M_{p,r}
 =\operatorname {Res}_Y(Y^2-zY+z,R_{p,r}),
$$

and the scalar $(r!)^2$ cancels exactly from
$\iota(\mathcal N)/\mathcal N$.

The normalized polynomial family has the triangular recurrence

$$
R_{p,p}=0,\qquad
R_{p,r}=L_r+(r+1)R_{p,r+1},
\qquad L_r=\frac{Y^r-1}{Y-1}.
$$

After evaluation at the two fixed quadratic roots, a six-coordinate
state—and therefore its tensor-product resultant state—has bounded
dimension.  Its terminal condition nevertheless sits at the moving
index $p$.

If $0\le r\le p-2$ and
$R_{p,r}=\sum_jc_jY^j$, then

$$
c_j=\sum_{k=\max(r,j+1)}^{p-1}\frac{k!}{r!}.
$$

For $r\ge1$, $c_{r-1}-c_r=1$; for $r=0$,
$c_0-c_1=1$.  Thus the coefficient content is exactly one in every
nonconstant case.  Its leading coefficient is $(p-1)!/r!$, and

$$
\frac{(p-1)!}{r!}
\le H(R_{p,r})
\le(p-r)\frac{(p-1)!}{r!}.
$$

Consequently

$$
\log H(R_{p,r})
 =\sum_{k=r+1}^{p-1}\log k+O(\log(p-r)).
$$

This is $\Theta(p\log p)$ when $r/p$ stays in a compact subinterval
of $(0,1)$, and it is
$d\log p+O(d^2/p+\log(d+1))$ when $d=p-1-r=o(p)$.
The statement concerns the primitive coefficient vector only.  It does
not infer a comparable height for the evaluated torus point, where
substantial cancellation may occur.

Finally, for

$$
\mathbb T_p=\{t:t\iota(t)=1\},\qquad
\delta_p(x)=\frac{\iota(x)}x,
$$

the map $\delta_p$ is surjective.  In the split algebra this is
$(x_+,x_-)\mapsto(x_-/x_+,x_+/x_-)$; in the inert field it is
$x\mapsto x^{p-1}$, whose image has order $p+1$.  Therefore the
norm-one condition alone cannot restrict the cancellation.  The ambient
coefficient prime support also grows with $p$, so no fixed-$S$
theorem applies directly.

I checked every coefficient identity, the $r=0$ and $d=1$ edge
cases, the quadratic resultant scaling, and the split/inert Hilbert-90
argument.  An independent run reproduced the JSON byte for byte, and a
separate sweep verified primitivity and torus surjectivity for additional
small primes.  Accepted SHA-256 hashes:

    d072cc5adf7634ca2a046db02608fbe85d6f5e6ea6e9fb4843e9ccad05deaf0c
    caa7c133bc41684bc34c14d3228fbc1576e21171bcfb5f2e9568828adc779e5a
    a04649b038e1cc14f9ddab23093f76259ab5d45466a34fc2eb0eee539a4ec93c

This precisely eliminates three shortcuts—visible factorial content,
bounded recurrence dimension by itself, and mere torus membership—but
does not bound the selected gcd or classify $e+\pi$.

## 2026-08-27 — coupling the two weighted left-factorial equations

Let $p\ne5$ be odd, $0\le d<p$, $m=p-1-d$, and

$$
W_m(Z)=\sum_{j=0}^{d}(m+j)!Z^j\in\mathbb F_p[Z].
$$

For $u=1+\zeta_5$, $v=1+\zeta_5^{-1}$, the previously derived
complementary identities show that the simultaneous $P$-zero is exactly

$$
W_m(u)=W_m(v)=0.
$$

The factorial ratio, including its terminal coefficient, gives the exact
polynomial differential equation

$$
\boxed{
Z^2W_m'(Z)+((m+1)Z-1)W_m(Z)=-m!}\pmod p.
$$

The possible coefficient of $Z^{d+1}$ is
$(m+d+1)(m+d)!=p(p-1)!$, so no boundary term was discarded.

Put $A=u+v=uv$ and

$$
q(Z)=Z^2-AZ+A=(Z-u)(Z-v).
$$

Write

$$
W_m(Z)\equiv a_m+b_mZ\pmod {q(Z)}.
$$

Away from $5$, the evaluation matrix at $u,v$ is invertible, hence

$$
W_m(u)=W_m(v)=0
\quad\Longleftrightarrow\quad
a_m=b_m=0.
$$

The product resultant is

$$
\mathcal R_m=a_m^2+Aa_mb_m+Ab_m^2.
$$

If $\mathcal I_m=(a_m,b_m)$, then

$$
(b_m,\mathcal R_m)=(b_m,a_m^2),\qquad
\mathcal I_m^2\subseteq(b_m,\mathcal R_m)\subseteq\mathcal I_m.
$$

Thus the two ideals have the same radical, whereas the resultant by itself
does not detect the true common zero.

The complementary recursion is

$$
\binom{a_m}{b_m}
 =\binom{m!}{0}
  +\begin{pmatrix}0&-A\\1&A\end{pmatrix}
   \binom{a_{m+1}}{b_{m+1}}.
$$

The matrix has eigenvalues $u,v$, and, with
$\kappa=5A-2$,

$$
M^5=-\kappa I.
$$

This recovers the exact five-block recurrence directly at the level of
the linear remainder.

There is also a prescribed double-root formulation.  Define

$$
H_m(Z)=W_m(\zeta_5^{-1}Z)-\zeta_5W_m(Z).
$$

Every coefficient with index $4\bmod5$ vanishes, and coefficientwise
use of the differential equation proves

$$
Z^2H_m'(Z)
 =(\zeta_5-(m+1)Z)H_m(Z)
  +\zeta_5(\zeta_5-1)W_m(Z).
$$

Since $\zeta_5^{-1}u=v$, this gives the equality of localized ideals

$$
\boxed{
(W_m(u),W_m(v))=(H_m(u),H_m'(u)).}
$$

The simultaneous zero is therefore precisely the assertion that the
fixed cyclotomic unit $u$ is a multiple root of the lacunary polynomial
$H_m$.

The product-only failure is already exact over $\mathbb F_{11}$:
for $d=4,m=6,\zeta_5=4$,

$$
W_6(5)=3,\qquad W_6(4)=0,
$$

while the remainder is $10+3Z$.  Hence the resultant vanishes but the
true two-generator ideal is the unit ideal.  This does not refute the
stronger conjecture that the true common support is only $19$.

The full source was line-audited.  I independently checked the boundary
coefficient, the resultant-ideal inclusions, the five-block matrix law,
the differential coupling, and the $p=11$ counterexample.  A resumable
independent run over every complementary index for all eligible primes
through $200$ reproduced the JSON byte for byte.  Accepted SHA-256
hashes:

    15bfc2bc01a61c9e0361c891995643e470f383acfd88ae13e14293fbfe4062ba
    63b2c86ef7017bef8e74d4eba839f101750e0e35be4528c837c46ab8185e650a
    0f2ed32b823ff9cec0e9d802378ce63749e454cbcc46d92f514296b3ccb48dfb

The exact finite scan still has only the true hit $(p,d)=(19,15)$, but
that observation remains diagnostic.  No all-prime support theorem or
classification of $e+\pi$ follows.

## 2026-08-27 — Pointed Euler double root and bounded-eliminant barrier

Invariant-ring normalization gives



$$
{\cal E}_{2m}(X)=X(X-1)P_m(X(X-1)),\qquad P_m\in\mathbb Z[U]
$$



with $P_m$ monic of degree $m-1$.  If
$d\mid E_{2m},E_{2m-2}$, then $U=-1/4$ is a double root modulo
the full odd modulus $d$, proving
$d\mid\operatorname{Disc}(P_m)$.  The normalized discriminant still
has a linear-size Sylvester matrix and an $O(M^2\log M)$ height bound.

The complete modular computation at $M=3288,\ p=151483$ gives gcd
degree exactly one for $P_{1644}$ and its derivative.  Thus there is
one double root and no second multiple root; the next principal
subresultant is nonzero.  Appell and shift jets supply no additional
bounded family of congruences.  This refutes a universal
higher-subdiscriminant route without excluding noncanonical eliminants.

~~~
8cecdea69be6432aac7f3dee4e8851e31977b2a9dce00f44620931e249353550  sources/root_unity_adjacent_euler_bounded_eliminant_no_go.md
2fd8c166a342e368bfc56d2c8391fd2b7dcae11eb9ef8897c02d41084da6475b  scripts/root_unity_adjacent_euler_bounded_eliminant_certificate.py
6792b17675377119323f546a61776fe533a5baefcdc5248725c65b76b50b0eab  results/root_unity_adjacent_euler_bounded_eliminant_certificate.json
6c451189b41e7ddaa3563da40a4c119a159c2442a873c6451c2bda8665c53dfe  results/root_unity_adjacent_euler_bounded_eliminant_hashes.sha256
~~~

Independent replay took $3.1$ seconds and $77{,}004$ KiB.  No
first-period product bound or classification follows.

## 2026-08-27 — Factorial-Pascal endpoint theorem and extended scan

The balanced diagonal secant Padé equations become a signed
even-binomial matrix after writing numerator and denominator coefficients
in the $(2i)!$ basis.  Its positive cofactors $d_i$, their binomial
transforms $e_k$, and exact Euler convolutions $w_m$ give



$$
C_q^{\rm prim}(x)=
 \operatorname{prim}\!\left(
 (8q+2)(8q+1)w_{4q}+w_{4q+1}x\right).
$$



Hadamard on the Pascal rows proves



$$
\log H(C_q^{\rm prim})
 \le3(\log2)q^2+O(q\log q).
$$



The theorem and $q\le12$ certificate are frozen at:

~~~
5e1fdadfd00705921fa05f97472af266d5eaf86ed9c70c67bab7547f47729c07  sources/centered_cosh_factorial_pascal_height_theorem.md
50086d13c37301566fa2e500d495b49bbfa7ee116d02b52a9cb298936b898e28  scripts/centered_cosh_factorial_pascal_height_certificate.py
aa27ea7ef6ba580a76947d4e50f287ee921f40bea751c5f8ef0d19ecf2620e2d  results/centered_cosh_factorial_pascal_height_certificate.json
9c607dca829bbb5b9f7255a8a5c37563c41523fea6524643c4ea893add5956a4  results/centered_cosh_factorial_pascal_height_hashes.sha256
~~~

A disjoint resumable FLINT scan covers every $13\le q\le100$.  At
$q=100$, $\log H_{\rm prim}/q^2=1.562189\ldots$, the primitive
height has 22,538 bits, and the content has 861 bits.  No anomalous
collapse appears.  Sampled contents through $q=100$ are
$(8q+2)$-smooth with maximum observed exponent five, but this is
finite evidence only.

~~~
0b7bb1ab95581ec660d5b1c4445e5d2e3a45247521500e4d450e0e66499b12e2  sources/centered_cosh_factorial_pascal_extended_scan.md
a43d49d009a1aa6a976097f42fecfd2ec8903538518ccff7c8abd860b73d39c9  scripts/centered_cosh_factorial_pascal_extended_scan.py
5b562dc109f2a247ba4094bea8078826c7cc5ac3c04fe75f9452ae93387359f6  results/centered_cosh_factorial_pascal_extended_scan.json
00c68385ad3fbcbf61f821cf9c5fb47b5a0a841cfd28667849c86dfbbbdb5249  results/centered_cosh_factorial_pascal_extended_scan_hashes.sha256
~~~

The theorem replay used about $65$ MiB; the extended scan peaked near
$1.56$ GiB under a 12-GiB guard, leaving about $47$ GiB available.
The GPU was not useful for exact integer nullspaces.  The quadratic
height scale remains larger than the $2q\log q+O(q)$ analytic gain,
so this does not classify $e+\pi$.

## 2026-08-27 — the evaluated large-prime resultant returns to the original trace

Let $1\le d<p$, $r=p-1-d$, and assume the derangement root
$E_d(-1)=0\pmod p$.  Put

$$
a=\eta^{-1},\qquad b=\bar\eta^{-1},\qquad
Z_d=P_d(\eta)P_d(\bar\eta).
$$

The boundary tail satisfies

$$
E_d(-x)=-x^{p-1}S_{p,r}(x^{-1}),\qquad
S_{p,r}=(Y-1)Q_{p,r}.
$$

For the primitive lift $R_{p,r}=Q_{p,r}/r!\pmod p$, Wilson's exact
sign

$$
d!r!=(-1)^{d+1}
$$

and
$P_d(X)=(-1)^dd!E_d(-X)$ give

$$
R_{p,r}(a)=a^{p-1}\frac{P_d(\eta)}{a-1},\qquad
R_{p,r}(b)=b^{p-1}\frac{P_d(\bar\eta)}{b-1}.
$$

Since $ab=q^{-1}$ and $(a-1)(b-1)=1$,

$$
\boxed{
\mathcal M_{p,r}=R_{p,r}(a)R_{p,r}(b)
 =q^{-(p-1)}Z_d=\chi_p^{-1}Z_d.}
$$

Thus the large primitive coefficient height of $R_{p,r}$ does not
survive evaluation.

The same scalar $\chi_p$ occurs in the fixed-ray norm-one equation and
cancels.  Frobenius identifies the remaining unit trace with

$$
T_d=\operatorname {Tr}_{K/F}(u_7^d),\qquad F=\mathbb Q(\sqrt5),
$$

so the quotient equation is equivalent, after cross multiplication, to

$$
\boxed{\operatorname {Tr}_{F/\mathbb Q}(Z_dT_d)=0\pmod p.}
$$

This remains meaningful even in the zero-factor branches.

With $t=\zeta_5+\zeta_5^{-1}$, $t^2+t-1=0$, write

$$
Z_d=z_0+z_1t,\qquad T_d=w_0+w_1t.
$$

The trace equation becomes

$$
2z_0w_0-z_0w_1-z_1w_0+3z_1w_1=0.
$$

Its pairing matrix

$$
\begin{pmatrix}2&-1\\-1&3\end{pmatrix}
$$

has determinant $5$.  For $p\ne5$ this is a nondegenerate
bidegree-$(1,1)$ rational graph: every projective $Z$ has exactly one
projective trace-orthogonal $T$.  Membership on the graph therefore
supplies no ambient finiteness or subgroup constraint.

The sequence $Z_n$ does admit a fixed order-four recurrence

$$
\sum_{j=0}^4(A_j(n)+tB_j(n))Z_{n+j}=0,
$$

whose explicit coefficient polynomials are recorded in the source and
were verified by a symbolic four-dimensional tensor transition.  The unit
trace has the simpler recurrence

$$
T_0=2,\qquad T_1=4+2t,\qquad
T_{n+2}=(4+2t)T_{n+1}+(2+t)T_n.
$$

These fixed recurrences compress the dynamics but do not control primes
in their intersection with the derangement roots.

There is a sharp endpoint warning.  At $r=0$, $d=p-1$, the
derangement equation is

$$
\sum_{k=0}^{p-1}k!=0\pmod p.
$$

Excluding this equation for every odd prime is precisely the prime case
of Kurepa's left-factorial conjecture.  The simultaneous $u_7$-trace
condition is stronger, so a joint theorem need not settle Kurepa in full;
nevertheless, any strategy that first classifies all derangement roots
encounters that open barrier.

I audited the Wilson signs, forced-factor product, Frobenius cancellation,
trace coordinates, graph nondegeneracy, and recurrence construction.
The symbolic certificate reran independently and reproduced its JSON
byte for byte.  Accepted SHA-256 hashes:

    8b69327750e6bab181e78f50d5b8a60bf97f3f1d6632254ad9b1493cc600a534
    fd13a77fe5c97f5ca16fbb0eafa92c66f653ab126f03fd23c514770b32855487
    a82cf461b71a617e4b394e1efbe6d4a501e625269f38d150ed7d06d93e0679e0

The evaluated compression is exact but returns to the original
prime-intersection problem.  It supplies no selected-gcd bound and no
classification of $e+\pi$.

## 2026-08-27 — all three $n=5$ branches as prescribed first jets

The weighted-factorial differential coupling extends uniformly.  For
units $c,r$, with $c^{-1}-1$ also a unit, define

$$
H_{m,c}(Z)=W_m(cZ)-c^{-1}W_m(Z).
$$

The exact polynomial identity is

$$
Z^2H_{m,c}'(Z)
 =c^{-1}(1-(m+1)cZ)H_{m,c}(Z)
  +c^{-1}(c^{-1}-1)W_m(Z).
$$

Evaluating it at $r$, together with
$H_{m,c}(r)=W_m(cr)-c^{-1}W_m(r)$, proves the localized ideal equality

$$
\boxed{
(W_m(r),W_m(cr))
 =(H_{m,c}(r),H_{m,c}'(r)).}
$$

Two specializations give the first two common-zero branches:

$$
(r,c)=(u,\zeta_5^{-1})
\quad\hbox{and}\quad
(r,c)=(1,u).
$$

The first is the $P_d(\eta),P_d(\bar\eta)$ branch; the second is the
$P_d(1),P_d(\eta)$ branch.  Their complementary unit factors are
respectively $\zeta_5-1$ and
$u^{-1}-1=-\bar\eta$.  The third branch is

$$
(P_d(\eta),C_d(\eta))
 =(\mathcal F_d(0,u),\partial_\lambda\mathcal F_d(0,u))
$$

up to a common unit.  Hence it is the prescribed double root
$\lambda=0$ of $\mathcal F_d$.  After the exact
$n\mapsto d=n\bmod p$ block reduction, these three prescribed
double-root alternatives exhaust the general-prime ideal obstruction.

All rows share a first-jet invariant.  For a polynomial $f$ and
prescribed point $s$,

$$
f(X)\equiv f(s)+f'(s)(X-s)\pmod{(X-s)^2}.
$$

Thus $\mathcal I_s(f)=(f(s),f'(s))$ is the coefficient ideal of the
first remainder.  Since

$$
\operatorname {Res}_X((X-s)^2,f)=f(s)^2,
$$

the ideal

$$
\mathcal K_s(f)
 =(f'(s),\operatorname {Res}_X((X-s)^2,f))
$$

obeys

$$
\mathcal I_s(f)^2\subseteq\mathcal K_s(f)\subseteq\mathcal I_s(f),
\qquad
\sqrt{\mathcal K_s(f)}=\sqrt{\mathcal I_s(f)}.
$$

This is the exact shared subresultant compression.  A full discriminant is
strictly coarser because it also detects multiple roots away from $s$.
The certificate supplies false positives in every row.  At
$p=31,d=18$, both $Z$-polynomials have the unrelated double root
$8$, while their prescribed first jets are nonzero:

$$
(H(17),H'(17))=(26,19),\qquad
(G(1),G'(1))=(1,1).
$$

At $p=11,d=4,u=5$,

$$
\mathcal F_4(\lambda,5)
 =\lambda^4-3\lambda^2-\lambda+5
$$

has the unrelated double root $4$, while its prescribed jet at zero is
$(5,10)\ne(0,0)$.

I audited the general chain-rule identity, recovery formula, unit
specializations, exhaustive trichotomy, first-jet ideal inclusions, and
all three false positives.  The final artifact supersedes two inconsistent
intermediate freezes; its default all-degree scan through $p\le100$
reran byte-identically.  Accepted SHA-256 hashes:

    dd8d121d34600e8320ed23651b924d711da9558404c43d744f5cb20eb1dfdd87
    cd18a2fd387ba0d95e7ef8fcb32b6e454c4a35454f430e49b651fdf0637d927b
    1c4ca1ddcfffe5f17896b62e7de3182bb8b8b447083f155827ea489fab853bc0

The uniform first-jet language is exact but does not bound the prime
support and does not classify $e+\pi$.

## 2026-08-27 — endpoint periods, scalar recurrence, and Casoratian

The normalized three-state Fourier recurrence has an exact scalar closure.
For

$$
c=\frac{p-2n-1}{2},\qquad
R_v(z)=P_n(z)(1+z)^{2v+1},\qquad u_v=c-v,
$$

the accepted rational-coordinate digit is

$$
U_v=\operatorname {Im}\int_1^i z^{u_v-1}R_v(z)\,dz.
$$

Reciprocity of $R_v$ gives a second endpoint-period representation for
the central digit:

$$
\boxed{D_v=\int_{-1}^{0}z^{u_v-1}R_v(z)\,dz.}
$$

Thus $D_v$, the real part of the first integral, and its imaginary part
are scalar solutions of one operator.  With

$$
E_v=(2n+2v+5)(2n+2v+7)
$$

and

$$
Q_v=n^2+12nv+21n+16v^2+58v+53,
$$

the exact recurrence is

$$
\boxed{
E_vX_{v+3}=64(v+1)(2v+3)X_v-8Q_vX_{v+1}
+2(2n+2v+5)(4n+10v+23)X_{v+2}.}
$$

Both the forward pivot $E_v$ and backward pivot
$64(v+1)(2v+3)$ are units for $0\le v\le c-4$.  Consequently, three
consecutive zero values propagate across the entire admissible interval.

The key point is to exclude the identically-zero matching target.  The
three columns $D_v,\operatorname {Re}I_v,\operatorname {Im}I_v$ have
initial Casoratian

$$
\begin{aligned}
W_{n,c}={}&(-1)^{n/2+1+c(c+1)/2}
\frac{2^{24}}{3^4 5^2 7^2}\\
&\times\prod_{j=1}^{n/2-1}
\frac{2^{14}(j+1)^3(2j+1)^2}
{j(4j+5)(4j+7)^2(4j+9)}\pmod p.
\end{aligned}
$$

The proof starts with an exact $n=2$ calculation.  Under
$(n,c)\mapsto(n+2,c-2)$, the weight is multiplied by

$$
H(z)=-2iz^{-2}(z-1)^2(z-i)^2.
$$

Three explicit Hermite reductions modulo an exact endpoint-vanishing
derivative give a $3\times3$ transition $T_n$ with

$$
\det T_n=
\frac{4096(n+1)^2(n+2)^3}
{n(2n+5)(2n+7)^2(2n+9)}.
$$

Iteration gives the displayed product.  The characteristic-$p$ boundary
terms were checked explicitly: the old value of $c$ is at least $5$, so
the certified primitives are polynomials vanishing at all four endpoints
and have degree at most $p-1$.  Every integer factor in the final product
is strictly smaller than $p$ when the target has $c\ge3$, so the
Casoratian is a unit even when $\mathbb F_p[i]$ is split.

On $v_p(q_n)=1$, put $\bar q_n=q_n/p\pmod p$.  The actual generic
matching residual

$$
F_v=4\bar q_n\operatorname {Im}I_v-p_nD_v
$$

is not identically zero, because $\bar q_n$ and $p_n$ are nonzero and the
two period columns are independent.  Therefore

$$
\boxed{F_v\text{ cannot vanish at three consecutive admissible }v.}
$$

This is deliberately not promoted to a separated-zero bound.  The target
has exact double returns at $(n,p)=(18,3167)$ and $(82,953)$, while the
abstract scalar recurrence at $(n,p)=(2,17)$ has the nonzero solution

$$
(1,9,0,0,2,0),
$$

with zeros at $v=2,3,5$.  Hence recurrence order alone cannot prove an
at-most-two result.

I read the full proof and certificate, checked all range and unit
conditions, reran the certificate byte-identically, and independently
reconstructed the endpoint polynomials, periods, scalar recurrence, and
product formula in $278$ additional prime cases with
$2\le n\le40$ and $3\le c\le34$.  Accepted SHA-256 hashes:

    b5eec04d60e8ca55e5219fc6083e9ad2cb84e9514009f13d32feffb935e158a6
    bf6d2214da1ce4fa6168648ea774fd033f593535da39e830eb33f895890d87f2
    603ccb3717bd073a5172513c5dbf43516aec248b34640e6f3713447f707a08a0

The adjacent-zero theorem is exact, but it does not yet bound the
complementary small-prime or prime-power part of the final matching
content and therefore does not close the remaining Fourier strip or
classify $e+\pi$.

## 2026-08-27 — three adjacent forms and the exact remaining content

The no-three-consecutive theorem has a sharp product consequence.  For
the three Fourier forms with $K_i=K+i$, write

$$
\frac{4S_i}{C_{0,i}}=\frac{A_i}{B_i},\qquad
d_i=\gcd(q_n,B_i),\qquad
g_i=\gcd(M_i,d_i),\qquad h_i=d_i g_i.
$$

For any $p^a\parallel q_n$, put

$$
x_i=v_p(d_i),\qquad y_i=v_p(g_i),\qquad m=\min_i y_i.
$$

The elementary divisibilities $g_i\mid d_i\mid q_n$ give

$$
\sum_i x_i\le3a,qquad
\sum_i y_i\le2a+m.
$$

Multiplying the resulting primewise inequality yields the exact
unconditional estimate

$$
\boxed{
\prod_{i=0}^2d_i g_i
\le q_n^5\gcd(g_0,g_1,g_2).}
$$

There is a stronger local result in the common one-block interval

$$
\mathcal I_{n,K}=\{p:K+2<p\le2(K-n)\}.
$$

The three forms correspond to three consecutive endpoint-period indices.
If $a=1$ and $p\mid g_i$, the exact exponent-match condition has two
possibilities.  On $v_p(C_{0,i})=1$, the normalized matching congruence
gives $F_i=0$.  On $v_p(C_{0,i})\ge2$, exponent matching forces both
$D_i=0$ and $U_i=0$, again giving $F_i=0$.  The nonzero target $F$ cannot
vanish at all three indices.  If $a\ge2$, survival forces
$v_p(C_{0,i})\ge2$ and hence $D_i=0$; the nonzero central endpoint period
also cannot vanish three times consecutively.  Therefore, with no
genericity assumption,

$$
\boxed{
p^a\parallel q_n,\ p\in\mathcal I_{n,K}
\Longrightarrow
\sum_{i=0}^2v_p(d_i g_i)\le5a.}
$$

Let

$$
G_3=\gcd(g_0,g_1,g_2),\qquad
q_{\rm out}=\prod_{\substack{p^a\parallel q_n\\
p\notin\mathcal I_{n,K}}}p^a.
$$

No common-band prime divides $G_3$, so

$$
G_3\mid q_{\rm out},\qquad
\prod_{i=0}^2d_i g_i\le q_n^5G_3\le q_n^5q_{\rm out}.
$$

The positivity estimate for each form then selects at least one member of
the triple with

$$
\boxed{
\Lambda_i^{\rm prim}
\ge\frac{\min_j\mathcal L_j}
{q_n^{2/3}G_3^{1/3}}.}
$$

This would change the high-region threshold to

$$
c>\frac{2+\theta}{3\log2}
$$

if one could prove
$\log G_3\le(\theta+o(1))\log q_n$.  In particular, a negligible triple
gcd would give $2/(3\log2)$.  No such bound is presently available, and
the loss outside the band can be exact.  Direct reconstruction at $n=2$
gives

$$
\begin{array}{c|r|r|r|r}
k&A&B&M&d=g\\ \hline
10&-149056&135135&-515851&7\\
11&-70016&75075&-273791&7\\
12&-1313792&1684683&-5886503&7.
\end{array}
$$

Thus, for $K=9,10,11$ and $q_2=7$,

$$
\prod_i(d_i g_i)=7^6=q_2^5G_3,
$$

with $G_3=q_{\rm out}=7$.  This finite example decisively rejects the
unconditional $q_n^5$ shortcut and shows why the old high-region constant
$1/\log2$ is not yet improved.

I audited the local exceptional-branch implications, all unit/range
conditions, the primewise global inequality, and the positivity selection.
The finite certificate reran byte-identically, and I independently
reconstructed its three exact rows through the earlier matching engine.
The final hashes below supersede and reject the earlier mathematically
correct but less sharp freeze
`c118ae... / b5e27a... / 10a89e...`:

    d176feffb4fd8b4004dce3574098d0ab2437cde2c93753f6ed319252f960cbbb
    6992ca346de330d07ee6dadf5cb9fc3b54f6f4fbe9ae50e2332332875673602f
    c5ef9e420be5f61edf3617b3264e96cb49cf8d1368c21ef9d14556c9ad05c2ce

The theorem isolates the remaining obstruction as the common final
content outside a moving prime band; it does not bound that obstruction or
classify $e+\pi$.

## 2026-08-27 — an exact mixed-$E/G$ division obstruction

For algebraic $\alpha$, define

$$
H_\alpha(z)=\alpha-e^z-4\arctan z,
\qquad
Q_\alpha(z)=\frac{H_\alpha(z)}{z-1}.
$$

The equality sought in this project is exactly

$$
Q_\alpha\text{ holomorphic at }1
\quad\Longleftrightarrow\quad
\alpha=e+\pi.
$$

There is an unconditional function-class theorem:

$$
\boxed{Q_\alpha\notin\mathcal E+\mathcal G
\quad\text{for every }\alpha\in\overline{\mathbb Q}.}
$$

If $Q_\alpha=E+G$, then

$$
R=(\alpha-e^z)-(z-1)E=(z-1)G+4\arctan z.
$$

The left side is an $E$-function and the right side is a $G$-function.
The function-level intersection is
$\mathcal E\cap\mathcal G=\overline{\mathbb Q}[z]$, so $R$ would be a
polynomial with algebraic coefficients.  But
$R(1)=\alpha-e$ is transcendental.  Thus, under the target algebraicity
hypothesis, $H_\alpha$ would give an explicit mixed order-$(-1,0)$ zero at
an algebraic point whose quotient by $z-1$ leaves the mixed class.  A
general André--Beukers zero-removal extension to $\mathcal E+\mathcal G$
is therefore false, not merely unproved.

The same family proves that differential-module invariants cannot detect
the desired cancellation.  Put

$$
A(z)=-\frac{(z-1)(z^2-3)}{(z+1)(z^2+1)},\qquad
B(z)=-\frac{2(z^2+2z-1)}{(z+1)(z^2+1)}.
$$

Then

$$
L=D^3+A(z)D^2+B(z)D
$$

annihilates $1,e^z,\arctan z$.  The exact cyclic determinant for
$H_\alpha,H_\alpha',H_\alpha''$ is

$$
-\frac{16(z+1)^2}{(z^2+1)^2},
$$

independent of $\alpha$ and nonzero.  Hence $L$ is the minimal
order-three operator for every $H_\alpha$, while
$L\circ M_{z-1}$ is the minimal gauge operator for every $Q_\alpha$.
The pole-versus-holomorphic alternative at $1$ is a numerical connection
constant invisible to the common operator, its order, slopes, and
differential Galois module.

There is also an exact finite-limit version.  The function

$$
F_\alpha(z)=\alpha(1-e^{-z})-2\operatorname {Si}(z)
$$

is an $E$-function and satisfies

$$
\lim_{x\to+\infty}F_\alpha(x)=\alpha-\pi.
$$

Thus $\alpha=e+\pi$ exactly when this finite limit is the $E$-value $e$.
Fischler--Rivoal prove that finite directional limits of $E$-functions are
precisely $G$-values, and explicitly state that the value-ring conjecture

$$
\mathbf E\cap\mathbf G=\overline{\mathbb Q}
$$

is currently out of reach.  This route therefore lands exactly on that
unproved intersection, rather than yielding a separation theorem.

The period interpretation was audited especially carefully because an
intermediate draft contained a categorical gap.  Let
$M=E(1)\oplus\mathbb Q(-1)$, with periods $e$ and $2\pi i$.  Its motivic
group is $\mathbb G_m^2$, but failure of numerical normality must be
measured against the period-structure group $G_P$, not just the motivic
group.  Under $\pi=\alpha-e$ with algebraic $\alpha$, a character relation
would be

$$
e^a(2\pi i)^b\in\overline{\mathbb Q}^{\times}.
$$

After absorbing $(2i)^b$, setting $x=e$, and clearing negative exponents,
this gives

$$
x^{a_+}(\alpha-x)^{b_+}
-c'x^{a_-}(\alpha-x)^{b_-}=0.
$$

For $(a,b)\ne(0,0)$ this polynomial is nonzero: otherwise
$x^a(\alpha-x)^b$ would be constant, whereas its logarithmic derivative is

$$
\frac{a\alpha-(a+b)x}{x(\alpha-x)},
$$

which vanishes identically only for $a=b=0$ because $\alpha>0$.
Consequently any nontrivial character relation would make $e$ algebraic.
Thus $G_P\simeq\mathbb G_m^2$ under the hypothesis, while

$$
\operatorname {trdeg}_{\overline{\mathbb Q}}
\overline{\mathbb Q}(e,2\pi i)=1<2=\dim G_P.
$$

The hypothesis would therefore make this direct sum an explicit nonnormal
sum of two individually normal rank-one period structures.  Proving its
normality would exclude algebraicity of $e+\pi$; present exponential-period
conjectures predict this, but present theorems do not prove it.  The
comparison/o-minimality theorem of Commelin--Habegger--Huber and the 2026
$E$-period construction of Snodgrass prove representation and membership,
not injectivity or numerical separation.

I audited the core function-class proof, independently recomputed the
operator identities and cyclic determinant, reconstructed $101$ exact
Taylor coefficients, and checked the primary sources.  During that audit I
rejected three changing source hashes and required the missing computation
of $G_P$ before accepting the final note.  The authoritative hashes are:

    9e1d933e6c3ec5778ce8d446dbd3cc2fd039e9f664ca8fc024e102e0122a5b30
    74addf87b0b81cc5ca3acf2af4942057982008db6c8a3b605149cff4f0bd3fb3
    d6f2070c9ae9833e6bb3431978734ba27b86617747c831e7cfd07c74d840476e

The final source hash supersedes and rejects the stale
`a9f75b...`, `162742...`, and `d3c150...` drafts.  The certificate reran
byte-identically and all control-character and Pandoc checks passed.  This
branch gives a rigorous no-go theorem and a precise conjectural frontier,
but no unconditional classification of $e+\pi$.

## 2026-08-27 — four endpoint-target returns and recurrence-order barriers

The scalar endpoint recurrence does not bound the total number of target
returns by its order.  On the simple Bessel-root branch, the exact case

$$
(n,p)=(3996,291869),\qquad c=141938,
$$

has $v_p(q_n)=1$ and

$$
\{v:F_v=0\}=\{34071,69843,112900,121346\}.
$$

All four zeros are isolated and generic: both $D_v$ and $U_v$ are nonzero.
The complete $141938$-term target transcript has SHA-256

    841981da77e423ae46f8290597fe55fe951630e6b2373eacb93ff26bb359aa79

and contains no other zeros.  Two retained cases have three returns:
$(n,p)=(756,18313)$ at $v=2136,2883,7328$, and
$(946,14629)$ at $v=1778,2010,3483$.

The initial endpoint data were reconstructed by the accepted
$n\mapsto n+2$ contiguity matrices and independently from the defining
polynomial.  If

$$
H(z)=(1+i)-2z+(1-i)z^2,\qquad H(z)^n=\sum_j\rho_jz^j,
$$

then $H(H^n)'=nH'H^n$ gives the linear coefficient recurrence

$$
(1+i)(j+1)\rho_{j+1}
=-2(n-j)\rho_j+(1-i)(2n-j+1)\rho_{j-1}.
$$

I also performed a third independent reconstruction by multiplying by $H$
exactly $3996$ times with modular vector arithmetic.  It recovered the same
initial triples, four zeros, neighboring target values, and full transcript
hash.

The global integral recurrence

$$
\begin{aligned}
&(k+1)(k+2)X_{k+3}-2(k+1)(5k-3n+4)X_{k+2}\\
&\quad+2(16k^2-20kn+10k+5n^2-7n+2)X_{k+1}\\
&\quad-16(k-n)(2k-2n-1)X_k=0
\end{aligned}
$$

was proved by an exact derivative certificate.  Under the one-block
specialization it is precisely the endpoint scalar operator modulo $p$.
Its backward coefficient is $-8p(p+1)$ at the lower preceding index, and
its forward coefficient is $p(p-1)$ at the upper index, so it resets at both
band edges rather than coupling adjacent bands.  The scalar generating
function satisfies an order-two differential equation only with a quadratic
forcing term; the triangular map from $(X_0,X_1,X_2)$ to that term is
injective.  The known Ore factor removes $p_nD_v$, but its adjacent minor
vanishes at $v=18,22,42$ for $(n,p)=(2,109)$.

The discovery scan evaluated 1758 simple-root target sequences and stopped
at the first four-return case in its stated ordering.  This proves that
universal total-return bounds of two and three are false.  It does not prove
unboundedly many returns, a density theorem, or the weighted-product estimate
needed for a better matching threshold.

The authoritative artifact hashes are:

    027760155b21947fa8bfeed5faa86028f5af626258da57026bd512ed2159d2fb
    350ef72fa216636c97615867031338db89b4ee3e1d105825d48d09ecfc8d1e3a
    88e99151fb56352ef349accf4f00d6572d7c9c54fc15ae35d91b62211dc5d6cd

The certificate compiled and reran byte-identically.  The source derivation,
global specialization, boundary pivots, and all four target records were
audited independently.

## 2026-08-27 — exact Hermite reduction of the quartic power kernel

For

$$
J_{n,k}^{(4)}=\int_0^1\frac{x^n(1-x)^n}{(1+x^4)^k}\,dx,
$$

iteration of

$$
\frac{x^m}{(1+x^4)^j}\,dx
=\frac{4j-m-5}{4(j-1)}
 \frac{x^m}{(1+x^4)^{j-1}}\,dx
+\frac1{4(j-1)}d\!\left(\frac{x^{m+1}}{(1+x^4)^{j-1}}\right)
$$

gives a complete Hermite reduction.  If the reduced numerator is
$a+bx+cx^2+dx^3$, then

$$
J_{n,k}^{(4)}=R_{n,k}
+\frac{a-c}{2\sqrt2}\log(1+\sqrt2)+\frac d4\log2
+\left(\frac{a+c}{4\sqrt2}+\frac b8\right)\pi.
$$

Baker's theorem and the elementary multiplicative independence of $2$ and
$1+\sqrt2$ make the actual log-free criterion exactly $d=0$, $a=c$.
The $d$-coordinate vanishes automatically for $k>n/2$.  Uniform proofs give
the simple-pole family $k=1$, $n\equiv6\pmod8$, the inversion-balanced ray

$$
(n,k)=(4j+2,3j+2),
$$

and the isolated pair $(3,2)$.  The exact scan $n,k\le160$ finds only these
61 cases, but the global completeness statement remains conjectural.

For $K=k-1$, the exact monomial denominator is

$$
\operatorname {den}A_{m,k}=
\begin{cases}
2^{2K+v_2(K!)}=2^{3K-s_2(K)},&m\text{ even},\\
2^{K+v_2(K!)},&m\equiv1\pmod4,\\
1,&m\equiv3\pmod4.
\end{cases}
$$

The rational endpoint terms add only exponential lcm cost, not a hidden
factorial.  On the balanced ray, Laplace's method gives
$J_{n,(3n+2)/4}\asymp\rho^n/\sqrt n$ with
$\rho=0.2403944897\ldots$.  A local ideal-content argument then proves that
the form obtained by matching with the exponential beta approximant diverges
after the entire algebraic content is removed.  Thus the only proved
infinite quartic ray is rigorously closed.

For every $k>n/2$, the adjacent determinant

$$
\mathcal K_{n,k}
=(a_{n,k+1}-c_{n,k+1})J_{n,k}^{(4)}
 -(a_{n,k}-c_{n,k})J_{n,k+1}^{(4)}
$$

cancels the remaining logarithm exactly.  Its surviving $\pi$-coordinate is
nonzero in all 9560 certified pairs and retains essentially both dyadic
denominators.  Its integral changes sign, however, so the positive lower
bound is lost.  No all-parameter lower bound or no-go theorem is presently
known for this adjacent-power branch.

The final artifacts, after repairing a TeX exponent typo and adding the
all-prime lcm justification, have hashes:

    df6c72965ceb6a8a177cb51e6cfa09431cbc372e4746f94177f57137f71fa56b
    bb77e21b9654020c7bc352e46066ec4344235bf23f71e124058206a39b7eb686
    aceac26eecdc2f6b441bbb7fd6c0914e2551ff6fe7eb0e5dd858509641061030

The certificate reran byte-identically, and I independently checked the
Hermite identity, logarithmic independence criterion, dyadic denominator
proof, balanced-ray content argument, and the distinction between proved
families and the finite completeness diagnostic.

## 2026-08-27 — zero-gap sparsity and the exact Bessel lift obstruction

Let

$$
q_0=q_1=1,\qquad q_n=(4n-2)q_{n-1}+q_{n-2},
$$

and, for an odd prime $p$, put

$$
\mathcal R_p=\{0\le r<p:p\mid q_r\},\qquad R_p=|\mathcal R_p|.
$$

The anti-period $q_{n+p}\equiv-q_n\pmod p$ permits a cyclic gap argument.
Starting at a root and normalizing $q_{r+1}$, define

$$
P_0(X)=0,\quad P_1(X)=1,\quad
P_{j+2}(X)=(4X+4j+6)P_{j+1}(X)+P_j(X).
$$

A gap of length $d$ starting at $r$ forces $P_d(r)=0$.  Since

$$
\deg P_d=d-1,\qquad \operatorname {lc}P_d=4^{d-1}\ne0\pmod p,
$$

the number $N_d$ of such gaps satisfies $N_d\le d-1$.  Their total length
is $p$, and hence, for every $1\le D\le p$,

$$
\boxed{R_p\le\frac{D(D-1)}2+\frac p{D+1}\le2p^{2/3}.}
$$

This all-prime theorem gives the squarefree smooth-radical estimate

$$
\sum_{n=N}^{2N-1}\log\operatorname {rad}_{\le X}(q_n)
\le3NX^{2/3}\log X+2X^{5/3}\log X.
$$

For $X=C N\log N$, its dyadic average is
$O_C(N^{2/3}(\log N)^{8/3})=o(N\log N)$.  This is an
average/existence statement, not a uniform assertion about every $n$.

There is also an exact first-lift theorem.  For every odd prime $p$ and
every $n\ge0$,

$$
\boxed{q_{n+2p}+2q_{n+p}+q_n\equiv2p q_n\pmod {p^2}.}
$$

The proof sets $u_n=(q_{n+p}+q_n)/p$.  The inhomogeneous terms in the
recurrences for $u_n$ and $u_{n+p}$ cancel modulo $p$, so
$u_{n+p}+u_n$ satisfies the original homogeneous recurrence.  Its two
initial values were not assumed: they were derived term by term from the
exact Bessel sum, including the four residues

$$
\begin{aligned}
q_p&\equiv-1+p(S-2),&
q_{2p}&\equiv1+p(-2S+6),\\
q_{p+1}&\equiv-1+p(T-5),&
q_{2p+1}&\equiv1+p(12-2T)
\end{aligned}
\pmod {p^2}.
$$

If $p\mid q_r$ and

$$
\delta_p(r)=\frac{-q_{r+p}-q_r}{p}\pmod p,
$$

then

$$
\boxed{(-1)^tq_{r+tp}\equiv q_r+tp\,\delta_p(r)\pmod {p^2}.}
$$

Thus a root has exactly one first lift when $\delta_p(r)\ne0$, no lift
when $\delta_p(r)=0$ but $p^2\nmid q_r$, and all $p$ lifts when both
quantities vanish.  Reflection modulo $p^2$ sends the lift parameter of a
central root $r=(p-1)/2$ to $p-1-t$, forcing
$\delta_p(r)=0$.  Hence a central root necessarily dies or branches fully.
The remaining condition

$$
p^2\mid q_{(p-1)/2}
$$

is a genuine Wieferich-type obstruction.  The first central root is
$(p,r)=(79,39)$; exactly

$$
q_{39}\equiv948=12\cdot79\pmod {79^2},\qquad
q_{39+79t}\equiv(-1)^t948\pmod {79^2},
$$

so it dies.  This example and the possible fully branching alternative
rule out a blanket simple-Hensel argument.

The precise term not controlled by the squarefree theorem is

$$
\mathcal E_X(n)
=\sum_{p\le X}(v_p(q_n)-1)_+\log p.
$$

The exact values $v_7(q_{361})=4$ and $v_{11}(q_{1359})=5$ show that it
cannot be discarded.  The three adjacent Fourier contents at $n=18$ and
$k=1004,1005,1006$ have $7$-adic valuations $(3,2,1)$ despite
$v_7(q_{18})=3$, so the triple gcd suppresses this example to one power.
No uniform theorem currently bounds that suppression through the reset
pivots.

I audited the gap polynomial proof, the averaging constants, every step of
the second-difference and affine-lift derivation, the central reflection
argument, and the scope of the cited primary literature.  I also found and
required correction of an erroneous Filaseta--Trifonov DOI before accepting
the final source.  The certificate reran byte-identically.  The
authoritative hashes are:

    dac7cd496b4342a8afc6d379274986d2030bc327c9017b3f6fa877108e62e1fc
    e5ca277a25f6f219808f2ca0da6a599ee549f329fc138db25f10a3998b6fd0bb
    41db4e47463dd41f4365c91442c1cccee8d3932258a4895d468210e2efcf3692

This is a genuine average arithmetic advance, but it leaves the
prime-power excess—and therefore the common outside-band content—open.  It
does not classify $e+\pi$.

## 2026-08-27 — all first lifts and the moving high-level valuation tail

I completed an independent audit of the prime-square branching law above
and pushed its averaging consequence through every prime-power level whose
period is no longer than the averaging interval.

For a root $r\bmod p$, put

$$
\delta_p(r)=\frac{-q_{r+p}-q_r}{p}\pmod p,
$$

and let $S_p$ count roots with $\delta_p(r)=0$, while $A_p$ counts those
singular roots for which $p^2\mid q_r$.  The affine lift formula gives the
exact root-count identity

$$
\boxed{R_{p^2}=R_p-S_p+pA_p.}
$$

Reflection sends $r$ to $p-1-r$ and gives

$$
\delta_p(p-1-r)=-\delta_p(r).
$$

It pairs noncentral singular roots and forces the central class
$m=(p-1)/2$ to have zero slope whenever it is a root.  At that class, the
factor pairs

$$
2(m+t)=p+(2t-1),\qquad
2(m+1-t)=p-(2t-1)
$$

give, term by term,

$$
\boxed{
q_m\equiv(-1)^m
\sum_{j=0}^m\frac{(1/2)_j^2}{j!}\pmod {p^2}.}
$$

Consequently the all-$p$ branch is exactly the vanishing modulo $p^2$ of
this truncated $\,{}_2F_0$ sum.  No all-prime theorem presently excludes
that Wieferich-type congruence.

Reduction modulo $p$ and the zero-gap theorem yield, for every $a\ge1$,

$$
\boxed{R_{p^a}\le p^{a-1}R_p\le2p^{a-1/3}.}
$$

This estimate is enough for all low-period valuation levels.  On
$[N,2N)$, uniformly in $X$,

$$
\frac1N\sum_{n=N}^{2N-1}
\sum_{p\le X}\sum_{\substack{a\ge2\\p^a\le N}}
{\bf1}_{p^a\mid q_n}\log p
\le6N^{1/3}\log N=o(N\log N).
$$

The proof counts at most
$(N/p^a+1)R_{p^a}\le4Np^{-1/3}$ occurrences at each admissible level and
sums over at most $\log N/\log p$ levels.  The complementary sum
$p^a>N$ is not controlled: each period class can meet the interval only
once, so the residue-density estimate loses precisely the averaging factor
that made the displayed bound useful.  This is now the exact moving tail
that must be controlled for the smooth prime-power content.

The C++ certificate exhaustively scans every root for every odd prime
$p\le200000$.  Its finite results are:

- $17{,}983$ odd primes and $18{,}013$ roots modulo $p$;
- no all-$p$ branch;
- the sole singular root is the central root $(79,39)$, and it dies;
- the sole base representative divisible by $p^2$ is $(13,8)$, with
  nonzero slope $\delta_{13}(8)=1$.

I inspected the implementation and result, independently reconstructed
every first-lift fiber and central hypergeometric congruence for all odd
primes below $300$, and reran the full $p\le200000$ program.  The full
rerun was byte-identical.  The authoritative hashes are:

    f02b4b936c2ca810299f037e158e7406214e89ef77e8ca98dcd67b2a9bd00911
    849e86b3bb26628261b8bb0bb9b457e1c9cec0a6823b94ebf3cfe94f9af02f92
    09a3622c5a4362127bddede30793b378765040da397d2e0dd50ca4cc50fdddf4

This sharpens the valuation obstruction but does not remove it and does
not classify $e+\pi$.

## 2026-08-27 — exact high-tail gaps and the ordinary-singleton barrier

The moving high-level tail has a second exact decomposition which shows
why excluding full branching would still not finish the valuation problem.
Define

$$
P_0(X)=0,\qquad P_1(X)=1,\qquad
P_{j+2}(X)=(4X+4j+6)P_{j+1}(X)+P_j(X).
$$

Induction in the Bessel recurrence gives

$$
\boxed{
q_{n+d}=P_d(n)q_{n+1}+P_{d-1}(n+1)q_n.}
$$

Because consecutive $q_n$ are coprime,

$$
\boxed{\gcd(q_n,q_{n+d})=\gcd(q_n,P_d(n)).}
$$

Moreover, $P_d(n)\le\{4(n+d)\}^{d-1}$.  Thus, if the same
$M>1$ divides $k$ terms in an interval $[N,N+L)$, multiplication over
consecutive gaps proves

$$
k\le1+\frac{(L-1)\log(4(N+L))}
{\log M+\log(4(N+L))}.
$$

This remains valid on fully branching fibers, but is too weak when $M>L$.

For the exact tail decomposition, let

$$
b_p(N)=\min\{a\ge2:p^a>N\},\qquad
h_{p,n}=(v_p(q_n)-b_p(N)+1)_+.
$$

Choose, for each prime, an index $n_p\in[N,2N)$ at which $h_{p,n}$ is
maximal, and retain

$$
S(N,X)=\sum_{p\le X}h_{p,n_p}\log p.
$$

If $G_{N,X}(n,m)$ denotes the corresponding truncated high part of
$\gcd(q_n,q_m)$, then

$$
\boxed{
S(N,X)\le H(N,X)\le S(N,X)+
\sum_{N\le n<m<2N}\log G_{N,X}(n,m).}
$$

Every term after $S$ divides a gap-polynomial gcd.  No gap polynomial
appears in $S$, since it deliberately keeps only one deepest occurrence
for each prime.  The direct aggregate gap bound is still only

$$
\sum_{N\le n<m<2N}\log G_{N,X}(n,m)
\le\frac{N(N-1)(N-2)}6\log(8N),
$$

whereas the required total is $o(N^2\log N)$.

The singleton obstruction is certified on an ordinary Hensel chain:

$$
q_{1359}\equiv3\cdot11^5\pmod {11^6},\qquad
v_{11}(q_{1359})=5.
$$

The unique child digits through the five tested lifts are $2,0,1,0,8$,
and the first slope is $\delta_{11}(6)=10\ne0\pmod {11}$.  With
$N=1359$, exact recurrence on the whole interval gives

$$
\{n\in[1359,2717]:11^4\mid q_n\}=\{1359\}.
$$

Consequently the $11^4$ and $11^5$ contributions, totaling $2\log11$,
lie wholly in the singleton-max term.  This finite example does not prove
that $S(N,X)$ is asymptotically large; it proves that ordinary unique
lifts, not just all-$p$ branches, populate the unresolved tail.

I checked the continuant and gcd derivations, the tail-star identity, all
constants in the cluster and cubic bounds, and the distinction between a
finite obstruction and an asymptotic counterexample.  The certificate
reran byte-identically.  The authoritative hashes are:

    aa7ed68bc510a86bdd3881f87d663ad3f6102694714392dad3073160589f7888
    0822247f578b3f383525b7dc9c04a2b84c576c259e35701db08f2bdbd73d809f
    83e0826bea67a1e80477749bd98c22859704528910464d05cd04e70a0665a252

The remaining estimate is an isolated large-squarefull-part problem for
individual Bessel denominators.  It is not solved here, and this theorem
does not classify $e+\pi$.

## 2026-08-27 — the central Bessel lift as a Laguerre parameter derivative

The exceptional central class in the Bessel lift admits a classical exact
normal form.  For an odd prime $p=2m+1$, define

$$
A_m=m!L_m(-1)=\sum_{j=0}^m j!\binom mj^2
$$

and

$$
C_m=m!\left.
\frac{\partial}{\partial\alpha}L_m^{(\alpha)}(-1)
\right|_{\alpha=0}.
$$

For

$$
Q_m(x)=\sum_{k=0}^m(-1)^k
\frac{(2m-k)!}{k!(m-k)!}x^k
$$

one has $q_m=Q_m(1)$ and the exact Bessel--Laguerre identity

$$
\boxed{q_m=(-1)^m m!L_m^{(-p)}(-1).}
$$

The Laguerre connection formula at parameters $-p$ and $0$ then gives

$$
\boxed{q_m\equiv(-1)^m(A_m-pC_m)\pmod {p^2},}
$$

with the two exact integer descriptions

$$
C_m=\sum_{r=1}^m\frac{(m)_r}{r}A_{m-r}
=\sum_{j=0}^m j!\binom mj^2(H_m-H_{m-j}).
$$

It follows that

$$
p\mid q_m\Longleftrightarrow p\mid A_m,
$$

and, conditional on this central root,

$$
\boxed{p^2\mid q_m\Longleftrightarrow A_m/p\equiv C_m\pmod p.}
$$

This makes the surviving Wieferich-type quantity completely explicit, but
does not prove that it is nonzero.

There is a useful warning against a tempting false shortcut.  If
$P_m(x)=Q_m(-x)$, the Padé identity
$P_m-e^xQ_m=O(x^{2m+1})$ yields the exact Wronskian

$$
\boxed{
P_m'Q_m-P_mQ_m'-P_mQ_m=(-1)^{m+1}x^{2m}.}
$$

Thus a central root has $Q_m'(1)\ne0\pmod p$: it is simple as a root in
the polynomial argument $x$.  Hensel lifting in $x$ nevertheless allows
the lifted root to remain exactly $x=1$ when $p^2\mid Q_m(1)$.
The unresolved congruence instead compares the Laguerre parameter values
$0$ and $-p$.  Argument-root simplicity therefore supplies no
all-prime exclusion.

The exact remainder-tree certificate scanned every $148{,}932$ odd prime
$p\le2{,}000{,}001$.  It found only the central root $p=79$, and

$$
A_{39}/79\equiv45,\qquad C_{39}\equiv57,\qquad
q_{39}/79\equiv12\pmod {79},
$$

so this root dies at the square level.  The scan is finite evidence only.
I checked the algebraic identities, the distinction between the two lift
directions, the remainder-tree invariants, and the archived hashes; a full
independent rerun was byte-identical.  The authoritative hashes are:

    f0356cfb8ff5297d8595b0c9c56017a46dfe1d4c18d6c13d6e007147078ce6f0
    49995374532dcb3369e62d643f2a69f39462d1d8c54ae6d68b5bdf718d3ae2c1
    5ddccadb1071fdc76bf95c4ccd0c2172f7dc728f6a8abf39f8f29899498a1f3d

The ordered residue transcript has SHA-256

    072ddd4c8400ed7a2e356aeeac42a8541db75c0e4f8b4aa3474c68df9ce5ec61

This sharpens the central obstruction but does not classify $e+\pi$.

## 2026-08-27 — neighboring quartic saddles and three-power positivity

For even $n$, write

$$
J_{n,k}=\int_0^1\frac{x^n(1-x)^n}{(1+x^4)^k}\,dx
$$

and let $L_{n,k}=a_{n,k}-c_{n,k}$ and
$E_{n,k}=a_{n,k}+c_{n,k}$ be the two even Hermite coordinates.  Exact
reflection and beta integration give

$$
\boxed{
L_{n,k}=(-1)^{n/2}\frac{2\sqrt2}{\pi}
\operatorname {Re}\int_0^\infty
\frac{[y(1+iy)]^n}{(1+y^4)^k}\,dy}
$$

and

$$
\boxed{
E_{n,k}=\frac{\sqrt2}{\pi}\int_0^\infty
\frac{y^n\{(1+y)^n+(1-y)^n\}}{(1+y^4)^k}\,dy>0.}
$$

These formulas identify distinct complex and real saddles without rotating
an infinite contour across a fourth root of $-1$.

Put $r=(4k/n)^{-1/4}$.  A uniform pole-free steepest-descent calculation
shows that the two-neighbor log-canceling determinant retains the complex
saddle with multiplier

$$
\frac1{1+y_i^4}-\frac1{1+x_-^4}
=-(1+i)r^5-\frac32r^6+\frac7{32}(-1+i)r^7+O(r^8).
$$

After the real projection its leading term is proportional to
$\cos(\Theta_{n,k}+\pi/4)$, and

$$
\Theta_{n,k+1}-\Theta_{n,k}=-r^5+O(r^6+n^{-1}).
$$

Thus short integer-power blocks contain full-size projections, but other
powers approach the moving zeros within $O(r^5)$.  This does not prove an
exact determinant zero; it rigorously rules out a lower bound by one fixed
positive fraction of the saddle envelope at every power.

Three powers remove the phase.  With $L_s=L_{n,k+s}$,

$$
\boxed{
L_1^2-L_0L_2
=\frac8{\pi^2}\mathcal I_{n,k}^2\rho^2
\left(r^{10}+O(r^{12}+n^{-1})\right).}
$$

Consequently this Hankel minor is positive whenever

$$
n\to\infty,\qquad r\to0,\qquad nr^{10}\to\infty,
$$

uniformly in the oscillatory phase.  In particular, the theorem holds
throughout every fixed window $c_1n\log n\le k\le c_2n\log n$.
The key exact identity is

$$
\bigl(\operatorname {Re}(Zg)\bigr)^2
-\operatorname {Re}(Z)\operatorname {Re}(Zg^2)
=|Z|^2|g|^2\sin^2(\arg g).
$$

After clearing $(L_0,L_1,L_2)$ to a primitive integer vector
$(a,b,c)$, the positivity of $b^2-ac$ gives a rational point
$t=u/v$ strictly between the two roots of
$a-2bt+ct^2$, with $v=O(r^{-5})$.  The explicit coefficients

$$
(C_0,C_1,C_2)
=\operatorname {sgn}(c)(cv,-2cu,-av+2bu)
$$

satisfy

$$
aC_0+bC_1+cC_2=0,\qquad
P(Q)=C_0Q^2+C_1Q+C_2>0,
$$

and $\max|C_j|=O(Hr^{-5})$.  Hence

$$
\Lambda_{n,k}(P)=
\int_0^1\frac{x^n(1-x)^nP(1+x^4)}
                 {(1+x^4)^{k+2}}\,dx
$$

is exactly log-free and positive.  Whole-real-line integration proves that
its $E(P)$, and therefore its $\pi$-coordinate, is positive.

The symmetric form exposes an exact analytic obstruction.  With

$$
F(x)=\frac{x^n(1-x)^nP(1+x^4)}{(1+x^4)^{k+2}},
$$

the odd coordinate cancels and

$$
\boxed{
\frac{\Lambda^{\rm sym}_{n,k}}{B^{\rm sym}_{n,k}}
=2\pi\frac{\int_{-1}^1F(x)\,dx}
              {\int_{-\infty}^{\infty}F(x)\,dx}.}
$$

The outer tail is bounded by

$$
\eta^{-2}\exp\left(
-(k-n)\log2+\frac n4\log(4k/n)+O(n)\right)=o(1),
$$

so

$$
\frac{\Lambda^{\rm sym}_{n,k}}{B^{\rm sym}_{n,k}}
=2\pi(1+o(1)).
$$

After normalization by its $\pi$-coefficient, this positive branch does
not tend to zero.  This conclusion is deliberately analytic: the
coefficient pair is in $\mathbb Q(\sqrt2)$, and a theorem about a fully
primitive matched algebraic integer would still require its common ideal
content and both embeddings.

An adversarial audit found two genuine presentation gaps in the first
frozen version.  The original infinite-tail argument had discarded the
decisive $2^{-k}$ endpoint factor; the corrected estimate is

$$
\int_1^\infty e^{nH(y)}\,dy
\le\frac{2^{n/2-k}}{2k-2n-1}.
$$

The symmetric-tail argument had also omitted the possible $c=0$ branch,
now handled directly by $P(Q)=1$.  The audit made the $O(r)$ connectors
inside a fixed pole-free rectangle explicit and tracked absolute, rather
than relative, $O(1/n)$ errors in the Hankel minor.  Both corrected
certificates reran byte-identically.  The superseding main hashes are:

    a24d515d85599ab6a44832879576784539c0666928a4e2c73257c783bc23017b
    5628406d31ed8c85f27210f2aaaa6e5b809286f0312d1e5b0b268a05b7af4a0a
    384b6e4f215771b615889b7e89ccf56e718357ada7d097e5dff6a2cae6397dd3

The separate adversarial-audit hashes are:

    53b685ebfe7235f3da6270e751bb77ee3594b07c260b0486716e31d45ca7d2cd
    e2accee40841a259f243b08e0b6324dc8e59d880825d00d9d322a72e251cc452
    d39fb95b501456f629e13b77b2737f4eff6a7fd6bc5049a0a29ba080757ba320

The theorem bypasses the two-power phase zero but reaches a
scale-invariant obstruction; it does not classify $e+\pi$.

## 2026-08-27 — central Charlier reformulation and Frobenius barrier

The central coefficient problem admits an exact polynomial formulation
that unifies the argument, parameter, and Hensel-lift directions.  Define

$$
F_n(a)=\sum_{j=0}^n\binom nj(a)_{\underline j}.
$$

Its exponential generating function, recurrence, and forward difference
are

$$
\sum_{n\ge0}F_n(a)\frac{z^n}{n!}=e^z(1+z)^a,
$$

$$
F_{n+1}(a)=(a+1-n)F_n(a)+nF_{n-1}(a),
\qquad
\Delta_aF_n(a)=nF_{n-1}(a).
$$

For $p=2m+1$, the three quantities governing the central branch are
exactly

$$
\boxed{
F_m(m)=A_m,\qquad
F_m'(m)=C_m,\qquad
F_m(m-p)=(-1)^mq_m.}
$$

Thus the desired all-branch central exclusion is equivalent, conditional
on $p\mid A_m$, to showing that the specific Charlier Hensel digit from
$a=m$ to $a=m-p=-m-1$ is not $-1$.  This is stronger and more
specific than merely proving that the root $a=m\pmod p$ is simple.

The coefficients also have an exact partial-injection interpretation.
The falling factorial $(a)_{\underline j}$ counts injections from a
chosen $j$-element subset, so $F_n(a)$ is the rook polynomial of all
partial injections from an $n$-set to an $a$-set.  Modulo $p^2$,
the parameter shift is consequently an exact nilpotent deformation, not
just a formal analogy.

Several plausible shortcuts fail for precise reasons:

1. Expanding the $p$-step Newton series produces the expected harmonic
   sums, but these are the ordinary Taylor coefficients of the same
   polynomial.  Wilson-quotient terms cancel after imposing
   $p\mid F_m(m)$; no extra first-order obstruction survives.

2. Frobenius gives a first coefficient $-1$ in the truncated generating
   function, but the putative second-order obstruction cancels identically
   through

   $$
   \partial_t^2G(z)^t=G(z)^t\{\log G(z)\}^2.
   $$

   Hence the most direct Frobenius lift simply reproduces Taylor's
   theorem.

3. The exact quotient after lowering the Charlier degree yields a valid
   congruence for the lift residue, but it does not force that residue to
   be nonzero.

4. Global parameter simplicity is false.  A certified counterexample is

   $$
   F_{288}(186)\equiv F'_{288}(186)\equiv0\pmod{577},
   $$

   while the diagonal values are $F_{288}(288)\equiv8$ and
   $F'_{288}(288)\equiv211\pmod{577}$.  Any separability proof must
   therefore use the special diagonal $a=m$, not a global discriminant
   assertion.

The bounded exact scan attached to this note again found only the central
root $p=79$ in its default range.  There

$$
A_m/p\equiv45,\qquad C_m\equiv57,\qquad q_m/p\equiv12\pmod{79},
$$

so the root dies at the first lift.  This is finite evidence only.

I checked the identities and the failure mechanisms and independently
reran the certificate byte-for-byte.  The current artifact hashes are:

    d635d1ed73444694bbece9aeefd473461bcf5d882bdab0c1b00148442b5c966a
    673d4de5d187fbae74132d3390b5cd795d82cb072c8464c25cfece5582d4c833
    4f4da49b13e85b8fcfe2e1179ea2cb4baf07ab325180948dfe7fb8907287a8b0

This reformulation identifies the remaining local arithmetic datum but
does not classify $e+\pi$.

## 2026-08-27 — multi-power quartic kernels and endpoint lattices

For even $n$, introduce the neighboring whole-line saddle integrals

$$
A_{\pm,j}=\int_0^\infty
\frac{y^n(1\pm y)^n}{(1+y^4)^{k+j}}\,dy,
\qquad
I_j=\int_0^\infty
\frac{[y(1+iy)]^n}{(1+y^4)^{k+j}}\,dy.
$$

The previously untreated odd Hermite coordinate is exactly

$$
\boxed{
b_j=-\frac1\pi\left(A_{+,j}-A_{-,j}
+2(-1)^{n/2}\operatorname {Im}I_j\right),}
$$

and hence

$$
b_j+\frac{E_j}{\sqrt2}
=\frac2\pi\left(A_{-,j}
-(-1)^{n/2}\operatorname {Im}I_j\right).
$$

For three neighboring powers, let $C=L\times E$.  Then $C$ cancels
both logarithmic coordinates exactly and

$$
\boxed{
C\mathbin{\cdot}J=C\mathbin{\cdot}R
+\frac{C\mathbin{\cdot}b}{8}\pi.}
$$

At the critical saddle scale $k\asymp n\log n$, with
$r=(4k/n)^{-1/4}$,

$$
C\mathbin{\cdot}b
\sim-\frac{16}{\pi^3}A_+|I|^2r^{15}<0.
$$

The leading coefficient is independent of the oscillatory complex phase.
Thus the rational $\pi$-coordinate is eventually nonzero, and

$$
\left|\pi+\frac{8C\mathbin{\cdot}R}{C\mathbin{\cdot}b}\right|
\ll\frac{J_{n,k}}{|I_{n,k}|}
=\exp\{-nr+O(nr^2)\}.
$$

This is a genuine rational approximation to $\pi$, but it proves
irrationality only if the primitive rational height grows more slowly
than the analytic gain.  That height cannot be inferred from the
uncleared cross product.

Four powers remove the numerator phase as well.  The exact Hankel kernel
has leading saddle polynomial

$$
W(t)\ \propto\ (g_+-t)(t-g_i)(t-\overline {g_i}),
$$

and

$$
c\mathbin{\cdot}J
\sim-\frac{512\sqrt2}{\pi^5}A_+J|I|^4r^{45}<0.
$$

The asymptotic is uniform once $nr^{45}\to\infty$, a condition still
satisfied for $k\asymp n\log n$.  However, the same polynomial
annihilates the leading $b$-saddles.  Four powers therefore exchange
the numerator-phase problem for a next-order primitive-$b$ problem;
nonvanishing of that next term remains under investigation.

The correct arithmetic invariant is an endpoint lattice.  For the
integrally cleared two-row matrix $A=(L;E)$,

$$
\boxed{
\det\ker_{\mathbb Z}A
=\frac{\sqrt{\det(AA^T)}}{\delta_2(A)}.}
$$

For three columns this says that the primitive coefficient vector is the
cross product divided by the gcd $\delta_2(A)$ of its $2\times2$
minors.  If

$$
M=(L;E;R;b/8)
$$

is the fully cleared four-row coordinate matrix and

$$
\Gamma=(R,b/8)\bigl(\ker_{\mathbb Z}(L,E)\bigr)\subseteq\mathbb Z^2,
$$

then, under full rank,

$$
\boxed{
[\mathbb Z^2:\Gamma]=\frac{\delta_4(M)}{\delta_2(A)}.}
$$

For at least five powers the full coordinate kernel has rank at least
one.  Consequently a naïve Siegel-lemma vector in the $L,E$-kernel can
be an exact zero period relation.  Nonzero small forms must instead be
controlled in the two-dimensional quotient lattice $\Gamma$, together
with the height of a lift back through the exact-zero kernel.

Adjacent differences have the exact integral

$$
K_{s,k}
=\sum_{j=0}^s(-1)^j\binom sjJ_{n,k+j}
=\int_0^1
\frac{x^{n+4s}(1-x)^n}{(1+x^4)^{k+s}}\,dx.
$$

For $s=uk$ and $n=o(k)$,

$$
\log K_{s,k}=-k\{(1+u)\log(1+u)-u\log u\}+o(k).
$$

After including the terminal dyadic denominator, the exponent is

$$
3(1+u)\log2-(1+u)\log(1+u)+u\log u.
$$

Its exact minimum is attained at $u=1/7$ and equals $\log7$.
This is only a pre-primitive finite-difference cost: common content may
alter it, so it is not being used as a final height estimate.

All four leading saddle multipliers satisfy the same integer polynomial

$$
\boxed{
F_{n,k}(t)=
t[4k(1-t)-n]^4-(1-t)[4k(1-t)-2n]^4.}
$$

Thus a rational recurrence that annihilates the real leading saddle
generically annihilates the positive and complex leading saddles too.
This is an exact obstruction to separating the branches solely through
their leading algebraic multipliers.

The source, certificate, and byte-identical result have hashes:

    e6d1732905ee102bbe6abb780a83e8454a28fa95aca93b2ae93725fa8dfed397
    0b63e338d265d879e06e82f379ad4022b592383baa21d4ec894def4b7315a239
    70e211c1787a90d38d43cd713c93430f4827f993e0c3923c9ca523ef3e4c99d1

The branch now isolates the unresolved arithmetic quantities
$\delta_2(A)$, $\delta_4(M)/\delta_2(A)$, and the lift height.  It does
not yet classify $e+\pi$.

## 2026-08-27: first nonzero odd correction for the four-power kernel

The phase-removing four-power construction was expanded one full saddle
order beyond the leading cancellation.  This was necessary because its
cubic kernel kills not only the leading real phase in the positive
determinant, but also the leading complex contribution to the odd
$\pi$-coordinate.  The new calculation identifies the first surviving
term and separates the analytic issue from the still-open primitive-content
issue.

For four consecutive powers let $c$ be the cofactor vector satisfying
$c\cdot L=c\cdot E=0$.  The exact odd-coordinate identity is

$$
c\cdot b=\frac2\pi\left(c\cdot A_-
       -(-1)^{n/2}c\cdot\operatorname {Im}I\right).
$$

Write the complex saddle ratios in the form

$$
\frac{I_j}{I_0}
=g_i^j\left[
1+\frac1n\{a_i j(j-1)+\beta_i j\}+O(n^{-2})\right].
$$

Direct saddle differentiation gives

$$
a_i=-\frac{\ell'(u_i)^2}{2\psi_i''(u_i)}
=2r^8+\frac{5i}{2}r^9+O(r^{10}).
$$

The exact symbolic first variation of the four-column determinant is

$$
c(\operatorname {Re}z,u)\cdot\operatorname {Im}z
=4\eta(\operatorname {Im}g)^4|Z|^4|p-g|^2
 \operatorname {Im}\{aZg^2(\bar g-p)\}+O(\eta^2).
$$

This formula proves three cancellations that had previously only been
suggested numerically: every correction linear in the power index cancels,
every first-order correction to the positive row cancels, and the first
survivor is the quadratic complex correction.  Its small-$r$ coefficient
is

$$
a_i g_i^2(\bar g_i-g_+)
=2(1+i)r^{13}
+\left(-\frac{11}{2}+\frac{5i}{2}\right)r^{14}
+O(r^{15}).
$$

Consequently, if $r\to0$, $nr^{45}\to\infty$, and
$|\sin\Phi|\ge\eta>0$, where

$$
\Phi=\arg I+\frac\pi4+2r+O(r^2),
$$

then

$$
\boxed{
c\cdot b=
-\frac{4096(-1)^{n/2}}{\pi^6}
 \frac{A_+|I|^5}{n}r^{43}\sin\Phi
\left[
1+O_\eta\left(
r+\frac1{nr^{43}}+nr^2\frac J{|I|}
+\frac{e^{-2nr+O(nr^2)}}{r^{43}}
\right)\right].}
$$

The direct negative-real saddle is smaller:

$$
\frac2\pi c\cdot A_-
\sim-\frac{1024\sqrt2}{\pi^6}A_+J|I|^4r^{45},
$$

with relative size

$$
nr^2\frac J{|I|}
=e^{-nr+O(nr^2+\log n)}.
$$

The oscillation is not an all-power nonvanishing theorem.  Nevertheless,
in every fixed critical window the adjacent-power phase mesh satisfies

$$
\frac12r_k^5\le\Phi_k-\Phi_{k+1}\le\frac32r_k^5.
$$

Every contained block of
$M_k=\lceil16\pi r_k^{-5}\rceil$ consecutive powers therefore has phase
drop at least $4\pi$ and mesh at most $2r_k^5$.  It contains indices
of both signs with $|\sin\Phi|>1/2$.  Thus the first correction proves
analytic nonvanishing on explicit phase-selected subsequences, while also
showing why a uniform lower bound over all powers is unavailable: integer
powers can lie within $O(r^5)$ of phase zeros, and the true cancellation
window is exponentially narrower.

For the selected subsequences the normalized rational approximation is

$$
\boxed{
\pi+\frac{8c\cdot R}{c\cdot b}
\sim
\frac{(-1)^{n/2}\sqrt2\,\pi\,nr^2}{\sin\Phi}\frac J{|I|}.}
$$

Hence it retains exponential analytic smallness.  A direct determinant
bound gives raw kernel height at most $24H^5$.  This still does not yield
a proof about $\pi$, because neither the gcd of the four cofactor entries
nor the content of the endpoint pair $(8c\cdot R,c\cdot b)$ is bounded
at the necessary exponential scale.  Those are now the exact arithmetic
targets; the phase question itself is no longer the sole obstruction.

The fully audited source, executable certificate, and byte-identical result
are:

    sources/quartic_four_power_odd_residual_first_correction.md
    scripts/quartic_four_power_odd_residual_certificate.py
    results/quartic_four_power_odd_residual_certificate.json

Their SHA-256 hashes are respectively:

    92a0b08015d8f143342c21bdb3da4a0e0cbeb41fb7f8a6e4cf28558bf9355908
    ceb0a26bfb5ba71e0be200f613468c92cf963b3e98012f6a180b14a8f3f3a40e
    9c6d6388813bcbcaca85217ceacdb6d0fe7a540fc0102f1c3fa94c5406f4d456

This is a rigorous advance within the quartic route, not a classification
of $e+\pi$.

## 2026-08-27: index Frobenius and the corrected central energy identity

The central Charlier obstruction was attacked in the polynomial index,
through a resonant differential equation, and through the symmetric
terminating ${}_2F_0$ representation.  Each route gives an exact new
identity, but each also exposes a new residue which is not presently
controlled.

For

$$
F_n(a)=\sum_{j=0}^n\binom nj(a)_{\underline j},
$$

Vandermonde convolution gives the exact all-degree identity

$$
\boxed{
F_{p+n}(a)=\sum_{r=0}^p\binom pr(a)_{\underline r}F_n(a-r).}
$$

Consequently

$$
F_{p+n}(a)\equiv F_p(a)F_n(a)+p\mathcal E_{p,n}(a)\pmod {p^2},
$$

where

$$
\mathcal E_{p,n}(a)=-(a)_{\underline p}F_n'(a)
+\sum_{r=1}^{p-1}\frac{(-1)^{r-1}}r(a)_{\underline r}
 \{F_n(a-r)-F_n(a)\}.
$$

Modulo $p$, a simultaneous zero of $F_n,F_n'$ propagates from index
$n$ to $n+p$.  Modulo $p^2$, however, its two lift digits acquire
the independent residues $\mathcal E_{p,n}(a_0)$ and
$\mathcal E_{p,n}'(a_0)$.  At the concrete double root
$(n,p)=(317,401)$, those correction digits are $258$ and $379$,
both nonzero.  Thus index propagation is not a hidden repeated-root
theorem.

The central value condition also has a resonant ODE formulation.  The
universal sequence

$$
B_0=0,\quad B_1=1,\quad
B_{r+1}=\frac{2r-1}{2r+1}(2B_r-B_{r-1})
$$

has generating equation

$$
2z(1-z)^2B'+(-1+2z+z^2)B=z.
$$

For $p=2m+1$, the central root is exactly the resonance condition
$B_{m-1}-2B_m=0$.  With $K=B/z$, the forbidden derivative residue is
$\beta_m=\int_0^1K$, and the exact conditional identity is

$$
\boxed{
\beta_m=2\int_0^1zK(z)^2\,dz-B_m^2\pmod p.}
$$

The term $-B_m^2$ is indispensable.  In characteristic $p$, the
polynomial used in integration by parts has degree $p$, and its $z^p$
coefficient has zero derivative but nonzero endpoint difference.  At the
known root $p=79$, the exact residues are

$$
(\beta_m,\ \int_0^1zK^2,\ B_m^2)=(16,5,73),
\qquad16=2\cdot5-73\pmod {79}.
$$

This correction was found during adversarial auditing; the false naive
identity without the Frobenius term is not retained anywhere in the
accepted source or certificate.  The corrected quadratic form is already
isotropic under the natural degree and endpoint constraints, so it gives
no positivity-based nonvanishing theorem.

Finally, if $a_j=(1/2)_j^2/j!$, the exact symmetric representation gives

$$
(-1)^mq_m\equiv\sum_{j=0}^{p-1}a_j\pmod {p^2}.
$$

For $0\le k\le m$, the first Dwork block satisfies

$$
\frac{a_{p+k}}{pa_k}\equiv-\frac14
\left[1+p\{4O_k-H_k-W_p-Q_p(16)\}\right]\pmod {p^2}.
$$

Conditional on a central root, summing this formula cancels the constant
Wilson and Fermat terms but leaves the old unknown lift digit plus a new
weighted harmonic sum equal to an uncontrolled next-block residue.  For
$p=79$ the three residues are $67,7,21$, satisfying
$21=-\tfrac14(67+7)$.  Hence the block identity is genuine but does not
close the lift.

The fully audited source, executable certificate, and byte-identical result
are:

    sources/bessel_central_index_frobenius_energy.md
    scripts/bessel_central_index_frobenius_energy_certificate.py
    results/bessel_central_index_frobenius_energy_certificate.json

Their SHA-256 hashes are respectively:

    ffaa15febfc5d49fe23079d702a69434318a799548b160c7a927a39392ffffa3
    55786ba7e92ed40e005e9d8ca2c79209d026724b56093495a62a87a9ad6340d8
    a13d2da2cef9982a8804c6bd20b9e18b03ba4411d4786fbe4b9653125732f44f

These are rigorous reductions and no-go identities.  They do not classify
$e+\pi$, and the central Hensel digit remains uncontrolled.

## 2026-08-27: exact four-power cofactor content and selected Smith obstruction

The primitive-content problem in the phase-removing four-power quartic
kernel was separated into forced row saturation, a canonical coefficient
factorization, and one selected Smith-coordinate gcd.

Let $\lambda,\epsilon\in\mathbb Z^4$ be integral clearings of the two
rows $L,E$.  The quadratic Hankel annihilator is

$$
Q(t)=q_0+q_1t+q_2t^2,
$$

where

$$
q=(\lambda_1\lambda_3-\lambda_2^2,\,
   \lambda_1\lambda_2-\lambda_0\lambda_3,\,
   \lambda_0\lambda_2-\lambda_1^2).
$$

If

$$
e_s=\sum_{j=0}^2q_j\epsilon_{j+s}\quad(s=0,1),
$$

then the raw phase-removing cubic is

$$
C(t)=Q(t)(e_1-e_0t).
$$

Gauss's lemma gives its exact content:

$$
\boxed{\operatorname {cont}(c)
=\operatorname {cont}(q)\operatorname {cont}(e).}
$$

More explicitly, writing $q=g_qq^*$,
$\widehat e_s=\sum q_j^*\epsilon_{j+s}$, and
$h=\gcd(\widehat e_0,\widehat e_1)$, one obtains

$$
\boxed{\operatorname {cont}(c)=g_q^2h.}
$$

The Plücker-minor identities

$$
\begin{aligned}
e_0&=-\lambda_3p_{01}+\lambda_2p_{02}-\lambda_1p_{12},\\
e_1&=\lambda_0p_{23}-\lambda_1p_{13}+\lambda_2p_{12}
\end{aligned}
$$

prove

$$
\boxed{\delta_2(A)\mid\gcd(e_0,e_1)\mid
\operatorname {cont}(c)},\qquad A=(\lambda;\epsilon).
$$

This identifies a forced saturation factor which must be removed before
any primitive-height inference.  The primitive canonical polynomial is

$$
C^*(t)=Q^*(t)(\eta_1-\eta_0t),
\qquad \eta_s=\widehat e_s/h.
$$

For every endpoint row $x$, its scalar product compresses exactly to

$$
\boxed{x\cdot c^*
=\eta_1\widehat x_0-\eta_0\widehat x_1.}
$$

The endpoint quotient is equally explicit.  Let
$K=\ker_{\mathbb Z}A$, let $B=(\rho;\beta)$ be one jointly cleared
two-row endpoint map, and suppose $M=(A;B)$ has full rank.  If
$s_1\mid s_2$ are the Smith invariants of $B(K)$, then

$$
s_1s_2=\frac{|\det M|}{\delta_2(A)}.
$$

With $N_\rho=(A;\rho)$ and $N_\beta=(A;\beta)$,

$$
s_1=
\frac{\gcd(\delta_3(N_\rho),\delta_3(N_\beta))}
     {\delta_2(A)},\qquad
s_2=\frac{|\det M|}{\delta_2(A)s_1}.
$$

For every primitive $v\in K$, write $(u,w)$ for its primitive
coordinates in a Smith-domain basis.  Then

$$
\boxed{\gcd((Bv)_1,(Bv)_2)
=s_1\gcd\!\left(u,\frac{s_2}{s_1}\right).}
$$

This formula proves that directions attaining both $s_1$ and $s_2$
exist.  Therefore no subexponential content bound can hold uniformly over
all kernel directions when $s_2$ is exponential.  It does not determine
the phase-removing direction.  For the canonical primitive vector $c^*$,
the exact obstruction is

$$
g_\Delta(c^*)=s_1\gcd(u_c,T),\qquad T=s_2/s_1.
$$

Finally, if $\Delta_c$ is the least clearing of its selected rational
endpoint pair and $\Delta$ clears the whole endpoint block, then

$$
g_\Delta(c^*)=\frac{\Delta}{\Delta_c}\,
g_{\mathrm{rat}}(c^*).
$$

This separates block-clearing content from intrinsic endpoint content.
A large quotient index or large block gcd alone therefore cannot prove
that the canonical form is absorbed.  A new local estimate for $u_c$
at prime powers dividing $T$ is required.

The fully audited source, executable certificate, and byte-identical result
are:

    sources/quartic_four_power_primitive_content_smith_reduction.md
    scripts/quartic_four_power_primitive_content_smith_certificate.py
    results/quartic_four_power_primitive_content_smith_certificate.json

Their SHA-256 hashes are respectively:

    09637356ca1aa6f3b2ae6ffd7f78da6d3e452e67ab9e2d0ba2691893911cc82e
    4b52c14b65c43c45a60adf3fd1e9e2080c1da923ac6e0b4848096b506023e497
    16e3c2cd4acd3a6d56910961e05eb1dbb64d37e0fc1f1f16224ecd3b1a4d8586

These are exact arithmetic reductions, not a primitive asymptotic theorem
and not a classification of $e+\pi$.

## 2026-08-27: fixed-slope rational cross product and exact boundary dyadic law

The rational three-power quartic cross product was analyzed at fixed slope,
and its complete two-primary coefficient content was proved on the
transition boundary.  The analytic fixed-slope statement is deliberately
conditional on the stated projected-contour/no-Stokes hypothesis; the
dyadic theorem is unconditional.

For three adjacent powers write

$$
J_s=R_s+\frac{L_s}{2\sqrt2}\log(1+\sqrt2)
+\left(\frac{E_s}{4\sqrt2}+\frac{b_s}{8}\right)\pi,
\qquad 0\le s\le2,
$$

and take $C=L\times E$.  Then

$$
\Lambda=C\cdot J=C\cdot R+\frac{C\cdot b}{8}\pi
$$

is a genuine rational $1,\pi$ form.  If integral column clearings are
$\Delta_s$, define the corresponding three-by-three determinants
$U,V$ from the $L,E,R$ and $L,E,b$ rows.  Multilinearity gives

$$
\boxed{8\Delta_0\Delta_1\Delta_2\Lambda=8U+V\pi.}
$$

Thus the fully primitive endpoint pair is exactly

$$
(p,q)=\frac{(8U,V)}{\gcd(8U,V)}.
$$

No coefficient-height statement which omits this gcd can settle the
branch.

Under the projected-saddle hypothesis at fixed
$k/n\to\kappa>1/2$, let $j(\kappa)$, $e(\kappa)$, and
$\ell(\kappa)$ be the real, positive, and accessible-complex saddle
rates.  Exact three-column determinants give

$$
C\cdot b\asymp
n^{-3/2}e^{n(e+2\ell)}
(-\operatorname {Im}z_i^*)|p-z_i^*|^2,
$$

while $C\cdot J$ has rate $e+\ell+j$, up to its real phase.  Hence

$$
\left|\pi+\frac AB\right|
\le\exp\{n(j(\kappa)-\ell(\kappa))+o(n)\}.
$$

At the transition,

$$
\ell(1/2)-j(1/2)
=1.388912660352581880\ldots.
$$

The universal denominator-cleared form has the much larger rate

$$
G(1/2)=10.643873127064585\ldots.
$$

This is a rigorous pre-primitive barrier: a primitive escape requires the
exact content $\gcd(8U,V)$ to absorb the difference.  It is not an upper
bound on that content.

The boundary family has a stronger unconditional theorem.  Put

$$
F_m=x^{4m}(1-x)^{4m},\qquad
D=x\frac d{dx},\qquad
P_K(T)=\prod_{r=1}^K(4r-1-T),
$$

and reduce

$$
P_K(D)F_m\equiv a_K+b_Kx+c_Kx^2+d_Kx^3
\pmod{x^4+1}.
$$

With $v_K=(a_K-c_K,a_K+c_K)$, exact arithmetic in the free rank-four
ring $\mathbb Z[x]/(x^4+1)$ proves, for every $m\ge1,K\ge0$,

$$
\boxed{
v_2(a_K-c_K)=v_2(a_K+c_K)=m,
}
$$

$$
\boxed{
v_2\det(v_K,v_{K+1})=2m+2+v_2(m),
}
$$

and

$$
\boxed{
v_2\det(v_K,v_{K+2})=2m+3+v_2(m).
}
$$

The proof-critical normalization was audited at the correct precision.
Writing

$$
g(e^tx)\equiv2h_t\pmod{x^4+1},
$$

the normalized $D^2$ projection is divided by $4m$, so its residue
modulo eight must be computed from the Bell expansion modulo $32$.
Terms with at least five differentiated factors vanish; the remaining
four Bell levels are periodic modulo four in both $m$ and $K$.  Their
complete $4\times4$ table yields the sharper congruence

$$
\det(A_{m,K},B_{m,K})\equiv4(m+K)\pmod8.
$$

This is an all-$m,K$ proof, not an extrapolation from the certificate.

At $n=4m,k=2m+1$, the reduced denominator exponents are

$$
d_0=5m-s_2(m),\qquad
d_1=d_0+2,\qquad
d_2=d_0+5+v_2(m+1),
$$

and the primitive cross vector satisfies

$$
\boxed{(v_2(C_0),v_2(C_1),v_2(C_2))
=(0,3,5+v_2(m+1)).}
$$

For the remaining odd coordinate, an exact terminating factorial sum
$S_m$ is proved.  The observed endpoint denominator law is equivalent
to the single weighted Fleck-type congruence

$$
v_2(S_m)=m+s_2(m)+v_2(m)+1.
$$

That congruence, the odd rational-endpoint denominator, and the final odd
gcd remain unproved.  The source and certificate explicitly keep them
separate from the theorem.

The fully audited source, executable certificate, and byte-identical result
are:

    sources/quartic_three_power_fixed_slope_content_barrier.md
    scripts/quartic_three_power_fixed_slope_content_certificate.py
    results/quartic_three_power_fixed_slope_content_certificate.json

Their SHA-256 hashes are respectively:

    c2f662894e40da7f1412ab252b3b68ff9a3f207ed39a687ddc4cfcb81f9360aa
    5619bbc9c2dbcde1a9763c5e70de6da30f2e8035693f1729ff31dcc637e33859
    55d53d07cdbbec988f2d2fa4c70a2958b9ec28d44540c8710556ec6fe10367c0

This isolates the two-primary coefficient arithmetic rigorously but does
not control the primitive endpoint pair and does not classify $e+\pi$.

## 2026-08-27: central adjoint and Hilbert-determinant no-go

The central Bessel resonance was reformulated as a coefficient-matrix
problem and the tempting ambient Hilbert determinant was evaluated exactly.
With $k_j=B_{j+1}$, let

$$
T_{r,r}=2r+1,\qquad T_{r,r-1}=2-4r,\qquad
T_{r,r-2}=2r-1.
$$

Then $Tk=e_0$.  If $\rho$ is the terminal coefficient row and
$c_j=1/(j+1)$, the two bordered determinants are

$$
\det\begin{pmatrix}T&e_0\\\rho^t&0\end{pmatrix}
=-(\det T)(2m-1)D_m,
$$

and

$$
\det\begin{pmatrix}T&e_0\\c^t&0\end{pmatrix}
=-(\det T)\beta_m.
$$

Thus the literal transpose adjoint computes $\beta_m$ rather than
constraining it independently.

For

$$
C_{ij}=\frac1{i+j+2},\qquad
R=2C-e_{m-1}e_{m-1}^t,
$$

the Cauchy inverse and the matrix determinant lemma give

$$
\det R=2^m\det C
\left(1-m\binom{2m-1}{m-1}^{2}\right).
$$

When $p=2m+1$, the final factor is $9/8\pmod p$, so $R$ is
nondegenerate for every $p\ge5$.  The degree-$p$ Frobenius boundary
term is nevertheless decisive:

$$
k^tRk=\beta_m+(2m-1)D_mJ_m.
$$

If $A$ consists of rows $1,\ldots,m-1$ of $T$ and
$\gamma=\prod_{r=1}^{m-1}(2r+1)$, then

$$
\det\begin{pmatrix}R&A^t\\A&0\end{pmatrix}
=(-1)^{m-1}\gamma^2k^tRk.
$$

Conditional on $D_m=0$, this is
$(-1)^{m-1}\gamma^2\beta_m$.  The nonzero Cauchy determinant therefore
removes only a unit under the Schur complement; the remaining compressed
determinant is precisely the original forbidden quantity.  This is an
exact no-go result for the adjoint/Hilbert shortcut, not an exclusion of
the central root.

The audited source, executable certificate, and byte-identical result are:

    sources/bessel_central_adjoint_hilbert_determinant_no_go.md
    scripts/bessel_central_adjoint_hilbert_determinant_certificate.py
    results/bessel_central_adjoint_hilbert_determinant_certificate.json

Their authoritative SHA-256 hashes are respectively:

    6318d4eed143e4cdaf10a8b66260877f555bc122f4dcee3cdfdfe6bed916b3f3
    c029841de1076cbfb0e59c1308679b46efa9013d698bb935881bd5c2b14a4d86
    6d09b794a4bc740079abc71dbfd6e92538df42afab8eea29bfec1e818d090f46

The earlier source hash beginning 2205237a is rejected: that file had
text-escape corruption and was replaced before acceptance.

## 2026-08-27: cubic field obstruction and a mixed rational-period branch

Two degree-three denominator families were reduced exactly.  For
$Q=1+x^3$,

$$
J^{(3)}_{n,k}
=R_{n,k}+\frac{L_{n,k}}3\log2
+\frac{E_{n,k}}{3\sqrt3}\pi.
$$

Consequently a rational combination which cancels $\log2$ belongs to
$\mathbb Q+\mathbb Q\pi/\sqrt3$, and cannot have a nonzero rational
$\pi$-coefficient.  For three adjacent powers, allowing coefficients in
$\mathbb Q(\sqrt3)$ still produces no intrinsic approximation.  If
$D=\det(L,E,R)\ne0$, every coefficientwise
$\mathbb Q+\mathbb Q\pi$ solution is

$$
u=\alpha(L\times E),\qquad v=\beta(L\times R),
$$

and its value is

$$
D\left(\alpha-\frac{\beta}{3}\pi\right).
$$

The determinant is common content, while $\alpha,\beta$ are freely
chosen external scalars.  Primitive reduction therefore returns an
arbitrary preselected rational form rather than a kernel-generated
approximation.  This closes the original cubic route at every slope.

For the mixed denominator

$$
Q=(1+x)(1+x^2)=1+x+x^2+x^3,
$$

the exact Hermite reduction instead gives

$$
H_{n,k}=R_{n,k}+\frac{L_{n,k}}4\log2+\frac{E_{n,k}}8\pi.
$$

The lowering recurrence uses

$$
(Q')^{-1}\equiv\frac{x^2-x}{4}\pmod Q,
$$

and its boundary is $U(1)/4^{j-1}-U(0)$.  Thus two adjacent powers give
a genuine rational $1,\pi$ form.  If
$\Delta_s(L_s,R_s,E_s)=(\lambda_s,\rho_s,\epsilon_s)$ and

$$
U=\lambda_1\rho_0-\lambda_0\rho_1,\qquad
V=\lambda_1\epsilon_0-\lambda_0\epsilon_1,
$$

then

$$
8\Delta_0\Delta_1\Lambda=8U+V\pi,
\qquad
(p,q)=\frac{(8U,V)}{\gcd(8U,V)}.
$$

Reciprocity gives a favorable raw positive-integral balance for
$2/3<k/n<1$, but a rational Hermite boundary survives on the half-line.
The exact example

$$
\int_0^\infty
\frac{x^2(1-x)^2}{((1+x)(1+x^2))^2}\,dx
=1-\frac\pi4
$$

shows why the half-line integral is not the $\pi$-coordinate.  On the
boundary $n=6m,k=4m+1$, every exact primitive form through $n=60$
has modulus below one, but this is finite evidence only.  A contour proof
for the accessible complex residues and an endpoint determinant-gcd
estimate remain necessary.

The audited source, executable certificate, and byte-identical result are:

    sources/cubic_and_mixed_cubic_kernel_field_structure.md
    scripts/cubic_and_mixed_cubic_kernel_certificate.py
    results/cubic_and_mixed_cubic_kernel_certificate.json

Their SHA-256 hashes are respectively:

    667715d432d1f5322d502a7334cc1414f23edebdd9023555a14d4dd45a0926d5
    64491ef73bafac79e5239f75988e04f69377bb52df283a78ad7aaa8dad377229
    cb341829c46052518ab34f260517db4b70b8d5080a7ae4a66632c9a53bf86bfd

These results open one rational-period branch and close another.  They do
not classify $e+\pi$.

## 2026-08-27: exhaustive archive reconciliation

The complete pre-existing archive was divided into three independent thematic
audits: foundations/Padé/pullbacks, factorial digits/cyclotomic units, and
Fourier/Bessel/quartic kernels.  Between them they covered all 124 original
source notes, all 104 original Python programs, the one C++ program, and all
108 original JSON result files.  Every Python program parsed as an AST, every
JSON file parsed, and the C++ file passed a syntax check.  This reconciliation
found no proof that $e+\pi$ is irrational, algebraic, or transcendental.

The audit also caught two implementation defects before their diagnostics were
accepted.  In the quartic boundary checker, the routine intended to compute
$(2r-1)!!$ used $(2r-1)!$; after correction it uses

$$
(2r-1)!!=\frac{(2r)!}{2^r r!}.
$$

A diagnostic labelled as a residue modulo $256$ also lacked its final
reduction.  Both were repaired, and the exact checker was run twice to
byte-identical output.  The all-degree theorem itself is

$$
v_2(S_m)=m+s_2(m)+v_2(m)+1,
$$

so the associated boundary denominator exponent is

$$
3m-s_2(m)-v_2(m)-1.
$$

The final artifacts and hashes are:

    0eb5e178c5fba5a52240e55257830eca97ea2639028e0c2d52e5cb0acfa37c50  sources/quartic_boundary_weighted_fleck_valuation.md
    672d864cdbb91b3283a30ba8caf062601a52801b09919eb1e7fff01d0c7f96a6  scripts/quartic_boundary_weighted_fleck_valuation_certificate.py
    834b52bc8e5003bcf0fb5f5cdb01189fc3fb83bfd3e95b8416914921e08804f9  results/quartic_boundary_weighted_fleck_valuation_certificate.json

This closes only one dyadic coordinate.  The other odd coordinates, the odd
rational endpoint, and the selected final determinant gcd remain open.

## 2026-08-27: full Galois no-go theorems for fixed cyclotomic log systems

Under the temporary hypothesis $s=e+\pi\in\overline{\mathbb Q}$, put
$K=\mathbb Q(s)$.  For an odd prime conductor $n$ unramified in $K$,
the fixed two-log unit edge has full norm

$$
\left|N_{K\mathbb Q(\zeta_n,i)/\mathbb Q}(\Lambda_{n,d})\right|
\asymp_{K,n}
\left[\rho_1^2
\left(\prod_{\rho_k>1}\rho_k^2\right)^{[K:\mathbb Q]}
\right]^d
d^{-2(1+[K:\mathbb Q]|\{k:\rho_k>1\}|)}.
$$

The exponential base is strictly greater than one.  For $n=5$, it is

$$
\varphi^{(4[K:\mathbb Q]-2)d},
$$

up to the displayed polynomial factor.  The ordinary coefficient-field trace
is identically zero; multiplication by $-i$ before tracing collapses the
primitive direction to the elementary partial-sum form $p_ds-q_d$; a
two-fold exterior determinant eliminates $s$, and exterior determinants of
order at least three vanish.  This is a no-go theorem for that fixed edge, not
a contradiction to algebraicity.

A separate full-orbit theorem treats finitely many copies, fixed algebraic
weights, and fixed logarithm sheets at a primitive prime conductor.  Exact
Galois matching requires

$$
\sigma_k(u)=\frac{2i}{p}\sum_{j,a}\sigma_k(C_{j,a})
\bigl(\widetilde{ka}+p m_j(ka)\bigr).
$$

For centered sheets, averaging the centered residues forces $u=0$.  If the
total centered coefficient vector is not even, the unique largest conjugate
pair grows like $\rho_*^d/d$.  If it is even, the centered remainder cancels,
but any nonzero target is supplied by monodromy and every conjugate tends to
$(\pi/e)\sigma_k(u)\ne0$.  A formal Dirichlet-character vector is not the
conjugate vector of one scalar unless this compatibility equation holds.

The audited source hashes are:

    7996462a59ed59a7bf6d5b1bc191078e69390c8c86cd4dd4348f430aceb555d9  sources/galois_balanced_two_log_full_norm_no_go.md
    0f1e1301e0bd875d9d549a66397a20a023991e824a52c0186eb2d9ac0bfb1472  sources/cyclotomic_multilog_galois_matching_no_go.md

These theorems leave open varying conductors, unequal degree allocations,
exponentially tuned coefficient systems, and genuinely different multipoint
Padé constructions.

## 2026-08-27: a certified new prime refutes the fixed-support ideal law

The proposed all-degree assertion that the $n=5$ two-log coordinate ideal
is supported only over $19$, equivalently the proposed containment
$361\in\mathfrak J_d$, is false.  The unconditional counterexample is

$$
(p,d)=(109321,6219),\qquad
\mathfrak p=(109321,t-53267),\qquad t^2+t-1=0.
$$

At this prime the two roots $x=70927$ and $y=38395$ satisfy

$$
P_{6219}(x)=P_{6219}(y)=0\pmod {109321}.
$$

The independent first-jet recurrence gives
$h_{6218}=h_{6219}=0$, and the complementary weighted-factorial form has

$$
m=103101,qquad W_m(85987)=W_m(76603)=0,
$$

with both derivatives nonzero.  At coordinate level,

$$
N_{6219}=3246(t-53267),\qquad
a_{6219}T_{6219}=103634(t-53267)\pmod p.
$$

Finally, a characteristic-zero multiplication-lattice calculation on the two
full generators gives Smith diagonal

$$
(1,109321),
$$

and therefore

$$
N_{\mathbb Q(t)/\mathbb Q}(\mathfrak J_{6219})=109321.
$$

The scan over every odd prime through $200000$ found only $(19,15)$ and
this pair, but that statement is explicitly finite and is not part of the
counterexample proof.  The final artifacts were replayed byte-identically:

    4d38ac26066f100a6af5999e0c9ed2a6b6ddfa5805a102b243c7efdd525fbb53  sources/algebraic_unit_two_log_n5_all_prime_counterexample.md
    c2ea5c245abbf8b12cfb0d6acf8ba7db0098a393d1dd395d34162d511add7b51  scripts/algebraic_unit_two_log_n5_all_prime_counterexample.py
    1383db00767615638db0a9a5c9475a0cd712478ad9f81a60a8e143dcf4b4fddd  results/algebraic_unit_two_log_n5_all_prime_counterexample.json

The surviving ideal problem is aggregate control of a varying exceptional-prime
set, not fixed support over $19$.

## 2026-08-27: Bessel block/resultant dichotomy and exact reflection

For the Bessel endpoint recurrence

$$
q_0=q_1=1,qquad q_n=(4n-2)q_{n-1}+q_{n-2},
$$

the rank-two continuant transition has adjacent determinant $\pm1$.  It
therefore detects simultaneous zeros but is blind to a prime power occurring in
only one block entry.  For the diagonal block
$D_N=\operatorname{diag}(q_N,\ldots,q_{2N-1})$, the largest Smith invariant
is exactly

$$
\operatorname{lcm}(q_N,\ldots,q_{2N-1})
=\frac{\Delta_N(D_N)}{\Delta_{N-1}(D_N)}.
$$

After removing the accepted threshold, its smooth part is exactly the high
singleton term.  The first standard invariant which retains every singleton is
a resultant:

$$
\left|\operatorname{Res}(B_N,F_N)\right|
=((N-1)!)^N\prod_{n=N}^{2N-1}q_n.
$$

It is already of logarithmic size
$(5/2)N^2\log N+O(N^2)$; the unpolluted product itself has size
$(3/2)N^2\log N+O(N^2)$.  Discriminants see collisions rather than isolated
depth, and the first nonzero subresultant discards the singleton information.

The exact central reflection also fails to supply an external bound.  If
$p_0=1,p_1=3$ obeys the same recurrence as $q_n$, then

$$
P_{2n+1}(-n-1)=(-1)^np_nq_n,
$$

and

$$
p_nq_{n-1}-p_{n-1}q_n=2(-1)^{n-1},\qquad
\gcd(p_n,q_n)=1.
$$

Thus, at every odd prime dividing $q_n$, the reflection has exactly the same
valuation as $q_n$; it may also contain unrelated primes from $p_n$.

For fixed $C>0$, the sharp sufficient missing statement can be written

$$
V_N(C)=\max_{\substack{N\le n<2N\\p\le CN\log N}}
v_p(q_n)\log p=o(N\log N).
$$

Indeed, the high singleton sum is at most
$O_C(N)V_N(C)=o(N^2\log N)$.  A uniform polynomial bound
$p^{v_p(q_n)}\le(2N)^A$ would be more than sufficient.  The exact lift

$$
v_{11}(q_{1359})=5
$$

has excess singleton depth three in $[680,1360)$, showing that the high tail
is real.

The final replayed artifacts and hashes are:

    b02e444c67f5449bd4bc4785687ec746195619629b6f8de8694f38a53578aeb2  sources/bessel_block_resultant_singleton_dichotomy.md
    6d3e4b64f432a564386dd35ebdd7f798d9c320b6fc2634185689dbd1e276d3bb  scripts/bessel_block_resultant_singleton_certificate.py
    6a1d036f380e359d4f7a7585a8f4cc1ea73b4f43674c63c9c80a4ecf2e32a51f  results/bessel_block_resultant_singleton_certificate.json

## 2026-08-27: denominator-free common-kernel identity and saturated quotient

For $H\in\mathbb Z[x]$ and $a\in\mathbb Z$, put

$$
f(x)=a+(1+x^2)H'(x),
$$

and define

$$
A(g)=\sum_{k\ge0}(-1)^kg^{(k)}(1),\qquad
B(g)=\sum_{k\ge0}(-1)^kg^{(k)}(0).
$$

The single constraint $A((1+x^2)H')=0$ gives the exact identity

$$
\boxed{
\int_0^1 f(x)\left(e^x+\frac4{1+x^2}\right)\,dx
=a(e+\pi)-B(f)+4(H(1)-H(0)).}
$$

There is no rational denominator clearing.  The weight is positive, but the
short polynomials found so far oscillate, so positivity does not prove
nonvanishing.

The first temporary search used individually primitive rational nullspace rays.
Those rays did not jointly form the saturated integer kernel; at search parameter
$40$, their index was $278628139008$.  An exact saturated reconstruction,
with $f(0)=f(1)=0$, proves for every $D\ge7$ that the integer endpoint map
has image

$$
\Phi(K_D)=8\mathbb Z\times2\mathbb Z.
$$

Its kernel has rank $D-5$.  Most very short full-lattice vectors are therefore
exact zero forms, which must be removed before interpreting LLL output.

The corrected finite search gives, among other forms, the rigorously nonzero
identity

$$
461515305521655600(e+\pi)-2704421761901323052
=5.12\ldots\times10^{-7},
$$

where the sign and decade are certified by rational Taylor/Machin enclosures.
This is a finite approximation, not an irrationality theorem.

On the rank-two useful quotient, exact rational Gram matrices show the capacity
model

$$
\|(u,v)\|_D^2\asymp
\rho^{-2D}u^2+\bigl(4(e+\pi)u+v\bigr)^2,
\qquad \rho=4.61158\ldots.
$$

The finite determinant data are consistent with this asymptotic model.  Generic
Minkowski balancing spends the cheap-direction gain on denominator growth and
reaches

$$
|a(e+\pi)+b|\asymp|a|^{-1},
$$

namely linear-form exponent one or rational-approximation exponent two.  This
explains why determinant/capacity alone cannot cross Roth's threshold.  It is
not an upper bound on exceptional vectors; such a sequence and a uniform
nonvanishing theorem remain open.

The exact package was independently replayed twice, byte-for-byte:

    a7dadecb10eded8f3e683636480c086f28c6dacfc7023d5a488dbdf3ce7ee192  sources/common_kernel_lattice_identity_and_capacity_audit.md
    5cf732291f8a0879cc8cbb5927edf0e726bfdb3b11ec3134fc98b3418f710110  scripts/common_kernel_lattice_exact_certificate.py
    4824876c62b09ae9f1e46aa9278917e49487c53b8e1ed93fb8a520977742127a  results/common_kernel_lattice_exact_certificate.json

No result in these post-audit sections proves that $e+\pi$ is irrational,
algebraic, or transcendental.

## 2026-08-27: exact two-form quotient criterion and circularity audit

The denominator-free common-kernel construction admits a useful exact
two-form criterion.  If, at each degree in an unbounded sequence, two integer
pairs $(a_{D,j},b_{D,j})$ have nonzero determinant and both satisfy

$$
|a_{D,j}\alpha+b_{D,j}|\le\varepsilon_D\longrightarrow0,
$$

then $\alpha$ is irrational.  Indeed, for $\alpha=p/q$ at least one of the
two forms is a nonzero multiple of $1/q$.  This removes the need to certify
the sign of either prescribed form, provided both smallness bounds and exact
nonproportionality are proved at the same degree.

The correct setting is the real quotient by the exact zero-coordinate
polynomials.  If $B_D$ is its sup-norm unit ball, $\Gamma_D$ the coefficient
image, and

$$
\Delta_D=\frac{\operatorname{covol}(\Gamma_D)}
                 {\operatorname{area}(B_D)},
$$

then Minkowski's second theorem gives

$$
2\Delta_D\le\lambda_1(D)\lambda_2(D)\le4\Delta_D.
$$

Thus a lower bound $\lambda_1\ge L_D$ forces $\lambda_2\to0$ only when
$\Delta_D/L_D\to0$, equivalently when
$\lambda_1(D)/\Delta_D\to\infty$.

This threshold is not a free determinant estimate.  If $e+\pi=p/q$, the
all-degree image theorem gives the exact zero direction
$(8q,-8p)\in8\mathbb Z\times2\mathbb Z$.  Every independent direction has
form value at least $1/q$ and hence quotient norm at least $1/(5q)$.  Therefore

$$
\lambda_2(D)\ge\frac1{5q},\qquad
\lambda_1(D)\le20q\Delta_D.
$$

The very estimate needed to force the second minimum to zero already rules
out the rational model.  Numerically, the quotient ellipsoid confirms this
diagnosis: its cheap-axis slope converges to $-(e+\pi)$ and Gauss reduction
returns ordinary continued-fraction convergents and semiconvergents.  Those
computations are explicitly diagnostic, not an all-degree theorem.

At the finite search parameter $40$, two saturated rows have exact pairs

$$
(461515305521655600,-2704421761901323052),
$$

$$
(-805266044026219440,4718757942649659800),
$$

with determinant $559082349120\ne0$.  Rational exponential-series and Machin
enclosures put both form values strictly between $3\cdot10^{-7}$ and
$6\cdot10^{-7}$.  This is a finite certificate only.

Two direct positivity mechanisms also have rigorous obstructions.  If
$(1-x)^r\mid f\in\mathbb Z[x]$ and $A(f)=f(i)=a\ne0$, then $r!\mid a$;
Chebyshev extrapolation gives

$$
\|f\|_{[0,1]}\ge
\frac{r!}{(2R/(R-1))R^{\deg f}},\qquad R=4.611581789\ldots.
$$

If $f=P^2$, the integral representation for $A$ and Laguerre orthogonality
give $A(P^2)\ge(\deg P)!^2$, so the common-kernel equality again forces a
factorially growing lower bound.  The ansatz $x(1-x)P^2$ has real value at
$i$ only when $P(i)=0$, hence only the zero target.  These statements rule out
the obvious square and high-endpoint-multiplicity families, not every
possible nonnegative common-kernel polynomial.

Both exact replay and the explicitly nonrigorous ellipsoid diagnostic matched
their frozen JSON byte-for-byte.  The authoritative hashes are:

    4fcf62e0cf809aa22a7141ba90d02eee0a221c50901f2b7cf5fa0b7ef23f0033  sources/common_kernel_two_form_quotient_audit.md
    cb15028325b9033a6e304ffc308e2aa2ba44ea7257190ff36ef5cd30b740590a  scripts/common_kernel_two_form_certificate.py
    4d6a8dd6a677bcffa7d74c4742ef5a5719477542d25c7b120f8b08ec29ba4f78  results/common_kernel_two_form_certificate.json
    61ce9226bdeaedf6e804d564f3240b96d4e07c2b18017161b23ab34235bfd5c7  scripts/common_kernel_quotient_ellipsoid_diagnostic.py
    4229e190aeba7cabe88fcf0d75377c497c1a98536b01a808c1701546162d438e  results/common_kernel_quotient_ellipsoid_diagnostic.json

Nothing in this two-form audit proves irrationality, algebraicity, or
transcendence of $e+\pi$.

## 2026-08-27: fixed and moving prime-support transcendence criteria

Let $\alpha=e+\pi$, and let

$$
\Lambda_\nu=Q_\nu\alpha-P_\nu,qquad
\gcd(P_\nu,Q_\nu)=1,qquad Q_\nu>0.
$$

For a finite prime set $\mathcal S$, write $m_{\mathcal S^c}$ for the
part of $|m|$ supported outside $\mathcal S$.  The exact $p$-adic
Subspace-Theorem criterion proved in the new source is:

$$
Q_\nu\to\infty,qquad
|\Lambda_\nu|(P_\nu)_{\mathcal S^c}(Q_\nu)_{\mathcal S^c}
\le Q_\nu^{1-\eta}
$$

for one fixed $\eta>0$ and infinitely many primitive pairs implies that
$e+\pi$ is transcendental.  At the real place use
$(-X+\alpha Y,Y)$, and at every $p\in\mathcal S$ use $(X,Y)$.  Their exact
product at $(P,Q)$ is

$$
\prod_v|L_{1,v}L_{2,v}|_v
=\frac{|\Lambda|P_{\mathcal S^c}Q_{\mathcal S^c}}{|P|}.
$$

The assumed inequality makes this $O(Q^{-\eta})$.  If $\alpha$ were
algebraic, the Subspace Theorem would place all sufficiently large points on
finitely many rational lines, but a rational line contains at most one
primitive point with $Q>0$.  This also handles rational $\alpha$, including
the unique possible primitive exact-zero point.

A quantitative version permits a different common prime set in each block.
For $M_j$ distinct primitive points, $s_j=1+|\mathcal S_j|$, minimum
$Q\to\infty$, and the same weighted inequality throughout the block,
Schlickewei's theorem gives at most

$$
\left\lfloor
(8s_jD)^{2^{14}\eta^{-2}s_j^6}
\right\rfloor
$$

rational lines under an algebraicity hypothesis, where $D$ is the fixed
normal-closure degree.  Consequently

$$
s_j^6\log(s_j+2)=o(\log M_j)
$$

is sufficient for transcendence.  This requires sparse support for the union
of every coefficient prime in the entire block; a per-point bound on the
number of primes is not enough.

For the factorial-digit forms

$$
W_{a,b}=\Delta^b(a!),\quad Z_{a,b}=\Delta^bC_a,\quad
H_{a,b}=\gcd(W_{a,b},Z_{a,b}),
$$

$$
Q_{a,b}=W_{a,b}/H_{a,b},\quad
P_{a,b}=Z_{a,b}/H_{a,b},\quad
\Lambda_{a,b}=\Delta^b x_a/H_{a,b},
$$

the analytic condition is already complete.  Uniformly for
$0\le b\le a+1$, the digit difference is $\exp(O(a))$ while
$\log W_{a,b}=\Omega(a\log a)$, and hence eventually

$$
|\Lambda_{a,b}|\le Q_{a,b}^{1/2}.
$$

Thus a fixed two-coefficient support theorem, or ultra-sparse cumulative
block support together with distinct unbounded primitive denominators, would
prove transcendence with no further analytic estimate.  The exact
denominator-only fixed-support target is

$$
U_{a,b}(Q_{a,b})_{\mathcal S^c}W_{a,b}^{\eta}
\le H_{a,b}^{1+\eta}.
$$

The family audit shows why no archived construction yet meets the criterion.
The cyclotomic $u_7$ ray would need near-total cancellation of its factorial
denominator-transfer divisor as well as support concentration.  The Bessel
theorems control square-free small-prime mass but not excess valuations,
outside cofactors, or the final numerator.  The common-kernel image
$8\mathbb Z\times2\mathbb Z$ is only a fixed divisibility statement.  Quartic
dyadic coordinate denominators acquire lcm, endpoint, selected-content, and
phase costs before reaching a final primitive pair.

The quantitative normalization was checked against page 246, equations
(1.3)--(1.5), of Schlickewei's 1992 primary paper.  During integration two
damaged TeX escapes were repaired; no mathematical statement changed.  The
current source hash is:

    384c195a8e113a817f9bbc08ad68b9eca1733491a99508cbfc53d76d8d7c637c  sources/padic_subspace_prime_support_transcendence_criterion.md

This criterion does not prove that any archived family has the required
coefficient support, so it does not yet classify $e+\pi$.

## 2026-08-27: saturated multi-exponential Hermite--Padé audit

For fixed integers $N\ge2$ and $m\ge1$, the diagonal type-I system for
$1,e^z,\ldots,e^{mz}$ has an exact residue representation.  With
$U=(m+1)(n+1)$ and $L=U-1$,

$$
A_{j,n}(z)=[u^n]\frac{e^{uz}}
 {\prod_{k\ne j}(j-k+u)^{n+1}},\qquad
R_{m,n}(z)=\sum_{j=0}^m A_{j,n}(z)e^{jz}
 =\frac{z^L}{L!}\mathbb E(e^{zT}),
$$

where the grouped simplex coordinates giving $T$ have the
$\operatorname{Dirichlet}(n+1,\ldots,n+1)$ law.  Its variance is

$$
\operatorname{Var}(T)=
\frac{m(m+2)}{12((m+1)(n+1)+1)}.
$$

Consequently the factorial upper bound at $z=ie/N$ is asymptotically sharp.
The universal clearing

$$
C_{m,n}=n!(m!)^{n+1}\operatorname{lcm}(1,\ldots,m)^n
$$

and a coefficient of only exponential size show, even after primitive
normalization,

$$
\log H=n\log n+O_{m,N}(n),\qquad
\log|\mathcal P(e,e^{is/N})|=-mn\log n+O_{m,N}(n).
$$

This does not yield a small algebraic integer under the temporary assumption
$s=e+\pi\in\overline{\mathbb Q}$.  Lindemann--Weierstrass applied to the
distinct algebraic exponents $r+jis/N$ proves that $e$ and $e^{is/N}$ are
algebraically independent.  Coefficient-field products, root-of-unity
projections, and complex-conjugate products are therefore still nonconstant
transcendental polynomial values.  Resultants in the exponential variable
leave a polynomial in $e$ and pay the gained height exponent.

The adjacent systems give the exact determinant

$$
\det\mathcal A(z)=
\frac{(-1)^{(n+1)m(m+1)/2}z^U}
 {(n+1)!^{m+1}(\prod_{k=0}^m k!)^{2(n+1)}}.
$$

After substituting $z=iX/N$ and clearing every row by $N^{n+1}$, the
$N^{-U}$ factor cancels exactly and the determinant is a root of unity times
$J_{m,n}X^U$, with $J_{m,n}$ a positive integer.  It grows at $X=e$; at the
algebraic endpoint its full number-field norm is at least one.  The same
residue argument for arbitrary pole multiplicities proves all-multi-index
normality, and hence the asserted type-II ranks.  A full coefficient
determinant has dimension $(m+1)(n+1)$ and incurs the still larger
$\Theta(n^2\log n)$ elimination cost.

The exact certificate checks 20 diagonal systems, 12 adjacent determinants,
24 type-II rank cases, and 56 Dirichlet variances.  It compiled and replayed
byte-identically.  Authoritative hashes are:

    679e8587e94f1563920bb6635b387c00732480deb1ac14d79df22df31aec6529  sources/nested_multi_exponential_hp_norm_barrier.md
    79fd558addcb9818c0138241ccdbb7eb2b660405bea4a2b31bf94ff5c3f3ce01  scripts/nested_multi_exponential_hp_certificate.py
    d04d2cedf77de24e65feaa8ded28aa15539f0fd2153d62ca17e407e6f3adc63e  results/nested_multi_exponential_hp_certificate.json

This closes the fixed-$(N,m)$ multi-exponential type-I/type-II elimination
mechanism, not every growing-parameter or arithmetically enriched construction.
It does not classify $e+\pi$.

## 2026-08-27: positive common-kernel endpoint bootstrap

The nonnegative cone of the denominator-free common-kernel construction admits
a uniform obstruction that is substantially sharper than the earlier
perfect-square examples.  For an integer polynomial $f$ of exact degree $n$
with $A(f)=f(i)=a\ne0$, let

$$
R=4.611581789\ldots,\qquad C_R={R\over R-1},
$$

and

$$
\mathcal D_{n,r}=\max\left\{1,\max_{1\le k<r}
 {2^{k+1}(n+1)n^{2k}\over(2k-1)!!}\right\}.
$$

Markov's derivative inequality, the exact endpoint derivative relations forced
by $f(i)=a$, and Bernstein--Walsh at $i$ give

$$
\|f\|_{[0,1]}\ge
\max_{1\le r\le n}
\min\left\{\mathcal D_{n,r}^{-1},{r!\over C_RR^n}\right\}.
$$

Choosing $r$ on the $n/2+o(n)$ scale proves

$$
\liminf_{n\to\infty}\|f\|_{[0,1]}^{1/n}
\ge R^{-1/2}=0.4656665\ldots .
$$

For nonnegative common-kernel $f$, its unnormalized target integral is bounded
below by the same exponential scale up to the explicit factor $3/(8n^2)$.
Thus exponential integral decay forces matching exponential growth of the
unnormalized coefficient $a$, and the resulting unnormalized linear-form
exponent is at most one.

This is not a primitive no-go theorem.  If $g=\gcd(a,b)$, the lower bound for
the primitive form is divided by $g$, and no theorem here controls that gcd.
That distinction is essential: the positive cone contains the exact witness

$$
f(x)=4x(1-x)^2(31-3x^2),\qquad (a,b)=(272,-1544),
$$

and finite beta-cone circuits through degree 40 have nontrivial contents.  The
finite computation therefore checks the construction and the normalization
caveat; it cannot replace an all-degree gcd theorem.

The certificate checked 40 exact beta-cone systems, compiled, and replayed
byte-identically.  Authoritative hashes are:

    596e21e493f16447307764b100bae383f5a639c7ad466150a50932b4a878d487  sources/common_kernel_positive_cone_endpoint_bootstrap_barrier.md
    ca1db0bc142979bb9e566d5a93664ae3bcb914c9ec7aaa698e3f36c3b2171d4e  scripts/common_kernel_positive_cone_endpoint_bootstrap_certificate.py
    35cf99fe9eb6e4a2203d2c357a3a04b36478628bce686a4907bb3dcd6e248a3d  results/common_kernel_positive_cone_endpoint_bootstrap_certificate.json

The theorem closes positivity before primitive normalization, but it does not
classify $e+\pi$.

## 2026-08-27: factorial-digit projective saturation and support dispersion

Let $V_n=(C_n,n!)^{\mathsf T}$ and
$F_{a,b}=\Delta^bV_a$.  The digit recurrence gives the exact block lattice

$$
\operatorname{span}_{\mathbb Z}\{V_a,\ldots,V_{a+B}\}
=\operatorname{span}_{\mathbb Z}\{F_{a,0},\ldots,F_{a,B}\}
=\operatorname{span}_{\mathbb Z}\{V_a,(g_{a,B},0)^{\mathsf T}\},
$$

where $g_{a,B}=\gcd(c_{a+1},\ldots,c_{a+B})$.  If
$r=\gcd(C_a,a!,g_{a,B})$, its Smith invariants are exactly
$r$ and $g_{a,B}a!/r$.  Hence every block of width at least one has full
projective saturation: after endpoint primitization its integer combinations
produce every primitive pair $(P,Q)$.  The same is true if the individual
input columns are first made primitive.

This does not create useful support.  Already for $b=0,1$, if
$c=c_{a+1}$ and $T=a!P-QC_a$, then

$$
(cQ-aT)F_{a,0}+TF_{a,1}=ca!(P,Q)^{\mathsf T}
$$

and application of the target functional gives

$$
(cQ-aT)x_a+T\Delta x_a
=ca!\bigl(Q(e+\pi)-P\bigr).
$$

Thus any manufactured support is obtained only after the full factorial gain
has become endpoint content and is divided away.  Coefficient boxes do not
restore the lost dimension: regardless of block width, a box of radius $H$
has only $O(H^2)$ distinct endpoint images.  Sign constraints are subsets of
the same box; fixed divisibilities scale both the image count and value range;
and apparent higher-dimensional collisions are exact zero forms.

For the untouched truncations, put

$$
h_n=\gcd(C_n,n!),\qquad p_n=C_n/h_n,\qquad q_n=n!/h_n.
$$

For $n<m$, the positive digit sum

$$
K_{n,m}=C_m-\frac{m!}{n!}C_n
$$

satisfies

$$
0<K_{n,m}<\frac{m!}{n!}\left(1+\frac1n\right),
\qquad m!\mid K_{n,m}q_nq_m.
$$

Taking valuations outside a fixed finite prime set $\mathcal S$ yields

$$
(q_n)_{\mathcal S^c}(q_m)_{\mathcal S^c}
>\frac{n!}{(1+1/n)(m!)_{\mathcal S}}.
$$

Consequently two comparable indices cannot both have small outside support,
and every infinite sequence satisfying the denominator-only fixed-support
criterion with exponent $\eta$ has

$$
\liminf_{j\to\infty}\frac{n_{j+1}}{n_j}\ge1+\eta.
$$

The surviving moving-support statement can be expressed without prime-power
loss.  Define

$$
\mathcal A(q)=\sum_{p\mid q}\frac{\log p}{p-1}.
$$

Since $q_n\mid n!$, Legendre's formula gives
$\log q_n\le n\mathcal A(q_n)$.  Therefore, if for some fixed
$\varepsilon>0$ there are infinitely many $n$ with

$$
\mathcal A(q_n)\le\left(\frac12-\varepsilon\right)\log n,
$$

then the exact truncation error is $<q_n^{-2-\delta}$ for a fixed
$\delta>0$.  The denominators are unbounded; Roth excludes algebraic
irrationality, and the exact rational case $q_n=n!$ eventually excludes
rationality.  Hence this support inequality would prove that $e+\pi$ is
transcendental.  The Mertens estimate gives the particularly transparent
sufficient condition $P^+(q_n)\le n^\theta$ infinitely often for any fixed
$\theta<1/2$.  Neither condition is currently proved for the actual digits.

The companion certificate checks 1,122 block HNF/Smith identities, 495
explicit universal combinations, and all 4,950 pairs through index 100 for
three support sets.  It compiled and replayed byte-identically.  Its hashes
are:

    f245c5fa5dc9b8a673f7dd6456bfc9266913a8edb138fb40929153ee9975dae5  sources/factorial_digit_integer_combination_support_barrier.md
    ed44a627bc0cf05a7471d1db5bfe12c0c5988fa731696d8c47226b5920cf4fc9  scripts/factorial_digit_combination_support_certificate.py
    d0d684d487c13a8f533dd97f628b070ef0f622166f5f7aab34413a4732755c4b  results/factorial_digit_combination_support_certificate.json

These theorems sharply restrict the coefficient-support route but do not
classify $e+\pi$.

## 2026-08-27: Bessel argument simplicity and inherited index slopes

Two different Hensel problems for the Bessel Padé denominator have now been
separated exactly.  Write

$$
Q_n(x)=\sum_{k=0}^n(-1)^k
\frac{(2n-k)!}{k!(n-k)!}x^k,
\qquad P_n(x)=Q_n(-x),
$$

and $q_n=Q_n(1)$.  The exact Padé Wronskian is

$$
P_n'Q_n-P_nQ_n'-P_nQ_n=(-1)^{n+1}x^{2n}.
$$

At $x=1$ it gives

$$
P_n(1)Q_n'(1)\equiv(-1)^n\pmod {q_n}.
$$

Consequently, if $a=v_p(q_n)>0$, the polynomial $Q_n(x)$ has a unique root
$\xi_{n,p}\in1+p\mathbb Z_p$ with

$$
v_p(1-\xi_{n,p})=a,
\qquad
\xi_{n,p}\equiv1-(-1)^nP_n(1)q_n\pmod {p^{2a}}.
$$

This is exact but not a height improvement:
$\operatorname{Res}_x(x-1,Q_n)=q_n$ and
$H(Q_n)=(2n)!/n!$, so the polynomial height, resultant, and target valuation
all remain on the $n\log n$ scale.  It also concerns variation in the
argument $x$, not variation of the index $n$.

The index problem has a separate uniform theorem.  For every odd prime $p$,
$a\ge1$, $M=p^a$, and integer $n$,

$$
q_{n+2M}+2q_{n+M}+q_n
\equiv2p^{2a-1}q_n\pmod {p^{2a}}.
$$

The proof first evaluates $D_0=q_{2M}+2q_M+q_0$.  An exact factorial
factorization shows that the unique term below modulus $p^{2a}$ is $j=p$,
whose residue is $2p^{2a-1}$ by Wilson.  Extending the recurrence through
$q_{-n-1}=-q_n$ and applying a discrete Wronskian at the reflected central
pair proves $D_1\equiv D_0\pmod {M^2}$ and propagates the formula to every
index.

For a root $r\bmod M$, define

$$
\delta_M(r)=\frac{-q_{r+M}-q_r}{M}\pmod M.
$$

Then

$$
(-1)^tq_{r+tM}\equiv q_r+tM\delta_M(r)\pmod {M^2}.
$$

If $d_M(r)=\gcd(\delta_M(r),M)$, the exact number of children modulo
$M^2$ is $d_M(r)$ when $d_M(r)\mid q_r/M$, and zero otherwise.  A further
quotient-recurrence calculation proves, for $a\ge2$,

$$
\delta_{p^a}(n)\equiv\delta_p(n)-q_n\pmod p.
$$

On a root this reduces to slope inheritance.  Every ordinary root modulo
$p$ has exactly one compatible descendant at every level, while a singular
descendant remains singular and at each exponent either dies or has all $p$
children.  Thus, if $O_p,S_p$ count ordinary and singular first-level roots,

$$
O_p\le R_{p^a}\le O_p+p^{a-1}S_p.
$$

The result sharply improves density information but not the required height
tail.  One must still exclude all-prime singular branching and, even on a
unique ordinary branch, bound the length of initial zero strings in the
$p$-adic index root.  The ordinary branch with $11^5\mid q_{1359}$ shows
that simplicity alone does not provide such a digit-complexity estimate.

Both notes were read line by line.  The factorial residues underlying slope
inheritance were expanded during audit, all TeX damage was repaired, and both
certificates compiled and replayed byte-identically.  Authoritative hashes
are:

    f08816f9bbbe96f6ea5ba09efed8d6f4dd84d69e282d699ff56622afcd06933d  sources/bessel_pade_argument_hensel_exact_no_go.md
    d25ce8aaba60055fde8a27503b4223b11f634b95e23e761761ae380e930633e7  scripts/bessel_pade_argument_hensel_certificate.py
    59f3437099aa2a483ffbb683102690009e4c1f7f39157f89d71a926a2281939f  results/bessel_pade_argument_hensel_certificate.json
    95f68e65b3a7458b869cdf610a28e77a9062e1467d78747dc2809563e84a2ee1  sources/bessel_prime_power_second_antiperiod_double_lift.md
    3ddb35fe31696478d46321b71bdf90d0b64a21ae92f4a6fbde0f286b48f19396  scripts/bessel_prime_power_second_antiperiod_certificate.py
    c9145c3911f04010a68707a5cbbf3da4f6a420e24888c173205d885e48b58115  results/bessel_prime_power_second_antiperiod_certificate.json

These are structural advances, not a classification of $e+\pi$.

## 2026-08-27: p-adic interpolation and root-of-unity endpoint reduction

Four further packages have been completed and independently replayed.

First, the signed Bessel denominator (f(n)=(-1)^nq_n) extends uniquely to
a (1)-Lipschitz function on every ℚ_p. Its explicit Mahler coefficients
have exact valuation slope (1/(2(p-1))), it obeys the continued index
recurrence, and an ordinary root ρ satisfies



$$
v_p(q_n)=v_p(n-\rho)
$$



throughout its residue class. A second representation



$$
f_p(x)=\sum_{k\ge0}\frac{(-x)_k(x+1)_k}{k!}
$$



converges uniformly, is a Newton series in (x(x+1)), and makes the
reflection (x\mapsto-x-1) exact. Both descriptions reduce the remaining
high prime-power tail to the digit complexity of one ordinary (p)-adic
zero. Neither yields the required non-Liouville estimate: direct truncation
either loses at least half the desired depth or reaches the full Bessel
height (n\log n).

Second, a constrained Hermite–Padé form



$$
R(z)=S(z)+(1+e^z)B(z)
$$



has been constructed so that its special value at (z=i\pi=i(s-e)) is the
single polynomial (S(i(s-e))) in (e) over ℚ(s,i), assuming
(s=e+\pi) algebraic. This removes the fatal two-generator norm defect.
For one exponential block the construction is exactly Padé approximation
to (1/(1+e^z)); positive tangent-number moments prove all-degree normality
and the fixed-degree endpoint asymptotic. The first nontrivial endpoint
denominator is an exact quotient of consecutive tangent numbers. Fixed
degree has factorial primitive height, while diagonal degree has matching
±(n\log n) height/value exponents.

Third, the endpoint forms were compared with a rigorous polynomial measure
for (e) over the hypothetical coefficient field ℚ(s,i). At fixed endpoint
degree (D), the required contradiction threshold is
(r^2D+r-1), where (r=[\mathbb Q(s):\mathbb Q]). The present endpoint
decay does not beat it. At growing degree, every available measure loses at
least a linear factor in (D), again overwhelming the construction.

The authoritative hashes and exact theorem statements are recorded in
`active_checkpoint_20260827.md`. No claim that (e+\pi) has been classified
is made. The next live tests are higher endpoint multiplicity/frequency
patterns and a possible dichotomy converting main-scale Bessel divisibility
from an archimedean obstruction into a (p)-adic support advantage.

## 2026-08-27: three attempted escapes closed exactly

The fixed-prime Bessel escape has been resolved for the fully matched
critical-Fourier construction. For the primitive match, both outside-(p)
cofactors are explicit, and a main-scale (p)-power in (q_n) does not establish
the Subspace inequality: away from exact valuation resonance with the Fourier
coefficient, the positive matched form diverges. The formerly surviving
resonance is now excluded by an all-parameter fixed-prime estimate. Writing
(n=2r) and (K=k-1), an exact positive super-Catalan factorization gives
(0<F_r(K)<(8K)^r); Legendre's digit-sum formula then proves



$$
v_p(B_{n,k})\log p\le \frac n2\log(8K)
 +4(1+\lfloor\log_pK\rfloor)\log p.
$$



This has leading scale ((1/2)n\log n), only half the hypothetical
main-scale Bessel depth, so exponent resonance is eventually impossible.
The accepted low and very-high matching theorems cover the outer ranges,
closing every (k>n) for this conversion. The general singleton-support
reason remains decisive: for a primitive pair, one coefficient is a
(p)-unit, so the outside-product is (\gg Q); the real linear form must
genuinely decay like a negative power of (Q). Different non-raw auxiliary
families remain outside this no-go.

The fixed-endpoint-degree root-of-unity escape has also been resolved. For
all (m\ge1,n\ge2), the (D=2) endpoint is an explicit rational quadratic
constructed from one functional value of a multiset Eulerian polynomial.
Its denominator is nonzero by Simion's simple-root theorem, and an exact pole
formula cancels the first pair (\pm i\pi), leaving the pair (\pm3i\pi).
Nevertheless, every fixed-degree primitive integer endpoint obeys an
effective algebraic-approximation lower bound at (i\pi). Therefore growing
the number of exponentials cannot make the primitive exponent unbounded at
one fixed endpoint degree. Coupled growing degree and determinants of several
endpoints remain logically open.

Finally, the current (E/G/\log) literature was audited theorem by theorem.
Assuming (s=e+\pi) algebraic forces every exact (E/E) representation of
(e,\pi) to have intersecting scaled inverse-Borel singularity sets;
otherwise Delaygue's theorem would already contradict the assumed linear
relation. Every exact algebraic logarithm similarly lands in the exceptional
Borel branch of Fischler–Rivoal. The assumption also puts the transcendental
numbers (e,π) in (\mathbf E\cap\mathbf G), but exclusion of such an
intersection remains a value-ring conjecture, not a consequence of the
known functional intersection. Exact statements and hashes for all three
packages are frozen in `active_checkpoint_20260827.md`.

## 2026-08-27: exterior, non-raw Bessel, and explicit mixed-pair audits

The coupled-degree exterior-power proposal was reduced to its actual
primitive endpoint invariant. A saturated basis of $\nu$ endpoint
polynomials has a divided-derivative Wronskian of actual degree
$\sum d_j-\nu(\nu-1)/2$, with a basis-independent primitive content. Under
the algebraicity hypothesis it becomes one integral polynomial in $e$, and
the full finite-height relative-norm threshold is explicit. The construction
with one factor $1+e^z$, however, inherits only the endpoint-value column;
the same scalar covector cannot occur twice in an exterior determinant. The
top Wronskian is exactly the coefficient determinant and primitively $\pm1$.
Higher endpoint multiplicity is the only direct source of further inherited
jet columns, and the generic exponent ledger retains at least the
linear-in-degree cost of the available measure. Exact finite computations on
460 tuples found no large degree, content, or primitive-height collapse.

The parameter-shift Bessel branch was tested against the 2026
$\Sigma$-operator theory and against arbitrary finite shift determinants.
The recurrence maps to a differential operator irregular at zero, while the
factorial-growth sequence has a radius-zero generating series and therefore
cannot satisfy any $\Sigma$-operator eventually. All finite shifts reduce
over $\mathbb Z[x]$ to $f_p(x),f_p(x+1)$. Since the second value is a
unit at an ordinary root, every local order is exactly the order of a
residual integer polynomial. Determinants that vanish formally at the root
contain $q_n$ at integer indices and pay the full Bessel height; all others
simply restate the residual-polynomial approximation problem. The first
parameter derivative is $-\sum m!$, so jet Padé forms import an unresolved
fixed-prime Euler-factorial problem rather than solve it.

The lowest-order mixed $E/G$ example was also computed completely. The
functions $e^z$ and $s-4\arctan z$ are algebraically independent over
$\overline{\mathbb Q}(z)$, have product Galois group
$\mathbb G_m\times\mathbb G_a$, and occur in a rational system ordinary at
zero and one. Under algebraic $s=e+\pi$, their algebraically normalized
solution values coincide at one anyway. The normalized connection and
monodromy matrices display $e$ and $\pi$ explicitly. Closing the
alternative $E$-system moves $\pi$ to infinity, and inverse Borel gives
only the exact rational vanishing perturbation
$s(t-1)/(t+1)$. This isolates the survivor as numerical mixed-period
injectivity for a specific rank-three solvable system.

All source proofs and exact certificate hashes are frozen in
`active_checkpoint_20260827.md`. None of these audits proves the target
classification.

## 2026-08-27: exact survivor localization

The common-kernel positivity branch now has a first-order arithmetic
coordinate. The Stein operator
$\mathcal TP=(1-x)P'-xP$ is an integral bijection onto $\ker A$, and
the two endpoint conditions reduce to one explicit rank-two Robin lattice
modulo $(1+x^2)^2$. This gives the lossless representation



$$
F=a+\mathcal TP,qquad
P=(1+x^2)^2Q+u(1+2x+x^3)+v(9x-x^2+4x^3).
$$



The output constant is explicit in the coefficients of
$\mathcal TP/(1+x^2)$. More strikingly, the integral Taylor truncations of
the zero-residual ODE give exactly $F_N=(1-x)^N$, which is positive and
has weighted integral tending to zero. They fail only the two Robin data,
by $(1-i)^N-N!$. The construction problem is therefore no longer a vague
search through a codimension-three polynomial lattice: it is the concrete
problem of correcting those exterior data inside the displayed lattice
without losing primitive decay. Taking real parts of the common endpoint
identity shows that a residual with nonnegative $(1-x)$-monomial
coefficients must be constant. Hence no positive combination of the Taylor
blocks can do the correction; the needed polynomial must have signed
monomial coefficients but remain nonnegative on $[0,1]$.

The proposed noncanonical two-column endpoint escape was reduced to one
polynomial $\Gamma_{C,D}=C\beta_D-D\beta_C$. Endpoint order equals
$(y+1)$-adic order before exponential substitution, so individual extra
jets are exactly higher endpoint multiplicity. At determinant level,
$\Gamma=0$ is necessary and sufficient. A zero estimate shows that in the
range $n+(2-m)D-\nu+2\ge0$, this forces both forms to be polynomial
multiples of one common remainder. For $m=1$, the complete parity exception
is exactly a square. The remaining range is the high-frequency inequality
$n<(m-2)D$, where a structured secondary exponential polynomial would need
exceptional origin order.

The Bessel residual search was carried through the two canonical Newton
coordinates and the first nonlinear recurrence invariants. Exact binomial
inversion makes every evaluated Mahler summand have one sign and exposes the
full Bessel coefficient scale. The termwise local estimate has a central-
binomial imbalance of only logarithmic size and cannot certify more than
half depth. The residue-grid basis is no better, diagonal analytic
renormalization changes no summand, polynomial quadratic invariants do not
exist, and the Hankel determinant is a unit at an ordinary root. What remains
is explicitly a nontriangular residual-polynomial lattice problem with both
high local valuation and sub-main primitive $\ell^1$-height.

That last lattice problem was then solved exactly at the level of one root
congruence. At the target depth $a=v_p(n-\rho)$, the condition
$v_p(B(\rho))\ge a$ is simply $p^a\mid B(n)$. In coefficient space its
lattice basis is $p^a$ together with the $d$ multiples
$(x-n)x^j$; all short directions have zero evaluation, and the quotient is
exactly $p^a\mathbb Z$. The dual lattice contains only the evaluation
functional divided by $p^a$. In the natural evaluation-weighted body every
usable point has norm at least $p^a$, while a primitive linear polynomial
attains $p^a+1$. Thus one-place transference and coefficient capacity are
not merely weak: they are equivalent to the desired bound. A survivor must
use related multiple places or new recurrence-specific local equations.

Finally, every split tensor/gauge manipulation of the explicit mixed
$\mathbb G_m\times\mathbb G_a$ system was excluded at once. Its tensor
coordinate ring remains
$\overline{\mathbb Q}(z)[e^z,e^{-z},-4\arctan z]$; monodromy separates the
pure $E$ subring and regular-singular growth separates the pure $G$
subring. Endpoint-regular rational gauges preserve the connection field
exactly. The numerical hyperplane encoding $e+\pi=s$ is not group-stable.
The only uncensored mixed route is now a genuinely non-split differential
extension which adds new iterated integrals and a new arithmetic connection
theorem.

The four source packages, exact certificates, replays, and hashes are frozen
in `active_checkpoint_20260827.md`. No target classification is claimed.

## 2026-08-27: high-frequency, nonsplit, and multi-prime survivors

Three successor branches have now been reduced exactly and centrally
replayed.

For noncanonical root-of-unity inheritance, vanishing of the two-column
correction produces a secondary form
$(y+1)H=C T_D-D T_C$. The space in which
$H(z,e^z)=O(z^{m(n+1)+D-1})$ could live has exact dimension
$(m-2)D-n$. It is therefore genuinely available throughout the unresolved
high-frequency range; a zero count alone cannot exclude the exterior
syzygy. Basis changes and the natural frequency/splitting symmetries preserve
the correction. An exact good-reduction certificate proves it nonzero for
all 1,762 admissible triples with $m\le20,n\le16,D\le12$. This is a finite
theorem only. The missing result is all-parameter normality, plausibly through
total positivity of the coupled endpoint map, together with a separate
primitive Wronskian-height estimate.

For the mixed differential system, all rank-three cross extensions are
classified by explicit rational first-order coboundary equations. The system
whose solution value is exactly $e+\pi$ is split. The simplest nonsplit
choice $r(z)=1/(z-2)$ has a full four-dimensional solvable differential
Galois group, certified by a nonzero monodromy commutator, but its target
entry is


$$
e+\pi+e\int_0^1\frac{e^{-t}(-4\arctan t)}{t-2}\,dt,
$$


and the added integral is strictly positive. Functional independence of the
new iterated integrals does not imply numerical independence of their values.
An arithmetic cancellation of the new connection period would itself require
the sort of specialization theorem the original problem lacks.

For Bessel residuals, imposing ordinary-root depth simultaneously at several
primes is exactly the CRT congruence $Q\mid B(n)$. If a restricted additive
residual family has evaluation ideal $g\mathbb Z$, its constrained index is
$Q/(Q,g)$ and its constrained evaluation ideal is
$\operatorname{lcm}(Q,g)\mathbb Z$. Thus every apparent determinant saving
is already paid by evaluated divisibility. The adjacent shift module is
unimodular, so the recurrence itself supplies no hidden sublattice; content
normalization likewise cancels no more local depth than its archimedean size.

All statements, scripts, exact outputs, and authoritative SHA-256 hashes are
frozen in `active_checkpoint_20260827.md`. None proves that $e+\pi$ is
algebraic, irrational, or transcendental. The live constructions are a
signed-but-positive Robin correction, an all-parameter high-frequency
normality theorem or exception, genuinely distinct Bessel local equations,
and a nonsplit extension whose new connection period is provably controlled.

## 2026-08-27: all-degree Bessel invariants and two-center accounting

The recurrence search has two additional exact boundaries. Every polynomial
constant-multiplier invariant in the index and one two-dimensional Bessel
state is constant or zero, in every state degree. The proof uses the exact
backward vector $(q_n-s_n,s_n)$, its transcendental limiting slope
$(e-1)/2$, and factorial-scale growth of $q_n$; it does not import an
unproved $p$-adic factorial assertion.

At two integer centers, the simultaneous evaluation lattice has index
$PR/\gcd(P,R,h)$. Two independent residuals therefore pay the summed
modulus through their coefficient determinant. One residual can compress two
conditions into one vector, but only with the expected factor-two loss. The
primitive recurrence determinant
$q_ns_{n+h}-s_nq_{n+h}=(-1)^nC_h(n)$ is genuinely small, yet its exact gcd
and valuation laws show that it measures only overlap between the two
denominators. It cannot carry independent local depths.

Both theorem packages and their byte-identical replays are frozen in
`active_checkpoint_20260827.md`. At this stage the remaining Bessel
possibilities included rational/nonconstant-multiplier invariants, multiple
independent states, or a nonlocal transform; the next entry closes the first
of those possibilities.

## 2026-08-27: adjoint moment kernel and rational invariant closure

The genuinely mixed extension now has an exact cohomological ledger. Its
cross class splits precisely for kernels in the image of
$(D-1)(D+q'/q-1)$, and split endpoint moments fill the full algebraic span
of $1,e,\pi$. A Hermite-type local residue completely detects
$(D-1)$-exact rational kernels. The first explicit zero-moment adjoint
kernel is split; one-simple-pole and all real constant-sign kernels have
strictly nonzero moments. For finitely many poles, the sole remaining issue is
an explicit algebraic relation among two polynomial core periods, a
Stieltjes transform and its derivatives, and $1,e,\pi$, with a separately
checkable nonzero local obstruction. Numerical PSLQ failures are archived
only as diagnostics.

The polynomial Bessel invariant theorem was strengthened locally to rational
first integrals. Polynomial Darboux multipliers cannot offset the primitive
transfer growth. Since the recurrence step is a polynomial automorphism,
unique factorization forces the numerator and denominator of any rational
first integral to share such a multiplier. Both must be constant. This
closes every rational invariant of the index and one recurrence state, while
leaving multi-state and nonlocal constructions untouched.

The centrally audited proofs, exact replays, and SHA-256 hashes are frozen in
`active_checkpoint_20260827.md`. Neither reduction supplies a numerical
connection-period independence theorem or the missing Bessel digit bound.

## 2026-08-27: all-parameter logistic endpoint normality

The last finite-rank uncertainty in the high-frequency root-of-unity branch
has been removed. Centering the confluent endpoint matrix reveals an exact
checkerboard decomposition. For even frequency count its nonzero blocks are
bi-moment matrices for a positive $\operatorname{sech}(\pi t)$ measure,
with polynomial systems in $t^2$ and $\tanh^2(\pi t)$. For odd frequency
count the corresponding positive measure contains $1/\sinh(\pi t)$, and
the second variable is $\coth^2(\pi t)$. Andreief's identity turns every
initial maximal minor needed for row rank into two Vandermonde determinants
of fixed strict sign. Consequently the endpoint rank is $D-1$ for all
parameters, with the exact parity defect predicted by the finite data.

The two-column correction has simultaneously been converted into an exact
Hermite-cardinal bordered-minor problem. Reflection reduces nonvanishing to
one constant or linear coefficient according to parity. This does not close
the branch: the rational cardinal row is outside the polynomial Chebyshev
system, and an exact entrywise-positive block already has a negative
nonconsecutive minor. Thus the remaining theorem is an augmented rational-
cardinal divided-difference sign statement, not generic total positivity.
The analytic proof and exact certificate were centrally audited and replayed;
their hashes are in the active checkpoint. No claim about $e+\pi$ follows
without that augmented determinant and the subsequent primitive-height
estimate.

## 2026-08-27: Laguerre squares, Euler transfer, and fixed-target gap

The positive common-kernel search produced a complete rational
parameterization for global squares in Laguerre coordinates. Primitive
integer clearing makes the endpoint value at least $n!$, while a rigorous
Bernstein--Walsh/Markov estimate supplies only exponential normalized decay.
Therefore a successful square family would need its rational output
numerator to absorb a factorial-square part of the endpoint coefficient.
Finite degree-three and degree-four searches show no such effect, but are not
used as an all-degree conclusion.

A separate fixed-target theorem is universal. If a nonnegative integer
common-kernel polynomial has fixed endpoint coefficient $a\ne0$, then its
exponential component is the positive number $ae-B$ with $B\in\mathbb Z$.
Its distance from zero is at least the fractional part of $ae$, and exact
primitive reduction can remove only a content divisor of $a$. Thus every
fixed-target positive family has a degree-independent primitive gap. The
case $a=2$ is bounded below by $e-5/2>5/24$. An infinite target-two
family confirms feasibility but has exponential mass exactly $2e$.

Finally, assuming algebraicity of $s=e+\pi$ transfers convergents $p/q$
of $e$ to algebraic exponents $i(s-p/q)$ of height $\log q+O_s(1)$,
for which the exponential misses $-1$ by order $q^{-2}$. The continued
fraction of $e$ beats every fixed lower-bound constant at the endpoint
exponent two. The strongest directly applicable uniform quantitative
Lindemann theorem has an exponent larger than $1266D$, and fixed-exponent
$E$-function measures are not uniform in the varying algebraic argument.
This route therefore requires a genuinely new exponent-two endpoint theorem.
All three audited packages and exact hashes are frozen in the active
checkpoint; none is a target classification.

## 2026-08-27: growing-target two-place synchronization

The only positive common-kernel regime left after the fixed-target gap has
an exact primitive decomposition. Its exponential and arctangent parts are
both positive after content removal, so a small form is equivalent to
simultaneous lower approximations to $e$ and $\pi$, together with one
explicit congruence modulo the cross-content. Euler's continued fraction
gives a universal lower bound of order
$D/(a^2\log a)$, and a Roth-breaking family would force an explicit
power-sized content excess.

That content excess cannot be excluded merely by requiring the input
polynomial to be primitive. A concrete zero-output direction added to a
positive target form gives primitive positive polynomials with target
$272m$ and output content $8m$ for every $m\ge17$. Exact reduction
collapses all of them to $34(e+\pi)-193$, however, so the example proves a
barrier rather than decay. A successful family must synchronize both
one-sided errors while changing its primitive output ray. The complete proof,
replay, and hashes are frozen in the active checkpoint.

## 2026-08-27: corrected two-column endpoint and primitive-height ledger

The two-column root-of-unity determinant has now been recalculated with its
endpoint derivative correction retained. With the convention
$W(F,G)=FG'-GF'$, the identity $g'(i\pi)=-1$ gives



$$
W(R_C,R_D)(i\pi)=
[W(C,D)-(C\beta_D-D\beta_C)](i\pi).
$$



Thus the polynomial relevant to the algebraicity comparison is
$\Delta=W-\Gamma$. Proving $\Gamma\ne0$ alone neither proves
$\Delta\ne0$ nor fixes its degree. This corrects the logical target of the
live augmented-cardinal branch.

The full interpolation map has an explicit all-parameter integer clearing
given by $2^{m(n+1)}$ times its confluent-Vandermonde determinant. After
saturating the endpoint kernel, every coefficient of the cleared corrected
polynomial is one exact integer contraction of the primitive Pluecker vector.
This separates three arithmetically independent quantities: bare Wronskian
content, correction content, and corrected content. In particular, exact
rows with correction contents $729$ and $128$ both have corrected content
one.

For a full-column-rank corrected coefficient map, the content of the image of
any primitive exterior vector divides the largest Smith invariant. No such
ambient cap exists in the rank-deficient range; decomposability and the
special complementary-minor endpoint locus are indispensable there. The
optimized Schwarz bound transfers twice the origin-order gain, but the
Wronskian coefficient height is quadratic, so the certified relative exponent
does not improve without exceptional corrected content, a degree/height
collapse, or analytic cancellation beyond Schwarz. All six exact diagnostic
rows remain below relative exponent two. The centrally audited proof, replay,
and updated hashes are in `active_checkpoint_20260827.md`. No target
classification follows.

## 2026-08-27: positive factor cone and changing high-content rays

The restricted cone $F=(1-x)^2H$, with nonnegative integer $H$ and the
common endpoint constraint $A(F)=F(\pm i)=a$, has been analyzed exactly.
For $\deg H\le7$, its unconstrained output image in the coordinates
$(a,B,4\int(F-a)/(1+x^2))$ is precisely
$4\mathbb Z\times\mathbb Z\times(1/210)\mathbb Z$. The divisibility
$4\mid a$ holds throughout this integer factor class, but no additional
degree-seven congruence couples the outputs.

An exact Bernstein interpolation construction realizes fourteen different
primitive positive rays by monic primitive nonnegative integer polynomials of
degree 66. Their positive forms decrease to
$1246188493618(e+\pi)-7302508153575$, rigorously between the two decimal
bounds recorded in the active checkpoint and of order $3.274\cdot10^{-13}$.
A positive zero-output direction permits enormous output cross-content without
destroying polynomial primitivity. An infinite congruence family supplies
changing primitive rays and arbitrary linear cross-content, but its values
grow. The finite construction therefore exposes real arithmetic flexibility
without assuming the missing infinite shrinking sequence. The proof and exact
replay are frozen in the active checkpoint.

## 2026-08-27: shifted root-of-unity minor and rational-cardinal reduction

The coordinate-row issue in the augmented endpoint determinant has an
all-parameter solution. After centering and deleting the constant derivative
column, the needed parity block retains full row rank. A finite
Polya-frequency factorization, strict monomial collocation, and Andreief's
identity give the proof without assuming total positivity of the full logistic
matrix.

The remaining border reduces exactly to a divided-difference determinant for
an explicit rational Hermite-cardinal function. Strict complete monotonicity
follows whenever its numerator is positive in an ordered repeated-node Newton
basis. Every coefficient is exactly positive for the full certified grid
$2\le m\le10,2\le n\le7$, including the parity-defect variants, but the
all-parameter Newton-positivity lemma remains unproved. A stronger pointwise
residue claim is false at $(m,n)=(8,3)$, so an eventual proof must retain the
integrated cancellations. Even universal correction nonvanishing would leave
the corrected-polynomial and primitive-height obstacles from the preceding
checkpoint. The audited proof, replay, and hashes are frozen in
`active_checkpoint_20260827.md`; no classification follows yet.

## 2026-08-27: exact universality and circularity of the positive factor cone

The full real factor-endpoint output cone is exactly the origin plus the open
half-plane $(e+\pi)a+c>0$. A strict positive order unit permits an algebraic
positive Hahn--Banach extension from the common plane. Bounded monotone moments
then force cancellation of the factorial endpoint term with the unique
coefficient $e$, and convergence across the four monomial residue classes
eliminates the remaining evaluation cycle at $i$. The dual cone is therefore
the single ray generated by $(e+\pi,1)$; bipolarity and the relative-interior
identity recover the exact open primal cone.

Rational approximation within a strict positive affine fiber proves more:
every primitive integer pair $(q,k)$ with $q(e+\pi)+k>0$ occurs as a fully
primitive output. Hence every rational lower approximant is realized, while an
infinite shrinking realized family exists if and only if $e+\pi$ is
irrational. This closes the cone-realizability branch by showing that its
remaining shrinking question is precisely the original unknown arithmetic
question. The proof was audited and its exact certificate replayed; hashes are
in the active checkpoint.

## 2026-08-27: universal positive pole truncation and correction nonvanishing

The remaining confluent-Newton lemma for the root-of-unity correction is now an
all-parameter theorem. For a genus-zero canonical product with increasing
positive zero rates, the finite Hermite remainder of an integral of a scaled
product power has strictly positive coefficients in the ordered repeated-rate
Newton basis whenever the pole multiplicity is the product exponent or one
larger. The proof uses a positive reciprocal-product cone, a sign-preserving
completion into ordered suffixes, continuity of finite Hermite projection, and
explicit positive branches through the infinite tail.

Cosine and sinc canonical products, with three elementary positive weights,
give exactly the two generic cardinal numerators and the parity-defect numerator.
Combined with the shifted-coordinate theorem, this proves $\Gamma\ne0$ for
all $m\ge2,n\ge D\ge2$. The result is stronger than the former finite grid,
but its boundary is sharp: it neither rules out cancellation in
$\Delta=W-\Gamma$ nor controls corrected primitive height or endpoint size.
The proof was audited and its 30-row rational replay and exhaustive finite
subproduct checks were rerun; hashes are frozen in the active checkpoint.

## 2026-08-27: top-cardinal degree theorem for the corrected determinant

The top Hermite-cardinal quotient has an exact centered simple-pole expansion
which is strictly completely monotone after one global sign. For even $n$,
all paired residues are positive. For odd $n$, explicit Newton coefficients
become positive Parseval integrals of centered binomial powers against elementary
nonnegative Fourier kernels. Negative real rootedness of the binomial-power
polynomials follows under Schur--Szego composition; its semigroup hypothesis
was checked against the primary published statement.

The resulting augmented checkerboard minor proves the top correction
coefficient nonzero exactly when parity permits. In every such regime,
$\deg\Delta=\deg\Gamma=n+D$, since the bare Wronskian stops at $2D-2$.
Parity forces the top coefficient to zero only when $n$ is even and $D$ is
odd, or when $m$ is even, $n$ is odd, and $D$ is even. The next
coefficient in those cases is an exact two-border sum; finite data are nonzero,
but opposite signs occur and no extrapolation is used. The audited proof,
primary-source check, deterministic replay, and hashes are frozen in the active
checkpoint.

## 2026-08-27: arithmetic of the positive cardinal Newton coefficients

The three cardinal numerators underlying the universal pole-truncation theorem
now have explicit rational local germs and an exact confluent-residue formula
for every ordered Newton coefficient. Their least denominators lie between a
local-jet lcm and an explicit confluent-Vandermonde multiple. In integer-rate
coordinates the primitive clearing content is one in the even generic and odd
defect families, and at most two in the odd generic family; positivity forces
primitive height at least the least denominator.

The even-family coordinate caveat is essential. Returning from the scaled
integer-square coordinate to the endpoint variable is non-unimodular. For a
degree-$d$ primitive numerator the induced content is a power of two bounded
by $2^{2d}$, and the exact row $(k,n)=(3,5)$ already produces $2^{32}$.
Thus the small-content theorem cannot be inserted into the corrected endpoint
threshold in the even case. In every parity the result concerns an isolated
cardinal numerator, not the saturated Pluecker contraction $W-\Gamma$; it is
therefore a denominator-height barrier rather than the missing transcendence
input. The proof, coordinate repair, exact replay, and final hashes are frozen
in the active checkpoint.

## 2026-08-27: corrected constant border for every even frequency count

For even $m=2k$, the corrected constant coefficient is the bordered minor
with rows $e_0$ and $e_1-E_0$. The latter has the exact centered
representative $U(N(-U^2)+2)$. Every ordered repeated-rate Newton coefficient
of $N$ has sign $(-1)^k$, and the first coefficient is exactly
$2(-1)^k$. The addition of two therefore leaves a nonzero nonnegative
reciprocal-suffix expansion after global sign normalization. Strict complete
monotonicity and the existing Andreief reduction prove $[z^0]\Delta\ne0$ for
every even $m\ge2$, $n\ge D\ge2$.

Together with the top-cardinal degree theorem, this leaves only odd $m\ge3$,
even $n$, and odd $D$ outside the universal corrected-nonvanishing theorem.
The same audit derives the exact defect row $2e_2-E_1$ and identifies the low
central jet which prevents a direct pole-truncation argument in the survivor.
This is an analytic nonvanishing advance; the decisive primitive content,
height, and endpoint-value comparison remains open. The proof, exact replay,
and hashes are frozen in the active checkpoint.

## 2026-08-27: corrected hard-family phase and the universal $D=3$ covariance theorem

The common-column reduction in the remaining odd-$m$, even-$n$, odd-$D$
family required a phase repair. For the natural positive Stieltjes
normalization $\rho_+$, direct substitution gives
$R(it)=-it\rho_+(t^2)$, not $+it\rho_+(t^2)$. Consequently



$$
V\sigma=V\psi-\mathcal E(V\rho_+),
$$



and the even and odd normalized bordered determinants have opposite
prefactors. The corrected target is



$$
\operatorname{NB}_A(V\psi)
 -\{\operatorname{NB}_A(\mathcal E(V\rho_+))
    -\operatorname{NB}_G(\mathcal E(V\rho_+))\}.
$$



For $D=3$, the two ordinary blocks have one row each. After probability
normalization, their density ratio is



$$
a(x)=h+1+2h\sum_{r=1}^k\frac{x}{x+r^2},
$$



which is strictly increasing, while
$q(x)=2\coth^2(\pi\sqrt x)-1$ is strictly decreasing. Exact bordered
determinant algebra factors the Euler-border difference as the border mass
times $\operatorname{Cov}(a,q)/\mathbb E(a)$. The positive natural Euler
row has positive mass, so its normalized difference is strictly negative.
The separate rational function
$\psi=\sum c_r/(x+r^2)$, $c_r>0$, is decreasing together with $q$, so
its border is a strictly positive covariance. These signs reinforce in the
corrected formula and prove $[z^{n+2}]\Gamma\ne0$ for every odd $m\ge3$,
even $n\ge4$, at $D=3$. Since the bare Wronskian has degree at most four,
the same coefficient of $\Delta$ is nonzero. This closes one infinite slice
of the final parity family but supplies neither the general $D\ge5$ result nor
the primitive-height estimate needed for a classification of $e+\pi$.

## 2026-08-27: all endpoint degrees for the three-frequency forced family

The corrected next-cardinal coefficient has now been proved nonzero for



$$
m=3,\qquad n\ge4\text{ even},\qquad
 D\ge3\text{ odd},\qquad D\le n.
$$



Writing $h=n+1$, $V=(1+x)^h$, $b=\mathcal E(V\rho)$, and using the
positive Stieltjes phase $R(it)=-it\rho(t^2)$, the original bordered
coefficient is a nonzero common factor times



$$
\operatorname{NB}_A(V\psi)
 -\{\operatorname{NB}_A(b)-\operatorname{NB}_G(b)\}.
$$



After division by $(1+x)^{h-2}$, the actual border depends affinely on
$c=2^{1-h}$. Its coefficient matrix is TN at $c=0$ and $c=1/2$ by
explicit block/selector factorizations; since the border occurs once, convexity
covers the whole interval. The csch derivative pairing is an exact reverse-TP
kernel, so column reversal gives a TN augmented moment matrix. Sylvester
condensation along a compatible terminal flag then proves
$\operatorname{NB}_A(b)\le\operatorname{NB}_G(b)$. The separate Cauchy
divided difference for $\psi=\gamma_h/(1+x)$ is strict and has exactly the
sign needed for $\operatorname{NB}_A(V\psi)>0$.

Consequently



$$
[z^{n+D-1}]\Gamma\ne0,
 \qquad \deg\Delta=n+D-1
$$



throughout this three-frequency family. Exact rational replay reconstructs the
raw cardinals and both original bordered determinants for every admissible
case with $n\le10$. This is a genuine all-parameter theorem, but only for
$m=3$; it neither proves the analogous one-border inequality at $m\ge5$
nor supplies the primitive-height estimate required to classify $e+\pi$.

## 2026-08-27: external-node Markov closure of the last forced family

The common-column phase audit first reduced the remaining odd-$m$, even-$n$,
odd-$D$ coefficient to



$$
\alpha\left\{\operatorname{NB}_A(V\psi)
 +\operatorname{NB}_G(\mathcal E(V\rho))
 -\operatorname{NB}_A(\mathcal E(V\rho))\right\},
 \qquad \alpha\ne0.
$$



Here $\psi$ is a strict positive Stieltjes sum, while $\rho$ is a positive
combination of $1/x$ and $1/(x+j^2)$. The sign error in the preliminary
normalization has been repaired: $R(it)=-it\rho(t^2)$, so the two parity
borders have opposite prefactors and the displayed terms reinforce.

The previously open Euler-border comparison is now an all-parameter theorem.
Let $p$ and $p_g$ be the monic degree-$d$ mixed biorthogonal polynomials
for $Vd\nu$ and $gVd\nu$, put $q=(1+2z\partial_z)p/(2d+1)$, and let
$r=q-p_g$. Orthogonality and the exact Euler adjoint give



$$
\int P(x)r(z(x))gV\,d\nu
 =-\frac{2h}{2d+1}\sum_{j=1}^k
   j^2J_jP(-j^2),
 \qquad J_j=\int\frac{p(z)V}{x+j^2}\,d\nu>0
$$



for every $\deg P<d$. If $R_{-b}(z)$ reproduces evaluation at the
external node $-b$, a generalized Andreief/Schur determinant proves



$$
\int\frac{R_{-b}(z(x))}{x+a}gV\,d\nu>0
 \qquad(a\ge0,b>0).
$$



The decisive sign is the elementary but nonlocal interpolation identity



$$
p_a(-b)=\frac{1-\prod_i(b+x_i)/(a+x_i)}{a-b}>0,
$$



with its positive continuous value at $a=b$. Moment uniqueness represents
$r$ as a negative sum of these reproducing kernels. Consequently, for every
central or noncentral divisor,



$$
\operatorname{NB}_A\!\left(\mathcal E\frac{V}{x+a}\right)
 <\operatorname{NB}_G\!\left(\mathcal E\frac{V}{x+a}\right).
$$



Positive linearity closes the actual cardinal row, proving



$$
[z^{n+D-1}]\Gamma\ne0,
 \qquad \deg\Delta=n+D-1
$$



for every odd $m\ge3$, even $n\ge4$, and odd $3\le D\le n$. Combined
with the earlier cases, $\Delta\ne0$ now holds throughout
$m\ge2,n\ge D\ge2$. This removes the last analytic cancellation problem,
but it does not control the primitive content or saturated height of
$W-\Gamma$, so it does not yet classify $e+\pi$.

## 2026-08-27: certified-coordinate cap for corrected primitive content

The complete nonvanishing theorem now supplies a coefficient that is known
nonzero in every parameter family, making a rank-independent content bound
possible. Put $N=q_E\Delta$, let $\mathfrak c_E=\operatorname{cont}(N)$,
and use the index set



$$
\mathcal I_{m,n,D}=
 \begin{cases}
  \{2D-1,\ldots,n+D\},&m\text{ odd},\\
  \{0\}\cup\{2D-1,\ldots,n+D\},&m\text{ even}.
 \end{cases}
$$



The parity-allowed top coefficient, the external-node next coefficient, and
the even-frequency constant coefficient prove that
$G_{\rm cert}=\gcd_{\ell\in\mathcal I}|N_\ell|$ is positive. Hence



$$
\mathfrak c_E\mid G_{\rm cert},\qquad
 H(N/\mathfrak c_E)\ge H(N)/G_{\rm cert}.
$$



This elementary divisibility becomes useful only because nonvanishing is now
all-parameter. It does not require the ambient corrected coefficient map to
have full rank. Moreover, with $A_K$ the cleared endpoint matrix,
$\delta_K$ its maximal-minor gcd, and
$\mathscr B_{a,b}=\det(A_K;e_a^T;E_b^*)$, the selected coordinates obey



$$
N_\ell=-\frac1{\delta_K}\sum_{a+b=\ell}\mathscr B_{a,b}
 \quad(\ell\ge2D-1),
 \qquad
 N_0=q_Ep_{01}-\frac{\mathscr B_{0,0}}{\delta_K}
 \quad(m\text{ even}).
$$



Thus the bound is expressed directly in saturated Pluecker coordinates, not
in an arbitrary rational nullspace basis. At the universal clearing $Q$,
$G_Q=(Q/q_E)G_{\rm cert}$ gives the necessary item-39 test



$$
(\kappa+1)\log G_Q>
 \kappa\log H(N_Q)+\log(C_0H_W)-2\mathcal G_1-\log Q.
$$



Failure rules out the current Schwarz/content implementation for that tuple;
success proves nothing because the cap can be loose. Exact rational examples
make the obstruction explicit. For $(m,n,D)=(3,5,4)$, the high-tail cap is
$729$ times the true content. For $(4,6,4)$, adding the certified constant
improves the overestimate from $93312$ to $128$, but it is still not exact.
Consequently the new theorem sharpens a necessary arithmetic certificate and a
primitive-height lower bound; it does not alter the unresolved asymptotic
exponent balance and does not classify $e+\pi$.

The exact replay checks nine tuples and all augmented-determinant identities,
content caps, height bounds, and clearing invariance. Its digest is
`5dbba748eb3a926c13da2dc16032008fa8f94fc020b169ae97f0a4a51b9714e0`;
the clean run used 81.207 MiB peak RSS. The frozen package is
`sources/root_unity_certified_coefficient_content_cap.md`,
`scripts/root_unity_certified_coefficient_content_cap_certificate.py`,
`results/root_unity_certified_coefficient_content_cap_certificate.json`, and
`results/root_unity_certified_coefficient_content_cap_hashes.sha256`.

## 2026-08-27: dyadic leading coefficient and the two-coefficient obstruction

On the infinite subfamily



$$
m=3,\qquad D=2,\qquad h=n+1=2^q,\qquad q\ge2,
$$



the saturated endpoint exterior vector is exactly $e_0\wedge e_2$. The top
cardinal gives an explicit odd integer $u_h$ with



$$
[z^{h+1}]\Delta=-\frac{u_h}{2^{h+q+1}(h-1)!},
 \qquad v_2([z^{h+1}]\Delta)=-2h.
$$



The valuation proof has a unique least term: only the logistic moment indexed
by $s=h$ reaches the minimal dyadic valuation. If $q_\Delta$ is the least
coefficient denominator and $\mathfrak c_\Delta$ the content after that
minimal clearing, then



$$
2^{2h}\mid q_\Delta,
 \mathfrak c_\Delta\mid N_h,
 2\nmid\mathfrak c_\Delta,
 \log|N_h|=O(h\log h).
$$



This excludes a hidden quadratic-size dyadic corrected content, but it does
not lower-bound primitive height: the primitive leading coefficient may still
be $\pm1$. A gcd theorem involving a second coefficient is the exact missing
arithmetic input. The deterministic finite replay covers $q=2,\ldots,6$ and
full corrected polynomials at $h=4,8,16$, with resident use below 0.2 GiB.
The proof, replay, and hashes are item 52 of the active checkpoint; no
classification of $e+\pi$ follows.

## 2026-08-27: corrected asymptotic capacity and its centered supersession

The corrected exterior construction now has a basis-free capacity ledger.
Universal endpoint and Wronskian majorants are linear in the primitive
saturated Pluecker height, and the exact leading content threshold is



$$
(\kappa+1)\chi>
 \kappa\log H(N_Q)+\log(C_0H_W)-2\mathcal G-\log Q,
 \qquad \kappa=r^2d+r-1.
$$



The same audit formulates the nondecomposable exterior regime:
$N=\binom\nu2>S=n+D-d$ permits rational tail elimination with
$\nu=O(\sqrt n)$, only $O(\sqrt n)$ loss of origin order, and a constant
Siegel exponent under fixed oversampling. It does not prove that the tail
kernel has nonzero low image, and the universal interpolation bound remains
$\exp\{mn^2\log n+O_m(n^2)\}$.

The uncentered analytic gain printed in this audit is superseded by the later
centered-frequency theorem. Every current use must substitute



$$
\mathcal G_{\rm ctr}
 =(L-n)\log\frac{2(L-n)}{e\pi m}-n\log\pi.
$$



The denominator, height, content, degree, Segre, and Siegel ledgers remain
valid after this replacement, and the centered theorem shows that the larger
gain still lies below $\log Q/2$. The exact replay used 16,512 KiB peak RSS.
The complete scope and hashes are item 53 of the active checkpoint; this is a
conditional capacity analysis, not a classification.

## 2026-08-27: parity--Segre collapse and rational-descent failure

For the full unconstrained endpoint space, reflection proves



$$
\beta_C(-z)+m\sigma C(z)=-\sigma\beta_C(z)
 \qquad(C(-z)=\sigma C(z)).
$$



Thus $\widehat\beta=\beta+(m/2)I$ reverses parity. When $n=2d$, an
odd/even pair is governed by a bilinear corrected map on
$\mathbb P^{d-1}\times\mathbb P^d$, whose dimension is $2d-1$ and degree
${2d-1\choose d-1}$. Degree collapse is therefore a rational hyperplane
section of a Segre variety, not merely a numerical optimization problem.

At $m=2$, the complete exact quadratic sections for $n=4,6,8$ have
closed-point degrees $1+2$, $4+6$, and $15+20$. The rational point at
$n=4$ does not persist to $n=6$. Allowing quartic output gives a rational
line at $n=6$ and a rational point on a component birational to a smooth
genus-six plane quintic at $n=8$, but the displayed primitive values at
$i\pi$ all exceed one. The deterministic chart/Gröbner replay took 21.751
seconds and peaked at 92.035 MiB RSS. These are exact finite classifications,
not an all-even-$n$ descent theorem; item 54 records the proof and hashes.

## 2026-08-27: centered-frequency Schwarz correction

Every exterior Wronskian sum has frequencies $0,\ldots,2m$. Multiplying by
$e^{-mz}$ relabels them as $-m,\ldots,m$, preserves coefficient height and
origin order, and changes the endpoint only by the rational sign $(-1)^m$.
The correct coarse type is therefore $m$, with stationary radius and gain



$$
\rho_{\rm ctr}=\frac{2(L-n)}m,
 \qquad
 \mathcal G_{\rm ctr}
 =(L-n)\log\frac{2(L-n)}{e\pi m}-n\log\pi.
$$



This improves the exterior negative logarithm by $2(L-n)\log2$. A separate
all-parameter argument nevertheless proves



$$
2\mathcal G_{\nu,{\rm ctr}}<\log Q_{m,n}
 \qquad(m\ge2, n\ge D\ge2, 2\le\nu\le D+1).
$$



Thus centering corrects every finite threshold but does not change the leading
$n\log n$ coefficient or rescue a content-free universal certificate. The
deterministic replay covers exact frequency algebra, 7,315 radius rows, and
8,265 denominator diagnostics; measured metadata are 1.604 seconds and 63.840
MiB peak RSS. Item 55 supersedes the earlier uncentered analytic formulas but
does not supply rank, content, or transcendence.

## 2026-08-27: centered exterior reflection and the surviving type

Parity eigenvectors satisfy the stronger raw remainder identity



$$
e^{mz}R_C(-z)=(-1)^m\sigma_CR_C(z).
$$



For a parity-homogeneous exterior vector, the centered sum obeys
$G_p(-z)=-\tau G_p(z)$, and its coefficients satisfy exact opposite-frequency
reciprocity. Same-parity blocks gain one uniform origin zero, with a gain of
three in the favorable single block. Pairing reciprocal frequencies into
$\cosh$ and $\sinh$ gives the refined circle factor



$$
D_m(R)=e^{mR}\frac{1-e^{-(2m+1)R}}{1-e^{-R}}.
$$



Because $D_m(R)\sim e^{mR}$, reflection does not lower exponential type
below $m$; it changes only finite prefactors and bounded origin order. The
38 exact monomial-pair rows retain both extreme frequencies and attain the
predicted minimal orders, while four parity-homogeneous sums have exact skew
rank four. The deterministic replay took 1.035404 seconds and peaked at
66.554688 MiB RSS. Item 56 freezes the all-parameter reciprocity and its exact
finite sharpness diagnostics; no classification follows.

## 2026-08-27: nondecomposable exterior sums and the exact rank-gap survivor

The corrected endpoint construction extends linearly from a single wedge to
every $p\in\bigwedge^2E_\nu$:



$$
\mathcal W_p(i\pi)=\Delta_p(i\pi),
 \qquad \operatorname{ord}_0\mathcal W_p\ge2L_\nu,
 \qquad L_\nu=m(n+1)+D+1-\nu.
$$



Killing all coefficients above degree $d$ produces a usable endpoint if and
only if



$$
\operatorname{rank}T_{\rm all}>\operatorname{rank}T_{>d}.
$$



The condition $\binom\nu2>n+D-d$ alone is false as a sufficiency claim. At
$(m,n,D,\nu,d)=(2,11,11,7,2)$, the full and tail ranks both equal 18; raising
$\nu$ to 8 restores the gap. Nor is universal parity-maximality available:
at $(m,n,D)=(2,21,7)$, the full rank is 26 rather than parity cap 27 and the
tail rank is 23 rather than 25, although the actual gap remains three.

Selected usable vectors have skew ranks 4, 6, or 8, proving that the
construction is genuinely outside the decomposable Pluecker-pair route. The
minimal full-endpoint basis has height one, but every certified centered
$r=1$ margin is negative, and the current remainder majorant still costs
$n^2\log n$ against only $n\log n$ analytic gain. Two deterministic final
replays were byte-identical; the larger measured peak was 929,576 KiB (about
907.8 MiB) RSS. Item 57 freezes the exact saturated-HNF grids, rank failures,
and hashes. The remaining requirements are an all-parameter weak rank-gap
theorem and intrinsic $O(n\log n)$-scale remainder/content control, not more
finite dimension counting; no classification of $e+\pi$ follows.

## 2026-08-27: endpoint-displacement square and product theorem

Checkpoint item 58 identifies an exact low-rank endpoint multiplication
displacement. For $m\ge2,n\ge m+1$, an explicit parity-block cofactor gives a
primitive polynomial $C_{m,n}$, of degree $m$ except degree $m-1$ when
$m$ is odd and $n$ is even, satisfying



$$
R_{zC_{m,n}}=zR_{C_{m,n}},\qquad
 W(R_{C_{m,n}},R_{zC_{m,n}})=R_{C_{m,n}}^2,
$$



and



$$
\Delta(C_{m,n},zC_{m,n})=C_{m,n}^2.
$$



The corrected endpoint is primitive of degree at most $2m$, and the
Wronskian has origin order at least $2m(n+1)$. The proof factors
$\beta_{zC}-z\beta_C$ through exactly $m$ logistic rows, so its rank is at
most $m$ for every parameter. Polarization on the kernel $U_D$ gives



$$
\Delta(C,zD)+\Delta(D,zC)=2CD,\qquad
 \dim(U_DU_D)\ge2D-2m-1,
$$



and hence an all-parameter nonzero corrected image of degree at most $2m$.
This is a genuine product-space rank-gap theorem, not a finite-rank
extrapolation.

The lower-parameter lift also cancels the universal two-copy clearing
exactly: the cleared square has endpoint content $Q_-^2$, leaving $R_C^2$
after intrinsic normalization. What remains open is the actual primitive
factor height. The proved cofactor/remainder majorants still cost too much,
and all fourteen exact $m=2,3$ sequence margins are negative. These finite
rows do not prove an asymptotic lower bound.

The frozen hashes are:

~~~
1883582877ed7f9b7fb6fdf7c99d66fa933bb9040f165cfdbab3bbcb2ca44e8b  sources/root_unity_endpoint_displacement_square_theorem.md
4bda9773163ec63cd4df868d1f0032cade310ea1525952540b1806aef214cb25  scripts/root_unity_endpoint_displacement_square_certificate.py
68be9373f11cef9a734a18412b091f4ec555c6aed582301e41c777dc9acd885a  results/root_unity_endpoint_displacement_square_certificate.json
84d6549d8293ddd022ff875b2bae47921b1db547a64b15606b1528e26d30d964  results/root_unity_endpoint_displacement_square_hashes.sha256
~~~

The deterministic replay checks six structural and fourteen sequence rows.
The conservative final run took about 31.5 seconds and reported 971,304 KiB
(about 948.54 MiB) peak RSS, below 2 GiB. Item 58 proves the square/product
theorem but does not classify $e+\pi$.

## 2026-08-27: third exterior endpoint jet and cube-root dimension gain

Checkpoint item 59 treats arbitrary
$p\in\bigwedge^3E_\nu$, rather than a canonical or decomposable
$3\times3$ Wronskian. At $z=i\pi$, direct differentiation gives



$$
R_C=C,\qquad R_C'=C'-\beta_C,\qquad
 R_C''=C''-\beta_C-2\theta_C,
$$



so



$$
\Delta^{(3)}
  =\det(\mathbf C,\mathbf C'-\boldsymbol\beta,
        \mathbf C''-\boldsymbol\beta-2\boldsymbol\theta)
$$



is the exact corrected endpoint map. The resulting analytic sum has endpoint
$\Delta^{(3)}_p(i\pi)$, origin order at least $3L_\nu$, raw frequencies
$0,\ldots,3m$, polynomial degree at most $3n$, and centered type $3m/2$.

The high-tail problem has domain size ${\nu\choose3}$ and
$2n+D-d$ rows, so fixed oversampling permits
$\nu=\Theta(n^{1/3})$. This cube-root gain is exact, but dimension counting
still does not prove a usable endpoint: the full corrected rank must strictly
exceed the tail rank, and no all-parameter rank-gap theorem is known.

The normalization audit explains why the extra analytic copy does not close
the arithmetic ledger:



$$
Q^2\Delta^{(3)}_p\in\mathbb Z[z],\qquad
 \overline{\mathcal W}^{(3)}_p=Q^3\mathcal W^{(3)}_p.
$$



After primitive endpoint normalization, two copies of $Q$ remain in the
proved analytic-height majorant. The centered gain triples, but the matched
multilinear height and algebraic-height costs also triple, leaving the same
per-column threshold as $k=2$. The four exact rank-gap-three rows are
diagnostics only.

The frozen hashes are:

~~~
6f0b2d7908da9f6b67135468e5e8744bbd9f1785963361dcd21a8d8e0923a281  sources/root_unity_third_exterior_sum_endpoint_audit.md
94623603b6bbe14dbdd736e04c595408d3af28dd1db71d31aa17f8178c64faac  scripts/root_unity_third_exterior_sum_certificate.py
3d09b003816d84ba655e2de8f497494e6115e15bb995c93da2975cf0a07b370c  results/root_unity_third_exterior_sum_certificate.json
16f8e44aa10be4345aae9de08b3c179d9ec381f30c8f9194d0faa6f709eb0492  results/root_unity_third_exterior_sum_hashes.sha256
~~~

The deterministic replay took 8.574 seconds and used 70.887 MiB peak RSS.
Item 59 proves the endpoint, support, order, normalization, and capacity
statements; its finite rank rows are not extrapolated, and it does not classify
$e+\pi$.

## 2026-08-27: intrinsic saturation of the global $k=2$ image

Checkpoint item 60 separates presentation size from the intrinsic global
Wronskian lattice. For a full-row-rank raw basis $R$, a transformed tall HNF



$$
UR^t=\begin{pmatrix}H_0\\0\end{pmatrix}
$$



gives the saturated basis and exact index



$$
S=(U^{-1}_{[:,0:r]})^t,\qquad
 R=H_0^tS,\qquad
 [L_{\rm sat}:L_{\rm raw}]=|\det H_0|.
$$



The index is also the product of the nonzero Smith invariants, the gcd of all
maximal minors, and the raw-to-saturated covolume ratio. If $g$ is the common
entry content, then



$$
[L_{\rm sat}:L_{\rm raw}]=g^rI_{\rm cross}.
$$



This proves exactly why a universal scalar clearing can make exterior
coordinates and raw global vectors enormous without forcing the same
primitive global height. The compatibility
$\mathcal E(Gx)=Q\,Nx$ also verifies that rational saturation preserves all
killed endpoint-tail coefficients.

On the ten representative rows with $m=2,3$ and
$n=2,3,5,8,10$, the repeated common scalar accounts for at least
$96.3970\%$ of the logarithmic index. Saturated LLL row scales are consistent
with $O(n\log n)$, while raw scales are much larger. This is finite evidence
only: there is no all-parameter Smith or Pluecker-height bound, LLL is not SVP,
and a short global vector can have zero corrected low endpoint.

The frozen hashes are:

~~~
cc56e51aa5ce1f7f1dadb2c10edf96fbdacadb2ca660f20130f2b57dec4f13ab  sources/root_unity_k2_global_image_saturation_audit.md
588393ba1cb273d13034cc069cca7b3f507c8b9adf62f13a8d6e8e71bb15d470  scripts/root_unity_k2_global_image_saturation_certificate.py
b66a378153646894f7bc923892f8ee50bb2dc8a665a56030a545d6d0488f1c92  results/root_unity_k2_global_image_saturation_certificate.json
72f63950f3e197f921bb256e84f6938fb7713a253183bf46e83a381cd2942e4f  results/root_unity_k2_global_image_saturation_hashes.sha256
~~~

The manifest additionally verifies the frozen item-57 dependency hash
3056828b21e08759fd7520c169db074aa9250c4e8bf4c8b6357c460881c3dd5f.
Two clean replays produced byte-identical JSON; the conservative run took
32.004 seconds and peaked at 240.594 MiB RSS. Item 60 proves the lattice
identities, not the observed growth law, and does not classify $e+\pi$.

## 2026-08-27: Gaussian parity mixing reaches only the Dirichlet boundary

Checkpoint item 61 combines the even and odd corrected endpoint blocks with an
exact Gaussian phase. For
$\widetilde N=N_{\rm e}-iN_{\rm o}$, coefficientwise sign rotation gives an
ordinary integer polynomial $A$ such that



$$
\widetilde N(z)=A(-iz),\qquad
 \widetilde N(i\pi)=A(\pi).
$$



The Gaussian coefficient ideal is exactly the ordinary integer gcd ideal, and
the Gaussian house is the ordinary coefficient height. Mixing therefore
creates no content bonus; the joint content is the gcd of the two block
contents. The analytic combination changes coefficient house by at most
$\sqrt2$ and does not alter centered exponential type or Schwarz gain.

If $e+\pi$ is temporarily assumed algebraic of degree $r$, direct norm
descent leaves the fixed-degree absolute measure cost
$r^2d+r-1$ and strict relative threshold $r^2d+r$. An exact rank-$t$
Dirichlet lemma supplies only



$$
|A(\pi)|\ll H(A)^{1-t},\qquad
 |A(\pi)|/H(A)\ll H(A)^{-t}.
$$



At full rank $t=d+1$, this merely meets the threshold when $r=1$, without
the strict gain needed for contradiction, and falls below it when $r>1$.
Thus parity mixing and rank alone cannot close the measure comparison.

The 26 exact replay rows show genuine finite joint-rank enlargement and
primitive vectors using every degree and both parities. Their ranks, bounded
searches, and decimal endpoint values are diagnostics, not an all-parameter
theorem.

The frozen hashes are:

~~~
fbfb6fba663768b80364462608d0267d233d1828924b9d25f12dd9a7a1ea4b6d  sources/root_unity_gaussian_parity_mixing_barrier.md
a338633131005b021bd8acd0a1edf9ca69fa21fc2af2ae2f0ba517be1e843143  scripts/root_unity_gaussian_parity_mixing_certificate.py
70a4df592056f424a481ca6da7a8d6b6c803f43d8c59c8103a24b5f3a0317c02  results/root_unity_gaussian_parity_mixing_certificate.json
74c2d5fab03af9520d7f7cb480c6ce3fd490ce2b26a0769c337672605d4eb280  results/root_unity_gaussian_parity_mixing_hashes.sha256
~~~

The script verifies the frozen item-57 dependency before import. Its final
replay took 1.122126 seconds and reported 73,280 KiB (71.5625 MiB) peak RSS.
Item 61 proves the phase/content and measure/Dirichlet barriers, not a
classification of $e+\pi$.

Items 58--61 have now been integrated into the active checkpoint and README.
All four frozen manifests were reverified before the central update. These
packages add exact construction and obstruction theorems plus explicitly
delimited finite diagnostics; none proves that $e+\pi$ is rational,
irrational, algebraic, or transcendental.

## 2026-08-27: fixed quadratic survivor with uniform intrinsic scale

Checkpoint item 62 closes the previously missing all-parameter low-degree
rank-gap and global-scale steps in one concrete $m=2$ family. With



$$
E_0=B-Az^2,\qquad E_1=C-Az^4,\qquad O=g_3z-g_1z^3,
$$



the exact product/exterior combination



$$
(2Ag_1g_3-Bg_1^2)E_0^2-Ag_1^2E_0E_1+A^3O^2
 =p_0+p_2z^2
$$



has $p_0p_2>0$ for every $n\ge5$. Its global image has order at least
$4n+4$, frequencies $0,\ldots,4$, and degree at most $2n-2$. The
strict signs follow from a hyperbolic-secant probability model, reversed
covariance, monotonicity of $I_5/I_3$, and an exact $n=5$ Fourier anchor.

The explicit clearing



$$
q_n^2D_n^5\mathscr F_n,qquad
 D_n=2^{2n+3},\quad q_n=2^{2n}(n-1)!,
$$



is integral and has logarithmic height at most $16n\log n+O(n)$. Thus a
nonzero fixed-degree survivor with the desired $O(n\log n)$ intrinsic scale
is now a theorem, not an LLL extrapolation. The leading constants still fail:
if $\chi_n$ is normalized exact endpoint content, endpoint and analytic
height constants are $10-\chi_n$ and $14-\chi_n$, while centered gain is
only $2$. Even maximal content allowed by the proof leaves a deficit of
$2n\log n$.

Frozen hashes:

~~~
47045420f729a14eb7eaf655988add44332db26091b837a9d24dfaed7d39c868  sources/root_unity_m2_quadratic_saturated_survivor_theorem.md
1ec66622c212bb27d7729e1b9e2d7519d355bbe755f40b239343172926b8a7fe  scripts/root_unity_m2_quadratic_saturated_survivor_certificate.py
9a44bea7db63f8f994a01bcaf284a9319f05050bc28c84c7c71fb889ee483274  results/root_unity_m2_quadratic_saturated_survivor_certificate.json
d5faaf65094d19b9a20fd178ee35de76a0fb37b8aa6399c8ec76491c87967880  results/root_unity_m2_quadratic_saturated_survivor_hashes.sha256
~~~

The 16-row deterministic replay took about 9.15 seconds and 78,632 KiB RSS.
Item 62 proves the construction and its current barrier, not a classification.

## 2026-08-27: aligned Gaussian saturation has index one

Checkpoint item 63 distinguishes the real unphased glue from the phase-aligned
Gaussian lattice. For separately saturated reflection eigenspaces,



$$
S_++S_-\subseteq S_0,\qquad2S_0\subseteq S_++S_-,
$$



so the unphased quotient is $2$-elementary. But if
$\sigma(w)=J\overline w$, then



$$
\boxed{S_{\mathbb G}^{\sigma=1}=S_+\oplus iS_-}
$$



exactly, with saturation index one after real doubling. Clearing a glued
half-vector by $1+i$ merely gives the same primitive analytic form as
separate doubling once endpoint content is divided out.

For every rigorous coefficientwise centered circle bound considered, a mixed
vector $u-iv$ is pointwise no smaller than either component, while joint
content is the gcd and joint height/degree cannot decrease. Hence its optimized
measure margin cannot beat the better parity block. The theorem does not cover
interference between distinct coefficient pairs or exceptional successive
minima inside one block.

Frozen hashes:

~~~
08c282e9ebd933b8b4def6806f9d6db1fb13e445c6b9ce1f6d57690c92162b9a  sources/root_unity_gaussian_global_saturation_no_gain.md
89004cd7c35e890803f486f3a69036d21980497c718b75ad78be4441335e4f5a  scripts/root_unity_gaussian_global_saturation_certificate.py
607cf35c54cf16f6da870b0b933c217388b8eb551132e07a8500ae95f0a78837  results/root_unity_gaussian_global_saturation_certificate.json
49d4d2e40a9cb421be3f409ca94129c487b5de3c685e8fe88fe6c39dd7fabbb7  results/root_unity_gaussian_global_saturation_hashes.sha256
~~~

The 12-row final replay took 60.242294 seconds and peaked at 999.941406 MiB.
Item 63 is a no-gain theorem for the stated majorants, not for all analytic
norms or all lattice directions.

## 2026-08-27: Hardy norm replaces the coefficientwise circle bound

Checkpoint item 64 derives the branch-free exact Gram identity



$$
\langle z^ae^{rz},z^be^{sz}\rangle_R
 =\sum_{\ell\ge\max(a,b)}
 {R^{2\ell}r^{\ell-a}s^{\ell-b}\over(\ell-a)!(\ell-b)!}
$$



and the zero-factored Hardy evaluation bound



$$
|F(i\pi)|\le
 {\pi^K\|F/z^K\|_{2,R}\over\sqrt{1-\pi^2/R^2}}.
$$



On the affine endpoint fiber $B^tx=p$, the exact real minimum is
$p^t(B^tA^{-1}B)^{-1}p$. Rational points have the same infimum by density,
but their denominators are uncontrolled; this is the remaining arithmetic
gap in this continuous optimization.

For saturated $m=2,d=2$ rows at $n=5,8,10$, the Hardy upper bounds improve
the coefficientwise bounds for the same functions by 15.48, 30.13, and 36.05
log units. The $n=8$ bound is already below one in absolute value, yet the
relative exponent is only $1.21038<3$. These high-precision values are
finite diagnostics, consistent with an $O(n)$ saving and not proof of a
changed $n\log n$ constant.

Frozen hashes:

~~~
24bc6c1e633118bec00659ed625d52266079555559c567e123d5d55943bc8a81  sources/root_unity_hardy_h2_saturated_circle_audit.md
8cd98734331b75ea26990759c5d13a8d022065340feb1ef5cea4871452912b6b  scripts/root_unity_hardy_h2_saturated_circle_certificate.py
a14b1af4b11b6760839b9237eaeb854156be6cc4588ffc83f656d9ed97347db2  results/root_unity_hardy_h2_saturated_circle_certificate.json
f5d80a9962ed914662be782301319b7d786aa6874510b876a5d24a54d9f3cbd4  results/root_unity_hardy_h2_saturated_circle_hashes.sha256
~~~

Two deterministic post-edit replays matched byte-for-byte. The final run took
45.85 seconds and 1012.97 MiB RSS. Items 62--64 have now been integrated into
the active checkpoint and README after independent manifest verification.
They materially sharpen the surviving route but do not classify $e+\pi$.

## 2026-08-27: exact quotient LP and the clearing-denominator obstruction

Checkpoint item 65 puts the fixed-endpoint coefficientwise optimization on
an exact footing. If $E$ is the rational endpoint map, $\Lambda$ a
rational right inverse, and the rows of $K$ a rational basis of $\ker E$,
then every normalized fixed-endpoint global vector is $b+tK$. Consequently
the best weighted-$\ell^1$ circle majorant is a finite rational linear
program. Rational points have the same infimum as real points by density,
but density neither bounds denominators nor certifies a proposed optimum.

The exact $(m,n,D,d,R)=(2,8,7,2,13)$ replay found a rank-$11$ saturated
image and rank-$8$ endpoint-zero kernel. It also caught a substantive error
in the temporary numerical probe: a kernel direction has exact one-sided
derivative



$$
-{39710900240730900314101\over17036837675827200}<0,
$$



so the alleged optimum admits an explicit rational descent. The improved
point is recorded only as feasible. Its bound has
$\log B=15.8874542397205888\ldots$ and degree-two measure margin
$-60.72193402085388\ldots$, hence is nowhere near sufficient.

After clearing denominators, the two audited global representatives have
primitive endpoint multipliers $6518378303365776642144000$ and
$645319452033211887572256000$; both global coefficient vectors have
content one. This rigorously exhibits, in one finite fiber, how a cheap
rational quotient direction can acquire an enormous integral clearing cost.
It is not a universal denominator lower bound. Item 69 later proves that
this clearing cost is irrelevant to endpoint-only homogeneous analytic
quotient arguments and corrects the earlier obstruction interpretation.

Frozen hashes:

~~~
070aa86143f9970c7925a07377fe1ff8f795992c8057e98505c6fc137f83f5e9  sources/root_unity_k2_exact_quotient_lp_audit.md
1f9ef63de854211c31bde2575cdc20d2271aae33e59f45d8810099c94af84a6c  scripts/root_unity_k2_exact_quotient_lp_certificate.py
a0e2a8d3d3c5db6904c713913ab5a441d72785931cb4e62c77fe7bfdae9fac1a  results/root_unity_k2_exact_quotient_lp_certificate.json
cebc31286ee464728467d9584ef729c667111cb2b69e1f6f9bb10ed5488065a4  results/root_unity_k2_exact_quotient_lp_hashes.sha256
~~~

The manifest and payloads were independently reverified after repairing two
source control characters. The deterministic replay took 27.12 seconds and
peaked at 1081.72 MiB RSS. Item 65 supplies neither irrationality nor
transcendence of $e+\pi$.

## 2026-08-27: centered-cosh lower lift and product survivor

Checkpoint item 66 proves



$$
P_n[zC]-zP_n[C]=[z^n](C/(2\cosh z))z^{n+1}.
$$



On the kernel of that coefficient functional, multiplication lifts exactly,
and $W(R_n[C],R_n[zC])=R_n[C]^2$. Polarization realizes rational symmetric
products as exterior sums with ordinary product endpoints. If $t+1$
consecutive tail jets vanish, a dimension argument unconditionally supplies a
nonzero endpoint of degree at most $2t+2$.

The exact $D=n-1,d=2$ grid through $n=20$ displays the stronger finite
quadratic pattern $t=\lfloor(n-1)/3\rfloor$, but no all-parameter rank gap
is inferred. At its proposed scaling the centered gain is $2/3$, the
optimistic Siegel height constant is $5/3$, and the ledger still requires
content $\chi>13/9$. A structured low-image quotient/Smith theorem remains
missing.

Frozen hashes:

~~~
8794eaeb7a8cf5f0c7e749c85afc67b2403b3dc6e3e752353bbf0ab020059581  sources/centered_cosh_lower_lift_product_audit.md
da827921d2621821553ed8bee069428638539fa5bb6b952c4636782d2b5aef71  scripts/centered_cosh_lower_lift_product_certificate.py
f3425385637efaa329f67a133c89844ac8a2a3a92603838ffe0e92c8ca1844bf  results/centered_cosh_lower_lift_product_certificate.json
51e0523cf8ce702885deb20d703ddd615cc15e645fe96fba2c35ce0c2ec54a92  results/centered_cosh_lower_lift_product_hashes.sha256
~~~

The deterministic replay took 7.22 seconds and about 91,680 KiB RSS. This is
a construction theorem, not a classification.

## 2026-08-27: antipodal Gaussian whole-circle no-gain

Checkpoint item 67 upgrades the earlier coefficientwise Gaussian barrier to
the exact whole function. For opposite reflection parities and $W=U-iV$,



$$
|W(z)|^2+|W(-z)|^2=2(|U(z)|^2+|V(z)|^2).
$$



Every centered-circle supremum of $W$ therefore dominates both components,
and the Hardy norms add in squares. The result survives division by an origin
zero of either parity. Unequal component orders add a factor
$(R/\pi)^\delta\ge1$, strengthening the comparison. Joint-content gcd and
height/degree domination then prove that cross-parity Gaussian mixing cannot
improve the optimized exact supremum or Hardy measure margin.

Frozen hashes:

~~~
6e979114a2d4a043e41fe6dcf6031d3c98eb86c434b3c8825c3b8aa1589ba412  sources/root_unity_gaussian_antipodal_no_gain_theorem.md
880e284b923fbeb911509bc2970d79b37434781d7eb002454408294661d81d79  scripts/root_unity_gaussian_antipodal_no_gain_certificate.py
1fa52598c244019d9892255d54deccbeb56ef0ed86b9d7c6496c2647049ebe8f  results/root_unity_gaussian_antipodal_no_gain_certificate.json
e6df57e7016a60e0154fba90a849ec34d707d691135d8bc04142c06a2abca15c  results/root_unity_gaussian_antipodal_no_gain_hashes.sha256
~~~

An independent replay took 1.16 seconds and about 71.5 MiB process RSS. Item
67 closes cross-parity whole-circle interference, but leaves the hard
single-parity quotient and endpoint arithmetic untouched.

## 2026-08-27: closer-root sech--Padé normality and clearing theorem

Checkpoint item 68 proves that the centered closer-root construction
$R=C+2\cosh zP$ is normal for every $n,D$. Its endpoint, after parity
reduction, is the $[N/K]$ Padé denominator of
$1/(2\cosh\sqrt x)$. Rectangular Schur-minor positivity proves the exact
degree and first omitted coefficient.

For fixed $K$, an exact discrete-pole Heine formula gives relative endpoint
$c_K(2K+1)^{-2N}(1+O_K(\rho_K^N))$. The quadratic case reduces to two
Euler numbers, one gcd, and the exact beta quotient. On $K=N$, Dzyadyk's
asymptotic gives $4N\log N+O(N)$ relative gain. A new local theorem using
Catalan Hankel determinants proves that mandatory endpoint clearing is
primitive and has height at least $16^N$, leaving exponent only
$O(\log N)$ against degree $2N+O(1)$. Dilation by an integral frequency
is projectively neutral; the centered/sech construction instead occupies the
half-frequency class.

Frozen hashes:

~~~
f837e5be64de4985e721f9e5d3731e6d13e01c41fa973a937c4bc1dce0977ecf  sources/root_unity_closer_root_sech_pade_audit.md
8a97f86cc74314ead643e34a8ccc7d1d7bd0c2502122c3da1143862d686c64b6  scripts/root_unity_closer_root_sech_pade_certificate.py
f16f21e3ebf0a52b66a201f29ebe6875e0b094c65077b0e800ce14278d7bba5e  results/root_unity_closer_root_sech_pade_certificate.json
53d611d1478c66290b05a683d9eb7ff3936f88228cc45bac36628b3019f7d117  results/root_unity_closer_root_sech_pade_hashes.sha256
~~~

The independent replay took 4.30 seconds and 73,560 KiB RSS. Item 68 is a
normality, asymptotic, and arithmetic-clearing theorem, not a classification.

## 2026-08-27: denominator-free endpoint quotients and Dirichlet boundary

Checkpoint item 69 corrects the interpretation of the finite item-65
clearing multipliers. The common zero and endpoint identity are exact
complex-linear constraints. Therefore the real Hardy minimizer in a
primitive endpoint fiber is a legitimate auxiliary entire function, and
rational points in the same exact fiber approach it. Neither Hardy nor the
homogeneous weighted-$\ell^1$ Schwarz quotient charges the denominators of
that representative; the conditional lower bound sees only the primitive
integer endpoint polynomial. Integral clearing remains relevant only to a
different argument that independently requires global integrality.

In coordinates $u=p_0-\pi^2p_2$, $v=p_2$, the exact binary quotient is



$$
Q_R/a=(u+\eta v)^2+\tau v^2.
$$



Consequently its normalized value differs from
$|\pi^2-p_0/p_2|$ by at most the collapse floor
$\varepsilon=\sqrt{\eta^2+\tau}$. Primitive endpoint optimization is thus
equivalent, up to $\varepsilon$, to rational approximation of $\pi^2$.
The continued-fraction balance gives exponent two; excluding rational
$e+\pi$ through a degree-two $e$-measure needs exponent strictly above
three. Positive definiteness and projective collapse alone cannot supply
that missing power.

The exact $n=5,8,10,12$ diagnostics exhibit collapse floors squared down
to $5.18\,10^{-44}$, without an asymptotic claim. The separately saved
$n=14,D=7$ row has a Hardy bound within $0.128$ log units of the actual
endpoint, but relative exponent only $1.27936<3$.

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

The main replay was byte-identical twice, took about 118.5 seconds, and
used at most about 461 MiB in polling. Item 69 removes a false denominator
barrier but supplies no irrationality or transcendence conclusion.

## 2026-08-27: all-parameter centered-cosh Pade ideal recurrence

Checkpoint item 70 proves an exact ideal theorem for the balanced product
spaces behind item 66. If $Q_q$ is the diagonal $[q/q]$ denominator for
$F(x)=1/(2\cosh\sqrt x)$, then



$$
Q_q\mathbb Q[x]_{\le2q}\subseteq{\cal E}_{q,1}\quad(q\ge2),
 \qquad
 xQ_q\mathbb Q[x]_{\le2q}\subseteq{\cal E}_{q,2}\quad(q\ge1).
$$



The proof is not a rank-pattern extrapolation. It splits each constrained
parity block by Pade division, passes to $\mathbb Q[x]/(Q_q)$, and proves
the needed controllability using a strictly positive rectangular Schur
minor. Duality supplies the corresponding finite recurrence for every
annihilator. The small case $(q,r)=(1,1)$ is an exact exception:
${\cal E}_{1,1}=Q_1^2\mathbb Q[x]_{\le1}$.

The result reduces the recurrence-certificate scale to the Pade cofactor
scale $O(q^2\log q)$, but it proves neither the finite-grid
codimension-one pattern nor quotient saturation nor a small primitive
quadratic survivor. Those missing quotient/Smith bounds are essential and
remain under investigation.

Frozen hashes:

~~~
a4e1fa3f9562f876bc5dafec817373238298d6565ad34c291f0a3a70513cad84  sources/centered_cosh_pade_ideal_recurrence_theorem.md
f20223fb9bb9f524db7532c1fe1f8aad22b6e01245564d4b55b3ddf6795e1a20  scripts/centered_cosh_pade_ideal_recurrence_certificate.py
a6a99505f1cef3c1499be9a331cf452c76c1fc7f7d9f0b66b1e6baf56efaa48d  results/centered_cosh_pade_ideal_recurrence_certificate.json
ef1345491b9747c118e1e8a9c1a5c34160923bfe6fdea8a2aed9e4b5dd0a7c1c  results/centered_cosh_pade_ideal_recurrence_hashes.sha256
~~~

The manifest and hashes were independently checked. A fresh exact replay took
0.99 seconds and about 68,616 KiB RSS. This theorem narrows the remaining
arithmetic bottleneck but supplies no classification of $e+\pi$.

## 2026-08-27: Kummer-period decomposition of the quadratic Euler gcd

Checkpoint item 71 separates the easy index factor from the genuinely
uncontrolled common Euler content. With



$$
A_N=(2N+2)(2N+1),\quad
 H_N=\gcd(|E_{2N}|,|E_{2N+2}|),\quad
 G_N=\gcd(A_N|E_{2N}|,|E_{2N+2}|),
$$



one has exactly



$$
G_N=H_N\gcd\left(A_N,{|E_{2N+2}|\over H_N}\right),
 \qquad H_N\mid G_N\mid A_NH_N.
$$



Split $H_N=S_NJ_N$ at the largest prime-power depth whose Euler--Kummer
period fits below $2N+2$. The unit-multiplier prime-power congruence proves



$$
S_N\mid\operatorname {lcm}(1,\ldots,3N+3),\qquad
 \log G_N=\log J_N+O(N).
$$



Every layer in $J_N$ is, and every excess layer arises from, simultaneous
divisibility of the adjacent pair $E_{2N},E_{2N+2}$ before its first
prime-power period. Therefore



$$
\log G_N=o(N\log N)\iff\log J_N=o(N\log N).
$$



This proves that the visible recurring $149$ and $241$ factors are
absorbed into the lcm-sized part. It also gives the exact height ledger



$$
\log H(\mathscr C_N)=2N\log N-\log J_N+O(N).
$$



The missing statement is now a quantitative adjacent first-period
Euler-irregularity bound. A direct centered Euler-polynomial resultant has
only an $O(N^2\log N)$ Hadamard bound and therefore does not solve it.

Frozen hashes:

~~~
a720ef166a3b772d85c32934782fcfa4d41797b274ea964259973a216bb369ca  sources/root_unity_quadratic_euler_gcd_kummer_obstruction.md
5685471a82b294cd77b60d3079067274f23e14f30e3317f2373c87ffcb2770d4  scripts/root_unity_quadratic_euler_gcd_kummer_certificate.py
89521c6ec34e3ff7c75d7845ab22de10562814a3cbe8d256bbd7769a9e2cb53d  results/root_unity_quadratic_euler_gcd_kummer_certificate.json
74b79cee3b86e5fe37700e1db68ed91976a56c01a783c1e10d5e13651d82ba49  results/root_unity_quadratic_euler_gcd_kummer_hashes.sha256
~~~

The cited prime-power congruence was checked against the primary paper. The
package then passed manifest, byte, syntax, and deterministic replay checks;
the fresh run took 5.88 seconds and about 75 MiB RSS. Item 71 supplies no
classification of $e+\pi$.

## 2026-08-27: all-degree endpoint collapse and the exact Dirichlet boundary

Checkpoint item 72 generalizes the binary quotient geometry to every fixed
endpoint degree. For a positive quotient form, the coordinates
$u=A_p(\pi)$ and $v=(p_1,\ldots,p_d)$ give



$$
{Q_n(p)\over a_n}=(u+\eta_n^tv)^2+v^t{\cal T}_nv,
$$



with an exact bound



$$
\left|\sqrt{Q_n(p)/a_n}-|A_p(\pi)|\right|
 \le\varepsilon_n\|v\|_\infty.
$$



Thus primitive minima up to nonconstant height $H$ differ by at most
$\varepsilon_nH$. To preserve an absolute exponent $\mu$, the required
condition is $\varepsilon_nH_n=o(H_n^{-\mu})$, not merely
$\varepsilon_n\to0$.

Geometry of numbers gives aligned absolute exponent $d$ from $d+1$
integer coefficients, and the norm of $2^{1/(d+1)}$ proves that this is
sharp as a dimension-only principle. Hypothetical algebraicity degree $r$
for $e+\pi$ gives conditional threshold $r^2d+r-1$. Ordinary Dirichlet
only equals the rational-case threshold and never strictly beats it.

The Gaussian polynomial $A_p(-iz)$ phase-aligns all monomials at $i\pi$
without changing height, content, or degree. In contrast, ordinary real
coefficients split into orthogonal even and odd blocks and have exponent only
$\lfloor d/2\rfloor$. Their actual degree after $\pi=s-e$ remains the
full parity degree, so the conditional measure cost is not halved.

Frozen hashes:

~~~
6201f479c27e16afe4fdf515e24d860c0c360ea0be29c31d12feb97da0831687  sources/root_unity_hardy_all_degree_endpoint_collapse_theorem.md
e29f72af7515d0cf65bab00f65019de6d0ac366e96290c84a26f300bc070eeca  scripts/root_unity_hardy_all_degree_endpoint_collapse_certificate.py
09ab52efda354fc909d0dc7f8de063fde054a9b9fc0c8bc272dad21c7d236a6d  results/root_unity_hardy_all_degree_endpoint_collapse_certificate.json
cbfd5640107565c87c1bc4a7657f064a6842685ccdb0fb711d6c1a9bccad118c  results/root_unity_hardy_all_degree_endpoint_collapse_hashes.sha256
~~~

The manifest pins both predecessor theorems and all hashes verify. Exact
block, rank-one, vertex, Gaussian, parity, threshold, pigeonhole, and norm
audits replay deterministically under a 1 GiB internal RSS guard. Item 72
does not provide the exceptional approximation or collapse rate it proves
necessary, and it does not classify $e+\pi$.

## 2026-08-27: a genuine adjacent first-period Euler-irregular seed

Checkpoint item 73 resolves two tempting qualitative shortcuts negatively.
Exact FLINT arithmetic gives



$$
\gcd(E_{3286},E_{3288})=151483,
$$



and deterministic trial division proves that $151483$ is prime. An
independent recurrence modulo $151483^2$ gives nonzero multiples of the
prime at both indices, so both valuations equal one.

The stronger statement comes from inverting the truncated cosh series in
$\mathbb F_{151483}[X]/(X^{151482})$. Scanning every even coefficient
proves that the complete first-period irregular-index set is exactly
$\{3286,3288\}$. Since the Kummer period $151482$ is far beyond the
indices, the item-71 factors at $N=1643$ are



$$
H_{1643}=J_{1643}=G_{1643}=151483,\qquad S_{1643}=1.
$$



The exact scan through this $N$ finds no earlier $J_N>1$, but that is
only a finite assertion. The example establishes that adjacent branches can
vanish together with the minimal possible total irregularity index two. It
therefore eliminates branch incompatibility and irregularity-index
amplification as unconditional routes to the needed bound. A quantitative
all-$N$ estimate for $J_N$ is still required.

Frozen hashes:

~~~
c9ed43839126af9542ec0c0891cb5a48023a7cb17ba21dca34cb83bc629b6078  sources/root_unity_adjacent_euler_irregular_seed_counterexample.md
a92019c257e7c985fdec00d5bb88b70154a67c8c8e0e9b2184dd0bb7f2c88542  scripts/root_unity_adjacent_euler_irregular_seed_certificate.py
4468c09210ac6a72303980f4cf27070c914a717bab474a8e7f86d4bd4fab3aaf  results/root_unity_adjacent_euler_irregular_seed_certificate.json
c4e0b694a4f57130370e1f66869f5d862536e21708a78a0fa1c8655463525f0f  results/root_unity_adjacent_euler_irregular_seed_hashes.sha256
~~~

The revised source and manifest passed strict TeX/control-byte checks. An
independent replay took 6.33 seconds, peaked at 86,904 KiB RSS, and preserved
the JSON hash with about 48 GiB system RAM still available. This is a finite
counterexample theorem, not a classification of $e+\pi$.

## 2026-08-27: successive minima and exterior no-amortization

Checkpoint item 74 tests the proposed escape through several independent
Hardy-short endpoint vectors. The evaluation/transverse image of the
integer coefficient lattice has determinant one. Minkowski's second theorem
therefore yields



$$
{1\over(d+1)!EH^d}\le\prod_{j=1}^{d+1}\lambda_j(H,E)
 \le {1\over EH^d}.
$$



This controls only the product of successive minima. For a full independent
set, replacing the constant coefficient column by the evaluation column is
a determinant-one operation, giving



$$
1\le|\det P|\le(d+1)!EH^d.
$$



For lower exterior powers, let $g$ be the Pluecker content and $W$ the
primitive exterior height. Exact contraction with the evaluation covector
constructs integer polynomials $R_J$ of degree at most $d$ with



$$
\max_JH(R_J)=W,\qquad
 |R_J(\pi)|\le{k!EH^{k-1}\over g}.
$$



Under conditional algebraicity and
$\kappa=r^2d+r-1$, this bounds the exterior-content exponent at the
Dirichlet scale by



$$
k-{d+1\over\kappa+1}.
$$



The strict reverse inequality is exactly what would be needed for the
contracted polynomial itself to violate the conditional measure. At $r=1$
the common boundary is $k-1$. Hence neither a determinant nor a saturated
wedge distributes the missing approximation power among several vectors.
If it succeeds, it has already produced the exceptional one-polynomial
approximation sought in item 72.

The same audit proves an all-rank Hardy/evaluation threshold comparison,
an additive degree/height ledger for products, and a one-small-factor bound
for translated pairwise resultants. Gaussian phase alignment preserves the
full statement, while real parity splitting gives only one evaluation
column per block.

Frozen hashes:

~~~
84ed2c28661846171d414529b6ed764646f47df1028b5c54590af5b15a65b9fe  sources/root_unity_hardy_successive_minima_exterior_no_go.md
b1a553637874fa957f781b8be2044377d8d2e80195a07fe7a99a1d7257f5f134  scripts/root_unity_hardy_successive_minima_exterior_certificate.py
7bc241179c63ac9fc0b6124c9279944c710243e06954a8c9508adf17fc11ea08  results/root_unity_hardy_successive_minima_exterior_certificate.json
2f13c98db67eb4dff21f6a442a1285207157ee08db712e410d53ddf213425e3b  results/root_unity_hardy_successive_minima_exterior_hashes.sha256
~~~

The revised $m,n\le d$ resultant hypothesis, all six dependency hashes,
syntax, control bytes, delimiters, and two JSON replays were independently
checked. The fresh replay took 4.29 seconds with roughly 48 GiB system RAM
remaining. Item 74 eliminates a method-level loophole but does not classify
$e+\pi$.

## 2026-08-27: exact centered-cosh residual quotient

Checkpoint item 75 closes the rational codimension question left by item 70.
Let $P,Q$ be the diagonal $[q/q]$ Padé pair for
$F(x)=1/(2\cosh\sqrt x)$, and $R,G$ the adjacent
$[q+1/q-1]$ pair. Schur positivity proves normality, while comparison of
the two Padé equations gives



$$
RQ-PG=\kappa x^{2q+1},\qquad\gcd(Q,G)=1.
$$



The constrained remainder spaces have exact $G$-Krylov bases. Consequently



$$
\rho_Q({\cal E}_{q,1})=G^2\mathbb Q[x]_{\le q-2}\quad(q\ge2),
$$



and the second quotient is



$$
\Phi({\cal E}_{q,2})=
 \mathbb Q\Phi(E^2)\oplus
 \bigl(\{0\}\oplus G^2\mathbb Q[x]_{\le q-2}\bigr)\quad(q\ge1).
$$



Thus the two nonexceptional images have codimension one for every $q$;
the $q=1,r=1$ image has codimension two. The first annihilator is
$[T]\mapsto[x^{q-1}]\rho_Q(G^{-2}T)$, and its moments obey the exact
$Q$-recurrence. Cramer's rule supplies the second-family syzygy
$E=GH+QK$, and evaluation at roots of $Q$ gives the corresponding
resultant product identity.

Frozen hashes:

~~~
1173dfd585050ef192cf0c71be8c6e14f6357a14e56e81d7f2afadf35d3f0afd  sources/centered_cosh_pade_residual_quotient_theorem.md
867b154754477d7e9e196f939dc5b5bf9e584d15d28fe3baa255505882dfd76e  scripts/centered_cosh_pade_residual_quotient_certificate.py
be9ed129087a44bb2d1d315efa8e19e3069682475a76b52a2c0410a5ec40d026  results/centered_cosh_pade_residual_quotient_certificate.json
eb10284c8cda928182de8b5f86f230a1bc708e8c3617391265c4f55849b77b13  results/centered_cosh_pade_residual_quotient_hashes.sha256
~~~

A fresh independent replay took 9.93 seconds, peaked at 87,048 KiB RSS, and
reproduced the frozen JSON. The theorem is over $\mathbb Q$; local Smith
factors and primitive annihilator height remain unresolved. No classification
of $e+\pi$ follows.

## 2026-08-27: reduced beta denominators and adjacent determinants

Checkpoint item 76 gives a quantitative theorem for the exact gcd isolated in
item 71. If



$$
P_N={|E_{2N+2}|\over G_N},\qquad
 Q_N={(2N+2)(2N+1)|E_{2N}|\over G_N},
$$



then



$$
{P_N\over Q_N}
 ={4\over\pi^2}{\beta(2N+3)\over\beta(2N+1)}
$$



and an alternating-tail calculation gives an error asymptotic with leading
term $32/(\pi^2 3^{2N+3})$. The explicit lower interval at $N$ and upper
interval at $N+1$ are disjoint, so the reduced ratios strictly decrease.

The adjacent determinant is a positive integer. Every secant Euler number is
odd, and



$$
v_2(Q_N)=1+v_2(N+1).
$$



The two adjacent valuations are therefore one and at least two, proving



$$
v_2(P_NQ_{N+1}-P_{N+1}Q_N)=1.
$$



The determinant is at least two, so the explicit error upper bound yields



$$
Q_NQ_{N+1}>{13\pi^2\over216}\,3^{2N+3}.
$$



This proves adjacent-product and individual-limsup exponential floors without
an irrationality measure. Zudilin's bound
$\mu(\pi^2)\le5.09541178\ldots$ separately yields the individual liminf



$$
\liminf_{N\to\infty}{\log Q_N\over N}
 \ge {2\log3\over5.095412}=0.4312162740\ldots.
$$



Frozen hashes:

~~~
8b22a86eea520400245e5529809da2dcce56cbfb26c9836677e23ccd0a197a0a  sources/root_unity_quadratic_euler_beta_denominator_floor.md
c9fd42d69521b2faaba8166c5495d25e75318a13a31327c9eaf41ea40ca18d1e  scripts/root_unity_quadratic_euler_beta_denominator_certificate.py
c36e90fdcd023c940ea525b98b5c4786e610061435d2aa8b913fb0200f4cfe97  results/root_unity_quadratic_euler_beta_denominator_certificate.json
22fba2af00e25aa5a956b923e490d2a853dd170ab2292178190bb5a1507d6f1d  results/root_unity_quadratic_euler_beta_denominator_hashes.sha256
~~~

Independent replay and proof audits pass. Both denominator floors are only
exponential in $N$, while the unreduced Euler scale is
$2N\log N+O(N)$. They therefore do not establish
$\log G_N=o(N\log N)$, do not bound $J_N$ at leading order, and do not
classify $e+\pi$.

## 2026-08-27: canonical quadratic two-regime no-go

Checkpoint item 77 asks whether the exact closer-root branch can be completed
by arguing that failure of “large $G_N$” makes $Q_N$ useful elsewhere.
For



$$
C_N(T)=4Q_N-P_NT^2,
$$



the relative endpoint is $\asymp3^{-2N}$. Conditional algebraicity degree
$r$ imposes the strict rate threshold



$$
\log Q_N<
 {2\log3\over2r^2+r}N-\Omega(N).
$$



Thus the first branch requires near-total cancellation of the factorial
Euler height. A new fixed-number-field lemma proves that the direct
translation $T=e+\pi-e$ has bounded coefficient-ideal content and
absolute projective coefficient height $\asymp Q_N$. Product-formula
normalization cannot erase failure of this threshold.

Exact adjacent elimination leaves only $T^2$ or $1$ after primitive
normalization, and the adjacent product has relative exponent at most two.
For fixed two-row weights, expansion of the beta Dirichlet series proves
that $(-1,9)$ is the unique nearest-pole cancellation. The resulting
Richardson ratio has base-$5$ error:



$$
{|\,\widehat C_N(\pi)\,|\over H(\widehat C_N)}
 ={48\over5^{2N+5}}\{1+O((5/7)^{2N+1})\}.
$$



Its reduced denominator is controlled by a new adjacent gcd. With
$h_N=\gcd(Q_N,Q_{N+1})$,



$$
{16Q_NQ_{N+1}\over9h_N^2}
 \le\widehat Q_N
 \le{8Q_NQ_{N+1}\over h_N}.
$$



The improved branch consequently needs



$$
\log h_N\ge
 \left(\log3-{\log5\over2r^2+r}\right)N+o(N).
$$



This is $0.5621329845\ldots N+o(N)$ for $r=1$. The exact valuation
ledger for three consecutive Euler numbers shows that small $G_N$ controls
the first reduced-denominator excess but gives no condition forcing the same
prime powers to survive into $Q_{N+1}$. Hence the two regimes are not
complementary without a genuinely new neighboring-valuation theorem.

Frozen hashes:

~~~
697f3b29d899a3dd229b6b7b9748ec77c74d60d603fb67ea5e7f10fef56cfdb3  sources/root_unity_quadratic_two_regime_canonical_no_go.md
b4508adf4f4235ccb65de8a17a7e24fc815434a67e35b8daf3ed8afd62f763e8  scripts/root_unity_quadratic_two_regime_canonical_certificate.py
05a48e1954f7999da7f042fccefb794c95c5eff65c66a82622d5168ab8060567  results/root_unity_quadratic_two_regime_canonical_certificate.json
398c9b03759673e2e0cce91e52abe74bf2a70b098f546158c8e972fba6de4398  results/root_unity_quadratic_two_regime_canonical_hashes.sha256
~~~

Independent replay reproduced the JSON in under one second at 69,220 KiB
peak RSS, with roughly 48 GiB system RAM available. All formula, dependency,
manifest, syntax, tag, delimiter, and control-byte checks pass. Item 77
closes a canonical dichotomy, not the arithmetic classification of
$e+\pi$.

## 2026-08-27: balanced quadratic border-content theorem

Checkpoint item 78 replaces the generic cofactor bookkeeping in the balanced
centered-cosh branch by a canonical two-determinant content.  Let



$$
F(x)={1\over2\cosh\sqrt{x}},\quad P_q/Q_q=[q/q]_F,
 \quad R_q/G_q=[q+1/q-1]_F.
$$



The exact Padé residual identity



$$
R_qQ_q-P_qG_q=\kappa_qx^{2q+1}
$$



allows a global residue calculation.  If
$a_m=[x^m]P_q^2/Q_q$, the two first moments satisfy



$$
h_j=-{\operatorname{lc}(Q_q)\over\kappa_q^2}
       a_{4q+1-j}\quad(j=0,1).
$$



Thus their primitive kernel polynomial is
$\operatorname{prim}(a_{4q}-a_{4q+1}x)$, provided the pair does not
vanish simultaneously.

An integral Toeplitz formulation makes the content explicit.  With
factorially cleared Padé matrix $T_q^\#$, primitive cofactor kernel $c_q$,
maximal-minor gcd $\delta_q$, and the two cleared borders $b_m$, put



$$
u_m=b_mc_q,qquad K_q=\gcd(u_{4q},u_{4q+1}).
$$



Then



$$
u_m={(-1)^q\over\delta_q}
       \det\!\begin{pmatrix}T_q^\#\\b_m\end{pmatrix},
 \qquad
 C_q^{\rm prim}={u_{4q}-u_{4q+1}x\over K_q}.
$$



This gives an exact local row-space criterion for every prime at which the
Padé matrix has full row rank.  A structured factorial clearing plus
Hadamard proves



$$
\log H(C_q^{\rm prim})\le(3+o(1))q^2\log q,
$$



reducing the previous cubic upper-bound scale.  The result deliberately does
not infer a lower bound from the finite data, does not extrapolate the
nonvanishing verified through $q=16$, and does not identify this border
content with the closer-root Euler gcd.

Frozen hashes:

~~~
a7db026c1ebc792ab30a8674897d48ddbedce71da350a730966fdfee5c6132a8  sources/centered_cosh_balanced_quadratic_border_content_theorem.md
e0c2e1b22bf916242ce685d1c43a1b88477b5052858fe26221d17bfaefb7d3bd  scripts/centered_cosh_balanced_quadratic_border_content_certificate.py
8272e59ac346044fcc23a76321ccf4252596c4b942dd3fc714228b6a694f3a27  results/centered_cosh_balanced_quadratic_border_content_certificate.json
c06ea9b875ba072de9bf250526538f6639afd7fa0131719febb5df9f36067eb3  results/centered_cosh_balanced_quadratic_border_content_hashes.sha256
~~~

Independent replay reproduces the frozen JSON in about 1.7 seconds at
1,425,356 KiB peak RSS.  At that time the 50-GiB host had about 48 GiB
available; the script's 2-GiB limit is an individual-process guard rather
than a machine allocation.  All source, determinant, manifest, syntax, and
byte audits pass.  Item 78 sharpens the remaining arithmetic target but does
not classify $e+\pi$.

## 2026-08-27: higher beta determinants and the multiplicity barrier

Checkpoint item 79 tests whether using many consecutive reduced beta ratios
can amplify the item-76 denominator floor.  Euler-product division gives the
exact signed expansion



$$
r_N={4\over\pi^2}\sum_{q\ \mathrm{odd}}b_qq^{-2N},
 \quad
 b_q=(-1)^{\omega(q)}\chi_4(q)
 {\prod_{p\mid q}(p^2-1)\over q^3}\quad(q>1).
$$



The unique extremal $h$-term response polynomial is



$$
A_h(X)=(X-1)\prod_{j=1}^{h-2}((2j+1)^2X-1).
$$



It has first surviving atom $(2h-1)^{-2}$, coefficient height
$\exp(2h\log h+O(h))$, an all-parameter tail bound, and a certified
nonvanishing range $N\ge N_0(h)=O(h^2)$.  Clearing one copy of every
participating reduced denominator gives the sharp comparison



$$
{2\log(2h-1)\over h}\le\log3,
$$



with equality only at $h=2$.  Hence extra exact mode cancellations cost at
least as much denominator multiplicity as they gain analytically.

The Vandermonde product is nonzero for all sizes by strict monotonicity, but
its exact beta-tail asymptotic gives only a linear-scale average floor.  For
fixed size, the signed Hankel determinant is eventually nonzero by its unique
leading Dirichlet-mode subset; its universal clearing exponent sum is
$h^2$.  The simultaneous higher-Euler determinant telescopes to the same
ratios and has exponent sum $h(h-1)$.  Finally,



$$
\det(r_{1+i+j})_{0\le i,j<3}
 =-{1238314183775556121\over51629038152493172462784000},
$$



so a positive Stieltjes/Jacobi continued-fraction argument cannot apply.

Frozen hashes:

~~~
e921fcb73e8c3fc4d62848008cc34d1f9ff0ee482fcba1e8ef5123462df1bca6  sources/root_unity_beta_higher_determinant_multiplicity_barrier.md
936b03be9dc6c63d17616d9e38c0c0c9a67755e1f8e20a746b2fe4fceaebaca7  scripts/root_unity_beta_higher_determinant_certificate.py
2f53dd329f9eef44bdd22868ec558da0a6f9c9f874d88cb077e3e53ddf9830ba  results/root_unity_beta_higher_determinant_certificate.json
abf5aae37871defe5a5fb0237506b0830fca17d94a6dd914bdf3994b086cf5c9  results/root_unity_beta_higher_determinant_hashes.sha256
~~~

The manifest pins the item-76 dependency, and independent replay reproduces
the JSON in about 0.21 seconds at 37,188 KiB peak RSS.  Strict source,
formula, JSON, Python, dependency, hash, delimiter, and byte checks pass.  The
remaining possibilities require a new theorem on actual lcm/common-content
correlations or a stronger growing signed determinant.  No classification of
$e+\pi$ follows from item 79.

## 2026-08-27: adjacent Euler descent and the discriminant barrier

Checkpoint item 80 attacks the neighboring gcd left by the two-regime
construction.  With $h_N=\gcd(Q_N,Q_{N+1})$, its exact local valuation is



$$
v_p(h_N)=\min((b+x-y)_+,(c+y-z)_+),
$$



where $b,c$ are the valuations of $A_N,A_{N+1}$ and $x,y,z$ those
of the three consecutive even Euler numbers.  At an off-index prime this is
positive exactly when $x>y>z$, giving



$$
(h_N^{\rm off})^2\mid|E_{2N}|,
 \qquad h_N^2\mid A_NA_{N+1}|E_{2N}|,
 \qquad v_2(h_N)=1.
$$



The squarefull descent is new structural information, but its logarithmic
upper bound remains $N\log N+O(N)$, not $o(N\log N)$.

For even $M=2m$, the centered Euler polynomial factors as
$\mathcal F_M(T)=f_M(T^2)$.  A common divisor $d$ of
$E_M,E_{M-2}$ forces



$$
\mathcal F_M(T)\equiv T^4V(T)\pmod d,
 \qquad f_M(Y)\equiv Y^2W(Y)\pmod d.
$$



Resultant and composition identities then prove



$$
d\mid\operatorname{Disc}(f_M),\qquad
 \operatorname{Disc}(\mathcal F_M)=
 (-4)^mE_M\operatorname{Disc}(f_M)^2,qquad
 d^3\mid\operatorname{Disc}(\mathcal F_M).
$$



Yet the natural Sylvester height is $O(M^2\log M)$, worse than the
trivial $O(M\log M)$ Euler bound.  The level-4 Eisenstein encoding has a
unit first Fourier coefficient after its constant term vanishes, distinct
adjacent residual eigenpackets, and an equally large Sturm determinant.
Neither route supplies the missing product estimate.

Frozen hashes:

~~~
28696128629ac4828d492dc5736545c8558e4546a3b566dfc2ecf7aa85170d13  sources/root_unity_adjacent_euler_descent_discriminant_barrier.md
8d1a5c5577389fb009eb3a1596c77d1cffc5183526515440db8f2f7553a9adf2  scripts/root_unity_adjacent_euler_descent_discriminant_certificate.py
2a62637288d4f807e4d34c17bdeaa64b5a03164f0303b18c27373bd7e47b1890  results/root_unity_adjacent_euler_descent_discriminant_certificate.json
57de6b30c8efc92532d3d7c8292e2467d176983baeb20443d7f17cfecf4f7f14  results/root_unity_adjacent_euler_descent_discriminant_hashes.sha256
~~~

All dependency hashes and independent replay checks pass.  The root replay
completed in under one second, reported 1,445,632 KiB peak RSS, and left
roughly 47--48 GiB available.  Item 80 is a structural theorem plus a
quantitative discriminant/modular no-go, not a classification of
$e+\pi$.

## 2026-08-27 — Actual beta-denominator lcm and first-period obstruction

The optimal $h$-term beta filter has integral coefficients and is
therefore cleared by the actual block lcm



$$
{\cal Q}_{N,h}=\operatorname{lcm}(Q_N,\ldots,Q_{N+h-1}).
$$



Combining this observation with the proved filter tail and nonvanishing
range gives



$$
{\cal Q}_{N,h}\ge
 \frac{(2h-1)^{2N}}
 {(4/\pi^2)((2h-1)^{-1}+(2N)^{-1})},
\qquad N\ge N_0(h),\quad N_0(h)\le2h^2+2.
$$



At $h=\lfloor\sqrt{(N-2)/2}\rfloor$, this is
$\log{\cal Q}_{N,h}\ge N\log N-O(N)$.

Writing $U_n=|E_{2n}|$,
$A_n=(2n+1)(2n+2)$, and
$B_n=U_n/\gcd(U_n,U_{n+1})$, exact valuations give
$B_n\mid Q_n\mid A_nB_n$.  The short-block $A_n$-lcm costs only
$o(N)$, while the Kummer-visible part of the $B_n$-lcm divides
$\operatorname{lcm}(1,\ldots,3(N+h))$.  Hence an
$N\log N-O(N)$ complementary factor remains, and each of its layers
has period longer than the full block.  Ordinary Kummer periodicity
provides no second index for those layers.  The missing input is a new
concentration or overlap theorem for first-period adjacent Euler drops.

Frozen package:

~~~
a0f3811a353cf19778bf0b262f20190de3735dccf8c2081a35d0b8c19035af28  sources/root_unity_beta_actual_lcm_kummer_barrier.md
fa9cda18584bbbb71cf5b12652ffd5c839468cc49886274a3e724d2b4205fdaf  scripts/root_unity_beta_actual_lcm_kummer_certificate.py
ae75d93ca1373db85dd704f8d20dabe0053797aac980efcee40b57f12dc92a13  results/root_unity_beta_actual_lcm_kummer_certificate.json
df801458d310f255dc59862dca63abedb3976eefc9edb680e9a75fc4662ec6ec  results/root_unity_beta_actual_lcm_kummer_hashes.sha256
~~~

The independent replay took $0.166$ seconds and $40{,}848$ KiB peak
RSS.  This theorem strengthens the denominator floor to an actual-lcm
statement but does not yield the individual denominator estimate needed
for a classification of $e+\pi$.

## 2026-08-27 — Universal balanced Padé endpoint nonvanishing

For the diagonal Padé pair to
$F(x)=1/(2\cosh\sqrt x)$, normalized by $Q(0)>0$, put



$$
a_m=[x^m]\frac{P(x)^2}{Q(x)}.
$$



An all-order Schur-function argument proves



$$
a_{4q}>0,\qquad a_{4q+1}<0\qquad(q\ge1).
$$



After $y=-x$, the secant generating function has the positive alphabet
$t_\nu=4/(\pi^2(2\nu+1)^2)$.  Jacobi--Trudi straightening determines
the numerator and error signs exactly.  For even $q$, the relevant skew
shape contains a full column of $q+1$ boxes, and tableau relaxation
gives



$$
s_{\Lambda/\mu}(t)
\le\frac{2^{-(n-q-1)}}{(2q+2)!}.
$$



This bound makes the error convolution strictly smaller than the positive
main term at both target degrees.  Therefore both residual moments from
the item-78 border theorem are individually nonzero and the balanced
survivor has exact quadratic endpoint degree for every order.

Frozen package:

~~~
6531d74029b442f3893425ef056af1dd2536988a2b508801439ab8e208493139  sources/centered_cosh_balanced_quadratic_nonvanishing_theorem.md
8d5ba5f486e8d5b422a9685d2665b70085a12152ee986b0832495ab770d85558  scripts/centered_cosh_balanced_quadratic_nonvanishing_certificate.py
3886c53959e0d263b6f803ec25b55facdea77aa6d7738b65a91f6385f0cb83e9  results/centered_cosh_balanced_quadratic_nonvanishing_certificate.json
f5d5ef9179b0386e259aac0c95969461c1244ed756c5b38b2c75ca94bc4e3f82  results/centered_cosh_balanced_quadratic_nonvanishing_hashes.sha256
~~~

The independent replay took about $1.10$ seconds and $72{,}876$ KiB
peak RSS.  This closes the local nonvanishing problem, but the primitive
content and normalized global-lift height remain uncontrolled; no
classification of $e+\pi$ follows.

## 2026-08-27 — Normalized Euler eliminant, Pascal height, and full moment obstruction

Three subsequent all-parameter results sharpened the two live branches.
First, the ordinary even Euler polynomial has the invariant-ring form



$$
{\cal E}_{2m}(X)=X(X-1)P_m(X(X-1)),
$$



with $P_m$ monic integral of degree $m-1$.  A common divisor of
$E_{2m}$ and $E_{2m-2}$ makes $-1/4$ a double root of $P_m$, so
it divides $\operatorname{Disc}(P_m)$.  At
$(2m,p)=(3288,151483)$, however, this is exactly one double root and
all remaining roots are simple.  Thus the next-subdiscriminant shortcut
is false, while the surviving Sylvester bound remains quadratic in the
degree.

Second, the balanced secant Padé system becomes a signed Pascal matrix in
the even-factorial basis.  Its exact integer endpoint convolution and a
Hadamard estimate prove



$$
\log H(C_q^{\rm prim})\le3(\log2)q^2+O(q\log q).
$$



This removes the former $q^2\log q$ clearing artifact.  A resumable
exact scan through $q=100$ nevertheless shows primitive height still
on a positive $q^2$ scale; the $q=100$ endpoint has 22,538 primitive
bits but only 861 content bits.  Sampled contents are $(8q+2)$-smooth,
which remains a finite observation.

Third, for every odd prime $p$, $r=(p-1)/2$, the paired
Cosgrave--Dilcher congruence gives



$$
E_{2n}\equiv M_p(n)=
 2\sum_{j=0}^{r-1}(-1)^j((2j+1)^2)^n\pmod p.
$$



The support is all nonzero quadratic residues, all weights are nonzero,
and the exact minimal constant-coefficient recurrence has order $r$
with characteristic polynomial $Z^r-1$.  Fourier inversion gives



$$
W_p(X)=-2\sum_{k=1}^{r}E_{2k}X^{r-k},\qquad
 W_p^2\equiv4\pmod{X^r-1},\qquad\deg W_p=r-1.
$$



Every full moment Hankel determinant is a nonzero weighted Vandermonde
square.  The seed $(N,p)=(1643,151483)$ proves that two adjacent zero
moments coexist with full rank and exact order $75741$.  Hence the
canonical bounded linear-recurrence, interpolation, and rank routes do
not compress the missing first-period prime product; a cross-prime
arithmetic coupling is still absent.

Frozen package hashes for the three source theorems and their replays are
recorded in checkpoint items 83--85 and in the top-level README.  The
newest item-85 hashes are:

~~~
4b24dbecf01e1a06690d4b75b620beb741c6825d6c1e1729cc28c333f020cd4e  sources/root_unity_adjacent_euler_first_period_moment_obstruction.md
46af6d5b3f93744f96eb023ddcb40b5085f956304b7f70a7700f29c99c1b6341  scripts/root_unity_adjacent_euler_first_period_moment_certificate.py
9abd8499467b5e0bc6830045195ba454b6dda212d449d3029d4dbe0b40260002  results/root_unity_adjacent_euler_first_period_moment_certificate.json
af340ed10de55eb9587fdb3167d475b7f5cda405367fedb3ca00244ed1b23adf  results/root_unity_adjacent_euler_first_period_moment_hashes.sha256
~~~

No result in this continuation classifies $e+\pi$.

## 2026-08-27 — Exact normalized lift of the balanced quadratic

The rational lift-height gap in the centered-cosh branch is now closed by
an explicit Padé basis.  For every $q\ge2$,



$$
{\cal E}_{q,1}=Q^2{\cal P}_q\oplus QG{\cal P}_{q-1}
                              \oplus G^2{\cal P}_{q-2}.
$$



For the primitive integer endpoint
$T_q=(u_{4q}-u_{4q+1}x)/K_q$, define



$$
C=\rho_Q(G^{-2}T_q),\quad J=(T_q-G^2C)/Q,\quad
 B=\rho_Q(G^{-1}J),\quad A=(J-GB)/Q.
$$



All divisions are exact and



$$
T_q=Q^2A+QGB+G^2C,qquad
 \deg A,\deg C\le q-2,quad\deg B\le q-1.
$$



Polarizing with the two centered Padé remainders gives a global form with
five frequencies, degree at most $6q$, origin order at least $8q+4$,
and endpoint $T_q(-\pi^2/4)$.  Since every construction step is linear,
the exact endpoint content $K_q$ divides every raw centered coefficient
before normalization; no ambient determinant or Cramer solve is needed.

The diagonal Schur cofactors admit the primewise clearing



$$
{\mathfrak D}_q=\prod_{p\le4q}
 p^{\lfloor2(q^2+q)/(p-1)\rfloor}.
$$



Its $2q^2\log q$ leading logarithm is cancelled by the $q$ forced
columns of height $q$, which give
$S_k\le((2q)!)^{-q}(2k)!^{-1}$.  Stable negative powers modulo $Q$
and an explicit Schur lower bound for the normalized cross coefficient
then prove



$$
\log H(T_q)=O(q^2),\qquad
 \log H_{\rm an}({\cal L}_q)=O(q^2).
$$



The global coefficients are rational and serve only in the analytic
Schwarz majorant for the already primitive integral endpoint; no common
denominator or integral global-height theorem is asserted.  This result
removes the quotient/Cramer artifact, but the remaining quadratic scale
still exceeds the available $2q\log q+O(q)$ analytic gain.

~~~
b5448650b31b887a163ba95f593e38fc5c45195b61800f8c834ecb7ed2369d9f  sources/centered_cosh_balanced_quadratic_normalized_global_lift_theorem.md
46dd6f87dbec2927c81a870225b8bee9542684ab48ceb391514d3aaab1c1e092  scripts/centered_cosh_balanced_quadratic_normalized_global_lift_certificate.py
d9fa114ca1047846654015ff5353631db481269a40f7c48414f918a956d9481c  results/centered_cosh_balanced_quadratic_normalized_global_lift_certificate.json
90c432faf5130880664ffa561aff0faa7d574dde8c1f50c265a13dc3002591c8  results/centered_cosh_balanced_quadratic_normalized_global_lift_hashes.sha256
~~~

The independent replay includes $q=2$, took about $3.85$ seconds,
and peaked at $77{,}596$ KiB RSS.  No classification of $e+\pi$
follows.

## 2026-08-27 — A polynomial section for bounded cyclic Euler windows

The first-period square-root identity has now been audited beyond its
linear recurrence.  Put



$$
A_p=-C_p/2=\sum_{k=0}^{r-1}a_kX^k,qquad r=(p-1)/2.
$$



Then $A_p^2=1$ modulo $X^r-1$, so its complete coefficient system is



$$
F_t(\boldsymbol a)=
 \sum_{i=0}^{r-1}a_i a_{\langle t-i\rangle_r}=\delta_{t,0}.
$$



For prescribed coefficient indices $S$ and selected equation indices
$T$, a separated anchor $u$ produces an explicit section by setting
$a_u=1$ and assigning one partner $a_{t-u}$ to absorb each desired
convolution value.  Therefore the selected convolution ideal has zero
intersection with the low-data ring.  Adding any pre-existing low ideal,
including the two adjacent Euler zeros, does not change that conclusion.

For initial intervals $S\subseteq[0,L]$, $T\subseteq[0,K]$, the
choice $u=L+K+1$ works for $r>2L+3K+2$.  At
$L=K=N+1$, this covers every prime $p>10N+15$; all smaller
first-period primes have total log-mass $O(N)$.  Hence a bounded
low-convolution window cannot supply the missing far-prime product bound.
The actual $(1643,151483)$ seed verifies a 1,645-equation synthetic
completion and an intentional failure at the next equation.

~~~
e783aeb445472e0630e7945931a5978b9a0a15180dee03e1409cb59693f8b1b8  sources/root_unity_adjacent_euler_cyclic_window_section_no_go.md
cb8301f80b2c5d3b57d6f8b6901d00c9c7d2484cd2f424a5ec55581c938a1ff0  scripts/root_unity_adjacent_euler_cyclic_window_section_certificate.py
9614598edb4ecb125e73696e38615df0b3e56466e7468f69630c581fb3988276  results/root_unity_adjacent_euler_cyclic_window_section_certificate.json
f955bf4e71a080d0622e314352a3784b93cc772a3146e66bdb258c35e1ce3904  results/root_unity_adjacent_euler_cyclic_window_section_hashes.sha256
~~~

The result is intentionally local: it leaves the full $r$-equation
system and nonlocal arithmetic couplings open, and does not classify
$e+\pi$.

## 2026-08-27 — Exact normalization bridge for the centered-cosh border

The factorial-Pascal and primitive bordered versions of the balanced
centered-cosh denominator have been reconciled exactly.  The signed even
binomial transform taking the primitive Pascal vector $d$ to the residual
vector $e$ is lower unitriangular over $\mathbb Z$, so $e$ is primitive.
Writing



$$
g_{B,q}=\gcd_k\left(e_k(2q)!/(2k)!\right),\qquad
 s_q=(2q)!/g_{B,q},
$$



a Bezout argument proves $g_{B,q}\mid(2q)!$.  Thus $s_q$ is integral,
divides $(2q)!$, and $s_qB_d(-x)$ is precisely the primitive ordinary
integer Pade denominator, up to global sign.

For the factorial-Pascal endpoints



$$
L_q=(8q+2)(8q+1)w_{4q},\qquad R_q=w_{4q+1},
$$



the earlier cleared bordered endpoints satisfy



$$
(u_{4q},u_{4q+1})=(s_qL_q,-s_qR_q),
 \qquad K_q^{\rm border}=s_q\gcd(L_q,R_q).
$$



This identity is valid for every $q\ge1$ and corrects the comparison of
the two content normalizations.  The accompanying exact computation finds
smooth support through $q=30$ and an lcm-square divisibility for
$2\le q\le30$, but these statements remain explicitly finite.  The
canonical S/J-fraction was reconstructed as a further diagnostic; its early
coefficients contain irregular primes and yield no all-parameter content
formula.

~~~
6841a257ef7123c0080469335b5bd9a35c3f54ea36701a3894a95a447b6763cb  sources/centered_cosh_pascal_border_normalization_theorem.md
04e9f875ed419e1b3ba03595cf3a01dd3eb9cf0ed101254d2f6a2172822d813a  scripts/centered_cosh_pascal_border_normalization_certificate.py
01639485ade5a8b3b349a725861d436294a389e621d23a2da9c16dffadd3ad1c  results/centered_cosh_pascal_border_normalization_certificate.json
6b828f9c0a0b1aff69e598969cc9f2da3da7665307c99295136ba0b08fe3cb23  results/centered_cosh_pascal_border_normalization_hashes.sha256
~~~

The dependency on the older bordered JSON is pinned in the manifest.  A clean
root replay reproduced the result in about $0.14$ seconds at roughly
$65$ MiB peak RSS.  Hash, syntax, and dependency checks pass.  The exact
bridge does not prove the needed all-$q$ gcd bound and does not classify
$e+\pi$.

## 2026-08-27 — Positive quadratic Robin repair and primitive gap

The exact Stein parameterization now yields a complete answer for quadratic
corrections to the factorial Taylor near-solution.  If
$t=1-x$, $(1-i)^N=R_N+iI_N$, and $M_N=N!-R_N$, every integral
quadratic repair is



$$
C_{N,q}=I_N-4q+(q-M_N/2)t-qt^2,
$$



with corrected residual



$$
F_{N,q}=t^N+M_Nt(1-t/2)-I_N(1-t)
          +q(4-6t+4t^2-t^3).
$$



These polynomials satisfy the three common-kernel equalities with target
$N!$.  The choices $q=0$ for $I_N\le0$ and
$q=\lceil I_N/3\rceil$ for $I_N>0$ are nonnegative on the entire
unit interval, so the Robin repair is genuinely constructive.

The construction nevertheless has a sharp arithmetic obstruction.  The
three exact weighted integrals of its correction basis are
$\pi-3/2$, $1+2\log2$, and $10$.  Positivity forces enough of the
last coordinate that the unnormalized form is asymptotically at least
$(\pi-3/2)N!$.  If the rational output is $B/D$ in lowest terms,
its primitive content is exactly $\gcd(N!,B)\le N!$.  Hence the fully
primitive positive form has liminf at least $\pi-3/2$.

More generally, Bernstein--Walsh evaluation at $i$, nonnegative Markov
integration, and the same exact content ledger give a positive primitive
gap for every fixed correction-degree bound.  A successful correction must
therefore have degree tending to infinity or exploit a genuinely different
nonlocal mechanism.

~~~
1611c4976a64836a20209871a55b92e09bcb6c0c9cb18701cd800567b1a0ac21  sources/common_kernel_stein_robin_quadratic_correction_barrier.md
f814471c0c627ff2fb9c4da2f99a4a37ebf6380316d030796c7ddc946c4921dc  scripts/common_kernel_stein_robin_quadratic_correction_certificate.py
4641657f345e13bde4ed84b4642ffd4942d3f6b8448f9c9a60ecbe573dbf216d  results/common_kernel_stein_robin_quadratic_correction_certificate.json
208982ad388c02ba42c79726b6eaefa8acd1ed7d5a2fad6de5c138a44483038a  results/common_kernel_stein_robin_quadratic_correction_hashes.sha256
~~~

The root replay reproduced the frozen JSON in about $1.45$ seconds at
$21{,}360$ KiB peak RSS, and all dependency hashes pass.  This is not a
proof about the arithmetic classification of $e+\pi$.

## 2026-08-27 — Exact unbalanced Padé allocation and one-third transition

The unbalanced centered-cosh lower lift now has an all-parameter
single-parity decomposition.  For $B=2M+\sigma$, $d=M+r$, the relevant
factor space is



$$
V_{M,r}^{(\sigma)}
 =Q_{[M+\sigma/M]}{\cal P}_{r-\sigma}
  \oplus
  G_{[M+1-\sigma\,/\,M+2\sigma-1]}{\cal P}_{r-1}.
$$



The formula corrects a tempting parity error: for $\sigma=1$, the
companion denominator is the lower $[M/(M+1)]$ entry.  In the range
$M\ge2r-\sigma$, coprimality makes the three quadratic summands direct,
so the product dimension is $6r-3\sigma$ and the ambient codimension is



$$
\delta=2M-4r+3\sigma+1=3(B-d)-d+1.
$$



After translating back to $(n,t)$, this is
$\delta=(3t-n)/2+O(1)$.  The one-third slope is therefore structural,
not a numerical artifact.  The exact minimum-degree question becomes a
square reversed-jet determinant for $1,H,H^2$ or $1,K,K^2$.  General
nonvanishing and cancellation between the two parity product spaces remain
open; the nonzero $M\le8$ grid is diagnostic only.

Primewise Schur clearing proves $O(M^2)$ input Padé log-height and a
direct-minor bound $O(rM^2+r\log r)$.  Even a hypothetical structured
reduction to the input $O(n^2)$ scale still exceeds the centered
$O(n\log n)$ gain.  This records the precise current majorant barrier
without asserting any lower bound on the true primitive height.

~~~
a9e1d82af845b01150b4075c26a45425d7907fbc1b48862d9b1ca70bb2e08f00  sources/centered_cosh_unbalanced_pade_slope_obstruction.md
193cda9b3eace30006c4ca839dac379212bf340dd5063e0b204a0a12cb81de0b  scripts/centered_cosh_unbalanced_pade_slope_obstruction_certificate.py
1699b6167fc69c3858fccb33abbdd9c27590a64ee14aa290b7eecfdf0d04db79  results/centered_cosh_unbalanced_pade_slope_obstruction_certificate.json
343a7a07d9a7b706caf7752a423b29e4b10be40f3c31cce0bfadc9d7ef978dd5  results/centered_cosh_unbalanced_pade_slope_obstruction_hashes.sha256
~~~

The replay passed in about one second at roughly $69$ MiB peak RSS, and
the root and independent branch audits agreed on every corrected degree
convention.  No arithmetic classification of $e+\pi$ follows.

## 2026-08-27 — Optimal integer Robin localizer and harmonic obstruction

An explicit growing-degree multiplier preserves the full Robin residue:



$$
h_m=x^{4m}(m+1-mx^4),\qquad
 h_m-1\in(1+x^2)^2\mathbb Z[x].
$$



It obeys $0\le h_m\le1$, has endpoints $(0,1)$, and has exact mass



$$
\int h_m=\int(1-x)h_m'
 =\frac{8m+5}{(4m+1)(4m+5)}.
$$



The endpoint congruence $h(1)\equiv1\pmod4$ proves its sup-norm
optimality.  The product rule then supplies genuine $O_K(1/m)$
localization for every fixed correction.

Two exact theorems block the desired use.  First, Gaussian arithmetic at
$1-i$ proves in every degree that a correction of the factorial Taylor
near-solution has endpoint order strictly below $N$.  Its boundary-layer
limit changes sign, so sufficiently large $m$ cannot preserve positivity.
Second, the complete rational output contains a defect coefficient
$A=N!-\Re(1-i)^N$.  Prime isolation shows that each
$5m/2<p<3m$, $p\nmid A$, occurs with valuation $-1$ in that rational
coordinate.  The reduced denominator is therefore of lcm scale,
$\log q\ge(1/2+o(1))m$, despite the sparse multiplier.

The output-gcd calculation is also exact.  If the residual were positive,
the fully primitive form would be at least
$3q/[N!(\deg F+1)^2]$, which grows on the natural localizing diagonals.
The result does not cover every varying moderate diagonal or every nonlocal
integer correction.

~~~
5eb2a69842edfa4d6b8f88390834179e3e3cba65881af44120bc5161d1555ec8  sources/common_kernel_integer_robin_localizer_barrier.md
252ecc1e461d5572102a0ed784811815d537efdcb75afeb96571d038d102aa4a  scripts/common_kernel_integer_robin_localizer_certificate.py
2bcab0e6031398337afc7b2797c08e949f7fae546b34d695386838dc07059468  results/common_kernel_integer_robin_localizer_certificate.json
1754bcceff930fe5ed44b67282f666970aeabb5616886dfb1e5cab3eb19c4a07  results/common_kernel_integer_robin_localizer_hashes.sha256
~~~

The root replay reproduced the frozen JSON in about $0.16$ seconds at
$21{,}072$ KiB peak RSS.  All pinned dependencies and hashes pass.  This
is a growing-degree route obstruction, not a proof about $e+\pi$.

## 2026-08-27 — A prime-window theorem for arbitrary high-order Robin localizers

The sparse-localizer harmonic denominator has been promoted to an
all-parameter theorem.  With $u=1+x^2$,
${\cal T}P=(1-x)P'-xP$, and
${\cal T}K=uG+(\alpha+\beta x)$, take any integral
$h\equiv1\pmod{u^2}$ with $h(0)=0$.  If
$n=\operatorname{ord}_0h$ and



$$
S_h=\frac{{\cal T}(hK)-{\cal T}K}{u},
$$



then the initial coefficients of $r=(h-1)/u$ are forced:
$r_{2j}=(-1)^{j+1}$ and $r_{2j+1}=0$ below $n$.  In the exact
identity



$$
S_h=(h-1)G+r(\alpha+\beta x)+(1-x)(h'/u)K,
$$



this leaves coefficient $\pm\alpha$ at $x^{p-1}$ for every prime in
the stated degree window.  When



$$
p>(\deg S_h+1)/2,
 \quad p-1>\deg G,
 \quad p<n,
 \quad p\nmid\alpha,
$$



that monomial is the unique source of a $p$-denominator, proving



$$
v_p\!\left(4\int_0^1S_h\right)=-1.
$$



Therefore $n\ge(1/2+\varepsilon)\deg h$ forces an exponential output
denominator.  Exact bookkeeping shows that a fixed rational base coordinate
and primitive normalization cannot remove the prime interval; for the
factorial Taylor correction the base denominator is only lcm-scale in
$N$.

Under positivity, the congruence also fixes $h(1)=1$.  A retained
endpoint derivative of ${\cal T}(hK)$, combined with shifted Markov
inequalities, gives a polynomial lower bound for its weighted absolute
norm.  The denominator-cleared norm thus diverges exponentially.  The
theorem deliberately leaves open nonlocal degree/order ratios, signed
cross-channel cancellations, and rapidly varying corrections.  An explicit
sign-changing polynomial annihilating both defect moments proves that this
scope qualification is necessary.

~~~
65b31f7df68551e35ecab50fb0f09026dbb87bd7e596075c13703367ac5a90c1  sources/common_kernel_robin_localizer_moment_denominator_barrier.md
84f878fe9f0e1cafecd32cb0661f760564ccf86018579e83ad4833b74bd0284f  scripts/common_kernel_robin_localizer_moment_denominator_certificate.py
c457c0aee6cdc289707c610083957a55c84b724205926930b694e8023a072fe0  results/common_kernel_robin_localizer_moment_denominator_certificate.json
1a523213cd86f5b3865bf86a7b35a4f0bd682df262af920cc7b02623f0560c03  results/common_kernel_robin_localizer_moment_denominator_hashes.sha256
~~~

The root replay took about $6.32$ seconds at $21{,}032$ KiB peak RSS,
and every frozen hash and dependency check passes.  This is a general route
obstruction, not an arithmetic classification of $e+\pi$.

## 2026-08-27 — Universal upper-half prime content for the Pascal endpoint

An exact Euler-periodicity argument proves the main regular layer in the
centered-cosh content.  If $U_n=|E_{2n}|$ and $T_n$ is the factorial
coefficient of $\sec^2\sqrt y$, then for every odd prime $\ell$, with
$h=(\ell-1)/2$ and $\chi=(-1)^h$,



$$
U_{n+h}\equiv\chi U_n\pmod\ell\quad(n\ge1),
 \qquad T_{n+h}\equiv\chi T_n\pmod\ell\quad(n\ge0).
$$



The value $U_h\equiv\chi-1$ is exceptional and is retained in the
midpoint calculation.  For the factorial-Pascal Padé pair, the reduced
odd-top border satisfies



$$
rJ_r=-(2r)![y^r],2(BH-p)yH'=0
 \quad(1\le r\le2q+1).
$$



Lucas's theorem maps the two endpoint convolutions to these borders for
every prime $4q<\ell\le8q+2$.  It follows that



$$
\prod_{4q<\ell\le8q+2\atop \ell\ {\mathrm{prime}}}\ell
 \mid G_q^{\rm Pascal}
$$



for all $q$.  The proof includes the midpoint and explicit-prefactor edge
cases and asserts only one squarefree layer.  The residual quotient may
still contain primes above $8q+2$ or deep small-prime powers; excluding
those remains the central arithmetic problem.

~~~
9e1a951e63b05455db4e6ade95f4b1a99b0c6330ff8680327f204b5e54f0b27d  sources/centered_cosh_pascal_universal_interval_content_theorem.md
cab278c79d3332e0d8f112fdaad0757fd309a5fcb24b120dad0ca384b67917a4  scripts/centered_cosh_pascal_universal_interval_content_certificate.py
18173a8bd0e455ac35bd3d2cebe3e0d73293f3ebe559381e63cb4e2531901384  results/centered_cosh_pascal_universal_interval_content_certificate.json
66e20c910ef2e167d8f52f57380086b0b97cfa473c0699901ad8c7f3f936ef78  results/centered_cosh_pascal_universal_interval_content_hashes.sha256
~~~

The root replay reproduced the frozen certificate in about $0.36$ seconds
at $34{,}304$ KiB peak RSS.  This is a universal endpoint-content theorem,
not a classification of $e+\pi$.

## 2026-08-27 — Even nonlocal moment denominators and the one-third window

Let $u=1+x^2$ and let even $h\in\mathbb Z[x]$ satisfy
$h\equiv1\pmod{u^2}$ and $h(0)=0$.  With
$n=\operatorname{ord}_0h$, $d=\deg h$, and $r=(h-1)/u$, the
forced prefix and global parity give



$$
r_{p-1}=\pm1,\qquad r_{2p-1}=0
$$



for every odd prime $d/3<p\leq n$.  Since these are the only two
coefficients paired with a $p$-divisible integration denominator,



$$
v_p\!\left(\int_0^1r\right)=-1.
$$



If $D(h)$ clears both $\int r$ and $\int xr$, and
$0\leq h\leq1$, shifted Markov supplies



$$
D(h)\max(|I_0|,|I_1|)
 \geq{1\over16d^2}\prod_{d/3<p\leq n\atop p>2}p.
$$



The family $h_k=(2x^4-x^8)^k$ has $(n,d)=(4k,8k)$ and
$\sqrt{k}\int h_k\to\sqrt\pi/8$, so its cleared mass grows at least
like $\exp(4k/3+o(k))$.  For the full correction output, the exact
survival residue is $2s_{p-1}+s_{2p-1}$; parity of $h$ does not
control the second coefficient.  A positive degree/order-four witness
shows why the remaining nonlocal range cannot be discarded as empty.

~~~
df2657ebe8e241d6f14b8c8628ba5c085662301936efc869f69669818749bb49  sources/common_kernel_even_nonlocal_moment_denominator_barrier.md
82e1828ef3f4ed22ffe7d60abcb9fbe9e709c6bf75df0fbcecb793b67bc632e6  scripts/common_kernel_even_nonlocal_moment_denominator_certificate.py
c53c46ce84fb9ea035020d24fbc876bc96136a03327188108e4212c08f21a842  results/common_kernel_even_nonlocal_moment_denominator_certificate.json
bc6aae22ca67cb7e04678432e3befdd33b7072ab3cc67b1d656134fd7e0a1806  results/common_kernel_even_nonlocal_moment_denominator_hashes.sha256
~~~

The root replay took about $3.42$ seconds at $21{,}488$ KiB peak RSS.
The proof and all exact audits pass.  This is a nonlocal route obstruction,
not a classification of $e+\pi$.

## 2026-08-27 — Exact coupled parity criterion and terminal-band exclusion

The separate unbalanced parity determinants did not account for cancellation
between $V_0^2$ and $xV_1^2$.  If $C$ is the full product coefficient
matrix and $J$ consists of its rows in degrees at least two, rank-nullity
gives the exact correction



$$
\dim((V_0^2+xV_1^2)\cap\mathbb Q[x]_{\leq1})
 =\operatorname{rank}C-\operatorname{rank}J,
$$



together with $\ker J/\ker C$ as the intrinsic survivor space.  Exact
Padé normality and a three-column reversed jet then prove



$$
n\geq5,\quad n-3\leq t\leq n-1
 \Longrightarrow
 (V_0^2+xV_1^2)\cap\mathbb Q[x]_{\leq1}=\{0\}.
$$



For equal blocks in the remaining strict-slope range, reversal reduces the
leading obstruction to a $6r$-column system in shifted
$1,K,K^2$, or a $6r+3$-column system in shifted $1,H,H^2$.
Their nonvanishing is not inferred from the exact 248-pair FLINT grid.
Generic coupled minors retain logarithmic height $O(n^3)$.

~~~
3aea77c0901bcf1d1209ee57c18dec01cc2c15c37c454249a8bb45af9b91d52d  sources/centered_cosh_unbalanced_coupled_parity_obstruction.md
d517a9033881398e4cef117ef57f3e6e5601c8f3aabd1f68dd43cffc1304ecda  scripts/centered_cosh_unbalanced_coupled_parity_certificate.py
6bd9b5f1d9c2046e2847718b35140789c08581913710d080c710d062fd6ab0cc  results/centered_cosh_unbalanced_coupled_parity_certificate.json
985a4a111319321868b17e526f0ecf6e41896708a92fc1db2256402188b7580a  results/centered_cosh_unbalanced_coupled_parity_hashes.sha256
~~~

The independent replay took about $6.63$ seconds at $38{,}968$ KiB
peak RSS.  Exact ranks, dependencies, syntax, JSON, and hashes pass.  This
closes the terminal band but does not classify $e+\pi$.

## 2026-08-27 — Positive cancellation of both nonsymmetric one-third residues

For an arbitrary congruence-preserving localizer, primes $d/3<p<n$
contribute through two possible denominators in each of
$I_0=\int r$ and $I_1=\int xr$.  Exact reduction gives



$$
I_0\in\mathbb Z_{(p)}
 \iff2r_{p-1}+r_{2p-1}\equiv0,qquad
 I_1\in\mathbb Z_{(p)}
 \iff r_{2p-2}\equiv0\pmod p.
$$



Both congruences can occur under positivity.  With



$$
h=(2x^4-x^8)^6
 \left(1-(1+x^2)^2x^3(1-x)^2\right)^2,
$$



one has $0\leq h\leq1$, $h\equiv1\pmod{(1+x^2)^2}$,
$(n,d)=(24,66)$, and



$$
r_{22}=1,\quad r_{44}=169\cdot23,\quad r_{45}=-1520.
$$



Thus the sole window prime 23 cancels in both moments.  The exact reduced
denominators are nonzero modulo 23.  This rules out the direct
prime-by-prime extension of item 94 but leaves aggregate surviving-prime
mass and additional correction channels open.

~~~
d91d09a05d767e31ef968f72813191421803e766c20c0407c0c69f39152b80fb  sources/common_kernel_nonsymmetric_two_moment_residue_counterexample.md
ab2712dcad3901dc5b0352338f34975347dc4bc4136c97ea1d7e0f4585e64629  scripts/common_kernel_nonsymmetric_two_moment_residue_certificate.py
d6452400a3014be7d59abdbed03ff2bd66f26c68692fa94f57090959212f57df  results/common_kernel_nonsymmetric_two_moment_residue_certificate.json
14edc755bb18e6726f6e1e5f6006afcc76950e2d3206dd3d2b942e10ee471081  results/common_kernel_nonsymmetric_two_moment_residue_hashes.sha256
~~~

The root replay took about $3.54$ seconds at $20{,}728$ KiB peak RSS,
and every exact check passes.  This counterexample protects the proof search
from an overgeneralized denominator claim; it does not classify $e+\pi$.

## 2026-08-27 — Positive CRT cancellation of an entire 17-prime window

The arbitrary-parity obstruction is aggregate, not merely local.  Let



$$
h=(2x^4-x^8)^{115}\bigl(1-(1+x^2)^2x^{75}(1-x)^{75}
 (c_0+c_1x)\bigr),
$$



with



$$
\begin{aligned}
c_0&=139574584508098815002244647712452355913710915,\\
c_1&= 92665357687907045832657432294875741514399515.
\end{aligned}
$$



This polynomial is integral, congruent to one modulo $(1+x^2)^2$,
vanishes at zero, and lies in $[0,1]$ throughout $[0,1]$.  Its
order and degree are $(n,d)=(460,1075)$.  Every one of the 17 primes in
the complete window $d/3<p<n$ satisfies



$$
2r_{p-1}+r_{2p-1}\equiv0,\qquad r_{2p-2}\equiv0\pmod p.
$$



Consequently their product
$237359812447644832129693355690076072498951997$ is coprime to the
common reduced denominator of the two moments.

The mechanism is an exact two-variable CRT interpolation in the coefficients
of $x^{75}(1-x)^{75}(c_0+c_1x)$.  Every local matrix is invertible, and
the least nonnegative representatives obey $c_0+c_1<4^{74}$, which is
exactly the padding capacity needed for positivity.  This proves a finite
all-window counterexample, not an asymptotic family.

~~~
271a0184572a5e203f56564c9db789410dc34eec18488c28f880d31bbfc015e2  sources/common_kernel_positive_crt_all_window_cancellation_barrier.md
b533da632f07a6887f225638b55ff67b1fd465fc09920f1da5ab5df4171b94ff  scripts/common_kernel_positive_crt_all_window_cancellation_certificate.py
32d4df4cba3eece31dd0d202f80db95495da3b02be0256155406bedea9be961b  results/common_kernel_positive_crt_all_window_cancellation_certificate.json
fd2a96672780209dcca4fd2ea4cf2d437fb491432667ed9fd32db0cc154f16b4  results/common_kernel_positive_crt_all_window_cancellation_hashes.sha256
~~~

The root replay used about $21$ MiB, and an independent sparse-polynomial
calculation rechecked every residue.  The result eliminates an overstrong
aggregate lemma but does not classify $e+\pi$.

## 2026-08-27 — Asymptotic cancellation of three quarters of the prime window

The CRT padding mechanism scales.  Fix
$2/(2+\log4)<\lambda<1$, let $L=\lfloor\lambda m\rfloor$, and set



$$
B_m=x^{4m}(m+1-mx^4),\qquad
 w_m=x^{4L}(1-x^4)^L(1-x^2).
$$



The identity



$$
B_m(1+x^2)w_m
 =x^{4(m+L)}(m+1-mx^4)(1-x^4)^{L+1}
$$



makes the two ITEM96 residue coordinates diagonal.  For every prime
$2m+2L<p<4m$, the diagonal coefficient is nonzero modulo $p$ unless
$p$ divides $K=2mL+6m+4L+5$.  A single ordinary CRT integer $c_m$
then makes both moments $p$-integral for every nondegenerate prime, while



$$
h_m=B_m\bigl(1-c_m(1+x^2)^2xw_m\bigr)
$$



remains integral, positive, congruence-preserving, and of exact
order/degree $(4m,4m+8L+11)$.

The canceled prime log-mass is $2(1-\lambda)m+o(m)$; the full natural
window mass is $(8/3)(1-\lambda)m+o(m)$.  Thus the ratio tends to
$3/4$.  Prime divisors of $K$ cost only $O(\log m)$, and
$\lambda\log4>2(1-\lambda)$ gives the CRT representative exponential
room inside the positivity capacity.

~~~
211fa36d058cfedb242e8dc732cac2ce9bb354e81e241fa6799f6f063a5715f5  sources/common_kernel_positive_crt_asymptotic_three_quarter_cancellation.md
01795ba68c3a16760f78f1913ed17821155b49c0e9e4591b8239a2ebd0a4b690  scripts/common_kernel_positive_crt_asymptotic_three_quarter_certificate.py
f4411917f17e2ba40f593ead5da578cbaf2fee1b2ee3b658343e957c5d1f531a  results/common_kernel_positive_crt_asymptotic_three_quarter_certificate.json
e5e497408f8b6a1ad6c4fc28634e2c5e8805754e3c10bf52e700325033d2625c  results/common_kernel_positive_crt_asymptotic_three_quarter_hashes.sha256
~~~

The deterministic replay and an independent polynomial reconstruction pass.
This closes the hoped-for universal aggregate survival lemma for the two
moments, but leaves further channels and the classification of $e+\pi$ open.

## 2026-08-27 — Exact double-zero counterexample in the Bessel index lift

The finite conjecture
$v_p(q_n)\leq1+\lceil\log_p n\rceil$ fails.  On the ordinary
$7$-adic root branch,



$$
n_*=464838342618219576262104570205987685961890202821
$$



satisfies $7^{56}<n_*<7^{57}$ and $v_7(q_{n_*})=59$.  With
$f(n)=(-1)^nq_n$ and $A_j=\Delta^jf(0)$, the exact closed formula
implies



$$
\frac{j!}{\lfloor j/2\rfloor!}\mid A_j.
$$



Every $j\geq869$ term therefore vanishes modulo $7^{60}$, and the
finite Mahler sum gives



$$
f(n_*)\equiv5\cdot7^{59}\pmod{7^{60}}.
$$



The two consecutive zero Hensel digits occur at positions 57 and 58; the
next digit is 6.  This falsifies the sharp digit claim without affecting the
weaker sufficient little-oh target.  That target reduces to controlling the
terminal zero-run length uniformly in both the prime and the surviving branch.

~~~
2e34ff5b30e658088d882568f83493c4c09582ccdbf921bb6337005b2c213abf  sources/bessel_padic_index_double_zero_counterexample.md
f0733a1493311401ceb6a0f59194012db20ee04ddf50203ecce601b4280eccf8  scripts/bessel_padic_index_double_zero_counterexample_certificate.py
c06353984f883dc02b441492fb5f414a8f0cd750378f86f4978bf8bde3db7a5d  results/bessel_padic_index_double_zero_counterexample_certificate.json
ee1b2591676f6721a1b133ffb8374c3e35de0a0f983ca930271603df6708f58a  results/bessel_padic_index_double_zero_counterexample_hashes.sha256
~~~

The byte-identical replay and an independent direct closed-sum evaluation pass.
This result prevents a false extrapolation and does not classify $e+\pi$.

## 2026-08-27 — Asymptotically complete cancellation of the one-third window

A shifted beta-type padding reaches every prime in the actual natural window.
For sufficiently large $q$, put



$$
B_q=x^{20q}(5q+1-5qx^4),\qquad
 w_q=x^{12q}(1-x^4)^{4q}(1-x^2).
$$



The product $B_q(1+x^2)w_q$ is supported in degrees divisible by four.
Every prime $(48q+11)/3<p<20q$ lies in its active coefficient range, and
the local diagonal entry fails only when the prime divides
$K_q=40q^2+44q+5$.  One CRT integer $c_q$ therefore makes



$$
h_q=B_q\bigl(1-c_q(1+x^2)^2xw_q\bigr)
$$



positive, integral, congruence-preserving, and simultaneously cancels both
moment residues at every nondegenerate window prime.

The exact padding maximum is
$(3/7)^{3q}(4/7)^{4q}$.  Its capacity exceeds the complete prime-window
product exponentially because



$$
7\log7-3\log3-4\log4-4>0.
$$



Consequently, if $D_q$ is the common reduced moment denominator,



$$
\gcd\!\left(D_q,\prod_{(48q+11)/3<p<20q}p\right)
 \mid40q^2+44q+5.
$$



Both canceled and total Chebyshev masses are $4q+o(q)$, so the fraction
canceled tends to one and the possible surviving mass is only $O(\log q)$.

~~~
e8cbb912fd801e83d31917ccbe24ff40dc936509e45bd4751ef11b2c7a454215  sources/common_kernel_positive_crt_asymptotic_full_window_cancellation.md
7f22f68204fbd302bdf73d1e07c32e6f487a814ef4d28f3a7aed986c96fa1e29  scripts/common_kernel_positive_crt_asymptotic_full_window_certificate.py
1328ed4a8d8eaf42f36e11752a3449df9a0db31edbb9aca7a2bd3f1a5d872a39  results/common_kernel_positive_crt_asymptotic_full_window_certificate.json
0d4277f69ba4fc92e7b0ebc9222cceb9172994f03dadfabfd169ad7b23fff008  results/common_kernel_positive_crt_asymptotic_full_window_hashes.sha256
~~~

The exact replay and an independent expansion pass.  This is a decisive
two-moment route obstruction, but it leaves the full correction output and
the arithmetic nature of $e+\pi$ unresolved.

## 2026-08-27 — Three consecutive zero digits on an ordinary Bessel branch

The attempted additive repair



$$
v_p(q_n)\leq \lceil\log_p n\rceil+2
$$



also fails.  On the ordinary $7$-adic root branch through $2$, an exact
$987$-digit integer $n_3$ satisfies



$$
7^{1167}<n_3<7^{1168},\qquad
 v_7(q_{n_3})=1171,\qquad
 q_{n_3}/7^{1171}\equiv1\pmod7.
$$



The compatible lift digits around the endpoint are



$$
(d_{1165},\ldots,d_{1171})=(1,3,4,0,0,0,4),
$$



so positions $1168,1169,1170$ form a zero run of length three.  The
Mahler-coefficient divisibility makes the verification modulo $7^{1172}$
finite at index $16436$, despite the enormous value of $n_3$.

~~~
3295664e80c0e3ee8a6b871fa73303de555548491b70a39077e7387a04dde2cf  sources/bessel_padic_index_triple_zero_counterexample.md
63be13d66517f6fdabed177a229626f215faa086356437fcc8520b336aae600d  scripts/bessel_padic_index_triple_zero_counterexample_certificate.py
c90fb481e9641c1c066280719a044675ed087acf868a891ade0bf4a0dfb09857  results/bessel_padic_index_triple_zero_counterexample_certificate.json
8088bcc99328176637a83dec7ce9139bc8bb02f394b96b323313954aaf0f6922  results/bessel_padic_index_triple_zero_counterexample_hashes.sha256
~~~

The frozen replay and an independent Newton-sum implementation agree.  This
disproves a fixed additive estimate only.  It neither proves unbounded zero
runs nor settles the uniform little-oh estimate, and it does not classify
$e+\pi$.

## 2026-08-27 — A local-method no-go theorem for Bessel zero runs

The known local features of the Bessel index interpolation—analyticity,
$1$-Lipschitz continuity, reflection, simple-root Hensel lifting, and an
exact affine lift-fiber law—cannot alone imply a zero-run bound.  Indeed, for
arbitrary increasing $N_j$,



$$
\rho=r+\sum_jp^{N_j},\qquad
 F_\rho(x)=(x-\rho)(x+\rho+1)
$$



has all those local features and satisfies



$$
v_p\!\left(F_\rho\left(r+\sum_{i\leq j}p^{N_i}\right)\right)=N_{j+1}.
$$



The zero gaps are therefore arbitrary.  The recursive choice
$N_{j+1}=N_jp^{N_j}$ realizes valuation mass asymptotic to the full
$n\log n$ scale.  The comparison function has a generally nonrational
$p$-adic coefficient and does not obey the Bessel difference equation, so
this is precisely a local-method obstruction, not a Bessel counterexample.

~~~
4372ccae9160d501a1c72631c1b4ce43865d29e6d36d88b11b192a7f7626ef03  sources/bessel_padic_local_zero_run_no_go.md
a3de0204026e19b10da91039d0347341d15367c33bd5c7e07b78c9c808c788a7  scripts/bessel_padic_local_zero_run_no_go_certificate.py
bec3c0854ba91906ca12e6827388b5f626d4e088b758bf7ba95c1629e94722de  results/bessel_padic_local_zero_run_no_go_certificate.json
2673e830c57748ec85d37d22ada1279e1d932cf11ca98b7790cd906ccda50e13  results/bessel_padic_local_zero_run_no_go_hashes.sha256
~~~

The exact symbolic proof and deterministic finite checks pass.  The surviving
Bessel task now requires global rational-height information from its specific
difference equation.  This note does not classify $e+\pi$.

## 2026-08-27 — Full fixed-correction CRT cancellation theorem

The positive common-kernel cancellation mechanism can cancel not only the two
defect moments but also the complete rational correction output attached to an
arbitrary fixed $K\in\mathbb Z[x]$.  Write



$$
u=1+x^2,\qquad {\cal T}P=(1-x)P'-xP,
 \qquad {\cal T}K=uG_0+\alpha+\beta x.
$$



For all sufficiently large $q$, finitely many nonnegative CRT coefficient
channels give an admissible $h_q$ of order $20q$ and degree
$48q+O_K(1)$.  If $D_q$ clears



$$
\int_0^1\frac{h_q-1}{u},\qquad
 \int_0^1x\frac{h_q-1}{u},\qquad
 \int_0^1\frac{{\cal T}(h_qK)-{\cal T}K}{u},
$$



then explicit fixed constants $C_K,\Delta_K$ satisfy



$$
\gcd\!\left(D_q,\prod_{(48q+C_K)/3<p<20q}p\right)
 \mid\Delta_K(40q^2+44q+5).
$$



Thus all but $O_K(\log q)$ of the window's $4q+o(q)$ Chebyshev mass is
canceled.  The proof decomposes
$(1+x)(1-x^2)^2K$ into four residue classes modulo four, reserves class one
for the moment equation, and uses classes two and three for the full output.
A coefficient-block lemma gives a uniform finite-field rank.  The degenerate
case is classified exactly as
$K=x(1-x)(1+x^2)^3R(x^4)$, where the full equation is automatic.

~~~
1071a65d0e799dd27754c6a117c573eee7170d7b430593c17da15fae0b1bc104  sources/common_kernel_positive_crt_full_correction_cancellation.md
64fd00d3c07ed7685362ee0df7c3872be7815c03360b9b6e67ae461d41644207  scripts/common_kernel_positive_crt_full_correction_certificate.py
20b7709fe330087fc44716c010950500d35ee5686c5787e281d09e2ff4bbbd53  results/common_kernel_positive_crt_full_correction_certificate.json
227318fce04df7c79dafb4a570ede3f0767c1c75b084aaaefe746b55a7c1a99a  results/common_kernel_positive_crt_full_correction_hashes.sha256
~~~

The deterministic replay, hash check, and an independent symbolic audit pass.
The theorem applies only to fixed $K$, so the native growing-degree and
primitive-content questions remain open.  It does not classify $e+\pi$.

## 2026-08-27 — Equal-secant condensation and transfer barrier

The two equal-parity centered-secant jets have been placed on an exact
contiguous/condensation lattice.  The canonical adjacent Padé pair satisfies



$$
\binom{X_M}{Y_M}=
 \begin{pmatrix}a_M&1\\a_My&b_M+y\end{pmatrix}
 \binom{X_{M-1}}{Y_{M-1}},\qquad a_Mb_M\ne0.
$$



Its symmetric square changes multiplier degree by two in each direction,
leaving a six-dimensional boundary quotient rather than a scalar recurrence.
An exact shear identifies the opposite parity as a flagged quadratic module;
the equal module embeds there with codimension three and basis determinant
$\pm b_M^{3m}$.

The equal determinant is the two-block Toeplitz minor $D_{m,m}^{(m)}$.
Desnanot--Jacobi supplies an all-parameter bilinear identity, but its smaller
minor has shift $m+1$, not the preceding equal shift $m-1$, and four
off-diagonal minors remain.  Their signs change on actual secant data.

Moreover, generic positive-node structure cannot close the gap.  For



$$
K_t(y)=y\left(\frac1{1-y}+\frac1{1-2y}+\frac{t}{1-3y}\right),
$$



one has



$$
\Delta_2(K_t)=(4t-1)(t^3-25t^2-13t+1).
$$



The value $t=1/4$ gives an exact singular jet with three positive simple
nodes, positive weights, coprime numerator and denominator, and ordinary
resultant $-4096$.  The special secant scan nevertheless certifies all
7,081 admissible determinants through $M=120$ as nonzero modulo
$2^{61}-1$; this remains finite evidence only.

~~~
4304030a5efa878aea3751bffb15f957a6dcec0b39e8ea24c80b3e7254812504  sources/centered_cosh_equal_jet_condensation_barrier.md
dcecfa5bcf000028eb994973b4a98618ac66ea50bbfd13e68e995c6bbfb8bbee  scripts/centered_cosh_equal_jet_condensation_barrier_certificate.py
6d4f4231ed0b4623289ede62bcea47b8ace626960b375f0727cc3c22dd280952  results/centered_cosh_equal_jet_condensation_barrier_certificate.json
c2e38c053485920cb7fb35d75d49fe9d5752eb36708b1138dbf8c0d786fac7b0  results/centered_cosh_equal_jet_condensation_barrier_hashes.sha256
~~~

The root replay and an independent symbolic condensation/counterexample audit
pass.  This is a structural barrier, not an all-parameter nonvanishing theorem
and not a classification of $e+\pi$.

### 2026-08-27 — Bessel all-integer jet identity and exact lift obstruction (item 105)

The Bessel denominator sequence $q_0=q_1=1$,
$q_n=(4n-2)q_{n-1}+q_{n-2}$ admits companion integer sequences $p_n,b_n$
for which the full family of local derivatives is



$$
f_p'(n)=(-1)^{n+1}(p_n{\cal K}_p-b_n),\qquad
 {\cal K}_p=\sum_{m\ge0}m!\in\mathbb Z_p.
$$



The proof includes a local-Tate-algebra convergence estimate for termwise
differentiation and the bound $0\le b_n\le4(n+1)p_n$.  On an ordinary
branch with $a=v_p(q_n)\ge1$ and unit derivative factor, the next compatible
root digit is exactly



$$
t\equiv(q_n/p^a)(p_n{\cal K}_p-b_n)^{-1}\pmod p.
$$



No $p^{2a}$ assertion is made.  Rational height control for the derivative
would already decide rationality of the fixed-prime Euler-series constant,
which is open.

~~~
fb68cec8ec01ca9dcfa39eb86af61f76a9bba07f18a6e955668ef2e90f89696e  sources/bessel_padic_all_integer_jet_euler_obstruction.md
0ede4cd80a7b343ca5c2e90c741d7b2629e41acb2b895aa27a10073da12f2755  scripts/bessel_padic_all_integer_jet_euler_obstruction_certificate.py
586de99873f278dce9af079db895937e8c1ffaadf48873027544d671c0466ea5  results/bessel_padic_all_integer_jet_euler_obstruction_certificate.json
b55fd4214f4207d6d4698b6a83ebb4bb474b09509cb42ac45e93beb8021520cf  results/bessel_padic_all_integer_jet_euler_obstruction_hashes.sha256
~~~

The root replay and manifest pass.  Item 105 isolates a global-method
obstruction; it supplies neither a zero-run estimate nor a classification of
$e+\pi$.

### 2026-08-27 — Central singular Bessel zero-run dichotomy (item 106)

Set $c=-1/2$ and $n_a=(p^a-1)/2$ for an odd prime.  The reflection
symmetry of the canonical interpolation makes its central local expansion
even.  If $f_p(c)\ne0$, then $v_p(q_{n_a})$ is eventually the constant
$v_p(f_p(c))$.  If $f_p(c)=0$, local factorization has even multiplicity
$\mu\ge2$, and



$$
v_p(q_{n_a})=\mu a+h\qquad(a\gg1).
$$



Thus a hypothetical central multiple zero creates a zero-digit run of length
$(\mu-1)a+h+O(1)$.  It is not proved to occur, and at fixed $p$ it is
still only logarithmic in the integer index.

~~~
f61c7e3005ee08d218bdc4150c0e34e9dcecc85119b74901f687aff9459d40e8  sources/bessel_padic_central_singular_zero_run_dichotomy.md
e36a44346586129d07691ccbf9a8e6a8f2247caf2b5bae94bac2314c371cccf4  scripts/bessel_padic_central_singular_zero_run_dichotomy_certificate.py
ee5417445c5bac26e8ffd710d36b8c1024dda1ebaa93a926496143eae681edcd  results/bessel_padic_central_singular_zero_run_dichotomy_certificate.json
7110154f392dd435ba554a6ec2f4239cebc766bc1eb933e01604bb0f81028e46  results/bessel_padic_central_singular_zero_run_dichotomy_hashes.sha256
~~~

The proof’s local analyticity dependency was rechecked against the exact
odd-prime analytic-order theorem, and the manifest and byte replay pass.  This
does not exclude the singular case and does not classify $e+\pi$.

### 2026-08-27 — Complete prime-window cancellation for growing corrections (item 107)

The fixed-correction CRT theorem now extends uniformly to every nonzero
$K_q\in\mathbb Z[x]$ with $\deg K_q\le12q-10$, with no coefficient-height
or content hypothesis.  A degree-adapted positive localizer has order $20q$,
degree $48q+13$, and cancels the complete prime window



$$
\frac{48q+\deg K_q+13}{3}<p<20q
$$



from the denominators of all three relevant correction integrals.  Since the
window is empty once $\deg K_q\ge12q-13$, this includes every nonvacuous
degree regime, including constant endpoint gaps.

The proof combines a consecutive Pascal-block determinant, a four-case
finite-field response rank argument, at most two CRT channels per prime, and a
uniform capacity proof using PNT entropy away from the endpoint and
parity/Brun--Titchmarsh at the endpoint.  The factorial-height native correction
is covered, and its localized polynomial has content one.

~~~
d1cd0012c8457ced0f064f23a8bf3256e91ff26730b8eaf5bcd7d984836f6ca7  sources/common_kernel_growing_correction_full_window_cancellation.md
8509d260b7d3ceaa879d88035a6b54802a08514dafe587be01694cb6d9c544f1  scripts/common_kernel_growing_correction_full_window_certificate.py
43e0146200996bcbc67fee8d47598abb6da10a6c32051f021afdbead43fb1f30  results/common_kernel_growing_correction_full_window_certificate.json
ef4c51baa0a9a2660be5e1360682f4bcb522354e1af8a6c87c6d3b9bfa057fc6  results/common_kernel_growing_correction_full_window_hashes.sha256
~~~

The root replay regenerated the identical JSON in 1.4 seconds with 22,488 KiB
peak RSS.  A separate symbolic audit checked 450 Pascal determinants and the
base padding identity.  The remaining native-family issue is analytic sign and
decay, not this denominator window; no classification of $e+\pi$ follows.

### 2026-08-27 — Finite shift--first-jet aggregate no-go (item 108)

The full finite shift and first-jet algebra of the Bessel interpolation reduces
integrally to four boundary generators $F,G,X,Y$.  A formal order $s$ on
the root locus $F=0$ is exactly an $F^s$ factor.  After integer-center
specialization and use of the all-integer jet theorem, any prime-independent
integer obtained by cancelling the Euler-series indeterminate is therefore
divisible by $q_n^s$, and a nonzero such integer has logarithmic height at
least $s n\log n+O(sn)$.

This proves that the proposed aggregate rational product formula gains no
valuation-to-height ratio inside this formal algebra.  A nonconstant dependence
on the Euler-series indeterminate instead leaves unrelated local $p$-adic
data and requires a new global theorem.

~~~
90f69f0589392c84c4205ac2b95b5375a86e212ae7e33490708186d9a6aef45a  sources/bessel_aggregate_shift_jet_product_formula_no_go.md
8b7f1368de6a442a95cae1bc1c3d4762c43317af81c3d7a478e33f2921e45c7c  scripts/bessel_aggregate_shift_jet_product_formula_no_go_certificate.py
c94bf05c654c1fa272b80d9ebddedc7ed2bb70d88c2be044a774fdb34a20fe52  results/bessel_aggregate_shift_jet_product_formula_no_go_certificate.json
11ee42a3940770707892dba303e502b8f4e9000d02f1db39767e9e41b82bf617  results/bessel_aggregate_shift_jet_product_formula_no_go_hashes.sha256
~~~

The manifest and byte-identical replay pass.  Independent checks covered both
positive and negative shifts and unrelated formal cofactors.  The theorem is a
scoped no-go, not a valuation bound and not a classification of $e+\pi$.

### 2026-08-27 — Actual centered-secant equal-jet sign barrier (item 109)

Exact rational reconstruction of the canonical Padé denominators for
$1/(2\cosh\sqrt x)$, followed by independent primitive integer clearing,
gives signs $+,-,-,+$ for $\Theta_6(X_M,Y_M)$ at
$M=6,7,14,15$.  Each corresponding $\Theta_4(X_{M-1},Y_{M-1})$ is
positive, so the six-dimensional condensation quotient itself changes sign.

The witnesses disprove every proposed canonical factorization whose missing
factor is uniformly a positive resultant/Gram determinant or a nonempty sum
of nonnegative Cauchy--Binet terms.  A sign-changing prefactor remains possible,
and all-parameter determinant nonvanishing remains open.

~~~
45bfb6497840dc9f9e0a997091c56d104d66157a992c57f598c31bd1001da218  sources/centered_cosh_equal_jet_actual_sign_barrier.md
5c5b94902e124fa52fdbd9e5d7141a3355313091aeb4828e03375f63dce5c701  scripts/centered_cosh_equal_jet_actual_sign_barrier_certificate.py
179d8366d87d48b9cd25761f1be71cbdc027b4f22fb0ad6dd7cb25b07c6cbd79  results/centered_cosh_equal_jet_actual_sign_barrier_certificate.json
dda7ad5eb73c802a0688d4cddea9a294ff943c29575ebc3f8a43f44d765148c0  results/centered_cosh_equal_jet_actual_sign_barrier_hashes.sha256
~~~

The deterministic replay and manifest pass.  A separate SymPy solve and
determinant calculation reproduced the decisive positive and negative hashes
and their positive lower minors.  This does not classify $e+\pi$.

### 2026-08-27 — Large-prime Bessel unit-cancellation frontier (item 110)

An elementary AM--GM size argument proves $v_p(q_n)\le n-1$ for every
$p>2n$.  This is uniform but still linear.  All individual terms in the
terminating factorial formula are $p$-units, so the remaining depth is
entirely cancellation.

At the boundary $p=2m+1$, pairing the factorial factors gives the exact
all-power expansion



$$
(-1)^m q_m=\sum_{\ell=0}^m(-p^2)^\ell S_{m,\ell},
$$



and hence an exact truncated congruence criterion for every desired valuation
depth.  Reflection kills the first index slope but does not control the
higher layers.  Separately, $q_8=13^2\cdot1846921$ refutes exponent one in
the range $n/2<p$.

~~~
baa384012e6f56f3437de42eb7614e0475763a883529fbfda97120497c97b11d  sources/bessel_large_prime_unit_cancellation_frontier.md
f7044fb57a01c7ea1198441833ce10d5e1c0c8613d72a3463da745ce50f0d29c  scripts/bessel_large_prime_unit_cancellation_frontier_certificate.py
58dda46677fc6c1fee1c30e2d865f055a9a3c94af9c74fac88845ea55fa81005  results/bessel_large_prime_unit_cancellation_frontier_certificate.json
e1c425fea9ab46f11686b52126ea76dcf70720704d949cec9d070f0bb2d93291  results/bessel_large_prime_unit_cancellation_frontier_hashes.sha256
~~~

The byte replay, manifest, and independent checks pass.  This is a precise
large-prime reduction, not the needed little-oh theorem and not a
classification of $e+\pi$.

### 2026-08-27 — Native sign control and exact Roth threshold (item 111)

For every admissible integral localizer in the native Taylor--Robin family,
one-signedness forces nonnegativity and factorial-quarter-root degree:



$$
(\deg h)^4\ge\frac{(N!-\Re(1-i)^N)(N+1)}{54e}.
$$



An exact integrating factor proves the endpoint envelope and also fixes the
raw positive weighted integral between $1/(N+1)$ and $5e/(N+1)$.
After honest denominator clearing and content removal, the associated reduced
rational approximation has error between
$1/((N+1)N!)$ and $5e/((N+1)N!)$.

Consequently a reduced denominator at most $(N!)^{1/2-\delta}$ infinitely
often would contradict every algebraic possibility by rational separation and
Roth.  Equivalently, the remaining arithmetic target is
$g/D\ge(N!)^{1/2+\delta}$, in addition to constructing a sign-controlled
localizer at all.

~~~
7a06684887367ce114e0c613e58c5dc1db688678099b0d3ed02b35c9c4b789e2  sources/common_kernel_native_sign_endpoint_degree_barrier.md
16f125838a585724b1e312b8bb6d0f8a7808c24883052c4773e33851b4438675  scripts/common_kernel_native_sign_endpoint_degree_certificate.py
4a9604b3f3adb787b66ce9733dc7de91c74226380734a42bc2e6fa687af15384  results/common_kernel_native_sign_endpoint_degree_certificate.json
400b4e5ae612683394a657c69f6aee4e1e2369b0d518f8c6027d51aa26c3efc3  results/common_kernel_native_sign_endpoint_degree_hashes.sha256
~~~

The root replay, manifest, and line audit pass.  This is the sharpest current
positive criterion in the common-kernel route, but its two decisive hypotheses
remain unproved; no classification follows yet.

### 2026-08-27 — Tangent-survivor exponential lower bound (item 112)

Writing the reduced adjacent tangent-number ratio as $P_r/Q_r$, the exact
identity



$$
\frac{P_r}{Q_r}=\pi^2\frac{A_r}{A_{r+1}},\qquad
 A_r=\sum_{j\ge0}(2j+1)^{-2r},
$$



gives a positive error of order $9^{-r}$.  Zudilin's upper bound
$5.09541178\ldots$ for the irrationality exponent of $\pi^2$ transfers
this into the individual all-index lower bound



$$
\liminf\frac{\log Q_r}{r}\ge\frac{\log9}{5.095412}.
$$



This rules out $\log Q_r=o(r)$ on every infinite subsequence.  There is
also a self-contained adjacent argument: strict moment log-convexity and the
exact tangent-number 2-adic valuation imply that the positive cross
determinant is even but not divisible by four, forcing
$Q_rQ_{r+1}>4\,9^r/(5\pi^2)$.  Exact adjacent irregular pairs and Kummer
congruences show why universal odd coprimality cannot supply the still-missing
factorial-scale bound.

~~~
8dc9acde0025c4038b1b7e486ee327b6f077dae737e828c111ec066e7fcf0439  sources/root_unity_tangent_survivor_exponential_no_go.md
59dbabc81c1e784ade8115a1cec509a9fb4a5eba37909237d2854e1384db19b2  scripts/root_unity_tangent_survivor_exponential_no_go_certificate.py
1e4e1b379087e37938918802a5040ab54841540b158acff537f64ca6ed594378  results/root_unity_tangent_survivor_exponential_no_go_certificate.json
71e0b42a14b2bbcc3dbfc104824048a51f75a1c9c97296da6f2c7c33acbd2e33  results/root_unity_tangent_survivor_exponential_no_go_hashes.sha256
~~~

The line audit, primary-source constant check, deterministic replay, manifest,
and control-byte scan pass.  The result closes the $o(r)$ survivor route but
does not prove an $o(r\log r)$ gcd estimate and does not classify $e+\pi$.

### 2026-08-27 — High-origin-order Roth-content obstruction (item 113)

The native quotient polynomial has an exact forced prefix.  If a localizer has
degree $d$, origin order $r$, and a prime satisfies



$$
\max\{N,(d+1)/2\}<p<r,\qquad
 p\nmid N!-\Re(1-i)^N,
$$



then the coefficient in degree $p-1$ is $\pm M_N$, and it is the unique
source of a $p$-denominator in the monomial integral.  Since the base
coordinate is $p$-integral, $p$ occurs to exact exponent one in the
complete reduced denominator.

Combining this all-parameter survival law with the sign-forced
factorial-quarter-root degree and PNT proves, for
$r\ge(1/2+\eta)d$,



$$
\log D\ge(\eta-o(1))d,\qquad
 \log(g/D)\le-(\eta-o(1))d.
$$



Thus the exact content threshold sufficient for Roth fails exponentially for
all high-origin-order localizers, including the canonical sparse family.  The
known nonlocal CRT construction has ratio $5/12<1/2$ and is not addressed.

~~~
d6d46ba4d8f87268062e027c76ae90b71e45e6e9c80685770e9517aafe741685  sources/common_kernel_roth_high_order_content_obstruction.md
0b0e139df870e3f262f334c0efd278a28a065c3fb85d87326db43bfd96729b8e  scripts/common_kernel_roth_high_order_content_obstruction_certificate.py
272cd4b67284f46d810ff9193b37abc0356848196e1f0e8203d9a9bd3d69516e  results/common_kernel_roth_high_order_content_obstruction_certificate.json
6fe2ebc3013eb81eb2284f44b8e07d03784d048ce76938877e6363b91386686b  results/common_kernel_roth_high_order_content_obstruction_hashes.sha256
~~~

The manifest and deterministic replay pass.  Forty-four independent exact
checks on perturbed admissible-congruence localizers verified the predicted
prime survival outside the certificate's sparse test family.  No
classification follows.

### 2026-08-27 — Endpoint-layer sign obstruction for the CRT family (item 114)

The complete prime-window cancellation family from item 107 is now
analytically excluded in its native specialization.  Its base localizer has,
at $t=1/(5q)$, an exact logarithmic slope between $3/t$ and $5/t$.
This makes the native residual negative by an amount uniform in both
coefficients $-I_N$ and $M_N/2$.

The CRT correction cannot compensate: its coefficient product has logarithm
$4q+o(q)$, whereas the endpoint padding contributes
$(4/(5q))^{4q}$.  The correction and its scaled first derivative are
therefore $\exp(-4q\log q+O(q))$.  The residual remains negative at the
endpoint-layer witness and is positive at $x=0$, so it changes sign for
every sufficiently large $q$, uniformly for $N\ge2$.

~~~
2abd83feaca1058a0c8a6723a4a66e55bfcbddc152985fb3ddebb1722a7693d1  sources/common_kernel_native_crt_endpoint_layer_sign_obstruction.md
0b77e84e1afa44993878dec140db7c6146d28efbeace227d92282c0466cca535  scripts/common_kernel_native_crt_endpoint_layer_sign_obstruction_certificate.py
ffa71b6f020e5fd6efdb3188feecf3b16992aa38c93a5ffdb21b621549bc280b  results/common_kernel_native_crt_endpoint_layer_sign_obstruction_certificate.json
35618f77fbf3a922cfb8ec1309950ac908a0daf901c4498c707d17c938e827ee  results/common_kernel_native_crt_endpoint_layer_sign_obstruction_hashes.sha256
~~~

The exact slope, perturbation constants, manifest, deterministic replay, and
control-byte scan pass.  This resolves the existing CRT family only; it does
not rule out a different low-order construction and does not classify
$e+\pi$.

### 2026-08-27 — Exact native sign-existence classification (item 115)

The native analytic problem now has a complete answer: an admissible integral
one-signed localizer exists for $N\ge2$ if and only if
$N\not\equiv5,6,7\pmod8$.  The construction uses the integrating-factor
coordinate $G=\mu H$, an increasing left profile, and the right profile



$$
G_R=\frac{J^2}{J+1/(eA^2)}.
$$



Their first crossing is smoothed by an explicit smooth minimum whose derivative
is a convex combination of the two branch derivatives.  The quotient
$(H-1)/(1+(1-t)^2)^2$ has integral Taylor jets through order three at both
endpoints.  An exact integral Hermite interpolant reduces the approximation
step to Draganov's simultaneous integer Bernstein theorem, producing genuine
ordinary-coefficient polynomials in $\mathbb Z[t]$.

Endpoint expansions preserve $0\le H\le1$, and a separate fourth-order
perturbation estimate handles the $I_N=0$ residual.  Thus the previous
endpoint obstruction is the only analytic existence obstruction when degree
and height are unrestricted.

~~~
283641248f64788c69516874407882efebd5393871ebc23a98a71bd66f30ffbc  sources/common_kernel_native_sign_integer_bernstein_existence.md
e927357755a9449cf1898bd682c75e6d9ae86a08ea24ce04756daf62d5a5b1e8  scripts/common_kernel_native_sign_integer_bernstein_certificate.py
0a6abc5d0c8b11c344cf9c74df93381fd60bc14215848b2ca8949d612891d4ab  results/common_kernel_native_sign_integer_bernstein_certificate.json
337f9276d17304927c34427277fbc62f8bb99642cf525a69aa01c6eed818a2f9  results/common_kernel_native_sign_integer_bernstein_hashes.sha256
~~~

The smoothing argument, primary approximation theorem, endpoint jets, replay,
manifest, and control-byte scan pass.  No useful degree or output-content
bound follows, so the arithmetic classification remains open.

### 2026-08-27 — Four-point exclusivity in the Bessel large-prime window (item 116)

The affine anti-period lift and exact reflection modulo $p^2$ now combine
into a complete orbit table.  For $r+s=p-1$, the four quotient residues are



$$
(c,c-\delta,-c-\delta,-c+2\delta).
$$



If the slope is nonzero, their four zero conditions are distinct for
$p\ge5$; consequently three representatives have valuation exactly one
and at most one can have greater depth.  A zero slope gives an all-four
square-threshold dichotomy, and reflection forces every central orbit onto
that singular branch.  The proof is affine throughout and never assumes
Hensel simplicity.

Every index with $p>n/2$ lies in one of these four-point or central
two-point orbits.  The remaining large-prime obstruction is therefore
localized to one exceptional representative in each ordinary orbit and to
fully branching singular orbits.

~~~
1e8fed0a5ab04c97c4e0749d40304d6398f9fd32d55c7b49085fb4b4ecca4e41  sources/bessel_large_prime_four_point_exclusivity.md
9a30c35da6a3132406bc5998c10a05f9ed2f4a47510e61cdce4ba7dabd9c29e3  scripts/bessel_large_prime_four_point_exclusivity_certificate.py
ce0a028b2170b8291e3bc42dd088c5bfdcfda2a89b4cf055b550a60623d1c190  results/bessel_large_prime_four_point_exclusivity_certificate.json
a13749e329b3f14381f0c5d9db8ca5239fe9ef7735ffdd071fd40c3531704eea  results/bessel_large_prime_four_point_exclusivity_hashes.sha256
~~~

The manifest pins the two recurrence dependencies, and the exact replay and
control-byte scan pass.  The finite $p<10000$ scan sees only the known
$(13,8)$ square and no cube, but no finite observation is promoted to an
all-prime exponent bound.

### 2026-08-27 — Exact native output moment and Farey isolation (item 117)

The complete dependence of the native rational coordinate on the integer
localizer is now a single weighted moment.  For
$h=1+(1+x^2)^2q$, $Q(t)=q(1-t)$, $a=-I_N$, and
$b=(N!-R_N)/2$, exact integration by parts gives



$$
\rho_{N,h}=\rho_{N,1}-5(a+b)
 -4\int_0^1(a+bt)t(2-t)^2Q(t)\,dt.
$$



The one exponential and four rational boundary terms have been tracked
separately.  Expanding a raw Bernstein channel produces four explicit beta
moments, and $\operatorname {lcm}(1,\ldots,n+5)$ clears every response.  This
yields a replayable integer numerator, reduced denominator, and final
$N!$-content ledger in the correct order.

A residue-constrained rounding theorem proves that arbitrary independently
prescribed channel residues modulo $m_n$ retain $C^3$ approximation when
$m_n=o(n)$, and an endpoint-channel counterexample makes that uniform scale
sharp.  Since the full response-clearing LCM is exponential, coefficientwise
full-modulus rounding is excluded; adaptive sparse congruences are not.

Finally, the sign-output error interval has length
$(5e-1)/((N+1)N!)<1/N!$ for $N\ge14$.  Farey separation therefore permits
at most one reduced candidate of denominator at most $\sqrt{N!}$, exactly
the region containing every Roth-scale target.  The candidate may or may not
exist.

~~~
ebb50316d59ff22aa49512372547311fd5f36d24dd88825fcdf6b5ee0090b529  sources/common_kernel_native_output_bernstein_congruence_isolation.md
b5d97041916bf6401df95dbed4427fa910810a6f984f4b977bc6800a587ebca7  scripts/common_kernel_native_output_bernstein_congruence_certificate.py
d9e9defc6276f6efc9777511de9a3f779f893b65a38de7a4bf448dd8e5669762  results/common_kernel_native_output_bernstein_congruence_certificate.json
559cc412db81ed449d4255654ad370f44a8ceb4d8acdce234a7f607d448ffcb7  results/common_kernel_native_output_bernstein_congruence_hashes.sha256
~~~

The line audit, fresh replay, dependency hashes, and control-byte checks pass.
The result isolates the required arithmetic hit but supplies neither that hit
nor a classification of $e+\pi$.

### 2026-08-27 — Fourth anti-period and cube-threshold exclusivity (item 118)

For every prime $p\ge5$, the Bessel denominator recurrence has the exact
next-layer congruence



$$
\sum_{j=0}^4\binom4j q_{n+jp}
 \equiv12p^2q_n\pmod {p^3}.
$$



The proof propagates the fourth binomial sum by the original recurrence.  Its
two initial values are obtained from the Mahler coefficients:
$A_{4p}\equiv12p^2$ and
$A_{4p+1}\equiv-24p^2\pmod {p^3}$; every interior operator term has enough
combined binomial and Mahler valuation to disappear.

On a root fibre the signed values are consequently cubic in the translate
parameter modulo $p^3$.  An ordinary fibre leaves at most one cube
representative.  If the first lift is all-square, cube divisibility is the
zero set of an explicit cubic $P_r$ over $\mathbf F_p$, giving at most
three representatives unless the four Newton coefficients all vanish.
Reflection identifies the paired polynomial with $P_r(-1-T)$.  This gives
at most six cubes across a full noncentral pair, and at most three among the
four representatives below $2p$, unless all four force the whole fibre.
The central invariant polynomial is quadratic after translation.

~~~
7fe7bd5b2cef3dcb2a12f49c0c620d8d173d818774701a06f1527d80d574a6be  sources/bessel_prime_cube_fourth_antiperiod_exclusivity.md
6e4f612c0d1485de3858d1a9a13320cad766416737f281179c08860eddb30a6f  scripts/bessel_prime_cube_fourth_antiperiod_exclusivity_certificate.py
b60d7edd95835764161553ea68d377f2edafdda321b81137b0d19b45eb139dec  results/bessel_prime_cube_fourth_antiperiod_exclusivity_certificate.json
a46f0ca172db4ff4a8e41cae15bf32b9d61b95f7a71644bfe59b6c4594a854e6  results/bessel_prime_cube_fourth_antiperiod_exclusivity_hashes.sha256
~~~

The recurrence, Mahler eliminations, Newton divisions, and reflection counts
were independently audited, and the exact replay passes.  The finite scan has
no all-square singular example and is not used to infer that theorem.  The
ordinary exceptional value and identically-zero fibre remain unresolved, so
the target valuation estimate and the classification of $e+\pi$ remain open.

### 2026-08-27 — Effective native integer-Bernstein construction (item 119)

The analytic sign construction has been quantified from endpoint profile to
integer polynomial.  The optimized parameter
$\ell=A/\gcd(A,b)$, $\epsilon=(eA\ell)^{-1}$ retains integral endpoint
jets and substantially improves the $a=0$ classes.

For a $C^5$ zero-jet remainder, a direct third-difference calculation gives



$$
\|(\widehat B_nr)'''-r'''\|_\infty
 \le
 \frac{3M_3+\tfrac{57}{2}M_4+\tfrac14M_5}{n}
 +\frac{96}{n-3}.
$$



The first and last four rounded channels vanish exactly under the stated
degree condition.  A one-sided smooth minimum then provides an explicit
global sign tolerance.  Its smallest margin contains
$\theta_N^N$, with $\theta_N\asymp(N!N)^{-1/2}$, yielding



$$
\log n_{\rm suff}
 \le\left(\frac12+o(1)\right)N^2\log N.
$$



The coefficient height is at most $n\log6+O(N\log N)$ logarithmically, and
the exact four-beta output has reduced denominator dividing the LCM through
$n+5$.  These bounds have the wrong direction for primitive content:
neither $D$ from below nor $g=\gcd(N!,c)$ in either useful direction is
controlled.

~~~
0f5f69dcfd1ce4c2258c0333fe60f20275b1e21591c0e5e0c55bcea05a7acbbb  sources/common_kernel_integer_bernstein_quantitative_arithmetic_audit.md
17fcb7a1ff987981934c3852b7620af38073046de4a233ef613004e1af80c805  scripts/common_kernel_integer_bernstein_quantitative_arithmetic_certificate.py
5ff1c6949bca45a7d4f3bd5c0eb107bf356ab52107949c7aa83a7dec061a895d  results/common_kernel_integer_bernstein_quantitative_arithmetic_certificate.json
80ac4f4e108fd87b7549499abe702e0ddee83c45450ba338e820d18a5ab8437d  results/common_kernel_integer_bernstein_quantitative_arithmetic_hashes.sha256
~~~

The smoothing, approximation constants, coefficient estimates, and exact
moment ledger were independently checked and replayed.  The construction is
now effective, but the arithmetic classification remains open.

### 2026-08-27 — All-even Bessel anti-period hierarchy (item 120)

The fourth anti-period is the second case of a complete hierarchy.  For
$p>2k$,



$$
S_{2k}(n)=\sum_{j=0}^{2k}\binom{2k}{j}q_{n+jp}
 \equiv\frac{(2k)!}{k!}p^kq_n\pmod {p^{k+1}},
$$



and $S_{2k-1}(n)\equiv0\pmod {p^k}$.  Recurrence induction reduces the
even law to two initial values.  Expanding
$((1+\Delta)^p-1)^{2k}$, every nonendpoint term has combined valuation at
least $k+1$; the surviving Mahler coefficients give the exact constant and
shifted sign.

The signed translate sequence is consequently a degree-$(2k-1)$ Newton
polynomial modulo $p^{k+1}$.  On any fibre wholly divisible by $p^k$, its
divided reduction has at most $2k-1$ next-level roots unless it is zero and
the full fibre survives.  Reflection gives the paired and finite-window
counts; central symmetry removes the odd top degree.

~~~
c0c834ca8851ddc8dba9edbc9ec74461c0d3aa1b553f79c2320b3d083a0c37de  sources/bessel_all_even_antiperiod_higher_threshold_exclusivity.md
b2f83c96c0166785d491ee0b2d776e67408e0b74f1211b6ea4e862216868c1f3  scripts/bessel_all_even_antiperiod_higher_threshold_exclusivity_certificate.py
53034eebf24139553ad006adedb9afab004e371558844166b1864a106cdce4dc  results/bessel_all_even_antiperiod_higher_threshold_exclusivity_certificate.json
a2ca08905562be561617da55d19620f829bef02ee303473fdb39bebe84f2d899  results/bessel_all_even_antiperiod_higher_threshold_exclusivity_hashes.sha256
~~~

The full valuation-floor and endpoint-sign audit passes, as does the exact
replay.  There are no qualifying full fibres for $k\ge2$ in the replay,
which is recorded only as scope.  The ordinary lift can still be arbitrarily
deep under the proved laws, so no denominator-height or $e+\pi$ conclusion
follows.

### 2026-08-27 — Exact rational-moment integer approximation (item 121)

The remaining qualitative congruence constraint in the native sign
construction can be imposed exactly.  For



$$
\ell(f)=4\int_0^1(a+bt)t(2-t)^2f(t)\,dt,
$$



every smooth rational-moment profile with integral endpoint jets through
order three has integer-polynomial $C^3$ approximants with the same jets
and exactly the same moment.

The first ingredient is the full image theorem
$\ell(B\mathbb Z[t])=\mathbb Q$ for every nonzero integer polynomial $B$.
For a general integer weight, its monomial moments are
$F(n)/\prod(n+j+1)$; taking $n=p^k-c$ gives arbitrarily negative
$p$-adic valuation at every prime, and additive Bezout identities recover
all rational numbers.

The second ingredient is the differential kernel



$$
{\cal D}S=2W'S+WS',\qquad
 \ell({\cal D}U)=4[W^2U]_0^1.
$$



After one exact affine moment match, the zero-moment remainder determines
$S=(\int_0^tWg)/W^2$.  Carefully weighted integer-Bernstein rounding,
including the omitted endpoint channels, gives ${\cal D}S_n\to g$ in
$C^3$ with exact zero moment and exact endpoint jets.

Rational grids would turn output intervals of width $w_N$ with
$Nw_N\to\infty$ into $D=o(N)$, enough for an irrationality
contradiction.  The native global range is only $O(1/N)$, so this
sufficient condition cannot occur.  A width $c/N$ also cannot by itself
force square-root denominators because it may lie in a one-sided Farey gap.

~~~
61e396ba87dd73f66a5e7f322c13498aab2b9d0bcd6479895016753014e1e18e  sources/common_kernel_native_exact_moment_integer_approximation.md
9abb9e47a0719f0c0d2b64aa13c7d95c7f3579919e96630c89ab8e5e17fba1e5  scripts/common_kernel_native_exact_moment_integer_approximation_certificate.py
343a71d530acb7dd3681f38d26213f60dd8b8da8a4eb7216eaf6b482a2fc53ae  results/common_kernel_native_exact_moment_integer_approximation_certificate.json
aa35956007909d980f86d43909eaad180d56b9c80a654059425513a1debbb6b9  results/common_kernel_native_exact_moment_integer_approximation_hashes.sha256
~~~

The full image, endpoint, weighted derivative, kernel, and Farey arguments
were audited and replayed.  This resolves exact-moment approximation but not
the arithmetic location needed for primitive decay or a classification of
$e+\pi$.

### 2026-08-27 — Sharp native output diameter (item 122)

The native positive form has the probability-density representation



$$
{\cal L}_N(G)=\int_0^1R(t)(w(t)+G'(t))\,dt,\qquad
 R(t)=e+\frac{4e^t}{t^2-2t+2},
$$



where the density is strictly positive and has fixed mass
$B_N=\int_0^1e^{-t}t^Ndt$.  Since $R$ increases from $e+2$ to $5e$,
every output lies in $((e+2)B_N,5eB_N)$.

An explicit compact mass transfer preserves strictness, the range barrier,
and identical integral endpoint germs.  Letting its early support approach
zero and its late cutoff capture the boundary layer at one proves



$$
\lim N{\cal W}_N=4-\frac2e.
$$



A fixed construction gives the explicit lower width $c_*/N$ for all
admissible $N\ge8$.  Conversely, the universal range proves that no native
family can satisfy $Nw_N\to\infty$.  The sharp width constant still misses
the raw positive-output constant, so a one-dimensional grid argument cannot
close the rational case.

~~~
7d4e9c5dc30c449ca369d52a3fb06e52ff681aedeb47b0dce45b2fc5239f36cc  sources/common_kernel_native_sign_output_range_sharp_width.md
1ee9c9572e165934294a0c5bd32fb4521f7dde406eaeae73b4d970a7870c1615  scripts/common_kernel_native_sign_output_range_sharp_width_certificate.py
25848e5590758fa622d14d45cb32b30a5e29d7c3022aff99de776f6946ec368b  results/common_kernel_native_sign_output_range_sharp_width_certificate.json
de1348caca545595e79ddc00929ece5d0ef7f18fb7eeb3f979beb26f2b766677  results/common_kernel_native_sign_output_range_sharp_width_hashes.sha256
~~~

### 2026-08-27 — Exact ordinary Bessel harmonic expansion (item 123)

For every large-prime reflection orbit, each terminating hypergeometric term
was factored into its multiples of $p$, a $p$-unit factorial quotient,
and elementary symmetric sums of reciprocal nonmultiples.  This gives an
exact finite all-power expansion



$$
T_k(r+pZ)=p^\nu U\Phi(Z)
 \sum_{\ell\ge0}p^\ell Z^\ell E_\ell
$$



in $\mathbb Q[Z]$.  The summed $j$-th layer is $p$-integral of degree at
most $j+1$, with constant layer $q_r$.  On an ordinary root the first
layer is $Z\delta\pmod p$, so the unique deeper lift is an explicit finite
harmonic-unit noncancellation problem.

The countermodel $G(T)=p(T-Z_*-p^{A-1})$ simultaneously satisfies every
currently used hierarchy, reflection, ordinary slope, four-point
exclusivity, permitted layer degrees, and factorial-scale height, while its
exceptional valuation is $A$.  With $A\asymp p$, this proves that a new
Bessel-specific coefficient invariant is necessary.

~~~
28a91596edafac946448ea68f4c95dfdcd94e63bcf7586394c464a69d6a76e3d  sources/bessel_large_prime_ordinary_harmonic_expansion_barrier.md
6d0416020a1d1b1f1cfd9093c305b3826b6a32a13f20aea70a72a1017e4ff2c9  scripts/bessel_large_prime_ordinary_harmonic_expansion_barrier_certificate.py
35d48aa29c9ed42a00ab07f407a03f2193cfef72c2109891874a0f2e831a2ade  results/bessel_large_prime_ordinary_harmonic_expansion_barrier_certificate.json
8b3762971ff913e67e26e2cf82baffc4ecfb41b9bcbd79d23cbcad167b6d5348  results/bessel_large_prime_ordinary_harmonic_expansion_barrier_hashes.sha256
~~~

### 2026-08-27 — Finite simultaneous exact moments (item 124)

Wronskian formal-adjoint operators isolate the coordinates of every finite
integer-weight moment map.  Together with the scalar full-image theorem they
prove



$$
{\boldsymbol L}(\mathbb Z[t])={\boldsymbol L}(\mathbb Q[t]),
$$



including inside arbitrary endpoint-zero ideals.

For two independent native weights the common kernel factors through two
first-order operators.  Their cross-weight is
$-\Delta t^2(2-t)^4$, with no interior zero, and a weighted fifth-derivative
integer-Bernstein estimate gives simultaneous exact-moment $C^3$
approximation.  A common strict smooth profile for any finite sign-possible
system is constructed using the shared $1/t$ descent allowance.  For an
independent pair, two compactly supported bump directions have invertible
moment matrix, allowing both moments to be made rational without sacrificing
strictness before integer approximation.

This is qualitative freedom, not a denominator theorem.  The moment pair is
locally fully variable, and eliminating the common target across indices
introduces a factorial ratio.  No $o(N)$ denominator or primitive-content
bound follows.

~~~
73704b5408699aaff3c3254f8e6f8c10c321d22ad06952135aba192591c77d5a  sources/common_kernel_finite_multimoment_exact_approximation.md
738aa3a7ad75ffaea71fdefc95ebed2fa038696c887af57bf3e56e1e7c15ca86  scripts/common_kernel_finite_multimoment_exact_approximation_certificate.py
a50ae12cc7b9e137b5e50745e1d50b8700d1ce36e31d2be0425ed2d994c6a89a  results/common_kernel_finite_multimoment_exact_approximation_certificate.json
b53b8e6f1855fe3eb7ef1b1eae1c303fad3b9cd5344462616606794fd0d9ce6d  results/common_kernel_finite_multimoment_exact_approximation_hashes.sha256
~~~

The three new packages passed independent line audits, deterministic replays,
and frozen-manifest checks.  None is being promoted to an irrationality,
algebraicity, or transcendence proof.

### 2026-08-27 — Exact fixed-index native output closure (item 125)

The fixed-mass bound from item 122 is not the complete pointwise geometry at
a fixed index.  Integrating $G'>-e^{-t}t^N$ backward from $G(1)=0$
gives $G(t)<J(t)=\int_t^1e^{-s}s^Nds$, in addition to $G<\mu$.
The two obstacles cross exactly once.  Therefore, with
$E_N=\min(\mu,J)$,



$$
\{{\cal L}_N(G)\}=({\cal L}^{\min}_N,{\cal L}^{0}_N),\qquad
 {\cal L}^{\min}_N={\cal L}^{0}_N-\int_0^1R'E_N.
$$



A flat perturbation of the increasing branch, a rationally parameterized
decreasing branch, and local smooth-min regularization approach the lower
endpoint with integral jets.  A two-corner cap approaches the upper endpoint
with the same endpoint germs, and convex interpolation fills every interior
value.  The limiting lower density has positive mass away from zero, proving
${\cal L}^{\min}_N>(e+2)B_N$.

The translated-coordinate formulas cancel the $e$-term symbolically and
are certified by rational exponential brackets, Machin bounds for $\pi$,
and an exact four-step reciprocal series.  Crucially, a coordinate
$c/D$ induces the reduced approximation denominator
$Q=N!D/\gcd(N!,|c|)$.  Once this conversion is made, every earlier
coordinate-grid row fails $Q\le\sqrt{N!}$.  A distinct exact scan finds six
genuine finite hits at $N=25,33,43,88,164,331$; no infinitude or Roth gain
is inferred.

~~~
c9a018f47b54ed565c958da3dbd53b38b912238b63e56234dfb8a9e68ec99d42  sources/common_kernel_native_fixed_N_output_closure.md
75631e0c53a5851bc36f77d592c2c4737cdd4b4ebe8bc5a637062781e93be875  scripts/common_kernel_native_fixed_N_output_closure_certificate.py
a1bb13e6083592872cc0b90d466153e5cb5e76b0f3d685d218ca18cfb4b5ee45  results/common_kernel_native_fixed_N_output_closure_certificate.json
a5c167be7be4ee5924131c4e0dfa2f97ac64232b5a8c90242e6fb064c2d8fcab  results/common_kernel_native_fixed_N_output_closure_hashes.sha256
~~~

Both final replays were byte-identical, the manifest passes, and the proof
was independently line-audited.  This resolves the exact fixed-$N$ output
closure but not the arithmetic classification of $e+\pi$.

### 2026-08-27 — Adjacent joint-output thin strips (item 126)

For two common native outputs, choosing
$q=b_N/b_M$ cancels the shared $t^2$ coefficient exactly.  The remaining
profile variation is proportional to
$b_N(\epsilon_N-\epsilon_M)t e^{-t}\delta H$.  Early/late splitting and
the fixed-mass variation estimate prove an all-$\tau$ strip bound.  In the
adjacent case its optimized normal width is



$$
O\!\left(\frac{2^{N/2}}{(N!)^{2/3}N^{4/3}}\right),
$$



and the joint area gains another $N^{-1}$.

The decisive correction is positional.  Exact Gaussian-power estimates give
$b_{N+1}\ge(7/2)b_N$ for all $N\ge2$, so every pair obeys
$T>5B_N/7\ge5/[7e(N+1)]$.  The primitive integer normal multiplies this by
$b_M/g$, where adjacent
$g\mid((N+1)R_N-R_{N+1})/2=O(N2^{N/2})$.  Hence the normal is not a small
integer direction.

On the monotone adjacent residue classes, the exact lower boundary is
$D_N^0=\int R e^{-t}t^N(1-t)$, with $N^2D_N^0\to5$.  Temporary
rationality turns this into a one-sided denominator lower bound rather than a
contradiction.  The only primitive two-output vector cancelling the common
factorial coefficient is $(M!/N!,-1)$, and its output remains at least
$(e+2)/(2e)$ for $N\ge14$.

~~~
a20afd820c91b4feef14479bb82b15dab1599a109b2463a6c5c97fc6edb5a8aa  sources/common_kernel_adjacent_joint_output_thin_strip_no_go.md
a26660b7b067571c348d221cf6e01ee9489903d4e7fbb9920caf30ef95970c72  scripts/common_kernel_adjacent_joint_output_thin_strip_certificate.py
8869c862afbe471cae5cf78694bbdaea812603ded1d87b8dba1f7aac5de466ae  results/common_kernel_adjacent_joint_output_thin_strip_certificate.json
df1f67b6f612402a0877ca937dc9494581f8ec3b58634f54abc418b475ec5ef6  results/common_kernel_adjacent_joint_output_thin_strip_hashes.sha256
~~~

Two final deterministic replays and the frozen dependency manifest pass.
This establishes a precise pairwise determinant no-go, while leaving
higher-output Smith content and new recurrence-specific arithmetic open.

### 2026-08-27 — First three ordinary Bessel layers and Wilson carry (item 127)

Splitting the exact all-power expansion into its five multiple-of-$p$
blocks gives closed rational-polynomial expressions for
${\cal C}_1,{\cal C}_2,{\cal C}_3$.  Wilson complementation reflects the
three high blocks into explicit low factorial-harmonic sums
$A_\ell,B_\ell,G_\ell$.  On a root, the ordinary slope becomes
$\delta=A_1+B_0$, and the next two raw layers have closed degree-three and
degree-four formulas at all four window endpoints.

Lifting the reflected high block modulo $p^2$ introduces the Wilson
quotient termwise, but that term cancels after summation because
$p\mid q_r$.  Substitution into the exact first-layer formula gives the
carried second digit



$$
F_{p,r}(Z_0)/p^2\equiv\kappa_2(Z_0)+{cal C}_2(Z_0)\pmod p.
$$



This calculation exposes why bounded raw-layer nonvanishing is insufficient.
Every positive raw layer vanishes exactly at $Z=0$; elsewhere it can be
cancelled by $\kappa_2$.  The proof target must therefore involve either
the base quotient $q_r/p$ itself or a carried, rather than raw,
noncancellation invariant.

The formula reconstructs the known $p=13$ square and a newly located
ordinary square at $p=52453,n=66831$, with exact valuation two.  Two
byte-identical eight-thread scans over $10000\le p<500000$ covered 40,309
primes, found that square alone, and found no singular orbit or cube.  The
scan is explicitly finite-only.

~~~
af171d428ac26019c3d98af3cd46a72cfa64db5a305857f369b05a6cfd5fa44f  sources/bessel_ordinary_first_three_layer_wilson_carry.md
6284b8afcbfed1349df814a7be0f4e507c59a9202308684ab7f706fbb366ad2a  scripts/bessel_ordinary_first_three_layer_wilson_carry_certificate.py
fde48d5d77ab0aa33fccdd6a9e229305e5e2c8c92a43fd8ec2ce5135b635bd86  scripts/bessel_ordinary_large_prime_scan.cpp
d27210380697091ae0e1f37573d1035c8c228885839c1d4720babaa4b3a2ef48  results/bessel_ordinary_first_three_layer_wilson_carry_certificate.json
76a9244467bac4c6b9ca35b534c8bbd73ae774e6e732fb298e85255b44035b54  results/bessel_ordinary_large_prime_scan_certificate.json
8404b4b76df36a327e29f7b444572326bf344b9691e2d522969723407956efa7  results/bessel_ordinary_first_three_layer_wilson_carry_hashes.sha256
~~~

The full sign and carry derivation, exact replay, duplicate finite scan, and
manifest pass.  The package proves no valuation bound and no classification
of $e+\pi$.

### 2026-08-27 — Native factorial windows and exact CF exhaustion (item 128)

The fixed-index closure endpoints satisfy



$$
{\cal L}^{0}_N=\frac5N-\frac4{N^2}-\frac5{N^3}
 +\frac{45}{N^4}+O(N^{-5}),
$$





$$
{\cal L}^{\min}_N=\left(1+\frac2e\right)
 \left(\frac1N-\frac1{N^3}+\frac1{N^4}+O(N^{-5})\right).
$$



The lower expansion follows from the exact crossing equation after proving
$J(\tau_N)/B_N\to1$ and
$\tau_N\sqrt{b/B_N}\to1$.  Uniform endpoint bounds give the necessary
window



$$
1<N\,N!\left(e+\pi-\frac PQ\right)<5.
$$



For every reduced hit with $N\ge10$ and $Q^2\le N!$, Legendre's
criterion makes $P/Q$ a principal convergent.  An exact 5,856-place
outward enclosure then certifies 5,684 common continued-fraction coefficients
through the first denominator above $\sqrt{2000!}$.  The exhaustive broad
candidate list is



$$
25,33,43,86,88,164,331,351,1477.
$$



The indices $86,351,1477$ are in forbidden residue classes, and the pinned
membership package certifies the other six.  Hence there is no new admissible
hit for $332\le N\le2000$.  The result is explicitly finite and proves no
infinitude, irrationality, or transcendence statement.

~~~
c7464fc9dbcbd5bd26146a500da797abdaf8b25ea04f3444994ec46097088e16  sources/common_kernel_native_cf_window_scan.md
d127322e0362aa179a5358d4ca54116929666ddc77e41acc33859ae026ec6a03  scripts/common_kernel_native_cf_window_scan_certificate.py
051f52f528a9835fc33938e99952fa483ae32ca9d5bf4b2d0c862c829fa94d9f  results/common_kernel_native_cf_window_scan_certificate.json
45c9253a4d4572806c0650345f2e47e4d8953618daf5c87512a1d62e0e1cd958  results/common_kernel_native_cf_window_scan_hashes.sha256
~~~

Two final replays were byte-identical, used about 37 MiB peak RSS, and the
manifest passes.  The finite scan isolates an infinite factorial/continued-
fraction matching problem rather than resolving it.

### 2026-08-27 — Multi-output Smith structure (item 129)

The cleared response matrix for any finite collection of native outputs has
the exact factorization $M=AC$, where $A$ consists of the two native
Gaussian columns and $C$ contains the two universal beta responses.  Hence
the variable response rank is at most two, and its Smith invariants and the
maximal minors of the factorial/affine augmentations reduce to exact products
of low-rank determinantal divisors.

Profile-independent relations are encoded by



$$
p(t)=(t^2-2t+2)q(t),
 \qquad
 \sum_j c_j(N+1)_j=0.
$$



Four consecutive outputs have a unique primitive relation whose invariant is
$\asymp N^2$.  For the five-index window
$N,N+1,\ldots,N+4$, $N\equiv0\pmod8$, the complete Smith image is



$$
\frac{2\eta_N}{(N+2)(N+3)}\mathbb Z,
 \qquad
 \eta_N=71\ \Longleftrightarrow\ N\equiv16\pmod{71}.
$$



A primitive relation attains the positive generator, but its reduced
denominator is exactly $Q_N=(N+2)(N+3)/2$, and $Q_N$ divides every
common correction denominator.  Thus the analytic $N^{-2}$ gain is
absorbed exactly by the forced arithmetic denominator.  The rank-two relation
lattice also contains a primitive exact-zero direction.

~~~
ea090145c760599bd1eb4a85192aa330da72cc8f6bebaebaff25b827e28c0367  sources/common_kernel_multioutput_smith_quadratic_denominator_obstruction.md
a346881d779d2c272a8a342bd3a16099134d3ba68e00f807672609192728df43  scripts/common_kernel_multioutput_smith_quadratic_denominator_certificate.py
cc8740eee8eb4c470cfca2ae1cb91c7898b0722a14b8a37eadb6b76e7c606e1e  results/common_kernel_multioutput_smith_quadratic_denominator_certificate.json
786c6e2c2f25aa1cd11a0b0b480277eaaacd1a8bda54b70af2ad9f6d46939fe5  results/common_kernel_multioutput_smith_quadratic_denominator_hashes.sha256
~~~

The proof, exact symbolic replay, markup audit, dependency pins, and two
deterministic outputs pass.  This supplies a sharp higher-output denominator
obstruction, not an irrationality or transcendence proof.

### 2026-08-27 — Symmetric Bessel transfer and unavoidable base carry (item 130)

For $p\mid q_r$, $s=p-1-r$, the reflection transfer has the exact
finite-field form



$$
M_{p,r}\equiv
 \begin{pmatrix}1&0\\4r+2&1\end{pmatrix}\pmod p.
$$



Its upper-right entry is the symmetric continuant
${\cal K}_h(2p)$, with $h=(p-3)/2-r$.  Oddness of the continuant yields



$$
\delta=\frac{q_r-q_s}{p}
 \equiv-2{\cal K}'_h(0)q_{r-1}\pmod p.
$$



This formula proves that ordinary slope nonvanishing is independent of the
base digit $q_r/p\bmod p$ within the transfer identity.  The exact Charlier
connection



$$
{\mathfrak A}_{p,r}\equiv
 (-1)^rq_r+p{\mathfrak L}_r
 \equiv(-1)^rq_s+p{\mathfrak L}_s\pmod{p^2}
$$



separates the slope condition from the additional Wieferich-type congruence
that characterizes $p^2\mid q_r$.

The frozen Wilson carry also reduces to



$$
\frac{F_{p,r}(Z_0)}{p^2}
 \equiv d+\Psi_{p,r}(Z_0)\pmod p,
 \qquad \frac{q_r}{p}\equiv c+pd\pmod{p^2},
$$



so the next uncontrolled base digit occurs with coefficient one.  Companion
solutions with altered initial values give exact recurrence countermodels to
any attempted deduction from ordinary slope or lower modular data alone.

~~~
769c886c1c8e5a6e406bd2018c71846e2831170359c2e97b43939e200a108c6e  sources/bessel_ordinary_symmetric_transfer_base_carry_barrier.md
7dbe32fb6ab59c001724543ea4a7e3657e9a5b6bb24ad918e363b549d285c9ec  scripts/bessel_ordinary_symmetric_transfer_base_carry_certificate.py
7f964cbbd5d0cdc749959614ae3e54e92bc8914227005fc9f4acf168a127512b  results/bessel_ordinary_symmetric_transfer_base_carry_certificate.json
bda724f3790cda56b5bc67fb99ccc854c693da1a2c7d53c85108e4cda394b5e6  results/bessel_ordinary_symmetric_transfer_base_carry_hashes.sha256
~~~

The congruence/equality distinction in the transfer proof was repaired during
audit.  Two final replays and the pinned manifest pass.  No all-prime square
or cube exclusion, valuation bound, or conclusion about $e+\pi$ follows.

### 2026-08-27 — Factorial-window CF entry dichotomy (item 131)

For a below principal convergent $p_k/q_k<x$, retain the original
continued-fraction index and let $N$ be the first admissible native index
such that $q_k^\tau\leq N!$, where



$$
\tau=\frac{2}{1-2\delta}.
$$



The gap-four admissible residue pattern gives



$$
1\leq\Lambda_k:=\frac{N!}{q_k^\tau}<N^4,
\qquad
 \frac{N!}{q_k^2}=\Lambda_kq_k^{\tau-2}.
$$



Writing $Z_k=N\,N!(x-p_k/q_k)$, every missed native window is either low
or high.  Exact continued-fraction coordinates give



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



For $\delta>0$, infinitely many low entries force
$\mu_-(x)\geq\tau>2$, whereas finitely many low entries imply
$\mu_-(x)\leq\tau$.  At the square-root boundary $\delta=0$, infinite
low entries improve the error only by
$\asymp\log\log q/\log q$, so Roth is not reached.

The exact norm inequality for $\phi$ shows that no sufficiently large
native-shaped hit exists for $q^2\leq N!$, even with every residue class
allowed, while every partial quotient of $\phi$ is one.  Hence misses alone
cannot force large partial quotients.  The revised scale theorem keeps two
independent facts separate: badly approximable inputs force a maximum scale
$\Omega(N)$, and multiplicative coverage of the factorial jump requires
$\Omega(\log N)$ fixed-ratio copies but does not determine their absolute
placement.

~~~
572ae7a426a22e1775a774732629c71d005dc0d1214288231bb8dd1456db3714  sources/common_kernel_factorial_window_cf_entry_dichotomy.md
d61d0617f8d1322d07d13f13b01e87366b1a7175b086128cc0096406b38aa3d4  scripts/common_kernel_factorial_window_cf_entry_dichotomy_certificate.py
401ef6b199eacf4f72ab41f7bd673e440f3c6dc7e0ce84b28571b2611d67f99e  results/common_kernel_factorial_window_cf_entry_dichotomy_certificate.json
e020e4c07067054101c4755b0a3899b79d93c7db468b0162daf2d946e1e944bc  results/common_kernel_factorial_window_cf_entry_dichotomy_hashes.sha256
~~~

The corrected source was line-audited and replayed independently at about
69 MiB peak RSS; its dependency and frozen manifest pass.  This is an
abstract dichotomy and countermodel, not a classification of $e+\pi$.

### 2026-08-27 — Symmetric-continuant Lommel derivative (item 132)

For



$$
{\cal K}_h(X)=[X-4h,X-4h+4,\ldots,X+4h],
$$



cofactor reflection and positive tail continuants give



$$
{\cal K}'_h(0)=(-1)^h\left(
 P_{h,0}^2+2\sum_{j=1}^h(-1)^jP_{h,j}^2\right).
$$



A separate arithmetic-continuant expansion yields



$$
{\cal K}'_h(0)
 =\sum_{a=0}^h(-16)^a(a!)^2
 \binom{h+a+1}{2a+1},
$$



and the corresponding formal generating identity.  Since
$P_{h,j}\leq P_{h,0}/(4^j j!)$, the alternating-square bracket lies
strictly between $13P_{h,0}^2/15$ and $17P_{h,0}^2/15$.
An even--odd block factorization also realizes the positive bracket as an
explicit pentadiagonal determinant.

The result proves integer nonvanishing and the exact real sign only.
It cannot be reduced to the desired finite-field conclusion:
${\cal K}'_2(0)=963$ is divisible by $107$.  Consequently neither the
ordinary-root determinant nor the independent Charlier base-square
condition is settled.

~~~
9d553e597f353915d16279031f4d0415342f8dfde628c925bcabd51e442f0d57  sources/bessel_symmetric_continuant_lommel_derivative_theorem.md
7e6816a4fbd63b818d1ea1acd370c274df1eeb2516ff2c5b5881a78f4619569c  scripts/bessel_symmetric_continuant_lommel_derivative_certificate.py
3b78a0cd61d0bf701db017a4a0a71fe59399aaa2e87e98e01c44c3baa2c5227e  results/bessel_symmetric_continuant_lommel_derivative_certificate.json
711d2f95dc6a8acee83b8a92b472d668f5aafcb4020197fe96ecfe3d8ea09bcf  results/bessel_symmetric_continuant_lommel_derivative_hashes.sha256
~~~

The replay checked both derivative formulas through $h=80$, all tail
formulas, 32 exact pentadiagonal determinants, and 560 individual
Cauchy--Binet minors at about 19 MiB peak RSS.  The dependency and final
manifest pass.  No $e+\pi$ conclusion follows.

### 2026-08-27 — Mixed-cubic Cartier content and denominator cancellation (item 133)

For $n=6m$, $k=4m+1$, the adjacent mixed-cubic form



$$
\Lambda_{01}=L_1H_0-L_0H_1=A_m+B_m\pi
$$



has the universal clearing



$$
{\cal D}_m=2^{9m+5}M_{4m+1}.
$$



An exact relative-Cartier endpoint lemma improves this to



$$
{\cal D}^{\sharp}_m=
 \frac{2^{9m+5}M_{4m+1}}
 {\displaystyle\prod_{2m<p<3m}p}.
$$



For such a prime, Frobenius extraction writes each transformed integrand as
$G^pg_s\,dy$.  Cartier sends both $g_s\,dy$ into the one-dimensional
space spanned by $dy/(1+y^2)$, because they have only the simple retained
poles $\pm i$ and are regular at infinity.  A termwise endpoint lemma
then makes $(pR_s,L_s,E_s)$ proportional modulo $p$, proving
$v_p(A_m)\geq0$.

A disjoint exactness criterion gives a common-content product
${\cal P}_m$ with



$$
\log\prod_{p\in{\cal P}_m}p
 =\left(-4\log2+\frac{\pi}{\sqrt3}+3\log3\right)m+o(m).
$$



The package also proves the exact recurrence
$a_mH_0+b_mH_1+c_mH_2=0$, hence
$\Lambda_{12}=(a_m/c_m)\Lambda_{01}$, and the contour identity



$$
B_m=\frac{2|C_m|^2}{m}
 \operatorname {Im}(I_2\overline{I_0}),
$$



where integration by parts has removed the leading $5/8$ ratio.

The sharpened arithmetic changes the conditional saddle ledger from below
one to



$$
d/h_{\rm cert}=1.0053272038\ldots,
\qquad d-h_{\rm cert}=0.0123840352\ldots
$$



per $n$.  These numbers remain conditional on proving that the specified
interior complex saddle is uniquely accessible and dominant for both
contours with a uniform asymptotic.  That analytic theorem is now the
precise remaining gap; no irrationality or transcendence conclusion is
drawn.

~~~
286d9cf4d3591a1a9b9fefc6dd3ee3dcc9f7c2ba49a73310909491814544d9e8  sources/mixed_cubic_boundary_cartier_content_and_recurrence.md
81d9fa515ba39719d17a5f35456e3749d34f8d857a0411b97fff228c39a36d6d  scripts/mixed_cubic_boundary_cartier_content_and_recurrence_certificate.py
3a060ecf43afe8a5047401cfed9ac2208345b5f2636ef88c14ce959324dace29  results/mixed_cubic_boundary_cartier_content_and_recurrence_certificate.json
34e61497fa2df8dd4dfcaf143be574bd3ada434977d41e6be75b590ba927a14c  results/mixed_cubic_boundary_cartier_content_and_recurrence_hashes.sha256
~~~

Two full exact replays through $m=36$ were byte-identical at under
95 MiB peak RSS; root replay reproduced the JSON hash.  The source delimiters,
controls, dependency, and final manifest pass.

### 2026-08-27 — Rational-case native denominator saturation (item 134)

Under the temporary hypothesis



$$
e+\pi=\frac uv,\qquad v\mid N!,
$$



the translated factorial coefficient $M=N!(e+\pi)$ is an integer.
Combining fixed-index closure with exact rational-moment integer
approximation proves that all and only the rational points of
$({\cal L}^{\min}_N,{\cal L}^{0}_N)$ are strict integer-localizer
outputs.

If $m/D$ is such an output in lowest terms, integer translation gives



$$
\rho=\frac{m-MD}{D},\qquad
 (m-MD,D)=1.
$$



The output and coordinate therefore have the same reduced denominator, and
positivity forces



$$
D{\cal L}^{0}_N>m\geq1.
$$



This inequality is sharp.  For admissible $N\geq1246$,
$D_N=\lfloor N/5\rfloor+1$ satisfies



$$
{\cal L}^{\min}_N<1/D_N<{\cal L}^{0}_N
$$



and is the least possible reduced output denominator.  The exact-moment
theorem realizes this rational target under the hypothesis, with



$$
D_N{\cal L}_{N,h}=1,\qquad
 1<D_N{\cal L}^{0}_N<1+\frac5N.
$$



Hence qualitative rational-point selection saturates the positive-integer
threshold rather than crossing it.  A separately controlled arithmetic
localizer with $D{\cal L}^{0}_N<1$ would still contradict rationality; it
is not excluded unconditionally.

~~~
52a554fd8c39d2caa641fafbbb43ad572b5e736e70c230793d5ece365da30332  sources/common_kernel_rational_case_denominator_saturation_barrier.md
d96c493f3af8e62638a23562ae096f732bcaf4306bcdee2e98ab05713fde0905  scripts/common_kernel_rational_case_denominator_saturation_certificate.py
c51ba0bdc55ac3ebc2220dcdfb44c7a728b8c80059f1cac99aa395d5cfb78371  results/common_kernel_rational_case_denominator_saturation_certificate.json
a90239b6de95a344d41728ee404dfde0d3a5c8ab8f6368e7bfdd1316c5c9dadf  results/common_kernel_rational_case_denominator_saturation_hashes.sha256
~~~

The exact $c_*>1/50$ proof, beta ledger, residue classes, 1245/1246
strictness, denominator gcds, all five dependencies, and manifest pass.
Root replay used about 69 MiB.  No arithmetic classification follows.

### 2026-08-27 — Temporary stop and saddle handoff

At the user's request, all research workers stopped and saved their current
state.  No proof in either requested classification direction has been
obtained.

Two explicitly unfinished notes now preserve the active mixed-cubic analytic
frontier:

~~~
fe731a600578a4b7d585af1f1de9b2c231d09929a13dc568400938414ac1313b  sources/mixed_cubic_boundary_saddle_handoff.md
c8eb9e3b6267bb6ccc949aa145ccb4bf3ac627a1a6f97d51aebcda930b29aa0b  sources/mixed_cubic_accessible_saddle_handoff_20260827.md
~~~

The accessible-saddle note records an exact algebraic parametrization of the
candidate $\tau$, its valid fixed circle $|v|=|\tau|<1/2$, the exact
degree-six angular critical polynomial, exact formulas for the quadratic
coefficient and determinant amplitude, and the external equal-modulus saddle
beyond the pole at $-1$.  It also records a provisional numerical Sturm sign
table.  The latter has not been certified in exact algebraic arithmetic and is
not a theorem.

The next run should construct the exact rational-interval/Sturm certificate,
prove the uniform fixed-circle complex-Laplace expansion, freeze and
independently audit that package, and only then combine it with item 133.
That conditional combination is aimed at irrationality; it would not finish
the algebraic-versus-transcendental classification.

The final pause audit parsed 238 Python programs and 245 JSON certificates,
syntax-checked both C++ programs, verified all 93 package manifests, and found
no disallowed control bytes among 750 text artifacts.  Four orphaned
exploratory Python processes were identified and terminated.  Memory then stood
at about 3.7 GiB used and 46 GiB available; no research worker or computation
was intentionally left active.

### 2026-08-28 — Exact mixed-cubic saddle and complex-Laplace closure (items 135--136)

The accessible saddle from the previous handoff is now exact.  A rational
isolation of its algebraic radius, a degree-six angular critical polynomial,
an exact nonvanishing discriminant on a connected interval, and a rational
basepoint Sturm count prove that there are exactly two circle-critical points.
Exact brackets and derivative signs select $\tau$ as the unique global
maximum.  The certificate also proves $\Re\lambda>0$ and
$\Im(b_2(\tau)/b_0(\tau))>0$.

A uniform fixed-circle complex-Laplace theorem then gives



$$
I_j(m)=\frac{\Psi(\tau)^m}{\sqrt{2\pi m}\sqrt\lambda}
 \left(b_j(\tau)+O(m^{-1})\right),\qquad j=0,2,
$$



and hence an eventually positive determinant coefficient with its exact
logarithmic rate.  Both packages passed two byte-identical independent root
replays and their manifests.

### 2026-08-28 — Corrected beta matching ledger (item 137)

The earlier claim that $d>h$ sufficed for positive matching was false.  For a
primitive $L=a+\varepsilon b\pi>0$, beta pair $(p_N,q_N)$, and
$\Delta=\gcd(b,q_N)$, the minimal match has final coefficient



$$
Q=\frac{bq_N}{\Delta g},\qquad g\mid\Delta.
$$



At beta scale $N\log N/n\to t$, the two positive terms have upper rate



$$
\max\{h-t-\Gamma,\ t+h-d-\Gamma\},
$$



where $\Gamma=n^{-1}\log(c_m\Delta_mg_m)$.  The optimum is $t=d/2$.
For the certified constants,



$$
h-d/2=1.156147151964244612\ldots>0.
$$



Therefore generic no-content matching needs $d>2h$.  Irrationality needs a
new content theorem with $\Gamma>h-d/2$; Roth-level transcendence needs
$\Gamma>h$.  The final wording explicitly notes that nonvanishing of the
shrinking $1,\pi$ forms uses the known irrationality of $\pi$, rather than
claiming a new independent proof.

### 2026-08-28 — Prime-support obstruction and temporary stop (item 138)

For the minimally matched form,



$$
P^*=b_0p_N-\varepsilon q_0a,quad Q^*=\Delta b_0q_0,quad
 g=\gcd(P^*,Q^*)=\gcd(P^*,\Delta),
$$



and the exact outside-prime product is



$$
P_{\mathcal S^c}Q_{\mathcal S^c}
 =\frac{(P^*)_{\mathcal S^c}(Q^*)_{\mathcal S^c}}
        {g_{\mathcal S^c}^{2}}.
$$



Exact arithmetic countermodels show that item 133's clearing, dyadic
integrality, and Cartier content alone permit arbitrary fresh primes to survive
in the primitive matched denominator.  They therefore imply neither the fixed
nor quantitative moving-support hypothesis.  These countermodels are not the
actual periods; a theorem specific to their primitive coordinates could still
work.

The final whole-archive audit parsed all 242 Python programs and all 249 JSON
certificates, syntax-checked both C++17 programs, verified all 97 package
manifests, and found no disallowed control byte in 860 audited text artifacts.
The authoritative handoff is `active_checkpoint_20260828.md`.  All workers were
stopped at the user's request; RAM was about 3.7 GiB used with 46 GiB available
out of 50 GiB, and no accelerator was needed.  A fresh backup and SHA-256
sidecar were written in `/content/drive/MyDrive` with timestamp
`20260828T001000Z_handoff_item138`.

### 2026-08-28 00:18 UTC — Final stop after brief automatic continuation

The persistent goal mechanism briefly resumed three classification-level
branches.  On the user's reiterated deadline, all three were interrupted
immediately; none had frozen a new file.  A completed exact finite diagnostic
of the actual item-133 pairs through $m=36$ found no synchronization signal
near the required threshold: at the nearest optimal beta index the observed
rate $(6m)^{-1}\log(c_m\Delta_mg_m)$ was at most about $0.66077$ for
$m\ge2$, versus the required $1.156147\ldots$.  Searching all compatible
$N\le6m$ for $3\le m\le36$ still left the finite matched upper ledger
positive.  These computations are diagnostics only and prove no asymptotic
obstruction.  Research was stopped again and a final timestamped backup was
prepared.

### 2026-08-28 — Resumed audit and cross-order factorial support dispersion (item 139)

The user explicitly resumed the persistent research goal.  A fresh audit read
all 829 substantive archive files (the other 829 files are AppleDouble
sidecars) and found no hidden proof or classification of $e+\pi$.  All 242
Python sources and 249 JSON files parse.  All 379 entries in the 97 existing
manifests still hash correctly.  One older JSON embeds a stale hash for a note
that was subsequently strengthened, and several `.pyc` files are stale; source
files and manifests, not bytecode leftovers, remain authoritative.

For the factorial-digit family, arbitrary primitive finite-difference forms
at bases $a\le m$ now satisfy the exact cross-order determinant identity



$$
P_{a,b}Q_{m,c}-P_{m,c}Q_{a,b}
 =\frac{a!\,\mathcal R_{a,b;m,c}}{J_{a,b}J_{m,c}},
$$



with a cancellation formula that bounds $|\mathcal R|$ using only one local
difference factor.  Consequently, for orders at most $B$,



$$
(Q_{a,b})_{\mathcal S^c}(Q_{m,c})_{\mathcal S^c}
 \ge
 \frac{a!}{2^{B+2}(m+B)^B(m!)_{\mathcal S}}.
$$



This extends the old untouched-truncation dispersion theorem to unequal bases
and arbitrary orders.  It rules out quantitative moving-support blocks inside
bounded multiplicative base windows whenever the orders remain genuinely
subdiagonal.  Along $b/a\to\lambda<1$, algebraicity would force harmonic
denominator-support mass at least $((1-\lambda)/2-o(1))\log a$.

The exact replay checked 1,061 indexed forms and 562,330 pairs through base
100 and order 10.  It found the exact duplicate primitive pair
$(a,b)=(14,1)$, $(m,c)=(16,0)$, so moving blocks must deduplicate actual
$(P,Q)$ values.  The new theorem is an obstruction and phase diagram, not a
support-concentration construction; highly lacunary and near-diagonal regimes
remain open.

```text
7e735ab6aed4021dd1de6b3cdd81d8c523a464a0800ce559f97096385541b526  sources/factorial_cross_order_support_dispersion.md
4fbfa121413ccf78ae39056428d93a84fe4e0aa1e0ff887db3d72bafe7d0ddbf  scripts/factorial_cross_order_support_diagnostic.py
9887b1bc2df6f98f50e0aca1e7a718f12f66b3417211612c1bc5c59365c87c85  results/factorial_cross_order_support_diagnostic_m100_b10.json
27888e059cc2f85395e63d3cfaca02017fcf39825d6799946720495806783fb4  results/factorial_cross_order_support_dispersion_hashes.sha256
```

No conclusion about the irrationality or transcendence of $e+\pi$ follows
from item 139 alone.

### 2026-08-28 — Actual mixed-cubic positive-match certificate (item 140)

The canonical item-133 mixed-cubic coordinates and beta matches were rebuilt
in a self-contained exact generator.  Rational Machin bounds orient every
primitive $1,\pi$ form; the beta integral gives
$E_N\ge N!/(2N+1)!$; and the final matching gcd is computed exactly.

For every $1\le m\le100$ and all 15,150 parity-compatible indices
$1\le N\le6m$, the resulting positive match has a rational certified lower
bound greater than one.  A second end-to-end run reproduced the 1.66 MB result
byte for byte, and a separate verifier checked the raw numerator-denominator
inequalities, scope, parity, transcript commitments, and pinned source hashes.

The same exact data show, only for the finite tested indices, that the
post-Cartier content $c_m$ is supported on primes at most $6m$ for
$m\le100$, $m=150$, and $m=200$.  This is not an all-$m$ support
theorem.  The finite matches being greater than one show that the canonical
integer-contradiction mechanism has not crossed its target in the certified
window; they do not imply an asymptotic obstruction.

The authoritative package manifest is
`results/mixed_cubic_actual_positive_match_finite_hashes.sha256`, with SHA-256
`17c2b94aa0f77d368065a3edf1251c77584440a42b67c20a7cc15dbda9f4e114`.
No arithmetic classification of $e+\pi$ follows from item 140.

### 2026-08-28 — Equal-valuation synchronization and CRT reduction (item 141)

The exact beta synchronization gcd was reduced prime by prime.  A prime can
enter the matching gcd only on an equal-valuation branch
$v_p(b_m)=v_p(q_N)>0$.  On the ordinary branch, prescribed local
synchronization data occupy at most



$$
\prod_{p\mid\Delta_m} R_p,\qquad R_p\le 2p^{2/3},
$$



residue classes modulo $2\Delta_mg_m$.  This is an exact CRT reduction, not
an upper bound for the actual synchronization gcd: obtaining exponential
$\Delta_mg_m$ at the saddle $N\asymp m/\log m$ would still require the
actual CRT class to have an exponentially small representative.  The
singular branch is a Wieferich/all-lift obstruction and remains open.

Finite exact scans reinforce the distinction.  In a 20-percent window around
the saddle, the largest observed actual synchronization rate for
$81\le m\le100$ was about $0.257895$, and for sampled
$105\le m\le200$ it was about $0.213268$; both are far below the required
irrationality content rate $h-d/2\approx1.156147$.  These observations are
finite diagnostics, not asymptotic upper bounds.  Removing every prime at
most $6m$ from the primitive $\pi$-coefficient still leaves an exponential
cofactor in the sampled range, so smooth-part estimates alone cannot control
all primes that can synchronize with $q_N$.

The authoritative manifest is
`results/mixed_cubic_equal_valuation_crt_reduction_hashes.sha256`.  Item 141
isolates the precise CRT bottleneck but proves neither irrationality nor
transcendence of $e+\pi$.

### 2026-08-28 — Fresh-prime log-residue reduction and width-49 theorem (item 142)

For every prime $p>6m$, simultaneous divisibility of the two actual
mixed-cubic integral coordinates is now equivalent to simultaneous
vanishing of two explicit logarithmic residues:



$$
p\mid\widehat A_m,\widehat B_m
 \quad\Longleftrightarrow\quad L_{0,m}=L_{1,m}=0\pmod p.
$$



The proof uses exact rational differentials and includes the endpoint case
$p=6m+1$.  Integral coefficient formulas, a four-step scalar recurrence,
and fixed-gap finite-field resultants then prove the uniform interval theorem



$$
6m<p<6m+49\quad\Longrightarrow\quad
 p\nmid\gcd(\widehat A_m,\widehat B_m)
$$



for every $m\ge1$.  The byte-stable certificate completely factors the 16
relevant fixed-gap resultants, uses deterministic primality certification
below $2^{64}$, and performs 455 independent coefficient-formula/recurrence
replays.

The exceptional reverse-implication ray $p=10m+3$ reduces to a coefficient
problem for the formal inverse of $y^5-y=z$.  More generally, the fixed-gap
resultants develop large compatible prime factors, so the computation does
not extend to all $p>6m$.  The authoritative manifest is
`results/mixed_cubic_large_prime_log_residue_hashes.sha256`.  Item 142 is an
unconditional infinite theorem, but it proves no classification of
$e+\pi$.

### 2026-08-28 — Coordinate, content, and fresh-prime audit (item 143)

The actual item-133 mixed-cubic coordinates now have explicit Gaussian
constant-term formulas and an exact primewise valuation formula for the
primitive content.  The $\pi$-coordinate is an explicit determinant and a
rational diagonal, hence P-recursive.  Combining the best published
irrationality-measure bound for $\pi$ with the frozen saddle theorem gives



$$
\limsup_{m\to\infty}\frac{\log c_m}{6m}
 \le h-\frac d{\mu_*}\approx1.99566316016,
$$



which remains far above the matching threshold
$h-d/2\approx1.15614715196$.  Thus this rigorous upper bound does not close
the content problem.

The log-residue pair also has an exact integral recurrence and a terminating
hypergeometric coefficient formula.  A deterministic exact scan through
$m=2000$ found that every prime divisor of the log-residue gcd was at most
$6m$.  A second deterministic scan tested all 2,402 prime cases on the
exceptional ray $p=10m+3$ with $m\le10000$, finding no common log zero
and no consecutive Taylor zero.  Both outputs were independently replayed
byte for byte.  These are finite results only and do not imply the all-
$m$ support conjecture.

The authoritative manifest is
`results/mixed_cubic_coordinates_sync_fresh_prime_audit_hashes.sha256`.
Item 143 records the sharpest coordinate reductions and finite evidence, but
proves neither irrationality nor transcendence of $e+\pi$.

### 2026-08-28 — Uniform exceptional-ray coprimality theorem (item 144)

The formerly exceptional fresh-prime ray is now closed for every index.  If
$m\ge1$ and $p=10m+3$ is prime, then the two mixed-cubic logarithmic
residues cannot vanish simultaneously modulo $p$.

The proof sets $n=4m+3$, $F(y)=y^5-y$, and
$\rho_j=\operatorname{Res}_{y=1}y^jF(y)^{-n}\,dy$.  Exact sign-checked
conversion expresses $L_0,L_1$ through $\rho_0,\ldots,\rho_6$.  The
residue recurrence



$$
(k+5-5n)\rho_{k+4}+(n-1-k)\rho_k=0
$$



forces one parity-class residue to vanish.  The global residue theorem gives
the nonzero anchor



$$
4\rho_2=\binom{5m+2}{m}\not\equiv0\pmod p.
$$



If $L_1=0$, the remaining formula gives
$L_0/4=(1-2m)\rho_2/3$ for even $m$, and
$L_0/4=(2m-1)\rho_2$ for odd $m$; both are nonzero modulo $p$.
This is a uniform proof, not a finite extrapolation.  A separate
implementation checked all 2,402 prime-ray cases with $m\le10000$ against
the original Taylor recurrence and independently computed residues.

The authoritative manifest is
`results/mixed_cubic_exceptional_ray_coprimality_hashes.sha256`.  Item 144
removes one genuine all-$m$ obstruction, but the nonexceptional moving-prime
problem and the arithmetic classification of $e+\pi$ remain open.

### 2026-08-28 — Near-diagonal factorial/beta bridge (item 145)

The previously open near-diagonal factorial regime has an exact bridge to
the beta approximants for $e$:



$$
D_{n,n}=q_n,\qquad W_{n,n}=n!q_n,
 \qquad \Delta^n\lfloor n!e\rfloor=n!p_n.
$$



Writing $R_n=\Delta^n\lfloor n!\pi\rfloor$, the selected local content is



$$
g_n=\gcd(q_n,n!p_n+R_n)
 =\gcd\!\left(q_n,q_{n-1}R_n+2(-1)^{n+1}n!\right).
$$



The second equality removes the beta numerator completely by the exact
Wronskian.  The primitive diagonal denominator splits as
$Q_n^{\rm diag}=(q_n/g_n)(n!/J_n)$, with the two factors coprime.

For general rays $b/a\to\lambda$, an exact height refinement plus Roth's
theorem shows that algebraicity and nonzero unbounded primitive denominators
force



$$
\liminf\left(
  \frac{\mathcal A(Q_{a,b})}{\log a}
  -\frac{\log g_{a,b}}{a\log a}
 \right)\ge\frac{1-\lambda}{2},
 \qquad
 \mathcal A(Q)=\sum_{p\mid Q}\frac{\log p}{p-1}.
$$



On short diagonal blocks, the exact continuant gcd gives the alternative
$s\ge\min\{M,\log R/((L-1)\log(4(N+L)))\}$ for the union of denominator
primes.  Under uniformly sub-main-scale $g_n$, polynomial blocks therefore
need polynomially many support primes.  All statements include the exact
nonzero, unbounded-height, and deduplication hypotheses.

Two byte-identical replays through $n=265$ verify the identities and find
only 16 indices with $g_n>1$, but this is finite evidence only.  The
authoritative manifest is
`results/factorial_near_diagonal_beta_bridge_hashes.sha256`.  Item 145
isolates the diagonal cancellation/support dichotomy but proves neither
irrationality nor transcendence of $e+\pi$.

### 2026-08-28 — Nonexceptional fresh primes reduced to two poles (item 146)

For a prime $p>6m$, put $\delta=p-6m$,
$e=2m+\delta-2$, and



$$
h(t)=\frac{(2-2t+t^2)^e}{(-2+3t-t^2)^\delta}
 =\sum h_jt^j.
$$



Fresh-prime Frobenius gives $f_j=-h_j\pmod p$ for every $j<p$.
Consequently, simultaneous logarithmic-residue vanishing forces
$h_{4m}=h_{4m+1}=0$, with the converse away from $p=10m+3$; item 144
has already excluded that exceptional ray directly.  The rational function
$h$ has only the two poles $1,2$, and its target coefficients now have
exact principal-part/Hahn and single-hypergeometric-polynomial formulas.

For every fixed admissible gap $\delta$, a rational connection determinant
$\mathcal R_\delta$ controls all possible exceptions.  If it is nonzero,
only primes dividing its numerator require a final power-of-two check.  The
existing fixed-gap certificate proves no exceptions for exactly



$$
\delta\in\{1,5,7,11,13,17,19,23,25,29,31,35,37,41,43,47\},
$$



giving 16 rigorous infinite prime subfamilies.  A uniform height theorem
also proves, conditional on $\mathcal R_q\ne0$, that



$$
p>129q^3\,62208^q
$$



excludes simultaneous vanishing without factorization.  The condition
$\mathcal R_q\ne0$ is not known for every moving $q$, so this is not an
unconditional moving-gap theorem.

The deterministic probe finds $\mathcal R_q\ne0$ for all 60 admissible
$q<180$, refutes fixed sign, and finds no recurrence in one bounded search
box.  These are finite diagnostics.  Its output replayed byte for byte.  The
authoritative manifest is
`results/mixed_cubic_large_prime_two_pole_hashes.sha256`.  Item 146 sharply
isolates the remaining all-fresh-prime determinant obstruction but proves no
classification of $e+\pi$.

### 2026-08-28 — Ten slope-10 prime rays closed uniformly (item 147)

For $p=10m+b$, the fresh-prime coefficient problem can be regrouped using



$$
F(y)=y^5-y=tA(t)R(t),\qquad W(y)=tR(t),
$$



so that the two logarithmic residues become fixed-degree polynomial weights
against one common power of $F$.  The exact residue recurrence reduces both
functionals to two states.  One state is anchored by a nonzero binomial
coefficient from the global residue theorem; the remaining possible common
zero is controlled by a fixed rational determinant in $m$.

Exact primitive reduction, complete factorization of the ray constants, and
direct replay of every compatible candidate prove



$$
(L_0,L_1)\not\equiv(0,0)\pmod p
$$



for every $m\ge1$ whenever $p=10m+b$ is prime and



$$
b\in\{1,3,7,9,11,13,17,19,21,23\}.
$$



The $b=3$ ray recovers item 144; the other nine rays are new.  The generator
replayed byte-identically, and an additional independent scan covered 3,062
prime cases with $m\le1000$ without a common zero.  The scan is diagnostic;
the theorem is uniform.  The authoritative manifest is
`results/mixed_cubic_moving_ray_y5_minus_y_hashes.sha256`.

This closes ten infinite fresh-prime rays, not all moving primes, and does not
prove that $e+\pi$ is irrational or transcendental.

### 2026-08-28 — Uniform 3-adic nonvanishing of every connection determinant (item 148)

For every positive odd $q$ with $3\nmid q$, let
$n=q-1$, $r=(q-1)/2$, $D(k)=k+v_3(k!)$, and let
$\mathcal R_q=C_0T_1-C_1T_0$ be the exact full-and-tail determinant from
item 146.  Isolating the maximal 3-adic generalized-binomial terms proves



$$
\boxed{v_3(\mathcal R_q)=1-D(n)-D(r).}
$$



For $q\equiv1\pmod6$, only the top terms survive after normalization
modulo $9$; their determinant is $3$ times an explicit 3-adic unit.  For
$q\equiv5\pmod6$, the top two terms survive and the four normalized
components are $2,2,4,7\pmod9$, so their determinant is $6$ times a
unit.  This proves $\mathcal R_q\ne0$ uniformly and removes the
characteristic-zero determinant-degeneracy hypothesis from the fixed-gap
meta-theorem.

The independent exact replay checked all 334 admissible $q\le1001$ and
reproduced the JSON byte for byte.  The authoritative manifest is
`results/mixed_cubic_connection_determinant_3adic_nonvanishing_hashes.sha256`
(manifest SHA-256
`1d40d475d6ad1c7ea903f5face4ef0f87d318dd8f34cbe2350c0968299c39a24`).

The theorem does not exclude a fresh prime that divides the numerator of
$\mathcal R_q$; such a prime still needs the final power-of-two congruence.
Nor does it supply the small-prime content rate needed for the matched
integer form.  Thus item 148 is a uniform obstruction theorem, not a proof
that $e+\pi$ is irrational or transcendental.

### 2026-08-28 — Rank-one Cartier divisor and positive content mass (item 149)

Let $c_m$ be the actual mixed-cubic content after removal of the frozen
squarefree rank-zero Cartier product.  For each odd prime $p<2m$, let
$q_p=p^{e_p}$ be the largest power of $p$ not exceeding $4m+1$.
If the two prime-power degree values satisfy



$$
d_{q_p}(6m,4m+1),\ d_{q_p}(6m,4m+2)\le2q_p-2,
$$



then the $e_p$-fold Cartier images of the adjacent differentials lie in one
common one-dimensional space.  A relative endpoint congruence at the full
top denominator layer gives, after the existing clearing and the possible
single $G_m$-division,



$$
v_p(U_m)\ge1,\qquad v_p(V_m)\ge e_p+1.
$$



Thus every such prime divides $c_m$.  The prime-number-theorem interval
decomposition evaluates the forced radical mass exactly:



$$
\log\prod_{p\in\mathcal H_m}p
 =(-4\log2+6\log3-3)m+o(m),
$$



and therefore



$$
\liminf_{m\to\infty}\frac{\log c_m}{6m}
 \ge0.13651416829481281845\ldots .
$$



The exact replay checked all $m=1,\ldots,100,150,200$, including the
stronger local valuation bounds, and reproduced its JSON byte for byte.  The
authoritative manifest is
`results/mixed_cubic_small_prime_rank_one_cartier_mass_hashes.sha256`
(manifest SHA-256
`90002db627dc5ebce5ff2141a12a9657eb5f0135306a13a9cd7df0a0a16de310`).

The matching threshold remains $1.1561471519642446\ldots$, leaving an exact
deficit $1.01963298366943179388\ldots$ per $6m$.  The theorem forces only one
digit at each qualifying prime and does not control the remaining prime-power
mass.  Item 149 is a genuine lower bound, but it does not prove that
$e+\pi$ is irrational or transcendental.

### 2026-08-28 — Slope-10 rays extended through intercept 57 (item 150)

The $y^5-y$ residue method now has a closed terminating formula in the
intercept.  For each parity, the formal ray determinant at $m=-b/10$ is



$$
D_{b,\epsilon}
 =S_{c_E}(b-1;b)S_{c_O}(b-2;b)
  -S_{c_O}(b-1;b)S_{c_E}(b-2;b),
$$



where the $S_c$ are explicit finite Pochhammer sums.  The two actual
surviving residue states are each a single binomial coefficient modulo
$p=10m+b$, by a sparse Cartier/Lucas formula.

Complete factorization and direct replay prove non-simultaneous vanishing for
every admissible odd $b\le57$.  Thirteen rays beyond item 147 are new.  The
largest candidate, $p=106512286889$ on $b=29$, was excluded exactly by an
$O(\sqrt p)$ FLINT product/remainder tree.  All 50 wrapped small-prime cases
were also replayed directly.

A separate standard-library certificate proves that neither parity
determinant is zero for any admissible odd $b\le2001$: 1,600 rational
determinants have nonzero reduction modulo $1000000007$.  This is finite
determinant classification only; constants beyond $b=57$ have not all been
factored and replayed.

Both archive JSONs reproduced byte for byte.  The authoritative manifest is
`results/moving_ray_y5_minus_y_extended_hashes.sha256`
(manifest SHA-256
`0581212c4c004521e7f4bd0d14eeb470f6f12e68b3231880e6fda1714c8af6f6`).

Item 150 closes additional infinite fresh-prime rays but neither all moving
primes nor the content deficit, and it does not decide $e+\pi$.

### 2026-08-28 — Exact rank-two Cartier determinant and radical ceiling (item 151)

At the next prime-power degree cutoff, the two iterated Cartier images have
the form $F(a_i+b_ix)\,dx$.  In the genuinely new floor case
$N\equiv3s\pmod q$, $K_0\equiv2s+1\pmod q$, their proportionality is
equivalent to the exact determinant



$$
\Delta_{q,s}
 =(c_{q-2}+c_{q-3}+c_{q-4})c_{2q-1}
 -(c_{2q-2}+c_{2q-3}+c_{2q-4})c_{q-1}=0,
$$



where
$\sum c_nx^n=x^{3s}(1-x)^{3s}(1+x+x^2+x^3)^{q-2s-2}$.
Every vanishing row supplies one additional surviving squarefree factor of
the actual primitive post-$G_m$ content, including the one-deeper valuation
needed when the prime was already removed by $G_m$.

Three infinite determinant-zero rays are proved:



$$
p=3s+4,
 \qquad p=5s+2\ (s\equiv1\!\!\pmod4),
 \qquad p=5s+1\ (s\equiv2\!\!\pmod4).
$$



For a fixed $m$, their primes divide respectively
$(3m+2)(5m+1)(10m+1)$, so these families contribute only $O(\log m)$.
No complete rank-two floor interval vanishes: explicit $s=1$ and $s=2$
nonzero formulas give interior witnesses in every parity class.

Even if every possible rank-two determinant vanished, the additional radical
mass could be no larger than



$$
\left(6-\frac{\pi}{\sqrt3}-3\log3\right)m+o(m)
 =0.89036376976145307522\ldots m+o(m).
$$



Together with item 149 this optimistic ceiling would still leave
$0.87123902204252294801\ldots$ per $6m$ below the matched-form threshold.
The rigorously forced deficit remains
$1.01963298366943179388\ldots$, because the three proved rays are thin.

The deterministic replay covers 102 exact coordinate indices, 1,062
delta-zero rows, and 124 vanishing rows; every determinant, divisibility,
valuation, fixed-$s$, and ray check passes, and the output is byte-stable.
The authoritative manifest is
`results/mixed_cubic_rank_two_cartier_hashes.sha256`
(manifest SHA-256
`c0194fe0a2ad3b19ed8c4974a43b6c690aee3831cc3bd2bfbf9142e3f7f5c9da`).

Item 151 proves a new divisor theorem and a sharp radical limitation.  It does
not control the missing prime-power multiplicity, close all fresh primes, or
decide whether $e+\pi$ is irrational or transcendental.

### 2026-08-28 — Uniform slope-10 evidence and cyclic support target (item 152)

For the formal two-state determinant on $p=10m+b$, define $x=2m$ and
the explicit universal factor $U_b(x)$.  Exact division, the affine change
$z=(5x+b)/2$, and normalization by $2^{b-3}$ give 2-integral quotients
whose reductions agree in all tested cases:



$$
\overline Q_{b,0}=\overline Q_{b,1}=
 \begin{cases}
 (1+z)^h,&b=4h+3,\\
 (1+z)^h+z^h,&b=4h+1.
 \end{cases}
$$



The exact audit covers both parities and every admissible odd
$7\le b\le201$: 79 intercepts, 158 rows, with ordered stream SHA-256
`310283465b20fd739f867a9d186a82bcec3aa23e3bb02b7acb47924b7ba2e52b`.
This remains finite evidence, not an induction.  Even a uniform proof would
show only that the formal ray determinant is nonzero; compatible odd
numerator primes can remain and require replay.

Independently, for $q=b-2$, $n=4m+b$, $N=6m$, and
$J_k=\operatorname{Res}_{y=1}y^kW^qF^{-n}\,dy$, exact differentiation and
Cartier reduction give



$$
(k+3q+5-5n)J_{k+4}+(n-1-k)J_k
+q(J_{k+1}-J_{k+2}+J_{k+3})=0
$$



and



$$
4\sum_{k=0}^{p-1}J_kT^k
=(-1)^qT^5W(T)^q(1-T^4)^N\pmod{T^p-1}.
$$



Thus simultaneous adjacent vanishing is equivalent to $J_0=J_4=0$, and
reciprocity gives $J_k=-J_{n+4-k}$.  The remaining theorem target is that
the $T^0$ and $T^4$ coefficients of the explicit cyclic product cannot
both vanish.  Individual coefficient zeros do occur, so naive full support
is false.

The archived generator replayed byte-identically, and an independent program
reconstructed representative determinant rows and direct cyclic products.
The authoritative manifest is
`results/moving_ray_uniform_2adic_hashes.sha256`
(manifest SHA-256
`1aa935b6b07ed07e2b576d4cc7aeb70e75804586c0ced49d992b16b13009b291`).

Item 152 sharpens the uniform fresh-prime target but does not close all rays,
the content deficit, or the irrationality question for $e+\pi$.

### 2026-08-28 — Corrected m-ray projection and recurrence barriers (item 153)

An audit of the proposed m-ray section found that palindromy had been applied
to $W_s=z^{p-q}H_s$ instead of to the reciprocal polynomial $H_s$.  The
resulting same-A formula was therefore discarded and was never admitted as a
theorem.  For



$$
G_m(z)=\frac{(1-z)^{10m+3}}{(1-z^4)^{4m+3}},\qquad
 A_r=[z^{p-6m-r}]G_m,\quad B_r=[z^{p-r}]G_m,
$$



the corrected conditions are



$$
D_1=A_1-B_8,\qquad
 D_2=A_2+A_3+A_4-B_5-B_6-B_7.
$$



Finite reflection and pole projection prove exactly



$$
D_1=2^{-2m-4}\Lambda_2,\qquad
 D_1+D_2=2^{-2m-2}\Lambda_1.
$$



Thus the corrected window is a coordinate change of the original unresolved
log-residue pair, not a new coprimality mechanism.  The direct audit passes
14 representative prime cases.  A separate exact scan through $m=1000$
finds that the common denominator is always a power of two and the gcd of the
scaled pair divides $(6m)!$.  This is finite evidence only.

The weighted-Cayley calculation proves the existing short relation and its
exact five-term recurrence, but explicit terminal examples show that those
conditions alone can preserve nonzero modes.  At the next row, the complete
formal simple-pole Hermite matrix for a uniform three-term telescoper has
determinant



$$
2^9 3^7 7(q-3)(2q-9)^2(5q-9)(5q-6).
$$



On valid rays its only relevant rank drops are $p=7$, with no recurrence
coordinates, and $p=10m+3$, which supplies only the already-known
$B_2=0$ and no $B_3$ term.  This rules out that uniform nonresonant
three-term propagation mechanism, but not prime-specific higher-pole
characteristic-p certificates.

Finally, the independent inverse-cubic representation



$$
\Lambda_s=2^{2m+2s+1}[z^{4m+s}]
 \frac{A(T(z))^{6m}}{\phi'(T(z))},
 \quad \phi(t)=t^3-2t^2+2t,
$$



has generic differential order three.  Using the required total derivation
$\partial_z+\phi'(t)^{-1}\partial_t$ gives an eight-term coefficient
recurrence with shifts $-4,\ldots,3$, not the false shorter recurrence
obtained by omitting $\partial_z$.  At the target row the three known zeros
leave five other coefficients, so there is no immediate one-row pivot.  This
does not exclude a multi-row or global recurrence argument.

All five JSON outputs replayed exactly.  The authoritative manifest is
`results/corrected_fresh_prime_structure_hashes.sha256` (manifest SHA-256
`d095032d3667d0c7fdc5a2c80d63db820d493a5597f2fb4041a942e1bc7102fa`).

The remaining targets are the global recurrence/Cartier-line problem, the
cyclic two-coefficient support theorem, prime-specific resonant certificates,
and additional prime-power content.  Item 153 does not decide $e+\pi$.

### 2026-08-28 — Global trace-polynomial recurrence barrier (item 154)

Let $T_0,T_1,T_2$ be the three inverse branches of
$\phi(t)=t^3-2t^2+2t=z$, and put



$$
F_i(z)=\frac{(-2+3T_i-T_i^2)^{6m}}{\phi'(T_i)}.
$$



Their trace is exactly



$$
S_m(z)=\sum_{i=0}^2F_i(z)
 =[t^2]\operatorname{rem}_t
 \bigl((-2+3t-t^2)^{6m},\phi(t)-z\bigr).
$$



Lagrange interpolation proves that this is an integer polynomial.  A residue
calculation at infinity proves



$$
\deg S_m=4m-1,\qquad [z^{4m-1}]S_m=-10m.
$$



Consequently $S_m$ is nonzero modulo every prime $p>6m$, but every
coefficient from degree $4m$ onward is zero.  Each branch, and hence the
trace, satisfies the exact order-three ODE and all rows of its eight-term
coefficient recurrence.  The backward coefficient is structurally singular
at



$$
C_{-4}(4m+3,6m)=0.
$$



This supplies a global counterexample to any recurrence-only implication
from the target triple—or even the entire target tail—to vanishing initial
data.  It does not show that the distinguished branch $T_0(0)=0$ has a
zero target.

The natural quotient shortcut also fails uniformly.  For
$(m,p)=(2,112291)$, all eight forward pivots and the target-matrix
denominator are $p$-units, but exact reduction gives a rank-one
$3\times3$ target map and therefore a two-dimensional kernel.  One kernel
line is the trace; a certified second vector is not proportional to it.  The
distinguished initial vector maps instead to



$$
(24641,63218,21102)\pmod{112291},
$$



so this is a rank-drop counterexample, not a common-zero counterexample.
Independent three-branch series reconstruction verifies the same matrix and
vectors.

The authoritative manifest is
`results/inverse_cubic_trace_barrier_hashes.sha256` (manifest SHA-256
`8c74802d29da0a46772cfc40a1fd9f6691ff4325c55b60b7ebaea673c2de3235`).

The scalar recurrence and its trace quotient are therefore exhausted as
standalone mechanisms.  The active target is the intersection of every
rank-drop kernel with the distinguished Cartier/Frobenius branch line.  Item
154 does not decide $e+\pi$.

### 2026-08-28 — Distinguished inverse-branch/trace transversality (item 155)

For $n=6m$, the first three coefficients of the distinguished inverse
branch are $2^{n-6}V$, where


$$
V=(32,32-24n,9n^2-41n+36).
$$


If $\tau$ is the corresponding initial vector of the trace polynomial, an
exact conjugate-branch calculation gives


$$
\gcd(\tau\wedge V)=
 \begin{cases}
  2^{3m},&m\ \text{odd},\\
  3\,2^{3m+4}m(3m-1),&m\ \text{even}.
 \end{cases}
$$


Every odd factor on the right is smaller than a fresh prime $p>6m$.
Therefore the distinguished branch and the trace branch are independent
modulo every fresh prime.

Over $\overline{\mathbb F}_p$, let $\mathcal B_m$ be the span of the
three genuine inverse-branch series and evaluate their coefficients in
degrees $4m,4m+1,4m+2$.  The trace is always in this target kernel.  If the
distinguished target triple also vanished, the kernel would contain the two
independent series $S_m,F_0$; since $\dim\mathcal B_m\le3$, the intrinsic
target rank would be at most one.  This formulation is valid even on
$p=12m-1$, where the rational recurrence transfer from arbitrary initial
coordinates has $p$-denominators and is deliberately not reduced.

The result is a uniform rank-drop reduction, not a contradiction: rank-one
targets genuinely occur.  The certificate replays the exact symbolic gcds and
direct cubic-remainder samples through $m=20$.  The authoritative manifest
is `results/inverse_cubic_distinguished_trace_transversality_hashes.sha256`
(SHA-256
`a13e512197a4edaebc9bae4f77c253c6fe2c4ffc53d32ec9e0306b5989ca3432`).

The active arithmetic target is now to exclude the resulting distinguished
rank-one intersection.  A promising exact fixed-gap computation suggests
that the common connection/cube obstruction is supported only on a short
Pochhammer product, but no uniform proof of that support theorem is yet
available.  Item 155 does not decide $e+\pi$.

### 2026-08-28 — Exact three-branch initial determinant (item 156)

The normalized initial coefficient columns of the distinguished branch and
the two conjugate branches have determinant


$$
-\frac{i}{64}n(n-2)(2n-1).
$$


Restoring their exact column scales gives


$$
\boxed{\det(F_0,F_\alpha,F_{\bar\alpha})_{\{0,1,2\}}
 =-i\,2^{2n-7}n(n-2)(2n-1)},\qquad n=6m.
$$


Thus, for a fresh prime $p>n$, the three-branch initial-coordinate matrix
can lose rank only when $p=2n-1=12m-1$, and it does lose rank on that ray.
This exactly matches the denominator found in the arbitrary-initial-coordinate
recurrence transfer.  The intrinsic item-155 rank statement remains valid
there because it does not invert this matrix.

The symbolic determinant, conjugate formulas, trace remainder, and direct
samples through $m=20$ replay exactly.  The authoritative manifest is
`results/inverse_cubic_branch_initial_determinant_hashes.sha256` (SHA-256
`4a41baaea0a9c96a3dce08d916bb1fa450d8d069e00bab549a209f0f38fa5713`).

This is a coordinate-degeneracy classification, not a target-nonvanishing
proof.  The fixed-gap cubic Smith invariant remains the active obstruction.
Item 156 does not decide $e+\pi$.

### 2026-08-28 — Cubic Smith reduction for the fixed-gap cube obstruction (item 157)

For the explicit $3\times6$ multiplication matrix over
$\mathbb Z[1/6][X]/(X^3-4^{q-1})$, the twenty maximal minors have the
twelve stated forms.  A local DVR argument controls the two mixed cubic
minors and proves, uniformly for every admissible $q$,



$$
G_q\mid\Delta_3(q)\mid d_3(q)^3.
$$



Thus the desired support bound would follow from the still-missing
divisibility



$$
d_3(q)\mid P_q,\qquad
 P_q=\prod_{j=0}^{q-2}(2q-3-3j).
$$



The standard-library certificate checks all 334 admissible odd
$q\le1001$.  It verifies $d_3(q)\mid P_q$ and $G_q\mid P_q^3$ in
that finite range, but this is finite evidence only and is not promoted to a
uniform theorem.  Consequently, exclusion of every compatible fresh prime
remains conditional.

The authoritative manifest is
`results/mixed_cubic_cube_smith_reduction_hashes.sha256` (SHA-256
`b103dc33740f37b3da36a4bec611d603db4329d24f3c3b4a4b1d08fe759ac0ce`).
The shared independent audit and canonical JSON replay both pass exactly.
Item 157 does not decide $e+\pi$.

### 2026-08-28 — Cartier infinity-resonance barrier (item 158)

Under a hypothetical common residue zero, Cartier semilinearity reduces the
relevant differential to an exact rational differential on $\mathbb P^1$.
Global Hermite reduction yields



$$
D_A(V)=c_1Q-c_0,\qquad \deg V\le2p.
$$



The exact monomial formula



$$
D_A(z^d)=(d-q+1)z^d+\frac{5q-6}{3}
 (z^{d+1}+z^{d+2}+z^{d+3})+(1-d)z^{d+4}
$$



then gives the sharp dichotomy



$$
\deg V\le1\quad\text{or}\quad\deg V=p+1.
$$



Therefore the previously proposed degree-$\le1$ primitive bound is false.
Exact row reduction constructs degree-$p+1$ witnesses at
$(p,q)=(11,5),(31,13),(97,13)$, including the actual residue ratios.  All
three have $(B_0,B_1)\ne(0,0)$.  They are exact counterexamples to the
bounded-primitive step, not counterexamples to fresh-prime nonvanishing.  The
endpoint $q=1$ remains separately excluded by the elementary relation
$4\ne1$.

The authoritative manifest is
`results/mixed_cubic_cartier_infinity_resonance_hashes.sha256` (SHA-256
`5995e5ed1caa8a87310325de59c0a9f6717d3e0aa22b862f46b49ea0f1552c62`).
The active target is to eliminate the degree-$p+1$ mode using a branch-,
cube-, or Frobenius-line condition, or to prove the uniform Smith support
divisibility left by item 157.  Item 158 does not decide $e+\pi$.

### 2026-08-28 — Möbius and order-three structure of the fixed-gap obstruction (item 159)

For



$$
\omega_s=
 \frac{(1+t)^{1+3s}(1+t^2)^{\alpha-s}}
      {t^q(1-t)^q}\,dt,
 \qquad \alpha=\frac{2q-3}{3},
$$



exact endpoint reflection gives



$$
T_s=\operatorname{Res}_{t=0}\omega_s,\qquad
 C_s=-2^{-\alpha}\operatorname{Res}_{t=1}\omega_s.
$$



After synchronizing the branch $a=2^\alpha$, setting
$\xi=X/a$, and using $X^3=4^{q-1}$, one obtains



$$
\xi^3=2,\qquad
 \lambda_s=-\left(\operatorname{Res}_0\omega_s+
 \xi\operatorname{Res}_1\omega_s\right),
 \qquad
 \frac{\omega_{s+1}}{\omega_s}=\frac{(1+t)^3}{1+t^2}.
$$



On the Kummer curve $y^3=1+t^2$, the quotient is
$((1+t)/y)^3$, and all rows have the same deck character.  The relative
endpoint weight $\xi$ is not that deck eigenvalue.  The change
$S=2/(1+t)$ gives



$$
\frac{(1+t)^3}{1+t^2}=\frac4{S^3-2S^2+2S},
$$



so this construction is an exact coordinate bridge to the existing
inverse-cubic route, not a new order-three closure.

For $q\ge5$, divisor classification proves that the actual
$C_s\leftrightarrow T_s$ transform is uniquely the projective involution
$z\mapsto2/z$.  The genuine order-three map



$$
\sigma(t)=\frac{it+3}{t+i}
$$



preserves the Kummer branch set but sends the endpoint poles into



$$
\{0,-3i,3i\},\qquad \{1,2-i,2+i\}.
$$



Thus closing under the order-three orbit introduces four additional
endpoints; the original two equations do not form a closed PSL2 eigenvector
system.

Finally,



$$
P_q=\prod_{j=0}^{q-2}(2q-3-3j)
 =3^{q-1}(q-1)!\binom{(2q-3)/3}{q-1}.
$$



Every prime away from $6P_q$ is greater than $q-1$, so the relevant
length-$(q-1)$ factorial and Pochhammer factors are units.  This is a
necessary nonresonance statement, not the missing jet/Bezout reduction.

The standard-library certificate checks all 101 admissible odd
$q\le301$, and two independent regenerations are byte-identical to the
canonical JSON.  This finite run controls the symbolic algebra; it is not
the proof of the uniform identities.  The authoritative manifest is
`results/mobius_order3_fixed_gap_hashes.sha256` (SHA-256
`bcbf95b2f95bb1667186e40a197f7867bea84f9bff78ec98f830ef46757fb277`).

Item 159 proves a structural endpoint/Kummer reduction and a no-go for this
specific order-three PSL2 shortcut.  It does not prove $d_3(q)\mid P_q$,
uniform cube support, fresh-prime nonvanishing, or any classification of
$e+\pi$.

### 2026-08-28 — Actual-coordinate higher-power Cartier audit (item 160)

The higher-order Cartier/Frobenius ledger was independently recomputed using
exact algebra and directed interval arithmetic.  **PROVED:**



$$
\begin{aligned}
T&=h-d/2
  =1.1561471519642446123307302239\ldots,\\
r_1&=(-4\log2+6\log3-3)/6
  =0.1365141682948128184504238226\ldots,\\
T-r_1&=1.0196329836694317938803064012\ldots .
\end{aligned}
$$



The rank-two interval union remains only an absolute radical ceiling:



$$
C_2=0.8903637697614530752201860316\ldots\quad\text{per }m.
$$



Even granting every possible rank-two floor cell would give total
rank-at-most-two radical rate at most
$0.2849081299217216643204548279\ldots$ per $6m$, leaving
$0.8712390220425229480102753960\ldots$.  The old binary64-style decimal
tails in the mutable overviews were corrected without changing any theorem.

For each item-149 or item-151 forced prime, set
$q_p=p^{e_p}$ and
$\delta_{m,p}=\mathbf1_{p\in\mathcal P_m}$.  **PROVED:** for
$1\le r\le e_p+1$,



$$
p^r\mid c_m
\iff v_p(q_pA_m)\ge r+\delta_{m,p}.
$$



The rows $(m,p)=(3,3),(9,13),(4,7)$ prove respectively that a
prime-power denominator layer, an already removed $G_m$-digit, and a
rank-two determinant zero do not automatically yield $p^2\mid c_m$.
The $m=6,N=4$ row also proves that matching must use the primitive
coefficient: the correct $\Delta_m$ is $91$, whereas the raw coordinate
would give $1001$.  Its
$(v_7(c_m),v_7(\Delta_m),v_7(g_m))=(1,1,1)$ shows legitimate same-prime
overlap across three sequential reductions, not three independent Cartier
gains.

**EXPERIMENTAL:** the exact $m\le100$ census has 725 of 928 rank-one
forced pairs and 63 of 120 rank-two vanishing pairs sharp at one digit.  The
raw equal-valuation guess fails on 343 of 4,553 tested pairs; the simplest
affine next-digit guess fails in 50 of 51 eligible groups, with the sole pass
degenerate on four points.  These finite statements are not asymptotic.

**OPEN:** derive a genuine modulo-$p^2$ or integral Frobenius formula for



$$
\eta_{m,p}\equiv
 {q_pA_m\over p^{1+\delta_{m,p}}}\pmod p
$$



and prove its vanishing on a family with sufficient logarithmic mass.
First-level Cartier rank data alone admits lifts of arbitrarily large
valuation and supplies neither a second digit nor a useful finite local upper
bound.  The selected comparison matrix is singular on the content locus, so
standard inversion-based Dwork/Hasse--Witt machinery is unavailable there;
no theorem identifies it with the ambient Hasse--Witt operator.

The builder output replayed byte-identically, the adversary checker passed,
and the dependency manifests were rehashed.  The authoritative manifest is
`results/higher_power_cartier_actual_valuation_hashes.sha256` (SHA-256
`e50b59c2823a6d07375f6d8f05d363499f0e58a948bb541a6b98d57a41ff1e14`).
Item 160 improves the reduction, not the proved asymptotic content rate, and
does not decide $e+\pi$.

### 2026-08-28 — Exact endpoint Hasse bands, Bockstein lift, and sequential ledger (item 161)

The requested higher-$p$-adic endpoint formula was derived in two
independent forms and cross-audited.

For $K_s=4m+1+s$, $\alpha\in\{-1,i,-i\}$, set



$$
C_{s,\alpha}(r)=[t^r]\,
 {u(\alpha+t)^{6m}\over Q_\alpha(\alpha+t)^{K_s}},
\qquad
H_\alpha(n)=(-\alpha)^{-n}-(1-\alpha)^{-n}.
$$



If $q=p^e$ and $D=1+\delta_{m,p}$, define



$$
\mathcal B_{s,h}=
\sum_\alpha
\sum_{\substack{k\ge1,\ p\nmid k\\p^{e-h}k\le K_s-1}}
 {C_{s,\alpha}(K_s-1-p^{e-h}k)\over k}
 H_\alpha(p^{e-h}k).
$$



**PROVED:** exact partial fractions and the decomposition
$n=p^vk$ give



$$
qR_s\equiv\sum_{h=0}^{\min(e,D)}p^h\mathcal B_{s,h}
\pmod {p^{D+1}}.
$$



Substitution into



$$
qA_m=L_1(qR_0)-L_0(qR_1)
$$



therefore gives a finite exact formula for



$$
\eta_{m,p}\equiv {qA_m\over p^D}\pmod p.
$$



For $D=1$ this is a genuine modulo-$p^2$ lift with the $q$ and
$q/p$ bands.  For $D=2$ it is a modulo-$p^3$ lift with a possible
$q/p^2$ band.  The proof is termwise and does not invert a singular
comparison matrix.

An independent universal partial-fraction derivation confirms that modulo
$p^2$, resonant pole layers have indices $j=pk+1$, while every
nonresonant pole layer still contributes modulo $p$.  In the rank-one
determinant these many coordinate corrections collapse.  If



$$
\Theta=\gamma_1P_0-\gamma_0P_1=T',
\qquad
\eta=F^{p-1}F'T\,dx,
$$



then on every fixed positive-mass band, eventually,



$$
{L_1X_0-L_0X_1\over p}
\equiv
V_L\bigl(B-pR(\eta)\bigr)+V_RL(\eta)\pmod p.
$$



The $x^{p-1}$ coefficient of $\Theta$ cancels, so $T$ is
$p$-integral.  The formula never divides by a Cartier scalar.  When the
common pole order reaches $p$, separate terms in this quotient can lose
integrality; the direct band formula is then the safe form.

The exact actual row $(m,p)=(6,7)$ is a sharp lower-band obstruction:
literal top-band truncation predicts $3$, while the complete lift and
frozen coordinate both give



$$
\eta_{6,7}=4\pmod7,
\qquad
(v_7(U_6),v_7(V_6),v_7(c_6))=(1,2,1).
$$



A separate ambient-class construction proves that first-level Cartier data
and any fixed-precision bounded collection of local jets can agree while
determinant valuations differ arbitrarily.  This limitation is compatible
with the actual-family formula, whose precision and number of Hasse
coefficients grow with $p$.

The matching audit also proves the exact sequential primewise ledger.  If



$$
\kappa_p=v_p(c_m),\quad
\beta_p=v_p(V_m)-\kappa_p,\quad t_p=v_p(q_N),
$$



then



$$
d_p=v_p(\Delta_m)=\min(\beta_p,t_p)
$$



and



$$
\gamma_p=v_p(g_m)=
\begin{cases}
\min(\beta_p,v_p(P^*)),&\beta_p=t_p>0,\\
0,&\text{otherwise}.
\end{cases}
$$



Consequently



$$
v_p(c_m\Delta_mg_m)=\kappa_p+d_p+\gamma_p,
\qquad
c_m\Delta_mg_m\mid |V_m|q_N.
$$



The remaining exact sequential weight at the optimal beta scale is



$$
1.0196329836694317938803064012400587396\ldots
\quad\text{per }6m.
$$



**EXPERIMENTAL:** the Hasse certificate matches all 118 forced rows with
$m\le30$, with zero mismatches.  Deleting lower bands changes 64 digits;
45 complete digits vanish.  A separate $(46,11)$ check exercises the
rank-zero third band and agrees.  These finite counts are not a density or
mass theorem.

Three independent formula/sign audits and all standard-library replays pass.
The authoritative manifest is
results/lifted_endpoint_hasse_bockstein_and_sequential_mass_hashes.sha256
(SHA-256
0eaa6eb73068d776797425d15d13c4800dcc9452f09eac3e06bf2b3cd8214ada).

**OPEN:** prove a positive logarithmic-mass theorem for vanishing of the
complete digit, derive sufficiently many deeper digits, or obtain legitimate
sequential matching mass.  Item 161 supplies the missing exact formula but
does not decide $e+\pi$.

### 2026-08-28 — Congruence-slab square divisors and the two-layer capacity barrier (item 162)

The item-161 Hasse calculation was accelerated by the exact local recurrence



$$
(A_\alpha B_\alpha)F'
=\bigl(6mA_\alpha'B_\alpha-K_sA_\alpha B_\alpha'\bigr)F.
$$



Starting with $P+v_p((K_s-1)!)$ digits and debiting
$v_p(n+1)$ at step $n$ gives every required coefficient modulo
$p^P$.  Sixteen fast/slow comparisons pass, and the complete exact
$m\le100$ census contains



$$
\begin{array}{c|r}
\text{forced rows}&1048\\
\eta=0&260\\
\eta\ne0&788\\
\text{frozen-coordinate mismatches}&0\\
\text{digits changed by deleting lower bands}&734.
\end{array}
$$



The 1,048 rows are the disjoint union of 928 item-149 rank-one rows and
120 additional item-151 rank-two-zero rows.

The main new result is a genuine infinite square-divisor theorem.
Let $p\equiv19\pmod {20}$ be prime and assume



$$
p\mid10m+1,\qquad p\le4m+1<p^2.
$$



Writing $p=20k+19$ and $m=(9p-1)/10+\ell p$, exact division gives



$$
\begin{aligned}
6m&=(5+6\ell)p+r,&r&=8k+7,\\
4m+1&=(3+4\ell)p+t,&t&=12k+12.
\end{aligned}
$$



The two item-149 Cartier polynomials simplify to



$$
P_0=x^r(1-x^4)^r,\qquad
P_1=x^r(1-x)(1-x^4)^{r-1}.
$$



Their selected offset is



$$
p-1-r=12k+11\equiv3\pmod4,
$$



but their supports contain only offsets $0\pmod4$ and
$0,1\pmod4$, respectively.  Thus



$$
\gamma_0=\gamma_1=0.
$$



The degrees are



$$
\deg P_0=2p-3,\qquad \deg P_1=2p-6,
$$



so $p\in\mathcal H_m$, while $p\notin\mathcal P_m$ and
$\delta_{m,p}=0$.  The relative Cartier congruence gives



$$
(pR_s,L_s,E_s)\equiv(0,0,0)\pmod p,
$$



and the item-160 bridge proves



$$
\boxed{\eta_{m,p}=0,\qquad p^2\mid c_m.}
$$



The affine subray $\ell=0$, equivalently $9p=10m+1$, is infinite by
Dirichlet's theorem.  However, the whole congruence slab is thin at each
fixed $m$:



$$
\prod_{p\in\mathcal S_m}p\mid10m+1,\qquad
\sum_{p\in\mathcal S_m}\log p\le\log(10m+1)=o(m).
$$



Thus this exact infinite theorem does not improve the exponential content
constant.

The adversarial mass audit supplies a stronger route-level obstruction.
For the item-149 and item-151 radical weights $R_H,R_Z$, the first lifted
digit has extra weight



$$
E_\eta\le R_H+R_Z.
$$



Using



$$
r_1=0.1365141682948128184504238226\ldots,\qquad
\limsup {R_Z\over m}\le C_2
=0.8903637697614530752201860316\ldots,
$$



the radical plus a universal second digit has absolute ceiling



$$
2\left(r_1+{C_2\over6}\right)
=0.5698162598434433286409096558\ldots .
$$



This is below



$$
T=1.1561471519642446123307302239\ldots
$$



by



$$
0.5863308921208012836898205681\ldots .
$$



Even four complete surviving forced digits have ceiling



$$
4\left(r_1+{C_2\over6}\right)
=1.1396325196868866572818193115\ldots<T;
$$



five are the first count not excluded by this support capacity.  These are
ceilings on the present certification mechanism, not upper bounds on the
actual content.

The exact eta-plus-matching condition that would suffice after booking the
rank-one rate is



$$
\liminf
{R_{Z,m}+E_{\eta,m}
 +\log\Delta_{m,N_m}+\log g_{m,N_m}\over6m}
>
1.0196329836694317938803064012\ldots ,
$$



where $\Delta,g$ must be recomputed sequentially after division by the
full actual $c_m$.

Three independent replays are byte-identical to the canonical extended
census, divisor-evaluation, and slab JSON files.  The slab certificate checks
48,511 complete $e_p=1$ family members for 84 primes through $5000$, and
33 independent Hasse rows through $p,m\le500$, with no failure.

The authoritative manifest is
results/lifted_endpoint_hasse_congruence_slab_and_capacity_hashes.sha256
(SHA-256
a7be9bf216788457bf48c5b29862386bd31750c505621144123d390e09ee0670).

**OPEN:** positive linear-scale deeper-digit mass or a sequential matching
lower bound.  Fixed primes, sublinear support, finitely many affine rays, and
finitely many fixed polynomial-divisor rays have zero rate.  Item 162 does
not decide $e+\pi$.

## 2026-08-29 — item 163: exact deeper-digit tower and matching no-go audit

**PROVED.**  For each forced row, let $e=e_p$,
$D=1+\delta_{m,p}$, $\mathscr A=q_pA_m$, and
$\mathscr B=8B_m$.  If



$$
\mathscr A/p^D=\sum_{j\ge0}a_jp^j,
 \qquad
 \mathscr B/p^D=\sum_{j\ge0}b_jp^j,
$$



then



$$
v_p(U_m)=1+v_p(\mathscr A/p^D),
 \qquad
 v_p(V_m)=e+1+v_p(\mathscr B/p^D).
$$



Thus $p^r\mid c_m$, for $r\ge2$, is equivalent to vanishing of
$a_0,\ldots,a_{r-2}$ and
$b_0,\ldots,b_{r-e-2}$, with the latter list empty for $r\le e+1$.
An arbitrary-precision Hasse recurrence supplies the coordinate digits, and
integer determinant convolution with carries supplies the two normalized
minor towers.  This mechanism never divides by a Cartier scalar.

**EXPERIMENTAL.**  The exact $e=1$, $m\le100$ replay contains 784 forced
rows.  The counts surviving through powers $p^1,p^2,p^3,p^4,p^5$ are
$784,58,5,0,0$.  The five cubic survivors are
$(36,19),(67,17),(74,19),(89,19),(100,23)$.  There are no fourth- or
fifth-power survivors in this range.  Two replays are byte-identical, and
an independent slow-series/carry audit found no mismatch.

**PROVED.**  Sequential division by the full actual content has the exact
primewise ledger



$$
\kappa_p=v_p(c_m),\quad
 \beta_p=v_p(V_m)-\kappa_p,\quad t_p=v_p(q_N),
$$





$$
d_p=v_p(\Delta)=\min(\beta_p,t_p),
$$



and



$$
\gamma_p=v_p(g)=
 \begin{cases}
 \min(\beta_p,v_p(P^*)),&\beta_p=t_p>0,\\
 0,&\text{otherwise}.
 \end{cases}
$$



Therefore $v_p(c_m\Delta g)=\kappa_p+d_p+\gamma_p$,
$\Delta g\mid q_N^2$, and $c_m\Delta g\mid |V_m|q_N$.  Since
$q_N<4^{N-1}N!$ for $N\ge2$, any
$N_m=o(m/\log m)$ has zero matching rate.  Fixed or recycled beta indices
cannot supply exponential mass.

**PROVED, SCOPED NO-GO.**  Let
$K_m^{(0)}=K_m/\gcd(K_m,G_m)$.  Then $K_m^{(0)}\mid V_m$, its residual
part after actual content divides primitive $b_m$, and
$\gcd(K_m^{(0)},c_mq_N)\mid c_m\Delta$.  Even optimistically charging the
entire clearing reservoir once to $\Delta$ and once again to $g$, then
adding the proved rank-one rate, gives



$$
1+r_1=1.1365141682948128184504238226\ldots<T,
$$



with deficit
$0.0196329836694317938803064012\ldots$.  This ceiling applies only to the
rank-one-plus-clearing-reservoir accounting and deliberately overcounts
overlap.  It is not an upper bound for actual content or for unrelated
matching sources.

**PROVED.**  For products of distinct certified all-even antiperiod blocks,
the forced divisor $D$ and total forward span $W$ satisfy



$$
\log D\le {\log3\over6}W.
$$



Thus saddle-compatible span $W=O(m/\log m)$ also gives zero rate, even if
the final content factor is granted a second copy.

**EXPERIMENTAL.**  The exact 15,150-candidate replay gives late-window mean
rates $0.1845733550$ from $c_m$, $0.0320234811$ from sequential
matching, and $0.2165968361$ in total.  These are diagnostics only.

**OPEN.**  The remaining possibilities include positive-mass deeper-digit
vanishing, abundance and synchronization of distinct first-level singular
primes, deeper all-lift/Wieferich behavior, or a moving-index ordinary CRT
representative theorem outside the scoped reservoir.  A targeted primary
literature recheck dated 2026-08-29 found no result settling $e+\pi$.

The item-163 artifacts passed independent cross-audits and are pinned by
results/item163_deeper_digits_and_sequential_matching_hashes.sha256
(SHA-256
786ea03268a7e86ef11f7cdcff6a9fb20d07b28ec3bacc69c3493acc364ec2fe).
Item 163 does not decide $e+\pi$.

## 2026-08-29 — item 164: infinite slab tail and singular matching

**PROVED — infinite third layer.**  On the item-162 slab



$$
p=20k+19\text{ prime},\qquad
 m=18k+17+\ell p,
$$



the complete $e_p=1$ band is $0\le\ell\le5k+3$.  If
$6\ell+4\ge p$, then



$$
p^3\mid c_m.
$$



The second-Cartier transform is explicit.  If $P_s=T_s'$,
$F=u^a/Q^c$, $a=5+6\ell$, and $c=4+4\ell$, define



$$
N_s=T_s(au'Q-cQ'u)
$$



and



$$
H_s(x)=\sum_{n=0}^{5}
 \left(\sum_{j=0}^{p-1}[x^{pn-4j}]N_s\right)x^n.
$$



Then $H_s(0)=0$, $\deg H_s\le5$, and



$$
\Phi_s={u^{4+6\ell}H_s\over Q^{5+4\ell}}\,dx
$$



computes the next normalized $A$-minor digit.  In the tail,



$$
\Phi_s=\left({u\over Q}\right)^p
 u^{4+6\ell-p}H_sQ^{p-5-4\ell}\,dx,
$$



whose residual degree is at most $p-2$.  Hence both differentials are
exact in characteristic $p$, the next $A$-digit vanishes, and the
period-minor gate is already automatic.  The explicit infinite subray is



$$
20m=5p^2-17p-2.
$$



**PROVED — zero rate.**  Since $p\mid10m+1$ on every slab row, the product
of all selected primes at fixed $m$ divides $10m+1$.  The new third copy
has only $O(\log m)=o(m)$ mass.

**EXPERIMENTAL.**  The exact $m\le250$ census has 4,535 forced rows, 196
with $p^2\mid c_m$, and 14 with $p^3\mid c_m$.  All cubic survivors are
rank one with primes $17,19,23,29,31$.  The supplied tail condition has
one hit $(74,19)$ and zero misses.  The next eligible tail row is
$(m,p)=(643,59)$, outside the census.  Two full archive-input replays are
byte-identical with SHA-256
$3b67025624a350f5dc3e5b51db37be29fa7cbf8a9b3b647020e86a40f882dfc7$.

**PROVED — singular matching law.**  For a beta-denominator root
$r\bmod p$, put



$$
\lambda={q_r\over p}\pmod p,
 \qquad
 \delta={-q_{r+p}-q_r\over p}\pmod p.
$$



At $N=r+tp$,



$$
{(-1)^tq_N\over p}\equiv\lambda+t\delta\pmod p.
$$



If $\delta=0$, $\lambda\ne0$, and
$v_p(b_m)=v_p(q_N)=1$, then the final-content condition is independent of
$t$:



$$
p\mid g
 \iff
 {b_m\over p}p_r-(-1)^r\lambda a_m\equiv0\pmod p.
$$



When it holds, every parity-compatible lift contributes
$p^2\mid\Delta g$ while using only modulus $2p$.  If $\lambda=0$, all
lifts instead have $v_p(q_N)\ge2$, so level-one equal valuation fails and
deeper divided data are required.

**PROVED, SCOPED NO-GO.**  The product of distinct central singular primes
at one $N$ divides $2N+1$, giving zero saddle-scale rate.  Even granting
perfect singular doubling to every prime at most $3m$ gives matching rate
at most one.  Rank one plus that entire optimistic contribution is
$1.1365141682948128\ldots<T$, short by
$0.0196329836694318\ldots$.

**EXPERIMENTAL.**  Exact scans through $p=200000$ find only one singular
root, the central dead root $(79,39)$, and no all-lift root.  The complete
$m\le100,N\le6m$ matching replay has 190 singular $\Delta$-events but
only one final-content hit, outside the saddle window.  These counts imply
no asymptotic rarity theorem.

**OPEN.**  Classify or bound noncentral singular roots, synchronize a
positive-mass family above the support cutoff with actual $b_m$ and a
single saddle-compatible $N$, or obtain deeper all-lift/internal-digit
mass.

The item-164 archive-input packages are pinned by
results/item164_third_layer_and_singular_matching_hashes.sha256
(SHA-256
47b388115ff0c7f61dbac00d0cb01792b6f8abcc3973e510c94e37cfacd73a00).
Item 164 does not decide $e+\pi$.

## 2026-08-29 — item 165: noncentral singular resultant criterion

**PROVED — exact singularity test.**  For a noncentral root
$p\mid q_r$, with $1\le r<(p-1)/2$ and
$h=(p-3)/2-r$, define



$$
\mathcal K_h(X)=[X-4h,X-4h+4,\ldots,X+4h]
                 =X\mathcal L_h(X^2),
 \qquad D_h=\mathcal K_h'(0).
$$



The exact reflection transfer gives



$$
{q_r-q_{p-1-r}\over p}
 \equiv-2D_hq_{r-1}\pmod p.
$$



Adjacent beta denominators are coprime, hence the root is singular if and
only if $p\mid D_h$.  Moreover



$$
\operatorname {Res}_X(X,\mathcal L_h(X^2))=D_h,
\qquad
 \operatorname {Disc}_X(\mathcal K_h)
 =(-1)^h4^hD_h^3\operatorname {Disc}_T(\mathcal L_h)^2.
$$



The exact Lommel sum, cofactor-square formula, and five-lag recurrence for
$D_h$ were independently replayed.  General transfer identities passed
493 additional exact checks through $p=97$.

**PROVED, SCOPED NO-GO.**  The cofactor bounds imply



$$
\log|D_h|=2h\log h+O(h).
$$



For $p>3m$ at a saddle-compatible $N$, the index
$h=(p-3)/2-N$ moves with $p$ and is of order $p$.  Direct
resultant-height collection is therefore vacuous at the needed scale.  The
product of distinct noncentral dead singular primes above $3m$ divides
$q_N$, but the residual gap requires only
$0.0588989510\ldots m$ of log product, or
$0.0084007101\ldots$ of the asymptotic $\log q_N$ budget.  The bound is
far too weak to exclude closure.

**PROVED — recurrence-only countermodel.**  Modified initial data modulo
$107^2$ produce a noncentral dead-singular root at $N=50$, governed by
$D_2=963=3^2\cdot107$.  The modular initial pair is
$(8349,11050)$.  This shows that a genuine exclusion must use arithmetic
of the fixed Bessel seed; it is not an actual-seed example.

**EXPERIMENTAL.**  The exact certificate finds zero noncentral singular
roots among 146 direct roots through $p=2000$, and zero among 40 certified
large-prime divisors with $N\le80$ and
$200000<p\le65{,}676{,}881$.  The large-prime list is targeted rather than
exhaustive.  Root replay is byte-identical with SHA-256
$aad6db1438e4e9d8e6dd1a491b784b45b0e4bf1ac31517180f4042bd1a091014$.

**OPEN.**  Prove an actual-seed exclusion or a sufficiently strong product
bound for noncentral singular primes, or construct and synchronize a
positive-mass family with $b_m$, the final coefficient congruence, and one
saddle-compatible index.

The package is pinned by
results/item165_noncentral_singular_hashes.sha256
(SHA-256
2b84fe9ebe7f2e5a3520a5b5d5a9a4873fe3ba74f785649aff256e808647e066).
Item 165 does not decide $e+\pi$.

## 2026-08-29 — Items 166–167: fixed-seed singularity and the exact square ray

### Item 166 — prescribed left-factorial obstruction

**PROVED.**  With $P_0=1,P_1=3$ following the same homogeneous recurrence
as $q_r$, and



$$
b_0=0,\quad b_1=4,\quad
 b_n=(4n-2)b_{n-1}+b_{n-2}+4q_{n-1},
$$



the actual Bessel seed satisfies, for prime $p=2r+2h+3$ and
$p\mid q_r$,



$$
E_{p,r}:=P_r(!p)-b_r\equiv2D_hq_{r-1}\pmod p.
$$



The exact Wronskian



$$
P_rq_{r-1}-P_{r-1}q_r=2(-1)^{r-1}
$$



then gives



$$
P_rE_{p,r}\equiv4(-1)^{r-1}D_h\pmod p.
$$



Thus a noncentral actual-seed root is singular if and only if
$!p\equiv b_rP_r^{-1}\pmod p$.  This is also an exact
gcd/resultant-to-Euler-determinant bridge.  It is only a prescribed-residue
reformulation: known ordinary Kurepa work does not supply the required
avoidance theorem or a product estimate.  The saddle-scale radical bound
therefore remains $R_{m,N}^{>}\mid q_N$, which is quantitatively too weak.

**EXPERIMENTAL.**  There are zero singular examples among 344 noncentral
roots through $p=5000$, zero prime ties on the grid $r,h\le500$, and
zero among five certified sparse factors through
$p=3{,}092{,}690{,}659$.  The final continuant computation exceeds 1.5
billion exact modular steps.  A composite tie
$79\mid q_{39},D_{78}$, with $2\cdot39+2\cdot78+3=237$, confirms that
the prime tied-index hypothesis cannot be discarded.

The package is pinned by
results/item166_actual_singular_hashes.sha256
(SHA-256
e36888428aa5f6ec8ff6477d8c4fc0501c063377c91baf866a2099975a1dfa18).

### Item 167 — complete relative endpoint and exact valuation three

**PROVED.**  For every prime $p=20k+19$, put



$$
\ell=2k+1,\qquad m={p^2-1\over10}.
$$



The second Cartier layer has
$H_0=h x^4$ and $H_1=\lambda x^3+\mu x^4$.  The remaining relative
period is represented by an exact differential whose proper Hermite
primitive has both endpoints zero.  Algebraically, the two relevant
four-section sums are equal and vanish under
$r\mapsto(p-1)/2-r$.  This closes the formerly open endpoint step.

The following period digit is



$$
b_1=-2h\lambda\gamma\delta\ne0,
$$



so the valuation is exact:



$$
\boxed{v_p(c_m)=3.}
$$



**PROVED, SCOPED NO-GO.**  This is an infinite cubic family, but one prime
is attached to each $m$ and it divides $10m+1$.  Its contribution is
only $O(\log m)$, hence zero in the required exponential ledger.

**EXPERIMENTAL.**  All 38 primes $p\le1999$ on the ray pass two
byte-identical certificate runs.  Direct Hasse computations for
$p=19,59,79,139,179,199$ agree with the symbolic law.

**OPEN.**  Obtain positive weighted mass from cells outside the thin divisor
$10m+1$, or control the deeper all-lift/noncentral singular branch with a
synchronized saddle-compatible matching theorem.

The package is pinned by results/item167_p2_ray_hashes.sha256
(SHA-256
e4d338df527a709878eea4da5dbe9fa65fc98844597e9e5c6c8dabb36b21fd1a).
Neither item decides $e+\pi$.

## 2026-08-29 — Item 180: moving residual determinant

Item 180 derives an exact coefficient formula and four-term recurrence for
the full moving $\kappa=0$ rank-two determinant.  This turns the residual
root question into a deterministic $O(p)$ finite-field computation.

In the positive-lift sector $p\ge5s+2$, the corresponding integer
coefficients are nonnegative and exponentially large on compact linear
subsectors.  Four exact off-ray witnesses show why this does not settle
the arithmetic problem: their lifted determinants are nonzero integers
but vanish modulo $p$, and the associated content valuation is exactly
one.

A rigorous averaging lemma now isolates the missing input.  If the number
of residual roots satisfies $r_p=o(p)$, their mean log-prime mass is
$o(m)$.  The exact scan through $p\le1000$ finds 169 roots among
25,454 admissible pairs, never more than four for one prime, but no
asymptotic root-count theorem is claimed.

The authoritative manifest is
results/item180_moving_residual_hashes.sha256
(SHA-256
5a7bb46b73de560e8896b673411947cc5df77f9272de58139ac93739468e2689).
Item 180 leaves the status of $e+\pi$ unchanged.

## 2026-08-29 — Item 181: next-parity fixed bands

Item 181 evaluates the actual constrained rank-one $B_0$ contraction on
all fixed bands $s=(j\bmod2)+2$.  The exact rational obstruction is
nonzero for every $j\ge1$ and both prime residue classes, with uniform
sign


$$
\operatorname {sgn}\Omega^{(2),\#}_{j,\rho}=(-1)^{j+1}.
$$


Thus every such fixed band survives the $B_0$ gate for all sufficiently
large admissible primes.

At fixed $m$, the relevant primes divide $(2m+3)(2m+4)$.  Their
log-prime weight is therefore only $O(\log m)$, so this all-band theorem
does not create positive linear-scale support.

The authoritative manifest is
results/item181_next_layer_hashes.sha256
(SHA-256
1cbf15dc8e65068e09643c48bc6d8ef487f9ae846c632fe1e5e314ef7bd770ef).
Item 181 leaves the status of $e+\pi$ unchanged.

## 2026-08-29 — Item 182: endpoint-tail arithmetic

Item 182 derives an exact all-degree representation of the Item 179
endpoint value by exponential tails and two conjugate logarithmic tails.
The resulting explicit bound gains an order-$2^{-n}$ analytic factor,
but after full-content and endpoint-gcd reduction it still contains the
uncontrolled effective height $H_{BC}/d$.  The gcd cancels from the
relative approximation ratio.

Exact rational reconstruction and rigorous intervals were extended through
$n=45$.  Every nondegenerate value for $2\le n\le45$ has absolute
value greater than one; this remains a finite theorem only.

The authoritative manifest is
results/item182_endpoint_asymptotic_hashes.sha256
(SHA-256
c33197afe0e00d10be4e3d6a4ee11205d14b2036103d07be3e932d919a961e2c).
Item 182 leaves the status of $e+\pi$ unchanged.

## 2026-08-29 — Item 184: reverse-polynomial endpoint bound

Item 184 combines the shifted logarithmic tails into one exact integral of
the reverse polynomial.  This removes the old $n+1$ triangle loss and
gives the all-degree constant


$$
{(q+1)^2\over q^2q!}+{16+12\sqrt2\over q2^n},
\qquad q=2n+1.
$$


A rational majorant with constant 33 is strictly sharper than Item 182 for
every $n\ge2$.

The same item proves that content reduction, endpoint-gcd division, and
common rescaling cannot alter the effective or projective height ratios.
On the exact Item 179 rays, projective amplification is at least $4^n$
for $7\le n\le30$, and the improved generic bound remains above one.
The required all-degree control of the actual kernel direction is open.

The authoritative manifest is
results/item184_endpoint_height_hashes.sha256
(SHA-256
4da022fb579a75a065d79bb798ea5d7a6183ddf3c03582f443236b89565b764c).
Item 184 leaves the status of $e+\pi$ unchanged.

## 2026-08-29 — Item 185: moving-root structure and real sign

Item 185 rewrites the moving $\kappa=0$ determinant as a fixed-level
coefficient determinant for powers of two fixed rational maps.  This gives
exact bivariate rational generating functions and a terminating binomial
formula for every entry.

In the positive-lift sector, the integer determinant is strictly negative
for $p-5s-2\ge1$.  On the boundary $p=5s+2$, it is zero exactly for
$s\equiv1\pmod4$ and positive for $s\equiv3\pmod4$.  This complete
real-sign theorem does not control divisibility modulo $p$.

Natural structural-factor, factorial/gamma, and pivot normalizations retain
growing exact interpolation complexity.  The extended finite census through
$p=2000$ has 322 roots among 92,496 pairs, with a maximum of five at
$p=1471$.  No claim beyond that finite range is made, and the desired
$r_p=o(p)$ theorem remains open.

The authoritative manifest is
results/item185_moving_root_count_hashes.sha256
(SHA-256
cc069e5ba0530ab9f708ac67b0b94fd57f00fb2816d9a4352014c9d49d36edfe).
Item 185 leaves the status of $e+\pi$ unchanged.

## 2026-08-29 — Item 183 builder checkpoint (UNFROZEN)

The builder stopped at the consolidation cutoff after deriving a universal
obstruction formula, proving $5/4<a_L/a_R<4/3$, and checking the endpoint
signs exactly for all $0\le s\le199$ and both residue classes.  If the
checkpoint package survives replay and independent audit, it gives actual
constrained nonidentity on all parity layers $0\le\ell\le99$.  It is
preserved in `sources/item183_builder_checkpoint_unfrozen.md` and is not an
authoritative frozen theorem.  The unrestricted all-layer statement remains
open.

## 2026-08-29 — Item 174: rank-two determinant and fixed-band reduction

Item 174 completed the scalar-free entry and lift ledger for the regular
$e=1,\kappa=0$ cell.  With $\Delta_{p,s}$ the exact first-Cartier
determinant, its zero locus satisfies


$$
p^2\mid c_m\iff A_0=0,
\qquad
p^3\mid c_m\iff A_0=A_1=B_0=0.
$$


For fixed $s$, fixed $p\bmod4$, and $p\ge8s+3$, the determinant
reduces to an explicit rational constant $C_{s,\rho}$.  Exact modular
certification proves nonvanishing for both residue classes through
$s=256$.  This gives zero log-prime rate for every
$s=o(m/\log m)$ strip and every finite union of affine rays, but not for
the moving linear-scale locus.

The finite replay has 18,147 rows through $m=500$, 295 determinant-zero
rows and 127 distinct zero pairs.  The lifted census through $m=100$ has
46 first-layer, eight second-layer, and zero cubic survivors.  These are
diagnostics only.

The sole independent audit passed the proof, all nine manifest entries,
and a fresh byte-identical replay.  The authoritative manifest is
results/item174_ranktwo_nonscalar_hashes.sha256 (SHA-256
c33d20f2844c0163e9eda86c5a94c4437119fe29cf2ea11c395fef62b18e5aa4).
Item 174 leaves the status of $e+\pi$ unchanged.

## 2026-08-29 — Item 175: fixed-band circular nonidentity

For


$$
F_j={u^{3j+2}\over Q^{2j+2}},\qquad j\ge1,
$$


Item 175 proves $w^B_{j,1}\ne0$ for every $j$.  Thus the rank-one
five-divisor $B_0$ functional never collapses as a formal linear form on
a fixed band outside a finite $j$-dependent prime set.  A rational
exactness obstruction proves the result for all $j$; the finite
certificate is only a replay.

The item also fixes the exact-before-reduction convention for the
Bockstein primitive: arbitrary congruent Cartier lifts introduce an
$x^p$ term which cannot be omitted.  The theorem does not control the
actual constrained moving values $\bar T(a)$, so positive-mass
nonvanishing remains open.

After presentation and scope repairs, the sole independent audit passed
the proof and fresh byte-identical replay.  The authoritative manifest is
results/item175_fixed_band_hashes.sha256 (SHA-256
433f859f58d0676ac88893c1d00999c99c3438183afb1479a2d3da3fe22111b7).
Item 175 leaves the status of $e+\pi$ unchanged.

## 2026-08-29 — Item 176: native reciprocal Padé no-decay theorem

For $S(z)=e^z+4\arctan(z/(2-z))$, Item 176 takes $Q_n$ to be the
degree-$n$ Taylor truncation of $1/S$.  This uniquely gives


$$
-1+Q_ne^z+Q_nF=O(z^{n+1})
$$


with the same polynomial on the exponential and period columns.  An exact
Rouché argument finds one simple zero $r\in(-1/2,-2/5)$ in
$|z|<3/5$, so Darboux asymptotics force the endpoint remainder to grow
like $|r|^{-n}$.  After exact $n!$ clearing and endpoint gcd reduction,
the primitive value still diverges and its ratio to primitive height tends
to $e+\pi$.

The theorem is limited to $B=C=Q_n$ as polynomials; independent
endpoint-matched $B,C$ are not covered.  The independent audit passed all
analytic constants, gcd accounting, and a fresh replay.  The authoritative
manifest is results/item176_route2_native_reciprocal_hashes.sha256
(SHA-256
d4278012ff8984bf625d909c6e96c4ce44300214ce850d75292d1228dcb21710).
Item 176 leaves the status of $e+\pi$ unchanged.

## 2026-08-29 — Item 177: actual constrained fixed-band values

Item 177 symbolically evaluates the actual rank-one $B_0$ contraction.
On $(j,s)=(1,1)$, it is nonzero for every prime $p\ge7$.  On
$(j,s)=(2,0)$, the only zeros are $p=7,11$, and it is nonzero for
every $p\ge13$.  Exact rational primitives, Gaussian Frobenius branches,
prime-factor residue classes, and seven direct Hasse replays agree.

The audit also found and repaired an inherited circular-coordinate sign:
$\chi_4(p)$ now multiplies Item 172 (4.11) and Item 175 (4.1)/(4.3).
This negates old displayed contractions when $p\equiv3\pmod4$, but
changes none of the Item 172 counts $2649,119,104,10,8$, its ten
survivors, any zero-gate theorem, or any stored direct-Hasse digit.

The two actual slices are fixed rays and hence zero-rate.  The
authoritative manifest is results/item177_actual_fixed_band_hashes.sha256
(SHA-256
ba275161b2954148ab716e82e73689eea55c4bc2cd39d940b50da09cec24fcb8).
Item 177 leaves the status of $e+\pi$ unchanged.

## 2026-08-29 — Item 178: all minimal-parity fixed bands

Item 178 proves actual constrained nonidentity for every fixed band with
the smallest parity-compatible residual $s=j\bmod2$.  The Cayley
exactness obstruction has the uniform sign


$$
\operatorname {sgn}\Omega^\#_{j,\rho}=(-1)^j
\qquad(j\ge1,\ \rho=1,3).
$$


Three sign cases reduce immediately to positive coefficients.  The fourth
uses


$$
(2+4t+3t^2+t^3)^L
=\sum_{r=0}^L\binom Lr(1+t)^{L+2r}
$$


to prove the needed strict adjacent central-coefficient inequality.
Therefore the rational $B_0$ constant is nonzero in every band, and its
mod-$p$ reduction is nonzero for all sufficiently large admissible
primes.

The union over all $j$ is still zero-rate: its primes divide
$(2m+1)(2m+2)$, so their log-prime weight is $O(\log m)$.  A separate
audit checked the exactness reduction, Euler identities, sign proof,
admissibility, replay, and dependency chain.  The authoritative manifest is
results/item178_minimal_parity_hashes.sha256 (SHA-256
7473dd09c8ac514522045ad8f94d2e0f2191c0ddec819d93862d6e6435abd2ea).
Item 178 leaves the status of $e+\pi$ unchanged.

## 2026-08-29 — Item 179: independent diagonal endpoint tax

Item 179 separates maximal Taylor cancellation from the endpoint identity
needed for a native form in $e+\pi$.  In every degree, maximal
compatibility with $B(1)=C(1)$, an extra zero in the endpoint-matched
family, and singularity of one square matrix $K_n$ are equivalent.

Exact finite-field arithmetic proves $\det K_n\ne0$ for
$1\le n\le256$.  Thus the maximal independent family is unique but not
endpoint-matched, and imposing the endpoint equality costs exactly one
Taylor order throughout that range.  Fraction arithmetic through $n=30$
independently reconstructs the same projective forms.  After separate
full-polynomial and endpoint gcd reduction, every nondegenerate value in
that exact range has $|L_n|>1$, reaching decade $10^{1421}$ at $n=30$.
This is finite evidence, not an asymptotic theorem.

The independent audit checked the all-degree equivalence, modular integer
safety, exact reconstructions, rational $e,\pi$ intervals, gcd ledgers,
and fresh replay.  The authoritative manifest is
results/item179_independent_diagonal_hashes.sha256 (SHA-256
bb52e1bd256eeca881be05d32b2697b507a2afaa3d790a9ef6d021c587fb3763).
Item 179 leaves the status of $e+\pi$ unchanged.

## 2026-08-29 — Item 170: complete prime-square residue classification

**PROVED.**  On $10m+1=p^2$, the admissible classes
$p\equiv1,9,11,19\pmod {20}$ have actual first-Cartier ranks
$2,1,1,0$, respectively, and exact content valuations



$$
1,2,2,3.
$$



Explicit nonzero leading $\mathscr B$-digits prove all four upper bounds;
balanced proper primitives close the corresponding $\mathscr A$-endpoint
identities.  Thus the $19$-class is the unique cubic square class and the
entire locus has no fourth layer.

**PROVED, SCOPED NO-GO.**  Since $p^2=10m+1$, the total contribution is
only $O(\log m)=o(m)$.  It supplies no positive weighted mass.

**EXPERIMENTAL.**  A dependency-pinned replay checks 146 admissible primes
through $2000$, including 20 independent full-coordinate rows through
$200$, with byte-identical JSON outputs.

The package is pinned by results/item170_square_ray_hashes.sha256
(SHA-256
43084691d5d2c1ceffe7a761d2c61e01763650f82098af1606f7f7d014223395).
Item 170 leaves the status of $e+\pi$ unchanged.

## 2026-08-29 — Item 171: higher prime-power loci

**PROVED.**  If $10m+1=p^a$ with odd prime $p\ne5$ and admissible
$a\ge3$, then $p\mid c_m$.  The proof derives universal sparse
top-Cartier forms, gives an explicit all-exponent Lucas digit/rank table,
and closes the unique rank-two class $p\equiv1\pmod {20}$ by a relative
endpoint cancellation.

The exact lower ledger is at least two content copies in classes
$7,17,19\pmod {20}$ and for $p=3,a\ge8$, and at least one copy in all
other admissible cases.  This is not an exact deeper-valuation formula:
finite rows explicitly disprove $v_p(c_m)=a+1$.

**PROVED, SCOPED NO-GO.**  The unique base prime contributes only
$O(\log m)$; even the full top exponent has zero normalized mass.

An independent replay covers 479 symbolic rows and eight exact modular
rows, and an audit extension checks 3,122 admissible rank rows with no
discrepancy.  These finite checks are not density theorems.

The package is pinned by results/item171_prime_power_loci_hashes.sha256
(SHA-256
34f537abd6bc05e10634bad88d52009a04f7f9ef66423b00df12c497605166e4).
Item 171 leaves the status of $e+\pi$ unchanged.

## 2026-08-29 — Item 172: the rank-one non-scalar system

**PROVED — exact scalar-free gate.**  Canonical Hasse-coordinate digits and
their determinant carries give $A_0,A_1,B_0$ directly, with



$$
p^3\mid c_m
 \iff A_0=A_1=B_0=0.
$$



No Cartier scalar is inverted.  A first Bockstein reduces $A_0,B_0$ to
five evaluations of one reduced primitive; $A_1$ remains a true next
Hasse digit.

**PROVED — non-determination and thin certificate classes.**  Two exact
rows at $p=107,s=15$ share both exact Cartier coefficients and their
nonzero reduced pair but have different $A_0$.  Thus the scalar data do
not determine the first lift.  Separately, every zero family that is,
for each fixed band, contained in finitely many fixed polynomial
congruences has $o(m)$ total log-prime weight.  The proof combines an
$O_J(\log m)$ finite-band bound with an unconditional $O(m/J)$ tail.

**OPEN.**  The actual moving non-scalar system is not proved to satisfy
the fixed-polynomial hypothesis and may still carry positive mass.

The package is pinned by results/item172_rankone_nonscalar_hashes.sha256
(SHA-256
2ba8bcc7bd15832b2615509ac68c146a4b143d3aba2d6001cde51b8eb9019d2c).
Item 172 leaves the status of $e+\pi$ unchanged.

## 2026-08-29 — Item 173: rank-zero missing digit and boundary tail

**PROVED — scalar-free carry.**  After the two separate rank-zero
primitives, $\mathscr A/p^2$ and $\mathscr B/p^2$ are exact determinants
of integral reduced coordinates.  Their canonical carry gives the missing
$A_1$ without scalar division.

**PROVED — one-row tail extension.**  The coefficient filter satisfies



$$
H_s(1)=N_s(1)=-4(3j+1)T_s(1).
$$



It therefore adds $3j+1=p$ to the automatic exactness range.  Under
$3j+1\ge p$ and $2j+2\le p$, both first post-normalization gates vanish
and $p^2\mid c_m$.  The residual polynomial has degree at most $p-2$.

**PROVED, SCOPED NO-GO.**  This support obeys $p^2\le6m$, hence has zero
linear-scale log-prime mass.  The exact pair
$(m,p)=(54,17),(180,29)$ realizes $A_1=4,0$, respectively, so the tail
hypotheses determine neither cubic outcome.

The package is pinned by results/item173_rankzero_nonscalar_hashes.sha256
(SHA-256
83aac60f69a4e40d52de23b08364e7e2b6ae07f0d3fa8719041bb69d7f64d7e2).
Item 173 leaves the status of $e+\pi$ unchanged.

## 2026-08-29 — Items 168–169: complete $e=1$ cells and deeper all-lifts

### Item 168 — positive-mass cell classification

**PROVED.**  If $p\le4m+1<p^2$, write



$$
6m=ap+r,\qquad4m+1=bp+t,qquad\kappa=2a-3b.
$$



Every nonboundary rank-at-most-two row lies in exactly one of the cells
$\kappa=0,1,2$.  Their exact PNT interval masses are



$$
C_0=0.3370475079987658\ldots,
 \quad C_1=0.4820375017701113\ldots,
 \quad C_2\le0.8903637697614535\ldots.
$$



The first two are proved radical masses; the third grants that every
rank-two determinant vanishes and is only an absolute ceiling.  Even if
every prime on all three supports carried three complete content layers,



$$
{3(C_0+C_1+C_2)\over6}
 =0.8547243897651653\ldots,
$$



still short of the route threshold by
$0.3014227621990792\ldots$.

**PROVED, SCOPED NO-GO.**  On the rank-one cell, simultaneous vanishing of
the two first Cartier scalars together with $3j+1\ge p$ forces
$p^3\mid c_m$.  But the same hypotheses force



$$
p(p+1)\le6m.
$$



More generally, every second-Cartier proof which obtains exactness solely by
extracting a fresh $(u/Q)^p$ and using residual degree at most $p-2$
has only $O(\sqrt m)=o(m)$ prime weight.  The rank-zero analogue forces
only $p^2\mid c_m$: after the already removed first factor, the next
rational-minor digit remains uncontrolled.

The balanced simultaneous-scalar-zero locus is exactly the old
$p\equiv19\pmod{20}$, $p\mid10m+1$ ray.  The square locus
$10m+1=p^2$ splits into four residue classes; only the class 19 is
already proved automatically cubic in this item.  The deterministic scan
checks all admissible scalar pairs through $p=2000$, finding 38
simultaneous zeros and no off-balanced example.

**OPEN.**  Non-scalar cancellation in the three lifted digit systems may
still have positive mass.  The degree-tail theorem does not exclude it.

The package is pinned by results/item168_positive_mass_hashes.sha256
(SHA-256
4d64a5c573ecc91119897d09d9b1de4fcb602120c3753d5770c921e234272559).

### Item 169 — second divided-index law on a singular all-lift orbit

**PROVED, CONDITIONAL LOCAL THEOREM.**  Let $p\ge7$, let $r$ be an
actual-seed beta root, and assume the all-lift hypotheses



$$
\lambda_p(r)=q_r/p\equiv0,
 \qquad
 \delta_p(r)=(-q_{r+p}-q_r)/p\equiv0\pmod p.
$$



For $a_x=(-1)^xq_{r+xp}$, put



$$
P_r(T)=\sum_{j=0}^3{\Delta^ja_0\over p^2}{T\choose j}\pmod p.
$$



Then for every $N=r+tp+up^2$,



$$
p^3\mid q_N\iff P_r(t)=0.
$$



At a root, if $B_r$ is the integral degree-five lift and
$\kappa_t=B_r(t)/p$, the fourth digit is



$$
{(-1)^{t+u}q_N\over p^3}
 \equiv\kappa_t+uP_r'(t)\pmod p.
$$



This proves the complete ordinary/dead/all-lift trichotomy through $p^4$.
The derivative is also the divided $p^2$-index slope and the associated
continuant-square obstruction.

At exact common valuation two, the first matching digit is the cubic



$$
M_p(T)=\beta p_r-(-1)^raP_r(T).
$$



Unless it is an identity, it gives at most three parity-compatible classes
modulo $2p^2$, with $p^3\mid\Delta g$.  At exact valuation three the
next affine matching law generically gives at most three classes modulo
$2p^3$, with $p^4\mid\Delta g$.  The resulting product ceilings remain
well above both the full missing rate and the narrow
$0.0196329836694\ldots$ residual gap.  Thus raw capacity is not the
barrier; existence and moving-CRT synchronization are.

**EXPERIMENTAL.**  A byte-identical replay through $p=20{,}000$ finds no
noncentral singular or all-lift root.  The only singular row is the central
dead example $(79,39,12)$, which is outside the local hypothesis.

**OPEN.**  No actual-seed noncentral all-lift orbit is known.  Its abundance,
occurrence squared or cubed in the actual primitive coefficient, and
saddle-compatible simultaneous matching all remain unproved.

The package is pinned by
results/item169_deeper_all_lift_hashes.sha256
(SHA-256
06931148ac57dabfeb35b6b200727b728a15b228166dbc2a2a97dd9cda93b3a3).
Neither item decides $e+\pi$.

## 2026-08-30 — Route-order correction and Route-1 continuation

The user's controlling instruction was re-applied: Route 1 must either
succeed or be ruled out by a route-wide rigorous impossibility theorem
before Route 2 can be promoted.  No such Route-1 impossibility theorem
exists.  The Route-2 work in Items 176, 179, 182, and 184 remains preserved
but queued.

### Item 189 — moving-root collisions

The moving determinant root count $r_p=o(p)$ remains OPEN.  A proved
collision identity shows that a uniform Sidon theorem would give
$r_p=O(\sqrt p)$.  A local block-energy inequality shows that
$C_p(h)=O(h)$ on a suitable short-shift range would already give
$r_p=O(p^{2/3})$.  Exact shift identities have windows growing as
$O(h)$; direct elimination produced no verified bounded-degree
resultant.  The complete $p\le5000$ scan is Sidon but remains finite
evidence.  Canonical, replay, and an independent root replay agree.

### Item 191 — moving determinant lift gates

On every determinant-zero rank-two row satisfying


$$
3j-1\ge p,\qquad2j+2\le p,
$$


the first relative Bockstein is exact and the scalar-free gates satisfy
$A_0=B_0=0$, hence $p^2\mid c_m$.  This includes rank-one and zero-row
Cartier degeneracies without choosing a pivot.  The inequalities imply
$p(p+1)\le6m$, so the theorem has zero exponential capacity.  Exact
finite rows show that $A_1$ can vanish or not vanish.

### Item 192 — Frobenius-seed rigidity

For every first-Witt beta-seed lift,


$$
(\lambda,\delta)\mapsto(\lambda+c,\delta-2c),
$$


so $I=\delta+2\lambda$ is invariant.  A dead singular actual fibre cannot
be changed into an all-lift fibre.  At higher seed digits, the
anti-Frobenius branch is invisible while the periodic branch injects a
degree-$p-1$ parity function, leaving the fixed-degree Newton
architecture.  This is a scoped no-go for seed engineering only.

### Item 193 — paired actual-seed invariant

For a noncentral reflected root pair $r,s=p-1-r$,


$$
\delta_r=\lambda_r-\lambda_s,\qquad
\delta_s=\lambda_s-\lambda_r,
$$


and therefore


$$
I_r=3\lambda_r-\lambda_s,\qquad
I_s=3\lambda_s-\lambda_r.
$$


Both invariants vanish if and only if the actual pair is already all-lift.
An ordinary pair may have one zero invariant; the exact example is
$p=7$.  The one-sided condition is equivalently a shifted prescribed
left-factorial residue, with no known avoidance or density theorem.

All four packages were replayed, their dependency manifests validated, and
their reports copied into the archive.  The literature status was rechecked
on 2026-08-30; no accepted proof changing the open status was found.

### Item 194 — PNT-side rank-zero coupled gates

The PNT-side $\kappa=2$ cell now has the exact division-free
classification


$$
A_0=B_0=0
\iff \ell_{0,0}=\ell_{1,0}=0.
$$


The proof identifies the endpoint-map kernel, converts the nonzero-log
branch to four evaluations of two primitives, and eliminates it using the
factor $u^{r+1}Q^{2s}$ of degree $p-1$.  The remaining quotient
$\lambda x+\mu$ is killed by
$(p-8s)\lambda=0$ and $-(p-1)\mu=0$.  Thus cubic content on this
positive-mass cell is confined to the exceptional common-log locus and the
additional gate $A_1=0$.  No mass theorem for that locus is proved.

### Item 195 — two-point moments and the conductor barrier

An exact four-Hasse-jet inversion recovers all entries of the moving
rank-two determinant from moments of


$$
R(x)=\frac{x^3(1-x)^3}{(1+x+x^2+x^3)^2}.
$$


The pair at shifts $s,s+h$ shares one fixed moment space, with $h$
entering as an $R^h$ twist.  Teichmuller lifting realizes every pure term
as a bounded-conductor rank-one Kummer sum on a fixed six-punctured line.

This geometry does not itself control reduction at the selected prime above
$p$.  The exact Jacobi family
$\sum_t t^s(1-t)^s$ vanishes modulo $p$ on a linear interval while its
complex lifts have size $\sqrt p$.  Separately, removing the natural
extension's forced zero tail gives


$$
C_p(h)\le\deg\gcd(G_p(S),G_p(S+h)).
$$


No $O(h)$ gcd bound is proved.  The canonical/replay outputs and an
archived-layout replay agree, and the path-stable dependency manifest
validates.

### Item 196 — all-moving rank-one gate map

The $\kappa=1$ first-gate calculation has been extended from fixed
residual layers to every moving $s$.  A single prime-independent rational
primitive gives exact separated contractions for $A_0$ and $B_0$, with
all denominators automatically invertible at admissible cell primes.

The exact row $(m,p,j,s)=(11,13,1,3)$ shows why the earlier rational sign
method cannot finish the moving problem: its $B_0$-contraction is nonzero
over $\mathbb Q$ but zero modulo the actual prime.  Hence Item 196 is a
scoped no-go for a proof technique, not a route-wide impossibility result.
The moving modular zero count, the joint $A_0=A_1=B_0=0$ system, and any
positive improvement in the Route-1 exponent remain open.  The package was
replayed byte-for-byte and archived with a path-stable dependency manifest.

### Item 197 — common-log locus as simultaneous square divisibility

The two leading logarithmic coordinates on the PNT-side rank-zero cell
have been collapsed to fixed integer coefficients $C_0(m),C_1(m)$: a
cell prime is common-log exactly when it divides both coefficients to the
second power.  Consequently the exceptional radical squared divides their
gcd.

Smith-form bookkeeping shows that this gcd belongs to the existing
endpoint content rather than to a new reservoir.  The best direct Cauchy
height estimate permits rate $0.52730229545\ldots$ per $6m$, already
larger than the raw cell ceiling $0.05617458467\ldots$ per $6m$, so it
supplies no gain.  The default exact scan found
no common-log row through $p\le151$, but that nonoccurrence is recorded
only as FINITE evidence.  The host-independent checker and archived-layout
replay are byte-identical and the dependency manifest validates.

### Item 198 — exact actual-pair common valuation

The common valuation of a reflected noncentral beta pair is now an exact
integer gcd with its symmetric transfer continuant.  This yields necessary
and sufficient square and cube criteria and an explicit next divided digit.
At a prescribed lower index, however, the resulting all-lift radical only
satisfies $R_N^2\mid q_N$.  A modified-seed construction realizes this
ceiling while retaining adjacent coprimality and a unit Wronskian; because
it changes the actual seed, it is only a scoped information-theoretic
countermodel.  No actual useful-prime mass is proved.

### Item 199 — transfer barrier for recycled matching

The exact two-index determinant shows that common sequential matching
content at $N,N+h$ divides the beta transfer continuant.  At the frozen
saddle this gives zero rate for every $h=o(N)$, including any portion
left after already booked reservoir overlap is removed.  The nearest-gap
specialization also proves
$\gcd(T_N,T_{N+2},T_{N+4})=1$.  Shifts comparable with $N$, one-index
matching, and disjoint supports are not ruled out.  Both Item-198 and
Item-199 archive-layout replays match their canonical outputs exactly.

### Item 200 — removing the forced common-log layer

The two Item-197 integer coefficients share the entire already removed
Cartier product $F_m=G_m$.  A prime-interval subproduct has logarithm
$2m+o(m)$, and parity proves the pair is nonzero along $m=2^a$, so
raw gcd or radical bounds cannot be subexponential.  The actual exceptional
question is the normalized divisibility
$R_m\mid\gcd(C_0/F_m,C_1/F_m)$.

All PNT-side rows under study overlap the Item-149 booked primes.  An exact
four-step coefficient recurrence reduces the local common-zero conditions
to a rank-three matrix whose kernel is $(0,2,2,1)$ modulo $p^2$.
Accordingly, adjacent recurrence rows and their local resultant cannot
prove nonoccurrence; a cancellation-aware global transfer or a new
Frobenius/Witt input is still needed.  The corrected normalized raw-cell
ceiling is $0.05617458467\ldots$ per $6m$.  The archived package and
dependency manifest replay exactly.

### Item 202 — the actual squarefull radical's Euler filter

The fixed seed supplies a canonical residue $T_N$ modulo $q_N$.  An
exact congruence identifies the moving continuant derivative with the
left-factorial difference $L_p-T_N$, so actual paired all-lift is exactly
$p^2\mid q_N$ plus $L_p\equiv T_N\pmod p$.  Pushing one digit further
shows that the unresolved quantity is $(L_p-T_N)/p\pmod p$; the direct
p-adic Euler expansion contributes no Wilson quotient at this level.

A formal CRT construction shows only that first-residue local data do not
control that lifted digit.  It is not an actual arithmetic counterexample.
The exact scan through $p\le20000$ finds 1,133 lower root pairs but no
lower square or all-lift row; this is FINITE evidence only.  Canonical,
replay, and archived-layout certificates agree byte-for-byte.

### Item 201 — exact comparable-gap transfer cost

A path-matching expansion and gamma product give the sharp transfer
continuant asymptotic for all $h=O(N)$.  Its rate at the beta saddle is
exactly $\theta h/N$, so the former height ceiling was asymptotically
sharp.  A common reused block is nevertheless strictly dominated by the
beta-denominator displacement between its two endpoints.  Pure two-index
and one-parent-forest recycling therefore have zero net linear gain and a
strict finite polynomial loss.

Pluecker identities yield exact common-gcd and lcm laws for triples of
transfer continuants.  They close common-to-three reuse and show that
globally triple-free reuse is no larger than its unique CRT modulus, but
do not exclude pair-specific multi-parent packing.  That distinction is
recorded as OPEN.  The package passed canonical, bundled, and archived-
layout replay.

### Item 203 — global transfer without factorial clearing

The actual five-term coefficient state has an all-row support gap modulo
$p$.  Dividing by $p$ produces an exact five-coordinate Frobenius
defect, and a gauge classification proves these values are independent of
all singular choices in the recurrence modulo $p^2$.  This removes the
naive factorial-clearing objection.  The remaining direct input consists
of moving truncated-log defects of degree at least $2p-1$, so no
common-log mass theorem follows.

### Item 204 — explicit discriminant and independent Hensel digit

The beta denominator is the value at $-1$ of a monic reverse-Bessel
polynomial whose derivative resultants and signed discriminant factor
completely.  All target-range root primes are simple, yet their square
valuation is equivalent to vanishing of a separate first Hensel digit.
The coefficient-shift discriminant also fails as a sufficient condition in
the target range.  The exact scan through $p\le20000$ finds no lower
square row, but this remains FINITE evidence.  Both new packages replay
byte-for-byte in the archived layout.

The controlling decision after Item 204 is unchanged: Route 1 remains
ACTIVE and Route 2 remains QUEUED.  The accumulated scoped obstructions do
not amount to a route-wide impossibility proof.

## 2026-08-31: Route-1 continuation through Item 209

### Item 205 — localized Smith content of the moving rank-one vector

For the canonical cleared moving coordinates $(X_s,Y_s,Z_s)$, every odd
admissible prime satisfies


$$
v_p\gcd(X_s,Y_s,Z_s)=\min\{v_p(g_0(s)),v_p(g_1(s))\}.
$$


The exact resonance ray $p=5s+4$, $s\equiv3\pmod4$, forces common
first-gate content.  Its row primes divide $10m+1$, so the whole ray has
zero normalized weight.  The height envelope and singular local transfer
do not control all other moving prime divisors.

### Item 206 — universal first-gate kernel and rank stratification

An exact relative differential identity proves that the two pole-weight
rows for every $j$ share the kernel $(2,-1,-1)$.  Hence cross-$j$
determinants in this plane vanish identically and cannot support a Sidon or
two-point collision theorem.  On rank two, the joint condition
$A_0=B_0=0$ is equivalent to $p\mid g_0(s),g_1(s)$.  The entire
rank-zero interval $2j+3\le p\le3j+2$ is automatic but satisfies
$p^2\le6m$, hence zero rate.  Rank-one exceptions above this interval
are actual and remain unresolved.

### Item 207 — no extra exponent from combining Hensel and Euler filters

At a prescribed beta root, the Hensel digit and the continuant/Euler
coordinate are an invertible diagonal relabelling of the two actual
first-Witt coordinates.  The determinant is a unit, so no valuation or
third relation is gained.  The actual row $(p,N,h)=(7,2,0)$ realizes a
nonzero point on the kernel of the former scalar invariant, ruling out that
rank-one collapse.

### Item 208 — exact off-ray cancellation

The suggested implication


$$
p>3s+2, p\mid g_0(s),g_1(s)\Longrightarrow p=5s+4
$$


is false.  The exact counterexample is


$$
(s,k,p)=(299,899,2399),\qquad2399=8s+7.
$$


The universal Frobenius-phase reduction rewrites every common-content test
as two coefficients of one finite polynomial.  At $2399$ the zero is a
genuine cancellation, not a support gap.  The finite audit through
$s=1500$ and the targeted $8s+7$ scan through $s=5000$ find no other
off-ray point, but no extrapolation is made.

### Item 209 — exact second-lift carry and actual non-forcing witnesses

Writing $\mathscr A=L_1X_0-L_0X_1$, rank one first gives
$p\mid\mathscr A$; after $A_0=0$, the second exact division gives


$$
A_1\equiv\mathscr A/p^2\pmod p.
$$


Common moving content does not force this digit: the actual controls have
$A_1=16$ at $(s,p,j)=(3,19,1)$, $925$ at $(299,1499,1)$, and
$404$ at $(299,2399,1)$, while $(3,19,3)$ has $A_1=0$.
The automatic-anchor row $(j,p,s,m)=(2,7,0,10)$ also has $A_1=1$.

All five packages were independently replayed from the archive layout and
their manifests validate.  None improves the Route-1 exponent or proves a
route-wide impossibility theorem.  Route 1 remains ACTIVE and Route 2
remains QUEUED.

## 2026-08-31: Items 210--212

### Item 210 — exact endpoint rank and global tail ceiling

For every admissible prime, the two endpoint first-gate rows are rank zero
exactly in $2j+2<p\le3j+2$.  Above that interval they can only have rank
one or two, controlled by a single anchor $\mu_j=L_jH_j$ with
$H_j\ne0$.  The remaining rational obstruction is the explicit integer
coefficient $\ell_j=2^jL_j$.

An exact order-three telescoping recurrence verifies $\ell_j\ne0$ through
$j=20000$, with an independent binomial check through $j=80$.  Treating
every later band as fully exceptional still bounds the complete family by
$1/180009$ per $6m$, approximately $0.0283\%$ of the missing gap.
This is a rigorous capacity theorem from a finite prefix, not an extrapolated
all-$j$ nonvanishing claim.

### Item 211 — exact structural-ray carry

On the proved ray $s\equiv3\pmod4$, $p=5s+4$, the $j=1$ resonant
coefficients vanish over the integers by a support gap.  Retaining the
polynomial Cartier carry yields four sparse sums and the exact criterion


$$
A_1\equiv(5/24)\Phi_s\pmod p.
$$


The bounded scan through $p\le20000$ has no $j=1$ zero, but no
extrapolation is made.  The actual $(s,p,j)=(3,19,3)$ zero proves that
anchor changes matter.  The entire ray is rate-zero because all its row
primes divide $10m+1$.

### Item 212 — stable off-ray phase elimination

The two moving common-content coefficients now have an exact normalized
finite-sum formula in both Frobenius phases.  The old structural ray is the
only prime-feasible forced support gap.  In the stable region $b\le k+2$,
the common-zero test becomes


$$
p\mid N_0(b,r),N_1(b,r),
$$


where the two fixed integers depend only on $(b,r)$.  This exactly retains
the off-ray cancellation $(s,p,b)=(299,2399,900)$.

The phase-row identity $10m+1-b=(5j+5-q)p$ proves that every aggregate
$b=o(m/\log m)$ has zero normalized weight.  The region with $b$
comparable to $m$ remains open.  First-singularity compatibility alone is
also insufficient, as shown by the actual-family false positive
$(s,p,q,b)=(13,53,2,37)$.

All three portable packages passed independent and archived-layout replay.  No
positive Route-1 exponent is added, and no route-wide impossibility theorem
is proved.

## 2026-08-31: Items 213--214

### Item 213 — actual beta carry and slope

The beta denominator is the special value of the integer polynomial
$\mathscr C_N(X)=\sum_j{N\choose j}X^{\underline j}$.  Taylor expansion
between the complementary integers $-N-1$ and $p-1-N$ gives the exact
divided value


$$
q_N/p\equiv(-1)^N(\kappa-d^-)\pmod p.
$$


The reflected denominator shares $\kappa$ and has slope $d^+$; their
difference is the known continuant/resultant coordinate.  Hence lower square,
upper square, singularity, and coupled square are respectively the three
pairwise and triple collisions among $\kappa,d^-,d^+$.  This is an exact
coordinate description, but it is rate-neutral and the squarefreeness problem
is unchanged.

### Item 214 — exact finite stable-phase gcd audit

The two stable eliminants admit a shared first-order hypergeometric term
recurrence.  Phase reconstruction imposes a separate congruence modulo twenty.
At the known cancellation $b=900$, the full gcd has eleven odd prime
factors; ten are phase-infeasible and $2399$ is feasible.  Complete exact
factorization through $b=900$ finds no other feasible common divisor.

The bounded uniqueness is not extrapolated.  A proved
$O(b\log b)$ height bound is much too large after summing over moving
phases, so height alone supplies no linear-rate theorem.

Both packages passed canonical, independent, and archive-layout replay.  The
Route-1 exponent ledger is unchanged.

## 2026-08-31: Items 215--216

### Item 215 — binary candidate theorem and zero spacing

The diagonal anchor now has an exact 2-adic summand expansion.  A unique
minimum valuation is an all-input nonvanishing certificate; hence every zero
would require a tied binary-carry minimum.  A separate mod-four congruence
proves all carry-one indices nonzero.  The finite prefix through $j=20000$
contains no zero, but that observation is not extrapolated.

The proved order-three recurrence also excludes three consecutive zeros.
Using decreasing band weights, this lowers the entire unresolved tail ceiling
from $0.00000555527779\ldots$ to
$0.00000370388881791465\ldots$ per $6m$.  This improves a rigorous upper
bound but supplies no positive exponent.

### Item 216 — first-order telescoping no-go

There is a unique constant-coefficient contiguous residual for the two stable
off-ray sums.  Its term ratio is in Gosper normal form, and coefficient
comparison forces the impossible degree $(3b-8)/5$ on every actual
$p>5$ phase.  Small $b$ is resolved exactly.  The known
$(b,p)=(900,2399)$ common divisor survives in the residual, demonstrating
that the theorem is only a first-order method obstruction.

Both packages passed independent archive-layout replay.  The Route-1 exponent
ledger is unchanged; higher-order phase localization and tied-minimum
nonvanishing remain open.

## 2026-08-31: Item 217

### Retained-state common-log invariant

The five relevant Frobenius-defect coordinates factor through a fixed
four-entry $j$-vector.  For $j=1,2$, comparison with the frozen Item-197
coordinates gives necessary and sufficient primitive congruence pairs:


$$
j=1:\ 2Y'_0-Y_0=2Y'_1-Y_1=0,
\qquad
j=2:\ 9X_0-10Y_0+Y'_0=9X_1-10Y_1+Y'_1=0.
$$



Exact creative telescoping proves one all-index contiguous relation for the
raw coefficient pair.  Its primitive resultants and a rank-31 bounded-ansatz
calculation show that this mechanism supplies one projective line, not a
second condition forcing zero propagation.  A concrete normalization
counterexample proves that the relation cannot simply be divided by the
Cartier product.

Both thin phase edges are unconditionally rate-zero.  The two fixed cell
masses are $1/36$ and $1/105$ per $6m$; excluding both would be enough
to cross the remaining optimistic gap, but no all-prime exclusion has been
proved.  The finite replay through $p\le199$ has no simultaneous collision
and is not extrapolated.  The Route-1 exponent ledger is unchanged.

## 2026-08-31: Item 219 (Item 218 remains in progress)

### The fixed $j=2$ beta-period gate

Using reciprocity and endpoint antiderivatives at $1,i,-i$, the $j=2$
common-log pair becomes two explicit sums with a four-periodic weight.  All
denominators are nonzero modulo the admissible prime, so this is an exact
all-prime reformulation rather than a finite pattern.

A boundary-free scalar twisted-Hermite reduction below Frobenius degree is
uniformly inconsistent.  The exact augmented determinant
$2304s(2s+1)^2$ is a unit throughout the cell.  The theorem does not exclude
Frobenius-resonant primitives or non-scalar cohomological remainders, and hence
does not prove the cell empty.

The deterministic scan checks 1,153 rows through $p\le401$, including
separate zeros of both coordinates but no common zero.  It is retained only as
experimental exact evidence.  No rate is booked and the paired fixed-cell
threshold remains open.

## 2026-08-31: Items 218, 220--221

### Item 218 — exact $j=1$ tails

Palindromy converts the two common-log coordinates into rational tails of
$\log(1+z^2)$.  A unique bounded-degree twisted derivative gives an all-index
four-term transfer.  Exact factorization and phase-resultant checks exclude
all rows on $0\le h\le8$, uniformly in $s$.  This thin strip has zero
linear weight, and unbounded $h$ remains open.

### Item 220 — Euler endpoint basis

For both fixed cells, a nonresonant Euler resolvent removes the finite-log
kernel and leaves three endpoint coordinates per moment.  The actual $j=1$
and $j=2$ pairs are explicit linear functionals of those coordinates.
One-good-prime rank certificates prove exact nullity zero for the stated
degree-at-most-eight linear and affine-Bezout ansatz.  No claim is made beyond
that bounded scope.

### Item 221 — first resonance and residual cohomology

The first scalar $z^p$ resonance has endpoint functional 7 and is therefore
forced to vanish under the common gate.  A genuine quadratic remainder remains;
its three cohomology classes have an all-row nonzero determinant.  The common
gate reduces to one polynomial's shifted endpoint periods, but the final two
periods are arithmetically independent of the exhausted first-order mechanism.

All packages passed independent and archive-layout replay.  Their finite
noncollision scans are not extrapolated, and the Route-1 exponent ledger is
unchanged.

## 2026-08-31: Item 224

### Inhomogeneous Cartier terminals in the fixed $j=2$ cell

The shifted one-polynomial periods satisfy an exact five-term recurrence with
unit pivots in the full interior range.  At the first upper resonance the
apparently vanishing coefficient is $-p$, but its product with the resonant
primitive has the nonzero reduction $7(-1)^r$.  The lower endpoint similarly
contributes $11$.  These are exact regularized boundary terms, not numerical
fits.

For $s\ge2$, a certified $z^3$ twisted-de-Rham reduction puts every common
collision on one initial line.  Forward and backward propagation gives the
necessary compatibility


$$
\Omega_{p,s}=7(-1)^r\beta-11\tau=0,
\qquad \beta\tau\ne0.
$$


The canonical clearing is an integer and a $p$-unit, but its height is only
bounded by $O(p\log p)$, which gives no nondivisibility or zero-rate theorem.

The exact finite classification through $p\le401$ excludes 1,108 of 1,115
$s\ge2$ rows by $\Omega\ne0$.  The remaining seven formal-compatible rows
are all direct non-collisions, proving that compatibility is not sufficient.
The $s=1$ family and an all-prime or density theorem remain OPEN.  Root replay
was byte-identical, independently simplified the $z^3$ identity to zero,
and checked the two regularizations on all 1,115 finite rows.  No exponent or
capacity reduction is booked.

Before Item 224 promotion, the archive through frozen Item 221 was snapshotted
as `e_pi_research_20260826_backup_20260831T015730_route1_item221.zip` with
SHA-256 `a1aab7b4a3cbd6c5496329ff956c56b75d587576925773b60b9ce2e4e2e32043`.
All 2,701 source files matched the ZIP entries by path, size, and SHA-256.

## 2026-08-31: Item 225

### The second $j=2$ Cartier terminal

Deleting all primitive terms with exponent divisible by $p$ gives a single
exact forcing formula for the shifted five-term recurrence.  It recovers the
first terminal weight 7 and gives second-terminal weight 29.  The exact
coefficient at the second singular pivot is $-2p$, so its multiplicity is
retained and cancels the primitive denominator $2p$; no factor two is lost.

The homogeneous freedom born at the first resonance has generating polynomial
$g=(1-z)^r(1+z)(1+z^2)^{2s}$.  The all-row inequality
$\deg g<p-4$ for $s\ge2$ makes that mode identically invisible to the
second terminal.  Eliminating the common initial scalar therefore proves the
new necessary system


$$
\beta\tau\ne0,\qquad \Omega_{p,s}=\Psi_{p,s}=0.
$$



Each of the seven $\Omega=0$ rows through $p\le401$ has nonzero $\Psi$,
and hence the finite joint census is empty.  This remains EXACT FINITE only;
simultaneous all-prime or zero-rate control is OPEN.  Root audit replayed the
full forcing identity on 175 rows, including every former survivor, and the
archive replay is byte-identical.  No exponent or capacity reduction is
booked.

## 2026-08-31: corrected Items 222--223

### Item 222 — all-phase $j=1$ eliminant numerator

The actual phase $p=6s+4h+3$ specializes the Item-218 eliminant to a
rational value with an explicit integer numerator $A_h$. Every clearing
factor is a $p$-unit, so a collision implies $p\mid A_h$ for all
admissible $h$, not merely in a scan. The individual height
$O(h\log h)$, however, sums too expensively in the moving range. A
degree/order-at-most-eight recurrence ansatz is ruled out by exact modular
determinants, but larger or different collective structures remain open.

### Item 223 — corrected two-source boundary transfer

The two endpoint conditions share one order-three Pearson moment recurrence
and force the initial state onto $\langle(1,1,-1)\rangle$. Direct
unreduced-moment audit shows that the lower and upper terminal multipliers are
$p$ and $2p$, with sources $-2\epsilon$ and $-4\epsilon$. The first
draft's equal-source condition was therefore retracted before archive
integration. Correctly, every collision must obey


$$
\Delta_+=2\Delta_-\ne0.
$$


The diagonal involution gives $\Delta_+=\Delta_-$, proving noncollision on
every actual diagonal $r=2s$. Twenty-two off-diagonal determinant survivors
occur through $p\le2000$, and none is a direct collision; this is finite
evidence only. Both packages passed byte-identical archive replay and add no
bookable exponent.

## 2026-08-31: Item 226

### Four-phase Cartier closure in the fixed $j=2$ cell

The exact regularized recurrence advances one full prime phase by
$Y_{q+1}=MY_q+bW(qp)$. The omitted primitive at the $q$-th terminal has
denominator $qp$, while the unreduced pivot is $-qp$; their multiplicity
cancels exactly. The endpoint weights have the four-cycle $7,29,11,-11$,
and the finite-period coefficients are invariant under a $4p$ shift.

Consequently a hypothetical collision must solve nine affine scalar equations:
one bottom equation, four terminal equations, and four closure equations. Exact
augmented rank gives the complete formal-solvability criterion. On rows with
$\det(I-M^4)\ne0$, the fixed point is unique and this closure recovers the
original gate exactly. The bounded census through $p\le401$ has no formally
solvable row among 1,115 cases, including 15 singular-determinant cases, but
the census is not extrapolated. Root replay extended the direct phase-identity
checks through $p\le251$. No rate or capacity is booked.

## 2026-08-31: Item 228

### The second $j=1$ Frobenius source

Deleting the primitive monomials with denominators $ap$ turns the exact
Pearson identity into a forced recurrence. The next terminal has pivot $3p$:
before regularization its unique pole contributes
$p u=\ell_{3p-1}/3=2\epsilon/3$, and the factor three gives the source
$+2\epsilon$. A separate deleted-derivative calculation confirms the sign.

The first free response is exactly the coefficient sequence of
$(1-z)^r(1+z^2)^{2s-1}$, whose support vanishes at all three entries of the
new terminal. This produces an additional necessary invariant $\Psi$. Every
one of the 22 corrected Item-223 finite survivors through $p\le2000$ fails
it, but this empty bounded joint census is not extrapolated. The extended root
replay checked 304,599 individual forcing steps through $p\le401$. No
bookable exponent is added.

## 2026-08-31: Item 229

### The incomplete-binomial coordinate in the fixed-$h$ $j=1$ determinant

Exact triangular Gosper reduction writes the corrected transfer determinant as


$$
\Theta_h(s)=c_h(s)S_s+t_{s+1}G_h(s)-2\Delta_-(h,s),
$$


where $c_h$ has degree $2h+1$ and nonzero leading coefficient
$-2^{4h+2}/(2h)!$. This proves only that the displayed polynomial
antidifference ansatz retains $S_s$; it does not prove non-rationality,
algebraic independence, or the impossibility of another cancellation. The
phase proportionality through $h\le80$ and the empty finite intersection
through $p\le2000$ are recorded as EXACT FINITE.

## 2026-08-31: Item 227

### Order-four control and the terminal ceiling in the fixed $j=2$ cell

The endpoint-weight map conjugates the feedback transfer to the four-cycle,
proving $N^4=I$, full observability, and an exact cyclotomic/control
factorization of $\det(I-M^4)$. A left-null classification proves that every
singular affine closure is consistent. The canonical path has no $-1$
Fourier mode, while lower-terminal reciprocity fixes phase 4; consequently
the last two phase residuals are algebraic combinations of $\Omega$ and
$\Psi$. Continuing the same four-periodic functional cannot produce a third
invariant. This scoped no-go books no capacity.

## 2026-08-31: Item 230

### Antiperiodic affine closure in the fixed $j=1$ cell

Retaining the exact $ap$ terminal multiplier gives one phase-independent
affine transfer and the normalized four-cycle $(-4,2,4,-2)$. Direct
coefficient sums prove $2p$-antiperiodicity, so the lower terminal, the next
two upper terminals, and three antiperiod coordinates form six equations in
one scalar. Their augmented-rank condition contains the earlier $\Theta$
and $\Psi$ invariants. On regular rows it is equivalent to the original
common-log gate by uniqueness and backward unit propagation.

All 2,435 rows through $p\le601$ are finitely inconsistent; three have
$\det(I+M^2)=0$. Independent replay extended the census to $p\le701$,
where five determinant-zero rows occur and none is formally solvable. These
bounded facts are not extrapolated. The all-prime rank locus and singular
family remain open, and no exponent is booked.

## 2026-08-31: Item 231

### One coefficient formula for the second $j=1$ resonance

The normalized recurrence solution has an integrating-factor expansion whose
first two Frobenius poles are governed by $g_a$ and $g_{a+p}$.  Exact
coefficient comparison removes the propagated scalars from Item 228 and proves
that a collision must satisfy


$$
g_a=2\Delta_-\ne0,\qquad g_{a+p}=-\Delta_-.
$$


Frobenius rewrites the defect $g_{a+p}-g_a$ as one polynomial coefficient;
palindromic reversal gives an exact finite reciprocal-binomial sum.  Gosper
reduction leaves a fixed-parameter incomplete sum.  Root replay is
byte-identical, a standalone recurrence/coefficient audit covers 329 rows, and
the extended census through $p\le2500$ has 29 first-condition survivors but
no joint zero.  The latter remains finite evidence only.

## 2026-08-31: Item 232

### Algebraic generating function for the diagonal incomplete sum

Lagrange inversion gives an algebraic generating function and exact factored
order-two recurrence for
$S_n=\sum_{j=0}^n(-1)^j\binom{2n+j-1}{j}$.  The same sequence and equivalent
formulas already appear in OEIS A371813, so no novelty is claimed.  The key
scope result is negative: this diagonal recurrence changes both the upper
endpoint and the binomial parameter, whereas Item 231's obstruction keeps the
row parameter fixed.  It therefore supplies no legitimate adjacent-row
elimination of the live coordinate.

## 2026-08-31: Item 233

### Exact redundancy of the remaining $j=1$ phase equations

The endpoint observability map diagonalizes the feedback shift into the modes
$1,i,-i$, giving an exact two-square expression for
$\det(I+M^2)$ and a complete singular-rank split.  Every singular affine
closure is consistent.  A coefficientwise residual identity, valid without
determinant division, proves that all six Item-230 phase equations reduce to
the already known $\Delta_+\ne0,\Theta=\Psi=0$ terminal system.  Additional
phases of this functional cannot provide a third invariant.  This is a scoped
structural no-go, not an exclusion of the simultaneous-zero locus, and no rate
is booked.

## 2026-08-31: Item 236

### All-$h$ cokernel proof of the phase-residual identity

The unique residual of the polynomial Gosper operator is computed by a finite
falling-moment functional $\Phi_s$.  Direct falling-basis algebra proves
$\Phi_s\mathcal L_s=0$, and coefficient extraction proves an exact
positive/negative binomial reflection.  At
$2r+6s_*+3=0$, the three reflected lower tops match the three upper tops in
reverse order, proving $c_h^+(s_*)=c_h^-(s_*)$ for every $h\ge1$.

The canonical replay through $h\le80$ and root extension through
$h\le100$ agree with the theorem.  The common residual's relation to the
Item-222 eliminant and endpoint scalar remains open, so no exponent or
capacity reduction is booked.

## 2026-08-31: Item 234

### The first actual $j=1$ coefficient Witt digit

An exact Frobenius expansion of the original integer coefficient through
order $p^2$ produces harmonic first corrections and a quadratic square.
Reflection and unreduced endpoint calculations give
$H_1=Q+2pR=-\epsilon M+pJ$.  On the original gate $p^2\mid C_\nu$, this
proves the explicit digit $C_\nu/p^2\bmod p$; the division is performed only
after the gate proves the required integrality.  A separate terminal theorem
retains every multiplier $ap$ and finds the squared-denominator carry in
lifted antiperiodicity.  The extended root census through $p\le2200$ has no
joint first-gate row, but that remains finite-only.

## 2026-08-31: Item 235

### Canonical $j=2$ Witt terminals are not yet the actual Witt bridge

The finite beta periods admit exact localized $p^2$ terminals and a harmonic
four-phase carry.  Unit observability proves that corrected closure lies in the
terminal-row span.  However, the original coefficient quotient and naive beta
lift differ by $3p$ at $(17,2,0)$.  The true second Frobenius digit contains
second-order linear and quadratic terms absent from the naive lift, and the
common initial line may also carry.  This exact scope barrier prevents any
capacity or rate claim from the canonical second-digit census.

## 2026-08-31: Item 238

### The squared carry is not a fourth first-digit endpoint mode

Comparing the exact regularized Pearson equations at $t$ and $t+2p$
produces a coupled recurrence between the ordinary moment $u_t$ and the
squared-denominator carry $v_t$.  A separate $t$-versus-$t+4p$
calculation proves it coefficientwise for arbitrary data in the endpoint-mode
space.  Since the ordinary terminal map is invertible on $1,i,-i$, the carry
triple equals $K$ times the ordinary triple on every phase.  One terminal
replaces one free digit by another and adds no scalar compatibility.

Root audit corrected one missing displayed plus sign, independently checked
the algebraic sign, reproduced the canonical output byte-for-byte, and
extended the direct and endpoint-map replays.  The relation to the actual
$p^3/\Omega^W$ gate remains open, so no rate is booked.

## 2026-08-31: Item 239

### The actual $j=2$ second digit

Expanding the two Frobenius defects through second order gives the quadratic
combination $21X^2+15Y^2-35XY$.  Exact section separation and reciprocity
then produce a corrected beta-period bridge with no unknown scalar.  It proves
the exact per-coordinate $p^3$-divisibility test and identifies why the
canonical lift in Item 235 missed the true digit.

Root audit checked the section coefficients and reciprocity signs, replayed
the package byte-for-byte, extended the exact-integer comparison, and used a
separate dependency-free implementation on 104 triples.  The latter also
reproduced the $p=17$ coefficientwise non-four-periodicity witness.  The
ordinary $p^2$ common gate and all-prime simultaneous-zero problem remain
open, so no rate is booked.

## 2026-08-31: Item 240

### The $j=1$ Witt digit and endpoint denominator tower

A termwise reciprocal-index calculation identifies Item 234's Hermite
functional $J_\nu$ with explicit short convolutions of the
squared-denominator sine endpoint moment.  On $p^2\mid C_\nu$, this gives
the exact extra-digit compatibility


$$
\Omega_\nu^W=-6\epsilon M_\nu^{(1)}
               +12\epsilon V_\nu^{\sin}+E_\nu.
$$



The derivative identity extends the coupled endpoint recurrence to every
denominator power $k\ge2$, and every terminal map factors through the
ordinary three-mode endpoint map.  No denominator level creates a fourth
mode.  The surviving $E_\nu$ functional is provably independent of the
six level-one/level-two endpoint functionals on
$\mathbb F_{29}[z]_{\le16}$; this is a universal-linear obstruction only.
Root replay verified the bridges, recurrence, terminal factorization, exact
rank minors, and tower tests.  Actual-family reduction of $E_\nu$ remains
open, so no common-log rate is booked.

## 2026-08-31: Item 237 (late freeze)

### Algebraicity and recurrence of the common $j=1$ residual

Residue substitution removes $h$ from the Item-236 coefficient kernel and
expresses $c_h^*$ as $[x^{2h}]C(x)$, with $C$ rational on an explicit
degree-six parametrized curve.  Exact elimination gives a primitive
bidegree-$(9,6)$ algebraic equation.  Substitution into a differential
operator proves an all-$h$ order-three, step-three recurrence; the cleared
operator numerator is identically zero.

The proposed hypergeometric gauge to Item 222's $E_h^*$ remains finite-only
because no bivariate WZ/Hermite divergence certificate is known.  Root audit
corrected an omitted $(-1)^j$ in one displayed definition, reproduced the
canonical output, and independently checked 82 direct values, 50 Lagrange
coefficient identities, 73 recurrence rows, and ten parametrized resultant
points.  No arithmetic nonvanishing theorem or rate is inferred.

## 2026-08-31: Item 241

### Character-harmonic collapse of the corrected $j=2$ kernel

Partial fractions collapse the $A_p^2$, $B_p^2$, and $A_pB_p$
coefficient sections to harmonic prefixes.  The mixed section introduces the
single character prefix
$\mathcal O_u=\sum_{j<u}(-1)^j/(2j+1)$.  The resulting full kernel has
closed parity formulas and exact seven-coordinate coefficient states.

The normalized odd coordinate $R_u=(-1)^u\mathcal O_u$ obeys an
inhomogeneous first-order recurrence with a nonzero source.  Thus the former
convolution array is no longer an obstacle, but its aggregate against the
actual binomial coefficients remains a bulk moment rather than a proved
terminal scalar.  Root audit independently reconstructed all convolution
components through $p=1009$ and replayed the archive layout.  Because this
kernel controls only an extra $p$-adic digit, no ordinary common-log rate is
booked.

## 2026-08-31: Item 242

### The full $j=1$ Frobenius kernel has a ten-level phase module

Putting the five Item-234 Frobenius terms over a common denominator produces
$\mathcal H_E=R_E/(1+z^{2p})^5$.  The resulting coefficient channels obey
the exact recurrence $(S_p^2+1)^5e=0$.  At each root of $1+z^2$, the
numerator times the actual row polynomial has order $2s+1<p$, so the
least common multiple of the reduced $p$-section denominators retains the
fifth power at both roots.

The initial draft overclaimed that one section retained both factors.  Root
audit identified the split-factor gap; the corrected proof makes only the
module-level claim.  An independent reconstruction verified the rootwise
multiplicities and exactly reproduced the rank-$6/7/8$ observation matrix.
The ambient rank theorem does not establish independence on the actual
binomial family, so no common-log rate is inferred.

## 2026-08-31: Item 244

### Abel reduction of the actual $j=2$ character coordinate

The exact parity projection of $P_\nu$ gives a closed factored polynomial
for precisely the odd denominators.  Applying the inhomogeneous Item-241
recurrence by summation by parts separates the aggregate into a known
endpoint boundary term and one terminally normalized residual
$\mathsf B_\nu$.  The only identically empty projection is
$\nu=0,r=1$.

Exact witnesses show that $\mathsf B_\nu$ neither vanishes universally nor
equals one common multiple of the old sine endpoint across both coordinates.
Root audit independently reconstructed the projection and Abel identity on
selected rows through $p=1009$, and an extended finite census checked all
rows through that bound.  No all-prime zero theorem or ordinary $p^2$ rate
is inferred.

## 2026-08-31: Item 245 (late freeze)

### Actual-family generalized $\pm i$ observation module

The exact target-section degree bound removes the fifth $Q$-adic numerator
digit, hence the separately excited old simple-pole pair.  Passing through one
canonical $Q(S_p)$ factor leaves the eight-dimensional module
$\mathbb F_p[Z]/Q^4$.  Multiplication by the actual numerator has norm
$(\alpha_\nu^2+\beta_\nu^2)^4$, which is also the determinant of the
normalized eight-phase observation matrix.

Alternating coefficient sums give $\alpha_\nu,\beta_\nu$ exactly, and
reciprocity maps both target sections to the same reflected residue without
equating their distinct polynomial weights.  Root audit independently rebuilt
all 368 coordinates through $p\le151$, verified the local and joint rank
criteria, and reproduced the frozen certificate.  The no-joint-drop census
through $p\le601$ remains finite-only, so no terminal obstruction or rate is
inferred.

## 2026-08-31: Item 246

### Closed form and recurrences for the $j=2$ bulk residual

Expanding Item 244's terminal tails gives a closed triangular rational sum and
an equivalent polynomial double integral.  Exact multiplication recurrences
for $1\pm t$, together with the parity-seed recurrence, produce a finite
row-parameter evaluation.  Reversal symmetry moves to a distinct pole, and
the $\nu=0,1$ pair necessarily brings in the opposite parity state.

Root audit independently verified the closed form, factor recurrences,
reciprocity, companion relation, and the exact
$-140105504768/121628516625$ witness at $p=37$.  Its numerator has
valuation one at $37$, disproving universal individual nonvanishing.
No simultaneous all-prime theorem or ordinary common-log rate follows.

## 2026-08-31: Item 247

### A one-seed eliminant for the $j=2$ residual pair

The actual congruence forces the Item-244 parameter $r$ to be odd.  The
shared selected-parity state first has a fixed determinant-two elimination.
Differentiating the even/odd decomposition of $(1-z)^{r-1}$ then expresses
the companion parity through the one odd seed whenever $r>1$.  The resulting
bookkeeping determinant is $2(r-1)$, which is a $p$-unit on every regular
prime row.

The exact singular locus is $r=1$, not an empty formal case; it gives the
prime family $p=6s+5$ and one remaining scalar.  A common denominator also
gives an integer pair whose gcd captures simultaneous modular vanishing
exactly.  Root audit independently checked the integer polynomial identities,
the Fraction-valued residuals, denominator clearing, and the
$(127,11)$ counterexample to nonvanishing of the eliminated scalar.  Neither
the gcd criterion nor the finite scans prove all-prime nonvanishing, and no
rate is inferred.

## 2026-08-31: Item 249

### Universal recurrence on the singular $j=2$ line

For $r=1$, the sole residual polynomial is
$(3-2t-t^2)(1+t)^{2s-1}$.  Exact expansion and the logarithmic derivative
give its coefficient formula and order-three row recurrence.  Reordering the
Item-246 triangular functional gives one alternating odd-denominator prefix
sum.

Writing $M=(p-2)/3$, termwise binomial reduction identifies the coefficients
modulo $p$ with the fixed series
$(1-t)(3+t)(1+t)^{-8/3}$.  Hence the residual is the universal rational
terminal value $\Theta_M\bmod p$, with a complete $p$-unit denominator
audit.  Root independently reconstructed the polynomial differential identity,
the recurrence, both functional forms, the fixed-series reduction, terminal
coefficients, and the exact excluded-boundary zero.

The boundary $p=11,s=1$ really vanishes, while the admissible scan through
$p\le20000$ has no zero.  The latter remains EXACT FINITE ONLY.  All-prime
admissible nonvanishing, any ordinary-gate consequence, and every rate or
capacity improvement remain OPEN.

## 2026-08-31: Item 248 (late freeze)

### Local logarithmic tails and the joint-root Wronskian no-go

Localizing at $I^2=-1$ turns each selected $p$-section of
$B_0^2P_\nu$ into one coefficient of the squared truncated logarithm times
four explicit linear powers.  Its logarithmic square has the exact harmonic
coefficient $8H_{k+1}/(k+2)$, and the four-factor part obeys a short Pearson
recurrence with unit pivots.

The two coefficients are second derivatives of parameter families with a
forced falling-factor.  Their common vanishing therefore forces a
division-free two-by-two Wronskian.  Correct split-root accounting finds exact
Wronskian root zeros at $p=109,149$, an individual seed root zero at
$p=41$, and an entire leading-pair zero at $p=59$.  Root independently
reproduced these witnesses and 66 direct coordinates.

These results disprove universal individual-pair and Wronskian-unit methods,
but not joint nonvanishing.  No common root appears through $p\le601$; that
statement and all census counts are EXACT FINITE ONLY.  The all-row common
root problem and every rate consequence remain OPEN.

## 2026-08-31: Item 250

### Affine Frobenius localization of the ordinary $j=2$ gate

Writing $p=2r+6s+3$ and $Q=2s$, the two moving beta tails are generated
by a common sequence $J_k$.  Its two-step recurrence has one Frobenius
pivot; the terminal summand at that pivot contributes one rather than zero,
so the correct localized odd seed is affine in $2^Q$.  This repairs the
homogeneous draft and agrees exactly with the frozen Item-219 coordinates.

The upper logarithmic tails retain a common factorial period.  A termwise
reciprocal identity makes their coefficient vector rank one with the common
$J_0$-period vector.  Division-free cross multiplication gives a linear
compatibility condition and, using $2^{2r+2}(2^Q)^3=1\pmod p$, a fixed-$r$
cubic resultant.  Separate inequalities audit every lower factorial, upper
factorial, hypergeometric string, phase denominator, and the sole retained
Frobenius denominator.

The necessary conditions do not characterize collisions.  Exact witnesses
at $p=67,367,953$ show cubic-only, linear-and-cubic, and one-gate false
positives.  Root independently reconstructed 85 rows and all three witness
types, then reproduced the sealed checker twice in an isolated archive
layout.  The $p\le401$ census is EXACT FINITE ONLY.  The actual remaining
period on the exceptional locus and all global arithmetic control are OPEN,
so the capacity and exponent bookings are exactly zero.

## 2026-08-31: Item 251

### Exact normalization of the exceptional ordinary $j=2$ period

The common even beta period and the common upper factorial tail share an
explicit factor $B_s$.  Their quotient leaves one integer diagonal $A_s$,
so the actual residual coordinate $Z$ is now known exactly rather than
treated as a formal compatibility parameter.  The determinant condition from
Item 250 plus one rank-aware residual equation is necessary and sufficient on
the nonzero coefficient-vector branch; the rank-zero branch remains separate.

The diagonal is a coefficient of $((2+x)^{3s-1}-1)/(1+x)$.  Lagrange
diagonal extraction gives its algebraic generating function, while a fully
specified bivariate exact derivative proves its order-two recurrence with
both endpoints retained.  Factoring by the $(-1)^s$ solution makes
$A_{s+1}+A_s$ hypergeometric, but recovering $A_s$ still requires an
alternating incomplete sum.

Exact admissible rows at $p=31$ and $p=41$ disprove universal
nonvanishing of $A_s$ and its increment.  Root independently checked the
telescoper in rational polynomial arithmetic, the period formula on every
row through $p\le401$, and the counterexamples.  The much larger scalar
scan is EXACT FINITE ONLY.  A coordinated Frobenius reduction leaves one
half-binomial prefix, whose required arithmetic remains OPEN; no rate is
booked.

## 2026-08-31: Item 252

### Frobenius normalization to one half-binomial prefix

At the actual relation $p=2r+6s+3$, the exponent in Item 251's diagonal is
$(p-1)/2-(r+2)$.  Euler's criterion and an exact finite contiguous descent
therefore reduce $A_s\bmod p$ to one universal prefix
$H_{s-1}=\sum_{j=0}^{s-1}(1/2)_j/(j!2^j)$, plus a completely explicit
fixed-$r$ boundary polynomial.  Pochhammer-rectangle bounds prove that no
denominator reaches $p$.

The summand ratio leads to one scalar Gosper equation.  A pole-chain argument
shows that it has no rational solution in characteristic zero.  In
characteristic $p$, the exceptional translation orbit forces a reduced
denominator of degree at least $(p-1)/2$; any other pole orbit has length
$p$.  Hence uniformly fixed-degree scalar closure is rigorously impossible.

Root independently checked the normal form on all rows through $p\le401$
and audited the pole-order profile.  The theorem is deliberately narrow:
phase-specific, higher-rank, and nonlinear relations remain possible.  The
bounded $p\le601$ census is EXACT FINITE ONLY, so no capacity or exponent is
booked.

## 2026-08-31: Item 253

### Actual-phase integer diagonal and terminal-increment separation

Writing $n=3m+\delta=(p-1)/2$, the remaining prefix is congruent to the
actual-phase diagonal
$K_{\delta,m}=\sum_{k\le m}\binom{3m+\delta}{k}(-1/2)^k$.  After the exact
integer normalization $B_{\delta,m}=2^nK_{\delta,m}-1$, its first difference
has a closed hypergeometric form.  Two exact multiples-of-$p$ identities and
a complete unit audit show that its terminal value is zero precisely when
$p\mid2m^2-m+3$, equivalently $p\mid2r^2+21r+81$.

The prefix is still an incomplete sum.  The rows $p=43$ and $p=127$
separate prefix zeros from terminal-increment zeros in both directions.  The
Cartier generating polynomial and all six Fourier sections are exact, but
the kernel $z^m-z^{m+6}$ proves that value-only sixth-root data leave the
target coefficient undetermined.  Root independently replayed every formula
and verified the corrected normalization
$Q_\delta(m)\equiv(2\delta^2+5\delta+29)/18\pmod p$.  The finite census is
not extrapolated, and no rate is booked.

## 2026-08-31: Item 254

### Mellin/Greene localization, punctured genus-one moments, and a height ceiling

The half-binomial prefix has an exact finite-field Mellin polynomial.  Its
Teichmuller lift splits into a three-point Greene period and an explicit
Jacobi unit.  The actual phase does not make the cutoff character bounded
order.  Residue-class substitutions expose fixed genus-one character factors,
including the $j=0$ curve $Y^2=X^3-1/2$, but leave the field-valued
rational puncture that defines the incomplete prefix.

The exact reduced numerator satisfies
 $H_m=N_m/2^{3m-s_2(m)}$, so all distinct zero primes have total log weight
less than $(3m-s_2(m)+1/2)\log2$.  Its normalized limit is $(\log2)/2$,
not zero, and exceeds the raw ordinary-cell mass.  The theorem therefore
books nothing.  Root independently verified the character, beta, cutoff,
binary-valuation, and exact $p=43,47$ zero formulas.

## 2026-08-31: Items 255--256

### Reciprocal incomplete-beta resonance and the first squared-denominator jet

The prefix zero is exactly one incomplete-beta moment zero.  Complementary
denominators pair the $-2$ moment with its $-1/2$ reciprocal, while the
endpoint-retaining contiguous transfer makes their value system rank one.
The first determinant digit is twice a moving harmonic interval; the exact
row $(p,r,s)=(23,1,3)$ makes it zero and gives determinant valuation two.

At the next digit, reflection necessarily introduces the squared-denominator
jet.  Differentiating the contiguous recurrence gives a triangular transfer,
but adjoining both reciprocal jets produces an exact four-by-four matrix of
rank two, not a new condition on the target moment.  The affine endpoint rows
obey the same dependencies.  Root independently reproduced the mod-$p^2$
reflection and all-rank theorem on 1,153 rows.  These are scoped no-go results
for the reciprocal tower through its first jet; higher jets and independent
periods remain open, and no rate is booked.

## 2026-08-31: Item 257

### Global row geometry and the numerator-height information barrier

The ordinary-$j=2$ family was reindexed by a single global parameter $M$.
This identifies the exact prime interval and proves that the visible residue
conditions are automatic, not density filters.  The reduced numerator of the
half-binomial prefix gives exact individual and aggregate containers, but
their logarithmic ceilings exceed the raw cell mass.  The full Item-251 gate
is affine and is not contained by prefix numerator divisibility.  Root
independently checked the reindex on 20,349 rows and the prefix arithmetic on
301 rows.  The observed zeros are EXACT FINITE ONLY; no rate is booked.

## 2026-08-31: Item 258

### The second reciprocal denominator jet

The second derivative state has exact reflection modulo $p^3$, an
endpoint-retaining triangular transfer, and a closed Hasse curvature.  On
every actual phase row the augmented six-coordinate system has rank exactly
three, with compatible affine endpoints.  Exact rows at $p=89$ and
$p=157$ defeat the simplest universal-unit shortcuts.  Root independently
reproduced 2,440 rank-three rows.  This order adds no target obstruction and
books no rate.

## 2026-08-31: Item 259

### All finite same-parameter jets at once

The unified formal resolvent satisfies exact reciprocal and contiguous
functional equations over a localized ring with $(p,z)$-adic filtration.
Truncating at any finite Hasse order shows that the reciprocal equations still
generate one rank-one relation module.  The formal target coordinate is free
in that module, and the affine endpoint is automatically compatible.  This
proves a no-go theorem for the entire same-parameter denominator-jet tower,
not merely its first few orders.  A separate sub-agent audit and root replay
both passed.  The theorem closes this mechanism but books no rate.

## 2026-08-31: Items 260--261

### Punctured elliptic cohomology in both prime classes

Exact birational transport and Hermite reduction identify the
half-binomial period on $Y^2=X^3-1/2$.  The finite-field sum of an exact
differential has a resonant endpoint term and cannot be silently discarded.
After retaining it, each prime class reduces to a second-kind coordinate and
a logarithmic coordinate whose differential has nonzero puncture residues.
The $p\equiv1\pmod6$ calculation also reduces the full Item-251 period and
rank-aware gate to the same pair.

Since compact/unpunctured de Rham classes have zero residues, the ordinary
elliptic trace does not evaluate the needed logarithmic coordinate.  Exact
prefix-zero witnesses occur at $p=47$ and $p=43,193,241$, so the desired
theorem must be weighted-density rather than all-prime nonvanishing.  Root
independently verified 486 and 488 endpoint identities, the localized normal
forms, the gate identities, and every named witness.  No rate is booked.

## 2026-08-31: Item 262

### Boundary-coefficient arithmetic and a failed capacity admission

The $p\equiv5\pmod6$ cutoff coefficient has an exact minimal order-two
recurrence, an odd-section recurrence, complete $3$-adic unit information,
an exact $2$-adic cancellation formula, linear fixed-ray height, and a
large-prime numerator-gcd restriction.  These are all-index theorems, not
finite extrapolations.

They do not contain the full target.  The $p=47$ prefix zero has nonzero
$K_3$, whereas at $p=59$, $K_3=0$ and the prefix is nonzero.  Exact
localization leaves the Item-251 period affine in $(H_q,h_q)$.  Root's
independent probe reproduced the recurrences, valuations, gcd restrictions,
605 actual rows, and 2,420 localization identities.  Since the fixed-ray
height sums quadratically across moving $\delta$, the positive-linear
capacity admission fails and no rate is booked.

## 2026-08-31: Item 263

### Exact punctured Cartier matrices and failure of endpoint descent

The odd punctured cohomology splits into three residue classes and the two
compact elliptic classes.  Direct Cartier selection gives the complete matrix
in both congruence phases.  Its characteristic polynomial discards the moving
prefix; the extension coefficient that retains the prefix is just the old
quantity $H_q$ or $H_q-h_q$.

The finite sum is not a functional on de Rham cohomology.  For
$p\equiv5\pmod6$, one exact differential has endpoint $-\epsilon$.  For
$p\equiv1\pmod6$, two exact endpoint defects satisfy the all-prime identity
$30d_0+12d_1=\epsilon$.  Consequently neither the order-two class relation
nor scalar trace/determinant data give a new collision equation.  Root's
independent probe reconstructed 77 prime-phase matrices and all 1,153 actual
cutoff rows through $p\le401$, with every bounded count labeled EXACT FINITE
ONLY.  The ordinary scalar-Frobenius shortcut is closed; arithmetic weighted
zero density remains open and no rate is booked.

## 2026-08-31: Item 264

### Global $j=1$ support and a componentwise-height information ceiling

The actual row equations give a bijection with all primes in an interval of
length $M/6$, proving the raw $1/36$-per-$6M$ cell mass.  Fixed-cell
prime intervals are disjoint, while their valuations still overlap the
already booked Cartier content.

The simultaneous full gate yields a square divisor in both fixed integers.
The inherited componentwise Cauchy height nevertheless gives only
$3.16381377\ldots$ per $M$, compared with raw $1/6$.  Bounded-degree
operations estimated solely by that same componentwise bound cannot improve
the ratio, but a separately proved exponential cancellation remains open.
Exact seed and Wronskian counterexamples do not collide in the full gate.
Root replayed 4,631 row bijections and the three witnesses without a collision
scan.  No weighted zero-density theorem follows and no rate is booked.

## 2026-08-31: Item 265

### Beta squarefull normalization and the unresolved high-singleton tail

The fixed-seed beta denominator has been audited at the level needed by the
capacity ledger.  Primewise normalization proves that, after the two
deterministic clearing copies have been removed, the remaining matching
quotient divides the square of the reduced beta denominator.  Any proposed
squarefull gain on the same reservoir must therefore be de-overlapped before
it can be counted.

The powerful-supported part satisfies
$E(q_N)\mid\operatorname{sqfull}(q_N)\mid E(q_N)^2$, so squarefull
little-oh and excess-valuation little-oh are equivalent.  The exact height is
$\log q_N=N\log N+(\log4-1)N+O(\log N)$, which leaves the full saddle
scale.  Averaging controls all levels $p^a\le N$, but a prime power with
$p^a>N$ can occur at a single block index and escape every pairwise-gcd
average.  The singleton envelope isolates this obstruction exactly.

Root independently reproduced the recurrence, reverse-Bessel specialization,
product bounds, transfer/gcd identities, primewise overlap inequalities, and
singleton envelope.  The canonical replay and all twelve manifest entries
match.  The discriminant, block-resultant, average-gcd, and
primitive-support conclusions are retained only as scoped method barriers.
No global squarefull rate follows and no Route-1 capacity is booked.

### Targeted literature triage

A primary-source check was recorded in
sources/route1_targeted_literature_note_items259_265.md.  Incomplete
hypergeometric and Picard-1-motive theories support the endpoint-retaining
mixed-extension formulation; Dwork and large-sieve frameworks identify the
sort of additional Frobenius/monodromy input that would be needed.
Central-binomial and $\lfloor p/6\rfloor$ congruences found in the search
do not remove the actual moving cutoff and affine endpoint.  No cited theorem
currently proves the required horizontal weighted zero density or the beta
high-singleton bound.  No novelty is inferred from this targeted search.

## 2026-08-31: Item 266

### Stable off-ray globalization and a scoped weighted-radical barrier

The two stable prime phases are now exact global interval families, not a
finite pattern.  Summing their disjoint prime intervals gives raw coefficient
$C_{\rm st}=0.239111014698\ldots$ per $M$.  The far subcell
$b\ge M/5$ has the exact rational coefficient
$1139587/9085230=0.125432927950\ldots$ per $M$, which exceeds the
current per-$M$ scoped gap by $0.007635025933\ldots$.  Hence slowly growing
layers are not the only capacity-relevant part of the off-ray branch.

The Item-212 localization gives exact integer eliminants depending on
$(b,r)$, including the retained $p=2399$ witness at $b=900$.  Multiplying
the layer divisors costs $O(M\log M)$, whereas the inherited eliminant-height
sum costs $O(M^2\log M)$.  A mock fixed sequence proves that the phase,
integrality, and those height envelopes alone cannot lower the far ceiling.
Because that mock sequence does not satisfy the actual hypergeometric
relations, the result is only a method barrier.

Root independently verified 3,003 stable rows, all exact interval fractions,
the witness factorization, and the sealed replay.  Item 149 already books the
first rank-one copy; the common $g_0,g_1$ condition can at most supply a
candidate extra first-gate copy and says nothing about the $A_1$ digit or a
third copy.  No actual common-zero lower bound or improved upper bound follows.
Item 266 therefore books zero rate and zero capacity reduction.

## 2026-08-31: Item 267

### Fixed generalized Jacobian, non-torsion third-kind direction, and conjugacy obstruction

Let $U=E\setminus D$ for $E:Y^2=X^3-1/2$ and
$D=E\cap\{X^3=1\}$.  The five-dimensional odd punctured module is the
de Rham realization of the fixed Picard 1-motive
$[L^-\to E]$, with $d_k=[P_k]-[-P_k]$ mapping to $2P_k$.
The old pair $(H_q,h_q)$, its incomplete-beta cutoffs, and the complete
Item-251 affine period are exact fixed-frame Cartier matrix coefficients of
this object.

The unit calculation is exact.  The only principal odd boundary direction is
$d_0+d_1+d_2$, generated by
$d\log((Y-\beta)/(Y+\beta))=3\beta\omega_2$.  The target class
$\omega_1$ has the different residue character
$(1,\zeta^2,\zeta)$.  Transporting $P_0$ gives $P=(2,2)$ on
$y^2=x^3-4$; the nonintegral finite point
$3P=(106/9,1090/27)$ proves by Nagell--Lutz that $P$ is non-torsion.

Nevertheless the abstract $p\equiv5\pmod6$ Cartier module has a
$p$-dependent normal form that omits $H_q,h_q$, while the
$p\equiv1\pmod6$ extension splits off resonance.  Since the finite endpoint
does not descend to de Rham cohomology, this basis change does not erase the
actual fixed-frame period; it only closes scalar and conjugacy shortcuts.
No basis-free elliptic-Wieferich equivalence has been proved.

Root reproduced the canonical JSON byte for byte, matched all ten manifest
entries and dependencies, and ran an independent checker through $p\le509$.
Its 95 phase rows and 1,834 cutoff rows are identity checks, not a zero census.
The moving-vector capacity admission fails, so Item 267 books zero rate and
zero retained-capacity improvement.

## 2026-08-31: Item 268

### Exact cross-$b$ contiguous identity and failure of common-gate propagation

The stable off-ray sequences admit an exact adjacent relation obtained from a
constant-term telescoping certificate.  Its phase interpretation sends
$(b,r)$ to $(b-5,r+3\bmod4)$, and its cross-$j$ realization sends
$(M,j)$ to $(M+(p-1)/2,j+1)$.  Boundary failures lie on
$p=3s+c$, $c=3,4,5$, whose primes divide
$(6M)(6M-1)(6M-2)$.  Thus the identity affects the entire far raw
coefficient $1139587/9085230$ up to zero logarithmic rate.

Under a common gate at $s$, the identity forces one nonzero linear
observation of the adjacent pair.  It does not force both adjacent
coordinates.  The exact $p=2399$ row makes the distinction concrete:
the current pair is zero, while the adjacent pair is $(2105,1694)$ and
lies only on the line $966g_0+128g_1=0$.  The relevant coefficient
resultant is $1564$.

The all-$s$ identity spans the kernel of the declared degree-$\le4$
adjacent ansatz, because its exact $25\times20$ evaluation matrix has rank
$19$.  This is not a theorem about higher degrees or nonlinear relations.
The adjacent line is exactly proportional to a current-layer combination and
has inherited exponential height, so multiplying over moving layers costs
$O(M^2)$ logarithmically.

Root's independent probe reproduced the sequence by coefficient extraction
and recurrence, checked 81 identity rows, recomputed both resultants and the
witness, and audited the phase map through $M\le360$ without scanning for
common zeros.  Item 149 already books the first rank-one copy; Item 268 adds
no independent copy, no $A_1$ digit, no weighted theorem, and no rate.

## 2026-08-31: Item 269

### Fixed universal incidence, exact slope denominators, and large-sieve admission failure

The two actual $j=2$ gates, including their rank-zero branch, are exactly
equivalent to a fixed bilinear incidence for the state
$(1,H_q,h_q)$ and a moving $2\times3$ row matrix.  The incidence itself
has bounded degree, but the row matrix is not supplied by Frobenius of the
fixed Picard 1-motive.  Adjoining it as a coordinate merely restates the
collision.

For both prime phases, the full rational slope $D_\delta$ has a unique
lowest-$3$-adic tail term.  In lowest terms its numerator is a
$3$-adic unit and its denominator exponent is
$L+v_3((2L-1)!!)$, with $L=3\delta$ or $3\delta-2$.  These exponents
strictly increase along the actual odd cutoffs.

This yields an all-parameter algebraic-correspondence no-go.  If a fixed
nonzero $P(T,V)\in\mathbb Q[T,V]$ vanished on an unbounded set of
$(\delta,D_\delta)$, the reduced denominator would divide the fixed leading
coefficient evaluated at $\delta$.  Its logarithmic size would then be
$O(\log\delta)$, contradicting the linear $3$-adic lower bound after the
finite leading-coefficient exceptions are removed.

The fixed Cartier module gives no alternative conjugacy-stable divisor:
normal-form changes erase the framed coefficient, while constant pullback to
the row line has trivial row monodromy.  Root independently rebuilt the slope
arithmetic, incidence, normal forms, and $p=47$ factor-through-row witness.
No new auxiliary sheaf or dynamical orbit is excluded.  The existing
fixed-divisor admission fails, the raw cell stays $2/35$ per $M$, and
Item 269 books zero rate.

## 2026-08-31: Item 270

### Exact all-shift contiguous module and bounded-window no-go

The stable off-ray pair has a complete rank-three
constant-term/twisted-de-Rham shift module.  The state
$X_s=(g_0(s),g_1(s),g_0(s+1))$ is independent over $\mathbb Q(s)$;
two infinity-aware three-layer syzygies together with the Item-268 adjacent
identity give an exact rational transfer.  The transfer determinant and all
reduced chart divisors factor into the declared linear forms.

The common gate has codimension two and leaves $X_s=(0,0,u)$.  Every fixed
forward or defined backward shift window is parameterized by that same
scalar.  Transported relations therefore do not supply a new scalar
condition, and a later common gate would be an accidental extra event rather
than an implication.  The $p=2399$ row realizes $u=2105\ne0$.

Every exceptional factor $a(s+h)+b$ puts the row prime into the fixed-$M$
container $a(2M+1)-ah-b$.  For fixed window radius $L$, all exceptions
have total logarithmic weight $O_L(\log M)$.  Root independently checked
25 adjacent rows, 50 syzygy rows, 25 transfers and determinants, 2,772
container identities, and the witness.  The full far raw coefficient remains
$1139587/9085230$ per $M$, but no weighted common-zero theorem follows.
Item 270 books zero rate.

## 2026-08-31: Item 271

### Auxiliary translation dynamics for the full moving slope

Both actual odd slope phases satisfy a proved degree-seven order-two
recurrence whose coefficients sum to zero.  Consequently
$\Delta_\delta=D_{\delta+2}-D_\delta$ obeys a first-order
hypergeometric update, and adjoining $(\delta,D,\Delta)$ produces an
autonomous rank-three rational skew product.

The proof uses a rational WZ certificate with exact degree-bounded polynomial
identity grids and two exact moving-boundary cancellations.  It is an
all-$\delta$ theorem, not recurrence fitting.  The direct iterate has
reduced degree $4n+3$, while actual rows at primes $167$ and $241$
meet the forward pole divisor modulo $p$.

This is translation-difference dynamics, not arithmetic Frobenius.  It
updates $D_\delta$ but not all entries of the full matrix $R_{r,s}$.
No lisse/crystalline compatible system, uniform conductor, monodromy, or
local-density theorem is obtained.  Root independently reproduced 47
recurrence and orbit rows, both pole witnesses, and all package hashes.
The raw $2/35$-per-$M$ cell and Route-1 booking remain unchanged.

## 2026-08-31: Item 272

### Partial complete-row translation module and exact rank-one class exclusion

For the two actual ordinary-$j=2$ phases, the same-prime row motion is



$$
\delta\mapsto\delta+2,\qquad r\mapsto r+6,\qquad
 s\mapsto s-2.
$$



Direct factorial and Pochhammer cancellation gives exact rational
multipliers for $c=2^{2s}$, $B_s$, $\kappa_r$, and
$\tau_{r,s}$.  Adjoining Item 271's update for
$(D_\delta,\Delta_\delta)$ yields the rank-seven state



$$
(1,c,B_s,\kappa_r,\tau_{r,s},D_\delta,\Delta_\delta).
$$



All new scalar denominators are nonzero mod $p$ on the actual forward
range; the $D$-block retains Item 271's explicit pole divisor and its two
actual witnesses.  The complete two-row matrix is nevertheless not closed,
because it also uses



$$
W=(f_0,f_1,U_0,U_1),
$$



equivalently the six coefficient sequences
$(f_0,f_1,P_0^\flat,P_1^\flat,H_0^\flat,H_1^\flat)$.

The first natural completion is excluded exactly.  For each sequence and
phase, a hypothetical relation



$$
A(n)a_n+B(n)a_{n+1}=0,
 \qquad \deg A,\deg B\le7,
$$



would give a nonzero null vector of a $27\times16$ evaluation matrix.
All twelve matrices instead have rank 16 over both
$\mathbb F_{1000000007}$ and $\mathbb F_{1000000009}$, and every
evaluated denominator is a unit.  The literal Item-250 affine chain also has
dimension growing with $r$, adds six coordinates under the row shift, and
changes its internal parameter.  These are scoped obstructions: higher
degree, higher rank, a direct $U$-module, and creative telescoping remain
OPEN.

Root reran the canonical checker to a byte-identical SHA-256
$462dad0634a98f70ebcdc64d18bb5f3162b030cd4e6d380b4e68cab4a77c710b$,
verified all six package hashes and six frozen dependencies, parsed every
JSON, and checked balanced report delimiters with no control characters.
The bounded coordinate and ratio rows are EXACT FINITE ONLY.  No complete
row, Frobenius, monodromy, or density theorem is obtained.  The capacity
stays $2/35$ per $M$, or $1/105$ per $6M$, and Item 272 books zero.

## 2026-08-31: Item 273

### Fixed $j=1$ rank-two incidence and nonprincipal collision ideal

For



$$
p=4h+6s+3,qquad M=3h+4s+2,
$$



the simultaneous divided gate $Q_0=Q_1=0$ is exactly a rank-two linear
incidence $A(h,s)Y=0$ on



$$
Y=(S_T,S_E),\qquad
 S_n=(f_{n+1},f_n,f_{n-1},f_{n-2})^{\mathsf T}.
$$



The logarithmic coefficients satisfy an exact rank-four recurrence obtained
from



$$
(1-z^4)F'(z)-a(z)F(z)=2z(1-z^2)P_0(z).
$$



Both actual endpoints lie beyond the forcing range.  The transfer corridor
is therefore homogeneous and invertible, with every forward and inverse
pivot a $p$-unit.  Multiplication by $(1-z)^2$ and
$(1+z^2)^2$ under the $h$- and $s$-shifts gives a rational parameter
realization of rank at most eight.

Four parameter-shift determinants were reduced exactly.  Their identities
are certified on a $25\times25$ rational grid only after proving that the
cleared difference has separate degree at most 24.  This degree bound turns
the grid into a polynomial identity proof, not an extrapolation.  The finite
singular list reduces on actual rows to the fixed edges
$h=1,2,3$ and $s=1,2$; every fixed shift window has an explicit
fixed-$M$ container of logarithmic weight $O_L(\log M)$.

The recognition does not principalize the gate.  On the generic rank-two
graph chart, two independent linear forms generate a height-two
nonprincipal ideal in four state variables.  By the principal ideal theorem,
no one nonconstant polynomial has exactly that codimension-two zero set over
the algebraic closure.  The concrete row
$(p,h,s)=(61,10,3)$, with $(Q_0,Q_1)=(46,18)$, also shows why
$Q_0^2+Q_1^2$ acquires extra split lines when $p\equiv1\pmod4$.
This leaves exterior-square, determinantal, finite-field, sheaf, and larger
necessary-divisor approaches OPEN.

Root's independent run reproduced the canonical certificate byte for byte
with SHA-256
$5a37a46d5b454a36eb56d8c44891e09673ae520c446454fa020d57aceb95b834$.
All seven package hashes, five dependencies, five JSON files, 2,500 exact
determinant-grid identities, and report controls/delimiters pass.  The 6,258
rank-two rows through $p\le1000$ are EXACT FINITE ONLY and are not an
all-prime theorem.  Item 149 de-overlap is unchanged, the raw fixed-$j=1$
ceiling remains $1/36$ per $6M$, and Item 273 books zero.

## 2026-08-31: Item 274

### Fixed reverse-Bessel determinants are blind to high singleton depth

The reverse-Bessel differential identity gives the integral scaled-jet
recurrence



$$
Z_{i,j+1}=Z_{i,j}+Z_{i-1,j}-2jZ_{i-1,j-1},
 \qquad Z_{i,0}=q_{N+i}.
$$



All fixed shifts of the beta denominator recurrence are integral polynomial
combinations of $(q_N,q_{N+1})$.  Multilinearity therefore proves that any
fixed-size determinant in a fixed shift/jet window with fixed-degree
rational-polynomial coefficients is



$$
\mathscr D_N=\sum_{k=0}^sC_k(N)q_N^kq_{N+1}^{s-k},
 \qquad C_k\in\mathbb Z[N],\quad
 \deg C_k\le s(d+L+J).
$$



Let $k$ be the first nonzero coefficient polynomial.  Away from its finite
integer-root set, if $a=v_p(q_N)>v_p(C_k(N))$, adjacent coprimality gives



$$
v_p(\mathscr D_N)=ka+v_p(C_k(N)).
$$



Thus $k=0$ is depth-blind up to $O(\log N)$, while $k\ge1$ is simply
the formal $q_N^k$ branch; a nonzero integer value already has logarithmic
height at least $kN\log N+O(N)$.  The exponential Padé Wronskian specializes
to a unit modulo the entire $q_N$, so it proves root simplicity but no bound
on the prime-power depth.  The exact Item-265 overlap quotient remains
divisible by $(q_N/\gcd(q_N,D_m))^k$.

Root independently reran the standard-library checker and obtained the same
SHA-256
$fb4ed044e6d665cd5670226dc77cf2979b0cc9efbf6ed3f0825ad824711b6427$.
All six package hashes, six dependencies, five JSON files, and repaired report
delimiters pass.  The bounded identity rows are EXACT FINITE ONLY.  The result
is a PROVED SCOPED NO-GO for ordinary fixed-length determinant height
arguments; growing-length auxiliaries and the global high-singleton theorem
remain OPEN.  Item 274 books zero rate and zero capacity reduction.

## 2026-08-31: Item 275

### Exterior-square encoding of the full fixed-$j=1$ gate

On the rank-two chart, the Hodge-dual signed row minors give the exact kernel
Plücker vector.  It satisfies the quadratic Plücker relation, and the original
two-row collision becomes the fixed flag incidence



$$
x\wedge K=0.
$$



The four written three-form coordinates have rank two for a nonzero
decomposable $K$.  Projectively the flag variety has codimension two in
$\operatorname{Gr}(2,4)\times\mathbb P^3$, so the construction does not
principalize the gate.

Item-273's exact rank-four transports induce a rank-six exterior-square
module with



$$
\det(\wedge^2U)=(\det U)^3.
$$



At $(h,s)=(1,1)$, the old and pulled-back $h$- and $s$-gate row planes
have stacked determinants $604/1365$ and $-7568/1365$.  Along the actual
fixed-$M$ step $(5,1,p=29)\mapsto(1,4,p=31)$, the corresponding exact
determinant is $-585482135072/1165539375$.  Hence the natural kernel line is
non-horizontal under all three transports.  The last witness is over
$\mathbb Q$ and compares different finite fields, so it is not a density
or individual-collision theorem.  Rank-one and rank-zero gates both collapse
to $K=0$, and $x=0$ is separately retained.

Root independently reproduced the certificate with SHA-256
$fb0f9396900e0acb134181fc8df3518edddf1e955b01ac5ed8b785a037004762$,
verified seven package hashes and three dependencies, parsed six JSON files,
and checked report controls and delimiters.  Item 275 is a PROVED SCOPED
NO-GO for the natural flat Plücker line, not for enlarged sheaves or weighted
incidence.  The raw $1/36$ ceiling and Route-1 booking remain unchanged.

## 2026-08-31: Item 276

### Primitive growing Casoratians transport singleton depth

The two-state transfer rows have primitive minors equal, up to sign and shift,
to gap continuants $P_h(n)$.  The scalar Casoratian satisfies



$$
\mathcal C_h(n)\equiv-P_h(n)q_{n+1}^2\pmod{q_n}.
$$



Adjacent coprimality therefore gives, level by level,



$$
p^s\mid\mathcal C_h(n)
 \Longleftrightarrow p^s\mid P_h(n)
 \Longleftrightarrow p^s\mid q_{n+h}.
$$



The exact inequalities
$(4n+6)^{h-1}\le P_h(n)\le[4(n+h)]^{h-1}$ make residual height $O(n)$
equivalent to $h=O(n/\log n)$.  The universal odd anti-period gap reaches
every divisor of $q_n$, but a high level $p^a>N$ costs at least
$N\log(4N+6)$.  The same divisibility equivalence holds for the Item-265
normalized denominator.

Root reproduced the canonical SHA-256
$545e22b2821e2a073cfa3872439d9598a1619cb128c928b0985c901e33deb8c6$
and verified six package hashes, six dependencies, five JSON files, and all
report delimiters.  Item 276 closes only one primitive growing minor; growing
products, sums, and block auxiliaries remain OPEN.  Booking is zero.

## 2026-08-31: Item 277

### Neighboring collision CRT and zero cluster mass

The exact fixed-$M$ neighbor step sends
$(h,s,p)$ to $(h-4,s+3,p+2)$.  If both rows collide, then
$[p(p+2)]^2\mid\gcd(C_0,C_1)$, which is already the known square radical.
The complete mixed-state CRT module is the product of the two finite-field
kernels.  Its idempotent stacked determinant vanishes modulo $p(p+2)$, even
when the corresponding rational row planes are transverse.

Neighbor edges are twin-prime positions.  The Brun/Selberg upper-bound sieve
gives $O(M/\log^2M)$ edges and $O(M/\log M)=o(M)$ endpoint log weight.
Consequently their perfect exclusion cannot reduce a linear ceiling.

Root reproduced SHA-256
$38554e99b31417a5b26b7fdbe92950793fae9f8bee965962903d98ca67d54532$,
verified seven package hashes and five dependencies, parsed six JSON files,
and audited the $p>5$ twin boundary.  Item 277 closes the neighboring
cross-field transversality shortcut, not isolated collision density.  The raw
$1/36$ ceiling and booking are unchanged.

## 2026-08-31: completion of Item 243

### Exact order-six actual-family closure and all-h gauge

For both residues $h=3n+r$, exact transported defect covectors satisfy an
order-six recurrence over $\mathbb Q(n)$.  Clearing denominators gives
coordinate degree at most 2240, and 2241 consecutive regular exact roots
prove the relation identically.  The forward cofactor has degree at most 1806.
Its Newton expansion has 1804 negative coefficients, three zero coefficients,
no positive coefficients, and a separately certified negative constant term;
hence it is strictly negative for every $n\ge0$.

The 12 defect initials and six independent gauge initials prove
$c_h^*=\mathcal R_hE_h^*$ for every $h\ge1$, $3\nmid h$.  Root's final
and initial-layer replays are byte-identical; 38 package files and six frozen
dependencies pass.  The ambient one-step covector is nonzero, and no
arithmetic density or capacity claim follows.  Booking is zero.

## 2026-08-31: Item 278

### Bounded beta-Casoratian portfolio theorem

For $A=\prod_iP_{h_i}(n)^{w_i}$, total gap budget
$L=\sum_iw_i(h_i-1)$, and $H=\log A$, exact positivity gives



$$
L\log(4n+6)\le H\le L\log(4(n+L+1)).
$$



The truncated valuation equals the weighted sum of return depths after the
Item-265 overlap is removed.  At fixed multiplicity $K$, full depth forces
a short return of level $p^{\lceil s/K\rceil}$.  Balancing canonical
anti-period levels gives the exact minimum gap cost
$(K-r)(p^q-1)+r(p^{q+1}-1)$ for $s=Kq+r$, so linear height yields only
$s\log p=O_K(\log n)$.  Unbounded portfolios and sums remain open.  Root's
byte-identical replay and package audit pass; booking is zero.

## 2026-08-31: Item 279

### Uniform fixed-diameter prime-cluster no-gain theorem

For every fixed anchored pattern $J$, the exact tied phase is
$(h-4j,s+3j,p+2j,M)$.  The CRT state module is the product of its local
kernels, all rank profiles survive, and every natural mixed maximal minor
vanishes over the product ring.  Rational multi-plane transversality therefore
creates no product-prime state divisor.  The only fixed-integer consequence is
the already recorded square radical.

The fixed-tuple Selberg upper-bound sieve gives endpoint weight
$O_{D,t}(M/\log^{t-1}M)=o(M)$ for every fixed cluster size and diameter;
their full non-singleton union is $O_D(M/\log M)=o(M)$.  Root's replay is
byte-identical and all hashes, dependencies, JSON files, and delimiters pass.
Isolated fixed-$j=1$ collision primes remain open.  Booking is zero.

## 2026-08-31: Item 282

### Unbounded product efficiency and the exact sum split

For every normalized target $Q$ and weighted continuant portfolio $A$,
primewise truncation proves



$$
\gcd(Q,A)\mid\prod_h\gcd(Q,P_h(n))^{w_h}.
$$



Dividing logarithms by $\log A$ shows that the portfolio efficiency is at
most its best primitive return efficiency.  This remains exact for the scalar
Casoratian product and for every target inside the Item-265 normalized beta
denominator.  Successive layers from repeated powers form a decreasing
divisibility chain.

With unrestricted multiplicity, certified anti-period depth $s$ has exact
minimum gap cost $s(p-1)$.  Linear height therefore gives only
$O(n/\log n)=o(n)$ certified capacity, uniformly across all odd primes.
Homogeneous sums reduce to residual continuant sums: a unique least valuation
is product-controlled, whereas tied minima define a separate cancellation
factor.  Root reproduced SHA-256
$97a9d02a5a2413d4df77bc0aa70e010ff096a6db7f9a9c61af1e5f542b92f384$
and verified the full package.  High-efficiency actual returns and
prime-independent cancellation sums remain open; booking is zero.

## 2026-08-31: Item 281

### Normalized Fitting recognition and fixed-form no-go

Writing $F_M$ for the squarefree forced Cartier product, the ideal generated
by $C_0/F_M$ and $C_1/F_M$ has positive generator $g_M$.  For every
actual fixed-$j=1$ prime,



$$
p\mid g_M\quad\Longleftrightarrow\quad
 p^2\mid C_0,C_1\quad\Longleftrightarrow\quad
 \text{the full gate collides}.
$$



The generic two-form collision ideal has zero elimination to the parameter
field.  A quadratic anisotropic norm is the exact local scalar minimum, but
Chebotarev shows that every finite fixed homogeneous-form library splits on
infinitely many actual phase primes.  Exact false positives are recorded for
five standard norm discriminants without density extrapolation.

The normalized height coefficient is
$H-\kappa=3.99058003744209\ldots$, while the raw target support is only
$1/6$ per $M$.  Root reproduced SHA-256
$e4717920001236194a8a4127476d3a88c12f5ae04e47dcc413bf9c7eb4c8d4f6$
and verified the full package.  Fixed-form scalarization is closed; the
isolated arithmetic gcd and parameter-dependent scalars remain open.

## 2026-08-31: Item 283

### Exact cancellation quotient for bounded homogeneous beta sums

For the declared fixed-sparsity and homogeneous-degree class, with moving gaps
inside the $O(n/\log n)$ budget, the scalar and primitive residual sums have
the same gcd with every normalized beta target.  If $B$ is the common gcd of
the residual terms, the sum-only factor divides $R/B$.  Consequently



$$
\log\mathcal X_\Sigma\le\log|R/B|=O(n)=o(n\log n).
$$



A unique least $p$-valuation gives no additive factor; tied minima account
for all of it.  If the sum forces $Q$, then only
$Q/\gcd(Q,B)$ is bounded by the residual, leaving the product baseline
explicit.  Root reproduced SHA-256
$ef16bc12b0ff051ae47ef91b614eea9af79782509e852a65b97a514a1e780cbe$
and verified the package.  Nonhomogeneous and unbounded sums remain open;
booking is zero.

## 2026-08-31: Item 284

### Exact parameter-dependent norm and its height barrier

For the complete fixed-$M$ candidate-prime product $B_M$, CRT produces a
least positive residue $d_M<B_M$ which is a nonresidue modulo every
candidate.  The raw norm has candidate-prime valuation exactly two off the
gate and at least four on it; the normalized norm vanishes modulo $p$
exactly on the collision.

The coefficient obeys $\log d_M\le M/6+o(M)$.  If its exponential height is
$\delta M+o(M)$, the inherited raw norm ratio is
$H/2+\delta/4$; even $\delta=0$ remains far above $1/6$.  Thus exact
scalar recognition does not imply a useful weighted bound by absolute height.
Root reproduced SHA-256
$f3ecc6fe0d1335733c9dd4b51f0680c438a766afbb29051c75bec26a6d7a5dee$
and verified the package.  Norm cancellation and moving prime-factor density
remain open; booking is zero.

## 2026-08-31: Item 289

### Exact balancing inside a fixed CRT nonresidue class

For one frozen simultaneous-nonresidue class $d_0\bmod B$, the norm values
form one affine lattice and their exact least absolute representative is the
nearest-lattice distance.  Primitive reduction gives



$$
x^2-(d_0+kB)y^2
 =\gcd(x,y)^2\bigl(X^2-d_0Y^2-kBY^2\bigr),
$$



with the parenthesized factor coprime to $B$ for every $k$.  Hence each
candidate valuation is exactly twice the valuation of $\gcd(x,y)$, and the
ideal generated by all representatives is $\gcd(x,y)^2\mathbf Z$.
Representative balancing and natural products or powers supply no new
exponent gain.

Root reproduced SHA-256
$8c9a9e717b5636615940ac91869c5743ccfe02d45008f0e3a7c42bb80d9b2669$
byte for byte and verified six package files, six dependencies, six JSON
files, all boundary cases, and report formatting.  Distinct CRT classes,
actual phase cancellation, and a useful moving-prime gcd theorem remain open.
The $1/36$-per-$6M$ ceiling is unchanged and booking is zero.

## 2026-08-31: Item 285

### Arbitrary-sum cancellation and exact boundary-unit tracking

For any finite nonzero integer sum $R=\sum_jT_j$, with common baseline
$B=\gcd_j|T_j|$, the additive target quotient



$$
{\gcd(Q,R)\over\gcd(Q,B)}
$$



divides $R/B$.  Hence every construction with explicit normalized
conservative height $\log(\sum_j|T_j|/B)=O(n)$ has only
$O(n)=o(n\log n)$ additive capture, with no bound on sparsity or degree.

For nonhomogeneous beta sums, exact Casoratian reduction gives a polynomial
$F(u)$ in $u=-q_{n+1}^2\bmod Q$.  A small factorization-independent lift
of $u$, or a monic low-height annihilator with nonzero resultant against
$F/B$, would close the additive quotient.  The canonical choices cost the
full $n\log n$ scale, and $\mathcal C_1$-homogenization controls a
different designed sum.  Root reproduced SHA-256
$0af4b01f76b7a51d1bc43b6d9b823e12c9b21d4ad8e3282abaa1fd5e9efde19e$
and verified all six package hashes, ten dependencies, five JSON files, and
the report format.  The low-height boundary-unit relation and Item-282 product
baseline remain open; booking is zero.

## 2026-08-31: completed Item 280

### Gauge-to-endpoint arithmetic localization

Using the completed Item-243 identity, every original actual fixed-$j=1$
collision kills the common lower/upper residual.  A division-free endpoint
elimination then forces both the phase eliminant and the natural endpoint
scalar to vanish modulo the row prime.  After the full unit audit this is



$$
p\mid\gcd\bigl(N_E(h),N_K(h)\bigr).
$$



Root reproduced SHA-256
$f8bd3c2da2ddb6b5de2ca8411e918c2ddf6a1b4dbde57e56aded3a7bdba34987$
and verified all package hashes and dependencies.  Whether the new scalar is
redundant or gives arithmetic codimension remains open; the inherited summed
height is $O(H^2\log H)$, so no weighted saving or booking follows.

## 2026-08-31: Item 286

### Fixed-field Frobenius-sieve applicability audit

The cited Kowalski theorem was checked against the exact isolated
fixed-$j=1$ gate.  The archive currently has a rational
translation-difference module and exact gcd/CRT recognition, but not a fixed
finite-field base, compatible auxiliary-$\ell$ lisse system, uniform
cohomological complexity, monodromy, cross-$\ell$ independence, or a
conjugacy-stable local gate.  Moreover $p$-divisibility of the pair in the
varying characteristic gives no formal condition modulo $\ell\ne p$.

Under a future exact-zero compatible bridge, Kowalski's fixed-field bound
would give a vertical power saving.  The distinct horizontal theorem needed
for the actual tied family has the exact sufficient threshold
$N(M)=o(M/\log M)$.  Root reproduced SHA-256
$012a1dc700a37197e2ccf153a3ea473266a019d23e4905e67ac31ab45b88c169$
and verified the sealed package.  No global horizontal no-go and no capacity
saving are claimed; booking is zero.

## 2026-08-31: Item 287

### Recurrence-universal annihilator kernel

The generic two-state beta recurrence has exact kernel
$(X,U+Y^2)$ after reduction modulo $X$ and substitution
$U=-Y^2$.  Hence an annihilator whose coefficients come only from the
recurrence is necessarily tautological; no positive-degree monic polynomial
in $U$ with polynomial or rational $n$-coefficients works universally.
The proper-target kernel is $(Q,U+Y^2)$, and degree one is exactly the
small-lift problem of Item 285.

Root reproduced SHA-256
$b50df1a58d84179c400ac17b430b143280b824e6a635a1f79391f9750e0eac10$
and verified the sealed package.  Special-seed arithmetic, proper-target
relations, the product baseline, and every positive beta-capacity theorem
remain open; booking is zero.

## 2026-08-31: Item 288

### All-row redundancy of the fixed-$j=1$ endpoint scalar

Exact reflected Gosper telescoping proves
$K_h=c_h(2d_hY_h-L_hX_h)$, with the full second factor localized at
primes at most $4h+3$.  The Item-243 gauge is a unit in the same
localization.  Hence every prime $q>4h+3$ dividing the reduced numerator of
$E_h^*$ also divides the reduced numerator of $K_h$.  Every actual row
prime lies in this range.

Root reproduced SHA-256
$fde756a5dff3b482bb38e342c4d26871dec90c32a7868110ba4f3186ba70b738$
byte for byte and verified the sealed package.  The implication is one-way:
it closes the extra endpoint-codimension mechanism but proves no weighted
control of $E_h^*$.  The retained ceiling is unchanged and booking is zero.

## 2026-08-31: Item 290

### Exact beta least-lift reduction and generic-continuant barrier

The minimum-height monic degree-one annihilator of the full beta boundary
unit has coefficient size $\rho_n$, the centered least residue of
$q_{n-1}^2\bmod q_n$.  Item 290 expresses it both through the exact
descending arithmetic-progression continued fraction and through the
constrained determinant $Ar=bh-ac$.  Palindromic continuant words prove
that coarse positivity, length, and partial-quotient size cannot yield a
growing lower bound.

Root required an explicit separate $n=2$ singleton convention, then
reproduced the repaired certificate SHA-256
$212c43b65b784cab3a245c3e5353510394e9a175f2cf294d0d49330f58d00e1b$
byte for byte and verified the package.  Both an $O(n)$-height lift and a
superlinear exclusion remain open for the actual reverse-Bessel seed; lower
bounds do not transfer to proper targets.  Booking is zero.

## 2026-08-31: Item 291

### Exact ordinary-$j=2$ connection plane

Termwise reversal and matching hypergeometric ratios prove that the lower
$B$-tail is $Y_\nu=2d_\nu$.  Hence
$H_\nu^\flat=-11d_\nu$ and
$D=9c\det(f,b)-11\det(f,d)$.  The actual-row unit audit for $z_1$
turns this into a complete rank theorem: rank is two exactly off $D=0$,
with every lower-rank chart explicit.  The condition remains necessary, not
sufficient, for the actual collision.

Root reproduced SHA-256
$831cd4c74b10555c261eccebef7fd9c5a871bcef97a43d52e77c731b9b7188b5$
byte for byte and verified the package.  The fitted order-three operator is
quarantined as exact finite evidence only.  No weighted bound or booking
follows.

## 2026-08-31: Item 292

### Reverse-Bessel least lift as an inhomogeneous $e$-determinant

The full beta seed and its companion are the two fixed-argument Bessel
specializations $q_n=(-1)^ny_n(-2)$ and $p_n=y_n(2)$.  Their quotient is
the $(3n-2)$-nd regular convergent to $e$, and the alternating Wronskian
turns the least lift into one exact fixed-right-hand-side minimization.  The
resulting $e$-identity retains a moving inhomogeneous center.

Root repaired the nonprimitive-pair step in the homogeneous comparison, then
reproduced SHA-256
$823385a1d313e3e602561d997972c867e623a3128280038c81b18a544a833696$
byte for byte.  Homogeneous irrationality measures alone give only polynomial
scale; inhomogeneous descent, proper targets, and the product baseline remain
open.  Booking is zero.

## 2026-08-31: Item 293

### Integral recurrence and generic-information density barrier for $E_h^*$

The sole surviving fixed-$j=1$ gate satisfies a primitive integral
order-three, step-three recurrence.  Its coefficient signs propagate exact
opposite signs in the two admissible residue classes, and the large-prime
part of its numerator is exactly the corresponding part of one coefficient
of Item 237's fixed algebraic series.  The forward factor $4h+39$ equals
the actual row prime on $s=6$, so no uniform modular forward-unit theorem
comes from the recurrence.

The rational comparison sequence $4h+9$ has every prime value on the actual
$s=1$ family and weighted mass $\sim2H$.  Thus generic algebraicity,
integral holonomy, and exponential height cannot imply the desired horizontal
$o(H)$ bound.  Root reproduced SHA-256
$7af9fd9fe5e6bff2a0402c142479bbca0632c9b5e0f8591a29b41741e1be81f7$
byte for byte and verified the package.  The no-go is strictly scoped;
sequence-specific arithmetic remains open and booking is zero.

## 2026-08-31: Item 294

### Exact half-integer gauge of the connection-minor candidate operator

Six polynomial cross-identities prove that the Item-291 candidate is exactly
the Item-237 coefficient operator on $h=3n+1/2,3n+5/2$ after one explicit
hypergeometric gauge.  This identifies the operator but does not put either
connection minor in its kernel.  The normalized-$M$ coefficient bridge is
still finite-only, and nonzero determinant witnesses exclude only the single
already-certified coefficient line for normalized $L$.  The gauge and
primitive forward coefficient also have explicit actual-row singular layers.

Root reproduced SHA-256
$5a451e4d0b0069e59c4bff84dbaf37e578c654627765f1683a5e0ae4f3977353$
byte for byte and verified all package and dependency hashes.  Sequence
annihilation, Frobenius realization, and weighted density remain open;
booking is zero.

## 2026-08-31: Item 295

### Sharp beta nearest window and exact descent defect

The full-target half-bound failure is equivalent to one nearest-integer
congruence together with the strict window $|H_n-ac/b|<Aa/(2b)$.  The
congruence without that window has the weaker exact threshold
$\rho_n<b/(2A)$.  The determinant-preserving Euclidean descent misses the
previous square-residue slice by $t_n=c-\kappa_n$, where
$t_n=\operatorname{nint}((bc-a^2)/b)$ and the Turan numerators satisfy
$T_n+T_{n-1}=4ac$.  Projection adds $ct_n$ and returns only the known
previous centered residue.

Root reproduced SHA-256
$7a19cdcb2f19bee4bf3a64e28f401b82179f40b02ef4ab8870b8c27f896642a0$
byte for byte and verified all package and dependency hashes.  The theorem
is a scoped obstruction to naive one-dimensional descent, not a proof or
disproof of the half-bound.  Booking is zero.

## 2026-08-31: Item 296

### Exact modular singular-ray atlas for $E_h^*$

The complete linear-factor analysis gives exactly the structural actual rays
$s=2,4,6$, three finite prime rows, and one excluded composite equality.
After actual-row substitution, every nonlinear coefficient core is
equivalent modulo $p$ to one of four irreducible primitive polynomials in
$s$.  On the regular interior, the recurrence transports an invertible
three-state module in the same characteristic.

Root reproduced SHA-256
$909da750976707960c8ba3b01a4e0456d970134bfa32d6e3235472dad4a7a0ab$
byte for byte and verified all package and dependency hashes.  The zero-
hyperplane result concerns unrestricted recurrence states only; the actual
$E_h^*$ orbit and weighted density remain open.  Booking is zero.

## 2026-08-31: Item 297

### Exact boundary renormalization on all structural $j=1$ rays

The rays $s=2,4,6$ are shifts of the same diagonal $p=4H+3$.  The
complete arbitrary-$H$ Pochhammer reduction proves that
$B_H=pE_H^*$ is integral and
$B_H=-3XV/4-9UY\pmod p$.  A factor-by-factor gauge audit proves
integrality of every neighboring recurrence value, including the exceptional
$(H,p)=(4,19)$ row.  Hence the structural coefficient zero is canceled by
the boundary pole rather than lowering the recurrence order.  The complete
fixed-core drop table yields no scalar target constraint.

Root reproduced SHA-256
$aa84dde588a119c67b868266ca536699b3675d2e53cb62ad8f1df66705ca7e6b$
byte for byte and independently checked the repaired all-$H$ algebra,
gauge valuations, overlap, and scope.  The pinned boundary residue and
weighted-density problem remain open.  Booking is zero.

## 2026-08-31: Item 298

### Exact centered beta dynamics and contraction obstruction

The beta Turan pair factors through $w_n=T_n/q_n$, with an exact affine
update and bijective centered two-coordinate form.  The actual forward carry
is $-6$ at $n=6$, remains negative, and tends to $-\infty$.  An exact
primitive-denominator ambient family maps a nearly maximal preceding
centered numerator to current numerator $-1$, while a second construction
rules out row-uniform contraction in every fixed unscaled norm.

Root reproduced SHA-256
$c2c1466482faee7ff6d98ebf2e42097306466841024c94b27988298120b1cb97$
byte for byte and audited the exact inverse, carry proof, primitive collapse,
and scope.  The witnesses are not the actual Turan orbit.  The half-bound,
actual short-branch invariant, proper targets, and product baseline remain
open.  Booking is zero.

## 2026-08-31: Item 300

### Sublinear-depth phase-blind beta-strip no-go

The exact seed-compatible interval $I_n$ has width
$q_{n-1}/((4n-2)(4n-1))$, and the affine image of the preceding interval is
strictly contained in it.  At depth $L$, the transported width is



$$
\frac{q_{n-L}q_{n-L-1}}
 {q_n(4(n-L)-2)(4(n-L)-1)}.
$$



Exact recurrence-product estimates prove that it diverges whenever
$L=o(n)$.  Every sufficiently large surviving strip contains two moving-
grid phases whose current centered numerators are $-1$ and
$-(q_n-1)/2$; inverse affine transport preserves every preceding grid and
strip.

Root reproduced SHA-256
$eda21ac33bb2570f4fbeaea721a0cebf70776bc07185ecf9c990c35dd0cde161$
byte for byte and audited the endpoint, width, divergence, grid, and scope
arguments.  The model witnesses are not the actual Turan seed orbit.  Only
sublinear-depth phase-blind affine-strip proofs are closed; base-reaching
seed arithmetic, proper targets, and the product baseline remain open.
Booking is zero.

## 2026-08-31: Item 301

### Boundary scalar reduction and exact de-overlap

Root-of-unity filters give all-$H$ formulas for $U_H,V_H$, and an
integrated odd filter gives $X_H$.  The structural boundary scalar is
therefore reduced to one explicit residual moment $Y_H$, with separate
even and odd target values.  The moment has an exact Gaussian integral and
first-order recurrence, but no nonvanishing or density theorem.

The actual boundary-neighbor combination is exactly
$L_j(h)=-Q_0(h)E_h^*$.  It duplicates the old gate whenever $Q_0$ is a
unit and is automatic at the complete finite $Q_0$-drop rows.  Root
reproduced SHA-256
$f25813facfe8befb751fdbcd1c5f521c23379162bd44244356c8b2568d9fc784$
byte for byte and audited the filters, moments, parity reductions, and
de-overlap.  The retained $1/36$ ceiling is unchanged.  Booking is zero.

## 2026-08-31: Item 302

### Base-reaching affine elimination is principal

The exact affine beta history from $x_2=6/7$ reconstructs the alternating
Turan formula.  In the integral polynomial ring, the base relation and all
affine updates have endpoint elimination ideal



$$
\mathcal I_n\cap\mathbb Z[X_n]
 =\langle q_nX_n-T_n\rangle.
$$



Thus polynomial elimination supplies no second endpoint relation.  The
continuant matrix gives $r_nS_n^2=1\pmod{q_n}$, and every proper divisor
sees the centered residue as a square unit.  This proves only the zero-rate
bound $|r_{n,Q}|\ge1$.

Root reproduced SHA-256
$1cc2de524522d9720cf475ac5836b6d5148edb285f09cf5759d54e5dde6a37dc$
byte for byte and audited the composition, continuants, ideal contraction,
and scope.  Modular-square/Ostrowski arithmetic, proper targets, and the
product baseline remain open.  Booking is zero.

## 2026-08-31: Item 304

### Universal nonvanishing of the structural boundary residue

The Item-301 Gaussian moment has the exact numerator


$$
N_n=2+(2+i)\sum_{k=1}^n\binom{2k}{k}(1+i)^k.
$$


At $n=2H$ and $p=4H+3$, Wilson's theorem and the central-binomial
congruence turn its truncation into a binomial-theorem/Frobenius evaluation.
The result is



$$
B_H=-24\left(1+(-1)^{\lfloor H/2\rfloor}2^H\right)\ne0\pmod p
$$



for every actual boundary prime.  Euler's criterion supplies the final
nonvanishing.

Root reproduced SHA-256
$df1cff1ceb904984ce37db8e76b31d95696610b019df92849d8646eb510e1274$
byte for byte and independently audited the Gaussian recurrence, Wilson
factor, Frobenius powers, parity formulas, and capacity scope.  The theorem
does not exclude a pinned collision because $B_H$ is not an independent
necessary-zero gate.  The $1/36$ ceiling is unchanged.  Booking is zero.

## 2026-08-31: Item 305

### Exact beta dual-window classification and multiplier no-go

Euler's continuant identity and Legendre's criterion give the exact
classification



$$
R=gQ_k,\qquad \kappa=gD_k,
$$



for every compatible residue below the proposed dual threshold.  The
reduction step fixes only the convergent $P_k/Q_k$; it does not remove the
common multiplier $g$.

Two symbolic infinite counterfamilies prove that this distinction is real.
The family $n=Q_k+2$ admits $R=2Q_k$, which cannot be any prefix
denominator because all such denominators are odd.  The family
$n=(Q_k+3)/2$ has both $Q_k<a/(2c)$ and $D_k<c$, refuting the proposed
tail lower bound.

Root reproduced SHA-256
$10d6989341d0e9c6416fe7a3a26be054ffab39e3df56f82b4e3fa1d42d79bcaf$
byte for byte and audited the classification, symbolic inequalities, and
scope.  The centered half-bound, seed-specific nearest quotient,
modular-square/Ostrowski arithmetic, proper targets, and product baseline
remain open.  Booking is zero.

## 2026-08-31: Item 306

### All-$n$ normalized ordinary-$j=2$ $M$-bridge

The normalized connection minor satisfies



$$
\frac{16^nM_{6n+e}}{g_n}
 =\lambda_e[x^{6n+e}]C(x)
$$



for both $e=1,5$ and every $n\ge0$.  The proof is an exact
twisted-Hermite calculation: all shifts $0,\ldots,3$ in both companions
reduce to a three-dimensional period basis, the beta-regularized exact terms
vanish meromorphically, and all nine plus/minus tensor coordinates cancel
under Item 237's operator.  A positive forward coefficient and three exact
initials on each ray complete the identification.

Root reproduced SHA-256
$cd48ec7f4cec273c72371d554c9a4ec55ed3cacde0108f4dc92975ba93dbbc55$
byte for byte and audited the endpoint, tensor dimension, normalization,
initials, and poles.  The independent $L$ minor and full determinant
weighted density remain open.  Booking is zero.

## 2026-08-31: Item 307

### Fixed-divisor closure of the three singular $j=1$ rays

Frobenius turns each of $s=2,4,6$ into a fixed rational coefficient source.
Exact Gaussian partial fractions give six parity-dependent linear forms in
$w_h=(-1)^{\lfloor h/2\rfloor}2^h$.  Euler's criterion converts a zero of
any form into divisibility by one fixed nonzero integer $D_{s,\epsilon}$.
The structural-ray collision mass is therefore $O(1)$, while the exact
row $(h,s,p)=(8,2,47)$ demonstrates that universal nonvanishing is false.

Root reproduced SHA-256
$7b4850b49b3b1615187936168e6f29ad8cd241aabfb9b7766d618d42a3376613$
byte for byte and audited the Frobenius, gauge-unit, Gaussian, Euler, and
capacity steps.  The fixed-$M$ support of these three rays was already
$O(\log M)$; off-ray weighted density remains open, the $1/36$ ceiling is
unchanged, and booking is zero.

## 2026-08-31: Item 308

### All-$s$ pinned divisors and the height-information no-go

The exact Frobenius source now yields, for every $s\geq1$, an integral
parity residue $a_s+b_{s,\epsilon}w_h$ after the $p$-unit clearing factor
$\Lambda_s=3\cdot2^{10s+10}$.  Euler's criterion gives the necessary
moving divisor



$$
D_{s,\epsilon}=2^{3s+1}a_s^2-
 \delta_{s,\epsilon}b_{s,\epsilon}^2.
$$



The containers are uniform quadratic norms and have logarithmic height
$O(s)$.  A fixed-$M$ comparison construction proves that these
qualitative facts alone cannot lower the $1/36$-per-$6M$ ceiling:
comparison containers of the same type retain mass arbitrarily close to the
complete raw cell.

Root reproduced SHA-256
$4efff9ca2fb1bc11cc6030e260ff73aae89c28bd157bb41fa6bbc3b32e41e5cf$
byte for byte and audited the all-$s$ Frobenius reduction, unit bridge,
Euler sign, norm identity, height estimate, fixed-$M$ comparison, and
scope.  Exact factor localization and $W_D(M)=o(M)$ remain open.  The
$1/36$ ceiling is unchanged and booking is zero.

## 2026-08-31: Item 309

### All-$n$ ordinary-$j=2$ $L$-bridge from the $y=-1$ branch

Tail inversion, a common beta normalization, and exact finite-part endpoint
vanishing turn the actual $L$-minor into a two-cycle determinant in the
same twisted period system as Item 306.  The full exterior-tensor identities
therefore prove recurrence membership, and three original-tail initials on
each ray give



$$
16^nL_{6n+e}/g_n=\mu_ea_{6n+e}
$$



for every $n\geq0$.  The sequence $a_r$ is the coefficient line of the
distinct $y=-1$ branch of Item 237's curve.

Root reproduced SHA-256
$b44200c2e3fe16fca4518e45b40540230db43deee496d84c43336907ef304c5a$
byte for byte and audited the branch, beta, endpoint, tensor, normalization,
initial, and pole arguments.  The full gate is now an exact two-branch
combination, but singular-layer clearing and weighted density remain open.
The $1/105$ ceiling is unchanged and booking is zero.

## 2026-08-31: Item 310

### P-recursive all-$s$ containers and the holonomy-information no-go

Exact generalized-diagonal formulas prove P-recursiveness of the Item 308
coefficient and container sequences.  The norm splitting field is split at
every actual prime class.  A nonzero first-order hypergeometric comparison
of exponential height contains all primes $6s<p\leq Ks$ and retains mass
tending to the raw $M/6$.

Root reproduced SHA-256
$025ac9ae87cbec544877e072dc5c79fad82039d4d85e4d1abe73d0ffadc77d16$
byte for byte.  Generic P-recursiveness, height, nonvanishing, and norm shape
are now closed as a capacity argument; exact operator coefficients, factor
localization, and $W_D(M)=o(M)$ remain open.  Booking is zero.

## 2026-08-31: Item 311 OPEN checkpoint

### Actual-seed beta multiplier divisibility reduction

The companion tail is exactly $(3q_n-p_n)/2$, and the appended-tail
continuant gives a Padé cross-determinant.  Combining this with Item 305
proves



$$
R<a/(2c)
 \iff
 \widehat D_k\mid a\ \hbox{ and }\ \widehat D_k>2cQ_k
$$



for some exact prefix index $k$.  Parity forces any such remainder to be
positive and odd.  A false first-tail/last-tail identity is explicitly
quarantined.

Root reproduced SHA-256
$a4d6aecd652c7f975ebac327840bc178d8a87ffc4e973e9a128f9eb2b4112814$
byte for byte.  The divisibility exclusion, the smaller lower bound, and the
full half-bound remain OPEN; the intermediate interval is untouched.
Booking is zero.

## 2026-08-31: Item 312

### Exact all-$s$ telescoper and singular-pivot localization

An explicit rational Gosper certificate proves an order-three,
degree-seven recurrence for the exact fixed-$j=1$ aggregate $A_s$, with
all removable endpoints audited.  After the fixed-$M$ substitution, every
leading or trailing pivot prime divides one of two nonzero degree-seven
integers, so the pivot-singular mass is $O(\log M)$.

Root reproduced SHA-256
$21373d42a41590895112b4567bd3eae988166db8d84d55db9514be0e59e8f7f9$
byte for byte.  The theorem does not localize collision zeros on regular
rows; bounded recurrence data alone is also closed scoped by an exact
comparison.  The $1/36$ ceiling and booking are unchanged.

## 2026-08-31: Item 313

### All-length 2-adic exclusion of the beta divisor branch

The hypothetical Item-311 divisor branch forces a proper even convergent
and an exact four-continuant identity.  Modulo eight its segment length must
be divisible by four.  A nilpotent all-length transfer congruence then gives
valuations $v_2(L)+1$ and $v_2(L)$ on the two sides, a contradiction.
Therefore



$$
R_{\rm act}\ge q_{n-1}/(2q_{n-2})\qquad(n\ge2).
$$



Root reproduced SHA-256
$ba2e32e504e69681c2c253033d8f44624feca815dda7b51085bf15f067699a9a$
byte for byte.  The centered half-bound and its intermediate window remain
OPEN; booking is zero.

## 2026-08-31: Item 314

### Fully cleared ordinary-$j=2$ two-branch gate

The two all-$n$ connection bridges have the exact universal ratio
$18:11$.  With $a_r$ and $b_r$ denoting the $y=-1$ and $y=0$
branch coefficients,



$$
D_{r,s}=\frac{g_n\kappa_e}{16^n}
          \left(18\,2^{2s}a_r+11b_r\right).
$$



The global denominator clearer $6^{r+3}r!$, the gauge, and the two ray
constants are units at every actual prime.  This proves the equivalence of
the original determinant gate and the cleared coefficient through all six
forward-singular layers.

Root reproduced SHA-256
$77de2dd46726a5a48e9adc4e40f96341d5da6c8db304d79f0ef8eeb7807245b1$
byte for byte and audited the normalization, Lagrange formulas, integer
clearer, past-step unit bound, six-layer distinction, and endpoint norm.
The norm is exactly Item 250's old resultant, so it is not rebooked.
Weighted zero density and actual-period incidence remain OPEN; the
$1/105$ ceiling and booking are unchanged.

## 2026-08-31: Item 315

### Global nonvanishing and arithmetic splitting of the old resultant

The exact recurrence sign pattern and three initials on each arithmetic ray
prove both branch coefficients are negative for all $n$.  Hence Item
314's endpoint resultant $N_{6n+e}$ is strictly negative and has no
characteristic-zero zero row.

The $e=1$ ray is a norm from $\mathbb Q(\sqrt[3]2)$, while the $e=5$
ray factors into one rational linear and one quadratic factor; the actual
prime chooses a component by the cubic character of 2.  Root reproduced
SHA-256
$09fdd67a6535a043bcbd1e2a46c4b14a633b9928a5f1c65618c34fab65cfabb6$
byte for byte.  Both factor types occur, the norm is still Item 250's old
resultant, and fixed-$M$ weighted density remains OPEN.  Booking is zero.

## 2026-08-31: Item 316

### Exact all-digit beta target and fixed-precision no-go

Canonical Ostrowski digits give two signed dual sums $E,U$.  Exact
continuant telescoping proves $-S<E<a-S$, removes the endpoint carry, and
shows that an actual intermediate-window failure is equivalent to



$$
a/(2c)\leq R<a/2,\qquad 0<|E|<c,\qquad
 U=(-1)^n\operatorname{sgn}(E)a.
$$



The nearest quotient is exactly $|E|$.  An explicit infinite family
passes the target modulo every preassigned $2^s$ but misses the integer
equality, closing fixed-precision truncations only.  Root reproduced
SHA-256
$5167e9d160fcecac86791944e41a176d3400f2a6856090de7cf78d55984e7aa4$
byte for byte.  The exact target, half-bound, and capacity remain OPEN.

## 2026-08-31: Item 317

### Gaussian companion and actual-container coupled system

One differential telescoper proves that $A_s$ and
$Z_s=(-2(1+i))^sB_s$ share Item 312's exact order-three operator.  The
actual $D_{s,\epsilon}$ is a period-four quadratic readout of three
common-operator solutions, yielding exact 24- and six-dimensional coupled
systems.

Eight nonzero degree-seven fixed-$M$ integers contain every four-step
pivot-singular prime, hence their mass is $O(\log M)$.  A nonzero regular
abstract state with zero readout proves that pivots and invertibility alone
cannot localize regular zeros; this is not the actual initial state.  Root
reproduced SHA-256
$334165a7e3a40f043aedd3ea2d221786569aa91262481c2347c436cf10890e44$
byte for byte.  The $1/36$ ceiling is unchanged.

## 2026-08-31: Item 318

### One transverse actual-period condition after the old $j=2$ gate

For $g=fZ+9cb-11d$, the three connection minors give



$$
D=9c\ell-11m,\quad E_b=\ell Z+11C,\quad
 E_d=mZ+9cC,\quad 11E_d-9cE_b=-DZ.
$$



On either nondegenerate chart, $D=0$ plus one division-free actual-period
residual is equivalent to the original collision.  There is at most one
new exterior condition, and determinant-only towers are blind on rank-one
data.  All denominators have one global $p$-unit clearing, including the
characteristic-11 chart.  Root reproduced SHA-256
$75e84016af2c7580f1954f795ed080d25083345578558aae49f6df4253891fd7$
byte for byte.  Weighted density and capacity reduction remain OPEN/zero.

## 2026-08-31: Item 319

### Third-minor factorization and period-elimination barrier

The third connection minor factors globally as



$$
C_r=\beta_rK_r,\qquad
 \beta_r=-\frac{3(r+1)!}{2(2r+3)(-r/3)_{r+1}},
$$



with $K_r$ built independently from canonical inhomogeneous and
homogeneous chains.  The removed factor is a $p$-unit on every actual row.
The exact syzygy $\ell E_d-mE_b=CD$ then proves that eliminating the
actual period on either nondegenerate chart returns only the old determinant
ideal $(D)$.  A genuine second condition must therefore retain the actual
period rather than use further coefficient minors.

Root reproduced SHA-256
$c4ce360823dd2d781bebc492e79b65d6ea183a7dada1d4cbee1b1c37334ec194$
byte for byte and independently checked 50 admissible rows through $r=149$.
The fixed-$M$ weighted gcd theorem remains OPEN; booking is zero.

## 2026-08-31: Item 320

### All-prefix beta complement resonance below half-linear depth

The exact Item-316 boundary drives a forced determinant recurrence for every
literal canonical prefix.  A normalized Casoratian gives its continuous
center, and an explicit factorial-growth threshold shows that for every
fixed $\lambda<1/2$, all depths through $\lambda n$ remain strictly
between the two exact-target endpoints.  Consequently target inheritance
cannot close this literal prefix/complement descent class.

Root reproduced SHA-256
$89755de7ea6ee90a4d91195d2aef7685fc9d47231a6937d3b73a5c9b8d4637e8$
byte for byte.  Critical/full depth, redigitization, nonlinear invariants,
the original exact equality, proper targets, and capacity remain OPEN.

## 2026-08-31: Item 321

### Actual fixed-$j=1$ fundamental basis and split-factor no-go

The actual rational/Gaussian solution triple has an exact Casoratian, whose
nonfundamental fixed-$M$ rows have only $O(\log M)$ prime mass.  All eight
period quadrics factor into genuine common-operator solution bases with
$p$-unit changes of basis.  Every actual norm is split modulo $p$, so
there is no Frobenius-forced double zero.

Transported quadratic invariants and regular single-collision operator
elimination are coordinate tautologies.  Root reproduced SHA-256
$c196625c48a6e1f154cbbed29bc938eff53a318f172bb7679ade099aa5da3c35$
byte for byte.  Arithmetic of the actual factor initial values and a
sublinear fixed-$M$ gcd/resultant remain OPEN; booking is zero.

## 2026-08-31: Item 322

### Period-retaining fixed-$M$ transfer and isolated conic target

The actual period state has an exact triangular recurrence, whose primitive
fixed-$M$, same-ray step is
$(r,s,p)\mapsto(r-42,s+15,p+6)$.  The induced exterior-residual transfer
is division-free.  On $\ell_r\ne0$, the collision is exactly
$H_{s-1}=\Theta_{r,s}$, and the prefix is a rationally weighted character
moment on the fixed conic $y^2=x(1-x/2)$.

Its exponent has linear size in $p$, and an exact root-count theorem forces
degree at least $(p-3)/4$ in every reduced pointwise rational rewrite.
Adjacent $p,p+6$ prime pairs have only $o(M)$ logarithmic mass, so even
perfect propagation on those pairs cannot control isolated collision rows.
Root reproduced SHA-256
$5266eab4b8856e4c4e3c78e261f85ff11977e06ff64169f602c474f83f06e5cf$
byte for byte.  Weighted density remains OPEN and booking is zero.

## 2026-09-01: Item 323

### All-depth beta dual transducer

The exact suffix continuants and loads give
$s_j=(RH_j-bN_j)/b$ with $-1<s_j<1$ at every depth.  Under the
Item-316 all-digit boundary, this is the signed deviation
$\sigma E_j-aQ_j/b$.  An all-index division-free comparison excludes
the inherited endpoint for every $j\ge3$, and the $j=1,2$ cells are
closed symbolically.

Root reproduced SHA-256
$680c7e2c3d5dfdeae2b61e37e38a81a363cf3aa25a5229062e3620c727c77bc6$
byte for byte and independently stressed 1,320 all-depth rows through
$n=120$.  Literal target inheritance is now closed at every depth.
The original equality, nonlinear/redigitized descendants, half-bound, and
capacity remain OPEN; booking is zero.

## 2026-09-01: Item 324

### Cross-parity resultant and actual parity-selection audit

The two fixed-$j=1$ parity quadrics have uniform resultant
$64(X^2+Y^2)^2$.  A simultaneous parity zero on even rows forces the
actual rational/Gaussian state to vanish and hence lies in the already thin
Item-321 Casoratian support.  Odd rows have four nonzero geometric
intersection lines.

Across a fixed-$M$ slice, however, $h\bmod2$ is constant and the
actual gate forces only that selected parity.  The unused parity is not a
consequence of the collision.  Root reproduced SHA-256
$e479b217fe07ab9d79d4355b992511febc331fc671e2d64bd9456c9b2e82b28a$
byte for byte.  Cross-parity elimination without a new bridge is closed
scoped; selected-factor weighted density remains OPEN and booking is zero.

## 2026-09-01: Item 325

### Actual fixed-$j=2$ conic involution and rank-two recurrence

The actual conic involution removes the puncture after summation and gives
an exact centered binomial convolution.  The resulting moving-exponent
period obeys an initialized rank-two recurrence.  Full Fourier support,
the minimal orbit-polynomial degree, and a pole-orbit argument close
bounded-support, fixed-degree, and rational rank-one gauge reductions for
the actual family.

Root reproduced SHA-256
$6ff7d4e393a70cd44b143cae227e7a04452c0c5af2ab7a3a287a2074d6275fde$
byte for byte and completed an independent stress audit.  The weighted
zero-density problem remains OPEN; booking is zero and the $1/105$
ceiling is unchanged.

## 2026-09-01: Item 326

### Actual selected fixed-$j=1$ step-12 recurrence no-go

The four actual selected-factor phases satisfy exact order-three
step-12 recurrences, with nonvanishing determinant data on every positive
integer row.  For any fixed bounded row gap, simultaneous actual candidate
primes have weighted mass $O(M/\log M)=o(M)$.  Isolated single rows still
retain linear raw capacity, so the recurrence alone does not prove the
needed density bound.

Root reproduced SHA-256
$9378b4078db1385f60a5128617f6e99c75cd282b6be3e5b0be95410da979450f$
byte for byte.  Bounded-gap cross-row elimination is closed scoped;
single-row arithmetic remains OPEN and booking is zero.

## 2026-09-01: Item 327

### Moving dyadic witnesses and all-degree beta projective collapse

Explicit canonical words show that every moving dyadic precision
$2^s\le2n-3$ can satisfy the positive target congruence without exact
equality; its raw logarithmic mass is only $O(\log n)$.  The exact suffix
identity $L_j-H_jL_m=-bN_j$ also makes every homogeneous residue test of
arbitrary depth and degree projectively equal to the fixed continuant state.

Root reproduced SHA-256
$12fadf2ad2b9703cb369cc7e0859bfdf68425f5267581aa6c4d76d9a7b33012a$
byte for byte.  This closes the declared dyadic and projective information
classes, not divided quotients, higher $b$-adic information, redigitization,
or the original target.  Booking and capacity reduction are zero.

## 2026-09-01: Item 328

### Actual fixed-$j=2$ Cartier digit and Frobenius break

The isolated conic period is exactly the $p$-th coefficient of
$(1-x)^n(1+x)^{n+q}$, and the actual collision becomes one affine
Cartier-digit equation on the nondegenerate chart.  The exact coefficient
recurrence loses this digit at its unique Frobenius pivot; the endpoint that
recovers it is more than $p/3$ steps away with a unit multiplier.

Root reproduced SHA-256
$5b372bd499c433695ab0dd487c78b6426386c500aaf249fe9944431d6e363b46$
byte for byte.  Bounded- and sublinear-depth local recurrence closure is
closed scoped.  Global target arithmetic and weighted zero density remain
OPEN; booking is zero and the $1/105$ ceiling is unchanged.

## 2026-09-01: Item 329

### Actual selected fixed-$j=1$ cubic Cartier carrier

The selected factor is exactly a unit multiple modulo $p$ of one tied
coefficient of $(2-4t+3t^2-t^3)^{4M}$; a dual coefficient represents the
opposite factor and gives the exact full-container zero union.  The carrier
has a fixed rational generating function and recurrence.  A comparison
family proves that degree, sign, integrality, and height alone cannot reduce
the raw cell ceiling.

Root reproduced SHA-256
$4c89f82c9f83dccfb3a32540532e5c986bff1043ec7bfd6f5584500bd7ecc7fc$
byte for byte and checked 113 extra actual rows.  Specific-carrier weighted
zero density remains OPEN; booking is zero and the $1/36$ ceiling is
unchanged.

## 2026-09-01: Item 330

### All-depth divided-quotient resonance and lift termination

Every beta divided-quotient bridge residual equals the old target defect
times a companion continuant.  The full residual ideal is exactly the
principal old-defect ideal, and every adjacent residual gcd divides that
defect.  The same-state normalized lift terminates after one quotient on
target, while the load tower merely re-encodes the original digits.

Root reproduced SHA-256
$331dcf86a9a2c283d92085e8ebec6da91a1f8dd042fa4149db4b580cc53ebcf0$
byte for byte.  Divided-quotient accumulation and same-state higher lifts are
closed scoped; nonlinear arithmetic and redigitization remain OPEN.  Booking
and capacity reduction are zero.

## 2026-09-01: Item 331

### Global Cartier coefficient concentration and fixed-target dichotomy

The actual ordinary-$j=2$ coefficient collapses to the integer sequence
$A_m=\sum_{j\le m}8^{m-j}\binom{2j}{j}$.  Fixed-$m$ sign fibres occupy
explicit residue classes modulo 8 with positive Chebyshev mass, and any fixed
rational target reduces to divisibility of one fixed integer.  The $m=0$
fibres supply full-progressions counterexamples to coefficient-only
nonconcentration.

Root reproduced SHA-256
$08739a4a4061d5b9d78328aa52b6355711657d75259a133660a3181404f640b2$
byte for byte and completed an enlarged stress audit.  The actual moving
affine target after the determinant gate remains OPEN; booking is zero and
the $1/105$ ceiling is unchanged.

## 2026-09-01: Item 332

### Global diagonal and dual collapse of the cubic carriers

The normalized selected cubic coefficient is the old residual diagonal
$b_h$, with the exact identity $c_h^*=2(4h+3)b_h/3$, and its Lagrange
curve is exactly Item 237's old degree-six curve.  The dual $J/L$ carrier
also reduces to the old opposite rank-one factor.  Exponent reduction creates
no new independent period.

Root reproduced SHA-256
$d544609c7ccc08f2ed0c661533939de60d97d2ab75509692925638420f789f68$
byte for byte.  Weighted density for the actual diagonal remains OPEN;
booking is zero and the $1/36$ ceiling is unchanged.

## 2026-09-01: Item 333

### All-degree, all-depth, all-modulus nonlinear-state saturation

The beta target defect is an integral polynomial coordinate.  Its ideal is
prime, radical, and integer-saturated, and formal specialization modulo every
composite modulus has kernel exactly the modulus plus the old defect.  Hence
recurrence-only nonlinear determinants, resultants, and formal valuation
lifts add no target codimension at any degree or depth.

Root reproduced SHA-256
$933120c05e0f67663608e9e53354407f4593718c149941942d070f4af3c0a76a$
byte for byte.  Canonical cofactor arithmetic and redigitization remain OPEN;
booking and beta capacity reduction are zero.

## 2026-09-01: Item 334

### Chart-free target-coupled Cartier carrier

The actual moving target is retained in two exact coordinate residuals.
Taking the primitive gcd of their numerators with the old determinant
produces a rowwise integer carrier whose tied-prime support is exactly the
original collision support on every chart.  This converts the live branch
into a precise fixed-$M$ average-gcd theorem.

Root reproduced SHA-256
$238046186f90bdffb2e9b4c72994bac4f0c2ba7e377b42f04753b5502ea861e2$
byte for byte and completed an enlarged stress audit.  The present pointwise
and aggregate height bounds are too large; the required $o(M)$ squarefree
mass remains OPEN.  Booking is zero and the $1/105$ ceiling is unchanged.

## 2026-09-01: Items 335--339

### Global beta cofactors and exact fixed-cell bottlenecks

Item 335 proves a global zero-rate theorem for the first canonical beta
cofactor and every fixed-complexity boundary portfolio.  Item 337 proves that
this conclusion cannot be extended to the whole growing tower: the exact
de-overlapped object is an LCM, and an explicit canonical intermediate-window
family has positive linear beta-scale LCM height.  The actual target-specific
gcd with this LCM remains open, so booking is zero.

Item 336 reduces the ordinary-(j=2) raw rows to an exact prime interval and
proves that affine resultants and qualitative carrier metadata alone cannot
lower its mass.  Item 338 proves the full two-state base-prime carry formula,
its tied-prime diagonal collapse, and safe removal of denominator and
central-binomial foreign support.  The remaining (j=2) input is a weighted
joint moving-target theorem.

Item 339 gives the fixed-(j=1) selected factor an integral positive-prefix
model.  Lucas forcing is completely classified and has only zero-rate support;
outside it, unit terms can cancel and the natural recurrence rank is linear.
Global moving-prime nonconcentration remains open.

Root reproduced every canonical certificate byte for byte and kept all finite
controls under EXACT FINITE ONLY.  Neither retained ceiling, the booked rate,
nor the Route-1 deficit changes.

## 2026-09-01: Items 340--341

### Full beta complement resonance and ordinary-(j=2) affine normal form

Item 340 proves that the full canonical complement-inverse construction is a
resonant copy of the original beta target.  On target, the returned residue,
digit word, cofactor sequence, and de-overlapped LCM are identical.  Its loop
defect is zero rate, and its congruence modulo each (Q) dividing the base
recovers only the old square ray.  The first possible transverse datum is the
quotient modulo (bQ); the resulting complement-covered and valuation-excess
parts of (Gamma_Q) remain OPEN.

Item 341 proves exact centered coordinates for the safely saturated
ordinary-(j=2) carrier.  They generate the full localized collision ideal, so
connection-only resultants or Groebner elimination cannot create another
condition.  Degenerate collisions localize to an explicit triple-minor
carrier, while the actual state is Zariski dense over characteristic zero,
including along an actual prime subsequence.  Moving finite-field correlation
and weighted support remain OPEN.

Root reproduced both certificates byte for byte, repaired three missing
display delimiters in the Item-341 draft before canonicalization, and retained
all finite controls as EXACT FINITE ONLY.  Both items book zero and change no
capacity ceiling, booked rate, or deficit.

## 2026-09-01: Items 342--345 and 347

### Finite-field lifts, exact beta de-overlap, and conductor barriers

Item 342 constructs an exact all-row Fourier/Kummer representation of the
fixed-(j=1) selected factor.  Its complex square-root bound lives in a
cyclotomic field of growing degree and controls all conjugates, not
divisibility at the selected prime.  Item 345 proves that ordinary Galois
descent cannot repair this formally: traces are not gate-forced, while every
relative norm ends in the same absolute norm with the same height.  Chosen-
prime (p)-adic nonconcentration remains open.

Item 343 proves the exact beta identity (K_Q=R_Q^perp J_Q), with (J_Q)
dividing (Q/rad(Q)).  Thus the only new squarefree question is the weighted
(t)-avoiding hit mass (Xi_Q); all repeated valuations are in the existing
squarefull branch.  Every quotient lift modulo (bQ^s) is exactly one further
residue of the same scalar (t), so repeated precision adds no independent
condition.

Items 344 and 347 settle the natural finite-field completion of the actual
ordinary-(j=2) prefix.  The quadratic Frobenius carrier returns the same
moving coefficient.  Completing all modes gives one legitimate
target-retaining Jacobi correlation, but the cutoff has maximal reduced
degree and the exact semisimple Kummer realization has rank at least (m+1).
Every positive-rate fixed-(M) bulk therefore has linear conductor.

Root independently replayed every certificate, repaired two LaTeX-only
defects in the Item-347 draft before canonicalization, and kept all control
rows under EXACT FINITE ONLY.  No item changes a retained ceiling, books
mass, or changes the Route-1 deficit.

## 2026-09-01: decision-phase synthesis through Item 383

### Global management result

The archive was moved from item-count progress to the capacity admission
rule requested in `word.txt`: only a proved rate increase, a strict reduction
of a material live ceiling, or closure of such a branch counts as strategic
progress.  `ROUTE1_MASTER_CAPACITY.md` now contains the updated theorem
registry, overlap rules, live-branch table, smallest missing theorem for each
branch, and the formal Route-1 decision rule.

### Beta branch

Items 346, 350, 354, 358, 362, 365, 367, 370, 373, 375, 378, and 381 turn
first-hit, incidence, singleton, content, and low-degree symmetric mechanisms
into exact theorems.  Positive singleton mass puts every fixed top-symmetric
coordinate on the same beta scale.  Nonconstant bounded-degree one-variable
residuals, coefficient content, reciprocal-one-sign forms, definite binary
and ternary quadratics, and the normalized Newton boundary are beta-scale.
General mixed-sign cancellation is not closed: the first surviving objects
are actual split-line correlations, primitive gcd/Pell norms, and indefinite
ternary conic isotropy.  The ambient conic examples are not actual carriers.

### Fixed-(j=1) branch

Items 348, 351, 353, 356--357, 360, 363--364, 366, 368--369, 371--372,
374, 376--377, 379--380, and 382--383 separate the true joint gate from its
many presentations.  The Hasse value and transverse period are independent
target coordinates, but determinant, cyclic-companion, filtered-module, and
horizontal-connection packaging creates no third condition.  Exact-zero
boundary strata are empty, primitive gcd reduction occurs below the selector,
and same-ray operator windows fail to align two actual fixed-(M) rows.

Item 383 also corrects the scope of Item 380.  The standard coordinatewise
lift produces a lacunary nonrational connection, but another integral
overconvergent lift produces the rational logarithmic form
$dq/(1-\lambda q)$.  Rationality is therefore not invariant.  The proved
invariant is the absence of a bounded simultaneous splitting, a filtered
splitting, or a dagger horizontal connection on the full moment disc.  No
prime-independent actual-family descent or weighted joint-zero theorem is
obtained.

### Ordinary-(j=2) branch

Items 349, 352, 355, 359, and 361 refine the degenerate and nondegenerate
charts, moment transfer, rational kernel, and matched Cartier reduction.
Every construction remains a description of the same (1/105) cell.  The live
closer is still the aggregate moving-modulus primitive-carrier/average-gcd
bound across both charts.

### Root audit and literature

Root independently replayed and audited Items 346--383, preserving all scans,
operator fits, holdouts, and ambient examples as EXACT FINITE ONLY.  The
Item-382 draft was narrowed so divisibility of the shift index by four means
an integral parameter return; actuality also requires the shifted (s) to
remain positive.  The Item-383 draft received one TeX-only exponent repair.
No audit delegated a booking decision.

The primary-source checkpoint in
`sources/route1_filtered_hasse_literature_note_20260901.md` records adjacent
Fontaine--Laffaille, prismatic, Dwork, and 1-motivic frameworks.  None, as
stated, supplies the missing moving-characteristic weighted zero-density
theorem for this actual family.

No result in this phase changes $r_1$, the deficit, the (1/36) or (1/105)
ceiling, or beta capacity.  Present upper bounds remain nonexhaustive, so
Route 1 stays ACTIVE and Route 2 stays QUEUED.

### Repository-wide integrity checkpoint

Root validated every non-master SHA-256 ledger after canonicalization: 361
ledgers, 2,165 payload entries, and zero remaining failures.  Ten legacy
ledger-only defects were repaired (one mistyped digest and nine stale path
prefixes); no mathematical payload was altered.  All 1,825 substantive JSON
files parse after lifting Python's integer-digit safety limit for the three
intentional giant-integer certificates, all 561 substantive Python scripts
compile, and all 624 Markdown files are free of forbidden control characters.
The controlling documents and Items 371--383 also pass delimiter checks that
distinguish display delimiters from TeX row-spacing commands.

## 2026-09-01 — audited Items 384--390 and first actual fresh-component ceiling

Root directed three parallel research tracks and remained the sole auditor.
Items 384--390 were independently replayed, repaired where necessary, and
promoted with canonical manifests, root audits, and eight-entry SHA-256
ledgers.

The fixed-cell and beta results are structural closers.  Item 384 proves a
nonzero shifted-CRT full-capacity comparison theorem for the entire rowwise
filtered-Hasse information class.  Item 385 proves that every fixed bounded
fixed-$j=2$ propagation window has zero-rate prime-pair support and leaves
the full isolated $1/105$ ceiling.  Item 386 proves that the surviving
low-degree beta varieties are not target-forced, including an exact empty
coordinate-gcd overlap.  Items 387 and 389 identify the unrestricted mixed
kernel quotient with the ordinary integer-linear-form lattice and prove its
all-degree analytic/coefficient-cost and continued-fraction threshold.
Item 388 proves that finite local digits and triple/forest matching data are
not an exhaustive mixed-cubic ceiling.

Item 390 is the material scoped gain.  For every nonzero actual row and every
$p>6m$, it proves



$$
v_p(c_m)=\min\{v_p(2^{2m}L_0),v_p(2^{2m+2}L_1)\},
$$



including all multiplicities.  An exact rational Sturm certificate at
$r=541/1000$, independently cross-checked by root, gives



$$
c_{m,>6m}<21\,136^m,
\qquad
\limsup{\log c_{m,>6m}\over6m}\le{\log136\over6}
=0.8187758142893420014\ldots .
$$



Root corrected the certificate's sign for the displayed component decrease
and restricted the uniform carrier bound to nonzero rows, which the frozen
saddle theorem supplies for all sufficiently large $m$.  No total ceiling
reduction was credited: the residual small-prime factor remains uncontrolled,
and an upper bound on the disjoint large-prime factor cannot be subtracted.

The booked rate and deficit therefore remain
$0.1365141682948128184504238226\ldots$ and
$1.0196329836694317938803064012\ldots$.  Route 1 remains ACTIVE; Route 2
remains QUEUED.

## 2026-09-01 — independently audited Items 391--400

Root kept three research branches active in parallel and remained the sole
auditor.  Ten packages were replayed, corrected where needed, promoted to
canonical `sources/`, `scripts/`, `results/`, and `manifests/`, and sealed
with eight-entry SHA-256 inventories.

Items 391, 395, 398, and 400 settle the generic fixed-$j=1$ density
program through the capacity-relevant logarithmic scale.  Sublogarithmic
clusters have zero rate.  The exact logarithmic cluster radical, its graph
valuations, and its admission coefficient are now explicit.  Aggregate
endpoint resultants are nearly perfect powers, but subtraction preserves all
candidate valuations.  Discriminants and derivative/Vandermonde carriers
are actually coprime to the target support, multiplicative energy is
gap-blind, and the full ambient prime set saturates the exact threshold.
Only gate-specific or cross-$M$ arithmetic survives.

Items 392, 394, 397, and 399 settle the natural fixed-$j=2$ aggregation
and overlap attempts.  Sublogarithmic propagation is zero rate; safe modulus
matching produces exactly the collision product; surviving factors are
atomic and have no reusable high-prime overlap; and phase-only reciprocity is
locally soluble on both rays.  The live nondegenerate object is the exact
selected-prime cyclotomic ideal retaining the ordered prefix.  Ordinary norm
descent permutes that prefix and has noncompetitive height.  A ray saving
must also control the degenerate chart.

Items 393 and 396 refine the mixed-cubic decision.  The small-prime
primitive remainder has a safe component ceiling below
$1.859148991866686$ and an exact layer cake; a successful forced-support
proof first becomes capacity-admissible at raw depth five.  On the fresh
side, the excluded fixed-gap corridor now grows logarithmically, but every
ordinary exponential fixed-gap height method has zero capacity.  The exact
primitive two-cubic carrier is sufficient for $q\equiv5\pmod6$; the
remaining uniform Smith-support/power-of-two problem is explicit.  Item
148's determinant nonvanishing was treated as inherited and was not booked
again.

The rigorous ledger is unchanged:



$$
r_1=0.1365141682948128184504238226\ldots,
\qquad
T-r_1=1.0196329836694317938803064012\ldots .
$$



Route 1 remains ACTIVE and Route 2 remains QUEUED.  Three new work-only
branches were launched: fixed-$j=1$ gate-specific cross-$M$ arithmetic,
fixed-$j=2$ both-chart ray nonconcentration, and the mixed-cubic uniform
Smith-support target.

Before this research cycle resumed, a private snapshot was verified. Its filesystem location and operational backup metadata are omitted from this public release.

## 2026-09-01 — independently audited Items 401--403

Root remained the sole auditor while three research branches ran in
parallel.  Items 401--403 were independently replayed, scope-checked,
promoted to the canonical directories, and sealed with root audits and
eight-entry SHA-256 inventories.

Item 401 proves an actual cross-$M$ theorem for fixed $j=1$.  Each prime
occurs in exactly $\lfloor p/12\rfloor$ consecutive tied rows, and both
original divided transverse coordinates are generated by one fixed rational
map.  Their generating functions are algebraic of degree at most $495$,
so they admit absolute polynomial recurrences within a fixed
characteristic.  The sharp negative conclusion is information-class scoped:
homogeneous recurrence operators leave prime columns CRT-independent and
admit a full-support zero-output orbit, which saturates the $M/12$
admission threshold.  Actual initial-state arithmetic and cross-prime
relations remain open.

Item 402 proves that the ordered incomplete cutoff has trivial
multiplicative stabilizer.  Therefore no proper formal Kummer-mode descent
preserves its support, and no complete unmarked Galois-invariant packet can
recover selected-coordinate vanishing.  Root narrowed the draft so that the
full-field statement applies to the formal mode-labelled support, not
automatically to a numerical specialization with possible extra identities.
Trace, norm, characteristic-polynomial, slope, and unmarked unit-root
compression are closed as sufficient mechanisms; the marked residual and
the degenerate chart remain open.

Item 403 proves the exact Smith invariants of the actual mixed-cubic
coefficient matrix



$$
d_1=d_2=H_q,
\qquad
d_3=H_qG_q^{\rm prim}
$$



away from $6$.  The resulting cubic support is unmarked: Items 411--412
later show that it is a three-branch union for $q\equiv1\pmod6$, whereas
the actual common-log collision selects one Frobenius branch.  Root added
dependency pinning and strict replay, and
restricted the ambient perturbation language to normalized $3$-adic data
that is continuous at the actual point.  The perturbations are not actual
rows; they show only that finite local matrix data cannot prove the global
unmarked support identity.  Divisibility by $H_qG_q^{\rm prim}$ is a
stronger sufficient exclusion in the split phase, not the exact marked
target there.

No positive linear mass was added and no complete ceiling was reduced.  The
booked rate and deficit remain
$0.1365141682948128184504238226\ldots$ and
$1.0196329836694317938803064012\ldots$.  Route 1 remains ACTIVE and
Route 2 remains QUEUED.  Three next-stage branches are active on the actual
fixed-$j=1$ initial orbit, the ordinary-$j=2$ degenerate chart, and the
actual mixed-cubic support identity.

## 2026-09-01 — independently audited Item 404

Item 404 couples the Item-349 triple-minor carrier to the two surviving
Item-334 target coordinates.  The exact degenerate collision carrier is



$$
\Gamma_{r,s}
=\gcd\!\left(\Pi_r,
|\operatorname{num}T_0|,
|\operatorname{num}T_1|\right),
$$



and tied-prime-safe saturation preserves its support while keeping
$\Gamma^{\rm sat}\mid\Pi^{\rm sat}$.  This turns the degenerate chart
from a necessary gate into an exact target-retaining carrier.

The strategic result is the exact rejected-mass identity.  A rare
degenerate chart does not save capacity because the nondegenerate chart may
fill the ray; likewise, few degenerate collisions do not save capacity
without a positive lower bound on degenerate occupancy.  The bookable term
is the mass with $p\mid\Pi^{\rm sat}$ but
$p\nmid\Gamma^{\rm sat}$.  Combined chart upper bounds must total
strictly below $1/35$ per ray before any fixed saving is credited.

The minor-information and pointwise-height obstruction uses only ambient
rank-one and integer packets and is not asserted for the actual sequences.
No positive rejected mass is proved, so the $1/105$ ceiling and the frozen
ledger remain unchanged.  A follow-on Builder/Closer branch is attacking the
actual moving-divisor/rejection-density theorem.

## 2026-09-01 — independently audited Item 405

Item 405 computes the actual first three levels of every fixed-prime
fixed-$j=1$ column.  The Hasse indices are $(1,4,7)$ or $(2,5,8)$.
Complete numerator factorization reduces every possible selected-Hasse zero
to seven phase-compatible rows, and the exact transverse value $Q_0$ is
nonzero on all seven.  Hence the actual joint gate is absent throughout the
complete depth-three initial strip.

The capacity audit is decisive but negative.  At fixed $M$, at most two
primes lie in that strip, so its total saving is only $O(\log M)$.  Any
fixed-depth strip is zero-rate.  A degree-three interpolation model matches
all exact initial coordinate values and obeys one common order-four
homogeneous recurrence while its later selector still saturates the
$M/12$ logarithmic-cluster threshold.  The model is not the actual Item-401
operator or orbit.

Root replaced stale work-package dependencies by the final audited Item-401
artifacts before sealing Item 405.  No rate or ceiling changed.  The next
fixed-$j=1$ branch is restricted to growing-depth actual-orbit arithmetic,
the explicit operator, cross-prime reciprocity, or a subthreshold common
carrier.

## 2026-09-01 — independently audited Item 407

Item 407 seals the exact one-ray ordinary-$j=2$ accounting.  The integer
$\mathcal J=(\Pi^{\rm sat})_{(\Gamma^{\rm sat})}$ carries precisely the
degenerate gate hits rejected by the actual target.  Coupling this chart to
the selected-prime nondegenerate chart gives the sharp normalized saving



$$
{1\over6}\max\!\left\{0,d-g,{1\over35}-g-n\right\}
$$



from future actual weighted constants $d,g,n$.  A complete linear-program
audit and explicit abstract extremizers show that nothing stronger follows
from those aggregate inputs alone.

Root replaced the draft's stale Item-404 work dependencies with audited
canonical dependencies and sealed byte-identical certificate and root
replays.  No positive-margin weighted theorem is supplied, so the result
books zero and leaves the $1/105$ ordinary-$j=2$ ceiling unchanged.

## 2026-09-01 — independently audited Item 406

Item 406 converts the actual mixed-cubic coefficient content into four
adjacent diagonals by two exact determinant-$6$ Hermite transformations.
It then uses Frobenius truncation and a Cayley residue change to show that a
compatible prime divides $H_q$ exactly when the last two relevant
coefficients of both explicit kernels $R_m$ and $S_m$ vanish.

Root independently simplified the two rational identities symbolically,
added the complete audited Item-403 dependency pins, and sealed strict
certificate and root replays.  The simultaneous four-adjacent nonvanishing
lemma and primitive-$G$ support remain open.  No booking or unconditional
capacity reduction follows.

## 2026-09-01 — independently audited Item 408

Item 408 extends the fixed-depth Item-405 audit to every growing contiguous
initial strip.  Exact column geometry locates the first $B$ levels in an
upper prime interval of width $3B/2$.  Ordinary PNT at the two linear
endpoints proves that every $B=o(M)$ deletes only $o(M)$ mass.  The
shortened-interval packing calculation gives



$$
a_b(c)=\max\!\left(0,{1\over6}-{3b\over2}\right)
 \left(1-{1\over2c}\right).
$$



Thus the first capacity-relevant contiguous depth is linear, not
$M/\log M$.  The selector is explicitly an information-class witness and
not the actual later orbit.  Root replaced stale Item-405 work pins with its
audited canonical package.  The result books zero and leaves the $1/36$
ceiling unchanged.

## 2026-09-01 — independently audited Items 409 and 413

Item 409 replaces the ordinary-$j=2$ degenerate target residuals by an
exact tied-characteristic incomplete-period carrier.  It also supplies the
pinned actual-formula row $(p,r,s)=(709,347,2)$, on which the carrier has
the foreign factor $79$.  This is a witness to foreign contamination, not
a prime census or a density theorem.

Item 413 projects the rejection carrier back onto its tied prime:



$$
j^{\rm tie}_{r,s}=\gcd(p,\mathcal J_{r,s})\in\{1,p\},
\qquad
J_e=A_e-B_e=D_e-G_e.
$$



The exact one-ray conditional saving is
$\max(0,a-b,1/35-g-n)/6$.  No positive tail-minus-foreign margin or
combined-chart saving was proved.  Both packages were replayed against
canonical dependencies and sealed with root audits; the ordinary-$j=2$
ceiling remains $1/105$.

## 2026-09-01 — independently audited Items 410 and 414

Item 410 collapses the compatible mixed-cubic scalar carriers to explicit
integers $W_m,J_{m,0},J_{m,2}$.  Item 414 then proves uniformly that



$$
Q_m=\prod_{4m<\ell<6m}\ell
$$



divides all three.  The product has logarithmic mass $2m+o(m)$ and is
exactly inherited Item-200 Cartier content transported into the new
carriers.  It cannot be booked again.  This also disproves Item 410's
proposed full-radical zero-rate target: the meaningful object is the radical
above $6m$.  The stripped height constant is still noncompetitive, so the
capacity delta is zero.

## 2026-09-01 — independently audited Items 411 and 412

Item 411 identifies the exact primitive unmarked Smith carrier and the exact
actual marked branch.  For $q\equiv5\pmod6$, cubing is bijective and the
two conditions coincide.  For $q\equiv1\pmod6$, the Smith carrier is the
union of three cube-root twists but the actual collision selects the root



$$
X_p=4^{(q-1)/3}2^{(p-1)/3}\pmod p.
$$



Item 412 interprets this as a cubic Frobenius mark and proves that symmetric
Smith/radical data or any fixed proper rational factor cannot select it
uniformly.  The no-go is restricted to those symmetric information classes;
no false branch was exhibited in the actual coefficient family.  No
weighted selected-branch theorem or booking follows.

## 2026-09-01 — independently audited Item 415

Item 415 combines canonical Item 200's full compulsory divisor
$F_m\mid\lambda_{0,m},\lambda_{1,m}$ with Item 390's exact all-depth
large-prime carrier.  With



$$
\mathfrak C_F=-4\log2+{\pi\over\sqrt3}+3\log3,
\qquad
\log F_m=\mathfrak C_Fm+o(m),
$$



division by $F_m$ preserves every valuation at $p>6m$ and proves



$$
\limsup {\log c_m^>\over6m}
\le {\log136-\mathfrak C_F\over6}
=0.4292678962895477202317242499\ldots .
$$



This improves the former strictly-large component ceiling by
$\mathfrak C_F/6=0.3895079179997942811851475804\ldots$.  The divisor and
its mass are inherited and not rebooked; the new result is the normalized
Item-200-plus-Item-390 synthesis.  It is a component ceiling only and cannot
be subtracted from the nonexhaustive whole-content ledger.

## 2026-09-01 — independently audited Item 416

Item 416 proves adaptive selected-prime-safe saturation for the
ordinary-$j=2$ rejection carrier.  Moving the cutoff from $2r+3$ to
$p$, or farther, removes exactly the same pure-foreign radical from the
tail and foreign-tail terms, so their difference is invariant.  In
particular, every contaminant $2r+3<q<p$ is removed for free.

For the remaining $q>p$ support, aligned factors map injectively to future
same-$r$ degenerate-gate rows, while transverse factors have no same-$r$
ordinary row.  The transport reaches only gate status; the target residual
changes with the second parameter.  The inherited height gives only
$O(M^2)$ foreign radical weight and $O(M^2/\log M)$ factor incidence,
both sharp in the explicitly abstract height/support information class and
both noncompetitive.

Root replaced the draft's stale Item-413 work pins with the complete audited
canonical package, regenerated byte-identical certificate and root replays,
and sealed an eight-entry inventory.  No rate changed.  The authoritative
ledger remains



$$
r_1=0.1365141682948128184504238226\ldots,
\qquad
T-r_1=1.0196329836694317938803064012\ldots .
$$



Route 1 remains ACTIVE and Route 2 remains QUEUED.  Root continues as lead
researcher and sole auditor while three Builder/Closer branches attack
further compulsory multiplicity, the normalized strictly-large carrier,
and the transverse $j=2$ foreign tail.

## 2026-09-01 — independently audited Item 418

Item 418 optimizes the exact common centered-circle Cauchy kernel of the two
fully Cartier-normalized Item-390 coordinates.  Angular maximization and an
exact radial sign identity reduce the minimizer to the unique positive root
of $9x^3+3x^2+12x-4$.  The resulting exponential base is



$$
\rho_*=135.5974839008548212502259703306\ldots,
$$



the unique real root of
$262144t^3-35555328t^2+1259712t-531441$.  Exact prefactor bounds then give
$|\lambda_{0,m}|<3\rho_*^m$ and
$|\lambda_{1,m}|<21\rho_*^m$.

After the inherited Item-200 divisor is removed, the strict-large component
ceiling becomes



$$
{\log\rho_*-\mathfrak C_F\over6}
=0.4287738853386578689457603829\ldots,
$$



a further decrease of
$0.0004940109508898512859638670\ldots$.  Root independently checked the
minimax signs, algebraic isolation, prefactors, capacity arithmetic, and
canonical dependency pins; certificate and root replays are byte-identical.

The no-go is deliberately restricted to centered circular pointwise
absolute-value bounds with the radius as the only variable.  The result is a
component ceiling only.  The booked rate and frozen deficit stay unchanged,
and $0.5908590983307739249345460183\ldots$ remains to be supplied outside
this component even under maximal credit.  Route 1 remains ACTIVE and Route
2 remains QUEUED.

## 2026-09-01 — independently audited Item 417

Item 417 audits every degree-forced prime-power Cartier-zero level for the
actual Item-390 residue pair.  If $E_m$ is the squarefree product of new
primes left after removing canonical Item 200's $F_m$, then



$$
F_mE_m\mid\lambda_{0,m},\lambda_{1,m},
\qquad
p\mid E_m\Longrightarrow p\le\sqrt{6m},
\qquad
\log E_m=o(m).
$$



The proof permits different witnessing levels in the two coordinates and
uses the exact iterated Cartier degree criterion.  Root completed the
displayed $q>6m$ exclusion for both adjacent rows before promotion.

Uniform higher multiplicity is false in the actual family.  The ordinary
row $(m,p)=(2,11)$, the Item-149 overlap row $(9,13)$, and the genuinely
higher-level row $(5,5)$, where $q=25$ qualifies but $q=5$ does not,
all have common valuation exactly one.  Once an iterated Cartier image is
zero, later images remain zero; the levels are nested characteristic-$p$
statements and cannot be counted as independent digits.

Thus the pure degree-zero tower is closed as a zero-rate,
nonmultiplicative mechanism.  It leaves Item 418's current component ceiling
and every central ledger quantity unchanged.  Integral/Witt lifts and
arithmetic common factors outside degree-forced zero images remain open.

## 2026-09-01 — independently audited Item 419

Item 419 classifies the remaining transverse foreign factors in the
ordinary-$j=2$ selected-prime tail.  If $q>p$ is in the opposite
nonzero residue class from $2r+3$, then



$$
Q^\perp={2q-2r-3\over3}\in2\mathbb Z+1,
\qquad
3Q^\perp+2r+3=2q.
$$



The lower finite-beta tail has exactly one $q$-multiple, the top
denominator $2q$, with binomial coefficient one.  The normalized terminal
therefore survives.  However the ordinary upper-tail parameter
$(r+Q^\perp+1)/2$ is half-integral, so the existing factorial period,
$f$-vector, and Item-409 target/rejection residual do not transport by
direct substitution.  This is a scoped parity obstruction, not a no-go for
a newly derived odd-sheet formula.

Canonical Item 314's algebraic height $h(a_r)=O(r)$, together with the
exact divisor chain through $\Pi_r$, improves the actual full-forward
foreign screen to



$$
B_e^{[p]}(M)=O(M^2/\log M),
\qquad
\sum\omega(F_{r,s}^{[p]})=O(M^2/(\log M)^2).
$$



Root corrected the draft's height attribution from Item 315 to Item 314,
added direct pins for Items 250, 314, and 349, and regenerated byte-identical
canonical and root replays.  The bounds remain superlinear, so no capacity
or booking changes and the ordinary-$j=2$ ceiling remains $1/105$.

## 2026-09-01 — independently audited Item 420

Item 420 moves beyond the circular optimization and analyzes the actual
size of every fixed rational combination of the two normalized
strictly-large carrier coordinates.  Both coordinates are constant terms
of amplitudes against one phase



$$
H(y)={(1-y)^6\over y^4(1+y^2)^4}.
$$



At every dominant critical point, the amplitude ratio is $f_1/f_0=5/2$.
Hence the only fixed leading cancellation is
$D_m=2\lambda_{1,m}-5\lambda_{0,m}$.  Exact integration by parts gives



$$
D_m={1\over m}\operatorname{CT}\!\left(
{y^4-4y^2-1\over2y(1+y^2)^2}H(y)^m\right).
$$



The resultant of the critical cubic with the new numerator is $176$, so
the new amplitude is nonzero at the saddles.  Standard two-saddle expansion
and a conjugate-phase subsequence argument prove



$$
\limsup |a\lambda_{0,m}+b\lambda_{1,m}|^{1/m}=\rho_*
$$



for every fixed nonzero rational pair $(a,b)$.  After division by $F_m$,
the root is $\rho_*e^{-\mathfrak C_F}$.

Root checked the exact rational identities, the nonzero resultants, the
two-saddle limsup argument, and the dependency pins before canonical
promotion.  This closes absolute-height arguments using one fixed
coordinate combination, regardless of contour shape.  It does not control
the joint gcd or $m$-dependent combinations.  The Item-418 component
ceiling and all ledger quantities remain unchanged.

## 2026-09-01 — independently audited Item 421

Item 421 asks whether Item 415's normalized residue coordinates also give
an exact carrier for Item 393's post-booking $p\le6m$ primitive remainder.
Three exact actual-family rows settle the proposed bridge negatively:



$$
F_2=11,
 \qquad c_2=288,
$$



so the Item-200 factor is not a second content divisor after $G_m$ has
already been removed.  At $(m,p)=(9,47)$, the post-booking depth is one
while both normalized coordinates are $47$-adic units.  More decisively,
at the booked overlap row $(13,11)$,



$$
v_{11}(c_{13})=2,
 \quad
 v_{11}(\lambda_{0,13})=v_{11}(\lambda_{1,13})=1,
 \quad
 11\in\mathcal P_{13}\cap\mathcal H_{13}.
$$



After the squarefree $F_m$-copy is divided, the normalized carrier again
has depth zero while one unbooked content digit remains.  Root independently
reconstructed the residue coordinates and contents, checked all memberships
and valuations, replayed the full $m\le100$ normalization census without
using it asymptotically, and replaced temporary Item-417 pins by canonical
ones.

Together with Item 417, the result closes exact $F_m$-carrier reuse plus
pure characteristic-$p$ degree-zero tower multiplicity.  Integral
Witt/Dwork lifts and weighted support estimates remain open.  A bare
squarefree support cutoff must satisfy
$\alpha<3.5451545899846435496\ldots$ before its $\alpha/6$ ceiling is
even smaller than the Item-418 outside-component comparison residual.  No
booking or global/component ceiling changes.

## 2026-09-01 — independently audited Item 422

Item 422 repairs the parity mismatch isolated in Item 419.  On the odd
transverse sheet the target is even, and matching the even coefficients
gives the integral parameter $D^\perp=(Q^\perp+r+2)/2$.  The resulting
terminating-binomial upper tail is exact.

The new object is nevertheless resonant.  Anti-reciprocal coefficient
reversal proves that its specialized vector is a unit multiple of the old
Item-349 $v$-column, so adjoining it leaves the connection-minor ideal
unchanged.  It contains no source-$s$ target period and cannot distinguish
target from rejection within this column information class.  Root checked
the all-$r$ rational identity, 7,001 termwise equalities, five explicitly
non-actual geometry/formula rows, and all unit conditions.  The natural
parity companion is closed at zero booking; the $1/105$ ceiling remains.

## 2026-09-01 — independently audited Item 423

Item 423 proves that every nonzero same-index fixed-degree polynomial
combination of $\lambda_{0,m},\lambda_{1,m}$ has limsup root $\rho_*$.
After the unique first cancellation $2\lambda_1-5\lambda_0$, a second tied
polynomial cancellation would require the nonreal saddle ratio whose exact
cubic is



$$
320t^3-400t^2+220t-11
$$



with discriminant $-3{,}460{,}300{,}800$.  Root checked the elimination,
nonvanishing resultants, degree comparison, and conjugate-phase subsequence
argument.  The theorem closes ordinary height bounds from one polynomial
Bezout combination, but not shifted rows, adaptive coefficients, or the
joint gcd.  The Item-418 ceiling is unchanged.

## 2026-09-01 — independently audited Item 424

Item 424 constructs a genuine first integral Witt/Bockstein endpoint vector
on every ordinary rank-zero row with $p^2>4m+1$:



$$
\mathcal W_s=(R_s,L_s/p,E_s/p)\pmod p.
$$



Its two determinants are $\kappa=A_m/p\bmod p$ and
$\xi=8B_m/p^2\bmod p$.  With $b=v_p(K_m)$, one has the exact actual-family
criterion



$$
v_p(c_m)\ge b+1\iff\kappa=0,
$$



and nonzero $\xi$ stops the depth exactly at $b+1$.  The row
$(13,11)$ has endpoint vectors $(7,6,6)$, $(2,8,3)$ and digits
$(\kappa,\xi)=(0,8)$, which proves $v_{11}(c_{13})=2$ and precisely
explains Item 421's missing digit.

Root audited the quotient/remainder factorization, integral primitive,
zero-boundary Bockstein, determinant normalization, booked overlap, and all
1,953 finite replay incidences without density inference.  A complete first
Witt layer has raw ceiling $0.3895079179997942812\ldots$, insufficient by
itself even under perfect saturation, and no positive mass is yet proved.
The result opens the integral higher-Witt branch but changes no ledger entry.
