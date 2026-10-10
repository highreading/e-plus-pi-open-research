> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Corrected matched $b=3$ exclusion, with the whole endpoint error retained

The erroneous $n=1$ entry must be withdrawn. The definitions give


$$
(\sigma_1,\chi_1,\kappa_1,V_1)=(-16,-44,-40,432),
$$


and hence


$$
(\sigma_1,\chi_1,\kappa_1,V_1)\equiv(5,5,2,5)\pmod 7.
$$


In particular, the corrected $7$-adic unit certificate survives.

I find no fatal obstruction in the all-prime-power transfer or in the complete endpoint quotient. The transfer proof does, however, need an explicit treatment of unequal finite supports. Below I supply that treatment, verify the $p=3$ boundary, and retain both the contraction content and the final endpoint gcd.

The resulting conclusion is:

> **Matched $b=3$ exclusion.** For the endpoint-matched cofactor family of degree caps $(n,3,n)$, let
> 

$$
> c_n=-\frac{A_n(1)}{B_n(1)}=\frac{p_n}{q_n},
> \qquad \gcd(p_n,q_n)=1,\quad q_n>0.
>
$$


> Using the explicit eight-prime certificate supplied in the question, the corrected arithmetic below proves
> 

$$
> \liminf_{n\to\infty}
> \frac1n\log\bigl|q_n(e+\pi)-p_n\bigr|
> >\frac{401}{20000}.
>
$$


> In particular,
> 

$$
> \bigl|q_n(e+\pi)-p_n\bigr|>\exp(n/50)
>
$$


> for every sufficiently large integer $n$. Thus **no unbounded-index subsequence of this matched cofactor family yields shrinking primitive endpoint forms**.

This is the matched $b=3$ family, not the previously excluded fixed-$b=3$ Gram center. The conclusion uses the supplied fixed-$b$ analytic theorem for eventual normality and the whole evaluated error. It does not decide the irrationality of $e+\pi$.

The finite portion is the coordinator’s explicitly supplied certificate, not a new computation performed by me. I give a direct exact verifier below and independently derive the identities that give the certificate its all-index force.

---

## 1. Scalar identities and the corrected small control

Put


$$
\phi(z)=1-z+\frac{z^2}{2},\qquad
H_n(x)=n![z^n]e^{xz}\phi(z)^n,
\qquad
\mathscr F_n(x)=x^nH_n(x),
$$


and define


$$
h_n=H_n(1),\quad u_n=H_n'(1),\quad v_n=H_n''(1).
$$


For a polynomial $P$, write


$$
I(P)=\int_1^\infty e^{1-x}P(x)\,dx
     =\sum_{r\ge0}P^{(r)}(1).
$$


Thus


$$
\mathcal A_n=I(\mathscr F_n),\qquad
\mathcal M_n=I(x\mathscr F_n)
$$


are integers.

### 1.1 Universal polynomial identities

Formal coefficient extraction, or equivalently taking the residue of a total derivative, gives


$$
H_{n+1}(x)
=(x-n-1)H_n(x)+(n+1-x)H_n'(x)+\frac{x}{2}H_n''(x).
\tag{1}
$$



For example, the residue identity


$$
0=\operatorname{Res}_{z=0}
\frac{d}{dz}\left(e^{xz}\phi(z)^{n+1}z^{-n-1}\right)
$$


gives (1) directly.

A second total-derivative identity gives


$$
xH_n'''(x)+(n+2-2x)H_n''(x)
       +2(x-1)H_n'(x)-2nH_n(x)=0.
\tag{2}
$$


Indeed, the relevant total derivative is that of


$$
2z\phi(z)e^{xz}\phi(z)^nz^{-n-1}.
$$



Differentiating (2) $d$ times and evaluating at $1$ yields the useful jet recurrence


$$
H_n^{(d+3)}(1)
=-(n+d)H_n^{(d+2)}(1)
  +2dH_n^{(d+1)}(1)+2(n-d)H_n^{(d)}(1).
\tag{3}
$$


In particular,


$$
H_n'''(1)=2nh_n-nv_n,
$$




$$
H_n''''(1)=-(n+1)H_n'''(1)+2v_n+2(n-1)u_n.
$$



Equations (1)–(3) prove the first three rows of the five-state recurrence. Multiplying (1) by $x^{n+1}$ also gives


$$
\mathscr F_{n+1}
=\frac{x^2}{2}\mathscr F_n''
+x(1-x)\mathscr F_n'
+\left(x^2-x-\frac{n(n+1)}2\right)\mathscr F_n.
\tag{4}
$$


Integration by parts, using


$$
I(P')=I(P)-P(1),
$$


then gives the remaining two rows.

The resulting recurrence, with $t=n+1$, is


$$
\begin{aligned}
h_{n+1}&=-nh_n+nu_n+\frac{v_n}{2},\\
u_{n+1}&=t\left(h_n-u_n+\frac{v_n}{2}\right),\\
v_{n+1}&=t\left(nh_n+u_n-\frac{n+2}{2}v_n\right),\\
\mathcal A_{n+1}&=t\mathcal M_n+h_n-u_n+\frac{v_n}{2},\\
\mathcal M_{n+1}
&=t^3\mathcal A_n+t(2n+3)\mathcal M_n\\
&\quad +(n^2+3n+4)h_n-(n+3)u_n+(n+2)v_n.
\end{aligned}
\tag{5}
$$


Its initial state is


$$
(h_0,u_0,v_0,\mathcal A_0,\mathcal M_0)=(1,0,0,1,2).
$$



The adjacent complete factorial contraction is


$$
\mathcal B_n=\mathcal M_n+h_n-u_n.
\tag{6}
$$


To see this without dividing modulo $n+1$, observe that


$$
\mathcal B_n
=\frac{I(\mathscr F_{n+1}')}{n+1}
=\frac{\mathcal A_{n+1}-h_{n+1}}{n+1},
$$


and subtract the first recurrence in (5) from the fourth.

These are polynomial identities, not conclusions extrapolated from the $n=0,\ldots,12$ controls.

### 1.2 Exact derivative rows

Let


$$
E_{k,r}=\mathscr F_k^{(r)}(1).
$$


For $b=3$, take the integer high rows


$$
r=(E_{n+1,0},E_{n+1,1},E_{n+1,2},E_{n+1,3}),
$$




$$
s=\frac1{n+2}
(E_{n+2,1},E_{n+2,2},E_{n+2,3},E_{n+2,4}).
\tag{7}
$$


The second division is an exact integer division.

Here is also a way to verify the high-row formulas without relying on a degree scan. Set


$$
\eta_{k,d}=\frac{H_k^{(d)}(1)}k,\qquad d\ge1.
$$


The first two normalized derivatives are obtained from the state at $k-1$ using (5); then


$$
\eta_{k,3}=2h_k-k\eta_{k,2},
$$


and, for $d\ge1$,


$$
\eta_{k,d+3}
=-(k+d)\eta_{k,d+2}
 +2d\eta_{k,d+1}+2(k-d)\eta_{k,d}.
\tag{8}
$$


For $r\ge1$,


$$
\frac{E_{k,r}}k
=\eta_{k,r}
+\sum_{a=1}^r
 \binom ra(k-1)_{a-1}H_k^{(r-a)}(1).
\tag{9}
$$


There is no inverse of $k$ on the right.

Equations (5), (8), and (9) express both rows in (7) polynomially over $\mathbb Z[1/2]$ in $n$ and the five-state coordinates. They therefore verify the supplied high-row formulas at every index, including indices where an odd prime divides $n+1$ or $n+2$.

The underlying integrality follows directly from the coefficients of $H_k$: $H_k\in\mathbb Z[x]$ and $H_k'/k\in\mathbb Z[x]$. The latter implies $k\mid E_{k,r}$ for every $r\ge1$, as in the supplied general cofactor reduction.

Define the cumulative rows


$$
\mathbf p_j=\sum_{i=1}^j E_{n,i-1},
\qquad
\mathbf u_j=\sum_{i=1}^j\frac{E_{n+1,i}}{n+1},
\qquad 0\le j\le3,
\tag{10}
$$


with empty sums zero, and let $\mathbf e=(1,1,1,1)$. Set


$$
\sigma=-\det[r;s;\mathbf e;\mathbf u],\qquad
\chi=-\det[r;s;\mathbf e;\mathbf p],\qquad
\kappa=\det[r;s;\mathbf u;\mathbf p].
\tag{11}
$$



### 1.3 Independent correction at $n=1$

The defining polynomials give


$$
H_1=x-1,\qquad H_2=x^2-4x+4,
\qquad H_3=x^3-9x^2+27x-24.
$$


Consequently


$$
(h_1,u_1,v_1,\mathcal A_1,\mathcal M_1)=(0,1,0,3,11),
\qquad \mathcal B_1=10,
$$


and


$$
r=(1,0,-4,0),\qquad s=(-1,10,28,-24),
$$




$$
\mathbf u=(0,0,-2,-2),\qquad
\mathbf p=(0,0,1,3).
$$


The three determinants in (11) are therefore


$$
\sigma_1=-16,\qquad \chi_1=-44,\qquad \kappa_1=-40.
$$


Hence


$$
V_1=\sigma_1\mathcal A_1-\chi_1\mathcal B_1-\kappa_1
=-48+440+40=432.
\tag{12}
$$



This identifies the first precise error in the earlier report: its $n=1$ determinant contraction was wrong. The five-state recurrence itself was not the source of that error.

---

## 2. Exact endpoint quotient and all contents

The actual approximation domain is $n\ge3$. Scalar seeds below $3$ are used only for congruence transfer.

Write


$$
L_k(y)=2^ki^kP_k(-i(2y-1)),\qquad \mathsf P_k=L_k(1),
$$


and


$$
w_k=\mathcal L\!\left(\frac{L_k(y)-\mathsf P_k}{y-1}\right).
$$


The supplied contiguous endpoint identities give


$$
G_n=\mathsf P_nw_{n+1}-\mathsf P_{n+1}w_n
=\frac{(-1)^n2^{2n+3}}{n+1}.
\tag{13}
$$



Put $t=n+1$, $f_n=2^n/(n!)^2$, and define the **raw** scalars


$$
\begin{aligned}
D_n&=t\mathsf P_{n+1}\chi_n-2\mathsf P_n\sigma_n,\\
Q_n&=2w_n\sigma_n-tw_{n+1}\chi_n,\\
V_n&=\sigma_n\mathcal A_n-\chi_n\mathcal B_n-\kappa_n.
\end{aligned}
\tag{14}
$$


Here $D_n,V_n\in\mathbb Z$.

### 2.1 The numerator is the whole reconstructed endpoint

Let $T_P=T_0(L_n)$ and $T_U=T_0(L_{n+1})$. The cumulative-row identities give


$$
T(L_n)=T_P\mathbf e-f_n\mathbf p,
\qquad
T(L_{n+1})=T_U\mathbf e-\frac{2f_n}{t}\mathbf u,
$$


where


$$
T_P=f_n\mathcal A_n,\qquad
T_U=\frac{2f_n}{t}\mathcal B_n.
\tag{15}
$$



The endpoint rows are


$$
\boldsymbol t
=\frac{\mathsf P_nT(L_{n+1})-\mathsf P_{n+1}T(L_n)}{G_n},
$$




$$
\boldsymbol x
=\frac{w_nT(L_{n+1})-w_{n+1}T(L_n)}{G_n}.
\tag{16}
$$


These are the actual reconstructed elementary endpoints, not isolated factorial tails.

Expanding the endpoint determinants with (11), (15), and (16) yields


$$
\frac{X_n}{Y_n}
=
\frac{Q_n+2f_nV_n}{D_n},
\qquad D_n\ne0.
\tag{17}
$$


In particular,


$$
Q_n+2f_nV_n
=2(w_n+T_P)\sigma_n
 -t(w_{n+1}+T_U)\chi_n-2f_n\kappa_n.
\tag{18}
$$


The $-\kappa_n$ contribution has not been dropped.

For the monic high-row convention, the common endpoint scale is


$$
\rho_n=\frac{n+2}{(2n+2)!(2n+4)!},
$$


and


$$
Y_n=\rho_n\frac{f_n}{tG_n}D_n,\qquad
X_n=\rho_n\frac{f_n}{tG_n}(Q_n+2f_nV_n).
\tag{19}
$$


Thus $Y_n\ne0$ is equivalent to $D_n\ne0$.

### 2.2 Row content, maximal-minor content, and contraction content

Let $c_1,c_2$ be the contents of the two rows in (7). After dividing these out, let $\mu_n$ be the gcd of the six maximal minors of the normalized high block. After dividing those minors by $\mu_n$, let $d_n$ be the gcd of the three resulting contractions.

On $D_n\ne0$, all these contents are defined and positive. Directly from the multilinearity of the contractions,


$$
\delta_n:=\gcd(|\sigma_n|,|\chi_n|,|\kappa_n|)
=c_1c_2\mu_nd_n.
\tag{20}
$$


Therefore define


$$
(\sigma_n^*,\chi_n^*,\kappa_n^*)
=\delta_n^{-1}(\sigma_n,\chi_n,\kappa_n),
$$


and define $D_n^*,Q_n^*,V_n^*$ by (14). Then


$$
\frac{X_n}{Y_n}
=
\frac{Q_n^*+\dfrac{2^{n+1}}{(n!)^2}V_n^*}{D_n^*}.
\tag{21}
$$



This removes all the stated high-row and contraction contents. It does **not** identify or discard the final endpoint gcd.

### 2.3 The actual primitive denominator

The moment formula


$$
\mathcal L(y^j)=
\frac{(1+i)^{j+1}-(1-i)^{j+1}}
{i\,2^j(j+1)}
$$


shows that


$$
2^n\operatorname{lcm}(1,\ldots,n+1)
$$


clears both $w_n$ and $w_{n+1}$. Consequently


$$
\lambda_n=
\operatorname{lcm}\!\left((n!)^2,\,
2^n\operatorname{lcm}(1,\ldots,n+1)\right)
\tag{22}
$$


is a valid clearer.

Set


$$
N_n=\lambda_n
\left(Q_n^*+\frac{2^{n+1}}{(n!)^2}V_n^*\right),
\qquad
Z_n=\lambda_nD_n^*,
$$




$$
g_n=\gcd(|N_n|,|Z_n|).
\tag{23}
$$


Then, on $D_n\ne0$,


$$
c_n=-\frac{X_n}{Y_n}=\frac{p_n}{q_n},
$$


where exactly


$$
q_n=\frac{|Z_n|}{g_n},
\qquad
p_n=-\operatorname{sign}(Z_n)\frac{N_n}{g_n}.
\tag{24}
$$


This is the actual primitive rational denominator, including the final endpoint cancellation.

---

## 3. All-prime-power transfer, including unequal supports

The following is an all-index theorem, not a consequence of testing a finite number of canonical degrees.

> **Transfer lemma.** Let $p$ be odd and $a\ge1$. If $m,n\ge0$ and
> 

$$
> m\equiv n\pmod{p^a},
>
$$


> then the five-state coordinates at $m,n$ are congruent modulo $p^a$. The same holds for
> 

$$
> \mathcal B,\ \sigma,\ \chi,\ \kappa,\ V.
>
$$



### 3.1 Coefficient transfer

Let


$$
a_s(n)=[z^s]\phi(z)^n.
$$


For $m\ge n$ with $p^a\mid m-n$, expansion of


$$
\phi(z)^{m-n}=(1+(\phi(z)-1))^{m-n}
$$


shows, for $s\ge1$, that


$$
v_p(a_s(m)-a_s(n))
\ge a-\lfloor\log_p s\rfloor.
\tag{25}
$$


Indeed, a contributing binomial coefficient has index $1\le j\le s$, and


$$
\binom{m-n}{j}=\frac{m-n}{j}\binom{m-n-1}{j-1}.
$$



For every integer $x$,


$$
v_p((x)_s)\ge v_p(s!)\ge\lfloor\log_p s\rfloor.
\tag{26}
$$


Also $(x)_s$ is an integer polynomial, so its values at $m,n$ are congruent modulo $p^a$.

It follows term by term that


$$
H_n^{(d)}(1)=\sum_{s\ge0}(n)_{s+d}a_s(n)
\tag{27}
$$


transfers for $d=0,1,2$. In (27), the terms are zero once $s+d>n$; comparing both sides over one common range therefore causes no support problem.

### 3.2 A common-index formula for the integral contractions

Write


$$
D_j=j!\sum_{r=0}^j\frac1{r!}
=\sum_{r=0}^j(j)_r\qquad(j\ge0).
$$


Define, for every $x\in\mathbb Z_p$,


$$
\mathfrak D(x)=\sum_{r\ge0}(x)_r.
\tag{28}
$$


This series converges uniformly because


$$
v_p((x)_r)\ge v_p(r!)\longrightarrow\infty.
$$


Each finite partial sum is an integer polynomial, so its limit is $1$-Lipschitz:


$$
x\equiv y\pmod{p^a}
\quad\Longrightarrow\quad
\mathfrak D(x)\equiv\mathfrak D(y)\pmod{p^a}.
\tag{29}
$$


For nonnegative integers $j$, it equals $D_j$.

Now use


$$
\mathcal A_n
=\sum_{s\ge0}(n)_s a_s(n)\mathfrak D(2n-s),
\tag{30}
$$




$$
\mathcal M_n
=\sum_{s\ge0}(n)_s a_s(n)\mathfrak D(2n+1-s).
\tag{31}
$$


These are finite sums in value: $(n)_s=0$ for $s>n$.

Equations (30)–(31) are the important support repair. When comparing $m$ and $n$, a term may lie beyond one polynomial’s original support, and its displayed $\mathfrak D$-argument may be negative. Formula (28) defines that argument legitimately, while the falling-factorial weight makes the term zero where it should be zero.

Apply (25)–(26) to the product $(n)_s a_s(n)$, and (29) to the $\mathfrak D$-factor. Every term transfers modulo $p^a$, proving transfer of both integral contractions. Equation (6) then proves transfer of $\mathcal B_n$.

### 3.3 The alternative $\mathcal B$-sum and the $p=3$ boundary

The draft also used


$$
\mathcal B_n
=2D_{2n+1}
+\sum_{s\ge1}
(n)_{s-1}(2n+2-s)a_s(n+1)D_{2n+1-s}.
\tag{32}
$$


Its weight


$$
W_s(x)=(x)_{s-1}(2x+2-s)
$$


does satisfy


$$
v_p(W_s(x))\ge\lfloor\log_p s\rfloor
\tag{33}
$$


for every odd $p$.

Here are all boundary cases:

* If $s<p$, the required bound is zero.
* If $s=p$ and $(x)_{p-1}$ is a unit, then necessarily
  $x\equiv-1\pmod p$, so $2x+2-p\equiv0\pmod p$.
* If $s\ge p+1$ and $\lfloor\log_p s\rfloor=1$, then $(s-1)!$ already contains $p$.
* If $k=\lfloor\log_p s\rfloor\ge2$, then
  

$$
v_p((s-1)!)\ge p^{k-1}-1\ge k.
$$


  The smallest boundary is $p=3,k=2$, where the last inequality is
  

$$
3-1=2.
$$


  Thus it is valid, including that boundary.

Using $\mathfrak D$ in (32) resolves its support issue in exactly the same way. The alternative proof is therefore sound too, although (30)–(31) give a shorter route to transfer of the five-state vector.

### 3.4 Transfer of the raw determinant contractions

Equations (5), (8), and (9) show that the rows defining (11) are polynomial expressions over $\mathbb Z[1/2]$ in $n$ and the five-state vector. Hence the raw quantities


$$
\sigma_n,\chi_n,\kappa_n,V_n
$$


transfer modulo every $p^a$, for odd $p$.

No periodicity of the content-normalized quantities is asserted. In particular, this proof does not silently assume that $\delta_n$ is a polynomial or is itself $1$-Lipschitz.

---

## 4. The corrected finite certificate

The corrected mod-$7$ table is


$$
\begin{array}{c|rrrrr|rrrr}
r&h&u&v&\mathcal A&\mathcal M&
\sigma&\chi&\kappa&V\\ \hline
0&1&0&0&1&2&0&5&0&6\\
1&0&1&0&3&4&5&5&2&5\\
2&1&5&2&0&4&6&5&5&2\\
3&2&5&2&2&4&1&2&1&6\\
4&3&6&3&0&2&0&2&1&1\\
5&3&3&3&5&0&2&4&5&5\\
6&5&2&3&5&5&6&3&5&1
\end{array}
\tag{34}
$$


Thus its $V$-vector is


$$
(6,5,2,6,1,5,1),
$$


not the old vector with second entry $4$.

Only the following eight primes are needed:


$$
\mathcal P=\{7,19,31,61,71,73,83,101\}.
\tag{35}
$$


Their supplied complete seed data contain $446$ rows. A compact summary is


$$
\begin{array}{c|r|rrrr|c}
p&\text{rows}&V_0&V_1&V_2&V_{p-1}&
\{r:V_r=0\pmod p\}\\ \hline
7&7&6&5&2&1&\varnothing\\
19&19&10&14&11&18&\varnothing\\
31&31&17&29&17&30&\varnothing\\
61&61&48&5&6&40&\varnothing\\
71&71&48&6&63&34&\varnothing\\
73&73&48&67&22&33&\varnothing\\
83&83&48&17&40&28&\varnothing\\
101&101&48&28&3&65&\varnothing
\end{array}
\tag{36}
$$


This summary does not replace the supplied full rows.

A direct exact verifier, independent of the five-state implementation, is as follows:

1. Construct $H_k$ from its defining coefficient formula for $0\le k\le102$.
2. Construct $\mathscr F_k=x^kH_k$.
3. Compute every needed $E_{k,r}$ by exact polynomial differentiation.
4. Compute $I(x^j)=D_j$ using
   

$$
D_0=1,\qquad D_j=jD_{j-1}+1.
$$


5. For each of the $446$ residue rows, reconstruct the state, the rows (7), (10), the three determinants (11), and $V$.
6. Perform the divisions by $n+1$ and $n+2$ **over the integers before reduction modulo $p$**.
7. Compare with every supplied seed entry and test $V\not\equiv0\pmod p$.

This specifies the finite certificate entirely by exact operations. I do not claim a new execution of that verifier. The $n=1$ control above is an explicit independent reconstruction, and the universal row and transfer identities have been derived rather than inferred from the finite controls.

The finite certificate, together with the proved transfer lemma, yields


$$
v_p(V_n)=0
\qquad(n\ge0,\ p\in\mathcal P).
\tag{37}
$$


This is the all-index conclusion; the finite lists alone would not give it.

Since $\delta_n\mid V_n$, (37) also proves


$$
v_p(\delta_n)=0,\qquad
v_p(V_n^*)=0,\qquad
v_p(D_n)=v_p(D_n^*)
\tag{38}
$$


on the quotient domain.

---

## 5. Strict separation in the complete numerator

Fix $p\in\mathcal P$, and put


$$
F=v_p(n!),\qquad
\ell=\lfloor\log_p(n+1)\rfloor.
$$


The moment denominators imply


$$
v_p(Q_n)\ge-\ell.
\tag{39}
$$


By (37), the factorial term in the complete numerator has valuation


$$
v_p\left(\frac{2^{n+1}}{(n!)^2}V_n\right)=-2F.
\tag{40}
$$



For every odd prime $p$ and every $n\ge p$,


$$
2v_p(n!)>\lfloor\log_p(n+1)\rfloor.
\tag{41}
$$


For completeness, if the right side is $1$, then $F\ge1$. If it is $k\ge2$, then $n\ge p^k-1$, so


$$
F\ge p^{k-1}-1,\qquad 2(p^{k-1}-1)>k.
$$



Thus, for $n\ge p$,


$$
v_p\left(Q_n+\frac{2^{n+1}}{(n!)^2}V_n\right)
=-2v_p(n!).
\tag{42}
$$


The two terms have strictly different valuations. There is no equal-depth cancellation, and the complete rational numerator is nonzero.

Applying the exact rational quotient valuation to (17), including its final reduction, gives


$$
v_p(q_n)
=2v_p(n!)+v_p(D_n)
=2v_p(n!)+v_p(D_n^*)
\ge2v_p(n!).
\tag{43}
$$


This is valid whenever


$$
n\ge p,\qquad D_n\ne0.
$$



Therefore the common effective arithmetic threshold for all eight primes is simply


$$
\boxed{n\ge101,\quad D_n\ne0.}
\tag{44}
$$


No analytic normality cutoff has been inserted into this statement.

In particular,


$$
q_n\ge\prod_{p\in\mathcal P}p^{2v_p(n!)}.
\tag{45}
$$


Using Legendre’s formula and the elementary digit-sum bound,


$$
q_n\ge
\frac{\exp(Wn)}{n^{16}\left(\prod_{p\in\mathcal P}p\right)^2},
\qquad
W=\sum_{p\in\mathcal P}\frac{2\log p}{p-1},
\tag{46}
$$


throughout the domain (44).

---

## 6. A strict rational rate certificate for the eight primes

The rate $2.19816\ldots$ in the supplied JSON belongs to the larger thirteen-prime set. It must not be attributed to the eight-prime certificate.

For the eight primes, a smaller exact certificate suffices. Define


$$
T_8(x)=2\sum_{j=0}^{7}\frac{x^{2j+1}}{2j+1},
\qquad
R_8(x)=\frac{2x^{17}}{17(1-x^2)}.
$$


For $0<x<1$,


$$
T_8(x)
<
\log\frac{1+x}{1-x}
<
T_8(x)+R_8(x).
\tag{47}
$$



Write $p=2^k(p/2^k)$. The following table supplies rational lower bounds for $\log p$; each follows by substituting its rational $x=(p-2^k)/(p+2^k)$ into


$$
kT_8(1/3)+T_8(x).
$$




$$
\begin{array}{c|c|c|c}
p&k&x&\text{strict lower bound for }\log p\\ \hline
7&2&3/11&194591/100000\\
19&4&3/35&294443/100000\\
31&4&15/47&343398/100000\\
61&5&29/93&411087/100000\\
71&6&7/135&426267/100000\\
73&6&9/137&429045/100000\\
83&6&19/147&441884/100000\\
101&6&37/165&461512/100000
\end{array}
\tag{48}
$$


These are finite rational inequalities, so no floating-point logarithm evaluation is needed.

Their weighted sum gives


$$
\begin{aligned}
W>{}&
\frac{194591}{300000}
+\frac{294443}{900000}
+\frac{343398}{1500000}
+\frac{411087}{3000000}\\
&+\frac{426267}{3500000}
+\frac{429045}{3600000}
+\frac{441884}{4100000}
+\frac{461512}{5000000}\\
>{}&\frac{4457}{2500}.
\end{aligned}
\tag{49}
$$



For the analytic rate


$$
\tau=2\log(1+\sqrt2),
$$


use


$$
\sqrt2<\frac{1414214}{1000000}.
$$


Then (47), with $x=1/3$ and $x=207107/2207107$, gives the rational upper certificate


$$
\begin{aligned}
\tau
<&\ 2\left[
T_8(1/3)+R_8(1/3)\right.\\
&\left.\hspace{15mm}
+T_8(207107/2207107)+R_8(207107/2207107)
\right]\\
<&\frac{7051}{4000}.
\end{aligned}
\tag{50}
$$


Consequently


$$
\boxed{
W-\tau>
\frac{4457}{2500}-\frac{7051}{4000}
=\frac{401}{20000}>\frac1{50}.
}
\tag{51}
$$



---

## 7. Whole-error nonvanishing and exclusion of the entire eventual family

Here the analytic input is the supplied **fixed-exponential-degree error theorem**, used at the fixed value $b=3$. Its stated conclusion is that, for all sufficiently large $n$,

* the projective solution is unique;
* $Y_n\ne0$, equivalently $D_n\ne0$;
* the entire normalized evaluated error is nonzero; and
* with $\epsilon_n>0$,
  

$$
\frac{(-1)^nR_n(1)}{Y_n\epsilon_n}
  \longrightarrow(\sqrt2-1)^3,
  \qquad
  \frac{\log\epsilon_n}{n}\longrightarrow-\tau.
  \tag{52}
$$



This is an inherited analytic theorem, with the supplied review status. I do not claim a new independent analytic proof or an effective normality cutoff.

Because endpoint matching gives $B_n(1)=C_n(1)=Y_n$ and $F(1)=\pi$,


$$
\frac{R_n(1)}{Y_n}
=\frac{X_n}{Y_n}+e+\pi
=e+\pi-c_n.
\tag{53}
$$


Thus (52) is a statement about the **whole evaluated error**, not either tail separately.

Combining (46), (51), and (52),


$$
\begin{aligned}
\log|q_n(e+\pi)-p_n|
&=\log q_n+\log|e+\pi-c_n|\\
&\ge (W-\tau)n-16\log n
 -2\sum_{p\in\mathcal P}\log p+o(n).
\end{aligned}
\tag{54}
$$


Hence


$$
\liminf_{n\to\infty}
\frac{\log|q_n(e+\pi)-p_n|}{n}
\ge W-\tau>\frac{401}{20000}.
\tag{55}
$$


In particular, the form is eventually nonzero and exceeds $\exp(n/50)$ in absolute value.

This also controls every integral representative of the same eventual projective solution. If an integral matched triple has endpoints $X,Y$, then


$$
-\frac XY=\frac{p_n}{q_n}
$$


implies $Y=kq_n$, $X=-kp_n$ for a nonzero integer $k$. Its evaluated remainder therefore has absolute value


$$
|k|\cdot|q_n(e+\pi)-p_n|
\ge |q_n(e+\pi)-p_n|.
\tag{56}
$$


Thus full coefficient primitiveness cannot restore shrinking after the actual endpoint denominator has been used.

The exclusion is consequently for **all sufficiently large indices and every unbounded-index subsequence**, not merely for selected congruence classes. It does not address arbitrary new inter-index combinations of these forms.

---

## 8. First unexcluded fixed matched allocation: $b=4$

After this exclusion, the first fixed matched allocation not excluded by the supplied record is


$$
\boxed{(n,4,n),\qquad \text{order }2n+5,\qquad n\ge4.}
$$


The already excluded Gram centers do not settle this matched allocation.

There is a bounded next arithmetic lemma available without constructing a larger scalar state.

### 8.1 A five-state transfer interface for matched $b=4$

Use three integer high rows of length five:


$$
R_1=(E_{n+1,j})_{j=0}^{4},
$$




$$
R_2=\left(\frac{E_{n+2,j+1}}{n+2}\right)_{j=0}^{4},
\qquad
R_3=\left(\frac{E_{n+3,j+2}}{n+3}\right)_{j=0}^{4}.
\tag{57}
$$


Define $\mathbf p,\mathbf u$ as in (10), now for $0\le j\le4$, and set


$$
\begin{aligned}
\sigma^{(4)}_n&=-\det[R_1;R_2;R_3;\mathbf e;\mathbf u],\\
\chi^{(4)}_n&=-\det[R_1;R_2;R_3;\mathbf e;\mathbf p],\\
\kappa^{(4)}_n&=\det[R_1;R_2;R_3;\mathbf u;\mathbf p],\\
V^{(4)}_n&=\sigma^{(4)}_n\mathcal A_n
-\chi^{(4)}_n\mathcal B_n-\kappa^{(4)}_n.
\end{aligned}
\tag{58}
$$



The maximum required derivative order is $6$. Equations (3), (8), and (9) express every entry in (57)–(58) polynomially over $\mathbb Z[1/2]$ in $n$ and the same five-state coordinates.

Therefore the proved transfer lemma immediately gives


$$
\boxed{
m\equiv n\pmod{p^a}
\Longrightarrow
V^{(4)}_m\equiv V^{(4)}_n\pmod{p^a}
}
\tag{59}
$$


for every odd $p$, every $a\ge1$, and all $m,n\ge0$. The same holds for the three raw contractions.

This is a proved interface. It is not yet a denominator-growth estimate: the relevant finite unit or bounded-valuation certificates for $V^{(4)}$ remain to be established.

### 8.2 A new exact boundary seed

At the scalar seed $n=0$,


$$
R_1=(0,1,2,0,0),
$$




$$
R_2=(0,-2,0,12,0),
$$




$$
R_3=(10,28,-24,-120,240),
$$


and


$$
\mathbf u=(0,1,3,3,3),\qquad
\mathbf p=(0,1,1,1,1).
$$


Direct determinants give


$$
\boxed{
(\sigma^{(4)}_0,\chi^{(4)}_0,\kappa^{(4)}_0)
=(960,-3360,-480).
}
\tag{60}
$$


Since $\mathcal A_0=1$ and $\mathcal B_0=3$,


$$
\boxed{V^{(4)}_0=11520.}
\tag{61}
$$


Here


$$
\delta^{(4)}_0=480,\qquad
(\sigma^{(4)*}_0,\chi^{(4)*}_0,\kappa^{(4)*}_0)
=(2,-7,-1),\qquad V^{(4)*}_0=24.
\tag{62}
$$


This is only a scalar congruence seed; $n=0$ is not an admissible $(n,4,n)$ approximant.

The general supplied endpoint reduction applies to (58), retaining its final gcd and the same complete-numerator separation gate. Thus an all-index unit certificate for enough primes would have immediate arithmetic force for this next family.

---

## Research deliverables

### (1) New result and proof status

* **False claim corrected:** the earlier $n=1$ contractions and mod-$7$ row were wrong. Equations (12) and (34) are the corrected values.
* **Paper proof supplied:** the all-prime-power transfer is valid, including unequal finite supports and the $p=3$ boundary. The proof transfers raw contractions, not an unjustified content-normalized substitute.
* **Complete quotient retained:** equations (21)–(24) preserve all stated contents and the final endpoint gcd.
* **Certificate-backed exclusion:** the eight supplied unit-prime certificates imply factorial-depth divisibility of the actual denominator for $n\ge101$, on $D_n\ne0$. Together with the inherited fixed-$b=3$ whole-error theorem, they exclude every eventual matched $b=3$ cofactor subsequence from primitive shrinking. The strict rate margin is rationally certified in (51).
* **New bounded follow-on lemma:** matched $b=4$ needs no larger scalar state for its raw arithmetic transfer; (59) is proved, with the exact seed (60)–(62).

No new independent execution of the supplied $446$-row certificate is claimed.

### (2) Exact remaining bottleneck

The irrationality of $e+\pi$ remains unresolved.

For the first unexcluded fixed matched allocation, $b=4$, the next bottleneck is the actual numerator contraction $V^{(4)}_n$, its possible shared content, and—where strict separation fails—the whole expression


$$
V^{(4)}_n+\frac{(n!)^2}{2^{n+1}}Q^{(4)}_n.
$$


The fixed-$b$ analytic theorem already supplies eventual normality and the whole-error rate for $b=4$; it supplies no endpoint-gcd estimate.

### (3) Bounded exact computation request

If the coordinator elects to proceed, request **exactly the same eight primes**


$$
\{7,19,31,61,71,73,83,101\},
$$


but now for the **matched $b=4$** contractions (57)–(58), at every $0\le r<p$: exactly **446 residue rows**, with no prime-list extension.

**Expected verifiable output:**

1. The full vectors
   

$$
(\sigma^{(4)}_r,\chi^{(4)}_r,\kappa^{(4)}_r,V^{(4)}_r)\pmod p.
$$


2. The exact zero set of $V^{(4)}_r\bmod p$.
3. The joint-zero set of the three contractions modulo $p$, kept separate from the $V^{(4)}$-zero set.
4. Confirmation of the exact seed
   

$$
(960,-3360,-480,11520)
$$


   before modular reduction.
5. For the primes with empty $V^{(4)}$-zero set, the resulting rationally bounded aggregate rate.

A raw scalar zero must not be promoted to a statement about the primitive numerator without analyzing the contraction content. Conversely, an empty raw zero set has an immediate all-index consequence through (59), with no extrapolation from finite degrees.
