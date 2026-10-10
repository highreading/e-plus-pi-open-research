> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent finite dyadic coefficient reconstruction on four odd disks modulo 1024

Status: Independently reviewed research result (AI review; not formal verification)
Author: worker_3
Reviewer: worker_2
Content SHA256: 95120d1360a13ef505aae42ed923cca030f0b44ceb99489e17c245501c410269
Review: work/astra_review_registry/reviews/worker3-dyadic-finite-coefficient-verification-v1-worker_2.md

STATUS: UNVERIFIED; submitted for independent review. This claim concerns a finite exact modular computation only.

DEFINITIONS. Let (Z)_r=Z(Z−1)…(Z−r+1), with (Z)_0=1. For a∈{1,3,5,7}, put X=a+8u. Sum over nonnegative b,c with R=b+2c<55, and set s=b+c and e=(-1)^b/(2^c b!c!). Define h_{b,c}=e(X)_R(X)_s. Define k_{0,0}=2 and, for R≥1, k_{b,c}=e(X)_{R−1}(X+1)_s(2X+2−R). Let D_19(Z)=Σ_{j=0}^{19}(Z)_j. Define finite polynomials H=Σh, K=Σk, A=Σh D_19(2X−R), B=Σk D_19(2X+1−R), and C=KA−HB.

CLAIM. Every retained h and k is coefficientwise 2-adically integral. Every coefficient of each finite H,K,A,B,C, reduced modulo 1024 and with trailing zero coefficients removed, agrees with the corresponding array in work/session_20260927/hp_b1_odd_dyadic_germs_checks.json (source SHA256 f8efc553dbad4713c088bddfe7c60d45d6f8caf87d868ddb4c2b85d1124f77fb). In ascending powers of u, the C arrays are: a=1: [0,216,32,768,512]; a=3: [652,296,544,128]; a=5: [564,184,672,768,512]; a=7: [824,808,480,128]. All remaining coefficients are zero modulo 1024.

METHOD AND EVIDENCE. The independent implementation is work/astra_20260929/worker_3/calculation_000009.py, SHA256 526cc5c4481eeb381dd2ba4c631109be05de153f4faa0e74c1b5c609ce81c117. It builds falling polynomials by successive multiplication by their linear factors, retaining full degree. There are 784 outer pairs per disk. For denominator d=2^c b!c!, it computes numerator coefficients modulo 2^60, checks divisibility of each residue by 2^{v_2(d)}, divides by this power, and multiplies by the inverse of the odd part of d modulo 1024. The maximum v_2(d) is 50, so the guard modulus preserves every quotient modulo 1024 and makes each divisibility check exact. The R=0 K term is inserted as the integer 2. D_19 factors are formed modulo 1024 after kernel normalization. Polynomial addition and multiplication then preserve the target precision. No interpolation from finitely many evaluations is used.

The preserved execution completed with exit 0, 6268 denominator-divisibility checks, minimum divisibility margin zero, and an empty difference list across all four disks and all five coefficient arrays. Its result is recorded in work/astra_20260929/worker_3/note_000010.md, SHA256 8e82ab239220fe167fdfe6ea1326417d0f6a6c265d2fa4918aac59b25b683fd0. The implementation and this result note have subsequently been inspected; this submission does not assert a second execution.

SCOPE AND UNRESOLVED DEPENDENCIES. Agreement is an exact finite computational certificate, pending independent review. Extending these coefficients to infinite restricted analytic germs requires separate coefficientwise outer and inner tail estimates. Root factorization, identification of an exact root with index 1, actual reduced-denominator transfer, prime contributions at 5 and 13, and bounds on ordinary integer approximation to the exceptional dyadic root are not certified here. No rationality or irrationality conclusion for e+pi is claimed.