> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 357 — target-specific Jacobi transform and the complete Gross–Koblitz unit-face obstruction for fixed $j=1$

Date: 2026-09-01

## 1. Outcome and admission threshold first

Retain the actual tied family



$$
n=2h,\qquad r=2s+1,\qquad p=2n+3r,\qquad 2M=3n+4r,       \tag{1.1}
$$



and



$$
a_{r,n}=[u^n]G(u)^{-r},\qquad
G(u)=1-4u+6u^2-4u^3.                                    \tag{1.2}
$$



The proved gate remains one-way:



$$
\boxed{
\text{ordinary fixed-}j=1\text{ collision}
\Longrightarrow p\mid a_{r,n}.}                         \tag{1.3}
$$



No selected-factor zero is called a full collision.

Item 356 closed multiplicativity-only compression but explicitly left
target-specific hypergeometric identities open.  The present item attacks
that surviving class.

This item applies a target-specific finite-field hypergeometric transform,
not a generic character estimate.  Put



$$
q=p^2,\qquad Q=q-1,\qquad E=p-r=2(n+r).                 \tag{1.4}
$$



Over $\mathbb F_q$, the coefficient-isolating Kummer lift from Item 342
has an exact two-frequency Jacobi/Appell representation.  Its complete
Gross–Koblitz/Stickelberger valuation-zero face is



$$
\boxed{
\mathscr U_{r,n}={(s,t,u)\in\mathbb Z_{\geq0}^3:s+t+u=n\}.}             \tag{1.5}
$$



Consequently



$$
\boxed{\#\mathscr U_{r,n}={ (n+1)(n+2)\over2}.}          \tag{1.6}
$$



More decisively, the exact reduction of this whole first face is



$$
\boxed{
\text{first Stickelberger face}=-[u^n]G(u)^E
\equiv-a_{r,n}\pmod p.}                                 \tag{1.7}
$$



Thus the target-specific Gross–Koblitz transform does not supply a second
condition.  Its first face is exactly the already-booked selected Hasse
coordinate, written as a two-dimensional triangular cancellation.

The construction reaches every actual row, so its raw possible reach is
the entire retained fixed-$j=1$ ceiling $1/36$ per $6M$.  The failure
is therefore not thin support.  It fails at the implication stage:

1. the original collision forces only the face sum in (1.7) to vanish;
2. the face has $\binom{n+2}{2}$ unit terms, not a unique minimal term;
3. on the positive-rate bulk this cardinality is unbounded and typically
   quadratic in $M$; and
4. two predeclared selected-zero rows have valuation exactly one in this
   very extension-field Kummer lift.

Hence



$$
\boxed{
\text{new forced condition}=0,\quad
\text{new linear log rate}=0,\quad
\text{new fixed-}j=1\text{ capacity reduction}=0.}       \tag{1.8}
$$



Booking is $0$, the $1/36$ ceiling is retained, and Route 1 remains
ACTIVE.

## 2. The exact target-specific Jacobi/Appell transform

Choose $i\in\mathbb F_q$ with $i^2=-1$.  The cubic factors as



$$
G(x)=(1-2x)(1-(1+i)x)(1-(1-i)x).                        \tag{2.1}
$$



Let $\Omega:\mathbb F_q^\times\to\mu_Q$ be the Teichmüller
character at a chosen prime $\mathfrak P\mid p$, extended by zero at
zero.  Define



$$
A=\Omega^{-n},\qquad B=\Omega^E                         \tag{2.2}
$$



and



$$
\mathscr S_{p,r,n}
=\sum_{x\in\mathbb F_q}A(x)B(G(x)).                    \tag{2.3}
$$



Reduction at $\mathfrak P$ and Item 342's extension-field coefficient
isolation give



$$
\mathscr S_{p,r,n}\equiv
\sum_{x\in\mathbb F_q^\times}x^{-n}G(x)^E
=-[u^n]G(u)^E\equiv-a_{r,n}\pmod{\mathfrak P}.          \tag{2.4}
$$



Put



$$
\alpha={1+i\over2},\qquad \beta={1-i\over2}.           \tag{2.5}
$$



After $y=2x$, equation (2.3) becomes



$$
\mathscr S_{p,r,n}
=\Omega(2)^n\sum_y
A(y)B(1-y)B(1-\alpha y)B(1-\beta y).                   \tag{2.6}
$$



For multiplicative characters extended by zero, write



$$
J(C,D)=\sum_{z\in\mathbb F_q}C(z)D(1-z).               \tag{2.7}
$$



Multiplicative Fourier inversion gives, for $y\ne0$,



$$
B(1-\lambda y)
={1\over Q}\sum_C C(\lambda)J(\bar C,B)C(y).           \tag{2.8}
$$



Expanding the three factors and applying character orthogonality yields
the exact two-frequency transform



$$
\boxed{
\mathscr S_{p,r,n}
={\Omega(2)^n\over Q^2}
\sum_{C,D}
D(\alpha)L(\beta)
J(\bar C,B)J(\bar D,B)J(ACD,B),}                       \tag{2.9}
$$



where



$$
L=\bar A\bar C\bar D.                                  \tag{2.10}
$$



Equation (2.9) is an exact finite-field Appell/Jacobi identity for the
actual tied target.  It is not a finite fit and does not replace the target
by an ambient hypergeometric family.

## 3. Complete Stickelberger valuation theorem

For $0\leq m<Q$, consider



$$
J_m=J(\Omega^{-m},\Omega^E).                            \tag{3.1}
$$



Let $s_p(v)$ be the sum of the two base-$p$ digits of
$0\leq v<p^2$.  Gross–Koblitz, equivalently Stickelberger's Jacobi-sum
valuation theorem, gives for $m\notin\{0,E\}$



$$
v_{\mathfrak P}(J_m)
={s_p(m)+s_p(Q-E)-s_p((m-E)\bmod Q)\over p-1}.          \tag{3.2}
$$



The exceptional cases are elementary:



$$
J_0=J(\varepsilon,B)=-1,\qquad
J_E=J(B^{-1},B)=-B^{-1}(-1),                            \tag{3.3}
$$



so both are units.

Because $0<E<p$, equation (3.2) has a complete carry classification.
If $0<m<E$, subtracting $E$ wraps modulo $Q$, and the digit-sum
difference is zero.  If $m>E$, subtracting $E$ either borrows one
base-$p$ digit or does not; the valuation is respectively $1$ or
$2$.  Therefore



$$
\boxed{
v_{\mathfrak P}(J_m)=0
\quad\Longleftrightarrow\quad 0\leq m\leq E.}           \tag{3.4}
$$



This is an all-parameter theorem for the actual family.

## 4. The complete first face is triangular

Parameterize the two characters in (2.9) as



$$
C=\Omega^s,\qquad D=\Omega^t.                           \tag{4.1}
$$



The three Jacobi arguments are then



$$
\Omega^{-s},\qquad \Omega^{-t},\qquad
\Omega^{-(n-s-t)}.                                      \tag{4.2}
$$



By (3.4), a term in (2.9) is a unit precisely when



$$
0\leq s\leq E,\qquad0\leq t\leq E,
\qquad(n-s-t)\bmod Q\in[0,E].                           \tag{4.3}
$$



The tied relation gives



$$
E=2(n+r)>n.                                              \tag{4.4}
$$



Moreover $Q+n-2E>E$ for every actual $p\geq13$.  Hence the wrapped
case in the last condition of (4.3) cannot be a unit.  Thus (4.3) is
equivalent to



$$
s\geq0,\qquad t\geq0,\qquad s+t\leq n.                 \tag{4.5}
$$



Writing $u=n-s-t$ proves (1.5) and (1.6).

The large face is not caused by a loose estimate.  It is the complete set
of terms of minimal $p$-adic valuation.

## 5. Exact evaluation of the first face

For $0\leq m\leq E<p$, direct reduction of the Jacobi sum gives



$$
\begin{aligned}
J_m
&\equiv\sum_{z\in\mathbb F_q^\times}z^{-m}(1-z)^E\\
&=-(-1)^m{E\choose m}pmod{\mathfrak P}.                \tag{5.1}
\end{aligned}
$$



Indeed, after expanding $(1-z)^E$, multiplicative orthogonality over
$\mathbb F_q^\times$ selects exactly the coefficient of $z^m$.

On the face $s+t+u=n$, the phase in (2.9) reduces to
$\alpha^t\beta^u$.  Since $Q^2\equiv1\pmod p$, equations
(2.9) and (5.1) give



$$
\mathscr S_{p,r,n}
\equiv
2^n(-1)^{n+3}
\sum_{s+t+u=n}
{E\choose s}{E\choose t}{E\choose u}
\alpha^t\beta^u.                                       \tag{5.2}
$$



Now



$$
\alpha+\beta=1,\qquad\alpha\beta={1\over2},            \tag{5.3}
$$



so



$$
\begin{aligned}
(1+z)(1+\alpha z)(1+\beta z)
&=1+2z+{3\over2}z^2+{1\over2}z^3\\
&=G(-z/2).                                               \tag{5.4}
\end{aligned}
$$



Therefore the sum in (5.2) equals



$$
[z^n]G(-z/2)^E=(-1)^n2^{-n}[u^n]G(u)^E.                \tag{5.5}
$$



Substitution into (5.2) proves (1.7), including its sign.

This is the decisive structural outcome: applying Gross–Koblitz to the
target-specific transform returns the selected Hasse coefficient itself.
It does not split that coefficient into a bounded number of independently
controlled unit factors.

## 6. Why the classical ${}_4F_3$ character skeleton also collapses

Item 342's terminating classical representation has upper parameters



$$
-{n\over4},\ {1-n\over4},\ {2-n\over4},\ {3-n\over4}   \tag{6.1}
$$



and lower parameters



$$
r+{1\over4},\ r+{1\over2},\ r+{3\over4},               \tag{6.2}
$$



with $k!$ supplying the fourth lower parameter $1$.  Modulo integer
shifts, both four-element multisets are exactly



$$
\boxed{\{0,1/4,1/2,3/4\}.}                              \tag{6.3}
$$



Thus the naive finite-character/Gauss-sum skeleton which remembers only
fractional parameters cancels its numerator and denominator Gauss quotients
term by term.  It is independent of the moving $(n,r)$ target.

All target information lies in the discarded integer shifts.  If
$n=4v$, their paired distances are



$$
(v+1,r+v,r+v,r+v),                                      \tag{6.4}
$$



while if $n=4v+2$, they are



$$
(v+1,r+v,r+v+1,r+v+1).                                 \tag{6.5}
$$



In both cases their total is



$$
\boxed{p-n+1.}                                          \tag{6.6}
$$



Accordingly, a correct p-adic transformation must retain these moving
contiguous-shift data.  Reducing the classical parameters modulo
$\mathbb Z$ is not an exact representation of $a_{r,n}$.

This section closes only that naive fractional-character translation.  It
does not rule out a new p-adic transformation which exploits the integer
shifts rather than discarding them.

## 7. The exact lift does not acquire a forced second digit

The Appell/Jacobi representation might still have helped if selected Hasse
vanishing universally forced its extension-field lift into
$\mathfrak P^2$.  It does not.

For the deterministic controls, choose the certificate's quadratic
unramified model



$$
R_p=(\mathbb Z/p^2\mathbb Z)[T]/(T^2-d),                 \tag{7.1}
$$



where $d$ is the declared least quadratic nonresidue modulo $p$.  For
$y\in\mathbb F_{p^2}$, its Teichmüller lift modulo $p^2$ is



$$
[y]\equiv\widetilde y^{,p^2}\pmod{p^2}.               \tag{7.2}
$$



Direct exact evaluation of (2.3) in this ring gives



$$
\mathscr S_{13,3,2}\equiv143=13\cdot11\pmod{13^2},     \tag{7.3}
$$



and



$$
\mathscr S_{47,5,16}\equiv188=47\cdot4\pmod{47^2}.     \tag{7.4}
$$



Both rows have $a_{r,n}=0\pmod p$, but both lifts have valuation exactly
one.  These are selected-coordinate controls only; neither is asserted to
be a full ordinary collision.

Thus



$$
\boxed{
a_{r,n}=0\pmod p
\not\Longrightarrow
v_{\mathfrak P}(\mathscr S_{p,r,n})\geq2.}              \tag{7.5}
$$



This is an exact finite counterexample to a universal second-digit claim,
not density evidence.

## 8. Declared exact controls

Only the five rows predeclared in Item 342 are used.

| $(h,s,p)$ | $(n,r,E)$ | selected Hasse coordinate | unit-face size | $\mathscr S\bmod p^2$ | selected-zero quotient |
|---|---|---:|---:|---:|---:|
| $(1,1,13)$ | $(2,3,10)$ | $0$ | $6$ | $143$ | $11$ |
| $(2,1,17)$ | $(4,3,14)$ | $8$ | $15$ | $264$ | — |
| $(8,2,47)$ | $(16,5,42)$ | $0$ | $153$ | $188$ | $4$ |
| $(4,4,43)$ | $(8,9,34)$ | $2$ | $45$ | $428$ | — |
| $(2,6,47)$ | $(4,13,34)$ | $36$ | $15$ | $199$ | — |

For every row, the certificate verifies:

1. the complete unit interval $0\leq m\leq E$ in (3.4);
2. the complete triangular face and its cardinality;
3. every Jacobi reduction (5.1) for $0\leq m\leq n$;
4. the factor identity (5.4) inside the actual quadratic field;
5. the reduction of the face to $-a_{r,n}$; and
6. the target-specific extension lift modulo $p^2$.

No prime is searched and no finite row is given asymptotic weight.

## 9. Capacity consequence and scoped no-go

The exact transform has full raw support:



$$
\sum_{\text{actual candidate rows}}\log p
={M\over6}+o(M).                                        \tag{9.1}
$$



Item 339 already proves that the rows with $n=o(M)$ have weighted mass
$o(M)$.  Away from that zero-rate edge, the first-face size
$\binom{n+2}{2}$ is unbounded.  On any bulk $n\geq\eta M$, it is at
least



$$
{\eta^2M^2\over2}+O(M).                                 \tag{9.2}
$$



The following method class is therefore closed:

> A unique-minimal-term or bounded-leading-face Gross–Koblitz argument,
> applied to the exact target-specific $\mathbb F_{p^2}$ transform,
> cannot create a second collision-forced condition or reduce the
> fixed-$j=1$ ceiling.  The complete first face is the old Hasse
> coordinate itself.

Also closed is the naive finite-character translation of the classical
${}_4F_3$ which discards all integer shifts.

The theorem does **not** rule out:

- a weighted nonconcentration or monodromy theorem for the triangular face;
- average cancellation on higher Stickelberger faces;
- a p-adic transformation that retains and exploits the moving shifts; or
- a second gate genuinely supplied by full-collision information.

No such asymptotic theorem is proved here.  Hence the exact transform is a
global method-class closure, not a ledger gain.

## 10. Strict decision

### PROVED

- the exact target-specific two-frequency Jacobi/Appell transform (2.9);
- the complete Gross–Koblitz/Stickelberger unit criterion (3.4);
- the complete triangular unit-face theorem (1.5) and its exact size;
- the exact reduction of the entire face to the selected Hasse coordinate;
- the equality of the classical upper and lower fractional-character
  multisets;
- the exact total moving shift $p-n+1$;
- the scoped unique-minimum/bounded-face Gross–Koblitz no-go;
- zero booking.

### EXACT FINITE ONLY

- five predeclared replay rows;
- two valuation-one selected-zero extension lifts;
- no prime scan, density inference, or full-collision claim.

### OPEN

- weighted nonconcentration for the triangular Hasse face;
- higher-face average cancellation;
- a p-adic transformation exploiting the integer parameter shifts;
- an additional condition supplied by full-collision information;
- $W_b(M)=o(M)$, any fixed-$j=1$ ceiling reduction,
  Route 1, and every conclusion about $e+\pi$.

## 11. Ledger and self-audit



$$
\begin{array}{c|c}
\text{quantity}&\text{Item 357 value}\\ \hline
\text{first Stickelberger face size}&\binom{n+2}{2}\\
\text{new collision-forced condition}&0\\
\text{new proved linear log rate}&0\\
\text{new fixed-}j=1\text{ capacity reduction}&0\\
\text{retained fixed-}j=1\text{ ceiling per }6M&1/36
\end{array}                                               \tag{11.1}
$$



The self-audit records:

1. the original collision implication is used only in its proved direction;
2. selected Hasse zeros are not called full collisions;
3. a first-face identity is not called a second independent condition;
4. valuation-one controls are not used as density evidence;
5. large face size is only a scoped obstruction, not a theorem against all
   p-adic transformations;
6. no capacity is booked without a weighted actual-family theorem.
