> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The exceptional fixed-$(b,c)=(1,1)$ endpoint indices: exact next digits

## Status

This note continues Proposition 6.1 of
`machin_endpoint_asymptotics.md`.  It does three things.

1. It gives an exact finite-precision formula which determines the endpoint
   valuation whenever the first nonzero $239$-adic digit occurs before any
   of the regular terms can intervene.
2. It proves that there are exactly two leading-residue exceptions among all
   positive odd $N<239^3$, and it determines the endpoint valuation at both
   of them from the next digit.
3. It derives a recurrence which proves an $N-O(\log N)$ denominator
   exponent for at least one member of every adjacent pair $\{N,N+2\}$, for
   all sufficiently large odd $N$.  The recurrence does **not** prove the
   desired pointwise statement at every exceptional index.

All computations in this note are exact integer or modular computations.
The accompanying script is
`scripts/machin_fixed_bc1_exceptional_digits.py`, and its generated record is
`results/machin_fixed_bc1_exceptional_digits.json`.

## 1. Exact normalization of every further $239$-adic digit

Put $p=239$,



$$
s_r=(-1)^{(r-1)/2}\quad(r\text{ positive and odd}),\qquad
 D_N=N^2+N-1.
$$



In equation (67) of the source note, separate the terms containing a negative
power of $p$.  Since



$$
g_r=s_r\left(\frac{16}{r5^r}-\frac4{rp^r}\right)
 \quad(r\text{ positive and odd}),
$$



the two occurrences of $g_N$ combine exactly as follows:



$$
-g_N-\frac{g_N}{D_N}
 =-\frac{16s_N(N+1)}{D_N5^N}
  +\frac{4s_N(N+1)}{D_Np^N}.
$$



Consequently the endpoint ratio $R_N=A(1)/B(1)$ has the exact decomposition



$$
R_N=4h_N+Q_N,                                      \tag{1}
$$



where



$$
h_N=
 \sum_{\substack{1\le r<N\\r\ {\rm odd}}}\frac{s_r}{rp^r}
 +\frac{s_N(N+1)}{D_Np^N},                         \tag{2}
$$



and $Q_N$ contains the $5$-power arctangent terms and the two factorial
terms, but no negative power $p^{-r}$ coming from the arctangent series.

As in Proposition 6.1, define



$$
a=v_p(N+1),\qquad d=v_p(D_N),\qquad
 W_*=N-a+d,
$$





$$
w(r)=r+v_p(r),\qquad
 W=\max\left(W_*,\max_{1\le r<N,\ r\ {\rm odd}}w(r)\right).       \tag{3}
$$



For each earlier $r$, write $e_r=v_p(r)$ and $u_r=r/p^{e_r}$; also
write $U=(N+1)/p^a$ and $V=D_N/p^d$.  Multiplying (2) by $p^W$ gives
the following exact element of $\mathbf Z_{(p)}$:



$$
\boxed{
 \Sigma_N:=p^Wh_N=
 \sum_{\substack{1\le r<N\\r\ {\rm odd}}}
 s_rp^{W-r-e_r}u_r^{-1}
 +s_Np^{W-W_*}UV^{-1}.}                           \tag{4}
$$



Reduction of (4) modulo $p$ is precisely the residue $\mathcal C_N$ in
(75).  More generally, modulo $p^k$ only the earlier indices satisfying



$$
W-w(r)<k                                              \tag{5}
$$



and, when $W-W_*<k$, the final term need be retained.  Formula (5) is a
rigorous finite computation: since $v_p(r)\le\lfloor\log_p(N-1)\rfloor$,
all relevant $r$'s lie in an interval of length
$k+O(\log N)$ immediately below $N$.

It remains to make sure that a digit found in (4) cannot be cancelled by
$Q_N$.  Put



$$
L=\lfloor\log_pN\rfloor,
 \qquad f=v_p((N+1)!),
 \qquad b=v_p(N+2),                                  \tag{6}
$$



and define



$$
\boxed{
 \Gamma_N=\min\{W-L,\ W+a-d,\ W-f,\ W-f-d+b\}.}    \tag{7}
$$



The four entries in (7) respectively bound, after multiplication by $p^W$,
the earlier $5$-power arctangent terms, the combined final $5$-power
term, the exponential partial sum, and the final $D_N(N+1)!$ term.  Thus



$$
v_p(p^WQ_N)\ge\Gamma_N.                            \tag{8}
$$



This proves the exact next-digit criterion.

**Lemma 1.1.**  Suppose an exact calculation modulo $p^k$ gives
$t=v_p(\Sigma_N)<k$.  If $t<\Gamma_N$, then



$$
\boxed{v_p(R_N)=-W+t.}                             \tag{9}
$$



If the reduced endpoint pair is $(\alpha_N,\beta_N)$ and $W-t>0$, then



$$
\boxed{v_p(\beta_N)=W-t.}                         \tag{10}
$$



**Proof.**  The modular computation fixes the valuation of (4) at $t$.
Equations (1) and (8), together with the fact that $4$ is a $p$-adic
unit, show that the singular summand has strictly smaller valuation than the
regular remainder.  This proves (9).  Equation (10) follows by reducing the
rational endpoint ratio to coprime numerator and denominator. $\square$

## 2. Complete classification below $239^3$

The classification in this section is a proof, rather than an inference from
the exhaustive computation.  Let $N$ be positive, odd, and $N<p^3$.
Every earlier index has $v_p(r)\le2$.  If $\delta=N-r$, then $\delta$
is a positive even integer and



$$
w(r)=N-\delta+v_p(r)\le N.                        \tag{11}
$$



Also, $a\le2$: because $p^3$ is odd, an odd $N<p^3$ satisfies
$N+1\le p^3-1$.  The congruences $p\mid N+1$ and $p\mid D_N$ are
mutually exclusive, because $N\equiv-1\pmod p$ gives
$D_N\equiv-1\pmod p$.

There are four cases.

* If $d>0$, then $a=0$ and $W_*=N+d>N$, so the final term is unique.
* If $a=1$, then $d=0$ and $W_*=N-1$.  A unit earlier term is at most
  $N-2$.  An exact-valuation-one term could tie only with $r=N-2$, but
  $N-2\equiv-3\pmod p$; an exact-valuation-two term would need the even
  gap $\delta\le2$ to tie or dominate and is ruled out by the same
  congruence.  Thus the final term is unique.
* If $a=2$, write

  

$$
N=p^2u-1,\qquad 2\le u\le238,\quad u\text{ even}.                 \tag{12}
$$



  Here $W_*=N-2$, and exactly one earlier term ties it: $r=N-2$, which
  is a $p$-adic unit.  Indeed a $p$-divisible earlier term would have
  an even gap $\delta\equiv-1\pmod p$, hence $\delta\ge238$, whereas
  its valuation is at most two.  Modulo $p$, the two tying terms sum, up
  to the unit sign $s_{N-2}$, to

  

$$
u-\frac13.                                        \tag{13}
$$



  Hence it vanishes exactly when $u\equiv1/3\equiv80\pmod p$.
* If $a=d=0$, then $W_*=N$.  An earlier term ties the final term only
  when $r=N-2$ has valuation two, so

  

$$
N=p^2u+2,\qquad 1\le u\le237,\quad u\text{ odd}.                  \tag{14}
$$



  Up to the unit sign $s_{N-2}$, the leading residue is

  

$$
\frac1u-\frac35.                                  \tag{15}
$$



  It vanishes exactly when $u\equiv5/3\equiv161\pmod p$.

Thus there are exactly two exceptions in the complete range:



$$
\boxed{
 \begin{aligned}
 N_B&=p^2\cdot80-1=4\,569\,679,\\
 N_A&=p^2\cdot161+2=9\,196\,483.
 \end{aligned}}                                     \tag{16}
$$



There are 119 ties of the form (12) and 119 of the form (14).  The exact
exhaustive script independently checks all 6,825,959 positive odd indices in
this range and finds these 238 ties and only the two zeros in (16).

## 3. The certified next digit at both exceptions

At $N_A$, one has $W=N_A$.  Modulo $p^2$, only $r=N_A-2$ and the
combined final term survive in (4); the next candidate gaps are $4$ and
$479$.  Direct exact modular arithmetic gives



$$
\begin{aligned}
 4\Sigma_{N_A}
 &\equiv4s_{N_A-2}\frac{p^2}{N_A-2}
       +4s_{N_A}\frac{N_A+1}{D_{N_A}}\\
 &\equiv36\,328=152p\pmod{p^2}.                    \tag{17}
 \end{aligned}
$$



Without the suppressed common factor $4$, the residue is
$9\,082=38p\pmod{p^2}$.  Therefore $v_p(\Sigma_{N_A})=1$.  The exact
regular gap is



$$
\Gamma_{N_A}=9\,157\,843>1.                       \tag{18}
$$



Lemma 1.1 now proves



$$
\boxed{
 v_p(R_{N_A})=-N_A+1=-9\,196\,482,
 \qquad v_p(\beta_{N_A})=N_A-1=9\,196\,482.}       \tag{19}
$$



At $N_B$, one has $W=N_B-2$.  Again only the two leading terms survive
modulo $p^2$; the next candidate gaps are $2$, $235$, and $57\,116$.
Here



$$
\begin{aligned}
 4\Sigma_{N_B}
 &\equiv4s_{N_B-2}\frac1{N_B-2}
       +4s_{N_B}\frac{80}{D_{N_B}}\\
 &\equiv19\,359=81p\pmod{p^2}.                    \tag{20}
 \end{aligned}
$$



Without the factor $4$, the residue is $19\,120=80p\pmod{p^2}$.  Since



$$
\Gamma_{N_B}=4\,550\,477>1,                       \tag{21}
$$



Lemma 1.1 proves



$$
\boxed{
 v_p(R_{N_B})=-N_B+3=-4\,569\,676,
 \qquad v_p(\beta_{N_B})=N_B-3=4\,569\,676.}       \tag{22}
$$



These two leading cancellations therefore lose only one power of $239$.

## 4. A further rigorous exception beyond the scanned range

The two indices in (16) are not the whole exceptional set.  A useful general
tie pattern is



$$
N=p^eu+e,\qquad r=N-e=p^eu,                       \tag{23}
$$



with $e$ even.  Provided the displayed term and the final term attain
$W=N$, their leading residue cancels when



$$
u\equiv(-1)^{e/2+1}\frac{e^2+e-1}{e+1}\pmod p,   \tag{24}
$$



assuming the denominator and numerator in (24) are $p$-adic units.  This
follows immediately from
$s_N/s_{N-e}=(-1)^{e/2}$, $N\equiv e\pmod p$, and (4).

For $e=4$, equation (24) gives $u\equiv-19/5\equiv44\pmod p$.  Taking
$u=283$ gives the odd index



$$
N_C=p^4\cdot283+4=923\,374\,845\,407.             \tag{25}
$$



At this specific index, direct comparison of the largest exact-valuation
candidates proves $W=N_C$; the tying earlier term is $r=N_C-4$, of exact
valuation four.  For exact valuations $e=0,1,2,3,4,5$, the respective gaps
$W-w(r_e)$ of the largest candidates are



$$
2,\ 481,\ 114\,244,\ 27\,303\,839,\ 0,
 143\,563\,580\,203.
$$



There is no exponent $e\ge6$, because $p^6>N_C$.  Thus the dominance
comparison is exhaustive.  Here $s_{N_C-4}=s_{N_C}=-1$, while
$N_C-4=p^4\cdot283$, $N_C+1\equiv5\pmod{p^2}$, and
$D_{N_C}\equiv19\pmod{p^2}$.  Hence, modulo $p^2$,



$$
\Sigma_{N_C}\equiv-283^{-1}-5\cdot19^{-1}
 \equiv2\,868=12p\pmod{p^2},
$$



and therefore



$$
4\Sigma_{N_C}\equiv11\,472=48p\pmod{p^2}.         \tag{26}
$$



The regular gap is



$$
\Gamma_{N_C}=919\,495\,119\,166>1.                \tag{27}
$$



Therefore this is a third rigorous leading exception, with



$$
\boxed{v_p(\beta_{N_C})=N_C-1=923\,374\,845\,406.}\tag{28}
$$



Equation (24) is only a tie-and-first-residue calculation.  It is not being
asserted here that every admissible $e$ automatically makes the two shown
terms dominant; that must be checked in each use, as it was for (25).

## 5. Congruence strata for $N$, $N+1$, and $D_N$

For an earlier candidate of exact valuation $e$, let $r_e$ be the
largest positive odd $r<N$ with $v_p(r)=e$, and put
$\delta_e=N-r_e$.  Then



$$
W-N=\max\left(d-a,\max_e(e-\delta_e)\right).       \tag{29}
$$



This is a convenient exact description of all possible leading strata.  It
also gives $W=N+O(\log N)$, since $a,d,e=O(\log N)$ and there is always
an odd $p$-unit among $N-2,N-4$.

The two roots of $D_N$ modulo $239$ are



$$
N\equiv15,223\pmod{239}.                           \tag{30}
$$



They are simple roots.  If $d>0$, then $a=0$.  For a $p$-divisible
earlier index, $\delta_e\equiv N\pmod p$ and $\delta_e$ is even.  The
smallest positive even representatives of the two classes in (30) are 254
and 462.  It follows, for example, that whenever
$\lfloor\log_p(N-1)\rfloor<255$, a $D_N$-divisible final term is strictly
dominant: no earlier exponent $e\le254$ can compensate for its positive
$d$.  This explains why the $D_N$ stratum creates no hidden exceptions
in the range of Section 2.

If $a>0$, then $N\equiv-1\pmod p$, $d=0$, and the smallest positive
even $\delta\equiv-1\pmod p$ is 238.  In the range $N<p^3$, this leaves
only the unit candidate $r=N-2$, producing exactly the $a=2$ family in
(12).  At much larger indices, (29) shows why higher exact-valuation strata
must also be considered.

## 6. A rigorous adjacent-pair theorem

There is a useful recurrence which controls two consecutive odd indices, but
not either specified index separately.  Define



$$
S_N=\sum_{\substack{1\le r<N\\r\ {\rm odd}}}\frac{s_rp^{N-r}}r,
 \qquad
 F_N=S_N+s_N\frac{N+1}{D_N}.                       \tag{31}
$$



Then $h_N=p^{-N}F_N$.  Since $s_{N+2}=-s_N$,



$$
S_{N+2}=p^2S_N+s_N\frac{p^2}{N}.                 \tag{32}
$$



Using



$$
\frac1N-\frac{N+1}{D_N}=-\frac1{ND_N},           \tag{33}
$$



one obtains the exact recurrence



$$
\boxed{F_{N+2}=p^2F_N-s_NH_N,}                   \tag{34}
$$



where



$$
H_N=\frac{p^2D_{N+2}+N(N+3)D_N}
            {ND_ND_{N+2}}.                        \tag{35}
$$



The numerator in (35) is the positive integer



$$
P_N=N^4+4N^3+(p^2+2)N^2+(5p^2-3)N+5p^2.         \tag{36}
$$



Put $B_N=\lfloor\log_pP_N\rfloor$.  Since the denominator of (35) is an
integer,



$$
v_p(H_N)\le v_p(P_N)\le B_N=O(\log N).           \tag{37}
$$



Use the convention $v_p(0)=+\infty$.  The quantity $H_N$ is nonzero
because its numerator $P_N$ is positive, so (34) prevents $F_N$ and
$F_{N+2}$ from both vanishing.  If either one vanishes, (34) directly makes
the valuation of the other displayed term equal to $v_p(H_N)\le B_N$.
If both $v_p(F_N)+2$ and $v_p(F_{N+2})$ were greater than $B_N$,
equation (34) would force $v_p(H_N)>B_N$, contradicting (37).  Hence



$$
\boxed{
 \min\{v_p(F_N)+2,\ v_p(F_{N+2})\}\le B_N.}       \tag{38}
$$



The regular part in (1), now scaled by $p^N$, has valuation at least



$$
G_N=\min\{N-L,\ N+a-d,\ N-f,\ N-f-d+b\}.         \tag{39}
$$



Legendre's formula gives $f\le(N+1)/(p-1)$, whereas
$a,d,L=O(\log N)$.  Thus $G_N$ and $G_{N+2}$ eventually exceed
$B_N$.  Combining (38), (39), and (1) proves:

**Adjacent-pair proposition.**  For every sufficiently large odd $N$, at least one
$j\in\{N,N+2\}$ satisfies



$$
\boxed{v_p(\beta_j)\ge j-B_N=j-O(\log N).}        \tag{40}
$$



This proposition includes exceptional indices and is unconditional.

## 7. Exact unresolved obstruction

Equation (38) permits an isolated index with very large $v_p(F_N)$, flanked
by controlled neighbors.  At such an index, the preceding recurrence merely
says that



$$
p^2F_{N-2}\equiv-s_NH_{N-2}\pmod{p^k}             \tag{41}
$$



to the relevant precision; it does not prevent this congruence from holding
for $k$ much larger than $\log N$.  The first-residue exceptions (16) and
(25) show that nontrivial cancellation strata genuinely occur.  Their next
digits happen to be units after one lost power, but finite examples cannot
establish a uniform all-index bound.

Therefore the precise pointwise question



$$
v_p(\beta_N)\ge N-O(\log N)\quad\text{for every odd }N             \tag{42}
$$



remains unresolved by this method.  What is now proved is the exact
finite-precision criterion (Lemma 1.1), the complete range
$N<239^3$, the three certified exceptional valuations (19), (22), and
(28), and the adjacent-pair theorem (40).
