> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 — the whole second mixed relation on $d\le 24,\ T=0$

The second mixed digit can be evaluated **without computing another collection of low constants**. The key additional fact is a four-digit factorization at precision $29^2$: after the actual column normalizations, both columns have a common high binomial factor, and their remaining factors are polynomials in the high coordinate modulo $29^2$.

This makes every first-order correction left after the leading proportionality a multiple of the genuine residual norm $T$. It includes the newly admitted $P$-support, the next $Q$-digit, all retained factorial and contact blocks, and the endpoint.

On the assigned original domain, for $0\le d\le24$ and $T=0$, the result is


$$
\boxed{
M_1=(6C_n)^{-1}D_1
=\frac{C_n}{6}\bigl(f(d)T_1+\beta(d)U\bigr)
\pmod{29}.
}
$$


In particular,


$$
\boxed{D_1=0\iff M_1=0}
$$


on this locus. This is a second-depth statement, not an all-depth valuation bound.

The proof below uses the supplied exact values $g_0=26,\ g_1=3$ only as finite arithmetic input. The infinite conclusion comes from the uniform factorization and finite-boundary argument, not from extrapolating that calculation.

---

## 1. Domain, actual columns, and precisions

Throughout,


$$
p=29,\qquad b=3^a,\qquad n=2001b,\qquad m_w=1,
$$




$$
a\ge1,\qquad a\equiv432827\pmod{682892}.
$$


All column coordinates remain $0\le j\le b$, and the contact inverses remain restricted to $0\le i,j<b$.

The metric is the corrected **falling** metric:


$$
\omega_j=j!\binom{n+2}{j}=(n+2)_{\underline j},
\qquad
\Omega=\operatorname{diag}(\omega_j^2).
$$


For the reconstructed columns, put


$$
W_j=\binom{n+2}{j},\qquad
P=\widehat P=\frac{Z_w}{p^2},\qquad
Q=\widehat Q=\frac{Y}{p^3},\qquad Y=\frac{V_w}{b!},
$$


and


$$
D=P^TP,\qquad M=P^TQ.
$$



Retain the actual higher parameters


$$
L=p^4,\qquad b=b_*+Lh,\qquad b_*=687936,
$$




$$
n=191110+LN,\qquad N=2001h+1946=3+pA,
$$




$$
h=pH+d,\qquad 0\le d<p,\qquad A=69h+67.
$$


These are determined by the original $3^a$. No independent high digits are introduced.

Define


$$
F(J)=\binom NJ\binom{2N+h-J}{h-J},\qquad 0\le J\le h,
$$


and


$$
X_k=\binom Ak\binom{2A+H-k}{H-k},\qquad 0\le k\le H.
$$


Thus


$$
\mathcal T=\sum_{k=0}^{H}X_k^2,\qquad T=\mathcal T\bmod p.
$$


On $T=0$,


$$
T_1=\frac{\mathcal T}{p}\bmod p,\qquad
U=\sum_{k=0}^{H}kX_k^2\bmod p.
$$



To determine $D,M\bmod p^2$, it suffices to retain


$$
Z_w\bmod p^4,\qquad Y\bmod p^5.
$$


I use the complete bounded kernels supplied in the archive, with the safe higher cutoffs of turn19 available before the reductions below.

---

## 2. All force blocks retained before cancellation

Write


$$
B_q(j)=\binom{2n+b-j-1}{b-j-q}.
$$


The complete reconstruction, including the absorbed endpoint, is


$$
\mathscr R\!\left(\sum_q a_q(j)r^q\right)_j
=(-1)^{j+1}W_j\sum_q a_q(j)B_q(j).
\tag{2.1}
$$



### 2.1 Carry bounds at the safe support

The positive-power carry argument extends to $0\le q\le145$:


$$
W_jB_q(j)\in p^2\mathbb Z_p.
\tag{2.2}
$$


Indeed, writing $q=pQ+q_0$, here $Q\le5$. If the weight does not borrow at digit $1$, the lower digit in the other binomial is still nonnegative, and the sum of the two digit-$1$ addends is at least


$$
41+\mathbf1_{q_0>0}-\mathbf1_{q_0=28}-j_1-\eta>28.
$$


Digit $3$ is unchanged by these bounded shifts and forces the second factor.

Likewise, for $-118\le q\le0$,


$$
W_jB_q(j)\in p\mathbb Z_p,
\tag{2.3}
$$


from digit $3$. These bounded shifts change neither the relevant digit $28$ of $b-q$ nor digit $15$ of $2n+q-1$.

The stronger unit-boundary bounds remain


$$
W_jB_0(j),\ W_jB_{-1}(j),\ jW_jB_{-2}(j)\in p^3\mathbb Z_p.
\tag{2.4}
$$



All these are factors forced within the four-digit block.

### 2.2 Consequences for the complete kernels

After applying (2.2), the complete positive $P$-kernel is needed only modulo $p^2$. Its graded Newton degree is then at most $57$, and its reconstructed positive Laurent support is at most $58$.

For $Q$, the positive contact kernel is needed modulo $p^3$. Its effective Newton degree is at most $57$, and its reconstructed support is again at most $58$. The complete contact polynomial is divisible by $p$.

The factorial boundary is


$$
-\sum_{s=0}^{117}(-1)^{b+s}c_s
\frac{(1+r)^s}{r^s}(1+j+jr^{-1}),
\qquad
c_s=\sum_{t=s}^{117}F_t\binom{2n}{t-s},
$$


where $F_t=(b+t)!/b!$.

The relevant accounting is:

| Complete contribution | Coefficient valuation | Reconstruction factor | Consequence for $Y\bmod p^5$ |
|---|---:|---:|---|
| $s=0,1$ boundary | possibly $0$ | (2.4), at least $p^3$ | retained |
| $2\le s\le30$ | at least $2$ | at least $p$ | retained through the next digit |
| $31\le s\le59$ | at least $3$ | at least $p$ | retained |
| $60\le s\le88$ | at least $4$ | at least $p$ | vanishes modulo $p^5$ |
| $89\le s\le117$ | at least $5$ | at least $p$ | vanishes modulo $p^5$ |
| positive contact coefficient in $p$ or $p^2$ | $1$ or $2$ | at least $p^2$ | retained |
| positive contact coefficient in $p^3$ | at least $3$ | at least $p^2$ | vanishes modulo $p^5$ |

Terms $F_t$ with $t\ge60$ feeding a *lower* boundary coefficient $c_s$ also have valuation at least four. Thus they vanish after negative-power reconstruction, not merely when $s\ge60$. Their effects in the positive boundary-contact force have still greater valuation.

For the $s=0,1$ boundary, the monomials are exactly combinations of


$$
B_0,\quad B_{-1},\quad jB_{-2}.
$$


For $s\ge2$, each monomial has its displayed coefficient factor and (2.3). Consequently, the $Q$-normalization by $p^3$ is termwise legitimate after this decomposition.

The complete logarithmic force is omitted only through the supplied whole-force estimate


$$
v_p(h_i^F/b!)
\ge F_n-F_b-\lfloor\log_p(2n+b-1)\rfloor\ge6.
\tag{2.5}
$$



No endpoint is removed:


$$
Z_{w,b}=W_b\,b\theta^P_{b-1},\qquad
Y_b=W_b(1+b\theta^Q_{b-1}).
\tag{2.6}
$$



---

## 3. New four-digit polynomial factorization

This is the main new lemma.

### Lemma 3.1 — common high factor through the next digit

For each $0\le x<L$, there are polynomials


$$
P_x(J),Q_x(J)\in(\mathbb Z/p^2\mathbb Z)[J]
$$


of degree at most $4$, with coefficients depending on the actual $n,b$, such that at every actual coordinate $j=LJ+x$,


$$
\boxed{
P_{LJ+x}\equiv(-1)^{j+1}F(J)P_x(J)\pmod{p^2},
}
\tag{3.1}
$$




$$
\boxed{
Q_{LJ+x}\equiv(-1)^{j+1}F(J)Q_x(J)\pmod{p^2}.
}
\tag{3.2}
$$



For $x>b_*$, the polynomial $P_x(J)$ has the factor $h-J$. Therefore the norm and mixed contractions can be extended to $J=h$ at these low indices, with zero added contribution.

The statement includes the newly admitted $P$-support; it is not restricted to the old support $\mathcal X$.

### Proof

#### A. The exact high factorial ratio

Set


$$
v=b_*-x,\qquad c_*=382219,
$$


and define


$$
e=\mathbf1_{x>191112},\qquad
u=\left\lfloor\frac{c_*+v}{L}\right\rfloor,
$$




$$
r=\mathbf1_{v-q<0}.
$$


For every retained $q$, one has


$$
e,u,r\in\{0,1\}.
$$


In particular,


$$
0<382219+q<L,
\qquad -L<v-q<L.
$$



Stripping four factorial levels from $W_jB_q(j)$ leaves the high ratio


$$
\frac{N!}{J!(N-J-e)!}
\frac{(2N+h-J+u)!}{(h-J-r)!(2N)!}.
$$


This is exactly


$$
\boxed{
F(J)(N-J)^e(2N+h-J+1)^u(h-J)^r.
}
\tag{3.3}
$$


The multiplier has degree at most $3$.

If $J=h$ and $r=1$, the original binomial is invalid and equals zero. The factor $h-J$ in (3.3) gives precisely that boundary zero.

If $x>b_*$, every nonnegative $P$-power has $r=1$. Thus its polynomial continuation to $J=h$ is zero.

#### B. The next low factorial unit is affine in $J$

For $t=pm+s$, $0\le s<p$, define the $p$-free factorial


$$
U_p(t)=\prod_{\substack{1\le i\le t\\p\nmid i}}i.
$$


For this odd prime,


$$
U_p(pm+s)
\equiv((p-1)!)^m\,s!\,(1+pmH_s)\pmod{p^2},
\tag{3.4}
$$


where $H_s=\sum_{i=1}^s i^{-1}$.

To verify (3.4), each full block has product


$$
\prod_{i=1}^{p-1}(pt+i)
\equiv(p-1)!\left(1+ptH_{p-1}\right)
\equiv(p-1)!\pmod{p^2}.
$$


The final partial block gives the displayed harmonic correction.

In a binomial factorial ratio, the exponent of $(p-1)!$ after a stripping step is the carry across that step. It depends only on the low digits. At the first three stripping levels, the $J$-part of each quotient in the harmonic correction is divisible by $p$. At the fourth level it is affine in $J$.

Consequently, after removing the fixed low power $p^{c_q(x)}$, the low unit has the form


$$
u_{q,x}^{(0)}+
p\bigl(u_{q,x}^{(1)}+J\,u_{q,x}^{(2)}\bigr)
\pmod{p^2},
\tag{3.5}
$$


with no unidentified higher-index unit.

Combining (3.3) and (3.5) gives a polynomial multiplier of degree at most $4$.

#### C. Kernel coefficients can be frozen at $x$

For $0\le r\le58$,


$$
\binom{x+LJ}{r}-\binom xr\in p^3\mathbb Z_p.
\tag{3.6}
$$


This follows from Vandermonde and


$$
v_p\binom{LJ}{i}\ge4-v_p(i)\ge3
\qquad(1\le i\le58).
$$



Thus:

* the positive $P$-coefficients can be evaluated at $x$ modulo $p^2$;
* the positive $Q$-coefficients can be evaluated at $x$ modulo $p^3$;
* in the boundary, replacing $j$ by $x$ changes the linear coefficient by $LJ$, and (2.3) makes its reconstructed error divisible by $p^5$.

The termwise normalizations established in Section 2 then give integral polynomial multipliers $P_x,Q_x$. Equations (3.1)–(3.2) follow. ∎

### Every actual coordinate boundary

Before extending any sum, the exact block ranges are


$$
\begin{cases}
0\le J\le h,&0\le x\le b_*,\\
0\le J\le h-1,&b_*<x<L.
\end{cases}
\tag{3.7}
$$


The second range is extended only after the factor $h-J$ has been exhibited in $P_x$.

Therefore


$$
D\equiv
\sum_{J=0}^{h}F(J)^2
\sum_{x=0}^{L-1}P_x(J)^2\pmod{p^2},
\tag{3.8}
$$




$$
M\equiv
\sum_{J=0}^{h}F(J)^2
\sum_{x=0}^{L-1}P_x(J)Q_x(J)\pmod{p^2}.
\tag{3.9}
$$



---

## 4. Fixing the leading unit and eliminating the whole next defect

Write


$$
\ell_0(J)=2N+h-J+1,\qquad
\ell_1(J)=N-J.
$$



The established leading-support factorization, interpreted via the stripping proof above, gives polynomial identities modulo $p$:


$$
P_x(J)\equiv
\begin{cases}
C_n c(x)\ell_{e(x)}(J),&x\in\mathcal X,\\
0,&x\notin\mathcal X,
\end{cases}
\tag{4.1}
$$


and, on $\mathcal X$,


$$
Q_x(J)\equiv\xi(x)\ell_{e(x)}(J).
\tag{4.2}
$$



These are identities for the low polynomial multipliers, not divisions by potentially zero values of $F(J)$.

The supplied exact low sums are


$$
\kappa_0=11,\qquad\kappa_1=18,
\qquad g_0=26,\qquad g_1=3.
$$


Since $6^{-1}=5\bmod29$,


$$
g_e=\kappa_e/6.
\tag{4.3}
$$



Thus the leading proportionality is now fixed:


$$
\boxed{M\bmod p=(6C_n)^{-1}(D\bmod p).}
\tag{4.4}
$$



More importantly, put


$$
c=(6C_n)^{-1}\in\mathbb Z_p^\times.
$$


By (4.1)–(4.3), the polynomial


$$
\mathcal H(J)=
\sum_x\left(P_x(J)Q_x(J)-cP_x(J)^2\right)
$$


has every coefficient divisible by $p$. Hence


$$
\mathcal H(J)=pR(J)\pmod{p^2}
\tag{4.5}
$$


for a polynomial $R\in\mathbb F_p[J]$, of degree at most $8$.

Combining (3.8)–(3.9),


$$
\boxed{
M-cD\equiv p\sum_{J=0}^{h}F(J)^2R(J)\pmod{p^2}.
}
\tag{4.6}
$$



The coefficients of $R$ need not be individually evaluated: the following exact finite-boundary identity evaluates their **whole contribution** on the assigned locus.

### Lemma 4.1 — fifth-digit contraction of every residual polynomial

For every $R\in\mathbb F_p[J]$,


$$
\boxed{
\sum_{J=0}^{h}F(J)^2R(J)
=
T\!\!
\sum_{\substack{0\le t\le3\\0\le d-t\le22}}
\binom3t^2B_{d-t}^{\,2}R(t)
\pmod p,
}
\tag{4.7}
$$


where $B_v=\binom{v+6}{6}\bmod p$.

#### Proof

Write $J=pk+t$. A nonzero $F(J)\bmod p$ requires


$$
0\le t\le3,\qquad0\le d-t\le22.
$$


In this range there is neither a borrow in $h-J$ nor a carry in adding its low digit to $6$. Lucas gives


$$
F(pk+t)\equiv\binom3t B_{d-t}X_k\pmod p.
$$


For each retained $t$, the exact range is $0\le k\le H$. All other $t$-terms vanish modulo $p$, including the shorter terminal ranges arising from $t>d$.

Finally, $R(pk+t)=R(t)$ in $\mathbb F_p$. Summing proves (4.7). ∎

On $T=0$, equations (4.6)–(4.7) give the evaluated whole relation


$$
\boxed{M-(6C_n)^{-1}D\equiv0\pmod{p^2}.}
\tag{4.8}
$$



This is not an unevaluated ghost prescription. It proves that **every** next-digit correction, including all new low support, lies in a contraction ideal annihilated by $T=0$.

---

## 5. Combining with the second norm digit

The preceding argument also supplies a direct justification for the reduction underlying turn19’s norm formula. From (4.1),


$$
\sum_xP_x(J)^2
=
C_n^2\bigl(11\ell_0(J)^2+18\ell_1(J)^2\bigr)
+pS(J)\pmod{p^2}
$$


for a polynomial $S$. Lemma 4.1 kills its complete $pS$-contribution on $T=0$. Hence


$$
D_1=
\frac{C_n^2}{p}
\sum_{J=0}^{h}
\bigl(11\ell_0(J)^2+18\ell_1(J)^2\bigr)F(J)^2
\pmod p.
\tag{5.1}
$$



For completeness, the one-step expansion for an admissible $t$, with $v=d-t$, is


$$
F(pk+t)\equiv
\binom3t B_vX_k
\left(1+p(E_t+kr_t)\right)\pmod{p^2},
$$


where


$$
r_t=H_{3-t}-H_t+H_v-H_{v+6}.
$$


The $k$-independent $E_t$-terms multiply $T$ and disappear. Also


$$
\ell_0(pk+t)=v+7+p(2A+H-k),\qquad
\ell_1(pk+t)=3-t+p(A-k).
$$


This gives


$$
D_1=C_n^2\bigl(f(d)T_1+\beta(d)U\bigr),
\tag{5.2}
$$


with


$$
\begin{aligned}
\beta(d)=2
\sum_{\substack{0\le t\le3\\0\le d-t\le22}}
\binom3t^2B_{d-t}^2
\Big[&
\bigl(11(d-t+7)^2+18(3-t)^2\bigr)\\
&\times\bigl(H_{3-t}-H_t+H_{d-t}-H_{d-t+6}\bigr)\\
&-11(d-t+7)-18(3-t)
\Big].
\end{aligned}
\tag{5.3}
$$



Combining (4.8) and (5.2), the full requested evaluation is


$$
\boxed{
M_1=\frac{C_n}{6}\bigl(f(d)T_1+\beta(d)U\bigr)
\pmod{29}
}
\tag{5.4}
$$


for $0\le d\le24,\ T=0$.

Since $C_n$ and $f(d)$ are units there,


$$
\boxed{
D_1=M_1=0
\iff
T_1=-f(d)^{-1}\beta(d)U.
}
\tag{5.5}
$$


If this condition fails, both actual scalar valuations are exactly $1$. If it holds, both are at least $2$; their subsequent difference remains uncontrolled.

---

## 6. Explicit cancellation of the genuine endpoint term

The endpoint is not merely covered abstractly by the polynomial argument. Its entire low-index fibre can be evaluated.

Consider


$$
j=LJ+b_*,\qquad0\le J\le h.
$$


Its terminal member $J=h$ is the actual endpoint $j=b$.

The weight has the fixed low borrows $(1,1,0,1)$. Factorial stripping gives


$$
\frac{W_{LJ+b_*}}{p^3}
\equiv5(N-J)\binom NJ\pmod p.
\tag{6.1}
$$


For example, the low factorial ratio is


$$
-\frac{2!\,7!\,24!\,7!}
{27!\,28!\,5!\,28!\;4!\,7!\,18!\,8!}
=5\pmod{29}.
$$



On this fibre, every positive $q$ introduces an additional final carry. Thus only the $q=0$ leading $P$-coefficient contributes to $Z_w/p^3\bmod p$:


$$
1-h_0(27)=14.
$$



For the complete leading $Q$-boundary,


$$
\mathcal Q_0=(2+r^{-1})(1+j+jr^{-1}),
$$


the $q=0,-1,-2$ coefficients at $j\equiv27$ are


$$
-2,\quad24,\quad-2.
$$


The corresponding low binomial units are $1,-1,1$, so their total is


$$
-2-24-2=1\pmod{29}.
$$


All other factorial and contact contributions have higher valuation on this fibre.

Consequently, including every $J$ in its actual finite range,


$$
\boxed{
\left[\frac Mp\right]_{j=LJ+b_*}
=2C_n(N-J)^2F(J)^2\pmod p.
}
\tag{6.2}
$$


Its whole sum is


$$
2C_n\sum_{J=0}^{h}(N-J)^2F(J)^2
=2C_n\psi_1(d)T
=0
$$


on $T=0$.

The final term $J=h$ is precisely


$$
2C_n(N-h)^2\binom Nh^2
=C_n\eta(d)\binom AH^2,
$$


where


$$
\eta(0)=18,\qquad\eta(1)=14,\qquad\eta(2)=18,
\qquad\eta(d)=0\quad(d\ge3).
$$


Therefore the actual finite interior of this fibre satisfies


$$
\boxed{
2C_n\sum_{J=0}^{h-1}(N-J)^2F(J)^2
=-C_n\eta(d)\binom AH^2
\pmod p
}
\tag{6.3}
$$


on $T=0$.

This exhibits the requested endpoint cancellation explicitly. The endpoint $1+b\theta^Q_{b-1}$ was retained; its contribution cancels against actual interior coordinates, not against an invented extension.

---

## 7. Scope, primitive denominator, and whole real error

I have prioritized the complete main relation. I do **not** give a new evaluation of $M/p^2\bmod p$ for $d=25,\ldots,28$. The bounds stated there in turn19 remain attached to its shifted-support proof; they are not used in the theorem above.

Retain the actual least two-column denominator


$$
N_B=d_B[u,v],\qquad v_{29}(d_B)=0.
$$


With the actual falling metric,


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
p_n=\frac{H_B}{g_B},\qquad q_n=\frac{A_B}{g_B}>0.
$$


The primitive multiplier is $1/g_B$ on the integer coefficient pair, or $d_B^2/g_B$ on the corresponding rational Gram pair. The actual reduced denominator is $q_n$, not a row-clearer.

For


$$
\delta=v_{29}(D),\qquad\mu=v_{29}(M),
$$


the retained exact interface is


$$
v_{29}(g_B)=
\min\{4F_n+4+\delta,\ 2F_n+F_b+5+\mu\},
$$




$$
v_{29}(q_n)=
\max\{0,\ 2F_n-F_b-1+\delta-\mu\}.
$$



Norm nonvanishing follows from positivity. Finiteness of the mixed valuation retains the supplied original-family nonvanishing dependency.

Writing the whole real error as


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


the exact primitive evaluated form remains


$$
q_n(e+\pi)-p_n=-q_n\epsilon_n.
$$


Under the supplied complete signed-error theorem,


$$
\epsilon_n>0\quad\text{eventually},\qquad
\log|\epsilon_n|
=-\left(2+\frac1{2001}\right)n\log(1+\sqrt2)+o(n).
$$


Thus the whole form is eventually negative and nonzero. Its complete exponential residual, logarithmic force, factorial boundary, and endpoint remain included.

There is still no global bound for the actual $q_n$, and no irrationality conclusion.

---

# Concluding ledger

## (1) New result and proof status

**Proved, using the supplied complete bounded-kernel interface and exact leading low constants:**

- A four-digit common-high-factor representation modulo $29^2$ for both actual normalized columns, including new support and all finite boundaries.
- The leading unit is
  

$$
M_0=(6C_n)^{-1}D_0.
$$


- On the original domain $0\le d\le24,\ T=0$, the whole second mixed relation is
  

$$
\boxed{
  M_1=(6C_n)^{-1}D_1
  =\frac{C_n}{6}\bigl(f(d)T_1+\beta(d)U\bigr).
  }
$$


- Hence the second norm-zero condition forces—and is equivalent to—the second mixed zero.
- The genuine endpoint term is explicitly canceled by the finite interior of its own low-index fibre.

The supplied finite computation fixes the leading constants. The second-depth theorem is obtained by the uniform polynomial factorization and exact Lucas contraction, not by finite sampling.

## (2) Exact remaining bottleneck

The next unresolved main quantity is the defect after another common scalar zero:


$$
\frac{M-(6C_n)^{-1}D}{29^2}\pmod{29}.
$$


The present argument annihilates the first residual polynomial by $T=0$; at the next precision its contraction can involve the next residual digit and additional weighted residual moments.

The shifted classes $d=25,\ldots,28$ still require their separate $M/29^2\bmod29$ evaluation. Ultimately, an all-depth relative valuation bound and control of the final primitive denominator across all primes remain necessary.

## (3) Computation request

**None.** No further leading low-constant calculation is needed for the relation proved here.
