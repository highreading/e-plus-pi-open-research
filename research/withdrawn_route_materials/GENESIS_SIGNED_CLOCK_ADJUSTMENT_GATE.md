> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Signed rational clock adjustment: explicit operation, classical gate, and scope

Status: the proposed subdivision operation is discarded as a Genesis obstruction. Its essential tangent/Machin addition mechanism is already public. The exact lemmas below concern the actual exponential and circular laws and may be reused as elementary background; no mechanism-level novelty, rationality decision, or stopping condition is claimed.

## Operation on actual source laws

For a finite word w=(t_1,...,t_l) of rational numbers, use the actual real principal arctangent at every entry and define

    T(w)=sum_j t_j,
    C(w)=4 sum_j atan(t_j),
    Phi(w)=(product_j exp(t_j), C(w))=(exp(T(w)), C(w)).

Concatenation multiplies the first component and adds the second. Thus this is a nonadditive operation on the pair of actual defining laws. Negating every letter negates both T and C and inverts the exponential component. No angular branch is reset during concatenation: C is the full real sum.

The singleton word (1) has Phi=(e,pi). Any word with T=1 and C=pi gives the same numerical trace exp(T)+C=S. Consequently a rationality assumption S in Q applies exactly to that trace, but does not imply rationality of the separate contributions or of traces of arbitrary words.

The prospective route was to constrain rational targets by an incompatibility of rational refinements preserving the two laws. The following explicit operation shows that signed rational refinement is substantially flexible. It supplies no such incompatibility.

## Exact rational adjustment lemma

For each integer d>=1 put D_d=4d^2-1 and define the rational three-letter block

    B_d=(1/(2d), 1/(2d), -4d/D_d).

Then

    C(B_d)=0,
    T(B_d)=-1/(d D_d).

Proof. Set a=1/(2d). We have 0<a<=1/2, hence 0<2 atan(a)<pi/2. The tangent double-angle formula gives

    tan(2 atan(a))=2a/(1-a^2)=4d/D_d.

The indicated interval fixes the principal branch, so atan(4d/D_d)=2 atan(a). This proves the zero circular increment. Direct rational arithmetic gives

    1/d - 4d/D_d = -1/(d D_d).

It follows that for EVERY rational r=p/d, with integer p and d>=1, there is a finite rational word J_r satisfying

    T(J_r)=r,  C(J_r)=0,  Phi(J_r)=(exp(r),0).

If p>0, concatenate p D_d copies of -B_d. If p<0, concatenate |p| D_d copies of B_d. For p=0 use the empty word. The resulting word has length at most

    3 |p| (4d^2-1).

This is a finite exact construction, not a numerical experiment. A more efficient construction is not needed for this lemma. Appending J_r to any word adjusts its exponential time by r without changing its full circular increment. In particular, any rational-argument angular representation with rational ordinary time can be adjusted to any other rational ordinary time. Under a rational S this does NOT force a second algebraic synchronized replica or any other algebraic output.

## A nontrivial simultaneous refinement and a three-letter limit

The 34-letter word

    w=(1, B_1, ten copies of -B_2)

has T(w)=1 and C(w)=pi, because T(B_1)=-1/3 and T(-B_2)=1/30. Explicitly its multiplicities are

    1:1,  1/2:2,  -4/3:1,  -1/4:20,  8/15:10.

Its total time is exactly 1; its circular increment is exactly pi. It contains no pair t,-t. Therefore the refinement is not merely deletion of opposite letters. It still reproduces only the same numerical pair (e,pi) and the same trace S.

For comparison, three letters are rigid in the following elementary sense. If real x,y,z satisfy

    x+y+z=1,   atan(x)+atan(y)+atan(z)=pi/4,

then their multiset is {1,t,-t} for some real t. Conversely every such multiset satisfies the two identities.

To prove necessity, multiply (1+ix)(1+iy)(1+iz). Its real and imaginary parts are 1-e_2 and e_1-e_3, where e_j are the elementary symmetric polynomials. The exact angular identity makes these two parts equal; e_1=1 therefore gives e_2=e_3. With z=1-x-y, direct factorization yields

    e_2-e_3=(x+y)(1-x)(1-y).

Thus x+y=0, x=1, or y=1, which gives the asserted multiset. The converse uses the oddness of the principal arctangent. No claim about a minimum length between 4 and 33 is made.

## Archive and fresh primary gate

The initial broad archive query included `Machin`, which also matched the substring in `machinery` and produced truncated output. That output is not described as a complete examined search. The narrowed complete filename search used `zero.angle|zero angle|arctan.*sum of arguments|signed.*subdivision|simultaneous.*subdivision|tangent addition` in Markdown under the inherited archive. It located, among other files, the current stage's `agent3_analysis/GENESIS_TWO_LAW_TRANSPORT_COMMUTATOR_GATE.md`.

That file was read for the mechanism boundary, not independently audited. Its exact exponential/circular transport laws and finite-word telescope section already distinguish preserved source laws from an absent numerical arithmetic closure consequence. The older archive also has a substantial endpoint-matched Machin route. No approximation or endpoint-content work is reopened here.

Fresh queries were:

- `"arctangent" "identities" "rational" "Machin" arxiv`
- `"arctangent" "sum of arguments" identities`
- `"tangent addition" "rational" "zero" identities`

Opened primary paper: Marco Abrate, Stefano Barbero, Umberto Cerruti and Nadir Murru, *Writing pi as sum of arctangents with linear recurrent sequences, Golden mean and Lucas numbers*, https://arxiv.org/abs/1409.6455 and the full PDF https://arxiv.org/pdf/1409.6455. Section1, especially the rational operation (x+y)/(1-xy), its branch correction, and the matrix/recurrence construction of exact angular words, was inspected. These are the essential public addition and rational-word operations used by the present blocks. The exact rational-time adjustment formula above is proved directly here; it is not attributed as a stated theorem of that paper. An attempted MDPI full-page open returned an internal error and is not claimed as a read. Secondary search hits supply no mathematical claims in this note.

Gate conclusion: the proposed obstruction through rational source-preserving subdivision uses a public essential mechanism and is discarded promptly. The absence of an exact public match to the particular time-adjustment formula is NOT a global novelty claim. The formula is elementary support derived from a classical addition law.

## Honest limit of the arithmetic bridge

The adjustment operation can preserve the original trace S, or can change the exponential time while holding the angle fixed. The first case gives no new arithmetic relation. The second case is not known to preserve algebraicity of the trace. For instance, the saved synchronized replication lemma says that under S algebraic, all e^m+m pi with m>=2 are transcendental, rather than algebraic.

No inference from equality of the total trace to a structural equivalence, finite quotient, or arithmetic closure of all words is asserted. No contradiction to S in Q has been produced. Research continues toward a different operation; the current note is a bounded exact checkpoint, not a closeout.
