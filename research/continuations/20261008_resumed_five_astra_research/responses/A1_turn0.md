> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The next ternary projection: a paid finite-core reduction and an exact certificate target

## Abstract

The unconditional rationality or irrationality of $e+\pi$ is not resolved here.

This continuation makes two rigorous advances concerning the **actual original ternary matrices**, rather than an auxiliary completion.

1. **The factorial part can be removed from the local core calculation through precision $3^{30}$, including the actual LOW/HIGH inverse and its Schur complement.** This is not merely a moment congruence. The inverse loss is paid, the physical HIGH coordinate $Y_m$ is retained, and the resulting rational beta-moment matrix determines the same local projection digit.

2. **Only the first already-known lift through the finite unit prefix is needed to determine the next projection digit.** The entire LOW/HIGH-plus-prefix expression in A1 Turn 18, equation (7.4), is represented by one corrected pairing of the explicit original polynomials
   

$$
\Psi_a
   =
   x^{D+b}y^{k_0+a}\bigl(y^{P_0/3}+3\bigr),
   \qquad 0\le a\le b/2.
$$


   Higher prefix-inverse digits do not enter that coefficient: their contribution is a stationary quadratic error divisible by $81$ after normalization.

These results give a bounded certificate for the **actual projection coefficient**, together with separate certificates for the retained terminal amplitudes. They do **not** evaluate that coefficient as zero or nonzero. In particular, an explicit formula for a finite pairing is not being described as the missing evaluation.

The audit also preserves a qualification in the coordinator’s review: the elementary boundaries in A1 Turn 18’s full nonterminal strip are correct, and its first-return deduction is correct if that strip is established. The extension through every corrected-column support layer is not independently certified by the material reproduced here. The new projection reduction below does not depend on promoting that extension to an accepted theorem.

The remaining tasks are therefore sharply separated:

- finish the support-layer audit needed for the asserted terminal-only coupling;
- evaluate the actual corrected projection coefficient;
- carry the actual endpoint and diagonal through the paid eliminations;
- prove a directional inverse estimate or growing relative-cofactor saving;
- compare the **actual all-prime final gcd** with the **nonzero whole evaluated error at the same infinite original indices**.

---

## 1. Original domain and finite objects

All assertions concern sufficiently large indices in the unchanged original family


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




$$
m=2^{2j-1},\qquad n=4^j+1=2m+1,\qquad A=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$


subject to


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$



The fixed accepted subwindow remains


$$
\frac{103}{1000}<\frac{N_0}{P_0}<\frac{104}{1000},
$$


where


$$
P_0=243P=3^{h-27},\qquad N_0=243r,\qquad D=P_0+N_0,
$$




$$
P=3^{h-32},\qquad r\equiv2\pmod9,\qquad r\ \text{odd},
$$


and


$$
\boxed{4^j=243(3^{26}-1)P-243r+1.}
\tag{1.1}
$$



No arbitrary pair $(P,r)$ is substituted for an original $(j,h)$. The accepted density theorem is reused only to supply infinitely many original indices in this fixed window.

Put


$$
x=y-1,\qquad Q=P_0/9,\qquad b=Q-N_0.
$$


Then


$$
D=10Q-b,\qquad
\frac{64}{1000}<\frac bQ<\frac{73}{1000},
$$


and $b$ is an even positive multiple of $243$.

The finite polynomial coordinates are


$$
U_s=x^s\quad(0\le s<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),
$$




$$
Y_t=y^t\quad(d\le t\le m),
\qquad
\nu=D/2-1,\qquad d=D+\nu.
$$


The physical HIGH terminal is **$Y_m$**.

The residual indices are


$$
R_*=\frac{P_0+1}{2},\qquad
\tau=\frac{N_0-3}{2},\qquad
\ell=\frac{3b}{2}+1,
$$




$$
K=\{0,\ldots,\ell-1\},\qquad
J=\{\ell,\ldots,\tau-1\},
$$




$$
n_J=\tau-\ell=\frac{Q-4b-5}{2},\qquad E=\frac{Q-3}{2}.
$$


Notice that


$$
R_*+\tau=\nu.
$$


Thus the last middle direction is $z_{\nu-1}$, represented in the $J$-block by


$$
\delta_J=e_{n_J-1}.
$$


This last middle direction and the physical HIGH coordinate $Y_m$ must not be conflated.

### 1.1 Complete functional and exact correction

The functional is


$$
\mathcal M(P)=
-\frac{3^h}{4}\mathfrak f(P)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](P-P(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^t)=(2t)!,
\tag{1.2}
$$


on polynomials of degree at most $2n-1$.

Its physical pole cutoff is


$$
2v+1\le4n-3=4H-4D+5<3^{h+1}.
\tag{1.3}
$$


Consequently $3^h$ pays every ternary pole denominator.

The complete core is


$$
G_c(f,g)=\mathcal M(Q_cfg),
\qquad
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=-71-A.
$$


Let $W=[U\ Y]$, and write


$$
E_c=G_c(W,W),\qquad C_i=G_c(W,z_i),
$$




$$
F_i=z_i-WE_c^{-1}C_i.
\tag{1.4}
$$


These are the actual corrected columns. In particular,


$$
G_c(W,F)=0,\qquad S_c=G_c(F,F).
$$



The following established results are reused at their stated original scope:

- $[W,F]$ is integral unimodular;
- $E_c^{-1},E_{\rm act}^{-1}\in3^{-1}M$;
- $S_c\in3^{26}M$;
- the finite unit-prefix inverse and selector;
- H2, including its rank, radical and endpoint consequences;
- the accepted complete diagonal valuation;
- the already paid $3^{-2}$ rank-$b$ elimination;
- the complete first producer-return difference established using the closed adjoining boundary.

None of their closed large calculations is repeated.

---

## 2. Audit of the new strip and the first return

### 2.1 The elementary finite-boundary checks are correct

For the proposed full nonterminal strip


$$
0\le u<\ell,\qquad \ell\le v\le\tau-2,
$$


put $s=u+v$. The exact upper bound is


$$
s\le\frac Q2+b-\frac72.
$$


Hence the low polynomial used in A1 Turn 18 has degree at most


$$
19Q-b+2+s\le\frac{39Q-3}{2}<2D.
$$



The principal extraction index satisfies


$$
k=\frac{9Q-3}{2}-s\ge4Q-b+2
=3Q+N_0+2.
$$


Thus the claimed two-position margin beyond the $3Q$-band is genuine.

The finite prefix correction has coefficient index


$$
C-u-v,\qquad C=\frac{3Q-3}{2},
$$


and


$$
C-u-v\ge N_0+2.
$$


This verifies the asserted finite polynomial-degree exclusion. It does not require extending the prefix sum to an unrestricted infinite matrix.

These checks do not reopen the already closed first adjoining boundary.

### 2.2 What is not independently supplied by those checks

The essential corrected-column assertion is


$$
(S_c)_{R_*+u,R_*+v}
\equiv G_c(z_{R_*+u},z_{R_*+v})
\pmod{3^{29}}
\tag{2.1}
$$


throughout the enlarged strip.

The displayed degree inequalities and low jets do not, by themselves, prove (2.1). Its proof also invokes uniform higher-digit support statements for the actual corrected columns. The coordinator’s late review expressly leaves that extension pending independent review.

More precisely, if a representative is expanded as


$$
F_i^*=\sum_r3^r f_{i,r},
$$


then every retained product $f_{i,r}f_{j,s}$ must be checked against all poles for which


$$
r+s+h-v_3(2v+1)<29.
\tag{2.2}
$$


A proof must either exclude the corresponding physical coefficient positions or supply the additional coefficient divisibility. A growing-grid description without its quantified supports is not a replacement for this check.

I therefore make the following scoped judgment:

- the elementary boundaries and raw extractions in the full-strip argument pass the present audit;
- no counterexample to the strip is obtained;
- the full corrected support-layer extension is not promoted here to an independently completed theorem.

The new results in Sections 3–5 concern the actual projection without requiring that promotion.

### 2.3 The first-return deduction is valid once terminal-only support is known

If the full strip is established, contraction with


$$
g_a=x^by^a,\qquad 0\le a\le b/2,
$$


gives


$$
G^T\bar L_c=\gamma_c\delta_J^T,
\qquad
\gamma_c=G^T\bar L_c\delta_J.
\tag{2.3}
$$


The terminal amplitude is retained.

The accepted finite identities


$$
\bar B^{-1}\delta_J=-e_0,\qquad
\delta_J^T\bar B^{-1}\delta_J=0
$$


then give


$$
G^TL_cB_c^{-1}L_c^TG\equiv0\pmod3,
$$


and hence


$$
27G^TL_cB_c^{-1}L_c^TG\in81M.
\tag{2.4}
$$



This deduction is sound. It does not imply that the endpoint return vanishes, because


$$
\delta_J^T\bar B^{-1}\bar f_J=-\varepsilon_0
$$


is a unit.

### 2.4 The raw precision-$30$ theorem has only its stated scope

The binomial-valuation argument in A1 Turn 18 applies to


$$
(Z_G)_a=x^{D+b}y^{R_*+a}
$$


and gives


$$
G_c(Z_G,Z_G)\in3^{30}M.
\tag{2.5}
$$


Its proof uses the complete finite pole sum, the retained $3^h$ payment of the factorial term, and the actual coefficient intervals.

Nothing in that argument evaluates


$$
G_c(F_G,F_G).
$$


The correction cannot be deleted from the next digit.

---

## 3. New theorem: the actual local projection is unchanged by paid removal of the factorial part

This section proves a result about the actual LOW/HIGH inverse. It is stronger than dropping a factorial term from a raw moment calculation.

Define the finite pole form


$$
\mathcal P(f,g)
=
3^h\sum_{v=0}^{2n-2}
\frac{[y^v]x^A(\beta+3y)f(y)g(y)}{2v+1}.
\tag{3.1}
$$


Because $Q_cfg$ is divisible by $y+1$, this is exactly the pole part of the complete core. Thus


$$
\mathcal P=G_c+3^h\mathcal T,
\qquad
\mathcal T(f,g)=\frac14\mathfrak f(Q_cfg).
\tag{3.2}
$$


For integral degree-$\le m$ polynomials, $\mathcal T$ is integral over $\mathbb Z_3$.

Let


$$
E_{\mathcal P}=\mathcal P(W,W),\qquad
C_{\mathcal P,i}=\mathcal P(W,z_i),
$$




$$
F_{\mathcal P,i}
=z_i-WE_{\mathcal P}^{-1}C_{\mathcal P,i},
\qquad
S_{\mathcal P}=\mathcal P(F_{\mathcal P},F_{\mathcal P}).
$$



### Theorem 3.1 — Paid pole replacement through the actual projection

For $h\ge2$,


$$
E_{\mathcal P}^{-1}\in3^{-1}M,
\tag{3.3}
$$




$$
F_{\mathcal P}-F\in3^{h-1}W M,
\tag{3.4}
$$


and


$$
\boxed{S_{\mathcal P}-S_c\in3^hM.}
\tag{3.5}
$$



In particular, for $h\ge30$, the pole form and complete core determine the same corrected core pairings modulo $3^{30}$.

#### Proof

Work in the actual integral unimodular basis $[W,F]$. Exact orthogonality gives the complete-core matrix


$$
\begin{pmatrix}E_c&0\\0&S_c\end{pmatrix}.
$$


In the same basis, the pole matrix is


$$
\begin{pmatrix}
E_c+3^hT_{WW}&3^hT_{WF}\\
3^hT_{FW}&S_c+3^hT_{FF}
\end{pmatrix},
\tag{3.6}
$$


where every $T$-block is integral.

Since $E_c^{-1}\in3^{-1}M$,


$$
3^hE_c^{-1}T_{WW}\in3^{h-1}M.
$$


For $h\ge2$, the matrix $I+3^hE_c^{-1}T_{WW}$ has an integral inverse. Therefore


$$
(E_c+3^hT_{WW})^{-1}\in3^{-1}M.
$$


This proves (3.3), including the inverse loss.

The pole-corrected columns are


$$
F_{\mathcal P}
=
F-W(E_c+3^hT_{WW})^{-1}3^hT_{WF}.
$$


Thus their difference from the actual complete-core columns is in $3^{h-1}WM$, proving (3.4).

Taking the Schur complement in (3.6),


$$
S_{\mathcal P}
=
S_c+3^hT_{FF}
-
3^{2h}T_{FW}(E_c+3^hT_{WW})^{-1}T_{WF}.
$$


The last term has valuation at least $2h-1$, which is at least $h$. This proves (3.5). ∎

### 3.1 Consequences for the projection and physical terminal

For any original integral middle combination $Z$, put


$$
\Gamma_c(Z)=G_c(W,Z)^TE_c^{-1}G_c(W,Z),
$$


with the corresponding bilinear interpretation for several columns. Define $\Gamma_{\mathcal P}$ using the pole form.

The raw Gram matrices differ by $3^hM$, and the corrected Gram matrices differ by $3^hM$. Hence


$$
\boxed{\Gamma_{\mathcal P}(Z)-\Gamma_c(Z)\in3^hM.}
\tag{3.7}
$$


Thus $\Gamma_G/3^{29}\pmod3$ may be computed from the finite pole form when $h\ge30$.

Equation (3.4) also retains the physical HIGH coefficient:


$$
[y^m](F_{\mathcal P,i}-F_i)\in3^{h-1}\mathbb Z_3.
$$


Therefore the actual terminal residue


$$
t_i=\frac{[y^m]F_i}{3^{20}}
$$


has the same reduction modulo $3$ as its pole-projection counterpart whenever $h\ge22$.

This is not an assertion that $t_i=0$. It is a paid method of determining its actual residue.

### 3.2 Passage through the finite prefix

Set


$$
U_c=-S_c/3^{26},\qquad U_{\mathcal P}=-S_{\mathcal P}/3^{26}.
$$


Then


$$
U_{\mathcal P}-U_c\in3^{h-26}M.
$$


For $h\ge30$, this difference is in $81M$. The prefix block remains a unit block, and its exact corrected lifts are integral. A stationary Schur-complement expansion therefore gives


$$
\mathcal R_{\mathcal P}-\mathcal R_c\in81M.
\tag{3.8}
$$


The same local normalized digit is preserved.

This does **not** authorize replacing the complete real determinant in the final error by a pole determinant. The replacement is local and $3$-adic.

---

## 4. Explicit finite beta entries, with every denominator paid

The pole form has an elementary exact rational evaluation.

For $N,s\ge0$, define


$$
I_N(s)
=
\frac12\int_0^1y^{s-1/2}(1-y)^N\,dy
=
\frac{2^NN!}{\prod_{k=0}^{N}(2s+2k+1)}.
\tag{4.1}
$$


For


$$
f=x^uy^r,\qquad g=x^vy^t,
$$


put


$$
N=A+u+v,\qquad s=r+t.
$$


Then


$$
\boxed{
\mathcal P(f,g)
=
3^h(-1)^N\bigl(\beta I_N(s)+3I_N(s+1)\bigr).
}
\tag{4.2}
$$


Equivalently,


$$
\boxed{
\mathcal P(f,g)=
\frac{
3^h(-1)^N2^NN!
\bigl(\beta(2s+2N+3)+3(2s+1)\bigr)}
{\prod_{k=0}^{N+1}(2s+2k+1)}.
}
\tag{4.3}
$$



The identity follows either by integrating the finite binomial expansion or by the beta recurrence


$$
\frac{I_N(s+1)}{I_N(s)}
=\frac{2s+1}{2s+2N+3}.
$$



### 4.1 The physical cutoff is unchanged

For every pairing used here,


$$
N+s+1\le2n-2.
$$


Consequently the largest odd denominator in (4.3) satisfies


$$
2s+2N+3\le4n-3.
$$


No pole outside the original functional has been introduced.

### 4.2 Modular evaluation without unpaid division

For the first term in (4.2), put


$$
a(N,s)
=
h+v_3(N!)
-\sum_{k=0}^{N}v_3(2s+2k+1).
\tag{4.4}
$$


The finite pole identity and the physical cutoff imply $a(N,s)\ge0$.

After stripping powers of $3$,


$$
3^h I_N(s)
=
3^{a(N,s)}2^N
\frac{
\prod_{r=1}^{N}r/3^{v_3(r)}
}{
\prod_{k=0}^{N}(2s+2k+1)/3^{v_3(2s+2k+1)}
}.
\tag{4.5}
$$


Every denominator in the last quotient is a ternary unit.

To compute modulo $3^{30}$:

- if $a(N,s)\ge30$, the term is zero;
- otherwise evaluate the unit quotient modulo $3^{30-a(N,s)}$;
- perform the analogous calculation for $I_N(s+1)$;
- combine the two complete terms with their factors $\beta$ and $3$.

This accounts explicitly for denominators of valuation $h$, if present. It is not a uniformly stable forward moment recurrence.

The new point in Sections 3–4 is not a new beta identity or a rediscovery of a classical Gram diagonalization. It is the proof that these finite rational entries determine the **same actual corrected projection digit after the paid inverse**.

---

## 5. New theorem: one known prefix lift determines the next projection coefficient

Write the normalized complete-core matrix as


$$
U_c=
\begin{pmatrix}
\mathsf A&\mathsf B\\
\mathsf B^T&\mathsf C
\end{pmatrix},
\qquad
\mathcal R_c=\mathsf C-\mathsf B^T\mathsf A^{-1}\mathsf B.
$$



Put


$$
a_0=R_*-1=\frac{P_0-1}{2},\qquad
J_0=P_0/3-1,
$$




$$
k_0=a_0-J_0=\frac{P_0/3+1}{2}.
$$


The closed finite selector is


$$
\bar{\mathsf A}^{-1}
\overline{\mathsf B_{\cdot,u}/3}
=-e_{k_0+u}\qquad(u\in K).
\tag{5.1}
$$


Its calculation is reused, not repeated.

Let $P_G$ be the prefix-coordinate matrix obtained by placing the coefficients of $g_a=x^by^a$ at positions $k_0+u$. These positions lie inside the original prefix because


$$
k_0+\ell-1
=\frac{3Q+1+3b}{2}<a_0
$$


for sufficiently large original indices.

Define


$$
\Psi_a
=
x^{D+b}\bigl(y^{R_*+a}+3y^{k_0+a}\bigr)
=
x^{D+b}y^{k_0+a}(y^{3Q}+3).
\tag{5.2}
$$


Since $3Q=P_0/3$, these are exactly the polynomials stated in the abstract.

They remain inside the original degree bound. Indeed,


$$
d-\deg\Psi_a
\ge \tau-\frac{3b}{2}
=n_J+1>0.
\tag{5.3}
$$



Let


$$
\mathcal F_a
=
\Psi_a-WE_c^{-1}G_c(W,\Psi_a).
\tag{5.4}
$$


By linearity,


$$
\mathcal F=F_{\rm tail}G+3F_{\rm prefix}P_G.
$$



### Theorem 5.1 — Stationary one-lift formula

On the original family,


$$
\boxed{
G^T\mathcal R_{c,KK}G
\equiv
-\frac{G_c(\mathcal F,\mathcal F)}{3^{26}}
\pmod{81}.
}
\tag{5.5}
$$


Moreover,


$$
G_c(\mathcal F,\mathcal F)\in3^{29}M.
\tag{5.6}
$$



Consequently the actual LOW/HIGH-plus-prefix projection coefficient is


$$
\boxed{
\Pi:=
\frac{G^T\mathcal R_{c,KK}G}{27}\pmod3
=
-\frac{G_c(\mathcal F,\mathcal F)}{3^{29}}\pmod3.
}
\tag{5.7}
$$



#### Proof

Write $\mathsf B_G=\mathsf B_KG$. By (5.1),


$$
\mathsf A^{-1}\mathsf B_G\equiv-3P_G\pmod9.
$$


Thus the exact prefix coefficient


$$
X=-\mathsf A^{-1}\mathsf B_G
$$


has the form


$$
X=3P_G+9Z
$$


for an integral matrix $Z$.

The exact prefix-orthogonal lift is represented in normalized coordinates by $(X,G)$. The trial lift $(3P_G,G)$ differs from it by $(-9Z,0)$, a vector entirely in the prefix space.

Exact orthogonality removes both linear errors. Therefore


$$
-\frac{G_c(\mathcal F,\mathcal F)}{3^{26}}
=
G^T\mathcal R_{c,KK}G+81Z^T\mathsf AZ.
\tag{5.8}
$$


This proves (5.5).

H2 supplies


$$
G^T\mathcal R_{c,KK}G\in27M.
$$


Equation (5.8) then proves (5.6), including the whole division by $3^{29}$. Dividing (5.8) by $27$ and reducing modulo $3$ proves (5.7). ∎

### 5.1 Relation to equation (7.4)

The complete raw theorem (2.5) and the exact LOW/HIGH Schur identity give


$$
\Pi
=
\frac{\Gamma_G}{3^{29}}
-
\frac{G^T\mathsf B^T\mathsf A^{-1}\mathsf BG}{27}
\pmod3.
\tag{5.9}
$$


Thus (5.7) concerns precisely the actual projection difference in equation (7.4).

If terminal-only coupling and (2.4) are established, then


$$
\Pi=\frac{G^T\mathcal S_c^{(2)}G}{27}\pmod3.
$$


Without that additional acceptance, the complete second-radical coefficient is


$$
\frac{G^T\mathcal S_c^{(2)}G}{27}
=
\Pi-\overline{G^TL_cB_c^{-1}L_c^TG}.
\tag{5.10}
$$



The one-lift theorem does not silently set the last term to zero.

### 5.2 What has actually advanced

The actual prefix inverse no longer needs to be known beyond its closed first selector in order to determine $\Pi$. Its higher digits contribute only the explicitly paid $81Z^T\mathsf AZ$.

What has **not** advanced to an evaluated result is the residue


$$
-G_c(\mathcal F,\mathcal F)/3^{29}\pmod3.
$$


It remains an actual corrected pairing, not a raw pairing.

---

## 6. Exact certificates for the projection and terminal amplitudes

The preceding reduction admits a certificate that does not require a claimed exact inverse.

### Proposition 6.1 — A residual modulo $3^{16}$ certifies a pairing modulo $3^{30}$

Let $\Psi$ be one of the original integral combinations above, or an integral combination of them. Suppose an integral vector $q$ satisfies


$$
E_{\mathcal P}q-\mathcal P(W,\Psi)\in3^{16}\mathbb Z_3^{\dim W}.
\tag{6.1}
$$


Set


$$
\widehat F=\Psi-Wq.
$$


Then, for two such certificates,


$$
\boxed{
\mathcal P(\widehat F,\widehat F')
\equiv
G_c(\mathcal F,\mathcal F')
\pmod{3^{30}}.
}
\tag{6.2}
$$



#### Proof

Let


$$
q_{\rm ex}=E_{\mathcal P}^{-1}\mathcal P(W,\Psi).
$$


By Theorem 3.1, the inverse loses at most one digit. Thus (6.1) gives


$$
q-q_{\rm ex}\in3^{15}\mathbb Z_3^{\dim W}.
$$


The exact pole-corrected column $F_{\mathcal P,\Psi}$ is orthogonal to $W$. Consequently


$$
\mathcal P(\widehat F,\widehat F')
-
\mathcal P(F_{\mathcal P,\Psi},F_{\mathcal P,\Psi'})
=
(q-q_{\rm ex})^TE_{\mathcal P}(q'-q'_{\rm ex})
\in3^{30}\mathbb Z_3.
$$


Theorem 3.1 identifies the exact pole and complete-core corrected pairings modulo $3^{30}$. ∎

This proof uses stationary error, not an uncontrolled substitution in a mixed pairing.

### 6.1 A separate certificate is needed for the physical terminal

Fifteen digits of a corrected column determine its stationary pairing at this precision. They do **not** determine its coefficient divided by $3^{20}$.

For a raw combination $Z$ of degree below $m$, suppose


$$
E_{\mathcal P}q_Z-\mathcal P(W,Z)\in3^{22}\mathbb Z_3^{\dim W}.
\tag{6.3}
$$


Then


$$
q_Z-q_{Z,\rm ex}\in3^{21}\mathbb Z_3^{\dim W}.
$$


Since $Z$ itself has no $y^m$-coefficient,


$$
\boxed{
\frac{[y^m]F_Z}{3^{20}}
\equiv
-\frac{(q_Z)_{Y_m}}{3^{20}}
\pmod3.
}
\tag{6.4}
$$


The whole division is paid by the accepted $3^{20}$ terminal divisibility and the $3^{21}$ error.

The coordinate in (6.4) is the actual physical $Y_m$-coordinate.

### 6.2 The retained middle-terminal coupling also has a one-lift certificate

Let $F_T=F_{\nu-1}$ be the exact corrected last middle column. Since the full prefix-to-tail block is in $3M$, the same first lift gives


$$
\boxed{
(\gamma_c)_a
=
-\frac{G_c(\mathcal F_a,F_T)}{3^{28}}\pmod3.
}
\tag{6.5}
$$



Indeed, the difference between the exact prefix lift and $3P_G$ is $9Z$; pairing it with the terminal prefix cross-column contributes $9Z^T\mathsf B_T\in27M$ in normalized coordinates. Division by $9$ therefore removes no uncontrolled residue.

Both columns in (6.5) can be certified by residuals modulo $3^{16}$. Their pairing is then known modulo $3^{30}$, more than the $3^{29}$ needed for (6.5).

Thus the projection coefficient, the middle-terminal amplitude, and the physical-HIGH amplitude have different, explicit precision requirements:

| Quantity | Residual precision | Inverse loss | Final observation |
|---|---:|---:|---:|
| $\Pi_{ac}$ | $3^{16}$ | one digit | pairing divided by $3^{29}$, modulo $3$ |
| $(\gamma_c)_a$ | $3^{16}$ | one digit | pairing divided by $3^{28}$, modulo $3$ |
| $G^T\bar t_K$ | $3^{22}$ | one digit | physical coefficient divided by $3^{20}$, modulo $3$ |

No terminal amplitude is inferred from its unit status or from a nonterminal continuation.

---

## 7. Complete producer, endpoint and diagonal returns

The producer is not changed:


$$
Q_{\rm act}=3P_n=Q_c+3^7\mathscr R,
$$




$$
3^7\mathscr R=\sum_{a=0}^{A+1}e_ax^a,
\qquad
e_a=-\frac{(A+1)!}{a!}(t_a+\xi v_a),
$$


with complete force


$$
t=3nh_{\rm vec}
+(b_{\rm force}+6)e_{n-1}
+\frac{2b_{\rm force}}{n-1}e_{n-2},
\qquad b_{\rm force}=-n-66.
\tag{7.1}
$$


The signed $\xi$, with its previously paid normalization, is retained.

Also retain


$$
\mathscr R(-1)
=-\frac{\xi((A+1)!)^2}{3^7},
$$


and


$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
\tag{7.2}
$$



The new pole replacement theorem concerns the local complete-core projection. It does not delete any component of (7.1)–(7.2).

### 7.1 First-radical returns

For $\alpha=c,\mathrm{act}$,


$$
\mathcal R_{\alpha,JJ}=3B_\alpha,\qquad
\mathcal R_{\alpha,KJ}=9L_\alpha,
$$




$$
\mathcal S_\alpha^{(2)}
=\mathcal R_{\alpha,KK}
-27L_\alpha B_\alpha^{-1}L_\alpha^T,
$$




$$
f_\alpha^{(2)}
=f_{\alpha,K}-3L_\alpha B_\alpha^{-1}f_{\alpha,J},
\tag{7.3}
$$




$$
\lambda_\alpha^{(2)}
=\lambda_\alpha-\frac13f_{\alpha,J}^TB_\alpha^{-1}f_{\alpha,J}.
\tag{7.4}
$$


The inverse cost is $3^{-1}$.

If terminal-only coupling holds, put


$$
\widehat t=G^T\bar t_K,\qquad
\gamma_{\rm act}=\gamma_c+\bar\kappa\,\widehat t.
$$


Then


$$
G^Tf_\alpha^{(2)}
\equiv G^Tf_{\alpha,K}+3\varepsilon_0\gamma_\alpha\pmod9.
\tag{7.5}
$$


The accepted producer differences remain


$$
f_{\rm act}^{(2)}-f_c^{(2)}
\equiv3\bar\kappa\varepsilon_0\bar t_K\pmod9,
$$




$$
\lambda_{\rm act}^{(2)}-\lambda_c^{(2)}
\equiv
-2\bar\kappa\varepsilon_0(\bar t_J^Tu_0)\pmod3,
\qquad u_0=\bar B^{-1}\bar f_J.
\tag{7.6}
$$



Neither $\widehat t$, $\gamma_c$, nor $\bar t_J^Tu_0$ has been evaluated here. The certificates in Section 6 describe how actual entries can be determined; they do not supply their values.

### 7.2 The rank-$b$ return remains paid in all three channels

Write its invertible block and radical coupling as


$$
D_b=9A_b,\qquad K_{bR}=27M_b,
\qquad A_b^{-1}\in M.
$$


The exact subsequent returns have the form


$$
T_{\rm new}=T_{RR}-81M_b^TA_b^{-1}M_b,
$$




$$
f_{\rm new}=f_R-3M_b^TA_b^{-1}f_b,
$$




$$
\lambda_{\rm new}
=\lambda^{(2)}-\frac19f_b^TA_b^{-1}f_b.
\tag{7.7}
$$


Thus its matrix return does not change the order-$27$ radical digit. Its endpoint and diagonal returns cannot be omitted.

The accepted complete diagonal valuation is retained:


$$
v_3(\lambda_{\rm new})=-1.
$$


This is a valuation of the complete returned diagonal, not a license to divide or discard its individual summands.

---

## 8. A concrete conditional connection to the directional inverse

The endpoint-annihilating coefficient combinations are


$$
g_a+g_{a+1}=(y+1)x^by^a,
\qquad 0\le a<b/2.
$$


Let $V$ have columns $e_a+e_{a+1}$. These columns span the leading endpoint-annihilating subspace. The actual higher endpoint lifts are still required; because the residual matrix lies in $27M$, changes to these lifts by $3M$ do not change its first normalized matrix digit.

Let


$$
\mathcal D
=
\frac{G^T\mathcal S_{\rm act}^{(2)}G}{27}\pmod3.
$$


The accepted complete producer-return theorem identifies this with the core coefficient. If the full nonterminal strip is accepted, then $\mathcal D=\Pi$. Otherwise the correction in (5.10) remains.

After the paid rank-$b$ elimination, the actual endpoint-adapted block is


$$
T=\begin{pmatrix}a&z^T\\z&C\end{pmatrix}\in27M,
\qquad v_3(\lambda)=-1.
$$



### Proposition 8.1 — An evaluated nonsingular digit would give a paid directional bound

If


$$
\det(V^T\mathcal D V)\ne0\quad\text{in }\mathbb F_3,
\tag{8.1}
$$


then the actual $C$ is nonsingular and


$$
\boxed{C^{-1}z\in\mathbb Z_3^{b/2}.}
\tag{8.2}
$$



If additionally


$$
s=a-z^TC^{-1}z\ne0,
$$


then


$$
v_3D_0-v_3D_1\ge3,
$$


where


$$
D_0=\det T,\qquad D_1=\det C-\lambda\det T.
$$



#### Proof

Condition (8.1) says that $C/27$ is invertible modulo $3$, up to the retained integral unit congruence from endpoint adaptation. Write


$$
C=27B,\qquad z=27w.
$$


Then $B^{-1}$ is integral and


$$
C^{-1}z=B^{-1}w\in\mathbb Z_3^{b/2}.
$$


Also $s\in27\mathbb Z_3$, so $\lambda s\in9\mathbb Z_3$. Hence


$$
D_0=\det C\,s,\qquad
D_1=\det C(1-\lambda s),
$$


and $1-\lambda s$ is a unit. The stated gain follows when $s\ne0$. ∎

This is a conditional implication, not a verified hypothesis. No determinant in (8.1) has been evaluated.

It also yields only a fixed local gain. A growing relative saving would require stronger information, for example


$$
v_3(a-z^TC^{-1}z)\longrightarrow\infty
$$


on the same original indices, while retaining nonzero scalar factors.

### 8.1 The resonant divisor has not disappeared

The complete moments still satisfy


$$
\mu_{t+1}+\mu_t
=
\frac{3^h}{2t+1}
-\frac{3^h}{4}\bigl((2t+2)!+(2t)!\bigr),
\qquad 0\le t\le2n-2.
\tag{8.3}
$$


The accepted forward recurrence has a genuine divisor of valuation $h$ at


$$
t_*=\frac{3^h-5}{2}.
$$


Its highest moment is


$$
T_*=\frac{3H+1}{2}\le2n-1,
$$


because $H-4D+5>0$ on the original window.

The beta-product evaluation includes the corresponding denominators. It does not cancel the resonant divisor or prove a uniform forward-solve bound.

If the directional criterion remains unavailable, the exact critical scalar remains


$$
\mathcal R=1-9\eta\alpha+9\eta\sigma,
$$


where


$$
a=27\alpha,\quad z=27w,\quad C=27B,\quad
\lambda=\eta/3,\quad
\sigma=\frac{w^T\operatorname{adj}(B)w}{\det B}.
\tag{8.4}
$$


Nonsingularity of the actual $B$, and nonresonance in the critical shell $v_3(\sigma)=-2$, are still open.

---

## 9. Bounded exact-arithmetic calculation for a genuinely new coefficient

No computation was performed. No closed $350$- or $62$-coordinate calculation, old producer calculation, first boundary, or raw radical cancellation is requested.

The following is a **certificate checker for one supplied original index**, not an unbounded search for an index or an instruction to reconstruct a dense producer.

### 9.1 Finite mathematical inputs

Supply one specified admissible original $(j,h)$, including verification of (1.1) and the fixed window.

Let


$$
s_W=\dim W=m-\nu+1.
$$


Use the first endpoint-annihilating direction


$$
Z_H=(y+1)x^{D+b}y^{R_*},
$$




$$
\Psi_H=(y+1)x^{D+b}y^{k_0}(y^{3Q}+3),
$$


and the last raw middle column


$$
z_T=z_{\nu-1}.
$$



Supply three finite residue vectors:

1. $q_\Psi\in\{0,\ldots,3^{16}-1\}^{s_W}$, satisfying
   

$$
E_{\mathcal P}q_\Psi\equiv\mathcal P(W,\Psi_H)\pmod{3^{16}};
$$


2. $q_T$ of the same size and precision, satisfying
   

$$
E_{\mathcal P}q_T\equiv\mathcal P(W,z_T)\pmod{3^{16}};
$$


3. $q_Z\in\{0,\ldots,3^{22}-1\}^{s_W}$, satisfying
   

$$
E_{\mathcal P}q_Z\equiv\mathcal P(W,Z_H)\pmod{3^{22}}.
$$



These are certificates to check, not presumed solutions.

All required matrix entries are given by (4.2). The polynomials $\Psi_H$ and $Z_H$ have respectively at most four and two terms of the form $x^uy^r$, so no large polynomial expansion is necessary for their pairings.

### 9.2 Explicit finite work bound

There are at most


$$
\frac{s_W(s_W+1)}2+7s_W+25
$$


basic pairings needed for these residuals and observations.

Each basic pairing can be evaluated using the unit-factor products in (4.5), with all factor indices bounded by $4n-3$. A conservative bound of


$$
1000\,n(s_W+8)^2(h+1)
$$


bounded-integer arithmetic operations suffices for a direct certificate check. This is not a claim of practical feasibility at every original index; it is an explicit finite mathematical bound determined before a particular check is admitted.

If no original tuple and certificate packet within the coordinator’s chosen size limit is available, the outcome is simply **no eligible finite certificate packet**. An auxiliary $(P,r)$-model is not a substitute.

### 9.3 Expected verifiable outputs

Set


$$
\widehat F_\Psi=\Psi_H-Wq_\Psi,\qquad
\widehat F_T=z_T-Wq_T.
$$



The checker should output:

1. The exact residue
   

$$
N\equiv\mathcal P(\widehat F_\Psi,\widehat F_\Psi)
   \pmod{3^{30}},\qquad 0\le N<3^{30}.
$$


   The proved divisibility requires $3^{29}\mid N$. The new coefficient is
   

$$
\boxed{\Pi_H\equiv-N/3^{29}\pmod3.}
$$



2. The exact residue
   

$$
M\equiv\mathcal P(\widehat F_\Psi,\widehat F_T)
   \pmod{3^{29}},\qquad 0\le M<3^{29}.
$$


   The proved divisibility requires $3^{28}\mid M$. The retained middle-terminal amplitude is
   

$$
\boxed{\gamma_H\equiv-M/3^{28}\pmod3.}
$$



3. The physical HIGH-terminal residue
   

$$
\boxed{
   \widehat t_H
   \equiv-(q_Z)_{Y_m}/3^{20}\pmod3.
   }
$$


   Its divisibility check must precede the division.

If the previously authored producer packet supplies $\bar\kappa$, then


$$
\gamma_{{\rm act},H}
=\gamma_H+\bar\kappa\,\widehat t_H
$$


is also determined.

No output is predicted in advance. A zero or nonzero output establishes only the stated coefficient at that one original index. It does not prove an eventual vanishing law, an infinite nonsingularity statement, or a growing saving.

---

## 10. Divisions, actual contents, all-prime gcd and whole error

### 10.1 Division ledger

| Operation | Payment retained |
|---|---|
| Complete pole denominators | $3^h$, on the physical cutoff $4n-3$ |
| Factorial removal in the local calculation | Theorem 3.1, including the inverse loss |
| Original producer normalization | Existing $3^7$ division and signed-$\xi$ normalization |
| LOW/HIGH inverse | $3^{-1}$ |
| Core normalization | $S_c/3^{26}$ |
| Unit prefix | Integral unit inverse |
| First prefix lift | Error $9Z$; stationary return $81Z^T\mathsf AZ$ |
| First-radical inverse | $3^{-1}B_\alpha^{-1}$ |
| Rank-$b$ inverse | $3^{-2}A_b^{-1}$ |
| Projection observation | Whole pairing divided by $3^{29}$ |
| Middle-terminal observation | Whole pairing divided by $3^{28}$ |
| Physical-terminal observation | Actual coefficient divided by $3^{20}$ |
| Residual certificate | One inverse digit lost: $16\to15$, or $22\to21$ |
| Resonant forward solve | Genuine $3^h$ divisor, not uniformly removed |
| Eventual $C^{-1}$ | Still unproved except under explicit conditional hypotheses |

There is no new content division.

### 10.2 The original clearers and contents are not replaced by beta denominators

Retain the actual column contents and the actual least simultaneous clearer $\ell_{\rm clr}$. The rational beta denominators used for a local $3$-adic certificate are not a new global clearer.

The final integers remain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


and


$$
\boxed{g_\ell=\gcd(|A_\ell|,|B_\ell|)}
$$


is the gcd over **all primes**.

For $B_\ell\ne0$, the actual primitive numerator and denominator are


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
\tag{10.1}
$$


Common determinant depths of eliminated blocks are not, by themselves, primitive-denominator savings.

The whole evaluated error is still


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
{g_\ell}\det H_{\rm complete}.
}
\tag{10.2}
$$


The determinant here is the complete evaluated mixed object. It is not the pole determinant of Section 3.

An irrationality proof would follow from


$$
B_\ell\ne0,\qquad \det H_{\rm complete}\ne0,
$$


and


$$
\boxed{
\log g_\ell-(m+1)\log\ell_{\rm clr}
-\log|\det H_{\rm complete}|
\longrightarrow+\infty
}
\tag{10.3}
$$


at the **same infinite original indices**. Indeed, (10.3) makes the nonzero whole error tend to zero, which is impossible if $e+\pi$ is rational.

No estimate proved in this report establishes (10.3).

---

## 11. Proof-status ledger and conclusion

| Statement | Status |
|---|---|
| Closed adjoining boundary and its producer-return consequence | Reused; not recalculated |
| Elementary boundaries in the full nonterminal strip | Audited and correct |
| Every corrected support layer in that enlarged strip | Independent audit still incomplete |
| Terminal-only support implies the separate first matrix-return cancellation | Rigorous conditional deduction |
| Complete raw radical pairing modulo $3^{30}$ | Reused at raw scope only |
| Actual pole/complete-core Schur congruence $S_{\mathcal P}-S_c\in3^hM$ | **New proved statement** |
| Preservation of actual terminal residues under that local replacement | **New proved statement** |
| One-lift prefix formula (5.5)–(5.7) | **New proved original-object statement** |
| Residual certificates with all inverse losses paid | **New proved statement** |
| Numerical value of the actual projection coefficient | **Not evaluated** |
| Terminal, endpoint and diagonal residues vanish | Not asserted |
| Nonsingular evaluated digit implies an actual directional bound | Conditional theorem |
| Growing relative-cofactor saving | Open |
| All-prime primitive denominator versus nonzero whole error | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

### Exact next bottleneck

The immediate analytic obligation is now the following finite, original-object problem:

> Evaluate the corrected beta-moment pairings
> 

$$
> -3^{-29}\mathcal P\!\left(
> \Psi_a-WE_{\mathcal P}^{-1}\mathcal P(W,\Psi_a),\,
> \Psi_c-WE_{\mathcal P}^{-1}\mathcal P(W,\Psi_c)
> \right)\pmod3
>
$$


> on the same infinite original subwindow, with the actual finite $W=[U\ Y]$, including $Y_m$.

The passage from this expression to the complete core and through the finite prefix is now proved and paid. Its residue is not evaluated by naming the pairing, by applying raw cancellations, or by replacing $W$ with another completion.

The bounded calculation in Section 9 can settle a genuinely new coefficient and its two relevant terminal observations at one specified original index. A uniform proof must then explain those outputs from the actual finite matrices, rather than extrapolate from them.

Beyond that fixed digit, the decisive unresolved issue remains an effective directional inverse or growing relative saving, followed by the all-prime comparison (10.3). Accordingly,


$$
\boxed{\text{No unconditional proof of rationality or irrationality of }e+\pi
\text{ is obtained.}}
$$


