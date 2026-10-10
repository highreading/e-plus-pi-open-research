> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, turn 3 — Audited saturated observables and a new original-phase norm congruence

## Executive conclusion

The new saturated certificate supports the proposed **23-bit contraction for both payloads**, but its justification requires an exact kernel lift and a normalization step that should be stated explicitly. I supply those steps below. In particular:

- the relevant presentation is the **single $163\times160$ matrix**, without a formal boundary coordinate;
- the reported free-coordinate contents $157,154$ survive passage to an exact saturated quotient;
- after dividing those contents, the available certified coordinate precisions are at least $194,197$ bits, respectively—not $351$ bits;
- these are more than sufficient for the required 23-bit compiled payloads.

I also audit the transport from turn 2. Its mathematical construction survives, with two important clarifications:

1. The negative odd-factorial extension takes values in $\mathbb Z_{(2)}^\times$, not generally in $\mathbb Z$. Its truncated Newton polynomial nevertheless represents it modulo $2^p$ on **all integers**.
2. The nonnegativity of the digit power $d_t$ must be proved for **every reachable prefix**, including prefixes with no valid terminal completion. A threshold argument supplies that proof. Negative factorials themselves are never introduced.

The substantive additional arithmetic result is the following original-phase norm law. For the supplied complete columns, with their common row signs suppressed only for purposes of writing the contractions, put


$$
X_j=\binom NjF_{b-j},\qquad
Y_j=\binom NjE_{b-j},\qquad 0\le j\le b.
$$


Then


$$
\boxed{4\mid X_j,\qquad 4\mid Y_j\quad\text{for every original row},}
$$


and


$$
\boxed{
\sum_{j=0}^{b}(sX_j+tY_j)^2\equiv0\pmod{32}
\qquad(s,t\in\mathbb Z).
}
$$


Consequently,


$$
\boxed{32\mid D_{\rm raw},\qquad16\mid E_{\rm raw}.}
$$



This is proved symbolically, not inferred from an unevaluated Gram contraction. The proof identifies a norm cancellation beyond the newly established common factor $4$: the fixed-normalized vector $X/4$ has even norm. It does **not** establish that $4$ is the actual column content, or that the primitive norm has exactly this cancellation.

The phase hypotheses are explicit. They hold at the supplied original binary index. I do not extrapolate them, or the short-numerator parity masks, to every member of an unspecified $u$-family.

No original Gram residue is computed here. The coordinator’s contraction remains an unreported computation.

---

## 1. Fixed data and scope

Retain


$$
b=150094635296999121,\qquad
n=4002b=600678730458590482242,
$$




$$
N=n+2,\qquad a=2n.
$$



The original physical range remains


$$
0\le j\le b.
$$



The accepted complete reconstructed series, at physical precision $2^{20}$, are


$$
F(z)=\frac{A_f(z)}{(1-z)^{a+81}},
\qquad
E(z)=\frac{A_e(z)}{(1-z)^{a+77}},
$$


with degrees $81,77$. The second series already contains the complete retained second force, finite return, terminal factorial cancellation, and exterior $+1$. None is added again.

For integer lifts of these short numerators, define


$$
X_j=\binom Nj[z^{b-j}]F(z),\qquad
Y_j=\binom Nj[z^{b-j}]E(z).
$$


These are signed-row equivalents of the supplied weighted columns: the common row signs cancel in the norm and mixed products. Thus


$$
\widetilde D=\sum_{j=0}^{b}X_j^2,\qquad
\widetilde E=\sum_{j=0}^{b}X_jY_j
$$


satisfy


$$
\widetilde D\equiv D_{\rm raw},\qquad
\widetilde E\equiv E_{\rm raw}\pmod{2^{20}}.
$$



All congruences below involving fewer than twenty physical bits therefore apply to the actual retained columns and contractions.

### Evidence classification

The new receipt reports:



$$
\begin{array}{c|c}
\text{Quantity}&\text{Reported value}\\ \hline
\text{Matrix shape}&163\times160\\
\text{Binary rank}&80\\
\text{Nonunit pivots}&80\\
\sum e_i&157\\
\max e_i&8\\
\text{High-degree minor valuation}&161\\
\text{Free payload contents}&157,\ 154\\
\text{Required observable bits}&23,\ 23
\end{array}
$$



I have audited the supplied producer’s mathematical logic. I have not independently regenerated its large artifact or recomputed these numerical outputs. They are **reported finite certificate data**, used at that scope.

The hashes identify the supplied source and receipt; a hash alone is not a mathematical verification of an unavailable artifact.

---

# Part I. Exact justification of the saturated payloads

## 2. The exact relation module

Let


$$
T(j)=\binom Nj^2
\binom{a+b-j-1}{b-j}^2,
\qquad 0\le j\le b,
$$


and define


$$
\mathcal A(j)=(N-j)^2(b-j)^2,\qquad
\mathcal B(j)=j^2(a+b-j)^2,
$$




$$
\Delta R(j)=\mathcal A(j)R(j+1)-\mathcal B(j)R(j).
$$



The exact finite functional is


$$
\mathscr L(P)=\sum_{j=0}^{b}T(j)P(j).
$$



The telescoping identity gives


$$
\mathscr L(\Delta R)
=
T(b)\mathcal A(b)R(b+1)-T(0)\mathcal B(0)R(0)=0.
$$


Both fluxes vanish exactly. In particular,


$$
\mathcal A(b)=0.
$$



This does not remove the physical terminal summand. At $j=b$, the norm and mixed summands remain


$$
\binom Nb^2 A_f(0)^2,\qquad
\binom Nb^2 A_f(0)A_e(0).
$$



Work over


$$
R=\mathbb Z_{(2)}.
$$


Let $V=R[j]_{\le162}$, and let $L$ be the exact $163\times160$ matrix whose columns are


$$
\Delta j^k,\qquad 0\le k\le159.
$$



The leading coefficients are


$$
[j^{k+3}]\Delta j^k=k+2n-4.
$$


Hence $L$ has rational rank $160$, and its saturated cokernel has rank three.

The earlier turn-2 presentations with a separate formal boundary are superseded here. No second matrix is needed.

---

## 3. Exact lifting of the modular annihilators

The supplied source constructs three modular free covectors, assembled as a matrix


$$
F\in\mathbb Z^{3\times163},
$$


and three integer generator representatives, assembled as


$$
S\in\mathbb Z^{163\times3},
$$


such that


$$
FL\equiv0\pmod{2^{512}},
\qquad
FS\equiv I_3\pmod{2^{512}}.
$$



These two congruences alone do not establish exact saturation. The high-degree minor supplies the missing argument.

### Lemma 1 — Exact kernel lift and exact dual normalization

Suppose the high-degree $160\times160$ submatrix $H$ of $L$, using rows $3,\ldots,162$, satisfies


$$
v_2(\det H)=161.
$$


Then there exists an exact matrix


$$
\widehat F\in R^{3\times163}
$$


such that


$$
\widehat FL=0,\qquad
\widehat FS=I_3,
\qquad
\widehat F\equiv F\pmod{2^{351}}.
$$


Moreover,


$$
\ker\widehat F
=
\operatorname{span}_{\mathbb Q}(L)\cap R^{163},
$$


so the columns of $S$ give an exact basis of the saturated quotient.

#### Proof

Split the relation matrix and the modular covectors according to the first three and last 160 polynomial coefficients:


$$
L=\begin{pmatrix}L_0\\H\end{pmatrix},
\qquad
F=(F_0\;\;F_H).
$$



Define


$$
F^\ast=(F_0\;\;-F_0L_0H^{-1}).
$$


Then


$$
F^\ast L=0
$$


exactly.

Because $H$ is integral,


$$
H^{-1}=\frac{\operatorname{adj}(H)}{\det H}
$$


has entries of valuation at least $-161$. Therefore


$$
F^\ast-F
=
\bigl(0\;\;-(FL)H^{-1}\bigr)
\in2^{351}R^{3\times163}.
$$


In particular, $F^\ast$ is $2$-integral.

Now put


$$
M=F^\ast S.
$$


The modular dual-basis identity and the preceding estimate imply


$$
M\equiv I_3\pmod{2^{351}}.
$$


Thus $M\in\mathrm{GL}_3(R)$. Define


$$
\widehat F=M^{-1}F^\ast.
$$


It follows that


$$
\widehat FL=0,\qquad \widehat FS=I_3,
\qquad
\widehat F-F\in2^{351}R^{3\times163}.
$$



The map $\widehat F:R^{163}\to R^3$ is surjective. Its kernel has rank $160$ and contains the columns of $L$. Over $\mathbb Q$, it therefore equals their span. Intersecting with $R^{163}$ gives the asserted saturated kernel.

The exact identity $\widehat FS=I_3$ then identifies the saturated quotient with $R^3$. ∎

### Consequence

The moment functional annihilates this exact kernel. Indeed, if


$$
P\in\operatorname{span}_{\mathbb Q}(L)\cap R^{163},
$$


some nonzero integer multiple of $P$ is an exact linear combination of telescoping relations. Torsion-freeness of the target $R$ gives


$$
\mathscr L(P)=0.
$$



This is the required passage from finite modular annihilation to exact observable identities.

---

## 4. Payload contents and the precise division guard

Let


$$
P_f=U_f^2,\qquad P_m=U_fU_e,
$$


padded to degree $162$, and let


$$
c_f=\widehat F P_f,\qquad c_m=\widehat F P_m
$$


be their exact quotient coordinates.

These coordinates lie in $R$; they need not be ordinary integers. Their $2$-adic contents are nevertheless well defined.

The computed modular coordinates satisfy


$$
c_f\equiv c_f^{\rm comp}\pmod{2^{351}},
\qquad
c_m\equiv c_m^{\rm comp}\pmod{2^{351}}.
$$


Since the reported minima $157,154$ are strictly below $351$, they are the exact minima for these exact coordinates:


$$
\min_i v_2(c_{f,i})=157,\qquad
\min_i v_2(c_{m,i})=154.
$$



The exact observable identities are


$$
D_f^2\widetilde D=\sum_i c_{f,i}\mathscr L(S_i),
$$




$$
D_fD_e\widetilde E=\sum_i c_{m,i}\mathscr L(S_i).
$$



Write


$$
D_f=2^{80}d_f,\qquad D_e=2^{77}d_e,
$$


with $d_f,d_e$ odd. Dividing the exact coordinate contents gives


$$
\boxed{
\sum_i\frac{c_{f,i}}{2^{157}}\mathscr L(S_i)
=
8d_f^2\widetilde D,
}
$$




$$
\boxed{
\sum_i\frac{c_{m,i}}{2^{154}}\mathscr L(S_i)
=
8d_fd_e\widetilde E.
}
$$



### The guard that must be checked

After dividing by $2^{157}$ or $2^{154}$, the certified coordinate precision is at least


$$
351-157=194,\qquad351-154=197
$$


bits.

Thus the specific required checks are


$$
351\ge157+23=180,
\qquad
351\ge154+23=177.
$$



They hold with ample margin.

The producer’s generic comparison


$$
\texttt{needed}\le\texttt{certified}
$$


would not by itself be sufficient for arbitrary larger contents: one must account for the content division. For the actual reported values, the stronger correct inequalities hold, so no repair of the resulting 23-bit payloads is necessary.

### Compiled integer payloads

Define


$$
\beta_{f,i}=
\left(\frac{c_{f,i}^{\rm comp}}{2^{157}}\bmod2^{23}\right),
\qquad
\beta_{m,i}=
\left(\frac{c_{m,i}^{\rm comp}}{2^{154}}\bmod2^{23}\right),
$$


and


$$
Q_f(j)=\sum_i\beta_{f,i}S_i(j),\qquad
Q_m(j)=\sum_i\beta_{m,i}S_i(j).
$$



Then $Q_f,Q_m$ are integer polynomials of degree at most $162$, and


$$
\mathscr L(Q_f)\equiv8d_f^2\widetilde D\pmod{2^{23}},
$$




$$
\mathscr L(Q_m)\equiv8d_fd_e\widetilde E\pmod{2^{23}}.
$$



Therefore


$$
\boxed{
D_{\rm raw}\equiv
d_f^{-2}\frac{\mathscr L(Q_f)}8\pmod{2^{20}},
}
$$




$$
\boxed{
E_{\rm raw}\equiv
(d_fd_e)^{-1}\frac{\mathscr L(Q_m)}8\pmod{2^{20}}.
}
$$



The division by $8$ is justified by the exact lifted identities. It is not inversion of a nonunit modulo $2^{23}$.

---

# Part II. Audit of the binary transport

## 5. Negative odd factorials: the exact statement

For nonnegative integers,


$$
g(h)=\prod_{r=1}^{h}(2r-1),\qquad g(0)=1.
$$


The recurrence


$$
g(h+1)=(2h+1)g(h)
$$


extends this uniquely to all integers as an odd $2$-local unit. Explicitly,


$$
g(-m)=\frac{(-1)^m}{(2m-1)!!},\qquad m\ge1.
$$



Thus negative values generally belong to


$$
\mathbb Z_{(2)}^\times,
$$


not to $\mathbb Z$.

The turn-2 Newton bound


$$
v_2(\gamma_r)\ge\lceil r/2\rceil
$$


implies that


$$
g_p(h)=\sum_{r=0}^{2p-2}\gamma_r\binom hr
$$


represents $g(h)$ modulo $2^p$ on nonnegative integers.

To extend this conclusion to negative integers, consider


$$
R_p(h)=g_p(h+1)-(2h+1)g_p(h).
$$


This is an integer-valued polynomial that vanishes modulo $2^p$ at every nonnegative integer. Its Newton coefficients, being forward differences at zero, are all divisible by $2^p$. Hence


$$
R_p(h)\equiv0\pmod{2^p}
$$


for every integer $h$.

Also $g_p(h)\equiv1\pmod2$ on all integers. The recurrence can therefore be run backwards using only odd inverses. This proves that the same polynomial represents the negative extension.

No negative factorial is defined or needed.

---

## 6. Reciprocal closure and valuation layers

Modulo $2^p$, the odd-factorial approximation admits layers


$$
g(h)=\sum_{\nu=0}^{p-1}2^\nu G_\nu(h),
\qquad
G_\nu\in\operatorname{Int}_{\le2\nu}(\mathbb Z).
$$



The following operations preserve the degree-by-valuation bound:

- integer translation and reflection;
- finite products;
- reciprocals of these odd-unit functions;
- positive and negative integral powers.

For reciprocals, write $g=1+H$, where $H$ begins in valuation layer one. Then


$$
g^{-1}\equiv\sum_{r=0}^{p-1}(-H)^r\pmod{2^p}.
$$


A product contributing to valuation layer $\nu$ has degree at most $2\nu$.

This argument takes place in the ring of integer-valued polynomial functions modulo $2^p$. It introduces no division by $r!$, and no loss of precision from an even inverse.

The classical odd-factorial and Newton machinery is reused here; the target-specific assertion is its closure for the exact correction factors and observable transport.

---

## 7. The factorial power on every reachable prefix

Let $L=2^{t+1}$, and write the residues of $b,c,S=c+b$ modulo $L$ as


$$
b_0,\ c_0,\ S_0.
$$


Set


$$
\kappa=\left\lfloor\frac{b_0+c_0}{L}\right\rfloor\in\{0,1\}.
$$



For a selected lower prefix $r\in[0,L-1]$,


$$
\lambda_b=\mathbf1_{r>b_0},\qquad
\lambda_S=\mathbf1_{r>S_0}.
$$



If $\kappa=0$, then $S_0=b_0+c_0\ge b_0$, so


$$
\lambda_b\ge\lambda_S,
\qquad
\kappa+\lambda_b-\lambda_S\in\{0,1\}.
$$



If $\kappa=1$, then


$$
S_0=b_0+c_0-L<b_0,
$$


so


$$
\lambda_b\le\lambda_S,
\qquad
\kappa+\lambda_b-\lambda_S\in\{0,1\}.
$$



Adding $\lambda_N\in\{0,1\}$ proves


$$
\boxed{
d_t=\kappa_{t+1}+\lambda_N'+\lambda_b'-\lambda_S'
\in\{0,1,2\}
}
$$


for **every reachable prefix**.

This proof does not assume that the prefix has a valid completion in $0\le j\le b$. Hence polynomial interpolation at temporarily invalid arguments cannot create a negative valuation shift.

---

## 8. Why invalid intermediate arguments are harmless

The factorial-ratio identity is used as an exact factorial identity only along accepted paths, where all original factorial arguments are nonnegative.

For polynomial interpolation and state construction, the odd correction factor is extended to all integer arguments using the odd-unit extension of $g$. This provides an everywhere-defined modular function. It is not an assertion that a factorial with a negative argument exists.

A path that cannot complete to a valid $j$ may still be transported formally. It contributes nothing to the terminal accepted state.

At the end of 71 digits, all fixed constants have been consumed and the remaining variable is zero. The terminal conditions are


$$
\lambda_b=0\iff j\le b,
$$


and, because $b<N,S$,


$$
j\le b\implies\lambda_N=\lambda_S=0.
$$


Thus acceptance of precisely


$$
\boxed{(0,0,0)}
$$


is equivalent to the original finite cutoff.

Merging prefixes with identical borrow flags is valid because their remaining factorial ratio and their future flag transitions depend only on those flags, the remaining fixed digits, and the remaining variable.

---

## 9. Degree bounds at the new precision

The section identity remains


$$
\binom{2h+\epsilon}{r}
=
\sum_u C_\epsilon(r,u)\binom hu,
$$


with


$$
v_2(C_\epsilon(r,u))\ge\max(0,2u-r).
$$



Combining this with the correction-factor layers and $d_t\ge0$ proves


$$
\deg P_{t,\lambda,\nu}
\le
\left\lfloor\frac D{2^t}\right\rfloor+2\nu.
$$



For both compiled payloads,


$$
D\le162,\qquad p=23.
$$


Therefore a sufficient degree envelope is


$$
\boxed{
B_t=\left\lfloor\frac{162}{2^t}\right\rfloor+44.
}
$$



In particular:

- at most four borrow states occur;
- the uniform envelope is degree $206$;
- after eight digits the degree is at most $44$;
- stable storage is at most $4\cdot45=180$ residues per observable.

A conservative unreduced product-degree bound is


$$
B_t+44\le250.
$$



### Implementation obligations, not an implementation verdict

A personally authored implementation should still verify:

1. only actual reachable masks are merged;
2. every transition has $d_t\in\{0,1,2\}$;
3. correction factors are inverted only as odd units;
4. Newton coefficients beyond the proved degree envelope vanish before truncation;
5. all 71 digits are consumed;
6. only terminal state $000$ is accepted.

These statements establish the mathematical specification. They do not certify code that has not yet produced a reported result.

---

# Part III. A new original-phase norm identity

## 10. The phase used in the proof

The actual parameters satisfy


$$
\boxed{
b\equiv \texttt{0x6d1}\pmod{2^{12}},
\qquad
n\equiv \texttt{0xf42}\pmod{2^{12}}.
}
$$


The second congruence follows from $n=4002b$ and the first.

In particular,


$$
b\bmod256=209,\qquad
N\bmod256=68,\qquad
(a+80)\bmod256=212.
$$



The following kernel lemma is a family statement at this explicitly stated phase. It does not require the actual numerator coefficients.

### Lemma 2 — An even kernel lattice with eight-divisible column sums

Let


$$
m=a+81,
$$


and, for $0\le r\le81$, define on the original range


$$
h_r(j)=
\binom Nj
\binom{m+b-j-r-1}{b-j-r},
$$


with the second factor zero when $b-j-r<0$.

Under the displayed phase congruences,


$$
\boxed{2\mid h_r(j)\quad\text{for every }j,r,}
$$


and


$$
\boxed{
8\mid\sum_{j=0}^{b}h_r(j)\quad\text{for every }r.
}
$$



#### Proof of the row divisibility

If $\binom Nj$ is even, there is nothing to prove.

If it is odd, Lucas’ criterion forces the low byte of $j$ to be a submask of


$$
N\bmod256=\texttt{0x44}.
$$


Thus


$$
j\bmod256\in\{0,4,64,68\}.
$$



For $0\le r\le81$,


$$
(b-r)\bmod256=209-r\in[128,209].
$$


Subtracting the possible low byte of $j$ incurs no borrow into bit eight. Consequently the low byte of $b-j-r$ lies in


$$
[60,209].
$$



Oddness of the second binomial would require


$$
(b-j-r)\mathbin{\&}(m-1)=0.
$$


But


$$
(m-1)\bmod256=212=\texttt{0xd4}.
$$


A byte disjoint from $\texttt{0xd4}$ is at most its complementary mask


$$
\texttt{0x2b}=43.
$$


This contradicts the lower bound $60$. Therefore the second binomial is even. ∎

#### Proof of the column-sum divisibility

The complete finite convolution is


$$
\sum_{j=0}^{b}h_r(j)
=
[z^{b-r}]
\frac{(1+z)^N}{(1-z)^m}.
$$



Since $4\mid N$,


$$
(1+z)^N\equiv(1-z)^N\pmod8.
$$


Indeed, with $t=z/(1-z)$,


$$
\left(\frac{1+z}{1-z}\right)^N=(1+2t)^N,
$$


whose linear and quadratic nonconstant terms are divisible by $8$, as are all terms of degree at least three.

Hence


$$
\sum_{j=0}^{b}h_r(j)
\equiv
\binom{n+78+b-r}{b-r}\pmod8.
$$



Now


$$
(n+78)\bmod2^{12}=\texttt{0xf90},
$$


and


$$
(b-r)\bmod2^{12}\in[\texttt{0x680},\texttt{0x6d1}].
$$


In adding these two lower indices:

- bit $9$ has two ones and forces a carry;
- bit $10$ has two ones and forces another carry;
- bit $11$ has a one from $n+78$ and the incoming carry, forcing a third.

Kummer’s theorem therefore makes this binomial divisible by $8$. ∎

### A genuine family norm consequence

For any integer polynomial


$$
B(z)=\sum_{r=0}^{81}B_rz^r,
$$


put


$$
Z_j=\binom Nj[z^{b-j}]\frac{B(z)}{(1-z)^{a+81}}.
$$


Lemma 2 gives


$$
Z_j\in2\mathbb Z,\qquad
\sum_jZ_j\in8\mathbb Z.
$$



For an even integer $x$,


$$
x^2\equiv2x\pmod8.
$$


Therefore


$$
\boxed{
\sum_{j=0}^{b}Z_j^2\equiv0\pmod8.
}
\tag{10.1}
$$



This is an original-phase kernel norm identity, valid for every numerator of degree at most $81$ under the explicit phase hypotheses. It is not a proposed evaluator and does not depend on a finite Gram experiment.

---

## 11. The complete columns have a common factor four

Reuse the accepted parity masks


$$
A_f(z)\equiv z^3(1+z)^{78}\pmod2,
\qquad
A_e(z)\equiv(1+z)^{77}\pmod2.
$$



Choose the convenient integral parity lifts


$$
A_f^{(0)}(z)=z^3(1-z)^{78},
\qquad
A_e^{(0)}(z)=(1-z)^{77}.
$$


Their reconstructed series are


$$
F^{(0)}(z)=\frac{z^3}{(1-z)^{a+3}},
\qquad
E^{(0)}(z)=\frac1{(1-z)^a}.
$$



Define their weighted rows by


$$
X_j^{(0)}
=
\binom Nj\binom{a+b-j-1}{b-j-3},
$$




$$
Y_j^{(0)}
=
\binom Nj\binom{a+b-j-1}{b-j}.
$$



### Lemma 3 — Both parity-lift columns are divisible by four

For every original row,


$$
4\mid X_j^{(0)},\qquad4\mid Y_j^{(0)}.
$$



#### Proof

We use


$$
N\equiv4\pmod8,\qquad a\equiv4\pmod8,\qquad b\equiv1\pmod8.
$$



If $j$ is odd, subtracting $j$ from $N$ produces borrows at bits zero and one. Thus


$$
4\mid\binom Nj.
$$



Suppose $j$ is even.

For $Y_j^{(0)}$, the other binomial counts carries in adding


$$
a-1\quad\text{and}\quad b-j.
$$


The latter is odd, while $a-1$ has both low bits set. A carry at bit zero forces another at bit one.

For $X_j^{(0)}$, write


$$
K=b-3\equiv6\pmod8.
$$


The other binomial counts carries in adding


$$
a+2\equiv6\pmod8
\quad\text{and}\quad K-j.
$$



If bit one of $j$ is zero, the addition has carries at bits one and two.

If bit one of $j$ is one, the weight subtraction already borrows at bit one. At bit two:

- if bit two of $j$ is one, the weight subtraction borrows again;
- if bit two of $j$ is zero, the other binomial has a carry at bit two.

In every case the product has at least two factors of $2$. Unsupported negative lower indices contribute zero. ∎

Now write


$$
A_f=A_f^{(0)}+2B_f,
\qquad \deg B_f\le81.
$$


The difference in weighted columns is


$$
X-X^{(0)}=2Z_f
$$


for a vector $Z_f$ from Lemma 2. Since $Z_f$ is even,


$$
4\mid X_j.
$$



For the second column, first put it over the same denominator:


$$
E(z)=\frac{(1-z)^4A_e(z)}{(1-z)^{a+81}}.
$$


The numerator has degree at most $81$, and


$$
(1-z)^4A_e(z)-(1-z)^{81}
$$


is coefficientwise even. Thus


$$
Y-Y^{(0)}=2Z_e
$$


with another vector $Z_e$ from Lemma 2. Consequently,


$$
\boxed{
4\mid X_j,\qquad4\mid Y_j\qquad(0\le j\le b).
}
\tag{11.1}
$$



This improves the turn-2 lower bounds on the binary column contents from one to two:


$$
\boxed{a_{\rm cont}\ge2,\qquad c_{\rm cont}\ge2.}
$$



It does not identify their exact contents.

---

## 12. Eight-divisible sums of the complete columns

For the first parity lift,


$$
\sum_jX_j^{(0)}
=
[z^{b-3}]
\frac{(1+z)^N}{(1-z)^{a+3}}
\equiv
\binom{n+b-3}{b-3}\pmod8.
$$



Here


$$
n\equiv2\pmod{16},\qquad b-3\equiv14\pmod{16}.
$$


Adding $n$ and $b-3$ forces carries at bits one, two, and three. Therefore


$$
8\mid\sum_jX_j^{(0)}.
$$



Similarly,


$$
\sum_jY_j^{(0)}
=
[z^b]\frac{(1+z)^N}{(1-z)^a}
\equiv
\binom{n+b-3}{b}\pmod8.
$$


Since $n-3$ has its three lowest bits set and $b$ is odd, adding $n-3$ and $b$ forces at least three carries. Hence


$$
8\mid\sum_jY_j^{(0)}.
$$



The perturbations $2Z_f,2Z_e$ have sums divisible by $16$, by Lemma 2. We have proved


$$
\boxed{
8\mid\sum_{j=0}^{b}X_j,\qquad
8\mid\sum_{j=0}^{b}Y_j.
}
\tag{12.1}
$$



These sums are proof devices for the signed-row-equivalent columns. They do not replace the physical columns, modify their forcing, or change the norm and mixed forms.

---

## 13. The new norm law

### Theorem 4 — Original-phase two-column norm congruence

Under the phase and parity hypotheses used above,


$$
\boxed{
\sum_{j=0}^{b}(sX_j+tY_j)^2\equiv0\pmod{32}
\qquad(s,t\in\mathbb Z).
}
$$



In particular,


$$
\boxed{
32\mid\widetilde D,\qquad
16\mid\widetilde E,
}
$$


and therefore


$$
\boxed{
32\mid D_{\rm raw},\qquad
16\mid E_{\rm raw}.
}
$$



#### Proof

Every coordinate of


$$
V=sX+tY
$$


is divisible by $4$, and its coordinate sum is divisible by $8$.

For $x\in4\mathbb Z$,


$$
x^2\equiv4x\pmod{32}.
$$


Thus


$$
\sum_jV_j^2
\equiv4\sum_jV_j
\equiv0\pmod{32}.
$$



Taking $V=X$ proves the norm statement. Taking $V=X+Y$ and subtracting the individual norm congruences gives


$$
2\sum_jX_jY_j\equiv0\pmod{32},
$$


hence the mixed divisibility by $16$. The physical congruences follow because the integer lifts agree with the actual contractions modulo $2^{20}$. ∎

### What cancellation has actually been characterized?

The proof establishes


$$
\boxed{
\sum_j(X_j/4)^2\equiv0\pmod2.
}
$$


This is a systematic cancellation at the **proved fixed normalization $4$**.

If the actual first-column content is exactly $4$, then its primitive vector has even norm, so its primitive norm loss is at least one. If the actual content is larger, that conclusion about the primitive vector does not follow.

Accordingly:

- a fixed-normalization norm cancellation is proved;
- exact column content is not proved;
- exact primitive norm loss is not proved;
- no upper bound on $v_2(D_{\rm raw})$ is obtained.

### Relation to the exact transport

At the first binary layer, squaring acts as the identity on residues modulo $2$. After the proved factor $4$ is removed,


$$
\sum_j(X_j/4)^2\bmod2
=
\sum_jX_j/4\bmod2.
$$


The right side is evaluated symbolically through the complete finite convolution, and the carry arguments above force it to vanish.

Thus the vanishing is a structural statement about the lowest surviving valuation layer of the actual transport. It is not an extrapolation from an auxiliary zero Gram.

### Family scope

The kernel norm identity (10.1) holds throughout the explicit phase


$$
b\equiv\texttt{0x6d1}\pmod{2^{12}},\qquad n=4002b.
$$


The stronger two-column theorem additionally requires the degree bounds and the two parity masks for the complete reconstructed columns.

Those hypotheses are supplied for the fixed original binary index. The present sources do not prove that they persist for every original $u$. I therefore make no such extension.

---

# Part IV. Consequences for the pending contraction and the global objective

## 14. Stronger checks for the 23-bit payload contraction

Let


$$
C_f=\mathscr L(Q_f)\pmod{2^{23}},
\qquad
C_m=\mathscr L(Q_m)\pmod{2^{23}}.
$$


The exact normalization identities and Theorem 4 imply


$$
\boxed{C_f\equiv0\pmod{2^8},}
$$




$$
\boxed{C_m\equiv0\pmod{2^7}.}
$$



These replace the weaker divisibility checks available in turn 2.

If the contraction returns a nonzero norm residue, then


$$
v_2(D_{\rm raw})=v_2(C_f)-3<20.
$$


The analogous statement holds for the mixed form:


$$
v_2(E_{\rm raw})=v_2(C_m)-3<20
$$


when its normalized residue is nonzero.

If the normalized norm vanishes modulo $2^{20}$, the only conclusion is


$$
v_2(D_{\rm raw})\ge20.
$$


The new theorem does not turn that lower bound into an exact depth.

---

## 15. Physical precision and the complete logarithmic guard

The physical input remains twenty-bit data. The 23-bit kernel calculation does not create higher-precision physical forcing.

Writing


$$
d_0=v_2(D_{\rm raw}),\qquad
e_0=v_2(E_{\rm raw}),
$$


the retained ratio


$$
\frac{E_{\rm raw}}{2D_{\rm raw}}
$$


requires, for $s$ reliable $2$-adic bits,


$$
M_E\ge s+d_0+1,
\qquad
M_D\ge s+2d_0+1-e_0.
$$



The new lower bounds are


$$
d_0\ge5,\qquad e_0\ge4.
$$


They do not by themselves verify a desired ratio precision.

The complete logarithmic omission condition remains


$$
K_{\rm norm}+a_{\rm cont}-d_0-1\ge s,
$$


with the accepted


$$
K_{\rm norm}\ge2000b-138.
$$



We may now use $a_{\rm cont}\ge2$, but we still need an actual upper bound on $d_0$. A nonzero twenty-bit norm residue would provide such a bound. A zero residue would not.

No source rows, exterior terms, or terminal returns are removed by this argument.

---

## 16. The exact bounded calculation still needed

No accepted Smith, payload, head, Schur, contact, conversion, or endpoint computation should be rerun.

The coordinator is already authoring the new contraction. Its mathematical inputs and expected verifiable outputs are now precise.

### Inputs

1. The exact original $b,n$.
2. The three certified integer generator representatives $S_i$, or their reductions modulo $2^{23}$ for evaluation.
3. The six normalized coordinate residues
   

$$
c_{f,i}/2^{157}\pmod{2^{23}},
   \qquad
   c_{m,i}/2^{154}\pmod{2^{23}}.
$$


4. The odd units
   

$$
d_f=D_f/2^{80},\qquad d_e=D_e/2^{77}\pmod{2^{20}}.
$$


5. The exact finite summand $T(j)$ and the audited 71-digit transport.

The compact basis-and-payload file is sufficient for the contraction. The retained large operation artifact supports the already reported finite saturation calculation; it need not be regenerated.

### Outputs

The new computation should return


$$
C_f,\ C_m\pmod{2^{23}},
$$


then


$$
D_{\rm raw},\ E_{\rm raw}\pmod{2^{20}}.
$$



Its receipt should record:

- both compiled payload degrees at most $162$;
- 71 consumed digits;
- at most four reachable borrow masks at each digit;
- nonnegative digit powers $d_t\in\{0,1,2\}$;
- the degree-by-valuation checks;
- terminal acceptance only at $000$;
- $C_f\equiv0\pmod{256}$;
- $C_m\equiv0\pmod{128}$;
- exact valuations only when the corresponding normalized residue is nonzero.

This is a specification for the calculation already in progress, not a report that it has succeeded.

---

## 17. All-prime normalization and the whole error remain separate

The local norm congruence does not determine the least actual two-column clearer, the actual row contents at odd primes, or the final all-prime gcd.

Retain


$$
A_B=N_{B,1}^{T}\Omega N_{B,1},
\qquad
H_B=N_{B,1}^{T}\Omega N_{B,2},
$$




$$
\boxed{
g_B=\gcd(A_B,|H_B|),
\qquad
q_n=\frac{A_B}{g_B},
\qquad
p_n=\frac{H_B}{g_B}.
}
$$



If $d_B$ is the least actual common clearer, the primitive multiplier remains


$$
\frac{d_B^2}{g_B}.
$$



No row content is divided out in the present contractions. A local binary calculation cannot replace the final gcd by a selected-prime part.

The real approximation quantity remains the **whole same-index form**


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n.
}
$$



Even conditional on the previously stated complete signed-error asymptotic, an irrationality proof still requires an infinite original subsequence for which the actual primitive denominator yields


$$
0<|q_n(e+\pi)-p_n|\longrightarrow0.
$$



Neither the newly proved norm congruence nor one completed original binary contraction would establish that infinite all-prime comparison.

The reviewed $n=3375$ whole-form enclosures remain finite results for their five stated probes. They are not rerun or extended here.

---

## 18. Proof-status ledger

| Statement | Status |
|---|---|
| Single $163\times160$ zero-flux presentation | Exact mathematical setup |
| Reported Smith data $80,80,157,8$ | Audited supplied finite certificate; not regenerated |
| Exact kernel lift with loss at most $161$ bits | **Proved** |
| Exact dual normalization and saturated quotient | **Proved** |
| Contents $157,154$ survive exact lifting | **Proved from the reported coordinate data** |
| Both compiled payloads need only 23 kernel bits | **Proved**, with the content-division guard made explicit |
| Negative odd-factorial extension and reciprocal closure | **Audited and clarified** |
| $d_t\ge0$ on every reachable prefix | **Proved**, including invalid-completion prefixes |
| Exact original cutoff at terminal $000$ | **Proved** |
| Degree envelope $162/2^t+44$ at precision 23 | **Proved** |
| Original-phase kernel norm divisible by $8$ | **New symbolic theorem** |
| Both complete original columns divisible by $4$ | **New proof using the accepted parity masks** |
| $32\mid D_{\rm raw}$, $16\mid E_{\rm raw}$ | **New original-phase norm theorem** |
| Exact column contents and primitive norm loss | Open |
| Original 23-bit payload contractions | In progress; **no result reported here** |
| All-prime primitive denominator versus whole error | Open |
| Irrationality or rationality of $e+\pi$ | Unresolved |

---

## Conclusion

The saturated-observable justification is valid after making the exact lift and dual normalization explicit. The resulting compiled payloads really do reduce both outstanding contractions to


$$
\boxed{23\text{ kernel bits, followed by an exact division by }8.}
$$



The transport’s potentially delicate points—negative arguments, temporarily invalid prefixes, valuation shifts, finite cutoff, degree layers, and odd reciprocals—have now been addressed without claiming that an unreported implementation is already correct.

The new arithmetic result is


$$
\boxed{
X,Y\in4\mathbb Z^{b+1},
\qquad
\sum_j(sX_j+tY_j)^2\equiv0\pmod{32}.
}
$$


In particular,


$$
\boxed{
v_2(D_{\rm raw})\ge5,\qquad
v_2(E_{\rm raw})\ge4.
}
$$



This is genuine original-phase norm information, obtained from the complete short-column structure and exact finite convolution. It is not an exact norm-depth result and supplies no primitive-content upper bound.

The immediate local bottleneck is the already planned bounded contraction: it must return the actual residues before an upper norm-depth bound or a norm-relative precision conclusion can be asserted.

The global bottleneck remains


$$
\boxed{
\text{all-prime control of the actual primitive denominator against the
whole same-index nonzero error on an infinite original sequence}.
}
$$



Accordingly, the attached method still gives neither an unconditional proof nor a disproof of irrationality of $e+\pi$.
