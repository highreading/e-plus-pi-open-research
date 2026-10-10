> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, Turn 2 — An integral three-variable evaluation of the complete raw pair

## Executive summary

The rationality or irrationality of $e+\pi$ remains unresolved.

The new result of this report is an **integral evaluation procedure for the actual raw norm and complete raw exponential pairing**. It avoids the common-baseline conversion and descending three-moment reduction altogether. In particular:



$$
\boxed{\text{The new whole-pair summation procedure has no additional dyadic clearing loss.}}
$$



Thus the previously proved losses $3497$ and $2735$, at raw precision $32$ on odd $u$, are not intrinsic losses of evaluating the pair. They remain correct for the earlier certificates, but are absent from the procedure below.

The construction has three parts.

1. Reuse the audited integral, type-$2$-only profiles, with the full finite completion and complete source.
2. Transform each resulting finite kernel into a coefficient of
   

$$
\frac{
   X^dY^\delta
   (1+X)^{N_1}(1+t/X)^{N_2}
   (1+tY)^{N_3}(1+1/Y)^{N_4}}
   {(1-t)^M},
$$


   minus an **explicit short offset tail**. This is an integral identity. It does not introduce a factorial clearer.
3. Evaluate that coefficient modulo $2^L$ by a derived Cartier shift procedure. Each active polynomial has at most
   

$$
\boxed{(6L-2)(4L-1)^2}
$$


   possible monomial positions. This is cubic in $L$, rather than exponential in $L$.

There is also a whole-assembly compression. After at most


$$
\left\lceil\log_2\!\bigl(\max(2r_f,r_f+\Delta_\varepsilon)\bigr)\right\rceil
$$


initial shifts, the entire kernel collection can be merged into at most **32 exponent/target classes**, carrying both output channels. Here


$$
r_f=m+I+1,\qquad
\Delta_\varepsilon=\rho+I+1.
$$


At raw precision $32$, ten shifts suffice for this merging bound.

These are proved arithmetic bounds, not a claim that a new original-family primitive digit has been evaluated. The initial coefficient assembly can still be large, the algorithm still reads the actual parameter word, and the actual content $a$ remains symbolic unless independently certified.

No relation $E-rQ$ at primitive depth, no infinite-family nonvanishing theorem for $E$, and no favorable all-prime denominator–whole-error comparison is proved.

---

## 1. Original objects and the scope of the evidence

Throughout,


$$
\boxed{b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.}
$$


The contact matrix has exactly the indices $0\le i,j<b$, and physical reconstruction has exactly the rows $0\le j\le b$.

Retain


$$
h=\frac n2,\qquad
R=2^h\binom nh,\qquad
\Lambda=\frac{(n!)^2}{2^n},
$$




$$
\phi(z)=1-z+\frac{z^2}{2},\qquad
\lambda_s=s![z^s]\phi(z)^n,\qquad
W_j=\binom{n+2}{j}.
$$


The original finite matrix and force are


$$
A_{ij}=
\sum_{s=0}^{n+i}
\lambda_s\binom{n+i}{s}\binom{2n+i-s}{j},
$$




$$
f_i^0=
\frac{(n+i)!}{n!}
[t^n](1+2t+2t^2)^n(1+t)^i,
\qquad
\mathfrak f=f^0/R.
$$



For a contact vector $z$,


$$
(\mathcal Rz)_j=W_j(jz_{j-1}-z_j),
\qquad z_{-1}=z_b=0.
$$


The corrected columns are unchanged:


$$
x=\frac12\mathcal RA^{-1}\mathfrak f,
\qquad
y=\frac{\mathcal RA^{-1}(h^e+h^F)+e_0}{4b!}.
$$



Write


$$
x=2^ax_0,\qquad
z^f=A^{-1}\mathfrak f,\qquad
z^k=A^{-1}k,
$$


where


$$
k=\frac{h^e-A(j!)_{0\le j<b}}{b!}.
$$



It is useful to name the two **raw** pairings:


$$
\mathcal U=\mathfrak f^T\mathcal B\mathfrak f,
\qquad
\mathcal V=\mathfrak f^T(\mathcal Bk+v_{\rm term}),
$$


with


$$
\mathcal B=A^{-T}\mathcal R^T\mathcal RA^{-1},
\qquad
v_{\rm term}=bW_b^2A^{-T}e_{b-1}.
$$


Their primitive normalizations are


$$
Q=2^{-2a-2}\mathcal U,\qquad
E=2^{-a-3}\mathcal V.
\tag{1.1}
$$



Explicitly,


$$
\mathcal U=
\sum_{j=0}^{b-1}W_j^2(\Delta_jz^f)^2
+b^2W_b^2(z^f_{b-1})^2,
\tag{1.2}
$$


and


$$
\boxed{
\mathcal V=
\sum_{j=0}^{b-1}W_j^2
(\Delta_jz^f)(\Delta_jz^k)
+b^2W_b^2z^f_{b-1}z^k_{b-1}
+bW_b^2z^f_{b-1}.
}
\tag{1.3}
$$


Both terminal terms in (1.3) are retained below.

### 1.1 What the new audit establishes

The attached certificate reports six auxiliary checks at $b=5,7,9$ and $L=3,4$. Their proper scope is the displayed finite identities:

- literal versus normal-ordered $\mathcal J$;
- full finite Schur completion;
- first-force completion;
- explicit profiles;
- complete exponential cancellation;
- auxiliary terminal $-1$;
- Vandermonde collapse.

The reported original-family residue arithmetic also verifies the earlier losses $3497$ and $2735$.

None of these finite checks evaluates a primitive digit on an infinite original subdomain. Nothing below promotes them to such a theorem.

---

## 2. Reused finite completion: exactly what enters the new evaluator

At raw precision $2^L$, retain


$$
I=\min(b-1,8L-2),\qquad
m=4(L-1),\qquad
d_{\rm tail}=\min(m,b),
$$




$$
T=\min(2L-1,2n-1),\qquad V=T+m.
\tag{2.1}
$$


The established filtrations give


$$
\mathfrak f_i\equiv0\pmod{2^L}\quad(i>I),
\qquad
\lambda_s\equiv c_s\equiv0\pmod{2^L}\quad(s>m),
$$


where


$$
c_0=1,\qquad
c_s=-\sum_{r=1}^s\binom sr\lambda_rc_{s-r}.
$$



The complete exponential source has the paid prefix


$$
k\equiv\sum_{t=0}^{T}a_t\mathbf a_{b+t}\pmod{2^L},
\qquad
a_t=\frac{(b+t)!}{b!}.
\tag{2.2}
$$


This is a prefix of the complete source after the original factorial subtraction, not a coefficientwise deletion from an aligned residual.

### 2.1 Full Schur data

For clarity, the finite return data used in the audited formulas are


$$
F_{jv}=
-\sum_{q=0}^v
\binom{-n}{b+q-j}\binom n{v-q},
$$




$$
(H^{-1})_{ij}=c_{i-j}\binom ij\quad(i\ge j),
$$




$$
K_{rt}=
\lambda_{d_{\rm tail}+r-t}
\binom{b+r}{d_{\rm tail}+r-t}.
$$


Let $E_{\rm tail}$ inject the last $d_{\rm tail}$ contact coordinates, and put


$$
G_v=E_{\rm tail}^TH^{-1}F_{\cdot v},
$$




$$
S=I+E_{\rm tail}^TH^{-1}F^{(m)}K.
\tag{2.3}
$$


Because $K\equiv0\pmod2$, $S$ is a unit matrix over $\mathbb Z_2$.

With the finite Pascal and upper-binomial matrices $P,U$, define


$$
D_f=E_{\rm tail}^TH^{-1}U^{-1}P^{-1}\mathfrak f_{\le I},
$$




$$
\eta_f=U_n^{(m)}KS^{-1}D_f.
\tag{2.4}
$$



For the complete source, retain


$$
\xi_v=
\sum_{t=0}^{T}a_t
\sum_{\substack{0\le r\le t\\0\le v-r\le m}}
\binom n{t-r}\lambda_{v-r}\binom{b+v}{v-r},
$$




$$
\delta_v=(KS^{-1}G^{[V]}\xi)_v-\xi_v,
\qquad
\theta_v=\sum_{w=v}^{V}\binom n{w-v}\delta_w.
\tag{2.5}
$$


The first term in $\delta_v$ is padded by zeros after its $m$ coordinates.

These formulas retain the entire finite return, including the returned source contribution whose cancellation was proved in Turn 1.

### 2.2 The integral profiles being reused

For $0\le j<b$, define


$$
\begin{aligned}
\Psi_{jv}
={}&(-1)^{b+v-j}
\sum_{s=0}^m(-1)^sc_s
\sum_{r=0}^s
\binom{n+r-1}{r}\binom j{s-r}\\
&\hspace{12mm}\cdot
\binom{2n+b+v+s-1-j}{b+v+s-r-j},
\end{aligned}
\tag{2.6}
$$


and


$$
\begin{aligned}
B_{ji}
={}&(-1)^{j-i}
\sum_{s=0}^m(-1)^sc_s
\sum_{r=0}^s\binom{n+r-1}{r}
\sum_{q=0}^i\binom{2n+r+q-1}{q}\\
&\quad\cdot
\binom{s-r+i-q}{s-r}
\binom j{s-r+i-q}
\binom{2n+b+s-1-j}{b+s-r-q-1-j}.
\end{aligned}
\tag{2.7}
$$


The audited completion states


$$
z^f_j\equiv
\sum_{i=0}^{I}\mathfrak f_iB_{ji}
+\sum_{v=0}^{m-1}(\eta_f)_v\Psi_{jv},
\tag{2.8}
$$




$$
z^k_j\equiv
\sum_{v=0}^{V}\theta_v\Psi_{jv}
\pmod{2^L}.
\tag{2.9}
$$



No proof of normal ordering is repeated here. The new work starts with these integral formulas.

### 2.3 Boundaries that are not being changed

The complete differential source is still


$$
\mathscr L_n
\left(
\frac{\phi^ng_n-e^z\phi^nU_b}{b!}
\right)
=
e^z\phi^{n+1}(C_{b-1}+C_b),
\tag{2.10}
$$


with


$$
C_j(z)=\sum_{r=0}^j\binom n{j-r}\frac{z^r}{r!},
\qquad
U_b(z)=\sum_{j=0}^{b-1}j!C_j(z).
$$


Both differential boundaries remain present.

The auxiliary extension of (2.9) has value $-1$ at $j=b$. It is **not** a physical contact value. Physical reconstruction continues to use $z_b^k=0$, with the separate $+1$ contribution in (1.3).

---

## 3. Integral kernel assembly without a common profile clearer

Every reconstructed profile is an integral linear combination, modulo $2^L$, of atoms


$$
(-1)^j\binom jd
\binom{2n+b+\eta-j}{b+\varepsilon-j}.
\tag{3.1}
$$


Indeed,


$$
j\binom{j-1}{d}=(d+1)\binom j{d+1},
$$


so reconstruction introduces only integral multipliers and shifts.

Products are assembled using the integral identity


$$
\binom jd\binom je
=
\sum_{r=\max(d,e)}^{d+e}
\frac{r!}{(r-d)!(r-e)!(d+e-r)!}\binom jr.
\tag{3.2}
$$


The displayed coefficients are ordinary integers. They can be formed as multinomial coefficients; no modular division is required.

Consequently the two interior pairings are integral linear combinations of


$$
\boxed{
\begin{aligned}
\mathcal K(d;\eta_1,\varepsilon_1;\eta_2,\varepsilon_2)
={}&
\sum_{j=0}^{b-1}
\binom{n+2}{j}^{2}\binom jd\\
&\cdot
\binom{2n+b+\eta_1-j}{b+\varepsilon_1-j}
\binom{2n+b+\eta_2-j}{b+\varepsilon_2-j}.
\end{aligned}}
\tag{3.3}
$$



The following bounds will be useful. Set


$$
\rho=T+2m+1,\qquad r_f=m+I+1.
\tag{3.4}
$$


For all assembled kernels,


$$
0\le d\le2r_f,
\qquad
-I-1\le\varepsilon_i\le\rho.
\tag{3.5}
$$


More importantly, inspection of the actual profiles gives the sharper complementary-offset bound


$$
\boxed{
-1\le a_i:=\eta_i-\varepsilon_i\le r_f-1.
}
\tag{3.6}
$$


For an exterior atom $a_i=r-1$; for a head atom $a_i=r+q$. Reconstruction does not change $a_i$.

This structure is what permits the small rational coefficient representation below.

As in the previous bounded-precision reduction, one may impose


$$
n>4D+2,\qquad D=I+2m+T+4.
\tag{3.7}
$$


It ensures that all large exponents used below are nonnegative. It is not a claim about half-length precision.

---

## 4. The new acceptance identity, including the exact short tail

Order the two factors in (3.3) so that


$$
\varepsilon_1\le\varepsilon_2,\qquad
\delta=\varepsilon_2-\varepsilon_1\ge0.
$$


Put


$$
N=n+2,\qquad
A=2n+a_1,\qquad B=2n+a_2.
$$



With the exact substitution $b=j+r$, the original endpoint becomes


$$
r\ge1.
$$


The second part of the kernel is


$$
h_r=
\binom{2n+r+\eta_1}{r+\varepsilon_1}
\binom{2n+r+\eta_2}{r+\varepsilon_2}.
\tag{4.1}
$$


After $k=r+\varepsilon_1$,


$$
h_r=\binom{A+k}{k}\binom{B+k+\delta}{k+\delta}.
$$



### 4.1 An integral Euler transformation

For $A-\delta\ge0$ and $B\ge0$,


$$
\boxed{
\sum_{k\ge0}
\binom{A+k}{k}\binom{B+k+\delta}{k+\delta}t^k
=
\frac{
\displaystyle\sum_{\ell\ge0}
\binom{A-\delta}{\ell}
\binom{B+\delta}{\ell+\delta}t^\ell}
{(1-t)^{A+B+1}}.
}
\tag{4.2}
$$



This is the classical Euler transformation of a terminating hypergeometric series, used here at its exact integral scope.

For a direct verification, the coefficients on the left satisfy


$$
(k+1)(k+\delta+1)h_{k+1}
=(k+A+1)(k+B+\delta+1)h_k,
$$


with initial value $\binom{B+\delta}{\delta}$.
The numerator coefficients on the right satisfy


$$
(\ell+1)(\ell+\delta+1)p_{\ell+1}
=(A-\delta-\ell)(B-\ell)p_\ell.
$$


Substitution of $H=(1-t)^{-A-B-1}P$ into the corresponding second-order differential equation gives the first recurrence and the same initial value. This proves (4.2) over $\mathbb Q[[t]]$; every coefficient in the displayed identity is integral.

There is no scalar division by a factorial or a large-offset product.

The numerator has the constant-term representation


$$
\sum_{\ell\ge0}
\binom{A-\delta}{\ell}
\binom{B+\delta}{\ell+\delta}t^\ell
=
\operatorname{CT}_Y
Y^\delta(1+tY)^{A-\delta}(1+1/Y)^{B+\delta}.
\tag{4.3}
$$



Similarly,


$$
\sum_{j\ge0}\binom Nj^2\binom jd\,t^j
=
\binom Nd\,
\operatorname{CT}_X
X^d(1+X)^{N-d}(1+t/X)^N.
\tag{4.4}
$$


To check (4.4), the constant term selects $j-d$ from the first binomial and $j$ from the second, and


$$
\binom Nd\binom{N-d}{j-d}
=\binom Nj\binom jd.
$$



### 4.2 Exact finite-cutoff correction

Equation (4.2) starts at $k=0$, whereas the physical sum has $r\ge1$.

If $\varepsilon_1<0$, all extra terms with $r<-\varepsilon_1$ already vanish by the negative-lower-index convention. There is no correction.

If $\varepsilon_1\ge0$, the extension has introduced exactly


$$
r=-\varepsilon_1,\ldots,0.
$$


Thus define


$$
\boxed{
\begin{aligned}
\mathcal T_{\rm off}
={}&
\sum_{k=0}^{\varepsilon_1}
\binom{N}{b+\varepsilon_1-k}^{2}
\binom{b+\varepsilon_1-k}{d}\\
&\quad\cdot
\binom{A+k}{k}
\binom{B+k+\delta}{k+\delta}
\qquad(\varepsilon_1\ge0),
\end{aligned}}
\tag{4.5}
$$


and $\mathcal T_{\rm off}=0$ otherwise.

This tail has at most $\rho+1$ terms. In particular, the $r=0$ term, when present, is explicitly subtracted.

### Theorem 4.1 — Integral coefficient acceptance identity

Let


$$
\begin{aligned}
N_1&=n+2-d, &N_2&=n+2,\\
N_3&=2n+a_1-\delta, &N_4&=2n+a_2+\delta,\\
M&=4n+a_1+a_2+1, &B_{\rm tar}&=b+\varepsilon_1.
\end{aligned}
\tag{4.6}
$$


Then


$$
\boxed{
\mathcal K
=
\binom{n+2}{d}
[t^{B_{\rm tar}}X^0Y^0]
\frac{
X^dY^\delta
(1+X)^{N_1}(1+t/X)^{N_2}
(1+tY)^{N_3}(1+1/Y)^{N_4}}
{(1-t)^M}
-\mathcal T_{\rm off}.
}
\tag{4.7}
$$



All exponents $N_i$ are nonnegative under (3.7). The coefficient is taken in a $t$-adic series with finite Laurent-polynomial coefficients in $X,Y$.

#### Proof

Multiply (4.3)–(4.4), include the factor $t^{-\varepsilon_1}$, and extract $t^b$. This gives the convolution over the extended $r$-range. Subtracting (4.5) restores exactly $r\ge1$, equivalently $j<b$. ∎

The finite boundary has not been replaced by an infinite one. The only extension is the displayed short tail, which is explicitly removed.

---

## 5. An integral Cartier evaluator with no output-precision loss

The coefficient in (4.7) is now evaluated, not left as an unevaluated diagonal.

Set


$$
v_1=X,\qquad v_2=t/X,\qquad v_3=tY,\qquad v_4=1/Y.
\tag{5.1}
$$


A state consists of:

- four nonnegative exponents $N_1,\ldots,N_4$;
- a nonnegative denominator exponent $M$;
- a target $B_{\rm tar}\ge0$;
- a finite Laurent polynomial $P(t,X,Y)$ over $\mathbb Z/2^L\mathbb Z$.

Its meaning is


$$
\mathcal A(P;\mathbf N,M,B_{\rm tar})
=
[t^{B_{\rm tar}}X^0Y^0]
P\,\frac{\prod_{i=1}^4(1+v_i)^{N_i}}{(1-t)^M}.
\tag{5.2}
$$


Initially $P=X^dY^\delta$.

For $\mathbf e=(e_t,e_X,e_Y)\in\{0,1\}^3$, define the Cartier operator


$$
\mathcal C_{\mathbf e}
\left(\sum c_{a,b,c}t^aX^bY^c\right)
=
\sum c_{2a+e_t,\,2b+e_X,\,2c+e_Y}
t^aX^bY^c.
\tag{5.3}
$$


Negative Laurent exponents cause no ambiguity.

### 5.1 The numerator shift identity

Write


$$
N_i=2h_i+\epsilon_i,\qquad \epsilon_i\in\{0,1\},
$$


and set


$$
H_i=\min(h_i,L-1),\qquad N_i'=h_i-H_i.
$$


Define the univariate polynomial


$$
K_i(v)=
\sum_{r=0}^{H_i}
2^r\binom{h_i}{r}v^r(1+v^2)^{H_i-r}.
\tag{5.4}
$$


Then


$$
\boxed{
(1+v)^{N_i}
\equiv
(1+v)^{\epsilon_i}K_i(v)(1+v^2)^{N_i'}
\pmod{2^L}.
}
\tag{5.5}
$$



Indeed,


$$
(1+v)^{2h_i}
=((1+v^2)+2v)^{h_i}.
$$


Every omitted term has $r\ge L$, hence contains $2^L$. Formula (5.4) factors out exactly the surviving common power of $1+v^2$.

### 5.2 The denominator shift identity

Write


$$
M=2h_0+\epsilon_0,\qquad \epsilon_0\in\{0,1\},
$$


and put


$$
M'=h_0+\epsilon_0+L-1.
$$


Define


$$
K_0(t)=
\sum_{s=0}^{L-1}
2^s\binom{h_0+s-1}{s}
t^s(1-t^2)^{L-1-s}.
\tag{5.6}
$$


When $h_0=0$, the coefficient is $1$ at $s=0$ and $0$ for $s>0$.

Then


$$
\boxed{
(1-t)^{-M}
\equiv
\frac{(1+t)^{\epsilon_0}K_0(t)}
     {(1-t^2)^{M'}}
\pmod{2^L}.
}
\tag{5.7}
$$


This follows from


$$
(1-t)^2=(1-t^2)-2t
$$


and the integral negative-binomial expansion. Terms with $s\ge L$ vanish modulo $2^L$.

Again, there is no inversion of $2$.

### 5.3 The actual state transition

Let $e=B_{\rm tar}\bmod2$. Form


$$
\boxed{
P'=
\mathcal C_{(e,0,0)}
\left[
P(1+t)^{\epsilon_0}K_0(t)
\prod_{i=1}^4(1+v_i)^{\epsilon_i}K_i(v_i)
\right].
}
\tag{5.8}
$$


Update


$$
\boxed{
N_i\leftarrow N_i',\qquad
M\leftarrow M',\qquad
B_{\rm tar}\leftarrow\lfloor B_{\rm tar}/2\rfloor.
}
\tag{5.9}
$$



### Theorem 5.1 — Shift closure and acceptance

Each transition preserves (5.2) modulo $2^L$.

When $B_{\rm tar}=0$ and all four $N_i=0$, the answer is


$$
\boxed{[t^0X^0Y^0]P.}
\tag{5.10}
$$



#### Proof

Substitute (5.5) and (5.7) into (5.2). All remaining large-power factors are functions of $t^2,X^2,Y^2$. Cartier extraction pulls these factors through unchanged after halving their exponents. This gives (5.8)–(5.9).

At termination, the only remaining denominator is $(1-t)^M$, whose constant coefficient is $1$. Since the numerator has no negative $t$-powers, the $t^0$ coefficient is exactly (5.10). ∎

The number of iterations is $O(\log(n+b+D))$. No loop of length $b$ occurs.

---

## 6. Reachable-state and arithmetic resource bounds

The preceding construction is not an exponential-size formal state action.

Put


$$
J=2L-1.
$$


Each factor


$$
(1+v_i)^{\epsilon_i}K_i(v_i)
$$


has degree at most $J$ in its single monomial $v_i$, and


$$
(1+t)^{\epsilon_0}K_0(t)
$$


has degree at most $J$ in $t$.

### 6.1 Cubic polynomial support

Suppose the current $X$-support has exponent width $w_X$. Multiplication in (5.8) enlarges that width by at most $2J$: one factor moves in the positive $X$-direction, one in the negative direction. Cartier extraction then gives


$$
w_X'\le\left\lfloor\frac{w_X}{2}\right\rfloor+J.
$$


The same bound holds for $Y$.

Initially both widths are zero. Hence


$$
w_X,w_Y\le2J.
\tag{6.1}
$$



The $t$-degree grows before Cartier extraction by at most $3J$, from $v_2,v_3$, and the denominator multiplier. Starting at degree zero,


$$
\deg_tP\le3J.
\tag{6.2}
$$



Therefore every active state polynomial has at most


$$
\boxed{
S_L=(3J+1)(2J+1)^2
=(6L-2)(4L-1)^2
}
\tag{6.3}
$$


possible coefficient positions.

The location of its Laurent-support box can move. Its size is bounded by (6.3); one does not allocate all positions between exponent zero and its moving center.

At $L=32$,


$$
\boxed{S_{32}=190\cdot127^2=3\,064\,510.}
\tag{6.4}
$$


For one scalar channel, a dense representation at this bound uses about $12.3$ million bytes of coefficient storage, apart from indexing and intermediate products.

This is a bound, not a measured occupancy.

### 6.2 Transition cost

The five multiplier polynomials are univariate polynomials along fixed lattice directions. They can be constructed with polynomially many short-binomial operations.

A direct line-convolution implementation costs


$$
O(L^4)
$$


operations in $\mathbb Z/2^L\mathbb Z$ per shift, with absolute constants determined by the five directions. Standard fast integer convolution gives a softly polynomial bit bound of order


$$
\widetilde O(L^4)
$$


per shift as well, rather than an exponential dependence on $L$.

For example, convolution along a line can be implemented by packing its coefficients into integers with enough guard bits to prevent carries between slots, multiplying those integers, and unpacking. This uses exact integer arithmetic and introduces no mathematical precision loss.

### 6.3 Whole-assembly merging after a short initial stage

There is additional compression specific to the actual assembled pair.

Initially,


$$
\begin{aligned}
N_1&=n+2-d,\\
N_2&=n+2,\\
N_3&=2n+a_1-\delta,\\
N_4&=2n+a_2+\delta,\\
M&=4n+a_1+a_2+1,\\
B_{\rm tar}&=b+\varepsilon_1.
\end{aligned}
$$


The exponent $N_2$ is identical for every kernel.

Set


$$
\Delta_\varepsilon=\rho+I+1.
$$


Using (3.5)–(3.6), the spreads of the other five entries are bounded by


$$
2r_f,\quad r_f+\Delta_\varepsilon,\quad
r_f+\Delta_\varepsilon,\quad2r_f,\quad
\Delta_\varepsilon.
\tag{6.5}
$$



Each update map in (5.9) contracts an integer interval of width $w$ to one of width at most $\lceil w/2\rceil$. Consequently, after


$$
\boxed{
t_0=
\left\lceil
\log_2\max(2r_f,r_f+\Delta_\varepsilon)
\right\rceil,
}
\tag{6.6}
$$


each varying entry has at most two possible values.

Thus there are at most


$$
\boxed{2^5=32}
\tag{6.7}
$$


distinct exponent/target tuples after this initial stage.

States with the same tuple may be added, because all subsequent transitions are linear in $P$. Their norm and exponential coefficients can be carried as a two-component coefficient vector.

The union of the support boxes after this stage has at most


$$
(6L-2)(4L)^2
\tag{6.8}
$$


positions per tuple: the initially different centers have also contracted to width at most one beyond the single-kernel bound.

At $L=32$,


$$
r_f=379,\qquad \Delta_\varepsilon=567,
$$


so $t_0=10$.

This yields a concrete whole-assembly strategy:

1. accumulate identical initial kernels;
2. stream each initial kernel through at most ten shifts at raw precision $32$;
3. merge into at most 32 classes;
4. traverse the remaining parameter word using only those classes.

### 6.4 What this resource bound does and does not solve

The bound removes the previous exponential precision-state obstruction and the thousands of artificial paid bits.

It does **not** prove that the initial actual coefficient list is small enough for a new high-depth production run. A conservative count of possible initial kernels is still polynomial of degree five in the precision, with substantial constants.

Nor does the procedure prove compressed periodic dependence on $u$. It reads the actual exponents derived from


$$
b=9^{18+32u}.
$$


Their bit length is $\Theta(u+1)$, not $O(\log(u+2))$.

Accordingly, no original-size primitive calculation is commissioned here.

---

## 7. The actual whole-pair congruence and every paid division

Let $\gamma_\kappa^Q,\gamma_\kappa^E\in\mathbb Z/2^L\mathbb Z$ be the coefficients obtained by assembling (2.8)–(2.9), reconstructing, and applying (3.2).

For a kernel $\kappa$, let $\operatorname{Acc}_L(\kappa)$ denote the **evaluated output of (5.8)–(5.10)**, including its scalar $\binom{n+2}{d}$, but before subtracting the short tail.

Then the actual pair satisfies


$$
\boxed{
\begin{aligned}
\mathcal U
\equiv{}&
\sum_\kappa\gamma_\kappa^Q
\bigl(\operatorname{Acc}_L(\kappa)-\mathcal T_{{\rm off},\kappa}\bigr)
+b^2W_b^2(z^f_{b-1})^2,\\[1mm]
\mathcal V
\equiv{}&
\sum_\kappa\gamma_\kappa^E
\bigl(\operatorname{Acc}_L(\kappa)-\mathcal T_{{\rm off},\kappa}\bigr)\\
&+b^2W_b^2z^f_{b-1}z^k_{b-1}
+bW_b^2z^f_{b-1}
\pmod{2^L}.
\end{aligned}}
\tag{7.1}
$$



This is an acceptance identity with an explicit terminating evaluator and a polynomial state bound. It is not a renaming of three unevaluated moments.

### 7.1 No additional whole-combination clearer

Every transition in §5 takes place in $\mathbb Z/2^L\mathbb Z$. There is no analogue of


$$
C_f,\quad C_k,\quad \kappa_Q,\quad \kappa_E
$$


to divide out.

Thus the new additional whole-combination loss is


$$
\boxed{e_{\rm sum}=0.}
\tag{7.2}
$$



This does not mean that every subsidiary scalar can be computed from an $L$-bit parameter residue without payment. For example, to evaluate


$$
2^r\binom hr\pmod{2^L}
$$


by a falling-factorial formula, it suffices to know $h$ modulo


$$
2^{\,L-r+v_2(r!)}
$$


and then perform the exact integer division. A uniform sufficient bound is less than $2L$ bits for $r<L$.

Likewise, $\binom{n+2}{d}$ may be computed from a parameter residue modulo


$$
2^{L+v_2(d!)}.
$$


These are **local, explicitly paid short-binomial computations**, not an added loss in the modulus of the whole raw pairing.

The source coefficients retain their previously proved parameter-precision requirements.

### 7.2 Offset tails and terminal binomials

The offset tails (4.5) have precision-sized length. Large-lower-index binomials occurring there, such as


$$
\binom{n+2}{b+s},
$$


can be evaluated by the one-variable specialization of §5, starting from


$$
[t^{b+s}](1+t)^{n+2}.
$$


This has $O(L)$ active coefficient positions and no scalar clearing loss.

The physical $W_b$ is handled in the same way. The terminal profile values are supplied by the finite formulas (2.8)–(2.9).

The short-tail subtraction removes the artificial $j=b$ value introduced by the Euler extension. The physical terminal in (7.1) is then added separately. There is no double counting and no substitution of the auxiliary value $z_b^k=-1$.

### 7.3 Actual primitive precision

For primitive output modulo $2^K$, the required raw precisions remain exactly


$$
\boxed{
L_Q=K+2a+2,\qquad L_E=K+a+3.
}
\tag{7.3}
$$


After evaluating the **whole** corresponding raw expression, one performs the whole divisions in (1.1).

No value $a=9$, or any other constant value, has been assumed. This report neither bounds the actual content uniformly on an original residue class nor proves that it is unbounded there.

The new procedure accepts the actual $a$ symbolically or uses an independently certified bound for a specified calculation.

---

## 8. What has not cancelled, and the remaining relative-pair obligation

The new transformation cancels an arithmetic obstacle: it avoids the profile-clearing and adjoint-pivot products.

It does **not** prove cancellation of any actual moment direction in $E-rQ$. No ratio inferred from a finite receipt is promoted to a family invariant.

For an integral candidate $r$, the exact paid relative identity is


$$
\boxed{
E-rQ
=
2^{-2a-3}\bigl(2^a\mathcal V-2r\mathcal U\bigr).
}
\tag{8.1}
$$


Therefore a congruence modulo $2^K$ requires the complete integral numerator


$$
2^a\mathcal V-2r\mathcal U
$$


at modulus $2^{K+2a+3}$.

In particular, its terminal contribution is


$$
\boxed{
2^aW_b^2bz^f_{b-1}(bz^k_{b-1}+1)
-2r\,b^2W_b^2(z^f_{b-1})^2.
}
\tag{8.2}
$$


Deleting the linear term in $z^f_{b-1}$ would change the relative problem.

### A concrete follow-on lemma

The new evaluator makes a more specific next target available:

> **Whole-response observable-quotient lemma.**  
> Starting from the actual two-component polynomial states obtained from (2.4)–(2.9), determine the observable quotient of the at-most-32 merged classes under (5.8), at the required raw depth. Prove either:
> 1. a derived relative coefficient $r(u)$ for which the complete acceptance functional of $2^a\mathcal V-2r(u)\mathcal U$, including (8.2) and all offset tails, vanishes to a stated primitive depth on an explicit infinite original subdomain; or
> 2. a stated nonzero digit of the complete $\mathcal V$ on such a subdomain.

This is now a quotient of explicit cubic-size polynomial spaces with explicitly known shifts. It is no longer a request to evaluate an original-size inverse or an unnamed long sum.

What remains difficult is the actual source-dependent initial polynomial content and its observation under the original parameter word. The present evaluation theorem does not supply that invariant.

---

## 9. Logarithmic contribution, actual normalization, and whole error

The logarithmic source remains


$$
\mathcal L_s=s![z^s]\frac{F(z)}{1-z},
$$


with the retained guard


$$
B_*=n-v_2(b!)-1-2s_2(n)-\ell.
\tag{9.1}
$$


The exponential evaluator is not a replacement for this source.

A primitive observation protected by the guard may omit the logarithmic contribution only within that stated range. Beyond it, the complete original logarithmic contribution is compulsory.

The producer normalization remains


$$
\omega_j=j!W_j,\qquad
u_j=\frac{2\Lambda R\,x_j}{\omega_j},\qquad
v_j=\frac{4b!\,y_j}{\omega_j},
$$


and its **actual least simultaneous clearer** is


$$
\boxed{
d_B=
\operatorname{lcm}_{0\le j\le b}
\{\operatorname{den}(u_j),\operatorname{den}(v_j)\}.
}
\tag{9.2}
$$


No reconstructed row content is divided out.

Writing $N=x^Tx$ and $H=x^Ty$, retain


$$
A_B=d_B^2\,4\Lambda^2R^2N,\qquad
H_B=d_B^2\,8\Lambda Rb!H,
$$




$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
}
\tag{9.3}
$$


The gcd in (9.3) is the all-prime gcd.

For every prime $p$,


$$
v_p(q_n)=
\max\{v_p(\mathscr D_n)+v_p(N)-v_p(H),0\},
\qquad
\mathscr D_n=\frac{\Lambda R}{2b!}.
\tag{9.4}
$$


The previously established ternary law is retained at its stated scope:


$$
v_3(q_n)=n-\frac{b+15}{2}.
$$


No recalculation of it is requested.

Finally,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


and the whole evaluated error is


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n.
}
\tag{9.5}
$$



An irrationality proof through this producer would require a favorable estimate for the actual $q_n$ and a nonzero whole error on the **same infinitely many original indices**. A nonzero exponential pairing alone is not that certificate.

---

## 10. Bounded exact arithmetic proposed for independent inspection

No computation was performed here. The algebraic claims above do not depend on a new numerical receipt.

A small, new audit can test the Euler-tail and Cartier evaluator without repeating the closed normal-ordering, Schur, or loss calculations.

### Inputs

Use the auxiliary values


$$
b=11,\qquad n=44022,\qquad L=5,
$$


and the four kernels


$$
\begin{array}{c|cc|cc}
d&\eta_1&\varepsilon_1&\eta_2&\varepsilon_2\\ \hline
0&-1&0&-1&0\\
3&2&-2&5&3\\
2&2&1&4&3\\
4&3&4&-1&0
\end{array}
\tag{10.1}
$$


with the two factors reordered when necessary to make
$\varepsilon_1\le\varepsilon_2$.

These cover:

- zero offset tail;
- a negative minimum lower offset;
- a nonempty short offset tail;
- nonzero $d$ and unequal complementary offsets.

### Expected verifiable outputs

For each row, the independently authored calculation should output:

1. the direct finite sum (3.3), reduced modulo $32$;
2. the Cartier acceptance value from (4.7) and §5;
3. the explicit offset-tail residue;
4. equality
   

$$
\mathcal K_{\rm direct}
   \equiv
   \operatorname{Acc}_5-\mathcal T_{\rm off}\pmod{32};
$$


5. zero difference;
6. the maximum observed support widths, checked against (6.1)–(6.3).

At $L=5$, the single-state support bound is


$$
(6L-2)(4L-1)^2=28\cdot19^2=10108.
$$


The direct comparison has only eleven summands per kernel. Its binomial coefficients have short lower indices.

This is a bounded auxiliary check of the **new** evaluator. It would establish only those finite cases. It would not establish a primitive digit or an infinite-family relative law.

---

## 11. Proof-status ledger

| Statement | Status |
|---|---|
| Audited normal ordering and full finite completion | Reused at their proved scope |
| Complete source prefix and both differential boundaries | Retained |
| Earlier $3497/2735$ certificate losses | Retained; not recomputed |
| Integral Euler transformation with exact short offset tail | **Proved** |
| Actual three-variable coefficient acceptance identity | **Proved** |
| Integral Cartier transition and terminal acceptance | **Proved** |
| No additional whole-pair dyadic clearing loss | **Proved** |
| Cubic single-state support bound | **Proved** |
| At most 32 merged exponent/target classes after a short initial stage | **Proved** |
| Practical runtime for a new primitive original-family calculation | Not established |
| Compressed periodic dependence of the complete response on $u$ | Not established |
| Actual content $a$, newly evaluated | Not obtained |
| Derived infinite-family congruence $E-rQ$ | Open |
| Infinite-original nonzero exponential digit | Open |
| Actual all-prime denominator versus nonzero whole same-index error | Unresolved |
| Rationality or irrationality of $e+\pi$ | Unresolved |

---

## Conclusion

The principal new result is an integral evaluation theorem for the actual raw pair:



$$
\boxed{
\begin{gathered}
\text{audited complete type-\(2\) profiles}\\
\longrightarrow
\text{an exact coefficient identity with a short, explicit offset tail}\\
\longrightarrow
\text{a cubic-support Cartier evaluator modulo the raw modulus itself}.
\end{gathered}}
$$



It retains the original contact boundary, full Schur return, complete factorial source prefix, both differential source boundaries, both physical exponential terminal terms, and the logarithmic guard.

It removes the $3497$- and $2735$-bit **computational** losses without replacing the actual contents, least simultaneous clearer, all-prime gcd, or primitive denominator.

The exact remaining bottleneck is now the **observable value of the actual assembled polynomial states at true primitive depth**, including their source-dependent coefficients and the original parameter word. A useful relative law or a nonzero infinite-family observation has not yet been proved.

After that local bottleneck, the all-prime denominator and the nonzero whole error still must be compared on the same infinite original indices.

**The new integral evaluation and resource bounds are rigorous. No unconditional proof or disproof of the irrationality of $e+\pi$ follows.**
