> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent integer-interval verification of the fixed limiting operator

The primary agent read the complete odd-order fixed-operator certificate, original program, and complete result file, and reviewed the actual matrices, two-mode boundary decomposition, half-line limit, and error-tail proofs. The verification below uses original witness vectors as exact rational data without running the original research program or mpmath library. The all-parity exclusion chain for the original diagonal family is now complete. Other routes receive priority team review under the user's instruction; rationality of e+π remains unresolved.

## Exact inputs and arithmetic

The original witness file is work/session_20260913/raw_odd_limit_certificate_vectors.json, SHA-256 `196c620cad7043be1932aaae4fc07f8192351053a2e0f9a1ce50d01e75ecc83f`. Three vectors each have 128 complex coordinates, totaling 768 real rationals and 1,536 integer tokens. Every denominator was checked against the original data as a positive power of two. All coordinates participate. The witness-generation program was not located and is not a mathematical-validity input.

The primary reviewer's [interval module](fixed_interval_main.py) uses only standard-library integers and Fraction. Endpoints are integers divided by 2¹⁹². Addition/subtraction are exact; multiplication/division use integer downward/upward rounding; square roots use integer square root with explicit upward rounding. Complex arithmetic is built from these interval operations. Complete original endpoints are preserved in result JSON; displayed decimals only describe the results.

Machin's identity and the alternating arctangent series enclose π. Taylor polynomials with explicit Lagrange remainders enclose cosine. The primary implementation uses exact remainder reduction of periodic angles rather than the original program's cosine recurrence, so neither the original interval library nor quadrature program is reused.

## Odd-order certificate

The primary [verification program](check_odd_fixed_operator_intervals_main.py) reconstructs 512-point paired quadrature, every required Fourier block, the 24-term matrix-exponential series, analytic alias bounds, and three complete half-line residuals. Input support is 0..63, output prefix 0..127, and block 128 is included to retain the last neighbor. The omitted infinite tail uses analytic Fourier decay from the original proof, retaining the full tail norm of the geometric right-hand-side vectors.

The actual inverse norm is less than 12, so 12 times the complete residual bounds each exact solution's distance from its witness. Independent primary recomputation verifies strict upper bounds 3.508×10⁻¹³, 2.827×10⁻¹², and 1.682×10⁻¹¹ respectively. The original finite-matrix inverse is not used to estimate error.

Boundary tests retain complete solution errors. The resulting exact rational intervals support:

| Actual fixed object | Verified strict interval |
|---|---|
| det D2₊ | 62/100 to 63/100 |
| det D3₊ | −136/100 to −135/100 |
| s∞=det D2₊/det D3₊ | −47/100 to −45/100 |

See the complete [odd-order fixed-operator controls](RAW_ODD_FIXED_OPERATOR_INTERVAL_MAIN_CONTROL.json). Reality of both determinants is proved separately by phase transformation, not by a small imaginary-part interval. The original matrix and limiting-operator proofs are now primary-reviewed. These checks supply their two required nonzero limits and a uniform inverse bound for actual finite matrices at sufficiently large indices. The convergence proof gives no effective first index.

## Even-order reuse

The actual even space has two components of degrees m and m−1. In the common Cayley space it is the kernel of evaluating the second component at −i; this exact codimension-one constraint must be retained. The primary reviewer checked the normalization, norm convergence of both evaluation vectors, inverse convergence from strict accretivity, and the complete inverse-compression identity.

The two columns of A0₊⁻¹U in the original proof are exactly w/√2 and v/√2. The first two verified witnesses therefore supply four complete scalar pairings. The primary [even-order postprocessing](check_even_corner_from_witnesses_main.py) uses the new residual bounds to recompute complete finite-support pairings and complex division by nonzero denominators. Reality follows from the reviewed actual compression limit.

The result supports 91149/100000 < g₊ < 91150/100000. An integral factorial series and complete tail bound for e additionally verify 783/1000 < √(3e)/(4g₊) < 784/1000. Complete exact results are in the [even endpoint-corner controls](RAW_EVEN_CORNER_FROM_WITNESSES_MAIN_CONTROL.json). No new linear solve or original HP index was added.

## Implications for continued research

These results close a set of inputs for fixed-operator nonvanishing and complete actual parity-specific exponential error. They do not themselves control the complete arctangent error or actual endpoint common factor. The four actual saddle amplitudes, complete contours, strict phase maximum, and endpoint remainders were subsequently checked separately; see the [saddle and overall exclusion note](MAIN_RAW_SADDLE_AND_EXCLUSION_APPLICATION.md). Together with separately reviewed actual denominator arithmetic, the original approximation exclusion theorem is registered. It does not prove rationality of e+π. See [arithmetic and analytic dependencies](MAIN_RAW_ARITHMETIC_AND_ANALYTIC_INPUT_CHAIN.md) for continuation status.
