> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Three consecutive zero index-Hensel digits for the Bessel denominator

Checked: 2026-08-27 UTC.

## 1. Theorem

Let



$$
q_0=q_1=1,\qquad q_n=(4n-2)q_{n-1}+q_{n-2}.
\tag{1}
$$



There is an exact integer $n_3$ on the ordinary $7$-adic index-root
branch through $2$ such that



$$
7^{1167}<n_3<7^{1168},
 \qquad
 v_7(q_{n_3})=1171,
 \qquad
 {q_{n_3}\over7^{1171}}\equiv1\pmod7.
\tag{2}
$$



Its decimal expansion has $987$ digits and SHA-256 digest

    b99aaafbf4474e3956ff60ff74039eadd8df1e384894725c01481f5528ebc8f4

and is stored exactly in the companion JSON.  For completeness, the exact
integer is

    756802081867351982204451880554288071372661809387728506437223003807921305001531327850791372970568236738039269463551121587659762466697025131751747386425314510022501248091390490254910243153397622842631947544945105455555167541116997051854319779700562468279231661109672707626186222729132787790172820015411884497288138968007428827195209890220011879606528681347680177711651451208784368084187621995157410375476545693501243461606979342522148757496590562296108929649686894530606864701937313469464285117803962870511668050942541393380291389143345921647004017647768179615176200380011740237499060386655568238207690456588020880017061093834650567265572503602612869614465025172879311948222773343533570503735606401553440822468974526317736217626926401369808061492116730577270964040751089418069810166878648649788255737899233592072253452313622878623041551026124325386211328995026509361063647117890796072612864887581297684824047649317050437834859644201449494370301768729581294368437600130737150198513243339206

The least representative has $1168$ base-$7$ digits.  In the convention
that $d_a$ lifts from modulus $7^a$ to modulus $7^{a+1}$, the compatible
branch digit window surrounding the last digit of this representative is



$$
(d_{1165},\ldots,d_{1171})=(1,3,4,0,0,0,4).
\tag{3}
$$



Thus



$$
d_{1168}=d_{1169}=d_{1170}=0
\tag{4}
$$



are three consecutive zero Hensel digits.  In particular, not only



$$
v_p(q_n)\leq1+\lceil\log_p n\rceil,
\tag{5}
$$



but also its fixed additive repair



$$
v_p(q_n)\leq2+\lceil\log_p n\rceil
\tag{6}
$$



is false.

This is a finite exact counterexample.  It does not prove that zero-run
lengths are unbounded, and it does not disprove



$$
V_N(C)=o(N\log N).
\tag{7}
$$



## 2. Rigorous modular evaluation

Put $f(n)=(-1)^nq_n$ and $A_j=\Delta^jf(0)$.  The proved Mahler
identities are



$$
f(x)=\sum_{j\geq0}A_j\binom{x}{j},
\tag{8}
$$





$$
A_{j+2}=-4(j+2)A_{j+1}-(8j+6)A_j-4jA_{j-1},
\tag{9}
$$



and



$$
{j!\over\lfloor j/2\rfloor!}\mid A_j.
\tag{10}
$$



For every $j\geq16437$,



$$
\begin{aligned}
 v_7(A_j)
 &\geq
 \left\lfloor{j\over7}\right\rfloor
 -\left\lfloor{\lfloor j/2\rfloor\over7}\right\rfloor\\
 &\geq {j\over14}-1>1172.
 \end{aligned}
\tag{11}
$$



Consequently the infinite Newton series modulo $7^{1172}$ has the
rigorous finite cutoff



$$
f(n_3)\equiv
 \sum_{j=0}^{16436}A_j\binom{n_3}{j}
 \pmod {7^{1172}}.
\tag{12}
$$



Exact modular arithmetic gives



$$
f(n_3)\equiv7^{1171}\pmod {7^{1172}}.
\tag{13}
$$



The integer $n_3$ is even, so $f(n_3)=q_{n_3}$, proving $(2)$.
Moreover,



$$
f(n_3+4\cdot7^{1171})\equiv0\pmod {7^{1172}},
\tag{14}
$$



which checks the next digit and its orientation.  Finally 

$$
n_3\equiv2
\pmod7
$$

, while



$$
\delta_7(2)={-q_9-q_2\over7}\equiv5\pmod7,
\tag{15}
$$



so this is the ordinary branch through $2$, not a singular lift.

## 3. Certificate and scope

The companion script

    scripts/bessel_padic_index_triple_zero_counterexample_certificate.py

checks $(2)$--$(4)$ and $(12)$--$(15)$ exactly.  It constructs all
$16437$ required Mahler coefficient residues from $(9)$, checks the
closed formula and the finite-difference definition independently through
index $120$, evaluates the Newton sum by tracking the $7$-unit and
valuation of every binomial coefficient, and records a hash of the full
coefficient-residue vector.

The all-index input is the proved recurrence and divisibility in
$(9)$--$(11)$; the calculation is therefore a proof of this particular
counterexample, not an extrapolation from a finite search.  No bounded or
unbounded run-length theorem follows merely from $(3)$.

Nothing in this note proves irrationality or transcendence of $e+\pi$.
