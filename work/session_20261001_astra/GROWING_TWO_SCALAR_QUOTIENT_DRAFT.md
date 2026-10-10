> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A two-scalar route to the actual determinant quotient

Status: main-agent algebraic draft, awaiting independent checking and investigation of its sign hypothesis. It is intended to avoid separate products of high-row majorants. No uniform sign, denominator-growth, or shrinking theorem is claimed.

## 1. The same high rows in one alternating form

Let 1<=b<=n. Retain the actual monic high block Uhigh and columns ell_0,...,ell_b. For endpoint rows x,y define

    Bform(x,y)=det[Uhigh;x;y],
    evec=(1,...,1),
    Fcal(P)=Bform(evec,(ell_j(P))_(j=0)^b).

The factorial functionals also act on P/(1-t) for polynomial P by absolutely convergent factorial sums. All original factorial arguments remain nonnegative in the stated domain.

Write

    Uref=p_(n+1),
    A0=p_n(1)>0, A1=p_(n+1)(1)>0,
    v0=L(p_n/(1-t)), v1=L(p_(n+1)/(1-t)),
    h=h_n!=0,
    arow=(ell_j(Uref/(1-t)))_j,
    crow=(ell_j(p_n/(1-t)))_j,
    z0=Bform(evec,arow), z1=Bform(evec,crow).

Both z0 and z1 are rational. Indeed

    ell_j(P/(1-t))=exp(1)P(1)-T_j(P),

and Bform(evec,evec)=0. Hence

    z0=-Bform(evec,T(Uref)),
    z1=-Bform(evec,T(p_n)).

These are actual determinant contractions, not independently bounded surrogates.

## 2. Exact endpoint and principal-remainder identities

The scalar-preserving reference formulas give

    V=(A1 p_n-A0 Uref)/(h(1-t)),
    W=(v0 Uref-v1 p_n)/(h(1-t)).

Linearity therefore yields

    D_V=(A1 z1-A0 z0)/h,
    D_W=(v0 z0-v1 z1)/h.

If z0!=0 and eta=z1/z0, then exactly

    D_W/D_V=-(v0/A0)(1-alpha eta)/(1-bref eta),
    alpha=v1/v0, bref=A1/A0,

provided D_V!=0. This is an actual quotient identity. It does not divide upper bounds.

It reduces one part of the analytic problem to controlling a single real rational projective coordinate eta. The pole is eta=1/bref. The cases z0=0 must be handled separately rather than omitted.

## 3. A concrete sufficient sign condition

The reference analysis supplies

    alpha<0, |alpha|<1/6, bref>=1/2,
    epsilon_n=|v0|/A0.

Assume

    z0*z1<=0 and (z0,z1)!=(0,0).

Then

    |A1 z1-A0 z0|=A0|z0|+A1|z1|>0,

so D_V is nonzero. Put c=-alpha, with 0<c<bref. The triangle inequality gives

    |v0 z0-v1 z1|
      =|v0| |z0+c z1|
      <=|v0|(|z0|+c|z1|)
      <=epsilon_n(A0|z0|+A1|z1|).

Consequently

    |D_W/D_V|<=epsilon_n.

This includes z0=0 or z1=0. It is a conditional lemma about actual determinant contractions. The sign condition has not been established on an unbounded growing-degree set. It is weaker than a common sign assertion for every Bernstein coefficient of every kernel summand.

If both z0 and z1 vanish, this argument supplies no endpoint. If their product is positive, it supplies no exclusion; an interval estimate keeping eta away from the pole could still be useful.

## 4. The companion determinant remains explicit

Let vrow and wrow be the actual functional rows of V and W. In terms of arow,crow,

    vrow=(-A0 arow+A1 crow)/h,
    wrow=(v0 arow-v1 crow)/h.

The reference Wronskian satisfies

    A1 v0-A0 v1=h.

For example, this follows by multiplying the exact projection-remainder formula by 1-t and evaluating at t=1: W=1/(1-t)-H has residue factor one there, with H polynomial.

Bilinearity now gives

    T=Bform(vrow,wrow)=-Bform(arow,crow)/h.

Thus under the sign condition above,

    |(D_W+T)/D_V|
      <=epsilon_n+|Bform(arow,crow)|/(|h| |D_V|).

The second term must be controlled in the same normalization. Neither a small separate bound for T nor a nonzero D_W establishes full-remainder nonvanishing. No such companion quotient estimate is proved here.

## 5. Arithmetic and research target

All common high-row factors cancel from z1/z0 and from the displayed determinant ratios. The previously reviewed primitive-minor arithmetic can express these contractions without identifying a coefficient clearer with q.

A useful next task is to check these identities and their signs, test the sign condition using only the existing frozen controls, and find an actual-family recurrence or inequality for z0,z1. The companion ratio and the fully reduced q must remain explicit.

Even if the sign condition is proved, an irrationality proof would still need adequate actual denominator control, a complete-remainder estimate, and nonzero evaluated forms on the same unbounded set. No fixed-b determinant limit may be substituted into the growing regime.
