> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 Turn 6 — Arithmetic scale, actual primitive normalization, and a finite-word obstruction to coordinate alignment

## Abstract

The global objective remains unresolved: neither the supplied work nor the results below prove rationality or irrationality of $e+\pi$.

The fixed normalized-tail issue is treated as closed. I do not repeat its proof or any of the closed low-row calculations.

This report makes two substantive advances.

1. **The content parameter has an explicit logarithmic bound in the original index.** If
   

$$
E(u)=249005515+574312172u,\qquad b=3^{E(u)},\qquad n=2001b,
$$


   then
   

$$
\boxed{
   c+2\le v_{29}\binom{n+2}{b}
   \le \left\lfloor\log_{29}(n+2)\right\rfloor.
   }
$$


   Consequently, a gain consisting only of a fixed multiple of $c$ contributes at most a polynomial factor in $n$. This is not a bound on $v_{29}(g_B)$. The actual scalar gcd can also contain norm cancellation, mixed-product cancellation, weighted-column contents, and factors already present in the actual clearer.

2. **The strong coordinate target has a new, explicit finite-word obstruction.** Its compatibility with the finite reconstruction lattice can be tested using only a short segment adjacent to the *actual physical terminal*, factorial valuations, and explicitly truncated rising-factorial square sums. The test is valid at every precision. Its potentially obstructing rows lie within
   

$$
O(\log b)
$$


   positions of the terminal—not within a fixed low-row guard. If the test fails, **no complete second force having the certified original source denominator can satisfy the coordinate target**. This is an obstruction, not a replacement source or an evaluation of an unknown contact pairing.

The obstruction does not, by itself, produce an original-family counterexample: the required comparison with the actual $K=c+4+\nu$ has not been evaluated at an original index. Nor does it obstruct the weaker scalar alignment automatically. Thus it gives a concrete way to reject the unnecessarily strong target, but does not establish the desired all-depth scalar invariant.

The exact remaining bottlenecks are:

- an evaluated relation for the complete original scalar
  

$$
\bar Z^T(6PY-29\bar Z)
$$


  at the actual depth and whole original word;
- an all-prime estimate for the actual primitive denominator, compared with the nonzero whole error on the same infinite original indices.

---

## 1. Original objects and accepted scope

Throughout,


$$
p=29,\qquad
b=3^{249005515+574312172u},\qquad n=2001b,
$$


where


$$
u\ge0,\qquad u\equiv2\pmod{p^9}.
$$



The domains remain exactly:

- contact coordinates $0\le j<b$;
- recurrence source rows $1\le i\le b-2$;
- reconstructed coordinates $0\le j\le b$.

Set


$$
N=n+2,\qquad W_j=\binom Nj,
$$


and


$$
(\mathcal R\theta)_j=W_j(j\theta_{j-1}-\theta_j),
\qquad \theta_{-1}=\theta_b=0.
$$


Write


$$
L=\mathcal RA^{-1}.
$$



The actual columns are


$$
Z_w=Lf^0,\qquad
Y=L\mathbf r+W_be_b.
$$


The complete first force is


$$
f_i^0=\frac{(n+i)!}{n!}J_i(n),\qquad
J_i(n)=[z^n](1+2z+2z^2)^n(1+z)^i.
$$


With the retained unit


$$
C_n=f_0^0\in\mathbb Z_p^\times,
$$


put


$$
\bar f=f^0/C_n,\qquad \bar Z=Z_w/C_n.
$$



The complete second force remains


$$
\mathbf r=A_{IE}z+\frac{h^F}{b!},
\qquad z_h=\frac{(b+h)!}{b!}.
$$


In particular, its initial charges are the original quantities


$$
r_i=
\sum_s a_s(n)(n+i)_{\underline s}
\left(T_{2n+i-s}+\frac{L_{2n+i-s}}{b!}\right),
\qquad i=0,1,
$$


and every recurrence source


$$
\mathcal H_i=
\sum_s a_s(n+1)(n+i)_{\underline s}
\binom{2n+i-s+1}{b},
\qquad 1\le i\le b-2,
$$


is retained. Here


$$
a_s(n)=[z^s](1-z+z^2/2)^n,
$$




$$
T_m=\frac1{b!}\sum_{q=b}^m(m)_{\underline q},
$$


and


$$
L_m=mL_{m-1}+2(m-1)!u_{m-1},
\qquad
u_r=[z^r](1-z+z^2/2)^{-1}.
$$



Both finite returns and the physical terminal $W_be_b$ remain part of $Y$.

### 1.1 Results reused, not reopened

At their stated retained-source scope, I use:

- the complete finite inverse and return identities;
- $p$-integrality of $A^{-1}$, as used in its retained reduction modulo $p$;
- the exact exterior factorial filtration and symbol cutoff;
- all-depth Cartier closure for the actual first source;
- the original-family unit theorem for $C_n$;
- the unbounded-content theorem;
- the signed whole-error theorem;
- the exact terminal normal vector, its unit norm, and the unitriangular reconstruction;
- the now-closed assertion
  

$$
V\in p\mathbb Z_p^{b+1}.
$$



The omitted full proofs of the archived theorems are not reconstructed here. Deductions using them retain that dependency.

The original split also remains unchanged:


$$
b=p^3B+5044,\qquad
j=\ell+p^3J<b,
$$


with upper endpoint $B$ for $\ell<5044$ and $B-1$ for $\ell\ge5044$. Nothing below replaces that finite domain by an arbitrary suffix.

---

## 2. An explicit original-index bound for $c$

Write


$$
Z_w=p^{c+2}x,\qquad x\text{ primitive at }p,
$$


and retain the terminal consequence


$$
c+2\le w,\qquad
w:=v_p(W_b)=v_p\binom{n+2}{b}.
$$



### Theorem 2.1 — Arithmetic scale of the content parameter

For every original index,


$$
\boxed{
c+2\le w\le M,\qquad
M:=\left\lfloor\log_p(n+2)\right\rfloor.
}
\tag{2.1}
$$


Equivalently,


$$
\boxed{
c\le
\left\lfloor
E(u)\log_p3+\log_p\!\left(2001+2\,3^{-E(u)}\right)
\right\rfloor-2.
}
\tag{2.2}
$$


In particular,


$$
c\le
\left\lfloor E(u)\log_p3+\log_p2003\right\rfloor-2.
\tag{2.3}
$$



#### Proof

Legendre’s formula gives


$$
w=
\sum_{k\ge1}
\left(
\left\lfloor\frac{N}{p^k}\right\rfloor
-\left\lfloor\frac b{p^k}\right\rfloor
-\left\lfloor\frac{N-b}{p^k}\right\rfloor
\right).
$$


Since $N=b+(N-b)$, each summand is either $0$ or $1$. All summands vanish for $p^k>N$. There are at most $M=\lfloor\log_pN\rfloor$ nonzero summands. Thus $w\le M$.

This is the factorial-valuation form of Kummer’s carry count; it includes the actual upper endpoint $N$.

Now


$$
N=2001\,3^{E(u)}+2
=3^{E(u)}\left(2001+2\,3^{-E(u)}\right).
$$


Combining this identity with $c+2\le w\le M$ proves (2.2). The weaker bound (2.3) follows from $3^{-E(u)}\le1$. ∎

### Corollary 2.2 — The content-square scale is polynomial

One has


$$
\boxed{
p^{2c+4}\le (n+2)^2.
}
\tag{2.4}
$$


More generally, for fixed $A,B$,


$$
p^{Ac+B}=\exp(O(\log n)).
\tag{2.5}
$$



Thus an improvement whose entire arithmetic contribution is an additional $p^{O(c)}$ common factor is subexponential in $n$.

This remains true on an original subsequence with $c\to\infty$. Unbounded content and logarithmic content growth are entirely compatible.

---

## 3. What this does—and does not—say about the actual gcd

It is essential not to identify first-column content with the full scalar gcd.

Retain the actual integer columns


$$
N_{B,1},\quad N_{B,2},
$$


their actual contents, and the least simultaneous clearer $d_B$. Define


$$
\omega_j=\frac{(n+2)!}{(n+2-j)!},\qquad
\Omega=\operatorname{diag}(\omega_0^2,\ldots,\omega_b^2),
$$




$$
A_B=N_{B,1}^{T}\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^{T}\Omega N_{B,2},
$$


and


$$
g_B=\gcd(A_B,|H_B|).
$$


The actual primitive integers are


$$
\boxed{
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
}
\tag{3.1}
$$



### 3.1 Exact content accounting at every prime

Let


$$
V_i=\operatorname{diag}(\omega_0,\ldots,\omega_b)N_{B,i},
$$


and write


$$
V_i=k_i v_i,
$$


where $k_i$ is the positive integer content of $V_i$ and $v_i$ is primitive over $\mathbb Z$. Put


$$
S=v_1^Tv_1,\qquad T=v_1^Tv_2.
$$


Then exactly


$$
A_B=k_1^2S,\qquad H_B=k_1k_2T,
$$


so


$$
\boxed{
g_B=k_1\gcd(k_1S,|k_2T|).
}
\tag{3.2}
$$



For a prime $\ell$, put


$$
\alpha_i=v_\ell(k_i),\qquad
\sigma=v_\ell(S),\qquad \chi=v_\ell(T),
$$


using $v_\ell(0)=+\infty$. Then


$$
\boxed{
v_\ell(g_B)=
\min\{2\alpha_1+\sigma,\ \alpha_1+\alpha_2+\chi\},
}
\tag{3.3}
$$


and


$$
\boxed{
v_\ell(q_n)=
\max\{\alpha_1-\alpha_2+\sigma-\chi,\ 0\}.
}
\tag{3.4}
$$



These are identities for the actual integer columns. They distinguish:

1. weighted-column content;
2. divisibility of a primitive norm;
3. divisibility of a primitive mixed product.

The unweighted contents of $N_{B,i}$ must likewise not be silently replaced by the weighted contents $k_i$.

### 3.2 The least simultaneous clearer remains separate

For the actual rational columns cleared by $d_B$, minimality implies


$$
\gcd\!\left(d_B,\operatorname{cont}(N_{B,1}),
                    \operatorname{cont}(N_{B,2})\right)=1.
\tag{3.5}
$$


Otherwise a common prime factor could be removed from the clearer and both integer columns.

This does **not** say that either column is individually primitive. It also does not remove common factors created by the weights $\omega_j$.

The actual primitive multiplier remains


$$
\boxed{d_B^2/g_B.}
\tag{3.6}
$$


Neither division by $C_n$ nor division by the $p$-adic unit $t^Tt$ changes this all-prime arithmetic.

### 3.3 Why no bound $v_p(g_B)=O(c)$ follows

For the normalized physical first column, write


$$
\bar Z=p^a\bar x,\qquad a=c+2,
$$


and


$$
\bar x^T\bar x=p^\nu\bar\eta,\qquad
\bar\eta\in\mathbb Z_p^\times.
$$


Then


$$
v_p(\bar Z^T\bar Z)=2a+\nu.
\tag{3.7}
$$



The content contribution $2a=2c+4$ is $O(\log n)$, but no theorem in the supplied material bounds $\nu$ by $O(c)$, or even by $o(n)$.

Moreover, if the desired scalar alignment holds,


$$
6\bar Z^TY-p\,\bar Z^T\bar Z
\in p^{2a+\nu+2}\mathbb Z_p,
\tag{3.8}
$$


then


$$
\boxed{
v_p(\bar Z^TY)=2a+\nu+1.
}
\tag{3.9}
$$


Indeed, (3.8) says


$$
6\bar Z^TY
=p^{2a+\nu+1}(\bar\eta+p\xi)
$$


for some $\xi\in\mathbb Z_p$, and the bracket is a unit.

Thus the scalar alignment involves the full norm valuation, including $\nu$, not only the content valuation.

Equation (3.9) concerns the normalized contractions. Transferring it to $A_B,H_B$ still requires restoring the actual archived column scalings and clearer. Those factors may not be declared units merely because $C_n$ is a unit.

### Scale conclusion

The justified conclusion is therefore:

> **Improving the $c$-dependent part alone supplies at most a polynomial saving. A material exponential saving must come from additional arithmetic—possibly a large $\nu$-dependent scalar cancellation at $29$, possibly large factors already present in the actual contents and clearer, and/or common factors at other primes.**

It would be incorrect to conclude that $v_{29}(g_B)$ is bounded by $c$.

---

## 4. A useful scale dichotomy for logarithmic forcing

The retained logarithmic threshold is


$$
N_{\log}
=
2v_p(n!)-v_p(b!)
-\left\lfloor\log_p(2n+b-1)\right\rfloor.
$$


Since $n=2001b=69pb$,


$$
v_p(n!)\ge n/p=69b,
\qquad
v_p(b!)\le b/(p-1)=b/28.
$$


Consequently,


$$
\boxed{
N_{\log}\ge
\frac{3863}{28}b
-\left\lfloor\log_p(4003b-1)\right\rfloor.
}
\tag{4.1}
$$



The actual target precision is


$$
K=c+4+\nu=a+2+\nu.
$$


Theorem 2.1 gives


$$
\boxed{K\le M+2+\nu.}
\tag{4.2}
$$



Therefore, under the additional hypothesis $\nu=o(n)$,


$$
K=o(n)<N_{\log}
$$


eventually. In that conditional regime the archived logarithmic cutoff pays the logarithmic omission at the target precision.

This is **not** an unconditional omission. If a large $\nu$ is invoked as the mechanism producing a material denominator saving, the logarithmic threshold has to be checked again. The complete logarithmic force remains in every unconditional formula below.

---

## 5. The exact scalar target and the stronger coordinate proposal

Reuse the established terminal data


$$
t_j=\frac{(N-j)!}{(N-b)!},\qquad t_b=1,
$$




$$
\tau=t^Tt\equiv8\pmod p,
\qquad
P=I-\frac{tt^T}{\tau}.
$$


Then


$$
t^T\bar Z=0,\qquad t^TY=W_b,
$$


and


$$
\boxed{
\Delta=\bar Z^T(6PY-p\bar Z).
}
\tag{5.1}
$$



The scalar objective is


$$
\boxed{
\Delta\in p^{2a+\nu+2}\mathbb Z_p.
}
\tag{5.2}
$$


The stronger proposal is


$$
\boxed{
6PY-p\bar Z\in p^K\mathbb Z_p^{b+1},
\qquad K=a+2+\nu.
}
\tag{5.3}
$$


It implies (5.2), but it asks for substantially more.

For example, if (5.3) holds, then


$$
6PY=p\bar Z+p^Kv
$$


for some integral $v$. Hence


$$
36\|PY\|^2-p^2\|\bar Z\|^2
=
2p^{K+1}\bar Z^Tv+p^{2K}v^Tv.
$$


Since $\bar Z\in p^a$, this gives


$$
\boxed{
36\|PY\|^2-p^2\|\bar Z\|^2
\in p^{2a+\nu+3}\mathbb Z_p.
}
\tag{5.4}
$$


In particular,


$$
v_p(\|PY\|^2)=2a+\nu+2.
\tag{5.5}
$$



The scalar alignment (5.2) does not require this second-norm assertion. Thus compatibility of (5.3) should be tested, not presumed.

The next section supplies a different, explicitly computable obstruction to (5.3).

---

## 6. A terminal-lattice obstruction at arbitrary depth

### 6.1 The denominator hypothesis must be paid

Put


$$
\bar\theta=A^{-1}\bar f,\qquad
\psi=A^{-1}\mathbf r,\qquad
h=6\psi-p\bar\theta.
$$



To avoid silently assuming integrality of every complete second-source entry, define the original source-denominator exponent


$$
\boxed{
\delta=
\max\left\{0,\ -\min_{0\le i<b}v_p(r_i)\right\}.
}
\tag{6.1}
$$


This uses the **complete original** $\mathbf r$, not a leading dictionary.

Because $A^{-1}$ is $p$-integral and $\bar f$ is integral,


$$
\boxed{h\in p^{-\delta}\mathbb Z_p^b.}
\tag{6.2}
$$


If the complete original-force integrality certificate gives $\mathbf r\in\mathbb Z_p^b$, then $\delta=0$.

The printed initial-charge formulas do support integrality at their displayed scope. For example,


$$
T_m\in\mathbb Z\qquad(m\ge b),
$$


because


$$
\frac{(m)_{\underline q}}{b!}
=\binom mq\,\frac{q!}{b!}\in\mathbb Z.
$$


Also,


$$
L_m=2m!\sum_{k=1}^m\frac{u_{k-1}}k,
$$


so


$$
v_p(L_m/b!)
\ge v_p(m!)-v_p(b!)-\lfloor\log_pm\rfloor.
\tag{6.3}
$$


In the two initial charges, nonzero falling-factorial terms have $m\ge n$, making this bound positive.

However, checking the two initial values and the integral displayed $\mathcal H_i$ is not, by itself, a check that every division in an unprinted recurrence is paid. Definition (6.1) preserves that distinction. The theorem below is valid with the actual $\delta$, so it does not depend on an unverified assertion $\delta=0$.

This auxiliary denominator exponent does not replace $d_B$, any actual column content, or the final primitive normalization.

### 6.2 Explicit terminal quantities

For $1\le r\le b$, set


$$
j=b-r,\qquad q=N-b+1=2000b+3,
$$


and define


$$
F_r=\frac{b!}{(b-r)!},
\qquad
G_r=(q)^{\overline r}
=\frac{(N-b+r)!}{(N-b)!}.
$$


Write


$$
f_r=v_p(F_r),\qquad g_r=v_p(G_r).
\tag{6.4}
$$


Then


$$
t_{b-r}=G_r,
$$


and


$$
\boxed{
W_{b-r}=W_b\,\frac{F_r}{G_r}.
}
\tag{6.5}
$$


In particular,


$$
v_p(W_{b-r})=w+f_r-g_r.
\tag{6.6}
$$



Now define the integer


$$
\boxed{
T_j=\sum_{s=0}^{j}
\left((N-j+1)^{\overline s}\right)^2.
}
\tag{6.7}
$$


This sum will shortly be replaced by an explicit bounded modular recurrence.

The unitriangular coefficients from Turn 5 are


$$
C_{jk}=\frac{(N-k)!}{(N-j)!}.
$$


Since $t_k=C_{jk}t_j$,


$$
B_j=\sum_{k=0}^jC_{jk}t_k
=t_j\sum_{k=0}^jC_{jk}^2.
$$


Reversing $k=j-s$ gives


$$
\boxed{B_j=t_jT_j.}
\tag{6.8}
$$



Consequently the boundary term in the strong coordinate congruence has valuation


$$
\boxed{
v_p\!\left(\frac{6W_b}{\tau}B_{b-r}\right)
=w+g_r+v_p(T_{b-r}).
}
\tag{6.9}
$$


The only divisions here are by the proved units $6$ and $\tau$.

### Theorem 6.1 — Explicit finite-word obstruction to the coordinate target

Let


$$
t_r^{\mathrm{sq}}:=v_p(T_{b-r}).
$$


If, at an original index, there is an $r\in\{1,\ldots,b\}$ such that


$$
\boxed{
f_r>2g_r+t_r^{\mathrm{sq}}+\delta
}
\tag{6.10}
$$


and


$$
\boxed{
K>w+g_r+t_r^{\mathrm{sq}},
}
\tag{6.11}
$$


then the strong coordinate congruence (5.3) is false at that original index.

The conclusion holds for the complete original force, with both returns, logarithmic forcing and physical terminal included.

#### Proof

The established integral unitriangular transformation $E$ gives, for $j<b$,


$$
\bigl(E(6PY-p\bar Z)\bigr)_j
=
-W_jh_j-\frac{6W_b}{\tau}B_j.
\tag{6.12}
$$


Because $E$ and $E^{-1}$ are integral, (5.3) implies that every expression in (6.12) is divisible by $p^K$.

At $j=b-r$, (6.2) and (6.6) give


$$
v_p(W_jh_j)\ge w+f_r-g_r-\delta.
$$


By (6.10), this is strictly greater than


$$
w+g_r+t_r^{\mathrm{sq}},
$$


which is the exact valuation of the second term by (6.9). Therefore the two terms cannot cancel at that lowest valuation. Their sum has valuation exactly


$$
w+g_r+t_r^{\mathrm{sq}}<K,
$$


contradicting (5.3). ∎

### Interpretation

This is not merely the coordinate criterion from Turn 5 under a new name.

- It can exclude the criterion **without evaluating any contact coordinate $h_j$**.
- It uses factorial valuations and an explicitly computable terminal square sum.
- It applies to every source with the certified original denominator bound; hence omitted or restored source terms cannot repair the obstruction.
- It retains the physical terminal, which is precisely what creates the unequal-valuation obstruction.

It does **not** assert that a source satisfying the relaxed lattice conditions equals the original source. Passing the test is not a proof of alignment.

---

## 7. Only $O(\log b)$ terminal rows can obstruct

The preceding theorem still appears to allow $b$ tests. The next result removes that apparent size.

Put


$$
m=\lfloor\log_p b\rfloor,
\qquad
R=\left\lceil\frac{812}{27}(m+2)\right\rceil.
\tag{7.1}
$$



### Theorem 7.1 — Growing terminal cutoff

If $r\ge R$, then


$$
f_r\le2g_r.
\tag{7.2}
$$


Therefore condition (6.10) is impossible there, for every $\delta\ge0$. Every possible obstruction in Theorem 6.1 lies in


$$
\boxed{
1\le r<\min\{b+1,R\}.
}
\tag{7.3}
$$



#### Proof

The number of multiples of $p^k$ in any interval of $r$ consecutive integers is at most $r/p^k+1$. Since the factors of $F_r$ are at most $b$,


$$
f_r
\le\sum_{k=1}^{m}\left(\frac r{p^k}+1\right)
\le\frac r{p-1}+m
=\frac r{28}+m.
\tag{7.4}
$$



Every block of $r$ consecutive integers contains at least $\lfloor r/p\rfloor$ multiples of $p$. Thus


$$
g_r\ge\left\lfloor\frac r{29}\right\rfloor
\ge\frac r{29}-1.
$$


It follows that


$$
2g_r-f_r
\ge
\left(\frac2{29}-\frac1{28}\right)r-m-2
=
\frac{27}{812}r-m-2.
$$


This is nonnegative for $r\ge R$. Since $t_r^{\mathrm{sq}}\ge0$ and $\delta\ge0$, (6.10) cannot hold. ∎

This is a genuinely growing cutoff. It does not reuse a fixed low carry guard at increasing precision.

---

## 8. The square-sum obstruction is finitely evaluable, not an unevaluated sum

For a candidate $r<R$, put


$$
M_r=f_r-2g_r-\delta.
$$


If $M_r\le0$, that row cannot obstruct.

Suppose $M_r>0$. To decide (6.10), it suffices to compute


$$
T_{b-r}\pmod{p^{M_r}}.
$$



Set


$$
a_r=q+r=N-(b-r)+1.
$$


Define


$$
s_0=1,\qquad
s_{h+1}=s_h(a_r+h)^2\pmod{p^{M_r}}.
\tag{8.1}
$$


Then


$$
s_h=(a_r)^{\overline h\,2}\pmod{p^{M_r}}.
$$



Every product of $h$ consecutive integers is divisible by $h!$. Hence


$$
v_p(s_h)\ge2v_p(h!).
$$


In particular, if


$$
h\ge p\left\lceil\frac{M_r}{2}\right\rceil,
$$


then $s_h\equiv0\pmod{p^{M_r}}$, and all subsequent terms also vanish.

Therefore


$$
\boxed{
T_{b-r}\equiv
\sum_{h=0}^{H_r}s_h\pmod{p^{M_r}},
}
\tag{8.2}
$$


where


$$
\boxed{
H_r=
\min\left\{
b-r,\;
p\left\lceil\frac{M_r}{2}\right\rceil-1
\right\}.
}
\tag{8.3}
$$



The output has a precise interpretation:

- If the residue in (8.2) is zero, this row supplies no obstruction.
- If it is nonzero, its exact valuation
  

$$
t_r^{\mathrm{sq}}<M_r
$$


  is determined, and the strong target is impossible whenever
  

$$
K>w+g_r+t_r^{\mathrm{sq}}.
$$



All endpoints in (8.2)–(8.3) are the actual finite endpoints. No infinite replacement sum is used.

### A compact obstruction threshold

Define


$$
\mathcal O=
\left\{
1\le r<\min(b+1,R):
v_p(T_{b-r})<f_r-2g_r-\delta
\right\}.
$$


If $\mathcal O\ne\varnothing$, let


$$
\Lambda_{\mathrm{term}}
=
w+\min_{r\in\mathcal O}
\bigl(g_r+v_p(T_{b-r})\bigr).
\tag{8.4}
$$


Then


$$
\boxed{
\text{strong coordinate alignment requires }K\le\Lambda_{\mathrm{term}}.
}
\tag{8.5}
$$


If $\mathcal O=\varnothing$, this particular lattice test imposes no upper bound.

Equation (8.4), together with the cutoff and recurrence, is an evaluated finite procedure on the original word—not a formal operator definition.

---

## 9. What compatibility has and has not been settled

The strong proposal is now subject to two additional requirements:

1. the second-norm condition (5.4);
2. the explicit terminal-lattice bound (8.5).

Neither is required merely by scalar alignment.

### Proved conclusion

The coordinate proposal is **not automatically compatible** with the finite reconstruction lattice. Its compatibility has a nontrivial, explicitly decidable necessary condition involving the actual upper word.

### Not proved

I have not established an original index for which


$$
K>\Lambda_{\mathrm{term}}.
$$


Therefore this report does **not** claim an original-family counterexample to the strong proposal.

Nor have I proved that all original indices pass the test. That would require an additional theorem relating:

- the actual $c,\nu$;
- the whole-word terminal valuation $w$;
- the finite values in (8.2);
- the complete source denominator $\delta$.

Passing this necessary test would still leave the complete original-force alignment unproved.

Thus the requested universal compatibility decision is not fully closed. The advance is an explicit finite-word obstruction capable of deciding incompatibility at an original index without computing unknown contact coordinates.

### Why this does not yet evaluate the scalar

The scalar is


$$
\Delta=\bar Z^T(6PY-p\bar Z).
$$


A nonzero coordinate defect may be orthogonal to $\bar Z$ modulo the required power of $p$. Consequently, failure of (5.3) does not imply failure of (5.2).

This is exactly why the scalar target is more economical than the coordinate target. The next research step should not restore the stronger target by assumption after an obstruction is found.

---

## 10. The concrete remaining original-source lemma

The all-depth Cartier theorem already evaluates the paid first-source directions after the actual word is supplied. It should be reused, not reproved.

The outstanding task is to relate those evaluated directions to the complete second response.

A suitable next lemma is the following.

> **Complete original-word scalar lemma.**  
> On a specified infinite subsequence of the unchanged original indices, write
> 

$$
> \bar Z=p^a\bar x,\qquad
> \bar x^T\bar x=p^\nu\bar\eta,
> \qquad a=c+2.
>
$$


> Using the complete original initial charges, every recurrence source row, both finite returns, the logarithmic force whenever its threshold is reached, and the physical terminal, prove
> 

$$
> \boxed{
> 6\bar x^TY^{[K]}
> \equiv p^{K-1}\bar\eta\pmod{p^K},
> \qquad K=a+2+\nu.
> }
> \tag{10.1}
>
$$


> The proof must evaluate the accepting value on the whole actual word, rather than on an arbitrary unread suffix.

The retained error


$$
\bar Z^T(Y-Y^{[K]})\in p^{2a+\nu+2}\mathbb Z_p
$$


then transfers (10.1) to the whole scalar.

This lemma is still open. The new terminal test changes the strategy by identifying when its stronger coordinate substitute is impossible or unnecessarily demanding. It does not supply an accepting value for (10.1).

A genuine induction for (10.1) would need a joint state containing the complete second-force charges and returns as well as the first-source Cartier state. Closure of the first-source module alone does not prove that joint invariant.

---

## 11. Consequences for the actual denominator/error comparison

At the same original index, retain


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


so


$$
q_n(e+\pi)-p_n=-q_n\epsilon_n.
$$


The retained signed-error theorem gives eventual nonzero whole error and


$$
\log|\epsilon_n|
=-\lambda n+o(n),
\qquad
\lambda=
\left(2+\frac1{2001}\right)\log(1+\sqrt2)>0.
\tag{11.1}
$$



The actual denominator satisfies


$$
\boxed{
\log q_n
=
\sum_{\ell\ {\rm prime}}
\max\{v_\ell(A_B)-v_\ell(H_B),0\}\log\ell.
}
\tag{11.2}
$$


Thus


$$
\log|q_n\epsilon_n|
=\log q_n-\lambda n+o(n).
\tag{11.3}
$$



A sufficient irrationality criterion is


$$
\limsup\frac{\log q_n}{n}<\lambda
$$


on the same infinite original indices. More generally, what is needed is


$$
0<|q_n\epsilon_n|\longrightarrow0.
\tag{11.4}
$$



### Exactly what the scale theorem changes

Theorem 2.1 rules out the following inference:

> “Because $c\to\infty$, increasingly deep $c$-dependent local alignment must eventually beat an exponential error.”

That inference is invalid. A factor $p^{O(c)}$ has logarithm $O(\log n)$, whereas the whole-error exponent is linear in $n$.

The theorem does **not** rule out a useful local scalar theorem involving a large $\nu$, nor a useful all-prime gcd theorem. Those would be different sources of scale.

### Exactly what the obstruction theorem changes

Theorems 6.1–8.1 change no value of $q_n$, $g_B$, or $\epsilon_n$. They change which sufficient local lemma is worth pursuing:

- if $K>\Lambda_{\mathrm{term}}$, the strong coordinate route is unavailable at that index;
- the scalar route may nevertheless remain viable;
- even successful scalar alignment must still be transferred through the actual contents and clearer and combined with all-prime denominator control.

If $\log A_B$ contains a term larger than linear in $n$, that term must also be canceled in $\log g_B$ before the exponential error can be exploited. No $p^{O(c)}$ saving can perform such a cancellation.

---

## 12. Bounded exact arithmetic and verifiable outputs

No closed low-row audit, unit table, exterior solve, or tail calculation needs to be repeated.

### 12.1 A new finite original-word obstruction certificate

For a chosen original index, the mathematical inputs are:

1. an integer
   

$$
u\ge0,\qquad u\equiv2\pmod{p^9};
$$


2. the exact original integers
   

$$
b=3^{249005515+574312172u},\qquad n=2001b;
$$


3. a certified complete-source denominator exponent $\delta$, with
   

$$
p^\delta\mathbf r\in\mathbb Z_p^b;
$$


4. the actual values $a=c+2$ and $\nu$, if the aim is to decide the strong target at its actual $K=a+2+\nu$.

No suffix is chosen independently of $u$.

The bounded arithmetic is:

- compute
  

$$
w=v_p\binom{n+2}{b}
$$


  by the complete Legendre sum;
- compute $m,R$ from (7.1);
- for $1\le r<\min(b+1,R)$, compute $f_r,g_r$;
- when $M_r=f_r-2g_r-\delta>0$, use (8.1)–(8.3);
- compare the resulting thresholds with the actual $K$.

**Expected verifiable output:** either

- an obstruction certificate
  

$$
(u,r,\delta,a,\nu,w,f_r,g_r,t_r^{\mathrm{sq}})
$$


  satisfying the two strict inequalities (6.10)–(6.11), which disproves the strong coordinate target at that one original index; or
- a complete “no terminal-lattice obstruction” certificate for that index.

The second output does not prove coordinate alignment or scalar alignment.

The computation is finite and grows with the actual word. It is not claimed to be inexpensive at the first original index. For example, $u=2$ is a fully specified admissible input, but its enormous word makes a practical execution decision a separate matter for the coordinator.

### 12.2 A shorter certificate is sufficient for disproof

To disprove the strong target at one original index, it is unnecessary to enumerate every candidate $r$. A single certified $r<R$ with the required factorial valuations and modular square-sum value suffices.

This is the most economical possible use of the new obstruction.

### 12.3 What no such computation proves

A successful finite certificate would not prove:

- failure or success of the scalar target at other indices;
- an all-depth invariant;
- a bound for the all-prime gcd;
- an irrationality criterion on an infinite sequence.

Those remain separate obligations.

---

## 13. Proof-status ledger

| Statement | Status |
|---|---|
| The normalized tail satisfies $V\in29\mathbb Z_{29}^{b+1}$ | Closed retained result; not recomputed |
| $c+2\le v_{29}\binom{n+2}{b}\le\lfloor\log_{29}(n+2)\rfloor$ | **Proved on every original index** |
| A gain consisting only of $29^{O(c)}$ is polynomial in $n$ | **Proved limitation** |
| $v_{29}(g_B)=O(c)$ | **Not proved and not inferred** |
| Exact all-prime content formulas (3.2)–(3.4) | **Proved identities for the actual integer columns** |
| Scalar alignment forces normalized mixed valuation $2a+\nu+1$ | **Proved conditional consequence** |
| Strong coordinate alignment forces the second-norm congruence (5.4) | **Proved necessary condition** |
| Terminal-lattice obstruction (6.10)–(6.11) | **Proved at all depths with the certified actual source denominator** |
| Only $O(\log b)$ terminal rows can supply that obstruction | **Proved** |
| Square-sum test has the explicit finite evaluation (8.1)–(8.3) | **Proved** |
| An original index actually violates the strong target | Not established |
| Universal compatibility of the strong coordinate target | Not established |
| Complete original-word scalar alignment at actual $K$ | Open |
| All-prime actual denominator versus whole same-index error | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

## Conclusion

The principal new arithmetic conclusion is


$$
\boxed{
29^{\,2c+4}\le(n+2)^2.
}
$$


Unbounded first-column content does not, by itself, provide the asymptotic scale needed to beat the whole exponential error. Any material saving must be located in additional arithmetic and verified in the actual scalar gcd—not inferred from $c$.

The principal new structural conclusion is the explicit terminal obstruction


$$
\boxed{
f_r>2g_r+v_{29}(T_{b-r})+\delta,\quad
K>w+g_r+v_{29}(T_{b-r})
\ \Longrightarrow\
6PY-29\bar Z\notin29^K.
}
$$


Every possible witness lies within $O(\log b)$ rows of the actual terminal, and its square-sum value is determined by a bounded recurrence. This is a concrete finite-word test of the stronger coordinate route, not an unevaluated contact-coordinate reformulation.

No actual violating original index has yet been certified, and no all-depth scalar accepting value has been proved. The next exact calculation, if undertaken, should seek a single original terminal-obstruction certificate rather than repeat a fixed low-row audit. If that certificate rules out the coordinate route, the scalar lemma (10.1) remains the correct target.

Finally, even a proof of that scalar lemma would leave the indispensable all-prime comparison for


$$
q_n=\frac{A_B}{\gcd(A_B,|H_B|)}
$$


against the nonzero whole error on the same infinite original indices. The global irrationality problem remains open.
