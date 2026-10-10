> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 339 — integral local coefficient, complete carry classification, and the growing-rank obstruction for fixed (j=1)

Date: 2026-09-01

## 1. Outcome and capacity first

Item 332 reduced the factor actually selected by the ordinary fixed-(j=1)
collision to



$$
b_h=[t^{2h}]F(t)^{4h/3},\qquad
 F(t)=1-2t+{3\over2}t^2-{1\over2}t^3.                    \tag{1.1}
$$



This item uses the *actual* row



$$
M=3h+4s+2,\qquad p=4h+6s+3                            \tag{1.2}
$$



and keeps the selected factor itself.  Put



$$
n=2h,\qquad r=2s+1.                                      \tag{1.3}
$$



Then



$$
p=2n+3r,\qquad 2M=3n+4r.                                \tag{1.4}
$$



The first theorem is the exact actual-row Frobenius reduction



$$
\boxed{
 b_h\equiv[t^n]F(t)^{-r}\pmod p.}                        \tag{1.5}
$$



After the integral change of scale



$$
G(u)=F(2u)=1-4u+6u^2-4u^3=(1-u)^4-u^4,                 \tag{1.6}
$$



define



$$
\boxed{
 a_{r,n}=2^n[t^n]F(t)^{-r}=[u^n]G(u)^{-r}\in\mathbb Z.}  \tag{1.7}
$$



Every actual (p) is odd, so (1.5)--(1.7) give



$$
\boxed{
 p\mid\operatorname{num}(b_h)\quad\Longleftrightarrow
 \quad p\mid a_{r,n}.}                                   \tag{1.8}
$$



The integer has the positive hypergeometric-prefix formula



$$
\boxed{
 a_{r,n}=\sum_{k=0}^{\lfloor n/4\rfloor}
 {r+k-1\choose k}{4r+n-1\choose n-4k}.}                 \tag{1.9}
$$



Lucas's theorem completely classifies when every summand in (1.9) is
forced to vanish modulo the tied prime:



$$
\boxed{
 p\text{ divides every summand of (1.9)}
 \quad\Longleftrightarrow\quad
 r=n+1, n\equiv2\pmod4.}                                \tag{1.10}
$$



On the original variables this is precisely



$$
\boxed{h=s\text{ odd},\qquad p=10h+3,\qquad M=7h+2.}   \tag{1.11}
$$



At a fixed (M), (1.11) supplies at most one row.  Its logarithmic mass
is therefore (O(\log M)=o(M)).  Outside this ray at least one summand
is a (p)-unit, but cancellation remains possible: the preselected row
((h,s,p)=(8,2,47)) has five (p)-unit summands whose sum is zero.

There is also a rigorous complexity obstruction.  For fixed (r), the
sequence (n\mapsto a_{r,n}) has reduced generating function



$$
\sum_{n\geq0}a_{r,n}u^n=G(u)^{-r}.                       \tag{1.12}
$$



Its exact minimal constant-coefficient recurrence order is



$$
\boxed{3r=6s+3}                                         \tag{1.13}
$$



over both (mathbb Q) and every actual (mathbb F_p).  The fixed-(M)
rows on which this rank, or the surviving-prefix length, is (o(M))
have weighted prime mass (o(M)).  Thus the direct local-recurrence and
bounded-tail methods reach only zero-rate edges; the positive-rate bulk
is a linearly growing-rank, linearly growing-length cancellation problem.

No cancellation/nonconcentration theorem is proved here.  Consequently



$$
\boxed{
 \text{new linear log rate}=0,\qquad
 \text{new fixed-}j=1\text{ ceiling reduction}=0.}        \tag{1.14}
$$



The retained ceiling is (1/36) per (6M).  The missing global input is
a uniform mod-(p) cancellation theorem, an average-gcd theorem, or a
genuine factor-localization theorem for (1.9), not one more local jet.

## 2. Why Frobenius removes the cubic branch

Let



$$
U(t)=F(t)^{1/3},\qquad U(0)=1.                            \tag{2.1}
$$



The coefficients of (U) lie in (mathbb Z[1/6]), so every actual
prime permits reduction.  Let



$$
\eta\equiv h\equiv p\pmod3,\qquad \eta\in\{1,2\}.       \tag{2.2}
$$



The value (eta=0) is impossible because (p>3) is prime.  In
(mathbb F_p[[t]]), Frobenius gives



$$
U(t)^p=U(t^p)
       =U(t)^\eta F(t)^{(p-\eta)/3}.                      \tag{2.3}
$$



Since (4h\equiv\eta\pmod3), equations (1.2)--(1.3) imply



$$
\begin{aligned}
 F(t)^{4h/3}
 &=F(t)^{(4h-\eta)/3}U(t)^\eta\\
 &=U(t)^pF(t)^{(4h-p)/3}\\
 &=U(t^p)F(t)^{-r},                                      \tag{2.4}
\end{aligned}
$$



because ((4h-p)/3=-(2s+1)=-r).  Finally (n=2h<p), so
only the constant term of (U(t^p)) can contribute to degree (n).
This proves (1.5).

This is a structural clarification.  The natural Frobenius lift does
not produce an additional cubic branch at the target degree.  It consumes
that branch and leaves the moving local coefficient of (F^{-r}).  This
statement does not rule out some different future global transformation;
it identifies exactly what the direct Frobenius realization still has to
control.

## 3. The exact integral hypergeometric prefix

From (1.6),



$$
G(u)^{-r}
 =(1-u)^{-4r}
  \left(1-\left({u\over1-u}\right)^4\right)^{-r}.         \tag{3.1}
$$



Expanding the second factor gives



$$
G(u)^{-r}
 =\sum_{k\geq0}{r+k-1\choose k}
   u^{4k}(1-u)^{-4r-4k}.                                  \tag{3.2}
$$



The coefficient of (u^n) in the (k)-th term is



$$
{r+k-1\choose k}
 {4r+4k+n-4k-1\choose n-4k},                             \tag{3.3}
$$



which proves (1.9).  In particular, (a_{r,n}) is an integer and every
summand is positive over (mathbb Z).  Positivity is useful for defining
the object exactly, but it does not prevent cancellation after reduction
modulo a moving prime.

The prefix is also carried globally by one fixed rational function.  Put



$$
\mathscr C(z,u)={zG(u)\over G(u)^2-z^2}.                 \tag{3.4}
$$



Summing the odd powers (r=1,3,5,\ldots) gives



$$
\mathscr C(z,u)
 =\sum_{\substack{r\geq1\\r\ {\rm odd}}}
  \sum_{n\geq0}a_{r,n}z^ru^n.                            \tag{3.5}
$$



For a fixed (M), define



$$
\mathcal R_M(w)=[x^{2M}]\mathscr C(wx^4,x^3).           \tag{3.6}
$$



Then



$$
[w^r]\mathcal R_M(w)=a_{r,n}\quad
 \text{whenever }3n+4r=2M.                               \tag{3.7}
$$



Moreover the tied candidate prime is read directly from that exponent:



$$
p={4M+r\over3}.                                         \tag{3.8}
$$



Thus the unresolved values do have a single fixed bivariate arithmetic
carrier.  What is open is a theorem controlling its moving coefficients
at their correspondingly moving primes.

## 4. Complete termwise Lucas/Kummer classification

Write



$$
N=4r+n-1,qquad d=N-p=r-n-1,\qquad m_k=n-4k.             \tag{4.1}
$$



The first factor in the (k)-th summand of (1.9) is always a (p)-unit:



$$
r+k-1<p,qquad k<p.                                      \tag{4.2}
$$



There are two cases.

If (r\leq n), then (d<0), hence (N<p).  Every second factor
({N\choose m_k}) is a (p)-unit as well.  Thus every summand in
(1.9) is individually nonzero modulo (p).

If (r\geq n+1), then (d\geq0) and (N=p+d<2p).  Since
(0\leq m_k<p), Lucas's theorem gives



$$
{p+d\choose m_k}\equiv{d\choose m_k}\pmod p.          \tag{4.3}
$$



Therefore the surviving terms are exactly



$$
m_k=n-4k\leq d.                                         \tag{4.4}
$$



Let



$$
\delta=n\bmod4\in\{0,2\}.                              \tag{4.5}
$$



Both (d) and (delta) are even.  All terms vanish exactly when the
smallest possible (m_k), namely (delta), exceeds (d).  The only
possibility is



$$
d=0,\qquad\delta=2,                                     \tag{4.6}
$$



which is (1.10).  The number of surviving terms is therefore



$$
\ell(r,n)=
 \begin{cases}
 \lfloor n/4\rfloor+1, & r\leq n,\\[2mm]
 0, & r>n\text{ and }\min(d,n)<\delta,\\[2mm]
 \left\lfloor{\min(d,n)-\delta\over4}\right\rfloor+1,
    & r>n\text{ and }\min(d,n)\geq\delta.
 \end{cases}                                             \tag{4.7}
$$



For (r>n), the entire target reduces explicitly to the surviving tail



$$
a_{r,n}\equiv
 \sum_{\substack{0\leq k\leq\lfloor n/4\rfloor\\n-4k\leq d}}
 {r+k-1\choose k}{d\choose n-4k}\pmod p.                \tag{4.8}
$$



Equations (4.6)--(4.8) close the termwise-carry question for this exact
prefix.  They do not close cancellation among surviving terms.

## 5. The exact recurrence rank and the zero-rate edges

For a fixed positive integer (r), (1.12) is already reduced: its
numerator is (1), while (G(0)=1), (deg G=3), and the leading
coefficient of (G) is (-4).  Consequently the denominator (G^r)
has degree (3r) over (mathbb Q) and over every actual
(mathbb F_p).  A reduced rational generating function has minimal
homogeneous constant-coefficient recurrence order equal to its denominator
degree.  This proves (1.13).

The capacity consequence uses the following elementary short-interval
lemma.

> **Weighted short-interval lemma.** If a set of fixed-(M) rows has all
> of its candidate primes in (O(1)) intervals of total length
> (Y(M)=o(M)), then its total (log p)-weight is (o(M)).

For (Y\leq M/(\log M)^2), the trivial integer count gives
(O(Y\log M)=o(M)).  For larger (Y=o(M)), Brun--Titchmarsh gives
(O(Y/\log Y)) primes; because (log Y\sim\log M), their logarithmic
weight is (O(Y)=o(M)).

At fixed (M), equations (1.4) give



$$
p={4M+r\over3}={6M-n\over4}.                            \tag{5.1}
$$



Hence rows with (r=o(M)), and therefore recurrence rank (3r=o(M)),
lie in a candidate-prime interval of length (o(M)).  They have zero
rate.

Likewise, (4.7) shows that (ell(r,n)=o(M)) implies one of



$$
n=o(M),\qquad d=r-n-1=o(M)                              \tag{5.2}
$$



on the appropriate row intervals.  Each condition describes (O(1))
candidate-prime intervals of total length (o(M)), so the short-prefix
support also has zero rate.

This is the precise scoped obstruction:



$$
\boxed{
 \begin{gathered}
 \text{bounded or sublinear direct recurrence rank, and bounded or}\\
 \text{sublinear surviving-tail length, cannot control positive-rate}\\
 \text{fixed-}j=1\text{ mass.}
 \end{gathered}}                                         \tag{5.3}
$$



It is not a no-go theorem for an as-yet unknown global transformation,
an average-gcd theorem, or a nonconcentration theorem specialized to
(mathscr C).

## 6. Exact controls and why universal nonvanishing is the wrong target

The deterministic certificate uses only these five rows selected before
the present theorem; it performs no scan.

| ((h,s,p)) | ((n,r,d,\delta)) | residues of the summands in (1.9) | (ell) | (a_{r,n}\bmod p) |
|---|---:|---|---:|---:|
| ((1,1,13)) | ((2,3,0,2)) | (0) | (0) | (0) |
| ((2,1,17)) | ((4,3,-2,0)) | (5,3) | (2) | (8) |
| ((8,2,47)) | ((16,5,-12,0)) | (1,4,43,23,23) | (5) | (0) |
| ((4,4,43)) | ((8,9,0,0)) | (0,0,2) | (1) | (2) |
| ((2,6,47)) | ((4,13,8,0)) | (23,13) | (2) | (36) |

The first row is the forced ray (1.11).  The fourth shows why the parity
condition in (1.10) is essential: at (d=0) and (delta=0), the final
(m_k=0) term survives.  Most importantly, the third row proves that
complete termwise unit support does not imply a nonzero sum.  It is an
exact cancellation witness, not an asymptotic sample and not a full
original collision.

## 7. Strategic conclusion

Define the selected-factor envelope



$$
W_b(M)=
 \sum_{\substack{h,s\geq1,\ M=3h+4s+2\\
                   p=4h+6s+3\ {\rm prime}\\
                   p\mid\operatorname{num}(b_h)}}\log p. \tag{7.1}
$$



The theorem required for a fixed-(j=1) ceiling reduction remains



$$
\boxed{W_b(M)=o(M).}                                    \tag{7.2}
$$



Item 339 settles the complete termwise-carry component of (7.2): its only
forced family has zero rate.  It also proves that the natural exact
one-variable recurrence and short-tail realizations have growing
complexity on every positive-rate bulk.  Therefore the next admissible
attack must address *cancellation* globally.  Suitable theorem targets
are:

1. a mod-(p) nonconcentration theorem for the prefix (1.9) along
   (p=2n+3r);
2. an average-gcd or factor-localization theorem for coefficients of the
   fixed rational carrier (3.4)--(3.7); or
3. a genuinely different fixed-rank Frobenius representation, accompanied
   by a proof that it implies the original selected-factor gate.

No generic height estimate, old algebraic curve, unselected parity,
bounded-gap row propagation, or finite zero census is used here.

## 8. Strict labels

### PROVED

- the actual-row Frobenius reduction (1.5);
- the integral normalization (1.7) and positive prefix (1.9);
- the fixed rational bivariate carrier (3.4)--(3.7);
- the complete termwise Lucas/Kummer classification (1.10);
- the zero-rate capacity of the unique forced carry ray;
- the exact minimal direct recurrence order (3r);
- zero-rate support for sublinear direct recurrence rank or surviving-prefix
  length;
- the scoped local-recurrence/termwise-carry no-go (5.3).

### EXACT FINITE ONLY

- the five preselected controls in Section 6;
- in particular, the all-unit cancellation at (p=47) is a counterexample
  to termwise-unit nonvanishing, not a density statement and not a full
  ordinary collision.

### OPEN

- (W_b(M)=o(M));
- a uniform cancellation/nonconcentration theorem for (1.9);
- average-gcd or global factor localization for (mathscr C);
- any alternative global fixed-rank Frobenius representation;
- any positive fixed-(j=1) capacity reduction;
- fixed-(j=1) closure, Route 1, and every conclusion about (e+\pi).

## 9. Ledger consequence



$$
\begin{array}{c|c}
\text{quantity}&\text{Item 339 value}\\ \hline
\text{new independent condition}&0\\
\text{new proved linear log rate}&0\\
\text{new fixed-}j=1\text{ capacity reduction}&0\\
\text{forced termwise-carry mass}&O(\log M)=o(M)\\
\text{retained fixed-}j=1\text{ ceiling per }6M&1/36
\end{array}                                                \tag{9.1}
$$



Item 339 is strategic progress because it closes a complete natural
method class and isolates the exact missing global input.  It is not a
ledger gain.
