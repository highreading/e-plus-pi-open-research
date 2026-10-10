> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent growing-arithmetic and endpoint-content review

Reviewer: Agent 4. Scope: 1<=b<=n, the assigned arithmetic identities in agent1/GROWING_DEGREE_ARITHMETIC.md and the automatic divisor in GROWING_FACTORIAL_CONTENT_DRAFT.md. Both completed family audits are preserved.

## Verdicts

- Monic Rodrigues row factors and unrestricted derivative divisibility: PASS.
- Elementary endpoint extension and signed maximal minors: PASS.
- Row, minor, and three-contraction content removal: PASS WITH CLARIFICATION concerning deficient-rank representatives.
- Conservative final clearer and exact reduced denominator: PASS.
- Automatic A_b^2 divisor, including actual cleared endpoints: PASS.
- b=1 and b=2 compatibility: PASS.
- Former strict residual-content target: NOT endorsed as attainable. Its combined analytic audit belongs to Agent 2.

No growing-degree rank, endpoint nonvanishing, remainder nonvanishing, or irrationality conclusion is established here. Agent 1's additional recurrence is outside this review.

## 1. Monic factors and all-size integrality

Write E_(k,r)=(d/dx)^r[x^k H_k(x)] at x=1. Rodrigues gives

    sum_m [y^m]L_k(y) x^(k+m)/(k+m)! = 2^k x^k H_k(x)/(k!)^2.

For k=n+l and r=l+j-1, the differentiated factorial argument is n+m+1-j, at least n+1-b>=1. Dividing by the leading coefficient 2^k(2k)!/(k!)^2 proves

    ell_j(p_(n+l))=E_(n+l,l+j-1)/(2n+2l)!.

Thus rho=1/rho_plus, where rho_plus=product_l (2n+2l)!, is exactly the monic high-row factor.

Let a_s(k)=[z^s](1-z+z^2/2)^k. The coefficient of x^(k-s) in H_k is (k)_s a_s(k). Each trinomial contribution with c quadratic selections has integer multinomial coefficient divided by 2^c and s>=2c. The consecutive product (k)_s contains at least c even factors. Therefore H_k is an integer polynomial.

Likewise H'_k/k has coefficients (k-1)_s a_s(k), 0<=s<=k-1; the same argument proves integrality. For r>=1, the term in the Leibniz expansion with no derivative on x^k contains H_k^(r), divisible by k. Every other nonzero term contains (k)_a with a>=1, also divisible by k. Hence k divides E_(k,r) for all k>=1,r>=1, including zero derivatives. This covers every entry of rows l>=2; row l=1 includes derivative order zero.

Separately, r! divides E_(k,r), because differentiating any integer monomial gives r! times an integer binomial coefficient. These two divisibilities do not justify multiplying k and r! without accounting for shared factors.

## 2. Elementary endpoints and minor signs

For 0<=j<=b<=n, summing the absolutely convergent factorial tail proves

    ell_j(Q/(1-y))=exp(1)Q(1)-T_j(Q).

The smallest partial-sum index is n-j>=0. Thus the endpoint formulas extend through j=n without negative factorials. With P=L_n, Uadj=L_(n+1), A=P(1), B=Uadj(1), and G=A w_U-B w_P=(-1)^n 2^(2n+3)/(n+1), Christoffel–Darboux and Taylor reconstruction give

    t_j=(A T_j(Uadj)-B T_j(P))/G,
    x_j=(w_P T_j(Uadj)-w_U T_j(P))/G.

In particular x_j is the reconstructed A endpoint, not just a tail.

For the integer high block R, expansion along its last two appended rows gives the signed minor coefficient (-1)^(i+j+1) for omitted zero-based columns i<j. Indeed the one-based last-row sum is b+(b+1), and the selected column sum is (i+1)+(j+1); their total has parity i+j+1. Surviving columns retain natural order. This proves the sign for all sizes, independently of a fixed-size symbolic example.

If all row contents c_l are positive, divide them out to obtain R0. If its maximal-minor content mu is positive, put hcont=Crows*mu. Then hcont is exactly the positive gcd of the maximal minors of R, and

    det[U;v;w]=rho hcont Bbar(v,w).

This holds for arbitrary rational endpoint rows.

The cumulative rows p_j=sum_(i=1)^j E_(n,i-1) and u_j=sum_(i=1)^j E_(n+1,i)/(n+1) are integral, with zero initial entries. Exact differences of the partial sums give

    T(P)=TP e-f p,
    T(Uadj)=TU e-2f u/(n+1),
    f=2^n/(n!)^2.

With sigma=-Bbar(e,u), c=-Bbar(e,p), kappa=Bbar(u,p), bilinearity and the Wronskian prove

    D=(n+1)B c-2A sigma,
    Q=2w_P sigma-(n+1)w_U c,
    V=sigma Acal-c Bcal-kappa,
    (X,Y)=rho hcont f/((n+1)G) (Q+2fV,D).

Here TP=f Acal and TU=2f Bcal/(n+1). The complete numerator also equals

    2(w_P+TP)sigma-(n+1)(w_U+TU)c-2f kappa.

Thus every partial-exponential and second-kind term is retained. On D!=0, d=gcd(|sigma|,|c|,|kappa|)>0. Dividing the three contractions by d produces starred quantities and removes exactly a common factor d from both complete endpoints.

## 3. Exact final gcd and rational scale correspondence

Put

    F=(2n+1)!,
    Lambda=2^(n+1)(n+2)!F(n!)^2,
    Nstar=Qstar+2fVstar,
    gamma=gcd(|Lambda Nstar|,|Lambda Dstar|).

Lambda clears Nstar directly from its expanded numerator: the T denominators divide F, the moment denominators through degree n divide 2^n(n+1)!, and Lambda also clears f. All remaining coefficients are integers. Dstar is integral. On Dstar!=0,

    q=Lambda |Dstar|/gamma.

If Nstar=0 this gives q=1. Otherwise the equivalent prime formula is max(0,v_p(Dstar)-v_p(Nstar)). At odd p, writing Rstar=Vstar+(n!)^2 Qstar/2^(n+1) retains the exact formula max(0,2v_p(n!)+v_p(Dstar)-v_p(Rstar)). The second-kind bound v_p(Qstar)>=-floor(log_p(n+1)) follows from the moment denominators and integral starred contractions. No bound for Vstar or transfer theorem for growing minors is supplied.

Now use the specified monic clearer

    M=2^(2n+3)F^2 rho_plus,
    g=gcd(|MX|,|MY|), Y!=0.

The exact endpoint scale is

    (X,Y)=rho_plus^(-1) hcont d f/((n+1)G) (Nstar,Dstar),
    (MX,MY)=(-1)^n hcont d 2^n F^2/(n!)^2 (Nstar,Dstar).

Consequently

    g=Crows*mu*d * F/[2(n+2)!(n!)^4] * gamma.

The rational denominator in this identity is essential. In particular g is not Crows*mu*d*gamma. The positive rational gcd of (Nstar,Dstar) is gamma/Lambda. Homogeneity of rational gcd justifies this equality even when the scale is nonintegral: after dividing an integer pair by its gcd, its coordinates are coprime, so a rational multiplier yielding an integer pair must have integral magnitude. An endpoint gcd taken after primitive polynomial normalization requires that normalization's additional scale as well.

## 4. Endpoint clearer and the automatic factorial divisor

Since (l+j-1)!/((l-1)!j!) is integral,

    R_lj/((l-1)!j!) is integral.

Define A_b=product_(j=0)^(b-2) j!, with A_1=1. Every maximal minor contains the row factor A_b. Its ordered selected column indices j_s satisfy j_s>=s-1, so its column factorial product is divisible by A_b. Therefore A_b^2 divides every maximal minor, including zero minors. On full row rank, A_b^2 divides hcont. It must not be counted again in addition to hcont.

It remains necessary to transfer this divisor to the actual endpoints. Let Delta_P=det[R;e;T(P)], Delta_U=det[R;e;T(Uadj)], and E=det[R;T(Uadj);T(P)]. The endpoint signs are

    rho_plus Y=(B Delta_P-A Delta_U)/G,
    rho_plus X=(w_P Delta_U-w_U Delta_P-E)/G.

Every T row is cleared by F, so F Delta_P, F Delta_U and F^2 E are integers. Also

    F/(2^n n!)=1*3*5*...*(2n+1)

is integral. Together with the moment denominator bound 2^n(n+1)!, this proves that (n+1)F clears w_P,w_U. Hence

    MX=(-1)^n(n+1)F^2(w_P Delta_U-w_U Delta_P-E),
    MY=(-1)^n(n+1)F^2(B Delta_P-A Delta_U)

are integers.

More explicitly, write EP=F Delta_P, EU=F Delta_U, EE=F^2 E, W1=(n+1)F w_P, W2=(n+1)F w_U. Apart from the common sign, the cleared pair is

    (W1 EU-W2 EP-(n+1)EE, (n+1)F(B EP-A EU)).

Divide every high minor by A_b^2. These quotients are integer coefficients of an alternating form, whether or not they arise as minors of another matrix. The same formulas and clearing argument apply to that form. Thus MX/A_b^2 and MY/A_b^2 are integers. On Y!=0 this proves A_b^2 divides g. The argument also proves hcont divides g on full high-row rank. This is a direct cleared-endpoint proof, not an inference from auxiliary minors alone.

For b=1 the high block is empty, its unique empty minor is 1, and A_1=Crows=mu=rho_plus=1. Every formula above remains valid. No empty-minor content is zero.

## 5. Rank qualifications and compatibility

The phrase 'the quotient domain is empty' for a zero high row must mean the domain of this chosen cofactor representative. A zero row or deficient high-row rank forces every maximal cofactor of the augmented matrix to vanish: adding one endpoint row cannot raise rank to b. Thus this representative gives X=Y=0. It does not establish nonexistence of other solutions of the original underdetermined system or exclude their nonzero endpoints.

In this deficient-rank case A_b^2 still divides all minors and both zero cleared endpoints, but g as defined on Y!=0 is not available. Do not divide by zero row content, mu, or d. Even full high-row rank does not alone imply rank b of the augmented system or nonzero Y. Dstar!=0 ensures nonzero Y and validates the quotient. A zero complete numerator is a different case, giving q=1; full remainder nonvanishing is another independent requirement.

Without content divisions, b=1 has (sigma,c,kappa)=(-K_(n+1),-H_n,0), where K is the familiar b=1 scalar. Both complete numerator and denominator have the same reversed sign relative to the established b=1 quotient.

For b=2, use high row (a,(n+1)k,(n+1)ell), p=(0,h,h+J), u=(0,k,k+ell). Direct determinants yield

    sigma=(n+1)k^2-a ell,
    c=((n+1)k-a)J-(n+1)(ell-k)h,
    kappa=a(kJ-ell h).

Thus V is precisely the completed b=2 Vtilde, including a*omega. The old b=2 V, complete numerator, and denominator are each n+1 times the corresponding quantities here. These are formal compatibility identities; no completed prime or degree scan was extended.

## 6. Obstruction draft and interpretation

I read GROWING_BOUND_OBSTRUCTION_DRAFT.md and the status correction in GROWING_FACTORIAL_CONTENT_DRAFT.md. The algebraic observation g<=|MY|=M|D_V| on Y!=0 follows immediately from the verified integer clearing. If the stated analytic bound |D_V|<=B_V and its logarithmic estimate hold, the draft's deduction limsup log g/(n^2 log n)<=3/4 follows. Together with log(A_b^2)=(1/4)n^2 log n+O(n^2), it gives the conditional upper limit 1/2 for the normalized residual content. The factorial asymptotic itself follows by summing log(j!), with b=floor(n/2).

Accordingly the former strict target above 1/2 is not promoted as an attainable remaining objective. The combined Gaussian-bound estimates and comparison of B_W with B_V belong to Agent 2's audit; this review does not independently certify those analytic inputs. Valid exact content divisibility is compatible with a vacuous sufficient shrinking criterion. A lower bound on a chosen upper-bound expression is not a lower bound on the actual primitive form.

No additional recurrence, new nonvanishing result, or replacement shrinking estimate is certified here.

## 7. Real execution and evidence

The saved check_growing_content_scales.py was inspected and preserved unchanged. Its application execution returned exit code 0, sandboxed=true, and PASS_FORMAL_ARITHMETIC. All 12 checks passed: endpoint X/Y, partial-row X/Y, monic cleared scale, rational gcd scale, both endpoint-clearer identities, three b=2 contractions, and the b=1 empty-minor convention. The real output was saved as growing_content_scale_stdout.txt; the certificate is growing_content_scale_checks.json.

These formal calculations supplement the all-size proofs above. They do not computationally prove unrestricted integrality or rank. Although some symbolic variables in the saved script carry nonzero assumptions, the verified rational identities extend wherever their displayed denominators are defined, by clearing denominators; zero contraction values are covered by the paper argument.

Agent 1's check_growing_degree_arithmetic.py and growing_degree_arithmetic_certificate.json were inspected in the preceding audit context. Their 18 reported checks were not represented as a fresh rerun. The independent execution here is the separate 12-check program. No execution failure occurred in this resumed growing-content check. The earlier b=2 file search failed because rg was absent; it was replaced then and is unrelated to this execution. An unfinished operation was not an access failure.

Source dependencies: the assigned Agent 1 arithmetic document and symbolic artifacts; GROWING_CONTENT_CRITERION_DRAFT.md for the specified monic scale; GROWING_FACTORIAL_CONTENT_DRAFT.md; GROWING_BOUND_OBSTRUCTION_DRAFT.md; agent2/PROOF_DRAFT.md for the exact reduced-system convention; and the previously read September 13 contiguous endpoint source/review and September 27 Rodrigues contraction sources. The completed b=1 and b=2 audits supply only their explicitly checked compatibility conventions.

All new files are under work/session_20261001_astra/agent4/. Reviewed and completed family files were not modified. No network, installation, external path, new prime scan, or new canonical degree scan was used.
