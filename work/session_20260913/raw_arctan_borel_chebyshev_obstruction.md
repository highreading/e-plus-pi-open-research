> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The actual raw Borel high blocks are not uniformly Chebyshev systems

Date: 2026-09-13. Continuation of `raw_arctan_positive_kernel_attempt.md`.
This note concerns the actual raw-arctangent system, rather than a
Machin or Möbius analogue. It proves two finite counterexamples to
proposed all-index structural theorems. It makes no claim that every
sufficiently large block fails.

## 1. The system that needs quantitative control

Put Q_0=1, Q_1=t and



$$
Q_{k+1}(t)=tQ_k(t)+\frac{k^2}{4k^2-1}Q_{k-1}(t),\qquad
 F_k(x)=\mathcal BQ_k(x)=\sum_d[t^d]Q_k(t)\frac{x^d}{d!}.
$$



The actual balanced degree-n polynomial P_B satisfies



$$
\int_0^1P_B(x)F_k(x)\,dx=0,
 \qquad k=n+1,\ldots,2n-1.
$$



An appealing route would make this entire consecutive block a
Chebyshev system on (0,1), thereby controlling the oscillations of
P_B. A d-dimensional Chebyshev space has no nonzero element with d
distinct zeros in that interval. Equivalently, every ordered d-node
collocation determinant of a basis is nonzero. The following examples
disprove this property both for unrestricted n and for all odd n.

## 2. A full-block counterexample at n=4

The block is F_5,F_6,F_7, with



$$
F_5=\frac{x^5}{120}+\frac{5x^3}{27}+\frac{5x}{21},\quad
 F_6=\frac{x^6}{720}+\frac{5x^4}{88}+\frac{5x^2}{22}+\frac5{231},
$$




$$
F_7=\frac{x^7}{5040}+\frac{7x^5}{520}
       +\frac{35x^3}{286}+\frac{35x}{429}.
$$



Writing D(a,b,c)=det(F_j(x_i)) with columns j=5,6,7 and rows
x_i=a,b,c, exact rational arithmetic gives



$$
D(1/8,1/4,3/8)=
 -\frac{80878214626081323779}{103816762437362560008192000}<0,
$$




$$
D(5/8,3/4,7/8)=
 \frac{80202758416306133}{41946166641358610104320}>0.
$$



Translate the first equally spaced triple continuously to the second.
All three nodes stay distinct and inside (0,1). Continuity gives a
singular collocation matrix at an intermediate triple. Since the three
polynomials have different degrees, they are linearly independent;
the resulting nonzero linear combination has three distinct interior
zeros. Thus this is a counterexample to the ordinary Chebyshev property,
not merely to an extended or endpoint version of that property.

## 3. An even-start full-block counterexample at odd n=5

Restricting to odd n makes the first high polynomial even, but does not
give an all-odd-index theorem. For n=5 the block is F_6,F_7,F_8,F_9.
Let W(x)=det(F_j^(r)(x)) with rows r=0,1,2,3. Its exact endpoint values
are



$$
W(0)=\frac{6125}{289496493}>0,\qquad
 W(1)=-\frac{237656983770709159}{711600336914064998400000}<0.
$$



For distinct fixed increasing real y_i, Taylor expansion and determinant
multilinearity give the standard local identity



$$
\frac{\det(F_j(x+\epsilon y_i))}
 {\prod_{i<j}\epsilon(y_j-y_i)}
 \longrightarrow\frac{W(x)}{0!1!2!3!}
 \qquad(\epsilon\longrightarrow0).
$$



Choose four interior nodes sufficiently close to 0, and four sufficiently
close to 1. Their determinants therefore have opposite signs. The
ordered configuration region 0<x_1<x_2<x_3<x_4<1 is convex. Joining the
two configurations gives a singular collocation matrix at four distinct
interior points and a nonzero element of this four-dimensional block
with four zeros. This again disproves the ordinary Chebyshev property.

The accompanying exact checker also supplies rational-node certificates:
the determinant at (1,2,3,4)/32 is positive, whereas that at
(1020,1021,1022,1023)/1024 is negative. Their complete rational values
are stored in `raw_arctan_borel_chebyshev_checks.json`.

## 4. Exact differential structure, and its limitation

The raw Legendre equation and its Borel transform give



$$
(1+t^2)Q_k''+2tQ_k'-k(k+1)Q_k=0,
$$




$$
\boxed{(x^2F_k'')''+(x^2F_k')'=k(k+1)F_k.}
$$



Indeed, if F_k=sum c_d x^d, its nonzero coefficients obey



$$
(d+2)^2(d+1)^2c_{d+2}=
 [k(k+1)-d(d+1)]c_d,
$$



which is exactly the displayed fourth-order equation. The three-term
raw recurrence also becomes the nonlocal recurrence



$$
F_{k+1}(x)=\int_0^xF_k(s)\,ds+\frac{k^2}{4k^2-1}F_{k-1}(x).
$$



These identities are useful structure, but are not a second-order
Sturm problem with shared separated boundary conditions. In particular,
individual imaginary-root or same-parity interlacing results cannot by
themselves prove the Chebyshev assertion contradicted above.

## 5. What remains open after these counterexamples

The n=4 and n=5 certificates do not exclude an eventual Chebyshev
theorem, nor a theorem on some unbounded subsequence. A proposed such
theorem must explicitly avoid these degrees and supply estimates that
are uniform as the block dimension n-1 grows. Fixed-order Wronskian
asymptotics or individual-polynomial root preservation do not provide
that uniformity.

The positive-kernel result and the primitive arithmetic result remain
valid. The exact quantitative target is still the selected signed
polynomial's mass and cancellation:



$$
\log|L_n|=\log q_n+n\log(\sqrt2-1)
              +\log M_n+\log\theta_n+o(n).
$$



No estimate for the actual M_n theta_n follows from the present
counterexamples. A quantitatively controlled determinant or a suitable
restricted subsequence remains a possible route; the broad all-index
and all-odd-index Chebyshev shortcuts are closed.
