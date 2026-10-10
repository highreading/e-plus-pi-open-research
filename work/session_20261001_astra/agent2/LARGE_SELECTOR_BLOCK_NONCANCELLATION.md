> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Large selectors: large-forcing adjacent pairs and a signed block bound

New author mathematics. The completed LARGE_SELECTOR_ENDPOINT_DOMINANCE.md is preserved without repeated checks. The main LARGE_SELECTOR_SELECTION_DRAFT.md and LARGE_SELECTOR_EXPONENTIAL_REMAINDER_DRAFT.md were read as author inputs. The actual dyadic denominator law remains a separate author dependency. No numerical search, independent review, or old computation is performed.

The new results are: uniform extension of the enclosure to the enlarged adjustment; many consecutive integer pairs with large forcing at BOTH nodes; an exact quarter-turn relation for consecutive endpoint integrals with an explicit remainder; and a block lower bound expressed through a finite rational phase determinant. No positive asymptotic lower bound for that determinant is established. Thus no unconditional large-forcing/noncancellation subsequence is claimed.

## 1. Uniformity before selection

Fix rho>0 and a constant C>0. Let n=2^s, s>=2, and consider nonnegative integers m in

    |m-rho n log n| <= C n log n/log log n.

All assertions about this interval are for sufficiently large n, so its lower endpoint is positive. Write m_lo and m_hi for integer bounds containing it. Then m_hi=O_rho,C(n log n) and m_lo is at least rho n log n/2 eventually.

Use the retained rational differential

    V(w)=w^2-w+1/2,
    A(w)=(2w^2-1)^2,
    G_m(w)=V(w)^n A(w)^m/w^(n+1).

Let alpha=(1+i)/2, c0=1/2, and h0=-i/2. The upper endpoint contribution is

    J_m=integral_(c0)^alpha G_m(w)dw.

The lower contribution is -conjugate(J_m). Thus, retaining both conjugate phases,

    Flog(n,m)=(-1)^(n+1)4n! Im J_m.

The forcing denominator is D(n,m)=n!2^(-n)U(n,m). On eligible nodes the main arithmetic input supplies U!=0 and v2(U)=n/2.

The saved endpoint construction defines Gaussian-rational coefficients g_j(n,m) by

    G_m(alpha+z)=sum_(j>=n)g_j(n,m)z^j,

and the finite Gaussian-rational sum

    Z_m=-sum_(j=n)^K g_j(n,m)h0^(j+1)/(j+1).

Its previously proved remainder applies to every nonnegative m, not only the old O(n) adjustment:

    J_m=Z_m+r_m,
    |r_m|<=3*10^(n+1)*25^m*(5/6)^(K+1)/(K+2).

Choose one common truncation depth for the WHOLE enlarged interval:

    K=max(n, ceil(((n+1)log 10+m_hi log 25
             +2n log n+2n log 2+log 12)/log(6/5))).

Set

    Rstar=3*10^(n+1)*25^(m_hi)*(5/6)^(K+1)/(K+2).

Then, uniformly at every node,

    |r_m|<=Rstar<=(1/4)exp(-2n log n)2^(-2n).

In particular K=O_rho,C(n log n). More precisely its leading coefficient is (rho log 25+2)/log(6/5), with an O_rho,C(n log n/log log n) remainder. Every coefficient g_j retains the exact integer m. No adjustment is discarded from a phase.

At any eligible node the normalized logarithmic error obeys

    Flog/D=(-1)^(n+1)2^(n+2) Im(Z_m/U_m)+epsilon_m,
    |epsilon_m|<=2^(n+2)Rstar/|U_m|.

Using |U_m|>=2^(n/2), this is at most exp(-2n log n). The extension therefore requires a larger common K, not an extrapolation of a moving-saddle asymptotic.

## 2. The complete exponential residual on the enlarged range

The new main exponential estimate is used as an author input. With Lambda_m=2n+8m,

    |Eexp/D| < B_E(n,m),
    B_E(n,m)=3 Lambda_m^n exp(Lambda_m/(n+1))
                 /((n+1)(n!)^2 |U_m|).

It bounds the complete exponential tail for every m>=0 on U_m!=0. Consequently the old restriction rho<1/(2 log 7) is unnecessary here.

Uniformly in the enlarged interval,

    log B_E <= -n log n+n log log n+O_rho,C(n)-log|U_m|.

The adjustment changes log Lambda_m by O_rho,C(1/log log n), and its contribution after multiplication by n is already covered by the stated error. This statement concerns magnitudes only and does not treat the adjustment as phase-negligible.

For the complete quotient c_m, the exact decomposition is

    c_m-(e+pi)=Flog/D+Eexp/D.

No endpoint reconstruction constant belongs to this direct forcing quotient. Both complete residuals remain present.

## 3. Strengthening forcing selection to many consecutive pairs

Put k=n/4 and r=n/2. Choose a power of two h satisfying

    log n/(2 log log n)<h<=log n/log log n.

Eventually h divides k. Let m0=floor(rho n log n), and let a0=2k ceil(m0/(2k)). Take the following 8h complete eligible runs:

    I_l={a0+2kl+k,...,a0+2kl+2k-1},
    0<=l<8h.

Every integer in these runs is parity eligible, because its residue modulo 2k belongs to [k,2k-1]. All nodes lie in

    [m0,m0+4nh+n/2].

This is within the required O(n log n/log log n) adjustment. Unlike the original h-grid selection, these runs include consecutive INTEGER nodes, whose endpoint multipliers rotate by a quarter turn rather than being aliased by a large dyadic step.

Define the large-forcing threshold

    T=(2h)^r.

The main polynomial identity gives degree r and leading coefficient 4^r/r! for U(n,m). For any r+1 arguments separated by at least h, its leading-coefficient divided difference proves

    max |U(n,m_j)| >= T.

Indeed the reciprocal interpolation denominators have absolute sum at most 2^r/(h^r r!), while the leading coefficient is 4^r/r!.

It follows that within ANY one residue class modulo h there are at most r selected nodes with |U|<T. Otherwise r+1 such nodes contradict the preceding inequality. There are h residue classes, so among all the runs at most hr=nh/2 nodes are below threshold.

There are 8hk=2nh nodes in total and 8h(k-1)=2nh-8h edges joining consecutive integers within runs. Removing a below-threshold node destroys at most two such edges. Hence at least

    (2nh-8h)-2hr=h(n-8)

edges have BOTH endpoints satisfying |U|>=T. In particular such edges exist for all sufficiently large n.

This is a simultaneous large-forcing theorem for adjacent nodes, not a search result. It uses no assertion about logarithmic phases.

For every high node in these runs,

    log|U| >= (n/2)(log log n-log log log n)+O(n).

The main Cauchy upper bound, uniformly on the same interval, gives

    log|U| <= (n/2)log log n+O_rho(n).

Thus both endpoints of every surviving edge satisfy

    log|U|=(1/2+o(1))n log log n.

For explicit uniform bounds below, take m_lo=m0, m_hi=a0+16kh-1 and

    H_U=(4m_hi/n)^(n/2) exp(n+n sqrt(n/m_lo)).

Then |U_m|<=H_U on the block. This is an upper bound, not an asymptotic replacement for any denominator.

## 4. Exact adjacent-node rotation and its bounded remainder

The adjacent relation follows from A(alpha)=-2i:

    J_(m+1)=-2i J_m+E_m,
    E_m=integral_(c0)^alpha G_m(w)(A(w)+2i)dw.       (1)

This retains both real and imaginary parts of J_m. It shows precisely how consecutive nodes can avoid simultaneous imaginary-part cancellation, provided the correction is controlled relative to the actual complex contribution.

There is a new explicit absolute remainder bound. Parametrize w=(1+iy)/2, 0<=y<=1, and put x=1-y. Along this segment,

    V(w)=(1-y^2)/4,
    |A(w)|=(1+6y^2+y^4)/4.

The latter function is convex in y. Its endpoint chord gives

    |A(w)|<=2(1-7x/8)<=2exp(-7x/8).

Also |V(w)|<=x/2, |w|>=1/2, and |dw|=dy/2. Therefore, for m>0,

    integral_(c0)^alpha |G_m(w)| |dw|
        <= Mabs(n,m),
    Mabs(n,m)=2^m n!/(7m/8)^(n+1).

Since the derivative of A((1+iy)/2) with respect to y has modulus at most four, and A(alpha)=-2i,

    |A(w)+2i|<=4x.

Consequently

    |E_m|<=Rshift(n,m),
    Rshift=4*2^m*(n+1)!/(7m/8)^(n+2)
           =[32(n+1)/(7m)] Mabs(n,m).               (2)

This is uniform throughout the enlarged adjustment. It does NOT imply |E_m|=O(n/m)|J_m|: Mabs is an upper bound, and division by it cannot produce a relative estimate for the actual oscillatory integral.

Taking imaginary parts in (1) gives

    (Im J_m, Im J_(m+1)/2)
      =(Im J_m,-Re J_m)+(0,Im E_m/2).

The Euclidean triangle inequality therefore proves the adjacent lower bound

    max(|Im J_m|,|Im J_(m+1)|)
       >= (|J_m|-Rshift/2)_+/sqrt(2).               (3)

Here x_+=max(x,0). With the computable endpoint sum this implies

    max(|Im J_m|,|Im J_(m+1)|)
       >= (|Z_m|-Rstar-Rshift/2)_+/sqrt(2).         (4)

Equations (1)-(4) are signed adjacent-node information beyond an isolated enclosure. However, no positive lower bound for their right side is currently established. The small ratio n/m applies to an absolute integral majorant; it cannot be substituted for the missing phase-sensitive comparison. This branch stops at that exact loss.

On a high-high edge, a valid complete-error consequence of (4) is

    max_j |c_j-(e+pi)|
      >= 2^(n+2)/(sqrt(2) H_U)
           (|Z_m|-Rstar-Rshift/2)_+ - Bstar,

where j=m,m+1 and Bstar is defined below. A negative right side supplies no dominance conclusion.

## 5. A phase determinant lower bound for a high-forcing block

An alternative avoids assuming that the correction in (1) is relatively small. For a surviving high-high edge e=(m,m+1), define the Gaussian-rational numbers

    p0=Z_m/U_m, p1=Z_(m+1)/U_(m+1),
    S_e=|p0|^2+|p1|^2,
    W_e=Im(conjugate(p0)p1).

Both S_e and W_e are rational. They retain the two conjugate phases and the actual forcing normalizations. If S_e=0 set d_e=0; otherwise set

    d_e=|W_e|/sqrt(2S_e).

A direct determinant inequality gives

    max(|Im p0|,|Im p1|)>=d_e.                      (5)

Indeed W_e=Re(p0)Im(p1)-Re(p1)Im(p0), and Cauchy-Schwarz bounds its magnitude by sqrt(S_e) times the Euclidean norm of the two imaginary parts. No sign or phase assumption is used.

Use one common K from Section 1 on the whole block. Define

    eta_star=2^(n+2)Rstar/T,
    Lambda_hi=2n+8m_hi,
    Bstar=3 Lambda_hi^n exp(Lambda_hi/(n+1))
                       /((n+1)(n!)^2 T).

Then eta_star<=exp(-2n log n), and

    log Bstar <= -n log n
           +(n/2)log log n+(n/2)log log log n+O_rho(n).

The complete normalized error at either high node differs from

    (-1)^(n+1)2^(n+2)Im(Z_m/U_m)

by at most eta_star+Bstar. Thus (5) yields the new complete pair bound

    max(|c_m-(e+pi)|,|c_(m+1)-(e+pi)|)
       >= [2^(n+2)d_e-eta_star-Bstar]_+.            (6)

This is an unconditional inequality within the named author inputs. A positive lower margin, however, requires a quantitative phase determinant.

Let d_block be the maximum of d_e over the at least h(n-8) high-high edges established in Section 3. The set is nonempty and finite. Then

    max_(high nodes) |c_m-(e+pi)|
       >= [2^(n+2)d_block-eta_star-Bstar]_+.        (7)

This supplies a precise block noncancellation test. It is not a new name for the unknown error: d_block is built from explicit finite Gaussian-rational sums and integer U values, independently of e and pi. Its squared comparisons can be made with rational arithmetic. No such search has been executed.

If the bracket is positive, an explicit selection is available: choose the first maximizing edge, then its endpoint with the larger |Im(Z_m/U_m)|. That endpoint has large forcing and satisfies the same complete lower bound. The rule is conditional on the positive margin; it is not claimed to satisfy it on an unbounded sequence.

## 6. Why the original U maximizer does not settle the phase test

Large |U| constrains a closed-contour coefficient. The quantities W_e involve the open-contour upper endpoint contribution and its neighbor, after the two conjugate contributions are combined. The divided-difference identity for U provides no inequality for these determinants.

The initial h-grid also has a specific phase limitation. For sufficiently large n, h is a multiple of four, and the endpoint multiplier satisfies

    A(alpha)^h=(-2i)^h=2^h.

Thus a step h has a positive real endpoint multiplier. It supplies no automatic quarter-turn separation. The expanded selection block in Section 3 resolves this combinatorial issue by guaranteeing actual step-one high-high edges. It does not resolve the analytic correction E_m in (1).

The remaining obstruction can be stated in either of two exact ways:

    |Z_m| must dominate Rstar+Rshift/2 on some high edge;

or, more generally,

    2^(n+2)|W_e|/sqrt(2S_e)
          must dominate eta_star+Bstar on some high edge.

No uniform lower bound for either margin follows from the available endpoint enclosure, parity, or large-forcing selection. Near-collinearity of the two Gaussian-rational endpoint contributions can make W_e small. Simultaneously small imaginary parts are therefore not excluded. Conversely, no theorem that such cancellation occurs on all high edges is proved.

These statements concern the exact adjusted m. No equidistribution, phase stability, or negligible-congruence-adjustment premise is introduced.

## 7. Actual primitive denominator and the conditional consequence

Let q_m be the fully reduced positive denominator of c_m. On the eligible nodes the separate main dyadic author law gives

    v2(q_m)=3n/2+2m-s2(n)-s2(n+4m).

Here s2(n)=1. Put X_hi=n+4m_hi and define

    Qmin=2^(3n/2+2m0-2-floor(log2 X_hi)).

Since s2(a)<=1+floor(log2 a), all eligible block nodes satisfy q_m>=Qmin. Consequently (7) gives a bound for actual primitive forms:

    max_(high nodes) q_m |c_m-(e+pi)|
       >= Qmin [2^(n+2)d_block-eta_star-Bstar]_+.    (8)

No coefficient clearer or unreduced forcing denominator replaces q_m. Uniformly for this block,

    log Qmin=2rho log 2 n log n+O_rho(n).

For example, an unbounded-sequence lower bound

    2^(n+2)d_block >= exp(-sigma n log n+o(n log n)),
    sigma<min(1,2rho log 2),

would make both error remainders negligible and would prove divergence of selected primitive forms with simultaneous large forcing. This is a precise sufficient next phase lemma. It is not proved here.

If the main strengthened odd-denominator consequence is additionally accepted, it can improve the compulsory q rate. It is unnecessary for the displayed bound (8), which uses only the exact dyadic part.

## 8. Strongest proved outcome and stopping point

The enlarged adjustment does not invalidate the endpoint enclosure: a common depth O_rho(n log n) gives the stated uniform remainder. The new exponential author estimate also extends uniformly and remains factorially small for every fixed rho>0.

A stronger forcing-selection theorem now guarantees at least h(n-8) consecutive eligible pairs whose two U values both have logarithmic size (1/2+o(1))n log log n. Thus simultaneous forcing largeness at neighbors is no longer a combinatorial gap.

The new analytic statements are the exact adjacent rotation with bounded remainder (1)-(4), and the complete block lower bound (6)-(8) from the explicit conjugate-phase determinant. They are not a claim that the positive-part margin is nonzero. No unbounded logarithmic or complete-error lower bound has been established.

The remaining mathematical task is a quantitative lower bound for one of these phase margins on the high-forcing edges. Merely reducing the enclosure remainder further cannot supply that lower bound. The endpoint integral, the phase determinant, and the necessary threshold have all been specified explicitly; no unknown norm is substituted for dominance.

All earlier records are preserved. This note and LARGE_SELECTOR_BLOCK_NONCANCELLATION_REPORT.md require read-back before completion is reported.
