> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 415 — the marked selector and the fully Cartier-normalized large-prime ceiling

Date: 2026-09-01  
Status: **CANONICAL, ROOT-AUDITED, COMPONENT CEILING REDUCED, NO BOOKING**

## 1. Verdict and capacity first

Write the tied prime in the form requested by the current branch,



$$
p=6m+2d+1,
 \qquad q=p-6m=2d+1.
 \tag{1.1}
$$



The difficult cubic class is exactly



$$
q\equiv1\pmod6
 \quad\Longleftrightarrow\quad
 d=3h.
 \tag{1.2}
$$



In that class Item 412 identifies the actual, rather than symmetric Smith,
branch by



$$
X_p=16^h\,2^{(p-1)/3}\pmod p.
 \tag{1.3}
$$



This item converts that marked incidence back into a prime-independent pair
of exact residue integers and then proves a new global **capacity
consequence** by joining two canonical theorems that had not previously
been combined in the ledger.
Let the Item-390 integers be



$$
\lambda_{0,m}=[y^{4m}]
 \frac{(1-y)^{6m}(1+y)}{(1+y^2)^{4m+1}},
 \tag{1.4}
$$





$$
\lambda_{1,m}=[y^{4m+1}]
 \frac{(1-y)^{6m}(1+y)^4}{(1+y^2)^{4m+2}}.
 \tag{1.5}
$$



These coordinates are integers, not merely rational values: for every
positive integer (k),



$$
(1+y^2)^{-k}
 =\sum_{j\ge0}(-1)^j\binom{k+j-1}{j}y^{2j}
 \in\mathbb Z[[y]],
$$



and the two numerator factors have integral coefficients.

For completeness, canonical Item 200 defines, for a positive modulus
(q),



$$
d_q(N,K)=
 \begin{cases}
 2r,&K\equiv0\pmod q,\\
 2r+3(q-t),&K\equiv t\pmod q,\quad1\le t<q,
 \end{cases}
 \quad r\equiv N\pmod q,\ 0\le r<q,
$$



and



$$
\mathcal P_m=\{\ell\text{ odd prime}:
 d_\ell(6m,4m+1)\le\ell-2,
 \ d_\ell(6m,4m+2)\le\ell-2\}.
$$



Canonical Item 200 already proves that the full rank-zero Cartier product



$$
F_m=\prod_{\ell\in\mathcal P_m}\ell=G_m
 \tag{1.6}
$$



divides both integers in (1.4)--(1.5), and that



$$
\log F_m=\mathfrak C_Fm+o(m),
 \qquad
 \mathfrak C_F=-4\log2+\frac{\pi}{\sqrt3}+3\log3
 =2.3370475079987656871\ldots .
 \tag{1.7}
$$



Its transparent (j=0) subproduct is



$$
\boxed{
 D_m=\prod_{\substack{4m+1<\ell<6m\\
                       \ell\text{ prime}}}\ell .}
 \tag{1.8}
$$



Item 200 proves (D_m\mid F_m\mid\lambda_{0,m},\lambda_{1,m}).
Section 4 below gives a short independent truncated-Frobenius proof of the
(D_m)-part, both to expose the mechanism and to make the new proof chain
checkable.  The divisor theorem itself is inherited and is not rebooked as
new Item-415 credit.

The factors of (F_m) are compulsory factors of the **auxiliary residue
carrier**.  They are not asserted to divide the normalized content: every
prime in (F_m) is at most (6m), precisely outside the all-depth range
of Item 390.  Their role
is to remove irrelevant height from the carrier for primes (p>6m).

Put



$$
\boxed{\mu_{s,m}=\lambda_{s,m}/F_m\in\mathbb Z.}
 \tag{1.9}
$$



Because every target prime satisfies (p>6m), division by (F_m) preserves
all target valuations.  Item 390 therefore sharpens to



$$
\boxed{
 v_p(c_m)=\min\{v_p(\mu_{0,m}),v_p(\mu_{1,m})\}
 \quad(p>6m).}
 \tag{1.10}
$$



Combining (1.7), (1.9)--(1.10) with Item 390's fixed-circle bounds proves the new
component ceiling



$$
\boxed{
 \limsup_{m\to\infty}\frac{\log c_m^>}{6m}
 \le \frac{\log136-\mathfrak C_F}{6}
 =0.4292678962895477202317242499\ldots .}
 \tag{1.11}
$$



The previous ceiling was ((\log136)/6).  Thus the rigorously proved
strictly-large component ceiling decreases by



$$
\boxed{
 \frac{\mathfrak C_F}{6}
 =0.3895079179997942811851475804\ldots .}              \tag{1.12}
$$



The interval subproduct (D_m) alone accounts for exactly (1/3) of
this improvement; Item 200's remaining (j\ge1) forced rows account for
the further
(0.0561745846664609478518142471\ldots).

This is positive linear-exponent progress of the **Closer** kind.  It is
not a positive divisor booking and it does not prove weighted zero density.
By Item 393, an upper bound for the disjoint large-prime factor cannot be
subtracted from the global upper bound for the whole content.  Hence the
booked rate, the global total-content ceiling, and the frozen deficit remain
unchanged.

## 2. Exact tied congruence and selector bookkeeping

Under (1.2), one has



$$
q=6h+1,\qquad n=q-1=6h,\qquad p=6(m+h)+1.
 \tag{2.1}
$$



Consequently



$$
n\bmod4=2(h\bmod2),
 \tag{2.2}
$$



and



$$
p\bmod18=
 \begin{cases}
 1,&m+h\equiv0\pmod3,\\
 7,&m+h\equiv1\pmod3,\\
 13,&m+h\equiv2\pmod3.
 \end{cases}                                             \tag{2.3}
$$



Item 412's notation has



$$
x_q=4^{(q-1)/3}=4^{2h}=16^h.
$$



The exponent identity



$$
2m+q-1=\frac{p-1}{3}+\frac{2(q-1)}3
$$



gives (1.3).  Thus the selected root lies in the rational linear factor
exactly when (2^{(p-1)/3}=1), equivalently when (2) is a cube modulo
(p).  For (p\equiv7,13\pmod {18}), Item 412's ordinary cubic-residue
tests recover the marked Eisenstein label; for (p\equiv1\pmod {18}), the
direct Frobenius equality remains necessary.

Equations (2.1)--(2.3) are the exact congruence-class conditions in the tied
family.  They do not imply that carrier divisors are equidistributed among
the three labels.

## 3. PROVED — the marked residual pair is phase independent

Retain Item 411's marked residuals



$$
\epsilon_0=s-X_pu,
 \qquad
 \epsilon_1=r-X_p(u+v).
 \tag{3.1}
$$



Its exact generator transport is



$$
\lambda_0=-(\epsilon_0+\epsilon_1),
 \tag{3.2}
$$





$$
(2n-1)\lambda_1
 =-(5n-7)\epsilon_0-(5n-1)\epsilon_1.
 \tag{3.3}
$$



At a tied prime (n=p-6m-1\equiv-6m-1\pmod p).  Solving
(3.2)--(3.3) gives



$$
2\epsilon_0\equiv
 2(5m+1)\lambda_{0,m}-(4m+1)\lambda_{1,m}\pmod p,
 \tag{3.4}
$$





$$
2\epsilon_1\equiv
 (4m+1)\lambda_{1,m}-2(5m+2)\lambda_{0,m}\pmod p.
 \tag{3.5}
$$



Define the integral representatives



$$
\mathcal A_m=2(5m+1)\lambda_{0,m}-(4m+1)\lambda_{1,m},
 \tag{3.6}
$$





$$
\mathcal B_m=(4m+1)\lambda_{1,m}-2(5m+2)\lambda_{0,m}.
 \tag{3.7}
$$



The change matrix from ((\lambda_0,\lambda_1)) to
((\mathcal A,\mathcal B)) has determinant



$$
-2(4m+1).                                             \tag{3.8}
$$



It is a unit at every (p>6m).  Hence, including all valuation depths,



$$
\min\{v_p(\mathcal A_m),v_p(\mathcal B_m)\}
 =\min\{v_p(\lambda_{0,m}),v_p(\lambda_{1,m})\}.
 \tag{3.9}
$$



For (p\equiv1\pmod6), equations (3.4)--(3.5) are exactly the Item-412
Frobenius-marked branch, not the union of its two twists.  Thus the marked
support set in the difficult class is



$$
\boxed{
 \{p>6m:p\equiv1\pmod6, p\mid\lambda_{0,m},\lambda_{1,m}\}.}
 \tag{3.10}
$$



The moving Eisenstein label is fully retained in the original residue pair;
passing to the symmetric Smith carrier is what forgets it.  Equations
(3.6)--(3.10) show that no separate branch-density assumption is needed to
obtain a deterministic height carrier.

## 4. INHERITED, independently rederived — the interval part of the Cartier strip

Fix a prime



$$
4m+1<\ell<6m
$$



and put



$$
a=6m-\ell,
 \qquad
 b=\ell-4m-1.
 \tag{4.1}
$$



Then (a>0), (b\ge2), and both target degrees (4m,4m+1) are below
(ell).  Work in the truncated ring



$$
\mathbb F_\ell[y]/(y^\ell).
$$



Frobenius gives



$$
(1-y)^{6m}=(1-y)^{a+\ell}\equiv(1-y)^a,
 \tag{4.2}
$$





$$
(1+y^2)^{-(4m+1)}
 =(1+y^2)^{b-\ell}\equiv(1+y^2)^b,
 \tag{4.3}
$$



and



$$
(1+y^2)^{-(4m+2)}
 \equiv(1+y^2)^{b-1}.                                  \tag{4.4}
$$



The polynomial replacing the kernel in (1.4) has degree



$$
a+1+2b=\ell-2m-1<4m,                                 \tag{4.5}
$$



so its coefficient of (y^{4m}) is zero.  The polynomial replacing the
kernel in (1.5) has degree



$$
a+4+2(b-1)=\ell-2m<4m+1,                             \tag{4.6}
$$



so its coefficient of (y^{4m+1}) is zero.  Therefore



$$
\lambda_{0,m}\equiv\lambda_{1,m}\equiv0\pmod\ell.
 \tag{4.7}
$$



Multiplying (4.7) over the distinct primes in (1.8) reproves



$$
D_m\mid\lambda_{0,m},\lambda_{1,m}.
 \tag{4.8}
$$



This is exactly canonical Item 200's (j=0) Cartier subproduct, not a new
divisor theorem.  Item 200's all-(j) argument proves the stronger
(F_m\mid\lambda_{0,m},\lambda_{1,m}) used in Section 5.

The strict lower endpoint in (1.8) is necessary.  If (4m+1) itself is
prime, the target (4m+1) is no longer below the characteristic and the
second truncation argument changes.  Omitting this single possible prime
costs only (O(\log m)=o(m)), so it has no effect on the interval rate.

## 5. PROVED — all-depth carrier and the new ceiling

For completeness, no prime (p>6m) belongs to (mathcal P_m): in that
range the two Item-200 defects are respectively



$$
d_p(6m,4m+1)=3p-3,
 \qquad
 d_p(6m,4m+2)=3p-6,
$$



and neither is at most (p-2).  Thus (p\nmid F_m).  Item 390 and (1.9)
therefore give



$$
\begin{aligned}
 v_p(c_m)
 &=\min\{v_p(\lambda_{0,m}),v_p(\lambda_{1,m})\}\\
 &=\min\{v_p(\mu_{0,m}),v_p(\mu_{1,m})\}.
\end{aligned}                                           \tag{5.1}
$$



Consequently



$$
c_m^>
 =\left(\gcd(|\mu_{0,m}|,|\mu_{1,m}|)\right)_{p>6m}.
 \tag{5.2}
$$



For all sufficiently large (m), Item 390 proves that the two residue
integers are not both zero and proves



$$
|\lambda_{0,m}|<3\cdot136^m,
 \qquad
 |\lambda_{1,m}|<21\cdot136^m.
 \tag{5.3}
$$



Thus



$$
c_m^><\frac{21\cdot136^m}{F_m}.                         \tag{5.4}
$$



Canonical Item 200 proves, by applying the prime number theorem to its
complete interval parametrization,



$$
\log F_m=\mathfrak C_Fm+o(m),
 \qquad
 \mathfrak C_F=-4\log2+\frac\pi{\sqrt3}+3\log3.
 \tag{5.5}
$$



Equations (5.4)--(5.5) prove (1.11).  The same theorem bounds the marked
(p\equiv1\pmod6) submass, but it is stronger: it controls both admissible
classes together and includes every (p)-adic depth.

## 6. What this does and does not say about weighted zero density

Define the difficult-class weighted mass



$$
\Theta_{1}^{>}(m)=
 \sum_{p>6m\atop p\equiv1\ (6)}
 \min\{v_p(\mu_{0,m}),v_p(\mu_{1,m})\}\log p.
 \tag{6.1}
$$



Then (5.2) gives the rigorous bound



$$
\limsup\frac{\Theta_1^>(m)}{6m}
 \le\frac{\log136-\mathfrak C_F}{6}.                 \tag{6.2}
$$



No theorem here proves the desired stronger statement



$$
\Theta_1^>(m)=o(m).                                   \tag{6.3}
$$



In particular, Chebotarev density for the cubic character of (2) among
all primes cannot replace (6.3): the divisors of the moving pair
((\mu_{0,m},\mu_{1,m})) are a correlated weighted subset.  The exact
congruence table (2.3) sorts a divisor after it occurs; it does not prove
that the three bins receive comparable mass.

The smallest remaining theorem on this branch is now the stripped-carrier
bound



$$
\log\left(\gcd(|\mu_{0,m}|,|\mu_{1,m}|)_{p>6m}\right)=o(m),
 \tag{6.4}
$$



or a direct selected-bin version of (6.4).  Unlike a first-digit radical
statement, (6.4) already includes the depth required by Item 390.

## 7. Ledger and overlap audit

The effect is deliberately separated into four entries.

1. **Booked lower bound:** no change.  (F_m=G_m) was already divided
   out in the frozen normalization, and its divisibility is inherited from
   Item 200.
2. **Strictly-large component ceiling:** decreases from
   ((\log136)/6) to ((\log136-\mathfrak C_F)/6), an
   improvement of (mathfrak C_F/6).
3. **Global total-content ceiling:** unchanged.  Item 393 forbids
   subtracting an upper bound for (c_m^>) from an upper bound for the
   product (c_m).
4. **Frozen deficit:** unchanged at
   
   

$$
T-r_1=1.0196329836694317938803064012\ldots .
$$



The interval subproduct support lies in (4m+1<\ell<6m), disjoint from
the booked (p<2m) Cartier support.  The remaining factors of (F_m)
may overlap earlier Cartier strata, but none is a second reservoir:
(F_m=G_m) is removed from an auxiliary height before the (p>6m) part
is measured.

## 8. Strict claim ledger

### PROVED

* The exact tied congruence table (2.1)--(2.3) and retained Frobenius mark.
* The phase-independent integral marked representatives (3.6)--(3.9).
* Inherited Item-200 integrality (F_m\mid\lambda_{0,m},\lambda_{1,m}),
  with an independent proof of its interval subproduct in Section 4.
* The new exact all-depth fully normalized carrier (1.10) and (5.2).
* The new component ceiling (1.11), improving the previous one by
  (mathfrak C_F/6).
* Zero booking and no global total-ceiling subtraction.

### OPEN

* Weighted zero density (6.3) or (6.4).
* Uniform selected-branch noncollision and (c_m^>=1).
* Any carrier-weighted Frobenius equidistribution theorem.
* Route-1 completion and irrationality of (e+\pi).

### NOT CLAIMED

* An actual wrong-branch prime.
* A Chebotarev law for divisors of the moving carrier.
* That finite normalization rows prove noncollision.
* That any factor of (F_m) is a new divisor of normalized content.
* Any new positive Route-1 mass.

## 9. Replay and dependencies

Run

```text
python scripts/item415_marked_selector_compulsory_strip_certificate.py \
  --output results/item415_marked_selector_compulsory_strip_certificate_replay.json \
  --replay results/item415_marked_selector_compulsory_strip_certificate.json
```

The standard-library replay:

1. verifies every pinned dependency hash;
2. checks the exact tied (d=3h), phase, modulo-(18), and Frobenius-mark
   bookkeeping on transparent rows;
3. evaluates (1.4)--(1.5) exactly for (1\le m\le160);
4. reconstructs canonical Item 200's full rank-zero prime set, verifies
   (F_m\mid\lambda_{0,m},\lambda_{1,m}), and checks that the displayed
   interval primes form its (j=0) subproduct in that declared range;
5. verifies every interval-prime divisibility and every degree inequality
   used in (4.5)--(4.7);
6. verifies the integral marked-basis transform and its determinant; and
7. records the exact capacity arithmetic.

The finite range is not the proof of the full (F_m)-divisibility theorem;
that theorem is inherited from canonical Item 200.  Section 4 supplies an
independent uniform proof of its interval subproduct.  The theorem and its
component-ceiling delta have been canonicalized after independent root audit.
