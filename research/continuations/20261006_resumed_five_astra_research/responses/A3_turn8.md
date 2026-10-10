> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3, Turn 8 — A saturated joint endpoint bound, its exact contact-lattice obstruction, and the remaining $15^{2a+1}$ binary law

## Executive conclusions

The irrationality or rationality of $e+\pi$ remains unresolved.

This turn makes two advances of different strengths.

### 1. A new joint endpoint theorem isolates the exact contact-lattice saturation factor

Write


$$
\delta_j^{>}=\gcd(R_j,C_j)_{>n+2},\qquad
g_n=\gcd(\delta_0^{>},\delta_3^{>}).
$$


Let $r_0,r_3$ be the **actual primitive contact rows**, and define


$$
\sigma_n=\gcd\bigl(\text{the three coordinates of }r_0\times r_3\bigr),
\qquad
\Sigma_n=(\sigma_n)_{>n+2}.
$$



The new theorem is


$$
\boxed{
\frac{g_n}{\gcd(g_n,\Sigma_n)}
\ \mid\
\gcd\!\left(\ell,Z,Y-2X,\mathscr K_n\right)_{>n+2}.
}
\tag{E1}
$$


Here all quantities are the actual recurrence-generated quantities:


$$
X=(n+1)a_n,\qquad Y=n(n+1)a_{n-1},\qquad
Z=2a_{n+1}-(n+1)a_n,
$$




$$
\ell=n!\tau_{n+1},
$$


and


$$
\mathscr K_n
=h_nb_{n+1}-h_{n+1}b_n-2(n!)^3.
$$



In particular, if


$$
T_{n+1}=2^{(n+1)/2}\tau_{n+1}\in\mathbb Z,
$$


then


$$
\boxed{
\frac{g_n}{\gcd(g_n,\Sigma_n)}
\mid (T_{n+1})_{>n+2},
\qquad
\log\frac{g_n}{\gcd(g_n,\Sigma_n)}
\le (n+1)\log(2+\sqrt2).
}
\tag{E2}
$$



Thus the **joint cancellation remaining after the exact contact-lattice saturation cost has been removed** has an unconditional $O(n)$ bound.

The saturation factor is not an unspecified ambient determinant. If


$$
\mathscr R_0=(-1,n,-n(n+1))\operatorname{adj}(J),\qquad
\mathscr R_3=(0,0,1)\operatorname{adj}(J),
$$


and $c_j$ is the actual three-coordinate content of $\mathscr R_j$, then


$$
\boxed{
\sigma_n=
\frac{|\det J|\,
       \operatorname{cont}(nJ_0+J_1)}
     {c_0c_3}.
}
\tag{E3}
$$


Moreover,


$$
\operatorname{cont}(nJ_0+J_1)_{>n+2}=1,
$$


so its large-prime valuation is exactly


$$
\boxed{
v_p(\Sigma_n)=v_p(\det J)-v_p(c_0)-v_p(c_3),
\qquad p>n+2.
}
\tag{E4}
$$



This is a genuine coupled-endpoint result, not an equivalent restatement of the separate $\mathfrak D_j$. It does **not**, however, prove the primary requested estimate for
$\log(\mathfrak D_0\mathfrak D_3)$. Two obstructions remain:

- cancellation supported on the actual contact-lattice collision factor $\Sigma_n$;
- large, prime-disjoint cancellation at the two endpoints.

An exponential reference-height bound controls neither obstruction by itself.

### 2. The requested remaining binary class is completed

On the original subfamily


$$
\boxed{n=15^{2a+1},\qquad a\ge1,}
$$


put


$$
t=v_2(n!),\qquad k=\frac{n-1}{2}.
$$


Then $n\equiv15\pmod{32}$ and $v_2(n+1)=4$. I prove


$$
\boxed{
v_2(G_0)=v_2(G_3)=1,
\qquad
v_2(R_0)=v_2(R_3)=k+4,
}
\tag{E5}
$$


and, for the complete exterior-corrected exponential force,


$$
\boxed{
v_2(r_0\mathbf U)=v_2(r_3\mathbf U)=5.
}
\tag{E6}
$$


After restoring the seed subtraction and the complete logarithmic force,


$$
\boxed{
v_2(C_0)=v_2(C_3)=5.
}
\tag{E7}
$$


Consequently, for the actual primitive endpoint denominators,


$$
\boxed{
v_2(d_0)=v_2(d_3)=t+k-1
=v_2(n!)+\frac{n-3}{2}.
}
\tag{E8}
$$



The endpoint-$3$ statement strengthens A4’s retained lower bound
$v_2(r_3\mathbf U)\ge5$ to an exact law on this subfamily. It is proved below, not inferred from that lower bound.

No program was executed. The announced new $3375$ identity/gcd postprocessing has not been received, and no new $\mathfrak D_j$, structural gcd, or projected gcd value is asserted.

---

# I. Scope and source assessment

## 1. Original construction and retained results

The index domain remains


$$
n=15^r,\quad r\ge2,
\qquad\text{or}\qquad
n=105^r,\quad r\ge2.
$$



Nothing below changes:

- the original $3\times3$ contact matrix;
- either corrected four-coordinate reconstruction column;
- the forcing cutoff $2n+2$;
- the complete terminal return;
- the exterior $+1$;
- the least clearer over all eight reconstructed entries;
- any actual reconstruction row content;
- the all-prime final weighted gcd;
- the actual primitive denominator;
- the whole error at the same original index.

I reuse Turn 7’s four endpoint equations, integral residual identities, exact local projection law, and polynomial projection losses


$$
\Pi_3=n^2+4n+1,\qquad
\Pi_0=n^2+6n+4.
$$


Their independent A4 review and the newly planned finite identity corroboration remain separate from their symbolic derivations. I do not attribute either to an executed program.

The retained comparison is


$$
\boxed{
\delta_j^{>}\mid\mathfrak D_j\mid\Pi_j\delta_j^{>}.
}
\tag{1.1}
$$


I do not rederive these polynomial losses as the main advance.

The relevant A4 Turn 10 conclusions are its retained all-prime denominator identity and its endpoint-$3$ binary force improvement. Its other weighted, quartic, and $29$-adic constructions have different domains and normalizations; their valuation conclusions are not imported here.

## 2. Actual residual and forcing constants

Throughout,


$$
m=n+1,\qquad N=n+2,
$$




$$
h=h_n=n!\tau_n,\qquad \ell=n!\tau_{n+1}.
$$



The actual terminal columns satisfy


$$
\mathbf H=\frac m2(hv'+\ell w'),
$$




$$
\mathbf C=S_nv'+T_nw'+mZe_2,
$$


where


$$
v'=(2N,N,m)^T,\qquad
w'=(0,N,2n+3)^T,
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
\tag{2.1}
$$



The fixed exponential/exterior seed remains


$$
(h_0,h_1,h_2)=(1,1,n+2),
$$




$$
(b_0,b_1,b_2)=(-1,n,n+2-n^2).
$$


In particular, $b_0=-1$ is retained.

The inhomogeneous Wronskian is the one generated by Turn 6’s recurrence with complete forcing


$$
\begin{aligned}
F_k={}&(n+1)a_k-nk\,a_{k-1}\\
&+\frac{(n-1)k(k-1)}2a_{k-2}
+\frac{k(k-1)(k-2)}2a_{k-3},
\end{aligned}
$$


and initial exterior coordinates


$$
w_{1,2}=2-n-2n^2,\qquad
w_{2,2}=2n+4-n^2,\qquad
w_{3,2}=n+1.
$$


At the original odd indices,


$$
\boxed{
\mathscr K_n=w_{1,n+1}-2(n!)^3.
}
\tag{2.2}
$$



Thus the new joint theorem below concerns the actual moment/reference/inhomogeneous-Wronskian residual. It is not an invariant of a freely chosen ambient state.

---

# II. The shared endpoint column and its exact saturation factor

## 3. A common kernel column

Both endpoint rows annihilate


$$
\boxed{L=nJ_0+J_1.}
\tag{3.1}
$$


Indeed, $r_3$ annihilates $J_0,J_1$, while $L$ is one of the two endpoint-$0$ kernel columns.

Turn 7’s endpoint equation for $L$ has coefficients


$$
P=nX+Y,
$$




$$
Q=nZ+2X-Y,
$$




$$
F=2m\bigl(Y-2X-(n-1)Z\bigr).
$$


Equivalently, as an identity of actual columns,


$$
\boxed{
L=\frac12\bigl(Pv'+Qw'+Fe_2\bigr).
}
\tag{3.2}
$$



This column identity follows from the retained row-coordinate identity, not from inversion of $J$.

## 4. Large-prime primitivity of the shared column

### Lemma 4.1

For every $p>n+2$,


$$
\boxed{\operatorname{cont}(L)_p=1.}
\tag{4.1}
$$



### Proof

At this scope, the change of coordinates with columns $v',w',e_2$ is invertible over $\mathbb Z_p$: its determinant is $2N^2$.

Thus $L\equiv0\pmod p$ would imply


$$
P\equiv Q\equiv F\equiv0\pmod p.
$$


Since $2m$ is a unit, this means


$$
nX+Y=0,
$$




$$
2X-Y+nZ=0,
$$




$$
-2X+Y-(n-1)Z=0
\pmod p.
$$


Adding the last two equations gives $Z=0$. The first two then give


$$
NX=0,\qquad Y=0.
$$


Hence $X=Y=Z=0\pmod p$, contrary to the retained terminal moment primitivity.

More explicitly, the linear map


$$
(X,Y,Z)\longmapsto
\left(P,Q,\frac{F}{2m}\right)
$$


has determinant $-N$, a unit at the stated scope. ∎

This is useful because it removes any additional large-prime content cost from the common kernel column itself.

## 5. Exact boundary determinant

Let


$$
\mathscr R_0=(-1,n,-nm)\operatorname{adj}(J),\qquad
\mathscr R_3=(0,0,1)\operatorname{adj}(J),
$$


and let


$$
c_j=\operatorname{cont}(\mathscr R_j)>0.
$$


Up to the harmless signs chosen for primitive rows,


$$
r_j=\mathscr R_j/c_j.
$$



The cross-product transformation law gives


$$
\mathscr R_0\times\mathscr R_3
=
\det(J)\,L.
$$


Indeed,


$$
(-1,n,-nm)\times(0,0,1)=(n,1,0).
$$



Therefore


$$
\boxed{
r_0\times r_3
=
\pm\frac{\det J}{c_0c_3}\,L.
}
\tag{5.1}
$$


Taking the contents of both sides gives


$$
\boxed{
\sigma_n
=
\frac{|\det J|\,\operatorname{cont}(L)}{c_0c_3}.
}
\tag{5.2}
$$



This is an integer because it is the content of an actual integral cross product.

For $p>n+2$, Lemma 4.1 gives


$$
\boxed{
v_p(\sigma_n)
=v_p(\det J)-v_p(c_0)-v_p(c_3).
}
\tag{5.3}
$$



The $c_j$ here are contents of the raw **contact rows**. They are not the four reconstruction row contents, which remain unchanged.

### Interpretation

The two-row matrix


$$
\mathcal R=
\begin{pmatrix}
r_0\\ r_3
\end{pmatrix}
$$


has Smith invariants


$$
1,\ \sigma_n.
$$


The first invariant is $1$ because either primitive row already has coordinate content $1$. The second is the gcd of the $2\times2$ minors, namely $\sigma_n$.

Thus $\sigma_n$ is the exact lattice index that must be paid when passing from two projected endpoint equations to their common kernel line. Full-state invertibility does not remove it.

---

# III. A saturated joint cancellation theorem

## 6. The local theorem

Fix $p>n+2$, and put


$$
e=\min\{v_p(R_0),v_p(R_3),v_p(C_0),v_p(C_3)\},
$$




$$
s=v_p(\sigma_n).
$$



### Theorem 6.1

One has


$$
\boxed{
(e-s)_+
\le
\min\{v_p(\ell),v_p(Z),v_p(Y-2X),v_p(\mathscr K_n)\}.
}
\tag{6.1}
$$



### Proof

There is nothing to prove when $e\le s$. Suppose $d=e-s>0$.

Because $L$ is primitive over $\mathbb Z_p$, extend it to a $\mathbb Z_p$-basis of $\mathbb Z_p^3$. In that basis, the endpoint row matrix has the form


$$
\mathcal R=(A\ \ 0),
$$


where $A$ is a $2\times2$ matrix with determinant valuation $s$.

If a column $V$ satisfies


$$
r_0V,\ r_3V\in p^e\mathbb Z_p,
$$


the adjugate formula for $A^{-1}$ shows that its two coordinates transverse to $L$ lie in $p^{e-s}\mathbb Z_p$. Consequently,


$$
V\equiv \lambda L\pmod{p^d}
$$


for some $\lambda\in\mathbb Z_p$.

Apply this separately to $\mathbf H$ and $\mathbf C$:


$$
\mathbf H\equiv\lambda L\pmod{p^d},
\qquad
\mathbf C\equiv\mu L\pmod{p^d}.
\tag{6.2}
$$



The reference column $\mathbf H$ is primitive over $\mathbb Z_p$. This follows from the retained companion-Wronskian unit ideal


$$
(h,\ell)=\mathbb Z_p
$$


and the unit coordinate transformations. Hence $\lambda$ is a unit.

Now compare the $e_2$-coordinates in the basis $v',w',e_2$.

The reference column has zero $e_2$-coordinate, whereas $L$ has coordinate $F/2$. Therefore


$$
\lambda F/2\equiv0\pmod{p^d},
$$


and thus


$$
F\equiv0\pmod{p^d}.
\tag{6.3}
$$



The complete residual has $e_2$-coordinate $mZ$. Using the second congruence in (6.2) and (6.3),


$$
mZ\equiv\mu F/2\equiv0\pmod{p^d}.
$$


Thus


$$
Z\equiv0\pmod{p^d}.
\tag{6.4}
$$



Since


$$
F=2m\bigl(Y-2X-(n-1)Z\bigr),
$$


we also obtain


$$
Y-2X\equiv0\pmod{p^d}.
\tag{6.5}
$$



It follows that


$$
Q=nZ+2X-Y\equiv0\pmod{p^d}.
$$


The $w'$-coordinate of the first congruence in (6.2) now gives


$$
\frac m2\ell\equiv \frac{\lambda Q}{2}\equiv0\pmod{p^d}.
$$


Hence


$$
\ell\equiv0\pmod{p^d}.
\tag{6.6}
$$



Finally, (6.2) implies


$$
\mathbf H\wedge\mathbf C\equiv0\pmod{p^d}.
$$


Its $v'\wedge w'$-coordinate is


$$
\frac m2(hT_n-\ell S_n)=\frac m2\mathscr K_n.
$$


Therefore


$$
\mathscr K_n\equiv0\pmod{p^d}.
\tag{6.7}
$$



Equations (6.4)–(6.7) prove the theorem. ∎

### What the proof uses

The proof specifically uses:

- both actual endpoint rows;
- their common **actual** moment column $L$;
- the actual primitive row contents through $\sigma_n$;
- the complete terminal residual normal coordinate $mZ$;
- the complete Wronskian $hT_n-\ell S_n=\mathscr K_n$.

It does not infer projected primitivity from an invertible full-state transfer. It also does not invoke the real dominance of $-2(n!)^3$.

## 7. Global arithmetic consequence

Define


$$
\mathcal B_n
=
\gcd(\ell,Z,Y-2X,\mathscr K_n)_{>n+2}.
$$


Theorem 6.1 gives


$$
\boxed{
\frac{g_n}{\gcd(g_n,\Sigma_n)}\mid\mathcal B_n.
}
\tag{7.1}
$$



Since $n+1$ is even,


$$
T_{n+1}=2^{(n+1)/2}\tau_{n+1}
$$


is an integer. At primes $p>n+2$, the factors $2$ and $n!$ are units, so


$$
v_p(\ell)=v_p(T_{n+1}).
$$


Thus


$$
\mathcal B_n\mid(T_{n+1})_{>n+2}.
$$



The constant-term representation gives


$$
0<\tau_{n+1}\le(1+\sqrt2)^{n+1}.
$$


Consequently,


$$
0<T_{n+1}\le(2+\sqrt2)^{n+1}.
$$


We have proved


$$
\boxed{
\log\frac{g_n}{\gcd(g_n,\Sigma_n)}
\le(n+1)\log(2+\sqrt2).
}
\tag{7.2}
$$



This is an unconditional $O(n)$ bound for a specified saturated part of the actual joint cancellation.

### Consequence for the Turn 7 contents

Let


$$
H_{\mathfrak D}=\gcd(\mathfrak D_0,\mathfrak D_3).
$$


Using the already established polynomial comparisons, one obtains


$$
H_{\mathfrak D}
\mid
\Pi_0\Pi_3\,\Sigma_n\,\mathcal B_n.
$$


In particular,


$$
\boxed{
\frac{H_{\mathfrak D}}
{\gcd(H_{\mathfrak D},\,\Pi_0\Pi_3\Sigma_n)}
\mid(T_{n+1})_{>n+2}.
}
\tag{7.3}
$$



No new claim about the numerical values of these gcds at $3375$ follows before the planned postprocessing is received.

---

# IV. What this does and does not resolve about the primary target

## 8. The exact additional factor beyond reference height

The reference-height argument now has an explicit arithmetic cost:


$$
\boxed{
\Sigma_n=
\left(
\frac{|\det J|\,\operatorname{cont}(nJ_0+J_1)}
     {c_0c_3}
\right)_{>n+2}.
}
\tag{8.1}
$$



It is the collision index of the two actual primitive endpoint rows. It is not a coefficient-height surrogate or an arbitrary ambient determinant.

At a prime not dividing $\Sigma_n T_{n+1}$, simultaneous endpoint cancellation is impossible:


$$
\boxed{
p>n+2,\quad p\nmid\Sigma_nT_{n+1}
\ \Longrightarrow\
\min\{v_p(\delta_0^{>}),v_p(\delta_3^{>})\}=0.
}
\tag{8.2}
$$



But this does not control cancellation at only one endpoint.

To make that distinction exact, write


$$
\delta_0^{>}=g_n E_{0,n},\qquad
\delta_3^{>}=g_n E_{3,n},
$$


where


$$
\gcd(E_{0,n},E_{3,n})=1.
$$


Also put


$$
g_{\mathrm{coll},n}=\gcd(g_n,\Sigma_n),\qquad
g_{\mathrm{sat},n}=g_n/g_{\mathrm{coll},n}.
$$


Then


$$
\boxed{
\delta_0^{>}\delta_3^{>}
=
g_{\mathrm{coll},n}^{\,2}
g_{\mathrm{sat},n}^{\,2}
E_{0,n}E_{3,n},
}
\tag{8.3}
$$


and the newly controlled factor is


$$
g_{\mathrm{sat},n}\mid\mathcal B_n,
\qquad
\log g_{\mathrm{sat},n}=O(n).
$$



Therefore


$$
\boxed{
\log(\mathfrak D_0\mathfrak D_3)
\le
2\log g_{\mathrm{coll},n}
+\log(E_{0,n}E_{3,n})
+2(n+1)\log(2+\sqrt2)
+O(\log n).
}
\tag{8.4}
$$



The remaining arithmetic factors are now explicitly separated:

1. the part of simultaneous cancellation lying on the actual contact-row collision index;
2. the two coprime endpoint-exclusive cancellation factors.

Neither has been proved $O(n)$ or $o(n\log n)$.

## 9. Why a propagated full-state determinant still does not finish the argument

The retained moment/reference/Wronskian recurrences have explicitly known seeds and forcing. Their full-state transfer can be analyzed primewise.

That does not establish saturation of the two endpoint observations. At the boundary, the relevant observation matrix is the actual two-row matrix $\mathcal R$, whose second Smith invariant is $\sigma_n$, not $1$. Even after that cost is paid, a theorem about **common** endpoint content says nothing quantitative about two large coprime exclusive contents.

Likewise,


$$
\mathscr K_n=-2(n!)^3+w_{1,n+1}
$$


with


$$
|w_{1,n+1}|<(n!)^3
$$


does not exclude


$$
\mathscr K_n\equiv0\pmod{p^a}.
$$


Theorem 6.1 uses $\mathscr K_n$ as an actual congruence constraint; it does not treat the factorial term as protected against cancellation.

### Concrete follow-on lemma

A sufficient next arithmetic lemma, now with the boundary saturation cost explicitly identified, is:

> **Contact-collision and one-sided residual lemma.**  
> On an infinite original subsequence, prove
> 

$$
> 2\log\gcd(g_n,\Sigma_n)
> +\log(E_{0,n}E_{3,n})
> =o(n\log n),
>
$$


> or the stronger $O(n)$ estimate, using the actual residuals
> 

$$
> \mathcal D_{j,i}
> =mZ(Q_{j,i}h-P_{j,i}\ell)-F_{j,i}\mathscr K_n
>
$$


> and their fixed complete recurrence data.

For a controlled-prime Bézout approach, the required object is an exponentially small nonzero element of the **product of the actual endpoint ideals**


$$
(R_0,C_0)(R_3,C_3)
$$


after localization only at primes at most $n+2$. A certificate involving only the intersection or sum of these ideals would control common cancellation, not the required product.

This distinction is the precise obstruction to upgrading the new joint theorem to the primary target. I do not claim that such a Bézout certificate has been constructed.

---

# V. The remaining binary class $n=15^{2a+1}$

## 10. Scope and notation

Assume


$$
n=15^{2a+1},\qquad a\ge1.
$$


Then


$$
n\equiv15\pmod{32},\qquad
m=n+1=16u,\quad u\ \text{odd},
$$


and


$$
N=n+2\equiv1\pmod{16}.
$$



Put


$$
t=v_2(n!),\qquad k=\frac{n-1}{2}.
$$


Then


$$
k\equiv7\pmod{16},\qquad v_2(k+1)=3.
$$



Write


$$
A=a_n,\quad B=a_{n-1},\quad C=a_{n-2},\quad
D=a_{n+1},\quad E=a_{n+2}.
$$



The calculation below pays the actual primitive-row divisions. It does not reduce an unnormalized reference pair and then silently treat it as primitive.

## 11. Correct parameter and index reduction

Let


$$
c_i(n)=i![z^i]q(z)^n,\qquad q(z)=1-z+\frac{z^2}{2}.
$$


The explicit formula


$$
c_i(n)
=
\sum_{b=0}^{\lfloor i/2\rfloor}
(-1)^{i-2b}
\frac{i!}{(i-2b)!\,b!\,2^b}(n)_{i-b}
$$


shows that


$$
c_i(n)\in\mathbb Z[n].
$$


The coefficient multiplying $(n)_{i-b}$ is an integer.

Also,


$$
v_2(c_i(n))
\ge v_2(i!)-\lfloor i/2\rfloor.
\tag{11.1}
$$



The moment expansion is


$$
a_j(n)=\sum_{i=0}^j\binom ji c_i(n).
$$


Modulo $16$, terms with $i\ge12$ vanish. For $1\le i\le11$, Vandermonde’s identity and


$$
v_2\binom{32}{r}=5-v_2(r)
$$


show that the change $j\mapsto j+32$, after multiplication by $c_i(n)$, is divisible by $16$.

Thus the valid reductions here are:

- parameter period $16$;
- index period $32$.

Since $n\equiv-1\pmod{16}$, the parameter reduces to $-1$, not to $15$ with an assumed shorter index period.

For parameter $-1$,


$$
\sum_{j\ge0}a_j(-1)\frac{z^j}{j!}=\frac{e^z}{q(z)},
$$


so


$$
\boxed{
a_j(-1)-j\,a_{j-1}(-1)
+\frac{j(j-1)}2a_{j-2}(-1)=1,
}
\tag{11.2}
$$


with $a_0(-1)=1,a_1(-1)=2$.

Using (11.2) modulo $16$ gives


$$
a_{13}(-1)=0,\quad
a_{14}(-1)=10,\quad
a_{15}(-1)=7,\quad
a_{16}(-1)=1,\quad
a_{17}(-1)=10
\pmod{16}.
$$


Therefore


$$
\boxed{
(C,B,A,D,E)\equiv(0,10,7,1,10)\pmod{16}.
}
\tag{11.3}
$$



These are short symbolic modular calculations, not reported program outputs.

---

## 12. Actual primitive endpoint-$0$ row

Retain Turn 7’s evaluated expansion


$$
\mathscr R_0=mN(X_0,Y_0,Z_0),
$$


where


$$
\begin{aligned}
X_0={}&-mNA^2+nNBD+n^2BE-nNAD-nND^2+nmAE,\\
Y_0={}&n\bigl(-(n-1)NCD+mNAB+mNA^2\\
&\hspace{19mm}-n(n-1)CE-nmBE+mNAD\bigr),\\
Z_0={}&nN\bigl(-nmB^2+(n-1)mAC+n(n-1)CD\\
&\hspace{19mm}-nmAB-m^2A^2+nmBD\bigr).
\end{aligned}
$$


Substituting (11.3) yields


$$
\boxed{(X_0,Y_0,Z_0)\equiv(2,0,0)\pmod{16}.}
\tag{12.1}
$$



Hence:

- $\operatorname{cont}(X_0,Y_0,Z_0)$ has binary valuation exactly $1$;
- the raw contact row $\mathscr R_0$ has binary content exactly $5$;
- the actual primitive row $r_0=(x_0,y_0,z_0)$ satisfies
  

$$
\boxed{x_0\ \text{odd},\qquad y_0,z_0\in8\mathbb Z.}
  \tag{12.2}
$$



All additional divisions are by odd integers.

Set


$$
\alpha_0=r_0v',\qquad \beta_0=r_0w'.
$$


Equation (12.2) gives


$$
\boxed{v_2(\alpha_0)=1.}
\tag{12.3}
$$



To evaluate $\beta_0$, use the actual endpoint equation for $L$:


$$
P\alpha_0+Q\beta_0+Fz_0=0.
$$


Here


$$
P=mn(A+B),
$$




$$
Q=2nD+m(2-n)A-mnB,
$$




$$
F=2m\bigl(mnB+m(n-3)A-2(n-1)D\bigr).
$$


From (11.3),


$$
v_2(P)=4,\qquad v_2(Q)=1,\qquad v_2(F)=7.
$$


Since $v_2(\alpha_0)=1$ and $v_2(z_0)\ge3$,


$$
v_2(P\alpha_0)=5,\qquad v_2(Fz_0)\ge10.
$$


The endpoint equation therefore forces


$$
\boxed{v_2(\beta_0)=4.}
\tag{12.4}
$$


Thus


$$
\boxed{v_2(G_0)=1.}
\tag{12.5}
$$



### A normalized congruence needed for the force

Put


$$
a_0^\flat=\alpha_0/2,\qquad b_0^\flat=\beta_0/16.
$$


Both are odd.

Divide the endpoint equation by $32$ and reduce modulo $4$. Since


$$
Q/2\equiv nD\pmod4,
$$


one obtains


$$
un(A+B)a_0^\flat+nD\,b_0^\flat\equiv0\pmod4.
$$


Now $A+B\equiv1\pmod4$ and $D\equiv1\pmod4$, so


$$
\boxed{
b_0^\flat\equiv-u\,a_0^\flat\pmod4.
}
\tag{12.6}
$$



This congruence is for the actual primitive row. Its derivation has paid the factor $2^5$ in the raw row content.

---

## 13. Actual primitive endpoint-$3$ row

The retained raw row is


$$
\mathscr R_3=
\left(
N^2D^2-mNAE,\;
m(nNBE-N^2AD),\;
mN^2(mA^2-nBD)
\right).
$$


Its first coordinate is odd. Therefore its binary content is zero, and passage to $r_3$ divides only by an odd integer.

The second and third coordinates have valuations exactly $4$ and $5$, respectively. It follows that


$$
v_2(\alpha_3)=1,\qquad v_2(\beta_3)=4,
$$


and hence


$$
\boxed{v_2(G_3)=1.}
\tag{13.1}
$$



More precisely, if the odd primitive-row division is denoted by $g$, including a possible sign, then modulo $4$,


$$
\frac{\alpha_3}{2}\equiv g^{-1},
$$


while


$$
\frac{\beta_3}{16}
\equiv 3u\,g^{-1}
\equiv-u\,g^{-1}.
$$


Thus, with


$$
a_3^\flat=\alpha_3/2,\qquad b_3^\flat=\beta_3/16,
$$


we again have


$$
\boxed{
b_3^\flat\equiv-u\,a_3^\flat\pmod4.
}
\tag{13.2}
$$



No even primitive-row division has been omitted.

---

# VI. Exact reference depths

## 14. The even reference value is exact; the odd one only needs a lower bound

For the odd index $n=2k+1$, relative to the terminal summand in the constant-term formula for $\tau_n$, the $r$-th preceding summand has ratio


$$
\frac{2^r(k)_r^2}{(2r+1)!}.
$$


The terminal summand has valuation


$$
-v_2(k!).
$$


For $r=1$, the ratio is $k^2/3$, which is odd. Hence the first two summands combine to an even multiple of the terminal summand.

For $r\ge2$,


$$
v_2\!\left(\frac{2^r(k)_r^2}{(2r+1)!}\right)
\ge r-s_2(r)\ge1.
$$


Therefore


$$
\boxed{v_2(\tau_n)\ge-v_2(k!)+1.}
\tag{14.1}
$$


This is a lower bound, not an asserted exact valuation.

For the even index $n+1=2(k+1)$, put $a=k+1$. Here $a$ is even and $v_2(a)=3$. The terminal summand has valuation


$$
-v_2(a!).
$$


Its relative $r=1$ correction has valuation $2v_2(a)=6$, and every correction with $r\ge2$ has valuation at least $1$. Hence the terminal summand is uniquely of lowest valuation:


$$
\boxed{
v_2(\tau_{n+1})=-v_2((k+1)!)
=-v_2(k!)-3.
}
\tag{14.2}
$$



Since


$$
t-v_2(k!)=k,
$$


these imply


$$
v_2(h)\ge k+1,\qquad
\boxed{v_2(\ell)=k-3.}
\tag{14.3}
$$



At both endpoints,


$$
v_2(\alpha_j)=1,\qquad v_2(\beta_j)=4.
$$


Thus


$$
v_2(h\alpha_j)\ge k+2,
\qquad
v_2(\ell\beta_j)=k+1.
$$


The second term is uniquely of lower valuation, so


$$
v_2(h\alpha_j+\ell\beta_j)=k+1.
$$



Using


$$
R_j=\frac m2(h\alpha_j+\ell\beta_j),
$$


we conclude


$$
\boxed{
v_2(R_0)=v_2(R_3)=k+4.
}
\tag{14.4}
$$



Equivalently, for the primitive reference combinations


$$
\xi_j=(\alpha_j/G_j)\tau_n+(\beta_j/G_j)\tau_{n+1},
$$




$$
\boxed{v_2(\xi_0)=v_2(\xi_3)=-v_2(k!).}
\tag{14.5}
$$



No exact valuation of the odd $\tau_n$ beyond (14.1) is needed.

---

# VII. Exact complete force valuation

## 15. A guarded reduction of the actual exponential force

The retained exact force identity can be rewritten as


$$
\boxed{
\Omega_n(z)
=q(z)^n\frac{d^n}{dz^n}\left(\frac{e^z}{1-z}\right).
}
\tag{15.1}
$$


Indeed, the elementary antiderivative used in
$\Omega_n=\mathscr H_n(E_n+I_n)$ gives


$$
E_n+I_n(z)
=e^z\sum_{r=0}^n(n)_r(1-z)^{n-r},
$$


which is exactly (15.1) after Leibniz expansion.

Therefore the actual factorial-normalized force coefficient satisfies


$$
\boxed{
u_j(n)=\sum_i\binom ji c_i(n)E_{n+j-i}.
}
\tag{15.2}
$$



This is an identity for the retained force. It does not prescribe a different cutoff or a shortened producer.

Modulo $4$, terms with $i\ge8$ vanish. Parameter reduction gives


$$
(c_0,\ldots,c_7)(n)
\equiv(1,1,1,0,2,2,2,0)\pmod4,
$$


because $n\equiv-1\pmod4$.

Also,


$$
E_s=\sum_{r=0}^s(s)_r
\equiv1+s+(s)_2+(s)_3\pmod4,
$$


so $E_s$ has period $4$, with residues


$$
(E_0,E_1,E_2,E_3)\equiv(1,2,1,0)\pmod4.
$$



Using $n\equiv7\pmod8$ in the guarded sum (15.2) gives


$$
\boxed{u_n\equiv u_{n+1}\equiv0\pmod4.}
\tag{15.3}
$$


Together with (11.3),


$$
\boxed{
u_n-A\equiv1\pmod4,\qquad
u_{n+1}-D\equiv3\pmod4.
}
\tag{15.4}
$$



The binomial reductions used here require the index modulo $8$, not an unjustified period $4$ for the entire force expression.

## 16. Projecting the complete exterior-corrected exponential vector

Retain


$$
\mathbf U=
\bigl(mN(u_n-A),\ N(u_{n+1}-D),\ u_{n+2}-E\bigr)^T.
$$


The terminal normal identity gives


$$
q_\partial\mathbf U=2mNZ.
$$


The seed/reference and logarithmic terminal columns are annihilated by $q_\partial$, so this follows from the retained complete normal identity without an earlier-index logarithmic recurrence.

The exact row-coordinate identity now yields


$$
\boxed{
r_j\mathbf U
=
\frac m2(u_n-A)\alpha_j
+
\left(u_{n+1}-D-\frac m2(u_n-A)\right)\beta_j
+
mZz_j.
}
\tag{16.1}
$$



At endpoint $0$, $v_2(z_0)\ge3$; at endpoint $3$, $v_2(z_3)=5$. Since $v_2(Z)=1$, the final term in (16.1) has valuation at least $8$ at either endpoint.

The term


$$
\frac m2(u_n-A)\beta_j
$$


has valuation at least $7$.

Consequently, after division by $16$, reduction modulo $4$ gives


$$
\frac{r_j\mathbf U}{16}
\equiv
u\,a_j^\flat(u_n-A)
+b_j^\flat(u_{n+1}-D)
\pmod4.
$$


Using (15.4) and the actual primitive-row congruences (12.6), (13.2),


$$
\frac{r_j\mathbf U}{16}
\equiv
u\,a_j^\flat+3(-u\,a_j^\flat)
=-2u\,a_j^\flat
\equiv2\pmod4.
$$


Thus


$$
\boxed{
v_2(r_0\mathbf U)=v_2(r_3\mathbf U)=5.
}
\tag{16.2}
$$



This proves the endpoint-$3$ exact value rather than treating A4’s extra factor as an equality.

---

# VIII. Restoring the seed, logarithmic force, and actual denominator

## 17. The complete residual

The complete residual is


$$
C_j=r_j\mathbf U-E_nR_j+r_j\mathbf Q.
$$



The seed term has valuation at least


$$
v_2(R_j)=k+4>5.
$$


No unit assumption about $E_n$ is needed.

For the complete logarithmic term,


$$
r_j\mathbf Q
=
2n!m!(\alpha_j\rho_n+\beta_j\rho_{n+1}).
$$


Retain the established companion clearer


$$
2^{n+1}\operatorname{lcm}(1,\ldots,m),
$$


which clears $4\rho_n,4\rho_{n+1}$. If


$$
e_2^\flat=\lfloor\log_2m\rfloor,
$$


then


$$
v_2(\rho_n),v_2(\rho_{n+1})
\ge-(n+3+e_2^\flat).
$$


Since $v_2(G_j)=1$ and $v_2(m)=4$,


$$
\boxed{
v_2(r_j\mathbf Q)
\ge2t-n+3-e_2^\flat>5
}
\tag{17.1}
$$


for every original index in this subfamily, whose smallest value is $3375$.

Hence the valuation $5$ in (16.2) survives both restorations:


$$
\boxed{v_2(C_0)=v_2(C_3)=5.}
\tag{17.2}
$$



Likewise,


$$
E_nR_j+C_j=r_j\mathbf U+r_j\mathbf Q
$$


has valuation exactly $5$.

## 18. Actual primitive endpoint denominators

The retained all-prime formula is


$$
d_j=
\frac{|n!R_j|}
{\gcd(|n!R_j|,\ |E_nR_j+C_j|)}.
$$


We have proved


$$
v_2(n!R_j)=t+k+4,
\qquad
v_2(E_nR_j+C_j)=5.
$$


Therefore


$$
\boxed{
v_2(d_0)=v_2(d_3)=t+k-1.
}
\tag{18.1}
$$



This is the actual primitive denominator calculation, not a reference-depth proxy.

If $h_{\rm end}=\gcd(d_0,d_3)$, then on this subfamily


$$
\boxed{
v_2\!\left(\frac{d_0d_3}{h_{\rm end}^2}\right)=0.
}
\tag{18.2}
$$


Thus the binary contribution to the endpoint imbalance is $1$, in contrast with the contribution $4$ proved in Turn 7 on
$15^{2a}$ and $105^{4a}$.

At $n=3375$,


$$
t=3367,\qquad k=1687,
$$


so the new symbolic theorem gives


$$
v_2(R_j)=1691,\qquad v_2(C_j)=5,
\qquad v_2(d_j)=5053.
$$


The last value agrees with the already accepted denominator receipt. It is not a request to recompute that value, and it is not the proof of the infinite-family law.

I retain A4’s $\gamma_3$ bound at its stated scope. No additional $\gamma_j$ value is claimed here without displaying its separate primitive-triple normalization.

---

# IX. Complete reconstruction and whole error remain unchanged

## 19. Both corrected columns and all row contents

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


and $sx=Sx,\ sy=Sy$, the full columns remain


$$
u=
(-sx_0,\ sx_0-sx_1,\ sx_1-sx_2,\ sx_2),
$$




$$
v=
(1-sy_0,\ sy_0-sy_1,\ sy_1-sy_2,\ sy_2).
$$


The exterior $+1$ remains in the first coordinate of $v$.

The least clearer is still over all eight entries. Every reconstructed row is still divided by its actual two-entry content.

At $3375$, those accepted row contents remain


$$
\boxed{(113940000,\ 9780750,\ 10125,\ 1).}
$$


They are not replaced by $c_0,c_3$, by $\sigma_n$, or by any selected-prime contact-row content.

## 20. Final weighted normalization

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
\right).
$$


The actual primitive pair is


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
\tag{20.1}
$$



Every prime remains in these gcds.

The whole same-index error remains


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda e_3\alpha_{n,2}(\lambda-\Lambda_{n,2}).
}
\tag{20.2}
$$



The accepted five $3375$ whole-form enclosures remain finite evidence: all five forms are nonzero and have absolute value greater than $1$. The complete-producer receipt explicitly did not compute those enclosures; they are retained from their separate accepted source.

Neither the new joint-content theorem nor the binary law proves that a sequence of these whole nonzero errors tends to zero.

---

# X. New bounded arithmetic and proof status

## 21. What is already planned, and what is genuinely new here

The coordinator’s announced postprocessing of the retained $3375$ artifact is already the appropriate finite corroboration for Turn 7:

- four endpoint equations;
- integral residual identities;
- structural gcd divisibilities;
- the new moment-reference projected gcd values.

I do not request that work a second time. No new gcd values are inferred before its receipt.

No old producer, selected $3/5/7$ extraction, binary denominator extraction, or whole-error enclosure needs to be rerun.

### Optional new add-on for the joint theorem

This turn supplies additional identities that can be checked in the same archived-data setting.

**Inputs**

- archived $J$;
- the actual primitive contact rows $r_0,r_3$;
- the raw contact rows and their exact contents $c_0,c_3$;
- archived terminal moments;
- archived $R_j,C_j,h,\ell$;
- $\mathscr K_n$ recovered from the retained $b_n,b_{n+1}$ and the complete logarithmic correction.

**Expected verifiable output**

1. The zero vector residual
   

$$
c_0c_3(r_0\times r_3)
   \mp\det(J)(nJ_0+J_1)=0,
$$


   with the sign determined by the actual primitive-row conventions.

2. The exact integer identity
   

$$
\sigma_n c_0c_3
   =
   |\det J|\,\operatorname{cont}(nJ_0+J_1).
$$



3. After removing only primes at most $3377$,
   

$$
\operatorname{cont}(nJ_0+J_1)_{>3377}=1.
$$



4. With
   

$$
g_n=\gcd(R_0,R_3,C_0,C_3)_{>3377},
$$


   the divisibility certificate
   

$$
\frac{g_n}{\gcd(g_n,\Sigma_n)}
   \mid
   \gcd(\ell,Z,Y-2X,\mathscr K_n)_{>3377}.
$$



The numerical values in items 2–4 are not supplied here. These are new identity/divisibility checks, not inferred outputs.

### Binary corroboration

The binary theorem is proved symbolically above and requires no new producer.

If new force fields are included in the announced archived-data postprocessing, its theorem-predicted values at $3375$ are


$$
v_2(\alpha_j)=1,\quad v_2(\beta_j)=4,\quad
v_2(R_j)=1691,\quad
v_2(r_j\mathbf U)=v_2(C_j)=5.
$$


These would be new corroborating fields. The already accepted denominator value $5053$ should not be recalculated merely to support the theorem.

## 22. Status ledger

| Statement | Status |
|---|---|
| Turn 7 endpoint equations and residual identities | Retained symbolic proofs; announced new finite corroboration pending |
| Turn 7 local projection ideal and $\Pi_0,\Pi_3$ losses | Retained; not rederived as the main advance |
| Actual shared column $L=nJ_0+J_1$ is primitive at $p>n+2$ | **New proof** |
| Exact contact-row collision index $\sigma_n$ | **New identity and Smith-index interpretation** |
| Saturated joint cancellation theorem (6.1) | **New proof** |
| $O(n)$ bound for $g_n/\gcd(g_n,\Sigma_n)$ | **New unconditional bound** |
| $O(n)$ or $o(n\log n)$ bound for $\log(\mathfrak D_0\mathfrak D_3)$ | Not proved |
| Exact endpoint-$0$ primitive-row depths on $15^{2a+1}$ | **New proof** |
| Exact reference projections $v_2(R_j)=k+4$ there | **New proof** |
| Exact complete exponential force depth $5$, both endpoints | **New proof** |
| Seed and complete logarithmic restoration | **Included in proof** |
| Actual binary denominator law $v_2(d_j)=t+k-1$ there | **New infinite-family theorem** |
| New $3375$ projected gcd values | Not received; not inferred |
| Infinite final all-prime denominator/whole-error comparison | Open |
| Irrationality or rationality of $e+\pi$ | Unresolved |

---

# Conclusion

The primary target has advanced, but has not been closed.

Coupling the two actual endpoint rows gives a new saturated joint theorem:


$$
\boxed{
\frac{\gcd(\delta_0^{>},\delta_3^{>})}
{\gcd(\delta_0^{>},\delta_3^{>},\Sigma_n)}
\mid
\gcd(\ell,Z,Y-2X,\mathscr K_n)_{>n+2}.
}
$$


The quotient has an unconditional $O(n)$ logarithmic bound. The exact extra arithmetic factor is the actual contact-row Smith index


$$
\boxed{
\Sigma_n=
\left(
\frac{|\det J|\,\operatorname{cont}(nJ_0+J_1)}
{c_0c_3}
\right)_{>n+2}.
}
$$



The precise remaining product-content obstruction is cancellation on this collision index together with the two prime-disjoint endpoint-exclusive contents. A full-state determinant or an exponential reference-height bound alone does not control them.

The secondary target is completed on the requested original subfamily:


$$
\boxed{
n=15^{2a+1},\ a\ge1
\quad\Longrightarrow\quad
v_2(r_j\mathbf U)=v_2(C_j)=5,\quad
v_2(R_j)=\frac{n-1}{2}+4,
}
$$


and


$$
\boxed{
v_2(d_0)=v_2(d_3)
=v_2(n!)+\frac{n-3}{2}.
}
$$


The proof retains the correct parameter/index periods, pays the primitive-row divisions, and restores the seed, complete logarithmic force, and exterior contribution.

Even a successful completion of the remaining content estimate must still be combined with every weight-dependent all-prime gcd and the whole nonzero same-index error in (20.2).



$$
\boxed{\text{No unconditional proof or disproof of the irrationality of }e+\pi
\text{ has been obtained.}}
$$


