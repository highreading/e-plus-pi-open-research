> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The actual adjoining ternary column: a finite-prefix evaluation and the remaining corrected-column obligation

## Abstract

The adjoining-column identity


$$
(\bar L_c e_0)_u=[y^{E-\ell-u}](1-y)^{-b},
\qquad 0\le u<\ell,
\tag{A}
$$


is **not established or refuted by the supplied sources or by the calculations below**. Here, as in turn14, the identity is over $\mathbb F_3$; an exact equality over $\mathbb Z_3$ would be a substantially stronger assertion.

There is, however, a new evaluation involving the **actual finite prefix**, rather than an arbitrary completion of the known Hankel block. It reduces the complete discrepancy in (A) to a specific, paid observation of the actual LOW/HIGH correction of the adjoining column.

Write


$$
a_0=\frac{P_0-1}{2},\qquad
J_0=\frac{P_0}{3}-1,\qquad
k_0=a_0-J_0=\frac{P_0/3+1}{2}.
$$


Let $C_i=G_c(W,z_i)$, let $E_c=G_c(W,W)$, and put


$$
j_* = R_*+\ell.
$$


Then the discrepancy in (A) is exactly


$$
\boxed{
(\bar L_ce_0)_u-[y^{E-\ell-u}](1-y)^{-b}
=
\overline{
\frac{(C_{R_*+u}+3C_{k_0+u})^TE_c^{-1}C_{j_*}}
     {3^{28}}
}.
}
\tag{B}
$$


The numerator in this formula is divisible by $3^{28}$; that division is justified below. Every $C_i$ and the inverse in (B) belongs to the original complete core.

The key finite-prefix calculation is


$$
\boxed{
\bar{\mathsf A}^{-1}\,\overline{\mathsf B_{\cdot,u}/3}
=-e_{k_0+u}
\qquad(0\le u<\ell).
}
\tag{C}
$$


Thus the prefix correction observes an actual, explicitly located prefix row. It cannot simply be discarded, but it need not be recomputed as a large quadratic contraction.

On the actual second radical, the model term in (A) contracts to zero. Consequently, for


$$
g_a=(y-1)^by^a,\qquad 0\le a\le b/2,
$$


the complete unresolved observation is


$$
\boxed{
(G^T\bar L_ce_0)_a
=
\overline{
\frac{
G_c\!\left(
x^Dy^{k_0}(y^{P_0/3}+3)g_a,\,
z_{j_*}-F_{j_*}
\right)}
{3^{28}}
}.
}
\tag{D}
$$


This identifies the actual correction and its physical-terminal component. It is **not an evaluation of the residue on the right**. In particular, this report does not replace that residue by zero.

The strongest established producer precision therefore remains the accepted direct bound and the complete rank-at-most-two return formula. The endpoint and diagonal returns remain active. No new unconditional relative-cofactor gain, all-prime primitive saving, or irrationality theorem follows.

---

## 1. Scope and original objects

### 1.1 Original indices and finite boundaries

Throughout, the index domain remains


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$


with


$$
m=2^{2j-1},\qquad n=4^j+1=2m+1,\qquad A=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$


and


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$



I use the fixed interior subwindow of turn14:


$$
\frac{103}{1000}<\frac{N_0}{P_0}<\frac{104}{1000}.
\tag{1.1}
$$


The relations


$$
P_0=243P=3^{h-27},\qquad N_0=243r,\qquad D=P_0+N_0,
$$




$$
P=3^{h-32},\qquad r\equiv2\pmod9,\qquad r\ \text{odd},
$$




$$
4^j=243(3^{26}-1)P-243r+1
\tag{1.2}
$$


are retained. Infinitude in this fixed subwindow is reused only at the scope of the previously established original-index density result.

Put $x=y-1$. The finite polynomial coordinates are


$$
U_s=x^s\quad(0\le s<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),
$$




$$
Y_t=y^t\quad(d\le t\le m),
\qquad
\nu=D/2-1,\qquad d=D+\nu.
$$


The physical HIGH terminal is $Y_m$.

As before,


$$
Q=P_0/9,\qquad b=Q-N_0,\qquad
\ell=\frac{3b}{2}+1,\qquad E=\frac{Q-3}{2},
$$




$$
R_*=\frac{P_0+1}{2},\qquad
\tau=\frac{N_0-3}{2},
$$




$$
K=\{0,\ldots,\ell-1\},\qquad
J=\{\ell,\ldots,\tau-1\}.
$$


The first column of $J$, in original middle coordinates, is


$$
j_*=R_*+\ell.
\tag{1.3}
$$


It is not the physical terminal. Indeed,


$$
n_J=|J|=\frac{Q-4b-5}{2}\longrightarrow\infty,
$$


so, for sufficiently large original tuples, $j_*\le\nu-2$.

### 1.2 Complete moment functional and exact correction

The functional is


$$
\mathcal M(P)=
-\frac{3^h}{4}\mathfrak f(P)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](P-P(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^t)=(2t)!.
\tag{1.4}
$$


Its domain here is degree at most $2n-1$, and its denominator cutoff is


$$
2v+1\le4n-3=4H-4D+5.
\tag{1.5}
$$



The complete core is


$$
G_c(f,g)=\mathcal M(Q_cfg),\qquad
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=-71-A.
$$



Let $W=[U\ Y]$, and define


$$
E_c=G_c(W,W),\qquad C_i=G_c(W,z_i).
$$


Then


$$
F_i=z_i-WE_c^{-1}C_i,
\qquad G_c(W,F_i)=0.
\tag{1.6}
$$


In particular,


$$
r_i:=z_i-F_i=WE_c^{-1}C_i
\tag{1.7}
$$


is the **actual** LOW/HIGH correction.

The exact core Schur entries satisfy


$$
(S_c)_{ij}
=
G_c(z_i,z_j)-C_i^TE_c^{-1}C_j.
\tag{1.8}
$$



The complete core is therefore defined well enough to state the outstanding column without ambiguity. The obstacle below is not that $L_c$ is undefined.

---

## 2. Results reused, without reopening their calculations

The coordinator’s current acceptance of H2 supersedes the “pending H2” status in turn14. I reuse the following at their stated sufficiently-large original scope:

1. The integrality and unimodularity of the basis $[W,F]$.
2. $E_c^{-1},E_{\rm act}^{-1}\in3^{-1}M$.
3. $S_c\in3^{26}M$.
4. The established finite-prefix leading matrix and its inverse.
5. The first-radical block, including the fact that every row indexed by $K$ is zero at that digit.
6. H2’s complete $K\times K$ second-layer identification.
7. The accepted nine-period source annihilation and the direct bound
   

$$
G^T(S_{\rm act}-S_c)G\in3^{30}M.
$$


8. The physical-terminal identities and complete return formulas of turn14.

No H2 rank calculation, nine-period producer calculation, or turn16 interpolation obstruction is repeated here.

The distinction essential to this turn is that H2 supplies a $K\times K$ statement. It does not itself supply the $K\times\{\ell\}$ strip.

---

## 3. The complete *uncorrected* adjoining strip is evaluated

This section evaluates $G_c(z_{R_*+u},z_{j_*})$, not $G_c(F_{R_*+u},F_{j_*})$. That distinction will be maintained.

The accepted complete low-degree moment formula from turn12 is


$$
\begin{aligned}
\mathcal M((y+1)x^HP)\equiv{}&
4\,3^{26}P_{c_9}
+4\,3^{27}P_{c_3}\\
&+3^{28}
\sum_{a\in\{1,5,7,11,13\}}a^{-1}P_{c_a}
\pmod{3^{29}},
\end{aligned}
\tag{3.1}
$$


where


$$
c_a=\frac{a(P_0/3)-1}{2},
\qquad \deg P\le2D.
$$


This formula includes the complete pole sum. The factorial term was paid by its factor $3^h$, not deleted from the functional.

### Proposition 3.1 — The raw adjoining strip

For every $0\le u<\ell$,


$$
\boxed{
\frac{G_c(z_{R_*+u},z_{j_*})}{3^{28}}
\equiv[y^{E-\ell-u}]x^{N_0}\pmod3.
}
\tag{3.2}
$$



#### Proof

Use (3.1) with


$$
P=x^D(\beta+3y)y^{R_*+u+j_*}.
$$


Since $P_0=9Q$,


$$
R_*+u+j_*=9Q+1+u+\ell.
$$


The degree of $P$ is at most $2D$ on the fixed subwindow, so (3.1) applies within its original finite boundary.

The $c_9$-extraction in $x^D$ is


$$
k_u=\frac{9Q-3}{2}-u-\ell.
\tag{3.3}
$$


At the two ends of the strip,


$$
\frac{9Q-5}{2}-3b\le k_u
\le\frac{9Q-5-3b}{2}.
$$


In particular,


$$
k_u-(4Q-b)\ge
\frac{Q-4b-5}{2}=n_J>0,
\tag{3.4}
$$


and $k_u<6Q$. The same strict band exclusions hold for $k_u-1$ for sufficiently large tuples.

Modulo $27$, the only coefficient band of $x^{9Q}$ that can contribute to $x^{9Q}x^{Q-b}$ at these indices is the band beginning at $4Q$. Its coefficient satisfies


$$
\frac{[y^{4Q}]x^{9Q}}9\equiv1\pmod3.
$$


Consequently,


$$
\frac{[y^{k_u}]x^D}{9}
\equiv[y^{k_u-4Q}]x^{N_0}
=[y^{E-\ell-u}]x^{N_0}\pmod3.
\tag{3.5}
$$


Both coefficients at $k_u$ and $k_u-1$ are divisible by $9$. Thus the $3y$-part of $\beta+3y$ contributes only at order $3^{29}$, while $\beta\equiv1\pmod3$.

For completeness, the remaining extractions in (3.1) are excluded as follows:

- $c_1,c_3,c_5$ lie below the minimum degree.
- At $c_7$, the extraction index in $x^D$ is
  

$$
\frac{3Q-3}{2}-u-\ell.
$$


  Its distance above $N_0=Q-b$ is at least $n_J$; it is below $9Q$. It is therefore in the characteristic-$3$ coefficient gap.
- At $c_{11}$, the extraction lies in the same gap $(N_0,9Q)$.
- At $c_{13}$, its distance above $D=10Q-b$ is at least $n_J$.

This proves (3.2), including all pole layers required modulo $3^{29}$. ∎

Since $E-\ell-u<Q$,


$$
-x^{N_0}
=(1-y^Q)(1-y)^{-b}
$$


gives


$$
-\frac{G_c(z_{R_*+u},z_{j_*})}{3^{28}}
\equiv[y^{E-\ell-u}](1-y)^{-b}\pmod3.
\tag{3.6}
$$



Thus the proposed adjoining-column expression is correct for the raw core pairing after normalization. The remaining issue is precisely the actual correction and finite-prefix return.

---

## 4. A new evaluation of the actual finite-prefix observation

Write


$$
U_c=-S_c/3^{26}
=
\begin{pmatrix}
\mathsf A&\mathsf B\\
\mathsf B^T&\mathsf C
\end{pmatrix},
$$


where the prefix has indices $0,\ldots,R_*-1$.

Set


$$
a_0=R_*-1=\frac{P_0-1}{2},\qquad
J_0=\frac{P_0}{3}-1.
$$


The accepted finite inverse is


$$
(\bar{\mathsf A}^{-1})_{pi}
=[y^{p+i-a_0}](1-y)^{-N_0},
\qquad 0\le p,i\le a_0.
\tag{4.1}
$$


For $u\in K$, the accepted actual divided cross-column is


$$
v_u:=\overline{\mathsf B_{\cdot,u}/3},
\qquad
(v_u)_i=[y^{J_0-i-u}]x^{N_0}.
\tag{4.2}
$$


Only the $K$-columns are being used in (4.2); no assertion about the adjoining column is imported.

### Proposition 4.1 — The prefix inverse is a coordinate selector

Let


$$
k_0=a_0-J_0=\frac{P_0/3+1}{2}.
$$


Then


$$
\boxed{
\bar{\mathsf A}^{-1}v_u=-e_{k_0+u}
\qquad(0\le u<\ell).
}
\tag{4.3}
$$



#### Proof

Because $N_0$ is odd,


$$
x^{N_0}=-(1-y)^{N_0}.
$$


The $p$-th component of the left side is therefore


$$
-\sum_{i=0}^{a_0}
[y^{p+i-a_0}](1-y)^{-N_0}
[y^{J_0-i-u}](1-y)^{N_0}.
\tag{4.4}
$$


The two coefficient indices sum to


$$
T=p-a_0+J_0-u=p-k_0-u.
$$



The finite bounds do not truncate the convolution. Indeed, a nonzero term requires both coefficient indices to be nonnegative. As $i$ varies, the first index then runs through all integers from $0$ to $T$; the inequalities $0\le i\le a_0$ are automatic because


$$
0\le J_0-u<a_0,\qquad 0\le p\le a_0.
$$


Thus (4.4) is


$$
-[y^T](1-y)^{-N_0}(1-y)^{N_0}
=-\mathbf1_{\{T=0\}}.
$$


This is precisely (4.3). ∎

This is an actual finite-boundary result. In particular, if


$$
v_*=\overline{\mathsf B_{\cdot,\ell}/3}
$$


denotes the as-yet unevaluated divided adjoining cross-column, then


$$
\boxed{
v_u^T\bar{\mathsf A}^{-1}v_*=-(v_*)_{k_0+u}.
}
\tag{4.5}
$$


The whole prefix contraction has become one specified entry of the actual adjoining cross-column.

---

## 5. The second raw strip needed by that selector

The selector in (4.5) observes prefix indices


$$
p_u=k_0+u.
$$


These satisfy


$$
R_*+u-p_u=P_0/3.
\tag{5.1}
$$



### Proposition 5.1

For every $0\le u<\ell$,


$$
\boxed{
G_c(z_{p_u},z_{j_*})\in3^{28}\mathbb Z_3.
}
\tag{5.2}
$$



#### Proof

Now


$$
p_u+j_*=6Q+1+u+\ell.
$$


The $c_9$-extraction in $x^D$ is


$$
k'_u=\frac{15Q-3}{2}-u-\ell.
$$


Its minimum satisfies


$$
k'_u-(6Q+N_0)
\ge\frac{Q-4b-5}{2}=n_J>0,
$$


and its maximum is below $9Q$.

Modulo $9$, the possible bands of $x^{9Q}x^{N_0}$ begin at


$$
0,\quad 3Q,\quad 6Q,\quad 9Q.
$$


The displayed extraction, and its one-step shift for the $3y$-term, lie strictly between the end of the $6Q$-band and the start of the $9Q$-band. Their coefficients are therefore zero modulo $9$.

The $c_3$-extraction is below the minimum degree. All remaining terms of (3.1) already contain $3^{28}$. Hence the complete pairing is divisible by $3^{28}$. ∎

Again, this is a raw-pairing statement, not a claim that the corrected cross-column vanishes.

---

## 6. Exact discrepancy for the actual adjoining column

The exact prefix Schur complement is


$$
\mathcal R_c=\mathsf C-\mathsf B^T\mathsf A^{-1}\mathsf B.
$$


By definition,


$$
L_c=\mathcal R_{c,KJ}/9.
\tag{6.1}
$$



The first-radical result implies


$$
\mathcal R_{c,KJ}\in9M.
$$


Also $\mathsf B\in3M$. Hence the divisions used in (6.1) and below are paid.

Define


$$
h_u=[y^{E-\ell-u}](1-y)^{-b}.
$$



### Theorem 6.1 — Actual adjoining-column discrepancy

For $0\le u<\ell$,


$$
\boxed{
(\bar L_ce_0)_u-h_u
=
\overline{
\frac{
(C_{R_*+u}+3C_{p_u})^TE_c^{-1}C_{j_*}
}{3^{28}}
},
\qquad p_u=k_0+u.
}
\tag{6.2}
$$



#### Proof

Put


$$
\Gamma_{ij}=C_i^TE_c^{-1}C_j.
$$


By (1.8),


$$
(S_c)_{ij}=G_c(z_i,z_j)-\Gamma_{ij}.
$$



For $i=R_*+u$, Proposition 3.1 and the divisibility of the actual Schur strip show


$$
\Gamma_{i,j_*}\in3^{28}\mathbb Z_3.
\tag{6.3}
$$


For $p=p_u$, the prefix cross-block satisfies


$$
(S_c)_{p,j_*}\in3^{27}\mathbb Z_3,
$$


so Proposition 5.1 gives


$$
\Gamma_{p,j_*}\in3^{27}\mathbb Z_3.
\tag{6.4}
$$


Thus $\Gamma_{i,j_*}+3\Gamma_{p,j_*}$ is divisible by $3^{28}$.

The exact normalized strip is


$$
\bar L_{c,u0}
=
-\overline{\frac{(S_c)_{i,j_*}}{3^{28}}}
-v_u^T\bar{\mathsf A}^{-1}v_*.
$$


Using (4.5),


$$
\bar L_{c,u0}
=
-\overline{\frac{(S_c)_{i,j_*}}{3^{28}}}
+(v_*)_{p}.
\tag{6.5}
$$


But


$$
(v_*)_p
=
-\overline{\frac{(S_c)_{p,j_*}}{3^{27}}}
=
\overline{\frac{\Gamma_{p,j_*}}{3^{27}}},
\tag{6.6}
$$


where Proposition 5.1 removed the raw pairing only at its proved precision.

Finally, Proposition 3.1 gives


$$
-\overline{\frac{(S_c)_{i,j_*}}{3^{28}}}
=
h_u+\overline{\frac{\Gamma_{i,j_*}}{3^{28}}}.
$$


Substitution in (6.5) proves (6.2). ∎

### What has and has not been evaluated

The raw moment contribution and the finite-prefix inverse contraction have now both been evaluated.

The remaining residue is an actual LOW/HIGH projection pairing. Formula (6.2) does **not** prove it vanishes. Calling its numerator a new symbol would not resolve that obligation.

In particular, (A) is equivalent to the actual source statement


$$
(C_{R_*+u}+3C_{p_u})^TE_c^{-1}C_{j_*}
\in3^{29}\mathbb Z_3
\quad(0\le u<\ell).
\tag{6.7}
$$


This is one digit stronger than the divisibility proved in (6.3)–(6.4).

---

## 7. Contraction with the actual radical

Under accepted H2, the full second radical is


$$
(y-1)^b\mathbb F_3[y]_{\le b/2}.
$$


Take its integral representatives


$$
g_a=(y-1)^by^a,\qquad 0\le a\le b/2.
$$



The model column contracts to


$$
\begin{aligned}
\sum_{u=0}^{\ell-1}(g_a)_u h_u
&=[y^{E-\ell}](1-y)^{-b}g_a\\
&=[y^{E-\ell}]y^a=0,
\end{aligned}
\tag{7.1}
$$


because


$$
E-\ell=n_J+b/2>b/2\ge a.
$$



Let


$$
\widehat l=G^T\bar L_ce_0.
$$


By linearity of $C_i=G_c(W,z_i)$, Theorem 6.1 gives


$$
\boxed{
\widehat l_a
=
\overline{
\frac{
G_c(\Psi_a,r_{j_*})
}{3^{28}}
},
}
\tag{7.2}
$$


where


$$
\Psi_a=x^Dy^{k_0}(y^{P_0/3}+3)g_a,
\qquad
r_{j_*}=z_{j_*}-F_{j_*}.
\tag{7.3}
$$


All polynomials lie in the original degree-$\le m$ space, so the moment products stay within degree $2n-1$.

This is a sharper, source-specific follow-on target:


$$
\boxed{
G_c(\Psi_a,r_{j_*})\in3^{29}\mathbb Z_3
\qquad(0\le a\le b/2).
}
\tag{7.4}
$$


It is weaker than the full entrywise identity (A), and it is exactly sufficient for the first matrix-return cancellation.

### The physical terminal is still present

Expand the exact correction in its actual $W$-coordinates:


$$
r_{j_*}
=
\sum_{s=0}^{D-1}\alpha_sx^s+
\sum_{t=d}^{m}\gamma_ty^t.
\tag{7.5}
$$


Since $z_{j_*}$ has degree below $m$,


$$
\gamma_m=-[y^m]F_{j_*}=-3^{20}t_{j_*}.
\tag{7.6}
$$


Thus (7.2) contains the physical-terminal contribution


$$
-3^{20}t_{j_*}\,G_c(\Psi_a,Y_m)
$$


inside its complete numerator. Neither $t_{j_*}=0$ nor separate divisibility of this summand by $3^{28}$ has been proved.

The division in (7.2) is paid for the **whole numerator**. It cannot be distributed among summands without further estimates.

---

## 8. Why the supplied support statements do not yet prove the last digit

The supplied files give:

- the complete jets through modulo $27$;
- existence of precision-$20$ representatives with a degree gap;
- selected support-envelope consequences;
- the completed $K\times K$ H2 calculation.

They do not reproduce a full, quantified higher-jet support theorem for the new mixed strip sufficient to verify (6.7) or (7.4). In particular, the statement needed is not merely that a representative exists modulo $3^{20}$. One must control the complete corrected-column pairings with $F_{j_*}$, including the higher-order terms and the finite LOW/HIGH projection.

The indispensable absent proof input is therefore:

> **A precise higher-jet support-and-remainder statement for the actual corrected adjoining column $F_{R_*+\ell}$, and its mixed pairings with $F_{R_*+u}+3F_{k_0+u}$, strong enough to determine those complete pairings modulo $3^{29}$.**

The core itself is defined. This missing input is a theorem or certificate about that core, not permission to choose another completion.

For calculations involving the complete actual endpoint-adapted scalar beyond the supplied congruences, additional original definitions are also absent from these packets: the component definitions of $h_{\rm vec}$ and $v$, the exact signed value of $\xi$, and the original formulas defining the endpoint vector and exterior diagonal. Their integrality, unit status, and certain perturbation consequences are supplied, but those facts do not determine their higher digits.

---

## 9. A useful paid-precision lemma for an actual certificate

There is a short way to certify the outstanding residue without reconstructing corrected columns to precision $29$.

### Proposition 9.1 — Fifteen digits of corrected columns suffice

Let $F_i^{[15]}$ be any integral degree-$\le m$ polynomial satisfying


$$
F_i^{[15]}\equiv F_i\pmod{3^{15}}.
$$


Then


$$
\boxed{
G_c(F_i^{[15]},F_j^{[15]})
\equiv G_c(F_i,F_j)\pmod{3^{30}}.
}
\tag{9.1}
$$



#### Proof

The integral unimodular basis $[W,F]$, together with


$$
G_c(W,F)=0,\qquad S_c\in3^{26}M,
$$


implies


$$
G_c(F_i,\Delta)\in3^{26}\mathbb Z_3
$$


for every integral degree-$\le m$ polynomial $\Delta$.

Write


$$
F_i^{[15]}=F_i+3^{15}\Delta_i.
$$


Expansion gives two linear errors divisible by $3^{41}$, and one quadratic error divisible by $3^{30}$, using complete functional integrality. This proves (9.1). ∎

Consequently, (7.2) also has the certificate form


$$
\boxed{
\widehat l_a
=
-\overline{
\frac{
G_c(F_{G,a}+3F_{G,a}^{\rm pre},F_{j_*})
}{3^{28}}
},
}
\tag{9.2}
$$


where


$$
F_{G,a}=\sum_u(g_a)_uF_{R_*+u},
\qquad
F_{G,a}^{\rm pre}=\sum_u(g_a)_uF_{k_0+u}.
$$


The model contraction has vanished by (7.1). Both arguments in (9.2) may be replaced by certified precision-$15$ representatives when computing the residue modulo $3$.

This is a paid precision reduction for an **actual** certificate. It does not furnish the certificate or prove its output is zero.

---

## 10. Complete producer, endpoint, and diagonal returns

The actual source remains


$$
Q_{\rm act}=3P_n=Q_c+3^7\mathscr R,
$$


with


$$
3^7\mathscr R=\sum_{a=0}^{A+1}e_ax^a,
\qquad
e_a=-\frac{(A+1)!}{a!}(t_a+\xi v_a),
$$


and complete force


$$
t=3nh_{\rm vec}
+(b_{\rm force}+6)e_{n-1}
+\frac{2b_{\rm force}}{n-1}e_{n-2},
\qquad b_{\rm force}=-n-66.
$$


The endpoint charge


$$
\mathscr R(-1)=-\frac{\xi((A+1)!)^2}{3^7}
$$


and the full return


$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right)
$$


are unchanged.

Let


$$
\widehat t=G^T\bar t_K.
$$


The accepted direct producer theorem and physical-terminal inverse evaluation give


$$
\boxed{
\frac{
G^T(\mathcal S^{(2)}_{\rm act}-\mathcal S^{(2)}_c)G
}{27}
\equiv
\bar\kappa
\left(\widehat t\,\widehat l^{\,T}
+\widehat l\,\widehat t^{\,T}\right)
\pmod3.
}
\tag{10.1}
$$


The present report identifies $\widehat l$ by (7.2) or (9.2), but does not evaluate it.

Therefore:

- The direct normalized producer difference remains proved divisible by $81$.
- The complete second-reduction difference is known at the first return as (10.1).
- Divisibility of that complete difference by $81$ remains conditional on the vanishing of the displayed return, for example on (7.4).

The endpoint and diagonal do not disappear if the matrix return vanishes. With


$$
\varepsilon_0=(-1)^{R_*+\ell},
\qquad u_0=\bar B^{-1}\bar f_J,
$$


the retained formulas are


$$
f^{(2)}_{\rm act}-f^{(2)}_c
\equiv3\bar\kappa\,\varepsilon_0\,\bar t_K\pmod9,
\tag{10.2}
$$




$$
\lambda^{(2)}_{\rm act}-\lambda^{(2)}_c
\equiv
-2\bar\kappa\,\varepsilon_0(\bar t_J^Tu_0)
\pmod3.
\tag{10.3}
$$


The established complete diagonal valuation


$$
v_3(\lambda^{(2)})=-1
$$


is retained. No stronger final scalar assertion follows from the new prefix calculation.

---

## 11. Consequences for the actual relative-cofactor target

Reuse the catalogue’s endpoint-complete finite blocks


$$
T=\begin{pmatrix}a&z^T\\z&C\end{pmatrix}\in27M,
\qquad v_3(\lambda)=-1.
$$


Assume $C$ is nonsingular. Write


$$
a=27\alpha,\quad z=27w,\quad C=27B,\quad \lambda=\eta/3,
$$




$$
\delta=\det B,\qquad
H_{\rm sc}=w^T\operatorname{adj}(B)w,
\qquad \sigma=H_{\rm sc}/\delta.
$$


The accepted exact scalar identity is


$$
\mathcal R=1-9\eta\alpha+9\eta\sigma.
\tag{11.1}
$$



For clarity, the corresponding relative-cofactor gain can be written explicitly. Put


$$
s=a-z^TC^{-1}z=27(\alpha-\sigma).
$$


Then


$$
D_0=\det C\,s,\qquad D_1=\det C\,\mathcal R,
$$


and, when both are nonzero,


$$
v_3D_0-v_3D_1=v_3(s)-v_3(\mathcal R).
\tag{11.2}
$$



Thus:

- If $v_3(\sigma)\ge-1$, then $\mathcal R\in1+3\mathbb Z_3$ and the gain is at least $2$.
- If $v_3(\sigma)\le-3$, then
  

$$
v_3(s)=3+v_3(\sigma),\qquad
  v_3(\mathcal R)=2+v_3(\sigma),
$$


  so the gain is exactly $1$.
- In the critical shell $v_3(\sigma)=-2$, one has $v_3(s)=1$, and the gain is
  

$$
1-v_3(\mathcal R).
$$


  Actual unit nonresonance would give gain $1$; deeper cancellation can destroy it.

These are conditional deductions from the exact finite scalar formula. Neither the adjoining-column calculation nor H2 determines which case the actual original blocks occupy.

Even a proved fixed gain of one or two ternary digits would not be an all-prime primitive-denominator theorem.

---

## 12. Divisions, contents, final gcd, and whole error

The payments used here are:

- the original $3^7$ producer normalization and the previously paid normalization of $\xi$;
- all pole denominators, paid by $3^h$ on the original cutoff;
- the original $3^{-1}$ LOW/HIGH inverse;
- the unit prefix inverse;
- the normalization $S_c/3^{26}$;
- the divided prefix columns $\mathsf B/3$;
- the first-radical inverse $3^{-1}B^{-1}$;
- the $3^{28}$ divisions in (6.2), (7.2), and (9.2), paid for their complete numerators;
- the further $3^{-2}$ rank-$b$ elimination when passing to the accepted endpoint-adapted block.

No inverse of the remaining block $C$ has been bounded or paid uniformly.

The actual column contents and least simultaneous clearer are not reevaluated. Retain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$




$$
g_\ell=\gcd(|A_\ell|,|B_\ell|),
$$


where the gcd is over **all primes**. For $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},
\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$



The whole evaluated error remains


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
{g_\ell}\det H_{\rm complete}.
}
\tag{12.1}
$$


An irrationality proof still requires, at the same infinite original indices,


$$
B_\ell\ne0,\qquad \det H_{\rm complete}\ne0,
$$


and


$$
\log g_\ell-(m+1)\log\ell_{\rm clr}
-\log|\det H_{\rm complete}|\longrightarrow+\infty.
\tag{12.2}
$$


None of these global obligations is discharged here.

---

## 13. Bounded verification and the next proof packet

No computation was executed. No repetition of the accepted H2 or nine-period calculations is requested.

### 13.1 Mathematical proof packet needed

The most useful next packet is a proof of (7.4), or a higher-jet theorem whose stated bounds imply it. It must specify:

1. the actual adjoining column $F_{j_*}$;
2. the mixed corrected combinations $F_{G,a}+3F_{G,a}^{\rm pre}$;
3. every retained coefficient-support bound and remainder valuation;
4. the original degree cutoff;
5. the terminal coefficient in (7.6);
6. the complete moment evaluation modulo $3^{29}$.

A proof only for $K\times K$ is not sufficient.

### 13.2 A bounded new finite certificate check

If the coordinator already has an authored certificate for one original admissible index and one radical index $a$, the new check can be confined to one residue.

**Inputs**

- One specified original $(j,h)$, with a certificate of (1.1)–(1.2).
- One $a$ with $0\le a\le b/2$.
- Certified precision-$15$ representatives of
  

$$
F_{G,a}+3F_{G,a}^{\rm pre},\qquad F_{j_*}.
$$


- A bounded, coordinator-authored exact-arithmetic certificate evaluating their complete $G_c$-pairing modulo $3^{29}$. The certificate should declare its finite operation count and representation-size bounds before inspection.

No unrestricted reconstruction is requested. If no such bounded original packet is available, the appropriate output is “no eligible certificate packet,” not an auxiliary surrogate.

**Expected verifiable output**

A residue $N_a$, $0\le N_a<3^{29}$, satisfying


$$
N_a\equiv
G_c(F_{G,a}+3F_{G,a}^{\rm pre},F_{j_*})
\pmod{3^{29}}.
$$


The proved divisibility requires


$$
N_a\equiv0\pmod{3^{28}}.
$$


The new output is


$$
\widehat l_a\equiv-N_a/3^{28}\pmod3.
$$



- Residue zero proves the desired contraction for that one $a$ and that one original index.
- Residue nonzero disproves the contraction there and, by (7.1), disproves (A) there.
- Either result has only its stated finite scope.

---

## 14. Proof-status ledger and conclusion

| Statement | Status |
|---|---|
| Complete raw adjoining strip, Proposition 3.1 | Proved |
| Actual finite-prefix selector, Proposition 4.1 | Proved |
| Complete raw strip observed by that selector | Proved |
| Exact actual discrepancy formula (6.2) | Proved, with the whole $3^{28}$ division paid |
| Model-column contraction on the actual radical | Evaluated and zero |
| Actual radical discrepancy formula (7.2) | Proved |
| Residue in (7.2) vanishes | Open |
| Full adjoining-column identity (A) | Neither proved nor refuted |
| Precision-$15$ certificate sufficiency | Proved |
| Complete first producer return | Retained; its unresolved vector is now identified by (7.2) |
| Endpoint and diagonal returns | Retained, not canceled |
| Actual critical-shell nonresonance or scalar congruence | Open |
| Growing relative-cofactor gain | Open |
| Same-index all-prime gcd versus nonzero whole error | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

### Final conclusion

The new actual-source result is the finite-prefix observation


$$
\bar{\mathsf A}^{-1}\overline{\mathsf B_{\cdot,u}/3}
=-e_{k_0+u},
$$


together with the evaluated raw strips. These yield the exact boundary discrepancy


$$
\boxed{
(\bar L_ce_0)_u-[y^{E-\ell-u}](1-y)^{-b}
=
\overline{
\frac{(C_{R_*+u}+3C_{k_0+u})^TE_c^{-1}C_{j_*}}
{3^{28}}
}.
}
$$



The precise next bottleneck is now the complete corrected-column observation


$$
\boxed{
G_c\!\left(
x^Dy^{k_0}(y^{P_0/3}+3)(y-1)^by^a,\,
z_{j_*}-F_{j_*}
\right)\in3^{29}\mathbb Z_3.
}
$$


It retains the actual LOW/HIGH inverse and the physical terminal. Its required residue has not been evaluated. Therefore this report does not claim to have completed Assignment A1 Turn17’s principal identity.

Even if that residue vanishes, the actual endpoint and diagonal returns, the critical scalar shell, and the quantitative all-prime primitive-denominator comparison remain separate obligations.



$$
\boxed{\text{No unconditional proof of rationality or irrationality of }e+\pi
\text{ is obtained.}}
$$


