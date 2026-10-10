> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the added-column endpoint theorem

Date: 2026-09-13. Reviewer: audit_results.

Target: raw_dual_endpoint_added_column_dyadic.md by audit_sources, verifying root's added-column proposal.
Verdict: FULL PASS, including the stronger congruence and every consequence in Section 5. No correction required.

## 1. Exact determinant sign and factorial

Expanding the last column of [X_n,B_n] gives

    sum_k (k)_n (-1)^(k-n)det X_n[omit k]
       =F_n W_n^(n)(1)=F_n n!V_n(1).

The last column index is 2n, so its cofactor parity is precisely k-n. Moving that column across n arctangent columns changes the sign by (-1)^n. Therefore det M_n=(-1)^n F_n n!V_n(1). There is exactly one n!, arising from the nth derivative at 1.

## 2. Universal minor bounds and the strict cutoff

After division by row factorials, the exponential minor factors as prod_(j=0)^n j!/prod_(k in E)k! times an integer binomial determinant. The binomial determinant on consecutive rows is 1, fixing both equality and sign for that block.

All row exponents in the complementary arctangent minor are k-n>=0. The explicit monic raw Legendre coefficient in the note has valuation

    phi(j)-phi(2a)-phi(j-2a)=v_2 binom(j,2a)>=0.

Thus its basis change and inverse are dyadically integral. The norm formula has valuation 2phi(j). Expansion of arbitrary row monomials in the full monic orthogonal basis shows that every complementary C determinant has valuation at least 2S(n). Equality for row degrees 0,...,n-1 follows from a unit triangular coefficient matrix. No negative moments or missing polynomial degrees occur.

The B row set 2n,...,3n attains both lower bounds. Every other set exchanges at least one row across the cutoff 2n-1/2n, losing at least phi(2n)-phi(2n-1)=v_2(2n)>0. Possible additional cancellations only raise a competing determinant's valuation. The least Laplace term is unique and cannot cancel.

Restoring all row factorials gives

    v_2(det M_n)=3S(n)+phi(n)+sum_(k=n)^(2n-1)phi(k).

Dividing by the exact factor F_n n! proves both endpoint nonvanishing and (7) for every n>=1.

## 3. The stronger congruence

The distinguished C minor is exactly the same in M_n and in the deleted-last-row determinant Delta_n^0. The unscaled consecutive B determinants have ratio n!. The Laplace row/column sign for M_n is +1, while that for Delta_n^0 is (-1)^n. Hence their distinguished terms have ratio exactly (-1)^n n!, not merely that valuation.

In both expansions every competing term is at least g_n=v_2(2n) powers of two deeper. Therefore

    Delta_n^0=L_n(1+epsilon),
    det M_n=(-1)^n n! L_n(1+eta),
    epsilon,eta in 2^g_n Z_2.

The factors 1+epsilon and 1+eta are units because g_n>=1. It is legitimate to divide their ratio in Z_2, even when L_n or the primitive leading coefficient has positive valuation. Substituting det M_n=(-1)^n F_n n!V_n(1) and v_n=Delta_n^0/F_n gives

    V_n(1)/v_n=(1+eta)/(1+epsilon)
        in 1+2^g_n Z_2.

This verifies the stated full congruence and the valuation of V_n(1)-v_n. The n=1 ratio is -1, which is correctly congruent to 1 modulo 2; the congruence does not imply a positive real ratio.

## 4. Full actual Hankel and Toeplitz invertibility

The first n moment rows have rank n and one-dimensional kernel spanned by q_n. The added last row takes value n!V_n(1) on that kernel, now proved nonzero. Hence the full square moment matrix is injective and invertible. Row reversal proves invertibility of the actual Toeplitz matrix A_n in every degree. No separate principal-minor or perfectness assumption enters.

Using q_n(0)=(2n)!v_n in A_n q_n=n!V_n(1)e_0 gives

    (A_n^(-1))_(0,0)=((2n)!/n!)v_n/V_n(1).

The quotient of endpoints is a dyadic unit, and phi(2n)-phi(n)=n. This proves the nonzero inverse corner and its exact valuation n. The leading coefficient of the actual exponential numerator is V_n(1), so its full degree 2n follows as stated.

## 5. Scope and independent consequence for the odd scalar

Only the previously saved n=1 control is needed to check the convention: det M_1=-1, Delta_1^0=-1, F_1=1, V_1(1)=1 and v_1=-1. The all-index proof above does not depend on this control.

The theorem removes the zero obstruction from the scalar s_m in raw_odd_dual_toeplitz_scalar_obstruction.md. With n=2m+1 and its exact factor B_m^odd,

    B_m^odd s_m=V_n(1)/v_n in 1+2 Z_2,
    v_2(s_m)=-1-phi(3m+2)+phi(m).

The valuation follows by applying phi(2n)=n+phi(n) and phi(2m+1)=m+phi(m) to the factorial factor. It supplies no Archimedean sign or size estimate. The outstanding odd-degree target is therefore only log|s_m|=o(m), with nonvanishing already proved.

The added-column theorem passes without a mathematical or wording correction.

