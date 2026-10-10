> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5 continuation: an infinite moving-prime theorem for the actual factorial norm content

## Status and scope

I do **not** obtain a proof or disproof of the irrationality of $S=e+\pi$.

The substantive arithmetic advance is an **exact moving-prime valuation theorem**, not another formula for an unspecified gcd. On an explicitly defined infinite proportional subfamily


$$
n=p-1,\qquad b=\frac{p-1}{2001},\qquad m=1,
$$


with $p$ in a fixed, explicitly specified arithmetic progression, I prove


$$
\boxed{v_p\!\left(\gcd(T,V_0)\right)=2}
$$


for the factorial metric obtained directly from the complete-remainder source. In fact,


$$
\boxed{v_p(T)=2.}
$$



The proof uses the **actual Rodrigues high rows**, their reduction modulo $p$ and $p^2$, and the restriction of the **actual metric row** $z_0^T\Omega$. It does not transfer a fixed-$b$ seed.

There is a Pochhammer-convention ambiguity in the supplied proportional notes. If their metric is instead intended to use **rising** factorials, I prove on the same subfamily the corresponding stronger local assertion


$$
\boxed{p\nmid T,\qquad p\nmid\gcd(T,V_0).}
$$


I distinguish these metrics below rather than silently equating them.

These are unconditional arithmetic statements about the indicated integer high-row kernel. Their application to the actual endpoint-normalized Gram center is valid at every finite normal index. Eventual normality and the full signed error on this subfamily remain at the supplied proportional theorem’s **author/dependency status**.

I also verify that A4’s recursive congruence steering extends to **every finite jet block**, without $N<2m$. The extension is a triangular polynomial automorphism, not a linear Smith-form statement, and provides no analytic norm control.

---

## 1. A metric-convention issue that must be made explicit

The weights in `MULTIROW_REMAINDER_RESEARCH.md` are explicitly


$$
w_j=\frac{(\ell-b)!}{(\ell-j)!},
\qquad \ell=n+m+1.
$$


After dividing every weight by $w_0$, the same Gram center therefore uses


$$
\boxed{\omega_j^-=\frac{\ell!}{(\ell-j)!}
=\ell(\ell-1)\cdots(\ell-j+1).}
\tag{1.1}
$$


Thus these are **falling factorials**.

The proportional notes write $(\ell)_j$ without resolving the convention in the displayed metric definition. If that symbol is intended as a rising factorial,


$$
\omega_j^+=\ell(\ell+1)\cdots(\ell+j-1),
\tag{1.2}
$$


it is a different metric: already


$$
\omega_2^-=\ell(\ell-1),\qquad
\omega_2^+=\ell(\ell+1).
$$


Consequently, identifying (1.2) with the explicit weights of the complete-remainder source would be incorrect.

This does not affect the elementary final-gcd algebra in A5_turn0: that algebra works for either specified positive integral diagonal metric. It does affect the arithmetic calculation. I give the main calculation for (1.1), and a separate result for (1.2).

---

# Part I. An actual high-row congruence at $n=p-1$

## 2. Notation and finite domain

Let $p$ be an odd prime and assume


$$
n=p-1,\qquad b\ge5,\qquad 2b-3<p.
\tag{2.1}
$$


Use the actual integer high rows


$$
R_{lj}=E_{n+l,l+j-1},
\qquad
1\le l\le b-2,\quad 0\le j\le b.
\tag{2.2}
$$


As in the supplied Rodrigues source, write


$$
Q(z)=1-z+\frac{z^2}{2},
$$




$$
H_k(x)=k![z^k]e^{xz}Q(z)^k,
\qquad
E_{k,r}=\left.\frac{d^r}{dx^r}\bigl(x^kH_k(x)\bigr)\right|_{x=1}.
\tag{2.3}
$$


The polynomial $H_k$ has integer coefficients. For the modular arguments, it is enough that its displayed coefficients belong to $\mathbb Z_{(p)}$, since $p$ is odd.

Let


$$
\mathcal K=\ker_{\mathbb Q}R\cap\mathbb Z^{b+1}.
\tag{2.4}
$$



### Lemma 2.1 — triangular reduction of the actual high block

For every $z=(z_0,\ldots,z_b)^T\in\mathcal K$,


$$
\boxed{z_0\equiv z_1\equiv\cdots\equiv z_{b-3}\equiv0\pmod p.}
\tag{2.5}
$$


Moreover $R$ has row rank $b-2$ modulo $p$.

### Proof

Write $k=p+s$, where $0\le s\le b-3$. The coefficient formula for $H_k$ is


$$
H_k(x)=\sum_{t=0}^k k^{\underline t}[z^t]Q(z)^k\,x^{k-t}.
$$


Modulo $p$, the falling product $k^{\underline t}$ vanishes when $t>s$. For $t\le s$,


$$
k^{\underline t}\equiv s^{\underline t}\pmod p,
\qquad
[z^t]Q(z)^{p+s}\equiv[z^t]Q(z)^s\pmod p.
$$


Hence


$$
H_{p+s}(x)\equiv x^pH_s(x)\pmod p,
$$


and therefore


$$
x^{p+s}H_{p+s}(x)\equiv x^{2p}x^sH_s(x)\pmod p.
\tag{2.6}
$$



The row $l=s+1$ has derivative order $r=s+j$. By (2.1), all these orders are less than $p$. Differentiating (2.6) gives


$$
R_{s+1,j}\equiv
\left.\frac{d^{s+j}}{dx^{s+j}}\bigl(x^sH_s(x)\bigr)\right|_{x=1}
\pmod p.
\tag{2.7}
$$


The polynomial $x^sH_s(x)$ is monic of degree $2s$. Consequently,


$$
R_{s+1,j}\equiv0\pmod p\quad(j>s),
\qquad
R_{s+1,s}\equiv(2s)!\not\equiv0\pmod p.
\tag{2.8}
$$


The first $b-2$ columns thus form a triangular invertible block modulo $p$. Solving the rows successively proves (2.5). ∎

This is a growing-dimension statement: the proof works uniformly under (2.1), not with constants or residues inherited from a fixed value of $b$.

---

## 3. The two extra congruences needed for the factorial metric

Set $m=1$. Then


$$
\ell=n+m+1=p+1.
\tag{3.1}
$$



For the falling metric (1.1),


$$
\omega_0^-=1,\qquad \omega_1^-=p+1,
$$


and, for $2\le j\le b<p$,


$$
\frac{\omega_j^-}{p}
\equiv (-1)^{j-2}(j-2)!\pmod p.
\tag{3.2}
$$



The first two high rows determine the first two weighted coordinates one level further, modulo $p^2$.

### Lemma 3.1 — the first two actual rows modulo $p^2$

For $1\le r<p$,


$$
\frac{E_{p,r}}p
\equiv2(-1)^{r-1}(r-1)!\pmod p.
\tag{3.3}
$$


For $3\le r<p$,


$$
\frac{E_{p+1,r}}p
\equiv2r(-1)^{r-3}(r-3)!\pmod p.
\tag{3.4}
$$


Also


$$
E_{p,0}\equiv1,\qquad
E_{p+1,1}\equiv1,\qquad
E_{p+1,2}\equiv2\pmod p.
\tag{3.5}
$$



### Proof

In $x^pH_p(x)$, the leading term is $x^{2p}$. Every intermediate term, corresponding to $1\le t<p$, has coefficient divisible by $p^2$: one factor of $p$ comes from $p^{\underline t}$, and another from


$$
[z^t]Q(z)^p\equiv0\pmod p.
$$


The last term has coefficient divisible by $p$ and exponent $p$, so its positive derivatives of order less than $p$ are divisible by $p^2$. Thus


$$
E_{p,r}\equiv(2p)^{\underline r}\pmod{p^2},
$$


which gives (3.3).

For $x^{p+1}H_{p+1}(x)$, the first two terms are


$$
x^{2p+2}-(p+1)^2x^{2p+1}.
$$


For derivative orders $3\le r<p$, all remaining terms contribute multiples of $p^2$. In particular, the $t=2$ coefficient is a multiple of $p$, while its exponent is $2p$, supplying another factor of $p$ after differentiation. The terms with $t=p,p+1$ are handled similarly; the intervening coefficients already contain $p^2$.

It follows that


$$
\begin{aligned}
\frac{E_{p+1,r}}p
&\equiv
4(-1)^{r-3}(r-3)!
-2(-1)^{r-2}(r-2)!\\
&=2r(-1)^{r-3}(r-3)!\pmod p.
\end{aligned}
$$


The three reductions in (3.5) also follow from (2.7). ∎

---

# Part II. Exact norm-content control

## 4. A ternary model for the restriction of the actual metric row

Put


$$
s=b-2.
$$


For $z\in\mathcal K$, define its three tail coordinates modulo $p$ by


$$
d_j(z)=(-1)^{j-2}(j-2)!\,z_j\pmod p,
\qquad j=s,s+1,s+2.
\tag{4.1}
$$


Write $d(z)$ for this three-vector.

By Lemma 2.1 and (3.2), every coordinate of


$$
\operatorname{diag}(\omega_j^-)z
$$


is divisible by $p$. Lemma 3.1 gives the exact first two coordinates after this division:


$$
\frac{z_0}{p}
\equiv2\sum_{j=s}^{s+2}(j-1)d_j(z)\pmod p,
\tag{4.2}
$$




$$
\frac{(p+1)z_1}{p}
\equiv-2\sum_{j=s}^{s+2}j\,d_j(z)\pmod p.
\tag{4.3}
$$


The intermediate coordinates $2\le j\le b-3$ vanish modulo $p$ after weighted division by $p$.

Indeed, (4.2) is the first high row divided by $p$. For the second row, (3.4) gives


$$
\frac{z_0}{p}+2\frac{z_1}{p}
+2\sum_{j=s}^{s+2}(j+1)d_j(z)\equiv0\pmod p,
$$


which, together with (4.2), gives (4.3).

Define


$$
a=(s-1,s,s+1)^T,\qquad
b_*=(s,s+1,s+2)^T,
$$




$$
M_s=I_3+4aa^T+4b_*b_*^T.
\tag{4.4}
$$



### Proposition 4.1 — actual metric-row congruence

For all $z,z'\in\mathcal K$,


$$
\boxed{
\frac{z^T\Omega^-z'}{p^2}
\equiv d(z)^TM_s\,d(z')\pmod p,
}
\tag{4.5}
$$


where


$$
\Omega^-=\operatorname{diag}\bigl((\omega_j^-)^2\bigr).
$$



In particular,


$$
\frac{z^T\Omega^-z}{p^2}
\equiv
\sum_{j=s}^{s+2}d_j(z)^2
+4\left(\sum_{j=s}^{s+2}(j-1)d_j(z)\right)^2
+4\left(\sum_{j=s}^{s+2}j\,d_j(z)\right)^2
\pmod p.
\tag{4.6}
$$



This proposition is explicitly about the restriction of the actual row


$$
z^T\Omega^-.
$$


No omitted derivative row, unrelated positive form, or raw determinant is substituted for it.

---

## 5. Restriction to the primitive zero-endpoint vector

Let $z\in\mathcal K$ be primitive and satisfy


$$
\mathbf ez=\sum_{j=0}^bz_j=0.
\tag{5.1}
$$


By Lemma 2.1, $d(z)\ne0\pmod p$: otherwise every coordinate of the primitive integer vector $z$ would be divisible by $p$.

The endpoint relation (5.1), expressed in the scaled coordinates (4.1), becomes


$$
s(s-1)d_s-sd_{s+1}+d_{s+2}=0\pmod p.
\tag{5.2}
$$


Thus $d(z)$ belongs to the plane with basis


$$
v=(1,0,-s(s-1))^T,\qquad w=(0,1,s)^T.
$$



The determinant of the restricted binary form is


$$
D_-(s)=
\det
\begin{pmatrix}
v^TM_sv&v^TM_sw\\
w^TM_sv&w^TM_sw
\end{pmatrix}.
\tag{5.3}
$$


A direct Cauchy–Binet calculation gives


$$
\begin{aligned}
D_-(s)
={}&\|e_s\|^2
+4\|a\times e_s\|^2
+4\|b_*\times e_s\|^2
+16(s^2+s+1)^2,\\
e_s={}&(s(s-1),-s,1)^T.
\end{aligned}
\tag{5.4}
$$


In particular $D_-(s)>0$ for real $s$. Expansion gives


$$
\boxed{
D_-(s)=
16s^6+16s^5-23s^4+46s^3+170s^2+40s+25.
}
\tag{5.5}
$$



For an odd prime, a nondegenerate binary quadratic form of determinant $D$ is anisotropic precisely when $-D$ is a quadratic nonresidue. This follows directly by completing the square.

### Theorem 5.1 — an exact upper bound, not just divisibility

Assume (2.1), $m=1$, and


$$
\left(\frac{-D_-(b-2)}p\right)=-1.
\tag{5.6}
$$


Then every primitive $z\in\mathcal K\cap\ker\mathbf e$ satisfies


$$
\boxed{v_p(z^T\Omega^-z)=2.}
\tag{5.7}
$$



Consequently, at every finite normal index, for the actual primitive zero-endpoint generator $z_0$ and any adapted lattice basis vector $z_1$,


$$
T=z_0^T\Omega^-z_0,\qquad V_0=z_0^T\Omega^-z_1
$$


satisfy


$$
\boxed{v_p(T)=2,\qquad v_p(V_0)\ge2,\qquad
v_p\bigl(\gcd(T,V_0)\bigr)=2.}
\tag{5.8}
$$



### Proof

Equation (4.6) proves $p^2\mid z^T\Omega^-z$. Its quotient modulo $p$ is the restricted binary form evaluated at the nonzero vector $d(z)$ satisfying (5.2). Under (5.6), that binary form is anisotropic, so the quotient is nonzero. This proves (5.7), including the upper bound $v_p(T)\le2$.

For $z_1\in\mathcal K$, (4.5) proves $p^2\mid V_0$. Taking the gcd with $T$, whose valuation is exactly two, proves (5.8). ∎

The distinction requested in the assignment is important here:

- the metric alone, together with the high rows, supplies $p^2\mid T,V_0$;
- **anisotropy supplies the missing upper bound** $p^3\nmid T$;
- only their combination proves the exact valuation of $\delta$.

---

## 6. The rising-factorial interpretation

If instead the intended metric is


$$
\omega_j^+=(p+1)(p+2)\cdots(p+j),
$$


then


$$
\omega_j^+\equiv j!\pmod p
\qquad(0\le j\le b<p).
$$


Lemma 2.1 reduces the norm modulo $p$ to


$$
z^T\Omega^+z
\equiv d_s^2+d_{s+1}^2+d_{s+2}^2\pmod p,
\qquad d_j=j!z_j.
\tag{6.1}
$$


The zero-endpoint condition becomes


$$
(s+1)(s+2)d_s+(s+2)d_{s+1}+d_{s+2}=0.
\tag{6.2}
$$


The determinant of this binary restriction is


$$
\boxed{D_+(s)=1+(s+2)^2+(s+1)^2(s+2)^2.}
\tag{6.3}
$$



Therefore


$$
\left(\frac{-D_+(b-2)}p\right)=-1
\quad\Longrightarrow\quad
\boxed{v_p(T)=v_p(\delta)=0.}
\tag{6.4}
$$


The proof is the same nonzero-tail and binary-anisotropy argument, now without a forced factor $p^2$.

This is a separate metric result, not an identification of $\Omega^+$ with $\Omega^-$.

---

# Part III. An explicitly infinite proportional subfamily

## 7. Fixing the Legendre-symbol conditions in one progression

Choose


$$
K=2001.
$$


Define the positive integers


$$
J_+=K^4+2K^2+2K+1,
\tag{7.1}
$$




$$
J_-=
401K^6+1144K^5+1902K^4+1690K^3
+777K^2+176K+16.
\tag{7.2}
$$


These satisfy


$$
J_+=K^4D_+\!\left(-2-\frac1K\right),
\qquad
J_-=K^6D_-\!\left(-2-\frac1K\right).
\tag{7.3}
$$


Also


$$
J_+\equiv1\pmod K,\qquad J_-\equiv16\pmod K.
$$


Since $K$ is odd,


$$
\gcd(K,4J_+J_-)=1.
$$



Consider primes in the simultaneous residue classes


$$
\boxed{
p\equiv1\pmod K,\qquad
p\equiv-1\pmod{4J_+J_-}.
}
\tag{7.4}
$$


The Chinese remainder theorem gives one reduced residue class modulo


$$
4KJ_+J_-.
$$


Dirichlet’s theorem on primes in arithmetic progressions therefore supplies infinitely many such primes. This use of Dirichlet is an established external theorem, not a finite certificate.

For each sufficiently large such prime, set


$$
\boxed{
n=p-1,\qquad b=\frac{p-1}{K},\qquad m=1.
}
\tag{7.5}
$$


Then


$$
\frac bn=\frac1{2001}<\frac1{1000},
$$


and the finite-domain conditions (2.1) hold.

Modulo $p$,


$$
s=b-2\equiv-2-\frac1K.
$$


As $K^4$ and $K^6$ are squares modulo $p$, (7.3) implies


$$
\left(\frac{-D_\pm(s)}p\right)
=
\left(\frac{-J_\pm}p\right).
\tag{7.6}
$$



For any positive integer $J$, primes satisfying $p\equiv-1\pmod{4J}$ obey


$$
\left(\frac Jp\right)=1,\qquad
\left(\frac{-1}p\right)=-1.
$$


For odd prime factors of $J$, this is immediate from quadratic reciprocity; if $2\mid J$, the progression also gives $p\equiv7\pmod8$. Hence


$$
\left(\frac{-J_\pm}p\right)=-1.
$$



We have proved the following genuinely infinite statement.

### Theorem 7.1 — exact norm content on a proportional family

On the infinite subfamily (7.4)–(7.5):

- for the original falling-factorial metric,
  

$$
\boxed{v_p(T)=v_p(\delta)=2;}
$$


- for the rising-factorial interpretation,
  

$$
\boxed{v_p(T)=v_p(\delta)=0.}
$$



The assertions hold for every actual primitive zero-endpoint generator whenever that generator is defined by a normal endpoint system. More generally, the norm assertions hold unconditionally for every primitive integer vector in


$$
\ker R\cap\ker\mathbf e.
$$



Thus the arithmetic theorem itself does not need the proportional analytic theorem. Only eventual identification with the author’s normalized center uses its normality conclusion.

### What its infinite force is—and is not

This proves that an unbounded, index-sized prime cannot contribute unaccounted extra norm content on this family:

- in the falling case, exactly two powers occur, and no third power can occur;
- in the rising case, not even one power occurs.

It is not a fixed-prime seed, and it is not finite evidence.

However, this controls **one moving prime per index**. It does not yet give a linear-in-$n$ estimate for the total logarithmic content, and it does not estimate the scalar cancellation at that prime.

---

## 8. Saturated Plücker content and the norm discriminant

Let $\mathscr L$ be the actual saturated rank-two coefficient lattice, with adapted basis $[z_0,z_1]$, and let


$$
C_\Omega=
\gcd_{i<j}
\left|
\omega_i\omega_j
\det
\begin{pmatrix}
z_{0i}&z_{1i}\\
z_{0j}&z_{1j}
\end{pmatrix}
\right|
\tag{8.1}
$$


be the content of its weighted Plücker vector.

On the subfamily above:

- for the falling metric,
  

$$
\boxed{v_p(C_{\Omega^-})=2;}
  \tag{8.2}
$$


- for the rising metric,
  

$$
\boxed{v_p(C_{\Omega^+})=0.}
  \tag{8.3}
$$



For (8.2), every weighted lattice vector is divisible by $p$. After division by $p$, its three tail coordinates are obtained by multiplying the original tail coordinates by units modulo $p$. Since $\mathscr L$ is saturated, a basis of it has rank two modulo $p$. Lemma 2.1 places all that rank in the three tail coordinates. Thus some $2\times2$ weighted minor divided by $p^2$ is a unit modulo $p$. This proves exact valuation two.

For (8.3), every rising weight is a $p$-unit, so saturation directly supplies a unit weighted minor.

The binary norm discriminant remains


$$
\mathcal D=TU_0-V_0^2
=\sum_{i<j}\omega_i^2\omega_j^2
\det
\begin{pmatrix}
z_{0i}&z_{1i}\\
z_{0j}&z_{1j}
\end{pmatrix}^{\!2}>0.
\tag{8.4}
$$


Thus $C_\Omega^2\mid\mathcal D$. In the falling case,


$$
v_p(\mathcal D)\ge4.
$$



I do **not** claim equality here: the sum of squared primitive weighted minors can cancel modulo $p$. Likewise, the general divisibility


$$
\delta\mid\mathcal D
$$


is not an upper bound for $\delta$. The exact upper bound in Theorem 5.1 came from the explicit anisotropic restriction of the actual metric, not from discriminant divisibility alone.

---

# Part IV. What this says about the final denominator

## 9. Keeping the actual primitive denominator

Retain the A5_turn0 definitions


$$
\delta=\gcd(T,|V_0|),\qquad
t=\frac T\delta,\qquad v_0=\frac{V_0}{\delta},
$$




$$
\alpha=\gcd(t,|a'|),\qquad
r=\frac{a'v_0-b't}{\alpha}.
$$


At every finite normal index, the actual primitive pair is


$$
\boxed{
q_n=\frac t\alpha\frac{k}{\gcd(k,|r|)},\qquad
p_n=\frac r{\gcd(k,|r|)}.
}
\tag{9.1}
$$


The final Gram gcd remains


$$
\boxed{g_B=k\delta\alpha\gcd(k,|r|).}
\tag{9.2}
$$



The new theorem gives, for the selected moving prime in either metric convention,


$$
v_p(t)=0,\qquad v_p(\alpha)=0.
$$


Consequently,


$$
\boxed{
v_p(q_n)=\max\{0,v_p(k)-v_p(r)\}.
}
\tag{9.3}
$$


In other words, **the primitive norm channel is completely resolved at this prime**. Any remaining $p$-power in the actual reduced denominator belongs entirely to the scalar channel.

This is useful localization, but not a bound for that scalar channel. In particular, I have not proved that $p\mid k$, that $r$ is a unit, or that their gcd is small.

---

## 10. Whole evaluated error and nonvanishing

On the subfamily $b/n=1/2001$, let


$$
\tau=(2+1/2001)\log(1+\sqrt2).
$$


If the supplied proportional signed-error theorem is accepted with its stated dependencies, then eventually


$$
\epsilon_n=\frac{p_n}{q_n}-S\ne0,
\qquad
\log|\epsilon_n|=-\tau n+o(n).
$$


Therefore the **whole primitive evaluated error** is exactly


$$
\boxed{
L_n=q_nS-p_n=-q_n\epsilon_n\ne0,
}
\tag{10.1}
$$


with


$$
\log|L_n|
=
\log\frac t\alpha
+\log\frac{k}{\gcd(k,|r|)}
-\tau n+o(n).
\tag{10.2}
$$



The new local theorem does not show that the sum of the two arithmetic budgets in (10.2) is less than $\tau n$, or greater than it. Hence it proves neither irrationality nor exclusion of this proportional center family.

---

# Part V. Independent algebra check on A4’s multijet extension

## 11. The restriction $N<2m$ is unnecessary for recursive solvability

Let $P$ be an integral-Hurwitz polynomial with


$$
P(0)=0,\qquad P(1)=1.
$$


For arbitrary integers $1\le m\le N$, put


$$
Q_{\boldsymbol K}(z)
=
P(z)+\sum_{k=m}^N K_k\frac{z^k(1-z)}{k!}.
$$


Define the complete numerator


$$
Z_j(Q)=j!\sum_{\ell=0}^j\frac{(e^z+F(Q(z)))^{(\ell)}(0)}{\ell!}.
$$



### Proposition 11.1 — nonlinear triangular automorphism

For every finite block $m\le j\le N$, there are polynomials


$$
\Phi_j\in\mathbb Z[K_m,\ldots,K_{j-1}]
$$


such that


$$
\boxed{
\frac{Z_j(Q_{\boldsymbol K})-Z_j(P)}2
=
K_j+\Phi_j(K_m,\ldots,K_{j-1}).
}
\tag{11.1}
$$


Consequently, the map


$$
(K_m,\ldots,K_N)\longmapsto
\left(\frac{Z_j(Q_{\boldsymbol K})-Z_j(P)}2\right)_{j=m}^N
\tag{11.2}
$$


is a triangular polynomial automorphism of $\mathbb Z^{N-m+1}$, with an integer-polynomial inverse.

### Proof

The derivatives $F^{(r)}(0)/2$, $r\ge1$, are integers. One direct verification uses


$$
\frac{F'(z)}2=\frac1{1-z+z^2/2}.
$$


Its Hurwitz coefficients satisfy an integer recurrence with initial coefficients $1,1$.

The derivatives of $Q_{\boldsymbol K}$ at zero are integer affine-linear expressions in the $K_k$. The Bell-polynomial composition formula therefore shows that every coefficient


$$
\frac{(F(Q_{\boldsymbol K})-F(P))^{(\ell)}(0)}2
$$


is an integer polynomial in the parameters of index at most $\ell$. Thus the left side of (11.1) is an integer polynomial involving only $K_m,\ldots,K_j$.

Now hold the lower parameters fixed and change $K_j$ by $u$. The pullback changes by


$$
u\frac{z^j(1-z)}{j!}.
$$


Since its order is $j$, through order $j$ the corresponding change in $F(Q)$ is exactly


$$
F'(0)u\frac{z^j}{j!}=2u\frac{z^j}{j!}.
$$


The complete numerator $Z_j$ therefore changes by exactly $2u$. This proves (11.1). Its inverse is obtained successively by subtracting $\Phi_j$. ∎

Thus arbitrary odd-modulus conditions


$$
Z_j(Q_{\boldsymbol K})\equiv a_j\pmod{d_j},
\qquad d_j\ \text{odd},
$$


remain recursively solvable for **all** finite $N$, with centered choices


$$
|K_j|\le\frac{d_j-1}{2}.
$$



The first nonlinear interaction does not destroy the diagonal coefficient $2$. It only changes the already determined lower-jet term.

### What must not be extended

Outside $N<2m$, the full response need not be affine-linear. For example, at $m=1,j=2$,


$$
\frac{Z_2(Q)-Z_2(P)}2
=
K_2+2P'(0)K_1+K_1^2.
$$


Thus there is no single linear response matrix whose Smith form describes the whole map.

The extension proves exact arithmetic solvability, not puncture avoidance, bounded composition norm, convergence of an infinite formal construction, or shrinking whole evaluated errors. I do not re-present the already archived radius/spacing obstruction as a new result.

---

# Required concluding ledger

## (1) New result and proof status

**Proved here by explicit arithmetic derivation:**

1. A triangular reduction modulo $p$ of the actual growing Rodrigues high block at $n=p-1$.
2. A modulo-$p^2$ restriction formula for the actual falling-factorial metric row.
3. An explicitly infinite proportional subfamily
   

$$
n=p-1,\quad b=(p-1)/2001,\quad m=1
$$


   on which
   

$$
v_p(T)=v_p(\delta)=2
$$


   for the original factorial metric.
4. For the rising-factorial interpretation, on the same subfamily,
   

$$
v_p(T)=v_p(\delta)=0.
$$


5. Exact moving-prime valuations of the saturated weighted Plücker content.
6. Extension of A4’s recursive odd-modulus solvability to arbitrary finite jet blocks, via a triangular polynomial automorphism.

The infinite prime supply uses the established Dirichlet theorem. No finite computation is used as proof of an infinite assertion.

Application to the actual normalized center is conditional on finite normality; eventual normality and the complete signed-error asymptotic remain inherited author-level dependencies.

## (2) Exact remaining bottleneck

At the controlled prime, the norm channel is now resolved:


$$
p\nmid t/\alpha.
$$


But the scalar channel remains exactly


$$
v_p(q_n)=\max\{0,v_p(k)-v_p(r)\}.
$$



Globally, a successful irrationality argument still requires a proved bound


$$
\log\frac{t}{\gcd(t,|a'|)}
+
\log\frac{k}{\gcd(k,|r|)}
<
\bigl((2+1/2001)\log(1+\sqrt2)-\varepsilon\bigr)n
$$


on an unbounded normal sequence, for some $\varepsilon>0$, together with the inherited whole-error nonvanishing.

The present theorem controls one moving prime per index, not the aggregate prime budget. That is the precise limitation; no conclusion about the rationality of $e+\pi$ follows.

## (3) Computation request

**None is required for the stated proofs.**

A bounded optional normalization check would be to verify symbolically the identities (5.5) and (7.2) from the displayed $3\times3$ matrix $M_s$ and plane basis $v,w$. The expected output is exact polynomial equality, not numerical sampling. Such a check would audit algebra only and would not establish any remaining denominator rate.
