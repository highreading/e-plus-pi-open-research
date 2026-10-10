> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Inverse-cubic trace quotient: a valid-prime rank-drop counterexample

## Scope

The trace-polynomial solution spans a known line in the kernel of the
target-evaluation map



$$
E_m:(c_0,c_1,c_2)\longmapsto
 (c_{4m},c_{4m+1},c_{4m+2})
$$



for the order-three inverse-cubic differential equation.  A possible
strengthening would be to prove that this trace line is the entire kernel
modulo every fresh prime.  The following exact example disproves that
strengthening.  It does not produce a common zero for the distinguished
inverse branch.

## Exact counterexample

Take



$$
m=2,\qquad n=12,\qquad p=112291.
$$



The integer $p$ is prime and $p>6m=12$, so it is a valid fresh prime.
Propagating the three coordinate initial states by the certified eight-term
recurrence to degrees $8,9,10$ gives a rational $3\times3$ target
matrix.  Every forward pivot $C_3(k,12)$, $0\le k\le7$, is a
$p$-unit.  The least common denominator of all nine entries has prime support



$$
\{2,3,23\},
$$



so reduction modulo $p$ is legitimate.  The reduced matrix is



$$
\overline E_2=
 \begin{pmatrix}
 36809&42527&81183\\
 67271&104225&67489\\
 91448&45547&90217
 \end{pmatrix}
 \pmod{112291}.
$$



Exact row reduction gives



$$
\operatorname {rank}\overline E_2=1.
$$



The trace polynomial has initial vector



$$
\tau=(2080,95651,53640),
$$



and $\overline E_2\tau=0$, as expected.  But the vector



$$
v=(69764,36809,0)
$$



also satisfies $\overline E_2v=0$, and



$$
69764\cdot95651-36809\cdot2080\not\equiv0\pmod p,
$$



so $v$ is not proportional to $\tau$.  Hence



$$
\boxed{\dim\ker\overline E_2=2>1.}
$$



The distinguished branch $T(0)=0$ has initial vector



$$
f_0=(2048,95907,53760),
$$



and



$$
\overline E_2f_0=(24641,63218,21102)\ne(0,0,0).
$$



These three target values are also checked directly from



$$
[t^N]\frac{A(t)^{12}}{R(t)^{N+1}},
 \qquad N=8,9,10,
$$



independently of the transfer matrix.

## Consequence

Factoring the scalar differential operator by the known trace solution does
not leave a target map that is injective modulo every fresh prime.  At the
example above, the quotient target map has rank one rather than two.  Thus
the trace quotient alone cannot prove fresh-prime nonvanishing.  A successful
argument would still have to intersect the enlarged target kernel with the
distinguished branch or Cartier/Frobenius line.  This note makes no claim
against such a branch-specific argument.

The deterministic exact certificate is
`scripts/inverse_cubic_trace_quotient_rank_drop_certificate.py`; its
byte-stable output is
`results/inverse_cubic_trace_quotient_rank_drop_certificate.json`.
