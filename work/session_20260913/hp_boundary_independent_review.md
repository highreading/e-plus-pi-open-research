> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the unequal-degree Hermite–Padé boundary theorem

2026-09-13. Reviewed `unequal_degree_hp_attempt.md`, especially Sections 3–4, against `endpoint_hp_continuation.md`, `sources/endpoint_matched_mobius_hp_rank_and_content.md`, and the actual integer endpoint normalization. Also reviewed the general `recurrence_density_transfer_lemma.md` while the boundary proof was being completed.

## Verdict

**No substantive gap was found in the `(a,b,c)=(n,0,n)` boundary proof.** The proof establishes unique projective solvability for every integer `n>=1`, and, after full endpoint reduction, eventual nonzero value and



$$
\liminf_{n\to\infty}\frac{\log|L_n|}{n\log n}\ge\frac12.
$$



This closes that exact boundary family as a source of shrinking integer forms. It does not exclude the `(n,b,n)` families with positive `b`, a different pullback, or another approximation construction. It proves no rationality or irrationality statement about `e+pi` itself.

The only wording issue found in the initial version was a possible conflation of an all-index nonzero coefficient pair with an all-index nonzero evaluated form. The author corrected the opening: uniqueness is all-index, whereas nonzero evaluated value and sign are proved eventually. No finite verification is being substituted for the asymptotic argument.

## 1. Independent normalization and exact moment checks

For `F(z)=4 arctan(z/(2-z))`, direct integration gives



$$
F(z)=z\int_{-1}^{1}\frac{du}{1-t(u)z},\qquad
t(u)=\frac{1+iu}{2}.
$$



In particular the functional is bilinear rather than Hermitian. With



$$
p_k(t)=\frac{i^kP_k(-i(2t-1))}{\binom{2k}{k}},
$$



we have `p_k(t(u))=i^k P_k(u)/binom(2k,k)`. Hence the sign in



$$
\mathcal L(p_k^2)=\frac{2(-1)^k}{(2k+1)\binom{2k}{k}^2}
$$



is necessary and correct. The argument never assumes positivity of these complex moments. Their nonzero values establish the required nondegeneracy.

Reversing `C` produces exactly the high equations



$$
\mathcal L(t^q C^*)=-\frac1{(n+q+1)!},\quad 0\le q<n,
\qquad C^*(1)=1
$$



when `B=1`. There is no factorial or index shift missing. Orthogonal projection fixes all coefficients below the `p_n` direction, and `p_n(1)>0` fixes that direction. If `B=0`, the same reasoning and the endpoint equation force the entire triple to vanish. Therefore normalization by `B=1` loses no nonzero projective solution.

The recurrence for `p_k` has a positive second coefficient. The coefficient-norm bound `||p_k||_1<=2^k` follows inductively since that coefficient is at most `1/12`. In the integer Legendre expansion at `t=1`, every summand is positive and the `j=0` summand gives `p_k(1)>=2^{-k}`. These two inequalities have the directions required for the subsequent estimates.

## 2. Signed logarithmic error and its lower bound

The Taylor tail at `z=1` is initially



$$
\frac1{p_n(1)}\mathcal L\left(\frac{p_n(t)}{1-t}\right).
$$



Subtracting the squared-polynomial expression changes its numerator by



$$
p_n(t)\frac{p_n(1)-p_n(t)}{1-t},
$$



whose second factor is a polynomial of degree at most `n-1`. Its moment vanishes by orthogonality. This proves the first equality in the claimed squared-error formula without a positivity assumption.

After substituting `t=(1+iu)/2`, the factor `1/(1-t)` is `2(1+iu)/(1+u^2)`. The imaginary odd part integrates to zero because `P_n(u)^2` is even. Thus the factor `2(-1)^n` and the strict sign `(-1)^n` in equation (18) are correct.

On `[-1,1]`, the real weight `1/(1+u^2)` lies between `1/2` and `1`. Combining this with the exact Legendre norm gives precisely the two constants in (19). The coarse lower bound



$$
|\pi-f_n|\ge\frac{2}{(2n+1)64^n}
$$



uses an **upper** bound for the denominator of the displayed error expression, obtained from `binom(2n,n)<=4^n` and `p_n(1)<=2^n`. Conversely, boundedness of `f_n` uses the opposite inequalities `binom(2n,n)>=2^n` and `p_n(1)>=2^{-n}`. These uses are consistent.

## 3. Rational height, reduced denominators, and every gcd

The identity



$$
J_n(t)=\sum_{j=0}^{\lfloor n/2\rfloor}
\binom nj\binom{2n-2j}{n}(2t-1)^{n-2j}
$$



is the correct integer expansion of `2^n i^n P_n(-i(2t-1))`: the two alternating signs cancel. The coefficient norm is exponentially bounded, for example by a polynomial in `n` times `24^n`; `J_n(1)` is a positive integer of exponential size. Therefore `C_{0,n}^*=J_n/J_n(1)` has a common rational denominator of exponential size.

The coefficients `[z^k]F=4 Im((1+i)^k)/(k 2^k)` through degree `n` have a common denominator dividing `2^n lcm(1,...,n)`. The elementary bound `log lcm(1,...,n)=O(n)` is sufficient. Thus the reduced denominator of `f_n` is at most `exp(O(n))`. Merely knowing that `f_n` is bounded as a real number would not justify this claim; the integer polynomial supplies the missing arithmetic information.

Let `A_n(1)=p_n^{end}/q_n` be reduced, with `q_n>0`. Since `B(1)=C(1)=1`, the primitive integer endpoint pair is exactly `(p_n^{end},q_n)`. Clearing every polynomial coefficient first and then taking the endpoint gcd yields the same pair up to sign: any integral representative is an integer multiple of this reduced pair. Consequently



$$
L_n=q_n\,[A_n(1)+e+\pi]
$$



already includes the full endpoint gcd. There is no remaining hidden divisor to remove.

The rational companion is `r_n=-A_n(1)-f_n`. If `D_n` is the reduced denominator of `f_n`, then its reduced denominator `Q_n` divides `q_n D_n`. Hence



$$
Q_n\le q_n\exp(O(n)).
$$



Extra cancellation can only make `Q_n` smaller. The proof needs this upper bound, so such cancellation cannot invalidate the deduction. It never assumes equality of denominators or coprimality between them.

## 4. Factorial perturbation and the continued-fraction quantifier

The projection estimate implies



$$
\|\delta C_n\|_1\le\frac{\exp(O(n))}{(n+1)!}.
$$



The absolutely convergent Taylor series of `F` at `1` bounds the truncated convolution by its full absolute coefficient sum times this norm. Together with the elementary exponential tail, this proves



$$
0<|e-r_n|\le\exp(-n\log n+O(n)).
$$



The positivity is justified by irrationality of `e`, since `r_n` is rational. Also `Q_n` tends to infinity: a convergent sequence of rational numbers with bounded reduced denominators cannot tend to an irrational limit.

I opened the cited primary [Cohn paper](https://arxiv.org/pdf/math/0601660), which proves Euler's continued-fraction expansion of `e`. From that expansion, the next partial quotient is `O(k)` at convergent index `k`, while the denominator grows at least exponentially in `k`. The exact convergent error lower bound therefore exceeds `q^{-2-epsilon}` for every fixed `epsilon>0`, once `q` is sufficiently large. Reduced nonconvergents satisfy the stronger Legendre lower bound `1/(2q^2)`. This gives the required statement for **all reduced rational fractions of sufficiently large denominator**, not merely one subsequence.

Applying it at the reduced `r_n` gives



$$
\log Q_n\ge\frac{n\log n}{2+\epsilon}-O_\epsilon(n).
$$



The preceding denominator upper bound then gives the identical lower leading scale for `log q_n`. No conjecture about the irrationality exponent of `pi` or of `e+pi` enters.

Finally, the factorial perturbation is eventually less than half of the exponential lower bound for `|pi-f_n|`. Hence `R_n(1)` is eventually nonzero with sign `(-1)^n` and `|R_n(1)|>=exp(-O(n))`. Multiplication by the fully reduced `q_n`, followed by `epsilon` tending to zero, proves the claimed liminf `1/2`. The order of quantifiers is valid: each fixed positive epsilon gives an eventual inequality; taking the supremum of the resulting liminf lower bounds yields `1/2`.

## 5. Independent finite controls

As a check of normalization rather than as an asymptotic argument, I independently reconstructed degrees `n=1,2,3,4,8` using:

- Rodrigues derivatives of `(t^2-t+1/2)^n`, rather than the author's Legendre recurrence;
- exact integrated monomial moments, rather than the archived jet helper;
- a fresh Fraction-based solution of the `n+1` equations;
- polynomial division of `p_n(t)^2` by `1-t` to verify the exact rational part of the squared-error identity;
- rational Machin intervals to check the signs and both error bounds.

All checks passed. The primitive endpoint pairs for `n=4` and `n=8` agree with the separately produced profile file. Some exact values are:

| n | A(1) | f_n | r_n | Reduced denominator Q_n |
|---:|---:|---:|---:|---:|
| 1 | -7 | 4 | 3 | 1 |
| 2 | -45/8 | 3 | 21/8 | 8 |
| 3 | -425/72 | 19/6 | 197/72 | 72 |
| 4 | -9551/1632 | 160/51 | 1477/544 | 544 |
| 8 | -220562724121/37639526400 | 183296/58345 | 102314808601/37639526400 | 37639526400 |

The complete bounded records are in `hp_boundary_independent_checks.json`. For example, `n=4` exhibits actual denominator cancellation in the companion `r_n`; the proof's inequality handles it correctly.

## 6. Added b=1 corollary and its limit

The author's additional `b=1` row has coefficients `(1+t_0,1+t_1)` with both `t_j` factorially small. Therefore the row is nonzero for all sufficiently large `n`, and the exact projection equivalence gives projective uniqueness in that range. The stated sufficient cutoff `n>=512` follows from the coarse displayed bound and `n!>=(n/3)^n`: its remaining upper bound decreases beyond 512 and is already below one there.

This proves only eventual rank and the coefficient ratio approaching `-1`. It does not show that `B(1)` is nonzero, control the reduced endpoint denominator, or establish eventual nondecay. The note explicitly preserves those limits. The `b=0` proof cannot simply be copied to `b=1`, because an exponentially bounded logarithmic companion has not been identified there.

## 7. Independent check of the recurrence-to-density transfer lemma

No substantive defect was found in `recurrence_density_transfer_lemma.md`. In particular:

1. A limiting companion matrix is cyclic with observation row `e_1`. Repeated eigenvalues cause no difficulty: on each Jordan block, the map `z -> z^d` has a local inverse because its eigenvalue is nonzero. Distinct eigenvalues have distinct `d`th powers by the stated root-of-unity exclusion. Hermite interpolation recovers `C` as a polynomial in `C^d`, so the observation determinant at every fixed spacing is nonzero.
2. The proof first fixes the progression window. It then excludes only finitely many exceptional primes and deletes `o(p)` progression starts. Szemerédi's limit is taken only afterward. This order avoids an unjustified uniformity assertion in the spacing.
3. The zero-full-state hypothesis is indispensable and is actually used. The proof does not infer nonzero states just from a nonzero limiting eigenvalue. Its central-binomial example correctly demonstrates the failure without this hypothesis.
4. The integer leading-coefficient bound prevents the observation numerator from becoming identically zero modulo a large prime for all spacings up to a sufficiently small multiple of `log p`. The degree and denominator exceptions then total `O(K^2)`, consistent with the quantitative bound.

One minor wording correction is advisable: boundary exceptions for a progression of spacing `d` are `O_r(d)`, not literally `O_r(1)`. For each fixed `d` this is still a constant, and summation through `K` is already absorbed by the stated `O(K^2)` term. It changes neither conclusion.

The general lemma does not itself verify the actual recurrence, denominator units, target-to-observation equivalence, or zero-state bound in a new arithmetic family. Nor does support zero density control unbounded higher valuations. Its application limits are correctly stated.
