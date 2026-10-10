> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Full short-stack factorial content and actual primitive cost

Author theorem, 2026-10-02. The construction is root's M24 short matching stack. General Gamma Gram divisibility and integer basis changes are classical; see the fresh gate. The result below concerns BOTH full determinant coefficients and their FINAL common content. It is not a denominator lower bound or an irrationality theorem.

## 1. Exact pair and normalization

For k>=1, let 0<=i<k, 0<=j<2k, r=i+j, and

    C_ij=D_(2r)-(-1)^r,
    R_ij=-(2r)!+4 sum_(a=1)^r (-1)^(r-a)/(2a-1),
    V_ij=(-1)^r.

Write beta(T)=det[C;R+TV]=beta_0+T beta_1 and

    L_k=lcm(1,3,...,6k-5),
    I_0=L_k^k beta_0,   I_1=L_k^k beta_1.

For k=1 the list ends at 1. Both I_i are integers. Whenever beta_1!=0, the actual reduced denominator and complete primitive error are exactly

    G_k=gcd(I_0,I_1),
    q_k=abs(I_1)/G_k,
    q_k abs(S-c_k)=L_k^k abs(beta(S))/G_k,
    c_k=-beta_0/beta_1,   S=e+pi.

Using a sufficient clearer does not change this actual pair after the final gcd. In particular the result is independent of a kernel basis and of any individually primitive normalization of its columns.

Put F_s=product_(r=0)^(s-1) r!, with F_0=1. Then, for every k>=1,

    F_(k-1)^2 divides I_0,
    F_k^2 divides I_1.

Consequently F_(k-1)^2 divides G_k. The asymmetric second assertion is part of the theorem; an evaluation term has a different effect on the two coefficients.

## 2. An integer Gamma basis

Define the integer-valued moment functional

    mu(P)=integral_0^infinity exp(-t) P((1-t)^2) dt.

The elementary endpoint expansion gives mu(y^r)=D_(2r). Apply the lower unitriangular binomial transform to the k TOP rows and the corresponding unitriangular column transform to ALL 2k columns. These replace y^i and y^j by (y-1)^i and (y-1)^j. Their determinants are 1; the lower row polynomials need not be changed. The transformed top block is

    A_ij-a_i b_j,
    A_ij=mu((y-1)^(i+j)), a_i=(-2)^i, b_j=(-2)^j.

Indeed evaluation at y=-1 sends (y-1)^j to (-2)^j. The transformed lower response has row i equal to (-1)^i b. The cleared lower regular block remains integral because its columns are integer combinations of the old columns.

For m=i+j, one has the exact finite identity

    A_ij=sum_(s=0)^m binom(m,s)(-2)^(m-s)(m+s)!.

It follows that m! divides A_ij, hence i! j! divides A_ij. Thus every d by d minor of A with row set H and column set J is divisible by

    product_(i in H) i! product_(j in J) j!.

For any increasing d distinct nonnegative indices j_0<...<j_(d-1), j_a>=a, so F_d divides their factorial product. For d=k and all k top rows the row product is F_k. For d=k-1 obtained by omitting any top row r, the row product is F_k/r!, which is divisible by F_k/(k-1)!=F_(k-1). These statements are integer divisibility, not estimates involving ratios of real determinants.

## 3. Constant coefficient and response coefficient

Expand the transformed top block A-ab in its rank-one perturbation. Any term replacing two top rows vanishes because the two replacement rows are proportional to b. The term retaining all k Gamma rows is divisible by F_k^2: expand along those rows and apply the minor divisibility. Each term replacing one top row retains k-1 Gamma rows, and expansion along them gives divisibility by F_(k-1)^2. All other rows are integral after the same L_k lower clearing. This proves the stated divisor of I_0.

For the coefficient of T, multilinearity replaces exactly one lower row by its response (-1)^i b. Two lower response replacements vanish. Once this lower response row occurs, every top-row evaluation replacement also vanishes because it duplicates a row proportional to b. Therefore I_1 is the sum of terms with ALL k Gamma rows retained. Expansion along those k rows gives the stronger factor F_k^2. No division by beta_1, by a moment, or by an error was used. Zero coefficients are covered by the integer divisibility statement.

Equivalently there are integers A_k,B_k such that

    I_0=F_(k-1)^2 A_k,
    I_1=F_(k-1)^2 (k-1)!^2 B_k,
    q_k=abs((k-1)!^2 B_k)/gcd(A_k,(k-1)!^2 B_k).

This last expression is an exact primitive interface. It does NOT imply that the remaining factorial factor survives: A_k can share it, and the complete gcd remains decisive.

### A stronger simultaneous dyadic factor

The exact moment recurrence in EVEN_GAMMA_ODD_SATURATION.md gives integers U_m=a_m/(2^m m!) with U_0=1,U_1=0 and U_(m+1)=(2m+1)U_m+U_(m-1). Therefore in the same top binomial basis both the Gamma entry and its evaluation perturbation have the factors 2^i and 2^j. Factor these from every row and selected column of a top minor before expanding its rank-one evaluation. The row sum is k(k-1)/2, and every selected set of k column indices has sum at least k(k-1)/2. The remaining Gamma rows and columns retain the factorial divisibility used above. Thus the stronger COMPLETE assertions are

    2^(k(k-1)) F_(k-1)^2 divides I_0,
    2^(k(k-1)) F_k^2 divides I_1.

The evaluation row shares the dyadic row/column factors, so the dyadic exponent loses no row even in the constant term. This is a simultaneous product divisor, not the maximum of two independently overlapping divisors. It supplies an additional exp[(log 2)k^2+O(k)] reduction of the actual coefficient-cost ceiling. The exact final gcd after this division remains required. Since W_k is odd and has primes above 4k, it remains coprime to the entire displayed factor.

## 4. Independent upper-prime content

The earlier all-degree Laurent theorem proves the simultaneous divisor

    W_k=product_(4k<p<6k-5) p^((p-4k+3)/2)

of I_0 and I_1. Its primes are >4k, whereas every prime of F_(k-1) is <=k-2. The factors are therefore coprime, and

    F_(k-1)^2 W_k divides G_k,
    q_k <= abs(I_1)/(F_(k-1)^2 W_k).

There is no overlap subtraction or double counting. Neither factor determines any further specialized gcd or any surviving prime of q_k.

## 5. A smaller all-degree size ceiling

The full matching of columns in each determinant term improves the earlier separate-entry Hadamard ceiling. Every entry except the one response entry is bounded by 3(2r)!; the response entry has absolute value 1. For a permutation term, the sum of r=i+j over ALL 2k rows before its response replacement is

    2 sum_(i=0)^(k-1) i + sum_(j=0)^(2k-1) j = 3k^2-2k.

Omitting the response row's nonnegative r can only decrease this sum. Since 2r<=6k-4, one obtains the exact safe bound

    abs(I_1) <= L_k^k k (2k)! 3^(2k-1) (6k-4)^(6k^2-4k).

Together with the full content theorem this gives an explicit ceiling with division by F_(k-1)^2 W_k. The classical log lcm(1,...,x)=O(x) and Stirling summation yield

    log F_(k-1)^2 = k^2 log k - (3/2)k^2 + O(k log k),
    log q_k <= 5 k^2 log k + O(k^2).

The classical PNT refinement from the already-read Rosser--Schoenfeld paper gives log W_k=k^2+o(k^2), as recorded in the Laurent note. It affects the second-order cost, not the leading 5 k^2 log k ceiling. These are upper bounds, not predictions of actual growth.

Analysis's complete M24 theorem gives log(S-c_k)=-4k log(1+sqrt(2))+O(log k) for sufficiently large k, with beta_1 nonzero. This error can be combined with the actual q_k, but the present upper ceiling is much larger than the error scale. The theorem establishes a genuine reduction in complete coefficient cost; it does not show that q_k(S-c_k) tends to zero or diverges. The unresolved arithmetic is further FINAL common content after the two proved factors, or a structural actual denominator estimate at the linear-in-k scale.

## 6. One exact normalization receipt

The new script `short_stack_factorial_receipt.py` performs one k=5 normalization test, rather than extending the old degree/prime atlas. It checks both integer binomial transforms, the exact Gamma finite-sum identity, every relevant k or k-1 Gamma minor (1302 checks), the two full determinant coefficients, affine dependence at T=0,1,2, and invariance of the FINAL primitive pair after the common factorial division. All assertions passed. The actual q has 308 bits, matching the already-saved root k=5 value; the theorem changes a provable bound, not this pre-existing reduced rational center. Results are saved in `SHORT_STACK_FACTORIAL_RECEIPT.json`.
