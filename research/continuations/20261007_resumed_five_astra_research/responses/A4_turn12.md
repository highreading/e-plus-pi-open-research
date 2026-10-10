> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the precision-$29$ ternary reduction and the complete binary modulus-$8$ calculation

## Executive conclusions

The global objective remains open. **Neither supplied construction proves that $e+\pi$ is rational or irrational.**

The two new local calculations nevertheless survive review, provided their previously established tools are used at exactly their stated original-family scope.

1. **Ternary calculation.** The complete low-degree moment formula modulo $3^{29}$, the corrected-column substitution, the finite prefix convolution, and the first-radical elimination are valid. The supplied old premise
   

$$
d_{\rm act}\in3^{-1}\mathbb Z_3
$$


   is precisely what is needed to justify the claimed complete diagonal valuation:
   

$$
v_3(\lambda^{(2)})=-1.
$$


   No stronger premise about the original diagonal is required.

2. **Second ternary operator.** On the specified fixed original subwindows,
   

$$
\frac{\mathcal S^{(2)}_{uv}}9
   \equiv [y^{E-u-v}](1-y)^{-b}\pmod3.
$$


   Its rank is exactly $b$, and its full radical is exactly
   

$$
(y-1)^b\mathbb F_3[y]_{\le b/2}.
$$


   The endpoint is nonzero on that radical. The endpoint-annihilating restriction therefore has rank $b$ and nullity $b/2$.

3. **Binary calculation.** The finite inverse modulo $8$, all four contact-row classes, the physical terminal, the sharp $a=1$ criterion, the complete exponential-source divisibility, and the evaluated linear norm acceptance are valid on the unchanged binary original family. In particular,
   

$$
\tau\in8\mathbb Z_2^{b+1},\qquad E\in2\mathbb Z_2,
$$


   and
   

$$
S\in8\mathbb Z_2,\qquad x^Tx\in8\mathbb Z_2,\qquad
   a=1\Longrightarrow Q\equiv0\pmod2.
$$



4. **Finite certificates.** Acceptance of the binary theorem promotes the supplied two-cost certificate to a complete classification of the $a=1$ question at its **21 stated original indices**. It proves $a(u)\ge2$ there, not an exact higher content and not a universal lower bound. The ternary auxiliary certificate remains a check of one auxiliary coefficient family; it does not establish actual producer scope or original-index infinitude.

5. **New result of this review.** A correctly paid, endpoint-adapted elimination of the rank-$b$ ternary block gives an exact residual cofactor normal form. It identifies a precise cancellation threshold: after the known common factors have been removed, unfavorable relative-cofactor cancellation can occur only at a particular determinant-valuation equality. It also gives an explicit next accepting lemma and countermodels showing why the present low-digit data do not establish that lemma.

No closed producer calculation, old modulus-$4$ proof, old mask enumeration, or completed certificate is repeated below.

---

## 1. Original objects and the scope of reuse

### 1.1 Ternary family

Throughout the ternary discussion retain


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




$$
m=2^{2j-1},\qquad n=4^j+1,\qquad A=4^j-1=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$


and


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$



Writing $x=y-1$, the finite coordinates are


$$
U_u=x^u\quad(0\le u<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),
$$




$$
Y_a=y^a\quad(d\le a\le m),\qquad
\nu=\frac D2-1,\qquad d=D+\nu.
$$


The physical HIGH terminal remains $Y_m$.

The complete functional is


$$
\mathcal M(P)=
-\frac{3^h}{4}\mathfrak f(P)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](P-P(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^t)=(2t)!.
$$


Its denominator cutoff is


$$
2v+1\le4H-4D+5.
$$



The core and corrected columns remain


$$
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=-71-A,
$$




$$
G_c(f,g)=\mathcal M(Q_cfg),\qquad
F=Z-WE_c^{-1}C_c,\qquad W=[U\ Y].
$$



The following are reused, not reproved:

- exact core orthogonality $G_c(W,F)=0$;
- the integral unimodular basis $[W,F]$;
- $S_c=G_c(F,F)\in3^{26}M$;
- the nested corrected-column support theorem through precision $20$, including its degree gap;
- the accepted actual/core transport through precision $28$;
- the reviewed next-producer identity
  

$$
\frac{S_{\rm act}-S_c}{3^{28}}
  \equiv-\kappa(\delta t^T+t\delta^T)\pmod3,
  \qquad
  t_i=\frac{[y^m]F_i}{3^{20}};
$$


- the actual endpoint reduction
  

$$
\bar e_{{\rm act},i}=(-1)^i;
$$


- the supplied original diagonal bound
  

$$
d_{\rm act}=w^TE_{\rm act}^{-1}w\in3^{-1}\mathbb Z_3.
$$



In the adjacent domain,


$$
P_0=243P,\qquad N_0=243r,\qquad D=P_0+N_0,
$$




$$
P=3^{h-32},\qquad r\equiv2\pmod9,\qquad r\ \text{odd},
$$


and the original relation


$$
4^j=243(3^{26}-1)P-243r+1
$$


is retained.

The new ternary analysis uses a fixed open original subwindow whose closure lies in


$$
\frac1{10}<\frac{N_0}{P_0}<\frac{19}{180}.
$$


Original-index infinitude here is inherited only from the previously established density theorem. It is not inferred from auxiliary pairs $(P,r)$.

### 1.2 Binary family

The binary discussion uses the distinct original family


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0,
$$


with


$$
h=\frac n2=2001b,\qquad d=\frac{b-1}{4},\qquad
g=\frac{h+1}{2}.
$$



Contact coordinates are $0\le i,j<b$; physical reconstruction has $0\le j\le b$. For a contact vector $z$,


$$
\Delta_jz=jz_{j-1}-z_j,\qquad z_{-1}=z_b=0,
$$




$$
W_j=\binom{n+2}{j},\qquad
(\mathcal Rz)_j=W_j\Delta_jz.
$$



Retain the complete columns


$$
x=\frac12\mathcal RA^{-1}\mathfrak f,\qquad
y=\frac{\mathcal RA^{-1}(h^e+h^F)+e_0}{4b!}.
$$


In particular, $h^F$ is not deleted.

Write


$$
z^f=A^{-1}\mathfrak f,\qquad x=2^ax_0,
$$


where $a$ is the actual minimum coordinate valuation, and


$$
z^k=A^{-1}k,\qquad
k=\frac{h^e-A(j!)_{0\le j<b}}{b!}.
$$



The whole force modulo $8$, the original modulus-$4$ obstruction $a\ge1$, and the scoped higher-precision completion results are reused.

---

# Part I. Ternary review

## 2. The complete low-degree moment formula

Set


$$
L_s=\mathcal M((y+1)x^Hy^s).
$$



### 2.1 Exact evaluation of the pole sum

For $0\le s\le2D$, the endpoint quotient is $x^Hy^s$, and its complete support lies within the original cutoff. The elementary beta-integral identity gives


$$
\begin{aligned}
\sum_{k=0}^{H}
\frac{(-1)^{H-k}\binom Hk}{2s+2k+1}
&=\int_0^1t^{2s}(t^2-1)^H\,dt\\
&=-\frac{2^HH!}{\prod_{k=0}^{H}(2s+1+2k)},
\end{aligned}
$$


because $H$ is odd.

For sufficiently large original tuples, the factorial part is zero modulo $3^{29}$. Hence


$$
L_s\equiv
-\frac{3^h2^HH!}
{\prod_{k=0}^{H}(2s+1+2k)}
\pmod{3^{29}}.
\tag{2.1}
$$



This evaluates the entire finite pole sum. It does not select only a favorable pole.

For the rational expression on the right, the inequalities


$$
2s+1<H,\qquad 2s+2H+1<3H
$$


allow exact valuation counting. For every $3^q\mid H$, the denominator contains $H/3^q$ complete residue cycles and one additional multiple precisely when $3^q\mid2s+1$. There is no multiple of $3H$. Consequently,


$$
v_3(\text{right side of }(2.1))
=h-v_3(2s+1).
\tag{2.2}
$$



The qualification “for the rational expression” matters: where this valuation is as large as $h$, the factorial term may affect the exact valuation of $L_s$. At the digits $26,27,28$ used below, it cannot.

### 2.2 The normalized unit

Define, for the rational expression,


$$
U_s=\frac{(2s+1)L_s}{3^h}.
$$


Then


$$
U_s=U_0\prod_{j=1}^{s}
\left(1+\frac{2H}{2j+1}\right)^{-1},
$$


and


$$
U_0=-\frac{4^H}{(2H+1)\binom{2H}{H}}.
$$



For powers $H\ge27$,


$$
4^H\equiv1\pmod{27},\qquad
\binom{2H}{H}\equiv20\pmod{27}.
$$


The central-binomial congruence follows by separating factors divisible by $3$:


$$
\frac{\binom{2H}{H}}{\binom{2H/3}{H/3}}
=
\prod_{\substack{1\le k\le H\\3\nmid k}}
\left(1+\frac Hk\right).
$$


This product is $1\pmod{27}$ for $H\ge27$; at $H=9$, the linear correction also vanishes modulo $27$. The base value is $\binom63=20$.

Since $20^{-1}\equiv23\pmod{27}$,


$$
U_0\equiv-23\equiv4\pmod{27}.
$$


For $s\le2D$, each factor in $U_s/U_0$ is $1\pmod{27}$, with a much larger original-family valuation margin. Thus


$$
U_s\equiv4\pmod{27}.
\tag{2.3}
$$



### 2.3 All surviving coefficient locations

Let


$$
\mu=\frac{P_0}{3}=3^{h-28},\qquad
c_a=\frac{a\mu-1}{2}.
$$


The condition $s\le2D$ permits precisely the relevant odd multiples


$$
a=1,3,5,7,9,11,13.
$$


Combining (2.1)–(2.3) gives, for every integral $P$ of degree at most $2D$,


$$
\boxed{
\begin{aligned}
\mathcal M((y+1)x^HP)\equiv{}&
4\,3^{26}P_{c_9}
+4\,3^{27}P_{c_3}\\
&+3^{28}\!\!\sum_{a\in\{1,5,7,11,13\}}
a^{-1}P_{c_a}
\pmod{3^{29}}.
\end{aligned}}
\tag{2.4}
$$



**Decision:** A1turn12’s complete moment formula and its normalized unit are accepted. The cutoff, factorial term, and all surviving denominator valuations are paid.

---

## 3. Corrected-column substitution and all digit orders

This is the most important place to avoid an unpaid extension of the old stationary estimate.

### 3.1 Why precision $20$ is sufficient

Let


$$
F_i^*=F_i+3^{20}\Delta_i
$$


be an integral degree-$\le m$ representative supplied by the support theorem.

Because $[W,F]$ is integral unimodular, write


$$
\Delta_i=Wa_i+Fb_i
$$


with integral coefficient vectors. Exact orthogonality gives


$$
G_c(F,\Delta_i)=S_cb_i\in3^{26}M.
$$


Therefore


$$
G_c(F^*,F^*)-S_c
\in3^{46}M+3^{40}M
\subseteq3^{40}M.
\tag{3.1}
$$



This proves the needed substitution directly. It does **not** assume that the earlier bound


$$
G_c\!\left(\frac{F-T}{9},\frac{F-T}{9}\right)\in3^{24}M
$$


automatically gains another digit.

The degree gap of $F^*=x^D\psi$ also permits digit representatives with the same top-degree bound. Prescribing the already known lower jets introduces no new high-degree coefficients: those jets themselves lie below that bound, and the nested support sets absorb the ensuing coefficientwise carries.

### 3.2 The selected radical

Put


$$
Q=\frac{P_0}{9},\qquad b=Q-N_0,\qquad
\ell=\frac{3b}{2}+1,\qquad E=\frac{Q-3}{2}.
$$


Here $b$ is positive, even, and divisible by $243$, and


$$
0<b<\frac Q6
$$


with fixed positive margin on a fixed interior subwindow.

The first-radical kernel is


$$
K=\{0,\ldots,\ell-1\}.
$$


Its corresponding original middle indices are $i=R_*+u$, where


$$
R_*=\frac{P_0+1}{2}.
$$


The terminal lies in the complementary block $J$, so $\delta|_K=0$.

The retained jets on $K$ are therefore


$$
\phi_{i,0}=y^i,\qquad \phi_{i,1}=0,\qquad
\phi_{i,2}=-y^{H/3+i}\pmod3.
$$



### 3.3 Total digit order two

The complete order-two contribution is


$$
-18\,
\mathcal M\!\left((y+1)x^Hy^{H/3}
x^D(\beta+3y)y^{i+j}\right).
\tag{3.2}
$$



The beta-product argument also applies to the shifted exponent $H/3+s$. Its largest denominator remains below $3H$. Since


$$
v_3(2H/3+2s+1)=v_3(2s+1)
$$


in the relevant low-degree range, the required normalized shifted formula is


$$
\frac{\mathcal M((y+1)x^Hy^{H/3}P)}{3^{26}}
\equiv [y^{c_9}]P\pmod3.
\tag{3.3}
$$


Its normalized unit is $1\pmod3$.

For the $P$ in (3.2), the surviving extraction lies strictly between $N_0$ and $P_0$. But


$$
x^D\equiv(y^{P_0}-1)x^{N_0}\pmod3
$$


has no support there. Thus (3.2) vanishes modulo $3^{29}$.

### 3.4 Total order three

Only


$$
\phi_{i,3}y^j+y^i\phi_{j,3}
$$


occurs.

The unit-weight extraction is absent by degree. In fact, a degree-$\le m$ corrected-column digit paired with a nonterminal $z_j$ has quotient degree at most


$$
H+m+j+1< H+m+\nu=\frac{3H-1}{2}.
$$


The supplied stricter degree gap is more than sufficient.

After excluding that unit pole, the common grid needed for a moment modulo $3^{26}$ is


$$
\frac H{3^{24}}=9P_0.
$$


The retained order-three width is


$$
\frac72D+1<\frac{9P_0-1}{2}.
$$


No half-grid extraction meets the support.

### 3.5 Orders four and higher

For a moment modulo $3^M$, the complete grid, before removing any pole, is at least $H/3^{M-1}$. At total order $s=4$, $M=25$, giving again $9P_0$. The width satisfies


$$
4D+1<\frac{9P_0-1}{2}.
$$



For $4\le s\le8$, the corresponding grids grow by a factor of $3$ per additional explicit digit, while the widths grow only linearly. For $s\ge9$, the retained precision-$20$ grid


$$
\Omega_{20}=\frac H{3^{19}}=3^7P_0
$$


already dominates every retained width, which is at most $21D+1$. Orders carrying $3^{29}$ vanish by integrality.

All polynomials remain in the original degree-$\le2n-1$ functional domain; their endpoint quotients remain within $0\le v\le2n-2$.

Consequently,


$$
\boxed{
(S_c)_{ij}\equiv G_c(z_i,z_j)\pmod{3^{29}}
\qquad(i,j\in R_*+K).
}
\tag{3.4}
$$



**Decision:** The precision-$29$ corrected-column step is valid. The omitted-looking stationary and top-degree hypotheses are supplied by the integral unimodular basis, exact orthogonality, and the stated degree-bounded precision-$20$ representatives. They are not new assumptions.

---

## 4. Core extraction, finite prefix convolution, and first-radical payment

### 4.1 The surviving core coefficient

Apply (2.4) to


$$
P=x^D(\beta+3y)y^{i+j}.
$$


On $K\times K$, the $c_3$ extraction and those with $a\le5$ lie below the minimum degree. The $a=7,11,13$ extractions lie in gaps or above the degree of $x^D$. The fixed subwindow gives positive margins for these exclusions.

The remaining index is


$$
k_{uv}=\frac{P_0-3}{2}-u-v.
$$


It lies, together with $k_{uv}-1$, between


$$
\frac{P_0}{3}+N_0
\quad\text{and}\quad
\frac{2P_0}{3}.
$$


The associated coefficients of $x^D$ are divisible by $9$. Using $\beta\equiv1\pmod9$,


$$
\frac{(S_c)_{R_*+u,R_*+v}}{3^{28}}
\equiv
\frac{[y^{k_{uv}}]x^D}{9}\pmod3.
$$



Modulo $27$, only the band beginning at $4P_0/9$ meets this interval, and


$$
\frac{[y^{4P_0/9}]x^{P_0}}9\equiv1\pmod3.
$$


Hence


$$
\boxed{
\frac{(S_c)_{R_*+u,R_*+v}}{3^{28}}
\equiv[y^{E-u-v}]x^{N_0}\pmod3.
}
\tag{4.1}
$$



### 4.2 The prefix convolution is genuinely finite

Write


$$
U=-S_{\rm act}/3^{26}
=
\begin{pmatrix}\mathsf A&\mathsf B\\
\mathsf B^T&\mathsf C\end{pmatrix},
$$


with prefix length $R_*$. Put


$$
a=\frac{P_0-1}{2},\qquad J_0=\frac{P_0}{3}-1.
$$


The relevant finite coefficients are


$$
(\mathsf A_0^{-1})_{ij}
=[y^{i+j-a}](1-y)^{-N_0},
\qquad 0\le i,j\le a,
$$


and


$$
(\mathsf B_1)_{i,u}
=[y^{J_0-i-u}]x^{N_0}.
$$



Set


$$
k=J_0-i-u,\qquad l=J_0-j-v.
$$


The inverse exponent is


$$
i+j-a=C-u-v-k-l,
\qquad C=\frac{P_0/3-3}{2}.
$$


If all three coefficient indices are nonnegative, then


$$
k\le C-u-v<J_0-u,\qquad
l\le C-u-v<J_0-v.
$$


Thus the lower bounds $i,j\ge0$ do not truncate the convolution. The upper bounds $i,j\le a$ are automatic because $J_0<a$.

Since the two factors $x^{N_0}$ contribute the same minus sign, the finite convolution is


$$
\boxed{
(\mathsf B_1^T\mathsf A_0^{-1}\mathsf B_1)_{uv}
=[y^{C-u-v}](1-y)^{N_0}=-V_{uv}.
}
\tag{4.2}
$$


It vanishes on $K\times K$.

This verifies the finite-boundary assertion rather than replacing it with an infinite convolution.

### 4.3 Producer and first-radical elimination

The reviewed producer update vanishes on $K\times K$, since $\delta|_K=0$. Its changes to the prefix cross correction begin one digit later, as already established in A4turn10.

For


$$
\mathcal R=\mathsf C-\mathsf B^T\mathsf A^{-1}\mathsf B,
$$


we obtain


$$
\frac{\mathcal R_{KK}}9
\equiv-[y^{E-u-v}]x^{N_0}\pmod3.
$$



Now


$$
\mathcal R_{JJ}=3B_J,\qquad B_J\in\operatorname{GL}(\mathbb Z_3),
\qquad \mathcal R_{KJ}\in9M.
$$


The inverse is exactly


$$
\mathcal R_{JJ}^{-1}=3^{-1}B_J^{-1}.
$$


Therefore its matrix correction has valuation at least


$$
2-1+2=3,
$$


and


$$
\boxed{
\frac{\mathcal S^{(2)}_{uv}}9
\equiv-[y^{E-u-v}]x^{N_0}\pmod3.
}
\tag{4.3}
$$



**Decision:** The prefix convolution and the new $3^{-1}$ payment are accepted.

---

## 5. Actual endpoint and complete diagonal

After prefix elimination retain exactly


$$
f=e_R-\mathsf B^T\mathsf A^{-1}e_C,
$$




$$
\lambda=3^{26}d_{\rm act}-e_C^T\mathsf A^{-1}e_C.
$$


After eliminating $J$, retain exactly


$$
f^{(2)}=f_K-\mathcal R_{KJ}\mathcal R_{JJ}^{-1}f_J,
$$




$$
\lambda^{(2)}
=\lambda-f_J^T\mathcal R_{JJ}^{-1}f_J.
\tag{5.1}
$$



Because $\mathsf B\in3M$ and the later endpoint correction lies in $3M$,


$$
\bar f^{(2)}_u=(-1)^{R_*+u}.
\tag{5.2}
$$



The supplied original premise gives


$$
3^{26}d_{\rm act}\in3^{25}\mathbb Z_3.
$$


Since $\mathsf A^{-1}$ is integral, $\lambda\in\mathbb Z_3$. This is the needed payment for dropping $3\lambda$ modulo $3$; the original diagonal itself has not been dropped.

Let


$$
n_J=\frac{Q-4b-5}{2}.
$$


After reindexing $J$, the finite inverse is


$$
(V_{JJ}^{-1})_{\alpha\beta}
=[y^{n_J-1-\alpha-\beta}](1-y)^{-N_0}.
$$


Consequently,


$$
3\lambda^{(2)}
\equiv
[y^{n_J-1}](1+y)^{-2}(1-y)^{-N_0}\pmod3.
\tag{5.3}
$$



In characteristic $3$,


$$
(1-y)^{-N_0}=\frac{(1-y)^b}{1-y^Q}.
$$


The extraction index is below $Q$ and above $b$. For $t\ge\deg P$,


$$
[y^t](1+y)^{-2}P(y)
=(-1)^t\bigl((t+1)P(-1)+P'(-1)\bigr).
$$


With $P=(1-y)^b$, the parity and divisibility of $b$ give


$$
P(-1)=1,\qquad P'(-1)=0
\quad\text{in }\mathbb F_3.
$$


Thus


$$
3\lambda^{(2)}
\equiv(-1)^{n_J-1}n_J\pmod3.
$$


Finally,


$$
n_J\equiv2\pmod3.
$$


Therefore


$$
\boxed{v_3(\lambda^{(2)})=-1.}
\tag{5.4}
$$



**Decision:** This is a valid actual scalar theorem. Its formerly missing original diagonal premise is explicitly supplied in the present packet.

---

## 6. Exact rational-Hankel rank and radical

Since $N_0=Q-b$, $N_0$ is odd, and $E<Q$,


$$
-[y^{E-u-v}]x^{N_0}
=[y^{E-u-v}](1-y)^{-b}.
$$


Let


$$
\mathcal H_{uv}=[y^{E-u-v}](1-y)^{-b},
\qquad 0\le u,v<\ell.
$$



The inequality


$$
E-2(\ell-1)=\frac{Q-3}{2}-3b>0
$$


ensures that every displayed coefficient index is nonnegative.

The sequence of coefficients of $(1-y)^{-b}$ satisfies an order-$b$ recurrence with unit first and last recurrence coefficients. Its consecutive $b\times b$ Hankel blocks are invertible. One can check this without invoking a characteristic-zero rank theorem: begin with the block indexed by $i+j-(b-1)$, which is anti-triangular with unit antidiagonal; forward shifts preserve invertibility through the recurrence with unit last coefficient. This proves


$$
\operatorname{rank}\mathcal H=b.
$$



For


$$
f=(y-1)^bg,\qquad \deg g\le b/2,
$$


one has


$$
(1-y)^{-b}f=g.
$$


The $u$-th pairing is $[y^{E-u}]g$, and


$$
E-(\ell-1)>b/2.
$$


It therefore vanishes. These vectors have dimension


$$
b/2+1=\ell-b,
$$


so they give the entire radical:


$$
\boxed{
\ker\mathcal H=(y-1)^b\mathbb F_3[y]_{\le b/2}.
}
\tag{6.1}
$$



The endpoint is, up to a fixed sign, evaluation at $-1$. On this radical,


$$
((y-1)^bg)(-1)=g(-1).
$$


It is nonzero. Its annihilating radical is exactly


$$
\boxed{
(y+1)(y-1)^b\mathbb F_3[y]_{<b/2}.
}
\tag{6.2}
$$



For completeness, if a linear functional is nonzero on the radical of a bilinear form, its kernel still maps onto the nondegenerate quotient. Hence restricting the form to that kernel preserves its rank. Therefore the endpoint-annihilating restriction has rank $b$ and nullity $b/2$.

**Decision:** The rank, full radical, and endpoint-annihilator claims are accepted. Their proofs work in characteristic $3$; no separability assumption is being smuggled into the repeated-root recurrence.

---

## 7. New result: an endpoint-adapted residual cofactor normal form

The preceding results allow a further exact deduction.

### 7.1 Paying the $3^{-2}$ inverse without changing the diagonal

The reduction of $f^{(2)}$ is nonzero on $\ker\mathcal H$. Choose an integral unimodular basis with:

- a rank-$b$ nondegenerate block lying **exactly** in $\ker f^{(2)}$;
- remaining vectors reducing to the full radical of $\mathcal H$;
- residual endpoint coordinates $(1,0,\ldots,0)$.

Such a basis uses only unit divisions: lift an endpoint-unit radical vector, normalize its endpoint to $1$, and subtract suitable multiples from the other lifts.

In this basis,


$$
\mathcal S^{(2)}
=
\begin{pmatrix}
9C&27X\\
27X^T&27Y
\end{pmatrix},
\qquad C\in\operatorname{GL}_b(\mathbb Z_3).
$$


The newly required inverse is


$$
(9C)^{-1}=3^{-2}C^{-1}.
$$


The residual matrix is


$$
T=27Y-81X^TC^{-1}X=27T_0,
\qquad T_0\in M_r(\mathbb Z_3),
$$


where


$$
r=b/2+1.
\tag{7.1}
$$



Because the eliminated endpoint coordinates are exactly zero, this elimination leaves


$$
\lambda^{(2)}=\frac{\upsilon}{3},
\qquad \upsilon\in\mathbb Z_3^\times
$$


unchanged. This is an advantage of the endpoint-adapted basis, not an assumption that an arbitrary complement has zero endpoint.

Let $M_0$ be the principal submatrix of $T_0$ obtained by deleting the endpoint coordinate.

### 7.2 Exact cofactor formula

The eliminated prefix, first-radical block, and rank-$b$ block contribute a common factor $\chi$ to the distinguished pair. Its valuation is


$$
v_3(\chi)=n_J+2b;
$$


unimodular coordinate changes alter it only by a unit.

The exact remaining pair is


$$
\boxed{
D_0=\chi\,3^{3r}\det T_0,
}
\tag{7.2}
$$




$$
\boxed{
D_1=\chi\,3^{3r-3}
\left(\det M_0-9\upsilon\det T_0\right).
}
\tag{7.3}
$$



This retains the whole bordered diagonal. In particular, the normalized diagonal term is two powers of $3$ deeper than the endpoint minor; it is not identically absent.

Assume $D_0\ne0$, and set


$$
d_0=v_3(\det T_0),\qquad d_M=v_3(\det M_0),
$$


allowing $d_M=+\infty$. Then:

- if $d_M<d_0+2$,
  

$$
v_3D_1-v_3D_0=d_M-d_0-3\le-2;
$$


- if $d_M>d_0+2$,
  

$$
v_3D_1-v_3D_0=-1;
$$


- only if
  

$$
\boxed{d_M=d_0+2}
  \tag{7.4}
$$


  can the two complete terms cancel and produce a larger relative valuation.

Thus unfavorable cancellation is confined to an exact determinant-valuation equality.

This is a new limitation and a new accepting criterion on the correctly paid residual structure. It is not yet an estimate for the actual determinants $T_0,M_0$.

### 7.3 A concrete next accepting lemma

A particularly simple sufficient statement would be:

> **Next accepting lemma.** On an infinite set of the same original ternary indices, the actual endpoint-annihilating residual satisfies
> 

$$
> \det M_0\in\mathbb Z_3^\times,
> \qquad \det T_0\ne0.
>
$$



It would imply


$$
v_3D_0-v_3D_1=3+v_3(\det T_0)\ge3.
\tag{7.5}
$$



The matrix $M_0\bmod3$ is the next actual digit on lifts of


$$
(y+1)(y-1)^by^a,\qquad 0\le a<b/2.
$$


Determining it requires the complete actual reduction one digit further, namely the information corresponding to $S_{\rm act}\bmod3^{30}$, with producer returns, prefix and first-radical corrections, and the exact endpoint lift retained.

The $3^{-2}$ correction in (7.1) starts at $3^4$, so it does not alter $T/27\bmod3$; nevertheless its inverse must remain paid in the exact cofactor identities.

### 7.4 Why the present data cannot imply this lemma

The limitation is genuine. Fix $\lambda=1/3$ and residual endpoint $e_0$. For


$$
T_L=
\begin{pmatrix}
0&27\\
27&-3^5+3^{6+L}
\end{pmatrix},
\qquad L\ge0,
$$


all entries lie in $27\mathbb Z_3$, and


$$
\frac{e_0^T\operatorname{adj}(T_L)e_0-\lambda\det T_L}
{\det T_L}
=-3^L.
$$


The relative valuation is any prescribed $L\ge0$. Replacing the lower-right entry by $-3^5$ makes the whole bordered numerator zero.

Conversely,


$$
T=\operatorname{diag}(3^k,27),\qquad k\ge3,
$$


gives relative valuation $-k$. Extra $27I$ blocks extend these examples to every larger residual dimension.

These are **not counterexamples about the actual producer**. They prove that the presently validated low-digit and diagonal data alone cannot determine the final relative cofactor.

---

# Part II. Binary review

## 8. Complete finite inverse modulo $8$

Use divided powers, $D=\partial_z$, $U_\gamma=(1+D)^\gamma$, and retain contact restriction $\pi$ and zero-padding $\iota$.

The exact factorization is


$$
A=P_bM_b,\qquad M_b=\pi U_nH_{\phi^n}U_n\iota.
$$



Since


$$
\phi^2=1+2\eta,\qquad
\eta=-z^{[1]}+2z^{[2]}-3z^{[3]}+3z^{[4]},
$$


and every positive-degree integral divided-power polynomial has even square,


$$
H_{\phi^n}\equiv1+2H_\eta\pmod8.
$$


For the full conjugation $C=U_nH_\eta U_{-n}$,


$$
C\equiv H_\eta+2H_{\eta'}U_{-1}
+H_{\eta''}U_{-2}\pmod4.
\tag{8.1}
$$


The coefficients of the omitted third and fourth derivative terms are divisible by $4$, using $n\equiv2\pmod{64}$.

Because $U_{2n}$ preserves the contact space,


$$
M_b\equiv(1+2C_b)U_{2n}^{(b)}\pmod8,
\qquad C_b=\pi C\iota.
$$


Hence


$$
z^f\equiv U_{-2n}^{(b)}
(q-2C_bq+4C_b^2q)\pmod8.
\tag{8.2}
$$


Conjugation precedes restriction, so leave-and-return paths are included.

### 8.1 Boundary-complete evaluation

The transformed force is


$$
q_i=(-1)^i\left(
2-i+3\binom i2-\binom i3+
4\binom i4-4\binom i5
\right)\pmod8.
$$


The finite $U_{-1}$ and $U_{-2}$ sums have the endpoint constants stated in A5turn6. They follow from finite hockey-stick sums at $B=b-1=4d$, not from infinite tails.

In exponential-generating notation, their polynomial coefficient lists modulo $4$ are


$$
[2,1,3,1],\quad [2,2,1,3,1],\quad [2,2,2,1,3,1].
$$


Using


$$
[PQ]_j=\sum_r\binom jr P_rQ_{j-r}
$$


for divided-power coefficients in (8.1) yields


$$
C_bq=e^{-z}[0,0,2,3,2,0,2,2]\pmod4.
$$



The quadratic term in (8.2) is also paid. Modulo $2$, the only possible exterior positions of $C\iota q$ are $b,\ldots,b+3$. Their coefficients vanish: the terminal input is $q_{4d}=0$, and the other potential fourth-degree coefficients contain $d\equiv0\pmod2$. Thus


$$
(1-\iota\pi)C\iota q=0\pmod2.
$$


Since $C^2\equiv0\pmod2$,


$$
C_b^2q=0\pmod2.
$$



Therefore


$$
z^f=U_{-2n}^{(b)}w\pmod8,
$$


where


$$
w_{4s}=2+2s,\qquad
w_{4s+2}=7-2s,\qquad
w_{2s+1}=-1\pmod8.
\tag{8.3}
$$



### 8.2 All four contact classes

Define


$$
B_r=\binom{h+r}{r},\qquad
C_r=\binom{h+r}{r-1},\qquad
D_r=\binom{h+r}{r-2}.
$$


Then the reviewed formulas are


$$
\begin{array}{c|c|c}
j&r&z_j^f\bmod8\\ \hline
4s&d-s&(-1)^r(2B_r-4C_r)\\
4s+1&d-s-1&(-1)^r(B_r-4C_r+4D_r)\\
4s+2&d-s-1&(-1)^r(B_r+4D_r)\\
4s+3&d-s-1&-(-1)^r(B_r-4C_r+4D_r).
\end{array}
\tag{8.4}
$$



The reverse generating series is used only through the finite degree $B$. Its extension beyond $B$ cannot affect any required coefficient. The multiplier expansion


$$
(1+X)^{-4h}\equiv
(1+X^4)^{-h}
-(4X+6X^2+4X^3)(1+X^4)^{-h-1}
+4X^4(1+X^4)^{-h-2}\pmod8
$$


is valid because $h\equiv1\pmod8$. Extracting its four classes gives (8.4).

### 8.3 All reconstructed differences and the physical terminal

For $j=4s$, $r=d-s$,


$$
\Delta_{4s}z^f
\equiv(-1)^r\bigl(-(4s+2)B_r+4C_r\bigr)\pmod8.
\tag{8.5}
$$


For the other three classes let $r=d-s-1$ and


$$
J_r=\binom{h+r}{r+1}.
$$


Then


$$
\begin{aligned}
\Delta_{4s+1}z^f
&\equiv(-1)^r(B_r-2J_r-4D_r),\\
\Delta_{4s+2}z^f
&\equiv(-1)^r((4s+1)B_r+4D_r),\\
\Delta_{4s+3}z^f
&\equiv4(-1)^r((s+1)B_r-C_r)
\end{aligned}
\pmod8.
\tag{8.6}
$$


These follow directly from (8.4) and Pascal’s identity.

At the physical terminal,


$$
z^f_{b-1}\equiv2\pmod8,\qquad
\boxed{\Delta_bz^f=bz^f_{b-1}\equiv2b\pmod8.}
\tag{8.7}
$$


The physical value remains $z_b^f=0$.

**Decision:** The complete inverse, all four row classes, and all physical differences are accepted.

---

## 9. Sharp classification of actual content one

A row witnesses $a=1$ exactly when


$$
v_2(W_j)+v_2(\Delta_jz^f)=2.
\tag{9.1}
$$



The exact weight valuations are


$$
v_2(W_{4s})=v_2\binom gs,
$$




$$
v_2(W_{4s+2})=1+v_2\binom{g-1}{s},
$$




$$
v_2(W_{4s+1})=v_2(W_{4s+3})
=2+v_2\binom{g-1}{s}.
\tag{9.2}
$$



For $4s$ rows:

- If $W_{4s}$ is odd, $s\subseteq g$, so $s\bmod64$ is $0,1,16,$ or $17$.
- For even $s$, $r=d-s\equiv52$ or $36\pmod{64}$. Then $B_r,C_r$ are even, and (8.5) reduces to $-2(-1)^rB_r\pmod8$. A content-one row occurs precisely when $v_2(B_r)=1$.
- For odd $s$, $r\equiv51$ or $35\pmod{64}$. Addition of $h$ and $r$ has carries at bits $0,1,5$, so $8\mid B_r$; also $C_r$ is even. No content-one row occurs.
- If $v_2(W_{4s})=1$, equation (8.5) shows that a witness occurs precisely when $B_r$ is odd. Since $h$ is odd, this forces $r$, and hence $s$, to be even.
- Weight valuation at least $2$ cannot yield (9.1), because the difference is already even.

All other row classes are excluded:

- A $4s+2$ row of weight valuation $1$ has $s\subseteq g-1$, forcing $B_r$ divisible by $4$.
- At weight valuation $2$, an odd $s$ would produce at least four borrows from $g-1$, whose valuation is $4$; hence $s$ is even and the difference is even.
- For $4s+1$, weight valuation $2$ forces $s\subseteq g-1$, again making the difference even.
- Every $4s+3$ difference is divisible by $4$.
- At $j=b$,
  

$$
v_2(W_b)=2+v_2\binom{g-1}{d}\ge3,
$$


  so the physical terminal is not a witness.

Together with the accepted $a\ge1$, this proves


$$
\boxed{
a=1\iff
\exists\,0\le s\le d,\ s\ {\rm even}:
v_2\binom gs+
v_2\binom{h+d-s}{d-s}=1.
}
\tag{9.3}
$$



### Finite certificate consequence

The two-cost DP charges both Kummer channels and starts and finishes with all carries zero. Its mathematical optimization is exactly the minimum in (9.3).

Accordingly, the supplied 21 minima, all at least $8$, prove


$$
a(u)\ge2\qquad(0\le u\le20).
$$


At $u=0$, combining this with the older independent upper bound gives


$$
\boxed{2\le a(0)\le10.}
$$



The minimum $8$ does **not** prove $a(0)=8$, $a(0)\ge8$, or even $a(0)\le8$: the modulus-$8$ theorem classifies content one, not arbitrary higher content.

The free-exit prefix certificates still have cost-one paths. They cannot prove universal $a\ge2$. No universal assertion is extracted from the 21 complete original words.

---

## 10. Complete exponential returns and actual primitive payment

The normalized exterior factorial source has the complete modulus-$8$ prefix


$$
s_{\rm ext}=e_b+2e_{b+1}+6e_{b+2}.
$$


Indeed the next factorial quotient contains three factors with total valuation at least $3$, and later quotients retain that divisibility.

Its transformed exterior part is


$$
v_{\rm ext}=5e_b+2e_{b+1}+6e_{b+2}\pmod8.
$$


The actual finite inverse gives


$$
z^k=
-\pi U_{-2n}v_{\rm ext}
+2U_{-2n}^{(b)}\pi Cv_{\rm ext}
-4U_{-2n}^{(b)}C_b\pi Cv_{\rm ext}
\pmod8.
\tag{10.1}
$$



The last return is evaluated, not dropped. Modulo $2$,


$$
(1-\iota\pi)Ce_b=e_{b+2}+e_{b+4}.
$$


The contact images of these two exterior odd coordinates agree, and $C^2=0$; hence


$$
C_b\pi Ce_b=0\pmod2.
$$



The linear return is


$$
\pi Cv_{\rm ext}
=e^{-z}(-2\eta'-z\eta'')
=e^{-z}[2,2,0,1]\pmod4.
\tag{10.2}
$$


Consequently,


$$
z^k_{4s}\equiv4\binom{h+d-s}{d-s}\pmod8.
\tag{10.3}
$$


For $r=d-s-1$, with


$$
c_r=[Y^{r+1}](1+Y)^{-h},
$$


the needed other classes are


$$
z^k_{4s+1}\equiv-c_r,\qquad
z^k_{4s+2}\equiv-2c_r\pmod4.
$$


Thus


$$
\Delta_{4s}z^k\equiv0,\qquad
\Delta_{4s+2}z^k\equiv0\pmod4.
$$



Define the complete physical source


$$
\tau_j=W_j\Delta_jz^k\quad(j<b),\qquad
\tau_b=W_b(bz^k_{b-1}+1).
$$



The row-by-row payment is valid:

- odd $W_j$ occurs only in $4s$ rows; the original mask obstruction makes the binomial in (10.3) even, giving an eight-divisible difference;
- weight valuation $1$ occurs only at even rows, where the difference is four-divisible;
- at weight valuation $2$, source parity makes the difference even, including the remaining $4s+1$ case by the stated low-bit carry in $c_r$;
- the terminal is paid by $v_2(W_b)\ge3$, with its complete $+1$ retained.

Therefore


$$
\boxed{\tau\in8\mathbb Z_2^{b+1}.}
\tag{10.4}
$$



Since


$$
\mathcal Rz^f=2^{a+1}x_0,\qquad
\mathcal V=(\mathcal Rz^f)^T\tau,
$$


the actual division gives


$$
E=2^{-a-3}\mathcal V=x_0^T(\tau/4)\in2\mathbb Z_2.
\tag{10.5}
$$



This conclusion is independent of the unknown exact $a$. It concerns the complete exponential source. Promotion to the full mixed column still requires the original logarithmic guard **after every normalization**.

---

## 11. Evaluated adjoint acceptance and norm parity

The physical boundary $z_b=0$ gives the exact telescope


$$
\sum_{j=0}^{b}(\mathcal Rz)_j
=\sum_{j=0}^{b-1}(n+1-j)W_jz_j.
$$


For


$$
S=\sum_{j=0}^{b-1}(n+1-j)W_jz^f_j,
$$


this yields


$$
\sum_jx_j=S/2.
\tag{11.1}
$$



The adjoint coefficient generating function, through the finite degree $B=b-1$, is


$$
(n+1-t)(1+t)^{1-n}.
$$


Using the evaluated polynomial representation of $w$, finite hockey-stick summation gives


$$
S\equiv
4\left[
\binom M{B-1}+\binom M{B-2}+\binom M{B-3}
\right]
-2\binom{M-1}{B}\pmod8,
$$


where $M=n+B-1$.

The first three displayed binomials are even by the specified low-bit tests. The last term reduces to


$$
\binom{M-1}{B}
=\binom{4(g+d-1)}{4d}
\equiv\binom{g+d-1}{d}\pmod4.
$$


Addition of $g-1$ and $d$ has carries at bits $4$ and $5$, so this binomial is divisible by $4$. Hence


$$
\boxed{S\in8\mathbb Z_2.}
\tag{11.2}
$$



Since $a\ge1$, $x/2$ is integral, and


$$
\sum_j(x_j/2)^2\equiv\sum_jx_j/2\pmod2.
$$


Equations (11.1)–(11.2) therefore imply


$$
\boxed{\sum_jx_j\in4\mathbb Z_2,\qquad x^Tx\in8\mathbb Z_2.}
\tag{11.3}
$$



For the actual primitive column,


$$
Q\equiv2^{-a-1}S\pmod2.
$$


When $a=1$, the known modulus pays this quotient and proves $Q$ even. When $a\ge2$, knowing only $S\bmod8$ does not determine $S/2^{a+1}\bmod2$.

**Decision:** The linear acceptance and norm consequence are accepted, with exactly this precision limitation.

---

# Part III. Arithmetic preservation and remaining proof obligations

## 12. Complete forcing, returns, and guards remain unchanged

The ternary actual columns are still


$$
F_{\rm act}=Z-WE_{\rm act}^{-1}C_{\rm act}.
$$


The producer remains


$$
3P_n-Q_c=3^7\mathscr R
=\sum_{a=0}^{A+1}
-\frac{(A+1)!}{a!}(t_a+\xi v_a)x^a,
$$


with complete force


$$
t=3nh_{\rm vec}
+(b_{\rm force}+6)e_{n-1}
+\frac{2b_{\rm force}}{n-1}e_{n-2},
\qquad b_{\rm force}=-n-66.
$$


The signed $\xi$ and its earlier paid common division are unchanged. So is


$$
J^T\varepsilon+\omega
=-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
$$



For the binary stream, the full higher-precision source is still


$$
k=\sum_{t=0}^{2n-1}\frac{(b+t)!}{b!}\mathbf a_{b+t}.
$$


At raw precision $2^L$, the retained completion uses


$$
I=\min(b-1,8L-2),\quad m_{\rm aux}=4(L-1),
$$




$$
T=\min(2L-1,2n-1),\quad V=T+m_{\rm aux},
$$


subject to


$$
n>4(I+2m_{\rm aux}+T+4)+2.
$$


Both completed return channels and both physical mixed terminal terms remain present. The completed auxiliary value $\widehat z_b^k=-1$ is not a replacement for the physical value $z_b^k=0$.

The logarithmic source retains


$$
\mathcal L_s=s![z^s]\frac{F(z)}{1-z},
\qquad
B_\star=n-v_2(b!)-1-2s_2(n)-\ell.
$$


It can be suppressed only when this guard protects the desired **paid** observation. For a depth-$K$ relative congruence, the actual $a$ and sufficient raw precision—such as


$$
L\ge2a+K+3
$$


in the supplied evaluator—remain necessary.

---

## 13. Actual contents, least clearers, all-prime gcds, and whole errors

### 13.1 Ternary construction

No actual column content or least simultaneous clearer has been reevaluated. Retain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$




$$
g_\ell=\gcd(|A_\ell|,|B_\ell|)
$$


over **all primes**.

For $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


The whole evaluated error remains


$$
\boxed{
q(e+\pi)-p=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
{g_\ell}\det H_{\rm complete}.
}
\tag{13.1}
$$



At its retained scope,


$$
v_3(q)=
\max\!\left(
0,\,
h-26+v_3Q_{\rm loc}(-1)+v_3D_1-v_3D_0
\right).
$$


The new cofactor normal form concerns the relative term, not the common determinant multiplicity.

An irrationality proof still requires, at the same infinite original indices,


$$
B_\ell\ne0,\qquad \det H_{\rm complete}\ne0,
$$


and


$$
\log g_\ell-(m+1)\log\ell_{\rm clr}
-\log|\det H_{\rm complete}|\longrightarrow+\infty.
\tag{13.2}
$$



### 13.2 Binary construction

Retain


$$
\omega_j=j!W_j,\qquad
u_j=\frac{2\Lambda R\,x_j}{\omega_j},\qquad
v_j=\frac{4b!\,y_j}{\omega_j},
$$


and the actual least simultaneous clearer


$$
d_B=\operatorname{lcm}_{0\le j\le b}
\{\operatorname{den}(u_j),\operatorname{den}(v_j)\}.
$$



With $\mathcal N=x^Tx$ and $\mathcal H=x^Ty$,


$$
A_B=d_B^2\,4\Lambda^2R^2\mathcal N,\qquad
H_B=d_B^2\,8\Lambda Rb!\mathcal H,
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
$$


This is again the final gcd over all primes.

The retained primewise identity is


$$
v_p(q_n)=
\max\!\left\{
v_p\!\left(\frac{\Lambda R}{2b!}\right)
+v_p(\mathcal N)-v_p(\mathcal H),0
\right\},
$$


including the previously established original-family law


$$
v_3(q_n)=n-\frac{b+15}{2}.
$$



The whole error is


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n.
}
\tag{13.3}
$$


No fixed binary source digit or norm digit proves


$$
0<|q_n(e+\pi)-p_n|\longrightarrow0
$$


at infinitely many original indices.

The two distinct original families have not been combined.

---

## 14. Finite evidence and a bounded new arithmetic check

The supplied ternary receipt checks one auxiliary pair


$$
(P,r)=(2187,227),
$$


including 11,665 divided coefficients and 29,524 series/recurrence positions. Its rank and scalar outputs agree with the symbolic proofs above. Its scope does not include actual producer jets or original-index density.

The binary two-cost receipt checks 504 auxiliary cases and 21 complete original words. By the accepted theorem, it settles the content-one question at those 21 words only. No rerun is needed.

No computation has been executed in this review. A small optional check of the **new cofactor limitation**, requiring only exact rational arithmetic, is as follows.

### Inputs

Use endpoint $e_0=(1,0)^T$, diagonal $\lambda=1/3$, and


$$
T_1=\begin{pmatrix}0&27\\27&486\end{pmatrix},\quad
T_2=\begin{pmatrix}0&27\\27&1944\end{pmatrix},
$$




$$
T_3=\begin{pmatrix}0&27\\27&-243\end{pmatrix},\quad
T_4=\begin{pmatrix}81&0\\0&27\end{pmatrix}.
$$



For each, calculate


$$
D_0=\det T,\qquad
D_1=e_0^T\operatorname{adj}(T)e_0-\lambda\det T,
\qquad D_1/D_0.
$$



### Expected verifiable outputs



$$
\begin{array}{c|r|r|c}
T&D_0&D_1&D_1/D_0\\ \hline
T_1&-729&729&-1\\
T_2&-729&2187&-3\\
T_3&-729&0&0\\
T_4&2187&-702&-26/81
\end{array}
$$



These checks certify only the stated residual countermodels and the signs in the new normal form. They do not assert that any countermodel is realized by an original producer.

---

## 15. Final proof-status ledger

| Statement | Status after independent review |
|---|---|
| Complete ternary beta-pole formula modulo $3^{29}$ | Validated |
| Normalized unit $4\bmod27$ | Validated |
| Precision-$20$ substitution at the new precision | Paid explicitly by orthogonality and the integral unimodular basis |
| Total orders $2,3,4$, and higher | Validated with degree, grid, cutoff, and factorial payments |
| Finite prefix cross convolution | Evaluated and validated |
| First-radical $3^{-1}$ inverse | Explicitly paid |
| Actual endpoint and complete $v_3(\lambda^{(2)})=-1$ | Validated using the supplied old diagonal premise |
| Rational-Hankel rank and exact radical | Validated |
| Endpoint-annihilating rank and nullity | Validated |
| Endpoint-adapted $3^{-2}$ elimination and residual cofactor normal form | **New proved result** |
| Actual exclusion of the cancellation equality $d_M=d_0+2$ | Open |
| Complete binary inverse modulo $8$, all rows and terminal | Validated |
| Sharp actual $a=1$ criterion | Validated |
| Complete $\tau\in8$, and $E$ even after actual content division | Validated |
| Evaluated $S\in8$, $x^Tx\in8$, and $a=1\Rightarrow Q$ even | Validated |
| $a(u)\ge2$ for the 21 certified original words | Finite certificate consequence |
| Universal $a\ge2$, exact higher contents, higher relative source law | Open |
| Same-index all-prime primitive denominator versus nonzero whole error | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

## Conclusion

The new source claims are mathematically stronger than their predecessors and, after the explicit payments above, are valid at their stated original scope.

The additional result proved here is the exact residual identity


$$
D_1=\chi\,3^{3r-3}
\left(\det M_0-9\upsilon\det T_0\right),
$$


together with its cancellation threshold


$$
v_3(\det M_0)=v_3(\det T_0)+2.
$$


It separates genuine relative-cofactor control from common determinant depth and explains precisely why the intermediate valuation $v_3(\lambda^{(2)})=-1$ is not, by itself, a final noncancellation theorem.

The next local ternary bottleneck is an actual, producer-aware evaluation on


$$
(y+1)(y-1)^b\mathbb F_3[y]_{<b/2},
$$


sufficient to control the residual endpoint minor and exclude or resolve that cancellation equality. The binary bottleneck is a higher-precision, actual-content-paid relative observation for the full mixed column, with the logarithmic guard intact.

Beyond both local tasks lies the unchanged global obligation: **the actual all-prime primitive denominator and the nonzero whole evaluated error must be controlled at the same infinite original indices.**



$$
\boxed{\text{No unconditional proof or disproof of irrationality of }e+\pi
\text{ follows from the attached work or from this review.}}
$$


