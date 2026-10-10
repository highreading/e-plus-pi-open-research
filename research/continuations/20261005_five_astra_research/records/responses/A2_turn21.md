> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 — the shifted mixed digit is the same unit multiple of the shifted norm digit

There is a useful strengthening of the common-high-factor argument: **on all four shifted classes, the entire normalized $Q$-column is divisible by $29$**, not merely its restriction to the old $P$-support. Thus


$$
Z_w\in29^3\mathbb Z_{29}^{b+1},
\qquad
Y\in29^4\mathbb Z_{29}^{b+1}.
$$


This removes the apparent need to compute an additional $P$-digit against a nonzero old $Q$-column.

Using the supplied common-factor construction **conditionally pending A4’s audit**, I prove the following new relation, independently of the numerical norm table:


$$
\boxed{
\frac{M}{29^2}\equiv
(6C_n)^{-1}\frac{D}{29^2}\pmod{29},
\qquad d=25,26,27,28.
}
\tag{A}
$$


Consequently the next norm zero forces—and is equivalent to—the next mixed zero in all four classes.

Conditional on confirmation of the supplied norm formula, the explicit mixed evaluation is


$$
\boxed{
\frac{M}{29^2}
\equiv C_n\bigl(\sigma_0(d)R_0+\sigma_1(d)R_1\bigr)\pmod{29},
}
\tag{B}
$$


where


$$
\boxed{
\begin{array}{c|rrrr}
d&25&26&27&28\\ \hline
\sigma_0(d)&26&12&12&10\\
\sigma_1(d)&3&21&21&3
\end{array}}
\tag{C}
$$


and $\sigma_e(d)=\rho_e(d)/6$ in $\mathbb F_{29}$.

The numerical substitution in (B)–(C) has exactly the pending-audit status of the supplied $\rho$-table. Relation (A) does not depend on that table: a correction to the norm coefficients would immediately correct the mixed coefficients by the same factor $1/6$, without another mixed calculation.

---

## 1. Original domain, actual metric, and residual moments

Throughout,


$$
p=29,\qquad b=3^a,\qquad n=2001b,
$$




$$
a\ge1,\qquad a\equiv432827\pmod{682892},\qquad m_w=1.
$$


The column indices are $0\le j\le b$; all contact inverses retain the actual range $0\le i,j<b$.

The metric is **falling**:


$$
\omega_j=j!\binom{n+2}{j}=(n+2)_{\underline j},
\qquad
\Omega=\operatorname{diag}(\omega_j^2).
$$


For the already weighted reconstructed coordinates, write


$$
W_j=\binom{n+2}{j},\qquad
P=\frac{Z_w}{p^2},\qquad Q=\frac{Y}{p^3},
\qquad Y=\frac{V_w}{b!},
$$




$$
D=P^TP,\qquad M=P^TQ.
$$



Retain


$$
L=p^4,\qquad b=b_*+Lh,\qquad b_*=687936,
$$




$$
n=191110+LN,\qquad N=2001h+1946=3+pA,
$$




$$
h=pH+d,\qquad A=69h+67.
$$


In this answer $25\le d\le28$. These parameters are extracted from the original power $3^a$; they are not freely chosen cylinder parameters.

Set


$$
F(J)=\binom NJ\binom{2N+h-J}{h-J},
\qquad 0\le J\le h,
$$




$$
\ell_0(J)=2N+h-J+1,\qquad \ell_1(J)=N-J.
$$


At the next section,


$$
X_k=\binom Ak\binom{2A+H-k}{H-k},
\qquad 0\le k\le H,
$$


and the required residual high moments are


$$
R_0=\sum_{k=0}^{H}(2A+H-k+1)^2X_k^2\pmod p,
$$




$$
R_1=\sum_{k=0}^{H}(A-k)^2X_k^2\pmod p.
\tag{1.1}
$$


Every displayed sum retains its actual finite boundary.

---

## 2. Precision and complete-force accounting

The new argument ultimately needs only


$$
P\bmod p^2,\qquad Q\bmod p^2,
\tag{2.1}
$$


equivalently


$$
Z_w\bmod p^4,\qquad Y\bmod p^5.
$$


The reason these column precisions determine the scalar digit modulo $p^3$ will be proved in Section 4; it is not assumed in advance.

I start with the complete safe construction already supplied in turn19:


$$
Z_w\bmod p^5,\qquad Y\bmod p^6.
$$


Thus the retained input includes


$$
d_s=s![z^s](1-z+z^2/2)^n,\qquad
F_r=\frac{(b+r)!}{b!},
$$


the complete factorial range $0\le r\le117$, and


$$
c_s=\sum_{r=s}^{117}F_r\binom{2n}{r-s},
\qquad 0\le s\le117.
\tag{2.2}
$$


The safe contact cutoffs are $s\le116$ for $P$ and $s\le145$ for $Q$, with all inverse actions retained at their stated precision.

The established reconstruction bounds reduce these complete inputs to (2.1) as follows.

| Contribution | Treatment for $Z_w\bmod p^4,\ Y\bmod p^5$ |
|---|---|
| Positive $P$-kernel | Retain coefficients modulo $p^2$; resulting support $0\le q\le58$. |
| Positive $Q$-contact kernel | Retain coefficients through valuation $2$; resulting support $0\le q\le58$. |
| Unit boundary $s=0,1$ | Retain complete coefficients at the required precision, not just their first residues. |
| Boundary $2\le s\le30$ | Retain its next coefficient digit as well as its leading digit. |
| Boundary $31\le s\le59$ | Retain the whole contributing block. |
| Factorial inputs $60\le r\le117$ | Their effects vanish only **after reconstruction**, by their coefficient valuation at least $4$ and the compulsory negative-power carry. |
| Higher positive contact grades | Vanish after their coefficient valuation is combined with the two compulsory reconstruction carries. |

The effective negative support is therefore $-60\le q\le0$. The normalization by $p^3$ of the retained $Q$-terms is supplied by low-block factors:

* $W_jB_0(j)$, $W_jB_{-1}(j)$, and $jW_jB_{-2}(j)$ have at least three low factors;
* the remaining boundary terms have their explicit coefficient factors plus the negative-power carry;
* positive contact terms have their explicit factor $p$ plus two reconstruction carries.

Here


$$
B_q(j)=\binom{2n+b-j-1}{b-j-q}.
$$



This termwise accounting matters below: **the normalization is paid for by low factors, not by division of a high binomial factor.**

The complete logarithmic forcing is absent at these precisions only through its supplied whole-force bound


$$
v_p(h_i^F/b!)
\ge
v_p(n!)-v_p(b!)
-\lfloor\log_p(2n+b-1)\rfloor
\ge6.
\tag{2.3}
$$


The actual endpoint remains


$$
Z_{w,b}=W_b\,b\theta^P_{b-1},\qquad
Y_b=W_b(1+b\theta^Q_{b-1}).
\tag{2.4}
$$



---

## 3. New refinement: the common factor always contains an $\ell$-factor

I reuse turn20’s polynomial factorization conditionally, as requested. The additional observation concerns the **natural stripping representatives** of its polynomials, rather than arbitrary representatives of the same coordinate functions.

Write


$$
j=LJ+x,\qquad 0\le x<L,\qquad v=b_*-x.
$$


Define


$$
e(x)=\mathbf1_{x>191112},
\qquad
u(x)=\left\lfloor\frac{382219+v}{L}\right\rfloor,
$$


and


$$
G_x(J)=\ell_1(J)^{e(x)}\ell_0(J)^{u(x)}.
\tag{3.1}
$$



### Lemma 3.1 — retained high-factor ideal

The natural polynomial representatives in the common-factor construction may be chosen in the form


$$
\boxed{
P_{LJ+x}\equiv(-1)^{j+1}F(J)G_x(J)A_x(J)\pmod{p^2},
}
\tag{3.2}
$$




$$
\boxed{
Q_{LJ+x}\equiv(-1)^{j+1}F(J)G_x(J)B_x(J)\pmod{p^2},
}
\tag{3.3}
$$


with integral polynomial coefficients modulo $p^2$. Moreover,


$$
\boxed{e(x)+u(x)\ge1\qquad(0\le x<L).}
\tag{3.4}
$$



#### Proof of the refinement

For every retained Laurent power $q$, put


$$
r=\mathbf1_{v-q<0}.
$$


The exact high factorial ratio in turn20’s stripping construction is


$$
\frac{N!}{J!(N-J-e)!}
\frac{(2N+h-J+u)!}{(h-J-r)!(2N)!}.
$$


The elementary contiguous factorial identities give


$$
\boxed{
F(J)\ell_1(J)^e\ell_0(J)^u(h-J)^r
=
F(J)G_x(J)(h-J)^r.
}
\tag{3.5}
$$



The factors $e,u$ are independent of $q$. The remaining low factorial units multiply (3.5); they do not cancel a factor of $G_x$. Section 2’s termwise normalization shows that division by $p^2$ for $P$, or by $p^3$ for $Q$, is supplied entirely by low carries and explicit coefficient factors. Therefore it also does not divide $G_x$.

Freezing the bounded coefficient functions at $x$, at the precisions justified in the supplied construction, preserves this factor. In particular, replacing a boundary coefficient $j$ by $x$ introduces $LJ$; with the compulsory reconstruction factor this is zero modulo $p^5$. Thus all retained terms still contain $G_x$, proving (3.2)–(3.3).

The values of $e,u$ are especially simple:


$$
(e,u)=
\begin{cases}
(0,1),&0\le x\le191112,\\
(1,1),&191112<x\le362874,\\
(1,0),&362874<x<L.
\end{cases}
\tag{3.6}
$$


Hence (3.4).

If $r=1,J=h$, the original lower index is invalid; the factor $h-J$ in (3.5) gives exactly zero. No division by $F(J)$, or by a value of $G_x(J)$, has occurred. ∎

The actual coordinate ranges remain


$$
\begin{cases}
0\le J\le h,&0\le x\le b_*,\\
0\le J\le h-1,&b_*<x<L.
\end{cases}
\tag{3.7}
$$


No extension of the second range is needed for the argument below.

---

## 4. The entire $Q$-column acquires the missing factor

### Lemma 4.1 — shifted high products

For every actual $0\le J\le h$, in all four shifted classes,


$$
\boxed{
p\mid F(J)\ell_0(J),\qquad
p\mid F(J)\ell_1(J).
}
\tag{4.1}
$$



#### Proof

Write $J=pk+t$, $0\le t<p$.

A nonzero $F(J)\bmod p$ requires, by Lucas,


$$
0\le t\le3,\qquad 0\le d-t\le22.
\tag{4.2}
$$


For $d=26,27,28$, no such $t$ exists, so $F(J)=0\bmod p$.

For $d=25$, the only possible term is $t=3$. At this residue,


$$
\ell_1(J)\equiv3-t=0,
$$




$$
\ell_0(J)\equiv d+7-t=32-t=0\pmod p.
$$


This proves both statements without requiring $F(J)$ to be a unit. ∎

Because $G_x$ contains at least one of these two linear factors, (4.1) implies


$$
p\mid F(J)G_x(J)
$$


for every actual coordinate. Lemma 3.1 now yields the new whole-column assertion


$$
\boxed{
P,Q\in p\mathbb Z_p^{b+1}.
}
\tag{4.3}
$$


In original normalizations,


$$
\boxed{
Z_w\in p^3\mathbb Z_p^{b+1},
\qquad
Y\in p^4\mathbb Z_p^{b+1}.
}
\tag{4.4}
$$



### Why the available precision is adequate

Define the integral columns


$$
P^\sharp=P/p=Z_w/p^3,\qquad
Q^\sharp=Q/p=Y/p^4.
$$


Then


$$
\boxed{
D/p^2=(P^\sharp)^TP^\sharp,\qquad
M/p^2=(P^\sharp)^TQ^\sharp.
}
\tag{4.5}
$$



Thus only $P,Q\bmod p^2$ are required. More explicitly, errors of size $p^2$ in either normalized column pair with an actual column divisible by $p$, producing scalar errors divisible by $p^3$.

This is why a new computation of $P,Q\bmod p^3$ is unnecessary. The apparent extra-precision obstruction disappears after proving (4.3).

---

## 5. Whole shifted contraction, including all support outside $\mathcal X$

Let $\mathcal X$ be the established old four-digit $P$-support. On it,


$$
G_x(J)=\ell_{e(x)}(J).
$$


The supplied leading polynomial identities are


$$
G_xA_x\equiv C_n c(x)\ell_{e(x)}\pmod p,
$$




$$
G_xB_x\equiv \xi(x)\ell_{e(x)}\pmod p.
$$


Since $\ell_e$ is a nonzero polynomial with unit leading coefficient, cancellation **in the polynomial ring** gives


$$
A_x\equiv C_n c(x),\qquad B_x\equiv\xi(x)\pmod p
\quad(x\in\mathcal X).
\tag{5.1}
$$


This is not division by a possibly zero value $F(J)$ or $\ell_e(J)$.

For $x\notin\mathcal X$, the supplied leading $P$-multiplier is the zero polynomial. Cancelling the nonzero polynomial $G_x\bmod p$ gives


$$
A_x\equiv0\pmod p.
$$


Together with $p\mid FG_x$, this proves


$$
\boxed{
P_{LJ+x}\equiv0\pmod{p^2}\qquad(x\notin\mathcal X).
}
\tag{5.2}
$$


This also recovers, in the present interface, the shifted-support conclusion of turn19.

Define the **integral** high quotients


$$
S_e(J)=\frac{\ell_e(J)F(J)}p,\qquad e=0,1.
\tag{5.3}
$$


Their integrality follows from (4.1), even when $F(J)=0\bmod p$.

Equations (3.2)–(3.3) and (5.1) yield


$$
P^\sharp_{LJ+x}
\equiv(-1)^{j+1}C_n c(x)S_{e(x)}(J)\pmod p,
$$




$$
Q^\sharp_{LJ+x}
\equiv(-1)^{j+1}\xi(x)S_{e(x)}(J)\pmod p
\qquad(x\in\mathcal X).
\tag{5.4}
$$



Outside $\mathcal X$, $P^\sharp=0\bmod p$. Since $Q^\sharp$ is now integral **everywhere**, every such coordinate contributes zero to the whole mixed digit.

This settles the new-support issue: there is no omitted term from “the next $P$-coefficient against the old $Q$-column,” because that old $Q$-column is zero globally on these four classes.

### Contracting the low coordinates

Use the supplied exact low constants


$$
\kappa_0=11,\qquad\kappa_1=18,
\qquad
g_0=26,\qquad g_1=3,
$$


where


$$
\sum_{\substack{x\in\mathcal X\\e(x)=e}}c(x)^2=\kappa_e,
\qquad
\sum_{\substack{x\in\mathcal X\\e(x)=e}}c(x)\xi(x)=g_e.
$$


They satisfy


$$
g_e=\kappa_e/6\pmod p.
\tag{5.5}
$$



Every $x\in\mathcal X$ has the actual range $0\le J\le h$. Therefore (4.5) and (5.4) give the complete contractions


$$
\frac D{p^2}
\equiv
C_n^2\sum_{e=0}^1\kappa_e
\sum_{J=0}^{h}S_e(J)^2\pmod p,
\tag{5.6}
$$




$$
\frac M{p^2}
\equiv
C_n\sum_{e=0}^1g_e
\sum_{J=0}^{h}S_e(J)^2\pmod p.
\tag{5.7}
$$


Substitution of (5.5) proves


$$
\boxed{
\frac M{p^2}\equiv
(6C_n)^{-1}\frac D{p^2}\pmod p.
}
\tag{5.8}
$$



No unevaluated collection of low-coordinate constants remains.

---

## 6. Residual high moments and the four explicit coefficient functions

I now use, conditionally pending A4’s audit, the supplied norm evaluation


$$
\frac D{p^2}
\equiv
C_n^2\bigl(\rho_0(d)R_0+\rho_1(d)R_1\bigr)\pmod p.
\tag{6.1}
$$


Its exact fifth-digit boundaries are consistent with the contraction above:

* For $t\le d$, $J=pk+t$ has $0\le k\le H$.
* For $t>d$, its range is $0\le k\le H-1$. In the four shifted classes these terms have both a first-binomial carry and a second-binomial carry, so $S_e(J)=0\bmod p$.
* The exceptional no-carry case is $d=25,t=3$. Here
  

$$
\ell_0(pk+3)=p(2A+H-k+1),\qquad
  \ell_1(pk+3)=p(A-k),
$$


  giving precisely the two moments $R_0,R_1$.
* In every remaining contributing case, the single carry in one of the binomials gives, by the usual one-step factorial stripping and contiguous identity, respectively the high multiplier
  

$$
(2A+H-k+1)X_k
  \quad\text{or}\quad
  (A-k)X_k.
$$


  Terms with two carries vanish after the division defining $S_e$.

Thus the whole shifted contraction involves the displayed finite $R_0,R_1$, not extra terminal moments or an independently chosen high-index range.

Combining (5.8) with (6.1),


$$
\boxed{
\frac M{p^2}
\equiv
\frac{C_n}{6}
\bigl(\rho_0(d)R_0+\rho_1(d)R_1\bigr)\pmod p.
}
\tag{6.2}
$$


The explicit coefficient functions are therefore


$$
\sigma_0(d)=5\rho_0(d),\qquad
\sigma_1(d)=5\rho_1(d)\pmod{29},
$$


since $6^{-1}=5\bmod29$. Using the supplied table:


$$
\begin{array}{c|rrrr}
d&25&26&27&28\\ \hline
\rho_0(d)&11&14&14&2\\
\rho_1(d)&18&10&10&18\\ \hline
\sigma_0(d)&26&12&12&10\\
\sigma_1(d)&3&21&21&3
\end{array}
\tag{6.3}
$$



Because $C_n$ is a unit on the original domain,


$$
\boxed{
D/p^2=0\pmod p
\iff
M/p^2=0\pmod p.
}
\tag{6.4}
$$


If this digit is nonzero, then $\delta=\mu=2$. If it vanishes, both valuations are at least $3$. Nothing here bounds their subsequent difference.

---

## 7. The exact endpoint contributes zero at this shifted digit

The endpoint has been retained throughout, including the $1$ in


$$
Y_b=W_b(1+b\theta^Q_{b-1}).
$$



There is also a direct endpoint check at the present precision. The supplied low-factorial calculation gives


$$
W_b/p^3\equiv5(N-h)\binom Nh\pmod p.
$$


Since $N\equiv3$ and $h\equiv d$, Lucas gives


$$
\binom Nh\equiv\binom3d\binom AH=0\pmod p
\qquad(25\le d\le28).
$$


Hence


$$
W_b\in p^4\mathbb Z_p.
$$


The integral reconstructed endpoint formulas imply


$$
Z_{w,b},Y_b\in p^4\mathbb Z_p.
$$


Its contribution to the assigned mixed digit is therefore


$$
\left[\frac M{p^2}\right]_{j=b}
=\frac{Z_{w,b}Y_b}{p^7}
\equiv0\pmod p.
\tag{7.1}
$$


This is an evaluated endpoint contribution, not a deletion of the endpoint.

---

## 8. Final gcd, actual primitive denominator, nonvanishing, and whole error

Retain the actual least two-column denominator:


$$
N_B=d_B[u,v],\qquad v_{29}(d_B)=0.
$$


With the actual falling metric,


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2}.
$$


The final normalization is


$$
g_B=\gcd(A_B,|H_B|),\qquad
p_n=H_B/g_B,\qquad q_n=A_B/g_B>0.
$$


The primitive multiplier is $1/g_B$ on the integer Gram pair, or $d_B^2/g_B$ on its rational Gram pair. The actual reduced denominator is $q_n$, not $d_B$, a row-clearer, or a contact determinant.

For


$$
\delta=v_{29}(D),\qquad\mu=v_{29}(M),
$$


the supplied exact interface remains


$$
v_{29}(g_B)=
\min\{4F_n+4+\delta,\;2F_n+F_b+5+\mu\},
$$




$$
v_{29}(q_n)=
\max\{0,\;2F_n-F_b-1+\delta-\mu\},
$$


where $F_n=v_{29}(n!)$, $F_b=v_{29}(b!)$.

Norm nonvanishing follows from positivity. Mixed nonvanishing retains the supplied original-family nonvanishing dependency; it is not inferred from the present local congruence.

For the whole real error


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


the exact evaluated primitive form is


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
$$


At the supplied status of the complete signed-error theorem,


$$
\epsilon_n>0\quad\text{eventually},
$$




$$
\log|\epsilon_n|
=-\left(2+\frac1{2001}\right)n\log(1+\sqrt2)+o(n).
$$


Thus the whole primitive form is eventually negative and nonzero. The complete exponential residual, logarithmic force, factorial/contact boundary, and endpoint remain included.

This finite-depth result supplies neither a global denominator bound nor a proof or disproof of irrationality of $e+\pi$.

---

# Concluding ledger

## (1) New result and proof status

**Proved in the supplied common-factor interface, retained conditionally pending A4’s audit:**

* The natural high multiplier contains
  

$$
G_x=\ell_1^{e(x)}\ell_0^{u(x)},\qquad e(x)+u(x)\ge1,
$$


  at every low coordinate.
* On all four original shifted classes,
  

$$
Y\in29^4\mathbb Z_{29}^{b+1}
$$


  globally.
* This makes the available column precision sufficient and eliminates every new-support contribution outside $\mathcal X$ at the assigned mixed digit.
* The whole relation is
  

$$
\boxed{M/29^2=(6C_n)^{-1}D/29^2\pmod{29}.}
$$


* The actual endpoint contribution is zero.
* Conditional on the supplied norm table, the explicit mixed coefficients are (6.3).

The low constants are supplied finite arithmetic inputs. The uniform implication follows from the high-factor ideal, Lucas separation, and exact finite boundaries—not from finite sampling.

## (2) Exact remaining bottleneck

At this layer there is no remaining mixed low-constant functional: the residual is zero.

The dependency still pending is A4’s audit of the common-factor interface and numerical norm evaluation. Beyond that, another common zero leaves the next relative-valuation problem unresolved. Ultimately one still needs justified all-depth arithmetic control and the **actual final primitive denominator across all primes**, together with the nonzero whole error, to obtain an irrationality argument.

## (3) Computation request

**None.** The supplied $(\kappa_0,\kappa_1,g_0,g_1)$ suffice. Any audited correction to the norm coefficient table transfers to the mixed table by multiplication by $1/6$; no additional low-coordinate enumeration is needed.
