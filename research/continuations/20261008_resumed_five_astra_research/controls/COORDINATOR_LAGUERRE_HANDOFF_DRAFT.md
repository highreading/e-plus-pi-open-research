> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

Divided Laguerre coordinates and complete borders
Coordinator scratch retained at the explicit user stop on 9 October 2026

STATUS: DRAFT. These are ideas derived before the stop, retained to avoid
losing context. No complete independent audit or paired upper theorem is
claimed. The finite diagnostics have only their stated bounded scopes.

The classical Laguerre Rodrigues formula, orthonormality for e^(-t) dt and
the earlier integral quadratic operator are reused. Primary classical
references are https://dlmf.nist.gov/18.5 and https://dlmf.nist.gov/18.12.
The old WEIGHTED_DETERMINANT_DYADIC_GATEWAY uses T=(X^2+I)/2. The proposed
variable here is y=t(t-2)/2=((1-t)^2-1)/2, so its operator is T-I.
The affine shift must be retained in any actual-source application.

Set x=1-t and let C_r be the Laguerre-coordinate vector of y^r/r!.
The proposed all-degree coordinate identity is

 C_(r,m)=(-1)^m sum_(s=0..r) (-1)^(r-s) (2s-1)!!
           * binom(r+s,2s) * binom(r+s,m),

with (-1)!!=1 and zero coordinates for m>2r. The proof sketch expands
y^r/r! and uses integral t^n L_m(t)=(-1)^m n! binom(n,m).
The integer coefficient identity is

 (r+s)! / [2^s s! (r-s)!]
       = (2s-1)!! binom(r+s,2s).

Its leading coordinates are C_(r,2r)=(2r-1)!! and
C_(r,2r-1)=-(2r-1)(2r-1)!!. They are odd. The even-coordinate square
minor of C_0,...,C_R is triangular with odd diagonal. This says nothing
by itself about the rank or depth of their Gram matrix.

The integer symmetric multiplication matrix for x has diagonal -2m and
off-diagonal entries m+1. Therefore x^(2a) C_s has integer coordinates.
The physical contact identity is

 <x^(2a) C_s,C_r> = binom(r+s,r) theta_(r+s)^(a).

The closed coordinate cache checks r=0..32 and 561 Gram pairs. A separate
new diagnostic reuses that cache, rather than reconstructing it, and
checks 648 physical cases with r,s=0..8 and a=1..8.

The proposed actual top source polynomial is

 L_j^a = sum_(h=0..d) binom(d,h) Q_h(a)
                   x^(2(a+h)) y^(d-h+j)/(d-h+j)!.

Its contact pairing is T_j^a(r)/o_d. For even d, the full top atom is
A_j^a=(d+j)! L_j^a(y=-1). The rising ratio then gives the same (d+m)!
evaluation in the complete normalized matrix. Bottom atoms remain zero;
they must not be replaced with evaluation of the bottom polynomial.
The bottom contact polynomial keeps every actual J_ell and physical
base d+ell. No original return or physical terminal is extended.

For the one-shot physical functional in A2 turn18, retain the exact
coefficients ell_(i,m), including R, N_d, mu_A, K_A and delta_k/4. Set

 h_i(t)=2^(-alpha) sum_(m=0..2d+1) ell_(i,m) (1-t)^(2m).

Then W_i^(r)=integral e^(-t) h_i(t) y^r/r! dt. A proposed integer-source
argument uses the exact split in A4 turn27 (1.4), under the actual H8
handoff hypothesis. Its top term has the factor o_d; the bottom term
has 2^(alpha-12)*gamma. Neither factor should be dropped. The source
coordinate support is at most 4d+2, independently of precision. This
does not prove a small primitive pair or integrality after any further
unpaid normalization. In particular it does not reinstate the failed
stronger integral W descent.

The reflection constants satisfy

 beta_m = integral e^(-t) L_m(1-t) dt
        = sum_(j=0..m) binom(m,j) !j/j!.

The numerator m! beta_m is odd: all terms except the last two contain
m(m-1), and exactly one of the last two terms is odd. The new diagnostic
checks this formula by direct polynomial integration through m=64.

For a divided y^r/r! source reflected by t -> 1-t, its factorial value
has numerator F_r=sum_j binom(r,j)(-1)^(r-j)(2j)!, which is odd, over
the full divisor 2^r r!. The complete rational arc comes from the
INTEGER quotient [(z-1)^r-(-2)^r]/(z+1), evaluated at z=t^2. With the
original odd clearer, the full -Gamma+4*arc numerator remains odd.
The new diagnostic checks the complete-border identity through r=32.
Individual odd numerators do not exclude cancellation between actual
row coefficients, and do not yield the desired joint determinant upper.

For any future proof write-up, verify the actual-source correspondence,
the exact H8 assumptions, o_d, both borders, selected atom and return
relations, full factorial divisors and all-prime content. Do not assign
an individually rational arc to each reflected Laguerre polynomial:
the rationality statement belongs to the complete even polynomial.

No new request, independent audit or additional calculation was made
to finish this scratch after the user's stop instruction.
