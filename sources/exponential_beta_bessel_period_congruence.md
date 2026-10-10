> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# An exact period congruence for the exponential beta coefficients

Date: 2026-08-27.

## 1. Theorem

For every integer $n\ge0$, the accepted exponential beta integral has
the exact endpoint evaluation



$$
\frac1{n!}\int_0^1x^n(1-x)^ne^x\,dx
 =(-1)^n(q_ne-p_n)>0.
 \tag{1}
$$



Thus $q_ne-p_n$ is positive for even $n$ and negative for odd $n$.
In the critical-Fourier construction, where $n$ is even, we write
$E_n=q_ne-p_n>0$.  The integer endpoint coefficients valid for every
$n$ are



$$
p_n=\sum_{j=0}^n\frac{(n+j)!}{j!(n-j)!},
 \qquad
 q_n=(-1)^n\sum_{j=0}^n(-1)^j
 \frac{(n+j)!}{j!(n-j)!}.
 \tag{2}
$$



Both satisfy



$$
X_n=2(2n-1)X_{n-1}+X_{n-2},
 \tag{3}
$$



with



$$
(p_0,p_1)=(1,3),\qquad(q_0,q_1)=(1,1).
 \tag{4}
$$



For every pair of integers $m\ge1$ and $n\ge0$,



$$
\boxed{
 p_{n+m}\equiv p_n\pmod m,\qquad
 q_{n+m}\equiv(-1)^m q_n\pmod m.}
 \tag{5}
$$



In particular, if $\ell$ is an odd prime and $a\ge1$, then



$$
p_{n+\ell^a}\equiv p_n\pmod{\ell^a},\qquad
 q_{n+\ell^a}\equiv-q_n\pmod{\ell^a}.
 \tag{6}
$$



Thus the roots of $q_n$ modulo every odd prime power repeat with period
$\ell^a$, up to the irrelevant sign in (6).

## 2. Proof

Put



$$
a_{r,j}=\frac{(r+j)!}{j!(r-j)!}
 =\binom{r+j}{j}\,r(r-1)\cdots(r-j+1).
 \tag{7}
$$



For $r=m$, every term $a_{m,j}$ with $j\ge1$ contains the integer
factor $m$.  Equation (2) therefore gives



$$
p_m\equiv1\pmod m,\qquad
 q_m\equiv(-1)^m\pmod m.
 \tag{8}
$$



For $r=m+1$, the $j=0$ term is one and



$$
a_{m+1,1}=(m+2)(m+1)\equiv2\pmod m.
$$



Every $a_{m+1,j}$ with $j\ge2$ contains $m$ in the falling product in
(7).  Consequently,



$$
p_{m+1}\equiv1+2=3\pmod m,
 \tag{9}
$$



and



$$
q_{m+1}
 \equiv(-1)^{m+1}(1-2)
 =(-1)^m\pmod m.
 \tag{10}
$$



The recurrence coefficient is periodic modulo $m$:



$$
2(2(n+m)-1)\equiv2(2n-1)\pmod m.
 \tag{11}
$$



Equations (8)--(10) say that, at indices $m,m+1$, the $p$-solution has
the same initial state modulo $m$ as at $0,1$, while the $q$-solution
has $(-1)^m$ times its initial state.  Induction in the common recurrence
(3), using (11), proves (5) for every $n\ge0$.  $\square$

## 3. Prime-power root-class consequence

Fix an odd prime power $M=\ell^a$, and write



$$
n=tM+r,\qquad0\le r<M.
 \tag{12}
$$



Repeated application of (5) gives



$$
p_n\equiv p_r\pmod M,\qquad
 q_n\equiv(-1)^tq_r\pmod M.
 \tag{13}
$$



Hence



$$
\boxed{
 \ell^a\mid q_n
 \quad\Longleftrightarrow\quad
 \ell^a\mid q_{\,n\bmod\ell^a}.}
 \tag{14}
$$



If $\ell^a$ divides the final matching content $g_{n,k}$ in the
critical-Fourier construction, then necessarily $\ell^a\mid q_n$.
Equation (14) therefore restricts $n$ to the finite root set



$$
\mathcal R_{\ell^a}
 =\{0\le r<\ell^a:q_r\equiv0\pmod{\ell^a}\}.
 \tag{15}
$$



Moreover, the normalized matching congruence may replace $p_n$ by $p_r$
modulo $\ell^a$, by (13).  This gives an exact finite-state reduction of
the Bessel side of the odd-content problem.

## 4. What the theorem does not imply

Equation (14) does not bound the size or number of the root classes
$\mathcal R_{\ell^a}$, and it does not show that roots fail to lift to
higher powers.  Indeed, the exact beta sequence has examples



$$
7^3\mid q_{18},\qquad
 7^4\mid q_{361},\qquad
 11^5\mid q_{1359}.
 \tag{16}
$$



The critical-Fourier matching certificate also has
$7^3\mid g_{18,1004}$.  Thus (5) is a structural congruence and a
finite-state reduction, not a uniform upper bound on $v_\ell(q_n)$ or
$v_\ell(g_{n,k})$.  Closing the odd-content problem still requires
combining the root classes (15) with the independent Fourier congruence for
$C_0$ and $S_{n,k}$.

## 5. Exact diagnostic

The companion script checks (5) for



$$
1\le m\le160,\qquad0\le n\le320,
$$



using exact integer recurrence values.  It separately checks the
prime-power examples in (16) and their shifted roots using modular
recurrence arithmetic.

Run

    python -m py_compile scripts/exponential_beta_bessel_period_congruence_certificate.py
    python scripts/exponential_beta_bessel_period_congruence_certificate.py

For a byte-identical rerun, use

    python scripts/exponential_beta_bessel_period_congruence_certificate.py \
      --output /tmp/exponential_beta_bessel_period_congruence.json
    cmp results/exponential_beta_bessel_period_congruence.json \
      /tmp/exponential_beta_bessel_period_congruence.json

The calculation is diagnostic only; the all-$m,n$ proof is the elementary
argument in Section 2.  Nothing in this note proves an arithmetic
classification of $e+\pi$.
