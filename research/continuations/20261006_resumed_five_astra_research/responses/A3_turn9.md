> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3, Turn 9 — A product-ideal certificate with clipped collision loss, and an exact restriction on endpoint-exclusive cancellation

## Executive conclusions

The rationality or irrationality of $e+\pi$ remains unresolved.

I accept the newly supplied $3375$ moment-reference receipt at its actual finite scope. Its source preserves the complete residual and verifies the claimed four terminal equations, twelve integral projection identities, terminal normal identity, and complete $\mathscr K_n$ bounds. At that index,


$$
\delta_0^{>}=\delta_3^{>}=\mathfrak D_0=\mathfrak D_3=1,
$$


both large normal-coefficient gcds excluding $G_j$ are $1$, and both structural gcds are $6754$. These calculations are complete; I do not propose repeating them.

This turn advances the **product**, rather than merely the saturated common ideal.

The main new result is an exact restriction on the two endpoint-exclusive factors. It uses a single evaluated residual belonging to the shared contact column:


$$
\mathcal D_L
=
mZ(Qh-P\ell)-F\mathscr K_n,
$$


where


$$
P=nX+Y,\qquad Q=nZ+2X-Y,\qquad
F=2m\bigl(Y-2X-(n-1)Z\bigr).
$$



After an explicit small-prime-supported normalization, define


$$
\Theta_n=\frac{2^{(n+1)/2}}{n!}\mathcal D_L\in\mathbb Z.
$$


For every original index at which $\Theta_n\ne0$, put


$$
D_n^{>}=(|\Theta_n|)_{>n+2},
$$




$$
\mathcal B_n=\gcd(\ell,Z,Y-2X,\mathscr K_n)_{>n+2},
\qquad
\mathcal A_n=\frac{D_n^{>}}{\mathcal B_n^2}.
$$


The proof below establishes that $\mathcal A_n$ is an integer.

Retain


$$
\delta_j^{>}=\gcd(R_j,C_j)_{>n+2},\qquad
g_n=\gcd(\delta_0^{>},\delta_3^{>}),
$$


and write


$$
\delta_j^{>}=g_nE_{j,n},\qquad \gcd(E_{0,n},E_{3,n})=1.
$$


Let $\Sigma_n$ be the actual large-prime contact-row collision index from Turn 8.

The new conclusions are


$$
\boxed{
\mathcal B_n\mid g_n,\qquad
\Gamma_n:=\frac{g_n}{\mathcal B_n}\mid\Sigma_n,
}
\tag{E1}
$$




$$
\boxed{
E_{0,n}E_{3,n}
\mid
\frac{\mathcal A_n}{\gcd(\mathcal A_n,\Sigma_n)},
}
\tag{E2}
$$


and


$$
\boxed{
\gcd\!\left(E_{0,n}E_{3,n},\frac{\Sigma_n}{\Gamma_n}\right)=1.
}
\tag{E3}
$$



Thus endpoint-exclusive cancellation cannot simply be placed arbitrarily on $\Sigma_n$. If the endpoint cancellation depths differ at a prime, the common cancellation has to attain **exactly the full collision depth above the source content**.

More importantly, there is a genuine product-ideal certificate:


$$
\boxed{
\delta_0^{>}\delta_3^{>}
\mid
D_n^{>}\gcd(\Sigma_n,\mathcal A_n).
}
\tag{E4}
$$


Consequently the integer


$$
\boxed{
\mathcal W_n
=
D_n^{>}\gcd(\Sigma_n,\mathcal A_n)
}
\tag{E5}
$$


belongs to


$$
(R_0,C_0)(R_3,C_3)
$$


after localization **only at primes at most $n+2$**.

This clips the collision loss: the cost is not all of $\Sigma_n$, but only


$$
\gcd(\Sigma_n,\mathcal A_n).
$$



I also prove that $\Theta_n\ne0$ for all sufficiently large original indices. Its unreduced integer size is


$$
\boxed{
\log|\Theta_n|
=
3\log(n!)
+n\log(2+\sqrt2)
+\frac52\log n
+O(1).
}
\tag{E6}
$$


This supplies an unconditional nonzero product certificate eventually, but **not** an exponential-height one. The large-prime part of $\Theta_n$, and the clipped collision gcd in (E5), remain uncontrolled at the required $O(n)$ scale.

The exclusive-content bound is nevertheless genuinely stronger than two separate reference-height bounds:


$$
\boxed{
\log(E_{0,n}E_{3,n})
\le 3\log(n!)+O(n),
}
\tag{E7}
$$


with the sharper exact subtractions displayed below. This is still far from the required $O(n)$ or $o(n\log n)$ result.

---

# I. Source assessment and unchanged construction

## 1. What the completed $3375$ receipt establishes

The supplied program is an exact postprocessing of the retained complete artifact. In particular, it:

- recovers the actual factorial-normalized moments and force coefficients;
- retains the fixed $E_n$;
- forms
  

$$
b_n=u_n-E_nh_n-a_n,\qquad
  b_{n+1}=u_{n+1}-E_nh_{n+1}-a_{n+1};
$$


- includes the complete logarithmic term in
  

$$
\mathscr K_n
  =h_nb_{n+1}-h_{n+1}b_n-2(n!)^3;
$$


- reconstructs $\mathbf U,\mathbf Q,\mathbf C$ without dropping the exterior correction;
- forms the primitive contact rows from the actual adjugate rows and their actual contents;
- removes every prime at most $3377$, and then, where appropriate, every prime power supported on $G_j$.

The repeated-gcd loop used to exclude support on $G_j$ is appropriate: it removes all such prime powers without assuming that a single gcd removes their full exponents.

The resulting finite facts are:

| Quantity | Endpoint $0$ | Endpoint $3$ |
|---|---:|---:|
| $\gcd(G_j,C_j)$ | $6754$ | $6754$ |
| Structural bound | $1756251198988290048$ | $519908584662016$ |
| $\delta_j^{>}$ | $1$ | $1$ |
| Large normal-$F$ gcd excluding $G_j$ | $1$ | $1$ |
| $\mathfrak D_j$ | $1$ | $1$ |
| $\Pi_j$ | $11410879$ | $11404126$ |

The first endpoint-$0$ residual has bit length $143103$. Since that residual is $\mathcal D_L$, the receipt already establishes


$$
\mathcal D_L\ne0
$$


at $3375$. No additional nonvanishing calculation is needed there.

These are finite corroborations of the symbolic identities and bounds, not evidence for universal exclusion of large-prime cancellation.

## 2. Scope retained throughout

The index domain remains


$$
n=15^r,\quad r\ge2,
\qquad\text{or}\qquad
n=105^r,\quad r\ge2.
$$



All original indices are odd. Write


$$
m=n+1,\qquad N=n+2.
$$



The following remain unchanged:

- the original $3\times3$ contact matrix;
- the original force cutoff $2n+2$;
- both corrected reconstruction columns;
- the complete terminal return;
- the exterior $+1$;
- the least clearer over all eight entries;
- all actual reconstruction row contents;
- all primes in the final weighted gcd;
- the actual primitive denominator;
- the whole error at the same original index.

The results below use the closed large-prime moment primitivity, reference unit-ideal theorem, complete residual decomposition, and polynomial projection comparison at their stated $p>N$ scope.

They do **not** require treating Turn 8’s saturation theorem as independently accepted. The local product argument is proved here from the actual columns and primitive rows.

---

# II. The actual complete scalar used in the product certificate

## 3. Moment, reference, and complete residual data

Retain


$$
X=ma_n,\qquad Y=mna_{n-1},\qquad Z=2a_{n+1}-ma_n,
$$




$$
h=n!\tau_n,\qquad \ell=n!\tau_{n+1}.
$$



The actual terminal columns are


$$
\mathbf H=\frac m2(hv'+\ell w'),
$$




$$
\mathbf C=S_nv'+T_nw'+mZe_2,
$$


where


$$
v'=(2N,N,m)^T,\qquad
w'=(0,N,2n+3)^T,\qquad e_2=(0,0,1)^T,
$$


and


$$
S_n=\frac{mb_n}{2}+2n!m!\rho_n,
$$




$$
T_n=b_{n+1}-\frac{mb_n}{2}+2n!m!\rho_{n+1}.
$$



The complete companion identity is


$$
\boxed{hT_n-\ell S_n=\mathscr K_n.}
\tag{3.1}
$$



The fixed exponential/exterior seed is still


$$
(h_0,h_1,h_2)=(1,1,n+2),
$$




$$
(b_0,b_1,b_2)=(-1,n,n+2-n^2).
$$


In particular, $b_0=-1$ has not been replaced by a homogeneous seed.

The retained complete forcing is


$$
\begin{aligned}
F_k={}&(n+1)a_k-nk\,a_{k-1}\\
&+\frac{(n-1)k(k-1)}2a_{k-2}
+\frac{k(k-1)(k-2)}2a_{k-3}.
\end{aligned}
$$


The associated initial exterior coordinates remain


$$
w_{1,2}=2-n-2n^2,\qquad
w_{2,2}=2n+4-n^2,\qquad
w_{3,2}=n+1.
$$



At the original indices,


$$
\boxed{
\mathscr K_n=h_nb_{n+1}-h_{n+1}b_n-2(n!)^3,
}
\tag{3.2}
$$


with the retained bounds


$$
\boxed{
\mathscr K_n<0,\qquad
(n!)^3<|\mathscr K_n|<3(n!)^3.
}
\tag{3.3}
$$



No earlier-index logarithmic recurrence is being introduced.

## 4. The common contact column

Both actual endpoint rows annihilate


$$
L=nJ_0+J_1.
$$


The evaluated column identity is


$$
\boxed{
L=\frac12(Pv'+Qw'+Fe_2),
}
\tag{4.1}
$$


where


$$
P=nX+Y,
$$




$$
Q=nZ+2X-Y,
$$




$$
F=2m\bigl(Y-2X-(n-1)Z\bigr).
$$



Define the complete shared residual


$$
\boxed{
\mathcal D_L=mZ(Qh-P\ell)-F\mathscr K_n.
}
\tag{4.2}
$$


This is exactly Turn 7’s $\mathcal D_{0,0}$. It also satisfies


$$
\mathcal D_L=n\mathcal D_{3,0}+\mathcal D_{3,1}.
$$


Thus it is not a newly chosen residual with a modified seed or forcing.

## 5. Integral normalization supported only on small primes

Put


$$
L_{\rm ref}=2^{m/2},
\qquad
\widehat h=L_{\rm ref}\tau_n,\qquad
\widehat\ell=L_{\rm ref}\tau_{n+1}.
$$


The constant-term denominators imply


$$
\widehat h,\widehat\ell\in\mathbb Z.
$$



Also define


$$
\widehat{\mathscr K}
=
\widehat h\,b_{n+1}
-\frac m2(\widehat h+\widehat\ell)b_n
-2L_{\rm ref}(n!)^2.
$$


Because $m$ is even and the actual $b_n,b_{n+1}$ are integral,


$$
\widehat{\mathscr K}\in\mathbb Z.
$$


Using the actual terminal reference relation,


$$
\widehat{\mathscr K}
=\frac{L_{\rm ref}}{n!}\mathscr K_n.
$$



Consequently


$$
\boxed{
\Theta_n
=
mZ(Q\widehat h-P\widehat\ell)
-F\widehat{\mathscr K}
=
\frac{L_{\rm ref}}{n!}\mathcal D_L
\in\mathbb Z.
}
\tag{5.1}
$$



For every $p>N$,


$$
\boxed{v_p(\Theta_n)=v_p(\mathcal D_L).}
\tag{5.2}
$$



This normalization is legitimate for the requested localization: $L_{\rm ref}/n!$ is a unit there. The subsequent height statements concern the canonical integer $\Theta_n$, or its actual large-prime part—not a rational number made artificially small by arbitrary small-prime division.

---

# III. Exact source content transverse to the common column

## 6. Large-prime primitivity of $L$

Fix $p>N$, and work over $\mathcal O=\mathbb Z_p$.

The coordinate matrix


$$
B_{\rm coord}=(v'\ \ w'\ \ e_2)
$$


has determinant


$$
\det B_{\rm coord}=2N^2,
$$


a unit in $\mathcal O$.

The map


$$
(X,Y,Z)\longmapsto
\left(P,Q,\frac{F}{2m}\right)
$$


has determinant $-N$. Hence the closed moment primitivity


$$
(X,Y,Z)=\mathcal O
$$


implies


$$
\boxed{L\text{ is primitive over }\mathcal O.}
\tag{6.1}
$$



The reference column $\mathbf H$ is primitive over $\mathcal O$, because


$$
(h,\ell)=\mathcal O.
$$



## 7. An exact source-content identity

Extend $L$ to an $\mathcal O$-basis of $\mathcal O^3$. Project $\mathbf H,\mathbf C$ onto the two coordinates transverse to $L$, and arrange those two projected columns in a $2\times2$ matrix $B$.

The choice of complementary basis changes $B$ by left multiplication by an invertible matrix. Thus the content valuation of $B$ is well defined.

### Lemma 7.1 — Exact transverse content

One has


$$
\boxed{
\min_{a,b}v_p(B_{ab})
=
b_p:=
\min\{v_p(\ell),v_p(Z),v_p(Y-2X),v_p(\mathscr K_n)\}.
}
\tag{7.1}
$$



### Proof

For $t\ge1$, the condition


$$
B\equiv0\pmod{p^t}
$$


is equivalent to the existence of $\lambda,\mu\in\mathcal O$ such that


$$
\mathbf H\equiv\lambda L,\qquad
\mathbf C\equiv\mu L\pmod{p^t}.
\tag{7.2}
$$



Suppose first that (7.2) holds. Since $\mathbf H$ is primitive, $\lambda$ is a unit.

In the $v',w',e_2$ coordinates, the reference column has zero third coordinate. Therefore


$$
F\equiv0\pmod{p^t}.
$$


The third coordinate of the complete residual then gives


$$
Z\equiv0\pmod{p^t}.
$$


The displayed formula for $F$ yields


$$
Y-2X\equiv0\pmod{p^t}.
$$


Hence


$$
Q\equiv0\pmod{p^t},
$$


and comparison of the $w'$-coordinate in the reference congruence gives


$$
\ell\equiv0\pmod{p^t}.
$$


Finally, $\mathbf H$ and $\mathbf C$ are proportional modulo $p^t$, so their $v'\wedge w'$ coefficient gives


$$
\mathscr K_n\equiv0\pmod{p^t}.
$$



Conversely, suppose


$$
\ell,\ Z,\ Y-2X,\ \mathscr K_n\in p^t\mathcal O.
$$


Then


$$
Q,F\in p^t\mathcal O.
$$


Moment primitivity forces $X$ to be a unit: otherwise $X,Y,Z$ would all vanish modulo $p$. Thus


$$
P=nX+Y\equiv NX\pmod{p^t}
$$


is a unit.

Reference primitivity makes $h$ a unit. From


$$
hT_n-\ell S_n=\mathscr K_n
$$


we obtain


$$
T_n\equiv0\pmod{p^t}.
$$


In the chosen coordinates,


$$
L\equiv(P/2,0,0)^T,
\quad
\mathbf H\equiv(mh/2,0,0)^T,
\quad
\mathbf C\equiv(S_n,0,0)^T
\pmod{p^t}.
$$


Thus both columns are multiples of $L$ modulo $p^t$.

The equivalence for every $t$ proves (7.1). ∎

This identifies the actual source content exactly. It is not merely an upper bound obtained after arbitrary saturation.

## 8. The source determinant is the complete shared residual

Direct calculation in the same coordinates gives


$$
\begin{aligned}
\det(L,\mathbf H,\mathbf C)
&=
2N^2\frac m4
\left(P\ell mZ-QhmZ+F\mathscr K_n\right)\\
&=
-\frac{mN^2}{2}\mathcal D_L.
\end{aligned}
$$


Therefore


$$
\boxed{
\det(L,\mathbf H,\mathbf C)
=-\frac{mN^2}{2}\mathcal D_L.
}
\tag{8.1}
$$



Since the basis containing $L$ has unit determinant over $\mathcal O$,


$$
\boxed{
v_p(\det B)=d_p:=v_p(\mathcal D_L)=v_p(\Theta_n).
}
\tag{8.2}
$$



When $\Theta_n\ne0$, the Smith invariants of $B$ have valuations


$$
\boxed{b_p,\quad d_p-b_p.}
\tag{8.3}
$$


In particular,


$$
\boxed{d_p\ge2b_p.}
\tag{8.4}
$$



This proves the integrality of


$$
\mathcal A_n=D_n^{>}/\mathcal B_n^2.
$$



---

# IV. The product-content lemma

## 9. The actual observation matrix and its collision index

Let


$$
r_0=\frac{\mathscr R_0}{c_0},
\qquad
r_3=\frac{\mathscr R_3}{c_3},
$$


with


$$
\mathscr R_0=(-1,n,-nm)\operatorname{adj}(J),
\qquad
\mathscr R_3=(0,0,1)\operatorname{adj}(J),
$$


and $c_j$ their actual positive three-coordinate contents.

The cross-product identity is


$$
\mathscr R_0\times\mathscr R_3
=\det(J)L.
$$


Up to the selected row signs,


$$
r_0\times r_3
=\pm\frac{\det J}{c_0c_3}L.
$$


Hence


$$
\sigma_n=\operatorname{cont}(r_0\times r_3)
=\frac{|\det J|\operatorname{cont}(L)}{c_0c_3}.
$$



Let


$$
s_p=v_p(\sigma_n).
$$


At $p>N$, primitivity of $L$ gives


$$
s_p=v_p(\det J)-v_p(c_0)-v_p(c_3).
$$



In the basis used above, the two endpoint rows have the form


$$
(r_0;r_3)=(A\ \ 0),
$$


where $A$ is $2\times2$, each row of $A$ is primitive, and


$$
v_p(\det A)=s_p.
$$



The matrix of actual endpoint projections is exactly


$$
\boxed{
\begin{pmatrix}
R_0&C_0\\
R_3&C_3
\end{pmatrix}
=AB.
}
\tag{9.1}
$$



Thus this is a statement about the actual $R,Q,F$-generated residual construction, not an arbitrary full-state transfer.

## 10. Local exclusive-depth rigidity

Set


$$
e_j=\min\{v_p(R_j),v_p(C_j)\},
$$


and abbreviate


$$
b=b_p,\qquad d=d_p,\qquad s=s_p,\qquad a=d-2b.
$$



### Theorem 10.1 — Product and exclusive-content bounds

If $d<\infty$, then


$$
\boxed{b\le e_j\le d-b.}
\tag{10.1}
$$


Also,


$$
\boxed{0\le\min(e_0,e_3)-b\le s.}
\tag{10.2}
$$



If the endpoint depths differ, then


$$
\boxed{
e_0\ne e_3
\quad\Longrightarrow\quad
\min(e_0,e_3)=b+s.
}
\tag{10.3}
$$



Consequently,


$$
\boxed{
|e_0-e_3|\le(d-2b-s)_+,
}
\tag{10.4}
$$


and


$$
\boxed{
e_0+e_3
\le d+\min\{s,d-2b\}.
}
\tag{10.5}
$$



### Proof

Divide $B$ by $p^b$. Its Smith invariants now have valuations $0,a$. Since each row of $A$ is primitive, the content of its product with $B/p^b$ lies between $0$ and $a$. This gives


$$
b\le e_j\le b+a=d-b.
$$



Put $e=\min(e_0,e_3)$. The adjugate identity


$$
\operatorname{adj}(A)\,AB=(\det A)B
$$


shows


$$
e\le b+s.
$$


The lower bound $e\ge b$ was just proved.

Now suppose $s>0$. Since both rows of $A$ are primitive and its determinant has valuation $s$, there is a unit $u\in\mathcal O^\times$ such that the second row is congruent to $u$ times the first modulo $p^s$. Multiplication by $B$ gives


$$
(R_3,C_3)-u(R_0,C_0)\in p^{b+s}\mathcal O^2.
$$


If $e_0\ne e_3$, the content valuation of the left side is exactly $\min(e_0,e_3)$. Hence


$$
\min(e_0,e_3)\ge b+s.
$$


Together with the preceding upper bound, this proves (10.3).

For $s=0$, (10.2) already gives $\min(e_0,e_3)=b$, so (10.3) holds there as well.

If the endpoint depths differ, their smaller value is $b+s$, while their larger value is at most $d-b$. Therefore


$$
|e_0-e_3|\le d-2b-s.
$$


If they are equal, (10.4) is automatic.

Finally,


$$
v_p(\det(AB))=s+d.
$$


Each term in its determinant is divisible by $p^{e_0+e_3}$, giving


$$
e_0+e_3\le s+d.
$$


The separate upper bounds also give


$$
e_0+e_3\le2(d-b).
$$


Taking the smaller upper bound proves


$$
e_0+e_3
\le\min(s+d,2d-2b)
=d+\min(s,d-2b).
$$


∎

### Interpretation

This theorem treats the two types of obstruction together.

- **Away from $\Sigma_n$:**
  

$$
\min(e_0,e_3)=b,\qquad e_0+e_3\le d.
$$


  The common part is exactly the transverse source content, and the **product** is bounded by the shared residual.

- **On $\Sigma_n$:** unequal endpoint depths are possible only after both endpoints have reached depth $b+s$.

- If
  

$$
s\ge d-2b,
$$


  then
  

$$
e_0=e_3.
$$


  Such a prime contributes no endpoint-exclusive factor at all.

Thus increasing collision depth does not provide an unlimited independent source of exclusive cancellation. The available exclusive depth decreases by that collision depth.

## 11. Global consequences

Apply Theorem 10.1 at every $p>N$.

First,


$$
\mathcal B_n\mid g_n,\qquad
\Gamma_n=g_n/\mathcal B_n\mid\Sigma_n.
$$



The exponent of $p$ in $E_{0,n}E_{3,n}$ is $|e_0-e_3|$. Hence (10.4) gives


$$
\boxed{
E_{0,n}E_{3,n}
\mid
\frac{\mathcal A_n}{\gcd(\mathcal A_n,\Sigma_n)}.
}
\tag{11.1}
$$



If $p\mid E_{0,n}E_{3,n}$, equation (10.3) gives


$$
v_p(\Gamma_n)=v_p(\Sigma_n).
$$


Therefore


$$
\boxed{
\gcd\!\left(E_{0,n}E_{3,n},\frac{\Sigma_n}{\Gamma_n}\right)=1.
}
\tag{11.2}
$$



Finally, (10.5) proves


$$
\boxed{
\delta_0^{>}\delta_3^{>}
\mid
D_n^{>}\gcd(\Sigma_n,\mathcal A_n).
}
\tag{11.3}
$$



Using the closed polynomial projection comparisons,


$$
\boxed{
\mathfrak D_0\mathfrak D_3
\mid
\Pi_0(n)\Pi_3(n)\,
D_n^{>}\gcd(\Sigma_n,\mathcal A_n).
}
\tag{11.4}
$$



This is a product-content divisor theorem, not a common-content theorem.

## 12. An explicit mixed-product identity

The scalar determinant calculation also gives the integral identity


$$
\boxed{
R_0C_3-R_3C_0
=
\mp\frac{mN^2\det J}{2c_0c_3}\mathcal D_L,
}
\tag{12.1}
$$


with the sign determined by the primitive-row conventions.

The left side belongs to the product ideal. By itself, this identity pays all of $\Sigma_n$.

Theorem 10.1 improves that certificate to the clipped factor


$$
\gcd(\Sigma_n,\mathcal A_n).
$$


That improvement uses both facts that the observation rows are primitive and that the source matrix has exact content $\mathcal B_n$. It does not follow from the state-transfer determinant alone.

---

# V. Nonvanishing and the height of the complete scalar

A divisor of zero would not provide the requested nonzero product certificate. I therefore address nonvanishing explicitly.

The following real calculation is used only to establish the size and eventual nonvanishing of the **complete scalar $\Theta_n$**. It is not an estimate of a primitive whole approximation form.

## 13. A fixed-saddle estimate for the actual moments

Let


$$
f(z)=1+z+\frac{z^2}{2},\qquad
r=\sqrt2,\qquad c=1+\sqrt2,\qquad v=2-\sqrt2.
$$


Since


$$
a_j=j![z^j]e^zq(z)^n,
$$


the substitution $z\mapsto-z$ gives


$$
a_j=(-1)^j j![z^j]e^{-z}f(z)^n.
$$



At $z=r$,


$$
\frac{rf'(r)}{f(r)}=1,\qquad
r\frac{d}{dr}\left(\frac{rf'(r)}{f(r)}\right)=v>0,
$$


and


$$
\frac{f(r)}r=c.
$$



For each fixed integer $s$, coefficient extraction on $|z|=r$ gives


$$
[z^{n+s}]e^{-z}f(z)^n
=
\frac{f(r)^n r^{-(n+s)}}{2\pi}
\int_{-\pi}^{\pi}
e^{-re^{i\theta}}e^{-is\theta}
\left(
\frac{f(re^{i\theta})}{f(r)}e^{-i\theta}
\right)^n\,d\theta.
$$



Because $f$ has positive coefficients at the three consecutive degrees $0,1,2$, equality in


$$
|f(re^{i\theta})|\le f(r)
$$


occurs only at $\theta=0$ modulo $2\pi$. Thus the portion away from a fixed neighborhood of $0$ is exponentially smaller.

Near $0$,


$$
\log\left(
\frac{f(re^{i\theta})}{f(r)}e^{-i\theta}
\right)
=-\frac v2\theta^2+O(\theta^3).
$$


Gaussian scaling, with the odd terms canceling in the symmetric integral, yields


$$
\boxed{
[z^{n+s}]e^{-z}f(z)^n
=
\frac{e^{-r}f(r)^n r^{-(n+s)}}{\sqrt{2\pi nv}}
\left(1+O(n^{-1})\right).
}
\tag{13.1}
$$



Only $s=-1,0,1$ is needed here.

Set


$$
M_n=\frac{n!e^{-r}c^n}{\sqrt{2\pi nv}}>0.
$$


Since the original $n$ are odd,


$$
a_n=-M_n(1+O(n^{-1})),
$$




$$
a_{n-1}=\frac r nM_n(1+O(n^{-1})),
$$




$$
a_{n+1}=\frac m rM_n(1+O(n^{-1})).
$$



Consequently,


$$
X=-mM_n(1+O(n^{-1})),
$$




$$
Y=mrM_n(1+O(n^{-1})),
$$




$$
Z=mcM_n(1+O(n^{-1})),
$$


and, crucially,


$$
\boxed{
F=-2m^2ncM_n(1+O(n^{-1})).
}
\tag{13.2}
$$



Thus $F<0$ eventually, with a factorial-scale lower bound. This lower bound is the point missing from an argument based merely on $|F|\ge1$.

## 14. Dominance in the complete shared residual

The retained constant-term representation gives


$$
0<\tau_n\le c^n,\qquad
0<\tau_{n+1}\le c^{n+1}.
$$


Hence


$$
h\le n!c^n,\qquad \ell\le n!c^{n+1}.
$$



Using the moment estimates above,


$$
\frac{|mZ(Qh-P\ell)|}{|F\mathscr K_n|}
=
O\!\left(\frac{n^C c^{2n}}{n!}\right)
\longrightarrow0
$$


for a fixed constant $C$. Here the lower bound


$$
|\mathscr K_n|>(n!)^3
$$


is used exactly at its established original-index scope.

Therefore


$$
\mathcal D_L=-F\mathscr K_n(1+o(1)).
$$


Since eventually $F<0$ and $\mathscr K_n<0$,


$$
\boxed{\mathcal D_L<0,\qquad \Theta_n<0}
\tag{14.1}
$$


for all sufficiently large original indices.

No congruential exclusion is inferred from this dominance. It proves real nonvanishing only.

## 15. Size of the normalized complete scalar

Write


$$
\kappa_n=\frac{|\mathscr K_n|}{(n!)^3},
\qquad 1<\kappa_n<3.
$$


Equations (13.2)–(14.1) give


$$
|\Theta_n|
=
\kappa_n C_*
n^{5/2}(n!)^3(2+\sqrt2)^n
\left(1+O(n^{-1})\right),
$$


where


$$
C_*=
\frac{2\sqrt2(1+\sqrt2)e^{-\sqrt2}}
{\sqrt{2\pi(2-\sqrt2)}}>0.
$$


In particular,


$$
\boxed{
\log|\Theta_n|
=
3\log(n!)
+n\log(2+\sqrt2)
+\frac52\log n
+O(1).
}
\tag{15.1}
$$



Thus the nonzero product certificate is unconditional eventually. Its required exponential height is not proved.

## 16. A genuine reduction of the exclusive-content bound

Let


$$
U_n=\frac{|\Theta_n|}{D_n^{>}},
$$


the complete part supported on primes at most $N$.

From (11.1),


$$
\begin{aligned}
\log(E_{0,n}E_{3,n})
\le{}&
\log|\Theta_n|-\log U_n-2\log\mathcal B_n\\
&-\log\gcd(\mathcal A_n,\Sigma_n).
\end{aligned}
$$


Therefore


$$
\boxed{
\begin{aligned}
\log(E_{0,n}E_{3,n})
\le{}&
3\log(n!)+n\log(2+\sqrt2)+\frac52\log n+O(1)\\
&-\log U_n-2\log\mathcal B_n
-\log\gcd(\mathcal A_n,\Sigma_n).
\end{aligned}}
\tag{16.1}
$$



Even discarding the favorable subtractions gives


$$
\log(E_{0,n}E_{3,n})\le3\log(n!)+O(n).
$$



For comparison, separate contact-reference bounds have two quadratic moment cofactors. After removing the guaranteed reference factorial supported on small primes, each endpoint reference has size at most


$$
(n!)^2e^{O(n)}.
$$


Bounding the two exclusive factors independently therefore gives at best


$$
4\log(n!)+O(n).
$$


The shared complete scalar saves one factorial in that coarse comparison and, more substantively, imposes the exact collision restrictions (11.1)–(11.2).

It does not reduce the exclusive content to $O(n)$.

---

# VI. The remaining obstruction, now in a concrete scalar

## 17. What is still missing from the product certificate

The new certificate is


$$
\mathcal W_n=D_n^{>}\gcd(\Sigma_n,\mathcal A_n).
$$


Its logarithmic height is exactly


$$
\boxed{
\log\mathcal W_n
=
\log|\Theta_n|-\log U_n
+\log\gcd(\Sigma_n,\mathcal A_n).
}
\tag{17.1}
$$



The unresolved arithmetic is therefore not the construction of a nonzero element of the localized product ideal. Such an element has now been constructed.

The unresolved issue is its height, or that of a better product-ideal element.

In particular:

1. The real factorial term in $\Theta_n$ does not force its large-prime part to be small.
2. The upper bound for $\mathcal B_n$ controls only the first source invariant.
3. The second invariant
   

$$
\mathcal A_n=D_n^{>}/\mathcal B_n^2
$$


   can still carry large endpoint-exclusive content.
4. Collision cancellation is clipped to $\gcd(\Sigma_n,\mathcal A_n)$, but that clipped gcd has not been shown exponentially bounded.

This identifies why the present certificate is insufficient, without turning a finite gcd equal to $1$ into a support theorem.

## 18. A concrete follow-on lemma

A sufficient next lemma is:

> **Complete shared-scalar smoothness and clipped-collision lemma.**  
> On an infinite original subsequence, prove
> 

$$
> \log D_n^{>}
> +\log\gcd\!\left(
> \Sigma_n,\frac{D_n^{>}}{\mathcal B_n^2}
> \right)
> =o(n\log n),
>
$$


> or the stronger $O(n)$ estimate, for the explicitly normalized complete scalar
> 

$$
> \Theta_n
> =
> mZ(Q\widehat h-P\widehat\ell)
> -F\left[
> \widehat h\,b_{n+1}
> -\frac m2(\widehat h+\widehat\ell)b_n
> -2^{m/2+1}(n!)^2
> \right].
>
$$



This is a sufficient scalar statement with the fixed actual seed and complete logarithmic correction. It is not asserted to be necessary.

Using (15.1), a particularly transparent sufficient pair of estimates would be


$$
\log U_n\ge3\log(n!)-O(n),
$$


and


$$
\log\gcd(\Sigma_n,\mathcal A_n)=O(n).
$$


Neither has been proved. The first could fail for this particular scalar even if some other exponentially small product-ideal certificate exists.

No continued-fraction or homogeneous-companion shortcut is being imported.

---

# VII. Binary theorem and final normalization remain at their exact scope

## 19. Retained odd-exponent binary law

The Turn 8 binary proof remains a separate infinite-family assertion under independent review. Nothing in this turn changes its normalization.

On


$$
n=15^{2a+1},\qquad a\ge1,
$$


it uses:

- parameter period $16$;
- index period $32$;
- actual raw contact-row binary contents
  

$$
v_2(c_0)=5,\qquad v_2(c_3)=0;
$$


- the actual primitive projections
  

$$
v_2(\alpha_j)=1,\qquad v_2(\beta_j)=4;
$$


- restoration of the seed subtraction and complete logarithmic force.

Its stated conclusions are


$$
v_2(R_j)=\frac{n-1}{2}+4,
\qquad
v_2(r_j\mathbf U)=v_2(C_j)=5,
$$


and


$$
\boxed{
v_2(d_j)=v_2(n!)+\frac{n-3}{2}.
}
$$



The new product theorem does not depend on this binary law. No new denominator computation is requested to corroborate it.

## 20. All eight reconstruction entries and row contents

With the retained notation


$$
x=T^{-1}(n!t),\qquad y=T^{-1}\widehat w,
$$




$$
S=
\begin{pmatrix}
1&-n&n(n+1)\\
0&1&-2n\\
0&0&1
\end{pmatrix},
$$


write $sx=Sx$, $sy=Sy$.

The complete columns remain


$$
\boxed{
u=(-sx_0,\ sx_0-sx_1,\ sx_1-sx_2,\ sx_2),
}
$$




$$
\boxed{
v=(1-sy_0,\ sy_0-sy_1,\ sy_1-sy_2,\ sy_2).
}
$$


The exterior $+1$ remains in $v_0$.

The least clearer is taken over all eight entries. Each reconstructed row is divided by its actual two-entry content.

At $3375$, those accepted row contents remain


$$
\boxed{(113940000,\ 9780750,\ 10125,\ 1).}
$$


They are not replaced by contact-row contents, $\mathcal B_n$, $\Sigma_n$, or any selected-prime quantity.

## 21. Actual endpoint denominators

For


$$
\delta_j=\gcd(|R_j|,|C_j|),
\quad
R_j^*=R_j/\delta_j,\quad C_j^*=C_j/\delta_j,
$$


the retained all-prime identity is


$$
\boxed{
d_j=
|R_j^*|
\frac{n!}{\gcd(n!,|E_nR_j^*+C_j^*|)}.
}
\tag{21.1}
$$


Equivalently,


$$
d_j=
\frac{|n!R_j|}
{\gcd(|n!R_j|,\ |E_nR_j+C_j|)}.
$$



For every $p>n$,


$$
v_p(d_j)=\bigl(v_p(R_j)-v_p(C_j)\bigr)_+.
$$


The new large-prime product theorem is not a replacement for this actual denominator.

## 22. Final weighted gcd and whole same-index error

For a reduced weight $\lambda=a/k_{\rm wt}$, retain


$$
J_{\rm wt}
=B_{\rm wt}\widetilde v_0-A_{\rm wt}\widetilde v_3,
$$




$$
T_{\rm wt}
=aJ_{\rm wt}+k_{\rm wt}A_{\rm wt}\widetilde v_3,
$$




$$
F_{\rm gcd}
=
\gcd(|A_{\rm wt}|,|a|)
\gcd(|B_{\rm wt}|,|a-k_{\rm wt}|),
$$




$$
G_{\rm wt}=\gcd(k_{\rm wt},|J_{\rm wt}|),
$$




$$
H_{\rm gcd}
=
\gcd\!\left(
h_{\rm end},
\frac{|T_{\rm wt}|}{F_{\rm gcd}G_{\rm wt}}
\right),
\qquad
h_{\rm end}=\gcd(d_0,d_3).
$$



The actual primitive pair remains


$$
\boxed{
q_\lambda=
\frac{k_{\rm wt}h_{\rm end}|A_{\rm wt}B_{\rm wt}|}
{F_{\rm gcd}G_{\rm wt}H_{\rm gcd}},
}
$$




$$
\boxed{
p_\lambda=
\operatorname{sgn}(A_{\rm wt}B_{\rm wt})
\frac{T_{\rm wt}}{F_{\rm gcd}G_{\rm wt}H_{\rm gcd}}.
}
$$



Every prime remains in these gcds.

The whole error remains


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda e_3\alpha_{n,2}(\lambda-\Lambda_{n,2}).
}
\tag{22.1}
$$



The five accepted $3375$ whole forms are still finite evidence: they are nonzero and have absolute value greater than $1$. The saddle calculation in §13 concerns $\Theta_n$, not these whole forms. It neither proves an infinite sequence tending to zero nor supplies a uniform obstruction for a weight family.

---

# VIII. New bounded arithmetic and proof status

## 23. No accepted calculation should be repeated

The following are already complete or already assigned as separate archived-data checks:

- the four $3375$ endpoint equations;
- the twelve integral projection identities;
- the complete terminal normal identity;
- the complete $\mathscr K_n$ bounds;
- the actual $\delta_j^{>}$, normal-$F$, and $\mathfrak D_j$ gcds;
- the structural gcds;
- the old denominator computation;
- the whole-form enclosures;
- the newly assigned cross-product/saturation and binary corroborating fields.

I do not request any of them again.

## 24. Genuinely new optional scalar fields

No finite computation is needed for the proofs in this report.

A useful **new** archived-data postprocessing would assess the size of the newly constructed certificate, rather than repeat the actual endpoint gcd calculation.

### Inputs

- the already evaluated $\mathcal D_L=\mathcal D_{0,0}$;
- archived $n!,\tau_n,\tau_{n+1},b_n,b_{n+1},X,Y,Z$;
- the existing small-prime list through $3377$;
- $\Sigma_n$ from the separately assigned contact-index fields.

### New verifiable outputs

1. The integer $\Theta_n$, with the zero identity
   

$$
n!\Theta_n-2^{(n+1)/2}\mathcal D_L=0.
$$



2. Its exact factorization into the two specified parts
   

$$
|\Theta_n|=U_nD_n^{>},
$$


   where every prime factor of $U_n$ is at most $3377$, and
   

$$
\gcd\!\left(D_n^{>},\prod_{p\le3377}p\right)=1.
$$


   No factorization of $D_n^{>}$ is required.

3. The exact gcd
   

$$
\gcd(\Sigma_n,D_n^{>}).
$$



4. The corresponding certificate
   

$$
\mathcal W_n=D_n^{>}\gcd(\Sigma_n,D_n^{>}),
$$


   and the exclusive upper divisor
   

$$
\frac{D_n^{>}}{\gcd(\Sigma_n,D_n^{>})}.
$$



At $3375$, the new theorem and the already accepted $g_n=1$ imply


$$
\mathcal B_n=1.
$$


Thus the displayed simplifications in items 3–4 are theorem consequences, not a request to recompute the old endpoint gcds.

The numerical sizes of these new scalar fields are not supplied here. Their purpose would be to reveal whether this particular certificate is arithmetically economical or very loose at the retained finite index. Either outcome would remain finite.

## 25. Status ledger

| Statement | Status |
|---|---|
| Completed $3375$ moment-reference receipt | Accepted finite corroboration after source assessment |
| Both $3375$ $\delta_j^{>}$ and $\mathfrak D_j$ equal $1$ | Finite fact |
| Universal no-large-primes claim | Not made |
| Exact transverse source content, Lemma 7.1 | **New proof** |
| Complete determinant identity (8.1) | **New proof** |
| Unequal-depth rigidity $\min(e_0,e_3)=b+s$ | **New proof** |
| Exclusive divisor (11.1) and support restriction (11.2) | **New proof** |
| Product divisor with clipped collision loss (11.3) | **New proof** |
| Nonzero localized product certificate eventually | **New unconditional result** |
| Eventual nonvanishing and size of $\Theta_n$ | **New saddle derivation using the complete retained $\mathscr K_n$ bounds** |
| Exclusive-content bound $3\log(n!)+O(n)$ | **New bound; insufficient for the primary target** |
| Exponential-height product-ideal element | Not proved |
| $O(n)$ or $o(n\log n)$ bound for $\log(\mathfrak D_0\mathfrak D_3)$ | Open |
| Infinite nonzero whole forms tending to zero | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

---

# Conclusion

This turn constructs and proves a new product-ideal certificate, rather than further bounding only the common ideal.

For the actual complete shared residual,


$$
\Theta_n
=
\frac{2^{(n+1)/2}}{n!}
\left[mZ(Qh-P\ell)-F\mathscr K_n\right],
$$


the actual large-prime endpoint product satisfies


$$
\boxed{
\delta_0^{>}\delta_3^{>}
\mid
D_n^{>}
\gcd\!\left(
\Sigma_n,\frac{D_n^{>}}{\mathcal B_n^2}
\right).
}
$$



The two disjoint exclusive factors satisfy the sharper restriction


$$
\boxed{
E_{0,n}E_{3,n}
\mid
\frac{D_n^{>}/\mathcal B_n^2}
{\gcd(D_n^{>}/\mathcal B_n^2,\Sigma_n)}.
}
$$


At an exclusive prime, the common endpoint depth must equal the source depth plus the **full** collision depth. This explicitly couples exclusivity and cancellation on $\Sigma_n$.

The scalar is nonzero for all sufficiently large original indices, but its unreduced height is


$$
3\log(n!)+n\log(2+\sqrt2)+O(\log n).
$$


The exact remaining arithmetic bottleneck is to control its actual large-prime part and the clipped collision gcd—or construct a better nonzero product-ideal element—at $O(n)$ or $o(n\log n)$ height.

Even that arithmetic advance would still have to be combined with every factor in the final weighted gcd and with the whole nonzero same-index error.



$$
\boxed{\text{No unconditional proof or disproof of the irrationality of }e+\pi
\text{ has been obtained.}}
$$


