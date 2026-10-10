> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The special-gcd two-branch conjecture and its factorial-series boundary

Date: 2026-09-13. Bounded continuation of
`hp_special_gcd_unit_lift.md`. This note contains one completed finite
falsification test, a new elementary differential lemma, an exact
reformulation of the unresolved exclusion, and a primary-source check.
It does not establish the two-branch conjecture.

Let



$$
H_n(x)=n![t^n]e^{xt}\phi(t)^n,\quad
 \phi(t)=1-t+t^2/2,\quad
 J_n(x)=nH_n(x)+H_n'(x),\quad
 g_n=\gcd(H_n(1),J_{n+1}(1)).
$$



## 1. The predeclared test and exactly what it says

The statement tested was



$$
Z_{p,1}:=\{0\le r<p:H_r(1)=J_{r+1}(1)=0\pmod p\}
 \subseteq\{1,p-1\}.                                      \tag{1}
$$



The range was all odd primes p<=101, in increasing order, with immediate
termination if a counterexample appeared. Direct powers of phi modulo p
and falling factorials computed both gates, independently of the
four-coordinate recurrence. The complete result was



$$
Z_{5,1}=\{1,4\},\qquad Z_{p,1}=\{1\}
 \quad(3\le p\le101,\ p\ne5).
$$



The code and full root sets are in `check_hp_two_branch_residues.py` and
`hp_two_branch_residue_checks.json`. No larger range was tested. The
absence of a counterexample is finite evidence, not a uniform theorem.

## 2. A useful exact equivalent of the uniform conjecture

The local results proved and independently checked in
`hp_special_gcd_unit_lift.md` give, for odd p,



$$
\begin{array}{ll}
 p\mid n-1:&v_p(g_n)=v_p(n-1),\\
 p\mid n+1:&v_p(g_n)=\min\{v_p(n+1),\lambda_p\},
 \end{array}                                               \tag{2}
$$



where lambda_p is the valuation of the factorial constant in Section5.
Both H_n(1) and J_(n+1)(1) preserve index congruences modulo every odd
prime power.

Consequently, the assertion (1) for every odd prime is equivalent to



$$
\boxed{\operatorname{oddpart}(g_n)\mid n^2-1
        \quad\hbox{for every }n\ge2.}                      \tag{3}
$$



Indeed, (1), index congruences, and (2) bound each odd valuation by the
corresponding valuation of n^2-1. Conversely, a joint root r outside
the two indicated residues would have r>=2 and would contradict (3)
at n=r. The residue r=0 is impossible because H_0(1)=1.

Thus the conjecture would do more than exclude primes p>2n+2: it would
give an O(log n) bound for the logarithm of the odd part of this exact
auxiliary gcd. The proven relation between this auxiliary gcd and the
full HP endpoint gcd still applies only for p>2n+2. Small-prime moment
and factorial valuations cannot be bypassed using (3).

Deciding which primes have lambda_p>0 is unnecessary for the bound (3):
the exact unit-2 lift already caps the entire residue -1 branch by
v_p(n+1), even if lambda_p is infinite.

## 3. A differential identity and the common-root simplicity lemma

The actual polynomial H_n satisfies



$$
\boxed{xH_n'''+(n+2-2x)H_n''+2(x-1)H_n'-2nH_n=0.}          \tag{4}
$$



For a direct proof, write F(t)=e^(xt)phi(t)^n and use
phi(F'-xF)=n phi' F, where the prime here differentiates in t.
Multiply by t and extract its t^n coefficient. Replacing the coefficients
of t^(n-j)F by H_n^(j)/n! gives (4). This is an identity over the rationals,
and all its displayed polynomial coefficients are integral.

Suppose p is odd, 1<=r<=p-2, and r is a joint root of the two gates.
The exact raising identity from the preceding note gives



$$
H_r(1)=0,\qquad H_r''(1)+(r-1)H_r'(1)=0\pmod p.             \tag{5}
$$



The factor r+1 was canceled only because r<=p-2. Then



$$
\boxed{H_r'(1)\ne0\pmod p.}                              \tag{6}
$$



To prove this, assume H_r'(1)=0. Equation(5) gives H_r''(1)=0.
Differentiating (4) j times and evaluating at x=1 gives



$$
H_r^{(j+3)}(1)+(r+j)H_r^{(j+2)}(1)
 -2jH_r^{(j+1)}(1)+2(j-r)H_r^{(j)}(1)=0.                    \tag{7}
$$



Its leading coefficient is1. Hence the first three vanishing derivatives
force every derivative through order r to vanish. Since r<p, the
factorials through r! are units in F_p; Taylor expansion at1 would make
the entire degree-r monic polynomial zero. This is impossible. For
r<3 the same conclusion follows immediately from the first derivatives.

This proves that any exceptional common gate is a simple x-root of H_r.
It does not say that it is a simple root as a function of the index r,
and it does not exclude that root. In fact (5) leaves the nonzero first
derivative free. Confusing those two kinds of roots would invalidate a
Hensel or multiplicity argument.

## 4. The exact finite-field boundary problem that is still missing

The preceding differential equation can be normalized without large
factorial denominators. For an indeterminate N define integer
polynomials d_j(N) by



$$
d_0=0,\quad d_1=1,\quad d_2=1-N,
$$




$$
d_{j+3}=-(N+j)d_{j+2}+2j d_{j+1}+2(N-j)d_j.                \tag{8}
$$



For example d_3=N(N-1) and d_4=-N(N-1)(N+1).
For a prime p>r+2 and an integer r>=2, the original pair of gates
vanishes modulo p if and only if



$$
\boxed{d_{r+1}(r)=d_{r+2}(r)=0\pmod p.}                   \tag{9}
$$



Necessity follows from (5), (6), (7), after dividing every derivative by
H_r'(1). For sufficiency, construct



$$
f(x)=\sum_{j=0}^r d_j(r)(x-1)^j/j!\in\mathbb F_p[x].
$$



The factorials are invertible. Assuming (9), recurrence(8) also gives
d_(r+3)=0. The derivatives through order r of the left side of (4)
all vanish at1 by (8); that left side has degree at most r, so it is
identically zero. The polynomial f has f'(1)=1.

Finally the degree<=r polynomial solution space of (4) over F_p is
one-dimensional. To see this, for a polynomial sum a_k x^k its coefficient
equation is



$$
2(r-k)a_k=(k+2)(k+1)(r+k+2)a_{k+2}
                -2(k+1)^2a_{k+1}.                         \tag{10}
$$



For 0<=k<r all factors 2(r-k) are units, so the leading coefficient
determines the rest. Every nonzero solution has degree r by its highest
coefficient equation. Therefore f is a nonzero multiple of H_r and (5)
holds; the original J gate follows.

Equation(9) is an exact reformulation, not a new nonvanishing theorem.
To settle just the large-prime endpoint obstruction, it would suffice
to prove that the two integers in (9) have no common prime divisor
greater than2r+2. The broader two-branch conjecture requires the other
prime/index ranges as well. The local recurrence admits the initial
data (0,1,1-r); the unproved step is their inability to satisfy both
terminal conditions modulo the relevant large prime.

The previously proved HP Wronskian degree bound likewise permits the
maximal-multiplicity case corresponding to these two gates. No strict
finite-field normality result was established in this bounded attempt.

## 5. Exact Euler-factorial and truncated-exponential formulas

Let i^2=-1 and put alpha=(1+i)/2, beta=(1-i)/2. For odd p these elements
are units in every completion of Q(i) above p. Since



$$
\phi(t)=(1-\alpha t)(1-\beta t),\qquad
 c_r=[t^r]\phi(t)^{-1}
     =\frac{\alpha^{r+1}-\beta^{r+1}}i,
$$



the already convergent constant



$$
\mathcal C_p=\sum_{r\ge0}(-1)^r r!c_r
$$



has the exact expression



$$
\boxed{\mathcal C_p=
 \frac{\alpha\,\mathfrak F_p(-\alpha)
       -\beta\,\mathfrak F_p(-\beta)}i,\qquad
 \mathfrak F_p(z)=\sum_{r\ge0}r!z^r.}                      \tag{11}
$$



It is fixed by conjugation and belongs to Q_p. The identity follows
term by term from convergent series; it is not an identification with
the ordinary left-factorial constant sum r!.

There is also a finite formula requiring no choice of a p-adic embedding.
Work in the quadratic etale algebra F_p[i]/(i^2+1), including its split
case. Define



$$
\mathfrak F^{[p]}(z)=\sum_{r=0}^{p-1}r!z^r,\qquad
 \mathfrak E^{[p]}(z)=\sum_{k=0}^{p-1}z^k/k!.
$$



Wilson's theorem gives, at any unit z,



$$
\mathfrak F^{[p]}(z)
       =-z^{p-1}\mathfrak E^{[p]}(-1/z).                   \tag{12}
$$



Indeed substitute r=p-1-k and use (p-1-k)!=(-1)^(k+1)/k!
modulo p. Applying (12) to (11) yields



$$
\boxed{\mathcal C_p\equiv
 -\frac{\alpha^p\mathfrak E^{[p]}(1-i)
       -\beta^p\mathfrak E^{[p]}(1+i)}i\pmod p.}           \tag{13}
$$



Here alpha^p=alpha and beta^p=beta when p=1 mod4; the two are exchanged
when p=3 mod4. Thus the residue -1 branch is an explicit relation between
two conjugate truncated exponentials. The known value v_5(C_5)=2 shows
that a universal p-unit claim for this weighted constant would already
be false.

## 6. What the primary literature does and does not supply

The exact expression(11) places the boundary constant in the arithmetic
of Euler factorial series and linear combinations with recurrence
weights. It is reasonable to call it a weighted left-factorial value;
no standard name or theorem specifically for this weight was located.

[Matala-aho and Zudilin, Euler's factorial series and global relations](https://arxiv.org/pdf/1703.02633)
construct explicit Pade approximants to the factorial series. Their
Theorem1 is a statement across a sufficiently large collection of primes,
at a fixed nonzero integer argument. It does not assert a nonzero residue
or a valuation bound at each specified prime. Their discussion connects
the ordinary factorial sum to Kurepa's conjecture. Our two algebraic
arguments and their linear combination require separate treatment.

[Seppala, Euler's factorial series at algebraic integer points](https://arxiv.org/pdf/1809.10997)
is the closer structural match: it studies linear combinations at several
algebraic integer arguments and treats recurrence weights in Section9.2.
Theorem3.1 gives existence of a nonvanishing valuation in a qualifying
collection, and Theorem3.4 gives a valuation at a prime in a height-dependent
interval. Neither is a theorem at every fixed p. Moreover, our arguments
-(1+-i)/2 are not algebraic integers; multiplying the linear-form
coefficients does not remove this argument hypothesis. Rescaling the
formal series leads to the generalized factorial weight r!/2^r, whose
local and global denominator estimates must be checked anew before any
published main theorem can be applied.

[Ernvall-Hytonen, Matala-Aho and Seppala, Euler's factorial series, Hardy integral, and continued fractions](https://arxiv.org/pdf/2111.13649)
provides fixed-prime lower bounds. Theorem1.4 assumes a nonzero integer
argument t with |t|_p<1 and an additional explicit smallness inequality;
its corollaries specialize to t=+-p^a. Our two arguments have p-adic
absolute value1 at every odd p and also occur in a linear combination,
so these hypotheses fail.

[Mestrovic, Variations of Kurepa's left factorial hypothesis](https://arxiv.org/pdf/1312.7037)
records the ordinary left-factorial/truncated-exponential equivalence and
several determinant formulations. Formula(13) is the corresponding exact
calculation for our quadratic weight. The ordinary Kurepa assertion,
even if assumed, does not prevent cancellation in our conjugate
combination; no equivalence to that assertion is claimed here.

The useful next target is the other-residue exclusion (9), or a more
direct special-value identity proving (3). Establishing nonvanishing of
C_p at every prime is both stronger than needed for the -1 branch's gcd
upper bound and contradicted if interpreted as a p-unit statement.

## 7. Verification and current scope

`check_hp_two_branch_identities.py` checks (4), (7), (8), and (10) against
four fixed exact polynomial controls n=1,2,4,8, and independently checks
(11)--(13) modulo the fixed primes3,5,7,13 in the quadratic algebra.
These checks support signs and normalization; Sections2--5 contain the
proofs of the identities and implications.

Audit_computations independently reviewed Sections3--4 and accepted the
x-ODE, both coefficient recurrences, the simple-root implication, and
the two-terminal-condition equivalence. In particular it verified the
last residual derivative and the one-dimensional polynomial solution
space used in the converse. No gap was found.

The two-branch theorem, the auxiliary odd-gcd bound (3), the large-prime
endpoint-gcd exclusion, and a useful bound for the final primitive
denominator all remain unproved. No irrationality claim follows from
the completed bounded test or the new reformulations.
