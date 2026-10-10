> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 Turn 7 — Independent audit of the wide-window ternary closure and exhaustive binary alignment certificate

## Executive verdict

The two applications have different proof mechanisms and must be kept separate.

### A1: wide-window support closure

**The wide-window argument passes, with an important clarification concerning representatives and precision.** On


$$
n=4^j+1,\qquad j>0,\qquad81\mid j,\qquad
0<D=H-(n-2)<H/972,\qquad H=3^{h-1},
$$


the finite inverse propagation, lower truncation correction, LOW projection, and required Neumann returns can be justified without enlarging HIGH. In particular, using the accepted actual-force and block interfaces,


$$
\boxed{V\widehat E^{-1}V^T\equiv0\pmod{729}}
$$


and hence


$$
\boxed{\mathcal D_6=0.}
$$



The clarification is substantive: applying the propagation lemma to a merely modular quotient and then dividing by $3$ would be unsafe. One must select an **exact supported divisible lift** of the HIGH residue before making the coefficient extractions. The finite inverse construction supplies such representatives; I spell this out below.

The depth-seven direct normalization also passes:


$$
\boxed{
\frac{\mathscr R_{\rm act}}{3^7}
\equiv
\mathcal C_7+\mathcal F_R\pmod3,
}
$$


with the actual $R$-strip and endpoint exactly as stated. This does not select an invertible, nonisotropic branch or determine an unconditional primitive denominator.

### A5 and the coordinator’s binary certificate

**The source-level arithmetic audit passes.** The separate period $1024$, diagonal half-period, reductions to $D\bmod16$ and $x\bmod8192$, six factorial patterns, negative moments, terminal zeros, and raw-weight pruning all have sufficient precision.

Crucially, the supplied $p,\delta,\beta$ representatives have enough **weighted raw precision** to support the original scalar theorem—not just an auxiliary table identity. This follows from the accepted raw reconstruction congruences and


$$
2X_j\in4\mathbb Z_2,\qquad4(Y_j-X_j)\in8\mathbb Z_2.
$$



Taking the supplied exhaustive receipt at its stated computational scope, the combined argument establishes, at the accepted contact-transfer and whole-force interfaces,


$$
\boxed{H-N\equiv0\pmod{128}}
$$


for


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
$$



This is a **computer-assisted original-family congruence**: the finite computation proves the complete low-state identity, while the proved periods and exact finite contraction transfer it to the original family. I have not executed or independently reproduced the table.

No norm valuation, unrestricted relative valuation, full gcd, or irrationality conclusion follows from that alignment alone.

---

# I. A1: the wide-window ternary theorem

## 1. Domain and normalization

Retain


$$
A=H-D,\quad m=\frac{A+1}{2},\quad
d=\frac{3D}{2}-1,\quad \nu=\frac D2-1,
$$




$$
r_1=\frac{H-1}{2},\qquad r_*=\frac{3H-1}{2}.
$$



The actual columns remain


$$
U_a=(y-1)^a,\quad 0\le a<D,
$$




$$
z_i=y^i(y-1)^D,\quad0\le i<\nu,
$$




$$
Y_b=y^b,\quad d\le b\le m.
$$



The review uses the complete functional, including its factorial term, endpoint subtraction, and cutoff:


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\sum_{\substack{v\ge0\\2v+1\le4n-3}}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1}.
$$



The exact full-normalization residual is


$$
\mathscr R_c
=
G_c(Z,Z)-3B^TL^{-1}B
-9\widetilde V\widehat E^{-1}\widetilde V^T,
$$


where


$$
\widehat E=E-3X^TL^{-1}X,\qquad
\widetilde V=V-B^TL^{-1}X.
$$



The coefficient $9$, rather than $3$, remains essential.

The older fixed-depth theorem is not being extended by citation. Its narrower window does not imply this new $H/972$ statement. The new proof must—and does—supply its own width budget.

## 2. Arithmetic margin

Set


$$
\omega=H/243=3^{h-6}.
$$


The real-window condition gives


$$
\omega>4D.
$$



By LTE,


$$
v_3(A)=v_3(4^j-1)=1+v_3(j)\ge5.
$$


The already justified $h\ge9$ implies that $H,\omega,D$ are all divisible by $27$. Therefore


$$
\boxed{\omega-4D\ge27.}
$$



Also,


$$
\beta=-71-A\equiv-71\pmod{243}.
$$



These are consequences of the original domain, not new restrictions.

---

## 3. Beta phase reduction

For odd $x$, write


$$
\mathcal B_M(x)=
\frac{(-1)^M2^MM!}{\prod_{a=0}^{M}(x+2a)}.
$$



When $3\mid x$, splitting the factors divisible by $3$ gives exactly


$$
\mathcal B_{3M}(x)
=
\frac13\mathcal B_M(x/3)\Theta_M(x),
$$


with


$$
\Theta_M(x)=
\frac{2^{2M}\prod_{1\le a\le3M,\ 3\nmid a}a}
{\prod_{0\le a\le3M,\ 3\nmid a}(x+2a)}.
$$



The excluded denominator factors are precisely those indexed by multiples of $3$. If $3^u\mid x$, the remaining denominator factors satisfy


$$
x+2a\equiv2a\pmod{3^u},
$$


so


$$
\boxed{\Theta_M(x)\equiv1\pmod{3^u}.}
$$



### Precision of the nonendpoint phases

For


$$
x=cH/81,\qquad c=1,3,\ldots,79,
$$


the scaled beta quantity has valuation


$$
v_3(HB_H((x-1)/2))=4-v_3(c).
$$


In the last reduction to length $81$, the argument before division is $3c$. Thus the weakest removed unit is $1$ modulo


$$
3^{1+v_3(c)}.
$$


Its effect on the scaled quantity is consequently divisible by


$$
3^{4-v_3(c)}3^{1+v_3(c)}=3^5.
$$


This proves the claimed congruence modulo $243$.

The same calculation validates the extra-$3$ reduction to $B_{27}$. At the exceptional endpoint, the last removed argument is $243$, so the asserted endpoint phase precision is also sufficient.

Thus the fifty-three nonendpoint bands and the top corner are not merely candidate support locations: the stated bounded phase formulas are valid.

### Support modulo $729$

At this higher precision the unshifted beta grid is


$$
H/243=\omega,
$$


and the extra-$3$ beta grid is


$$
H/81=3\omega.
$$


The top corner remains exceptional. Therefore


$$
\boxed{\operatorname{supp}(V_{i,\bullet}\bmod729)\subseteq J(\nu).}
$$



No phase computation modulo $729$ is needed for the support argument.

---

## 4. Finite inverse propagation and the exact-lift clarification

The exact finite inverse remains


$$
(R_H)_{ab}
=[z^{d+m-a-b}](1-z)^{-A},
\qquad d\le a,b\le m.
$$



The sparse series congruences are valid:


$$
(1-z)^H\equiv(1-z^{3\omega})^{81}\pmod{243},
$$




$$
(1-z)^H\equiv(1-z^\omega)^{243}\pmod{729}.
$$


They follow by repeated cubing of a congruence modulo $3$; each cubing gains a power of $3$. Inversion is legitimate because the constant terms are $1$.

Consequently


$$
(1-z)^{-A}\equiv(1-z)^D S(z^\omega)
$$


at the respective precision.

For a half-grid-supported vector $w$, the polynomial copies underlying $R_Hw$ are


$$
(y-1)^D
\sum_b w_b\sum_{u\ge0}s_u y^{r_1-b-u\omega}.
$$



Three finite-boundary facts are decisive.

1. **Negative starting exponents.**  
   A copy starting below degree $0$ has largest degree at most $D-1<d$. It contributes nothing to HIGH and may be discarded.

2. **Upper endpoint.**
   

$$
r_1-b\le r_1-d=m-D.
$$


   Thus retained copies have degree at most $m$. No column beyond HIGH is introduced.

3. **Lower truncation.**  
   If $P=(y-1)^DQ$ is the finite sum of retained copies and $p=P_{\ge d}$, then
   

$$
\pi(p)
   =
   P-\left(P_{<d}-\operatorname{rem}_{(y-1)^D}P_{<d}\right).
$$


   The quotient of the correction has degree at most
   

$$
d-1-D=\nu-1.
$$


   This lies inside the allowed band around $0$.

Hence


$$
R_Hw\in\mathcal C(W)
$$


with the original finite HIGH boundaries.

### Required interpretation of $\mathcal C(W)$

For subsequent division by $3$, it is not enough to say only


$$
\pi(p)/(y-1)^D\quad\text{is supported in }I(W)\pmod{243}
$$


and then apply a coefficient functional losing one digit.

The safe statement is:

> The HIGH residue has a representative $p$ for which the exact polynomial $\pi(p)/(y-1)^D$ is supported in $I(W)$.

The construction above supplies precisely such a representative: choose integer or $3$-adic lifts of the finitely many sparse coefficients, form $P$, and perform the exact finite lower truncation and monic remainder correction.

Because $F$ is integral, replacing a HIGH input by another representative modulo $243$ does not change $Fp\bmod243$. Thus this stronger representative choice is legitimate at each inverse step.

This closes the potential lost-precision gap rather than assuming it away.

---

## 5. Complete $F$-propagation, including LOW

Let


$$
F=(\widehat E-E_0)/3.
$$


Take an exact supported lift


$$
\pi(p)=(y-1)^DQ,\qquad\operatorname{supp}Q\subseteq I(W).
$$



The LOW pairing divided by $3$ extracts coefficients from


$$
(y-1)^H(y-1)^a(\beta+3y)Q.
$$


Modulo $729$, this polynomial is supported in $I(W+D)$.

After dividing the functional by $3$, the possible top weight is $1/3$. Thus **modulus $729$, not merely $243$, is the correct polynomial precision** for a conclusion modulo $243$. A coefficient error in $729\mathbb Z_3$ becomes an error in $243\mathbb Z_3$, which is harmless.

All pole indices relevant at that precision lie on the half-grid. Hence, under


$$
W+D<\frac{\omega-1}{2},
$$


the LOW pairing vanishes modulo $243$:


$$
G_c(U,\pi(p))/3\equiv0\pmod{243}.
$$



Writing $p=\pi(p)+Ur$, this gives


$$
Xp-Lr\equiv0\pmod{243}.
$$


The exact identity


$$
\widehat Ep-G_c(Y,\pi(p))
=
3X^T(r-L^{-1}Xp)
$$


therefore gives


$$
\widehat Ep\equiv G_c(Y,\pi(p))\pmod{729}.
$$



After division by $3$, the remaining coefficient extraction is supported in $J(W+1)$. The remainder contribution to $E_0p$ is absent exactly by degree:


$$
A+(D-1)+m<r_*.
$$


The same modulus-$729$ polynomial argument handles $E_0p/3$.

Thus


$$
\boxed{\operatorname{supp}(Fp\bmod243)\subseteq J(W+1).}
$$



This proof retains the actual LOW correction. It does not replace it by zero.

---

## 6. Every required Neumann return

For


$$
p_{\ell,j}=(R_HF)^\ell R_HV_j^T,
$$


the preceding lemmas give exact supported representatives of the residue classes with


$$
p_{\ell,j}\in\mathcal C(\nu+\ell)\pmod{243},
\qquad0\le\ell\le5.
$$



The support overlap test uses


$$
\nu+(\nu+\ell+D)=2D-2+\ell.
$$


For $\ell\le5$,


$$
2D-2+\ell\le2D+3
<
\frac{\omega-1}{2},
$$


because $\omega-4D\ge27$.

Therefore


$$
V(R_HF)^\ell R_HV^T\equiv0\pmod{243},
\qquad0\le\ell\le5.
$$



For the zeroth return, the modulus-$729$ inverse propagation gives the stronger result


$$
VR_HV^T\equiv0\pmod{729}.
$$


For all other terms, the outer factor $3^\ell$ supplies the extra digit:


$$
\widehat E^{-1}
\equiv
\sum_{\ell=0}^{5}(-3R_HF)^\ell R_H
\pmod{729}.
$$


Consequently


$$
\boxed{V\widehat E^{-1}V^T\equiv0\pmod{729}.}
$$



All five terms needed for $\mathcal D_6$, including their carries, are covered. No “last summand only” inference is being used.

Using the accepted actual-force transfer,


$$
\boxed{\mathcal D_6=0.}
$$


Its radical is the whole residual space, and the transported nonzero endpoint


$$
\overline e=((-1)^i)_{0\le i<\nu}
$$


is outside its zero image.

---

## 7. Depth seven: direct normalization and actual force

Since $B\in3^6M$,


$$
3B^TL^{-1}B\in3^{13}M.
$$


Replacing $\widetilde V$ by $V$ changes the HIGH-return contribution only modulo $3^8$. The stronger return congruence therefore gives


$$
\mathscr R_c\equiv G_c(Z,Z)\pmod{3^8}.
$$



In the beta expansion, all relevant odd arguments are below


$$
\omega=3^{h-6}.
$$


A beta term can contribute after division by $3^7$ only at argument


$$
3^{h-7}=H/729.
$$


There is only one positive odd multiple of this number below $3^{h-6}$: the number itself. Thus


$$
i+j+t=\varrho,\qquad
\varrho=\frac{H/729-1}{2}.
$$



The normalized beta factor is


$$
\frac{3^h}{3^7}
B_H\!\left(\frac{H/729-1}{2}\right)
\equiv B_{729}(0)\pmod3.
$$



For completeness,


$$
B_m(0)=(-1)^m4^m\frac{(m!)^2}{(2m+1)!}.
$$


When $m=3^a$, numerator and denominator factorial valuations cancel. The squared numerator unit is $1\bmod3$, while the stripped unit of $(2m+1)!$ is $-1\bmod3$. Since $m$ is odd,


$$
B_{3^a}(0)\equiv1\pmod3.
$$


Also $\beta\equiv1\pmod3$. The extra-$3$ term is beyond this digit.

Hence


$$
\boxed{
(\mathcal C_7)_{ij}
=[y^{\varrho-i-j}](y-1)^D.
}
$$



The previously accepted degree-sensitive actual-force perturbation gives


$$
(\mathcal F_R)_{ij}
=[y^{r_1-i-j}]
\frac{R(y)(y-1)^{2D}-R(-1)(-2)^{2D}}{y+1},
$$


for the actual


$$
R=(3P_n-Q_c)/729.
$$



The endpoint-division correction from multiplying by $y^{i+j}$ has degree at most $i+j-1<r_1$, so it does not alter the selected coefficient. The required strip is exactly


$$
\boxed{r_1-(D-4),\ldots,r_1.}
$$



Therefore


$$
\boxed{
\mathscr R_{\rm act}\in3^7M,\qquad
\mathscr R_{\rm act}/3^7\equiv\mathcal C_7+\mathcal F_R\pmod3.
}
$$



### Conditional denominator

If this actual sum is invertible and


$$
\overline e^{\,T}(\mathcal C_7+\mathcal F_R)^{-1}\overline e\ne0,
$$


then, and only under those sufficient branch conditions,


$$
v_3(\det G_{\rm act})=D+7\nu,
$$




$$
v_3(v^TG_{\rm act}^{-1}v)=-7,
$$


and


$$
\boxed{
v_3(q)=\max\{0,h+2v_3((n-1)!)-7\}.
}
$$



The endpoint’s nonzero residue alone does not establish this nonisotropy condition.

---

# II. Binary certificate: arithmetic audit and original-family transfer

## 8. Weighted raw precision is sufficient

This is the key bridge from the auxiliary table to the actual scalar theorem.

For an interior coordinate, set


$$
a_j=(-1)^{j+1}W_j\mathcal F_j,\qquad
b_j=(-1)^{j+1}W_j\mathcal G_j.
$$


The accepted reconstructed-column congruences are


$$
a_j\equiv2X_j\pmod{128},\qquad
b_j\equiv4(Y_j-X_j)\pmod{256}.
$$



Because $X,Y\in2\mathbb Z_2^{b+1}$,


$$
a_j\in4\mathbb Z_2,\qquad b_j\in8\mathbb Z_2.
$$



Writing


$$
a_j=2X_j+128r_j,\qquad
b_j=4(Y_j-X_j)+256s_j,
$$


gives


$$
a_j^2-4X_j^2
=
256r_j(2X_j)+128^2r_j^2\in1024\mathbb Z_2,
$$


and


$$
a_jb_j-8X_j(Y_j-X_j)
=
128r_j\,4(Y_j-X_j)
+256s_j\,2X_j
+32768r_js_j
\in1024\mathbb Z_2.
$$



Thus


$$
\boxed{
a_j^2\equiv4X_j^2,\qquad
a_jb_j\equiv8X_j(Y_j-X_j)\pmod{1024}.
}
$$



This is a weighted statement about reconstructed raw columns. It does **not** assert that every normalized $U_s$ or $V_s$ is intrinsically known modulo $1024$.

### Why the selected coefficient representatives suffice

- $P\bmod128$ determines the first raw column modulo $128$, since the finite reconstruction uses integral binomial coefficients.
- $Q-2P\bmod256$ is well-defined from $Q\bmod256$ and $P\bmod128$.
- The nine exterior coefficients $\beta\bmod256$ determine their complete raw contribution at the second-column precision.
- The accepted coefficient-valued transfer and tail bounds apply to the complete reconstructed columns.

Accordingly, arbitrary higher lifts of these accepted residues cannot change the whole raw products modulo $1024$. This resolves the representative issue.

---

## 9. Safe periods and optimized coefficient tables

### Separate period $1024$

The product of all odd residues modulo $2^{10}$ is $1$, so


$$
O(m+1024)\equiv O(m)\pmod{1024},
$$


and


$$
L_7(m+65536)\equiv L_7(m)\pmod{1024}.
$$



For $r\le15$, binomial translation gives


$$
v_2\left(\binom{x+h}{r}-\binom xr\right)
\ge v_2(h)-\lfloor\log_2r\rfloor.
$$


This follows from Vandermonde and


$$
\binom hi=\frac hi\binom{h-1}{i-1}.
$$



The separate $1024$-shifts preserve every factorial-unit argument, elementary factor, bounded coefficient, and explicit coordinate multiplier at the required precision. This validates A5 turn4’s safe period theorem.

### Diagonal half-period

Under


$$
(D,t)\mapsto(D+512,t+512),
$$


$d=D-t$ stays fixed; $k,K,C$ have the required residues; the coefficient argument changes by $65536$; and the only potentially changing elementary factor is $C-t$. Its square satisfies


$$
(x+512h)^2\equiv x^2\pmod{1024}.
$$



Thus the diagonal half-period is valid. The coordinator did not need to rely on it for coverage, because the computation covers all $524288$ full states.

### Reduction to $D\bmod16$

Since


$$
A=256(4002D+2532)+132,
$$


a $16$-shift in $D$ changes $A$ by a number of valuation


$$
8+1+4=13.
$$


The worst bounded-binomial loss is $3$, leaving ten bits. Therefore


$$
a_s(A)\pmod{1024},\qquad s\le15,
$$


is determined by $D\bmod16$.

This is not the previously restricted substitution $A=644$. The code computes the actual bounded multiplier for each of the eight odd residue classes.

### Reduction to $x\bmod8192$

An $8192=2^{13}$ shift likewise leaves ten bits after the maximal loss of three. It also preserves the explicit factor $x\bmod1024$.

The table’s use of $x-1\bmod8192$ is safe, including at residue $x=0$: the integer-valued binomial polynomial at $-1$ is congruent modulo $1024$ to its value at $8191$. No negative factorial is needed.

Thus the optimized coefficient tables preserve the actual evaluation at


$$
j=128t+\rho.
$$



---

## 10. Floors, units, boundaries, and products

### Six patterns

The imported `SHAPES` table is generated from the actual three floors. All six factors are implemented correctly:


$$
K,\quad Kd,\quad Kk,\quad d,\quad k,\quad dk.
$$


In particular, the $(\rho,s)=(85,-10)$ pattern uses $k$, not an incorrectly shifted high kernel.

### Negative moments and terminal zeros

The arrays include all moments


$$
-10\le s\le15.
$$


The first-column entries below $-1$ are zero by construction.

For terminal states, every negative actual lower argument is removed by


$$
d=0,\qquad \ell_0=-1,
$$


before factorial-unit access. The terminal residue range is exactly $0\le\rho\le80$.

### Unit indexing

An argument $128q+a$, $0\le a<128$, may be reduced by $q\bmod512$, because the $L_7$ period is $65536$. The indices `iu`, `il`, `ic`, and the corresponding weight indices implement exactly that reduction.

All inverted residues are odd.

### Pruning

The condition


$$
\texttt{dep}\ge5
$$


removes only rows whose explicit raw factor


$$
2^{2\,\texttt{dep}}
$$


is already zero modulo $1024$. It does not remove weight-depth-four rows.

Likewise, a moment with exponent at least ten vanishes before multiplication by any integral coefficient. Neither filter divides by an even factor or presupposes cancellation.

### Integer arithmetic

The bounded binomial evaluations are exact before reduction. The NumPy products and short matrix products remain well within signed $64$-bit range for the displayed representative ranges. Modular reductions occur between the potentially longer multiplicative chains.

I find no overflow, indexing, floor, or boundary obstruction in the supplied implementation.

---

## 11. What the exhaustive receipt establishes

The receipt reports


$$
524288\ \text{full states},\qquad512\ \text{terminal states},
$$


with every mixed coefficient zero modulo $1024$.

The source covers each odd $D\bmod1024$ and every $t\bmod1024$, using positive full-block representatives. Thus, combined with the safe periods, the receipt establishes


$$
\mathcal D_{\rm full}(D,t)\equiv0\pmod{1024}
$$


for every admissible full low state, and


$$
\mathcal D_{\rm end}(D)\equiv0\pmod{1024}
$$


for every odd terminal state.

The existing fourteen full and six terminal scalar comparisons are retained only as finite implementation corroboration. They have not been rerun here and are not the universal proof.

The reported independent $512$-period equalities are now exhaustive finite facts about the computed functions on the safe $1024$-state space. They are not consequences of the withdrawn individual-factor argument. They are also unnecessary for the alignment conclusion.

### Transfer to the original finite sum

The exact contraction is


$$
8(H-N)\equiv
\sum_{t=0}^{D-1}\mathcal B_t^2\mathcal D_{\rm full}(D,t)
+\mathcal B_D^2\mathcal D_{\rm end}(D)
\pmod{1024},
$$


where


$$
\mathcal B_t=\binom Ct\binom{2C+D-t}{D-t}.
$$



The full range, shortened terminal block, and actual high kernel remain unchanged. The actual exterior point, including its $+1$, contributes zero at this precision by the accepted endpoint bounds.

Every low coefficient now vanishes modulo $1024$, so the actual high kernel need not be evaluated:


$$
8(H-N)\equiv0\pmod{1024}.
$$


Exact division of the whole divisible residue yields


$$
\boxed{H-N\equiv0\pmod{128}.}
$$



No periodicity of $\mathcal B_t$, no high-index truncation, and no extra original-family reachability assumption is required.

---

# III. Consequences and remaining obligations

## 12. What binary alignment does—and does not—imply

Let


$$
\alpha=v_2(N),\qquad\gamma=v_2(H).
$$


The new congruence gives


$$
\boxed{\gamma=\alpha\quad\text{if }\alpha\le6.}
$$


If $N\equiv0\pmod{128}$, it gives only


$$
\alpha,\gamma\ge7.
$$



The norm table is not a norm valuation theorem: it still has to be contracted against the actual $\mathcal B_t^2$, including the terminal block. In particular, the auxiliary $D=7$ calculation does not prove an original-family subfamily with $\alpha=6$.

The actual primitive interface remains


$$
v_2(q_n)=
\max\left\{
0,\frac{3n}{2}-v_2(b!)-s_2(n)-1-(\gamma-\alpha)
\right\}.
$$


One may set $\gamma-\alpha=0$ only at indices where the norm valuation is independently known to be at most six.

### Concrete follow-on lemmas

1. **Ternary actual depth-seven endpoint lemma.**  
   Evaluate the actual $R$-strip and determine the radical, endpoint image, and, on invertible branches, endpoint contraction of
   

$$
\mathcal C_7+\mathcal F_R.
$$



2. **Binary norm/deeper-defect lemma.**  
   Contract the certified norm coefficients with the actual high kernel on the original exponential family. On the locus $N\equiv0\pmod{128}$, derive the next actual relative-depth data rather than inferring $\gamma-\alpha$ from mixed alignment.

These are specific mathematical bottlenecks, not requests to repeat the completed contact computation.

---

## 13. Final gcd and whole evaluated errors

For A1 retain


$$
A_\ell=\ell^k\beta_0,\qquad B_\ell=\ell^k\beta_1,\qquad
g_\ell=\gcd(|A_\ell|,|B_\ell|).
$$


When $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
$$


and exactly


$$
\boxed{
q(e+\pi)-p=
\frac{\operatorname{sgn}(B_\ell)\ell^k}{g_\ell}
\det H_{\rm complete}.
}
$$


The primitive polynomial multiplier must remain restored in the actual global pair.

For the binary Gram construction retain


$$
N_B=d_B[u,v],\qquad
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
$$


The primitive multiplier is $d_B^2/g_B$, and the whole error is


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
$$



At the retained scope of the complete signed-error theorem,


$$
\epsilon_n<0\quad\text{eventually},
\qquad
\log|\epsilon_n|
=
-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$


Neither local result proves that the entire nonzero primitive form tends to zero. Neither determines the odd-prime part of the final gcd.

---

## 14. Additional exact arithmetic evidence

### Needed for the current mathematical promotion

**No new scalar probes or contact recomputation are needed.** The supplied source, complete-state receipt, safe-period proof, weighted precision argument, and exact endpoint contraction suffice for the binary promotion, at the accepted construction interfaces.

For archival verification, the coordinator may personally inspect the already produced table and check:

- shapes $(512,1024)$, $(512,)$;
- state ordering $D_0=2i+1$;
- all mixed entries zero;
- the stated distributions and diagonal equalities;
- consistency with the receipt’s recorded table digest.

That is artifact verification of an existing computation, not a new mathematical scan.

### Optional bounded ternary implementation check

The phase proof is algebraic and does not depend on execution. A bounded corroborating calculation may use:

- $B_{81}((c-1)/2)$, odd $1\le c\le79$;
- $B_{27}((c-1)/2)$, odd $1\le c\le25$;
- $B_{81}(40)$;
- $B_{729}(0)$.

Expected output is the stated valuations and normalized phases, including


$$
243B_{81}(40)\equiv-2\pmod3,\qquad
B_{729}(0)\equiv1\pmod3.
$$


No original-size matrix calculation is needed to validate the support closure.

---

# Final proof-status ledger

| Statement | Status |
|---|---|
| A1 finite lower truncation and divisible inverse lifts | Proved, with the exact-supported-representative clarification |
| A1 complete LOW-corrected $F$-propagation | Proved at the required loss-one precision |
| $V\widehat E^{-1}V^T\equiv0\pmod{729}$ | Proved using the retained block interface |
| $\mathcal D_6=0$ on the full $H/972$ domain | Proved using accepted actual-force transfer |
| Depth-seven $\mathcal C_7+\mathcal F_R$, actual strip and endpoint | Proved |
| Exact depth-seven denominator | Conditional on invertibility and endpoint nonisotropy |
| Binary optimized coefficient computation | Source audit passes; exhaustive result supplied, not rerun |
| Weighted representative precision | Proved sufficient for the actual raw scalar contraction |
| Original-family $H-N\equiv0\pmod{128}$ | Computer-assisted theorem at the accepted transfer/force interfaces |
| New norm valuation, full gcd, primitive-error decay | Not established |

The new local results are therefore a valid ternary residual closure through depth six, an explicit actual depth-seven form, and a certified binary alignment through modulus $128$. The remaining obstacles are the actual endpoint-coupled ternary form, the binary norm and deeper relative valuations, and—globally—the same-index final primitive denominator versus whole nonzero error.



$$
\boxed{\text{An unconditional proof or disproof of irrationality of }e+\pi
\text{ remains unresolved.}}
$$


