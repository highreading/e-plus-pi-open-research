> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, turn 1 — Verified exterior gluing, shorter integral numerators, and a target-specific three-moment reduction

## Executive conclusion

I reuse the accepted original $76\times 76$ Schur inverse. I do not regenerate that solve or propose rerunning its certificate. The coordinator’s complete $f_0,\ldots,f_{47}$ will be the first-force input.

This report advances the target in three substantive ways.

1. **The complete Laurent gluing can be strengthened.**  
   The entire principal part of the exponential contact response is retained. After reconstruction, its successive negative coefficients cancel by the factorial-tail recurrence. The last possible negative coefficient is exactly a signed multiple of $v_{24}$, which vanishes modulo $2^{20}$. Thus the complete reconstructed exponential series is analytic modulo $2^{20}$, and its constant correction is exactly the required exterior $-1$ in signed-reversed coordinates.

2. **The reconstructed numerators are shorter than the previous uniform bounds suggest.**  
   Using the complete first-force factorial filtration together with the accepted inverse-band filtration, I prove
   

$$
(1-z)^{44}\mid \widehat P_{f,2},
   \qquad
   (1-z)^{48}\mid \widehat P_{e,2}
   \quad\text{in }(\mathbb Z/2^{20}\mathbb Z)[z].
$$


   Consequently the four reconstructed numerators can be stored in at most
   

$$
178+258+178+254=\boxed{868}
$$


   residue slots, rather than $960$. Their construction below uses integral polynomial arithmetic, exact finite prefix subtractions, and monic synthetic division only.

3. **All independent numerator shifts admit a new exact reduction to nine common moments.**  
   For the actual degree bounds, each branch-pair payload reduces to three moments of one explicitly specified truncated hypergeometric summand. Symmetry leaves only the three branch types $11,12,22$, hence nine common moments for both complete outputs. The finite boundary term is explicit at the original cutoff $j=b$.

This third result is an exact coefficient relation, not yet a practical twenty-bit evaluation. Its obstruction is now explicit: the three-dimensional reduction is over $\mathbb Q_2$, not automatically over $\mathbb Z/2^{20}\mathbb Z$. I give:

- exact fraction-free reduction rules;
- concrete binary guard bounds, at most $1027$ additional bits for the displayed unsaturated reduction;
- a sharper, proved obstruction to treating that rational reduction as a three-state integral quotient;
- a bounded matrix calculation, of size at most $516\times512$, that can inspect the relevant integral quotient without touching the original-length operator.

No weighted original Gram pair is claimed to have been evaluated.

---

## 1. Fixed domain, normalization, and inputs

Throughout,


$$
b=150094635296999121,\qquad
n=600678730458590482242=4002b,
$$




$$
B=b-1,\qquad N=n+2,\qquad L=b+176,
\qquad q=2^{20}.
$$



The contact domain remains $0,\ldots,b-1$. Reconstruction remains $0,\ldots,b$, with


$$
(Cx)_j=jx_{j-1}-x_j,\qquad x_{-1}=x_b=0,
$$


and


$$
W_j=\binom Nj,\qquad \mathcal R=\operatorname{diag}(W_j)C.
$$



The two columns and raw outputs remain


$$
\mathsf a=\mathcal RA^{-1}f,
\qquad
\mathsf b=\mathcal RA^{-1}r+W_be_b,
$$




$$
D_{\rm raw}=\sum_{j=0}^{b}\mathsf a_j^2,
\qquad
E_{\rm raw}=\sum_{j=0}^{b}\mathsf a_j\mathsf b_j.
$$



The complete second force is still


$$
r=\frac{h^e+h^F-A(j!)_{0\le j<b}}{b!}.
$$


Its exponential part is represented by the full factorial load


$$
v_t=\frac{(b+t)!}{b!},\qquad 0\le t\le23.
$$


In particular, no separate factorial subtraction is to be added after forming the accepted exterior-load representation: that representation is already for the normalized, subtracted exponential force.

### 1.1 A normalization point in the supplied producers

Let $B_\ell=\texttt{central}(n/2,\ell)$. The normalized first-force convention used by `normalized_binary_finite_audit_coordinator.py` is


$$
\boxed{
f_i=\sum_{\ell=0}^{i}
\binom i\ell
\left(\prod_{t=\ell+1}^{i}(n+t)\right)B_\ell.
}
\tag{1.1}
$$



By contrast, the auxiliary difference producer `weighted_force_audit_coordinator.py` returns this quantity multiplied by $(-1)^i$.

Thus the input to the present formulas is (1.1), **without** that auxiliary outer sign. The signs in the Newton formula below come from $L^{-1}$ and signed reversal; they are not an instruction to sign the input force a second time.

This is a convention check, not a request to redo the coordinator’s complete head calculation.

---

## 2. The full principal part and its terminal factorial cancellation

Put


$$
t(z)=(1-z)^{-n}.
$$


For an exterior load $\eta$, retain the accepted identity


$$
\mathcal F_\eta=tA_\eta-B_\eta,
$$


where


$$
A_\eta(z)=\sum_r(-1)^r\eta_rz^{-r-1}P_r(z),
\qquad
B_\eta(z)=\sum_r(-1)^r\eta_rz^{-r-1},
$$




$$
P_r(z)=\sum_{a=0}^{r}(-1)^a\binom na z^a.
$$



For the complete factorial load,


$$
B_v(z)=\sum_{r=0}^{23}(-1)^rv_rz^{-r-1}.
\tag{2.1}
$$



The accepted finite exterior-load and Schur formulas give


$$
G_e^*=G_e^{\rm an}+B_v,
\tag{2.2}
$$


with $G_e^{\rm an}$ analytic and its coefficients $0,\ldots,b-1$ equal to the actual signed-reversed contact response.

The reconstruction operator is


$$
\mathfrak C_b=\theta-b-z,\qquad \theta=z\frac{d}{dz}.
$$



### Proposition 1 — Complete reconstruction of the principal part

Over the integers,


$$
\boxed{
\mathfrak C_b B_v=-1+v_{24}z^{-24}.
}
\tag{2.3}
$$


Consequently,


$$
\boxed{
\mathfrak C_bG_e^*
=
\mathfrak C_bG_e^{\rm an}-1
\pmod{2^{20}},
}
\tag{2.4}
$$


and the complete reconstructed exponential series is analytic modulo $2^{20}$.

#### Proof

For $1\le h\le23$, the coefficient of $z^{-h}$ in $\mathfrak C_bB_v$ is


$$
(-1)^h\bigl((b+h)v_{h-1}-v_h\bigr)=0,
$$


because


$$
v_h=(b+h)v_{h-1}.
$$



The constant coefficient comes only from $-z(v_0z^{-1})$, and is $-v_0=-1$.

At the last possible negative exponent,


$$
[z^{-24}]\mathfrak C_bB_v=(b+24)v_{23}=v_{24}.
$$


Finally,


$$
v_2(v_{24})\ge v_2(24!)=22\ge20.
$$


This proves both identities. ∎

This verifies the entire principal part, not only its $z^{-1}$-coefficient. It also identifies the finite terminal remainder instead of silently extending the tail.

### 2.1 The original reconstructed endpoint

For either analytic contact response, and for $0\le k\le b$,


$$
[z^k]\mathfrak C_bG=-(b-k)g_k-g_{k-1}.
$$



At $k=0$, corresponding to $j=b$,


$$
[z^0]\mathfrak C_bG_f=-bg_{f,0},
$$




$$
[z^0]\mathfrak C_bG_e^*=-bg_{e,0}-1.
$$



Since $b$ is odd, multiplication by the signed-reversal factor $(-1)^b=-1$ turns the latter correction into the physical exterior $+1$. Therefore


$$
\mathsf b_b=W_b\bigl(b(A^{-1}r^e)_{b-1}+1\bigr)
\pmod q,
$$


with the original endpoint intact.

At $k=b$, corresponding to $j=0$, the coefficient of the unneeded extension value $g_b$ is zero. No extra contact row has been introduced.

---

## 3. An integral constructor for the complete contact numerators

Here is an implementation-level mathematical specification. It does not require an original-length vector.

### 3.1 The two endpoint corrections

Retain


$$
\Psi G
=
\sum_{s=0}^{76}(-1)^sc_s
\binom{B-\theta}{s}
z^{-s}\bigl(G-P_{<s}G\bigr).
\tag{3.1}
$$



Construct the complete exterior load


$$
u_r^{\rm out}=\sum_{t=r}^{23}\binom n{t-r}v_t,
$$




$$
h_r^{\rm out}
=
\sum_{k=\max(0,r-76)}^{\min(r,23)}
\lambda_{r-k}\binom{b+r}{r-k}u_k^{\rm out},
\qquad 0\le r\le99.
\tag{3.2}
$$



For the first source, define


$$
a_d=(-1)^d\sum_{\ell=d}^{47}
(-1)^\ell f_\ell\binom{B-d}{\ell-d},
\qquad 0\le d\le47,
$$


so that


$$
Y_f=\sum_{d=0}^{47}a_dz^d(1-z)^{-n-d-1}.
\tag{3.3}
$$



Set


$$
Z_f=\Psi Y_f,\qquad Z_e=\Psi\mathcal F_{h^{\rm out}}.
$$


The endpoint vectors, in the supplied orientation, are


$$
(e_\alpha)_t
=
(-1)^{b-76+t}[z^{75-t}]Z_\alpha,
\qquad 0\le t<76.
$$


Then use the already supplied inverse:


$$
\beta_\alpha=S^{-1}e_\alpha,
\qquad
\eta_\alpha=\overline K\beta_\alpha.
\tag{3.4}
$$



The complete responses are


$$
\boxed{
G_f=t\Psi Y_f-t\Psi\mathcal F_{\eta_f},
}
\tag{3.5}
$$




$$
\boxed{
G_e^*=tA_v+t\Psi\mathcal F_{h^{\rm out}}
-t\Psi\mathcal F_{\eta_e}.
}
\tag{3.6}
$$



These are two new right-hand-side applications of the accepted inverse, not a new operator solve.

### 3.2 Atomic band action, including every prefix subtraction

Represent an input by a sum of atoms


$$
a\,z^r(1-z)^{-A},
$$


where $A=0$ or $A=n+\delta$, with the small offset $\delta$ explicitly recorded.

For one atom, the untruncated part of $t\Psi$ contributes, for every


$$
0\le s\le76,\qquad 0\le e\le s,
$$


the term


$$
\boxed{
a(-1)^{s+e}c_s
\binom{B-r+s-e}{s-e}
\binom{A+e-1}{e}
z^{r-s+e}(1-z)^{-A-e-n}.
}
\tag{3.7}
$$



For $A=0$, use the divided-derivative convention: only $e=0$ survives.

If $g_k=[z^k]G$ denotes the coefficient of the **complete analytic input**, the required finite-band subtraction is, for each $s$,


$$
\boxed{
-(-1)^sc_s
\sum_{k=0}^{s-1}
g_k\binom{B-k+s}{s}
z^{k-s}(1-z)^{-n}.
}
\tag{3.8}
$$



Equation (3.8) must be applied to the sum of the input atoms. In particular, the cancellation $tA_\eta-B_\eta$ is not to be discarded before obtaining its analytic prefix.

All binomial coefficients in (3.7)–(3.8) are integral generalized binomial coefficients. There is no inversion of $s!$, $e!$, or an even residue modulo $q$.

### 3.3 Collecting the exterior atoms before applying the band

For a load of length $R$, form the two ordinary polynomials


$$
A^{[R]}_\eta(z)
=
\sum_{r=0}^{R-1}(-1)^r\eta_rz^{R-r-1}P_r(z),
$$




$$
B^{[R]}_\eta(z)
=
-\sum_{r=0}^{R-1}(-1)^r\eta_rz^{R-r-1}.
$$


Then


$$
\mathcal F_\eta
=
z^{-R}\left(A^{[R]}_\eta(1-z)^{-n}
+B^{[R]}_\eta\right).
\tag{3.9}
$$



Both polynomial lengths are at most $R$. Thus the band routine need not act separately on all individual terms in every $P_r$.

The only required load lengths are $24,76,100$.

### 3.4 Collecting into the original common normalization

Use


$$
G_\alpha
=
z^{-176}\left(
\frac{P_{\alpha,2}}{(1-z)^{2n+124}}
+
\frac{P_{\alpha,1}}{(1-z)^n}
\right).
\tag{3.10}
$$



An atom


$$
a z^r(1-z)^{-2n-\delta}
$$


contributes


$$
a z^{176+r}(1-z)^{124-\delta}
$$


to $P_{\alpha,2}$.

An atom


$$
a z^r(1-z)^{-n}
$$


contributes $az^{176+r}$ to $P_{\alpha,1}$.

Every exponent used in this collection is nonnegative. The previous bounds remain valid:


$$
\deg P_{\alpha,2}\le299,\qquad
\deg P_{\alpha,1}\le175.
$$



The direct term $tA_v$ belongs to the $n$-branch of $G_e^*$.

---

## 4. Proved extra divisibility and the shorter reconstructed numerators

The improvement uses a factorial bound on the actual first force, not extrapolation from initial pairs.

### Lemma 2 — Complete first-force filtration

For the normalized first force (1.1),


$$
\boxed{
v_2(f_i)\ge v_2\!\left(\left\lfloor\frac i2\right\rfloor!\right).
}
\tag{4.1}
$$



#### Proof

The central formula has a falling-factorial prefactor of length $\lceil\ell/2\rceil$; its remaining odd factors and central summands are $2$-adically integral. Hence


$$
v_2(B_\ell)\ge v_2(\lceil\ell/2\rceil!).
$$



Moreover,


$$
\binom i\ell (n+i)_{\underline{i-\ell}}
=
\frac{i!}{\ell!}\binom{n+i}{i-\ell}.
$$


Thus the $\ell$-th summand of $f_i$ has valuation at least


$$
v_2(i!)-v_2(\ell!)+v_2(\lceil\ell/2\rceil!).
$$



Writing $\ell=2j$ or $2j+1$ gives


$$
v_2(\ell!)-v_2(\lceil\ell/2\rceil!)\le j.
$$


Therefore the displayed valuation is at least


$$
v_2(i!)-\lfloor i/2\rfloor
=
v_2(\lfloor i/2\rfloor!).
$$


Taking the sum preserves this lower bound. ∎

Use also the accepted band filtration


$$
v_2(c_s)\ge\left\lceil\frac s4\right\rceil.
\tag{4.2}
$$



### Proposition 3 — Pole reduction at twenty bits

In the normalization (3.10),


$$
\boxed{
(1-z)^{44}\mid P_{f,2},
\qquad
(1-z)^{48}\mid P_{e,2}
\pmod q.
}
\tag{4.3}
$$



#### Proof

A first-source atom arising from $f_\ell$, followed by a band term indexed by $s,e$, has $2n$-branch pole offset


$$
d+1+e\le \ell+1+s.
$$



If it survives modulo $2^{20}$, then


$$
v_2(\lfloor\ell/2\rfloor!)
+\left\lceil\frac s4\right\rceil
\le19.
$$


Consequently


$$
\ell+1+s
\le
76+\ell+1-4v_2(\lfloor\ell/2\rfloor!)
\le80.
\tag{4.4}
$$


The last inequality follows by writing $\ell=2j$ or $2j+1$ and using
$v_2(j!)=j-s_2(j)$; it also covers $j=0$.

Thus the first uncorrected response has $2n$-branch pole offset at most $80$.

An exterior input has initial exponent $n$. After the band and final $t$, its $2n$-branch offset is at most $76$. This applies to:

- the complete exterior second source;
- both finite Schur correction loads.

Hence the full first response has offset at most $80$, and the full exponential response has offset at most $76$. Bringing them to offset $124$ proves (4.3). ∎

### 4.1 Reconstruction preserves these factors

For a branch with exponent $A$, define


$$
\mathcal D_A(P)
=
(1-z)\bigl(zP'-(b+176+z)P\bigr)+AzP.
\tag{4.5}
$$



If $P=(1-z)^hR$, then


$$
\boxed{
\mathcal D_A(P)=(1-z)^h\mathcal D_{A-h}(R).
}
\tag{4.6}
$$



Thus the same powers divide the reconstructed numerators:


$$
(1-z)^{44}\mid\widehat P_{f,2},
\qquad
(1-z)^{48}\mid\widehat P_{e,2}.
$$



Define the shorter numerators


$$
p_{f,1}=\widehat P_{f,1},\qquad
p_{e,1}=\widehat P_{e,1},
$$




$$
p_{f,2}=\frac{\widehat P_{f,2}}{(1-z)^{44}},
\qquad
p_{e,2}=\frac{\widehat P_{e,2}}{(1-z)^{48}}.
\tag{4.7}
$$



Then


$$
\boxed{
\widehat G_f
=
z^{-176}\left(
\frac{p_{f,1}}{(1-z)^{n+1}}
+
\frac{p_{f,2}}{(1-z)^{2n+81}}
\right),
}
\tag{4.8}
$$




$$
\boxed{
\widehat G_e
=
z^{-176}\left(
\frac{p_{e,1}}{(1-z)^{n+1}}
+
\frac{p_{e,2}}{(1-z)^{2n+77}}
\right).
}
\tag{4.9}
$$



The degree bounds are


$$
\begin{array}{c|c|c}
\text{numerator}&\text{degree at most}&\text{residue slots}\\ \hline
p_{f,1}&177&178\\
p_{f,2}&257&258\\
p_{e,1}&177&178\\
p_{e,2}&253&254
\end{array}
\tag{4.10}
$$



These are proved upper bounds. The actual degrees may be smaller after the coordinator constructs the coefficients.

### 4.2 How to perform every division by $1-z$

Division by $1-z$ is monic up to the unit $-1$, so it is valid over $\mathbb Z/2^{20}\mathbb Z$.

For $P(z)=\sum_{i=0}^{d}p_iz^i$, define


$$
u_i=\sum_{j=0}^{i}p_j,\qquad 0\le i<d.
$$


Then


$$
P=(1-z)\sum_{i=0}^{d-1}u_iz^i+P(1)z^d.
$$



Each asserted factor is therefore checked and removed by one cumulative-sum pass with zero remainder. Repeat $44$ or $48$ times.

One must **not** assume that an arbitrary reconstructed numerator is divisible by $1-z$: from (4.5),


$$
\mathcal D_A(P)(1)=A\,P(1).
$$


The factors in (4.7) are justified by Proposition 3 and identity (4.6), not by a generic reconstruction rule.

---

## 5. The exponent $123$, the shortened exponents $79,75$, and independent shifts

Retain the accepted core


$$
Q_{\rho\sigma}
=
(1-x)^\rho(1-y)^\sigma
-d(1+u)(u+xy).
$$



For the original common normalization,


$$
[d^n]\frac1{Q_{\rho\sigma}}
=
\frac{((1+u)(u+xy))^n}
{(1-x)^{\rho(n+1)}(1-y)^{\sigma(n+1)}}.
$$



The reconstructed common $2$-branch exponent is $2n+125$, whereas the core contributes $2n+2$. Their difference is


$$
\boxed{125-2=123,}
$$


not $124$.

After cancelling the proved numerator factors, the additional $2$-branch poles are


$$
\boxed{79\text{ for }f,\qquad75\text{ for }e.}
\tag{5.1}
$$



For $\alpha\in\{f,e\}$, put


$$
h_{\alpha,1}=0,\qquad
h_{f,2}=79,\qquad h_{e,2}=75.
$$


Then the shortened branch-pair kernel is


$$
\boxed{
\mathcal K_{\alpha\beta;\rho\sigma}
=
\frac{(1+u)^2(u+xy)^2}
{(1-x)^{h_{\alpha,\rho}}
 (1-y)^{h_{\beta,\sigma}}
 Q_{\rho\sigma}}.
}
\tag{5.2}
$$



The target remains


$$
\boxed{[x^Ly^Lu^{n+2}d^n],\qquad L=b+176.}
\tag{5.3}
$$



A numerator monomial $x^ry^s$ changes the targets separately to


$$
L-r,\qquad L-s.
$$


No step identifies $x$ and $y$, and no step replaces these two shifts by $r+s$.

---

## 6. Every finite cutoff subtraction in the weight gluing

Write


$$
\widehat G_{\alpha,\rho}
=
z^{-176}p_{\alpha,\rho}(z)(1-z)^{-A_{\alpha,\rho}},
$$


where


$$
A_{f,1}=A_{e,1}=n+1,\quad
A_{f,2}=2n+81,\quad
A_{e,2}=2n+77.
$$



For one branch pair, the four-variable coefficient contains terms through $j=L$, whereas the physical contraction stops at $j=b$.

The exact excess band is


$$
\boxed{
\operatorname{Tail}_{\alpha\beta;\rho\sigma}
=
\sum_{h=1}^{176}
W_{b+h}^{\,2}
[z^{176-h}]
\frac{p_{\alpha,\rho}(z)}{(1-z)^{A_{\alpha,\rho}}}
[z^{176-h}]
\frac{p_{\beta,\sigma}(z)}{(1-z)^{A_{\beta,\sigma}}}.
}
\tag{6.1}
$$



Thus the branchwise contraction over the original range is


$$
\begin{aligned}
C_{\alpha\beta;\rho\sigma}
={}&[x^Ly^Lu^{n+2}d^n]\,
p_{\alpha,\rho}(x)p_{\beta,\sigma}(y)
\mathcal K_{\alpha\beta;\rho\sigma}\\
&-\operatorname{Tail}_{\alpha\beta;\rho\sigma}.
\end{aligned}
\tag{6.2}
$$



Both complete reconstructed series are analytic modulo $q$, by the first-column construction and Proposition 1. Therefore


$$
\sum_{\rho,\sigma}\operatorname{Tail}_{\alpha\beta;\rho\sigma}=0
\pmod q.
\tag{6.3}
$$



This proves why the complete kernel sum has the original cutoff. It does **not** make an individual branch tail zero.

The two distinct finite subtractions have now both been specified:

- the band-prefix subtraction (3.8);
- the weight-gluing excess band (6.1).

The finite Schur return is retained separately in (3.4)–(3.6).

---

# Part II. What the direct Cartier approach now proves—and does not prove

## 7. Precision-adapted source layers

The proof of Proposition 3 works modulo $2^p$, $1\le p\le20$, and gives


$$
(1-z)^{124-4p}\mid P_{f,2}\pmod{2^p},
$$




$$
(1-z)^{128-4p}\mid P_{e,2}\pmod{2^p}.
\tag{7.1}
$$



Consequently one may choose integral binary layers so that an intrinsic source layer $2^a$, $0\le a<20$, has reconstructed $2$-branch data bounded by


$$
\begin{array}{c|c|c}
&\text{numerator degree}&\text{additional pole beyond }Q\\ \hline
f&181+4a&4a+3\\
e&177+4a&4a-1
\end{array}
\tag{7.2}
$$


with a negative pole exponent interpreted as a numerator factor. In particular, the $a=0$ exponential $2$-branch has an extra numerator factor $1-z$, rather than a pole.

Each such layer is stored modulo


$$
\boxed{2^{20-a}.}
$$



For a product, the total source valuation is the sum of the two source-layer valuations. There are


$$
\#\{(a_1,a_2):a_1+a_2<20\}=210
$$


ordered source-layer pairs before collection for each branch pair.

This is a genuine improvement over placing the pole $123$ in every low-valuation state.

### 7.1 Exact factored Cartier update

Let


$$
X=1-x,\qquad Y=1-y,\qquad Q=Q_{\rho\sigma}.
$$


For $D\in\{X,Y,Q\}$, define the integral polynomial


$$
R_D=\frac{D(\mathbf z)^2-D(\mathbf z^2)}2.
$$


In particular,


$$
R_X=-x,\qquad R_Y=-y.
$$



For a state


$$
2^a\frac{P}{X^hY^kQ^\ell},
$$


put


$$
e_X=\lceil h/2\rceil,\quad \epsilon_X=2e_X-h,
$$


and similarly for $Y,Q$.

For a binary digit vector $\varepsilon$, the exact section is the sum over


$$
j_X+j_Y+j_Q<20-a
$$


of


$$
\begin{aligned}
&2^{a+J}(-1)^J
\binom{e_X+j_X-1}{j_X}
\binom{e_Y+j_Y-1}{j_Y}
\binom{e_Q+j_Q-1}{j_Q}\\
&\quad\times
\frac{
\Lambda_\varepsilon\!\left(
P X^{\epsilon_X}Y^{\epsilon_Y}Q^{\epsilon_Q}
R_X^{j_X}R_Y^{j_Y}R_Q^{j_Q}
\right)}
{X^{e_X+j_X}Y^{e_Y+j_Y}Q^{e_Q+j_Q}},
\end{aligned}
\tag{7.3}
$$


where $J=j_X+j_Y+j_Q$. An exponent zero has only its $j=0$ term.

The output layer is reduced modulo $2^{20-a-J}$. The reachable support is contained in the parity-selected, halved Minkowski sum of the displayed polynomial supports. This specifies the exact support update without a dense expansion requirement.

### 7.2 A proved envelope, not an asserted small reachable set

After $t$ sections, a valid common-denominator envelope at layer $a$ is


$$
Q^{a+1}X^{h_t(a)}Y^{h_t(a)},
\qquad
h_t(a)=a+\left\lceil\frac{3a+3}{2^t}\right\rceil.
\tag{7.4}
$$



The corresponding numerator degrees satisfy


$$
\begin{aligned}
\deg_xP&\le \rho(a+1)+h_t(a)+\left\lfloor178/2^t\right\rfloor,\\
\deg_yP&\le \sigma(a+1)+h_t(a)+\left\lfloor178/2^t\right\rfloor,\\
\deg_uP&\le2(a+1)+\left\lfloor2/2^t\right\rfloor,\\
\deg_dP&\le a.
\end{aligned}
\tag{7.5}
$$



For $t\ge8$, setting $k=a+1$, these become


$$
\deg_xP\le(\rho+1)k,\quad
\deg_yP\le(\sigma+1)k,\quad
\deg_uP\le2k,\quad
\deg_dP\le k-1.
$$



The resulting dense-envelope counts, summed over the twenty valuation layers, are


$$
\begin{array}{c|r}
(\rho,\sigma)&\text{residue slots}\\ \hline
(1,1)&6,327,958\\
(1,2)&9,397,892\\
(2,1)&9,397,892\\
(2,2)&13,957,258\\ \hline
\text{total}&39,081,000
\end{array}
\tag{7.6}
$$



These counts are combinatorial upper bounds, not enumerated reachable supports.

For example, the layer $a=19$, branch $22$, has envelope counts


$$
\begin{array}{c|r}
t&\text{slots}\\ \hline
0&76,371,440\\
2&11,612,020\\
4&4,612,500\\
8&3,051,220
\end{array}
$$


although this highest layer is only binary and its initial numerator is factored.

The number of carry triples in (7.3), summed over source layers, is bounded by


$$
\sum_{a=0}^{19}\binom{22-a}{3}
=\binom{23}{4}=8855
$$


per digit and branch type before zero detection and collection.

**Conclusion about this approach.** The shortened source layers improve the initial representation substantially. They do not, by themselves, prove a practical complete contraction along the original padded 71-digit target word. I do not call the envelope in (7.6) a feasible reachable module, and I do not infer an impossibility theorem from its size.

The next result takes the permitted exact-coefficient-relation alternative and removes the independent-shift explosion altogether.

---

# Part III. A new exact three-moment quotient for the actual numerators

## 8. Converting every numerator shift into one polynomial payload

For the four shortened branches, set


$$
\begin{array}{c|c|c}
(\alpha,\rho)&R_{\alpha,\rho}&A_{\alpha,\rho}-R_{\alpha,\rho}\\ \hline
(f,1),(e,1)&177&n-176\\
(f,2)&257&2n-176\\
(e,2)&253&2n-176
\end{array}
\tag{8.1}
$$



The alignment in the last column is the useful specialization: it is independent of which corrected column is being used.

Define


$$
a_\rho=\rho n-176,
$$




$$
D_{\alpha,\rho}=(a_\rho)^{\overline{R_{\alpha,\rho}}}.
\tag{8.2}
$$



If


$$
p_{\alpha,\rho}(z)=\sum_{r=0}^{R_{\alpha,\rho}}p_{\alpha,\rho,r}z^r,
$$


define the polynomial in $j$


$$
\boxed{
U_{\alpha,\rho}(j)
=
\sum_{r=0}^{R_{\alpha,\rho}}
p_{\alpha,\rho,r}
(L-j)_{\underline r}
(a_\rho+L-j)^{\overline{R_{\alpha,\rho}-r}}.
}
\tag{8.3}
$$



It has degree at most $R_{\alpha,\rho}$.

### Lemma 4 — Independent-shift conversion

For every $0\le j\le b$,


$$
\boxed{
[z^{L-j}]
\frac{p_{\alpha,\rho}(z)}{(1-z)^{A_{\alpha,\rho}}}
=
\frac{U_{\alpha,\rho}(j)}{D_{\alpha,\rho}}
\binom{a_\rho+L-j-1}{L-j}.
}
\tag{8.4}
$$



#### Proof

For a single numerator monomial $z^r$, the ratio of its coefficient to the binomial on the right is


$$
\frac{
\binom{A_{\alpha,\rho}+L-r-j-1}{L-r-j}
}{
\binom{a_\rho+L-j-1}{L-j}
}
=
\frac{
(L-j)_{\underline r}
(a_\rho+L-j)^{\overline{R_{\alpha,\rho}-r}}
}{
(a_\rho)^{\overline{R_{\alpha,\rho}}}
}.
$$


The falling factorial makes the expression zero when $r>L-j$, as required. Summing proves the identity. ∎

### 8.1 Integral construction of $U_{\alpha,\rho}$

The bases


$$
\phi_r(j)
=
(L-j)_{\underline r}
(a_\rho+L-j)^{\overline{R-r}}
$$


can be generated in $O(R^2)$ polynomial arithmetic:

1. Construct $\phi_0=(a_\rho+L-j)^{\overline R}$.
2. To obtain $\phi_{r+1}$, divide $\phi_r$ by its known factor
   

$$
a_\rho+L-j+R-r-1,
$$


   then multiply by $L-j-r$.

The divisor is linear with leading coefficient $-1$, a unit. Synthetic division is therefore integral in every working residue ring. Accumulate $p_r\phi_r$ as the bases are generated.

No rational interpolation and no inversion of a factorial is required.

---

## 9. Three common moments per branch type

For $\rho,\sigma\in\{1,2\}$, define the exact summand


$$
\boxed{
T_{\rho\sigma}(j)
=
\binom Nj^{\!2}
\binom{\rho n+b-j-1}{L-j}
\binom{\sigma n+b-j-1}{L-j},
\qquad 0\le j\le b.
}
\tag{9.1}
$$



The three moments are


$$
M_{\rho\sigma,r}
=
\sum_{j=0}^{b}j^rT_{\rho\sigma}(j),
\qquad r=0,1,2.
\tag{9.2}
$$



They use the original cutoff $j\le b$ and the original squared weight.

By Lemma 4,


$$
\boxed{
C_{\alpha\beta;\rho\sigma}
=
\frac{
\sum_{j=0}^{b}
T_{\rho\sigma}(j)
U_{\alpha,\rho}(j)U_{\beta,\sigma}(j)
}{
D_{\alpha,\rho}D_{\beta,\sigma}
}.
}
\tag{9.3}
$$



Thus all numerator shifts have become one polynomial payload.

### 9.1 The exact telescoping operator

Put


$$
\mathcal A(j)=(N-j)^2(L-j)^2,
$$




$$
\mathcal B_{\rho\sigma}(j)
=
j^2(\rho n+b-j)(\sigma n+b-j).
$$


Then


$$
T_{\rho\sigma}(j)\mathcal A(j)
=
T_{\rho\sigma}(j+1)\mathcal B_{\rho\sigma}(j+1).
\tag{9.4}
$$



Define


$$
\boxed{
\Delta_{\rho\sigma}R
=
\mathcal A(j)R(j+1)
-\mathcal B_{\rho\sigma}(j)R(j).
}
\tag{9.5}
$$



For every polynomial $R$,


$$
\boxed{
\sum_{j=0}^{b}T_{\rho\sigma}(j)\Delta_{\rho\sigma}R(j)
=
T_{\rho\sigma}(b)\mathcal A(b)R(b+1).
}
\tag{9.6}
$$



The lower boundary is zero because $\mathcal B_{\rho\sigma}(0)=0$. The upper boundary is not zero and is not omitted.

It is explicitly


$$
T_{\rho\sigma}(b)
=
W_b^2
\binom{\rho n-1}{176}
\binom{\sigma n-1}{176},
$$




$$
\mathcal A(b)=(N-b)^2\,176^2.
\tag{9.7}
$$



This telescoping boundary is additional bookkeeping for the scalar reduction. It does not replace the finite Schur return already included in the numerators.

### 9.2 Why three moments suffice at the actual degrees

For $R(j)=j^k$,


$$
\deg\Delta_{\rho\sigma}j^k\le k+3,
$$


and its $j^{k+3}$-coefficient is


$$
\boxed{
k+\tau_{\rho\sigma},
\qquad
\tau_{\rho\sigma}=(\rho+\sigma-2)n-356.
}
\tag{9.8}
$$



The actual payload degrees are


$$
\begin{array}{c|c}
\text{payload}&\text{degree bound }D\\ \hline
f1\,f1,\ f1\,e1&354\\
f1\,f2,\ f2\,e1&434\\
f1\,e2&430\\
f2\,f2&514\\
f2\,e2&510
\end{array}
\tag{9.9}
$$



For branch $11$, the possible resonance is $k=356$, but the largest required $k=D-3$ is only $351$. Thus it is not encountered.

For branches $12$ and $22$, all required pivots are nonzero positive integers.

### Theorem 5 — Target-specific three-moment relation

For every payload in (9.9), there are explicitly constructible polynomials $R$, $Q_0+Q_1j+Q_2j^2$, and a nonzero integer


$$
\Gamma_{\rho\sigma,D}
=
\prod_{k=0}^{D-3}(k+\tau_{\rho\sigma})
$$


such that


$$
\boxed{
\Gamma_{\rho\sigma,D}\,
U_{\alpha,\rho}U_{\beta,\sigma}
=
\Delta_{\rho\sigma}R+Q_0+Q_1j+Q_2j^2.
}
\tag{9.10}
$$



Consequently,


$$
\boxed{
\begin{aligned}
&\Gamma_{\rho\sigma,D}
D_{\alpha,\rho}D_{\beta,\sigma}
C_{\alpha\beta;\rho\sigma}\\
&\qquad=
T_{\rho\sigma}(b)\mathcal A(b)R(b+1)
+\sum_{r=0}^{2}Q_rM_{\rho\sigma,r}.
\end{aligned}
}
\tag{9.11}
$$



#### Proof and fraction-free algorithm

Starting at degree $D$, use $\Delta j^{D-3}$ to remove the leading term. At each step:

- multiply the current identity by the nonzero pivot $k+\tau$;
- subtract the current leading coefficient times $\Delta j^k$;
- update the accumulated certificate polynomial.

This reduces the degree by at least one without any division. Continuing to degree $2$ gives (9.10). Equation (9.6) then gives (9.11). ∎

Since $T_{12}=T_{21}$, both complete outputs use only


$$
\boxed{
M_{11,0},M_{11,1},M_{11,2},\
M_{12,0},M_{12,1},M_{12,2},\
M_{22,0},M_{22,1},M_{22,2}.
}
$$



This removes the named obstruction of separately extracting every independent numerator shift. It is a new relation for the actual short numerators and actual finite cutoff, not a generic automaticity assertion.

---

## 10. Exact guard counts and the integral obstruction

The rational reduction cannot be executed by inverting its displayed denominators modulo $2^{20}$.

Here the valuations can be bounded—and, for the chosen multipliers, evaluated—using only short consecutive products.

From


$$
b\equiv721\pmod{1024},\qquad n\equiv834\pmod{1024},
$$


one obtains


$$
v_2(D_{f,1})=v_2(D_{e,1})=177,
$$




$$
v_2(D_{f,2})=258,\qquad
v_2(D_{e,2})=255.
$$



The complete multiplier valuations in (9.11) are


$$
\begin{array}{c|r|r|r}
\text{payload}&D&v_2(\Gamma)&
v_2(\Gamma D_{\alpha,\rho}D_{\beta,\sigma})\\ \hline
f1\,f1\text{ or }f1\,e1&354&349&703\\
f1\,f2\text{ or }f2\,e1&434&433&868\\
f1\,e2&430&430&862\\
f2\,f2&514&511&1027\\
f2\,e2&510&508&1021
\end{array}
\tag{10.1}
$$



For example, the $f2\,f2$ pivot product is a block of $512$ consecutive integers whose residues run from $288$ through $799$ modulo $1024$. Its valuation is


$$
256+128+64+32+16+8+4+2+1=511.
$$



Therefore a straightforward evaluation of (9.11), followed by exact division, has the sufficient pure-kernel precision bound


$$
\boxed{20+1027=1047\text{ bits}.}
\tag{10.2}
$$



This is a guard bound for the displayed, unsaturated reduction. It is **not** a proof that the actual observable requires $1047$ bits. Common factors and an integral basis may reduce the loss.

Nor does it require lifting the physical force or Schur solve to $1047$ bits: one may choose integer lifts of the known twenty-bit numerator coefficients. Changing those lifts changes the original integral kernel contraction by a multiple of $2^{20}$. The additional precision would be needed only to carry out the denominator-bearing kernel identity safely.

Nevertheless, a $1047$-bit moment evaluation has not been shown practical here. It is not a twenty-bit solution in disguise.

### 10.1 A sharply scoped obstruction to a three-state integral quotient

There is a more precise reason that the rational moment quotient must not be treated as an integral rank-three quotient.

Adjoin a formal boundary observable $\mathcal E$, and impose the polynomial telescoping relations


$$
\Delta j^k-(b+1)^k\mathcal E=0,
\qquad 0\le k\le D-3,
\tag{10.3}
$$


on the $D+1$ monomial moments and $\mathcal E$.

The relation matrix has size


$$
(D+2)\times(D-2).
$$



Modulo $2$, $N$ is even, $L$ is odd, and both $\rho n+b,\sigma n+b$ are odd. Hence


$$
\mathcal A(j)\equiv\mathcal B_{\rho\sigma}(j)
\equiv j^2(j+1)^2,
$$


so


$$
\Delta R\equiv j^2(j+1)^2\bigl(R(j+1)-R(j)\bigr).
\tag{10.4}
$$



Over $\mathbb F_2$, the kernel of $R(j)\mapsto R(j+1)-R(j)$ is


$$
\mathbb F_2[j^2+j].
$$


On polynomials of degree at most $D-3$, with the even values of $D$ in (9.9), the polynomial part has rank $(D-2)/2$. The boundary row adds one rank, because $b+1$ is even and its $k=0$ entry is nonzero.

Thus the full relation matrix has binary rank


$$
\boxed{D/2.}
\tag{10.5}
$$



Its rational rank is $D-2$. Therefore it has exactly


$$
\boxed{D/2-2}
$$


nonunit Smith pivots.

For the largest case $D=514$, this means:

- rational quotient dimension: $4$, including the boundary;
- binary quotient dimension: $259$;
- nonunit Smith pivots: $255$.

This proves a narrowly scoped obstruction: **the displayed polynomial-telescoping presentation is not an integral four-generator presentation**, even though its rational quotient has dimension four.

It does not rule out an observable quotient for the actual payloads, or a different Cartier compression.

Moreover, the sum of the nonunit Smith valuations is at most $v_2(\Gamma)$, because the leading triangular minor is $\Gamma$. For $D=514$, that sum is at most $511$. The integral obstruction is therefore bounded and explicitly inspectable; it is not an unspecified original-length phenomenon.

---

## 11. The concrete next lemma

The next target can now be stated more concretely than “find a small four-variable kernel module.”

> **Integral observable transport lemma.**  
> For the three summands $T_{11},T_{12},T_{22}$, the original cutoff $0\le j\le b$, and the six actual payloads in (9.9), construct binary target-section maps on a saturated observable quotient of the finite presentations (10.3). Retain the boundary observable (9.7), all nonunit Smith components that affect these payloads, and valuation-layer moduli $2^{20-a}$. Prove a uniform bounded presentation along the original target digit word and evaluate the two complete payload sums.

The outstanding issue is now the transport of a specific integral moment presentation, not unspecified closure under the complete force or Schur descendants. Those descendants are already contained in the four short polynomials.

---

# Part IV. Bounded exact arithmetic warranted now

## 12. A new numerator-and-moment certificate

This is a new bounded calculation. It does not repeat the accepted operator or endpoint computation.

### Inputs

- The exact $b,n$ above.
- The retained $\lambda_s,c_s,\overline K,S^{-1}$ modulo $2^{20}$.
- The coordinator’s complete normalized $f_0,\ldots,f_{47}$.
- The full factorial load $v_0,\ldots,v_{23}$.
- The fixed polynomial formulas in this report.

### Calculation A: complete numerator construction

1. Form (3.2).
2. Obtain the two endpoint right-hand sides and apply the retained $S^{-1}$.
3. Apply (3.7) with every prefix subtraction (3.8).
4. Collect the four contact polynomials.
5. Verify
   

$$
P_{<0}G_f=0,\qquad P_{<0}G_e^*=B_v.
$$


6. Verify the full reconstructed identity
   

$$
\mathfrak C_bB_v=-1+v_{24}z^{-24},
   \qquad v_{24}=0\pmod q.
$$


7. Remove the $44$ and $48$ factors of $1-z$ by synthetic division with zero remainders.
8. Produce the four shortened reconstructed coefficient lists in (4.10).
9. Verify the first $152$ nonnegative response coefficients from the finite convolution definitions, using the same retained endpoint action.
10. Verify the complete negative-coefficient cancellation needed for (6.3).

The symbolic band contribution bound from the previous report remains conservative:


$$
3003(48+76+100+76)=900900
$$


first-branch contributions before collection. The new synthetic divisions add fewer than $48\cdot302$ coefficient steps per relevant polynomial.

### Calculation B: exact polynomial moment certificates

For each of the six distinct payloads:

1. Construct the relevant $U$-polynomials by the monic synthetic-division procedure in §8.1.
2. Form their product.
3. Construct $R,Q_0,Q_1,Q_2,\Gamma$ by fraction-free reduction.
4. Verify the full polynomial identity (9.10), coefficient by coefficient.
5. Record the exact multiplier valuation from (10.1).

These are polynomial calculations of degree at most $514$, with small-degree multipliers $\mathcal A,\mathcal B$. They do not sum over $j=0,\ldots,b$.

### Calculation C: inspect the integral quotient

Form the matrices (10.3), of largest size


$$
\boxed{516\times512},
$$


and compute their $2$-primary Smith data, or an equivalent valuation-aware normal form, together with the images of the actual payloads.

The expected verifiable checks include:

- rational rank $D-2$;
- binary rank $D/2$;
- the corresponding number $D/2-2$ of nonunit pivots;
- total nonunit valuation at most the displayed $v_2(\Gamma)$;
- the actual payload coordinates in the resulting presentation.

This computation tests whether the actual observables avoid much of the torsion obstruction. It is not a weighted Gram evaluation unless the necessary moment observables are also evaluated.

### Required receipt distinction

The new certificate should report separately:

- numerator construction completed;
- all finite gluing residuals zero;
- shortened numerator lists produced;
- polynomial moment identities verified;
- integral presentation data computed;
- original weighted Gram pair evaluated or not evaluated.

No numerical value of $D_{\rm raw}$ or $E_{\rm raw}$ is predicted in this report.

---

## 13. Precision, contents, and the logarithmic term

No row content has been divided out in the numerator construction.

Let


$$
a=\min_jv_2(\mathsf a_j),\qquad
c=\min_jv_2(\mathsf b_j),
$$




$$
d_0=v_2(D_{\rm raw}),\qquad e_0=v_2(E_{\rm raw}).
$$


These remain unevaluated at the original index.

The ratio interface is still


$$
\frac HN=\frac{E_{\rm raw}}{2D_{\rm raw}}.
$$


Certified ratio accuracy modulo $2^s$ is ensured by


$$
M_E\ge s+d_0+1,
\qquad
M_D\ge s+2d_0+1-e_0,
$$


with the valuations themselves certified below the working depths.

The accepted bound


$$
K_{\rm norm}\ge2000b-138
$$


justifies omitting the logarithmic force in the present **absolute** twenty-bit numerator calculation.

It does not, without a norm bound, justify a norm-relative twenty-bit omission. A sufficient explicit inequality for the omitted mixed term is


$$
\boxed{
K_{\rm norm}+a-d_0-1\ge s,
}
\tag{13.1}
$$


using the coordinate-content lower bound on its contraction. Until the actual quantities on the right side of this comparison are controlled, no relative claim is made.

At higher physical precision, the complete logarithmic contribution, complete force, and endpoint data must all be supplied at that precision. The pure-kernel guard issue in §10 is separate from this physical-precision requirement.

---

## 14. Global arithmetic and irrationality status

Nothing above changes the all-prime reduction.

With the least actual two-column clearer $d_B$, retain the complete integer columns and


$$
A_B=N_{B,1}^{T}\Omega N_{B,1},\qquad
H_B=N_{B,1}^{T}\Omega N_{B,2}.
$$


Then


$$
g_B=\gcd(A_B,|H_B|),
\qquad
q_n=\frac{A_B}{g_B},
\qquad
p_n=\frac{H_B}{g_B}.
$$



The primitive multiplier remains


$$
\frac{d_B^2}{g_B}.
$$


A binary local calculation does not determine this all-prime gcd or the actual primitive denominator.

Likewise the relevant approximation quantity remains the whole same-index form


$$
q_n(e+\pi)-p_n=-q_n\epsilon_n.
$$



Conditional on the previously stated complete signed-error theorem,


$$
\log|\epsilon_n|
=
-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n),
$$


one still needs an infinite original subsequence on which the **actual** $q_n$ makes the whole nonzero form tend to zero. No such all-prime denominator estimate is proved here.

---

## 15. Proof-status ledger

| Item | Status |
|---|---|
| Original twenty-bit Schur inverse | Accepted finite input; not regenerated |
| Complete first head $f_0,\ldots,f_{47}$ | Coordinator input; normalization clarified |
| Entire exponential principal part | Retained and verified |
| Reconstruction of that principal part | **Proved:** $-1+v_{24}z^{-24}$ |
| Original $j=b$ coordinate and exterior $+1$ | **Verified** |
| Independent $x,y$ shifts and exponent $123$ | **Verified** |
| Integral band constructor with all prefix subtractions | **Specified explicitly** |
| Extra factors $(1-z)^{44}$, $(1-z)^{48}$ | **Proved** |
| Four shortened numerators, at most $868$ slots | **Proved bounds; coefficients not computed here** |
| Precision-layered factored Cartier update | **Exact recurrence and proved envelopes** |
| Practical complete Cartier evaluation at the original target | Not established |
| Reduction of actual numerator shifts to nine common moments | **Proved exact relation** |
| Original-cutoff telescoping boundary | **Explicit and retained** |
| Three-dimensional rational quotient usable as an integral three-state quotient | **Not valid without further work; obstruction quantified** |
| Bounded numerator, polynomial, and Smith calculations | New specifications; not executed here |
| Original weighted Gram pair, contents, norm-relative law | Not evaluated or certified |
| All-prime primitive denominator versus whole error | Open |
| Irrationality or rationality of $e+\pi$ | Unresolved |

---

## Conclusion

The new local result is stronger than the previous four-variable identity alone.

The full factorial principal part reconstructs to exactly the exterior correction, with a vanishing terminal remainder. The complete corrected columns then admit rigorously shortened integral numerators. Most importantly, their many independent numerator shifts reduce to **nine common truncated hypergeometric moments**, with an explicit original-cutoff boundary and a fraction-free polynomial certificate.

The exact remaining local bottleneck is:



$$
\boxed{
\text{Evaluate the integral observable moment data at the original target,
without discarding its nonunit components or unpaid precision guards.}
}
$$



The bounded calculation warranted now is the construction of the four actual shortened numerators, verification of the six polynomial moment certificates, and inspection of the associated matrices of size at most $516\times512$. It reuses the completed endpoint inverse and does not reopen that calculation.

Even a successful original Gram evaluation would remain a finite local result. A proof of irrationality by this route would still require an infinite-family argument and all-prime control of the actual primitive denominator against the whole same-index nonzero error.



$$
\boxed{\text{The irrationality of }e+\pi\text{ remains unproved here.}}
$$


