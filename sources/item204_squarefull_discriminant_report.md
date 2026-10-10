> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 204: the reverse-Bessel discriminant is explicit, but square divisibility is a separate Hensel digit

Date: 2026-08-30 (Beijing time)

## 1. Verdict

Let



$$
q_0=q_1=1,\qquad q_N=(4N-2)q_{N-1}+q_{N-2}.
$$



The actual denominator has the monic polynomial realization



$$
A_N(X)=\sum_{k=0}^N{(2N-k)!\over k!(N-k)!}X^k,
 \qquad \boxed{q_N=A_N(-1)}.                              \tag{1.1}
$$



This is a scaled reverse-Bessel polynomial.  It satisfies the exact
recurrence and derivative identity



$$
A_0=1,\quad A_1=X+2,\quad
 A_N=(4N-2)A_{N-1}+X^2A_{N-2},                            \tag{1.2}
$$





$$
\boxed{2A_N'(X)=A_N(X)-XA_{N-1}(X).}                    \tag{1.3}
$$



Put $c_k=A_k(0)=(2k)!/k!$.  The natural adjacent and derivative
resultants, including all signs and leading factors, are



$$
\boxed{\operatorname {Res}(A_N,A_{N-1})
       =\prod_{k=1}^{N-1}c_k^2,}                          \tag{1.4}
$$





$$
\boxed{\operatorname {Res}(A_N,A_N')
       =(2N-1)!!\prod_{k=1}^{N-1}c_k^2,}                  \tag{1.5}
$$



and therefore



$$
\boxed{\operatorname {Disc}(A_N)
 =(-1)^{N(N-1)/2}(2N-1)!!
       \prod_{k=1}^{N-1}\left({(2k)!\over k!}\right)^2.} \tag{1.6}
$$



In particular, every prime $p>2N+1$ is absent from this discriminant.
At an actual root there is an even more direct statement:



$$
\boxed{2A_N'(-1)=q_N+q_{N-1}.}                           \tag{1.7}
$$



Adjacent denominators are coprime, so if an odd prime $p\mid q_N$,
then $A_N'(-1)\not\equiv0\pmod p$.  Thus every actual root at $X=-1$
is a simple polynomial root, including every root in the range
$p>2N+1$.

This does **not** prove that $p^2\nmid q_N$.  Write



$$
\lambda_{p,N}:={q_N\over p}\pmod p.
$$



The unique lift of the root residue $-1\pmod p$ to a root modulo
$p^2$ is $-1+pt_{p,N}$, where



$$
\boxed{
 t_{p,N}\equiv-\lambda_{p,N}A_N'(-1)^{-1}
 \equiv-2\lambda_{p,N}q_{N-1}^{-1}\pmod p.}              \tag{1.8}
$$



Consequently



$$
\boxed{p^2\mid q_N\iff t_{p,N}=0.}                      \tag{1.9}
$$



The discriminant proves uniqueness of the Hensel lift; it does not say
whether that lift is the distinguished integer $-1$.  The missing datum
is exactly the first divided value $\lambda_{p,N}$.  No identity in this
note forces it to be nonzero.

There is also a sharply scoped two-sided failure for the other natural
polynomialization.  Let



$$
Q_0(T)=1,\quad Q_1(T)=T+1,\quad
 Q_N(T)=(T+4N-2)Q_{N-1}(T)+Q_{N-2}(T).                    \tag{1.10}
$$



Then $Q_N(0)=q_N$, and $Q_N'(0)=b_N/4$ for the jet sequence of
Item 202.  The exact target-range row



$$
(N,p)=(48,2879),\qquad p>2N+1,                            \tag{1.11}
$$



satisfies



$$
Q_{48}(0)\equiv2879\cdot2248\not\equiv0\pmod {2879^2},
 \qquad Q_{48}'(0)\equiv0\pmod {2879}.                   \tag{1.12}
$$



Thus $0$ is a multiple root of $Q_{48}\bmod2879$, and $2879$
divides its discriminant, but $2879^2\nmid q_{48}$.  Shift-continuant
multiplicity is not sufficient for square divisibility even in the
prescribed large-prime range.

Conversely, the actual rows $(N,p)=(8,13),(79,7),(79,31)$ have
$p^2\mid q_N$ and $Q_N'(0)\not\equiv0\pmod p$.  These three rows are
all outside $p>2N+1$.  They disprove necessity only globally; this note
makes **no target-range non-necessity claim** from them.

The outcome is therefore a scoped no-go, not a squarefreeness theorem:
the reverse-Bessel discriminant, its derivative at the root, the
companion Wronskian, and the natural coefficient-shift discriminant do
not by themselves yield a proper bound for the large-prime squarefull
part of the actual $q_N$.  Whether any $p>2N+1$ actually satisfies
$p^2\mid q_N$ remains open.

## 2. Polynomial, derivative, and resultant identities -- PROVED

The coefficient of $X^k$ in $A_N$ is



$$
a_{N,k}={(2N-k)!\over k!(N-k)!}.
$$



Substitution in (1.2) verifies the recurrence coefficient by coefficient.
Evaluation at $X=-1$ gives the actual recurrence and initial values,
proving (1.1).  The same coefficient formula gives



$$
2A_N'=A_N-XA_{N-1},
$$



including the constant and leading coefficients, proving (1.3).

For the resultants, reduce (1.2) modulo $A_{N-1}$.  Since all the
polynomials are monic and consecutive degree products are even,



$$
\begin{aligned}
 \operatorname {Res}(A_N,A_{N-1})
 &=\operatorname {Res}(X^2A_{N-2},A_{N-1})\\
 &=A_{N-1}(0)^2\operatorname {Res}(A_{N-1},A_{N-2}).
\end{aligned}                                             \tag{2.1}
$$



Starting with $\operatorname {Res}(A_1,A_0)=1$ proves (1.4).

Next, (1.3), invariance under adding a multiple of the first polynomial,
and multiplicativity give



$$
\begin{aligned}
 2^N\operatorname {Res}(A_N,A_N')
 &=\operatorname {Res}(A_N,A_N-XA_{N-1})\\
 &=\operatorname {Res}(A_N,-X)
   \operatorname {Res}(A_N,A_{N-1})\\
 &=A_N(0)\operatorname {Res}(A_N,A_{N-1}).
\end{aligned}                                             \tag{2.2}
$$



Since



$$
{A_N(0)\over2^N}={(2N)!\over2^NN!}=(2N-1)!!,
$$



equation (2.2) proves (1.5).  For a monic degree-$N$ polynomial,



$$
\operatorname {Disc}(A_N)
 =(-1)^{N(N-1)/2}\operatorname {Res}(A_N,A_N'),
$$



which proves (1.6) with the displayed sign.

Every prime factor on the right side of (1.5) is at most $2N-1$.
Therefore the whole polynomial is separable modulo every
$p>2N+1$.  This is stronger than a height estimate but weaker than a
statement about the valuation of one fixed integer value.

## 3. Exact Hensel coordinate -- PROVED

Putting $X=-1$ in (1.3) proves (1.7).  The recurrence can be run
backwards without changing the gcd of adjacent terms, so



$$
\gcd(q_N,q_{N-1})=\gcd(q_1,q_0)=1.                       \tag{3.1}
$$



If the odd prime $p\mid q_N$, equations (1.7) and (3.1) show that



$$
A_N'(-1)\equiv {q_{N-1}\over2}\not\equiv0\pmod p.       \tag{3.2}
$$



For any $t\in\mathbb F_p$, exact Taylor expansion modulo $p^2$ gives



$$
A_N(-1+pt)\equiv q_N+ptA_N'(-1)\pmod {p^2}.              \tag{3.3}
$$



Divide (3.3) by $p$.  There is one root digit, namely



$$
t=-{q_N/p\over A_N'(-1)},
$$



and substitution of (3.2) proves (1.8).  The fixed point $-1$ is the
lifted root exactly when this digit is zero, proving (1.9).

This locates the obstruction precisely.  A discriminant or resultant
computed modulo $p$ sees (3.2), hence the existence and uniqueness of a
lift.  It does not see $q_N/p\pmod p$, hence cannot decide whether the
root lift has digit zero.

## 4. Same-polynomial Hensel countermodel -- PROVED, SCOPED

The distinction is visible inside one actual reverse-Bessel polynomial,
without changing its coefficients.  For $N=4$,



$$
A_4(X)=X^4+20X^3+180X^2+840X+1680.
$$



At $p=13>2N+1$,



$$
A_4(-1)=1001=13\cdot77,
 \qquad A_4'(-1)=536\equiv3\pmod {13}.                    \tag{4.1}
$$



Formula (1.8) gives $t=9$.  Accordingly,



$$
-1+13t=116,
 \qquad A_4(116)=13^2\cdot1{,}271{,}024.                  \tag{4.2}
$$



The two evaluation points are identical modulo $13$; the polynomial,
its discriminant, the root residue, and the derivative residue are the
same.  Nevertheless the value at $-1$ has valuation one and the value at
$116$ has valuation at least two.  Thus those mod-$p$ data cannot
determine the first-Witt evaluation digit.

This is not an actual counterexample to large-prime square divisibility:
the actual evaluation point is $-1$, not $116$, and
$13^2\nmid q_4$.  It is a countermodel only to arguments which try to
deduce the valuation of a fixed integer lift from separability,
discriminant, derivative, and root-residue data alone.

## 5. The all-coefficient-shift continuant -- PROVED NO-GO WITH FINITE EXACT WITNESSES

Differentiate (1.10) at $T=0$.  If



$$
d_N:=Q_N'(0),
$$



then



$$
d_0=0,\quad d_1=1,\quad
 d_N=(4N-2)d_{N-1}+d_{N-2}+q_{N-1}.                       \tag{5.1}
$$



Thus $4d_N=b_N$ for the jet-correction sequence used in Item 202.
If $p\mid q_N$ and $p\mid d_N$, then $T=0$ is a multiple root of
$Q_N\bmod p$, so $p\mid\operatorname {Disc}(Q_N)$.

The exact target-range witness is



$$
p=2879>97=2\cdot48+1,
$$



with



$$
q_{48}\equiv6{,}471{,}992=2879\cdot2248\pmod {2879^2},
 \qquad d_{48}\equiv0\pmod {2879}.                        \tag{5.2}
$$



Hence $v_{2879}(q_{48})=1$ although the shift-polynomial root is
multiple.  This proves that the shift discriminant is not a sufficient
squarefull criterion in the range of interest.

For the reverse implication, exact actual values give



$$
\begin{array}{c|c|c|c}
 (N,p)&v_p(q_N)&d_N\pmod p&p>2N+1\\ \hline
 (8,13)&2&7&\text{no}\\
 (79,7)&2&1&\text{no}\\
 (79,31)&2&16&\text{no}.
\end{array}                                               \tag{5.3}
$$



Thus multiplicity at the distinguished root $T=0$ is not necessary in
the unrestricted sequence.  Because all three rows in (5.3) violate
$p>2N+1$, they do
not settle necessity in the prescribed range.  The checker and this
report preserve that scope explicitly.

The usual unit Wronskian likewise proves only coprimality with an adjacent
or companion value.  The actual square rows in (5.3) show globally that a
unit Wronskian does not force a sequence value to be squarefree.  Again,
no target-range conclusion follows from those rows.

## 6. Radical ledger

Define



$$
S_N=\prod_{\substack{p>2N+1\\p^2\mid q_N}}p.              \tag{6.1}
$$



The only unconditional all-index bound remains



$$
\boxed{S_N^2\mid q_N.}                                   \tag{6.2}
$$



Equation (1.6) adds no factor to (6.2): every prime counted by $S_N$
is automatically absent from the reverse-Bessel discriminant.  This says
that its polynomial root is unramified, not that the fixed value has
valuation one.  Likewise, (1.8) rewrites every candidate as the condition
$t_{p,N}=0$, but supplies no cross-prime or product estimate for those
zero digits.

Therefore this route proves neither $S_N=1$, nor a proper sub-capacity
bound, nor any $o(N\log N)$ estimate.  The Euler/left-factorial filter of
Item 202 is downstream and is not used here.

## 7. Exact replay and finite evidence

The deterministic standard-library checker performs the following.

1. It constructs $A_N$ both from its closed sum and its polynomial
   recurrence through $N=8$, and checks (1.3) coefficient by coefficient.
2. It computes the Sylvester determinants by fraction-free Bareiss
   elimination through $N=8$, checking the signs and all factors in
   (1.4)--(1.6).
3. It replays the exact $(N,p)=(4,13)$ Hensel witness, the target-range
   $(N,p)=(48,2879)$ insufficiency witness, and the three explicitly
   out-of-range necessity witnesses.
4. It reconstructs every actual lower root with $p>2N+1$ for primes
   $p\leq20000$, checks (1.7)--(1.9), and finds 1,133 root rows and no
   row with $p^2\mid q_N$.

The last absence statement is **EXPERIMENTAL FINITE**.  It is not an
all-prime squarefreeness theorem.  The displayed witnesses are finite
exact calculations; the scoped logical no-go deductions from them are
proved statements.

## 8. Status ledger

### PROVED

- The scaled reverse-Bessel representation (1.1), recurrence (1.2), and
  derivative identity (1.3).
- The adjacent resultant, derivative resultant, and signed discriminant
  formulas (1.4)--(1.6).
- Simplicity of every odd actual polynomial root at $X=-1$, and in
  particular separability for every $p>2N+1$.
- The exact Hensel digit and square criterion (1.8)--(1.9).
- The scoped same-polynomial Hensel no-go of Section 4.
- Failure of the coefficient-shift discriminant as a sufficient condition
  in the target range, via $(48,2879)$.
- Global failure of coefficient-shift multiplicity as a necessary
  condition, with no target-range necessity claim.

### EXPERIMENTAL FINITE

- The symbolic/Sylvester replay through $N=8$.
- The displayed exact arithmetic fixtures.
- The actual lower-index scan through $p\leq20000$, including its finite
  absence of a large-prime square row.

### OPEN

- Whether any $p>2N+1$ satisfies $p^2\mid q_N$ for the actual seed.
- Any proper all-$N$ bound for $S_N$ below the capacity (6.2).
- Any recurrence-mod-$p^2$, $p$-adic, or cross-prime theorem forcing
  the actual Hensel digit in (1.8) to be nonzero or sufficiently sparse.
- All downstream all-lift, coefficient, matching, saddle, and moving-CRT
  requirements.
- Irrationality, rationality, or transcendence of the target constant.

## 9. Portable artifacts

The source, checker, canonical result, replay result, and manifest archive
as

```text
sources/item204_squarefull_discriminant_report.md
scripts/item204_squarefull_discriminant_certificate.py
results/item204_squarefull_discriminant_certificate.json
results/item204_squarefull_discriminant_certificate.replay.json
results/item204_squarefull_discriminant_hashes.sha256
```

From the archive root, replay with

```text
python scripts/item204_squarefull_discriminant_certificate.py \
  --prime-limit 20000 \
  --symbolic-limit 8 \
  --output results/item204_squarefull_discriminant_certificate.replay.json
```

Canonical and replay JSON are byte-identical.  The report uses the frozen
Item 202 source only to inherit the prior problem boundary:

```text
abbc68e283f16871798be0c6da8af5df55ba6bf865a5864eefc0f8e19fe88f62  sources/item202_actual_squarefull_filter_report.md
```
