> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, turn 4 — A depth-eight kernel lattice, a depth-twenty Gram theorem, and a safe higher-precision contract

## Executive conclusion

The two accepted contractions now establish


$$
D_{\rm raw}\equiv E_{\rm raw}\equiv0\pmod{2^{20}},
$$


and establish **only**


$$
v_2(D_{\rm raw}),\ v_2(E_{\rm raw})\ge20.
$$


The compiled-payload cross-check correctly includes the content-division guards $194,197$. It uses a different payload normalization, but the same transport routine; it is not an independently implemented transport. The 102 direct small-binomial comparisons, including 91 nonzero comparisons, remain finite corroboration at their stated inputs.

The mathematical advance below explains both original weighted zeros without evaluating either Gram sum again.

For the exact degree-$81$ kernel


$$
h_r(j)=
\binom Nj
\binom{a+80+b-j-r}{b-j-r},
\qquad
0\le r\le81,\quad 0\le j\le b,
$$


with unsupported lower indices interpreted as zero, I prove


$$
\boxed{\min_{r,j}v_2(h_r(j))=8.}
$$


Thus the arbitrary-numerator kernel lattice really is substantially deeper than the turn-3 argument detected.

More importantly, its shallowest rows occur in four-element sets obtained by toggling binary positions $38$ and $41$. On each such set, the entire kernel row is proportional, to sufficient precision, by a common odd scalar. This gives


$$
\boxed{
2^{18}\mid\sum_{j=0}^{b}Z_jZ'_j
}
$$


for **every two** integer-numerator vectors in this degree-$81$ kernel lattice.

For the two accepted complete physical columns, the parity lifts have stronger contents:


$$
2^{11}\mid X_j^{(0)},\qquad 2^{10}\mid Y_j^{(0)}.
$$


Combining these facts yields


$$
\boxed{
2^9\mid X_j,\ Y_j\quad(0\le j\le b),
}
$$


and, crucially,


$$
\boxed{
2^{20}\mid\sum_{j=0}^{b}X_j^2,\qquad
2^{20}\mid\sum_{j=0}^{b}X_jY_j.
}
$$


This is a structural explanation of **both** accepted twenty-bit zeros. It distinguishes pointwise content $2^9$ from the additional Gram cancellation. It does **not** prove that either column has exact content $2^9$, or that either Gram depth is exactly $20$.

I also derive a four-parity test per column which decides, from the existing short numerators modulo $4$, whether its content is exactly $2^9$ or at least $2^{10}$. This is new, tiny numerator post-processing—not a rerun of an accepted producer or contraction.

For the proposed new physical precision $32$, the conservative dimensions


$$
\boxed{
m=124,\quad T=36,\quad I=72,\quad R=160,\quad L_0=284,\quad K_0=196
}
$$


are justified below. All physical stages can be performed at 32 bits when their integral normalizations and unit inverses are retained. The twenty-bit $n$-branch disappearance and the $44/48$ polynomial factors cannot be silently promoted to 32 bits. I specify the exact new checks and a factor-independent normalization available if the new reconstructed $n$-branches vanish.

The all-prime actual denominator and the whole same-index error remain open.

---

# 1. Accepted finite data and scope

Retain exactly


$$
b=150094635296999121=9^{18},\qquad
n=4002b=600678730458590482242,
$$




$$
N=n+2,\qquad a=2n.
$$



The physical row domain is still


$$
\boxed{0\le j\le b.}
$$



At physical precision $2^{20}$, the accepted complete reconstructed columns have the representations


$$
F(z)=\frac{A_f(z)}{(1-z)^{a+81}},
\qquad
E(z)=\frac{A_e(z)}{(1-z)^{a+77}},
$$


with degrees $81,77$, and


$$
A_f\equiv z^3(1-z)^{78}\pmod2,
\qquad
A_e\equiv(1-z)^{77}\pmod2.
$$



The second column already includes the retained second force, finite return, terminal factorial cancellation and exterior $+1$. Nothing is added again.

For integer lifts of these numerators, define


$$
X_j=\binom Nj[z^{b-j}]F(z),\qquad
Y_j=\binom Nj[z^{b-j}]E(z).
$$


The common physical row signs do not affect contents, norms or mixed products. The lifted contractions agree with the actual retained contractions modulo $2^{20}$.

### What the new receipts establish

The fixed-divisor contraction reports:

- physical precision $20$;
- effective kernel precisions $34,36$, with a shared 36-bit transport;
- 71 consumed digits;
- terminal acceptance only at $000$;
- the complete original finite cutoff and exterior retained;
- both normalized Gram residues zero modulo $2^{20}$.

The compiled-payload cross-check reports:

- kernel precision $23$;
- post-content coordinate guards $194,197$;
- 71 consumed digits;
- both compiled observables zero modulo $2^{23}$;
- agreement with the distinct fixed-divisor payload evaluation.

The source explicitly checks


$$
\text{content}+23\le351.
$$


That is the correct guard. The exact lift and dual normalization from turn 3 need not be reopened.

Neither receipt evaluates an all-prime gcd or determines an exact norm depth. No accepted computation is proposed for rerunning here.

---

# Part I. The original degree-$81$ kernel is much deeper

## 2. Exact kernel and carry states

Put


$$
C=a+80,\qquad B_r=b-r.
$$


Then


$$
h_r(j)=\binom Nj\binom{C+B_r-j}{B_r-j}.
$$



For a supported row, write


$$
k=B_r-j\ge0.
$$


Kummer’s theorem gives


$$
v_2(h_r(j))
=
\#\{\text{borrows in }N-j\}
+
\#\{\text{carries in }C+k\}.
\tag{2.1}
$$



At a modulus $2^t$, let the selected lower prefix of $j$ be $q$, and define


$$
\lambda_N=\mathbf1_{q>N\bmod2^t},
\quad
\lambda_B=\mathbf1_{q>B_r\bmod2^t},
\quad
\lambda_S=\mathbf1_{q>(C+B_r)\bmod2^t}.
$$


Also put


$$
\kappa_t=
\left\lfloor
\frac{(C\bmod2^t)+(B_r\bmod2^t)}{2^t}
\right\rfloor.
$$



The contribution to (2.1) at this scale is


$$
\boxed{
d_t=\kappa_t+\lambda_N+\lambda_B-\lambda_S.
}
\tag{2.2}
$$


As in the accepted transport proof, this lies in $\{0,1,2\}$ on every reachable prefix.

Encode the flag triple by


$$
x=4\lambda_N+2\lambda_B+\lambda_S.
$$


Define


$$
f(x)=\lambda_N+\lambda_B-\lambda_S.
$$


For masks $0,\ldots,7$,


$$
f=(0,-1,1,0,1,0,2,1).
$$



If the next fixed bits of $N,B_r,S_r=C+B_r$ form the mask $v$, put


$$
z=7-v.
$$


The two possible next states are


$$
x\mathbin{\&}z,\qquad x\mathbin{|}z,
$$


and the edge entering state $y$ has cost


$$
\kappa_{t+1}+f(y).
\tag{2.3}
$$



This is an exact min-plus version of the established carry transport. It computes a pointwise valuation minimum, not a Gram sum.

---

## 3. All 82 shifts have the same upper carry problem

For $0\le r\le81$,


$$
B_r\bmod256=209-r\in[128,209].
$$


Also


$$
N\bmod256=68,\qquad C\bmod256=212,
$$


and


$$
S_r\bmod256=165-r\in[84,165].
$$



Consequently,


$$
68<S_r\bmod256<B_r\bmod256,
\qquad \kappa_8=1.
$$


The four possible masks after the first eight bits are therefore


$$
\boxed{0,\ 4,\ 5,\ 7.}
\tag{3.1}
$$



Most importantly, subtracting $r\le81$ changes none of the bits above position $7$. The upper carry problem is identical for every shift.

The bytes, from the most significant end, are


$$
\begin{array}{c|c}
N&\texttt{20 90 17 8a d1 dc e6 0f 44}\\
b&\texttt{00 02 15 3e 46 8b 91 c6 d1}\\
C&\texttt{41 20 2f 15 a3 b9 cc 1e d4}\\
C+b&\texttt{41 22 44 53 ea 45 5d e5 a5}.
\end{array}
\tag{3.2}
$$



Thus above the low byte, the inputs are fixed for the entire degree-$81$ family.

### Exact upper min-plus certificate

Initialize all four masks in (3.1) at cost zero. Apply (2.3) from bit $8$ upward. The following are exact small min-plus products; they are not physical Gram evaluations.



$$
\begin{array}{c|l}
\text{number of consumed bits }t&
\text{minimum costs by reachable mask}\\ \hline
8&0:0,\ 4:0,\ 5:0,\ 7:0\\
16&0:0,\ 4:1,\ 6:7,\ 7:3\\
24&0:1,\ 1:0,\ 3:1,\ 7:5\\
32&0:3,\ 1:2,\ 3:3,\ 7:7\\
38&0:4,\ 2:5,\ 6:6,\ 7:5\\
41&0:4,\ 2:6,\ 6:6,\ 7:8\\
48&0:7,\ 2:10,\ 3:7,\ 7:9\\
52&0:9,\ 1:7,\ 3:10,\ 7:9\\
58&0:7,\ 4:8,\ 6:17,\ 7:9.
\end{array}
\tag{3.3}
$$



At $t=58$, the remaining bits of $B_r$ are zero. For acceptance, masks $6,7$ are impossible: their $B_r$-borrow cannot clear. Mask $0$ needs no additional cost. Mask $4$ needs two more borrows before the next available $N$-bit clears it.

Hence


$$
\boxed{\text{every accepted upper path costs at least }7.}
\tag{3.4}
$$



For later use, reverse min-plus propagation from the accepted terminal state gives


$$
\begin{array}{c|c}
t&\text{remaining minimum costs on masks }0,2,6,7\\ \hline
38&(3,3,3,3)\\
41&(3,3,3,3).
\end{array}
\tag{3.5}
$$



Equations (2.3), (3.2), and the terminal condition specify every entry of these small products. In particular, the lower bound is over **all four** possible incoming low-byte states, not merely a selected family of prefixes.

---

## 4. Exact pointwise kernel content

At the eighth scale, every mask in (3.1) has


$$
d_8=\kappa_8+f(x)\ge1.
$$


Thus the low byte contributes at least one to (2.1). Combining this with (3.4),


$$
\boxed{v_2(h_r(j))\ge8}
\tag{4.1}
$$


for every supported original row and every $0\le r\le81$.

This lower bound is sharp.

Take $r=81$, and take


$$
j_*=
2^9+2^{10}+2^{23}+2^{27}+2^{31}
+2^{43}+2^{48}+2^{50}.
\tag{4.2}
$$


This is an original supported index, since $j_*<b-81$.

Every selected bit of $j_*$ is a bit of $N$, so


$$
\binom N{j_*}\quad\text{is odd}.
$$


For $k=b-81-j_*$, the addition $C+k$ has exactly the eight carries at positions


$$
\boxed{7,\ 24,\ 25,\ 33,\ 34,\ 42,\ 44,\ 45.}
$$


Therefore


$$
v_2(h_{81}(j_*))=8.
$$



We have proved:

### Theorem 1 — Sharp content of the arbitrary-numerator kernel lattice

For the fixed original $b,n$,


$$
\boxed{\min_{0\le r\le81,\ 0\le j\le b}v_2(h_r(j))=8.}
$$


Consequently, for every integer polynomial $B$ of degree at most $81$,


$$
Z_j=\sum_{r=0}^{81}B_rh_r(j)
$$


satisfies


$$
\boxed{2^8\mid Z_j\quad(0\le j\le b).}
$$



This is an original-word theorem. It is **not** a theorem for every $b$ sharing only the twelve low bits used in turn 3.

---

# Part II. Why the kernel has extra Gram cancellation

## 5. The shallowest rows come in quartets

Call a row **active** if


$$
v_2(h_r(j))=8
$$


for at least one $r$.

An active row must have:

- low-byte carry cost exactly $1$;
- upper carry cost exactly $7$.

By (3.3) and (3.5), every upper path of total cost $7$ must pass through mask $0$ immediately before bit $38$, and again immediately before bit $41$. Indeed, at either checkpoint, every other mask has forward cost greater than $4$, while the remaining cost is $3$.

At both bit positions $38$ and $41$,


$$
(N_t,B_{r,t},S_{r,t})=(1,1,1),
\qquad \kappa_{t+1}=0.
$$


Thus $z=0$. From mask $0$, both choices of the next bit lead back to mask $0$, with zero carry cost.

It follows that toggling either bit $38$ or bit $41$:

- preserves the carry cost;
- preserves terminal acceptance;
- preserves the original cutoff;
- preserves activity, for the same shift $r$.

The active rows therefore split into disjoint four-element sets


$$
\boxed{
j,\quad j\mathbin{\oplus}2^{38},\quad
j\mathbin{\oplus}2^{41},\quad
j\mathbin{\oplus}2^{38}\mathbin{\oplus}2^{41}.
}
\tag{5.1}
$$



This is a statement about the original finite row set. No infinite completion or changed endpoint is involved.

---

## 6. A whole-row proportionality lemma

Counting active rows is enough for a norm congruence modulo $4$, but not by itself for a mixed-product congruence. We need a common multiplier for the **whole row**.

Retain the exact base kernel


$$
K(j)=
\binom Nj\binom{a+b-j-1}{b-j}.
$$


For each shift $r$, the accepted shift identity gives


$$
h_r(j)=\frac{K(j)}{D}\,U_r(j),
\qquad
D=(a)^{\overline{81}},
$$


where


$$
U_r(j)=
(b-j)_{\underline r}
(a+b-j)^{\overline{81-r}}.
$$



The established fixed-divisor argument gives


$$
P_r:=U_r/2^{73}\in\operatorname{Int}_{\le81}(\mathbb Z),
$$


and


$$
D=2^{80}d,\qquad d\ \text{odd}.
$$


Hence


$$
\boxed{
h_r(j)=\frac{K(j)}{2^7d}P_r(j).
}
\tag{6.1}
$$



### Integer-valued translation bound

If $P\in\operatorname{Int}_{\le81}(\mathbb Z)$, then for $t\ge7$,


$$
\boxed{
P(j+2^t)-P(j)\in2^{t-6}\mathbb Z.
}
\tag{6.2}
$$



To prove this, expand $P$ in the binomial basis and use Vandermonde:


$$
\binom{j+2^t}{r}-\binom jr
=
\sum_{i=1}^{r}\binom{2^t}{i}\binom j{r-i}.
$$


For $1\le i\le81$,


$$
v_2\binom{2^t}{i}
=t-v_2(i)\ge t-6.
$$


Negative translations follow by exchanging the two arguments.

Now let $j,j'$ be adjacent rows in one quartet. Thus $j'-j=\pm2^{38}$ or $\pm2^{41}$.

Choose an $r$ for which both rows have $v_2(h_r)=8$. Equation (6.1) shows


$$
v_2(K(j))\le15.
$$


By (6.2), $P_r(j')-P_r(j)$ is divisible by $2^{32}$, so the valuations of these two $P_r$-values agree. Since the two $h_r$-values have valuation $8$,


$$
v_2(K(j'))=v_2(K(j)).
$$


Therefore


$$
u=\frac{K(j')}{K(j)}
$$


is an odd $2$-local unit.

For **every** shift $s$, not only the selected $r$, equations (6.1)–(6.2) now give


$$
h_s(j')-u h_s(j)
=
\frac{K(j')}{2^7d}\bigl(P_s(j')-P_s(j)\bigr)
\in2^{25}\mathbb Z_{(2)}.
$$



### Lemma 2 — Common odd proportionality on active quartets

For adjacent rows $j,j'$ of an active quartet, there is an odd $2$-local unit $u$, independent of the numerator, such that


$$
\boxed{
h_s(j')\equiv u h_s(j)\pmod{2^{25}}
\quad(0\le s\le81).
}
\tag{6.3}
$$



Thus every integer-numerator vector in the kernel lattice has the same row multiplier $u$.

---

## 7. Universal kernel Gram divisibility

Let $Z,Z'$ be any two integer-numerator vectors in the degree-$81$ lattice.

On a nonactive row, every $h_r$ is divisible by $2^9$, so


$$
Z_jZ'_j\in2^{18}\mathbb Z.
$$



On an active quartet, divide both vectors by $2^8$. By (6.3), adjacent normalized rows are multiplied, modulo $4$, by the same odd unit $u$. Since


$$
u^2\equiv1\pmod4,
$$


the normalized mixed product is constant modulo $4$ across the quartet. Its four-term sum is therefore zero modulo $4$.

This proves:

### Theorem 3 — Universal Gram depth of the kernel lattice

For all integer polynomials $B,B'$ of degree at most $81$,


$$
\boxed{
2^{18}\mid
\sum_{j=0}^{b}Z_jZ'_j.
}
\tag{7.1}
$$



In particular, all norms in the lattice are divisible by $2^{18}$.

The theorem proves a lower Gram depth. It does not assert that $18$ is the exact minimum Gram depth.

---

# Part III. The complete columns force the observed twenty-bit zeros

## 8. The parity lifts are deeper than their turn-3 bounds

Put both complete columns over the denominator $(1-z)^{a+81}$. The parity-lift numerators are


$$
A_f^{(0)}=z^3(1-z)^{78},
\qquad
A_{e,\mathrm{common}}^{(0)}=(1-z)^{81}.
$$


Their weighted columns are


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



The upper carry problem from bit $8$ onward is the same as before:

- for $X^{(0)}$, the two lower parameters are
  

$$
B=b-3,\qquad C=a+2;
$$


- for $Y^{(0)}$, they are
  

$$
B=b,\qquad C=a-1.
$$



Their low bytes are


$$
(B,C)=(206,134),\qquad(209,131),
$$


and in both cases


$$
(B+C)\bmod256=84,\qquad \kappa_8=1.
$$


The ordering is again


$$
68<84<B\bmod256.
$$


Thus bit $7$ contributes at least one carry, and the upper bits contribute at least seven.

For $Y^{(0)}$, the turn-3 low-three-bit argument already gives at least two factors of $2$. Therefore


$$
\boxed{2^{10}\mid Y_j^{(0)}.}
\tag{8.1}
$$



For $X^{(0)}$, the low-four-bit bound is three, not merely two. Here


$$
N\equiv4,\quad B\equiv14,\quad C\equiv6\pmod{16}.
$$


For $j\bmod16=0,\ldots,15$, the combined borrow/carry counts within these four bits are


$$
3,4,3,5,3,4,3,6,3,4,3,5,3,4,3,7.
$$


Every count is at least three. Adding the separate contribution at bit $7$ and the upper minimum seven gives


$$
\boxed{2^{11}\mid X_j^{(0)}.}
\tag{8.2}
$$



All statements include unsupported rows as zero.

---

## 9. Content at least $2^9$

Write


$$
A_f=A_f^{(0)}+2B_f,
$$


and


$$
(1-z)^4A_e=(1-z)^{81}+2B_e,
$$


where $B_f,B_e\in\mathbb Z[z]$ have degree at most $81$.

The corresponding kernel-lattice vectors satisfy


$$
X=X^{(0)}+2Z_f,\qquad
Y=Y^{(0)}+2Z_e.
\tag{9.1}
$$



Theorem 1 and (8.1)–(8.2) give


$$
\boxed{
X,Y\in2^9\mathbb Z^{b+1}.
}
\tag{9.2}
$$



Moreover, on a **nonactive** row, $Z_f,Z_e$ are divisible by $2^9$, so


$$
\boxed{
2^{10}\mid X_j,\ Y_j
\quad\text{on every nonactive row}.
}
\tag{9.3}
$$



The distinction between (9.2) and (9.3) supplies the final two Gram bits.

---

## 10. The depth-twenty theorem

On a nonactive row, (9.3) gives


$$
X_j^2,\ X_jY_j,\ Y_j^2\in2^{20}\mathbb Z.
$$



On an active quartet, divide the complete columns by $2^9$. They remain integer-numerator kernel vectors, so Lemma 2 supplies a common odd row multiplier to much more precision than needed. The normalized products are consequently constant modulo $4$ across the quartet, and their four-term sums vanish modulo $4$.

We obtain:

### Theorem 4 — Original complete two-column Gram depth

For the original $b,n$, the accepted complete parity masks and the degree bounds imply


$$
\boxed{
X,Y\in2^9\mathbb Z^{b+1},
}
$$


and


$$
\boxed{
2^{20}\mid
\sum_{j=0}^{b}V_jW_j
\qquad
\bigl(V,W\in\mathbb ZX+\mathbb ZY\bigr).
}
\tag{10.1}
$$



In particular,


$$
\boxed{
v_2(D_{\rm raw})\ge20,\qquad
v_2(E_{\rm raw})\ge20.
}
\tag{10.2}
$$



### What this explains—and what it does not

The observed zeros are explained by:

1. a sharp universal kernel content $2^8$;
2. the actual parity class, which raises column content to at least $2^9$;
3. a four-row cancellation on the only rows that could contribute below depth $20$.

This does **not** identify:

- the exact actual column contents;
- the exact norm or mixed depths;
- the primitive norm loss;
- a ratio to positive prescribed precision.

It also does not extend a twenty-bit short representation to true thirty-two-bit physical columns.

---

# 11. A short actual-numerator test for exact content $2^9$

The new theorem gives a particularly small follow-on calculation.

A low-byte carry cost of exactly one is possible precisely as follows. Put


$$
u=81-r.
$$


Then


$$
u\in[0,81],\qquad u\mathbin{\&}16=0,
$$


and the two possible low prefixes of $j$ are


$$
J=u\mathbin{\&}68,\qquad J+128.
$$


Here


$$
J\in\{0,4,64,68\}.
$$



For a fixed $J$, all eligible shifts have the same support modulo $2$ after dividing $h_r$ by $2^8$. Different $J$'s have disjoint supports. Each support is nonempty.

The four shift sets are


$$
\begin{aligned}
\mathcal R_0={}&[38,41]\cup[46,49]\cup[70,73]\cup[78,81],\\
\mathcal R_4={}&[34,37]\cup[42,45]\cup[66,69]\cup[74,77],\\
\mathcal R_{64}={}&[6,9]\cup[14,17],\\
\mathcal R_{68}={}&[2,5]\cup[10,13],
\end{aligned}
\tag{11.1}
$$


where each interval denotes its integer points.

For $B(z)=\sum B_rz^r$, define


$$
\chi_J(B)=\sum_{r\in\mathcal R_J}B_r\pmod2.
\tag{11.2}
$$



Then


$$
Z/2^8\not\equiv0\pmod2
\iff
(\chi_0,\chi_4,\chi_{64},\chi_{68})(B)\ne(0,0,0,0).
\tag{11.3}
$$



Applying this to (9.1):



$$
\boxed{
a_{\rm cont}=9
\iff
\bigl(\chi_J(B_f)\bigr)_J\ne0,
}
$$


and otherwise $a_{\rm cont}\ge10$. Similarly,


$$
\boxed{
c_{\rm cont}=9
\iff
\bigl(\chi_J(B_e)\bigr)_J\ne0,
}
$$


and otherwise $c_{\rm cont}\ge10$.

Only $A_f,A_e\bmod4$ are needed. The calculation consists of **eight parity sums** after the two displayed numerator subtractions and exact divisions by $2$.

The numeric arrays are not printed in the supplied reports, so I do not invent these eight outputs. This is an unevaluated, explicitly bounded new post-processing task on the retained artifact—not a request to rerun an accepted computation.

---

# Part IV. Precision consequences

## 12. What higher nonzero Gram residues would permit

Suppose a genuine higher-precision calculation returns nonzero residues modulo $2^{32}$. Then


$$
d_0=v_2(D_{\rm raw}),\qquad e_0=v_2(E_{\rm raw})
$$


are exact and lie in


$$
20\le d_0,e_0\le31.
$$



For $s$ reliable absolute $2$-adic bits in


$$
\frac{E_{\rm raw}}{2D_{\rm raw}},
$$


the sufficient guards remain


$$
M_E\ge s+d_0+1,
\qquad
M_D\ge s+2d_0+1-e_0.
\tag{12.1}
$$



With $M_D=M_E=32$,


$$
\boxed{
s\le
\min\{31-d_0,\ 31-2d_0+e_0\}.
}
\tag{12.2}
$$



Thus even a nonzero 32-bit Gram pair need not deliver many ratio bits. A zero norm residue at 32 bits would again provide no upper norm-depth bound.

If the eight parity tests establish $a_{\rm cont}=9$, a nonzero norm residue would identify the primitive binary norm loss as


$$
d_0-18.
$$


Without the exact content test, only


$$
9\le a_{\rm cont}\le\lfloor d_0/2\rfloor
$$


is justified.

### Logarithmic omission guard

Retain the complete norm-relative condition


$$
K_{\rm norm}+a_{\rm cont}-d_0-1\ge s,
$$


with


$$
K_{\rm norm}\ge2000b-138.
$$



If a true 32-bit norm residue is nonzero, then $d_0\le31$, and the new content bound gives


$$
K_{\rm norm}+a_{\rm cont}-d_0-1
\ge K_{\rm norm}-23
\ge2000b-161.
\tag{12.3}
$$


This verifies the contemplated small logarithmic guards once the norm depth has an actual upper bound. A zero norm residue does not do so.

---

## 13. A useful precision distinction: columns versus Gram forms

The new content theorem improves comparison precision, but does not manufacture physical coefficients.

Suppose $x,x'$ agree coordinatewise modulo $2^M$, and both have content at least $2^c$. Then


$$
\sum x_j'^2-\sum x_j^2
\in
2^{\min(M+c+1,\,2M)}\mathbb Z.
\tag{13.1}
$$



For two columns of contents at least $2^c,2^{c'}$, both supplied to precision $2^M$,


$$
\sum x'_jy'_j-\sum x_jy_j
\in
2^{\min(M+c,M+c',2M)}\mathbb Z.
\tag{13.2}
$$



With $M=20$ and $c=c'=9$, integer lifts of the accepted columns agree with the actual Gram forms to at least

- $30$ bits for the norm;
- $29$ bits for the mixed form.

However, the accepted contractions evaluated only twenty normalized physical bits. They have not supplied these additional residues. In particular, their zero outputs do **not** imply vanishing modulo $2^{30}$ or $2^{29}$.

Likewise, true physical column precision $23$, together with the proved content bound, would suffice for a 32-bit norm/mixed comparison. The proposed full 32-bit physical lift is conservative and safe. It remains a genuinely new lift; changing representatives of the old coefficients cannot produce true 32-bit columns.

---

# Part V. Safe contract for the proposed 32-bit physical lift

## 14. Tail cutoffs

### 14.1 Central series

For the coefficient appearing in the central formula,


$$
\frac{2^s(s!)^2}{(2s+\delta)!},
\qquad \delta\in\{0,1\},
$$


one has exactly


$$
v_2\!\left(\frac{2^s(s!)^2}{(2s+\delta)!}\right)
=v_2(s!).
\tag{14.1}
$$


After cancellation, the remaining denominator is odd.

Now


$$
v_2(36!)=18+9+4+2+1=34.
$$


Thus every central term with $s\ge36$ vanishes modulo $2^{32}$, with two spare valuation bits:


$$
\boxed{T=36\ \text{is safe}.}
$$



No even modular inverse is involved.

### 14.2 First-force head

The central prefactor at index $\ell$ contains a falling product of length $\lceil\ell/2\rceil$, so


$$
v_2(B_\ell)\ge
v_2\!\left(\left\lceil\frac\ell2\right\rceil!\right).
$$



For a summand in the first force,


$$
\binom i\ell
(n+\ell+1)\cdots(n+i)B_\ell,
$$


its valuation is at least


$$
v_2(i!)-v_2(\ell!)
+
v_2\!\left(\left\lceil\frac\ell2\right\rceil!\right).
$$


Since


$$
v_2(\ell!)-
v_2\!\left(\left\lceil\frac\ell2\right\rceil!\right)
\le\left\lfloor\frac\ell2\right\rfloor,
$$


this is at least


$$
v_2\!\left(\left\lfloor\frac i2\right\rfloor!\right).
$$



Therefore every original first-force index $i\ge72$ has depth at least $34$:


$$
\boxed{I=72\ \text{is safe}.}
\tag{14.2}
$$



This is a tail proof, not an extrapolation from a checked interval of zero coefficients.

### 14.3 Exponential exterior

For


$$
v_t=(b+1)\cdots(b+t),
$$




$$
v_2(v_t)\ge v_2(t!).
$$


Thus $v_t\equiv0\pmod{2^{32}}$ for $t\ge36$.

The retained exterior tail has length $36$. Applying a bandwidth-$m$ operator yields support length


$$
\boxed{R=m+36.}
\tag{14.3}
$$



---

## 15. Operator and finite endpoint precision

The bandwidth formula


$$
m=4(P-1)
$$


uses the established integral construction in which, after normalization by an odd diagonal unit, the nonidentity operator lies in $2R$ and has bandwidth at most four.

Indeed,


$$
(I+Q)^{-1}\equiv
\sum_{k=0}^{P-1}(-Q)^k\pmod{2^P},
\qquad Q\in2R,
$$


and the last retained power has bandwidth at most $4(P-1)$.

For $P=32$,


$$
\boxed{m=124.}
$$



The corresponding precision contract is:

1. **New operator coefficients:** compute the actual normalized symbol and inverse coefficients modulo $2^{32}$. Old twenty-bit representatives are insufficient.
2. **Finite boundary:** construct the endpoint data for bandwidth $124$, not a padded $76$-band certificate.
3. **Unit inverse:** the finite endpoint/Schur inverse must be justified over $\mathbb Z_{(2)}$, for example by its established identity-plus-even form. Its unit determinant is the relevant guard.
4. **No physical loss:** integral matrix products and inverses of unit matrices preserve 32-bit precision.
5. **Complete return:** retain the same finite return and terminal selection formula, with the new boundary size.

The supplied head and numerator sources refer to archived operator and Schur artifacts rather than printing their coefficient arrays. Consequently, the numerical 32-bit operator and endpoint assertions are obligations of the genuinely new lift. The abstract precision claim above is conditional on the exact integral/unit hypotheses of the accepted construction; it is not a certification of unavailable new coefficient data.

---

## 16. Laurent and numerator dimensions

With


$$
m=124,\quad I=72,\quad R=160,
$$


the safe offsets are


$$
\boxed{
L_0=m+R=284,\qquad K_0=m+I=196.
}
$$



These follow directly from the source exponents.

For a base-$n$ source, the shifted numerator exponent is


$$
r-s+e+L_0,
$$


and the power of $1-z$ is


$$
K_0-\text{extra}-e,
$$


where $\text{extra}\in\{0,I\}$, $e\le s\le m$. Both are nonnegative with these choices.

The safe array lengths are:

| Object | Safe length |
|---|---:|
| first-force head | $72$ |
| factorial exterior tail | $36$ |
| complete exterior load | $160$ |
| $2n$-branch numerator | $L_0+K_0=480$ |
| $n$-branch numerator | $L_0=284$ |
| reconstructed $2n$-branch numerator | $482$ |
| reconstructed $n$-branch numerator | $286$ |

A convenient independent-jet contract is


$$
\boxed{
\mathrm{JET}=2m-1=247,\qquad
\mathrm{MAX}=\mathrm{JET}+m=371.
}
$$


The required inverse-power coefficients then extend only through


$$
\mathrm{JET}+L_0=\mathrm{MAX}+R=531.
$$



Thus the complete principal-part and jet checks can cover


$$
-284\le k\le247
$$


using bounded arrays. No original-length allocation is needed.

The reconstructed representation, before any target-specific cancellation, is


$$
z^{-284}
\left(
\frac{H_2(z)}{(1-z)^{2n+197}}
+
\frac{H_1(z)}{(1-z)^{n+1}}
\right).
\tag{16.1}
$$



The reconstruction must still check the whole relation


$$
(k-b)g_k-g_{k-1},
$$


including the exponential terminal contribution


$$
-b\,g_0-1.
$$


This is where the retained exterior $+1$ continues to enter. It is not omitted or added a second time.

---

## 17. Do the $n$-branch and the $44/48$ factors persist?

### The rigorous answer from the supplied sources

Their twenty-bit disappearance/divisibility is accepted. Their thirty-two-bit disappearance/divisibility is **not proved by those sources**.

There is no valid operation that promotes


$$
H_1\equiv0\pmod{2^{20}}
$$


to


$$
H_1\equiv0\pmod{2^{32}}.
$$


Likewise, zero remainders in twenty-bit division by $(1-z)^{44}$ or $(1-z)^{48}$ do not certify the same divisions at 32 bits.

Accordingly, the safe new construction must initially retain both branches in (16.1).

### Exact bounded checks required

For each new complete reconstructed column:

1. Check all coefficients of the reconstructed $n$-branch modulo $2^{32}$.
2. If it vanishes, check the $z^{284}$ factor in the surviving branch.
3. After removing that shift, determine the actual multiplicity of $1-z$ by exact polynomial divisions modulo $2^{32}$, retaining every remainder.

These divisions cost no binary precision: $z$ is a coefficient shift, and $1-z$ is monic up to a unit. Their issue is **truth of divisibility**, not a nonunit guard.

### Why $44/48$ are not invariant parameters

The new surviving denominator, if the $n$-branch vanishes, is initially


$$
(1-z)^{2n+197},
$$


rather than $(1-z)^{2n+125}$.

Therefore:

- retaining factors $44,48$ would give short-degree bounds $153,149$;
- retaining short exponents $81,77$ would require factors $116,120$.

One cannot simultaneously keep the old factor counts and the old short degrees. Which multiplicities the actual new numerators possess is a new bounded arithmetic question.

I do not claim either numerical outcome before the new physical data exist.

---

## 18. A fully guarded fallback if the new $n$-branches vanish

If the new $n$-branches vanish and the contact shift $z^{284}$ is verified, one need not remove any $1-z$ factor to obtain a bounded contraction.

Both numerators then have degree at most


$$
R_*=197
$$


over the denominator $(1-z)^{a+197}$.

For this degree,


$$
v_2(197!)=193.
$$


The maximum valuation of $\binom{197}{r}$ is $6$; it is attained at $r=70$, since


$$
197=70+127
$$


has six carries. Thus the universal fixed-divisor exponent is


$$
\boxed{t_{197}=193-6=187.}
$$



For the actual $a$,


$$
v_2\bigl((a)^{\overline{197}}\bigr)
=
99+50+25+12+6+3+1+1
=
\boxed{197}.
$$


There is no contribution from multiples of $512$ in this short interval.

Hence the integral fixed-divisor normalization has loss


$$
197-187=10
$$


per column, and loss $20$ for either Gram payload. A 32-bit physical Gram target is therefore recovered from


$$
\boxed{52\text{ kernel bits}}
$$


for both payloads.

The payload degree is at most $394$. The established odd-factorial Newton evaluator has degree $102$ at 52 bits, and the transport degree envelope is


$$
\boxed{
\left\lfloor\frac{394}{2^t}\right\rfloor+102.
}
$$


An unreduced product envelope is below degree $600$.

This is a bounded, explicitly guarded fallback. It needs no $2^{32}$-entry residue table and no new saturation computation. It is conditional on the new $n$-branch and contact checks, not on the unverified $44/48$ factors.

If a reconstructed $n$-branch survives, it must remain in the observable representation; the one-base $R_*=197$ contraction is then not applicable as written.

---

# 19. Bounded work that remains justified

No accepted twenty-bit producer, Smith calculation, payload compilation, or contraction needs to be rerun.

There are two genuinely new bounded tasks.

## A. Eight-bit content certificate from the retained short arrays

**Inputs**

- $A_f,A_e\bmod4$;
- the explicit parity lifts;
- the four shift sets in (11.1).

**Operations**

Form


$$
B_f=\frac{A_f-z^3(1-z)^{78}}2\pmod2,
$$




$$
B_e=\frac{(1-z)^4A_e-(1-z)^{81}}2\pmod2,
$$


and evaluate their four $\chi_J$'s.

**Verifiable output**

For each column:

- four parity bits;
- “content exactly $9$” if at least one bit is nonzero;
- otherwise “content at least $10$.”

This does not evaluate a Gram form.

## B. The independently planned new physical lift

**Inputs**

- the original $b,n$;
- the exact accepted finite operator and force formulas;
- newly evaluated 32-bit operator and finite endpoint data;
- the dimensions established in §§14–16.

**Required output**

1. New complete physical forcing/head/exterior data modulo $2^{32}$.
2. New integral finite inverse and endpoint-return checks.
3. Both reconstructed branches for both columns.
4. Complete principal-part and terminal $+1$ checks.
5. Explicit $n$-branch zero/nonzero decisions.
6. Actual contact and $1-z$ division remainders and exponents.
7. Newly derived conversion/fixed-divisor guards for the representation actually obtained.
8. New norm/mixed residues, with exact valuations only for nonzero residues.
9. The ratio guard (12.1), evaluated using those actual depths.

The odd-factorial Newton evaluator replaces any exponential modulus table throughout.

---

# 20. All-prime normalization and the whole error are still open

The local binary theorem does not determine the least actual common clearer, odd-prime row contents, or the final gcd.

Retain the complete integer columns and


$$
A_B=N_{B,1}^{T}\Omega N_{B,1},
\qquad
H_B=N_{B,1}^{T}\Omega N_{B,2},
$$




$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=\frac{A_B}{g_B},\qquad
p_n=\frac{H_B}{g_B}.
}
$$



With the least actual common clearer $d_B$, the primitive multiplier remains


$$
\frac{d_B^2}{g_B}.
$$



No column content has been divided out of the physical contractions in this report. In particular, the newly proved binary contents do not authorize replacing the final all-prime gcd by a selected-prime normalization.

The approximation quantity remains the whole same-index form


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n.
}
$$



Even conditional on the previously stated complete signed-error asymptotic, an irrationality argument still needs an infinite original subsequence on which the **actual primitive denominator** makes the whole nonzero form tend to zero.

Neither a structural twenty-bit Gram zero nor a future nonzero thirty-two-bit residue proves that infinite all-prime comparison.

---

# 21. Proof-status ledger

| Statement | Status |
|---|---|
| Accepted original norm and mixed residues are zero modulo $2^{20}$ | Accepted finite computations |
| Correct saturated content-division guards $194,197$ | Explicitly checked in the new supplied cross-check |
| Upper carry minimum $7$, including all 82 shifts | Exact finite min-plus certificate at the original word |
| Universal kernel content exactly $2^8$ | **Proved**, including an explicit attaining row |
| Active rows form quartets at bits $38,41$ | **Proved** |
| Common odd proportionality of whole kernel rows | **Proved** using integer-valued translation |
| Universal degree-$81$ kernel Gram divisibility $2^{18}$ | **Proved** |
| Parity-lift contents $2^{11},2^{10}$ | **Proved** |
| Complete physical column contents at least $2^9$ | **Proved** |
| Both original complete Gram forms divisible by $2^{20}$ | **Proved structurally** |
| Exact actual contents $9$ versus at least $10$ | Reduced to eight explicit parity sums; outputs not supplied |
| Proposed cutoff and dimension tuple $124,36,72,160,284,196$ | **Derived**, with integral/unit operator hypotheses explicit |
| Thirty-two-bit $n$-branch disappearance | New finite check required |
| Thirty-two-bit $1-z$ multiplicities | New finite check required |
| Exact norm/mixed depths and ratio precision | Open pending higher nonzero data |
| All-prime primitive denominator versus whole same-index error | Open |
| Irrationality or rationality of $e+\pi$ | Unresolved |

---

## Conclusion

The accepted twenty-bit zero is no longer unexplained by the column structure.

The new result is


$$
\boxed{
\text{kernel content }2^8
\quad+\quad
\text{actual parity class}
\quad+\quad
\text{four-row odd-unit cancellation}
}
$$


which proves


$$
\boxed{
X,Y\in2^9\mathbb Z^{b+1},
\qquad
D_{\rm raw},E_{\rm raw}\in2^{20}\mathbb Z.
}
$$



The arbitrary-numerator lattice therefore does force substantially deeper weighted columns than the earlier parity argument detected. Its fixed original binary phase also forces genuine mixed-product cancellation, not merely pointwise divisibility or a norm-only parity effect.

The immediate mathematical bottleneck is now sharper:



$$
\boxed{
\text{exact actual content and the first nonzero Gram layer above depth }20.
}
$$



The content question has a new eight-parity-bit certificate. The higher physical lift has a safe bounded precision contract, but its $n$-branch cancellation and polynomial factor removals must be established anew before higher residues are interpreted.

The global bottleneck remains unchanged:



$$
\boxed{
\text{all-prime control of the actual primitive denominator against the
whole same-index nonzero error on an infinite original sequence}.
}
$$



Accordingly, this turn proves a new original-phase content and Gram-depth theorem, but gives neither an unconditional proof nor a disproof of the irrationality of $e+\pi$.
