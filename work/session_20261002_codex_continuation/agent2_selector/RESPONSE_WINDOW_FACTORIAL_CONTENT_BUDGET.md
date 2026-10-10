> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Growing response-changing windows: exact factorial content budget

2026-10-02. Original application to the ACTUAL response-changing e+pi centers. The arithmetic-progression product/lcm bound is classical and explicitly credited; no claim of novelty is made for that lemma. The new target is a uniform growing-window denominator-gain count with complete response/error/coefficient interfaces retained.

## Fresh gate and overlap

Archive queries covered Hong/Qian,0903.0530, product-gcd/lcm factorial budgets, growing response windows and arithmetic-progression least common multiples. No matching prior explicit growing-window statement was returned by the bounded queries. Read the current `RESPONSE_CHANGING_SEED_PRIMITIVE_PROJECTION.md` content/divisor/window statements as internal overlap. The analysis agent suggested the relevant primary source while authoring its DISTINCT complete-error product theorem; that analytic result is not rederived here.

Fresh primary searches concerned arithmetic-progression product/lcm excess and factorial divisibility. Opened Hong–Qian, *The least common multiple of consecutive arithmetic progression terms*, full primary https://arxiv.org/pdf/0903.0530, Lemmas3.2–3.3 and proof, and its level-counting p-adic expression(3.1). Lemma3.3 gives the classical factorial bound for a coprime arithmetic progression, with Lemma3.2 credited there to Farhi/Hong–Feng. The clipped gcd application and actual e+pi-window consequences below are our specific use of that established arithmetic fact.

## 1. Exact ACTUAL centers and content

Let c=p/q be an OLD actual reduced matched center with q positive ODD, gcd(p,q)=1, response U!=0, and put H=p−6q!=0. For any integer K>=1 take a_i=2i,1<=i<=K. The fixed matched seed

    G6=2/w+1/(w−1)−4,
    R(G6)=A(G6)=1,B(G6)=2,Pi(G6)=−8

gives the response-changing kernel F_i=F+(2iU/q)G6 and ACTUAL data

    U_i=U(q+2i)/q!=0,
    c_i=(p+12i)/(q+2i),
    g_i=gcd(q+2i,|H|), q_i=(q+2i)/g_i,
    q_i(S−c_i)=[q(S−c)+2i(S−6)]/g_i.                    (1)

Every primitive denominator q_i is odd. No coefficient clearer replaces the actual gcd in(1), and no error is divided out.

## 2. Factorial divisibility, valid for every K

The EXACT clipped-content identity is

    [product_(i=1)^K g_i]/lcm(g_1,...,g_K) divides(K−1)! .  (2)

Proof. There is no2-content because every q+2i is odd. For an odd prime l, choose an index i0 where v_l(g_i) is largest. For i!=i0,

    v_l(g_i)<=min(v_l(q+2i),v_l(q+2i0))
                  <=v_l(2(i−i0))=v_l(i−i0).

The first inequality holds even if the actual clipped maximum is tied: g_i divides both H and its progression term, and v_l(g_i0)>=v_l(g_i). The second follows by subtracting the progression terms. Summing the other valuations gives at most

    v_l((i0−1)!(K−i0)!)<=v_l((K−1)!),

because the corresponding binomial coefficient is an integer. This proves(2), prime by prime. It is the usual arithmetic-progression factorial bound adapted to valuations clipped by H, consistent with the opened primary Lemma3.3.

Since lcm(g_i) divides|H|, the COMPLETE actual content budget is

    product_i g_i divides(K−1)!|H|,
    product_i g_i<=(K−1)!|H|,
    product_i q_i>=product_i(q+2i)/[(K−1)!|H|].            (3)

This replaces the much larger fixed-block pairwise-difference majorant. It remains valid for K depending on q and for any actual zero numerator in a new center. The case H=0 is excluded from(2)–(3): it means old c=6, so all new centers are6 and their complete errors are nonzero because S!=6; it is absent eventually on a sequence converging to S.

## 3. Quantified number of large denominator gains

For G>1 let J(G) count the indices with g_i>=G. Equation(3) proves

    J(G)<= [log|H|+log((K−1)!)]/log G.                    (4)

In particular, a node with q_i<=q^(1−epsilon),0<epsilon<1, has g_i>=q^epsilon since q+2i>=q. Its count therefore obeys

    # {i:q_i<=q^(1−epsilon)}
       <=[log|H|+log((K−1)!)]/[epsilon log q].             (5)

Suppose c→S=e+pi, q→infinity, and

    K log(K+1)=o(log q).

Then |H|=q|c−6|~(6−S)q and log|H|=log q+O(1), so

    # {i:q_i<=q^(1−epsilon)}<=1/epsilon+o(1).              (6)

For fixed epsilon the integer count is eventually at most floor(1/epsilon). Thus a window whose length tends to infinity can contain only a bounded number of outputs with a fixed positive-power denominator saving. This is a GLOBAL actual-content assertion; it does not rely on survival of any fixed prime after the response change.

Equation(6) does NOT exclude those bounded exceptional outputs, or an infinite sequence selecting one such output at each OLD index. It is not a lower bound for the smallest actual q in the window, and no sparsity statement is substituted for the missing selected-node theorem.

## 4. Denominator rates and the whole complete-error window

Taking logarithms in(3),

    (1/K)sum_i log q_i
       >=log q−log|H|/K−log((K−1)!)/K.                   (7)

A useful explicit window is K=floor(sqrt(log q)), for sufficiently large q. Then all but a bounded number of nodes have q_i>q^(1−epsilon), and the geometric mean is at least

    q exp[−sqrt(log q)−O(log log q)].                     (8)

Thus the leading logarithmic denominator rate is unchanged over almost all of this growing block; its possible favorable individual nodes remain explicit.

The complete errors are uniformly bounded by the EXACT formula(1). With W=2K and W<q, a safe bound is

    max_i |S−c_i|
       <=[q|S−c|+2K|S−6|]/(q−2K).                       (9)

For the window in(8), 2K/q→0, so convergence of the OLD actual c is preserved uniformly on the ENTIRE growing block. There are no poles or zero responses introduced in this enlargement. At most one complete error can vanish, because the numerator q(S−c)+2i(S−6) is affine in i with nonzero slope2(S−6).

The primitive errors remain exactly those in(1). The large actual denominators quantified by(6)–(8) cannot by themselves produce an error lower bound: the old actual error may be zero or exceptionally aligned, and the seed term may cancel it at one index. Analysis's separately authored complete-error product theorem handles explicit signed-error premises; no premise is silently supplied by the polynomial upper bound here.

## 5. Scalar, degree and support costs over the growing block

The added coefficient at node i is2iU/q. If the OLD U is integral, its ACTUAL reduced coefficient denominator is

    q/gcd(2iU,q),

with numerator2iU/gcd(2iU,q). The worst added real coefficient size in the whole block is at most2K|U|/q, and the numerator height after scalar clearing is O(K|U|). No pole order or polynomial degree grows with K: G6 has degree2 numerator over w(w−1), with height7.

For every old prime l dividing q with l>K, l divides none of q+2i. Hence EVERY new primitive q_i avoids all such old primes. Smaller old primes may survive at particular indices dividing i; the exceptional-support condition gcd(2i,q)=1 is retained when complete old-support removal is desired. The growing-window denominator budget does not assume that condition.

## Outcome

The response-changing family preserves the actual target and convergence throughout a growing window while erasing old local-prime support. Its global content can be priced uniformly by a classical factorial bound. Consequently only O(1/epsilon) nodes in a window of length o(log q/log log q) can achieve a q^epsilon denominator gain; most actual denominators retain the leading global rate. A single favorable selected output remains possible and unresolved. No small primitive form or irrationality statement follows from the count alone.
