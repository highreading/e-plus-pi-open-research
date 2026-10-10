> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# An all-start algebraic nonvanishing block for the actual half-step certificate

2026-10-02. Original author theorem. This strengthens the completed half-step saddle block and requires no moving-saddle input. It does not prove the still-open constant-shift conjecture. The representation search was recorded before pursuit in `HALF_STEP_CHRISTOFFEL_TARGET.md`; the exact state formulas are proved in `HALF_STEP_THREE_STATE_OUTPUT.md`. The proof below uses rational matrix residues and exact endpoint orders, rather than transferring a positivity assertion from a different Christoffel family. Its classical overlap is finite-degree rational observability; the present work is the exact actual-kernel application and its complete arithmetic consequence.

Let n=4k≥4, r=n/2, d=n+1, z(w)=1−2w², a=(1+i)/2, z_+=1−i, z_−=1+i. Retain the proved ACTUAL fixed polynomial

    P(w)=P̆_n(w)=−2^(−n−1)w V(w)^r R_n(w),
    deg P=3n+1=6r+1,
    ord_a P=ord_(bar a)P=r.                       (1)

The exact order follows from the proved R_n(a),R_n(bar a)≠0. Its actual output is

    W̆(n,h)=2^(n+1)Y_h,
    Y_h=i∫_(bar a)^a P(w)z(w)^h dw.               (2)

For the rational state X_h=(D_h,A_h,B_h)^T defined in the preceding note, write Y_h=R(h)X_h and the pulled-back three-output matrix O(h) there. Its entries are rational functions, without U divisions, and have no pole on h≥0.

## 1. Uniform pole and numerator-degree theorem

Define

    D_n(h)=∏_(k=1)^(3r+3)(h+k)
               ∏_(k=0)^(3r+1)(2h+2k+3).          (3)

Then

    p_n(h)=D_n(h) det O(h)

is a nonzero rational-coefficient polynomial of degree exactly 2n+2. Consequently det O can have at most 2n+2 distinct nonnegative real zeros. The overclearing polynomial p_n is used here; no uniform claim that the REDUCED numerator has degree 2n is needed.

### A. Every matrix pole has a rank-one residue

Write S_j(h)=M(h+j−1)…M(h), with S_0=I, for the regular state transition

    M(t)=[ (2t+2)/(2t+3)   0   1/(2t+3) ]
         [       0          1      −1     ]
         [       0          1       1     ].

A pulled-back output at h+i, i=0,1,2, is a sum of even-monomial rows e_1^T S_(i+j) and odd-monomial rows e_3^T S_(i+j+1)/(h+i+j+1). The coefficients are the fixed binomial expansion coefficients of P and contain no h denominator.

The only possible half-integer poles are h=−k−3/2 for 0≤k≤3r+1. At any such pole, exactly one factor in a given S_j is singular, namely M(h+k), if j≥k+1. Its residue is rank one:

    Res M(h+k)=(1/2)e_1(-1,0,1).

All products S_j with this pole have the SAME residue row direction

    (-1,0,1)S_k(h_0)

on their right. The left factors and output coefficients only change its scalar multiplier. The bottom two rows of every S_j are constant endpoint rotations and have no half-integer poles. Thus the entire O matrix has a rank-one residue at each possible half-integer pole.

For integer poles, write P_odd(w)=w H(z(w)), where H has degree at most 3r. In the constant complex endpoint coordinates Z_+,Z_−, the odd output at h+i has the row

    −(i/4) Σ_(j=0)^(3r) H_j
        [ z_+^(i+j+1)Z_+−z_−^(i+j+1)Z_− ]/(h+i+j+1).

At h=−k, all singular terms have i+j+1=k, so the residue endpoint row is a scalar multiple of the SAME row (z_+^k,−z_−^k). There is no D-coordinate residue and the even-monomial rows have no integer poles. Hence O again has a rank-one residue. The possible integer poles satisfy 1≤k≤3r+3.

All entry poles are simple: the linear factors in a given S_j are distinct, and the odd primitive denominators occur only at integers, disjoint from half-integer transition denominators. If a matrix has expansion C/(h−h_0)+A(h), with A analytic and rank C≤1, determinant multilinearity makes all terms of pole order ≥2 vanish. Therefore det O has at most a simple pole at every listed location and no other finite pole. Formula (3) removes them all. A rational function without finite poles is a polynomial.

### B. Its leading term at infinity is strictly nonzero

First the even part of the actual P has an exact nonzero initial term

    P_even(w)=c_n w²+O(w⁴),
    c_n=[n 2^(2−r)/r!]∏_(j=0)^(r−1)(n+1+2j)>0.   (4)

To derive (4), use the proved adjoint kernel expression

    P=−4w(1−t)^d κ_n(t), t=1−2w²,
    κ_n=Σ_(ell=0)^r 2^ell a_(n−2ell)/ell!
                                    D_t^ell[t^ell h_full(t)],
    h_full=V(w)^n/(4w^(n+2)), D_t=−(4w)^(-1)D_w.

The first odd Laurent coefficient of h_full at w=0 is

    −n 2^(−n−1)w^(−n−1).

Only the top ell=r term can produce the w² coefficient of P. Each derivative multiplies this leading odd Laurent term by (n+1+2j)/4, a positive factor. Multiplication by −4w(2w²)^d gives exactly (4). Every lower ell yields a higher power; even Laurent terms yield odd powers and cannot affect w².

Choose the positive homogeneous solution

    C_h=∫_(-1/sqrt2)^(1/sqrt2) z(w)^h dw
       =(1/sqrt2)B(1/2,h+1),
    C_(h+1)/C_h=(2h+2)/(2h+3).

For the homogeneous state (C_h,0,0), the output is F(h)C_h, with

    F(h)=∫_(-1/sqrt2)^(1/sqrt2)P_even(w)z(w)^h dw / C_h.

This equality also follows directly from the even-monomial moment formulas; the odd output vanishes when the endpoint state is zero. Fixed-n real Laplace estimation at w=0, or the exact beta moments, gives

    F(h)=c_n/(4h)(1+O_n(1/h)).                   (5)

In particular the slow output mode has a nonzero leading coefficient.

Two further fundamental states use the base moments i∫_0^a z^h dw and −i∫_0^(bar a)z^h dw, and endpoint states (z_+^h,i z_+^h), (z_−^h,−i z_−^h), respectively. Their forward transition is exactly M(h), because a z_+=bar a z_−=1. The determinant of the three state columns is

    −2i C_h(z_+z_−)^h≠0.                       (6)

Their actual R(h)-outputs differ from i∫_0^a Pz^h dw and its conjugate only by the lower-end odd-primitive constants. Those constants are rational functions of h of size O_n(1/h), and therefore are exponentially smaller than the endpoint modes below.

On w=a(1−x), z(w)=z_++2ix−ix², and

    z(w)/z_+=1−z_+ x+O(x²).

Also |z(as)|=sqrt(1+s⁴) is strictly increasing for 0≤s≤1. Thus the endpoint a is uniquely dominant on the straight radial segment 0→a. Using the exact endpoint order r in (1), the elementary endpoint Laplace expansion gives

    i∫_0^a P(w)z(w)^h dw
       =γ_n z_+^h h^(−r−1)(1+O_n(1/h)),
    γ_n=i a P^(r)(a)(−a)^r / z_+^(r+1)≠0.         (7)

This expansion is for fixed n and h→∞ only; no uniform large-n claim is needed. The conjugate output has coefficient bar γ_n. The same lower-end rational correction does not change (7).

Apply O(h) to these three fundamental columns. By (5)–(7), its three-output determinant has leading Vandermonde factor

    det[1,z_+^j,z_−^j]_(j=0)^2
       =(z_+−1)(z_−−1)(z_−−z_+)=2i.

Dividing by (6) proves the exact nonzero asymptotic

    det O(h)=−(c_n/4)|γ_n|² h^(−n−3)
                                         (1+O_n(1/h)).   (8)

Since D_n has degree 3n+5 and positive leading coefficient 2^(3r+2), equations (3),(8) show that p_n has degree exactly 2n+2 and nonzero leading coefficient. This completes the uniform algebraic theorem. The fixed-n asymptotic establishes a polynomial coefficient for EVERY n, without choosing an n-dependent start or invoking a large-n phase approximation.

## 2. Actual all-start block nonvanishing

For every integer H≥0, the 2n+3 distinct starts H,…,H+2n+2 cannot all be roots of the nonzero degree-(2n+2) polynomial p_n. At some such h the output matrix O(h) is invertible. The actual state X_h is nonzero because its two endpoint coordinates cannot both vanish. Therefore one of its three actual certificate outputs is nonzero. We have proved

    for EVERY n=4k≥4 and H≥0,
    ∃ell∈[H,H+2n+4]∩Z: W̆(n,ell)≠0.             (9)

The corresponding direct center support ends at ell+d≤H+3n+5. This handles forcing zeros and exact zero errors without division. Selection by the least nonzero rational certificate defines a finite rule independent of π.

## 3. Complete arithmetic consequence in the requested regime

For H=2ρ n log n+O(n), retain all actual support nodes H,…,H+3n+5 and define

    L*=7n+2H+10,
    N*=8n+2H+10,
    A*=max_(0≤j≤3n+5)|U_(H+j)|,
    Λ*=14n+4H+20.

The largest certificate primitive degree 3n+2ell+2 is L*. The largest actual center degree 2n+2s is N*, and its full exponential parameter 2n+4s is Λ*. The exact half-step lattice gives

    |W̆(n,ell)|≥2^(r+1)/O_(L*),
    ∃s in the selected support with U_s≠0:
    |β_s−π|≥B*=1/[2^r O_(L*) (A*)²].            (10)

The full exponential and actual beta denominator bounds are

    0<|e−α_s|<E*=3(Λ*)^n exp(Λ*/(n+1)) /
                                [(n+1)(n!)²2^r],
    den(β_s)≤O_(N*) A*/2.                        (11)

For the ACTUAL fully reduced denominator q_s of c_s=α_s+β_s, the saved e irrationality-measure input gives

    q_s≥2(C_ε/E*)^(1/(2+ε))/(O_(N*) A*).         (12)

When E*≤B*/2, the same-node complete error and primitive form satisfy

    |c_s−(e+π)|≥B*/2,
    q_s|c_s−(e+π)|≥(C_ε/E*)^(1/(2+ε)) /
                    [2^r O_(N*)O_(L*)(A*)³].     (13)

The forcing Cauchy height remains log A*≤r log log n+O_ρ(n). Thus log E*≤−n log n+n log log n+O_ρ(n). The classically sourced odd-lcm PNT gives log O_(L*),log O_(N*)=4ρ n log n+o_ρ(n log n), and consequently

    liminf log B*/(n log n)≥−4ρ,
    liminf log q_s/(n log n)≥1/2−4ρ,
    liminf log(q_s|c_s−(e+π)|)/(n log n)≥1/2−8ρ.  (14)

The full exponential domination holds when 4ρ<1; actual primitive divergence holds for 0<ρ<1/16. The leading threshold is unchanged, while the support and finite lattice constants improve sharply. An exact direct witness is selected by the saved rational π-enclosure rule, maximizing |β_s−p| with |p−π|≤B*/8; it retains |β_s−π|≥3B*/4 and (13) once E*≤B*/4.

All denominator claims concern the same actual reduced center. No exact even-h dyadic formula is imposed at odd h. No saddle assumption is used for (9). The general constant-shift determinant positivity remains open, and no irrationality conclusion for e+π is claimed.
