> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A nonvanishing criterion for the endpoint's p-adic coefficient limit

Date: 2026-09-13. Bounded literature and original continuation by audit_sources.
Independent review passed: raw_endpoint_padic_nonvanishing_independent_review.md.

The main new arithmetic statement is


$$
\boxed{
A_{mp}\equiv A_m\left(1+\frac{mp}{2}q_p(2)\right)\pmod{p^2}
\qquad(p\ {\rm odd},\ m\ge1),
}
\tag{1}
$$


where $A_n=\binom{2n}{n}Q_n(1)$ is the actual integer endpoint sequence and $q_p(2)=(2^{p-1}-1)/p$. Combined with root's already proved Gauss congruences, this gives


$$
\boxed{
v_p(A_m)\le1
\ \Longrightarrow\
\mathcal A_{m,p}:=\lim_{r\to\infty}A_{mp^r}\ne0,\qquad
v_p(\mathcal A_{m,p})=v_p(A_m).
}
\tag{2}
$$


Thus seeds with exactly one factor of $p$ are settled uniformly, without computing a new degree-$mp$ seed. Higher initial valuations are not settled here.

The literature supplies an applicable finite-binomial identity and a distinct Dwork analytic limit. I retain the distinction: the Dwork unit function is not the individual coefficient-ray limit in (2). An exact convergent Witt-coordinate representation of the latter is given in Section 6; it does not by itself exclude cancellation.

## 1. Exact integer polynomial and the two different limits

The symmetric constant-term expression in root's note has an equivalent representation over $\mathbb Z$:


$$
A_n=\operatorname{CT}(2+z+2z^{-1})^n
=\sum_{j=0}^{\lfloor n/2\rfloor}
 \binom n{2j}\binom{2j}{j}2^{n-j}.
\tag{3}
$$


Each surviving term uses the same number of positive and negative powers, so it agrees exactly with the representation having both outer coefficients $\sqrt2$. No unramified extension or coefficient Frobenius is required in (3).

Set


$$
f(z)=2+z+2z^{-1},\qquad
F(t)=\sum_{n\ge0}A_nt^n.
$$


Constant-term extraction, or the binomial series in (3), gives


$$
\boxed{F(t)=(1-4t-4t^2)^{-1/2}.}
\tag{4}
$$


The square-root branch has constant coefficient one. This is the generalized central trinomial family $T_n(2,2)$, not an elliptic-period generating series.

Root's raw_endpoint_gauss_stability_and_exact_17_depth.md supplies


$$
A_{mp^r}-A_{mp^{r-1}}\in p^r\mathbb Z,\qquad r\ge1.
\tag{5}
$$


The proof of (5) is not repeated here. In particular


$$
\mathcal A_{m,p}\equiv A_{mp}\pmod{p^2}.
\tag{6}
$$



Mellit–Vlasenko's Theorem 1 applies directly to (3): its Newton interval is $[-1,1]$, with zero its only interior lattice point. With $F_s(t)=\sum_{n<p^s}A_nt^n$, the theorem gives the Dwork truncation-ratio congruences. Their Lemma 2 gives a unit analytic limit for $F_s(t)/F_{s-1}(t^p)$ on the domain where $F_1(t)$ is a unit. Near zero that limit is


$$
\frac{F(t)}{F(t^p)}
=\sqrt{\frac{1-4t^p-4t^{2p}}{1-4t-4t^2}}.
\tag{7}
$$


These are function values indexed by a $p$-adic variable $t$; (2) concerns coefficients whose indices grow. A unit value of (7) does not imply that a chosen limiting coefficient is nonzero. [Mellit–Vlasenko, Theorem 1 and Lemma 2, pp.1–4](https://arxiv.org/pdf/1306.5811).

## 2. The applicable primary finite-binomial congruence

For every odd $p$,


$$
\sum_{j=1}^{p-1}\binom{2j}{j}\frac1{j2^j}
\equiv q_p(2)\pmod p.
\tag{8}
$$


For $p\ge5$, this is recorded as Lemma 5, equation (12), of Belbachir–Otmani, which cites Tauraso. Tauraso's equation (8) gives the underlying polynomial finite-logarithm identity. The original source and its parameter specialization are therefore available, rather than only a search-result statement. [Belbachir–Otmani, pp.6–7](https://math.colgate.edu/~integers/x27/x27.pdf), [Tauraso, Section 3, equation (8)](https://cs.uwaterloo.ca/journals/JIS/VOL19/Tauraso/taur31.pdf).

Here is an independent elementary specialization, to check all branches and signs. In characteristic $p$, put


$$
S(X)=\sum_{j=1}^{(p-1)/2}\binom{2j}{j}\frac{X^j}{j},
\quad \mathfrak l(X)=\sum_{j=1}^{p-1}\frac{X^j}{j},
\quad \alpha+\beta=1,\quad\alpha\beta=X.
$$


The polynomial $\mathfrak l(\alpha)+\mathfrak l(\beta)$ has degree at most $(p-1)/2$ in $X$. Its derivative is


$$
\frac{-1+(\alpha-\beta)^{p-1}}X
=\frac{(1-4X)^{(p-1)/2}-1}X
=S'(X).
$$


The constant terms agree because $\mathfrak l(1)=0$ modulo $p$. Since the degrees are below $p$, differentiation proves equality.

Now take $X=1/2$ and, in $\mathbb Z_p[i]$, choose
$\alpha=(1+i)/2,\ \beta=(1-i)/2$. This étale algebra is valid for every odd $p$, whether split or unramified. The elementary binomial congruence


$$
\mathfrak l(x)\equiv\frac{1-x^p-(1-x)^p}{p}\pmod p
$$


gives


$$
S(1/2)\equiv\frac{2(1-\alpha^p-\beta^p)}p\pmod p.
$$


The exact root-of-unity evaluation is


$$
\alpha^p+\beta^p=\left(\frac2p\right)2^{-(p-1)/2}=:u.
$$


This $u$ is rational, $u\equiv1\pmod p$, and
$u^2=2^{1-p}=(1+pq_p(2))^{-1}$. Hence
$u\equiv1-pq_p(2)/2\pmod{p^2}$, proving (8). Terms with $j>(p-1)/2$ vanish modulo $p$ because their central binomial coefficient is divisible by $p$, while $j$ is a unit. The same argument covers $p=3$; its single retained term is also an immediate check.

This proof does not assume that $i$ lies in $\mathbb Z_p$, or take an ambiguous square root of a $p$-adic unit.

## 3. The degree-p seed has an exact first correction

For $1\le j\le(p-1)/2$,


$$
\binom p{2j}\equiv-\frac p{2j}\pmod{p^2}.
$$


Substituting into (3) and using (8) gives


$$
A_p\equiv 2^p-p2^{p-1}q_p(2)
\equiv2+pq_p(2)=1+2^{p-1}\pmod{p^2}.
\tag{9}
$$


In particular, with $g_0=(A_p-2)/p$,


$$
g_0\equiv q_p(2)\pmod p.
\tag{10}
$$


The quantities in (9) are actual integers; all denominators used to derive the congruence are units at the odd prime.

## 4. A three-coefficient calculation proves the all-m congruence

Define the integer Laurent polynomial


$$
G(z)=\frac{f(z)^p-f(z^p)}p.
$$


It has support in $[-p,p]$. Among exponents divisible by $p$, its only coefficients are


$$
[z^p]G=0,\qquad
[z^0]G=g_0,\qquad
[z^{-p}]G=\frac{2^p-2}{p}=2q_p(2).
\tag{11}
$$


For arbitrary $m\ge1$, binomial expansion gives


$$
f(z)^{mp}\equiv
f(z^p)^m+mp\,G(z)f(z^p)^{m-1}\pmod{p^2}.
$$


Only the three exponents in (11) contribute to its constant term. Write
$B_{m-1}=[z^1]f(z)^{m-1}$. Then


$$
A_{mp}\equiv A_m+
mp\left(g_0A_{m-1}+2q_p(2)B_{m-1}\right)\pmod{p^2}.
\tag{12}
$$



The symmetry $f(2/z)=f(z)$ gives
$[z^{-1}]f^{m-1}=2B_{m-1}$, and therefore the exact identity


$$
A_m=2A_{m-1}+4B_{m-1}.
\tag{13}
$$


Using (10) in (12), the bracket becomes
$q_p(2)(A_{m-1}+2B_{m-1})=q_p(2)A_m/2$ modulo $p$. This proves (1).

This argument does not require $m<p$, does not divide by $A_m$, and remains valid when $p\mid m$ or $A_m\equiv0\pmod p$. Terms of order at least two in $pG$ are all divisible by $p^2$.

## 5. Nonvanishing and actual endpoint-depth consequences

Equations (1) and (6) give the explicit limiting congruence


$$
\boxed{
\mathcal A_{m,p}
\equiv A_m\left(1+\frac{mp}{2}q_p(2)\right)\pmod{p^2}.
}
\tag{14}
$$


The factor in parentheses is a unit. If $v_p(A_m)=0$, the limit is a unit. If $v_p(A_m)=1$, its correction term is already divisible by $p^2$, so
$\mathcal A_{m,p}\equiv A_m\pmod{p^2}$, with exact valuation one. This proves (2).

For the actual saturated degree $n=mp^\nu,\ 3m<p$, root's Gauss-stability note and the reviewed Cauchy scalar formula show that the valuation of the normalized simultaneous denominator is determined by $A_n$ whenever that valuation is less than $\nu$. Consequently:


$$
\boxed{
\begin{array}{ll}
v_p(A_m)=0:& v_p(d_n^{II})=0\quad(\nu\ge1),\\[2mm]
v_p(A_m)=1:& v_p(d_n^{II})=1\quad(\nu\ge2).
\end{array}}
\tag{15}
$$


In the second line,


$$
v_p(Z_n)=\frac{n-m}{p-1}+1,\qquad
v_p(c_n^Q)=\frac{n-m}{p-1}.
$$


The congruence depth does not determine $v_p(d_n^{II})$ at $\nu=1$ in that line.

Since $A_4=136=8\cdot17$, (15) yields


$$
v_{17}(d_{4\cdot17^\nu}^{II})=1\qquad(\nu\ge2)
$$


from the degree-four seed alone. It agrees with root's independent degree-68 certificate, but does not depend on computing that certificate. No new numerical seed or scan is used here.

For $v_p(A_m)\ge2$, (14) says only that the limit is divisible by $p^2$. It does not prove that the limit is nonzero, that the initial valuation persists, or that all endpoint depths are bounded.

## 6. An exact convergent representation, with its cancellation limitation

There is an elementary integral formal unit behind (4):


$$
H(t)=\frac{1-2t+\sqrt{1-4t-4t^2}}2\in1+t\mathbb Z[[t]].
$$


Integrality follows recursively from
$H^2-(1-2t)H+2t^2=0$, whose coefficient multiplying each new unknown coefficient is $2H(0)-1=1$. Direct differentiation gives


$$
F(t)-1=-t\frac{H'(t)}{H(t)}.
$$


Every integral formal unit has a unique factorization


$$
H(t)=\prod_{d\ge1}(1-b_dt^d),\qquad b_d\in\mathbb Z.
$$


This can be proved by successively removing its first nonzero coefficient; each coefficient requires only finitely many factors. Logarithmic differentiation gives the exact ghost-coordinate identity


$$
A_n=\sum_{d\mid n}d\,b_d^{\,n/d}.
\tag{16}
$$



For $p\nmid m$, split $d=ep^j$, $e\mid m$. Let $\omega_p(b)$ denote the Teichmüller unit congruent to $b$ modulo $p$, and put $\omega_p(b)=0$ if $p\mid b$. Taking the limit in (16) yields


$$
\boxed{
\mathcal A_{m,p}
=\sum_{e\mid m}e\sum_{j\ge0}
p^j\,\omega_p(b_{ep^j})^{\,m/e}.
}
\tag{17}
$$


For each fixed $j$, the limit
$b^{p^{r-j}}\to\omega_p(b)$ is elementary. The tails with $j\ge J$ are uniformly divisible by $p^J$, so the interchange of the limit and sum is justified. Formula (17) is a usual Witt-coordinate representation, derived here for the actual algebraic unit rather than asserted from a generic formal analogy.

It represents the limit exactly and converges at a controlled rate. Its summands can cancel, so it supplies no extra nonvanishing statement for seeds with valuation at least two. Positivity of the original integer constant terms does not give a $p$-adic sign or prevent this cancellation.

## 7. Exact remaining target and source coverage

A concrete next step is the transformation $A_{mp}$ modulo $p^3$, or a corresponding higher-level relative congruence that retains the vanishing of $A_m$. At the next order, the terms involving $G^2$ and the next precision of the coefficients of $G$ enter; the three-coefficient first-order simplification alone does not control them. A proved identity forcing these corrections to retain the full initial valuation would extend (2). No such identity is asserted here.

The primary-source PDFs and hashes are retained in literature_endpoint_padic/coverage.json. The source scope is limited and explicit:

- Mellit–Vlasenko, arXiv:1306.5811, Theorem 1 and Lemma 2, pp.1–4: applicable Dwork congruences and unit truncation-ratio limit, not coefficient-ray nonvanishing.
- Tauraso, JIS 19 (2016), Article 16.5.4, Section 3 equation (8), with the finite-logarithm definitions: the applicable binomial polynomial identity.
- Belbachir–Otmani, Integers 23 (2023), A27, Lemma 5 equation (12): direct specialization (8), with its reference to Tauraso. Its unrelated quadrinomial assertions are not used.

The new conclusion is the actual all-$m$ formula (1) and its endpoint nonvanishing criterion for seed valuations zero or one. The main rationality problem, large-prime growth, and deeper exceptional coefficient limits remain open.
