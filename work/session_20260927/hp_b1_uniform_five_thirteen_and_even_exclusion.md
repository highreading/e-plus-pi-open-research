> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Uniform primes 5 and 13 exclude every even index of the b=1 route

Date: 2026-09-27. Assembly by audit_computations.
Status: FULL PASS in `hp_b1_uniform_5_13_independent_review.md`
(audit_results), including the actual prime transfer, all-depth lift,
complete finite seeds, and this final all-even synthesis.

## 1. Exact uniform actual-denominator bound

Let q_n be the positive reduced denominator of the actual b=1
endpoint rational number X/Y=A(1)/B(1). Its normalization is fixed in
`hp_b1_ternary_actual_denominator.md`, and was already independently
checked against the original endpoint kernel in the prior session.
For every n>=13 with Delta_n!=0,



$$
\boxed{v_5(q_n)\ge2v_5(n!),\qquad v_{13}(q_n)\ge2v_{13}(n!).}
 \tag{1}
$$


The accepted analytic endpoint theorem supplies Delta_n!=0 for every
sufficiently large n, so this is a uniform asymptotic statement on
both parities.

Proof: fix p=5 or13. The complete seed certificate and all-residue
transfer in `hp_b1_prime_seed_transfer_and_closed_atlas.md` show
mathscr C_n is a p-unit unless n=1 modulo p. In the unit case,
the exact Rodrigues numerator and the strict second-kind separation
give v_p(mathscr U_n)=-2v_p(n!). Since Delta is integral, actual
rational reduction gives v_p(q_n)>=2v_p(n!).

For n=1 modulo p, set a=v_p(n-1). The analytic residue-one theorem
in `hp_b1_residue_one_actual_numerator.md`, Sections 1-2, proves
v_p(mathscr C_n)=a and v_p(H_n),v_p(K_(n+1))>=a. Thus
v_p(Delta_n)>=a and v_p(mathscr Q_n)>=a-floor(log_p(n+1)).
For n>=p, 2v_p(n!)>floor(log_p(n+1)); the factorial term of the
actual numerator consequently has uniquely least valuation
a-2v_p(n!). It follows exactly that



$$
v_p(q_n)=2v_p(n!)+v_p(\Delta_n)-a\ge2v_p(n!).
$$


This proves (1) in every residue. It includes the endpoint numerator
cancellation; no coefficient clearer or unreduced endpoint height is
used as a replacement for q_n.

## 2. All-even divergence of the actual primitive forms

The independently passed dyadic theorem is



$$
v_2(q_n)\ge2v_2(n!)-n/2\quad(n\ge2\text{ even},\ \Delta_n\ne0).
$$


The three prime factors belong to the same reduced denominator, hence
for all sufficiently large even n,



$$
2^{\,2v_2(n!)-n/2}5^{\,2v_5(n!)}13^{\,2v_{13}(n!)}\mid q_n.
 \tag{2}
$$


Therefore



$$
\liminf_{\substack{n\to\infty\\n\text{ even}}}\frac{\log q_n}{n}
 \ge d_{\rm even}:=\frac32\log2+\frac12\log5+\frac16\log13.
 \tag{3}
$$


The exact b=1 error theorem from the preceding session is



$$
\log|\mathcal L_n|=\log q_n-2n\log(1+\sqrt2)+o(n),
 \tag{4}
$$


where mathcal L_n is the actual gcd-reduced integer form in e+pi.
Combining (3)-(4) gives



$$
\boxed{\liminf_{\substack{n\to\infty\\n\text{ even}}}
 \frac{\log|\mathcal L_n|}{n}
 \ge d_{\rm even}-2\log(1+\sqrt2)>0.}                   \tag{5}
$$


For an exact positivity certificate, exponentiate six times the
inequality. Its left side is 2^9 5^3 13=832000, while
(1+sqrt2)^12=19601+13860sqrt2<19601+27720=47321.
Thus the claimed gap is strict without decimal logarithms.

Every even subsequence of this fixed b=1 construction therefore has
growing primitive forms. This does not rule out odd subsequences,
other degree allocations, or other constructions, and does not prove
irrationality of e+pi.

## 3. Dependencies and reproducibility

* `hp_b1_ternary_actual_denominator.md`: exact actual numerator and
  Rodrigues contractions, independent FULL PASS.
* `hp_b1_dyadic_numerator_and_six_class_exclusion.md`: all-even
  dyadic numerator valuation and reduced-q lower bound, root FULL PASS.
* `hp_b1_prime_seed_transfer_and_closed_atlas.md`: all-residue transfer
  and complete predeclared prime seeds, independent FULL PASS.
* `hp_b1_residue_one_actual_numerator.md`: analytic root-disk unit
  lift for every p>=5, independent FULL PASS in the same review.
* `../session_20260913/hp_b1_endpoint_attempt.md`: actual nonvanishing
  and primitive evaluated-error exponent, independently reviewed.

The finite seed checker is `check_hp_b1_predeclared_prime_seeds.py`.
The separate exact rate checker is
`check_hp_b1_closed_prime_rate_and_crt.py`; its output also records
the odd-index CRT calculation in the accompanying note.
