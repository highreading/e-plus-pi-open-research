> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The first even-degree P coefficient gate and an exact top-block cancellation

Date: 2026-09-13. Original continuation by audit_results.

For every even n>=2 this note proves the first of the two remaining
leading-coefficient gates for P=(1+z²)(A'C−AC')+C²:



$$
\boxed{v_2([z^{2n-1}]P)>v_2([z^{2n}]P).}          \tag{1}
$$



The second gate at z^(2n−2) remains open. Its common top exponential
row-set contribution is shown below to vanish exactly. No bound on
the discarded row-set contributions is inferred from that vanishing.

## 1. Actual coefficient notation and the required bounds

Use the canonical raw triple B(1)=1,C(1)=4, and ascending coefficient
indices a_j,b_j,c_j for A,B,C. Put



$$
h_2=a_{n-2}-c_{n-1},\quad
p_0=[z^{2n}]P=\Xi_n,\quad p_1=[z^{2n-1}]P.
$$



The exact coefficient identity is



$$
p_1=2(a_n c_{n-2}-h_2c_n).                        \tag{2}
$$



Write phi(j)=v_2(j!), epsilon=1 if n=2 modulo4 and0 otherwise.
The already proved even-degree results are



$$
v_2(a_n)=-n,\quad
v_2(c_n)\ge-n-2\phi(n-1)-2\epsilon,\quad
v_2(\Xi_n)=-2n-2\phi(n-1)-2\epsilon.              \tag{3}
$$



I will prove the two additional bounds



$$
v_2(h_2)\ge-n,\qquad
v_2(c_{n-2})\ge-n-2\phi(n-1)-2\epsilon.           \tag{4}
$$



Then both products inside(2) have valuation at least v_2(Xi_n),
and its explicit factor2 proves(1). In particular the two even
residue classes retain their different proved baseline valuations;
they are not normalized by the same hypothetical dominant product.

## 2. A one-gap bordered-Cauchy bound

The only new Cauchy estimate needed is an even-pole set with one
missing penultimate pole. Fix an integer R>=1. Compare the consecutive
pole indices 0,1,...,R−1 with the modified indices



$$
\mathcal M=\{0,1,\ldots,R-2,R\}.                 \tag{5}
$$



The actual poles are twice these indices (a fixed parity translation
is harmless). Let x_1,...,x_(R−1) be arbitrary distinct odd integers.
The bordered block, after the usual row and column sign changes,
has entries1/(x_i−2m) and last row (−1)^m at the poles m in M.
All denominators are odd units. Put



$$
f(m)=(-1)^m\prod_{i=1}^{R-1}(x_i-2m).
$$



For every j>=0,



$$
\Delta^j f(0)\in2^j\mathbb Z.                   \tag{6}
$$



Indeed if g(s)=prod_i(x_i−s), then
Delta^j f(0)=(−1)^j[(S_2+I)^j g](0), where S_2 g(s)=g(s+2).
The operator S_2+I sends Z[s] into2Z[s], because
g(s+2)+g(s)=2g(s)+[g(s+2)−g(s)] has all coefficients even.
Its quotient by2 again preserves Z[s], proving(6) by iteration.

The leading coefficient of the interpolation polynomial for f on M
is its divided difference. In its Newton expansion at0, only the
terms binom(m,R−1) and binom(m,R) can contribute to that leading
coefficient: the nodes in M are nonnegative and at most R. The
result is exactly



$$
[\mathcal M]f=
\frac{\Delta^{R-1}f(0)}{(R-1)!}
+\frac{\Delta^Rf(0)}{R!}.                         \tag{7}
$$



For the second term, reduce (m)_R on the nodes in M. Its degree-R
term is removed by the monic node polynomial; the remaining
degree-(R−1) coefficient is1, since the node sum differs from
0+...+(R−1) by1. This also proves(7) directly for every R,
including R=1 with M={1}.

The Vandermonde of M is R times the consecutive Vandermonde.
Clearing the odd Cauchy denominators and using the standard
alternant identity, the modified bordered determinant is an odd
unit times the common prefactor



$$
V(x)\,2^{(R-1)(R-2)/2}
      \Bigl(\prod_{j=0}^{R-2}j!\Bigr)
$$



multiplied by



$$
R\Delta^{R-1}f(0)+\Delta^Rf(0).                  \tag{8}
$$



If R is odd, (6) makes(8) divisible by2^(R−1). If R is even,
its first term has the extra factor2 from R and its second already
has2^R, so(8) is divisible by2^R. Thus its valuation is at least
R−1+1_(R even). This is exactly the extra parity factor in the
original consecutive-pole global bordered-Cauchy bound.

Consequently the one-gap bordered block never falls below the
original global bound with the same row and pole counts. This
assertion concerns a lower bound, not equality or an odd-unit ratio
to the consecutive block. In a square Cauchy block the same pole
change simply multiplies its pole Vandermonde by R, and likewise
cannot lower its valuation.

## 3. The bound for the actual c_(n−2) coordinate

Let n=2R. Delete the C_(n−2) coordinate column in its actual
augmented determinant. The even C poles are now
{0,2,...,2R−4,2R}, and the odd poles are the unchanged
{1,3,...,2R−1}. Each set has R poles.

With the endpoint border assigned to C, every nonzero parity
orientation has one square block of size R and one bordered block
of size R. If the modified even block is square, its Vandermonde
only gains v_2(R). If it is bordered, Section2 supplies the same
global bound as before. Therefore the entire C minor has valuation
at least L_(n−1), exactly the lower bound used for c_n in
raw_Xi_even_dyadic.md. With the border assigned to B, both C
blocks are square; their pure-C lower bound2S(n) is also unchanged
or improved.

Retain the reviewed notation
S(n)=sum_(j<n)phi(j), c_n^val=2floor((n+2)/4),
L_n=2S(n)+c_n^val, H_n=sum_(k=2n+1)^(3n)phi(k),
V_n=S(n)−H_n+L_n for the reduced endpoint determinant valuation.
The exponential block has n+1 columns. Its C-border contribution
has valuation at least



$$
S(n+1)-H_n-\phi(2n)+L_{n-1}.                    \tag{9}
$$



This uses only the maximum factorial sum at rows{2n,...,3n}
and the global integral Vandermonde lower bound, not a unique
minimum. The other border assignment has a gap at least
2+n+2phi(n−1)−c_(n−1)^val>0 above(9), by the same binomial
alternant and pure-C bound as in the original c_n proof.

Subtracting V_n in the actual coordinate cofactor quotient gives



$$
v_2(c_{n-2})\ge-n+L_{n-1}-L_n
=-n-2\phi(n-1)-2\epsilon.                        \tag{10}
$$



The appended coordinate row has no factorial factor. No normalization
by a different C cofactor was used.

## 4. The cancellation-adapted h_2 row

The exact reconstruction row for h_2=a_(n−2)−c_(n−1) is the negative
coefficient row at k=n−2, with the extended conventions
f_s=0 for negative s, t_(−1)=1 and t_(−2)=0. The latter even
entry already vanishes in the parity formula. There is only one
possible negative odd denominator, namely−1. Thus this introduces
exactly the additional −c_(n−1), without a fictitious negative
Taylor coefficient for arctangent.

The signed Cauchy argument for the h=a_(n−1)−c_n row in
raw_Xi_even_dyadic.md applies unchanged to the global lower
bounds: all nonzero denominators remain odd, and the square/
bordered identities use integer Vandermondes and signed products,
not positivity of the row values. Here the ordinary row set is
{n−2} union{n+1,...,3n}.

With the border in C, the n+1 exponential columns have the same
maximum factorial sum at{2n,...,3n}. The C block has n ordinary
rows and its original consecutive pole sets, so its global bound
is L_n. The reduced numerator valuation is at least
S(n+1)−H_n−phi(2n)+L_n=V_n−n.
The other border assignment has gap at least
2+n+2phi(n)−c_n^val>0. Hence



$$
v_2(h_2)\ge-n.                                    \tag{11}
$$



This is a bound on the modified row itself. Subtracting unrelated
valuations of a_(n−2) and c_(n−1) would not establish it.
Equations(3),(10),(11) now prove(1) through(2).

## 5. The exact common top-block polynomial is linear

This section identifies a cancellation relevant to the still-open
second gate. It does not assert that the common top row set
approximates that quadratic expression to the required precision.

Reverse the polynomials with t=1/z. If C(z)=z^n U(t) and
A(z)=z^n V(t), the reversal of P is



$$
z^{-2n}P(z)=U^2+(1+t^2)(VU'-V'U).                \tag{12}
$$



For the common factorial-maximal exponential row set
{2n,...,3n}, the C cofactors are at one common scale
U_top=kappa(Q_n−lambda Q_(n−1)), with lambda=Q_n(1)/Q_(n−1)(1).
The corresponding pure arctangent reconstruction is V_top=−S_U,
using the same second-kind polynomial definition and common
cofactor scale as raw_Xi_top_block_factorization.md.

For a polynomial U with second kind S_U, define



$$
T_U=U^2+(1+t^2)(US_U'-U'S_U).
$$



The reviewed Legendre second-kind Wronskian identity gives
T_(Q_m)=(2m+1)h_m. For two adjacent degrees, define their cross
term by polarization. Its derivative, using
LQ_j=j(j+1)Q_j and LS_j=j(j+1)S_j−2Q_j', is



$$
T_{Q_n,Q_{n-1}}'
=2n(Q_{n-1}S_n-Q_nS_{n-1})=2n h_{n-1}.
$$



The cross term is odd by parity, so its constant is zero. Therefore



$$
\boxed{
T_{U_{\rm top}}
=\kappa^2\bigl[(2n+1)h_n
+\lambda^2(2n-1)h_{n-1}
-2n\lambda h_{n-1}t\bigr].}                      \tag{13}
$$



In particular its t² coefficient is exactly zero. This statement
holds in both parity classes and is an identity, not a dyadic
leading-term estimate. Its constant agrees with the previously
factored Xi_top because h_n=−n²h_(n−1)/(4n²−1).

The actual p_2 is a quadratic expression in complete coefficient
cofactor sums. Products involving other exponential row sets, and
the −4 endpoint assignment, have not been bounded at valuation
v_2(Xi_n)+1. Their cancellation cannot be inferred from(13).

## 6. A precise correction decomposition for the remaining gate

For the full actual reversed C polynomial U, the exact low Taylor
reconstruction is



$$
V=-S_U-E_B,\qquad
E_B(t)=t^n[\operatorname{Taylor}_{\le n}(B(z)e^z)]_{z=1/t}.
$$



Consequently the exact reversed P is



$$
T_U+(1+t^2)(E_B'U-E_BU').                         \tag{14}
$$



The new all-coefficient B theorem proves
v_2([t^s]E_B)>=phi(n)−phi(n−s)>=0, since each Taylor term has
valuation at least phi(n)−phi(j)−phi(n−s−j), and
phi(j)+phi(n−s−j)<=phi(n−s). This removes any untracked
factorial denominator from E_B.

The remaining target is an actual uniform bound for the t²
coefficient of(14), separating U into its common top cofactor
vector and its other row-set contributions with one common scale.
The norm identity(13) already cancels the whole top contribution;
a proof must now bound the cross terms and the E_B correction.
The present note does not assert the needed bound, nor any
squarefreeness or triple-root exclusion conclusion beyond the
proved first coefficient gate(1).
