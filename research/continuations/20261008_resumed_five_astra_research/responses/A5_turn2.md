> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Large-prime contact transversality and two-border content depth for the complete compact pencil

## 1. Results and proof status

The rationality or irrationality of


$$
s_0=e+\pi
$$


remains unresolved.

The completed auxiliary $11\to12$ certificate definitively refutes the unrestricted $S$-unit claim for the **paid Schur transfer**. It does not establish an eventual failure, an original-index failure, or a large-prime divisor of the different final content $G_k$. That calculation is not repeated here.

The analytic comparison in A4 Turn 1 is also closed and is reused at its proved scope. The remaining problem is arithmetic.

This report proves the following additional statements.

### New proved statements

1. **Large-prime transversality of the positive contact array.** Let
   

$$
U_k=(a_{2(m+j)})_{\substack{0\le m<2k\\0\le j<k}}.
$$


   For every $k\ge2$ and every prime $p>k$,
   

$$
\boxed{\operatorname{rank}_{\mathbf F_p}U_k=k.}
   \tag{1.1}
$$


   The proof uses only the original moments through $3k-2$.

2. **A consequence for the complete contact matrix, with its atom retained.** For
   

$$
C_k=(c_{m+j}),\qquad v=(( -1)^j)_{j<k},
$$


   one has
   

$$
\boxed{
   \operatorname{rank}_{\mathbf F_p}
   \begin{pmatrix}C_k\\v^T\end{pmatrix}=k,
   \qquad
   \operatorname{rank}_{\mathbf F_p}C_k\ge k-1
   \quad(p>k).
   }
   \tag{1.2}
$$


   Consequently,
   

$$
\boxed{
   \operatorname{rad}\bigl(\delta_{k-1}(C_k)\bigr)
   \mid \operatorname{rad}(k!),
   }
   \tag{1.3}
$$


   where $\delta_h$ denotes the gcd of all $h\times h$ minors. Thus, outside the primes at most $k$, at most **one** contact Smith invariant can be nonunit. Its depth is not bounded by this theorem.

3. **An evaluated small-prime certificate for the complete right forcing.** The complete returns satisfy
   

$$
\tau_n+\bigl((2n+2)!+(2n)!\bigr)=\frac4{2n+1}.
$$


   A specified $k\times k$ determinant of this forcing equals the nonzero integer
   

$$
\boxed{
   \Theta_k=
   (4\Lambda_k)^k
   \frac{
   2^{k(k-1)}\displaystyle\prod_{r=1}^{k-1}(r!)^2
   }{
   \displaystyle\prod_{i,j=0}^{k-1}(2i+2j+1)
   }.
   }
   \tag{1.4}
$$


   Every prime divisor of $\Theta_k$ is at most $6k-5$, and
   $\log\Theta_k=O(k^2)$. This is a paid matrix-minor certificate, not merely scalar primitivity.

4. **An all-prime content-depth bound for two explicit original rectangles.** Define
   

$$
Z_k=
   \left[
   (c_{m+j})_{\substack{0\le m<2k\\0\le j<k}}
   \ \middle|\
   (\Lambda_k\tau_{m+j})_{\substack{0\le m<2k\\0\le j<k-1}}
   \right],
   \tag{1.5}
$$


   and
   

$$
Y_k=
   \left[
   (\sigma_{m+j})_{\substack{0\le m<2k-1\\0\le j<k}}
   \ \middle|\
   (\Lambda_k\tau_{m+j})_{\substack{0\le m<2k-1\\0\le j<k}}
   \right],
   \tag{1.6}
$$


   where
   

$$
\sigma_n=c_{n+1}+c_n,\qquad \tau_n=r_{n+1}+r_n.
$$


   Put
   

$$
\mathscr R_k=\delta_{2k-1}(Z_k),\qquad
   \mathscr L_k=\delta_{2k-1}(Y_k).
$$


   Whenever $H_{1,k}\ne0$,
   

$$
\boxed{
   \operatorname{lcm}(\mathscr R_k,\mathscr L_k)
   \mid G_k
   \mid \Lambda_k\mathscr R_k\mathscr L_k.
   }
   \tag{1.7}
$$


   In particular, for every prime $p>6k-4$,
   

$$
\boxed{
   \max\{v_p(\mathscr R_k),v_p(\mathscr L_k)\}
   \le v_p(G_k)
   \le v_p(\mathscr R_k)+v_p(\mathscr L_k).
   }
   \tag{1.8}
$$


   Thus the large-prime support of $G_k$ is exactly the union of the large-prime supports of these two **actual rectangular determinantal contents**.

5. **A justified local reduction of the full pencil.** At every prime $p>6k-4$, the original $2k\times2k$ pencil can be reduced, using only $p$-adic units, to a specified $(k+1)\times(k+1)$ bordered pencil. Its two coefficients are
   

$$
h\det\mathsf B+r\,\operatorname{adj}(\mathsf B)b,
   \qquad
   e_0^T\operatorname{adj}(\mathsf B)b.
   \tag{1.9}
$$


   This identifies the exact remaining rank/cofactor obstruction.

These results do **not** prove that $G_k$ has only small-prime support. They also do not give a content upper bound with leading coefficient below $4$, or a successful primitive-error sequence.

The principal advance is that the matrix step is now more sharply localized: large-prime contact degeneracy has at most one invariant factor, and the complete affine-content problem has an exact two-border depth bound and a smaller local cofactor model.

---

## 2. Original objects, boundaries, and established inputs

### 2.1 The unchanged compact pencil

Throughout,


$$
k\ge2,\qquad 0\le m<2k,\qquad 0\le j<k.
$$



Retain


$$
a_0=1,\qquad a_d=1-da_{d-1},
$$




$$
u_n=a_{2n},\qquad f_n=(2n)!,\qquad w_n=(-1)^n,
$$




$$
c_n=u_n-w_n,
$$




$$
\rho_0=0,\qquad \rho_{n+1}+\rho_n=\frac1{2n+1},
$$




$$
r_n=-f_n+4\rho_n.
$$



The original integer affine polynomial is


$$
H_k(s)=
\det\left[
(c_{m+j})\ \middle|\
\bigl(\Lambda_k[r_{m+j}+s(-1)^{m+j}]\bigr)
\right],
\tag{2.1}
$$


where


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5).
$$



Write


$$
H_k(s)=H_{0,k}+H_{1,k}s.
$$


The actual normalization remains


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|),
$$




$$
q_k=\frac{|H_{1,k}|}{G_k},
\qquad
p_k=-\frac{\operatorname{sgn}(H_{1,k})H_{0,k}}{G_k}.
\tag{2.2}
$$



No lower divisor, rectangular content, Schur numerator, or local unit is substituted for this final all-prime gcd.

The finite limits are exactly


$$
m+j\le3k-2,\qquad
\max\text{ factorial}=(6k-4)!,\qquad
\max\text{ odd denominator}=6k-5.
\tag{2.3}
$$



### 2.2 Closed analytic input

For the same complete determinants and primitive pairs, A4 Turn 1 proves, for $k\ge64$,


$$
0<\varepsilon_k=s_0-\frac{p_k}{q_k},
\qquad
0<\varepsilon_{k+1}\le\frac14\varepsilon_k,
\tag{2.4}
$$


and, with


$$
A=17+12\sqrt2,
$$




$$
\frac{3}{4k^2A^{k-1}}
\le\varepsilon_k
\le\frac{63}{2A^{k-1}}.
\tag{2.5}
$$



Its Christoffel applications have the required positive-definiteness hypotheses: the measures actually used have positive density on $(0,1)$. Its signed atom and overlap terms were paid before passing to the whole determinant. Those proofs are not reopened.

The whole primitive error is still


$$
\boxed{
\ell_k=q_ks_0-p_k
=\frac{|H_k(s_0)|}{G_k}>0.
}
\tag{2.6}
$$



The accepted raw scales are


$$
\log|H_k(s_0)|=4k^2\log k+O(k^2),
\qquad
\log|H_{1,k}|=4k^2\log k+O(k^2).
\tag{2.7}
$$


Ordinary-error contraction does not cancel $G_k$ from (2.6).

### 2.3 Closed arithmetic payments

The actual raw right-column clearers are


$$
\Lambda_{k,j}
=\operatorname{lcm}(1,3,\ldots,4k+2j-3),
$$


and


$$
E_k=\frac{\Lambda_k^k}{\prod_{j=0}^{k-1}\Lambda_{k,j}}.
\tag{2.8}
$$



Reuse the proved product divisor


$$
\mathcal P_k=
E_k\,2^{k(k-1)}
\prod_{r=0}^{k-2}(r!)^2,
\qquad
\boxed{\mathcal P_k\mid G_k.}
\tag{2.9}
$$



The shared powers of $2$ in this product have already been paid by the contact-minor proof. They are not multiplied in a second time.

Also retained are the exact transformed contact-column contents


$$
2^{\max(1,j)},
$$


and the actual clearer $(2k-1+j)!$ for a complete factorial-normalized contact column. That normalization is not used in the new arguments.

For the rational polynomial $H_k/\Lambda_k^k$, the actual least simultaneous coefficient clearer remains


$$
\frac{\Lambda_k^k}{d_{H,k}},
\qquad
d_{H,k}=\gcd(\Lambda_k^k,H_{0,k},H_{1,k}),
\tag{2.10}
$$


and its content after that clearing is $G_k/d_{H,k}$.

---

## 3. The complete forced displacement, including all shift commutators

The new rank argument must not be confused with homogeneous inheritance from a scalar recurrence.

Put


$$
P_n=(2n+1)(2n+2)=4n^2+6n+2.
$$


The original moments satisfy


$$
u_{n+1}=P_nu_n-(2n+1),
\qquad
f_{n+1}=P_nf_n.
\tag{3.1}
$$



With the already paid $\Lambda_k$, the complete five-state system is


$$
\begin{pmatrix}
u_{n+1}\\ f_{n+1}\\ \Lambda_k\rho_{n+1}\\ w_{n+1}\\1
\end{pmatrix}
=
\begin{pmatrix}
P_n&0&0&0&-(2n+1)\\
0&P_n&0&0&0\\
0&0&-1&0&\Lambda_k/(2n+1)\\
0&0&0&-1&0\\
0&0&0&0&1
\end{pmatrix}
\begin{pmatrix}
u_n\\ f_n\\ \Lambda_k\rho_n\\ w_n\\1
\end{pmatrix}.
\tag{3.2}
$$



For the size-$k$ object this is used only for


$$
0\le n\le3k-3.
$$


Its determinant is $P_n^2$; its inverse has actual least simultaneous entry clearer $P_n$. Hence these state transitions are regular at every prime $p>6k-4$.

That fact alone says nothing about matrix primitivity.

### 3.1 Exact rectangular displacement

Let


$$
M=\operatorname{diag}(0,1,\ldots,2k-2),
\qquad
J=\operatorname{diag}(0,1,\ldots,k-1),
$$


and


$$
B_J=4J^2+6J.
$$


For a moment matrix, a minus subscript denotes rows $m=0,\ldots,2k-2$, and a plus subscript denotes the next physical rows.

The crucial column-shift identity is


$$
\boxed{
P_{m+j}-P_m=8mj+4j^2+6j.
}
\tag{3.3}
$$



Consequently,


$$
U_+
=P(M)U_-+8MU_-J+U_-B_J
-(2M+I)\mathbf1\mathbf1^T-2\mathbf1\mathbf1^TJ,
\tag{3.4}
$$


and


$$
F_+
=P(M)F_-+8MF_-J+F_-B_J.
\tag{3.5}
$$



Write $W_-=(w_{m+j})$. Since $C=U-W$,


$$
\begin{aligned}
C_+={}&P(M)C_-+8MC_-J+C_-B_J\\
&+(P(M)+I)W_-+8MW_-J+W_-B_J\\
&-(2M+I)\mathbf1\mathbf1^T-2\mathbf1\mathbf1^TJ.
\end{aligned}
\tag{3.6}
$$



For the complete paid right block


$$
\mathcal R(s)_{mj}
=\Lambda_k(r_{m+j}+s w_{m+j}),
$$


one obtains


$$
\boxed{
\mathcal R(s)_++\mathcal R(s)_-
=
-\Lambda_k\bigl((P(M)+I)F_-+8MF_-J+F_-B_J\bigr)
+4\Lambda_k\mathcal D,
}
\tag{3.7}
$$


where


$$
\mathcal D_{mj}=\frac1{2m+2j+1}.
\tag{3.8}
$$



The period cancels in (3.7), but the complete arctangent forcing does not.

All terms involving $J$ and $J^2$ are retained. A relation annihilating the original columns need not annihilate their $J$- or $J^2$-weighted versions. This is precisely why applying a common row recurrence does not automatically produce an integral recurrence for interpolation cofactors.

Every successor in (3.4)–(3.7) is at most moment $3k-2$. No extra terminal row is introduced.

---

## 4. An evaluated matrix certificate for the complete right forcing

Define the complete returns


$$
\sigma_n=c_{n+1}+c_n
=u_{n+1}+u_n,
$$




$$
\boxed{
\tau_n=r_{n+1}+r_n
=-(2n+2)!-(2n)!+\frac4{2n+1}.
}
\tag{4.1}
$$



On $0\le m<2k-1$, $0\le j<k$, set


$$
T_{mj}=\Lambda_k\tau_{m+j},
$$




$$
V_{mj}=\Lambda_k\bigl((2m+2j+2)!+(2m+2j)!\bigr).
$$


Then the complete identity is


$$
\boxed{T+V=4\Lambda_k\mathcal D.}
\tag{4.2}
$$



### 4.1 Clearers and contents in this identity

The actual denominator of $\tau_n$ is $2n+1$: adding its integer factorial part cannot cancel an odd divisor of the numerator $4$.

The full return array includes every index $0\le n\le3k-3$. Its actual least simultaneous clearer is therefore $\Lambda_k$. The cleared array $T$ has actual entry content $1$:

* its entry at $n=0$ is $\Lambda_k\tau_0=\Lambda_k$;
* for every odd prime power $p^a$ occurring maximally in $\Lambda_k$, the entry with $2n+1=p^a$ is a unit modulo $p$ after the remaining $p$-power is removed.

For the first $k$ rows, put


$$
L_k^{\mathrm{force}}
=\operatorname{lcm}(1,3,\ldots,4k-3).
$$


The actual least clearer of the raw forcing array $4\mathcal D_0$ is $L_k^{\mathrm{force}}$, and its content after multiplication by the already paid $\Lambda_k$ is exactly


$$
\frac{4\Lambda_k}{L_k^{\mathrm{force}}}.
\tag{4.3}
$$


No division by this content is made below.

### 4.2 The determinant evaluation

Let $T_0,V_0,\mathcal D_0$ be the first $k$ rows. The Cauchy determinant identity gives


$$
\det\mathcal D_0
=
\frac{
\prod_{0\le i<l<k}2(l-i)
\prod_{0\le j<t<k}2(t-j)
}{
\prod_{i,j=0}^{k-1}(2i+2j+1)
}.
$$


Since


$$
\prod_{0\le i<l<k}(l-i)=\prod_{r=1}^{k-1}r!,
$$


this is


$$
\det\mathcal D_0
=
\frac{
2^{k(k-1)}\prod_{r=1}^{k-1}(r!)^2
}{
\prod_{i,j=0}^{k-1}(2i+2j+1)
}.
\tag{4.4}
$$



Therefore


$$
\det(T_0+V_0)=\Theta_k
$$


with $\Theta_k$ as in (1.4).

This determinant is a nonzero integer because $T_0+V_0$ is an integer matrix. Its prime divisors can only come from the displayed numerator, and hence are at most $6k-5$.

More explicitly,


$$
\begin{aligned}
v_p(\Theta_k)
={}&k\,v_p(4\Lambda_k)
+k(k-1)v_p(2)
+2\sum_{r=1}^{k-1}v_p(r!)\\
&-\sum_{i,j=0}^{k-1}v_p(2i+2j+1).
\end{aligned}
\tag{4.5}
$$



Thus this is an evaluated prime-power certificate, not an unnamed correction term.

### 4.3 Determinantal consequences

Expanding $\det(T_0+V_0)$ by columns expresses $\Theta_k$ as an integer combination of $k$-minors of the horizontal matrix $[T_0\mid V_0]$. Expanding by rows gives the analogous statement for the vertical matrix.

Hence


$$
\boxed{
\delta_k([T_0\mid V_0])\mid\Theta_k,
\qquad
\delta_k\begin{pmatrix}T_0\\V_0\end{pmatrix}\mid\Theta_k.
}
\tag{4.6}
$$



In particular, for every $p>6k-4$,


$$
\ker T_0\cap\ker V_0=\{0\},
\tag{4.7}
$$


and the corresponding common left kernel is also zero.

Finally, Hadamard's inequality gives


$$
\Theta_k\le (4\Lambda_k\sqrt{k})^k.
$$


The elementary bound $\log\operatorname{lcm}(1,\ldots,N)=O(N)$ therefore yields


$$
\boxed{\log\Theta_k=O(k^2).}
\tag{4.8}
$$



This is a genuinely small forcing certificate relative to the leading $4k^2\log k$ raw scale. The unresolved issue is whether it can be transferred to the actual mixed minors without introducing uncontrolled interpolation cofactors.

---

## 5. Large-prime transversality of the finite positive contact array

The next theorem is independent of the completed five-consecutive scalar gcd calculation.

### Theorem 5.1

For every $k\ge2$ and every prime $p>k$,


$$
\operatorname{rank}_{\mathbf F_p}U_k=k.
$$



### Proof

Work over a field $K$ of characteristic zero, or of characteristic $p>k$.

Introduce the formal series


$$
\mathcal U(z)=\sum_{n\ge0}u_nz^n.
$$


From


$$
u_{n+1}=(4n^2+6n+2)u_n-(2n+1)
$$


one obtains


$$
\mathcal L\mathcal U=\frac{1-3z}{(1-z)^2},
\tag{5.1}
$$


where


$$
\boxed{
\mathcal L
=1-2z-10z^2\frac{d}{dz}-4z^3\frac{d^2}{dz^2}.
}
\tag{5.2}
$$



Indeed,


$$
\frac{\mathcal U-1}{z}
=(4\theta^2+6\theta+2)\mathcal U
-\frac{1+z}{(1-z)^2},
\qquad \theta=z\frac{d}{dz},
$$


which rearranges to (5.1).

Suppose a nonzero column relation exists:


$$
\sum_{j=0}^{r}x_ju_{m+j}=0
\qquad(0\le m<2k),
\tag{5.3}
$$


where $r\le k-1$ and $x_r\ne0$.

Define the reversed polynomial


$$
B(z)=\sum_{j=0}^{r}x_jz^{r-j}.
$$


Then $B(0)=x_r\ne0$. Equation (5.3) says that


$$
B(z)\mathcal U(z)-A(z)=O(z^{2k+r})
\tag{5.4}
$$


for a polynomial $A$ with $\deg A<r$. Thus, with $R=A/B$,


$$
\mathcal U-R=O(z^{2k+r}).
$$



Because every derivative in $\mathcal L$ is multiplied by enough powers of $z$,


$$
\mathcal L(\mathcal U-R)=O(z^{2k+r}).
\tag{5.5}
$$



Now put


$$
N_B(z)=B(z)^3\mathcal L(A/B).
$$


Direct differentiation gives


$$
\begin{aligned}
N_B={}&(1-2z)AB^2
-10z^2(A'B-AB')B\\
&-4z^3\bigl(A''B^2-AB''B-2A'B'B+2A(B')^2\bigr).
\end{aligned}
\tag{5.6}
$$



For $r\ge1$,


$$
\boxed{\deg N_B\le3r-1.}
\tag{5.7}
$$


The possible degree-$3r$ term cancels. When $\deg A=r-1$, its scalar coefficient is


$$
-2-10(-1)-4(-1)(-2)=0.
$$


When $\deg A\le r-2$, the degree bound is immediate.

It follows that


$$
Q(z):=(1-z)^2N_B(z)-(1-3z)B(z)^3
$$


has degree at most $3r+1$. On the other hand, (5.1) and (5.5) imply


$$
Q(z)=O(z^{2k+r}).
$$


But


$$
2k+r-(3r+1)=2(k-r)-1\ge1.
$$


Hence $Q$ is the zero polynomial. The case $r=0$ gives the same conclusion directly.

We have therefore produced a rational function $R$ satisfying


$$
\mathcal LR=\frac{1-3z}{(1-z)^2}.
\tag{5.8}
$$



This is impossible in the stated characteristic.

If $R$ has no pole at $z=1$, then $\mathcal LR$ is regular there, whereas the right side has a nonzero double pole.

If $R$ has a pole of order $m\ge1$ at $1$, then $m\le r\le k-1$. The leading pole contributed by $-4z^3R''$ has order $m+2$ and nonzero coefficient proportional to


$$
4m(m+1).
$$


It cannot vanish because $p>k$, or because the characteristic is zero. The other terms have smaller pole order. Thus $\mathcal LR$ has a pole of order at least $3$, again contradicting (5.8).

This contradiction proves the theorem. ∎

### 5.1 Finite-boundary audit

The largest coefficient used in (5.4) is


$$
u_{2k+r-1}\le u_{3k-2}.
$$


To obtain the vanishing coefficients of $Q$, equation (5.1) is needed only through that same finite order.

The formal-series notation does not append a row to the original matrix or use $u_{3k-1}$. The largest factorial degree remains $6k-4$.

---

## 6. Consequences for the complete contact matrix

Let


$$
w=(( -1)^m)_{m<2k},\qquad v=(( -1)^j)_{j<k}.
$$


The complete identity is


$$
U_k=C_k+w v^T.
\tag{6.1}
$$



### Corollary 6.1

For $p>k$,


$$
\operatorname{rank}
\begin{pmatrix}C_k\\v^T\end{pmatrix}=k,
\qquad
\operatorname{rank}C_k\ge k-1.
$$



#### Proof

If $C_kx=0$ and $v^Tx=0$, then (6.1) gives $U_kx=0$. Theorem 5.1 forces $x=0$.

Appending one row increases rank by at most one, proving the second assertion. ∎

If $C_k$ has rank $k-1$ modulo such a prime, its one-dimensional kernel is transverse to the atom evaluation:


$$
x\in\ker C_k,\ x\ne0
\quad\Longrightarrow\quad
v^Tx\ne0.
\tag{6.2}
$$


Also,


$$
w\notin\operatorname{im}C_k.
\tag{6.3}
$$


Otherwise $U_k=C_k(I+yv^T)$ for some $y$, contradicting its rank $k$.

### 6.1 Determinantal-divisor consequences

The rank statements imply


$$
\operatorname{rad}\bigl(\delta_k(U_k)\bigr)
\mid\operatorname{rad}(k!),
\tag{6.4}
$$




$$
\operatorname{rad}\left(
\delta_k\begin{pmatrix}C_k\\v^T\end{pmatrix}
\right)
\mid\operatorname{rad}(k!),
\tag{6.5}
$$


and (1.3).

These support assertions are for the stated rectangular contact objects, not for $G_k$.

Combining (1.3) with the previously proved contact-minor divisor gives


$$
2^{(k-1)(k-2)}
\prod_{r=0}^{k-3}(r!)^2
\mid\delta_{k-1}(C_k),
\tag{6.6}
$$


while every prime divisor of this determinantal divisor is at most $k$.

At a prime $p>k$, all but possibly the last contact Smith invariant are units. Thus the complete contact defect has been reduced to one possible $p$-adic invariant. Nothing here bounds the valuation of that last invariant.

This is the precise improvement over scalar five-consecutive primitivity: it is a rank statement about the original finite contact matrix, not merely about individual columns.

---

## 7. Two original rectangles and an all-prime depth theorem

This section proves (1.7) without using an unpaid Schur division or a conjectural support assertion.

### 7.1 Isolating the period by unimodular operations

In the original right block, leave column $0$ unchanged and replace each column $j\ge1$ by the sum of the old columns $j$ and $j-1$. This is a simultaneous unit-triangular column transformation. The new right columns are


$$
\Lambda_k(r_m+s w_m),\qquad
\Lambda_k\tau_{m+j-1}\quad(1\le j<k).
$$



Move the first right column to the front. Then apply the unit lower-bidiagonal row transformation


$$
\text{new row }0=\text{old row }0,
\qquad
\text{new row }r=\text{old row }r+\text{old row }r-1.
$$


The period vector becomes $e_0$.

Up to the explicit column-permutation sign, the determinant is now


$$
F_k(s)=
\det
\begin{pmatrix}
\Lambda_k(s-1)&b\\
d&B
\end{pmatrix}.
\tag{7.1}
$$


Here $B$ has size $N=2k-1$, and all entries are integers.

In this ordering,


$$
d_m=\Lambda_k\tau_m\qquad(0\le m<N),
$$


the contact part of $B$ is


$$
\sigma_{m+j},
$$


and its other columns are


$$
\Lambda_k(\tau_{m+j}+\tau_{m+j-1})
\qquad(1\le j<k).
$$


Thus the complete correction $4/(2n+1)$ remains in every return.

Let


$$
D=\det B,\qquad
L=b\,\operatorname{adj}(B)d.
$$


Then


$$
F_k(s)=\Lambda_k(s-1)D-L.
\tag{7.2}
$$


Consequently,


$$
\boxed{G_k=\gcd(|\Lambda_kD|,|L|).}
\tag{7.3}
$$



The coefficient content is unchanged by the preceding operations.

Deleting the period column from (7.1) gives a unimodular row transform of $Z_k$. Deleting the period row gives, after the inverse right-column transformation, $Y_k$. Therefore


$$
\mathscr R_k
=\gcd\bigl(|D|,\{\text{entries of }b\operatorname{adj}(B)\}\bigr),
\tag{7.4}
$$




$$
\mathscr L_k
=\gcd\bigl(|D|,\{\text{entries of }\operatorname{adj}(B)d\}\bigr).
\tag{7.5}
$$



All moments in these rectangles are original:


$$
\max c\text{-index}=3k-2,
\qquad
\max \sigma,\tau\text{-index}=3k-3.
$$


Their returns therefore stop at the same moment $3k-2$.

### 7.2 A bordered-content lemma

Let $B$ be an integral $N\times N$ matrix with nonzero determinant $D$, and let $b,d$ be integral borders. Put


$$
g=\gcd(|D|,|b\operatorname{adj}(B)d|),
$$




$$
R=\gcd(|D|,\text{entries of }b\operatorname{adj}(B)),
$$




$$
C=\gcd(|D|,\text{entries of }\operatorname{adj}(B)d).
$$


Then


$$
\boxed{\operatorname{lcm}(R,C)\mid g\mid RC.}
\tag{7.6}
$$



#### Proof

The lower divisibility is immediate: both $R$ and $C$ divide $D$ and the scalar $b\operatorname{adj}(B)d$.

For the upper divisibility, fix a prime $p$. Use Smith form over $\mathbf Z_p$, absorbing units into the borders, so that the diagonal entries of $B$ are $p^{s_i}$. Put


$$
S=\sum_i s_i,\qquad b_i^\ast=v_p(b_i),\qquad d_i^\ast=v_p(d_i).
$$


Then


$$
r:=v_p(R)=\min\left(S,\min_i(S-s_i+b_i^\ast)\right),
$$




$$
c:=v_p(C)=\min\left(S,\min_i(S-s_i+d_i^\ast)\right).
$$



If $r+c\ge S$, then $v_p(g)\le S\le r+c$.

Suppose $r+c<S$. Choose indices attaining $r,c$. They must be the same index $i$: if they were distinct,


$$
r+c\ge 2S-s_i-s_j\ge S.
$$


The $i$-th summand in


$$
b\operatorname{adj}(B)d
=\sum_l b_ld_l\,p^{S-s_l}
$$


has valuation


$$
S-s_i+b_i^\ast+d_i^\ast
=r+c-(S-s_i).
$$


This is less than $s_i$. Every other summand has valuation at least


$$
S-s_l\ge s_i.
$$


Hence no cancellation is possible at the least valuation, and


$$
v_p(g)=r+c-(S-s_i)\le r+c.
$$


This proves $g\mid RC$. ∎

### 7.3 Application to the actual content

For integers $D,L,\Lambda$,


$$
\frac{\gcd(\Lambda D,L)}{\gcd(D,L)}\mid\Lambda.
$$


Applying this and (7.6) to (7.3)–(7.5) proves


$$
\operatorname{lcm}(\mathscr R_k,\mathscr L_k)
\mid G_k
\mid\Lambda_k\mathscr R_k\mathscr L_k.
$$



The hypothesis $D\ne0$ is equivalent here to $H_{1,k}\ne0$, and is validated on the established nonvanishing domain, in particular for every $k\ge64$ and every original $K_u$.

### 7.4 Exact large-prime support and a sharper depth formula

For $p>6k-4$, $\Lambda_k$ is a unit. Thus


$$
p\mid G_k
\quad\Longleftrightarrow\quad
p\mid\mathscr R_k\mathscr L_k.
\tag{7.7}
$$



Equivalently,


$$
\boxed{
p\nmid G_k
\iff
\operatorname{rank}_{\mathbf F_p}Z_k=2k-1
\ \text{and}\
\operatorname{rank}_{\mathbf F_p}Y_k=2k-1.
}
\tag{7.8}
$$



If additionally


$$
\operatorname{rank}_{\mathbf F_p}B\ge N-1,
$$


so at most one Smith invariant of $B$ is nonunit, the proof gives the exact formula


$$
\boxed{
v_p(G_k)=
\min\left(
v_p(D),
v_p(\mathscr R_k)+v_p(\mathscr L_k)
\right).
}
\tag{7.9}
$$



These are genuine depth statements. They do not assert that either rectangular content is a unit.

### 7.5 Interaction with the paid contact divisor

Put


$$
d_h^{\mathrm{cont}}
=2^{h(h-1)}\prod_{r=0}^{h-2}(r!)^2.
$$


Laplace expansion along contact columns gives


$$
d_k^{\mathrm{cont}}\mid\mathscr R_k,
\qquad
d_{k-1}^{\mathrm{cont}}\mid\mathscr L_k.
\tag{7.10}
$$



For $Y_k$, every maximal minor contains at least $k-1$ contact columns; its contact block is an integral row transform of a submatrix of $C_k$. This validates the use of the established contact-minor theorem.

Thus (7.8) is a statement about large-prime residual saturation, not about globally primitive columns before their forced small-prime contents are paid.

---

## 8. A justified $(k+1)$-dimensional local model of the full pencil

Theorem 5.1 permits a reduction that was previously unavailable without an unproved matrix-primitivity assumption.

Fix $p>6k-4$, and work over $\mathbf Z_p$.

Choose the explicit unimodular $k\times k$ matrix $V$ whose columns are


$$
V_0=e_0,\qquad V_j=e_j-(-1)^j e_0\quad(j\ge1).
$$


Then


$$
v^TV=e_0^T,\qquad \det V=1.
$$



By Theorem 5.1, $U_kV$ is a primitive rank-$k$ matrix over $\mathbf Z_p$. Hence there is


$$
S\in\operatorname{GL}_{2k}(\mathbf Z_p)
$$


such that


$$
SU_kV=\begin{pmatrix}I_k\\0\end{pmatrix}.
\tag{8.1}
$$



Write


$$
Sw=\binom{a}{b},
\qquad
S(r_{m+j})V=\binom{\mathsf A}{\mathsf B},
$$


with $a,b\in\mathbf Z_p^k$, and define


$$
h=1-a_0,\qquad r=e_0^T\mathsf A,\qquad \eta=\det S\in\mathbf Z_p^\times.
$$



Since the atom is retained,


$$
SC_kV=
\begin{pmatrix}
I_k-ae_0^T\\
-be_0^T
\end{pmatrix}.
\tag{8.2}
$$



Now add $s\Lambda_k$ times each contact column to its corresponding right column. This is a determinant-one polynomial column operation:


$$
r+s w+s c=r+s u.
$$


It removes no correction from $r$.

Expanding along the $k-1$ unchanged unit contact columns gives the exact identity


$$
\boxed{
\frac{\eta H_k(s)}{\Lambda_k^k}
=
\det
\begin{pmatrix}
h&r+s e_0^T\\
-b&\mathsf B
\end{pmatrix}.
}
\tag{8.3}
$$



Therefore, with


$$
c=\operatorname{adj}(\mathsf B)b,
$$




$$
\boxed{
\frac{\eta H_{0,k}}{\Lambda_k^k}
=h\det\mathsf B+r c,
\qquad
\frac{\eta H_{1,k}}{\Lambda_k^k}
=c_0.
}
\tag{8.4}
$$



All divisions in (8.3)–(8.4) are by $p$-adic units. This is a local valuation argument, not a new global integer normalization. It assigns no guessed global clearer or content to $S$.

It also gives


$$
\boxed{
v_p(\delta_k(C_k))
=
\min\bigl(v_p(h),v_p(b_0),\ldots,v_p(b_{k-1})\bigr).
}
\tag{8.5}
$$



### 8.1 The exact unresolved cofactor

Modulo $p$, the possibilities are now explicit.

* If $\mathsf B$ is invertible, the two coefficients are nonzero as a pair precisely when
  

$$
\left(
  e_0^T\mathsf B^{-1}b,\ 
  h+r\mathsf B^{-1}b
  \right)\ne(0,0).
  \tag{8.6}
$$



* If $\operatorname{rank}\mathsf B=k-1$, write
  

$$
\operatorname{adj}(\mathsf B)=\gamma x y^T,
  \qquad \gamma\ne0,
$$


  where $x,y$ span the right and left kernels. The coefficient pair is nonzero precisely when
  

$$
y^Tb\ne0
  \quad\text{and}\quad
  (x_0,rx)\ne(0,0).
  \tag{8.7}
$$



* If $\operatorname{rank}\mathsf B\le k-2$, then
  

$$
\det\mathsf B=0,\qquad \operatorname{adj}(\mathsf B)=0,
$$


  and both coefficients vanish modulo $p$.

Thus the unresolved matrix step is not the scalar recurrence. It is the rank of this actual projected right block and the indicated left/right cofactor evaluations.

---

## 9. Why the forcing certificate does not yet prove final primitivity

The determinant $\Theta_k$ proves strong transversality for the pair consisting of the complete return matrix and the factorial-return matrix. But the factorial-return columns are not independent columns of the original pencil.

For example, a right kernel relation in $Z_k$ has the form


$$
C_kx+\Lambda_k(\tau_{m+j})y=0.
\tag{9.1}
$$


Using the complete forcing identity yields


$$
4\Lambda_k\mathcal D\,y
=V y-C_kx.
\tag{9.2}
$$


Neither term on the right is known to vanish separately.

Applying a moment recurrence to (9.1) produces the weighted-column terms in (3.4)–(3.7). It does not imply the same relation for $Jx,J^2x,Jy,J^2y$. Eliminating those terms requires actual interpolation minors. Their denominators cannot be replaced by the small factors $P_n$.

Likewise, a left annihilator of the two blocks of $Y_k$ need not annihilate the factorial-return block. The Cauchy certificate therefore cannot simply be inserted into the original mixed determinant ideal.

This identifies the outstanding certificate problem concretely:

> One must transfer the evaluated forcing-minor certificate into the actual maximal-minor ideals of $Y_k$ and $Z_k$, or prove the equivalent cofactor conditions (8.6)–(8.7), while retaining the weighted commutators and paying every interpolation division.

No such transfer has been proved here.

The new theorem (1.2) also does not finish this step. A rank-$(k-1)$ contact matrix already forces every full $H_k(s)$ determinant to vanish modulo $p$, even though its kernel is transverse to the atom. The period update cannot repair a dependence among the fixed contact columns.

---

## 10. The falsified paid transfer and the complete valuation accounting

The original adjacent Schur identity remains


$$
D_{\mathrm{tr}}^{\,2}F^+
=\mathcal K F-\mathcal T,
\tag{10.1}
$$


where


$$
F=\omega_k t^kH_k,\qquad
F^+=\omega_{k+1}H_{k+1},
\qquad
t=\frac{\Lambda_{k+1}}{\Lambda_k}.
$$


Its actual contents are


$$
\operatorname{cont}(F)=t^kG_k,\qquad
\operatorname{cont}(F^+)=G_{k+1}.
\tag{10.2}
$$



The complete new corner uses


$$
\begin{pmatrix}
\lambda(\tau_{3k-1}+\tau_{3k-2})&\sigma_{3k-1}\\
\lambda(\tau_{3k}+\tau_{3k-1})&\sigma_{3k}
\end{pmatrix},
\qquad \lambda=\Lambda_{k+1}.
$$


Thus the adjacent physical endpoint is moment $3k+1$, factorial $(6k+2)!$, and odd denominator $6k+1$.

With


$$
g_{\mathrm{tr}}
=\gcd(D_{\mathrm{tr}}^2,|\mathcal K|,|\mathcal T|),
$$


the actual primitive transfer is


$$
\chi F^+=\alpha F+\beta,
$$




$$
\alpha=\frac{\mathcal K}{g_{\mathrm{tr}}},
\qquad
\beta=-\frac{\mathcal T}{g_{\mathrm{tr}}},
\qquad
\chi=\frac{D_{\mathrm{tr}}^2}{g_{\mathrm{tr}}},
\tag{10.3}
$$


and


$$
\gcd(|\alpha|,|\beta|,\chi)=1.
$$


The actual forward and inverse simultaneous clearers are $\chi$ and $|\alpha|$, respectively.

### 10.1 What the completed $11\to12$ certificate establishes

The certificate gives


$$
|\alpha_{11}|
=2^{73}3^6 5^4 11^2\,A_{11},
$$




$$
\chi_{11}
=47^2 53^2 59^2 61^2\,C_{11},
$$


where $A_{11}>1$, $C_{11}>1$, and both residual integers are coprime to every prime at most $67$.

The primes at most $68$ are exactly the primes at most $67$. Hence each residual has a prime divisor outside the proposed support of $68!$. This refutes the unrestricted assertion


$$
\operatorname{rad}(|\alpha_k|\chi_k)
\mid\operatorname{rad}((6k+2)!).
$$



This finite conclusion is reused, not recomputed. Neither residual is evidence by itself about the support of $G_k$.

### 10.2 An exact valuation rule retaining $\alpha,\beta,\chi$

There is no legitimate replacement of the paid transfer by a unit transfer at large primes.

Write


$$
F=g(f_0+f_1s),
\qquad
g=t^kG_k,
\qquad
\gcd(f_0,f_1)=1.
$$


For a prime $p$, put


$$
a=v_p(\alpha),\quad b=v_p(\beta),\quad c=v_p(\chi),\quad m=v_p(g).
$$



If $a+m\ne b$, then


$$
\boxed{
c+v_p(G_{k+1})=\min(a+m,b).
}
\tag{10.4}
$$



If $a+m=b$, put


$$
u=\frac{\alpha g}{p^{a+m}},\qquad
v=\frac{\beta}{p^b},
$$


which are $p$-adic units. Then


$$
\boxed{
c+v_p(G_{k+1})
=a+m+
\min\bigl(v_p(f_1),v_p(uf_0+v)\bigr).
}
\tag{10.5}
$$



To prove these formulas, take the content of


$$
\alpha g(f_0+f_1s)+\beta.
$$


When the two indicated depths differ, reducing after the smaller power of $p$ leaves a primitive coefficient pair. At equal depth, the displayed constant-term cancellation is the only additional contribution.

Thus:

* the large-prime contribution of $\alpha$ remains;
* the division by $\chi$ remains;
* $\beta$ and its possible cancellation remain;
* $m$ includes the actual $t^kG_k$, not a forced lower divisor.

These formulas are exact, but do not bound the balanced cancellation in (10.5).

---

## 11. Consequences for the original infinite domain

The original compact index set is


$$
\mathcal O=\{K_u=9^{18+32u}:u\ge0\}.
$$


Put


$$
B_{\mathcal O}=9^{32},
\qquad K_{u+1}=B_{\mathcal O}K_u.
$$



Every theorem above applies to the corresponding original matrices. Their whole errors remain


$$
\boxed{
0<\ell_{K_u}
=\frac{|H_{K_u}(s_0)|}{G_{K_u}}.
}
\tag{11.1}
$$



The new content-depth theorem gives the rigorous bounds


$$
\frac{|H_{K_u}(s_0)|}
{\Lambda_{K_u}\mathscr R_{K_u}\mathscr L_{K_u}}
\le \ell_{K_u}
\le
\frac{|H_{K_u}(s_0)|}
{\operatorname{lcm}(\mathscr R_{K_u},\mathscr L_{K_u})}.
\tag{11.2}
$$


These are inequalities for the actual whole error, not alternative definitions.

### 11.1 A content upper bound would diagnose failure, not prove rationality

If one proved, on the required original domain,


$$
\log\mathscr R_k+\log\mathscr L_k
\le(4-\eta)k^2\log k+O(k^2)
\qquad(\eta>0),
\tag{11.3}
$$


then (1.7), $\log\Lambda_k=O(k)$, and the raw leading-$4$ estimate would force


$$
\ell_k\longrightarrow\infty
$$


there.

That would prove failure of primitive decay for this family. It would not prove that $e+\pi$ is rational.

No bound such as (11.3) has been established.

### 11.2 The original-index irrationality condition is unchanged

Because all original indices are odd, the exact positive original-endpoint cross difference is


$$
\Delta_u^{\mathcal O}
=
\frac{
H_{0,K_u}H_{1,K_{u+1}}
-H_{0,K_{u+1}}H_{1,K_u}
}{
G_{K_u}G_{K_{u+1}}
}.
\tag{11.4}
$$



Both final all-prime gcds remain present.

The closed analytic contraction and the original-endpoint minimum-denominator selector give


$$
0<\ell_{i_{\mathcal O}(u)}
\le
\sqrt{\frac{42\Delta_u^{\mathcal O}}{A^{K_u-1}}},
\qquad
i_{\mathcal O}(u)\in\{K_u,K_{u+1}\},
\tag{11.5}
$$


where the endpoint with smaller actual denominator is chosen.

Therefore the condition


$$
\boxed{
\Delta_u^{\mathcal O}=o(A^{K_u-1})
}
\tag{11.6}
$$


on a specified infinite set of $u$ would prove irrationality, using nonzero whole errors at original indices only.

No estimate in this report proves (11.6).

---

## 12. The separate binary producer is not altered

The compact local reductions do not identify its denominator with the denominator of the separate binary producer.

That construction remains on


$$
b=9^{18+32u},\qquad n=4002b,
$$


with contact indices $0,\ldots,b-1$, physical reconstruction indices $0,\ldots,b$, and terminal condition


$$
z_b=0.
$$



Its complete corrected columns remain


$$
x=\frac12RA^{-1}f,
\qquad
y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},
\qquad
x=2^ax_0.
\tag{12.1}
$$


The terms $h^F,e_0$, and the division by $4b!$ are retained.

The complete return remains


$$
S=\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f,
$$


and the paid valuation remains only


$$
v_2\!\left(\frac{S}{2^{a+1}}\right)\ge\chi-a,
\qquad
\chi=v_2\binom{n+b-1}{b-1}.
\tag{12.2}
$$



Its norm $Q=x_0^Tx_0$, corrected-column contents, least simultaneous clearer, and final all-prime scalar gcd remain unevaluated here. Its valuation


$$
v_3(q^{\mathrm{bin}})=n-\frac{b+15}{2}
$$


is not transferred to $q_k$.

---

## 13. One bounded auxiliary calculation for the new obstruction

No computation is needed to complete the proofs in Sections 3–8. No completed $11\to12$, $32$, or $33$ calculation is proposed again.

A small new check can examine the two rectangular contents, rather than the already falsified transfer-support conjecture.

### 13.1 Bounded inputs

Use the auxiliary size $k=5$, not an original index.

Generate only


$$
a_0,\ldots,a_{26},
\qquad
\rho_0,\ldots,\rho_{13},
$$


and hence moments through $13$. Use


$$
\Lambda_5=\operatorname{lcm}(1,3,\ldots,25).
$$



Construct:

* $U_5,C_5$, each $10\times5$;
* $Z_5$, of size $10\times9$;
* $Y_5$, of size $9\times10$;
* the $9\times9$ block $B$ in (7.1), with its complete borders.

The physical limits are exactly moment $13$, factorial $26!$, and odd denominator $25$.

### 13.2 Expected verifiable outputs

1. The ten signed maximal minors of $Z_5$, and the ten signed maximal minors of $Y_5$, computed by exact arithmetic.

2. Their actual all-prime gcds
   

$$
\mathscr R_5,\qquad\mathscr L_5,
$$


   with Bézout certificates.

3. Exact $H_{0,5},H_{1,5},G_5$, with a coefficient-gcd Bézout certificate.

4. A check of $D\ne0$. If it fails, report that fact and omit conclusions requiring the nonzero-$D$ hypothesis; no Schur inversion is needed.

5. Exact zero residuals for
   

$$
F_5(s)-\Lambda_5(s-1)D+b\operatorname{adj}(B)d,
$$


   and exact divisibility checks for
   

$$
\operatorname{lcm}(\mathscr R_5,\mathscr L_5)\mid G_5,
   \qquad
   G_5\mid\Lambda_5\mathscr R_5\mathscr L_5.
$$



6. Smith certificates for $U_5$ and $C_5$, sufficient to verify the new support statements for $\delta_5(U_5)$ and $\delta_4(C_5)$.

7. The residuals of $\mathscr R_5,\mathscr L_5,G_5$ after stripping every prime at most $26$:
   

$$
2,3,5,7,11,13,17,19,23.
$$


   No unrestricted factorization is required.

The expected output is an exact certificate, not a presupposed pass of a support conjecture. A nonunit residual would establish only an auxiliary finite obstruction. Unit residuals would establish only this finite support check.

---

## 14. Final assessment

### What is now proved

For the original finite compact matrices:

* the positive contact array has full column rank modulo every prime $p>k$;
* the complete contact matrix has rank at least $k-1$, with a precisely transverse atom evaluation;
* the complete right forcing has the evaluated, paid small-prime determinant certificate $\Theta_k$;
* the actual final content satisfies
  

$$
\boxed{
  \operatorname{lcm}(\mathscr R_k,\mathscr L_k)
  \mid G_k
  \mid\Lambda_k\mathscr R_k\mathscr L_k;
  }
$$


* at large primes, final-content support is exactly the failure of full rank in one of the two specified original rectangles;
* a validated local reduction identifies the remaining $(k+1)$-dimensional rank/cofactor obstruction.

These statements are rigorous. The optional finite calculation is not part of their proof.

### What is not proved

The small-prime forcing certificate has not been transferred to the maximal-minor ideals of $Y_k$ and $Z_k$. The weighted column commutators prevent the direct scalar-inheritance argument. Their elimination still incurs actual interpolation cofactors.

Neither the last possible large-prime contact invariant nor the residual two-border contents have a sufficient valuation-depth bound. In particular, no leading-$<4$ upper bound for $G_k$, no useful original-domain primitive-denominator bound, and no bound of the form (11.6) has been established.

### Exact remaining bottleneck

The concrete matrix obligation is to control, in the original objects, either



$$
\mathscr R_k=\delta_{2k-1}(Z_k),
\qquad
\mathscr L_k=\delta_{2k-1}(Y_k),
$$


including all prime-power depths, or the equivalent local rank and cofactor conditions (8.6)–(8.7).

For an irrationality proof, that control must ultimately yield


$$
0<
\frac{|H_{K_u}(e+\pi)|}{G_{K_u}}
\longrightarrow0
$$


on an infinite set of the same original indices, or establish the paid original-endpoint cross-difference condition (11.6).

The new results narrow and partially evaluate the all-prime matrix obstruction. They do not remove it. **No unconditional proof of rationality or irrationality of $e+\pi$ follows from the attached work or from this report.**
