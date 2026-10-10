> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Two-law noncommuting transport: exact bridge, target loss, and public-core gate

Status: discarded bounded Genesis candidate. The two actual laws are retained in the definitions. No numerical independence theorem, rational approximation, or audit is asserted.

## Actual global bilinear bridge

Put E(z)=exp(z), A(z)=4 arctan(z), T(z)=z+1, and M(z)=(z+1)/(1-z). Near z=0, with A continued from its real branch,

    E(Tz)=e E(z),
    A(Mz)-A(z)=pi.

The second identity follows either by differentiating both sides and evaluating at zero, or from the tangent addition law. It is an identity on the appropriate continued sheet, not an equality of arbitrary principal branches across every cut. Thus, for any scalar r,

    E(Tz)+[A(Mz)-A(z)]E(z)=r E(z)

holds identically on this local domain if and only if r=S=e+pi. Under S rational it is a rational-parameter global bilinear transport relation. This is an exact scalar-to-object bridge without claiming that either individual transport constant becomes rational.

The proposed operation was to exploit noncommuting rational-domain transports to force an arithmetic restriction on the rational parameter. Its first test is the complete difference between the two word orders.

## Exact commutator test

Define P=T o M and Q=M o T. Their explicit rational forms are

    P(z)=2/(1-z), Q(z)=-(z+2)/z.

The exponential transport ratio satisfies

    E(P(z))/E(Q(z))=exp(P(z)-Q(z))

and

    P(z)-Q(z)=(2+z-z^2)/(z(1-z)).

For the additive law, on any common continued sheet away from the poles,

    d/dz [A(P(z))-A(Q(z))]
      =8/(z^2-2z+5)-8/(2z^2+4z+4).

Every displayed formula is unconditional and its coefficients are rational. The derivative loses any branch integration constant; this is not a proof that the complete additive difference has a rational value at a rational base point.

A combined multiplicative word-order observable, formed locally as

    K(z)=[E(P(z))/E(Q(z))] exp(i[A(P(z))-A(Q(z))]/4),

is an algebraic factor times exp(P-Q), because exp(2 i arctan(w))=(1+iw)/(1-iw). Its logarithmic derivative is

    K'/K=(P-Q)'+(i/4)[A(P)-A(Q)]'.

Again this is independent of r and of the rationality hypothesis. The natural noncommuting comparison retains interior law data but eliminates the numerical parameter it was intended to constrain. A different operation would have to supply an actual arithmetic output consequence from the bilinear identity; that consequence has not been derived.

## Archive and fresh primary gate

Archive query: `cocycle|difference.?galois|noncommut.{0,40}(transport|M.bi|functional)|translation.{0,40}(arctan|logarithm)|M.bi.{0,50}(exponential|functional)`, over sources and work Markdown.

The decisive inherited match was sources/explicit_nonsplit_mixed_extension_audit.md, its Sections 7--8: differences of path transports can eliminate absolute target constants, and functional noncommutativity does not by itself provide numerical specialization. The older raw transport files concern distinct asymptotic systems and were not treated as an exact match to the present T,M construction.

Fresh searches:

- `noncommuting Mobius transformations exponential logarithm functional equations cocycle transcendence`
- `difference Galois exponential logarithm functions translation Mobius transformation algebraic independence`
- `exponential periods e pi algebraic independence functional equation logarithm exponential values`
- `Hardouin Singer differential Galois theory linear difference equations 2008 arxiv`
- `Mobius transformation logarithm cocycle group cohomology functional equation arctangent`
- `mixed exponential logarithmic values e pi independence Waldschmidt exponential periods conjecture`

Opened full primary papers: Hardouin--Singer, https://arxiv.org/pdf/0801.1493 (50 pages), especially the introduction and first-order additive/multiplicative difference equations; Di Vizio--Hardouin--Wibmer, https://arxiv.org/pdf/1302.7198 (43 pages), difference algebraic relations among differential-equation solutions. Opened the author survey Waldschmidt, https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/TranscendencePeriods.pdf (29 pages), to delimit the familiar numerical period/exponential-period problem. Bertrand's primary article landing page https://aif.centre-mersenne.org/articles/10.5802/aif.2507/ was opened; it was not substituted for a full paper read.

None of these reads is claimed to settle the exact bilinear numerical identity above. The proposed continuation through differential/difference Galois functional independence, followed by a value-faithfulness step, is nevertheless an already public essential mechanism and is expressly excluded by the active protocol. The commutator formulas give a separate concrete target-loss result. Therefore this candidate is discarded promptly; no noncommuting Galois variant or periodicity extension is developed.

## Additional bounded gate: finite rational-group relations and cocycle closure

This addendum inspects the operator core itself, separately from Galois classification. Write J=M^2, so J(z)=-1/z. Then J^2=id and (J T)^3=id as rational transformations. Moreover

    D_2=T o M o T o J, D_2(z)=2z.

For example, successive application of J,T,M,T gives z -> -1/z -> (z-1)/z -> 2z-1 -> 2z. Thus the rational domain group also contains D_2^(-j) T D_2^j, the translation z -> z+2^(-j).

This does not propagate the scalar rationality assumption to a second rational synchronized replica. Substituting z -> z/2 in the bilinear identity still evaluates E(z/2+1)/E(z/2)=e; it does not evaluate E((z+1)/2)/E(z/2)=sqrt(e). The coefficient remains S. Extracting fractional-translation multipliers yields positive radicals of e, but no rationality of sqrt(e)+pi follows. The root's separate positive-radical field-exchange theorem already delimits that algebraic enlargement.

Here is a precise finite-word closure lemma. For a consistent lift of a composable word g_1...g_l, additive increments A(g_j w)-A(w) telescope along its successive arguments to A(g_1...g_l z)-A(z). Multiplicative ratios E(g_j w)/E(w) telescope to E(g_1...g_l z)/E(z). If the rational word is the identity and the chosen lift returns to the same complex base point, the exponential ratio is 1 and the additive increment is 4 pi times an integer winding difference around i and -i. This follows from

    A(z)=(2/i)[log(1+iz)-log(1-iz)].

The complete lift must be used: for z>0, both real principal values give A(Jz)-A(z)=-2pi, while two successive +pi M continuations give +2pi. Their difference is exactly 4pi. They cannot be interchanged inside a group-word telescope.

Thus imposing the standard finite group/cocycle relations retains the circular monodromy and the exact exponential law but gives no arithmetic constraint on e+pi. This is a scoped result for word closure and coboundary operations, not a classification of arbitrary noncommuting operator algebras or a global impossibility theorem.

The additional archive query was `Lewis.?Zagier|Eichler|group.{0,30}cocycle|weighted.{0,20}composition|modular.{0,25}(transport|relation)|Mayer.{0,20}operator`; it returned no exact archived match. Fresh queries were `Lewis Zagier period functions Maass wave forms transfer operator modular group cocycle primary arxiv`, `Mayer transfer operator Gauss map modular group functional equation period functions primary paper`, and `weighted composition operators cocycle representation group relation holomorphic primary paper`.

Opened full primary documents: Lewis--Zagier, https://arxiv.org/pdf/math/0101270 (68 pages), its introduction and Section I.2, explicitly organizing functional equations by the modular transformations z+1 and -1/z; Bruggeman--Lewis--Zagier, https://people.mpim-bonn.mpg.de/zagier/files/tex/PeriodFunctions4MaassWaveForms/pfmw-coh130826-rb.pdf (132 pages), its introduction's cocycle and modular group-relation equations. A weighted-composition PDF at https://math.indianapolis.iu.edu/~ccowen/Downloads/44HermitWComp.pdf failed to fetch and is not claimed as read.

These papers do not state our numerical S identity or provide its missing arithmetic theorem. They do establish the proposed operator core of group-relation/cocycle consistency as public machinery. The finite-word closure branch is therefore discarded under the human's mechanism rule. A future genuinely different operation must give more than this already public consistency mechanism, and must prove its rational-S output property rather than assume finite arithmetic closure of the full transformed functions.

## Full orbit cannot silently be replaced by a finite scalar module

For distinct nonnegative integers j, the functions

    E(M(T^j z))=exp(-1-2/(z+j-1))

are linearly independent over C(z). Indeed, in any finite putative relation, at z=1-j only its jth term has an essential singularity. All other terms, including their rational coefficients, are meromorphic there. A nonzero rational coefficient cannot remove the essential singularity, so that coefficient must vanish. Repeating at each distinct pole proves independence.

Likewise, the functions A(T^j z)=4 arctan(z+j) are linearly independent over C(z), even after adjoining a rational summand. Their branch points -j+i and -j-i are pairwise distinct. Continuation of a finite relation around -j+i changes only its jth logarithmic term, by a nonzero 4pi multiple of its rational coefficient. Hence that coefficient is zero; repeat for every j.

Both proofs are unconditional and remain true under a hypothetical rational S. Consequently, rationality of the single transport trace S cannot supply a finite-dimensional C(z) module containing either full noncommuting orbit. This does not forbid finite-dimensional quotients, selected observables, nonlinear operations, or a genuinely different infinite operator construction. It precisely rules out treating the actual full transformed functions as the two scalar source eigenspaces. The essential-singularity and monodromy proofs are classical support, not a retained Genesis obstruction principle.
