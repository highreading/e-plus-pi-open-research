> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A precision-local candidate for the actual producer coefficients

Status: NEW coordinator application and full derivation, 9 October 2026;
DIFFERENT external proof audit pending. The producer scalar's unit/depth
theorem is REUSED from resumed20261005 A1turn9 and audited A4turn17. The
new target here is an original-index computation whose state is bounded
by the requested precision, rather than by `n`. No source-specific prefix
Schur contraction or unconditional global irrationality result is claimed.

## 1. Source, overlap gate and actual recurrence

The full archive and primary-source checks are recorded in
`gates/PRECISION_LOCAL_PRODUCER_GATE_20261009.md`. The classical Bessel
generating-function background and Pascal transform are reused algebra.
The formula below is proved directly from the actual recurrence, so its
normalization is independent of external Bessel conventions.

Retain


$$
\gamma_0=1,\quad\gamma_1=0,\quad
\gamma_{r+1}=(4r+2)\gamma_r+4\gamma_{r-1},\qquad r\ge1.
$$


Let $F(t)=\sum_{r\ge0}\gamma_rt^r/r!$. The recurrence and exceptional
first moment imply


$$
(1-4t)F''=6F'+4F,\qquad F(0)=1,\quad F'(0)=0.
$$


The unique formal rational solution is


$$
\boxed{F(t)=(1-4t)^{-1/2}\exp(\sqrt{1-4t}-1).}                 \tag{1}
$$


Indeed direct formal differentiation verifies the equation and both
initial coefficients; the differential equation prescribes every next
coefficient. Put $g_h=\Delta^h\gamma_0$. Its exponential generating
function is


$$
\sum_{h\ge0}\frac{g_h}{h!}t^h
=e^{-t}F(t)
=(1-4t)^{-1/2}e^{-3t}\exp(t^2R(t)),\qquad R(t)\in\mathbb Z[[t]]. \tag{2}
$$


Here $\sqrt{1-4t}=1-2t+t^2R(t)$, with integral Catalan coefficients.
The coefficients of `(1-4t)^(-1/2)` are integral. The coefficients
`3^m/m!` of `exp(-3t)` are in `Z_3`. For degree `h`, the last exponential
uses only factorials `m!` with `m<=floor(h/2)`. Thus


$$
\boxed{v_3(g_h)\ge v_3(h!)-v_3(\lfloor h/2\rfloor!)
\ge\lfloor h/6\rfloor.}                                    \tag{3}
$$


The second inequality counts multiples of3 in the interval
`floor(h/2)+1,...,h`. This is an all-degree proof, not a finite pattern.

The exact integer recurrence, useful for bounded generation, is


$$
g_0=1,\quad g_1=-1,\quad g_2=5,
$$




$$
\boxed{g_h=4(h-1)g_{h-1}+(8h-7)g_{h-2}+4(h-2)g_{h-3},\ h\ge3.} \tag{4}
$$


It follows by the ordinary binomial transform: if
$G(z)=\sum g_hz^h=\Gamma(z/(1+z))/(1+z)$, then


$$
4z^2(1+z)^2G'=(1-9z^2-4z^3)G+z-1.
$$


The recurrence is optional; equation(2) already proves the needed bound.

## 2. Literal finite Pascal matrix and a weighted locality theorem

Let $T_n[a,b]=\binom{a+b}{a}\gamma_{a+b}$ and let $P_n$ be the
finite lower Pascal matrix. Set $\widehat T_n=P_n^{-1}T_nP_n^{-T}$.
The classical double binomial transform gives the exact formal identity


$$
\sum_{a,b\ge0}\widehat T[a,b]x^ay^b
=\sum_{h\ge0}g_h\frac{(x+y+2xy)^h}{(1-xy)^{h+1}}.            \tag{5}
$$


Each entry with `a,b<n` uses only raw row indices `<=a` and column
indices `<=b`, so it equals the literal FINITE transformed entry. No
infinite inverse or extra terminal coordinate is introduced.

At precision `3^M`, only `h<6M` is needed by(3). For `d=a-b`, one
explicit entry formula is


$$
\widehat T[a,b]
=\sum_{h\ge0}g_h
\sum_{\substack{p,q,c\ge0\\p+q+c=h\\p-q=d}}
\frac{h!}{p!q!c!}2^c\binom{a+q}{h}.                         \tag{6}
$$


The convention `binom(a+q,h)=0` when `a+q<h` pays the numerator degree
admission. All factorial ratios in the coefficient are integers.
Every contributing `h` satisfies `h>=|a-b|`. Hence


$$
v_3(\widehat T[a,b])\ge\lfloor |a-b|/6\rfloor.              \tag{7}
$$



REUSE the modulo3 blocks from the old unit theorem:


$$
B_3=\begin{pmatrix}1&2&2\\2&0&0\\2&0&2\end{pmatrix},
\quad B_2=\begin{pmatrix}1&2\\2&0\end{pmatrix},\quad B_1=(1).
$$


Let `B` be their literal finite block diagonal lift, preserving the
actual last block. Its inverse is integral over `Z_3` and has bandwidth2.
Put `E=widehatT-B`; then every entry of `E` is divisible by3, and


$$
v_3(E[a,b])\ge\max\{1,\lfloor |a-b|/6\rfloor\}.
$$


If an entry has finite valuation `nu>=1`, its jump is at most `6nu+5`.
Each additional multiplication by `B^-1` adds at most2 to that jump,
so a factor `B^-1 E` of weight `nu` jumps at most `13nu`.

Use the finite Neumann expansion


$$
\widehat T_n^{-1}
\equiv\sum_{r=0}^{M-1}(-B^{-1}E)^r B^{-1}\pmod{3^M}.       \tag{8}
$$


Any product path of total weight at least `M` vanishes. Every surviving
path has total displacement at most


$$
\boxed{w_M=13(M-1)+2.}                                     \tag{9}
$$


Thus the literal finite inverse has this bandwidth modulo `3^M`.
This statement also controls the maximum excursion of a surviving
path, which is what permits a finite end window; net displacement alone
would not suffice.

## 3. Recover the actual top coefficients and complete scalar

Take the original `n=4^j+1`, `j=84645 mod531441`, sufficiently large
for the finite end window below. Let `F_fac=(n-1)!`,
$u_a=F_{\rm fac}(-2)^a/a!$, `v=T_n^-1u`,
$k_a=\binom{n+a}{a}\gamma_{n+a}$, `h=T_n^-1 k`.

Modulo `3^M`, `u` has support in the last `3M` coordinates: every
factorial quotient of length at least `3M` contains at least `M`
multiples of3. Since `P_n^-1` is lower triangular,
`uhat=P_n^-1 u` has the same end support. Inverse(8) is sufficient to
compute its top outputs, then `v=P_n^-T vhat`. For a top coordinate
`a`, the latter uses ONLY coordinates `b>=a`, with coefficient
`(-1)^(b-a) binom(b,a)`.

The next force is equally local after paying its Pascal embedding.
In `T_(n+1)` let `khat` denote the transformed next column above its
literal last coordinate, and put `r_b=binom(n,b)` for `b<n`. Exact finite
block multiplication gives


$$
P_n^{-1}k=\widehat T_n r+\widehat k,
\quad
h=P_n^{-T}r+P_n^{-T}\widehat T_n^{-1}\widehat k.             \tag{10}
$$


The first term has the explicit value


$$
(P_n^{-T}r)_a=(-1)^{n-a-1}\binom na.                       \tag{11}
$$


The second right-hand side `khat` is supported in the last `6M-1`
coordinates modulo `3^M`, by(7). This separates a known dense term from
the actual local inverse, and does not replace the full force by zero.

For any requested top length `L`, take an end window of length at least


$$
\boxed{R_M=\max\{L,6M\}+13(M-1)+4,}                       \tag{12}
$$


rounding upward by at most2 so its LEFT edge is a true multiple-of3
block boundary. Its RIGHT edge is the actual `n-1`. If this exceeds `n`,
use the whole finite matrix instead. Formula(8), including all paths
that can affect the requested outputs, is unchanged in this window:
any path leaving the left edge would have weight at least `M`.
The local matrix remains a ternary unit matrix because it preserves
the complete leading blocks and actual short final block.

The scalar contraction uses only the last `3M` coordinates:


$$
\Xi=F_{\rm fac}^2-\widehat u^T\widehat T_n^{-1}\widehat u,
\quad
\chi=3n\,u^Th+6u_{n-1}.                                  \tag{13}
$$


For sufficiently large original `n`, `F_fac^2=0 mod3^M`; this is a paid
factorial valuation, not an invented value of the integer factorial.
REUSE `v3(Xi)=v3(chi)=1`. To obtain `xi=chi/Xi mod3^p`, run the LOCAL
solver at `M=p+1`, then divide both scalars by3 and invert the unit
`Xi/3`. A direct digit solve may be used in the end window; its size is
linear in `p`, not in the original `n`.

With `b_force=-n-66`, the complete original top coefficient is still


$$
q_a=-\frac{F_{\rm fac}}{a!}
\left(3nh_a+(b_{\rm force}+6)\delta_{a,n-1}
 +\frac{2b_{\rm force}}{n-1}\delta_{a,n-2}+\xi v_a\right). \tag{14}
$$


Both forcing constants and the scalar division are retained. For the
actual 72-coefficient source jet modulo `3^32`, take `p=32`, `M=33`,
`L=72`; a left-aligned end window of at most622 coordinates suffices
by(12). Its resulting `V70` is the actual same-index polynomial, obtained
by the saved monic division formula. No prefix W-return is evaluated by
this local coefficient calculation.

## 4. Input residues and bounded implementation

In(6), the lower binomial index is `<6M`. Vandermonde gives


$$
\binom{a+3^E+q}{h}\equiv\binom{a+q}{h}\pmod{3^M}
\quad(E\ge M+\lfloor\log_3 h\rfloor).
$$


Indeed `v3(binom(3^E,j))=E-v3(j)` for `1<=j<=h<3^E`.
The same payment applies to every top Pascal coefficient and(11), whose
small lower indices are bounded by `max(L,3M)`. A safe common input is


$$
\boxed{n\pmod{3^{M+\lfloor\log_3 R_M\rfloor+1}}.}          \tag{15}
$$


Finite factorial products, the true last-block type and `(-2)^a` are
then determined at the required precision; the latter has period
`3^(M-1)` modulo `3^M`. The huge original `n` is never replaced by a
small matrix size. Only proved low-degree entry periodicity is used.

For `M=33`, using the conservative window bound622 in(15), the modulus
is `3^39`. Thus `n=4^j+1 mod3^39` can be calculated by modular
exponentiation of the actual `j`; specifying a complete original
progression requires the corresponding actual residue of `j mod3^38`.
The present progression fixes fewer digits. One computed representative
does not give a uniform theorem over all its unfixed higher digits.

A practical entry generator can first compute the finite transformed
array at small row indices, recover the degree`<6M` diagonal Newton
polynomials in the row parameter from(6), then evaluate them at the true
end-window row residues. That is polynomial interpolation of proved
entry polynomials, not empirical continuation of an inverse. The digit
solve, top Pascal reconstruction and scalar division must each be
checked independently. Any computation receives a separate bounded gate.

## 5. Proof status and remaining target

The formal coefficient bound, weighted inverse path law and finite
embedding above are coordinator-derived candidates pending a DIFFERENT
complete audit. The old scalar unit is already independently established.
Even if this precision-local algorithm passes all audits and bounded
checks, it computes producer coefficients only. The complete actual
physical7 prefix Schur contraction, all other complete returns, global
all-prime primitive denominator and whole nonzero-error decay remain
their stated separate obligations.
