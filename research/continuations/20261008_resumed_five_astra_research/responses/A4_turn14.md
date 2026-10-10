> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The original producer scalar and a paid finite-precision reduction of the actual source

## Abstract and proof status

The rationality or irrationality of $e+\pi$ remains unresolved.

The primary scalar obligation in this assignment can, however, be closed. At every sufficiently large original index


$$
j>0,\qquad j\equiv84645\pmod{531441},\qquad n=4^j+1,
$$


the actual producer scalar satisfies


$$
\boxed{\Xi\equiv-\frac32\equiv120\pmod{243}.}
$$


Consequently,


$$
\boxed{v_3(\Xi)=1,\qquad \frac{\Xi}{3}\equiv40\pmod{81}.}
$$


The complete forcing numerator satisfies


$$
\boxed{u^T\mathbf t\equiv-168\pmod{729},}
$$


and hence


$$
\boxed{\xi\equiv112\equiv31\pmod{81},\qquad v_3(\xi)=0.}
$$



These conclusions are not obtained by substituting a small matrix for a large matrix on the strength of a congruence of sizes. I prove an exact finite Pascal reduction theorem: modulo $3^s$, the Pascal-transformed matrix is block diagonal in blocks of length $3^s$, with the actual final incomplete block retained. The theorem is derived from the given gamma recurrence and explicit integer binomial identities. Applied with $s=5$, it legitimately reduces the relevant terminal calculation to its actual final two coordinates.

In particular, the proposed diagonal test is true:


$$
\boxed{(\widehat T_n)_{n-1,n-1}\equiv9\pmod{243}.}
$$


Thus its residue modulo $9$ is zero; more precisely, that diagonal entry has ternary valuation exactly $2$.

The scalar result makes the original 72-coefficient $V_{70}$ reduction unconditional on the retained original family. In fact, the original congruence gives a stronger tail payment:


$$
\boxed{
\delta Q-(y+1)x^{A-70}V_{70}(x)\in3^{37}\mathbb Z_3[x].
}
$$


With the complete finite $W$-projection retained, this changes the complete Schur matrix only by $3^{35}$, and the normalized prefix matrix only by $3^9$.

I also prove a bounded reconstruction lemma for the **actual** 72 producer coefficients at the precision needed by the next prefix transport. It uses:

- gamma coefficients only through index $197$;
- the original residue $4^j\bmod 3^{37}$;
- a $617$-dimensional terminal band matrix of half-bandwidth at most $197$, not an original-index factorial matrix.

This reconstruction is a proved reduction, not a performed computation or an evaluation of the next prefix return.

The secondary obligation remains open:


$$
\frac{
\mathcal M(\delta Q\,\widehat F_i\widehat F_j)
-(b_i^\delta)^TE_{\rm act}^{-1}b_j^\delta
}{3^{29}}\pmod3.
$$


The complete $W$-return, physical HIGH terminal $Y_m$, and negative endpoint remain present. The short raw producer does not establish short corrected-column support.

No different external audit is claimed here. In particular, this self-continuation is not the different full audit still required for the new statements in Turn 13.

---

## 1. Original domain, finite objects, and scope of reuse

### 1.1 The original indices are unchanged

All assertions about the research family retain


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




$$
m=2^{2j-1},\qquad n=4^j+1=2m+1,\qquad A=4^j-1=n-2,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$


with


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15},
$$


and


$$
\frac{103}{1000}<\frac{N_0}{P_0}<\frac{104}{1000}.
$$



The derived parameters remain


$$
P_0=243P=3^{h-27},\qquad N_0=243r,\qquad D=P_0+N_0,
$$




$$
P=3^{h-32},\qquad r\equiv2\pmod9,\qquad r\ \text{odd},
$$




$$
4^j=243(3^{26}-1)P-243r+1.
$$


Set


$$
x=y-1,\qquad Q=27P,\qquad b=Q-N_0=2R,\qquad \chi=P-R,\qquad c=2\chi.
$$


Thus


$$
N_0=25P+c,\qquad D=268P+c,\qquad D+b=270P.
$$



For the producer calculation it is convenient to write


$$
N=n-1=4^j.
$$


Since


$$
84645=3^4\cdot1045,\qquad 3\nmid1045,
$$


every original $j$ has $v_3(j)=4$. The lifting-the-exponent identity gives


$$
\boxed{v_3(N-1)=v_3(4^j-1)=5.}
\tag{1.1}
$$


In particular,


$$
N\equiv1\pmod{243},\qquad n\equiv2\pmod{243}.
$$


The proof below explains exactly when, and why, this size congruence can be used.

### 1.2 Complete columns and physical boundaries

Retain


$$
U_s=x^s\quad(0\le s<D),
$$




$$
z_i=x^Dy^i\quad(0\le i<\nu),\qquad \nu=D/2-1,
$$




$$
Y_t=y^t\quad(d\le t\le m),\qquad d=D+\nu,
\qquad W=[U\ Y].
$$


The highest physical HIGH column is $Y_m$.

The complete functional is


$$
\mathcal M(P)=
-\frac{3^h}{4}\mathfrak f(P)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](P-P(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^t)=(2t)!.
\tag{1.2}
$$


Its physical cutoff remains


$$
K_{\rm phys}=2n-2,
\qquad
2K_{\rm phys}+1=4H-4D+5<3^{h+1}.
\tag{1.3}
$$



For $\alpha=c,\mathrm{act}$,


$$
G_\alpha(f,g)=\mathcal M(Q_\alpha fg),\qquad
E_\alpha=G_\alpha(W,W),
$$




$$
F_\alpha[p]
=x^Dp-WE_\alpha^{-1}G_\alpha(W,x^Dp).
\tag{1.4}
$$


The core producer is


$$
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=-71-A.
$$


Equivalently,


$$
\beta+3y=b_{\rm force}+3x,\qquad b_{\rm force}=-n-66.
$$



The actual finite prefix has


$$
R_*=\frac{9Q+1}{2},\qquad
a_0=R_*-1=121P+\frac{P-1}{2}.
$$


The other boundaries are still


$$
\tau=\frac{N_0-3}{2},\qquad \ell=3R+1,
$$




$$
K=\{0,\ldots,\ell-1\},\qquad
J=\{\ell,\ldots,\tau-1\},\qquad R_*+\tau=\nu.
$$


No last middle column is removed.

### 1.3 What is reused, and what is not re-audited

The complete prefix theorem


$$
\mathscr H^TZ_\alpha^T\mathsf A_\alpha Z_\alpha\mathscr H\in27M,
\qquad \alpha=c,\mathrm{act},
\tag{1.5}
$$


has passed its different complete audit and is reused. Its proof and the closed 122-constant calculation are not repeated.

The nine evaluated leading inverse-image bands are also reused:


$$
\mathcal S=\{14,15,16,41,42,43,95,96,97\},
$$




$$
C(Y)=2Y^{14}(1-Y)^2(1+Y^{27}+Y^{81})
      =2\sum_{r\in\mathcal S}Y^r
      \quad\text{in }\mathbb F_3[Y].
\tag{1.6}
$$



The Turn 13 complete source-$81$ cancellation and fourth-residual-digit contraction remain at their stated review status. The producer proof below does not require those results. It does not certify a different audit of them, of the Turn 12 $J$-theorem, or of any whole seventh-order assembly.

The paid bounds for the complete finite projection, in particular


$$
E_\alpha^{-1}\in3^{-1}\operatorname{Mat}(\mathbb Z_3),
\tag{1.7}
$$


are reused at their original scope.

---

# Part I. A finite Pascal theorem from the exact gamma recurrence

## 2. The forcing matrix and the actual scalar

The source definitions are


$$
F_{\rm fac}=N!,
$$




$$
\gamma_0=1,\qquad \gamma_1=0,\qquad
\gamma_{r+1}=(4r+2)\gamma_r+4\gamma_{r-1}\quad(r\ge1),
$$




$$
T_n(a,b)=\binom{a+b}{a}\gamma_{a+b},
\qquad 0\le a,b<n.
\tag{2.1}
$$



Let


$$
\mathcal P_n(a,b)=\binom ab
$$


be the finite lower Pascal matrix, and define


$$
\widehat T_n=\mathcal P_n^{-1}T_n\mathcal P_n^{-T}.
\tag{2.2}
$$


Every matrix in this definition is finite.

The vectors and scalar are


$$
u_a=\frac{N!(-2)^a}{a!},\qquad v=T_n^{-1}u,
$$




$$
h_{\rm vec}
=T_n^{-1}\left(\binom{n+a}{a}\gamma_{n+a}\right)_{a=0}^{n-1},
$$




$$
\mathbf t
=3nh_{\rm vec}
+(b_{\rm force}+6)e_N
+\frac{2b_{\rm force}}N e_{N-1},
\tag{2.3}
$$




$$
\Xi=F_{\rm fac}^2-u^Tv,\qquad
\xi=\frac{u^T\mathbf t}{\Xi}.
\tag{2.4}
$$



The denominator $N$ in the force is a ternary unit. The denominator $\Xi$ must be evaluated; its depth is not determined merely by the invertibility of $T_n$.

---

## 3. An explicit formula for the gamma sequence

Define


$$
B_r(z)=
\sum_{k=0}^r
\frac{(r+k)!}{(r-k)!\,k!}\left(\frac z2\right)^k.
\tag{3.1}
$$


These polynomials satisfy


$$
B_{r+1}(z)=(2r+1)zB_r(z)+B_{r-1}(z).
\tag{3.2}
$$



Here is a direct coefficient verification. For $k\ge1$, after multiplication by the common factor


$$
\frac{(r+1-k)!\,k!\,2^k}{(r+k-1)!},
$$


the coefficient identity becomes


$$
(r+k)(r+k+1)
=
(r-k)(r-k+1)+2k(2r+1).
$$


The constant coefficient is immediate, and the endpoint coefficients follow with the out-of-range terms set to zero.

Since $B_0=1$ and $B_1=1+z$, the sequence


$$
(-2)^rB_r(-1)
$$


has initial values $1,0$ and the recurrence in (2.1). Therefore


$$
\boxed{
\gamma_r=(-2)^r
\sum_{k=0}^r A_k\binom{r+k}{2k},
\qquad
A_k=(-1)^k\frac{(2k)!}{2^k k!}.
}
\tag{3.3}
$$


The numbers $A_k=(-1)^k(2k-1)!!$ are integers.

This formula is proved from the supplied recurrence; no Bessel-moment theorem is being imported.

---

## 4. Two valuation bounds for the Newton coefficients

Write the exact Newton expansion


$$
\gamma_r=\sum_{l=0}^r c_l\binom rl,
\qquad
c_l=\sum_{a=0}^l(-1)^{l-a}\binom la\gamma_a.
\tag{4.1}
$$



Two bounds will be useful:


$$
\boxed{
v_3(c_l)\ge \lfloor\log_3 l\rfloor\quad(l\ge1),
}
\tag{4.2}
$$


and


$$
\boxed{
v_3(c_l)\ge\left\lfloor\frac l6\right\rfloor\quad(l\ge0).
}
\tag{4.3}
$$



### 4.1 Bounds for the coefficients in (3.3)

For $k\ge1$,


$$
v_3(A_k)=v_3((2k)!)-v_3(k!).
$$


Let $q$ be the largest power of $3$ not exceeding $2k$.

- If $q>k$, then $q\in(k,2k]$.
- If $q\le k$, then $2q\in(k,2k]$, because $q>2k/3$.

Thus the product $(k+1)\cdots(2k)$ contains a factor of valuation
$\lfloor\log_3(2k)\rfloor$. Hence


$$
v_3(A_k)\ge\lfloor\log_3(2k)\rfloor.
\tag{4.4}
$$


The same interval contains at least $\lfloor k/3\rfloor$ multiples of $3$, so


$$
v_3(A_k)\ge\lfloor k/3\rfloor.
\tag{4.5}
$$



Vandermonde's identity gives


$$
\binom{r+k}{2k}
=
\sum_{t=k}^{2k}\binom rt\binom k{2k-t}.
$$


Consequently, if


$$
B_r(-1)=\sum_{t=0}^r d_t\binom rt,
$$


then


$$
d_t=\sum_{k=\lceil t/2\rceil}^{t}
A_k\binom k{2k-t}.
\tag{4.6}
$$


It follows that


$$
v_3(d_t)\ge\lfloor\log_3 t\rfloor\quad(t\ge1),
\qquad
v_3(d_t)\ge\lfloor t/6\rfloor.
\tag{4.7}
$$



### 4.2 Multiplication by $(-2)^r$

We have


$$
(-2)^r=(1-3)^r=\sum_{h=0}^r(-3)^h\binom rh.
$$


The integer product identity


$$
\binom rh\binom rt
=
\sum_{l=\max(h,t)}^{h+t}
\frac{l!}{(l-h)!(l-t)!(h+t-l)!}\binom rl
\tag{4.8}
$$


counts ordered pairs of subsets by the size of their union.

A contribution to $c_l$ therefore has valuation at least


$$
h+\lfloor\log_3 t\rfloor
$$


when $h,t\ge1$. Since


$$
3^h t\ge h+t\ge l,
$$


this is at least $\lfloor\log_3 l\rfloor$. If $h=0$, then $t=l$; if $t=0$, then $h=l$. These cases give the same bound.

Likewise,


$$
h+\lfloor t/6\rfloor
\ge\lfloor(h+t)/6\rfloor
\ge\lfloor l/6\rfloor.
$$


This proves both (4.2) and (4.3).

In particular, modulo $3^s$, (4.1) truncates at $l<3^s$. Modulo $3^L$, the stronger size bound truncates it at $l<6L$.

---

## 5. Exact finite Pascal conjugation

For $r\ge0$, let


$$
D_r=\operatorname{diag}\left(\binom ar\right)_{a=0}^{n-1},
\qquad
C_r=\mathcal P_n^{-1}D_r\mathcal P_n.
$$


A finite difference calculation gives


$$
\boxed{
(C_r)_{a,i}
=
\binom ar\binom r{a-i}.
}
\tag{5.1}
$$


As usual, a binomial coefficient is zero outside its nonnegative range.

Indeed,


$$
\begin{aligned}
(C_r)_{a,i}
&=\sum_{b=i}^{a}
(-1)^{a-b}\binom ab\binom br\binom bi\\
&=\binom ai
\sum_{b=i}^{a}(-1)^{a-b}\binom{a-i}{b-i}\binom br\\
&=\binom ai\binom i{r-a+i}
=\binom ar\binom r{a-i}.
\end{aligned}
$$


All sums are within $0,\ldots,n-1$.

The finite Pascal identity


$$
\left(\binom{a+b}{a}\right)_{a,b}
=\mathcal P_n\mathcal P_n^T
$$


and Vandermonde's identity now give


$$
\boxed{
\widehat T_n
=
\sum_l c_l\sum_{r+s=l} C_rC_s^T.
}
\tag{5.2}
$$


At a fixed finite size the sum is finite: terms with $r\ge n$ or $s\ge n$ are zero.

For later use, the entry form is


$$
\boxed{
(\widehat T_n)_{a,b}
=
\sum_l c_l\sum_{r=0}^{l}
\binom ar\binom b{l-r}
\binom l{r+b-a}.
}
\tag{5.3}
$$


To obtain it, put $t=a-i$ in the finite product $C_rC_s^T$ and use


$$
\sum_t\binom rt\binom s{t+b-a}
=\binom{r+s}{r+b-a}.
$$


No negative row and no row beyond the finite matrix is needed: the factors
$\binom ar,\binom bs$ enforce the relevant finite admission.

---

## 6. The block reduction theorem

### Theorem 6.1 — Finite Pascal blocks at every ternary precision

Let $s\ge1$, $q=3^s$, and write


$$
n=kq+r,\qquad 0\le r<q.
$$


Then


$$
\boxed{
\widehat T_n
\equiv
\operatorname{diag}
\bigl(
\underbrace{\widehat T_q,\ldots,\widehat T_q}_{k\ \mathrm{copies}},
\widehat T_r
\bigr)
\pmod{3^s},
}
\tag{6.1}
$$


with the final block omitted when $r=0$.

The final $\widehat T_r$ is the actual leading $r$-by-$r$ block associated with the finite Pascal transform. It is not an infinite-matrix boundary convention.

#### Proof

We first record the binomial continuity estimate. For $1\le a_1<q$,


$$
\binom{z+qv}{a_1}-\binom z{a_1}
=
\sum_{i=1}^{a_1}\binom{qv}{i}\binom z{a_1-i}.
$$


Since


$$
\binom{qv}{i}=\frac{qv}{i}\binom{qv-1}{i-1},
$$


we have


$$
\boxed{
\binom{z+qv}{a_1}
\equiv\binom z{a_1}
\pmod{3^{s-\lfloor\log_3 a_1\rfloor}}.
}
\tag{6.2}
$$


This is valid for integer arguments; generalized binomial coefficients, when needed, are still integers.

By (4.2), only $l<q$ contributes to (5.2) modulo $3^s$. Fix such an $l\ge1$ and put


$$
e=\lfloor\log_3 l\rfloor.
$$


For every $r\le l$, formula (5.1), together with (6.2), shows that $C_r$ is block diagonal in $q$-blocks modulo $3^{s-e}$:

- inside a $q$-block, its entries agree with those of the first block;
- if an entry crosses the lower edge of its row block, then $a-i>a\bmod q$, so
  $\binom{a\bmod q}{r}=0$, and the crossing entry is divisible by $3^{s-e}$.

Multiplication by $c_l$, which is divisible by $3^e$, makes every discrepancy vanish modulo $3^s$.

The products $C_rC_s^T$ have the correct final incomplete block. Both factors are lower triangular before transposition; computing a leading principal submatrix of their product never requires an index beyond that principal submatrix. Thus the finite last block is exactly the leading block stated in (6.1).

The $l=0$ term is the identity and causes no exception. Summing proves the theorem. ∎

This theorem supplies the missing justification for reducing the original large size. A size congruence alone would not have supplied it.

---

## 7. Ternary invertibility and the evaluated small blocks

The first gamma values are


$$
\gamma_0=1,\quad \gamma_1=0,\quad
\gamma_2=4,\quad \gamma_3=40,\quad \gamma_4=576.
$$


Direct finite Pascal conjugation gives


$$
\widehat T_1=(1),
$$




$$
\boxed{
\widehat T_2=
\begin{pmatrix}
1&-1\\
-1&9
\end{pmatrix},
\qquad
\widehat T_2^{-1}
=\frac18
\begin{pmatrix}
9&1\\
1&1
\end{pmatrix},
}
\tag{7.1}
$$


and


$$
\boxed{
\widehat T_3=
\begin{pmatrix}
1&-1&5\\
-1&9&99\\
5&99&3017
\end{pmatrix}.
}
\tag{7.2}
$$



Modulo $3$, these are the finite blocks


$$
B_1=(1),\qquad
B_2=\begin{pmatrix}1&2\\2&0\end{pmatrix},
$$




$$
B_3=
\begin{pmatrix}
1&2&2\\
2&0&0\\
2&0&2
\end{pmatrix}.
$$


Their determinants are units modulo $3$. Theorem 6.1 with $s=1$ therefore proves


$$
\boxed{T_n\in\operatorname{GL}_n(\mathbb Z_3)\quad(n\ge1).}
\tag{7.3}
$$



This is also a consequence of the new block theorem, rather than an assumed scalar conclusion from the earlier unit theorem.

---

# Part II. Evaluation of the actual original scalar and force

## 8. The terminal block at the original indices

Apply Theorem 6.1 with $q=243$. By (1.1),


$$
n\equiv2\pmod{243}.
$$


The last two coordinates of $\widehat T_n$, indexed by $N-1,N$, are therefore the actual final block


$$
\begin{pmatrix}1&-1\\-1&9\end{pmatrix}\pmod{243},
$$


with all couplings to earlier blocks zero modulo $243$.

In particular,


$$
\boxed{
(\widehat T_n)_{N,N}\equiv9\pmod{243}.
}
\tag{8.1}
$$


This proves the proposed zero modulo $9$, and evaluates its stronger original residue.

The block inverse is legitimate modulo $243$: every full block and the final block have unit determinant modulo $3$, by (7.3).

---

## 9. The transformed vector $u$, with all factorial factors paid

For $a\le N-2$, the quotient $N!/a!$ contains $N-1$, which is divisible by $243$. Thus


$$
u_a\equiv0\pmod{243}\qquad(a\le N-2).
\tag{9.1}
$$


The two remaining entries are


$$
u_{N-1}=N(-2)^{N-1},\qquad u_N=(-2)^N.
$$



Because $v_3(N-1)=5$,


$$
(-2)^{N-1}\equiv1\pmod{729}.
$$


Hence


$$
u_{N-1}\equiv1,\qquad u_N\equiv-2\pmod{243}.
$$



The inverse Pascal matrix is lower triangular and integral. Therefore, with


$$
\widehat u=\mathcal P_n^{-1}u,
$$


all entries before $N-1$ are still zero modulo $243$, while


$$
\widehat u_{N-1}\equiv1,
$$




$$
\widehat u_N
\equiv u_N-Nu_{N-1}\equiv-3\pmod{243}.
$$


Thus


$$
\boxed{
\widehat u\equiv e_{N-1}-3e_N\pmod{243}.
}
\tag{9.2}
$$



The exact factorial term $F_{\rm fac}^2=(N!)^2$ has not been removed from the definition of $\Xi$. At the present precision it is zero, since the original $N$ is sufficiently large.

---

## 10. Evaluation of $\Xi$

The finite change of basis gives


$$
u^TT_n^{-1}u=\widehat u^T\widehat T_n^{-1}\widehat u.
$$


Using the actual final block (7.1),


$$
\begin{aligned}
u^TT_n^{-1}u
&\equiv
(1,-3)\,
\frac18
\begin{pmatrix}9&1\\1&1\end{pmatrix}
\binom1{-3}\\
&=(1,-3)\binom{3/4}{-1/4}\\
&=\frac32
\pmod{243}.
\end{aligned}
\tag{10.1}
$$


All denominators here, $8$ and $4$, are retained ternary units.

Consequently,


$$
\boxed{
\Xi=F_{\rm fac}^2-u^TT_n^{-1}u
\equiv-\frac32\equiv120\pmod{243}.
}
\tag{10.2}
$$


It follows immediately that


$$
\boxed{
\Xi\ne0,\qquad v_3(\Xi)=1,\qquad
\frac{\Xi}{3}\equiv-\frac12\equiv40\pmod{81}.
}
\tag{10.3}
$$



In particular,


$$
\Xi/3\equiv1\pmod3,
$$


as required by the original depth-one test.

This is an original-index theorem. It is not inferred from a finite pattern at freely selected sizes.

---

## 11. Evaluation of the complete forcing numerator

The value of $u^Th_{\rm vec}$ must use the actual next column of $T_{n+1}$, not an unrelated local column.

Write the full Pascal matrix in block form:


$$
\mathcal P_{n+1}=
\begin{pmatrix}
\mathcal P_n&0\\
p^T&1
\end{pmatrix},
\qquad
p_a=\binom na.
$$


Let


$$
k=(\widehat T_{n+1})_{\{0,\ldots,n-1\},\,n}.
$$


The exact factorization


$$
T_{n+1}=\mathcal P_{n+1}\widehat T_{n+1}\mathcal P_{n+1}^T
$$


gives


$$
\boxed{
h_{\rm vec}
=\mathcal P_n^{-T}
\left(p+\widehat T_n^{-1}k\right).
}
\tag{11.1}
$$


Therefore


$$
u^Th_{\rm vec}
=
\widehat u^Tp+\widehat u^T\widehat T_n^{-1}k.
\tag{11.2}
$$



Modulo $243$, the actual last block of $\widehat T_{n+1}$ has size three. By (7.2),


$$
k_{\{N-1,N\}}\equiv\binom5{99}.
$$


Also,


$$
p_{\{N-1,N\}}
=
\binom{\binom n2}{n}
\equiv\binom12\pmod{243}.
$$


Thus


$$
\widehat T_2^{-1}\binom5{99}
=
\frac18\binom{144}{104}
=\binom{18}{13},
$$


and


$$
\boxed{
u^Th_{\rm vec}
\equiv
(1,-3)\binom{19}{15}
=-26
\pmod{243}.
}
\tag{11.3}
$$


The entry $99$, although zero modulo $3$, has been retained at the precision where it matters.

Now include both explicit terminal force terms:


$$
\begin{aligned}
u^T\mathbf t
={}&3n\,u^Th_{\rm vec}
 +(b_{\rm force}+6)(-2)^N
 +\frac{2b_{\rm force}}N\,N(-2)^{N-1}\\
={}&3n\,u^Th_{\rm vec}+6(-2)^N.
\end{aligned}
\tag{11.4}
$$


The cancellation in the second line is exact and uses both terms.

Since $n\equiv2\pmod{243}$ and $(-2)^N\equiv-2\pmod{729}$,


$$
\boxed{
u^T\mathbf t
\equiv3\cdot2\cdot(-26)+6(-2)
=-168\pmod{729}.
}
\tag{11.5}
$$


Hence


$$
v_3(u^T\mathbf t)=1.
$$


Combining (10.3) and (11.5),


$$
\boxed{
\xi=\frac{u^T\mathbf t}{\Xi}
\equiv112\equiv31\pmod{81},
\qquad v_3(\xi)=0.
}
\tag{11.6}
$$



This does **not** assert the exact equality $\xi=112$. Replacing the actual $\xi$ by $112$ in the higher-precision producer would be unjustified.

For reference, the same calculation gives


$$
v_N\equiv-\frac14,\qquad v_{N-1}\equiv1\pmod{243},
$$




$$
(h_{\rm vec})_N\equiv15,\qquad
(h_{\rm vec})_{N-1}\equiv4\pmod{243}.
\tag{11.7}
$$


These are finite-precision residues, not substitutes for the full vectors in the producer.

---

# Part III. The unconditional original 72-coefficient source reduction

## 12. Actual coefficients and the negative endpoint

The signed producer coefficients remain exactly


$$
\boxed{
q_a:=[x^a]\delta Q
=-\frac{N!}{a!}\bigl(t_a+\xi v_a\bigr),
\qquad 0\le a\le N.
}
\tag{12.1}
$$


By (7.3), $h_{\rm vec},v\in\mathbb Z_3^n$. The force denominator $N$ is a unit, and (11.6) makes $\xi$ integral. Thus every $q_a$ is integral.

At the negative endpoint $y=-1$, or $x=-2$,


$$
\begin{aligned}
\delta Q(-1)
&=-u^T\mathbf t-\xi u^Tv\\
&=-\xi(\Xi+u^Tv)\\
&=\boxed{-\xi F_{\rm fac}^2}.
\end{aligned}
\tag{12.2}
$$


This endpoint is not identically zero. Indeed $\xi$ is a ternary unit and $F_{\rm fac}\ne0$.

Its high divisibility will be used only in a paid finite-precision replacement.

---

## 13. The original congruence gives a $3^{37}$ tail payment

Consider the product of the last 72 integers in $N!$:


$$
\frac{N!}{(N-72)!}
=\prod_{r=0}^{71}(N-r).
$$


The factor $N$ is a unit, the factor $N-1$ has valuation $5$, and for $2\le r\le71$,


$$
v_3(N-r)=v_3(r-1),
$$


because $v_3(N-1)=5>v_3(r-1)$. Therefore


$$
\begin{aligned}
v_3\!\left(\frac{N!}{(N-72)!}\right)
&=5+v_3(70!)\\
&=5+23+7+2\\
&=\boxed{37}.
\end{aligned}
\tag{13.1}
$$


For every $a\le N-72=n-73$, the quotient $N!/a!$ contains this product. Hence


$$
q_a\in3^{37}\mathbb Z_3\qquad(a\le n-73).
\tag{13.2}
$$



Retain all 72 original top coefficients:


$$
P_{71}(x)=\sum_{r=0}^{71}q_{n-72+r}x^r.
$$


Then


$$
\delta Q=x^{n-72}P_{71}(x)+L(x),
\qquad
L\in3^{37}\mathbb Z_3[x].
\tag{13.3}
$$


The original $N$ is sufficiently large that $(N!)^2\in3^{37}\mathbb Z_3$. Equation (12.2), evaluated in (13.3), gives


$$
P_{71}(-2)\in3^{37}\mathbb Z_3.
$$


Monic division by $x+2=y+1$ yields


$$
P_{71}(x)=(x+2)V_{70}(x)+P_{71}(-2),
$$


where


$$
\boxed{
[x^b]V_{70}
=
\sum_{r=b+1}^{71}
(-2)^{r-b-1}q_{n-72+r},
\qquad 0\le b\le70.
}
\tag{13.4}
$$



Thus, with every $q_a$ still given by the actual formula (12.1),


$$
\boxed{
\delta Q_{\rm short}=(y+1)x^{A-70}V_{70}(x),
\qquad
\delta Q-\delta Q_{\rm short}\in3^{37}\mathbb Z_3[x].
}
\tag{13.5}
$$



This retains the prescribed 72 coefficients. No higher coefficient of $T_n^{-1}h$, $T_n^{-1}u$, or $\xi$ has been replaced by its leading residue.

---

## 14. Complete projection payment

The physical cutoff (1.3) implies that $\mathcal M$ maps integral polynomials to $\mathbb Z_3$: every retained denominator $2v+1$ has valuation at most $h$, and the factorial summand is integral.

Under the proved integrality of the actual producer, the paid inverse bound (1.7) therefore gives


$$
F_{\rm act}[p],F_c[p]\in3^{-1}\mathbb Z_3[y]
\tag{14.1}
$$


for integral admitted inputs $p$.

Let $Q'=Q_{\rm act}+\epsilon$, with


$$
\epsilon\in3^{37}\mathbb Z_3[x].
$$


The $W$-matrix perturbation is in $3^{37}M$. Since the original inverse costs only $3^{-1}$, its product with the perturbation lies in $3^{36}M$. The finite Neumann identity gives the same $3^{-1}$ inverse allowance for the perturbed matrix.

The exact stationary Schur identity gives


$$
S_{Q'}(p,q)-S_{\rm act}(p,q)
=
\mathcal M(\epsilon F_{\rm act}[p]F_{\rm act}[q])
-c_p^TE_{Q'}^{-1}c_q,
$$


where


$$
c_p=\mathcal M(\epsilon W F_{\rm act}[p]).
$$


The first term lies in $3^{35}\mathbb Z_3$. Each $c_p$ lies in $3^{36}M$, so the return lies in $3^{71}\mathbb Z_3$. Therefore


$$
\boxed{S_{Q'}-S_{\rm act}\in3^{35}M.}
\tag{14.2}
$$



Applying this to (13.5),


$$
\boxed{
\mathsf A_{\rm short}-\mathsf A_{\rm act}
\in3^9M,
}
\tag{14.3}
$$


after the original $3^{26}$ prefix normalization.

Thus the 72-coefficient replacement is now unconditional on the original family and is more precise than the modulo-$81$ target. The actual $W$, $Y_m$, and finite projection are unchanged.

### Keeping the actual inverse literal

For the next transport one may also keep $E_{\rm act}^{-1}$ itself, rather than replacing it by a shortened-producer inverse.

Let


$$
\alpha_\alpha[p]=E_\alpha^{-1}G_\alpha(W,x^Dp).
$$


Both $\alpha_c[p]$ and $\alpha_{\rm act}[p]$ lie in $3^{-1}M$. For


$$
b_p^\delta=\mathcal M(\delta Q\,W\,F_c[p]),
$$


the exact identity is


$$
\boxed{
E_{\rm act}^{-1}b_p^\delta
=\alpha_{\rm act}[p]-\alpha_c[p]\in3^{-1}M.
}
\tag{14.4}
$$


This is stronger than the naive bound obtained by separately multiplying an arbitrary $3^{-1}$ cross vector by a $3^{-1}$ inverse.

Consequently, changing $\delta Q$ by $3^s$ changes


$$
\mathcal M(\delta Q F_c[p]F_c[q])
-(b_p^\delta)^TE_{\rm act}^{-1}b_q^\delta
$$


by $3^{s-2}$, for $s\ge2$. Both cross variations are paid using (14.4); the quadratic variation is still deeper.

In particular:

- the replacement error $3^{37}$ changes this whole expression by $3^{35}$;
- knowing the actual $V_{70}$ modulo $3^{32}$ suffices for its quotient by $3^{29}$ modulo $3$.

The $W$-return has been controlled, not deleted.

---

# Part IV. A bounded reconstruction of the actual producer coefficients

## 15. Why a bounded coefficient reduction is possible

The scalar calculation does not evaluate the 72 coefficients to the needed precision. A further uniform reduction is available, however.

By (4.3), modulo $3^L$, equation (5.3) truncates at


$$
l\le6L-1.
$$


Thus


$$
\widehat T_n\bmod3^L
$$


has half-bandwidth at most


$$
R_L=6L-1.
\tag{15.1}
$$



The inverse also has a precision-dependent finite bandwidth. This does not follow from inverting a band matrix over a field; it follows from the ternary depth of its successive corrections.

### Lemma 15.1 — Paid inverse locality

For $L\ge1$,


$$
\boxed{
(\widehat T_n^{-1})_{a,b}\equiv0\pmod{3^L}
\quad\text{if}\quad
|a-b|>13(L-1)+2.
}
\tag{15.2}
$$



#### Proof

Let $H_0$ be the integral block diagonal lift of $\widehat T_n\bmod3$, using the blocks $B_3,B_1,B_2$ displayed in §7. Its inverse $D_0$ is integral over $\mathbb Z_3$ and has half-bandwidth $2$.

Write the ternary digit expansion


$$
\widehat T_n=H_0+\sum_{q\ge1}3^qH_q.
$$


The bound (15.1), applied modulo $3^{q+1}$, shows that $H_q$ has half-bandwidth at most


$$
6q+5.
$$



A term in the finite Neumann expansion modulo $3^L$, containing $k$ correction factors of depths $q_1,\ldots,q_k$, has total depth


$$
Q=q_1+\cdots+q_k<L.
$$


Its half-bandwidth is at most


$$
2(k+1)+\sum_{i=1}^k(6q_i+5)
=6Q+7k+2
\le13Q+2.
$$


The term with no correction has half-bandwidth $2$. Summing proves (15.2). ∎

### Finite-edge consequence

Suppose a terminal principal window starts at an index divisible by $3$, so it contains complete leading $3$-blocks and the actual final incomplete block.

If every observed row and every forcing support is farther than


$$
13(L-1)+2
$$


from the lower edge of that window, all Neumann paths relevant modulo $3^L$ remain inside it. The window solve then agrees with the original finite solve on the observed rows.

This explicitly proves the finite-boundary reduction. It is not an assumption that inverses of band matrices are banded.

---

## 16. The $617$-coordinate reconstruction at the required precision

Take


$$
L=33,\qquad R_L=197,\qquad
\rho_L=13\cdot32+2=418.
$$


The actual last 197 coordinates and every relevant inverse path lie in the terminal window of length


$$
\boxed{617.}
\tag{16.1}
$$


Indeed,


$$
617-197+1=421>418,
$$


and, since $n\equiv2\pmod3$,


$$
n-617\equiv0\pmod3.
$$


Thus the lower edge is a genuine $3$-block boundary. The original family is sufficiently large that this window exists.

### 16.1 Matrix entries

Only $c_0,\ldots,c_{197}$ are needed. They are obtained from the supplied gamma recurrence through index $197$ and the finite Newton formula (4.1).

Every window entry is explicitly


$$
\boxed{
\sum_{l=0}^{197}c_l
\sum_{r=0}^{l}
\binom ar\binom b{l-r}
\binom l{r+b-a}
\pmod{3^{33}},
}
\tag{16.2}
$$


with $a,b$ in the actual terminal window.

For $r\le197$, estimate (6.2) shows that $\binom ar\bmod3^{33}$ is determined by


$$
a\bmod3^{37},
$$


because $\lfloor\log_3 197\rfloor=4$. Therefore all these entries are determined by


$$
\boxed{N\bmod3^{37}.}
\tag{16.3}
$$


This is a proved residue dependence of the original finite entries.

### 16.2 The transformed $u$-force

If $a\le N-99$, then $N!/a!$ contains at least 99 consecutive integers and is divisible by $3^{33}$. Thus $u\bmod3^{33}$ is supported on its last 99 coordinates.

For $0\le d\le98$,


$$
u_{N-d}
=(-2)^{N-d}\prod_{r=0}^{d-1}(N-r).
\tag{16.4}
$$


No original factorial is needed to compute this value.

The finite Pascal transform is


$$
\boxed{
\widehat u_{N-e}
=
\sum_{d=e}^{98}
(-1)^{d-e}\binom{N-e}{d-e}u_{N-d}
\pmod{3^{33}},
\quad 0\le e\le98.
}
\tag{16.5}
$$


Earlier coordinates are zero modulo $3^{33}$.

### 16.3 The next-column force

Let $k$ be the actual transformed next column in (11.1). Formula (15.1) gives


$$
k_a\equiv0\pmod{3^{33}}
\qquad(a<n-197).
$$


Its last 197 entries are evaluated by (16.2), with $b=n$.

Thus both required transformed forces are supported in the admitted part of the terminal window. Two unit window solves give


$$
z_u=\widehat T_n^{-1}\widehat u,\qquad
z_h=\widehat T_n^{-1}k
$$


on every needed terminal coordinate, modulo $3^{33}$.

### 16.4 Returning to the actual coefficients

For $0\le d\le71$,


$$
\boxed{
v_{N-d}
=
\sum_{e=0}^{d}
(-1)^{d-e}\binom{N-e}{d-e}(z_u)_{N-e}
\pmod{3^{33}}.
}
\tag{16.6}
$$



The exact identity


$$
(\mathcal P_n^{-T}p)_a
=(-1)^{n-a-1}\binom na
$$


follows by completing the finite alternating binomial sum with its one missing last term. Hence


$$
\boxed{
(h_{\rm vec})_{N-d}
=
(-1)^d\binom{N+1}{d+1}
+
\sum_{e=0}^{d}
(-1)^{d-e}\binom{N-e}{d-e}(z_h)_{N-e}
\pmod{3^{33}}.
}
\tag{16.7}
$$



For the scalar and its numerator, use the same finite vectors:


$$
\Xi\equiv-\widehat u^Tz_u\pmod{3^{33}},
$$




$$
u^Th_{\rm vec}
=\widehat u^Tp+\widehat u^Tz_h.
$$


The already proved depth-one statements pay division of both numerator and denominator by $3$. They determine


$$
\xi\bmod3^{32}.
$$



Finally,


$$
q_{N-d}
=
-\left(\prod_{r=0}^{d-1}(N-r)\right)
\bigl(t_{N-d}+\xi v_{N-d}\bigr)
\pmod{3^{32}},
\tag{16.8}
$$


and (13.4) determines every coefficient of $V_{70}\bmod3^{32}$.

### Status of this reduction

This proves that the required actual producer jet can be reconstructed from bounded inputs. It does not report the resulting 72-entry array as computed.

It also does not shorten $F_c[g]$, $E_{\rm act}^{-1}$, or the physical HIGH return. Those are different finite objects.

---

# Part V. The actual physical-seventh prefix transport

## 17. The nine bands remain the actual tests

Put


$$
\Pi=P/3,\qquad L_*=(P-1)/2,\qquad \kappa_1=(\Pi-1)/2.
$$


The complete second-kernel amplitudes remain


$$
H_i=(1-y)^e y^{L_*+i},
$$


where


$$
(e,\eta,w)=
\begin{cases}
(c,0,c),&\text{Ranges I--II},\\
(\Pi,\Pi-c,\Pi-c),&\text{Range III}.
\end{cases}
$$


Their established finite gaps include


$$
w+2k-2\le\kappa_1-120,
\qquad
i+\eta+1\le\delta<\kappa_1.
$$


The complete leading inverse images are


$$
Z_{0,H_i}(y)=y^i(1-y)^\eta C(y^P).
$$



Choose the explicit integral lift


$$
\boxed{
g_i(y)=2y^i(1-y)^\eta\sum_{r\in\mathcal S}y^{rP}.
}
\tag{17.1}
$$


Its degree is


$$
97P+\eta+i<a_0,
$$


so it is an admitted original prefix input. Define


$$
\widehat F_i=F_c[g_i],
\qquad
b_i^\delta=\mathcal M(\delta Q\,W\,\widehat F_i).
\tag{17.2}
$$



With the original normalizations,


$$
\Delta_A=\frac{\mathsf A_{\rm act}-\mathsf A_c}{27}\pmod3,
$$


and


$$
\mathcal P_{7,\alpha}
=
\frac{\mathscr H^Td_\alpha^T\mathsf A_\alpha^{-1}d_\alpha\mathscr H}{27}
\pmod3.
$$


The complete stationary identity remains


$$
\boxed{
\mathcal P_{7,\rm act}-\mathcal P_{7,c}
=
\frac{
\mathcal M(\delta Q\,\widehat F_i\widehat F_j)
-(b_i^\delta)^TE_{\rm act}^{-1}b_j^\delta
}{3^{29}}
\pmod3.
}
\tag{17.3}
$$


The complete comparison pays the division by $3^{29}$.

The scalar theorem and §§13–14 now prove that (17.3) is unchanged if $\delta Q$ in its two cross expressions is replaced by the actual $\delta Q_{\rm short}$, while $E_{\rm act}^{-1}$ remains literal. The error after division by $3^{29}$ lies in $3^6\mathbb Z_3$.

This is a rigorous source reduction, not an evaluation of (17.3).

---

## 18. The precise obstruction to closing the next transport

Write


$$
F_{r,i}=F_c[y^{rP+i}(1-y)^\eta],
\qquad r\in\mathcal S.
$$


Then


$$
\widehat F_i=2\sum_{r\in\mathcal S}F_{r,i}.
$$


Consequently the whole numerator in (17.3) contains all $9\times9$ band pairs:


$$
4\sum_{r,s\in\mathcal S}
\left[
\mathcal M(\delta Q\,F_{r,i}F_{s,j})
-
\mathcal M(\delta Q\,W F_{r,i})^T
E_{\rm act}^{-1}
\mathcal M(\delta Q\,W F_{s,j})
\right].
\tag{18.1}
$$


Only the complete sum has the established $3^{29}$ payment. Individual summands may not be divided by $3^{29}$ without a separate proof.

The new scalar and producer locality theorems determine neither:

1. the required coefficient observations of the complete $F_{r,i}$; nor
2. the contraction of their complete cross vectors through $E_{\rm act}^{-1}$.

In particular, the physical terminal component remains


$$
\boxed{
(b_i^\delta)_{Y_m}
=\mathcal M(\delta Q\,Y_m\,\widehat F_i).
}
\tag{18.2}
$$


It has not been set to zero.

The negative endpoint also remains literal in the original source:


$$
(\delta Q\,\widehat F_i\widehat F_j)(-1)
=-\xi F_{\rm fac}^2\,\widehat F_i(-1)\widehat F_j(-1).
\tag{18.3}
$$


Its replacement by the endpoint-zero shortened source is justified only at the paid finite precision of §14.

### Why the short-producer argument still stops here

The supplied A1 Turn 3 obstruction applies directly. A factor or a narrow terminal width in the raw producer does not automatically survive:

- monic LOW remainders;
- complete LOW feedback;
- finite HIGH inverse copies;
- lower truncation;
- the physical upper terminal $m$;
- the paid divisions in the observed return.

The nine-band polynomial is an uncorrected prefix input. Its factorization does not show that $\widehat F_i$ has the same factor.

Nor do the abstract comparisons


$$
\mathsf A_{\rm act}-\mathsf A_c\in27M,\qquad
d_{\rm act}-d_c\in81M
$$


determine the contraction of $\Delta_A$. A symmetric jet supported at row $14P$, for example, can pair nontrivially with the first nine-band inverse image. This is an obstruction to inference from the comparison bounds, not a counterexample for the actual producer.

### Concrete follow-on obligation

The producer part is now reduced to the explicitly reconstructible $V_{70}\bmod3^{32}$. The next lemma must evaluate, in the original complete objects,


$$
\boxed{
\begin{aligned}
\mathcal N_{ij}:={}&
\mathcal M\!\left(
(y+1)x^{A-70}V_{70}\,\widehat F_i\widehat F_j
\right)\\
&-
\mathcal M\!\left(
(y+1)x^{A-70}V_{70}\,W\widehat F_i
\right)^T
E_{\rm act}^{-1}
\mathcal M\!\left(
(y+1)x^{A-70}V_{70}\,W\widehat F_j
\right)
\end{aligned}
}
\tag{18.4}
$$


modulo $3^{30}$, for all the admitted original $i,j$.

A necessary first scalar test is $\mathcal N_{00}/3^{29}\pmod3$, with the exact $g_0$ from (17.1). Its value is not supplied here. Closing (18.4) requires either explicit complete projected-column coefficient cancellations at the surviving physical poles, or a proved observed-annihilation lemma that includes the LOW feedback and the $Y_m$ return. A raw-support argument is insufficient.

Thus the outstanding object is now a specific complete source/terminal contraction, not the former uncertainty about the depth of $\Xi$.

---

## 19. The core alternative is also not claimed closed

The complete core prefix matrix modulo $81$ and its next inverse quadratic have not been evaluated here.

The retained Turn 13 results concerning the complete residual modulo $81$, including


$$
D_{121}\equiv54,\qquad D_{122}\equiv27\pmod{81},
$$


are not discarded. Their proved zero linear residual pairing does not eliminate:

- lower-digit residual cross terms;
- changes of the finite inverse;
- the next core matrix coefficient;
- the actual $\Delta_A$ contraction.

No core-only result in this report is promoted to an actual-producer result.

---

# Part VI. Other returns and the global arithmetic remain unchanged

## 20. Complete forcing and physical returns

The complete forcing identity remains


$$
\boxed{
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
}
\tag{20.1}
$$


Both terms, including the physical terminal coordinate, are retained.

The complete source recurrence remains


$$
\mu_{t+1}+\mu_t
=
\frac{3^h}{2t+1}
-\frac{3^h}{4}\bigl((2t+2)!+(2t)!\bigr),
\qquad0\le t\le2n-2,
$$


with the genuine resonance


$$
t_*=\frac{3^h-5}{2}.
$$



The diagonal frames are not exchanged:


$$
\lambda_{\rm new}
=
\lambda^{\rm pref}
-\frac13f_J^TB^{-1}f_J
-\frac19f_b^TA_b^{-1}f_b
\in3^{-2}\mathbb Z_3,
$$


whereas in the monomial-first frame


$$
\lambda_4
=
\lambda_{\rm new}
-\frac1{81}f_C^TA_4^{-1}f_C
\in3^{-4}\mathbb Z_3.
$$


The physical-$5$ complementary returns remain active at order $7$.

The separate $J$, rank-$b$, first physical-$4$, endpoint, and whole-force obligations retain their assigned scope. No whole seventh-order matrix is assembled or certified here.

---

## 21. Actual contents, least clearer, all-prime gcd, and whole error

The local denominators $2,4,8,N$, and the paid division by $3$ in $\Xi$, have been accounted for in $\mathbb Z_3$. This does not evaluate denominators at other primes.

No result here changes any original integer column content or the actual least simultaneous clearer $\ell_{\rm clr}$.

Retain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


and the final gcd over **all primes**


$$
g_\ell=\gcd(|A_\ell|,|B_\ell|).
$$


For $B_\ell\ne0$, the actual primitive pair remains


$$
q=\frac{|B_\ell|}{g_\ell},
\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


The whole evaluated error is exactly


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
{g_\ell}\det H_{\rm complete}.
}
\tag{21.1}
$$



An irrationality proof still requires, at the **same infinite original indices**,


$$
B_\ell\ne0,\qquad \det H_{\rm complete}\ne0,
$$


and


$$
\boxed{
\log g_\ell-(m+1)\log\ell_{\rm clr}
-\log|\det H_{\rm complete}|
\longrightarrow+\infty.
}
\tag{21.2}
$$


These conditions would make the nonzero whole integer linear forms tend to zero. If $e+\pi=a/b$ were rational, every such nonzero form would have absolute value at least $1/|b|$.

The producer scalar $\Xi\ne0$ is not the nonvanishing of $\det H_{\rm complete}$. Its unit-normalized depth is not an all-prime primitive-denominator estimate.

The reused density theorem supplies infinitely many original Range III indices in


$$
3/25<\chi/P<31/250.
$$


It does not establish (21.2), or the necessary same-index nonvanishing.

---

# Part VII. Separately gated bounded arithmetic checks

## 22. No computation is needed for the scalar proof

The scalar theorem above is symbolic. No tool computation was performed, and no old 122-constant, nine-block, sector, or source-moment calculation needs to be repeated.

Two optional bounded checks are mathematically well specified.

### Gate A: small recurrence and Pascal certificate

**Inputs**

- The given gamma recurrence through index $10$.
- Pascal matrices of sizes $2$ and $3$.
- Newton coefficients $c_0,\ldots,c_8$.

**Expected verifiable outputs**

Modulo $9$,


$$
(\gamma_0,\ldots,\gamma_{10})
=(1,0,4,4,0,7,1,0,4,1,0),
$$




$$
(c_0,\ldots,c_8)
=(1,8,5,0,0,6,3,6,6).
$$


Exactly,


$$
\widehat T_2=
\begin{pmatrix}1&-1\\-1&9\end{pmatrix},
$$




$$
\widehat T_3=
\begin{pmatrix}
1&-1&5\\
-1&9&99\\
5&99&3017
\end{pmatrix}.
$$


The evaluated identities to check are


$$
(1,-3)\widehat T_2^{-1}\binom1{-3}=\frac32,
$$




$$
(1,-3)\left[
\binom12+\widehat T_2^{-1}\binom5{99}
\right]=-26.
$$



This certificate checks the bounded arithmetic used in the proof. The uniform reduction follows from §§3–6, not from the finite check.

### Gate B: one bounded actual-producer coefficient receipt

This is a separate, optional follow-on calculation, not a prerequisite for the proved scalar theorem.

**Fully specified inputs**

Take the original progression index


$$
j_0=84645,
$$


and the bounded residue


$$
\overline N=4^{84645}\bmod3^{37}.
$$


Use:

- modulus $3^{33}$;
- gamma and Newton coefficients through index $197$;
- the $617$-coordinate terminal window;
- entries (16.2);
- forces (16.5) and the next-column formula;
- the two unit window solves;
- formulas (16.6)–(16.8) and (13.4).

No factorial at the original size is an input.

**Expected verifiable outputs**

1. The residue $\overline N$, together with $\overline N\equiv1\pmod{243}$.
2. Both window residual equations equal zero modulo $3^{33}$.
3. The scalar checks
   

$$
\Xi\equiv120\pmod{243},
   \qquad
   u^T\mathbf t\equiv-168\pmod{729},
   \qquad
   \xi\equiv31\pmod{81}.
$$


4. The complete 72-entry array
   

$$
(q_{n-72},\ldots,q_{n-1})\pmod{3^{32}},
$$


   and the complete 71-entry array of $V_{70}\pmod{3^{32}}$.
5. Verification of the coefficient identity
   

$$
P_{71}=(x+2)V_{70}+P_{71}(-2)
   \pmod{3^{32}}.
$$



This would be a finite receipt for one original producer index. It would not assert that $j_0$ supplies a retained $(h,D,P,\chi)$ density tuple, and it would not evaluate any physical prefix return. The uniform validity of the coefficient-reconstruction method is supplied by the locality proof, not by this one calculation.

No bounded arithmetic receipt for the whole expression (18.4) is yet specified, because the necessary complete projected-column reduction remains unproved.

---

## Conclusion

### New proved results

1. **The original producer scalar has depth exactly one:**
   

$$
\boxed{
   \Xi\equiv-\frac32\pmod{243},
   \qquad v_3(\Xi)=1.
   }
$$



2. **The proposed diagonal test is true, with a stronger evaluated residue:**
   

$$
\boxed{
   (\widehat T_n)_{n-1,n-1}\equiv9\pmod{243}.
   }
$$


   Its reduction to a terminal two-coordinate block is justified by a proved finite Pascal theorem, not by a size-congruence guess.

3. **The complete force gives**
   

$$
\boxed{
   u^T\mathbf t\equiv-168\pmod{729},
   \qquad
   \xi\equiv112\pmod{81},
   \qquad v_3(\xi)=0.
   }
$$



4. **The original 72-coefficient source reduction is unconditional and fully paid:**
   

$$
\boxed{
   \delta Q-(y+1)x^{A-70}V_{70}\in3^{37}\mathbb Z_3[x].
   }
$$


   It preserves the complete next prefix jet after all finite $W$-projection costs.

5. **The actual 72-coefficient jet admits a bounded, original-index reconstruction.** The proof requires no huge original factorial matrix and preserves the true terminal boundary.

### Exact remaining local bottleneck

The complete source-specific quotient (18.4), divided by $3^{29}$ and reduced modulo $3$, is not evaluated. Its complete $W$-return, including the physical $Y_m$ component, remains essential. The old short-producer/short-corrected-column implication is still invalid without a further observed-annihilation proof.

The complete core prefix jet modulo $81$ is likewise not closed here, and no unknown actual $\Delta_A$ contribution has been suppressed.

### Global proof status

No result here establishes the actual all-prime contents, least clearer, final gcd, primitive denominator, or same-index nonzero whole-error decay.



$$
\boxed{
\text{The primary original-producer scalar obligation is closed.}
}
$$




$$
\boxed{
\text{The complete actual physical-seventh prefix transport remains open.}
}
$$




$$
\boxed{
\text{The rationality or irrationality of }e+\pi\text{ remains unresolved.}
}
$$


