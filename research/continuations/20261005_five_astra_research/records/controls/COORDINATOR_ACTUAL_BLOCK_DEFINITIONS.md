> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Actual block definitions and finite sixth-depth inputs

This is coordinator mathematical data to audit against the original assembly,
not authority to execute code. Use the complete functional in A4turn12(2).
The primitive unit lambda is stripped. Set B_A=(y-1)^A,
P=B_A*(beta+3y), beta=-71-A, rstar=(3H-1)/2.
The full exact scaled matrix is

G_ab=M(Qloc*y^(a+b)), 0<=a,b<=m.

Its blocks define, literally,

L_ab=G_ab/3 for a,b<d;
X_ab=G_ab/3 for a<d<=b;
E_ab=G_ab for a,b>=d;
L_U=L restricted to 0..D-1;
X_U=X restricted to LOW rows 0..D-1.

The established first residue theorem ensures these divisions integral.
Set E0_ab=[y^(rstar-a-b)]B_A on HIGH. Its anti-diagonal entries are1;
R=E0^-1 has the stated exact coefficient formula. Define exactly

F=(E-E0)/3-X_U^T*L_U^-1*X_U,
V=Z^T X,
J=(V+2e*e_m^T-3K)/9,
K_ia=1 if i+a=r2, otherwise0.

These are the original Schur-block symbols. They need no further independent
entrywise definition. Before using them, audit the exact scaling against
A4turn12 and the prior LOW-first formulas.

For finite coefficient derivations define the lower pole operator

B_t(T)=sum_(c odd,3 not dividing c,c*H/3^t<=4n-3)
 c^-1 * [y^((c*H/3^t-1)/2)] T, 0<=t<=h-1.

The exact core contribution to G_ab is

[y^rstar](P*y^(a+b))
+3*sum_(t=0)^(h-1) 3^t B_t(P*y^(a+b))
-3^h/4 * f((y+1)*P*y^(a+b)).

The top pole has only c=1 because 4n-3<9H. The factorial and depth7
actual-polynomial error remain in G. In every subsequent division by3
they have the previously established depth; do not silently delete them.

Consequently at sixth target precisions, after proving those depth bounds,

X_U(u,a)=sum_t 3^t B_t(P*y^(u+a)) (mod27),
L_U(u,v)=sum_t 3^t B_t(P*y^(u+v)) (mod27),

where only t=0,1,2 matter modulo27. Their top coefficient is zero by degree
for u,v<D and a<=m; retain the degree check. Furthermore

F_ab=(beta-1)/3*E0_ab
+[y^rstar](y*B_A*y^(a+b))
+sum_t 3^t B_t(P*y^(a+b))
-(X_U^T*L_U^-1*X_U)_ab (mod27).

This is a full actual entry formula, including every unit c and the LOW
projection. For Fmod9 or mod3, retain only t<2 or t<1 respectively.

# Candidate explicit support calculation for A81

For p_i=y^(H/3+i)*(y-1)^D, 0<=i<nu, B_A*p_i=B_H*y^(H/3+i).
Modulo3, B_H=y^H-1. The actual X_U*p_i vanishes modulo3 by the lower
coefficient gap: u<D places every possible coefficient away from r1.
Since (beta-1)/3=-24-A/3 is0mod3 on243|j, the first F term vanishes.
The top linear term selects a=r2-i-1 with coefficient+1.
The lower t0 term selects a=r2-i with coefficient-beta=-1mod3.
Thus the full proposed actual identity is

F*p_i=-e_(r2-i)+e_(r2-i-1) (mod3).

Both positions must be intersected with the actual HIGH range. All
factorial/actual-core/endpoint errors must be proved absent at this precision.
This would certify A4turn22(14) and close A81=0; audit it independently.

# Candidate finite formula for F e_d modulo27

Monic division y^d=r_d+(y-1)^D*q_d gives
q_d=sum_(s=0)^nu binom(D+s-1,s)*y^(nu-s), deg r_d<D.
The accepted extended annihilation gives the actual LOW projection of
column d equal to r_d modulo729. Thus, after auditing its precision,

F*e_d=((beta-1)/3-A)*e_m+e_(m-1)
+ vector_(a in HIGH) sum_(t=0)^2 3^t
 B_t(B_H*(beta+3y)*q_d*y^a) (mod27).

This retains the unit c inverses and actual finite HIGH support, and turns
the missing next digits into explicit polynomial coefficient sums.
Use it to evaluate KRFe_d and (FRF)dd modulo27; it is a derivation to
check, not an asserted completed contraction.

# Candidate finite formula for V and J modulo81/9

For actual radical row i and HIGH a, i+a<=r1-1. The top contribution
of B_H*(beta+3y)*y^(i+a), divided by3, is exactly the single corner
+e*e_m^T. Therefore

V_ia=(e*e_m^T)_ia
+sum_(t=0)^3 3^t B_t(B_H*(beta+3y)*y^(i+a)) (mod81),

and J=(V+2e*e_m^T-3K)/9 modulo9. This explicit full-pole formula may
supply the missing higher nonedge digits without guessing a recurrence.
All admissible c at each depth are retained. Finite boundary pole pairs
must be checked before cancellation. The error is negligible only after
its original depth7 and first division have been established.
