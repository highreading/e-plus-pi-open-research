> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Power-of-two total depth with a convergent inverse-critical 20-lattice

2026-10-02. Original analytic theorem and compatibility handoff, Agent 3. Root/Agent 1 own the new complete 5-adic denominator theorem; Agent 2 owns the reflected projection/dyadic arithmetic and period-preserving rational correction. No arithmetic theorem is independently audited or rederived here.

## Fresh gate

Archive searches covered `(power.of.two|2^s|2^k).{0,40}(critical|round|inverse|reflection)`, `inverse.{0,30}critical`, `n.{0,15}multiple.{0,6}20`, and n congruent to 20 patterns. The returned old congruence-class hits concern prime-index p mod20 in other constructions, not this inverse-critical n-rounding. Read the current reflected exact family and current quadratic/lattice notes as exact internal overlap. The old fixed-n nearest-N rule cannot be substituted for this new fixed-N rounding argument. Search absence makes no global novelty claim.

Fresh primary queries:

- `site:arxiv.org Hermite Pade exponential approximation multiindex uniform nearby`
- `site:arxiv.org asymptotic inversion saddle point integer rounding uniform parameter`
- `site:arxiv.org rational approximation exponential common denominator multi index`

Opened full primary Kuijlaars, Stahl, Van Assche, Wielonsky, https://arxiv.org/pdf/math/0510278, and Dunster, Gil, Segura, https://arxiv.org/pdf/1705.01190. Uniform approximation/saddle and simultaneous Laguerre parameter methods overlap. Neither directly provides the present arithmetic-index subsequence. The proof uses the already authored UNIFORM actual-center expansion plus elementary inversion and a bounded-index rounding calculation.

## 1. Exact inverse leading curve

Fix N_s=2^s, with s tending to infinity. For real t>0 put R_t=sqrt(N_s/t), and define

    Psi_s(t)=t/R_t-2R_t+log(R_t/(4t))
            =t^(3/2)/sqrt(N_s)-2sqrt(N_s)/sqrt(t)
                         +(1/2)log N_s-(3/2)log t-log4.       (1)

Let t_s be the unique root of Psi_s(t)=0 in a neighborhood of x_s=sqrt(2N_s). This root is well defined for every sufficiently large s. Indeed Psi_s(x_s)=-(1/2)log x_s-log(4sqrt(2))<0, its fixed-N derivative is

    Psi_s'(t)=3/(2R_t)+R_t/t-3/(2t),                         (2)

which is positive and asymptotic to 2sqrt(2)/sqrt(t) throughout that neighborhood. Its variation over a displacement of order sqrt(x_s)log x_s is controlled by differentiation. It crosses zero once, with

    t_s=x_s+[sqrt(x_s)/(2sqrt(2))]
                       [(1/2)log x_s+log(4sqrt(2))]
                       +O(log² x_s).                         (3)

The exact implicit curve (1) retains the varying prefactor R/(4n). Replacing that prefactor by its limit still gives convergence but loses a logarithm in the quantitative error bound. This is why the curve in (1), rather than only a fixed limiting ratio, is used here.

Choose

    n_s=20·nearest_integer(t_s/20),
    h_s=N_s-n_s.                                             (4)

Either choice at a tie is allowed. Then |n_s-t_s|<=10, n_s is a positive multiple of20, h_s is positive and divisible by4, and h_s>=6 eventually. Moreover

    n_s~sqrt(2N_s), N_s/n_s²->1/2,
    Psi_s(n_s)=O(n_s^-1/2).                                  (5)

The last estimate follows directly from (2) and the bounded rounding in (4). The slope has order n^-1/2; it is not the fixed-n depth slope of order n^-3/2.

## 2. COMPLETE analytic center on this subsequence

Use the actual reflected kernels and projection at n=n_s, h=h_s, N=N_s:

    F0=(1-2w+2w²)^N/[w^(N+1)(1-w)^h], F1=wF0,
    Ri=Res0 Fi-Res1 Fi,
    Ai=Res1(e^(w-1)Fi), Bi=Res0(e^w Fi),
    T=(h-1)!, mi=T(Ai-Ri), F=m1F0-m0F1,
    U=T(A1R0-A0R1)>0.

The uniform quadratic theorem gives, with R=sqrt(N/n), lambda=N/n²,

    alpha=e [R/(4n)] exp[n/R-2R](1+O(n^-1/2))
             -exp[-R+1/4-lambda/4](1+O(n^-1/2)),
    |beta-pi|<=exp[-(n/2)log n+O(n)],
    U/T=2R D A(1+O(n^-1/2)).                                (6)

The FIRST prefactor/exponential product in (6) is exactly e exp(Psi_s(n)). Equations (5)-(6) therefore prove

    alpha_s=e+O(n_s^-1/2),
    beta_s=pi+O(exp[-(n_s/2)log n_s+O(n_s)]),
    c_s=alpha_s+beta_s=e+pi+O(n_s^-1/2)
                            =e+pi+O(N_s^-1/4).              (7)

This is the full actual rational center: the normalization U is nonzero, both exponential poles are retained, and the two primitive endpoints are retained in the beta estimate. The proof does not assume a signed error at the rounded node or a lower bound for its residual.

## 3. Exact arithmetic interface, with attribution

Agent 2's eligible dyadic theorem applies because N=2^s>n and n,h are divisible by4. Its exact conclusion is

    v2(U)=1, tau:=v2(q)=v2(N!)+1=N.                         (8)

Here q is the complete reduced denominator, not its factorial clearer:

    q=N! O_N U/gcd(N! O_N U,
                    O_N[N!B(F)]+N! O_N[4 Im P(a)]).

Agent 1's saved `agent1_arithmetic/REFLECTED_ACTUAL_FIVE_DENOMINATOR.md` has premise n≡0 mod20,h>=6 and conclusion

    b5:=v5(q)=v5(N!)+v5(U)>=N/4-O(log N).                    (9)

All those premises hold in (4). Its attributed receipt is `REFLECTED_ACTUAL_FIVE_DENOMINATOR_RECEIPT.json`; neither theorem nor receipt is independently audited here. The proof of (9) belongs to the arithmetic agent; no raw factorial depth is independently assumed to survive. This note uses that saved COMPLETE-q theorem with attribution.

## 4. Compatibility with the complete period-preserving correction

Use Agent 2's primitive permitted denominator Q(w)=2w²-10w+13, whose two nonreal poles lie off the vertical path. Its derivative-sum correction has zero ordinary and twisted pole residues and therefore preserves the target coefficient/period exactly. Agent 2's `EVEN_LEADING_QUADRATIC_CORRECTION_COST.md`, Sections6–7, supplies the exact formula, including BOTH endpoint contributions.

With tau=N choose admissible odd r=N/2+O(1), 5 not dividing r, d=r+1, and j=2r-1-N>=0. Its scaled rational shift is

    eta=Y/(2^N5^d), Y odd and a5-adic unit.

Writing the OLD actual primitive center c=A_num/(2^N B), B=5^b5 B0 odd, gcd(B0,5)=1, let L=lcm(B,5^d). Choose the known-data dyadic cancellation class

    kY L/5^d=A_num L/B mod2^N,

with 5 not dividing k and |k|<=(5/2)2^N. The corrected actual center is c_k=c-k eta, with exact primitive denominator

    q_k=2^N L/gcd(2^N L,
                         A_num L/B-kY L/5^d).               (10)

The complete signed target error is exactly

    (e+pi)-c_k=[(e+pi)-c]+k eta.                            (11)

The full correction norm estimate gives

    |k eta|<=5(r+1)5^(-r/2)
                =exp[-(log5/4)N+O(log N)].                  (12)

Combining (7), (11) and (12) proves the corrected centers STILL converge:

    |c_k-(e+pi)|<=O(N^-1/4)
                           +exp[-(log5/4)N+O(log N)].        (13)

No sign or relative residual statement is inferred if the old error happens to be smaller than or comparable with the correction quantum.

## 5. What the actual denominator gain does and does not prove

If b5!=d, Agent 2's full reduction gives

    q_k=B0 5^max(b5,d),
    q_k/q=5^max(d-b5,0)/2^N.

Using (9) and d=N/2+O(1),

    q_k/q<=exp[-(log2-log5/4)N+O(log N)].                   (14)

Thus the new actual5 supply yields a genuine primitive denominator reduction, with constant log2-log5/4=0.2907877... positive. If b5=d, retain instead the exact tied reduction

    q_k=B0 5^max(0,b5-v5(A_num-kYB0)),

which can only improve the comparison. The arithmetic numerator content is not discarded.

If a lower bound on the corrected q is needed, select a second admissible odd r within O(1) so that d!=b5; the available choices cannot all equal that one depth. Then

    q_k>=5^d=exp[(log5/2)N+O(1)].                           (15)

The exponentially small real shift in (12) and genuine q gain in (14) therefore coexist with corrected convergence in (13). They do not provide a primitive small-linear-form theorem: (13) is an upper bound of polynomial order, not an exponentially small error compatible with (15). Conversely that polynomial upper bound is not a lower bound for the rounded residual. An exceptionally small old residual or cancellation in (11) remains a distinct question. No rationality statement about e+pi follows from this subsequence or denominator improvement alone.
