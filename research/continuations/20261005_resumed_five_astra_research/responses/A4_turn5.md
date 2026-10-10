> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 independent review: actual-force residual transfer and the precision-two convolution recurrence

## 1. Audit verdict

I accept the two principal local results, with the qualifications below.

### A1 turn 2

On the original domain


$$
n=4^j+1,\qquad j>0,\qquad81\mid j,\qquad
0<D=H-(n-2)<H/972,\qquad H=3^{h-1},
$$


the new structural argument does justify


$$
\boxed{\mathscr R_{\rm act}\equiv\mathscr R_c\pmod{3^7}}
$$


in the **full scaled-matrix normalization**, assuming the retained full-force congruence and integral block results at their stated scopes.

The stronger direct pairing estimates, the complete finite-ring HIGH-return formula, and the next actual-polynomial Hankel strip also pass this review:


$$
\boxed{
\frac{\mathscr R_{\rm act}}{3^6}
\equiv-\frac{V\mathcal I_HV^T}{81}\pmod3,
}
$$


and


$$
\boxed{
\frac{\mathscr R_{\rm act}-\mathscr R_c}{3^7}
\equiv
\left([y^{r_1-i-j}]W_R(y)\right)_{0\le i,j<\nu}
\pmod3.
}
$$



These are structural transfer statements, not consequences of the finite building-block certificate alone. The rank, radical, endpoint coupling, and resulting unconditional denominator depth remain open.

### A2 turn 1

The carry-free recurrence correctly computes


$$
\boxed{
\mathcal T\bmod841,\qquad
U=\sum_{k=0}^H kX_k^2\bmod29
}
$$


for every nonnegative integer $H$ and $0\le d\le24$, with


$$
A=2001H+69d+67,\qquad
X_k=\binom Ak\binom{2A+H-k}{H-k}.
$$



The adjacent-digit harmonic weight and its six-residue compression are valid. The first-digit initialization of the $U$-accumulator is correct in the stated initial state. Four appended zero digits suffice.

For a fixed input, the affine and doubling carries are deterministic. Thus there are at most **two live sum-carry states**, not 8004 simultaneously live carry states. The number 8004 is a valid uniform transducer-state upper bound.

There is one notation issue worth correcting in the factorial derivation: the displayed one-level factorial formula must refer to the product of integers **not divisible by $29$**, not to the fully stripped factorial unit without its recursive factor. I give the precise formulation below. This does not invalidate the recurrence.

No tools were executed. I do not replay the already closed population theorem or infer any irrationality conclusion from these local results.

---

# Part I. Review of A1’s actual-force residual theorem

## 2. Domain, matrix normalization, and complete functional

Retain


$$
A=H-D,\quad m=\frac{A+1}{2},\quad
d=\frac{3D}{2}-1,\quad \nu=\frac D2-1,
$$




$$
r_1=\frac{H-1}{2},\qquad r_*=\frac{3H-1}{2}.
$$


The column ranges remain exactly


$$
0\le a\le m,\qquad
U_a=(y-1)^a\ (0\le a<D),\qquad
z_i=y^i(y-1)^D\ (0\le i<\nu),
$$


and


$$
Y_b=y^b\qquad(d\le b\le m).
$$



Here $D$ is a positive multiple of six. Consequently $D\ge6$, $\nu\ge2$, and $H>5832$, so $h\ge9$.

The reference polynomial and actual correction are


$$
Q_c=(y+1)(y-1)^A(\beta+3y),\qquad \beta=-71-A,
$$




$$
Q_n^{\rm loc}=Q_c+3^6R,\qquad R\in\mathbb Z_3[y],\quad \deg R\le n.
$$


The review uses this as the retained **actual full-force congruence**; it does not replace $R$ by an arbitrary chosen polynomial.

The functional remains


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
\sum_{r=0}^{h}
\sum_{\substack{c\ge1\ {\rm odd}\\3\nmid c\\c3^r\le4n-3}}
3^{h-r}c^{-1}[y^{(c3^r-1)/2}]
\frac{F(y)-F(-1)}{y+1}.
$$


All poles, the cutoff, the endpoint subtraction, and the factorial force are retained.

The exact full-normalization Schur residual is


$$
\mathscr R=
G(Z,Z)-3B^TL^{-1}B
-9\widetilde V\widehat E^{-1}\widetilde V^T,
$$


where


$$
G(U,U)=3L,\quad G(U,Z)=3B,\quad
G(U,Y)=3X,\quad G(Z,Y)=3V,
$$




$$
\widehat E=E-3X^TL^{-1}X,\qquad
\widetilde V=V-B^TL^{-1}X.
$$



**Normalization check:** the final coefficient is $9$, not $3$. The coefficient $3$ belongs to the residual after the first LOW division. A1 turn 2 uses the full normalization consistently.

---

## 3. The Schur perturbation lemma is valid

Suppose an integral unimodular column transformation puts the reference form into


$$
\begin{pmatrix}A_0&0\\0&\mathscr R_0\end{pmatrix},
\qquad A_0^{-1}\in3^{-1}M(\mathbb Z_3),
$$


and the transformed perturbation is $3^PT$, $P\ge2$.

The perturbed eliminated block is


$$
A_0+3^PT_{EE}
=A_0\bigl(I+3^PA_0^{-1}T_{EE}\bigr).
$$


Since


$$
3^PA_0^{-1}T_{EE}\in3^{P-1}M(\mathbb Z_3),
$$


its parenthesized factor is invertible over $\mathbb Z_3$, and


$$
(A_0+3^PT_{EE})^{-1}\in3^{-1}M(\mathbb Z_3).
$$


The new residual is therefore exactly


$$
\mathscr R_0+3^PT_{RR}
-3^{2P}T_{RE}(A_0+3^PT_{EE})^{-1}T_{ER}.
$$


Hence


$$
\boxed{
\mathscr R_{\rm act}
=\mathscr R_0+3^PT_{RR}+O(3^{2P-1}).
}
$$



The eliminated inverse loss is indeed **one**. No inverse of the residual block is used, so this argument remains valid on singular residual branches.

This lemma does not authorize a Neumann expansion of the full matrix inverse. A1 correctly avoids that stronger and generally unjustified conclusion.

---

## 4. Top-pole annihilation gives the extra transfer digit

Because


$$
3H<4n-3<9H,
$$


the only depth-$h$ pole is $3H=3^h$. Thus


$$
\mathcal M(F)\equiv[y^{r_*}]C_F\pmod3,
\qquad
C_F=\frac{F-F(-1)}{y+1}.
$$



The corrected reference residual columns satisfy


$$
\widehat z_i^{\,c}\equiv z_i\pmod3.
$$


The linear perturbation in the Schur lemma is consequently, modulo three,


$$
\mathcal M(R\widehat z_i^{\,c}\widehat z_j^{\,c})
\equiv[y^{r_*}]C_{Rz_iz_j}.
$$



Now


$$
\deg z_i\le d-1,
$$


and therefore


$$
\deg C_{Rz_iz_j}
\le n+2(d-1)-1
=A+2d-1
=H+2D-3<r_*.
$$


The coefficient vanishes **exactly by degree**.

With $P=6$, the linear perturbation belongs to $3^7$, while the quadratic correction belongs to $3^{11}$. Therefore


$$
\boxed{\mathscr R_{\rm act}\equiv\mathscr R_c\pmod{3^7}.}
$$



This resolves the specific missing digit identified in A1 turn 21. There is no contradiction with that earlier precision obstruction: a generic $3^6$ matrix perturbation does not transfer this digit, but the actual perturbation has additional polynomial and finite-pole structure.

---

## 5. Beta valuation and direct $ZZ/UZ$ depths

### 5.1 The beta valuation has the required restricted scope

For


$$
B_H(s)=\frac{(-1)^H2^HH!}
{\prod_{a=0}^{H}(2s+2a+1)},
$$


the statement


$$
v_3(B_H(s))=-v_3(2s+1)
$$


is correct for


$$
0\le s\le(H-3)/2.
$$



Here is a direct proof of the precise valuation. For each $1\le q\le h-1$, among the first $H$ terms


$$
2s+1,\ 2s+3,\ldots,2s+2H-1
$$


there are exactly $H/3^q$ multiples of $3^q$. The final term


$$
2s+2H+1
$$


is divisible by $3^q$ exactly when $2s+1$ is. Moreover,


$$
2s+2H+1\le3H-2,
$$


so the denominator contains no multiple of $3^h=3H$. Its valuation is thus


$$
\sum_{q=1}^{h-1}\frac H{3^q}+v_3(2s+1).
$$


The first sum is $v_3(H!)$, proving the assertion.

The upper bound on $s$ matters; this is not an unrestricted beta valuation formula.

### 5.2 Direct pairing bounds

For $ZZ$,


$$
C_{Q_cz_iz_j}
=y^{i+j}(y-1)^H(y-1)^D(\beta+3y).
$$


Expanding the last degree-$D$ factor gives beta shifts no larger than


$$
i+j+D+1\le2D-3.
$$


The $UZ$ shifts are smaller.

Since


$$
2s+1\le4D-5<H/243=3^{h-6},
$$


we have


$$
v_3(2s+1)\le h-7.
$$


Thus every scaled beta term in these pairings has valuation at least seven. The factorial term has valuation at least $h\ge9$.

For the actual $3^6R$ correction, the top-pole coefficient is absent by degree. Its complete functional value consequently has an additional factor of three. Therefore


$$
\boxed{
G_c(Z,Z),\,G_{\rm act}(Z,Z),\,
G_c(U,Z),\,G_{\rm act}(U,Z)\in3^7M(\mathbb Z_3).
}
$$



In particular,


$$
B\in3^6M(\mathbb Z_3).
$$


The omitted LOW correction has valuation at least


$$
v_3(3B^TL^{-1}B)\ge13,
$$


and replacing $\widetilde V$ by $V$ in the HIGH contraction changes it only in $3^8M$. Hence


$$
\boxed{
\mathscr R_{\rm act}
\equiv-9V\widehat E^{-1}V^T\pmod{3^7}.
}
$$



There is no lost factor of three here.

---

## 6. The finite-ring operator and the building-block certificate

The beta entry formulas in A1 §5 follow by canceling the factor $y+1$ in $Q_c$, expanding the actual basis products, and using


$$
B_p(s)=
(-1)^p2^{2p+1}
\frac{p!\,(s+p+1)!\,(2s)!}
{(2s+2p+2)!\,s!}.
$$


The displayed powers $3^{h-1}$ and $3^h$ agree with the divided $L,X,V$ blocks and the undivided $E$ block.

The factorial omissions at these evaluation precisions are justified: even after the one division by three, their depth is at least $h-1\ge8$.

### 6.1 Finite inverses

The LOW inverse is the finite reciprocal-series identity


$$
\sum_{t\ge0}(-1)^t\binom{r_1+t}{t}z^t
=(1+z)^{-(r_1+1)}.
$$


Its reverse-triangular orientation gives


$$
(R_L)_{ab}=[z^{a+b-D+1}](1+z)^{r_1+1}.
$$



For HIGH,


$$
r_*=A+d+m.
$$


Writing $q=a+b-d-m$, the nonzero entries of $E_0$ are the coefficients


$$
(-1)^q\binom Aq
$$


of $(1-z)^A$. Thus the inverse, on the same finite range $d\le a,b\le m$, is


$$
(R_H)_{ab}=[z^{d+m-a-b}](1-z)^{-A}.
$$


No infinite matrix inverse is being substituted for a finite one.

Four LOW Neumann terms give precision $81$, and five HIGH terms give precision $243$. The factor three in


$$
E-3X^T\mathcal I_LX
$$


makes LOW inverse precision $81$ sufficient for HIGH precision $243$.

### 6.2 Divisibility before division

The retained fifth-carry theorem gives


$$
\mathscr R_{\rm act}\in3^6M.
$$


Combined with the congruence modulo $3^7$, it implies


$$
V\widehat E^{-1}V^T\in81M.
$$


Since


$$
\mathcal I_H\equiv\widehat E^{-1}\pmod{243},
$$


the residue $N_*=V\mathcal I_HV^T\bmod243$ is divisible by $81$, and


$$
\boxed{\mathcal D_6=-N_*/81\bmod3}
$$


is well-defined.

**All five HIGH-return terms are required.** Carries from the first four terms cannot be discarded in favor of the last term alone.

### 6.3 Exact scope of the coordinator certificate

The supplied certificate establishes its stated finite checks:

- 1001 factorial-unit arguments;
- 1681 beta identities and scaled-residue comparisons;
- 72 LOW inverse tests;
- 540 HIGH inverse and Neumann tests.

Its factorial recursion is correct. The product of all units modulo $243$ is $-1$, and recursively removing multiples of three gives the displayed unit-factorial formula.

The certificate does **not** establish the actual-force transfer, residual rank, or endpoint coupling. Those require the structural arguments above and further work, respectively.

---

## 7. The next actual-force strip: no missing pole

Modulo nine, the only potentially contributing pole layers are:

- the depth-$h$ pole $3H$, with weight one;
- the depth-$(h-1)$ pole $H$, with weight three.

At the second layer, $5H$ is already outside the cutoff. There is therefore no omitted additional odd unit at that precision.

From the retained corner value of $V\bmod3$ and $R_He_m=e_d$,


$$
\widehat z_i^{\,c}=z_i+3w_i\pmod9,
$$


where $w_i\bmod3$ has a representative of degree at most $d$. Thus the top-pole coefficient of each mixed term $C_{Rz_iw_j}$ is still zero by degree. The first surviving linear perturbation is exactly


$$
3[y^{r_1}]C_{Rz_iz_j}.
$$


The quadratic Schur perturbation is in $3^{11}$, beyond the required modulus $3^8$. Hence


$$
\boxed{
\frac{\mathscr R_{\rm act}-\mathscr R_c}{3^7}
\equiv
\bigl([y^{r_1}]C_{Rz_iz_j}\bigr)_{i,j}\pmod3.
}
$$



For the Hankel description, let


$$
F(y)=R(y)(y-1)^{2D},\qquad t=i+j.
$$


The exact identity


$$
C_{y^tF}=y^tC_F+
F(-1)\frac{y^t-(-1)^t}{y+1}
$$


shows that the additional endpoint-division term has degree at most $t-1<r_1$. Therefore


$$
[y^{r_1}]C_{Rz_iz_j}
=[y^{r_1-i-j}]W_R.
$$



The required strip is precisely


$$
r_1-(D-4),\ldots,r_1.
$$


This is the strip of the **actual**


$$
R=\frac{3P_n-Q_c}{729},
$$


not a freely chosen perturbation.

---

## 8. Endpoint and conditional denominator normalization

Evaluating the complete corrected columns gives


$$
e_{\rm res}
=z(-1)-B^TL^{-1}u
-3\widetilde V\widehat E^{-1}(v-X^TL^{-1}u).
$$


Consequently


$$
\boxed{
e_{\rm res}\equiv((-1)^i)_{0\le i<\nu}\pmod3.
}
$$


Dividing the residual **form** by $3^6$ does not divide this covector.

If, and only insofar as the following sufficient conditions are established,


$$
\det\mathcal D_6\ne0,\qquad
\overline e_{\rm res}^{\,T}\mathcal D_6^{-1}
\overline e_{\rm res}\ne0,
$$


then


$$
v_3(\det G_{\rm act})=D+6\nu,\qquad
v_3(v^TG_{\rm act}^{-1}v)=-6.
$$


The eliminated contribution has depth at least $-1$, so it cannot cancel the residual term of depth $-6$.

The exact ratio is


$$
\frac{\beta_1}{\beta_0}
=\frac{3^hQ_n^{\rm loc}(-1)}4
v^TG_{\rm act}^{-1}v.
$$


Using the retained endpoint law gives the conditional result


$$
\boxed{
v_3(q)=
\max\{0,h+2v_3((n-1)!)-6\}.
}
$$



This is a sufficient-branch deduction, not a characterization of all branches. In particular, endpoint nonzero residue does not prove nonisotropy.

---

# Part II. Review of A2’s mod-$841$ convolution recurrence

## 9. Carry-free paths preserve the complete finite sum

Set $p=29$. If $p\mid X_k$, then


$$
X_k^2\equiv0\pmod{p^2},
\qquad kX_k^2\equiv0\pmod p.
$$


It is therefore exact at the requested precisions to retain only unit $X_k$.

Write $l=H-k$. A binomial coefficient is a $p$-adic unit precisely when its defining addition is carry-free. Accordingly, the conditions are


$$
k_i\le a_i,\qquad c_i+l_i\le p-1,
$$


together with


$$
k_i+l_i+\sigma_i=\eta_i+p\sigma_{i+1}.
$$



Starting at $\sigma_0=0$ and accepting only zero terminal carry gives exactly


$$
k+l=H,\qquad k,l\ge0.
$$


Thus the accepted paths correspond bijectively to the unit summands with


$$
0\le k\le H.
$$


The finite endpoint is not enlarged.

---

## 10. Derivation of the adjacent-digit harmonic factor

Define the one-level $p$-free product


$$
F_p(N)=\prod_{\substack{1\le r\le N\\p\nmid r}}r.
$$


For $0\le s<p$,


$$
F_p(pm+s)
\equiv ((p-1)!)^m\,s!\,(1+pmH_s)\pmod{p^2}.
$$


Indeed, each complete block contributes


$$
\prod_{r=1}^{p-1}(pj+r)
\equiv(p-1)!(1+pjH_{p-1})
\equiv(p-1)!\pmod{p^2},
$$


and the final partial block contributes $s!(1+pmH_s)$.

For the fully stripped factorial unit


$$
\mathcal U_p(N)=N!/p^{v_p(N!)},
$$


one must additionally use


$$
\mathcal U_p(N)=F_p(N)\mathcal U_p(\lfloor N/p\rfloor).
$$


This recursive factor is essential. A1’s $U_5$ and the one-level object in A2’s explanatory sentence should not be conflated.

For a carry-free binomial $\binom NK$, the complete-block exponents cancel at every level. The digit-$i$ correction is


$$
n_{i+1}H_{n_i}
-k_{i+1}H_{k_i}
-(n_{i+1}-k_{i+1})H_{n_i-k_i}.
$$


Only the next digit is needed because the correction is already multiplied by $p$.

Apply this first to $\binom Ak$, then to $\binom{2A+l}{l}$. The second addition has no carries, so its top digits are $c_i+l_i$. The combined correction is exactly


$$
\begin{aligned}
E(\tau,\tau')={}&
a'H_a-k'H_k-(a'-k')H_{a-k}\\
&+(c'+l')H_{c+l}-c'H_c-l'H_l.
\end{aligned}
$$


Squaring gives


$$
\boxed{
X_k^2\equiv
\prod_i
\binom{a_i}{k_i}^{2}\binom{c_i+l_i}{l_i}^{2}
\prod_i(1+2pE(\tau_i,\tau_{i+1}))
\pmod{p^2}.
}
$$



This proves the weight formula uniformly, rather than by extrapolation from the 3795 checks.

---

## 11. Compression, first-digit moment, and termination

### 11.1 Six-residue compression

The identity


$$
E(\tau,\tau')
=a'v_1(\tau)+k'v_2(\tau)+c'v_3(\tau)+l'v_4(\tau)
$$


is an exact rearrangement of the harmonic expression.

At a prefix, store its total weight $W\bmod p^2$, its weighted last harmonic vector $Z\bmod p$, and its weighted first digit $V\bmod p$. Extending by a current tuple gives


$$
W_{\rm new}\;{+}{=}\;
g\left(W+2p(aZ_1+kZ_2+cZ_3+lZ_4)\right).
$$


Since the harmonic term is already multiplied by $p$, only $Z\bmod p$ is needed. For the new harmonic vector, only the prefix weight modulo $p$ is needed:


$$
(Z_r)_{\rm new}\;{+}{=}\;(g\bmod p)(W\bmod p)v_r.
$$


These update rules remain valid after merging paths.

### 11.2 Correct normalization of $U$

Because


$$
k\equiv k_0\pmod p,
$$


the desired moment is the terminal weighted first digit:


$$
U=\sum k_0X_k^2\bmod p.
$$


At the initial state $W=1$, the first update is


$$
V_{\rm new}\;{+}{=}\;(g\bmod p)k_0.
$$


At every later digit,


$$
V_{\rm new}\;{+}{=}\;(g\bmod p)V.
$$



Thus A2’s first-digit rule is correct as initialized. A generalized implementation with arbitrary initial weight would need the factor $W\bmod p$; the coordinator implementation includes it explicitly.

There is **no division of $U$ by $29$**. By contrast, $T_1=\mathcal T/29\bmod29$ is defined only when $T=0$.

### 11.3 Termination

After the last input digit, the multiplier carry is at most 2000. Under appended zeros it satisfies


$$
2000\longmapsto68\longmapsto2\longmapsto0.
$$


At the third appended digit, the remaining $A$-digit is at most two, so doubling also leaves zero carry. The fourth appended digit is therefore a zero tuple for every accepted path and closes the final adjacent-digit interaction.

Accepting only zero terminal sum carry excludes paths representing the wrong finite sum. Hence four appended zeros suffice.

### 11.4 Actual live breadth

For a specified $H,d$, the pair $(\kappa_i,\varepsilon_i)$ is determined by the input prefix. Only $\sigma_i\in\{0,1\}$ branches. Therefore the exact uniform live-state bound is


$$
\boxed{2.}
$$


The corresponding candidate-transition bound is at most $2\cdot29=58$ per digit.

The number


$$
2001\cdot2\cdot2=8004
$$


is a bound on the uniform transducer state alphabet, not on simultaneous breadth for a fixed input.

---

## 12. Finite certificate and downstream obligation

The coordinator’s 3795 complete exact-convolution comparisons establish exactly their reported finite scope:

- $0\le H\le150,\ 0\le d\le24$;
- twenty additional pairs at $H=299,840,841,842,900$.

The comparisons include all summands $0\le k\le H$, with exact divisions in the direct recurrence. They corroborate the implementation and the carry-boundary handling. The general proof is supplied by the carry and factorial derivation above.

The population theorem is retained without replay. The remaining local obligation is not population but deeper relative valuation control.

Writing


$$
\alpha=v_{29}(D),\qquad\gamma=v_{29}(M),
$$


the established congruence


$$
M-rD\in29^3\mathbb Z_{29}
$$


gives $\gamma=\alpha=2$ when $\alpha=2$, but does not determine $\gamma-\alpha$ when $\alpha\ge3$.

A concrete follow-on lemma is:

> On the original deeper locus $D\in29^3\mathbb Z_{29}$, derive the actual normalized defect
> 

$$
> E_4=(M-rD)/29^3\bmod29
>
$$


> together with $D/29^3\bmod29$, retaining the actual column normalizations, complete force, finite contact boundary, and endpoint.

A recurrence for $\mathcal T\bmod29^3$ alone would not automatically prove this lemma. At that precision, summands with $v_{29}(X_k)=1$ begin to contribute, and the stronger actual-column reconstruction must also be supplied.

---

# 13. Final arithmetic interface and proof status

For A1’s cleared determinant pair,


$$
A_\ell=\ell^k\beta_0,\qquad B_\ell=\ell^k\beta_1,\qquad
g_\ell=\gcd(|A_\ell|,|B_\ell|),
$$


retain


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


Where $B_\ell\ne0$, the whole evaluated error is


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell^k}{g_\ell}
\det H_{\rm complete}.
}
$$



For A2’s actual integer Gram pair, retain


$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B,
$$


and


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
$$


The exact local denominator interface remains


$$
v_{29}(q_n)
=\max\{0,\,2F_n-F_b-1+\alpha-\gamma\}.
$$


Neither reviewed recurrence nor residual transfer determines the full all-prime gcd.

## New result of this review

The outstanding structural checks are resolved as follows:

1. **Accepted:** A1’s loss-one Schur lemma, actual top-pole transfer modulo $3^7$, direct $ZZ/UZ$ depth seven, complete HIGH-return digit, next actual-force strip, and endpoint transport.
2. **Accepted conditionally:** A1’s exact $q$-depth formula under the explicitly stated invertibility and nonisotropy conditions.
3. **Accepted:** A2’s precision-two convolution recurrence, finite endpoint, adjacent-digit weighting, termination, and normalized first-digit $U$-moment.
4. **Clarified:** A2’s factorial-unit notation and the distinction between 8004 transducer states and at most two live sum-carry states.

## Exact remaining bottlenecks

- **A1:** determine the rank and endpoint coupling of
  

$$
-V\mathcal I_HV^T/81\bmod3
$$


  uniformly on the original family. On singular branches, retain the actual $R$-strip together with the next core and endpoint data.
- **A2:** control the actual normalized fourth defect and the resulting relative valuations on the deeper norm locus.
- **Globally:** control the actual final primitive denominators and prove nonzero whole primitive errors tending to zero along the same original indices.

## Bounded computation needed

No additional bounded computation is needed to validate the two local statements accepted here; the supplied certificates already cover their implementation-level checks.

Any subsequent A1 finite residual calculation should take an explicitly verified original-domain input $(j,H,D)$, modulus $243$, and the exact finite arrays as inputs, and return:

1. $V\mathcal I_HV^T\bmod243$;
2. entrywise divisibility by $81$;
3. $\mathcal D_6\bmod3$;
4. its rank and radical;
5. endpoint-image membership and, on the invertible branch, $\kappa_0$.

Such output would establish only that input’s result, not uniform rank behavior. No original-size rank calculation is claimed here.



$$
\boxed{\text{The irrationality or rationality of }e+\pi\text{ remains unresolved.}}
$$


