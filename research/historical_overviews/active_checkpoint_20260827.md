> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Active research checkpoint — 2026-08-27 UTC

This file is a resumable checkpoint for the active objective: prove, unconditionally
and rigorously, either that $e+\pi$ is transcendental or that it is algebraic.
No such proof has been obtained at this checkpoint.  In particular, none of the
conditional implications or finite computations in the archive is being promoted
to a classification.

## Archive-reading status

- `README.md` has been read completely.
- `research_log.md` has been read completely through its current final line
  before this checkpoint update; the subsequent lines are the independently
  audited additions recorded below.
- `sources/literature_status.md` has been read completely.
- The original 124 source notes, 105 source scripts (104 Python and one C++),
  and 108 result certificates have now been covered by three independent
  thematic audits: foundations/Padé/pullbacks; factorial digits/cyclotomic
  units; and Fourier/Bessel/quartic kernels.  Every original Python file parsed
  as an AST, every original JSON file parsed, and the C++ certificate passed a
  syntax check.  The post-audit additions described below have separate exact
  replays.

The current archive inventory is 262 Markdown notes under `sources`, 240 source
programs under `scripts` (238 Python and two C++), and 245 JSON certificates
under `results`, in addition to the top-level files and Python bytecode caches.

## Current rigorous frontier

The archive still contains no unconditional proof that $e+\pi$ is irrational,
algebraic, or transcendental.  Its strongest live arithmetic obstructions are:

1. The critical Fourier/Bessel matched construction is rigorously excluded below
   $k=(3/10)n\log n$ and above $k=(3/2)n\log n$.  Its remaining middle strip
   is governed by prime-power content in the Bessel endpoint denominator and by
   common final content outside a moving one-block prime band.
2. The quartic four-power construction has a rigorous phase-selected analytic
   asymptotic, but its primitive size depends on a selected Smith-coordinate gcd
   at prime powers dividing the endpoint quotient invariant.
3. The mixed cubic denominator $(1+x)(1+x^2)$ gives genuine rational
   $1,\pi$ forms and finite shrinking examples, but no contour theorem or
   endpoint-determinant gcd theorem has yet been proved.  Fixed-slope exponential
   approximation by itself is also not automatically strong enough to match the
   factorial-height Padé denominators for $e$.
4. The factorial-digit and cyclotomic-unit routes have exact local reductions but
   retain uncontrolled past-content or moving-prime selected-gcd problems.
5. The conceptual mixed $E/G$-value and exponential-period reductions land on
   presently unproved injectivity/intersection conjectures; they are not proofs.

## Post-log quartic Fleck theorem and repaired certificate

Two files postdate the top-level README/log freeze:

- `sources/quartic_boundary_weighted_fleck_valuation.md`
- `scripts/quartic_boundary_weighted_fleck_valuation_certificate.py`

The source proves, for every $m\ge1$,



$$
v_2(S_m)=m+s_2(m)+v_2(m)+1,
$$



and hence the two-primary denominator exponent
$3m-s_2(m)-v_2(m)-1$ for the first odd boundary coordinate.  A line audit
found the proof sound.  The original unlogged checker nevertheless failed at
$m=1$: its `odd_double_factorial(2r-1)` routine used `(2r-1)!` instead of
`(2r)!`.  The routine was corrected.  A second audit noticed that the field
labelled `S_normalized_odd_residue_mod_256` omitted the final reduction modulo
256; that diagnostic-only expression was corrected as well.  The exact scan
through $m=64$ was then run twice to independent output paths, and the results
were byte-identical.

Current SHA-256 values are:

```
0eb5e178c5fba5a52240e55257830eca97ea2639028e0c2d52e5cb0acfa37c50  sources/quartic_boundary_weighted_fleck_valuation.md
672d864cdbb91b3283a30ba8caf062601a52801b09919eb1e7fff01d0c7f96a6  scripts/quartic_boundary_weighted_fleck_valuation_certificate.py
834b52bc8e5003bcf0fb5f5cdb01189fc3fb83bfd3e95b8416914921e08804f9  results/quartic_boundary_weighted_fleck_valuation_certificate.json
```

This theorem removes only the previously conjectural dyadic valuation for one
quartic coordinate.  It does not control the other adjacent odd coordinates,
the odd rational endpoint, or the final determinant gcd, and therefore does not
classify $e+\pi$.

## Post-audit exact structural results

The following results were obtained after the exhaustive archive pass.  None is
a classification of $e+\pi$.

1. `sources/galois_balanced_two_log_full_norm_no_go.md` proves that the full
   absolute norm of the fixed cyclotomic two-log edge grows exponentially under
   the temporary algebraicity hypothesis.  Ordinary trace is zero, the natural
   nonzero trace collapses to the elementary exponential partial sum, and
   exterior powers either eliminate the target or vanish.
2. `sources/cyclotomic_multilog_galois_matching_no_go.md` gives the corrected
   all-conjugate matching obstruction for a full primitive-prime logarithmic
   orbit.  Centered sheets force the scalar target coefficient to vanish; an
   unbalanced orbit has an expanding conjugate; an even centered orbit leaves
   nonzero monodromy limits.  Formal character projectors do not evade the
   single-scalar Galois compatibility condition.
3. `sources/bessel_block_resultant_singleton_dichotomy.md` proves the unit-minor
   continuant transition law, identifies the thresholded high singleton sum as
   the smooth part of the largest diagonal Smith invariant, and proves that the
   first standard singleton-sensitive resultant is already at main product
   scale.  The exact reflection factorization
   

$$
P_{2n+1}(-n-1)=(-1)^np_nq_n
$$


   merely reproduces the unknown $q_n$-prime depth on primes dividing
   $q_n$.  A sufficient surviving target is $V_N(C)=o(N\log N)$, where
   $V_N(C)=\max v_p(q_n)\log p$ over the relevant block and smooth-prime
   range.  The exact example $v_{11}(q_{1359})=5$ has excess singleton depth
   three in the block $[680,1360)$.
4. `sources/algebraic_unit_two_log_n5_all_prime_counterexample.md` refutes the
   conjectured all-prime support theorem.  At
   $(p,d)=(109321,6219)$, an explicit prime ideal divides the two-log
   coordinate ideal; a characteristic-zero six-minor Smith computation gives
   ideal norm exactly $109321$.  The accompanying scan through $p\le200000$
   is labelled finite and is not used in the counterexample proof.
5. A new common-kernel identity has been proved.  For $H\in\mathbb Z[x]$,
   $a\in\mathbb Z$, and $f=a+(1+x^2)H'$, the constraint
   $A((1+x^2)H')=0$ gives
   

$$
\int_0^1 f(x)\left(e^x+\frac4{1+x^2}\right)\,dx
   =a(e+\pi)-B(f)+4(H(1)-H(0)).
$$


   An audit found that the first temporary search used an unsaturated joint
   integer nullspace.  A saturated-kernel reconstruction proves, with endpoint
   zeros imposed, that the exact output image is
   $8\mathbb Z\times2\mathbb Z$.  It also certifies the finite nonzero form
   

$$
461515305521655600(e+\pi)-2704421761901323052
   =5.12\ldots\times10^{-7}.
$$


   The rank-two quotient metric has the ordinary Dirichlet/Minkowski balance:
   determinant/capacity alone reaches linear-form exponent one, not a
   Roth-breaking exponent.  This does not exclude exceptional vectors, but no
   infinite nonvanishing or exceptional-rate theorem is known.
6. A separate exact two-form quotient audit proves that two simultaneous
   nonproportional small forms would imply irrationality, but also identifies
   the precise noncircular threshold.  With $\lambda_1,\lambda_2$ the quotient
   minima and $\Delta_D$ the normalized covolume, Minkowski gives
   $2\Delta_D\le\lambda_1\lambda_2\le4\Delta_D$.  For a hypothetical rational
   value $e+\pi=p/q$, the exact zero direction $(8q,-8p)$ forces
   $\lambda_2\ge1/(5q)$ and $\lambda_1\le20q\Delta_D$.  Hence the desired
   estimate $\lambda_1/\Delta_D\to\infty$ already contains the missing
   irrationality input; determinant/transference alone is circular here.
   Exact finite degree-40 forms are independent and both about $10^{-7}$, but
   no all-degree decay theorem follows.  Endpoint-multiplicity and perfect-square
   positivity ansatzes are also excluded by factorial lower bounds.
7. A $p$-adic Subspace-Theorem criterion now turns coefficient support into a
   genuine transcendence conclusion.  For a fixed finite $\mathcal S$,
   primitive $Q\to\infty$, and fixed $\eta>0$, it is enough that
   $|Q(e+\pi)-P|P_{\mathcal S^c}Q_{\mathcal S^c}\le Q^{1-\eta}$ infinitely
   often.  A quantitative moving-support block theorem permits
   $s_j^6\log(s_j+2)=o(\log M_j)$.  Factorial-digit forms already satisfy
   $|\Lambda_{a,b}|\le Q_{a,b}^{1/2}$ uniformly in their full admissible
   range; their remaining gap is an all-prime support theorem for both
   primitive coefficients plus distinct unbounded height.  No archived family
   presently supplies it.
8. The saturated fixed-$(N,m)$ multi-exponential Hermite--Padé system has exact
   primitive scales $\log H=n\log n+O(n)$ and
   $\log|R|=-mn\log n+O(n)$.  Under hypothetical algebraicity of $e+\pi$,
   however, its evaluated generators $e$ and $e^{i(e+\pi)/N}$ are algebraically
   independent by Lindemann--Weierstrass.  Coefficient norms and Fourier
   projections therefore remain transcendental values; an $(m+1)$-row
   elimination spends exactly the exponent-$m$ gain; and the canonical
   adjacent/type-II determinant clears to a growing integer multiple of $e^U$
   (or an algebraic endpoint monomial of full norm at least one).  This is an
   exact barrier for the fixed-parameter mechanism, not a classification.
9. The nonnegative common-kernel cone has a uniform endpoint-bootstrap lower
   bound.  For every integer polynomial of exact degree $n$ with $f(i)\ne0$,
   its interval norm has exponential liminf at least
   $R^{-1/2}=0.4656665\ldots$, where $R=4.611581789\ldots$.  A nonnegative
   common-kernel integral inherits this lower bound up to a polynomial factor,
   so before normalization its coefficient growth consumes every positive
   decay exponent.  This does not survive automatically after division by
   $\gcd(a,b)$; an all-degree content theorem remains the precise missing
   arithmetic input.
10. Factorial-digit blocks have full projective saturation but only rank two.
    Their exact lattice is
    $\langle V_a,(\gcd(c_{a+1},\ldots,c_{a+B}),0)\rangle$; after primitive
    normalization, unrestricted combinations yield every rational pair and
    therefore reduce to the original approximation problem.  Untouched
    denominators obey an exact two-index factorial divisibility and support
    dispersion law.  A proved surviving criterion is
    $\sum_{p\mid q_n}\log p/(p-1)\le(1/2-\varepsilon)\log n$ infinitely
    often (or $P^+(q_n)\le n^\theta$, $\theta<1/2$), which would imply
    transcendence by Roth.  No theorem establishes that support condition.
11. The Bessel denominator has an exact exponent-doubling index law:
    $q_{n+2p^a}+2q_{n+p^a}+q_n\equiv2p^{2a-1}q_n\pmod {p^{2a}}$.
    Its index slope satisfies
    $\delta_{p^a}(n)\equiv\delta_p(n)-q_n\pmod p$, so ordinary roots lift
    uniquely forever and all singularity is inherited from level $p$.
    This improves the root count to
    $O_p\le R_{p^a}\le O_p+p^{a-1}S_p$, but does not control the digit depth
    of a unique ordinary branch.  Separately, the Padé argument root at
    $x=1$ is always Hensel-simple; its exact resultant and coefficient height
    show why that different simplicity gives no index-height saving.

The common-kernel package was subsequently repaired for Markdown escaping and
replayed twice byte-identically.  Its authoritative hashes are:

```
a7dadecb10eded8f3e683636480c086f28c6dacfc7023d5a488dbdf3ce7ee192  sources/common_kernel_lattice_identity_and_capacity_audit.md
5cf732291f8a0879cc8cbb5927edf0e726bfdb3b11ec3134fc98b3418f710110  scripts/common_kernel_lattice_exact_certificate.py
4824876c62b09ae9f1e46aa9278917e49487c53b8e1ed93fb8a520977742127a  results/common_kernel_lattice_exact_certificate.json
```

The later two-form quotient package was independently compiled and replayed
byte-identically.  Its hashes are:

```
4fcf62e0cf809aa22a7141ba90d02eee0a221c50901f2b7cf5fa0b7ef23f0033  sources/common_kernel_two_form_quotient_audit.md
cb15028325b9033a6e304ffc308e2aa2ba44ea7257190ff36ef5cd30b740590a  scripts/common_kernel_two_form_certificate.py
4d6a8dd6a677bcffa7d74c4742ef5a5719477542d25c7b120f8b08ec29ba4f78  results/common_kernel_two_form_certificate.json
61ce9226bdeaedf6e804d564f3240b96d4e07c2b18017161b23ab34235bfd5c7  scripts/common_kernel_quotient_ellipsoid_diagnostic.py
4229e190aeba7cabe88fcf0d75377c497c1a98536b01a808c1701546162d438e  results/common_kernel_quotient_ellipsoid_diagnostic.json
```

The prime-support source was checked against the primary quantitative theorem.
Two TeX escape defects were repaired during integration; its current hash is:

```
384c195a8e113a817f9bbc08ad68b9eca1733491a99508cbfc53d76d8d7c637c  sources/padic_subspace_prime_support_transcendence_criterion.md
```

The multi-exponential package was compiled and replayed byte-identically.  Its
current hashes are:

```
679e8587e94f1563920bb6635b387c00732480deb1ac14d79df22df31aec6529  sources/nested_multi_exponential_hp_norm_barrier.md
79fd558addcb9818c0138241ccdbb7eb2b660405bea4a2b31bf94ff5c3f3ce01  scripts/nested_multi_exponential_hp_certificate.py
d04d2cedf77de24e65feaa8ded28aa15539f0fd2153d62ca17e407e6f3adc63e  results/nested_multi_exponential_hp_certificate.json
```

The positive common-kernel endpoint-bootstrap package was compiled and
replayed byte-identically.  Its current hashes are:

```
596e21e493f16447307764b100bae383f5a639c7ad466150a50932b4a878d487  sources/common_kernel_positive_cone_endpoint_bootstrap_barrier.md
ca1db0bc142979bb9e566d5a93664ae3bcb914c9ec7aaa698e3f36c3b2171d4e  scripts/common_kernel_positive_cone_endpoint_bootstrap_certificate.py
35cf99fe9eb6e4a2203d2c357a3a04b36478628bce686a4907bb3dcd6e248a3d  results/common_kernel_positive_cone_endpoint_bootstrap_certificate.json
```

The factorial-digit projective-saturation and support-gap package was read,
compiled, and replayed byte-identically.  Its current hashes are:

```
f245c5fa5dc9b8a673f7dd6456bfc9266913a8edb138fb40929153ee9975dae5  sources/factorial_digit_integer_combination_support_barrier.md
ed44a627bc0cf05a7471d1db5bfe12c0c5988fa731696d8c47226b5920cf4fc9  scripts/factorial_digit_combination_support_certificate.py
d0d684d487c13a8f533dd97f628b070ef0f622166f5f7aab34413a4732755c4b  results/factorial_digit_combination_support_certificate.json
```

The two Bessel Hensel/index-lift packages were read in full, their delicate
initial-value and slope-inheritance calculations were independently checked,
and both certificates replayed byte-identically.  Their current hashes are:

```
f08816f9bbbe96f6ea5ba09efed8d6f4dd84d69e282d699ff56622afcd06933d  sources/bessel_pade_argument_hensel_exact_no_go.md
d25ce8aaba60055fde8a27503b4223b11f634b95e23e761761ae380e930633e7  scripts/bessel_pade_argument_hensel_certificate.py
59f3437099aa2a483ffbb683102690009e4c1f7f39157f89d71a926a2281939f  results/bessel_pade_argument_hensel_certificate.json
95f68e65b3a7458b869cdf610a28e77a9062e1467d78747dc2809563e84a2ee1  sources/bessel_prime_power_second_antiperiod_double_lift.md
3ddb35fe31696478d46321b71bdf90d0b64a21ae92f4a6fbde0f286b48f19396  scripts/bessel_prime_power_second_antiperiod_certificate.py
c9145c3911f04010a68707a5cbbf3da4f6a420e24888c173205d885e48b58115  results/bessel_prime_power_second_antiperiod_certificate.json
```

After integrating all post-audit files, a whole-archive integrity pass parsed
all 107 Python programs as ASTs and all 112 JSON results, found no illicit
control bytes in the 129 source notes or three top-level Markdown files, and
passed the C++ syntax check.  Fresh replays of the common-kernel, new-prime, and
Bessel certificates matched their frozen JSON files exactly; the new-prime
stdout and archived JSON had the identical SHA-256
`1383db00767615638db0a9a5c9475a0cd712478ad9f81a60a8e143dcf4b4fddd`.

## Immediate continuation protocol

1. Re-run the whole-archive AST/JSON/syntax inventory after every new frozen
   certificate and compare each embedded source/script hash.
2. Recheck the latest live constructions against the actual requirement of a
   transcendence proof, not merely a finite small form or irrationality criterion.
3. Pursue either a genuinely exceptional useful-quotient vector theorem or an
   arithmetic amplification (for example, a fixed-place Subspace/Ridout input)
   that can turn weaker real decay into transcendence; generic rank-two geometry
   cannot suffice.
4. Select one narrowly stated new lemma with a plausible all-degree proof;
   independently audit every normalization and content step before integration.
5. Append only proved results to `research_log.md`; keep diagnostics explicitly
   finite and conditional statements explicitly conditional.

## Post-checkpoint theorem packages (2026-08-27 UTC)

12. The signed Bessel denominator sequence (f(n)=(-1)^nq_n) has a unique
    (1)-Lipschitz continuation (f_p:\mathbb Z_p\to\mathbb Z_p). Its Mahler
    coefficients are

    

$$
A_j=(-1)^j j!\sum_{m\le j/2}\frac{(-1)^m}{m!}
                  \binom{2j-2m}{j},
$$



    with (j!/\lfloor j/2\rfloor!\mid A_j) and exact limiting lower
    valuation slope (1/(2(p-1))). The continuation satisfies

    

$$
f_p(x+2)+(4x+6)f_p(x+1)-f_p(x)=0.
$$



    At every ordinary zero ρ in a residue class (r\pmod p),
    (v_p(q_n)=v_p(n-\rho)) for (n\equiv r\pmod p). This converts the
    remaining high-valuation tail exactly into a rational-approximation
    problem for the digits of a (p)-adic analytic zero. It does not bound
    that digit depth: Strassmann and simple Hensel lifting count roots, whereas
    the missing estimate is a uniform non-Liouville bound such as
    (v_p(n-\rho)\log p=o(n\log n)).

13. The same continuation has the uniformly convergent parameter identity

    

$$
f_p(x)=\sum_{k\ge0}\frac{(-x)_k(x+1)_k}{k!}
          ={}_2F_0(-x,x+1;;1),
$$



    and each term has valuation at least
    (v_p((2k)!)-v_p(k!)). It is a Newton series in (x(x+1)) and satisfies
    (f_p(-x-1)=f_p(x)). On an ordinary root the quadratic coordinate is a
    local isometry. Raw truncations cannot give the needed height saving:
    below the first term containing the factor ρ−n, retaining depth (a)
    already forces truncation length comparable with (a); at length at least
    (n), evaluation at (n) freezes to ((-1)^nq_n), with the full
    (n\log n) height. The exact certified retained depth is at most half the
    target depth up to a logarithmic carry term.

14. A root-of-unity constrained Hermite–Padé construction removes the second
    transcendental generator at the endpoint. Writing

    

$$
R(z)=S(z)+(1+e^z)B(z),\qquad \deg S\le D,
$$



    gives (R(i\pi)=S(i\pi)=S(i(s-e))) if (s=e+\pi) is algebraic. The
    constrained dimension is (m(n+1)+D+1), and the expected vanishing order
    is (m(n+1)+D). For (m=1) the construction is completely proved as a
    Padé problem for (1/(1+e^z)). If (d=\lfloor D/2\rfloor) and (D) is
    fixed, its primitive endpoint polynomial satisfies

    

$$
\frac{|S(i\pi)|}{H(S)}=\Theta_D((2d+1)^{-n}).
$$



    For (D=2), its denominator is the exact tangent-number quotient

    

$$
Q_r=\frac{\tau_{r+1}}
             {\gcd(\tau_{r+1},8r(2r+1)\tau_r)},
$$



    and 
    
    

$$
|S(i\pi)|=(8\pi^2/9+o(1))Q_r9^{-r}.
$$



    On the diagonal (D=n), both (log H(S)=n\log n+O(n)) and
    (-\log|S(i\pi)|=n\log n+O(n)). The endpoint repair is real, but fixed
    degree retains factorial primitive height and diagonal degree consumes the
    gain in every presently available measure for (e).

15. The endpoint reduction has been compared with an explicit polynomial
    lower bound at (e). Under (s=e+\pi) algebraic of degree (r), a
    polynomial (P\in\mathcal O_{\mathbb Q(s,i)}[X]), of fixed degree at most
    (D) and house (H), satisfies

    

$$
|P(e)|\ge H^{-(r^2D+r-1+o(1))}.
$$



    The relative-norm reduction, coefficient height, the (D=0) case, and
    the exceptional linear continued-fraction case were checked separately.
    Consequently the constrained family would prove transcendence at fixed
    (D) if its endpoint exponent beat (r^2D+r-1). In particular, for
    (D=2), subexponential (Q_r) along an infinite subsequence would suffice;
    current exact data instead show factorial growth and no theorem supplies
    the required tangent-number gcd. For growing (D), the degree factor in
    the lower bound destroys the diagonal gain.

The four packages above were read in full, their symbolic scripts were
compiled and replayed byte-identically, and their authoritative hashes at
this checkpoint are:

```
a50f45248133e437ee318b8cc28e6bbcc51de3568f3e621043221c90ddb4f348  sources/bessel_padic_index_interpolation_analytic_height_barrier.md
46f27500593c5804ce1978a79de0d16a9ef217cec21bfcd2255fd1a03a3c93d8  scripts/bessel_padic_index_interpolation_certificate.py
8b260695bf95b1c2a2c8196d3577dafe4948d5a85a084e44c6307de6b02e276e  results/bessel_padic_index_interpolation_certificate.json
a78e0a3588dd02197d1dc5e2aec1ab5988c4ae78a2a6f86e0af65623e092d96d  sources/bessel_padic_hypergeometric_zero_pade_barrier.md
99e40135972e4f3665d07e460cd4e8443d40d5e7b41bbc6cdce8d2d5c24820fb  scripts/bessel_padic_hypergeometric_zero_pade_certificate.py
bed72438f9c8a590542582c39c21a8c0b4bbdcd309bbb81167c3e906d391296c  results/bessel_padic_hypergeometric_zero_pade_certificate.json
c3d93dccb926ef3fbf2165c3b9aa8d3809a7014c44538589bfd31f724f3da82b  sources/root_unity_constrained_hermite_pade_audit.md
37a4aac6d832e0c5c5d2580bcb3c8f1861d8676eeccba4a119563ac62aba7389  scripts/root_unity_low_degree_hp_certificate.py
74d7fa0641132aac6ba424015371aa78ed35f30e97cf3d9fff43b9b1474c31a6  results/root_unity_low_degree_hp_certificate.json
d53e940de2e9567c1668dffbd03de021d33aaf29f9b54c4787d6cd6d85701bd6  sources/root_of_unity_low_degree_polynomial_e_measure.md
79e45045696003a485515a2bc61523f3cdfe40deb1e00fba70d129eb5ea96ae1  scripts/root_of_unity_polynomial_e_measure_certificate.py
846361683d75aceb7baa8162336425e7734ebddb24e28d0ac8935a382bbed589  results/root_of_unity_polynomial_e_measure_certificate.json
```

These are structural advances and certified exclusions of several tempting
shortcuts. They do not yet classify (e+\pi). The live research targets are
(i) a genuinely sharper auxiliary construction for the ordinary (p)-adic
Bessel zero, (ii) a higher-multiplicity/root-of-unity endpoint family whose
primitive decay beats the degree-dependent lower bound, or (iii) a theorem
turning the high Bessel prime-power branch into a support-amplified target
form while controlling both primitive coefficients.

## Second post-checkpoint reduction pass (2026-08-27 UTC)

16. The proposed dichotomy “small Bessel prime powers prove the archimedean
    estimate, while a main-scale fixed prime proves the (p)-adic criterion”
    fails for the fully matched critical-Fourier family. Write
    (q=p^au), (B=p^bv), (d=\gcd(q,B)=p^{\min(a,b)}d_0),
    (M=q_0A-B_0r), and (g=\gcd(M,d)=p^tg_0). The final primitive pair has

    

$$
v_p(Q)=\max(a,b)-t,\qquad v_p(P)=v_p(M)-t,
$$



    and exact outside parts

    

$$
Q_{\{p\}^c}=\frac{uv}{d_0g_0},\qquad
    P_{\{p\}^c}=\frac{|M|/p^{v_p(M)}}{g_0}.
$$



    If (a\ne b), then (v_p(M)=t=0), and a hypothetical main-scale
    root (\log u=o(n\log n)) still gives
    (\Lambda\ge\mathcal L/u\to\infty). The apparent exact-resonance
    escape is also impossible. For (n=2r), (K=k-1), the central Fourier
    coefficient has the exact positive super-Catalan factorization

    

$$
C_0=\mathcal S(r,K-r)\frac{F_r(K)}{D_r(K)},\qquad
    0<F_r(K)<(8K)^r.
$$



    Legendre's digit-sum formula and
    (B=\operatorname{lcm}(1,\ldots,K)C_0/h) therefore give, for every
    fixed odd prime (p),

    

$$
v_p(B)\log p\le \frac n2\log(8K)
       +4(1+\lfloor\log_pK\rfloor)\log p.
$$



    In every critical window this is
    ((1/2+o(1))n\log n), whereas a main-scale ordinary Bessel root has
    (a\log p=(1+o(1))n\log n). Thus (v_p(B)=a) is eventually impossible,
    and (\Lambda\ge\mathcal L/u\to\infty) throughout the critical range.
    Together with the accepted low- and very-high matching theorems, this
    covers every (k>n). More fundamentally, for support
    (\mathcal S=\{p\}), primitivity forces
    (P_{\mathcal S^c}Q_{\mathcal S^c}\gg Q), so the Subspace criterion
    always requires (\Lambda\ll Q^{-\eta}). A divergent form cannot be
    rescued by denominator concentration at one prime. This is a no-go for
    the fully matched critical-Fourier construction, not for arbitrary
    non-raw auxiliary families.

17. Growing the number of exponentials at fixed endpoint degree has an
    all-parameter (D=2) reduction. With

    

$$
\Phi_{m,n}(X)=\prod_{j=0}^{m-1}(X-j)^{n+1},\quad
    \varepsilon\equiv mn\pmod2,\quad
    \Psi=X^\varepsilon\Phi,
$$



    and (\mathcal L(Q)=Q(d/dz)(1+e^z)^{-1}|_{z=0}), the canonical even
    endpoint is

    

$$
S(z)=-\mathcal L(\Psi'')+\mathcal L(\Psi)z^2.
$$



    MacMahon's multiset-Eulerian identity and Simion's simple-negative-root
    theorem prove (\mathcal L(\Psi)\ne0) for every (m\ge1,n\ge2).
    An exact Mittag–Leffler quotient shows that the contributions of the
    first poles (\pm i\pi) cancel from the rational approximation to
    (\pi^2); the next poles are (\pm3i\pi). For every fixed (D), however,
    Aleksentsev's algebraic approximation measure gives

    

$$
|C(i\pi)|\gg_D H(C)^{-K_\pi(D)}
$$



    for all nonzero integer (C) of degree at most (D). Thus varying
    (m,n) cannot force an unbounded primitive endpoint exponent at one
    fixed (D). This does not rule out a specified finite exponent for a
    specified hypothetical degree, coupled (D\to\infty), or determinants
    of several independent endpoints. Higher endpoint multiplicity has the
    same pole locations, and common shifts of arbitrary integer frequency
    sets change the primitive endpoint only by sign.

18. A complete current-literature audit of (E)-, (G)-, and logarithm-value
    theorems yields a forced Borel-collision theorem. Under
    (s=e+\pi\in\overline{\mathbb Q}), if (E)-functions (F,G) and
    nonzero algebraic (x,y) satisfy (F(x)=e), (G(y)=\pi), then Delaygue's
    theorem forces

    

$$
\frac{\rho_F}{x}=\frac{\rho_G}{y}
$$



    for some finite inverse-Borel singularities
    (\rho_F\in\mathfrak S(F)), (\rho_G\in\mathfrak S(G)). In particular,
    every exact (E)-function interpolant (G(y)=\pi) must satisfy
    (y\in\mathfrak S(G)), because (\mathfrak S(e^z)=\{1\}). Likewise,
    (F(x)=e^\eta) with algebraic (x,\eta\ne0) forces
    (x/\eta\in\mathfrak S(F)), exactly the exceptional branch of the
    Fischler–Rivoal logarithm theorem. Under the same hypothesis,
    (e,\pi\) would be transcendental elements of the still-conjectural
    value-ring intersection (\mathbf E\cap\mathbf G). Current Beukers
    specialization, interpolation, mixed (p)-adic functional independence,
    algebraic-independence measures, and (E)-period structures all retain
    an exact zero/functional-dependence branch and do not contradict this.

The authoritative hashes for this second pass are:

```
c0767ccb9d9cdf9e5779087fb21092ec14308ec8f44d04c839f3f25945da1508  sources/bessel_fixed_root_fourier_single_prime_subspace_barrier.md
e195a8d3960918d0096002ac9010619bdd1aa1a7b0012ca3ab254695d08624b4  scripts/bessel_fixed_root_fourier_single_prime_certificate.py
ae445b4222d18c25486388520c5df3ea9661d13dacf00c05474598c20be71009  results/bessel_fixed_root_fourier_single_prime_certificate.json
661b8751b8689a21ce93ed171419d4f148175b5e1a5dd1137ae32b87a2cb149e  sources/root_unity_fixed_D_growing_m_obstruction.md
bd01de829f498f26fcbbc27643b532b4f73e00913cdccfe273b8475f3ea83cb2  scripts/root_unity_D2_growing_m_certificate.py
632858c3e02207be13bd8dfceac9ad5aec641384433a84f506e555592f52e7d3  results/root_unity_D2_growing_m_certificate.json
8bbcd71ffba7076ea09b39849fca825c957e33886703fac3bd7530d62f06ed56  sources/independent_mixed_e_g_logarithm_value_audit.md
f5ba325e9a2b2c2971a2c5076641bb8af1d28cf97d5e18d2b94af229b77d1cb4  results/independent_mixed_e_g_logarithm_value_audit.txt
```

The Bessel and (D=2) scripts were independently replayed after central
proof audit. The mixed-value package is a theorem/provenance note with a
compact hash manifest rather than a computational certificate. None of these
results classifies (e+\pi); they sharply remove three false shortcuts and
leave coupled-degree/multi-endpoint, genuinely non-raw (p)-adic auxiliary,
and low-order mixed-connection questions active.

## Third post-checkpoint reduction pass (2026-08-27 UTC)

19. The coupled-degree/multi-endpoint exterior proposal has an exact
    rank-one obstruction. For $\nu$ independent endpoint polynomials
    $C_j\in\mathbb Z[z]_{\le D}$, the canonical divided-derivative
    Wronskian

    

$$
W_\nu(z)=\det(C_j^{[a]}(z))_{1\le j\le\nu,\,0\le a<\nu}
$$



    has actual degree

    

$$
d=\sum_{j=1}^{\nu}d_j-\frac{\nu(\nu-1)}2
      \le\nu(D-\nu+1),
$$



    where $d_j$ are the pivot degrees of the saturated endpoint space.
    Its primitive coefficient content is basis-independent. Under
    $s=e+\pi\in\overline{\mathbb Q}$,
    $\delta^d\widetilde W_\nu(i(s-X))$ is an integral polynomial in
    $X$ over $\mathbb Q(s,i)$, and the exact relative-norm inequality
    is recorded in the source. However, in
    $R_j=C_j+(1+e^z)B_j$, only the value column is inherited at
    $i\pi$; $\nu$ small scalar values therefore contribute only one
    small determinant factor. At top rank $\nu=D+1$, the Wronskian is
    exactly the coefficient determinant and primitively $\pm1$. Higher
    endpoint multiplicity supplies at most
    $q=\min(h_{\rm end},\nu)$ inherited jet columns, but under the stated
    noncollapse scales the required gain retains a cost at least
    $r^2D$. An exact 460-tuple grid found only unit degree defects and
    exterior content at most six; this finite observation is not promoted
    to an asymptotic theorem.

20. The non-raw Bessel shift/$\Sigma$-operator routes have an exact
    scoped exclusion. For $f(n)=(-1)^nq_n$, Rivoal's morphism sends

    

$$
1+(4n-2)\sigma-\sigma^2
      \longmapsto 4z^2\frac d{dz}+1+2z-z^2,
$$



    which is irregular at zero. More strongly, $f(n)$ has factorial
    growth and a radius-zero ordinary generating series, so it cannot
    eventually satisfy any $\Sigma$-operator. Every finite polynomial
    shift form reduces exactly to

    

$$
A(x)f_p(x)+B(x)f_p(x+1),
$$



    and at an ordinary root $\rho$, the boundary value
    $f_p(\rho+1)$ is a unit. Thus its valuation is exactly
    $v_p(B(\rho))$. Shift determinants similarly reduce to the
    determinant of their $B$-polynomial matrix. Formal root preservation
    forces a factor $q_n$ at integer indices and hence the full
    $n\log n$ height; the other branch is merely the still-open
    residual-polynomial approximation problem. Parameter jets do not
    evade it: already
    $f_p'(0)=-\sum_{m\ge0}m!$, importing Euler's fixed-prime
    $p$-adic factorial constant.

21. The elementary mixed $E/G$ pair is now completely explicit. Under
    the test hypothesis $s=e+\pi\in\overline{\mathbb Q}$,

    

$$
(1,e^z,s-4\arctan z)^T
$$



    solves a rational rank-three system ordinary at $0,1$, with
    algebraic initial data, Picard--Vessiot group
    $\mathbb G_m\times\mathbb G_a$, and algebraically independent
    nonconstant coordinates over $\overline{\mathbb Q}(z)$; nevertheless
    those coordinates coincide at $z=1$. Its normalized connection
    matrix contains $e$ and $-\pi$, and its monodromy contains
    $\mp4\pi E_{31}$. The closed $E$-system built from
    $L_s=s(1-e^{-z})-2\operatorname{Si}(z)$ places $\pi$ only in a
    limit/Stokes constant at infinity. Moreover its inverse Borel transform
    satisfies the exact collapse

    

$$
2\psi(L_s)(t)-(s-4\arctan t)=s\frac{t-1}{t+1}.
$$



    Thus it is only a rational perturbation, vanishing at the target, of
    the original $G$-interpolant. Functional independence, ordinary-point
    regularity, solvable Galois group, monodromy, and current connection or
    Stokes theorems do not supply the missing numerical mixed-period
    injectivity.

The authoritative hashes for this third pass are:

```
18db8252a651f692f55dc2f44c7fa8bede9d33d29cf86525714406c88b7ca8e5  sources/root_unity_endpoint_exterior_power_audit.md
b233dea8890e530f0017958bca9cfdbbb7a072d617b4c922afb62cde0cf08313  scripts/root_unity_endpoint_exterior_certificate.py
f0b3dac47625930a698c2bb5f69ef79b8b9e89380f32c18d9d19dd6b5f753a52  results/root_unity_endpoint_exterior_certificate.json
074e8bc290f37e14eccbe38f2068e4a0ca775162afb0643511483b08300950e7  sources/bessel_parameter_hermite_pade_sigma_operator_barrier.md
021952bfa6729962a238c1eeda7466ccad2bd7dc48de59b8cd52a2809bf77c7b  scripts/bessel_parameter_hermite_pade_sigma_certificate.py
fbb6a8840614b4aed0113e5ff83ecffa1d6a3cd37b454609e8b22f23ec18ba10  results/bessel_parameter_hermite_pade_sigma_certificate.json
81dc71a0ed4fcb2a4a32ab04b749644ecd0b3bbc14a4f3ac6b183e311086c2f7  sources/explicit_low_order_mixed_pair_monodromy_stokes_audit.md
44d54f11d2662665ff90acc2ab786b2d87154771da6e4cefb606f838a6bb3b33  scripts/explicit_low_order_mixed_pair_certificate.py
b834488e904487ea09fe0de80ecdc5364afb18337dcc59d1df4cc6be8988403a  results/explicit_low_order_mixed_pair_certificate.json
```

All three computational packages were independently replayed byte-for-byte
after central proof audit. These results do not classify $e+\pi$. They
close the naive exterior determinant, finite-shift/$\Sigma$, and explicit
low-order mixed-system shortcuts, leaving noncanonical multiple inherited
endpoint columns, genuinely new Bessel tail transforms, arithmetic residual
polynomials, and mixed connection-period injectivity as exact survivors.

## Fourth post-checkpoint reduction pass (2026-08-27 UTC)

22. The entire integer common-kernel plane now has a lossless Stein--Robin
    parameterization. With

    

$$
A(F)=\sum_{k\ge0}(-1)^kF^{(k)}(1),\qquad
    \mathcal TP=(1-x)P'-xP,
$$



    the operator $\mathcal T$ is an integral bijection from
    $\mathbb Z[x]$ onto $\ker A\cap\mathbb Z[x]$. Hence
    $A(F)=F(\pm i)=a\in\mathbb Z$ if and only if

    

$$
F=a+\mathcal TP,qquad
    P=(1+x^2)^2Q+u(1+2x+x^3)+v(9x-x^2+4x^3),
$$



    for unique $P\in\mathbb Z[x]$, with $Q\in\mathbb Z[x]$ and
    $u,v\in\mathbb Z$. Writing
    $G_P=\mathcal TP/(1+x^2)=\sum g_jx^j$, the exact output is

    

$$
a(e+\pi)-a-P(0)+4\sum_j\frac{g_j}{j+1}.
$$



    The unconstrained ODE has an exact positive integral near miss:

    

$$
a_N=N!,\quad
    P_N=N!\sum_{j=0}^{N-1}\frac{(1-x)^j}{(j+1)!},\quad
    a_N+\mathcal TP_N=(1-x)^N.
$$



    Its weighted integral tends to zero, but it fails precisely the two
    exterior Robin conditions, since
    $\mathcal TP_N(i)=(1-i)^N-N!\ne0$. Thus positivity, integrality, and
    decay coexist before the endpoint constraint. Moreover, a real-part
    comparison proves that no nonconstant residual with nonnegative
    $(1-x)$-monomial coefficients can satisfy the common endpoint equality,
    so positive combinations of these Taylor blocks cannot repair it. The
    exact survivor is an all-degree correction with signed monomial
    coefficients, inside the displayed Robin lattice, which remains
    nonnegative on $[0,1]$ and preserves decay after primitive
    normalization.

23. Noncanonical two-column endpoint inheritance is governed by an exact
    module criterion. For algebraic-coefficient Laurent polynomials,

    

$$
\operatorname{ord}_{z=i\pi}F(z,e^z)=v_{y+1}(F).
$$



    Individual inheritance of $q$ jets therefore already requires the
    factor $(y+1)^{q-1}$. For two coupled endpoints the determinant
    correction is

    

$$
\Gamma_{C,D}=C\beta_D-D\beta_C,qquad
    \beta_C=T_C(z,-1),
$$



    and two-column inheritance is equivalent to $\Gamma_{C,D}=0$.
    Whenever
    $n+(2-m)D-\nu+2\ge0$, a zero estimate forces the full identity
    $CT_D-DT_C=0$; both forms are polynomial multiples of one common
    remainder, so the determinant is only a square/product of one direction.
    This covers the natural $\nu=2$ family for every $m\le3$. For
    $m=1$, the only exception occurs when $n$ is even and $D$ odd,
    and it is exactly $W=C_0^2$. The remaining genuine range is
    $m\ge4$, $n<(m-2)D$, where a structured secondary exponential
    polynomial would need exceptional origin order.

24. The residual Bessel problem also survives neither canonical Mahler nor
    residue-grid Newton coordinates. The global truncation has the exact
    same-sign formula

    

$$
S_K(n)=(-1)^K\sum_{i=0}^K
      \binom ni\binom{n-i-1}{K-i}q_i
$$



    and lies between $\binom nKq_K$ and
    $2^K\binom nKq_K$. Its available termwise root estimate is

    

$$
v_p(S_K(n))\ge\min(D_K,a-V_K),qquad
    D_K-V_K=O(\log_pK),
$$



    so that method certifies at most $a/2+O(\log_pK)$. The first Mahler
    term containing $x-n$ already costs at least $q_{n+1}$. On the
    $p$-step grid, coefficients satisfy
    $q_{r+pj}\le|C_j|\le2^jq_{r+pj}$, and the first term seeing $n$
    costs $q_{n+p}$. Diagonal Amice rescaling changes no evaluated term.
    Finally, the recurrence has no nonzero polynomial quadratic invariant or
    anti-invariant, and its canonical Hankel determinant is a unit at every
    ordinary root. The exact survivor is a genuinely nontriangular residual
    polynomial with high value at $\rho$ and sub-main primitive
    $\ell^1$-height.

25. Tensor, exterior, split stabilization, and rational gauge operations on
    the explicit mixed system cannot create the missing numerical theorem.
    Every tensor-category matrix coefficient lies in

    

$$
\overline{\mathbb Q}(z)[e^z,e^{-z},-4\arctan z].
$$



    Monodromy proves that an $E$-function in this ring is independent of
    $\arctan z$, while regular-singular growth at $\pm\infty$ proves
    that a $G$-function in it is independent of $e^{\pm z}$. The
    smallest visible tensor coupling contains $e\pi$, not a new pure
    coordinate. For every rational gauge regular and invertible at $0,1$,

    

$$
\widetilde C=P(1)CP(0)^{-1},\qquad
    \overline{\mathbb Q}(\widetilde C_{ij})
      =\overline{\mathbb Q}(C_{ij})
      =\overline{\mathbb Q}(e,\pi).
$$



    The target hyperplane is not stable under
    $(X,Y)\mapsto(aX,Y+b)$. Hence no Tannakian invariant of the split
    $\mathbb G_m\times\mathbb G_a$ module forces it. Only a genuinely
    non-split differential extension, enlarging the Picard--Vessiot field and
    adding new connection constants, lies outside this no-go.

26. The surviving single-root residual-polynomial problem is itself an exact
    circular lattice quotient. Put $a=v_p(n-\rho)$ and $P=p^a$. For every
    $B\in\mathbb Z[x]$,

    

$$
v_p(B(\rho))\ge a\quad\Longleftrightarrow\quad P\mid B(n).
$$



    In degree at most $d$, the coefficient lattice has basis

    

$$
P,\ x-n,\ (x-n)x,\ldots,(x-n)x^{d-1},
$$



    determinant $P$, and dual
    $\mathbb Z^{d+1}+P^{-1}\mathbb Z(1,n,\ldots,n^d)$. Its first $d$
    short directions all vanish at $n$; the quotient evaluation lattice is
    exactly $P\mathbb Z$. Hence every primitive usable residual satisfies

    

$$
a\log p\le\log H_1(B)+\deg(B)\log(n+1).
$$



    This is sharp: $B_*(x)=x+(P-n)$ has $B_*(n)=P$, and in the
    evaluation-weighted $\ell^1$ body the first usable norm lies in
    $[P,P+1]$ when $P\ge n$. Content normalization removes exactly the
    same local order it removes from height. Thus transference or capacity
    based only on the single congruence is equivalent to already knowing the
    desired digit bound. Several related places, new local equations, or a
    recurrence-special transform are not covered.

The authoritative hashes for this fourth pass are:

```
6853ceef8ae4065c65d0954a5ef0d0c7b1ae43e76167f999cbd3a11818432406  sources/common_kernel_stein_robin_parameterization.md
a841840c5b6abe8778ae58cb50eb00eb201cacdcbde389f32a9f4cdae9673bbf  scripts/common_kernel_stein_robin_certificate.py
be08f99f85f11a42f9f9efc32091eb6d6300a81b4511352ca58d0c6792d09aa5  results/common_kernel_stein_robin_certificate.json
1e902d02dc8004f467d2c19bb07fa323bfa3488afea1d000cabc06dda8f5f7e5  sources/root_unity_noncanonical_two_column_module_audit.md
3be45a96b60b1c9628d174eeba032e66406c566417728ce47fa926f6fbf9b665  scripts/root_unity_two_column_module_certificate.py
39b79c4edcb0f9eb0116555de91f3634bd744d8f121b5feea5410a28784c2b11  results/root_unity_two_column_module_certificate.json
db43343c1ab6516f169be9d0bc215c16b02ff8ffcea97e23779582bc9d7dc893  sources/bessel_mahler_newton_residual_invariant_barrier.md
31c3024d8156f64091a35c5be3fdd7fee1dfac83a6882c628b1bdd853c1b20fd  scripts/bessel_mahler_newton_residual_invariant_certificate.py
7cd3cac660cfca566ed3e9fbb0dc157cb230075f79b19edeb927fefa20403e51  results/bessel_mahler_newton_residual_invariant_certificate.json
bb8347a7cd1cd91df990a5b09142bfadcfa18d6c273bf4070f4415c05393e36c  sources/explicit_mixed_pair_tensor_gauge_no_go.md
2be4be8faad234d06f2b1baf99ca5bc9432f20b36db4a5ce6f4fda88a6000a1d  scripts/explicit_mixed_pair_tensor_gauge_certificate.py
570f313507e4f5cfa32443249fb8d7671cc1b5bb1887ce47d8ed8616a4c1a0b0  results/explicit_mixed_pair_tensor_gauge_certificate.json
3a3990e311686c6029ebfd459c377ecfcaf9e44f1e0049d0f9f3a684df92699e  sources/bessel_root_residual_lattice_duality_capacity_barrier.md
01225a43561b18ce67672ea81c30a24adf10dcc022f3cb088e1c03d6ea941dfc  scripts/bessel_root_residual_lattice_duality_certificate.py
6dbc0eb291f2b6612e30031c7b397f719834eca270e4e012c82bac23702bce39  results/bessel_root_residual_lattice_duality_certificate.json
```

All five packages were centrally audited and replayed exactly. They do not
classify $e+\pi$. They replace broad searches by four narrow survivors:
positive Robin correction, high-frequency structured two-column inheritance,
multi-place or genuinely transformed Bessel arithmetic, and genuinely
non-split mixed differential extensions.

## Fifth post-checkpoint reduction pass (2026-08-27 UTC)

27. The genuine high-frequency two-column range has an exact secondary-space
    formulation. If the correction polynomial $\Gamma_{C,D}$ vanishes, then

    

$$
C T_D-D T_C=(y+1)H,
    \qquad \deg_yH\le m-2,\quad \deg_zH\le n+D,
$$



    and $H(z,e^z)$ vanishes at zero to order at least
    $L=m(n+1)+D-1$. The ambient order kernel has the exact dimension

    

$$
(m-1)(n+D+1)-L=(m-2)D-n.
$$



    It is therefore genuinely nonzero precisely in the unresolved range
    $n<(m-2)D$; dimension counting cannot prove normality there. Basis
    changes, common frequency shifts/reflections, and scalar splitting gauges
    preserve vanishing of $\Gamma$. A good-reduction computation at
    $p=1{,}000{,}000{,}007$ rigorously proves $\Gamma\ne0$ for all 1,762
    triples
    $4\le m\le20$, $2\le n\le16$,
    $2\le D\le\min(12,n)$, $n<(m-2)D$. This finite theorem does not
    imply the required all-parameter normality statement. Even if an
    exceptional syzygy exists, its secondary content is not automatically
    the primitive content of the endpoint Wronskian seen by the polynomial
    measure for $e$.

28. The first genuinely nonsplit rational extension of the explicit mixed
    exponential/logarithmic system has been classified and computed. The
    exact rank-three carrier of $e+\pi$ is split by the rational change
    $w\mapsto w+y$. With $r(z)=1/(z-2)$, the nonsplit perturbation adds

    

$$
K(z)=e^z\int_0^z\frac{e^{-t}(-4\arctan t)}{t-2}\,dt,
$$



    and the selected connection entry becomes $e+\pi+K(1)$, where
    $K(1)>0$. Monodromy around $i$ and $2$ has a nonzero central
    commutator, proving that $e^z,-4\arctan z,J,K$ are functionally
    algebraically independent and that the differential Galois group is the
    full four-dimensional solvable extension. This does not yield numerical
    independence of their values at one. Under algebraic $e+\pi$, the
    connection field can still have transcendence degree at most three with
    no contradiction to any proved specialization theorem. Thus nonsplitting
    introduces a new exponential period instead of isolating the target.

29. Simultaneous ordinary Bessel roots at several primes do not amplify the
    residual lattice. For $a_p=v_p(n-\rho_p)$ and
    $Q=\prod_pp^{a_p}$, one has exactly

    

$$
v_p(B(\rho_p))\ge a_p\ (p\in\mathcal S)
       \quad\Longleftrightarrow\quad Q\mid B(n).
$$



    More generally, if an additive residual group $\Gamma$ has evaluation
    ideal $E_n(\Gamma)=g\mathbb Z$, then

    

$$
[\Gamma:\Gamma(Q)]=\frac Q{(Q,g)},\qquad
    E_n(\Gamma(Q))=\operatorname{lcm}(Q,g)\mathbb Z.
$$



    Any determinant discount is therefore exactly preloaded evaluated
    divisibility, and every usable residual still pays
    $\log Q\le\log H_1(B)+\deg(B)\log(n+1)$. The adjacent Bessel-shift
    coefficients satisfy the unimodular identity
    $U_jV_{j+1}-U_{j+1}V_j=(-1)^j$, so arbitrary polynomial multipliers on
    two adjacent shifts generate the whole residual ring; the recurrence
    hides no proper low-index sublattice. Composite content removes exactly
    the same part of the CRT modulus that its archimedean size pays. Surviving
    Bessel strategies must couple different local equations or centers, or
    prove a genuinely nonlinear primitive-height collapse.

The authoritative hashes for this fifth pass are:

```
8f44953048aca6fca3ac9dd14877a7e7e8eb2eec3bb70e687f52e51747db7e09  sources/root_unity_high_m_secondary_syzygy_audit.md
92699040a33f0e8ccc3d15b66f03301ce35f01bac9db397e6d4478f983bbd180  scripts/root_unity_high_m_two_column_modular_certificate.py
cab8e1c8b10f7a6a1131dd277a8bc6512d901383525b7f7aa40198d745c3ea5c  results/root_unity_high_m_two_column_modular_certificate.json
8ffbb6634f3659b87d05ecbf10b34366d9d3cd43e7cd6bd911f7773cb6ef662f  sources/explicit_nonsplit_mixed_extension_audit.md
22527f6b416b249f4510c209860ba44aeae5ef26ec99f5e7d0ebb3c1c98478a0  scripts/explicit_nonsplit_mixed_extension_certificate.py
cfa1b203629f61f4c538b29b4a1c381f72517e809aa05528f9fdfb6724283ff0  results/explicit_nonsplit_mixed_extension_certificate.json
ec0a18bf5a72182b911cd78f59d9e3dfa3a7e94122810ca138c41921d96a5f89  sources/bessel_simultaneous_crt_recurrence_sublattice_barrier.md
5614775405946b219d9e149a5b8d3e909e9bb82af52205c3a1c0c155c2acb9b8  scripts/bessel_simultaneous_crt_recurrence_sublattice_certificate.py
4a4aaec2113e84dbc2a0b727ac7afe0494523f9d6188882f6a09096615fd50d9  results/bessel_simultaneous_crt_recurrence_sublattice_certificate.json
```

All three packages were centrally proof-audited and replayed byte-for-byte.
They do not classify $e+\pi$. They sharpen the live problems to an
all-parameter total-positivity/normality theorem for the high-$m$ endpoint
map, a nonsplit extension with arithmetically controlled vanishing connection
period, a Bessel construction using genuinely distinct local data, and the
positive signed-coefficient Robin correction from item 22.

## Sixth post-checkpoint reduction pass (2026-08-27 UTC)

30. Polynomial nonlinear invariants of one Bessel recurrence state are now
    excluded in every degree. If

    

$$
\mathscr P(x+1;-(4x+2)y+z,y)=\lambda\mathscr P(x;y,z),
    \qquad \mathscr P\in\mathbb Q[x,y,z],\quad\lambda\in\mathbb Q^\times,
$$



    then $\lambda=1$ forces $\mathscr P$ to be constant, while
    $\lambda\ne1$ forces $\mathscr P=0$. The proof uses the unimodular
    fundamental matrix built from $q_n$ and
    $s_n=(p_n-q_n)/2$:

    

$$
M_n^{-1}e_2=(q_n-s_n,s_n)^T,
    \qquad \frac{s_n}{q_n}\longrightarrow\frac{e-1}{2}.
$$



    A nonzero homogeneous state-degree $r$ component would therefore
    evaluate as $\lambda^{n-1}q_n^rR(s_n/q_n)$, with nonzero rational
    $R$. Transcendence of $(e-1)/2$ keeps the last factor away from zero,
    while $q_n\ge n^n$ on even indices contradicts polynomial growth in
    $n$. Rational invariants with poles, nonconstant Darboux multipliers,
    and multi-state/nonlocal transforms remain outside the theorem.

31. The exact lattice for two distinct integer centers is also known. With
    $m=n+h$ and moduli $P,R$,

    

$$
[\mathbb Z[x]_{\le d}:\{B:P\mid B(n),\ R\mid B(m)\}]
      =\frac{PR}{\gcd(P,R,h)}\qquad(d\ge1).
$$



    Thus two independent linear residuals have coefficient determinant
    divisible by this index and jointly pay the summed local depth, up to
    $\log h$. One shared residual can interpolate both conditions below
    product height, but gains only the ordinary factor-two dimension
    compression. The natural primitive Bessel cross-determinant is

    

$$
q_ns_{n+h}-s_nq_{n+h}=(-1)^nC_h(n),
    \qquad 1\le C_h(n)\le[4(n+h)]^{h-1},
$$



    with
    $\gcd(q_n,q_{n+h})=\gcd(q_n,C_h(n))$. At an odd prime with unequal
    depths at the two centers, its valuation is exactly the smaller depth,
    never their sum. Same-root conditions are nested and contribute an lcm,
    not a product. Hence the small recurrence determinant measures only
    shared support; it does not produce the two coefficient-independent
    small residuals that a true cross-center argument requires.

The authoritative hashes added in this sixth pass are:

```
0857a3555c51e8f3c95f6a20363a6d81f6e917bd764999ef9f5932bae28c1d1a  sources/bessel_all_degree_polynomial_recurrence_invariant_exclusion.md
fbee547bd62e01bdb19de922c0629c234e2897a6ae999168d4f9d5d1a8c9535b  scripts/bessel_all_degree_polynomial_invariant_certificate.py
7038bb8403d8fa64106dfa3d8c129124834a8d0a0c5421dbbdb550cc3372704b  results/bessel_all_degree_polynomial_invariant_certificate.json
3acd353fd6fc5509cdd1802a0db910085234d41b2f2957eb053606963adfd1a4  sources/bessel_two_center_evaluation_lattice_cross_determinant.md
6eaf0d5e0b560d27971c2fdd3eba1449f6fcd1c6d8e78501f4a45674296dd4c5  scripts/bessel_two_center_evaluation_lattice_certificate.py
c45f0975b719cd8a0f4891250653cb1c7ee7f9a11d69c2d31b9d0db3593eddb3  results/bessel_two_center_evaluation_lattice_certificate.json
```

Both packages were centrally proof-audited and replayed byte-for-byte. They
close polynomial one-state invariants and generic two-center compression,
but do not supply the Bessel digit-depth estimate or classify $e+\pi$.

32. The rational-kernel moment in a genuinely coupled rank-three mixed
    extension has an exact adjoint/cohomology reduction. With

    

$$
h=q'/q-1=-\frac{(z+1)^2}{z^2+1},\qquad
    L^*=(D-1)(D+h),
$$



    the cross extension $u'=u+r(-4\arctan z)$ splits rationally if and
    only if $r=L^*\phi$. Its split endpoint moments fill exactly

    

$$
V=\overline{\mathbb Q}+\overline{\mathbb Q}e
       +\overline{\mathbb Q}\pi,
$$



    through the boundary formula

    

$$
K_{L^*\phi}(1)=
      -\pi(\phi'(1)-2\phi(1))+2\phi(1)-4e\phi(0).
$$



    Thus every closed rational integration-by-parts cancellation is a split
    coboundary. An explicit nonzero zero-moment kernel is exhibited, but its
    splitting is also explicit. The local Hermite obstruction

    

$$
\Omega_\alpha(r)=\sum_{j\ge1}
       \frac{(-1)^{j-1}}{(j-1)!}c_{\alpha,j}
$$



    gives a complete test for $r\notin(D-1)\overline{\mathbb Q}(z)$.
    A single simple pole is always nonexact but its Stieltjes-transform
    moment is rigorously nonzero; every constant-sign real rational kernel
    is likewise excluded. Polynomial cross classes reduce to two explicit
    core periods $\kappa_0,\kappa_1$. For a finite pole set, success is
    exactly an algebraic relation among those core periods, derivatives of
    the Stieltjes transform, and $1,e,\pi$, together with a nonzero local
    obstruction. No proved theorem supplies that global arithmetic
    collision. The stronger zero-period survivor is
    $[r]\in\ker(\mathcal H_\times\to\mathbb C/V)$ with nonzero image in
    $\mathcal H_e$; cross-nonsplit polynomial classes with zero image in
    $\mathcal H_e$ remain governed separately by the two core periods.

33. The one-state Bessel invariant exclusion extends from constant
    multipliers to rational first integrals. The recurrence substitution

    

$$
\sigma(x,y,z)=(x+1,-(4x+2)y+z,y)
$$



    is a polynomial automorphism. If
    $P\ne0$ and $\sigma(P)=\mu(x)P$ with
    $\mu\in\mathbb Q[x]\setminus\{0\}$, then the transfer formula gains
    the factor $\prod_{k<n}\mu(k)$; this cannot cancel the
    $q_n^m$ growth of any positive state-degree component and in fact
    strengthens it. Hence $\mu=1$ and $P$ is constant. In the UFD
    $\mathbb Q[x,y,z]$, a reduced rational invariant $P/Q$ forces
    numerator and denominator to be polynomial Darboux factors with the
    same polynomial multiplier. Therefore

    

$$
\boxed{\mathbb Q(x,y,z)^\sigma=\mathbb Q},
$$



    and rational constant-multiplier semi-invariants are constant as well.
    Multiple transported states and nonlocal transforms remain outside this
    theorem.

The authoritative hashes for items 32--33 are:

```
3883e77396d1aa8fdf1a77eeead8d3687cb7b51cbadfc1b9fd59a7d105d795bd  sources/mixed_extension_moment_kernel_audit.md
89d66a0b702f8ca2fe58d737602a5e0c7d8f31f99c6742a86b31abba3bba834f  scripts/mixed_extension_moment_kernel_certificate.py
6f6eb2d611d9034f52261126c6a96576ea66e301794f25309c7cee28952fb20b  results/mixed_extension_moment_kernel_certificate.json
558f926f1c00047057a873fd27fbd520ea95d019e4c001546b057ef7a28461b6  sources/bessel_rational_first_integral_darboux_exclusion.md
58bc67190cbbca934600e04e15d1c89043b5478872a176621ec96515b00ee967  scripts/bessel_rational_first_integral_darboux_certificate.py
8f93c56af8e474191cd32ec341bf044b685fcd8b8156be05b7fcb939c722909b  results/bessel_rational_first_integral_darboux_certificate.json
```

Both packages were centrally proof-audited and replayed byte-for-byte. They
do not classify $e+\pi$. The mixed branch now requires a genuine arithmetic
relation among explicit connection periods, while the Bessel branch requires
multiple states or a nonlocal construction rather than a rational invariant
of one state.

34. The high-frequency root-of-unity endpoint matrix now has an
    all-parameter normality theorem. For

    

$$
K_{q,a}=\mathcal L\!\left((X^q\Phi_{m,n})^{(a)}\right),
    \qquad 0\le q\le D-2,\quad 0\le a\le D,
$$



    one has $\operatorname{rank}K=D-1$ for every
    $m\ge1$ and $n\ge D\ge2$. After centering the nodes, the matrix
    splits into parity blocks. For even $m$, these are positive
    $\operatorname{sech}(\pi t)$ bi-moment matrices in
    $t^2$ and $\tanh^2(\pi t)$; for odd $m$, they are positive
    $1/\sinh(\pi t)$ bi-moment matrices in $t^2$ and
    $\coth^2(\pi t)$. Andreief's identity and two Vandermonde
    determinants make the required initial maximal minors strictly
    nonzero. The endpoint-kernel parity dimensions are exactly

    

$$
(2,0)\quad\text{if }mn\text{ is odd and }D\text{ is even},
    \qquad (1,1)\quad\text{otherwise}.
$$



    The correction polynomial also has an exact bordered-minor formula.
    If $\Lambda_b$ is the alternating Hermite-cardinal polynomial and
    $E_{b,a}=-\mathcal L(\Lambda_b^{(a)})$, then each coefficient of
    $\Gamma_{C,D}=C\beta_D-D\beta_C$ is, up to a single fixed nonzero
    Pluecker scalar, a sum of determinants
    $\det[K;e_a^T;E_b]$. Reflection reduces global nonvanishing to the
    constant bordered minor outside the parity defect and the linear
    bordered minor inside it. This is not yet a proof of nonvanishing:
    ordinary total positivity is false, as an exact normalized block at
    $(m,n,D)=(2,4,5)$ has a nonconsecutive minor $-145920$. The
    survivor is therefore a specific augmented rational-cardinal
    Chebyshev lemma (and, after it, the primitive endpoint-height problem),
    not endpoint rank itself. In the complete $m=1$ classification,
    $\Gamma=0$ exactly when $n$ is even and $D$ is odd; all finite
    rows with $m\ge2$ remain nonzero.

The authoritative hashes added for item 34 are:

```
cc1752e68d37ae30e1bb00425aab858c4b5b08bd9d1fdeef42cf4607ba3c1d97  sources/root_unity_gamma_logistic_minor_audit.md
0f78050d995111aa7a1339c5bff5b2b635a7069e89081004d35a0ec24d4874ae  scripts/root_unity_gamma_logistic_minor_certificate.py
0afd54c2a0654bdda5942dedf171ff2e5636b7f299c2f22495722de9163a3db8  results/root_unity_gamma_logistic_minor_certificate.json
```

The proof was centrally checked line by line, including the contour shifts,
the principal-value integration by parts at the central pole, the parity
counts, and the complementary-minor identity. The exact certificate replayed
byte-for-byte. This theorem removes the former all-parameter endpoint-rank
uncertainty but does not classify $e+\pi$.

35. All rational common-kernel squares have an exact Laguerre
    parametrization and a factorial--gcd obstruction. If

    

$$
F(x)=q(1-x)^2,\qquad q=\sum_{k=0}^n c_kL_k,
$$



    then the common endpoint conditions are
    $v\cdot c=0$ and $c\cdot c=(u\cdot c)^2$, where
    $u_k+i v_k=L_k(1-i)$. Every nonconstant rational solution is

    

$$
c=\rho\bigl((d\cdot d-(u\cdot d)^2)e_0
                    +2(u\cdot d)d\bigr),
    \quad d_0=0,\quad v\cdot d=0,\quad u\cdot d\ne0,
$$



    and the converse is lossless. After clearing to a primitive
    $Q\in\mathbb Z[t]$, one has
    $m=Q(1-i)\in\mathbb Z$,
    $m^2=\sum c_k^2$, and $|m|\ge n!$. If
    $I_Q=m^2(e+\pi)-b_Q$, $b_Q=B/D$ is reduced, and
    $g=\gcd(B,m^2)$, then the primitive coefficient is exactly
    $Dm^2/g$. Bernstein--Walsh and Markov inequalities give

    

$$
\frac{I_Q}{m^2}\ge
      \frac{3}{16n^2C^{2n}},\qquad
    C=4.61158178930871498088\ldots .
$$



    Consequently any shrinking square family requires exceptional gcd
    absorption satisfying
    $g n^2C^{2n}/(Dm^2)\to\infty$, against the factorial-square endpoint
    scale. This is a necessary condition, not an all-degree gcd bound.

36. The Euler-transfer route has a sharp quantitative formulation. Under
    the temporary hypothesis $s=e+\pi\in\overline{\mathbb Q}$, put
    $\beta_r=i(s-r)$ for $r=p/q$. Then

    

$$
|e^{\beta_r}+1|=2\left|\sin\frac{e-r}{2}\right|,
    \qquad h(\beta_r)=\log q+O_s(1),
    \qquad [\mathbb Q(\beta_r):\mathbb Q]\le2[\mathbb Q(s):\mathbb Q].
$$



    Continued-fraction convergents of $e$ hit height exponent exactly
    two, and on $m=3k-2$ satisfy
    $q_m^2|e^{\beta_{p_m/q_m}}+1|<1/(2k)$. Thus a uniform algebraic
    lower bound at exponent $\kappa\le2$ would disprove the hypothesis,
    while every $\kappa>2$ is compatible. Direct specialization of the
    Nesterenko--Waldschmidt theorem is valid but its optimized height
    coefficient is greater than $1266D$; the explicit $x=2$ exponent
    is already about $87285.52$ in the formal degree-one case. Baker
    theory does not apply because $\beta_r$ is additive algebraic, not a
    logarithm of an algebraic number. The sharp $E$-function
    irrationality measure for fixed $e$ also cannot improve the varying
    algebraic-exponent estimate. The missing result is precisely a new
    uniform Hermite--Lindemann endpoint exponent-two theorem.

37. Fixed-target positivity is now completely excluded, independently of
    the square ansatz. Fix $a\in\mathbb Z\setminus\{0\}$. For every
    nonzero $F\in\mathbb Z[x]$, nonnegative on $[0,1]$, with
    $A(F)=F(\pm i)=a$, the exponential component is

    

$$
\int_0^1F(x)e^x\,dx=ae-B(F)>0,
    \qquad B(F)\in\mathbb Z.
$$



    Hence it is at least $\delta_a=ae-\lfloor ae\rfloor>0$. Writing the
    full rational coordinate as $N/D$ in lowest terms, the cleared pair
    is $(aD,N)$ and
    $\gcd(aD,N)=\gcd(a,N)\mid a$. Therefore the fully primitive positive
    value is uniformly bounded below by $\delta_a/|a|$. For $a=2$,

    

$$
L(F)_{\rm primitive}\ge e-\frac52>\frac5{24}.
$$



    This covers every fixed-target endpoint localizer, Stein--Robin form,
    Markov--Lukacs representation, and exact lcm clearing. The cone is not
    empty: for $n\equiv3\pmod4$,
    $F_n=x^n+nx^{n-1}+x^{n+2}+(n+2)x^{n+1}$ is nonnegative and has
    $A(F_n)=F_n(\pm i)=2$, but its exponential mass is exactly $2e$.
    A positive survivor must therefore have $|a_n|\to\infty$ and an
    exceptional cross-content mechanism.

The authoritative hashes for items 35--37 are:

```
47a223b2212367c0a7a02c0b5337fdbb5b37865c62b43319094c7133f88e3566  sources/laguerre_square_common_kernel_parameterization_and_gcd_barrier.md
a340dee1265e48250738f38c3854907c4f1a6398dc9b0ddab7da207c9953007c  scripts/laguerre_square_common_kernel_certificate.py
403ee9908aa63a67d834601e30bcf8cacffee196c567524c8ee84798ac072c30  results/laguerre_square_common_kernel_certificate.json
647bad652fe635ae7962dc806ff7f3a3ea3dd960780804430703c3fa5904bfcf  sources/euler_transfer_quantitative_lindemann_barrier.md
5c8139dba2329088e6a749ce1d516ebf597d247495d696c0805000e5d5e70803  scripts/euler_transfer_quantitative_lindemann_certificate.py
de957e98ffa22d322a1585fd5947e7f3f517a6b51f78b05c41d6413c3c70330b  results/euler_transfer_quantitative_lindemann_certificate.json
ed27e3873717d5b2ec2512e91125f5a8047874f95c52a581dba7e0785e7d4950  sources/fixed_target_positive_common_kernel_primitive_gap.md
c66125e1861ecc9780e9cf24902e15fba70fc98f62a54568b9b27bf6af636b6e  scripts/fixed_target_positive_common_kernel_gap_certificate.py
827330c3b05e69f9c7c36690906750eff29c1b22bec4f8fbf3f5d7112a8bafca  results/fixed_target_positive_common_kernel_gap_certificate.json
```

All three packages were centrally proof-audited and replayed byte-for-byte.
The published quantitative theorems in item 36 were checked against their
primary statements and exact hypotheses. None of these results classifies
$e+\pi$.

38. The remaining growing-target positive regime has an exact two-place
    synchronization law. Write

    

$$
G=\frac{F-a}{1+x^2},\qquad
    4\int_0^1G=\frac MD,\qquad B=B(F),
$$



    with $(M,D)=1$, and let
    $g=\gcd(aD,M-BD)=\gcd(a,M-BD)\mid a$. The fully primitive value
    decomposes as

    

$$
\Lambda_F=
       \frac Dg(ae-B)+\frac1g(aD\pi+M),
$$



    and both summands are positive. Hence

    

$$
\Lambda_F\ge
      \frac{D\{ae\}+\{aD\pi\}}g.
$$



    For $a>0$, with $\alpha=aD/g$, the primitive approximation splits
    exactly into the two lower errors

    

$$
e-\frac Ba>0,\qquad
    \pi+\frac{M}{aD}>0,
$$



    whose sum is $\Lambda_F/\alpha$; the synchronization condition is
    $M\equiv BD\pmod g$. Euler's continued fraction gives, for every
    $p\in\mathbb Z,q\ge1$,

    

$$
|qe-p|>\frac1{q(4\log_2q+8)},
$$



    and consequently

    

$$
\Lambda_F>\frac{D}{|a|^2(4\log_2|a|+8)}.
$$



    If $0<\Lambda_F\le\alpha^{-1-\eta}$, then necessarily
    $\alpha^{2+\eta}<a^2(4\log_2a+8)$ and the cross-content has an
    explicit super-baseline lower bound. No generic sublinear content
    theorem is possible: the primitive positive family

    

$$
F_m=m\,4x(1-x)^2(31-3x^2)
       +x(1-x)^2(1+x^2)(-2090+4553x+744x^2)
$$



    has $a_m=272m$, $g_m=8m$, and polynomial content one for every
    $m\ge17$. Its primitive output, however, is always the fixed pair
    $(34,-193)$. The only live positive regime is therefore a sequence
    of changing primitive rays with simultaneously small one-sided errors
    and synchronized large content.

The authoritative hashes for item 38 are:

```
d4aea08fb0684baf9bd0931ab436718d7e23cdf8084f9c9683ac99cb26629405  sources/growing_target_positive_two_place_synchronization_barrier.md
acbc468214c6e450f8102f72ab4ea8f6e860eccc568d6b5eef03f7383ade83b8  scripts/growing_target_positive_synchronization_certificate.py
1eb2ea1e1d40479f691ad6d41417da7ef52d7977a8fb3de37c6acb9e63cc4b7f  results/growing_target_positive_synchronization_certificate.json
```

The proof was centrally audited, including the continued-fraction bound,
the two positive summands, the exact content identity, and positivity of the
saturation family. The certificate replayed byte-for-byte. This result does
not classify $e+\pi$.

39. The two-column root-of-unity endpoint must use the corrected polynomial
    $\Delta=W(C,D)-\Gamma$, not $\Gamma$ or the bare endpoint Wronskian
    separately. With $g=1+e^z$, $\xi=i\pi$, and
    $R_C=C+gT_C$, the sign $g'(\xi)=-1$ gives the exact identity

    

$$
W(R_C,R_D)(i\pi)=
       [W(C,D)-(C\beta_D-D\beta_C)](i\pi)=\Delta(i\pi).
$$



    If the two remainders have origin order at least
    $L=m(n+1)+D-1$, their Wronskian has order at least $2L$. A uniform
    all-parameter clearing for the interpolation map is

    

$$
Q_{m,n}=2^{m(n+1)}
      \left(\prod_{a=0}^n a!\right)^m
      \prod_{h=1}^{m-1}h^{(m-h)(n+1)^2}.
$$



    After saturating the endpoint kernel, let $p$ be its primitive
    Pluecker vector, let $E^*=q_EE$, and index exterior coordinates by
    $u<v$. The exact integer corrected-coefficient map is

    

$$
(\mathcal A_\Delta)_{\ell,(u,v)}=
      q_E(v-u)\mathbf1_{\ell=u+v-1}
      -E^*_{\ell-u,v}+E^*_{\ell-v,u},
    \qquad q_E\Delta=\mathcal A_\Delta p.
$$



    Bare-Wronskian, $\Gamma$, and corrected-$\Delta$ contents are
    independent: exact rows have $\Gamma$-contents $729$ and $128$
    but corrected content one. If $\mathcal A_\Delta$ has full column
    rank and largest Smith invariant $s_R$, then
    $\operatorname{cont}(\mathcal A_\Delta x)\mid s_R$ for every
    primitive exterior vector $x$. In the rank-deficient range there is
    no ambient primitive-vector cap; any useful theorem must use the
    decomposable complementary-minor locus of the endpoint kernel.

    The optimized Schwarz estimate duplicates both the one-column analytic
    gain and its height cost. If $d=\deg P_\Delta$,
    $\kappa=r^2d+r-1$ under hypothetical algebraicity of degree $r$,
    and $\mathfrak c_Q=\operatorname{cont}(Q\Delta)$, the leading
    corrected-content requirement is

    

$$
(\kappa+1)\log\mathfrak c_Q>
      \kappa\log H(Q\Delta)+\log(C_0H_W)
      -2\mathcal G_1-\log Q.
$$



    Neither $\Gamma\ne0$ nor its content proves $\Delta\ne0$, its
    degree, or this inequality. A coefficient of $\Gamma$ above degree
    $2D-2$ would suffice for corrected nonvanishing, but a separate
    structured content or sharper-cancellation theorem would still be
    required. The six replay rows all have corrected content one and
    diagnostic relative exponents below two.

The centrally audited hashes for item 39 are:

```
a077b16a5a4563995bd1377e3c3686afb1dcae1b5f2106b8de77827b3feb535e  sources/root_unity_corrected_exterior_primitive_height_audit.md
c00e04f61e323f2394cdc66cf866e7b14cfc191fcb3c39a9820264cfa6eecee1  scripts/root_unity_corrected_exterior_primitive_height_certificate.py
50fb246beccfc3a6eaedb78272eadb2212c3543d9b87ca9cbbb23b73d1fa40f6  results/root_unity_corrected_exterior_primitive_height_certificate.json
de75825bb7c04a678a5e04dcd90eefbc06eb883d5ddad81c9e4cd748330ff1f7  results/root_unity_corrected_exterior_primitive_height_hashes.sha256
```

The source was read line by line, two TeX escape defects were repaired, and
the certificate was replayed byte-for-byte. The determinant sign, saturation,
Smith hypotheses, and height ledger were checked independently. Item 39 is a
barrier and normalization theorem, not a classification of $e+\pi$.

40. In the positive common-kernel factor class

    

$$
F=(1-x)^2H,\qquad H\in\mathbb Z[x],\qquad H\ge0\quad(0\le x\le1),
$$



    impose $A(F)=F(i)=F(-i)=a$, put $B=B(F)$, and set

    

$$
I=4\int_0^1\frac{F-a}{1+x^2}\,dx.
$$



    For $\deg H\le7$, the exact unconstrained integer image is

    

$$
(a,B,I)\in4\mathbb Z\times\mathbb Z\times\frac1{210}\mathbb Z,
$$



    with equality as lattices. In particular, $4\mid a$ universally in
    this factor class, but there is no further congruence coupling these
    three coordinates in degree seven. An exact Bernstein interpolation
    construction gives fourteen genuinely changing primitive positive rays,
    ending at

    

$$
1246188493618(e+\pi)-7302508153575,
$$



    whose value lies rigorously between
    $3.273998315148272218902473900\cdot10^{-13}$ and
    $3.273998315148272218902473901\cdot10^{-13}$. Each ray is realized by
    a monic primitive nonnegative integer polynomial of degree 66. A monic
    degree-64 zero-output direction preserves positivity and polynomial
    primitivity while producing output cross-contents as large as 114 decimal
    digits. There is also an infinite family of changing primitive rays
    $(16n+4,-85n)$ for $n\equiv3\pmod {170}$, with arbitrarily scalable
    cross-content, but its primitive value grows. Thus the construction proves
    that positivity and primitivity permit very large synchronized content and
    several excellent rays; it does not supply the infinite shrinking sequence
    needed even for irrationality.

The centrally audited hashes for item 40 are:

```
3290247371ed4d0fa23fa071be3f8a9175f7a6ea3c9840e572543f56fdc388a4  sources/factor_endpoint_positive_cone_lattice_and_rays.md
0f290c6612af6fa97dba74efc441c76a836137d2c9df37c3a692dbd0501d97ff  scripts/factor_endpoint_positive_cone_rays_certificate.py
29c445a795cee6b557d81df16c4687dfd1e8de4df5f1912a94fcb803c7204be1  results/factor_endpoint_positive_cone_rays_certificate.json
```

The lattice computation, positivity bounds, primitive-ray reductions, and
rigorous enclosures were checked independently, and the certificate replayed
byte-for-byte.

41. The augmented root-of-unity determinant now has an all-parameter proof
    that its coordinate row is not redundant. In shifted coordinates, deleting
    column $a=0$ and retaining the parity block in columns
    $a=2,4,\ldots$ leaves full possible row rank for every
    $m\ge1$ and $n\ge D\ge2$. The proof factors the relevant coefficient
    matrix through a totally nonnegative Toeplitz matrix generated by a product
    of linear factors with nonpositive zeros, then obtains strictness from a
    monomial collocation determinant and Andreief's identity.

    The remaining generic border is exactly a repeated-node divided-difference
    determinant for an explicit rational cardinal function $\rho_{m,n}$.
    For even $m=2k$, after writing $U=X-(m-1)/2$, it has the form

    

$$
\rho(x)=\frac{N(x)}{
      \prod_{r=1}^{k}(x+(r-\tfrac12)^2)^{n+1}}.
$$



    For odd $m$, subtracting the known central cardinal value removes the
    central pole and gives the analogous denominator with nodes $r^2$.
    Positivity of the numerator in the ordered repeated-node Newton basis
    expands $\rho$ as a positive sum of reciprocal products and hence proves
    strict complete monotonicity and border nonvanishing. Exact arithmetic
    verifies every such Newton coefficient for all generic tuples
    $2\le m\le10,2\le n\le7$, as well as every parity-defect tuple in that
    box; 50 borders were also checked directly. These are finite theorems only.
    The tempting pointwise simple-residue strengthening is false already at
    $(m,n)=(8,3)$. For $m=1$, the exact classification remains
    $\Gamma=0$ precisely when $n$ is even and $D$ is odd.

    The unresolved all-parameter step is now the explicit confluent-Newton
    positivity lemma for the three cardinal numerators. Even if that proves
    $\Gamma\ne0$, item 39 shows that corrected nonvanishing and the decisive
    primitive-height estimate still require separate arguments.

The centrally audited hashes for item 41 are:

```
d22b2cb5a92d4a8c4bebdb1f61a095cbf15e342fb8a19d1a61dfc3a3d87edb47  sources/root_unity_gamma_augmented_newton_audit.md
3159d11398f882eeb35a8c4b47c21c23717fc8cc1599d6f87744994841b57b14  scripts/root_unity_gamma_augmented_newton_certificate.py
bdcf5ce1a437fc763b77ee529b29cba850f7972c197b12ab14df5d551471ff31  results/root_unity_gamma_augmented_newton_certificate.json
```

The shifted-minor proof, cardinal reductions, parity cases, and strict-complete-
monotonicity criterion were checked line by line. The exact certificate replayed
byte-for-byte. Item 41 does not classify $e+\pi$.

42. The entire positive factor-endpoint cone is universal, in an exact sense
    that also proves why this branch cannot decide irrationality by convex
    optimization alone. Let $s=e+\pi$, write $F=(1-x)^2H$, impose
    $H\ge0$, $A(F)=F(i)=F(-i)=a$, and let $(a,c)$ be the rational
    output pair. The real output cone is exactly

    

$$
\mathcal C_{\mathbb R}=\{(0,0)\}\cup
       \{(a,c)\in\mathbb R^2:sa+c>0\}.
$$



    The proof uses the strict order unit $H_*=3+8x+3x^2$, extends every
    positive functional on the common plane to all polynomials, and analyzes
    its Hausdorff moments. Factorial growth of the endpoint functional forces
    the unique coefficient cancellation $\mu=ev$; convergence of the four
    monomial residue classes then kills the remaining $i^n$ cycle. Hence the
    dual cone is exactly $\mathbb R_{\ge0}(s,1)$, and finite-dimensional
    bipolarity plus equality of relative interiors gives the open half-plane.

    Rational density inside a strictly positive affine fiber then proves that
    every primitive $(q,k)\in\mathbb Z^2$ satisfying
    $q(e+\pi)+k>0$ is the fully primitive output of a primitive positive
    integer polynomial in this factor class. In particular every coprime lower
    rational approximant $p/q<e+\pi$ is realized. It follows exactly that an
    infinite shrinking family in this cone exists if and only if $e+\pi$ is
    irrational: in the rational case the primitive values have a fixed gap,
    while in the irrational case lower continued-fraction convergents are
    realized. Thus realizability supplies no independent arithmetic input.

The centrally audited hashes for item 42 are:

```
7cd5c84affdf2cfc21959bc363a40209803fb4f9702ce39c0ae1018a1cfcb17c  sources/factor_endpoint_positive_cone_universality_and_circularity.md
bc9f0eb1bc39bda01e437d191ee82c3a5463e0777a3f58779d4f57415f45d726  scripts/factor_endpoint_positive_cone_universality_certificate.py
a702d448ddd3e2374c0b87f3ed15a1da5f6b6238a88327c6e3e2a8923011061b  results/factor_endpoint_positive_cone_universality_certificate.json
```

The positive-extension lemma, moment duality, boundary exclusion, rational
lifting, and primitive normalization were checked line by line. The certificate
replayed byte-for-byte. Item 42 is a universality-and-circularity theorem, not a
classification of $e+\pi$.

## Bessel checkpoint item 105: all-integer jet identity and the exact one-digit obstruction



$$
q_0=q_1=1,\qquad q_n=(4n-2)q_{n-1}+q_{n-2},
$$





$$
p_0=1,\quad p_1=3,\qquad p_n=(4n-2)p_{n-1}+p_{n-2},
$$



and define



$$
b_0=0,\quad b_1=4,\qquad
 b_{n+2}=(4n+6)b_{n+1}+b_n+4q_{n+1}.
$$



For every prime $p$, put ${\cal K}_p=\sum_{m\ge0}m!\in\mathbb Z_p$.
Then the interpolation



$$
f_p(x)=\sum_{k\ge0}\frac{(-x)_k(x+1)_k}{k!}
$$



satisfies



$$
\boxed{f_p'(n)=(-1)^{n+1}(p_n{\cal K}_p-b_n)}
 \qquad(n\ge0).                                          \tag{105.1}
$$



Termwise differentiation in (105.1) is justified in the local Tate algebra,
not merely pointwise: on $n+p\mathbb Z_p$ for odd $p$, and on
$n+4\mathbb Z_2$, the Gauss valuations of the derivative summands grow
linearly in $k$.  At the first two integers one obtains



$$
f_p'(0)=-{\cal K}_p,\qquad f_p'(1)=3{\cal K}_p-4,
$$



and differentiation of the global Bessel difference equation propagates
the identity to every $n$.  The integer multipliers already have main
Bessel height:



$$
0\le b_n\le4(n+1)p_n,qquad
 \log\max(1,b_n)=n\log n+O(n).                           \tag{105.2}
$$



For an odd prime, suppose $a=v_p(q_n)\ge1$ lies on an ordinary branch and
$u_n=p_n{\cal K}_p-b_n$ is a unit.  If the compatible root has next digit
$\rho\equiv n+t p^a\pmod{p^{a+1}}$, then the exact affine lift law gives



$$
\boxed{t\equiv(q_n/p^a)u_n^{-1}\pmod p.}               \tag{105.3}
$$



No stronger modulus is claimed.  Formula (105.1) also shows, for every fixed
integer $n$,



$$
f_p'(n)\in\mathbb Q\quad\Longleftrightarrow\quad
 {\cal K}_p\in\mathbb Q.
$$



Irrationality of ${\cal K}_p$ at any specified prime is itself open.
Consequently direct local Taylor/Hermite--Padé coefficients do not provide
rational height data without solving an additional fixed-prime Euler-series
problem.

Frozen item-105 package:

~~~
fb68cec8ec01ca9dcfa39eb86af61f76a9bba07f18a6e955668ef2e90f89696e  sources/bessel_padic_all_integer_jet_euler_obstruction.md
0ede4cd80a7b343ca5c2e90c741d7b2629e41acb2b895aa27a10073da12f2755  scripts/bessel_padic_all_integer_jet_euler_obstruction_certificate.py
586de99873f278dce9af079db895937e8c1ffaadf48873027544d671c0466ea5  results/bessel_padic_all_integer_jet_euler_obstruction_certificate.json
b55fd4214f4207d6d4698b6a83ebb4bb474b09509cb42ac45e93beb8021520cf  results/bessel_padic_all_integer_jet_euler_obstruction_hashes.sha256
~~~

The deterministic root replay and manifest pass.  Item 105 is an exact
global-method obstruction; it neither bounds the zero-run length nor
classifies $e+\pi$.

43. The universal confluent-Newton positivity lemma from item 41 is true. Let
    $0<A_1<A_2<\cdots$, $\sum A_j^{-1}<\infty$, and

    

$$
\mathcal P(x)=\prod_{j\ge1}(1+x/A_j),\qquad
    F(x)=\int_0^1w(s)\mathcal P(s^2x)^\nu\,ds,
$$



    where $w\ge0$ is positive on an interior interval and
    $h\in\{\nu,\nu+1\}$. If $\mathscr R_{k,h}F$ is the Hermite
    remainder modulo the first $k$ product blocks to multiplicity $h$,
    then every coefficient in its ordered repeated-rate Newton expansion is
    strictly positive.

    The proof expands the first $k$ blocks into positive reciprocal
    subproducts. Every tail zero has rate $A_\ell/s^2>A_k$, so multiplication
    by a tail factor and deletion of the polynomial part preserves this cone.
    Any reciprocal subproduct expands nonnegatively in the ordered Coxian
    suffix basis. Local-uniform convergence makes the Hermite/polar projection
    continuous. Strictness follows either from a direct suffix term when
    $h=\nu$, or from finitely many positive tail deletions when
    $h=\nu+1$, followed in both cases by a strictly positive convergent
    infinite retention product.

    Applying the theorem to

    

$$
\cos(\pi\sqrt{-x})=\prod_{r\ge1}
       \left(1+\frac{x}{(r-\tfrac12)^2}\right)
$$



    with weight $1$, and to

    

$$
\frac{\sin(\pi\sqrt{-x})}{\pi\sqrt{-x}}
       =\prod_{r\ge1}\left(1+\frac{x}{r^2}\right)
$$



    with weights $s^\nu$ and $(1-s)s^\nu$, supplies respectively the
    even-$m$ $\Lambda_0$, odd-$m$ $\Lambda_0$, and parity-defect
    $\Lambda_1$ cardinal numerators. Exact entire jet extensions fix the raw
    signs and normalizations. Together with item 41's shifted-coordinate
    theorem, this proves

    

$$
\boxed{\Gamma\ne0\quad\text{for every }m\ge2,
           \ n\ge D\ge2.}
$$



    For $m=1$, the earlier exact degeneracy classification remains in force.
    This theorem does not prevent cancellation in $\Delta=W-\Gamma$ and does
    not supply the necessary primitive-height or endpoint-value bound.

The centrally audited hashes for item 43 are:

```
af3049a869327cc7d1138cea448878c64bebadcf0305a124c5d6f923e7937ba6  sources/root_unity_gamma_positive_pole_truncation_theorem.md
ca78fcef77b9394215f1c61e04658b5c0881c5507cbce35eeb0975bb121f8b1f  scripts/root_unity_gamma_positive_pole_truncation_certificate.py
0fa242f90fae8f5ed652d046b79af6190597265fadcc5da3517654990a0cbcf3  results/root_unity_gamma_positive_pole_truncation_certificate.json
```

The reciprocal-cone algebra, ordered-basis completion, infinite-product
strictness, Hermite-projection limit, three entire extensions, and all scalar
signs were checked independently. The 30-row exact certificate and all 253
subproduct completions replayed deterministically. Item 43 proves correction
nonvanishing, not a classification of $e+\pi$.

44. A second all-parameter theorem locates the top coefficient of $\Gamma$
    whenever parity allows it. The top Hermite-cardinal quotient has the exact
    simple-pole formula

    

$$
\frac{\Lambda_n(X)}{\Phi(X)}=
      \frac1{n!}\sum_{j=0}^{m-1}
      \frac{(-1)^{j+(n+1)(m-1-j)}}
      {[j!(m-1-j)!]^{n+1}}\frac1{X-j}.
$$



    After centering, this quotient is, up to a global sign, a strictly
    completely monotone rational function of $-U^2$. For even $n$, the
    paired simple-pole residues are directly positive. For odd $n$, its
    ordered Newton coefficients are positive because explicit centered
    binomial-power sums are Parseval integrals of two nonnegative functions.
    Positivity of the centered binomial power follows from negative real
    rootedness under Schur--Szego composition; the exact semigroup hypothesis
    was checked against the primary published theorem.

    Checkerboard block factorization, the Hermite--Genocchi sign, and
    Andreief's identity then prove

    

$$
[z^{n+D}]\Gamma\ne0
$$



    exactly when

    

$$
n+D\text{ is even},\qquad\text{or}\qquad
    m,n\text{ are odd and }D\text{ is even}.
$$



    Equivalently, parity forces the top coefficient to vanish only for
    $n$ even and $D$ odd (arbitrary $m$), or for $m$ even,
    $n$ odd, and $D$ even. In every allowed regime,

    

$$
\boxed{\deg\Delta=\deg\Gamma=n+D,}
$$



    because $\deg W\le2D-2<n+D$. Thus corrected nonvanishing and its exact
    degree are proved in all parity-allowed regimes. In the two forced regimes,
    the coefficient at $n+D-1$ is a sum of two bordered minors. It is nonzero
    on the exact replay grid, but the summands can have opposite signs, so no
    universal claim is made there.

The centrally audited hashes for item 44 are:

```
63d1b3532150fc7f2e9e2f142e6cd1c797c9ed3c3739a4b3de2d30932c27061c  sources/root_unity_gamma_top_cardinal_degree_theorem.md
b843529adf1d2f407e3f331618efd75354984887984c0e7084155a7caf24ae12  scripts/root_unity_gamma_top_cardinal_degree_certificate.py
755c6a43ddf21b80b68133bf85978406b5123a0151e67bc046b0498e5576b2ba  results/root_unity_gamma_top_cardinal_degree_certificate.json
b06af46052c733ed78ca7353565c0d64b7db1f4d004f173472a101d5bc707509  results/root_unity_gamma_top_cardinal_degree_hashes.sha256
```

The residue formula, parity count, Fourier identities, complete-monotonicity
step, central-pole boundary conditions, and corrected degree comparison were
checked line by line. The Schur--Szego semigroup statement was verified in the
primary source, and the 88 complete-monotonicity rows plus 100 bordered-minor
rows replayed byte-for-byte. Item 44 does not provide primitive-height control
and does not classify $e+\pi$.

45. The arithmetic carried by the positive cardinal Newton coefficients is now
    explicit in all three families. Every ordered confluent Newton coefficient
    has an exact local-residue formula, and if $q_N$ is the least denominator
    of the normalized cardinal numerator, then

    

$$
\mathcal L_{\rm loc}\mid q_N
      \quad\text{and}\quad
      q_N\mid L_*\mathcal V_{k,h}(b).
$$



    In the integer-rate coordinate, the primitive clearing content is one for
    even-$m$ $\Lambda_0$, divides two for odd-$m$ $\Lambda_0$, and is
    one for the odd defect $\Lambda_1$. Positivity also gives

    

$$
H(P_N)\ge q_N.
$$



    Thus the large local denominators survive in primitive height rather than
    furnishing a large common factor. The coordinate qualification is
    essential. For even $m=2k$, returning the primitive integer-rate
    numerator to the original endpoint variable creates content $C_E$ with

    

$$
C_E\text{ a power of two},\qquad
       1\le C_E\le2^{2(k(n+1)-1)}.
$$



    This can be nearly sharp: the exact row $(k,n)=(3,5)$ has
    $C_E=2^{32}$, while the exponent in the bound is 34. Consequently the
    isolated odd-family $\log2$ cap must never be transferred to the even
    endpoint coordinate. More importantly, none of these cardinal-content
    bounds controls the saturated endpoint Pluecker vector or the corrected
    contraction $W-\Gamma$. The package is a rigorous barrier to cardinal
    clearing alone, not a corrected-content theorem.

The centrally audited hashes for item 45 are:

```
9b7caad744854d7d29576b5355a0e42169f0650e72033c3f4a1372f198ad8b23  sources/root_unity_cardinal_newton_arithmetic_barrier.md
19a44d53e0e1bea35228c6292ca2d072b1ee02636fc1d8a4d2b72837870d77c8  scripts/root_unity_cardinal_newton_arithmetic_certificate.py
6292030c230b78e7770084a4533bd1529ed6cdb8cc6a4e773498ad4a8f95f4e3  results/root_unity_cardinal_newton_arithmetic_certificate.json
```

The local germs, residue reconstruction, denominator sandwich, content
normalization, dyadic coordinate lemma, and height bounds were checked line by
line. The 30-row exact rational certificate replayed centrally. Item 45 does
not bound corrected content and does not classify $e+\pi$.

46. Corrected nonvanishing is now proved for every even number of frequencies.
    The exact constant coefficient is

    

$$
[z^0]\Delta\ \doteq\
      \det\!\begin{pmatrix}K\\e_0^T\\e_1^T-E_0\end{pmatrix},
$$



    and the last row is represented by
    $\mathcal L((\Lambda_0+2X+1)^{(a)})$. For $m=2k$, centering on the
    odd columns gives

    

$$
\Lambda_0(c+U)+2U=U\{N_{m,n}(-U^2)+2\}.
$$



    If $\sigma=(-1)^k$, every raw repeated-rate Newton coefficient of
    $N_{m,n}$ has sign $\sigma$, while
    $\gamma_0=N(-1/4)=2\sigma$. Adding two therefore changes the normalized
    first coefficient either from two to four or from two to zero, and leaves
    every later coefficient strictly positive. The resulting reciprocal-suffix
    expansion is still nonzero and strictly completely monotone. The existing
    divided-difference/Andreief theorem proves

    

$$
\boxed{[z^0]\Delta\ne0\quad
              (m\ge2\text{ even},\ n\ge D\ge2).}
$$



    The same audit fixes the defect coefficient exactly as

    

$$
[z^1]\Delta\ \doteq\
      \det\!\begin{pmatrix}K\\e_0^T\\2e_2^T-E_1\end{pmatrix}.
$$



    Combining this theorem with item 44 leaves only

    

$$
m\ge3\text{ odd},\qquad n\text{ even},\qquad D\text{ odd}
$$



    outside the proved universal $\Delta\ne0$ regimes for $m\ge2$. In
    that family a genuine low central jet prevents direct application of the
    pole-truncation theorem. Even closing this last nonvanishing family would
    not provide the primitive height/content inequality required for a
    transcendence conclusion.

The centrally audited hashes for item 46 are:

```
405f929aac17a760d4bffd8d610130a96ad780677ed9b8380c33696dc4e23ada  sources/root_unity_corrected_low_border_even_m_theorem.md
dfd545753d9160c6d87402579b83c0e0f930e77dc8ddf8b1efbe403decb34b23  scripts/root_unity_corrected_low_border_even_m_certificate.py
2862b462b31e0aaad6375db5a3bd1a717f6cb41eca586af53065ab211d8e509c  results/root_unity_corrected_low_border_even_m_certificate.json
bec0f1a7eafdc5713b6366bb5fe81fcf98dba5e83476c04ebe4e4dea8ba5a3b4  results/root_unity_corrected_low_border_even_m_hashes.sha256
```

The exact corrected scalar, dual-polynomial rows, centered Newton
normalization, strict-complete-monotonicity argument, parity combination, and
central-boundary limitation were checked independently. The exact Newton and
bordered-minor grids replayed deterministically. Item 46 is a nonvanishing
theorem, not a classification of $e+\pi$.

49. The preliminary all-parameter reduction for the last forced family has
    been corrected and frozen. For odd $m=2k+1$, even $n$, and odd
    $D=2d+1$, the derivative difference

    

$$
F=\Lambda_{n-1}-\Lambda_n'
$$



    has no double poles and no central pole after division by $\Phi$. Its
    centered quotient is

    

$$
\frac{F(k+U)}{\Phi(k+U)}=\psi(-U^2),\qquad
       \psi(x)=\sum_{r=1}^k\frac{c_r}{x+r^2},\qquad c_r>0.
$$



    The strict residue sign follows by pairing the regular-part weights about
    each positive node, using the strict decrease of
    $w_0>w_1>\cdots>w_k>0$. A direct phase reconstruction fixes the earlier
    sign ambiguity:

    

$$
R(it)=-it\rho(t^2),\qquad
       V\sigma=V\psi-\mathcal E(V\rho),
       \qquad \mathcal E=2x\frac d{dx}+h+1.
$$



    Hence the normalized next coefficient is a nonzero common phase times

    

$$
\operatorname{NB}_A(V\psi)
       +\operatorname{NB}_G(\mathcal E(V\rho))
       -\operatorname{NB}_A(\mathcal E(V\rho)).
$$



    The first term is strictly positive. The remaining polewise comparison is
    exactly a Markov transform. With $z=\operatorname{csch}^2(\pi\sqrt x)$,
    $g=\pi\sqrt x\coth(\pi\sqrt x)$, and $T=1+2z\,d/dz$, let $p$ and
    $p_g$ be the monic degree-$d$ mixed biorthogonal polynomials for
    $Vd\nu$ and $gVd\nu$, and set $q=Tp/(2d+1)$. Then, for
    $W=V/(x+a)$,

    

$$
\operatorname{NB}_A(\mathcal EW)-
       \operatorname{NB}_G(\mathcal EW)
       =\ell_d(2d+1)\int gW(q-p_g)\,d\nu.
$$



    This package proves the reduction, boundary conditions, residues, and
    phases. Its recorded finite grid verifies the final sign but does not use
    that grid as a theorem; item 50 supplies the missing universal argument.

The centrally audited hashes for item 49 are:

```
d026dc66a6974c411360cdbbb67f64821c5b7b9a016e2b4101ec122fe12161c3  sources/root_unity_gamma_forced_odd_m_next_coefficient_audit.md
9b8cecf67ce5631dc4025080e794ed9272c8ab1629f09cb9b81b5f6623df96de  scripts/root_unity_gamma_forced_odd_m_next_coefficient_certificate.py
2ba6b9a887c068c422d914228e77af1db1948f66dac496b463e99a3f6df6f570  results/root_unity_gamma_forced_odd_m_next_coefficient_certificate.json
ac68590653c8404a81dbfe406c1cf7b3f53bfa60d212667fc77bdb5e0c7bbe2b  results/root_unity_gamma_forced_odd_m_next_coefficient_hashes.sha256
```

The pole cancellations, positive residues, endpoint decomposition, corrected
column phases, adjoint identity, and finite exact anchors were checked line by
line. The manifest, Python compilation, and control-byte audit pass. Item 49 is
a reduction package whose formerly open inequality is superseded by item 50.

50. The external-node Markov comparison closes the last corrected-nonvanishing
    family for every parameter. Retain

    

$$
m=2k+1\ge3,\quad n\ge4\text{ even},\quad
      D=2d+1\ge3\text{ odd},\quad D\le n,
$$



    so $h=n+1\ge2d+3$. Let $p,p_g,q$ be as in item 49 and put
    $r=q-p_g$. For the positive measures

    

$$
d\mu_0=Vd\nu,\qquad d\mu=gVd\nu,
$$



    orthogonality and the Euler adjoint give, for every $\deg P<d$,

    

$$
\int P(x)r(z(x))\,d\mu(x)
       =-\frac{2h}{2d+1}\sum_{j=1}^k
         j^2J_jP(-j^2),
       \qquad
       J_j=\int\frac{p(z(x))}{x+j^2}\,d\mu_0(x)>0.
$$



    The strict sign of $J_j$ is a divided-difference/Andreief sign
    cancellation. For an arbitrary positive mixed measure and an external node
    $\xi=-b<0$, let $R_\xi(z)$ reproduce evaluation at $\xi$ on
    polynomials of degree below $d$. Its Stieltjes transform is strictly
    positive:

    

$$
K_d(a,\xi)=\int\frac{R_\xi(z(x))}{x+a}\,d\mu(x)>0
       \qquad(a\ge0).
$$



    The Schur determinant proof reduces the sign to the exact interpolation
    value

    

$$
p_a(-b)=
       \frac{1-\prod_i(b+x_i)/(a+x_i)}{a-b}>0,
$$



    with continuous value $\sum_i(a+x_i)^{-1}$ at $a=b$. This covers
    $a>b$, $a<b$, $a=b$, and the central pole $a=0$.

    Moment uniqueness now upgrades the preceding moment identity to

    

$$
r(z)=-\frac{2h}{2d+1}\sum_{j=1}^k
             j^2J_jR_{-j^2}(z).
$$



    Therefore every divisor Markov transform is strictly negative, and

    

$$
\operatorname{NB}_A\!\left(\mathcal E\frac{V}{x+a}\right)
       <
       \operatorname{NB}_G\!\left(\mathcal E\frac{V}{x+a}\right)
       \qquad(a\ge0).
$$



    Positive linearity proves the strict comparison for the actual $\rho$.
    Together with the positive $V\psi$ border and the corrected phase,

    

$$
\boxed{[z^{n+D-1}]\Gamma\ne0},\qquad
       \boxed{\deg\Delta=n+D-1}
$$



    throughout the last forced family. Combined with the earlier top-degree
    and even-frequency theorems, corrected exterior nonvanishing is now proved
    for every $m\ge2,n\ge D\ge2$. This still supplies no primitive-content,
    saturated-height, or endpoint-value inequality strong enough to classify
    $e+\pi$.

The centrally audited hashes for item 50 are:

```
d5f0d4e61690c3c41f4e419f817ba4ec19f40572505ac61867957c80a487f412  sources/root_unity_forced_odd_m_all_D_markov_theorem.md
412c4abd9849269c12a01f87d9fef4f20ec93511ff3ce5bc215912731e9fd8d0  scripts/root_unity_forced_odd_m_all_D_markov_certificate.py
b67f85c6ce4da44a686f6aa02ddeec6ec026ed049af735a65b09ff2704c80cdd  results/root_unity_forced_odd_m_all_D_markov_certificate.json
04393f30554f042a644736591fab251f999eb0bb2e603d7b5941c01fabe60d7b  results/root_unity_forced_odd_m_all_D_markov_hashes.sha256
```

The adjoint boundary, mixed-moment signs, divisor transforms, Schur-block
orientation, all interpolation cases, negative-node moment representation,
strict polewise sum, common phase, and degree comparison were independently
audited. The exact rational replay, manifest, Python compilation, and
control-byte audit all pass. Item 50 is a universal corrected-nonvanishing and
degree theorem, not a classification of $e+\pi$.

47. The degree-three slice of the last parity-forced family is now closed for
    every parameter:

    

$$
m=2k+1\ge3,\qquad n\ge4\text{ even},\qquad D=3.
$$



    A fresh phase audit first corrected the live common-column normalization.
    With the natural positive Stieltjes function

    

$$
\rho_+(x)=\frac{w_0}{x}
        +2\sum_{r=1}^k\frac{w_r}{x+r^2},
$$



    the centered quotient satisfies

    

$$
R(it)=-it\rho_+(t^2),\qquad
       V\sigma=V\psi-\mathcal E(V\rho_+),
       \quad \mathcal E=2x\frac d{dx}+h+1.
$$



    The even and odd bordered ratios consequently have opposite, rather than
    equal, common prefactors. The corrected normalized target is

    

$$
\mathcal T=\operatorname{NB}_A(V\psi)
       -\{\operatorname{NB}_A(\mathcal E(V\rho_+))
          -\operatorname{NB}_G(\mathcal E(V\rho_+))\}.
$$



    For $D=3$, put

    

$$
q(x)=2\coth^2(\pi\sqrt x)-1,
       \qquad
       a(x)=\frac{\mathcal EV(x)}{V(x)}
       =h+1+2h\sum_{r=1}^k\frac{x}{x+r^2}.
$$



    Under the positive probability measure proportional to
    $V(t^2)t^h/\sinh(\pi t)\,dt$, the function $a$ is strictly increasing
    and $q$ is strictly decreasing. Direct $2$-by-$2$ determinant
    algebra gives, for every integrable border row $f$,

    

$$
\operatorname{NB}_A(f)-\operatorname{NB}_G(f)
      =\langle f,1\rangle
       \frac{\operatorname{Cov}(a,q)}{\mathbb E a}.
$$



    The Euler image of $-V\rho_+$ has strictly negative Laurent
    coefficients, including a legitimate $x^{-1}$ term whose multiplier is
    $h-1=n>0$. It therefore makes the displayed difference strictly
    positive in the signed-row convention, or strictly negative in the
    natural positive convention. Independently,

    

$$
\psi(x)=\sum_{r=1}^k\frac{c_r}{x+r^2},\qquad c_r>0,
$$



    is strictly decreasing together with $q$, so
    $\operatorname{NB}_A(V\psi)>0$ by the same symmetrized covariance
    identity. Both terms in the corrected target reinforce and prove

    

$$
\boxed{[z^{n+2}]\Gamma\ne0}
$$



    throughout this subfamily. Since $\deg W\le4<n+2$, this also proves
    $[z^{n+2}]\Delta\ne0$. It does not cover odd $D\ge5$ or address the
    primitive-height/content threshold.

The centrally audited hashes for item 47 are:

```
0a622e8048d2a407db2edb3e18aee0726c3dced1dab3e79145f890d7d39444e5  sources/root_unity_forced_odd_m_D3_covariance_theorem.md
645d87bf0afd0a1c0f7c30b8e72b742e682be2563bd4b7b59b5011f41c688b89  scripts/root_unity_forced_odd_m_D3_covariance_certificate.py
f126cb4a5f5b09f0ae3658e814d4c9967e242dbcad1ac01990f0d50be91e3bd2  results/root_unity_forced_odd_m_D3_covariance_certificate.json
5c9b319c056f6c2bfb1539212455dd8771e5ea2254065b8eb39c16c14de2e793  results/root_unity_forced_odd_m_D3_covariance_hashes.sha256
```

The centered phase, Bernoulli moment normalization, covariance factorization,
strict monotonicities, central integrability, and raw sign anchor were checked
independently. The 24-row exact replay, manifest, Python compilation, and
control-byte audit all pass. Item 47 is a corrected nonvanishing theorem, not
a classification of $e+\pi$.

48. The complete three-frequency slice of the last parity-forced family is now
    closed at every admissible endpoint degree:

    

$$
m=3,\qquad n\ge4\text{ even},\qquad
       D=2d+1\ge3\text{ odd},\qquad D\le n.
$$



    With $h=n+1$, $V(x)=(1+x)^h$, and the corrected positive Stieltjes
    normalization, put

    

$$
\rho(x)=\frac{w_0}{x}+\frac{2w_1}{x+1},\qquad
       b=\mathcal E(V\rho),\qquad \mathcal E=2x\frac d{dx}+h+1.
$$



    A direct phase reconstruction against the original cardinal determinants
    gives

    

$$
[z^{n+D-1}]\Gamma=C_* (-1)^d\pi^{2d}
       \left\{\operatorname{NB}_A(V\psi)
       -\bigl(\operatorname{NB}_A(b)-\operatorname{NB}_G(b)\bigr)\right\}.
$$



    The new ingredient is a total-nonnegativity theorem for the coefficient
    matrix containing this actual border row exactly once. After removing the
    common factor $(1+x)^{h-2}$, the normalized residue parameter is
    $c=2^{1-h}$. At $c=0$, and separately at $c=1/2$, the ordered
    coefficient rows factor into consecutive $1$-by-$2$ and $2$-by-$2$
    TN blocks followed by a repeated-target selector whose minors are all zero
    or one. Every minor containing the single border is affine in $c$, so
    convexity covers the actual value.

    The csch pairing kernel has the exact reverse-TP representation

    

$$
\langle x^j,Q_v\rangle=
      4\Gamma(2j+h+1)\pi^{-(2j+h+1)}
      \sum_{q\ge0}(2q+1)^{-2((h+1)/2+j-v)}.
$$



    Cauchy--Binet and generalized Vandermonde signs therefore turn the bordered
    coefficient theorem into an ordinary TN moment matrix after column reversal.
    A terminal-flag ratio lemma, proved by compatible right-to-left row
    replacements and Sylvester condensation, yields

    

$$
\operatorname{NB}_A(b)\le\operatorname{NB}_G(b).
$$



    The remaining term is strict because

    

$$
\psi[x_1,\ldots,x_{d+1}]
       =\frac{(-1)^d\gamma_h}{\prod_j(1+x_j)},
       \qquad \gamma_h>0,
$$



    and Andreief's identity cancels this divided-difference sign against the
    decreasing csch-variable Vandermonde. Hence

    

$$
\boxed{[z^{n+D-1}]\Gamma\ne0},\qquad
       \boxed{\deg\Delta=n+D-1}
$$



    for every tuple above. This proof uses the actual border only once and does
    not assert the known-false generic-residue or full-Lace strengthening.
    Frequencies $m\ge5$ and the primitive-height/content threshold remain
    open.

The centrally audited hashes for item 48 are:

```
b4edfce7f56b1b1afb41aee93a79c2d39599e05b4cc105d1b3449a2e25c56d8e  sources/root_unity_forced_odd_m3_next_coefficient_theorem.md
5a715d699081e503b19fcc6d504cf734e9f2537cf0714a5438a2ef648bc44755  scripts/root_unity_forced_odd_m3_next_coefficient_certificate.py
0e25e85ea079fe1cdc3273fba642b79b3488bb90b6d433608cebe7dbf9b180cb  results/root_unity_forced_odd_m3_next_coefficient_certificate.json
51615cb37312555a897f0d05100022d555cc67ae013a9515843a78963cbdf358  results/root_unity_forced_odd_m3_next_coefficient_hashes.sha256
```

The one-border factorization, selector minors, reverse-TP kernel, flag-ratio
signs, strict divided difference, and raw phase identification were checked
line by line. The exact rational replay, hash manifest, Python compilation,
and control-byte audit all pass. Item 48 is a corrected nonvanishing and degree
theorem, not a classification of $e+\pi$.

51. The now-certified nonzero coefficients give a rank-independent corrected
    content cap and primitive-height lower bound. With

    

$$
N=q_E\Delta,\qquad
       \mathfrak c_E=\operatorname{cont}(N),
$$



    define

    

$$
\mathcal I_{m,n,D}=
      \begin{cases}
       \{2D-1,\ldots,n+D\},&m\text{ odd},\\
       \{0\}\cup\{2D-1,\ldots,n+D\},&m\text{ even},
      \end{cases}
      \qquad
      G_{\rm cert}=\gcd_{\ell\in\mathcal I_{m,n,D}}|N_\ell|.
$$



    The top-cardinal theorem, the external-node forced-family theorem, and the
    corrected even-frequency constant-border theorem imply
    $G_{\rm cert}>0$ for every $m\ge2,n\ge D\ge2$. Therefore

    

$$
\boxed{\mathfrak c_E\mid G_{\rm cert}},\qquad
       \boxed{H(N/\mathfrak c_E)\ge H(N)/G_{\rm cert}}.
$$



    This remains valid when the ambient corrected map is rank deficient. If
    $A_K$ is the cleared endpoint matrix, $\delta_K$ its maximal-minor
    gcd, $p$ the saturated Pluecker vector, $E^*=q_EE$, and

    

$$
\mathscr B_{a,b}=\det\!\begin{pmatrix}A_K\\e_a^T\\E_b^*\end{pmatrix},
$$



    then the cap can be reconstructed without an unsaturated nullspace basis:

    

$$
N_\ell=-\delta_K^{-1}\sum_{a+b=\ell}\mathscr B_{a,b}
      \quad(\ell\ge2D-1),
      \qquad
      N_0=q_Ep_{01}-\delta_K^{-1}\mathscr B_{0,0}\quad(m\text{ even}).
$$



    At universal clearing $Q$, put
    $G_Q=(Q/q_E)G_{\rm cert}$. Then the item-39 content threshold can hold
    only if

    

$$
(\kappa+1)\log G_Q>
      \kappa\log H(N_Q)+\log(C_0H_W)-2\mathcal G_1-\log Q.
$$



    This is a necessary test, not a sufficient estimate. Exact rows show why:
    for $(m,n,D)=(3,5,4)$, the selected high-tail cap is $729$ times
    the true content after normalization; for $(4,6,4)$, adjoining the
    certified constant reduces the overestimate from $93312$ to $128$,
    but does not remove it. Thus the theorem sharpens the corrected arithmetic
    certificate and can exclude parameter choices, but it changes no asymptotic
    exponent obstruction and proves no irrationality or transcendence result.

The item-51 package is:

```
4efb563c8a122bdf7d180769de35916f2e1b1001bb6089268d8401e97a426f8e  sources/root_unity_certified_coefficient_content_cap.md
4054f428bba6858f8461d1cb75a4f28a0e11f0e57c677b9775593e1fdb0c6a53  scripts/root_unity_certified_coefficient_content_cap_certificate.py
1ce20377433d852dc11ca130b83db19c921b8f43028c88cb2e61bf42797f1d16  results/root_unity_certified_coefficient_content_cap_certificate.json
3841f62ad41719ce681227a14838dd7ff0957cdab9d7ca32c85a8a58ed8d02bc  results/root_unity_certified_coefficient_content_cap_hashes.sha256
```

The exact replay checks nine tuples, every augmented-determinant identity,
content divisibility, the primitive-height lower bound, and invariance under
universal clearing. Its grid digest is
`5dbba748eb3a926c13da2dc16032008fa8f94fc020b169ae97f0a4a51b9714e0`;
the clean run took 6.27 seconds and peaked at 80.809 MiB RSS.

52. The leading corrected coefficient has an exact dyadic content cap on the
    infinite subfamily

    

$$
m=3,\qquad D=2,\qquad h=n+1=2^q,\qquad q\ge2.
$$



    The centered checkerboard theorem makes the saturated endpoint exterior
    vector exactly $p=e_0\wedge e_2$, represented by $C=1,D=z^2$. If
    $u_h$ is the explicit odd integer obtained from the top cardinal, then

    

$$
\boxed{[z^{h+1}]\Delta
       =-\frac{u_h}{2^{h+q+1}(h-1)!}},\qquad
      \boxed{v_2([z^{h+1}]\Delta)=-2h}.
$$



    The proof isolates a unique least-valuation logistic-moment term: among
    $s\le3h/2$, only $s=h$ has $v_2(s)=q$, and the coefficient of
    $X^{2h-1}$ in the relevant integer cardinal numerator has valuation one.
    If $q_\Delta$ is the intrinsic least denominator and
    $\mathfrak c_\Delta$ the content after minimal clearing, reduction of the
    leading coefficient gives

    

$$
2^{2h}\mid q_\Delta,\qquad
      \mathfrak c_\Delta\mid N_h,\qquad
      2\nmid\mathfrak c_\Delta,
$$



    with $\log|N_h|=O(h\log h)$. At universal clearing $Q$, this also gives

    

$$
v_2(\operatorname{cont}(Q\Delta))\le v_2(Q)-2h.
$$



    This is a genuine all-parameter corrected-content filter, but one leading
    coefficient cannot lower-bound primitive height: the still-allowed extreme
    $q_\Delta=D_h$, $\mathfrak c_\Delta=|N_h|$ leaves primitive leading
    coefficient $\pm1$. A second-coefficient gcd or full intrinsic-content
    theorem remains necessary.

The item-52 package is:

```
2cb92883e8af3470a4148110b3648cab1862d7193fb610204f3b458c107bc554  sources/root_unity_leading_coefficient_dyadic_content_barrier.md
a3723630fee4ecf477964dfef2ca2d969fe86cd54ba9d9da40599cc9418e0281  scripts/root_unity_leading_coefficient_dyadic_content_certificate.py
e675b4ae6920fdc6bbc2229f1e527eda412ce1c469eb2f32914fa1fb42347b9e  results/root_unity_leading_coefficient_dyadic_content_certificate.json
ee6b91fe50749b7e894baf09009e5bd6434bf80657d552fab8ee8ecfb00dfbb4  results/root_unity_leading_coefficient_dyadic_content_hashes.sha256
```

The deterministic exact replay covers $q=2,\ldots,6$, reconstructs the
complete corrected polynomial at $h=4,8,16$, and checks the saturated
checkerboard normalization and valuation term by term. The source records
resident use below 0.2 GiB, and the JSON certifies it stayed below the 2 GiB
cap. Finite observed contents are not extrapolated. Item 52 does not classify
$e+\pi$.

53. The corrected asymptotic-capacity audit gives a basis-free arithmetic
    ledger for the two-column and exterior-sum constructions. For the primitive
    saturated Pluecker vector $p$, it proves universal majorants of the form

    

$$
\begin{aligned}
      H(N_Q)&\le P_0\{Q\omega_D+D(D+1)mC_B\},\\
      H(W(\overline R_C,\overline R_D))
        &\le2R_D(m+1)(n+1)(n+m)P_0(Q+2C_B)^2,
    \end{aligned}
$$



    linear in $H(p)$, rather than quadratic in an arbitrary endpoint-basis
    height. With $\chi=\log\operatorname{cont}(Q\Delta)$ and
    $\kappa=r^2d+r-1$, the exact leading content threshold is

    

$$
(\kappa+1)\chi>
      \kappa\log H(N_Q)+\log(C_0H_W)-2\mathcal G-\log Q,
$$



    with the appropriate finite field/measure constants added for literal use.
    The only universal lower bound currently proved is $\chi\ge0$, while the
    Cramer interpolation majorant has logarithm $mn^2\log n+O_m(n^2)$.

    The source also formulates the conditional nondecomposable exterior-sum
    regime. With $N=\binom\nu2>S=n+D-d$, high coefficients can be killed by
    rational linear algebra using $\nu=O(\sqrt n)$, losing only
    $O(\sqrt n)$ origin order and replacing a growing cofactor exponent by a
    constant Siegel exponent. This leaves two indispensable inputs: a nonzero
    low-image rank gap and intrinsic remainder/content control on the
    $O(n\log n)$ scale. Item 57 supplies exact finite rank information but no
    all-parameter rank-gap theorem.

    **Analytic supersession.** The uncentered gains and radii printed in item
    53's source are valid weaker estimates but are superseded by item 55. Every
    current threshold must replace $\mathcal G$ by the centered gain

    

$$
\mathcal G_{\rm ctr}
       =(L-n)\log\frac{2(L-n)}{e\pi m}-n\log\pi.
$$



    The denominator, coefficient-height, primitive-content, degree-regime,
    Siegel, and conditional intrinsic-height ledgers of item 53 remain valid
    after that substitution. Item 55 proves that even the larger centered gain
    remains below the denominator scale, so the principal obstruction is
    unchanged.

The item-53 package is:

```
3e444b2b42ddec77985e100acfe0e484c0059e8ea5e6e15ecfe32e8ff8bfa8db  sources/root_unity_corrected_asymptotic_capacity_barrier.md
bfd7023b7e3c607f90bb7e0e42ccc219d859764e98f8fe4b15f876d6d1f48cee  scripts/root_unity_corrected_asymptotic_capacity_certificate.py
6b27c3bddb66a9b2bbcf04fbf80f7b0b44e23f9060feefa9fc6852b7adf85c18  results/root_unity_corrected_asymptotic_capacity_certificate.json
dfee4540b150f82e607489b6494510a0d71f439f7230b6dc16e4702a8ac18cf4  results/root_unity_corrected_asymptotic_capacity_hashes.sha256
```

The deterministic certificate replays the exact denominator and universal
majorants, representative degree rows, Segre dimensions, exterior/Siegel
counts, and conditional thresholds. Its JSON records peak RSS 16,512 KiB,
below the 2 GiB cap. Finite rows are diagnostics; the all-parameter claims are
proved in the source. Item 53, with item 55's analytic correction understood,
does not classify $e+\pi$.

54. The unconstrained full-endpoint parity problem is exactly a Segre-section
    problem. For every parity eigenvector $C(-z)=\sigma C(z)$, the endpoint
    specialization obeys

    

$$
\boxed{\beta_C(-z)+m\sigma C(z)=-\sigma\beta_C(z)}.
$$



    Hence $\widehat\beta=\beta+(m/2)I$ and
    $\mathcal A=\partial_z-\widehat\beta$ reverse parity. For even
    $n=2d$, an odd/even pair $C=zU(z^2),D=V(z^2)$ satisfies

    

$$
\Delta(z)=xU(x)(\mathcal QV)(x)-V(x)(\mathcal PU)(x),
      \qquad x=z^2.
$$



    Thus the high corrected coefficients are rational hyperplanes in the
    Segre coordinates on

    The ambient variety is $\mathbb P^{d-1}\times\mathbb P^d$, of
    dimension $2d-1$ and degree ${2d-1\choose d-1}$.

    The complete exact quadratic-collapse chart audit at $m=2$ gives closed
    point degrees $1+2$ for $n=4$, $4+6$ for $n=6$, and $15+20$
    for $n=8$. Therefore the rational quadratic branch visible at $n=4$
    already fails at $n=6$; projective nonemptiness over
    $\overline{\mathbb Q}$ does not imply rational descent. Allowing quartic
    output gives a rational-line component at $n=6$ and a rational point on
    a genus-six component birational to a smooth plane quintic at $n=8$.
    The displayed primitive endpoint values at $i\pi$ are all larger than
    one. No infinite rational section, descent, primitive-content theorem, or
    small-value family follows.

The item-54 package is:

```
060154ed344344caa5b34974851a163edf3ddee745930fb15b4779c26c8b2c34  sources/root_unity_unconstrained_parity_segre_collapse_audit.md
0741815a1dfc2c6e672e4d580d2838ab02a5a1a9776a0c01bb0aa359b2d498e4  scripts/root_unity_unconstrained_parity_segre_collapse_certificate.py
29fe44f0ed9191eff4729d026934cf240435238393ed839bae0a1c4af4f72744  results/root_unity_unconstrained_parity_segre_collapse_certificate.json
618903be6ca94dd687595489edd0e01dbb0955da31e5afc188a359278d410e2c  results/root_unity_unconstrained_parity_segre_collapse_hashes.sha256
```

The deterministic replay reconstructs the reflection matrices, parity
operators, every projective chart at $n=4,6,8$, the irreducible eliminants,
the rational-line cofactor family, and the smooth genus-six component. Measured
replay metadata, not embedded as a JSON resource field, are 21.751 seconds and
92.035 MiB peak RSS. The finite chart classification is only for the displayed
three tuples. Item 54 does not classify $e+\pi$.

55. Centering the exterior frequency spectrum corrects the Schwarz ledger.
    Every exterior Wronskian sum has raw frequencies $0,\ldots,2m$. The exact
    relabeling

    

$$
\widetilde F(z)=e^{-mz}F(z)
$$



    moves them to $-m,\ldots,m$, preserves coefficient height and origin
    multiplicity, and gives

    

$$
\widetilde F(i\pi)=(-1)^mF(i\pi).
$$



    The coarse circle type is therefore $m$, not $2m$. If $A=L-n$, the
    exact stationary radius and one-column gain are

    

$$
\boxed{\rho_{\rm ctr}=\frac{2A}{m}},\qquad
      \boxed{\mathcal G_{\rm ctr}
       =A\log\frac{2A}{e\pi m}-n\log\pi}.
$$



    This adds $A\log2$ per column, or $2A\log2$ to the exterior estimate.
    The allowed root-of-unity endpoint range is always in the interior-radius
    case. More importantly, the source proves the stronger all-parameter
    denominator inequality

    

$$
\boxed{2\mathcal G_{\nu,{\rm ctr}}<\log Q_{m,n}}
      \qquad(m\ge2, n\ge D\ge2, 2\le\nu\le D+1).
$$



    Thus a content-free universal certificate remains negative when the
    Wronskian-height majorant is at least $Q^2$. The correction changes
    finite constants by $O(n)$ at fixed $m$, but not the leading
    $n\log n$ gain or the missing intrinsic-height/content theorem. It
    supersedes all earlier uses of the uncentered type-$2m$ formula,
    including item 53's analytic expressions.

The item-55 package is:

```
55bc0e5ea75dfb52da3e26105c20aa8edfb434be9598c669e20e86975e2367cb  sources/root_unity_centered_frequency_schwarz_correction.md
e878085f24618bc338a5985fde2fb64f68874bbcc960f19d6763142ccfba07b0  scripts/root_unity_centered_frequency_schwarz_certificate.py
f2702805ad553498e647af92b3d400419d09145008985acbf8812d1e3fa102ef  results/root_unity_centered_frequency_schwarz_certificate.json
133b0e7120ba58bfe24543510319c5427c63c4653e318a4a126e05fc61fc2d43  results/root_unity_centered_frequency_schwarz_hashes.sha256
```

The deterministic replay checks exact frequency dictionaries, the endpoint
sign, symbolic optimization and boundary match, 7,315 endpoint-radius rows,
and 8,265 denominator/gain diagnostics. Measured replay metadata, not embedded
as a JSON resource field, are 1.604 seconds and 63.840 MiB peak RSS. The
inequality itself is proved analytically, not inferred from those grids. Item
55 supplies no rank gap, content theorem, or classification of $e+\pi$.

56. Reflection gives an exact reciprocity law inside the centered exterior
    construction. If $C(-z)=\sigma_C C(z)$, then

    

$$
\boxed{e^{mz}R_C(-z)=(-1)^m\sigma_C R_C(z)}.
$$



    For a parity-homogeneous exterior vector with
    $(J\wedge J)p=\tau p$, the centered Wronskian sum
    $G_p=e^{-mz}F_p$ satisfies

    

$$
\boxed{G_p(-z)=-\tau G_p(z)},\qquad
      a_{-r,k}=(-\tau)(-1)^ka_{r,k}.
$$



    Same-parity blocks therefore have the uniform refinement
    $\operatorname{ord}_0G_p\ge2L+1$; a single favorable block reaches
    $2L+3$, while mixed parity retains $2L$. Opposite frequencies pair
    into exact $\cosh$ or $\sinh$ terms, replacing the crude slot factor by

    

$$
D_m(R)=1+2\sum_{r=1}^m\cosh(rR)
       =e^{mR}\frac{1-e^{-(2m+1)R}}{1-e^{-R}}.
$$



    This is a strict finite prefactor improvement whenever a noncentral
    coefficient occurs, but $D_m(R)\sim e^{mR}$: reflection does not reduce
    type below $m$. Its extra origin order is bounded and changes the gain
    only by $O(\log n)$. Exact finite rows retain both extreme frequencies
    and attain the predicted minimal orders, so no stronger type or uniform
    origin factor follows from reciprocity alone.

The item-56 package is:

```
f33c84043e777fa0939043f29ae4905311c7be233bd86ac64235a8199b23fc57  sources/root_unity_centered_exterior_reflection_reciprocity.md
712b9226e6226496835458468007c9383542b8802cb594f84996aacd85b439ce  scripts/root_unity_centered_exterior_reflection_certificate.py
49b31b503ee952d6d7016ff456800e6ee629e12b4b087d7963279ac1fb81cce4  results/root_unity_centered_exterior_reflection_certificate.json
d00fda1642ea6e2b339a873a8f4d72c6e58fb0bf50a11450a2797905a510f984  results/root_unity_centered_exterior_reflection_hashes.sha256
```

The deterministic replay checks 38 full-endpoint monomial pairs and four
genuinely nondecomposable parity-homogeneous sums, including coefficient
reciprocity, exact Taylor orders, and nonvanishing extreme frequencies.
Measured replay metadata, not embedded as a JSON resource field, are 1.035404
seconds and 66.554688 MiB peak RSS. These finite rows are sharpness
diagnostics, not an all-parameter nonvanishing claim. Item 56 does not classify
$e+\pi$.

57. Arbitrary nondecomposable exterior sums are an exact extension of the
    corrected two-column construction. For a reduced endpoint space $E_\nu$
    and any $p\in\bigwedge^2E_\nu$, not necessarily a simple wedge, linearity
    gives

    

$$
\boxed{\mathcal W_p(i\pi)=\Delta_p(i\pi)},\qquad
      \boxed{\operatorname{ord}_0\mathcal W_p\ge2L_\nu},
      \quad L_\nu=m(n+1)+D+1-\nu.
$$



    If $T_{>d}$ is the map of corrected coefficients above degree $d$, a
    nonzero low-degree endpoint exists exactly when

    

$$
\boxed{\operatorname{rank}T_{\rm all}>
             \operatorname{rank}T_{>d}}.
$$



    Dimension counting alone is genuinely insufficient. At
    $(m,n,D,\nu,d)=(2,11,11,7,2)$, one has
    $\binom72=21>20$, but the full and tail ranks both equal 18, so the
    three-dimensional tail kernel is the full kernel. Raising $\nu$ to 8
    restores a rank gap of two. A separate exact counterexample shows that
    parity-maximality cannot supply the missing universal proof:
    $(m,n,D)=(2,21,7)$ has full block ranks $14+12=26$, versus parity cap
    27, and tail ranks $12+11=23$, versus cap 25, although its actual
    low-degree gap remains three.

    The selected usable exterior vectors have skew ranks 4, 6, or 8 for
    $n\ge3$, so they are genuinely nondecomposable rather than disguised
    single Wronskians. The minimal full-endpoint variant has monomial basis
    height one and removes the endpoint-lattice basis cost. Nevertheless every
    certified centered $r=1$ margin is negative, and the present universal
    interpolation majorant still has logarithm $mn^2\log n+O_m(n^2)$,
    against centered analytic gain only $(m-1)n\log n+O_m(n)$. This is a
    no-go for the current majorant, not a lower bound on intrinsic height. The
    surviving requirements are a weaker all-parameter rank-gap theorem and an
    intrinsic saturated remainder/content theorem on the $O(n\log n)$ scale.

The item-57 package is:

```
adaffc0036744504f9dfd39cdced4a95c95cab5540b75ddceb466e31085d989f  sources/root_unity_nondecomposable_exterior_sum_audit.md
3056828b21e08759fd7520c169db074aa9250c4e8bf4c8b6357c460881c3dd5f  scripts/root_unity_nondecomposable_exterior_sum_certificate.py
5f024e764a4450c0bd9541ee5115fe5261846c5ca389b6819826b9691d18e1ea  results/root_unity_nondecomposable_exterior_sum_certificate.json
a491b884e93a73f13e098d6921c4f6b112dcbed0189585f2765e59f03a8866d7  results/root_unity_nondecomposable_exterior_sum_hashes.sha256
```

The exact certificate builds saturated endpoint and tail kernels by
transformed HNF, verifies the exterior embedding and endpoint identity,
constructs every cleared Wronskian sum, and checks complete origin jets. It
contains 22 diagonal rows, one rank-gap rescue, 22 full-endpoint rows, 154
small parity-rank tuples, and the exact outside-grid parity-maximality
counterexample. Two final replays were byte-identical; the larger measured
peak was 929,576 KiB (about 907.8 MiB), below the 2 GiB cap. The bounded
$\{-1,0,1\}$ LLL-coordinate search is not a shortest-vector certificate,
and no finite rank or height pattern is extrapolated. Item 57 does not classify
$e+\pi$.

58. Endpoint multiplication has an exact low-rank displacement which produces
    a universal square/product survivor. For

    

$$
m\ge2,\qquad n\ge m+1,\qquad M=m(n+1),
$$



    put

    

$$
s_{m,n}=
      \begin{cases}
       m-1,&m\text{ odd and }n\text{ even},\\
       m,&\text{otherwise}.
      \end{cases}
$$



    The endpoint-displacement square theorem constructs an explicit primitive
    $C_{m,n}\in\mathbb Z[z]$, of degree exactly $s_{m,n}$, such that in
    every full endpoint space with $s_{m,n}+1\le D\le n$,

    

$$
\boxed{R_{zC_{m,n}}=zR_{C_{m,n}},\qquad
      W(R_{C_{m,n}},R_{zC_{m,n}})=R_{C_{m,n}}^2,}
$$



    and

    

$$
\boxed{\Delta(C_{m,n},zC_{m,n})=C_{m,n}^2.}
$$



    The square has origin order at least $2M$, and its corrected endpoint is
    nonzero, primitive, and of degree at most $2m$. The mechanism is the
    all-parameter factorization

    

$$
[z^b](\beta_{zC}-z\beta_C)
       =\sum_{q=0}^{m-1}p_{bq}H_q(C),
$$



    so endpoint multiplication displacement has rank at most $m$. Initial
    nonzero logistic minors give $C_{m,n}$ by an explicit parity-block
    cofactor.

    The polarized theorem is also exact. If
    $U_D=\ker H\subseteq\mathbb Q[z]_{\le D-1}$, then for $D\ge m+1$

    

$$
\dim U_D=D-m,\qquad
      \Delta(C,zD)+\Delta(D,zC)=2CD
      \quad(C,D\in U_D),
$$



    and

    

$$
\dim(U_DU_D)\ge2D-2m-1.
$$



    Hence $U_DU_D\cap\mathbb Q[z]_{\le2m}\ne0$, proving a
    basis-independent all-parameter exterior rank gap at target degree
    $2m$. This is a product-space theorem, not an extrapolation from the
    finite replay.

    Primitive normalization cancels the universal two-copy clearing exactly.
    With the lower-parameter clearing $Q_-$,

    

$$
W(Q_-R_C,zQ_-R_C)=Q_-^2R_C^2
$$



    has endpoint content exactly $Q_-^2$; after intrinsic division the
    analytic function is $R_C^2$. Nevertheless the proved fixed-$m$
    bounds only give

    

$$
\log H(C_{m,n})
       \le r_{m,n}mn\log n+O_m(n),\qquad
      \log H(R_{C_{m,n}})
       \le\log H(C_{m,n})+mn\log n+O_m(n),
$$



    with $r_{m,n}\le\lceil m/2\rceil$. All fourteen exact $m=2,3$
    sequence diagnostics have a negative leading degree-one-field measure
    margin; those finite values are warnings, not asymptotic lower bounds.
    Thus the theorem removes the universal $Q^2$ normalization cost but does
    not prove the required primitive-factor height/value inequality.

The item-58 package is:

~~~
1883582877ed7f9b7fb6fdf7c99d66fa933bb9040f165cfdbab3bbcb2ca44e8b  sources/root_unity_endpoint_displacement_square_theorem.md
4bda9773163ec63cd4df868d1f0032cade310ea1525952540b1806aef214cb25  scripts/root_unity_endpoint_displacement_square_certificate.py
68be9373f11cef9a734a18412b091f4ec555c6aed582301e41c777dc9acd885a  results/root_unity_endpoint_displacement_square_certificate.json
84d6549d8293ddd022ff875b2bae47921b1db547a64b15606b1528e26d30d964  results/root_unity_endpoint_displacement_square_hashes.sha256
~~~

The deterministic exact replay checks six structural anchors and fourteen
fixed-$m$ sequence rows. The final conservative measured run took about
31.5 seconds and reported 971,304 KiB peak RSS (about 948.54 MiB), below the
2 GiB cap. Item 58 is an all-parameter square/product theorem plus finite
height diagnostics; it does not classify $e+\pi$.

59. The genuinely nondecomposable third exterior sum has an exact corrected
    endpoint jet and a real cube-root dimension gain. For
    $p\in\bigwedge^3E_\nu$, define

    

$$
\mathcal W^{(3)}_p
       =\sum_{i<j<k}p_{ijk}
        \det(R_i,R_i',R_i'').
$$



    With

    

$$
\beta_C=T_C(z,-1),\qquad
      \theta_C=(\partial_z-\partial_y)T_C(z,-1),
$$



    the exact endpoint jet at $z=i\pi$ is

    

$$
R_C=C,\qquad R_C'=C'-\beta_C,\qquad
      R_C''=C''-\beta_C-2\theta_C.
$$



    Therefore

    

$$
\boxed{\Delta^{(3)}(C_1,C_2,C_3)
       =\det(\mathbf C,\mathbf C'-\boldsymbol\beta,
        \mathbf C''-\boldsymbol\beta-2\boldsymbol\theta),}
      \qquad
      \boxed{\mathcal W^{(3)}_p(i\pi)=\Delta^{(3)}_p(i\pi).}
$$



    Universally,

    

$$
\deg\Delta^{(3)}_p\le2n+D,\qquad
      \operatorname{ord}_0\mathcal W^{(3)}_p\ge3L_\nu,
$$



    while the analytic frequencies are $0,\ldots,3m$, the polynomial
    coefficient degree is at most $3n$, and midpoint centering gives type
    $3m/2$.

    At target degree $d$, the third-exterior domain and high-tail counts are

    

$$
N_3={\nu\choose3},\qquad S_3=2n+D-d.
$$



    Thus fixed oversampling permits
    $\nu\sim\{6\tau(2+\delta)n\}^{1/3}$, a genuine
    $\Theta(n^{1/3})$ endpoint-dimension loss. A usable endpoint still
    exists if and only if

    

$$
\operatorname{rank}\mathcal T^{(3)}_{\rm all}
       >\operatorname{rank}\mathcal T^{(3)}_{>d};
$$



    item 59 proves no all-parameter rank-gap theorem.

    The exact normalization is the decisive arithmetic warning:

    

$$
N^{(3)}_{Q,p}=Q^2\Delta^{(3)}_p\in\mathbb Z[z],
      \qquad
      \overline{\mathcal W}^{(3)}_p=Q^3\mathcal W^{(3)}_p.
$$



    If $c_p=\operatorname{cont}(N^{(3)}_{Q,p})$, then

    

$$
F_p=\frac{\overline{\mathcal W}^{(3)}_p}{Qc_p},
      \qquad F_p(i\pi)=\frac{N^{(3)}_{Q,p}(i\pi)}{c_p}.
$$



    Hence two copies of $Q$ remain in the present universal analytic-height
    majorant. Although the centered analytic gain triples, the previously
    proved inequality $2\mathcal G_{\nu,\rm ctr}<\log Q$ makes the
    content-free universal certificate strictly negative. In an intrinsic
    matched cubic-height model, both the height payment and gain triple, so
    the per-column threshold is exactly the same as for $k=2$, not better.

    The four exact $d=2$ rows have rank gap three, contraction rank six,
    primitive quadratic output, both extreme frequencies, and the predicted
    origin-order lower bound. These are finite diagnostics only; their
    25--56 digit primitive heights are arithmetic warnings rather than
    asymptotic bounds.

The item-59 package is:

~~~
6f0b2d7908da9f6b67135468e5e8744bbd9f1785963361dcd21a8d8e0923a281  sources/root_unity_third_exterior_sum_endpoint_audit.md
94623603b6bbe14dbdd736e04c595408d3af28dd1db71d31aa17f8178c64faac  scripts/root_unity_third_exterior_sum_certificate.py
3d09b003816d84ba655e2de8f497494e6115e15bb995c93da2975cf0a07b370c  results/root_unity_third_exterior_sum_certificate.json
16f8e44aa10be4345aae9de08b3c179d9ec381f30c8f9194d0faa6f709eb0492  results/root_unity_third_exterior_sum_hashes.sha256
~~~

The deterministic replay took 8.574 seconds and peaked at 70.887 MiB RSS,
below the 2 GiB cap. The endpoint-jet, normalization, support, order,
dimension asymptotics, and universal-ledger obstruction are theorems; the
four rank gaps are finite diagnostics. Item 59 does not classify $e+\pi$.

60. Saturating the complete global $k=2$ Wronskian image after high-tail
    cancellation exposes an exact and very large removable lattice index.
    Let $R\in\mathbb Z^{r\times P}$ be a full-row-rank basis of the raw
    global image lattice. If a transformed tall HNF is

    

$$
UR^t=\begin{pmatrix}H_0\\0\end{pmatrix},
      \qquad U\in\operatorname{GL}_P(\mathbb Z),
$$



    then

    

$$
\boxed{S=(U^{-1}_{[:,0:r]})^t}
$$



    is an exact basis of
    $L_{\rm sat}=\operatorname{span}_{\mathbb Q}(R)\cap\mathbb Z^P$, and

    

$$
\boxed{R=H_0^tS,\qquad
      [L_{\rm sat}:L_{\rm raw}]=|\det H_0|.}
$$



    The same index is the product of the nonzero Smith invariants and the gcd
    of all maximal minors. It is also the exact covolume ratio:

    

$$
\det(RR^t)
       =[L_{\rm sat}:L_{\rm raw}]^2\det(SS^t).
$$



    If $g$ is the common content of $R$, then

    

$$
[L_{\rm sat}:L_{\rm raw}]=g^rI_{\rm cross}.
$$



    Moreover $\operatorname{Sat}(cL)=\operatorname{Sat}(L)$ for every
    nonzero integer $c$. These are all-parameter lattice identities: a
    $Q^2$-scale presentation of the complete Wronskian map does not itself
    impose a $Q^2$-scale primitive global height.

    The endpoint compatibility was checked with its actual scalar. If
    $N:x\mapsto Q\Delta_x$ and $\mathcal E$ evaluates global frequencies
    at $i\pi$, then

    

$$
\boxed{\mathcal E(Gx)=Q\,Nx.}
$$



    Consequently rational saturation of the global image preserves every
    killed high endpoint coefficient exactly.

    On the representative exact grid
    $m\in\{2,3\}$, $n\in\{2,3,5,8,10\}$, $d=2$, the common scalar
    $g^r$ accounts for $96.3970\%$ to $100\%$ of the logarithmic
    saturation index. For $n\ge3$,

    

$$
\frac{\log\lambda_{\rm sat}^{\rm LLL}}{n\log n}
      \in[2.63,3.74]\quad(m=2),\qquad
      \in[4.71,6.12]\quad(m=3).
$$



    The corresponding raw LLL log norms reach $355.64$ and $722.80$.
    This is exact finite evidence consistent with an intrinsic
    $O(n\log n)$-scale global image, not an asymptotic theorem. There is no
    uniform Smith/Pluecker-height formula, LLL is not an SVP certificate, and
    a short saturated global vector can have zero corrected low endpoint.

The item-60 package is:

~~~
cc56e51aa5ce1f7f1dadb2c10edf96fbdacadb2ca660f20130f2b57dec4f13ab  sources/root_unity_k2_global_image_saturation_audit.md
588393ba1cb273d13034cc069cca7b3f507c8b9adf62f13a8d6e8e71bb15d470  scripts/root_unity_k2_global_image_saturation_certificate.py
b66a378153646894f7bc923892f8ee50bb2dc8a665a56030a545d6d0488f1c92  results/root_unity_k2_global_image_saturation_certificate.json
72f63950f3e197f921bb256e84f6938fb7713a253183bf46e83a381cd2942e4f  results/root_unity_k2_global_image_saturation_hashes.sha256
~~~

The item-60 manifest also pins and verifies the item-57 constructor dependency
at SHA-256
3056828b21e08759fd7520c169db074aa9250c4e8bf4c8b6357c460881c3dd5f.
Two deterministic clean replays produced byte-identical JSON; the conservative
run took 32.004 seconds and peaked at 240.594 MiB RSS, below the 2 GiB cap.
The HNF/Smith/covolume formulas are theorems; the displayed growth pattern is
finite evidence only. Item 60 does not classify $e+\pi$.

61. Gaussian mixing of the even and odd corrected endpoint blocks gives an
    exact real phase descent, but no improved $e$-measure exponent. If

    

$$
N_{\rm e}\in\mathbb Z[z^2],\qquad
      N_{\rm o}\in z\mathbb Z[z^2],
$$



    define $\widetilde N=N_{\rm e}-iN_{\rm o}$. With
    $n_j=[z^j](N_{\rm e}+N_{\rm o})$,

    

$$
A(X)=\sum_j(-1)^{\lfloor j/2\rfloor}n_jX^j
$$



    gives the exact identities

    

$$
\boxed{\widetilde N(z)=A(-iz),\qquad
      \widetilde N(i\pi)=A(\pi).}
$$



    Gaussian content is exactly the ordinary coefficient gcd, up to a unit,
    and Gaussian house equals ordinary integer height. In particular, mixing
    two blocks replaces their separate contents by their gcd; it creates no
    multiplicative content bonus. The corresponding analytic combination
    costs at most a fixed factor $\sqrt2$ in coefficient house and has the
    same centered Schwarz gain.

    Under the temporary hypothesis that $s=e+\pi$ is algebraic of degree
    $r$, the ordinary norm descent proves for a primitive degree-$d$
    endpoint

    

$$
-\log|A(\pi)|
       \le(r^2d+r-1+o(1))\log H(A),
$$



    or relative threshold $r^2d+r$. Working over
    $\mathbb Q(s,i)/\mathbb Q(i)$ gives the same norm degree and cannot
    halve this cost.

    A rank-$t$ joint endpoint lattice supplies by exact Dirichlet
    pigeonholing only

    

$$
|A(\pi)|\ll H(A)^{1-t},\qquad
      |A(\pi)|/H(A)\ll H(A)^{-t}.
$$



    Since $t\le d+1$, full rank merely reaches relative exponent $d+1$.
    For $r=1$ this equals, but does not strictly beat, the algebraic
    threshold; for $r>1$ it is strictly too small. Thus parity mixing and
    joint rank alone cannot provide the strict approximation exponent needed
    for a contradiction.

    The 26-row exact replay finds full joint low-image rank on many small
    full-endpoint rows and candidates using every degree and both parities.
    These calculations confirm that mixing genuinely enlarges the finite
    image, but the rank patterns, bounded searches, and decimal values are
    diagnostics only. No all-parameter joint-rank, intrinsic-height, or
    corrected-content theorem follows.

The item-61 package is:

~~~
fbfb6fba663768b80364462608d0267d233d1828924b9d25f12dd9a7a1ea4b6d  sources/root_unity_gaussian_parity_mixing_barrier.md
a338633131005b021bd8acd0a1edf9ca69fa21fc2af2ae2f0ba517be1e843143  scripts/root_unity_gaussian_parity_mixing_certificate.py
70a4df592056f424a481ca6da7a8d6b6c803f43d8c59c8103a24b5f3a0317c02  results/root_unity_gaussian_parity_mixing_certificate.json
74c2d5fab03af9520d7f7cb480c6ce3fd490ce2b26a0769c337672605d4eb280  results/root_unity_gaussian_parity_mixing_hashes.sha256
~~~

The script verifies the frozen item-57 dependency hash before import. Its
final deterministic replay took 1.122126 seconds and reported 73,280 KiB
(71.5625 MiB) peak RSS, below the 2 GiB cap. Item 61 proves the phase/content
descent and the algebraic-measure/Dirichlet barrier; its ranks are finite
diagnostics. It does not classify $e+\pi$.

Items 58--61 therefore add one all-parameter square/product construction,
one exact $k=3$ endpoint/normalization audit, one exact global-image
saturation theorem, and one exact Gaussian-mixing barrier. None proves that
$e+\pi$ is rational, irrational, algebraic, or transcendental.

62. In the $m=2$ construction there is now an explicit all-parameter
    quadratic survivor in the intrinsically saturated global image. For every
    $n\ge5$, write the five lower-excess entries as

    

$$
A=H_{0,0},\quad B=H_{0,2},\quad C=H_{0,4},\qquad
      g_1=H_{1,1},\quad g_3=H_{1,3},
$$



    and put

    

$$
E_0=B-Az^2,\qquad E_1=C-Az^4,\qquad O=g_3z-g_1z^3.
$$



    These three endpoints lie in the exact lower-parameter excess kernel.
    The mixed-parity exterior combination

    

$$
P_n=(2Ag_1g_3-Bg_1^2)E_0^2
          -Ag_1^2E_0E_1+A^3O^2
$$



    cancels its coefficients in degrees $4,6,8$ identically and is exactly

    

$$
\boxed{P_n(z)=p_{0,n}+p_{2,n}z^2,\qquad
             p_{0,n}p_{2,n}>0.}
$$



    Its global image has frequencies $0,\ldots,4$, polynomial coefficient
    degree at most $2n-2$, and origin order at least $4n+4$. The uniform
    nonvanishing proof uses the probability measure proportional to
    $(t^2+1/4)^n\operatorname{sech}(\pi t)dt$. With

    

$$
x={1\over4}\operatorname{sech}^2(\pi t),\quad
      h=t\tanh(\pi t),\quad
      \alpha=\mathbb Ex,\quad\beta=\mathbb Ex^2,\quad
      \gamma={\mathbb E(hx)\over\mathbb Eh},
$$



    strict reversed covariance gives $\gamma<\alpha<1/8$, while monotonicity
    of $I_5(n)/I_3(n)$, anchored by an exact $n=5$ Fourier calculation,
    gives $\beta<\alpha/12$. These inequalities prove the two strict signs
    needed for $p_0p_2>0$.

    More importantly, this is the first fixed-output-degree survivor in the
    present branch with a proved uniform $O(n\log n)$ global vector. With

    

$$
D_n=2^{2n+3},\qquad q_n=2^{2n}(n-1)!,
$$



    the explicit vector $q_n^2D_n^5\mathscr F_n$ is integral and has

    

$$
\log H\le16n\log n+O(n).
$$



    If $g_n$ is the exact gcd of the two endpoint coefficients after the
    $D_n^5$ clearing and
    $\chi_n=\log g_n/(n\log n)$, the proved sharp ledger is

    

$$
\log H(P_n^{\rm prim})\le(10-\chi_n)n\log n+O(n),
      \qquad
      \log H_{\rm an}(\mathscr F_n)
        \le(14-\chi_n)n\log n+O(n).
$$



    The centered analytic gain has leading constant only $2$. In the easiest
    rational $e+\pi$ case, the present bounds could close only if

    

$$
2>34-3\chi_n,
$$



    whereas the endpoint formula gives merely $0\le\chi_n\le10+o(1)$.
    Even the formally maximal content therefore leaves a leading deficit of
    $2n\log n$. This is a barrier for the proved majorant, not a lower bound
    on the true saturated height.

The item-62 package is:

~~~
47045420f729a14eb7eaf655988add44332db26091b837a9d24dfaed7d39c868  sources/root_unity_m2_quadratic_saturated_survivor_theorem.md
1ec66622c212bb27d7729e1b9e2d7519d355bbe755f40b239343172926b8a7fe  scripts/root_unity_m2_quadratic_saturated_survivor_certificate.py
9a44bea7db63f8f994a01bcaf284a9319f05050bc28c84c7c71fb889ee483274  results/root_unity_m2_quadratic_saturated_survivor_certificate.json
d5faaf65094d19b9a20fd178ee35de76a0fb37b8aa6399c8ec76491c87967880  results/root_unity_m2_quadratic_saturated_survivor_hashes.sha256
~~~

The deterministic replay checks 16 exact rows, $5\le n\le20$, in about
9.15 seconds and peaked at 78,632 KiB RSS. The construction, nonvanishing,
integral clearing, and height ledger are all-parameter theorems; the finite
gcd and margin rows are diagnostics. Item 62 does not classify $e+\pi$.

63. Saturating the even and odd global-reflection blocks jointly over the
    Gaussian integers gives no additional phase-aligned lattice direction.
    If

    

$$
S_\pm=V_\pm\cap\mathbb Z^P,
      \qquad S_0=(V_+\oplus V_-)\cap\mathbb Z^P,
$$



    then the unphased quotient is genuinely $2$-primary:

    

$$
S_++S_-\subseteq S_0,\qquad2S_0\subseteq S_++S_-.
$$



    However, for the signed reflection $J$, the anti-linear involution
    $\sigma(w)=J\overline w$, and the intrinsic Gaussian saturation
    $S_{\mathbb G}$, the aligned fixed locus is exactly

    

$$
\boxed{S_{\mathbb G}^{\sigma=1}=S_+\oplus iS_-.}
$$



    It has saturation index one in the real-doubled lattice. The tempting
    $(1+i)$-cleared glue and the separately aligned doubled vector reduce to
    the same primitive analytic form after endpoint-content normalization.

    There is also an all-parameter coefficientwise no-gain theorem. For an
    aligned mix $w=u-iv$, every displayed centered circle majorant,
    including the exact supremum within each reflected pair, dominates the
    corresponding majorant of each nonzero component. Joint endpoint content
    is $\gcd(c_+,c_-)$; joint primitive height and degree cannot decrease.
    Hence, for

    

$$
\kappa_r(d)=r^2d+r-1,
$$



    the optimized measure margin satisfies

    

$$
\boxed{\sup_{u,v}\mathfrak M_r(u-iv)
      =\max\{\sup_u\mathfrak M_r(u),\sup_v\mathfrak M_r(-iv)\}.}
$$



    This theorem is deliberately limited to the rigorous absolute-coefficient
    circle bounds; whole-function interference and exceptionally short
    vectors inside one parity block remain open. On the exact 12-row grid the
    unphased glue indices are $2,4,8,16$, the aligned index is always one,
    and every bounded-search margin is negative. Those finite signs are not
    extrapolated.

The item-63 package is:

~~~
08c282e9ebd933b8b4def6806f9d6db1fb13e445c6b9ce1f6d57690c92162b9a  sources/root_unity_gaussian_global_saturation_no_gain.md
89004cd7c35e890803f486f3a69036d21980497c718b75ad78be4441335e4f5a  scripts/root_unity_gaussian_global_saturation_certificate.py
607cf35c54cf16f6da870b0b933c217388b8eb551132e07a8500ae95f0a78837  results/root_unity_gaussian_global_saturation_certificate.json
49d4d2e40a9cb421be3f409ca94129c487b5de3c685e8fe88fe6c39dd7fabbb7  results/root_unity_gaussian_global_saturation_hashes.sha256
~~~

The manifest also pins the item-60 saturation constructor. The final replay
took 60.242294 seconds and peaked at 999.941406 MiB RSS. Item 63 proves the
fixed-locus and coefficientwise no-gain identities, not an all-parameter
successive-minimum bound or a classification of $e+\pi$.

64. The coefficientwise circle majorant can be replaced, for any fixed
    centered exponential polynomial, by an exact Hardy--$H^2$ norm. For
    $f_{r,a}(z)=z^ae^{rz}$,

    

$$
\boxed{
      \langle f_{r,a},f_{s,b}\rangle_R
       =\sum_{\ell\ge\max(a,b)}
        {R^{2\ell}r^{\ell-a}s^{\ell-b}
         \over(\ell-a)!(\ell-b)!}.}
$$



    If $F=z^KH$ and $R>\pi$, Parseval and Cauchy--Schwarz give

    

$$
\boxed{|F(i\pi)|\le
      {\pi^K\|H\|_{2,R}\over\sqrt{1-\pi^2/R^2}}.}
$$



    For a finite endpoint fiber $B^tx=p$ with positive Gram matrix $A$,
    the exact real minimum is

    

$$
x_*=A^{-1}B(B^tA^{-1}B)^{-1}p,
      \qquad
      \min x^tAx=p^t(B^tA^{-1}B)^{-1}p.
$$



    If the fiber is rational, its rational points have the same infimum by
    density. That last statement gives no denominator bound for a rational
    near-minimizer and no integral shortest-vector certificate.

    For the saturated $m=2,d=2$ image at $n=5,8,10$, exact origin-jet
    cancellation followed by 180-digit evaluation shows improvements of
    $15.4798,30.1299,36.0468$ logarithmic units over the optimized
    coefficientwise bound for the same function. At $n=8$, the endpoint

    

$$
(p_0,p_2)=(27262976,2762317)
$$



    has direct log modulus $-3.89202658\ldots$ and Hardy upper log
    $-3.60197033\ldots$, but its relative exponent is only
    $1.21038\ldots<3$. The observed savings are consistent with $O(n)$,
    not a proved change to the $n\log n$ leading ledger. All decimal
    optimizations are stability diagnostics; the Gram, Hardy, and constrained
    minimum formulas are exact.

The item-64 package is:

~~~
24bc6c1e633118bec00659ed625d52266079555559c567e123d5d55943bc8a81  sources/root_unity_hardy_h2_saturated_circle_audit.md
8cd98734331b75ea26990759c5d13a8d022065340feb1ef5cea4871452912b6b  scripts/root_unity_hardy_h2_saturated_circle_certificate.py
a14b1af4b11b6760839b9237eaeb854156be6cc4588ffc83f656d9ed97347db2  results/root_unity_hardy_h2_saturated_circle_certificate.json
f5d80a9962ed914662be782301319b7d786aa6874510b876a5d24a54d9f3cbd4  results/root_unity_hardy_h2_saturated_circle_hashes.sha256
~~~

Two post-edit replays produced byte-identical JSON. The final run took 45.85
seconds and peaked at 1012.97 MiB RSS. Item 64 proves a substantially sharper
analytic tool but supplies neither rational-denominator control nor a
classification of $e+\pi$.

Items 62--64 therefore add a uniform fixed-degree $O(n\log n)$ survivor,
an exact Gaussian aligned-saturation no-gain theorem, and an exact
Hardy-space replacement for the coefficientwise circle bound. None proves
that $e+\pi$ is rational, irrational, algebraic, or transcendental.

65. The fixed-endpoint optimization inside the saturated $k=2$ global
    image is an exact rational weighted-$\ell^1$ quotient problem. If
    $E:V\to\mathbb Q^q$ is the retained endpoint map, $\Lambda$ is a
    rational right inverse, the rows of $K$ span $\ker E$, and
    $b=(p/H)\Lambda$, then

    

$$
\inf_{Ex=p/H}\sum_jw_j|x_j|
      =\inf_{t\in\mathbb R^s}\sum_jw_j|b_j+(tK)_j|.
$$



    Rational points have the same infimum by density, but this supplies no
    denominator bound. A rational feasible point proves only an upper bound;
    an optimum requires, for example, a matching exact dual certificate.

    At $(m,n,D,d,R)=(2,8,7,2,13)$, with endpoint

    

$$
p=(5441060864,0,551294727),
$$



    the exact saturated image has rank $11$, and its endpoint-zero kernel
    has rank $8$. The temporary purported optimum is rigorously
    nonoptimal: one exact kernel direction has one-sided derivative

    

$$
-{39710900240730900314101\over17036837675827200}<0,
$$



    and an explicit rational step strictly decreases the objective. The
    improved feasible point has

    

$$
\log B_{\rm imp}=15.8874542397205888\ldots,
      \qquad -\log B_{\rm imp}-2\log H(p)
      =-60.72193402085388\ldots,
$$



    far below the degree-two measure threshold. Clearing the two rational
    global representatives multiplies their primitive endpoints by

    

$$
6518378303365776642144000
      \quad\hbox{and}\quad
      645319452033211887572256000,
$$



    respectively; both cleared global vectors have content one. This is a
    rigorous finite integral-lattice clearing phenomenon, not an asymptotic
    lower bound. Item 69 below proves that it is **not** an obstruction to
    endpoint-only Hardy or weighted-$\ell^1$ Schwarz quotient bounds; it
    matters only to a separate method that requires global integrality. No
    floating linear-program output enters the certificate.

The item-65 package is:

~~~
070aa86143f9970c7925a07377fe1ff8f795992c8057e98505c6fc137f83f5e9  sources/root_unity_k2_exact_quotient_lp_audit.md
1f9ef63de854211c31bde2575cdc20d2271aae33e59f45d8810099c94af84a6c  scripts/root_unity_k2_exact_quotient_lp_certificate.py
a0e2a8d3d3c5db6904c713913ab5a441d72785931cb4e62c77fe7bfdae9fac1a  results/root_unity_k2_exact_quotient_lp_certificate.json
cebc31286ee464728467d9584ef729c667111cb2b69e1f6f9bb10ed5488065a4  results/root_unity_k2_exact_quotient_lp_hashes.sha256
~~~

The manifest, all payload hashes, and the absence of CR or other unexpected
control bytes were independently reverified after repair. The final replay
took 27.12 seconds and peaked at 1081.72 MiB RSS. Item 65 converts the
continuous quotient idea into an exact theorem and computes its integer
clearing cost. Its earlier interpretation as an endpoint-analytic
obstruction is superseded by item 69. It does not classify $e+\pi$.

66. At $\zeta=i\pi/2$, the centered-cosh lower lift
    $P_n[C]=-T_n(C/(2\cosh z))$,
    $R_n[C]=C+2\cosh zP_n[C]$, has exact rank-one displacement

    

$$
P_n[zC]-zP_n[C]=[z^n](C/(2\cosh z))z^{n+1}.
$$



    On the kernel of this coefficient functional,
    $R_n[zC]=zR_n[C]$, so
    $W(R_n[C],R_n[zC])=R_n[C]^2$; polarization realizes symmetric
    products as rational exterior sums. Killing $t+1$ consecutive tail
    jets unconditionally gives a nonzero product endpoint of degree at most
    $2t+2$. The stronger quadratic pattern
    $t=\lfloor(n-1)/3\rfloor$ is exactly certified only for
    $5\le n\le20$. Even granting that pattern and an optimistic
    survivor-preserving Siegel bound, its scaling has height constant $5/3$,
    centered gain $2/3$, and needs endpoint-content constant
    $\chi>13/9$. The missing step is a structured quotient/Smith height
    theorem that guarantees a nonzero low endpoint.

The item-66 package is:

~~~
8794eaeb7a8cf5f0c7e749c85afc67b2403b3dc6e3e752353bbf0ab020059581  sources/centered_cosh_lower_lift_product_audit.md
da827921d2621821553ed8bee069428638539fa5bb6b952c4636782d2b5aef71  scripts/centered_cosh_lower_lift_product_certificate.py
f3425385637efaa329f67a133c89844ac8a2a3a92603838ffe0e92c8ca1844bf  results/centered_cosh_lower_lift_product_certificate.json
51e0523cf8ce702885deb20d703ddd615cc15e645fe96fba2c35ce0c2ec54a92  results/centered_cosh_lower_lift_product_hashes.sha256
~~~

The independently replayed certificate took 7.22 seconds and about 91,680
KiB RSS. Item 66 proves the lift/product mechanism and a growing-degree
survivor, not an all-$n$ quadratic survivor or a classification.

67. For reflection-even $F_+$, reflection-odd $F_-$, and
    $F=F_+-iF_-$, divide by any common $z^K$ and put
    $U=F_+/z^K$, $V=F_-/z^K$, $W=U-iV$. The quotients retain
    opposite parity and satisfy

    

$$
\boxed{|W(z)|^2+|W(-z)|^2
       =2\bigl(|U(z)|^2+|V(z)|^2\bigr).}
$$



    Hence
    $\|W\|_{\infty,R}\ge\max(\|U\|_{\infty,R},\|V\|_{\infty,R})$
    and $\|W\|_{2,R}^2=\|U\|_{2,R}^2+\|V\|_{2,R}^2$. Unequal actual
    origin orders add factors $(R/\pi)^\delta\ge1$, strengthening the
    comparison. With joint-content gcd and height/degree domination, neither
    the exact whole-circle supremum margin nor the Hardy margin of a genuine
    Gaussian mix can exceed either component's margin. This closes item 63's
    whole-circle cross-parity interference caveat; single-parity minima remain
    open.

The item-67 package is:

~~~
6e979114a2d4a043e41fe6dcf6031d3c98eb86c434b3c8825c3b8aa1589ba412  sources/root_unity_gaussian_antipodal_no_gain_theorem.md
880e284b923fbeb911509bc2970d79b37434781d7eb002454408294661d81d79  scripts/root_unity_gaussian_antipodal_no_gain_certificate.py
1fa52598c244019d9892255d54deccbeb56ef0ed86b9d7c6496c2647049ebe8f  results/root_unity_gaussian_antipodal_no_gain_certificate.json
e6df57e7016a60e0154fba90a849ec34d707d691135d8bc04142c06a2abca15c  results/root_unity_gaussian_antipodal_no_gain_hashes.sha256
~~~

The manifest, compilation, JSON, and strict control-byte audits pass; an
independent replay took 1.16 seconds and about 71.5 MiB process RSS. Items 66
and 67 narrow the surviving arithmetic problem but do not classify
$e+\pi$.

68. The closer-root centered family

    

$$
R=C+2\cosh z\,P,qquad \operatorname{ord}_0R\ge n+D+1,
      \qquad R(i\pi/2)=C(i\pi/2)
$$



    is normal for every $n,D$. If
    $N=\lfloor n/2\rfloor$, $K=\lfloor D/2\rfloor$, and
    $\epsilon=1$ exactly when $n,D$ are both odd, then

    

$$
C(z)=z^\epsilon Q_{N,K}(z^2),
$$



    where $-U/Q_{N,K}$ is the $[N/K]$ Padé approximant to
    $1/(2\cosh\sqrt x)$. Positive rectangular Schur minors prove the
    parity, exact degree, normality, and first nonzero remainder coefficient
    without a finite extrapolation.

    For every fixed $K\ge1$, the primitive endpoint satisfies

    

$$
{ |Q_{N,K}(-\pi^2/4)|\over H(Q_{N,K}) }
      =c_K(2K+1)^{-2N}\{1+O_K(\rho_K^N)\},
      \qquad
      \rho_K=\left({2K+1\over2K+3}\right)^2,
$$



    with an explicit positive rational $c_K$. For $D=2$, mandatory
    clearing gives the exact Euler-number/gcd family and the relative value

    

$$
{\beta(2N+3)\over\beta(2N+1)}-1
      \sim {8\over3^{2N+3}}.
$$



    On the diagonal $K=N$, Dzyadyk's theorem yields relative gain
    $4N\log N+O(N)$. A new Catalan-Hankel local argument proves that the
    mandatory $2^{2N}$ endpoint clearing is primitive and has height at
    least $16^N$; the resulting relative exponent is only $O(\log N)$,
    while the degree in $e$ is $2N+O(1)$. Pure integer-frequency
    dilation is exactly primitive-equivalent after clearing. The centered
    construction is genuinely different, but belongs to a half-integer
    frequency class; scalar symmetric bands retain the same cosh zero
    lattice.

The item-68 package is:

~~~
f837e5be64de4985e721f9e5d3731e6d13e01c41fa973a937c4bc1dce0977ecf  sources/root_unity_closer_root_sech_pade_audit.md
8a97f86cc74314ead643e34a8ccc7d1d7bd0c2502122c3da1143862d686c64b6  scripts/root_unity_closer_root_sech_pade_certificate.py
f16f21e3ebf0a52b66a201f29ebe6875e0b094c65077b0e800ce14278d7bba5e  results/root_unity_closer_root_sech_pade_certificate.json
53d611d1478c66290b05a683d9eb7ff3936f88228cc45bac36628b3019f7d117  results/root_unity_closer_root_sech_pade_hashes.sha256
~~~

An independent replay took 4.30 seconds and 73,560 KiB RSS; the manifest,
syntax, JSON, and strict control-byte checks all pass. Item 68 proves the
closer-root construction and its current arithmetic barrier, not a
classification of $e+\pi$.

69. Global denominators do not enter endpoint-only Hardy or coefficientwise
    Schwarz quotient arguments. If the rational endpoint map has rank two
    and $E(F)=(p_0,p_2)$ implies
    $F(i\pi)=p_0-p_2\pi^2$, then every primitive integer endpoint has a
    rational representative. The common origin zero and endpoint identity
    extend complex-linearly. The real Hilbert-space minimizer is a legitimate
    auxiliary function, and rational points in its exact endpoint fiber
    approach the same minimum. The conditional $e$-measure sees only the
    primitive endpoint polynomial $p_0-p_2X^2$, not denominators of the
    global representative. The same homogeneity argument applies to the
    rational weighted-$\ell^1$ quotient. This corrects the interpretation,
    not the finite clearing data, of item 65.

    If $Q_R(p)=p^tC_Rp$ is the squared binary Hardy quotient and
    $u=p_0-\pi^2p_2$, $v=p_2$, then exactly

    

$$
{Q_R(p)\over a}=(u+\eta v)^2+\tau v^2,
      \qquad a>0,\quad\tau>0.
$$



    With $\varepsilon=\sqrt{\eta^2+\tau}$,

    

$$
\boxed{
      \left|{\sqrt{Q_R(p)}\over\sqrt a\,|p_2|}
      -\left|\pi^2-{p_0\over p_2}\right|\right|
      \le\varepsilon.}
$$



    Projective collapse therefore reduces primitive endpoint optimization,
    up to $\varepsilon$, to rational approximation of $\pi^2$. Ordinary
    continued-fraction balance gives approximation exponent two, whereas
    excluding rational $s=e+\pi$ by the degree-two $e$-measure requires
    $|\pi^2-p_0/p_2|<|p_2|^{-3-\epsilon}$. Collapse and positive
    definiteness alone do not supply that exceptional exponent.

    Finite rows $n=5,8,10,12$ have $\varepsilon^2$ approximately
    $1.23\,10^{-13},3.86\,10^{-28},7.10\,10^{-32},5.18\,10^{-44}$,
    but no asymptotic rate is inferred. A separate $n=14,D=7$ even-block
    row has endpoint $(121551268148674560,12315718362050897)$, Hardy log
    bound $-10.98977\ldots$, and relative exponent
    $1.27936\ldots<3$; it is likewise finite evidence.

The item-69 package and supplemental diagnostic are:

~~~
5bd489df02183a374145d889ca96a6d2f3940ba141af0592962920021fc3a901  sources/root_unity_hardy_endpoint_quotient_geometry_correction.md
1b99140f9a2d36731364847254e578526cbfafeca12c19aed992704c8231cac9  scripts/root_unity_hardy_endpoint_quotient_geometry_certificate.py
14019a29cd3af0e41130ddfc71f927ab9969be394e98ca7903571118d97cdcec  results/root_unity_hardy_endpoint_quotient_geometry_certificate.json
88b5cef191c3231286d4a9160986e797000869d7ee0e897d6ff252e053562469  results/root_unity_hardy_endpoint_quotient_geometry_hashes.sha256
fe388e4445efd3e1ee961707c0c230768d6e2d3745da3b44831ca53e22294fc5  scripts/root_unity_hardy_h2_even_n14_diagnostic.py
3472669cf21abc9cc0edcc41a1bb18c061b58b6fc62f490bddd3c739b7128a3c  results/root_unity_hardy_h2_even_n14_diagnostic.json
36c2727e4f971663811439f5920381483d30d5ec154e3946c9c45b8226d785b2  results/root_unity_hardy_h2_even_n14_diagnostic_hashes.sha256
~~~

The main certificate replayed twice byte-identically in 118.36 and 118.62
seconds, with about 461 MiB maximum observed RSS. All manifest, dependency,
syntax, JSON, and control-byte checks pass. The $n=14$ run used about 1 GiB
at peak in live polling; system memory remained above roughly 47 GiB
available. Item 69 removes a false denominator barrier but exposes the
endpoint-approximation boundary. It does not classify $e+\pi$.

70. Put

    

$$
F(x)={1\over2\cosh\sqrt x},
$$



    and let $Q_q$ be its diagonal $[q/q]$ Pade denominator. For the
    balanced centered-cosh endpoint-product spaces of item 66, with
    $n=3q+r$, $D=n-1$, and $r\in\{1,2\}$, there are exact
    all-parameter ideal inclusions

    

$$
\boxed{Q_q\mathbb Q[x]_{\le2q}\subseteq {\cal E}_{q,1}\quad(q\ge2),
      \qquad xQ_q\mathbb Q[x]_{\le2q}\subseteq {\cal E}_{q,2}\quad(q\ge1).}
$$



    Thus every coefficient functional annihilating the corresponding
    product image obeys the finite recurrence with characteristic
    polynomial $Q_q$ (shifted once in the $r=2$ case). This is not a
    finite-grid inference. Polynomial division gives
    $V=Q_q\mathbb Q[x]_{\le m}\oplus W$; in
    $\mathbb Q[x]/(Q_q)$, the required controllability follows from an
    explicitly selected positive rectangular Jacobi--Trudi/Schur minor for
    the coefficients of $F$. The edge $(q,r)=(1,1)$ is genuinely
    exceptional:
    ${\cal E}_{1,1}=Q_1^2\mathbb Q[x]_{\le1}$, and the proposed
    $Q_1\mathbb Q[x]_{\le2}$ inclusion fails.

    This replaces a generic ambient cofactor description by a degree-$q$
    Pade recurrence with a standard clearing bound
    $O(q^2\log q)$. It does **not** prove that the residual quotient is
    one-dimensional, saturated, or has a small primitive survivor. Those
    quotient/Smith assertions remain the arithmetic bottleneck, so the
    smaller recurrence height cannot yet be entered as a proved survivor
    height in the transcendence ledger.

The item-70 package is:

~~~
a4e1fa3f9562f876bc5dafec817373238298d6565ad34c291f0a3a70513cad84  sources/centered_cosh_pade_ideal_recurrence_theorem.md
f20223fb9bb9f524db7532c1fe1f8aad22b6e01245564d4b55b3ddf6795e1a20  scripts/centered_cosh_pade_ideal_recurrence_certificate.py
a6a99505f1cef3c1499be9a331cf452c76c1fc7f7d9f0b66b1e6baf56efaa48d  results/centered_cosh_pade_ideal_recurrence_certificate.json
ef1345491b9747c118e1e8a9c1a5c34160923bfe6fdea8a2aed9e4b5dd0a7c1c  results/centered_cosh_pade_ideal_recurrence_hashes.sha256
~~~

The manifest and payload hashes were independently verified. A fresh exact
replay reproduced the certificate and took 0.99 seconds with about 68,616 KiB
peak process RSS. Item 70 proves the ideal/recurrence layer, not the missing
quotient arithmetic and not a classification of $e+\pi$.

71. For the quadratic closer-root content, put

    

$$
A_N=(2N+2)(2N+1),\quad
      H_N=\gcd(|E_{2N}|,|E_{2N+2}|),\quad
      G_N=\gcd(A_N|E_{2N}|,|E_{2N+2}|).
$$



    There is the exact elementary separation

    

$$
G_N=H_N\gcd\left(A_N,{|E_{2N+2}|\over H_N}\right),
      \qquad H_N\mid G_N\mid A_NH_N.
$$



    Thus the index factor $A_N$ changes $\log G_N$ by only
    $O(\log N)$. For each odd prime define
    $a_p(N)=\max\{a:\varphi(p^a)\le2N+2\}$, with value zero when
    the set is empty, and split

    

$$
S_N=\prod_{p\ {\mathrm{odd}}}p^{\min(v_p(H_N),a_p(N))},
      \qquad J_N=H_N/S_N.
$$



    The prime-power Euler--Kummer congruence has a unit multiplier, so
    divisibility of positive even Euler indices is exactly periodic modulo
    $\varphi(p^a)$. It follows unconditionally that

    

$$
S_N\mid\operatorname {lcm}(1,\ldots,3N+3),\qquad
      \boxed{\log G_N=\log J_N+O(N)}.
$$



    Every valuation layer in $J_N$ is precisely a simultaneous adjacent
    pair

    

$$
p^a\mid E_{2N},E_{2N+2},\qquad \varphi(p^a)>2N+2,
$$



    lying before its first $p^a$-Kummer period. Conversely every such
    excess layer enters $J_N$. Hence

    

$$
\log G_N=o(N\log N)\quad\Longleftrightarrow\quad
      \log J_N=o(N\log N).
$$



    The recurring endpoint factors $149$ and $241$ lie in the harmless
    periodic factor $S_N$; their recurrence is not evidence of
    factorial-scale cancellation. The primitive quadratic height is now
    exactly localized as

    

$$
\log H(\mathscr C_N)=2N\log N-\log J_N+O(N).
$$



    A direct reduced Euler-polynomial resultant supplies at best
    $O(N^2\log N)$, which is too large. The remaining input is an
    unconditional quantitative bound for adjacent first-period,
    higher-order Euler-irregular layers.

The item-71 package is:

~~~
a720ef166a3b772d85c32934782fcfa4d41797b274ea964259973a216bb369ca  sources/root_unity_quadratic_euler_gcd_kummer_obstruction.md
5685471a82b294cd77b60d3079067274f23e14f30e3317f2373c87ffcb2770d4  scripts/root_unity_quadratic_euler_gcd_kummer_certificate.py
89521c6ec34e3ff7c75d7845ab22de10562814a3cbe8d256bbd7769a9e2cb53d  results/root_unity_quadratic_euler_gcd_kummer_certificate.json
74b79cee3b86e5fe37700e1db68ed91976a56c01a783c1e10d5e13651d82ba49  results/root_unity_quadratic_euler_gcd_kummer_hashes.sha256
~~~

The primary congruence was independently checked in the cited paper; the
manifest, strict byte audit, syntax check, and deterministic JSON replay all
pass. A fresh replay took 5.88 seconds and 76,880 KiB peak RSS. Item 71
isolates the exact unresolved local factor but does not bound it and does not
classify $e+\pi$.

72. The endpoint-collapse geometry of item 69 extends exactly to every fixed
    degree. For

    

$$
A_p(X)=\sum_{j=0}^dp_jX^j,\qquad
      Q_n(p)=p^tC_np,qquad C_n\succ0,
$$



    use $u=A_p(\pi)$ and $v=(p_1,\ldots,p_d)$. There are exact
    $a_n>0$, $\eta_n$, and ${\cal T}_n\succ0$ such that

    

$$
{Q_n(p)\over a_n}=(u+\eta_n^tv)^2+v^t{\cal T}_nv.
$$



    If

    

$$
\varepsilon_n=max_{\|x\|_\infty\le1}
       \sqrt{x^t(\eta_n\eta_n^t+{\cal T}_n)x},
$$



    then the exact reverse-triangle comparison is

    

$$
\boxed{\left|\sqrt{Q_n(p)/a_n}-|A_p(\pi)|\right|
        \le\varepsilon_n\|(p_1,\ldots,p_d)\|_\infty.}
$$



    Hence the primitive quotient minimum through nonconstant height $H$
    differs from the primitive polynomial-approximation minimum by at most
    $\varepsilon_nH$. To transfer an absolute approximation exponent
    $\mu$ along heights $H_n$, one needs the quantitative rate

    

$$
\varepsilon_nH_n=o(H_n^{-\mu});
$$



    merely proving $\varepsilon_n\to0$ is insufficient.

    With $d+1$ phase-aligned integer coordinates, the dimension-only
    Dirichlet absolute exponent is exactly $d$. It is sharp in this level
    of generality by the algebraic-norm example
    $2^{1/(d+1)}$. Under hypothetical algebraicity of
    $s=e+\pi$ of degree $r$, the conditional $e$-measure threshold is

    

$$
\kappa_r(d)=r^2d+r-1.
$$



    For $r=1$, Dirichlet only meets this boundary, while a contradiction
    requires a strict improvement; for $r>1$, it falls strictly short.
    Gaussian phase alignment $C_p(z)=A_p(-iz)$ preserves height, content,
    and degree and realizes $C_p(i\pi)=A_p(\pi)$. Without it, the even and
    odd real-coefficient blocks are orthogonal and the best dimension-only
    exponent is only $\lfloor d/2\rfloor$. Their actual degree after
    $\pi=s-e$ is not halved, so parity gives no measure-cost compensation.

The item-72 package is:

~~~
6201f479c27e16afe4fdf515e24d860c0c360ea0be29c31d12feb97da0831687  sources/root_unity_hardy_all_degree_endpoint_collapse_theorem.md
e29f72af7515d0cf65bab00f65019de6d0ac366e96290c84a26f300bc070eeca  scripts/root_unity_hardy_all_degree_endpoint_collapse_certificate.py
09ab52efda354fc909d0dc7f8de063fde054a9b9fc0c8bc272dad21c7d236a6d  results/root_unity_hardy_all_degree_endpoint_collapse_certificate.json
cbfd5640107565c87c1bc4a7657f064a6842685ccdb0fb711d6c1a9bccad118c  results/root_unity_hardy_all_degree_endpoint_collapse_hashes.sha256
~~~

The manifest also pins and verifies the item-69 and conditional-measure source
dependencies. Two fresh replays preserved the deterministic JSON hash; syntax,
control-byte, parity, block-Schur, and threshold audits pass, with an internal
RSS guard below 1 GiB. Item 72 identifies the exact exceptional-approximation
and collapse-rate requirements but supplies neither one and does not classify
$e+\pi$.

73. The first genuinely interior adjacent Euler-irregular seed occurs on the
    exact scan at

    

$$
N=1643,\qquad p=151483.
$$



    The prime $p$ satisfies

    

$$
\boxed{\gcd(E_{3286},E_{3288})=151483},
      \qquad
      v_p(E_{3286})=v_p(E_{3288})=1.
$$



    A complete reciprocal-cosh computation in
    $\mathbb F_p[X]/(X^{p-1})$, rather than a partial factor-table
    lookup, proves that

    

$$
\{r:2\le r\le p-3,\ r\ {\rm even},\ p\mid E_r\}
      =\{3286,3288\}.
$$



    Thus the total $E$-irregularity index is exactly two. Since
    $p-1=151482>3288$, this factor lies strictly before its first Kummer
    period. In the item-71 decomposition one has exactly

    

$$
H_{1643}=J_{1643}=G_{1643}=151483,\qquad S_{1643}=1.
$$



    The exact scan through $N=1643$ has no earlier row with $J_N>1$.
    This is finite information only. It proves that $J_N$ is not
    identically one, refutes universal adjacent-branch incompatibility, and
    refutes any claim that an adjacent pair must force a large total
    irregularity index. It supplies no asymptotic bound for $J_N$.

The item-73 package is:

~~~
c9ed43839126af9542ec0c0891cb5a48023a7cb17ba21dca34cb83bc629b6078  sources/root_unity_adjacent_euler_irregular_seed_counterexample.md
a92019c257e7c985fdec00d5bb88b70154a67c8c8e0e9b2184dd0bb7f2c88542  scripts/root_unity_adjacent_euler_irregular_seed_certificate.py
4468c09210ac6a72303980f4cf27070c914a717bab474a8e7f86d4bd4fab3aaf  results/root_unity_adjacent_euler_irregular_seed_certificate.json
c4e0b694a4f57130370e1f66869f5d862536e21708a78a0fa1c8655463525f0f  results/root_unity_adjacent_euler_irregular_seed_hashes.sha256
~~~

The source wording, manifest, payload hashes, Python syntax, and strict byte
audit pass. An independent exact replay reproduced the JSON in 6.33 seconds
with 86,904 KiB peak RSS while 48 GiB of system RAM remained available.
Item 73 is a rigorous counterexample to two proposed local shortcuts, not a
classification of $e+\pi$.

74. Several independent Hardy-short endpoints do not amortize the
    one-polynomial approximation cost. Put $N=d+1$, use coordinates
    $u=A_p(\pi)$, $v=(p_1,\ldots,p_d)$, and let
    $K(H,E)=[-E,E]\times[-H,H]^d$. The endpoint lattice has covolume one,
    so Minkowski's second theorem gives the exact window

    

$$
{1\over N!EH^d}\le\prod_{j=1}^N\lambda_j(H,E)
      \le {1\over EH^d}.
$$



    If $N$ independent integer endpoints have transverse height at most
    $H$ and evaluation at most $E$, their transformed determinant
    satisfies

    

$$
1\le|\det P|\le N!EH^d.
$$



    More generally, for $k\le d$, let $g$ be the content of the
    $k$-row Pluecker vector and $W$ its primitive height. Contracting
    with the evaluation covector gives explicit nonzero integer polynomials
    $R_J$ with

    

$$
\max_J H(R_J)=W,\qquad
      |R_J(\pi)|\le {k!EH^{k-1}\over g}.
$$



    Under hypothetical algebraicity of $s=e+\pi$, put
    $\kappa=r^2d+r-1$. At the Dirichlet scale
    $E=H^{-d+o(1)}$, the conditional $e$-measure forces

    

$$
\limsup{\log g\over\log H}
      \le k-{d+1\over\kappa+1}.
$$



    Under the standard noncollapse parametrization, beating that measure
    requires the strict reverse inequality. For $r=1$, the two boundaries
    are exactly $g=H^{k-1+o(1)}$ versus a required exponent strictly
    greater than $k-1$. Thus any successful exterior-content or
    exterior-height gain is already an exceptional ordinary polynomial
    approximation $R_J(\pi)$; it is not a free determinant gain.

    The all-$k$ Hardy rank thresholds differ from the evaluation
    thresholds by at most $\varepsilon_nH$. Products add degree and
    height, while a translated pairwise Sylvester resultant lies in the
    ideal of its two constant terms and receives only one small factor.
    Phase alignment preserves the theorem; unaligned parity supplies at
    most one evaluation column per block.

The item-74 package is:

~~~
84ed2c28661846171d414529b6ed764646f47df1028b5c54590af5b15a65b9fe  sources/root_unity_hardy_successive_minima_exterior_no_go.md
b1a553637874fa957f781b8be2044377d8d2e80195a07fe7a99a1d7257f5f134  scripts/root_unity_hardy_successive_minima_exterior_certificate.py
7bc241179c63ac9fc0b6124c9279944c710243e06954a8c9508adf17fc11ea08  results/root_unity_hardy_successive_minima_exterior_certificate.json
2f13c98db67eb4dff21f6a442a1285207157ee08db712e410d53ddf213425e3b  results/root_unity_hardy_successive_minima_exterior_hashes.sha256
~~~

All six manifest entries, Python syntax, UTF-8/control-byte checks, TeX
delimiter counts, and two deterministic replays pass. The independent replay
took 4.29 seconds; total live system use stayed below 2.4 GiB with about
48 GiB available. Item 74 closes a canonical multi-vector loophole but
produces no exceptional approximation and no classification of $e+\pi$.

75. The balanced centered-cosh Padé product image now has a complete
    all-parameter rational quotient description. Let $Q,P$ be the
    denominator and numerator of the diagonal $[q/q]$ approximant to

    

$$
F(x)={1\over2\cosh\sqrt x},
$$



    and let $G,R$ be those of the adjacent $[q+1/q-1]$ entry. Padé
    normality follows from strictly positive Schur specializations, and the
    two entries satisfy

    

$$
RQ-PG=\kappa x^{2q+1},\qquad \gcd(Q,G)=1.
$$



    If $\rho_Q$ denotes reduction in $\mathbb Q[x]/(Q)$, the exact
    residual images are

    

$$
\boxed{\rho_Q({\cal E}_{q,1})
             =G^2\mathbb Q[x]_{\le q-2}}\qquad(q\ge2)
$$



    and, for

    

$$
\Phi(T)=\left(T(0),\rho_Q\left({T-T(0)\over x}\right)\right),
$$



    

$$
\boxed{\Phi({\cal E}_{q,2})
       =\mathbb Q\Phi(E^2)\oplus
        \bigl(\{0\}\oplus G^2\mathbb Q[x]_{\le q-2}\bigr)}
        \qquad(q\ge1),
$$



    where $E$ is the specified minimal even Padé factor. Consequently the
    two images have codimension exactly one in their ambient polynomial
    spaces:

    

$$
\dim{\cal E}_{q,1}=3q\quad(q\ge2),\qquad
      \dim{\cal E}_{q,2}=3q+1\quad(q\ge1).
$$



    The edge $(q,r)=(1,1)$ has codimension two. The quotient proof uses an
    exact $G$-Krylov description of every constrained Padé remainder and,
    in the second family, the Cramer syzygy $E=GH+QK$. The unique first
    annihilator is

    

$$
\lambda([T])=[x^{q-1}]\rho_Q(G^{-2}T),
$$



    so its moments obey the order-$q$ recurrence with characteristic
    polynomial $Q$. There is also the exact arithmetic identity

    

$$
\operatorname {Res}(Q,P)\operatorname {Res}(Q,G)
       ={\kappa^qQ(0)^{2q+1}\over\operatorname {lc}(Q)^2}.
$$



    These are rational vector-space theorems. They do not determine the
    local Smith factors, integral saturation, or the primitive height of the
    surviving codimension-one functional; generic minor clearing can still
    cost $O(q^3\log q)$.

The item-75 package is:

~~~
1173dfd585050ef192cf0c71be8c6e14f6357a14e56e81d7f2afadf35d3f0afd  sources/centered_cosh_pade_residual_quotient_theorem.md
867b154754477d7e9e196f939dc5b5bf9e584d15d28fe3baa255505882dfd76e  scripts/centered_cosh_pade_residual_quotient_certificate.py
be9ed129087a44bb2d1d315efa8e19e3069682475a76b52a2c0410a5ec40d026  results/centered_cosh_pade_residual_quotient_certificate.json
eb10284c8cda928182de8b5f86f230a1bc708e8c3617391265c4f55849b77b13  results/centered_cosh_pade_residual_quotient_hashes.sha256
~~~

The manifest, Python syntax, JSON, TeX delimiters, and strict control-byte
audits pass. An independent exact replay preserved the JSON hash in 9.93
seconds at 87,048 KiB peak RSS. Item 75 proves the finite-grid codimension
pattern for every parameter, but not the integral height estimate needed to
classify $e+\pi$.

76. The reduced quadratic Euler ratios have both individual and adjacent
    exponential denominator floors. Define

    

$$
A_N=(2N+2)(2N+1),\quad
      P_N={|E_{2N+2}|\over G_N},\quad
      Q_N={A_N|E_{2N}|\over G_N},
$$



    where $G_N=\gcd(A_N|E_{2N}|,|E_{2N+2}|)$. The exact beta identity is

    

$$
{P_N\over Q_N}
       ={4\over\pi^2}{\beta(2N+3)\over\beta(2N+1)}
       ={4\over\pi^2}
        +{32\over\pi^2\,3^{2N+3}}
          \left(1+O\left((3/5)^{2N+1}\right)\right).
$$



    Explicit alternating-tail intervals at consecutive indices are
    disjoint, so these reduced ratios strictly decrease. Their adjacent
    integral determinant satisfies the stronger exact assertion

    

$$
D_N=P_NQ_{N+1}-P_{N+1}Q_N>0,\qquad v_2(D_N)=1.
$$



    Indeed, every secant Euler number is odd,
    $v_2(Q_N)=1+v_2(N+1)$, and the adjacent denominator valuations are one
    and at least two. Thus $D_N\ge2$, and the explicit upper error bound
    gives

    

$$
\boxed{Q_NQ_{N+1}>
       {13\pi^2\over216}\,3^{2N+3}}.
$$



    Hence

    

$$
\liminf_{N\to\infty}
       {\log Q_N+\log Q_{N+1}\over N}\ge2\log3,\qquad
      \limsup_{N\to\infty}{\log Q_N\over N}\ge\log3.
$$



    Separately, Zudilin's proved
    $\mu(\pi^2)\le5.09541178\ldots$, used with the safe upper decimal
    $5.095412$, transfers through $4/\pi^2$ to

    

$$
\liminf_{N\to\infty}{\log Q_N\over N}
       \ge {2\log3\over5.095412}
       =0.4312162740\ldots.
$$



    Both conclusions improve $\log G_N$ by only $O(N)$, whereas the
    unreduced Euler scale is $2N\log N+O(N)$. They do not prove
    $\log G_N=o(N\log N)$ and do not control the item-71 factor $J_N$
    at leading scale.

The item-76 package is:

~~~
8b22a86eea520400245e5529809da2dcce56cbfb26c9836677e23ccd0a197a0a  sources/root_unity_quadratic_euler_beta_denominator_floor.md
c9fd42d69521b2faaba8166c5495d25e75318a13a31327c9eaf41ea40ca18d1e  scripts/root_unity_quadratic_euler_beta_denominator_certificate.py
c36e90fdcd023c940ea525b98b5c4786e610061435d2aa8b913fb0200f4cfe97  results/root_unity_quadratic_euler_beta_denominator_certificate.json
22fba2af00e25aa5a956b923e490d2a853dd170ab2292178190bb5a1507d6f1d  results/root_unity_quadratic_euler_beta_denominator_hashes.sha256
~~~

The manifest pins items 71 and 73. Independent hashing, syntax, strict-byte,
and deterministic replay checks pass; the replay used about 37 MiB RSS while
48 GiB remained available. Item 76 gives new quantitative arithmetic
information but no classification of $e+\pi$.

77. The canonical “large $G_N$ or small $G_N$” quadratic dichotomy does
    not close. For

    

$$
C_N(T)=4Q_N-P_NT^2,\qquad
      {P_N\over Q_N}={4\over\pi^2}(1+\delta_{2N+1}),
$$



    one has $H(C_N)=4Q_N$ and
    $|C_N(\pi)|/H(C_N)=\delta_{2N+1}\asymp3^{-2N}$.
    If $e+\pi$ were algebraic of degree $r$, this first branch would
    require

    

$$
\limsup{\log Q_N\over N}
       <c_{3,r}:={2\log3\over2r^2+r}
$$



    with a strict linear margin. Thus $G_N$ would have to remove almost
    the entire factorial Euler height, not merely be exponential.

    Direct translation to a polynomial in $e$ cannot hide a large
    $Q_N$ in coefficient content. Over the fixed field
    $K=\mathbb Q(e+\pi)$, after a fixed integral clearing $m$, every
    common prime-ideal coefficient valuation of

    

$$
m^2\{4Q-P(e+\pi-X)^2\}
$$



    is bounded by $v_{\mathfrak p}(4m^4)$. Its absolute projective
    coefficient height is therefore $\asymp_K Q$.

    Adjacent determinant and Bezout eliminations primitive-normalize to
    $T^2$ or $1$, and the adjacent product has relative exponent at
    most two, below every degree-four conditional threshold. Among all
    fixed affine combinations of two adjacent rows, the unique
    nearest-pole cancellation has weights $(-1,9)$:

    

$$
{9P_{N+1}/Q_{N+1}-P_N/Q_N\over8}.
$$



    Its relative error is

    

$$
{48\over5^{2N+5}}\{1+O((5/7)^{2N+1})\},
$$



    but its reduced denominator creates a new obstruction. Put

    

$$
h_N=\gcd(Q_N,Q_{N+1}),\quad
      K_N=\gcd(9P_{N+1}Q_N-P_NQ_{N+1},8Q_NQ_{N+1}).
$$



    Then $K_N=h_NL_N$, $L_N\mid9h_N/2$, and

    

$$
{16Q_NQ_{N+1}\over9h_N^2}
       \le\widehat Q_N
       \le{8Q_NQ_{N+1}\over h_N}.
$$



    Consequently the improved branch needs

    

$$
\log h_N\ge
      \left(\log3-{\log5\over2r^2+r}\right)N+o(N).
$$



    At $r=1$ the coefficient is
    $0.5621329845\ldots$. A primewise identity shows that small $G_N$
    controls only the excess in the first Euler comparison; survival in
    $h_N$ additionally requires a compatible third consecutive Euler
    valuation. No such implication follows from the first regime.

The item-77 package is:

~~~
697f3b29d899a3dd229b6b7b9748ec77c74d60d603fb67ea5e7f10fef56cfdb3  sources/root_unity_quadratic_two_regime_canonical_no_go.md
b4508adf4f4235ccb65de8a17a7e24fc815434a67e35b8daf3ed8afd62f763e8  scripts/root_unity_quadratic_two_regime_canonical_certificate.py
05a48e1954f7999da7f042fccefb794c95c5eff65c66a82622d5168ab8060567  results/root_unity_quadratic_two_regime_canonical_certificate.json
398c9b03759673e2e0cce91e52abe74bf2a70b098f546158c8e972fba6de4398  results/root_unity_quadratic_two_regime_canonical_hashes.sha256
~~~

The all-parameter derivation, fixed-field height statement, manifest,
syntax, byte checks, and an independent exact replay pass. The replay
checked 120 Euler rows, 75,480 content instances, and 4,096 valuation
ledgers in under one second at about 68 MiB RSS. Item 77 is a sharp
canonical two-regime no-go, not a classification of $e+\pi$.

## Centered-cosh checkpoint item 78: balanced quadratic border content

The balanced centered-cosh Padé branch has now been reduced to an exact
two-border content problem.  Put



$$
F(x)={1\over2\cosh\sqrt{x}},\qquad {P_q\over Q_q}=[q/q]_F,
 \qquad {R_q\over G_q}=[q+1/q-1]_F,
$$



with the primitive normalization of $Q_q$.  The previous residual theorem
gives



$$
R_qQ_q-P_qG_q=\kappa_qx^{2q+1},\qquad (Q_q,G_q)=1.
$$



For $a_m=[x^m]P_q(x)^2/Q_q(x)$, a global-residue calculation now proves
the exact first-moment identities



$$
h_j=-{\operatorname{lc}(Q_q)\over\kappa_q^2}
       a_{4q+1-j},\qquad j=0,1.
$$



Consequently, whenever this first-moment pair is nonzero, the unique primitive
quadratic kernel direction is



$$
C_q^{\rm prim}(x)=
 \operatorname{prim}\bigl(a_{4q}-a_{4q+1}x\bigr).          \tag{78.1}
$$



There is also a completely integral realization.  If $T_q^\#$ is the
factorially cleared $q$-by-$(q+1)$ Toeplitz Padé matrix, $c_q$ its
primitive cofactor kernel, $\delta_q$ the gcd of its maximal minors, and
$b_{4q},b_{4q+1}$ the two cleared convolution-border rows, define



$$
u_m=b_m c_q,\qquad K_q=\gcd(u_{4q},u_{4q+1}).
$$



Then



$$
u_m={(-1)^q\over\delta_q}
       \det\!\begin{pmatrix}T_q^\#\\ b_m\end{pmatrix},
 \qquad
 C_q^{\rm prim}(x)={u_{4q}-u_{4q+1}x\over K_q}.           \tag{78.2}
$$



At every prime where $T_q^\#$ has full row rank, $p\mid K_q$ is
equivalent to simultaneous membership of both border rows in its row space
modulo $p$.  Thus the remaining arithmetic issue is a precise two-border
rank event rather than an unspecified Smith-content loss.  Factorial row
clearing and Hadamard give the all-parameter upper bound



$$
\log H(C_q^{\rm prim})\le(3+o(1))q^2\log q.              \tag{78.3}
$$



This improves the earlier generic cubic cofactor majorant, but it is only an
upper bound.  No all-$q$ proof that the two first moments are not both zero,
no lower bound on $K_q$, and no normalized global-lift height theorem is
known.  Exact computation through $q=16$ verifies nonvanishing and all
identities; the $q=11$ primitive pair has both coefficients odd, disproving
a universal parity-shape identification with the closer-root Euler family.

The frozen item-78 package is:

~~~
a7db026c1ebc792ab30a8674897d48ddbedce71da350a730966fdfee5c6132a8  sources/centered_cosh_balanced_quadratic_border_content_theorem.md
e0c2e1b22bf916242ce685d1c43a1b88477b5052858fe26221d17bfaefb7d3bd  scripts/centered_cosh_balanced_quadratic_border_content_certificate.py
8272e59ac346044fcc23a76321ccf4252596c4b942dd3fc714228b6a694f3a27  results/centered_cosh_balanced_quadratic_border_content_certificate.json
c06ea9b875ba072de9bf250526538f6639afd7fa0131719febb5df9f36067eb3  results/centered_cosh_balanced_quadratic_border_content_hashes.sha256
~~~

The manifest, syntax, exact identities, source delimiters, and byte checks all
pass.  An independent replay took about 1.7 seconds and peaked at
1,425,356 KiB RSS, with about 48 GiB still available on the machine.  The
2-GiB certificate field is a per-process runaway guard, not a global RAM cap.
Item 78 isolates a new local rank/content target; it does not classify
$e+\pi$.

## Root-of-unity checkpoint item 79: higher-determinant multiplicity barrier

The reduced beta ratios



$$
r_N={P_N\over Q_N}
 ={|E_{2N+2}|\over(2N+2)(2N+1)|E_{2N}|},
 \qquad \alpha={4\over\pi^2},
$$



admit the exact absolutely convergent signed-mode expansion



$$
r_N=\alpha\sum_{q\ \mathrm{odd}}b_qq^{-2N},
 \qquad
 b_q=(-1)^{\omega(q)}\chi_4(q)
       {\prod_{p\mid q}(p^2-1)\over q^3}\quad(q>1).       \tag{79.1}
$$



All $b_q$ are nonzero, but the signs vary; in particular
$b_3=8/27$ and $b_5=-24/125$.  This rules out a direct positive
Stieltjes-moment treatment.

For $h\ge2$, the unique $h$-term filter that kills the constant mode
and the first $h-2$ nonconstant modes is



$$
A_h(X)=(X-1)\prod_{j=1}^{h-2}((2j+1)^2X-1).
$$



It has $\log H(A_h)=2h\log h+O(h)$, first surviving base
$(2h-1)^{-2}$, and the uniform estimate



$$
|L_{N,h}|\le {4\over\pi^2}(2h-1)^{-2N}
 \left({1\over2h-1}+{1\over2N}\right).                   \tag{79.2}
$$



An explicit tail comparison proves nonvanishing for
$N\ge N_0(h)=O(h^2)$.  With one universal denominator copy for each
ratio, its gain per copy satisfies



$$
{2\log(2h-1)\over h}\le\log3,                           \tag{79.3}
$$



with equality only at $h=2$.  Higher fixed linear cancellation therefore
cannot beat the original adjacent row at the analytic-per-copy level.

Three determinant variants give the same obstruction.  The all-size
Vandermonde floor is only $O(N+h)$ per denominator, with a uniform
asymptotic showing no hidden $\log(N+h)$.  A fixed $h$-by-$h$ Hankel
determinant is eventually nonzero by its unique first $h$ signed
Dirichlet modes, but its universal clearing has $h^2$ denominator copies.
The simultaneous higher-Euler-ratio determinant telescopes to products of
the original $r_N$'s and has $h(h-1)$ copies.  Moreover,



$$
\det(r_{1+i+j})_{0\le i,j<3}
 =-{1238314183775556121\over51629038152493172462784000}<0,\tag{79.4}
$$



so ordinary Hankel total positivity already fails.

The theorem leaves two genuine escapes: growing-size signed-Hankel
nonvanishing with stronger decay, or a large systematic reduction of the
actual lcm/common numerator content relative to the universal clearing.
Both require new correlation information among adjacent Euler-number gcds.

The frozen item-79 package is:

~~~
e921fcb73e8c3fc4d62848008cc34d1f9ff0ee482fcba1e8ef5123462df1bca6  sources/root_unity_beta_higher_determinant_multiplicity_barrier.md
936b03be9dc6c63d17616d9e38c0c0c9a67755e1f8e20a746b2fe4fceaebaca7  scripts/root_unity_beta_higher_determinant_certificate.py
2f53dd329f9eef44bdd22868ec558da0a6f9c9f874d88cb077e3e53ddf9830ba  results/root_unity_beta_higher_determinant_certificate.json
abf5aae37871defe5a5fb0237506b0830fca17d94a6dd914bdf3994b086cf5c9  results/root_unity_beta_higher_determinant_hashes.sha256
~~~

The manifest also pins the frozen item-76 beta-floor dependency.  Independent
replay took about 0.21 seconds at 37,188 KiB peak RSS; proof, syntax, JSON,
dependency, delimiter, and byte audits pass.  Item 79 closes the canonical
higher-filter shortcuts, not the classification of $e+\pi$.

## Root-of-unity checkpoint item 80: adjacent descent and discriminant barrier

Write $A_N=(2N+2)(2N+1)$ and $h_N=\gcd(Q_N,Q_{N+1})$.
For every prime put



$$
b=v_p(A_N),\ c=v_p(A_{N+1}),\quad
 x=v_p(E_{2N}),\ y=v_p(E_{2N+2}),\ z=v_p(E_{2N+4}).
$$



Exact reduction gives



$$
v_p(h_N)=\min((b+x-y)_+,(c+y-z)_+).                     \tag{80.1}
$$



Away from $A_NA_{N+1}$, support is therefore equivalent to the strict
descent $x>y>z$, and $2v_p(h_N)\le x$.  If
$h_N^{\rm off}$ is the off-index part, then



$$
(h_N^{\rm off})^2\mid |E_{2N}|,
 \qquad h_N^2\mid A_NA_{N+1}|E_{2N}|,
 \qquad v_2(h_N)=1.                                      \tag{80.2}
$$



This is a genuine squarefull-layer restriction, but it supplies only
$\log h_N\le N\log N+O(N)$, not the subexponential neighboring-gcd
bound needed by item 77.

The same common Euler divisibility has an exact polynomial interpretation.
For even $M=2m$, define



$$
\mathcal F_M(T)=\sum_{j=0}^M\binom MjE_jT^{M-j}=f_M(T^2).
$$



If $d\mid E_M,E_{M-2}$, then zero is a fourth-order modular root:



$$
\mathcal F_M(T)\equiv T^4V(T)\pmod d,
 \qquad f_M(Y)\equiv Y^2W(Y)\pmod d.                     \tag{80.3}
$$



The resultant identity and the exact composition discriminant formula give



$$
d\mid\operatorname{Disc}(f_M),\qquad
 \operatorname{Disc}(\mathcal F_M)=
 (-4)^mE_M\operatorname{Disc}(f_M)^2,
 \qquad d^3\mid\operatorname{Disc}(\mathcal F_M).        \tag{80.4}
$$



However, the Sylvester matrix has dimension $O(M)$ and entries bounded by
$M!$, hence logarithmic determinant size $O(M^2\log M)$.  This is worse
by a factor of order $M$ than the trivial bound $d\le|E_{M-2}|$.

A level-4 Eisenstein-series encoding fails for a separate exact reason:
Euler divisibility kills only its constant term, while the coefficient of
$q$ remains a unit.  Neighboring weights also have distinct residual
eigenpackets for $p>3$, and a full Sturm/congruence determinant again has
the $O(M^2\log M)$ ledger.  Thus neither natural elimination globalizes
the strict valuation descent at the required scale.

The frozen item-80 package is:

~~~
28696128629ac4828d492dc5736545c8558e4546a3b566dfc2ecf7aa85170d13  sources/root_unity_adjacent_euler_descent_discriminant_barrier.md
8d1a5c5577389fb009eb3a1596c77d1cffc5183526515440db8f2f7553a9adf2  scripts/root_unity_adjacent_euler_descent_discriminant_certificate.py
2a62637288d4f807e4d34c17bdeaa64b5a03164f0303b18c27373bd7e47b1890  results/root_unity_adjacent_euler_descent_discriminant_certificate.json
57de6b30c8efc92532d3d7c8292e2467d176983baeb20443d7f17cfecf4f7f14  results/root_unity_adjacent_euler_descent_discriminant_hashes.sha256
~~~

All three frozen dependencies, the manifest, syntax, exact replay, equation
tags, delimiters, and byte audits pass.  The independent root replay took
under one second, reported 1,445,632 KiB peak RSS, and left about 47--48 GiB
available.  Item 80 proves structural descent and two quantitative no-go
ledgers; it does not classify $e+\pi$.

## Root-of-unity checkpoint item 81: actual block lcm and Kummer barrier

Let



$$
r_n=\frac{|E_{2n+2}|}{(2n+1)(2n+2)|E_{2n}|}
     =\frac{P_n}{Q_n}
$$



in lowest terms, and put



$$
{\cal Q}_{N,h}=\operatorname{lcm}(Q_N,\ldots,Q_{N+h-1}).
$$



The optimal $h$-term beta filter from item 79 has integral
coefficients, so the actual block lcm clears it.  Its certified
nonvanishing and tail bound give



$$
{\cal Q}_{N,h}\ge
 \frac{(2h-1)^{2N}}
 {(4/\pi^2)((2h-1)^{-1}+(2N)^{-1})}
 \qquad(N\ge N_0(h)),
$$



where $N_0(h)\le2h^2+2$.  Hence, for



$$
h_N=\left\lfloor\sqrt{\frac{N-2}{2}}\right\rfloor,
\qquad
 \log{\cal Q}_{N,h_N}\ge N\log N-O(N).                  \tag{81.1}
$$



This is an actual-lcm theorem, not a product-clearing estimate.  If



$$
U_n=|E_{2n}|,\quad A_n=(2n+1)(2n+2),\quad
 B_n=\frac{U_n}{\gcd(U_n,U_{n+1})},
$$



then the exact primewise formula proves



$$
B_n\mid Q_n\mid A_nB_n.
$$



The elementary $A_n$-block lcm costs only
$O(\sqrt N\log N)$, so the $B_n$-block lcm retains the
$N\log N-O(N)$ lower bound.

For $M=N+h$, truncate each prime exponent at the largest $a$ with
$\varphi(p^a)\le2M$.  This Kummer-visible factor divides
$\operatorname{lcm}(1,\ldots,3M)$ and therefore has logarithm
$O(M)$.  The complementary block factor ${\cal J}_{N,h_N}$ satisfies



$$
\log{\cal J}_{N,h_N}\ge N\log N-O(N).                   \tag{81.2}
$$



Every one of its layers is witnessed by a strict adjacent Euler
valuation drop at a shifted threshold $p^t$ with
$\varphi(p^t)/2>M$.  Standard Kummer periodicity consequently reaches
no second index in the block and supplies no concentration theorem for
exactly this large mass.  The unstructured conversion from an lcm to a
single denominator has rate



$$
\frac{2\log(2h-1)}h\le\log3,
$$



with equality only at $h=2$; even (81.1) therefore yields no individual
$N\log N$ denominator bound without a new first-period
concentration/overlap theorem.

Frozen item-81 package:

~~~
a0f3811a353cf19778bf0b262f20190de3735dccf8c2081a35d0b8c19035af28  sources/root_unity_beta_actual_lcm_kummer_barrier.md
fa9cda18584bbbb71cf5b12652ffd5c839468cc49886274a3e724d2b4205fdaf  scripts/root_unity_beta_actual_lcm_kummer_certificate.py
ae75d93ca1373db85dd704f8d20dabe0053797aac980efcee40b57f12dc92a13  results/root_unity_beta_actual_lcm_kummer_certificate.json
df801458d310f255dc59862dca63abedb3976eefc9edb680e9a75fc4662ec6ec  results/root_unity_beta_actual_lcm_kummer_hashes.sha256
~~~

The manifest, dependencies, syntax, control-byte scan, and independent
replay pass.  The root replay took $0.166$ seconds and $40{,}848$ KiB
peak RSS.  Item 81 isolates a first-period concentration problem; it does
not classify $e+\pi$.

## Centered-cosh checkpoint item 82: universal balanced nonvanishing

The conditional endpoint clause in item 78 is now removed.  For the
normal diagonal Padé pair



$$
F(x)=\frac1{2\cosh\sqrt x},\qquad FQ-P=O(x^{2q+1}),
\qquad Q(0)>0,
$$



put $a_m=[x^m]P^2/Q$.  Then, for every $q\ge1$,



$$
\boxed{a_{4q}>0,\qquad a_{4q+1}<0.}                     \tag{82.1}
$$



The proof writes $H(y)=2F(-y)=\sec\sqrt y$ as the complete-symmetric
generating function of the positive alphabet



$$
t_\nu=\frac4{\pi^2(2\nu+1)^2},\qquad
 e_j(t)=\frac1{(2j)!}.
$$



If $B(y)=Q(-y)$ is put in cofactor normalization and
$BH-p=E$, Jacobi--Trudi straightening gives



$$
[y^n]BH=
 \begin{cases}
 s_{(q^q,n)}(t),&0\le n\le q,\\
 0,&q<n\le2q,\\
 (-1)^q s_{(n-q,(q+1)^q)}(t),&n\ge2q+1.
 \end{cases}                                             \tag{82.2}
$$



Odd $q$ follows immediately from coefficient signs.  For even $q$,
restricting tableaux to $\mu=(q^q)$ and its skew complement gives
$s_\Lambda/s_\mu\le s_{\Lambda/\mu}$.  The complement contains a
full column of $q+1$ boxes; discarding every remaining tableau
constraint proves



$$
s_{\Lambda/\mu}(t)
 \le e_{q+1}(t)h_1(t)^{n-q-1}
 =\frac{2^{-(n-q-1)}}{(2q+2)!}.
$$



Together with $h_j\le2^{-j}$ and
$h_m\ge(4/\pi^2)^m$, this makes the error convolution strictly smaller
than the positive constant-term contribution at $m=4q,4q+1$.
The elementary majorant is checked at $q=2$ using $\pi^2<10$, and
its successive ratio is



$$
\frac{\pi^8}{2048(2q+1)(2q+4)}<1.
$$



Thus both residual first moments in item 78 are individually nonzero,
and its primitive survivor has exact degree one in $x$, hence exact
degree two in the original even endpoint variable, for every $q$.
This theorem does not estimate the two-border content $K_q$ or the
normalized global lift height.

Frozen item-82 package:

~~~
6531d74029b442f3893425ef056af1dd2536988a2b508801439ab8e208493139  sources/centered_cosh_balanced_quadratic_nonvanishing_theorem.md
8d5ba5f486e8d5b422a9685d2665b70085a12152ee986b0832495ab770d85558  scripts/centered_cosh_balanced_quadratic_nonvanishing_certificate.py
3886c53959e0d263b6f803ec25b55facdea77aa6d7738b65a91f6385f0cb83e9  results/centered_cosh_balanced_quadratic_nonvanishing_certificate.json
f5d5ef9179b0386e259aac0c95969461c1244ed756c5b38b2c75ca94bc4e3f82  results/centered_cosh_balanced_quadratic_nonvanishing_hashes.sha256
~~~

The manifest, syntax, exact signs, Schur identities, delimiter checks,
control-byte scan, and independent replay pass.  The replay took about
$1.10$ seconds and $72{,}876$ KiB peak RSS.  Item 82 proves universal
local nonvanishing, not a classification of $e+\pi$.

## Root-of-unity checkpoint item 83: normalized bounded-eliminant no-go

For the ordinary Euler polynomial ${\cal E}_{2m}(X)$, invariant-ring
reduction gives a monic integral polynomial $P_m$ of degree $m-1$:



$$
{\cal E}_{2m}(X)=X(X-1)P_m(X(X-1)).
$$



If $d\mid E_M,E_{M-2}$, $M=2m$, then
$U=-1/4$ is a double root of $P_m$ modulo the full odd modulus
$d$, and hence



$$
d\mid\operatorname{Disc}(P_m).   \tag{83.1}
$$



This removes the permanent roots and artificial affine powers of $4$
from item 80.  The degree remains linear, and the direct Sylvester bound
is still $O(M^2\log M)$.

The exact first-period seed $M=3288,\ p=151483$ is decisive against a
higher-subdiscriminant shortcut:



$$
\gcd(f_{3288},f_{3288}')=Y,\qquad
 \gcd\!\left(f_{3288}/(Y-1),(f_{3288}/(Y-1))'\right)=Y
 \quad\text{in }\mathbb F_p[Y].
$$



Thus $P_{1644}$ has exactly one double root and every other root is
simple.  Only the resultant end of the subresultant chain is forced to
vanish.  The Appell differential recurrence supplies no third
congruence at the fixed point; all centered shift jets are parity or
permanent-root identities.  This is a restricted no-go for the
canonical bounded-jet constructions, not for every possible eliminant.

Frozen item-83 package:

~~~
8cecdea69be6432aac7f3dee4e8851e31977b2a9dce00f44620931e249353550  sources/root_unity_adjacent_euler_bounded_eliminant_no_go.md
2fd8c166a342e368bfc56d2c8391fd2b7dcae11eb9ef8897c02d41084da6475b  scripts/root_unity_adjacent_euler_bounded_eliminant_certificate.py
6792b17675377119323f546a61776fe533a5baefcdc5248725c65b76b50b0eab  results/root_unity_adjacent_euler_bounded_eliminant_certificate.json
6c451189b41e7ddaa3563da40a4c119a159c2442a873c6451c2bda8665c53dfe  results/root_unity_adjacent_euler_bounded_eliminant_hashes.sha256
~~~

Independent replay of the full degree-1644 modular gcd took $3.1$
seconds and $77{,}004$ KiB peak RSS.  Item 83 neither bounds the
first-period factor nor classifies $e+\pi$.

## Centered-cosh checkpoint item 84: factorial-Pascal height theorem

The balanced diagonal secant Padé pair has an integral even-factorial
model.  If



$$
W_{r,i}=\binom{2(q+r)}{2i}\quad
 (1\le r\le q,\ 0\le i\le q)
$$



and $d_i$ is the positive minor deleting column $i$, then



$$
p(y)=\sum_{i=0}^q\frac{d_i}{(2i)!}y^i,\qquad
 B(y)=\sum_{k=0}^q\frac{e_k}{(2k)!}y^k,
$$



where



$$
e_k=\sum_{i=0}^k(-1)^{k-i}\binom{2k}{2i}d_i.
$$



The signed Pascal cofactor identity proves $BH-p=O(y^{2q+1})$.
Strict total positivity proves every $d_i>0$ and also makes
$e_q\ne0$, so the pair has exact type $[q/q]$.

Writing $H(y)=\sec\sqrt y$, the endpoint coefficients
$A_m=[y^m]p^2/B$ satisfy



$$
A_m=\frac{w_m}{(2m)!}\qquad(m\le4q+1)
$$



for explicit integral Euler/binomial convolutions $w_m$.  Therefore



$$
C_q^{\rm prim}(x)=
 \operatorname{prim}\!\left(
 (8q+2)(8q+1)w_{4q}+w_{4q+1}x\right).                    \tag{84.1}
$$



Hadamard on the Pascal rows gives



$$
\max_i d_i<2^{3q^2+q},
$$



and the exact convolutions yield the improved all-order estimate



$$
\boxed{\log H(C_q^{\rm prim})
 \le3(\log2)q^2+O(q\log q).}                             \tag{84.2}
$$



This removes the earlier spurious $q^2\log q$ factorial cost, but the
available analytic gain is only $2q\log q+O(q)$, and no normalized
global-lift bound follows.

Frozen item-84 package:

~~~
5e1fdadfd00705921fa05f97472af266d5eaf86ed9c70c67bab7547f47729c07  sources/centered_cosh_factorial_pascal_height_theorem.md
50086d13c37301566fa2e500d495b49bbfa7ee116d02b52a9cb298936b898e28  scripts/centered_cosh_factorial_pascal_height_certificate.py
aa27ea7ef6ba580a76947d4e50f287ee921f40bea751c5f8ef0d19ecf2620e2d  results/centered_cosh_factorial_pascal_height_certificate.json
9c607dca829bbb5b9f7255a8a5c37563c41523fea6524643c4ea893add5956a4  results/centered_cosh_factorial_pascal_height_hashes.sha256
~~~

The independent replay took $0.231$ seconds and $64{,}776$ KiB.
Item 84 is a sharper local height theorem, not a classification.

## Centered-cosh checkpoint item 84a: exact $q=13$ through $100$ scan

A separate resumable FLINT scan begins strictly above the frozen
$q\le12$ certificate grid and contains all 88 exact rows
$13\le q\le100$.  At $q=100$,



$$
\frac{\log H_{\rm prim}}{q^2}=1.5621890918\ldots,\qquad
 \frac{-\log|r_q-4/\pi^2|}{q}=8.8099182292\ldots.
$$



The primitive height has 22,538 bits, versus only 861 bits in the
two-coordinate endpoint content.  No content collapse occurs on the
grid.  Complete factorizations at $q=30,50,75,100$, and separately
for all $q\le25$, contain only primes at most $8q+2$; the sampled
maximum exponent is $5$.  This is evidence for exponential content,
not an all-$q$ theorem.

Frozen diagnostic files:

~~~
0b7bb1ab95581ec660d5b1c4445e5d2e3a45247521500e4d450e0e66499b12e2  sources/centered_cosh_factorial_pascal_extended_scan.md
a43d49d009a1aa6a976097f42fecfd2ec8903538518ccff7c8abd860b73d39c9  scripts/centered_cosh_factorial_pascal_extended_scan.py
5b562dc109f2a247ba4094bea8078826c7cc5ac3c04fe75f9452ae93387359f6  results/centered_cosh_factorial_pascal_extended_scan.json
00c68385ad3fbcbf61f821cf9c5fb47b5a0a841cfd28667849c86dfbbbdb5249  results/centered_cosh_factorial_pascal_extended_scan_hashes.sha256
~~~

The scan checkpointed every row, used a 12-GiB failure guard, peaked at
about $1.56$ GiB, and left about $47$ GiB available.  Its exact
integer arithmetic was CPU-bound; the T4 accelerator offered no useful
kernel.  Finite trends are not a proof about $e+\pi$.

## Root-of-unity checkpoint item 85: full first-period moment complexity

For every odd prime $p$, put $r=(p-1)/2$.  Pairing the primary
Cosgrave--Dilcher power-sum congruence gives the exact finite-field model



$$
E_{2n}\equiv M_p(n)=
 2\sum_{j=0}^{r-1}(-1)^j\bigl((2j+1)^2\bigr)^n\pmod p,
 \qquad n\ge1.                                           \tag{85.1}
$$



The $(2j+1)^2$ are exactly all $r$ distinct nonzero quadratic
residues and every displayed weight is nonzero.  Therefore $M_p$ has
minimal constant-coefficient recurrence order exactly $r$, with
characteristic polynomial $Z^r-1$.  Its unique weight interpolant is



$$
W_p(X)=-2\sum_{k=1}^{r}E_{2k}X^{r-k},\qquad
 W_p(X)^2\equiv4\pmod{X^r-1},\qquad \deg W_p=r-1.        \tag{85.2}
$$



Every full $r$-by-$r$ moment Hankel determinant is a nonzero
weighted Vandermonde square.  Hence two adjacent zero moments create no
rank defect in the full support model.  The sole endpoint prime
$p=2N+3$ contributes at most $O(\log N)$; for strict first-period
primes the adjacent divisibility condition is precisely the vanishing of
two adjacent Fourier coefficients of the particular square root (85.2).

At the exact seed $(N,p)=(1643,151483)$, one has $r=75741$,
$\deg W_p=75740$, and the two coefficients vanish while the full
Hankel determinant remains nonsingular.  Thus bounded-order linear
recurrences, bounded-degree interpolation, and the canonical moment-rank
determinant cannot supply the missing cross-prime concentration estimate.
This is deliberately not an impossibility theorem for nonlinear or
arithmetic couplings, and it does not bound the first-period prime product.

Frozen item-85 package:

~~~
4b24dbecf01e1a06690d4b75b620beb741c6825d6c1e1729cc28c333f020cd4e  sources/root_unity_adjacent_euler_first_period_moment_obstruction.md
46af6d5b3f93744f96eb023ddcb40b5085f956304b7f70a7700f29c99c1b6341  scripts/root_unity_adjacent_euler_first_period_moment_certificate.py
9abd8499467b5e0bc6830045195ba454b6dda212d449d3029d4dbe0b40260002  results/root_unity_adjacent_euler_first_period_moment_certificate.json
af340ed10de55eb9587fdb3167d475b7f5cda405367fedb3ca00244ed1b23adf  results/root_unity_adjacent_euler_first_period_moment_hashes.sha256
~~~

Independent replay took about $1.11$ seconds and $27{,}604$ KiB
peak RSS.  The exact recurrence qualifier is constant-coefficient and
linear; item 85 neither proves (nor disproves) the needed prime-product
bound and does not classify $e+\pi$.

## Centered-cosh checkpoint item 86: normalized direct global lift

The quotient/Cramer gap left by items 78 and 84 is now removed.  For the
normal Padé pairs $(Q,P)$ of type $[q/q]$ and $(G,R)$ of type
$[q+1/q-1]$, both normalized to constant term one, the complete
balanced endpoint image has the exact direct decomposition



$$
\boxed{{\cal E}_{q,1}=Q^2{\cal P}_q\oplus
 QG{\cal P}_{q-1}\oplus G^2{\cal P}_{q-2}}.             \tag{86.1}
$$



Let $T_q=(u_{4q}-u_{4q+1}x)/K_q$ be the universally nonzero primitive
integer endpoint.  Reduction modulo $Q$ gives a canonical right inverse:



$$
\begin{aligned}
 C&=\rho_Q(G^{-2}T_q),&J&=(T_q-G^2C)/Q,\\
 B&=\rho_Q(G^{-1}J),&A&=(J-GB)/Q.
 \end{aligned}
$$



Every division is exact,
$\deg A,\deg C\le q-2$, $\deg B\le q-1$, and



$$
T_q=Q^2A+QGB+G^2C.                \tag{86.2}
$$



Writing



$$
{\cal Q}=Q(z^2)-2\cosh z\,P(z^2),\qquad
 {\cal G}=G(z^2)-2\cosh z\,R(z^2),
$$



the explicit global form



$$
{\cal L}_q=A(z^2){\cal Q}^2+B(z^2){\cal Q}{\cal G}
                    +C(z^2){\cal G}^2                   \tag{86.3}
$$



has frequencies $-2,\ldots,2$, polynomial degree at most $6q$,
origin order at least $8q+4$, and endpoint
$T_q(-\pi^2/4)$.  Linearity proves exact coefficientwise division by
the two-border content $K_q$; no ambient determinant is used.

A prime-by-prime denominator



$$
{\mathfrak D}_q=\prod_{p\le4q}
 p^{\lfloor2(q^2+q)/(p-1)\rfloor}
$$



clears every diagonal Schur cofactor.  Each relevant shape contains
$q$ forced columns of height $q$, so tableau relaxation contributes
$((2q)!)^{-q}$ and cancels the $2q^2\log q$ leading clearing cost.
Together with stable negative powers in $\mathbb Q[x]/(Q)$ and an
explicit normalized lower bound for the cross coefficient $\kappa$,
this proves



$$
\boxed{\log H(T_q)=O(q^2),\qquad
        \log H_{\rm an}({\cal L}_q)=O(q^2).}             \tag{86.4}
$$



The global coefficients are rational and are used only for the analytic
Schwarz bound on the already primitive integral endpoint; (86.4) makes no
common-denominator or primitive-integral-global-height assertion.  The
replay finds $H_{\rm an}=3H(T_q)/2$ for $2\le q\le7$, but this is
explicitly finite-only.  Most importantly, the proved $O(q^2)$ scale
still exceeds the available $2q\log q+O(q)$ Schwarz gain.

Frozen item-86 package:

~~~
b5448650b31b887a163ba95f593e38fc5c45195b61800f8c834ecb7ed2369d9f  sources/centered_cosh_balanced_quadratic_normalized_global_lift_theorem.md
46dd6f87dbec2927c81a870225b8bee9542684ab48ceb391514d3aaab1c1e092  scripts/centered_cosh_balanced_quadratic_normalized_global_lift_certificate.py
d9fa114ca1047846654015ff5353631db481269a40f7c48414f918a956d9481c  results/centered_cosh_balanced_quadratic_normalized_global_lift_certificate.json
90c432faf5130880664ffa561aff0faa7d574dde8c1f50c265a13dc3002591c8  results/centered_cosh_balanced_quadratic_normalized_global_lift_hashes.sha256
~~~

Independent replay took about $3.85$ seconds and $77{,}596$ KiB
peak RSS.  Item 86 closes the rational analytic lift gap, not the
quadratic-versus-$q\log q$ scale gap, and does not classify $e+\pi$.

## Drive backup after item 86

A full streaming backup of this research directory was created at

`/content/drive/MyDrive/e_pi_research_20260826_backup_20260827T183247Z.tar.gz`.

It contains 839 archive entries, has size 7,787,203 bytes and SHA-256

`c1051be18b4263434aabe2989ee551b4ef2b4928a8a9f6a8576ce1c5b0b7c302`.

Both `gzip -t` and a complete `tar -tzf` listing passed.  The backup is
additional recovery state; it is not a research result.

## Root-of-unity checkpoint item 87: bounded cyclic-window section no-go

Normalize the first-period interpolant by



$$
A_p(X)=-\frac12C_p(X)=\sum_{k=0}^{r-1}a_kX^k,qquad
 r=(p-1)/2.
$$



The exact square-root identity becomes



$$
A_p(X)^2\equiv1\pmod{X^r-1},\qquad
 F_t(\boldsymbol a):=\sum_{i=0}^{r-1}a_i a_{\langle t-i\rangle_r}
 =\delta_{t,0}.                                           \tag{87.1}
$$



The wraparound coefficients in (87.1) cannot be discarded.  More
strongly, let $S$ be prescribed coefficient indices and $T$ selected
convolution indices.  If a residue $u$ separates $S$, $T-u$, and
their relevant pairwise sumsets, then over any ring with $2$ invertible
there is an explicit polynomial section:



$$
a_u=1,\qquad
 a_{t-u}=\frac{c_t-B_t(\boldsymbol b)}2\quad(t\in T),
$$



with all other unseen coefficients zero.  It realizes arbitrary
prescribed $a_s=b_s$ and $F_t=c_t$.  Hence the selected convolution
ideal has zero intersection with the low-data ring; after any existing
low ideal ${\cal J}$, including $a_N=a_{N+1}=0$, its intersection is
exactly ${\cal J}$.

For initial intervals $S\subseteq[0,L]$, $T\subseteq[0,K]$, the
anchor $u=L+K+1$ works whenever



$$
r>2L+3K+2.                  \tag{87.2}
$$



Taking $L=K=N+1$, the section applies to every
$p>10N+15$.  All complementary first-period primes have total
logarithmic mass $O(N)$ by Chebyshev.  Thus precisely on the far-prime
range needing an $o(N\log N)$ estimate, the first $N+2$ cyclic
equations add no formal algebraic restriction on the low Euler prefix.

At $(N,p)=(1643,151483)$, the explicit anchor $u=3289$ and 1,645
far partners give a sparse synthetic completion satisfying
$F_0=1,F_1=\cdots=F_{1644}=0$, including the two actual adjacent
Euler zeros.  The next equation fails, as intended, so the example does
not masquerade as a global square root.  The theorem leaves open use of
all $r$ equations, nonlocal $p$-dependent selections, or additional
arithmetic information about the actual sign assignment.

Frozen item-87 package:

~~~
e783aeb445472e0630e7945931a5978b9a0a15180dee03e1409cb59693f8b1b8  sources/root_unity_adjacent_euler_cyclic_window_section_no_go.md
cb8301f80b2c5d3b57d6f8b6901d00c9c7d2484cd2f424a5ec55581c938a1ff0  scripts/root_unity_adjacent_euler_cyclic_window_section_certificate.py
9614598edb4ecb125e73696e38615df0b3e56466e7468f69630c581fb3988276  results/root_unity_adjacent_euler_cyclic_window_section_certificate.json
f955bf4e71a080d0622e314352a3784b93cc772a3146e66bdb258c35e1ce3904  results/root_unity_adjacent_euler_cyclic_window_section_hashes.sha256
~~~

Independent replay took about $3.01$ seconds and $20{,}848$ KiB
peak RSS.  Item 87 is a formal bounded-window no-go, not a global
prime-product estimate and not a classification of $e+\pi$.

## Centered-cosh checkpoint item 88: exact Pascal/border normalization bridge

The factorial-Pascal denominator and the primitive ordinary denominator in
the earlier bordered centered-cosh construction have now been matched with
their exact scale.  Let $d=(d_0,\ldots,d_q)$ be the positive primitive
signed-Pascal cofactor vector and set



$$
e_k=\sum_{i=0}^k(-1)^{k-i}\binom{2k}{2i}d_i,
 \qquad
 B_d(y)=\sum_{k=0}^q\frac{e_k}{(2k)!}y^k.
$$



The binomial transform from $d$ to $e$ is lower unitriangular over
$\mathbb Z$, hence $\gcd(e_0,\ldots,e_q)=1$.  Define



$$
g_{B,q}=\gcd_{0\le k\le q}
       \left(e_k\frac{(2q)!}{(2k)!}\right),
 \qquad s_q=\frac{(2q)!}{g_{B,q}}.
$$



A Bezout identity for the $e_k$ proves $g_{B,q}\mid(2q)!$.  Therefore
$s_q$ is an integer dividing $(2q)!$, and



$$
Q_q^{\rm ord}(x)=s_q B_d(-x)
$$



has primitive integral ordinary coefficients.  Since the relevant Pade
kernel is one-dimensional, this is exactly, up to global sign, the primitive
denominator used by the bordered construction.

If $w_m$ denotes the exact factorial-Pascal residual sequence, put



$$
L_q=(8q+2)(8q+1)w_{4q},\qquad
 R_q=w_{4q+1},\qquad
 G_q^{\rm Pascal}=\gcd(L_q,R_q).
$$



Direct coefficient scaling gives the all-parameter endpoint identity



$$
(u_{4q},u_{4q+1})=(s_qL_q,-s_qR_q)
$$



for a consistent global sign, and hence



$$
\boxed{K_q^{\rm border}=s_qG_q^{\rm Pascal}.}           \tag{88.1}
$$



This removes an ambiguity that previously made the two recorded contents
look directly comparable.  It does not yet supply the needed all-parameter
content bound.  The complete finite scan $1\le q\le30$ finds only primes at
most $8q+2$ in $G_q^{\rm Pascal}$, and for $2\le q\le30$ finds



$$
G_q^{\rm Pascal}\mid\operatorname{lcm}(1,\ldots,8q+2)^2.
$$



These are finite diagnostics only.  The edge $q=1$ does not satisfy the
displayed square bound, and no fixed-power lcm divisibility or smoothness
theorem for all $q$ is claimed.  The canonical Jacobi continued fraction
was also reconstructed initially, but its coefficients already contain
irregular large primes and currently provide no local-prime explanation.

Frozen item-88 package:

~~~
6841a257ef7123c0080469335b5bd9a35c3f54ea36701a3894a95a447b6763cb  sources/centered_cosh_pascal_border_normalization_theorem.md
04e9f875ed419e1b3ba03595cf3a01dd3eb9cf0ed101254d2f6a2172822d813a  scripts/centered_cosh_pascal_border_normalization_certificate.py
01639485ade5a8b3b349a725861d436294a389e621d23a2da9c16dffadd3ad1c  results/centered_cosh_pascal_border_normalization_certificate.json
6b828f9c0a0b1aff69e598969cc9f2da3da7665307c99295136ba0b08fe3cb23  results/centered_cosh_pascal_border_normalization_hashes.sha256
~~~

The manifest additionally pins the older bordered certificate at
`8272e59ac346044fcc23a76321ccf4252596c4b942dd3fc714228b6a694f3a27`.
An independent clean replay took about $0.14$ seconds and reported about
$65$ MiB peak RSS; all hashes, syntax, and dependency checks pass.  Item 88
is an exact normalization theorem, not a classification of $e+\pi$.

## Common-kernel checkpoint item 89: positive quadratic Robin repair and gap

The Taylor near-solution's Robin defect can in fact be repaired integrally
and positively in every degree by a quadratic correction.  Put



$$
t=1-x,\qquad (1-i)^N=R_N+iI_N,\qquad M_N=N!-R_N.
$$



Every integral correction of degree at most two is uniquely



$$
C_{N,q}(t)=I_N-4q+\left(q-\frac{M_N}{2}\right)t-qt^2,
 \qquad q\in\mathbb Z,
$$



and the corrected residual is



$$
F_{N,q}=t^N+M_Nt\left(1-\frac t2\right)
          -I_N(1-t)+q(4-6t+4t^2-t^3).                    \tag{89.1}
$$



It satisfies



$$
A(F_{N,q})=F_{N,q}(i)=F_{N,q}(-i)=N!.
$$



Taking $q=0$ when $I_N\le0$, and
$q=\lceil I_N/3\rceil$ when $I_N>0$, proves



$$
F_{N,q}\ge M_Nt(1-t/2)\ge0\qquad(0\le t\le1).
$$



Thus the local endpoint repair problem itself is solvable.  However, exact
integration gives



$$
L\!\left(t-\frac{t^2}{2}\right)=\pi-\frac32,
 \quad L(1-t)=1+2\log2,
 \quad L(4-6t+4t^2-t^3)=10.
$$



Every positive quadratic repair consequently obeys, after exact rational
denominator clearing and removal of all output content,



$$
\boxed{
 \liminf_{N\to\infty}\Lambda_{N,q}\ge\pi-\frac32>0.}     \tag{89.2}
$$



The content calculation is exact: if the rational coordinate is $B/D$
in lowest terms, the primitive content is
$h=\gcd(N!D,B)=\gcd(N!,B)$, so
$\Lambda=(D/h)L\ge L/N!$.  Therefore even full factorial output content
cannot make this family shrink.

A Bernstein--Walsh/Markov argument extends the obstruction to every fixed
correction-degree bound $m$: any positive corrected family has



$$
\liminf\Lambda(F_N)
 \ge\frac{3}{8(m+1)^2C_RR^{m+1}}>0,
 \qquad R=4.6115817893\ldots .                            \tag{89.3}
$$



Hence any viable Robin correction must have genuinely growing degree or
new nonlocal structure.

Frozen item-89 package:

~~~
1611c4976a64836a20209871a55b92e09bcb6c0c9cb18701cd800567b1a0ac21  sources/common_kernel_stein_robin_quadratic_correction_barrier.md
f814471c0c627ff2fb9c4da2f99a4a37ebf6380316d030796c7ddc946c4921dc  scripts/common_kernel_stein_robin_quadratic_correction_certificate.py
4641657f345e13bde4ed84b4642ffd4942d3f6b8448f9c9a60ecbe573dbf216d  results/common_kernel_stein_robin_quadratic_correction_certificate.json
208982ad388c02ba42c79726b6eaefa8acd1ed7d5a2fad6de5c138a44483038a  results/common_kernel_stein_robin_quadratic_correction_hashes.sha256
~~~

The manifest pins both prerequisite theorem packages.  Independent replay
took about $1.45$ seconds at $21{,}360$ KiB peak RSS; hashes, syntax,
dependencies, and exact output all pass.  Item 89 is a constructive local
repair plus a bounded-degree no-go theorem, not a classification of
$e+\pi$.

## Centered-cosh checkpoint item 90: unbalanced one-third slope obstruction

The single-parity block of the unbalanced lower lift now has an exact
all-parameter Padé decomposition.  Write



$$
B=2M+\sigma,\qquad d=M+r,\qquad\sigma\in\{0,1\},
$$



and let $V_{M,r}^{(\sigma)}$ be the degree-at-most-$d$ polynomials
whose $F=(2\cosh\sqrt x)^{-1}$ product vanishes in degrees
$d+1,\ldots,B$.  With the two normal anti-diagonal entries



$$
(P,Q):[M+\sigma/M],\qquad
 (R,G):[M+1-\sigma\,/\,M+2\sigma-1],
$$



one has, for $1\le r\le M$,



$$
\boxed{
 V_{M,r}^{(\sigma)}
 =Q{\cal P}_{r-\sigma}\oplus G{\cal P}_{r-1}.}           \tag{90.1}
$$



The odd-terminal case $\sigma=1$ genuinely uses the lower Padé entry
$[M/(M+1)]$; using the even companion would give a false dimension.
When $M\ge2r-\sigma$, coprimality of $Q,G$ gives the further direct
sum



$$
\left(V_{M,r}^{(\sigma)}\right)^2
 =Q^2{\cal P}_{2r-2\sigma}\oplus
  QG{\cal P}_{2r-\sigma-1}\oplus
  G^2{\cal P}_{2r-2}.                                    \tag{90.2}
$$



Its dimension is $6r-3\sigma$, and its exact codimension in
${\cal P}_{2d}$ is



$$
\boxed{
 \delta=2M-4r+3\sigma+1=3(B-d)-d+1.}                    \tag{90.3}
$$



For the original lower-lift parameters,



$$
M=\frac{n+t}{4}+O(1),\qquad
 r=\frac{n-t}{4}+O(1),\qquad
 \delta=\frac{3t-n}{2}+O(1).
$$



Thus $t/n=1/3$ is the exact single-block codimension transition.
The minimum-degree problem is reduced, by reversal, to an explicit square
jet determinant for $1,H,H^2$ when $\sigma=0$, or $1,K,K^2$ when
$\sigma=1$, where



$$
H=y^2\widehat G/\widehat Q,
 \qquad K=y\widehat Q/\widehat G.
$$



The $(r,\sigma)=(1,1)$ determinant is automatically nonzero.  All 36
tested secant cases with $M\le8$ are nonzero, but that grid is explicitly
finite-only.  Neither general determinant nonvanishing nor the coupled
cancellation theorem for the two parity blocks has been proved.

A common Schur clearing proves input Padé log-height $O(M^2)$; direct
product-image minors cost $O(rM^2+r\log r)$.  Even the optimistic scale
$O(M^2)=O(n^2)$, if a new quotient theorem removed the factor $r$,
would exceed the centered gain $2t\log n+O(n)$.  This is a limitation of
the proved majorants, not a primitive-height lower bound.

Frozen item-90 package:

~~~
a9e1d82af845b01150b4075c26a45425d7907fbc1b48862d9b1ca70bb2e08f00  sources/centered_cosh_unbalanced_pade_slope_obstruction.md
193cda9b3eace30006c4ca839dac379212bf340dd5063e0b204a0a12cb81de0b  scripts/centered_cosh_unbalanced_pade_slope_obstruction_certificate.py
1699b6167fc69c3858fccb33abbdd9c27590a64ee14aa290b7eecfdf0d04db79  results/centered_cosh_unbalanced_pade_slope_obstruction_certificate.json
343a7a07d9a7b706caf7752a423b29e4b10be40f3c31cce0bfadc9d7ef978dd5  results/centered_cosh_unbalanced_pade_slope_obstruction_hashes.sha256
~~~

Two independent line audits found the corrected parity formulas sound.
The clean replay took about one second at $69{,}404$ KiB peak RSS;
hash, syntax, JSON, control-byte, and delimiter checks pass.  Item 90 is an
allocation/slope and majorant obstruction, not a classification of
$e+\pi$.

## Common-kernel checkpoint item 91: optimal integer Robin localizer barrier

There is an explicit sup-norm-optimal integer boundary layer preserving both
Robin jets.  With $u=1+x^2$, put



$$
h_m(x)=x^{4m}(m+1-mx^4),\qquad m\ge1.
$$



Then



$$
h_m\equiv1\pmod{u^2},\quad h_m(0)=0,\quad h_m(1)=1,
 \quad0\le h_m\le1,
$$



and



$$
\int_0^1h_m,dx
 =\int_0^1(1-x)h_m'(x)\,dx
 =\frac{8m+5}{(4m+1)(4m+5)}\sim\frac1{2m}.               \tag{91.1}
$$



Every integral $h\equiv1\pmod{u^2}$ satisfies
$h(1)\equiv1\pmod4$, so its sup norm on $[0,1]$ is at least one.
Thus this is an exact optimal boundary layer.  For fixed $K$, the product
rule gives



$$
\|{\cal T}(h_mK)\|_1
 \le \frac{8m+5}{(4m+1)(4m+5)}
       \left(\|{\cal T}K\|_\infty+\|K\|_\infty\right).
                                                               \tag{91.2}
$$



Despite this analytic localization, two rigorous obstructions prevent its
Taylor--Robin application.  First, no integral correction $K$ of the
Taylor near-solution can satisfy
$\operatorname{ord}_{x=1}K\ge N$.  An all-$N$ proof divides the Robin
defect equation by $(1-i)^N$ and reduces it modulo the Gaussian prime
$1-i$, or modulo its square in even degree.  Consequently, for every
fixed admissible $K$, the boundary-scaled residual has the sign-changing
limit



$$
-\frac{c y^r}{4^r}e^{-y}
 \left((r+1)(1+y)-y^2\right),
 \qquad r=\operatorname{ord}_{x=1}K<N.                   \tag{91.3}
$$



Hence sufficiently strong localization destroys positivity.

Second, the full rational output, not merely an unreduced expression, has
an unavoidable harmonic denominator.  If



$$
{\cal T}K=uG+(A+Bx),
$$



then a genuine Taylor repair forces



$$
A=N!-\Re(1-i)^N>0,qquad B=-\Im(1-i)^N.
$$



For fixed $N,K$, every prime



$$
\frac{5m}{2}<p<3m,\qquad p\nmid A,
$$



occurs to valuation exactly one in the reduced output denominator.  Thus



$$
\boxed{\log q_{N,K}(m)\ge(1/2+o(1))m.}                 \tag{91.4}
$$



If the residual were nevertheless nonnegative, its value at zero and a
Legendre/Markov spike bound would give, after exact primitive normalization,



$$
\Lambda_{N,K,m}
 \ge\frac{3q_{N,K}(m)}{N!(\deg F_{N,K,m}+1)^2}.           \tag{91.5}
$$



This diverges exponentially on the natural localizing diagonals
$\deg K=o(m)$, $N\log N=o(m)$.  The theorem does not exclude moderate
diagonals with rapidly varying $K_N$, nor nonlocal constructions outside
this family.

Frozen item-91 package:

~~~
5eb2a69842edfa4d6b8f88390834179e3e3cba65881af44120bc5161d1555ec8  sources/common_kernel_integer_robin_localizer_barrier.md
252ecc1e461d5572102a0ed784811815d537efdcb75afeb96571d038d102aa4a  scripts/common_kernel_integer_robin_localizer_certificate.py
2bcab0e6031398337afc7b2797c08e949f7fae546b34d695386838dc07059468  results/common_kernel_integer_robin_localizer_certificate.json
1754bcceff930fe5ed44b67282f666970aeabb5616886dfb1e5cab3eb19c4a07  results/common_kernel_integer_robin_localizer_hashes.sha256
~~~

The manifest pins both preceding common-kernel theorem packages.
Independent replay took about $0.16$ seconds at $21{,}072$ KiB peak
RSS, with about $47$ GiB system memory still available.  All source,
dependency, hash, syntax, and exact replay checks pass.  Item 91 closes this
specific sparse-localizer mechanism, not the classification of $e+\pi$.

## Common-kernel checkpoint item 92: every high-order Robin localizer has a prime-window denominator

The harmonic obstruction from item 91 is not special to the sparse
multiplier.  Put $u=1+x^2$, ${\cal T}P=(1-x)P'-xP$, and write



$$
{cal T}K=uG+(\alpha+\beta x).
$$



For an arbitrary integral multiplier



$$
h\equiv1\pmod{u^2},\qquad h(0)=0,qquad
 n=\operatorname{ord}_0h,qquad d=\deg h,
$$



define



$$
S_h=\frac{{\cal T}(hK)-{\cal T}K}{u}\in\mathbb Z[x].
$$



If $e_h=\deg S_h$, every odd prime satisfying



$$
p>\frac{e_h+1}{2},\qquad p-1>\deg G,qquad
 p<n,qquad p\nmid\alpha
$$



has the exact valuation



$$
\boxed{v_p\!\left(4\int_0^1S_h(x)\,dx\right)=-1.}       \tag{92.1}
$$



The proof uses the forced low prefix of
$r=(h-1)/u$: below degree $n$,



$$
r_{2j}=(-1)^{j+1},\qquad r_{2j+1}=0.
$$



In the exact product identity



$$
S_h=(h-1)G+r(\alpha+\beta x)
       +(1-x)\frac{h'}uK,
$$



the coefficient of $x^{p-1}$ is therefore $\pm\alpha$, while $p$
occurs in no other monomial-integration denominator.  Consequently, for
fixed correction data and
$n\ge(1/2+\varepsilon)d$, the prime number theorem gives



$$
\log\operatorname{den}\!\left(4\int_0^1S_h\right)
 \ge\varepsilon d+o(d),                                  \tag{92.2}
$$



up to the explicitly accounted fixed target and base-coordinate factors.
For the factorial Taylor correction, the base denominator divides
$\operatorname{lcm}(1,\ldots,N-1)$, while
$\alpha=N!-\Re(1-i)^N$; hence taking $d\gg N\log N$ does not erase
the prime window.

There is an independent analytic obstruction under $0\le h\le1$.
The congruence forces $h(1)=1$, and if
$s=\operatorname{ord}_{x=1}K$, then



$$
\bigl({\cal T}(hK)\bigr)^{(s)}(1)=-(s+1)K^{(s)}(1).
$$



Shifted Markov inequalities turn this retained endpoint jet into only a
polynomially small $L^1$ lower bound.  Multiplying it by the denominator
in (92.2) therefore diverges exponentially throughout the high-order
regime.

The scope boundary is genuine.  An exact sign-changing degree-ten witness
obeys the congruence, both endpoint conditions, and annihilates both defect
moments; thus congruence data alone do not exclude nonlocal cancellation.
The theorem leaves open families with $d\ge(2-o(1))n$, sign-changing
cross-channel cancellation, and substantially varying corrections.

Frozen item-92 package:

~~~
65b31f7df68551e35ecab50fb0f09026dbb87bd7e596075c13703367ac5a90c1  sources/common_kernel_robin_localizer_moment_denominator_barrier.md
84f878fe9f0e1cafecd32cb0661f760564ccf86018579e83ad4833b74bd0284f  scripts/common_kernel_robin_localizer_moment_denominator_certificate.py
c457c0aee6cdc289707c610083957a55c84b724205926930b694e8023a072fe0  results/common_kernel_robin_localizer_moment_denominator_certificate.json
1a523213cd86f5b3865bf86a7b35a4f0bd682df262af920cc7b02623f0560c03  results/common_kernel_robin_localizer_moment_denominator_hashes.sha256
~~~

The manifest pins item 89.  A clean root replay took about $6.32$ seconds
and reported $21{,}032$ KiB peak RSS; hashes, syntax, JSON, dependency,
and control-byte checks pass.  Item 92 is an all-parameter obstruction for
one broad construction class, not a classification of $e+\pi$.

## Centered-cosh checkpoint item 93: a universal squarefree content interval

The large-prime layer seen in the finite factorial-Pascal data is now an
all-parameter theorem.  With the established notation



$$
H(y)=\sec\sqrt y=\sum_{n\ge0}U_n\frac{y^n}{(2n)!},
 \qquad H(y)^2=\sum_{n\ge0}T_n\frac{y^n}{(2n)!},
$$



let $d_i$ be the primitive signed-Pascal kernel, let $e_k$ be its
unitriangular binomial transform, and define the two endpoint integers
$w_{4q},w_{4q+1}$ as in item 88.  Then



$$
\boxed{
  \prod_{\substack{\ell\ {\mathrm{prime}}\\4q<\ell\le8q+2}}\ell
  \ \bigm|\ 
  G_q^{\rm Pascal}
  =\gcd\!\left((8q+2)(8q+1)w_{4q},w_{4q+1}\right).}     \tag{93.1}
$$



For an odd prime $\ell$, put
$h=(\ell-1)/2$ and $\chi=(-1)^h$.  Euler-polynomial power sums prove



$$
U_{n+h}\equiv\chi U_n\pmod\ell\quad(n\ge1),\qquad
 T_{n+h}\equiv\chi T_n\pmod\ell\quad(n\ge0),           \tag{93.2}
$$



with the necessary exceptional value $U_h\equiv\chi-1\pmod\ell$.
The Lucas-reduced endpoint border is



$$
J_r=2\sum_i\binom{2r-1}{2i}d_iU_{r-i}
     -\sum_k\binom{2r-1}{2k}e_kT_{r-k}.
$$



For the Padé pair $p,B$, differentiation in the factorial basis gives



$$
rJ_r=-(2r)![y^r],2(BH-p)yH'=0
 \qquad(1\le r\le2q+1).                                 \tag{93.3}
$$



Lucas's theorem converts both endpoint coordinates modulo every prime in
the interval into one of these zero borders.  The midpoint
$\ell=4q+1$ and the possible prefactor prime $\ell=8q+1$ are handled
separately and exactly.

Equation (93.1) proves a universal *lower* content layer.  It does not prove
that no prime above $8q+2$ divides the gcd, that interval valuations are
small, or that the full gcd divides a fixed power of the lcm.  The natural
remaining object is the integer exceptional quotient obtained after
dividing by the squarefree product in (93.1).

Frozen item-93 package:

~~~
9e1a951e63b05455db4e6ade95f4b1a99b0c6330ff8680327f204b5e54f0b27d  sources/centered_cosh_pascal_universal_interval_content_theorem.md
cab278c79d3332e0d8f112fdaad0757fd309a5fcb24b120dad0ca384b67917a4  scripts/centered_cosh_pascal_universal_interval_content_certificate.py
18173a8bd0e455ac35bd3d2cebe3e0d73293f3ebe559381e63cb4e2531901384  results/centered_cosh_pascal_universal_interval_content_certificate.json
66e20c910ef2e167d8f52f57380086b0b97cfa473c0699901ad8c7f3f936ef78  results/centered_cosh_pascal_universal_interval_content_hashes.sha256
~~~

A clean root replay took about $0.36$ seconds and reported $34{,}304$
KiB peak RSS.  The symbolic proof, edge cases, hashes, JSON, Python syntax,
and declared finite diagnostics all pass.  Item 93 explains a genuine
universal content gain but does not classify $e+\pi$.

The completed but deliberately non-replayable aggregate continuation through
$111\leq q\leq220$ was preserved as
`results/centered_cosh_pascal_content_ephemeral_q111_220.json`, SHA-256
`919b54dab0fd0451182a3ea56d11c006e742b4dce963cda1b37a262bb162bf5b`.
Every completed row had exceptional quotient one after trial division through
$8q+2$, and no lcm-square valuation violation occurred.  Only aggregate
assertions were retained, so this file is finite evidence and is not promoted
to an all-parameter certificate.

## Common-kernel checkpoint item 94: an even nonlocal one-third prime window

The high-order harmonic-denominator mechanism extends strictly beyond the
one-half regime for even multipliers.  Let $u=1+x^2$, take even
$h\in\mathbb Z[x]$ with



$$
h\equiv1\pmod{u^2},\qquad h(0)=0,
 \qquad n=\operatorname{ord}_0h,\quad d=\deg h,
$$



and put $r=(h-1)/u$.  Then every odd prime in the one-third window has
exact reduced valuation



$$
\boxed{
 d/3<p\leq n\quad\Longrightarrow\quad
 v_p\!\left(\int_0^1r(x)\,dx\right)=-1.}               \tag{94.1}
$$



Indeed, below order $n$,
$r_{2j}=(-1)^{j+1}$ and $r_{2j+1}=0$.  Since $3p>d$, only the
integration denominators $p$ and $2p$ can contribute; their numerators
are respectively $\pm1$ and zero, the latter by global evenness.  If
$D(h)$ is the least common clearing of
$I_0=\int r$ and $I_1=\int xr$, then



$$
\prod_{d/3<p\leq n\atop p>2}p\mid D(h).                \tag{94.2}
$$



Under $0\leq h\leq1$ on $[0,1]$, shifted Markov gives



$$
D(h)\max(|I_0|,|I_1|)
 \geq {1\over16d^2}\prod_{d/3<p\leq n\atop p>2}p.      \tag{94.3}
$$



Thus $n\geq(1/3+\varepsilon)d$ forces exponential denominator-cleared
size.  The explicit positive family
$h_k=(2x^4-x^8)^k$, with $(n,d)=(4k,8k)$, satisfies



$$
\int_0^1h_k\sim{\sqrt\pi\over8\sqrt k},\qquad
 \log\!\left(D(h_k)\int_0^1h_k\right)
 \geq {4k\over3}+o(k).                                  \tag{94.4}
$$



For the full Robin channel the exact residue is
$2s_{p-1}+s_{2p-1}\pmod p$; evenness of $h$ alone does not kill the
second term.  A separate positive congruence-preserving polynomial of
degree/order ratio four proves that the region $d\geq3n$ is genuinely
populated.  Hence item 94 is a broad obstruction, not a theorem for every
nonlocal or cross-channel construction.

Frozen item-94 package:

~~~
df2657ebe8e241d6f14b8c8628ba5c085662301936efc869f69669818749bb49  sources/common_kernel_even_nonlocal_moment_denominator_barrier.md
82e1828ef3f4ed22ffe7d60abcb9fbe9e709c6bf75df0fbcecb793b67bc632e6  scripts/common_kernel_even_nonlocal_moment_denominator_certificate.py
c53c46ce84fb9ea035020d24fbc876bc96136a03327188108e4212c08f21a842  results/common_kernel_even_nonlocal_moment_denominator_certificate.json
bc6aae22ca67cb7e04678432e3befdd33b7072ab3cc67b1d656134fd7e0a1806  results/common_kernel_even_nonlocal_moment_denominator_hashes.sha256
~~~

A clean root replay took about $3.42$ seconds and reported $21{,}488$
KiB peak RSS.  The all-parameter valuation proof, endpoint Laplace limit,
positivity factorizations, JSON, syntax, dependency, and manifest audits pass.
Item 94 does not classify $e+\pi$.

## Centered-cosh checkpoint item 95: coupled parity and the terminal slope band

For the two actual parity blocks $V_0,V_1$ in the unbalanced lift, put



$$
{\cal E}_{n,t}=V_0^2+xV_1^2,\qquad D=n-1.
$$



Let $C_{n,t}$ be the full degree-$0,\ldots,D$ coefficient matrix of
any product spanning family and let $J_{n,t}$ retain only degrees
$2,\ldots,D$.  Cross-block relations and cancellations are handled
exactly by



$$
\boxed{
 \dim({\cal E}_{n,t}\cap\mathbb Q[x]_{\leq1})
 =\operatorname{rank}C_{n,t}-\operatorname{rank}J_{n,t},}
                                                               \tag{95.1}
$$



with


$$
\ker J_{n,t}/\ker C_{n,t}\simeq
{\cal E}_{n,t}\cap\mathbb Q[x]_{\leq1}
$$

.  Reversal turns $J$ into
the exact coupled high jet.

The resulting all-parameter terminal theorem is



$$
\boxed{
 n\geq5,\quad n-3\leq t\leq n-1
 \quad\Longrightarrow\quad
 {\cal E}_{n,t}\cap\mathbb Q[x]_{\leq1}=\{0\}.}        \tag{95.2}
$$



All parity edges are included.  In the only two-dimensional odd edge,
reversal gives the three jets $1,K,K^2$, whose leading determinant is
$k_1^3\ne0$; hence a nonzero product has degree at least
$2d_0-2=n-3\geq2$.

For equal parity blocks in the wider strict-slope range, the unresolved
determinants are reduced explicitly to



$$
\{y^j,y^jK,y^jK^2:0\leq j\leq2r-1\}                  \tag{95.3}
$$



of size $6r$, or to the $6r+3$ columns



$$
1,\ldots,y^{2r+1};\quad H,\ldots,y^{2r}H;\quad
 H^2,\ldots,y^{2r-1}H^2.                                \tag{95.4}
$$



Their all-parameter nonvanishing remains open.  Exact FLINT ranks find no
low survivor for all 248 pairs
$5\leq n\leq28$, $0\leq t<n$, $3t>n$, and find all tested leading
jets nonzero; these are finite diagnostics only.  Generic Schur clearing
still gives logarithmic maximal-minor height $O(n^3)$.

Frozen item-95 package:

~~~
3aea77c0901bcf1d1209ee57c18dec01cc2c15c37c454249a8bb45af9b91d52d  sources/centered_cosh_unbalanced_coupled_parity_obstruction.md
d517a9033881398e4cef117ef57f3e6e5601c8f3aabd1f68dd43cffc1304ecda  scripts/centered_cosh_unbalanced_coupled_parity_certificate.py
6bd9b5f1d9c2046e2847718b35140789c08581913710d080c710d062fd6ab0cc  results/centered_cosh_unbalanced_coupled_parity_certificate.json
985a4a111319321868b17e526f0ecf6e41896708a92fc1db2256402188b7580a  results/centered_cosh_unbalanced_coupled_parity_hashes.sha256
~~~

The root replay took about $6.63$ seconds at $38{,}968$ KiB peak RSS;
both audits, the exact ranks, source dependencies, syntax, JSON, and manifest
pass.  Item 95 closes the terminal band only and does not classify
$e+\pi$.

## Common-kernel checkpoint item 96: nonsymmetric two-moment cancellation

The evenness assumption in item 94 cannot be removed prime by prime, even
after using both defect moments and retaining positivity.  For arbitrary
$h$, with $r=(h-1)/(1+x^2)$, and every odd prime
$d/3<p<n$, the exact local criterion is



$$
\begin{aligned}
 \int_0^1r\in\mathbb Z_{(p)}
 &\iff 2r_{p-1}+r_{2p-1}\equiv0\pmod p,\\
 \int_0^1xr\in\mathbb Z_{(p)}
 &\iff r_{2p-2}\equiv0\pmod p.
\end{aligned}                                            \tag{96.1}
$$



The forced coefficients are $r_{p-1}=(-1)^{(p+1)/2}$ and
$r_{p-2}=0$, but the two coefficients near $2p$ are free enough to
cancel both residues.  An exact positive counterexample is



$$
h=(2x^4-x^8)^6
 \left(1-(1+x^2)^2x^3(1-x)^2\right)^2.                 \tag{96.2}
$$



It satisfies $0\leq h\leq1$,
$h\equiv1\pmod{(1+x^2)^2}$, $(n,d)=(24,66)$, and at the genuine
window prime $p=23$,



$$
r_{22}=1,\qquad r_{44}=3887=169\cdot23,
 \qquad r_{45}=-1520,                                   \tag{96.3}
$$



so $2r_{22}+r_{45}=-66\cdot23$ and $r_{44}=169\cdot23$.
Both exact reduced moment denominators are prime to 23.  Positivity follows
symbolically from factor bounds, not from sampling.

This refutes only universal survival of each individual window prime.  It
does not refute an exponential lower bound for the aggregate surviving
prime product, recovery by a third/full channel, or a theorem under extra
structure.  The ratio-four positive family has $d/3>n$, so its
one-third window is identically empty.

Frozen item-96 package:

~~~
d91d09a05d767e31ef968f72813191421803e766c20c0407c0c69f39152b80fb  sources/common_kernel_nonsymmetric_two_moment_residue_counterexample.md
ab2712dcad3901dc5b0352338f34975347dc4bc4136c97ea1d7e0f4585e64629  scripts/common_kernel_nonsymmetric_two_moment_residue_certificate.py
d6452400a3014be7d59abdbed03ff2bd66f26c68692fa94f57090959212f57df  results/common_kernel_nonsymmetric_two_moment_residue_certificate.json
14edc755bb18e6726f6e1e5f6006afcc76950e2d3206dd3d2b942e10ee471081  results/common_kernel_nonsymmetric_two_moment_residue_hashes.sha256
~~~

The root replay took about $3.54$ seconds at $20{,}728$ KiB peak RSS.
The general residue lemma, exact fractions, positivity identities, syntax,
JSON, dependencies, and manifest pass.  Item 96 prevents an invalid
generalization and does not classify $e+\pi$.

## Common-kernel checkpoint item 97: positive CRT cancellation of a full window

The aggregate version of the nonsymmetric two-moment claim also fails for a
substantial finite window.  Put



$$
a=2x^4-x^8,\quad m=115,\quad L=75,\quad w=x^L(1-x)^L,
$$





$$
\begin{aligned}
 c_0&=139574584508098815002244647712452355913710915,\\
 c_1&= 92665357687907045832657432294875741514399515,
\end{aligned}
$$



and



$$
h=a^m\bigl(1-(1+x^2)^2w(c_0+c_1x)\bigr).             \tag{97.1}
$$



Then $h\in\mathbb Z[x]$, $h\equiv1\pmod{(1+x^2)^2}$,
$h(0)=0$, $0\leq h\leq1$ on $[0,1]$, and
$(n,d)=(460,1075)$.  Every prime in the complete interval
$d/3<p<n$, namely



$$
\{359,367,373,379,383,389,397,401,409,
   419,421,431,433,439,443,449,457\},                  \tag{97.2}
$$



cancels from both reduced moment denominators.  Their product is



$$
237359812447644832129693355690076072498951997,        \tag{97.3}
$$



and is coprime to the exact common denominator of $I_0,I_1$.

The construction has an exact conditional CRT lemma.  With
$A_m=a^m$, $R_m=(A_m-1)/(1+x^2)$, and
$G_{m,L}=A_m(1+x^2)x^L(1-x)^L$, the two coefficients $c_0,c_1$
solve, modulo each target prime, the two equations forcing
$r_{2p-2}=0$ and $r_{2p-1}=-2r_{p-1}$.  Ordinary least nonnegative
CRT representatives preserve integrality.  Positivity follows from the exact
capacity inequality



$$
c_0+c_1<4^{74},\qquad
 (1+x^2)^2x^{75}(1-x)^{75}(c_0+c_1x)\leq1.             \tag{97.4}
$$



Frozen item-97 package:

~~~
271a0184572a5e203f56564c9db789410dc34eec18488c28f880d31bbfc015e2  sources/common_kernel_positive_crt_all_window_cancellation_barrier.md
b533da632f07a6887f225638b55ff67b1fd465fc09920f1da5ab5df4171b94ff  scripts/common_kernel_positive_crt_all_window_cancellation_certificate.py
32d4df4cba3eece31dd0d202f80db95495da3b02be0256155406bedea9be961b  results/common_kernel_positive_crt_all_window_cancellation_certificate.json
fd2a96672780209dcca4fd2ea4cf2d437fb491432667ed9fd32db0cc154f16b4  results/common_kernel_positive_crt_all_window_cancellation_hashes.sha256
~~~

A root replay took about $0.23$ seconds at $21{,}000$ KiB peak RSS.
An independent dictionary-polynomial reconstruction rechecked all 34 residues;
syntax, JSON, dependencies, and hashes pass.  Item 97 is a rigorous finite
aggregate barrier, not an asymptotic cancellation family and not a
classification of $e+\pi$.

## Common-kernel checkpoint item 98: asymptotic three-quarter cancellation

The finite CRT mechanism scales unconditionally.  Let



$$
B_m=x^{4m}(m+1-mx^4),\qquad
 w_m=x^{4L}(1-x^4)^L(1-x^2),
$$



where $L=\lfloor\lambda m\rfloor$ and



$$
\frac{2}{2+\log4}<\lambda<1.
$$



For every sufficiently large $m$, ordinary one-variable CRT supplies an
integer $0<c_m<P_m$ such that



$$
h_m=B_m\bigl(1-c_m(1+x^2)^2xw_m\bigr)                 \tag{98.1}
$$



is integral, congruent to one modulo $(1+x^2)^2$, has
$(n_m,d_m)=(4m,4m+8L+11)$, and satisfies $0\leq h_m\leq1$ on
$[0,1]$.  The target set is



$$
{cal P}_m=\{p:2m+2L<p<4m,\ p\nmid K_{m,L}\},
 \qquad K_{m,L}=2mL+6m+4L+5.                           \tag{98.2}
$$



The sparse identity



$$
B_m(1+x^2)w_m
 =x^{4(m+L)}(m+1-mx^4)(1-x^4)^{L+1}                   \tag{98.3}
$$



diagonalizes every local residue matrix.  If
$t=(p-1)/2-m-L$, its diagonal entry is



$$
g_p=(-1)^t\binom{L+1}{t}
 \frac{(m+1)(L+2)-t}{L+2-t},                           \tag{98.4}
$$



and $g_p\equiv0\pmod p$ exactly when $p\mid K_{m,L}$.  The excluded
log-mass is at most $\log K_{m,L}=O(\log m)$.  Hence



$$
\sum_{p\in{cal P}_m}\log p=2(1-\lambda)m+o(m),
$$



whereas the full natural window has mass
$(8/3)(1-\lambda)m+o(m)$.  Thus both moment denominators lose
asymptotically three quarters of the window mass.  The strict capacity
inequality is



$$
\lambda\log4>2(1-\lambda),
$$



which puts the least CRT representative below $4^{L-1}$ with exponential
room and proves positivity.

Frozen item-98 package:

~~~
211fa36d058cfedb242e8dc732cac2ce9bb354e81e241fa6799f6f063a5715f5  sources/common_kernel_positive_crt_asymptotic_three_quarter_cancellation.md
01795ba68c3a16760f78f1913ed17821155b49c0e9e4591b8239a2ebd0a4b690  scripts/common_kernel_positive_crt_asymptotic_three_quarter_certificate.py
f4411917f17e2ba40f593ead5da578cbaf2fee1b2ee3b658343e957c5d1f531a  results/common_kernel_positive_crt_asymptotic_three_quarter_certificate.json
e5e497408f8b6a1ad6c4fc28634e2c5e8805754e3c10bf52e700325033d2625c  results/common_kernel_positive_crt_asymptotic_three_quarter_hashes.sha256
~~~

The root replay took about $0.13$ seconds at $20{,}972$ KiB peak RSS.
An independent sparse-polynomial implementation reproduced every representative
residue; the all-parameter asymptotics are proved from the prime number theorem,
not extrapolated from that instance.  Item 98 is an asymptotic route barrier,
not a classification of $e+\pi$.

## Bessel checkpoint item 99: double-zero index-Hensel counterexample

The attractive finite pattern



$$
v_p(q_n)\leq1+\lceil\log_p n\rceil
$$



is false for the Bessel denominator recurrence
$q_0=q_1=1$, $q_n=(4n-2)q_{n-1}+q_{n-2}$.  The exact counterexample is



$$
\boxed{
 p=7,\quad
 n_*=464838342618219576262104570205987685961890202821,
 \quad v_7(q_{n_*})=59.}                                \tag{99.1}
$$



Here $7^{56}<n_*<7^{57}$, so the proposed upper bound is $58$.
For $f(n)=(-1)^nq_n$, let $A_j=\Delta^jf(0)$.  The exact formulas



$$
A_{j+2}=-4(j+2)A_{j+1}-(8j+6)A_j-4jA_{j-1},
$$





$$
A_j=(-1)^j j!\sum_{m=0}^{\lfloor j/2\rfloor}
 \frac{(-1)^m}{m!}\binom{2j-2m}{j}                     \tag{99.2}
$$



agree, and $j!/\lfloor j/2\rfloor!\mid A_j$.  Thus every term with
$j\geq869$ vanishes modulo $7^{60}$, making the Mahler evaluation
finite and rigorous.  It gives



$$
f(n_*)\equiv5\cdot7^{59}\pmod{7^{60}},\qquad
 q_{n_*}/7^{59}\equiv2\pmod7.                           \tag{99.3}
$$



The ordinary branch through the root $2\pmod7$ has consecutive zero lift
digits at positions $57,58$, followed by digit $6$ at position $59$.
This refutes the proposed prohibition on two consecutive zero digits.

The surviving sufficient reduction uses the terminal zero-run length
$L_{p,n}$: uniformly on the relevant block,



$$
v_p(q_n)\log p
 \leq\log(2N)+\log p+L_{p,n}\log p.                     \tag{99.4}
$$



A uniform $L_{p,n}=o(N)$ across ordinary and surviving singular paths would
still prove the required $V_N(C)=o(N\log N)$; fixed-$p$ constants do not.

Frozen item-99 package:

~~~
2e34ff5b30e658088d882568f83493c4c09582ccdbf921bb6337005b2c213abf  sources/bessel_padic_index_double_zero_counterexample.md
f0733a1493311401ceb6a0f59194012db20ee04ddf50203ecce601b4280eccf8  scripts/bessel_padic_index_double_zero_counterexample_certificate.py
c06353984f883dc02b441492fb5f414a8f0cd750378f86f4978bf8bde3db7a5d  results/bessel_padic_index_double_zero_counterexample_certificate.json
ee1b2591676f6721a1b133ffb8374c3e35de0a0f983ca930271603df6708f58a  results/bessel_padic_index_double_zero_counterexample_hashes.sha256
~~~

A byte-identical root replay took about $11.57$ seconds at $20{,}864$
KiB peak RSS.  A separate implementation recomputed the closed Mahler sum and
both nonzero terminal residues.  Item 99 closes only the sharp digit conjecture;
it does not refute the little-oh Bessel target or classify $e+\pi$.

## Common-kernel checkpoint item 100: asymptotically full-window cancellation

Shifted entropy padding strengthens item 98 from three quarters to the entire
one-third window up to logarithmic exceptional mass.  For every sufficiently
large integer $q$, set



$$
B_q=x^{20q}(5q+1-5qx^4),\qquad
 w_q=x^{12q}(1-x^4)^{4q}(1-x^2),                        \tag{100.1}
$$



and $K_q=40q^2+44q+5$.  For every prime



$$
\frac{48q+11}{3}<p<20q,qquad p\nmid K_q,
$$



the same sparse diagonal calculation gives a unit $g_p$.  A single least
nonnegative CRT integer $c_q$ defines



$$
h_q=B_q\bigl(1-c_q(1+x^2)^2xw_q\bigr),                \tag{100.2}
$$



with



$$
h_q\in\mathbb Z[x],\quad h_q\equiv1\pmod{(1+x^2)^2},
 \quad h_q(0)=0,\quad0\leq h_q\leq1,
$$



and exact order/degree $(n_q,d_q)=(20q,48q+11)$.

Writing $t=(p-1)/2-8q$, every actual window prime has
$2\leq t\leq2q-1$, and



$$
g_p=(-1)^t\binom{4q+1}{t}
 \frac{(5q+1)(4q+2)-t}{4q+2-t},
 \qquad g_p\equiv0\pmod p\iff p\mid K_q.               \tag{100.3}
$$



The padding maximum is exact:



$$
\max_{0\leq z\leq1}z^{3q}(1-z)^{4q}
 =\left(\frac37\right)^{3q}\left(\frac47\right)^{4q}. \tag{100.4}
$$



The entropy margin over the whole prime product is



$$
\Gamma=7\log7-3\log3-4\log4-4>0,                     \tag{100.5}
$$



so the CRT representative fits inside the positivity capacity with exponential
room.  If $D_q$ clears both moments, then



$$
\boxed{
 \gcd\!\left(D_q,\prod_{d_q/3<p<n_q}p\right)\mid K_q.} \tag{100.6}
$$



The canceled and total window log-masses are both $4q+o(q)$; the possible
uncanceled divisors of $K_q$ have mass only $O(\log q)$.  Thus the
canceled fraction tends to one.

Frozen item-100 package:

~~~
e8cbb912fd801e83d31917ccbe24ff40dc936509e45bd4751ef11b2c7a454215  sources/common_kernel_positive_crt_asymptotic_full_window_cancellation.md
7f22f68204fbd302bdf73d1e07c32e6f487a814ef4d28f3a7aed986c96fa1e29  scripts/common_kernel_positive_crt_asymptotic_full_window_certificate.py
1328ed4a8d8eaf42f36e11752a3449df9a0db31edbb9aca7a2bd3f1a5d872a39  results/common_kernel_positive_crt_asymptotic_full_window_certificate.json
0d4277f69ba4fc92e7b0ebc9222cceb9172994f03dadfabfd169ad7b23fff008  results/common_kernel_positive_crt_asymptotic_full_window_hashes.sha256
~~~

The root replay took about $0.038$ seconds at $20{,}740$ KiB peak RSS;
an independent dictionary-polynomial expansion reproduced every window residue
and the exact integer capacity inequality.  Item 100 completely defeats the
two-isolated-moment window-product lemma asymptotically, but does not control
the full correction channel or classify $e+\pi$.

## Bessel checkpoint item 101: an exact triple-zero lift

The ordinary $7$-adic index-root branch through $2$ has three consecutive
zero lift digits.  The exact least representative $n_3$, stored in full in
the source and certificate, has $987$ decimal digits and satisfies



$$
7^{1167}<n_3<7^{1168},\qquad
 v_7(q_{n_3})=1171,\qquad
 q_{n_3}/7^{1171}\equiv1\pmod7.                         \tag{101.1}
$$



Its decimal SHA-256 digest is

~~~
b99aaafbf4474e3956ff60ff74039eadd8df1e384894725c01481f5528ebc8f4
~~~

In the convention that digit $d_a$ lifts a root modulo $7^a$ to one
modulo $7^{a+1}$, the surrounding window is



$$
(d_{1165},\ldots,d_{1171})=(1,3,4,0,0,0,4).            \tag{101.2}
$$



Thus both proposed fixed additive bounds $+1$ and $+2$ beyond
$\lceil\log_p n\rceil$ are false.  For $f(n)=(-1)^nq_n$, the Mahler
divisibility



$$
\frac{j!}{\lfloor j/2\rfloor!}\mid\Delta^jf(0)
$$



makes every omitted term from $j=16437$ onward vanish modulo $7^{1172}$.
The resulting finite exact sum gives



$$
f(n_3)\equiv7^{1171}\pmod{7^{1172}},\qquad
 f(n_3+4\cdot7^{1171})\equiv0\pmod{7^{1172}}.           \tag{101.3}
$$



Frozen item-101 package:

~~~
3295664e80c0e3ee8a6b871fa73303de555548491b70a39077e7387a04dde2cf  sources/bessel_padic_index_triple_zero_counterexample.md
63be13d66517f6fdabed177a229626f215faa086356437fcc8520b336aae600d  scripts/bessel_padic_index_triple_zero_counterexample_certificate.py
c90fb481e9641c1c066280719a044675ed087acf868a891ade0bf4a0dfb09857  results/bessel_padic_index_triple_zero_counterexample_certificate.json
8088bcc99328176637a83dec7ce9139bc8bb02f394b96b323313954aaf0f6922  results/bessel_padic_index_triple_zero_counterexample_hashes.sha256
~~~

The frozen replay is byte-identical.  A second implementation independently
recomputed the base-seven digits and both Mahler residues.  This finite theorem
does not show that zero runs are unbounded: the surviving sufficient target is
still a uniform sublinear bound for terminal zero-run length.  Item 101 does
not classify $e+\pi$.

## Bessel checkpoint item 102: local zero-run methods are insufficient

There is an exact comparison family showing that the local properties so far
proved for the Bessel interpolation cannot by themselves bound terminal zero
runs.  For an odd prime $p$, choose $r$ with $2r+1\not\equiv0\pmod p$,
an arbitrary increasing sequence $N_1<N_2<\cdots$, and put



$$
\rho=r+\sum_{j\geq1}p^{N_j},\qquad
 F_\rho(x)=x(x+1)-\rho(\rho+1).
$$



This $\mathbb Z_p$-polynomial is analytic and $1$-Lipschitz, obeys the
reflection $F_\rho(-x-1)=F_\rho(x)$, and has a simple root at $\rho$.
For $M=p^a$, its exact lift-fiber law is



$$
F_\rho(x+tM)=F_\rho(x)+tM(2x+1)+t^2M^2.               \tag{102.1}
$$



At the integer prefix



$$
n_j=r+\sum_{i\leq j}p^{N_i}
$$



one has



$$
\boxed{v_p(F_\rho(n_j))=N_{j+1}},                     \tag{102.2}
$$



so the terminal zero run has the arbitrarily prescribed length
$N_{j+1}-N_j-1$.  Taking $N_{j+1}=N_jp^{N_j}$ even gives



$$
\frac{v_p(F_\rho(n_j))\log p}{n_j\log n_j}\longrightarrow1. \tag{102.3}
$$



Thus simplicity, reflection, periodicity, and exact affine Hensel lifting are
compatible with the entire forbidden main scale.  This does not construct a
Bessel counterexample: the comparison coefficient
$-\rho(\rho+1)$ is generally nonrational, and $F_\rho$ does not satisfy
the Bessel difference equation.  It proves that a successful Bessel argument
must add global rational-height or recurrence-specific information.

Frozen item-102 package:

~~~
4372ccae9160d501a1c72631c1b4ce43865d29e6d36d88b11b192a7f7626ef03  sources/bessel_padic_local_zero_run_no_go.md
a3de0204026e19b10da91039d0347341d15367c33bd5c7e07b78c9c808c788a7  scripts/bessel_padic_local_zero_run_no_go_certificate.py
bec3c0854ba91906ca12e6827388b5f626d4e088b758bf7ba95c1629e94722de  results/bessel_padic_local_zero_run_no_go_certificate.json
2673e830c57748ec85d37d22ada1279e1d932cf11ca98b7790cd906ccda50e13  results/bessel_padic_local_zero_run_no_go_hashes.sha256
~~~

The all-parameter proof is the displayed factorization and translation
identity; the deterministic finite replay checks four regression examples.
Item 102 is a method barrier, not a classification of $e+\pi$.

## Common-kernel checkpoint item 103: finite positive CRT channels also cancel a fixed full correction

The asymptotically complete two-moment cancellation from item 100 persists
after adjoining the full rational output generated by any *fixed*
$K\in\mathbb Z[x]$.  With



$$
u=1+x^2,\qquad {\cal T}P=(1-x)P'-xP,
 \qquad {\cal T}K=uG_0+\alpha+\beta x,
$$



there are explicit constants $C_K\geq0$ and $\Delta_K\geq1$ such that,
for every sufficiently large $q$, a nonnegative finite-channel CRT
construction gives an integer polynomial $h_q$ with



$$
h_q\equiv1\pmod{u^2},\quad h_q(0)=0,\quad
 0\leq h_q(x)\leq1\ (0\leq x\leq1),
$$





$$
\operatorname{ord}_0h_q=20q,\qquad \deg h_q=48q+O_K(1).
$$



If



$$
r_q=(h_q-1)/u,\qquad
 S_q=\{{\cal T}(h_qK)-{\cal T}K\}/u
$$



and $D_q$ clears $\int_0^1r_q$, $\int_0^1xr_q$, and
$\int_0^1S_q$, then



$$
\boxed{
 \gcd\!\left(D_q,
 \prod_{(48q+C_K)/3<p<20q}p\right)
 \mid \Delta_K(40q^2+44q+5).}                         \tag{103.1}
$$



The window has Chebyshev mass $4q+o(q)$, while the possible surviving
mass on the right of (103.1) is only $O_K(\log q)$.

The new exact response calculation uses



$$
H_K=(1+x)(1-x^2)^2K
 =H_0(x^4)+xH_1(x^4)+x^2H_2(x^4)+x^3H_3(x^4).
$$



For $h_q=B_q(1-u^2w_qC_q)$, with $C_q$ supported in residue classes
$1,2,3\pmod4$, the variation of the high full-output coefficient at
$O=2p-1$ is exactly



$$
\delta s_O\equiv-[x^O]V_qH_KC_q\pmod p.              \tag{103.2}
$$



Class one controls the remaining moment equation, while classes two and
three supply independent full-output responses.  A finite coefficient-block
lemma proves the needed response rank uniformly outside the fixed factor
$\Delta_K$.  When only the class-zero response remains, either finitely
many class-one shifts have rank two, or the apparently proportional case is
classified exactly as



$$
K=x(1-x)(1+x^2)^3R(x^4),                              \tag{103.3}
$$



for which $\alpha=\beta=0$ and the full equation is automatic.  The
positivity capacity retains the strict entropy margin



$$
7\log7-3\log3-4\log4-4>0.
$$



The exceptional linear direction $K=1-x$ is handled by a deliberately
non-even class-three channel.  This does not contradict the earlier
linear-$K$ identity: that formula had the standing hypothesis that $h$
was even, and the exact operator calculation records the odd terms which it
therefore omitted.

Frozen item-103 package:

~~~
1071a65d0e799dd27754c6a117c573eee7170d7b430593c17da15fae0b1bc104  sources/common_kernel_positive_crt_full_correction_cancellation.md
64fd00d3c07ed7685362ee0df7c3872be7815c03360b9b6e67ae461d41644207  scripts/common_kernel_positive_crt_full_correction_certificate.py
20b7709fe330087fc44716c010950500d35ee5686c5787e281d09e2ff4bbbd53  results/common_kernel_positive_crt_full_correction_certificate.json
227318fce04df7c79dafb4a570ede3f0767c1c75b084aaaefe746b55a7c1a99a  results/common_kernel_positive_crt_full_correction_hashes.sha256
~~~

The root replay was byte-stable and the manifest passed before and after it.
An independent symbolic implementation verified the Stein response and the
structural exceptional family through degree 16.  Item 103 is a rigorous
barrier only for fixed $K$; growing-degree corrections and primitive content
remain outside its scope, and it does not classify $e+\pi$.

## Centered-secant checkpoint item 104: condensation and contiguous transfer do not close the equal jets

The two remaining equal-parity Hermite--Padé determinants in the unbalanced
centered-cosh route now have exact Toeplitz, condensation, and contiguous
transfer descriptions.  Put



$$
F(x)=\frac1{2\cosh\sqrt x},
$$



and, for a binary polynomial pair $(D,N)$, define the equal and flagged
quadratic modules



$$
{\cal E}_m(D,N)=D^2{\cal P}_{m-1}+DN{\cal P}_{m-1}+N^2{\cal P}_{m-1},
$$





$$
{\cal F}_m(D,N)=D^2{\cal P}_{m+1}+DN{\cal P}_{m}+N^2{\cal P}_{m-1}.
$$



For the canonical adjacent Padé pair $(X_M,Y_M)$, all-parameter contiguous
identities give



$$
\binom{X_M}{Y_M}=
 \begin{pmatrix}a_M&1\\a_My&b_M+y\end{pmatrix}
 \binom{X_{M-1}}{Y_{M-1}},
 \qquad a_Mb_M\ne0.                                    \tag{104.1}
$$



The symmetric square of this matrix has polynomial degree two, so



$$
{\cal E}_{m-2}(X_{M-1},Y_{M-1})
 \subseteq {\cal E}_m(X_M,Y_M)
 \subseteq {\cal E}_{m+2}(X_{M-1},Y_{M-1}).             \tag{104.2}
$$



In the admissible secant range, the first inclusion has codimension exactly
six.  Thus the constant nonzero scalar-transfer determinant does not make the
quadratic multiplier window invariant.

There is also an exact parity coupling.  The shear identity



$$
{\cal F}_m(D,N-yD)={\cal F}_m(D,N)
$$



canonically reduces the other parity, and



$$
{\cal E}_m(X_M,Y_M)\subseteq
 {\cal F}_m(X_M,Y_{M-1})                                \tag{104.3}
$$



has codimension three.  An explicit basis completion has determinant
$\pm b_M^{3m}$, so the parities are coupled but retain a new
three-dimensional boundary minor.

Writing $K=\sum_{n\ge1}k_ny^n$ and
$K^2=\sum_{n\ge2}\ell_ny^n$, define the two-block Toeplitz minors



$$
D_{p,q}^{(s)}=\det\left(
 [k_{s+i-j}]\ \middle|\ [\ell_{s+i-j}]
 \right).
$$



The equal determinant is $D_{m,m}^{(m)}$, and Desnanot--Jacobi gives



$$
D_{p,q}^{(s)}D_{p-1,q-1}^{(s+1)}
 =D_{p-1,q}^{(s+1)}D_{p,q-1}^{(s)}
 -D_{p,q-1}^{(s+1)}D_{p-1,q}^{(s)}.                    \tag{104.4}
$$



On the equal diagonal, (104.4) introduces the wrong shift and four
off-diagonal minors; their signs are not fixed even on genuine secant data.
It therefore does not yield a scalar positive recurrence.

A sharp generic counterexample rules out repairing this with positive-node or
ordinary-resultant arguments alone.  For



$$
K_t(y)=y\left(\frac1{1-y}+\frac1{1-2y}+\frac{t}{1-3y}\right),
$$



the first boundary determinant is



$$
\Delta_2(K_t)=(4t-1)(t^3-25t^2-13t+1).                \tag{104.5}
$$



At $t=1/4$, it vanishes despite three positive simple nodes, positive
weights, a coprime numerator and denominator, and resultant $-4096$.

The exact modular scan certifies all 7,081 admissible special secant
determinants through $M=120$ as nonzero modulo $2^{61}-1$, with stream
digest

~~~
7b9c798b64ad0e436118965f8fe6d53ee6f243149010160c23b7b155b94d05c9
~~~

This is finite evidence only.

Frozen item-104 package:

~~~
4304030a5efa878aea3751bffb15f957a6dcec0b39e8ea24c80b3e7254812504  sources/centered_cosh_equal_jet_condensation_barrier.md
dcecfa5bcf000028eb994973b4a98618ac66ea50bbfd13e68e995c6bbfb8bbee  scripts/centered_cosh_equal_jet_condensation_barrier_certificate.py
6d4f4231ed0b4623289ede62bcea47b8ace626960b375f0727cc3c22dd280952  results/centered_cosh_equal_jet_condensation_barrier_certificate.json
c2e38c053485920cb7fb35d75d49fe9d5752eb36708b1138dbf8c0d786fac7b0  results/centered_cosh_equal_jet_condensation_barrier_hashes.sha256
~~~

The root replay reproduced the frozen JSON, and an independent symbolic
implementation verified (104.4), (104.5), the displayed rational identity,
and the resultant.  Item 104 isolates the special boundary identity still
needed; it proves neither all-parameter secant nonvanishing nor a
classification of $e+\pi$.

## Bessel checkpoint item 106: the central singular zero-run dichotomy

For an odd prime $p$, let $f_p$ denote the locally analytic canonical
interpolation of $f_p(n)=(-1)^nq_n$, and put



$$
c=-\frac12,\qquad n_a=\frac{p^a-1}{2}.
$$



The exact reflection $f_p(-x-1)=f_p(x)$ makes the central expansion even.
There are exactly two possibilities:



$$
f_p(c)\ne0
 \quad\Longrightarrow\quad
 v_p(q_{n_a})=v_p(f_p(c))\quad(a\gg1),                 \tag{106.1}
$$



whereas, if $f_p(c)=0$, local analytic factorization gives



$$
f_p(c+y)=y^\mu U(y),\qquad \mu\ge2\text{ even},
 \quad U(0)\ne0,
$$



and hence



$$
\boxed{v_p(q_{n_a})=\mu a+h\quad(a\gg1)},
 \qquad h=v_p(U(0)).                                  \tag{106.2}
$$



Because $n_a$ has exactly $a$ base-$p$ digits, all equal to
$(p-1)/2$, the second alternative creates $(\mu-1)a+h+O(1)$
terminal zero lift digits.  The proof uses only the already established
order-one local analyticity for odd $p$, reflection, and nonvanishing of
the positive integer values $q_n$ to exclude an identically zero local
restriction.

This is a conditional dichotomy: it does not prove $f_p(-1/2)=0$ for any
prime.  The first central residue, at $p=79$, is already known to die at
the first lift.  Even a fixed-prime singular branch would contribute only
$O(\log n_a)$ to $v_p(q_{n_a})\log p$, far below the global
$n_a\log n_a$ scale.

Frozen item-106 package:

~~~
f61c7e3005ee08d218bdc4150c0e34e9dcecc85119b74901f687aff9459d40e8  sources/bessel_padic_central_singular_zero_run_dichotomy.md
e36a44346586129d07691ccbf9a8e6a8f2247caf2b5bae94bac2314c371cccf4  scripts/bessel_padic_central_singular_zero_run_dichotomy_certificate.py
ee5417445c5bac26e8ffd710d36b8c1024dda1ebaa93a926496143eae681edcd  results/bessel_padic_central_singular_zero_run_dichotomy_certificate.json
7110154f392dd435ba554a6ec2f4239cebc766bc1eb933e01604bb0f81028e46  results/bessel_padic_central_singular_zero_run_dichotomy_hashes.sha256
~~~

The manifest and byte-for-byte replay pass.  Item 106 rules out a naive
universal one-digit-depth estimate without excluding central multiple zeros;
it supplies neither that exclusion nor a classification of $e+\pi$.

## Common-kernel checkpoint item 107: growing corrections cancel the complete prime window

Put $u=1+x^2$ and ${\cal T}P=(1-x)P'-xP$.  For every sufficiently
large $q$, and simultaneously for every nonzero
$K_q\in\mathbb Z[x]$ with $k_q=\deg K_q\le12q-10$, there is an
integral polynomial $h_q$ satisfying



$$
h_q\equiv1\pmod {u^2},\qquad h_q(0)=0,\qquad
 0\le h_q\le1\text{ on }[0,1],
$$





$$
\operatorname {ord}_0h_q=20q,qquad \deg h_q=48q+13. \tag{107.1}
$$



There is no restriction on coefficient height, content, or sparsity.  With



$$
r_q=\frac{h_q-1}{u},\qquad
 S_q=\frac{{\cal T}(h_qK_q)-{\cal T}K_q}{u},
$$



and $D_q$ the common clearing denominator of
$\int_0^1r_q$, $\int_0^1xr_q$, and $\int_0^1S_q$, one has



$$
\boxed{\gcd\!\left(D_q,
 \prod_{(48q+k_q+13)/3<p<20q}p\right)=1.}              \tag{107.2}
$$



This covers the complete potentially nonempty range: the displayed window is
already empty for $k_q\ge12q-13$.  The construction uses



$$
E=\left\lfloor\frac{k_q+5}{4}\right\rfloor+1,
 \quad A=3q-E,
$$



a degree-adapted positive padding, and all class-
$1,2,3\pmod4$ channels through level $E$.  A self-contained consecutive
Pascal-block determinant proves the needed finite-field rank.  Each window
prime activates at most two channels.  CRT representatives therefore have
coefficient sum at most $(2m_q+1)P_q$; a PNT entropy estimate for
$A/q\not\to0$, and parity plus the Montgomery--Vaughan
Brun--Titchmarsh inequality at the endpoint, fit them uniformly inside the
positive padding.

The factorial-height native Taylor--Robin correction



$$
K_N=I_N-\frac{M_N}{2}(1-x)
$$



is included with no height restriction.  If
$N-1<(48q+14)/3$, its target-zero integral coordinate is also free of
every prime in the complete window, while the localized polynomial has
constant coefficient one and hence primitive content one.  Thus neither
factorial coefficient height nor primitive content resurrects this proposed
denominator obstruction.  Sign and decay of the corrected Taylor residual
remain separate and unresolved.

Frozen item-107 package:

~~~
d1cd0012c8457ced0f064f23a8bf3256e91ff26730b8eaf5bcd7d984836f6ca7  sources/common_kernel_growing_correction_full_window_cancellation.md
8509d260b7d3ceaa879d88035a6b54802a08514dafe587be01694cb6d9c544f1  scripts/common_kernel_growing_correction_full_window_certificate.py
43e0146200996bcbc67fee8d47598abb6da10a6c32051f021afdbead43fb1f30  results/common_kernel_growing_correction_full_window_certificate.json
ef4c51baa0a9a2660be5e1360682f4bcb522354e1af8a6c87c6d3b9bfa057fc6  results/common_kernel_growing_correction_full_window_hashes.sha256
~~~

The root replay reproduced the frozen JSON in 1.4 seconds at 22,488 KiB peak
RSS.  An independent 450-case exact audit verified the Pascal determinant,
and the padding identity was checked symbolically.  Item 107 eliminates the
full-window denominator mechanism; it does not classify $e+\pi$.

## Bessel checkpoint item 108: finite shift--first-jet product formulas repackage the root factor

Every polynomial expression with coefficients in $\mathbb Z[x]$, built
from finitely many shifts $f_p(x+j)$ and first parameter jets
$f_p'(x+j)$, reduces integrally to



$$
\overline E(x,F,G,X,Y)\in\mathbb Z[x,F,G,X,Y],
$$



where $F=f_p(x)$, $G=f_p(x+1)$, $X=f_p'(x)$, and
$Y=f_p'(x+1)$.  This includes polynomial combinations of finite linear
forms, Wronskians, and determinants.  No division is used in the reduction.

If order $s$ at a root of $F$ is forced formally using only the Bessel
recurrence, its derivative, and $F=0$, then exactly



$$
\overline E=F^s\overline C,
 \qquad \overline C\in\mathbb Z[x,F,G,X,Y].             \tag{108.1}
$$



At an integer center $n$, substitute



$$
F=(-1)^nq_n,\quad G=(-1)^{n+1}q_{n+1},
$$





$$
X=(-1)^{n+1}(p_nK-b_n),\quad
 Y=(-1)^{n+2}(p_{n+1}K-b_{n+1}).                       \tag{108.2}
$$



The resulting $\Psi_n(K)$ lies in $\mathbb Z[K]$, and (108.1) gives
coefficientwise divisibility by $q_n^s$.  In particular, if the
indeterminate $K$ cancels and a single prime-independent integer $I_n$
remains, then



$$
\boxed{q_n^s\mid I_n},\qquad
 I_n\ne0\Longrightarrow
 \log|I_n|\ge s\log q_n=s n\log n+O(sn).               \tag{108.3}
$$



Thus an ordinary rational product formula over varying primes cannot profit
from a root order manufactured inside this formal algebra: the auxiliary has
already absorbed the complete $q_n^s$, and dividing it out removes exactly
that order.  If $K$ does not cancel, the local values retain the distinct
Euler factorial constants ${\cal K}_p$, so a product formula would require a
new global arithmetic relation for those constants.

The theorem is deliberately scoped.  It does not cover special smallness at
the actual root not forced by the recurrence, new integral transforms,
separately controlled higher or infinite jets, or a new arithmetic relation
among the ${\cal K}_p$.

Frozen item-108 package:

~~~
90f69f0589392c84c4205ac2b95b5375a86e212ae7e33490708186d9a6aef45a  sources/bessel_aggregate_shift_jet_product_formula_no_go.md
8b7f1368de6a442a95cae1bc1c3d4762c43317af81c3d7a478e33f2921e45c7c  scripts/bessel_aggregate_shift_jet_product_formula_no_go_certificate.py
c94bf05c654c1fa272b80d9ebddedc7ed2bb70d88c2be044a774fdb34a20fe52  results/bessel_aggregate_shift_jet_product_formula_no_go_certificate.json
11ee42a3940770707892dba303e502b8f4e9000d02f1db39767e9e41b82bf617  results/bessel_aggregate_shift_jet_product_formula_no_go_hashes.sha256
~~~

The manifest and byte-for-byte replay pass.  An independent audit checked 425
positive and negative shift evaluations and 76 unrelated coefficientwise
specializations.  Item 108 excludes this finite formal product-formula
shortcut; it does not bound $v_p(q_n)$ or classify $e+\pi$.

## Secant checkpoint item 109: the actual equal-jet condensation quotient changes sign

Let



$$
F(x)=\frac1{2\cosh\sqrt x},
$$



let $Q_{L,D}(0)=1$ be its normal Padé denominator of type $[L/D]$,
and put



$$
X_M=\widehat Q_{M,M},\qquad
 Y_M=y\widehat Q_{M+1,M}.
$$



For the equal quadratic-jet determinant



$$
\Theta_m(D,N)=
 \det [y^i]\{y^jD^2,y^jDN,y^jN^2:0\le j<m\}_{0\le i<3m},
$$



exact integer reconstruction gives



$$
\boxed{
 \begin{array}{c|rrrr}
 M&6&7&14&15\\ \hline
 \operatorname {sgn}\Theta_6(X_M,Y_M)&+&-&-&+
 \end{array}.}                                          \tag{109.1}
$$



The four corresponding lower determinants
$\Theta_4(X_{M-1},Y_{M-1})$ are all positive.  Consequently the canonical
six-dimensional condensation quotient



$$
\frac{\Theta_6(X_M,Y_M)}{\Theta_4(X_{M-1},Y_{M-1})}
$$



has the same sign sequence $+,-,-,+$.  Independent primitive integer
clearing preserves these signs because



$$
\Theta_m(uD,vN)=u^{3m}v^{3m}\Theta_m(D,N)
 \qquad(u,v>0).
$$



These are witnesses from the actual centered-secant kernel, not a generic
positive-node counterexample.  They exclude a missing condensation factor
that is uniformly a positive resultant, positive Gram determinant, or
nonempty Cauchy--Binet sum of nonnegative terms under the fixed normalization.
They likewise exclude using these determinants themselves as fixed-sign
normalizing minors of a sign-regular multiple-orthogonality system.  They do
not exclude a genuinely sign-changing prefactor and do not prove or disprove
all-parameter nonvanishing.

Frozen item-109 package:

~~~
45bfb6497840dc9f9e0a997091c56d104d66157a992c57f598c31bd1001da218  sources/centered_cosh_equal_jet_actual_sign_barrier.md
5c5b94902e124fa52fdbd9e5d7141a3355313091aeb4828e03375f63dce5c701  scripts/centered_cosh_equal_jet_actual_sign_barrier_certificate.py
179d8366d87d48b9cd25761f1be71cbdc027b4f22fb0ad6dd7cb25b07c6cbd79  results/centered_cosh_equal_jet_actual_sign_barrier_certificate.json
dda7ad5eb73c802a0688d4cddea9a294ff943c29575ebc3f8a43f44d765148c0  results/centered_cosh_equal_jet_actual_sign_barrier_hashes.sha256
~~~

The frozen replay takes 0.08 seconds and peaks at 33,412 KiB RSS.  A separate
SymPy reconstruction reproduced the full signed determinant hashes for the
first positive/negative pair and both positive lower minors.  Item 109 closes
the fixed-positive-factor route, not the secant nonvanishing problem and not
the classification of $e+\pi$.

## Bessel checkpoint item 110: the large-prime unit-cancellation frontier

For the Bessel denominator sequence, the elementary size estimate now gives
the uniform bound



$$
\boxed{p>2n\quad\Longrightarrow\quad v_p(q_n)\le n-1.} \tag{110.1}
$$



Indeed,



$$
q_n<4^{n-1}n!<(2n+1)^n\le p^n.
$$



The estimate remains linear and therefore does not give the required
$o(n)$ exponent when $p\asymp n$.  In this range every summand in the
terminating factorial expression for $q_n$, and every nonzero coefficient
in the stated factorial normalization of its Padé denominator, is a
$p$-adic unit.  The valuation is pure cancellation.  The Padé Wronskian
only identifies it with the distance from $1$ to a simple argument root;
simplicity itself supplies no distance bound.

At the central boundary $p=2m+1$, define



$$
c_j=\frac{(1/2)_j^2}{j!},\qquad
 S_{m,\ell}=\sum_{j=\ell}^m c_j
 e_\ell\!\left(1,\frac1{3^2},\ldots,\frac1{(2j-1)^2}\right).
$$



Every denominator is a $p$-unit, and the complete all-power identity is



$$
\boxed{(-1)^m q_m=\sum_{\ell=0}^m(-p^2)^\ell S_{m,\ell}.}       \tag{110.2}
$$



Thus, for every $A\ge1$,



$$
v_p(q_m)\ge A
 \iff
 \sum_{\ell=0}^{\min\{m,\lfloor(A-1)/2\rfloor\}}
 (-p^2)^\ell S_{m,\ell}\equiv0\pmod {p^A}.             \tag{110.3}
$$



Each additional pair of powers introduces a new symmetric harmonic layer.
Reflection forces the first central index slope to vanish but decides none of
these higher congruences.  The wider range $n/2<p$ is not squarefree:



$$
q_8=13^2\cdot1846921.
$$



Frozen item-110 package:

~~~
baa384012e6f56f3437de42eb7614e0475763a883529fbfda97120497c97b11d  sources/bessel_large_prime_unit_cancellation_frontier.md
f7044fb57a01c7ea1198441833ce10d5e1c0c8613d72a3463da745ce50f0d29c  scripts/bessel_large_prime_unit_cancellation_frontier_certificate.py
58dda46677fc6c1fee1c30e2d865f055a9a3c94af9c74fac88845ea55fa81005  results/bessel_large_prime_unit_cancellation_frontier_certificate.json
e1c425fea9ab46f11686b52126ea76dcf70720704d949cec9d070f0bb2d93291  results/bessel_large_prime_unit_cancellation_frontier_hashes.sha256
~~~

The manifest and byte-identical replay pass.  An independent exact expansion
at $p=47,59,79$ reproduced every coefficient sign, denominator-unit
property, and central valuation.  Item 110 isolates cancellation rather than
bounding it at little-oh scale; it does not classify $e+\pi$.

## Common-kernel checkpoint item 111: sign control forces factorial-quarter-root degree

For the native Taylor--Robin correction



$$
K_N(x)=I_N-\frac{M_N}{2}(1-x),\qquad
 (1-i)^N=R_N+iI_N,\quad M_N=N!-R_N,
$$



let $h\in\mathbb Z[x]$ satisfy



$$
h\equiv1\pmod{(1+x^2)^2},\qquad h(0)=0,qquad
 0\le h\le1\text{ on }[0,1],
$$



and put $F_{N,h}=(1-x)^N+{\cal T}(hK_N)$.  If this residual is
one-signed, it is necessarily nonnegative.  The classes
$N\equiv5,6,7\pmod8$ are impossible, and every remaining candidate of
degree $d=\deg h$ obeys



$$
\boxed{d^4\ge\frac{M_N(N+1)}{54e}.}                   \tag{111.1}
$$



If $I_N<0$, there is also



$$
d^2\ge\frac{(-I_N)(N+1)}{8e}.
$$



Thus



$$
\log d\ge\frac14N\log N-\frac14N+O(\log N),           \tag{111.2}
$$



excluding every $\exp(o(N\log N))$-degree sign-controlled localizer.
The proof writes $H(t)=h(1-t)$, $a=-I_N$, $b=M_N/2$, and uses the
exact integrating factor



$$
\mu(t)=t(a+bt)e^{-t},\qquad
 (\mu H)'=e^{-t}\{F_{N,h}(1-t)-t^N\}.                  \tag{111.3}
$$



The resulting endpoint envelope, combined with Markov's inequality at
$t=1/(3d^2)$, gives (111.1).

Analytically, every such positive residual is already small at the exact
scale



$$
\boxed{\frac1{N+1}\le L_{N,h}\le\frac{5e}{N+1}.}       \tag{111.4}
$$



If



$$
L_{N,h}=N!(e+\pi)+\frac{c_{N,h}}{D_{N,h}},\qquad
 g_{N,h}=\gcd(N!,c_{N,h}),
$$



then primitive decay is equivalent to $D_{N,h}/g_{N,h}=o(N)$.  More
sharply, the reduced rational approximant



$$
q_{N,h}=\frac{N!D_{N,h}}{g_{N,h}},\qquad
 p_{N,h}=-\frac{c_{N,h}}{g_{N,h}}
$$



satisfies



$$
\frac1{(N+1)N!}
 \le\left|(e+\pi)-\frac{p_{N,h}}{q_{N,h}}\right|
 \le\frac{5e}{(N+1)N!}.                                \tag{111.5}
$$



Therefore, if some fixed $0<\delta<1/2$ and infinitely many
sign-controlled candidates satisfied



$$
q_{N,h}\le(N!)^{1/2-\delta}
 \quad\Longleftrightarrow\quad
 \frac{g_{N,h}}{D_{N,h}}\ge(N!)^{1/2+\delta},           \tag{111.6}
$$



then rational separation and Roth's theorem would prove that $e+\pi$ is
transcendental.  Neither existence of a sign-controlled $h$ nor the content
threshold (111.6) is proved.

Frozen item-111 package:

~~~
7a06684887367ce114e0c613e58c5dc1db688678099b0d3ed02b35c9c4b789e2  sources/common_kernel_native_sign_endpoint_degree_barrier.md
16f125838a585724b1e312b8bb6d0f8a7808c24883052c4773e33851b4438675  scripts/common_kernel_native_sign_endpoint_degree_certificate.py
4a9604b3f3adb787b66ce9733dc7de91c74226380734a42bc2e6fa687af15384  results/common_kernel_native_sign_endpoint_degree_certificate.json
400b4e5ae612683394a657c69f6aee4e1e2369b0d518f8c6027d51aa26c3efc3  results/common_kernel_native_sign_endpoint_degree_hashes.sha256
~~~

The manifest and deterministic replay pass at 71,260 KiB peak RSS.  The
integrating-factor identity, constants, primitive normalization, and Roth
exponent were independently checked line by line.  Item 111 turns the live
common-kernel route into the explicit construction/content target (111.6); it
does not itself classify $e+\pi$.

## Root-of-unity checkpoint item 112: tangent survivor has an exponential floor

Let $\tau_r$ be the positive tangent numbers and reduce



$$
\frac{8r(2r+1)\tau_r}{\tau_{r+1}}=\frac{P_r}{Q_r}.
$$



The exact odd-zeta identity



$$
\boxed{\frac{P_r}{Q_r}
 =\pi^2\frac{(1-2^{-2r})\zeta(2r)}
 {(1-2^{-2r-2})\zeta(2r+2)}}                         \tag{112.1}
$$



shows that these reduced fractions decrease strictly to $\pi^2$, with



$$
0<\frac{P_r}{Q_r}-\pi^2<\frac{5\pi^2}{2}\,9^{-r},
 \qquad
 \frac{P_r}{Q_r}-\pi^2
 =\frac{8\pi^2}{9}\,9^{-r}
  \left(1+O((9/25)^r)\right).                           \tag{112.2}
$$



Zudilin's proved bound
$\mu(\pi^2)=\mu(\zeta(2))\le5.09541178\ldots$ therefore gives



$$
\boxed{\liminf_{r\to\infty}\frac{\log Q_r}{r}
 \ge \frac{\log9}{5.095412}
 =0.4312162740\ldots.}                                  \tag{112.3}
$$



Thus the proposed $D=2$ activation condition $\log Q_r=o(r)$ is
unconditionally impossible, even along a subsequence.  Independently of an
irrationality measure, the adjacent determinant



$$
D_r=P_rQ_{r+1}-P_{r+1}Q_r
$$



is a positive integer with $v_2(D_r)=1$, and hence



$$
\boxed{Q_rQ_{r+1}>\frac4{5\pi^2}9^r.}                 \tag{112.4}
$$



Exact irregular pairs
$\gcd(\tau_{45},\tau_{46})=2^{88}\cdot587$ and
$\gcd(\tau_{168},\tau_{169})=2^{331}\cdot491$, together with their
Kummer progressions, also disprove a universal odd-coprimality shortcut.
The result is exponential rather than factorial scale, so it does not settle
the broader tangent-gcd problem or classify $e+\pi$.

Frozen item-112 package:

~~~
8dc9acde0025c4038b1b7e486ee327b6f077dae737e828c111ec066e7fcf0439  sources/root_unity_tangent_survivor_exponential_no_go.md
59dbabc81c1e784ade8115a1cec509a9fb4a5eba37909237d2854e1384db19b2  scripts/root_unity_tangent_survivor_exponential_no_go_certificate.py
1e4e1b379087e37938918802a5040ab54841540b158acff537f64ca6ed594378  results/root_unity_tangent_survivor_exponential_no_go_certificate.json
71e0b42a14b2bbcc3dbfc104824048a51f75a1c9c97296da6f2c7c33acbd2e33  results/root_unity_tangent_survivor_exponential_no_go_hashes.sha256
~~~

The source was audited line by line, including the irrationality-measure
transfer, odd-zeta tail, exact two-part, and Kummer conditions.  The primary
published constant was checked, and the byte-identical replay passes in under
one second at 36,976 KiB peak RSS with no control bytes.

## Common-kernel checkpoint item 113: high-origin-order content obstruction

Retain the native sign-controlled setup of item 111 and write



$$
d=\deg h,\qquad r=\operatorname {ord}_0h,\qquad
 L_{N,h}=N!(e+\pi)+\frac{c_{N,h}}{D_{N,h}},\qquad
 g_{N,h}=\gcd(N!,c_{N,h}).
$$



The exact quotient polynomial



$$
S_{N,h}
 =\frac{{\cal T}(hK_N)-{\cal T}K_N}{1+x^2}\in\mathbb Z[x]
$$



has degree $d$.  For every odd prime



$$
\max\!\left\{N,\frac{d+1}{2}\right\}<p<r,\qquad p\nmid M_N,
$$



its forced low coefficient is



$$
[x^{p-1}]S_{N,h}=\pm M_N.
$$



Because $2p>d+1$, this is the unique monomial integral whose denominator
is divisible by $p$.  The base coordinate has denominator supported below
$N$, so the prime survives the complete reduced output to exact exponent
one:



$$
\boxed{
 \prod_{\substack{\max\{N,(d+1)/2\}<p<r\\p\nmid M_N}}p
 \ \bigg|\ D_{N,h}.}                                    \tag{113.1}
$$



If $r\ge(1/2+\eta)d$ for a fixed $0<\eta<1/2$, sign control and the
item-111 degree bound give
$\log N!,\log M_N,N=o(d)$.  The prime number theorem applied to
(113.1) therefore yields



$$
\boxed{\log D_{N,h}\ge(\eta-o(1))d,\qquad
 \log\frac{g_{N,h}}{D_{N,h}}\le-(\eta-o(1))d.}          \tag{113.2}
$$



Thus the Roth content target
$g_{N,h}/D_{N,h}\ge(N!)^{1/2+\delta}$ is impossible throughout this
high-origin-order regime.  In particular, for
$h_m=x^{4m}(m+1-mx^4)$, both exponents sharpen in magnitude to
$(2-o(1))m$.  The $20q/(48q+13)\to5/12$ nonlocal CRT family lies
strictly below one half, so item 113 deliberately does not cover it.

Frozen item-113 package:

~~~
d6d46ba4d8f87268062e027c76ae90b71e45e6e9c80685770e9517aafe741685  sources/common_kernel_roth_high_order_content_obstruction.md
0b0e139df870e3f262f334c0efd278a28a065c3fb85d87326db43bfd96729b8e  scripts/common_kernel_roth_high_order_content_obstruction_certificate.py
272cd4b67284f46d810ff9193b37abc0356848196e1f0e8203d9a9bd3d69516e  results/common_kernel_roth_high_order_content_obstruction_certificate.json
6fe2ebc3013eb81eb2284f44b8e07d03784d048ce76938877e6363b91386686b  results/common_kernel_roth_high_order_content_obstruction_hashes.sha256
~~~

The complete source proof, manifest, and byte-identical 15.3-second replay
pass at only 75,404 KiB peak child RSS.  A separate perturbation audit, not
restricted to the sparse $h_m$, reproduced exact denominator survival for
44 additional prime/output pairs.  This closes a large local regime but
leaves the low-order nonlocal construction/content problem open and does not
classify $e+\pi$.

## Drive backup after items 112--113

A fresh full backup was created at

`/content/drive/MyDrive/e_pi_research_20260826_backup_20260827T211922Z.tar.gz`.

It contains 975 entries, has size 8,582,064 bytes, and SHA-256

`0fd8a86170fb19f5868c65e6e240c8607c53a8cbe9db7e5bf52ecc2107071889`.

Both the gzip integrity test and complete tar listing passed.  This is
recovery state, not a mathematical result.

## Common-kernel checkpoint item 114: the critical CRT family changes sign

The item-107 full-window native specialization has



$$
B_q=x^{20q}(5q+1-5qx^4),\qquad
 h_q=B_q(1-E_q),
$$



where $E_q=(1+x^2)^2x^{12q-8}(1-x^4)^{4q}(1-x^2)C_q$,
$\deg C_q\le11$, its coefficients are nonnegative, and their sum is at
most $(2m_q+1)P_q$ with $\log P_q=4q+o(q)$.

At the endpoint-layer point



$$
t_q=1-x_q=\frac1{5q},
$$



the exact logarithmic slope of $H_{B,q}(t)=B_q(1-t)$ satisfies



$$
\boxed{3\le t_q\lambda_q\le5.}                         \tag{114.1}
$$



Writing $a=-I_N\ge0$, $b=M_N/2\ge1$, this forces the unperturbed
native residual to obey, uniformly for every $N\ge2$,



$$
F_{B,N,q}(x_q)
 \le-2aH_{B,q}(t_q)-\frac12bt_qH_{B,q}(t_q).           \tag{114.2}
$$



On the other hand, the padding gives



$$
E_q(x_q)+t_q|E_q'(x_q)|
 =\exp\{-4q\log q+O(q)\}=o(1),                         \tag{114.3}
$$



with the explicit logarithmic derivative bound
$|E_q'(x_q)|/E_q(x_q)\le120q^2$.  It cannot repair (114.2).
If $I_N>0$, the endpoint value $F_{N,q}(1)=-I_N$ is already negative;
in every case $F_{N,q}(0)=1$.  Therefore every member of this existing
order-$20q$, degree-$48q+13$ CRT family changes sign for all
sufficiently large $q$, uniformly in $N$.

Frozen item-114 package:

~~~
2abd83feaca1058a0c8a6723a4a66e55bfcbddc152985fb3ddebb1722a7693d1  sources/common_kernel_native_crt_endpoint_layer_sign_obstruction.md
0b77e84e1afa44993878dec140db7c6146d28efbeace227d92282c0466cca535  scripts/common_kernel_native_crt_endpoint_layer_sign_obstruction_certificate.py
ffa71b6f020e5fd6efdb3188feecf3b16992aa38c93a5ffdb21b621549bc280b  results/common_kernel_native_crt_endpoint_layer_sign_obstruction_certificate.json
35618f77fbf3a922cfb8ec1309950ac908a0daf901c4498c707d17c938e827ee  results/common_kernel_native_crt_endpoint_layer_sign_obstruction_hashes.sha256
~~~

The source was line-audited, and the exact 5.5-second replay, manifest, and
control-byte checks pass at 68,532 KiB peak child RSS.  The theorem preserves
the algebraic CRT cancellation but proves it cannot coexist with native sign
in this family.  Other low-order localizers remain possible; no classification
of $e+\pi$ follows.

## Common-kernel checkpoint item 115: exact native sign-existence classification

The analytic existence question is now settled completely.  For every
$N\ge2$, there is an $h\in\mathbb Z[x]$ satisfying



$$
h\equiv1\pmod{(1+x^2)^2},\qquad h(0)=0,\qquad
 0\le h\le1,\qquad F_{N,h}\ge0\quad\hbox{on }[0,1]
$$



if and only if



$$
\boxed{N\not\equiv5,6,7\pmod8.}                       \tag{115.1}
$$



For $I_N\le0$, put $a=-I_N$, $b=M_N/2$, $A=a+b$, and in the
$t=1-x$ coordinate define



$$
w=e^{-t}t^N,\quad J(t)=\int_t^1w(s)\,ds,\quad
 \mu=t(a+bt)e^{-t}.
$$



The two strict subsolutions



$$
G_L=\mu(1-4t^2),\qquad
 G_R=\frac{J^2}{J+1/(eA^2)}
$$



cross transversely before $t=1/4$.  Their smooth minimum satisfies
$0<G<\mu$ and $G'>-w$, so $H=G/\mu$ has
$0<H<1$ and a strictly positive residual.  For
$v=1+(1-t)^2$ and $q=(H-1)/v^2$, its endpoint expansions are



$$
q(t)=-t^2-2t^3+O(t^4),                               \tag{115.2}
$$





$$
q(1-s)=-1+(A+2)s^2+
 \{-A^3+A(1-N)+b\}s^3+O(s^4).                         \tag{115.3}
$$



All Taylor coefficients through order three are integral.  Exact integral
Hermite interpolation followed by Draganov's nearest-integer Bernstein
theorem gives ordinary polynomials $Q_n\in\mathbb Z[t]$ converging to
$q$ in $C^3$ with those endpoint jets fixed.  Then



$$
h_n(x)=1+(1+x^2)^2Q_n(1-x)
$$



preserves the interval and residual inequalities for all sufficiently large
approximating degrees.  The delicate $I_N=0$ endpoint has positive main
residual $2bt+O(bt^2)$, while the approximation perturbation is
$O(b\|Q_n'''-q'''\|t^4)$.

Frozen item-115 package:

~~~
283641248f64788c69516874407882efebd5393871ebc23a98a71bd66f30ffbc  sources/common_kernel_native_sign_integer_bernstein_existence.md
e927357755a9449cf1898bd682c75e6d9ae86a08ea24ce04756daf62d5a5b1e8  scripts/common_kernel_native_sign_integer_bernstein_certificate.py
0a6abc5d0c8b11c344cf9c74df93381fd60bc14215848b2ca8949d612891d4ab  results/common_kernel_native_sign_integer_bernstein_certificate.json
337f9276d17304927c34427277fbc62f8bb99642cf525a69aa01c6eed818a2f9  results/common_kernel_native_sign_integer_bernstein_hashes.sha256
~~~

The primary approximation theorem and its ordinary-integral-coefficient
hypotheses were independently checked.  The smooth-min repair, endpoint
stability, exact Hermite Bezout identity, manifest, and byte-identical replay
all pass; root replay peaked at 75,140 KiB RSS.  The construction gives no
degree upper bound and no control of $D_{N,h}/g_{N,h}$.  It therefore
settles the analytic half of the native route but not the arithmetic half or
the classification of $e+\pi$.

## Bessel checkpoint item 116: four-point large-prime exclusivity

Let $q_0=q_1=1$ and
$q_n=(4n-2)q_{n-1}+q_{n-2}$.  For $p\ge5$, take a root
$0\le r\le(p-1)/2$ of $q_r\bmod p$, put
$s=p-1-r$, and define



$$
c=\frac{q_r}{p}\pmod p,\qquad
 \delta=\frac{-q_{r+p}-q_r}{p}\pmod p.
$$



The exact affine anti-period lift and reflection modulo $p^2$ give



$$
\boxed{
 \left(\frac{q_r}{p},\frac{q_s}{p},
       \frac{q_{r+p}}p,\frac{q_{s+p}}p\right)
 \equiv(c,c-\delta,-c-\delta,-c+2\delta)\pmod p.}       \tag{116.1}
$$



For a noncentral orbit and $\delta\ne0$, the four possible vanishing
conditions are $c/\delta\equiv0,1,-1,2\pmod p$, which are distinct.
Thus at most one of the four original values has valuation at least two,
and the other three have valuation exactly one.  If $\delta=0$, either
all four have valuation one or all four have valuation at least two.
At the central fixed point $r=s=(p-1)/2$, reflection forces
$\delta=0$, and the corresponding two representatives obey the analogous
all-or-none dichotomy.

Every $n<2p$, equivalently every occurrence in the window $p>n/2$,
belongs to exactly one such orbit.  The result uses no simple-root or Hensel
assumption.  It leaves one exceptional representative per ordinary orbit,
and fully singular orbits, without an exponent bound.

Frozen item-116 package:

~~~
1e8fed0a5ab04c97c4e0749d40304d6398f9fd32d55c7b49085fb4b4ecca4e41  sources/bessel_large_prime_four_point_exclusivity.md
9a30c35da6a3132406bc5998c10a05f9ed2f4a47510e61cdce4ba7dabd9c29e3  scripts/bessel_large_prime_four_point_exclusivity_certificate.py
ce0a028b2170b8291e3bc42dd088c5bfdcfda2a89b4cf055b550a60623d1c190  results/bessel_large_prime_four_point_exclusivity_certificate.json
a13749e329b3f14381f0c5d9db8ca5239fe9ef7735ffdd071fd40c3531704eea  results/bessel_large_prime_four_point_exclusivity_hashes.sha256
~~~

The manifest pins both recurrence dependencies, and the 4.9-second replay
checks 11,472,792 finite window values at low memory.  The only square in
the diagnostic range $p<10000$ is $(p,n)=(13,8)$, and no cube occurs;
that scan is evidence only.  The all-prime quotient table and exclusivity
law are symbolic.  They narrow but do not close the little-oh valuation
problem or classify $e+\pi$.

## Drive backup after item 116

A further full recovery archive was created at

`/content/drive/MyDrive/e_pi_research_20260826_backup_20260827T213338Z.tar.gz`.

It contains 990 entries, has size 8,637,961 bytes, and SHA-256

`2166e709a23c53cd0d644167c69c1ddb9527d43e61478dec9d5564f3014a6a37`.

Both the gzip integrity check and the complete tar listing passed.

## Common-kernel checkpoint item 117: exact output moment and Farey isolation

For every admissible native localizer



$$
h(x)=1+(1+x^2)^2q(x),\qquad Q(t)=q(1-t),
$$



put $a=-I_N$, $b=(N!-R_N)/2$, and $A=a+b$.  A complete integration
by parts reduces the variable rational coordinate to the single moment



$$
\boxed{
 \rho_{N,h}=\rho_{N,1}-5A
 -4\int_0^1(a+bt)t(2-t)^2Q(t)\,dt.}                  \tag{117.1}
$$



Here $h=1$ is only a nonadmissible algebraic reference coordinate.  The
term $5K(0)$ before substituting $K(0)=-A$ consists of one exponential
boundary contribution and four rational-kernel boundary contributions.

For a raw Bernstein channel $t^k(1-t)^{n-k}$, write



$$
(w_1,w_2,w_3,w_4)=(4a,4b-4a,a-4b,b).
$$



Its exact response is



$$
R_{n,k}=4\sum_{j=1}^4w_j
 \frac{(k+j)!(n-k)!}{(n+j+1)!}.                       \tag{117.2}
$$



Multiplication by $L_{n+5}=\operatorname {lcm}(1,\ldots,n+5)$ makes every
response integral.  This gives an exact ledger in which cancellation against
$L_{n+5}$ is performed before the final gcd with $N!$; denominator
cancellation and primitive content are therefore not conflated.

If arbitrary residue classes modulo $m_n$ are prescribed independently in
all interior Bernstein channels, nearest-representative rounding preserves
$C^3$ approximation uniformly when $m_n=o(n)$.  The third-derivative
rounding multiplier is exactly $96m_n/(n-3)$, and the $k=4$ endpoint
channel proves this scale sharp for a guarantee uniform over arbitrary
patterns.  Since $\log L_{n+5}\sim n$, this excludes only the naive
coefficientwise full-LCM method; adaptive sparse and correlated congruences
remain open.

Independently, all sign-controlled outputs lie in a rational-approximation
interval of length



$$
\Delta_N=\frac{5e-1}{(N+1)N!}.
$$



For every $N\ge14$, $\Delta_N<1/N!$.  Since distinct reduced rationals
with denominators at most $\sqrt{N!}$ are separated by at least $1/N!$,
there is at most one sign-output candidate satisfying



$$
q\le\sqrt{N!}
 \quad\Longleftrightarrow\quad
 \frac{g_{N,h}}{D_{N,h}}\ge\sqrt{N!}.                 \tag{117.3}
$$



Thus a Roth-scale construction must hit the unique candidate, if it exists.
This is an isolation theorem, not an existence or exclusion theorem.

Frozen item-117 package:

~~~
ebb50316d59ff22aa49512372547311fd5f36d24dd88825fcdf6b5ee0090b529  sources/common_kernel_native_output_bernstein_congruence_isolation.md
b5d97041916bf6401df95dbed4427fa910810a6f984f4b977bc6800a587ebca7  scripts/common_kernel_native_output_bernstein_congruence_certificate.py
d9e9defc6276f6efc9777511de9a3f779f893b65a38de7a4bf448dd8e5669762  results/common_kernel_native_output_bernstein_congruence_certificate.json
559cc412db81ed449d4255654ad370f44a8ceb4d8acdce234a7f607d448ffcb7  results/common_kernel_native_output_bernstein_congruence_hashes.sha256
~~~

The proof was independently line-audited.  The manifest passes before and
after a fresh deterministic replay; the latter peaked at 89,256 KiB RSS on
the root run, with its 40 GiB guard satisfied.  The exact moment formula,
response ledger, and scoped rounding and separation statements do not prove
the primitive-decay threshold or classify $e+\pi$.

## Bessel checkpoint item 118: fourth anti-period and cube exclusivity

For $q_0=q_1=1$ and
$q_n=(4n-2)q_{n-1}+q_{n-2}$, every prime $p\ge5$ satisfies the new
universal congruence



$$
\boxed{
 q_{n+4p}+4q_{n+3p}+6q_{n+2p}+4q_{n+p}+q_n
 \equiv12p^2q_n\pmod {p^3}.}                          \tag{118.1}
$$



It follows from a recurrence for the binomial anti-period sums and two exact
Mahler endpoint values.  In particular,
$A_{4p}\equiv12p^2$ and $A_{4p+1}\equiv-24p^2\pmod {p^3}$; all interior
terms in $((1+\Delta)^p-1)^4$ vanish at the required precision.

If $p\mid q_r$ and $a_t=(-1)^tq_{r+tp}$, define the integral first three
differences



$$
d=\frac{\Delta a_0}{p},\qquad
 e=\frac{\Delta^2a_0}{p^2},\qquad
 h=\frac{\Delta^3a_0}{p^2}.
$$



Then (118.1) gives the exact cubic Newton law



$$
\boxed{
 a_t\equiv q_r+tpd+p^2\binom t2e+p^2\binom t3h
 \pmod {p^3}.}                                        \tag{118.2}
$$



On an ordinary first-lift fibre, exactly one residue $t\bmod p$ reaches
$p^2$, and at most that representative can reach $p^3$.  On an all-square
singular fibre, cube divisibility is equivalent to the vanishing of the
explicit polynomial



$$
P_r(T)=\frac{q_r}{p^2}+\frac d pT
        +e\binom T2+h\binom T3\pmod p.                 \tag{118.3}
$$



Thus a nonzero fibre polynomial permits at most three cube representatives;
the alternative is the exact four-coefficient condition $P_r\equiv0$, in
which every representative is a cube.

Reflection couples a noncentral pair by
$P_s(T)=P_r(-1-T)$.  Across the $2p$ representatives there are at most
six cubes unless the complete fibre survives.  More sharply, among the four
indices below $2p$, the arguments are $0,1,-1,-2$; a nonzero cubic
permits at most three, while all four force the full $2p$-representative
branch.  At the central fixed point the invariant cubic is even after a
translation, hence has degree at most two and at most two roots unless it
vanishes identically.

Frozen item-118 package:

~~~
7fe7bd5b2cef3dcb2a12f49c0c620d8d173d818774701a06f1527d80d574a6be  sources/bessel_prime_cube_fourth_antiperiod_exclusivity.md
6e4f612c0d1485de3858d1a9a13320cad766416737f281179c08860eddb30a6f  scripts/bessel_prime_cube_fourth_antiperiod_exclusivity_certificate.py
b60d7edd95835764161553ea68d377f2edafdda321b81137b0d19b45eb139dec  results/bessel_prime_cube_fourth_antiperiod_exclusivity_certificate.json
a46f0ca172db4ff4a8e41cae15bf32b9d61b95f7a71644bfe59b6c4594a854e6  results/bessel_prime_cube_fourth_antiperiod_exclusivity_hashes.sha256
~~~

The all-parameter proof was independently audited through every valuation and
reflection division.  The dependency manifest, control scan, and fresh
5.5-second replay pass at negligible memory.  The finite grid contains no
all-square singular fibre and is explicitly not evidence for that symbolic
branch.  One ordinary exceptional representative and the identically-zero
singular polynomial remain uncontrolled, so no uniform exponent bound or
classification of $e+\pi$ follows.

## Common-kernel checkpoint item 119: effective integer-Bernstein realization

The qualitative sign-existence theorem is now quantitatively effective.  For
$a=-I_N$, $b=(N!-R_N)/2$, and $A=a+b$, the optimized right-end choice is



$$
\ell=\frac{A}{\gcd(A,b)},\qquad
 \epsilon=\frac1{eA\ell}.                              \tag{119.1}
$$



It gives integral endpoint jets through order three; in particular,
$\ell=1$ in the classes $a=0$.

For a $C^5$ remainder $r$ with zero endpoint jets through order three,
put $M_j=\|r^{(j)}\|_\infty$.  The ordinary-coefficient nearest-integer
Bernstein polynomial obeys the explicit bound



$$
\boxed{
 \|(\widehat B_nr)'''-r'''\|_\infty
 \le
 \frac{3M_3+\tfrac{57}{2}M_4+\tfrac14M_5}{n}
 +\frac{96}{n-3},}                                    \tag{119.2}
$$



for $n\ge8$ and $n>9M_4/8$, with exact endpoint jets.  The proof uses an
exact third-difference estimate for the rounding error and a probabilistic
integral formula for the classical Bernstein derivative.

An explicit one-sided smoothing preserves the upper barrier automatically.
Its limiting residual margin is



$$
\rho_N=\epsilon^2e^{-1}\theta_N^N,\qquad
 \theta_N=
 \frac{\gamma_N}{a+\sqrt{a^2+2b\gamma_N}}
 \asymp(N!N)^{-1/2}.                                  \tag{119.3}
$$



The resulting completely explicit sufficient degree satisfies



$$
\boxed{
 \log n_N^{\rm suff}
 \le\frac N2\log A+O(N\log N)
 =\left(\frac12+o(1)\right)N^2\log N.}                \tag{119.4}
$$



This is much larger than the universal necessary scale
$(1/4+o(1))N\log N$ for $\log\deg h$, so it is not claimed optimal.
The constructed coefficient height obeys



$$
\log H(h_{N,n})\le n\log6+O(N\log N).                \tag{119.5}
$$



The variable rational coordinate is exactly a sum of four beta responses
$(k+j)!(n-k)!/(n+j+1)!$, $1\le j\le4$.  Consequently



$$
D_{N,n}\mid\operatorname {lcm}(1,\ldots,n+5),\qquad
 \log|c_{N,n}|\le\psi(n+5)+\log N!+O(1).              \tag{119.6}
$$



These are upper height and denominator bounds only.  They give neither a
lower bound for $D_{N,n}$ nor a nontrivial estimate for
$g_{N,n}=\gcd(N!,c_{N,n})$, and hence neither prove nor disprove the
Roth-scale content condition.

Frozen item-119 package:

~~~
0f5f69dcfd1ce4c2258c0333fe60f20275b1e21591c0e5e0c55bcea05a7acbbb  sources/common_kernel_integer_bernstein_quantitative_arithmetic_audit.md
17fcb7a1ff987981934c3852b7620af38073046de4a233ef613004e1af80c805  scripts/common_kernel_integer_bernstein_quantitative_arithmetic_certificate.py
5ff1c6949bca45a7d4f3bd5c0eb107bf356ab52107949c7aa83a7dec061a895d  results/common_kernel_integer_bernstein_quantitative_arithmetic_certificate.json
80ac4f4e108fd87b7549499abe702e0ddee83c45450ba338e820d18a5ab8437d  results/common_kernel_integer_bernstein_quantitative_arithmetic_hashes.sha256
~~~

The endpoint optimization, smoothing constants, Bernstein estimate, height
recurrence, beta-moment normalization, and scope were independently audited.
The fresh 3.6-second replay passed at 78,608 KiB peak RSS.  This makes the
analytic construction effective but does not classify $e+\pi$.

## Bessel checkpoint item 120: the all-even anti-period hierarchy

For every $k\ge1$, every prime $p>2k$, and every $n\ge0$, the Bessel
denominators satisfy



$$
\boxed{
 \sum_{j=0}^{2k}\binom{2k}{j}q_{n+jp}
 \equiv\frac{(2k)!}{k!}\,p^kq_n\pmod {p^{k+1}}.}       \tag{120.1}
$$



The adjacent odd binomial sum vanishes modulo $p^k$.  The recurrence proof
reduces (120.1) to two Mahler endpoints.  A complete nonendpoint valuation
calculation in $((1+z)^p-1)^{2k}$ removes every other term, while



$$
A_{2kp}\equiv\frac{(2k)!}{k!}p^k,\qquad
 A_{2kp+1}\equiv-2\frac{(2k)!}{k!}p^k
 \pmod {p^{k+1}}                                      \tag{120.2}
$$



give the endpoints.  The two $(-1)^k$ factors in the first congruence
cancel exactly.

On a root fibre $a_t=(-1)^tq_{r+tp}$, all forward differences of order at
least $2k$ vanish modulo $p^{k+1}$.  Hence



$$
a_t\equiv\sum_{j=0}^{2k-1}\binom tj\Delta^ja_0
 \pmod {p^{k+1}}.                                     \tag{120.3}
$$



If the whole fibre already survives through $p^k$, division produces an
explicit degree-$(2k-1)$ polynomial over $\mathbf F_p$ governing survival
to $p^{k+1}$.  It has at most $2k-1$ roots unless all its divided
differences vanish and the entire fibre survives.  Reflection sends it to
$P(-1-T)$, giving at most $4k-2$ survivors across a paired fibre, improved
to $2k-1$ in a window whose $2L$ test arguments are distinct.  At the
central fixed point the degree drops to at most $2k-2$.

Frozen item-120 package:

~~~
c0c834ca8851ddc8dba9edbc9ec74461c0d3aa1b553f79c2320b3d083a0c37de  sources/bessel_all_even_antiperiod_higher_threshold_exclusivity.md
b2f83c96c0166785d491ee0b2d776e67408e0b74f1211b6ea4e862216868c1f3  scripts/bessel_all_even_antiperiod_higher_threshold_exclusivity_certificate.py
53034eebf24139553ad006adedb9afab004e371558844166b1864a106cdce4dc  results/bessel_all_even_antiperiod_higher_threshold_exclusivity_certificate.json
a2ca08905562be561617da55d19620f829bef02ee303473fdb39bebe84f2d899  results/bessel_all_even_antiperiod_higher_threshold_exclusivity_hashes.sha256
~~~

The proof was independently audited through the recurrence, Legendre floors,
endpoint signs, Newton divisions, and reflection.  The fresh replay checks
124,268 even and 124,268 odd congruences and passes at 23,472 KiB peak child
RSS.  Its zero qualifying full-fibre count for every $k\ge2$ is explicitly
not used as evidence.  The hierarchy does not bound the unique ordinary lift
or exclude a zero threshold polynomial, so the required little-oh valuation
bound and classification of $e+\pi$ remain open.

## Common-kernel checkpoint item 121: exact rational-moment integer approximation

Let



$$
W(t)=(a+bt)t(2-t)^2,\qquad
 \ell(f)=4\int_0^1W(t)f(t)\,dt,
$$



where $a,b\ge0$ are integers and $a+b>0$.  If
$f\in C^\infty[0,1]$ has integral normalized endpoint jets through order
three and $\ell(f)\in\mathbb Q$, then there are $P_n\in\mathbb Z[t]$
with the same endpoint jets such that



$$
\boxed{\ell(P_n)=\ell(f),\qquad
 \|P_n-f\|_{C^3[0,1]}\longrightarrow0.}               \tag{121.1}
$$



There is no qualitative image obstruction: for every nonzero
$B\in\mathbb Z[t]$,



$$
\boxed{\ell(B\mathbb Z[t])=\mathbb Q.}                \tag{121.2}
$$



The proof writes the monomial moments of a nonzero $V\in\mathbb Z[t]$ as



$$
\int_0^1V(t)t^n\,dt=
 \frac{F(n)}{\prod_{j=0}^{d}(n+j+1)}.
$$



Along $n=p^k-c$, one denominator factor has arbitrarily negative
$p$-adic valuation while the numerator valuation stabilizes.  Additive
subgroup and Bezout arguments then give every $1/p^k$, hence all of
$\mathbb Q$.

After matching the endpoint jets and the desired moment once, the remaining
function $g$ has zero moment and zero endpoint jets.  Put



$$
S(t)=\frac{\int_0^tW(u)g(u)\,du}{W(t)^2},\qquad
 {\cal D}S=2W'S+WS'=g.                                \tag{121.3}
$$



For every polynomial $U$,



$$
\ell({\cal D}U)=4[W^2U]_0^1.                         \tag{121.4}
$$



Integer Bernstein approximants $S_n$, with the necessary endpoint channels
omitted exactly, satisfy weighted fourth-derivative estimates adapted to
$\operatorname {ord}_0W=1$ or $2$.  Consequently
${\cal D}S_n\to g$ in $C^3$, has zero endpoint jets, and has exactly zero
moment.  This proves (121.1).

If strict real profiles swept output intervals of width $w_N$ with
$Nw_N\to\infty$, an elementary rational grid and (121.1) would give
reduced output denominators $D_N=o(N)$, proving $e+\pi$ irrational by
the positive-form argument.  But every native sign output already lies in a
global interval of width $O(1/N)$, so that sufficient hypothesis is
unavailable.  Moreover, a one-sided Farey gap immediately above $1/2$
shows that width $c/N$ alone does not force denominator $O(\sqrt N)$.

Frozen item-121 package:

~~~
61e396ba87dd73f66a5e7f322c13498aab2b9d0bcd6479895016753014e1e18e  sources/common_kernel_native_exact_moment_integer_approximation.md
9abb9e47a0719f0c0d2b64aa13c7d95c7f3579919e96630c89ab8e5e17fba1e5  scripts/common_kernel_native_exact_moment_integer_approximation_certificate.py
343a71d530acb7dd3681f38d26213f60dd8b8da8a4eb7216eaf6b482a2fc53ae  results/common_kernel_native_exact_moment_integer_approximation_certificate.json
aa35956007909d980f86d43909eaad180d56b9c80a654059425513a1debbb6b9  results/common_kernel_native_exact_moment_integer_approximation_hashes.sha256
~~~

The moment-image group, endpoint reduction, weighted rounding estimates,
kernel identity, and Farey scope were independently line-audited.  A fresh
replay and manifest pass at 76,712 KiB peak RSS.  Exact moment preservation
removes a qualitative construction obstacle but supplies no exceptional
rational position, primitive decay, or classification of $e+\pi$.

## Drive backup after items 117--121

A fresh recovery archive was created at

/content/drive/MyDrive/e_pi_research_20260826_backup_20260827T215701Z.tar.gz.

It contains 1,014 entries, has size 8,741,702 bytes, and SHA-256

2708c1eeeca019f12d0d125b0c08f2c7c21caa572ee2c68fb8b0beb5039cdb87.

Both the gzip integrity test and complete tar listing passed.  The archive
contains the frozen item-121 package and the central documents through item
120; this appended item-121 integration remains recoverable from its frozen
source, script, result, and manifest inside the archive.

## Common-kernel checkpoint item 122: sharp native sign-output diameter

Writing



$$
w(t)=e^{-t}t^N,\qquad B_N=\int_0^1w(t)\,dt,\qquad
 \nu=w+G',
$$



every strict native sign profile has $\nu>0$, fixed mass
$\int_0^1\nu=B_N$, and positive output



$$
{\cal L}_N(G)=\int_0^1R(t)\nu(t)\,dt,
 \qquad R(t)=e+\frac{4e^t}{t^2-2t+2}.
$$



Since



$$
R'(t)=\frac{4e^t(2-t)^2}{(t^2-2t+2)^2}>0,
 \quad R(0)=e+2,\quad R(1)=5e,
$$



one obtains the universal strict range



$$
\boxed{(e+2)B_N<{\cal L}_N(G)<5eB_N}               \tag{122.1}
$$



and hence width at most $(4e-2)B_N$.  An ordered mass-transfer
construction, with identical endpoint germs and integral normalized jets,
attains the sharp asymptotic diameter.  If ${\cal W}_N$ is the supremal
same-germ diameter along the sign-possible indices, then



$$
\boxed{\lim N{\cal W}_N=4-\frac2e.}                 \tag{122.2}
$$



There is also a completely explicit pair for every admissible $N\ge8$ with



$$
{\cal L}_N(G_-)-{\cal L}_N(G_+)\ge\frac{c_*}{N},
 \quad
 c_*=16e^{-4}\left(\frac{e^{3/4}}{17}
                    -\frac{e^{1/4}}{25}\right)>0.   \tag{122.3}
$$



The arithmetic conclusion is a sharp no-go for width alone.  A rational grid
in an interval of width $c/N$ guarantees only denominator $O(N)$, while
the sufficient $o(N)$ denominator would require $Nw_N\to\infty$, which
(122.1) rules out throughout the native family.  Even the limiting width/raw
upper ratio misses the crude positive-integer contradiction by the factor
$5e/(4e-2)>1$.  Positional or additional arithmetic information is still
required.

Frozen item-122 package:

~~~
7d4e9c5dc30c449ca369d52a3fb06e52ff681aedeb47b0dce45b2fc5239f36cc  sources/common_kernel_native_sign_output_range_sharp_width.md
1ee9c9572e165934294a0c5bd32fb4521f7dde406eaeae73b4d970a7870c1615  scripts/common_kernel_native_sign_output_range_sharp_width_certificate.py
25848e5590758fa622d14d45cb32b30a5e29d7c3022aff99de776f6946ec368b  results/common_kernel_native_sign_output_range_sharp_width_certificate.json
de1348caca545595e79ddc00929ece5d0ef7f18fb7eeb3f979beb26f2b766677  results/common_kernel_native_sign_output_range_sharp_width_hashes.sha256
~~~

The integrating factor, endpoint lattice, transfer barrier, sharp limiting
constant, and rational-grid scope were independently audited.  A fresh replay
and manifest verification pass at 77,324 KiB peak RSS.  This determines the
native width frontier but does not classify $e+\pi$.

## Bessel checkpoint item 123: exact ordinary-lift harmonic expansion and barrier

For a prime $p\ge5$, a root representative
$0\le r\le(p-1)/2$, and



$$
T_k(x)=\frac1{k!}\prod_{a=x-k+1}^{x+k}a,
$$



all four reflection-window evaluations have an exact finite expansion.  If
$I_{r,k}=\{r-k+1,\ldots,r+k\}$, multiples of $p$ are removed into
$M_{r,k}$, the remaining set is ${\cal A}_{r,k}$, and
$\nu_{r,k}=|M_{r,k}|-\lfloor k/p\rfloor$, then



$$
\boxed{
 T_k(r+pZ)=p^{\nu_{r,k}}U_{r,k}\Phi_{r,k}(Z)
 \sum_{\ell\ge0}p^\ell Z^\ell
 e_\ell\bigl((a^{-1})_{a\in{\cal A}_{r,k}}\bigr).}   \tag{123.1}
$$



This is an equality in $\mathbb Q[Z]$, with every displayed denominator a
$p$-unit.  Summing the terminating hypergeometric terms gives coefficient
polynomials



$$
{\cal C}_{p,r,j}\in\mathbb Z_{(p)}[Z],\qquad
 \deg {\cal C}_{p,r,j}\le j+1,\qquad
 {\cal C}_{p,r,0}=q_r.                               \tag{123.2}
$$



On an ordinary root fibre, the first layer is the exact unit-slope law
${\cal C}_{p,r,1}(Z)\equiv Z\delta\pmod p$.  Thus the valuation of the
unique possible exceptional representative is reduced explicitly to a finite
symmetric-harmonic unit sum at every $p$-adic order.  What is missing is a
Bessel-specific noncancellation theorem for that sum.

A rigorous countermodel scopes the existing structural inputs.  The linear
polynomial



$$
G(T)=p(T-Z_*-p^{A-1})
$$



has ordinary unit slope, exact reflection companion, all proved even and odd
finite-difference divisibilities, the permitted layer degrees, four-point
exclusivity, height at most $2p^A$, and
$v_p(G(Z_*))=A$ while the other three valuations equal one.  Taking
$A\asymp p$ proves that those inputs together with an
$\exp(O(p\log p))$ height bound cannot imply a sublinear exponent.  The
countermodel deliberately does not satisfy the Bessel recurrence or the exact
coefficients in (123.1).

Frozen item-123 package:

~~~
28a91596edafac946448ea68f4c95dfdcd94e63bcf7586394c464a69d6a76e3d  sources/bessel_large_prime_ordinary_harmonic_expansion_barrier.md
6d0416020a1d1b1f1cfd9093c305b3826b6a32a13f20aea70a72a1017e4ff2c9  scripts/bessel_large_prime_ordinary_harmonic_expansion_barrier_certificate.py
35d48aa29c9ed42a00ab07f407a03f2193cfef72c2109891874a0f2e831a2ade  results/bessel_large_prime_ordinary_harmonic_expansion_barrier_certificate.json
8b3762971ff913e67e26e2cf82baffc4ecfb41b9bcbd79d23cbcad167b6d5348  results/bessel_large_prime_ordinary_harmonic_expansion_barrier_hashes.sha256
~~~

The exact factor separation, four-value reconstruction, first-layer
congruence, and countermodel hierarchy were independently audited.  Two
replays agree; the final run used 20.50 MiB peak RSS.  The remaining problem
is recurrence-specific noncancellation, not another formal congruence layer.

## Common-kernel checkpoint item 124: finite simultaneous exact moments

For arbitrary integer weights $V_1,\ldots,V_m$, define



$$
{\boldsymbol L}(P)=\left(\int_0^1V_1P,\ldots,
                                \int_0^1V_mP\right).
$$



Wronskian formal-adjoint coordinate isolators and the scalar moment-image
theorem give the complete algebraic characterization



$$
\boxed{{\boldsymbol L}(\mathbb Z[t])
       ={\boldsymbol L}(\mathbb Q[t]).}               \tag{124.1}
$$



In particular, linearly independent weights have full image $\mathbb Q^m$,
and the same statement holds inside every prescribed endpoint-zero ideal.

For two independent native weights
$V_i=(a_i+b_it)t(2-t)^2$, every smooth rational-moment target with integral
endpoint jets through order three has integer-polynomial approximants
preserving both moments and all those jets exactly while converging in
$C^3$.  The common zero-moment kernel factors as



$$
g={\cal D}_{V_1}{\cal D}_K U,\qquad
 K=V_2V_1'-V_1V_2'
   =-(a_1b_2-a_2b_1)t^2(2-t)^4,                      \tag{124.2}
$$



so the two inverse equations have no interior singularity.  Weighted integer
Bernstein estimates through derivative five complete the approximation.

A single strict smooth sign profile exists for every finite sign-possible
native system.  For an independent pair, two compactly supported bump
directions give a nonsingular moment matrix; a tiny perturbation therefore
makes both moments rational without changing endpoint germs or losing strict
sign margins, and (124.2) transfers it to one integer polynomial.

This simultaneous freedom does not itself create primitive content.  The two
moments are locally freely variable, and eliminating $e+\pi$ between
indices $N<M$ introduces the factorial ratio $M!/N!$, destroying
smallness.  No common denominator $o(N)$, numerator gcd, or shrinking
primitive integer follows.

Frozen item-124 package:

~~~
73704b5408699aaff3c3254f8e6f8c10c321d22ad06952135aba192591c77d5a  sources/common_kernel_finite_multimoment_exact_approximation.md
738aa3a7ad75ffaea71fdefc95ebed2fa038696c887af57bf3e56e1e7c15ca86  scripts/common_kernel_finite_multimoment_exact_approximation_certificate.py
a50ae12cc7b9e137b5e50745e1d50b8700d1ce36e31d2be0425ed2d994c6a89a  results/common_kernel_finite_multimoment_exact_approximation_certificate.json
b53b8e6f1855fe3eb7ef1b1eae1c303fad3b9cd5344462616606794fd0d9ce6d  results/common_kernel_finite_multimoment_exact_approximation_hashes.sha256
~~~

The image theorem, double-kernel inversion, fifth-derivative weighted
rounding, common-profile gluing, and compact-bump rationalization were
independently audited.  The manifest and fresh replay pass at 85,560 KiB peak
RSS.  This removes a qualitative two-moment obstruction but supplies no
classification of $e+\pi$.

## Drive backup after items 122--124

The integrated archive was compressed to

/content/drive/MyDrive/e_pi_research_20260826_backup_20260827T221612Z.tar.gz.

It contains 1,028 entries, has size 8,805,495 bytes, and SHA-256

122f035c2b1c99d2338eb888a2e21caee28de44709dd18934b73a56d3cf46270.

Both the gzip integrity test and a complete tar listing passed.  This backup
contains the frozen item-122--124 packages and all three central documents
integrated through item 124.

## Common-kernel checkpoint item 125: exact fixed-index output closure

For an admissible native index, put



$$
w=e^{-t}t^N,\qquad J(t)=\int_t^1w(s)\,ds,\qquad
 \mu=t(a+bt)e^{-t}.
$$



Every strict profile satisfies both $0<G<\mu$ and, after integrating
$G'>-w$ backward from $G(1)=0$, the additional obstacle $G<J$.
Since $\mu$ is strictly increasing and $J$ strictly decreasing, they
cross once at $\tau_N$.  With



$$
E_N=\min\{\mu,J\},\qquad
 {\cal L}^{\min}_N={\cal L}^{0}_N-\int_0^1R'(t)E_N(t)\,dt,
$$



the exact fixed-index output set and its closure are



$$
\boxed{\{{\cal L}_N(G)\}=({\cal L}^{\min}_N,{\cal L}^{0}_N),\qquad
 \overline{\{{\cal L}_N(G)\}}
   =[ {\cal L}^{\min}_N,{\cal L}^{0}_N].}             \tag{125.1}
$$



Both endpoints are approached by strict smooth profiles with the same
integral endpoint germs.  The lower envelope carries positive mass away from
zero, so for every fixed admissible $N$,



$$
\boxed{{\cal L}^{\min}_N>(e+2)B_N.}                  \tag{125.2}
$$



Thus the looser lower endpoint from item 122 is asymptotically sharp but is
not the exact fixed-$N$ closure endpoint.

The exact arithmetic replay also repairs a denominator distinction.  If a
translated coordinate is $\rho=c/D$ in lowest terms, the induced reduced
rational approximation to $e+\pi$ has denominator



$$
Q=\frac{N!D}{\gcd(N!,|c|)},                          \tag{125.3}
$$



which can be much larger than $D$.  All earlier small-coordinate-grid hits
have $Q>\lfloor\sqrt{N!}\rfloor$.  A separate exact rational scan finds
genuine $P/Q$ hits with $Q\le\lfloor\sqrt{N!}\rfloor$ at
$N=25,33,43,88,164,331$, but six finite hits give neither an infinite
height-controlled sequence nor a Roth exponent gain.

Frozen item-125 package:

~~~
c9a018f47b54ed565c958da3dbd53b38b912238b63e56234dfb8a9e68ec99d42  sources/common_kernel_native_fixed_N_output_closure.md
75631e0c53a5851bc36f77d592c2c4737cdd4b4ebe8bc5a637062781e93be875  scripts/common_kernel_native_fixed_N_output_closure_certificate.py
a1bb13e6083592872cc0b90d466153e5cb5e76b0f3d685d218ca18cfb4b5ee45  results/common_kernel_native_fixed_N_output_closure_certificate.json
a5c167be7be4ee5924131c4e0dfa2f97ac64232b5a8c90242e6fb064c2d8fcab  results/common_kernel_native_fixed_N_output_closure_hashes.sha256
~~~

The obstacle proof, endpoint-germ constructions, exact integral series,
root brackets, and denominator conversion were independently audited.  Two
final replays were byte-identical; the last used 28,044 KiB peak RSS, and the
manifest passes.  This determines the real fixed-index output geometry but
does not classify $e+\pi$.

## Common-kernel checkpoint item 126: adjacent joint-output thin-strip no-go

For sign-possible $N<M$, set



$$
q=\frac{b_N}{b_M},\qquad
 T(H)={\cal L}_N(H)-q{\cal L}_M(H),
 \qquad \epsilon_j=\frac{a_j}{b_j}.
$$



The exact cancellation of the shared quadratic weight gives, for any two
common profiles,



$$
\delta G_N-q\delta G_M
 =b_N(\epsilon_N-\epsilon_M)t e^{-t}\delta H.
$$



Splitting at any $0<\tau\le1$ yields



$$
\operatorname {diam}T
 \le |\epsilon_N-\epsilon_M|
 \left\{8e b_N\tau^2+
 \frac{2(4e-2)qB_M}{\tau+\epsilon_M}\right\}.        \tag{126.1}
$$



The determinant-one coordinates $(x,y)\mapsto(x-qy,y)$ consequently give
$\operatorname {area}{\cal O}_{N,M}le(4e-2)B_M\operatorname {diam}T$.
For adjacent indices,



$$
\operatorname {diam}T
 \ll\frac{2^{N/2}}{(N!)^{2/3}N^{4/3}},\qquad
 \operatorname {area}{\cal O}_{N,N+1}
 \ll\frac{2^{N/2}}{(N!)^{2/3}N^{7/3}}.               \tag{126.2}
$$



This extreme thinness is defeated by position and integer normalization.
The all-parameter bound $b_{N+1}\ge(7/2)b_N$ implies $q\le2/7$, hence



$$
\boxed{T(H)>\frac57B_N\ge\frac5{7e(N+1)}}           \tag{126.3}
$$



for every pair.  If $g=\gcd(b_N,b_M)$, the primitive integer normal is



$$
U=\frac{b_M}{g}{\cal L}_N-
   \frac{b_N}{g}{\cal L}_M=\frac{b_M}{g}T.            \tag{126.4}
$$



For adjacent indices,
$g\mid((N+1)R_N-R_{N+1})/2=O(N2^{N/2})$, while
$b_{N+1}\asymp(N+1)!$; thus the primitive normal is centered at
factorial-over-exponential scale, not near zero.

On $N\equiv0,1,2\pmod8$, the exact adjacent infimum is



$$
D_N^0=\int_0^1R(t)e^{-t}t^N(1-t)\,dt,
 \qquad N^2D_N^0\longrightarrow5.                   \tag{126.5}
$$



Under the temporary rationality hypothesis, outputs within a fixed multiple
of this boundary require clearing denominator $\Omega(N^2)$, and every
positive rational output already requires $D>(N+1)/(5e)$.  Separately,
the unique primitive vector cancelling the two factorial coefficients is
$(M!/N!,-1)$; its value is at least $(e+2)/(2e)$ for $N\ge14$.
Accordingly neither the adjacent difference nor the factorial-cancel
direction supplies a small nonzero integer.

Frozen item-126 package:

~~~
a20afd820c91b4feef14479bb82b15dab1599a109b2463a6c5c97fc6edb5a8aa  sources/common_kernel_adjacent_joint_output_thin_strip_no_go.md
a26660b7b067571c348d221cf6e01ee9489903d4e7fbb9920caf30ef95970c72  scripts/common_kernel_adjacent_joint_output_thin_strip_certificate.py
8869c862afbe471cae5cf78694bbdaea812603ded1d87b8dba1f7aac5de466ae  results/common_kernel_adjacent_joint_output_thin_strip_certificate.json
df1f67b6f612402a0877ca937dc9494581f8ec3b58634f54abc418b475ec5ef6  results/common_kernel_adjacent_joint_output_thin_strip_hashes.sha256
~~~

The thin-coordinate algebra, coefficient-ratio theorem, positional bound,
adjacent asymptotics, conditional denominator logic, and primitive
normalizations were independently audited.  Two fresh replays pass; the
last used 70,880 KiB peak RSS.  This is a scoped no-go for the natural
two-output determinant routes, not a classification of $e+\pi$.

## Bessel checkpoint item 127: first three layers and Wilson carry

The exact ordinary-root expansion splits into five factorial blocks.  After
Wilson reflection, the high blocks reduce modulo $p$ to three explicit
low factorial-harmonic families $A_\ell,B_\ell,G_\ell$.  In particular,
on a root $p\mid q_r$,



$$
\delta=A_1+B_0,                                      \tag{127.1}
$$



and the next two raw layers are



$$
\begin{aligned}
 {\cal C}_2(Z)\equiv{}&Z^2(A_2+B_1)+Z(Z+1)G_0\\
 &+Z^2(Z+1)A_1+Z(Z^2-1)B_0,\\
 {\cal C}_3(Z)\equiv{}&Z^3(A_3+B_2)+Z^2(Z+1)G_1\\
 &+Z^3(Z+1)A_2+Z^2(Z^2-1)B_1
 \pmod p.                                             \tag{127.2}
\end{aligned}
$$



The first lower-layer carry is also explicit.  If $Z_0$ is the unique
ordinary square-threshold endpoint, then



$$
\frac{F_{p,r}(Z_0)}{p^2}\equiv
 \kappa_2(Z_0)+{\cal C}_2(Z_0)\pmod p,                \tag{127.3}
$$



where



$$
\kappa_2(Z_0)=
 \frac{q_r/p+Z_0\widehat P+Z_0(Z_0+1)q_r}{p}
 +Z_0(Z_0+1)R_r.
$$



Here $\widehat P=A_1^\sharp+B_0^\sharp$, and
$R_r$ is an explicit factorial-weighted harmonic sum.  The Wilson quotient
cancels from $R_r$ because $p\mid q_r$.

The crucial obstruction is exact at every order:



$$
\boxed{{\cal C}_{p,r,j}(0)=0\qquad(j\ge1).}          \tag{127.4}
$$



Thus no theorem asserting nonvanishing of some bounded *raw* positive layer
can control the base endpoint; there the entire valuation is already in
$q_r$.  At the other endpoints, a nonzero raw layer can cancel with the
carried lower digits.  A valid bounded-valuation proof must separately
exclude the base square or prove noncancellation for the carried expression.

The carried formula reproduces the square at $(p,r,Z_0)=(13,4,-1)$ and a
new finite diagnostic square



$$
p=52453,\qquad r=14378,qquad Z_0=1,qquad n=66831,
$$



where $v_p(q_n)=2$ and $q_n/p^2\equiv41153\pmod p$.  An exhaustive
eight-thread exact scan over $10000\le p<500000$ covered 40,309 primes and
20,351 ordinary root orbits, found no singular orbit, this one square only,
and no cube.  These statements are finite diagnostics, not a universal
valuation bound.

Frozen item-127 package:

~~~
af171d428ac26019c3d98af3cd46a72cfa64db5a305857f369b05a6cfd5fa44f  sources/bessel_ordinary_first_three_layer_wilson_carry.md
6284b8afcbfed1349df814a7be0f4e507c59a9202308684ab7f706fbb366ad2a  scripts/bessel_ordinary_first_three_layer_wilson_carry_certificate.py
fde48d5d77ab0aa33fccdd6a9e229305e5e2c8c92a43fd8ec2ce5135b635bd86  scripts/bessel_ordinary_large_prime_scan.cpp
d27210380697091ae0e1f37573d1035c8c228885839c1d4720babaa4b3a2ef48  results/bessel_ordinary_first_three_layer_wilson_carry_certificate.json
76a9244467bac4c6b9ca35b534c8bbd73ae774e6e732fb298e85255b44035b54  results/bessel_ordinary_large_prime_scan_certificate.json
8404b4b76df36a327e29f7b444572326bf344b9691e2d522969723407956efa7  results/bessel_ordinary_first_three_layer_wilson_carry_hashes.sha256
~~~

The five-block signs, Wilson weights, harmonic reflections, endpoint table,
and carry numerator were independently derived and audited.  Two Python
replays and two full C++ scans were byte-identical; peak scan RSS was 106
MiB, and the manifest passes.  No irrationality or transcendence conclusion
is claimed.

## Drive backup after items 125--127

A fresh recovery archive was created at

/content/drive/MyDrive/e_pi_research_20260826_backup_20260827T224408Z.tar.gz.

It contains 1,045 entries, has size 8,898,907 bytes, and SHA-256

3ea7f09f520fed61ecf6e26437f6a916d5636d97ff976aeda9ca5dbde9b95370.

The gzip integrity test and complete tar listing passed.  The archive
contains all frozen item-125--127 artifacts and all three central documents
integrated through item 127.  This backup record itself was appended only
after verification; the complete frozen packages and preceding checkpoint
text are inside the archive.

### 2026-08-27 — Native factorial windows and continued fractions (item 128)

The exact endpoint asymptotics imply that every reduced native hit with
$N\ge10$ and $Q^2\le N!$ is a principal continued-fraction convergent
and must satisfy



$$
1<N\,N!\left(e+\pi-\frac PQ\right)<5.
$$



An exact outward fixed-point enclosure of $e+\pi$, with 5,856 decimal
places and width $71822\cdot10^{-5856}$, certifies the continued-fraction
prefix far enough to exhaust this window for every $10\le N\le2000$.
There are nine broad candidates; three are in forbidden native residue
classes, leaving exactly the six previously certified hits
$25,33,43,88,164,331$.  In particular there is no new admissible hit from
332 through 2000.

~~~
c7464fc9dbcbd5bd26146a500da797abdaf8b25ea04f3444994ec46097088e16  sources/common_kernel_native_cf_window_scan.md
d127322e0362aa179a5358d4ca54116929666ddc77e41acc33859ae026ec6a03  scripts/common_kernel_native_cf_window_scan_certificate.py
051f52f528a9835fc33938e99952fa483ae32ca9d5bf4b2d0c862c829fa94d9f  results/common_kernel_native_cf_window_scan_certificate.json
45c9253a4d4572806c0650345f2e47e4d8953618daf5c87512a1d62e0e1cd958  results/common_kernel_native_cf_window_scan_hashes.sha256
~~~

The source was line-audited, the exact replay was repeated byte-identically,
and the manifest passes.  This is a finite exclusion only: no infinite match,
irrationality proof, or Roth power saving has been obtained.

An unfrozen exact extension, using the same outward interval algorithm with
16,466 decimal places, certified 16,079 common continued-fraction
coefficients through $\sqrt{5000!}$.  It found the same nine broad
candidates and hence no candidate at all for $1478\le N\le5000$.  The run
took about 62 seconds and is retained only as finite diagnostic evidence; the
frozen theorem-facing cutoff remains $N=2000$.

### 2026-08-27 — Multi-output Smith denominator obstruction (item 129)

Every cleared simultaneous native response factors through the same two
Gaussian columns, so additional outputs create left kernels but no new
variable moment directions.  On five consecutive sign-possible indices
starting with $N\equiv0\pmod8$, a primitive factorial/Gaussian-annihilating
relation has exact value



$$
\delta_N=\frac{2\eta_N}{(N+2)(N+3)},
 \qquad
 \eta_N\in\{1,71\}.
$$



The exceptional value $71$ occurs exactly when
$N\equiv16\pmod{71}$.  Although $\delta_N=O(N^{-2})$, its reduced
denominator is $Q_N=(N+2)(N+3)/2$, and the exact Smith calculation proves
$Q_N\mid D$ for every common denominator $D$ of the five rational
corrections.  Therefore $D\delta_N$ is already a nonzero integer.  Four
outputs have a growing invariant; five outputs also introduce exact-zero
relations.

~~~
ea090145c760599bd1eb4a85192aa330da72cc8f6bebaebaff25b827e28c0367  sources/common_kernel_multioutput_smith_quadratic_denominator_obstruction.md
a346881d779d2c272a8a342bd3a16099134d3ba68e00f807672609192728df43  scripts/common_kernel_multioutput_smith_quadratic_denominator_certificate.py
cc8740eee8eb4c470cfca2ae1cb91c7898b0722a14b8a37eadb6b76e7c606e1e  results/common_kernel_multioutput_smith_quadratic_denominator_certificate.json
786c6e2c2f25aa1cd11a0b0b480277eaaacd1a8bda54b70af2ad9f6d46939fe5  results/common_kernel_multioutput_smith_quadratic_denominator_hashes.sha256
~~~

The all-parameter proof, exact generators, resultants, markup audit, dependency
pins, repeated replay, and manifest pass.  This closes the natural
multi-output Smith shortcut without proving the requested classification.

### 2026-08-27 — Symmetric Bessel transfer and base-carry barrier (item 130)

At every noncentral root $p\mid q_r$, the reflection transfer and its
symmetric-continuant entry give



$$
M_{p,r}\equiv
 \begin{pmatrix}1&0\\4r+2&1\end{pmatrix}\pmod p,
 \qquad
 \delta\equiv-2{\cal K}'_h(0)q_{r-1}\pmod p.
$$



The base quotient $q_r/p\bmod p$ is absent from the slope formula.  A
Charlier connection expresses base squarefreeness as a separate
partial-injection congruence, while the next carried layer contains the next
base digit $d$ with coefficient one:



$$
\frac{F_{p,r}(Z_0)}{p^2}\equiv d+\Psi_{p,r}(Z_0)\pmod p.
$$



Thus ordinary simplicity and raw-layer resultants cannot by themselves prove
the required uniform valuation bound.  Exact companion-solution examples
show this limitation for the recurrence while deliberately changing the
initial normalization; they are not counterexamples for the original
sequence.

~~~
769c886c1c8e5a6e406bd2018c71846e2831170359c2e97b43939e200a108c6e  sources/bessel_ordinary_symmetric_transfer_base_carry_barrier.md
7dbe32fb6ab59c001724543ea4a7e3657e9a5b6bb24ad918e363b549d285c9ec  scripts/bessel_ordinary_symmetric_transfer_base_carry_certificate.py
7f964cbbd5d0cdc749959614ae3e54e92bc8914227005fc9f4acf168a127512b  results/bessel_ordinary_symmetric_transfer_base_carry_certificate.json
bda724f3790cda56b5bc67fb99ccc854c693da1a2c7d53c85108e4cda394b5e6  results/bessel_ordinary_symmetric_transfer_base_carry_hashes.sha256
~~~

The signs, continuants, Charlier lifts, carry representatives, countermodels,
dependencies, and repeated exact replay pass.  This package narrows the
Bessel frontier without proving an arithmetic classification.

## Live mixed-cubic continuation

For $Q=(1+x)(1+x^2)$, $n=6m$, and $k=4m+1$, direct differentiation
has produced the exact three-power relation



$$
A_mH_{n,k}+B_mH_{n,k+1}+C_mH_{n,k+2}=0,
$$





$$
A_m=(10m+2)(10m+3),\quad
 B_m=-(10m+3)(20m+5),\quad
 C_m=8(2m+1)(4m+1).
$$



Indeed, with



$$
S_m(x)=-(6m+1)-(10m+3)(x+x^2+x^3)-x^4,
$$



the derivative of
$x^{n+1}(1-x)^{n+1}S_m(x)/Q(x)^{k+1}$ is the integrand of the displayed
linear combination, and its endpoint values vanish.  Consequently the two
successive log-cancelled $1,\pi$ forms are rationally proportional:
$\Lambda_{k+1,k+2}=(A_m/C_m)\Lambda_{k,k+1}$.  This explains the repeated
primitive pairs in the boundary data and prevents the first three adjacent
powers from supplying a second independent small form.  A separate prime-band
content theorem and full asymptotic audit are still in progress; this live
identity has not yet been assigned a frozen item number.

## Common-kernel checkpoint item 131: factorial-entry dichotomy

At the first admissible entry of a below convergent denominator under the
power cutoff $q^\tau\leq N!$, $\tau=2/(1-2\delta)$, the exact
gap-four ledger is



$$
1\leq N!/q^\tau<N^4.
$$



For $Z=N\,N!(x-p/q)$, a low native-window miss yields



$$
a_{\mathrm{next}}>\frac{N}{5}\frac{N!}{q^2}-2,
$$



whereas a high miss yields the opposite-type upper bound



$$
a_{\mathrm{next}}<N\frac{N!}{q^2}.
$$



Thus, for $\delta>0$, infinitely many low entries are Roth-incompatible
with algebraic irrationality, while eventual high entries bound the
below-side irrationality exponent from above.  At $\delta=0$, the low
gain is logarithmic only.  The exact golden-ratio countermodel proves that
absent factorial-window hits do not abstractly force large partial
quotients.  Badly approximable inputs require a maximum window scale
$\Omega(N)$; separately, connected fixed-ratio coverage needs
$\Omega(\log N)$ copies.

~~~
572ae7a426a22e1775a774732629c71d005dc0d1214288231bb8dd1456db3714  sources/common_kernel_factorial_window_cf_entry_dichotomy.md
d61d0617f8d1322d07d13f13b01e87366b1a7175b086128cc0096406b38aa3d4  scripts/common_kernel_factorial_window_cf_entry_dichotomy_certificate.py
401ef6b199eacf4f72ab41f7bd673e440f3c6dc7e0ce84b28571b2611d67f99e  results/common_kernel_factorial_window_cf_entry_dichotomy_certificate.json
e020e4c07067054101c4755b0a3899b79d93c7db468b0162daf2d946e1e944bc  results/common_kernel_factorial_window_cf_entry_dichotomy_hashes.sha256
~~~

The source correction separating absolute scale from relative coverage was
audited before freezing.  Independent replay, dependency checking, markup,
control bytes, and the manifest pass at about 69 MiB peak RSS.  No claim
about the arithmetic nature of $e+\pi$ follows.

## Bessel checkpoint item 132: an all-$h$ derivative formula

The symmetric transfer continuant now has the exact identities



$$
\begin{aligned}
 {\cal K}'_h(0)
 &=(-1)^h\left(
 P_{h,0}^2+2\sum_{j=1}^h(-1)^jP_{h,j}^2\right)\\
 &=\sum_{a=0}^h(-16)^a(a!)^2
 \binom{h+a+1}{2a+1}.
\end{aligned}
$$



The positive tails satisfy $P_{h,j}\leq P_{h,0}/(4^j j!)$, whence



$$
\frac{13}{15}P_{h,0}^2
 <(-1)^h{\cal K}'_h(0)
 <\frac{17}{15}P_{h,0}^2.
$$



There is also an exact pentadiagonal determinant representation.  These
facts prove integer nonvanishing and sign, but not modular nonvanishing:
${\cal K}'_2(0)=963$ is divisible by $107$.  The independent base
Charlier digit remains outside this theorem.

~~~
9d553e597f353915d16279031f4d0415342f8dfde628c925bcabd51e442f0d57  sources/bessel_symmetric_continuant_lommel_derivative_theorem.md
7e6816a4fbd63b818d1ea1acd370c274df1eeb2516ff2c5b5881a78f4619569c  scripts/bessel_symmetric_continuant_lommel_derivative_certificate.py
3b78a0cd61d0bf701db017a4a0a71fe59399aaa2e87e98e01c44c3baa2c5227e  results/bessel_symmetric_continuant_lommel_derivative_certificate.json
711d2f95dc6a8acee83b8a92b472d668f5aafcb4020197fe96ecfe3d8ea09bcf  results/bessel_symmetric_continuant_lommel_derivative_hashes.sha256
~~~

Root replay, the two independent formulas, tail and block identities,
Cauchy--Binet minors, control bytes, dependency, and manifest pass at about
19 MiB peak RSS.  The result does not prove a Bessel valuation bound or
classify $e+\pi$.

## Mixed-cubic checkpoint item 133: the arithmetic crosses one conditionally

For the boundary adjacent form
$\Lambda_{01}=A_m+B_m\pi$, exact partial fractions and a new
relative-Cartier theorem give



$$
{\cal D}^{\sharp}_m=
 \frac{2^{9m+5}M_{4m+1}}
 {\displaystyle\prod_{2m<p<3m}p}
$$



as a common clearing.  A disjoint exact-differential prime set divides the
two cleared coordinates and has logarithmic size



$$
\left(-4\log2+\frac{\pi}{\sqrt3}+3\log3\right)m+o(m).
$$



For $2m<p<3m$, both transformed residual differentials have Cartier image
in one common line.  The relative endpoint lemma therefore makes
$(pR_s,L_s,E_s)$ proportional mod $p$ and removes the entire
squarefree middle band from the determinant denominator.

The exact three-adjacent relation proves that the next adjacent form is
rationally proportional, not independent.  The exact common-phase contour
identity removes the leading residue ratio $5/8$.

Conditional on a still-unproved unique accessible-saddle asymptotic, the
now-proved arithmetic gives



$$
d=2.3370623743\ldots,\quad
 h_{\rm cert}=2.3246783391\ldots,\quad
 d/h_{\rm cert}=1.0053272038\ldots.
$$



This was originally described as crossing the threshold needed to match with a
positive $e$-form.  Item 137 corrects that downstream claim: absent a new
exponential matching-content theorem, the generic threshold is $d>2h$, not
$d>h$.  The contour theorem was later established in items 135--136, but no
irrationality or arithmetic classification of $e+\pi$ followed.

~~~
286d9cf4d3591a1a9b9fefc6dd3ee3dcc9f7c2ba49a73310909491814544d9e8  sources/mixed_cubic_boundary_cartier_content_and_recurrence.md
81d9fa515ba39719d17a5f35456e3749d34f8d857a0411b97fff228c39a36d6d  scripts/mixed_cubic_boundary_cartier_content_and_recurrence_certificate.py
3a060ecf43afe8a5047401cfed9ac2208345b5f2636ef88c14ce959324dace29  results/mixed_cubic_boundary_cartier_content_and_recurrence_certificate.json
34e61497fa2df8dd4dfcaf143be574bd3ada434977d41e6be75b590ba927a14c  results/mixed_cubic_boundary_cartier_content_and_recurrence_hashes.sha256
~~~

The clearings, relative-Cartier proof, disjoint content, PNT constants,
recurrence, contour identities, markup, controls, repeated replay, and
manifest pass.  The then-live saddle target is now closed by items 135--136;
the corrected live target is the synchronization/support gap in items 137--138.

## Common-kernel checkpoint item 134: conditional denominator saturation

If $e+\pi=u/v$ and $v\mid N!$, then $M=N!(e+\pi)\in\mathbb Z$.
The strict native integer outputs are exactly



$$
\mathbb Q\cap({\cal L}^{\min}_N,{\cal L}^{0}_N).
$$



For an output $m/D>0$ in lowest terms, the translated coordinate
$(m-MD)/D$ has the same reduced denominator.  Therefore every member
satisfies $D{\cal L}^{0}_N>m\geq1$, so qualitative rational-point
selection cannot produce the desired strict positive-integer contradiction.

For every admissible $N\geq1246$,
$D_N=\lfloor N/5\rfloor+1$ is the least possible denominator and



$$
{\cal L}^{\min}_N<1/D_N<{\cal L}^{0}_N,\qquad
 1<D_N{\cal L}^{0}_N<1+5/N.
$$



Under the rationality hypothesis the target $1/D_N$ is realized exactly,
with cleared positive value one.  This saturation theorem is conditional
and closes only the qualitative interval-selection shortcut.

~~~
52a554fd8c39d2caa641fafbbb43ad572b5e736e70c230793d5ece365da30332  sources/common_kernel_rational_case_denominator_saturation_barrier.md
d96c493f3af8e62638a23562ae096f732bcaf4306bcdee2e98ab05713fde0905  scripts/common_kernel_rational_case_denominator_saturation_certificate.py
c51ba0bdc55ac3ebc2220dcdfb44c7a728b8c80059f1cac99aa395d5cfb78371  results/common_kernel_rational_case_denominator_saturation_certificate.json
a90239b6de95a344d41728ee404dfde0d3a5c8ab8f6368e7bfdd1316c5c9dadf  results/common_kernel_rational_case_denominator_saturation_hashes.sha256
~~~

Five dependency manifests, exact inequalities, controls, markup, repeated
replay, and the frozen manifest pass at about 69 MiB peak RSS.  The theorem
does not prove rationality, irrationality, or transcendence of $e+\pi$.

## Temporary-stop handoff — 2026-08-27 UTC

Research was stopped at the user's request after all active workers had saved
their state.  No proof that $e+\pi$ is algebraic, irrational, or
transcendental has been obtained.  Items 131--134 above are the last frozen
packages.  Two additional notes preserve the unfinished analytic work and are
explicitly not theorem packages:

~~~
fe731a600578a4b7d585af1f1de9b2c231d09929a13dc568400938414ac1313b  sources/mixed_cubic_boundary_saddle_handoff.md
c8eb9e3b6267bb6ccc949aa145ccb4bf3ac627a1a6f97d51aebcda930b29aa0b  sources/mixed_cubic_accessible_saddle_handoff_20260827.md
~~~

The second hash differs from the worker's first report only because eight
accidental tab/carriage-return characters in intended $\tau$/$\rho$
tokens were normalized before this checkpoint was frozen.

The most concrete next target is an exact fixed-circle saddle certificate for



$$
\Psi(v)=\frac{(1+2v)^6(1+(1-i)v)^6}{v^4(1+v)^4}.
$$



The proposed accessible saddle is



$$
\tau=0.3933435869406637868\ldots+
      0.2348766139072831759\ldots i,\qquad
 \rho=|\tau|=0.45813338794274588\ldots<\frac12,
$$



where $\tau$ is a root of



$$
4v^3+(6-i)v^2-iv-1-i=0.
$$



The exact algebraic parametrization, the degree-six angular critical
polynomial, the provisional Sturm sign table, the exact quadratic saddle
coefficient, and the amplitude quotient are all recorded in the accessible
saddle handoff.  Numerically the critical polynomial has only two real roots:
the one at $\tau$ is the circle maximum and the other is the circle minimum.
This is diagnostic evidence, not yet an exact certificate.

The next instance should:

1. isolate the selected algebraic radius by rational endpoints;
2. certify the complete degree-six Sturm sign table using exact rational
   interval arithmetic over the selected real-algebraic embedding;
3. certify the maximum, $\Re\lambda>0$, and
   $\operatorname{Im}(b_2(\tau)/b_0(\tau))>0$;
4. write the uniform fixed-circle complex-Laplace proof for both amplitudes;
5. replay the resulting certificate twice, freeze a manifest, and obtain an
   independent line/formula audit.

The equal-modulus saddle
$\tau^*=-1-\overline{\tau}$ has modulus greater than one and lies in a
different radial region beyond the pole at $-1$; it must be mentioned but
does not lie on the valid coefficient circle.  The accessible-saddle theorem
was subsequently completed.  The factor-of-two audit in item 137 shows that
the $0.012384$ per-$n$ margin only makes the integer $1,\pi$ forms shrink;
it does not suffice for generic positive matching with an $e$-form.  The
original classification objective therefore remains unfinished.

At pause time no accelerator computation was active or needed: the decisive
work is low-degree exact symbolic algebra and proof writing.  System memory was
safe, with about 6.4 GiB used and 44 GiB available out of 50 GiB; swap is
disabled.

### Final pause audit

After the handoff edits, all 238 Python programs parsed as ASTs, all 245 JSON
certificates loaded, both C++ programs passed a C++17 syntax check, and all 93
package hash manifests verified.  A control-byte scan passed on 750 text
artifacts, and the inventory exactly matched 262 source notes, 238 Python
programs, two C++ programs, and 245 JSON certificates.

Four orphaned exploratory Python processes from earlier worker tasks were still
running despite the workers having returned.  Their exact process identities
and working directory were checked, and those research jobs were terminated to
honor the requested pause.  This reduced memory use to about 3.7 GiB, leaving
about 46 GiB available.  All subagents are complete and no research computation
is intentionally active.
