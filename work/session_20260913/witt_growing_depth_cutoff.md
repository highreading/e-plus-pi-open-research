> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# What the quantitative support theorem already gives at growing depth

This is an elementary consequence of the reviewed first-Witt theorem,
not a new independent distribution theorem or a bound on the full tower.

Let d_(m,p)=v_p(c_m)-b_(m,p) on the exact Item427 ordinary rank-zero
scope p^2>4m+1, and let

    S(X)=sum_(X<m<=2X) sum_p 1_(d_(m,p)>=1) log p.

The reviewed result gives S(X)<=C X^2 delta(X), where
delta(X)=exp(-c(log log X)^(1/9)), for some fixed c>0.
For any positive cutoff K=K(X), pointwise nonnegativity gives

    sum_(X<m<=2X) sum_p min(d_(m,p),K)log p
       <=K S(X)<=C X^2 K delta(X).                    (1)

Thus the weighted depth truncated at

    K(X)=floor(exp((c/2)(log log X)^(1/9)))

already has zero normalized dyadic average. The cutoff tends to infinity;
the theorem is therefore stronger than a statement about each fixed
finite layer separately. In particular any fixed power of log log X
can be used for K, since its logarithm is O(log log log X).

For this explicit cutoff the full sum has the exact decomposition

    sum d log p = sum min(d,K)log p + sum (d-K)_+log p.

Consequently the full tower has zero normalized dyadic average if and
only if its remaining weighted tail sum is o(X^2). The only unresolved
part is the mass at depths exceeding this growing cutoff. This is not
permission to discard that tail: the available coefficient-height
bound still allows depths of order X/log X at a large prime.

A useful sufficient moment version follows from Hölder. For any fixed
a>1, put M_a(X)=sum_(X<m<=2X)sum_p d_(m,p)^a log p. Then

    sum d log p <= M_a(X)^(1/a) S(X)^(1-1/a).          (2)

If M_a(X)=O(X^2 (log log X)^B) for any fixed B, (2) and the
quantitative support theorem prove the full o(X^2) conclusion. More
generally it is enough that

    [M_a(X)/X^2] delta(X)^(a-1) ->0.

This is a precise target for the current integral-rank/normalized-log-gcd
investigation. No such moment estimate has yet been established for
the actual family. An arbitrary array of nonnegative depths can place
large weights on its rare support; the actual arithmetic must prevent
that concentration.
