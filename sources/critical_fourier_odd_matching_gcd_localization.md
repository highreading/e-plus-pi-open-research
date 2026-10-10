> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact localization of the odd matching content in the critical Fourier family

Date: 2026-08-26.

## 1. Scope and outcome

Let $n>0$ be even, put $K=k-1$, and suppose $k>n$.  Retain the
accepted exact Fourier coordinates



$$
J_{n,k}=2^{-2K}\left(S_{n,k}+\frac{C_0}{4}\pi\right),
 \qquad
 S_{n,k}=\sum_{m=1}^{K}\frac{N_m}{m}=\frac{T_{n,k}}{L_K},
 \qquad
 L_K=\operatorname{lcm}(1,\ldots,K).
 \tag{1}
$$



Write the coordinate ratio in lowest terms as



$$
\frac{4S_{n,k}}{C_0}=\frac AB,
 \qquad A\in\mathbb Z,\quad B\in\mathbb Z_{>0},\quad \gcd(A,B)=1.
 \tag{2}
$$



Let



$$
E_n=q_ne-p_n>0,
 \qquad \gcd(p_n,q_n)=1,
 \tag{3}
$$



be the accepted primitive exponential beta form.  Put



$$
d=\gcd(q_n,B),\qquad q_n=dq_0,\qquad B=dB_0,
 \tag{4}
$$



and let



$$
M=q_0A-B_0p_n,
 \qquad
 C=\frac{q_nB}{d}=dq_0B_0
 \tag{5}
$$



be the constant and common target coefficient after minimal matching.  The
accepted matching lemma gives



$$
g:=\gcd(M,C)=\gcd(M,d).
 \tag{6}
$$



This note sharpens (6) prime power by prime power.  For every odd prime
$\ell$, put



$$
\alpha=v_\ell(q_n),\qquad
 \beta=v_\ell(B).
 \tag{7}
$$



Then



$$
\boxed{\alpha\ne\beta\quad\Longrightarrow\quad v_\ell(g)=0.}
 \tag{8}
$$



If $\alpha=\beta=a>0$, then



$$
\boxed{
 v_\ell(g)
 =\min\left\{
 a,
 v_\ell\!\left(
 4\frac{q_n}{\ell^a}\frac{\ell^aS_{n,k}}{C_0}-p_n
 \right)
 \right\}.}
 \tag{9}
$$



The expression inside the valuation in (9) is an $\ell$-adic integer.
Thus a prime can survive in the final content only after two independent
conditions: its exponent in $B$ must equal its *full* exponent in $q_n$,
and a further normalized congruence must hold.

Equations (8)--(9) are exact, but they are not by themselves a useful global
upper bound.  Exact counterexamples show that $g$ need not be one, prime,
or squarefree, need not divide $\operatorname{rad}(q_n)$, and can contain a
prime larger than $K$.  In particular,



$$
(n,k,d,g)=(4,40,1001,143),\quad(8,110,169,169),
 \quad(18,1004,343,343),
 \tag{10}
$$



and



$$
(n,k,d,g)=(72,190,17479,227),\quad
 (92,443,78287,647),\quad(64,798,937,937),
 \tag{11}
$$



where the surviving primes in (11) satisfy respectively



$$
227>189=K,\qquad647>442=K,\qquad937>797=K.
 \tag{12}
$$



These are finite exact obstructions to several tempting shortcuts; they do
not disprove the possibility of a subtler asymptotic bound for $g$.

## 2. The prime-power localization theorem

### Theorem 2.1

With the notation above, let $\ell$ be any prime divisor of $d$.  Then
$\ell$ is odd, and equations (8)--(9) hold.  More explicitly, if
$\alpha=\beta=a>0$, then



$$
v_\ell(g)
 =\min\{a,v_\ell(q_nA-p_nB)-a\}.
 \tag{13}
$$



Moreover,



$$
\gcd(g,q_0B_0)=1,\qquad dg\mid q_nA-p_nB,\qquad
 g^2\mid q_nA-p_nB.
 \tag{14}
$$



### Proof

The accepted $2$-adic theorem proves that $B$, $p_n$, and $q_n$ are
odd, hence so are $d$ and $g$.  Fix an odd prime $\ell\mid d$.

If $\alpha>\beta$, then



$$
v_\ell(d)=\beta,\qquad \ell\mid q_0,\qquad \ell\nmid B_0p_n.
$$



Reduction of (5) modulo $\ell$ gives



$$
M\equiv-B_0p_n\not\equiv0\pmod\ell,
$$



where $\ell\nmid p_n$ follows from $\gcd(p_n,q_n)=1$.  Thus
$v_\ell(g)=0$.  If $\beta>\alpha$, then



$$
\ell\mid B_0,qquad \ell\nmid q_0A,
$$



because $\gcd(A,B)=1$.  Hence



$$
M\equiv q_0A\not\equiv0\pmod\ell,
$$



and again $v_\ell(g)=0$.  This proves (8).

Suppose now that $\alpha=\beta=a>0$.  Then $q_0$ and $B_0$ are both
$\ell$-adic units, while



$$
q_nA-p_nB=\ell^a(q_0A-p_nB_0)=\ell^aM.
 \tag{15}
$$



Equation (6) therefore gives (13).

To rewrite (13) intrinsically in the Fourier coordinates, observe from (2)
that



$$
\ell^a\frac{4S_{n,k}}{C_0}
 =\ell^a\frac AB=\frac A{B_0}\in\mathbb Z_\ell^\times.
 \tag{16}
$$



Multiplication of the expression in (9) by the unit $B_0$ gives exactly
$M$.  This proves (9), including its integrality assertion.

The same reductions show that no prime divisor of $q_0B_0$ divides $M$,
so $\gcd(g,q_0B_0)=1$.  Finally (15), $g\mid M$, and $g\mid d$ imply
the last two divisibilities in (14).  $\square$

## 3. A formula using only unreduced Fourier data

For an odd prime $\ell$, put



$$
\lambda=v_\ell(L_K),\qquad
 c=v_\ell(C_0),\qquad
 \sigma=v_\ell(S_{n,k}),
 \tag{17}
$$



with $v_\ell(0)=+\infty$.  Since $A/B=4S/C_0$ is reduced and
$v_\ell(4)=0$,



$$
\boxed{\beta=v_\ell(B)=\max(0,c-\sigma).}
 \tag{18}
$$



Consequently the complete local test is as follows.  Set



$$
a=v_\ell(q_n),\qquad b=\max(0,c-\sigma).
$$



If $a\ne b$, then $v_\ell(g)=0$.  If $a=b>0$, then (9) is
equivalently



$$
\boxed{
 v_\ell(g)
 =\min\left\{a,
 v_\ell(4q_nS_{n,k}-p_nC_0)-c
 \right\}.}
 \tag{19}
$$



Since $S=T/L_K$, the entirely integral version is



$$
\boxed{
 v_\ell(g)
 =\min\left\{a,
 v_\ell(4q_nT_{n,k}-p_nL_KC_0)-\lambda-c
 \right\}}
 \tag{20}
$$



when $a=b>0$, and zero otherwise.  In particular, for $1\le t\le a$,



$$
\ell^t\mid g
 \quad\Longleftrightarrow\quad
 \begin{cases}
 v_\ell(q_n)=v_\ell(B)=a,\\
 4q_nT_{n,k}\equiv p_nL_KC_0
 \pmod{\ell^{\lambda+c+t}}.
 \end{cases}
 \tag{21}
$$



Equation (21) is the exact hypergeometric/Fourier congruence left by the odd
content problem.  Here $q_n$ has either of the exact forms



$$
q_n=(-1)^n\sum_{j=0}^{n}(-1)^j
 \frac{(n+j)!}{j!(n-j)!},
 \qquad
 q_n=2(2n-1)q_{n-1}+q_{n-2},
 \tag{22}
$$



with $q_0=q_1=1$, while



$$
C_0=\sum_{j=0}^{n/2}\binom n{2j}
 \frac{(n+2j)!(2K-n-2j)!}
 {(n/2+j)!(K-n/2-j)!K!}
 \tag{23}
$$



is the accepted super-Catalan sum, and $T_{n,k}$ is the exact Fourier
harmonic sum in (1).  Thus (21)--(23) reduce the question to explicit
prime-power congruences.  A resultant involving only $q_n$ and $C_0$
cannot by itself decide $g$: the exact exponent match also depends on
$v_\ell(S)$, and the survival test uses the first normalized quotients in
(19) or (20).

## 4. Exact counterexamples

The companion certificate reconstructs $G_{n,k}(y)$ over
$\mathbb Z[i]$, obtains $C_0,T,A,B$ exactly, constructs the beta pair by
the recurrence (22), and verifies (8)--(9) for every prime dividing $d$ in
each recorded case.

The smallest examples establish logically distinct failures.

* At $(n,k)=(4,40)$,
  

$$
q_4=1001=7\cdot11\cdot13,\qquad d=1001,\qquad
  g=143=11\cdot13.
$$


  Thus $g$ can contain distinct odd primes.  The prime $7$ is excluded
  by the exact exponent mismatch $v_7(q_4)=1\ne2=v_7(B)$.
* At $(n,k)=(8,110)$, $d=g=13^2$.  Thus $g$ need not be squarefree and
  need not divide $\operatorname{rad}(q_n)$.
* At $(n,k)=(18,1004)$, $d=g=7^3$.  Here the normalized congruence in
  (9) actually has valuation $5$, so all three available powers survive.
* At $(n,k)=(64,798)$, $d=g=937$ although $937>K=797$.  The other two
  examples in (11) independently exhibit the same failure of a
  prime-support cutoff at $K$.

These examples also show why the exact valuation condition in (8) is useful:
large pieces of $d$ can disappear immediately when the exponents differ.
They do not, however, give an asymptotic upper bound on the remaining
exact-match part.

## 5. Reproduction and limitation

From the archive root, run

    python -m py_compile scripts/critical_fourier_odd_matching_gcd_certificate.py
    python scripts/critical_fourier_odd_matching_gcd_certificate.py

For a byte-identical rerun without replacing the archived result, run

    python scripts/critical_fourier_odd_matching_gcd_certificate.py \
      --output /tmp/critical_fourier_odd_matching_gcd_certificate.json
    cmp results/critical_fourier_odd_matching_gcd_certificate.json \
      /tmp/critical_fourier_odd_matching_gcd_certificate.json

The theorem localizes the remaining obstruction exactly and rules out several
false simplifications.  It does not prove a useful uniform upper bound for
$g$, does not close the high-$k$ matched family, and does not prove any
arithmetic classification of $e+\pi$.
