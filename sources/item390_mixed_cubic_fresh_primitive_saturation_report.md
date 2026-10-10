> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 390 — Actual mixed-cubic fresh primitive saturation and a global height ceiling

Date: 2026-09-01  
Status: **WORK-ONLY, UNAUDITED, NO CENTRAL EDIT, NO BOOKING**

## 1. Scoped verdict

Item 388 showed that finitely many local Witt/Hasse digits cannot exclude an
arbitrary common rescaling in an ambient information class.  That ambient
rescaling does **not** survive unchanged in the actual normalized
mixed-cubic family.

Let



$$
N=6m,\qquad K_0=4m+1,\qquad K_1=4m+2,
$$



and retain the frozen coordinates



$$
H_s=R_s+\frac{L_s}{4}\log2+\frac{E_s}{8}\pi,
 \qquad
 A_m=L_1R_0-L_0R_1,
 \qquad
 B_m=\frac{L_1E_0-L_0E_1}{8}.
$$



After the frozen clearing and Cartier removal, write



$$
U_m=\frac{D_m^\sharp A_m}{G_m},\qquad
 V_m=\frac{D_m^\sharp B_m}{G_m},\qquad
 c_m=\gcd(U_m,V_m).
$$



Define the integral logarithmic residues



$$
\lambda_{0,m}=2^{2m}L_0,
 \qquad
 \lambda_{1,m}=2^{2m+2}L_1,
$$



and the strictly large-prime primitive content



$$
c_m^{>}:=\prod_{p>6m}p^{v_p(c_m)}.
$$



For every row with $(U_m,V_m)\ne(0,0)$—in particular for every
sufficiently large $m$, by the frozen nonzero saddle-amplitude theorem—
this item proves the exact, all-depth identity



$$
\boxed{
 v_p(c_m)=
 \min\{v_p(\lambda_{0,m}),v_p(\lambda_{1,m})\}
 \quad(p>6m),}
 \tag{1.1}
$$



and hence



$$
\boxed{
 c_m^{>}=
 \left(\gcd(|\lambda_{0,m}|,|\lambda_{1,m}|)\right)_{p>6m}.}
 \tag{1.2}
$$



Thus every nontrivial common scalar outside the coarse local envelope
$p\le6m$ is target-forced by one exact global primitive carrier.  It is not
an arbitrary scalar invisible to the period construction.

For all sufficiently large $m$, the same carrier satisfies the uniform
height bound



$$
\boxed{c_m^{>}<21\cdot136^m,}
 \tag{1.3}
$$



so



$$
\boxed{
 \limsup_{m\to\infty}\frac{\log c_m^{>}}{6m}
 \le\frac{\log136}{6}
 =0.8187758142893420014\ldots .}
 \tag{1.4}
$$



This is a material Closer result for the **strictly large-prime fresh
component**.  It does not prove $c_m^{>}=1$, does not control undeclared
content at primes $p\le6m$, and does not bound fresh beta matching or
multi-parent reuse.

## 2. Exact normalization and the global carrier

Put



$$
M=M_{4m+1},\qquad
 T=\prod_{2m<p<3m}p,\qquad
 K=M/T.
$$



The frozen coordinate audit gives



$$
\widehat A_m=2^{9m+4}MA_m\in\mathbb Z,
 \qquad
 \widehat B_m=2^{9m+5}B_m\in\mathbb Z,
$$



and



$$
U_m=\frac{2\widehat A_m}{TG_m},
 \qquad
 V_m=\frac{K\widehat B_m}{G_m}.
 \tag{2.1}
$$



For $p>6m$, every factor in (2.1) other than the raw coordinates is a
$p$-unit.  Therefore



$$
v_p(c_m)=\min\{v_p(A_m),v_p(B_m)\}.
 \tag{2.2}
$$



The two integral residues have the exact characteristic-zero coefficient
formulas



$$
\lambda_{0,m}=[y^{4m}]
 \frac{(1-y)^{6m}(1+y)}{(1+y^2)^{4m+1}},
 \tag{2.3}
$$





$$
\lambda_{1,m}=[y^{4m+1}]
 \frac{(1-y)^{6m}(1+y)^4}{(1+y^2)^{4m+2}}.
 \tag{2.4}
$$



Equations (2.3)–(2.4) are not auxiliary ambient objects: they are exactly
the actual $(-1)$-pole log residues of the two mixed-cubic rows.

## 3. All-depth primitive-saturation theorem

The previous large-prime theorem established only the first-digit
equivalence



$$
p\mid\widehat A_m,\widehat B_m
 \quad\Longleftrightarrow\quad
 L_0\equiv L_1\equiv0\pmod p
 \qquad(p>6m).
 \tag{3.1}
$$



The same exact-differential argument gives every valuation layer at once.

Fix $p>6m$, and put



$$
t=\min\{v_p(L_0),v_p(L_1)\}.
$$



All $R_s,E_s,L_s$ are $p$-integral.  From



$$
A_m=L_1R_0-L_0R_1,
 \qquad
 8B_m=L_1E_0-L_0E_1
$$



one immediately gets



$$
\min\{v_p(A_m),v_p(B_m)\}\ge t.
 \tag{3.2}
$$



Assume the inequality were strict.  Write



$$
\ell_s=p^{-t}L_s\in\mathbb Z_p,
 \qquad
 (\ell_0,\ell_1)\not\equiv(0,0)\pmod p,
$$



and form the actual normalized differential



$$
\Omega=\ell_1\omega_0-\ell_0\omega_1
 =\frac{u^{6m}(\ell_1Q-\ell_0)}{Q^{4m+2}}\,dx.
 \tag{3.3}
$$



Its log coordinate is identically zero.  Strictness in (3.2) says that its
rational endpoint coordinate and its $\pi$-coordinate also vanish modulo
$p$.  Hence all simple residues vanish.  Since the pole orders are below
$p$ and (3.3) is proper at infinity, the frozen partial-fraction argument
makes $\Omega=dF$ over $\mathbb F_p(x)$, with $F(0)=F(1)$.

If $p=6m+1$, the local coefficients at $0$ and $1$ force



$$
\ell_1-\ell_0=0,
 \qquad
 4\ell_1-\ell_0=0,
$$



and hence $\ell_0=\ell_1=0$, a contradiction.  If $p>6m+1$, the
endpoint and infinity conditions force



$$
F-C=\frac{u^{6m+1}(ax+b)}{Q^{4m+1}}.
$$



Differentiating and comparing with (3.3) gives



$$
b=(10m+2)a,
 \qquad
 4a(4m+1)=0.
$$



Because $p>6m$, one obtains $a=b=0$, and then
$\ell_0=\ell_1=0$, again a contradiction.  Therefore equality holds in
(3.2):



$$
\min\{v_p(A_m),v_p(B_m)\}
 =\min\{v_p(L_0),v_p(L_1)\}.
 \tag{3.4}
$$



The dyadic factors in $\lambda_{0,m},\lambda_{1,m}$, and every factor in
(2.1), are $p$-units.  Combining (2.2) and (3.4) proves (1.1), including
all multiplicities.  Multiplying (1.1) over $p>6m$ proves (1.2).

This is stronger than a new Hasse digit: it is an all-depth primitive
saturation theorem for the complete strictly large-prime scalar class.

## 4. A rigorous fixed-circle height bound

Let $0<r<1$.  Cauchy's formula applied to (2.3) gives



$$
|\lambda_{0,m}|
 \le r^{-4m}
 \max_{|z|=r}
 \left|
 \frac{(1-z)^{6m}(1+z)}{(1+z^2)^{4m+1}}
 \right|.
 \tag{4.1}
$$



The analogous bound from (2.4) is



$$
|\lambda_{1,m}|
 \le r^{-4m-1}
 \max_{|z|=r}
 \left|
 \frac{(1-z)^{6m}(1+z)^4}{(1+z^2)^{4m+2}}
 \right|.
 \tag{4.2}
$$



Take



$$
r=\frac{541}{1000}.
$$



For $z=re^{i\theta}$, put $c=\cos\theta$ and



$$
A=1+r^2-2rc,
 \qquad
 B=(1-r^2)^2+4r^2c^2.
$$



Then



$$
r^{-4}\left|\frac{(1-z)^6}{(1+z^2)^4}\right|
 =\frac{A^3}{r^4B^2}.
 \tag{4.3}
$$



The replay constructs the exact quartic



$$
P(c)=136r^4B^2-A^3.
 \tag{4.4}
$$



Its rational Sturm sequence has degrees $4,3,2,1,0$.  The endpoint sign
strings are



$$
(+,-,-,+,+)\quad\text{at }c=-1,
$$



and



$$
(+,+,-,-,+)\quad\text{at }c=1.
$$



Both have two sign variations, so $P$ has no zero in $[-1,1]$.
Moreover



$$
P(0)=
 \frac{94488816526994204984060513778645377}
 {125000000000000000000000000000000000}>0.
$$



Consequently



$$
\max_{|z|=r}
 r^{-4}\left|\frac{(1-z)^6}{(1+z^2)^4}\right|<136.
 \tag{4.5}
$$



The fixed amplitudes satisfy the elementary exact bounds



$$
\max_{|z|=r}\left|\frac{1+z}{1+z^2}\right|
 \le\frac{1+r}{1-r^2}
 =\frac{1000}{459}<3,
 \tag{4.6}
$$



and



$$
r^{-1}\max_{|z|=r}
 \left|\frac{(1+z)^4}{(1+z^2)^2}\right|
 \le
 \frac{2374681000}{113978421}<21.
 \tag{4.7}
$$



Equations (4.1)–(4.7) give



$$
|\lambda_{0,m}|<3\cdot136^m,
 \qquad
 |\lambda_{1,m}|<21\cdot136^m.
 \tag{4.8}
$$



The frozen saddle theorem makes the actual pair $(U_m,V_m)$ nonzero for
all sufficiently large $m$.  For those rows, if both residue integers
were zero then the defining determinant coordinates $A_m,B_m$, and hence
$U_m,V_m$, would both be zero.  Thus at least one residue integer is
nonzero, and (1.2), (4.8) prove (1.3)–(1.4).  No assertion about the finitely
many earlier rows is needed for the limsup.

No prime scan, assumed zero density, or factorization pattern enters this
bound.

## 5. Capacity and de-overlap

The inherited irrationality-measure ceiling for the **entire** content was



$$
\limsup\frac{\log c_m}{6m}\le1.99566316016\ldots .
$$



Before this item it was the only general height ceiling that automatically
covered the large-prime fresh factor.  Item 390 replaces it, for that
component, by



$$
\frac{\log136}{6}=0.8187758142893420\ldots,
$$



a component-ceiling decrease of



$$
1.1768873458706580\ldots .
$$



The booked rank-one rate plus the maximal new large-prime fresh rate is



$$
r_1+\frac{\log136}{6}
 =0.9552899825841548\ldots<T,
$$



leaving



$$
T-r_1-\frac{\log136}{6}
 =0.2008571693800898\ldots .
$$



This last comparison is an admission/capacity statement only: it says the
strictly large-prime scalar branch cannot by itself fill the Route-1 deficit.
It is not an upper bound for all remaining branches.

The de-overlap is exact within the scope proved here:

1. $p>6m$ is disjoint from the booked rank-one Cartier support
   $p<2m$, from the frozen Cartier/clearing factors, and from every prime
   in $M_{4m+1}$.
2. Equation (1.1) includes the full valuation, so no higher-digit copy at
   the same large prime may be counted again.
3. This does **not** automatically de-overlap later beta matching at a
   residual prime of $b_m=|V_m|/c_m$.  Any combined theorem must still be
   formulated on that primitive residual target.

Accordingly the ledger delta is:



$$
\boxed{\Delta r_{\rm booked}=0.}
$$



The result is a Closer ceiling, not a Builder divisor.

## 6. What is closed and what remains open

### Closed in this item

* Arbitrary ambient common rescaling as an explanation of actual content at
  primes $p>6m$.
* Every finite-depth ambiguity at such a prime: (1.1) is all-depth.
* The absence of any quantitative ceiling for the strictly large-prime
  fresh scalar component.
* Double-counting higher $p$-adic layers of that component.

### Not closed

* The stronger support conjecture $c_m^{>}=1$.
* Common content at primes $p\le6m$ outside the already classified forced
  supports.
* Uniform valuation mass on the small-prime Cartier/Witt side.
* Fresh beta singleton matching, $\Gamma_Q$, or multi-parent reuse.
* A combined exhaustive ceiling for the whole declared mixed-cubic
  architecture.
* Route 1 or the irrationality of $e+\pi$.

The correct next Closer target is therefore the remaining small-prime
primitive complement or a primewise coupling of the primitive beta target
to its global LCM—not another isolated large-prime scan.

## 7. Replay and dependencies

Deterministic replay:

```text
python work/item390_mixed_cubic_fresh_primitive_saturation_certificate.py \
  --output work/item390_mixed_cubic_fresh_primitive_saturation_certificate.replay.json
```

The replay uses exact rational polynomial arithmetic for the Sturm
certificate and independently cross-checks (2.3)–(2.4) against the frozen
scalar recurrence for $1\le m\le12$.  Those finite rows certify only the
normalization, not a support conjecture.

Primary dependencies:

* `ROUTE1_MASTER_CAPACITY.md`;
* `sources/mixed_cubic_coordinates_and_synchronization_audit.md`;
* `sources/mixed_cubic_large_prime_log_residue_theorem.md`;
* `sources/mixed_cubic_fresh_prime_coprimality_supplement.md`;
* `work/item388_mixed_cubic_local_data_nonexhaustion_report.md`.

All Item-390 artifacts are confined to `work/`.  No central document is
edited and no mass is booked.
