> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Large primes on the fixed $u_7^d$ ray: factorial tails, a quadratic resultant, and a trace-cancellation obstruction

## Status

This note analyzes the branch $p>d$ in the exact criterion



$$
\begin{cases}
 E_d(-1)\equiv0\pmod {p^a},\\
 \operatorname {Tr}_{K/\mathbb Q}
 \bigl(u_7^dE_d(-\eta)E_d(-\bar\eta)\bigr)
 \equiv0\pmod {p^a},
 \end{cases}
\tag{1}
$$



at its first level $a=1$, for primes $p\nmid20$. Here



$$
K=\mathbb Q(\zeta_{20})^+,\qquad
 F=\mathbb Q(\sqrt5),\qquad
 E_d(X)=\sum_{j=0}^d\frac{X^j}{j!},
\tag{2}
$$



and



$$
\eta=(1+\zeta_5)^{-1},\qquad
 \bar\eta=1-\eta,\qquad q=\eta\bar\eta.
\tag{3}
$$



The main result is an exact boundary transformation. It replaces the two
truncated exponentials at $\eta,\bar\eta$ by a single quadratic
resultant and replaces $u_7^d$ by one of four fixed
Frobenius-class unit traces. It also proves a negative structural result:
the final $F/\mathbb Q$ trace condition does **not** factor into the
vanishing of its two conjugate scalar components. Exact nonzero
cancellation witnesses occur in all four Frobenius classes modulo $20$.

This is a local theorem and a rigorous obstruction to a tempting
factorization argument. It is not a uniform bound for the large-prime
gcd, and it proves nothing about the arithmetic nature of $e+\pi$.

The exact certificate is
<scripts/cyclotomic_unit_large_prime_boundary_resultant.py>, with output
<results/cyclotomic_unit_large_prime_boundary_resultant_p2000.json>.

## 1. Wilson's sign and the boundary factorial tail

Let $p\nmid20$ be prime and $1\le d<p$. Put



$$
r=p-1-d
\tag{4}
$$



and define, in $\mathbb F_p[Y]$,



$$
S_{p,r}(Y)=\sum_{k=r}^{p-1}k!Y^k.
\tag{5}
$$



For $0\le j\le p-1$, Wilson's theorem and
${p-1\choose j}\equiv(-1)^j\pmod p$ give the sign-sensitive identity



$$
j!(p-1-j)!\equiv(-1)^{j+1}\pmod p,
\qquad
             \frac1{j!}\equiv
             (-1)^{j+1}(p-1-j)!\pmod p.
\tag{6}
$$



Therefore every unit $x$ in an $\mathbb F_p$-algebra satisfies



$$
\begin{aligned}
 E_d(-x)
  &=\sum_{j=0}^d\frac{(-x)^j}{j!}\\
  &=-\sum_{j=0}^d x^j(p-1-j)!\\
  &=-x^{p-1}\sum_{k=r}^{p-1}k!x^{-k}.
 \end{aligned}
\tag{7}
$$



In particular,



$$
\boxed{E_d(-x)=-x^{p-1}S_{p,r}(x^{-1}),}
\qquad
 \boxed{E_d(-1)=0\ \Longleftrightarrow\ S_{p,r}(1)=0.}
\tag{8}
$$



The tail has a useful differential identity:



$$
\boxed{
 Y^2S_{p,r}'(Y)+(Y-1)S_{p,r}(Y)=-r!Y^r
 \quad\text{in }\mathbb F_p[Y].}
\tag{9}
$$



Indeed, the coefficient of $Y^n$ cancels for
$r<n<p$, the coefficient at $Y^r$ is $-r!$, and the prospective
coefficient at $Y^p$ is $p(p-1)!=0$.

Assume from now on that the first congruence in (1) holds. Then
$S_{p,r}(1)=0$, so there is a unique
$Q_{p,r}\in\mathbb F_p[Y]$ such that



$$
S_{p,r}(Y)=(Y-1)Q_{p,r}(Y).
\tag{10}
$$



Putting $Y=1$ in (9) gives



$$
\boxed{Q_{p,r}(1)=S_{p,r}'(1)=-r!\ne0\pmod p.}
\tag{11}
$$



Thus the forced root $Y=1$ is simple. This nonzero sign and factorial
factor are retained in the certificate.

## 2. The exact quadratic resultant

Put



$$
a=\eta^{-1}=1+\zeta_5,\qquad
 b=\bar\eta^{-1}=1+\zeta_5^{-1},\qquad
 z=q^{-1}.
\tag{12}
$$



Since $\eta+\bar\eta=1$,



$$
a+b=ab=z,
\tag{13}
$$



so $a,b$ are the roots of



$$
f_z(Y)=Y^2-zY+z.
\tag{14}
$$



More importantly, the two forced linear factors in (10) cancel exactly:



$$
(a-1)(b-1)=\zeta_5\zeta_5^{-1}=1.
\tag{15}
$$



Equations (8), (10), and (15) now give



$$
\begin{aligned}
 E_d(-\eta)E_d(-\bar\eta)
  &=q^{p-1}S_{p,r}(a)S_{p,r}(b)\\
  &=q^{p-1}Q_{p,r}(a)Q_{p,r}(b).
 \end{aligned}
\tag{16}
$$



Define the quadratic resultant



$$
\mathcal N_{p,r}
  =\operatorname {Res}_Y\bigl(f_z(Y),Q_{p,r}(Y)\bigr)
  =Q_{p,r}(a)Q_{p,r}(b)
  \in\mathcal O_F/p\mathcal O_F.
\tag{17}
$$



The exact identity is therefore



$$
\boxed{
 E_d(-\eta)E_d(-\bar\eta)
      =q^{p-1}\mathcal N_{p,r}
 \quad\text{in }\mathcal O_F/p\mathcal O_F.}
\tag{18}
$$



This is a genuine degree-two resultant. If the remainder of
$Q_{p,r}(Y)$ modulo $f_z(Y)$ is $A+BY$, then the certificate computes
it independently from



$$
\boxed{
 \mathcal N_{p,r}=A^2+zAB+zB^2.}
\tag{19}
$$



No conjugate factor, sign, or power of $q$ is suppressed in
(18)--(19).

## 3. Frobenius at the unit factor

Let $\sigma_p$ be the automorphism of $K$ induced by
$\zeta_{20}\mapsto\zeta_{20}^p$. Since $p\nmid20$,



$$
x^p\equiv\sigma_p(x)\pmod p
\tag{20}
$$



for every cyclotomic integer $x$. With $d=p-1-r$, this gives



$$
\boxed{
 u_7^d=u_7^{p-1-r}
       \equiv\sigma_p(u_7)u_7^{-r-1}\pmod p.}
\tag{21}
$$



Let $\tau$ denote the nontrivial automorphism of $K/F$, and put



$$
\boxed{
 W_{c,r}=
 \operatorname {Tr}_{K/F}
 \bigl(\sigma_c(u_7)u_7^{-r-1}\bigr)\in\mathcal O_F,}
\tag{22}
$$



where $c\in\{1,3,7,9\}$ is the class of $p$ in



$$
(\mathbb Z/20\mathbb Z)^\times/\{\pm1\}
   =\{\{\pm1\},\{\pm3\},\{\pm7\},\{\pm9\}\}.
\tag{23}
$$



Thus $W_{c,r}$ is one of four fixed unit-trace sequences in $r$; it
does not otherwise depend on $p$.

The remaining scalar $q^{p-1}$ is also explicit in
$\mathcal O_F/p\mathcal O_F$. The element $q$ satisfies
$q^2-3q+1=0$, so its $F/\mathbb Q$ norm is $1$. Hence, with all
entries below understood in that quotient,



$$
\chi_p:=q^{p-1}=\frac{\sigma_p(q)}q
 =
 \begin{cases}
 1,&p\equiv1,9,11,19\pmod {20},\\
 q^{-2},&p\equiv3,7,13,17\pmod {20}.
 \end{cases}
\tag{24}
$$



Combining (18), (21), and transitivity of trace proves the promised
boundary decomposition.

### Theorem 1 (boundary resultant and Frobenius-class trace)

For $p\nmid20$, $1\le d<p$, $r=p-1-d$, and
$E_d(-1)=0\pmod p$, the second congruence in (1) is equivalent to



$$
\boxed{
 \operatorname {tr}_{(\mathcal O_F/p)/\mathbb F_p}
 \bigl(\chi_p\,\mathcal N_{p,r}\,W_{c,r}\bigr)=0,}
\tag{25}
$$



where $\mathcal N_{p,r}$, $W_{c,r}$, and $\chi_p$ are exactly
(17), (22), and (24). Here $\operatorname {tr}$ is the algebra trace;
it applies both when $\mathcal O_F/p$ is a field and when it is a
split product.

## 4. The trace condition does not factor

The splitting behavior is determined by $(5/p)$.

### Split classes

If



$$
p\equiv1,9,11,19\pmod {20},
\tag{26}
$$



then



$$
\mathcal O_F/p\mathcal O_F
                     \simeq\mathbb F_p\times\mathbb F_p.
\tag{27}
$$



Writing



$$
y=\chi_p\mathcal N_{p,r}W_{c,r}=(y_+,y_-),
$$



condition (25) is exactly



$$
y_++y_-=0.
\tag{28}
$$



It is not the pair of conditions $y_+=y_-=0$.

### Inert classes

If



$$
p\equiv3,7,13,17\pmod {20},
\tag{29}
$$



then



$$
\mathcal O_F/p\mathcal O_F\simeq\mathbb F_{p^2}.
\tag{30}
$$



Condition (25) is exactly



$$
y+y^p=0.
\tag{31}
$$



It is not the condition $y=0$. In particular, whenever $y\ne0$,
(31) is equivalently $y^{p-1}=-1$.

These statements already show that the algebra trace is one linear
condition, not two scalar vanishing conditions. The exact finite
certificate goes further.

### Proposition 2 (nonzero cancellation in every Frobenius class)

For each quotient Frobenius class in (23), there is a pair
$(p,d)$, with $p>d$, satisfying both congruences in (1) while



$$
\mathcal N_{p,r}\ne0,\qquad W_{c,r}\ne0,
\qquad
                \chi_p\mathcal N_{p,r}W_{c,r}\ne0.
\tag{32}
$$



One exact witness in each class is

| quotient class | $p\bmod20$ | $p$ | $d$ | $r=p-1-d$ |
|---:|---:|---:|---:|---:|
| $\{\pm1\}$ | $19$ | $1879$ | $1427$ | $451$ |
| $\{\pm3\}$ | $17$ | $277$ | $199$ | $77$ |
| $\{\pm7\}$ | $13$ | $13$ | $8$ | $4$ |
| $\{\pm9\}$ | $11$ | $31$ | $28$ | $2$ |

For the split witnesses, the two components in (28) are nonzero
opposites. For the inert witnesses, the nonzero element in (31) is sent
to its negative by Frobenius. The certificate independently reconstructs
$Q_{p,r}$, verifies (9), evaluates the resultant both from its two
conjugate factors and from (19), reconstructs the Frobenius action on
$u_7$, and records nonzero coordinates for both factors in (32).

Proposition 2 is a finite exact obstruction. It does not assert that
there are infinitely many such pairs.

## 5. The exact norm-one ratio equation

Let $\iota$ be the nontrivial $F/\mathbb Q$ conjugation. At a solution
of (25) for which the two factors in (32) are nonzero, put



$$
y=\chi_p\mathcal N_{p,r}W_{c,r}.
$$



The trace equation says $\iota(y)=-y$, with $\iota$ interpreted as
the second split component or as Frobenius in the inert case. Dividing by
the nonzero factors gives



$$
\boxed{
 \frac{\iota(\mathcal N_{p,r})}{\mathcal N_{p,r}}
   =
 -\frac{\chi_pW_{c,r}}
        {\iota(\chi_p)\,\iota(W_{c,r})}.}
\tag{33}
$$



Both sides have norm $1$. Equation (33) is the correct replacement for
the false componentwise-vanishing argument.

It is not yet a standard fixed-target $S$-unit equation. The right side
contains a ratio of conjugates of the **sum**
$W_{c,r}$, not just a monomial in a fixed unit group. More seriously,
the left side is a resultant of $Q_{p,r}$, whose degree is $p-2$ and
whose factorial coefficients move with both $p$ and $r$. Moreover
(33) is an equality in a varying characteristic-$p$ quotient, not an
equality of fixed characteristic-zero algebraic numbers. These are the
hypotheses that any Subspace-, $S$-unit-, or height-based continuation
must address; none is assumed here.

## 6. Finite certificate and conclusion

The script scans every prime



$$
3\le p<2000,\qquad p\ne5,
\tag{34}
$$



and every $1\le d<p$, using only exact finite-field and cyclotomic
arithmetic. In that finite box the complete list of simultaneous roots is



$$
(p,d)=(13,8),(31,28),(277,199),(1879,1427).
\tag{35}
$$



This finite list is not extrapolated. Its role is to certify that:

1. no quotient Frobenius class modulo $20$ can be discarded;
2. neither the resultant nor the unit-trace factor must vanish;
3. genuine nonzero conjugate cancellation occurs in both the split and
   inert cases; and
4. the remaining large-prime problem is the moving norm-one ratio
   equation (33), not a pair of scalar zero problems.

Thus the boundary transformation is exact and useful, but it does not by
itself prove a uniform bound for
$\gcd(D_{0,d},X_d)$.
