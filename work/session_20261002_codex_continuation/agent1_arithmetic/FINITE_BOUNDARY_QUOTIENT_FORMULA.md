> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Eliminating the p² reference from the boundary constants

New author mathematics, 2026-10-02, target L7. This gives an explicit finite formula for the constants in ALL_STRUCTURAL_BOUNDARY_CHARTS.md. It is not an independent review. Use b,m,p,h in that theorem, d=b−h,M=m+1−h. All objects in this note lie in F_p. No full N inverse, high-row derivative or actual n=p²−h computation is required.

## 1. A coefficient window of length p+d

Let alpha_s=[z^s]q0(z)^(-h),0<=s<=p+d−1. These coefficients are computed by formal inversion of the polynomial q0^h, whose constant coefficient is1. This requires no division by s or by p. For s<d define

    adot_s=[z^s]q0(z)^(-h) log q0(z).

Only log coefficients of degrees<d<p are needed, so their denominators are p-units.

Define f_l,v(u)=(u+l)_v and take its value f0_l,v and first derivative f1_l,v at u=0, for0<=v<=p+l. These are integer-polynomial derivatives reduced modulo p. They can be generated without division by the two-variable recurrence

    f0_(v+1)=(l−v) f0_v,
    f1_(v+1)=(l−v) f1_v+f0_v,
    f0_0=1,f1_0=0.

For0<=l<d,0<=j<b, put

    T_lj=sum_(s=0)^max(l−j) alpha_s f0_l,j+s,
    G_lj=sum_(s=0)^(p+l−j) alpha_s f1_l,j+s
                +sum_(s=0)^max(l−j) adot_s f0_l,j+s.       (1)

An empty upper range contributes0. This G is the fixed lower-row derivative from the all-depth chart. The one-u window terminates at v=p+l because v=p+l+1 contains the second zero factor u−p. Short a_s derivatives enter only where f0 is nonzero.

Let d_j=Dcal_j modulo p for0<=j<p. Define g_0=2d_(p−1), g_j=jg_(j−1)+2d_(j−1). In lower row l put o=l−h−s and

    F_l=sum_(s=0)^(p+l) alpha_s f1_l,s d_(o mod p)
        +sum_(s=0)^l adot_s f0_l,s d_(o mod p)
        +sum_(s=0)^max(l−h) alpha_s f0_l,s g_(l−h−s).       (2)

The first two sums include the actual backward first residues d_(p−j). Their unspecified higher digits belong to the killed kernel. The final sum is the derivative of the positive-index Dcal terms propagated from Dcal_(2u)=1+2uR1. Thus F is exactly the fixed derivative in the all-depth chart, with the backward symbols held constant. No scalar interpolation assumption at a negative index is made.

## 2. Only the seed and two triangular solves remain

Take N*,A*,J* at the seed r=p−h, all modulo p. Let Delta=det N*, P=J*_0, and use the exact polynomial adjugate to define

    Ybar=adj(N*)D0*J*/P,
    Bbar=adj(N*)A*.

Ybar's first d coordinates are zero. Its final h coordinates retain the fixed canonical cofactor response, even when Delta=0. The matrix T is precisely the lower d rows of N*. Let T0 be its first d columns.

Set

    S_l=(-1)^(h−1)(h−1)!l! J*_(h+l)/P.

This is the normalized endpoint source with the carry set to zero. The carried contribution can be discarded ONLY because the previously proved kernel annihilates it in the contraction. Solve the unit triangular systems

    y=T0^(-1)(Delta S−G Ybar),
    bcor=T0^(-1)(Delta F−G Bbar).              (3)

Set K0=Z(I+Dpol)^h and K1=-K0 log(I+Dpol), where the finite matrix logarithm has degrees1,...,b−1 with p-unit denominators. Define

    xbar=K0Ybar, tbar=K0Bbar,
    X_j=(K0[:,0:d] y+K1Ybar)_j,0<=j<=M,
    Tcor_j=(K0[:,0:d] bcor+K1Bbar)_j,0<=j<=M.              (4)

X_j is x_j/(uP_n) modulo p. Tcor_0 is (t0+Delta)/u modulo p, and Tcor_j is t_j/u for j>=1. In taking the derivative for (4), Delta's derivative and the backward symbols' derivatives can be set to zero: their low reconstructed contributions are respectively the exact correction cancellation and the kernel e^(−z)Pol_(h−1). Unknown high Y/B derivative coordinates are also invisible because K0's low metric rows vanish in their last h columns. These facts explain why no high-row derivative appears in (3),(4).

## 3. Explicit delta and nu

Put w_j=(M)_j² for0<=j<=M, and wtilde_j=[M!(j−M−1)!]² for M<j<=b. Then

    delta=sum_(j=0)^M w_j X_j²
              +sum_(j=M+1)^b wtilde_j xbar_j²,
    nu=sum_(j=0)^M w_j X_j Tcor_j
              +sum_(j=M+1)^b wtilde_j xbar_j tbar_j.       (5)

This nu retains kappa through Tcor_0. Formulas (1)–(5) reproduce the normalized constants of the all-depth theorem. They permit exact finite inputs using a seed n<p and a coefficient window p+d, instead of a full reference n=p²−h. The mathematical bound on actual q still uses that theorem's beta comparison and rational-sum valuation; (5) is not raw content identified with q.

The arithmetic cost in the prime parameter is a linear coefficient-window length for fixed b,h, together with finite-dimensional adjugate/triangular work. This is not an algorithmic complexity claim uniform in b. The matrix polynomial may be constructed exactly before reduction, and coefficient inversions divide only by1 or established p-units.

## 4. Own-reference exact verification and limits

finite_boundary_chart.py implements (1)–(5), saving FINITE_BOUNDARY_CHART_RECEIPT.json with T,G,F, both triangular solves, low/high contractions and final constants. It agrees EXACTLY with the eight direct reference states authored earlier in this stage:

- b4,m1,h1 at p5,7,43,67,71;
- b5,m1,h2 at p7,13;
- b7,m2,h3 at p13.

The raw receipt includes the singular full N at b4,p7 and delta=0 at b4,p5. These exact finite agreements validate the author implementation against the larger references; the derivation above and the all-depth kernel theorem supply the infinite statement. No independent review, broader prime atlas, prime supply or construction exclusion is inferred from the agreements.
