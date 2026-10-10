> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## A1 — exact core endpoint law and the precision obstruction to transfer

I reuse the accepted fifth-carry theorem without reopening its proof. The new calculation below gives a closed, inverse-free endpoint-cofactor formula for the exact linear core, with its Jacobi normalization and scalar factors restored. It also gives a precision-sensitive transfer lemma.

**This is a partial resolution of the assignment.** The core formula is exact, but its $3$-adic cancellation has not been evaluated uniformly on the prescribed index domain. Moreover, the available actual-polynomial precision does not determine the first remaining radical digit when $v_3(j)=4$. Consequently I do not identify the actual endpoint ratio or the actual reduced denominator.

### 1. Domain, actual columns, and exact core

Retain throughout


$$
j>0,\qquad81\mid j,\qquad n=4^j+1,\qquad
0<D=H-(n-2)<H/972,
$$


and


$$
H=3^{h-1},\quad A=n-2=H-D,\quad
m=\frac{A+1}{2},\quad k=m+1,
$$




$$
d=\frac{3D}{2}-1,\qquad \nu=\frac D2-1.
$$


The columns are the actual monomials $1,y,\ldots,y^m$. No orthogonal-polynomial basis is asserted to be integral or Smith-equivalent to these columns.

Write


$$
Q_n=\lambda Q_n^{\rm loc},\qquad
\lambda=L_n/3\in\mathbb Z_3^\times,
$$


and, with $\tau=v_3(j)+2$,


$$
Q_n^{\rm loc}=Q_{\rm core}+3^\tau R,\qquad
Q_{\rm core}=(y+1)(y-1)^A(\beta+3y),
$$


where


$$
\beta=-71-A,\qquad r=-\beta/3=(A+71)/3>1.
$$



The complete functional, with $\lambda$ temporarily removed, remains


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+3^h\sum_{v\ge0}
 \frac{[y^v]\bigl(F-F(-1)\bigr)/(y+1)}{2v+1},
\qquad \mathfrak f(y^s)=(2s)!.
$$


Every denominator retains the cutoff $2v+1\le4n-3$.

Define $G_{\rm core}$ to be the **arctangent core matrix only**:


$$
(G_{\rm core})_{ab}
=3^h\int_0^1x^{2a+2b}(x^2-1)^A(\beta+3x^2)\,dx,
\quad 0\le a,b\le m.
$$


Its relation to the complete actual matrix is treated in §4; it is not silently substituted for that matrix.

Set


$$
c=\frac{(-1)^A3^h}{2}.
$$


After $t=x^2$,


$$
(G_{\rm core})_{ab}
=c\int_0^1t^{a+b}t^{-1/2}(1-t)^A\,3(t-r)\,dt.       \tag{1}
$$



Here $A$ is odd, so $c<0$, while $t-r<0$ on $[0,1]$. Thus $G_{\rm core}$ is positive definite over $\mathbb R$.

### 2. Monic Jacobi normalization and nonzero conditions

Let


$$
J_s(t)=P_s^{(A,-1/2)}(2t-1),\qquad
L_s=\frac{(s+A+\tfrac12)_s}{s!},\qquad
p_s(t)=\frac{J_s(t)}{L_s}.
$$


The number $L_s$ is the leading coefficient of $J_s$, so $p_s$ is monic of degree $s$. An entirely explicit rational formula is


$$
p_s(t)=
\frac{(-1)^s(\tfrac12)_s}{(s+A+\tfrac12)_s}
\sum_{\ell=0}^{s}
 \frac{(-s)_\ell(s+A+\tfrac12)_\ell}
      {(\tfrac12)_\ell\,\ell!}\,t^\ell.             \tag{2}
$$


This includes $p_0=1$.

For the unmodified measure $t^{-1/2}(1-t)^A\,dt$, the monic norm is


$$
h_s=
\frac{\Gamma(s+A+1)\Gamma(s+\tfrac12)}
 {(2s+A+\tfrac12)s!\Gamma(s+A+\tfrac12)L_s^2}.       \tag{3}
$$


In particular $h_0=B(\tfrac12,A+1)$, as required.

Every zero of $p_s$ lies in $(0,1)$. Since $r>1$,


$$
p_s(r)>0,\qquad
a_s=\frac{p_{s+1}(r)}{p_s(r)}>0.
$$


Thus none of the Christoffel denominators vanishes.

Put


$$
q_s(t)=\frac{p_{s+1}(t)-a_sp_s(t)}{t-r}.             \tag{4}
$$


This is monic of degree $s$, not degree $s+1$. Its norm for the measure $3(t-r)t^{-1/2}(1-t)^A\,dt$ is


$$
h_s^c=-3a_sh_s.                                    \tag{5}
$$


For example, (5) follows directly by multiplying (4) by $q_s$ and integrating against the base measure: the $p_{s+1}$ term vanishes, while
$\int q_sp_s\,d\mu=h_s$.

### 3. Closed relative endpoint-cofactor law for the core

Let


$$
v=(1,-1,\ldots,(-1)^m)^T.
$$


The determinant and relative endpoint cofactor are


$$
\boxed{\det G_{\rm core}
=c^k(-3)^k p_k(r)\prod_{s=0}^{k-1}h_s,}             \tag{6}
$$




$$
\boxed{
\mathscr K_{\rm core}
:=\frac{v^T\operatorname{adj}(G_{\rm core})v}
        {\det G_{\rm core}}
=\frac1c\sum_{s=0}^{m}\frac{q_s(-1)^2}{-3a_sh_s}.
}                                                               \tag{7}
$$


Indeed, the product of (5) telescopes because
$\prod_{s=0}^{k-1}a_s=p_k(r)$. The scalar $c$ occurs to the $k$-th power in (6), but to the inverse first power in (7).

There is also a closed expression with no kernel sum. Define


$$
F_s(t)=p_{s+1}(t)-a_sp_s(t).
$$


The monic Christoffel–Darboux identity gives


$$
\boxed{
\mathscr K_{\rm core}
=
\left.
\frac{F_{m+1}'(t)F_m(t)-F_m'(t)F_{m+1}(t)}
 {-3c\,a_mh_m(t-r)^2}
\right|_{t=-1}.
}                                                               \tag{8}
$$


The derivatives of the common denominator $t-r$ cancel exactly in this Wronskian. Formula (8) requires base Jacobi polynomials only through degree $m+2$.

All quantities in (6)–(8) are explicit rational numbers using (2)–(3). Moreover,


$$
\det G_{\rm core}>0,\qquad \mathscr K_{\rm core}>0,
$$


so both the core determinant and the core endpoint cofactor are nonzero.

These are **core-only** nonvanishing statements. In particular, $Q_{\rm core}(-1)=0$; replacing the whole construction by this core would erase its period response. The nonzero core kernel is not itself the response coefficient of the actual construction.

#### What is and is not evaluated

Equations (6) and (8) are a closed relative cofactor law, rather than another matrix inverse. The determinant valuation is exactly


$$
v_3(\det G_{\rm core})
=hk+k+v_3(p_k(r))+\sum_{s=0}^{k-1}v_3(h_s).        \tag{9}
$$


The norm valuations in this expression reduce to factorial-product valuations.

However, I have **not** evaluated uniformly the valuation of the Wronskian numerator in (8), or the cancellations in $p_s(r)$. Real positivity proves nonvanishing, not absence of $3$-adic cancellation. Thus (8) does not yet meet the stronger requested all-depth valuation conclusion.

### 4. Complete actual perturbation, including endpoint subtraction

Let


$$
G_{\rm act}
=\bigl(\mathcal M(Q_n^{\rm loc}y^{a+b})\bigr)_{0\le a,b\le m}.
$$


Then exactly


$$
G_{\rm act}=G_{\rm core}+\Delta,
$$


where


$$
\begin{aligned}
\Delta_{ab}={}&
-\frac{3^h}{4}\mathfrak f(Q_n^{\rm loc}y^{a+b})\\
&+3^{h+\tau}
\sum_{v\ge0}
\frac{[y^v]\bigl(Ry^{a+b}-(-1)^{a+b}R(-1)\bigr)/(y+1)}
 {2v+1}.
\end{aligned}                                                    \tag{10}
$$


Thus the factorial term is retained in full, and the second line includes the actual endpoint error.

The supplied cutoff implies


$$
\boxed{\Delta\in3^P M_k(\mathbb Z_3),\qquad
P=\min(h,\tau).}                                                  \tag{11}
$$


Restoring the actual primitive polynomial multiplies both matrices and their difference by $\lambda$. Their endpoint kernels are then multiplied by $\lambda^{-1}$, not left literally unchanged.

### 5. A precision-sensitive transfer lemma

The following bounded lemma identifies the endpoint losses without assuming an integral Jacobi transformation.

Let $G$ be any nonsingular symmetric matrix over $\mathbb Q_3$, $e$ an endpoint vector, and $\Delta\in3^P M_k(\mathbb Z_3)$. Define


$$
L=\max\{0,-\min_{a,b}v_3((G^{-1})_{ab})\},
$$




$$
u=G^{-1}e,\qquad \mu=\min_a v_3(u_a),\qquad
K=e^TG^{-1}e.
$$


If $P>L$, then $G+\Delta$ is nonsingular and


$$
\frac{\det(G+\Delta)}{\det G}\in1+3^{P-L}\mathbb Z_3,               \tag{12}
$$




$$
\boxed{
v_3\!\left(e^T(G+\Delta)^{-1}e-K\right)\ge P+2\mu.
}                                                               \tag{13}
$$



**Proof.** Since $G^{-1}\Delta\in3^{P-L}M_k(\mathbb Z_3)$, its Neumann series converges and proves (12). The exact resolvent expansion gives


$$
e^T(G+\Delta)^{-1}e-K
=-u^T\Delta u+u^T\Delta G^{-1}\Delta u-\cdots.
$$


The first term has valuation at least $P+2\mu$; each further term gains at least $P-L>0$. This proves (13). ∎

In particular, the relative endpoint valuation transfers if


$$
P>L,\qquad P+2\mu>v_3(K).                           \tag{14}
$$


These are sufficient conditions, not claimed necessary conditions.

For application to (10), the missing quantities are the **actual monomial-coordinate** inverse loss $L$, the endpoint-solution depth $\mu$, and the core kernel valuation. Rational Jacobi orthogonalization does not supply these losses without tracking its denominators.

### 6. First unavailable depth in the accepted integral elimination

There is a sharper obstruction already visible in the accepted fifth result.

After the established integral eliminations, the full scaled matrix has $\nu>0$ residual directions divisible by $3^6$: one power comes from the first LOW normalization, followed by the five accepted vanishing LOW digits. The transported endpoint has nonzero residue in those residual coordinates.

On the allowed subdomain


$$
v_3(j)=4,
$$


the supplied polynomial approximation has only $\tau=6$. Hence it determines the full matrix only modulo $3^6$. It does **not** determine


$$
\boxed{\text{the residual full-matrix block divided by }3^6
       \pmod3.}                                                   \tag{15}
$$


Equivalently, in the first-LOW normalization it does not determine the residual block divided by $3^5$ modulo $3$.

This is the first precise unavailable digit for a transfer based solely on the available congruence. It is exactly where an unknown $3^6$ perturbation can affect the residual inverse and its endpoint contraction. Because the transported endpoint is nonzero there, those directions cannot be discarded.

This does not prove that the actual core and actual matrix have different endpoint valuations. It proves that their equality does not follow from the stated precision. Higher-$v_3(j)$ indices provide more digits, but still require comparison with the corresponding inverse and endpoint losses.

### 7. Final gcd, actual denominator, and whole error

No new actual denominator valuation follows from the core formulas.

For the actual complete integer pair retain


$$
g=\gcd(|A_{\rm det}|,|B_{\rm det}|).
$$


On indices where $B_{\rm det}\ne0$,


$$
q=\frac{|B_{\rm det}|}{g},\qquad
p=-\frac{\operatorname{sgn}(B_{\rm det})A_{\rm det}}g,
$$


and


$$
\boxed{
q(e+\pi)-p
=\frac{\operatorname{sgn}(B_{\rm det})\ell^k}{g}
 \det H_{\rm complete}.
}
$$


The primitive multiplier is $\ell^k/g$, with the **final** gcd. The complete determinant includes the exponential term, every rational arctangent contribution, and the actual period response.

Neither core positivity nor (8) proves $B_{\rm det}\ne0$, whole-error nonvanishing, or decay of this primitive error.

## Closing ledger

1. **New result and proof status.** Proved: the exactly normalized core determinant formula (6), the closed endpoint-cofactor law (8), core nonvanishing, the complete perturbation identity (10), and the endpoint-sensitive transfer lemma (12)–(14). The fifth-carry theorem is reused, not reproved. Uniform $3$-adic evaluation of the core Wronskian remains unresolved.

2. **Exact remaining bottleneck.** Evaluate the core Wronskian cancellation and the monomial-coordinate inverse/endpoint losses. Then compare those losses with the actual available precision. At $v_3(j)=4$, the first unavailable residual digit is (15). Actual reduced-denominator control and nonzero whole primitive errors tending to zero remain missing; irrationality of $e+\pi$ is not decided.

3. **Computation request.** None. Small Jacobi checks would verify normalization only, not evaluate the prescribed infinite cancellation or overcome the unavailable actual residual digit.
