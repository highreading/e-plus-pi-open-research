> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, Turn 9 — Linear precision–degree filtration and an endpoint-preserving coefficient recurrence

## Executive assessment

The quadratic degree bound in Turn 8 can be replaced by a **linear bound**, with the complete central force and every finite contact endpoint retained:



$$
\boxed{\deg P_p\le 4p-1\pmod{2^p}.}
\tag{0.1}
$$



Here and below, a degree bound modulo $2^p$ means that every Newton coefficient above that degree is divisible by $2^p$.

In particular,


$$
\boxed{\mathfrak p_{380}^{*}(-3)\equiv0\pmod{2^{95}}.}
\tag{0.2}
$$


The same divisibility holds for the actual coefficient on every original index. Thus precision $96$, not any of $16,32,64$, is the first precision **not excluded by this filtration** from detecting coefficient $380$.

This is not a proof that precision $96$ actually detects it. Contact-operator cancellations can improve the degree bound, and the argument below does not prove sharpness for the actual solution.

I also derive a particularly simple exact recurrence for all finite suffix operators:


$$
\boxed{
\mathscr T_{v,b}=\mathscr S_b^{\,v},\qquad
\mathscr S_b\binom xr=\binom b{r+1}-\binom x{r+1}.
}
\tag{0.3}
$$


It permits evaluation at


$$
h=-95,\qquad n=-190,\qquad b=-95/2001
$$


using only already justified polynomial continuation. No negative-sized matrix is introduced.

**What is not closed:** I do not determine whether the coefficient limit is zero or has finite valuation. Consequently, I do not prove the quantitative $k+3$ compensation, a grouped norm-content theorem, the full scalar residual, or irrationality of $e+\pi$. This is a partial advance: it closes the quadratic-degree obstruction and proves a substantial coefficient divisibility, but not the requested coefficient-limit evaluation.

No tools have been executed.

---

## 1. Scope, original domain, and retained results

The original family remains


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0,
$$


with


$$
b=128D+81,\quad n=128C+66,\quad C=4002D+2532,
$$


and


$$
k=2C+1,\qquad h=32k+1,\qquad n=64k+2,\qquad
b=\frac{32k+1}{2001}.
$$



Every actual contact matrix has indices


$$
0\le i,j<b.
$$


The scalar coordinates remain $0\le j\le b$, partitioned as


$$
0\le t<D,\quad 0\le\rho<128;
\qquad
t=D,\quad 0\le\rho\le80;
$$


with $j=b=128D+81$ separate.

I reuse the accepted integral Newton-polynomial contact transport and its polynomial suffix continuation. The proofs below do not assume that the transport is multiplicative in the contact symbol.

I retain the corrected shift theorem only at its proved threshold:


$$
v_2(k+3)=\ell\ge5
\Longrightarrow
v_2\!\left(
\frac{a_{380}(2n)\mathcal M_{380}(0)}{\mathcal B_0}
\right)=2-\ell.
\tag{1.1}
$$


The supplied twelve reachability cases $\ell=5,\ldots,16$ are reused at their stated finite scope; no repeat calculation is proposed.

The accepted fixed-precision interfaces, including


$$
H-N\in128\mathbb Z_2,\qquad N-2S\in256\mathbb Z_2,
$$


are not promoted to growing-precision residual theorems.

---

## 2. Index-dependent factorial depth of the complete force

Put


$$
L(m)=v_2(m!)\qquad(m\ge0).
$$



The central formulas give


$$
v_2(B_\ell(h))\ge L\!\left(\left\lceil\frac\ell2\right\rceil\right)
\tag{2.1}
$$


for every $h\in\mathbb Z_2$. Indeed:

* for $\ell=2j$, the prefactor contains $(h)_{\underline j}$;
* for $\ell=2j+1$, it contains $(h)_{\underline{j+1}}$;
* the other prefactor factors are integral;
* every central summand is integral, with additional scalar depth $L(s)$.

The complete infinite central sum therefore preserves the bound (2.1). It is not necessary to replace the sum by an old residue vector.

The forcing is


$$
F_i(h,n)=
\sum_{\ell=0}^i
\binom i\ell
\prod_{t=\ell+1}^i(n+t)\,B_\ell(h).
$$


Consequently,


$$
\boxed{
v_2(F_i(h,n))\ge w_i,
}
\tag{2.2}
$$


where


$$
w_i=
\min_{0\le\ell\le i}
\left\{
v_2\binom i\ell+
L(i-\ell)+
L\!\left(\left\lceil\frac\ell2\right\rceil\right)
\right\}.
\tag{2.3}
$$



This is a uniform bound for the **whole forcing entry**, including every central-index and summation tail.

### Lemma 1 — A linear force envelope

For all $i\ge0$,


$$
\boxed{i-4w_i\le3.}
\tag{2.4}
$$



### Proof

Fix $\ell$, put


$$
m=\left\lceil\frac\ell2\right\rceil,\qquad t=i-\ell.
$$


Then $\ell\le2m$, and


$$
L(m)\ge\left\lfloor\frac m2\right\rfloor,\qquad
L(t)\ge\left\lfloor\frac t2\right\rfloor.
$$


It follows that


$$
\begin{aligned}
i-4\bigl(L(m)+L(t)\bigr)
&\le
2m-4\left\lfloor\frac m2\right\rfloor
+t-4\left\lfloor\frac t2\right\rfloor\\
&\le2+1=3.
\end{aligned}
$$


Adding the nonnegative depth $v_2\binom i\ell$ only improves the inequality. Taking the minimum defining $w_i$ proves (2.4). ∎

Thus the complete signed input


$$
g(x)=\sum_{i\ge0}(-1)^iF_i\binom xi
$$


has the precision-dependent support


$$
\boxed{
g\bmod2^p\text{ has degree at most }4p-1.
}
\tag{2.5}
$$



This improves the uniform $i<6p$ cutoff from Turn 8. It also supplies the weighted information needed after contact inversion, rather than merely a standalone input cutoff.

---

## 3. Weighted contact inversion: the quadratic bound disappears

Write


$$
U=-x+x^2-\frac{x^3}{2}+\frac{x^4}{8}
$$


in the integral divided-power ring, and decompose the contact correction by symbol order:


$$
\mathscr K=\sum_{r\ge1}\mathscr K_r,
$$


where


$$
\mathscr K_r=
\sum_{s=1}^{4r}
2^r\binom hr[x^{[s]}]U^r\,\mathscr C_{s;n,b}.
\tag{3.1}
$$



Each $\mathscr K_r$:

1. increases Newton degree by at most $4r$;
2. maps the integral Newton lattice into $2^r$ times that lattice.

The second statement follows from divided-power integrality and integral contact transport. It is valid with the actual finite upper endpoint.

Consider a contribution originating in forcing index $i$, followed by contact orders $r_1,\ldots,r_q$. Write


$$
R=r_1+\cdots+r_q.
$$


Its valuation is at least $w_i+R$, and its degree is at most $i+4R$. If it survives modulo $2^p$, then


$$
w_i+R\le p-1.
$$


Lemma 1 gives


$$
i+4R
\le 4w_i+3+4R
\le4p-1.
$$



### Theorem 2 — Complete linear degree bound

For the complete first-force solution,


$$
P_p\equiv\sum_{q=0}^{p-1}(-\mathscr K)^qg\pmod{2^p},
$$


one has


$$
\boxed{\deg P_p\le4p-1\pmod{2^p}.}
\tag{3.2}
$$



This includes all retained force tails, all contact orders, and all finite endpoint terms.

### Why endpoint terms do not invalidate the proof

The accepted bound is


$$
\deg\mathscr T_{v,b}f\le\deg f+v.
$$


Hence each summand in


$$
\mathscr C_sf(x)=
\sum_{v=0}^s
(-1)^{s-v}\binom{x}{s-v}\binom nv
\mathscr T_{v,b}f(x-s+v)
$$


has degree at most


$$
(s-v)+(\deg f+v)=\deg f+s.
$$


This argument applies to the entire suffix polynomial, not just its highest-degree part. In particular, it retains every $b$-dependent integration constant.

---

## 4. What precision can see coefficient $380$?

Applying Theorem 2 at $p=95$ gives


$$
4p-1=379.
$$


Therefore


$$
\boxed{
\mathfrak p_{380}(u)\in2^{95}\mathbb Z_2
\quad\text{for every original }u,
}
\tag{4.1}
$$


and, by the compatible continuation,


$$
\boxed{
\mathfrak p_{380}^{*}(-3)\in2^{95}\mathbb Z_2.
}
\tag{4.2}
$$



At $p=96$, the bound is $383$, so coefficient $380$ is no longer excluded.

The distinction is important:

* **Proved:** no precision $p\le95$ can detect a nonzero residue.
* **Proved:** $p=96$ is the first precision permitted by the envelope (3.2).
* **Not proved:** the actual coefficient is nonzero modulo $2^{96}$.
* **Not proved:** $4p-1$ is the sharp degree bound for the actual contact solution.

Thus the Turn 8 batch $p=16,32,64$ would necessarily return zero for this coefficient. It cannot resolve the obstruction.

### A source of further degree improvement

If $f$ has leading Newton term $c_d\binom xd$, then


$$
\boxed{
[x^{\{d+s\}}]\mathscr C_sf
=
(-1)^s\binom{n+d+s}{s}c_d.
}
\tag{4.3}
$$



To prove this, the leading ordinary coefficient of $\mathscr T_{v,b}f$ is


$$
\frac{(-1)^vc_d}{(d+v)!}.
$$


After multiplication by $\binom{x}{s-v}$, conversion to the Newton coefficient of degree $d+s$, and summation over $v$, the result is


$$
(-1)^sc_d
\sum_{v=0}^s
\binom{d+s}{s-v}\binom nv
=
(-1)^sc_d\binom{n+d+s}{s}.
$$


Vandermonde is a polynomial identity, so negative integral $n$ is allowed here.

This formula explains why the linear envelope need not be sharp: top-degree transport can acquire additional binary depth or vanish exactly. However, vanishing of this leading coefficient does **not** by itself prove that all intermediate-degree or endpoint contributions vanish.

---

## 5. Exact suffix recurrence with every endpoint retained

Define


$$
(\mathscr S_bf)(x)=\sum_{z=x}^{b-1}f(z)
$$


first for ordinary finite sums and then by polynomial continuation.

The hockey-stick identity gives


$$
\boxed{
\mathscr S_b\binom xr
=
\binom b{r+1}-\binom x{r+1}.
}
\tag{5.1}
$$



Thus, if


$$
f(x)=\sum_{r=0}^d a_r\binom xr,
$$


then the Newton coefficients of $\mathscr S_bf$ are exactly


$$
\boxed{
(\mathscr S_bf)_0=\sum_{r=0}^d a_r\binom b{r+1},
\qquad
(\mathscr S_bf)_{r+1}=-a_r.
}
\tag{5.2}
$$



Every endpoint contribution is concentrated explicitly in the new constant coefficient.

### Lemma 3 — Iterated suffix identity

For every integer $v\ge0$,


$$
\boxed{\mathscr T_{v,b}=\mathscr S_b^{\,v}.}
\tag{5.3}
$$



### Proof

The cases $v=0,1$ follow from the definitions. For a genuine finite interval, interchanging finite sums gives


$$
\mathscr S_b\mathscr T_{v,b}f(x)
=
\sum_{z=x}^{b-1}
\left(
\sum_{y=x}^{z}
\binom{v+z-y-1}{v-1}
\right)f(z).
$$


The inner sum is $\binom{v+z-x}{v}$, proving the next case. Both sides are polynomial functions of $x,b$ for polynomial $f$; the identity therefore extends by polynomial continuation. ∎

At the limiting parameters, the practical recurrence is consequently


$$
T_0=f,\qquad T_{v+1}=\mathscr S_{-95/2001}T_v,
\tag{5.4}
$$


followed by


$$
\mathscr C_sf(x)=
\sum_{v=0}^s
(-1)^{s-v}\binom{x}{s-v}\binom{-190}{v}
T_v(x-s+v).
\tag{5.5}
$$



These are polynomial operations of bounded degree. They do not refer to a matrix of size $-95/2001$, or to any altered original matrix boundary.

---

## 6. Precision-safe recurrence for a bounded coefficient calculation

For a chosen raw precision $p$, let


$$
D_p=4p-1.
$$


The following ingredients suffice:

1. Central indices $0\le\ell\le D_p$, pruning those with
   

$$
L(\lceil\ell/2\rceil)\ge p.
$$


2. Central summation indices satisfying $L(s)<p$; the conservative range $s<2p$ remains valid.
3. Forcing indices $0\le i\le D_p$, pruning with the exact lower bound $w_i$.
4. Contact orders $1\le r<p$, with all their divided-power coefficients.
5. The suffix recurrence (5.2), always using $b=-95/2001$.

Compute the full retained input $g_p$, not a lifted fixed-precision vector. Then use


$$
P^{(0)}=0,\qquad
P^{(m+1)}=g_p-\mathscr K_pP^{(m)}\pmod{2^p}.
\tag{6.1}
$$


Because $\mathscr K_p$ is even, $p$ iterations suffice.

All coefficients above $D_p$ may be discarded **after the complete contact application**: Theorem 2 shows that they vanish modulo $2^p$ in these iterates. One must not discard a high-degree intermediate suffix term merely because its degree is large; its later boundary constant can affect low degrees.

For polynomial implementation, translations and products can use the exact identities


$$
\binom{x-a}{r}
=
\sum_{j=0}^r\binom{-a}{r-j}\binom xj,
\tag{6.2}
$$


and


$$
\binom xa\binom xb
=
\sum_{j=\max(a,b)}^{a+b}
\frac{j!}{(j-a)!(j-b)!(a+b-j)!}\binom xj.
\tag{6.3}
$$


All displayed structure constants are integers.

### Complexity and arithmetic scope

The suffix recurrence itself is inexpensive: producing $T_0,\ldots,T_S$ from a degree-$D$ polynomial takes $O(S(D+S))$ arithmetic operations after the $\binom b r$ table is available.

A straightforward dense implementation of all translations, products, contact applications, and $p$ fixed-point steps has a conservative polynomial arithmetic bound $O(p^5)$ when $D,S=O(p)$. This is an arithmetic-operation bound, not a measured runtime or a bit-complexity guarantee. Weighted pruning and cached transforms should reduce the workload, but no unproved runtime claim is needed.

At the first admissible precision,


$$
p=96,\qquad D_p=383.
$$


The complete central input requires at most $384\cdot192$ unpruned central summands. No original-sized matrix or original-sized factorial is involved.

Even denominators must never be inverted modulo $2^p$. Evaluate rational binomials by exact cancellation, or by stripping their powers of two before odd-unit inversion.

---

## 7. Compensation: a proved lower bound, not the missing local factor

The new divisibility gives


$$
v_2(\mathfrak p_{380}(u))\ge95.
$$


Combining it with the corrected shift theorem yields


$$
v_2\!\left(
\frac{\mathfrak p_{380}(u)a_{380}(2n)\mathcal M_{380}(0)}
{\mathcal B_0}
\right)
\ge97-\ell.
\tag{7.1}
$$



Thus this particular term is proved integral whenever


$$
5\le\ell\le97.
\tag{7.2}
$$


This includes the supplied twelve certified depths, without recomputing their reachability.

It does not handle arbitrarily large $\ell$. A fixed absolute coefficient depth cannot compensate for the unbounded loss $2-\ell$.

The exact remaining individual-term lemma is still


$$
\boxed{
v_2(\mathfrak p_{380}^{*}(k))
\ge v_2(k+3)-2
\quad\text{when }v_2(k+3)\ge5.
}
\tag{7.3}
$$



A concrete stronger route would be to prove a convergent local factorization


$$
\mathfrak p_{380}^{*}(k)=(k+3)G(k),
\qquad
G(k)\in2^{-2}\mathbb Z_2
$$


throughout that neighborhood. Neither continuity nor (4.2) proves this factorization.

If the limit has finite valuation $q$, the accepted reachability theorem instead forces eventual failure of individual-term compensation. The bounded calculation described above can detect that alternative, but no nonzero residue is asserted here.

---

## 8. What is preserved in the unresolved scalar problem

No grouped content theorem follows from the new degree filtration. The full raw first-column contraction remains


$$
4N=\sum_{j=0}^b(2X_j)^2,
$$


with the exact terminal partition and the endpoint


$$
2X_b=W_b\,b\theta_{b-1}.
$$


For the second column, the endpoint remains


$$
4Y_b=W_b(1+b\eta_{b-1});
$$


the $+1$ is not removed.

The complete scalar obligation remains


$$
\sum_{j=0}^b(F_j^{[p]})^2-8S(C,D)
\equiv0\pmod{2^{2\mu+6}},
$$


at sufficient raw precision, where $F_j^{[p]}$ denotes the whole first raw numerator. The mixed contraction remains separate.

The present first-coefficient result neither omits the second forcing nor evaluates it: the complete factorial/exterior force and the whole logarithmic-force estimate retain exactly their Turn 8 scopes. No all-precision deletion of the logarithmic force is made.

---

## 9. Primitive arithmetic and the whole evaluated error

Retain the least actual clearer $d_B$, the integer columns


$$
N_B=d_B[u,v],
$$


and


$$
A_B=N_{B,1}^{T}\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^{T}\Omega N_{B,2}.
$$


The final reduction is


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B>0,\qquad p_n=H_B/g_B.
}
$$


This is the full gcd, including all odd primes. The primitive multiplier remains $d_B^2/g_B$.

The retained nonvanishing statements $N>0$ and $H\ne0$ are unchanged. The complete signed error remains


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi)<0
\quad\text{eventually},
$$


with


$$
\log|\epsilon_n|
=
-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$


Hence


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n>0
\quad\text{eventually}.
}
$$


Nothing proved here bounds the full primitive denominator sufficiently to make this whole evaluated form tend to zero.

---

## 10. Final ledger and bounded calculation

### New proved results

1. The complete force has the factorial-depth bound (2.3).
2. The complete first solution satisfies
   

$$
\deg P_p\le4p-1\pmod{2^p},
$$


   including all finite endpoints.
3. Consequently,
   

$$
\mathfrak p_{380}(u),\ \mathfrak p_{380}^{*}(-3)\in2^{95}\mathbb Z_2.
$$


4. Individual-term integrality is proved for the dangerous moment on every reachable depth $5\le\ell\le97$.
5. The exact suffix recurrence (5.2)–(5.5) gives an endpoint-preserving bounded evaluation method at the limiting parameters.

### Precise limitations

The bound is not proved sharp for the actual solution. Precision $96$ is the first **filtration-admissible** precision, not an established first nonzero precision.

The coefficient limit has not been evaluated. Its vanishing, finite valuation, and quantitative local divisibility remain unresolved. No grouped content theorem or scalar residual theorem is supplied in their place.

### Next bounded calculation worth inspecting

Use


$$
p=96,\quad h=-95,\quad n=-190,\quad b=-95/2001,
$$


the complete central formulas, the factorial pruning (2.3), all contact orders $r<96$, and the suffix recurrence above.

The required verifiable outputs are:

* the coefficient
  

$$
R_{96}=[x^{\{380\}}]P_{96}\pmod{2^{96}};
$$


* its forced reduction $R_{96}\equiv0\pmod{2^{95}}$;
* the complete coefficient-valued inverse residual
  

$$
(I+\mathscr K_{96})P_{96}-g_{96}\equiv0\pmod{2^{96}};
$$


* a certificate that all retained Newton coefficients above degree $383$ vanish modulo $2^{96}$.

If $R_{96}=2^{95}$, the limiting valuation is exactly $95$, and individual-term compensation fails on sufficiently deep original branches. If $R_{96}=0$, the calculation proves only one additional bit of vanishing; it does not prove a zero limit.

The immediate mathematical bottleneck is therefore the **actual limit or a local $k+3$ factor**, not force restoration or quadratic polynomial size. Beyond it remain grouped scalar cancellation, the mixed contraction, the full gcd, and the primitive-denominator/whole-error comparison.



$$
\boxed{\text{No unconditional proof or disproof of irrationality of }e+\pi\text{ is obtained.}}
$$


