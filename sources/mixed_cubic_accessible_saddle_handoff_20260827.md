> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Handoff: the mixed-cubic accessible saddle

Date: 2026-08-27.

Status: **unfinished research handoff, not a frozen theorem package**.  The
exact algebraic reductions below were checked symbolically in a scratch
SymPy session, and the numerical root/sign data were checked at high
precision.  The decisive Sturm signs have not yet been converted into a
replayable exact rational-interval certificate, so no coefficient
asymptotic is claimed here.

This note concerns equations (37)--(50) of
`sources/mixed_cubic_boundary_cartier_content_and_recurrence.md`.

## 1. Main simplification: a fixed circle appears to close the contour gap

Write



$$
\Psi(v)=\frac{(1+2v)^6(1+(1-i)v)^6}{v^4(1+v)^4},\qquad
 S(v)=4v^3+(6-i)v^2-iv-1-i.
$$



Let



$$
g(a)=128a^6-384a^5+280a^4-20a^3-55a^2+a+2.              \tag{H1}
$$



The smaller positive real root is



$$
a=0.209886201147898499701474253755\ldots,
 \qquad \rho=\sqrt a
 =0.458133387942745883976258263842\ldots.                 \tag{H2}
$$



Define



$$
\begin{aligned}
 x(a)&=-\frac{(4a+1)(16a^4-52a^3+49a^2-18a+1)}5,\\
 y(a)&= \frac{64a^5-208a^4+196a^3-67a^2-11a+5}5.
\end{aligned}                                               \tag{H3}
$$



Polynomial reduction modulo (g(a)) gives exactly



$$
x(a)^2+y(a)^2=a,
 \qquad S(x(a)+iy(a))=0.                                   \tag{H4}
$$



Thus



$$
\tau=x+iy
 =0.393343586940663786762530462701\ldots
  +0.234876613907283175916788717192\ldots,i               \tag{H5}
$$



lies on the circle (|v|=\rho).  Since (\rho<1/2), this circle
is a legitimate representative of both coefficient contours (I_0,I_2):
the only nonzero finite pole that matters for radial continuation is at
(-1), while the zeros at (-1/2) and (-(1+i)/2) cause no contour
obstruction (and in fact lie outside this circle).  Consequently, a strict
maximum theorem for (|\Psi|) on this one fixed circle is enough.  No
steepest-descent deformation across (-1) is needed.

## 2. Exact circle critical polynomial

Put (v=x+iy), (x^2+y^2=a), and



$$
A=1+4x+4a,\qquad B=1+2x+2y+2a,\qquad C=1+2x+a.
$$



On (|v|=\rho),



$$
|\Psi(v)|=\frac{A^3B^3}{a^2C^2}.                         \tag{H6}
$$



All three of (A,B,C) are positive because (\rho<1/2).  With
(x=\rho\cos\theta), (y=\rho\sin\theta), the numerator of the
angular logarithmic derivative of (H6) is



$$
D=-12yBC+6(x-y)AC+4yAB.                                  \tag{H7}
$$



Use (q=\tan(\theta/2)).  Direct expansion gives



$$
D=-\frac{2\rho}{(1+q^2)^3}P_\rho(q),                     \tag{H8}
$$



where



$$
\begin{aligned}
P_R(q)={}&R^4(12q^6+16q^5+12q^4+32q^3-12q^2+16q-12)\\
&+R^3(-36q^6-80q^5+20q^4+20q^2+80q-36)\\
&+R^2(39q^6+106q^5-89q^4-44q^3+89q^2+106q-39)\\
&+R(-18q^6-60q^5+50q^4+50q^2+60q-18)\\
&+(3q^6+14q^5+3q^4+28q^3-3q^2+14q-3).                    \tag{H9}
\end{aligned}
$$



The number (R=\rho) is the selected positive root of



$$
f(R)=128R^{12}-384R^{10}+280R^8-20R^6-55R^4+R^2+2.       \tag{H10}
$$



A symbolic Sturm sequence for (P_R) over (mathbb Q(R)) has degrees



$$
6,5,4,3,2,1,0.                                           \tag{H11}
$$



High-precision evaluation produced the following sign table:



$$
\begin{array}{c|c|c}
q&\text{Sturm signs}&V(q)\\ \hline
-\infty &(+,-,+,-,-,-,+)&4\\
-282    &(+,-,+,-,-,-,+)&4\\
-281    &(-,-,+,-,-,-,+)&3\\
11/40   &(-,+,+,+,+,-,+)&3\\
69/250  &(+,+,+,+,+,-,+)&2\\
+\infty &(+,+,+,+,-,+,+)&2.
\end{array}                                                \tag{H12}
$$



Numerically, the two real roots are



$$
q_-=-281.4419861561231\ldots,
 \qquad q_+=0.2758461130900741\ldots.                     \tag{H13}
$$



Moreover,



$$
\frac{y}{\rho+x}=q_+,
$$



so the positive root is precisely the point (\tau).

**Unfinished rigor point.**  The entries in (H12) still need exact sign
certification at the selected algebraic embedding.  The intended replay is:

1. isolate the root (R) of (H10) in a narrow rational interval around
   (0.45813338794274588), using a rational Sturm count for (f);
2. form the Sturm remainders of (H9) in (mathbb Q(R)[q]);
3. evaluate every numerator and denominator by exact rational interval
   Horner arithmetic (refining the isolating interval until zero is
   excluded);
4. reproduce (H12), and separately certify
   (y/(R+x)\in(11/40,69/250)).

The numerical margins in the Sturm evaluations are large.  For reference,
the leading-coefficient values of the seven normalized Sturm polynomials
were approximately



$$
1,\ 6,\ 10915.31,\ 8.20497,\ -1.0842495\cdot10^7,
 \ 2.14884,\ 2.1575837\cdot10^8.
$$



Once (H12) is exact, the circle has exactly two critical points.  The local
second derivative below makes (\tau) a strict local maximum; periodicity
then makes it the unique global maximum.

## 3. Local quadratic coefficient and determinant amplitude

For a local branch of (log\Psi), put



$$
\lambda=\tau^2(\log\Psi)''(\tau)
 =\frac{(2-2i)\tau S'(\tau)}
 {(1+\tau)(1+2\tau)(1+(1-i)\tau)}.                         \tag{H14}
$$



Modulo (g(a)), exact simplification gives



$$
\begin{aligned}
 \Re\lambda
 &=\frac4{15}(3456a^5-11040a^4+9680a^3-2460a^2-810a+217),\\
 \Im\lambda
 &=-\frac2{15}(3456a^5-12160a^4+13000a^3-4820a^2-505a+222).
                                                               \tag{H15}
\end{aligned}
$$



Numerically,



$$
\lambda=2.1621300694647513101
         -0.2244185193994579759,i,                         \tag{H16}
$$



so (Re\lambda>0).  This is the condition that the second derivative
of (log|\Psi(\rho e^{i\theta})|) at (\tau) is negative.

The claimed nonzero amplitude also has a short exact representative:



$$
\Im\frac{b_2(\tau)}{b_0(\tau)}
 =\frac{(2a-1)(128a^4-416a^3+352a^2-44a-47)}{400}           \tag{H17}
$$



at the selected root (a).  Its numerical value is



$$
0.0642986930247985444592549992741\ldots>0.                \tag{H18}
$$



The final exact replay should certify rational intervals, for example
(Re\lambda>2) and (0.064<\Im(b_2/b_0)<0.065), directly from the
isolating interval for (a).  This would turn the present symbolic
reductions into a short exact sign proof.

## 4. The equal-modulus saddle across (-1)

It must not be discarded without explanation.  There is an exact
anti-holomorphic symmetry:



$$
S(-1-\overline v)=-\overline{S(v)},\qquad
 \Psi(-1-\overline v)=-\overline{\Psi(v)}.                  \tag{H19}
$$



Hence



$$
\tau^*=-1-\overline\tau
 =-1.3933435869406637868+0.2348766139072831759,i            \tag{H20}
$$



is another saddle and



$$
|\Psi(\tau^*)|=|\Psi(\tau)|.                              \tag{H21}
$$



Its squared radius is



$$
|\tau^*|^2=1+2x+a
 =1.9965733750292260732\ldots>1.                            \tag{H22}
$$



Thus the pole at (-1), on the unit circle, lies between the radii of
(\tau) and (\tau^*).  More importantly, the coefficient integral can
be evaluated directly on (|v|=\rho<1/2), where (conditional on exact
certification of (H12)) (\tau) is the sole modulus maximum.  The external
saddle is therefore not being ignored: it belongs to a different radial
region and simply does not occur in this fixed-circle Laplace integral.
Any deformation designed to reach it would have to account for the pole
cycle at (-1); it is unnecessary for the coefficient asymptotic.

The third saddle is



$$
-\frac12-0.2197532278145663518,i,
$$



and has (|\Psi|=0.003528270316945449\ldots), versus
(|\Psi(\tau)|=4339.119484827354\ldots).  This is useful diagnostic
information but is not needed after the fixed-circle maximum theorem.

## 5. Asymptotic that follows once the exact maximum certificate is finished

Parameterize the valid circle by (v=\rho e^{i\theta}).  Then



$$
I_j=\frac1{2\pi}\int_{-\pi}^{\pi}
 \Psi(\rho e^{i\theta})^m b_j(\rho e^{i\theta})\,d\theta,
 \qquad j=0,2.                                             \tag{H23}
$$



If (H12), (H15), and the relevant signs are certified exactly, standard
one-dimensional analytic saddle expansion on this *fixed* contour gives,
with the square root chosen by (Re\sqrt\lambda>0),



$$
I_j=\frac{\Psi(\tau)^m}{\sqrt{2\pi m}\sqrt\lambda}
 \left(b_j(\tau)+O(m^{-1})\right),\qquad j=0,2.             \tag{H24}
$$



The off-saddle error is exponentially smaller by compactness and strict
uniqueness; the local analytic Taylor expansion gives the stated uniform
power error for these two fixed amplitudes.  Consequently,



$$
\Im(I_2\overline{I_0})
 =\frac{|\Psi(\tau)|^{2m}}{2\pi m|\lambda|}
 \left(\Im(b_2(\tau)\overline{b_0(\tau)})+O(m^{-1})\right). \tag{H25}
$$



Since



$$
\Im(b_2\overline{b_0})
 =|b_0|^2\Im(b_2/b_0)>0,                                  \tag{H26}
$$



the exact identity in the parent source would yield



$$
B_m\sim
 \frac{2^{-14m-3}|\Psi(\tau)|^{2m}}
      {\pi m^2|\lambda|}
 \Im(b_2(\tau)\overline{b_0(\tau)}),                     \tag{H27}
$$



and in particular (B_m>0) for all sufficiently large (m), together
with



$$
\frac1{6m}\log|B_m|
 \longrightarrow
 \frac{2\log|\Psi(\tau)|-14\log2}{6}=2\ell.              \tag{H28}
$$



Equation (H28) is **not yet promoted here**, solely because the exact
Sturm/interval replay and the polished uniform saddle proof remain to be
written.

## 6. Precise next steps

1. Implement a deterministic certificate script using only exact integer
   and rational arithmetic for (H1)--(H18).  Monitor RSS; all polynomial
   degrees are at most 12 in (R) and 6 in (q), so this should be small.
2. Do not rely on floating signs.  Isolate (a,R) by rational Sturm
   intervals and certify each required algebraic sign by exact interval
   Horner evaluation or a resultant/Sturm sign query.
3. Record the complete Sturm sign table (H12) and verify that no cleared
   denominator vanishes at the selected embedding.
4. Write a self-contained fixed-circle saddle lemma proving (H24), including
   the exponentially small complementary arc and the branch convention for
   (sqrt\lambda).
5. State (H19)--(H22) prominently in the theorem: the external saddle is
   equal in modulus but absent from the chosen coefficient circle, not
   silently omitted.
6. Replay twice, compare JSON bytes, create a manifest, and request an
   independent formula/line audit before freezing.

No implication for (e+\pi), irrationality, or transcendence follows from
this handoff note alone.

