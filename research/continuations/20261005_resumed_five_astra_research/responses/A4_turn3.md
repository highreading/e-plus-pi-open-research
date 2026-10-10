> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 independent audit: terminal Jacobi identities and primitive endpoint arithmetic

## Executive verdict

**Neither audited application proves irrationality or rationality of $e+\pi$.** Within their stated hypotheses, however, the principal new exact identities in both reports pass this audit.

### A1 turn1

The following identities are consistent, with all normalizations and signs retained:

- the monic Jacobi norm and its integral-column normalization;
- the terminal recurrence and differentiation identities;
- the reduction of the three-polynomial Wronskian to $\Phi(X,Y)$;
- the **original monomial-coordinate inverse kernel**, including the divisor $3x-\eta$, the divided-difference sign, and the scalar $2\,3^{2-h}/(\mathfrak aN_m)$;
- the coefficient-content formulas for the inverse and endpoint losses;
- the restricted ternary-digit criterion, on the specified resonant family.

In particular, I find **no failed identity among these exact formulas**. The inverse-kernel formula can be certified directly by a small beta-moment Gram calculation; the precise comparison is specified below.

The scope qualifications matter:

1. The terminal valuations $v_3(\gamma)=10$ and $v_3(\rho)=4$ use $v_3(A)=5$, hence the restricted original family $v_3(j)=4$.
2. The coefficient-unit residues modulo $27$ use sufficiently deep resonance; $t\ge8$ suffices for the displayed replacement $A/3^5\equiv1/4\pmod{27}$.
3. The digit criterion does **not** establish infinitely many endpoint-unit indices.
4. The rank-one perturbation is an artificial counterexample to an inference from precision alone. It is not the actual residual force.

### A3 turn1

The primitive denominator decomposition


$$
\widehat q=\frac{kh|AB|}{FGH}
$$


is correct, including when primes are shared by $h$, $F$, $G$, or the remaining endpoint factors. The proof does not require those factors to be pairwise coprime.

The positive rational nondiagonal metric, its least **positive integer** clearer, primitive integer content, final Gram gcd, and the two sharp condition-number statements also pass, in the explicitly specified normalized geometry.

The outstanding arithmetic obligation is still a theorem about the **actual reduced endpoint data**, not about the size of a metric clearer. No supplied identity proves the required denominator upper bound or eventual nonvanishing of the signed whole error.

No tools, external endpoints, or computations were used in this audit.

---

# Part I. A1: exact terminal Jacobi audit

## 1. Domain and normalization

Retain the original domain


$$
j>0,\qquad 81\mid j,\qquad n=4^j+1,
$$




$$
A=n-2=4^j-1,\qquad m=\frac{A+1}{2},\qquad k=m+1,
$$


together with the original real-window conditions. The terminal valuation assertions under review concern the further family


$$
v_3(j)=4,\qquad v_3(A)=5.
$$



The columns remain the original monomials


$$
1,x,\ldots,x^m.
$$


Set


$$
w(x)=x^{-1/2}(1-x)^A,\qquad
c=-\frac{3^h}{2},\qquad
r=\frac{A+71}{3}>1.
$$


Since $A$ is odd, the core matrix is


$$
G_{ij}=3c\int_0^1 x^{i+j}(x-r)w(x)\,dx,
\qquad 0\le i,j\le m.
\tag{1.1}
$$


It is positive definite over $\mathbb R$: both $c$ and $x-r$ are negative on the integration interval.

Let $p_s$ be monic for $w(x)\,dx$, and put


$$
J_s=\kappa_sp_s,\qquad
\kappa_s=\frac{(s+A+\tfrac12)_s}{s!}.
$$


The formula


$$
J_s(x)=\sum_{j=0}^s
\binom{s+A}{j}\binom{s-\tfrac12}{s-j}
x^j(x-1)^{s-j}
\tag{1.2}
$$


has the claimed leading coefficient and belongs to $\mathbb Z_3[x]$. This integrality does not imply that $\kappa_s$ is a unit.

All zeros of $p_s$ lie in $(0,1)$. Thus the evaluations at $r>1$ and at $-1$ used below are nonzero. In particular,


$$
a_s=\frac{p_{s+1}(r)}{p_s(r)}>0.
$$



I reuse the previously accepted polar laws at their stated scope; I do not repeat the moving-base theorem application.

---

## 2. Norm normalization: exact check

The monic norm is


$$
h_s=
\frac{
s!\,\Gamma(s+\tfrac12)\Gamma(s+A+1)\Gamma(s+A+\tfrac12)
}{
(2s+A+\tfrac12)\Gamma(2s+A+\tfrac12)^2
}.
\tag{2.1}
$$


Using the half-integer gamma formula gives


$$
h_s=
\frac{
2\,4^{2s+A}(2s)!(2s+2A)!((2s+A)!)^2
}{
(4s+2A+1)((4s+2A)!)^2
}.
\tag{2.2}
$$


At $2m=A+1$, this is


$$
\boxed{
h_m=
\frac{
2^{4A+3}(A+1)!(3A+1)!((2A+1)!)^2
}{
(4A+3)((4A+2)!)^2
}.
}
\tag{2.3}
$$



There is no missing beta normalization.

For $9\mid A$, the already audited Legendre reduction yields


$$
v_3(h_m)=s_3(4A)-s_3(2A)-s_3(A)-1.
\tag{2.4}
$$


The actual integral Jacobi norm is


$$
\kappa_m^2h_m
=
\frac{\Gamma(m+\tfrac12)\Gamma(m+A+1)}
{(2m+A+\tfrac12)m!\Gamma(m+A+\tfrac12)}.
\tag{2.5}
$$



Writing


$$
U(m)=\frac{\binom{6m}{3m}}{\binom{2m}{m}},
$$


direct factorial cancellation gives


$$
\boxed{
9\kappa_m^2h_m
=
N_m=
\frac{2^{2A+3}(3A+2)}
{(A+1)((4A+3)/3)U(m)}.
}
\tag{2.6}
$$


The factorial valuation identity for multiplication of an argument by $3$ gives $v_3(U(m))=0$. The corresponding factorial-unit cancellation gives $U(m)\equiv1\pmod3$. Consequently, for odd $A$ divisible by $9$,


$$
N_m\in\mathbb Z_3^\times,\qquad N_m\equiv1\pmod3,
$$


and


$$
v_3(\kappa_m^2h_m)=-2.
\tag{2.7}
$$



Combining (2.4) and (2.7),


$$
\boxed{
e_m:=v_3(\kappa_m)
=\frac{s_3(A)+s_3(2A)-s_3(4A)-1}{2},
\qquad
v_3(h_m)=-2-2e_m.
}
\tag{2.8}
$$



**Verdict:** the norm identities pass. In particular, one must not add a second monic-normalization loss after using $N_m$.

---

## 3. Recurrence and differentiation signs

Write


$$
P=p_m,\qquad Q=p_{m+1},\qquad U=p_{m-1}.
$$


The monic recurrence is


$$
Q=(x-\beta)P-\gamma U,
$$


where


$$
\beta=\frac{3(2A^2+4A+1)}{(4A+1)(4A+5)},
$$




$$
\gamma=
\frac{3A^2(A+1)(3A+1)}
{(4A+1)^2(4A-1)(4A+3)}.
\tag{3.1}
$$


For $v_3(A)=5$,


$$
v_3(\beta)=1,\qquad v_3(\gamma)=10.
$$



The leading-coefficient ratio is


$$
\frac{\kappa_m}{\kappa_{m-1}}
=\frac{(4A-1)(4A+1)}{3A(A+1)},
$$


so


$$
\boxed{
\rho=\gamma\frac{\kappa_m}{\kappa_{m-1}}
=\frac{A(3A+1)}{(4A+1)(4A+3)},
\qquad v_3(\rho)=4.
}
\tag{3.2}
$$


The drop from depth $10$ to depth $4$ is real.

For a direct sign check, define


$$
z=\frac{4A+1}{2},\qquad
e=\frac{(A+1)(3A+1)}{2(4A+1)}.
$$


The relevant lowering and raising identities can be written


$$
x(1-x)P'=(-mx+e)P+(z+1)\gamma U,
\tag{3.3}
$$




$$
x(1-x)U'
=\bigl((m+A-\tfrac12)x+\tfrac12-e\bigr)U-(z-1)P.
\tag{3.4}
$$


Subtracting the products with $U$ and $P$, respectively, and evaluating at $-1$, where $x(1-x)=-2$, gives


$$
\boxed{
W(P,U)(-1)
=-\frac12\left[
(z+1)\gamma U(-1)^2
+(2A+2e)P(-1)U(-1)
+(z-1)P(-1)^2
\right],
}
\tag{3.5}
$$


for


$$
W(f,g)=f'g-g'f.
$$



This proves the source’s differentiation formula with its exact sign.

---

## 4. Three-polynomial Wronskian reduction

Let


$$
a=a_m,\qquad
F_m=Q-aP,\qquad
F_{m+1}=p_{m+2}-a_{m+1}Q.
$$


Write the next recurrence as


$$
p_{m+2}=(x-\beta_{m+1})Q-\gamma_{m+1}P.
$$


Evaluation at $r$ gives


$$
a_{m+1}=r-\beta_{m+1}-\frac{\gamma_{m+1}}a.
$$


Therefore


$$
F_{m+1}=(x-r)Q+\frac{\gamma_{m+1}}aF_m.
\tag{4.1}
$$


The second term drops out of $W(F_{m+1},F_m)$, but only after this exact identity has retained the full correction. Thus


$$
W(F_{m+1},F_m)
=QF_m+(x-r)W(Q,F_m)
=Q^2-aPQ-a(x-r)W(Q,P).
$$


At $-1$,


$$
\boxed{
\mathcal W(-1)=Q(-1)^2-aP(-1)Q(-1)
+a(r+1)W(Q,P)(-1).
}
\tag{4.2}
$$



This independently confirms the source’s plus sign in the last term.

Set


$$
X=J_m(-1),\qquad Y=J_{m-1}(-1),\qquad
q_0=-1-\beta,
$$




$$
\mathfrak a=a/3,\qquad
k_0=a(r+1)=\mathfrak a(A+74),\qquad B_0=2A+2e.
$$


I use $k_0,B_0$ here only to avoid confusing these terminal scalars with dimensions and endpoint arithmetic below.

Since


$$
W(Q,P)=P^2+\gamma W(P,U),
$$


substitution proves


$$
\boxed{
\mathcal W(-1)=\kappa_m^{-2}\Phi(X,Y),
}
$$


where


$$
\Phi=CX^2+\rho DXY+\rho^2EY^2,
\tag{4.3}
$$




$$
C=q_0^2-aq_0+k_0-\frac{k_0\gamma(z-1)}2,
$$




$$
D=a-2q_0-\frac{k_0B_0}{2},
\qquad
E=1-\frac{k_0(z+1)}2.
\tag{4.4}
$$



The three-polynomial reduction therefore passes.

### Coefficient valuations and scope

At the accepted polar unit


$$
\mathfrak a\equiv25\pmod{27}
$$


and sufficiently deep resonance,


$$
\frac C3\equiv7\pmod9,\qquad
\frac{\rho}{3^4}\equiv7\pmod{27},\qquad
D\equiv1\pmod{27},\qquad E\equiv4\pmod{27}.
\tag{4.5}
$$


For example, reducing $A$ modulo $27$ gives


$$
q_0\equiv-\frac85,\qquad B_0\equiv1,\qquad
k_0\equiv74\mathfrak a,
$$


so the low part of $C$ is exactly


$$
\frac{64}{25}+\frac{394}{5}\mathfrak a.
$$


The term involving $\gamma$ has valuation at least $10$ and does not change the displayed residue.

The normalized $\rho$-residue modulo $27$ uses


$$
A/3^5\equiv1/4\pmod{27};
$$


with $A=(243+\epsilon)/4$, this follows from $v_3(\epsilon)\ge8$. This is compatible with the source’s “sufficiently large” family, but should not be attributed merely to $t\ge7$.

The coefficient depths are consequently $1,4,8$. If $x=v_3(X)$ and $y=v_3(Y)$, the only ties for the smallest valuation occur at


$$
x-y=3,\qquad x-y=4.
$$


The source’s two noncancellation branches and its two $3$-adic root depths follow exactly.

---

## 5. Original monomial inverse kernel: decisive derivation

This is the most important normalization check.

Define


$$
q_m(x)=\frac{Q(x)-aP(x)}{x-r}.
$$


Its norm for $3(x-r)w(x)\,dx$ is


$$
-3ah_m.
$$


For the matrix (1.1), the Christoffel–Darboux kernel is therefore


$$
K_G(x,y)
=
-\frac1{3cah_m}
\frac{q_{m+1}(x)q_m(y)-q_m(x)q_{m+1}(y)}{x-y}.
\tag{5.1}
$$


Here


$$
K_G(x,y)=\sum_{i,j=0}^m(G^{-1})_{ij}x^iy^j
$$


is literally the inverse in the original monomial coordinates.

By (4.1),


$$
q_{m+1}=Q+\frac{\gamma_{m+1}}a q_m.
$$


The added multiple cancels in (5.1). Using


$$
Q=(x-r)q_m+aP,
$$


the divided difference becomes


$$
q_m(x)q_m(y)
+a\frac{P(x)q_m(y)-q_m(x)P(y)}{x-y}.
\tag{5.2}
$$



Now let $\eta=A+71$ and


$$
\widehat Q=\kappa_m Q,\qquad
Z=\frac{\widehat Q-aJ_m}{3x-\eta}.
$$


Since


$$
3x-\eta=3(x-r),
$$


one has


$$
\boxed{q_m=3Z/\kappa_m,}
\tag{5.3}
$$


not $Z/\kappa_m$.

For the actual family, $3\nmid\eta$. The numerator belongs to $\mathbb Z_3[x]$, it is divisible by $3x-\eta$ over $\mathbb Q_3[x]$, and this divisor is primitive over $\mathbb Z_3$. Gauss content therefore gives


$$
Z\in\mathbb Z_3[x].
$$



Substituting (5.3) into (5.2) gives


$$
\frac9{\kappa_m^2}
\left[
Z(x)Z(y)+\mathfrak a
\frac{J_m(x)Z(y)-Z(x)J_m(y)}{x-y}
\right].
$$


Thus, with the source’s definition of $\mathcal E$,


$$
K_G(x,y)
=-\frac3{cah_m\kappa_m^2}\mathcal E(x,y).
$$


Finally $c=-3^h/2$, $a=3\mathfrak a$, and
$h_m\kappa_m^2=N_m/9$, so


$$
\boxed{
K_G(x,y)
=\frac{2\,3^{2-h}}{\mathfrak aN_m}\mathcal E(x,y).
}
\tag{5.4}
$$



**Both the scalar and the divided-difference sign are correct.**

At the diagonal,


$$
\mathcal E(x,x)
=Z(x)^2+\mathfrak a\bigl(J_m'(x)Z(x)-Z'(x)J_m(x)\bigr).
$$


Consequently,


$$
\boxed{
\mathcal E(-1,-1)=\frac{\Phi(X,Y)}{(A+74)^2}.
}
\tag{5.5}
$$


This yields


$$
\boxed{
v^TG^{-1}v
=\frac{2\,3^{2-h}}{\mathfrak aN_m(A+74)^2}\Phi(X,Y),
\quad v_i=(-1)^i.
}
\tag{5.6}
$$



An omission of the $3$ in (5.3), a reversal of the divided difference, or use of a probability-normalized weight would fail these identities. None of those mistakes occurs in the supplied formula.

---

## 6. Coefficient and endpoint losses

Because the scalar in (5.4) has valuation $2-h$,


$$
L=\max\{0,h-2-\operatorname{cont}_3\mathcal E(x,y)\},
$$




$$
\mu=2-h+\operatorname{cont}_3\mathcal E(x,-1).
\tag{6.1}
$$


These are original-coordinate statements.

Modulo $3$, the actual hypotheses give


$$
\widehat Q\equiv xJ_m,\qquad
3x-\eta\equiv1,\qquad \mathfrak a\equiv1.
$$


Therefore


$$
Z\equiv xJ_m
$$


and


$$
\boxed{
\mathcal E(x,y)\equiv(xy-1)J_m(x)J_m(y)\pmod3.
}
\tag{6.2}
$$


In particular, if $X=J_m(-1)$ is a unit, then


$$
\mathcal E(x,-1)\equiv(-x-1)J_m(x)X\not\equiv0.
$$


Both contents in (6.1) are zero. For the large indices under discussion,


$$
\boxed{
L=h-2,\qquad \mu=2-h,\qquad
v_3(v^TG^{-1}v)=3-h.
}
\tag{6.3}
$$



There is no inconsistency between the zero endpoint-column content and the extra factor $3$ in the endpoint contraction: substituting $x=-1$ into (6.2) makes $xy-1$ vanish.

The two sufficient transfer conditions with precision $6$ require


$$
h<8,\qquad h<7,
$$


respectively. They fail on the large family.

---

## 7. Restricted ternary-digit criterion

The coefficient identity


$$
(-1)^nJ_n(-1)
=[z^n](1+z)^{3n-1}(1-z)^{n-1/2}
$$


is valid modulo $3$ when $A=2n-1$. With


$$
F=(1+z)^3(1-z),\qquad
A_0=(1+z)^{-1}(1-z)^{-1/2},
$$


one has


$$
A_0(z)=G(z)A_0(z^3),\qquad G=(1+z)^2(1-z).
$$


The Cartier transition


$$
H_S(3q+d)=H_{\mathcal C_d(SGF^d)}(q)
\tag{7.1}
$$


follows by extracting coefficients after separating the factor depending on $z^3$.

The transitions used by the source are correct:


$$
\mathcal C_2(GF^2)=G,
$$


and, with $U=1+z$, $V=(1+z)^2$,


$$
\begin{array}{c|ccc}
S&0&1&2\\ \hline
G&V&G&\text{unused}\\
U&U&V&0\\
V&U&2V&0.
\end{array}
\tag{7.2}
$$



The fixed low ternary digits of $247/8$, read low to high, are


$$
2,1,1,1,\overline{1,0}.
$$


At depth $7$ the state is $2V$, and thereafter the states at odd/even fixed depths alternate as stated. Once the state is a nonzero multiple of $U$ or $V$, a digit $2$ kills it, while digits $0,1$ preserve a nonzero state with nonzero constant term.

Thus, on the specified resonant family and $t\ge7$,


$$
\boxed{
J_m(-1)\in\mathbb Z_3^\times
\iff
m=2^{2j-1}\text{ has no ternary digit }2
\text{ outside its units position}.
}
\tag{7.3}
$$



This is a proof about the whole evaluated value modulo $3$, not a coefficient sample. It establishes no infinitude assertion about the restricted-digit powers.

---

## 8. Actual force versus the artificial perturbation

The actual perturbation remains


$$
\begin{aligned}
\Delta_{ij}={}&-\frac{3^h}{4}\,
\mathfrak f(Q_n^{\rm loc}y^{i+j})\\
&+3^{h+6}
\sum_{\substack{v\ge0\\2v+1\le4n-3}}
\frac{
[y^v]\bigl(Ry^{i+j}-(-1)^{i+j}R(-1)\bigr)/(y+1)
}{2v+1},
\end{aligned}
\qquad 0\le i,j\le m.
\tag{8.1}
$$


Here $\mathfrak f(y^s)=(2s)!$. Neither line can be dropped.

For the artificial matrix


$$
G^\sharp=G+3^6vv^T,
$$


Sherman–Morrison gives


$$
v^T(G^\sharp)^{-1}v=\frac{K}{1+3^6K},
\qquad K=v^TG^{-1}v.
$$


If $v_3(K)<-6$, the denominator has valuation $6+v_3(K)$, hence


$$
v_3\bigl(v^T(G^\sharp)^{-1}v\bigr)=-6.
\tag{8.2}
$$


This is a valid precision counterexample, including invertibility: $1+3^6K\ne0$ under that valuation hypothesis.

It proves only that the entrywise congruence, even with symmetry and the Hankel pattern, is insufficient. It says nothing by itself about the value produced by (8.1).

A concrete exact follow-on formulation is to evaluate, for the **actual** $\Delta$,


$$
D_\Delta=\det(I+G^{-1}\Delta),
$$




$$
N_\Delta
=v^T\operatorname{adj}(I+G^{-1}\Delta)G^{-1}v.
\tag{8.3}
$$


Whenever $D_\Delta\ne0$,


$$
v^T(G+\Delta)^{-1}v=\frac{N_\Delta}{D_\Delta}.
\tag{8.4}
$$


A structured residual lemma must prove the needed nonvanishing and relative valuations of these two actual quantities, or an equivalent finite Schur-complement pair. This formulation avoids assuming a convergent Neumann expansion when its precision condition fails.

---

# Part II. A3: primitive denominator and metric audit

## 9. Correct all-prime denominator theorem

Assume the two endpoint rows have been reduced:


$$
\gcd(u_0,v_0)=\gcd(u_b,v_b)=1,\qquad u_0u_b\ne0.
$$


Let


$$
u_0=hA,\qquad u_b=hB,\qquad h>0,\qquad\gcd(A,B)=1,
$$


and let $a,k>0$ satisfy


$$
\gcd(a,k)=1.
$$


Define


$$
T=av_0B+(k-a)v_bA,\qquad J=Bv_0-Av_b,
$$




$$
F_A=\gcd(|A|,a),\qquad
F_B=\gcd(|B|,|a-k|),\qquad F=F_AF_B,
$$




$$
G=\gcd(k,|J|),\qquad
H=\gcd\!\left(h,\frac{|T|}{FG}\right).
\tag{9.1}
$$


Then the reduced fraction for $T/(khAB)$ is


$$
\boxed{
\widehat q=\frac{kh|AB|}{FGH},\qquad
\widehat p=\operatorname{sgn}(AB)\frac{T}{FGH}.
}
\tag{9.2}
$$



This is the source’s theorem, with $|a-k|$ making the algebraic statement independent of the eventual $a>k$ specialization.

### Proof, including shared primes

Row primitivity implies


$$
\gcd(A,v_0B)=1,\qquad \gcd(B,v_bA)=1.
$$


Therefore


$$
\gcd(|A|,|T|)=F_A,\qquad
\gcd(|B|,|T|)=F_B,
$$


and


$$
\gcd(|AB|,|T|)=F.
\tag{9.3}
$$


Put


$$
M=|AB|/F,\qquad t_1=T/F.
$$


Then $\gcd(M,t_1)=1$, so


$$
\gcd(kh|AB|,|T|)=F\gcd(kh,|t_1|).
\tag{9.4}
$$



Since $F\mid a(a-k)$ and $\gcd(a,k)=1$,


$$
\gcd(F,k)=1.
$$


Also


$$
T=aJ+kAv_b.
$$


Thus


$$
\gcd(k,|t_1|)=\gcd(k,|T|)=\gcd(k,|J|)=G.
$$


Writing $k=Gk_1$, $t_1=Gt_2$ gives


$$
\gcd(k_1,t_2)=1.
$$


It follows, even when $k_1$ and $h$ share primes, that


$$
\gcd(kh,|t_1|)
=G\gcd(k_1h,|t_2|)
=G\gcd(h,|t_2|)
=GH.
\tag{9.5}
$$


This proves (9.2).

No step assumes $\gcd(F,h)=1$, $\gcd(G,h)=1$, or $\gcd(h,AB)=1$.

Equivalently, for every prime $p$, the final result satisfies the direct check


$$
v_p(\widehat q)
=
\max\{0,\,
v_p(k)+v_p(h)+v_p(A)+v_p(B)-v_p(T)\}.
\tag{9.6}
$$


This is a useful independent certificate of all shared-prime interactions.

The case $T=0$ is also covered using $\gcd(d,0)=d$; it gives $\widehat q=1$, as it must.

### Endpoint row primitivity is essential

Joint primitivity of the full matrix $[U,V]$ does not imply primitivity of either endpoint row. The preliminary divisions by


$$
r_0=\gcd(|U_0|,|V_0|),\qquad
r_b=\gcd(|U_b|,|V_b|)
$$


are therefore necessary. A3 explicitly makes them. Its argument does not silently replace row primitivity by joint primitivity.

The lower bound follows:


$$
\widehat q\ge\frac{|AB|}{F}
\ge\frac{|AB|}{a(a-k)}
\quad(a>k).
\tag{9.7}
$$


It is a structural lower bound, not a denominator-growth theorem for the actual family.

---

## 10. Minor content and resultant claims

The raw endpoint minor is


$$
U_bV_0-U_0V_b=r_0r_bhJ.
$$


If $\delta$ divides every full-column $2\times2$ minor, then


$$
\frac{\delta}{\gcd(\delta,r_0r_bh)}\mid J.
\tag{10.1}
$$


This follows prime by prime and requires no coprimality assumption.

The actual endpoint constraints


$$
\sum_jU_j=0,\qquad \sum_jV_j=d_B
$$


give


$$
\delta\mid d_BU_i\quad\text{for every }i,
$$


hence


$$
\delta\mid d_B\gcd_j|U_j|.
\tag{10.2}
$$


The degree-one resultant has the claimed sign:


$$
\operatorname{Res}_z(hAz-v_0,hBz-v_b)
=h(Bv_0-Av_b)=hJ.
\tag{10.3}
$$



These statements constrain $G$; none determines the remaining shared-denominator gcd $H$.

---

## 11. Positive rational metric and least integral clearer

Let $m=d+2$, with all original coordinates $0,\ldots,b$, and assume every $U_j\ne0$. In the normalized coordinates,


$$
U\mapsto\mathbf1,\qquad V\mapsto c.
$$


For


$$
w=\frac ak e_0+\frac{k-a}{k}e_b,\qquad
\mathbf1^Tw=1,\qquad
P=I-\frac1m\mathbf1\mathbf1^T,
$$


the matrix


$$
B=ww^T+\gamma P,\qquad \gamma>0,
$$


is positive definite because


$$
x^TBx=(w^Tx)^2+\gamma\|Px\|^2
$$


can vanish only at $x=0$. Moreover


$$
B\mathbf1=w,\qquad \mathbf1^TB\mathbf1=1.
$$


Its pullback


$$
W=\operatorname{diag}(U_j^{-1})B\operatorname{diag}(U_j^{-1})
$$


therefore realizes $\widehat c$ exactly on the complete actual lift.

For the optimal fixed-selector choice $\gamma=\|w\|^2$, put


$$
z=ae_0+(k-a)e_b,\qquad Z=z^Tz,
$$




$$
C=mzz^T+Z(mI-\mathbf1\mathbf1^T).
$$


Then


$$
B=C/(mk^2).
$$


There are at least two interior coordinates when $d\ge2$. Their off-diagonal entry is $-Z$; the endpoint entries then show


$$
\gcd(\text{entries of }C)
=\gcd(Z,ma^2,ma(k-a),m(k-a)^2)
=\gcd(Z,m)=c_C.
\tag{11.1}
$$


Thus $C_0=C/c_C$ is primitive integral, and the least positive integer clearer of $B$ is


$$
mk^2/c_C.
$$



For the pullback of $C_0$, the least positive integer clearer is exactly


$$
\boxed{
\ell=\operatorname{lcm}_{0\le i\le j\le b}
\frac{|U_iU_j|}
{\gcd(|U_iU_j|,|(C_0)_{ij}|)}.
}
\tag{11.2}
$$


The resulting $\Omega$ is primitive integral. Indeed, for each prime $p$, primitivity of $C_0$ provides an entry of valuation zero, so the minimum entry valuation after pullback is nonpositive. The least integer clearer shifts that minimum to exactly zero.

The resulting Gram quantities satisfy


$$
\mathcal A=U^T\Omega U=\ell\,\frac{mk^2}{c_C}>0,\qquad
\mathcal H=U^T\Omega V=\mathcal A\widehat c.
$$


Hence


$$
\boxed{
g_{\rm Gram}=\gcd(\mathcal A,|\mathcal H|)
=\frac{\mathcal A}{\widehat q}.
}
\tag{11.3}
$$


The metric clearer creates no new reduced denominator: its forced Gram content leaves precisely (9.2).

---

## 12. Condition numbers

All claims here concern the normalized Euclidean geometry, not the raw coefficient geometry.

For a prescribed $w$ with $\mathbf1^Tw=1$, put


$$
L=m\|w\|^2.
$$


The classical angle inequality gives


$$
\kappa(B)\ge
\bigl(\sqrt L+\sqrt{L-1}\bigr)^2
$$


when $B\mathbf1=w$. The source’s matrix attains it: on the relevant two-dimensional plane, $mB$ is


$$
\begin{pmatrix}
1&t\\ t&1+2t^2
\end{pmatrix},
\qquad t^2=L-1,
$$


with eigenvalues


$$
L\pm\sqrt{L(L-1)}.
$$


The complementary eigenvalues equal $L$. Thus the exact optimum and


$$
\kappa_{\rm endpoint}
=8(d+2)\frac{n^4}{d^2}(1+o(1))
$$


are correct.

For a metric allowed to use the actual rational companion $c$, the minimum-norm admissible vector is


$$
w_*=\frac1m\mathbf1+
\frac{\widehat c-\bar c}{\|c-\bar c\mathbf1\|^2}
(c-\bar c\mathbf1).
$$


It is rational and uses no $S=e+\pi$. Applying the same sharp fixed-vector result gives


$$
\boxed{
\kappa_{\min}
=\bigl(\sqrt{1+\mathcal R}+\sqrt{\mathcal R}\bigr)^2,
\quad
\mathcal R=
m\frac{(\widehat c-\bar c)^2}{\|c-\bar c\mathbf1\|^2}.
}
\tag{12.1}
$$


The exact spread variance


$$
V_s=\frac{d(d+1)(d^2+7d+4)}{12(d+2)}
$$


and the accepted CSC estimates imply, on $2\le d=o(n)$,


$$
\kappa_{\min}
=\frac{4(d+2)n^4}{V_s}(1+o(1)).
$$


For $d\to\infty$, this is


$$
48\,\frac{n^4}{d^2}(1+o(1)).
$$


These deductions do not use the unreviewed common-error expansion in A3 turn0.

---

# Part III. Exact certificates and remaining research obligations

## 13. Bounded beta-moment certificate for A1

A small admissible algebraic test is $A=9$, so $m=5$. One may additionally use $A=27$, $m=14$. These are admissible for the exact odd-$A$, $9\mid A$ identities; they are **not** original resonant indices and do not test infinitude or actual-force transfer.

Take $h=0$ solely for scalar testing, hence $c=-1/2$. Define


$$
\mu_r=B(r+\tfrac12,A+1)
=\frac{A!}{\prod_{j=0}^A(r+j+\tfrac12)},
\qquad 0\le r\le2m+1.
$$


Construct the exact rational matrix


$$
G_{ij}=-\frac32\bigl(\mu_{i+j+1}-r\mu_{i+j}\bigr),
\qquad 0\le i,j\le m,
\quad r=(A+71)/3.
\tag{13.1}
$$



Independently construct $J_s,p_s$ through $s=m+2$, and use the actual


$$
a=p_{m+1}(r)/p_m(r),
$$


not the artificial value $a=75$ used in the separate coefficient-residue certificate.

### Required comparisons

1. **Norm**
   

$$
\sum_{i,j}[x^i]p_m\,[x^j]p_m\,\mu_{i+j}
$$


   versus (2.3).

2. **Christoffel division**
   

$$
(3x-\eta)Z-(\kappa_mp_{m+1}-aJ_m)=0.
$$



3. **Full original-coordinate kernel**  
   If $E_{ij}=[x^iy^j]\mathcal E$, compare
   

$$
\boxed{
   G^{-1}\quad\text{with}\quad
   \frac{18}{\mathfrak aN_m}(E_{ij})_{0\le i,j\le m}.
   }
   \tag{13.2}
$$


   Equivalently, verify that their product with $G$ is the identity matrix.

4. **Endpoint**
   

$$
v^TG^{-1}v
   \quad\text{versus}\quad
   \frac{18\,\Phi(X,Y)}
   {\mathfrak aN_m(A+74)^2}.
$$



5. **Independent Wronskian**
   

$$
\kappa_m^2
   W(F_{m+1},F_m)(-1)-\Phi(X,Y)=0.
$$



**Expected output:** exact zero differences in every scalar and coefficient comparison, and an exact identity matrix in (13.2). No failed identity is predicted by the audit.

The $A=9$ test involves only a $6\times6$ rational matrix and polynomials through degree $7$. It certifies the bounded arithmetic instance, while the derivations above establish the general identities.

---

## 14. Bounded shared-prime certificate for A3

Before generating actual columns, the algebraic gcd theorem can be tested on small endpoint data with deliberate shared primes.

For example, take


$$
a=5,\quad k=2,\quad h=15,\quad A=5,\quad B=3,\quad v_b=1.
$$


The primitive endpoint denominators are $75$ and $45$.



$$
\begin{array}{c|r|r|r|r|r|r|c}
v_0&T&J&F&G&H&\widehat q&\widehat p\\ \hline
2&15&1&15&1&1&30&1\\
4&45&7&15&1&3&10&1\\
7&90&16&15&2&3&5&1\\
1&0&-2&15&2&15&1&0
\end{array}
$$


These entries follow directly from the displayed formulas. They test additional cancellation at primes already appearing in $F$, as well as the $T=0$ case.

To test sharing between $k$ and $h$, use


$$
a=5,\quad k=2,\quad h=8,\quad A=B=1,\quad
v_0=3,\quad v_b=1.
$$


Then


$$
T=12,\quad J=2,\quad F=1,\quad G=2,\quad H=2,
$$


and the result is $3/4$.

These are synthetic algebraic certificates, not samples from the actual contact construction.

For actual columns, the coordinator’s proposed finite records should compare, independently:

- the raw single-gcd reduction of
  

$$
\frac{aV_0U_b+(k-a)V_bU_0}{kU_0U_b};
$$


- the decomposed result (9.2);
- the least clearer (11.2);
- primitive metric content;
- the exact Gram gcd (11.3).

Actual generation must retain


$$
H_b,T:\{0,\ldots,d\}^2,\qquad
K:\{0,\ldots,b\}\times\{0,\ldots,d\}.
$$


No finite successful list proves an infinite denominator bound.

---

## 15. Primitive errors and the exact remaining bottlenecks

### A1 determinant construction

For the actual complete determinant


$$
\det H_{\rm complete}=\beta_0+\beta_1(e+\pi),
$$


retain an actual coefficient clearer $\ell^k$ and the final gcd


$$
g=\gcd(|\ell^k\beta_0|,|\ell^k\beta_1|).
$$


When $\beta_1\ne0$,


$$
q=\frac{|\ell^k\beta_1|}{g},\qquad
p=-\frac{\operatorname{sgn}(\beta_1)\ell^k\beta_0}{g},
$$


and


$$
\boxed{
q(e+\pi)-p
=\frac{\operatorname{sgn}(\beta_1)\ell^k}{g}
\det H_{\rm complete}.
}
\tag{15.1}
$$


The actual polynomial multiplier $\lambda_n$ must be restored in exact matrix and endpoint values.

The audited core identities establish neither $\beta_1\ne0$ nor decay and nonvanishing of (15.1).

### A3 signed extrapolation

With the primitive Gram pair,


$$
\boxed{
\widehat q(e+\pi)-\widehat p
=
\frac{d_B^2}{g_{\rm Gram}}
\left[(u^T\Omega u)(e+\pi)-u^T\Omega v\right]
=\widehat q\bigl((e+\pi)-\widehat c\bigr).
}
\tag{15.2}
$$


The complete evaluated error includes


$$
\begin{aligned}
\widehat c-(e+\pi)
={}&(-1)^{n+1}
\left[\lambda\frac{F_0}{P_0}+(1-\lambda)\frac{F_b}{P_b}\right]\\
&+\lambda\frac{E_0}{P_0}
+(1-\lambda)\frac{E_b}{P_b}
+(-1)^n\lambda\frac{D}{P_0},
\end{aligned}
$$


where $\lambda=n^2/d$ and $E_j$ retains the complete exponential insertion. Its accepted bound yields


$$
|\widehat q(e+\pi)-\widehat p|
\le
C\frac{kh|AB|}{FGH}M^{-2n-b}
\left(\frac{d+1}{n}+\frac{n^2}{d}e^{-\kappa n}\right).
\tag{15.3}
$$



The useful follow-on arithmetic lemma remains:

> On an infinite admissible sublinear sequence, prove a divisor $h_0\mid h$ satisfying
> 

$$
> T\equiv0\pmod{FGh_0},
>
$$


> and an upper bound for the resulting cofactor strong enough to make the right side of (15.3) tend to zero. Also prove unbounded reduced denominators, suitable nonconstancy, or another valid whole-error nonvanishing statement.

The row reductions and the exact divisions by $F,G$ must precede this congruence. Raw minor divisibility cannot replace it.

---

## Final ledger

### Results established by this audit

1. A1’s norm, recurrence, differentiation, three-polynomial Wronskian, original monomial inverse kernel, and endpoint normalization are mutually consistent and have explicit derivations.
2. The endpoint-unit branch has exactly the stated losses and precision obstruction.
3. The restricted ternary-digit criterion is valid at its stated resonant scope, without an infinitude conclusion.
4. A3’s primitive denominator formula survives all shared-prime interactions and the zero-numerator edge case.
5. The positive rational metric, least integral clearer, primitive metric content, final Gram gcd, and normalized-geometry conditioning claims are valid.

### Exact unresolved bottlenecks

- **A1:** evaluate the complete actual residual transport, including invertibility and actual endpoint response; the artificial rank-one example cannot answer that question.
- **A3:** control the actual shared endpoint cancellation and global cofactor after the final gcd, together with nonvanishing of the signed whole error.
- **Globally:** obtain an infinite original-index sequence of integer pairs satisfying
  

$$
0<|q(e+\pi)-p|\longrightarrow0.
$$



The bounded calculations above would provide exact implementation certificates, not those missing infinite results.



$$
\boxed{\text{The irrationality or rationality of }e+\pi\text{ remains unresolved.}}
$$


