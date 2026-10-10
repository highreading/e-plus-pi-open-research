> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the Borel CZDS, sector and actual mixed-root claims

Date: 2026-09-13. Reviewer: audit_computations.
Reviewed: `literature_borel_czds_sector_and_mixed_obstruction.md`.

**Outcome: PASS**, with the two requested explicitness corrections now
applied by the author: strict half-plane preservation uses a positive
margin inside a closed circular region; the crossing formula uses an
explicit sum of multiplicities and treats a zero parity component.
No degree scan or numerical root calculation was used.

## 1. Primary theorem hypotheses were checked directly

I read the accessible primary author-hosted Craven--Csordas survey,
Definition 1.5, Theorem 2.4(1), and Theorem 4.1, including its explicit
reciprocal-factorial example:
https://math.hawaii.edu/~tom/mathfiles/czdssurvey.pdf .
Its CZDS theorem applies to REAL input coefficients and counts nonreal
zeros with multiplicity. Its Schur--Szego theorem instead permits
complex coefficients and gives the indicated root-location description
for binomial coefficient composition. These are different statements.

I also read Cardon--Forgacs--Piotrowski--Sorensen--White, Section 4.2,
and its definition of sectors (which includes the vertex):
https://arxiv.org/pdf/1802.02641 . Its necessary contraction condition
indeed excludes the reciprocal factorial. The explicit quadratic and
fourth-degree arguments in the reviewed note independently establish
the particular obstructions used here. No inaccessible later theorem
of Chasse is needed for any mathematical conclusion in this audit.

## 2. An independent elementary proof of the real Borel CZDS theorem

The real-coefficient restriction can be checked constructively. Write
N_R(f) for the number of real zeros with multiplicity. For an integer
j>=1 and a nonzero real polynomial f of degree d,

    (theta+j)f=x^(1-j) D(x^j f),  theta=xD.

The polynomial x^j f has N_R(f)+j real zeros. Rolle's theorem, including
multiplicities, gives at least N_R(f)+j-1 real zeros of its derivative.
Dividing its forced factor x^(j-1) leaves at least N_R(f) real zeros.
The resulting degree is still d, because its leading coefficient is
multiplied by d+j, which is nonzero. Thus each factor 1+theta/j cannot increase the
number of nonreal zeros for a real input.

Apply the product of these factors for j=1,...,N to f(x/N). Its multiplier
on the coefficient of x^k is exactly

    N^(-k) product_(j=1)^N (1+k/j)
       =(N+k)!/[N! k! N^k] ->1/k!.

Every finite product preserves at least the input's real-zero count.
The coefficient limit has the same degree d and nonzero leading
coefficient. Polynomial-root continuity therefore preserves that lower
bound on real zeros, counted with multiplicity: roots cannot escape to
infinity, and a limit of real roots is real. The limit is Bf.
This proves the precise real-input CZDS inequality used in the note,
independently of the cited survey. It supplies no such argument for
complex coefficients, because the real Rolle step would then fail.

## 3. Phases, degree drops and the real high pencil

The definitions p_k(t)=i^(-k)Q_k(it) and g_k(t)=i^(-k)F_k(it) have the
correct phase: p_k is ordinary monic Legendre, and g_k=Bp_k is real.
For a real raw mixture, even and odd k contribute real and imaginary
coefficients respectively after rotation. If both parity components
are nonzero, no one scalar phase makes the entire rotated polynomial
real. Independence of polynomial degrees excludes an accidental
vanishing of a nonzero parity component.

For a nonzero real combination p of p_m,...,p_N, let d be its actual
degree. Then d>=m, even if top coefficients are absent. Orthogonality
to all degrees below m forces at least m sign changes in (-1,1):
otherwise the product of factors at all sign-change points would be
an allowed test polynomial whose product with p has one nonzero sign.
Hence p has at most d-m nonreal zeros. Section 2 transfers this upper
bound to Bp. Since Bp is real, its nonreal roots occur in conjugate
pairs, giving the stated even-integer refinement.

For m=n+1,N=2n-1 the bound is at most n-2. The result concerns the
real phase-adjusted pencil; it does not claim that Borel preserves
orthogonality or retains those real roots within the original interval.
Each real pencil U+sV has the required phase-adjusted coefficients;
the parameter s=i of the actual rotated mixture is outside this theorem.

## 4. Strict half-plane preservation has the correct normalization

For degree d, put the input in binomial form
A(z)=sum binom(d,j)a_j z^j, and use the symbol

    J_d(z)=sum binom(d,j) z^j/j!=L_d(-z).

Then the Schur--Szego composition is exactly BA, with no missing j!
or binomial factor. Laguerre orthogonality gives d strictly negative
roots beta_j of J_d. The cited theorem describes every output root as
-w beta_j, with w in a containing closed circular region of the input.

To retain a STRICT half-plane conclusion, put the finitely many input
roots in Re(e^(-i theta)z)>=epsilon>0. This is an allowed closed circular
region. Since -beta_j>0, every output root has strictly positive rotated
real part. Thus no root on the boundary or at zero appears. Intersecting
two such half-plane conclusions gives the open convex-sector statement;
the closed-sector version including the vertex follows by a coefficient
limit. Degree is preserved throughout.

The quadratic no-uniform-contraction example has the correct scaling:
after factoring z^m and putting z=(m+1)u, the coefficients are
1,-2cos(theta),(m+1)/(m+2). For sufficiently large m its conjugate roots
have cos(theta_m)=cos(theta)sqrt((m+2)/(m+1)), so theta_m tends to theta.
The zero at the vertex is explicitly allowed by the cited sector
convention. If one instead requires zero-free inputs, replace z^m by
(z-epsilon)^m after fixing a large m; continuity preserves the offending
simple nonreal pair. The example 4+z^4 also has exactly the asserted
unchanged arguments after Borel.

## 5. The actual adjacent two-term theorem is correct for every k

The ratio p_k/p_(k+1) has simple real poles t_j and positive residues,
by the interlacing signs of p_k(t_j)/p_(k+1)'(t_j). Since both polynomials
are monic and differ in degree by one, the residues sum to 1 and there
is no polynomial part. For z off the real line,

    Im sum_j w_j/(z-t_j)
       =-Im(z) sum_j w_j/|z-t_j|^2.

The root equation p_(k+1)+ic p_k=0, c>0, requires this ratio to equal
i/c. A pole is not a root because consecutive Legendre polynomials
are coprime. Real nonpoles are excluded because the ratio is real there;
the upper half-plane is excluded by the displayed sign. Thus all k+1
roots lie strictly below the real line. The identity

    Q_(k+1)(iz)-cQ_k(iz)=i^(k+1)[p_(k+1)(z)+ic p_k(z)]

has the correct plus sign. Multiplication by i carries the strict lower
half-plane into the strict right half-plane. Section 4 transfers that
location to F_(k+1)-cF_k. The k=0 case is included, with root c>0.
No simplicity assertion about the final transformed roots is required.

Taking k=2n-2 gives a member of the actual high span for every n>=3:
both indices lie between n+1 and 2n-1. Its degree is exactly 2n-1,
so all that many roots are in the open right half-plane. This disproves
the stronger half-plane count, but says nothing contradictory about
how many of them lie on the interval (0,1).

## 6. Both generic counterexamples are exact and appropriately scoped

For (z-1)(z-i), direct Borel transformation gives
(z-(1+i))^2/2. The nonreal-zero count changes from one to two, so the
real CZDS theorem really cannot be extended to all complex inputs.

The cubic (x-4)((x+1)^2+25) has exactly one right-half-plane root and
none on its boundary. Its Borel transform multiplied by 6 has derivative
3[(x-2)^2+32]>0, one real root a strictly between 0 and 6, and a nonreal
conjugate pair with real part (6-a)/2>0. Thus its right-half-plane count
increases from one to three. This does not conflict with preservation
when ALL input roots lie in that half-plane. Neither generic example
is incorrectly promoted to an actual-family counterexample.

## 7. Common factors and sign-selected crossings

Assume f is nonzero and write f(x)=A(x^2)+xB(x^2). If one parity
component vanishes, its interior zero count is exactly that of the
other polynomial in y=x^2; the extra x factor has no interior zero.
Otherwise factor A=DA0,B=DB0 with gcd(A0,B0)=1 and put
P=A0^2-yB0^2. This polynomial is not identically zero: equality of
those squares would give incompatible parities of their valuations
at y=0. At a positive root of P, neither A0 nor B0 is zero, by
coprimality. The wanted factor A0+sqrt(y)B0 vanishes if and only if
A0B0<0. Its other factor A0-sqrt(y)B0 is then nonzero, so its root
multiplicity is exactly ord_y P.

The map x->x^2 is a diffeomorphism of (0,1), preserving multiplicities.
Consequently the corrected sum of multiplicities in equation (10)
is exact. If D also vanishes at a selected root, the two multiplicities
must ADD, as they do in that formula. For a distinct-root count the
correct object is instead the UNION of the D roots and the sign-selected
P roots, so such an intersection contributes only once. The reviewed
note now explicitly makes both distinctions.

No bound on the unsigned roots of P or on the half-plane roots of f
can silently replace this selected set. The actual mixed interval
zero theorem remains unproved, and none of the reviewed results
establishes irrationality of e+pi.
