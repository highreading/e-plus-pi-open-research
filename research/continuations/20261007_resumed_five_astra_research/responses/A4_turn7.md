> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Referee report on the depth-$26$ core, the new prime-$29$ digits, and paid contact projections

## Abstract and principal conclusions

The new work contains substantial valid local mathematics, but its three streams have different proof statuses.

1. **The depth-$26$ ternary core theorem is valid.** The stationary Gram argument, the nested precision-$20$ column approximations, the treatment of all digit orders, and the complete moment calculation—including the lower-pole cancellation—give
   

$$
S_c\equiv
   3^{26}\Bigl([y^{c-i-j}](y-1)^D\Bigr)_{0\le i,j<\nu}
   \pmod{3^{27}},
   \qquad
   c=\frac{H/3^{25}-1}{2}.
$$


   Its nonvanishing criterion, rank, radical, and infinite original subwindow are correct.

   **Identification of this operator with the actual residual remains conditional.** The recovered actual-block identity proves a precision-$7$ perturbation identity. It does not establish the stronger reset/coefficient hypotheses needed for
   $\Phi_R\in3^{21}M$. The distinction matters at exactly the proposed depth-$26$ actual digit.

2. **The new prime-$29$ content and whole-defect deductions are valid at their stated retained-source scope.** The leading ordinary-$000$ description gives $Y\in29^6$ when $c\ge3$, and hence an evaluated zero of the whole $29^{11}$-digit when $c\ge4$. The retained unbounded-content theorem supplies infinitely many original indices of this kind.

   The assertion $Le_i\in29^3$ through $i=231$ is not independently certified merely by saying that its enlarged shifts lie in a “retained guard.” I give a direct, weaker finite-boundary lemma that avoids this unresolved guard extension:
   

$$
Le_i\equiv0\pmod{29}\qquad(0\le i<435).
$$


   Together with the recovered all-row first-force formula, this **does close the actual normalized-tail feedback at the displayed digit, including the $c=2$ stratum**:
   

$$
V=L\bar w\in29\mathbb Z_{29}^{b+1}.
$$


   This conclusion includes the integral head coordinates of $\bar w$ and the physical terminal.

3. **The actual contact directions and paid contact identities are correct.** The raw cross-product factor is
   

$$
z\times W_j=-2((n+1)!)^2(R_jV)^T.
$$


   It must be combined with the least denominator and actual content used to form the primitive row. I make this accounting explicit below. The claimed large-prime support bound is valid, including the branch $p\nmid F$. It is not a subfactorial gcd estimate.

The new three-residue prime-$29$ row remains unevaluated. None of the accepted local results establishes the required all-prime bound for an actual primitive denominator, or compares it successfully with the nonzero whole error on the same infinite original indices. The rationality or irrationality of $e+\pi$ remains unresolved.

---

# 1. Scope of this review

The already closed binary assembled exterior calculation and universal endpoint-gauge decision are not reopened. Neither are the old prime-$29$ zero-row calculation, the archived first-force formula, or the previously proved exact exterior factorial filtration.

The following distinctions are maintained throughout:

- a symbolic proof on the original family;
- a deduction using an expressly retained theorem;
- a finite certificate with only finite scope;
- a conditional implication whose original-object hypothesis is still unverified;
- an open arithmetic obligation.

In particular, the scaled ternary moment certificate covers exactly its $68$ reported monomials at smaller pole parameters. Its inclusion of every retained denominator is useful auxiliary evidence, but it is not the proof of the original depth-$26$ theorem.

---

# 2. The ternary depth-$26$ theorem

## 2.1 Original domain and finite boundaries

Retain exactly


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




$$
m=2^{2j-1},\qquad n=4^j+1,\qquad A=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$


and


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$



For sufficiently large retained tuples,


$$
v_3(D)=5,\qquad D\equiv0\pmod2,\qquad D\ge486.
$$



Put $x=y-1$, and retain


$$
U_u=x^u\quad(0\le u<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m),
$$


where


$$
\nu=D/2-1,\qquad d=3D/2-1.
$$


The HIGH interval is the finite interval $[d,m]$; its physical terminal is $Y_m$.

The complete functional is


$$
\mathcal M(P)=
-\frac{3^h}{4}\mathfrak f(P)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](P-P(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^s)=(2s)!.
$$


Its denominator cutoff is


$$
2v+1\le4n-3=4H-4D+5.
$$



The form and complete corrected columns are


$$
G_c(f,g)=\mathcal M(Q_cfg),\qquad
Q_c=(y+1)x^A(\beta+3y),\quad \beta=-71-A,
$$




$$
F=Z-WE_c^{-1}C_c,\qquad W=[U\ Y].
$$



The accepted precision-$20$ theorem supplies:

- an integral unimodular basis $[W,F]$;
- $G_c(W,F)=0$;
- $E_c^{-1}\in3^{-1}M(\mathbb Z_3)$;
- $S_c=G_c(F,F)\in3^{21}M$;
- the nested support statement for every $1\le p\le20$;
- $B\in3^{20}M$ in the normalized LOW/HIGH block system.

These are precisely the previously established results needed here. No improvement of the old five-operation safety margin is required.

---

## 2.2 The stationary Gram lemma is correct

Suppose


$$
F^*=F+3^p\Delta
$$


with integral columns of degree at most $m$. Because $[W,F]$ is integral unimodular, write


$$
\Delta=WC+FD
$$


with integral matrices $C,D$. Orthogonality gives


$$
G_c(F,\Delta)=S_cD.
$$


Thus


$$
G_c(F^*,F^*)-S_c
=
3^p(S_cD+D^TS_c)+3^{2p}G_c(\Delta,\Delta).
$$



The functional is integral on the relevant integral inputs: at the retained cutoff every denominator has $3$-valuation at most $h$, and $4$ is a $3$-adic unit. Consequently,


$$
G_c(F^*,F^*)-S_c
\in3^{\min(p+s,2p)}M
$$


when $S_c\in3^sM$.

For $p=20,s=21$,


$$
\boxed{S_c\equiv G_c(F^*,F^*)\pmod{3^{40}}.}
$$



This is a finite-space statement. It uses neither an infinite HIGH inverse nor an unpaid additional LOW inversion.

---

## 2.3 Nested support and the first two digits

The accepted support theorem has the necessary scope:


$$
F_i\equiv x^D\psi_{i,p}\pmod{3^p},\qquad
\operatorname{supp}\psi_{i,p}
\subseteq I_{\Omega_{20}}(pD/2),
\quad 1\le p\le20,
$$


where


$$
\Omega_{20}=H/3^{19},\qquad \deg\psi_{i,p}\le m-D.
$$



It is not merely a statement at $p=20$. Since multiplication by the monic polynomial $x^D$ is injective over
$(\mathbb Z/3^p\mathbb Z)[y]$, the quotients agree at common precision. Nested support then permits


$$
F_i^*=x^D\sum_{a=0}^{19}3^a\phi_{i,a},
$$


with


$$
\deg\phi_{i,a}\le m-D,\qquad
\operatorname{supp}\phi_{i,a}
\subseteq I_{\Omega_{20}}\bigl((a+1)D/2\bigr).
$$



The first two digits require the actual terminal calculation.

For $i<\nu$ and $d\le b\le m$,


$$
i+b\le\nu-1+m=\frac{H-1}{2}-1.
$$


Hence the top $\beta x^H$ extraction is absent. The extra $3y$ reaches the top extraction only for


$$
(i,b)=(\nu-1,m).
$$


At the next pole, $x^H\equiv y^H-1\pmod3$ makes the normalized extraction vanish. All further lower poles, and the factorial term, have an additional factor $3$. Therefore


$$
V^T\equiv e_{Y_m}e_{\nu-1}^T\pmod3.
$$



Write


$$
y^d=r_d+x^Dq_d,\qquad \deg r_d<D,
$$




$$
q_d(y)=\sum_{a=0}^{\nu}\binom{D+a-1}{a}y^{\nu-a}.
$$


The retained finite identities are


$$
Re_{Y_m}=e_{Y_d},\qquad L^{-1}Xe_{Y_d}\equiv r_d\pmod3.
$$


Solving the LOW/HIGH system, with $B\in3^{20}M$, gives


$$
\boxed{
F_i\equiv x^D\bigl(y^i-3\delta_{i,\nu-1}q_d\bigr)\pmod9.
}
$$



Thus one may take


$$
\phi_{i,0}=y^i,\qquad
\phi_{i,1}=-\delta_{i,\nu-1}q_d.
$$


The support of these exact lifts is within the required nested sets. In particular, no HIGH coordinate beyond $m$ has been introduced.

---

## 2.4 Every total digit order is accounted for

For a product of digits of total order $s=a+b$, the explicit scalar is $3^s$. For $2\le s\le26$, set


$$
q=27-s.
$$


After removing $y+1$, the polynomial has the form


$$
x^H\,x^D(\beta+3y)\phi_{i,a}\phi_{j,b}.
$$


Its local width is at most


$$
w_s=(2+s/2)D+1.
$$



The common coefficient grid is


$$
\Lambda_q=\frac{H}{3^{\max(19,q-1)}}.
$$


Every pole that can contribute modulo $3^q$, including the top pole, lies on an odd half-grid relative to $\Lambda_q$.

The restrictive case is $s=2,q=25$:


$$
\frac{H/3^{24}}D>\frac{147968}{19683}>\frac{15}{2},
$$


so


$$
3D+1<\frac{H/3^{24}-1}{2}.
$$


For $3\le s\le7$, the grid spacing increases geometrically while the width increases only linearly. For $7\le s\le26$, the common grid is $\Omega_{20}$, and


$$
w_s\le15D+1<(\Omega_{20}-1)/2.
$$



Terms with $s\ge27$ vanish by integrality alone. The factorial part vanishes at the required precision because $h\ge27$. Thus


$$
\boxed{\text{Every term of total digit order at least \(2\) is zero modulo \(3^{27}\).}}
$$



This argument includes every retained lower pole. It is not a top-pole calculation.

---

## 2.5 Complete low-degree moment extraction

Put


$$
\Omega=H/3^{25},\qquad c=(\Omega-1)/2.
$$


For every integral $P$ with $\deg P\le2D$, the claimed formula is


$$
\boxed{
\mathcal M((y+1)x^HP)
\equiv3^{26}[y^c]P\pmod{3^{27}}.
}
$$



Here is the complete extraction.

The window gives


$$
\Omega/D>\frac{147968}{59049}>\frac52,
$$


so $\deg P<\Omega$. The top pole is absent by degree, and the factorial term is zero modulo $3^{27}$.

Every lower denominator is uniquely


$$
\alpha H/3^t,\qquad \alpha>0\ \text{odd},\quad 3\nmid\alpha,
$$


with weight $3^{t+1}\alpha^{-1}$. Only $0\le t\le25$ matters.

### Interior layers $1\le t\le24$

The required precision of $x^H$ is $3^{26-t}$, so its support lies on


$$
H/3^{25-t}.
$$


Combining this with the pole grid gives spacing at least $H/3^{24}=3\Omega$. Its half-spacing exceeds $2D$. Every extraction is zero.

### Layer $t=0$

The only denominator at this layer is $H$, at $r_1=(H-1)/2$, with weight $3$.

Because $\deg P<\Omega$, only $[y^c]P$ can contribute. The corresponding index in $x^H$ is


$$
L\Omega,\qquad L=(3^{25}-1)/2,\qquad L\equiv1\pmod3.
$$


Using


$$
\binom Hk=\frac Hk\binom{H-1}{k-1},
\qquad
\binom{H-1}{k-1}\equiv(-1)^{k-1}\pmod3,
$$


and the sign of $(y-1)^H$, one obtains


$$
\frac{[y^{L\Omega}]x^H}{3^{25}}\equiv L^{-1}\equiv1\pmod3.
$$


This contributes $3^{26}[y^c]P$.

### Layer $t=25$

Only $x^H\equiv y^H-1\pmod3$ is needed. The only possible extractions occur at $c$ and $H+c$, corresponding to denominators


$$
\Omega,\qquad 2H+\Omega.
$$


Both lie inside the actual cutoff. Their normalized units are


$$
1,\qquad 2\cdot3^{25}+1,
$$


which agree modulo $3$. The coefficients from $-1$ and $y^H$ have opposite signs, so these two contributions cancel.

This proves the complete moment formula. The lower-pole cancellation is essential.

---

## 2.6 The explicit operator, nonvanishing, rank, and radical

For total digit order zero,


$$
P=x^D(\beta+3y)y^{i+j}
$$


has degree at most $2D$. Since $\beta\equiv1\pmod3$,


$$
G_c(z_i,z_j)
\equiv3^{26}[y^{c-i-j}]x^D\pmod{3^{27}}.
$$


The total-order-one terms have an extra factor $3$, so the same moment lemma kills them modulo $3^{27}$.

The stationary approximation therefore proves


$$
\boxed{
S_c\equiv3^{26}H_c\pmod{3^{27}},
\qquad
(H_c)_{ij}=[y^{c-i-j}](y-1)^D.
}
$$


Equivalently,


$$
\boxed{K_{26}=-H_c,\qquad K_{21}=\cdots=K_{25}=0.}
$$



Since $i+j\le D-4$,


$$
K_{26}=0\quad\text{if }c>2D-4.
$$


Conversely, when $c\le2D-4$, the original lower window ensures $c>D$ for sufficiently large tuples. Taking $i+j=c-D$ gives coefficient $1$ of $y^D$ in $x^D$. Thus


$$
\boxed{K_{26}\ne0\iff c\le2D-4.}
$$



On


$$
3<\Omega/D<7/2,
$$


define


$$
t=c-\frac{3D}{2}+2,\qquad r=2D-3-c.
$$


The first $t$ rows and columns are zero. On the remaining coordinates, reversal of one order yields a triangular matrix with diagonal $-1$. Hence


$$
\boxed{
\operatorname{rank}K_{26}=r,\qquad
\operatorname{rad}K_{26}
=\operatorname{span}_{\mathbb F_3}\{e_0,\ldots,e_{t-1}\}.
}
$$



These are exact rank and radical statements, not merely a nonzero-minor certificate.

---

## 2.7 The infinite subwindow is an original subfamily

Let $\alpha=\log_3 4$. It is irrational. Therefore the progression


$$
j=84645+531441k
$$


has dense fractional parts $j\alpha\bmod1$, with infinitely many visits to every nonempty open interval.

For $N=\lceil j\alpha\rceil$, take $H=3^N$, so $h=N+1$. Then


$$
D/H=1-3^{j\alpha-N}+3^{-N}.
$$


The desired subwindow is


$$
\frac{2}{7\cdot3^{25}}<D/H<\frac1{3\cdot3^{25}}.
$$


It lies strictly within the original window, since


$$
\frac{147968}{59049}<3,
\qquad
2\frac{147968}{59049}>\frac72.
$$


Choosing a smaller closed interval inside it absorbs the term $3^{-N}$.

Thus infinitely many unchanged original indices satisfy the rank subwindow. This conclusion does not use the finite scaled moment certificate.

---

# 3. Actual ternary transport: the remaining premise is real

## 3.1 What the recovered identity proves

The recovered source gives


$$
Q_{\rm act}=Q_c+3^6R_{\rm prod},
\qquad R_{\rm prod}=3\mathscr R,
$$


and therefore


$$
E_{\rm act}=E_c+3^7J,
\qquad
J=\bigl(\mathcal M(\mathscr R\,ww')\bigr).
$$



This is an exact complete-form identity. It includes both parts of $\mathcal M$, the endpoint subtraction, and the original finite cutoff.

It does **not** prove the stronger reset assertion


$$
\deg\mathscr R\le A+1,
$$


the omitted exact coefficient formula, or the endpoint factorization needed to derive


$$
\mathscr R\equiv(y+1)x^{A-48}q_{20}(x)\pmod{3^{20}},
\qquad \deg q_{20}\le48.
$$



A4 turn2 proves an implication from those hypotheses. The present recovery receipt does not verify those hypotheses for the actual recovered producer. Referring back to that conditional implication is not an independent verification.

---

## 3.2 The exact effect of the missing extra digit

Retain the paid-chain conclusion at its established scope:


$$
\mathcal Q\in3^{21}M.
$$


The Schur identity is


$$
S_{\rm act}=S_c+3^6\Phi_R-3^{13}\mathcal Q.
$$



If only the weaker linear bound


$$
\Phi_R\in3^{20}M
$$


is available, then $S_{\rm act}\in3^{26}M$, but


$$
\boxed{
-\frac{S_{\rm act}}{3^{26}}
\equiv
K_{26}-\frac{\Phi_R}{3^{20}}
\pmod3.
}
$$


The unknown term is at exactly the same digit as the proposed actual Hankel operator.

Thus the stronger premise is not cosmetic. To identify the actual depth-$26$ operator, one must prove


$$
\Phi_R/3^{20}\equiv0\pmod3
$$


for the actual recovered producer. The reset/coefficient/endpoint theorem is one sufficient route; a direct proof of this observation would also suffice.

No coefficient computation on the core alone supplies it.

---

## 3.3 Endpoint transport is less demanding

The endpoint congruence does not require the stronger linear bound.

From the exact perturbation identity and $E_c^{-1}\in3^{-1}M$, a Neumann argument gives


$$
E_{\rm act}^{-1}\in3^{-1}M.
$$


The exact correction has the form


$$
F_{\rm act}=F-3^7WE_{\rm act}^{-1}T.
$$


Integrality of $T$ already makes the difference divisible by $3$; the stronger retained $T\in3M$ is more than enough. Therefore


$$
e_{\rm act}\equiv F(-1)^T\pmod3.
$$


Since $F_i\equiv x^Dy^i\pmod3$,


$$
\boxed{(\bar e_{\rm act})_i=(-1)^i.}
$$



It is nonzero on the **proved core radical**. It is nonzero on the actual radical identified in A1 only after actual Hankel transport has been justified.

The complete diagonal


$$
d_{\rm act}=w^TE_{\rm act}^{-1}w\in3^{-1}\mathbb Z_3
$$


must remain in the bordered observation.

---

## 3.4 A sharper concrete next lemma

Assume the actual depth-$26$ identification has been proved. Order the coordinates as the nondegenerate complement followed by the radical:


$$
U=-S_{\rm act}/3^{26}
=
\begin{pmatrix}A&B\\B^T&C\end{pmatrix}.
$$


Then


$$
A\in\operatorname{GL}_r(\mathbb Z_3),\qquad B\in3M,\qquad C\in3M.
$$


Consequently


$$
R=C-B^TA^{-1}B
$$


satisfies the useful simplification


$$
\boxed{
R/3\equiv C/3\pmod3.
}
$$


Also


$$
f=e_R-B^TA^{-1}e_C\equiv e_R\pmod3.
$$



Thus the first radical digit does not require a new large inverse calculation:


$$
\boxed{
(R/3)_{ij}
\equiv-\frac{(S_{\rm act})_{ij}}{3^{27}}\pmod3,
\qquad 0\le i,j<t.
}
$$



At this next digit the producer returns:


$$
-\frac{(S_{\rm act})_{ij}}{3^{27}}
\equiv
-\frac{(S_c)_{ij}}{3^{27}}
-\frac{(\Phi_R)_{ij}}{3^{21}}
\pmod3.
$$


The quadratic term is too deep to matter under the retained chain bound. Therefore even a proof of $\Phi_R\in3^{21}M$ does not evaluate the next radical digit.

The complete bordered diagonal after complement elimination remains


$$
3^{26}d_{\rm act}-e_C^TA^{-1}e_C.
$$


If an inverse of $R=3V$ is later used, its factor $3^{-1}$ is a new paid division.

---

# 4. The new prime-$29$ statements

## 4.1 Original objects

Retain


$$
p=29,\qquad D=p^3=24389,
$$




$$
b=3^{249005515+574312172u},\qquad n=2001b,
$$




$$
u\ge0,\qquad u\equiv2\pmod{p^9}.
$$



The domains remain:

- contact coordinates $0\le j<b$;
- recurrence source rows $1\le i\le b-2$;
- reconstructed coordinates $0\le j\le b$.

Write


$$
W_j=\binom{n+2}{j},\qquad
(\mathcal Rx)_j=W_j(jx_{j-1}-x_j),
\quad x_{-1}=x_b=0,
$$




$$
L=\mathcal RA^{-1}.
$$


The complete columns are


$$
Z_w=Lf^0,\qquad
Y=L\mathbf r+W_be_b,
\qquad
\mathbf r=A_{IE}z+h^F/b!.
$$



Both exponential charges, factorial subtraction, logarithmic forcing from $F/(1-z)$, both finite returns, and the separate physical terminal remain in these objects.

The original split is


$$
b=DB+5044,\qquad n+2=DW+20389,\qquad 2n-1=DA+16384,
$$


with


$$
0\le J\le B\quad(\ell<5044),\qquad
0\le J\le B-1\quad(\ell\ge5044).
$$



---

## 4.2 Leading ordinary-$000$ response

The proof of


$$
Y_{\ell+DJ}/p^5
\equiv(-1)^{b-\ell-J}\beta_\ell K(J)\pmod p
$$


is a valid consequence of the retained branch inequalities and complete coefficient-order-two expansion.

After removing the common upper $p^3$, a leading contribution has total low order $2$.

- The two unit return atoms already have order at least $2$. Any outgoing addition carry or weight borrow raises the order.
- Positive-symbol order-one atoms have at least one further low order. Again, a nonordinary outgoing interface raises the total order.
- An order-two coefficient can contribute only with no low event. In the retained sparse-interface geometry, this forces $000$.

The newly retained exterior indices through $30$ and symbols through $58$ give maximal lower displacement $60$, hence support


$$
0\le\ell\le5104.
$$



This is a source-to-response deduction, not a consequence of the old zero-row certificate.

---

## 4.3 The seven-row source units can be checked

At $\ell=tp^2$, $0\le t\le6$, the newly visible reconstructed row factor is


$$
j/p^2=t+pJ.
$$


Its $pJ$ coefficient is


$$
d_t^{\rm rec}
=\binom{24}{t}\binom{25-t}{6-t}\pmod{29}.
$$



The relevant low digits are


$$
n+2:(2,7,24),\qquad 2n-1:(28,13,19),\qquad
b:(27,28,5).
$$


For the zero-event reconstructed branch with lower shift $b+2$, stripping the three low levels gives exactly the displayed binomial product.

For $t<6$, the unit first-source branch gives


$$
a_{tp^2}=-2(6-t)d_t^{\rm rec}.
$$


For example, the low factorial ratio responsible for $-2$ contains


$$
\frac1{14}\equiv-2\pmod{29}.
$$



The two unit second-return branches give


$$
-\frac32(6-t)d_t^{\rm rec}.
$$


The reconstructed $j$-branch adds $t\,d_t^{\rm rec}$, and the already paid exterior value $v_2/p^2=-6$ adds $-6d_t^{\rm rec}$. Their sum is


$$
\beta_{tp^2}
=-\frac52(6-t)d_t^{\rm rec}.
$$



The other branches do not enter these leading rows:

- short positive row degrees encounter the two zero low digits of $tp^2$;
- the degree-$29$ possibility still has a low event;
- coefficient-order-two branches with a constant row factor have a low event except for the retained $h=2$ exterior term;
- the remaining exterior terms $h\ge3$ acquire a first-digit carry.

Thus the seven-row units are not merely numerical guesses. They give


$$
d^{\rm rec}=(26,21,5,11,26,3,7),
$$




$$
a=(7,22,18,21,12,23,0),
$$




$$
\beta=(16,13,8,19,15,7,0).
$$



The arithmetic correction is therefore


$$
\sum_{t=0}^6a_{tp^2}d_t^{\rm rec}\equiv12\pmod{29},
$$


and


$$
\boxed{\Delta\mathcal L=6\cdot12=14\pmod{29}.}
$$



This checks the source units needed for the correction. It does not evaluate the completed low row.

At $\ell=0$, the three stripped units are indeed


$$
L_0=9,\qquad L_1=18,\qquad L_2=26,
$$


so


$$
\beta_0=9+18-6\cdot26=16\pmod{29}.
$$


In particular,


$$
6\beta_0-2a_0=24\ne0\pmod{29}.
$$



---

## 4.4 Content classification and the whole $p^{11}$-digit

The exact normalization is


$$
\bar f=f^0/C_n,\qquad
\bar Z=Z_*+p^2U+p^7V,
$$


with $C_n$ a $p$-adic unit and


$$
\bar Z-Z_*\in p^5.
$$


At $\ell=0$,


$$
Z_{*,DJ}/p^4\equiv(-1)^{b-J}7K(J)\pmod p.
$$


This original row contains every $0\le J\le B$.

Therefore


$$
c\ge3
\iff Z_*\in p^5
\iff K(J)\equiv0\pmod p\quad(0\le J\le B).
$$


The complete leading first profile and the physical terminal are required for the reverse implication.

The ordinary-$000$ theorem then gives


$$
\boxed{c\ge3\Longrightarrow Y\in p^6\mathbb Z_p^{b+1}.}
$$



For


$$
\mathcal Q=6Y/p^5-2Z_*/p^4,
$$


the row $\ell=0$ has unit coefficient $24$, so


$$
\boxed{\mathcal Q\equiv0\pmod p\iff c\ge3.}
$$



The whole defect is


$$
\Delta(\bar f)=6\bar Z^TY-p\bar Z^T\bar Z.
$$


When $c\ge4$,


$$
6\bar Z^TY\in p^{c+8}\subseteq p^{12},
$$




$$
p\bar Z^T\bar Z\in p^{2c+5}\subseteq p^{12}.
$$


Hence


$$
\boxed{
\Delta(\bar f)\equiv\Delta(f_*)\equiv0\pmod{p^{12}}
\qquad(c\ge4).
}
$$



This is an evaluated whole-defect zero. Under the retained theorem that $c$ is unbounded in every original progression, it holds on an increasing infinite sequence of unchanged original indices.

---

# 5. Actual-tail feedback: a new direct finite-boundary proof

## 5.1 The advertised $p^3$ guard extension is not established by a range assertion alone

A2 states


$$
Le_i\in p^3\qquad(0\le i\le231)
$$


and gives enlarged shift bounds


$$
\alpha\le290,\qquad -232\le v\le58.
$$



These shifts preserve the elementary sparse-interface geometry. Indeed, with


$$
a_0=16384+\alpha,\qquad b_0=5044+v,
$$


the enclosing box gives


$$
4812\le b_0\le5102,
$$




$$
21196\le a_0+b_0\le21776,
$$


and therefore


$$
0<b_0<20389<a_0+b_0<24389.
$$



This verifies the geometric inequalities. It does not, by itself, prove that every newly required complete source and return is covered by the previously proved three-event guard. The packet does not display the enlarged guard theorem with this complete scope.

Fortunately, the claimed $p^3$ strength is unnecessary for the displayed actual-tail feedback. A direct modulo-$p$ argument suffices.

---

## 5.2 A finite short-source annihilation lemma

### Lemma

For the actual original family,


$$
\boxed{Le_i\equiv0\pmod{29}\qquad(0\le i<435).}
$$



### Proof

Use the retained complete finite inverse modulo $p$:


$$
A^{-1}\equiv R_{2n,II}\mathsf P_-\pmod p,
$$


where


$$
(R_{2n})_{kl}=\binom{-2n}{l-k},\qquad
(\mathsf P_-)_{li}=(-1)^{l-i}\binom li.
$$


Both indices remain in $0,\ldots,b-1$.

Write


$$
x=A^{-1}e_i.
$$


Since $p\mid2n$,


$$
(1+z)^{-2n}\equiv(1+z^p)^{-2n/p}\pmod p.
$$


Thus the upper convolution only uses $l-k$ divisible by $p$.

Write


$$
i=i_0+pi_1,\qquad 0\le i_0<p,\quad 0\le i_1\le14,
$$


and


$$
k=k_0+pk',\qquad 0\le k_0<p.
$$


For $k_0\le26$, put


$$
b'=(b-27)/p,\qquad M=b'-k',\qquad a=2n/p.
$$


The actual upper endpoint $b-1$ gives exactly this value of $M$. Lucas reduction yields


$$
x_k\equiv
(-1)^{k-i}\binom{k_0}{i_0}
\sum_{q=0}^{M}
\binom{a+q-1}{q}\binom{k'+q}{i_1}
\pmod p.
$$



Vandermonde followed by finite hockey-stick summation gives


$$
\sum_{q=0}^{M}
\binom{a+q-1}{q}\binom{k'+q}{i_1}
=
\sum_{r=0}^{i_1}
\binom{k'}{i_1-r}
\binom{a+r-1}{r}
\binom{a+M}{M-r}.
$$



The original digits give


$$
a\equiv14\pmod p,\qquad b'\equiv28\pmod p.
$$


If $k'\bmod p=s\le7$, then


$$
M\bmod p=28-s,
$$


and, for $r\le14$, no subtraction borrow occurs in $M-r$. Hence


$$
(a+M)\bmod p=13-s,
$$




$$
(M-r)\bmod p=28-s-r>13-s.
$$


Lucas's theorem makes every last binomial zero modulo $p$. Therefore


$$
x_k=0\pmod p
$$


whenever $k_0\le26$ and $k'\bmod p\le7$.

Now consider a contact coordinate $j<b$. If $W_j\not\equiv0\pmod p$, the first two digits of $n+2$ force


$$
j_0\le2,\qquad j_1\le7.
$$


Thus $x_j=0$. If $j_0=1$ or $2$, then $x_{j-1}=0$ as well. If $j_0=0$, the factor $j$ itself is zero modulo $p$. Consequently


$$
W_j(jx_{j-1}-x_j)=0\pmod p.
$$


Coordinates with $W_j=0$ are already zero.

Finally, the physical terminal is


$$
(Le_i)_b=bW_bx_{b-1},
$$


which vanishes modulo $p$ by the retained $v_p(W_b)\ge6$. This proves the lemma on the full reconstructed domain. ∎

This proof does not assume the unverified $p^3$ guard extension. It also does not enlarge the finite interval or replace its upper endpoint.

---

## 5.3 The recovered source now closes the actual tail

The archived exact first-force formula is


$$
f_i^0=\frac{(n+i)!}{n!}J_i
=i!\binom{n+i}{i}J_i,
\qquad J_i\in\mathbb Z.
$$


Thus the previously proposed $\mathbf H_8$ is already proved:


$$
f_i^0\in p^8\mathbb Z_p\qquad(i\ge232).
$$



In the actual decomposition


$$
\bar f=f_*+p^2\bar v+p^7\bar w,
$$


the head coordinates of $\bar w$ are integral, and for $i>202$,


$$
\bar w_i=f_i^0/(p^7C_n).
$$


Therefore


$$
\bar w_i\in p\mathbb Z_p\qquad(i\ge232).
$$



Split the actual finite source:


$$
\bar w=\sum_{i=0}^{231}\bar w_i e_i+p\,w_{\rm tail},
$$


with $w_{\rm tail}$ integral. The lemma and $p$-integrality of the physical finite map $L$ give


$$
\boxed{
V=L\bar w\in p\mathbb Z_p^{b+1}.
}
$$



This includes all head coordinates $0,\ldots,231$; they have not been discarded. It includes the physical terminal. Hence


$$
\boxed{V^T\mathcal Q=0\pmod p}
$$


on the entire original family, including $c=2$.

The updated next-digit identity is therefore


$$
\frac{\Delta(\bar f)-\Delta(f_*)}{p^{12}}
\equiv
6\,\frac{U^TY}{p^{10}}
-2\,\frac{Z_*^TU}{p^9}
\pmod p.
$$


The two remaining paid $U$-pairings have not been evaluated here.

This closes a genuine local obligation. It does not establish growing-depth tail deletion.

---

# 6. The physical terminal and the unevaluated new low row

## 6.1 Terminal units

The recovered first-force formula also validates the first flat source modulo $p$. For $i<p$, Frobenius gives


$$
J_i\equiv C_n\pmod p,
$$


because $n$ is divisible by $p$ and $(1+t)^i$ has degree $<p$. Hence


$$
\bar f_i\equiv i!\pmod p\quad(i<p),
\qquad
\bar f_i\equiv0\pmod p\quad(i\ge p).
$$


The decomposition then gives the same residues for $f_*$.

The last row of the finite inverse yields


$$
\chi_{b-1}\equiv
\sum_{i=0}^{26}(-1)^i(26)_{\underline i}
\equiv22\pmod{29}.
$$


The short recurrence


$$
d_0=1,\qquad d_m=1-md_{m-1}
$$


checks the final residue $d_{26}=22$.

For the complete second solution, the logarithmic force is paid at this fixed precision. Exact exterior filtration leaves only $v_0=1,v_1=-1$ modulo $p$. In the retained finite return, their last-row displacements are $1$ and $2$; the corresponding negative binomials are divisible by $p$. Therefore


$$
\psi_{b-1}\equiv0\pmod p.
$$



Thus


$$
Z_{*,b}=bW_b\chi_{b-1},\qquad
Y_b=W_b(b\psi_{b-1}+1)
$$


has the claimed units. The separate $+1$ is indispensable.

The low weight unit is


$$
\frac{2!}{27!\,4!}
\frac{7!}{28!\,7!}
\frac{24!}{5!\,18!}
\equiv11\pmod{29}.
$$


Since the two low borrows contribute $p^2$,


$$
W_b/p^6\equiv11k_B\pmod p.
$$


Consequently


$$
\frac{6Z_{*,b}Y_b}{p^{12}}
\equiv6\cdot27\cdot22\cdot11^2\,k_B^2
=14k_B^2\pmod p.
$$


The norm terminal $pZ_{*,b}^2$ is in $p^{13}$.

Therefore


$$
\boxed{\text{The physical terminal contribution at this next flat digit is }14k_B^2.}
$$



This is a terminal contribution, not an evaluation of the whole next digit.

---

## 6.2 The completed three-residue row is still open

The proposed whole $p^{11}$-digit observation is


$$
\delta_{11}
=\mathcal A S-\mathcal D k_B^2+\mathcal L T\pmod p,
$$


with the actual split at $5044$.

The new profiles belong to $Y/p^5$, not to the previously certified $Y/p^4$ calculation. The correction


$$
\Delta\mathcal L=14
$$


shows concretely why the old row cannot simply be reused.

No value for


$$
(\mathcal A,\mathcal D,\mathcal L)
$$


is supplied by the attached certificates. In particular:

- the old five-entry zero row does not evaluate it;
- a nonzero individual row does not prove its completed sum is nonzero;
- the evaluated zero on $c\ge4$ does not evaluate it uniformly on $c=2,3$;
- the new actual-tail result does not evaluate the flat defect.

If the new row is nonzero, the required upper observation remains an invariant of the actual original upper word $B$, not of an arbitrary continuation.

Growing precision also remains mandatory:


$$
K=c+4+\nu,
$$


with the complete symbol range, finite exterior solve, finite returns, physical terminal, and logarithmic head retained at that $K$. The fixed-depth tail result above does not authorize their deletion.

---

# 7. Actual paid contact projections

## 7.1 The directions and raw scale

Retain the actual finite matrix


$$
T=
\begin{pmatrix}
c&b&a\\
d&c&b\\
e_*&d&c
\end{pmatrix},
\qquad
R_j=\ell_j\operatorname{adj}(T),
$$




$$
\ell_0=(-1,n,-nm),\qquad \ell_3=(0,0,1).
$$



No new index family is introduced: these statements concern the original geometric-family indices at which the retained finite-producer nonvanishing theorem gives $\det T\ne0$.

With


$$
V=
\begin{pmatrix}
2N&0&0\\
N&N&0\\
m&t&1
\end{pmatrix},
\qquad \det V=2N^2,
$$


the source gives


$$
Vz=2N(n+1)!\,k,
$$




$$
W_j=2N(n+1)!\,V^{-1}k_j,
$$


where


$$
k=T_1+nT_0,\qquad k_3=T_0,\qquad k_0=T_2-nmT_0.
$$



The evaluated directions


$$
W_3=
\begin{pmatrix}
X\\ Z\\ Y-X-(2n+1)Z
\end{pmatrix}
$$


and


$$
W_0=
\begin{pmatrix}
mZ-(n^2+1)X-(n-1)Y\\
mY+(1-n)X-m^2Z\\
2m(mX+(n^2+n+1)Z-NY)
\end{pmatrix}
$$


are consistent with the finite kernel equations and the supplied symbolic receipt.

The raw scale can also be derived directly. For any invertible $V$,


$$
(V^{-1}u)\times(V^{-1}v)
=(\det V)^{-1}V^T(u\times v).
$$


Moreover,


$$
k\times k_j=-R_j^T
$$


for both $j=0,3$, by the cofactor formulas for the columns of $T$. Therefore


$$
\boxed{
z\times W_j=-2((n+1)!)^2(R_jV)^T.
}
$$



This is a raw-contact identity. It is not yet the primitive-contact identity.

---

## 7.2 Least row denominators and actual contents

Let $d_j^{\rm row}$ be the least positive integer clearing the three coordinates of $R_j$, and let


$$
\gamma_j=\gcd\bigl(\text{coordinates of }d_j^{\rm row}R_j\bigr)>0.
$$


With the recorded sign convention $\sigma_j$,


$$
r_j=\sigma_j\frac{d_j^{\rm row}}{\gamma_j}R_j.
$$



Put


$$
\mathbf c_j=r_jV,\qquad
A_j=z\times W_j,
$$




$$
h_j=\gcd(|A_{j,1}|,|A_{j,2}|,|A_{j,3}|),
\qquad
\kappa_j=\gcd(|c_{j,1}|,|c_{j,2}|,|c_{j,3}|).
$$


The raw scale gives the exact content ledger


$$
\boxed{
d_j^{\rm row}h_j
=
2((n+1)!)^2\gamma_j\kappa_j.
}
$$


In particular,


$$
\mathbf c_j
=\varepsilon_j\kappa_j A_j^T/h_j
$$


with the appropriate actual sign $\varepsilon_j$.

This explicitly retains both paid operations:

1. clearing the rational raw row by its least denominator;
2. dividing by the actual content of that integer row.

Neither operation can be replaced by the raw adjugate.

Because $r_j$ is primitive and


$$
\mathbf c_j\operatorname{adj}(V)=2N^2r_j,
$$


one obtains


$$
\boxed{\kappa_j\mid2N^2.}
$$



The other contents and clearers in the construction remain distinct: the least eight-entry clearer, later two-entry reconstruction contents, and final weight gcds are not $\gamma_j$, $h_j$, or $\kappa_j$.

---

## 7.3 The paid Bézout identity

Writing $z=(P,Q,F)^T$, the cross product gives


$$
h_j\widehat R_j
=
\varepsilon_j\kappa_j
\left[
W_{j,3}M+
F(W_{j,1}\widehat\ell-W_{j,2}\widehat h)
\right].
$$



Retain


$$
C=mZ,\qquad
g_{\rm aff}=\gcd(|F|,|CM|),
$$




$$
\Theta=CM+F\bigl(2L_n(n!)^2-\mathscr K_n^\circ\bigr),
\qquad
T_{\rm aff}=\Theta/g_{\rm aff}.
$$


The division is paid because $g_{\rm aff}$ divides both displayed summands.

Define


$$
\widehat{\mathcal B}_j
=
W_{j,3}\bigl(2L_n(n!)^2-\mathscr K_n^\circ\bigr)
-C(W_{j,1}\widehat\ell-W_{j,2}\widehat h).
$$


Then cancellation of the $CMW_{j,3}$ terms proves


$$
\boxed{
\varepsilon_j\kappa_jW_{j,3}g_{\rm aff}T_{\rm aff}
-Ch_j\widehat R_j
=
\varepsilon_j\kappa_jF\widehat{\mathcal B}_j.
}
$$



The complete factorial term $2L_n(n!)^2$ is retained. This identity is valid for the actual paid contacts, not merely for an arbitrary syzygy.

---

## 7.4 Large-prime support, and a modest all-prime extension

Let


$$
D_j=\frac{|\widehat R_j|}
{\gcd(|\widehat R_j|,|F|)}
$$


whenever the original paid reference denominator is defined.

For $p>N$, $\kappa_j$ is a unit. The valuation proof in A3 is correct and yields


$$
\gcd(|T_{\rm aff}|,D_j)_{>N}
\mid
\gcd\left(D_j,\left|\frac F{g_{\rm aff}}\widehat{\mathcal B}_j\right|\right)_{>N}.
$$


The branch $p\nmid F$ remains present. If also $p\nmid W_{j,3}$, the sharper truncated-valuation equality follows by reducing the paid identity modulo $p^{v_p(\widehat R_j)}$.

There is also an elementary all-prime version, with the actual contact content retained:


$$
\boxed{
\gcd(|T_{\rm aff}|,D_j)
\mid
\gcd\left(
D_j,\,
\kappa_j\left|\frac F{g_{\rm aff}}\widehat{\mathcal B}_j\right|
\right).
}
$$



Indeed, at any prime write


$$
f=v_p(F),\quad g=v_p(g_{\rm aff}),\quad
r=v_p(\widehat R_j),\quad t=v_p(T_{\rm aff}),
$$




$$
d=\max(r-f,0),\qquad e=\min(t,d),\qquad k=v_p(\kappa_j).
$$


When $d>0$, $r=d+f\ge e+f$. Both terms on the left of the paid identity have valuation at least $e+g$. Hence


$$
k+f+v_p(\widehat{\mathcal B}_j)\ge e+g,
$$


which is exactly the asserted divisibility.

This is an additional paid support statement. It is **not** the final all-prime gcd theorem: the evaluated $\widehat{\mathcal B}_j$ can still have large correlated factors, and other actual clearers and contents remain to be transported.

In particular, no argument here proves


$$
\log J_{\rm res}=o(n\log n).
$$


The source-specific paid-contact correlation lemma remains a genuine open obligation.

---

# 8. Final arithmetic and the global irrationality criterion

The complete forcing must remain in the determinant construction. In particular, the retained closure contains the logarithmic forcing, both exponential boundary charges, finite returns, exterior constants, and the physical terminal. The core approximants $F^*$ are not replacements for the actual multiplier or for the complete forcing identity.

For the determinant construction retain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


where $\ell_{\rm clr}$ is the actual least simultaneous clearer, and


$$
g_\ell=\gcd(|A_\ell|,|B_\ell|)
$$


is over **all primes**. For $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
$$


and the whole same-index error is


$$
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{g_\ell}
\det H_{\rm complete}.
$$



For the weighted construction retain the actual integer columns and weights:


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
$$


The actual primitive multiplier is still


$$
d_B^2/g_B,
$$


not a selected-prime normalization and not division by the $29$-adic unit $C_n$.

At the same original index,


$$
q_n(e+\pi)-p_n=-q_n\epsilon_n.
$$


The retained signed-error theorem supplies eventual nonzero whole error and its stated asymptotic decay. What remains missing is an all-prime estimate for the actual $q_n$ proving


$$
0<|q_n\epsilon_n|\longrightarrow0
$$


on the same infinite original indices.

For comparison, if $e+\pi=a/d$ were rational, every nonzero value of
$q_n(e+\pi)-p_n$ would have absolute value at least $1/d$. Thus the displayed nonzero convergence would prove irrationality. No accepted result in this report establishes that convergence.

The ternary and prime-$29$ infinite subfamilies are different. They cannot be combined into an unproved simultaneous primitive-denominator estimate.

---

# 9. Bounded certificates and changed obligations

No closed expensive computation should be repeated.

## 9.1 Ternary actual-reset obligation

The immediate obligation is a proof for the **actual recovered producer** of either



$$
\Phi_R\in3^{21}M,
$$


or the sufficient reset/coefficient/endpoint statement


$$
\mathscr R\equiv(y+1)x^{A-48}q_{20}(x)\pmod{3^{20}},
\qquad \deg q_{20}\le48,
$$


together with the degree information used in the orthogonality multiplier argument.

A single numerical tuple cannot prove this infinite-family assertion. The coordinator should recover the exact producer reset and coefficient identities and supply a symbolic coefficientwise proof. The precision-$7$ block receipt is not a substitute.

After actual transport is established, a finite next-digit certificate for one selected original tuple needs only:

- exact original $j,h,D,m,\nu,t$;
- actual residual entries on $0\le i,j<t$ modulo $3^{28}$;
- the transported endpoint and complete bordered diagonal.

Expected output:


$$
-\bigl((S_{\rm act})_{ij}/3^{27}\bigr)_{i,j<t}\pmod3,
$$


the vector $((-1)^i)_{i<t}$, and the resulting complete distinguished pairing. This is a finite-tuple certificate only.

The old $68$-monomial scaled moment check need not be repeated.

## 9.2 Prime-$29$ low row

The actual-tail issue at the displayed digit is closed by the proof above. Neither a new $\mathbf H_8$ calculation nor a large adjoint-tail sum is needed.

The genuine bounded remaining calculation is the new low row. Its bounded inputs are those already specified in A2:

- the stored first-column profiles;
- the $29$ new symbol residues through $s=58$;
- the $29$ exterior residues for $2\le h\le30$;
- the additional rows through $5104$;
- the seven-row reconstruction correction;
- the original split at $5044$.

The proposed upper bound is $10\,996\,170$ new branch-row evaluations, with a $306300$-entry Pascal table. The old $5075$-row calculation is reused, not rerun.

Expected verifiable outputs are:

1. the complete triple
   

$$
(\mathcal A,\mathcal D,\mathcal L)\in\mathbb F_{29}^3;
$$


2. source/return and lower/upper subtotals;
3. the seven-row table and reconstruction subtotal $14$;
4. the boundary-correct observation identity.

No value for that triple is predicted.

## 9.3 Paid contact correlation

The fixed-size direction and raw-scale certificate is already sufficient and need not be repeated.

The remaining contact obligation is not another symbolic direction check. It is an infinite-family estimate for the evaluated paid correlations


$$
\gcd\left(
D_j,\left|\frac F{g_{\rm aff}}\widehat{\mathcal B}_j\right|
\right),
$$


with the actual contents and clearers transported to the final arithmetic. Direct height bounds generally give only an $O(n\log n)$ scale and do not prove the required $o(n\log n)$ estimate.

---

# 10. Proof-status summary and conclusion

| Statement | Status after this review |
|---|---|
| Stationary finite-Gram lemma | Proved |
| Nested corrected-column use for every $1\le p\le20$ | Valid at the accepted finite-core scope |
| First two core digits with $Y_m$ and LOW feedback | Verified |
| Complete depth-$26$ moment formula | Proved, including all lower poles and factorial term |
| Explicit $K_{26}$, nonzero criterion, rank, radical | Proved |
| Infinite original rank subwindow | Proved |
| Actual endpoint modulo $3$ | Proved from exact perturbation and integrality |
| Actual $K_{26}=K_{26}^{\rm core}$ | Conditional on the stronger actual linear premise |
| Stronger actual-reset premise for the recovered producer | Not established by the supplied recovery receipt |
| Leading $Y/p^5$ ordinary-$000$ form | Valid using the retained complete branch/guard results |
| Seven-row reconstruction correction $14$ | Verified with source units |
| $c\ge3$ classification and $Y\in p^6$ | Proved at the retained original-source scope |
| Whole $p^{11}$-digit zero for $c\ge4$ | Proved; infinite scope uses the retained unbounded-content theorem |
| Advertised $Le_i\in p^3$ through $231$ | Not independently closed by the stated guard-range assertion |
| $Le_i\equiv0\pmod p$ for $i<435$ | New finite-boundary proof |
| Actual $V=L\bar w\in p$, including $c=2$ feedback | New proved consequence |
| Physical terminal $14k_B^2$ | Verified at the stated next flat digit |
| Completed new three-residue low row | Unevaluated |
| Actual contact directions and raw scale | Verified |
| Least denominator/content ledger and $\kappa_j\mid2N^2$ | Proved |
| Paid contact identity and large-prime support | Proved |
| All-prime contact support with explicit $\kappa_j$ | New proved extension |
| Subfactorial resonance or final all-prime denominator theorem | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

The principal new rigorous conclusions are the independently checked depth-$26$ **core** theorem, the direct finite-boundary annihilation of the actual prime-$29$ tail at the displayed feedback digit, and the explicit denominator/content accounting for the paid contact projections.

The exact remaining bottlenecks are:

1. the stronger actual-producer linear observation needed to transport the ternary Hankel operator;
2. the next actual radical digit, including its producer contribution and complete bordered diagonal;
3. the new prime-$29$ low row and, if necessary, its actual-upper-word accepting value;
4. growing-depth primitive alignment;
5. transport through every actual content, paid division, and least clearer to the **ALL-prime final gcd**;
6. comparison of the resulting **actual primitive denominator** with the **nonzero whole error at the same infinite original indices**.



$$
\boxed{\text{No unconditional proof of rationality or irrationality of }e+\pi\text{ has been obtained.}}
$$


