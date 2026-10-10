> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 Turn 20 — Independent referee report and a sharper evaluated rational-error bound

## 1. Executive decisions

The global objective remains unresolved: **this report proves neither rationality nor irrationality of $e+\pi$.**

The two reports under review are mathematically compatible with the already accepted Turn 19 theorem for the **same integer polynomial**


$$
\log |H_k(e+\pi)|=4k^2\log k+O(k^2).
$$



My decisions are as follows.

1. **A5’s complementary-minor estimate is accepted.** The enlargement from even polynomials to all polynomials has the correct inequality direction. The coefficient-functional normalization, Laguerre norms, and Jacobi complementary-minor identity are correct.

2. **A5’s exterior, overlap, and atom estimates are accepted.** They use the exact exterior density, the full overlap mass, and the entire negative-atom contribution. The cutoff $k\ge64$ and its numerical constants are valid without finite computation.

3. **A5’s actual slope extraction is accepted.** The contact atom disappears from that particular identity because of an exact cross-Vandermonde zero, not because it was neglected. The sign is $(-1)^k$, and the extracted coefficient is the actual $H_{1,k}$.

4. **A5’s inequality (7.8) is accepted with its displayed constants.** It concerns the ordinary rational error
   

$$
e+\pi-\frac{p_k}{q_k},
$$


   not the whole primitive error. Its convergence assertion does not imply irrationality.

5. **A3’s individual column clearers and valuation formula for $E_k$ are accepted.** They are exact least clearers of the complete raw rational columns.

6. **A3’s product divisibility is accepted:**
   

$$
D_{k-1}E_k\mid G_k.
$$


   The proof genuinely establishes the product, including at shared primes.

7. **A3’s same-$G_k$ slope-height ceiling is accepted.** It gives
   

$$
G_k\le U_k,\qquad \log U_k=4k^2\log k+O(k^2).
$$



8. **A3’s content envelope remains a conjecture.** No supplied argument excludes additional large-prime content or bounds its higher prime-power depth. With the now accepted leading-$4$ raw scale, its conditional consequence improves to
   

$$
\log\!\left(q_k(e+\pi)-p_k\right)
   \ge 3k^2\log k-O(k^2),
$$


   rather than the weaker leading-$1$ statement in A3.

9. **A further unconditional evaluated consequence is proved here.** For the actual primitive rationals, for every $k\ge64$,
   

$$
\boxed{
   \frac{1}{16k^2\,204^{\,k-1}}
   \le
   e+\pi-\frac{p_k}{q_k}
   \le
   \frac{336}{11^{\,k-1}}.
   }
   \tag{1.1}
$$


   This improves both exponential bases in A5’s rational-error estimate. It still does not settle the whole primitive error, because the actual $q_k$, equivalently the actual all-prime $G_k$, remains uncontrolled at the required scale.

No additional finite computation is needed for these symbolic conclusions.

---

## 2. Exact objects and normalization

Throughout the compact construction,


$$
k\ge2,\qquad 0\le m<2k,\qquad 0\le j<k.
$$


Thus


$$
m+j\le3k-2.
$$



Retain the complete recurrences


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
C_{mj}=c_{m+j},\qquad \mathcal R_{mj}=r_{m+j},
\qquad w_m=(-1)^m,\qquad v_j=(-1)^j,
$$


and


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5).
$$


The integer affine polynomial is exactly


$$
H_k(s)=
\det[C\mid \Lambda_k\mathcal R+s\Lambda_kwv^T]
=H_{0,k}+H_{1,k}s.
\tag{2.1}
$$



The maximum factorial degree is $6k-4$; the final rational moment is $r_{3k-2}$; the final odd denominator allowed by its recurrence is $6k-5$. Neither report extends the physical matrix.

Write


$$
s_0=e+\pi,\qquad
G_k=\gcd(|H_{0,k}|,|H_{1,k}|).
$$


The previously accepted sign theorem gives, for $k\ge32$,


$$
(-1)^kH_k(s_0)>0,\qquad (-1)^kH_{1,k}>0.
$$


Accordingly,


$$
q_k=\frac{|H_{1,k}|}{G_k},\qquad
p_k=-\frac{\operatorname{sgn}(H_{1,k})H_{0,k}}{G_k},
$$


and


$$
\ell_k:=q_ks_0-p_k
=\frac{|H_k(s_0)|}{G_k}>0.
\tag{2.2}
$$


In particular,


$$
s_0-\frac{p_k}{q_k}
=\frac{|H_k(s_0)|}{|H_{1,k}|}
=\frac{\ell_k}{q_k}.
\tag{2.3}
$$



The cancellation of $G_k$ in (2.3) is legitimate. Its disappearance from that quotient does **not** permit its disappearance from (2.2).

---

## 3. Endpoint measures, moments, and determinant signs

### 3.1 The charge measure

The measure


$$
d\eta(t)=e^{t-1}\,dt,\qquad t\le1,
$$


has total mass one. Integration by parts gives


$$
\int t^d\,d\eta(t)=1-d\int t^{d-1}\,d\eta(t)=a_d.
$$



Its pushforward under $x=t^2$ is


$$
d\mu(x)=
\frac{e^{-1}}{2\sqrt x}
\left(e^{-\sqrt x}+\mathbf1_{(0,1)}(x)e^{\sqrt x}\right)\,dx.
\tag{3.1}
$$


Thus


$$
\int x^n\,d\mu(x)=a_{2n}.
$$



On $x=s^2>1$, only the negative $t$-branch occurs, so


$$
d\mu(x)=e^{-1}e^{-s}\,ds,\qquad s>1.
\tag{3.2}
$$


Also,


$$
\mu([0,1])
=\eta([-1,1])
=\int_{-1}^{1}e^{t-1}\,dt
=1-e^{-2}.
\tag{3.3}
$$


The positive branch on $0<x<1$ is therefore fully present.

The signed functional is


$$
L(f)=\int f\,d\mu-f(-1).
\tag{3.4}
$$


Its negative atom has mass exactly $-1$.

### 3.2 The compact measure

The compact measure is


$$
d\nu(x)=
\frac{e^{\sqrt x}+4/(1+x)}{2\sqrt x}\,
\mathbf1_{(0,1)}(x)\,dx.
\tag{3.5}
$$


Equivalently,


$$
\int f\,d\nu
=\int_0^1 f(t^2)
\left(e^t+\frac4{1+t^2}\right)\,dt.
$$



The complete endpoint calculation is


$$
\int_0^1 e^t t^{2n}\,dt=e\,a_{2n}-(2n)!,
$$




$$
4\int_0^1\frac{t^{2n}}{1+t^2}\,dt
=\pi(-1)^n+4\rho_n.
$$


Consequently,


$$
\nu_n=e\,c_n+s_0(-1)^n+r_n.
\tag{3.6}
$$


Both the factorial endpoint and the complete arctangent correction are retained.

For $0\le t\le1$,


$$
3\le e^t+\frac4{1+t^2}<7.
$$


Therefore, with


$$
J_k^\nu=\det(\nu_{i+j})_{i,j<k},
\qquad
h_k=\det\left(\frac1{2i+2j+1}\right)_{i,j<k},
$$


positive-semidefinite comparison gives


$$
3^kh_k\le J_k^\nu\le7^kh_k.
\tag{3.7}
$$



### 3.3 Orthogonal compression and its sign

Let $P_n$ be the monic orthogonal polynomials for $\nu$, and define


$$
T^{(k)}_{rj}=L(x^jP_{k+r}(x)),\qquad 0\le r,j<k.
$$


Equation (3.6) gives


$$
H_k(s_0)=\Lambda_k^k\det[C\mid N],
\qquad N_{mj}=\nu_{m+j}.
$$


The unitriangular replacement of monomials by $P_0,\ldots,P_{2k-1}$ has determinant one. After exchanging the two $k$-column groups, the compact block contributes $J_k^\nu$. Hence


$$
\boxed{
H_k(s_0)=(-1)^{k^2}\Lambda_k^kJ_k^\nu\det T^{(k)}.
}
\tag{3.8}
$$


Since $k^2\equiv k\pmod2$, the sign is $(-1)^k$.

The normalized alternant identity is


$$
A_k(x):=
\frac{\det(P_{k+r}(x_i))_{r,i}}{V(x)}
=
\frac1{k!J_k^\nu}
\int V(y)^2\prod_{i,j}(x_i-y_j)\,d\nu^k(y).
\tag{3.9}
$$


The denominator $k!J_k^\nu$ is correct: Andréief’s identity gives


$$
\int V(y)^2\,d\nu^k(y)=k!J_k^\nu.
$$


Thus the measure in (3.9) is a probability measure.

Applying determinant integration once more,


$$
\det T^{(k)}
=\frac1{k!}\int V(x)^2A_k(x)\,dL^k(x).
\tag{3.10}
$$


Terms with at least two atoms vanish because $V(x)^2=0$ at repeated coordinates. The remaining decomposition is exactly


$$
\det T^{(k)}=D_{\mu,k}-D_{a,k},
\tag{3.11}
$$


with the normalizations and atom factors stated in A5.

**Decision:** all measures, endpoint moments, normalizations, and signs in these identities are correct.

---

## 4. Referee check of the coefficient-functional enlargement

Define


$$
Z_{n,\alpha}
=\det((2\alpha+2i+2j)!)_{0\le i,j<n},
\qquad Z_{0,\alpha}=1,
$$


and


$$
Z_k=Z_{k,k}.
$$


Let


$$
M=((2k+2i+2j)!)_{0\le i,j<k}.
$$


This is the Gram matrix of


$$
1,s^2,\ldots,s^{2k-2}
$$


for


$$
\langle f,g\rangle_k
=\int_0^\infty f(s)g(s)s^{2k}e^{-s}\,ds.
\tag{4.1}
$$



Deleting the first $m$ rows and columns leaves $Z_{k-m,k+2m}$. Jacobi’s complementary-minor identity therefore gives


$$
\frac{Z_{k-m,k+2m}}{Z_k}
=\det((M^{-1})_{ij})_{0\le i,j<m}.
\tag{4.2}
$$



### 4.1 Why enlargement gives an upper bound

On the even-polynomial space, the squared norm of the coefficient functional


$$
f\longmapsto[s^{2i}]f
$$


is $(M^{-1})_{ii}$.

For nested inner-product spaces, the supremum defining a functional norm can only increase when its domain is enlarged. Thus restriction from all polynomials of degree at most $2k-2$ to the even subspace gives


$$
(M^{-1})_{ii}
\le
\|[s^{2i}]\|_{\text{full space}}^2.
\tag{4.3}
$$


This is the correct direction.

### 4.2 Exact full-space norm bound

Use the monic Laguerre polynomials


$$
Q_r(s)=(-1)^rr!L_r^{(2k)}(s),
\qquad 0\le r\le2k-2.
$$


Their coefficients and norms are


$$
Q_r(s)=(-1)^rr!
\sum_{d=0}^r(-1)^d
\binom{r+2k}{r-d}\frac{s^d}{d!},
$$




$$
\|Q_r\|_k^2=r!(r+2k)!.
\tag{4.4}
$$


The Rodrigues integration-by-parts proof has vanishing boundary terms: the polynomial powers at zero suffice through all $r$ integrations, and the exponential controls infinity.

For $d\le r$,


$$
\frac{|[s^d]Q_r|}{|Q_r(0)|}
=
\frac{r(r-1)\cdots(r-d+1)}
{d!(2k+1)(2k+2)\cdots(2k+d)}
\le\frac1{d!}.
\tag{4.5}
$$


When $d>r$, the coefficient is zero.

Orthogonal expansion therefore yields


$$
(M^{-1})_{ii}
\le
\frac1{((2i)!)^2}
\sum_{r=0}^{2k-2}
\frac{Q_r(0)^2}{r!(r+2k)!}.
$$


Since


$$
Q_r(0)=(-1)^r\frac{(r+2k)!}{(2k)!},
$$


the sum is


$$
\frac1{(2k)!}
\sum_{r=0}^{2k-2}\binom{2k+r}{2k}
=
\frac{\binom{4k-1}{2k-2}}{(2k)!}.
$$


Write


$$
K_k^{\mathrm{coef}}
=\frac{\binom{4k-1}{2k-2}}{(2k)!}.
$$


Hadamard’s inequality in (4.2) proves


$$
\boxed{
\frac{Z_{k-m,k+2m}}{Z_k}
\le
\frac{(K_k^{\mathrm{coef}})^m}
{\prod_{i=0}^{m-1}((2i)!)^2}
\le (K_k^{\mathrm{coef}})^m.
}
\tag{4.6}
$$



This includes $m=0$ and $m=k$.

### 4.3 Boundary qualification

The full-space enlargement introduces auxiliary odd polynomial degrees, but it does not enlarge the physical matrix or require higher factorial degrees. The largest weighted product degree is


$$
2k+2(2k-2)=6k-4.
$$


That is exactly the original maximal factorial boundary.

The factorial determinant bounds


$$
\boxed{
\prod_{i=0}^{k-1}(2i)!(2k+2i)!
\le Z_k
\le
\prod_{i=0}^{k-1}(2k+4i)!
}
\tag{4.7}
$$


also follow correctly. The lower bound compares each constrained even monic minimum with the unrestricted monic minimum; the upper bound is Gram-Hadamard.

**Decision:** A5’s conditioning argument is accepted in full.

---

## 5. Exterior, overlap, atom, and cutoff audit

To avoid confusing A5’s exterior contribution with A3’s arithmetic factor $E_k$, denote the former by $\mathcal E_k$.

Put


$$
a_{\mathrm{in}}=1-e^{-2},\qquad
z_k=(e-e^{-1})K_k^{\mathrm{coef}},
\qquad
b_k=\frac{e\,8^k}{4}K_k^{\mathrm{coef}}.
$$



### 5.1 Exterior shift

For all $x_i>1$, (3.9) gives


$$
\prod_i(x_i-1)^k\le A_k(x)\le\prod_i x_i^k.
$$


The exact exterior density gives


$$
\mathcal E_k\le e^{-k}Z_k.
$$



For the lower bound, write $s_i=t_i+1$. Then


$$
(s_i^2-1)^k\ge t_i^{2k},
$$


and


$$
|(t_j+1)^2-(t_i+1)^2|
=|t_j-t_i|(t_j+t_i+2)
\ge |t_j^2-t_i^2|.
$$


Each density supplies $e^{-2}e^{-t_i}\,dt_i$. Hence


$$
\boxed{
e^{-2k}Z_k\le\mathcal E_k\le e^{-k}Z_k.
}
\tag{5.1}
$$



### 5.2 Complete overlap contribution

With exactly $m$ inside variables:

- their mutual squared Vandermonde is at most one;
- every inside–outside pair costs at most $x_{\mathrm{outside}}^2$;
- the alternant costs at most $\prod_{\mathrm{outside}}x_i^k$;
- the inside mass is exactly $a_{\mathrm{in}}^m$.

The choice of the $m$ inside variables, combined with $1/k!$, leaves the factor $1/m!$ after the outside integral is written as $Z_{k-m,k+2m}$. Thus


$$
|\text{\(m\)-inside contribution}|
\le
\frac{a_{\mathrm{in}}^m}{m!}
e^{-(k-m)}Z_{k-m,k+2m}.
$$


Using (4.6) and summing,


$$
\boxed{
|D_{\mu,k}-\mathcal E_k|
\le e^{-k}Z_k(e^{z_k}-1).
}
\tag{5.2}
$$



### 5.3 Complete atom contribution

At the actual atom,


$$
|-1-y_j|\le2,
$$


so the alternant contributes at most $2^k$ in addition to the outside powers. Also


$$
(x+1)^2\le4\quad(0\le x\le1),\qquad
(x+1)^2\le4x^2\quad(x>1).
$$


Consequently,


$$
|D_{a,k}|
\le
2^k4^{k-1}
\sum_{m=0}^{k-1}
\frac{a_{\mathrm{in}}^m}{m!}
e^{-(k-1-m)}
Z_{k-1-m,k+2m+2}.
$$


Applying (4.6) with deleted size $m+1$ gives


$$
\boxed{
|D_{a,k}|\le e^{-k}Z_k\,b_ke^{z_k}.
}
\tag{5.3}
$$


This is the whole atom term, not a selected endpoint contribution.

In both (5.2) and (5.3), the largest factorial degree in the nonempty determinants remains $6k-4$.

### 5.4 Uniform numerical cutoff

The elementary estimate


$$
K_k^{\mathrm{coef}}
\le\frac{16^k}{(2k)!}
\le\left(\frac{36}{k^2}\right)^k
\tag{5.4}
$$


uses only $e<3$ and $(2k)!\ge(2k/e)^{2k}$.

For $k\ge64$, it gives $K_k^{\mathrm{coef}}<1/6$, hence


$$
z_k<\frac12,\qquad e^{z_k}<2,\qquad
e^{z_k}-1\le6K_k^{\mathrm{coef}}.
$$


The total adverse contribution relative to $e^{-2k}Z_k$ is at most


$$
\varepsilon_k
=e^k\bigl[e^{z_k}(1+b_k)-1\bigr].
$$


Therefore


$$
\varepsilon_k
\le6\cdot3^kK_k^{\mathrm{coef}}
+\frac32\,24^kK_k^{\mathrm{coef}}
\le2\cdot24^kK_k^{\mathrm{coef}},
$$


where the last inequality already holds for $k\ge2$. Thus


$$
\varepsilon_k
\le\frac{2\cdot384^k}{(2k)!}
\le2\left(\frac{864}{k^2}\right)^k
\le2\cdot4^{-k}<\frac12
\qquad(k\ge64).
\tag{5.5}
$$


Here $864/64^2<1/4$, and the ratio decreases thereafter.

It follows that


$$
\boxed{
\frac12e^{-2k}Z_k
\le\det T^{(k)}
\le2e^{-k}Z_k,\qquad k\ge64.
}
\tag{5.6}
$$



**Decision:** the complete comparison and the cutoff are accepted.

---

## 6. Actual slope extraction and A5’s rational-error constants

### 6.1 The slope is an actual coefficient

From (3.6),


$$
H_k(s_0+z)
=\Lambda_k^k\det[C\mid N+zwv^T].
$$


The right block is the moment block of $\nu+z\delta_{-1}$.

In the two-measure determinant formula, extracting one compact atom gives


$$
\begin{aligned}
\frac{H_{1,k}}{\Lambda_k^k}
={}&\frac1{k!(k-1)!}
\int V(x)^2V(y)^2\prod_j(y_j+1)^2\\
&\quad\cdot
\prod_i(-1-x_i)\prod_{i,j}(y_j-x_i)
\,d\mu^k(x)\,d\nu^{k-1}(y).
\end{aligned}
\tag{6.1}
$$


A contact atom at the same point would make a cross factor zero. This explains the appearance of $\mu$ rather than $L$.

There are $k+k(k-1)=k^2$ reversed cross factors. Thus the extracted sign is $(-1)^k$.

Define


$$
d\nu_+(y)=(1+y)^2\,d\nu(y),
\qquad
J_{k-1}^+=\det\left(\int y^{a+b}\,d\nu_+(y)\right)_{a,b<k-1}.
$$


Then


$$
\boxed{
(-1)^kH_{1,k}=\Lambda_k^kJ_{k-1}^+S_k,
}
\tag{6.2}
$$


with $S_k$ as in A5.

For exterior variables,


$$
(x+1)\prod_{j=1}^{k-1}(x-y_j)\ge(x-1)^k.
$$


For arbitrary variables, its absolute value is at most $2$ inside and $2x^k$ outside. Consequently the exterior lower bound is $e^{-2k}Z_k$, while the absolute overlap loss is at most


$$
2^ke^{-k}Z_k(e^{z_k}-1).
$$


Its relative size is bounded by


$$
6\cdot6^kK_k^{\mathrm{coef}}
\le\frac{6\cdot96^k}{(2k)!}
\le\frac{2\cdot384^k}{(2k)!}<\frac12.
$$


Therefore


$$
\boxed{
\frac12e^{-2k}Z_k\le S_k\le2^{k+1}e^{-k}Z_k
\qquad(k\ge64).
}
\tag{6.3}
$$



This proves actual slope nonvanishing on the same indices as (5.6).

### 6.2 Verification of (7.8)

Combining (3.8), (5.6), (6.2), and (6.3),


$$
\frac{e^{-k}}{2^{k+2}}
\frac{J_k^\nu}{J_{k-1}^+}
\le
s_0-\frac{p_k}{q_k}
\le
4e^k\frac{J_k^\nu}{J_{k-1}^+}.
\tag{6.4}
$$



The compact weight bounds give


$$
3^{k-1}h_{k-1}\le J_{k-1}^+\le28^{k-1}h_{k-1}.
$$


Cauchy’s determinant formula gives


$$
\frac{h_k}{h_{k-1}}
=
\frac{16^{k-1}}
{(4k-3)\binom{4k-4}{2k-2}^2}.
$$


Using


$$
\frac{2^{2n}}{2n+1}\le\binom{2n}{n}\le2^{2n},
\qquad n=2k-2,
$$


one obtains


$$
\frac1{(4k-3)16^{k-1}}
\le\frac{h_k}{h_{k-1}}
\le\frac{4k-3}{16^{k-1}}.
$$



For the lower error bound, $e^{-k}\ge3^{-k}$ gives


$$
\frac{e^{-k}}{2^{k+2}}
\frac{3^k}{28^{k-1}}
\frac1{(4k-3)16^{k-1}}
\ge
\frac{112}{(4k-3)896^k}.
$$


For the upper error bound, $e^k\le3^k$ gives


$$
4e^k\frac{7^k}{3^{k-1}}
\frac{4k-3}{16^{k-1}}
\le
84(4k-3)\left(\frac7{16}\right)^{k-1}.
$$



Thus A5’s displayed inequality is correct:


$$
\boxed{
\frac{112}{(4k-3)896^k}
\le s_0-\frac{p_k}{q_k}
\le84(4k-3)\left(\frac7{16}\right)^{k-1}.
}
\tag{6.5}
$$



Its sufficient and necessary conditions for whole-error decay are also correctly directed. They remain unproved arithmetic conditions on the actual primitive $q_k$.

---

## 7. Referee check of A3’s arithmetic factors

### 7.1 Exact individual column clearers

The recurrence gives


$$
r_{n+1}+r_n
=-(2n+2)!-(2n)!+\frac4{2n+1}.
\tag{7.1}
$$


For column $j$, define


$$
\Lambda_{k,j}=\operatorname{lcm}(1,3,\ldots,4k+2j-3).
$$



Sufficiency is immediate from the full recurrence: each $\rho_n$ in that column uses only odd denominators at most $4k+2j-3$.

For necessity, suppose $C$ clears


$$
r_j,\ldots,r_{2k-1+j}.
$$


Using (7.1) only for


$$
j\le n\le2k-2+j
$$


shows


$$
2n+1\mid C.
$$


Thus every odd integer in


$$
[2j+1,\,4k+2j-3]
\tag{7.2}
$$


divides $C$.

If an odd prime power $q\le4k+2j-3$ lies below $2j+1$, then $q\le2j-1$. Its least odd multiple not below $2j+1$ is less than


$$
2j+1+2q\le6j-1\le4k+2j-3,
$$


because $j\le k-1$. Hence (7.2) also forces $q\mid C$.

Therefore


$$
\boxed{
\Lambda_{k,j}\text{ is the actual least clearer of column }j.
}
\tag{7.3}
$$


No successor moment is used. The final column has clearer $\Lambda_k$, so the least clearer of the entire raw array remains exactly $\Lambda_k$.

### 7.2 Exact factor and its prime powers

Column extraction gives


$$
H_k(s)=E_k\widehat H_k(s),
\qquad
E_k=\prod_{j=0}^{k-1}\frac{\Lambda_k}{\Lambda_{k,j}},
\tag{7.4}
$$


where $\widehat H_k\in\mathbb Z[s]$.

For an odd prime $p$,


$$
v_p(E_k)
=
\sum_{\substack{a\ge1\\p^a\le6k-5}}
\#\{0\le j<k:4k+2j-3<p^a\}.
$$


If $p^a\le4k-3$, the contribution is zero. Otherwise, putting


$$
d=\frac{p^a-4k+3}{2},
$$


the inequality is exactly $j<d$. Since $1\le d\le k-1$, the count is $d$. Therefore


$$
\boxed{
v_p(E_k)=
\sum_{\substack{a\ge1\\4k-3<p^a\le6k-5}}
\frac{p^a-4k+3}{2},
\qquad v_2(E_k)=0.
}
\tag{7.5}
$$



### 7.3 Why the product $D_{k-1}E_k$ divides

Reuse the established contact-minor theorem, with its negative atom retained:


$$
D_{k-1}:=\prod_{r=0}^{k-2}(r!)^2
$$


divides every size-$k$ contact minor.

Expand $\widehat H_k(s)$ along its contact columns. Every complementary right-block minor is an integer polynomial. Hence


$$
D_{k-1}\mid\widehat H_{0,k},
\qquad
D_{k-1}\mid\widehat H_{1,k}.
$$


Multiplying by the exact scalar $E_k$ in (7.4) proves


$$
\boxed{D_{k-1}E_k\mid G_k.}
\tag{7.6}
$$



This argument remains valid when $D_{k-1}$ and $E_k$ share primes. It does not infer a product from two unrelated divisibility statements.

**Decision:** A3’s least-clearer theorem, valuation formula, and product divisibility are accepted.

---

## 8. The same-$G_k$ height ceiling and the conjectural envelope

### 8.1 Slope-height ceiling

Conditioning the slope identity on $y$ gives the matrix


$$
(\widetilde M_y)_{ab}
=\int x^{a+b}(x+1)\prod_{j=1}^{k-1}(x-y_j)\,d\mu(x).
$$


For $0\le x\le1$, the polynomial factor has absolute value at most $2$; for $x\ge1$, at most $2x^k$. With $N=k+a+b$,


$$
|(\widetilde M_y)_{ab}|
\le2+2a_{2N}\le4(2N)!.
\tag{8.1}
$$



The convexity of $n\mapsto\log((2k+2n)!)$ shows that the largest permutation product pairs increasing row and column indices. Explicitly, swapping an inverted pairing $a<b$, $c<d$ increases the product because


$$
f(a+c)+f(b+d)\ge f(a+d)+f(b+c)
$$


for convex $f$. Thus


$$
|\det\widetilde M_y|
\le4^kk!\prod_{r=0}^{k-1}(2k+4r)!.
$$


Finally,


$$
(1+t^2)^2\left(e^t+\frac4{1+t^2}\right)\le28,
$$


so


$$
J_{k-1}^+\le28^{k-1}h_{k-1}.
$$


It follows that


$$
|H_{1,k}|\le
U_k:=
\Lambda_k^k4^kk!28^{k-1}h_{k-1}
\prod_{r=0}^{k-1}(2k+4r)!.
\tag{8.2}
$$


Since $H_{1,k}\ne0$ for $k\ge32$,


$$
\boxed{G_k\le|H_{1,k}|\le U_k.}
\tag{8.3}
$$



All moments used have index at most $3k-2$. Also


$$
\log U_k=4k^2\log k+O(k^2).
$$



### 8.2 Compatibility with Turn 19

The A5 bounds independently give


$$
\log|H_k(s_0)|=4k^2\log k+O(k^2).
$$


This agrees with, and does not replace or weaken, the accepted Turn 19 theorem valid already for $k\ge32$.

A5 also gives the matching slope scale


$$
\boxed{
\log|H_{1,k}|=4k^2\log k+O(k^2).
}
\tag{8.4}
$$


Indeed $J_{k-1}^+$ has logarithm $O(k^2)$, and the additional factors in (6.2)–(6.3) contribute only $O(k)$.

Consequently,


$$
\log q_k=4k^2\log k-\log G_k+O(k^2),
$$




$$
\log\ell_k=4k^2\log k-\log G_k+O(k^2).
\tag{8.5}
$$



A3’s leading-$2$ lower estimate remains a valid weaker inequality, but it is no longer the best current lower scale and should not be used as such.

### 8.3 Content envelope: conditional, not established

A3 proposes


$$
G_k\mid
B_k:=D_{k-1}E_k\,2^{2k^2}\Lambda_k^{2k}.
\tag{8.6}
$$


Since


$$
\log D_{k-1}=k^2\log k+O(k^2),
\qquad
\log E_k=O(k^2),
\qquad
\log\Lambda_k=O(k),
$$


this would imply


$$
\log G_k\le k^2\log k+O(k^2).
$$


Using the accepted leading-$4$ lower scale,


$$
\boxed{
\log\ell_k\ge3k^2\log k-O(k^2)\longrightarrow+\infty.
}
\tag{8.7}
$$


Together with (7.6), the envelope would in fact give


$$
\log G_k=k^2\log k+O(k^2),
$$


and hence


$$
\log q_k=\log\ell_k=3k^2\log k+O(k^2).
\tag{8.8}
$$



These are conditional deductions only.

The obstruction is exactly the one identified in A3. For


$$
A_k=[C\mid\Lambda_k\mathcal R],\qquad
u_k=\Lambda_kw,\qquad z_k=(0,\ldots,0,v)^T,
$$


a prime $p>6k-5$ divides $G_k$ precisely when


$$
\det A_k\equiv0,\qquad
z_k^T\operatorname{adj}(A_k)u_k\equiv0\pmod p.
$$


Rank at most $2k-2$ forces both congruences. Rank $2k-1$ reduces the second to a nullvector transversality condition. The moment recurrences do not rule out either mechanism, and reduction modulo $p$ alone does not control higher powers.

**Decision:** the conjecture is neither accepted nor disproved here.

---

## 9. New evaluated consequence: a sharper rational-error theorem

The determinant ratios in A5 can be bounded more efficiently than by separately comparing $J_k^\nu$ and $J_{k-1}^+$. Their ratio is an exact Christoffel extremal quantity.

### 9.1 Exact ratio identity

Let $m=k-1$, and let


$$
K_m^\nu(a,a)
$$


be the squared norm of evaluation at $a$ on polynomials of degree at most $m$, with norm from $\nu$.

Adding an atom $t\delta_{-1}$ to the $k\times k$ moment matrix is a rank-one update. The coefficient of $t$ in its determinant is


$$
J_k^\nu K_m^\nu(-1,-1).
$$


On the other hand, extracting that atom in the determinant integral gives


$$
J_{k-1}^{(x+1)^2\nu}=J_{k-1}^+.
$$


Therefore


$$
\boxed{
R_k:=\frac{J_k^\nu}{J_{k-1}^+}
=\frac1{K_m^\nu(-1,-1)}
=\min_{\substack{\deg p\le m\\p(-1)=1}}
\int_0^1p(x)^2\,d\nu(x).
}
\tag{9.1}
$$


The extremal formula follows directly from Cauchy–Schwarz in the finite-dimensional polynomial Hilbert space.

This identity concerns the existing positive compact measure. It introduces no new arithmetic normalization.

### 9.2 Evaluated lower bound for $R_k$

From the exact density,


$$
\frac{d\nu}{dx}\ge\frac32,\qquad0<x<1.
\tag{9.2}
$$


For Lebesgue measure on $[0,1]$, the orthonormal polynomials are


$$
\sqrt{2r+1}\,P_r(2x-1),
$$


where $P_r$ is the ordinary Legendre polynomial. Thus


$$
K_m^{dx}(-1,-1)=
\sum_{r=0}^m(2r+1)P_r(3)^2.
$$



Put


$$
\beta=3+2\sqrt2.
$$


The classical integral formula


$$
P_r(3)=\frac1\pi\int_0^\pi
(3+2\sqrt2\cos\theta)^r\,d\theta
$$


implies $0<P_r(3)\le\beta^r$. Its normalization can be checked by summing the geometric series under the integral: the generating function is


$$
(1-6t+t^2)^{-1/2},
$$


the Legendre generating function at $3$.

It follows that


$$
K_m^{dx}(-1,-1)
\le\beta^{2m}\sum_{r=0}^m(2r+1)
=(m+1)^2\beta^{2m}.
$$


Every polynomial with $p(-1)=1$ therefore satisfies


$$
\int p^2\,d\nu
\ge\frac32\int p^2\,dx
\ge\frac{3}{2k^2\beta^{2(k-1)}}.
$$


Hence


$$
R_k\ge\frac{3}{2k^2\beta^{2(k-1)}}.
\tag{9.3}
$$



### 9.3 Evaluated upper bound for $R_k$

Use the admissible polynomial


$$
p(x)=\frac{T_m(2x-1)}{T_m(-3)},
$$


where $T_m$ is the Chebyshev polynomial. On $[0,1]$,


$$
|T_m(2x-1)|\le1,
$$


while


$$
|T_m(-3)|=T_m(3)
=\frac{\beta^m+\beta^{-m}}2
\ge\frac{\beta^m}{2}.
$$


Since $\nu([0,1])<7$,


$$
R_k\le\int p^2\,d\nu
\le\frac{28}{\beta^{2(k-1)}}.
\tag{9.4}
$$



No extra physical moment is used: all squared test polynomials have degree at most $2k-2$.

### 9.4 New rational and whole-error bounds

Insert (9.3)–(9.4) into (6.4). With


$$
A=\beta^2=17+12\sqrt2,
$$


we obtain


$$
\frac{3}{2^{k+3}e^k k^2A^{k-1}}
\le s_0-\frac{p_k}{q_k}
\le\frac{112e^k}{A^{k-1}}.
\tag{9.5}
$$



Using $e<3$, $33<A<34$, this gives the entirely rational evaluated bounds


$$
\boxed{
\frac1{16k^2\,204^{k-1}}
\le s_0-\frac{p_k}{q_k}
\le\frac{336}{11^{k-1}},
\qquad k\ge64.
}
\tag{9.6}
$$



Multiplying by the **actual** primitive denominator,


$$
\boxed{
\frac{q_k}{16k^2\,204^{k-1}}
\le\ell_k
\le\frac{336q_k}{11^{k-1}}.
}
\tag{9.7}
$$



Thus:

- a sufficient condition for primitive decay on an infinite set is
  

$$
q_k=o(11^{k-1});
  \tag{9.8}
$$


- a necessary condition for primitive decay is
  

$$
q_k=o(k^2\,204^{k-1}).
  \tag{9.9}
$$



These improve A5’s corresponding sufficient and necessary conditions. Neither is presently established.

### 9.5 Combined arithmetic interpretation

By the accepted product divisor, define the actual residual content


$$
\Gamma_k=\frac{G_k}{D_{k-1}E_k}\in\mathbb Z_{>0}.
$$


Then (8.5) becomes


$$
\boxed{
\log q_k
=3k^2\log k-\log\Gamma_k+O(k^2),
\qquad
\log\ell_k
=3k^2\log k-\log\Gamma_k+O(k^2).
}
\tag{9.10}
$$



Accordingly, a subsequence with $\ell_k\to0$ would necessarily require


$$
\log\Gamma_k\ge3k^2\log k-O(k^2).
\tag{9.11}
$$


By contrast, A3’s conjectural envelope permits only


$$
\log\Gamma_k=O(k^2).
$$


This makes the unresolved arithmetic alternatives explicit. The known forced factors remove only the leading-$1$ factorial scale; successful primitive decay would require almost all of the remaining leading-$3$ scale to occur in the **additional actual common content**.

---

## 10. Arithmetic ledger and original-domain preservation

### 10.1 Clearers and contents remain distinct

The following quantities are not identified with one another:

- raw-array least entry clearer: $\Lambda_k$;
- column least clearers: $\Lambda_{k,j}$;
- extracted column factor: $E_k$;
- contact-minor divisor: $D_{k-1}$;
- actual final coefficient gcd: $G_k$.

For the rational polynomial $H_k/\Lambda_k^k$, put


$$
d_{H,k}=\gcd(\Lambda_k^k,H_{0,k},H_{1,k}).
$$


Its actual least simultaneous coefficient clearer and remaining content are


$$
\frac{\Lambda_k^k}{d_{H,k}},
\qquad
\frac{G_k}{d_{H,k}}.
\tag{10.1}
$$


Neither is evaluated by the analytic comparison.

For a saturated integer contact basis $X$, with


$$
B_{rj}=\sum_mX_{rm}r_{m+j},\qquad
u_r=\sum_mX_{rm}(-1)^m,
$$


the actual entry clearer remains


$$
L_X=
\frac{\Lambda_k}
{\gcd(\Lambda_k,\{\Lambda_kB_{rj}\}_{r,j})}.
$$


Its row contents remain


$$
\gcd\bigl(L_Xu_r,\{L_XB_{rj}\}_j\bigr).
$$


If


$$
L_X^k\det\mathcal M_X(s)=A_0+A_1s,
$$


the least simultaneous coefficient clearer and remaining content are exactly


$$
\frac{L_X^k}{\gcd(L_X^k,A_0,A_1)},
\qquad
\frac{\gcd(A_0,A_1)}{\gcd(L_X^k,A_0,A_1)}.
\tag{10.2}
$$



For independently cleared monic contact rows, the exact polynomial clearers $d_m$, row clearers, actual row contents $\kappa_r$, subsequent column contents $\gamma_j$, and frame index


$$
J_k^{\mathrm{frame}}
=
\frac{\prod_{m=k}^{2k-1}d_m}
{|\det C_k|/\delta_{k,2k-1}}
$$


remain separate payments. The paid multiplier


$$
\frac{\prod_r d_{k+r}\ell_r^{\mathrm{row}}}
{\prod_r\kappa_r\prod_j\gamma_j}
$$


does not eliminate the need for the final coefficient gcd.

The direct block argument avoids selecting such a frame. It does not assert values for those contents.

### 10.2 Same infinite original indices, without producer transfer

Every compact theorem proved here holds at


$$
k=b(u)=9^{18+32u},\qquad u\ge0,
$$


because these indices exceed $64$.

The separate binary producer remains exactly


$$
b=9^{18+32u},\qquad n=4002b,
$$


with contact range $0,\ldots,b-1$, physical reconstruction range $0,\ldots,b$, and


$$
z_b=0.
$$



Its complete corrected columns remain


$$
x=\frac12RA^{-1}f,\qquad
y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},
\qquad x=2^ax_0.
$$


The full return is


$$
S=\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f.
$$


After division, the retained statement is only


$$
v_2\!\left(\frac{S}{2^{a+1}}\right)\ge\chi-a,
\qquad
\chi=v_2\binom{n+b-1}{b-1}.
$$


The subtraction of $a$, the forcing $h^F$, the correction $e_0$, the factor $4b!$, and the terminal condition are not removed.

The norm $Q=x_0^Tx_0$, corrected-column contents, least simultaneous clearer, and final all-prime gcd of that producer remain unevaluated here. Its established valuation


$$
v_3(q^{\mathrm{bin}})=n-\frac{b+15}{2}
$$


does not transfer to $q_k$.

Likewise, the distinct constructions reviewed in Turn 19 retain their own original admissibility conditions and arithmetic normalizations. No compact identity supplied here settles their remaining obligations.

---

## 11. Proof status, remaining lemma, and bounded arithmetic

### 11.1 New proved result

The principal new result of this turn is the exact extremal identity (9.1) and its evaluated consequence


$$
\frac1{16k^2\,204^{k-1}}
\le e+\pi-\frac{p_k}{q_k}
\le\frac{336}{11^{k-1}},
\qquad k\ge64.
$$


It applies to the actual primitive rationals and therefore also at the same infinite original indices $k=9^{18+32u}$.

The independent referee review also accepts A5’s conditioning and slope arguments and A3’s exact column factor and product divisor.

### 11.2 Concrete remaining follow-on lemma

An arithmetic lemma sufficient for an irrationality proof through this family would be:

> **Primitive-denominator lemma.** On an explicitly specified infinite subset of the original indices $k=9^{18+32u}$,
> 

$$
> \frac{|H_{1,k}|}{G_k}=o(11^{k-1}).
>
$$



By (9.7), this would give $0<\ell_k\to0$. If $s_0=A/B$ were rational, then


$$
\ell_k=\frac{Aq_k-Bp_k}{B}\ge\frac1B,
$$


a contradiction.

This lemma is **open**. It requires genuine control of the actual all-prime $G_k$, not replacement by $D_{k-1}E_k$.

In the opposite direction, A3’s proposed content envelope would prove primitive divergence for this compact family. It too remains open. Its large-prime rank-and-transversality requirement is not supplied by denominator enumeration or factorial divisibility.

### 11.3 Finite calculation status

**No finite calculation is required to establish the symbolic claims audited or proved here.** I do not commission a duplicate $k=32$ calculation or the optional $k=64$ calculation.

The coordinator’s already planned bounded $k=32$ test remains appropriately targeted. Its inputs are:

- $a_0,\ldots,a_{188}$;
- $c_0,\ldots,c_{94}$ and $r_0,\ldots,r_{94}$;
- $\Lambda_{32}=\operatorname{lcm}(1,3,\ldots,187)$;
- the two original $64\times64$ matrices for $H_{32}(0)$ and $H_{32}(1)$.

The verifiable outputs are the exact coefficients, their gcd with a Bézout certificate, the primitive pair, verification of


$$
D_{31}E_{32}\mid G_{32},
$$


and


$$
W_{32}=
\frac{G_{32}}{\gcd(G_{32},B_{32})}.
$$


An output $W_{32}>1$ would falsify the all-$k$ envelope. An output $W_{32}=1$ would establish only that finite instance, not an infinite content theorem and not an original-index instance.

---

## Final assessment

There is no substantive mathematical gap in the assigned A5 analytic claims or A3’s proved column-factor claims. The necessary corrections are matters of proof status and current strength:

- the best accepted raw whole-error scale is leading $4$, not leading $2$;
- A3’s content envelope is a conjecture;
- its updated conditional divergence scale is leading $3$;
- convergent primitive rationals do not by themselves prove irrationality.

The new evaluated rational-error theorem substantially sharpens the analytic approximation rate while preserving the complete moments, finite boundaries, same integer polynomial, actual primitive denominator, and actual all-prime gcd.

The exact unresolved bottleneck is still arithmetic:


$$
\boxed{
\ell_k=\frac{|H_k(e+\pi)|}{G_k}
\quad\text{on one infinite set of original indices.}
}
$$


Neither primitive decay nor primitive divergence for the compact family has been established unconditionally. Consequently, **the rationality or irrationality of $e+\pi$ remains unresolved.**
