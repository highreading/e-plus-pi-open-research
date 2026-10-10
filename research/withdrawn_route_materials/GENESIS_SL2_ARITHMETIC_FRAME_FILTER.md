> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Genesis root candidate G-R9: rational character versus arithmetic frame

2026-10-02. Active original-design support, no main proof and no independent audit. The candidate finite-matrix trace core is discarded as classical after the fresh gate below. This note is not a retained new mathematical paradigm.

## Exact candidate and bridge

Put S=e+pi and H=[[e,1],[e*pi-1,pi]]. Then det H=1 and tr H=S. Under S=q in Q, both eigenvalues solve X^2-q X+1=0 and hence are algebraic. This is a valid nonlinear algebraic output of the rational-sum hypothesis. It does not separate the two original constants.

More generally, for any x,y in a characteristic-zero field set

H(x,y)=[[x,1],[xy-1,y]], P(y)=[[0,1],[1,y]], C(s)=[[0,-1],[1,s]], s=x+y.

Direct multiplication gives det P=-1 and H P=P C(s). Thus P^-1 H P=C(s), without exceptions. In particular all traces h_n=tr(H^n), including negative n, satisfy h_0=2, h_1=s, h_(n+1)=s h_n-h_(n-1). Under rational s they are ALL rational. Exterior powers, characteristic polynomials, and all polynomial conjugacy invariants of this one matrix likewise depend only on s and the fixed determinant.

## The missing frame does not follow

If S were rational, H would be conjugate over Q(e,pi) to the rational matrix C(S), while its actual entries remain transcendental. There cannot be a conjugating B in GL_2(Qbar): otherwise H=B C(S) B^-1 would have algebraic entries, contradicting the established transcendence of e. Thus rationality of a character and rationality of the conjugating frame are different conditions even for the actual conditional object.

An unconditional countermodel makes the scope independent of the unresolved hypothesis: take any transcendental x and any rational s, put y=s-x, and use the displayed H(x,y). It has rational determinant, rational trace, algebraic spectrum, and rational traces of EVERY power, yet no arithmetic conjugating frame. A rational character does not make the entries or eigenvectors algebraic.

The synchronized-law replicas e^n+n*pi from Agent1's backbone are not tr(H^n). For example tr(H^2)=(e+pi)^2-2, while the synchronized replica is e^2+2*pi. Their difference is 2*e*pi+pi^2-2*pi-2>0 (already e>2 and pi>3 suffice). No operation equating them has been proved.

The actual function matrix H(z)=[[exp z,1],[4 exp(z) atan(z)-1,4 atan(z)]] has rational germs at0, determinant1, and trace F(z)=exp z+4 atan z. Conjugation by P(4 atan z) gives C(F(z)) identically. At a rational endpoint with rational F, the endpoint companion matrix becomes rational, but the moving frame still contains the actual logarithmic function. Merely relabeling this identity as arithmetic holonomy inserts no new arithmetic condition.

## Fresh archive and public literature gate

Archive query covered Fricke, character variety, trace/SL2, spectral algebraization, Cayley-Hamilton and trace/e/pi across sources and work. Existing overlap included finite algebra/norm carriers, the root radical-symmetry filter and Agent3's distinct infinite-operator spectral-edge countermodel. No previous actual H/P formula was located in this bounded search; absence is not a novelty claim.

Fresh queries: SL2 character variety Fricke trace polynomial eigenvalues; matrix SL2 transcendental entries algebraic trace companion conjugation trace powers. Opened Serge Cantat, *Endomorphisms and bijections of the character variety (F2,SL2(C))* (2020), full11-page PDF at https://afst.centre-mersenne.org/item/10.5802/afst.1648.pdf. Read Section1/printedp898: the classical Fricke coordinate theorem and Cayley-Hamilton trace reductions. This directly identifies matrix-character polynomial closure as a public core. Also opened Przytycki--Sikora q-alg/9705011 full47-page PDF, but did not use unread sections as mathematical support. Search returns outside primary sources were not relied on.

The displayed H/P identity and conditional actual-frame warning have elementary proofs above. They are specific support deductions, not new trace theory. DISCARD finite spectral/character algebraization as a Genesis core. This does not exclude genuinely infinite, nonlinear, or additional law-sensitive operations.

