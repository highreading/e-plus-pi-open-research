> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Fixed-prime factorial growth: the actual endpoint-minor gate

Date: 2026-09-13. Bounded arithmetic continuation by audit_computations.
Independent review: PASS by audit_results; see raw_fixed_prime_denominator_gate_independent_review.md, including the exact frozen-input checks. This status applies to the proved formulas and conditional implications, not to the proposed fixed-prime bound.
This note does not prove the proposed all-even fixed-prime lower bound.
It gives an exact integral exponential endpoint border, separates the two
possible losses from the visible factorial, and explains precisely why the
existing saturation and Smith results do not close the gate. No canonical
degree was constructed and no degree or prime sweep was run.

## 1. The proposed obstruction concerns the reduced denominator

Write the actual canonical endpoint approximation as



$$
-A_n(1)=N_n/Z_n=p_n/q_n,\qquad
 q_n=|Z_n|/\gcd(|Z_n|,|N_n|),
\tag{1}
$$



where $B_n(1)=1,C_n(1)=4$. The already proved integral dual
normalization gives



$$
N_n=\widehat P_{e,n}(1)+4\widehat P_{a,n}(1),\qquad
 \widehat P_e=[\widehat Q e^z]_{\le2n},\quad
 \widehat P_a=[\widehat Q\arctan z]_{\le2n}.
\tag{2}
$$



Every polynomial in (2) is integral. In particular its endpoint gcd is
retained in (1). The exact augmented determinants satisfy



$$
\Delta_B=(-1)^{n+1}F_nZ_n,\qquad
 \Delta_A=(-1)^n n!F_nN_n.
\tag{3}
$$



Thus the extremal maximal-minor content $F_n$ cancels completely. A
divisor of $F_n$, however large, is not by itself a divisor of $q_n$.

The candidate under investigation is, for every fixed prime $p$,



$$
v_p(q_n)\ge n/(p-1)-O_p(\log n)\qquad(n\text{ even}).
\tag{4}
$$



There is no proof of (4) in the existing odd-prime results. At $p=2$ a
stronger all-index theorem is already proved:



$$
v_2(q_n)=n+2\lfloor(n+2)/4\rfloor.
\tag{5}
$$



Reference: raw_arctan_endpoint_dyadic_attempt.md and its independent
review. The old source note's finite-scope warning about (5) is superseded
by this session's proof.

## 2. The exact cofactor coordinates

Use the integer $(n+1)$-by-$n$ normalized difference matrix
$\mathsf Z$ of raw_endpoint_scalar_cauchy_restriction.md. Let



$$
\delta_r=\det\mathsf Z[\widehat r,:],\quad
 \Theta=\gcd_r|\delta_r|,\quad
 R=(2n)!/n!,\quad c_r=(2n)!/(n+r)!,
$$




$$
h=\gcd_r|c_r\delta_r|,\qquad 0\le r\le n.
\tag{6}
$$



All gcds are positive. The proved polynomial transport is



$$
h\widehat Q=R\mathscr P,
\quad
 \mathscr P(z)=\sum_{r,s=0}^n(-1)^{r+s}\binom ns\delta_r
 \frac{(n+r+s)!}{(n+r)!}z^{2n-r-s},
\tag{7}
$$



with $\operatorname{cont}\mathscr P=\Theta$. Put



$$
K=\mathscr P(1),\qquad
 J_e=h\widehat P_e(1),\quad J_a=h\widehat P_a(1).
\tag{8}
$$



Consequently



$$
hZ=RK,\qquad hN=J_e+4J_a,
\quad
 q=\frac{R|K|}{\gcd(R|K|,|J_e+4J_a|)}.
\tag{9}
$$



The last formula is exact even when the displayed integer pair has a
common factor $h$. It reduces the same rational number. Here $K\ne0$
by the established endpoint normality theorem.

## 3. A new integral exponential endpoint border

Define the positive integers



$$
D_{n,r}=\sum_{j=0}^{n+r}\binom{n+j}{j}(n+r)_j,
 \qquad (a)_j=a(a-1)\cdots(a-j+1).
\tag{10}
$$



Then the actual exponential endpoint has the exact formula



$$
\boxed{J_e=\sum_{r=0}^n(-1)^{r+n}c_r\delta_rD_{n,r}.}
\tag{11}
$$



The positivity in (10) does not make (11) a positive sum: the cofactors
and their alternating signs remain.

To prove (11), let $E_k=\sum_{j=0}^k1/j!$. Applying the endpoint Taylor
functional to (7) produces the row



$$
\ell_{e,r}=\sum_{s=0}^n(-1)^s\binom ns
 \frac{(n+r+s)!}{(n+r)!}E_{r+s}.
\tag{12}
$$



Use the elementary identity



$$
E_k=\frac1{k!}\int_0^\infty e^{-t}(1+t)^k\,dt.
$$



After setting $x=1+t$, the sum in the integral is precisely
$D_x^n[x^{n+r}(1-x)^n]$. Integration by parts $n$ times is valid:
the function inside the derivative has a zero of order $n$ at 1,
all boundary terms at infinity vanish against the exponential, and the
two signs at each integration cancel. Thus



$$
\ell_{e,r}=
 \frac{(-1)^n}{(n+r)!}\int_0^\infty e^{-t}(1+t)^{n+r}t^n\,dt
 =(-1)^n n!\sum_{j=0}^{n+r}
 \frac{\binom{n+j}{j}}{(n+r-j)!}.
\tag{13}
$$



Multiplying by $R$ gives
$R\ell_{e,r}=(-1)^nc_rD_{n,r}$, proving (11), including every
factorial and sign. This finite-sum identity was independently checked by
audit_sources after the note was saved; that scoped check does not serve
as an independent audit of the rest of the note. Equivalently



$$
J_e=(-1)^n\det[\mathsf Z\mid(R\ell_{e,r})_{r=0}^n].
\tag{14}
$$



No transcendental quantity occurs in (10), (11), or (14).

There is also a finite, exact first-layer border at every prime, without
assuming $p\mid n$. Put $a_0=n\bmod p$ and
$b_0=(n+r)\bmod p$, represented in $\{0,\ldots,p-1\}$. Then



$$
\boxed{D_{n,r}\equiv
 d_p(a_0,b_0):=
 \sum_{j=0}^{\min(p-1-a_0,b_0)}
 \binom{a_0+j}{j}(b_0)_j\pmod p.}
\tag{14a}
$$



For $j\ge p$, the falling factorial $(n+r)_j$ vanishes modulo
$p$. For $j<p$, its reduction is $(b_0)_j$, while the product
formula for $\binom{n+j}{j}$, whose denominator is a unit, reduces to
$\binom{a_0+j}{j}$ and is zero if $a_0+j\ge p$. This proves
(14a) directly. In particular, for $p\mid n$, the row depends only on
$r\bmod p$ and is $\sum_{j=0}^{r\bmod p}(r\bmod p)_j$.
It is not always a unit: for $p=5$, the entries at residues 2 and 4
are respectively $5$ and $65$, both zero modulo 5. These are zeros
of the border weights, not counterexamples to any assertion about the
actual cofactor sum.

More generally, at precision $p^b$, terms with $v_p(j!)\ge b$
vanish, since $(n+r)_j=j!\binom{n+r}{j}$. The border therefore needs
only $j<J_b$, where $J_b=\min\{j:v_p(j!)\ge b\}\le pb$.
Its reduction is periodic in both $n$ and $r$ modulo
$p^{2b-1}$. Indeed, for retained $j$, clearing the denominator
$j!$ in $\binom{n+j}{j}$ costs at most $b-1$ powers of $p$,
and falling factorials have integral coefficients. This gives a bounded
exact description of the endpoint border at each fixed precision. It
does not determine the primitive weighted cofactor vector multiplying
that border in (11).

For normalization only, the frozen $n=2$ primitive coefficients give
$(c_r\delta_r/h)_{r=0}^2=(940,64,49)$. Equation (10) gives
$(D_{2,0},D_{2,1},D_{2,2})=(19,106,685)$, and (11) gives
$940\cdot19-64\cdot106+49\cdot685=44641$, the already saved
$\widehat P_e(1)$. No degree was solved for this check.

## 4. The arctangent border is deep enough unless the exponential border is already deep

For a fixed prime put



$$
a=\lfloor\log_p(2n)\rfloor,\quad r_p=v_p(R),\quad
 d=v_p(h)-v_p(\Theta),\quad
 \kappa=v_p(K)-v_p(\Theta),\quad
 e=v_p(\widehat P_e(1)).
\tag{15}
$$



If $\widehat P_e(1)=0$, set $e=+\infty$. Since
$\Theta\mid h\mid R\Theta$, we have $0\le d\le r_p$, and
$\kappa\ge0$. Also $e\ge0$ whenever finite, by the established
integrality of $\widehat P_e$.

Every arctangent endpoint coefficient in (7) is a partial sum of
$\tau_j$, $1\le j\le2n$, whose denominator divides
$L_{2n}=\operatorname{lcm}(1,\ldots,2n)$. Therefore



$$
\boxed{v_p(J_a)\ge r_p+v_p(\Theta)-a,\qquad
 v_p(\widehat P_a(1))\ge r_p-d-a.}
\tag{16}
$$



This also follows from $L_{2n}\mid R$: every prime power at most $2n$
has a multiple among $n+1,\ldots,2n$, so the assertion holds prime by
prime. No $p$-integrality of an individual unscaled $\tau_j$ was
assumed.

In particular, if



$$
d+e<r_p-a,
\tag{17}
$$



the arctangent term is strictly deeper than the exponential term, even
before its additional factor 4. Hence $v_p(N)=e$ and (9) yields



$$
\boxed{v_p(q)=r_p-d+\kappa-e.}
\tag{18}
$$



The right side is positive under (17). Universally, including failure of
(17), one has the weaker but useful sufficient-target inequality



$$
\boxed{v_p(q)\ge\max\{0,r_p-d-e-a\}.}
\tag{19}
$$



Indeed, if (17) holds use (18); if it fails the expression inside the
maximum is nonpositive. Thus (19) makes no inference about cancellation
at equal valuations.

Since Legendre's formula gives
$r_p=n/(p-1)+O_p(\log n)$, the concrete sufficient estimate



$$
\boxed{v_p(h/\Theta)+v_p(\widehat P_e(1))=O_p(\log n)}
\tag{20}
$$



would prove (4). This is a sufficient target, not an equivalence:
the endpoint excess $\kappa$ in (18) can compensate for a larger
weighted-minor loss.

The two parts of (20) have distinct exact meanings. The first is



$$
d=\min_r\{v_p(c_r)+v_p(\delta_r)\}
       -\min_r v_p(\delta_r).
\tag{21}
$$



The second is the excess valuation of the signed sum (11) above that
weighted minimum. Rank information about $\mathsf Z$ alone does not
bound either difference. This is the precise minimum-minor and endpoint
cancellation obstruction.

## 5. What saturation proves, and why it cannot be accumulated

For $n=mp^\nu$, $p$ odd and $3m<p$, the reviewed Cauchy theorem
gives $\delta_n,\Theta,h$ all $p$-units. Thus $d=0$. Each
$c_r$, $r<n$, is divisible by $p$, while
$D_{n,n}\equiv1\pmod p$, because every nonconstant term in (10)
contains $2n$. Equation (11) gives $e=0$, recovering the actual
exponential numerator unit directly.

For the useful even family



$$
\boxed{n=2p^\nu,\quad p\ge7,\quad\nu\ge1,}
$$



the seed raw Legendre endpoint $Q_2(1)=4/3$ is a $p$-unit. The
already proved endpoint stability theorem gives $\kappa=0$, and
(16) is strictly positive. Consequently



$$
\boxed{v_p(q_{2p^\nu})=(2p^\nu-2)/(p-1).}
\tag{22}
$$



This is an immediate precise even-ray consequence of the existing
saturation theorem, now also consistent with (11). It does not apply
to all even indices.

More strongly, the saturation hypothesis cannot hold at two distinct
odd primes for the same positive $n$. If both $p,q\mid n$ were
saturated, then



$$
q\le n/p^{v_p(n)}<p/3,
 \qquad p\le n/q^{v_q(n)}<q/3,
$$



a contradiction. Thus the available saturated rays cannot be combined
to obtain an arbitrarily large finite set of simultaneous fixed-prime
factorial divisors. This is a logical obstruction to that proposed use
of the existing theorem, not a counterexample to (4).

For general odd $p\mid n$, the stronger existing rank theorem says



$$
\operatorname{rank}_{\mathbb F_p}\mathsf Z
 =n-\min(b,T-1-b),\quad
 T=p^{\lfloor\log_p(3n)\rfloor},\ b=n\bmod T.
\tag{23}
$$



It determines the nonunit Smith count and, through the exact congruence
modulo $n$, the Smith exponents truncated at $v_p(n)$. It does not
determine the relative valuations of the individual maximal minors in
(21), or the signed border (11). The unspecified deeper Smith layers
are precisely where a general extension has to do new work.

## 6. Closed cached diagnostic and earlier barriers

Only the already saved exact triples at $n=2,4,8,16$ were used. Their
endpoint sums were reduced by their exact gcd, with no polynomial solve:

|n|v2(q)|v3(q)|v5(q)|v7(q)|v11(q)|v13(q)|v17(q)|v19(q)|
|--:|--:|--:|--:|--:|--:|--:|--:|--:|
|2|4|0|0|0|0|1|0|0|
|4|6|1|0|0|0|0|0|0|
|8|12|2|1|1|0|0|0|0|
|16|24|6|1|2|1|1|0|0|

Exact reduced integers and source scope are saved in
raw_fixed_prime_denominator_cached_checks.json. These four cases do not
refute (4), and they do not establish a logarithmic uniform defect.
The displayed primes were a fixed small-prime list, not a search for a
favorable pattern.

The following earlier failures must remain separate:

* Smooth-divisor saturation is about $F_n$; (3) shows why it does not
  survive automatically in $q_n$.
* The simultaneous polynomial denominator $d_n^{II}=|K|/\Theta$ is
  different from the reduced endpoint denominator (9).
* The Gauss/Dwork coefficient-ray results control the raw Legendre seed
  endpoint on saturated rays. A unit analytic Dwork quotient does not
  prove nonvanishing of every coefficient-ray limit; higher seed
  valuations remain an explicit barrier in the existing note.
* The large-prime cubic carrier applies at $p>3n$, so it cannot be
  used as a fixed-small-prime estimate as $n$ grows.
* The older common-kernel rational-output saturation concerns another
  family and assumes rationality. It is not a valuation theorem for
  this raw HP family.

## 7. Consequence if the missing bound were proved

If (4) held for every fixed prime in arbitrarily large finite sets,
then, first fixing the finite set and then letting even $n\to\infty$,



$$
\liminf\frac{\log q_n}{n}
 \ge\sum_{p\in S}\frac{\log p}{p-1}.
$$



The right sides are unbounded as the finite prime set grows. Hence
$\log q_n/n\to\infty$. If, in addition, the actual endpoint error
has a proved nonzero exponential asymptotic, as targeted by the companion
endpoint-scalar assembly, then this would rule out shrinking primitive
forms along this entire even raw family. This last implication requires
an error estimate after division by $Z_n$; the already passed
unreduced-remainder asymptotic alone does not replace that input.
Neither implication proves rationality or irrationality of $e+\pi$.

At present only the dyadic theorem, special odd-prime rays, the exact
border (11), and the sufficient gate (20) are proved. The useful next
arithmetic question is a uniform comparison of the weighted minimum
and the bordered sum in (21)/(11), with the endpoint excess retained
if the sufficient target (20) is too strong. No lower bound on the
whole reduced denominator is inferred from an unnormalized clearing
factor.
