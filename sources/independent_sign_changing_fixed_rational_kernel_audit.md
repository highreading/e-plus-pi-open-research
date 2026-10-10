> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit: sign-changing fixed rational kernel barrier

Audited: 2026-08-26 UTC

## Verdict and frozen checkpoint

**ACCEPT** for the frozen target

    sources/sign_changing_fixed_rational_kernel_barrier.md
    SHA-256 42d090fe9f47b0a974456672e9d7cd8ae76be08e3e9c56f89379f2f8cf14727b

I independently re-derived the symmetrization, the exact midpoint
asymptotic and its relative error, the exponential coordinate-height
bound, primitive normalization, the full prime-power content bound, both
matching orientations, and the final divergence.  No positivity of the
kernel is used.  The conclusion is valid on an arbitrary infinite,
possibly sparse, set of even indices.

The target was not edited during this audit.  Its short Laplace argument
can be made completely quantitative by the exact beta-integral calculation
in Section 2 below; that calculation gives precisely the coefficient and
the relative $O(1/n)$ stated in the target.

## 1. Symmetrization and the exceptional antisymmetric case

Write



$$
w_n(x)=x^n(1-x)^n,\qquad
 K_{\rm s}(x)=\frac{K(x)+K(1-x)}2 .
$$



The substitution $u=1-x$ gives



$$
\int_0^1w_n(x)K(1-x)\,dx
 =\int_0^1w_n(u)K(u)\,du .
$$



Consequently



$$
J_n(K)=J_n(K_{\rm s})
$$



for every nonnegative integer $n$, without a parity assumption.  Since
$K$ has no pole on $[0,1]$, neither $K(1-x)$ nor $K_{\rm s}$ has a
pole there.

If $K_{\rm s}\equiv0$, every moment is zero.  A relevant-index identity



$$
0=r_n+\varepsilon_nc_n\pi,
 \qquad r_n,c_n\in\mathbb Q,\quad c_n>0,
$$



would imply $\pi=-r_n/(\varepsilon_nc_n)\in\mathbb Q$, a contradiction.
Thus the hypothesis on even an individual relevant index rules out this
case.  There is no hidden zero-moment exception.

For nonzero $K_{\rm s}$, put $t=x-1/2$.  The rational function
$K_{\rm s}(1/2+t)$ is real analytic near zero and is even in $t$.
Hence its first nonzero Taylor term has the unique form



$$
K_{\rm s}(1/2+t)=a t^{2m}+O(t^{2m+2}),
 \qquad m\geq0,\quad a\ne0.
$$



This includes kernels vanishing to any fixed even order at the midpoint.
It also shows that no odd leading term or parity-dependent cancellation
has been omitted.

## 2. Exact midpoint asymptotic

For $j\geq0$, define



$$
M_{n,j}=\int_{-1/2}^{1/2}
          (1-4t^2)^n t^{2j}\,dt .
$$



The substitutions $u=2t$ and then $z=u^2$ give the exact identity



$$
M_{n,j}
 =\frac1{2\cdot4^j}
   B\left(j+\frac12,n+1\right).                 \tag{A1}
$$



There is a bounded function $h$ on $[-1/2,1/2]$ such that



$$
K_{\rm s}(1/2+t)=a t^{2m}+t^{2m+2}h(t).        \tag{A2}
$$



Indeed, the quotient defining $h$ has a removable singularity at zero,
and away from zero it is continuous on a compact set.  This global
factorization avoids any uniformity issue at the edge of a local Taylor
neighborhood.

Since



$$
x^n(1-x)^n=4^{-n}(1-4t^2)^n,
$$



equations (A1)--(A2) yield



$$
J_n(K)
 =4^{-n}\left(aM_{n,m}+O_K(M_{n,m+1})\right).   \tag{A3}
$$



The exact ratio of the two moments is



$$
\frac{M_{n,m+1}}{M_{n,m}}
 =\frac{m+1/2}{4(n+m+3/2)}
 =O_m(n^{-1}).                                  \tag{A4}
$$



Moreover, the standard fixed-shift gamma-ratio estimate gives



$$
\begin{aligned}
 M_{n,m}
 &=\frac{\Gamma(m+1/2)}{2\cdot4^m}
   \frac{\Gamma(n+1)}{\Gamma(n+m+3/2)}\\
 &=\frac{\Gamma(m+1/2)}{2\cdot4^m}
   n^{-m-1/2}\left(1+O_m(n^{-1})\right).
                                                               \tag{A5}
 \end{aligned}
$$



Substitution into (A3) proves exactly



$$
J_n(K)=
 \frac{a\Gamma(m+1/2)}{2\cdot4^m}
 4^{-n}n^{-m-1/2}
 \left(1+O_K(n^{-1})\right).                    \tag{A6}
$$



The leading constant is nonzero.  Therefore, for fixed positive
constants $c_0,n_0$,



$$
\operatorname{sgn}J_n(K)=\operatorname{sgn}a,\qquad
 |J_n(K)|\geq c_0\,4^{-n}n^{-m-1/2}
                                                               \tag{A7}
$$



for all $n\geq n_0$.  This proves the target's exact factor
$\Gamma(m+1/2)/(2\cdot4^m)$, its relative error, and its eventual-sign
claim.

## 3. Arithmetic height does not require positivity

Choose a reduced representation



$$
K=P/Q,\qquad P,Q\in\mathbb Z[x],\quad \gcd(P,Q)=1.
$$



Because the rational function has no pole on $[0,1]$, this reduced
denominator has no zero there.  Divide



$$
P(x)x^n(1-x)^n=Q(x)S_n(x)+R_n(x),
 \qquad \deg R_n<\deg Q .
$$



There are $2n+O_K(1)$ long-division steps.  At each step the denominator
is multiplied by at most the fixed leading coefficient of $Q$, and the
integer-numerator $\ell^1$-norm is multiplied by at most a fixed
constant.  Since



$$
\left\|P(x)x^n(1-x)^n\right\|_1
 \leq \|P\|_1\,2^n,
$$



all coefficients of $S_n,R_n$ can be put on one denominator, with both
that denominator and all numerators at most $C^n$.

Integrating $S_n$, whose degree is $O_K(n)$, costs a divisor of



$$
\operatorname{lcm}(1,2,\ldots,O_K(n))=\exp(O_K(n)),
$$



so its rational integral still has exponential height.  The remaining
integral is a rational combination of the fixed constants



$$
\omega_j=\int_0^1\frac{x^j}{Q(x)}\,dx,
 \qquad 0\leq j<\deg Q .
$$



In the finite-dimensional rational vector space spanned by
$1,\pi,\omega_0,\ldots$, extend the linearly independent pair
$1,\pi$ to a fixed basis.  Every coordinate of $J_n(K)$ in this basis
then has height at most $C_K^n$.  Whenever



$$
J_n(K)=r_n+\varepsilon_nc_n\pi
$$



with rational $r_n,c_n$, uniqueness of basis coordinates identifies
these as the first two coordinates and forces all others to vanish.
Thus, after enlarging $C_K$,



$$
H(r_n)\leq C_K^n,\qquad H(c_n)\leq C_K^n.       \tag{A8}
$$



No estimate in this argument uses a sign condition on $K$ or on its
moment.  The constant-denominator case is included with $R_n=0$.

Write in lowest terms



$$
r_n=\frac{a_n}{b_n},\qquad
 c_n=\frac{u_n}{v_n},
\qquad b_n,v_n>0,\quad u_n>0.
$$



Clearing by $T_n=\operatorname{lcm}(b_n,v_n)$ gives a pre-primitive
$\pi$-coefficient



$$
\frac{T_nu_n}{v_n}\leq b_nu_n.
$$



Primitive reduction can only decrease it.  Hence, if



$$
L_n=A_n+\varepsilon_nB_n\pi=\mu_nJ_n(K),
\qquad B_n,\mu_n>0,
$$



is the primitive integer normalization, then



$$
B_n\leq b_nu_n,\qquad
 c_nB_n\leq b_nu_n^2\leq C_2^n                 \tag{A9}
$$



for a fixed $C_2$.  This also covers $r_n=0$, represented as $0/1$.
The equality of $\pi$-coefficients gives $B_n=\mu_nc_n$, which will be
used below.

## 4. Exponential pair and content after matching

For even $n$, repeated integration by parts gives



$$
E_n=\frac1{n!}\int_0^1x^n(1-x)^ne^x\,dx
     =q_ne-p_n>0.
$$



The endpoint sums satisfy



$$
X_n=2(2n-1)X_{n-1}+X_{n-2}
$$



for $X=p,q$, with



$$
(p_0,p_1)=(1,3),\qquad(q_0,q_1)=(1,1).
$$



Their adjacent determinant has absolute value $2$, while the recurrence
makes all entries odd.  Therefore



$$
\gcd(p_n,q_n)=1.                               \tag{A10}
$$



Reversing the alternating endpoint sum for $q_n$ makes its absolute
terms strictly decreasing.  The difference of the first two is



$$
\frac{(2n)!}{n!}-\frac{(2n-1)!}{(n-1)!}
 =\frac{n(2n-1)!}{n!},
$$



and the remaining alternating tail is nonnegative.  Thus



$$
q_n\geq\frac{n(2n-1)!}{n!}.                    \tag{A11}
$$



Also



$$
0<E_n\leq\frac{e\,n!}{(2n+1)!}.                \tag{A12}
$$



To audit the final content, consider arbitrary primitive integer pairs



$$
(-p,q),\qquad(A,\delta B),\qquad q,B>0.
$$



Put



$$
d=\gcd(q,B),\qquad q=dq_0,\qquad B=dB_0.
$$



The minimal coefficient-matching multipliers are $B_0,q_0$, the common
target coefficient is $dq_0B_0$, and the constant coefficient has the
form



$$
M=-B_0p\mathbin{\pm}q_0A.                      \tag{A13}
$$



If a prime $\ell$ divides $q_0$, then $B_0p$ is a unit modulo
$\ell$, by $\gcd(q_0,B_0)=1$ and $\gcd(p,q)=1$; hence
$\ell\nmid M$.  If $\ell\mid B_0$, then $q_0A$ is a unit modulo
$\ell$, by $\gcd(A,B)=1$; again $\ell\nmid M$.  It follows
prime-power by prime-power that



$$
\gcd(M,dq_0B_0)\mid d.                          \tag{A14}
$$



In particular, the final content $g$ is at most $d\leq B$.  This
argument covers $A=0$: primitivity then forces $B=1$.

## 5. Matching orientations and divergence

Let



$$
\sigma=\operatorname{sgn}a,\qquad
 \widetilde L_n=\sigma L_n,\qquad
 \delta_n=\sigma\varepsilon_n.
$$



For every sufficiently large relevant index, (A7) and $\mu_n>0$ imply



$$
\widetilde L_n>0,\qquad
 \frac{\widetilde L_n}{B_n}
 =\frac{\mu_n|J_n(K)|}{\mu_nc_n}
 =\frac{|J_n(K)|}{c_n}.                         \tag{A15}
$$



The oriented pair remains primitive.

Put $d_n=\gcd(q_n,B_n)$.  If $\delta_n=1$, the minimal matched
$e+\pi$ form is



$$
W_n^+=\frac{B_n}{d_n}E_n+
       \frac{q_n}{d_n}\widetilde L_n>0.
$$



Using (A15), $B_n/d_n\geq1$, and the content bound $g_n\leq B_n$,



$$
\left|\frac{W_n^+}{g_n}\right|
 \geq\frac{q_n|J_n(K)|}{c_nB_n}.                \tag{A16}
$$



If $\delta_n=-1$, the minimal matched form with equal positive
coefficients of $e$ and $\pi$ is



$$
\begin{aligned}
 W_n^-&=\frac{B_n}{d_n}E_n-
        \frac{q_n}{d_n}\widetilde L_n\\
 &=\frac{q_nB_n}{d_n}
   \left(\frac{E_n}{q_n}-\frac{|J_n(K)|}{c_n}\right).
                                                               \tag{A17}
 \end{aligned}
$$



The ratio of the first positive term in parentheses to the second is, by
(A7), (A8), and (A12), using $q_n\geq1$,



$$
0\leq
 \frac{c_nE_n}{q_n|J_n(K)|}
 \leq C_3^n n^{m+1/2}\frac{n!}{(2n+1)!}
 \longrightarrow0.                              \tag{A18}
$$



Indeed,



$$
\frac{(2n+1)!}{n!}\geq(n+1)^{n+1},
$$



which dominates every fixed exponential times a fixed power of $n$.
Thus (A17) is eventually negative and has absolute value at least



$$
\frac{q_nB_n}{d_n}\frac{|J_n(K)|}{2c_n}
 \geq\frac{q_n|J_n(K)|}{2c_n}.
$$



After the final content division,



$$
\left|\frac{W_n^-}{g_n}\right|
 \geq\frac{q_n|J_n(K)|}{2c_nB_n}.               \tag{A19}
$$



Combining (A7), (A9), (A11), and either (A16) or (A19), with the harmless
factor $1/2$ absorbed into a fixed constant, gives



$$
|\Lambda_n^{\rm prim}|
 \geq c_4\,
 \frac{n(2n-1)!}{n!}\,
 \frac{4^{-n}n^{-m-1/2}}{C_2^n}.                \tag{A20}
$$



Finally,



$$
\frac{n(2n-1)!}{n!}
 =n\prod_{k=n+1}^{2n-1}k
 \geq n^n.
$$



Therefore the right side of (A20) tends to infinity.  All estimates have
one threshold depending only on the fixed kernel, so the same conclusion
holds along any infinite subset of the relevant even indices, regardless
of how the two signs are interlaced.

## 6. Hidden-case checklist

- **Purely antisymmetric kernel:** impossible under the moment hypothesis,
  because it would give a nontrivial rational relation with $\pi$.
- **Midpoint zero:** an arbitrary finite even order $2m$ is included;
  a nonzero rational function cannot vanish to infinite order.
- **Endpoint zeros or sign changes:** harmless; the beta weight
  concentrates at the midpoint and the exact remainder ratio is
  $O(1/n)$.
- **Poles and removable factors:** the reduced $P/Q$ presentation makes
  $Q$ zero-free on $[0,1]$.  Symmetrization creates no interval pole.
- **Zero rational coordinate:** $r_n=0$ is harmless.  The stipulated
  $c_n>0$ rules out a zero $\pi$-coordinate and ensures $B_n>0$.
- **Parity:** symmetrization and Laplace asymptotics hold for every $n$;
  evenness is used only for the displayed primitive exponential form.
- **Primitive sign orientation:** multiplication by $\sigma=\pm1$
  preserves primitivity, while $B_n=\mu_nc_n$ makes (A15) exact.
- **Minimal matching:** the multipliers are exactly
  $B_n/d_n,q_n/d_n$; their signs in (A16)--(A17) are the ones required
  to produce equal coefficients of $e$ and $\pi$.
- **Large final gcd:** (A14) controls every prime power, so final
  primitive reduction cannot absorb the factorial growth.
- **Sparse relevant set:** every infinite subset of the positive integers
  is unbounded, and the bounds are uniform for all sufficiently large
  relevant indices.

## 7. Markup validation

The frozen target and this audit were checked for valid UTF-8, NUL and C0
control bytes, carriage returns, trailing whitespace, balanced display
math delimiters, and unfinished code fences.  No defect was found.

## Conclusion

The extension from positive kernels to arbitrary fixed real rational
kernels with no pole on the interval is rigorous.  Symmetrization either
annihilates every moment, contradicting the stipulated nonzero
$\pi$-coordinate, or produces a nonzero even analytic germ at the
midpoint.  Its exact beta-moment asymptotic supplies a fixed-sign
exponential lower bound.  Fixed rational arithmetic costs only
exponential height, the content lemma prevents a hidden primitive
collapse, and the factorial size of $q_n$ forces both sign classes of
matched forms to diverge.
