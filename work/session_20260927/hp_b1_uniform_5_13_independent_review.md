> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit: uniform primes 5 and 13 and all-even b=1 exclusion

Date: 2026-09-27. Reviewer: audit_results.
Verdict: FULL PASS within the explicitly listed scope below.
No mathematical repair requested.

Reviewed:

1. hp_b1_prime_seed_transfer_and_closed_atlas.md, the complete
   all-residue transfer and the six-prime scalar certificate.
2. hp_b1_residue_one_actual_numerator.md, Sections 1–2, including
   the analytic first-lift dependency from the September 13 notes.
3. hp_b1_uniform_five_thirteen_and_even_exclusion.md, read after
   finalization, including its combination with the already passed
   all-even dyadic bound and evaluated b=1 error theorem.

The separate ternary-root analysis in Sections 3–4 of the second
source is not certified by this review. The requested additional
odd-index coverage analysis was not started after the user's stop
instruction. The other four primes below occur only because their
seed verification was already part of the active closed-atlas audit.

## 1. Actual reduced quotient and normalization

The numerator throughout is exactly


$$
\mathscr U_n=\mathscr Q_n+
       \frac{2^{n+1}}{(n!)^2}\mathscr C_n,\qquad
 X/Y=\mathscr U_n/\Delta_n,
$$




$$
\mathscr C_n=K_{n+1}\mathscr A_n-H_n\mathscr B_n,\quad
 \mathscr Q_n=2K_{n+1}Q_n-(n+1)H_nQ_{n+1}.
$$


This is the same rational endpoint previously checked in
hp_b1_adjacent_scalar_independent_review.md. K denotes J_k/k
in these b=1 sources. No b=2 derivative combination is substituted.

The factorial index in both T_n and T_(n+1) remains n+j.
The Rodrigues scale is respectively 2^n/(n!)^2 and
2^(n+1)/((n+1)(n!)^2). Consequently the rational numerator above
and its dyadically integral C_n are the actual objects before
endpoint reduction. A coefficient clearer is not used as q.
Every conclusion concerning q assumes Delta_n!=0; the accepted
analytic theorem guarantees that condition at all sufficiently
large indices.

## 2. All-index residue transfer, including the prime boundary

The recurrence D_j=jD_(j-1)+1 resets at multiples of p and proves
D_j=D_(j mod p) modulo p for every nonnegative j.
If n=r modulo p, only s<=r survives in the H,A contractions.
The coefficient a_s(n) and the falling factorial then reduce to
their seed-r values. Their D indices reduce to the same seed
indices, all nonnegative.

For K,B and r<=p-2, only s<=r+1 survives. At the exceptional
boundary r=p-1, s=1,...,p-1 is killed by Frobenius in
a_s(n+1), s=p is killed by 2n+2-s, and s>=p+1 is killed by
(n)_(s-1). Only s=0 survives, exactly as in the seed r=p-1.
This proves every coordinate of the source's all-residue formula
without division by a possibly nonunit n+1.

The seed r=0 is a well-defined scalar contraction; the transfer
does not assume existence of a canonical degree-zero b=1 family.

## 3. Independent finite seeds

I recomputed all 72 residue rows for the predeclared primes
5,7,11,13,17,19. The new computation starts from the defining
coefficient formula for H_k(x) and from the explicit ordinary
Legendre binomial formula after its change of variable:


$$
L_k(t)=
 \sum_{j=0}^{\lfloor k/2\rfloor}
 \frac{(2k-2j)!}{j!(k-j)!(k-2j)!}(2t-1)^{k-2j}.
$$


It then evaluates the original rational factorial and exponential
partial sums exactly. It uses neither the author's modular tail
engine nor the author's Legendre recurrence. The two H,K coordinates
are additionally checked against their direct factorial functionals.

Every H,K,A,B,C coordinate agrees with the author's certificate.
The independently obtained zero sets of C are


$$
\begin{array}{c|c}
 p&\{r:\mathscr C_r=0\pmod p\}\\ \hline
 5&\{1\}\\
 7&\{1,2,3\}\\
 11&\{1,2\}\\
 13&\{1\}\\
 17&\{1,3,11\}\\
 19&\{1,14\}.
 \end{array}
$$


These are complete scalar seeds for a proved transfer identity,
not samples used to guess an all-index theorem.

The independent checker is check_hp_b1_uniform_prime_independent.py;
its full output is hp_b1_uniform_prime_independent_certificate.json.
Both are saved in this session. No canonical HP solve, factorization,
or extension of the prime list was performed.

## 4. Analytic root-disk lift and its full-depth consequence

I checked the restricted-series construction in Sections 1–2 of
hp_b1_residue_one_actual_numerator.md. The product of the two
falling factorials has the claimed Gauss lower bound after division
by b!c!, namely k-v_p(k!) with k=floor((b+2c)/p).
The inner series D(X)=sum_r (X)_r is uniformly integral on each
disk, including the affine arguments 2X-R and 2X+1-R.
The denominator X+1=2+pY is an analytic unit.
Thus the four interpolants converge coefficientwise in Z_p<Y>.
In particular A=3 and B=10 modulo p as entire residue series.

The first-lift dependency has been read directly. It retains the
high-tail terms R in [p,2p), which produce the quadratic first-lift
coefficient. That coefficient is pH_1Y^2, respectively pJ_2Y^2;
both vanish because H_1=J_2=0. This justifies affine lifts here:
ordinary index differentiation alone would not have sufficed.
The exact index slopes are H'(1)=-3/2 and K'(1)=4.
The latter follows from the adjacent identity, with the second
x-derivative interpolant having index slope 3 and the remaining
linear term contributing 1.

Consequently, coefficientwise for every p>=5,


$$
H(1+pY)=-\tfrac32pY,\quad K(1+pY)=4pY
       \pmod{p^2},
$$




$$
C(1+pY)=27pY\pmod{p^2}.
$$


The exact value C(1)=0 is crucial. Dividing the remainder by Y
therefore preserves integral restricted coefficients, so
C(1+pY)/(pY) is a unit throughout Z_p. This proves, at every
depth a=v_p(n-1)>=1,


$$
v_p(\mathscr C_n)=a,\qquad
 v_p(H_n)\ge a,\quad v_p(K_{n+1})\ge a.
$$


There is no restriction to the first lift a=1.

For a separate exact check of the two critical primes, my checker
truncates R<2p by the proved Gauss tail bound, computes numerator
coefficients modulo p^3 before any one-power denominator loss,
and retains all potentially surviving Y coefficients. It gives


$$
\begin{array}{c|c|c|c}
 p&\text{modulus}&H(1+pY)&K(1+pY)\\ \hline
 5&25&5Y&20Y\\
 13&169&65Y&52Y
 \end{array}
$$


and C congruent respectively to 10Y modulo 25 and 13Y modulo 169.
All omitted higher coefficients have a proved zero reduction.
This is an independent coefficientwise certificate, not evaluation
at finitely many integer indices.

## 5. Strict separation proves the reduced-denominator statement

The rational second-kind convolution gives
v_p(Q_k)>=-floor(log_p k). Write f=v_p(n!) and
L=floor(log_p(n+1)). For n>=p and p odd, 2f>L.
If L=1 the claim follows from f>=1; if L>=2, then
n>=p^L-1 and 2f>=2(p^(L-1)-1)>L.

Away from residue 1 at p=5 or 13, the independent seeds make
C_n a unit. Hence the exponential part of the actual numerator
has valuation -2f, strictly less than the Q part's lower bound -L.
No cancellation is possible, and


$$
v_p(q_n)=2f+v_p(\Delta_n)\ge2f.
$$


On residue 1, put a=v_p(n-1). The lifted numerator has valuation
a-2f, while the Q part has valuation at least a-L.
Again the least term is unique. Since Delta_n is an integer
divisible by p^a,


$$
v_p(q_n)=2f+v_p(\Delta_n)-a\ge2f.
$$


The max-with-zero in rational reduction is harmless because these
right-hand sides are nonnegative. No unit hypothesis on P_n has
been used.

Therefore the actual, fully reduced denominator satisfies


$$
\boxed{v_5(q_n)\ge2v_5(n!),\qquad
        v_{13}(q_n)\ge2v_{13}(n!)}
$$


for every sufficiently large n, in every residue class.
The only eventual qualification is the accepted nonzero-endpoint
domain; n>=13 suffices for both elementary factorial comparisons.

## 6. The all-even exclusion follows for this actual family

The already independently passed dyadic theorem gives, for even n,
v_2(q_n)>=2v_2(n!)-n/2. All three prime bounds concern the same
reduced q_n. Legendre's factorial valuation formula yields


$$
\liminf_{\substack{n\to\infty\\2\mid n}}\frac{\log q_n}{n}
 \ge L_*:=\tfrac32\log2+\tfrac12\log5+\tfrac16\log13.
$$


The accepted full evaluated b=1 error has exponent
-2log(1+sqrt2), including its actual endpoint normalization.
Hence


$$
\boxed{
 \liminf_{\substack{n\to\infty\\2\mid n}}
 \frac1n\log|\mathcal L_n|
 \ge L_*-2\log(1+\sqrt2)>0.}
$$


In particular the primitive integer forms diverge along all even
indices. The strict inequality needs no floating-point evidence:
already 2^(3/2)5^(1/2)=2sqrt10 exceeds
(1+sqrt2)^2=3+2sqrt2, because 40>17+12sqrt2.
The positive prime-13 contribution only strengthens the gap.
The synthesis source's separate integer-power certificate also
checks: 832000>(1+sqrt2)^12=19601+13860sqrt2.

This excludes every even-index shrinking subsequence of the b=1
family. It does not establish whole-family exclusion, odd-index
coverage, or irrationality of e+pi. No such claim is promoted here.
