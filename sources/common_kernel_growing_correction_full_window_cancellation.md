> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Growing corrections still admit complete prime-window CRT cancellation

Checked: 2026-08-27 UTC.

## 1. Verdict

Put



$$
u=1+x^2,\qquad {\cal T}P=(1-x)P'-xP.
$$



For each positive integer $q$, let



$$
K_q\in\mathbb Z[x]\setminus\{0\},\qquad
 k_q=\deg K_q,
$$



with completely arbitrary coefficients, subject only to



$$
k_q\leq12q-10.                   \tag{1}
$$



For every sufficiently large $q$, the conclusion below holds
simultaneously for every such polynomial.  There is no coefficient-height,
content, sparsity, or fixed-congruence hypothesis.

This note constructs $h_q\in\mathbb Z[x]$ satisfying



$$
\boxed{
 h_q\equiv1\pmod {u^2},\qquad h_q(0)=0,\qquad
 0\leq h_q(x)\leq1\quad(0\leq x\leq1),}                 \tag{2}
$$



with the exact degrees



$$
\boxed{
 \operatorname {ord}_0h_q=20q,\qquad
 \deg h_q=48q+13.}                                      \tag{3}
$$



Define



$$
r_q=\frac{h_q-1}{u},\qquad
 S_q=\frac{{\cal T}(h_qK_q)-{\cal T}K_q}{u},            \tag{4}
$$



and let $D_q$ be the least positive common clearing denominator of



$$
\int_0^1r_q(x)\,dx,\qquad
 \int_0^1xr_q(x)\,dx,\qquad
 \int_0^1S_q(x)\,dx.                                   \tag{5}
$$



Then



$$
\deg S_q+1=48q+k_q+13,                                 \tag{6}
$$



and every prime in its complete one-third window is absent from all
three rational denominators:



$$
\boxed{
 \gcd\!\left(
 D_q,
 \prod_{(48q+k_q+13)/3<p<20q}p
 \right)=1.}                                            \tag{7}
$$



There are no exceptional primes depending on the coefficients of
$K_q$, and not even the quadratic exceptional integer from the
single-channel construction survives.

If $k_q/q\to c<12$, the window has Chebyshev mass



$$
\boxed{
 \sum_{(48q+k_q+13)/3<p<20q}\log p
 =\left(4-\frac c3\right)q+o(q).}                        \tag{8}
$$



Thus the theorem includes $k_q=o(q)$, every fixed linear growth rate
$k_q\sim cq$ with $c<12$, and corrections of unbounded or
factorial coefficient height.  The ratio $12$ is the natural maximal
linear threshold for this prime-window question: when
$k_q\geq12q-13$, the lower endpoint in (7) is at least $20q$, so
the window is empty.  Since every potentially nonempty window has
$k_q\leq12q-14$, condition (1) covers the complete nonvacuous range,
including endpoint gaps $12q-k_q=O(1)$.

The native Taylor--Robin correction is linear but has factorial-size
coefficients.  It is covered without any relation between that
coefficient height and $q$.  Section 8 also shows that, when the
Taylor degree lies below the prime window, neither its base rational
coordinate nor primitive polynomial content restores a window-prime
obstruction.

This is a negative result about a proposed denominator mechanism.  It
does not prove positivity or decay of the resulting corrected Taylor
residual and proves neither irrationality nor transcendence of
$e+\pi$.

## 2. Degree-adapted padding

For brevity write $k=k_q$, and put



$$
E=\left\lfloor\frac{k+5}{4}\right\rfloor+1,
 \qquad A=3q-E.                                         \tag{9}
$$



Condition (1) makes $A\geq1$.  Use the same positive base



$$
B_q=x^{20q}(5q+1-5qx^4).                               \tag{10}
$$



The exact identity



$$
B_q-1=-(1-x^4)^2\sum_{j=0}^{5q-1}(j+1)x^{4j}
$$



shows that $B_q\equiv1\pmod {u^2}$, since
$(1-x^4)^2=(1-x^2)^2u^2$.  Also, on writing $z=x^4$,
the derivative of $z^{5q}(5q+1-5qz)$ is
$5q(5q+1)z^{5q-1}(1-z)$.  Thus $0\leq B_q\leq1$ on
$[0,1]$.

Shift the padding to the left by exactly $E$ four-step units:



$$
\boxed{
 w_q=x^{4A}(1-x^4)^{4q}(1-x^2).}                        \tag{11}
$$



Set



$$
V_q=x^{20q+4A}(5q+1-5qx^4)(1-x^4)^{4q},               \tag{12}
$$



so that



$$
B_quw_q=V_q(1-x^4).             \tag{13}
$$



All three polynomials in (12)--(13) are supported in degrees divisible
by four.

The correction polynomial will use the universal channel set



$$
\boxed{
 \mathscr S_E=
 \{x^{r+4a}:r\in\{1,2,3\},\ 0\leq a\leq E\}.}          \tag{14}
$$



It has $3(E+1)=O(k+1)$ monomials.  No channel in residue class zero
modulo four is used.

Once nonnegative integer coefficients have been assigned, write the
resulting polynomial as $C_q$ and define



$$
\boxed{
 h_q=B_q(1-u^2w_qC_q).}                                  \tag{15}
$$



The largest channel is $x^{3+4E}$.  Its coefficient will be forced
to be positive.  Consequently



$$
\begin{aligned}
 \deg w_q&=28q-4E+2,\\
 \deg(1-u^2w_qC_q)&=28q+9,\\
 \deg h_q&=48q+13.                                      \tag{16}
\end{aligned}
$$



The second factor in (15) has constant term one, proving the order in
(3).  Since $K_q\ne0$, the leading term of
${\cal T}(h_qK_q)$ cannot cancel against ${\cal T}K_q$.  Division
by the monic quadratic $u$ proves (6).

## 3. An invertible consecutive Pascal block

The finite-field input is stronger than the coefficient-root lemma used
for a fixed correction.

**Pascal-block lemma.**  Let $n,e,\kappa$ be nonnegative integers with



$$
0\leq\kappa\leq n,              \tag{17}
$$



and use the convention $\binom nr=0$ outside $0\leq r\leq n$.
The $(e+1)$-square matrix



$$
T_{ij}=(-1)^{\kappa+i-j}\binom n{\kappa+i-j},
 \qquad0\leq i,j\leq e,                                 \tag{18}
$$



has determinant whose absolute value is



$$
\boxed{
 |\det T|=
 \prod_{j=0}^e
 \frac{\binom{n+e-j}{\kappa}}
      {\binom{\kappa+e-j}{\kappa}}
 =\prod_{\ell=0}^e
 \frac{(n+\ell)!\,\ell!}
      {(n+\ell-\kappa)!\,(\kappa+\ell)!}.}             \tag{19}
$$



Here is a self-contained determinant proof.  Remove the row and column
signs in (18), and write



$$
D_e(n,\kappa)=\det_{0\leq i,j\leq e}
                 \binom n{\kappa+i-j},
 \qquad D_{-1}(n,\kappa)=1.
$$



Desnanot--Jacobi condensation on the first and last rows and columns
gives, for $e\geq1$,



$$
D_e(n,\kappa)D_{e-2}(n,\kappa)
 =D_{e-1}(n,\kappa)^2
  -D_{e-1}(n,\kappa-1)D_{e-1}(n,\kappa+1).
$$



Let $F_e(n,\kappa)$ denote the second product in (19).  Direct
telescoping gives



$$
\frac{F_{e-1}(n,\kappa-1)F_{e-1}(n,\kappa+1)}
      {F_{e-1}(n,\kappa)^2}
 =\frac{\kappa(n-\kappa)}
       {(\kappa+e)(n-\kappa+e)},
$$



while



$$
\frac{F_e(n,\kappa)F_{e-2}(n,\kappa)}
      {F_{e-1}(n,\kappa)^2}
 =\frac{e(n+e)}{(\kappa+e)(n-\kappa+e)}.
$$



The two numerators add to the common denominator.  Since
$D_0=F_0=\binom n\kappa$, induction proves $D_e=F_e$ for
$0<\kappa<n$.  At $\kappa=0,n$, the binomial matrix is triangular
with diagonal one, and (19) is also one.  Restoring the signs proves
(19).

If $p$ is a prime with



$$
n+e<p,                          \tag{20}
$$



then every factorial in (19) is a $p$-unit, so $T$ is invertible
over $\mathbb F_p$.

Equivalently, if $P\in\mathbb F_p[y]$ has degree at most $e$, its
coefficients are determined by any $e+1$ consecutive coefficients



$$
[y^\kappa](1-y)^nP,\ldots,
 [y^{\kappa+e}](1-y)^nP.                                \tag{21}
$$



In particular, those consecutive coefficients cannot all vanish unless
$P=0$.  Unlike a statement confined to the central binomial range,
(21) remains valid when $\kappa+e>n$.  This is precisely what permits
the padding shift in (11) to absorb all growing channel degrees.

## 4. Exact two-row response system

Reduce now modulo a prime in the window (7).  Put



$$
t_0=\frac{p-1}{2}-8q,
 \qquad t=t_0+E.                                        \tag{22}
$$



The lower endpoint of (7) gives $t_0\geq2$, while $p<20q$ gives
$t_0\leq2q-1$.  Also



$$
4q+E<p                          \tag{23}
$$



for all sufficiently large $q$.

Write



$$
\mathcal V_q(y)=(5q+1-5qy)(1-y)^{4q},                 \tag{24}
$$



and decompose the coefficient-dependent but degree-bounded polynomial



$$
\begin{aligned}
 H_{K_q}(x)
 &:=(1+x)(1-x^2)^2K_q(x)\\
 &=H_0(x^4)+xH_1(x^4)+x^2H_2(x^4)+x^3H_3(x^4).          \tag{25}
\end{aligned}
$$



Each $H_j$ has degree at most $E-1$.

Write the three residue components of $C_q$ as



$$
C_q=xC_1(x^4)+x^2C_2(x^4)+x^3C_3(x^4).                \tag{26}
$$



For the varying part $\delta h=-B_qu^2w_qC_q$, equations (12)--(13)
give



$$
\delta r=\frac{\delta h}{u}
          =-V_q(1-x^4)C_q.
$$



Consequently the positive response row whose negative is added to the
moment coefficient at degree $2p-1$ is



$$
[y^t]\mathcal V_q(1-y)C_1,                             \tag{27}
$$



and the full-output row is



$$
[y^t]\mathcal V_q
 \{H_0C_1+yH_3C_2+yH_2C_3\}.                           \tag{28}
$$



For completeness, if $\delta h=u^2Q$ and $L=QK_q$, then at
$O=2p-1$,



$$
\frac{{\cal T}(u^2L)}u
 =4x(1-x)L+u(1-x)L'-xuL,
$$



and collecting the four relevant coefficients, using
$O\equiv-1\pmod p$, gives



$$
[x^O]\frac{{\cal T}(u^2L)}u
 \equiv[x^O](1+x)(1-x^2)L\pmod p.                      \tag{29}
$$



Substitution of $Q=-B_qw_qC_q$ gives the negative of (28).  If



$$
{\cal T}K_q=uG_0+(\alpha+\beta x),                     \tag{30}
$$



the product rule gives



$$
S_q=(h_q-1)G_0+\frac{(h_q-1)(\alpha+\beta x)}u
     +(1-x)\frac{h_q'}uK_q.
$$



The forced low coefficient of $S_q$ is



$$
[x^{p-1}]S_q=\varepsilon_p\alpha,
 \qquad\varepsilon_p=(-1)^{(p+1)/2}.                    \tag{31}
$$



Here the growing degree causes no hidden low or high base term.  Indeed,
$\deg G_0\leq k-1<p-1$, while $h_q'/u$ has order at least
$20q-1>p-1$.  Hence the forced prefix of $r_q$ gives (31) exactly.
Also, with



$$
S_{B,q}=\frac{{\cal T}(B_qK_q)-{\cal T}K_q}{u},
$$



one has



$$
\deg S_{B,q}\leq20q+k+3<2p-1.                          \tag{31a}
$$



The last strict inequality follows from $k\leq12q-10$ and the
lower endpoint of the prime window.  Thus the coefficient at degree
$2p-1$ is entirely the varying response (28)--(29).

Hence the two local targets for (27)--(28) are



$$
(2\varepsilon_p,
                          2\varepsilon_p\alpha).         \tag{32}
$$



## 5. No coefficient-dependent exceptional primes

The channels in (14) always solve (32), prime by prime.

First, the $E+1$ class-one moment responses are the consecutive
coefficients of



$$
(1-y)^{4q}(5q+1-5qy)(1-y)                              \tag{33}
$$



from index $t_0$ through $t_0+E$.  Apply the Pascal-block lemma with
$n=4q,e=E,\kappa=t_0$.  The polynomial multiplying
$(1-y)^{4q}$ is nonzero and has degree at most $E$, so at least one
class-one moment response is a unit modulo $p$.  This removes the
single-coefficient quadratic degeneracy entirely.

Now work in $\mathbb F_p[y]$.

* If $H_3\ne0$, the class-two full responses form the consecutive
  coefficient block of $\mathcal V_qH_3$ beginning at $t_0-1$.
  The lemma supplies a nonzero response.  It changes no moment, so it and
  a nonzero class-one moment column solve (32).

* If $H_3=0,H_2\ne0$, the identical argument uses a class-three
  column.

* Suppose $H_2=H_3=0$.  If the full row on all class-one columns were
  proportional to the moment row, subtract the corresponding scalar
  multiple.  The block lemma applied from index $t_0$ would force

  

$$
H_0=\lambda(1-y).               \tag{34}
$$



  Otherwise two class-one columns give a nonzero two-by-two minor and
  solve (32).

In the remaining case (34), the proportional row is automatically
consistent.  Indeed, over every field of odd characteristic, divisibility



$$
(1+x)(1-x^2)^2\mid
 \lambda(1-x^4)+xH_1(x^4)                               \tag{35}
$$



forces $\lambda=0$: the double zero at $x=1$ gives
$H_1(1)=0,H_1'(1)=\lambda$, while the first derivative at the triple
zero $x=-1$ is $8\lambda$.  With $\lambda=0$, divisibility by
$(1-x)^2(1+x)^3$ forces $H_1(x^4)$ to have a triple zero at
$-1$, hence also at $1$.  Thus
$H_1(x^4)=(1-x^4)^3R(x^4)$, and exact division gives



$$
K_q\equiv x(1-x)u^3R(x^4)\pmod p,                      \tag{36}
$$



Such a polynomial is divisible by $u^3$, so its image under ${\cal T}$
is divisible by $u^2$.  Hence $\alpha\equiv0\pmod p$.  Both the full
row and its target in (32) vanish.

This exhausts every reduction of every integer polynomial $K_q$.
No coefficient content needs to be excluded.

## 6. CRT, exact degree, and positivity capacity

Let



$$
P_q=\prod_{(48q+k+13)/3<p<20q}p.                       \tag{37}
$$



Let $m_q$ be the number of primes in (37).  For each prime, solve (32)
by one of the cases in Section 5, setting all unused local residues to
zero.  Every local solution uses at most two channels.  Consequently the
union of the active channels over all primes has size at most $2m_q$.
Apply the ordinary Chinese remainder theorem separately on that union,
take least nonnegative representatives in $[0,P_q)$, and set every
other channel coefficient to zero.

Finally add $P_q$ to the coefficient of the largest channel
$x^{3+4E}$.  This changes no congruence, preserves nonnegativity, and
forces the exact degrees (3), (6).  The coefficient sum satisfies



$$
\sum_{c\text{ a coefficient of }C_q}c
                         \leq(2m_q+1)P_q.                \tag{38}
$$



For $z=x^4$, the padding maximum is exact:



$$
\boxed{
 \max_{0\leq z\leq1}z^A(1-z)^{4q}
 =\left(\frac A{A+4q}\right)^A
  \left(\frac{4q}{A+4q}\right)^{4q}.}                  \tag{39}
$$



Let $Q_q$ be one quarter of the reciprocal of (39), and put $a=A/q$.
The fact that



$$
4E-k\in\{6,7,8,9\}             \tag{40}
$$



shows that, along any sequence on which $a$ tends to a positive
limit, the prime number theorem gives



$$
\log P_q=\frac43A+o(q).                                \tag{41}
$$



On the other hand,



$$
\frac1q\log Q_q
 =(a+4)\log(a+4)-a\log a-4\log4+o(1).                  \tag{42}
$$



The entropy margin over (41) is



$$
f(a)=(a+4)\log(a+4)-a\log a-4\log4-\frac43a.          \tag{43}
$$



It is strictly positive for $0<a\leq3$.  Indeed,



$$
f'(a)=\log(1+4/a)-4/3                                  \tag{44}
$$



and $f''(a)=-4/(a(a+4))<0$.  Moreover $f'(a)\to+\infty$ as
$a\downarrow0$, while
$f'(3)=\log(7/3)-4/3<0$ by $\log x<x-1$.  Thus $f'$ has exactly
one zero, which is a maximum of $f$.  Therefore the
minimum on $[0,3]$ is at an endpoint.  One has $f(0)=0$, while



$$
f(3)=7\log7-3\log3-4\log4-4>0                         \tag{45}
$$



because $7^7/(3^3 4^4)>81>e^4$.  Thus (38)--(45) prove the
required capacity inequality whenever $a$ stays bounded away from
zero: the harmless factor $2m_q+1$ has logarithm $O(\log q)$.

It remains to make the endpoint $a\to0$ uniform.  Write
$\delta=4E-k$.  The length of the prime window is



$$
Y_q=20q-\frac{48q+k+13}{3}
     =\frac{4A+\delta-13}{3}<\frac43A.
$$



Its upper endpoint $20q$ is even.  Counting only the possible odd
integers $20q-1,20q-3,\ldots$ and using
$\delta\leq9$ gives the exact elementary bound



$$
m_q\leq\left\lfloor\frac{2A}{3}\right\rfloor.
$$



Also (39) gives the useful unconditional lower bound



$$
Q_q\geq\frac14\left(\frac{4q}{A}\right)^A.
$$



If $A$ stays bounded, then
$P_q<(20q)^{m_q}$ and $A-m_q\geq\lceil A/3\rceil>0$, so
(38) is smaller than $Q_q$ for all sufficiently large $q$.

Suppose next that $A\to\infty$ and $A=o(q)$.  When
$\log A\leq\tfrac14\log q$, the parity bound gives



$$
\log\{(2m_q+1)P_q\}
 \leq\frac{2A}{3}\log(20q)+O(\log A),
 \qquad
 \log Q_q\geq\frac{3A}{4}\log q-\log4,
$$



so the latter is larger.  In the complementary case, apply the explicit
Brun--Titchmarsh inequality



$$
\pi(x+y)-\pi(x)<\frac{2y}{\log y}\qquad(y>1)
$$



to this interval.  Since $Y_q=(4/3+o(1))A$, it yields



$$
m_q\leq\left(\frac83+o(1)\right)\frac{A}{\log A},
 \qquad
 \log\{(2m_q+1)P_q\}=O(A),
$$



where the second estimate uses
$\log A>\tfrac14\log q$.  But



$$
\frac{\log Q_q}{A}\geq\log\frac{4q}{A}-\frac{\log4}{A}
 \longrightarrow\infty,
$$



so the capacity again wins.  The short-interval inequality used here is
Theorem 2 of H. L. Montgomery and R. C. Vaughan,
[“The large sieve,” *Mathematika* 20 (1973), 119--134](https://doi.org/10.1112/S0025579300004708).

Finally, if the capacity inequality failed for infinitely many
admissible pairs $(q,A)$, compactness would give a subsequence on which
$A/q$ tends to a limit in $[0,3]$.  A positive limit is excluded by
(41)--(45).  At limit zero, pass once more to a subsequence on which
$A$ is bounded or tends to infinity; the preceding endpoint argument
excludes both.  Therefore, uniformly for every admissible integer
$1\leq A\leq3q-2$,



$$
(2m_q+1)P_q<Q_q                 \tag{46}
$$



for all sufficiently large $q$.

On $[0,1]$, $C_q\geq0,u^2\leq4,1-x^2\leq1$.
Equations (38), (39), and (46) therefore give



$$
0\leq u^2w_qC_q\leq1.           \tag{47}
$$



Since $0\leq B_q\leq1$, equation (15) proves (2).

## 7. Denominator conclusion

For every prime in (7), $p<20q=\operatorname {ord}_0h_q$, so the
prefix of $r_q$ is the prefix of $-1/u$.  In particular
$r_{p-2}=0$.  No class-zero channel occurs, and the two local equations
give



$$
\begin{aligned}
 r_{2p-2}&\equiv0,\\
 2r_{p-1}+r_{2p-1}&\equiv0,\\
 2s_{p-1}+s_{2p-1}&\equiv0\pmod p.                      \tag{48}
\end{aligned}
$$



For the first moment, only the monomial denominators $p,2p$ can be
divisible by $p$, giving the second line of (48).  For the second
moment, the criterion is
$2r_{p-2}+r_{2p-2}\equiv0$, which reduces to the first line.
Indeed, $3p>48q+k+13$ exceeds both relevant degree-plus-one bounds.
Similarly, by (6) and the lower endpoint of (7),



$$
\deg S_q+1<3p.                  \tag{49}
$$



so only denominators $p,2p$ occur in the full integral, and the third
line of (48) is its exact $p$-integrality criterion.  Every
window prime is absent from $D_q$, proving (7).

The prime number theorem gives



$$
\begin{aligned}
 \log P_q
 &=\vartheta(20q)-
   \vartheta\!\left(\frac{48q+k_q+13}{3}\right)\\
 &=4q-\frac{k_q}{3}+o(q),                               \tag{50}
\end{aligned}
$$



which proves (8).

## 8. Native Taylor correction and primitive-content audit

Let



$$
(1-i)^N=R_N+iI_N,\qquad M_N=N!-R_N,                    \tag{51}
$$



and use the exact linear defect correction



$$
K_N(x)=I_N-\frac{M_N}{2}(1-x).                          \tag{52}
$$



This is integral: for $N\geq2$, $(1-i)^N$ is divisible by
$(1-i)^2=-2i$ in $\mathbb Z[i]$, so $R_N$, and therefore
$M_N$, is even.

For every choice of $N=N(q)\geq2$, its degree is one, no matter how
large its factorial coefficients become.  The growing-correction theorem
therefore applies with



$$
E=2,\qquad A=3q-2,qquad
 \deg S_q+1=48q+14.                                     \tag{53}
$$



There is no need to exclude primes dividing $I_N$, $M_N$, or
$N!$.  Modulo such a prime, the adaptive response simply moves to a
different case in Section 5, or its full target becomes zero.

The unlocalized common residual is



$$
F_N^*=(1-x)^N+{\cal T}K_N.                              \tag{54}
$$



In fact, direct calculation gives



$$
{\cal T}K_N=-\frac{M_N}{2}u+(M_N-I_Nx).
$$



It follows at $x=\pm i$ that $F_N^*=N!$.  Hence the target-zero
quotient



$$
Q_N^*=\frac{F_N^*-N!}{u}\in\mathbb Z[x]
$$



has degree at most $N-2$, and its rational integral coordinate has
denominator dividing $\operatorname {lcm}(1,\ldots,N-1)$.
Consequently, if



$$
N-1<\frac{48q+14}{3},            \tag{55}
$$



then for the localized common polynomial



$$
F_{N,q}=(1-x)^N+{\cal T}(h_qK_N)                        \tag{56}
$$



the exact target-zero coordinate is



$$
Q_{N,q}=\frac{F_{N,q}-N!}{u}=Q_N^*+S_q.
$$



Its reduced rational integral $\int_0^1Q_{N,q}(x)\,dx$ has no
denominator prime in



$$
\frac{48q+14}{3}<p<20q.         \tag{57}
$$



This includes every diagonal $N=o(q)$, and in particular every regime
$q\gg N\log N$ previously used to dominate the factorial correction
height.

There is no hidden common polynomial content in (56).  Since
$\operatorname {ord}_0h_q=20q\geq2$,



$$
F_{N,q}(0)=1.                   \tag{58}
$$



Thus $F_{N,q}$ is primitive in $\mathbb Z[x]$.  Multiplying all of
its coefficients by a common scalar gives content exactly that scalar,
and taking the primitive part restores $F_{N,q}$.  Separately, under
(55), the reduced integral coordinate of $Q_{N,q}$ is already
window-prime-free.  Thus neither factorial coefficient height nor common
content of this native polynomial supplies the proposed window
obstruction.  This statement does not concern the content of a different
transformed or determinantal output.

This does not prove that (56) is nonnegative or that its weighted
integral tends to zero after exact normalization.  Those analytic and
global-content questions remain separate.

## 9. Replay and scope

The deterministic replay verifies:

* the Pascal determinant formula and its modular nonvanishing;
* a degree-$60$ correction whose reductions deliberately cycle through
  all four response cases at different primes;
* a correction of degree $300=10q$, testing a padding exponent close
  to the natural endpoint regime;
* a degree-$235=12q-17$ correction at $q=21$, for which $A=2$
  and the complete window consists of the single endpoint prime $419$;
* the native $N=200$ factorial-height linear correction;
* exact CRT reconstruction, forced top degree, positivity capacity,
  all three residue equations, reduced rational denominators, and the
  native base-output and content claims.

From the research directory run

    python3 scripts/common_kernel_growing_correction_full_window_certificate.py
    sha256sum -c results/common_kernel_growing_correction_full_window_hashes.sha256

Finite replay instances check normalization and implementation only.
The all-parameter degree range, rank theorem, entropy comparison, and
native-family conclusion are the proofs above.

The replay uses exact CPU arithmetic, no hardware accelerator, and a
small fraction of the available Colab RAM.  No conclusion about
$e+\pi$ is claimed.
