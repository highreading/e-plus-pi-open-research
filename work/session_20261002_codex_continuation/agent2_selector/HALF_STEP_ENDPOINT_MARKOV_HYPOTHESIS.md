> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Endpoint-row positive Markov representation: a targeted hypothesis

2026-10-02. Original continuation of the positive-gauge two-state reduction. The proposed stronger identity would represent the actual normalized complex endpoint coefficient as a positive Cauchy moment on [0,1]. It is a hypothesis only, and its necessary sector condition is tested before attempting a uniform proof.

Archive searches for Markov, Stieltjes, Cauchy transform and positive measure in the preceding two-scalar determinant note, softened-singularity endpoint note, and current selector work found no positive Cauchy representation of the actual half-step endpoint row. An initial shell glob named no existing period file and was corrected to explicit files; no conclusion is based on that failed command. Existing positive-period results concern the slow column and do not supply the desired endpoint representation.

Online primary search: `Van Assche Pade approximation orthogonal polynomials Markov functions Cauchy transform arxiv`. Opened full primary paper Walter Van Assche, *Padé and Hermite–Padé approximation and orthogonality*, https://arxiv.org/pdf/math/0609094. Its positive-measure Cauchy-transform setup is classical overlap. No theorem in it identifies the current row k(h).

Let k_+(h)=k_A(h)+i k_B(h), the coefficient multiplying (1−i)^h in the exact positive-gauge K_h. The endpoint asymptotic in the algebraic block proof gives

    k_+(h)~γ_n(z_+−1)h^(−r)/(c_n/4).

Define

    g_n(h)=k_+(h)(c_n/4)/[γ_n(z_+−1)].

The candidate representation is

    g_n(h)=−i∫_0^1 t^h dμ_n(t)/(z_+−t),

possibly times a positive scalar normalization with μ_n a positive measure. Such a representation forces g into the fixed closed sector Re g≥0, −Re g≤Im g≤0, because z_+=1−i and 0≤t≤1. It would restrict the adjacent endpoint phase sufficiently to exclude a zero two-output Casoratian under an appropriate strict support condition.

The following exact experiment checks this NECESSARY sector condition for the actual n=4,8 rational rows on the whole nonnegative axis. It is not another sampled W check. Failure would reject this specific representation rather than disprove all positive representations or the constant-shift conjecture. A positive sector test alone would not prove existence of μ_n.

## Exact rejection of this particular representation

`check_half_step_markov_sector.py` derives k from the actual saved output row, uses the exact endpoint derivative to compute gamma, and checks the necessary sector at h=0 before attempting an all-axis sign test. The exact evidence is saved in `half_step_markov_sector.json` and its log. Already at n=4,

    Re g_4(0)=−5128368245/2448023228928<0.

At n=8 the real part is positive but

    Im g_8(0)=53357489550380819601655 /
                               204129692534100054395818647552>0.

Thus the proposed fixed positive Cauchy-moment representation with the stated phase normalization fails. There is no reason to perform the larger all-axis test after these exact necessary-condition failures. This rules out this specific simple mechanism, not uniform Casoratian nonvanishing or a representation with additional signed/algebraic terms. The positive-gauge reduction and the proved algebraic block theorem are unaffected.
