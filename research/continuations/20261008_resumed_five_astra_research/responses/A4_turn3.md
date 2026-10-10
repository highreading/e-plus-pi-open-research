> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the ternary projection, with a terminal bootstrap and a paid returned inverse direction

## 1. Executive conclusions

The rationality or irrationality of $e+\pi$ remains unresolved.

At their stated precision and on the stated original family, the principal new local results of A1 Turn 0 and A1 Turn 1 pass this audit:

1. The factorial part may be removed **locally and $3$-adically** through the actual LOW/HIGH projection, with the one-digit inverse loss paid.
2. The first prefix lift suffices for the order-$27$ radical coefficient; its omitted part is exactly a stationary $81Z^{T}\mathsf A Z$ return.
3. The sparse Jacobi filter has the asserted residual against the actual mixed space $W$, including every HIGH row up to $Y_m$, for **$16\le p\le25$**.
4. The last middle column is exceptional. Its trial residual is not small:
   

$$
\mathcal P(W,\widetilde F_{\nu-1}^{(p)})
   \equiv 3\mathfrak t_p e_{Y_m}\pmod{3^p},
   \qquad
   \mathfrak t_p\in\mathbb Z_3^\times.
$$


   In fact, the leading unit can be evaluated:
   

$$
\boxed{\mathfrak t_p\equiv1\pmod3.}
$$


5. The logarithmic compression is valid through $3^{30}$, and its scalar is
   

$$
\boxed{K_{3^{15}}\equiv13\pmod{81}.}
$$


6. The corrected, not merely raw, projection coefficient is
   

$$
\boxed{\Pi=0.}
$$


7. The alternative proof of the nonterminal strip is valid. It can be checked from the complete pole moments and the actual finite prefix, without accepting the historically pending support-layer argument.
8. Consequently, after the retained producer comparison and paid rank-$b$ matrix return,
   

$$
\boxed{T\in81M.}
$$



There is also a further result available from these ingredients. It does **not** pretend that the exceptional terminal residual vanishes.

> **New terminal bootstrap.** On the same original family,
> 

$$
> \boxed{
> [y^m]F_i\in3^{25}\mathbb Z_3\quad(0\le i\le\nu-2),\qquad
> [y^m]F_{\nu-1}\in3^{24}\mathbb Z_3.
> }
>
$$


> Moreover, for the actual LOW/HIGH inverse,
> 

$$
> \boxed{(E_c^{-1})_{Y_m,Y_m}\in3^{23}\mathbb Z_3.}
>
$$



Thus the originally normalized physical-terminal vector satisfies


$$
\boxed{\bar t=0,\qquad t_i=3^{-20}[y^m]F_i.}
$$


The last amplitude at the finer scale $3^{24}$, and the middle-terminal coupling $\gamma_c$, are not thereby evaluated.

Finally, a two-coordinate pivot in the **fully returned** bordered Schur matrix is uniformly invertible with an explicitly paid one-digit loss. It yields a rank-one returned matrix correction in $3^7M$. This is a genuine, evaluated partial inverse consequence, but it is not a proof of the outstanding $C^{-1}z$ estimate and gives no growing relative-cofactor saving.

---

## 2. Original domain, finite spaces, and accepted inputs

All assertions below retain


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




$$
m=2^{2j-1},\qquad n=4^j+1=2m+1,\qquad A=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A.
$$



The global window remains


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15},
$$


and the fixed subwindow remains


$$
\frac{103}{1000}<\rho:=\frac{N_0}{P_0}<\frac{104}{1000},
$$


where


$$
P_0=243P=3^{h-27},\quad N_0=243r,\quad D=P_0+N_0,
$$




$$
P=3^{h-32},\quad r\equiv2\pmod9,\quad r\text{ odd},
$$


and


$$
\boxed{4^j=243(3^{26}-1)P-243r+1.}
$$



No independent choice of $P,r$ is substituted for an original index. The supplied density theorem is reused only for infinitude within this unchanged original subwindow.

Put


$$
x=y-1,\qquad Q=P_0/9=3^{h-29},\qquad b=Q-N_0.
$$


Then


$$
D=10Q-b,\qquad .064<\frac bQ<.073,
$$


and $D,b$ are even, while $Q,N_0$ are odd. In particular,


$$
m=\frac{H-D+1}{2}.
$$



The finite coordinates are exactly


$$
U_s=x^s\quad(0\le s<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),
$$




$$
Y_t=y^t\quad(d\le t\le m),
\qquad
\nu=D/2-1,\quad d=D+\nu.
$$


Thus


$$
W=[U\ Y].
$$



The LOW span is also the span of the monomials $1,y,\ldots,y^{D-1}$; the HIGH span is exactly the span of $y^d,\ldots,y^m$. The omitted monomial degrees are $D,\ldots,d-1$. No consecutive orthogonal-polynomial degree space replaces $W$.

The residual indices are


$$
R_*=\frac{9Q+1}{2},\quad
\tau=\frac{Q-b-3}{2},\quad
\ell=\frac{3b}{2}+1,
$$




$$
K=\{0,\ldots,\ell-1\},\quad
J=\{\ell,\ldots,\tau-1\},
$$




$$
n_J=\frac{Q-4b-5}{2},\qquad E=\frac{Q-3}{2}.
$$


Since $R_*+\tau=\nu$, $\delta_J=e_{n_J-1}$ denotes the **last middle direction**, $z_{\nu-1}$. It is not the physical HIGH coordinate $Y_m$.

All fixed-margin inequalities used below hold for sufficiently large original indices. For example,


$$
2b+\frac52<\frac Q6,\qquad
\frac b2+1<\frac Q{27},\qquad n_J\ge2.
$$


These follow from $b/Q<.073$; no new subwindow is required.

### 2.1 Complete functional and original corrections

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


The core is


$$
G_c(f,g)=\mathcal M(Q_cfg),
\qquad
Q_c=(y+1)x^A(\beta+3y),\quad \beta=-71-A.
$$


Write


$$
E_c=G_c(W,W),\qquad
F_i=z_i-WE_c^{-1}G_c(W,z_i),\qquad S_c=G_c(F,F).
$$



For $\deg f,\deg g\le m$,


$$
\deg(Q_cfg)\le A+2+2m=2n-1.
$$


The pole polynomial has degree at most $2n-2$, and its largest denominator is


$$
4n-3=4H-4D+5<3^{h+1}.
$$


Hence the retained $3^h$ pays every ternary pole denominator.

The following established original-object results are reused, not recalculated:

- integral unimodularity of $[W,F]$;
- $E_c^{-1},E_{\rm act}^{-1}\in3^{-1}M$;
- $S_c\in3^{26}M$;
- the finite prefix identities and H2 at their supplied scope;
- the closed adjoining-column producer comparison;
- the paid rank-$b$ elimination and complete returned diagonal valuation;
- the complete raw radical comparison through $3^{30}$.

The old full-strip support proof is **not** included in this accepted-input list.

---

## 3. Audit of A1 Turn 0

### 3.1 Pole replacement through the actual inverse

Define


$$
\mathcal P(f,g)=
3^h\sum_{v=0}^{2n-2}
\frac{[y^v]x^A(\beta+3y)fg}{2v+1}.
$$


Then


$$
\mathcal P=G_c+3^h\mathcal T,\qquad
\mathcal T(f,g)=\tfrac14\mathfrak f(Q_cfg),
$$


and $\mathcal T$ is integral on integral degree-$\le m$ polynomials.

In the actual basis $[W,F]$, the pole matrix is


$$
\begin{pmatrix}
E_c+3^hT_{WW}&3^hT_{WF}\\
3^hT_{FW}&S_c+3^hT_{FF}
\end{pmatrix}.
$$


Since $E_c^{-1}\in3^{-1}M$, for $h\ge2$


$$
(E_c+3^hT_{WW})^{-1}\in3^{-1}M.
$$


The exact pole-corrected columns therefore satisfy


$$
F_{\mathcal P}-F\in3^{h-1}WM,
$$


and their Schur complement satisfies


$$
\begin{aligned}
S_{\mathcal P}-S_c
={}&3^hT_{FF}\\
&-3^{2h}T_{FW}
(E_c+3^hT_{WW})^{-1}T_{WF}
\in3^hM.
\end{aligned}
$$


The inverse loss has been included: the quadratic term has valuation at least $2h-1$.

Thus the Turn 0 pole-replacement theorem is correct. It is a local congruence, not a replacement of the complete real determinant.

The beta entries used there are also correct:


$$
I_N(s)=\frac12\int_0^1y^{s-1/2}(1-y)^N\,dy
=\frac{2^NN!}{\prod_{k=0}^{N}(2s+2k+1)},
$$


and


$$
\mathcal P(x^uy^r,x^vy^t)
=3^h(-1)^N\bigl(\beta I_N(s)+3I_N(s+1)\bigr),
$$


where $N=A+u+v$ and $s=r+t$. Here


$$
N+s+1\le2n-2,
$$


so the product formula introduces no pole beyond the original cutoff. Stripping the powers of $3$ before modular inversion is essential and valid.

### 3.2 Stationary residual certificates

If


$$
E_{\mathcal P}q-\mathcal P(W,\Psi)\in3^{16}M,
$$


the inverse loss gives


$$
q-q_{\rm ex}\in3^{15}M.
$$


Exact pole orthogonality then leaves only a quadratic error:


$$
\mathcal P(\Psi-Wq,\Psi'-Wq')
-\mathcal P(F_{\mathcal P,\Psi},F_{\mathcal P,\Psi'})
\in3^{30}\mathbb Z_3.
$$


This is a valid stationary certificate.

A physical coefficient divided by $3^{20}$ requires the separate $22\to21$ residual payment. A $16\to15$ pairing certificate does not determine that coefficient.

The very large dense certificate proposed in Turn 0 is mathematically finite, but it is not an admissible computational proposal for the present assignment. Nothing below requests it.

### 3.3 The one-lift prefix identity

Let


$$
a_0=\frac{9Q-1}{2},\quad J_0=3Q-1,\quad
k_0=a_0-J_0=\frac{3Q+1}{2}.
$$


For $g_a=x^by^a$, $0\le a\le b/2$, the accepted selector gives


$$
X:=-\mathsf A^{-1}\mathsf B_G=3P_G+9Z,\qquad Z\in M.
$$


The trial lifted polynomials are


$$
\Psi_a=x^{D+b}y^{k_0+a}(y^{3Q}+3).
$$


They remain nonterminal:


$$
\deg(\Psi_a/x^D)
\le R_*+\frac{3b}{2}
=\nu-(n_J+1).
$$


Their prefix positions also remain inside the finite prefix.

If $\mathcal F_a$ denotes the actual LOW/HIGH correction of $\Psi_a$, exact prefix orthogonality gives


$$
-\frac{G_c(\mathcal F,\mathcal F)}{3^{26}}
=
G^T\mathcal R_{c,KK}G+81Z^T\mathsf A Z.
$$


Consequently


$$
\boxed{
\Pi=
\frac{G^T\mathcal R_{c,KK}G}{27}\pmod3
=
-\frac{G_c(\mathcal F,\mathcal F)}{3^{29}}\pmod3.
}
$$


The complete division is paid by H2 and this identity.

There is no unsupported step here. At the next digit, however, $Z^T\mathsf A Z$ is no longer invisible.

---

## 4. Audit of the sparse Jacobi filter

### 4.1 Coefficients and orthogonality

For


$$
N=3^{p-1},\qquad M=\frac{N-1}{2},
$$


put


$$
R_N(Y)={}_2F_1\!\left(-M,\frac{3N}{2};\frac12;Y\right).
$$


Its coefficients satisfy


$$
r_k=(-1)^k\binom Mk
\frac{\prod_{a=0}^{k-1}(3N+2a)}
{\prod_{a=0}^{k-1}(2a+1)}.
$$



For $1\le k\le M$,


$$
v_3\binom Mk=v_3\binom{2k}{k},
$$


because $2a+1<N$ and


$$
v_3(N-(2a+1))=v_3(2a+1).
$$


Also


$$
v_3\prod_{a=0}^{k-1}(3N+2a)
=p+v_3((k-1)!).
$$


Combining the numerator and denominator valuations gives


$$
\boxed{v_3(r_k)=p-v_3(k)\ge2.}
$$


Thus $R_N\in\mathbb Z_3[Y]$ and $R_N\equiv1\pmod9$.

The stated Rodrigues formula is correct. Its boundary terms vanish in $M$ integrations by parts, giving


$$
\int_0^1Y^{q-1/2}(1-Y)^NR_N(Y)\,dY=0
\qquad(0\le q<M).
$$



These are classical Jacobi identities; the relevant new issue is their embedding in the original finite $W$.

### 4.2 Degree and same-$W$ checks

Set


$$
L=3^{h-p},\qquad Y=y^L.
$$


For $16\le p\le25$,


$$
\frac LD=\frac{3^{27-p}}{1+\rho}
\ge\frac9{1.104}>8.
$$


In particular, $L>4D$.

For $0\le i\le\nu-2$,


$$
\widetilde F_i^{(p)}=x^Dy^iR_N(y^L)
$$


has


$$
\widetilde F_i^{(p)}-z_i\in\operatorname{span}Y,
$$


because every nonconstant filter term starts at exponent at least $L>d$. Moreover,


$$
m-\deg\widetilde F_i^{(p)}
\ge\frac{L-4D+7}{2}>0.
$$


Thus no term crosses $Y_m$.

For the last middle index, the analogous degree gap is still positive:


$$
m-\deg\widetilde F_{\nu-1}^{(p)}
\ge\frac{L-4D+5}{2}>0.
$$


Its problem is a residual at $Y_m$, not excessive polynomial degree.

No argument here extends $p$ beyond $25$.

### 4.3 Residual against every LOW and HIGH row

The coefficientwise congruence


$$
x^H\equiv(Y-1)^N\pmod{3^p}
$$


is valid: write $x^L=(Y-1)+3B(y)$ and expand its $N$-th power. For every nonleading term,


$$
v_3\binom Nk+k\ge p.
$$



The pole functional is integral on the physical cutoff, so this congruence loses no digit when evaluated.

A pole surviving modulo $3^p$ must satisfy


$$
v_3(2v+1)\ge h-p+1,
$$


and therefore


$$
v\equiv\frac{L-1}{2}\pmod L.
$$



For a LOW row $x^u$, the remaining low band has degree


$$
u+i+1\le d-2<\frac{L-1}{2}.
$$


It misses every possible surviving residue.

For a HIGH row $y^t$, a contributing monomial must have


$$
t+i+\epsilon=qL+\frac{L-1}{2},\qquad \epsilon\in\{0,1\}.
$$


For $i\le\nu-2$,


$$
t+i+\epsilon\le m+\nu-1=\frac{H-3}{2},
$$


so $0\le q\le M-1$. The full macro-moment is then zero by Jacobi orthogonality.

The largest macro-pole index used is at most


$$
2H-\frac{3L+1}{2}<2H-2D+2=2n-2.
$$


Thus the moment has not been completed beyond the physical cutoff.

It follows that


$$
\boxed{\mathcal P(W,\widetilde F_i^{(p)})\in3^pM
\quad(i\le\nu-2).}
$$


The actual inverse loses one digit:


$$
F_i-\widetilde F_i^{(p)}\in3^{p-1}WM.
$$


At $p=16$, stationary pairing error is in $3^{30}M$; at $p=25$, the direct nonterminal physical-coefficient bound is $3^{24}$.

### 4.4 The exceptional terminal residual survives

For $i=\nu-1$, the $3y$-term at $t=m$ has


$$
m+i+1=\frac{H-1}{2},
$$


which corresponds to $q=M$, outside the orthogonality range.

The residual is


$$
\boxed{
\mathcal P(W,\widetilde F_{\nu-1}^{(p)})
\equiv3\mathfrak t_p e_{Y_m}\pmod{3^p},
}
$$


where


$$
\mathfrak t_p
=(-1)^{N+M}3^p2^{4N-1}
\frac{M!(N+M)!(2N)!}{(4N)!}.
$$


This formula follows directly from the $M$-th Jacobi moment by Rodrigues and integration by parts.

Writing $q=p-1$, Legendre’s formula gives


$$
v_3(M!)+v_3((N+M)!)=N-q-1,
$$




$$
v_3((2N)!)=N-1,\qquad v_3((4N)!)=2N-1.
$$


Therefore $v_3(\mathfrak t_p)=0$.

The leading unit can also be determined. If


$$
U(a)=a!/3^{v_3(a!)}\pmod3,
$$


then


$$
U(a)=(-1)^{v_3(a!)}\prod a_\ell!\pmod3,
$$


where $a_\ell$ are the ternary digits. The numbers $M,N+M$ have only digits $1$, $2N$ has one digit $2$, and $4N$ has digits $11$ followed by zeros. After including the sign and power of $2$, this gives


$$
\mathfrak t_p\equiv(-1)^{M+1-p}=1\pmod3,
$$


since $M\equiv p-1\pmod2$.

Hence


$$
\boxed{\mathcal P(W,\widetilde F_{\nu-1}^{(p)})
\equiv3e_{Y_m}\pmod9.}
$$


The last trial column is not a residual-$3^p$ certificate.

---

## 5. Audit of logarithmic compression and $K_N$

Here $p=16$, $N=3^{15}$, and $L=3^{h-16}$.

For nonterminal $p_1,p_2$, let


$$
B=x^D(\beta+3y)p_1p_2,\qquad \deg B\le2D-5.
$$


The trial pairing is the original finite pole functional applied to


$$
x^H B(y)R_N(y^L)^2.
$$



In formal power series,


$$
(1-y)^H=(1-y^L)^N
\exp\!\left(-H\sum_{L\nmid k}\frac{y^k}{k}\right).
$$


Every coefficient of the exponent has valuation at least $16$, so the quadratic exponential error is in $3^{32}$. Truncation is always at the physical pole cutoff.

Write


$$
A_0(Y)=(Y-1)^NR_N(Y)^2=\sum_q a_qY^q.
$$


Then $\deg A_0=2N-1$, and $A_0(1)=0$.

For a coefficient $B_s$, put $c=2s+1$. The window gives


$$
c<4D+1<3^{h-25},\qquad v_3(c)\le h-26.
$$



### 5.1 Terms without the logarithm

For every relevant $q$,


$$
3^h\left(\frac1{c+2qL}-\frac1c\right)\in3^{36}\mathbb Z_3.
$$


The constant-denominator sum is zero because $\sum a_q=0$. All its terms lie within the original cutoff:


$$
(2N-1)L+\deg B<2H-2D+2.
$$



### 5.2 Logarithmic terms

For $k=v-qL-s\ge1$, $L\nmid k$, and $d_v=2v+1$, the scalar valuation is


$$
2h-1-v_3(k)-v_3(d_v).
$$


The valuation checks are:

| Case | Lower bound |
|---|---:|
| $v_3(k)<v_3(c)$ | $53$ |
| $v_3(k)>v_3(c)$ | $42$ |
| A possible contribution modulo $3^{30}$ | $v_3(k)=v_3(c)$, $v_3(d_v)\ge h-4$ |

For the surviving case,


$$
\frac1k\equiv-\frac2c
$$


at the needed precision. After multiplication by $3^hH/d_v$, the error is in $3^{35}$.

Write $d_v=aL$, $a$ odd, and $q_0=(a-1)/2$. Since $s<(L-1)/2$, $k>0$ is exactly $q\le q_0$. Therefore


$$
\sum_{q\le q_0}a_q
=-[Y^{q_0}](1-Y)^{N-1}R_N(Y)^2.
$$


Adding the inactive macro-denominators changes the answer only by $3^{30}$. Their largest denominator is


$$
(4N-3)L=4H-3L<4H-4D+5.
$$



Consequently


$$
G_c(F[p_1],F[p_2])
\equiv K_N\,\mathcal J_h(B)\pmod{3^{30}},
$$


where


$$
\mathcal J_h(B)=3^h\sum_s\frac{B_s}{2s+1}
$$


and


$$
K_N=-N\int_0^1Y^{-1/2}(1-Y)^{N-1}R_N(Y)^2\,dY.
$$



Every inverse loss and stationary payment used to pass from the trial pairing to this corrected pairing has already been accounted for.

### 5.3 Exact scalar and residue

Integration of


$$
\frac{d}{dY}\bigl(Y^{1/2}(1-Y)^NR_N(Y)^2\bigr)
$$


and orthogonality give


$$
N\int_0^1Y^{-1/2}(1-Y)^{N-1}R_N^2
=\left(N+2M+\tfrac12\right)h_R,
$$


where


$$
h_R=\int_0^1Y^{-1/2}(1-Y)^NR_N^2.
$$


The Rodrigues norm yields


$$
\boxed{
K_N=
-\frac{4^{2N-1}}
{\binom{N-1}{(N-1)/2}\binom{3N-1}{(3N-1)/2}}.
}
$$


Both binomial denominators are ternary units.

For


$$
B_q=\binom{3^q-1}{(3^q-1)/2},
$$


stripping multiples of $3$ gives, for $q\ge4$,


$$
B_q\equiv-B_{q-1}\pmod{81}.
$$


Indeed, the complete unit product modulo $81$ is $-1$, while the square of the unit product from $1$ through $40$ is $1$.

Using


$$
B_3=10400600\equiv38\pmod{81},
$$


one gets


$$
B_{15}\equiv38,\quad B_{16}\equiv43,\quad
B_{15}B_{16}\equiv14.
$$


Also $4^{2N-1}\equiv61$ and $14^{-1}\equiv29$. Thus


$$
\boxed{K_N\equiv-61\cdot29\equiv13\pmod{81}.}
$$



---

## 6. The actual coefficient $\Pi$

For the prescribed one-lift polynomials,


$$
B_{ac}
=x^{10Q+b}(\beta+3y)y^{3Q+1+a+c}(y^{3Q}+3)^2.
$$


Let $t=a+c$, $0\le t\le b$. Split this as


$$
B_{\rm high}+6B_{\rm mid}+9B_{\rm low},
$$


with starting exponents $9Q+1+t$, $6Q+1+t$, and $3Q+1+t$.

The accepted raw radical theorem, together with its paid low-degree moment formula whose scalar is $4\pmod{81}$, gives


$$
\mathcal J_h(B_{\rm high})\in3^{30}\mathbb Z_3.
$$


This use is at the accepted raw scope; it does not itself replace a corrected pairing.

For the other two terms, the poles relevant modulo $3^{30}$ are


$$
2s+1=dQ,\qquad d=1,3,\ldots,39,
$$


with weights $3^{29}/d$.

For $6B_{\rm mid}$, only $3\mid d$ matters. The nonzero candidate indices are those for $d=15,21,27$. After expanding $x^b$, they lie in


$$
uQ+\frac Q3<k<uQ+\frac{2Q}{3},
\qquad u=1,4,7.
$$


The required margin is exactly


$$
2b+\frac52<\frac Q6.
$$


The accepted valuation identity


$$
v_3\binom{10Q}{uQ+r}
=v_3(Q)-v_3(r)+v_3\binom9u
$$


therefore gives valuation at least $4$. This pays even the $d=27$ layer.

For $9B_{\rm low}$, only $d=9,27$ can matter. The former has the same valuation-$\ge4$ interval; the latter is above the degree, including the $3y$ shift.

Hence


$$
\mathcal J_h(B_{ac})\in3^{30}\mathbb Z_3.
$$


The corrected compression now gives


$$
G_c(\mathcal F_a,\mathcal F_c)\in3^{30}\mathbb Z_3,
$$


and the exact one-lift formula proves


$$
\boxed{\Pi=0.}
$$



This is an evaluation of the entire matrix, not an extrapolation from a finite table.

---

## 7. Independent proof of the nonterminal strip

The old support-layer argument still contains an unsupported step at its asserted uniform corrected-column comparison. Its degree inequalities do not quantify every higher corrected support layer.

That historical gap is bypassed, not retroactively filled, by the following pole calculation.

### 7.1 Corrected $K$-to-$J$ entries

For


$$
0\le u<\ell,\qquad \ell\le v\le\tau-2,
$$


both columns are nonterminal. Their compressed polynomial is


$$
B=x^D(\beta+3y)y^{9Q+1+u+v}.
$$


The finite bound is


$$
u+v\le\frac Q2+b-\frac72,
$$


so $\deg B<2D$.

Modulo $3^{29}$, the candidate poles have $d=3,9,15,21,27,33,39$.

- $d=3,9,15$ have negative extraction indices.
- The $d=21$ index is at least $N_0+2$ and lies below $9Q$.
- The $d=33$ index lies in the same characteristic-$3$ gap.
- The $d=39$ index is at least $D+2$.
- At $d=27$,
  

$$
k=\frac{9Q-3}{2}-u-v\ge4Q-b+2=3Q+N_0+2.
$$



Use


$$
x^D\equiv(y^Q-1)^9x^{N_0}\pmod{27}.
$$


The band starting at $3Q$ is missed by at least two positions. The only possible band is that starting at $4Q$, whose coefficient is


$$
-\binom94=-126\equiv9\pmod{27}.
$$


Since $\beta\equiv1\pmod3$, and the $3y$ term adds a digit,


$$
\boxed{
\frac{(S_c)_{R_*+u,R_*+v}}{3^{28}}
\equiv[y^{E-u-v}]x^{N_0}\pmod3.
}
$$



### 7.2 Actual finite prefix

For a prefix index $0\le p\le a_0$, the relevant principal index is


$$
9Q-1-p-v.
$$


Its minimum is


$$
4Q+\frac b2+3>3Q+N_0,
$$


and it is below $9Q$. Modulo $9$, only the band beginning at $6Q$ survives. With the sign $U_c=-S_c/3^{26}$, this gives


$$
(\mathsf B_1)_{p,v}
=[y^{3Q-1-p-v}]x^{N_0}.
$$



The finite prefix convolution can also be checked directly. Put


$$
h_r=[y^r](1-y)^{N_0},\qquad
g_r=[y^r](1-y)^{-N_0},
$$


with negative-index coefficients zero. The leading prefix matrix and its inverse are


$$
(\mathsf A_0)_{pq}=h_{a_0-p-q},\qquad
(\mathsf A_0^{-1})_{pq}=g_{p+q-a_0}.
$$


Their product is the finite coefficient convolution $hg=1$.

Since $J_0=3Q-1<a_0$, the nonnegative coefficient conditions force every contributing summand into the original prefix range. Therefore


$$
(\mathsf B_1^T\mathsf A_0^{-1}\mathsf B_1)_{u,v}
=[y^{C-u-v}](1-y)^{N_0},
\qquad C=\frac{3Q-3}{2}.
$$


But


$$
C-u-v\ge N_0+2,
$$


so this correction is zero on the full displayed strip.

Thus


$$
\boxed{
(\bar L_c)_{u,v-\ell}
=[y^{E-u-v}](1-y)^{-b}.
}
$$



### 7.3 Terminal-only contraction and first matrix return

Because $b$ is even,


$$
x^b(1-y)^{-b}=1.
$$


Hence, for $g_a=x^by^a$,


$$
g_a^T\bar L_{c,\cdot,v-\ell}
=[y^{E-v}]y^a=0,
$$


since


$$
E-v\ge b/2+2>a.
$$


Therefore


$$
G^T\bar L_c=\gamma_c\delta_J^T.
$$


The value of $\gamma_c$ is not supplied by this support statement.

Using the accepted finite identities


$$
\bar B^{-1}\delta_J=-e_0,\qquad
\delta_J^T\bar B^{-1}\delta_J=0,
$$


one obtains


$$
\boxed{27G^TL_cB_c^{-1}L_c^TG\in81M.}
$$


The retained producer comparison gives the corresponding actual-producer conclusion.

Together with $\Pi=0$ and the paid rank-$b$ matrix return, this proves $T\in81M$.

---

## 8. New result: bootstrap at the exceptional physical terminal

The exceptional residual must not be discarded. It can instead be used.

### 8.1 A low-precision raw lemma at $p=25$

Set


$$
N=3^{24},\qquad L=3^{h-25},\qquad R=R_N(y^L).
$$



**Lemma.** If $B\in\mathbb Z_3[y]$ and $\deg B<2D$, then


$$
\boxed{
3^h\sum_{v=0}^{2n-2}
\frac{[y^v]x^H B(y)R^2}{2v+1}
\in3^{26}\mathbb Z_3.
}
$$



**Proof.**
Here $L>8D$. In the logarithmic identity, every exponent coefficient has valuation at least $25$, so modulo $3^{26}$ only the linear logarithmic term can matter.

Write


$$
A_0(Y)=(Y-1)^NR_N(Y)^2=\sum_q a_qY^q.
$$


For $B_s$, let $c=2s+1$. Since $c<4D<L$,


$$
v_3(c)\le h-26<v_3(L).
$$


Thus every term without the logarithm has denominator valuation $v_3(c)$ and is already in $3^{26}$.

For a logarithmic term, the scalar valuation is


$$
2h-1-v_3(k)-v_3(d_v).
$$


As before, unequal valuations of $k$ and $c$ cannot contribute. A term below valuation $26$ can occur only when


$$
v_3(k)=v_3(c)=h-26,\qquad v_3(d_v)=h.
$$


The physical bounds then force


$$
c=3^{h-26},\qquad d_v=3^h.
$$


Replacing $1/k$ by $-2/c$ makes an error in $3^{26}$.

The remaining possible contribution is


$$
2\cdot3^{25}B_s\sum_{q\le q_0}a_q,
\qquad q_0=\frac{3N-1}{2}.
$$


But


$$
A_0(Y)\equiv Y^N-1\pmod3,
$$


because $R_N\equiv1\pmod9$. Since $N\le q_0<2N$,


$$
\sum_{q\le q_0}a_q\equiv0\pmod3.
$$


This pays the last digit.

All polynomials before logarithmic truncation lie within the physical cutoff:


$$
2H-L+\deg B<2H-2D+2.
$$


The logarithmic calculation was likewise truncated at that cutoff. ∎

This is a new proof at $p=25$, not an unproved extension to $p>25$.

### 8.2 The last actual coefficient

Let


$$
\widetilde F_T=\widetilde F_{\nu-1}^{(25)},\qquad
r_T=\mathcal P(W,\widetilde F_T)
=3\mathfrak t_{25}e_{Y_m}+3^{25}r.
$$


Put


$$
q_T=E_{\mathcal P}^{-1}r_T,\qquad
F_{\mathcal P,T}=\widetilde F_T-Wq_T.
$$


The inverse loses one digit, while $r_T\in3M$; hence $q_T$ is integral. It is **not** asserted to lie in $3^{24}M$.

Exact orthogonality gives


$$
\mathcal P(\widetilde F_T,\widetilde F_T)
=(S_{\mathcal P})_{TT}+q_T^Tr_T.
$$


The left side is in $3^{26}$ by the lemma, using


$$
B=x^D(\beta+3y)y^{2\nu-2},\qquad \deg B=2D-3.
$$


Also $S_{\mathcal P}\in3^{26}M$. Therefore


$$
3\mathfrak t_{25}(q_T)_{Y_m}
+3^{25}q_T^Tr\in3^{26}\mathbb Z_3.
$$


Reducing modulo $3^{25}$, and using that $\mathfrak t_{25}$ is a unit, yields


$$
(q_T)_{Y_m}\in3^{24}\mathbb Z_3.
$$



The trial polynomial has degree below $m$, so


$$
[y^m]F_{\mathcal P,T}=-(q_T)_{Y_m}.
$$


The pole/complete-core column difference is in $3^{h-1}W$, hence


$$
\boxed{[y^m]F_{\nu-1}\in3^{24}\mathbb Z_3.}
$$



This does not contradict the exceptional residual. The residual remains $3e_{Y_m}\pmod9$; only the physical top coefficient of its actual correction has been shown highly divisible.

### 8.3 One further digit for nonterminal coefficients

For $i\le\nu-2$, write


$$
F_{\mathcal P,i}=\widetilde F_i^{(25)}-Wq_i.
$$


The residual theorem gives $q_i\in3^{24}M$. Exact mixed orthogonality gives


$$
\mathcal P(\widetilde F_i^{(25)},\widetilde F_T)
=(S_{\mathcal P})_{iT}+q_i^Tr_T.
$$


The raw pairing is in $3^{26}$ by the lemma, now with


$$
B=x^D(\beta+3y)y^{i+\nu-1},\qquad \deg B\le2D-4.
$$


Thus


$$
3\mathfrak t_{25}(q_i)_{Y_m}\in3^{26}\mathbb Z_3,
$$


because the remainder $3^{25}q_i^Tr$ is in $3^{49}$. Consequently


$$
\boxed{[y^m]F_i\in3^{25}\mathbb Z_3\quad(i\le\nu-2).}
$$



### 8.4 A physical coordinate of the actual inverse

From


$$
q_T=3\mathfrak t_{25}E_{\mathcal P}^{-1}e_{Y_m}
+3^{25}E_{\mathcal P}^{-1}r
$$


and $(q_T)_{Y_m}\in3^{24}$, while $E_{\mathcal P}^{-1}\in3^{-1}M$, it follows that


$$
(E_{\mathcal P}^{-1})_{Y_m,Y_m}\in3^{23}\mathbb Z_3.
$$


The resolvent identity gives


$$
E_{\mathcal P}^{-1}-E_c^{-1}\in3^{h-2}M.
$$


Hence


$$
\boxed{(E_c^{-1})_{Y_m,Y_m}\in3^{23}\mathbb Z_3.}
$$



This is an actual same-$W$ inverse estimate. It does not bound the eventual $C^{-1}z$.

---

## 9. A more explicit remaining formula for $\gamma_c$

The exceptional residual also gives a precise mixed-pairing identity.

Using $p=16$, a nonterminal corrected combination $\mathcal F_a$, and the last middle column $F_T$, exact orthogonality gives


$$
G_c(\mathcal F_a,F_T)
\equiv
K_{3^{15}}\mathcal J_h(B_{aT})
+3\mathfrak t_{16}[y^m]\mathcal F_a
\pmod{3^{30}},
$$


where


$$
B_{aT}
=x^{10Q}(\beta+3y)
y^{(13Q-b-3)/2+a}(y^{3Q}+3).
$$


The residual remainder is paid: the nonterminal correction is in $3^{15}W$, while the terminal residual remainder is in $3^{16}M$, giving $3^{31}$.

The raw logarithmic compression applies here because $\deg B_{aT}<2D$; it is not being used to erase the terminal correction.

Put


$$
r_a=b/2+1-a,\qquad 1\le r_a<Q/27.
$$


At the $d=27$ pole, the two extraction indices are


$$
4Q+r_a,\qquad 7Q+r_a.
$$


For $r_a>0$, their binomial coefficients in $x^{10Q}$ have valuation at least $6$. The sole contribution modulo $3^{29}$ occurs when $a=b/2$, from the $3y$-shift at $4Q$. Its divided coefficient is


$$
\frac1{3}\binom{10Q}{4Q}\equiv
\frac1{3}\binom{10}{4}=70\equiv1\pmod3.
$$


The scaling congruence follows by stripping multiples of $3$ from $\binom{3a}{3b}$; its unit quotient is $1\pmod3$.

The other active poles are either outside support or have an additional paid digit. Therefore


$$
\boxed{
\mathcal J_h(B_{aT})\equiv
3^{28}\delta_{a,b/2}\pmod{3^{29}}.
}
$$



The accepted one-lift middle-terminal identity says


$$
(\gamma_c)_a=-3^{-28}G_c(\mathcal F_a,F_T)\pmod3.
$$


It follows first that


$$
[y^m]\mathcal F_a\in3^{27}\mathbb Z_3,
$$


and then, since $K_{3^{15}}\equiv\mathfrak t_{16}\equiv1\pmod3$,


$$
\boxed{
(\gamma_c)_a
=
-\delta_{a,b/2}
-\frac{[y^m]\mathcal F_a}{3^{27}}
\pmod3.
}
$$



This is not an evaluation of $\gamma_c$. It is an evaluated boundary term plus a sharply specified actual coefficient obligation. In particular, the vanishing of $3^{-20}[y^m]\mathcal F_a\pmod3$ says nothing about the coefficient divided by $3^{27}$.

A concrete next terminal lemma would determine


$$
[y^m]\mathcal F_a\pmod{3^{28}}
$$


for the original $\Psi_a$, without replacing $W$ or extending $p$ beyond $25$ without a new construction.

---

## 10. Complete forcing and all returned channels

The producer is unchanged:


$$
Q_{\rm act}=3P_n=Q_c+3^7\mathscr R,
$$




$$
3^7\mathscr R=\sum_{a=0}^{A+1}e_ax^a,\qquad
e_a=-\frac{(A+1)!}{a!}(t_a+\xi v_a),
$$


with the complete force


$$
t=3nh_{\rm vec}
+(b_{\rm force}+6)e_{n-1}
+\frac{2b_{\rm force}}{n-1}e_{n-2},
\qquad b_{\rm force}=-n-66.
$$


The signed $\xi$ and its paid normalization remain intact, as do


$$
\mathscr R(-1)
=-\frac{\xi((A+1)!)^2}{3^7},
$$




$$
J^T\varepsilon+\omega
=-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
$$



### 10.1 First-radical returns

For $\alpha=c,\mathrm{act}$,


$$
\mathcal S_\alpha^{(2)}
=\mathcal R_{\alpha,KK}
-27L_\alpha B_\alpha^{-1}L_\alpha^T,
$$




$$
f_\alpha^{(2)}
=f_{\alpha,K}-3L_\alpha B_\alpha^{-1}f_{\alpha,J},
$$




$$
\lambda_\alpha^{(2)}
=\lambda_\alpha-\frac13f_{\alpha,J}^TB_\alpha^{-1}f_{\alpha,J}.
$$


The inverse cost is $3^{-1}$.

The new terminal bootstrap gives $\bar t_K=\bar t_J=0$. Therefore the supplied producer congruences now yield


$$
\bar L_{\rm act}=\bar L_c,
$$




$$
f_{\rm act}^{(2)}-f_c^{(2)}\equiv0\pmod9,
$$


and the additional evaluated diagonal consequence


$$
\boxed{\lambda_{\rm act}^{(2)}-\lambda_c^{(2)}\equiv0\pmod3.}
$$



Nevertheless,


$$
G^Tf_\alpha^{(2)}
\equiv G^Tf_{\alpha,K}+3\varepsilon_0\gamma_c\pmod9
$$


still contains the unevaluated $\gamma_c$.

### 10.2 Rank-$b$ returns

Retain all three exact formulas:


$$
T_{\rm new}=T_{RR}-81M_b^TA_b^{-1}M_b,
$$




$$
f_{\rm new}=f_R-3M_b^TA_b^{-1}f_b,
$$




$$
\lambda_{\rm new}
=\lambda^{(2)}-\frac19f_b^TA_b^{-1}f_b.
$$


The inverse cost is $3^{-2}$.

The new congruence for $\lambda^{(2)}_{\rm act}-\lambda^{(2)}_c$ does **not** by itself propagate to the same congruence after this elimination: the paid $1/9$ return can expose endpoint differences. No such propagation is asserted.

After all retained returns and actual endpoint adaptation,


$$
T=\begin{pmatrix}a&z^T\\z&C\end{pmatrix}\in81M,
\qquad v_3(\lambda)=-1.
$$


At order $81$, the second prefix lift, the next $J$-return, the producer contribution, and the rank-$b$ matrix return are all visible.

---

## 11. A paid inverse direction in the fully returned Schur pair

This consequence uses the **actual final** $a,z,C,\lambda$, after all returns.

In endpoint-adapted coordinates, the bordered matrix is


$$
\mathscr H=
\begin{pmatrix}
\lambda&1&0\\
1&a&z^T\\
0&z&C
\end{pmatrix}.
$$


Write


$$
a=81\alpha,\quad z=81w,\quad C=81B,\quad
\lambda=\eta/3,\quad \eta\in\mathbb Z_3^\times.
$$


Set


$$
u=1-\lambda a=1-27\eta\alpha.
$$


Then


$$
\boxed{u\in1+27\mathbb Z_3.}
$$



The first two coordinates have the explicit inverse


$$
\begin{pmatrix}\lambda&1\\1&a\end{pmatrix}^{-1}
=
\begin{pmatrix}
-a/u&1/u\\
1/u&-\lambda/u
\end{pmatrix}.
$$


Its loss is exactly one digit in the lower-right entry. The displacement of the remaining coordinates is explicitly


$$
\begin{pmatrix}z^T/u\\-\lambda z^T/u\end{pmatrix},
$$


whose two rows lie respectively in $3^4M$ and $3^3M$.

Eliminating this paid block gives the actual returned matrix


$$
\boxed{
C^\sharp=C+\frac{\lambda}{u}zz^T,
\qquad C^\sharp-C\in3^7M.
}
$$


No inverse of $C$ has been assumed.

If $r=b/2$, the two distinguished local cofactors satisfy


$$
D_0=\det T,\qquad
\boxed{D_1=u\det C^\sharp.}
$$


Equivalently,


$$
C^\sharp
=81\left(B+\frac{27\eta}{u}ww^T\right),
$$


so


$$
\boxed{\frac{D_1}{81^r}\equiv\det B\pmod{27}.}
$$



This is an evaluated, paid boundary inverse and an explicit improvement of the fully returned Schur representation. It does not close the remaining annihilator solve.

### 11.1 Why $T\in81M$ gives no growing saving

The obstruction is real, not merely a missing estimate. For the bare valuation hypotheses, take $r=1$,


$$
a=0,\quad z=81,\quad C=-2187\eta,\quad \lambda=\eta/3.
$$


Then $T\in81M$, $C\ne0$, but


$$
C^{-1}z=-\frac1{27\eta},
$$


and


$$
D_0=-81^2,\qquad D_1=0.
$$


Replacing $C$ by $-2187\eta+81\cdot3^k$ makes $D_1$ arbitrarily highly divisible without changing $D_0$.

This example is only a counterexample to an inference from the stated valuation hypotheses; it is not a model substituted for the original matrices.

Thus neither $\Pi=0$ nor $T\in81M$ proves a favorable relative cofactor estimate.

### 11.2 Concrete fully returned directional lemma

A useful next obligation is now:

> For the actual
> 

$$
> B^\sharp=B+\frac{27\eta}{u}ww^T,
>
$$


> prove nonsingularity and construct its actual directional solution
> 

$$
> B^\sharp v=w,\qquad v\in3^{-1}\mathbb Z_3^r,
>
$$


> uniformly on the same infinite original subwindow.

This is a linear-system target in the fully returned object, not a named unknown Schur scalar.

Its implication is rigorous. If such $v$ exists, then


$$
\epsilon=1-\frac{27\eta}{u}w^Tv\in1+9\mathbb Z_3.
$$


The determinant lemma gives $\det B=\epsilon\det B^\sharp\ne0$, and


$$
B^{-1}w=v/\epsilon\in3^{-1}\mathbb Z_3^r.
$$


Hence


$$
C^{-1}z\in3^{-1}\mathbb Z_3^r.
$$


If the resulting Schur scalar is nonzero, this gives a fixed relative gain of at least $3$; an integral solution gives at least $4$. Neither conclusion is a growing saving.

A full-Gram inverse dual to the **actual omitted middle coefficient functionals** is a possible classical interface for this lemma. Merely writing that inverse as an unevaluated kernel sum would not prove the lemma, and replacing $W$ by consecutive Jacobi degrees would address a different projection.

---

## 12. Remaining resonance, arithmetic ledger, and whole error

The complete moments still obey


$$
\mu_{t+1}+\mu_t
=
\frac{3^h}{2t+1}
-\frac{3^h}{4}\bigl((2t+2)!+(2t)!\bigr),
\qquad 0\le t\le2n-2.
$$


The forward resonance


$$
t_*=\frac{3^h-5}{2}
$$


still has a genuine divisor of valuation $h$. Its highest moment remains physical:


$$
\frac{3H+1}{2}\le2n-1
\iff H-4D+5\ge0.
$$


Neither the filter nor the returned two-coordinate pivot removes that divisor.

### 12.1 Division ledger

| Operation | Payment |
|---|---|
| Original poles | $3^h$, on the original cutoff |
| Local factorial removal | Schur perturbation $3^h$, including inverse loss |
| LOW/HIGH inverse | $3^{-1}$ |
| Jacobi normalization | $v_3(r_k)=p-v_3(k)\ge2$ |
| $p=16$ nonterminal residual | $16\to15$; stationary error $3^{30}$ |
| $p=25$ nonterminal residual | $25\to24$ |
| Exceptional terminal residual | Retained $3\mathfrak t_p e_{Y_m}$, not discarded |
| New terminal bootstrap | Exact stationary identity, then division by $3\mathfrak t_{25}$ |
| Physical inverse diagonal transfer | Resolvent loss $3^{h-2}$ |
| Core normalization | $3^{26}$ |
| Prefix lift | Exact $81Z^T\mathsf A Z$ return |
| Projection observation | Whole pairing divided by $3^{29}$ |
| Middle-terminal observation | Whole pairing divided by $3^{28}$ |
| New $\gamma_c$ target | Actual physical coefficient divided by $3^{27}$, divisibility proved |
| First-radical inverse | $3^{-1}$ |
| Rank-$b$ inverse | $3^{-2}$ |
| Fully returned boundary pivot | One-digit loss; rank-one return in $3^7M$ |
| Eventual annihilator inverse | Still open |
| Forward resonance | Genuine $3^h$ divisor retained |

There is no new content division.

### 12.2 Actual contents, clearer, gcd, and primitive denominator

The actual original column contents and the actual least simultaneous clearer $\ell_{\rm clr}$ are unchanged. Neither beta denominators nor Jacobi coefficients define a replacement global clearer.

Retain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


and the gcd over **all primes**


$$
\boxed{g_\ell=\gcd(|A_\ell|,|B_\ell|).}
$$


For $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


The whole evaluated error remains


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
{g_\ell}\det H_{\rm complete}.
}
$$



No ordinary-error comparison is reopened here.

An irrationality proof would still require, at the same infinite original indices,


$$
B_\ell\ne0,\qquad \det H_{\rm complete}\ne0,
$$


and


$$
\boxed{
\log g_\ell-(m+1)\log\ell_{\rm clr}
-\log|\det H_{\rm complete}|\longrightarrow+\infty.
}
$$


This makes the nonzero whole error tend to zero, which is impossible for rational $e+\pi$. None of the present fixed-depth results proves this condition.

---

## 13. Bounded exact-arithmetic checks

No tool computation was performed. No dense original-index calculation is proposed.

The analytic arguments above need, at most, a small optional constant certificate.

### Inputs

- modulus $81$;
- integers $1,\ldots,80$;
- $\binom{26}{13}$ and $\binom{10}{4}$;
- the exponents $15,16$, used only in the proved recurrence;
- optionally $p=2,N=3,M=1$ for the universal terminal-moment formula.

### Expected verifiable outputs



$$
\binom{26}{13}=10400600\equiv38\pmod{81},
$$




$$
\prod_{\substack{1\le a\le80\\3\nmid a}}a\equiv-1\pmod{81},
\qquad
\left(\prod_{\substack{1\le a\le40\\3\nmid a}}a\right)^2\equiv1\pmod{81},
$$




$$
B_{15}\equiv38,\quad B_{16}\equiv43,\quad
B_{15}B_{16}\equiv14,
$$




$$
14^{-1}\equiv29,\quad4^{-1}\equiv61,\quad
K_{3^{15}}\equiv13\pmod{81},
$$


and


$$
\binom{10}{4}=210,\qquad 210/3\equiv1\pmod3.
$$


The optional terminal base value is


$$
\mathfrak t_2=\frac{256}{385}\equiv1\pmod3.
$$



These checks require only a few hundred bounded integer or modular operations. Their outputs certify fixed constants. The uniform original-index statements follow from the analytic proofs, not from extrapolation of these finite outputs.

No closed H2, producer, adjoining-boundary, or large determinant calculation is repeated.

---

## 14. Proof-status ledger and final bottleneck

| Statement | Status after this audit |
|---|---|
| Turn 0 pole/complete-core Schur replacement | Independently verified with inverse payment |
| Turn 0 one-lift identity and stationary certificates | Independently verified |
| Sparse filter on the actual LOW/HIGH space, $16\le p\le25$ | Independently verified |
| Physical finite-degree and cutoff checks | Independently verified |
| Last trial residual $3\mathfrak t_p e_{Y_m}$ | Independently verified and retained |
| $\mathfrak t_p\equiv1\pmod3$ | New evaluated unit |
| Logarithmic compression through $3^{30}$ | Independently verified |
| $K_{3^{15}}\equiv13\pmod{81}$ | Independently evaluated |
| Actual $\Pi$ | Verified to be zero |
| Historical full support-layer proof | Still not independently completed as a proof |
| Required nonterminal strip | Independently proved by the alternative pole argument |
| $T\in81M$ after paid matrix returns | Verified |
| Nonterminal physical coefficients in $3^{25}$ | New proved strengthening |
| Last physical coefficient in $3^{24}$ | New proved terminal bootstrap |
| $(E_c^{-1})_{Y_m,Y_m}\in3^{23}$ | New actual same-$W$ inverse estimate |
| Original normalized physical-terminal vector $\bar t$ | Evaluated: zero |
| $\gamma_c$ | Still open; explicit boundary/coefficient formula derived |
| Fully returned two-coordinate inverse | Proved, with one-digit loss |
| Actual $C^{-1}z$, or equivalent returned directional solve | Open |
| Growing relative-cofactor saving | Open |
| All-prime gcd versus nonzero whole error | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

### Final conclusion

The new projection arithmetic is sound at its stated scope. In particular,


$$
\boxed{\Pi=0,\qquad T\in81M.}
$$



The additional terminal bootstrap proves more than the direct nonterminal filter estimate:


$$
\boxed{
[y^m]F_i\in3^{25}\ (i\le\nu-2),\qquad
[y^m]F_{\nu-1}\in3^{24},\qquad
(E_c^{-1})_{Y_m,Y_m}\in3^{23}.
}
$$


It does so by **using**, not suppressing, the surviving unit-amplitude residual multiplied by $3$.

The next precise local bottlenecks are:

1. the actual coefficients $[y^m]\mathcal F_a\pmod{3^{28}}$, which now determine $\gamma_c$ through an evaluated boundary formula;
2. the fully returned directional solve for $B^\sharp$, with the second prefix lift, next $J$-return, producer, endpoint, diagonal, and rank-$b$ contributions all retained;
3. a nonzero, growing relative arithmetic improvement, followed by the same-index all-prime primitive whole-error comparison.

The evaluated zero digit does not provide that growth. Accordingly,


$$
\boxed{\text{No unconditional rationality or irrationality proof for }e+\pi
\text{ is obtained.}}
$$


