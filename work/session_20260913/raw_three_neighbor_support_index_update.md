> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Uniform ternary support and the three-neighbor mandatory divisor

Date: 2026-09-13. Original elementary synthesis by audit_computations;
independent review requested. All arithmetic inputs have independent
reviews. This note updates the two historical index-restriction
syntheses without transferring their old density constants to a larger
divisor. No new prime list, canonical degree, or numerical scan is used.

Retain even $n$, the actual reduced denominator $q_n$,



$$
\alpha=5\log\phi,\quad\beta=\tfrac32\log2,
 \quad B=\alpha-\beta,
 \quad a_n=v_2(q_n)=\tfrac32n+\epsilon_n^{(2)},
 \quad\epsilon_n^{(2)}\in\{0,1\}.
$$



The accepted error asymptotic says
$|L_n|=Cq_ne^{-\alpha n}(1+o(1))$, with $C>0$.
The new arithmetic input is the full $n-1$ congruence and its
uniform ternary consequence, reviewed in
`raw_appell_minus_one_residue_independent_review.md`.

## 1. Exact simultaneous divisor, including the large-prime exception

For even $n\ge16$, define a prime set



$$
\mathcal S(n)=\{3\}
 \cup\{p\ge7:\ p\mid n(n-1)(n+1),\ p\text{ prime}\}
 \cup\begin{cases}
 \{5\},&5\mid n(n+1)\text{ or }25\mid n-1,\\
 \varnothing,&\text{otherwise}.
 \end{cases}
$$



Put $\chi_n=1$ if $n-1$ is a prime at least seven, and zero
otherwise; put $\sigma_n=1$ if $25\mid n-1$, and zero otherwise.
Then the explicit integer



$$
\boxed{
 \Lambda_\star(n)=
 \frac{2^{a_n}\displaystyle\prod_{p\in\mathcal S(n)}p^{v_p(n!)}}
 {(n-1)^{\chi_n}5^{\sigma_n}}
 \quad\text{divides }q_n\qquad(n\ge16\text{ even}).}
 \tag{1}
$$



Here are all required uniform threshold checks.

The ternary exponent is valid for every $n\ge9$, with no residue
restriction. Odd primes dividing $n(n+1)$ satisfy the full factorial
bound for even $n\ge16$, by the reviewed historical threshold proof.

For an odd proper prime divisor of $n-1$, write $n-1=mp$.
The cofactor $m$ is odd and at least three. The inequality
$2mp+2<p^m$ holds at $m=3,p=3$ and persists as either variable
increases. Since $v_p(n!)\ge m$, the strict Taylor-loss threshold
holds uniformly. Therefore the new numerator-unit theorem gives the
full factorial exponent whenever $p\ne5$.

If instead $p=n-1$ is prime, then $v_p(n!)=1$, while the same
strict threshold fails. The present inputs do not force that factor of
$p$. The denominator $(n-1)^{\chi_n}$ in (1) removes exactly
this unproved single exponent. It is not a claim that the actual
denominator lacks the prime. For $n\ge16$, this exceptional prime
cannot be three or five.

If $25\mid n-1$, write $n-1=5m$, so $m\ge5$. The
inequality $10m+2<5^{m-1}$ holds at five and persists. Hence
$v_5(n!)\ge m>\lfloor\log_5(2n)\rfloor+1$. The reviewed exact
valuation $v_5(\widehat P_e(1))=1$ and the greater arctangent
valuation give $v_5(q_n)\ge v_5(n!)-1$. This is the second explicit
loss in (1). The shallow class $v_5(n-1)=1$ is deliberately omitted.

The supports at distinct primes can be combined. The divisions in (1)
are exact divisions of an integer: the large exceptional prime has
factorial exponent one, and the five-adic exponent in its indicated
range is greater than one. Neither loss interacts with the dyadic or
ternary exponent.

## 2. Updated exact necessary budget

Define



$$
S_\star(n)=\sum_{p\in\mathcal S(n)}\frac{\log p}{p-1},
 \qquad
 D_\star(n)=\sum_{p\in\mathcal S(n)}
       \frac{s_p(n)\log p}{p-1}.
$$



Legendre's formula gives the exact identity



$$
\log\Lambda_\star(n)-\alpha n
 =n(S_\star(n)-B)-D_\star(n)
   -\chi_n\log(n-1)-\sigma_n\log5
   +\epsilon_n^{(2)}\log2.
 \tag{2}
$$



Every supported prime divides $n(n-1)(n+1)$, including the always
supported prime three. Thus the digit-sum bound remains
$D_\star(n)=O((\log n)^2)$, uniformly. The two additional losses
are $O(\log n)$. Any shrinking even subsequence must make the
right side of (2) tend to minus infinity; in particular it must satisfy
$\limsup S_\star(n)\le B$.

One may still multiply (1) by the reviewed single first-seed bonus from
the $n+1=mp^\nu$, $p>3m$ theorem. At most one prime qualifies,
and the extra factor is at most $n+1$. This costs at most
$\log(n+1)$ in any upper estimate for this known lower divisor.
It does not provide an upper bound for the unknown higher seed depth.

## 3. A larger explicit CRT exclusion

The fixed weight sets $\{3,5,7,11\}$ and $\{3,5,7,13\}$
both exceed $B$, with already reviewed exact positivity certificates.
Prime three is now available at every index. For prime five, use the
two residues zero and minus one modulo five and the controlled class
one modulo twenty-five; their combined density is $11/25$.
For each of seven, eleven, and thirteen, any of zero, one, or minus one
modulo that prime now suffices. Fixed-prime threshold exceptions affect
only finitely many indices, and the possible one-power loss at five
does not change an exponential divergence conclusion.

Consequently the union of these two explicit exclusions has relative
density among even indices



$$
\boxed{
 \frac{11}{25}\frac37
 \left(1-\left(1-\frac3{11}\right)
          \left(1-\frac3{13}\right)\right)
 =\frac{189}{2275}.}
 \tag{3}
$$



This is an exact finite CRT count. The absolute primitive forms grow
exponentially along every sufficiently large member of this union.
It is an illustrative subset of the exclusions supplied by (2), not
the density of all excluded indices.

## 4. A sharper tail estimate for the updated mean

The earlier mean bound $\mu_*<1/2$ alone does not prove a
positive-density conclusion after adding the third residue. A sharper
bound using the same five retained primes suffices. Put



$$
\mu_*:=\sum_{p\text{ odd}}\frac{\log p}{p(p-1)}.
$$



All remaining odd primes after $3,5,7,11,13$ are odd integers at
least seventeen. The function
$f(x)=\log(2x+1)/(2x(2x+1))$ is decreasing for $x\ge1$.
For example, with $t=2x+1$, the derivative has numerator
$(t-1)-(2t-1)\log t<0$ for $t\ge3$. Therefore



$$
\sum_{j=8}^{\infty}f(j)
 \le\int_7^\infty f(x)\,dx
 =\frac12\int_{15}^{\infty}\frac{\log t}{t(t-1)}\,dt.
$$



For $t\ge15$,



$$
\frac1{t(t-1)}
 =\frac1{t^2}+\frac1{t^2(t-1)}
 \le\frac1{t^2}+\frac{15}{14t^3}.
$$



Integrating these two elementary terms yields



$$
\boxed{
 \mu_*\le\overline\mu_\star:=
 \frac{\log3}{6}+\frac{\log5}{20}+\frac{\log7}{42}
 +\frac{\log11}{110}+\frac{\log13}{156}
 +\frac{58\log15+57}{1680}.}
 \tag{4}
$$



No new prime list or prime-distribution theorem is used.

## 5. Exact certificates for a positive-density remaining budget

The support of three is constant. For five, the supported proportion
is $2/5+1/25$; for every prime at least seven it is $3/p$.
Thus, averaging over even indices and bounding the residue-count
rounding errors by $O(X^{-1}\sum_{p\le2X+1}\log p/(p-1))=o(1)$,



$$
\limsup_{X\to\infty}\frac1X\sum_{k=1}^X S_\star(2k)
 \le3\mu_*-\frac{\log5}{25}.
 \tag{5}
$$



The subtraction is exactly the missing shallow five-adic class: it has
density $4/25$, and its weight is $\log5/4$. The always present
prime three already agrees with $3\mu_*$'s contribution.

Here are entirely rational certificates with enough margin for (5).
The following logarithm upper bounds hold:



$$
\log3<1099/1000,\quad \log5<161/100,\quad
 \log7<973/500,\quad \log11<1199/500,\quad
 \log13<513/200,\quad\log15<2709/1000.
$$



For each displayed rational $r$, the exact rational sum
$\sum_{j=0}^{20}r^j/j!$ already exceeds the integer whose logarithm
is bounded. Substitution in (4) gives



$$
\overline\mu_\star<\frac{1731533}{3640000}.
$$



Also $\log5>8/5$, for example by six positive terms of
$2\sum_{k\ge0}(2/3)^{2k+1}/(2k+1)$. Consequently



$$
3\mu_*-\frac{\log5}{25}
 <\frac{4961639}{3640000}<\frac{1091}{800}.
 \tag{6}
$$



Finally $B>273/200$ has a short exact certificate. Since
$\phi>809/500$, use the first six positive terms of the logarithm
series with $u=309/1309$ to lower-bound $\log\phi$. Upper-bound
$\log2$, with $v=1/3$, by



$$
2\sum_{k=0}^5\frac{v^{2k+1}}{2k+1}
 +\frac{2v^{13}}{13(1-v^2)}.
$$



Five times the former lower bound minus three halves of this upper
bound is greater than $273/200$ by exact rational comparison.
The elementary bound $\phi>809/500$ follows by squaring
$\sqrt5>559/250$. All finite certificates in this section were
recomputed with rational arithmetic; decimals are not proof inputs.

Apply Markov's inequality with $c=273/200<B$. Equations (5)–(6)
show that the set of even indices with $S_\star(n)\le c$ has lower
relative density at least



$$
\boxed{
 1-\frac{4961639/3640000}{273/200}
 =\frac{6961}{4968600}>\frac1{1092}.}
 \tag{7}
$$



On this whole set, the nonnegative digit correction and the explicit
losses in (2) imply



$$
\boxed{
 \log\Lambda_\star(n)\le
  (\alpha-(B-c))n+\log2.}
 \tag{8}
$$



The seed bonus mentioned after (2) changes the right side by at most
$\log(n+1)$. Hence even the strengthened simultaneous mandatory
divisor, with uniform ternary support, the three neighboring factors,
the controlled deep five-adic class, and the known first seed bonus,
leaves a positive-density set below the shrinking threshold by a fixed
exponential factor.

This upper bound is for the explicit lower divisor, not for the actual
$q_n$. It neither proves shrinkage on this set nor excludes additional
arithmetic factors there. It shows precisely that these currently
specified support-based lower bounds do not alone eliminate every
candidate subsequence. The historical one-fifth density is not asserted
for the strengthened divisor.
