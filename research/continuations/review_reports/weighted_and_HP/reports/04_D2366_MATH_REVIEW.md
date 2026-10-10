> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# D2366：hp_b2_cubic_maximal_minor_gate.md

Attribution：/root/organization_evidence

Mathematical verdict：**a valid all-depth local ideal theorem for large primes; no uniform bound on actual gcd depth is supplied**。

Original path：`work/session_20260927/hp_b2_cubic_maximal_minor_gate.md`

Original SHA-256: `7736790e3894ce58b43cc2810fca914c1e6a0f1e51029921ef4469817fe062b1`

Actual reading: complete source textL1–L279，9608characters，9608bytes; including status and dependencies, scope, and correction sections.

Copy of the original bytes：`[private local path removed]`

Existing primary review: review 27。

inherited primaryscope：All sections; p>2n+4 for valuation and endpoint assertions; polynomial identities themselves are universal; finite diagnostic claims not used

Specific source-text basis：

- L44–91: the equality for v_p(Omega) requires p>2n+4; actual endpoint depth only satisfies d_p<=v_p(Omega).
- L95–129: the raising/ODE/transition determinant is (n+1)^4/2; primitivity of the state is a local premise.
- L153–210: actual homogeneous elimination of the two minors and the unit-ideal conversion are correct.
- L222–270: the actual exceptional factor n^2+4n+1 in P(1) and the cutoff are retained. Simple Hensel lifting supplies no upper bound on depth.

Rederivation and valid usable conclusions：

Collecting cubic monomials directly gives uE+(nu+(n+2)h)D=-(n+1)C. The coefficients of h^3, h^2u, hu^2, and u^3 are respectively 2(n+1)(n+2), -4(n+1), -(n+1)(n-2), and -(n+1); every term containing v cancels. If h is a unit, subtracting (n+u/h) times the first column from the second reduces the minor ideal to (D,E). If u is a unit, this identity replaces it with (D,C); if u is not a unit, both are units. If h is not a unit, the primitive state and the values of the two minors/third minor ensure at least one unit. The all-depth formula therefore holds within the stated large-prime scope only.

The 11 formal-identity controls in B2_MAIN_FORMAL_CONTROL_RESULT.json and the actual primitive-kernel handoff in primary review 27 are reused. An additional local model takes n=2, p=11, h=1: f(u)=u^3+4u-8 has a simple root at u=7. Successive Hensel lifting to 11^6 and v=(6-2u-u^2)/u give D=0 with arbitrarily deep C. This model only shows that the local equations and separability cannot bound depth by themselves; it neither constructs an actual H_n nor refutes the source. Source lines 255–263 explicitly state this limitation.

Conditions of use and limits relative to the main goal：

- Every unit prefactor uses p>2n+4. A universal polynomial identity does not make its valuation conclusion universal at small primes.
- Large Omega does not imply a large actual endpoint gcd. A necessary condition cannot be reversed into a sufficient condition.
- A q rate still requires quantitative control of how closely the actual state approaches the cubic root, the depth of D, small primes, and complete endpoint content.

Definite errors in the text: none were found in this object's actual assertions in this batch. The counterexamples or proof obligations above are not registered as errors in this document.

Coordinates of independent exact small examples：

- [Complete results](../OWN_EXACT_INTERFACE_EXAMPLES.json#/b2_arbitrary_depth_synthetic_equation_states); pointer `/b2_arbitrary_depth_synthetic_equation_states`。

Program written by the reviewer：[check_interface_examples_owned.py](../check_interface_examples_owned.py)。
