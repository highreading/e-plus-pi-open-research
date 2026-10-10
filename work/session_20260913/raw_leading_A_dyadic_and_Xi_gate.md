> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The leading A coefficient and the still separate infinity cross-minor

Date: 2026-09-13. Original dyadic continuation by audit_sources.

The canonical raw triple is normalized by `B(1)=1`, `C(1)=4`.
Write its coefficients as a_j,b_j,c_j. This note proves

    v_2(a_n)=-n for every n>=1.                       (1)

Thus A has exact degree n, as B now does by
`raw_leading_B_dyadic_all_indices.md`. This result does not establish
the distinct cross-minor

    Xi_n=a_n c_(n-1)-(a_(n-1)-c_n)c_n.                (2)

## 1. Exact appended row and normalization

Use the raw high-jet matrix J_n and its endpoint border
`C(1)-4B(1)` from `raw_homogeneous_ode_independent_review.md`.
For the coefficient a_n, the reconstruction row is exactly

    u_(a_n)=-( f_(n-j) | t_(n-j) )_(j=0,...,n),

where `f_k=1/k!` for k>=0, and the arctangent coefficients have
`t_0=0`. Thus appending u_(a_n) is, up to sign, appending the original
coefficient row at Taylor index n. After dividing the original high
rows n+1,...,3n by their factorials, and moving this extra row into
order, the numerator determinant has ordinary rows

    k=n,n+1,...,3n

and the final endpoint border. It has n+1 exponential and n+1
arctangent columns. Call this reduced determinant D_A, allowing the
irrelevant global sign from row permutations.

The appended coefficient row is not multiplied by n! in D_A. If one
instead uses the integer minor A_star, then the cofactor identity is
`a_n=A_star/(n! Delta_B)`; its additional n! cancels when passing
to the present reduced coefficient-row determinant. This distinction
is necessary for (1).

The reduced denominator determinant has established valuation

    V_n=S(n)-H_n+L_n,
    S(m)=sum_(j=0)^(m-1)phi(j), phi(j)=v_2(j!),
    H_n=sum_(k=2n+1)^(3n)phi(k),
    L_n=2S(n)+c_n^val, c_n^val=2 floor((n+2)/4).     (3)

The superscript on c_n^val distinguishes this valuation constant
from the actual coefficient c_n.

## 2. The arctangent lower bounds still hold at row n

The C-border block has n ordinary rows with columns C_0,...,C_n.
For any selected rows k>=n, the same bound L_n as in the archived
bordered-rank proof holds. This extension of the old row range does
not assume a formal negative moment: split the coefficient matrix
directly by parity. Its nonzero entries are signed `1/(k-j)` with
positive odd denominators; k=j=n contributes t_0=0 in a parity-zero
block. The square and bordered Cauchy bounds use only the parity,
distinctness, and consecutive pole sets. Their row-Vandermonde lower
bounds are unchanged by allowing the smallest row n. Therefore the
proof of the global bound applies verbatim to this enlarged range.

Likewise an unbordered block with m consecutive arctangent columns
and m selected ordinary rows has valuation at least `2S(m)`, whenever
its nonzero differences are positive odd integers. To see this
without extending an orthogonal functional to negative powers, its
nonzero determinant splits into square Cauchy blocks of sizes
`e=ceil(m/2)` and `o=floor(m/2)`. Each block's row and pole
Vandermondes give the lower bound

    2g(e)+2g(o)=2S(m),
    g(r)=r(r-1)/2+S(r).

The identity `g(e)+g(o)=S(m)` follows immediately from
`phi(2r)=phi(2r+1)=r+phi(r)`. Zero determinants satisfy the bound
automatically.

For the specific n-row set

    U_A={n,n+1,...,2n-1},

the bordered bound is attained. If n=2r, its even rows make the
square odd-pole block, while its odd rows make the bordered even-pole
block of size r+1. Its first row-to-pole difference is 2r+1; when the
bordered size is even, r is odd and this is 3 modulo4. If n=2r+1,
its odd rows make the square even-pole block and its even rows make
the bordered odd-pole block, again of size r+1 and first difference
2r+1. The same mod4 condition holds whenever needed. All row sets
are consecutive within their parity. The archived equality criterion
therefore gives

    v_2(C_(U_A))=L_n.                                (4)

The empty ordinary-row block at n=1 uses the standard determinant-one
convention, so this also includes n=1.

## 3. Unique C-border term and the other assignment

Expand D_A along its n+1 exponential columns. If the border goes
to C, the factorial-valuation sum of the n+1 selected ordinary rows
has a unique maximum at

    S_A={2n,2n+1,...,3n}.

Indeed its smallest member 2n has strictly larger factorial valuation
than every excluded index at most 2n-1. Any other row set loses at
least one power. The consecutive exponential Vandermonde attains
the global bound S(n+1), and its complementary C minor attains (4).
All other Vandermondes are at least S(n+1) and all C minors at least
L_n. Hence the S_A term is the unique least one in this assignment,
of valuation

    S(n+1)-H_n-phi(2n)+L_n
       =V_n+phi(n)-phi(2n)
       =V_n-n.                                      (5)

If instead the border goes to the exponential block, its factor -4
and the integral Lambda alternant give the bound

    2+S(n)-H_n

for that block. The remaining pure arctangent block has size n+1 and
valuation at least `2S(n+1)` by Section 2. Relative to (5), the gap
is at least

    2+2phi(n)+n-c_n^val >0.                          (6)

Positivity follows from `c_n^val<=(n+2)/2`. Therefore this assignment
cannot cancel the unique minimum. The full reduced numerator has
valuation V_n-n, and dividing by the reduced denominator of valuation
V_n proves (1).

## 4. The exact remaining Xi gate and why B/A nonvanishing does not settle it

At infinity put `C^rev(t)=t^n C(1/t)`. The two Laurent germs, after
removing the constant branch of arctangent, have first jets

    H^rev(t)=a_n+(a_(n-1)-c_n)t+O(t^2),
    C^rev(t)=c_n+c_(n-1)t+O(t^2).

Their two-by-two jet determinant is exactly (2). In the original
integer minor normalization, retain

    Delta=det[J_n; B(1)],
    A_star=det[J_n; n! u_(a_n)],
    A_minus=det[J_n; (n-1)! u_(a_(n-1))],
    C_star=det[J_n; u_(c_n)],
    C_minus=det[J_n; u_(c_(n-1))].

Define the cancellation-adapted integer minor combination

    H_minus=A_minus-(n-1)! C_star.

Linearity in the appended row shows this is itself the determinant
with appended row `(n-1)![u_(a_(n-1))-u_(c_n)]`. Both normalization
factors are retained in the exact identity

    Xi_n=[A_star C_minus-n H_minus C_star]
                         /[n! Delta^2].              (7)

This is equivalent to the three-term formula already proved, but
groups its potentially cancelling terms before a valuation comparison.
Together with (1), a sufficient next theorem would be an exact
valuation for c_(n-1) and a strict bound

    v_2((a_(n-1)-c_n)c_n)>-n+v_2(c_(n-1)).            (8)

Neither (8) nor the nonvanishing of c_(n-1) is proved here. Equality
or the reverse inequality could also be handled by an exact unit
comparison; it must not be dismissed.

The B-leading interpolation lemma controls a different family of
linear bordered determinants. It does not supply the valuation of
H_minus or the two products in (7). In particular, its divisibility
precision is not an entrywise small perturbation theorem for the
inverse arctangent moment matrix, whose dyadic determinant contains
much larger powers of two. Replacing the exact C-minor lower bounds
by a presumed well-conditioned inverse would be unjustified.

This note establishes (1), not Xi_n!=0. The latter remains the
arithmetic gate for promoting the cubic-stratum integral recurrence
to every degree.
