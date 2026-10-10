> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2, Turn 8 — A complete $29$-digit compression, with the relative Gram law still open

## Executive summary

The irrationality or rationality of $e+\pi$ is **not settled** by the supplied work or by this report.

The main advance here is a proved compression of the **entire finite contact-word and three-column Gram calculation** to a base-$29$ digit transfer. Unlike Turn 7’s band reduction, this construction does not leave original-length binomial transforms or a row-by-row Gram summation unevaluated.

The construction retains:

- the original family
  

$$
a=432827+682892t,\qquad b=3^a,\qquad n=2001b,
  \qquad t\equiv364\pmod{841};
$$


- the complete normalized force, including its logarithmic contribution when its proved valuation budget is insufficient;
- the actual ranges $0\le i,j<b$ and $0\le j\le b$;
- the factorial and binomial **units**, including the odd-prime sign absent from a naive binary adaptation;
- both projection charges, the genuine exterior $+1$, and the shortened final block;
- actual column content and the full primitive-norm cancellation.

Two additional results are proved:

1. A **finite quotient relation for the actual recurrence propagators**, with explicit preperiod and period bounds. This supplies the missing compression of Turn 7’s three recurrence-generated input columns.

2. A **relative logarithmic protection bound at the true primitive norm**:
   

$$
v_{29}\!\left(
   \frac{M}{D}-\frac{M^{(e)}}D
   \right)
   \ge N_{\log}-c-3-\nu,
$$


   where
   

$$
P=29^cx,\qquad
   v_{29}(x^Tx)=\nu.
$$


   Thus logarithmic omission in the required ratio modulo $29$ is justified if
   

$$
N_{\log}\ge c+4+\nu.
$$



These are genuine evaluation and protection results. They are **not** an evaluated invariant of the actual norm and mixed channels. I do not prove a conserved form forcing


$$
\chi+\mathcal N(\alpha-29\rho_n)\in29^2\mathcal N\mathbb Z_{29},
$$


and I do not produce a nonzero actual normalized defect on an original index.

Accordingly, the assignment’s central all-depth alignment obligation remains open. The exact missing statement and a verifiable normalized-defect certificate are specified below.

No tools were executed.

---

## 1. Domain, notation, and audit scope

Put $p=29$. Throughout, the original parameters are


$$
a=432827+682892t,\qquad b=3^a,\qquad n=2001b,
$$


with


$$
t\ge0,\qquad t\equiv364\pmod{841}.
$$



The contact coordinates are exactly


$$
0\le i,j<b,
$$


and the reconstructed coordinates are exactly


$$
0\le j\le b.
$$



Retain


$$
W_j=\binom{n+2}{j},\qquad
\omega_j=j!W_j,
$$




$$
(Cx)_j=jx_{j-1}-x_j,\qquad
\mathcal R=\operatorname{diag}(W_j)C,
$$


with the endpoint interpretation of $C$: its first row is $-x_0$, its last row is $bx_{b-1}$, and no additional contact coordinate is introduced.

The actual systems and reconstructed columns are


$$
A=\widetilde N(I+S)^n,\qquad
A\theta=f^0,\qquad A\psi=\mathbf r,
$$




$$
Z_w=\mathcal R\theta,\qquad
Y=\mathcal R\psi+W_be_b.
$$


The normalizations remain


$$
P=\frac{Z_w}{p^2},\qquad
Q=\frac Y{p^3},\qquad
D=P^TP,\qquad M=P^TQ.
$$



The complete force is


$$
\mathbf r=\frac{h^e+h^F-A(j!)_{0\le j<b}}{b!}.
$$



### 1.1 Accepted results used at their stated scope

I use the audited conclusions of A4turn17 concerning:

- the complete finite displacement
  

$$
\mathcal DA=-\mathcal VC,\qquad
  \mathcal Df^0=0,\qquad
  \mathcal D\mathbf r=\mathcal Ve_b;
$$


- integral invertibility of the contact system;
- the unit
  

$$
f_0^0=J,\qquad
  J\equiv\prod_{\nu\ge0}j_{n_\nu}\not\equiv0\pmod{29};
$$


- the complete-force terminal residue
  

$$
\psi_{b-1}\equiv0\pmod{29};
$$


- the projection
  

$$
\ell_j=\frac{\omega_b}{\omega_j},\qquad
  \mathscr S=\ell^T\ell\equiv8\pmod{29},\qquad
  \Pi=I-\frac{\ell\ell^T}{\mathscr S}.
$$



The fixed-degree nearest-neighbor route remains closed at its audited scope. It is not reopened here.

### 1.2 Audit of Turn 7

Turn 7’s finite-difference and endpoint factorization is algebraically consistent. In particular:

- the falling-factorial truncation at $s<pK$ is uniform;
- the omitted terms of the infinite convolution are exactly the displayed finite endpoint correction;
- $H\equiv I\pmod p$ and $K^{\mathrm{tail}}\equiv0\pmod p$;
- the endpoint inverse is therefore a unit inverse.

Its limitation is exactly the one stated there: the binomial transforms and Gram accumulation still have original-length ranges. A bounded band width is not a digit compression of those sums.

The two-scalar boundary reduction also survives direct algebraic audit; its precise status is revisited in §8.

### 1.3 What can be reused from A5turn15

The reusable mechanism is the expansion of a normalized finite inverse into bounded-length matrix words, followed by digit evaluation of products of high-index binomial coefficients.

Two qualifications are essential.

1. At an odd prime, the unit-factorial table has a sign twist. It cannot be copied from the binary construction unchanged.

2. To claim compression of all six entries of Turn 7’s Gram matrix, one must also compress $h^{(0)},h^{(1)},\tau$. Merely compressing the actual two force columns does not by itself prove that stronger claim.

Both points are handled explicitly below.

---

# 2. Odd-prime factorial units: the required $29$-digit construction

Fix an absolute precision $p^K$, $K\ge1$, and work in


$$
R_K=\mathbb Z/p^K\mathbb Z.
$$



Define


$$
O_K(N)=\prod_{\substack{1\le r\le N\\p\nmid r}}r\pmod{p^K},
$$


and the factorial unit


$$
U_K(N)=p^{-v_p(N!)}N!\pmod{p^K}.
$$



Every $U_K(N)$ is a unit.

## 2.1 The odd-prime sign

For odd $p$, the product of all units modulo $p^K$ is $-1$. Pairing each unit with its inverse leaves only $1$ and $-1$.

Consequently,


$$
\boxed{
O_K(N+p^K)=-O_K(N)\pmod{p^K}.
}
\tag{2.1}
$$


Thus $O_K$ has period $2p^K$, not generally $p^K$.

Equivalently,


$$
O_K(N)
=
(-1)^{\lfloor N/p^K\rfloor}
O_K(N\bmod p^K).
\tag{2.2}
$$



This sign is part of the unit information needed by the actual Gram calculation.

## 2.2 A least-significant-digit formula

Separating multiples of $p$ gives


$$
U_K(N)=O_K(N)U_K(\lfloor N/p\rfloor).
$$


Iterating,


$$
\boxed{
U_K(N)=\prod_{\ell\ge0}O_K(\lfloor N/p^\ell\rfloor).
}
\tag{2.3}
$$



Write


$$
N=\sum_{h\ge0}N_hp^h,\qquad 0\le N_h<p.
$$


Combining (2.2) and (2.3),


$$
\boxed{
U_K(N)=
(-1)^{\,\sum_{h\ge K}(h-K+1)N_h}
\prod_{\ell\ge0}
O_K\!\left(
\sum_{r=0}^{K-1}N_{\ell+r}p^r
\right)
\pmod{p^K}.
}
\tag{2.4}
$$



The sign exponent is read modulo $2$. To verify it, note that


$$
\sum_{\ell\ge0}\left\lfloor\frac N{p^{K+\ell}}\right\rfloor
\equiv
\sum_{h\ge K}(h-K+1)N_h\pmod2,
$$


because $p$ is odd.

Formula (2.4) uses:

- a window of $K$ consecutive base-$p$ digits;
- the position parity after the first $K$ digits;
- a unit accumulator in $R_K^\times$.

A terminal flush of zero digits completes the last windows. No nonunit is inverted.

## 2.3 Binomial coefficients with large lower indices

For $0\le B\le A$, let


$$
e=v_p\binom AB.
$$


Kummer’s theorem computes $e$ as the number of carries in


$$
B+(A-B)=A.
$$



Then


$$
\boxed{
\binom AB
=
p^eU_K(A)U_K(B)^{-1}U_K(A-B)^{-1}
\pmod{p^K}.
}
\tag{2.5}
$$



The carry count can be clipped at $K$. If a product’s total valuation reaches $K$, that product contributes zero.

For negative upper entries in the finite inverse, use the exact identity


$$
\boxed{
\binom{-n}{d}=(-1)^d\binom{n+d-1}{d},
\qquad d\ge0.
}
\tag{2.6}
$$


At $p=29$, the parity of $d$ is the parity of the sum of its base-$29$ digits. It is not determined by the lowest digit alone.

---

## 3. A precise digit-summation lemma

The construction above gives the following form of the high-index kernel lemma.

### Lemma 1 — Unit-sensitive digit evaluation

Fix $K$. Consider a finite sum over a fixed number of nonnegative integer variables, with exact affine bounds and relations. Suppose its summand is a product of:

- binomial coefficients with nonnegative affine upper and lower arguments;
- polynomial factors;
- signs of affine integer expressions;
- coefficients in $R_K$;
- finite-state weights of the summation variables.

Assume all summation variables have an explicit upper bound in terms of the input parameters.

Then the sum modulo $p^K$ has a finite least-significant-digit base-$p$ transfer. Its state set depends on $K$, the number of variables, the affine coefficients, and the finite-state weights, but not on the magnitudes of the input parameters.

#### Proof

For every binomial factor, introduce digit streams for its upper argument, lower argument, and their difference. Finite carry registers verify the affine relations and the binomial validity conditions. They also accumulate Kummer valuations.

Formula (2.4) supplies the factorial units, and (2.5) supplies the binomial residue. Polynomial residues and signs require only finite additional registers.

Inequalities are checked by finite borrow registers. The stipulated upper bound fixes a common digit length; zero padding and terminal carry conditions ensure that each valid integer tuple is counted exactly once.

At each digit, sum over all admissible choices of summation-variable digits. Multiply by the transition weights, and sum final accepting weights. This is precisely the requested finite sum. ∎

This is a construction of the residue, not only an assertion of automaticity. It retains all unit factors and all finite bounds.

---

# 4. Normalized forcing at precision $29^K$

Set


$$
a_s(n)=[z^s]\phi(z)^n,\qquad
\phi(z)=1-z+\frac{z^2}{2}.
$$



Every $a_s(n)$ is $29$-integral. It can be generated without nonunit modular division:


$$
\boxed{
a_s(n)=(-1)^s
\sum_{v=0}^{\lfloor s/2\rfloor}
2^{-v}\binom n{s-v}\binom{s-v}{v}.
}
\tag{4.1}
$$



## 4.1 Complete factorial/exponential force

The exact normalized factorial/exponential force is


$$
r_i^{(e)}
=
\sum_s a_s(n)(n+i)_{\underline s}
\sum_{t\ge0}
\binom{2n+i-s}{b+t}\frac{(b+t)!}{b!}.
$$



Using


$$
(n+i)_{\underline s}=s!\binom{n+i}{s},
\qquad
\frac{(b+t)!}{b!}=t!\binom{b+t}{t},
$$


we obtain


$$
\boxed{
r_i^{(e)}
\equiv
\sum_{\substack{0\le s<pK\\0\le t<pK}}
a_s(n)s!t!
\binom{n+i}{s}
\binom{b+t}{t}
\binom{2n+i-s}{b+t}
\pmod{p^K},
}
\tag{4.2}
$$


with the original validity restrictions retained.

Indeed, $s\ge pK$ makes the first falling factorial divisible by $p^K$, while $t\ge pK$ makes $t!$ divisible by $p^K$.

The lower index $b+t$ is still genuinely large. It is evaluated by the digit transfer; it is not replaced by a small index or by a bounded-degree Newton polynomial.

## 4.2 Complete logarithmic budget and the exceptional branch

Retain the audited whole-force bound


$$
r^F\in p^{N_{\log}}\mathbb Z_p^b,
$$


where


$$
\boxed{
N_{\log}
=
2F_n-F_b-\left\lfloor\log_p(2n+b-1)\right\rfloor,
\qquad F_m=v_p(m!).
}
\tag{4.3}
$$



On the present original family,


$$
\boxed{N_{\log}\ge b.}
\tag{4.4}
$$



For completeness, $F_n\ge n/29=69b$, $F_b\le b/28$, and


$$
\left\lfloor\log_{29}(4003b-1)\right\rfloor\le b+2.
$$


The latter follows from $4003b<29^{b+3}$, first checked at $b=1$ and then preserved on increasing $b$. These inequalities give (4.4), with ample margin.

Therefore:

- if $K\le N_{\log}$, the complete logarithmic force is zero modulo $p^K$;
- if $K>N_{\log}$, then
  

$$
b<K,\qquad n<2001K.
  \tag{4.5}
$$



In the second branch, the original finite system itself has size bounded in terms of $K$. The complete logarithmic values can be generated exactly from


$$
u_0=u_1=1,\qquad u_m=u_{m-1}-\frac12u_{m-2},
$$




$$
L_0=0,\qquad
L_m=mL_{m-1}+2(m-1)!u_{m-1},
$$


and the supplied complete force formula.

This branch is a bounded exact rational calculation. It does not silently divide by a nonunit modulo $p^K$, and it does not return to an unrestricted original-size raw-factorial computation.

## 4.3 The first force and both complete initial entries

The first force admits a binomial-product formula:


$$
\boxed{
J_i=
\sum_{v=0}^{\lfloor n/2\rfloor}
\binom nv
\binom{2n-2v+i}{n-2v}.
}
\tag{4.6}
$$


This follows from


$$
1+2t+2t^2=(1+t)^2+t^2.
$$



Hence


$$
f_i^0=\frac{(n+i)!}{n!}J_i
$$


is covered by Lemma 1. In particular, both $f_0^0$ and $f_1^0$ have digit evaluations preserving the actual higher digits of $n$.

The complete initial force entries remain


$$
\boxed{
r_i=
\sum_s a_s(n)(n+i)_{\underline s}
\left(T_{2n+i-s}+\frac{L_{2n+i-s}}{b!}\right),
\qquad i=0,1.
}
\tag{4.7}
$$


No logarithmic initial value is declared zero merely because its interior displacement is homogeneous.

---

# 5. The whole finite inverse as bounded-length contact words

Let


$$
T=(I+S)^n,\qquad
L_{ir}=\binom ir,\qquad
V_{ir}=\binom{n+i}{r},
\qquad 0\le i,r<b.
$$


Finite Vandermonde convolution gives


$$
V=LT.
$$



Write


$$
\widetilde N=V+E.
$$


Modulo $p^K$,


$$
\boxed{
E_{ir}\equiv
\sum_{s=1}^{pK-1}
a_s(n)s!\binom{n+i}{s}\binom{n+i-s}{r}.
}
\tag{5.1}
$$



Because $p\mid n$,

- $a_s(n)\equiv0\pmod p$ for $1\le s<p$;
- $p\mid s!$ for $s\ge p$.

Thus


$$
E\in pM_b(\mathbb Z_p).
$$



It follows that


$$
\boxed{
A^{-1}
\equiv
T^{-1}
\sum_{k=0}^{K-1}(-V^{-1}E)^kV^{-1}
\pmod{p^K}.
}
\tag{5.2}
$$



Every matrix in (5.2) retains its actual $b\times b$ boundary. The factors have explicit entries


$$
(T^{-1})_{rt}
=
\begin{cases}
\binom{-n}{t-r},&t\ge r,\\
0,&t<r,
\end{cases}
\tag{5.3}
$$


and


$$
\boxed{
(V^{-1})_{ri}
=
\sum_{t=\max(r,i)}^{b-1}
\binom{-n}{t-r}(-1)^{t-i}\binom ti.
}
\tag{5.4}
$$



After inserting (5.1) and (5.4), each word in (5.2) becomes a finite sum over $O(K)$ variables, with affine finite bounds and binomial-product weights.

Lemma 1 evaluates these sums by digits. There is no remaining loop over $0,\ldots,b-1$ in the proposed evaluation mechanism.

This replaces Turn 7’s original-length transforms rather than merely renaming them.

---

# 6. Compressing all three recurrence inputs

To compress all six Gram entries, one must also handle


$$
h^{(0)},\qquad h^{(1)},\qquad\tau,
$$


not only $f^0$ and $\mathbf r$.

Retain


$$
\alpha_i=2n+2i+1,
$$




$$
\beta_i=\frac{(n+i)(n+3i-1)}2,\qquad
\gamma_i=\frac{(n+i)(n+i-1)(1-i)}2.
$$



The actual recurrence is


$$
h_{i+1}=\alpha_i h_i-\beta_i h_{i-1}-\gamma_i h_{i-2}
+\text{source}_i,
\qquad1\le i\le b-2,
$$


with $\gamma_1=0$.

## 6.1 A finite quotient theorem for periodic matrix products

Define, for $i\ge2$,


$$
T_i^{\mathrm{rec}}=
\begin{pmatrix}
\alpha_i&-\beta_i&-\gamma_i\\
1&0&0\\
0&1&0
\end{pmatrix}.
\tag{6.1}
$$


Modulo $p^K$,


$$
T_{i+p^K}^{\mathrm{rec}}=T_i^{\mathrm{rec}}.
\tag{6.2}
$$



The following explicit power bound is useful.

### Lemma 2 — Uniform power quotient for $3\times3$ matrices

For every $B\in M_3(R_K)$,


$$
\boxed{
B^{q+\Pi_K}=B^q\qquad(q\ge3K),
}
\tag{6.3}
$$


where


$$
\boxed{
\Pi_K=p^K\operatorname{lcm}(p-1,p^2-1,p^3-1)
=731640\,p^K.
}
\tag{6.4}
$$



#### Proof

The descending sequence


$$
R_K^3\supseteq BR_K^3\supseteq B^2R_K^3\supseteq\cdots
$$


stabilizes by step $3K$, since $R_K^3$ has composition length $3K$.

On the stable image, $B$ is an automorphism. The Fitting decomposition makes this image a direct summand of $R_K^3$, hence a free $R_K$-module of rank at most three.

Modulo $p$, an automorphism of rank at most three has semisimple order dividing


$$
\operatorname{lcm}(p-1,p^2-1,p^3-1),
$$


and its unipotent part has order dividing $p$, since $p>3$. Lifting from modulo $p$ to modulo $p^K$ adds a factor dividing $p^{K-1}$.

Thus the restriction of $B$ to its stable image has order dividing $\Pi_K$. Since $B^q$ maps into that image for $q\ge3K$, (6.3) follows. ∎

This proof retains the actual matrix entries in $R_K$; it is not a valuation-only argument.

## 6.2 Exact interval products

Let $P_K=p^K$, and consider


$$
\mathcal P(u,v)=T_v^{\mathrm{rec}}\cdots T_u^{\mathrm{rec}},
\qquad u\le v.
$$



Write


$$
v-u+1=qP_K+r,\qquad0\le r<P_K,
$$


and let $a=u\bmod P_K$. Set


$$
B_a=T_{a+P_K-1}^{\mathrm{rec}}\cdots T_a^{\mathrm{rec}},
$$




$$
Q_{a,r}=T_{a+r-1}^{\mathrm{rec}}\cdots T_a^{\mathrm{rec}},
\qquad Q_{a,0}=I.
$$


Periodicity gives


$$
\boxed{
\mathcal P(u,v)=Q_{a,r}B_a^q\pmod{p^K}.
}
\tag{6.5}
$$



By Lemma 2, this depends only on:

- $u\bmod p^K$;
- $v-u+1\bmod p^K$;
- $q$ if $q<3K$;
- otherwise $q\bmod\Pi_K$, together with the fact $q\ge3K$.

All these are finite digit data.

In particular, whenever both intervals are inside the actual finite range and the initial interval contains at least $3Kp^K$ factors,


$$
\boxed{
\mathcal P(u,v+\Pi_Kp^K)=\mathcal P(u,v)\pmod{p^K}.
}
\tag{6.6}
$$



Equation (6.6) is an actual quotient transition relation for the recurrence propagator. It compresses those propagators; it does **not** assert the desired norm/mixed alignment.

## 6.3 The homogeneous inputs

At the first step,


$$
h_2=-\beta_1h_0+\alpha_1h_1.
$$


Thus the initial three-vector is


$$
\begin{pmatrix}h_2\\h_1\\h_0\end{pmatrix}
=
\begin{pmatrix}
-\beta_1&\alpha_1\\
0&1\\
1&0
\end{pmatrix}
\begin{pmatrix}h_0\\h_1\end{pmatrix}.
\tag{6.7}
$$



For $j\ge2$, $h_j$ is obtained from (6.7) by the interval product


$$
T_{j-1}^{\mathrm{rec}}\cdots T_2^{\mathrm{rec}}.
$$


Consequently $h_j^{(0)}$ and $h_j^{(1)}$ are finite-state weights of $j$, with state size depending on $K$, not on $b$.

No negative initial index has been introduced.

## 6.4 The complete particular input $\tau$

The source is


$$
\mathcal H_i=(\mathcal Ve_b)_i.
$$


At precision $p^K$,


$$
\boxed{
\mathcal H_i\equiv
\sum_{s=0}^{pK-1}
a_s(n+1)s!\binom{n+i}{s}
\binom{2n+i-s+1}{b}
\pmod{p^K},
}
\tag{6.8}
$$


again with the original validity restrictions.

For $j\ge2$,


$$
\boxed{
\tau_j
=
\sum_{\ell=1}^{j-1}
e_1^T
\left(T_{j-1}^{\mathrm{rec}}\cdots
T_{\ell+1}^{\mathrm{rec}}\right)e_1\,
\mathcal H_\ell.
}
\tag{6.9}
$$


An empty product is the identity.

The propagator in (6.9) is covered by §6.2, and $\mathcal H_\ell$ is covered by Lemma 1. Hence (6.9) is a digit sum with one additional summation variable, not a row-by-row recurrence of length $b$.

This completes the missing compression of the three actual input columns.

---

# 7. The complete six-entry Gram transfer

Define


$$
B_0=\mathcal RA^{-1}h^{(0)},\qquad
B_1=\mathcal RA^{-1}h^{(1)},\qquad
B_*=\mathcal RA^{-1}\tau+W_be_b.
$$


Let


$$
\mathcal B=(B_0,B_1,B_*).
$$



For each input, use the contact-word expansion of §5, with the input digit weights of §6. Reconstruction is performed with the three separate cases:

- $j=0$:
  

$$
\mathbf B_0=-\zeta_0;
$$


- $1\le j<b$:
  

$$
\mathbf B_j=W_j(j\zeta_{j-1}-\zeta_j);
$$


- $j=b$:
  

$$
\boxed{
  \mathbf B_b=W_b(b\zeta_{b-1}+e_*^T).
  }
  \tag{7.1}
$$



Thus the genuine exterior $+1$ is preserved explicitly.

Expanding


$$
G^{\mathrm{raw}}_{ab}
=\sum_{j=0}^b(\mathbf B_j)_a(\mathbf B_j)_b
$$


introduces only one more summation variable, the actual coordinate $j$. Every term is now covered by Lemma 1 and the recurrence-weight construction.

### Theorem 3 — Complete $29$-digit Gram evaluation

For every original index and every $K\ge1$, all six entries of


$$
G^{\mathrm{raw}}=\mathcal B^T\mathcal B\pmod{p^K}
$$


have a finite base-$29$ digit-transfer evaluation whose state bound depends on $K$, but not on $b$.

The transfer reads the actual digits of $n,b$, enforces every original finite bound, and retains the full factorial and binomial units.

The straightforward construction is not claimed to be efficient in $K$. It is, however, independent of the original number of rows except for reading the parameter digits.

## 7.1 Projection and both charges

The charges remain exactly


$$
\boxed{
\ell^TB_0=\ell^TB_1=0,\qquad
\ell^TB_*=W_b.
}
\tag{7.2}
$$


Equivalently,


$$
\ell^TZ_w=0,\qquad \ell^TY=W_b.
$$



Therefore


$$
\boxed{
G=(\Pi\mathcal B)^T(\Pi\mathcal B)
=
G^{\mathrm{raw}}-\frac{W_b^2}{\mathscr S}e_*e_*^T.
}
\tag{7.3}
$$



The projection scalar itself needs no original-length sum. Since


$$
\ell_{b-r}=\frac{(n+2-b+r)!}{(n+2-b)!},
$$


we have, safely,


$$
\boxed{
\mathscr S\equiv
\sum_{r=0}^{\min(b,pK-1)}
\left(\frac{(n+2-b+r)!}{(n+2-b)!}\right)^2
\pmod{p^K}.
}
\tag{7.4}
$$


Terms with $r\ge pK$ already vanish before squaring. The inverse of $\mathscr S$ is a demonstrated unit inverse on the preferred family.

## 7.2 Lattice accounting

The audited unweighted kernel basis is saturated:


$$
\ker_{\mathbb Z_p}\mathcal V
=
\mathbb Z_pq_0\oplus\mathbb Z_pq_1\oplus\mathbb Z_pq_*,
$$


where


$$
q_0=CA^{-1}h^{(0)},\quad
q_1=CA^{-1}h^{(1)},\quad
q_*=CA^{-1}\tau+e_b.
$$



After weighting, the relevant saturated coefficient lattice remains


$$
\boxed{
\Lambda_{\mathrm{wt}}
=
\left\{
s\in\mathbb Q_p^3:
\mathbf B_js\in\mathbb Z_p
\text{ for every }0\le j\le b
\right\}.
}
\tag{7.5}
$$



Nothing in Theorem 3 replaces this lattice by $\mathbb Z_p^3$. The digit evaluation uses the actual weighted columns and their actual coefficients. It does not use a fictitious unimodular weighting operation or an integral contact lift of the projection.

---

# 8. Exact preferred digits, not a substituted digit family

Write


$$
t=364+841u,\qquad u\ge0.
$$


Then


$$
\boxed{
a=a_*+Au,\qquad
a_*=249005515,\qquad
A=574312172=28\cdot29^5.
}
\tag{8.1}
$$


Thus the actual input is


$$
\boxed{
b=3^{249005515}\left(3^{574312172}\right)^u,\qquad
n=2001b.
}
\tag{8.2}
$$



For any requested digit length $L$, the exact prefix is specified by


$$
b\bmod29^L
=
3^{\,249005515+574312172u}\bmod29^L,
\qquad
n\bmod29^L=2001b\bmod29^L.
\tag{8.3}
$$



No high digit is set to zero except after the true terminal digit of the integer.

The supplied low digits


$$
n_0,n_1,n_2,n_3=0,7,24,7
$$


remain unchanged. They are not treated as a specification of the rest of the input.

## 8.1 What original reachability does prove

Since


$$
3^{28}\equiv1+15\cdot29\pmod{29^2},
$$


we have


$$
v_{29}(3^A-1)=6.
$$


Therefore, for nonnegative integers $u,v$,


$$
\boxed{
v_{29}(b(u)-b(v))=6+v_{29}(u-v)
\qquad(u\ne v).
}
\tag{8.4}
$$



Consequently, finite refinement of the original $u$-parameter gives the usual unique next-digit lifting within the corresponding $29^6$-cylinder.

This does **not** authorize replacing the original family by arbitrary full digit strings. Nor does finite $29$-adic reachability alone prove preservation of an independently required real analytic window.

No new digit restriction or new subsequence is imposed in this report. All statements above hold on the entire retained preferred family, and hence remain available on any already accepted analytic-window subsequence.

---

# 9. Audit of the two-scalar reduced force law

Set


$$
f=(f_0^0,f_1^0,0)^T,\qquad
r=(r_0,r_1,1)^T,
$$


so that


$$
Z_w=\mathcal Bf,\qquad Y=\mathcal Br.
$$



Define


$$
\alpha=\frac{r_0}{f_0^0}\in p\mathbb Z_p,\qquad
\Delta=r_1-\frac{f_1^0}{f_0^0}r_0.
$$


With


$$
H_1=f^TGe_1,\qquad H_*=f^TGe_*,
$$


we have exactly


$$
U:=Y^\parallel-\alpha Z_w
=\Delta B_1+\Pi B_*,
$$


and


$$
\boxed{
\chi=Z_w^TU=\Delta H_1+H_*.
}
\tag{9.1}
$$



Write


$$
P=p^cx,\qquad
x^Tx=\mathfrak a\mathfrak b,\qquad
\mathfrak a\in\mathbb Z_p^\times,
$$


and put


$$
\nu=v_p(\mathfrak b).
$$


Then


$$
\boxed{
\mathcal N=Z_w^TZ_w
=p^{2c+4}\mathfrak a\mathfrak b.
}
\tag{9.2}
$$



The audited channel polarization gives


$$
\mathcal E_{\mathrm{force}}
=
\frac{2\chi}{p^{c+2}\mathfrak a}
-\frac{\mathfrak b}{\mathfrak a}s_U.
$$


Since $U\in p^3\mathbb Z_p^{b+1}$, also $s_U\in p^3\mathbb Z_p$. Hence


$$
\boxed{
\mathcal E_{\mathrm{force}}\in p^3\mathfrak b\mathbb Z_p
\iff
\chi\in p^{c+5}\mathfrak b\mathbb Z_p.
}
\tag{9.3}
$$



This validates Turn 7’s norm-factor criterion, but not its satisfaction by the actual family.

## 9.1 The final numerator condition implies the preliminary norm factor

There is a useful logical simplification.

Suppose


$$
\boxed{
\chi+\mathcal N(\alpha-p\rho_n)
\in p^2\mathcal N\mathbb Z_p.
}
\tag{9.4}
$$


Because $\alpha-p\rho_n\in p\mathbb Z_p$,


$$
\chi\in p\mathcal N\mathbb Z_p.
$$


Thus


$$
v_p(\chi)\ge2c+5+\nu\ge c+5+\nu,
$$


since $c\ge0$. By (9.3), the preliminary force norm factor follows.

Therefore a direct proof of (9.4) would settle both local obligations without first dividing by $\mathfrak b$. This avoids a circular preliminary division.

It still does not prove (9.4).

---

# 10. A new relative logarithmic protection theorem

Let $Y^{(e)}$ be reconstructed from the complete factorial/exponential part of the normalized force, while retaining the exterior $W_be_b$. Define


$$
M^{(e)}=P^T\frac{Y^{(e)}}{p^3}.
$$



### Proposition 4 — Protection at the actual primitive norm

On every retained original index,


$$
\boxed{
v_p(M-M^{(e)})\ge c+N_{\log}-3,
}
\tag{10.1}
$$


and


$$
\boxed{
v_p\!\left(\frac MD-\frac{M^{(e)}}D\right)
\ge N_{\log}-c-3-\nu.
}
\tag{10.2}
$$



In particular, if


$$
\boxed{
N_{\log}\ge c+4+\nu,
}
\tag{10.3}
$$


then


$$
\boxed{
\frac MD\equiv\frac{M^{(e)}}D\pmod p.
}
\tag{10.4}
$$



#### Proof

The complete logarithmic input has depth at least $N_{\log}$. Integral contact inversion and reconstruction give


$$
Y-Y^{(e)}\in p^{N_{\log}}\mathbb Z_p^{b+1}.
$$


Since $P=p^cx$,


$$
M-M^{(e)}
=
p^{-3}P^T(Y-Y^{(e)})
$$


has valuation at least $c+N_{\log}-3$.

The actual norm has


$$
v_p(D)=2c+\nu.
$$


Dividing by the nonzero $D$ proves (10.2), and (10.3) implies (10.4). ∎

This pays the entire primitive-norm loss $\nu$. It does not replace it by common column content.

The proposition also explains why absolute logarithmic negligibility is not enough: if $\nu$ is deeper than expected, the normalized ratio can still detect the logarithmic force.

---

# 11. What the transfer does not prove

Let


$$
\mathcal C=Z_w^TY^\parallel=Z_w^TY=p^5M.
$$


The desired numerator is


$$
\mathcal F
=
\chi+\mathcal N(\alpha-p\rho_n)
=
\mathcal C-p\rho_n\mathcal N.
\tag{11.1}
$$



The construction above evaluates $\mathcal N,\chi,\mathcal C,\mathcal F$ at any prescribed absolute precision, with all units retained.

It does not prove


$$
\boxed{
v_p(\mathcal F)\ge v_p(\mathcal N)+2
}
\tag{11.2}
$$


on the original family.

The recurrence quotient relation (6.6) is insufficient for this purpose. It controls finite-state evaluation of the input recurrence. It does not identify the norm and mixed output functionals after:

- contact inversion;
- weighted reconstruction;
- projection;
- summation over the exact endpoint-sensitive coordinate range;
- actual content removal;
- primitive-norm cancellation.

Similarly, the fact that every finite prefix in the preferred $29$-adic cylinder is reachable does not prove that the Gram defect is determined by a fixed prefix. The transfer explicitly retains higher-digit effects.

No nonzero actual normalized defect has been computed here. Thus there is no original-family counterexample to alignment in this report.

---

## 12. A concrete normalized-defect certificate

There is a particularly clean way to test the outstanding law without separately estimating content.

Let


$$
d=v_p(\mathcal N)=2c+4+\nu.
$$


Positivity of the nonzero first-column real norm proves $\mathcal N\ne0$, so $d$ is finite.

Compute


$$
\mathcal N\bmod p^{d+1},
\qquad
\mathcal C\bmod p^{d+2}.
$$



There are two cases.

### Case A: $v_p(\mathcal C)<d+1$

Then


$$
\frac{\mathcal C}{p\mathcal N}
=\frac MD
$$


is nonintegral. The desired alignment with the unit $\rho_n$ fails.

### Case B: $v_p(\mathcal C)\ge d+1$

The actual normalized defect modulo $p$ is


$$
\boxed{
\delta_{\mathrm{act}}
=
\left(\frac{\mathcal C}{p^{d+1}}\right)
\left(\frac{\mathcal N}{p^d}\right)^{-1}
-\rho_n
\pmod p.
}
\tag{12.1}
$$


Only the demonstrated unit $\mathcal N/p^d$ is inverted.

Then


$$
\boxed{
\delta_{\mathrm{act}}=0
\iff
\mathcal F\in p^2\mathcal N\mathbb Z_p.
}
\tag{12.2}
$$



This certificate uses the **whole actual norm**, including all primitive cancellation. It is not a test at a surrogate depth.

The required absolute precision is exactly


$$
\boxed{
K=d+2=2c+6+\nu.
}
\tag{12.3}
$$



A nonzero value in (12.1) at one original index would refute the claimed universal alignment at that index. Zero values at finitely many indices would establish only those finite cases.

---

## 13. The next mathematical lemma

The remaining local target can now be stated directly in terms of the explicit transfer.

> **Original-family norm-relative transfer lemma — open.**  
> Let the norm and mixed output channels be constructed from (4.2), (4.6)–(4.7), (5.1)–(5.4), (6.5)–(6.9), and the endpoint reconstruction (7.1). On the original orbit
> 

$$
> b=3^{249005515}\left(3^{574312172}\right)^u,\qquad
> n=2001b,\qquad u\ge0,
>
$$


> prove
> 

$$
> \mathcal C-p\rho_n\mathcal N
> \in p^2\mathcal N\mathbb Z_p,
>
$$


> with $\mathcal N\ne0$, or produce an original index with the nonzero certificate (12.1), or with the failure in Case A.

A successful proof must exhibit a relation between the **actual output functionals**, not merely between internal recurrence states. Possible mechanisms remain a conserved bilinear form, an output-compatible quotient under the original multiplication update, or an original-family induction. None is established here.

This is the precise point at which the present assignment remains incomplete.

---

# 14. Bounded exact arithmetic for inspection

The following checks are proposed, not executed.

## A. Odd-prime factorial-unit audit

Use


$$
p=29,\qquad K\in\{1,2\},
\qquad 0\le B\le A\le1685.
$$



Compare exact binomial reduction with:

1. Kummer carry valuation;
2. the sign-sensitive formula (2.4);
3. the unit quotient (2.5).

**Expected verifiable output:** zero discrepancies.

Mandatory individual checks include


$$
O_1(29)\equiv-1\pmod{29},
$$




$$
\binom{58}{29}\equiv2\pmod{29},
$$


and


$$
\frac1{29}\binom{29^2}{29}\equiv1\pmod{29}.
$$



The first check specifically detects an incorrect odd-prime adaptation that drops the sign.

## B. Recurrence-propagator quotient audit

Use


$$
n=29,\qquad K\in\{1,2\}.
$$


For starting phases


$$
a\in\{2,28,29,p^K-1\},
$$


compare direct products with (6.5), using lengths


$$
0,\ 1,\ p^K-1,\ p^K,\ p^K+1,\ 3Kp^K,\ (3K+1)p^K+1.
$$



Also verify by modular matrix powering


$$
B_a^{3K+\Pi_K}-B_a^{3K}=0\pmod{p^K}.
$$



**Expected verifiable output:** zero matrices in every comparison.

These are auxiliary implementation checks. The all-matrix quotient theorem rests on Lemma 2, not on the finite table.

## C. Complete six-entry Gram audit

Use


$$
p=29,\qquad n=29,\qquad b=4,\qquad K=2.
$$



Compute the three columns:

- by direct exact inversion and reconstruction;
- by the contact-word digit expansion and recurrence-propagator weights.

Project using the actual auxiliary $\ell$, not the original-family residue $\mathscr S\equiv8$.

**Expected verifiable outputs:**

- zero difference modulo $29^2$ in all reconstructed coordinates;
- zero difference modulo $29^2$ in all six projected Gram entries;
- the common reduction
  

$$
\boxed{
  G\equiv
  \begin{pmatrix}
  21&19&0\\
  19&5&0\\
  0&0&0
  \end{pmatrix}
  \pmod{29}.
  }
$$



For a complete-force comparison in this auxiliary system, generate the actual logarithmic coefficients rather than invoking an original-family size bound.

## D. Preferred-parameter audit

Check exactly


$$
432827+682892(364+841u)
=
249005515+574312172u,
$$




$$
3^{28}\equiv1+15\cdot29\pmod{29^2}.
$$



For the smallest preferred parameter $u=0$, calculate


$$
3^{249005515}\bmod29^6
$$


by modular exponentiation and compare it with the retained deep-refinement residue $B=410910916$. Then multiply by $2001$ and verify the supplied low $n$-digits.

**Expected verifiable output:** agreement of the preferred prefix and the original parameter formula. This is a prefix audit, not a Gram-law calculation.

## E. What an original normalized-defect receipt must contain

After the transfer implementation is audited, any bounded original-index computation should report:

1. the exact original parameter $u$;
2. the actual parameter digit streams, or a verifiable exact construction of them;
3. the requested absolute precision $K$;
4. $\mathcal N,\mathcal C\bmod29^K$;
5. whether $d=v_{29}(\mathcal N)$ has been certified by a nonzero digit;
6. if $d+2\le K$, the certificate (12.1), including the independently retained $\rho_n\bmod29$;
7. the complete logarithmic budget and whether omission was justified;
8. the separate endpoint contributions.

If $\mathcal N\equiv0\pmod{29^K}$, the correct output is only


$$
v_{29}(\mathcal N)\ge K.
$$


It is not an alignment certificate.

No actual value of $\delta_{\mathrm{act}}$ is predicted without performing this calculation.

---

# 15. Nonvanishing, full gcd, primitive denominator, and whole error

The original finite boundaries are unchanged. In a block decomposition with block size $29^4$, the last block is shortened at $j=b$; it is not filled to a complete block. The recurrence stops at $i=b-2$, and the exterior term remains the separate $j=b$ contribution.

The actual norm is nonzero:


$$
D=P^TP>0.
$$


Mixed nonvanishing retains its supplied original-family dependency. A zero modular residue is not a proof that the mixed integer is zero.

The least actual two-column clearer and integer Gram pair remain


$$
N_B=d_B[u,v],\qquad v_{29}(d_B)=0,
$$




$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2}.
$$



The final reduction is still


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
p_n=\frac{H_B}{g_B},\qquad
q_n=\frac{A_B}{g_B}>0.
}
\tag{15.1}
$$


The primitive multiplier remains $d_B^2/g_B$.

With


$$
\delta=v_{29}(D),\qquad\mu=v_{29}(M),
$$


retain


$$
v_{29}(g_B)
=
\min\{4F_n+4+\delta,\ 2F_n+F_b+5+\mu\},
$$




$$
\boxed{
v_{29}(q_n)
=
\max\{0,\ 2F_n-F_b-1+\delta-\mu\}.
}
\tag{15.2}
$$



An affirmative local alignment law would give $\delta=\mu$, since $\rho_n$ is a unit. It would still settle only the $29$-part of the denominator. The actual denominator obeys


$$
\boxed{
\log q_n
=
\sum_{\ell}
\max\{v_\ell(A_B)-v_\ell(H_B),0\}\log\ell.
}
\tag{15.3}
$$



No all-prime bound for (15.3) is proved here.

Finally, with


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


the whole evaluated form is


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n.
}
\tag{15.4}
$$


At the retained hypotheses and proof status of the complete signed-error theorem,


$$
\epsilon_n>0\quad\text{eventually},
$$


and


$$
\log|\epsilon_n|
=
-\left(2+\frac1{2001}\right)n\log(1+\sqrt2)+o(n).
$$



No individual exponential, logarithmic, or endpoint error component replaces this whole error.

---

# Final proof-status ledger

| Statement | Status |
|---|---|
| Turn 7 band/endpoint factorization | Algebraically valid at its finite-precision scope |
| Turn 7 two-scalar boundary contraction | Valid identity and criterion |
| Odd-prime unit-factorial digit formula, including signs | Proved here |
| Bounded contact-word expansion of the normalized finite inverse | Proved here |
| Finite quotient relation for the actual recurrence propagators | Proved here |
| Digit compression of $h^{(0)},h^{(1)},\tau$ | Proved here |
| Entire six-entry endpoint-exact Gram digit transfer | Proved here |
| Replacement of weighted saturation by $\mathbb Z_{29}^3$ | Not made |
| Relative logarithmic protection at actual primitive norm | Proved here, with explicit threshold |
| Final numerator condition implies the preliminary norm factor | Proved here |
| Conserved output relation forcing actual all-depth alignment | Not obtained |
| Nonzero actual normalized defect on an original index | Not obtained |
| Full all-prime primitive-denominator bound | Open |
| Whole nonzero evaluated form tends to zero | Open |

## Conclusion

The new result is a **complete, unit-sensitive, endpoint-exact $29$-digit compression of the actual three-column Gram calculation**, together with an explicit recurrence quotient relation and a relative logarithmic protection theorem.

The exact remaining local bottleneck is no longer original-length evaluation. It is the mathematical relation


$$
\boxed{
\mathcal C-29\rho_n\mathcal N
\in29^2\mathcal N\mathbb Z_{29}
}
$$


at the first nonzero digit of the **actual** norm.

That relation has neither been proved nor refuted here. The normalized certificate (12.1) specifies exactly what a finite original-index obstruction would have to exhibit.

Even a proof of this local relation would leave the full all-prime gcd and the comparison of the actual primitive denominator with the whole signed error.



$$
\boxed{
\text{An unconditional proof or disproof of irrationality of }e+\pi
\text{ remains unresolved.}
}
$$


