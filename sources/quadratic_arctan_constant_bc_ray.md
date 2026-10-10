> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A primitive no-decay theorem for the constant-$B,C$ quadratic pullback ray

## Statement

For a fixed integer $p\ge2$, let



$$
F_p(z)=4\arctan\frac{(p-1)z}{p-z^2}.
\tag{1}
$$



Then $F_p(1)=\pi$.  Consider the dimension-balanced endpoint-matched
Hermite--Padé ray with



$$
\deg A\le a,\qquad B(z)=C(z)=1,
\tag{2}
$$



and maximal cancellation at $z=0$:



$$
A_a(z)+e^z+F_p(z)=O(z^{a+1}).
\tag{3}
$$



After clearing every polynomial denominator and then reducing the endpoint
pair completely, write the primitive endpoint form as



$$
\mathcal L_{p,a}=Q_{p,a}(e+\pi)-P_{p,a},
\qquad
\gcd(P_{p,a},Q_{p,a})=1,\quad Q_{p,a}>0.
\tag{4}
$$



The theorem is



$$
\boxed{
|\mathcal L_{p,a}|
\geq
\exp\!\left(\frac12a\log a-O_p(a)\right)
\longrightarrow\infty.}
\tag{5}
$$



Thus this entire fixed-$B,C$ ray fails after complete primitive
normalization.  The proof does not assume a gcd formula and does not assume
that the oscillatory Taylor tail of $F_p$ has a fixed sign.

This is a no-go theorem for one explicit ray.  It does not decide whether
$e+\pi$ is algebraic or transcendental.

## 1. Exact rational approximant

Equation (3) forces



$$
A_a(z)=-T_a(e^z+F_p(z)),
\tag{6}
$$



where $T_a$ is Taylor truncation through degree $a$.  Put



$$
E_a=\sum_{k=0}^a\frac1{k!},
\qquad
\Pi_{p,a}=T_aF_p(1),
\qquad
R_{p,a}=E_a+\Pi_{p,a}.
\tag{7}
$$



If $R_{p,a}=P_{p,a}/Q_{p,a}$ in lowest terms, then the endpoint of (3)
is



$$
(e+\pi)-R_{p,a}.
$$



Clearing all coefficients of the polynomial triple can introduce a common
multiple of the endpoint pair, but the final endpoint gcd removes exactly
that multiple.  Hence (4) is indeed the completely reduced endpoint form,
and



$$
|\mathcal L_{p,a}|
=Q_{p,a}|(e+\pi)-R_{p,a}|.
\tag{8}
$$



## 2. Exponential denominator complexity of the $\pi$ truncation

Differentiation gives



$$
F_p'(z)=
\frac{4(p-1)(p+z^2)}
{z^4+(p^2-4p+1)z^2+p^2}.
\tag{9}
$$



Define integers



$$
c_{p,0}=1,\qquad c_{p,1}=-p^2+5p-1,
\tag{10}
$$





$$
c_{p,m}=-(p^2-4p+1)c_{p,m-1}-p^2c_{p,m-2}.
\tag{11}
$$



Coefficient comparison in (9) yields



$$
F_p(z)=
\sum_{m\ge0}
\frac{4(p-1)c_{p,m}}{p^{2m+1}(2m+1)}z^{2m+1}.
\tag{12}
$$



For (a\geq1), let



$$
M=\left\lfloor\frac{a-1}{2}\right\rfloor.
$$



The omitted case (a=0) has $\Pi_{p,0}=0$ and $D_{p,0}=1$, and is
irrelevant to the asymptotic theorem.

It follows directly from (12) that the reduced denominator
$D_{p,a}$ of $\Pi_{p,a}$ divides



$$
p^{2M+1}\operatorname{lcm}(1,2,\ldots,2M+1).
\tag{13}
$$



Chebyshev's elementary estimate



$$
\log\operatorname{lcm}(1,2,\ldots,n)=O(n)
\tag{14}
$$



therefore gives



$$
\boxed{\log D_{p,a}=O_p(a).}
\tag{15}
$$



Only this upper bound is used; no assertion about the exact cancellations
in (13) is needed.

## 3. A superexponential lower bound for the exponential denominator

Write the exponential truncation in lowest terms as



$$
E_a=\frac{r_a}{q_a},\qquad \gcd(r_a,q_a)=1,\quad q_a>0.
\tag{16}
$$



The exact continued fraction of $e$ gives a fixed $c_e>0$ such that
every reduced rational $r/q$ satisfies



$$
\left|e-\frac rq\right|
\geq\frac{c_e}{q^2\log(2q)}.
\tag{17}
$$



On the other hand,



$$
0<e-E_a<\frac2{(a+1)!}.
\tag{18}
$$



Equations (17)--(18), together with the trivial $q_a\le a!$, imply



$$
\log q_a
\geq
\frac12\log((a+1)!)
-\frac12\log\log(2a!)
-O(1)
=\frac12a\log a-O(a).
\tag{19}
$$



Now write $\Pi_{p,a}=u_{p,a}/D_{p,a}$ and
$R_{p,a}=P_{p,a}/Q_{p,a}$, both in lowest terms.  Since



$$
E_a=R_{p,a}-\Pi_{p,a},
$$



the reduced denominator $q_a$ divides
$\operatorname{lcm}(Q_{p,a},D_{p,a})$, and hence



$$
q_a\le Q_{p,a}D_{p,a}.
\tag{20}
$$



Combining (15), (19), and (20) gives the normalization-independent bound



$$
\boxed{
\log Q_{p,a}\geq\frac12a\log a-O_p(a).}
\tag{21}
$$



This is the key arithmetic step: even an unexpectedly large gcd in the
combined endpoint pair cannot reduce its denominator below the scale in
(21).

## 4. Cancellation between the two analytic tails cannot occur

The finite irrationality measure for $\pi$, weakened safely to exponent
$36/5$, supplies a constant $c_\pi>0$ such that every reduced
$u/D$ satisfies



$$
\left|\pi-\frac uD\right|
\geq c_\pi D^{-36/5}.
\tag{22}
$$



Applying (22) to $\Pi_{p,a}$, then using (15), gives



$$
|\pi-\Pi_{p,a}|\geq\exp(-O_p(a)).
\tag{23}
$$



By contrast, (18) gives



$$
|e-E_a|=\exp(-a\log a+O(a)).
\tag{24}
$$



For all sufficiently large $a$, (24) is at most half the lower bound in
(23).  The reverse triangle inequality therefore proves



$$
\begin{aligned}
|(e+\pi)-R_{p,a}|
&=|(e-E_a)+(\pi-\Pi_{p,a})|\\
&\geq|\pi-\Pi_{p,a}|-|e-E_a|\\
&\geq\exp(-O_p(a)).
\end{aligned}
\tag{25}
$$



Finally, (8), (21), and (25) give (5).

## 5. Relation to the finite scan

The exact bounded scan in
scripts/quadratic_arctan_nondiagonal_probe.py contains this ray as
$(a,b,c)=(a,0,0)$.  For $p=2,3,4,5$, a targeted exact continuation
through $a=100$ agrees with (5): after a few accidental low-degree forms
below one, the primitive magnitudes grow rapidly.  These calculations are
diagnostic only; the all-degree conclusion is the theorem above.

The proof uses the already independently audited rational-approximation
bound for $e$ and the independently audited exponent-$36/5$ consequence
of the Zeilberger--Zudilin irrationality measure for $\pi$.
