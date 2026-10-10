> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 420 — fixed-coordinate saddle obstruction beyond circular Cauchy optimization

Date: 2026-09-01  
Status: **CANONICAL, ROOT-AUDITED, SCOPED HEIGHT NO-GO, NO BOOKING**

## 1. Capacity-first verdict

Canonical Item 390 identifies the complete strictly-large mixed-cubic
content with the $p>6m$ part of the gcd of two exact residue integers.
Canonical Item 415 removes the complete forced Cartier product $F_m$, and
canonical Item 418 proves the component ceiling



$$
\limsup_{m\to\infty}\frac{\log c_m^>}{6m}
 \le \frac{\log\rho_*-\mathfrak C_F}{6}
 =0.4287738853386578689457603829\ldots,
 \tag{1.1}
$$



where



$$
\rho_*=135.5974839008548212502259703306\ldots,
 \qquad
 \mathfrak C_F=2.3370475079987656871108854826\ldots .
 \tag{1.2}
$$



The natural next idea is to exploit the visibly near-proportional pair
instead of bounding the two coordinates separately.  This item settles the
entire class of **fixed rational coordinate combinations**.

For every fixed $(a,b)\in\mathbb Q^2\setminus\{(0,0)\}$, this item proves



$$
\boxed{
 \limsup_{m\to\infty}
 |a\lambda_{0,m}+b\lambda_{1,m}|^{1/m}=\rho_* .}
 \tag{1.3}
$$



There is exactly one leading saddle cancellation,



$$
D_m:=2\lambda_{1,m}-5\lambda_{0,m},
 \tag{1.4}
$$



but it removes only a polynomial factor:



$$
D_m=m^{-3/2}
 \bigl(C_D\tau^m+\overline{C_D}\,\overline{\tau}^{\,m}
 +O(\rho_*^m/m)\bigr),
 \qquad |\tau|=\rho_*,\quad C_D\ne0.
 \tag{1.5}
$$



The uncancelled combinations have the usual $m^{-1/2}$ saddle scale.
Consequently, after division by $F_m$, every fixed nonzero normalized
combination still has root base



$$
\rho_*e^{-\mathfrak C_F}
 =13.1004071782333102143382142797\ldots .
 \tag{1.6}
$$



Thus no asymmetric circle, noncircular contour, or other absolute-height
argument applied to one fixed coordinate combination can reduce the
exponential base in Item 418.  This is an obstruction from the **actual
size of the sequence**, not merely from a loose contour estimate.

The ledger delta is exactly zero.  A genuinely smaller component ceiling
must use information not present in a fixed linear combination: an
$m$-dependent combination, a joint gcd/resultant theorem, or arithmetic
nonconcentration of the normalized pair.

## 2. Inherited exact carrier and common phase

Retain the canonical residue formulas



$$
\lambda_{0,m}=[y^{4m}]
 \frac{(1-y)^{6m}(1+y)}{(1+y^2)^{4m+1}},
 \tag{2.1}
$$





$$
\lambda_{1,m}=[y^{4m+1}]
 \frac{(1-y)^{6m}(1+y)^4}{(1+y^2)^{4m+2}}.
 \tag{2.2}
$$



Write (operatorname{CT}) for constant term and define



$$
H(y)=\frac{(1-y)^6}{y^4(1+y^2)^4},
 \qquad
 f_0(y)=\frac{1+y}{1+y^2},
 \qquad
 f_1(y)=\frac{(1+y)^4}{y(1+y^2)^2}.
 \tag{2.3}
$$



Then both coordinates are periods of the same phase:



$$
\lambda_{0,m}=\operatorname{CT}\bigl(f_0H^m\bigr),
 \qquad
 \lambda_{1,m}=\operatorname{CT}\bigl(f_1H^m\bigr).
 \tag{2.4}
$$



Canonical Items 390 and 415 give



$$
c_m^>=
 \bigl(\gcd(|\mu_{0,m}|,|\mu_{1,m}|)\bigr)_{p>6m},
 \qquad
 \mu_{s,m}=\lambda_{s,m}/F_m,
 \tag{2.5}
$$



on every nonzero row, and



$$
\log F_m=\mathfrak C_Fm+o(m).
 \tag{2.6}
$$



All factors of $F_m$ are at most $6m$.  Division by $F_m$ therefore
does not alter any target valuation in the strictly-large component.  No
new divisor is introduced or booked here.

## 3. The critical cubic and the unique fixed cancellation

Direct logarithmic differentiation gives



$$
\frac{H'(y)}{H(y)}
 =\frac{2P(y)}{y(1-y)(1+y^2)},
 \qquad
 P(y)=3y^3-6y^2-y-2.
 \tag{3.1}
$$



The amplitude ratio satisfies the exact identity



$$
\frac{f_1(y)}{f_0(y)}-\frac52
 =-\frac{P(y)}{2y(1+y^2)}.
 \tag{3.2}
$$



Hence at every critical point of (H),



$$
f_1=\frac52f_0.
 \tag{3.3}
$$



The relevant denominators and $f_0$ do not vanish there.  For example,



$$
\operatorname{Res}(P,1+y)=10,
 \qquad
 \operatorname{Res}(P,P')=9900.
 \tag{3.4}
$$



For a fixed combination $a\lambda_0+b\lambda_1$, its leading amplitude
at either dominant saddle is therefore



$$
f_0\left(a+\frac52b\right).
 \tag{3.5}
$$



It vanishes precisely when (2a+5b=0).  Up to a nonzero rational scalar,
the only fixed leading cancellation is exactly (1.4).  There is no second
fixed direction to test.

## 4. Exact integration by parts for the cancelled direction

Put



$$
A(y)=\frac{1-y^2}{2(1+y^2)}.
 \tag{4.1}
$$



Equations (3.1)–(3.2) give the rational identity



$$
2f_1-5f_0=-A\frac{H'}H.
 \tag{4.2}
$$



Using the constant-term contour and integrating a total derivative gives,
for every $m\ge1$,



$$
\begin{aligned}
 D_m
 &=-\frac1m\frac1{2\pi i}
   \oint \frac{A(y)}y\,d(H(y)^m)\\
 &=\frac1m\operatorname{CT}\bigl(q(y)H(y)^m\bigr),
\end{aligned}
\tag{4.3}
$$



where



$$
q(y)=y\left(\frac{A(y)}y\right)'
 =\frac{y^4-4y^2-1}{2y(1+y^2)^2}.
 \tag{4.4}
$$



This is an exact, all-$m$ two-coordinate cancellation identity.  In
ordinary coefficient notation it says



$$
mD_m=\frac12[y^{4m+1}]
 \frac{(y^4-4y^2-1)(1-y)^{6m}}
 {(1+y^2)^{4m+2}}.
 \tag{4.5}
$$



The new amplitude does not vanish at a critical point:



$$
\operatorname{Res}
 \bigl(P,y^4-4y^2-1\bigr)=176\ne0.
 \tag{4.6}
$$



Thus (4.3) buys exactly one factor $m^{-1}$; it does not remove the
dominant exponential phase.

## 5. Exact dominant-saddle geometry

The cubic $P$ has discriminant $-3300$, hence one real root
$\beta$ and a conjugate pair $\alpha,\bar\alpha$.  Since
$P(2)<0<P(3)$, one has $\beta>1$.  Vieta gives



$$
x:=\alpha\bar\alpha=\frac{2}{3\beta}.
 \tag{5.1}
$$



Substitution of $\beta=2/(3x)$ in $P(\beta)=0$ yields



$$
9x^3+3x^2+12x-4=0.
 \tag{5.2}
$$



This is exactly the Item-418 minimizer equation.  Therefore



$$
|\alpha|=|\bar\alpha|=r_*=\sqrt{x_*}.
 \tag{5.3}
$$



Item 418 proves that on $|y|=r_*$, these are the only two points where
$|H|$ attains its maximum, and that maximum is $\rho_*$.  The maximum
is quadratic: $P$ is squarefree, and the exact angular derivative in
Item 418 changes sign simply at the maximizing cosine.

For completeness, eliminating $y$ from $P(y)=0$ and $t=H(y)$ gives



$$
262144t^3+68124672t^2+4819949712t-531441=0.
 \tag{5.4}
$$



Its discriminant is



$$
-9597549474870371132689612800000000<0.
 \tag{5.5}
$$



Thus $H(\alpha)=\tau$ and $H(\bar\alpha)=\bar\tau$ are distinct
nonreal conjugates, with



$$
|\tau|=\rho_*.
 \tag{5.6}
$$



The deterministic replay verifies (3.1), (3.2), (4.2)–(4.6), (5.2), and
the cleared polynomial relation behind (5.4), all over $\mathbb Q$.

## 6. Saddle lemma and the true root size

We use the following elementary one-variable saddle lemma.

**Lemma.**  Let $f$ be rational and holomorphic at
$\alpha,\bar\alpha$ and on a neighborhood of the circle
$|y|=r_*$.  If $f(\alpha)\ne0$, then there is a nonzero constant
$C_f$ such that



$$
\operatorname{CT}(fH^m)
 =m^{-1/2}
 \left(C_f\tau^m+\overline{C_f}\,\overline{\tau}^{\,m}
 +O(\rho_*^m/m)\right).
 \tag{6.1}
$$



To prove the lemma, write the constant term as the integral on
$|y|=r_*$, split the circle into fixed small arcs around
$\alpha,\bar\alpha$, and their complement.  Item 418's strict maximizer
theorem bounds the complement by $(\rho_*-\epsilon)^m$.  On each small
arc, $H'=0$, $H''\ne0$, and the real part of the angular quadratic
term is negative.  Taylor expansion followed by the Gaussian change of
variables gives (6.1); its leading constant is nonzero precisely when the
amplitude is nonzero at the saddle.  The two local expansions are
conjugate because all rational functions involved have real coefficients.

Apply the lemma first to



$$
f=af_0+bf_1.
 \tag{6.2}
$$



If $2a+5b\ne0$, (3.5) makes its saddle amplitude nonzero, giving (6.1).
If $2a+5b=0$, the combination is a nonzero multiple of $D_m$.  Apply
the lemma to $q$, whose saddle amplitude is nonzero by (4.6), and then
use the exact factor $1/m$ in (4.3).  This gives (1.5).

Finally write $\tau=\rho_*e^{i\phi}$ and
$C=|C|e^{i\delta}$.  Equation (5.5) implies
$e^{2i\phi}\ne1$.  Therefore



$$
\frac1N\sum_{m=1}^N\cos^2(m\phi+\delta)\longrightarrow\frac12.
 \tag{6.3}
$$



In particular, the conjugate saddle sum is bounded away from zero along
an infinite subsequence.  Polynomial factors do not affect $m$-th roots.
This proves (1.3) in both cases.

## 7. Consequence for normalized height arguments

For fixed integers (a,b), Item 415 gives



$$
a\mu_{0,m}+b\mu_{1,m}
 =\frac{a\lambda_{0,m}+b\lambda_{1,m}}{F_m}\in\mathbb Z.
 \tag{7.1}
$$



Combining (1.3) with (2.6),



$$
\boxed{
 \limsup_{m\to\infty}
 |a\mu_{0,m}+b\mu_{1,m}|^{1/m}
 =\rho_*e^{-\mathfrak C_F}.}
 \tag{7.2}
$$



Since $c_m^>$ divides every integer combination in (7.1), one may try
to bound it through a particularly small combination.  Equation (7.2)
shows that no **fixed** choice improves the exponential height.  The best
visible cancellation $D_m$ changes $m^{-1/2}$ to $m^{-3/2}$, which
contributes only $O(\log m)$ to a logarithmic ledger.

This also closes the following contour extensions:

1. using different centered radii for the two coordinates;
2. using a noncircular contour to bound one fixed combination by absolute
   values; and
3. replacing the pair by (2\lambda_1-5\lambda_0) before applying
   Cauchy or steepest descent.

Any such proof of a uniform bound with exponential base below $\rho_*$
would contradict the actual limsup in (1.3).  The theorem does **not**
exclude a joint arithmetic bound for the gcd that is much smaller than
every fixed combination.

## 8. Capacity and de-overlap ledger

The exact ledger effect is:

1. **Booked lower bound:** no change.
2. **Strictly-large component ceiling:** no change from Item 418;
   it remains (1.1).
3. **Global total-content ceiling:** no change.  A component bound is not
   an additive subtraction from a global upper bound.
4. **Frozen deficit:** no change at
   (1.0196329836694317938803064012\ldots).

As an admission comparison only, even eliminating the entire strictly-large
component would still leave



$$
0.5908590983307739249345460183\ldots
 \tag{8.1}
$$



outside it.  This is not a de-overlapped global conclusion.

The capacity screen therefore says: do not invest further in fixed
coordinate combinations or contour tuning.  The live alternatives are a
joint gcd/resultant identity, an $m$-dependent transfer with a proved
smaller root base, or valuation-weighted zero density.

## 9. Strict claim ledger

### PROVED

* The common-phase constant-term model (2.3)–(2.4).
* The unique fixed leading cancellation $D_m=2\lambda_1-5\lambda_0$.
* The exact integration-by-parts identity (4.3)–(4.5).
* Nonvanishing of the post-cancellation saddle amplitude, by (4.6).
* The actual root-size theorem (1.3) for every fixed nonzero rational
  coordinate combination.
* The normalized root-size theorem (7.2).
* Zero booking and zero component/global ledger delta.

### SCOPED NO-GO

* No absolute-height argument applied to one fixed coordinate combination,
  regardless of circular, asymmetric, or noncircular contour, can improve
  Item 418's exponential base.

### OPEN

* An $m$-dependent coordinate combination with a genuinely smaller root
  base.
* A joint gcd, resultant, recurrence-transfer, or modular nonconcentration
  theorem for $(\mu_{0,m},\mu_{1,m})$.
* $\log c_m^>=o(m)$ or $c_m^>=1$.
* Any new booked Route-1 mass, Route-1 completion, or irrationality of
  $e+\pi$.

### NOT CLAIMED

* That the gcd has exponential size $\rho_*e^{-\mathfrak C_F}$.
* That a finite census proves noncollision.
* That every $m$-dependent linear combination is obstructed.
* Any proof of the irrationality of $e+\pi$.

## 10. Deterministic replay

Run

```text
python scripts/item420_normalized_contour_extension_certificate.py \
  --output results/item420_normalized_contour_extension_certificate_replay.json \
  --replay results/item420_normalized_contour_extension_certificate.json
```

The standard-library replay:

1. pins canonical Items 390, 415, and 418 by SHA-256;
2. verifies the common-phase critical cubic exactly;
3. verifies the unique amplitude cancellation and integration-by-parts
   identity over $\mathbb Q(y)$;
4. computes the exact nonvanishing resultants (9900), (10), and (176);
5. verifies the critical-modulus and critical-value polynomial relations;
6. checks (4.5) independently on sixteen exact integer rows; and
7. records the unchanged, de-overlapped component ledger.

The canonical artifacts are stored in `sources/`, `scripts/`, `results/`,
and `manifests/`.
