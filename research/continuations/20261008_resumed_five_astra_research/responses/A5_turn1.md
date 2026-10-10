> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A paid divided-difference content lemma and the obstruction to a Schur recurrence

## 1. Result and proof status

The rationality or irrationality of


$$
s_0=e+\pi
$$


remains unresolved.

The requested decisive arithmetic bridge has not been established. In particular, this report proves neither a content upper bound with leading coefficient strictly below $4$, nor sufficiently small actual primitive denominators or adjacent cross differences.

It does, however, establish a new arithmetic statement for the **same complete compact pencil**:

> **New content-divisor theorem.** Put
> 

$$
> D_{k-1}^{\mathrm{Lag}}=\prod_{r=0}^{k-2}(r!)^2,
> \qquad
> E_k=\frac{\Lambda_k^k}{\prod_{j=0}^{k-1}\Lambda_{k,j}}.
>
$$


> For every $k\ge2$, both coefficients of the original polynomial $H_k(s)$ are divisible by
> 

$$
> \boxed{2^{k(k-1)}D_{k-1}^{\mathrm{Lag}}E_k.}
> \tag{1.1}
>
$$


> Consequently, on the established nonvanishing domain $k\ge32$,
> 

$$
> \boxed{2^{k(k-1)}D_{k-1}^{\mathrm{Lag}}E_k\mid G_k.}
> \tag{1.2}
>
$$



This is a product divisibility, including the shared powers of $2$. It is not obtained by improperly multiplying previously separate divisibilities.

The proof gives additional evaluated arithmetic information:

* exact coefficient contents of the transformed contact columns;
* exact least clearers and content $1$ for the factorial-normalized complete contact columns;
* a five-consecutive-term, all-prime transversality statement for their integral numerators;
* a corresponding determinantal-divisor bound for the original finite contact matrix.

These results improve the established absolute ceilings for the actual $q_k$ and $\Delta_k$ by explicit factors. They do **not** change the leading $k^2\log k$ scale.

The recurrence investigation also produces a precise negative conclusion about a proposed method:

> The complete contact and right moments do not satisfy the homogeneous unimodular Bessel recurrence satisfied by the factorial-normalized positive contact part. The missing terms are explicitly nonzero: they include the contact atom, a factorial endpoint forcing, and the complete beta-integral form of the arctangent correction.

Moreover, index shifts introduce nonzero column-weighted commutators. Thus a regular moment-state transfer does not automatically induce a regular transfer for the paid Schur numerators.

No finite calculation has been executed for this report. The completed $k=32$ and $k=33$ certificates are reused only at their stated finite scope.

---

## 2. Exact objects and established inputs

### 2.1 Original compact pencil

Throughout the compact construction,


$$
k\ge2,\qquad 0\le m<2k,\qquad 0\le j<k.
$$



The complete moments are


$$
a_0=1,\qquad a_d=1-da_{d-1},
$$




$$
c_n=a_{2n}-(-1)^n,
$$




$$
\rho_0=0,\qquad \rho_{n+1}+\rho_n=\frac1{2n+1},
$$




$$
r_n=-(2n)!+4\rho_n.
$$



Set


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5)
$$


and


$$
H_k(s)=
\det\left[
(c_{m+j})\ \middle|\
\bigl(\Lambda_k[r_{m+j}+s(-1)^{m+j}]\bigr)
\right]
=H_{0,k}+H_{1,k}s.
\tag{2.1}
$$



The largest original moment is $r_{3k-2}$, the largest factorial is
$(6k-4)!$, and the last possible odd denominator is $6k-5$.

The actual all-prime normalization is


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|),
$$




$$
q_k=\frac{|H_{1,k}|}{G_k},
\qquad
p_k=-\frac{\operatorname{sgn}(H_{1,k})H_{0,k}}{G_k}.
\tag{2.2}
$$



No proved lower divisor of $G_k$, including the new divisor (1.2), is substituted for $G_k$ in these definitions.

### 2.2 Reused analytic results

The complete A5 turn-0 theorem is used at its accepted scope. For $k\ge32$,


$$
(-1)^kH_k(s_0)>0,\qquad (-1)^kH_{1,k}>0.
$$


Hence


$$
\ell_k:=q_ks_0-p_k=\frac{|H_k(s_0)|}{G_k}>0.
\tag{2.3}
$$



For


$$
\mathfrak a=17+12\sqrt2
$$


and $k\ge64$,


$$
0<\varepsilon_{k+1}\le\frac14\varepsilon_k,
\qquad
\varepsilon_k=s_0-\frac{p_k}{q_k},
\tag{2.4}
$$


and


$$
\frac1{k^2\mathfrak a^{\,k-1}}
\le\varepsilon_k
\le\frac{42}{\mathfrak a^{\,k-1}}.
\tag{2.5}
$$



Their proofs are not repeated. The still-refereed parent correlated Gamma comparison, including its proposed relative asymptotic refinement, is not needed below.

The accepted raw leading scale is


$$
\log |H_k(s_0)|=4k^2\log k+O(k^2).
\tag{2.6}
$$


The older leading-$2$ lower estimate is not used in place of (2.6).

### 2.3 Reused column clearers

For each complete raw right column,


$$
\Lambda_{k,j}
=\operatorname{lcm}(1,3,\ldots,4k+2j-3)
$$


is its actual least clearer. Thus


$$
H_k(s)=E_k\widehat H_k(s),
\qquad
E_k=\frac{\Lambda_k^k}{\prod_{j=0}^{k-1}\Lambda_{k,j}}\in\mathbb Z_{>0},
\tag{2.7}
$$


where $\widehat H_k$ uses $\Lambda_{k,j}$ in right column $j$.

The established prime-power evaluation of $E_k$ remains


$$
v_p(E_k)=
\sum_{\substack{a\ge1\\4k-3<p^a\le6k-5}}
\frac{p^a-4k+3}{2}
\quad(p\ \text{odd}),
\qquad v_2(E_k)=0.
\tag{2.8}
$$



---

## 3. The same paid adjacent pencil

The arithmetic investigation below does not replace the accepted adjacent pencil.

Define


$$
\sigma_n=c_{n+1}+c_n=a_{2n+2}+a_{2n},
$$


and retain the complete identity


$$
\boxed{
\tau_n=r_{n+1}+r_n
=-(2n+2)!-(2n)!+\frac4{2n+1}.
}
\tag{3.1}
$$



The nested array is


$$
\begin{array}{ll}
\mathscr M_{0,T_0}(s)=s-1,
&
\mathscr M_{r,T_0}(s)=\tau_{r-1}\quad(r\ge1),\\[1mm]
\mathscr M_{0,C_j}=c_j,
&
\mathscr M_{r,C_j}=\sigma_{r+j-1}\quad(r\ge1),\\[1mm]
\mathscr M_{0,T_j}=\tau_{j-1}\quad(j\ge1),
&
\mathscr M_{r,T_j}
=\tau_{r+j-1}+\tau_{r+j-2}\quad(r,j\ge1).
\end{array}
\tag{3.2}
$$



Its leading $2k$-square determinant equals


$$
\omega_k\frac{H_k(s)}{\Lambda_k^k},
\qquad
\omega_k=(-1)^{k(k+1)/2}.
$$



For an adjacent pair put


$$
\lambda=\Lambda_{k+1},\qquad t=\frac{\Lambda_{k+1}}{\Lambda_k},
$$


and multiply every $T$-column by $\lambda$. Then


$$
F(s)=\omega_k t^kH_k(s),
\qquad
F^+(s)=\omega_{k+1}H_{k+1}(s).
\tag{3.3}
$$


Their actual coefficient contents are


$$
\operatorname{cont}(F)=t^kG_k,\qquad
\operatorname{cont}(F^+)=G_{k+1}.
\tag{3.4}
$$



Partition the enlarged matrix as


$$
\begin{pmatrix}
\lambda(s-1)&b&\beta\\
d&B_0&U\\
\delta&V&W
\end{pmatrix},
$$


where $B_0$ has size $2k-1$. The new corner is exactly


$$
W=
\begin{pmatrix}
\lambda(\tau_{3k-1}+\tau_{3k-2})&\sigma_{3k-1}\\
\lambda(\tau_{3k}+\tau_{3k-1})&\sigma_{3k}
\end{pmatrix}.
\tag{3.5}
$$



Thus the enlarged physical cutoff is $r_{3k+1}$, with factorial
$(6k+2)!$ and last odd denominator $6k+1$. No successor moment beyond the $k+1$ matrix is used.

Using the established definitions


$$
D=\det B_0,
$$




$$
\mathcal S=DW-V\operatorname{adj}(B_0)U,
$$




$$
\mathcal t=D\beta-b\operatorname{adj}(B_0)U,\qquad
\mathcal z=D\delta-V\operatorname{adj}(B_0)d,
$$




$$
\mathcal K=\det\mathcal S,\qquad
\mathcal T=\mathcal t\,\operatorname{adj}(\mathcal S)\mathcal z,
$$


the paid identity is


$$
\boxed{D^2F^+(s)=\mathcal K F(s)-\mathcal T.}
\tag{3.6}
$$



For $k\ge64$, the actual positive reduced cross difference satisfies


$$
\boxed{
\Delta_k
=\frac{\lambda|\mathcal T|}
{|D|\,t^kG_kG_{k+1}}.
}
\tag{3.7}
$$


Both final gcds remain present.

Only after dividing by the actual $q_{k+1}$ is the cancellation legitimate:


$$
\boxed{
\frac{\Delta_k}{q_{k+1}}
=\frac{|\mathcal T|}{t^kG_k|\mathcal K|}.
}
\tag{3.8}
$$


The accepted contraction gives


$$
\frac{\Delta_k}{q_{k+1}}
<\ell_k
\le\frac43\frac{\Delta_k}{q_{k+1}}.
\tag{3.9}
$$



The arithmetic problem is therefore still a bound on a fully paid quantity, not on an unnormalized Schur numerator.

---

## 4. Evaluated moment transfers: what is regular, and what is not

### 4.1 The original five-state recurrence has bounded prime support

Write


$$
u_n=a_{2n},\qquad f_n=(2n)!,\qquad
P_n=(2n+1)(2n+2).
$$


The original recurrence gives


$$
u_{n+1}=P_nu_n-(2n+1),\qquad
f_{n+1}=P_nf_n.
\tag{4.1}
$$



For the adjacent physical cutoff, use the already paid $\lambda=\Lambda_{k+1}$. The state


$$
X_n=(u_n,f_n,\lambda\rho_n,(-1)^n,1)^T
$$


satisfies


$$
X_{n+1}=
\begin{pmatrix}
P_n&0&0&0&-(2n+1)\\
0&P_n&0&0&0\\
0&0&-1&0&\lambda/(2n+1)\\
0&0&0&-1&0\\
0&0&0&0&1
\end{pmatrix}X_n.
\tag{4.2}
$$



For every transition needed by the $k+1$ matrix,


$$
0\le n\le3k,
$$


the entry $\lambda/(2n+1)$ is integral. The matrix has coefficient content $1$ and determinant


$$
P_n^2.
\tag{4.3}
$$



Its inverse has actual least simultaneous entry clearer $P_n$: an entry $1/P_n$ occurs, and multiplication by $P_n$ clears the whole inverse. The cleared inverse has content $1$.

Thus this moment-state transport is invertible modulo every prime


$$
p>6k+2.
\tag{4.4}
$$



This is a genuine evaluated regularity statement. It does **not** establish that the mixed Hankel pencil, its Schur block, or its coefficient pair is primitive at those primes.

### 4.2 A useful divided-difference normalization

Let $\Delta$ denote forward difference in the moment index, and put


$$
d_n=\Delta^nu_0.
$$



The finite moment identity


$$
u_n=\int_0^\infty (t-1)^{2n}e^{-t}\,dt
\tag{4.5}
$$


follows by integration by parts from
$a_d=1-da_{d-1}$. Hence


$$
d_n=\int_0^\infty [t(t-2)]^n e^{-t}\,dt.
\tag{4.6}
$$



To derive its recurrence, set


$$
I_n=\int_{-1}^{\infty}(z^2-1)^ne^{-z}\,dz,
\qquad d_n=e^{-1}I_n.
$$


For $n\ge1$, integration by parts has zero lower boundary term, and gives


$$
I_{n+1}
=2(n+1)(2n+1)I_n+4n(n+1)I_{n-1}.
$$


Therefore


$$
d_{n+1}
=2(n+1)(2n+1)d_n+4n(n+1)d_{n-1}.
\tag{4.7}
$$



Since $d_0=1$ and $d_1=0$, it follows that


$$
\boxed{d_n=2^n n!\,g_n,}
\tag{4.8}
$$


where


$$
g_0=1,\qquad g_1=0,\qquad
g_{n+1}=(2n+1)g_n+g_{n-1}.
\tag{4.9}
$$



In particular $g_n\in\mathbb Z$, and its two-state transfer has determinant $-1$:


$$
\binom{g_{n+1}}{g_n}
=
\begin{pmatrix}2n+1&1\\1&0\end{pmatrix}
\binom{g_n}{g_{n-1}}.
\tag{4.10}
$$



This is the classical Bessel-polynomial recurrence in a convenient normalization; the arithmetic application below is derived directly rather than imported from a determinant formula.

### 4.3 The contact atom changes the complete recurrence

The complete contact moment is not $u_n$. Since


$$
\Delta^n((-1)^m)\big|_{m=0}=(-2)^n,
$$


we obtain


$$
\boxed{
\Delta^nc_0
=2^n\bigl(n!g_n-(-1)^n\bigr).
}
\tag{4.11}
$$



Define


$$
b_n=n!g_n-(-1)^n.
\tag{4.12}
$$


Then


$$
b_0=0,\qquad b_1=1,
$$


and direct substitution in (4.9) yields


$$
\boxed{
b_{n+1}
=(n+1)(2n+1)b_n+n(n+1)b_{n-1}
+\bigl((n+1)^2+1\bigr)(-1)^n.
}
\tag{4.13}
$$



Thus the complete sequence is forced. In particular, if


$$
\mathcal B_n y
=y_{n+1}-2(n+1)(2n+1)y_n-4n(n+1)y_{n-1},
$$


then


$$
\boxed{
\mathcal B_n(\Delta^\bullet c_0)
=2\bigl((n+1)^2+1\bigr)(-2)^n\ne0.
}
\tag{4.14}
$$



The failed equality in a homogeneous-recurrence argument is exactly the assertion that the left side of (4.14) vanishes.

The atom has not disappeared. Under $x\mapsto x-1$, its location $-1$ becomes $-2$, producing precisely the term $-(-2)^n$ in (4.11).

### 4.4 The complete right forcing is also explicit

Put


$$
F_n=\Delta^n f_0
=\int_0^\infty(t^2-1)^ne^{-t}\,dt,
\qquad
V_n=\Delta^n\rho_0.
$$


Unlike (4.7), the lower endpoint $t=0$ now contributes:


$$
\boxed{\mathcal B_nF=(-1)^{n+1}.}
\tag{4.15}
$$



The arctangent recurrence gives


$$
V_{n+1}+2V_n=\beta_n,
\tag{4.16}
$$


where the forcing is evaluated:


$$
\begin{aligned}
\beta_n
&=\sum_{j=0}^n(-1)^{n-j}\binom nj\frac1{2j+1}\\
&=\int_0^1(t^2-1)^n\,dt\\
&=\boxed{
(-1)^n\frac{2^{2n}(n!)^2}{(2n+1)!}
}.
\end{aligned}
\tag{4.17}
$$



This is not a named unevaluated correction. Its actual denominator is the odd part of


$$
(2n+1)\binom{2n}{n}.
\tag{4.18}
$$


The finite sum in (4.17) also proves that this denominator divides
$\operatorname{lcm}(1,3,\ldots,2n+1)$. Thus the existing $\lambda$ pays it throughout the adjacent physical domain.

For the complete right moment after finite differences,


$$
R_n(s):=\Delta^n\bigl(r_0+s(-1)^0\bigr)
=-F_n+4V_n+s(-2)^n,
\tag{4.19}
$$


one obtains


$$
\boxed{
\mathcal B_nR
=(-1)^n
-2\bigl((n+1)^2+1\bigr)(R_n+F_n)
+4(2n^2+3n+2)\beta_n.
}
\tag{4.20}
$$



Equations (4.14) and (4.20) exhibit all three obstructions to the proposed homogeneous two-state transfer:

1. the contact atom;
2. the factorial endpoint forcing;
3. the full arctangent forcing.

None can be deleted when passing to the original determinant.

### 4.5 Boundary audit

For a $k$-matrix, the divided differences used below have


$$
n\le3k-2.
$$


Recurrence (4.7) is used only when its successor remains within that range. Its largest polynomial degree is $2(3k-2)=6k-4$.

For the adjacent $k+1$ matrix, the corresponding limits are


$$
n\le3k+1,\qquad 2n\le6k+2.
$$


Equation (4.16) uses $\beta_n$ only when $V_{n+1}$ is physically present. No additional original row or successor moment is introduced.

---

## 5. New scalar transversality and exact column payments

The forced recurrence (4.13), although unsuitable as a homogeneous transfer, has a useful arithmetic consequence.

### Lemma 5.1 — Five consecutive complete numerators are primitive

For every $n\ge0$,


$$
\boxed{\gcd(b_n,b_{n+1},b_{n+2},b_{n+3},b_{n+4})=1.}
\tag{5.1}
$$



#### Proof

A common divisor of these five integers divides, by (4.13),


$$
(n+2)^2+1,\qquad (n+3)^2+1,\qquad (n+4)^2+1.
$$


For any integer $x$, the gcd of


$$
x^2+1,\quad (x+1)^2+1,\quad (x+2)^2+1
$$


divides the difference of the two consecutive first differences, which is $2$. But at least one of the first two displayed integers is odd. Their threefold gcd is therefore $1$. ∎

This is an all-prime statement, not merely a parity observation.

Also,


$$
\boxed{\gcd(b_n,n!)=1}
\tag{5.2}
$$


because $b_n=n!g_n-(-1)^n$. In particular, $b_n$ is odd for every $n\ge1$.

### 5.1 Unimodular finite differences in the original contact matrix

Let


$$
C=(c_{m+j})_{\substack{0\le m<2k\\0\le j<k}}.
$$


Apply the unit lower-triangular row matrix


$$
U_{mi}=(-1)^{m-i}\binom mi\qquad(i\le m)
$$


and the corresponding unit upper-triangular contact-column matrix. Both have determinant $1$, and both have integral inverses.

The resulting contact matrix is


$$
C'_{mj}=\Delta^{m+j}c_0
=\boxed{2^{m+j}b_{m+j}.}
\tag{5.3}
$$



No factorial division has been performed in this transformation.

### Proposition 5.2 — Actual transformed contact-column contents

For $0\le j<k$, the actual integer content of column $j$ of $C'$ is


$$
\boxed{\kappa_{k,j}=2^{\max(1,j)}.}
\tag{5.4}
$$



#### Proof

For $j\ge1$, the entry at $m=0$ has exact binary valuation $j$, while all later entries have binary valuation $m+j\ge j+1$. For $j=0$, the first entry is $0$, and the entry at $m=1$ is $2$, so the minimum binary valuation is $1$.

No odd prime can divide the whole column. When $k\ge3$, the column contains at least five consecutive $b$-values, and Lemma 5.1 applies. For $k=2$, each allowed interval starts at $j=0$ or $j=1$ and contains $b_1=1$. ∎

Thus the exact scalar extracted by making these transformed contact columns primitive is


$$
\boxed{
C_k^{\mathrm{col}}
=\prod_{j=0}^{k-1}\kappa_{k,j}
=2^{\,1+k(k-1)/2}.
}
\tag{5.5}
$$



### 5.2 Actual right-column contents after their least clearers

Consider a complete right column, as a column with coefficients in $\mathbb Z[s]$, after multiplication by its actual least clearer $\Lambda_{k,j}$.

Its coefficient-column content is exactly $1$. Indeed, its period coefficients have gcd $\Lambda_{k,j}$, while minimality of the clearer implies


$$
\gcd\!\left(\Lambda_{k,j},
\{\Lambda_{k,j}r_{m+j}\}_{m=0}^{2k-1}\right)=1.
\tag{5.6}
$$



The unimodular row transformation preserves this coefficient content and preserves its least raw entry clearer.

Consequently, after the exact extraction $E_k$, followed by the actual contact-column extraction (5.5), one obtains an integer affine pencil with all individual coefficient-columns primitive. Its determinant content is still


$$
\boxed{
\frac{G_k}{E_kC_k^{\mathrm{col}}},
}
\tag{5.7}
$$


not $1$ in general.

Columnwise primitivity is therefore explicitly distinguished from final determinant primitivity.

### 5.3 The precise cost of the tempting factorial normalization

The complete normalized contact moment is


$$
\frac{\Delta^nc_0}{2^n n!}
=g_n-\frac{(-1)^n}{n!}
=\frac{b_n}{n!}.
\tag{5.8}
$$


By (5.2), its actual denominator is $n!$.

For a column with indices


$$
j\le n\le N_j:=2k-1+j,
$$


the actual least simultaneous clearer of (5.8) is therefore


$$
\boxed{N_j!.}
\tag{5.9}
$$


After multiplication by $N_j!$, the column has actual content $1$.

To verify the latter assertion, let a prime divide all cleared entries. If $p\le N_j$, the last entry $b_{N_j}$ excludes it by (5.2). If $p>N_j$, every factorial quotient is a unit modulo $p$, so the prime would divide every $b_n$ in the interval, contrary to Lemma 5.1; the $k=2$ intervals again contain $b_1=1$.

Thus the atom creates an exact factorial denominator, not a removable cosmetic term.

Finally, division by $(m+j)!$ is not a common row or column scaling of the original matrix. Replacing the complete columns by $g_{m+j}$ would both delete the atom and change the producer. No such replacement is made here.

---

## 6. New determinantal-divisor theorem

Let $\delta_h(C)$ denote the gcd of all $h\times h$ minors of the original finite contact matrix $C$. The following statement concerns that actual matrix, not a new moment family.

### Theorem 6.1 — Paid contact-minor divisibility

For every $1\le h\le k$,


$$
\boxed{
2^{h(h-1)}
\prod_{r=0}^{h-2}(r!)^2
\mid \delta_h(C).
}
\tag{6.1}
$$


The product is interpreted as $1$ when $h=1$.

#### Proof

The unimodular row and contact-column transformations preserve every determinantal-divisor ideal. It suffices to prove the assertion for $C'$.

For row indices $I$ and column indices $J$, each of cardinality $h$, factor


$$
2^{\sum_{m\in I}m+\sum_{j\in J}j}
$$


from the corresponding minor of (5.3). Since the indices are distinct nonnegative integers,


$$
\sum_{m\in I}m+\sum_{j\in J}j\ge h(h-1).
\tag{6.2}
$$



The remaining matrix has entries


$$
b_{m+j}=(m+j)!g_{m+j}-(-1)^m(-1)^j.
$$


Write


$$
A_{mj}=(m+j)!g_{m+j}.
$$


Every minor of $A$, on row set $I'$ and column set $J'$, is divisible by


$$
\prod_{m\in I'}m!\prod_{j\in J'}j!,
\tag{6.3}
$$


because


$$
(m+j)!g_{m+j}
=m!j!\binom{m+j}{m}g_{m+j}.
$$



The matrix $b_{m+j}$ is a rank-one perturbation of $A$. Its $h$-minor is the $h$-minor of $A$ plus an integer linear combination of $(h-1)$-minors of $A$. Every such term is divisible by


$$
\left(\prod_{r=0}^{h-2}r!\right)^2,
\tag{6.4}
$$


since any $h-1$ distinct nonnegative row or column indices, in increasing order, dominate $0,\ldots,h-2$.

Combining (6.2) and (6.4) proves the product divisibility. In particular, the factorial divisibility has been proved **after** the binary factor is removed; the powers of $2$ shared by the two factors are fully paid. ∎

### Corollary 6.2 — New divisor of the actual coefficient content

For every $k\ge2$,


$$
2^{k(k-1)}D_{k-1}^{\mathrm{Lag}}E_k
\mid H_{0,k},H_{1,k}.
\tag{6.5}
$$



#### Proof

Start with $\widehat H_k$ in (2.7), whose right columns are integral affine columns. Apply the same unimodular row transformation and contact-column transformation used above.

Expand the determinant along its $k$ contact columns. Every contact minor is divisible by


$$
2^{k(k-1)}D_{k-1}^{\mathrm{Lag}}
$$


by Theorem 6.1. Every complementary right minor has integer coefficients. Hence this factor divides both coefficients of $\widehat H_k$.

Multiplication by the already established exact factor $E_k$ proves (6.5). ∎

This proves (1.1)–(1.2).

---

## 7. Consequences for actual denominators and adjacent cross differences

Let the established evaluated slope ceiling be


$$
U_k=
\Lambda_k^k4^kk!\,28^{k-1}h_{k-1}
\prod_{r=0}^{k-1}(2k+4r)!,
\tag{7.1}
$$


where


$$
h_m=
\frac{
2^{m(m-1)}\prod_{j=1}^{m-1}(j!)^2
}{
\prod_{i,j=0}^{m-1}(2i+2j+1)
}.
\tag{7.2}
$$



Define the completely specified rational ceiling


$$
\mathcal Q_k'=
\frac{U_k}
{2^{k(k-1)}D_{k-1}^{\mathrm{Lag}}E_k}.
\tag{7.3}
$$


The new divisor gives the unconditional bound


$$
\boxed{q_k\le\mathcal Q_k'\qquad(k\ge32).}
\tag{7.4}
$$



Using only the accepted turn-0 analytic theorem,


$$
\boxed{
0<\Delta_k
\le
\frac{42\,\mathcal Q_k'\mathcal Q_{k+1}'}
{\mathfrak a^{\,k-1}}
\qquad(k\ge64).
}
\tag{7.5}
$$



Relative to the previously stated ceiling using only
$D_{k-1}^{\mathrm{Lag}}E_k$, the denominator ceiling improves by
$2^{k(k-1)}$, and the adjacent cross-difference ceiling improves by


$$
2^{k(k-1)+(k+1)k}=2^{2k^2}.
$$



These are evaluated bounds for the actual reduced quantities, not bounds for an unpaid transfer determinant.

They are nevertheless insufficient:


$$
\log \mathcal Q_k'=3k^2\log k+O(k^2).
\tag{7.6}
$$


The new binary factor contributes $O(k^2)$, not a change in the leading coefficient.

If


$$
\Gamma_k'=
\frac{G_k}
{2^{k(k-1)}D_{k-1}^{\mathrm{Lag}}E_k},
$$


then the unresolved arithmetic size is still reflected in


$$
\log q_k
=3k^2\log k-\log\Gamma_k'+O(k^2).
\tag{7.7}
$$


No useful upper or lower asymptotic estimate for this actual residual content has been proved.

---

## 8. Why regular moment transport does not give regular Schur transport

There are two separate failures in the proposed inheritance argument.

### 8.1 Complete forcing prevents the homogeneous reduction

Equations (4.14) and (4.20) already disprove the required homogeneous equalities. The unimodular recurrence (4.10) governs $g_n$, not the complete contact and right columns.

The exact factorial clearers in §5.3 show that this is also an arithmetic failure, not merely an analytic distinction.

### 8.2 Index shifts create a nonzero commutator

Even the original recurrence cannot be applied to all columns using a common scalar row coefficient.

For the contact sequence,


$$
c_{n+1}=P_nc_n+(P_n+1)(-1)^n-(2n+1).
\tag{8.1}
$$


At column shift $j$,


$$
P_{m+j}-P_m=2j(4m+2j+3).
\tag{8.2}
$$



If one tries to use the coefficient $P_m$ uniformly across the row, the omitted defect is


$$
\boxed{
(P_{m+j}-P_m)a_{2(m+j)}-2j.
}
\tag{8.3}
$$


It is not identically zero.

Equivalently, applying the row recurrence to a constant linear combination
$\sum_j x_jc_{m+j}$ produces additional combinations weighted by $j$ and $j^2$. Vanishing of the original combination on the interpolation rows does not imply vanishing of those weighted combinations.

This is the concrete point at which the Schur residuals fail to inherit the scalar moment recurrence. Closing the enlarged system requires additional elimination. Its denominators are minors of the actual finite interpolation matrix; they are not automatically products of the $P_n$.

The physical terminal does not remove this defect. The Schur residuals are evaluated precisely at the two new physical rows, and the weighted-column terms remain there.

---

## 9. Exact payment of the affine Schur recurrence

The Schur identity itself does produce an affine recurrence, but its actual least clearer must be paid.

Assume $D\ne0$ and $\mathcal K\ne0$, as established for $k\ge32$. Define


$$
g_k^{\mathrm{tr}}
=\gcd(D^2,|\mathcal K|,|\mathcal T|),
$$




$$
\alpha_k=\frac{\mathcal K}{g_k^{\mathrm{tr}}},
\qquad
\beta_k=-\frac{\mathcal T}{g_k^{\mathrm{tr}}},
\qquad
\chi_k=\frac{D^2}{g_k^{\mathrm{tr}}}.
\tag{9.1}
$$



Then


$$
\boxed{\chi_kF^+=\alpha_kF+\beta_k,}
\tag{9.2}
$$


and


$$
\gcd(|\alpha_k|,|\beta_k|,\chi_k)=1.
\tag{9.3}
$$



The actual least simultaneous clearer of


$$
\frac{\mathcal K}{D^2},\qquad
\frac{\mathcal T}{D^2}
$$


is exactly $\chi_k$. The cleared transfer matrix


$$
\begin{pmatrix}
\alpha_k&\beta_k\\
0&\chi_k
\end{pmatrix}
\tag{9.4}
$$


has content $1$. Its determinant is $\alpha_k\chi_k$.

Similarly, the inverse affine transfer has actual least simultaneous clearer
$|\alpha_k|$, and its cleared matrix also has content $1$.

Thus the relevant prime support is that of


$$
|\alpha_k|\chi_k,
\tag{9.5}
$$


not merely the prime support of the moment-state determinants $P_n^2$.

There is also the exact all-prime adjacent-content relation


$$
\boxed{
\gcd\!\left(
\chi_kG_{k+1},\,
|\alpha_k|t^kG_k
\right)
=
\gcd\!\left(
|\alpha_k|t^kG_k,\,
|\beta_k|
\right).
}
\tag{9.6}
$$



Indeed, the coefficient lists of $\chi_kF^+$ and $\alpha_kF$ differ only by the constant $\beta_k$.

Equation (9.6) is an invariant relation, not an upper content bound. Without an estimate for the paid $\alpha_k,\beta_k,\chi_k$, it does not control either actual gcd separately.

### A concrete follow-on lemma

The precise small-prime-support assertion needed by the simplest recurrence-inheritance mechanism is:

> **Proposed $S$-unit inheritance lemma.** Whenever the complete adjacent construction has $D\mathcal K\ne0$,
> 

$$
> \operatorname{rad}(|\alpha_k|\chi_k)
> \mid
> \operatorname{rad}((6k+2)!).
> \tag{9.7}
>
$$



This is a falsifiable replacement for the unsupported assertion that regular moment transport automatically makes the Schur transfer regular.

It is **not proved or assumed here**. The forcing and commutator calculations explain why it does not follow from the evaluated moment recurrence. Even if (9.7) were true, valuation-depth control and control of $\beta_k$ would still be necessary for a decisive content theorem.

---

## 10. Completed finite evidence: retained, not repeated

The supplied $k=32$ and $k=33$ calculations are reused as finite arithmetic evidence.

They report:

* $q_{32}$ has $6437$ digits and $q_{33}$ has $6891$ digits;
* $v_2(G_{32})=3375$ and $v_2(G_{33})=3602$;
* the old proposed envelope fails by $2^{547}$ at $32$ and by $2^{592}$ at $33$;
* trial division of each reported $G_k$ by all primes in its denominator range leaves residual $1$;
* the actual positive $\Delta_{32}$ has $13281$ digits;
* $10^{453}<q_{33}/q_{32}<10^{454}$;
* the certified whole-error lower bounds are $10^{4857}$ and $10^{5213}$;
* the finite ordinary-error ratio is less than $1/2$.

The new divisor theorem is compatible with these data. It is not an upper envelope, and it does not repair the refuted envelope by guessing a larger binary constant.

The finite contraction and denominator explosion coexist. That observation reinforces, but does not prove infinitely, the distinction between ordinary-error decay and whole-error decay.

Neither $32$ nor $33$ is an original binary index. Neither lies in the $k\ge64$ analytic theorem. No infinite growth law, large-prime exclusion, or original-index conclusion is inferred from them.

---

## 11. One bounded follow-on calculation, if authorized

No finite computation is needed for the proofs in §§4–7.

A new, bounded calculation can test the specific recurrence-inheritance assertion (9.7), rather than repeat a Smith sweep or the completed $32\to33$ diagnostic.

### 11.1 Inputs

Use the adjacent pair $k=11$, $k+1=12$. This is an auxiliary algebraic test of the proposed all-$k$ inheritance mechanism, not an original-index instance.

Generate only


$$
a_0,\ldots,a_{68},\qquad
\rho_0,\ldots,\rho_{34},
$$


and hence


$$
c_0,\ldots,c_{34},\qquad
r_0,\ldots,r_{34}.
$$



Use


$$
\Lambda_{11}=\operatorname{lcm}(1,3,\ldots,61),
\qquad
\lambda=\Lambda_{12}=\operatorname{lcm}(1,3,\ldots,67),
$$


with the exact jump $t=\lambda/\Lambda_{11}$.

Construct the complete nested $24\times24$ matrix (3.2), including every $4/(2n+1)$ correction. Form its $21\times21$ block $B_0$, and the complete adjacent blocks defining $D,\mathcal K,\mathcal T$.

The physical cutoff is exactly moment $34$, factorial $68!$, and odd denominator $67$.

### 11.2 Expected verifiable outputs

1. Exact $D,\mathcal K,\mathcal T$, with determinant and exact-division certificates.
2. A check of $D\mathcal K\ne0$. If it fails, no divided transfer is to be formed.
3. The exact
   

$$
g_{11}^{\mathrm{tr}}
   =\gcd(D^2,|\mathcal K|,|\mathcal T|),
$$


   with an extended-gcd certificate.
4. The actual primitive transfer triple
   

$$
(\alpha_{11},\beta_{11},\chi_{11}),
$$


   with
   

$$
\gcd(|\alpha_{11}|,|\beta_{11}|,\chi_{11})=1
$$


   and zero coefficient residuals in
   

$$
\chi_{11}F^+-\alpha_{11}F-\beta_{11}.
$$


5. The two exact residual integers obtained by stripping every prime at most $67$ from $|\alpha_{11}|$ and $\chi_{11}$.

A residual greater than $1$ would disprove the proposed unrestricted $S$-unit inheritance lemma at this auxiliary pair. Residuals equal to $1$ would establish only this one finite support test.

If the coefficient-content identity (9.6) is also checked, the inputs must include the actual all-prime $G_{11}$ and $G_{12}$, each with a Bézout certificate. They may not be replaced by the new forced divisors.

This is a test of the **actual least Schur clearer and inverse clearer**. It is not a repetition of the completed determinant-growth diagnostic, and it requires no unrestricted factorization of the residual integers.

---

## 12. Normalization and original-domain ledger

### 12.1 Compact coefficient clearers remain unchanged

For the rational polynomial $H_k/\Lambda_k^k$, put


$$
d_{H,k}=\gcd(\Lambda_k^k,H_{0,k},H_{1,k}).
$$


Its actual least simultaneous coefficient clearer and its remaining content are


$$
\frac{\Lambda_k^k}{d_{H,k}},
\qquad
\frac{G_k}{d_{H,k}}.
\tag{12.1}
$$



The new row and contact-column transformations are unimodular. The explicitly extracted factors are only:

* the exact right-column factor $E_k$;
* the actual transformed contact-column factor $C_k^{\mathrm{col}}$, if that optional primitive-column form is used.

The larger factor in (1.1) is established by minors, not by pretending that it is an entrywise row divisor. No unproved row content is extracted.

No nonsaturated contact frame is substituted. Consequently the previously separate saturation payment


$$
\frac{|\det C_k|}{\delta_{k,2k-1}}
$$


is not assigned a guessed value or silently spent.

### 12.2 Same infinite original compact indices

Let


$$
K_u=9^{18+32u},\qquad B=9^{32}.
$$


All new arithmetic theorems apply at every $K_u$, and the whole error there remains exactly


$$
0<\ell_{K_u}
=\frac{|H_{K_u}(s_0)|}{G_{K_u}}.
\tag{12.2}
$$



For consecutive original indices, both final gcds occur in


$$
\Delta_u^{\mathrm{orig}}
=
\frac{
H_{0,K_u}H_{1,BK_u}
-H_{0,BK_u}H_{1,K_u}
}{
G_{K_u}G_{BK_u}
}>0.
\tag{12.3}
$$


The accepted contraction implies


$$
\left(1-4^{-(B-1)K_u}\right)\ell_{K_u}
\le
\frac{\Delta_u^{\mathrm{orig}}}{q_{BK_u}}
<\ell_{K_u}.
\tag{12.4}
$$



No smallness statement for the right side has been proved. In particular, a selector using $k$ and $k+1$ must not be described as producing errors at original indices unless the selected index actually belongs to that set. Formula (12.4) keeps both candidates inside the original progression.

### 12.3 Separate binary producer

The separate original binary reconstruction remains on


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
$$


Its contact indices are $0,\ldots,b-1$, while its physical reconstruction includes $0,\ldots,b$, with


$$
z_b=0.
$$



The complete corrected columns remain


$$
x=\frac12RA^{-1}f,
\qquad
y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},
\qquad x=2^ax_0.
$$


The terms $h^F$, $e_0$, and the division by $4b!$ are retained.

The complete return is


$$
S=\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f,
$$


and the paid valuation remains only


$$
v_2\!\left(\frac{S}{2^{a+1}}\right)\ge\chi-a,
\qquad
\chi=v_2\binom{n+b-1}{b-1}.
$$



The norm $Q=x_0^Tx_0$, corrected-column contents, least simultaneous clearer, and final all-prime scalar gcd of that producer are not evaluated here. Its established valuation


$$
v_3(q^{\mathrm{bin}})=n-\frac{b+15}{2}
$$


is not transferred to $q_k$.

---

## 13. Final assessment

### New proved arithmetic results

For the original finite compact matrices:

1. The complete divided contact moments satisfy
   

$$
\Delta^nc_0=2^n(n!g_n-(-1)^n),
$$


   with an evaluated forced recurrence.

2. Their integral numerators satisfy the all-prime transversality statement
   

$$
\gcd(b_n,\ldots,b_{n+4})=1.
$$



3. The transformed contact-column contents are exactly
   

$$
2^{\max(1,j)}.
$$



4. The tempting complete factorial normalization has actual column clearer
   

$$
(2k-1+j)!
$$


   and remaining column content $1$; it is not a free unimodular normalization.

5. The actual contact determinantal divisors satisfy (6.1), yielding
   

$$
\boxed{
   2^{k(k-1)}D_{k-1}^{\mathrm{Lag}}E_k\mid G_k.
   }
$$



6. This gives the explicit improved ceilings (7.4)–(7.5) for the actual primitive denominator and actual adjacent cross difference.

### Exact failed step

The homogeneous recurrence does not govern the complete columns: its omitted forcing is explicitly (4.14) and (4.20). Even before Schur elimination, column shifts create the nonzero defect (8.3). Eliminating those additional terms incurs actual interpolation denominators, whose primitive payments are $\alpha_k,\beta_k,\chi_k$, not merely the small factors from the original moment transfer.

### Remaining mathematical bottleneck

The decisive requirement is still an all-prime estimate for the **actual final content or actual paid adjacent ratio**. In particular, one of the following would suffice for a substantive resolution of this family’s status:

* an actual upper bound
  

$$
\log G_k\le(4-\eta)k^2\log k+O(k^2),\qquad \eta>0,
$$


  on the required infinite domain, which together with raw leading $4$ would force whole-error divergence there; or

* an actual bound
  

$$
\frac{|\mathcal T|}
  {t^kG_k|\mathcal K|}\longrightarrow0
$$


  at the same infinite original indices, which by (3.9) would give nonzero whole errors tending to zero and therefore prove irrationality.

Neither has been proved.

The new result is therefore a rigorous, nontrivial arithmetic strengthening of the forced content, together with a fully evaluated obstruction to the simplest recurrence-inheritance argument. It does not yet resolve the all-prime primitive normalization, and it does not decide the rationality or irrationality of $e+\pi$.
