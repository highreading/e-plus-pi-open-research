> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, turn 4: a fixed-$3$ saturation theorem for the actual proportional center

I do not obtain an unconditional decision on the irrationality of $e+\pi$.

I do obtain a fixed-prime result on the **assigned unbounded family**, rather than another moving-prime calculation. The result includes the actual endpoint-matched lift, its saturated coefficient lattice, the restricted falling metric, and the final denominator cancellation.

Put


$$
n=2001\cdot3^a,\qquad b=3^a,\qquad a\ge1,
\qquad \ell=n+2,
\qquad \omega_j=\frac{\ell!}{(\ell-j)!}.
$$


For the actual rational center $p_n/q_n$, reduced with $q_n>0$, the arithmetic developed below proves


$$
\boxed{v_3(q_n)\le n-8.}
\tag{A}
$$


The proof does not extrapolate a fixed-$b$ polynomial transfer. It uses a divided-column contact matrix which is unimodular over $\mathbb Z_3$ even as $b$ grows.

There is also an exact smaller-scale norm law. If $z_0$ is the primitive zero-$B(1)$ generator of the saturated matched $B$-coefficient lattice, then


$$
\boxed{
v_3(z_0^T\Omega z_0)
=2v_3((b-1)!)+1=b-2a,
}
\qquad \Omega=\operatorname{diag}(\omega_j^2).
\tag{B}
$$


This is not presented as the primitive denominator. The final gcd is treated separately in Sections 7–8.

The fixed-$3$ estimate is compatible with, but does not establish, a favorable aggregate denominator rate. Its leading logarithmic contribution is at most $n\log 3$; all other primes remain to be controlled at the same indices.

---

## 1. An exact contact reduction that includes matching and both endpoints

This section derives the matrix used below directly from the contact problem. Thus no growing-$b$ extension of a fixed-$b$ theorem is assumed.

Write


$$
\phi(z)=1-z+\frac{z^2}{2},\qquad
F(z)=4\arctan\frac{z}{2-z},\qquad F'(z)=\frac2{\phi(z)}.
$$


Consider the endpoint-matched contact construction with caps $(n,b,n)$, contact order


$$
M=2n+b,
$$


and prescribed endpoints


$$
A(1)=P,\qquad B(1)=C(1)=Q.
$$


Set


$$
A=(z-1)A'+P,\quad
B=(z-1)B'+Q,\quad
C=(z-1)C'+Q.
$$


Then


$$
\deg A',\deg C'<n,\qquad \deg B'<b,
$$


and the contact condition is equivalent to


$$
A'+e^zB'+F C'
\equiv
\frac{P+Q(e^z+F)}{1-z}\pmod {z^M}.
\tag{1.1}
$$



### 1.1 Eliminating $A'$ and $C'$

Apply $\phi^n D^n$, where $D=d/dz$. The $A'$ term disappears. Moreover


$$
\phi^nD^n(C'F)
$$


is a polynomial of degree at most $n-1$.

Here is the degree justification. Leibniz expansion makes it rational with denominator dividing $\phi^n$, so multiplication by $\phi^n$ makes it polynomial. At infinity, $F$ has a Laurent expansion consisting of a constant and negative powers: its derivative is $O(z^{-2})$. Thus $C'F$ is a polynomial of degree at most $n-1$, plus negative powers. Its $n$-th derivative is $O(z^{-n-1})$. Multiplication by $\phi^n=O(z^{2n})$ leaves degree at most $n-1$.

Put


$$
g=(1+D)^nB',\qquad g(z)=\sum_{j=0}^{b-1}g_jz^j.
$$


Taking coefficients of degrees $n,\ldots,n+b-1$ after the preceding operation gives


$$
N g=P f+Q h,
\tag{1.2}
$$


where


$$
N_{ij}=\sum_{s=0}^{\min(2n,n+i)}
 a_s(n)(n+i)^{\underline{j+s}},
\qquad
a_s(n)=[z^s]\phi(z)^n,
\tag{1.3}
$$


and $0\le i,j<b$.

The forcing vectors are the **whole** forcing vectors:


$$
f_i=(n+i)![z^{n+i}]\phi^nD^n\frac1{1-z},
\tag{1.4}
$$




$$
h_i=(n+i)![z^{n+i}]\phi^nD^n\frac{e^z+F}{1-z}.
\tag{1.5}
$$



The map


$$
C'\longmapsto \phi^nD^n(C'F)
$$


from polynomials of degree $<n$ to themselves is injective. Indeed, a zero image would make $C'F$ a polynomial, which is impossible for nonzero $C'$: $F$ has nonzero logarithmic singularities at the two roots of $\phi$. Hence the map is an isomorphism over $\mathbb Q$. After reconstructing $C'$, the remaining $n$ coefficients determine $A'$.

Consequently, nonsingularity of $N$ proves normality of this endpoint problem; (1.2) determines its actual $B$-lift.

### 1.2 The explicit $P$-forcing

Define


$$
J_i=[t^n](1+2t+2t^2)^n(1+t)^i,
\qquad
D_i=\frac{(n+i)!}{n!},
\qquad
f^{\,0}_i=D_iJ_i,
$$


and


$$
\lambda=\frac{(n!)^2}{2^n}.
$$


Then


$$
\boxed{f=\lambda f^{\,0}.}
\tag{1.6}
$$



For a direct coefficient verification, the substitution $u=z/(1-z)$, followed by reversal of the resulting polynomial, gives


$$
[z^{n+i}]\frac{\phi(z)^n}{(1-z)^{n+1}}
=
2^{-n}[u^n](1+2u+2u^2)^n(1+u)^i.
$$


Multiplying by $n!(n+i)!$ proves (1.6).

### 1.3 The complete $Q$-forcing is $3$-integral

Let


$$
\mathcal D_m=m!\sum_{r=0}^m\frac1{r!},
\qquad
\mathcal F_m=[z^m]\frac{F(z)}{1-z}.
$$


Then


$$
h=h^e+h^F,
\tag{1.7}
$$


where


$$
h^e_i=\sum_s a_s(n)(n+i)^{\underline s}\,
                 \mathcal D_{2n+i-s},
\tag{1.8}
$$




$$
h^F_i=\sum_s a_s(n)(n+i)^{\underline s}\,
                 (2n+i-s)!\mathcal F_{2n+i-s}.
\tag{1.9}
$$


The sum ranges are those in (1.3). In particular every index $2n+i-s$ is at least $n$.

Both vectors belong to $\mathbb Z[1/2]^b$. For the logarithmic part, write


$$
\frac1{\phi(z)}=\sum_{r\ge0}c_rz^r,\qquad c_r\in\mathbb Z[1/2].
$$


Since


$$
[z^r]F(z)=\frac{2c_{r-1}}r\quad(r\ge1),
$$


the quantity $m!\mathcal F_m$ is dyadically integral. Thus (1.9) retains the full logarithmic forcing without introducing an uncontrolled odd-prime denominator.

Let $Z$ denote multiplication by $z-1$, and set


$$
K=Z(1+D)^{-n}.
$$


The actual two-column $B$-lift is therefore


$$
\boxed{
u=\lambda K N^{-1}f^{\,0},\qquad
v=e_0+K N^{-1}h.
}
\tag{1.10}
$$


It satisfies


$$
\boldsymbol e u=0,\qquad \boldsymbol e v=1,
$$


and its endpoint coordinates are respectively $(1,0)$ and $(0,1)$. Matching and both endpoints are built into (1.10); there is no omitted endpoint correction.

---

## 2. Divided columns remove the growing contact determinant content at $3$

Let


$$
D_b=\operatorname{diag}(0!,1!,\ldots,(b-1)!),
\qquad
\widetilde N=ND_b^{-1}.
$$


Its entries are


$$
\widetilde N_{ij}
=
\sum_s a_s(n)(n+i)^{\underline s}
              \binom{n+i-s}{j}.
\tag{2.1}
$$


They lie in $\mathbb Z[1/2]$.

The following divisibility is the key point.

### Lemma 2.1
For every positive integer $n$, there is a matrix
$C\in M_b(\mathbb Z[1/2])$ such that


$$
\boxed{
\widetilde N=B(n)+nC,\qquad
B(n)_{ij}=\binom{n+i}{j}.
}
\tag{2.2}
$$



#### Proof

For $s\ge1$,


$$
s\,a_s(n)
=n[z^{s-1}]\phi'(z)\phi(z)^{n-1}.
$$


Therefore


$$
a_s(n)(n+i)^{\underline s}
=
n(s-1)!\binom{n+i}{s}
       [z^{s-1}]\phi'\phi^{n-1},
$$


which belongs to $n\mathbb Z[1/2]$. The $s=0$ term of (2.1) is $\binom{n+i}{j}$. ∎

The binomial matrix $B(n)$ is unimodular over $\mathbb Z$. Indeed,


$$
B(n)=P_bT_b(n),
$$


where


$$
(P_b)_{ir}=\binom ir,\qquad
(T_b(n))_{rj}=\binom n{j-r}.
$$


Both factors are triangular with diagonal entries one.

Hence, whenever $3\mid n$,


$$
\boxed{\widetilde N\in\operatorname{GL}_b(\mathbb Z_3).}
\tag{2.3}
$$


This holds for arbitrary growing dimension. In particular, $N$ is nonsingular over $\mathbb Q$, so the assigned indices are arithmetically normal without appealing to an eventual-normality hypothesis.

The substantial content here is that the factorial column factors are removed **before** taking determinants. The remaining contact block is a $3$-adic unit matrix. A raw determinant valuation $\sum_{j<b}v_3(j!)$ is not credited as an endpoint denominator.

---

## 3. An explicit recursive $3$-adic description

The reduction is recursive in both precision and dimension.

### 3.1 Frobenius coefficient recursion

Set


$$
R_\phi(t)=\frac{\phi(t)^3-\phi(t^3)}3\in\mathbb Z_3[t].
$$


Then, exactly,


$$
\boxed{
\phi(t)^{3n}
=
\sum_{r=0}^n
\binom nr3^rR_\phi(t)^r\phi(t^3)^{n-r}.
}
\tag{3.1}
$$


Together with (2.1), this computes the contact rows at


$$
(n,b)\longmapsto(3n,3b)
$$


to any prescribed $3$-adic precision. Terms whose displayed valuation exceeds that precision may be omitted with a proved modulus.

Modulo $3$, the Pascal matrices satisfy the Lucas tensor recursion


$$
\binom{3I+r}{3J+s}
\equiv\binom IJ\binom rs\pmod3,
\qquad 0\le r,s<3.
\tag{3.2}
$$


Thus the unit reduction of the growing divided contact block is recursively explicit, rather than a finite seed with $b$ held fixed.

After obtaining an inverse modulo $3$, ordinary inverse lifting,


$$
H_{\rm new}=H(2I-\widetilde N H),
\tag{3.3}
$$


doubles its verified precision. Equation (2.3) guarantees that no nonunit pivot is hidden in this step.

### 3.2 The integral divided reconstruction

Let $S$ be the shift acting on divided coefficients:


$$
D\left(\sum_j y_j\frac{z^j}{j!}\right)
=\sum_j y_{j+1}\frac{z^j}{j!}.
$$


Then


$$
(1+S)^{-n}
=\sum_{r=0}^{b-1}\binom{-n}{r}S^r
\tag{3.4}
$$


is integral. Multiplication by $z-1$ becomes


$$
(\mathcal Z y)_j=j\,y_{j-1}-y_j,
\tag{3.5}
$$


with missing coefficients zero.

Define


$$
y=\widetilde N^{-1}f^{\,0},\qquad
y^Q=\widetilde N^{-1}h,
\qquad
z=KD_b^{-1}y.
\tag{3.6}
$$


Then $u=\lambda z$.

For every divided coefficient vector $c\in\mathbb Z_3^b$,


$$
\boxed{
\bigl(\operatorname{diag}(\omega_j)KD_b^{-1}c\bigr)_j
=
\binom{n+2}{j}\,
\bigl(\mathcal Z(1+S)^{-n}c\bigr)_j
\in\mathbb Z_3.
}
\tag{3.7}
$$


This is the actual falling metric. No alternate metric is introduced.

It follows immediately that


$$
\operatorname{diag}(\omega_j)z,\quad
\operatorname{diag}(\omega_j)v
\in\mathbb Z_3^{b+1}.
\tag{3.8}
$$



---

## 4. Uniform modulo-$9$ structure on the assigned family

Now specialize to


$$
n=2001\cdot3^a,\quad b=3^a,\quad a\ge1.
$$


Write


$$
k=v_3(n)=a+1,\qquad
F_n=v_3(n!),\qquad s=v_3((b-1)!).
$$



For $1\le r<b$,


$$
v_3\binom nr\ge k-v_3(r)\ge2.
$$


Together with (2.2), this proves


$$
\boxed{\widetilde N\equiv P_b\pmod9.}
\tag{4.1}
$$


The same argument gives


$$
\boxed{(1+S)^{-n}\equiv I\pmod9.}
\tag{4.2}
$$



### 4.1 Endpoint Lucas structure

Put


$$
W(t)=t^{-1}+2+2t.
$$


Then


$$
J_i=\operatorname{CT}_t W(t)^n(1+t)^i.
\tag{4.3}
$$



Since $n$ is divisible by $3^{a+1}$ and $i<b$, Frobenius gives


$$
J_i\equiv J_0\pmod3.
\tag{4.4}
$$


Moreover $J_0$ is a $3$-unit. Indeed, its base-$3$ digit factors are


$$
\operatorname{CT}W^0=1,\quad
\operatorname{CT}W^1=2,\quad
\operatorname{CT}W^2=8,
$$


all units modulo $3$. The Laurent exponent range of $W^r$, $r=0,1,2$, is contained in $[-2,2]$, which makes the constant-term digit factorization exact modulo $3$.

For the first three forcing positions one has the stronger statement


$$
\boxed{J_1\equiv J_2\equiv J_0\pmod9.}
\tag{4.5}
$$


To see this, use


$$
W(t)^n\equiv W(t^3)^{n/3}\pmod{3^k}.
$$


It follows by raising $W^3\equiv W(t^3)\pmod3$ to the power $n/3$, retaining the valuation of the binomial cross terms. The coefficients of exponents $-1,-2$ therefore vanish modulo $9$.

Solving (4.1) on the first three coordinates now gives


$$
\boxed{(y_0,y_1,y_2)\equiv(J_0,0,J_0)\pmod9.}
\tag{4.6}
$$



On all coordinates, (4.4) and the inverse Pascal transform give


$$
y_j\equiv J_0\,!j\pmod3,
\tag{4.7}
$$


where $!j$ denotes the derangement number. This is only the elementary finite-difference identity


$$
!j=\sum_{i=0}^j(-1)^{j-i}\binom ji i!;
$$


no Hankel determinant result is used.

Since $b-1\equiv2\pmod3$ and is even,


$$
!(b-1)\equiv1\pmod3.
$$


Thus


$$
\boxed{y_{b-1}\in\mathbb Z_3^\times.}
\tag{4.8}
$$



---

## 5. The restricted metric has exact norm depth one before primitive scaling

Define


$$
\mathfrak D=z^T\Omega z.
$$


By (3.8), $\mathfrak D\in\mathbb Z_3$.

For $3\le j\le b$,


$$
v_3(\omega_j)=k+v_3((j-3)!),
$$


so


$$
v_3\binom{n+2}{j}
=k-v_3\bigl(j(j-1)(j-2)\bigr)\ge1.
\tag{5.1}
$$


The first three weighted coordinates, by (4.2) and (4.6), are


$$
\bigl(\omega_0z_0,\omega_1z_1,\omega_2z_2\bigr)
\equiv(-J_0,2J_0,-J_0)\pmod9.
\tag{5.2}
$$


Here these subscripts are coefficient indices, not lattice-basis labels.

Every later weighted coordinate is divisible by $3$. Its square therefore vanishes modulo $9$. Hence


$$
\boxed{
\mathfrak D\equiv6J_0^2\pmod9,\qquad
v_3(\mathfrak D)=1.
}
\tag{5.3}
$$



This explicitly resolves the first isotropic reduction: the three surviving squares do cancel modulo $3$, but not modulo $9$.

### 5.1 Exact primitive zero-endpoint scale

All coefficients of $z$ have valuation at least $-s$. Its last coefficient is


$$
z_b=\frac{y_{b-1}}{(b-1)!},
$$


so (4.8) proves


$$
\boxed{\min_jv_3(z_j)=v_3(z_b)=-s.}
\tag{5.4}
$$



The primitive zero-endpoint lattice generator is therefore a $3$-adic unit multiple of $3^s z$. Consequently


$$
\boxed{
v_3(T)=2s+1,\qquad T=z_0^T\Omega z_0.
}
\tag{5.5}
$$


Legendre’s formula yields


$$
s=\frac{b-1-2a}{2},
$$


and hence the announced exact law


$$
v_3(T)=b-2a.
$$



---

## 6. Complete saturation of the matched coefficient lattice

The unit divided contact block does not by itself identify the saturated ordinary-coefficient lattice. The remaining factorial congruences can, however, be resolved exactly in rank two.

Normalize locally by


$$
\zeta=\frac z{z_b}.
$$


Then


$$
\zeta\in\mathbb Z_3^{b+1},\qquad
\zeta_b=1,\qquad
\boldsymbol e\zeta=0.
$$


Put


$$
w=v-v_b\zeta.
$$


Thus


$$
w_b=0,\qquad \boldsymbol e w=1.
$$



Define


$$
\mu=\max\{0,-\min_jv_3(w_j)\}.
\tag{6.1}
$$


Both $v$ and $v_b\zeta$ have denominators of depth at most $s$, so


$$
0\le\mu\le s.
\tag{6.2}
$$



Every vector in the rational matched plane has a unique expression


$$
B=c\zeta+Qw.
$$


Its last coefficient is $c$, and its endpoint sum is $Q$. Therefore it is integral precisely when


$$
c\in\mathbb Z_3,\qquad Q\in3^\mu\mathbb Z_3.
$$


We have proved the exact saturated description


$$
\boxed{
\mathscr L\otimes\mathbb Z_3
=
\mathbb Z_3\zeta\oplus\mathbb Z_3(3^\mu w),
\qquad v_3(h)=\mu.
}
\tag{6.3}
$$



This includes the actual matching equation through the construction of $v$, and not merely the high-row kernel.

The actual $A$-endpoint row on this basis is equally explicit:


$$
\boxed{
\xi=\frac1{\lambda z_b},\qquad
\eta=-\frac{3^\mu v_b}{\lambda z_b}.
}
\tag{6.4}
$$


Indeed $u=\lambda z$ has $A$-endpoint one, while $v$ has $A$-endpoint zero.

Let


$$
\kappa=v_3(v_b),
$$


allowing $\kappa=\infty$ if $v_b=0$, and let $d=v_3(d_B)$, where $d_B$ is the least denominator of the full two-column lift. Since $u$ is already integral at $3$,


$$
\boxed{d=\max(\mu,-\kappa),\qquad 0\le d\le s.}
\tag{6.5}
$$


The equality follows in both directions from $v=v_b\zeta+w$, with $\zeta_b=1$.

For the endpoint scalars used in the earlier exact factorization, let $D_0$ be their least common denominator and $\gamma=\gcd(h,a,b_{\rm end})$. Equations (6.4) give


$$
\boxed{
v_3(D_0)=2F_n-s+d-\mu,\qquad v_3(\gamma)=0,
}
\tag{6.6}
$$


and therefore


$$
\boxed{
v_3(k)=2F_n-s+d,\qquad k=\frac{hD_0}{\gamma}.
}
\tag{6.7}
$$



The assertion $v_3(\gamma)=0$ has a specific reason. The denominator in (6.6) has positive valuation; minimality of that common denominator forces at least one of the two endpoint numerators to be a unit. It is not an assumption of scalar primitiveness.

Equations (3.1)–(3.5) and (6.1)–(6.7) supply an exact recursive $3$-adic saturated description, with a uniform bound on every residual denominator depth. No unbounded matching-row saturation remains hidden.

---

## 7. The whole cross contraction and the final gcd

Define the complete cross contraction


$$
\boxed{
\mathfrak C=z^T\Omega v
=z^T\Omega\left(e_0+KD_b^{-1}\widetilde N^{-1}(h^e+h^F)\right).
}
\tag{7.1}
$$


Every term in (7.1) is retained. In particular, it contains the endpoint correction $e_0$, the whole exponential forcing, and the whole logarithmic forcing.

By (3.8),


$$
\mathfrak C\in\mathbb Z_3.
$$


Write


$$
\chi=v_3(\mathfrak C),
$$


with $\chi=\infty$ if it vanishes. The actual center is exactly


$$
\boxed{
\mathfrak c_n=\frac{u^T\Omega v}{u^T\Omega u}
=\frac{\mathfrak C}{\lambda\mathfrak D}.
}
\tag{7.2}
$$



Let $N_B=d_B[u,v]$ be the primitive integer lift from the supplied intrinsic interface, and let


$$
A_B=N_{B,1}^T\Omega N_{B,1},\qquad
H_B=N_{B,1}^T\Omega N_{B,2},\qquad
g_B=\gcd(A_B,|H_B|).
$$


Then


$$
v_3(A_B)=2d+4F_n+1,
$$




$$
v_3(H_B)=2d+2F_n+\chi.
$$


Thus the **evaluated final gcd**, not a row content, has exact valuation


$$
\boxed{
v_3(g_B)
=2d+2F_n+\min(2F_n+1,\chi).
}
\tag{7.3}
$$


The actual primitive denominator satisfies


$$
\boxed{
v_3(q_n)
=2F_n+1-\min(2F_n+1,\chi)
=\max(0,2F_n+1-\chi).
}
\tag{7.4}
$$



The unresolved value $\chi$ is an explicitly defined whole contraction, not an omitted error term. Any extra cancellation in it decreases the denominator; it cannot invalidate the upper bound.

### 7.1 A further forced cancellation: $\chi\ge2$

On this family one can prove more than integrality.

First, the divisibility argument in Lemma 2.1 also gives


$$
h^e_i\equiv\mathcal D_{2n+i}\pmod9.
$$


The sequence $\mathcal D_m$ is periodic modulo $9$ with period $9$: in


$$
\mathcal D_m=\sum_{r\ge0}m^{\underline r},
$$


all terms with $r\ge6$ vanish modulo $9$, and the remaining falling-factorial polynomials are periodic modulo $9$. Since $9\mid n$,


$$
h^e_i\equiv\mathcal D_i\pmod9.
\tag{7.5}
$$



Second,


$$
h^F\equiv0\pmod9.
\tag{7.6}
$$


Indeed every factorial index in (1.9) is at least $n$, and


$$
v_3(m!\mathcal F_m)
\ge v_3(m!)-\lfloor\log_3m\rfloor.
$$


For the present $n\ge6003$, this is at least two throughout
$n\le m\le2n+b-1$.

Combining (4.1), (7.5), and (7.6), the inverse Pascal transform gives


$$
y^Q_j\equiv j!\pmod9.
\tag{7.7}
$$


Together with (4.2), the divided reconstruction is zero modulo $9$ at coordinates $1,\ldots,b-1$; at coordinate zero it is $-1$, canceled by $e_0$. The final weighted coordinate is congruent to


$$
\binom{n+2}{b}b!=\omega_b,
$$


which is divisible by $9$.

Therefore


$$
\boxed{
\operatorname{diag}(\omega_j)v\equiv0\pmod9,
\qquad \chi\ge2.
}
\tag{7.8}
$$


Equations (7.4) and (7.8) prove


$$
v_3(q_n)\le2F_n-1.
$$


Finally, the base-$3$ expansion of $2001$ is $2202010_3$, whose digit sum is seven. Hence


$$
2F_n=n-7,
$$


and


$$
\boxed{v_3(q_n)\le n-8.}
$$



---

## 8. Compatibility with the retained $t/\alpha$ and scalar factors

For completeness, retain the exact factorization


$$
\delta=\gcd(T,|V_0|),\qquad
t=T/\delta,\qquad v_0=V_0/\delta,
$$




$$
\alpha=\gcd(t,|a'|),\qquad
r=\frac{a'v_0-b't}{\alpha}.
$$


Then


$$
\boxed{
q_n=\frac t\alpha\frac{k}{\gcd(k,|r|)},
\qquad
g_B=k\delta\alpha\gcd(k,|r|).
}
\tag{8.1}
$$



Nothing in Sections 2–7 replaces (8.1) by a Gram determinant.

Using the local adapted basis $\zeta,3^\mu w$,


$$
v_3(T)=2s+1,
$$


and


$$
V_0
=3^\mu\left(
\frac{\mathfrak C}{z_b}
-\frac{v_b\mathfrak D}{z_b^2}
\right).
\tag{8.2}
$$


In particular,


$$
v_3(V_0)\ge\mu+s.
$$


Thus


$$
v_3(t)\le s+1-\mu.
\tag{8.3}
$$


Also, by (6.4)–(6.6),


$$
v_3(a')=d-\mu.
$$


Therefore


$$
v_3(t/\alpha)
=\max(0,v_3(t)-(d-\mu)),
\tag{8.4}
$$


while


$$
v_3(k)=2F_n-s+d.
$$


These formulas explicitly preserve the norm cancellation, the endpoint numerator cancellation $\alpha$, and the final scalar cancellation $\gcd(k,r)$.

The stronger whole-contraction calculation (7.3)–(7.8) proves that their actual combined contribution is at most $n-8$. The scalar and norm channels have not been estimated using incompatible normalizations.

---

## 9. Whole error, nonvanishing, and the aggregate limitation

The arithmetic normality used above is proved by (2.3). For the analytic conclusion, I retain the supplied proportional signed-rate theorem at its stated source/dependency status rather than re-proving its contour analysis.

On the assigned sequence,


$$
\frac bn=\frac1{2001}<0.001,
\qquad
\tau_c=\left(2+\frac1{2001}\right)\log(1+\sqrt2).
$$


Under that supplied theorem, eventually


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi)\ne0,
\qquad
\log|\epsilon_n|=-\tau_c n+o(n).
$$


The **whole primitive evaluated error** is exactly


$$
\boxed{
L_n=q_n(e+\pi)-p_n=-q_n\epsilon_n\ne0,
}
\tag{9.1}
$$


and


$$
\log|L_n|
=
\log\frac t\alpha
+\log\frac{k}{\gcd(k,|r|)}
-\tau_c n+o(n).
\tag{9.2}
$$



The new fixed-prime theorem supplies only


$$
v_3(q_n)\log3\le(n-8)\log3.
$$


It supplies no upper bound for


$$
\sum_{p\ne3}v_p(q_n)\log p.
$$


Accordingly, it proves neither primitive shrinking nor exclusion of this proportional-center family.

I do not add a $d=3$ seven-tail chart: the secondary assignment permitted that step only if it produced a uniform recursive mechanism. The fixed-$3$ divided-column mechanism above is the substantive uniform mechanism obtained here; another isolated moving-prime chart would not strengthen its aggregate conclusion.

---

# 10. Cross-review of A3’s compensated pair and the unique-last-term argument

## 10.1 The compensated normalization and final gcd pass the algebraic audit

From the contiguous $b=2$ formulas,


$$
Y_k=s_k\mathscr D_k,\qquad
X_k=s_k\mathscr X_k,
\qquad
s_k=\frac{(-1)^k}{4(k!)^4(k+1)^3}.
$$


This scalar agrees with the displayed Rodrigues/Wronskian factors.

Thus A3’s definitions


$$
J_k=\frac{\mathscr D_k}{(k!)^2},
\qquad
H_k=\frac{\mathscr X_k}{(k!)^2}
$$


are exact. If


$$
\mathcal H=\sum_jw_jH_{n+j},
\qquad
\mathcal J=\sum_jw_jJ_{n+j},
$$


and $L_N$ is A3’s common clearer, then


$$
U=L_N\mathcal H,\qquad T=L_N\mathcal J,
$$


and, for $T\ne0$,


$$
q=\frac{|T|}{\gcd(|U|,|T|)},\qquad
P=-\operatorname{sgn}(T)\frac{U}{\gcd(|U|,|T|)}
$$


is the actual primitive pair.

The whole evaluated error is


$$
\boxed{
q(e+\pi)-P
=q\,\frac{\mathcal H+(e+\pi)\mathcal J}{\mathcal J}.
}
\tag{10.1}
$$


The filtered complete-error nonvanishing remains unproved. Nonvanishing of $\mathcal H$ alone does not resolve it.

A3’s growth-ratio manipulations are algebraically consistent with its stated inherited raw asymptotics. Those asymptotic premises are not independently re-proved here.

## 10.2 The unique-last-term claim is valid at odd primes under its raw-unit hypothesis

Let


$$
N=n+m,\qquad p\mid N,\qquad p\ \text{odd},\qquad p\nmid a.
$$


Use the **exact raw** decomposition


$$
\mathscr X_k=Q_k+\frac{2^{k+1}}{(k!)^2}V_k.
$$


Then


$$
\boxed{
H_k=\frac{Q_k}{(k!)^2}
+\frac{2^{k+1}V_k}{(k!)^4}.
}
\tag{10.2}
$$


The fourth factorial power is indispensable.

Assume


$$
v_p(V_N)=0.
\tag{10.3}
$$


The raw $V_k$ are $p$-integral, while the second-kind moment bound gives


$$
v_p(Q_k)\ge-\lfloor\log_p(k+1)\rfloor.
\tag{10.4}
$$



Put


$$
F=v_p(N!),\qquad d=v_p(N)\ge1.
$$


For $k<N$,


$$
v_p(k!)\le F-d.
\tag{10.5}
$$


Also, because $p\le N$,


$$
\lfloor\log_p(N+1)\rfloor\le F<2F.
\tag{10.6}
$$


For example, if $A=\lfloor N/p\rfloor$, then
$N+1<(p^{A+1})$, so the logarithmic floor is at most $A\le F$.

The last factorial term in (10.2) has valuation $-4F$. Its last $Q_N$-term has valuation at least


$$
-2F-\lfloor\log_p(N+1)\rfloor>-4F.
$$


Every earlier factorial term has valuation at least


$$
-4(F-d)>-4F.
$$


Every earlier $Q$-term has valuation at least


$$
-2(F-d)-\lfloor\log_p(N+1)\rfloor>-4F.
$$



The last binomial-filter weight is $a^m$, a $p$-unit. All other weights are $p$-integral. Therefore the last factorial term is uniquely of least valuation, and


$$
\boxed{v_p(\mathcal H)=-4F.}
\tag{10.7}
$$


Since $\mathscr D_k$ is integral,


$$
\boxed{v_p(\mathcal J)\ge-2F.}
\tag{10.8}
$$


For $\mathcal J\ne0$, the actual reduced denominator of
$-\mathcal H/\mathcal J$ consequently satisfies


$$
\boxed{
v_p(q)=4F+v_p(\mathcal J)\ge2F.
}
\tag{10.9}
$$



There is no equal-valuation gap in this argument under (10.3).

### Necessary qualifications

1. **Odd prime:** at $p=2$, the factor $2^{k+1}$, and possible dyadic denominators in $V_k$, change the scale. The assertion $-4F$ cannot simply be reused.

2. **Exact raw $V_N$:** a unit statement for a differently normalized contraction is insufficient unless its canceled scalar has been tracked at $p$.

3. **Last weight:** if $p\mid a$, the last term need not be a unit-weighted unique minimum.

4. **Filtered endpoint:** $\mathcal J\ne0$ is still required. A3’s eventual same-sign endpoint theorem supplies this on its stated domain.

5. **Whole error:** (10.7) proves $\mathcal H\ne0$, not
$\mathcal H+(e+\pi)\mathcal J\ne0$.

A slightly broader bounded lemma also follows. If


$$
v=v_p(V_N)
<
\min\{4d,\ 2F-\lfloor\log_p(N+1)\rfloor\},
$$


then the same strict comparisons give


$$
v_p(\mathcal H)=-4F+v,\qquad
v_p(q)\ge2F-v.
$$


This extension still requires a proved valuation of the exact raw $V_N$; it supplies no automatic raw-unit theorem.

---

# Concluding ledger

## (1) New result and proof status

**Proved here by explicit arithmetic derivation:**

- A direct endpoint-matched contact reduction with both prescribed endpoint coordinates and the complete exponential/logarithmic forcing.
- A divided-column identity
  

$$
\widetilde N=B(n)+nC,
$$


  proving $3$-adic unimodularity for every growing dimension when $3\mid n$.
- Exact Frobenius/Lucas and precision recursions on
  

$$
n=2001\cdot3^a,\qquad b=3^a.
$$


- An exact saturated matched $B$-lattice description and its actual endpoint rows.
- The primitive norm law
  

$$
v_3(T)=b-2a.
$$


- The evaluated final-gcd formula
  

$$
v_3(g_B)=2d+2F_n+\min(2F_n+1,\chi),
$$


  with the complete contraction $\mathfrak C$ specified in (7.1).
- The actual primitive-denominator bound
  

$$
\boxed{v_3(q_n)\le n-8.}
$$


- The odd-prime unique-last-term implication for A3, conditional on a unit **exact raw** $V_N$.

These are author proofs, not claimed independent computational certifications. No finite calculation is used to prove an infinite assertion.

The whole-error asymptotic retains the supplied proportional theorem’s dependency boundary.

## (2) Exact remaining bottleneck

The fixed-$3$ growing-dimension saturation problem now has a linear actual-denominator upper bound. It does **not** control the other primes.

The remaining arithmetic requirement for this proportional center is an upper bound on the same-index sum


$$
\sum_{p\ne3}v_p(q_n)\log p
$$


strong enough that the total


$$
\log q_n
=
\log\frac t\alpha+
\log\frac{k}{\gcd(k,|r|)}
$$


lies strictly below


$$
\left(2+\frac1{2001}\right)\log(1+\sqrt2)\,n
$$


on an unbounded sequence.

For A3, the remaining local premise is a proved supply of indices with the required valuation of the **raw** $V_N$. Its filtered whole-error nonvanishing remains a separate gap.

No irrationality or rationality conclusion for $e+\pi$ follows.

## (3) Bounded exact computation request

If the coordinator elects to arrange an independent audit, I request only these two family indices:


$$
(a,n,b)=(1,6003,3),\qquad(2,18009,9).
$$



Using the defining coefficient formulas (1.3), (1.8), and (1.9), and exact divided-column arithmetic, the expected verifiable outputs are:

1. $\widetilde N\bmod9$, confirming the Pascal matrix.
2. The first three entries of $y\bmod9$, and $y_{b-1}\bmod3$.
3. The full weighted vectors
   

$$
\operatorname{diag}(\omega_j)z\bmod9,\qquad
   \operatorname{diag}(\omega_j)v\bmod9.
$$


4. The receipts
   

$$
\mathfrak D\equiv6J_0^2\pmod9,\qquad
   \operatorname{diag}(\omega_j)v\equiv0\pmod9.
$$


5. Optionally, $\mathfrak C\bmod81$. If this resolves $\chi<4$, then output the exact resulting
   

$$
v_3(q_n)=2F_n+1-\chi
$$


   and the corresponding final-gcd valuation from (7.3), explicitly retaining the least lift-denominator depth $d$.

This is a bounded normalization audit. It is not needed for the infinite proof, and its output would not establish the missing aggregate prime budget.
