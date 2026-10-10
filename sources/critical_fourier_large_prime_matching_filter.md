> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# An exact first-digit filter for large-prime critical-Fourier matching

Date: 2026-08-27.

## 1. Outcome

Let $n>0$ be even, $K=k-1\ge n$, and retain the accepted critical
Fourier data



$$
G_{n,k}(y)=P_n(y)(1+y)^{2(K-n)},\qquad
 C_m=[y^{K+m}]G_{n,k}(y),
 \tag{1}
$$





$$
S_{n,k}=\sum_{m=1}^{K}\frac{N_m}{m},\qquad
 \frac{4S_{n,k}}{C_0}=\frac AB
 \quad\text{in lowest terms}.
 \tag{2}
$$



Let $p_n,q_n$ be the primitive exponential beta coefficients and let
$g_{n,k}$ be the final content after minimal matching.  This note gives
an exact first-$p$-adic-digit test for primes in the large-prime band



$$
\boxed{K<p\le2(K-n).}
 \tag{3}
$$



Every prime in (3) divides $C_0$.  If the first digit $C_0/p\pmod p$
does not vanish, then membership in $g_{n,k}$ is decided exactly by one
Bessel valuation and one explicit Fourier congruence.  The test explains,
rather than excludes, the known surviving primes $227,647,937>K$.

The theorem is a finite-state localization.  It is not a uniform bound on
$g_{n,k}$, because a second-order exceptional branch remains and because
primes outside (3) are not covered.

## 2. The two explicit Fourier digits

Let $p$ be an odd prime satisfying (3), and put



$$
s=2(K-n)-p,\qquad u=p-K,\qquad d=2n+s=2K-p.
 \tag{4}
$$



Then



$$
0\le s<p,\quad s\ \text{is odd},\quad
 1\le u\le K,\quad0\le d<K<p,
 \tag{5}
$$



and



$$
R(y):=P_n(y)(1+y)^s
      =\sum_{t=0}^{d}\rho_ty^t,
 \qquad \rho_t=a_t+ib_t\in\mathbb Z[i].
 \tag{6}
$$



All quantities below are reduced in $\mathbb F_p[i]$.  Define



$$
H_p(y)=\sum_{j=1}^{p-1}
          \frac{(-1)^{j-1}}j y^j
 \tag{7}
$$



and the central digit



$$
D_{n,K,p}:=[y^K]R(y)H_p(y)
 =\sum_{t=0}^{d}\rho_t
   \frac{(-1)^{K-t-1}}{K-t}.
 \tag{8}
$$



Although (8) is written in $\mathbb F_p[i]$, the theorem below shows
that its imaginary part is zero.  We therefore regard $D_{n,K,p}$ as an
element of $\mathbb F_p$.

For a Gaussian residue $\rho=a+ib$, put



$$
\nu_m(\rho)=
 a\sin\frac{m\pi}{2}
 -b\left(1-\cos\frac{m\pi}{2}\right)\in\mathbb F_p.
 \tag{9}
$$



The sine and cosine in (9) belong to $\{0,\pm1\}$, so this is only a
four-case integer definition.  Define the rational-coordinate digit



$$
U_{n,K,p}=\sum_{t=0}^{d}
 \frac{\nu_{u+t}(\rho_t)}{u+t}
 \in\mathbb F_p.
 \tag{10}
$$



Every denominator in (8) lies between $u$ and $K$, and every
denominator in (10) has the same property.  Hence all are nonzero modulo
$p$.

### Theorem 2.1

With the notation above,



$$
\boxed{
 \frac{C_0}{p}\equiv D_{n,K,p}\pmod p,
 \qquad
 S_{n,k}\equiv U_{n,K,p}\pmod p.}
 \tag{11}
$$



Suppose $D_{n,K,p}\ne0$.  Then



$$
\boxed{
 p\mid g_{n,k}
 \quad\Longleftrightarrow\quad
 \begin{cases}
  v_p(q_n)=1,\\
  U_{n,K,p}\ne0,\\
  4(q_n/p)U_{n,K,p}\equiv p_nD_{n,K,p}\pmod p.
 \end{cases}}
 \tag{12}
$$



Thus a surviving prime in (3) is either in the exceptional branch



$$
D_{n,K,p}=0,
 \tag{13}
$$



which is equivalent to $p^2\mid C_0$, or it passes all three exact tests
in (12).

## 3. Proof of the Fourier digit formulas

The definitions give the exact factorization



$$
G_{n,k}(y)=R(y)(1+y)^p.
 \tag{14}
$$



The binomial coefficients satisfy



$$
\frac1p\binom pj
 =\frac1j\binom{p-1}{j-1}
 \equiv\frac{(-1)^{j-1}}j\pmod p
 \qquad(1\le j<p).
 \tag{15}
$$



Consequently, over $(\mathbb Z[i]/p^2\mathbb Z[i])[y]$,



$$
(1+y)^p\equiv1+y^p+pH_p(y)\pmod{p^2}.
 \tag{16}
$$



Because $d<K<p$, neither $R(y)$ nor $y^pR(y)$ has a term of degree
$K$.  Taking the central coefficient in (14)--(16) gives



$$
C_0\equiv p[y^K]R(y)H_p(y)\pmod{p^2},
 \tag{17}
$$



which proves the first congruence in (11).  It also proves that (8) is
real modulo $p$, because $C_0$ is an ordinary integer.

Reduction of (14) only modulo $p$ gives



$$
G_{n,k}(y)\equiv R(y)(1+y^p)\pmod p.
 \tag{18}
$$



For $1\le m<u$, the exponent $K+m$ lies strictly between $d$ and
$p$, so



$$
C_m\equiv0\pmod p.
 \tag{19}
$$



For $u\le m\le K$, the same coefficient comes from $y^pR(y)$, and



$$
C_m\equiv\rho_{m-u}\pmod p.
 \tag{20}
$$



Since $p>K$, all denominators $1,\ldots,K$ are $p$-adic units.
Substitution of (19)--(20) into the definition of $S_{n,k}$ gives the
second congruence in (11).

It remains to prove (12).  Put



$$
c=v_p(C_0),\qquad \sigma=v_p(S_{n,k}).
$$



The accepted exact denominator formula is



$$
v_p(B)=\max(0,c-\sigma).
 \tag{21}
$$



If $D_{n,K,p}\ne0$, the first congruence in (11) gives $c=1$.
If $U_{n,K,p}=0$, the second gives $\sigma\ge1$, hence $v_p(B)=0$
and $p\nmid g_{n,k}$.  If $U_{n,K,p}\ne0$, then $\sigma=0$ and
$v_p(B)=1$.  The exact odd matching-localization theorem now says that
$p$ can survive only if $v_p(q_n)=v_p(B)=1$, and in that case



$$
p\mid g_{n,k}
 \quad\Longleftrightarrow\quad
 v_p(4q_nS_{n,k}-p_nC_0)\ge2.
 \tag{22}
$$



Divide the expression in (22) by $p$ and apply (11).  The resulting
congruence is exactly the third line of (12).  Every implication used here
is reversible, proving the equivalence.  Equation (17) also proves the
equivalence asserted after (13).  $\square$

## 4. Reflection of the Bessel root classes

The existing period congruence can be supplemented by a reflection that
is useful when applying (12).

### Lemma 4.1

For every odd integer $M\ge3$ and $0\le r<M$,



$$
\boxed{
 p_{M-1-r}\equiv p_r\pmod M,
 \qquad q_{M-1-r}\equiv q_r\pmod M.}
 \tag{23}
$$



In particular, the root set of $q_r\pmod{p^a}$ is invariant under
$r\mapsto p^a-1-r$.

### Proof

The exact period theorem gives, because $M$ is odd,



$$
(p_M,p_{M+1})\equiv(1,3),\qquad
 (q_M,q_{M+1})\equiv(-1,-1)\pmod M.
 \tag{24}
$$



Run the recurrence



$$
X_j=(4j-2)X_{j-1}+X_{j-2}
 \tag{25}
$$



backward twice.  Equation (24) gives



$$
(p_{M-1},p_{M-2})\equiv(1,3),\qquad
 (q_{M-1},q_{M-2})\equiv(1,1)\pmod M.
 \tag{26}
$$



For $Y_r=X_{M-1-r}$, rearranging (25) at index $M-r$ gives



$$
Y_{r+1}\equiv(4r+2)Y_r+Y_{r-1}\pmod M,
 \tag{27}
$$



which is the original recurrence at index $r+1$.  The initial states in
(26) match those at indices $0,1$, so induction proves (23).
$\square$

## 5. The known large-prime survivors

The three certified examples with a surviving prime larger than $K$ all
lie in (3), have $D,U\ne0$, and pass (12).  The exact residues are



$$
\begin{array}{c|c|c|c|c|c|c}
(n,K,p)&D&U&q_n/p&p_n&4(q_n/p)U&p_nD\\ \hline
(72,189,227)&163&112&88&65&153&153\\
(92,442,647)&261&240&324&277&480&480\\
(64,797,937)&257&463&601&397&833&833
\end{array}
\pmod p.
 \tag{28}
$$



In every row $v_p(q_n)=1$.  Thus the known counterexamples are on the
generic first-digit branch, not hidden in the exception (13).

## 6. Exact finite-grid certificate

The companion script reconstructs the unreduced Fourier data over
$\mathbb Z[i]$, computes $A,B,g_{n,k}$ exactly, and independently
computes the two residues $D,U$.  On the grid



$$
2\le n\le12\quad(n\ \mathrm{even}),\qquad n\le K\le160,
 \tag{29}
$$



it checks 12,223 prime instances from (3), spread over 864 parameter
pairs.  In every instance it verifies both congruences in (11).  On the
generic branch it verifies the equivalence (12) against the final content
computed from the primitive integer coefficients.

The grid contains 83 instances of $D=0$, three instances in which a
simple Bessel root is rejected by the last congruence in (12), and one
generic survivor, $(n,K,p)=(2,6,7)$.  These counts are finite diagnostic
facts, not density estimates.  The script separately checks 51,840
reflection congruences for all odd moduli through $321$, and checks the
three large examples in (28).

Run

    python -m py_compile scripts/critical_fourier_large_prime_matching_filter_certificate.py
    python scripts/critical_fourier_large_prime_matching_filter_certificate.py

For a byte-identical rerun, use

    python scripts/critical_fourier_large_prime_matching_filter_certificate.py \
      --output /tmp/critical_fourier_large_prime_matching_filter_certificate.json
    cmp results/critical_fourier_large_prime_matching_filter_certificate.json \
      /tmp/critical_fourier_large_prime_matching_filter_certificate.json

The all-parameter result is the proof in Sections 2--4; the grid only
checks normalization, indices, and the exact local equivalence.

## 7. Limitations

Equation (12) is exact whenever $D\ne0$, but it does not bound how often
the Bessel root and Fourier digit congruence can coincide.  The condition
$D=0$ requires a second-order expansion of the central coefficient.
Primes $p\le K$ require the separate multi-block analysis, while primes
$p>2(K-n)$ can divide $C_0$ only through additional arithmetic not
forced by the one-block gap.

Nothing in this note proves a uniform upper bound for $g_{n,k}$, and
nothing proves that $e+\pi$ is algebraic, transcendental, rational, or
irrational.
