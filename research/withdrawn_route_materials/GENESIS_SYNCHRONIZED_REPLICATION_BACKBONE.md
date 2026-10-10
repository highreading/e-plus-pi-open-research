> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Synchronized replication: a classical backbone, not a retained obstruction tool

Status: proved background lemma; Genesis construction remains active. No rationality decision, new general transcendence theorem, or mechanism-level novelty claim is made.

## Actual operation and exact input

The two actual defining laws replicate differently: the exponential value multiplies, while the lifted circular clock adds. For a positive integer m define

    R_m = exp(m) + m · (4 atan(1)) = e^m + m pi.

The circular term is m repetitions of the clock increment pi, not 4 atan(m). The operation is nonadditive in its exponential component. Its initial value is R_1=S=e+pi. Consequently S in Q is exactly the assertion R_1 in Q; no stronger scalar consequence is being assumed.

## Proved exceptional-value lemma

For every complex number y and every transcendental complex number x, at most one positive integer m has

    x^m + m y in Qbar.

Indeed, suppose m != n and a_m=x^m+m y, a_n=x^n+n y are algebraic. Eliminating y gives

    n x^m - m x^n = n a_m - m a_n.

Thus x is a zero of the nonzero polynomial

    n T^m - m T^n - (n a_m - m a_n) in Qbar[T].

A number algebraic over Qbar is algebraic over Q: the finitely many polynomial coefficients lie in a number field, and algebraicity is transitive. This contradicts the transcendence of x.

Taking x=e and y=pi proves that at most one R_m is algebraic. In particular, under S in Q (or even S in Qbar), every R_m with m>=2 is transcendental. This uses the classical transcendence of e; it does not establish that m=1 is nonexceptional.

## Exact polynomial classification

There is a useful general form. Let x be transcendental, let y be arbitrary, and set

    F_i=P_i(x)+c_i y,
    P_i in Qbar[T], c_i in Qbar minus {0}.

If F_i and F_j are algebraic, then

    P_i/c_i - P_j/c_j

is a constant polynomial. Conversely, if this difference is constant, algebraicity of either F_i or F_j implies algebraicity of the other. To prove the first direction, eliminate y and apply the previous polynomial argument. Thus all algebraic F_i belong to one equivalence class of normalized polynomials modulo constants. Synchronized replicas correspond to P_m=T^m,c_m=m; their classes are pairwise distinct.

This classification is ordinary algebra over the algebraic numbers. It is credited background, not an invented discrete invariant or a new Genesis theorem.

## Archive and primary gate

The bounded archive search covered all Markdown files under `[private local path removed]`, with the exact fragments `e^m+m`, `e^n+n`, `e^k+k`, and the mechanism words `replica`, `replication`, `synchronized`, `synchronised`. The synchronization matches concern the old approximation/content route, not this replication lemma. A separate classical-core search for Lindemann-Weierstrass and transcendence of e located the already used exponential transcendence background.

Relevant archive files read for the mechanism boundary were `sources/e_function_logarithm_exceptional_set_no_go.md`, especially its exact exceptional-point and algebraic-scalar discussion, and the introductory scope and logarithmic setting of `sources/exponential_theorem_audit.md`. They explicitly warn that further conditional transcendence consequences are compatible with S being algebraic. This note does not reopen those routes and is not an independent audit.

Fresh public queries included:

- `Hermite 1873 Sur la fonction exponentielle original pdf e transcendental`
- `Lindemann Weierstrass 1885 Über die Zahl e original paper pdf`
- `"e^n" "n pi" transcendental`
- `"exponential polynomial" "algebraic values" Lindemann Weierstrass`
- `"exponential" "replication" "additive" "clock" mathematics`

The primary proof paper Sever Angel Popescu, *A simple and self-contained proof for the Lindemann-Weierstrass theorem*, was opened in full HTML at https://arxiv.org/html/2306.14352v2 and its Theorem3.2 and Corollary3.2 were inspected. Corollary3.2 gives transcendence of exp(alpha) for nonzero algebraic alpha, hence of e. Historical Hermite sources were located in the search, but their full original texts were not read here and no claim is imported from an unseen text. No technical result from secondary search hits is used.

Gate conclusion: the exceptional-value lemma and polynomial classification have an explicitly classical essential core. They are NOT retained as a new proof mechanism. No unsuccessful search is promoted as global novelty. They can serve as background inside a genuinely new operation if such an operation is later constructed and separately gated.

## Precise unresolved transfer

A contradiction would follow from a separately proved operation that, under R_1 in Q, forces an algebraic F=P(e)+c pi whose normalized polynomial P/c is nonconstant modulo T. For example, forcing any R_m with m>=2 to be algebraic would suffice. No such operation has been constructed or proved.

Rationality of R_1 alone does not give algebraic closure of synchronized replicas. In fact the proved lemma says all other replicas must be transcendental under that hypothesis. The desired second-exception transfer is not asserted as an axiom, as a source symmetry, or as a general conjecture without hypotheses. It remains the concrete missing construction.

Research continues beyond this background checkpoint. No main proof or research stop is declared.
