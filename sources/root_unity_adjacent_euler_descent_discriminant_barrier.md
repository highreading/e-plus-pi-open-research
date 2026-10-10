> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Adjacent Euler descent and the discriminant barrier

## Exact squarefull support, a fourth-order modular root, and why the natural elimination is too large

Checked: 2026-08-27 UTC

## 1. Scope and conclusions

Let the secant Euler numbers be defined by



$$
\operatorname {sech}z=\sum_{j\geq0}E_j{z^j\over j!},
 \qquad E_{2j+1}=0,
                                                               \tag{1}
$$



and put



$$
\begin{aligned}
 A_N&=(2N+2)(2N+1),\\
 G_N&=\gcd\!\left(A_N|E_{2N}|,|E_{2N+2}|\right),\\
 Q_N&={A_N|E_{2N}|\over G_N},
 \qquad h_N=\gcd(Q_N,Q_{N+1}).
 \end{aligned}                                                \tag{2}
$$



This note proves two all-parameter structural statements.

First, away from primes dividing the two explicit index factors
$A_NA_{N+1}$, every prime in $h_N$ is supported on a strict
three-term descent of Euler valuations.  If $h_N^{\rm off}$ denotes the
largest divisor of $h_N$ supported away from $A_NA_{N+1}$, then



$$
\boxed{(h_N^{\rm off})^2\mid |E_{2N}|.}                    \tag{3}
$$



There is also the global, index-inclusive divisibility



$$
\boxed{h_N^2\mid A_NA_{N+1}|E_{2N}|.}                     \tag{4}
$$



In particular, an off-index prime in $h_N$ must divide
$E_{2N}$ at least twice and $E_{2N+2}$ at least once.  This is a
genuine squarefull-layer restriction, but (3) gives only a square-root
upper bound and is far too weak for the neighboring-denominator problem.

Second, simultaneous divisibility of $E_{M-2}$ and $E_M$, with
$M$ even, makes zero a fourth-order root modulo the common divisor of a
centered Euler polynomial.  The associated exact discriminant identity
gives a cubic divisibility statement.  Nevertheless the discriminant has
logarithmic height $O(M^2\log M)$, whereas the original common divisor
already has the sharper trivial ledger $O(M\log M)$.  Thus the natural
discriminant and Sylvester-subresultant routes lose a factor of order
$M$ in the exponent.

These statements do not bound the first-period factor $J_N$ from the
quadratic Euler--Kummer decomposition by $\exp(o(N\log N))$.  They also
do not prove or disprove that $e+\pi$ is transcendental.

## 2. The exact three-valuation descent

For a prime $p$, abbreviate



$$
\begin{aligned}
 b&=v_p(A_N),&c&=v_p(A_{N+1}),\\
 x&=v_p(E_{2N}),&y&=v_p(E_{2N+2}),&z&=v_p(E_{2N+4}).
 \end{aligned}                                                \tag{5}
$$



Reduction of the two fractions in (2) gives exactly



$$
\begin{aligned}
 v_p(Q_N)&=(b+x-y)_+,\\
 v_p(Q_{N+1})&=(c+y-z)_+,\\
 t_p:=v_p(h_N)&=\min\!\left((b+x-y)_+,(c+y-z)_+\right),
 \end{aligned}                                                \tag{6}
$$



where $u_+=\max(u,0)$.  This formula includes every prime, including
the index primes and $p=2$.

Define the index-prime set and the corresponding support decomposition by



$$
\begin{aligned}
 \mathcal I_N&=\{p:\ p\mid A_NA_{N+1}\},\\
 h_N^{\rm idx}&=\prod_{p\in\mathcal I_N}p^{t_p},
 &h_N^{\rm off}&=\prod_{p\notin\mathcal I_N}p^{t_p}.
 \end{aligned}                                                \tag{7}
$$



Thus $h_N=h_N^{\rm idx}h_N^{\rm off}$ and the two factors are
coprime.  This is a support decomposition: at an index prime, (6), rather
than a claim that all of its valuation comes from $A_NA_{N+1}$, is the
exact statement.

If $p\notin\mathcal I_N$, then $b=c=0$.  A positive $t_p$ in
(6) is therefore equivalent to



$$
x>y>z.                              \tag{8}
$$



In that case



$$
2t_p\leq x-z\leq x.                     \tag{9}
$$



This proves (3) prime by prime.  It also proves the sharper support
assertion



$$
p\mid h_N^{\rm off}\quad\Longrightarrow\quad
 p^2\mid E_{2N},\qquad p\mid E_{2N+2}.                     \tag{10}
$$



For an arbitrary prime with $t_p>0$, add the two inequalities implicit
in (6).  Since $z\geq0$,



$$
2t_p\leq b+c+x-z\leq b+c+x.                  \tag{11}
$$



This proves (4), again prime by prime.

The prime 2 is completely explicit.  Every secant Euler number is odd,
so $x=y=z=0$ at $p=2$, while



$$
v_2(A_N)=1+v_2(N+1),\qquad
 v_2(A_{N+1})=1+v_2(N+2).                                  \tag{12}
$$



Exactly one of $N+1,N+2$ is odd.  Hence



$$
v_2(h_N)=1.                      \tag{13}
$$



Odd index primes remain governed by the full formula (6); deleting
$b,c$ there would be invalid.  Finally, the beta formula and Stirling's
formula give $\log|E_{2N}|=2N\log N+O(N)$.  Equations (3)--(4) imply
only



$$
\log h_N^{\rm off}\leq N\log N+O(N),\qquad
 \log h_N\leq N\log N+O(N).                               \tag{14}
$$



This square-root scale is not a subexponential estimate and does not close
the Richardson or two-regime construction.

## 3. Adjacent Euler divisibility as a fourth-order root

Let $M=2m\geq4$, and define the centered integer Euler polynomial



$$
\mathcal F_M(T)=
 \sum_{j=0}^{M}\binom MjE_jT^{M-j}
 =2^M\mathcal E_M\!\left({T+1\over2}\right),              \tag{15}
$$



where $\mathcal E_M(X)$ is the ordinary Euler polynomial.  Since the
odd secant Euler numbers vanish, $\mathcal F_M$ is monic and even.  Write



$$
\mathcal F_M(T)=f_M(T^2),\qquad
 f_M(Y)=\sum_{k=0}^{m}\binom M{2k}E_{M-2k}Y^k.              \tag{16}
$$



Then $f_M$ is monic of degree $m$, and



$$
f_M(0)=E_M,qquad
                 f_M'(0)=\binom M2E_{M-2}.                  \tag{17}
$$



Let $d$ be any positive common divisor of $E_M$ and $E_{M-2}$.
Equations (16)--(17) give the exact congruences



$$
\boxed{\mathcal F_M(T)\equiv T^4V(T)\pmod d,qquad
        f_M(Y)\equiv Y^2W(Y)\pmod d}                       \tag{18}
$$



for integer polynomials $V,W$.  Thus zero is a root of order at least
four in the $T$-coordinate and at least two in the $Y$-coordinate
over $\mathbb Z/d\mathbb Z$.  In particular, every prime-power layer
in the adjacent Euler gcd has this modular multiple-root interpretation.

For the quadratic Kummer obstruction, take $M=2N+2$ and



$$
d=H_N=\gcd(|E_{2N}|,|E_{2N+2}|).          \tag{19}
$$



The factor $J_N$ divides this $d$, so (18) applies to every layer of
$J_N$, including the interior seed at $N=1643$.

## 4. Exact discriminant divisibility

The resultant adjugate identity gives polynomials
$A_M,B_M\in\mathbb Z[Y]$ such that



$$
A_M(Y)f_M(Y)+B_M(Y)f_M'(Y)
       =\operatorname {Res}(f_M,f_M').                       \tag{20}
$$



The resultant is nonzero.  Indeed, Brillhart's multiple-root theorem for
Euler polynomials says that the only Euler polynomial with a multiple
root is the degree-five exception; here $M$ is even.  Equivalently,
$\mathcal F_M$, and hence $f_M$, is squarefree over characteristic
zero.

Evaluating (20) at zero and using (17) shows



$$
d\mid\operatorname {Disc}(f_M).         \tag{21}
$$



There is also an exact composition formula.  Taking the roots of $f_M$
and pairing the two square roots of each one gives



$$
\boxed{
 \operatorname {Disc}(\mathcal F_M)
   =(-4)^m f_M(0)\operatorname {Disc}(f_M)^2.}              \tag{22}
$$



Combining (17), (21), and (22) proves the all-layer divisibility



$$
\boxed{d^3\mid\operatorname {Disc}(\mathcal F_M).}        \tag{23}
$$



This is stronger than merely observing that every prime in $d$ divides
a discriminant: the full common prime-power valuation is counted three
times.  It is nevertheless quantitatively ineffective for the present
problem because the eliminating integer is much too large.

## 5. The height ledger and the loss of a factor $M$

For every even $j\geq2$, the beta-value formula, $\beta(j+1)<1$, and
$\pi>3$ give $|E_j|\leq j!$; the same bound is immediate at $j=0$.
Consequently every coefficient of $\mathcal F_M$, and hence every
coefficient of $f_M$, has modulus at most



$$
\binom Mj j!\leq M!.                         \tag{24}
$$



Apply Hadamard's inequality to the $(2m-1)$-row Sylvester matrix of the
monic degree-$m$ polynomial $f_M$ and its derivative.  Rows coming
from $f_M$ have Euclidean norm at most
$\sqrt{m+1}\,M!$, and rows coming from $f_M'$ have norm at most
$m\sqrt m\,M!$.  Therefore



$$
|\operatorname {Disc}(f_M)|
 \leq
 \bigl(\sqrt{m+1}\,M!\bigr)^{m-1}
 \bigl(m\sqrt m\,M!\bigr)^m,
 \qquad
 \log|\operatorname {Disc}(f_M)|=O(M^2\log M).             \tag{25}
$$



The same scale follows for (22).  More generally, every ordinary
Sylvester subresultant minor in this degree-and-height model has order at
most $2m-1$, entries bounded by $mM!$, and therefore the same
$O(M^2\log M)$ logarithmic ledger.  A useful subresultant argument would
need a new factor isolation or a matrix of genuinely smaller effective
dimension; choosing another unstructured minor does not supply it.

By contrast, before introducing any polynomial elimination one already
has



$$
d\leq|E_{M-2}|\leq(M-2)!,
 \qquad \log d=O(M\log M).                                  \tag{26}
$$



Thus even the cubic divisibility (23), divided through by three, gives an
upper bound worse by a factor of order $M$ than (26).  This rigorously
explains why the fourth-order-root observation does not control $J_N$.

## 6. The level-4 Eisenstein-series test

There is a natural modular encoding, but it does not turn the two constant
terms into a small common determinant.  Let $\chi_4$ be the primitive odd
character modulo 4 and let $k=2N+1$.  In the standard unnormalized
convention, the level-4 Eisenstein series



$$
\mathscr E_k(q)=
 {L(1-k,\chi_4)\over2}
 +\sum_{n\geq1}\left(\sum_{d\mid n}\chi_4(d)d^{k-1}\right)q^n
 \in M_k(\Gamma_0(4),\chi_4)                               \tag{27}
$$



has



$$
L(-2N,\chi_4)={E_{2N}\over2},\qquad
 \mathscr E_k(q)={E_{2N}\over4}+q+q^2+
                  (1-3^{2N})q^3+\cdots .                   \tag{28}
$$



Thus, for an odd prime power $p^a$, divisibility
$p^a\mid E_{2N}$ makes the constant term of
$4\mathscr E_k$ vanish modulo $p^a$, but its coefficient of $q$
is the unit 4:



$$
4\mathscr E_k(q)\equiv4q+4q^2+\cdots
                         \pmod {p^a}.                        \tag{29}
$$



This is a one-cusp constant-term congruence, not coefficientwise
divisibility of a modular form.  Sturm's theorem therefore cannot be
applied directly to bound $p^a$.  Simultaneous divisibility of
$E_{2N}$ and $E_{2N+2}$ merely supplies (29) in the two different
weights $k$ and $k+2$.

Multiplication by an integral weight-2 form of constant term one aligns
the weights, and a level-4 Serre derivative gives another such alignment.
Neither operation by itself turns (29) into coefficientwise vanishing:
the resulting residue has zero constant at infinity, but its positive
Fourier coefficients are not constrained by the two Euler divisibilities.
It could vanish for an exceptional modulus only through an additional
congruence theorem, not from the constant terms alone.
Likewise, the Eisenstein Hecke eigenvalues away from $4p$ are



$$
1+\chi_4(\ell)\ell^{k-1}\quad\hbox{and}\quad
 1+\chi_4(\ell)\ell^{k+1}.                                  \tag{30}
$$



For $p>3$ these are not one common residual eigenpacket: equality for
all $\ell\nmid4p$ would force $\ell^2=1\pmod p$ for every such
prime $\ell$, which is false.  In particular a weight-2 multiplier does
not identify the two Eisenstein ideals or couple the neighboring Kummer
branches.

The size ledger for a full congruence-module computation is no better.
The index of $\Gamma_0(4)$ is 6, so the Sturm bound in weight $k$ is



$$
B_k=\left\lfloor{k\over2}\right\rfloor. \tag{31}
$$



The level-4 ring can be represented using fixed weight-2 theta/Eisenstein
generators, with the odd-character module generated by the weight-1 form
$\theta^2$.  Hence the relevant truncated coefficient lattice has
dimension $O(k)$.  Through $n\leq B_k$, the Eisenstein coefficients
in (27) obey



$$
\left|\sum_{d\mid n}\chi_4(d)d^{k-1}\right|
       \leq n^k=\exp(O(k\log k)).                            \tag{32}
$$



The fixed-generator monomial basis has the same safe coefficient scale:
there are $O(k)$ factors and $O(k)$ retained powers of $q$, so a
direct convolution bound is $\exp(O(k\log k))$.  Hadamard's inequality
on an $O(k)$-dimensional congruence or Hecke determinant consequently
gives $O(k^2\log k)$ for its logarithm.  This is the modular analogue
of (25), not an $O(k)$ or $o(k\log k)$ product bound.  A smaller
congruence ideal could exist only through additional arithmetic
factorization not supplied by the ring structure, the multiplier, the
Serre derivative, or Sturm's bound.

## 7. Literature boundary and the exact missing lemma

The prime-power Euler--Kummer congruence controls one residue branch at a
time.  When $\varphi(p^a)>2N+2$, the two indices $2N$ and $2N+2$
lie in distinct neighboring first-period branches.  Applying branchwise
periodicity or a one-branch lifting statement twice does not bound their
simultaneous product.

The cyclotomic and $p$-adic literature similarly supplies per-prime
irregularity indices, class-number interpretations, and branchwise
lifting data.  Those results do not, as stated, give a uniform product
estimate over the varying primes which divide both fixed adjacent Euler
numbers.  The known interior example $p=151483$, with total
$E$-irregularity index exactly two, also shows that adjacency cannot be
converted into a large total irregularity index without an additional
hypothesis.  These sentences report the boundary of the cited tools; they
are not a theorem that no stronger result exists elsewhere.

In the notation of the frozen Kummer decomposition, the still-missing
statement can be written exactly as



$$
\sum_{\substack{p\ {\rm odd},\ a>a_p(N)\\
                  p^a\mid E_{2N},\ p^a\mid E_{2N+2}}}
       \log p=o(N\log N),                                   \tag{33}
$$



where each valuation layer $a$ is counted once.  The left side is
$\log J_N$.  Neither (3), (23), a total irregularity-index bound, nor a
branchwise Kummer congruence proves (33).

Relevant primary sources are:

1. J. Brillhart, *On the Euler and Bernoulli polynomials*, J. Reine
   Angew. Math. 234 (1969), 45--64,
   <https://doi.org/10.1515/crll.1969.234.45>.  Its
   multiple-root theorem supplies the characteristic-zero nonvanishing
   used above.
2. R. Ernvall and T. Metsänkylä, *Cyclotomic invariants and
   $E$-irregular primes*, Math. Comp. 32 (1978), 617--629,
   <https://doi.org/10.1090/S0025-5718-1978-0482273-9>.
3. R. Ernvall, *An upper bound for the index of
   $\chi$-irregularity*, Mathematika 32 (1985), 39--44,
   <https://doi.org/10.1112/S0025579300010834>.
4. J. B. Cosgrave and K. Dilcher, *On a congruence of Emma Lehmer related
   to Euler numbers*, Acta Arith. 161 (2013), 47--67,
   <https://www.impan.pl/shop/publication/transaction/download/product/82378>.
   Equation (2.2) there is the prime-power Euler--Kummer congruence used
   in the frozen decomposition.
5. J. Sturm, *On the congruence of modular forms*, in *Number Theory
   (New York, 1984--1985)*, Lecture Notes in Math. 1240, Springer (1987),
   275--280, <https://doi.org/10.1007/BFb0072985>.  At level 4 its bound
   gives (31).

## 8. Replay and logical scope

The deterministic companion certificate checks the valuation inequalities
on an exhaustive bounded symbolic grid, verifies (3)--(4) and the exact
$2$-part on exact Euler rows, constructs (15)--(17), verifies the
resultant and composition identities, checks (21)--(23), and audits the
Hadamard bound on a declared finite degree grid.  Those computations audit
the formulas.  The arguments above prove the all-parameter statements.

From the research directory run

    python3 scripts/root_unity_adjacent_euler_descent_discriminant_certificate.py
    sha256sum -c results/root_unity_adjacent_euler_descent_discriminant_hashes.sha256

No finite computation here is extrapolated to (33), and no claim here
classifies $e+\pi$.
