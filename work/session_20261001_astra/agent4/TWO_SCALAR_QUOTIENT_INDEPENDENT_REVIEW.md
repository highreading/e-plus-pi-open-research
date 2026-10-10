> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent two-scalar quotient review

Reviewer: Agent 4. Scope: the resumed two-scalar assignment, with actual approximation controls exactly n=4,6,8,10. This review preserves the completed family, arithmetic/content, and additional recurrence reviews.

Verdict: PASS for the exact quotient algebra, the conditional endpoint and complete companion bounds, and the endpoint bridge in Agent 3 Sections 6–7, subject to the domains and rank conventions below. PASS for the abstract conditioning limitation. The factorial-array transfer passes on its actual domain; it is not a closed positivity recurrence. No unbounded growing-degree theorem is established.

The independent program check_two_scalar_quotient_independent.py was saved, inspected, and executed successfully: exit code 0, 907 checks. Its complete evidence and stdout were read back. It imports no author program, reconstructs monic polynomials by recurrence, and uses direct rational moments, finite projection/kernel sums, determinants, and the saved full polynomial triples. All 33 protected files, including reviewed sources and completed Agent 4 artifacts, retained their hashes. No author certificate-writing entry point was executed.

## 1. Sources and separate verdicts

Reviewed inputs are agent2/TWO_SCALAR_DETERMINANT_QUOTIENT.md, TWO_SCALAR_DETERMINANT_QUOTIENT_REPORT.md, REPORT.md, check_two_scalar_quotient.py, two_scalar_quotient_evidence.json, and growing_regime_certificates.json; agent3/BERNSTEIN_DIFFERENCE_CONTINUATION.md only for the endpoint bridge in Sections 6–7; and PRIMITIVE_CONDITIONING_LIMITATION.md. Paths are relative to work/session_20261001_astra/. Input hashes are in the independent evidence.

| Component | Verdict |
|---|---|
| Rational z0,z1; determinant signs and monic scales | PASS |
| Rank conventions, zero coordinates, opposite-sign endpoint lemma | PASS with explicit nonzero-pair and representative qualifications |
| Projective separation Delta | PASS; no quantitative separation theorem supplied |
| Rational e/pi companions and fully reduced q | PASS |
| Primitive alternating form, decomposability, Plucker identities | PASS on full high-row rank |
| Complete companion bound with C | PASS; C cannot be omitted |
| Factorial array and shifted minors | PASS in the domains in Section 7 |
| Frozen controls n=4,6,8,10 | Independent exact PASS |
| Agent 3 endpoint bridge, Sections 6–7 | PASS only for the bridge |
| Primitive conditioning example | PASS as an abstract example, not actual HP data |
| Detailed revised reference estimate | Outside this verdict; Agent 1's separate audit |
| Unbounded opposite-sign law, suitable q/C control, full-error nonvanishing | Unproved |

## 2. Reference facts needed here

Write L(f)=integral from -1 to 1 of f((1+iu)/2) du. The monic polynomials satisfy p0=1, p1=t-1/2 and

p_(k+1)=(t-1/2)p_k+beta_k p_(k-1), beta_k=k^2/[4(4k^2-1)].

Their Legendre realization is p_k((1+iu)/2)=i^k P_k(u)/binom(2k,k). Orthogonality gives h_k=L(p_k^2)=2(-1)^k/[(2k+1)binom(2k,k)^2]. Put A_k=p_k(1) and v_k=L(p_k/(1-t)).

The endpoint recurrence A_(k+1)=A_k/2+beta_k A_(k-1), starting at 1,1/2, gives A_k>0 and 1/2<=A_(k+1)/A_k<=2/3 by induction, since beta_k<=1/12. It also gives A_k>=2^(-k). The coefficient norm satisfies M_(k+1)<=3M_k/2+beta_k M_(k-1); induction with M0=1,M1=3/2 proves M_k=||p_k||_1<=2^k.

Orthogonality applied to p_k(t)(p_k(t)-A_k)/(t-1) proves

A_k v_k=L(p_k^2/(1-t))=2(-1)^k/binom(2k,k)^2 * integral[-1,1] P_k(u)^2/(1+u^2) du.

Thus v_k is nonzero with sign (-1)^k. Moreover v_k A_k/h_k lies between 1 and 2, using integral P_k^2=2/(2k+1). Applying L to the recurrence divided by 1-t gives v_(k+1)=v_k/2+beta_k v_(k-1) for k>=1. Alternating signs imply, with c_k=|v_(k+1)/v_k|,

c_k=beta_(k+1)/(1/2+c_(k+1))<2 beta_(k+1)<=1/6.

For this review n>=1, so the displayed bound is valid. These arguments establish the sign and ratio facts independently of the revised contour estimates.

Christoffel–Darboux follows by telescoping the monic recurrence with h_k/h_(k-1)=-beta_k. For P=p_n, U=p_(n+1), A0=A_n, A1=A_(n+1), h=h_n, the finite kernel and projection remainder satisfy

V=(A1 P-A0 U)/[h(1-t)],
W=(v_n U-v_(n+1)P)/[h(1-t)].

Here W=1/(1-t)-sum_(k=0)^n v_k p_k/h_k. To derive the second identity, apply L in the kernel variable to the CD identity and use L(p_k)=0 for k>=1. Multiplying by 1-t and evaluating at 1 gives A1 v_n-A0 v_(n+1)=h. The independent controls additionally reconstructed both finite sums and verified these polynomial identities directly.

The main bound below retains epsilon_n=|v_n|/A_n exactly. It needs no detailed disk, Gaussian, or revised contour majorant. Any later use of log epsilon_n=-2log(1+sqrt(2)) n+O(1) is a separately identified reference-rate dependency, not a conclusion of this review of Agent 1's pending detailed estimate.

## 3. Determinant ledger and degeneracies

Assume 1<=b<=n. Set ell_j(t^r)=1/(n+r+1-j)! for 0<=j<=b. Every factorial argument is at least n+1-b>=1. Let the high matrix have rows ell(p_(n+l)), l=1,...,b-1, and define B(x,y)=det[high;x;y]. Write evec=(1,...,1), a=ell(U/(1-t)), c=ell(P/(1-t)).

If E_m=sum_(r=0)^m 1/r! and tau_Q,j=sum_k [t^k]Q E_(n+k-j), summing the complete factorial tail gives

ell_j(Q/(1-t))=e Q(1)-tau_Q,j.

All partial-sum indices are nonnegative because n-j>=0. Thus a=e A1 evec-tau_U and c=e A0 evec-tau_P. Consequently

z0=B(evec,a)=-B(evec,tau_U), z1=B(evec,c)=-B(evec,tau_P)

are rational, although a,c themselves need not be rational.

Writing v=ell(V), w=ell(W), the CD formulas give

v=(-A0 a+A1 c)/h, w=(v_n a-v_(n+1)c)/h.

The determinant of this change of two rows is (A0 v_(n+1)-A1 v_n)/h^2=-1/h. Hence, with D_V=B(evec,v), D_W=B(evec,w), T=B(v,w),

D_V=(A1 z1-A0 z0)/h,
D_W=(v_n z0-v_(n+1)z1)/h,
T=-B(a,c)/h.

For the cofactor normalization Bcoeff dot x=det[high;evec+v;x], summing its coefficients gives Y=Bcoeff dot evec=-D_V. The underlying endpoint-matched HP reconstruction gives R(1)=D_W+T. At the four controls both relations were checked against the saved primitive full triples and the original formal HP residual through the required order.

These polynomial identities remain valid when the selected cofactor vector is zero. Quotients require D_V!=0. Full high-row rank is needed before dividing row contents or maximal-minor content, but full high-row rank alone does not establish augmented rank or endpoint nonvanishing. Conversely D_V!=0 supplies full high-row rank and augmented rank b. Deficient high-row rank makes this chosen maximal-cofactor representative zero; it does not rule out other solutions of the original underdetermined system. An augmented rank-b representative can also have Y=0, in which case the endpoint quotient is unavailable. Full-remainder nonvanishing is an additional condition even when Y!=0.

For b=1 the high block is empty, its empty minor is 1, and the same determinant formulas apply. No division by a zero content is allowed.

## 4. Opposite signs and projective separation

Put alpha=v_(n+1)/v_n<0, c_ref=-alpha<1/6, b_ref=A1/A0>=1/2 and epsilon=|v_n|/A0. If z0 z1<=0 and (z0,z1)!=(0,0),

|A1 z1-A0 z0|=A0|z0|+A1|z1|>0.

The numerator satisfies |v_n z0-v_(n+1)z1|<=|v_n|(|z0|+c_ref|z1|), so |D_W/D_V|<=epsilon. The coordinate cases are explicit: z1=0 gives D_W/D_V=-v_n/A0; z0=0 gives -v_(n+1)/A1, whose absolute value is epsilon c_ref/b_ref<epsilon/3. Both zero give D_V=0.

For a nonzero pair define

Delta=|A1 z1-A0 z0|/(A0|z0|+A1|z1|).

Then 0<=Delta<=1, Delta>0 iff D_V!=0, and opposite signs give Delta=1. On Delta>0 the same triangle inequality gives |D_W/D_V|<=epsilon/Delta. If z0!=0 and eta=z1/z0,

D_W/D_V=-(v_n/A0)(1-alpha eta)/(1-b_ref eta).

The pole is eta=A0/A1. Avoiding exact equality with the pole does not bound Delta away from zero. No infinite-index sign or separation theorem follows from the four controls.

## 5. Primitive scales and the actual rational companions

Clear high row l by (2n+2l)!, divide its positive integer content c_l, and let R0 denote the resulting primitive rows. The integrality of these cleared rows is the previously completed arithmetic review's Rodrigues identity; it was also checked directly at all four controls. Define m_ij=(-1)^(i+j+1)det(R0 omitting columns i,j), mu=gcd|m_ij|, and N_ij=m_ij/mu for i<j, extending antisymmetrically. On full high-row rank mu>0. Laplace expansion in the last two rows proves

B(x,y)=gamma_high x^T N y,
gamma_high=(product_l c_l)mu/product_l(2n+2l)! >0.

This scale is rational, not generally integer. It is distinct from the endpoint gcd and from the arithmetic review's residual minor content.

Write Bbar(x,y)=x^TNy, Z0=-Bbar(evec,tau_U), Z1=-Bbar(evec,tau_P), K_tail=Bbar(tau_U,tau_P), and d_endpoint=A1 Z1-A0 Z0. These contractions are rational, not asserted integral. Then z_i=gamma_high Z_i, D_V=gamma_high d_endpoint/h, and expansion gives

Bbar(a,c)=e d_endpoint+K_tail.

Consequently T/D_V=r_e-e with r_e=-K_tail/d_endpoint rational. Define w_k=L((p_k-A_k)/(t-1)), which is rational by polynomial integration. Since L(1/(1-t))=pi, v_k=A_k pi-w_k. Therefore

D_W/D_V=r_pi-pi,
r_pi=(w_(n+1)Z1-w_n Z0)/d_endpoint.

Using Y=-D_V and R=X+Y(e+pi),

X/Y=-r_pi-r_e,
R(1)/Y=e+pi-r_pi-r_e.

If X/Y=p_int/q in lowest terms with q>0, then

q=den(-r_pi-r_e), p_int+q(e+pi)=q R(1)/Y.

This is reduction after summing the two rational companions. Separate companion denominators or coefficient clearers do not replace q. A zero rational numerator gives q=1. Individual irrationality of e and pi makes each separate error nonzero; it does not prevent their sum from vanishing.

## 6. Decomposability, Plucker, and the complete bound

The alternating form Bbar vanishes when either argument belongs to the high-row span. On full high-row rank it descends to a nonzero alternating form on a two-dimensional quotient. Thus N has rank two and is decomposable. Its Plucker relation is an identity on this quotient and does not require either Z coordinate to be nonzero.

For coordinate vector f_j put kappa_j=Bbar(evec,f_j)=sum_i N_ij, S_j=sum_k|N_jk|. The signs matter: kappa_j is the column sum, the negative of the row sum. The rank-two identity gives

kappa_j Bbar(a,c)=Z0 Bbar(f_j,c)-Z1 Bbar(f_j,a),
kappa_j K_tail=Z1 Bbar(f_j,tau_U)-Z0 Bbar(f_j,tau_P).

If d_endpoint!=0 then some kappa_j!=0: otherwise Bbar(evec,x)=0 for every x, forcing Z0=Z1=0. Hence

C=C_(n,b)=min_(kappa_j!=0) S_j/|kappa_j|

is defined, rational, and at least 1. The undivided identities also hold at kappa_j=0; the divided bound uses only eligible coordinates.

Let Nstart=n+1-b>=1. For any polynomial Q,

|ell_j(Q/(1-t))|<=e ||Q||_1/Nstart!,

because each complete factorial tail starts at an index at least Nstart and sum_(r>=0)1/(Nstart+r)!<=e/Nstart!. Bounding the two coordinate contractions in the first Plucker identity gives

|Bbar(a,c)|<=C e (|Z0| ||P||_1+|Z1| ||U||_1)/Nstart!.

Since |d_endpoint|=Delta(A0|Z0|+A1|Z1|),

|T/D_V|<=C e max(||P||_1/A0,||U||_1/A1)/(Delta Nstart!)
<=C e 4^(n+1)/(Delta (n+1-b)!).

The complete evaluated bound is therefore

|R(1)/Y| <= [epsilon_n+C e 4^(n+1)/(n+1-b)!]/Delta.

Neither C nor Delta can be dropped without additional information. For b=floor(n/2), the logarithm of e4^(n+1)/(n+1-b)! is -n log n/2+O(n); this observation alone controls neither C nor q.

A sufficient same-index condition for a shrinking sequence of nonzero integer linear forms is

(q/Delta)[epsilon_n+C e4^(n+1)/(n+1-b)!] -> 0,

along an unbounded sequence with D_V!=0 and D_W+T!=0. A stronger conditional corollary follows if the separately supplied rate log epsilon_n=-tau n+O(1), tau=2log(1+sqrt(2)), is valid, log(q/Delta)<=(tau-eta)n for fixed eta>0, and log C=O(n), together with full-remainder nonvanishing. This review does not establish those growing-degree hypotheses or certify Agent 1's detailed revised estimates.

The abstract limitation is exact: for m>=2, R=(m,m-1,m) has primitive row and primitive signed minors, with N=[[0,m,1-m],[-m,0,m],[m-1,-m,0]]. Here kappa=(-1,0,1), S=(2m-1,2m,2m-1), C=2m-1. Taking a=f0,c=f2 gives z0=-1,z1=1, Delta=1 and Bbar(a,c)/d_endpoint=(1-m)/(A0+A1), unbounded for fixed positive A0,A1. Primitivity follows from m-(m-1)=1; decomposability follows directly from det[R;x;y]. These arbitrary rows are not actual factorial tails. This refutes a dimension-only bound based on rank, primitivity, decomposability and opposite signs, not an estimate exploiting the actual HP structure.

## 7. Factorial arrays and shifted-minor domains

Define Q_(k,m)=sum_r [t^r]p_k/(m+r)! only for k>=0,m>=1. Applying this functional to the polynomial recurrence proves

Q_(0,m)=1/m!, Q_(1,m)=1/(m+1)!-1/(2m!),
Q_(k+1,m)=Q_(k,m+1)-Q_(k,m)/2+beta_k Q_(k-1,m), k>=1.

For H_(k,m)=Q_(k,m)-Q_(k,m+1), the rearranged formula H=Q_k/2-Q_(k+1)+beta_k Q_(k-1) is directly defined for k>=1. At k=0 one must explicitly set beta0=0 and omit the negative-index term. Iterating the shift gives, for k>=2,m>=1,

Q_(k,m+2)=Q_(k+2,m)+Q_(k+1,m)+(1/4-beta_(k+1)-beta_k)Q_(k,m)-beta_k Q_(k-1,m)+beta_k beta_(k-1)Q_(k-2,m).

The tail identity (ell_(j+1)-ell_j)(P/(1-t))=ell_(j+1)(P) follows by telescoping. Replace determinant columns by the first column and successive differences. Expansion along the evec row contributes sign (-1)^(b+1); the high-row differences contribute (-1)^(b-1). Applied to z=-B(evec,tau), or directly to the tail row, this yields

z_s=(-1)^(b+1)D_s(n,b), s=0,1,

where D_s has high rows H_(n+l,n-j), l=1,...,b-1, and last row Q_(n+1-s,n-j), columns j=0,...,b-1. This formula also works at b=1 with no high rows.

Let (Jq)_k=q_(k+1)+q_k/2-beta_k q_(k-1), with the omitted-negative-index convention at k=0. With Qmat_(n,d)[k,j]=Q_(k,n-j), and F_s selecting rows of I-J at k=n+1,...,n+b-1 followed by the selector at n+1-s,

D_s(n,b)=det(F_s(n,b) Qmat_(n,b)),
D_s(n+2,b+1)=det(F_s(n+2,b+1) J^2 Qmat_(n,b+1)).

The enlarged base window requires n-b>=1 under the stated m>=1 definition. It is valid for the intended even regime n>=4,b=n/2, but cannot silently be asserted for b=n. The left factor has finite support, so ordinary finite Cauchy–Binet supplies its exact minor expansion. It introduces an enlarged collection of minors and negative coefficients; it does not close on two old scalars or prove sign propagation.

The independent checks used only saved transitions 4->6,6->8,8->10, including explicit Cauchy–Binet sums at 4->6 with 54 nonzero left-minor terms for each s. Reference polynomials through degree 17 support those shifts; no n=12 approximant was evaluated. Scalar-array boundary checks supplement the algebraic proof and are not an all-index proof by sampling.

## 8. Agent 3 endpoint bridge only

For even n>=4,b=n/2 define Phi_n(P;x)=sum_m [t^m]P x^(n+m+1)/(n+m+1)!, whose derivatives j at 1 equal ell_j(P). Write A_k(x)=sum_m n![t^m]p_k x^m/(n+m)! and r_k(x)=T_n((1-t)p_k;x).

Direct differentiation gives (D_x-1)Phi_n(P;x)=x^n T_n((1-t)P;x)/n!; for P/(1-t) it gives x^n T_n(P;x)/n!. This identity is valid for the entire factorial-tail transform, not a truncation of the tail. In the determinant insert exp(x-1), whose derivatives at 1 are evec. Moving that row first contributes (-1)^(b-1), equal to (-1)^(b+1). Eliminating it replaces each other function by (D_x-1) of that function. Factoring the common x^n/n! from the remaining b functions multiplies their Wronskian at 1 by (n!)^(-b); the derivative product-rule transformation is triangular. Thus

z0=(-1)^(b+1)Wr(r_(n+1),...,r_(n+b-1),A_(n+1))(1)/(n!)^b,
z1=(-1)^(b+1)Wr(r_(n+1),...,r_(n+b-1),A_n)(1)/(n!)^b.

Let eta_k=(-1)^(k+b-1) and E_k=eta_k times the corresponding Wronskian. For even n this gives z0=-E_(n+1)/(n!)^b and z1=E_n/(n!)^b, hence

D_V=[A1 E_n+A0 E_(n+1)]/[h_n(n!)^b].

The ordered coefficient-minor formula follows by Cauchy–Binet: the determinant of falling powers (m_a)_j is the Vandermonde product over a<c of (m_c-m_a). Expanding the coefficient determinant along its final row yields sign (-1)^(b-1+a), exactly the source's inner alternating sum. All coefficient indices are bounded by n+b. Therefore nonnegative lower bounds E_n>=e_n>=0,E_(n+1)>=e_(n+1)>=0 with e_n+e_(n+1)>0 imply D_V>0, Y<0 and the needed ranks, since h_n>0 for even n.

The independent program checked Wronskian signs/scales at all four controls and reconstructed the full ordered-minor sum at n=6. It recovered exactly

E_6=1355870278086451/73150524144312975360000,
E_7=181648924564193/70441245472301383680000.

This accepts only the endpoint bridge. It certifies no unrelated Bernstein coefficient/difference recurrence, no termwise positivity shortcut, and no unbounded lower bounds for E_k.

## 9. Independent finite evidence

The evidence file two_scalar_quotient_independent_checks.json contains all exact z coordinates, determinant scales, primitive minors, contractions, companions, kappa and S vectors, minimizing coordinates for C, reduced p/q, bridge values, and input/protected hashes.

| n | b | sign pair | Delta | digits(q) | primitive endpoint gcd | minimizing j for C |
|---|---|---|---|---|---|---|
| 4 | 2 | z0<0<z1 | 1 | 10 | 3 | 2 |
| 6 | 3 | z0<0<z1 | 1 | 23 | 20 | 1 |
| 8 | 4 | z0<0<z1 | 1 | 43 | 140 | 1 |
| 10 | 5 | z0<0<z1 | 1 | 68 | 28224 | 1 |

The exact reduced denominators, in this order, are

1579037328;
46408283362666199304000;
2627462866500644932618935434601637157971200;
92890499671018242619170077012713821810696149560486573723113383808000.

The independently computed C values are

2009/1021;
694288919809/604385055271;
11033844156019887755931676121/9674460924431872076346352727;
6411659808416170857457639908203852821320225992509/5652190600327147840051085004116244763851484500379.

For n=4 the ledger can be checked compactly: z0=-309857/2633637888000, z1=90073/146313216000, D_V=135377/103219200, gamma_high=1/3628800, primitive minors (-1510,1515,-494), kappa=(-5,-1016,1021), S=(3025,2004,2009). The companions are r_pi=34444072/10965537 and r_e=4292250565/1579037328, yielding p_int=-9252196933 and q=1579037328.

All saved full triples were checked for integral primitivity, degree caps, endpoint matching, cofactor proportionality, high equations, original formal residual coefficients, and actual endpoint gcd/reduction. The checker compares the author's four contraction values as a multiset; the saved readback additionally shows each labeled Z0,Z1,K,d agrees with the independently labeled Z0,Z1,K_tail,d_endpoint. No label permutation is being accepted.

Fresh rational intervals use Machin's identity with 220 alternating terms for each arctangent and the e series through 300 with upper tail 1/(300*300!). They prove positive complete normalized errors and positive integer forms at each of these four controls. Saved intervals were checked for overlap and sign consistency; this does not claim independent reconstruction of every saved interval endpoint. The independent outward-rounded intervals are retained in the evidence. None of these finite nonzero controls proves nonvanishing on an unbounded sequence.

## 10. Remaining mathematical gates and delivery scope

The useful proved output is the exact rational two-scalar reduction and its complete conditional bound retaining both Delta and C, together with the endpoint bridge. Open gates are an unbounded opposite-sign law or other quantitative separation, actual factorial-structure control of C, sufficiently small fully reduced q on the same indices, and full evaluated remainder nonvanishing. There is no rationality or irrationality conclusion for e+pi.

The earlier completed reviews remain authoritative in their separate scopes. In particular the additional recurrence review's rejected strict residual-content target is not revived here. Agent 1's detailed revised reference-estimate audit and Agent 3's unrelated Bernstein recurrences are not absorbed into this verdict.

Independent artifacts in this directory: check_two_scalar_quotient_independent.py, two_scalar_quotient_independent_checks.json, two_scalar_quotient_independent_stdout.txt. A separate TWO_SCALAR_QUOTIENT_INDEPENDENT_REPORT.md supplies the concise completion report without changing the historical REPORT.md.
