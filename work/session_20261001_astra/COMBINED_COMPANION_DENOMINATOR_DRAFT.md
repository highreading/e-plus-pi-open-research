> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Combined rational companion: the cancellation-sensitive height budget

Status: new main-agent author deduction, not independently reviewed. This preserves the previously unsaved refinement of DIRECT_SELECTOR_HEIGHT_OBSTRUCTION_DRAFT.md. It is a necessary arithmetic budget, not an irrationality proof.

Use that note's primitive integer selector L, height H, integer polynomial K, and nonzero forcing normalization U=K(1), A=|U|. Write the complete rational center as

    c=r+alpha+beta,
    q=den(c), B=den(r+beta).

Here alpha is the rational exponential companion, beta the rational logarithmic companion, and r a rational endpoint correction. The complete exponential estimate is

    0<|e-alpha|<=27(2M)^n H/[(n+1)n!A],
    M=1+sqrt(2).

Since alpha=c-(r+beta), its actual reduced denominator is at most qB. The saved elementary approximation bound for e gives, for every epsilon>0,

    q^(2+epsilon)>=C_epsilon (n+1)n!A/
                     [27(2M)^n H B^(2+epsilon)],

and therefore

    (2+epsilon)log q>=log(n!)-log(H/A)
                       -(2+epsilon)log B-O_epsilon(n).   (1)

No degree estimate is needed in (1): any degree cost is contained in the actual H/A and B. This is stronger than replacing B by a product of separate correction and logarithmic denominators. It retains their cancellation exactly. The ratio H/A is invariant under common scaling of the selector.

For an explicit formula, let g be the positive coefficient gcd of K, write K0=K/g and U0=K0(1), and choose any positive integer D clearing the required moments. Then

    J=D calL((K0-U0)/(t-1)) is an integer,
    beta=J/(D U0).

If r=a/v in lowest terms with v>0, the actual combined denominator is

    B=vD|U0|/gcd(vD|U0|,|aD U0+vJ|).                  (2)

The zero numerator case is included and gives B=1. Enlarging D changes numerator and gcd together and cannot improve B. Formula (2) does not assume that any of its separate factors are coprime.

If log(H/A)=O(n) and log B=o(n log n), equation (1) implies

    liminf log q/(n log n)>=1/2.

This remains true for a factorial-height primitive selector if its normalized cost H/A is only exponential. If additionally the complete error is eventually nonzero and its logarithm is bounded below by -O(n), its primitive forms diverge. A substantially smaller complete error is not excluded.

Conversely, if log q=O(n), log B=O(n log n), and |log(H/A)|=O(n log n), then (1), applied for every fixed epsilon>0, forces

    liminf [log(H/A)+2log B]/(n log n)>=1.             (3)

Thus a large endpoint-correction denominator only helps avoid this obstruction if it survives the actual sum r+beta. It cannot be counted before the gcd in (2).

For reconstructed coordinate centers, the rational selector row and the endpoint correction must first be derived from the actual lift. A nonzero coordinate j>0 has no endpoint correction; coordinate zero generally does. The B-only Gram center has its own correction. These centers need not coincide, and their combined denominators cannot be interchanged.

The exact interface (1)-(3) is now available to the researchers studying primitive selector heights and eligible coordinate gcds. It supplies no actual asymptotic estimate for their combined denominator or signed error. The e+pi question remains open.
