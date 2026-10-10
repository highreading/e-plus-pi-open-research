> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Root-bound review and extension, stage 2

Status: limited independent review of Main's NEW implications, conditional on the explicitly inherited analytic inputs; original upper-bound refinement proved by this author, not independently reviewed. S denotes the actual e+pi. No irrationality or primitive-content conclusion follows.

## 1. Sources and inherited hypotheses

Read in full: work/parallel_batch_01/main/REVERSE_COEFFICIENT_ROOT_BOUND_STAGE2.md; work/parallel_batch_01/main/ROOT_ANNULI_AND_ACTUAL_RESULTANTS_STAGE1.md; and the historical agent3_analysis/GROWING_POLE_ALL_ROOT_LOCALIZATION.md and GROWING_POLE_ORDER_SHORT_COMPLETE_PRODUCT.md under work/session_20261002_codex_continuation/.

Assume their complete analytic identities and estimates for k>=131072, 1<=m<=k. These historical analytic results are inherited hypotheses, not independently audited here. Write beta(S+t)=sum b_l t^l for the ACTUAL complete stack. Its degree is exactly m, b_0 and b_m are nonzero, and all endpoint jets remain present.

Set ell=log(1+sqrt(2)), c=4ell, a=1/(48e^4), C=4/a, L0=exp(-C), C0=log(32 pi^2(3+2sqrt(2))^2). Let F*>0 and I_l be the actual compact insertion determinants from those sources; I_k=1. Put g_m=4^(m-1)/binom(2m-2,m-1) and kappa_m=g_m^m.

The inherited leading coefficient bounds are L0 kappa_m F* I_m <= |b_m| <= kappa_m F* I_m, and L0 F* I_0 <= |b_0| <= F* I_0. No scalar normalization changes these coefficient ratios or roots.

## 2. Limited review of Main's new implications

Verdict on insertion ratios: VALID under the inherited normalized insertion identity. I_l/I_0 is the product of successive value kernels. For positive measures w>=gamma/2, the variational formula K_w(z)=sup |p(z)|^2/integral |p|^2 dw gives K_w<=2K_gamma. The same applies to sigma_m(1+y)^(2r), since its density is at least gamma/2. Summing c(k-r)+2log k+log2 gives exactly ck-2ell(l-1)+2log k+log2 after division by l. The measure keeps pole order m throughout.

Verdict on middle-coefficient normalization: VALID. The inherited bound includes 1/l!, and division by |b_0|>=L0 F* I_0 gives Main's E_l exactly. Subtracting E_1 leaves (l-1)(-2log k+log2-2ell)+C/l-C-log(l!)/l, which is nonpositive. The lower bound for the constant coefficient, rather than an upper bound, is used in the correct direction.

Verdict on l=m and m=1: VALID. The leading coefficient uses its separate exact confluent factor kappa_m, not the middle-coefficient bound. The inequalities kappa_m^(1/m)<=2m-1<=3^(m-1)<=exp(2ell(m-1)) justify the simplification. When m=1, g_m=kappa_m=1, no middle index exists, and the displayed majorant remains valid. I_k=1 introduces no extra factorial when m=k.

Verdict on reverse exclusion disk: VALID. With M=exp(ck+E_1), every normalized coefficient is bounded by M^l. For |t|<=1/(2M), the finite sum is at most 1-2^(-m)<1, so the constant term cannot cancel. The closed disk is excluded, giving the stated non-strict logarithmic lower bound with W=E_1+log2. This applies to all complex roots and multiplicities.

Verdict on Stage 2 annulus and its stated regime: VALID. Combining that lower bound with the inherited U=O(m^2+m log(k+1)+1) yields the uniform two-sided exponent for m=o(sqrt(k)). The earlier Stage 1 sufficient regime remains valid and is weaker.

Verdict on asymmetric coprimality: VALID. When t=exp[-c(K-k)+W(k,m)+U(K,n)]<1, every root of the later polynomial is strictly nearer S than every root of the earlier polynomial. Thus there is no common complex root. For fixed proportional separation, m log k=o(k) and n=o(sqrt(K)) suffice. Main's example m=floor(k^(3/4)), n=floor(K^(2/5)) satisfies those conditions.

Verdict on resultant comparison and primitive normalization: VALID. For actual primitive polynomials P,Q of degrees m,n and positive leading coefficients A,B, factor alpha-S from every cross difference. This gives |Res(P,Q)|=B^m|P(S)|^n times a product of mn factors with moduli between 1-t and 1+t. Integer nonvanishing combined with the UPPER estimate implies B^(1/n)|P(S)|^(1/m)>=1/(1+t). The exponent allocation is correct. Actual coefficient clearers and final gcds are retained by Res(I,J)=g^n h^m Res(P,Q), up to signs. The degree-normalized paired leading bound follows from the inherited product estimate with error O(m+log k+log(m+1)+1)=o(k) in the stated regime. It supplies no individual leading-coefficient lower bound.

No correction to these reviewed implications is required. This verdict does not certify the historical analytic hypotheses or the new original research below.

## 3. Original refinement: exact Taylor weights

Write d=m-1 and nu_m(f)=sum_(j=0)^d a_j f^(j)(-1), with the actual coefficients
 a_j=2^j binom(d,j)(2(d-j)-1)!!/(2d-1)!!.
In Taylor coordinates v=u+1, the coefficient weight is w_j=a_j j!, not a_j alone. For 0<=j<d,
 w_(j+1)/w_j=2(d-j)/(2(d-j)-1)>1.
Therefore 0<w_j<=w_d=d!/(1/2)_d=g_m. For m=1 this says w_0=g_1=1. This elementary identity uses every actual endpoint derivative; no jet is discarded.

For a polynomial P(v_1,...,v_l), define ||P||_r=sum_alpha |[v^alpha]P| r^|alpha|. For 0<r<=1, application of all l jet functionals is bounded by
 |nu_m^tensor(l)(P)| <= g_m^l r^(-l(m-1)) ||P||_r.
Indeed the selected exponents satisfy alpha_a<=m-1, their weights are at most g_m^l, and r^(-|alpha|)<=r^(-l(m-1)). This includes the entire selected sum, not only its top term.

The old bound replaced each w_j by 2^j. Near l=m this discarded a large gain: g_m grows only on the order of sqrt(m).

## 4. Original refinement: confluent Vandermonde coefficient norm

Let Delta(v)=det[v_i^(j-1)]_(i,j=1)^l. Its l! distinct monomials all have degree l(l-1)/2 and coefficient of modulus one. Thus
 ||Delta||_r=l! r^(l(l-1)/2),
 ||Delta^2||_r<=(l!)^2 r^(l(l-1)).
The latter follows from submultiplicativity and does not assume absence of cancellation. It improves the old product-of-pairs bound 2^[l(l-1)]r^[l(l-1)]. We need only this inequality; no unproved exact absolute coefficient formula is used.

## 5. Complete insertion bound with a variable radius

For 1<=l<m, let h=m-l, v_a=u_a+1 and cross_0=product_i(1+x_i)^(2l). The inherited exact formula is
 b_l=(-1)^k/[l!(k-l)!] integral Delta(x)^2 nu_m^tensor(l){Delta(v)^2 product_(a,i)(v_a-1-x_i)^2 F(x,v-1)} d sigma_m^(k-l).

The inherited real conditional comparison bounds |F| by F* on the full cube, and F has degree at most k in each inserted variable. Repeated univariate Markov gives the Taylor coefficients bounded by F*k^(2|alpha|)/product alpha_a!. Summing yields, for every r>0,
 ||F(x,v-1)||_r <= F* exp(l k^2 r).
This is a finite-polynomial Taylor norm bound, not a claim of positivity at complex nodes.

For x_i in [0,1],
 ||product_(a,i)(v_a-1-x_i)^2||_r <= cross_0 exp(2rl(k-l)).
Let D_k=k^2+2k. Combining these bounds with Sections 3 and 4, then integrating the actual compact measure, proves for 0<r<=1:
 |b_l| <= F* I_l l! g_m^l r^(-lh) exp(l D_k r).
The l! here is the remaining factor (l!)^2/l!. The compact integral's factor 1/(k-l)! is already in I_l. These factorials are not suppressed.

Dividing by the inherited NONZERO leading coefficient gives
 |b_l/b_m| <= exp(C) (I_l/I_m) l! g_m^(-h) r^(-lh) exp(l D_k r).                 (A)
This keeps the exact leading confluent factor kappa_m=g_m^m.

For l>=1, the radius-dependent logarithm is -lh log r+l D_k r. Its global minimum on positive radii is at r=h/D_k. Since 1<=h<=m<=k, this radius lies in (0,1], so the preceding jet bound applies without alteration. Consequently
 (1/h)log|b_l/b_m| <= (1/h)log(I_l/I_m)+C/h+log(l!)/h-log g_m+l log(D_k/h)+l.   (B)
Zero coefficients satisfy the corresponding exponential inequality automatically.

For l=0, separately use |b_0|<=F* I_0 and |b_m|>=exp(-C)g_m^m F* I_m to obtain
 (1/m)log|b_0/b_m| <= (1/m)log(I_0/I_m)+C/m-log g_m.                         (C)
Thus no limiting interpretation of the optimized radius or a nonexistent inserted variable is required.

## 6. Explicit every-root upper bound

The inherited actual insertion-ratio bound states, for every 0<=l<m and h=m-l,
 (1/h)log(I_l/I_m) <= -ck+(c+log4)(m-1)+2log k+C0+log(6m).
Its direction follows from lower bounds on each value kernel, since I_l/I_m is the reciprocal of their product.

Use g_m>=1, C/h<=C, log(l!)/h <= (m-1)log(m+1), and l log(D_k/h)+l <= (m-1)log D_k+(m-1). These also give a common majorant for (C). Therefore define
 U_new(k,m)=2log k+(c+log4)(m-1)+C0+log(6m)+C
             +(m-1)[log(m+1)+log(k^2+2k)+1]+log2.
For all k>=131072 and 1<=m<=k, EVERY complex root alpha of the actual degree-m polynomial satisfies
 log|alpha-S| <= -ck+U_new(k,m).                                           (D)

Proof of the passage to roots: let M=max_(0<=l<m)|b_l/b_m|^(1/(m-l)). Equations (B)-(C) bound log M by -ck+U_new-log2. For |t|>2M, the sum of all lower terms divided by |b_m t^m| is less than sum_(h=1)^m 2^(-h)<1. Hence the leading term cannot cancel. This proves (D), independently of real-rootedness or simplicity. The argument uses every coefficient and does not infer individual localization from product smallness.

Uniformly for 1<=m<=k, U_new=O(m log(k+1)+1), with absolute constants. For m=1, Sections 3-5 have no middle index, (C) supplies the result, and the displayed U_new reduces to 2log k+C0+log6+C+log2. For m=k, I_m=1 and all estimates remain valid, though this coarse bound need not imply shrinking roots. No claim about the separately assigned diagonal primitive-value threshold is made.

Combining (D) with Main's reviewed reverse bound gives the actual annulus
 exp[-ck-W(k,m)] <= |alpha-S| <= exp[-ck+U_new(k,m)].
Thus for every integer sequence m log k=o(k), uniformly over ALL complex roots with multiplicity,
 log|alpha-S|=-4k log(1+sqrt(2))+o(k).
This extends the inherited upper regime m=o(sqrt(k)). For example m=floor(k^(3/4)) is allowed asymptotically. The theorem is conditional on the inherited complete analytic inputs, while the refinements and their combination are proved here.

## 7. Obstruction, scope and handoff

The old pairwise Vandermonde estimate loses exp(O(l^2)); at h=1 this produces the unwanted O(m^2) root-exponent error. Optimizing its Taylor radius alone would not remove that loss. The present factorial Vandermonde estimate replaces it by O(l log(l+1)), while the maximal actual Taylor weight cancels against most of the exact leading factor. The optimized radius then retains l log(D_k/h)+l. Even at the worst near-leading index h=1, the resulting loss is only O(m log k).

This particular absolute-norm/Markov method still leaves O(m log k), notably from the k^2 derivative scale and factorial norm. It does not establish the two-sided asymptotic for every m=o(k), nor for proportional pole order. Further refinement would require additional structure beyond these majorants; no such refinement is asserted.

All statements concern the original complete polynomial and hence its actual primitive scalar multiple. No basis factor, moment clearer, coefficient gcd or rational denominator is evaluated or replaced. The result is analytic localization, not control of primitive small values. Main may combine this improved upper bound with its resultant argument; resultant/content coupling and rational-factor multiplicity bounds remain Main's task.

No new numerical computation or external source access was needed. These are symbolic proofs; no finite experiment is presented as verification. This stage preserves the separate completed PAIRED_EXTRACTION_STAGE1.md and does not repeat that research.
