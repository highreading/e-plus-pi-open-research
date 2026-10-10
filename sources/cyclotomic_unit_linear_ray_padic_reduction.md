> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The fixed $u_7^d$ ray: an exact $p$-adic reduction of the denominator-transfer gcd

## Status and scope

This note treats the one remaining arithmetic term in the accepted
denominator-transfer argument on the fixed linear ray



$$
\theta_d=u_7^d.
\tag{1}
$$



It proves three all-degree facts.

1. The factor $2\operatorname {lcm}(1,\ldots,d)$ in the transferred
   coefficient changes the logarithm of the selected gcd by only $O(d)$.
   Thus it may be removed without changing the desired
   $o(d\log d)$ question.
2. The remaining trace and the derangement number are outputs of an exact
   finite state modulo every integer $m$. An explicit reset period is
   given in terms of three unit orders.
3. At every prime $p\nmid20$, nested universal periods give a finite
   $p$-ary tree containing every possible common $p$-adic zero. For
   $p>d$, this is an exact criterion for factors of the reduced
   derangement denominator.

This is a rigorous reduction, **not** an all-degree gcd estimate. The
finite scan through $d=1000$ is a diagnostic only. In particular, this
note does not prove that the primitive rational forms tend to zero or to
infinity, and it proves nothing about the arithmetic nature of
$e+\pi$.

The exact generator is
<scripts/cyclotomic_unit_linear_ray_padic_reduction.py>, with output
<results/cyclotomic_unit_linear_ray_padic_reduction.json>.

## 1. Notation from the denominator-transfer theorem

Put



$$
D_d={!d},\qquad h_d=d!,\qquad
 \delta_d=\gcd(D_d,h_d),\qquad
 D_{0,d}=\frac{D_d}{\delta_d},
\tag{2}
$$



and



$$
P_d(X)=\sum_{j=0}^d(-1)^{d-j}\frac{d!}{j!}X^j\in\mathbb Z[X].
\tag{3}
$$



Let



$$
K=\mathbb Q(\zeta_{20})^+,\qquad
 \eta=(1+\zeta_5)^{-1},\qquad
 \bar\eta=1-\eta,
\tag{4}
$$



and let $u_7\in\mathcal O_K^\times$ be the real cyclotomic unit used in
the trace construction. Both $\eta$ and $\bar\eta$ are units in
$\mathbb Z[\zeta_5]$. Define



$$
\begin{aligned}
 X_d&=\operatorname {Tr}_{K/\mathbb Q}
       \bigl(u_7^dP_d(\eta)P_d(\bar\eta)\bigr),\\
 \ell_d&=\operatorname {lcm}(1,\ldots,d),\\
 C_d&=2\ell_dX_d.
 \end{aligned}
\tag{5}
$$



The product $P_d(\eta)P_d(\bar\eta)$ is fixed by complex conjugation
and lies in the quadratic real subfield of $K$. It is an algebraic
integer, so $X_d\in\mathbb Z$. The accepted denominator-transfer theorem
states that



$$
\frac{D_{0,d}}{\gcd(D_{0,d},C_d)}
\tag{6}
$$



divides the primitive coefficient of $e+\pi$ produced by this edge.
Consequently a bound



$$
\log\gcd(D_{0,d},C_d)=o(d\log d)
\tag{7}
$$



would be enough for the existing raw asymptotic argument. The purpose of
this note is to isolate (7) as sharply as possible.

## 2. Removing the lcm factor exactly

Define



$$
g_{X,d}=\gcd(D_{0,d},X_d),\qquad
 g_{C,d}=\gcd(D_{0,d},C_d).
\tag{8}
$$



### Proposition 1 (lcm separation)

For every $d\ge1$,



$$
\boxed{
 g_{X,d}\mid g_{C,d}\mid 2\ell_dg_{X,d}.}
\tag{9}
$$



In particular,



$$
0\le \log g_{C,d}-\log g_{X,d}
       \le\log(2\ell_d)=O(d),
\tag{10}
$$



and therefore



$$
\boxed{
 \log g_{C,d}=o(d\log d)
 \quad\Longleftrightarrow\quad
 \log g_{X,d}=o(d\log d).}
\tag{11}
$$



#### Proof

The first divisibility follows from $X_d\mid2\ell_dX_d$. For a prime
$p$, put



$$
a=v_p(D_{0,d}),\quad b=v_p(2\ell_d),\quad c=v_p(X_d).
$$



Then



$$
\min(a,b+c)\le \min(a,b)+\min(a,c).
$$



This is exactly the second divisibility in (9), prime by prime.

The elementary Chebyshev bound



$$
\log\operatorname {lcm}(1,\ldots,d)=\psi(d)=O(d)
\tag{12}
$$



proves (10). For completeness, one obtains
$\vartheta(2x)-\vartheta(x)\le2x\log2$ because the product of the primes
in $(x,2x]$ divides
${2\lfloor x\rfloor\choose\lfloor x\rfloor}<4^x$, first for integral
$x$, which is all that is needed. Summing over dyadic intervals gives
$\vartheta(x)=O(x)$, and then
$\psi(d)=\sum_{k\ge1}\vartheta(d^{1/k})=O(d)$. Equation (11) follows
from (10). ∎

The exact local identity behind Proposition 1 is also useful. Since



$$
v_p(D_{0,d})=\max\{v_p(D_d)-v_p(d!),0\}
\tag{13}
$$



and



$$
v_p(\ell_d)=\max\{j:p^j\le d\}=\lfloor\log_p d\rfloor,
$$



we have



$$
\boxed{
 \begin{aligned}
 v_p(g_{C,d})
   =\min\bigl(&\max\{v_p(D_d)-v_p(d!),0\},\\
              &v_p(2)+\lfloor\log_p d\rfloor+v_p(X_d)\bigr).
 \end{aligned}}
\tag{14}
$$



Thus the lcm contributes only the explicitly displayed local allowance.

## 3. The derangement state is periodic modulo its modulus

Set



$$
A_d=(-1)^dD_d.
\tag{15}
$$



The derangement recurrence becomes



$$
A_0=1,\qquad A_d=1-dA_{d-1}.
\tag{16}
$$



### Lemma 2 (exact period)

For every positive integer $m$,



$$
A_{d+m}\equiv A_d\pmod m
\tag{17}
$$



for all $d\ge0$.

#### Proof

At $d=m$, (16) gives $A_m\equiv1=A_0\pmod m$. If
$A_{m+r-1}\equiv A_{r-1}\pmod m$, then



$$
A_{m+r}=1-(m+r)A_{m+r-1}
       \equiv1-rA_{r-1}=A_r\pmod m.
$$



Induction on $r$ proves (17). ∎

For divisibility, the harmless sign in (15) may be ignored. Hence



$$
p^k\mid D_d
 \quad\Longleftrightarrow\quad
 A_{d\bmod p^k}\equiv0\pmod {p^k}.
\tag{18}
$$



The literature contains substantially finer fixed-prime Hensel analyses
of derangements. In particular, Piotr Miska's
[Arithmetic Properties of the Sequence of Derangements and its
Generalizations](https://arxiv.org/abs/1508.01987), Theorem 6, treats
$D_d/(d-1)$. That result is compatible with (17), but it neither
contains the moving trace $X_d$ nor supplies the uniform-in-$p$ estimate
needed in (11). Lemma 2 is proved here independently.

## 4. A finite algebraic state for the trace

The polynomial (3) satisfies the exact recurrence



$$
P_0(X)=1,\qquad
                  P_d(X)=X^d-dP_{d-1}(X).
\tag{19}
$$



Introduce the state



$$
\mathcal S_d=
 \bigl(A_d,\eta^d,\bar\eta^d,
       P_d(\eta),P_d(\bar\eta),u_7^d\bigr).
\tag{20}
$$



The first five entries lie in
$\mathbb Z\times\mathbb Z[\zeta_5]^4$, and the last lies in
$\mathcal O_K$. Reduction modulo $m$ is therefore well defined.

For a unit $\alpha$ in either quotient ring, write
$\operatorname {ord}_m(\alpha)$ for its finite multiplicative order.
Put



$$
L_m=\operatorname {lcm}\bigl(
 m,\operatorname {ord}_m(\eta),
 \operatorname {ord}_m(\bar\eta),
 \operatorname {ord}_m(u_7)\bigr).
\tag{21}
$$



### Proposition 3 (joint state reset)

For every $m\ge1$,



$$
\mathcal S_{d+L_m}\equiv\mathcal S_d\pmod m
\tag{22}
$$



for all $d\ge0$. Consequently



$$
X_{d+L_m}\equiv X_d\pmod m.
\tag{23}
$$



#### Proof

The definition of $L_m$ gives



$$
\eta^{L_m}\equiv\bar\eta^{L_m}\equiv1,
 \qquad u_7^{L_m}\equiv1\pmod m.
$$



Because $m\mid L_m$, (16) and (19) give, without any assumption on the
preceding state,



$$
\begin{aligned}
 A_{L_m}&=1-L_mA_{L_m-1}\equiv1=A_0,\\
 P_{L_m}(\eta)&=\eta^{L_m}-L_mP_{L_m-1}(\eta)
                   \equiv1=P_0(\eta),\\
 P_{L_m}(\bar\eta)&\equiv1=P_0(\bar\eta).
 \end{aligned}
$$



Thus $\mathcal S_{L_m}\equiv\mathcal S_0\pmod m$. After index $L_m$,
the coefficient $d$ in (16) and (19) repeats modulo $m$, while the
three unit-power recurrences have returned to their initial values.
Induction gives (22). The trace defining $X_d$ is an integral polynomial
function of this state, proving (23). ∎

This proposition turns every fixed congruence question into a finite one.
It is important, however, to preserve the factorial offset in $D_{0,d}$.
For every prime $p$ and $a\ge1$, (13) gives the exact criterion



$$
\boxed{
 p^a\mid g_{X,d}
 \quad\Longleftrightarrow\quad
 \begin{cases}
 p^{a+v_p(d!)}\mid A_d,\\
 p^a\mid X_d.
 \end{cases}}
\tag{24}
$$



The equal-level common-root condition



$$
p^a\mid A_d,\qquad p^a\mid X_d
\tag{25}
$$



is therefore a necessary envelope for (24), and is exact when $p>d$.
This distinction prevents a finite same-level root count from being
mistaken for a bound on $g_{X,d}$ at small primes.

## 5. Nested universal periods away from the conductor

Let $p\nmid20$ be prime and put



$$
f_p=\operatorname {ord}_{20}(p).
\tag{26}
$$



Reduction of the cyclotomic integer ring modulo $p$ is a product of
finite fields whose residue degrees divide $f_p$. Thus each of
$\eta,\bar\eta,u_7$ has order dividing $p^{f_p}-1$ modulo $p$.
For $k\ge1$, the kernel of reduction from level $p^k$ to level $p$
has exponent dividing $p^{k-1}$: if $z\equiv1\pmod p$, the binomial
theorem gives $z^{p^{k-1}}\equiv1\pmod {p^k}$. Hence all three unit
orders modulo $p^k$ divide



$$
p^{k-1}(p^{f_p}-1).
\tag{27}
$$



It follows from Proposition 3 that



$$
\boxed{
              T_{p,k}=p^k(p^{f_p}-1)}
\tag{28}
$$



is a simultaneous period of $A_d$ and $X_d$ modulo $p^k$. The extra
factor $p$ relative to (27) makes the recurrence coefficient $d$
repeat.

Define the finite common-root set



$$
\mathcal R_{p,k}=
 \{0\le r<T_{p,k}:A_r\equiv X_r\equiv0\pmod {p^k}\}.
\tag{29}
$$



Because $T_{p,k+1}=pT_{p,k}$, the sets form an exact $p$-ary lift tree:



$$
\boxed{
 \mathcal R_{p,k+1}=
 \{r+tT_{p,k}:r\in\mathcal R_{p,k},\ 0\le t<p,
      \ A_{r+tT_{p,k}}\equiv X_{r+tT_{p,k}}\equiv0
          \pmod {p^{k+1}}\}.}
\tag{30}
$$



This is not an asymptotic assertion: it is a finite exact test at every
level. It also shows exactly what remains to be controlled. A uniform
bound for $g_{X,d}$ would require a uniform restriction on the depth and
location of these simultaneous branches, together with the stronger
factorial-offset condition (24). Periodicity alone does not provide such
a restriction.

## 6. A particularly clean criterion for $p>d$

Write



$$
E_d(Y)=\sum_{j=0}^d\frac{Y^j}{j!}.
\tag{31}
$$



From (3),



$$
P_d(X)=(-1)^dd!E_d(-X),\qquad
 D_d=(-1)^dd!E_d(-1).
\tag{32}
$$



If $p>d$, every denominator in (31), as well as $d!$ and $\ell_d$,
is a unit modulo every power of $p$. Therefore, for $a\ge1$,



$$
\boxed{
 p^a\mid g_{X,d}
 \quad\Longleftrightarrow\quad
 \begin{cases}
 E_d(-1)\equiv0\pmod {p^a},\\
 \operatorname {Tr}_{K/\mathbb Q}
  \bigl(u_7^dE_d(-\eta)E_d(-\bar\eta)\bigr)
      \equiv0\pmod {p^a}.
 \end{cases}}
\tag{33}
$$



Congruences in (33) are interpreted in the integral quotient; this quotient
is unramified when $p\nmid20$.
Thus every large-prime contribution is exactly the intersection of two
explicit truncated-exponential zero conditions. No denominator clearing
remains in this formulation.

## 7. Why the accelerated moving-target theorem does not transfer

The accepted accelerated-ray argument takes
$\theta_d=u_7^{t_d}$ with



$$
\frac{t_d}{d\log d}\longrightarrow\infty.
\tag{34}
$$



Its moving-target gcd theorem requires the projective heights of the two
normalized coefficient polynomials to be $o(t_d)$. The coefficient
construction available here gives the bound $O(d\log d)$. Under (34)
this is sufficient. On the fixed linear ray $t_d=d$, it is not: the
available bound is not $o(d)$.

This is a failure to verify a hypothesis, not a theorem that cancellation
must occur. A fixed-target Subspace or $S$-unit theorem is also
inapplicable because the targets contain $P_d(\eta)$ and
$P_d(\bar\eta)$ and therefore move with $d$. Projective normalization
removes a common scalar but does not turn these moving coefficient ratios
into fixed targets. Consequently no Subspace-theorem conclusion is used
in this note.

## 8. Exact finite diagnostics

The companion script uses the integral recurrences (16) and (19), exact
cyclotomic arithmetic, and the integral trace pairing. Its default run
checks every $2\le d\le1000$. In that finite range it finds



$$
\gcd(D_{0,d},C_d)>1
 \quad\Longleftrightarrow\quad
 (d,\gcd)\in
 \{(4,3),(8,13),(12,11),(28,31),(199,277)\},
\tag{35}
$$



whereas after removing the lcm factor,



$$
\gcd(D_{0,d},X_d)>1
 \quad\Longleftrightarrow\quad
 (d,\gcd)\in
 \{(8,13),(28,31),(199,277)\}.
\tag{36}
$$



All three primes in (36) exceed $d$, and the script independently checks
both congruences in (33). The script also:

1. verifies (17) for a collection of prime-power and composite moduli;
2. computes the exact mod-$p$ orders of $\eta,\bar\eta,u_7$ at
   $p=3,7,11,13,31,277$;
3. checks the resulting state resets;
4. enumerates selected adjacent levels of the nested tree (30); and
5. verifies (9) and (14) in the full finite scan.

Equations (35)--(36) are not extrapolated. In fact, the level-one sets
$\mathcal R_{p,1}$ are already nonempty for several small primes. This
directly rules out the tempting but false shortcut that the two sequences
have no common roots modulo $p$.

## 9. Conclusion

The fixed linear edge has been reduced to the following precise local
problem:



$$
\boxed{
 \text{Bound }
 \sum_p\min\bigl(\max\{v_p(D_d)-v_p(d!),0\},v_p(X_d)\bigr)\log p
       =\log g_{X,d}.}
\tag{37}
$$



The lcm clearing costs only $O(d)$, and every local term in (37) is
decidable by the finite state of Proposition 3. Away from the conductor,
the potential terms lie on the explicit nested tree (30), with the exact
large-prime equations (33). What is still missing is a **uniform** bound
on the total depth and size of those branches as both $p$ and $d$
vary. Neither fixed-prime periodicity, the existing derangement Hensel
theory, nor the accelerated moving-target theorem supplies that bound.
