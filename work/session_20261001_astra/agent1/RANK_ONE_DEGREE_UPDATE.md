> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Rank-one degree update between endpoint lifts

Author research, 2026-10-01. New structural deductions; no independent review, scans, or repeated controls. The retained FIXED_WEIGHT_CONTACT_NORMALITY theorem is used as an AUTHOR DEPENDENCY, not promoted to independently accepted status.

## 1. Hypotheses and conventions

Put K=2n+b, with n>=1 and 1<=b<=n. Let R_T=A+B exp(z)+CF(z), where F(0)=0, F'=2/Q, Q=1-z+z^2/2. Contact K means R_T=O(z^K). Write E(T)=(A(1),B(1)) on triples satisfying B(1)=C(1).

The balanced hypothesis used below is precisely:

(BN) The square contact system with caps (n-1,b-1,n-1) and contact K has zero kernel.

All unconditional-from-balanced conclusions are stated on the accepted range of (BN). No numerical cutoff for that accepted range is invented here: its exact statement was not present in the material available within this agent's directory. Statements using the weighted author theorem additionally require n>=ceil(exp(32)), 1<=b<=floor(log n). Thus their domain is the intersection of that explicit author range with the accepted (BN) range.

The weighted hypothesis is:

(WN-author) The square contact system with caps (n,b-1,n-1) and contact K+1 has zero kernel.

This is exactly the retained author theorem. Its calculations are not repeated.

The three matched spaces are

 U: caps (n+1,b,n), contact K;
 V: T in U with a(T):=[z^(n+1)]A=0;
 W: T in U with ell(T):=[z^K]R_T=0.

V is the balanced RELAXED endpoint space, with contact K. W is the genuinely weighted endpoint space, with contact K+1. These contacts must not be conflated with the older balanced contact-K+1 selector line.

## 2. Dimensions and the endpoint-zero direction

The balanced contact space before matching has 2n+b+3 coefficients and K Taylor constraints, hence dimension at least three. If all three coefficient endpoints vanish, division by z-1 produces a solution of (BN). Thus its endpoint map to Q^3 is injective, and consequently an isomorphism. After matching, dim V=2 and E:V->Q^2 is an isomorphism. Write its inverse L_b.

Consider now H: caps (n,b-1,n-1), contact K, without matching. Its coefficient count is K+1, so dim H>=1. The functional [z^n]A has zero kernel on H by (BN), hence dim H=1 and this functional is an isomorphism. There is a unique h=(A_h,B_h,C_h) in H with [z^n]A_h=1.

Define

 D=(z-1)h.

Then D lies in U, E(D)=0, and a(D)=1. Conversely every endpoint-zero element of U is divisible componentwise by z-1 and its quotient lies in H. Therefore

 ker(E|U)=Q D,
 U=V direct-sum Q D,
 dim U=3.

This argument derives the common-space dimension using balanced normality alone. It does not use the weighted theorem to infer this dimension.

## 3. Exact rational endpoint covector

Let T_X=L_b(1,0), T_Y=L_b(0,1), and

 f_X=ell(T_X), f_Y=ell(T_Y), Delta=ell(D).

For e=(X,Y)^T, write f(e)=f_X X+f_Y Y. Under (WN-author), Delta is nonzero: otherwise h would have contact K+1, contradicting that square theorem. Hence

 L_w(e)=L_b(e)-D f(e)/Delta.                         (3.1)

This is the requested rank-one map. All coefficients of D and f/Delta are rational. It proves E:W->Q^2 is an isomorphism and identifies its inverse explicitly.

The highest A coefficient is

 [z^(n+1)]A_w(e)=-f(e)/Delta.                       (3.2)

Thus the update is genuinely nonbalanced exactly on endpoint directions for which f(e)!=0. Nonzero Delta alone does not prove that f is a nonzero covector. Formula (3.1) is always an outer-product update of rank at most one, and has rank exactly one if and only if f!=0. No adjacent balanced-normality implication is asserted here. Establishing f!=0 throughout a concrete range remains separate from the proved denominator nonvanishing. Formula (3.2) is the exact criterion for each endpoint direction.

For an entirely explicit finite rational construction of f, order the balanced unknown coefficients as A_0,...,A_n,B_0,...,B_b,C_0,...,C_n. Let M_b have rows consisting of the K Taylor equations, B(1)-C(1), A(1), and B(1), in that order. It is square and invertible by (BN). Its Taylor entries are

 A_j column: 1 if k=j, otherwise 0;
 B_j column: 1/(k-j)! if k>=j, otherwise 0;
 C_j column: mu_(k-j-1) if k>=j+1, otherwise 0,

where mu_r=L(t^r). Let J insert (X,Y) into the last two right-hand-side positions, with all other positions zero. Let c_K be the same Taylor row at index K. Then

 (f_X,f_Y)=c_K M_b^(-1) J.                          (3.3)

This is an explicit rational endpoint covector, with a specified matrix, row ordering, and factorial/moment entries; it is not an unspecified selector.

## 4. Actual forcing and denominator scales

Use the established isomorphism S_n(C)=Q^n D_z^n(CF) on deg C<n. Set

 w=exp(z)Q(z)^n, s_k=[z^k]w, q_k=[z^k]Q^n,
 T=(s_(n+r-j))_(r,j=0,...,b-1),
 q=(q_n,...,q_(n+b-1))^T,
 r=(s_(n+b-j))_(j=0,...,b-1).

Negative coefficient indices are zero. Balanced square normality is equivalent to det T!=0: after n derivatives its polynomial block is eliminated, S_n handles C, and the remaining b rows are exactly T.

For h normalized as above, put V_h=(D_z+1)^n B_h. Differentiating its contact conditions n times and multiplying by Q^n gives

 n! Q^n+w V_h+S_n(C_h)=O(z^(n+b)),
 V_h=-n! T^(-1)q.                                  (4.1)

Thus the actual forcing scale is n!, and

 B_D=(z-1)B_h=-n!(z-1)(D_z+1)^(-n)(T^(-1)q).        (4.2)

The inverse differential operator is finite on polynomials of degree <=b-1:

 (D_z+1)^(-n)=sum_(k=0)^(b-1) (-1)^k binom(n+k-1,k)D_z^k.

Define the retained bordered determinant with EXACT ordering

 D_border=det [[T,q],[r,q_(n+b)]].

Its Schur complement is S=q_(n+b)-r T^(-1)q, so D_border=det(T) S. Since taking n derivatives multiplies the first surviving Taylor coefficient at K by K!/(n+b)!, while multiplication by Q^n leaves that leading coefficient unchanged,

 [z^K]R_h=n!(n+b)!/K! * S,
 Delta=-n!(n+b)!/K! * D_border/det T.               (4.3)

The minus sign comes from D=(z-1)h. Consequently

 -f(e)/Delta=K!/[n!(n+b)!] * f(e)det T/D_border.    (4.4)

These are the actual Taylor and endpoint-lift scales. The factorial in (4.4) cannot be counted as a gain independently of the determinant ratio.

Combining (4.2)-(4.4) also cancels det T exactly:

 B_w(e)-B_b(e)
 =-K!/(n+b)! * f(e)/D_border
      *(z-1)(D_z+1)^(-n)(adj(T)q).                 (4.5)

Thus the common balanced determinant denominator in the endpoint-zero direction does not survive twice. The remaining denominators are the endpoint forcing f(e), through M_b^(-1), and the single actual border D_border. This is a useful exact cancellation, rather than a comparison of reference errors.

## 5. A lower bound for the update denominator

The retained author theorem supplies, with d=b+1 and a0=1+sqrt(2),

 |D_border|>=a0^(nd) exp(-2d)
 /[d! b! 2^(d^2+4d+2) d^(d^2) n^(d^2/2)].

We use that result as an author dependency without rederiving it. A new elementary upper bound suffices for the balanced denominator in (4.3). On |z|=rho=sqrt(2),

 |s_k|<=exp(rho) a0^n rho^(n-k).

Row and column scaling of T removes rho^(j-r), with total determinant scale one. Hadamard's inequality gives

 |det T|<=b^(b/2) exp(rho b) a0^(nb).

Therefore

 |Delta|>= n!(n+b)!/K! * a0^n exp(-2d-rho b)
 /[d! b! 2^(d^2+4d+2) d^(d^2) n^(d^2/2) b^(b/2)].  (5.1)

This is a genuine quantitative denominator bound; Delta is no longer merely declared nonzero. For b<=log n its logarithmic lower bound is

 log|Delta|>=n log((1+sqrt(2))/4)-O((log n)^3).

The factorial ratio follows from ordinary factorial estimates, uniformly for b<=log n. This lower bound can be exponentially small and does not supply a favorable update by itself.

For completeness the numerator has the direct exact expression

 f(e)=sum_j B_b,j(e)/(K-j)! + sum_j C_b,j(e)mu_(K-j-1).

With eta=1/sqrt(2), its elementary bound is

 |f(e)|<=||B_b(e)||_1/(K-b)!
          +2 eta^(K-1) sum_j |C_b,j(e)| eta^(-j).   (5.2)

The unresolved quantities are actual endpoint-lift coefficient norms in (5.2), or the more economical combined expression in (4.5). An unevaluated endpoint inverse cannot be discarded merely because (5.1) exists.

## 6. Exact B-only factorial Gram centers

A center requires a specified positive quadratic metric. To avoid silently choosing one, first give formulas valid for EVERY rational positive-definite B-coefficient Gram matrix G. They therefore apply to any fixed B-only factorial metric.

Write u=coeff(B_b(1,0)), v=coeff(B_b(0,1)), dB=coeff(B_D), alpha=f_X/Delta, beta=f_Y/Delta. Then

 B_b(X,1)=Xu+v,
 B_w(X,1)=X(u-alpha dB)+(v-beta dB).

For b>=4, projection onto B is injective on U. Indeed, if B=0, then Q^(n+2)D_z^(n+2)(CF) is a polynomial of degree at most n+1: the derivative eliminates the logarithmic polynomial part, and its decay at infinity gives this degree bound. Contact K forces this polynomial to vanish to order at least K-n-2=n+b-2>=n+2 at zero. It is therefore zero. Hence CF is polynomial, which forces C=0 because F is not rational; contact then forces A=0. Consequently u and u-alpha dB, each corresponding to endpoint (1,0), are nonzero, and both Gram denominators below are strictly positive for b>=4. For 1<=b<=3, the formulas retain their explicit nonzero-denominator hypotheses; no B-injectivity claim is made.

Define

 a=u^TGu, c=u^TGv, h=u^TGdB, k=v^TGdB, s=dB^TGdB.

If a>0, the balanced center is x_b=-c/a. If

 a_w=a-2alpha h+alpha^2 s>0,

then the weighted center is exactly

 x_w=-(c-beta h-alpha k+alpha beta s)/a_w.          (6.1)

Equivalently, putting r0=v+x_b u and t0=beta+alpha x_b,

 x_w-x_b=[alpha dB^TG r0+t0 h-alpha t0 s]/a_w.     (6.2)

The center shift thus depends on the actual forcing covector and B-direction, not solely on a smaller reference error. If a or a_w is zero, its B-only norm is independent of X and has no unique center. These cases must not be divided through.

For an explicit standard factorial metric take m>=b and

 P_m(B;x)=sum_(j=0)^b B_j x^(m-j)/(m-j)!,
 ||B||_m^2=integral_0^1 P_m(B;x)^2 dx.

Its rational positive-definite Gram is

 G_m,ij=1/[(m-i)!(m-j)!(2m-i-j+1)].                (6.3)

The exact degree-shift comparison is

 G_(m+1),ij/G_m,ij
 =(2m-i-j+1)/[(m+1-i)(m+1-j)(2m-i-j+3)].          (6.4)

If balanced and weighted estimates use different factorial centers, substitute their actual matrices separately in (6.1). In particular the natural shifts m=n+1 and m=n+2 are covered by (6.4). This ratio is not constant across i,j, so there is no universal multiplicative conversion of centers.

For complete generality with G_b and G_w, define U_w=u-alpha dB, V_w=v-beta dB. Then

 x_b=-u^TG_b v/(u^TG_b u),
 x_w=-U_w^TG_w V_w/(U_w^TG_w U_w).                 (6.5)

Their equality is precisely equality after cross multiplication. These formulas compare actual rational centers whenever the metrics are rational and the denominators nonzero. A real norm-minimizing center is then itself rational; no rounding is needed for these particular quadratic metrics.

The full pulled-back endpoint Grams also obey an exact rank-at-most-two relation. With L=[u,v], f=(f_X,f_Y),

 H_w-H_b=-(L^TGdB f+f^T dB^TG L)/Delta
                +(dB^TGdB) f^T f/Delta^2.         (6.6)

The lift update has rank at most one (exactly one when f!=0); its Gram update has rank at most two. Calling both updates rank one would be incorrect.

## 7. Endpoint cancellation and primitive stopping rule

For every prescribed rational pair (X,Y), equation (3.1) gives exactly the same endpoints, and

 R_w(1)=R_b(1)=X+Y(e+pi),
 R_w(z)-R_b(z)=-f(X,Y)/Delta *(z-1)R_h(z).         (7.1)

The added Taylor contact is compensated by a function vanishing at the evaluation point. This identity is stronger than a norm comparison.

When Y!=0, both lifts have the identical reduced ratio X/Y and identical primitive pair (p,q), after the same sign convention q>0. Therefore the primitive evaluated forms p+q(e+pi) are identical. Different polynomial contents or coefficient clearers cannot change that conclusion.

STOP: transporting a fixed endpoint selection from balanced to weighted by (3.1) is not a new-approximant improvement. It only changes the representation and possible certificates for the same primitive forms. No further raw reference-error comparison is warranted for that selection.

Choosing the center separately in each B-only norm is a DIFFERENT selection. At Y=1 it changes the rational approximant exactly when x_w!=x_b. Equations (6.1)-(6.5) decide that algebraically, but no universal inequality or nonzero shift is claimed. A shifted center can have a much larger reduced denominator. The relevant primitive comparison must retain den(x_w), not a coefficient clearer or the norm alone.

The older stopped selector is preserved: inside W, imposing a=0 gives W intersect V, equivalently f(X,Y)=0. This is precisely the balanced contact-K+1 slice. Its triples and primitive pairs coincide with those of that balanced slice, exactly as established previously. The present broader stopping result concerns all prescribed endpoints, even when the two lifts are different triples.

## 8. Results and remaining term

New results are the common-space direct sum and normalized endpoint-zero direction; explicit rational endpoint covector; factorial-scaled Schur formula (4.3); adjugate cancellation (4.5); quantitative denominator bound (5.1); and exact factorial Gram-center and Gram-update identities.

All structural statements depend on (BN). Nonzero Delta and the explicit bound additionally depend on the retained weighted AUTHOR theorem. No theorem's review status has been changed.

For a fixed endpoint selection the approximant route is stopped by exact identity. For a newly chosen Gram-center selection, a favorable bound is still missing for

 f(e)/D_border *(D_z+1)^(-n)(adj(T)q),

including the factor K!/(n+b)! in (4.5), and ultimately for the denominator of the selected rational center. The lower bound (5.1) alone does not control the endpoint forcing f(e). This is the precise remaining quantitative term, not a free extra factorial gain.

No shrinking, complete-remainder nonvanishing, or irrationality conclusion follows. No prior proof was audited or recalculated.
