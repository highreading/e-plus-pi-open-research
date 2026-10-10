> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A linear mixed-return window, including every first-transition tie

Coordinator derivation, 9 October 2026. NEW; DIFFERENT review PENDING.
This extends the earlier BOTH-parity first-return note. It reuses the
full general mixed kernel, whose ODD derivative is retained. FULL
A2turn14 was read before this note: its multi-column mixed residue,
paired coefficient transformation and FULL-RANK leading cancellation
are distinct NEW results with favorable parent review and DIFFERENT
review pending. The proposed lower-rank window below does not undo
that later full-rank cancellation.

Before writing this derivation, scoped current/prior/Desktop English
MD/TEX searches find the first-return and mixed-kernel notes and the
older weighted-stack warnings; no proved multi-return independence
modulo R_(p+1) or full equality-tie sum is recovered. A2turn14 proves
a bottom-only mixed determinant and a later full-rank theta-kernel
cancellation, not this finite U_d/U_p coupled rank. Primary web queries
show no matching original theorem in the inspected result scope. All
binomial, finite-field root and irrational-rotation identities are
REUSE; no unread external theorem or exhaustive novelty claim is used.

## 1. Original range and the stronger rank statement

Keep ORIGINAL d=9^(18+32u)-1. On the SAME original return columns
0<=r<2L<=d, assume

    L dyadic, d=2L+rho, rho even>=4,
    p>=rho+1, rho+p<=L, 1<=h<=rho-1.                 (1)

Use the actual minimizing atom-source spaces R_p and R_(p+1) from
the earlier note. Let V_z=U_p(z,bullet), 0<=z<h. The NEW rank claim is

    rank [R_(p+1);V_0;...;V_(h-1)] = p+h.            (2)

Thus ALL h return rows are independent modulo the larger source space,
not just pairwise independent modulo R_p. This also pays the complete
tie sum below. The parameter p is an ACTUAL Cauchy/product count;
the research index d is unchanged. Every finite convolution is an
operation on the normalized binary rank matrix only.

The passed rectangular criterion gives dim R_(p+1)=p and dim R_p=p-1.
For ODD p, rho+p odd<=L implies rho+p+1<=L, paying the needed extra
top contact row. These parity cutoffs are not suppressed.

## 2. ALL higher mixed rows at both parities

Put a=1+omega Y, b=1+omega^2Y, omega^2+omega+1=0. Tr is coefficientwise
trace with variables fixed. Expanding the FULL general mixed kernel,
including the odd derivative, gives the following exact formal series.

If p is ODD,

    U_p(2v,Y)=Tr(omega^(2p+2v)*b^(p-1)/a^(p+2v)),
    U_p(2v+1,Y)=Tr(omega^(2p+2v)*b^(p-1)*Y(1+Y)
                                      /a^(p+2v+3)). (3)

If p is EVEN,

    U_p(2v,Y)=Tr(omega^(2p+2v+1)*b^(p+1)/a^(p+2v+2)),
    U_p(2v+1,Y)=Tr(omega^(2p+2v)*b^p/a^(p+2v+2)).     (4)

For a direct derivation at odd p, the coefficient of X^(2v) in the
two terms of the kernel has common denominator a^(p+2v+2) and
numerator omega^(2p+2v-1)b^(p-1)*(omega^2 b^2+1).
The identity omega^2 b^2+1=omega*a^2 gives the first line of(3).
At X^(2v+1), the common numerator is
omega^(2p+2v)b^(p-1)*(ab+1). Since ab+1=Y(1+Y), the second line follows.
At even p the derivative vanishes and the two parity coefficients
of the squared denominator give(4). All denominators have constant1.
At z=0 these agree with the earlier BOTH-parity S_p formulas.

The exact binomial recurrence, independently of the generating law, is

    U_(p+1)(z,r)=U_p(z,r)+U_p(z+1,r) mod2.             (5)

It follows by Pascal on binom(p+1,t), changing t to t+1 in the second
sum. The relation uses the full direct binomial definition and hence
holds at odd as well as even p. No vanished odd derivative is assumed.

## 3. Finite root reduction for an arbitrary row combination

Apply the SAME unit binary column convolution C_d=(ab)^d on the
first2L return columns. As before a^(2L)=b^(2L)=1 modY^(2L).
A row from R_(p+1) has form

    Tr(b^(2rho)*Q/a^p), deg Q<=p-1.                  (6)

If a binary combination of the V_z were in this source space,
clearing BOTH denominators leads to

    b^p N+a^p N^sigma=0 modY^(2L),
    N=b^(2rho)*(Q+Q_mix),                            (7)

where Q_mix is the corresponding binary sum of the following
candidate numerators, obtained DIRECTLY from(3)--(4).

At ODD p,

    Q_(2v)=omega^(2p+2v)*a^(rho-2v)*b^(p-rho-1),
    Q_(2v+1)=omega^(2p+2v)*a^(rho-2v-3)
                                *b^(p-rho-1)*Y(1+Y). (8)

At EVEN p,

    Q_(2v)=omega^(2p+2v+1)*a^(rho-2v-2)*b^(p-rho+1),
    Q_(2v+1)=omega^(2p+2v)*a^(rho-2v-2)*b^(p-rho).    (9)

All a and b exponents in(8)--(9) are nonnegative under(1).
Every Q_z has degree<=p-1. Thus the degree in(7) is at most
2rho+2p-1<=2L-1, so its congruence is an EXACT polynomial identity.
At the root of a, b is a unit; hence a^p divides Q+Q_mix.
Since the latter has degree<p, it is zero. Therefore Q=Q_mix is the
ONLY possible numerator. This includes linear combinations of all
the mixed rows, not just individual-row tests.

## 4. ODD p: two independent coefficient obstructions per pair

Write p=2m_c+1. The source numerator in(6) is

    Q=a*Q_old+c_new*omega^(2d+p+1), c_new in F2,
    Q_old=omega^(2d)*sum_(l=0)^(m_c-1)
             omega^(2l)*(c_odd,l+c_even,l*omega*b)
                                    a^(2(m_c-l-1)).  (10)

Every candidate in(8) is divisible by a under h<=rho-1: the smallest
a exponent is2 for an even z and1 for an odd z. Hence Q_mix at the
root of a is zero, forcing c_new=0. Divide the candidates by a and
compare them with Q_old.

Put A=a^2, B=b^2=omega*(1+omega A), and t=(p-rho-1)/2=m_c-rho/2.
The even z=2v candidate becomes

    E_v=omega^(2p+2v+t)*a*A^(rho/2-v-1)*(1+omega A)^t.

For v>=1, pair it with the preceding odd z=2v-1 candidate

    O_(v-1)=omega^(2p+2v-2+t)
                   *A^(rho/2-v-1)*(1+omega A)^t*Y(1+Y).

Both have lowest A degree s=rho/2-v-1 in their Y coefficient.
Their Y*A^s coefficients are EQUAL because the phases differ by3.
The allowed coefficient from(10), at l=m_c-s-1=t+v, is
omega^(2d+2l)*c_even,l. The ratio of either nonzero candidate
coefficient to this phase is

    omega^(2p+1-2d-t)=omega^(rho/2-2d)=omega^(-L),    (11)

which is outside F2. If precisely one of the two binary candidate
coefficients is1, membership in(10) is impossible.

If BOTH are1, their Y terms cancel. But a+omega*Y(1+Y)=b^2 gives

    E_v+O_(v-1)=omega^(2p+2v+t+1)
                  *A^s*(1+omega A)^(t+1).

Its A^s coefficient has the SAME ratio(11) to the allowed odd-source
phase omega^(2d+2l). The zero Y coefficient forces c_even,l=0, so the
remaining constant coefficient also contradicts c_odd,l in F2.

The isolated first row z=0 has the earlier nonzero Y coefficient with
ratio(11). For an arbitrary nonzero mixed combination, take its
LOWEST A degree: only the indicated pair or the isolated z0 can
contribute there. Candidates at greater A degree contribute neither
the Y nor constant coefficient there. The two cases just proved
exclude every nonzero combination. This proves(2) at ODD p.

The decomposition Q(Y)=Q_even(A)+Y Q_odd(A) is unique: A is an affine
linear polynomial in Y^2. Thus comparison of these coefficients is
an exact polynomial-basis argument, not a lowest-Y-degree guess.

## 5. EVEN p: the full larger source space still cannot absorb a pair

Write p=2m_c. The numerator in(6) is the full paired space

    Q=omega^(2d)*sum_(l=0)^(m_c-1)
        omega^(2l)*(c_odd,l+c_even,l*omega*b)
                                      a^(p-2l-2).   (12)

Set t=(p-rho)/2=m_c-rho/2 and s=rho/2-v-1. The two candidates(9) are

    E_v=omega^(2p+2v+1+t)*b*A^s*(1+omega A)^t,
    O_v=omega^(2p+2v+t)*A^s*(1+omega A)^t.           (13)

Only E_v has a Y*A^s coefficient. Its phase, after the omega^2 from b,
is omega^(2p+2v+t). At l=m_c-s-1=t+v, the ratio to the allowed source
phase is

    omega^(2p-2d-t)=omega^(rho/2-2d)=omega^(-L).     (14)

It is not in F2. Hence in the lowest-A-degree pair a nonzero E_v
coefficient is impossible. With E_v absent, a nonzero O_v has an A^s
coefficient with the SAME phase and ratio(14), so is also impossible.
Other pairs have greater A degree. This excludes every nonzero mixed
combination and proves(2) at EVEN p. A final unpaired even row is
excluded by the same Y coefficient. All relevant l lie between0 and
m_c-1 under(1). The stronger even bound h<=rho also follows, but the
uniform bound rho-1 is sufficient for the application.

## 6. COMPLETE mixed leading minors, including equality ties

Reuse S_n,T_p,D_p,F_q(p) and their increasing digit formula from the
previous mixed-cost note. Let s=min{r>=2:D_r>=L_d}, p=s-1. For a selected
q=p+h common-column minor containing the atom, retain

    q<=d, alpha-2>4q, d-2q+1-2m>0.                  (15)

Every factorial correction and atom-in-W pattern is then above the
minimum. Product counts are uniquely p if D_(p+1)>L_d, or exactly
p and p+1 if equality holds. All other counts have extra binary depth.

At the minimum the N_d source/forcing minor is uniquely T_p in the
p sector, or T_(p+1) in the other sector. The full complementary K_d,
normalized Cauchy factors, gamma and atom factors are odd and retained
before reduction. The multi-column mixed Newton identity supplies
the bottom rows V_0,...,V_(h-1), with the full2^j*j! payment. The sum
over WHICH selected returns are bottom corrections is consequently
the Laplace determinant

    det[R_p;V_0;...;V_(h-1)].                       (16)

This is a COMPLETE leading-compound assertion requiring independent
audit of its relative scalar normalizations, not an attainment inferred
merely from the cost minimum. The stronger rank(2) implies rank(16)
is q-1, so some q-1 ORIGINAL returns attain F_q(p) at strict crossing.

At equality D_(p+1)=L_d the other minimum sector has bottom rows

    U_(p+1)(z)=V_z+V_(z+1), 0<=z<h-1,

by(5), and top source space R_(p+1)=R_p+span(v_new), where
v_new=U_d(p-1)+U_d(p) for odd p and v_new=U_d(p-1) for even p.
Every full normalized relative scalar is ONE in F2. Write
W'_z=V_z+V_(z+1). The determinant-one binary change of the V rows
to V_(h-1),W'_0,...,W'_(h-2) gives the SUM of the two minimum sectors:

    det[R_p;V_(h-1)+v_new;W'_0;...;W'_(h-2)].        (17)

For h=1 this is exactly the earlier first-transition tie formula.
It is not the determinant of either summand considered separately.

Equation(2) proves v_new lies outside R_p+span(V_0,...,V_(h-1)).
In any relation among(17), a nonzero coefficient of V_(h-1)+v_new
would contradict that exclusion. If that coefficient is zero, the
remaining W' rows are independent modulo R_p because the V rows
are independent there. Thus(17) has rank q-1. Some ORIGINAL return
columns attain the tied full value F_q(p)=F_q(p+1). Cancellation
of the two sectors is explicitly paid for EVERY h in(1).

## 7. A longer window on the SAME infinite original subfamily

Use the independently passed original interval
(9/8)2^a<k<(7/6)2^a, a=floor(log2 k), L=2^(a-1).
Then L/4-1<rho<L/3-1, rho divisible by16, and p=d/4+O(log d).
All inequalities in(1) hold with linear slack at sufficiently large
indices. For EVERY1<=h<=rho-1, q=p+h is below d/2 with linear slack,
so(15) holds. The full original index/real constraints are unchanged.

The proposed complete attaining window now reaches

    q_max=p+rho-1=d/4+rho+O(log d),

which is strictly greater than d/4 by a fixed positive fraction of d
on this interval. It covers BOTH p parities and ALL equality ties.
The established irrational-rotation proof gives infinitely many SAME
original indices; no new digit or equality distribution conjecture
is used. Each q obtains ORIGINAL-column cofactor existence. This
does not claim one nested complete elimination flag beyond the old
window, or retain the old division-by2 algorithm unchanged.

## 8. Remaining scope

The new finite stack-rank argument and full tie expansion are PENDING
DIFFERENT audit, as are the general mixed kernel and any new relative
multi-sector normalization not already covered by A4turn22. There is
no new original-sized computation or need to rerun the closed first-
return auxiliary receipt. A new bounded check of higher rows would
verify only that finite scope.

A2turn14's later FULL-RANK linear cancellation remains valid at its
stated reviewed scope: its bottom count is d+2-p, well outside the
present h<=rho-1 window, and its theta sources/coefficient border
are distinct. The present lower-rank eta-source theorem does not
bound the excess of that terminal pair. BOTH coefficient borders,
other odd-prime depths, least clearer, ALL-prime G, actual primitive
q and whole nonzero error remain OPEN. No producer retirement or
decision about rationality of e+pi follows here.
