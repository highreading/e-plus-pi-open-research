> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Higher-power Cartier/Frobenius quantitative-ledger audit

Date: 2026-08-28

## 1. Scope and verdict

This is a read-only audit of the live Desktop archive, with emphasis on the
frozen higher-order Cartier/Frobenius packages 149--153.  No Desktop file was
modified.

The quantitative ledger is internally consistent:

- **PROVED:** the coefficient rate is
  $h=2.3246783391437311102576951141\ldots$, the rational-error
  exponent is $d=2.3370623743589729958539297805\ldots$, and ordinary
  positive matching has optimal beta scale $t=d/2$ and extra-content
  threshold
  

$$
T:=h-d/2=1.1561471519642446123307302239\ldots .
$$


- **PROVED:** item 149 forces one surviving digit on an explicit prime set,
  with rate
  

$$
r_1={-4\log2+6\log3-3\over6}
       =0.1365141682948128184504238226\ldots .
$$


- **PROVED:** item 151's rank-two theorem gives exact additional squarefree
  divisors, but its three proved uniform zero rays have zero exponential
  rate.  The rigorously proved rate therefore remains $r_1$.
- **PROVED UPPER CEILING, NOT A LOWER BOUND:** even if every possible
  rank-two floor determinant vanished, its additional radical mass could be
  at most
  

$$
C_2=6-\pi/\sqrt3-3\log3
       =0.8903637697614530752201860316\ldots
$$


  per $m$.  This would give total rank-at-most-two radical rate at most
  $0.2849081299217216643204548279\ldots$ per $6m$, still short by
  $0.8712390220425229480102753960\ldots$.
- **OPEN:** no package proves a second surviving $p$-adic digit on a set
  of positive weighted mass.  The currently proved deficit is
  

$$
T-r_1=1.0196329836694317938803064012\ldots
    \quad\text{per }6m.
$$



The most dangerous logical error would be to interpret $e_p$ Cartier
iterations at the denominator layer $q_p=p^{e_p}$ as a congruence modulo
$p^{e_p}$.  Every frozen Cartier conclusion here is still a
characteristic-$p$, modulo-$p$ statement.  It supplies one surviving
digit after the frozen normalizations, not $e_p$ digits and not an
automatic lift modulo $p^2$.

## 2. Hash-bound audit snapshot

The mutable overview files read for this audit had the following hashes:

```text
b5568af88dff169f316935529ba0b68087db9f33f5fa0b13aff4eff39ce8e928  README.md
f3e54d8be0636fa82e5ed12b7a96936f44522ad5f59732b501a39ce2e08d75e3  research_log.md
7d60803b797c43a0a36bbeb6577a93769475d627322f99b18ab9c3b6b887474d  active_checkpoint_20260828.md
```

The exact analytic ledger was checked against these frozen sources:

```text
286d9cf4d3591a1a9b9fefc6dd3ee3dcc9f7c2ba49a73310909491814544d9e8  sources/mixed_cubic_boundary_cartier_content_and_recurrence.md
55454aa99b2fcd06a87d94c1b51bedd912a740b731ba57eecfc391bd4572fc65  sources/mixed_cubic_accessible_saddle_exact_algebraic_certificate.md
ef8cc49a5a9b5533da790be732a7a5144be22cefacca8253320d297e22359318  sources/mixed_cubic_fixed_circle_complex_laplace_theorem.md
4ab613af6143b6bed1570f5b4b925fa4a35cec1ad04402080710381a6b3dc0d5  sources/mixed_cubic_matching_factor_two_and_classification_barrier.md
```

Their manifest SHA-256 values are, in the same order,
`34e61497fa2df8dd4dfcaf143be574bd3ada434977d41e6be75b590ba927a14c`,
`3521a1347ec499acf98d60bdd8f48ba991ef2a9e20c00c806313e91d1e5d8b10`,
`27ec125fd342aafe335f1026a72545c5afb205747def2781b25f4581f6a426c8`,
and
`e91ab6383402477c99a53ea11fe1de29bf9004288048e9ce84fd64ea4676bd0d`.

The item-149--153 primary sources and authoritative manifest hashes are:

```text
# item 149
593e1f69809c44245bd2d79bf1a503f96d1972a39ba17ea43ba7cd9f4b0e124b  sources/mixed_cubic_small_prime_rank_one_cartier_mass.md
90002db627dc5ebce5ff2141a12a9657eb5f0135306a13a9cd7df0a0a16de310  results/mixed_cubic_small_prime_rank_one_cartier_mass_hashes.sha256

# item 150
27b536024744191e2e0b76d319a949f34afb38f48f84c92e62d67c4e4248eb0d  sources/moving_ray_y5_minus_y_extended_theorem.md
0581212c4c004521e7f4bd0d14eeb470f6f12e68b3231880e6fda1714c8af6f6  results/moving_ray_y5_minus_y_extended_hashes.sha256

# item 151
9b34e9088d73a828af12b548f34e669f181d586c212edbf8e80c16ee37c83962  sources/mixed_cubic_rank_two_cartier_determinant.md
c0194fe0a2ad3b19ed8c4974a43b6c690aee3831cc3bd2bfbf9142e3f7f5c9da  results/mixed_cubic_rank_two_cartier_hashes.sha256

# item 152
101a2f44b3166c6ebebbe81e0f950a40b489eeb0352a601ea496082283fcd2bc  sources/moving_ray_uniform_2adic_and_cyclic_evidence.md
1aa935b6b07ed07e2b576d4cc7aeb70e75804586c0ced49d992b16b13009b291  results/moving_ray_uniform_2adic_hashes.sha256

# item 153
b92985ab3b54ec34a358258ffe3ba478b0c2d51040f4629f008ad88ea0594c7b  sources/mixed_cubic_valid_mray_cartier_reduction.md
1430bb8d337e3c858a3c1e05d2b78d6ee219a8fe5b933baca4af1d0fa726f98b  sources/corrected_mray_epsilon_projection_proof.md
7a052ed4c72b5e3f2d2bbd4b5dc94041d4004325b0684ff4bfdd2eb5bd055907  sources/weighted_cayley_recurrence_obstruction.md
6e47d1a3f2c8c284e3ee9c317c9ae1363173a969b4cd736cf5ec76c47beb55df  sources/weighted_cayley_three_term_no_go.md
294b0a523e2b0890c47cf565b76d0018c79b92ea6b6c2a576b23cc38e540a97f  sources/inverse_cubic_log_residue_obstruction.md
d095032d3667d0c7fdc5a2c80d63db820d493a5597f2fb4041a942e1bc7102fa  results/corrected_fresh_prime_structure_hashes.sha256
```

All 41 entries listed by the five item-149--153 manifests were independently
rehashed; every entry matched.  In particular, the two quantitative
certificate pairs are bound by

```text
286fde361ff66512dc41bdf39ef853bb6fd1d97582c59e8b2e5343dde190b41b  scripts/mixed_cubic_small_prime_rank_one_cartier_certificate.py
10991033ef60dece85f588cdc676a29bd5d1503ad2a28eb718c020f81dbdd6c3  results/mixed_cubic_small_prime_rank_one_cartier_certificate.json
96d3691e214fbd8690ecc4491370d511c176932f658e83b5253440114e87949c  scripts/mixed_cubic_rank_two_cartier_certificate.py
1fbc73c50ca83cdbbabef090460a944218dc1074a573b32555e4a009f2cb1b02  results/mixed_cubic_rank_two_cartier_certificate.json
```

## 3. Independent exact/interval recomputation

Let $a$ be the smaller positive root of



$$
128a^6-384a^5+280a^4-20a^3-55a^2+a+2=0,
$$



and define $\tau$ and $\Psi$ by the frozen saddle formulas.  Let
$x_*$ be the root in $(0,1)$ of
$5x^3+5x^2+5x-3=0$.  The exact formulas are



$$
\ell={\log|\Psi(\tau)|-7\log2\over6},
\qquad
\phi=\log x_*+\log(1-x_*)-{2\over3}\log((1+x_*)(1+x_*^2)),
$$





$$
\mathfrak C=-4\log2+{\pi\over\sqrt3}+3\log3,
\qquad
c_0={3\over2}\log2+{1\over2}-{\mathfrak C\over6},
$$





$$
h=2\ell+c_0,
\qquad d=\ell-\phi.
$$



Exact rational bisection of both algebraic roots, a rational Machin
enclosure for $\pi$, and directed interval evaluation of the logarithms
gave



$$
\begin{aligned}
2.3246783391437311102576951141305620522234564135413821
&<h\\
&<2.3246783391437311102576951141305620522234564135413822,\\
2.3370623743589729958539297805468573066534630858270130
&<d\\
&<2.3370623743589729958539297805468573066534630858270131,\\
1.1561471519642446123307302238571333988967248706278756
&<T\\
&<1.1561471519642446123307302238571333988967248706278757.
\end{aligned}
$$



These intervals independently certify



$$
d>h,
\qquad d<2h,
\qquad h-d/2>0.
$$



For a beta scale with $N\log N/(6m)\to t$, the ordinary positive-matching
ledger is



$$
\max\{h-t-\Gamma_*,\ t+h-d-\Gamma_*\}.
$$



It balances at $t=d/2$, giving $T-\Gamma_*$.  Thus:

- **PROVED:** with no exponential extra content, the method would require
  $d>2h$, which the certified constants contradict;
- **PROVED:** an internal/matching content theorem with
  $\Gamma_*>T$ would suffice for irrationality by this positive-matching
  route;
- **PROVED:** the stronger Roth-level threshold in the frozen matching note
  is $\Gamma_*>h$.

## 4. Rank-one and rank-two ledger

### Rank one

**PROVED.**  Item 149 gives



$$
\prod_{p\in\mathcal H_m}p\mid c_m,
\qquad
\log\prod_{p\in\mathcal H_m}p
=C_1m+o(m),
$$



where



$$
C_1=-4\log2+6\log3-3
=0.8190850097688769107025429357\ldots .
$$



Therefore



$$
\liminf {\log c_m\over6m}\ge r_1={C_1\over6}
=0.1365141682948128184504238226\ldots .
$$



The proof is all-$m$; the 102 archived coordinate rows are finite
normalization and endpoint checks, not its basis.

### Rank two

**PROVED.**  Item 151 classifies the next Cartier floor by the exact
determinant $\Delta_{q,s}$, and every vanishing row supplies one additional
squarefree factor after the existing $G_m$-division.  Its three proved
uniform zero rays contribute only $O(\log m)$, so the proved asymptotic
lower rate is still $r_1$.

**PROVED UPPER CEILING ONLY.**  The union of every possible rank-two floor
interval has PNT mass at most



$$
C_2=6-{\pi\over\sqrt3}-3\log3
=0.8903637697614530752201860316\ldots
$$



per $m$.  Hence even the impossible best case gives only



$$
{C_1+C_2\over6}
=0.2849081299217216643204548279\ldots
$$



per $6m$, leaving



$$
T-{C_1+C_2\over6}
=0.8712390220425229480102753960\ldots .
$$



It is invalid to add $C_2/6$ to the proved lower bound: $C_2$ is a
limsup ceiling on a containing interval union, not a proved mass of zeros.

## 5. Status ledger

- **PROVED:** item 149's one-digit divisor and its exact PNT mass.
- **PROVED:** item 151's rank-two determinant, post-$G_m$ divisor theorem,
  three thin zero rays, and absolute radical ceiling.
- **PROVED but rate-neutral here:** item 150 closes finitely many infinite
  fresh-prime rays; it supplies no positive post-$G_m$ content rate.
- **EXPERIMENTAL:** item 152's uniform 2-adic deflation pattern is checked on
  158 rows only.  Its recurrence and cyclic identities are proved, but the
  two-coefficient support theorem and odd-numerator control remain open.
- **EXPERIMENTAL:** item 153's scan through $m=1000$ finds power-of-two
  denominators and a scaled gcd dividing $(6m)!$.  No uniform divisibility
  or multiplicity theorem follows from that scan.
- **OPEN:** a positive-density or positive-mass theorem for the complete
  rank-two zero set $\mathcal Z_m$.
- **OPEN:** any modulo-$p^2$, crystalline, Witt-vector, or equivalent
  integral lift that forces additional valuations of the actual determinants.
- **OPEN:** enough total extra content to cross $T$; fresh-prime support
  exclusions alone do not control prime powers.

The decimal strings `0.13651416829481286...`,
`0.8903637697614535...`, `0.28490812992172176...`, and
`0.8712390220425228...` in the overview files are rounded binary64-style
approximations, not literal high-precision prefixes.  The exact symbolic
formulas are correct, and the corrected values above do not change any sign,
inequality, or theorem boundary.

## 6. Smallest open higher-prime-power lemma

With only the currently proved rank-one radical input, a sufficient purely
higher-power statement can be written without classifying individual primes.
Define



$$
\mathcal M_m^{\rm pow}
=\sum_p\max\{v_p(c_m)-1,0\}\log p.
$$



A clean sufficient aggregate multiplicity target is



$$
\boxed{
\liminf_{m\to\infty}{\mathcal M_m^{\rm pow}\over6m}
>T-r_1
=1.0196329836694317938803064012\ldots .}
$$



Indeed,



$$
\log c_m\ge
\log\prod_{p\in\mathcal H_m}p+\mathcal M_m^{\rm pow},
$$



so this scalar lemma alone would give
$\liminf\log c_m/(6m)>T$.  It makes no per-prime claim and is therefore
strictly weaker than demanding a fixed number of extra digits at every
qualifying prime.  A still weaker mixed radical/multiplicity lemma may replace
part of its right side by a separately proved positive rate for new
squarefree primes, but no such rate is currently available.  Even granting
the entire rank-two radical ceiling would leave
$0.8712390220425229480\ldots$ to be supplied by higher multiplicity or
deeper-rank structure.

A single generic assertion $v_p(c_m)\ge2$ on the rank-one set would add
only another $r_1$, far below the required deficit.  The open problem is
therefore a weighted mass theorem, not merely the existence of an isolated
second digit.

## 7. Most dangerous logical vulnerability

The top-layer identity has the form



$$
(q_pR,L,E)\pmod p
=\operatorname{Frob}^{e_p}
 \bigl(\mathcal Z(\mathcal C^{e_p}\bar\omega)\bigr),
\qquad q_p=p^{e_p}.
$$



Both Cartier and Frobenius here act in characteristic $p$.  The exponent
$e_p$ records how far the denominator layer descends before reduction; it
does not raise the modulus.  Consequently none of the following is currently
justified:



$$
p^{e_p}\mid c_m,
\qquad v_p(c_m)\ge e_p,
\qquad \Delta_{q_p,s}=0\pmod p\Longrightarrow p^2\mid c_m.
$$



Item 149's abstract coordinate examples show that the modulo-$p$ ledger is
sharp: the relevant minors can have exactly the one valuation supplied by
the theorem.  Any higher-digit claim needs a new integral lift with controlled
first error term, not another use of the same characteristic-$p$ identity.

Two related safeguards are mandatory:

1. the rank-two constant $C_2$ must never be booked as achieved content;
2. the original squarefree Cartier factor $G_m$ and the constant
   $\mathfrak C$ have already been spent in the normalization defining
   $h$.  They cannot be counted again inside
   $\Gamma_m=(6m)^{-1}\log(c_m\Delta_mg_m)$, and neither matching gcd
   $\Delta_m$ nor final content $g_m$ has a proved exponential lower
   bound.

The clean next local target is therefore a genuine modulo-$p^2$ endpoint
formula (or an equivalent integral cohomological lift) whose determinant
error can be shown to vanish on a set with a quantified weighted mass.  A
finite replay or an additional characteristic-$p$ Cartier iteration cannot
substitute for that lift.
