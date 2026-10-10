> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, Turn 12 — General negative-integer truncation and simultaneous high-shift control

## Executive conclusion

The coordinator’s exact calculation settles the finite coefficient decision:


$$
\boxed{\mathfrak p_{380}^{*}(-3)=0.}
$$


The receipt certifies the rational calculation, with 9216 central summands, 191 coefficientwise crosschecks, and exact inverse residuals. Its identification with the continued solution still uses the continuation and contact identities; agreement of two finite inverses alone does not prove those identities.

There is now an analytic explanation of the observed pattern. For every positive integer $a$, put $N=2a$. At the continued parameter


$$
h=-a,\qquad n=-N,
$$


the **entire high sector**, not just its first $N+1$ coefficients, satisfies


$$
\boxed{
p_{N+m}=B_N(-a)(N-1)_{\underline m}\qquad(m\ge0).
}
\tag{A}
$$


Consequently,


$$
\boxed{p_r=0\qquad(r\ge2N).}
\tag{B}
$$


The proof below comes directly from the complete terminating central formulas and the exact contact equation. It does not extrapolate the finite receipt.

On the parameter line $n=64k+2$, this supplies the coefficientwise root hierarchy


$$
\boxed{
p_r^{*}(-c)=0
\quad\text{for every integer }c\ge1
\text{ with }128c-4\le r.
}
\tag{C}
$$


Assuming the uniform Lipschitz theorem currently assigned to A4 passes at its stated all-coefficient scope, these roots give


$$
\boxed{
v_2(p_r^{*}(k))
\ge
3+\max_{1\le c\le\lfloor(r+4)/128\rfloor}v_2(k+c).
}
\tag{D}
$$



A maximum of local depths is not their sum. Nevertheless, a consecutive-product lemma converts (D) into a simultaneous bound for **every positive high shift in the complete first-column reconstruction**. If


$$
c_s=\left\lfloor\frac{s+4}{128}\right\rfloor\ge1,
$$


then the entire order-$s$ reconstructed group, normalized by its actual higher kernel, has an explicit loss bounded by


$$
\boxed{v_2((c_s-1)!)-3,}
\tag{E}
$$


with additional nonnegative, explicitly retained weight and numerator valuations. In particular, there is no remaining loss growing like an arbitrarily deep $v_2(k+c)$ for a fixed shift.

This is a useful whole-high-sector result, but it is **not yet a content-relative norm theorem**. The factorial loss in (E) grows with the shift. Neither its elimination at growing precision nor the required complete scalar cancellation is proved here.

No unconditional proof or disproof of irrationality of $e+\pi$ is obtained.

---

## 1. Domain, scope, and proof dependencies

The actual family remains


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0,
$$


with


$$
b=128D+81,\qquad n=128C+66,\qquad C=4002D+2532,
$$


and


$$
k=2C+1,\qquad h=32k+1,\qquad n=64k+2,\qquad
b=\frac{32k+1}{2001}.
$$



Actual contact matrices retain


$$
0\le i,j<b.
$$


The scalar coordinates retain


$$
0\le j\le b,
$$


partitioned into


$$
0\le t<D,\quad0\le\rho<128,
$$


the shortened block


$$
t=D,\quad0\le\rho\le80,
$$


and the separate endpoint $j=b$.

Negative integers below are **evaluation parameters of the polynomial continuation**, never negative matrix sizes.

### Status of the inputs

I use the complete central-force formulas, suffix identities, finite contact transport, and compatible Newton-lattice construction at their supplied scope.

The exact endpoint factorization is rederived below. The quantitative statements using


$$
P(k)-P(k')\in2^{v_2(k-k')+3}\mathcal M
\tag{1.1}
$$


are explicitly **conditional on A4’s pending audit of that theorem**. The present argument does not upgrade a pending theorem to an accepted input.

The coordinator’s receipt is accepted as a finite exact rational computation. I have not executed its code or inspected the hashed large artifact.

---

## 2. Exact central generating function at every negative even $n$

Let


$$
N=2a,\qquad a\ge1,
$$


and evaluate the complete central formulas at $h=-a$. Write


$$
B_\ell=B_\ell(-a).
$$



For $\ell\ge N$, both central sums terminate: writing $\ell=2j$ or $2j+1$, their factor $\binom{h+j}{s}$ becomes $\binom{j-a}{s}$.

Define the formal exponential series


$$
\mathcal H_N(z)=\sum_{m\ge0}\frac{B_{N+m}}{m!}z^m.
$$



### Theorem 1 — Complete high-central generating function

For every positive even integer $N=2a$,


$$
\boxed{
\mathcal H_N(z)
=
B_N\left(1+z+\frac{z^2}{2}\right)^{-N}.
}
\tag{2.1}
$$



This is an identity in $\mathbb Q[[z]]$. Each coefficient on its left is obtained from a finite terminating central sum.

### Proof

Use $(x)_r$ for a rising factorial. Relative to $B_N$, the even central formula at $j=a+r$ gives


$$
\frac{B_{N+2r}}{B_N}
=
(-1)^r\frac{(2r)!}{2^r r!}(N)_r
\sum_{s=0}^{r}
\frac{(-r)_s(N+r)_s}{(1/2)_s\,s!}\,2^{-s}.
\tag{2.2}
$$


Indeed, the added odd factors are


$$
1\cdot3\cdots(2r-1)=\frac{(2r)!}{2^r r!},
$$


the added falling factors are


$$
(-N)_{\underline r}=(-1)^r(N)_r,
$$


and


$$
\frac{2^s(s!)^2}{(2s)!}
=
\frac{s!}{2^s(1/2)_s}.
$$



Likewise, the odd central formula gives


$$
\frac{B_{N+2r+1}}{B_N}
=
(-1)^{r+1}\frac{(2r+1)!}{2^r r!}(N)_{r+1}
\sum_{s=0}^{r}
\frac{(-r)_s(N+r+1)_s}{(3/2)_s\,s!}\,2^{-s}.
\tag{2.3}
$$



Now expand the proposed right side:


$$
\left(1+z+\frac{z^2}{2}\right)^{-N}
=
\sum_{q\ge0}\frac{(-1)^q(N)_q}{q!}
\left(z+\frac{z^2}{2}\right)^q.
$$


Therefore


$$
m![z^m]\left(1+z+\frac{z^2}{2}\right)^{-N}
=
m!\sum_{\ell=0}^{\lfloor m/2\rfloor}
\frac{(-1)^{m-\ell}(N)_{m-\ell}}
{(m-2\ell)!\,\ell!\,2^\ell}.
\tag{2.4}
$$



For $m=2r$, substitute $\ell=r-s$ in (2.4), factor out


$$
(-1)^r\frac{(2r)!}{2^r r!}(N)_r,
$$


and use


$$
(2s)!=4^s s!(1/2)_s.
$$


The remaining finite sum is exactly (2.2).

For $m=2r+1$, the same substitution, with


$$
(2s+1)!=4^s s!(3/2)_s,
$$


gives (2.3). This proves every coefficient of (2.1). ∎

### Nonvanishing of the normalizing coefficient

At $j=a$, the central sum has only its $s=0$ term. Hence


$$
B_N=
\left(\prod_{t=1}^{a}(-2a+2t-1)\right)
(-a)_{\underline a}\ne0.
\tag{2.5}
$$


Thus the support result below is not caused by a zero normalizing constant.

---

## 3. Exact endpoint cancellation and the complete high-sector equation

Let


$$
E_d(x)=\binom xd,\qquad
\mathscr J E_d=E_{d+1},\qquad
\mathcal L_bE_d=\binom b{d+1}.
$$


The suffix identity is


$$
\mathscr S_b=-\mathscr J+E_0\mathcal L_b.
$$



For $v\ge1$, telescoping gives


$$
\mathscr S_b^vP
=
(-\mathscr J)^vP+
\sum_{a=0}^{v-1}
(-1)^aE_a\,\mathcal L_b\mathscr S_b^{v-1-a}P.
\tag{3.1}
$$



Insert this into the complete order-$s$ contact formula. The bulk term on $E_d$ is


$$
(-1)^s\binom{n+d+s}{s}E_{d+s}.
$$


For endpoint output degree $e<s$, all summands have the same endpoint moment. Vandermonde therefore gives


$$
\boxed{
[E_e]R_sP
=
(-1)^e\binom{n+e}{s}
\mathcal L_b\mathscr S_b^{s-1-e}P.
}
\tag{3.2}
$$



At $n=-N$, if $e\ge N$ and $s>e$, then


$$
\binom{e-N}{s}=0.
$$


Thus **every endpoint injection into degrees $e\ge N$ vanishes exactly**, for every endpoint $b$.

Bulk transport cannot cross from below $N$ into that sector either: an output $N+m$ from an input below $N$ has $s>m$, so its multiplier $\binom ms$ is zero.

Consequently the high sector is genuinely closed.

The complete symbol is


$$
1+\sum_{s\ge1}\lambda_s\frac{z^s}{s!}
=
\left(1-z+\frac{z^2}{2}\right)^{-N},
\tag{3.3}
$$


because $1+2U=(1-z+z^2/2)^2$ and $h=-N/2$.

Writing $g_i=(-1)^iF_i$, the high-sector equation is therefore


$$
p_{N+m}
+
\sum_{s=1}^{m}(-1)^s\lambda_s\binom ms p_{N+m-s}
=
g_{N+m}.
\tag{3.4}
$$



This derivation retains all endpoint moments before proving their cancellation. No endpoint term is discarded by a valuation estimate.

---

## 4. General high-sector truncation law

At $n=-N$, the complete force becomes


$$
F_{N+m}
=
\sum_{r=0}^{m}
\binom{N+m}{N+r}\frac{m!}{r!}B_{N+r}.
\tag{4.1}
$$


All lower central indices vanish because their force product contains $n+N=0$.

Define


$$
G(t)=\sum_{m\ge0}\frac{g_{N+m}}{m!}t^m,
\qquad
Q(t)=\sum_{m\ge0}\frac{p_{N+m}}{m!}t^m.
$$


Here $N$ is even. The ordinary binomial transform in (4.1) gives


$$
G(t)
=
(1+t)^{-N-1}
\mathcal H_N\!\left(-\frac{t}{1+t}\right).
\tag{4.2}
$$


For example, this follows coefficientwise from


$$
\sum_{m\ge r}\binom{N+m}{N+r}x^m
=
\frac{x^r}{(1-x)^{N+r+1}}.
$$



By Theorem 1,


$$
G(t)
=
B_N
\frac{(1+t)^{N-1}}{(1+t+t^2/2)^N}.
\tag{4.3}
$$


On the other hand, (3.4) gives


$$
Q(t)=(1+t+t^2/2)^N G(t).
$$


Therefore


$$
\boxed{Q(t)=B_N(1+t)^{N-1}.}
\tag{4.4}
$$



### Theorem 2 — Entire high-sector support and coefficients

For every $a\ge1$, at $h=-a,\ n=-2a=-N$,


$$
\boxed{
p_{N+m}=B_N(N-1)_{\underline m}\qquad(m\ge0).
}
\tag{4.5}
$$


The high-sector support is exactly


$$
\boxed{N\le r\le2N-1.}
\tag{4.6}
$$


All coefficients in this interval are nonzero, and every coefficient $r\ge2N$ is zero.

These are formal-series identities derived from terminating rational central sums. Their application to the continued solution uses the supplied compatible contact construction; it does not require analytic convergence in a real variable.

For $N=190$, (4.5) proves the coordinator’s observed pattern for **all** $m\ge0$, including the entire zero tail. This is the new proof that extends beyond the receipt’s finite scope.

---

## 5. Coefficientwise local-factor hierarchy

On the parameter line


$$
n=64k+2,
$$


put $k=-c$, where $c\ge1$ is an integer. Then


$$
n=-(64c-2),\qquad h=-(32c-1).
$$


Theorem 2 applies with


$$
N_c=64c-2.
$$


Hence


$$
\boxed{
p_r^{*}(-c)=0\qquad(r\ge128c-4).
}
\tag{5.1}
$$



Define


$$
J_r=\left\lfloor\frac{r+4}{128}\right\rfloor.
$$


Thus $p_r^*$ has all the roots


$$
-1,-2,\ldots,-J_r.
$$



### Conditional quantitative consequence

Assume the pending all-coefficient Lipschitz theorem (1.1). Comparing $k$ with each $-c$ gives


$$
v_2(p_r^*(k))\ge v_2(k+c)+3
\qquad(1\le c\le J_r).
$$


Therefore


$$
\boxed{
v_2(p_r^*(k))
\ge3+\max_{1\le c\le J_r}v_2(k+c).
}
\tag{5.2}
$$



This conclusion is uniform in the actual original index $u$; it is not restricted to a single previously reached cylinder.

### What the hierarchy does not prove

Neither continuity nor the stated Lipschitz estimate alone proves


$$
p_r^*(k)\in
\left(\prod_{c=1}^{J_r}(k+c)\right)\mathbb Z_2
$$


with an integral quotient.

That assertion requires quantitative higher divided differences or a suitable analytic coefficient norm. Repeatedly dividing a Lipschitz function by distinct linear factors does not preserve the same Lipschitz constant automatically.

The next section obtains a useful product-denominator bound without making this unjustified step.

---

## 6. A consecutive-product lemma pays all deep local factors simultaneously

### Lemma 3 — Product valuation after removal of a deepest factor

For $L\ge1$ consecutive nonzero integers


$$
x+1,\ldots,x+L,
$$


let


$$
M=\max_{1\le c\le L}v_2(x+c).
$$


Then


$$
\boxed{
\sum_{c=1}^{L}v_2(x+c)-M
\le v_2((L-1)!).
}
\tag{6.1}
$$



### Proof

Choose a factor attaining $M$. For $1\le a\le M$, removing that factor leaves at most


$$
\left\lceil\frac L{2^a}\right\rceil-1
=
\left\lfloor\frac{L-1}{2^a}\right\rfloor
$$


multiples of $2^a$. For $a>M$, there are none. Summing these counts over $a$ gives (6.1). ∎

Combining (5.2) and (6.1) yields the following pointwise, division-safe hierarchy:


$$
\boxed{
v_2\!\left(
\frac{p_r^*(k)}{\prod_{c=1}^{L}(k+c)}
\right)
\ge3-v_2((L-1)!)
\qquad(1\le L\le J_r).
}
\tag{6.2}
$$



This is weaker than an integral product quotient, but stronger than a collection of unrelated single-root statements. Its loss depends only on the number of shifts, not on the depth of the actual parameter’s proximity to any root.

---

## 7. Entire positive high-shift groups in the actual reconstruction

For a complete retained Newton polynomial, define


$$
F_s(x;2n)
=
\binom{2n+s-1}{s}
\sum_{r\ge s}p_r\binom{x}{r-s},
$$


and


$$
U_s(x)
=
F_s(x)+xF_s(x-1)+xF_{s+1}(x-1).
\tag{7.1}
$$


All sums are finite at a retained precision. For the complete solution, their interpretation is through the compatible integral reconstruction.

Fix an actual original index and an actual integer coordinate $j<b$. For $s\ge0$, set


$$
c_s=\left\lfloor\frac{s+4}{128}\right\rfloor.
$$


Every coefficient occurring in $U_s(j)$ has index $r\ge s$. All the binomial multipliers in (7.1) are integral at the actual parameters. Consequently, if $c_s\ge1$, (5.2) gives


$$
\boxed{
v_2(U_s(j))
\ge
3+\max_{1\le c\le c_s}v_2(k+c).
}
\tag{7.2}
$$


This includes all three reconstruction terms, not only the $j=0$ contribution.

Now write


$$
j=128t+\rho,\qquad d=D-t,\qquad K=k+d,
$$


and retain the exact stripping indices


$$
a_0=\left\lfloor\frac{84-\rho}{128}\right\rfloor,\qquad
l_0=\left\lfloor\frac{80-\rho-s}{128}\right\rfloor.
$$


For $s\ge0$,


$$
a_0\in\{-1,0\},\qquad l_0\le0.
$$



For a nonzero actual moment, the supplied exact quotient is


$$
\frac{\mathcal M_s(j)}{J_d}
=
2^{m_{\rho s}}u_{\rho s}
\frac{(K+a_0)!\,d!\,(k-1)!}
{(d+l_0)!\,(k+c_s)!\,(K-1)!},
\quad
J_d=\binom{k+d-1}{d},
\tag{7.3}
$$


with $u_{\rho s}$ an odd unit. Equivalently,


$$
\boxed{
\frac{\mathcal M_s(j)}{J_d}
=
2^{m_{\rho s}}u_{\rho s}
\frac{K^{\,a_0+1}\,d_{\underline{-l_0}}}
{k\prod_{c=1}^{c_s}(k+c)}.
}
\tag{7.4}
$$


Here $K^{a_0+1}$ means $K$ or $1$, respectively. No factorial with a negative actual argument is introduced: invalid moments are zero and are treated as zero.

The stripped low valuation $m_{\rho s}$ is nonnegative. It is the sum of the first seven factorial-floor carry contributions for the actual valid binomial.

Since actual $k$ is odd, Lemma 3 and (7.2) prove:

### Theorem 4 — Simultaneous high-shift bound

Conditional on the pending uniform Lipschitz theorem, every actual original index, every actual interior coordinate, and every $s\ge0$ with $c_s\ge1$ satisfy


$$
\boxed{
v_2\!\left(
U_s(j)\frac{\mathcal M_s(j)}{J_d}
\right)
\ge
m_{\rho s}
+v_2\!\left(K^{a_0+1}d_{\underline{-l_0}}\right)
+3-v_2((c_s-1)!).
}
\tag{7.5}
$$



The formula explicitly retains the actual finite numerator, the low stripping contribution, and the entire high denominator chain.

### Adding the actual weight

The higher kernel is


$$
\mathcal B_t=\binom Ct J_d.
$$


The exact weight stripping gives


$$
\frac{W_{128t+\rho}}{\binom Ct}\in\mathbb Z_2.
$$


For $\rho\le68$, its valuation is $v_2\binom{68}{\rho}$. For $\rho>68$, it is


$$
v_2\binom{196}{\rho}+v_2(C-t).
$$


Thus the complete order-$s$ raw first-column group


$$
A_{j,s}=W_jU_s(j)\mathcal M_s(j)
$$


obeys


$$
\boxed{
\begin{aligned}
v_2(A_{j,s}/\mathcal B_t)\ge{}&
v_2\!\left(W_j/\binom Ct\right)
+m_{\rho s}\\
&+v_2\!\left(K^{a_0+1}d_{\underline{-l_0}}\right)
+3-v_2((c_s-1)!).
\end{aligned}
}
\tag{7.6}
$$



This is a **same-index theorem for the entire positive high-shift family**. It does not replace the large kernels by reference kernels.

For any finite collection of shifts with $1\le c_s\le L$, summing complete groups preserves the coarse bound


$$
\boxed{
\sum_s A_{j,s}\in
2^{\,3-v_2((L-1)!)}\mathcal B_t\mathbb Z_2.
}
\tag{7.7}
$$



In particular, all arbitrarily deep root contacts have been paid simultaneously, at a stated factorial loss. The old fixed-$s$ unbounded-loss mechanism is no longer an obstruction to these force-weighted groups if the Lipschitz audit passes.

---

## 8. Why this still falls short of $N-2S$

The new bound has a precise limitation:


$$
v_2((c_s-1)!)\longrightarrow\infty
\qquad(s\to\infty).
$$


At raw precision $p$, the accepted degree envelope permits shifts of size comparable to $4p$, so this remaining loss can grow with $p$.

An absolute coefficient bound and a local-root bound do not automatically add. From


$$
v_2(p_r)\ge w_r,\qquad v_2(p_r)\ge M+3
$$


one obtains only


$$
v_2(p_r)\ge\max(w_r,M+3),
$$


not $w_r+M+3$. That distinction prevents the present proof from simply paying the factorial loss using the old absolute coefficient filtration.

Moreover, coordinate content alone would not prove the extra cancellation in


$$
N-2S(C,D)\in2^{2\mu+4}\mathbb Z_2.
$$


The complete target remains


$$
\boxed{
\sum_{j=0}^{b}(F_j^{[p]})^2-8S(C,D)
\equiv0\pmod{2^{2\mu+6}},
}
\tag{8.1}
$$


at sufficient raw precision, with every original coordinate retained.

### Concrete follow-on lemma

The sharpened coefficient target is now:

> **Weighted multiple-root lemma.** Prove, for $L\le J_r$, a bound of the form
> 

$$
> v_2\!\left(
> \frac{p_r^*(k)}{\prod_{c=1}^{L}(k+c)}
> \right)
> \ge \sigma(r,L),
>
$$


> where $\sigma(r,L)$ retains enough of the coefficient’s precision–degree weight to dominate the complete shift losses when $L=\lfloor(s+4)/128\rfloor$ and $r\ge s$.

A proof must control higher divided differences of the **complete force and contact inverse**, including endpoint feedback. The root identities alone do not supply it.

Alternatively, a complete grouped scalar identity could bypass termwise product division. Such an identity must evaluate (8.1), rather than merely regroup its summands.

---

## 9. Second force, finite endpoints, and primitive arithmetic remain unchanged

The present truncation theorem concerns the complete first force. It does not identify the second solution.

The second column still contains:

- its complete factorial/exterior force;
- all retained contact insertions;
- the logarithmic force, omitted only at precisions justified by its accepted whole-input estimate;
- the actual exterior $+1$.

The endpoint formulas remain


$$
2X_b=W_b\,b\theta_{b-1},
\qquad
4Y_b=W_b(1+b\eta_{b-1}).
$$


The norm and mixed contractions retain all full blocks, the shortened terminal block, and the separate coordinate $b$. Accepted nonvanishing


$$
N>0,\qquad H\ne0
$$


is not altered.

With the least actual clearer $d_B$,


$$
N_B=d_B[u,v],\qquad
A_B=N_{B,1}^{T}\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^{T}\Omega N_{B,2},
$$


the final primitive arithmetic is


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
}
\tag{9.1}
$$


The gcd includes every odd prime, and the primitive multiplier remains $d_B^2/g_B$.

The whole evaluated error remains


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n>0
\quad\text{eventually},
}
$$


with


$$
\log|\epsilon_n|
=
-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$


The required same-index bound on the **full primitive denominator** is not supplied by a binary high-sector theorem.

---

## 10. Bounded exact arithmetic worth inspecting next

No further calculation of $p_{380}^{*}(-3)$, and no precision-$139$ or $180$ path screen, is needed.

The general truncation law above is symbolic and requires no finite computation to establish its infinite scope. A bounded independent check can nevertheless audit its algebra and investigate the next, genuinely stronger lemma.

### A. Small-parameter exact audit of the general law

For


$$
N\in\{2,4,6,10\},\qquad h=-N/2,
$$


compute the complete terminating central coefficients


$$
B_N,\ldots,B_{3N}.
$$



**Expected verifiable outputs:**

1. Exact equality through degree $2N$ in
   

$$
\sum_{m=0}^{2N}\frac{B_{N+m}}{m!}z^m
   \equiv B_N(1+z+z^2/2)^{-N}\pmod{z^{2N+1}}.
$$


2. Independent high-sector triangular inversion.
3. Exact values
   

$$
p_{N+m}=B_N(N-1)_{\underline m}
   \qquad(0\le m\le2N).
$$


4. Exact inverse residuals.

These are algebra audits, not the proof of the general theorem.

### B. A bounded test of weighted multiple-root control

Take raw precision $p=128$, the complete precision-$p$ force and inverse, and the accepted degree bound $511$. Form exact rational-polynomial representatives of


$$
p_{252}^{[128]}(k),\qquad
p_{380}^{[128]}(k),\qquad
p_{508}^{[128]}(k).
$$


Their true continued coefficients have respectively at least two, three, and four roots in the hierarchy.

For each representative $f$, construct its Newton interpolation expansion at


$$
-1,-2,\ldots,-L,
\qquad L=2,3,4,
$$


retaining the interpolation remainder explicitly:


$$
f(k)=R_{L-1}(k)+
\left(\prod_{c=1}^{L}(k+c)\right)Q(k).
$$



**Expected verifiable outputs:**

- exact interpolation coefficients and their binary valuations;
- the exact polynomial remainder $R_{L-1}$, not silently set to zero;
- a certified coefficient-denominator bound for $Q$;
- the complete coefficient-valued inverse residual modulo $2^{128}$.

The finite representatives need not have exact zero values at the roots: their errors are controlled only modulo the retained precision. Preserving that remainder is essential. A passing result would establish only these bounded divided-difference estimates, while suggesting the quantitative statement needed for an all-depth proof.

---

## Final ledger

### New results established symbolically

1. The complete high-central generating function:
   

$$
\sum_{m\ge0}\frac{B_{N+m}(-N/2)}{m!}z^m
   =
   B_N(-N/2)(1+z+z^2/2)^{-N}.
$$



2. The entire negative-integer high-sector law:
   

$$
p_{N+m}=B_N(N-1)_{\underline m},
   \qquad p_r=0\quad(r\ge2N).
$$



3. The parameter-line root hierarchy:
   

$$
p_r^*(-c)=0\qquad(128c-4\le r).
$$



4. A consecutive-product valuation lemma that pays all but a stated factorial loss after one deepest local factor has been compensated.

### Conditional on the pending Lipschitz audit

Every positive high-shift group in the actual first-column reconstruction satisfies the explicit same-index bound (7.6). This controls all deep negative-integer denominator contacts simultaneously, not merely $s=380$.

### Exact remaining bottleneck

The remaining local issue is **weighted multiple-root divisibility**, or an equivalent complete grouped cancellation, strong enough to eliminate the growing factorial loss. Beyond it remain:

- the complete content-relative scalar $N-2S$;
- mixed relative alignment with the second full force;
- the actual finite endpoint and shortened block contributions;
- the final all-prime gcd;
- the same-index comparison of the actual primitive denominator with the whole nonzero error.



$$
\boxed{\text{The irrationality of }e+\pi\text{ remains unresolved.}}
$$


