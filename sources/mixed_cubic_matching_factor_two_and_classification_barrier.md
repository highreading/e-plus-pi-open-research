> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Mixed-cubic matching: the missing factor two and the classification barrier

Date: 2026-08-27.

## 1. Scope and verdict

This note audits the implication



$$
\text{item 133 arithmetic}+
 \text{the frozen saddle packages}+
 \text{a positive \(e\)-form}
 \quad\Longrightarrow\quad
 \text{a conclusion about }e+\pi .                                \tag{1}
$$



The audit finds a missing synchronization hypothesis.

Let $n=6m$.  The frozen exact-algebraic saddle certificate and the frozen
fixed-circle complex-Laplace theorem, combined with item 133, produce
nonzero integer $\pi$-forms whose values tend to zero.  In the notation
below their certified coefficient and rational error rates are



$$
h=2.3246783391437307\ldots,
 \qquad d=2.3370623743589730\ldots,                                \tag{2}
$$



so $d/h=1.0053272038\ldots>1$.  Together with the independently known
irrationality of $\pi$, this makes the resulting shrinking forms nonzero;
it is not an independent new proof of that theorem.  More importantly, it is
**not**, by itself, enough to match the form with the standard positive beta
form for $e$.

With no proved exponential common content at the matching stage, the two
positive matched terms have optimal rate



$$
\boxed{h-\frac d2=1.1561471519642442\ldots>0.}                    \tag{3}
$$



Thus the available generic upper bound grows exponentially.  The
unsynchronized sufficient threshold is $d>2h$, not $d>h$.

More generally, let $c_m$ be the extra primitive content of the item 133
integer pair, let $\Delta_m$ be the coefficient-matching gcd with the
chosen beta denominator, and let $g_m$ be the final content of the
matched pair.  At the optimal beta scale, irrationality of $e+\pi$
would follow from



$$
\liminf\frac1n\log(c_m\Delta_mg_m)>h-\frac d2,                    \tag{4}
$$



whereas a Roth-level transcendence conclusion would require the much
stronger condition



$$
\liminf\frac1n\log(c_m\Delta_mg_m)>h.                             \tag{5}
$$



No theorem in item 133, its dependencies, or the standard beta-form
matching sources proves either (4) or (5).  In particular, the Cartier
content in item 133 has already been spent in the definition of $h$; it
is not a matching gcd with the Bessel/beta denominator.

This is a theorem about the logical and quantitative output of the current
chain.  It does not prove that the actual extra contents in (4)--(5) are
small, and it does not rule out a new arithmetic synchronization theorem.
It proves that such a theorem is an additional indispensable input.

## 2. What the frozen saddle packages give

Retain the notation of
`sources/mixed_cubic_boundary_cartier_content_and_recurrence.md`.  Put



$$
\mathcal G_m=\prod_{p\in\mathcal P_m}p,
 \qquad
 U_m=\frac{\mathcal D_m^\sharp A_m}{\mathcal G_m},
 \qquad
 V_m=\frac{\mathcal D_m^\sharp B_m}{\mathcal G_m}.                 \tag{6}
$$



The frozen Cartier theorem proves $U_m,V_m\in\mathbb Z$.  The frozen
exact-algebraic and fixed-circle packages, including the nonzero determinant
amplitude and the unique-modulus maximum, prove



$$
\frac1n\log|B_m|\longrightarrow2\ell,                             \tag{7}
$$



and the positive-integral estimate gives



$$
\limsup\frac1n\log|A_m+B_m\pi|\leq\phi+\ell.                     \tag{8}
$$



The prime number theorem estimates already proved in item 133 give



$$
\frac1n\log\left|\frac{\mathcal D_m^\sharp}{\mathcal G_m}\right|
 \longrightarrow
 c_0:=\frac32\log2+\frac12-\frac{\mathfrak C}{6},                 \tag{9}
$$



where



$$
\mathfrak C=-4\log2+\frac\pi{\sqrt3}+3\log3.                    \tag{10}
$$



Consequently



$$
\begin{aligned}
 \frac1n\log|V_m|&\longrightarrow h:=2\ell+c_0,\\
 \limsup\frac1n\log|U_m+V_m\pi|
 &\leq c_0+\phi+\ell=h-d,
 \qquad d:=\ell-\phi.                                             \tag{11}
\end{aligned}
$$



Numerically,



$$
h-d=-0.0123840352152423\ldots.                                   \tag{12}
$$



The saddle determinant amplitude proves $V_m\ne0$ for all sufficiently
large $m$.  Hence $U_m+V_m\pi\ne0$, because $\pi$ is irrational.
Equations (11)--(12) then give a genuine shrinking nonzero integer form in
$1,\pi$.

There is no remaining denominator issue in this conclusion: (6) is
integral by the frozen theorem.  Nor is a lower asymptotic for (8) needed.
The frozen fixed-circle theorem supplies the uniform expansion needed for
(7), including its nonzero cross-amplitude; the already-recorded positive
integral estimate supplies the upper bound (8).

This conclusion does not yet mention $e+\pi$.

## 3. Exact minimal matching with the beta $e$-form

We record the matching calculation with all three contents visible.

Let



$$
L=a+\varepsilon b\pi>0,
 \qquad a\in\mathbb Z,\quad b\in\mathbb Z_{>0},\quad
 \varepsilon\in\{1,-1\},\quad \gcd(a,b)=1.                       \tag{13}
$$



For an integer $N\geq1$, the standard beta form is



$$
E_N=(-1)^N(q_Ne-p_N)
 =\frac1{N!}\int_0^1x^N(1-x)^Ne^x\,dx>0,                         \tag{14}
$$



where $p_N,q_N\in\mathbb Z$, $q_N>0$, and
$\gcd(p_N,q_N)=1$.  We may choose the parity of $N$ so that the
coefficient sign $(-1)^N$ in (14) equals $\varepsilon$.  Changing $N$
by one does not affect any exponential rate below.

Put



$$
\Delta=\gcd(b,q_N),\qquad b=\Delta b_0,qquad q_N=\Delta q_0.     \tag{15}
$$



The minimally coefficient-matched form is the positive sum



$$
W=b_0E_N+q_0L=M+C(e+\pi)>0,                                      \tag{16}
$$



where, up to the common harmless sign $\varepsilon$,



$$
C=\Delta b_0q_0=\frac{bq_N}{\Delta}.                              \tag{17}
$$



Let



$$
g=\gcd(M,C).                                                       \tag{18}
$$



Then



$$
\boxed{g\mid\Delta.}                                             \tag{19}
$$



Indeed, reduction of $M$ modulo a prime divisor of $q_0$ leaves a
unit multiple of $b_0p_N$, while reduction modulo a prime divisor of
$b_0$ leaves a unit multiple of $q_0a$.  Thus
$\gcd(M,b_0q_0)=1$, prime power by prime power.  Since
$C=\Delta b_0q_0$, every prime-power divisor of (18) lies in $\Delta$.

The fully primitive positive form therefore is



$$
\boxed{
 \Omega=\frac Wg
 =\frac{b}{\Delta g}E_N
  +\frac{q_N}{\Delta g}L>0,}                                     \tag{20}
$$



and its $e+\pi$ coefficient is



$$
\boxed{Q=\frac{bq_N}{\Delta g}.}                                 \tag{21}
$$



Equations (19)--(21) are exact.  In particular, an upper bound on
$\Delta$ or $g$ cannot help to prove smallness; a *lower* bound for
their product is required.

## 4. The beta scale and the factor-two optimization

The recurrence for $q_N$, or its terminating factorial sum, gives



$$
\log q_N=N\log N+O(N).                                           \tag{22}
$$



For completeness, the lower bound follows by iterating
$q_N\geq(4N-2)q_{N-1}$, and the reverse inequality with $4N+O(1)$
gives the upper bound.  Also, since $1\leq e^x\leq e$, beta integration
gives



$$
\frac{N!}{(2N+1)!}\leq E_N\leq
 e\frac{N!}{(2N+1)!},
 \qquad
 \log E_N=-N\log N+O(N).                                         \tag{23}
$$



Let $N=N(n)$ have the required parity and satisfy



$$
\frac{N\log N}{n}\longrightarrow t>0.                            \tag{24}
$$



Let



$$
c_m=\gcd(U_m,V_m),                                                \tag{25}
$$



and apply (13)--(21) to the primitive reduction of
$U_m+V_m\pi$.  Define the total content gain



$$
\Gamma_m=\frac1n\log(c_m\Delta_mg_m).                             \tag{26}
$$



Equations (11), (20), and (22)--(24) give the available upper ledger



$$
\limsup\frac1n\log\Omega_m
 \leq
 \max\{h-t-\Gamma_*,\ t+h-d-\Gamma_*\},                          \tag{27}
$$



on every subsequence on which
$\liminf\Gamma_m\geq\Gamma_*$.  The corresponding coefficient obeys



$$
\limsup\frac1n\log Q_m
 \leq h+t-\Gamma_*.                                               \tag{28}
$$



The two terms in (27) balance at



$$
t=\frac d2,                                                       \tag{29}
$$



where



$$
\limsup\frac1n\log\Omega_m
 \leq h-\frac d2-\Gamma_*.
                                                                        \tag{30}
$$



This proves the following precise thresholds.

**Theorem 4.1 (matching thresholds).**

1. A proved bound
   
   

$$
\Gamma_*>h-\frac d2                                           \tag{31}
$$


   
   makes the positive integer forms $\Omega_m$ tend to zero and hence
   proves $e+\pi$ irrational.
2. With no exponential extra content, $\Gamma_*=0$, this method requires
   
   

$$
\boxed{d>2h.}                                                  \tag{32}
$$


   
   The weaker inequality $d>h$ does not make both positive summands in
   (20) small.
3. If (31) holds, the linear-form decay exponent furnished by (27)--(30)
   relative to (28) is at least
   
   

$$
\lambda(\Gamma_*)
    =\frac{\Gamma_*+d/2-h}{h+d/2-\Gamma_*},                        \tag{33}
$$


   
   whenever the denominator in (33) is positive.  It crosses the Roth
   threshold $1$ exactly when
   
   

$$
\boxed{\Gamma_*>h.}                                            \tag{34}
$$


   
   If the coefficient in (28) stays bounded instead, the shrinking
   positive forms give an immediate contradiction without Roth.

The positivity in (20) supplies nonvanishing, so no cancellation caveat is
hidden in Theorem 4.1.

For the item 133 constants,



$$
\begin{aligned}
 d/2&=1.1685311871794865\ldots,\\
 h-d/2&=1.1561471519642442\ldots,\\
 2h-d&=2.3122943039284884\ldots.                                  \tag{35}
\end{aligned}
$$



Thus the unsynchronized certified bound is exponentially on the wrong
side.  Irrationality needs an additional content product of rate greater
than $1.1561471519\ldots$ per $n$.  Roth-level transcendence needs a
rate greater than $2.3246783391\ldots$ per $n$.  Item 133 supplies no
divisibility relation at all between $V_m$ and $q_{N(n)}$, and no lower
bound for the final $g_m$.

The often tempting condition $q_N\mid b$ is precisely a large matching
gcd, not a generic fact.  It makes $\Delta=q_N$, which can repair the
irrationality balance, but it is not implied by a denominator clearing for
$b$.  Divisibility by a known clearing multiplier and divisibility of the
actual endpoint coefficient are different assertions.

## 5. A sharp abstract countermodel to the exponent-$>1$ shortcut

The logical issue can be seen without asymptotics.  Put



$$
\theta_0=3-e.
$$



Then $e+\theta_0=3\in\mathbb Q$.  Let $p_j/q_j>e$ run through the
upper continued-fraction convergents of $e$.  Define



$$
r_j=3-\frac{p_j}{q_j}<\theta_0.                                  \tag{36}
$$



The positive integer $\theta_0$-form is



$$
q_j\theta_0-(3q_j-p_j)=p_j-q_je>0,                               \tag{37}
$$



and



$$
0<\theta_0-r_j=\frac{p_j}{q_j}-e<\frac1{q_j^2}.                  \tag{38}
$$



Thus a positive rational approximation exponent $2>1$ for one summand is
perfectly compatible with a rational sum with $e$.  The corresponding
oriented positive $e$-form has the *opposite* target-coefficient sign.
Using the sign needed for $e+\theta_0$ makes the two forms cancel exactly.

This countermodel does not replace $\pi$ by $\theta_0$ in the main
problem.  Its precise role is to disprove any abstract lemma which tries to
deduce irrationality of a sum from only positivity of separately oriented
forms and a rational approximation exponent greater than one.  The missing
coefficient-sign and denominator synchronization contains the arithmetic
content of the problem.

## 6. Why the one-dimensional output is not yet a classification method

Even the stronger unsynchronized hypothesis $d>2h$ would only prove
irrationality by this matching.  With $\Gamma_*=0$, equations (28)--(33)
give



$$
\lambda(0)=\frac{d-2h}{d+2h}<1.                                  \tag{39}
$$



Hence the resulting forms do not cross Roth's linear-form exponent $1$.
This strict inequality holds for every finite positive $d,h$, not just
for the item 133 constants.

There is also an elementary norm obstruction.  Let $\alpha$ be algebraic
of degree $r\geq2$.  Choose a fixed integer $D_\alpha>0$ such that
$D_\alpha\alpha$ is an algebraic integer.  If



$$
0<|M+Q\alpha|<1,
$$



then $|M|\ll_\alpha Q$, and the nonzero integer norm of
$D_\alpha(M+Q\alpha)$ gives



$$
\boxed{|M+Q\alpha|\gg_\alpha Q^{-(r-1)}.}                       \tag{40}
$$



Indeed, every nondistinguished conjugate is $O_\alpha(Q)$, so their
product consumes $r-1$ powers of $Q$.  Full-norm amplification therefore
makes the required exponent worse.  Roth improves (40) to the universal
threshold $1+\eta$, but (39) is still below it.

Two simultaneous rational linear forms do not change this accounting by
themselves.  For



$$
\Omega_i=M_i+Q_i\alpha\quad(i=1,2),
$$



their coefficient determinant satisfies



$$
M_1Q_2-M_2Q_1=Q_2\Omega_1-Q_1\Omega_2.                           \tag{41}
$$



If the pairs are independent, the left side is a nonzero integer, so



$$
1\leq Q_2|\Omega_1|+Q_1|\Omega_2|.                               \tag{42}
$$



At comparable heights this again requires linear-form exponent greater
than one.  If the determinant vanishes, the two forms are proportional and
carry only one-dimensional information.

## 7. Translation under hypothetical algebraicity

There is a second exact way to see the classification obstruction.  Assume
temporarily that



$$
s=e+\pi
$$



is algebraic of degree $r$, and let $R_j=A_j/B_j\to\pi$ be reduced
rational approximants.  Put



$$
\alpha_j=s-R_j.
$$



Then



$$
\deg\alpha_j=r,
 \qquad
 h(\alpha_j)=\log B_j+O_s(1),
 \qquad
 |e-\alpha_j|=|\pi-R_j|.                                         \tag{43}
$$



Thus the mixed-cubic exponent $d/h=1.005327\ldots$ becomes only an
algebraic approximation of $e$ of the same Weil-height exponent.  For
$r=1$, the elementary continued-fraction lower bound



$$
\left|e-\frac pq\right|\gg\frac1{q^2\log(2q)}                   \tag{44}
$$



shows why an exponent below $2$ is compatible with rational $s$.

Let



$$
F_s(X)=a_r\prod_{k=1}^r(X-s_k)\in\mathbb Z[X]
$$



be the primitive minimal polynomial of $s=s_1$, and define



$$
G_j(X)=B_j^rF_s\left(X+\frac{A_j}{B_j}\right)\in\mathbb Z[X].    \tag{45}
$$



At $X=e$, exact factorization gives



$$
G_j(e)=a_rB_j^r(R_j-\pi)
        \prod_{k=2}^r(e+R_j-s_k).                                  \tag{46}
$$



The product over $k\geq2$ tends to
$\prod_{k=2}^r(s-s_k)\ne0$.  Therefore



$$
\boxed{|G_j(e)|\asymp_s B_j^r|R_j-\pi|.}                         \tag{47}
$$



If the rational error has exponent $\kappa$, so that
$|R_j-\pi|=B_j^{-\kappa+o(1)}$, then



$$
|G_j(e)|=B_j^{r-\kappa+o(1)}.                                    \tag{48}
$$



For every hypothetical degree $r\geq2$, the current
$\kappa=d/h=1.005327\ldots$ makes this resultant value grow.  Moreover,
$G_j(e)$ is transcendental, not a rational integer norm, so the lower
bound $|N|\geq1$ is unavailable.  The conjugate product has spent the
distinguished small factor on $r-1$ ordinary factors.

Equations (40) and (47)--(48) rigorously exclude the naive full-norm or
single-resultant amplification as a classification-level completion of
the current one-dimensional data.  They do not exclude a construction
which is simultaneously small at several embeddings or which proves the
new content condition (5).

## 8. Exact conclusion and surviving targets

Combining the three frozen packages gives the following unconditional
conclusion:

* item 133 gives an infinite sequence of nonzero shrinking integer forms
  in $1,\pi$, with the rates (2) and (11).

The following conclusions do **not** follow from the current chain:

* irrationality of $e+\pi$, because the generic positive beta matching
  needs either $d>2h$ or the additional content bound (4);
* transcendence of $e+\pi$, because even a generic repaired irrationality
  match remains below Roth by (39), while norms and two-form determinants
  obey (40) and (42).

There are three precise positive targets left by the audit.

1. Prove (4) for an explicitly synchronized beta index
   $N\sim(d/2)n/\log n$.  This would establish irrationality.
2. Prove the stronger (5), necessarily using almost all of both the
   matching gcd and final content at the optimal scale.  This would cross
   Roth and establish transcendence.
3. Construct genuinely simultaneous conjugate forms whose nondistinguished
   factors are sublinear in the main coefficient.  A single distinguished
   form and its formal norm cannot do this.

No classification of $e+\pi$ is asserted in this note.
