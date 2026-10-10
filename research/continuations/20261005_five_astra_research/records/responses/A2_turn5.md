> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 turn 5: audit passed, the two $b=5$ root disks closed, and an exact growing-family $3$-adic cancellation law

The fixed-$3$ theorem in A5 turn 4 **passes the independent arithmetic audit**, for the actual two-column $B$-metric center and the stated contact order $2n+b$. In particular, its contact reduction, both forcing columns, divided reconstruction, local saturation, and final denominator formula are correct.

There is a stronger result on the **same unbounded family**:


$$
n=2001\,3^a,\qquad b=3^a,\qquad a\ge1,\qquad m_w=1.
$$


Writing A5’s complete contractions as


$$
\mathfrak D=z^T\Omega z,\qquad
\mathfrak C=z^T\Omega v,
$$


I prove


$$
\boxed{
v_3(\mathfrak C)=v_3(b!)+1=\frac{b+1}{2}.
}
\tag{1}
$$


This resolves the previously unknown $\chi$, rather than merely bounding it. It also proves that the complete two-column lift is $3$-integral, so its least common denominator satisfies $v_3(d_B)=0$. Consequently,


$$
\boxed{
v_3(q_n)=n-\frac{b+13}{2}
}
\tag{2}
$$


for every $a\ge1$. The complete cross contraction is nonzero at every one of these indices.

Separately, the supplied prime-square data and the audited restricted-analytic expansion prove that the genuine matched-$b=5$ disks contain unique simple roots


$$
\boxed{\nu_2\in9+49\mathbb Z_7,\qquad
       \nu_3\in24+49\mathbb Z_7.}
\tag{3}
$$


Their exact local valuation law is proved below. No logarithmic bound on integer proximity to these roots is claimed.

These results do not decide the irrationality of $e+\pi$.

---

## 1. Independent audit of the growing actual center

### 1.1 Contact order and endpoint substitution: pass

This is the two-dimensional, endpoint-matched $B$-coefficient plane with contact order


$$
M=2n+b.
$$


It must not be confused with the one-dimensional matched endpoint construction of contact order $2n+b+1$, used in the fixed-$b=5$ part of this report.

For


$$
A(1)=P,\qquad B(1)=C(1)=Q,
$$


write, using primes here as polynomial labels,


$$
A=(z-1)A'+P,\quad
B=(z-1)B'+Q,\quad
C=(z-1)C'+Q.
$$


Then


$$
A+e^zB+FC=O(z^M)
$$


is equivalent to


$$
A'+e^zB'+FC'
\equiv
\frac{P+Q(e^z+F)}{1-z}\pmod {z^M}.
\tag{4}
$$


The sign on the right is positive. Multiplication or division by $1-z$, a unit at zero, preserves the contact order.

With


$$
\phi(z)=1-z+\frac{z^2}{2},\qquad F'(z)=\frac2{\phi(z)},
$$


application of $\phi^nD^n$ eliminates $A'$. It sends $FC'$, for $\deg C'<n$, to a polynomial of degree at most $n-1$:

* its denominator divides $\phi^n$, so the product is polynomial;
* near infinity, $F$ has a constant plus a Laurent series in negative powers;
* after $n$ derivatives, $C'F$ is $O(z^{-n-1})$;
* multiplication by $\phi^n=O(z^{2n})$ leaves degree at most $n-1$.

The map


$$
C'\longmapsto \phi^nD^n(C'F)
$$


is injective: a zero image would imply that $C'F$ is polynomial, contrary to the nonzero logarithmic singularities of $F$ at the roots of $\phi$, unless $C'=0$. Its domain and target both have dimension $n$, so it is an isomorphism over $\mathbb Q$.

Thus precisely the coefficients of degrees


$$
n,n+1,\ldots,n+b-1
$$


give the $b$ equations determining $B'$. The index count is correct.

### 1.2 Both forcing columns and all factorial shifts: pass

Put


$$
g=(1+D)^nB',\qquad g(z)=\sum_{j=0}^{b-1}g_jz^j.
$$


The contact matrix is


$$
N_{ij}=\sum_{s=0}^{\min(2n,n+i)}
a_s(n)(n+i)^{\underline{j+s}},
\qquad 0\le i,j<b,
\tag{5}
$$


where terms with $j+s>n+i$ vanish. This follows directly from


$$
(n+i)![z^{n+i}]e^z\phi(z)^n z^j.
$$



The two right-hand sides are exactly


$$
f_i=(n+i)![z^{n+i}]\phi^nD^n\frac1{1-z},
$$




$$
h_i=(n+i)![z^{n+i}]\phi^nD^n\frac{e^z+F}{1-z}.
\tag{6}
$$


No endpoint or forcing column is omitted.

For the $P$-column,


$$
f=\lambda f^0,\qquad
\lambda=\frac{(n!)^2}{2^n},
$$


with


$$
f_i^0=\frac{(n+i)!}{n!}
[t^n](1+2t+2t^2)^n(1+t)^i.
\tag{7}
$$


The coefficient transformation in the source has the correct factorial shift and factor $2^{-n}$.

For the $Q$-column, let


$$
\mathcal D_m=m!\sum_{r=0}^m\frac1{r!},
\qquad
\mathcal F_m=[z^m]\frac{F(z)}{1-z}.
$$


Then


$$
h_i^e=\sum_s a_s(n)(n+i)^{\underline s}\,
                     \mathcal D_{2n+i-s},
$$




$$
h_i^F=\sum_s a_s(n)(n+i)^{\underline s}\,
                     (2n+i-s)!\mathcal F_{2n+i-s}.
\tag{8}
$$


In these sums,


$$
n\le 2n+i-s\le 2n+b-1.
\tag{9}
$$



The rational logarithmic forcing causes no hidden odd-prime denominators after the displayed factorial multiplication. Indeed, if


$$
\phi(z)^{-1}=\sum_{r\ge0}c_rz^r,\qquad c_r\in\mathbb Z[1/2],
$$


then


$$
[z^r]F(z)=\frac{2c_{r-1}}r,
$$


and therefore


$$
m!\mathcal F_m
=\sum_{r=1}^m \frac{2m!}{r}c_{r-1}\in\mathbb Z[1/2].
\tag{10}
$$


More quantitatively,


$$
v_3(m!\mathcal F_m)
\ge v_3(m!)-\lfloor\log_3m\rfloor.
\tag{11}
$$


This bound applies to the **whole** logarithmic coefficient, not just one term.

### 1.3 Growing-dimensional divided-column divisibility: pass

Let


$$
D_b=\operatorname{diag}(0!,1!,\ldots,(b-1)!),
\qquad \widetilde N=ND_b^{-1}.
$$


Then


$$
\widetilde N_{ij}
=\sum_s a_s(n)(n+i)^{\underline s}
                 \binom{n+i-s}{j}.
\tag{12}
$$


For $s\ge1$,


$$
s\,a_s(n)
=n[z^{s-1}]\phi'\phi^{n-1},
$$


and hence


$$
a_s(n)(n+i)^{\underline s}
=
n(s-1)!\binom{n+i}{s}
[z^{s-1}]\phi'\phi^{n-1}.
\tag{13}
$$


Thus


$$
\boxed{\widetilde N=B(n)+nC,\qquad C\in M_b(\mathbb Z[1/2]),}
\tag{14}
$$


where $B(n)_{ij}=\binom{n+i}{j}$.

Vandermonde’s identity factors


$$
B(n)=P_bT_b(n),\qquad
(P_b)_{ir}=\binom ir,\quad
(T_b(n))_{rj}=\binom n{j-r}.
$$


Both triangular factors have determinant one. Consequently,


$$
3\mid n\quad\Longrightarrow\quad
\widetilde N\in\operatorname{GL}_b(\mathbb Z_3).
\tag{15}
$$


Nothing in this argument bounds $b$ by a fixed constant. The conclusion remains valid as $b=3^a$ grows.

The Frobenius recursion and inverse-lifting formulas in A5 are also valid. In particular, their role is to compute an already proved unit matrix to prescribed precision; they are not substitutes for the proof of (15).

### 1.4 Divided reconstruction and the actual metric: pass

In divided coefficients, differentiation is the shift $S$, so


$$
(1+S)^{-n}
=\sum_{r=0}^{b-1}\binom{-n}{r}S^r
$$


has integral entries. Multiplication by $z-1$ is


$$
(\mathcal Zt)_j=j\,t_{j-1}-t_j.
\tag{16}
$$



Set


$$
y=\widetilde N^{-1}f^0,\qquad
y^Q=\widetilde N^{-1}(h^e+h^F),
$$




$$
z=KD_b^{-1}y,\qquad
u=\lambda z,\qquad
v=e_0+KD_b^{-1}y^Q.
\tag{17}
$$


These are the actual two columns:


$$
\boldsymbol e u=0,\qquad \boldsymbol e v=1.
$$



For $\ell=n+2$ and $\omega_j=\ell^{\underline j}$,


$$
\omega_j\frac{(\mathcal Zt)_j}{j!}
=\binom{\ell}{j}(\mathcal Zt)_j.
\tag{18}
$$


Thus the claimed integral reconstruction uses the actual falling metric, with no change of weights.

### 1.5 Norm, saturation, and final quotient: pass

On the assigned family, put


$$
k=v_3(n)=a+1,\quad F_n=v_3(n!),\quad
s=v_3((b-1)!).
$$


For $1\le r<b$,


$$
v_3\binom nr\ge k-v_3(r)\ge2,
$$


and the analogous bound holds for $\binom{-n}{r}$. Therefore


$$
\widetilde N\equiv P_b\pmod9,\qquad
(1+S)^{-n}\equiv I\pmod9.
\tag{19}
$$



The constant-term Lucas argument gives $J_0\in\mathbb Z_3^\times$, and the first three entries are


$$
(y_0,y_1,y_2)\equiv(J_0,0,J_0)\pmod9.
$$


The complete weighted zero-endpoint vector begins


$$
(\omega_0z_0,\omega_1z_1,\omega_2z_2)
\equiv(-J_0,2J_0,-J_0)\pmod9.
\tag{20}
$$


For $3\le j\le b$,


$$
v_3\binom{n+2}{j}
=k-v_3(j(j-1)(j-2))\ge1.
\tag{21}
$$


Consequently,


$$
\boxed{\mathfrak D=z^T\Omega z\equiv6J_0^2\pmod9,\qquad
v_3(\mathfrak D)=1.}
\tag{22}
$$



The top coefficient satisfies


$$
z_b=\frac{y_{b-1}}{(b-1)!},\qquad y_{b-1}\in\mathbb Z_3^\times.
$$


All earlier ordinary coefficients have valuation at least $-s$. Hence


$$
\min_jv_3(z_j)=-s,
$$


and the primitive zero-endpoint norm has valuation $2s+1=b-2a$, as claimed.

For the saturation audit, normalize


$$
\zeta=z/z_b,\qquad w=v-v_b\zeta.
$$


Then $\zeta$ is integral, $\zeta_b=1$, $\boldsymbol e\zeta=0$, while $w_b=0$ and $\boldsymbol e w=1$. A vector $c\zeta+Qw$ is integral exactly when


$$
c\in\mathbb Z_3,\qquad Q\in3^\mu\mathbb Z_3,
\quad
\mu=\max(0,-\min_jv_3(w_j)).
\tag{23}
$$


This proves the stated saturation of the **$B$-coefficient plane**. It is not an assertion that all reconstructed $A$- and $C$-coefficients are simultaneously integral.

The endpoint coordinates on $\zeta,3^\mu w$ are


$$
\xi=(\lambda z_b)^{-1},\qquad
\eta=-3^\mu v_b(\lambda z_b)^{-1}.
\tag{24}
$$


They give the denominator and scalar valuations in A5 without an extra assumed primitiveness condition. In particular, the minimal common endpoint denominator forces one endpoint numerator to be a unit.

Finally, the center sign is correct:


$$
\mathfrak c_n
=\frac{u^T\Omega v}{u^T\Omega u}
=\frac{\mathfrak C}{\lambda\mathfrak D},
\qquad
\mathfrak C=z^T\Omega v.
\tag{25}
$$


It is the negative of the minimizing $A$-endpoint at $Q=1$, which is the sign appropriate to approximation of $e+\pi$.

Let


$$
N_B=d_B[u,v],
$$


where $d_B$ is the least common denominator of the full lift, and define the actual integer contractions


$$
A_B=N_{B,1}^T\Omega N_{B,1},\qquad
H_B=N_{B,1}^T\Omega N_{B,2}.
$$


With


$$
g_B=\gcd(A_B,|H_B|),\qquad
p_n=H_B/g_B,\qquad q_n=A_B/g_B,
\tag{26}
$$


the pair is primitive. If $d=v_3(d_B)$ and $\chi=v_3(\mathfrak C)$, then


$$
v_3(A_B)=2d+4F_n+1,\qquad
v_3(H_B)=2d+2F_n+\chi.
$$


Therefore


$$
\boxed{
v_3(q_n)=\max(0,2F_n+1-\chi).
}
\tag{27}
$$


This is an evaluated final-gcd calculation, not a symbolic-content calculation.

**Audit verdict:** the growing-center arithmetic theorem passes. Its original $\chi\ge2$ argument is valid. Sections 3–4 below strengthen it to an exact value.

---

## 2. The genuine matched-$b=5$ root disks

Here the family is the distinct fixed-degree construction


$$
(n,5,n),\qquad n\ge5,\qquad\text{contact order }2n+6.
$$



### 2.1 All-depth convergence audit

The scalar functions in A2 turn 4 are defined through


$$
a_s(x)=[z^s]\phi(z)^x,\qquad
\mathscr D(x)=\sum_{j\ge0}(x)_j,
$$


and


$$
\begin{aligned}
h(x)&=\sum_s(x)_sa_s(x),\\
u(x)&=\sum_s(x)_{s+1}a_s(x),\\
v(x)&=\sum_s(x)_{s+2}a_s(x),\\
\mathcal A(x)&=\sum_s(x)_sa_s(x)\mathscr D(2x-s),\\
\mathcal M(x)&=\sum_s(x)_sa_s(x)\mathscr D(2x+1-s).
\end{aligned}
\tag{28}
$$



For $x=r+pT$, write $m=\lfloor s/p\rfloor$. Expanding $a_s$ in binomial polynomials gives


$$
v_{\rm G}\!\left((r+pT)_{s+d}\binom{r+pT}{j}\right)
\ge m-v_p(m!),\qquad d=0,1,2,\quad j\le s.
\tag{29}
$$


The right side tends to infinity for every odd $p$. Also


$$
v_{\rm G}((a+pcT)_j)\ge\lfloor j/p\rfloor.
$$


These bounds prove coefficientwise convergence in the Tate algebra:


$$
(h,u,v,\mathcal A,\mathcal M)(r+pT)
\in\mathbb Z_p\langle T\rangle^5.
\tag{30}
$$


They also justify the all-depth finite truncation bounds stated in the source. Thus the analytic extension does not rest merely on integer congruence transfer.

For $p\ge5$ and $2r<p$, the range $p\le s<2p$ contributes the scalar carry


$$
pT^2\mathbf S_r.
$$


The reason is the product of the two congruences


$$
a_{p+j}(r+pT)\equiv-T a_j(r)\pmod p,
$$




$$
\frac{(r+pT)_{p+j+d}}p
\equiv-T(r)_{j+d}\pmod p
$$


when $j+d\le r$; otherwise the second expression vanishes modulo $p$. Terms with $s\ge2p$ vanish modulo $p^2$.

Hence the audited scalar expansion is


$$
\mathbf S(r+pT)
=\mathbf S_r+pT\mathbf L_r+pT^2\mathbf S_r
+p^2\mathbf E_r(T),
\tag{31}
$$


with $\mathbf E_r$ restricted analytic.

The fixed $b=5$ contraction polynomial $\mathcal V$ is homogeneous of degree six in the five scalar coordinates. Euler’s identity therefore makes the carry contribution


$$
6pT^2\widetilde V_r.
$$


At $r=2,3$, the supplied root residues satisfy $7\mid\widetilde V_r$. Thus


$$
\boxed{
\widetilde V(r+7T)
=\widetilde V_r+7\Lambda_rT+49G_r(T),
\quad G_r\in\mathbb Z_7\langle T\rangle.
}
\tag{32}
$$


The restricted-analytic and carry arguments pass the audit.

### 2.2 The supplied seed arithmetic determines both disks

The four supplied rows give


$$
\widetilde V_2\equiv7,\quad
\widetilde V_9\equiv0,\quad
\widetilde V_3\equiv35,\quad
\widetilde V_{10}\equiv7\pmod{49}.
$$


These residues also agree directly with


$$
\widetilde V=\widetilde\sigma\mathcal A
-\widetilde\chi(\mathcal M+h-u)-\widetilde\kappa
$$


using the supplied scalar and contraction rows.

Therefore


$$
(\beta_2,\Lambda_2)=(1,6),\qquad
(\beta_3,\Lambda_3)=(5,3)\pmod7,
\tag{33}
$$


where $\beta_r=\widetilde V_r/7$.

Both slopes are units. The unique first lifts are


$$
T_2\equiv-1\cdot6^{-1}=1\pmod7,
$$




$$
T_3\equiv-5\cdot3^{-1}=3\pmod7.
$$


Thus the two roots have exactly the locations in (3).

### 2.3 Unique all-depth roots and exact valuations

Define


$$
f_r(T)=\frac{\widetilde V(r+7T)}7
=\beta_r+\Lambda_rT+7G_r(T).
$$


For $t,u\in\mathbb Z_7$,


$$
G_r(t)-G_r(u)=(t-u)H_r(t,u),
\qquad H_r(t,u)\in\mathbb Z_7.
$$


Consequently,


$$
f_r(t)-f_r(u)
=(t-u)\bigl(\Lambda_r+7H_r(t,u)\bigr).
\tag{34}
$$


The factor in parentheses is a unit. Hensel lifting gives one root $T_r$, and (34) gives


$$
v_7(f_r(t))=v_7(t-T_r).
$$


Putting $\nu_r=r+7T_r$, we obtain


$$
\boxed{
v_7(\widetilde V(n))=v_7(n-\nu_r),
\qquad n\in r+7\mathbb Z_7,\quad r=2,3.
}
\tag{35}
$$



The inherited evaluated-content result says that the full contraction gcd $d_n$ is a $7$-unit. Therefore, at the ordinary integer indices of the fixed-$b=5$ family,


$$
\boxed{
v_7(V_n^*)=v_7(n-\nu_r)
\quad(n\ge5,\ n\equiv r\pmod7).
}
\tag{36}
$$


In particular, the six nonroot lifts in each disk have exact valuation one:


$$
\begin{array}{ll}
r=2:&n\equiv2,16,23,30,37,44\pmod{49},\\
r=3:&n\equiv3,10,17,31,38,45\pmod{49}.
\end{array}
\tag{37}
$$



The inherited all-index nonvanishing at $19$ shows that neither $\nu_r$ is a nonnegative integer. It does not identify either root as rational or algebraic over $\mathbb Q$, and (35) does not imply $O(\log n)$ integer proximity.

### 2.4 The final denominator is still the endpoint gcd

For clarity, this root classification does not replace the actual denominator by $V_n^*$. Retain


$$
S_n^*=Q_n^*+\frac{2^{n+1}}{(n!)^2}V_n^*,
\qquad c_n=-\frac{S_n^*}{D_n^*}.
$$


For any valid integral clearer $\lambda_n$,


$$
N_n=\lambda_nS_n^*,\qquad Z_n=\lambda_nD_n^*,
$$


and, on $D_n^*\ne0$,


$$
\boxed{
q_n=\frac{|Z_n|}{\gcd(|N_n|,|Z_n|)},\qquad
p_n=-\operatorname{sign}(Z_n)
       \frac{N_n}{\gcd(|N_n|,|Z_n|)}.
}
\tag{38}
$$


Near a deep root approach, the exact $7$-adic expression remains


$$
v_7(q_n)
=
\max\!\left(
0,\,
2v_7(n!)+v_7(D_n^*)
-v_7\!\left(V_n^*+\frac{(n!)^2}{2^{n+1}}Q_n^*\right)
\right),
\tag{39}
$$


when the complete numerator is nonzero.

The inherited fixed-$b$ whole-error theorem supplies eventual nonvanishing of $c_n-(e+\pi)$ and of the relevant endpoint. I do not recompute the already established density exclusion.

---

## 3. New quantitative lemma: exact complete $Q$-column cancellation

Return now to the growing two-column center. Define


$$
F_b=v_3(b!)=\frac{b-1}{2},\qquad
L=F_b+1=\frac{b+1}{2},\qquad
U_b=\frac{b!}{3^{F_b}}\in\mathbb Z_3^\times.
\tag{40}
$$



The key new statement is a reconstruction congruence for the **complete** $Q$-forcing.

### Theorem
Let


$$
t^Q=(1+S_b)^{-n}\widetilde N^{-1}(h^e+h^F)
$$


be the divided coefficients of the actual polynomial $B'$ for endpoint pair $(P,Q)=(0,1)$. Then


$$
\boxed{
t_j^Q\equiv
\bigl(1+2U_b3^L\bigr)j!
\pmod{3^{L+1}},
\qquad 0\le j<b.
}
\tag{41}
$$



This is uniform in the growing dimension $b=3^a$. The proof follows.

### 3.1 An infinite divided-coefficient comparison sequence

Define integers


$$
G_j=\sum_{r=0}^n\binom nr(j+r)!,
\qquad j\ge0.
\tag{42}
$$


They are the divided coefficients of


$$
(1+D)^n\frac1{1-z}.
$$


Besides $v_3(G_j)\ge v_3(j!)$, they satisfy the stronger divisibility


$$
\boxed{G_j-j!\in n\,j!\mathbb Z.}
\tag{43}
$$


Indeed, for $r\ge1$,


$$
\binom nr\frac{(j+r)!}{j!}
=
n\binom{n-1}{r-1}(r-1)!\binom{j+r}{r},
$$


which is an integer multiple of $n$.

Extend the divided contact matrix to all columns $j\ge0$:


$$
\mathcal N_{ij}
=\sum_s a_s(n)(n+i)^{\underline s}
                    \binom{n+i-s}{j}.
\tag{44}
$$


Its entries vanish for $j>n+i$, and its first $b$ columns are $\widetilde N$. The proof of (14) applies to every extended column:


$$
\mathcal N_{ij}=\binom{n+i}{j}+nC_{ij},
\qquad C_{ij}\in\mathbb Z_3.
\tag{45}
$$



The identity


$$
D^n\frac{e^z}{1-z}
=e^z(1+D)^n\frac1{1-z}
$$


now gives the exact finite coefficient relation


$$
h_i^e=\sum_{j\ge0}\mathcal N_{ij}G_j.
\tag{46}
$$


Define the omitted-column remainder


$$
R_i=\sum_{j\ge b}\mathcal N_{ij}G_j.
$$


Then


$$
\boxed{
\widetilde N^{-1}h^e
=G_{<b}+\widetilde N^{-1}R.
}
\tag{47}
$$


The sign is **plus**.

### 3.2 Evaluate the omitted-column remainder at its first nonzero depth

For $b\le j<3b$ and $0\le i<b$,


$$
\mathcal N_{ij}\equiv0\pmod3.
\tag{48}
$$


To see this, reduce (45) modulo $3$. Since $n$ is divisible by $3b=3^{a+1}$, the base-$3$ digit of $n+i$ in position $a$ is zero; that digit of $j\in[b,3b)$ is one or two. Lucas’s formula makes the binomial coefficient zero.

For $j\ge b+3$,


$$
v_3(j!)\ge F_b+1.
$$


Together with (48), these columns contribute zero modulo $3^{F_b+2}=3^{L+1}$ until $j=3b$. Beyond that,


$$
v_3((3b)!)=\frac{3b-1}{2}\ge F_b+2,
$$


so integrality alone suffices.

Thus only the three columns


$$
j=b,\ b+1,\ b+2
$$


can contribute modulo $3^{L+1}$.

For $d=0,1,2$, Vandermonde’s identity gives


$$
\binom{n+i}{b+d}
\equiv
\binom{i}{d}\binom nb\pmod9.
\tag{49}
$$


Indeed, among the positive lower arguments at most $b+2$, the only one divisible by $b=3^a$ is $b$; every other $\binom nt$ has valuation at least two.

Moreover,


$$
\frac1{3}\binom nb\equiv1\pmod3.
\tag{50}
$$


Here $n/(3b)=667\equiv1\pmod3$, and
$\binom{n-1}{b-1}\equiv1\pmod3$.

Using (43), (45), and $k\ge2$, we therefore obtain


$$
\frac{R_i}{3^L}
\equiv
U_b\sum_{d=0}^2\binom idd!
\equiv U_b\mathcal D_i\pmod3.
\tag{51}
$$


Since $\widetilde N^{-1}\equiv P_b^{-1}\pmod3$ and


$$
\mathcal D_i=\sum_{j=0}^i\binom ijj!,
$$


equation (47) yields


$$
\boxed{
\widetilde N^{-1}h^e
\equiv G_{<b}+U_b3^L(j!)_{j<b}
\pmod{3^{L+1}}.
}
\tag{52}
$$



There is no loss proportional to the number of columns: every discarded term has the required valuation individually.

### 3.3 The second contribution comes from the truncated inverse

The infinite series


$$
\sum_{r\ge0}\binom{-n}{r}G_{j+r}
$$


converges $3$-adically, because $G_{j+r}$ is divisible by $(j+r)!$. The binomial convolution identity proves


$$
\boxed{
\sum_{r\ge0}\binom{-n}{r}G_{j+r}=j!.
}
\tag{53}
$$


One may justify rearrangement directly by substituting (42): the inner sum over $0\le s\le n$ is finite, and the factorial valuations tend to infinity.

Let


$$
E_j=\sum_{r\ge b-j}\binom{-n}{r}G_{j+r},
\qquad 0\le j<b.
$$


Then the finite reconstruction of $G_{<b}$ is


$$
\bigl((1+S_b)^{-n}G_{<b}\bigr)_j=j!-E_j.
\tag{54}
$$



As in the previous step, to compute $E_j$ modulo $3^{L+1}$, only indices $j+r=b,b+1,b+2$ matter. In the range $1\le r\le b+2$, all inverse-binomial coefficients have valuation at least two except possibly $r=b$. At that index,


$$
\frac1{3}\binom{-n}{b}\equiv-1\pmod3.
\tag{55}
$$


Consequently,


$$
\boxed{
E_j\equiv-U_b3^Lj!\pmod{3^{L+1}},
\qquad 0\le j<b.
}
\tag{56}
$$


For $j\ge3$, both sides are zero at the displayed precision.

Since $(1+S_b)^{-n}\equiv I\pmod3$, applying it to (52), and then using (54)–(56), gives


$$
(1+S_b)^{-n}\widetilde N^{-1}h^e
\equiv
j!+2U_b3^Lj!\pmod{3^{L+1}}.
\tag{57}
$$


The factor two is the sum of two distinct effects:

1. the omitted contact columns in (47);
2. the omitted inverse-reconstruction tail in (54).

They have the same sign after reconstruction.

### 3.4 The complete logarithmic forcing cannot affect this precision

From (9) and (11),


$$
v_3(h_i^F)\ge F_n-\lfloor\log_3(2n+b-1)\rfloor
=F_n-(a+7).
\tag{58}
$$


Since


$$
F_n=\frac{n-7}{2}=\frac{2001b-7}{2},
$$


we have


$$
F_n-(a+7)-(L+1)=1000b-a-12>0.
\tag{59}
$$


Both $\widetilde N^{-1}$ and the divided reconstruction are integral over $\mathbb Z_3$. Therefore the entire $h^F$ contribution vanishes modulo $3^{L+1}$.

This proves (41) for the **complete** forcing. The logarithmic part has not been removed from the rational center; its valuation has been proved too large to change this particular leading residue.

---

## 4. Exact $\chi$, actual saturation, and the final gcd

Let


$$
\widehat z_j=\omega_jz_j,\qquad
\widehat v_j=\omega_jv_j.
$$


Set $c=1+2U_b3^L$. Equation (41) gives:

* at coordinate zero,
  

$$
\widehat v_0=1-t_0^Q
  \equiv-2U_b3^L\pmod{3^{L+1}};
  \tag{60}
$$


* at every internal coordinate $1\le j<b$,
  

$$
\widehat v_j
  =\binom{n+2}{j}(jt_{j-1}^Q-t_j^Q)
  \equiv0\pmod{3^{L+1}};
  \tag{61}
$$


* at the top coordinate,
  

$$
\widehat v_b
  =\binom{n+2}{b}b\,t_{b-1}^Q
  \equiv c\,\omega_b\pmod{3^{L+1}}.
  \tag{62}
$$



The exact valuation of $\omega_b$ is


$$
v_3(\omega_b)=k+v_3((b-3)!)=F_b+1=L.
\tag{63}
$$


Also $\widehat z_b\equiv0\pmod3$, while


$$
\widehat z_0\equiv-J_0\pmod3.
$$


Thus the top-coordinate contribution to $\mathfrak C$ vanishes modulo $3^{L+1}$, and all internal contributions do as well. Only coordinate zero survives:


$$
\boxed{
\frac{\mathfrak C}{3^L}
\equiv2U_bJ_0\pmod3.
}
\tag{64}
$$


Both factors are units. Hence


$$
\boxed{\chi=v_3(\mathfrak C)=L=\frac{b+1}{2},}
$$


and $\mathfrak C\ne0$ for every $a\ge1$.

### 4.1 The full lift is $3$-integral

For $j<b$,


$$
t_j^Q=cj!+3^{L+1}r_j,\qquad r_j\in\mathbb Z_3.
$$


Since


$$
v_3(j!)\le s=F_b-a<L+1,
$$


all ordinary coefficients $t_j^Q/j!$ are integral. Therefore $v\in\mathbb Z_3^{b+1}$. Its top coefficient is


$$
v_b=\frac{t_{b-1}^Q}{(b-1)!}\in\mathbb Z_3^\times.
\tag{65}
$$


The column $u=\lambda z$ was already integral, since $2F_n-s>0$. Consequently,


$$
\boxed{v_3(d_B)=0.}
\tag{66}
$$


In the adapted saturation notation, this also proves


$$
\boxed{\mu=0,\qquad v_3(v_b)=0.}
\tag{67}
$$


Thus the previously bounded local saturation parameters are now determined.

### 4.2 Exact evaluated final-gcd depth

Using $d=0$, $\chi=L$, and $L<2F_n+1$, the actual Gram contractions satisfy


$$
v_3(A_B)=4F_n+1,\qquad
v_3(H_B)=2F_n+L.
$$


Therefore the actual final gcd is


$$
\boxed{
v_3(g_B)=2F_n+L=n+\frac{b-13}{2}.
}
\tag{68}
$$


Subtracting from $v_3(A_B)$,


$$
\boxed{
v_3(q_n)=2F_n+1-L
=n-\frac{b+13}{2}.
}
\tag{69}
$$



This includes the full evaluated cross contraction, the least lift denominator, and the final metric-dependent gcd. No high-row content or symbolic coefficient gcd has been substituted for $g_B$.

The two supplied finite controls fit the result:

* $n=6003,b=3$: $\chi=2$, $v_3(q_n)=5995$;
* $n=18009,b=9$: the new prediction is
  

$$
\boxed{\chi=5,\qquad v_3(q_n)=17998.}
  \tag{70}
$$


  The supplied modulus $81$ could not resolve this depth.

---

## 5. What this changes—and does not change—in primitive error balance

The exact rational center is


$$
\frac{p_n}{q_n}=\frac{H_B}{A_B},
\qquad
g_B=\gcd(A_B,|H_B|),
$$


with $q_n>0$. Arithmetic normality holds at every assigned index, and the new congruence proves $H_B\ne0$ at every assigned index.

For the **whole evaluated error**, retain the supplied proportional signed-rate theorem at its stated analytic dependency status. Since


$$
\frac bn=\frac1{2001},\qquad
\tau_c=\left(2+\frac1{2001}\right)\log(1+\sqrt2),
$$


it gives eventually


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi)\ne0,\qquad
\log|\epsilon_n|=-\tau_cn+o(n).
$$


Thus


$$
\boxed{
L_n=q_n(e+\pi)-p_n=-q_n\epsilon_n\ne0.
}
\tag{71}
$$



Define the exact contribution of all other primes by


$$
R_n=\sum_{p\ne3}v_p(q_n)\log p.
$$


Equation (69) gives the identity


$$
\log q_n
=
\left(1-\frac1{4002}\right)n\log3
-\frac{13}{2}\log3+R_n.
\tag{72}
$$


Consequently,


$$
\boxed{
\log|L_n|
=
R_n-
\left[
\tau_c-\left(1-\frac1{4002}\right)\log3
\right]n
-\frac{13}{2}\log3+o(n).
}
\tag{73}
$$



This is a genuine same-family improvement and an exact resolution of the assigned $\chi$-bottleneck. It is not enough to settle primitive shrinking or exclusion: the bracket is positive, approximately $0.665$, and no adequate bound for $R_n$ has been proved here.

The next arithmetic obstruction is therefore no longer an unresolved fixed-$3$ cross contraction or $3$-adic saturation. It is the actual remaining-prime contribution to the same evaluated gcd (26).

---

# Concluding ledger

## (1) New result and proof status

**Independently audited and passed**

* A5’s contact order $2n+b$, endpoint substitution, and both forcing columns.
* The rational logarithmic-forcing integrality and all factorial index bounds.
* Growing-dimensional divisibility $\widetilde N=B(n)+nC$.
* Divided reconstruction in the actual falling metric.
* The local $B$-coefficient saturation and endpoint rows.
* The exact actual-denominator formula
  

$$
v_3(q_n)=\max(0,2v_3(n!)+1-\chi).
$$



**Newly proved**

For every $a\ge1$, $n=2001\,3^a$, $b=3^a$,


$$
\boxed{
\chi=\frac{b+1}{2},\qquad
v_3(d_B)=0,\qquad
v_3(g_B)=n+\frac{b-13}{2},\qquad
v_3(q_n)=n-\frac{b+13}{2}.
}
$$


The complete cross contraction is nonzero throughout this domain.

**Root-disk classification completed**

Using the supplied finite seed data and the audited all-depth analytic expansion, the two genuine $b=5$ disks have unique simple roots


$$
\nu_2\equiv9\pmod{49},\qquad
\nu_3\equiv24\pmod{49},
$$


and exact local valuation $v_7(V_n^*)=v_7(n-\nu_r)$ at the ordinary integer indices. No $O(\log n)$ proximity claim is made.

**Not proved**

An unconditional rationality or irrationality decision for $e+\pi$; an aggregate remaining-prime estimate for the growing center; or a whole-family matched-$b=5$ exclusion.

## (2) Exact remaining bottleneck

For the growing center, the unresolved arithmetic is now precisely


$$
\sum_{p\ne3}
\left(
v_p(A_B)-\min\{v_p(A_B),v_p(H_B)\}
\right)\log p,
$$


on the same indices $n=2001\,3^a,b=3^a$, with the full $H_B$.

For the $b=5$ root disks, existence and uniqueness are settled. What remains for unrestricted integer-index denominator bounds is quantitative arithmetic control of approach to $\nu_2,\nu_3$, or a different argument that retains the complete numerator in (39).

## (3) Bounded exact computation request

**REQUEST: pro / max / high**

One extension of an existing control is sufficient:

**Inputs**


$$
n=18009,\qquad b=9,\qquad m_w=1,\qquad
\text{modulus }729=3^6.
$$


Use the defining contact coefficients and the complete $h^e+h^F$ forcing.

**Expected verifiable output**

1. The divided reconstructed $Q$-column $t^Q$, checking
   

$$
\boxed{t_j^Q\equiv487\,j!\pmod{729},\qquad 0\le j<9.}
$$


2. The full weighted vector, checking
   

$$
\boxed{
   (\omega_jv_j)_{j=0}^9
   \equiv(243,0,0,0,0,0,0,0,0,243)\pmod{729}.
   }
$$


3. The complete contractions, checking
   

$$
\mathfrak D\equiv6\pmod9,\qquad
   \boxed{\mathfrak C\equiv486\pmod{729}.}
$$


4. From these exact residues, the finite conclusions
   

$$
\chi=5,\qquad v_3(q_n)=17998,
$$


   together with confirmation that the ordinary $Q$-column is $3$-integral and its top coefficient is a unit.

This is a bounded independent check of the new leading-residue calculation. The infinite theorem above is proved by the omitted-column and inverse-tail arguments, not by this computation.
