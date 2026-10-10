> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the high-radius integral-jet pullback

## Verdict

**ACCEPT**, for the frozen artifacts listed below.

The note under audit correctly proves, for



$$
F(w)=4\arctan\frac{w}{2-w},\qquad
 \phi(z)=z+\frac{z^7-z^8}{140},\qquad
 G(z)=F(\phi(z)),
$$



that



$$
G(1)=\pi,\qquad G^{(n)}(0)\in\mathbb Z\quad(n\geq0),
 \qquad \rho(G)>\frac32.
$$



The all-order integrality argument, genuine-singularity argument, reversal of
the root problem, Schur--Cohn convention, and all eight exact rational gaps
are valid.  The finite diagonal Hermite--Padé records for
$1\leq n\leq15$ also reproduce and survive an independent exact
construction.  The note correctly limits those records to finite diagnostics;
it does not claim an all-degree estimate or a classification of $e+\pi$.

## 1. Frozen input snapshot

The audit froze these five files before doing any calculation:

| artifact | SHA-256 |
|---|---|
| `sources/high_radius_composed_integral_jet_pullback.md` | `0f1a41bb40ec457e51f1b0c1fa5299de784f93a3c7f92bc372bcad2fff7e7b87` |
| `scripts/high_radius_composed_pullback_certificate.py` | `ed1e0e6c92392f0fa27f5fbe6e00603151c22ed1ec05d3eaaed9e0211ae7fce4` |
| `results/high_radius_composed_pullback_certificate.json` | `b3bbdda30c993a122dc056cc137689ee9281d4ecc11efabac69174891c348e23` |
| `scripts/high_radius_composed_pullback_hp_probe.py` | `f7cb212ebb4b9e79cc08486c8d090e36e9245144e24ffc06aca120699149963d` |
| `results/high_radius_composed_pullback_hp_n15.json` | `831626a38451e3a060f1e790038a27935c226210cb6fc4bf0c4fae448f6e772d` |

The independent program rehashed the five inputs both at the beginning and
at the end of its run.  All five hashes remained equal to the frozen values.

The audit artifacts are:

| artifact | SHA-256 |
|---|---|
| `scripts/independent_high_radius_composed_pullback_audit.py` | `3802bb756fe0c01b592e7547896cdb3eee8e1ba56088ff2b7d22ce26b4394f29` |
| `results/independent_high_radius_composed_pullback_audit.json` | `08b1d5ef58f94624dad47773377bdc7dce822347adfe994f56811e68f13e55af` |

The two source programs were also rerun to temporary output files with their
documented defaults.  The regenerated radius JSON had SHA-256
`b3bbdda30c993a122dc056cc137689ee9281d4ecc11efabac69174891c348e23`,
and the regenerated $n\leq15$ HP JSON had SHA-256
`831626a38451e3a060f1e790038a27935c226210cb6fc4bf0c4fae448f6e772d`.
Thus both reproduced byte-for-byte.

## 2. Endpoint and all-order Hurwitz integrality

Direct substitution gives



$$
\phi(0)=0,\qquad \phi(1)=1,
$$



and exact differentiation gives the derivative jets



$$
\bigl(\phi'(0),\ldots,\phi^{(8)}(0)\bigr)
 =(1,0,0,0,0,0,36,-288).
$$



Hence $G(1)=F(1)=\pi$, and every derivative jet of $\phi$ is an
integer.  The base-jet formula in the source note was checked from
$F'(w)=4/(w^2-2w+2)$.  It can be split into the transparent integer
forms



$$
F^{(2m)}(0)
 =2^{2-m}(2m-1)!\sin\frac{m\pi}{2},
$$



and



$$
F^{(2m+1)}(0)=\pm 2^{1-m}(2m)!.
$$



The relevant powers of two divide the displayed factorials (and a vanishing
sine only makes the even case immediate).  Thus every $F^{(k)}(0)$ is an
integer.  Exponential partial Bell polynomials have integer coefficients, so
Faà di Bruno's formula then proves $G^{(n)}(0)\in\mathbb Z$ for every
$n$, not merely for the finite computed range.

As a separate computational check, the audit generated the ordinary Taylor
series of $F$ from



$$
(2-2w+w^2)F'(w)=4
$$



and then composed that series with $\phi$ by exact rational polynomial
multiplication.  This differs from the source program's direct division of
the rational function $G'$.  The independently computed jets through order
120 have the same canonical-vector hash,

`47e6d2c95ecb8c968bd5a890ea83e2c5ead1efee6787942e3ed0c13f9215ce83`,

as the archived certificate.  The jets through order 46 have hash

`ac06b6a1b3b436cade3760f3e25b6fab5911e96f4e0cfb6d7b8e87b609373ab2`,

matching the finite HP file.

## 3. Genuine singularities and the exact radius characterization

The source differentiates correctly:



$$
G'(z)=\frac{4\phi'(z)}
 {\bigl(\phi(z)-(1+i)\bigr)\bigl(\phi(z)-(1-i)\bigr)}.
$$



For completeness, if $\phi(z)-(1+i)$ has multiplicity $m$ at
$z_0$, write



$$
\phi(z)-(1+i)=c(z-z_0)^m+O((z-z_0)^{m+1}),\qquad c\ne0.
$$



Then $\phi'(z)=mc(z-z_0)^{m-1}+O((z-z_0)^m)$, while the other
denominator factor equals $2i$ at $z_0$.  Consequently $G'$ has a
simple pole with nonzero residue there.  The same calculation applies over
$1-i$.  Every such preimage is therefore a genuine logarithmic
singularity; criticality of $\phi$ cannot remove it.

Conversely, in any disk containing no preimage of $1\pm i$, the displayed
rational derivative is holomorphic and has a primitive matching the germ at
zero.  Therefore the Taylor radius is exactly



$$
\rho(G)=\min\{|z|:\phi(z)=1+i\text{ or }\phi(z)=1-i\}.
$$



Real coefficients of $\phi$ make the two modulus multisets identical.
This validates every step connecting the polynomial root certificate to the
Taylor radius.

## 4. Independent Schur--Cohn audit

Let $q(z)=\phi(z)-(1+i)$ and $r=3/2$.  Exact substitution independently
gave



$$
w^8q(r/w)=-(1+i)w^8+\frac32w^7
 +\frac{2187}{17920}w-\frac{6561}{35840},
$$



which is the same polynomial as equation (10) of the source note.  Its roots
are $w=r/z$ as $z$ ranges over the roots of $q$.  Thus all roots of
the reversed polynomial being in $|w|<1$ is exactly equivalent to every
root of $q$ satisfying $|z|>3/2$.

The convention in the source is correct.  If a degree-$d$ polynomial is
made monic and has constant coefficient $c$, define



$$
P^*(w)=w^d\overline{P(1/\overline w)}.
$$



Then $P-cP^*$ has zero constant coefficient and leading coefficient
$1-|c|^2$.  Cohn's reduction



$$
P\longmapsto\frac{P-cP^*}{w}
$$



reduces by one the number of roots in the open unit disk precisely when
$|c|<1$.  Iterating to degree zero proves that all roots start inside the
unit disk if and only if all successive gaps $1-|c|^2$ are positive.
For degree one this also reduces immediately to the familiar condition that
the unique root have modulus less than one, fixing the direction of the
inequality.

The independent code represented the polynomials directly in SymPy over
Gaussian rationals, normalized by the exact leading coefficient at each
stage, formed the reversed-conjugate polynomial symbolically, and repeated
the recursion through degrees $8,7,\ldots,1$.  It did not import or call
the rational-pair implementation under audit.  All eight normalized
constants and all eight reduced rational gaps agree exactly with the archived
JSON.  The complete numerators and denominators printed in equation (15) of
the source note were also parsed and compared to the JSON; all eight table
rows agree exactly.  Every gap numerator and denominator is a positive
integer.  This rigorously certifies



$$
\rho(G)>\frac32.
$$



As a non-rigorous diagnostic only, an independent 80-digit `mpmath.polyroots`
calculation agrees with all eight archived SymPy roots to at least 50 decimal
places.  Its nearest root is



$$
1.1643315582209919122503107517611919262\ldots
 +1.0380180762857160549078253764671130991\ldots i,
$$



of modulus



$$
1.5598556036265734152460990842856358070\ldots.
$$



This decimal calculation is not used in the proof.

## 5. Independent finite Hermite--Padé audit

The source eliminates $A$ first and solves an integer derivative matrix in
the coefficients of $B,C$.  The audit instead formed the full ordinary
Taylor-coefficient system directly.  Its columns are all coefficients of
$A,B,C$; its rows impose every coefficient condition from order zero
through $3n$, followed by $C(1)=B(1)$.  This is a
$(3n+2)$-by-$(3n+3)$ rational matrix.  It had full row rank for every
$1\leq n\leq15$, independently yielding a one-dimensional kernel and the
same primitive polynomial triple.

For the cofactor content, the audit also rebuilt the source's integer
high-derivative matrix.  It selected the last nonzero kernel coordinate for
one maximal minor, whereas the source selects the first.  It then evaluated
a second minor at the first nonzero coordinate and verified the exact
cofactor-vector proportionality.  This independently verifies that the
reported scalar is the common maximal-cofactor content.

The following compact table summarizes the independent records.  `high rank`
is the rank of the source-sized $(2n+1)$-by-$(2n+2)$ matrix; `full rank`
is the rank of the audit's full matrix.  `content digits` and `height digits`
refer to the exact cofactor content and primitive triple.  The endpoint entry
is the certified base-ten decade of the fully reduced endpoint form.

| $n$ | high rank | full rank | content digits | height digits | endpoint |
|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 5 | 1 | 1 | exactly zero |
| 2 | 5 | 8 | 1 | 4 | 0 |
| 3 | 7 | 11 | 3 | 12 | 7 |
| 4 | 9 | 14 | 6 | 23 | 15 |
| 5 | 11 | 17 | 12 | 38 | 26 |
| 6 | 13 | 20 | 20 | 57 | 44 |
| 7 | 15 | 23 | 30 | 81 | 64 |
| 8 | 17 | 26 | 42 | 109 | 89 |
| 9 | 19 | 29 | 58 | 141 | 119 |
| 10 | 21 | 32 | 77 | 178 | 150 |
| 11 | 23 | 35 | 100 | 221 | 191 |
| 12 | 25 | 38 | 125 | 267 | 233 |
| 13 | 27 | 41 | 155 | 319 | 281 |
| 14 | 29 | 44 | 190 | 374 | 331 |
| 15 | 31 | 47 | 228 | 434 | 385 |

For every $n\leq15$, the audit compared all of the following against the
archived record:

* source-sized shape, rank, and nullity;
* the canonical SHA-256 of the primitive high kernel;
* maximal-cofactor common-content digit count;
* primitive-triple height and canonical SHA-256;
* exact raw endpoint pair, endpoint gcd, and exact reduced endpoint pair;
* exact numerator and denominator of the coefficient at order $3n+1$;
* its nonvanishing flag; and
* the certified endpoint sign and base-ten decade.

Every comparison passed.  In particular, all fifteen first-free coefficients
are nonzero, and the $n=1$ endpoint pair is exactly $(0,0)$.

For the endpoint signs, the audit did not reuse the source interval.  It used
200 terms for the Taylor interval for $e$, 200 alternating terms for
$\arctan(1/5)$, 60 for $\arctan(1/239)$, and Machin's identity



$$
\pi=16\arctan(1/5)-4\arctan(1/239).
$$



The resulting exact rational interval independently gives the same sign and
decade in every record.  Separately, the byte-for-byte source-output
reproduction checks the source interval-fraction hashes as well.  Finally,
the decade list and content-digit list printed in equations (20) and (21) of
the source note were parsed and found identical to the archived JSON arrays.

## 6. Format and scope checks

The Markdown source is valid UTF-8 (`iconv` round-trip succeeded).  Pandoc
converted it with `--from=markdown+tex_math_dollars --to=html` without an
error or warning.  Both Python files compile, and both JSON files parse.

The accepted result is a useful analytic/arithmetic construction, but its
finite endpoint forms grow strongly.  Neither the source note nor this audit
proves algebraicity or transcendence of $e+\pi$.  Any use of this candidate
in that classification problem still requires a new all-degree primitive
height/content estimate or a different non-diagonal construction.
