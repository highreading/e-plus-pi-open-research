> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A weaker top-two criterion suffices for endpoint noncancellation

Date: 2026-09-13. Root continuation. This is a rigorous conditional
implication using previously proved facts about the actual family.
The new concentration hypothesis is not proved. No arithmetic height
or irrationality conclusion is asserted.

Let P_n=sum a_l phi_l be the reflected, canonically normalized raw
polynomial, with phi_l=sqrt(2l+1)P_l(2t-1). Put N_n=||P_n||_2 and

    e_n=||Proj_{<=n-2} P_n||_2/N_n,
    kappa_n=|P_n(0)| / sum_{l=0}^n sqrt(2l+1)|a_l|.

The established normalization and mass theorems give

    a_n=-(1/(4n)+O(n^-2))a_{n-1}+O(N_n/n²)+1/z_n,
    1/(z_n N_n)<=exp(O(n))/(n!)².                       (1)

In particular |a_n|/N_n=O(1/n). The established high-orthogonality
concentration theorem gives, for any fixed A>c_0=log16+3,

    w_n=ceil(A n/log(n+1)), d_n=n-w_n,
    ||Proj_{<=d_n}P_n||_2/N_n <=epsilon_n,
    epsilon_n=exp(-(A-c_0+o(1))n).                      (2)

All subsequent assertions hold for sufficiently large n. The implicit
constants in (1) are uniform for the actual sequence.

The original high-moment theorem uses U_n(x)=P_n(1-x). Reflection
commutes with every Legendre projection, so its norm estimate(2)
applies unchanged to the reflected P_n used here. The test functions
themselves are reflected; they are not identified with the original
F_k. See raw_reflection_convention_bridge.md.

## 1. Quantitative endpoint estimate

Write m_n=sqrt(2n-1)|a_{n-1}| for the absolute contribution of mode
n-1 at t=0, and let r_n be the sum of absolute contributions of all
other modes divided by m_n. If e_n=o(1), then

    |a_{n-1}|/N_n=sqrt(1-e_n²-O(n^-2))=1-o(1).         (3)

The exact squared endpoint weights in modes d_n+1,...,n-2 sum to

    S_n=(n-1)²-(d_n+1)².

Cauchy-Schwarz, separating those modes from the exponentially small
lower block and the top mode, gives

    r_n <= [sqrt(S_n)e_n+(d_n+1)epsilon_n+O(n^-1/2)]
             /[sqrt(2n-1)sqrt(1-e_n²-O(n^-2))].        (4)

Here the O(n^-1/2) numerator is sqrt(2n+1)|a_n|/N_n.
Since S_n/(2n-1)=w_n(1+o(1)) and w_n=o(n),

    r_n <= (1+o(1))sqrt(w_n)e_n+O(1/n)
                         +O(sqrt(n)epsilon_n).        (5)

Whenever the right side is less than1, P_n(0) is nonzero and the
triangle inequality yields the explicit bound

    kappa_n >= (1-r_n)/(1+r_n).                        (6)

Thus no additional signed noncancellation hypothesis is needed once
this quantitative top-two concentration bound is available.

## 2. Consequences weaker than an O(1/n) graph estimate

If e_n=o(sqrt(log n/n)), choose any fixed A>c_0 in (2). Equations
(5)-(6) give r_n=o(1) and therefore kappa_n->1.

More generally, if

    L:=limsup e_n sqrt(n/log n) < 1/sqrt(c_0),          (7)

choose A>c_0 sufficiently close to c_0 that sqrt(A)L<1. Then
limsup r_n<=sqrt(A)L<1, so kappa_n is eventually bounded below by a
positive constant. In particular B_n has exact degree n eventually.

For that last implication recall B_{n,n}=P_n(0). It is an ordinary
real lower bound conditional on (7), not a consequence of the
separate dyadic nonvanishing theorem.

Under either hypothesis the established endpoint quotient identity

    beta_n=B_{n,n-1}/B_{n,n}
      =-sum (-1)^l l(l+1)sqrt(2l+1)a_l / P_n(0)

and the sublinear band (2) prove

    beta_n/n² -> -1.                                  (8)

For completeness, the contribution to beta_n+n(n+1) from l>d_n is
at most 2n(w_n+1) times the total absolute endpoint mass divided by
|P_n(0)|. The lower block contributes at most
n(n+1)(d_n+1)epsilon_n N_n/|P_n(0)|. Equations (3)-(6) give
|P_n(0)|>=c sqrt(n)N_n. Division by n² makes these contributions
O(w_n/n)+O(sqrt(n)epsilon_n), hence (8). This argument also gives
beta_n/n²=-1+O(1/log n) under the strict limsup condition (7).

If the stronger proposed e_n=O(1/n) holds, (5) improves its endpoint
consequence to

    1-kappa_n=O(1/sqrt(n log n)).                      (9)

The top mode adds only O(1/n) to r_n and is absorbed by this bound.
The full graph norm O(1/n) sought in raw_top_two_concentration_attempt.md
is therefore sufficient but substantially stronger than required for
(8). An o(sqrt(log n/n)) graph bound for the whole two-dimensional
space also suffices, since it implies the same bound for the actual
selected polynomial. A bound only on the selected direction suffices
as well; full-space transversality is not logically necessary for it.

## 3. Scope and the next mathematical problem

The all-degree facts used here are (1)-(2). Equations (4)-(6) and the
conditional implications (7)-(9) are new deductions. The missing
statement is still quantitative concentration of the actual selected
polynomial, or a sufficient whole-space graph bound. The closed
n=4,8,16 diagnostics do not prove it.

The estimate does not control ||P_n|| above, the primitive denominator,
the signed remainder, or the normalized connection coefficients.
Obtaining beta_n/n²->-1 would supply one of the explicitly missing
accessory-scaling hypotheses, not all of them.
