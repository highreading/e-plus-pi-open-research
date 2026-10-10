> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The lifted mixed-cubic endpoint digit: an exact Hasse-band formula

Date: 2026-08-28

## 1. Verdict

Let



$$
N=6m,\qquad K_s=4m+1+s,\qquad
 \omega_s={u^N\over Q^{K_s}}\,dx,\qquad
 u=x(1-x),\quad Q=(1+x)(1+x^2),
$$



and write



$$
H_s=R_s+{L_s\over4}\log2+{E_s\over8}\pi,
 \qquad A_m=L_1R_0-L_0R_1.
$$



For a forced item-149 or item-151 prime $p<2m$, put



$$
q=p^e=\max\{p^a:p^a\le4m+1\},\qquad
 \delta={\bf1}_{p\in\mathcal P_m},\qquad D=1+\delta.
$$



**PROVED.**  The digit



$$
\eta_{m,p}\equiv {qA_m\over p^D}\pmod p
$$



has the explicit finite Hasse-derivative formula (4.2) below.  In the
non-rank-zero branch it is a genuine congruence modulo $p^2$, and it has
exactly two pole-index bands: $q$ and $q/p$.  In the already-divided
rank-zero branch the required precision is $p^3$, with a possible third
band $q/p^2$.  This is integral lift information, not another
characteristic-$p$ Cartier restatement.

**PROVED obstruction.**  Literal truncation to the top $q$-band can give
the wrong value of $\eta_{m,p}$.  At the exact actual-coordinate row
$(m,p)=(6,7)$, the
top-band formula gives $3$, whereas the complete two-band formula and the
frozen coordinate both give $4\pmod 7$.  Thus any proposed lift that
only refines the $e$-fold Cartier image and simply discards the
$q/p$-band is false.  This example does not exclude a special identity
that recovers lower bands from top data plus additional actual-family input.

**EXPERIMENTAL (exact finite audit only).**  A standard-library replay checks
all 94 item-149 rows and 24 additional item-151 determinant-zero rows with
$m\le30$.  All 118 Hasse digits agree with the frozen exact coordinates.
Deleting the lower band changes 64 of the 118 digits.  There are 45 zeros of
$\eta$ in this window.  These counts imply no density or asymptotic mass.
The $m\le30$ rows exercise only $h=0,1$; an independent exact spot check
of the possible third band at $(m,p)=(46,11)$ also agrees, while uniform
validity of that branch rests on the proof.

**OPEN.**  Formula (4.2) does not prove that its determinant vanishes on a
family of positive logarithmic mass.  That remains the precise arithmetic
target needed to improve the item-149 content rate.

## 2. Local Hasse coefficients

Let



$$
\mathcal A=\{-1,i,-i\}.
$$



For $\alpha\in\mathcal A$, write



$$
Q(x)=(x-\alpha)Q_\alpha(x)
$$



in the étale quadratic algebra $\mathbb Z_{(p)}[i]$, and define



$$
C_{s,\alpha}(r)
 =[t^r]\,{u(\alpha+t)^N\over Q_\alpha(\alpha+t)^{K_s}}
 ={1\over r!}{d^r\over dt^r}
 \left.{u(\alpha+t)^N\over Q_\alpha(\alpha+t)^{K_s}}
 \right|_{t=0}.                                      \tag{2.1}
$$



The coefficient-extraction definition in (2.1), rather than the displayed
ordinary-derivative notation, is valid integrally even when $r!$ is not a
unit.  These are Hasse derivatives.  Everything is completely explicit:



$$
\begin{array}{c|c|c}
\alpha&u(\alpha+t)&Q_\alpha(\alpha+t)\\ \hline
-1&-2+3t-t^2&2-2t+t^2\\
i&1+i+(1-2i)t-t^2&-2+2i+(1+3i)t+t^2\\
-i&\overline{u(i+t)}&\overline{Q_i(i+t)}.
\end{array}                                           \tag{2.2}
$$



Because $\operatorname {disc}Q=-16$, all constant terms in (2.2) are
$p$-adic units for odd $p$.  Thus (2.1) can be evaluated modulo any
power of $p$ by finite truncated power-series inversion.

The partial fractions are exactly



$$
{u^N\over Q^{K_s}}
 =\sum_{\alpha\in\mathcal A}\sum_{j=1}^{K_s}
 {C_{s,\alpha}(K_s-j)\over(x-\alpha)^j}.              \tag{2.3}
$$



There is no polynomial quotient: the numerator degree is $12m$, whereas
the denominator degrees are $12m+3$ and $12m+6$.

## 3. Exact endpoint and logarithmic coordinates

Put



$$
H_\alpha(n)=(-\alpha)^{-n}-(1-\alpha)^{-n}.            \tag{3.1}
$$



Integrating every term of (2.3) from $0$ to $1$ gives



$$
R_s=\sum_{\alpha\in\mathcal A}\sum_{n=1}^{K_s-1}
 {C_{s,\alpha}(K_s-1-n)\over n}H_\alpha(n).             \tag{3.2}
$$



The simple-pole logarithms are



$$
\int_0^1{dx\over x+1}=\log2,
$$





$$
\int_0^1{dx\over x-i}={1\over2}\log2+{i\pi\over4},
 \qquad
 \int_0^1{dx\over x+i}={1\over2}\log2-{i\pi\over4}.
$$



Consequently



$$
\boxed{
 L_s=4C_{s,-1}(K_s-1)
     +2C_{s,i}(K_s-1)+2C_{s,-i}(K_s-1).}               \tag{3.3}
$$



Equations (3.2)--(3.3) are exact over $\mathbb Q(i)$; conjugate terms make
the displayed values rational.

## 4. The lifted Hasse-band theorem

Since $K_s-1\le4m+1<pq$, every integer $1\le n\le K_s-1$ has
$v_p(n)\le e$.  For $0\le h\le\min(e,D)$, define



$$
\begin{split}
 \mathcal B_{s,h}:={}&
 \sum_{\alpha\in\mathcal A}
 \sum_{\substack{k\ge1,\ p\nmid k\\p^{e-h}k\le K_s-1}}
 {C_{s,\alpha}(K_s-1-p^{e-h}k)\over k}\\
 &\qquad\qquad\times
 H_\alpha(p^{e-h}k)
 \pmod {p^{D+1}}.                                      \tag{4.1}
\end{split}
$$



Then



$$
\boxed{
 \eta_{m,p}\equiv p^{-D}
 \left[
 L_1\sum_{h=0}^{\min(e,D)}p^h\mathcal B_{0,h}
 -L_0\sum_{h=0}^{\min(e,D)}p^h\mathcal B_{1,h}
 \right]\pmod p.}                                    \tag{4.2}
$$



The bracket in (4.2) is evaluated modulo $p^{D+1}$.  Its divisibility by
$p^D$ is the item-149 or item-151 divisor theorem, so the divided residue
is well-defined.  More fundamentally, (3.2) gives the lifted endpoint
identity



$$
\boxed{
 qR_s\equiv\sum_{h=0}^{\min(e,D)}p^h\mathcal B_{s,h}
 \pmod {p^{D+1}}.}                                    \tag{4.3}
$$



### Proof

In (3.2), write $n=p^v k$ with $p\nmid k$.  Because $v\le e$,



$$
{q\over n}={p^{e-v}\over k}.
$$



Set $h=e-v$.  Terms with $h\ge D+1$ vanish modulo $p^{D+1}$; grouping
the remaining terms gives (4.3) exactly.  Substitute (4.3) and (3.3) into



$$
qA_m=L_1(qR_0)-L_0(qR_1)
$$



and divide by the already-proved $p^D$.  This proves (4.2).  No finite
calculation, Frobenius inversion, or unproved identification with an ambient
Hasse--Witt matrix is used.  $\square$

For $\delta=0$, $D=1$, so (4.3) is the promised genuine modulo-$p^2$
formula



$$
qR_s\equiv\mathcal B_{s,0}+p\mathcal B_{s,1}\pmod {p^2}. \tag{4.4}
$$



For $\delta=1$, the digit lies one level deeper and (4.3) must be read
modulo $p^3$:



$$
qR_s\equiv\mathcal B_{s,0}+p\mathcal B_{s,1}
 +{\bf1}_{e\ge2}p^2\mathcal B_{s,2}\pmod {p^3}.         \tag{4.5}
$$



## 5. A sharp lower-band counterexample

At $(m,p)=(6,7)$, one has $e=1,\delta=0$.  Working modulo $49$, the
exact Hasse computation gives



$$
(L_0,L_1)=(14,5),
$$





$$
(\mathcal B_{0,0},\mathcal B_{1,0})=(42,10),
 \qquad
 (7\mathcal B_{0,1},7\mathcal B_{1,1})=(21,28).
$$



Hence the top band alone gives



$$
7^{-1}(5\cdot42-14\cdot10)\equiv3\pmod7,
$$



whereas the full lift gives



$$
7^{-1}(5\cdot14-14\cdot38)\equiv4\pmod7.
$$



The frozen actual coordinate gives the same value $4$.  Thus the
$q/p$-band is arithmetically real and cannot simply be omitted from the
lifted endpoint identity.

## 6. Replay and exact scope

Run

```text
python scripts/lifted_endpoint_hasse_certificate.py \
  --max-m 30 \
  --output results/lifted_endpoint_hasse_certificate_m30.json
```

The script uses only the Python standard library.  It constructs the Hasse
coefficients in $\mathbb Z/p^{2+\delta}\mathbb Z[i]$, evaluates
(3.3), (4.1), and (4.2), and compares with the independently frozen exact
$U_m$ normalization.  The pinned inputs are the item-140 actual-coordinate
JSON and the item-151 rank-two JSON.

The replay proves exact agreement for the listed 118 finite rows only.  The
uniform result is the termwise proof of (4.3); the replay audits signs,
branches, normalization, and the nontrivial lower-band contribution.

## 7. Remaining target

Formula (4.2) replaces the vague request for a Witt/Dwork lift by a concrete
finite determinant of Hasse coefficients.  A positive result now has to
prove cancellation of that determinant modulo $p^{D+1}$ on a prime family
of positive weighted mass.  Conversely, a nonvanishing theorem for (4.2)
would rule out higher content on the corresponding family.  Neither type of
uniform family theorem is currently proved.
