> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4, Turn 10 — Independent audit of the actual producer strip, rational-weight cancellation, and high-shift obstruction

## Executive verdict

The principal advance is in A1. Its factorial normalization and signed rank-one argument are valid, and they close the previously outstanding producer-strip obligation **using the accepted order-six producer congruence at its original scope**. Consequently, the previously reviewed core radical now transfers to the actual depth-seven residual.

There is also a stronger consequence available from the same proof:

> **New actual producer-force consequence.** On A1’s original domain, the uncorrected residual-column contribution of $R$ vanishes modulo $27$, not merely at the one coefficient strip modulo $3$. More precisely, $W_R\bmod27$ has an explicit nine-step support pattern, and all the coefficient windows used by the displayed precision-$27$ pole functional avoid that support.

This does **not** evaluate the complete corrected-column force. It removes its uncorrected-column part and leaves a more specific cross-term obligation.

The other audit conclusions are:

1. **A3’s local gcd classification passes**, given the stated complete-producer hypotheses. Its stronger companion divisibility proof has one source-hypothesis detail that must be made explicit: the odd-prime integrality of the coefficients $\alpha_r$ used in the logarithmic/arctangent force. Integrality of the whole $\mathcal W_\ell$ alone is insufficient to justify the termwise estimate. With that coefficient property supplied by the accepted complete producer, the proof is correct.

2. **A3’s fixed-$d$ analytic deductions are no longer provisional.** Turn 9 already reviewed the needed expansion and whole-force remainder. In particular, the logarithmically offset integer-weight family on $d=2,\ 15\mid n$ has eventual nonzero whole error and divergent actual primitive forms.

3. **A5’s corrected high-shift obstruction passes for $\ell\ge5$**. Its executive statement and initial theorem heading still contain the obsolete $\ell\ge4$ assertion and must be corrected. Original-index reachability and the odd Newton multiplier are valid. The target-dependent logarithmic omission, growing factorial cutoff, and finite inverse are valid at their stated integral interfaces. They do not supply the missing complete force coefficients.

4. **The minimum-multiplicity certificate concerns the model only.** Its reported outputs yield an additional model bit at the sixteen stated original indices. They establish neither an actual norm valuation nor an infinite parity theorem.

No proof or disproof of irrationality of $e+\pi$ follows.

No tools were executed. The literature gate is used as supplied; no new search or exhaustive novelty claim is made.

---

# I. A1: the normalized producer theorem passes

## 1. Original domain and retained hypotheses

The producer conclusions below retain exactly


$$
n=4^j+1,\qquad j>0,\qquad81\mid j,
$$




$$
A=n-2=H-D,\qquad H=3^{h-1},\qquad0<D<H/972.
$$



The actual residual boundary is


$$
0\le i,j<\nu,\qquad \nu=D/2-1,
$$


so that


$$
0\le i+j\le D-4.
$$



The accepted producer interface is only


$$
\mathcal E_n:=3P_n-Q_c=3^6R,\qquad R\in\mathbb Z_3[y],
$$


where


$$
Q_c=(y+1)(y-1)^A(\beta+3y),\qquad \beta=-71-A.
$$


Since the leading coefficients agree,


$$
\deg \mathcal E_n,\deg R\le n-1.
$$



No coefficientwise depth-seven congruence is assumed.

Write


$$
x=y-1,\qquad t=v_3(A).
$$


Lifting the exponent gives


$$
t=1+v_3(j)\ge5.
$$


The retained domain also gives $D=2\cdot3^t s$ with $s\ge1$, as in Turn 9. In particular, all the small terminal shifts used below are less than $D$.

---

## 2. Even moments, recurrence, and finite Pascal reduction

The shifted positive moments are correctly identified as


$$
\Lambda_r=\int_0^\infty e^{-z}\bigl(z(z-2)\bigr)^r\,dz
=\sum_{k=0}^r\binom rk(-2)^{r-k}(r+k)!.
$$


Thus $\gamma_r=\Lambda_r/r!$ is integral.

The integration-by-parts recurrence is correct:


$$
\gamma_0=1,\qquad\gamma_1=0,\qquad
\gamma_{r+1}=(4r+2)\gamma_r+4\gamma_{r-1}.
$$


It gives


$$
\gamma_r\equiv
\begin{cases}
1,&r\equiv0,2\pmod3,\\
0,&r\equiv1\pmod3.
\end{cases}
$$



For


$$
\mathsf T_n=\left(\binom{a+b}{a}\gamma_{a+b}\right)_{0\le a,b<n},
$$


Lucas reduction yields exactly the four nonzero residue blocks


$$
(0,0),\ (0,2),\ (2,0),\ (1,1).
$$


There is no omitted block arising from a carry: if the two low digits sum to at least $3$, the binomial coefficient vanishes modulo $3$.

The rectangular Pascal factorization is also valid:


$$
Z_{p,q}=P_p
\begin{pmatrix}I_q\\0\end{pmatrix}P_q^T
\quad(p\ge q),
\qquad
(P_p)_{ij}=\binom ij.
$$


It follows from the finite Vandermonde identity, with precisely the finite index ranges stated.

Here


$$
m_0=m_2\quad\text{or}\quad m_0=m_2+1.
$$


The resulting $0,2$ block consists of $m_2$ invertible blocks


$$
\begin{pmatrix}1&1\\1&0\end{pmatrix}
$$


and possibly one additional entry $1$. The residue-$1$ block is $2I_{m_1}$.

Therefore


$$
\boxed{\mathsf T_n\in\operatorname{GL}_n(\mathbb Z_3)}
$$


for every finite $n\ge1$, with


$$
\det\mathsf T_n\equiv(-1)^{m_1+m_2}\pmod3.
$$



**Audit status:** pass. This is a theorem for the actual shifted even-subsequence moments, not an import from an unstepped derangement Hankel formula.

---

## 3. Signed rank-one denominator and nonvanishing

Let


$$
F=(n-1)!,\qquad
u_a=\frac{F(-2)^a}{a!},\qquad
\mathsf J=\operatorname{diag}(a!).
$$


The signed matrix in the shifted basis is exactly


$$
\Gamma_n=\mathsf J
\left(\mathsf T_n-\frac{uu^T}{F^2}\right)\mathsf J.
$$


The triangular basis change has determinant $1$, so


$$
\det\Gamma_n=\det C_n.
$$



With


$$
\eta_n=F^2-u^T\mathsf T_n^{-1}u,
$$


the determinant and inverse formulas are correct:


$$
\det C_n
=\left(\prod_{a=0}^{n-1}(a!)^2\right)
\det\mathsf T_n\,\frac{\eta_n}{F^2},
$$




$$
\Gamma_n^{-1}
=\mathsf J^{-1}
\left(
\mathsf T_n^{-1}
+\frac{\mathsf T_n^{-1}uu^T\mathsf T_n^{-1}}{\eta_n}
\right)\mathsf J^{-1}.
$$



In particular, the valuation formula retains the full signed denominator:


$$
v_3(\det C_n)
=
2\sum_{a=0}^{n-1}v_3(a!)
-2v_3(F)+v_3(\eta_n).
$$



The real nonvanishing argument is valid. The positive Gram space contains $1,x$, with Gram matrix $\operatorname{diag}(1,8)$. Evaluation at $x=-2$ has squared norm at least $3/2$, hence


$$
\eta_n\le-\frac{F^2}{2}<0\qquad(n\ge2).
$$



This proves $\eta_n\ne0$; it does **not** prove that $\eta_n$ is a $3$-adic unit.

**Audit status:** pass, including the distinction between real nonvanishing and $3$-adic inverse loss.

---

## 4. Complete force and the scalar-integrality argument

In the shifted variable,


$$
Q_c=3x^n+(b+6)x^{n-1}+2b x^{n-2},
\qquad b=-68-A.
$$


Since $Q_c(-1)=0$, its entire signed force is its positive force:


$$
H_a=3\Lambda_{n+a}+(b+6)\Lambda_{n-1+a}+2b\Lambda_{n-2+a}.
$$



The normalized expression


$$
\tau_a=\frac{H_a}{a!F}
$$


is exactly


$$
\begin{aligned}
\tau_a={}&3n\binom{n+a}{a}\gamma_{n+a}\\
&+(b+6)\binom{n-1+a}{a}\gamma_{n-1+a}\\
&+\frac{2b}{n-1}\binom{n-2+a}{a}\gamma_{n-2+a}.
\end{aligned}
$$


Because $n\equiv2\pmod3$, $n-1$ is a unit. Thus $\tau\in\mathbb Z_3^n$.

Define


$$
\mathbf t=\mathsf T_n^{-1}\tau,\qquad
\mathbf v=\mathsf T_n^{-1}u,\qquad
\xi_n=\frac{u^T\mathbf t}{\eta_n}.
$$


The exact solution is


$$
e_a=-\frac{F}{a!}(t_a+\xi_n v_a),
\qquad
\mathcal E_n(-1)=-F^2\xi_n.
$$



The terminal pivot is correctly computed. For $n=3N+2$,


$$
u_a\equiv0\pmod3\quad(a\le n-3),\qquad
u_{n-2}\equiv u_{n-1}\equiv1\pmod3.
$$


The terminal residue-$1$ block is $2Z_{N+1}$, and


$$
(Z_{N+1}^{-1})_{N,N}=1.
$$


Consequently


$$
v_{n-1}\equiv2\pmod3.
$$



At $a=n-1$, the factorial multiplier is $1$. Since the accepted order-six interface makes $e_{n-1}$ integral,


$$
\xi_n=-\frac{e_{n-1}+t_{n-1}}{v_{n-1}}\in\mathbb Z_3.
$$



This is the decisive division-safe step. It proves divisibility of the **actual numerator** relative to $\eta_n$, rather than discarding $\eta_n$.

Therefore


$$
\boxed{
v_3(e_a)\ge v_3\!\left(\frac{(n-1)!}{a!}\right)
}
$$


and


$$
\boxed{
v_3(\mathcal E_n(-1))\ge2v_3((n-1)!).
}
$$



The producer endpoint nonvanishing proof also passes:


$$
P_n(-1)=0
\Longrightarrow P_n=(y+1)S
\Longrightarrow
0=\rho(P_nS)=\mu((y+1)S^2)>0.
$$



This does not establish nonvanishing of the later complete determinant coefficient.

---

## 5. Terminal localization, strip vanishing, and the actual radical

The terminal products used for depth $7$ have the claimed valuations. After division by $3^6$,


$$
\overline R=(y+1)(y-1)^{A-\kappa}B(y-1),
\qquad \deg B\le\kappa,
$$


with


$$
\kappa=
\begin{cases}
6,&t=5,\\
3,&t=6,\\
0,&t\ge7.
\end{cases}
$$



The endpoint subtraction is legitimate because $R(-1)\equiv0\pmod3$. Thus


$$
\overline W_R=(y^H-1)T_D(y),\qquad\deg T_D\le D.
$$


It follows that


$$
[y^r]W_R\equiv0\pmod3\qquad(D<r<H).
$$



The actual required range is


$$
r_1-(D-4)\le r\le r_1,\qquad r_1=(H-1)/2.
$$


Its lower endpoint exceeds $D$, since $H+7>4D$. Hence


$$
\boxed{\mathcal F_R=0}
$$


on the entire original domain.

The accepted residual transfer therefore becomes


$$
\boxed{\mathscr R_{\rm act}/3^7\equiv\mathcal C_7\pmod3.}
$$



The Turn 9 core results now transfer without further matrix enlargement:

- the actual depth-seven digit is singular;
- its radical and image are the reviewed finite-boundary radical and image;
- it vanishes entirely exactly when
  

$$
D<H/2916;
$$


- the transported endpoint lies outside its image when
  

$$
D<H/2187.
$$



These are depth-seven statements, not evaluations of the next Schur operator or the full endpoint inverse contraction.

---

## 6. The ten-coefficient jet passes

Let $\ell_9$ be the least terminal length whose factorial product has valuation at least $9$. The table is correct:


$$
\begin{array}{c|c|c}
t&\ell_9&\deg B_3\le\\ \hline
5&11&9\\
6&11&9\\
7&8&6\\
8&5&3\\
\ge9&2&0.
\end{array}
$$



For $t=6$, the length-$11$ product has valuation $10$, but the preceding products have valuation at most $8$; hence length $11$ is indeed minimal for reaching $9$.

One obtains


$$
\boxed{
R(y)\equiv
(y+1)(y-1)^{n-\ell_9}B_3(y-1)\pmod{27},
\qquad\deg B_3\le\ell_9-2.
}
$$



Thus the jet has at most ten coefficients. Those are coefficients of the **actual** producer correction, but they have not been evaluated uniformly. A ten-coefficient output does not imply a uniformly bounded computation of the underlying finite matrix solution.

---

# II. New consequence: precision-$27$ support localization of the actual producer force

## 7. A nine-step support theorem

The preceding jet yields more than the modulo-$3$ strip theorem.

### Theorem

On A1’s original domain, there exists


$$
T_D\in(\mathbb Z/27\mathbb Z)[y],\qquad\deg T_D\le D,
$$


such that


$$
\boxed{
W_R(y)\equiv
\bigl(y^{H/9}-1\bigr)^9T_D(y)\pmod{27}.
}
\tag{7.1}
$$



Consequently, a coefficient of $W_R\bmod27$ can be nonzero only in


$$
\boxed{
\bigcup_{m=0}^{9}
\left[mH/9,\ mH/9+D\right].
}
\tag{7.2}
$$



### Proof

Put $\ell=\ell_9$. The endpoint bound gives $R(-1)\equiv0\pmod{27}$, so the jet implies


$$
W_R\equiv
(y-1)^{n-\ell+2D}B_3(y-1)
=(y-1)^H T_D(y)\pmod{27},
$$


where


$$
T_D(y)=(y-1)^{D+2-\ell}B_3(y-1).
$$


The exponent is nonnegative because $D$ is much larger than $\ell\le11$, and


$$
\deg T_D\le D+2-\ell+\ell-2=D.
$$



Since $H/9$ is a power of $3$,


$$
(y-1)^{H/9}=y^{H/9}-1+3U(y)
$$


for an integer polynomial $U$. Raising to the ninth power gives


$$
(A+3U)^9\equiv A^9\pmod{27}.
$$


Indeed, the linear correction has factor $9\cdot3=27$, the quadratic correction has factor $\binom92 3^2$, and all higher corrections are also divisible by $27$.

Thus


$$
(y-1)^H\equiv(y^{H/9}-1)^9\pmod{27}.
$$


Multiplication by $T_D$ proves (7.1), and its degree proves (7.2). ∎

This is a theorem about the actual $R$, using the accepted order-six interface. It is not a model replacement.

---

## 8. All displayed pole windows miss this support

For odd $c$, define


$$
r_c=\frac{cH/3-1}{2}.
$$


The precision-$27$ functional uses:

- $c=9$ for the top pole;
- $c=3$ for $r_1$;
- $c\in\{1,5,7,11\}$ for the following layer.

For $0\le s\le D-4$,


$$
r_c-s=\frac{cH}{6}-\frac12-s.
$$


Because $c$ is odd, $cH/6$ lies halfway between two successive multiples of $H/9$. Its distance from either is $H/18$.

The lower distance after subtracting $1/2+s$ is at least


$$
H/18-D+7/2>D,
$$


using $D<H/972$. The point also remains below the next multiple of $H/9$. Therefore it lies in none of the support intervals (7.2).

Hence


$$
\boxed{
[y^{r_c-s}]W_R\equiv0\pmod{27}
}
\tag{8.1}
$$


for all the displayed pole values and every actual $s=i+j$.

Let the uncorrected residual columns be


$$
z_i^0=(y-1)^D y^i,\qquad0\le i<\nu.
$$


Since $R(-1)\equiv0\pmod{27}$,


$$
\frac{Rz_i^0z_j^0-(Rz_i^0z_j^0)(-1)}{y+1}
\equiv y^{i+j}W_R\pmod{27}.
$$


Using the accepted precision-$27$ evaluation of the **complete** functional—including the already established valuation omission of its factorial term—gives


$$
\boxed{
\mathcal M(Rz_i^0z_j^0)\equiv0\pmod{27},
\qquad0\le i,j<\nu.
}
\tag{8.2}
$$



The finite degree and pole cutoff remain the original ones. No out-of-range pole is introduced.

### Material consequence for the remaining force

Write, exactly,


$$
\widehat z_i^{\,c}=z_i^0+\delta_i.
$$


Then


$$
\boxed{
(\Phi_R)_{ij}\equiv
\mathcal M\!\left(
R(z_i^0\delta_j+\delta_i z_j^0+\delta_i\delta_j)
\right)\pmod{27}.
}
\tag{8.3}
$$



Thus the next producer-force bottleneck is no longer the full uncorrected contribution. It is the interaction of the actual terminal jet with the corrected-column terms.

No extra divisibility of $\delta_i$ is assumed here. In particular, (8.3) does **not** imply $\Phi_R=0$.

The next Schur calculation must still retain


$$
G_c(Z,Z)-9V\widehat E^{-1}V^T
+3^8\mathcal K_{\rm LOW}+3^6\Phi_R
\pmod{3^9},
$$


with whole-numerator summation before division on a vanishing depth-seven branch.

---

# III. A3: companion divisibility, full gcd branches, and actual-height consequences

## 9. Companion divisibility: correct argument with an explicit coefficient hypothesis

For


$$
p>d\ge2,\qquad p\mid n,\qquad s=v_p(n),
$$


the combinatorial argument


$$
q_jK^{\underline j}\in n\mathbb Z[1/2]\qquad(j\ge1)
$$


is correct. It retains every coefficient of $Q(z)^n$, not only the first few. Consequently,


$$
\mathcal B_K\equiv1\pmod{p^s}
$$


and


$$
w_i\equiv\mathcal W_{2n+i}\pmod{p^s}.
$$



The factorial estimate


$$
v_p(\ell!)-\lfloor\log_p\ell\rfloor\ge s
\qquad(\ell\ge2n)
$$


is also correct. The function is nondecreasing: at a power $p^r$, the factorial valuation rises by $r$, while the floor logarithm rises by only $1$.

There is, however, one hypothesis that should be written explicitly:



$$
\boxed{\alpha_r\in\mathbb Z_p\quad\text{for every odd prime }p.}
\tag{9.1}
$$



Under (9.1), each logarithmic/arctangent summand has valuation at least $s$. The displayed assertion $\mathcal W_\ell\in\mathbb Z[1/2]$, by itself, does not establish (9.1) or the separate divisibility of that part.

Thus:

- if dyadic integrality of the actual $\alpha_r$ is part of the accepted complete producer, A3’s proof passes;
- if it is not in the retained interface, its actual defining formula or recurrence must be attached before labeling this step self-contained.

The remaining proof is valid:


$$
\mathcal W_{2n+i}\equiv\sum_{t=0}^{i}i^{\underline t}\pmod{p^s},
$$




$$
C_{ij}\equiv i^{\underline j}\pmod{p^s}.
$$


The triangular diagonal $i!$ is a unit because $i\le d<p$, so


$$
y_j\equiv1\pmod{p^s}.
$$


Finally, retaining the exterior $+1$,


$$
v_0=1-\sum_{j=0}^d(-1)^j n^{\overline j}y_j
\equiv0\pmod{p^s}.
$$



The result is a lower bound:


$$
v_p(v_0)\ge v_p(n),
$$


not an exact valuation.

---

## 10. Every local gcd branch passes

Retain the additional unit condition


$$
\tau_nD_d\not\equiv0\pmod p.
$$


With


$$
m=2v_p(n!),\quad w=v_p(v_0),\quad
\kappa=v_p(k),\quad r=v_p(a-k),
$$


the stated endpoint valuations imply


$$
v_p(\mathcal W)=w,\qquad
v_p(\mathcal V)=v_p(J)=0.
$$



The complete numerator is


$$
T=(a-k)J+k\mathcal W.
$$


This immediately verifies all branches:

- **$p\mid k$:**
  

$$
v_p(T)=0,\qquad v_p(q_\lambda)=m+\kappa.
$$



- **$p\nmid k,\ r\ne w$:**
  

$$
v_p(T)=\min(r,w),\qquad
  v_p(q_\lambda)=\max(0,m-\min(r,w)).
$$



- **$a=k=1$:**
  

$$
v_p(q_1)=\max(0,m-w).
$$



- **Resonance $r=w<\infty$:**
  

$$
v_p(T)=w+\chi,\qquad
  v_p(q_\lambda)=\max(0,m-w-\chi).
$$



The final shared gcd is precisely


$$
v_p(H_{\rm gcd})=
\begin{cases}
\min(m-w,\chi),&p\nmid k,\ r=w<m,\\
0,&\text{otherwise}.
\end{cases}
$$


Equality $r=w$ is necessary but not sufficient for an extra shared gcd: the leading units must cancel.

The full global normalization remains


$$
F=\gcd(|A|,|a|)\gcd(|B|,|a-k|),\qquad
G=\gcd(k,|J|),
$$




$$
H_{\rm gcd}=\gcd\!\left(h,\frac{|T|}{FG}\right),
$$




$$
q_\lambda=\frac{kh|AB|}{FGH_{\rm gcd}},\qquad
p_\lambda=\operatorname{sgn}(AB)\frac{T}{FGH_{\rm gcd}}.
$$



There is no second raw-minor factor available: its local content has already been consumed by row contents and $h$.

---

## 11. Actual-height sparsity has the claimed, limited scope

For $a\ne k$, ordinary cancellation over the selected eligible primes divides the single integer $a-k$. Therefore


$$
q_\lambda\ge
\frac{Q_{\mathcal P}(n)}
{2\mathcal H\,\mathcal R_{\mathcal P}(a,k)}.
$$


There is no unjustified multiplication of one height loss for each prime.

The rational-reconstruction uniqueness argument is already accepted and need not be reproved. Its application here is legitimate because the actual residue is


$$
\Theta_{n,d}=-\mathcal VJ^{-1},
$$


and $J$ is a unit at every selected prime.

The polynomial sparsity bound follows by counting the possible exponent vectors:


$$
\prod_{p\in\mathcal P}(2v_p(n!)+1)
=O_{\mathcal P}(n^{|\mathcal P|}).
$$



The essential restrictions are:

- $\mathcal P$ is fixed and finite;
- a height bound $\mathcal H_n$ is specified with $\log\mathcal H_n=o(n)$;
- the modulus is exponentially large;
- the conclusion is “at most polynomially many exceptional weights,” not “none.”

The unresolved object is the existence and identity of these short reconstructions of the **moving actual residue**.

---

## 12. The logarithmically offset divergence is now a theorem at fixed $d$

Turn 9 already reviewed


$$
\Lambda_{n,d}
=\frac{n^2}{d}+\frac{(2d-3-3\sqrt2)n}{d}+O_d(1)
$$


and the complete fixed-$d$ endpoint error law. These results should no longer be called provisional in A3 Turn 4.

For


$$
d=2,\qquad15\mid n,
$$


let


$$
L_n=\lfloor\log_2 n\rfloor,
$$




$$
a_n=
15\left\lceil\frac{n^2+(1-3\sqrt2)n}{30}\right\rceil+15L_n,
\qquad k_n=1.
$$


The rounding error is bounded, so


$$
a_n-\Lambda_{n,2}=15L_n+O(1)>0
$$


eventually.

The exact whole-error identity then gives


$$
c_{a_n}-(e+\pi)
=
(-1)^n120\pi\frac{L_n}{n^2}
M^{-2n-3}
\left(1+O(L_n^{-1})+O(n^{-1})\right).
$$


This includes the complete factorial and endpoint forces through the reviewed whole-error expansion.

Because $15\mid a_n$, both $a_n-1$ and $k_n$ are units at $3,5$. The eligible-prime theorem therefore survives the full gcd:


$$
v_3(q_{a_n})=2v_3(n!),\qquad
v_5(q_{a_n})=2v_5(n!).
$$


Hence


$$
\boxed{
|q_{a_n}(e+\pi)-p_{a_n}|
\ge c\,\frac{L_n}{n^6}(11/10)^n\longrightarrow\infty.
}
$$



This excludes this particular polynomial-height, analytically improved family as an irrationality construction. It does not exclude resonant or exceptionally close threshold weights.

---

# IV. A5: corrected obstruction and precision framework

## 13. The valid threshold is $\ell\ge5$, not $\ell\ge4$

Retain exactly


$$
b=9^{18+32u},\quad n=4002b,\quad
D=(b-81)/128,
$$




$$
C=4002D+2532,\qquad k=2C+1.
$$



For $s=380,\ j=0$, factorial stripping gives


$$
\frac{\mathcal M_{380}(0)}{\mathcal B_0}
=u_*
\frac{(k+D)D(D-1)(D-2)}
{k(k+1)(k+2)(k+3)},
\qquad u_*\in\mathbb Z_2^\times.
$$



If $\ell=v_2(k+3)\ge5$, the valuation tuple is


$$
(1,0,2,0;\ 0,1,0,\ell),
$$


and therefore


$$
\boxed{
v_2(\mathcal M_{380}(0)/\mathcal B_0)=2-\ell.
}
$$



At $\ell=4$, $v_2(D-1)$ need not equal $2$, so the obsolete statement in the executive summary and initial theorem heading is false as written. The report’s later corrected statement is the valid one.

The multiplier proof passes:


$$
2n=-380+128(k+3).
$$


For $\ell\ge5$, the perturbation has valuation at least $12$, greater than every valuation among $1,\ldots,380$. Thus


$$
\binom{2n+379}{380}\equiv1\pmod2.
$$



---

## 14. Reachability is genuinely on the original exponential family

The identity


$$
v_2(D_u-D_v)=1+v_2(u-v)
$$


follows correctly from LTE. Since $D_0$ is odd, the first $2^{q-1}$ values exhaust all odd residues modulo $2^q$.

The congruence


$$
2001D+1267\equiv0\pmod{2^m}
$$


has one odd solution modulo $2^m$. Choosing the next digit to avoid divisibility by $2^{m+1}$ produces exact valuation $m$, and hence arbitrarily large exact $\ell=m+2$.

Therefore the fixed restored moment, including its mandatory multiplier, has unbounded loss relative to the old common kernel on actual original indices.

This disproves a uniform shift-only loss bound. It does not disprove the complete residual estimate, because the actual $p_{380}$ and possible grouped cancellations remain unevaluated.

---

## 15. Logarithmic omission, factorial cutoff, and finite inverse

The bound


$$
\mu\le\operatorname{bitlength}(2C+D)
$$


is valid by taking $t=0$ and using the carry count.

At


$$
T=2\mu+4,\qquad p=T+3,
$$


the accepted whole logarithmic-force estimate exceeds $p$ throughout the original domain. Its use is division-safe because omission occurs before common-kernel normalization, through the retained integral raw-column operators.

The three-bit margin is sufficient for the displayed scalar interfaces:

- division by $4$ in the norm loses two bits;
- division by $8$ in the mixed contraction loses three.

The factorial cutoff is also correct:


$$
v_2\!\left(\frac{(b+2p)!}{b!}\right)\ge p
$$


because $b$ is odd and exactly $p$ of the $2p$ factors are even. Thus $a<2p$ is a safe raw cutoff.

Finally, the contact correction is even, so on the original finite range $0\le i,j<b$,


$$
(I+K_{n,b})^{-1}\equiv
\sum_{r=0}^{p-1}(-K_{n,b})^r\pmod{2^p}.
$$


The contact-symbol truncation $s\le4(p-1)$ is valid in the stated integral divided-power algebra.

**Scope:** these are valid preparation and truncation theorems. They do not define the missing higher central-force coefficients by lifting a modulo-$256$ receipt.

Force-weighted term contents are likewise legitimate lower-bound normalizations, but they need not equal coordinate contents; sums may acquire additional divisibility.

The complete contraction boundaries remain


$$
0\le t<D,\ 0\le\rho<128;
\qquad t=D,\ 0\le\rho\le80;
\qquad j=b
$$


with the exterior $+1$ retained.

---

# V. The supplied minimum-multiplicity certificate

## 16. What the certificate establishes—and what it does not

The certificate reports, for $u=0,\ldots,15$:

- the previously stated $\mu_u$;
- even minimum multiplicity;
- $\xi_u\equiv u\pmod2$;
- zero normalized model next bit.

Combined with the accepted exact model pairing theorem, its reported outputs imply


$$
\boxed{
v_2(S(C_u,D_u))\ge2\mu_u+3
\qquad(0\le u\le15).
}
$$



For example, the lower bounds at $u=0,1,2,3$ are respectively


$$
17,\ 37,\ 55,\ 67.
$$


They are lower bounds, not exact valuations.

The auxiliary direct checks concern the stated odd $D\le63$, not original exponential indices.

The JSON is a result summary rather than a displayed carry-transition proof or complete path-count trace. I have not independently recomputed its large-index multiplicities. Its parity products and scope labels are internally consistent, and its mathematical implications are as above.

It supplies no proof that minimum multiplicity is even for every original $u$. Nor does it improve


$$
N=2S+256R_u,\qquad R_u\in\mathbb Z_2
$$


to arbitrary precision.

Thus the actual conclusions at these certified indices remain only the accepted fixed-precision ones,


$$
N\in256\mathbb Z_2,\qquad H\in128\mathbb Z_2,
$$


not a valuation near $2\mu_u$.

---

# VI. Primitive normalization and whole evaluated errors

## 17. No local result replaces the full gcd

### A1

Retain


$$
A_\ell=\ell^k\beta_0,\qquad B_\ell=\ell^k\beta_1,\qquad
g_\ell=\gcd(|A_\ell|,|B_\ell|).
$$


When $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
$$


and


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell^k}{g_\ell}
\det H_{\rm complete}.
}
$$



The now-established actual depth-seven radical does not determine $B_\ell\ne0$, the all-prime gcd, or this whole error.

### A3

The primitive denominator is the full


$$
q_\lambda=\frac{kh|AB|}{FGH_{\rm gcd}},
$$


and the exact whole form is


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=q_\lambda e_b\alpha_{n,d}(\lambda-\Lambda_{n,d}).
}
$$


A denominator lower bound produces divergence only when paired with a whole-error lower bound. The logarithmically offset family supplies both; a general moderate-height weight does not.

### A5

Retain


$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B,
$$


including every odd prime. The whole error remains


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n.
}
$$


Neither the shift obstruction nor the model certificate evaluates the full primitive denominator.

---

# VII. Concrete follow-on obligation and bounded exact arithmetic

## 18. Sharpened follow-on lemma for A1

The new support theorem reduces the immediate local task to:

> **Corrected-column terminal-jet lemma.** Evaluate, uniformly on the original domain,
> 

$$
> \mathcal M\!\left(
> R(z_i^0\delta_j+\delta_i z_j^0+\delta_i\delta_j)
> \right)\pmod{27},
>
$$


> using the actual $B_3$, the actual finite corrected columns, every pole, the LOW cross term, and the transported endpoint. Then form the next actual Schur operator on $\ker\mathcal C_7$, summing the complete numerator before division.

This is narrower than evaluating the original arbitrary-degree $R$-force: the bare term has now been proved zero modulo $27$.

For A3, the unresolved arithmetic task remains the identity of short reconstructions of $\Theta_{n,d}$, not uniqueness. The coefficient property (9.1) should be attached explicitly to the companion-divisibility proof.

For A5, the missing full force remains separately necessary. In particular, one must determine coefficient compensation or grouped cancellation for


$$
v_2(p_{380})+v_2(\mathcal B_0)+2-v_2(k+3).
$$


The finite inverse alone does not answer that question.

---

## 19. A bounded calculation worth inspecting

No computation is required for the proof of the new support theorem. A small exact polynomial certificate can independently check its arithmetic mechanism.

### Inputs

Use the auxiliary pairs


$$
(H,D)=(27,1),\qquad(81,2).
$$


For each $0\le r\le D$, set $T(y)=y^r$.

### Expected verifiable output

Verify coefficientwise modulo $27$:


$$
(y-1)^H T(y)
\equiv
(y^{H/9}-1)^9T(y).
$$


Return:

1. zero coefficient vector for the difference modulo $27$;
2. support contained in
   

$$
\bigcup_{m=0}^{9}[mH/9,mH/9+D];
$$


3. the nine-step multiplier coefficients
   

$$
(-1)^{9-m}\binom9m\pmod{27}.
$$



These are auxiliary checks of the polynomial identity, not original-domain producer evaluations.

The existing proposed small-$n$ A1 calculation remains useful for checking the exact signed coefficient formula and terminal pivot. It must not assume the original-domain order-six congruence at those auxiliary indices.

For A3, a symbolic check of the actual defining formula or recurrence for $\alpha_r$, proving $\alpha_r\in\mathbb Z[1/2]$, is preferable to a finite coefficient sample: the divisibility theorem needs the property through a growing force endpoint.

---

## Final proof ledger

| Claim | Audit conclusion |
|---|---|
| A1 normalized even-moment unit theorem | Proved |
| A1 finite Pascal transformations and boundaries | Correct |
| A1 exact signed denominator and inverse loss | Correctly retained |
| A1 terminal pivot and actual scalar integrality | Proved using accepted producer integrality |
| A1 factorial localization and actual strip | Proved on the full original domain |
| Transfer of reviewed core radical to actual depth seven | Established |
| A1 ten-coefficient $R\bmod27$ jet | Proved; coefficients not uniformly evaluated |
| **New precision-$27$ support and bare-force vanishing** | **Proved** |
| Complete next corrected-column force | Still unevaluated |
| A3 companion divisibility | Correct with explicit odd-prime integrality of actual $\alpha_r$ |
| A3 all gcd branches and resonance | Correct |
| A3 actual-height sparsity | Correct at fixed finite prime set and specified height bound |
| A3 log-offset whole-form divergence | Established using Turn 9’s reviewed analytic result |
| A5 high-shift obstruction | Correct for $\ell\ge5$, not uniformly for $\ell=4$ |
| A5 original reachability and odd multiplier | Proved |
| A5 growing-target omissions and finite inverse | Valid framework, not an evaluated full force |
| Minimum-multiplicity certificate | Finite model information only |

### Exact remaining bottleneck

The strongest newly resolved obligation is A1’s actual producer-strip transfer. The next local obstruction is the **complete corrected-column Schur operator on the actual depth-seven radical**, now with its bare $R$-force removed modulo $27$.

The other outstanding obstructions remain actual moving-residue reconstruction in A3 and complete force–shift compensation in A5.

Globally, none of these reports yet supplies a same-index infinite family with its actual full primitive denominator and whole nonzero error satisfying


$$
0<|q(e+\pi)-p|\longrightarrow0.
$$





$$
\boxed{\text{An unconditional proof or disproof of irrationality of }e+\pi
\text{ remains unresolved.}}
$$


