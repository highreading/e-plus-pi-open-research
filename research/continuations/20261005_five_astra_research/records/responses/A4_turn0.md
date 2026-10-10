> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 research report: a multijet congruence theorem and a simultaneous-cancellation radius obstruction

## Summary

I do **not** obtain an unconditional determination of the irrationality of $e+\pi$.

I obtain two complementary results for a new multijet family:

1. **Exact triangular-response theorem.** In a high-order block lying below the first nonlinear interaction, endpoint-preserving integral Hurwitz jets act on the complete integer Taylor numerators by an integer matrix whose Smith normal form is $2I$. Consequently, arbitrary odd-modulus cancellation conditions at all Taylor truncations in that block can be solved simultaneously, using only exact rational arithmetic.

2. **Simultaneous-cancellation radius obstruction.** Such arithmetic solvability cannot be combined with a uniformly bounded puncture-avoidance perturbation on a fixed disk $r>2$ if one requires complete odd-denominator cancellation at two nearby even Taylor truncations of the **same modified pullback**. In particular, cancellation at both $n$ and $n+2$ forces an exponentially growing analytic norm:
   

$$
\|e^z+F(Q(z))\|_r
   \ge
   \frac{(r-1)r^n}
   {2^{v_2((n+2)!)}(1+r^{-2})}.
$$


   The right side tends to infinity for every fixed $r>2$.

The second result is not the single-jet proximity reduction in another notation. It uses the incompatibility of **two different exact primitive denominators for a common analytic function**, and does not assume or require a small-residue statement concerning $e+\pi$.

Neither result rederives an excluded HP or Gram family.

---

## 1. Setup and scope

Let


$$
F(w)=4\arctan\!\left(\frac{w}{2-w}\right),
\qquad
F'(w)=\frac{4}{(w-(1+i))(w-(1-i))}.
$$



Fix a real rational integral-Hurwitz polynomial $P$, meaning


$$
P^{(j)}(0)\in\mathbb Z\quad(j\ge0),
$$


with


$$
P(0)=0,\qquad P(1)=1.
$$



For the analytic conclusions, assume additionally that $P$ omits $1+i$ and $1-i$ on a neighborhood of the closed disk $|z|\le r$, where $r>2$. The branch of $F(P(z))$ starts at zero. On the real endpoint path its value at $1$ is $\pi$.

This is a conditional input on the base polynomial, not a new audit of the degree-81 certificate or the Schur-prefix existence theorem. The results below apply to **any** base polynomial satisfying these explicit hypotheses.

The new family is


$$
Q_{\boldsymbol K}(z)
=
P(z)+
\sum_{k=m}^{N}K_k\frac{z^k(1-z)}{k!},
\qquad K_k\in\mathbb Z,
\tag{1.1}
$$


with


$$
1\le m\le N<2m.
\tag{1.2}
$$



Each member fixes $0$ and $1$ and has integral Hurwitz derivatives. It is a multijet Taylor-pullback family, not one of the excluded raw, fixed-$b$, or fixed Gram centers.

For a pullback $Q$, define the **complete** Taylor endpoint and its integer numerator by


$$
H_Q(z)=e^z+F(Q(z)),\qquad
c_j(Q)=\sum_{\ell=0}^{j}\frac{H_Q^{(\ell)}(0)}{\ell!},
\qquad
Z_j(Q)=j!c_j(Q).
\tag{1.3}
$$



Where the branch is analytic through the endpoint,


$$
H_Q(1)=S=e+\pi.
$$



The actual reduced data are always


$$
g_j(Q)=\gcd(j!,|Z_j(Q)|),\qquad
q_j(Q)=\frac{j!}{g_j(Q)},\qquad
p_j(Q)=\frac{Z_j(Q)}{g_j(Q)}.
\tag{1.4}
$$


Thus


$$
c_j(Q)=\frac{p_j(Q)}{q_j(Q)},\qquad
q_j(Q)>0,\qquad
\gcd(p_j(Q),q_j(Q))=1,
\tag{1.5}
$$


and the whole primitive evaluated error is


$$
L_j(Q)=q_j(Q)S-p_j(Q)=q_j(Q)\bigl(S-c_j(Q)\bigr).
\tag{1.6}
$$



No coefficient clearer is being substituted for $q_j(Q)$.

---

## 2. Exact linear response of a high-order multijet block

### Theorem 1: integral triangular response and Smith form

For the domain (1.2), there is a lower-triangular integer matrix


$$
B=(B_{jk})_{m\le j,k\le N},
\qquad B_{jj}=1,
\tag{2.1}
$$


such that


$$
Z_j(Q_{\boldsymbol K})-Z_j(P)
=
2\sum_{k=m}^{j}B_{jk}K_k
\qquad(m\le j\le N).
\tag{2.2}
$$



Consequently:

- $B$ is unimodular over $\mathbb Z$;
- the response matrix $2B$ has Smith normal form $2I_{N-m+1}$;
- the possible numerator changes in this block are exactly
  

$$
2\mathbb Z^{N-m+1}.
  \tag{2.3}
$$



This is an exact statement about the **complete** Taylor numerator, including the exponential contribution.

### Proof

Put


$$
\Delta(z)=Q_{\boldsymbol K}(z)-P(z).
$$


Since $\Delta(z)=O(z^m)$, formal Taylor expansion gives


$$
F(P+\Delta)-F(P)
=
F'(P)\Delta+O(z^{2m}).
\tag{2.4}
$$


Because $N<2m$, the nonlinear terms make no contribution through order $N$.

Write


$$
T(z)=(1-z)F'(P(z))
=\sum_{h\ge0}t_hz^h.
\tag{2.5}
$$


Then through order $N$,


$$
F(Q_{\boldsymbol K})-F(P)
=
\sum_{k=m}^{N}\frac{K_k}{k!}z^kT(z).
\tag{2.6}
$$


Taking the complete Taylor sum through order $j$, evaluated at $1$, yields


$$
Z_j(Q_{\boldsymbol K})-Z_j(P)
=
\sum_{k=m}^{j}
K_k\frac{j!}{k!}
\sum_{h=0}^{j-k}t_h.
\tag{2.7}
$$



All Hurwitz derivatives of $F$ of positive order are even integers: the recurrence supplied in the source has initial values $2,2$, and preserves evenness. Therefore $F'/2$ has integral Hurwitz derivatives. Composition with the integral-Hurwitz polynomial $P$, followed by multiplication by $1-z$, preserves this property. Hence


$$
t_h=\frac{2u_h}{h!},\qquad u_h\in\mathbb Z,\qquad u_0=1.
\tag{2.8}
$$


Define


$$
B_{jk}
=
\sum_{h=0}^{j-k}\frac{j!}{k!h!}u_h
\quad(k\le j),
\qquad B_{jk}=0\quad(k>j).
\tag{2.9}
$$


Every summand is integral because $k+h\le j$:


$$
\frac{j!}{k!h!}
=
\binom jk\binom{j-k}{h}(j-k-h)!.
$$


Moreover $B_{jj}=u_0=1$. This proves (2.2).

An integer lower-unitriangular matrix has an integer inverse. Thus


$$
B^{-1}(2B)=2I,
$$


which proves the stated Smith form and image lattice. ∎

### Why the block condition matters

The assumption $N<2m$ removes all quadratic and higher interactions among the added jets. This is a genuine linear-response theorem, not a derivative calculation promoted to a global affine formula.

Outside this domain, a triangular polynomial response remains possible, but the displayed Smith-form conclusion has not been proved here.

---

## 3. Simultaneous odd-modulus steering

### Corollary 2: independent congruences at every truncation in the block

Let $d_j\ge1$ be arbitrary odd integers, and let $a_j\in\mathbb Z$, for $m\le j\le N<2m$. There exist integers $K_m,\ldots,K_N$ such that


$$
Z_j(Q_{\boldsymbol K})\equiv a_j\pmod{d_j}
\qquad(m\le j\le N).
\tag{3.1}
$$



They can be constructed recursively, with centered representatives satisfying


$$
|K_j|\le\frac{d_j-1}{2}.
\tag{3.2}
$$



### Proof

After $K_m,\ldots,K_{j-1}$ have been chosen, equation (2.2) reads


$$
Z_j(Q_{\boldsymbol K})
=
Z_j(P)+2\sum_{k=m}^{j-1}B_{jk}K_k+2K_j.
$$


As $2$ is invertible modulo $d_j$, there is a unique residue class for $K_j$ that enforces (3.1). Choose its centered representative. Later parameters do not change earlier rows. ∎

In particular, let


$$
f_j=v_2(j!),\qquad O_j=\frac{j!}{2^{f_j}}.
$$


Taking


$$
d_j=O_j,\qquad a_j=0
\tag{3.3}
$$


gives simultaneous cancellation of the full odd part of the factorial at every truncation in the block.

This arithmetic construction does not consult $S$. Its obstruction is analytic, as shown below.

### Explicit sufficient perturbation budget

For the centered choices,


$$
\|\Delta\|_r
\le
(1+r)\sum_{k=m}^{N}\frac{|K_k|r^k}{k!}
\le
\frac{1+r}{2}
\sum_{k=m}^{N}\frac{(d_k-1)r^k}{k!}.
\tag{3.4}
$$



Let the base puncture distance be


$$
\delta
=
\min_{\substack{|z|\le r\\ a\in\{1+i,1-i\}}}|P(z)-a|>0.
\tag{3.5}
$$


Any exact parameter vector satisfying


$$
\|\Delta\|_r<\delta
\tag{3.6}
$$


preserves puncture avoidance.

Formula (3.4) is only a sufficient estimate. The next theorem supplies a necessary obstruction that remains valid even when substantial cancellation between the perturbation monomials makes (3.4) very wasteful.

---

## 4. Exact parity and final denominators

The following elementary observation is needed to make the obstruction a statement about primitive denominators.

All derivatives of $F(Q)$ are even integers. If


$$
D_j=j!\sum_{\ell=0}^{j}\frac1{\ell!},
$$


then


$$
D_j=jD_{j-1}+1.
$$


Therefore $D_j$ is odd at every even $j\ge2$. Consequently,


$$
Z_j(Q)\ \text{is odd for every even }j\ge2.
\tag{4.1}
$$



For any such $j$, the final gcd $g_j(Q)$ is odd, so


$$
q_j(Q)
=
2^{f_j}\frac{O_j}{\gcd(O_j,Z_j(Q))}.
\tag{4.2}
$$


If $O_j\mid Z_j(Q)$, this becomes exactly


$$
g_j(Q)=O_j,\qquad
q_j(Q)=2^{f_j},\qquad
p_j(Q)=\frac{Z_j(Q)}{O_j}\in2\mathbb Z+1.
\tag{4.3}
$$



In particular, the endpoint center is nonzero. These are full reduction identities, not lower bounds derived from a written denominator.

---

## 5. A new simultaneous-cancellation radius tradeoff

### Theorem 3: two even endpoints force a large analytic norm

Let $Q$ be one integral-Hurwitz polynomial fixing $0,1$, and suppose $H_Q$ is analytic on a neighborhood of $|z|\le r$, with $r>1$. Put


$$
M_Q(r)=\max_{|z|\le r}|H_Q(z)|.
\tag{5.1}
$$



Let $2\le n<\ell$ be even integers. Suppose that the complete odd factorial denominators cancel at **both** truncations:


$$
O_n\mid Z_n(Q),\qquad O_\ell\mid Z_\ell(Q).
\tag{5.2}
$$


Then


$$
\boxed{
M_Q(r)
\ge
\frac{(r-1)r^n}
{2^{f_\ell}\bigl(1+r^{-(\ell-n)}\bigr)}.
}
\tag{5.3}
$$



This theorem does not require the high-block condition $N<2m$. It applies to arbitrary multijet perturbations satisfying its hypotheses.

### Proof

By (4.3),


$$
c_n(Q)=\frac{p_n}{2^{f_n}},
\qquad
c_\ell(Q)=\frac{p_\ell}{2^{f_\ell}},
\qquad p_n,p_\ell\text{ odd}.
$$


Because $n,\ell$ are distinct even integers,


$$
f_\ell>f_n.
$$


Thus


$$
c_\ell(Q)-c_n(Q)
=
\frac{p_\ell-2^{f_\ell-f_n}p_n}{2^{f_\ell}}.
\tag{5.4}
$$


Its numerator is odd and hence nonzero. In particular,


$$
|c_\ell(Q)-c_n(Q)|\ge2^{-f_\ell}.
\tag{5.5}
$$



On the other hand, Cauchy’s estimate for the coefficients of $H_Q$ gives the full Taylor-tail bound


$$
|H_Q(1)-c_j(Q)|
\le
M_Q(r)\sum_{k=j+1}^\infty r^{-k}
=
\frac{M_Q(r)}{r-1}r^{-j}.
\tag{5.6}
$$


Subtracting the two tails,


$$
|c_\ell(Q)-c_n(Q)|
\le
\frac{M_Q(r)}{r-1}
\bigl(r^{-n}+r^{-\ell}\bigr).
\tag{5.7}
$$


Combining (5.5) and (5.7) proves (5.3). ∎

### Adjacent even truncations

With $\ell=n+2$, the theorem gives


$$
\boxed{
M_Q(r)
\ge
\frac{(r-1)r^n}
{2^{v_2((n+2)!)}(1+r^{-2})}.
}
\tag{5.8}
$$


Since


$$
v_2((n+2)!)=n+2-s_2(n+2)\le n+1,
$$


one also has


$$
M_Q(r)
\ge
\frac{r-1}{2(1+r^{-2})}\left(\frac r2\right)^n.
\tag{5.9}
$$



Therefore, for every fixed $r>2$, no uniformly bounded family $H_{Q_n}$ can have complete odd cancellation at both $n$ and $n+2$ for arbitrarily large even $n$.

### Wider windows

If $\ell=n+d$, where $d\ge2$ is even, then the weaker but convenient estimate


$$
M_Q(r)
\ge
\frac{r-1}{1+r^{-d}}\,2^{-d}\left(\frac r2\right)^n
\tag{5.10}
$$


follows from $f_\ell\le\ell$.

Hence bounded analytic norm is impossible whenever


$$
n\log(r/2)-d\log2\longrightarrow+\infty.
\tag{5.11}
$$


In particular, the obstruction covers $d=o(n)$.

This is a quantitative separation requirement on simultaneous cancellation endpoints.

---

## 6. Conversion into an explicit puncture-avoidance budget

The norm obstruction can be connected directly to the size of the pullback perturbation, rather than left as a statement about an unspecified composition norm.

Assume


$$
Q=P+\Delta,\qquad \|\Delta\|_r=\varepsilon<\delta,
\tag{6.1}
$$


with $\delta$ as in (3.5), and put


$$
M_0(r)=\|e^z+F(P(z))\|_r.
$$



For $0\le t\le1$, every $P(z)+t\Delta(z)$ is at least $\delta-\varepsilon$ from either puncture. Consequently,


$$
|F'(P(z)+t\Delta(z))|
\le\frac4{(\delta-\varepsilon)^2}.
$$


Integration along this homotopy, with the branches normalized at $z=0$, gives


$$
\|F(Q)-F(P)\|_r
\le
\frac{4\varepsilon}{(\delta-\varepsilon)^2}.
\tag{6.2}
$$


Thus


$$
M_Q(r)
\le
M_0(r)+\frac{4\varepsilon}{(\delta-\varepsilon)^2}.
\tag{6.3}
$$



Combining with Theorem 3 proves the necessary budget


$$
\boxed{
M_0(r)+\frac{4\varepsilon}{(\delta-\varepsilon)^2}
\ge
\frac{(r-1)r^n}
{2^{f_\ell}(1+r^{-(\ell-n)})}.
}
\tag{6.4}
$$



For the particularly natural safety budget $\varepsilon\le\delta/2$,


$$
M_Q(r)\le M_0(r)+\frac8\delta.
\tag{6.5}
$$


Therefore simultaneous cancellation is impossible whenever


$$
\frac{(r-1)r^n}
{2^{f_\ell}(1+r^{-(\ell-n)})}
>
M_0(r)+\frac8\delta.
\tag{6.6}
$$



For $\ell=n+2$ and fixed $r>2$, this fails beyond a finite, explicitly bounded index once upper and lower bounds for $M_0(r)$ and $\delta$ are supplied.

**Crucially, (6.6) excludes every parameter vector inside the stated norm budget—not merely the recursively centered vector from Corollary 2.** Large cancellations between parameters do not circumvent it.

---

## 7. Partial cancellation and nonvanishing

There is also a useful version that retains uncancelled odd factors.

For any two distinct even indices $n<\ell$, write the actual reduced denominators as


$$
q_n=2^{f_n}b_n,\qquad q_\ell=2^{f_\ell}b_\ell,
\qquad b_n,b_\ell\text{ odd}.
\tag{7.1}
$$


By (4.2),


$$
b_j=\frac{O_j}{\gcd(O_j,Z_j(Q))}.
\tag{7.2}
$$



The centers cannot be equal: their reduced denominators have different dyadic valuations. Hence


$$
|c_\ell-c_n|
\ge
\frac1{\operatorname{lcm}(q_n,q_\ell)}
=
\frac1{2^{f_\ell}\operatorname{lcm}(b_n,b_\ell)}.
\tag{7.3}
$$


The same tail argument proves


$$
\boxed{
\operatorname{lcm}(b_n,b_\ell)
\ge
\frac{(r-1)r^n}
{M_Q(r)\,2^{f_\ell}(1+r^{-(\ell-n)})}.
}
\tag{7.4}
$$



Thus, under bounded analytic norm on $r>2$, nearby even truncations must collectively retain exponentially large odd denominator content. Full cancellation is the special case $b_n=b_\ell=1$.

This gives a multijet **radius/remaining-denominator tradeoff**, not just a failure of one chosen congruence algorithm.

### Whole evaluated error and nonvanishing

The exact errors remain


$$
L_j=q_jS-p_j.
$$


Because $c_n\ne c_\ell$, they cannot both vanish. More quantitatively, (7.3) implies


$$
\max\!\left(
\frac{|L_n|}{q_n},
\frac{|L_\ell|}{q_\ell}
\right)
\ge
\frac1{2\,\operatorname{lcm}(q_n,q_\ell)}.
\tag{7.5}
$$



This proves nonvanishing of at least one member of each pair, unconditionally. It does **not** prove that every individual error is nonzero, and does not supply a shrinking nonzero subsequence.

---

## 8. What this resolves—and what it does not

### Resolved

The simultaneous arithmetic steering problem in a high-order linear block has no hidden odd-prime rank obstruction. Its complete response lattice is exactly $2\mathbb Z^t$.

However, increasing the number of endpoint-preserving jets does not automatically buy a favorable simultaneous analytic construction. If a common pullback cancels the full odd denominator at two nearby even truncations, its analytic norm must grow at least on the scale $(r/2)^n$. A fixed positive puncture margin and a fixed small perturbation budget forbid this.

The obstruction is independent of:

- any assumption about the irrationality of $S$;
- distribution of binary digits of $S$;
- a conjectural small-residue estimate;
- asymptotics of an excluded HP center;
- a finite search over parameter vectors.

### Not resolved

The theorem does not exclude:

1. cancellation at only one truncation per modified polynomial;
2. simultaneous cancellation at widely separated truncations outside (5.11);
3. partial cancellation retaining odd factors large enough to satisfy (7.4);
4. pullbacks whose puncture distance degenerates with the index;
5. a different approximation functional, rather than ordinary Taylor truncation.

For the single-endpoint multijet problem, the exact triangular lattice provides arithmetic freedom, but a favorable real error still requires an independent quantitative approximation theorem. The lattice rank alone cannot provide it.

---

## Final required ledger

### (1) New result and proof status

**Proved here, author-level and not independently reviewed:**

- The high-block multijet response matrix has Smith normal form $2I$, with an explicit integer formula and the exact domain $m\le N<2m$.
- Arbitrary odd-modulus conditions on the complete Taylor numerators can be solved simultaneously in that block.
- Complete odd cancellation at two nearby even truncations of one pullback forces the analytic lower bound (5.3).
- Under an explicit puncture-preserving perturbation budget, (6.4) gives a necessary cost, and (6.6) gives an eventual exclusion on every fixed disk $r>2$.
- Partial cancellation must retain the actual odd denominator content required by (7.4).

No finite evidence is used to prove these infinite statements.

### (2) Exact remaining bottleneck

A successful route still needs a construction producing infinitely many **nonzero** whole primitive errors


$$
q_n(e+\pi)-p_n\longrightarrow0,
$$


with the actual final gcd retained.

For this multijet Taylor route, simultaneous cancellation at nearby truncations cannot achieve that through a uniformly bounded disk-$r>2$ perturbation. The remaining one-endpoint or widely separated-endpoint problem requires a new arithmetic–analytic approximation estimate, not merely simultaneous congruence solvability.

### (3) Computation request

**None is necessary to decide the lemmas proved above.** A numerical cutoff for a chosen base polynomial would require certified values of its puncture margin $\delta$ and composition bound $M_0(r)$, but would only specialize the proved obstruction; it would not decide irrationality of $e+\pi$.
