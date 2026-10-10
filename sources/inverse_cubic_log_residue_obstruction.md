> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Inverse-cubic model for the corrected fresh-prime obstruction

## Scope and status

This note gives an exact inverse-function model for the fixed logarithmic
coefficients $\Lambda_s$, derives their minimal generic differential rank,
and certifies the resulting coefficient recurrence.  It is a structural
local-pivot obstruction, not a fresh-prime nonvanishing theorem.  In
particular, the correct recurrence has eight terms, so the three zeros
furnished by the corrected A/B reduction do not by themselves give a
one-row pivot to a nonzero initial coefficient.

## 1. The fixed coefficients and the nonexceptional equivalence

Put



$$
\Lambda_s(m)=[y^{4m+s}]
 \frac{(1-y)^{6m}(1+y)^{1+3s}}
 {(1+y^2)^{4m+1+s}}.
$$



The exact adjacent differential identity gives



$$
16a_m\Lambda_0+4b_m\Lambda_1+c_m\Lambda_2=0,       \tag{1.1}
$$



where



$$
a_m=(10m+2)(10m+3),\qquad
 b_m=-(10m+3)(20m+5),\qquad
 c_m=8(2m+1)(4m+1).
$$



Let $p>6m$ be prime.  Then $c_m$ and $10m+2=2(5m+1)$
are p-units.  Consequently, if $p\ne10m+3$, then



$$
(\Lambda_1,\Lambda_2)\equiv(0,0)\pmod p
 \quad\Longleftrightarrow\quad
 (\Lambda_0,\Lambda_1)\equiv(0,0)\pmod p.           \tag{1.2}
$$



Thus a nonexceptional coprimality theorem for the corrected pair would be
exactly the original unresolved fresh-prime log-residue theorem, not a
strictly weaker corollary.

## 2. One inverse-cubic coefficient sequence

Let



$$
n=6m,\qquad
 A(t)=-2+3t-t^2,\qquad
 R(t)=t^2-2t+2,
$$



and define



$$
c_N=[t^N]\frac{A(t)^n}{R(t)^{N+1}}.                 \tag{2.1}
$$



Indeed, for



$$
\omega_s=\frac{\{x(1-x)\}^{6m}}
 {\{(1+x)(1+x^2)\}^{4m+1+s}}\,dx,
$$



the coordinate $t=x+1$ gives



$$
\operatorname {Res}_{x=-1}\omega_s=c_{4m+s}.
$$



With the standard normalization $L_s=2\operatorname {Res}_{-1}\omega_s$,
one obtains the exact scaling



$$
\boxed{\Lambda_s=2^{2m+2s+1}c_{4m+s}.}              \tag{2.2}
$$



All powers of 2 are units at the odd fresh primes.  Hence the common-zero
condition in (1.2) supplies three consecutive zeros



$$
c_{4m}=c_{4m+1}=c_{4m+2}=0\pmod p.                  \tag{2.3}
$$



Now put



$$
\phi(t)=tR(t)=t^3-2t^2+2t
$$



and let $T(z)$ be its formal inverse at the origin.  A residue change of
variables gives



$$
\begin{aligned}
 c_N
 &=\operatorname {Res}_{t=0}
   \frac{A(t)^n\,dt}{\{tR(t)\}^{N+1}}\\
 &=[z^N]F_n(z),\qquad
 F_n(z)=A(T(z))^nT'(z)
       =\frac{A(T(z))^n}{\phi'(T(z))}.                \tag{2.4}
 \end{aligned}
$$



Thus all the shifted logarithmic residues lie in one algebraic coefficient
sequence.

## 3. Exact differential rank

Work in the cubic field



$$
\mathcal K=\mathbb Q(n,z)[t]/(\phi(t)-z)
$$



with its total derivation



$$
\delta z=1,\qquad \delta t=\frac1{\phi'(t)}.         \tag{3.1}
$$



If $r_j=F_n^{(j)}/F_n$, then



$$
r_0=1,\qquad
 r_1=\frac{nA'/A-\phi''/\phi'}{\phi'},\qquad
 r_{j+1}=\delta r_j+r_1r_j.                           \tag{3.2}
$$



Writing $r_0,r_1,r_2$ in the basis $1,t,t^2$, their determinant is



$$
-\frac{nP_n(z)}
 {(z-4)^2(z-1)^2(27z^2-40z+16)^2},                   \tag{3.3}
$$



where



$$
\begin{aligned}
 P_n(z)={}&125n^2z^3-600n^2z^2+960n^2z-512n^2\\
 &-125nz^3+900nz^2-1920nz+1280n\\
 &+20z^3-336z^2+720z-512.
\end{aligned}
$$



This rational function is nonzero.  Therefore $F_n,F_n',F_n''$ are
linearly independent over $\mathbb Q(n,z)$; the generic scalar
differential order is exactly three.  The unique order-three equation is
computed by the certificate script from the null vector of
$(r_0,r_1,r_2,r_3)$.

There is an essential audit point here.  Once a representative has been
reduced modulo $\phi(t)-z$, its derivative is



$$
\delta h=\frac{\partial h}{\partial z}
          +\frac1{\phi'(t)}\frac{\partial h}{\partial t}.            \tag{3.4}
$$



Omitting the explicit $\partial h/\partial z$ term produces a false,
shorter recurrence.  The archived certificate checks the corrected total
derivative against unreduced rational functions before accepting the ODE.

## 4. The true coefficient recurrence

Clear the common polynomial denominator in the order-three ODE and write



$$
F_n(z)=\sum_{j\ge0}c_jz^j,\qquad c_j=0\quad(j<0).
$$



Coefficient comparison gives



$$
\boxed{\sum_{h=-4}^{3}C_h(k,n)c_{k+h}=0\qquad(k\ge0),}             \tag{4.1}
$$



an eight-term recurrence.  The two edge coefficients factor as



$$
\begin{aligned}
 C_{-4}(k,n)={}&5(5n-4)(5n-1)
 (3k-2n-10)(3k-2n-9)(3k-2n-8),\\
 C_3(k,n)={}&-16384(k+1)(k+2)(k+3)(n-2)(2n-1).        \tag{4.2}
\end{aligned}
$$



The six exact middle polynomials are recorded in the JSON certificate and
are regenerated symbolically by the script; they are not inferred from
sample data.

At the target $n=6m$, $N=4m$, the three equations in (2.3) leave the
five terms



$$
c_{N-4},c_{N-3},c_{N-2},c_{N-1},c_{N+3}
$$



in the $k=N$ row.  Hence the $k=N$ row of (4.1) alone supplies no zero
propagation.  This does not exclude a multi-row or global use of the same
recurrence.  Moreover,



$$
C_{-4}(N,6m)=-3600(30m-4)(30m-1),                   \tag{4.3}
$$





$$
C_3(N,6m)=-16384(4m+1)(4m+2)(4m+3)(6m-2)(12m-1),   \tag{4.4}
$$



so even the edge pivots have additional possible fresh-prime resonances;
they are not controlled solely by the old exceptional ray
$p=10m+3$.

## 5. Certificate and conclusion

The exact generator

`scripts/inverse_cubic_log_residue_certificate.py`

performs all of the following:

1. constructs the cubic-field derivation with both terms in (3.4);
2. proves the nonzero determinant (3.3);
3. derives and verifies the unique order-three ODE against unreduced
   rational functions;
4. derives every polynomial $C_h(k,n)$ in (4.1);
5. checks (2.2) and every available recurrence row independently for
   $m=1,\ldots,12$.

The deterministic result is

`results/inverse_cubic_log_residue_certificate_m12.json`.

This reformulation is exact and independent of the A/B section proof, but
it does not prove fresh-prime coprimality.  Its precise conclusion is that
the inverse-cubic route has generic differential rank three yet an
eight-term coefficient recurrence whose target row still contains five
other coefficients after the three known zeros.  This rules out only the
immediate one-row pivot and gives no global nonvanishing conclusion.
