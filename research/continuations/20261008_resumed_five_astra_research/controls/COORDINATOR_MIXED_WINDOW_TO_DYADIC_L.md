> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Complete mixed-return independence through the dyadic size L

Coordinator derivation, 9 October 2026. NEW; DIFFERENT review PENDING.
This is a separate extension of the already admitted linear-window note.
That admitted source and its request hashes remain unchanged. The parent
reads FULL A4turn23, including the independently passed full mixed kernel,
both-parity first transition, actual relative odd prefactors, original
subfamily, and NEW two-return proof. FULL A2turn14 terminal theta-sector
cancellation remains distinct: the eta ranks below do not contradict it.

## 1. Overlap and primary-literature scope

Before this derivation, current/prior/Desktop English MD/TEX searches recover
the older source-rank notes, first-return obstruction, weighted-stack warnings,
the newly admitted h<=rho-1 parent theorem, and A4turn23's two-return theorem.
No earlier proof of the larger coupled rank up to q=L is found in the scoped
mixed-pole/exponent search. A broad q<=L query is not used as evidence of
exhaustive novelty. Primary arXiv/DLMF queries on mixed Cauchy finite-difference
rank recover ordinary binomial generating/Pascal identities, not this actual
coupled rank theorem. Those standard identities are REUSE; no unread external
theorem is imported. DLMF26.3 is checked for the binomial identities only:
https://dlmf.nist.gov/26.3. The new argument is the finite cleared-degree
cutoff and elimination of all higher mixed pole orders in the original array.

## 2. Original finite domain and statement

Keep ORIGINAL d=9^(18+32u)-1. On the first2L ORIGINAL return columns assume

    L dyadic, d=2L+rho, rho even>=4,
    p>=rho+1, rho+p<=L,
    1<=h, q=p+h<=L.                                (1)

Use the actual atom-source spaces R_p and R_(p+1), with dimensions p-1,p.
Their already passed rectangular cutoff includes rho+p+1<=L when p is ODD.
Put V_z=U_p(z,bullet). The proposed stronger theorem is

    rank [R_(p+1);V_0;...;V_(h-1)] = p+h=q.         (2)

The auxiliary p is the actual Cauchy/product count. Original d and all
physical boundaries are retained. All generating series and unit convolutions
below act on the normalized binary parity array, not on the integer pencil.

## 3. Reuse: both higher-row formulas and the small-pole range

In F4, omega^2+omega+1=0, set a=1+omega Y, b=1+omega^2 Y.
Coefficientwise trace fixes Y. The FULL mixed kernel, including its ODD
derivative, gives

    p ODD:
    V_(2v)=Tr(omega^(2p+2v)*b^(p-1)/a^(p+2v)),
    V_(2v+1)=Tr(omega^(2p+2v)*b^(p-1)*Y(1+Y)
                                               /a^(p+2v+3));

    p EVEN:
    V_(2v)=Tr(omega^(2p+2v+1)*b^(p+1)/a^(p+2v+2)),
    V_(2v+1)=Tr(omega^(2p+2v)*b^p/a^(p+2v+2)).      (3)

The admitted small-window proof excludes every nonzero mixed combination
modulo R_(p+1) for h<=rho-1, and its EVEN proof explicitly extends to h<=rho.
It compares the lowest A=a^2 level in the unique decomposition F4[Y]=
F4[A]+Y F4[A]. The source phase ratio is omega^(-L), outside F2. For ODD p,
the paired even/preceding-odd candidates have equal Y coefficients; if both
bits are1 their Y parts cancel, but a+omega Y(1+Y)=b^2 leaves the same
obstructed constant phase. For EVEN p the even and odd candidates have,
respectively, an obstructed Y coefficient and an obstructed constant.
The NEW extension below pays the terms whose a exponents became negative.
The small-window result still awaits full DIFFERENT A2turn15 review.

## 4. One finite degree cutoff for every larger combination

Apply the same C_d=(ab)^d convolution on the first2L coordinates. It is
invertible because its constant is1. At this precision a^(2L)=b^(2L)=1.
Every source combination in R_(p+1) becomes

    Tr(b^(2rho)*Q/a^p), deg Q<=p-1.                (4)

For EVEN p, C_d V_(2v), C_d V_(2v+1) have a-pole order

    n_(2v)=n_(2v+1)=p+2v+2-rho

and respective numerators omega^(2p+2v+1)b^(rho+p+1),
omega^(2p+2v)b^(rho+p).
For ODD p their a-pole orders are

    n_(2v)=p+2v-rho,
    n_(2v+1)=p+2v+3-rho

and numerators omega^(2p+2v)b^(rho+p-1),
omega^(2p+2v)b^(rho+p-1)Y(1+Y).
All these pole orders are positive under(1). Negative exponents have been
kept as actual denominators, not reduced illegally as polynomial powers.

Let M be the maximum of p and these pole orders for 0<=z<h. Write an
alleged zero trace combination as Tr(N/a^M). Its source numerator is
b^(2rho)Q a^(M-p); the mixed numerators are the just displayed numerators
multiplied by a^(M-n_z). Therefore

    deg N<=M+2rho-1,
    M+rho=max(p+rho,q+(q mod2))<=L.                (5)

To check the second identity, for EVEN p both rows of a pair have pole
p+2v+2-rho: the last even row gives q+1-rho, while the last odd gives
q-rho. For ODD p the last odd row has pole q+1-rho, while the last even
has pole q-rho. These are exactly the two q parities in(5).
L is EVEN and q<=L, so an ODD q automatically pays the extra1.

Clear BOTH unit denominators a^M and b^M. The finite zero congruence is

    b^M N+a^M N^sigma=0 modY^(2L).

Its degree is at most2M+2rho-1<=2L-1. It is consequently an EXACT
polynomial identity. At the root Y=omega^2 of a, b=omega^2 is a unit;
N/a^M has no pole there. The conjugate term is regular at that root.
Thus all negative Laurent coefficients at this root must vanish.
This statement alone need not force an arbitrary polynomial part to zero;
the following high-pole elimination and small-window proof do that.

## 5. EVEN p: each new pair has an uncancellable highest pole

The old small-window proof covers z<rho. For a new pair z=2v>=rho,
its two rows have common pole n=p+2v+2-rho>=p+2. With binary bits e,o,
their rational sum at the a root is exactly

    omega^(2p+2v)*b^(rho+p)*(e*omega*b+o)/a^n.      (6)

At the root, omega*b=1. If exactly one bit is1, (6) has a nonzero pole
of order n. If both bits are1, use omega*b+1=omega^2 a: it has a nonzero
pole of order n-1. All preceding pairs have pole at most n-2, and every
source or old small-window row has pole at most p. So neither case can
be cancelled. A last unpaired even row has the same unit highest pole.
Start at the highest present pair and descend. All bits with z>=rho
must be0. The remaining small-window combination is excluded by the
EVEN proof recalled in Section3. This establishes(2) at EVEN p.

## 6. ODD p: the one critical equal-pole row is also excluded

The old proof covers z<rho-1. The new row z=rho-1 is ODD and has pole
p+1. The row z=rho is EVEN and has pole p. All later rows have distinct
orders above p: the odd rows give p+3,p+5,...; the even rows give p+2,p+4,... .
At Y=omega^2, Y(1+Y)=1 and b is a unit. Thus all numerators at these
distinct higher poles are units. From the highest order downwards, every
bit with n_z>p must be0. No source or older row can cancel such a pole.

Only the critical EVEN row z=rho can remain in addition to the old range.
Its candidate numerator at common denominator a^p is

    Q_critical=omega^(2p+rho)*b^(p-rho-1).         (7)

Every older mixed candidate is divisible by a. The source numerator at
ODD p is

    Q=a*Q_old+c_new*omega^(2d+p+1), c_new in F2.   (8)

All remaining mixed candidates, including(7), have degree<p. The exact
root identity therefore forces Q to equal their sum, as in the small
window proof: a^p divides b^(2rho) times the difference, and b is a unit
at the root. Evaluate this equality at a=0. The ratio of(7)'s root value
to the allowed constant phase in(8) is

    omega^(4p-rho-2-(2d+p+1))
    =omega^(3p-rho-2d-3)=omega^(-L).              (9)

Here d=2L+rho and exponents are taken modulo3. The ratio is outside F2
because dyadic L is nonzero modulo3. Hence the critical bit is0 and
c_new=0. The remaining old combination is excluded by Section3.
This proves(2) at ODD p, including the critical row omitted by a simple
distinct-pole argument.

## 7. Complete compounds and every first-crossing tie through q=L

Let p be the actual minimizing count: s=min{r>=2:D_r>=L_d}, p=s-1.
Retain F_q(p), the full factorial and atom exclusions, all paid integer
source divisors and the exact mixed Cauchy-Newton normalization. FULL
A4turn23 derives the actual general leading odd prefactor, including
gamma, Cauchy denominators, complementary K_d determinant, atom and
every odd factorial. Its formula is valid for general bottom count h.
Thus the minimum sector has full leading stack

    det[R_p;V_0;...;V_(h-1)]                      (10)

with all actual prefactors retained before binary reduction. Its rank is
q-1 by(2), so some q-1 ORIGINAL returns attain F_q(p) in a strict crossing.

At D_(p+1)=L_d, precisely the p and p+1 product sectors tie. Pascal gives
U_(p+1)(z)=V_z+V_(z+1) at both parities. Put W'_z=V_z+V_(z+1), and use
R_(p+1)=R_p+span(v_new). Their complete sum is

    det[R_p;V_(h-1)+v_new;W'_0;...;W'_(h-2)].     (11)

All relative normalized odd prefactors reduce to1, rather than being
silently assigned the same integer value. The change from V rows to
V_(h-1),W'_0,...,W'_(h-2) has determinant1 over F2. By(2), v_new is outside
R_p+span(V), so(11) has rank q-1. This pays ALL h and both parities,
not just an isolated tied summand. Full DIFFERENT review of this larger
argument is pending. No one nested corrected elimination flag is asserted.

## 8. Same infinite original subfamily and quantitative window

On the already passed interval (9/8)2^a<k<(7/6)2^a, L=2^(a-1), the same
original indices have L/4-1<rho<L/3-1 and p=d/4+O(log d). The hypotheses
p>=rho+1 and p+rho<=L hold with linear slack. For EVERY q<=L,

    alpha-2-4q>=2rho-s_2(d)-2>0,
    d-2q+1-2m>=rho+1-2m>0.                       (12)

These pay ALL factorial patterns and atom-in-W patterns before the leading
minimum is evaluated. The infinite original family follows from the already
proved irrational rotation, with no parity/equality distribution filter.
All physical bottom jets use orders<=q-1<=L-1, actual returns r<2L<=d,
and their successor moment is within3d+1. No physical terminal is enlarged.

The proposed attaining common-cofactor window is now

    q<=L, with L/d in (3/7,4/9)+O(1/d),

strictly beyond the old q<=p+rho-1 window. Integer Cramer row numerators
may use these actual cofactors retaining their odd mu, both full borders,
and the existing exact common scalar transfer. This gives no upper bound
for the residual joint coefficient gcd. At full terminal size the theta
leading cancellation of A2turn14, higher-excess terms, other odd primes,
least clearers and the ALL-prime primitive whole error remain OPEN.
No producer retirement or rationality decision for e+pi follows.
