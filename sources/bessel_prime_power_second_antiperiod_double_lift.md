> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Prime-power second anti-periods and inherited index slopes

Checked: 2026-08-27 UTC.

## 1. Verdict

Let



$$
q_0=q_1=1,\qquad q_n=(4n-2)q_{n-1}+q_{n-2}.
\tag{1}
$$



Two uniform prime-power statements can be proved.

First, if $p$ is odd, $a\geq1$, and $M=p^a$, then



$$
\boxed{
 q_{n+2M}+2q_{n+M}+q_n
 \equiv 2p^{\,2a-1}q_n\pmod {p^{2a}} }
\tag{2}
$$



for every integer $n\geq0$.  Thus a root modulo $p^a$ has an exact
affine lift law all the way to modulus $p^{2a}$.

Second, define for every $n$



$$
\delta_{p^a}(n)=\frac{-q_{n+p^a}-q_n}{p^a}\pmod {p^a}.
\tag{3}
$$



For $a\geq2$, its reduction modulo $p$ satisfies



$$
\boxed{\delta_{p^a}(n)\equiv\delta_p(n)-q_n\pmod p.}
\tag{4}
$$



In particular, on every root modulo $p$,



$$
\boxed{\delta_{p^a}(n)\equiv\delta_p(n)\pmod p.}
\tag{5}
$$



Consequently, index-slope simplicity or singularity is inherited from the
first level.  Every ordinary root modulo $p$ has exactly one descendant
at every modulus $p^a$.  Every descendant of a singular root remains
singular and, at each one-exponent lift, either dies or has all $p$
children.

These results sharply reduce the possible branching, but they do not prove
a prime-power-height bound.  Singular base roots are not known to die for
every prime.  More importantly, even a unique ordinary branch can have an
exceptionally small integer truncation at a very deep level.  Nothing here
proves



$$
\max_{N\leq n<2N}\max_{p\leq C N\log N}
       v_p(q_n)\log p=o(N\log N).
\tag{6}
$$



Sections 7 and 8 give the exact density improvement and the remaining
index-height obstruction.  No polynomial-argument Hensel theorem is
silently substituted for an index-slope theorem.

## 2. Inputs and extension to all integer indices

We use the already proved odd anti-period congruence



$$
q_{n+M}\equiv-q_n\pmod M
\tag{7}
$$



for odd $M$.  The proof in

    sources/exponential_beta_bessel_period_congruence.md

starts at nonnegative indices.  Extend (1) backwards to all
$n\in\mathbb Z$.  Uniqueness in the recurrence gives



$$
\boxed{q_{-n-1}=-q_n}\qquad(n\in\mathbb Z).
\tag{8}
$$



It follows either by (8), or by running the same invertible recurrence
backwards modulo $M$, that (7) holds for every integer $n$.

For $a=1$, (2) is Theorem 3 of

    sources/bessel_denominator_zero_gap_smooth_radical_barrier.md

The next two sections prove the new prime-power case $a\geq2$.

## 3. The initial second difference at zero

Write



$$
A_{r,j}=\frac{(r+j)!}{j!(r-j)!},\qquad
 q_r=(-1)^r\sum_{j=0}^r(-1)^jA_{r,j},
\tag{9}
$$



and put



$$
D_n=q_{n+2M}+2q_{n+M}+q_n.
\tag{10}
$$



Since $M$ is odd, the $j=0$ terms cancel and



$$
D_0=\sum_{j=1}^{2M}(-1)^j
       \bigl(A_{2M,j}-2A_{M,j}\bigr),
\tag{11}
$$



where $A_{M,j}=0$ for $j>M$.

For $1\leq j<M$ and $c\in\{1,2\}$, pairing factors equidistant from
$cM$ gives the exact identity



$$
A_{cM,j}=(-1)^{j-1}cM(j-1)!
 \left(1+\frac{cM}{j}\right)
 \prod_{h=1}^{j-1}\left(1-\frac{c^2M^2}{h^2}\right).
\tag{12}
$$



Congruences involving the displayed rational factors are taken in
$\mathbb Q_p$; their product in (12) is the integer on the left.  Set



$$
R_c(j)=\prod_{h=1}^{j-1}
       \left(1-\frac{c^2M^2}{h^2}\right),\qquad
 b=\lfloor\log_p(j-1)\rfloor,
\tag{13}
$$



with $b=0$ when $j=1$.  Because $j<M=p^a$, every factor correction
has valuation at least $2a-2b\geq2$.  Hence



$$
R_c(j)\equiv1\pmod {p^{\,2a-2b}},\qquad
 R_2(j)-R_1(j)\equiv0\pmod {p^{\,2a-2b}}.
\tag{14}
$$



Subtracting twice the $c=1$ expression from the $c=2$ expression gives



$$
\begin{aligned}
 A_{2M,j}-2A_{M,j}
  ={}&(-1)^{j-1}2M(j-1)!
       \biggl\{R_2(j)-R_1(j)\\
     &\hspace{34mm}+\frac{M}{j}
       \bigl(2R_2(j)-R_1(j)\bigr)\biggr\}.
\end{aligned}
\tag{15}
$$



Two elementary valuation facts now isolate one term.

First,



$$
v_p((j-1)!)+a\geq2b.
\tag{16}
$$



For $b=0$ this is immediate.  For $b\geq1$, the factorial
$(j-1)!$ contains $p^b!$, so its valuation is at least
$(p^b-1)/(p-1)\geq b$, while $a\geq b+1$.  Thus the first term in
braces in (15), after multiplication by $2M(j-1)!$, is zero modulo
$p^{2a}$.

Second,



$$
v_p((j-1)!)<v_p(j)
 \quad\Longleftrightarrow\quad j=p.
\tag{17}
$$



Indeed, this is clear for $p\nmid j$.  If $v_p(j)=1$ and $j>p$,
then $(j-1)!$ already contains $p$.  If $v_p(j)=s\geq2$, then



$$
v_p((j-1)!)\geq v_p((p^s-1)!)
 =\frac{p^s-1}{p-1}-s\geq s
\tag{18}
$$



for odd $p$; the limiting case is $p=3,s=2$, where equality holds.
Consequently, the second term in braces in (15) is zero modulo $p^{2a}$
for every $j\neq p$.  The correction $2R_2-R_1-1$ has valuation at
least two, so it cannot alter this conclusion or the leading residue at
$j=p$.

At the unique exceptional index $j=p$, the outer sign in (11) and
Wilson's congruence give



$$
(-1)^p\bigl(A_{2M,p}-2A_{M,p}\bigr)
 \equiv-2p^{2a-1}(p-1)!
 \equiv2p^{2a-1}\pmod {p^{2a}}.
\tag{19}
$$



It remains to discard $M\leq j\leq2M$.  The integer identity



$$
A_{r,j}=j!\binom rj\binom{r+j}j
\tag{20}
$$



shows that every such term is divisible by $p^{2a}$, because



$$
v_p(j!)\geq v_p(M!)=\frac{p^a-1}{p-1}\geq2a
\tag{21}
$$



for odd $p$ and $a\geq2$.  Equations (11)--(21) prove



$$
\boxed{D_0\equiv2p^{2a-1}\pmod {p^{2a}}}.
\tag{22}
$$



## 4. A discrete Wronskian supplies the other initial value

Put $c_n=4n-2$.  Comparing the three shifted recurrences in (10) gives



$$
D_n-c_nD_{n-1}-D_{n-2}
 =8M\bigl(q_{n+2M-1}+q_{n+M-1}\bigr)
 \equiv0\pmod {M^2},
\tag{23}
$$



where (7) gives the last congruence.  Thus $D_n$ obeys the same
homogeneous recurrence as $q_n$, modulo $M^2$.

The second initial value is not assumed.  Define the discrete Wronskian



$$
W_n=D_nq_{n-1}-D_{n-1}q_n.
\tag{24}
$$



Equation (23) and the exact recurrence for $q_n$ imply



$$
W_n\equiv-W_{n-1}\pmod {M^2}.
\tag{25}
$$



Reflection (8) gives the exact symmetry



$$
D_{-2M-1-n}=-D_n.
\tag{26}
$$



At the two central indices, $D_{-M-1}=-D_{-M}$, and hence



$$
W_{-M}=D_{-M}(q_{-M-1}+q_{-M})
       =-D_{-M}(q_M+q_{M-1}).
\tag{27}
$$



Both factors on the right are divisible by $M$.  The first is a sum of
two adjacent anti-period pairs from (10); the second follows from
$q_M\equiv-1$ and $q_{M-1}\equiv1\pmod M$.  Therefore
$W_{-M}\equiv0\pmod {M^2}$.  Propagating (25) to $n=1$ yields



$$
0\equiv W_1=D_1q_0-D_0q_1=D_1-D_0\pmod {M^2}.
\tag{28}
$$



Now (22), (23), (28), and $q_0=q_1=1$ imply



$$
D_n\equiv D_0q_n
 \equiv2p^{2a-1}q_n\pmod {p^{2a}},
\tag{29}
$$



which proves (2).

## 5. Exact exponent-doubling and one-exponent lifts

Let $r\in\{0,\ldots,M-1\}$ satisfy $M\mid q_r$, and use the index
slope (3).  For $t\in\mathbb Z$, put
$B_t=(-1)^tq_{r+tM}$.  Every term is a root modulo $M$, so (2) makes
the second finite difference of $B_t$ zero modulo $M^2$.  Its first two
values give



$$
\boxed{(-1)^tq_{r+tM}
 \equiv q_r+tM\delta_M(r)\pmod {M^2}.}
\tag{30}
$$



The $M$ children $r+tM\pmod {M^2}$ are roots modulo $M^2$ exactly
when



$$
\frac{q_r}{M}+t\delta_M(r)\equiv0\pmod M.
\tag{31}
$$



If



$$
d_M(r)=\gcd(\delta_M(r),M),
\tag{32}
$$



the number of children is $d_M(r)$ when
$d_M(r)\mid q_r/M$, and zero otherwise.  Thus



$$
\boxed{
 R_{M^2}=\sum_{\substack{r\in\mathcal R_M\\
                         d_M(r)\mid q_r/M}}d_M(r), }
\tag{33}
$$



where
$\mathcal R_M=\{0\leq r<M:M\mid q_r\}$.

Reducing (30) only modulo $pM=p^{a+1}$ gives the exact one-exponent
law



$$
p^{a+1}\mid q_{r+tM}
 \quad\Longleftrightarrow\quad
 \frac{q_r}{M}+t\delta_M(r)\equiv0\pmod p,
\qquad 0\leq t<p.
\tag{34}
$$



It has one solution if $p\nmid\delta_M(r)$, and either zero or all $p$
solutions when $p\mid\delta_M(r)$.

## 6. The slope modulo $p$ is inherited from level one

For any odd multiple $L$ of $p$, define the integral sequence



$$
u_L(n)=\frac{q_{n+L}+q_n}{L}=-\delta_L(n).
\tag{35}
$$



Comparison of the recurrences at $n+L$ and $n$ gives



$$
u_L(n)=c_nu_L(n-1)+u_L(n-2)+4q_{n+L-1}.
\tag{36}
$$



Modulo $p$, the anti-period congruence makes the last term
$-4q_{n-1}$.  Hence, for $M=p^a$, the difference



$$
E_a(n)=u_M(n)-u_p(n)
\tag{37}
$$



obeys the homogeneous $q_n$-recurrence modulo $p$.

For completeness, its two initial values can be computed without an
unproved quotient-period assertion.  Let



$$
S=\sum_{h=0}^{p-2}h!,\qquad
 T=\sum_{j=2}^{p-2}(j+1)(j-2)!.
\tag{38}
$$



The prime-level calculation in the source cited in Section 2 gives



$$
u_p(0)\equiv S-2,\qquad u_p(1)\equiv T-5\pmod p.
\tag{39}
$$



For $a\geq2$, divide the factorial terms in (9) by $M$.  Modulo $p$,



$$
\frac{A_{M,j}}M\equiv(-1)^{j-1}(j-1)!
 \quad(1\leq j\leq p),
\tag{40}
$$



and all later terms vanish.  Wilson's congruence gives



$$
u_M(0)\equiv\sum_{h=0}^{p-1}h!\equiv S-1\pmod p.
\tag{41}
$$



For the other initial value, the $j=1$ term first gives
$(2-A_{M+1,1})/M\equiv-3$.  For $2\leq j\leq M+1$, write the full
numerator around its central factor:



$$
\frac{A_{M+1,j}}M
 =\frac{1}{j!}
   \prod_{\substack{2-j\leq h\leq j+1\\h\neq0}}(M+h).
\tag{42}
$$



For every offset in this range, $v_p(M+h)=v_p(h)$.  Indeed, this follows
from $v_p(h)<a$ unless $h=M$; the only possible nonzero multiple of
$M$ in the range is $h=M$, and then
$v_p(M+h)=v_p(2M)=a=v_p(h)$ because $p$ is odd.  The negative offsets
contribute the valuation of $(j-2)!$, while the positive offsets
contribute the valuation of $(j+1)!$.  Therefore



$$
v_p\left(\frac{A_{M+1,j}}M\right)
 =v_p((j-2)!)+v_p((j+1)!)-v_p(j!)
 =v_p((j-2)!)+v_p(j+1).
\tag{43}
$$



This also covers the endpoint $j=M+1$: its offsets run from $1-M$ to
$M+2$, and the preceding discussion explicitly accounts for the extra
offset $h=M$.  In particular, (43) is at least one whenever
$j\geq p+2$, because then $(j-2)!$ contains $p$.

It remains to calculate the unit cases.  For $2\leq j\leq p-2$, direct
reduction of (42) gives



$$
\frac{A_{M+1,j}}M
 \equiv
 \frac{(-1)^{j-2}(j-2)!(j+1)!}{j!}
 =(j+1)(-1)^{j-2}(j-2)!\pmod p.
\tag{44}
$$



At $j=p-1$, equation (43) has valuation one, so the residue is zero.
At $j=p$, cancel the factor $p$ in the positive product against the
one in $p!$.  Since



$$
\frac{M+p}{p}=1+p^{a-1}\equiv1\pmod p,
$$



the positive product divided by $p!$ is congruent to $1$, while the
negative product is
$(-1)^{p-2}(p-2)!\equiv-1\pmod p$.  Hence the residue is $-1$.
At $j=p+1$, the same cancellation makes the positive product divided by
$(p+1)!$ congruent to the remaining factor $M+p+2\equiv2$, while the
negative product is
$(-1)^{p-1}(p-1)!\equiv-1$.  Hence the residue is $-2$.
Altogether,



$$
\frac{A_{M+1,j}}M\equiv
 \begin{cases}
  (j+1)(-1)^{j-2}(j-2)!,&2\leq j\leq p-2,\\
  0,&j=p-1,\\
  -1,&j=p,\\
  -2,&j=p+1,\\
  0,&p+2\leq j\leq M+1
 \end{cases}
 \pmod p.
\tag{45}
$$



Substitution of the outer signs in (9) yields



$$
u_M(1)\equiv-3+T+1-2=T-4\pmod p.
\tag{46}
$$



For $p=3$, the empty ordinary ranges in (38) and (45) give the same result; it
can also be checked directly from $q_3,q_4,q_9,q_{10}$.

Equations (39), (41), and (46) say
$E_a(0)=E_a(1)=1$.  Since $q_0=q_1=1$, uniqueness in the homogeneous
recurrence gives



$$
u_{p^a}(n)-u_p(n)\equiv q_n\pmod p.
\tag{47}
$$



Negating (47) proves (4).

If $n=r+tp$, where $p\mid q_r$ and $0\leq r<p$, the first-level
affine law also gives



$$
\delta_p(n)\equiv(-1)^t\delta_p(r)\pmod p.
\tag{48}
$$



Combining (5) and (48), every prime-power root above $r$ has a unit
index slope exactly when $\delta_p(r)\neq0$.  No new singular branch can
appear above an ordinary root.

## 7. Uniform root-count consequence

Define the ordinary and singular first-level counts



$$
\begin{aligned}
 O_p&=\#\{0\leq r<p:p\mid q_r,\ \delta_p(r)\neq0\},\\
 S_p&=\#\{0\leq r<p:p\mid q_r,\ \delta_p(r)=0\}.
\end{aligned}
\tag{49}
$$



Every ordinary root has one child at each stage by (34) and (48), so it
generates exactly one infinite compatible branch.  Every singular root has
at most $p^{a-1}$ descendants modulo $p^a$.  Therefore, uniformly in
$p$ and $a$,



$$
\boxed{
 O_p\leq R_{p^a}\leq O_p+p^{a-1}S_p.}
\tag{50}
$$



This strictly sharpens $R_{p^a}\leq p^{a-1}R_p$ whenever ordinary roots
occur.  If every singular first-level root dies modulo $p^2$, equivalently
if the all-$p$ count $A_p$ from

    sources/bessel_denominator_all_lift_branching_wieferich_barrier.md

is zero, then



$$
\boxed{R_{p^a}=O_p\qquad(a\geq2).}
\tag{51}
$$



The exhaustive computation $p\leq200000$ in that source found
$A_p=0$, but this is finite evidence, not an all-prime theorem.  The
central truncated-hypergeometric congruence recorded there remains an exact
possible singular obstruction.

## 8. Why the high-level tail is still open

There are now two sharply separated issues.

1. **Singular first-level roots.**  Formula (48) proves that all later
   singularity descends from $S_p$; it does not prove that every such
   root dies.  Replacing the singular term in (50) by zero for all primes
   would require the still-open all-prime exclusion $A_p=0$.

2. **Depth of an ordinary singleton branch.**  Even (51) for every prime
   would control the number of root classes, not the size of their least
   representatives.  The ordinary branch containing
   $11^5\mid q_{1359}$ illustrates the distinction: its lifts from
   $11$ to $11^2$, and from $11^2$ to $11^4$, are unique.  A
   simple $p$-adic root can still have a long initial string of small
   base-$p$ digits.

The polynomial-argument theorem in

    sources/bessel_pade_argument_hensel_exact_no_go.md

does not resolve either issue.  It says that, when
$p\mid Q_n(1)=q_n$, the root of $Q_n(x)$ near $x=1$ is simple.
The slope (3) changes the **index** $n$, not the polynomial argument
$x$.  The singular example $p=79,r=39$ already proves that these
notions of simplicity cannot be identified.

For a route specifically through (30) and (34), the exact unsolved local
input is now:

- exclude all-$p$ lifting for every singular base root, or bound its
  aggregate contribution strongly enough; and
- prove a quantitative digit-complexity or $p$-adic irrationality
  estimate for the unique index root on every ordinary branch, strong
  enough to prevent integer truncations $n\in[N,2N)$ with
  $v_p(q_n)\log p\gg N\log N$.

Existence and simplicity of the ordinary $p$-adic branch give neither
digit estimate.  This is why the uniform target (6), and hence the desired
high-level excess bound, remains open.

Nothing in this note proves irrationality or transcendence of $e+\pi$.

## 9. Exact diagnostic

The companion script

    scripts/bessel_prime_power_second_antiperiod_certificate.py

checks (2) for several odd primes and exponents, checks the unique
subcritical factorial index $j=p$, verifies the Wronskian initial-value
identity, checks (4) on arbitrary indices, and independently enumerates
the children in (33) and (34) for manageable moduli.  It also records the
ordinary $11$-adic branch through index $1359$.

Run

    python -m py_compile scripts/bessel_prime_power_second_antiperiod_certificate.py
    python scripts/bessel_prime_power_second_antiperiod_certificate.py

For a byte-identical replay, use

    python scripts/bessel_prime_power_second_antiperiod_certificate.py \
      --output /tmp/bessel_prime_power_second_antiperiod_certificate.json
    cmp results/bessel_prime_power_second_antiperiod_certificate.json \
      /tmp/bessel_prime_power_second_antiperiod_certificate.json

The calculation is diagnostic only; the proofs for all $p,a,n$ are in
Sections 2--7.
