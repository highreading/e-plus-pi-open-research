> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The exact residual quotient of the balanced centered-cosh product image

Checked: 2026-08-27 UTC

## 1. Statement

Put



$$
F(x)=\frac1{2\cosh\sqrt x}=\sum_{j\geq0}f_jx^j,
 \qquad {\cal P}_d=\mathbb Q[x]_{\leq d}.                    \tag{1}
$$



For $q\geq1$, let $Q=Q_q$ and $P=P_q$ be the denominator and
numerator of the diagonal $[q/q]$ Padé approximant to $F$:



$$
\deg Q=\deg P=q,\qquad FQ-P=O(x^{2q+1}).                   \tag{2}
$$



For $r\in\{1,2\}$, set $n=3q+r$, $D=n-1$, and



$$
{\cal U}_{q,r}=
 \left\{C\in\mathbb Q[z]_{\leq D}:
 [z^k]F(z^2)C(z)=0\quad(n\leq k\leq n+q)\right\}.           \tag{3}
$$



Its even endpoint-product image, written in $x=z^2$, is



$$
{\cal E}_{q,r}=
 \operatorname {span}_{\mathbb Q}
 \left\{\frac{C(z)D(z)+C(-z)D(-z)}2:
 C,D\in{\cal U}_{q,r}\right\}
 \subseteq{\cal P}_{3q+r-1}.                               \tag{4}
$$



The companion Padé-ideal theorem proves



$$
Q{\cal P}_{2q}\subseteq{\cal E}_{q,1}\quad(q\geq2),
 \qquad
 xQ{\cal P}_{2q}\subseteq{\cal E}_{q,2}\quad(q\geq1).       \tag{5}
$$



Let $G$ and $R$ be the denominator and numerator of the adjacent Padé
approximant of type $[q+1/q-1]$:



$$
\deg G=q-1,\qquad \deg R=q+1,\qquad
 FG-R=O(x^{2q+1}).                                         \tag{6}
$$



For $q=1$ this means $G=1$.  Reduction modulo $Q$ is denoted by



$$
\rho_Q:\mathbb Q[x]\longrightarrow
 A:=\mathbb Q[x]/(Q),                                      \tag{7}
$$



always using the representative of degree at most $q-1$.  The first
quotient theorem is



$$
\boxed{\rho_Q({\cal E}_{q,1})=G^2{\cal P}_{q-2}\subset A
 \quad(q\geq2).}                                           \tag{8}
$$



Products displayed in $A$ are understood modulo $Q$.  The polynomial
$G$ is a unit in $A$, so the right side of (8) has dimension $q-1$.
Together with (5), this gives



$$
\boxed{
 \dim{\cal E}_{q,1}=3q,\qquad
 \operatorname {codim}_{{\cal P}_{3q}}{\cal E}_{q,1}=1
 \quad(q\geq2).}                                           \tag{9}
$$



The omitted edge is genuinely exceptional:



$$
{\cal E}_{1,1}=Q_1^2{\cal P}_1,\qquad
 \dim{\cal E}_{1,1}=2,\qquad
 \operatorname {codim}_{{\cal P}_3}{\cal E}_{1,1}=2.       \tag{10}
$$



For $r=2$, define



$$
\begin{split}
 \Phi:{\cal P}_{3q+1}&\longrightarrow\mathbb Q\oplus A,\\
 T&\longmapsto
 \left(T(0),\rho_Q\!\left(\frac{T-T(0)}x\right)\right).
 \end{split}                                               \tag{11}
$$



Its kernel is $xQ{\cal P}_{2q}$.  Let $E$ be the even minimal Padé
factor defined in Section 6.  It has $E(0)\ne0$.  With the convention
${\cal P}_{-1}=0$, the second quotient theorem is



$$
\boxed{
 \Phi({\cal E}_{q,2})=
 \mathbb Q\Phi(E^2)\ \oplus\
 \bigl(\{0\}\oplus G^2{\cal P}_{q-2}\bigr)
 \quad(q\geq1).}                                           \tag{12}
$$



The sum is direct because the first coordinate of $\Phi(E^2)$ is
$E(0)^2\ne0$, whereas the second summand has first coordinate zero.
Thus



$$
\boxed{
 \dim{\cal E}_{q,2}=3q+1,\qquad
 \operatorname {codim}_{{\cal P}_{3q+1}}{\cal E}_{q,2}=1
 \quad(q\geq1).}                                           \tag{13}
$$



Equations (8)--(13) are all-parameter rational statements.  They do not
assert an integral Smith or saturation theorem.

## 2. Normality and the adjacent cross identity

The product



$$
\cosh\sqrt x=\prod_{\ell\geq0}(1+t_\ell x),
 \qquad t_\ell=\frac4{\pi^2(2\ell+1)^2}>0                  \tag{14}
$$



gives



$$
f_j=\frac{(-1)^j}{2}h_j(t_0,t_1,\ldots).                  \tag{15}
$$



All relevant Schur specializations converge because
$\sum_\ell t_\ell<\infty$, and they are strictly positive.  Every
Toeplitz determinant used for a Padé entry of type $[L/M]$,
$L\geq M$, is, after row and column signs, a power of $2^{-1}$ times
such a Schur specialization.  For example,



$$
\det[f_{L+i-j}]_{i,j=1}^{M}
   =\pm2^{-M}s_{(L^M)}(t_0,t_1,\ldots)\ne0.                 \tag{16}
$$



Normalize the denominator constant to one.  The determinant (16)
uniquely solves for its remaining coefficients.  Replacing the
terminal denominator column gives, up to sign,
$2^{-M}s_{((L+1)^M)}$, so the denominator has degree exactly $M$.
If the numerator had degree less than $L$, the denominator vector
would annihilate the square matrix
$[f_{L+i-j}]_{i,j=0}^{M}$, whose determinant is, up to sign,
$2^{-(M+1)}s_{(L^{M+1})}\ne0$.  Thus the numerator has degree
exactly $L$ and the Padé entry has no defect.  This proves all
normality used below without finite extrapolation.

The two approximants in (2) and (6) give



$$
RQ-PG=O(x^{2q+1}).                                        \tag{17}
$$



The left side has degree at most $2q+1$, and its leading term comes
only from $RQ$.  Therefore



$$
\boxed{
 RQ-PG=\kappa x^{2q+1},\qquad
 \kappa=\operatorname {lc}(R)\operatorname {lc}(Q)\ne0.}   \tag{18}
$$



If $Q$ and $G$ had a common root, (18) would force it to be zero.
Their constant terms are nonzero.  Hence



$$
\gcd(Q,G)=1,                                               \tag{19}
$$



so $G$ is a unit in $A$.

## 3. Parity blocks and Padé remainders for $r=1$

Write $C(z)=A_0(x)+zA_1(x)$.  If $q=2a$, the parity blocks in
${\cal U}_{q,1}$ are



$$
\begin{aligned}
 V_0&=\{A\in{\cal P}_{3a}:[x^j](FA)=0,\
                         3a+1\leq j\leq4a\},\\
 V_1&=\{B\in{\cal P}_{3a-1}:[x^j](FB)=0,\
                         3a\leq j\leq4a\}.
 \end{aligned}                                             \tag{20}
$$



If $q=2a+1$, they coincide:



$$
V_0=V_1=:V=
 \{A\in{\cal P}_{3a+1}:[x^j](FA)=0,\
                         3a+2\leq j\leq4a+2\}.             \tag{21}
$$



In either case



$$
{\cal E}_{q,1}=V_0^2+xV_1^2.                              \tag{22}
$$



Polynomial division by $Q$, using (2), gives



$$
\begin{array}{lll}
 q=2a:&V_0=Q{\cal P}_{a}\oplus W_0,
       &V_1=Q{\cal P}_{a-1}\oplus W_1,\\[1mm]
 q=2a+1:&V=Q{\cal P}_{a}\oplus W.
 \end{array}                                               \tag{23}
$$



Each $W$ consists of the representatives of degree at most $q-1$
satisfying the corresponding constraints in (20) or (21).  Those
constraints have full row rank.  For $I=[A,A+c-1]$, select coefficient
columns $q-c,\ldots,q-1$.  After signs, the selected determinant is



$$
2^{-c}\det[h_{L+r-s}]_{r,s=0}^{c-1}
 =2^{-c}s_{(L^c)}(t_0,t_1,\ldots)>0,
 \qquad L=A-q+c.                                           \tag{24}
$$



In every block above $L=q+1$.  Therefore



$$
\begin{array}{c|ccc}
 &W_0&W_1&W\\ \hline
 \dim&a&a-1&a.
 \end{array}                                               \tag{25}
$$



## 4. The $G$-Krylov description

The exact remainder identities are



$$
\boxed{
 \begin{array}{ll}
 q=2a:&
 W_0=\rho_Q(G{\cal P}_{a-1}),\qquad
 W_1=\rho_Q(G{\cal P}_{a-2}),\\[1mm]
 q=2a+1:&
 W=\rho_Q(G{\cal P}_{a-1}).
 \end{array}}                                              \tag{26}
$$



A polynomial space with negative degree is zero.  For $q=2a$,
$0\leq s\leq a-1$, and $3a+1\leq j\leq4a$, one has



$$
q+2\leq j-s\leq2q.                                        \tag{27}
$$



Thus $[x^j](Fx^sG)=0$ by the high zero block of the
$[q+1/q-1]$ entry.  Replacing $x^sG$ by $\rho_Q(x^sG)$ does
not change these coefficients: the quotient by $Q$ has degree at most
$s-1$, while $FQ=P+O(x^{2q+1})$ and $q+s-1<j\leq2q$.
Hence $\rho_Q(x^sG)\in W_0$.  The same calculation for
$0\leq s\leq a-2$ and $3a\leq j\leq4a$ proves membership in
$W_1$.

For $q=2a+1$, use $0\leq s\leq a-1$ and
$3a+2\leq j\leq4a+2$; again



$$
q+2\leq j-s\leq2q.                                        \tag{28}
$$



Since $G$ is a unit in $A$, the displayed Krylov vectors are
independent.  Their counts agree with (25), proving (26).

## 5. Proof of the $r=1$ quotient

Modulo $Q$, every product in (22) containing a $Q$-multiple vanishes.
For $q=2a\geq2$, (23) and (26) give



$$
\begin{aligned}
 \rho_Q({\cal E}_{q,1})
  &=W_0^2+xW_1^2\\
  &=G^2{\cal P}_{2a-2}+xG^2{\cal P}_{2a-4}
    =G^2{\cal P}_{q-2}.
 \end{aligned}                                             \tag{29}
$$



For $q=2a+1\geq3$,



$$
\rho_Q({\cal E}_{q,1})
 =W^2+xW^2
 =G^2({\cal P}_{2a-2}+x{\cal P}_{2a-2})
 =G^2{\cal P}_{q-2}.                                       \tag{30}
$$



Because $G$ is a unit and $q-2<q$, this space has dimension $q-1$.
The kernel of reduction from ${\cal P}_{3q}$ to $A$ is exactly
$Q{\cal P}_{2q}$, already contained in ${\cal E}_{q,1}$ by (5).
This proves (8)--(9).

When $q=1$, both parity blocks are $\mathbb QQ_1$, so (10) follows.
The exceptional image does not contain $Q_1{\cal P}_2$; the quotient
used in (8) is not defined there.

## 6. The extra factor and an exact Padé syzygy for $r=2$

Evaluation at zero gives



$$
\ker\bigl(C\mapsto C(0):{\cal U}_{q,2}\to\mathbb Q\bigr)
 =z{\cal U}_{q,1}.                                         \tag{31}
$$



Indeed, division by $z$ shifts the zero interval $[3q+2,4q+2]$ back
to $[3q+1,4q+1]$, with exactly the degree bound for
${\cal U}_{q,1}$.

Define



$$
c=\left\lfloor\frac q2\right\rfloor+1,\qquad
 A_*=\begin{cases}
       3a+1,&q=2a,\\
       3a+3,&q=2a+1.
      \end{cases}                                          \tag{32}
$$



Let $E,S$ be the denominator and numerator of the normal Padé entry
of type



$$
[A_*-1/c].                                                 \tag{33}
$$



Then



$$
\deg E=c,\qquad \deg S=A_*-1,\qquad E(0)\ne0,\qquad
 FE-S=O(x^{2q+2}).                                         \tag{34}
$$



Its zero block is $A_*,\ldots,2q+1$, exactly the even-parity block
needed in ${\cal U}_{q,2}$.  Identifying $E(x)$ with $E(z^2)$, its
$z$-degree also satisfies the endpoint bound.  Thus
$E\in{\cal U}_{q,2}$, and (31) gives



$$
{\cal U}_{q,2}=z{\cal U}_{q,1}\oplus\mathbb QE.            \tag{35}
$$



Solve



$$
\begin{pmatrix}G&Q\\R&P\end{pmatrix}
 \binom HK=\binom ES.                                      \tag{36}
$$



By (18), Cramer's rule gives



$$
H=\frac{QS-PE}{\kappa x^{2q+1}},\qquad
 K=\frac{ER-GS}{\kappa x^{2q+1}}.                          \tag{37}
$$



Both quotients are polynomials.  For example,



$$
QS-PE=Q(S-FE)+E(FQ-P)=O(x^{2q+1}),                        \tag{38}
$$



and the second numerator is treated identically.  Degree comparison
in the first quotient gives



$$
\deg H\leq A_*-q-2=
 \begin{cases}
  a-1,&q=2a,\\
  a,&q=2a+1.
 \end{cases}                                               \tag{39}
$$



Consequently



$$
\boxed{
 E=GH+QK,\qquad
 \rho_Q(E)\in
 \begin{cases}
  G{\cal P}_{a-1},&q=2a,\\
  G{\cal P}_{a},&q=2a+1.
 \end{cases}}                                              \tag{40}
$$



This exact syzygy prevents the extra lift direction from enlarging the
residual quotient.

## 7. Proof of the $r=2$ quotient

Write a member of ${\cal U}_{q,1}$ as $A(x)+zB(x)$.  Expanding the
products in (35) and taking their even parts gives



$$
{\cal E}_{q,2}
 =x{\cal E}_{q,1}
  +\operatorname {span}\bigl(E^2,\ xE V_1^{\rm old}\bigr), \tag{41}
$$



where $V_1^{\rm old}$ is the odd parity block of
${\cal U}_{q,1}$.

For $q\geq2$, the image of $x{\cal E}_{q,1}$ under (11) is



$$
\{0\}\oplus G^2{\cal P}_{q-2}.                            \tag{42}
$$



The mixed term in (41) lies in the same space.  If $q=2a$, then
(23), (26), and (40) give



$$
\rho_Q(EV_1^{\rm old})
 \subseteq G^2{\cal P}_{(a-1)+(a-2)}
 \subseteq G^2{\cal P}_{q-2}.                              \tag{43}
$$



If $q=2a+1$, they give



$$
\rho_Q(EV_1^{\rm old})
 \subseteq G^2{\cal P}_{a+(a-1)}
 =G^2{\cal P}_{q-2}.                                       \tag{44}
$$



The only remaining direction is $\Phi(E^2)$.  Its first coordinate is
nonzero, proving equality and directness in (12).

For $q=1$, put



$$
A=f_1,\qquad B=f_2,\qquad C=f_3,\qquad
 Q_1=A-Bx,\qquad E=B-Cx.                                   \tag{45}
$$



Normality gives $B\ne0$ and $AC-B^2\ne0$.  The parity blocks of
${\cal U}_{1,2}$ are



$$
V_0=\operatorname {span}(E,xQ_1),\qquad
 V_1=\mathbb QQ_1.                                         \tag{46}
$$



The three direct identities in the Padé-ideal theorem show that
$xQ_1{\cal P}_2\subseteq V_0^2+xV_1^2$.  This ideal has dimension
three and zero constant term, while $E^2$ belongs to the product image
and has nonzero constant term.  On the other hand (46) supplies at most
$3+1=4$ product directions.  Hence the product image has dimension
four in ${\cal P}_4$, and its quotient is precisely
$\mathbb Q\Phi(E^2)$.  This proves (12)--(13) at the edge.

## 8. The unique rational annihilators

The top-coefficient functional



$$
\omega([T])=[x^{q-1}]\rho_Q(T)                            \tag{47}
$$



is Frobenius on $A$: if $T\ne0$ has degree $d<q$, then
$\omega(x^{q-1-d}T)\ne0$.  From (8), the unique annihilator of the
$r=1$ residual space, up to a nonzero scalar, is



$$
\boxed{\lambda([T])=\omega(G^{-2}T).}                     \tag{48}
$$



Indeed, it annihilates $G^2{\cal P}_{q-2}$, which has codimension one
in $A$.  Its moments



$$
h_j=\lambda(x^j)                                          \tag{49}
$$



obey



$$
\sum_{k=0}^q[x^k]Q\,h_{j+k}=0\qquad(j\geq0).              \tag{50}
$$



Identity (18) also gives



$$
G^{-1}\equiv-\frac{P}{\kappa x^{2q+1}}\pmod Q,\qquad
 G^{-2}\equiv\frac{P^2}{\kappa^2x^{4q+2}}\pmod Q,          \tag{51}
$$



where $x$ is a unit because $Q(0)\ne0$.

For $r=2$, write



$$
E^2=E(0)^2+xR_E.                                          \tag{52}
$$



On $\mathbb Q\oplus A$, the unique annihilator of (12) is



$$
\boxed{
 \eta(c,[T])=\lambda([T])-
        c\,\frac{\lambda([R_E])}{E(0)^2}.}                 \tag{53}
$$



For $q=1$, use $G=1$, ${\cal P}_{-1}=0$, and the same formula; then
$\lambda=\omega$ on the one-dimensional algebra $A$.

If $(h_0,h_1)\ne(0,0)$, the corresponding low-degree kernel direction
for (49) is $h_1-h_0x$.  No nonvanishing assertion about either
individual coordinate is used.

## 9. An exact resultant identity and the integral boundary

Write



$$
Q(x)=q_0+q_1x+\cdots+q_qx^q.                              \tag{54}
$$



With the standard resultant convention, (18) implies



$$
\boxed{
 \operatorname {Res}(Q,P)\operatorname {Res}(Q,G)
 =\frac{\kappa^q q_0^{\,2q+1}}{q_q^2}.}                   \tag{55}
$$



Let $\alpha_1,\ldots,\alpha_q$ be the roots of $Q$, with multiplicity.
At those roots, (18) gives



$$
-P(\alpha_i)G(\alpha_i)=\kappa\alpha_i^{2q+1}.             \tag{56}
$$



Multiply (56), use $\prod_i\alpha_i=(-1)^q q_0/q_q$, and include the
leading-coefficient factors in the two resultants.  The signs cancel,
yielding (55).

After primitive integral normalizations of $Q$ and $G$, multiplication
by $G$ on the rational monomial basis of $A$ has determinant



$$
\frac{\operatorname {Res}(Q,G)}{q_q^{q-1}}.               \tag{57}
$$



This is a genuine arithmetic obstruction, but it does not determine the
Smith data of the residual lattice:

* the integral content depends on local valuations of all maximal
  minors of the first $q-1$ columns of multiplication by $G^2$, not
  only on its full determinant;
* (55) does not prove local saturation at primes dividing a resultant
  or a leading coefficient;
* under the previously proved standard $O(q^2\log q)$
  coefficient-height bound for cleared Padé entries, a generic
  $q$-dimensional adjugate or maximal-minor clearing can still cost
  $O(q^3\log q)$.

Thus the theorem proves exact rational codimension and a structured
annihilator, but not an $O(q^2\log q)$ primitive-survivor height bound.
That requires a separate local-prime or Smith theorem.

## 10. Deterministic replay and logical boundary

The companion files are:

* scripts/centered_cosh_pade_residual_quotient_certificate.py
* results/centered_cosh_pade_residual_quotient_certificate.json
* results/centered_cosh_pade_residual_quotient_hashes.sha256

The replay verifies, on a finite exact grid, Padé normality and zero
blocks, (18)--(19), the Krylov equalities (26), both quotient formulas,
the syzygy (37)--(40), the annihilators, the $q=1$ edges, and (55).
Those computations are diagnostics; the all-$q$ proof is (14)--(57).

Nothing in this note proves that $e+\pi$ is algebraic or
transcendental.
