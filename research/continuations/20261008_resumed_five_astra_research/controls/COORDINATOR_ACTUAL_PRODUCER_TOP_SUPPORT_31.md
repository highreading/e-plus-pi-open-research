> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Reused actual producer support, instantiated at precision31

Coordinator proof ledger,8 October2026. This is an elementary precision
extension of OLD A1turn9 Sections2--4 and A1turn14 Section2. It is not a new
producer or a new general support mechanism. It does not evaluate Delta_GG,
Delta_bG, the actual returned endpoint, or the diagonal return.

## Exact original data, recovered from the closed archive

Keep n=A+2, F_fac=(n-1)!=(A+1)!, v_3(A)=5 and n-1=4^j a ternary unit.
The moment recurrence is gamma_0=1,gamma_1=0 and
gamma_(r+1)=(4r+2)gamma_r+4gamma_(r-1). The original unit moment matrix is

    T_n(a,b)=binom(a+b,a)*gamma_(a+b), 0<=a,b<n.

The OLD integral inverse theorem is retained; no new inverse is inferred
from the finite350-coordinate receipt. Define the complete actual vectors

    h_vec=T_n^(-1)*(binom(n+a,a)*gamma_(n+a))_(a=0)^(n-1),
    u_a=F_fac*(-2)^a/a!, v=T_n^(-1)u,
    b_force=-n-66,
    t=3n*h_vec+(b_force+6)e_(n-1)
       +2*b_force/(n-1)*e_(n-2),
    eta=F_fac^2-u^T*v, chi=u^T*t,
    xi=chi/eta.

The archive's paid signed normalization gives xi integral (in fact a ternary
unit on this original family). It is essential to keep the ENTIRE t+xi*v.
All h_vec,v,t entries are integral over Z_3. The exact correction is

    Q_c=(y+1)*x^A*(beta+3y), beta=-71-A=1 (mod3),
    Q_act=3P_n=Q_c+3^7*R,
    [x^a](3^7 R)=-F_fac/a!*(t_a+xi*v_a), 0<=a<=A+1,
    R(-1)=-xi*F_fac^2/3^7, x=y-1.

The different historical notation3^6 R_prod has R_prod=3R. Do not confuse
its coefficient budget with the current3^7 convention.

## Paid general coefficient budget

For an integer K with0<=K<3^5 and a<=A-K-1, F_fac/a! contains
A,A-1,...,A-K. For1<=k<=K, v_3(A-k)=v_3(k), because v_3(A)=5 and k<3^5.
Consequently

    v_3(F_fac/a!) >= 5+v_3(K!).

The complete t_a+xi*v_a is integral, so after the ACTUAL3^7 division,

    v_3([x^a]R) >= v_3(K!)-2.

If v_3(K!)>=s+2, reduction modulo3^s is divisible by x^(A-K):

    R=x^(A-K)*B_s(x) (mod3^s), deg B_s<=K+1.

For sufficiently large original j, R(-1)=R(x=-2) vanishes modulo3^s;
the exact valuation n-8-s_3(n-1), already derived in A1turn14, pays this.
Since -2 is a unit, B_s(-2)=0. Monic division by x+2 therefore yields

    R=(y+1)*x^(A-K)*q_s(x) (mod3^s), deg q_s<=K.

No unit assumption on individual t_a or v_a is made. No nonunit division
is hidden in this factorization.

## Precision31 and the complete reciprocal

The OLD precision24 instance K=54 is retained. For the NEW required instance
s=31, choose K=72<243. Legendre's elementary formula gives

    v_3(72!)=24+8+2=34 >= 33.

Thus

    R=(y+1)*x^(A-72)*q_31(x) (mod3^31), deg q_31<=72.

This is a valid coefficient support bound at the required precision; it
does not provide the values of q_31 or its action on corrected columns.
Because beta=1 (mod3), the ENTIRE reciprocal is

    r_31(y)=beta^(-1)*sum_(k=0)^30(-3y/beta)^k,
    (beta+3y)r_31=1 (mod3^31), deg r_31<=30.

For an ACTUAL trial F*=x^D*psi, the exact candidate multiplier is

    L=x^(D-72)*q_31*r_31*psi,
    Q_c*L=R*F* (mod3^31), deg L<=deg F*+30.

This use additionally requires D>=72 and the actual finite degree gap>=30.
It says nothing about replacing F by F*: that replacement must separately
pay its actual residual, inverse loss and BOTH linear pairing errors at
precision31. If deg L>m, the omitted physical coefficient and returned tail
must be evaluated. Likewise, a pole-grid separation valid at precision20
cannot be promoted to31 without checking every new LOWER/HIGH extraction.

## Scope for the next actual-radical task

The supported multiplier supplies a concrete bounded polynomial degree72
plus the full degree30 reciprocal. It is available for A4's complete
producer-on-radical proof. It does not establish either normalized producer
residue is zero, does not identify the actual endpoint with core evaluation,
and does not pay the1/9 diagonal return. Those are the actual next obligations.
