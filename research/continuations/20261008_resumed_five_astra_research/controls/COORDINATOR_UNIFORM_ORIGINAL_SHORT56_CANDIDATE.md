> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A uniform 56-coefficient source representative on the original family

Coordinator derivation, 9 October 2026. Full proof supplied; a DIFFERENT
external audit is pending. This proof uses the already established old
ternary unit/scalar theorem. It does NOT depend on the new precision-local
candidate or on freezing higher input digits. The numerical coefficients
themselves remain variable along the original progression.

## 1. Reuse and overlap scope

The exact search for56-coefficient representatives, V54 and the three
critical omitted coefficients covers all Desktop continuations, mathematical
sources and work, and the current work. The only relevant match is the
earlier parent deduction from the saved single-index jet. The other two
matches are the same unrelated256-coefficient dyadic endpoint report.
The original72-coefficient source theorem, finite modulo3 Pascal blocks,
actual scalar integrality and complete stationary Schur payment are REUSED.
The characteristic3 binomial identity below is proved directly; no new
external Lucas or Bessel theorem is imported. The existing primary-source
Bessel/Pascal gates cover the reused background.

## 2. Actual coefficients and the finite inverse modulo3

Put $N=n-1=4^j$, with the original $j=84645\pmod{531441}$. Thus
$v_3(N-1)=5$ and $n=2\pmod3$. Retain the COMPLETE definitions


$$
u_a=N!(-2)^a/a!,\quad v=T_n^{-1}u,\quad h=T_n^{-1}k,
$$




$$
t=3nh+(b_{\rm force}+6)e_N+
          2b_{\rm force}e_{N-1}/N,
\qquad q_a=-\frac{N!}{a!}(t_a+\xi v_a).
$$


REUSE $T_n^{-1}\in\operatorname{Mat}(\mathbb Z_3)$ and
$\xi\in\mathbb Z_3$. Hence all force entries are ternary integral.

Modulo3, u is supported at its last two coordinates, with both entries1.
For the literal finite lower Pascal matrix P,


$$
\widehat u=P^{-1}u\equiv e_{N-1}\pmod3.
$$


REUSE the complete finite transformed block theorem modulo3. The actual
last block is


$$
B_2=\begin{pmatrix}1&2\\2&0\end{pmatrix},\qquad
B_2^{-1}=\begin{pmatrix}0&2\\2&2\end{pmatrix}\quad\text{in }\mathbb F_3.
$$


All earlier blocks are uncoupled at this precision. Consequently


$$
\widehat v=\widehat T_n^{-1}\widehat u\equiv2e_N\pmod3,
$$


and the exact finite inverse Pascal reconstruction gives, for EVERY
$0\le a\le N$,


$$
\boxed{v_a\equiv2(-1)^{N-a}\binom Na\pmod3.}                 \tag{1}
$$


This retains the complete dense raw inverse vector; it is not a statement
that v has short support.

## 3. Pay the three borderline omitted coefficients

For d=56,57,58, set a=N-d. There are no explicit endpoint force constants
in t_a, so $t_a=3nh_a$. Since N=1mod9, write N=9K+1. In characteristic3,


$$
(1+z)^N=(1+z)(1+z^9)^K.
$$


The coefficients with degree2,3,4mod9 are zero. These are precisely the
residues of d=56,57,58, so


$$
\binom Nd\equiv0\pmod3.
$$


By(1), $v_{N-d}\in3\mathbb Z_3$. Hence the COMPLETE force bracket
$t_{N-d}+\xi v_{N-d}$ is divisible by3.

The exact factorial quotients for these three d have valuation31:


$$
v_3\left(\frac{N!}{(N-d)!}\right)
=5+v_3((d-2)!)=31,\qquad d=56,57,58.
$$


The equality uses $v_3(N-r)=v_3(r-1)$ for2<=r<=57, whose latter
valuations are strictly below5. Therefore


$$
q_{N-56},q_{N-57},q_{N-58}\in3^{32}\mathbb Z_3.
$$


At d=59 the factorial quotient alone has valuation


$$
5+v_3(57!)=5+19+6+2=32.
$$


Every more distant quotient contains this same product. All force brackets
remain integral, so


$$
\boxed{q_a\in3^{32}\mathbb Z_3\quad(0\le a\le N-56).}     \tag{2}
$$


No original factorial or matrix computation is required for this proof.

## 4. The actual same-index V54 and complete projection

Keep the original LAST56 coefficients:


$$
P_{55}(x)=\sum_{r=0}^{55}q_{N-55+r}x^r,
\qquad \delta Q=x^{N-55}P_{55}+L,\quad L\in3^{32}\mathbb Z_3[x].
$$


The exact retained endpoint is
$\delta Q(-1)=-\xi(N!)^2$, which is in3^32 for sufficiently large
original N. At x=-2 the factor x^(N-55) is a ternary unit, so
$P_{55}(-2)\in3^{32}\mathbb Z_3$. Monic division gives the ACTUAL
same-index degree54 polynomial


$$
V_{54}(x)=\sum_{b=0}^{54}x^b
       \sum_{r=b+1}^{55}(-2)^{r-b-1}q_{N-55+r},
$$


and therefore


$$
\boxed{\delta Q-(y+1)x^{A-54}V_{54}(x)
       \in3^{32}\mathbb Z_3[x],\qquad x=y-1.}              \tag{3}
$$


All coefficients are the original rational coefficients, ternary integral;
this does not assert integrality at other primes or replace the actual xi
by a low-digit constant.

REUSE the complete stationary projection bound. At the same physical
cutoff, M maps admitted ternary-integral polynomials to Z3, complete
corrected columns cost at most3^-1, and the full W inverse retains its
3^-1 allowance after a3^32-small perturbation. Its stationary linear term
has depth at least30; each cross vector has depth at least31, so its full
returned quadratic has depth at least61. Thus replacing deltaQ by(3)
changes the COMPLETE finite Schur matrix by3^30, and the normalized prefix
matrix, divided by3^26, by3^4. It preserves that matrix modulo81 and the
actual next prefix quotient divided by3^29 modulo3.

The true W space, its physical Y_m terminal and all LOW/HIGH feedback
remain literal. The complete returned source expression is still to be
evaluated; shrinking the producer does not shrink its corrected columns.

## 5. Relation to the existing coefficient receipt

The saved j84645 72-entry jet has16 leading zero coefficients modulo3^32
and hence yields precisely this56-entry representative. The earlier
extraction certificate independently validates its monic division without
rerunning the solver. Formula(2) now proves the WIDTH uniformly on the
original progression. It does not prove that all56 coefficient VALUES
are constant on that progression. The previously frozen j84645+3^38t
subfamily still supplies those particular saved coefficient values,
conditionally on the separate precision-local proof.

No complete Schur value, terminal-vector value, global all-prime gcd,
primitive denominator or unconditional e+pi theorem is claimed here.
