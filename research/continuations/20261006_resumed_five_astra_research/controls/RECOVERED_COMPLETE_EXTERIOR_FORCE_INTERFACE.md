> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Recovered all-row complete exterior-force interface

This is a documentary recovery and direct algebraic consequence of the existing exact contact source, not a new assumed recurrence. Read COMPLETE_CONTACT_FORCE_SOURCE_EXCERPT.md equations4--11, whose original source and SHA are stated there. Its h^e_i and h^F_i formulas apply to EVERY row0<=i<b.

Write lambda_s=s![z^s]phi(z)^n, phi=1-z+z^2/2. The complete extended matrix after the finite U_n conversion is

    A_ext(i,j)=sum_s lambda_s binom(n+i,s) binom(2n+i-s,j), j>=0.

This follows exactly from tildeN U_n and Vandermonde. For each row its degree is finite. Let D_m=m!sum_(r=0)^m1/r! and L_m=m![z^m](F/(1-z)), F'=2/phi,F(0)=0. The actual complete contact force is

    h^e_i=sum_s lambda_s binom(n+i,s)D_(2n+i-s),
    h^F_i=sum_s lambda_s binom(n+i,s)L_(2n+i-s).

The exact factorial identity

    D_m=sum_(j=0)^m binom(m,j)j!

gives, row by row,

    h^e_i=sum_(j>=0) A_ext(i,j)j!.

Let I=0..b-1 and t=(j!)_(j in I). Then the actual normalized residual vector is

    r=(h^e+h^F-A_II t)/b!
     =A_IE z+h^F/b!,
    z_h=(b+h)!/b!, h>=0.

The exterior sum is finite at each row; no infinite tail has been substituted. Thus the FULL exponential component is exactly A_IE z on EVERY finite contact row. Agreement is not limited to the two initial charges.

The actual reconstruction R has rows0..b, (R x)_j=binom(n+2,j)(j x_(j-1)-x_j), x_-1=x_b=0. Consequently

    R t=-e0+b!binom(n+2,b)e_b,

and the complete documentary contact identity yields

    V_w=R A_II^-1(h^e+h^F)+e0
       =R A_II^-1(h^e+h^F-A_II t)+b!binom(n+2,b)e_b.

Therefore Y=V_w/b! is precisely

    Y=R A_II^-1 r+W_b e_b.

This is the actual A2 finite residual convention. All interior rows, the two initial charges, the factorial subtraction and the inclusive physical terminal are retained. A2's recurrence representation of r is an alternative description of this same full vector, not a new free forcing choice. If a previously recorded recurrence has an incompatible sign or scaling, reconcile it against these exact source identities instead of deleting its residual.

At fixed precision p^K, omission of h^F/b! is legitimate only after its proved whole-row logarithmic guard has been paid. When that guard is at leastK, the required EF_K identity is a consequence of this documentary recovery:

    r=A_IE z mod p^K.

The selected fixedp6 guard in A2turn13 is well above6 on the original29family. This closes its packet-relative missing ALL-ROW force interface. It does not prove that its subsequent exterior inverse truncation, displacement/shift bounds, both endpoint returns, source saturation or conditional mixed conclusion are correct; those need their stated independent checks. It does not determine the actual norm-relative depth d-c, primitive mixed digit, all-prime q or whole same-index error.
