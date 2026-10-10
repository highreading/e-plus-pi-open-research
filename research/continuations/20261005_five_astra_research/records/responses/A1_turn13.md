> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## A1 audit and next-digit reduction

The clean modulo-$27$ law passes. The radical calculation also passes **from A4’s displayed first-LOW formula**, including its two cancellations. However, the documents supplied here do not independently establish the deep endpoint estimate used to obtain that formula, or the normalization identities used for the claimed final-gcd bound. Those dependencies must remain explicit.

For the next digit, I obtain fixed rational-polynomial contractions for the **unprojected norm and mixed scalar modulo $81$**, together with an exact reduction of the missing projection correction to one scalar over $\mathbb F_3$. This is useful progress, but **not a completed modulo-$81$ polynomial-ray theorem**: the remaining scalar and the lower factorial tail have not been evaluated.

### 1. Clean law: signs and index domain

Take


$$
j=3u,\qquad u\ge1,\qquad
N=4^j,\quad n=N+1,\quad M=(N-1)/3=3T.
$$


Using the supplied coefficient certificate,


$$
\mathcal H(3T)\equiv4+9T,\qquad
\mathcal G(3T)\equiv2+9T\pmod{27}.
$$


Then


$$
(4+9T)^{-1}\equiv7-36T\pmod{27},
$$


and hence


$$
\Theta\equiv(7-36T)(2+9T)
\equiv14+18T\pmod{27}.
$$


Since $N=1+9T$,


$$
N\Theta\equiv14+9T\pmod{27}.
$$


The previously derived ray therefore becomes


$$
Q^{\rm loc}(y)
\equiv(y+1)(y-1)^{n-2}(3y+10-9T)\pmod{27}.
$$


Finally,


$$
4^{3u}=64^u=(1+63)^u\equiv1+9u\pmod{27},
$$


so $T\equiv u\pmod3$. Thus the clean law is


$$
\boxed{
Q^{\rm loc}(y)\equiv
(y+1)(y-1)^{n-2}(3y+10-9u)\pmod{27},
\qquad j=3u,\ u\ge1.
}
$$


In particular, on $9\mid j$, the last factor is $3y+10$.

This conclusion uses the supplied symbolic coefficient certificate and the inherited polynomial-tail and endpoint bounds; it is not an independent re-execution of that certificate. For literal entries of the actual primitive polynomial,


$$
\boxed{Q_n=\lambda Q^{\rm loc},\qquad \lambda=L_n/3\in\mathbb Z_3^\times.}
$$



### 2. Audit of the actual second radical

Write $A=n-2$, $H=3^{h-1}$, $D=H-A$, and


$$
d=\frac{3D}{2}-1,\qquad
m=\frac{A+1}{2},\qquad
\nu=\frac D2-1.
$$


The audit concerns A4’s stated domain $h\ge5$, $0<D<H/6$, with positive radical dimension.

#### Complete rational functional

The correct functional is


$$
-\mathfrak f(F)+4\sum_{v\ge0}\frac{[y^v]C_F}{2v+1},
\qquad
\mathfrak f(y^s)=(2s)!,\qquad
C_F=\frac{F-F(-1)}{y+1}.
$$


It is not the derangement functional. Since $\deg C_F\le2n-2$, the cutoff $2v+1\le4n-3$ is correct. Sorting these denominators by their exact $3$-valuation proves A4’s all-pole formula. Its factorial term vanishes modulo $9$ after LOW division when $h\ge3$.

The endpoint subtraction remains part of this exact formula. Its later removal requires the separately cited deep endpoint estimate.

#### Basis and HIGH correction

The polynomials


$$
1,y,\ldots,y^{D-1},\quad z_0,\ldots,z_{\nu-1},
\qquad z_i=y^i(y-1)^D,
$$


have consecutive degrees $0,\ldots,d-1$, all with leading coefficient one. Their coefficient matrix is triangular with determinant one: this is an actual integral unimodular basis.

Modulo $3$,


$$
(y-1)^Az_i=y^i(y^H-1).
$$


Because


$$
i+j\le\nu-1+m=(H-3)/2<(H-1)/2,
$$


the coefficient part of the LOW–HIGH coupling vanishes after contraction by $Z$. Only the specified corner survives:


$$
Z^T\bar X=e_{\nu-1}e_m^T.
$$


The HIGH matrix is anti-triangular with unit anti-diagonal at $i+j=d+m$. Its inverse vanishes for $i+j>d+m$, so


$$
(\bar E^{-1})_{mm}=0.
$$


Consequently,


$$
Z^T\bar X\bar E^{-1}\bar X^TZ=0.
$$


This cancellation is valid; it does not discard a potentially nonzero Schur term without evaluation.

#### Pole cancellation and next form

Put $B_{ij}=y^{i+j}(y-1)^D$. Then


$$
(y-1)^Az_iz_j=(y^H-1)B_{ij}\pmod3,
\qquad \deg B_{ij}\le2D-4<H/3.
$$


The $a=1$ and $a=7$ pole indices differ by $H$, and their unit weights agree modulo $3$. Their contributions cancel. The $a=5,11$ indices miss both coefficient ranges.

For $H\ge3$ a power of $3$,


$$
(y-1)^H\equiv y^H-1+3y^{H/3}-3y^{2H/3}\pmod9.
$$


The range $0<D<H/6$ leaves only the $3y^{H/3}$ contribution at the required coefficient. Therefore, **conditional on A4’s first-LOW formula**, its next form is indeed


$$
\boxed{
W_{ij}=[y^{(H/3-1)/2-i-j}](y-1)^D\pmod3,
\quad 0\le i,j<\nu.
}
$$


If $D<H/12$, the target degree exceeds $\deg B_{ij}$, proving $W=0$.

The endpoint restriction is


$$
z_i(-1)=(-1)^i(-2)^D\equiv(-1)^i\pmod3,
$$


so it is nonzero when $\nu>0$. This does **not** by itself prove a distinguished cofactor has exact valuation.

The Smith-factor implications


$$
v_3(\det S)\ge2\nu,\qquad
v_3(\operatorname{adj}(S)_{00})\ge2\nu-2
$$


follow. The claimed


$$
v_3(g)\ge d+2\nu
$$


additionally uses normalization formulas not displayed in these sources; I cannot upgrade that claim to an independently audited final-gcd theorem.

### 3. New bounded lemma: the block factorial quotient modulo $243$

Let $a=b+c$, with $b,c\ge0$. Then


$$
\boxed{
\binom{3a}{3b}\equiv
\binom ab\left[
1+\frac92abc+
\frac{81}{8}abc\bigl(abc-b^2-bc-c^2+1\bigr)
\right]\pmod{243}.
}
\tag{1}
$$



**Proof.** Set


$$
U(a)=\prod_{r=0}^{a-1}(3r+1)(3r+2)
=2^a\prod_{r=0}^{a-1}\left(1+\frac92r(r+1)\right).
$$


Products involving three of the $9$-terms vanish modulo $243$. With


$$
S(a)=\sum_{r<a}r(r+1)=\frac{a(a^2-1)}3,\qquad
V(a)=\sum_{r<a}r^2(r+1)^2,
$$


the quotient expansion gives


$$
\frac{U(a)}{U(b)U(c)}
\equiv
1+\frac92\Delta S+
\frac{81}{8}\bigl((\Delta S)^2-\Delta V\bigr)\pmod{243}.
$$


Here


$$
\Delta S=abc,
$$


and, using $V(a)=(3a^5-5a^3+2a)/15$,


$$
\Delta V=abc(b^2+bc+c^2-1).
$$


Separating multiples of $3$ in the factorials proves (1). All inversions in this argument are of $3$-adic units. ∎

This provides a proved next-digit building block without invoking an unevaluated prime-power binomial formula.

### 4. Explicit raw contractions modulo $81$

Use the established contraction operator $\mathscr C_M$, defined on monomials by


$$
\mathscr C_M(D^aE^b)=
\sum_{t=0}^{\min(a,b)}C_{a,t}(M)C_{b,t}(M),
$$




$$
C_{a,t}(M)=
\sum_{h=t}^{a}
\left\{\begin{matrix}a\\h\end{matrix}\right\}
(M)_h\binom ht.
$$


Its exact identity holds for every integer $M\ge0$.

Define


$$
f_{12}(s)=\sum_{\ell=0}^{11}
\frac{(-1)^\ell}{2^\ell\ell!}(s)_\ell(s+1)^{\overline\ell},
\qquad
A_2(t)=1-9t+81\binom t2,
$$


and


$$
\begin{aligned}
F_0(t)&=4f_{12}(3t)-8(3t+1)f_{12}(3t+1)\\
&\quad+4(3t+1)(3t+2)f_{12}(3t+2),\\
F_1(t)&=-8f_{12}(3t+1)+16(3t+2)f_{12}(3t+2)\\
&\quad-8(3t+2)(3t+3)f_{12}(3t+3).
\end{aligned}
$$


Put $E_0^*=A_2F_0/3$, $E_1^*=A_2F_1$. The exact moment truncation gives


$$
E_0^*(t)\equiv e_{3t}/3\pmod{81},\qquad
E_1^*(t)\equiv e_{3t+1}\pmod{81}.
$$


Indeed, the omitted terms contain a rising factorial of length at least $12$, hence are divisible by $3^5$; also $(-8)^t\equiv A_2(t)\pmod{243}$.

With $t=D+E$, define the fixed polynomials


$$
\boxed{
\mathcal H_*(M)=
\mathscr C_M\left(\left(1+\frac92tDE\right)E_0^*(t)\right),
}
\tag{2}
$$




$$
\boxed{
\begin{aligned}
\mathcal G_*(M)=\mathscr C_M\Bigl(&
[1+3D-9DE+27DE^2\\
&+\tfrac92tDE+\tfrac{27}{2}tD^2E]E_1^*(t)\Bigr).
\end{aligned}
}
\tag{3}
$$


The adjacent factor used in (3) is


$$
\frac{3(D+E)+1}{3E+1}
\equiv1+3D-9DE+27DE^2\pmod{81}.
$$


Multiplication by (1) modulo $81$ gives exactly the displayed bracket, including its surviving cross term.

Thus, for the inherited raw norm and mixed contractions,


$$
\boxed{R/3\equiv\mathcal H_*(M),\qquad X\equiv\mathcal G_*(M)\pmod{81}.}
\tag{4}
$$


These are genuinely fixed contractions: their respective degrees are at most $29$ and $30$. Their coefficient denominators have $3$-depth at most $5$ and $4$, respectively. Evaluation modulo $81$ is therefore safe using numerator guard moduli $3^9$ and $3^8$, or by exact rational evaluation.

### 5. Precisely what projection still changes

On $3\mid M$, write the established residual divisibilities as


$$
v=9v_0,\qquad w=3w_0.
$$


Define only for identifying the outstanding obstruction


$$
\alpha=v_0^TE^{-1}v_0\pmod3,\qquad
\beta=v_0^TE^{-1}w_0\pmod3.
$$


The exact Schur identities imply


$$
c/3\equiv\mathcal H_*-27\alpha,\qquad
\xi_{\rm last}\equiv\mathcal G_*-27\beta\pmod{81}.
$$


Since $\mathcal H_*\equiv1$ and $\mathcal G_*\equiv2\pmod3$,


$$
\boxed{
\frac{\xi_{\rm last}}{c/3}
\equiv
\mathcal G_*\mathcal H_*^{-1}
+27(2\alpha-\beta)\pmod{81}.
}
\tag{5}
$$


Thus only the **combined projection**


$$
v_0^TE^{-1}(2v_0-w_0)\pmod3
$$


is needed, rather than two independent scalars.

I have not evaluated this combination using the final Pascal blocks. Nor have I proved that every lower factorial term disappears modulo $81$ on $9\mid j$. Equation (5) is consequently an obstruction reduction, not the requested completed ray theorem.

### 6. Primitive normalization and complete error

For integer coefficients $A,B$ obtained by clearing the **complete** determinant pair, retain


$$
g=\gcd(|A|,|B|),\qquad q=\frac{|B|}{g},\qquad
p=-\frac{\operatorname{sgn}(B)A}{g}.
$$


Where $B\ne0$,


$$
q(e+\pi)-p
=\frac{\operatorname{sgn}(B)}g\bigl(A+B(e+\pi)\bigr).
$$


If $A+BS=\ell^k\det H_{\rm complete}$, this is


$$
\frac{\operatorname{sgn}(B)\ell^k}{g}\det H_{\rm complete},
\qquad k=(n+1)/2.
$$


No factorial, arctangent, or period term is removed from this identity. The original construction proves $Q_n(-1)\ne0$; it does not alone prove $B\ne0$. The supplied later responses cite, but do not establish here, the additional regular-family response and whole-error nonvanishing results.

## Closing ledger

1. **New result and proof status.** Proved the modulo-$243$ quotient (1), the bounded raw next-digit contractions (2)–(4), and the combined projection obstruction (5). The clean law passes using the supplied certificate. A4’s radical cancellations pass conditional on its displayed first-LOW formula. No completed modulo-$81$ ray or irrationality proof is claimed.

2. **Exact remaining bottleneck.** Evaluate $v_0^TE^{-1}(2v_0-w_0)\bmod3$, retain or eliminate the modulo-$81$ factorial tail, and verify the deep endpoint precision. Separately, irrationality still requires nonzero **whole primitive errors** tending to zero after the actual final gcd.

3. **Bounded computation request.** Expand (2)–(3), whose degrees are at most $29,30$, and return exact rational coefficients, common-denominator $3$-depths, and the reductions after $M=9V$ modulo $81$. If coefficients are not individually $3$-integral, return exact Newton coefficients with denominator bookkeeping. This evaluates the proved raw contractions only; it must not be labeled a completed projected ray certificate.
