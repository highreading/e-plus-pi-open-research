> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 230 — phase-antiperiodic affine closure for the (j=1) cell

Date: 2026-08-31

## 1. Scope and verdict

Retain the complete Item 223 parameterization



$$
p=2r+6s+3,\qquad r=2h,\qquad h,s\geq1,                         \tag{1.1}
$$



and Item 228's regularized boundary moments for



$$
W=(1-z)^r(1+z^2)^{2s-1},\qquad
 \epsilon=(-1)^{(p-1)/2}=(-1)^{s+1}.                           \tag{1.2}
$$



This item continues the order-three Pearson recurrence through every
successive Frobenius phase.  Its principal result is an exact structural
reformulation, not an all-prime noncollision theorem.

**PROVED — fixed one-phase transfer.**  If (Y_a) is the three-entry
regularized state at the (ap) terminal, there are a fixed matrix
(M=M_{p,r,s}) and column (b=b_{p,r,s}), independent of (a), such that



$$
Y_{a+1}=M Y_a+b\ell_{ap-1}.                  \tag{1.3}
$$



The exact terminal multiplier is (ap), not merely (0\pmod p).  The
unreduced pole has residue (ell_{ap-1}/a) after multiplication by (p),
so the factor (a) cancels and the terminal source is exactly
(ell_{ap-1}).

**PROVED — antiperiod two, period four.**  Coefficient by coefficient,



$$
\widehat u_{t+2p}=-\widehat u_t,\qquad
             \widehat u_{t+4p}= \widehat u_t\pmod p.           \tag{1.4}
$$



The terminal weights have exact phase period four and phase antiperiod two.
After normalizing (Z_a=\epsilon Y_a), their cycle for (a=2,3,4,5) is



$$
(-4,2,4,-2).                      \tag{1.5}
$$



**PROVED — exact six-equation rank criterion.**  A collision supplies one
scalar (mu) that must solve six equations (c_i\mu=d_i): the lower
(p)-terminal, the (2p)- and (3p)-terminals, and the three coordinates
of the (2p)-antiperiod closure.  Formal solvability is equivalent to



$$
\operatorname {rank}[c\mid d]=\operatorname {rank}c=1,        \tag{1.6}
$$



or, equivalently, some (c_i\ne0) and all fifteen augmented minors
(c_i d_j-c_jd_i) vanish.  Every original collision must pass this test.
The first two old invariants occur literally among the minors: one is
(2\Theta), and another is (-\epsilon\Psi).

**PROVED — completeness on regular rows.**  If



$$
\mathfrak D_{p,r,s}=\det(I+M^2)\ne0,  \tag{1.7}
$$



formal solvability of the six equations is equivalent to the original
common-log collision.  On (mathfrak D=0) rows, the system remains
necessary, but sufficiency is not asserted.

**EXACT FINITE ONLY.**  Through (p\le601), all 2,435 actual rows have an
inconsistent six-equation system.  Exactly three rows have
(mathfrak D=0), and all three are nevertheless formally inconsistent.
Every one of the fifteen individual minors has zeros in this finite census,
so no individual minor has been promoted to a uniform unit theorem.

**OPEN.**  No all-prime augmented-rank inconsistency, classification of
(mathfrak D=0), or weighted zero-rate theorem is proved.  This item books
no new Route-1 rate and proves nothing about (e+\pi).

## 2. The regularized Pearson recurrence

Item 228 defines



$$
\widehat u_t=\widehat{\mathcal L}_\epsilon
              \bigl(z^{p+r+t}W\bigr),                         \tag{2.1}
$$



where monomials whose primitive denominator is divisible by (p) are
deleted.  Put



$$
\sigma=(1-z)(1+z^2),\qquad
 K_t=z^{p+r+t+1}\sigma W.                                    \tag{2.2}
$$



The exact coefficients are



$$
\begin{aligned}
A_t&=p+2r+4s+t+2,&B_t&=p+r+t+1,\\
C_t&=p+2r+t+2,&D_t&=p+r+4s+t+1,                              \tag{2.3}
\end{aligned}
$$



and the regularized recurrence is



$$
B_t\widehat u_t-C_t\widehat u_{t+1}
 +D_t\widehat u_{t+2}-A_t\widehat u_{t+3}
 =-\sum_{q\ge1}[z^{qp}]K_t\,\ell_{qp-1}\pmod p.              \tag{2.4}
$$



All signs in what follows come from (2.4); no sign is inferred from a
finite sample.

## 3. Every (ap) multiplicity and source

Set



$$
T=2s+1,\qquad t_a=T+(a-2)p\quad(a\ge2).                       \tag{3.1}
$$



Substituting (1.1) gives the exact integer identity



$$
A_{t_a}=ap.                       \tag{3.2}
$$



The degree of (sigma W) is (r+4s+1<p), and its leading coefficient is
(-1).  Hence at (t=t_a) the sole deleted derivative is its top monomial
at exponent (ap).  Formula (2.4) gives



$$
-(-1)\ell_{ap-1}=\ell_{ap-1}.              \tag{3.3}
$$



There is an independent unreduced check.  The leading monomial of (W) is
(z^{r+4s-2}), with coefficient (1), and the only pole in
(u_{t_a+3}) is therefore



$$
{\ell_{ap-1}\over ap}.                 \tag{3.4}
$$



Consequently



$$
p u_{t_a+3}\equiv{\ell_{ap-1}\over a},\qquad
 ap u_{t_a+3}\equiv\ell_{ap-1}\pmod p.                        \tag{3.5}
$$



Thus the phase multiplicity (a) is retained until it cancels.  Dropping it
before (3.5) would give the wrong source at every phase except (a=1).

For the boundary functional of Items 223 and 228,



$$
\begin{array}{c|rrrr}
a\bmod4&1&2&3&0\\ \hline
\ell_{ap-1}&-2\epsilon&-4\epsilon&2\epsilon&4\epsilon.
\end{array}                                                     \tag{3.6}
$$



No entry vanishes for an actual prime (p\ge13).

## 4. Construction of the one-phase map

Define the terminal state



$$
Y_a=(\widehat u_{t_a},\widehat u_{t_a+1},
                         \widehat u_{t_a+2})^t.                 \tag{4.1}
$$



For (1\le j\le p-1), the leading recurrence pivot after the (a)-th
terminal is



$$
A_{t_a+j}\equiv j\ne0\pmod p.           \tag{4.2}
$$



Since (deg(\sigma W)<p), the only deleted derivative in this open phase
has exponent (ap), and its coefficient depends only on (j), not on
(a).  Propagating the three input coordinates and one normalized forcing
column therefore defines a fixed (M) and (b) satisfying (1.3).

At (t=t_a), the value (widehat u_{t_a+3}) is free after terminal
compatibility is imposed.  Its homogeneous response (x_n), normalized by
(x_0=1), has generating polynomial exactly



$$
\sum_{n\ge0}x_nz^n=W(z).               \tag{4.3}
$$



This is Item 228's coefficient form of the Pearson identity.  Moreover,



$$
(p-3)-\deg W
 =p-3-(r+4s-2)=r+2s+2>0.                                    \tag{4.4}
$$



The next state uses free-mode coefficients (p-3,p-2,p-1), all beyond
the support in (4.3).  Hence the entire free column is identically zero.
No untracked resonance parameter is hidden in (1.3).

## 5. Coefficientwise phase antiperiodicity

Write (W=\sum_k w_kz^k).  Directly from the definition,



$$
\widehat u_t=
 \sum_{\substack{k\\p\nmid p+r+t+k+1}}
 w_k{\ell_{p+r+t+k}\over p+r+t+k+1}\pmod p.                   \tag{5.1}
$$



Replacing (t) by (t+2p) preserves the deleted-denominator condition and
every retained inverse modulo (p).  Since (2p\equiv2\pmod4) and
(ell_{n+2}=-\ell_n), it negates every retained summand.  Replacing (t)
by (t+4p) fixes every summand.  This proves (1.4) coefficient by
coefficient, including all deleted pole positions.

Normalize



$$
Z_a=\epsilon Y_a.                       \tag{5.2}
$$



Then (1.3), (3.6), and (1.4) become



$$
Z_{a+1}=MZ_a+bw_a,\qquad Z_{a+2}=-Z_a,                        \tag{5.3}
$$



with



$$
(w_2,w_3,w_4,w_5)=(-4,2,4,-2).              \tag{5.4}
$$



The entries in (5.4) are neither period one nor period two for (p\ge13),
but satisfy (w_{a+2}=-w_a) and (w_{a+4}=w_a).  Thus the terminal source
has exact phase period four.

## 6. The six scalar equations

Let (v) be the terminal state obtained by propagating the Item 223 common
line



$$
(u_0,u_1,u_2)=\lambda(1,1,-1)          \tag{6.1}
$$



to (t=T).  Put



$$
a=(r+T+1,-(2r+T+2),r+4s+T+1).                               \tag{6.2}
$$



Then



$$
av=\Delta_+.                           \tag{6.3}
$$



Write



$$
\mu=\epsilon\lambda,\qquad Z_2=\mu v.       \tag{6.4}
$$



The lower source of Item 223 and the first two upper terminals give



$$
\begin{aligned}
 \Delta_-\mu&=-2,\\
 \Delta_+\mu&=-4,\\
 a(Mv)\mu&=2+4ab.                                             \tag{6.5}
\end{aligned}
$$



Indeed, (Z_3=M(\mu v)-4b), so the last equation in (6.5) is exactly the
(3p) terminal equation (aZ_3=2).

The antiperiod condition (Z_4=-Z_2) gives



$$
(I+M^2)v\,\mu=4Mb-2b.                      \tag{6.6}
$$



Equations (6.5) and the three coordinates of (6.6) are the six rows



$$
c_i\mu=d_i.                       \tag{6.7}
$$



Because the first right side is (-2\ne0), an all-zero coefficient column
is inconsistent.  Elementary one-variable linear algebra proves



$$
\boxed{\text{(6.7) is solvable}\iff
 \bigl(\exists i:c_i\ne0\bigr)\ \text{and}\
 c_id_j-c_jd_i=0\ \text{for all }i<j.}                         \tag{6.8}
$$



There are fifteen minors in (6.8).  The first old transfer minor is



$$
\det\!\begin{pmatrix}\Delta_-&-2\\\Delta_+&-4\end{pmatrix}
 =2(\Delta_+-2\Delta_-)=2\Theta.                              \tag{6.9}
$$



The minor from the (2p)- and (3p)-terminal rows is



$$
-\epsilon\Psi,                    \tag{6.10}
$$



where (Psi) is exactly Item 228's second Frobenius invariant.  Thus
Item 230 retains both corrected earlier conditions and adds the three
antiperiod coordinates without replacing either one.

The relations (Z_4=-Z_2), (w_4=-w_2), and (5.3) also imply
(Z_5=-Z_3) and (Z_6=Z_2).  Hence the (4p) closure and the (4p,5p)
terminal equations follow from (6.5)--(6.6); they are not missing equations.

## 7. Why (det(I+M^2)\ne0) gives completeness

The actual regularized coefficient-sum state satisfies (6.6) by Section 5.
If



$$
\mathfrak D=\det(I+M^2)\ne0,             \tag{7.1}
$$



then the affine antiperiod equation has a unique state (Z_2).  Therefore,
if a scalar (mu) makes (mu v) satisfy (6.6), it equals the actual
regularized state.

For (0\le t<T), both the forward pivots (A_t) and the backward
coefficients (B_t) are (p)-units.  The equality at (Y_2) consequently
propagates uniquely back to



$$
(u_0,u_1,u_2)=\lambda(1,1,-1).         \tag{7.2}
$$



By Item 223, (7.2) is equivalent to the original pair of common-log endpoint
conditions.  This proves, on every (mathfrak D\ne0) row,



$$
\boxed{\text{formal solvability of (6.7)}
        \iff\text{original common-log collision}.}             \tag{7.3}
$$



When (mathfrak D=0), uniqueness can fail.  The forward implication from
an original collision to (6.7) remains valid, but the reverse implication
is deliberately not claimed.

## 8. Direct replay and finite census

The direct identity replay covers all 184 actual rows with (p\le151).
For phases (a=2,3,4,5), it checks 736 terminal source rows, including:

* 2,944 unreduced rational moment evaluations;
* the exact multiplier (ap) before modular reduction;
* the residue (p u_{t_a+3}=\ell_{ap-1}/a);
* recovery of (ell_{ap-1}) after multiplication by (ap);
* 2,760 direct regularized coefficient sums;
* every one-phase transfer, every terminal equation, (2p)
  antiperiodicity, and (4p) periodicity;
* equality of the (2p/3p) augmented minor with
  (-\epsilon\Psi).

The source-row stream has SHA-256

`068b1788aa3da03e7432bc45ec59728144006ca80ee79986abddc09a3e8ea440`.

These computations replay the all-row identities proved in Sections 2--7;
the finite bound is not part of their proof.

Separately, the exact finite census through (p\le601) gives



$$
\begin{array}{l|r}
\text{actual rows}&2435\\
\mathfrak D\ne0&2432\\
\mathfrak D=0&3\\
\text{formally solvable six-equation rows}&0\\
\text{Item 223 transfer survivors}&11\\
\text{joint Item 223/228 survivors}&0\\
\text{direct common-gate zeros}&0.
\end{array}                                                     \tag{8.1}
$$



The three determinant-zero rows ((p,r,s)) are



$$
(349,2,57),\quad(457,128,33),\quad(577,86,67). \tag{8.2}
$$



Each row in (8.2) has augmented rank greater than coefficient rank.  Every
one of the fifteen individual minors in (6.8) vanishes on at least one row
of this census.  The complete row transcript has SHA-256

`be4b9b48cae43b2449bab7b9cf5499b8ac2d230e8004b0c0fe1bb333eddb618b`.

All statements in (8.1)--(8.2) are labeled **EXACT FINITE ONLY**.  They
prove no all-prime assertion, asymptotic density, or logarithmic rate.

## 9. Consequence and next obstruction

Item 230 converts the infinite succession of (j=1) Frobenius poles into
one fixed affine transfer and an exact antiperiodic fixed-point equation.
On (mathfrak D\ne0) rows, this is a complete reformulation of the original
gate, rather than merely another necessary scalar invariant.

The remaining all-prime obstruction is now sharply separated into two
questions:

1. prove augmented-rank inconsistency for all regular rows; and
2. classify, exclude, or prove zero weighted rate for the singular family
   (mathfrak D=0).

The finite zeros of every individual minor show that no unproved
single-minor unit shortcut is available from the present census.

Conditional exclusion of the entire (j=1) cell would remove (1/6) per
(m), but no all-prime or zero-rate theorem is established here.  Therefore



$$
\boxed{\text{new unconditional linear log rate}=0,\qquad
        \text{new divisibility exponent}=0.}                   \tag{9.1}
$$



## 10. Reproduction and labels

From the portable archive root, run

```text
python scripts/item230_j1_phase_closure_certificate.py \
  --output results/item230_j1_phase_closure_certificate.json
python scripts/item230_j1_phase_closure_certificate.py \
  --output results/item230_j1_phase_closure_certificate_replay.json
```

The checker uses only Python 3.11+ standard-library exact integer,
`Fraction`, polynomial, and finite-field arithmetic.  Its portable
dependencies are the frozen Item 218, 223, and 228 checkers.

**PROVED**

* the exact (ap) multiplicity and source (ell_{ap-1}) at every upper
  Frobenius phase;
* the fixed affine phase transfer and exact disappearance of each free
  column before the next terminal;
* coefficientwise (2p) antiperiodicity and (4p) periodicity;
* the six-equation augmented-rank necessary criterion;
* equivalence with the original common-log collision when
  (det(I+M^2)\ne0).

**EXACT FINITE**

* the direct source and coefficientwise replay through (p\le151);
* the determinant and augmented-rank census through (p\le601).

**OPEN**

* all-prime inconsistency of the six-equation system;
* classification or zero-rate control of (det(I+M^2)=0);
* any positive Route-1 rate, radical saving, or conclusion about
  (e+\pi).
