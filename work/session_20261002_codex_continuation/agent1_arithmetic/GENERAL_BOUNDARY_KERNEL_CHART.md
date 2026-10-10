> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The common kernel behind the fixed-b n+1 boundary chart

New author mathematics, 2026-10-02. This develops L4 after the b4 local chart; it is not an independent review. Use the exact normalized definitions and complete center c=2^n V/((n!)²D)+beta in GENERAL_FIXED_B_ODD_ORIGIN.md. Fix b>=4, 1<=m<=floor((b−1)/2), and an odd prime p>b. Assume the endpoint digits P_r are p-units for0<=r<p. All power-series arguments below are finite truncations of degrees less than b<p; they involve no analytic evaluation of a formal exponential at a p-adic point.

Put u=n+1, k=v_p(u)>=1, Delta=det N, B=adj(N)A, x=KY, t=KB. The author theorem is that constants delta_(p,b,m),nu_(p,b,m) exist with

    D_n/(u²P_n²)=delta_(p,b,m) mod p,
    V_n/(u²P_n)=nu_(p,b,m) mod p                 (1)

at every nonnegative n=-1 modulo p and every depth k. Both quotients are p-integral. Their constants are obtained at the single reference n*=p²−1 modulo p^5. If nu is a unit, the actual complete denominator satisfies

    v_p(q_n)=2v_p(n!)+v_p(D_n)−2v_p(n+1)
             >=2v_p(n!)                         (2)

at every normal boundary index n>=2p. This is a local theorem on the n+1 disk, not yet a whole fixed-b exclusion. Larger b,m can have other structural negative residue disks, identified in Section7.

## 1. Lower triangular contact map as a coefficient transform

Write q0(z)=1−z+z²/2. Index the lower rows i=1,...,b−1 by l=i−1. Reduction modulo u gives a (b−1)x b matrix T with

    T_lj=l![z^(l−j)] e^z/q0(z), 0<=j<=l,
    T_lj=0, j>l.                               (3)

Indeed (n+i)_(j+s) reduces to (i−1)_(j+s), with the short coefficient a_s(-1)=[z^s]q0(z)^(-1). Let T0 be the first b−1 columns of T. It is triangular with diagonal l!, hence p-invertible. In ordinary coefficient coordinates v(z)=sum_j v_j z^j, its action is

    (Tv)_l/l! = [z^l](e^z v(z)/q0(z)).          (4)

The last column of T is zero. The first column of adj(N) therefore has last coordinate (-1)^(b−1) product_(l=0)^(b−2) l!, a p-unit, with all earlier coordinates zero modulo u.

The endpoint source D0J has every lower coordinate divisible by u. Solving NY=Delta D0J with T0 proves Y_j is divisible by u for j<=b−2. Modulo p, its last coordinate is the displayed p-unit times P_n. At n=-1,

    K0=Z(I+Dpol),
    K0 e_(b−1) has support in rows b−2,b−1,b.    (5)

For every allowed b>=4,m, m<=b−3. Consequently x_j is divisible by u for all metric rows0<=j<=m, while every remaining weight Omega_j=(u+m)_j² has a u² factor. Thus D is divisible by u².

## 2. The backward Dcal parameter has the same annihilator

Keep R=Dcal_(2u−1) at its actual p-adic precision; only R modulo p is fixed as C_p=Dcal_(p−1). Define Dcal_(-1)=R solely as a symbol in the finite short-row formula, and define

    Abar_l(R)=sum_(s=0)^l [z^s]q0(z)^(-1) (l)_s Dcal_(l−1−s).

These are exactly the lower A rows modulo u. Their exponential coefficient generating function through degree b−2 is

    sum_l Abar_l(R) z^l/l!
       =q0(z)^(-1)[R+integral_0^z e^s/(1−s) ds].             (6)

This uses sum_(j>=0)Dcal_j z^j/j!=e^z/(1−z), an exact formal identity from Dcal_j=j!sum_(r=0)^j1/r!.

Combining (4),(6), the zeroth-order lower solution B_j is Delta times the coefficients through degree b−2 of

    b_R(z)=e^(−z)[R+integral_0^z e^s/(1−s) ds].              (7)

Its decisive identity is

    (I+partial_z)b_R(z)=1/(1−z).              (8)

Thus K0B has first coordinate -Delta, and coordinates1,...,b−3 equal0, modulo u. In particular t0+Delta and t_j,1<=j<=m, are divisible by u. The complete numerator retains kappa in the identity

    V=x0(t0+Delta)+sum_(j=1)^b Omega_j x_j t_j.               (9)

Equations (5),(8),(9) prove V is divisible by u². Removing the correction would destroy this forced normalization.

The entire R dependence in (7) is R e^(−z). Its image under I+partial_z is zero in every available coefficient degree. This explains the cancellation without a full N inverse.

## 3. Uniform first-order precision, including the first depth

There are fixed p-residue matrices G and vectors F, depending only on p,b, with

    N_lower=T+u(G+epsilon T) mod p^(k+1),
    A_lower=Abar(R)+u(F+epsilon Abar(C_p)) mod p^(k+1),       (10)

where epsilon=u/p modulo p for k=1, and epsilon=0 for k>=2. R in Abar(R) remains exact to the required precision.

For completeness, in row i a falling factorial of length at least i contains u. A length at least p+i contains u and u−p, so its contribution vanishes modulo p^(k+1), or is outside the finite sum if u=p. Short coefficients s<i have p-unit polynomial denominators because i<b<p; they admit a first-order expansion at n=-1. All other surviving terms have their u factor already, so they require a_s(n) only modulo p and Dcal only modulo p.

For n=u−1,

    q0(z)^n=q0(z^p)^(u/p)/q0(z) mod p.

All relevant degrees are below p+b−1<2p. At k>=2 the remaining q0(z^p) factor is1 to this precision. At k=1 its only extra coefficients are -epsilon [z^ell]q0(z)^(-1) in degree p+ell,0<=ell<=b−2. Wilson's theorem gives, whenever j+ell<=i−1,

    (u+i−1)_(p+j+ell)/u=−(i−1)_(j+ell) mod p.

The product of these two minus signs gives exactly the common scale u epsilon T in N. For A, the same sum sees the modulo-p Dcal value with offset i−2−ell, with the offset -1 interpreted as C_p. It therefore gives u epsilon Abar(C_p). The fixed short Dcal offsets0,...,b−3 are propagated polynomially from the actual R by the recurrence, so their first-order dependence requires only R modulo p=C_p. This proves (10).

In solving the lower B equations through one more p-adic digit, the epsilon terms cancel: T0 applied to Delta b_R is Delta Abar(R), and Abar(R)−Abar(C_p) has a p factor. The last column of T is zero. The unknown higher R digits are also eliminated by (8). Hence

    (t0+Delta)/u, t_j/u for1<=j<=m,

modulo p are fixed functions of the fixed N,A seed, G,F and C_p. They are independent of k, u/p and the higher digits of R. Delta may be0 modulo p; T0 is the only matrix inverted.

## 4. Endpoint carry is exactly the same e^(−z) direction

Write n=pa−1 and W0(z)=z^(-1)+2+2z. Frobenius and the support interval show

    J_i(n)=P_(a−1)J_i(p−1)+h c_i mod p,
    h=CT_z W0(z)^(a−1)z,
    c_0=0,
    c_i=[y^(i−1)](1+y)^i/(1+y+y²/2), i>=1.                (11)

Only the low exponents0,p can couple to the high factor: its interval is[-p+1,p−1+i], with i<p. The upper-edge coefficients of W0^(p−1) equal those of (1+y+y²/2)^(-1) through degree b−2, proving (11).

The carry source in lower row l=i−1, after dividing D0_i by u, is h l!c_(l+1). A direct binomial transform gives

    sum_(l>=0)c_(l+1) z^l
      =(1−z)^(-2) (1+z/(1−z)+(z/(1−z))²/2)^(-1)
      =q0(z)^(-1).                                      (12)

All uses of (12) are truncated below b<p. Comparing (4),(12), T0^(-1) maps this carry source to the coefficients of h e^(−z). This is EXACTLY the R-variation direction in Section2. Therefore K0 annihilates its effect on x_j/u for every metric row j<=m<=b−3.

The normalized low Y equations involve G's last column times Y_(b−1), which is a fixed multiple of P_n. The epsilon term has no last-column contribution because T's final column is zero, and its low-column contribution has an extra u. Also P_(p−1) is a p-unit, so P_(a−1)=P_n/P_(p−1). It follows that x_j/u modulo p for j<=m is a fixed multiple of P_n, and every high x_j modulo p is a fixed multiple of P_n. Neither statement depends on h.

## 5. Normalized contraction and complete beta

For j<=m the zeroth metric weights are fixed p-units. For j>=m+1,

    Omega_j/u² = [m!(−1)^(j−m−1)(j−m−1)!]² mod p.

All these coefficients are fixed because j<=b<p. Section3 fixes the normalized low t corrections, and the high t coordinates modulo p are fixed by all-residue N,A transfer. Substitution into (9) and D=x^TOmega x proves (1). Thus a SINGLE k=2 reference determines delta,nu at every depth; finite higher-depth samples are not part of the theorem's justification.

Moreover HY=K^TOmega x is divisible by u, so the normalized selector zhat=D0 adj(N)^THY has every coefficient divisible by u. Its Rodrigues logarithmic polynomial shares that content; D has u² content. Dividing their exact endpoint difference by the monic t−1 preserves u content. The complete moment companion consequently obeys

    v_p(beta)>=k−v_p(D)−floor(log_p(2n+b−1)).               (13)

If nu is a unit, v_p(V)=2k. The factorial term has valuation2k−2v_p(n!)−v_p(D). Write a0=floor(n/p)>=2. Since u< p^a0 and2n+b−1<p^(a0+1), one has k<=a0−1 and floor(log_p(2n+b−1))<=a0, whereas2v_p(n!)−k>=a0+1. The factorial term is strictly deeper than (13). The actual rational sum takes that smaller valuation, proving (2) with its final evaluated gcd retained.

## 6. What this extension resolves

The n+1 normalized chart works at every fixed b>=4 and allowed m, using the same finite coefficient kernel. It resolves the endpoint-carry and backward-reset ambiguities uniformly, including the k=1 Frobenius correction and singular full N. It does not prove nu is a unit at a particular prime without its finite reference, nor does it eliminate other residue disks. No numerical extrapolation, growing-b valuation uniformity, signed-error theorem or e+pi conclusion is claimed.

## 7. Other forced negative disks: a concrete limit on a one-chart atlas

There is a further exact obstruction to a whole-family criterion that uses only the origin and n+1 charts. Let1<=h<=m+1, reduce n to-h modulo p, and suppose

    h<b−m−1.                                             (14)

Rows i=h,...,b−1 of N have N_ij=0 for j>i−h, with triangular diagonal(i−h)!. Thus their first b−h columns form a p-invertible triangle, while D0J vanishes in these rows. NY=Delta D0J forces Y to be supported in its last h coordinates. At n=-h,

    K=Z(I+Dpol)^h,
    Omega_j=(m+1−h)_j²,

so K Y has no support below row b−2h, while the metric has support only through m+1−h. Condition (14) is exactly b−2h>m+1−h. Therefore D=0 modulo p. For these same indices the first coordinate of KY is0 (b−2h>m+1−h>=0), and HY=0, so V=0 modulo p WITH kappa retained.

For example b5,m1 has forced disks n=-1 and-2; b5,m2 has only the forced n=-1 disk from this argument; b6,m2 has forced n=-1,-2. These are metric-kernel deductions, not scans. They show where a future multiple-chart normalization must begin. The common e^(−z) cancellation above resolves the h=1 disk; an h>1 disk has an h-dimensional lower-source/kernel problem and cannot be closed by simply reusing (1).
