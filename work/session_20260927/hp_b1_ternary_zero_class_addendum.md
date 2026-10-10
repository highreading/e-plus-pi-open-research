> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The second ternary residue class for the actual b=1 denominator

Date: 2026-09-27. Author: audit_computations.
Status: original short continuation, awaiting independent review.

Retain exactly the actual endpoint quotient, factorial sums and notation
of `hp_b1_ternary_actual_denominator.md`. No new normalization is used.

For every n>=3 with n=0 modulo 3,



$$
v_3(\mathscr U_n)=-2v_3(n!),
 \qquad \mathscr U_n=2K_{n+1}S_n-(n+1)H_nS_{n+1}.
 \tag{1}
$$


Consequently, whenever Delta_n!=0,



$$
\boxed{v_3(q_n)=2v_3(n!)+v_3(\Delta_n)\ge2v_3(n!).}    \tag{2}
$$


Here Delta_n is an integer, and is in fact divisible by 3. Its eventual
nonvanishing is already proved by the degree-one analytic endpoint
theorem. The present note makes no claim about all-index nonvanishing
within this class.

The proof is a finite residue calculation on the actual sums. In the
sum for mathscr A_n, every s>=1 has (n)_s divisible by 3, so
mathscr A_n=D_(2n)=1 modulo 3 and H_n=1 modulo 3.
For mathscr B_n, only s=0,1 can survive: s>=2 has
(n)_(s-1) divisible by 3. Its two surviving terms are



$$
2D_{2n+1}+(2n+1)a_1(n+1)D_{2n}=2\cdot2-1=0\pmod3.
$$


Deleting D from the same formula gives K_(n+1)=2-1=1 modulo 3.
Thus



$$
(H_n,K_{n+1},\mathscr A_n,\mathscr B_n,\mathscr C_n)
      =(1,1,1,0,1)\pmod3.                             \tag{3}
$$


In particular the normalized numerator mathscr C_n is a unit.

For n=3, 2v_3(n!)=2>floor(log_3(n+1))=1. For n>=6,
the same elementary argument as in the main ternary note proves
2v_3(n!)>floor(log_3(n+1)): the floor-log value 1 is immediate,
the value 2 gives 2floor(n/3)>=4, and larger values a give
2floor(n/3)>=2(3^(a-1)-1)>a.
Therefore the scaled rational second-kind part vanishes modulo 3,
and (3) proves (1). Reduction of the actual rational endpoint proves (2).

For completeness, the Lucas factorization gives
P_(n+1)=-P_n modulo 3 when n=0 modulo 3. Equation (3) then
gives Delta_n=P_(n+1)-2P_n=0 modulo 3, consistent with (2).
No upper bound for this additional denominator valuation is needed.

Combining (2) with the all-even dyadic numerator theorem in
`hp_b1_dyadic_numerator_and_six_class_exclusion.md` gives the same
primitive exponential lower rate



$$
\liminf_{\substack{n\to\infty\\n=0\ (6)}}
 \frac{\log|\mathcal L_n|}{n}
 \ge\log(18\sqrt2-24)>0.                               \tag{4}
$$


Together with the reviewed n=2 ternary class and the dyadic result,
this excludes shrinking on the two even residue classes n=0,2
modulo 6. It leaves n=4 modulo 6 and all odd indices open.

The remaining ternary class has a genuinely different local algebra:
at n=1 modulo 3, H_n and K_(n+1) both vanish modulo 3.
The existing unit-eight theorem gives
v_3(K_(n+1))=v_3(n-1), but no one-layer unit argument for
mathscr C_n follows, since both summands defining it vanish.
That higher-precision cancellation is not assumed away here.
