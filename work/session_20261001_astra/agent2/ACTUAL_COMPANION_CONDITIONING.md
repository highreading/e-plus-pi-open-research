> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Actual-family companion conditioning

Status: exact extraction from four retained records and a new cancellation-preserving integral identity. No uniform exponential bound for C, growing-degree sign theorem, or shrinking integer-form theorem is proved.

## Exact retained evidence

The application successfully executed extract_companion_conditioning.py. It reads only two_scalar_quotient_evidence.json and restricts the records to n=4,6,8,10. It constructs N from the saved primitive upper-triangular minors, without solving systems or constructing new approximation indices. The source bytes were unchanged during execution; hashes are recorded in companion_conditioning_extraction.json.

For each row the output retains the complete integer matrix, kappa_j=sum_i N_ij, signed row sum -kappa_j, absolute sum S_j, positive and negative masses, and all eligible ratios S_j/|kappa_j|. It also records cancelled mass S_j-|kappa_j|, cancelled and surviving fractions, and cancelled mass divided by the net magnitude. Zero denominators are explicitly ineligible rather than assigned a finite ratio.

The exact minima are:

| n | C | minimizing rows |
|---:|---|---|
|4|2009/1021|2|
|6|694288919809/604385055271|1|
|8|11033844156019887755931676121/9674460924431872076346352727|1|
|10|6411659808416170857457639908203852821320225992509/5652190600327147840051085004116244763851484500379|1|

All rows are eligible in these records. Every displayed minimum lies strictly between 1 and 2. These statements concern four exact finite records only. The output preserves their actual reduced q and projective separation Delta=1; neither is extrapolated.

For example, at n=4 the matrix is

N=[[0,-1510,1515],[1510,0,-494],[-1515,494,0]].

Its kappa vector is (-5,-1016,1021), its absolute row sums are (3025,2004,2009), and its eligible ratios are (605,501/254,2009/1021). Large cancellation in one row need not determine the minimum over rows.

## A rejected shortcut and a remaining row inequality

The proposed assertion that every row has nonincreasing absolute entries in increasing column order, omitting the diagonal, fails at the first retained index. At n=4, row zero has |N_02|=1515>1510=|N_01|. The exact witness is saved in conditioning_monotonicity_witness.json. This subroute is stopped.

A different sufficient inequality is available for row one. Write P=|N_10| and H=sum_{k>=2}|N_1k|. If H<P, the reverse triangle inequality gives

|kappa_1|>=P-H,
C<=S_1/|kappa_1|<=(P+H)/(P-H).

All four retained row-one tests have positive margin P-H. Their exact margins and ratios are in the extraction output. An all-index estimate H/P<=1-exp(-O(n)) would supply an exponential upper bound for C. No such actual-family estimate has been proved. In particular, the successful finite tests do not establish it.

PRIMITIVE_CONDITIONING_LIMITATION.md rules out obtaining that conclusion from rank, primitivity, decomposability, and opposite endpoint signs alone. Its abstract high row (m,m-1,m) gives C=2m-1 at fixed dimension. The present work does not use that invalid shortcut.

## A new actual-family identity avoiding C

Use the definitions of TWO_SCALAR_DETERMINANT_QUOTIENT.md, without repeating Agent 4's independent quotient audit. Let Bbar(x,y)=x^T N y be the primitive alternating form, with endpoint rows represented as column vectors when multiplied by N. Put

Uref=p_(n+1), A0=p_n(1), A1=p_(n+1)(1),
tau_U=T(Uref), tau_P=T(p_n),
Z0=-Bbar(evec,tau_U), Z1=-Bbar(evec,tau_P),
d=A1 Z1-A0 Z0,
K_tail=Bbar(tau_U,tau_P).

Assume 2<=b<=n and d!=0. Define the rational vector

beta=A0 tau_U-A1 tau_P,
lambda=N beta/d.

Because evec^T N beta=d, sum_j lambda_j=1. Furthermore Uhigh N=0. Indeed for any high row u and any y, det[Uhigh;u;y]=0, so u^T N=0; antisymmetry then gives N u=0 as well. Consequently

Uhigh lambda=0.

The full tail rows obey

arow=e A1 evec-tau_U,
crow=e A0 evec-tau_P,
beta=A1 crow-A0 arow.

Thus

sum_j lambda_j arow_j
 =arow^T N beta/d
 =A1 Bbar(arow,crow)/d.

The existing exact companion identity Bbar(arow,crow)=e d+K_tail gives

e+K_tail/d=(1/A1)sum_j lambda_j arow_j.                 (1)

This vector is formed from the actual endpoint combination, not from arbitrary abstract tail rows. Common high-row scaling cancels between N and d. No bound on individual entries of lambda is assumed.

## Rodrigues polynomial and the two exact boundary cancellations

Write

H_k(x)=k![z^k]exp(xz)(1-z+z^2/2)^k,
Pcal_k(x)=x^k H_k(x).

For k=n+1, the monic Rodrigues identity is

sum_l [t^l]p_k(t) x^(k+l)/(k+l)!=Pcal_k(x)/(2k)!.

Differentiating j times and evaluating at one yields

ell_j(Uref)=Pcal_k^(j)(1)/(2k)!.

Define

S_lambda(x)=sum_{j=0}^b lambda_j Pcal_k^(j)(x),
r=k-b=n+1-b>=1.

The first actual high row is ell(Uref), because b>=2. Therefore Uhigh lambda=0 proves S_lambda(1)=0. Also x^k divides Pcal_k, so x^r divides every derivative entering S_lambda. Since x and 1-x are relatively prime,

G_lambda(x)=S_lambda(x)/[x^r(1-x)]

is a rational polynomial, of degree at most n+b. These cancellations are exact properties of the actual high block; they do not follow merely from primitivity of its minors.

For an integer m>=0, direct integration gives

e integral_0^1 exp(-x)x^m/m! dx=e-sum_{a=0}^m 1/a!.

For a monomial t^l in Uref, the full tail in arow_j starts at factorial index n+l+1-j. Applying the last identity with m=n+l-j gives

arow_j=e/(2n+2)! integral_0^1 exp(-x)Pcal_(n+1)^(j+1)(x) dx.

All indices are nonnegative since j<=b<=n. This is an identity for complete factorial tails, not a first-term approximation. Summing against lambda and using (1) gives

e+K_tail/d=e/[A1(2n+2)!] integral_0^1 exp(-x)S_lambda'(x) dx.

Integration by parts has zero boundary contribution: S_lambda(1)=0 by the actual high row and S_lambda(0)=0 by r>=1. Hence the new exact formula is

e+K_tail/d
 =e/[A1(2n+2)!] integral_0^1 exp(-x)x^r(1-x)G_lambda(x) dx.       (2)

The signs and factorial index in this formula are important. The integral initially contains S_lambda', and the boundary cancellations convert it into the integral of S_lambda. Omitting that derivative would miss the factorial-tail starting index.

In particular, if H_lambda is any rigorous upper bound for |G_lambda| on [0,1],

|e+K_tail/d|
 <=e H_lambda/[A1(2n+2)!(r+1)(r+2)].                    (3)

This follows from exp(-x)<=1 and the elementary integral of x^r(1-x). One can take H_lambda=max_i |g_i| where g_i are the exact Bernstein coefficients of G_lambda in any degree at least its degree: the Bernstein basis is nonnegative and sums to one. No common sign of those coefficients is asserted. Equation (2) also permits direct integration of the combined polynomial to retain further cancellation.

The useful new lemma is the actual-family cancellation identity (2), together with (3). It avoids the row-sum conditioning quantity C. It does not make conditioning disappear: lambda and therefore G_lambda contain the actual denominator d. No uniform estimate on H_lambda relative to that normalization is proved here. Merely bounding its terms separately can reintroduce the losses that the combined polynomial was intended to retain.

## Relation to the reviewed derivative structure

ADDITIONAL_GROWING_CONTENT.md and agent4/ADDITIONAL_GROWING_REVIEW.md provide exact derivative recurrences for Pcal_k and E_(k,j)=Pcal_k^(j)(1), together with a four-starting-column representation of the high block. These are actual polynomial identities and can be used to construct S_lambda and G_lambda algebraically. Their signed partition sums do not provide a lower bound for |d| or |kappa_j| merely from the sizes of their individual terms.

If the reviewed transformation is used, R=W T with det T=1 requires

det[R;x;y]=det[W;x T^(-1);y T^(-1)].

The appended evec, tau_U, tau_P and any full tail rows must all undergo the same transformation. The conditioning quantity based on evec and coordinate rows is not invariant if that change is ignored. No column transformation is performed in this continuation; the extraction and formula (2) stay in the original columns.

The reviewed factorial and row/minor contents are common scalars already removed in N. They are not added as fresh gains to C or to the companion. No product divisor or sign is inferred from partition summands.

## Actual reduced denominator, separation, and nonvanishing

Keep

Delta=|d|/(A0|Z0|+A1|Z1|)>0,
q=den(-r_pi-r_e), r_e=-K_tail/d,
r_pi=(w1 Z1-w0 Z0)/d.

This q is the fully reduced endpoint denominator, including the final endpoint cancellation. In particular, the denominator of d or a separate companion denominator is not substituted for q.

Combining the previously established principal bound |D_W/D_V|<=epsilon_n/Delta with (3), and using T/D_V=-(e+K_tail/d), gives

|L_int|<=q[epsilon_n/Delta+B_comp],
B_comp=e H_lambda/[A1(2n+2)!(r+1)(r+2)].                (4)

A sufficient condition is that the right side tends to zero on an unbounded set with D_V!=0 and D_W+T!=0 at every selected index. Neither a uniform bound proving this decay nor complete-remainder nonvanishing is obtained here. Reference sign success in four records does not prove an unbounded sign theorem. Individual irrationality of e implies the companion e+K_tail/d is nonzero, but does not prevent cancellation with the principal pi error.

No exponential bound for C is claimed. The all-index row-one domination gap remains open; alternatively, formula (2) asks for a useful direct estimate of the actual combined polynomial G_lambda. The latter is a new exact representation and quantitative norm inequality, not an established uniform error rate.

## Files and scope

The new artifacts are ACTUAL_COMPANION_CONDITIONING.md, ACTUAL_COMPANION_CONDITIONING_REPORT.md, extract_companion_conditioning.py, companion_conditioning_extraction.json, and conditioning_monotonicity_witness.json. The extraction script and exact output require read-back verification. The source certificate and prior corrected records are preserved.

No canonical system was solved, no approximation index was added, and no prime scan, networking, installation, external path, or other agent's file modification was used. The exact extraction is finite evidence; the integral lemma is proved by the actual Rodrigues and high-row identities above.
