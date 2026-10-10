> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Root multiplicity research, stage 3

Status: limited independent review of the assigned NEW general polynomial implications; original exact pencil displacement calculation with an unresolved multiplicity obstruction. No growing-pole multiplicity theorem or irrationality conclusion is claimed.

## Limited review

Source read in full: work/parallel_batch_01/main/DOMINANT_RATIONAL_FACTOR_CONTENT_BOUND_STAGE3.md. Historical analytic localization is an inherited hypothesis, not audited here. This review does not review the preceding upper-bound refinement.

1. Nonlinear irreducible discriminant estimate: VALID. A primitive irreducible integer factor f of degree d>=2 is separable in characteristic zero. Its discriminant is a nonzero integer. If all its roots lie in the stated radius-R disk and its positive leading coefficient is a, then 1<=|Disc(f)|<=a^(2d-2)(2R)^(d(d-1)). With L=log(1/(2R))>0, division by 2d-2 gives log a>=dL/2. Repetition of f in P does not affect this argument; its contribution is multiplied by its exponent.

2. Dominant rational-factor exception: VALID. Gauss's lemma and positive orientation give P=product f_i^e_i with no nonunit scalar, so failure of log A>=mL/2 forces some linear factor qT-p with log q<L/2. Two distinct such reduced rational roots would have separation at least 1/(qq')>2R, impossible in the disk. This proves the stated uniqueness among small-denominator rational roots, not uniqueness of all rational roots.

3. Exact multiplicity inequality: VALID. If P=(qT-p)^e Q with exact multiplicity e and n=m-e, then Q(p/q)!=0 and A=q^e B. The nonzero integer resultant equals q^n Q(p/q); in modulus it is at most q^n B(2R)^n. Thus log A>=(m-e)L+(2e-m)log q. When n=0, primitivity and positive orientation force Q=B=1; the resultant is 1 and the inequality is equality log A=m log q. If log q<L/2 and e<=m/2, subtraction of mL/2 yields (2e-m)(log q-L/2)>=0, contradicting the hypothesized failure. Strict majority follows.

4. Unconditional e_* formulation: VALID. Either log A>=mL/2 already, or the exceptional multiplicity exceeds m/2 and therefore is the largest rational-factor multiplicity. Dropping its nonnegative (2e-m)log q term gives log A>=(m-e_*)L. Together these prove log A>=min(m/2,m-e_*)L. For m=1, e_*=1 and this is the correct zero bound. For a pure rational linear power it likewise permits zero. No squarefreeness hypothesis was accidentally introduced.

The actual-polynomial specialization is a valid application whenever its inherited root radius satisfies 2R<1 and the inherited degree statement holds. It retains the full coefficient clearer and final gcd. The unknown e_* remains an unknown; the general theorem does not determine it.

## Original research: complete rational pencil and an exact boundary identity

Starting sources read in full: historical main/GENERAL_POLE_RANK_M_PRIMITIVE_INTERFACE.md and agent3_analysis/GROWING_POLE_ALL_ROOT_LOCALIZATION.md under work/session_20261002_codex_continuation/.

Use N=2k, k>=m>=1. Write rho=mu-nu_m and tau_s(y^r)=R_r+s nu_m(y^r), where R_r=a_(m,r)-(2r)!. Here a_(m,r) is the full rational part of the normalized compact rational-kernel moment; nu_m contains every derivative through m-1. Define

 T(s)=[rho(y^(i+j)); tau_s(y^(i+j))]_(0<=i<k,0<=j<N),
 W=T'(s)=[0;nu_m(y^(i+j))].

Thus det T(s)=beta(s), exactly. At s=S, adding e times the top rows recovers the full compact functional sigma_m. No exponential or rational endpoint has been deleted. Work with this rational pencil to avoid mistaking symmetry of individual Hankel blocks for symmetry of a square effective matrix.

Let Y be multiplication by y truncated to degrees below N: for p of degree below N with top coefficient p_(N-1), Yp=yp-p_(N-1)y^N. Let Z be the k-by-k row shift with Z_(i,i+1)=1 for i<k-1 and last row zero. Put Z_2=diag(Z,Z). Define the two terminal rows

 d_rho=(rho(y^(k+j)))_(0<=j<N),
 d_tau(s)=(tau_s(y^(k+j)))_(0<=j<N),

and the column

 v(s)=(rho(y^(N+i)))_(0<=i<k) concatenated with (tau_s(y^(N+i)))_(0<=i<k).

Let u_rho and u_tau be the unit columns at the last row of the top and bottom blocks, respectively; let e_top extract the coefficient of y^(N-1). Then the ACTUAL pencil satisfies

 T(s)Y-Z_2 T(s)=u_rho d_rho+u_tau d_tau(s)-v(s)e_top^T.     (D)

In particular its displacement rank is at most three, with all terminal moments displayed.

Proof. In a nonterminal row indexed i<k-1, applying its functional to Yp gives lambda(y^(i+1)p)-p_(N-1)lambda(y^(N+i)); the first term is the next row of T(s)p. In a terminal row i=k-1, the corresponding first term is lambda(y^k p), supplied by the relevant d row. This proves every entry of (D). At the last column, the terminal contributions cancel the subtracted moment exactly, as required because Y y^(N-1)=0. The maximum moment index is 3k-1, one beyond the original stack's 3k-2: dropping this endpoint would make the identity false.

Differentiating gives the accompanying identity for the actual response:

 WY-Z_2 W=u_tau d_nu-v_nu e_top^T,                         (E)

where d_nu=(nu_m(y^(k+j)))_j and v_nu has zero upper block and lower entries nu_m(y^(N+i)). This retains all Taylor factorials implicitly through the exact moment functional; no derivative-coordinate rescaling is performed.

## What the identity does and does not establish

For a root r and a right nullvector p of T(r), identity (D) gives

 T(r)Yp=u_rho rho(y^k p)+u_tau tau_r(y^k p)-v(r)p_(N-1).  (F)

Thus multiplication by y does not preserve the actual root space without controlling three boundary contributions. Even imposing p_(N-1)=0 leaves the two terminal moments. Hankel structure alone is insufficient to manufacture an invariant multiplication space or a positive bilinear eigenvalue problem.

The inherited effective reduction is

 beta(S+t)=beta(S) det(I_m+t J_m H_eff).

Its nonzero leading coefficient implies J_m H_eff is invertible. Algebraic multiplicities of roots correspond to algebraic eigenvalue multiplicities of this matrix; kernel dimensions count only geometric multiplicity. The documented failure of the natural symmetry substitution is inherited and was not recomputed.

More explicitly, a formal right chain for the rational pencil at r satisfies

 T(r)p_0=0,
 T(r)p_j=-W p_(j-1), j>=1.

A nonzero left nullvector lambda gives the necessary extension conditions lambda^T W p_(j-1)=0. If nullity is one, simplicity is equivalent to a nonzero left-right response pairing lambda^T W p_0. Neither the full moment formulas nor (D) presently give a sign or nonvanishing theorem for this pairing. For larger nullity the determinant order aggregates the local partial multiplicities; controlling just one chain or a rank is not enough.

These observations are not claimed as a new multiplicity criterion. Their useful original component is the explicit boundary calculation (D)-(F), which shows precisely what is missing from the multiplication-based approach. A low displacement rank does not bound eigenvalue multiplicity. I stop this branch before assuming that it does or assuming an unproved symmetrizer.

## Endpoint case and unresolved target

The requested majority exclusion cannot hold for m=1: the inherited degree-one actual rational polynomial necessarily has a rational zero of exact multiplicity one, which exceeds m/2. Equivalently, at that zero the only derivative of order at most floor(m/2)=0 is zero. Any useful positive theorem must therefore explicitly restrict m>=2, with m tending to infinity for the requested growing-pole range.

For m>=2, this stage proves no exclusion of a rational factor of multiplicity greater than m/2, on any infinite growing-pole range. Rationality of r makes T(r) and its chains rational but supplies no sign for the response pairing. The inherited nonzero value at S and localization also do not settle multiplicity.

A narrowly useful next target is to derive a bilinear identity for the full left-right response pairing, using the actual matching equations and the three boundary terms in (F), with a proved sign or nondegeneracy statement on an explicit parameter range. Such an identity would contain information beyond rank and beyond rephrasing derivative vanishing. Without it, a purported simplicity or majority-multiplicity proof would have an explicit unresolved gap.

No numerical factorization atlas, coefficient-gcd test, diagonal compact-determinant calculation, networking, or old audit was performed. No new computation is needed for the entrywise proof above. Earlier stage files are preserved. The present stage provides a completed limited review and a bounded original structural calculation with an explicit remaining obstruction, not a solution of the main arithmetic interface.
