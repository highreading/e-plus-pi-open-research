> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact-contact moment determinants: lattice structure, arithmetic payments, and the remaining primitive-error problem

## 1. Executive conclusion and proof status

The question whether $e+\pi$ is rational or irrational remains unresolved.

This report continues the compact determinant of A5 turn 10. The basic mixed integration-by-parts construction is reused, not claimed as new. The new results concern its contact lattice and its arithmetic normalization.

The main proved results are:

1. **An all-$k$ description of the contact equations as orthogonality for a signed moment functional.** Its leading $k\times k$ Hankel matrix is nonsingular for every $k\ge2$, with exactly one negative eigenvalue. This gives the exact dimension and minimum-degree structure of the contact space.

2. **An exact integer-lattice filtration theorem.** Minimal leading-coefficient payments are quotients of successive lattice indices and therefore telescope. They are not independent factorial payments for each row.

3. **An explicit infinite integer contact basis for $k=3$, proved for all degrees.** Its only nonmonic basis element has leading coefficient $401$; all subsequent basis elements are monic and primitive. The full contact-response lattice has Smith invariants
   

$$
\boxed{2,\ 2,\ 32}.
$$


   This is an all-degree congruence theorem, not an extrapolation from finite examples.

4. **An exact determinant-normalization theorem.** For the minimum-degree square family, changing the rational contact basis changes the determinant only by a rational scalar. Consequently its primitive coefficient pair is basis-independent. In a block-determinant computation, the contact lattice index is an exact common divisor of both coefficients, over all primes.

5. **A complete endpoint and clearer ledger.** All exponential and arctangent rational corrections are specified explicitly. The least simultaneous clearer of the raw monomial correction array is evaluated exactly. For the explicit $k=3$ contact basis, the actual entry clearer is
   

$$
\boxed{45045}.
$$



These results do **not** establish primitive decay or nonvanishing of the whole determinant at infinitely many sizes. An explicit whole-error upper bound is proved below, but its leading arithmetic scale remains


$$
\exp\!\bigl(4k^2\log k+O(k^2)\bigr)
$$


before the final coefficient gcd is removed. The necessary correlated cancellation in that final gcd has not been proved.

Thus the outstanding problem is now more specific: it is not merely “find a contact lattice.” It is to control the **actual primitive coefficient pair and whole determinant error**, including possible cancellation, on one and the same infinite sequence.

---

## 2. Definitions and complete endpoint corrections

Write


$$
z=t^2,\qquad P(t)=p(z),\qquad p\in\mathbb Z[z].
$$


Let


$$
a_m=\mathcal A(t^m),\qquad
\mathcal A(P)=\sum_{r=0}^{\deg P}(-1)^rP^{(r)}(1).
$$


The established recurrence is


$$
a_0=1,\qquad a_m=1-ma_{m-1}.
$$



Define


$$
c_n=a_{2n}-(-1)^n.
$$


Then the $k$ contact equations are exactly


$$
\boxed{\sum_m p_m c_{m+j}=0\qquad(0\le j<k),}
\tag{2.1}
$$


where $p(z)=\sum_m p_mz^m$.

For later arithmetic, define the rational arctangent corrections


$$
\rho_0=0,\qquad
\rho_n=\sum_{\ell=0}^{n-1}\frac{(-1)^\ell}{2n-1-2\ell}
\quad(n\ge1).
$$


Equivalently,


$$
\boxed{\rho_{n+1}+\rho_n=\frac1{2n+1}.}
\tag{2.2}
$$


The complete rational part of the $n$-th even mixed moment is


$$
\boxed{r_n=-(2n)!+4\rho_n.}
\tag{2.3}
$$


Thus


$$
r_0=-1,\qquad
\boxed{
r_{n+1}+r_n
=-(2n+2)!-(2n)!+\frac4{2n+1}.
}
\tag{2.4}
$$



For a contact polynomial $p$, put


$$
u(p)=p(-1).
$$


The compact moment is exactly


$$
\begin{aligned}
M_j(p)
&=\int_0^1\left(e^t+\frac4{1+t^2}\right)t^{2j}p(t^2)\,dt\\
&=(-1)^j u(p)(e+\pi)+\sum_m p_mr_{m+j}.
\end{aligned}
\tag{2.5}
$$



In particular, neither the factorial endpoint term $-(2n)!$ nor any arctangent rational correction is omitted.

---

## 3. A signed-moment theorem for every $k$

### 3.1 The positive measure behind $\mathcal A$

For every even polynomial $P$,


$$
\mathcal A(P)
=\int_0^\infty e^{-v}P(v-1)\,dv.
$$


Indeed, this identity holds on monomials by the factorial-moment formula and the binomial theorem.

Consequently, define a positive functional on $\mathbb R[z]$ by


$$
\mu(q)=\int_0^\infty e^{-v}q((v-1)^2)\,dv.
$$


Its moments are


$$
\mu(z^n)=a_{2n}.
$$


It has a positive density on $(0,\infty)$:


$$
d\mu(z)=
\frac{e^{-1}}{2\sqrt z}
\left(e^{-\sqrt z}
+\mathbf 1_{(0,1)}(z)e^{\sqrt z}\right)\,dz.
\tag{3.1}
$$


In particular,


$$
\mu(1)=1.
$$



The contact functional is


$$
\boxed{L(q)=\mu(q)-q(-1).}
\tag{3.2}
$$


Thus $L(z^n)=c_n$, and contact means


$$
L(z^jp)=0\qquad(0\le j<k).
$$



The subtraction at $-1$ is essential. This is not a positive orthogonality problem.

---

### 3.2 Signature and nonsingularity

Let


$$
C_k=(c_{i+j})_{0\le i,j<k}.
$$



**Theorem 3.1.** For every $k\ge2$, $C_k$ is nonsingular and has inertia


$$
(k-1\text{ positive},\ 1\text{ negative}).
$$


In particular,


$$
\boxed{\det C_k<0.}
\tag{3.3}
$$



**Proof.** On the codimension-one subspace of polynomials $q$ of degree $<k$ satisfying $q(-1)=0$,


$$
L(q^2)=\mu(q^2)>0
$$


unless $q=0$. Hence $C_k$ has at least $k-1$ positive eigenvalues.

Also,


$$
c_0=0,\qquad c_1=2,\qquad c_2=8,
$$


so its leading $2\times2$ principal submatrix is


$$
\begin{pmatrix}0&2\\2&8\end{pmatrix},
$$


whose determinant is $-4$. Therefore the quadratic form has a negative direction. All $k$ eigenvalues are now accounted for, proving the assertion. $\square$

It follows immediately that, for $d\ge k-1$,


$$
\dim_{\mathbb Q}
\{p:\deg p\le d,\ L(z^jp)=0,\ 0\le j<k\}
=d+1-k.
\tag{3.4}
$$


There is no nonzero contact polynomial of degree $<k$, and there is a unique monic contact polynomial of degree $k$.

This theorem is specific to the present signed functional. It is stronger than an unproved rank assumption in a generic kernel search.

---

### 3.3 Evaluation at the pole and the roots of the minimum-degree row

Let $p_k$ denote the monic degree-$k$ contact polynomial.

**Theorem 3.2.** For $k\ge2$,


$$
p_k(-1)\ne0.
$$


Moreover, $p_k$ has exactly one root in $(-\infty,-1)$ and exactly $k-1$ simple roots in $(0,\infty)$.

**Proof.**

First, if $p_k(-1)=0$, write $p_k=(z+1)q$, with $\deg q=k-1$. Contact gives


$$
0=L(p_kq)=\mu((z+1)q^2)>0,
$$


a contradiction.

For the root statement, let $\pi_k$ be the monic degree-$k$ orthogonal polynomial for $\mu$, and let $K_{k-1}(z,-1)$ be the reproducing kernel for polynomials of degree $<k$ in $L^2(\mu)$. Orthogonality gives


$$
p_k(z)=\pi_k(z)+p_k(-1)K_{k-1}(z,-1),
$$


hence


$$
p_k(-1)=
\frac{\pi_k(-1)}{1-K_{k-1}(-1,-1)}.
\tag{3.5}
$$



Because $\mu(1)=1$, the constant polynomial contributes $1$ to the kernel. For $k\ge2$, the degree-one orthogonal polynomial has nonzero value at $-1$, so


$$
K_{k-1}(-1,-1)>1.
$$


All roots of $\pi_k$ lie in $(0,\infty)$, giving


$$
\operatorname{sgn}\pi_k(-1)=(-1)^k.
$$


Thus


$$
\operatorname{sgn}p_k(-1)=(-1)^{k+1}.
$$


Its sign at $-\infty$ is $(-1)^k$, so it has a root below $-1$.

Finally, contact implies


$$
\mu((z+1)z^jp_k)=0\qquad(0\le j<k-1).
$$


The usual sign-change argument for the positive measure $(z+1)d\mu(z)$ gives at least $k-1$ sign changes in $(0,\infty)$. Together with the negative root, this exhausts the degree. $\square$

This proves a nonzero period coefficient for the minimum-degree row. It does **not** prove nonvanishing of a square mixed-moment determinant.

---

## 4. The integer contact lattice and its exact payments

For $d\ge k-1$, let


$$
\Phi_{k,d}=(c_{m+j})_{\substack{0\le j<k\\0\le m\le d}},
$$


and let


$$
\mathscr I_{k,d}=\Phi_{k,d}\mathbb Z^{d+1}\subseteq\mathbb Z^k.
$$


Write


$$
\delta_{k,d}=[\mathbb Z^k:\mathscr I_{k,d}].
$$


Equivalently, $\delta_{k,d}$ is the gcd of all $k\times k$ minors of $\Phi_{k,d}$. Since $C_k$ is nonsingular,


$$
\delta_{k,k-1}=|\det C_k|.
$$



### 4.1 Exact leading-coefficient theorem

**Theorem 4.1.** For $m\ge k$, the least positive leading coefficient of an integer contact polynomial of degree $m$ is


$$
\boxed{
e_{k,m}=\frac{\delta_{k,m-1}}{\delta_{k,m}}.
}
\tag{4.1}
$$


One can choose contact polynomials $B_{k,m}\in\mathbb Z[z]$, of degree $m$ and leading coefficient $e_{k,m}$, such that


$$
\{B_{k,m}:m\ge k\}
$$


is a $\mathbb Z$-basis of the full integer contact lattice. Every $B_{k,m}$ is primitive.

**Proof.** Adjoining the column


$$
v_m=(c_m,\ldots,c_{m+k-1})^T
$$


enlarges $\mathscr I_{k,m-1}$ to $\mathscr I_{k,m}$. The quotient is cyclic, generated by the class of $v_m$, and its order is


$$
[\mathscr I_{k,m}:\mathscr I_{k,m-1}]
=\delta_{k,m-1}/\delta_{k,m}.
$$


That order is precisely the least positive integer $e$ for which


$$
ev_m+\sum_{\ell<m}b_\ell v_\ell=0
$$


with integer $b_\ell$, proving (4.1).

Successive cancellation of leading terms proves that the chosen polynomials form a basis. If all coefficients of one basis element had a common divisor greater than one, division would give a smaller positive allowable leading coefficient, a contradiction. $\square$

The exact aggregate payment is therefore


$$
\boxed{
\prod_{m=k}^{d}e_{k,m}
=\frac{|\det C_k|}{\delta_{k,d}}.
}
\tag{4.2}
$$



This telescoping is important: multiplying a separate denominator bound for every rationally normalized row can seriously overpay.

---

### 4.2 A bounded construction for every fixed $k$

The preceding basis is constructive by integer elimination. There is also a finite bound after which all its leading coefficients are $1$.

Put


$$
D_k=|\det C_k|.
$$


For any positive integer $D$,


$$
a_n\equiv\sum_{r=0}^{D-1}(-1)^r(n)_r\pmod D,
\tag{4.3}
$$


because each falling factorial $(n)_r$ with $r\ge D$ is divisible by $D$. This remains valid for $r>n$, when $(n)_r=0$.

The right side is a polynomial in $n$ modulo $D$, and therefore $a_n$ is periodic modulo $D$, with period $D$. It follows that


$$
c_{m+2D}\equiv c_m\pmod D.
\tag{4.4}
$$


Moreover,


$$
D_k\mathbb Z^k\subseteq C_k\mathbb Z^k.
$$


Thus every response column is generated by the first


$$
\max(k,2D_k)
$$


columns. Consequently,


$$
\boxed{
e_{k,m}=1\qquad
\bigl(m\ge\max(k,2D_k)\bigr).
}
\tag{4.5}
$$



This is a bounded, deterministic construction of an infinite integer basis for every fixed $k$. The bound is far too large for the intended asymptotic application, but it is an actual termination proof, not an unspecified search.

---

### 4.3 A rigorous size bound, and what it does not prove

Set


$$
f_j=4^j(2j)!.
$$


Since


$$
|c_{i+j}|\le2(2i+2j)!
\le2f_if_j,
$$


the determinant expansion gives


$$
\boxed{
D_k\le 2^k k!\prod_{j=0}^{k-1}f_j^2.
}
\tag{4.6}
$$


Hence


$$
\log D_k\le 2k^2\log k+O(k^2).
\tag{4.7}
$$



This is an upper bound on a specific lattice payment. It is **not** a lower bound on the height of every contact basis. In particular, it does not convert the factorial norm of $\mathcal A$ into a universal obstruction.

---

## 5. An explicit infinite contact basis at $k=3$

This section gives a fully evaluated all-degree specialization of the lattice theorem.

Put


$$
d_m=\frac{c_m}{2}.
$$


All $c_m$ are even: the recurrence


$$
a_{2m+2}=(2m+2)(2m+1)a_{2m}-(2m+1)
\tag{5.1}
$$


shows inductively that $a_{2m}$ is odd.

For $m\ge2$, define


$$
\boxed{
Q_m(z)=z^m-d_mz+4d_m-d_{m+1}.
}
\tag{5.2}
$$


These satisfy the first two contact equations. Explicitly,


$$
Q_2=z^2-4z-117,\qquad
Q_3=z^3-133z-6884.
$$



Their remaining $k=3$ response, after division by $2$, is


$$
\boxed{
q_m=d_{m+2}-4d_{m+1}-117d_m.
}
\tag{5.3}
$$



### 5.1 An all-degree congruence

**Lemma 5.1.**


$$
q_m\equiv0\pmod{16}\qquad(m\ge0).
\tag{5.4}
$$



**Proof.** Recurrence (5.1), separated according to the parity of $m$, proves


$$
a_{2m}\equiv 8\left\lfloor\frac m2\right\rfloor+1\pmod{32}.
$$


For example, the two induction steps reduce to the fact that $h(h+1)$ is even. Therefore


$$
d_m\equiv
\begin{cases}
2m,&m\ \text{even},\\
2m-1,&m\ \text{odd}
\end{cases}
\pmod{16}.
$$


Substitution in (5.3), using $117\equiv5\pmod{16}$, gives $-16m$ in either parity case. $\square$

The first two nonzero responses are


$$
q_2=16\cdot401,\qquad
q_3=16\cdot38891.
$$


The exact Bézout identity is


$$
\boxed{6498\cdot401-67\cdot38891=1.}
\tag{5.5}
$$



Define


$$
R(z)=6498Q_2(z)-67Q_3(z).
$$


Its third normalized response is exactly $16$. Now put


$$
\boxed{
T_3(z)=401Q_3(z)-38891Q_2(z)
}
\tag{5.6}
$$


and, for every $m\ge4$,


$$
\boxed{
S_m(z)=Q_m(z)-\frac{q_m}{16}R(z).
}
\tag{5.7}
$$


All coefficients are integers, and every displayed polynomial satisfies all three contact equations.

The exceptional row is explicitly


$$
\boxed{
T_3(z)=401z^3-38891z^2+102231z+1789763.
}
\tag{5.8}
$$



### 5.2 Exact lattice and Smith conclusions

**Theorem 5.2.**


$$
\boxed{\{T_3,S_4,S_5,\ldots\}}
$$


is a $\mathbb Z$-basis of the complete $k=3$ integer contact lattice. Every member is primitive; $S_m$ is monic for every $m\ge4$.

The response lattice has Smith invariants


$$
\boxed{2,\ 2,\ 32.}
\tag{5.9}
$$


Its index in $\mathbb Z^3$ is $128$.

**Proof.** After dividing the response matrix by $2$, its first two columns have an upper $2\times2$ minor of determinant $-1$. Integer elimination reduces the remaining row responses to the $q_m$. Lemma 5.1 and identity (5.5) show that their gcd is exactly $16$. Thus the normalized Smith invariants are $1,1,16$, and the original ones are $2,2,32$.

Any integer contact polynomial can have all terms of degree at least $4$ eliminated using the monic $S_m$. The remaining degree-at-most-three contact lattice is generated by $T_3$, because $\gcd(401,38891)=1$. Primitivity follows either directly or from Theorem 4.1. $\square$

For the minimum-degree three-row family, using $T_3,S_4,S_5$, the exact leading-coefficient payment is


$$
\boxed{401.}
$$


This is a genuine example of correlated elimination reducing repeated row clearings. It does not show that coefficient norms are small: $d_m$, and hence the coefficients in (5.7), still have factorial growth.

---

## 6. Rank-one period structure and primitive basis invariance

Let $p_0,\ldots,p_{k-1}$ be any contact rows. Put


$$
u_r=p_r(-1),\qquad v_j=(-1)^j,
$$


and


$$
B_{rj}=\sum_m p_{r,m}r_{m+j}.
$$


Equation (2.5) gives


$$
\boxed{\mathcal M(s)=B+suv^T,\qquad s=e+\pi.}
\tag{6.1}
$$


Since $uv^T$ has rank at most one,


$$
\boxed{
\det\mathcal M(s)=\alpha_k+\beta_ks
}
\tag{6.2}
$$


with


$$
\alpha_k=\det B,\qquad
\beta_k=v^T\operatorname{adj}(B)u.
$$


This formula does not require $B$ to be invertible.

Thus the determinant is **at most linear**, not necessarily of exact degree one. Proving $\beta_k\ne0$ remains a separate issue.

Now restrict to


$$
\deg p_r\le2k-1.
$$


By (3.4), the contact space has dimension $k$. Any two rational bases differ by a matrix in $\mathrm{GL}_k(\mathbb Q)$, so their determinants differ by a nonzero rational scalar.

**Consequently, whenever the coefficient pair is nonzero, its primitive integer pair is independent of the rational contact basis.**

This is a precise reason not to treat row normalization costs as intrinsic Diophantine costs.

---

## 7. Exact clearers and the block determinant ledger

### 7.1 The raw monomial clearer

For the minimum-degree family, the largest moment index is


$$
N=3k-2.
$$


Define


$$
\boxed{
\Lambda_k=\operatorname{lcm}(1,3,5,\ldots,6k-5).
}
\tag{7.1}
$$



This is the **least** simultaneous denominator clearer of


$$
r_0,\ldots,r_{3k-2}.
$$



Indeed, it clears every term in (2.3). Conversely, if an integer clears all these $r_n$, recurrence (2.4) shows that it clears


$$
\frac4{2n+1}\qquad(0\le n<3k-2).
$$


The denominators are odd and coprime to $4$, proving minimality.

For a particular integer contact basis $X=(p_{r,m})$, its actual entry clearer is


$$
\boxed{
L_X=
\frac{\Lambda_k}
{\gcd\!\left(\Lambda_k,\,
\{\Lambda_k B_{rj}:0\le r,j<k\}\right)}.
}
\tag{7.2}
$$


This may be smaller than the raw clearer. It must not automatically be replaced by $\Lambda_k$.

Since $\Lambda_k\le\operatorname{lcm}(1,\ldots,6k-5)$, the archived elementary lcm bound gives


$$
\log L_X=O(k).
$$


Thus entry clearing contributes at most $O(k^2)$ to a $k\times k$ determinant. The unresolved factorial-scale issue lies elsewhere.

---

### 7.2 The actual $k=3$ entry clearer

For $T_3,S_4,S_5$,


$$
\boxed{L_X=\Lambda_3=45045=3^2\cdot5\cdot7\cdot11\cdot13.}
\tag{7.3}
$$



Here is a direct prime-power verification.

A row of degree $d$, shifted by column $j$, whose leading coefficient is a $p$-adic unit, forces a denominator $p^a$ when


$$
2(d+j)-1=p^a:
$$


the highest correction contains $4/p^a$, whereas all lower-degree corrections have smaller odd denominators and hence lower $p$-adic denominator depth.

Apply this to:

- $T_3$, column $0$: $2\cdot3-1=5$;
- $T_3$, column $1$: $2\cdot4-1=7$;
- $T_3$, column $2$: $2\cdot5-1=9$;
- $S_4$, column $2$: $2\cdot6-1=11$;
- $S_5$, column $2$: $2\cdot7-1=13$.

The leading coefficient $401$ is a unit at $3,5,7$, and the other two rows are monic. These force every prime power in $45045$, while (7.1) supplies the matching upper bound.

This evaluates the entry clearer. It does not yet evaluate the determinant-pair clearer or its final gcd.

---

### 7.3 A block determinant with an exact all-prime index factor

Let


$$
\Phi=\Phi_{k,2k-1},\qquad
\delta=\delta_{k,2k-1}.
$$


Use row indices $0\le m<2k$ and column indices $0\le j<k$, and set


$$
\mathcal R_{mj}=r_{m+j},\qquad
w_m=(-1)^m,\qquad v_j=(-1)^j.
$$


Define the integer polynomial


$$
\boxed{
H_k(s)=
\det\left[
\Phi^T\ \middle|\ 
\Lambda_k\mathcal R+s\Lambda_kwv^T
\right].
}
\tag{7.4}
$$


It is at most linear:


$$
H_k(s)=H_{0,k}+H_{1,k}s,\qquad H_{0,k},H_{1,k}\in\mathbb Z.
$$



If $X$ is a $\mathbb Z$-basis of the integer kernel of $\Phi$, then


$$
\boxed{
H_k(s)=\pm\delta\,\Lambda_k^k\det\mathcal M_X(s).
}
\tag{7.5}
$$



**Proof.** The integer kernel is saturated, so its basis can be completed to a unimodular basis of $\mathbb Z^{2k}$. Multiplication of (7.4) by the corresponding unimodular row matrix gives a block-triangular matrix. Its upper-left block is a basis matrix for the response image, of determinant $\pm\delta$; its lower-right block is $\Lambda_k\mathcal M_X(s)$. $\square$

In particular,


$$
\boxed{\delta\mid H_{0,k},\qquad \delta\mid H_{1,k}.}
\tag{7.6}
$$


This includes prime powers and every prime. It is not merely a square-free divisibility statement.

For $k=3$, the factor in (7.5) is exactly


$$
128\cdot45045^3.
$$



---

### 7.4 The actual primitive pair

Assume $(H_{0,k},H_{1,k})\ne(0,0)$, and define the **final all-prime gcd**


$$
\boxed{G_k=\gcd(|H_{0,k}|,|H_{1,k}|).}
\tag{7.7}
$$


If $H_{1,k}\ne0$, the actual primitive denominator is


$$
\boxed{q_k=\frac{|H_{1,k}|}{G_k},}
\tag{7.8}
$$


with numerator chosen with the corresponding sign. The whole primitive error is exactly


$$
\boxed{
|\ell_k|
=\frac{|H_{0,k}+H_{1,k}(e+\pi)|}{G_k}.
}
\tag{7.9}
$$



Neither $\delta$, a row content, nor an entry clearer may be substituted for $G_k$.

For completeness, if an entry clearer $L_X$ gives


$$
L_X^k\det\mathcal M_X(s)=A_0+A_1s,
$$


then the least clearer of the two determinant coefficients is


$$
\frac{L_X^k}{\gcd(L_X^k,A_0,A_1)}.
$$


After that clearing, the remaining coefficient content is


$$
\frac{\gcd(A_0,A_1)}
{\gcd(L_X^k,A_0,A_1)}.
$$


These are distinct payments.

No simplified all-$k$ evaluation of $G_k$ is proved here.

---

## 8. Explicit coefficient and whole-error bounds

The determinant and final gcd will not be left without any quantitative bounds. The bounds below are rigorous, but insufficient for irrationality.

### 8.1 A coefficient-height bound

The correction formula gives


$$
|r_n|\le5(2n)!,
$$


and therefore


$$
|r_{m+j}+(-1)^{m+j}|\le6f_mf_j.
$$


The determinant expansion at $s=0,1$ gives


$$
|H_{0,k}|\le T_k,\qquad |H_{1,k}|\le2T_k,
\tag{8.1}
$$


where


$$
\boxed{
T_k=(2k)!\,12^k\Lambda_k^k
\left(\prod_{m=0}^{2k-1}f_m\right)
\left(\prod_{j=0}^{k-1}f_j^2\right).
}
\tag{8.2}
$$


Thus, whenever the pair is nonzero,


$$
\boxed{
\delta\le G_k\le2T_k.
}
\tag{8.3}
$$


Also, since all $c_n$ are even,


$$
\delta\ge2^k.
$$



These bounds retain the actual gcd. Their weakness is explicit:


$$
\log T_k=6k^2\log k+O(k^2).
$$



---

### 8.2 A whole-determinant estimate with compact energy retained

Let


$$
h_k=\det_{0\le r,j<k}\frac1{2r+2j+1}.
$$


The Cauchy determinant evaluates it exactly:


$$
\boxed{
h_k=
\frac{2^{k(k-1)}
\left(\prod_{j=1}^{k-1}j!\right)^2}
{\displaystyle\prod_{r,j=0}^{k-1}(2r+2j+1)}.
}
\tag{8.4}
$$


In particular,


$$
\log h_k=-2(\log2)k^2+O(k\log k).
\tag{8.5}
$$



Define


$$
S_k=\frac{(2k)^{k(k-1)/2}}{\prod_{j=1}^{k-1}j!},
\qquad
B_k=2^k k!\prod_{m=0}^{2k-1}f_m.
\tag{8.6}
$$



Then the entire evaluated determinant satisfies


$$
\boxed{
|H_k(e+\pi)|
\le
F_k:=
\Lambda_k^k
\binom{2k}{k}
B_k\,7^kS_kh_k.
}
\tag{8.7}
$$



Here is the derivation.

For the integer kernel basis $X$, its maximal minors are, up to signs, the complementary minors of $\Phi$, divided by $\delta$. This follows from the same unimodular-completion argument as (7.5). Each complementary contact minor has absolute value at most $B_k$.

The mixed weight


$$
e^t+\frac4{1+t^2}
$$


is positive and less than $7$ on $[0,1]$. Andréief’s identity expresses every relevant mixed-moment minor as a positive integral of


$$
\det(x_\ell^{i_r})\det(x_\ell^j),\qquad x_\ell=t_\ell^2.
$$


For increasing indices $i_r\in\{0,\ldots,2k-1\}$,


$$
\det(x_\ell^{i_r})=V(x)\,s_\lambda(x),
$$


where $s_\lambda$ is a Schur polynomial with nonnegative coefficients. On $[0,1]^k$,


$$
s_\lambda(x)\le s_\lambda(1,\ldots,1)
=\prod_{r<s}\frac{i_s-i_r}{s-r}\le S_k.
$$


The remaining Vandermonde-square integral is exactly $h_k$, up to the already included weight bound $7^k$. Summing over the $\binom{2k}{k}$ complementary minors and using (7.5) proves (8.7).

Thus the actual primitive error has the rigorous bound


$$
\boxed{|\ell_k|\le \frac{F_k}{G_k}.}
\tag{8.8}
$$


Its numerator scale is


$$
\boxed{\log F_k=4k^2\log k+O(k^2).}
\tag{8.9}
$$



The compact real-energy contribution (8.5) is retained. It does not, by itself, defeat the factorial-scale arithmetic factor.

---

## 9. What has improved, and the exact obstruction that remains

The new lattice results remove two unjustified inferences.

### 9.1 A factorial functional norm is not a universal basis lower bound

The norm estimate in turn 10 shows that $\mathcal A$ can be factorially large on bounded monomials. It does not show that every integer contact basis must incur that norm independently in every row.

The telescoping identity (4.2), the explicit $k=3$ basis, and primitive basis invariance demonstrate why such an inference would be invalid.

### 9.2 Row normalization is not the final arithmetic normalization

Within the minimum-degree contact space, all rational bases yield the same primitive pair. Therefore a large determinant factor caused solely by changing contact bases disappears completely at primitive reduction.

Nevertheless, this does not prove a favorable final normalization. The unresolved common factor is the actual


$$
G_k=\gcd(H_{0,k},H_{1,k}),
$$


after the endpoint corrections have been included.

### 9.3 Precise remaining mathematical obligations

Two independent statements are still missing:

1. **Whole nonvanishing:** prove
   

$$
H_k(e+\pi)\ne0
$$


   on the selected infinite sizes. The root theorem for one contact polynomial and the positivity of the mixed weight do not prove this determinant statement. The complementary contact minors have signs, so cancellations remain possible.

2. **Paid primitive decay:** prove
   

$$
\frac{|H_k(e+\pi)|}{G_k}\longrightarrow0
$$


   on those same sizes, with $H_{1,k}\ne0$.

A concrete sufficient follow-on lemma is:

> **Primitive contact-determinant lemma sought.** On an explicitly specified infinite set of original indices, prove $H_{1,k}\ne0$, $H_k(e+\pi)\ne0$, and
> 

$$
> \frac{F_k}{G_k}\longrightarrow0,
>
$$


> where $F_k$ is the explicit product in (8.7).

This is stronger than necessary, because (8.7) discards cancellations. A successful alternative could replace it by a sharper signed determinant estimate. Either route must concern the whole evaluated determinant, not only a coefficient or one integral component.

---

## 10. Comparison with the attached obstructions

The attached results remain useful at their stated scopes.

- **Correlated-source Smith obstruction.** Its rank-two beta-response factorization and exact quadratic denominator concern a shared localizer in a different output family. They do not identify the present contact-response matrix or its final coefficient gcd. The present index factor (7.6) is a separate exterior-lattice identity.

- **Positive-derivative divergence theorem.** That theorem uses positivity of two separately primitive forms, minimal coefficient matching, and a specific final-content divisor. Here the determinant is an alternating combination, and the signed functional $L=\mu-\delta_{-1}$ has one negative direction. Its positivity argument and content divisor cannot be imported.

- **Raw-arctangent endpoint family.** The distinction between coefficient nonvanishing and whole-error nonvanishing applies directly. Theorem 3.2 proves $p_k(-1)\ne0$, not $H_k(e+\pi)\ne0$.

- **Family005.** Its reproduced finite certificates and its own infinite bridges are not contact-lattice, gcd, or nonvanishing theorems for this determinant. No closed certificate calculation is repeated here.

The basic mixed coefficient matching is already covered by the supplied archive and the literature gate. The new claims of this report are the signed-Hankel, integer-filtration, explicit $k=3$, and normalization results above.

---

## 11. Preservation of the original binary family

Nothing above identifies the compact determinant with the original binary reconstruction.

The original domain remains


$$
\boxed{
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
}
$$


The contact range remains $0,\ldots,b-1$, while physical reconstruction remains $0,\ldots,b$, with


$$
z_b=0.
$$


The complete corrected columns remain


$$
\boxed{
x=\frac12RA^{-1}f,\qquad
y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},
\qquad x=2^ax_0.
}
$$


In particular, neither $h^F$ nor the endpoint vector $e_0$ is dropped.

The paid scalar acceptance is still


$$
S=\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f,
\qquad
\frac{S}{2^{a+1}}\in\mathbb Z.
$$


If the full-return theorem is accepted, its consequence after payment is only


$$
v_2\!\left(\frac{S}{2^{a+1}}\right)\ge\chi-a,
\qquad
\chi=v_2\binom{n+b-1}{b-1}.
$$


The subtraction of $a$ is indispensable.

The norm


$$
Q=x_0^Tx_0,
$$


the actual corrected-column contents, the least simultaneous clearer, and the final all-prime scalar gcd remain part of that original problem. The supplied material does not provide enough information to evaluate all of them here; no compact-determinant quantity is substituted for them.

The established original denominator valuation remains


$$
\boxed{v_3(q)=n-\frac{b+15}{2}.}
$$



If the compact construction is tested on the same original parameter set, one may set


$$
k=b(u).
$$


Then all compact estimates and nonvanishing claims must hold on one common infinite subset of those $u$. This indexing does **not** establish an identity with the original binary approximants, and it transfers none of their arithmetic or analytic gains.

---

## 12. Bounded exact-arithmetic check and final research status

No numerical experiment is needed for the all-degree proofs above. One small, new arithmetic check would independently audit the normalization formulas without repeating the closed turn-10 computation.

### Proposed bounded check: the $k=3$ arithmetic ledger

**Mathematical inputs**

- The recurrence $a_0=1,\ a_m=1-ma_{m-1}$, through $m=14$.
- Definitions (5.2)–(5.8), producing $T_3,S_4,S_5$.
- Corrections $r_0,\ldots,r_7$ from (2.2)–(2.3).
- The $3\times6$ matrix $\Phi_{3,5}$.
- The $6\times6$ block determinant (7.4).

**Expected verifiable outputs**

1. All nine contact equalities for $T_3,S_4,S_5$.
2. Smith invariants $2,2,32$ for $\Phi_{3,5}$.
3. Primitive contents $1,1,1$ of the three rows.
4. Actual entry clearer $45045$.
5. The exact two integer coefficients $H_{0,3},H_{1,3}$, their all-prime gcd, and the resulting primitive pair.
6. Verification of
   

$$
H_3(s)=\pm128\cdot45045^3\det\mathcal M_X(s).
$$



This is a bounded exact-integer/rational calculation. It would check one normalization ledger only. It would not establish an infinite gcd estimate, a useful infinite sequence, or irrationality.

### Final conclusion

The new proved advance is an explicit structural and arithmetic description of the compact contact construction: nonsingular signed contact matrices for every $k\ge2$, telescoping integer-basis payments, a complete infinite $k=3$ basis with evaluated Smith data and entry clearer, and a basis-independent primitive determinant normalization.

The remaining bottleneck is exact and substantive:


$$
\boxed{
\text{control the final all-prime }G_k
\text{ and the nonzero whole error }
H_k(e+\pi)
\text{ on the same infinite sizes.}
}
$$



The present work neither proves primitive decay nor proves divergence for this family. It therefore proves no rationality or irrationality theorem for $e+\pi$.
