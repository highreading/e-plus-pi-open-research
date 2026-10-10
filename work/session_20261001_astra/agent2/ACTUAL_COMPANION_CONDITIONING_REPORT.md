> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Report: actual companion conditioning

The application completed the exact extraction for precisely n=4,6,8,10. companion_conditioning_extraction.json contains every primitive antisymmetric matrix, kappa_j, absolute row sum, eligible ratio, minimum C, and exact positive/negative cancellation measure. The source certificate was unchanged during execution; source and script hashes are recorded.

The minima are 2009/1021, 694288919809/604385055271, 11033844156019887755931676121/9674460924431872076346352727, and 6411659808416170857457639908203852821320225992509/5652190600327147840051085004116244763851484500379. All lie between 1 and 2, as finite exact statements only.

The all-row coefficient-monotonicity shortcut fails at n=4: |N_02|=1515>1510=|N_01|. The saved exact witness stops that subroute. Row-one first-entry domination holds in all four retained records, but no uniform domination estimate is proved.

A genuinely new actual-family lemma avoids C. On 2<=b<=n and d!=0, define beta=A0 tau_U-A1 tau_P and lambda=N beta/d. Then sum lambda_j=1 and Uhigh lambda=0. For the actual Rodrigues polynomial Pcal_(n+1), put S_lambda=sum lambda_j Pcal_(n+1)^(j) and r=n+1-b. The first high row proves S_lambda(1)=0, while x^r divides S_lambda. Thus G_lambda=S_lambda/[x^r(1-x)] is a rational polynomial of degree at most n+b.

Complete factorial-tail integration and integration by parts give exactly

e+K_tail/d=e/[A1(2n+2)!] integral_0^1 exp(-x)x^r(1-x)G_lambda(x) dx.

Consequently its magnitude is at most e times the supremum norm of G_lambda divided by A1(2n+2)!(r+1)(r+2). The proof retains cancellation before taking absolute values. It uses the actual derivative high row, not abstract rank or primitivity. The conditioning remains in the normalization d inside G_lambda; no favorable uniform norm bound is established.

The actual primitive estimate is |L_int|<=q(epsilon_n/Delta+B_comp). Actual reduced q, projective separation Delta, and complete-remainder nonvanishing must be controlled at the same unbounded indices. These inputs remain unresolved. No shrinking theorem, unbounded sign theorem, or exponential bound for C is inferred from the finite records.

The detailed note records the reviewed derivative/minor dependencies and the required simultaneous transformation of appended rows. No column transformation, new canonical solve, degree extension, prime scan, networking, installation, or edit outside Agent 2's directory was used. Prior corrections and certificates are preserved. All new artifacts are to be verified by read-back before completion.
