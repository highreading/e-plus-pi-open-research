> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# M25. One extra column: the complete integer coefficient lattice

Author algebraic theorem with six new exact receipts. This target concerns width 2k+1, whereas M24 fixes width 2k. It does not establish a favorable infinite approximation sequence or decide the irrationality of e+pi.

## Fresh archive and primary-paper gate

Archive queries for exterior matching-kernel modules, one-extra-column paired constructions, and the full coefficient-pair Smith lattice did not find this specialization. Generic free-parameter Hermite–Pade approximation, primitive kernel completion and integer lattice normal forms are established tools and are credited.

Fresh primary sources read: Zhang and Cheng, *An efficient version of the Bombieri–Vaaler theorem*, arXiv:1707.05941, Theorems1.4/2.6 and Section3; and Labahn and Storjohann, *Computing bases in Hermite normal form of lattices of integer relations*, May8,2026 author manuscript, Sections1 and2. The latter explicitly treats integer relation lattices, canonical Hermite image bases and minimum matrix denominators. A separate Kannan–Bachem PDF link failed to fetch; no theorem from that inaccessible copy is used. No located source proves the e+pi consequence required here.

The following exterior-power and rank-two identities are proved directly, rather than inferred from a lattice height bound.

## Full matching space and coefficient map

Use the endpoint sequences C_r=D_(2r)-(-1)^r, R_r=-(2r)!+4 sum_(a=1)^r(-1)^(r-a)/(2a-1), and V_r=(-1)^r. Let C,R,V now have k rows and 2k+1 columns, entry indexed by i+j. C has full row rank. The saturated lattice

    K={z in Z^(2k+1): Cz=0}

has rank k+1. A Smith decomposition UCT=[diag(s_1,...,s_k),0] with T unimodular gives a saturated integer basis Q=T[:,k:]; no separately primitive rational nullspace columns are substituted for this lattice basis.

Choose an integer delta clearing RQ, and put

    H(T)=delta(RQ+T VQ), a k by(k+1) integer polynomial matrix.

For each omitted column j, write its signed maximal minor as

    (-1)^j det H(T)_[omit j] = A_(0j)+T A_(1j).

The matrix A of these two-coordinate columns is integral. All minors are affine because VQ has rank at most one.

For any integer (k+1) by k matrix Z, the complete physical determinant of the right polynomials QZ satisfies

    delta^k det(RQZ+S VQZ) = (Aw)_0+S(Aw)_1,
    w_j=(-1)^j det Z_[omit j].

This is full Cauchy–Binet; both endpoint contributions are included.

Every vector w in Z^(k+1) can occur as these exterior coordinates. To prove it, write w=g w_primitive, complete the primitive covector w_primitive^T to a unimodular basis, take its k kernel columns, and multiply one column by the appropriate signed g. Thus the COMPLETE attainable integer coefficient-pair module is exactly

    L=A Z^(k+1) subset Z^2.                 (1)

This is a stronger statement than rational spanning. The full gcd of each attained pair must still be removed afterwards.

## Rank-two criterion

The map A has rank2 if and only if the following rational bordered determinant is nonzero:

    det [ C ; R ; E ] !=0, E_j=(-1)^j.      (2)

Indeed, after splitting off C, this is equivalent to [RQ;EQ] having full rank k+1. If RQ has rank<k, its constant minor vector vanishes and A cannot have rank2. If RQ has rank k, reduce it to [I,0]. The rank-one perturbation v(EQ), with nonzero v_i=(-1)^i, changes the maximal-minor vector in a direction independent of its constant vector exactly when the final component of EQ is nonzero. This is precisely the bordered criterion.

Equation(2) is nonzero in every new exact instance k1..6. The analysis agent subsequently proved this determinant nonzero with sign(-1)^k for every k>=24 by its complete positive-tail integral representation; see agent3_analysis/SHORT_RECTANGULAR_BORDER_NONZERO.md. Thus rank2 and the rational-direction realization below hold for every k>=24, independently of the finite receipts.

## Minimal lattice multiple and exact primitive denominator

Assume rank A=2. Let B be the 2-square Hermite basis of L, and let d_1|d_2 be its Smith invariants. Then [Z^2:L]=d_1d_2, while the exponent of the quotient group is d_2.

For any primitive target pair (b,a), a>0, its LEAST positive lattice multiplier is exactly

    lambda(b,a)=lcm(denominators of B^(-1)(b,a)^T),
    lambda(b,a) divides d_2.                (3)

There is therefore an integer family of right polynomials of degree at most2k with complete determinant

    delta^k det H_physical(S)=lambda(b,a)(b+aS).

After the final gcd, its actual center and denominator are

    c=-b/a, q_actual=a,
    q_actual(S-c)=b+aS.                     (4)

In particular, if rank2 holds, every rational center can be encoded at this single fixed k. Free choice of a rational direction does not itself prove smallness of a nonzero integer form. Selecting a direction already close to S would import exactly the Diophantine approximation problem one is trying to solve. The required lifting vectors, polynomial coefficients and full physical integral must be controlled rather than discarded.

This also explains why the M24 positive signed-error theorem cannot be transferred to every k-plane in this enlarged kernel: (4) allows centers on either side of S and arbitrarily far from it.

## Whole stacked minors and matching content

The coefficient lattice can be computed without guessing a short kernel basis. Let Delta_C be the gcd of the k-square minors of C. Choose delta clearing the FULL R matrix, and form the 2 by(2k+1) coefficient matrix G of the signed maximal minors of

    [ C ; delta(R+T V) ].

Then, exactly as integer lattices,

    G Z^(2k+1) = Delta_C L.                 (5)

Proof: a unimodular right transformation to Smith coordinates acts unimodularly on the maximal-minor vectors. The first k top pivots must be included for a nonzero maximal minor; each remaining minor is Delta_C times a maximal minor of delta(RQ+T VQ). Left top Smith operations affect only an overall sign. Taking images gives(5).

Consequently each nonzero Smith invariant of G is Delta_C times the corresponding invariant of A, and its rank-two lattice index is Delta_C^2 times the index of L. The matching determinantal divisor is therefore a genuine, removable module factor. Formula(5) does not assert a favorable asymptotic size for the two remaining invariants.

## Six new exact receipts

The driver checks the unimodular Smith decomposition of C, saturation of Q, exact affine maximal minors, rank2, the Hermite image lattice, both Smith invariants, the full stacked identity(5), and complete determinant realization of four fresh primitive directions at every k1..6. It finally removes the attained pair gcd and verifies the actual denominators1,1,7,50 for those directions.

For the minimal restricted entry clearer used in the receipt, the coefficient-lattice index bit lengths are

    9,52,134,271,459,708,

and the quotient-exponent bit lengths are

    9,49,124,245,409,623.

These are exact finite integer measurements, not asymptotic cost or approximation claims. The receipt also stores the universal full-entry clearer and matching determinantal divisor for(5).

Files: EXTRA_COLUMN_PAIR_LATTICE_CERTIFICATE.json and extra_column_pair_lattice.py.

## Outstanding original arithmetic question

Can one choose controlled coefficient-lattice directions whose COMPLETE primitive errors are nonzero and tend to zero, with a justified infinite sequence and all lifting costs retained? The lattice description makes this question exact; it does not solve it. The main e+pi problem remains open.
