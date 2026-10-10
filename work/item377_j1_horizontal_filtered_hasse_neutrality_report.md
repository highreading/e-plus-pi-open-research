> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 377 — horizontality remains information-neutral for the filtered-Hasse extension

Date: 2026-09-01

## 1. Outcome and admission audit

The actual fixed-$j=1$ selector remains



$$
p=4h+6s+3,\qquad M=3h+4s+2,
\qquad n=2h,\qquad r=2s+1.                    \tag{1.1}
$$



The ordinary collision only gives the one-way implication



$$
\text{full collision}\Longrightarrow
a_{r,n}=0,\qquad Q_0(h,s)=0\pmod p.           \tag{1.2}
$$



Item 374 constructed a minimal rank-two filtered Frobenius module whose
graded Hasse invariant is exactly $Q_0$, while its full Frobenius is an
isogeny with fixed Hodge weights $(0,1)$.  The remaining question is
whether adding a flat Griffiths-transverse connection forces $Q_0$ to
satisfy a new differential or difference equation.

It does not.  On the standard two-parameter formal base



$$
R=W(k)[[H,S]],\qquad F(H)=H^p,\quad F(S)=S^p, \tag{1.3}
$$



the horizontal connection exists, is unique, and is integral for **every**
$q\in R$.  If



$$
C:=p^{-1}F_\Omega^*:\Omega_R^1\longrightarrow\Omega_R^1, \tag{1.4}
$$



then its only nonzero matrix entry is



$$
\boxed{\omega_q=-\sum_{j\ge0}C^j(dq).}       \tag{1.5}
$$



The series converges $(H,S)$-adically.  It obeys



$$
C(\omega_q)-\omega_q=dq,\qquad d\omega_q=0. \tag{1.6}
$$



Thus integrability and Frobenius horizontality are automatic for every
candidate $q$; they do not cut out a proper Hasse divisor.

This closes a sharply scoped method class:



$$
\boxed{\text{fixed rank }2+\text{fixed Hodge polygon}
+\text{ordinary formal horizontality alone}}
$$



cannot give horizontal nonconcentration of $Q_0$.  What remains open is
a *prime-independent geometric origin* with bounded base, connection, and
conductor, together with a distribution theorem for its extension class.

The raw fixed-$j=1$ reach is still



$$
\sum\log p\le {M\over6}+o(M),\qquad
\Gamma_{j=1}^{\max}={1\over36}.              \tag{1.7}
$$



No weighted theorem is proved.  The booking is zero and the entire
$1/36$ ceiling is retained.

---

## 2. The exact general horizontality equations

Let $R$ be a $p$-torsion-free complete ring with Frobenius lift $F$,
and suppose



$$
F_\Omega^*(\Omega_R^1)\subset p\Omega_R^1.  \tag{2.1}
$$



Write $W=W(k)$ in the standard formal-disc case.  For any lift
$q\in R$ of the transverse Hasse coordinate, take



$$
\mathcal M=Re_1\oplus Re_2,qquad
\operatorname {Fil}^0\mathcal M=\mathcal M,qquad
\operatorname {Fil}^1\mathcal M=Re_1,qquad
\operatorname {Fil}^2\mathcal M=0.           \tag{2.2}
$$



The divided and full Frobenius maps are



$$
\varphi_1(e_1)=e_1+qe_2,qquad
\varphi_0(e_1)=p\varphi_1(e_1),\qquad
\varphi_0(e_2)=e_2.                          \tag{2.3}
$$



In the ordered basis $(e_1,e_2)$, full Frobenius has matrix



$$
A_q=\begin{bmatrix}p&0\\pq&1\end{bmatrix}.  \tag{2.4}
$$



The most general connection matrix is



$$
\Gamma=\begin{bmatrix}a&b\\c&d\end{bmatrix},
\qquad a,b,c,d\in\Omega_R^1.                 \tag{2.5}
$$



Griffiths transversality is



$$
\nabla\operatorname {Fil}^1
\subset\operatorname {Fil}^0\otimes\Omega_R^1. \tag{2.6}
$$



For this two-step filtration (2.6) puts no additional zero into (2.5).
This point matters: requiring 

$$
\nabla\operatorname {Fil}^1\subset
\operatorname {Fil}^1\otimes\Omega^1
$$

 would be the stronger condition
of filtration preservation, not ordinary Griffiths transversality.

Full Frobenius horizontality is exactly



$$
dA_q+\Gamma A_q=A_qF_\Omega^*(\Gamma).       \tag{2.7}
$$



Entry by entry, (2.7) is



$$
\begin{aligned}
a+qb&=F_\Omega^*(a),\\
b&=pF_\Omega^*(b),\\
p\,dq+pc+pq,d&=pqF_\Omega^*(a)+F_\Omega^*(c),\\
d&=pqF_\Omega^*(b)+F_\Omega^*(d).
\end{aligned}                                \tag{2.8}
$$



Because $R$ is $p$-adically separated and (2.1) holds, the second
equation gives $b=0$.  The first and fourth then give



$$
a=0,\qquad d=0.                              \tag{2.9}
$$



After division by $p$, the remaining equation is



$$
C(c)-c=dq.                                   \tag{2.10}
$$



Consequently, whenever $C$ is topologically nilpotent on one-forms,
there is exactly one horizontal connection:



$$
\Gamma_q=\begin{bmatrix}0&0\\\omega_q&0\end{bmatrix},
\qquad
\omega_q=-(1-C)^{-1}dq=-\sum_{j\ge0}C^j(dq). \tag{2.11}
$$



Equation (2.10) is also the divided-Frobenius horizontality equation on
$\operatorname {Fil}^1$:



$$
\nabla\varphi_1(e_1)
=(\varphi_0\otimes C)\nabla(e_1).             \tag{2.12}
$$



Thus the full and divided formulations agree; no extra condition was
lost by working with (2.7).

---

## 3. Convergence and integrability on the two-parameter base

For a monomial one-form on (1.3),



$$
C(H^uS^v\,dH)
=F(H^uS^v)H^{p-1}dH,                         \tag{3.1}
$$



and similarly with $dS$.  Its $(H,S)$-adic order grows from $u+v$
to



$$
p(u+v)+p-1.                                  \tag{3.2}
$$



Hence $C$ is topologically nilpotent, proving convergence and
uniqueness in (2.11).  For example,



$$
C^j(dH)=H^{p^j-1}dH.                         \tag{3.3}
$$



Moreover,



$$
C^j(dq)=p^{-j}d(F^j(q))                      \tag{3.4}
$$



is integral and closed.  Therefore



$$
d\omega_q=0.                                \tag{3.5}
$$



Since the matrix unit $E_{21}$ squares to zero,



$$
d\Gamma_q+\Gamma_q\wedge\Gamma_q
=E_{21}d\omega_q=0.                          \tag{3.6}
$$



So (2.11) is an integrable connection, not merely a formal solution of
the matrix equation.

This proves the promised arbitrary-coordinate theorem:

> **Horizontal neutrality theorem.**  On the standard two-parameter
> formal Frobenius base, every analytic Hasse coordinate $q(H,S)$
> admits a unique integral, flat, Griffiths-transverse connection on the
> Item 374 rank-two filtered Frobenius module.  Horizontality imposes no
> differential equation on $q$.

If one instead imposes the stronger non-Griffiths condition that
$\operatorname {Fil}^1$ itself be horizontal, then $c=0$, and
(2.10) forces $dq=0$.  That conclusion is caused entirely by the extra
filtration-preservation axiom and cannot be credited to the filtered
crystalline architecture posed here.

---

## 4. What this says—and does not say—about the actual $(h,s)$ family

There are three distinct bases which must not be conflated.

1. **Formal two-parameter base.**  If an actual coefficient moment is
   represented by any $q(H,S)\in W(k)[[H,S]]$, the theorem applies to
   it without regard to its degree or zero set.

2. **Coefficient-moment base.**  One may take $q$ itself, or the local
   moment coordinates from Item 374, as formal coordinates.  Again the
   connection exists for every value.

3. **Cross-prime tied selector.**  The integers $(h,s)$ in (1.1) live
   in changing residue characteristics, and the terminating coefficient
   defining $Q_0$ changes with the selected row.  Items 374 and 377 do
   not construct one prime-independent algebraic base carrying all those
   rows.

Thus this item proves a local formal no-go, not a global compatible-system
existence theorem.  It says that the ordinary connection axioms cannot
create the missing global arithmetic input.  It does **not** say that a
genuinely geometric family with additional structure could never impose
a useful restriction.

The exact missing input is now sharper:



$$
\boxed{
\begin{gathered}
\text{construct a prime-independent bounded-complexity family whose}\\
\text{local filtered extension class pulls back to the actual }Q_0,\\
\text{then prove weighted nonconcentration of its splitting primes.}
\end{gathered}}                              \tag{4.1}
$$



---

## 5. Dense residue-product support survives in the connection

Item 374 gave



$$
Q_0=-\sum_{x\in\mathbb F_{p^2}^{\times}}R(x),
\qquad
\prod_xU(-R(x))=U(Q_0),                      \tag{5.1}
$$



with at least



$$
N_p\ge p^2-1-\{4+2(p-1)+2|h-s|\}=p^2-O(p)  \tag{5.2}
$$



nonidentity pointwise factors.

There is an exact universal coefficient-moment version of the horizontal
connection.  Give those factors independent formal coordinates
$y_1,\ldots,y_N$, put



$$
q=y_1+\cdots+y_N,
\qquad F(y_i)=y_i^p.                          \tag{5.3}
$$



Then (2.11) becomes



$$
\omega_q
=-\sum_{i=1}^N\sum_{j\ge0}y_i^{p^j-1}dy_i.  \tag{5.4}
$$



Modulo the maximal ideal,



$$
\omega_q\equiv-\sum_{i=1}^Ndy_i.            \tag{5.5}
$$



Therefore all $N$ independent local directions survive already in the
cotangent term of the unique connection.  A universal pointwise lift of
the Item 374 product has at least $p^2-O(p)$ coefficient directions and
cannot be a bounded-support horizontal construction.

This is a coefficient-support statement, not a geometric conductor lower
bound after pullback.  On the actual two-dimensional selector base the
forms $dy_i$ can become dependent and may cancel.  Proving that no such
pullback compression exists would require new arithmetic information
about the actual $R(x)$; it is left open.  In particular, no conductor
claim is inferred merely from (5.2).

Literal Kummer and Artin--Schreier realizations remain separate and closed
in Item 371; this item does not reopen them.

---

## 6. Strategic conclusion

The Item 374 Hasse-subdeterminant route survives the addition of a flat
connection, but only in a tautological way: the connection absorbs
$dq$ through the normalized Frobenius resolvent $(1-C)^{-1}$.  Fixed
rank, fixed Hodge polygon, integrability, Griffiths transversality, and
Frobenius horizontality together still accept every $q$.

Accordingly:

- no second target-forced Hasse condition is obtained;
- no bounded-conductor compatible system is constructed;
- no weighted zero-density statement is proved;
- no part of the $1/36$ ceiling is removed;
- new booking is $0$;
- Route 1 remains `ACTIVE`.

The next admissible Builder step must add genuinely global geometric or
arithmetic structure.  More local filtered-connection packaging of the
same arbitrary coordinate cannot change the ledger.

---

## 7. Strict labels

### PROVED

1. The full general horizontality equations (2.8).
2. The unique integral connection (2.11) for every $q$ on the standard
   two-parameter formal Frobenius base.
3. Integrability and divided-Frobenius compatibility.
4. The horizontality-information-neutral no-go for fixed rank two and
   fixed Hodge weights $(0,1)$.
5. Dense cotangent support on the universal coefficient-moment base.
6. Retained $1/36$ ceiling and zero booking.

### DECLARED EXACT CONTROLS ONLY

The deterministic certificate checks the matrix equations, the truncated
normalized-Frobenius resolvent on declared polynomials, and the universal
dense-support formula.  These are algebraic controls, not a collision or
prime census.

### OPEN

1. A prime-independent geometric family realizing the actual cross-prime
   $Q_0$ as a filtered extension class.
2. Bounded conductor or bounded-complexity after pullback to the actual
   tied selector.
3. Weighted nonconcentration of local splitting, $W_{H,Q}(M)=o(M)$, or
   any strict fixed-$j=1$ ceiling reduction.
4. Route 1 and every conclusion about $e+\pi$.

