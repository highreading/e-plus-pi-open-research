> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Applicability check for complex-logarithm theorems at the shared 5-adic endpoint

Primary review: main Codex. October 4, 2026. This checks the project's specific application of published theorems, without claiming to reprove Matveev's main theorem in full.

Use Min Sha, *Effective results on the Skolem Problem for linear recurrence sequences*, arXiv:1505.07147v6, October 2, 2018, §2.4, formula (2.19). Full original PDF SHA-256: `b3a67f64dc3907e0e80b53069d313b21272db516729afd3db40f2ac5346703d2`. The primary agent read complete §2.4 and relevant absolute-height definitions and viewed the original formula page. Direct source: [the pinned version](https://arxiv.org/pdf/1505.07147v6).

The original theorem is E. M. Matveev, *An explicit lower bound for a homogeneous rational linear form in the logarithms of algebraic numbers. II*, Izvestiya: Mathematics 64:6 (2000), 1217–1269, Corollary 2.3. The primary reviewer read complete §§2,21 and parameter definitions on printed pages 1217–1218. The original image on PDF page 3 clearly shows Λ≠0. The English full text was retrieved with default TLS verification from the [official MathNet resource](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=314&what=fullteng), 53 pages, SHA-256 `e395e4698837950b683362558441e1e75298ad28cb0cc8cf260a556c93093574`.

The corollary permits a number field embedded in C and arbitrary fixed nonzero logarithm values. Each A_j≥max{D h(α_j),|log α_j|,0.16}; B for the integer coefficients can be replaced by their maximum absolute value B*. The linear form must be nonzero. The more generous constant 2^(6k+20) is used without optimizing other constants. The linear-independence condition in Theorem 2.1 is not an additional condition of Corollary 2.3.

The project takes Z=4+4r−i(r+2), z=2+i, d=r+1, W=Z z^d, and Y=Im W, for odd r≥1 with 5 not dividing r. The verified Gaussian endpoint formula makes Y odd and not divisible by 5, so Y≠0. Set ξ=Z/conj Z and ζ=z/conj z=(3+4i)/5; then



$$
\xi\zeta^d-1=\frac{2iY}{\overline W}\ne0.
$$



The three α=(ξ,ζ,−1) lie in Q(i), with D=2. Their principal logarithms are nonzero: Z has nonzero imaginary part, so ξ≠1; ζ≠1; log(−1)=iπ. Choose integer a to shift the phase into the principal interval. Then Λ=log ξ+d log ζ+2a log(−1), |2a|≤d+2, and exp Λ≠1, hence Λ≠0. The original theorem permits the last integer coefficient to be zero.

The primitive minimal polynomial of ζ is 5X²−6X+5, with both roots of modulus 1, so h(ζ)=log5/2. Z is a Gaussian integer with h(Z)=log|Z|. Height product/inverse inequalities give h(ξ)≤2h(Z)=log(17r²+36r+20). One may choose A_1=O(1+log r), A_2,A_3=O(1), and B*=O(d). Thus |Λ|≥exp[−C(1+log(r+2))²] for an effective absolute constant C.

If |ξζ^d−1|≤1/2, the principal log(1+u) has modulus at most 2|u|, giving |Y|≥|Z|5^(d/2)exp[−C(1+log(r+2))²]/4. Otherwise |Y|>|Z|5^(d/2)/4 follows directly. Combining this with the modulus upper bound gives the exponential leading order of the complete endpoint quantity, rather than an estimate for one incomplete endpoint term.

Reading limits: Matveev plain-text extraction loses the ≠ glyph in several places; original images govern. A final constant-comparison display in §21 also uses min/max differently from the §2 statement. This application uses published Corollary 2.3 and Sha's exact restatement, rather than treating that extracted/typographic line as an independent constant proof. Full review of every intermediate lemma in the external paper is not claimed.

This check supports endpoint-phase and grid-width conclusions for the shared 5-adic correction. It supplies no error lower bound for the selected nearest grid point and does not solve simultaneous control of complete error, final denominator, and nonvanishing.
