> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1, Turn 9 — Exact valuation of the signed producer denominator and a uniform scalar-precision theorem

## Executive conclusion

The scalar obstruction identified in the assignment can be resolved.

For the **actual** normalized even-moment matrix


$$
\mathsf T_n=\left(\binom{a+b}{a}\gamma_{a+b}\right)_{0\le a,b<n},
\qquad
F=(n-1)!,
\qquad
u_a=\frac{F(-2)^a}{a!},
$$


and the actual complete-force numerator


$$
\eta_n=F^2-u^T\mathsf T_n^{-1}u,
\qquad
\chi_n=u^T\mathsf T_n^{-1}\tau,
$$


I prove


$$
\boxed{\eta_n\equiv3\pmod9,\qquad \chi_n\equiv3\pmod9}
$$


for **every**


$$
n\ge5,\qquad n\equiv2\pmod3.
$$


Consequently,


$$
\boxed{v_3(\eta_n)=v_3(\chi_n)=1,\qquad
\xi_n=\frac{\chi_n}{\eta_n}\in1+3\mathbb Z_3.}
$$



In particular, this holds throughout the retained original family


$$
n=4^j+1,\qquad j>0,\qquad81\mid j,
$$


without imposing any new restriction on its higher digits or its real window.

This is not an extrapolation from the probes at $n=5,8,11,14,17$. The proof uses:

* an explicit finite Pascal vector respecting the genuinely shorter residue-$2$ class;
* the actual normalized moments modulo $9$;
* a quadratic approximation identity for the inverse contraction;
* an exact cancellation in the **complete** producer force.

The principal consequences are:

1. **The signed scalar denominator loses exactly one $3$-adic digit.** There is no unknown index-dependent scalar precision loss.
2. **The actual producer endpoint has the sharp valuation**
   

$$
\boxed{Q_n^{\rm loc}(-1)=-F^2\xi_n,\qquad
   v_3(Q_n^{\rm loc}(-1))=2v_3(F).}
$$


3. **A fully specified Pascal digit recurrence computes the true pair $(\eta_n,\chi_n)$** at any prescribed finite precision. Its inversions are only the already-proved finite Pascal inverse modulo $3$ and scalar unit inversions.
4. **The terminal producer jet is now evaluable with a uniform precision budget.** To determine $R\bmod3^p$, a sufficient scalar-input precision is $3^{p+7}$, with the accepted factorial-tail and endpoint conditions retained.

These results resolve the proposed producer-scalar bottleneck. They do **not** prove nonvanishing or a relative valuation law for the later residual determinant/cofactor pair. The full final gcd and the whole evaluated error remain global obligations.

No tools were used.

---

## 1. Scope and source-status separation

The original domain remains


$$
n=4^j+1,\qquad j>0,\qquad81\mid j,
$$




$$
A=n-2=H-D,\qquad H=3^{h-1},\qquad0<D<H/972,
$$


with


$$
t=v_3(A)=1+v_3(j)\ge5.
$$



The finite residual coordinates remain exactly


$$
m=\frac{A+1}{2},\qquad d=\frac{3D}{2}-1,\qquad
\nu=\frac D2-1,
$$




$$
U_a=(y-1)^a\quad(0\le a<D),\qquad
z_i=(y-1)^Dy^i\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m).
$$



Nothing below enlarges HIGH, restores a deleted residual coordinate, or changes the original index family.

### Results reused at their established scope

I reuse from A1 Turn 5:

* the exact shifted moment recurrence;
* the theorem $\mathsf T_n\in\operatorname{GL}_n(\mathbb Z_3)$;
* the exact rank-one determinant and inverse identities;
* the complete normalized producer force;
* the actual order-six interface and factorial-saturation consequences on the original domain.

I reuse A4 Turn 13’s independent closure of the **coarser** propagation required by A1 Turn 7. Thus the audited depth-$14$ determinant-pair reduction is available on its stated narrow original-index window.

I do **not** use as an established premise any of the still-pending Turn 8 refinements:

* the sharper supported return;
* $\mathcal Q\in27M$;
* the depth-$16$ reduction;
* the at-most-twenty-feature bulk–boundary decomposition.

The new scalar theorem is independent of those claims. This report takes the producer-scalar route offered in the assignment, rather than removing or simplifying any of the twenty proposed boundary features.

The supplied finite certificates retain only their stated finite scope.

---

# Part I. The actual scalar denominator

## 2. Actual moments and a modulo-$9$ identity

Put $x=y-1$. The positive moments are


$$
\Lambda_r=\int_0^\infty e^{-s}\bigl(s(s-2)\bigr)^r\,ds,
\qquad
\gamma_r=\frac{\Lambda_r}{r!}.
$$


The established exact recurrence is


$$
\gamma_0=1,\qquad\gamma_1=0,
$$




$$
\boxed{\gamma_{r+1}=(4r+2)\gamma_r+4\gamma_{r-1}\qquad(r\ge1).}
\tag{2.1}
$$



Its modulo-$3$ consequence was already used in the unit theorem. Here the additional information needed is modulo $9$.

### Lemma 2.1 — Actual normalized moments modulo $9$

The sequence $\gamma_r\bmod9$ has period $9$, with one period


$$
\boxed{1,\ 0,\ 4,\ 4,\ 0,\ 7,\ 1,\ 0,\ 4.}
\tag{2.2}
$$


In particular, for every $s\ge0$,


$$
\boxed{
\gamma_{3s+1}\equiv0\pmod9,\qquad
\gamma_{3s}+2\gamma_{3s+2}\equiv0\pmod9,
}
\tag{2.3}
$$


and


$$
\gamma_{3s+2}\equiv1\pmod3.
\tag{2.4}
$$



### Proof

Applying (2.1) modulo $9$ gives the displayed values through $\gamma_8$, followed by


$$
\gamma_9\equiv1,\qquad\gamma_{10}\equiv0\pmod9.
$$


The coefficient $4r+2$ is periodic modulo $9$ with period $9$. Thus the equality of the two successive initial residues at indices $0,1$ and $9,10$ propagates by the recurrence.

The three possibilities for


$$
(\gamma_{3s},\gamma_{3s+2})\pmod9
$$


are $(1,4),(4,7),(1,4)$, giving (2.3)–(2.4). ∎

This is a proof by recurrence, not a claim inferred from an unbounded computation.

---

## 3. Two finite binomial identities

The following elementary congruences supply the extra digit needed for the scalar contraction.

### Lemma 3.1

For $i,j\ge0$, writing $s=i+j$,


$$
\boxed{\binom{3s}{3i}\equiv\binom{s}{i}\pmod9,}
\tag{3.1}
$$


and


$$
\boxed{
\binom{3s+2}{3i+1}
\equiv(2+3s)\binom{s}{i}\pmod9.
}
\tag{3.2}
$$



### Proof

Modulo $9$,


$$
(1+z)^{3s}
=\bigl(1+z^3+3z+3z^2\bigr)^s
$$


is the sum of


$$
(1+z^3)^s
$$


and


$$
3s(z+z^2)(1+z^3)^{s-1},
$$


because every term containing at least two factors $3z+3z^2$ is divisible by $9$.

The second displayed polynomial has no exponent divisible by $3$, proving (3.1).

For (3.2), the exact identity


$$
\binom{3s+2}{3i+1}
=
\frac{(3s+2)(3s+1)}
     {(3i+1)(3j+1)}
\binom{3s}{3i}
$$


uses only unit denominators in $\mathbb Z_3$. Modulo $9$,


$$
(3s+2)(3s+1)\equiv2,
$$




$$
(3i+1)(3j+1)\equiv1+3s,
$$


so the quotient is


$$
2(1-3s)\equiv2+3s\pmod9.
$$


Now apply (3.1). ∎

---

## 4. The finite Pascal test vector

For the scalar theorem, temporarily write


$$
n=3N+2,\qquad N\ge1.
$$


This includes every original index, but permits a stronger theorem.

The original finite residue-class sizes are


$$
m_0=N+1,\qquad m_1=N+1,\qquad m_2=N.
$$


The last class is genuinely shorter and will remain so.

Define


$$
c_i=(-1)^{N-i}\binom Ni,\qquad0\le i\le N,
$$


and the actual $n$-vector $w$ by


$$
\boxed{
w_{3i}=c_i,\qquad w_{3i+1}=-c_i\quad(0\le i\le N),
\qquad
w_{3i+2}=0\quad(0\le i<N).
}
\tag{4.1}
$$



Let


$$
Z=\left(\binom{i+j}{i}\right)_{0\le i,j\le N},
\qquad
P=\left(\binom ij\right)_{0\le i,j\le N}.
$$


The finite identities


$$
Z=PP^T,\qquad c=P^{-T}e_N
$$


give


$$
\boxed{Zc=e_N.}
\tag{4.2}
$$



### Lemma 4.1 — The test vector is an actual inverse lift modulo $3$

For


$$
F=(n-1)!,
\qquad
u_a=\frac{F(-2)^a}{a!},
$$


one has


$$
\boxed{\mathsf T_nw\equiv u\pmod3.}
\tag{4.3}
$$



### Proof

Since $3N$ occurs in $F/a!$ whenever $a\le3N-1$,


$$
u_a\equiv0\pmod3\quad(a\le3N-1),
$$


whereas


$$
u_{3N}\equiv u_{3N+1}\equiv1\pmod3.
$$



The established finite residue decomposition of $\mathsf T_n\bmod3$ is


$$
\begin{pmatrix}
Z&0&Z_{N+1,N}\\
0&2Z&0\\
Z_{N,N+1}&0&0
\end{pmatrix}.
$$


Applying this matrix to $(c,-c,0)$, and using (4.2), gives:

* $e_N$ in the residue-$0$ class;
* $-2e_N\equiv e_N$ in the residue-$1$ class;
* zero in the residue-$2$ class, because it consists of the first $N$ coordinates of $Zc=e_N$.

This is exactly $u\bmod3$. ∎

The last step is where the actual finite endpoint matters. Adding a residue-$2$ coordinate would change the argument.

---

## 5. Exact valuation of $\eta_n$

### Theorem 5.1 — Signed producer denominator law

For every $n\ge5$ with $n\equiv2\pmod3$,


$$
\boxed{\eta_n=F^2-u^T\mathsf T_n^{-1}u\equiv3\pmod9.}
\tag{5.1}
$$


Hence


$$
\boxed{v_3(\eta_n)=1.}
\tag{5.2}
$$



### Proof

Let


$$
v=\mathsf T_n^{-1}u.
$$


The normalized positive matrix is a $3$-adic unit matrix, and Lemma 4.1 gives


$$
w-v\in3\mathbb Z_3^n.
$$


Therefore


$$
(w-v)^T\mathsf T_n(w-v)\in9\mathbb Z_3.
$$


Expanding this exact quadratic expression yields


$$
u^T\mathsf T_n^{-1}u
\equiv2u^Tw-w^T\mathsf T_nw\pmod9.
$$


Consequently,


$$
\boxed{
\eta_n\equiv F^2-2u^Tw+w^T\mathsf T_nw\pmod9.
}
\tag{5.3}
$$



We now evaluate both contractions.

### 5.1 The linear contraction

Pairing the two coordinates in (4.1),


$$
\begin{aligned}
u^Tw
&=\sum_{i=0}^N c_iF
\left(
\frac{(-2)^{3i}}{(3i)!}
-\frac{(-2)^{3i+1}}{(3i+1)!}
\right)\\
&=
\sum_{i=0}^N
c_i\,3(i+1)\frac{F(-2)^{3i}}{(3i+1)!}.
\end{aligned}
\tag{5.4}
$$



If $i<N$, the factorial quotient in (5.4) contains $3N$, so the corresponding summand is divisible by $9$. The terminal summand is


$$
3(N+1)(-2)^{3N}.
$$


Since $(-2)^3=-8\equiv1\pmod9$,


$$
\boxed{u^Tw\equiv3(N+1)\pmod9.}
\tag{5.5}
$$



### 5.2 The quadratic contraction

All residue-$(0,1)$ cross terms vanish modulo $9$, by
$\gamma_{3s+1}\equiv0\pmod9$.

For $s=i+j$, the sum of the residue-$(0,0)$ and residue-$(1,1)$ entries is, by Lemma 3.1,


$$
\binom{s}{i}
\left(\gamma_{3s}+(2+3s)\gamma_{3s+2}\right)
\pmod9.
$$


Equations (2.3)–(2.4) reduce this to


$$
3s\binom{s}{i}\pmod9.
$$


Thus


$$
w^T\mathsf T_nw
\equiv
3\sum_{i,j=0}^N c_ic_j(i+j)\binom{i+j}{i}
\pmod9.
\tag{5.6}
$$



Let $D_N=\operatorname{diag}(0,1,\ldots,N)$. The integer sum in (5.6) is


$$
c^T(D_NZ+ZD_N)c.
$$


Using $Zc=e_N$, it equals


$$
2c^TD_Ne_N=2N.
$$


Therefore


$$
\boxed{w^T\mathsf T_nw\equiv6N\pmod9.}
\tag{5.7}
$$



Finally $F$ is divisible by $3$, because $n\ge5$. Substituting (5.5) and (5.7) into (5.3),


$$
\eta_n\equiv-6(N+1)+6N=-6\equiv3\pmod9.
$$


This proves both claims. ∎

### Scope clarification

The exceptional auxiliary order $n=2$ has


$$
\eta_2=-\frac12,
$$


so $v_3(\eta_2)=0$. The condition $n\ge5$ is necessary for the stated theorem.

The finite probes supplied with the assignment agree with Theorem 5.1, but they are not used to establish it.

---

# Part II. The complete-force numerator

## 6. An exact simplification of $\chi_n$

Retain the actual core


$$
Q_c=(y+1)x^A(\beta+3y),
\qquad
\beta=-71-A.
$$


Put


$$
b_c=\beta+3=-68-A.
$$


Then


$$
Q_c=3x^n+(b_c+6)x^{n-1}+2b_cx^{n-2}.
$$



The whole normalized producer force is


$$
\begin{aligned}
\tau_a={}&
3n\binom{n+a}{a}\gamma_{n+a}\\
&+(b_c+6)\binom{n-1+a}{a}\gamma_{n-1+a}\\
&+\frac{2b_c}{n-1}\binom{n-2+a}{a}\gamma_{n-2+a},
\qquad0\le a<n.
\end{aligned}
\tag{6.1}
$$



Define the actual next positive-moment column


$$
k_a=\binom{n+a}{a}\gamma_{n+a},
\qquad0\le a<n,
$$


and


$$
z^+=\mathsf T_n^{-1}k,\qquad
\sigma_n=u^Tz^+.
$$



Because the last two terms in (6.1) are actual columns of $\mathsf T_n$,


$$
\boxed{
\mathsf T_n^{-1}\tau
=
3n z^+
+(b_c+6)e_{n-1}
+\frac{2b_c}{n-1}e_{n-2}.
}
\tag{6.2}
$$



Moreover,


$$
u_{n-2}=-\frac{n-1}{2}u_{n-1}.
$$


Taking the contraction with $u$ in (6.2) therefore gives the exact identity


$$
\boxed{
\chi_n=3n\sigma_n+6u_{n-1}
=3\bigl(n\sigma_n+2u_{n-1}\bigr).
}
\tag{6.3}
$$



This is an exact cancellation in the **complete force**. Neither of the lower-degree force terms has been discarded. Their entire contribution has been evaluated, and the dependence on $b_c$ cancels in this particular scalar.

---

## 7. Exact valuation of $\chi_n$ and the scalar quotient

### Theorem 7.1 — Complete numerator and scalar response

For every $n\ge5$ with $n\equiv2\pmod3$,


$$
\boxed{\chi_n\equiv3\pmod9,}
\tag{7.1}
$$


and hence


$$
\boxed{
v_3(\chi_n)=1,\qquad
\xi_n=\frac{\chi_n}{\eta_n}\in1+3\mathbb Z_3.
}
\tag{7.2}
$$



### Proof

Continue to write $n=3N+2$. By Lemma 4.1,


$$
\sigma_n=u^T\mathsf T_n^{-1}k\equiv w^Tk\pmod3.
$$



Modulo $3$, the column $k$ is supported only in residue-$0$ rows. Indeed, a row of residue $1$ or $2$, paired with the column index $n\equiv2\pmod3$, incurs a lowest-digit carry in the binomial coefficient.

For $a=3i$,


$$
k_{3i}\equiv\binom{i+N}{i}\pmod3.
$$


Therefore


$$
\sigma_n
\equiv
\sum_{i=0}^N c_i\binom{i+N}{i}
=c^TZe_N
=1
\pmod3.
\tag{7.3}
$$



Also $n\equiv2\pmod3$ and $u_{n-1}\equiv1\pmod3$. Equation (6.3) gives


$$
\frac{\chi_n}{3}
\equiv2\cdot1+2\cdot1
\equiv1\pmod3.
$$


This proves (7.1). Theorem 5.1 gives


$$
\eta_n/3\equiv1\pmod3,
$$


so their quotient satisfies (7.2). ∎

### What this improves

Turn 5 established $\xi_n\in\mathbb Z_3$ on the original domain using the retained coefficient integrality and a terminal unit pivot.

The present argument establishes the sharper statement


$$
\xi_n\in1+3\mathbb Z_3
$$


on the larger arithmetic class $n\ge5,\ n\equiv2\pmod3$, without using the original order-six congruence.

The order-six congruence is still needed when defining the integral correction


$$
R=(3P_n-Q_c)/3^6
$$


on the original family. It is not being extended to auxiliary orders.

---

## 8. Producer determinant, inverse loss, and endpoint

### 8.1 Exact producer determinant valuation

The established rank-one determinant identity is


$$
\det C_n
=
\left(\prod_{a=0}^{n-1}(a!)^2\right)
\det\mathsf T_n\,\frac{\eta_n}{F^2}.
$$


Since $\det\mathsf T_n$ is a $3$-adic unit, Theorem 5.1 gives


$$
\boxed{
v_3(\det C_n)
=
2\sum_{a=0}^{n-2}v_3(a!)+1
\qquad(n\ge5,\ n\equiv2\pmod3).
}
\tag{8.1}
$$



This proves nonsingularity of the **producer matrix** in this arithmetic class. It says nothing by itself about nonsingularity of the later residual matrix $G_{\rm act}$.

### 8.2 Exact inverse loss in the shifted producer coordinates

Let


$$
\mathsf J=\operatorname{diag}(a!)_{0\le a<n},
\qquad
v=\mathsf T_n^{-1}u.
$$


The actual signed shifted matrix satisfies


$$
\Gamma_n^{-1}
=
\mathsf J^{-1}
\left(\mathsf T_n^{-1}+\frac{vv^T}{\eta_n}\right)
\mathsf J^{-1}.
\tag{8.2}
$$



The middle matrix has entries in $3^{-1}\mathbb Z_3$. Its terminal diagonal entry has valuation exactly $-1$, because


$$
v_{n-1}\equiv-1\equiv2\pmod3
$$


by the explicit lift (4.1), whereas $\eta_n$ has valuation $1$.

Thus


$$
\boxed{
\min_{a,b}v_3\bigl((\Gamma_n^{-1})_{ab}\bigr)
=-2v_3(F)-1,
}
\tag{8.3}
$$


attained at $(n-1,n-1)$.

This producer inverse loss must not be confused with the separate loss-one estimate for the later eliminated block.

### 8.3 Sharp actual endpoint valuation

Write


$$
\mathcal E_n=3P_n-Q_c=\sum_{a=0}^{n-1}e_ax^a.
$$


The exact coefficient and endpoint formulas remain


$$
e_a=-\frac{F}{a!}\bigl(t_a+\xi_nv_a\bigr),
\qquad
\mathcal E_n(-1)=-F^2\xi_n.
$$


Because $Q_c(-1)=0$,


$$
\boxed{
Q_n^{\rm loc}(-1)=3P_n(-1)=-F^2\xi_n.
}
\tag{8.4}
$$


Theorem 7.1 therefore yields


$$
\boxed{
v_3(Q_n^{\rm loc}(-1))=2v_3(F),
\qquad
v_3(P_n(-1))=2v_3(F)-1.
}
\tag{8.5}
$$



In particular, the actual endpoint is nonzero. It is never replaced by the zero core endpoint.

---

# Part III. A controlled recurrence for the true scalar pair

## 9. An explicit finite Pascal inverse modulo $3$

The valuation theorem already answers the first alternative in the assignment. For subsequent coefficient evaluation, it is useful to specify the finite recurrence completely.

For $n=3N+2$, group coordinates by residues $0,1,2$, with sizes


$$
N+1,\quad N+1,\quad N.
$$


For a right-hand side $f$, first form


$$
a_r=P_{m_r}^{-1}f_r
$$


using the finite inverse Pascal entries


$$
(P_m^{-1})_{ij}=(-1)^{i-j}\binom ij.
$$



The central residue-block inverse modulo $3$ is the following explicit operation:


$$
\begin{aligned}
b_{0,i}&=a_{2,i} &&(0\le i<N),\\
b_{0,N}&=a_{0,N},\\
b_1&=2a_1,\\
b_2&=(a_{0,i})_{0\le i<N}-a_2.
\end{aligned}
\tag{9.1}
$$


Finally set


$$
x_r=P_{m_r}^{-T}b_r
$$


and ungroup the original indices.

Denote this entirely specified map by $\mathscr L_n$. The finite Pascal factorization proves


$$
\boxed{\mathscr L_n(f)=\mathsf T_n^{-1}f\pmod3.}
\tag{9.2}
$$



There is no inverse of an unspecified matrix in this base step.

---

## 10. Digit lifting with an explicit stopping precision

Let $f\in\mathbb Z_3^n$ and suppose the entries of $f,\mathsf T_n$ are known modulo $3^L$. Set $s_0=0$. For $0\le r<L$, define


$$
d_r=
\mathscr L_n\left(
\frac{f-\mathsf T_ns_r}{3^r}\bmod3
\right),
$$


choosing digit representatives $0,1,2$, and put


$$
\boxed{s_{r+1}=s_r+3^rd_r.}
\tag{10.1}
$$



### Proposition 10.1

Every displayed division in (10.1) is legitimate, and


$$
\boxed{s_r\equiv\mathsf T_n^{-1}f\pmod{3^r}.}
\tag{10.2}
$$



### Proof

Inductively,


$$
f-\mathsf T_ns_r\in3^r\mathbb Z_3^n.
$$


Equation (9.2) makes the next corrected residual divisible by $3^{r+1}$. Since $\mathsf T_n$ is a unit matrix, the resulting solution is unique at each precision. ∎

The inputs are generated without any hidden $3$-adic division:

* $\gamma_r$ by (2.1), through the required finite endpoint $2n-1$;
* binomial coefficients by integer Pascal recurrence;
* $F$ by its finite factorial product;
* $u$, for example, by
  

$$
u_{n-1}=(-2)^{n-1},\qquad
  u_{a-1}=-\frac a2u_a,
$$


  where $2$ is a unit;
* $k$ by its displayed entrywise formula.

Thus (10.1) is an actual finite arithmetic algorithm, not a renaming of $\mathsf T_n^{-1}u$ or $\mathsf T_n^{-1}k$.

Its state size grows with $n$. I do **not** claim a constant-state digit automaton in $n$. The new uniform conclusion is the precision bound, together with an explicit finite solver.

---

## 11. Quadratic precision protection for the scalar pair

There is a useful further economy: scalar contractions need fewer solution digits than a direct inverse-vector calculation would suggest.

Suppose


$$
w_r\equiv\mathsf T_n^{-1}u\pmod{3^r},
\qquad
z_r\equiv\mathsf T_n^{-1}k\pmod{3^r}.
$$


Then the exact quadratic and bilinear identities imply


$$
\boxed{
\eta_n\equiv
F^2-2u^Tw_r+w_r^T\mathsf T_nw_r
\pmod{3^{2r}},
}
\tag{11.1}
$$


and


$$
\boxed{
\sigma_n\equiv
u^Tz_r+w_r^Tk-w_r^T\mathsf T_nz_r
\pmod{3^{2r}}.
}
\tag{11.2}
$$



Indeed, the respective errors are


$$
-\bigl(w_r-\mathsf T_n^{-1}u\bigr)^T
\mathsf T_n
\bigl(w_r-\mathsf T_n^{-1}u\bigr)
$$


and


$$
\bigl(\mathsf T_n^{-1}u-w_r\bigr)^T
\mathsf T_n
\bigl(\mathsf T_n^{-1}k-z_r\bigr).
$$


Both are divisible by $3^{2r}$.

### Theorem 11.1 — Uniform scalar-precision theorem

To compute


$$
\xi_n\bmod3^M
$$


for any $M\ge1$, it suffices to:

1. generate $F,u,\mathsf T_n,k$ modulo $3^{M+1}$;
2. lift the two vector solutions through
   

$$
r=\left\lceil\frac{M+1}{2}\right\rceil
$$


   digits using (10.1);
3. evaluate (11.1) modulo $3^{M+1}$;
4. evaluate (11.2) modulo $3^M$;
5. form
   

$$
\boxed{
   \xi_n
   \equiv
   \bigl(n\sigma_n+2u_{n-1}\bigr)
   \left(\frac{\eta_n}{3}\right)^{-1}
   \pmod{3^M}.
   }
   \tag{11.3}
$$



The scalar inverse in (11.3) is an ordinary unit inverse, because


$$
\eta_n/3\equiv1\pmod3.
$$



### Precision accounting

The one-digit loss is explicit:


$$
\eta_n\bmod3^{M+1}
\quad\Longrightarrow\quad
\eta_n/3\bmod3^M.
$$


There is no additional unknown loss depending on $n$.

The complete numerator is handled through the exact factorization


$$
\chi_n/3=n\sigma_n+2u_{n-1}.
$$


No separate force summand is divided approximately and then discarded.

---

## 12. Consequence for the actual terminal producer jet

Fix $p\ge1$, and put


$$
M=6+p.
$$


On the original domain,


$$
R=\frac{\mathcal E_n}{3^6}
$$


is coefficientwise integral.

Using (6.2), the exact coefficients can be written


$$
\boxed{
e_a=-\frac{F}{a!}
\left[
3n z_a^+
+(b_c+6)\mathbf1_{a=n-1}
+\frac{2b_c}{n-1}\mathbf1_{a=n-2}
+\xi_nv_a
\right].
}
\tag{12.1}
$$



Therefore a sufficient uniform procedure for $R\bmod3^p$ is:

* compute $v,z^+\bmod3^M$ by (10.1);
* compute $\xi_n\bmod3^M$, using input precision $3^{M+1}=3^{p+7}$;
* evaluate (12.1) modulo $3^M$;
* divide the **whole coefficient** $e_a$ by $3^6$.

The accepted original order-six congruence makes that last division legitimate.

Factorial saturation still reduces the output to the actual terminal set. If


$$
L_a=v_3(F/a!)\ge M,
$$


then $e_a\equiv0\pmod{3^M}$. For the remaining coefficients, only precision $M-L_a$ of the bracket in (12.1) is needed.

With the exact terminal length retained, this recovers


$$
R(y)\equiv(y+1)x^{A-\kappa_p}B_p(x)\pmod{3^p},
\qquad
\deg B_p\le\kappa_p,
$$


under the established factorial-tail and endpoint conditions.

### New conclusion

Previously, the terminal jet was bounded in length but its evaluation carried an uncertified scalar-denominator precision requirement.

That particular gap is now closed:



$$
\boxed{
\text{The actual terminal jet has a finite prescribed computation,
with exactly one scalar input digit lost.}
}
$$



This does not make the later residual bulk finite-dimensional uniformly in $n$. It makes its producer input genuinely computable at each prescribed precision.

---

# Part IV. What changes in the relative arithmetic

## 13. The audited determinant pair, with the endpoint now evaluated arithmetically

Use the independently audited Turn 7 window


$$
j\equiv81\pmod{243},
\qquad
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad
C_{16}=512\cdot17^2\,3^{15}.
$$


For sufficiently large original indices in this window, the established reduction is


$$
S_{\rm act}=-3^{14}\Upsilon
$$


on the **whole original residual space** of dimension $\nu$.

Retain the exact pair


$$
\mathcal D_0=\det\Upsilon,
$$




$$
\mathcal D_1
=
e_{\rm act}^T\operatorname{adj}(\Upsilon)e_{\rm act}
-3^{14}d_{\rm act}\det\Upsilon.
$$


The transported endpoint $e_{\rm act}$ and eliminated contraction $d_{\rm act}$ are unchanged.

When $\mathcal D_0\ne0$, the audited ratio was


$$
\frac{\beta_1}{\beta_0}
=
-\frac{3^{h-14}Q_n^{\rm loc}(-1)}4
\frac{\mathcal D_1}{\mathcal D_0}.
$$


Substituting the newly sharpened exact endpoint formula gives


$$
\boxed{
\frac{\beta_1}{\beta_0}
=
\frac{3^{h-14}F^2\xi_n}{4}
\frac{\mathcal D_1}{\mathcal D_0},
\qquad \xi_n\in1+3\mathbb Z_3.
}
\tag{13.1}
$$



Thus, if $\mathcal D_0\mathcal D_1\ne0$,


$$
\boxed{
v_3(q)
=
\max\left\{
0,\,
h-14+2v_3(F)
+v_3(\mathcal D_1)-v_3(\mathcal D_0)
\right\}.
}
\tag{13.2}
$$



The producer scalar is no longer an unknown term in this valuation. The later relative pair valuation still is.

### What cannot be inferred

The facts


$$
\eta_n\ne0,\qquad \chi_n\ne0,\qquad Q_n^{\rm loc}(-1)\ne0
$$


do not imply


$$
\mathcal D_0\ne0
\quad\text{or}\quad
\mathcal D_1\ne0.
$$



Producer nonsingularity is not residual nonsingularity. Nor does a unit producer response prevent cancellation in the complete endpoint inverse contraction.

No formal Woodbury reduction is being used to infer nonsingularity.

---

## 14. Exact remaining local obstruction and a concrete follow-on lemma

The scalar-denominator problem is solved, but it exposes the next obstruction cleanly.

A bounded terminal jet determines the producer input at fixed precision. It does not by itself control the inverse loss of the growing residual bulk or the cancellation between its endpoint contraction and the eliminated-block contribution.

A useful next lemma is therefore not another common residual zero digit.

> **Uniform terminal-input relative-return lemma.**  
> Insert the actual terminal coefficients obtained from (12.1) into the complete finite mixed force. Establish a closed return/displacement recurrence for its endpoint-sensitive contractions through the actual eliminated inverse, with an explicit inverse-loss bound. The recurrence must retain:
> * the full original residual radical;
> * the finite HIGH endpoints $d,m$;
> * the transported endpoint;
> * every boundary feature appearing in any audited bulk–boundary decomposition;
> * the complete LOW contribution.
>
> Its output must determine nonvanishing and the relative valuation of the actual determinant/cofactor pair, not merely their common divisibility.

The new scalar theorem makes this a better-posed task: all required producer digits now have a prescribed input precision. A recurrence that still treats those digits as formal unknowns is no longer necessary.

What remains unproved is the return law itself and its relative, rather than absolute, precision bound.

---

# Part V. Global normalization and whole error

## 15. Complete force, full gcd, and primitive denominator

The residual functional remains exactly


$$
\boxed{
\mathcal M(F_0)=
-\frac{3^h}{4}\mathfrak f(F_0)
+
3^h\!\!\sum_{\substack{v\ge0\\2v+1\le4n-3}}
\frac{[y^v](F_0-F_0(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^r)=(2r)!.
}
\tag{15.1}
$$



The producer-force simplification in §6 does not replace this functional or remove its factorial part, endpoint subtraction, or finite cutoff.

Restore


$$
Q_n=\lambda Q_n^{\rm loc},
\qquad
R_{\rm rat}=\frac{4\lambda}{3^h}G_{\rm act},
$$


and


$$
H_{\rm complete}
=
R_{\rm rat}+(e+\pi)Q_n(-1)vv^T.
$$


Retain


$$
\beta_0=\det R_{\rm rat},
\qquad
\beta_1=Q_n(-1)v^T\operatorname{adj}(R_{\rm rat})v.
$$



For a clearing integer $\ell$, with $k=m+1$, put


$$
A_\ell=\ell^k\beta_0,\qquad
B_\ell=\ell^k\beta_1,
$$


and preserve the **full all-prime gcd**


$$
\boxed{g_\ell=\gcd(|A_\ell|,|B_\ell|).}
\tag{15.2}
$$



When $B_\ell\ne0$, the actual primitive approximation is


$$
q=\frac{|B_\ell|}{g_\ell},
\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


Its whole evaluated error is


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell^k}{g_\ell}
\det H_{\rm complete}.
}
\tag{15.3}
$$



Neither the exact scalar valuation nor the terminal-jet algorithm determines the all-prime gcd. Neither proves that the whole error is nonzero and tends to zero on the same original indices.

---

# Part VI. Bounded exact arithmetic and proof status

## 16. Proposed bounded verification

No computation is needed for Theorems 5.1 and 7.1. Their proofs are symbolic and uniform.

A useful independent finite audit would check the scalar law and the actual recurrence rather than rerun LOW isotropy.

### Inputs

Use the auxiliary orders


$$
\boxed{
n=3N+2\quad(1\le N\le27),
\qquad\text{and }n=245.
}
$$


The last input has $v_3(n-2)=5$, but it is still an **auxiliary order**, not an original index $4^j+1$.

Use modulus


$$
3^{11},
$$


so the target scalar quotient precision is $3^{10}$.

For each input:

1. generate $\gamma_0,\ldots,\gamma_{2n-1}$ from the exact recurrence;
2. construct the actual $\mathsf T_n,F,u,k$;
3. construct the explicit vector $w$ from (4.1);
4. lift the $u$- and $k$-solutions through six digits by (10.1);
5. compute $\eta_n\bmod3^{11}$ from (11.1);
6. compute $\chi_n/3\bmod3^{10}$ from (11.2) and (6.3);
7. compute $\xi_n\bmod3^{10}$;
8. independently compare with a direct modular inverse of the actual $\mathsf T_n$.

For the small orders $n\le32$, an additional exact rational check of the original signed producer formulas is reasonable. No order-six congruence should be assumed for these auxiliary inputs.

### Expected verifiable output

For every listed input:



$$
\mathsf T_nw\equiv u\pmod3,
$$




$$
u^Tw\equiv3(N+1)\pmod9,
$$




$$
w^T\mathsf T_nw\equiv6N\pmod9,
$$




$$
\boxed{\eta_n\equiv3\pmod9,\qquad
\chi_n\equiv3\pmod9,\qquad
\xi_n\equiv1\pmod3.}
$$



The certificate should also report:

* agreement of the lifted and direct modular scalar pairs through modulus $3^{11}$;
* agreement of the scalar quotient through modulus $3^{10}$;
* the complete-force identity
  

$$
u^T\mathsf T_n^{-1}\tau
  =3n\,u^T\mathsf T_n^{-1}k+6u_{n-1};
$$


* for the exact small-order cases, agreement of the producer determinant valuation with (8.1) and of the endpoint with (8.4).

Such a calculation would verify only those finite instances and the implementation of the recurrence. The uniform law rests on the proofs above.

---

## 17. Proof-status ledger

| Statement | Status |
|---|---|
| Normalized even-moment unit theorem | Reused at its established finite-order scope |
| Actual moment identities modulo $9$ | Proved here |
| Explicit Pascal inverse lift respecting the shortened class | Proved here |
| $\eta_n\equiv3\pmod9$ for all $n\ge5,\ n\equiv2\pmod3$ | Proved here |
| Exact complete-force reduction $\chi_n=3n\sigma_n+6u_{n-1}$ | Proved here |
| $\chi_n\equiv3\pmod9$, $\xi_n\in1+3\mathbb Z_3$ | Proved here |
| Exact producer determinant valuation and inverse loss | Derived here |
| Sharp actual endpoint valuation $2v_3(F)$ | Derived here |
| Explicit finite Pascal digit recurrence for the true scalar pair | Proved here |
| Uniform one-digit scalar denominator loss | Proved here |
| Terminal-jet computation at prescribed precision | Proved using the accepted original order-six interface and saturation conditions |
| Turn 8 refined propagation, $\mathcal Q\in27M$, and boundary decomposition | Not used; independent audit remains pending |
| Actual residual determinant/cofactor nonvanishing | Unresolved |
| Uniform relative residual valuation law | Unresolved |
| Full final gcd and whole nonzero error tending to zero | Unresolved |

## Closing conclusion

The proposed smaller object is decisive for the **producer-precision problem**:



$$
\boxed{
v_3(\eta_n)=v_3(\chi_n)=1,\qquad
\xi_n\in1+3\mathbb Z_3
}
$$


throughout the original family, indeed throughout all $n\ge5$ with $n\equiv2\pmod3$.

This supplies an exact scalar denominator law, a sharp endpoint valuation, and a finite prescribed computation of the actual terminal jet with every denominator loss paid. It removes the previously unknown scalar precision requirement rather than adding another common residual zero digit.

The exact remaining local bottleneck is the **nonvanishing and relative valuation of the actual residual determinant/cofactor pair**, with the full radical and transported endpoint retained. The exact remaining global bottleneck is the actual primitive denominator after the full all-prime gcd, compared with the whole nonzero same-index evaluated error.



$$
\boxed{\text{An unconditional proof or disproof of irrationality of }e+\pi
\text{ remains unresolved.}}
$$


