> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the quantitative fixed-cut rate

Date: 2026-09-13. Reviewer: audit_computations.

Reviewed `raw_quantitative_fixed_cut_transport.md` in full.
The complex-disk continuation, uniform bound, Cauchy estimate,
ordered-product rate, and propagation to the actual normalized
columns and high kernel pass. No mathematical repair is requested.

## 1. Analytic continuation on the full disk

For `j>=3`, the parameter `alpha=(j-2)/j` lies in `[1/3,1)`.
On the chosen disk `|w|<=1/8`, the polynomial under the square
root `h_alpha` differs from one by at most `2R^2+R^4<1`.
The root normalized at one is therefore analytic and uniformly
close to one. The denominator of `rho_alpha` remains close
to two, and `alpha` stays bounded away from zero. Thus `rho`,
its selected square root, and `b_alpha` are analytic and
uniformly nonzero on a neighborhood of the closed disk.

The actual finite compression has norm at most one after
division by `j^2`. Since `|c(w)|>15`, the full inverse in
`C_j` differs from the identity by at most `1/14`. Its
boundary compression therefore also lies within `1/14` of
the identity and is invertible. This verifies both inverses
in (2), including nonreal points on the disk. The dependence
on `1/c=4w^2/(1-w^2)^2` is analytic at zero.

The exact factor in `Q_j` follows from

    T_j=Gamma_j^(-1)(R_phys)^(-1),
    R_phys=x^(-1) C_j,
    x/lambda=j^2(1-w^2)^2/4.

At zero, `Q_j` is lower triangular. Its upper-right entry
vanishes to order at least two because every entry is even
in `w`. This is the required removability, not merely a
boundedness claim on a punctured sector.

I checked every factor in (4) directly. The old and new
diagonal parameters have ratio `rho_alpha`, the scalar
cocycle ratio is `b_alpha`, and the exponential parameters
are `eta` and `alpha eta`. Multiplying the two diagonal
gauges produces precisely `Q_12/(w sqrt(rho))` and
`w Q_21 sqrt(rho)`. The former is analytic at zero by the
even upper-right zero. Hence (4) really defines a full-disk
holomorphic matrix without relying on a multivalued square
root of `w`. Its value at zero is exactly the previously
reviewed diagonal matrix `L_j`.

## 2. A uniform bound independent of the argument of c

The norm estimates in (6) are justified by `|c|>15` and
the norm-one self-adjoint operators; no right-half-plane
assumption is required on this disk. The geometric boundary
vector has `q=w^2`, `m=4w^2`, and
`|c||m|=|1-w^2|^2`. Its fixed weighted norms are therefore
uniformly `O(1/|c|)`.

The previously proved coefficient perturbation estimates
remain independent of the spectral parameter. Sandwiched
between those vectors, their linear remainder is
`O(1/(|c|^2j^2))` and the second resolvent term is
`O(1/(|c|^3j^2))`. Thus (7) is valid uniformly on the
whole disk. Division by `m` and a uniform Neumann inverse
give (8). The exact lower-triangular first factor protects
the additional `1/|c|` in its upper-right remainder.

For the reference cocycle, all expressions in (9) are
analytic on the same large-`|c|` branch. The identity for
`c d/dc` follows by differentiating
`c=(1-w^2)^2/(4w^2)`. Along the short time interval,
`|x/t^2|>=|c|>15`; hence the bounded generator and
derivative estimates continue to hold even if `Re c`
is negative. The separate upper-right weighted estimate
therefore applies to the reference error as well.

Subtracting the two step expansions and using the exact
formula (4), the upper-right error is divided by `w` but
was already `O(|w|^2/j^2)`. The lower-left error is
multiplied by `w`; the diagonal errors remain `O(j^-2)`.
All other factors are uniformly bounded with bounded
inverses. This proves the uniform full-disk bound (11).
The finitely many initial `j` can be included by their
explicit analytic formulas on the same fixed disk.

## 3. Cauchy's estimate and the global harmonic sum

Cauchy's estimate applied on the fixed disk gives a
derivative bound `C/j^2` on its half-radius disk. Integrating
from zero proves `||S_j(w)-L_j||<=C|w|/j^2` there.

For `x=chi N^2`, the accepted half-plane estimate gives
`|w_j|<=C_K j/N`. When `w_j` is outside the smaller disk,
the original uniform `O_K(j^-2)` bound for both `S_j-I`
and `L_j-I` is at most a constant times `|w_j|/j^2`.
When a fixed small `j` is involved, `w_j` eventually enters
the disk uniformly on the compact set. These cases together
give the claimed `C_K/(Nj)` bound for all actual preceding
cuts, with no unproved extension of a sector estimate.

All ordered subproducts have bounded norms because the
large-index step errors are summable and the finite initial
head is bounded. The telescoping product difference is
therefore bounded by the harmonic sum
`C_(K,J) sum 1/(Nj)=O_(K,J)(log N/N)`. The tail of the
positive diagonal product is `O(1/N)`, giving (16).
Inversion near the fixed positive limit gives the same
inverse rate. Applying the uniform estimate on a slightly
larger compact set and then Cauchy's formula proves every
fixed derivative bound stated in (17).

## 4. Actual columns, condition numbers, and the high kernel

The explicit fixed-cut matrices have convergent expansions
in `x^(-1/2)`. After their *unequal* column powers are
removed, the first omitted entries are `O(x^(-1/2))`,
hence `O_K(1/N)` at `x=chi N^2`. Multiplication by the
corrected product therefore gives (18) with the claimed
`O(log N/N)` rate. The exact lambda products and column
powers are unchanged.

On the positive real axis, the normalized limiting matrix
is uniformly invertible on a compact interval and its first
column norm is uniformly nonzero. The elementary two-by-two
singular-value calculation is stable under an
`O(log N/N)` matrix error, while its extra `1/sqrt(x)`
error is only `O(1/N)`. The rate for `cond(P_N)/N` and
the relative rates of the two positive-axis singular
values therefore follow.

The analytic boundary divided difference already has
`O(1/N)` error, including its diagonal. Combining it with
the two quantitatively normalized columns gives the
two-parameter `O(log N/N)` kernel error. The lower cut
in the prescribed high interval is exponentially small
under the exact upper even normalization, so it does not
alter this rate. Uniform holomorphy on enlarged compact
sets gives the stated fixed-order derivatives.

The estimate is an absolute normalized matrix-kernel error.
It does not remove actual amplitude factors or imply
stability for a growing full-density determinant. The source
note preserves both limitations correctly.
