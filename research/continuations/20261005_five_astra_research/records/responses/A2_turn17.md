> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 — a norm factor, a remaining multiplier obstruction, and the binary audit

**Status.** I can now prove a factorization of the actual normalized norm by the genuine residual norm $T(N_1,H)$. The factorization does **not** justify the converse implication $D_0=0\Rightarrow T=0$: there is an additional multiplier, and four of its low-digit zeros can be proved directly. I give a finite, explicit formula for that multiplier, but have not evaluated all its remaining zeros.

For MAIN29 grades $0+1$, I obtain a more explicit surviving contraction, with evaluated initial kernels and an ordinary binomial sum for every residual state. I do **not** prove that this contraction has the required norm factor.

The independent audit of A5turn15 passes. In particular, its infinite conclusions


$$
X,Y\in2\mathbb Z_2^{b+1},\qquad
X^TX\equiv X^TY\equiv0\pmod8
$$


do follow from the supplied fixed-polynomial input and the stated finite-boundary identities. The two infinite convolution evaluations are valid.

---

## 1. MAIN29 domain and normalization

Throughout Sections 1–6,


$$
p=29,\qquad b=3^a,\qquad n=2001b,\qquad
a\ge1,\quad a\equiv432827\pmod{682892},\qquad m_w=1.
$$


Write


$$
L=p^4,\qquad b=b_*+Lh,\qquad b_*=687936,
$$


so that


$$
n=n_*+L(2001h+1946),\qquad n_*=191110.
$$


Thus


$$
N:=\left\lfloor\frac{n+2}{L}\right\rfloor=2001h+1946
   =3+29N_1,\qquad N_1=69h+67.
$$


Finally,


$$
h=29H+d,\qquad 0\le d<29.
$$


These are digits of the original $3^a$, not independently chosen cylinder parameters.

The actual columns and metric remain


$$
W_j=\binom{n+2}{j},\quad 0\le j\le b,
$$




$$
Z_w\in p^2\mathbb Z_p^{b+1},\qquad
Y=V_w/b!\in p^3\mathbb Z_p^{b+1},
$$




$$
\widehat P=Z_w/p^2,\quad \widehat Q=Y/p^3,\quad
D_0=\widehat P^T\widehat P\bmod p.
$$



I reuse, without rederiving, the established disappearance of initial product grades at least $3$ in the scalar modulo $p^6$, and the established grade-$2$ residual-norm factor.

---

## 2. A particularly useful grade-zero $P$-kernel

Set


$$
C=C_n,\qquad
h_0(j)=\sum_{i=0}^{28}(-1)^i i!\binom ji.
$$


The first forcing digit gives


$$
h_P(j)\equiv C h_0(j)\pmod p.
$$


Indeed, $29\mid n$, and Frobenius gives


$$
J_t\equiv0\pmod p\quad(1\le t\le28),\qquad J_0=C\pmod p.
$$


The contact operator is divisible by $p$, so it does not change this first digit.

Moreover,


$$
h_0(j)+j h_0(j-1)
 =1+29!\binom j{29}\equiv1\pmod p.
$$


In the reconstructed Laurent variable $r=x/(1-x)$, we may therefore choose


$$
\boxed{\mathcal P_0(j,r)=C\bigl(r+1-h_0(j)\bigr).}
\tag{2.1}
$$


This is a legitimate integral choice of the grade-zero representative. Write the complete kernel as


$$
\mathcal P=\mathcal P_0+p\mathcal P_1+p^2\mathcal P_2\pmod{p^3},
\tag{2.2}
$$


where the representatives can be chosen with the previous graded degree bounds. In particular, $\mathcal P_1$ has both degrees at most $58$.

Let $Z^{(i)}$ be the reconstructed weighted column associated with $\mathcal P_i$. The new base column is explicitly


$$
\boxed{
Z^{(0)}_j=(-1)^{j+1}CW_j
\left\{
\binom{2n+b-j}{b-j}
-h_0(j)\binom{2n+b-j-1}{b-j}
\right\},
\quad 0\le j\le b.
}
\tag{2.3}
$$


The endpoint $j=b$ is included in this formula.

### Lemma 2.1 — the base column already has the two required factors



$$
\boxed{Z^{(0)}\in p^2\mathbb Z_p^{b+1}.}
\tag{2.4}
$$



**Proof.** Consider separately


$$
W_j\binom{2n+b-j}{b-j},
\qquad
W_j\binom{2n+b-j-1}{b-j}.
$$


In base $29$, the relevant low digits are


$$
n+2=(2,7,24,7,\ldots),
$$




$$
2n=(0,14,19,15,\ldots),\qquad
2n-1=(28,13,19,15,\ldots),
$$




$$
b=(27,28,5,28,\ldots).
$$



At digit $1$, if subtraction of $j$ from $n+2$ has no borrow, then $j_1\le7$. Consequently the digit of $b-j$ there is at least $20$. Adding either $13$ or $14$, with any incoming carry, produces a carry in the other binomial. Thus the two binomials together have at least one carry at digit $1$.

At digit $3$, absence of a borrow in the weight similarly implies $j_3\le7$, and hence a digit of $b-j$ at least $20$. Addition of $15$ forces a carry in the other binomial.

These are distinct digit positions. Kummer’s theorem proves divisibility by $p^2$ for each product, and therefore for (2.3). ∎

Since $Z_w$ and $Z^{(0)}$ are both divisible by $p^2$, (2.2) also gives


$$
Z^{(1)}\in p\mathbb Z_p^{b+1}.
\tag{2.5}
$$



---

## 3. Exact factorization of the base norm

The following construction uses only factorials of numbers between $0$ and $28$. It is an exact finite formula, not a sampling prescription.

Put


$$
N_*=191112,\qquad c_0=382220,\qquad c_{-1}=382219.
$$


For $0\le x\le b_*$, let

* $e(x)=\mathbf1_{x>N_*}$, the final low-block borrow in the weight;
* $v=b_*-x$;
* $\nu_\tau(x)$ be the total number of low-block carries in
  

$$
\binom{n+2}{j}\binom{2n+\tau+b-j}{b-j},
  \qquad j=LJ+x,\quad \tau=0,-1,
$$


  counting the first four digit positions only.

Thus $\nu_\tau(x)\ge2$. For an integer $u$, let $\operatorname{dig}_i(u)$ denote the $i$-th digit of $u\bmod L$. Define


$$
\mu_\tau(x)=
\mathbf1_{\nu_\tau(x)=2}
\prod_{i=0}^{3}
\frac{
 \operatorname{dig}_i(N_*)!\,
 \operatorname{dig}_i(c_\tau+v)!
}{
 \operatorname{dig}_i(x)!\,
 \operatorname{dig}_i(N_*-x)!\,
 \operatorname{dig}_i(v)!\,
 \operatorname{dig}_i(c_\tau)!
}
\in\mathbb F_{29}.
\tag{3.1}
$$


Every denominator in (3.1) is a unit. Put


$$
c(x)=\mu_0(x)-h_0(x)\mu_{-1}(x),
\qquad
\boxed{\kappa_e=\sum_{\substack{0\le x\le b_*\\e(x)=e}}c(x)^2
\quad(e=0,1).}
\tag{3.2}
$$



These two constants have not been numerically evaluated here.

### Lemma 3.1 — exact separation after four digits

For $j=LJ+x$, the nonzero possibilities for $Z^{(0)}_j/p^2\bmod p$ are


$$
\boxed{
\frac{Z^{(0)}_j}{p^2}
\equiv
(-1)^{j+1}C\,c(x)
\binom NJ\binom{2N+h-J}{h-J}
\begin{cases}
2N+h-J+1,&e(x)=0,\\
N-J,&e(x)=1.
\end{cases}
\pmod p.
}
\tag{3.3}
$$


For $x>b_*$, the residue is zero.

**Proof.** Repeatedly separate the $p$-parts and unit parts of the factorials in the two binomial products. The first four levels contribute (3.1). The sign is
$(-1)^{\nu_\tau(x)}=1$ when $\nu_\tau(x)=2$.

Exactly one of the two binomials has the final low-block carry. If it is the weight, the remaining high factorial ratio is


$$
(N-J)\binom NJ\binom{2N+h-J}{h-J}.
$$


If it is the other binomial, the remaining ratio is


$$
(2N+h-J+1)\binom NJ\binom{2N+h-J}{h-J}.
$$


The two choices $\tau=0,-1$ have the same high ratio.

If $x>b_*$, both binomials carry at digit $3$, while at least one carries at digit $1$. Such a term is divisible by $p^3$. This also shows why no extra high-index endpoint is introduced. ∎

Now define the genuine residual norm, with its actual finite range,


$$
T=T(N_1,H)
=\sum_{k=0}^{H}
\binom{N_1}{k}^2
\binom{2N_1+H-k}{H-k}^2\pmod p.
\tag{3.4}
$$


For $v\in\mathbb Z$, put


$$
B_v=
\begin{cases}
\binom{v+6}{6}\pmod p,&0\le v\le22,\\
0,&\text{otherwise}.
\end{cases}
$$


Set


$$
\psi_1(d)=
\sum_{t=0}^{3}\binom3t^2(3-t)^2B_{d-t}^2
=9B_d^2+7B_{d-1}^2+9B_{d-2}^2,
\tag{3.5}
$$




$$
\psi_0(d)=
\sum_{t=0}^{3}\binom3t^2(7+d-t)^2B_{d-t}^2.
\tag{3.6}
$$



### Proposition 3.2 — evaluated residual factor of the base norm



$$
\boxed{
\frac{(Z^{(0)})^TZ^{(0)}}{p^4}
\equiv
C^2\bigl(\kappa_0\psi_0(d)+\kappa_1\psi_1(d)\bigr)\,
T(N_1,H)
\pmod p.
}
\tag{3.7}
$$



**Proof.** Square (3.3) and sum over $x$. Then write $J=29k+t$. Since $N\bmod29=3$, a nonzero term requires $0\le t\le3$. Nonvanishing of the second binomial requires


$$
0\le d-t\le22.
$$


There is then no borrow from $h-J$ and no low carry in adding $2N$. Lucas gives


$$
\binom NJ\binom{2N+h-J}{h-J}
\equiv
\binom3t B_{d-t}
\binom{N_1}{k}
\binom{2N_1+H-k}{H-k}.
$$


The two linear factors in (3.3) reduce respectively to $7+d-t$ and $3-t$. This proves (3.7). ∎

### A columnwise zero that must not be omitted

For $25\le d\le28$,


$$
\boxed{Z^{(0)}\in p^3\mathbb Z_p^{b+1}.}
\tag{3.8}
$$


Indeed, for $d\ge26$ there is no $t\in[0,3]$ with $0\le d-t\le22$. For $d=25$, the only possibility is $t=3$, but **both** linear factors in (3.3) vanish:


$$
3-t=0,\qquad 7+d-t=29.
$$


This is a statement about every base-column coordinate, not cancellation in its norm.

---

## 4. The actual norm factor and its exact limitation

By the established disappearance of initial grades at least $3$, applied to $pZ_w^TZ_w$,


$$
D_0\equiv
\frac{(Z^{(0)})^TZ^{(0)}}{p^4}
+
2\frac{(Z^{(0)})^TZ^{(1)}}{p^3}
\pmod p.
\tag{4.1}
$$


All other terms have the excluded initial grades. The displayed quotients are integral by (2.4)–(2.5).

The established grade-$2$ lemma applies to the second contraction:


$$
\frac{(Z^{(0)})^TZ^{(1)}}{p^3}
=K_{01}\,T(N_1,H)\pmod p.
\tag{4.2}
$$



Here $K_{01}$ is not an unspecified growing-dimensional contraction. It has the following finite definition.

1. Form the Newton contraction numerator for $\mathcal P_0(j,r)\mathcal P_1(j,s)$, padded to $K_2=88$.
2. Apply the four fixed sections, retaining total ghost cost at most $3$.
3. For the unique cost-$2$ contact-only path, the final section contributes
   

$$
\Phi/p=2z\pmod p.
$$


   Multiply its preceding scalar, its actual ghost-binomial weights, and $2\Psi_{e_U,0,0,1}(d)$.
4. For every cost-$3$ path, sum each terminal monomial coefficient times the explicit multiplier
   

$$
\Psi_{\lambda,\alpha,\beta,\gamma}(d)
$$


   from turn16, equation (11).

All arithmetic in this definition is over $\mathbb F_{29}$; all ghost-binomial weights use the original exponents. There is no division of an unevaluated residual coefficient.

Consequently,


$$
\boxed{
D_0=T(N_1,H)\,\Lambda(n,b;d),
}
\tag{4.3}
$$


where, for $0\le d\le24$, the exact finite multiplier is


$$
\boxed{
\Lambda(n,b;d)
=C^2\bigl(\kappa_0\psi_0(d)+\kappa_1\psi_1(d)\bigr)+2K_{01}.
}
\tag{4.4}
$$



For $25\le d\le28$, one can choose the multiplier to be zero. In fact,


$$
\boxed{D_0=0\qquad(25\le d\le28)}
\tag{4.5}
$$


without any assumption on $T$. To see this directly, the same grade elimination gives


$$
D_0\equiv
\frac{2(Z^{(0)})^TZ_w-(Z^{(0)})^TZ^{(0)}}{p^4}\pmod p,
$$


and (3.8), together with $Z_w\in p^2\mathbb Z_p^{b+1}$, makes the numerator divisible by $p^5$.

### What the zero-locus statement actually says

We have proved


$$
T=0\ \Longrightarrow\ D_0=0.
$$


For $0\le d\le24$, the exact converse condition is


$$
\boxed{
D_0=0
\quad\Longleftrightarrow\quad
T=0\ \text{or}\ \Lambda(n,b;d)=0.
}
\tag{4.6}
$$


For $25\le d\le28$, the norm digit vanishes regardless of $T$.

Thus identifying $D_0=0$ with $T=0$ would still be incorrect. I have **not** evaluated every possible additional zero of (4.4) on $0\le d\le24$. This is the remaining norm-multiplier part of the assignment.

---

## 5. Grades $0+1$: explicit surviving contraction

The grade-zero $Q$-kernel can also be evaluated. Modulo $p$, the complete boundary has


$$
c_0=1,\qquad c_1=-1,
$$


and all other boundary coefficients and the contact part vanish. Since $b$ is odd,


$$
\boxed{
\mathcal Q_0(j,s)
=(2+s^{-1})(1+j+js^{-1}).
}
\tag{5.1}
$$


Write the actual complete kernel as


$$
\mathcal Q=\mathcal Q_0+p\mathcal Q_1+p^2\mathcal Q_2+p^3\mathcal Q_3.
$$


Here $\mathcal Q_1$ is obtained from the complete retained force and boundary, not from an isolated tail.

Let $\mathscr B(F,G)$ denote the full reconstructed weighted scalar contraction of two kernels, including $j=b$. Then the complete initial grades $0+1$ are


$$
\boxed{
\begin{aligned}
E_{[0]}+E_{[1]}={}&
6C\,\mathscr B(\mathcal P_0,\mathcal Q_0)\\
&+p\left[
6C\,\mathscr B(\mathcal P_1,\mathcal Q_0)
+6C\,\mathscr B(\mathcal P_0,\mathcal Q_1)
-\mathscr B(\mathcal P_0,\mathcal P_0)
\right]
\pmod{p^6}.
\end{aligned}}
\tag{5.2}
$$


Unlike the earlier generic expression, both grade-zero kernels in (5.2) are now explicit.

Here is an ordinary binomial-sum form of every residual contraction in (5.2). It retains all finite boundaries.

Suppose that four exact section steps leave exponent offsets


$$
\lambda=(\lambda_r,\lambda_s,\lambda_U,\lambda_z)
$$


and numerator monomial $r^\alpha s^\beta z^\gamma$. Put $A=N+h+1$. Its residual contraction is exactly


$$
\boxed{
\begin{aligned}
\mathscr C_{\lambda,\alpha,\beta,\gamma}
=\sum_{t=0}^{N-\lambda_U}
&\binom{N-\lambda_U}{t}
 \binom{N-\lambda_z}{\lambda_U+t-\gamma}\\
&\times
 \binom{2N+h+1-\lambda_r-\lambda_U-t}{h-\alpha-t}\\
&\times
 \binom{2N+h+1-\lambda_s-\lambda_U-t}{h-\beta-t}.
\end{aligned}}
\tag{5.3}
$$


Invalid lower indices give zero. Formula (5.3) follows by expanding $U^{N-\lambda_U}$ according to the number $t$ of selected $rs$-terms. In particular, it is valid at the endpoints of the finite sum, not merely in its interior.

For complete precision bookkeeping, the section recursion is


$$
e^{(i+1)}=\left\lfloor e^{(i)}/p\right\rfloor-\nu_i,
$$


with the actual binomial weight


$$
p^{|\nu_i|}
\prod_f\binom{\lfloor e_f^{(i)}/p\rfloor}{(\nu_i)_f}.
$$


One retains

* all paths of total ghost cost at most $5$ for grade $0$;
* all paths of total ghost cost at most $4$ for grade $1$.

Each terminal numerator coefficient is multiplied by (5.3), at the remaining precision. Offsets are obtained from this exact recursion; they are not guessed from the last ghost alone. Thus borrowing caused by an earlier ghost is included.

This gives a precise surviving contraction for grades $0+1$, with no remaining multivariable coefficient extraction. It does **not**, by itself, prove that their sum is a multiple of $T$ after division by $p^5$. In particular, higher-precision instances of (5.3) cannot be replaced by their modulo-$p$ norm factors.

The full scalar is still


$$
\mathcal E\equiv E_{[0]}+E_{[1]}+E_{[2]}\pmod{p^6},
\qquad
E_{[2]}/p^5=K_2T\pmod p.
$$


The last factorial block remains handled by the established higher-grade disappearance; it has not been reintroduced as an unresolved obstruction.

---

## 6. Independent audit of A5turn15

The binary domain is exactly


$$
b=9^r,\qquad n=4002b,\qquad r=18+32u,\quad u\ge0.
$$


The actual columns and metric are


$$
X=\frac{Z_w}{2R},\qquad Y=\frac{V_w}{4b!},
\qquad R=2^{n/2}\binom n{n/2},
$$




$$
\omega_j=j!\binom{n+2}{j}=(n+2)_{\underline j},
\qquad 0\le j\le b.
$$


The inverse still has index range $0\le i,j<b$.

### 6.1 Bounded operator transfer: passed

The supplied degree-$17/15$ vectors reduce exactly to the stated $P\bmod8$ and $Q-2P\bmod16$.

The reference substitution uses


$$
v_2(n-2)=6,\qquad v_2(b-81)=7.
$$


The bound


$$
v_2\!\left(\binom{x+\delta}{a}-\binom xa\right)
\ge v_2(\delta)-\lfloor\log_2a\rfloor
$$


is sufficient only after the powers of $2$ multiplying each operator iterate are included. A5’s table does this correctly, including the lower-index-$17$ term. No substitution is made in the large kernel $T(-2n)$.

### 6.2 Fresh whole-column $Y$-parity: passed

Write


$$
b=128D+81,\qquad n=128C+66,
$$


where $D$ is odd and $C\equiv2\pmod4$. The paired carry expression


$$
e_t=\binom Ct\binom{2C+1+D-t}{D-t}\pmod2
$$


vanishes identically: the first factor forces $t$ even, and then the second factor has an odd lower index added to the odd integer $2C+1$.

For odd $j$, the complete residual gives


$$
\eta_j\equiv\binom{2n+b-1-j}{b-j}\pmod2.
$$


If $W_j/4$ is odd, Lucas restricts $j\bmod128$ to


$$
1,3,65,67.
$$


At residues $3,67$, both reconstruction terms are even. At $j=128t+1,128t+65$, the reconstruction and weight give precisely $e_t$. Hence every nonterminal odd coordinate of $Y$ is even. Combining this with the even-coordinate support proves whole-column evenness, subject to the endpoint below.

### 6.3 Full odd endpoint: passed

In


$$
W_b=\frac{n+2}{b}\binom{n+1}{b-1},
$$


the binomial has consecutive borrows at positions $4,5,6,7$. The last one uses $C$ even and $D$ odd. Therefore


$$
v_2(W_b)\ge6.
$$


Keeping the actual endpoint terms,


$$
X_b=\frac{W_b\,b\theta_{b-1}}2,\qquad
Y_b=\frac{W_b(1+b\eta_{b-1})}{4},
$$


gives


$$
v_2(X_b)\ge5,\qquad v_2(Y_b)\ge4.
$$


The endpoint $1$ is essential in the formula, but its scalar contribution is zero at the assigned precision.

### 6.4 Reconstruction formulas (20), (22), (23): passed

The finite moment identity


$$
(T(-2n)\mathcal S_b\binom Xr)_j
=(-1)^j\sum_{t=0}^{r}
 \binom j{r-t}\binom{2n+t-1}{t}
 \binom{2n+b-1-j}{b-1-j-t}
$$


retains the upper boundary. Substituting the supplied polynomial coefficients yields the displayed reconstruction reductions.

The potentially delicate simplifications are valid:

* For $j=4k$, the complete difference reduces to
  

$$
G_j\equiv
  8(1+k)\binom{4T}{4\ell+4}+(8+12k)\binom{4T}{4\ell}
  \equiv12k\binom{4T}{4\ell}\pmod{16}.
$$


  If $k$ is even, the two binomials have equal parity; if $k$ is odd, the latter is even.

* The congruence
  

$$
\binom{2A}{2B}\equiv\binom AB\pmod4
$$


  is valid: in
  

$$
(1+z)^{2A}\equiv(1+z^2)^A+2Az(1+z^2)^{A-1}\pmod4,
$$


  the correction has only odd powers.

* At $j=4k+2$, the two minus signs in the reductions of $W_j/2$ and the reconstruction binomial cancel, giving A5’s positive formula (23).

* In the valuation-one case for $W_j$, the complete difference satisfies $G_j\equiv2B\pmod8$. This is exactly the precision needed after division by $4$, and proves $Y_{4k+2}\equiv0\pmod4$.

Thus the resulting formulas are indeed


$$
X_{4k}\equiv-(k+1)F_k,\qquad Y_{4k}\equiv-F_k\pmod4,
$$




$$
Y_{4k+2}\equiv0\pmod4,
$$




$$
X_{4k+2}\equiv
\binom{M-1}{k}\binom{h+m-k-1}{m-k-1}\pmod4.
$$



### 6.5 Infinite convolutions (39) and (43): passed

Put $A=(M-1)/2=16C+8$, which is even. For the $4k+2$ sum,


$$
\Sigma=[z^{m-1}](1+z)^{M-1}(1-z)^{-2M}.
$$


Modulo $4$,


$$
(1+z)^{M-1}\equiv(1+z^2)^A,
$$




$$
(1-z)^{-2M}\equiv
(1+z^2)^{-M}+2Mz(1+z^2)^{-M-1}.
$$


Since $m-1$ is odd,


$$
\frac{\Sigma}{2}\equiv
[w^{16D+9}](1+w)^{-(16C+10)}=0\pmod2.
$$


The last series has only even powers over $\mathbb F_2$. This is an infinite formal-series argument, not sampling.

For the even-$k$ norm contribution, taking the even part gives


$$
[w^{m/2}](1+w)^{A-M}
=
[w^{16D+10}](1+w)^{-(16C+9)}.
$$


Since $16D+10$ is even, its integer coefficient is


$$
\binom{16(C+D)+18}{16D+10}\pmod4.
$$


The borrows at binary positions $3,4$ prove divisibility by $4$. Hence


$$
\boxed{X^TX\equiv X^TY\equiv0\pmod8.}
$$



No repair to these coordinate or infinite convolution formulas is required. The fixed lift is finite input to these proofs, not their replacement. A5’s subsequent digit $(H-N)/8\bmod2$ remains outside this audit.

---

## 7. Primitive arithmetic and the whole real errors

For each family separately, retain its stated actual metric and the least two-column denominator


$$
N_B=d_B[u,v].
$$


Then


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
p_n=H_B/g_B,\qquad q_n=A_B/g_B>0.
$$


The primitive multiplier on the integer coefficient pair is $1/g_B$; $q_n$ is the actual reduced center denominator.

For MAIN29, with its stated rising-factorial metric and $v_{29}(d_B)=0$,


$$
\delta=v_{29}(\widehat P^T\widehat P),\qquad
\mu=v_{29}(\widehat P^T\widehat Q),
$$




$$
v_{29}(g_B)=
\min\{4F_n+4+\delta,\ 2F_n+F_b+5+\mu\},
$$




$$
v_{29}(q_n)=
\max\{0,\ 2F_n-F_b-1+\delta-\mu\}.
$$


The norm is nonzero by positivity. Finiteness of the mixed valuation retains the supplied original-family nonvanishing dependency.

For the binary falling-factorial metric,


$$
v_2(q_n)=
\max\left\{0,\frac{3n}{2}-v_2(b!)-s_2(n)-1-(\gamma-\alpha)\right\}.
$$


The proved lower bounds $\alpha,\gamma\ge3$ do not bound their difference.

At the supplied status of the complete signed-error theorems,


$$
q_n(e+\pi)-p_n=-q_n\epsilon_n,
$$


with the MAIN29 form eventually negative and the binary form eventually positive, in both cases nonzero. Their complete exponential residuals, logarithmic forces, and endpoint contributions remain included. No local result here supplies the necessary global denominator rate.

---

# Concluding ledger

## (1) New result and proof status

**Proved, using the established higher-grade and grade-$2$ results:**

* The explicit base kernel (2.1) and its whole-column divisibility by $29^2$.
* The exact four-digit separation (3.3).
* The base-norm factorization (3.7).
* The actual norm factorization
  

$$
D_0=T(N_1,H)\Lambda(n,b;d),
$$


  with the finite multiplier formula (4.4).
* The additional actual norm-zero cylinder
  

$$
D_0=0\qquad(d=25,26,27,28),
$$


  without assuming $T=0$.
* The explicit initial grade-zero $Q$-kernel and the complete surviving grades-$0+1$ contraction (5.2)–(5.3).
* A5turn15’s whole-column parity, complete endpoint, reconstruction formulas, infinite convolutions, and $\alpha,\gamma\ge3$ pass the independent audit.

**Not proved:** all remaining zeros of $\Lambda$; the required grades-$0+1$ scalar cancellation; MAIN29 alignment on the full actual norm-zero locus; an all-depth valuation estimate; irrationality or rationality of $e+\pi$.

## (2) Exact remaining bottleneck

Two distinct issues remain:

1. Evaluate $\Lambda(n,b;d)$ for $0\le d\le24$, retaining the actual first corrected $P$-kernel. A claim $D_0=0\iff T=0$ still requires excluding its zeros and is already inapplicable on $d=25,\ldots,28$.

2. Evaluate (5.2), with its complete ghost paths and the higher-precision residual sums (5.3), on **both** parts of the norm-zero locus:
   

$$
T=0,\qquad\text{and}\qquad T\ne0,\ \Lambda=0.
$$


   The second includes the newly proved $d=25,\ldots,28$ norm-zero cylinders.

## (3) Bounded computation request

No growing-dimensional inverse or new binary lift is requested.

A useful exact computation is:

**Inputs:** $p=29$, the constants


$$
b_*=687936,\quad N_*=191112,\quad
c_0=382220,\quad c_{-1}=382219,
$$


and equations (3.1)–(3.2).

**Expected verifiable output:**

1. The two residues $\kappa_0,\kappa_1$.
2. The $29$ values of
   

$$
\kappa_0\psi_0(d)+\kappa_1\psi_1(d),
$$


   including all zeros.
3. An independent check, for each low index $x$, of the asserted minimum two carries and of the extra carry when $x>b_*$.

This uses fewer than $29^4$ low-index cases, with only digit factorials at most $28!$. It evaluates the two fixed low-block constants, not the infinite original assertion. The separate $K_{01}$ multiplier and grades-$0+1$ contraction would remain to be evaluated.
