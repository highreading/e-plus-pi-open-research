> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5 Turn 12: Orthogonal compression of the complete compact determinant

## 1. Result and proof status

The rationality or irrationality of $e+\pi$ remains unresolved.

This report does **not** evaluate the all-size Smith invariants or the maximal-minor gcd


$$
\delta_{k,2k-1}.
$$


Nor does it infer such an evaluation from the finite $k=2,\ldots,10$ receipt. Instead, it follows the assignment’s alternative route: a sharper estimate for the **whole evaluated signed determinant**, obtained by an exact orthogonal compression of the original $2k\times2k$ block matrix.

The new result is the bound


$$
\boxed{
|H_k(e+\pi)|
\le F_k^\perp
:=
\Lambda_k^k\,21^k k!\,h_k
\prod_{r=0}^{k-1}(2k+4r)! ,
\qquad k\ge2,
}
\tag{1.1}
$$


where


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5)
$$


and


$$
h_k=
\frac{2^{k(k-1)}
\left(\prod_{j=1}^{k-1}j!\right)^2}
{\prod_{r,j=0}^{k-1}(2r+2j+1)}.
$$



This is not another application of a generic factorial matrix norm. Its proof first compresses the complete evaluated block determinant into:

1. a positive compact Hankel determinant; and
2. a signed $k\times k$ cross-moment determinant involving compact orthogonal polynomials.

That compression eliminates the sum over complementary contact minors and its Schur-polynomial amplification.

Compared with the previous bound $F_k$ in Turn 11,


$$
\boxed{
\log\frac{F_k^\perp}{F_k}
=-c_*k^2+O(k\log k),
\qquad
c_*=\frac{17}{2}\log2-\frac92\log3+\frac34>0.
}
\tag{1.2}
$$


Numerically $c_*$ is approximately $1.698$. Thus the improvement is an exponential factor of order $\exp(-1.698\,k^2)$, not merely a polynomial factor.

The leading factorial scale nevertheless remains


$$
\log F_k^\perp=4k^2\log k+O(k^2).
$$


Consequently, this improvement does not yet establish primitive decay. The final all-prime gcd and whole-error nonvanishing remain essential.

---

## 2. Original compact objects and the accepted arithmetic ledger

Throughout the compact construction,


$$
k\ge2,\qquad 0\le m<2k,\qquad 0\le j<k.
$$



Let


$$
a_0=1,\qquad a_d=1-da_{d-1},
$$


and define


$$
c_n=a_{2n}-(-1)^n.
$$


The complete contact matrix is


$$
\Phi_{k,2k-1}=(c_{j+m})_{\substack{0\le j<k\\0\le m<2k}}.
$$



The positive measure $\mu$ on $[0,\infty)$ satisfies


$$
\int z^n\,d\mu(z)=a_{2n}.
$$


The actual signed contact functional is


$$
L(f)=\int f\,d\mu-f(-1).
\tag{2.1}
$$


In particular, the negative point mass is retained.

The rational corrections are


$$
\rho_0=0,\qquad
\rho_{n+1}+\rho_n=\frac1{2n+1},
$$


and


$$
r_n=-(2n)!+4\rho_n.
\tag{2.2}
$$


No factorial endpoint or rational arctangent correction is removed.

Write


$$
\mathcal R_{mj}=r_{m+j},\qquad
w_m=(-1)^m,\qquad v_j=(-1)^j.
$$


The integer affine polynomial under study remains exactly


$$
H_k(s)=
\det\left[
\Phi_{k,2k-1}^{T}
\ \middle|\
\Lambda_k\mathcal R+s\Lambda_kwv^T
\right]
=H_{0,k}+H_{1,k}s.
\tag{2.3}
$$



### 2.1 What is reused

The supplied proofs establish, at their stated scope:

- $C_k=(c_{i+j})_{0\le i,j<k}$ is nonsingular with inertia $(k-1,1)$.
- The integer contact kernel is saturated.
- Its exact successive leading-coefficient payments telescope:
  

$$
\prod_{m=k}^{2k-1}e_{k,m}
  =\frac{|\det C_k|}{\delta_{k,2k-1}}.
$$


- For a saturated integer kernel basis $X$,
  

$$
H_k(s)=\pm\delta_{k,2k-1}\Lambda_k^k\det\mathcal M_X(s).
  \tag{2.4}
$$


- Rational changes of contact basis do not change the primitive coefficient pair, when that pair is nonzero.

These facts do not identify a monic-row clearer with the saturation payment, and do not identify either with the final coefficient gcd.

### 2.2 Review of the parent divisor

Set


$$
D_s=\prod_{r=0}^{s-1}(r!)^2.
$$


The parent’s integral Laguerre-frame argument gives


$$
D_{k-1}\mid\delta_{k,2k-1}.
\tag{2.5}
$$



The proof has the required hypotheses:

1. the full charge measure has a monic integral orthogonal frame with norms $(r!)^2$;
2. the even monomials have integral coordinates in that frame;
3. every size-$s$ cross-moment minor is consequently divisible by $D_s$;
4. subtracting the actual rank-one negative mass changes a size-$k$ determinant by size-$(k-1)$ cofactors.

Thus


$$
D_{k-1}\mid H_{0,k},H_{1,k}.
$$


This is valid all-prime divisibility. It is not an evaluation of either $\delta_{k,2k-1}$ or the final gcd.

The finite Smith receipt is consistent with this result, but its scope remains $k=2,\ldots,10$.

---

## 3. The complete evaluated determinant as a two-measure determinant

Introduce the positive compact measure $\nu$ on $[0,1]$ by


$$
\int f(z)\,d\nu(z)
=
\int_0^1
f(t^2)\left(e^t+\frac4{1+t^2}\right)\,dt.
\tag{3.1}
$$


Let


$$
\nu_n=\int z^n\,d\nu(z).
$$



The complete mixed-moment identity, before imposing any contact relation, is


$$
\nu_n=e\,a_{2n}+\pi(-1)^n+r_n.
$$


Since $a_{2n}=c_n+(-1)^n$,


$$
\boxed{
\nu_n=e\,c_n+(e+\pi)(-1)^n+r_n.
}
\tag{3.2}
$$



Let


$$
N_{mj}=\nu_{m+j}.
$$


At $s=e+\pi$, the right block of (2.3) is therefore


$$
\Lambda_k(N-e\Phi^T).
$$


Adding $e\Lambda_k$ times each corresponding contact column to the right block yields the exact identity


$$
\boxed{
H_k(e+\pi)
=
\Lambda_k^k
\det\left[\Phi^T\mid N\right].
}
\tag{3.3}
$$



This is an equality over $\mathbb R$, used only for estimating the already-defined integer linear form. It does not constitute an arithmetic change of its coefficients, and it introduces no unrecorded denominator payment.

---

## 4. New structural theorem: exact orthogonal compression

Let $P_n$ be the monic degree-$n$ orthogonal polynomial for $\nu$. This polynomial exists uniquely because $\nu$ has positive density on $(0,1)$.

Put


$$
h_n^\nu=\int P_n(z)^2\,d\nu(z)>0,
$$


and


$$
J_k^\nu=\det(\nu_{i+j})_{0\le i,j<k}
=\prod_{n=0}^{k-1}h_n^\nu.
\tag{4.1}
$$



Define the signed residual matrix


$$
T^{(k)}_{rj}
=
L\!\left(z^jP_{k+r}(z)\right),
\qquad 0\le r,j<k.
\tag{4.2}
$$



### Theorem 4.1

For every $k\ge2$,


$$
\boxed{
H_k(e+\pi)
=
(-1)^{k^2}\Lambda_k^k
J_k^\nu\det T^{(k)}.
}
\tag{4.3}
$$



### Proof

In (3.3), replace the monomial row polynomials


$$
1,z,\ldots,z^{2k-1}
$$


by


$$
P_0,P_1,\ldots,P_{2k-1}.
$$


Because these polynomials are monic, the row transformation is lower triangular with diagonal entries $1$. Its determinant is exactly $1$.

After the transformation, the contact block has entries


$$
L(z^jP_n),
$$


and the compact block has entries


$$
\int z^jP_n(z)\,d\nu(z).
$$



For $n\ge k$ and $j<k$, orthogonality makes every entry in the lower compact block zero.

For $0\le n,j<k$, the compact block is upper triangular: its entry is zero when $j<n$, while its diagonal entry is


$$
\int z^nP_n\,d\nu
=\int P_n^2\,d\nu=h_n^\nu,
$$


because $z^n-P_n$ has degree less than $n$.

Thus the transformed matrix has block form


$$
\begin{pmatrix}
A&B\\
T^{(k)}&0
\end{pmatrix},
\qquad
\det B=J_k^\nu.
$$


Exchanging the two groups of $k$ columns has sign $(-1)^{k^2}$, and produces a block upper-triangular matrix. Equation (4.3) follows. $\square$

### Consequences and limits

Since $J_k^\nu>0$,


$$
\boxed{
H_k(e+\pi)\ne0
\quad\Longleftrightarrow\quad
\det T^{(k)}\ne0.
}
\tag{4.4}
$$



This locates the remaining signed cancellation in one explicit matrix. It does not prove that cancellation is absent.

The matrix $T^{(k)}$ is not a Gram matrix. Positivity of $\nu$, or the one-negative-direction theorem for $L$, does not imply its nonsingularity.

---

## 5. Derivation of the improved whole-error bound

### 5.1 Root bounds for the compact orthogonal polynomials

Every $P_n$ has $n$ simple roots in $(0,1)$.

For completeness, the usual sign-change proof applies here: if $P_n$ had fewer than $n$ sign changes in the interior of the support, multiplication by the product of its sign-changing factors would produce a polynomial of degree less than $n$ whose product with $P_n$ has fixed nonzero sign almost everywhere. That contradicts orthogonality.

Writing those roots as $\xi_1,\ldots,\xi_n$, we have


$$
P_n(z)=\prod_{\ell=1}^n(z-\xi_\ell).
$$


Consequently,


$$
|P_n(z)|\le1\quad(0\le z\le1),
\tag{5.1}
$$




$$
|P_n(z)|\le z^n\quad(z\ge1),
\tag{5.2}
$$


and


$$
|P_n(-1)|\le2^n.
\tag{5.3}
$$



These inequalities are the source of the improvement: no Schur-polynomial expansion or sum over contact minors is needed.

### 5.2 Bounds for the signed residual entries

Let


$$
n=k+r,\qquad N=n+j.
$$


Using (2.1) and (5.1)–(5.3),


$$
\begin{aligned}
|T^{(k)}_{rj}|
&\le
\int z^j|P_n(z)|\,d\mu(z)+|P_n(-1)|\\
&\le
1+a_{2N}+2^n.
\end{aligned}
\tag{5.4}
$$



For $N\ge1$,


$$
0<a_{2N}\le(2N)!.
$$


Indeed, $a_{2N}/(2N)!$ is the even partial sum of the alternating series for $e^{-1}$, and is at most $1$.

Also $N\ge n\ge2$, so


$$
2^n\le(2N)!.
$$


Therefore


$$
\boxed{
|T^{(k)}_{rj}|
\le3(2k+2r+2j)!.
}
\tag{5.5}
$$



### 5.3 Which factorial product dominates the determinant expansion?

For nonnegative integers $a\le b$ and $c\le d$, factorial log-convexity gives


$$
(2a+2c)!(2b+2d)!
\ge
(2a+2d)!(2b+2c)!.
\tag{5.6}
$$


One way to check this is to compare the ratios obtained by increasing the second argument from $c$ to $d$: the ratio is larger when the first argument is larger.

Thus swapping an inversion of a permutation cannot decrease


$$
\prod_{r=0}^{k-1}(2k+2r+2\sigma(r))!.
$$


The maximum occurs at the identity permutation. The determinant expansion and (5.5) therefore imply


$$
\boxed{
|\det T^{(k)}|
\le
3^k k!\prod_{r=0}^{k-1}(2k+4r)!.
}
\tag{5.7}
$$



### 5.4 Retaining the compact energy

On $0\le t\le1$,


$$
0<e^t+\frac4{1+t^2}<7.
$$


Hence, in positive-semidefinite order,


$$
(\nu_{i+j})_{i,j<k}
\preceq
7\left(\frac1{2i+2j+1}\right)_{i,j<k}.
$$


Both matrices are positive definite. Determinant monotonicity gives


$$
J_k^\nu\le7^k h_k.
\tag{5.8}
$$



Combining (4.3), (5.7), and (5.8) proves (1.1).

---

## 6. Quantified improvement over Turn 11

The former bound was


$$
F_k=
\Lambda_k^k
\binom{2k}{k}
\,2^k k!
\left(\prod_{m=0}^{2k-1}4^m(2m)!\right)
7^kS_kh_k,
$$


where


$$
S_k=\frac{(2k)^{k(k-1)/2}}{\prod_{j=1}^{k-1}j!}.
$$


Thus the exact ratio of the two explicit bounds is


$$
\frac{F_k^\perp}{F_k}
=
\frac{(3/2)^k}{\binom{2k}{k}S_k}
\frac{\prod_{r=0}^{k-1}(2k+4r)!}
{\prod_{m=0}^{2k-1}4^m(2m)!}.
\tag{6.1}
$$



Stirling summation gives


$$
\log\prod_{r=0}^{k-1}(2k+4r)!
=
4k^2\log k+
\left(\frac92\log6-\frac12\log2-6\right)k^2
+O(k\log k),
$$




$$
\log\prod_{m=0}^{2k-1}4^m(2m)!
=
4k^2\log k+(6\log4-6)k^2+O(k\log k),
$$


and


$$
\log S_k=
\left(\frac12\log2+\frac34\right)k^2+O(k\log k).
$$


Substitution proves (1.2).

This is a genuine improvement in the whole-error budget, but not a reduction of its $4k^2\log k$ leading term.

---

## 7. Arithmetic payments remain separate

For a saturated integer contact basis $X$, let


$$
B_{rj}=\sum_m X_{rm}r_{m+j}.
$$


Its actual entry clearer is still


$$
L_X=
\frac{\Lambda_k}
{\gcd\!\left(\Lambda_k,\{\Lambda_kB_{rj}\}_{r,j}\right)}.
\tag{7.1}
$$


The new real orthogonal compression neither evaluates nor changes this number.

If


$$
L_X^k\det\mathcal M_X(s)=A_0+A_1s,
$$


then the least simultaneous clearer of the two rational determinant coefficients is


$$
\frac{L_X^k}{\gcd(L_X^k,A_0,A_1)}.
$$


The remaining integer content after that clearing is


$$
\frac{\gcd(A_0,A_1)}{\gcd(L_X^k,A_0,A_1)}.
$$



Finally, for the original block coefficients,


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|).
$$


When $H_{1,k}\ne0$, the actual primitive denominator and whole error are


$$
q_k=\frac{|H_{1,k}|}{G_k},
\qquad
|\ell_k|=
\frac{|H_k(e+\pi)|}{G_k}.
$$


The new proved estimate is therefore precisely


$$
\boxed{
|\ell_k|\le\frac{F_k^\perp}{G_k}.
}
\tag{7.2}
$$



Using only the parent divisor gives the weaker valid estimate


$$
|\ell_k|\le\frac{F_k^\perp}{D_{k-1}}.
$$


Its upper-bound logarithm still has leading term


$$
3k^2\log k+O(k^2).
$$


This does not tend to $-\infty$. It says that the available estimates remain insufficient—not that the actual primitive errors diverge.

---

## 8. Original binary domain and boundaries are unchanged

The original domain remains


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
$$


Its contact indices remain $0,\ldots,b-1$; physical reconstruction remains $0,\ldots,b$, with terminal condition


$$
z_b=0.
$$



The complete corrected columns remain


$$
x=\frac12RA^{-1}f,\qquad
y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},
\qquad x=2^ax_0.
$$


Neither $h^F$ nor $e_0$ is omitted.

The accepted full-return divisor applies to


$$
S=\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f.
$$


After the paid division, its consequence retains the subtraction of $a$:


$$
v_2\!\left(\frac{S}{2^{a+1}}\right)\ge\chi-a,
\qquad
\chi=v_2\binom{n+b-1}{b-1}.
$$


The original norm $Q=x_0^Tx_0$, actual corrected-column contents, simultaneous clearer, and final all-prime gcd are not evaluated by the present compact argument.

Likewise, the original valuation


$$
v_3(q)=n-\frac{b+15}{2}
$$


is not transferred to the compact family.

The new compact theorem holds, in particular, on the explicit infinite set


$$
k=9^{18+32u},\qquad u\ge0.
$$


This is an indexing statement only. No primitive-decay conclusion is proved on that set.

---

## 9. Concrete next lemma and bounded verification

### 9.1 The sharper outstanding lemma

A sufficient next result, now with a strictly smaller explicit numerator budget, is:

> On an explicit infinite subset $U\subseteq\mathbb Z_{\ge0}$, with  
> $k=9^{18+32u}$, prove simultaneously
> 

$$
> H_{1,k}\ne0,\qquad
> \det T^{(k)}\ne0,\qquad
> \frac{F_k^\perp}{G_k}\longrightarrow0.
>
$$



By (4.3), the middle condition is exactly whole-error nonvanishing. The first and third conditions concern the actual primitive integer pair, not a row normalization.

If these statements held, rationality $e+\pi=A/B$ would force every nonzero primitive error to be at least $1/B$, contradicting its convergence to zero.

A potentially weaker sufficient result could estimate the signed determinant $\det T^{(k)}$ directly rather than use (5.7). Its entries have now been specified explicitly, with both the positive charge and negative mass retained.

### 9.2 Optional bounded exact-arithmetic audit

No new finite Smith search is required for this proof. A small audit can check the compression mechanism without repeating any closed arithmetic certificate.

**Inputs**

For the auxiliary rational compact measure $dt$ under $z=t^2$, take


$$
\widehat\nu_n=\frac1{2n+1},\qquad 0\le n\le8.
$$


Take $k=2$, and compute $c_0,\ldots,c_4$ from the stated recurrence.

**Expected verifiable outputs**

1. The monic orthogonal polynomials $\widehat P_0,\ldots,\widehat P_3$, computed by rational Gram elimination.
2. Their exact orthogonality against lower monomials.
3. The identity
   

$$
\det\!\left[
   (c_{m+j})_{\substack{m<4\\j<2}}
   \ \middle|\
   (\widehat\nu_{m+j})_{\substack{m<4\\j<2}}
   \right]
   =
   \det(\widehat\nu_{i+j})_{i,j<2}
   \det\!\left(
   L(z^j\widehat P_{2+r})
   \right)_{r,j<2}.
$$



All inputs and outputs are rational and bounded. This audits only the block-compression algebra. It supplies no evidence for nonvanishing or decay in the actual exponential/arctangent family.

---

## 10. Conclusion

The new proved advance is an exact orthogonal compression of the **complete evaluated** compact determinant, together with the strictly sharper whole-error estimate


$$
|H_k(e+\pi)|
\le
\Lambda_k^k21^kk!h_k
\prod_{r=0}^{k-1}(2k+4r)!.
$$


It improves the previous explicit bound by


$$
\exp\!\left(-c_*k^2+O(k\log k)\right),
\qquad c_*>0,
$$


for all sufficiently large sizes, including the original-index choice $k=9^{18+32u}$.

The exact remaining bottleneck is still


$$
\boxed{
\text{a sufficiently large final all-prime }G_k
\text{ and nonzero whole signed determinant,
on the same infinite original indices.}
}
$$



No all-size Smith formula, primitive-decay theorem, or unconditional rationality or irrationality theorem for $e+\pi$ has been established.
