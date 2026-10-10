> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, Turn 8 — Complete growing-precision force restoration and a coefficient-sensitive reduction at $k=-3$

## Executive summary

The newly attached central formulas remove the specific input deficiency identified in Turn 7. They permit a complete, uniform, growing-precision construction of the **actual signed first-force polynomial and its finite contact inverse**. The higher coefficients must be computed from those formulas, not by lifting the modulus-$256$ vector.

The principal result of this report is an explicit coefficient-sensitive reduction:

> For each precision $p$, a finite rational-polynomial calculation produces a polynomial $\Pi_p(k)$ whose value is the actual signed Newton coefficient $p_{380}$ modulo $2^p$, uniformly on every original index. The calculation retains all contact orders that can survive modulo $2^p$ and the actual upper endpoint $b$. Moreover, the residue
> 

$$
> \Pi_p(-3)\pmod{2^p}
>
$$


> is well defined, and these residues are compatible as $p$ grows. Thus they characterize the actual coefficient limit as $k+3\to0$ along the original family.

This is a characterization by bounded exact arithmetic, not an evaluated value. In particular, I do **not** assert that the limit is zero.

The reduction gives a sharp, testable obstruction:

* If $\Pi_p(-3)\not\equiv0\pmod{2^p}$ for even one precision, then the coefficient has a finite limiting valuation. Consequently, **termwise compensation fails** at $s=380,j=0$ on sufficiently deep reachable branches.
* If every residue vanishes, that establishes a zero limit, but **does not by itself establish the linear valuation gain** needed for termwise compensation. A quantitative local divisibility theorem is still required.
* Failure of termwise compensation would not disprove the norm residual theorem: complete grouped cancellation could still occur before common-kernel division.

I also restore the growing factorial/exterior data and the complete finite contact insertion needed for the second column, explaining precisely where the whole logarithmic-force estimate permits omission at the target precision.

**Not obtained:** an evaluation of the complete residual


$$
N-2S(C,D)\pmod{2^{2\mu+4}},
$$


a proof or disproof of its proposed divisibility, or an unconditional resolution of irrationality of $e+\pi$. The coefficient calculation below is a genuine finite reduction of the moving-force issue, but is not a substitute for evaluating that residual.

No tools or supplied code have been executed.

---

## 1. Domain, accepted results, and conventions

The original domain remains


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0,
$$


with


$$
b=128D+81,\quad n=128C+66,\quad C=4002D+2532,
$$




$$
k=2C+1=8004D+5065.
$$


Useful exact relations are


$$
n=64k+2,\qquad h=\frac n2=32k+1,\qquad
b=\frac{32k+1}{2001}.
\tag{1.1}
$$



Every actual contact matrix has indices


$$
0\le i,j<b.
$$


Scalar coordinates have indices $0\le j\le b$, with the exact partition


$$
0\le t<D,\quad 0\le\rho<128,
$$




$$
t=D,\quad 0\le\rho\le80,
$$


and the separate exterior coordinate $j=b=128D+81$.

Retain


$$
X=\frac{Z_w}{2R},\qquad Y=\frac{V_w}{4b!},\qquad
N=X^TX>0,\qquad H=X^TY\ne0.
$$



I reuse the following established results at their stated scopes:

1. The complete finite-precision interfaces, including
   

$$
H-N\in128\mathbb Z_2,\qquad N-2S(C,D)\in256\mathbb Z_2.
$$


2. The exact model theorem for $S$, including its shortened terminal coefficient.
3. The arbitrary-monomial contact transport and its integral Newton-polynomial action.
4. The whole logarithmic-force estimate.
5. The **corrected** singularity theorem:
   

$$
\ell=v_2(k+3)\ge5
   \Longrightarrow
   v_2\!\left(
   \frac{a_{380}(2n)\mathcal M_{380}(0)}{\mathcal B_0}
   \right)=2-\ell.
   \tag{1.2}
$$


6. Original-family reachability of arbitrarily large $\ell$.

The source claim with threshold $\ell\ge4$ is not used.

The newly supplied sixteen even minimum counts imply, through the accepted **model** theorem,


$$
S(C_u,D_u)\in2^{2\mu_u+3}\mathbb Z
\qquad(0\le u\le15).
\tag{1.3}
$$


They do not strengthen the actual residual estimate.

---

## 2. Complete growing central and forcing tails

Here $p\ge1$ denotes a raw binary precision. Write $B_\ell(h)$ for the exact normalized central coefficient displayed in Turn 20.

### Theorem 1 — Uniform conservative cutoffs

Modulo $2^p$, the complete first force is obtained by retaining only


$$
0\le s<2p,\qquad
0\le\ell<4p,\qquad
0\le i<6p.
\tag{2.1}
$$


Here $s$ is the central summation index, $\ell$ the central coefficient index, and $i$ the forcing index.

These bounds hold uniformly on the original family. The same formulas, interpreted as convergent $2$-adic sums and integer-valued polynomials, have the stated tail bounds for $h,n\in\mathbb Z_2$.

### Proof

The scalar factors in the two central sums are


$$
c_s^{\mathrm e}=\frac{2^s(s!)^2}{(2s)!},\qquad
c_s^{\mathrm o}=\frac{2^s(s!)^2}{(2s+1)!},
$$


and satisfy


$$
v_2(c_s^{\mathrm e})=v_2(c_s^{\mathrm o})=v_2(s!).
$$


If $s\ge2p$, then $s!$ contains at least $p$ even factors. Thus both scalar factors lie in $2^p\mathbb Z_2$. All accompanying binomial factors are $2$-integral, including at $2$-adic arguments.

For the central-index tail, a product of $m$ consecutive $2$-adic integers has valuation at least $v_2(m!)$, because


$$
(h)_{\underline m}=m!\binom hm.
$$


For even $\ell=2j\ge4p$, the central prefactor contains a falling product of length $j\ge2p$. For odd $\ell=2j+1\ge4p$, it contains one of length $j+1\ge2p$. Therefore


$$
B_\ell(h)\in2^p\mathbb Z_2
\qquad(\ell\ge4p).
\tag{2.2}
$$



Finally, the exact forcing is


$$
F_i(h,n):=\frac{f_i^0}{R}
=
\sum_{\ell=0}^{i}
\binom i\ell
\prod_{t=\ell+1}^{i}(n+t)\,B_\ell(h).
\tag{2.3}
$$


If $i\ge6p$, every retained $\ell<4p$ leaves a consecutive product of length at least $2p+1$. Its valuation is at least $p$. The omitted $\ell$-terms already have that depth by (2.2). Hence


$$
F_i(h,n)\in2^p\mathbb Z_2
\qquad(i\ge6p).
\tag{2.4}
$$


This proves all three whole-tail assertions. ∎

These are deliberately conservative bounds. They replace, rather than extrapolate, the fixed bounds $s\le9,\ell\le10,i\le17$ used at raw precision $256$.

### 2.1 Explicit precision-$p$ first-force polynomial

Let $B_\ell^{[p]}(h)$ be the displayed central formula with $s=0,\ldots,2p-1$, and put


$$
F_i^{[p]}(h,n)=
\sum_{\ell=0}^{\min(i,4p-1)}
\binom i\ell
\prod_{t=\ell+1}^{i}(n+t)\,B_\ell^{[p]}(h).
\tag{2.5}
$$


Then the complete signed Newton input is


$$
\boxed{
g_p(x;h,n)=
\sum_{i=0}^{6p-1}(-1)^iF_i^{[p]}(h,n)\binom xi.
}
\tag{2.6}
$$


It has degree at most $6p-1$, and represents the actual input modulo $2^p$. No higher coefficient is inferred from an old residue vector.

All rational factors in this construction must be handled exactly, or by stripping their power of two before inversion of their odd denominator.

---

## 3. All contact orders and the finite endpoint

Set


$$
U=-x+x^2-\frac{x^3}{2}+\frac{x^4}{8}
=\sum_{s=1}^4u_sx^{[s]},
\qquad (u_1,u_2,u_3,u_4)=(-1,2,-3,3).
$$


The exact contact symbol is


$$
\phi^n=(1+2U)^h.
$$



Define the finite precision symbol


$$
\Lambda_p(z;h)=
\sum_{r=1}^{p-1}2^r\binom hr U(z)^r
=\sum_{s=1}^{4(p-1)}\lambda_{p,s}(h)z^{[s]}.
\tag{3.1}
$$


Every omitted $r\ge p$ term is zero modulo $2^p$. This safe argument requires no special congruence class of $h$.

For an integral Newton polynomial $f$, define


$$
\mathscr C_{s;n,b}f(x)=
\sum_{v=0}^{s}
(-1)^{s-v}\binom{x}{s-v}\binom nv\,
\mathscr T_{v,b}f(x-s+v),
\tag{3.2}
$$


where


$$
\mathscr T_{0,b}f=f,\qquad
\mathscr T_{v,b}f(y)=
\sum_{z=y}^{b-1}
\binom{v+z-y-1}{v-1}f(z)
\quad(v\ge1),
\tag{3.3}
$$


with its exact polynomial continuation.

The upper endpoint in (3.3) is the **actual $b-1$**. Neither it nor the large reconstruction kernel is replaced by a small reference.

Put


$$
\mathscr K_p=\sum_{s=1}^{4(p-1)}
\lambda_{p,s}(h)\mathscr C_{s;n,b}.
\tag{3.4}
$$


The accepted arbitrary-monomial transport identifies this action with the actual finite contact correction modulo $2^p$.

Since $\mathscr K_p$ maps integral Newton polynomials into twice that lattice,


$$
\boxed{
P_p=
\sum_{q=0}^{p-1}(-\mathscr K_p)^qg_p
}
\tag{3.5}
$$


is the complete signed first solution modulo $2^p$.

Indeed,


$$
(I+\mathscr K_p)P_p-g_p
=(-1)^{p-1}\mathscr K_p^{\,p}g_p
\in2^p\operatorname{Int}(\mathbb Z_2).
\tag{3.6}
$$


This is a coefficient-valued inverse residual, not merely agreement at finitely many matrix rows.

### 3.1 Explicit degree bounds

A safe bound is


$$
\deg\mathscr C_s f\le\deg f+s.
$$


Consequently,


$$
\boxed{
\deg P_p\le d_p:=6p-1+4(p-1)^2.
}
\tag{3.7}
$$


This bound includes some terms already zero modulo $2^p$; that redundancy is harmless.

The stronger weighted observation that a contact term of symbol order $r$ has degree increment at most $4r$ can substantially reduce an implementation. The conservative bound (3.7), however, suffices for the finite reduction below without relying on pruning decisions.

---

## 4. A bounded exact characterization of the actual $p_{380}$

To avoid confusion with the primitive numerator $p_n$, denote the actual signed Newton coefficient by


$$
\mathfrak p_{380}.
$$



### Theorem 2 — Uniform polynomial residue and moving-branch limit

Compute $P_p$ by (2.5)–(3.5), with the endpoint $b$ kept symbolic, and define


$$
\boxed{
\Pi_p(k)=
[x^{\{380\}}]\,
P_p\!\left(x;\,
h=32k+1,\ n=64k+2,\ b=\frac{32k+1}{2001}
\right).
}
\tag{4.1}
$$


Here $[x^{\{r\}}]$ means the coefficient of $\binom xr$, not an ordinary monomial coefficient.

Then:

1. $\Pi_p\in\mathbb Q[k]$, with odd parameter denominator $2001$ allowed.
2. On every original index,
   

$$
\mathfrak p_{380}(u)\equiv\Pi_p(k_u)\pmod{2^p}.
   \tag{4.2}
$$


3. The residues $\Pi_p(k)\pmod{2^p}$ are compatible under increasing $p$, for every $k\in\mathbb Z_2$.
4. There is a continuous function
   

$$
\mathfrak p_{380}^{*}:\mathbb Z_2\longrightarrow\mathbb Z_2
$$


   characterized by these residues. It agrees with the actual coefficient on original indices and satisfies
   

$$
\boxed{
   \lim_{\substack{u:\ v_2(k_u+3)\to\infty}}
   \mathfrak p_{380}(u)
   =
   \mathfrak p_{380}^{*}(-3)
   =
   \lim_{p\to\infty}\Pi_p(-3).
   }
   \tag{4.3}
$$



### Proof

All retained central formulas are rational polynomials in $h$. Finite forcing formation is polynomial arithmetic. The suffix operator maps rational polynomials in $x,b$ to rational polynomials in $x,b$, by finite polynomial summation. Thus (4.1) is a finite rational-polynomial construction.

The tail proofs in §2 and the inverse residual (3.6) show coefficientwise agreement with the complete construction modulo $2^p$. Integral Newton transport preserves every omitted $2^p$-multiple. This proves (4.2).

The same arguments work for $h,n,b\in\mathbb Z_2$: binomial polynomials are integral on $\mathbb Z_2$, and the suffix identities are integral Newton identities in their integer arguments and extend continuously to $2$-adic arguments. Thus two truncation precisions give congruent coefficients at the smaller precision. This proves compatibility.

For each fixed $p$, $\Pi_p$ is continuous. Compatible polynomial residues define a continuous $\mathbb Z_2$-valued function. Finally, original-family reachability and $k_u\to-3$ imply (4.3). ∎

At the limiting parameter the exact substitutions are


$$
\boxed{
k=-3,\qquad h=-95,\qquad n=-190,\qquad b=-\frac{95}{2001}.
}
\tag{4.4}
$$


These are **evaluation parameters for the polynomial continuation**, not replacement original indices or negative-sized matrices. The endpoint dependence has already been encoded by the finite suffix polynomials before making this substitution.

### 4.1 An explicit uniformity certificate

Uniformity need not be asserted abstractly.

After constructing $\Pi_p$, write it in ordinary powers of $k$, and choose


$$
\delta_p=
\max\bigl(0,\,-\min_a v_2([k^a]\Pi_p)\bigr).
\tag{4.5}
$$


Then


$$
2^{\delta_p}\Pi_p\in\mathbb Z_2[k].
$$


For $k,k'\in\mathbb Z_2$,


$$
v_2\bigl(\Pi_p(k)-\Pi_p(k')\bigr)
\ge v_2(k-k')-\delta_p.
\tag{4.6}
$$


Therefore


$$
\boxed{
v_2(k+3)\ge p+\delta_p
\Longrightarrow
\mathfrak p_{380}(k)\equiv\Pi_p(-3)\pmod{2^p}.
}
\tag{4.7}
$$



The integer $\delta_p$ is a finite, exactly computable denominator bound. This gives a verifiable cylinder theorem on the original indices, rather than relying on a few endpoint shifts as evidence of a period.

---

## 5. What this says—and does not say—about compensation

The accepted singularity theorem gives, for $\ell=v_2(k+3)\ge5$,


$$
v_2\!\left(
\frac{\mathfrak p_{380}(u)a_{380}(2n)\mathcal M_{380}(0)}
{\mathcal B_0}
\right)
=
v_2(\mathfrak p_{380}(u))+2-\ell.
\tag{5.1}
$$



### Corollary 3 — A finite certificate can disprove termwise compensation

Suppose a bounded calculation finds


$$
v_2(\Pi_p(-3))=q<p.
\tag{5.2}
$$


Then, on every original index with


$$
\ell\ge\max(5,p+\delta_p),
$$


one has


$$
v_2(\mathfrak p_{380}(u))=q.
$$


Consequently the valuation in (5.1) equals


$$
q+2-\ell,
$$


and is unbounded below on the original family.

This would rigorously disprove coefficient compensation for this individual moment.

### The zero-limit case is subtler

If


$$
\Pi_p(-3)\equiv0\pmod{2^p}
\quad\text{for every }p,
$$


then $\mathfrak p_{380}^{*}(-3)=0$. Continuity alone gives only


$$
v_2(\mathfrak p_{380}(u))\longrightarrow\infty
\quad(\ell\to\infty).
$$


It does not give


$$
v_2(\mathfrak p_{380}(u))\ge\ell-2,
\tag{5.3}
$$


which is the exact condition for the individual normalized term in (5.1) to be integral.

Thus the concrete follow-on coefficient lemma is:

> **Quantitative compensation lemma.** Establish, or refute,
> 

$$
> \mathfrak p_{380}^{*}(k)\in
> 2^{-2}(k+3)\mathbb Z_2
>
$$


> on the reachable neighborhood $v_2(k+3)\ge5$, interpreted as the valuation inequality (5.3).

An unevaluated zero-limit claim is not a proof of this lemma.

I have not evaluated (5.2), nor proved (5.3). Therefore the compensation question is reduced to exact coefficient arithmetic and a quantitative local theorem, but is not resolved in this response.

---

## 6. Complete grouped reconstruction before kernel division

If termwise compensation fails, the valid next object is the complete finite suffix reconstruction.

For each precision $p$, write


$$
P_p(x)=\sum_{r=0}^{d_p}p_r^{[p]}\binom xr,
$$


and put


$$
F_s^{[p]}(x;A)=
\binom{A+s-1}{s}
\sum_{r=s}^{d_p}p_r^{[p]}\binom{x}{r-s},
\qquad A=2n.
\tag{6.1}
$$


The exact finite suffix identity yields


$$
\theta_j\equiv(-1)^j
\sum_{s=0}^{d_p}F_s^{[p]}(j;A)\mathcal M_s(j)
\pmod{2^p}.
\tag{6.2}
$$


With


$$
U_s^{[p]}(x)=
F_s^{[p]}(x)+xF_s^{[p]}(x-1)
+xF_{s+1}^{[p]}(x-1),
\tag{6.3}
$$


the first raw column is


$$
2X_j\equiv
(-1)^{j+1}W_j
\sum_{s=-1}^{d_p}U_s^{[p]}(j)\mathcal M_s(j)
\pmod{2^p}.
\tag{6.4}
$$



This is the appropriate complete grouped identity. At $j=0$, it is


$$
\boxed{
-2X_0\equiv
\sum_{s=0}^{d_p}
p_s^{[p]}
\binom{2n+s-1}{s}
\mathcal M_s(0)
\pmod{2^p}.
}
\tag{6.5}
$$


All $s$, not just $380$, occur before division by $\mathcal B_0$.

Equation (6.5) establishes the grouping but **not its desired content**. To obtain compensation by grouping, one must prove divisibility of its complete right-hand side. Neither its integral summands nor its finite-suffix origin imply divisibility by the moving kernel $\mathcal B_0$.

A useful next lemma would be a finite telescoping identity for (6.5), with endpoint terms explicit, whose remainder is divisible by the required kernel content. No such telescoping identity is established here.

---

## 7. Growing exterior force and all boundary insertions

At raw precision $p$, retain


$$
f_a=\frac{(b+a)!}{b!},\qquad 0\le a<2p.
$$


As proved in Turn 7,


$$
f_a\in2^p\mathbb Z_2\qquad(a\ge2p).
\tag{7.1}
$$


Thus the complete retained exterior data are


$$
\boxed{
B_a^{[p]}=
\sum_{u=a}^{2p-1}f_u\binom{2n}{u-a},
\qquad0\le a<2p.
}
\tag{7.2}
$$



The arbitrary-monomial exterior insertion displayed by the supplied implementation has the exact polynomial form


$$
J_{s,p}(x)=
\sum_{a=0}^{2p-1}B_a^{[p]}
\sum_{v=1}^{s}
(-1)^{b+a+s-v}
\binom{x}{s-v}\binom nv
\binom{b+a-x+s-1}{v-1}.
\tag{7.3}
$$


On the original family $b$ is odd, so the sign in (7.3) has a fixed polynomial-compatible interpretation. Its degree in $x$ is at most $s-1$.

Consequently the full retained contact-induced second forcing is


$$
J_p=\sum_{s=1}^{4(p-1)}\lambda_{p,s}J_{s,p},
\tag{7.4}
$$


and its finite inverse is


$$
Q_p=\sum_{q=0}^{p-1}(-\mathscr K_p)^qJ_p
\pmod{2^p},
\tag{7.5}
$$


in addition to any retained logarithmic-force input.

This restores all contact-induced exterior orders, not just the degree-eight correction visible modulo $256$. The exterior part of the solution remains


$$
-\sum_{a=0}^{2p-1}B_a^{[p]}
\binom{-2n}{b+a-i},
\tag{7.6}
$$


with its actual $b+a-i$, followed by the polynomial part from $Q_p$.

For the specific target


$$
T=2\mu+4,\qquad p=T+3,
$$


the whole logarithmic-force estimate and the accepted comparison


$$
\mu\le\operatorname{bitlength}(2C+D)
$$


show that its complete normalized input is zero modulo $2^p$. This omission occurs before integral contact inversion and reconstruction. It is not an all-precision assertion that the logarithmic force is identically zero.

The endpoint remains


$$
2X_b=W_b\,b\theta_{b-1},
\qquad
4Y_b=W_b(1+b\eta_{b-1}).
\tag{7.7}
$$


The $+1$ has not been removed.

---

## 8. The actual residual still requires a scalar theorem

Let $F_j^{[p]}$ denote the complete first raw numerator in (6.4), including its weight and with the endpoint from (7.7). Then


$$
4N\equiv
\sum_{t=0}^{D-1}\sum_{\rho=0}^{127}
(F_{128t+\rho}^{[p]})^2
+
\sum_{\rho=0}^{80}(F_{128D+\rho}^{[p]})^2
+
(F_b^{[p]})^2
\pmod{2^p}.
\tag{8.1}
$$


Thus the proposed norm theorem is equivalent, at sufficient raw precision, to


$$
\boxed{
\sum_{j=0}^{b}(F_j^{[p]})^2-8S(C,D)
\equiv0\pmod{2^{T+2}},
\qquad T=2\mu+4.
}
\tag{8.2}
$$


This retains the complete first force, finite inverse, shortened terminal block, and actual endpoint.

The force restoration is now explicit. What is missing is a proof that the **complete scalar** (8.2) vanishes uniformly on the original family. The scalar includes actual large binomial kernels; coefficient-cylinder uniformity does not make those kernels periodic.

In particular:

* A nonzero limiting $\mathfrak p_{380}^{*}(-3)$ would refute an individual-term argument, not (8.2).
* A successful quantitative compensation lemma would supply a local content statement, not automatically the extra scalar cancellation in (8.2).
* The sixteen even model counts do not determine (8.2).

---

## 9. Bounded exact arithmetic proposed for personal inspection

The appropriate next calculation is the coefficient-limit certificate, not another model minimum count.

### Inputs

For a chosen precision $p$, use exactly:

1. Central formulas (Turn 20, equations 2.1–2.2), with
   

$$
s<2p,\qquad\ell<4p.
$$


2. Exact force (2.5), with $i<6p$.
3. $U=(-1,2,-3,3)$ in divided-power coordinates.
4. Every contact-symbol order $1\le r<p$.
5. The polynomial suffix operator with symbolic upper endpoint $b$.
6. The $p$-term inverse (3.5).
7. The substitutions (1.1).

No old residue vector is an input.

### Degree and precision certificate

Use the degree bound


$$
d_p=6p-1+4(p-1)^2.
$$


Compute all Newton coefficients through that bound, or use rigorously justified coefficient-weight pruning. If $d_p<380$, the desired coefficient is zero at that precision without further evaluation.

All arithmetic is exact rational arithmetic or valuation/odd-unit arithmetic. No even denominator is inverted modulo $2^p$.

### Required outputs

1. The exact polynomial $\Pi_p(k)$, or a reproducible straight-line representation of it.
2. Its evaluated residue
   

$$
R_p=\Pi_p(-3)\pmod{2^p}.
$$


3. The exact denominator bound $\delta_p$ in (4.5).
4. The coefficient-valued inverse residual
   

$$
(I+\mathscr K_p)P_p-g_p\equiv0\pmod{2^p}.
$$


5. Compatibility with the preceding computed precision.
6. If $R_p\ne0$, its exact valuation $q<p$, and the certified original cylinder
   

$$
v_2(k+3)\ge p+\delta_p
$$


   on which $v_2(\mathfrak p_{380})=q$.

A first bounded batch may take $p=16,32,64$, with later precision increased only if the residues remain zero. These are finite coefficient calculations, not growing original matrices. I give no unmeasured runtime claim.

**Expected verifiable output is a residue and a certificate, not an expected nonzero answer.** If all residues in this batch are zero, the output proves only those finite-precision vanishing statements.

---

## 10. Primitive denominator and whole evaluated error

No normalization is changed.

With the least actual clearer $d_B$, let


$$
N_B=d_B[u,v],
$$




$$
A_B=N_{B,1}^{T}\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^{T}\Omega N_{B,2}.
$$


The final gcd and actual primitive pair are


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=\frac{A_B}{g_B}>0,\qquad
p_n=\frac{H_B}{g_B}.
}
\tag{10.1}
$$


This gcd includes every odd prime. The primitive multiplier remains $d_B^2/g_B$.

For $\alpha=v_2(N)$ and $\gamma=v_2(H)$, the retained interface is


$$
v_2(q_n)=
\max\left\{
0,\frac{3n}{2}-v_2(b!)-s_2(n)-1-(\gamma-\alpha)
\right\}.
\tag{10.2}
$$


The coefficient characterization does not determine $\alpha$, $\gamma$, or the full denominator.

The accepted whole signed error is


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi)<0
\quad\text{eventually},
$$




$$
\log|\epsilon_n|
=
-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$


Hence the entire evaluated form remains


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n>0
}
\quad\text{eventually}.
\tag{10.3}
$$


A same-index bound on the **full primitive denominator** sufficient to make (10.3) tend to zero remains necessary for an irrationality proof by this family.

---

## 11. Final result and proof status

### New rigorous reduction

The supplied exact central force now yields:

* complete growing cutoffs
  

$$
s<2p,\qquad\ell<4p,\qquad i<6p;
$$


* an all-contact-order finite inverse modulo $2^p$, with the actual endpoint retained;
* an explicit degree bound;
* a finite rational-polynomial residue $\Pi_p(k)$ for the actual signed coefficient $\mathfrak p_{380}$;
* a compatible characterization of its limit at $k=-3$;
* an exact, computable uniformity bound on the original indices;
* a finite-certificate criterion that would disprove termwise force-shift compensation.

The growing exterior force and contact insertion are likewise explicit at the target precision, with the whole logarithmic-force omission justified before normalization.

### What remains unresolved

This report does **not** evaluate $\Pi_p(-3)$ at a precision that establishes a nonzero limit, prove quantitative coefficient compensation, or establish a grouped cancellation theorem. Therefore it does not resolve


$$
N-2S(C,D)\in2^{2\mu+4}\mathbb Z_2.
$$



The immediate bounded task is to evaluate the coefficient-limit certificate above. The exact remaining structural bottleneck is then either:

1. quantitative divisibility of the actual coefficient near $k=-3$, or
2. a complete grouped identity before common-kernel division,

followed in either case by the whole scalar residual (8.2), the mixed contraction, and the final-denominator/whole-error comparison.



$$
\boxed{\text{The irrationality of }e+\pi\text{ remains unresolved.}}
$$


