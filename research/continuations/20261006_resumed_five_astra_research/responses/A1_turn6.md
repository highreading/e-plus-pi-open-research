> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1turn6 — Suffix synchronization closes the deep-family collision question; the remaining target is the complete scalar response

## Executive conclusions

The new suffix proposal contains a valid and substantially stronger digit argument. Its principal conclusion is not limited to the sampled powers:



$$
\boxed{
m\equiv851\pmod{6561}
\quad\Longrightarrow\quad
\operatorname{cont}_3(J_m)=\operatorname{cont}_3(J_{m-1}),
}
$$


where both polynomials retain the parameter $A=2m-1$.

The constructive policy is also valid. There is one small repair to its statement: the prefix and suffix can overlap in **one** digit. In that case the middle length is $-1$, the content is zero, and the proposed final inequality still holds. Larger overlaps are impossible on the sufficiently large fixed real window.

Consequently, on original tuples for which the retained actual unit normalization is established,


$$
\boxed{
t=v_3(8m-247)\ge9
\quad\Longrightarrow\quad
\operatorname{cont}_3(\mathcal E)=2r,\qquad
s_c\ge t+23\ge32.
}
$$


Here $r=\operatorname{cont}_3(J_m)$. Thus the condition $s_c<32$ is excluded on that branch.

**An essential scope qualification remains:** the supplied proof of the Christoffel unit applies to the sufficiently deep, controlled-growth resonant family. It does not establish the same unit valuation for every arbitrarily large power having a specified resonance depth. The digit theorem is universal on its congruence; the normalized inverse conclusion is universal only where its normalization hypotheses hold. On the constructed original family those hypotheses are available, so the exclusion is unconditional there.

The checked Matveev text input closes the fixed-real-window reachability dependency. Below I give an explicit interval and an arithmetic-progression hitting argument, without claiming another PDF inspection or requiring a new source search.

For the subsequent direct method, I derive:

1. an exact whole-scalar variation identity that requires **no small worst-case core inverse loss**;
2. the actual derivative pairing with the full producer remainder;
3. an exact finite pole-pair cancellation for the saturated residual pairing, retaining every $\Delta_H$ coefficient and both cutoff boundaries.

These are rigorous reductions and cancellation results. They do not yet evaluate the actual cofactor pair or prove primitive-error decay.

---

## 1. Domain and notation

Throughout the original family,


$$
j>0,\qquad j\equiv81\pmod{243},\qquad
m=2^{2j-1},\qquad A=2m-1=4^j-1,
$$




$$
L=h-1,\qquad H=3^L,\qquad D=H-A,
$$


and


$$
a_*:=\frac1{2C_{16}}<\frac DH<\frac1{C_{16}}=:b_*,
\qquad C_{16}=147968\,3^{15}.
$$



In this report,


$$
t=v_3(8m-247)=v_3(4^{j+1}-247).
$$


This is **not** the quantity denoted $t=v_3(A)=5$ in A1_turn13. Keeping these two depths distinct is necessary.

The Jacobi degrees and binomial upper indices are:



$$
\begin{array}{c|ccc}
&\text{degree}&\text{integral upper index}&\text{half-integral upper index}\\ \hline
J_m&m&3m-1&m-\tfrac12\\
J_{m-1}&m-1&3m-2&m-\tfrac32.
\end{array}
$$



In particular, the integral upper index is not the degree. Their high streams must be compared separately.

---

## 2. Exact suffix synchronization

### 2.1 What the finite certificate establishes

The eight-state recurrence in the supplied program is exactly the established Lucas–Kummer recurrence:



$$
k_i+r_i+c=d_i+3c',
$$




$$
b'=\mathbf1_{\{N_i-k_i-b<0\}},\qquad
e'=\mathbf1_{\{\alpha_i-r_i-e<0\}},
$$


with transition cost $b'+e'$.

Thus a complete evaluation of its first eight transitions is a finite exact arithmetic proof of the corresponding eight-digit identity. It is not a proof about arbitrary future digits until the future inputs and terminal rules have also been identified.

I accept the personally certified finite identity, at precisely that scope:


$$
(0,\infty,\infty,\infty,\infty,1,1,3)
\tag{2.1}
$$


is the state-cost vector for both columns after eight digits at residue $851$. The program uses the stated state order and does not replace polynomial content by an endpoint evaluation. No repetition of that computation is needed.

### 2.2 The future streams agree exactly

Write


$$
m=851+6561M,\qquad M\ge0.
$$


Then


$$
m-1=850+6561M,
$$




$$
3m-1=2552+6561(3M),\qquad
3m-2=2551+6561(3M).
$$



For the half-integral indices, the exact decompositions are


$$
m-\frac12=4131+6561\left(M-\frac12\right),
$$




$$
m-\frac32=4130+6561\left(M-\frac12\right).
\tag{2.2}
$$



Therefore, after eight digits, both evaluators have:

- remaining degree stream $M$;
- remaining integral-upper stream $3M$;
- remaining half-integral-upper stream $M-\tfrac12$.

The state vector already carries every incoming addition carry and both incoming borrows. There is no further hidden dependence on the discarded low digits.

### 2.3 Terminal rules

The allowed integer variables satisfy $k+r=s$, where $s$ is the actual degree. Beyond the finite degree stream, their digits must be zero. An incoming addition carry cannot be accepted indefinitely against a zero degree stream.

The integral upper stream becomes zero after its finite last digit. The half-integral upper stream is eventually all ones. With forced zero digits for $k,r$, an incoming half-borrow clears at an eventual digit one. Acceptance requires final carry and both borrows zero.

These rules are identical for the common streams in §2.2, including $M=0$. Hence equal vectors in (2.1) produce equal final minima.

### Theorem 2.1 — Universal synchronization

For every integer $M\ge0$,


$$
\boxed{
\operatorname{cont}_3(J_{851+6561M})
=
\operatorname{cont}_3(J_{850+6561M}),
}
\tag{2.3}
$$


with common Jacobi parameter $A=2(851+6561M)-1$.

This is a universal theorem obtained from a finite transition identity and an exact common-tail proof. The additional 81 complete integers corroborate it but are not needed to extend its scope.

---

## 3. Uniform zero-cost suffix and constructive middle policy

### 3.1 The low suffix for every depth

The low-to-high expansion is


$$
247/8=(2,1,1,1,1,0,1,0,1,0,\ldots)_3.
\tag{3.1}
$$



For $J_m$, the zero-cost path described in A1_turn5 starts with


$$
(k_0,r_0)=(2,0),
$$


continues through the initial ones with $(1,0)$, and reaches half-carry $q=0$ at position $5$, whose digit is zero. Thereafter, on the fixed $0/1$ suffix, choosing $k_i=0,\ r_i=m_i$ preserves zero addition carry and both zero borrows.

For $J_{m-1}$, its units digit is one; the initial choice $(1,0)$, followed by $(0,m_i)$, gives the corresponding zero-cost path.

Thus for every $t\ge6$, both paths leave the prescribed first $t$ digits with


$$
(c,b,e,q)=(0,0,0,0).
\tag{3.2}
$$


The previous degree digit is zero or one. This proves the uniform suffix statement algebraically, not by extending the finite table through depth $16$.

The common remaining half stream after such a suffix is indeed $M-\tfrac12$: if $a_t$ is the least residue of $247/8$ modulo $3^t$, then its half-index residue is


$$
a_t+\frac{3^t-1}{2},
$$


which lies in $[0,3^t)$ for these suffixes. Subtracting it leaves the quotient $M-\tfrac12$. The adjacent column has the residue one smaller and the same quotient.

### 3.2 Proof of the policy

At an unknown degree digit $d$, use


$$
k=
\begin{cases}
0,&q=0,\ d=0,1,\\
2,&q=0,\ d=2,\\
0,&q=1,\ d=0,\\
1,&q=1,\ d=1,2,
\end{cases}
\qquad r=d-k.
\tag{3.3}
$$



The displayed half-digit and half-carry tables in the proposal follow directly by adding the digit of $-\tfrac12$, namely one, together with the incoming carry. Substitution into those tables proves that the half-borrow stays zero. Also $k+r=d$, so the addition carry stays zero.

For the integral subtraction, its digit is the preceding degree digit after the fixed initial portion.

The useful invariant is:

- if $q=0$, the preceding degree digit is zero or one and the incoming integral borrow is zero;
- if $q=1$, the preceding digit is at least one;
- an incoming integral borrow one occurs only immediately after a transition $q=0,d=2$, whose preceding digit for the next step is two.

Consequently:

- $q=0,d=0,1$ creates no borrow;
- $q=0,d=2$ creates exactly one borrow;
- at the next digit, the preceding digit two clears that borrow, since $k\le1$;
- all other $q=1$ transitions create no borrow.

Two charged transitions cannot be consecutive: after a charge, $q=1$. Therefore a middle word of length $w\ge0$ costs at most


$$
\left\lceil\frac w2\right\rceil.
\tag{3.4}
$$



A following string of ones creates no new charge and clears a possible incoming integral borrow. After the leading ones, a zero degree digit clears the half-carry; the remaining forced zero tail accepts in state $000$.

The policy therefore proves the claimed bound for every middle word. The 3280-word certificate is finite corroboration of this induction, not its replacement.

---

## 4. Prefix length and the overlap repair

### 4.1 Exactly the guaranteed 25-digit prefix

For sufficiently large tuples in the window, $D>2$, and


$$
m=\frac{3^L-D+1}{2}.
$$


Because


$$
C_{16}>3^{25},
$$


the window gives


$$
D<3^{L-25}.
$$


It follows that $m$ lies inside the $L$-digit ternary cylinder whose first 25 digits are ones:


$$
\frac{3^L-3^{L-25}}2
\le m\le
\frac{3^L-1}2.
\tag{4.1}
$$


The upper bound is more restrictive than the upper endpoint of that cylinder.

Thus $L$ really is the number of ternary digits of $m$, and 25 leading ones are guaranteed. A universal 26th leading one is not supplied by this window.

### 4.2 Overlap

The suffix has alternating zero and one digits beyond its initial block. Hence any overlap of length at least two with an all-one prefix would contain a prescribed zero. Such an overlap is impossible.

There are therefore two possibilities:

1. **Disjoint blocks:** $t\le L-25$.  
   The middle length is
   

$$
w=L-t-25\ge0.
$$



2. **One-digit overlap:** $t=L-24$.  
   The overlapping suffix digit must be one. Every digit is then prescribed and is zero or one except the units digit two. The zero-cost path proves $r=0$.

In the second case $w=-1$, but


$$
\left\lceil\frac{-1}{2}\right\rceil=0.
$$


Thus the same numerical bound remains valid, provided this case is explained rather than described as a middle word of negative length.

We obtain


$$
\boxed{
r\le\left\lceil\frac{L-t-25}{2}\right\rceil,
}
\tag{4.2}
$$


on every sufficiently large compatible integer, with the one-digit-overlap interpretation above.

In particular,


$$
2r\le L-t-24=h-t-25.
\tag{4.3}
$$



---

## 5. Complete exclusion theorem and its normalization scope

For $t\ge8$,


$$
8m\equiv247\pmod{3^t}
\quad\Longrightarrow\quad m\equiv851\pmod{6561}.
$$


Theorem 2.1 therefore gives $r=u$. In particular,


$$
r<4+u;
$$


the collision $r=4+u$ is impossible.

Under the retained normalization,


$$
v_3(a_m)=1,\quad \mathfrak a=a_m/3\in\mathbb Z_3^\times,
$$




$$
v_3(b_m)=1,\quad v_3(\rho)=4,\quad
N_m=9\kappa_m^2h_m\in\mathbb Z_3^\times,
$$


the established noncollision identity applies:


$$
\operatorname{cont}_3(\mathcal E)=2r.
\tag{5.1}
$$



Here the norm is the actual norm, with


$$
v_3(h_m)=-2-2v_3(\kappa_m),
$$


and


$$
N_m=
\frac{2^{2A+3}(3A+2)}
{(A+1)((4A+3)/3)\,U(m)},\qquad
U(m)=\frac{\binom{6m}{3m}}{\binom{2m}{m}}.
$$


No leading coefficient or norm unit is discarded.

The retained finite core comparison then gives


$$
s_c=h-2-2r.
$$


Combining with (4.3),


$$
\boxed{s_c\ge t+23.}
\tag{5.2}
$$



### Theorem 5.1 — Deep-family inverse-comparison exclusion

On every sufficiently large original-window tuple satisfying the actual unit-normalizer hypotheses and


$$
t=v_3(4^{j+1}-247)\ge9,
$$


one has


$$
\boxed{
r=u,\qquad \operatorname{cont}_3(\mathcal E)=2r,\qquad s_c\ge32.
}
\tag{5.3}
$$



On the sufficiently deep controlled-growth resonant family of A1_turn1, the normalizer hypotheses are established by the retained continuation theorem. Hence (5.3) is unconditional on that original family.

For arbitrary original powers with $t\ge9$, synchronization and the upper content bound are unconditional; the supplied proofs do not justify assigning the Christoffel unit valuation beyond its established scope.

**Research consequence:** the collision problem is closed on the deep normalized subfamily. No seven-row collision search or further collision analysis is warranted there.

---

## 6. Matveev and exact-window intersection

The supplied checked primary-text input provides an effective lower bound of the required form for the nonzero real linear form


$$
q\log4-p\log3.
$$


For positive rationals $4,3$, the field degree is one, their logarithmic heights are $\log4,\log3$, and the nearest integer $p$ satisfies $|p|\le2q$. Unique factorization proves nonvanishing.

Thus the checked theorem implies effective constants $c>0,K>0$ such that


$$
\boxed{\|q\alpha\|\ge c q^{-K},\qquad \alpha=\log_3 4.}
\tag{6.1}
$$


The intersection argument needs only this effective polynomial form, not the particular loose numerical value $10^{12}$. I do not claim an independent visual inspection of the PDF.

### 6.1 A fixed exact interval

If $x=\{j\alpha\}$ and $L=\lceil j\alpha\rceil$, then


$$
\frac DH=1-3^{x-1}+3^{-L}.
\tag{6.2}
$$



The limiting admissible interval is


$$
I=\left(
1+\log_3(1-b_*),\
1+\log_3(1-a_*)
\right),
$$


of fixed positive length


$$
|I|=\log_3\frac{1-a_*}{1-b_*}.
\tag{6.3}
$$



Choose a fixed closed subinterval $I'$ in the interior of $I$. Its positive margin absorbs $3^{-L}$ for all sufficiently large $L$. A hit in $I'$ then proves the **strict original window**, not merely a leading-digit condition.

### 6.2 Exact resonance and quantitative hitting

The order of $4$ modulo $3^{t+1}$ is $3^t$. Exact resonance depth $t$ can therefore be imposed by choosing a suitable residue


$$
j\equiv j_t\pmod{3^t}
$$


whose image modulo $3^{t+1}$ agrees with $247$ to depth $t$ but not $t+1$. For $t\ge6$, the retained LTE implication gives $j\equiv81\pmod{243}$.

On this progression the rotation step is


$$
\beta=3^t\alpha.
$$


Choose a fixed Dirichlet bound $Q$, depending only on $|I'|$, sufficiently large that a step of magnitude at most $1/Q$ is smaller than the interval. Dirichlet approximation supplies $1\le q\le Q$ with


$$
0<\delta=\|q\beta\|\le1/Q.
$$


By (6.1),


$$
\delta\ge c(3^tQ)^{-K}.
$$


Successive positive multiples of the signed step $q\beta$ cover the circle with gaps at most $\delta$ before one full traversal. Consequently a hit occurs after


$$
O(\delta^{-1})
$$


such multiples, and hence at an original index bounded by a fixed power of $3^t$. Starting the progression beyond any prescribed fixed exponential lower threshold does not change this conclusion.

Therefore one can select exact-window, exact-resonance original indices with


$$
\boxed{\log(j+1)=O(t).}
\tag{6.4}
$$



This closes the real-window dependency used by the retained moving-base tail argument. It establishes the original controlled-growth family needed in Theorem 5.1, rather than an auxiliary arbitrary-middle family.

---

## 7. Direct whole-scalar response without a small core inverse loss

The failed inequality $s_c<32$ concerns a uniform matrix comparison. It need not govern a particular observable.

Set


$$
B=-S_c/3^{26},\qquad T=-S_{\rm act}/3^{26}=B+E,
$$




$$
f=e_{\rm act}-e_c,\qquad g=d_{\rm act}-d_c.
$$


The retained congruences are


$$
E\in3^6M_\nu(\mathbb Z_3),\qquad
f\in3^6\mathbb Z_3^\nu,\qquad g\in3^4\mathbb Z_3.
$$



Assume temporarily that $B,T$ are nonsingular. Define


$$
x=B^{-1}e_c,\qquad z=f-Ex,
$$


and the complete scalars


$$
F_c=e_c^TB^{-1}e_c-3^{26}d_c,
$$




$$
F_{\rm act}=e_{\rm act}^TT^{-1}e_{\rm act}-3^{26}d_{\rm act}.
$$



### Proposition 7.1 — Exact directional identity



$$
\boxed{
F_{\rm act}-F_c
=
2f^Tx-x^TEx-3^{26}g
+z^TT^{-1}z.
}
\tag{7.1}
$$



Indeed,


$$
e_{\rm act}=Tx+z.
$$


Expanding $e_{\rm act}^TT^{-1}e_{\rm act}$ gives (7.1).

This identity does **not** require $B^{-1}E$ to be integral or small. It isolates the actual correlated residual


$$
z=f-Ex,
$$


rather than estimating $f$ and $Ex$ independently.

### Full scalar guard

Put


$$
A_{\rm lin}=2f^Tx-x^TEx-3^{26}g,\qquad
R_{\rm dir}=z^TT^{-1}z.
$$


A sufficient exact guard is


$$
\boxed{
v_3(A_{\rm lin})>v_3(F_c),\qquad
v_3(R_{\rm dir})>v_3(F_c).
}
\tag{7.2}
$$


It protects the valuation of the **whole** scalar, including its subtraction.

A coarse sufficient bound for the second condition is


$$
2\min_i v_3(z_i)-\lambda(T)>v_3(F_c),
$$


but this is not compulsory: evaluating the single pairing $z^Ty$, where $Ty=z$, can be much stronger.

The remaining directional target is therefore concrete: prove additional cancellation in the actual $z$ and its actual response, not another general bound for all entries of $T^{-1}$.

---

## 8. Actual derivative pairing and a finite pole-pair cancellation

### 8.1 The derivative uses the full endpoint solution

Introduce the exact path


$$
Q_\theta=Q_c+\theta\,3^6R,\qquad
G_\theta(P,Q)=\mathcal M(Q_\theta PQ).
$$


Let $v=(1,-1,\ldots,(-1)^m)^T$, and let the coefficient vector of $P_\theta$ be


$$
G_\theta^{-1}v.
$$


Then


$$
\frac{d}{d\theta}\bigl(v^TG_\theta^{-1}v\bigr)
=
-3^6\mathcal M(RP_\theta^2).
\tag{8.1}
$$



Exact block elimination gives


$$
v^TG_\theta^{-1}v=d_\theta+e_\theta^TS_\theta^{-1}e_\theta.
$$


Therefore the corresponding normalized whole scalar satisfies


$$
\boxed{
F_\theta'=3^{32}\mathcal M(RP_\theta^2).
}
\tag{8.2}
$$



This is the actual derivative pairing. The polynomial $P_\theta$ includes the eliminated LOW/HIGH component as well as the corrected residual component. Replacing it by an endpoint-unit Jacobi branch, or by a residual polynomial alone, would not evaluate (8.2).

### 8.2 An exact cancellation tied to the original saturated residual

Use the accepted precision-$25$ saturation


$$
R=R_{25}+3^{25}\Delta_{25},
$$




$$
R_{25}=(y+1)x^{A-54}B_{25}(x),\qquad \deg B_{25}\le54,
$$


and the actual core representatives


$$
\phi_i=x^D\psi_i.
$$



For each original residual pair $0\le i,j<\nu$, put


$$
V_{ij}=x^{D-54}B_{25}(x)\psi_i\psi_j.
$$


Then, exactly,


$$
R_{25}\phi_i\phi_j=(y+1)x^HV_{ij}.
\tag{8.3}
$$



Since $H$ is odd, define the complete polynomial


$$
\Delta_H(y)=x^H-(y^H-1)
=\sum_{k=1}^{H-1}(-1)^{H-k}\binom Hk y^k.
\tag{8.4}
$$


Every layer is retained, and


$$
v_3([y^k]\Delta_H)=L-v_3(k).
$$



Write


$$
B_{\rm cut}=2n-2,\qquad
w_r=\frac{3^h}{2r+1}\quad(0\le r\le B_{\rm cut}).
$$


For any polynomial $V=\sum_rV_ry^r$, the original finite pole functional gives the exact identity


$$
\begin{aligned}
\mathcal M((y+1)x^HV)
={}&-\frac{3^h}{4}\mathfrak f((y+1)x^HV)\\
&+\sum_{r\ge0}V_r
\left(
\mathbf1_{r+H\le B_{\rm cut}}w_{r+H}
-\mathbf1_{r\le B_{\rm cut}}w_r
\right)\\
&+\sum_{v=0}^{B_{\rm cut}}w_v[y^v](\Delta_HV).
\end{aligned}
\tag{8.5}
$$



For a genuinely paired interior index $0\le r\le B_{\rm cut}-H$,


$$
\boxed{
w_{r+H}-w_r
=
-\frac{2\,3^hH}{(2r+1)(2r+2H+1)}.
}
\tag{8.6}
$$



If $a=v_3(2r+1)<L$, then both denominator valuations equal $a$, and


$$
v_3(w_{r+H}-w_r)=h+L-2a.
\tag{8.7}
$$


The unpaired weight has valuation $h-a$. Thus this pair gains exactly


$$
L-a
$$


digits.

This is an exact cancellation for the actual original finite residual pairing (8.3), with the actual $B_{25}$ and corrected representatives. It is not a claim that the entire pairing gains that many digits:

- unpaired terminal indices remain in (8.5);
- all $\Delta_H$ terms remain;
- the factorial term remains;
- $3^{25}\Delta_{25}$ must be restored;
- the full endpoint polynomial in (8.2) has additional components.

Those are precisely the terms that a useful observable lemma must control.

### 8.3 Both corrected representatives remain necessary

In core-corrected coordinates, put


$$
K(P,Q)=\mathcal M(RPQ),
$$


and let


$$
T_R=K(W,\widehat Z^{\,c}),\qquad
K_Z=K(\widehat Z^{\,c},\widehat Z^{\,c}).
$$


Then


$$
\widehat Z^{\,\rm act}
=
\widehat Z^{\,c}-3^6WE_{\rm act}^{-1}T_R,
$$


and


$$
\boxed{
S_{\rm act}-S_c
=
3^6K_Z-3^{12}T_R^TE_{\rm act}^{-1}T_R.
}
\tag{8.8}
$$



Thus (8.5) is to be used inside the complete pairing calculation, not in place of the nonlinear Schur correction. It supplies a specific cancellation mechanism beyond bare entrywise depth while retaining both representatives.

---

## 9. Finite forcing, terminal return, and arithmetic normalization

Nothing above changes the finite spaces:


$$
U_u=x^u\quad(0\le u<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m),\qquad
d=\frac{3D}{2}-1,\quad \nu=\frac D2-1.
$$



The functional is still


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\sum_{\substack{v\ge0\\2v+1\le4n-3}}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1}.
$$


Both leading extractions, all allowed lower poles, the factorial force, and the LOW subtraction must enter the complete return before any reduction.

The terminal equations remain


$$
\mu_{i+\nu}^{\langle26\rangle}
+\sum_{k=0}^{\nu-1}f_k\mu_{i+k}^{\langle26\rangle}
=b_i^{\langle26\rangle},
\qquad0\le i\le\nu-2,
$$




$$
J^T\varepsilon+\omega
=
-\varepsilon-s\bigl(\theta e_{\nu-1}
+3^{26}b^{\langle26\rangle}\bigr).
$$


There is no moment beyond $D-4$, and $\omega_{\nu-1}$ is retained.

The actual pair is


$$
D_0=\det T,\qquad
D_1=e_{\rm act}^T\operatorname{adj}(T)e_{\rm act}
-3^{26}d_{\rm act}\det T.
$$


When both are nonzero,


$$
v_3(q)=
\max\left\{
0,\,
h-26+2v_3((n-1)!)
+v_3(D_1)-v_3(D_0)
\right\}.
$$


This is not determined by the new inverse-loss exclusion.

After restoring every row content, the actual multiplier, and the actual clearer,


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,\qquad
g_\ell=\gcd(|A_\ell|,|B_\ell|)
$$


over all primes. For $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
$$


and


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{g_\ell}
\det H_{\rm complete}.
}
\tag{9.1}
$$



No norm, common row power, or local content may replace this all-prime primitive normalization.

---

## 10. Next lemma and bounded calculation

The collision question is no longer the next target on the deep normalized family.

### Concrete follow-on lemma

For the actual original tuple, establish either:

1. the complete directional guard (7.2), using
   

$$
z=(e_{\rm act}-e_c)-(T-B)B^{-1}e_c,
$$


   with an actual evaluation of $z^TT^{-1}z$; or

2. directly,
   

$$
D_0D_1\ne0
$$


   and a usable law for $v_3(D_1)-v_3(D_0)$.

The structural work needed is to combine the pole-pair gain (8.6) with all $\Delta_H$ layers, the unpaired cutoff terms, complete forcing, eliminated endpoint component, and terminal return. A bound for the paired bulk alone is insufficient.

### New bounded exact-arithmetic interface

No accepted suffix, content, endpoint, or precision-budget computation should be rerun.

For **one newly supplied certified original tuple**, the direct test requires:

- the complete actual rational producer and multiplier;
- the original finite blocks and both corrected representatives;
- the actual endpoint data;
- $B_{25}$ and $\Delta_{25}$, or equivalent exact reconstruction data;
- a stated precision bound, with every division loss certified.

The verifiable output should be:

1. the exact decomposition (8.5), separately recording paired bulk, unpaired boundary, all $\Delta_H$ contributions, and factorial force;
2. the complete Schur reconstruction (8.8);
3. $F_c$, $A_{\rm lin}$, and $R_{\rm dir}$, or certified valuations and residues at explicitly sufficient precision;
4. either a strict guard proving scalar preservation, or an explicit statement that the precision does not decide it;
5. if the direct pair is evaluated, both $D_0,D_1$, with the full subtraction.

This is an unevaluated finite specification. No feasible small runtime follows from the supplied sources, and no favorable residue is predicted.

---

## 11. Final proof-status ledger

| Claim | Status |
|---|---|
| Eight-digit state-vector identity | Accepted exact finite certificate, with recurrence audited |
| Common future degree, integral-upper, and half-upper streams | Proved |
| Common terminal rules | Proved |
| Universal $r=u$ on $m\equiv851\pmod{6561}$ | Proved |
| Uniform zero-cost resonance suffix | Proved |
| Constructive arbitrary-middle upper bound | Proved |
| Prefix/suffix overlap | Repaired: at most one digit; bound survives |
| Fixed exact-window quantitative intersection | Closed using the checked Matveev text input |
| $\operatorname{cont}_3(\mathcal E)=2r$ and $s_c\ge t+23$ | Proved under actual unit normalization |
| Exclusion on the sufficiently deep controlled-growth original family | Unconditional using retained continuation |
| Unit normalization for every resonant original power | Not established at that broader scope |
| Exact scalar variation and actual derivative pairing | Proved |
| Actual finite saturated-residual pole-pair cancellation | Proved, with all remainder terms retained |
| Complete directional guard or direct cofactor valuation | Unresolved |
| Actual primitive denominator and whole nonzero error decay | Unresolved |

### Conclusion

The new suffix argument supersedes collision analysis on the deep normalized original family:


$$
\boxed{
r=u,\qquad \operatorname{cont}_3(\mathcal E)=2r,\qquad s_c\ge t+23.
}
$$



The research bottleneck is now the **actual complete scalar response**, not a uniform small inverse loss. The directional identity (7.1) and the exact pole-pair cancellation (8.6) identify a concrete route: exploit correlated endpoint and forcing cancellation while retaining the full finite system.

They do not yet prove nonvanishing of the actual cofactor pair, control the all-prime primitive gcd, or produce infinitely many same-index nonzero errors tending to zero.



$$
\boxed{\text{The irrationality of }e+\pi\text{ remains unresolved by this work.}}
$$


