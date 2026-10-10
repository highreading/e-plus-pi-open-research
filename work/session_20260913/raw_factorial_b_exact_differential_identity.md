> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact differential identity for the primitive factorial coordinates

2026-09-13. Original continuation by root. Independent review requested
from audit_sources as part of the general small-residue transfer.
Independent review: **PASS**, recorded in
raw_factorial_b_differential_independent_review.md.

All notation is the actual original primitive construction, with

    W(t)=t^n(t-1)^n V(t),
    S(t)=(1+t^2)^n U(t),
    U(t)=sum_(j=0)^n U_j t^j,
    b(t)=sum_(j=0)^n U_j/(n+j)! t^j in Z[t].

The integrality and primitivity of the b vector were already proved.
Let D denote ordinary differentiation in t. Then the exact identity is

    (t-1)^n V(t) = (1+D^2)^n [t^n b(t)].                 (1)

This is not just an identity of high coefficients. Indeed the previously
proved reconstruction S^(n)=Traw gives, coefficient by coefficient,

    w_(n+r)=S_(n+r)/r!,          0<=r<=2n,

because Traw_r=(n+r)! w_(n+r). On the other hand the coefficient of
 t^r in the right side of (1) is

    sum_(h=0)^n binom(n,h) U_(r-n+2h)/r!
      = S_(n+r)/r!,

where U_j is zero outside 0<=j<=n and in the second sum one replaces h
by n-h. The left side is W/t^n and has exactly these coefficients.
All factorial divisions have been accounted for in this derivation.

## A general transfer lemma

Let p be prime, 0<=k<p, n=k+mp with m>=0. Suppose c is a p-integral
scalar and the actual factorial polynomials satisfy

    b_n(t) = c (t-1)^(n-k) b_k(t) mod p.                 (2)

The fixed low-degree V_k and b_k must use the SAME Appell/background
construction; no comparison to an arbitrary model is asserted.
Then

    V_n(t) = c t^(n-k) V_k(t) mod p.                     (3)

Proof. Work in F_p[t]. The derivation D satisfies D^p=0, since the
product of p consecutive integers is divisible by p. Hence

    (1+D^2)^n=(1+D^2)^k.

Also t^n b_n = c [t(t-1)]^(mp) t^k b_k. The derivative of the bracketed
factor is zero in characteristic p, so every power of D commutes with
multiplication by that factor. Applying (1) and then (2) gives

    (t-1)^n V_n
      =c [t(t-1)]^(mp)(t-1)^k V_k.

Cancel the nonzero polynomial (t-1)^n in F_p[t]. This proves (3).
The argument retains every low coefficient and avoids an unjustified
truncation after a large polynomial factor is introduced.

If moreover p>2k, the exact integral endpoint border implies

    Pe_n(1) = c Pe_k(1) mod p.                           (4)

For each surviving monomial of V_k indexed by s in [0,k], the large
index is r=n-k+s. Its border is

    D_(n,r)=sum_j binom(n+j,j)(n+r)_j.

Terms j>=p vanish modulo p because of the falling factorial. For j<p,
Lucas (or the elementary product formula with j! a unit) reduces the
first binomial to binom(k+j,j); the falling factorial reduces to
(k+s)_j. Since k+s<=2k<p, all terms j>k+s also vanish. This is exactly
D_(k,s) modulo p. Substitution into Pe=sum V_r D proves (4).

Thus a separately proved small-residue congruence for b transfers
DIRECTLY to the actual Rodrigues polynomial and exponential numerator.
The remaining hypothesis in (2) is being derived by a same-size
augmented-Schur comparison and Lucas factorization. No assertion that
(2) always holds is made independently of that proof.
