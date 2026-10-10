> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Cubic squarefreeness: exact coefficient reduction and remaining dyadic gates

Date: 2026-09-13. Bounded original continuation by audit_results.

This note derives all four accessory coefficients from a bounded
number of actual leading coefficients and separates two attainable
targets: excluding a triple root, and proving full squarefreeness.
Neither all-index target is proved here. Existing exact controls
show that the simple distinct-Newton-slopes argument at n=1 does
not persist in the saved even degrees.

## 1. Archive and closed exact controls

Inspected inputs were raw_all_index_cubic_gate.md,
raw_hp_homogeneous_ode.md, raw_hp_origin_finite_jets.md,
raw_accessory_scaling_and_compactness.md, its saved JSON,
and the completed leading-B and Xi valuation notes. The all-index
gate proves q_3=b_n Xi_n!=0 with exact valuation, but does not
provide valuations of the other three accessory coefficients.
The origin note expressly allows Q(0)=0 and Taylor order greater
than3n+1. Those exceptions cannot be silently excluded here.

The only exact controls used are the already saved n=2,4,8,16
cases in raw_accessory_scaling_probe.json, together with the
previously computed n=1 cubic. No new degree, canonical solve,
branch-coefficient scan, or spectral-root scan was performed.

For n=1, the primitive cubic divided by4 is
−464z³−1746z²−2697z+1403. Its coefficient valuations, in ascending
degree, are [0,0,1,4]. The lower Newton polygon has three
length-one edges, of distinct slopes0,1,3. Its three roots have
distinct valuations, proving squarefreeness in this single case.

For the saved **monic** even cubics the exact data are:

| n | v2(q0/q3), v2(q1/q3), v2(q2/q3), 0 | v2 Disc(Q/q3) |
|---:|---|---:|
| 2 | [3,0,1,0] | 3 |
| 4 | [2,0,1,0] | 4 |
| 8 | [3,0,1,0] | 5 |
| 16 | [4,0,1,0] | 6 |

Each of these polygons has vertices (0,v2(q0/q3)),(1,0),(3,0).
The horizontal edge has length2 and residual polynomial z²+1
over F_2, with a repeated root. Thus these controls have two
unit roots not separated by the first Newton polygon. Their
already certified characteristic-zero squarefreeness does not
follow merely from the displayed slopes.

## 2. A polynomial containing the needed cross-minors

Use the actual triple A,B,C of degree at most n, in any common
nonzero rational scale, and put D=1+z². Define the polynomial



$$
\boxed{P(z)=D(A'C-AC')+C^2.}                       \tag{1}
$$



It has degree at most2n. Let H=A+C(F−F_infinity), where the formal
Laurent expansion of arctan at infinity is
F−F_infinity=−z^(−1)+z^(−3)/3−z^(−5)/5+.... Then



$$
K:=H'C-HC'=(A'C-AC')+C^2/D=P/D.
\tag{2}
$$



Write B=b_0 z^n+b_1 z^(n−1)+b_2 z^(n−2)+b_3 z^(n−3)+...,
where b_j means the coefficient counted down from the leading
degree n, not the usual ascending index. Missing coefficients are
zero. Similarly write



$$
K=\kappa_0z^{2n-2}+\kappa_1z^{2n-3}
                  +\kappa_2z^{2n-4}+\kappa_3z^{2n-5}+\cdots.
\tag{3}
$$



If p_j=[z^(2n−j)]P, then



$$
\kappa_0=p_0,\quad\kappa_1=p_1,
\quad\kappa_2=p_2-p_0,\quad\kappa_3=p_3-p_1.
\tag{4}
$$



Thus these four quantities use an ordinary polynomial, with no
truncation or convergence assumption for the formal arctangent.

For explicit cross-minors, set a_j=[z^(n−j)]A and
c_j=[z^(n−j)]C. Define
h_0=a_0, h_1=a_1−c_0, h_2=a_2−c_1,
h_3=a_3−c_2+c_0/3, h_4=a_4−c_3+c_1/3.
These are the first five Laurent coefficients of H. Direct
differentiation gives



$$
\begin{aligned}
\kappa_0&=h_0c_1-h_1c_0=\Xi_n,\\
\kappa_1&=2(h_0c_2-h_2c_0),\\
\kappa_2&=3(h_0c_3-h_3c_0)+(h_1c_2-h_2c_1),\\
\kappa_3&=4(h_0c_4-h_4c_0)+2(h_1c_3-h_3c_1).
\end{aligned}                                                     \tag{5}
$$



The factors1/3 in the intermediate h coefficients cancel as in(4);
in any event3 is a dyadic unit. For small n, Laurent h indices
beyond the polynomial degree remain meaningful, while missing
a_j,c_j are zero. Equations(4) provide a boundary-safe alternative.

## 3. Exact formulas for all four accessory coefficients

The identity



$$
e^{-z}W(H,Be^z,C)
=(B+2B'+B'')K-(B+B')K'-B L,
\quad L=H'C''-H''C',                              \tag{6}
$$



follows by expanding the determinant by its exponential column.
The first two Laurent coefficients of L are
−n(n−1)kappa_0 at degree2n−4 and
−n(n−2)kappa_1 at degree2n−5. This follows termwise from the
degrees n,n−1,n−2 of the two Laurent columns; the equal-degree
terms cancel. Multiply(6) by D²=z⁴+2z²+1 and divide by z^(3n−1).
The result is



$$
\boxed{\begin{aligned}
q_3={}&b_0\kappa_0,\\
q_2={}&b_0\kappa_1+(b_1+2b_0)\kappa_0,\\
q_1={}&b_0\kappa_2+(b_1+3b_0)\kappa_1
                              +(b_2+2b_0)\kappa_0,\\
q_0={}&b_0\kappa_3+(b_1+4b_0)\kappa_2
       +(b_2+b_1+2b_0)\kappa_1\\
     &+(b_3-2b_2+2b_1+4b_0)\kappa_0.
\end{aligned}}                                                     \tag{7}
$$



Every n-dependent derivative multiplier in(6) cancels in(7).
The q_2 formula is consistent with the previously known
q_2/q_3=beta+2gamma+2, since kappa_1/kappa_0=2gamma.
The q_1 and q_0 formulas supply the additional explicit leading
cross-minors needed for a discriminant or Newton-polygon argument.
These are exact all-index identities, not asymptotic expansions
in n and not merely formulas valid in generic root configurations.

## 4. A substantially weaker gate excluding only a triple root

For a cubic q_3 z³+q_2 z²+q_1 z+q_0, a necessary condition for
a triple root in characteristic zero is



$$
\mathcal H=q_2^2-3q_3q_1=0.                       \tag{8}
$$



Indeed a triple root gives q_2=−3q_3 r and q_1=3q_3 r².
The condition in(8), together with
2q_2³−9q_3q_2q_1+27q_3²q_0=0, is also sufficient for a triple
root. Nonzero mathcal H excludes a triple root but does not
exclude a double root.

An exact useful sufficient dyadic gate is therefore



$$
v_2(q_2/q_3)>0,\qquad v_2(q_1/q_3)=0.            \tag{9}
$$



Under(9), the two terms in mathcal H/q_3² have valuations at least2
and0. Hence mathcal H!=0. Formula(7) expresses the gate entirely
through actual bounded leading minors. For example the stronger
conditions



$$
\frac{b_1}{b_0},\frac{\kappa_1}{\kappa_0}\in4\mathbb Z_2,
\quad \frac{b_2}{b_0}\in2\mathbb Z_2,
\quad \frac{\kappa_2}{\kappa_0}\in\mathbb Z_2^\times
\tag{10}
$$



imply v_2(q_2/q_3)=1 and v_2(q_1/q_3)=0. These four conditions
hold in each saved even control, but they have not been proved
for every even n. The all-index leading-B and Xi theorems only
give the denominators b_0 and kappa_0; they do not establish the
new numerator gates in(10).

For reference, the exact Hessian coefficient reduction is



$$
\begin{aligned}
\mathcal H={}&b_0^2(\kappa_1^2-3\kappa_0\kappa_2)
 -b_0(b_1+5b_0)\kappa_0\kappa_1\\
&+(b_1^2+4b_0b_1-2b_0^2-3b_0b_2)\kappa_0^2.
\end{aligned}                                                     \tag{11}
$$



This can be tested by an actual dyadic cofactor expansion without
having to prove full squarefreeness first.

## 5. Full squarefreeness requires additional cancellation control

Write the monic cubic as z³+Bz²+Cz+D_0. Its discriminant is



$$
\Delta=B^2C^2-4C^3-4B^3D_0-27D_0^2+18BCD_0.
\tag{12}
$$



When v_2(B)=1 and C is a unit, the first two displayed terms both
have valuation2. They must be combined as



$$
B^2C^2-4C^3=4C^2[(B/2)^2-C].                    \tag{13}
$$



The saved data show why this cancellation cannot be ignored:

| n | v2((B/2)²−C) | v2(first pair combined) | v2(−27D0²) | v2(18BCD0) |
|---:|---:|---:|---:|---:|
| 2 | 1 | 3 | 6 | 5 |
| 4 | 2 | 4 | 4 | 4 |
| 8 | 12 | 14 | 6 | 5 |
| 16 | 5 | 7 | 8 | 6 |

At n=4 three contributions tie at the actual discriminant valuation.
At n=8 the nominal first pair has twelve extra powers before the
cross term supplies the actual leading valuation. The equal list
v_2 Delta=v_2(n)+2 in these four controls is not a proof of that
formula in other degrees.

A concrete sufficient noncancellation lemma, for any cubic rather
than an assumed actual-family theorem, is as follows. If a>=3 and



$$
v_2(B)=1,\quad v_2(C)=0,\quad v_2(D_0)=a,
\quad v_2((B/2)^2-C)\ge a+1,                     \tag{14}
$$



then the last term in(12) has valuation a+2, while the combined
first pair has valuation at least a+3, the D_0² term has valuation
2a>=a+3, and the B³D_0 term has valuation a+5. Therefore



$$
\boxed{v_2\Delta=a+2<\infty.}                    \tag{15}
$$



The saved n=8,16 cubics meet(14). Applying it in every degree
divisible by8 would require proving the actual four gates there;
no such assertion is made. Other valuation classes need their
own leading-residue analysis. In particular the a=2 case cannot
be included in this unique-lowest-term proof.

## 6. Exact obstruction and useful next arithmetic step

The most accessible new all-index target is the weaker Hessian
nonvanishing(8), using(10) or a direct leading residue in(11).
It would exclude an ordinary triple root everywhere and in
particular prove the translated-cubic three-integer carrier G
nonzero, without needing squarefreeness. The already proved
four-integer endpoint carrier remains nonzero independently of
that target.

The current leading-coordinate lemmas do not close(10). In
particular kappa_2 contains terms such as c_(n−1)² and c_n²
whose individual valuations can be much lower than the observed
valuation of kappa_2. Thus applying a triangle lower bound to
its separate terms loses the exact cancellations. The new
cross-minors in(5), or the top polynomial coefficients in(4),
must be treated coherently in the same style as the completed
Xi proof. A discriminant estimate has further cancellations
exhibited explicitly in(13).

These formulas supply a concrete bounded list of actual minors
and a smaller nonvanishing target. They do not prove an all-index
Newton polygon, root separation, nonzero discriminant, or a
primitive-denominator growth estimate.

### Subsequent exact improvement during this bounded task

raw_B_coefficient_dyadic_divisibility.md now proves
v_2(B_(n,j))>=phi(n)−phi(j) for every canonical coefficient.
Consequently for every even n, both b_1/b_0 and b_2/b_0 are even.
The weaker triple-root exclusion therefore needs only
kappa_1/kappa_0 even and kappa_2/kappa_0 a unit. Equivalently,
the next two coefficients below the leading one of
P=D(A'C−AC')+C² must both have strictly greater valuation than
its leading coefficient. Those two coherent cross-minor gates
remain unproved. This is a partial completion of the proposed
dyadic route, not an all-index squarefreeness claim.

Verification: check_raw_cubic_leading_coefficients.py and
raw_cubic_leading_coefficients_checks.json check(7) on the four
already saved exact triples, the symbolic Hessian identity(11),
and the displayed exact valuations. All checks pass. No new degree
or root was computed.
