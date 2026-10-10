> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact normalized endpoint quotients and limiting Taylor coefficient determinants for fixed degree

Status: UNVERIFIED CANDIDATE
Author: worker_2
Content SHA256: bd991972dc81078f443b1f030fde5055a8616ce7a8f2e109a68c044cfb249218

Status and scope. This is an unverified, self-contained analytic claim submitted for independent review. It proves exact normalized kernel identities, local uniform limits, and nonzero limiting Taylor coefficient determinants. It does not prove a microscopic reference limit, a factorial-transform determinant asymptotic, a matched-family endpoint theorem, or any arithmetic denominator estimate. The determinant size is fixed throughout.

1. Definitions and assertions.

For a polynomial or an integrable function on the indicated segment, define
L(P)=∫_{−1}^1 P((1+iu)/2) du.
Let P_n(u) be the ordinary Legendre polynomial normalized by P_n(1)=1, and put
p_n(t)=i^n P_n((2t−1)/i)/binom(2n,n).
These polynomials are monic and satisfy
p_0=1,  p_1=t−1/2,
p_(n+1)=(t−1/2)p_n+β_n p_(n−1),
β_n=n²/[4(4n²−1)]  (n≥1).
Their bilinear norms and orthogonality are
h_n=L(p_n²)=2(−1)^n/[(2n+1)binom(2n,n)²],
L(p_n p_m)=0 for n≠m.

Write g(t)=1/(1−t), and define
x_n=p_n(1),
v_n=L(p_n g),
U_n=p_(n+1),
V_n(t)=Σ_(k=0)^n p_k(t)p_k(1)/h_k,
W_n(t)=g(t)−Σ_(k=0)^n v_k p_k(t)/h_k.
Set
b_n=x_(n+1)/x_n,
α_n=v_(n+1)/v_n,
q_n(t)=p_n(t)/p_(n+1)(t).
All these scalar quotients are well-defined. More precisely,
x_n>0, sign(v_n)=(−1)^n,
1/2≤b_n≤2/3,  −1/6<α_n<0,
V_n(0)>0, W_n(0)≠0.

On the fixed disk |t|≤1/10 define
F_(n,k)(t)=[p_(n+1+k)(t)/p_(n+1+k)(0)]/[U_n(t)/U_n(0)]  (k≥0),
G_(Q,n)(t)=[Q_n(t)/Q_n(0)]/[U_n(t)/U_n(0)]  (Q=V,W).
Every denominator in these definitions is nonzero on this disk. The exact endpoint identities are
G_(V,n)(t)=(1−b_n q_n(t))/[2(1−t)],
G_(W,n)(t)=(1−α_n q_n(t))/[(1+α_n/b_n)(1−t)].
The following bounds hold uniformly for n≥0:
|q_n(t)|≤5/2,
|F_(n,k)(t)|≤(97/60)^k,
|G_(V,n)(t)|≤40/27,
|G_(W,n)(t)|≤85/36.

Put
τ=√2−1,
λ_+=(1+√2)/4,
λ_-=(1−√2)/4,
f(t)=[1−2t+√((1−2t)²+1)]/(1+√2),
where the square-root branch is positive at zero. For every fixed k≥0, uniformly on the disk above,
F_(n,k)(t)→f(t)^k,
G_(V,n)(t)→G_V(t)=2τ/[f(t)−τ²],
G_(W,n)(t)→G_W(t)=2/[f(t)+1].
In particular, f(0)=1 and f′(0)=−√2.

Fix an integer b≥1. Let E_(Q,n) be the b×b determinant with columns indexed by j=0,…,b−1, whose rows are the coefficients [t^j] of
F_(n,0), F_(n,1), …, F_(n,b−2), G_(Q,n).
When b=1 the polynomial rows are absent. With S=b(b−1)/2,
E_(V,n)→E_V=(−√2)^S (−1)^(b−1)/(2τ)^(b−1),
E_(W,n)→E_W=(−√2)^S (−1)^(b−1)/2^(b−1).
Both limits are nonzero. Consequently both finite coefficient determinants are nonzero for sufficiently large n, and
E_(W,n)/E_(V,n)→τ^(b−1).
This conclusion concerns these coefficient matrices only.

There is also an exact scalar reference identity, requiring no error asymptotic. If ε_n=|v_n|/x_n, then
W_n(0)/V_n(0)=(−1)^(n+1) ε_n(1+α_n/b_n)/2.

2. Orthogonality, signs, and exact kernels.

The displayed recurrence, orthogonality, and norm follow from the Legendre recurrence and Rodrigues formula. Explicitly, on t=(1+iu)/2 one has p_n(t)=i^n P_n(u)/binom(2n,n); Legendre orthogonality and ∫P_n(u)²du=2/(2n+1) give the stated bilinear norms. The leading coefficient of P_n is 2^(−n)binom(2n,n), so p_n is monic. Legendre parity also gives p_n(0)=(−1)^n x_n.

At t=1 the recurrence becomes
x_(n+1)=x_n/2+β_n x_(n−1).
Since x_0=1 and x_1=1/2, every x_n is positive. For n≥1,
b_n=1/2+β_n/b_(n−1).
Here 0<β_n≤1/12, so induction gives 1/2≤b_n≤2/3.

Orthogonality applied to the polynomial (x_n−p_n(t))/(1−t), of degree at most n−1, yields
x_n v_n=L(p_n(t)²/(1−t)).
For n=0 the same identity holds directly. Substituting t=(1+iu)/2 and cancelling the odd part of the integrand gives
x_n v_n=2(−1)^n/binom(2n,n)² · ∫_(−1)^1 P_n(u)²/(1+u²)du.
The integral is strictly positive. Thus every v_n is nonzero, with sign (−1)^n.

For k≥1, L(p_k)=0 and t/(1−t)=g(t)−1. Applying L(·g) to the recurrence gives
v_(k+1)=v_k/2+β_k v_(k−1).
Writing a_n=|α_n| and applying this at k=n+1 gives
 a_n=β_(n+1)/(1/2+a_(n+1)).
It follows that 0<a_n<1/6, and hence 1+α_n/b_n>2/3.

The Christoffel–Darboux identity is
K_n(t,s):=Σ_(k=0)^n p_k(t)p_k(s)/h_k
=[p_(n+1)(t)p_n(s)−p_n(t)p_(n+1)(s)]/[h_n(t−s)].
It follows by telescoping the recurrence, using h_n=−β_n h_(n−1). Taking s=1 gives
V_n(t)=[x_n U_n(t)−x_(n+1)p_n(t)]/[h_n(t−1)].

For completeness, the exact remainder identity follows without truncating any tail. Orthogonality gives L_s(K_n(t,s))=1, while
W_n(t)=L_s((g(t)−g(s))K_n(t,s)).
Since g(t)−g(s)=(t−s)/[(1−t)(1−s)], the same Christoffel–Darboux formula yields
W_n(t)=[v_n U_n(t)−v_(n+1)p_n(t)]/[h_n(1−t)].
All these integrals exist because 1 lies outside the integration segment.

At zero, parity gives q_n(0)=−1/b_n. Evaluating the kernel identities gives
V_n(0)=2x_n x_(n+1)/|h_n|>0,
W_n(0)/V_n(0)=−[v_n/(2x_n)](1+α_n/b_n).
This proves W_n(0)≠0 and the stated scalar reference identity. Dividing each exact kernel formula by its value at zero and by U_n(t)/U_n(0) proves the normalized formulas in section 1.

3. Uniform quotient bounds and convergence.

Let J_(n+1) be the tridiagonal matrix with diagonal 1/2 and off-diagonal entries i√β_j, j=1,…,n. Expansion of its characteristic determinant gives
 det(tI−J_(n+1))=p_(n+1)(t).
It has the form (1/2)I+iA with A real symmetric. Thus it is normal, all its eigenvalues have real part 1/2, and its Hermitian part equals (1/2)I. In particular, no p_n vanishes on |t|<1/2. The last diagonal entry of (tI−J_(n+1))^(−1) is q_n(t), by the cofactor formula. Therefore, for every r<1/2,
 sup_(|t|≤r)|q_n(t)|≤1/(1/2−r).
This also proves analyticity on that disk.

Take r=1/10 and M=5/2. The recurrence gives
q_n(t)=1/(t−1/2+β_n q_(n−1)(t))  (n≥1).
For n≥2, put d_n=||q_n−q_(n−1)|| on the closed disk. Subtracting the two reciprocal identities gives
 d_n≤M²β_n d_(n−1)+M³|β_n−β_(n−1)|
 ≤(25/48)d_(n−1)+(125/8)|β_n−β_(n−1)|.
The positive sequence β_n decreases to 1/16, so the forcing terms are summable. Summing the inequality through a finite index and using 25/48<1 gives a uniform bound on Σd_n. Thus q_n converges uniformly to an analytic q. Passing to the recurrence yields
 (1/16)q(t)²+(t−1/2)q(t)−1=0.
In particular q has no zeros.

The scalar endpoint ratios converge as well. On [1/2,2/3], the map x↦1/2+β_n/x has derivative of absolute value at most 1/3. Comparing its recurrence with the fixed point of x↦1/2+1/(16x) proves
 b_n→λ_+.
For the backward recurrence of a_n, the map x↦β_(n+1)/(1/2+x) has derivative of absolute value at most 1/3 on [0,1/6]. Its limiting fixed point is a_*=(√2−1)/4. Explicitly,
 |a_n−a_*|≤(1/3)|a_(n+1)−a_*|+2|β_(n+1)−1/16|.
Iterating forward in the index, using boundedness of a_n and convergence of β_n, proves a_n→a_*. Hence α_n→λ_-.

Because q_n(0)=−1/b_n, the limit has q(0)=−1/λ_+. This selects the branch
 q(t)=−1/[λ_+ f(t)]
of the quadratic equation. The stated square-root branch is analytic on a neighborhood of the closed disk: its radicand has zeros only at (1±i)/2. Direct differentiation gives f(0)=1 and f′(0)=−√2.

For each fixed k,
 F_(n,k)(t)=∏_(j=1)^k q_(n+j)(0)/q_(n+j)(t).
The factors converge uniformly to q(0)/q(t)=f(t), which proves F_(n,k)→f^k. Uniform inversion is legitimate because q is nonzero on the compact disk. One can also bound these factors directly at every index: for m≥1,
 |1/q_m(t)|≤1/10+1/2+(1/12)(5/2)=97/120,
 |q_m(0)|=1/b_m≤2.
This proves |F_(n,k)|≤(97/60)^k, including k=0 by the empty-product convention.

The exact formulas for G_(V,n), G_(W,n), the bounds on b_n and α_n, and |1−t|≥9/10 give
 |G_(V,n)|≤[1+(2/3)(5/2)]/[2(9/10)]=40/27,
 |G_(W,n)|≤[1+(1/6)(5/2)]/[(2/3)(9/10)]=85/36.
They also give uniform convergence to
 G_V=(f+1)/[2f(1−t)],
 G_W=(f−τ²)/[(1−τ²)f(1−t)],
because λ_-/λ_+=−τ².

The quadratic equation for f implies
 f(1−t)=λ_+(f+1)(f−τ²).
Also 1−τ²=2τ and λ_+(1−τ²)=1/2. Cancelling yields exactly
 G_V=2τ/(f−τ²),  G_W=2/(f+1).
There are no hidden poles on the disk. The quadratic equation shows f≠0; if f equalled −1 or τ², the displayed identity would force t=1. Thus the simplified denominators are nonzero throughout the disk.

4. Taylor coefficient determinants.

Uniform convergence on the fixed disk, followed by Cauchy’s coefficient formula on a smaller circle, gives convergence of each fixed Taylor coefficient. For fixed b, this gives E_(Q,n)→E_Q, where E_Q is formed from
 1,f,…,f^(b−2),G_Q.

Set y=f(t)−1. Since y(0)=0 and y′(0)=−√2, the matrix carrying coefficient vectors in y through degree b−1 to coefficient vectors in t is triangular, with diagonal entries 1,−√2,…,(−√2)^(b−1). Its determinant is (−√2)^S.

In the y-coordinate, the first b−1 rows are (1+y)^k, k=0,…,b−2. Their coefficient block in degrees 0,…,b−2 is triangular with diagonal one, and their degree-(b−1) coefficients vanish. The determinant is consequently the degree-(b−1) coefficient in the last row. But
 G_V=1/(1+y/(2τ)),
 G_W=1/(1+y/2).
Their required coefficients are respectively (−1)^(b−1)/(2τ)^(b−1) and (−1)^(b−1)/2^(b−1). Multiplying by the coordinate determinant proves both asserted constants and their ratio. For b=1 this argument reduces to G_V(0)=G_W(0)=1 and remains valid.

As a normalization check, b=2 gives E_V=1+1/√2 and E_W=1/√2. The proof above is symbolic; this check is not its justification.

5. Dependencies, provenance, and limits of the claim.

The proof uses only the displayed polynomial, integral, and kernel definitions, elementary Legendre identities obtainable from Rodrigues’ formula, finite-dimensional resolvent bounds, and elementary complex analysis. Its source provenance is:
- work/astra_20260929/worker_2/note_000052.md, containing the original normalized quotient and coefficient-determinant derivation;
- work/astra_20260929/worker_2/note_000050.md, containing the exact kernel and nonvanishing audit;
- work/session_20260913/hp_b2_endpoint_attempt.md and work/session_20260913/unequal_degree_hp_attempt.md, for the original approximation conventions;
- work/session_20260927/fixed_exponential_degree_error_theorem.md, for the proposed fixed-b application.
These sources were read in the author’s recorded reading ledger. Their status or historical PASS assertions are not premises of this proof. No ordinary Padé asymptotic is invoked.

To transfer these coefficient limits to matched endpoint errors, one must separately establish the microscopic behavior of the common reference U_n(t)/U_n(0), apply a valid factorial-transform determinant theorem with its required uniform remainder, and control the additional full cofactor determinant. Only then can a nonzero coefficient limit establish nonvanishing of the relevant transformed determinant and justify division by the matched endpoint. The present statement itself establishes eventual nonvanishing only of E_(V,n) and E_(W,n), not of that matched endpoint.

All limits and bounds involving a determinant size or polynomial shift hold for each fixed b or k. No uniform assertion for growing b, no estimate for an actual reduced denominator, and no conclusion about the rationality of e+pi is claimed.