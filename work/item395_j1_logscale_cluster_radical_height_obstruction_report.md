> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 395 — the logarithmic-window cluster radical and the exact height obstruction for the actual fixed-$j=1$ gate

Date: 2026-09-01

## 1. Outcome and capacity first

Item 391 proved that a spacing argument first becomes capacity-relevant at
row offsets $d\asymp\log M$.  This item attacks that precise scale for the
actual joint Hasse--transverse collision set



$$
\mathcal Z_M=\{p\in\mathcal P_M:p\mid R_{H\mathscr T}(M)\},
 \qquad
 W(M)=\sum_{p\in\mathcal Z_M}\log p.                    \tag{1.1}
$$



No proof of logarithmic pair-freeness was found.  Instead, the exact
shifted formulas yield a rigorous arithmetic obstruction and a sharp target.

1. **PROVED — one aggregate actual cluster radical.**  For every integer
   window $D=o(M)$, evaluations of the actual collision polynomial at
   $\pm2d$, $1\le d\le D$, give a single radical
   $\mathcal C_{M,D}$ whose prime divisors are exactly the collision primes
   having another collision prime within $D$ row steps.

2. **PROVED — cluster-plus-isolated master inequality.**  If
   $D\sim c\log M$, then
   

$$
\limsup {W(M)\over6M}
     \le
     \limsup {\log\mathcal C_{M,D}\over6M}+{1\over72c}.
                                                               \tag{1.2}
$$


   Thus a strict saving below $1/36$ follows as soon as
   

$$
\log\mathcal C_{M,D}
      \le\left({2c-1\over12c}-\varepsilon\right)M       \tag{1.3}
$$


   for one $c>1/2$ and one $\varepsilon>0$.

3. **PROVED — shifted-norm height is information-neutral at logarithmic
   scale.**  Uniformly for $1\le d\le c\log M$, the two shifted norms
   differ multiplicatively from the collision radical by at most
   

$$
\exp(c/4+o(1)).                \tag{1.4}
$$


   Their logarithmic heights therefore differ from $W(M)$ by only
   $O_c(1)$, not by a positive multiple of $M$.  The ordinary bound
   $\gcd(A,B)\le\min(|A|,|B|)$, even after multiplying all logarithmically
   many shifts, cannot prove (1.3).

4. **PROVED — resultant sign and generic height do not repair this.**  The
   shifted resultant has an exact discriminant-type product.  Its sign is
   the parity of the already-unknown root gaps crossing $2d$, and its
   natural nonzero height is superlinear.  A sign argument is therefore
   circular and an integer-height upper bound gives no nonvanishing.

This is a scoped Closer theorem.  It closes the proposed *generic shifted-
norm/resultant height or sign* route at logarithmic scale, while preserving
the possibility of a special actual factor-localization, monodromy, or
average-gcd theorem.  It proves no strict bound on $\mathcal C_{M,D}$, so



$$
\boxed{\text{new booking}=0,\qquad
        \text{new whole-cell capacity reduction}=0,\qquad
        \text{retained ceiling}=1/36.}                  \tag{1.5}
$$



## 2. Exact actual-family setup

Retain Item 391's notation



$$
L_M={4M+3\over3},\qquad U_M={3M-1\over2},
 \qquad U_M-L_M={M-9\over6},                            \tag{2.1}
$$





$$
F_M(X)=\prod_{p\in\mathcal Z_M}(X-p),qquad
 R_M=R_{H\mathscr T}(M)=\prod_{p\in\mathcal Z_M}p,
 \qquad n_M=|\mathcal Z_M|.                             \tag{2.2}
$$



The set $\mathcal Z_M$ is Item 363's actual joint-gate set.  No ambient
selector replaces it.  Its roots have the exact tied rows



$$
h_p=3M-2p,qquad s_p={3p-4M-1\over2},                  \tag{2.3}
$$



and difference $2d$ is row offset $d$.

For $2d<L_M$ and $U_M+2d<2L_M$, Item 391 proved



$$
E^-_{M,d}:=\gcd\bigl(R_M,(-1)^{n_M}F_M(2d)\bigr)
 =\prod_{\substack{p\in\mathcal Z_M\\p+2d\in\mathcal Z_M}}p, \tag{2.4}
$$





$$
E^+_{M,d}:=\gcd\bigl(R_M,(-1)^{n_M}F_M(-2d)\bigr)
 =\prod_{\substack{p\in\mathcal Z_M\\p-2d\in\mathcal Z_M}}p. \tag{2.5}
$$



Both size conditions hold uniformly for $d=O(\log M)$, and more generally
for every $d=o(M)$ in a fixed sufficiently small linear range.

## 3. Exact paired factorization of the shifted resultant

Put



$$
\Delta_{M,d}=\operatorname {Res}_X
       \bigl(F_M(X),F_M(X+2d)\bigr).                   \tag{3.1}
$$



Pair the factors indexed by $(p,q)$ and $(q,p)$, retaining the diagonal
factor $2d$.  This gives the all-$M$ identity



$$
\boxed{
 \Delta_{M,d}=(2d)^{n_M}
  \prod_{\substack{p,q\in\mathcal Z_M\\p<q}}
       \bigl((2d)^2-(q-p)^2\bigr).}                    \tag{3.2}
$$



It recovers the exact zero criterion



$$
\Delta_{M,d}=0
 \iff \exists p:\ p,p+2d\in\mathcal Z_M.             \tag{3.3}
$$



When $\Delta_{M,d}\ne0$, (3.2) also gives



$$
\operatorname {sgn}\Delta_{M,d}
 =(-1)^{A_{M,d}},
 \qquad
 A_{M,d}=\#\{p<q:q-p>2d\}.                             \tag{3.4}
$$



Thus the sign is not fixed by the tied interval or the degree.  Computing
it requires knowing on which side of $2d$ every actual root gap lies;
equality is precisely the desired nonvanishing question.  Equation (3.4)
therefore makes a root-gap sign argument circular rather than proving
(3.3) impossible.

If the resultant is nonzero, (2.1) and (3.2) give the generic upper bound



$$
\log|\Delta_{M,d}|
 \le n_M\log(2d)+n_M(n_M-1)\log(U_M-L_M+2d).           \tag{3.5}
$$



The prime number theorem on the tied interval gives



$$
n_M\le|\mathcal P_M|
 ={M\over6\log M}+o\left({M\over\log M}\right).       \tag{3.6}
$$



At $d=O(\log M)$, the right side of (3.5) can be
$O(M^2/\log M)$.  The integer lower bound for a nonzero resultant is only
$|\Delta|\ge1$.  A superlinear upper height cannot exclude zero, and no
$<1$ estimate is available from (3.2).

## 4. One exact radical for the entire logarithmic window

For an integer $D$ satisfying the size hypotheses in Section 2, define



$$
\boxed{
 \mathcal C_{M,D}=\operatorname {rad}\!\left(
   \prod_{d=1}^{D}E^-_{M,d}E^+_{M,d}\right).}           \tag{4.1}
$$



Equations (2.4)--(2.5) prove the exact support identity



$$
p\mid\mathcal C_{M,D}
 \iff
 p\in\mathcal Z_M\text{ and }
 \exists q\in\mathcal Z_M\setminus\{p\}:|p-q|\le2D. \tag{4.2}
$$



Thus $\mathcal C_{M,D}$ is not a union bound and does not count an endpoint
once for every partner.  It is the squarefree radical of all and only the
actual clustered endpoints.

Let



$$
\mathcal I_{M,D}=R_M/\mathcal C_{M,D}.                 \tag{4.3}
$$



The primes dividing $\mathcal I_{M,D}$ have mutual distance greater than
$2D$.  Elementary packing in the exact interval (2.1) gives



$$
\omega(\mathcal I_{M,D})
 \le1+\left\lfloor{M-9\over12D}\right\rfloor,          \tag{4.4}
$$



and hence



$$
\boxed{
 W(M)=\log\mathcal C_{M,D}+\log\mathcal I_{M,D}
 \le\log\mathcal C_{M,D}
   +\left(1+{M-9\over12D}\right)\log U_M.}             \tag{4.5}
$$



This is an unconditional actual-family inequality.  It isolates the exact
arithmetic quantity whose logarithmic-scale control would reduce capacity.

## 5. Sharp paired-mass threshold at $D\sim c\log M$

Take $D\sim c\log M$ with $c>0$.  Divide (4.5) by $6M$:



$$
\boxed{
 \limsup {W(M)\over6M}
 \le
 \limsup {\log\mathcal C_{M,D}\over6M}
 +{1\over72c}.}                                        \tag{5.1}
$$



The raw ceiling is $1/36$.  Consequently a sufficient strict
factor-localization theorem is



$$
\boxed{
 \log\mathcal C_{M,D}
 \le\left({2c-1\over12c}-\varepsilon\right)M,
 \qquad c>{1\over2},\quad\varepsilon>0.}               \tag{5.2}
$$



Indeed, the coefficient available to the cluster radical is exactly



$$
{1\over6}-{1\over12c}={2c-1\over12c}.                 \tag{5.3}
$$



For example, at $c=1$, it is enough to prove



$$
\log\mathcal C_{M,\lfloor\log M\rfloor}
 \le(1/12-\varepsilon)M.                               \tag{5.4}
$$



For a zero-rate theorem, it is enough to take
$D=c(M)\log M=o(M)$, with $c(M)\to\infty$, and prove



$$
\log\mathcal C_{M,D}=o(M).                            \tag{5.5}
$$



Equations (5.2) and (5.5) are sufficient targets, not established bounds.

## 6. The logarithmic shifted norms have the same height as the target

Define the positive shifted norms



$$
\mathcal N^-_{M,d}=(-1)^{n_M}F_M(2d)
   =\prod_{p\in\mathcal Z_M}(p-2d),
 \qquad
 \mathcal N^+_{M,d}=(-1)^{n_M}F_M(-2d)
   =\prod_{p\in\mathcal Z_M}(p+2d).                    \tag{6.1}
$$



For $2d<L_M$, put $x_p=2d/p\in(0,1)$.  The elementary inequalities



$$
0\le-\log(1-x)\le{x\over1-x},
 \qquad 0\le\log(1+x)\le x                            \tag{6.2}
$$



give



$$
0\le\log R_M-\log\mathcal N^-_{M,d}
 \le {2d\,n_M\over L_M-2d},                            \tag{6.3}
$$





$$
0\le\log\mathcal N^+_{M,d}-\log R_M
 \le {2d\,n_M\over L_M}.                              \tag{6.4}
$$



Using (3.6), $L_M=(4/3+o(1))M$, and
$d\le c\log M$, both right sides are at most



$$
{2c\log M\over(4/3+o(1))M}
 \left({M\over6\log M}+o\left({M\over\log M}\right)\right)
 ={c\over4}+o(1).                                      \tag{6.5}
$$



Therefore, uniformly throughout the full capacity-relevant window,



$$
\boxed{
 e^{-c/4-o(1)}R_M
 \le\mathcal N^-_{M,d}\le R_M
 \le\mathcal N^+_{M,d}
 \le e^{c/4+o(1)}R_M.}                                 \tag{6.6}
$$



This is the exact logarithmic-scale height obstruction.  The norms do not
land in integers of sublinear logarithmic height.  They are constant-factor
perturbations of the unknown radical itself.

## 7. Scoped no-go for ordinary height, sign, and unlocalized products

From (2.4)--(2.5) and the ordinary gcd inequality,



$$
\log E^-_{M,d}\le\min(\log R_M,\log\mathcal N^-_{M,d}),
 \qquad
 \log E^+_{M,d}\le\min(\log R_M,\log\mathcal N^+_{M,d}). \tag{7.1}
$$



Equations (6.3)--(6.6) show that (7.1) gives at best



$$
\log E^\pm_{M,d}\le W(M)+O_c(1).                    \tag{7.2}
$$



After normalization by $6M$, this is the original ceiling.  Multiplying
the bounds for $D\asymp\log M$ shifts gives $O(DW)$, which is worse;
taking the radical only returns the tautology



$$
\mathcal C_{M,D}\mid R_M.                             \tag{7.3}
$$



Likewise, the sign formula (3.4) depends on the unknown gap pattern, and the
resultant height (3.5) is far above the integer nonzero threshold.  Hence
the following method class is closed:

> Start only from the actual polynomial $F_M$, use the identities at
> $\pm2d$ or the shifted resultant, and bound gcds solely by ordinary
> integer height, resultant sign, or an unlocalized product over shifts.

Every member of that class retains



$$
\log\mathcal C_{M,D}\le W(M)\le {M\over6}+o(M),        \tag{7.4}
$$



so its best whole-cell normalized ceiling remains $1/36$.

The scope is important.  This does **not** rule out:

1. a special factorization of $\mathcal N^\pm_{M,d}$ tied to the actual
   Hasse--transverse moments;
2. a theorem localizing the candidate-prime part of those norms into an
   $\exp((1/12-\varepsilon)M)$-sized carrier at $c=1$;
3. an average-gcd theorem proving (5.2);
4. a compatible-system or monodromy theorem controlling the joint zeros;
5. direct pair-freeness by arithmetic information absent from $F_M$'s
   generic root product.

## 8. Admission target for the next logarithmic-scale attempt

A future factor-localization candidate should be tested directly against
(5.2).  For $D\sim c\log M$, it must prove



$$
\limsup {1\over M}\log\mathcal C_{M,D}
 <{2c-1\over12c}.                                      \tag{8.1}
$$



An $O(M)$ bound with an unspecified or larger constant is not enough.
At $c=1$, the required strict coefficient is below $1/12$.  An
$o(M)$ theorem is stronger than necessary for a strict saving, but is the
right target if this branch is intended to close the cell.

Item 391's Selberg theorem gives only a sublogarithmic zero-rate result.  At
$D\asymp\log M$, its ambient pair upper bound is $O(M)$ with a constant
too large to improve the raw $M/6$ ceiling.  Item 395 identifies the
missing input precisely as a *gate-specific* bound for (4.1), not a generic
prime-pair count.

## 9. Deterministic replay and finite-data policy

The standard-library certificate pins all Item 391 artifacts and verifies,
on four predeclared root sets inside the actual candidate intervals at
$M=180,300$:

1. the direct and paired forms of the resultant (3.2);
2. its exact zero and sign rules;
3. both shifted norm/gcd endpoint radicals;
4. the aggregate cluster radical and the factorization
   $R_M=\mathcal C_{M,D}\mathcal I_{M,D}$;
5. isolation and the exact packing bound; and
6. the rational upper-bound parameters in (6.3)--(6.4).

These root sets are algebraic controls only.  They are not claimed to be
actual collision sets.  No actual gate scan, zero census, optimization, or
finite-to-infinite inference is included.  The all-family proofs are
Sections 3--7.

From the archive root run

```text
python work/item395_j1_logscale_cluster_radical_height_obstruction_certificate.py \
  --output work/item395_j1_logscale_cluster_radical_height_obstruction_certificate_replay.json
```

The replay must be byte-identical to the shipped certificate.

## 10. Strict decision and ledger

### PROVED

- the exact paired resultant factorization and sign formula;
- the exact logarithmic-window cluster radical;
- the cluster-plus-isolated master inequality (4.5);
- the sharp strict-saving threshold (5.2);
- the uniform constant-factor norm comparison (6.6);
- the scoped ordinary-height/resultant-sign/unlocalized-product no-go;
- zero booking and retention of the $1/36$ ceiling.

### CONDITIONAL TARGETS ONLY

- any bound of the form (5.2) or (5.5);
- any actual logarithmic pair-freeness theorem;
- any strict whole-cell capacity reduction.

### DECLARED EXACT CONTROLS ONLY

- four abstract root sets at $M=180,300$;
- no collision scan and no finite density inference.

### OPEN

- gate-specific factor localization for $\mathcal C_{M,D}$;
- a logarithmic-window weighted zero-density theorem;
- $W(M)=o(M)$, any new Route-1 booking, and every conclusion about
  $e+\pi$.



$$
\boxed{
 \text{new proved linear log rate}=0,\quad
 \text{new booked mass}=0,\quad
 \text{new whole-cell capacity reduction}=0.}          \tag{10.1}
$$


