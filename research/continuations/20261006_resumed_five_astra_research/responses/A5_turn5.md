> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, turn 5 — Sixteen-row norm blocks, an odd normalized Gram form, and the unresolved cross-block depth

## Executive conclusion

The new receipt genuinely establishes


$$
\boxed{v_2(D_{\rm raw})\ge30,\qquad v_2(E_{\rm raw})\ge29.}
$$


These are newly evaluated physical residues, not promotions of the old twenty-bit zeros. Neither valuation is yet exact.

I close the support-interpretation gap in the four-parity content test. With the supplied outputs


$$
\chi_f=(1,0,1,0),\qquad \chi_e=(0,0,0,0),
$$


the complete physical columns satisfy


$$
\boxed{v_2(\operatorname{content}X)=9,\qquad
v_2(\operatorname{content}Y)\ge10.}
$$


In particular, the binary norm loss after making the first column primitive is


$$
\boxed{v_2(D_{\rm raw})-18\ge12.}
$$


This is not the final all-prime denominator normalization.

The new structural advance is a larger original-row grouping:

* valuation-eight kernel rows form **octets**, not merely quartets: bit $52$ is an additional free bit;
* valuation-nine kernel rows form quartets at bits $41,52$;
* the active octets pair under the low-bit toggle $6$, giving **sixteen original rows**;
* on each paired block, the normalized first-column norm is governed, to the needed precision, by an odd multiple of the explicit form
  

$$
\boxed{Q(x,z)=x^2+2xz+2z^2=(x+z)^2+z^2.}
$$



The associated $2\times2$ Gram matrix is


$$
\boxed{
G_0=\begin{pmatrix}1&1\\1&2\end{pmatrix},\qquad \det G_0=1.
}
$$



This proves structurally


$$
\boxed{2^{22}\mid D_{\rm raw}.}
$$


More sharply, every active sixteen-row block in either of the first column’s odd support classes has **exact block norm valuation $22$**. Thus the observed global depth at least $30$ cannot be explained by claiming that every such block is itself thirty-divisible. It requires cancellation between normalized block contributions.

This yields a concrete residual bottleneck:


$$
\boxed{
\frac{D_{\rm raw}}{2^{22}}
\equiv
\sum_{\text{active paired blocks}}\alpha\,Q(x,z)
+\sum_{\text{valuation-nine quartets}}\beta\,t^2
+\sum_{\text{remaining rows}}c^2
\equiv0\pmod{2^8},
}
$$


where every displayed $\alpha,\beta$ is an explicitly defined odd $2$-local unit. The new contraction certifies the final congruence numerically. The derivation below explains the four primitive norm bits preceding it, but does **not** yet explain these remaining eight bits structurally or bound the first nonzero global norm layer.

No accepted $37/45$-bit contraction, Smith calculation, twenty-bit producer, or newly accepted operator/Schur calculation is proposed for repetition.

---

# 1. Data, scope, and notation

Retain exactly


$$
b=150094635296999121=9^{18},\qquad
n=4002b=600678730458590482242,
$$




$$
N=n+2,\qquad a=2n,
$$


and the original physical row domain


$$
\boxed{0\le j\le b.}
$$



The accepted twenty-bit complete presentations are


$$
F(z)=\frac{A_f(z)}{(1-z)^{a+81}},\qquad
E(z)=\frac{A_e(z)}{(1-z)^{a+77}}.
$$


The second presentation includes the complete retained second force, finite return, terminal factorial cancellation, and exterior $+1$.

I use $\widetilde X,\widetilde Y$ for integer lifts furnished by these short presentations, and $X,Y$ for the actual complete physical columns. Thus


$$
X-\widetilde X,\ Y-\widetilde Y\in2^{20}\mathbb Z^{b+1}.
$$


All lower-content assertions below concern the actual columns as well as these lifts.

The common row signs can be suppressed in norms and mixed products. No row is deleted, and no endpoint is extended.

The exact degree-$81$ atoms are


$$
h_r(j)=
\binom Nj
\binom{a+80+b-j-r}{b-j-r},
\qquad 0\le r\le81,
$$


with unsupported lower indices giving zero.

Write


$$
\mu(j)=\min_{0\le r\le81}v_2(h_r(j)).
$$


The accepted min-plus certificate establishes $\mu(j)\ge8$, with equality attained.

---

# 2. What the new receipts do and do not establish

## 2.1 The new quadratic calculation

The $45$-kernel-bit source retains:

* $44$ numerator bits before the norm’s exact $14$-bit division;
* $45$ numerator bits before the mixed form’s exact $16$-bit division;
* the odd denominator units with valuations $80,77$;
* all $71$ input digits;
* terminal acceptance at $000$;
* the complete exterior and the original inclusive range.

Its reported zero residues are therefore


$$
\boxed{D_{\rm raw}\equiv0\pmod{2^{30}},\qquad
E_{\rm raw}\equiv0\pmod{2^{29}}.}
$$



The pointwise content lower bound $9$, independently of the exact-content interpretation, supplies the physical comparison:


$$
D_{\rm raw}-\widetilde X^T\widetilde X\in2^{30}\mathbb Z,
$$




$$
E_{\rm raw}-\widetilde X^T\widetilde Y\in2^{29}\mathbb Z.
$$


Hence these are genuine physical lower bounds.

The code shares the already inspected transport implementation. It is a new precision target, not a wholly independent implementation of that transport.

## 2.2 The new operator and Schur calculation

The supplied source and receipt establish, at the original $b,n$ and precision $32$:

* bandwidth $m=124$;
* all $249$ inverse-coefficient convolution residuals;
* both finite inverse products, comprising $30752$ entries;
* $15376$ transpose entries;
* $15376$ lower padded zeros;
* identity parity of the $124\times124$ Schur matrix.

The matrix inverse uses only odd pivots. This agrees with the independently checked identity-modulo-$2$ property and introduces no binary precision loss.

These are accepted new finite results. They do **not** yet certify the new complete force, physical head, or reconstructed numerators.

---

# Part I. Closing the four-support interpretation

## 3. The low-byte support calculation

Put


$$
u=81-r,\qquad B_r=b-r.
$$


Then


$$
B_r\bmod256=128+u,\qquad
(a+80)\bmod256=212,
$$




$$
N\bmod256=68,\qquad
(a+80+B_r)\bmod256=84+u.
$$



A valuation-eight atom must have low-byte cost exactly $1$ and upper cost exactly $7$.

Before the eighth scale, zero cost requires:

1. no borrow from subtracting the low seven bits of $j$ from $N$;
2. no carry in the corresponding low-seven-bit addition.

Consequently, if $J=j\bmod128$, then


$$
J\in\{0,4,64,68\}.
$$


The second condition is


$$
u-J\ge0,\qquad (u-J)\mathbin{\&}84=0.
$$


Since the allowed bits of $u-J$ are disjoint from those of $J$, this is equivalent to


$$
\boxed{u\mathbin{\&}16=0,\qquad u\mathbin{\&}68=J.}
$$



The complete low byte of $j$ is either


$$
J\quad\text{or}\quad J+128.
$$



For $j\bmod256=J$, the incoming upper state is $000$. For $j\bmod256=J+128$, it is $101$. Indeed,


$$
0\le u-J\le43
$$


gives


$$
J+128>84+u,\qquad J+128\le128+u.
$$


These statements are uniform over every eligible shift $r$.

Above the low byte, the fixed words are identical for all $r$. Thus, for fixed $J$ and a fixed choice of the bit-$7$ branch, all eligible shifts have exactly the same valuation-eight support.

This proves the support assertion used by the parity test—not just the arithmetic description of its four shift sets.

## 3.1 Nonempty support

The attaining upper word from turn 4, with low byte zero, has upper cost $7$ from state $000$. The same upper word works with low byte $J$ for each


$$
J=0,4,64,68,
$$


and an eligible shift from the corresponding set.

Thus each of the four supports is nonempty.

## 3.2 Parity after division by $2^8$

On its valuation-eight support,


$$
h_r(j)/2^8
$$


is odd. Outside that support, it is even.

Therefore, for


$$
Z_j=\sum_{r=0}^{81}B_rh_r(j),
$$


one has, on support class $J$,


$$
\boxed{\frac{Z_j}{2^8}\equiv\chi_J(B)\pmod2.}
$$



This is the missing interpretation linking the independently checked parity sums to actual row content.

---

# 4. Exact first content and stronger second content

Recall


$$
\widetilde X=X^{(0)}+2Z_f,\qquad
\widetilde Y=Y^{(0)}+2Z_e,
$$


where


$$
2^{11}\mid X^{(0)}_j,\qquad 2^{10}\mid Y^{(0)}_j.
$$



Consequently,


$$
\frac{\widetilde X_j}{2^9}\equiv\chi_J(B_f)\pmod2
$$


on active support class $J$, and similarly for the second column.

The supplied parity outputs now give rigorously


$$
\boxed{v_2(\operatorname{content}X)=9,}
$$




$$
\boxed{v_2(\operatorname{content}Y)\ge10.}
$$



The transfer to the actual physical columns uses only precision modulo $2^{10}$, far below the accepted twenty physical bits.

At the particular attaining row


$$
j_*=
1416173266667008,
$$


the low byte is $0$. Hence


$$
\boxed{X_{j_*}\equiv512\pmod{1024}.}
$$


This is a theorem prediction suitable for the independent bounded witness evaluation described in §15.

It does not claim that every first-column row has exact depth $9$.

---

# Part II. Larger groups of original rows

## 5. A third free bit on the shallowest rows

The accepted upper table at $52$ consumed bits is


$$
0:9,\qquad1:7,\qquad3:10,\qquad7:9.
$$


Every transition cost is nonnegative.

Thus every accepted upper path of cost at most $8$ must be in state $1$ immediately before bit $52$.

At bit $52$,


$$
(N_{52},B_{r,52},S_{r,52})=(1,1,0),
$$


so the transition mask is $1$. Also $\kappa_{53}=1$, and


$$
1+f(1)=0.
$$


From state $1$, both choices of the bit of $j$ return to state $1$, at zero cost.

Therefore toggling bit $52$ preserves every atom path of total valuation at most $9$.

This is a new consequence of the already checked min-plus table; no new min-plus run is needed.

---

## 6. The valuation-layer partition

Partition the original rows into


$$
\mathcal A=\{j:\mu(j)=8\},
$$




$$
\mathcal B=\{j:\mu(j)=9\},
$$




$$
\mathcal C=\{j:\mu(j)\ge10\}.
$$



### 6.1 Active octets

For $\mathcal A$, the turn-4 checkpoints force state $0$ before bits $38$ and $41$. Section 5 adds state $1$ before bit $52$.

Thus $\mathcal A$ is a disjoint union of octets


$$
\boxed{
\left\{
j\mathbin{\oplus}\epsilon_{38}2^{38}
 \mathbin{\oplus}\epsilon_{41}2^{41}
 \mathbin{\oplus}\epsilon_{52}2^{52}
:\epsilon_{38},\epsilon_{41},\epsilon_{52}\in\{0,1\}
\right\}.
}
$$



All eight rows remain original supported rows.

### 6.2 Valuation-nine quartets

An atom of valuation $9$ has upper cost at most $8$.

At checkpoint $41$, every state other than $0$ has forward-plus-remaining cost at least $9$. Therefore such an atom must pass through state $0$ before bit $41$.

At checkpoint $52$, the preceding argument forces state $1$.

Thus toggles $41,52$ preserve an attaining valuation-nine atom. They also preserve $\mathcal A$; hence they cannot send a row of $\mathcal B$ into $\mathcal A$.

Therefore $\mathcal B$ is a disjoint union of quartets at bits


$$
\boxed{41,\ 52.}
$$



### 6.3 Actual row-content bounds on these layers

The parity-lift decomposition gives


$$
\begin{array}{c|cc}
\text{row layer}&v_2(X_j)\text{ at least}&v_2(Y_j)\text{ at least}\\ \hline
\mathcal A&9&10\\
\mathcal B&10&10\\
\mathcal C&11&10.
\end{array}
\tag{6.1}
$$



The last row is important: for the first column,


$$
X^{(0)}_j\in2^{11}\mathbb Z,\qquad 2Z_{f,j}\in2^{11}\mathbb Z
$$


on $\mathcal C$. The second column does not receive that same $11$-bit bound merely from this argument.

---

# 7. Stronger whole-row proportionality

Retain the exact base


$$
K(j)=\binom Nj\binom{a+b-j-1}{b-j}.
$$


The accepted fixed-divisor identity is


$$
h_r(j)=\frac{K(j)}{2^7d}P_r(j),
$$


where $d$ is odd and


$$
P_r\in\operatorname{Int}_{\le81}(\mathbb Z).
$$



The integer-valued translation estimate is


$$
P_r(j+2^t)-P_r(j)\in2^{t-6}\mathbb Z.
$$



There is a useful strengthening of the previous precision estimate:


$$
\boxed{v_2(K(j))\ge10}
$$


for every original row, because $K=Y^{(0)}$.

Suppose $j,j'$ are adjacent in one of the octets or quartets just constructed, and an atom has the same valuation $8$ or $9$ on both. The translation bound first proves that


$$
v_2(K(j'))=v_2(K(j)).
$$


Thus


$$
u=\frac{K(j')}{K(j)}
$$


is an odd $2$-local unit.

For every atom,


$$
h_r(j')-u h_r(j)
=
\frac{K(j')}{2^7d}\bigl(P_r(j')-P_r(j)\bigr),
$$


and therefore


$$
\boxed{
h_r(j')\equiv u h_r(j)\pmod{2^{t-3}}.
}
\tag{7.1}
$$



In particular:

* bit $38$ gives precision $35$;
* bit $41$ gives precision $38$;
* bit $52$ gives precision $49$.

These are congruences for the exact short-presentation lifts. Their use for physical norms is subsequently limited by the genuine physical comparison precision.

On any active octet, if $j_0$ is a representative and


$$
u_\epsilon=\frac{K(j_\epsilon)}{K(j_0)},
$$


then


$$
\widetilde X_{j_\epsilon}
\equiv u_\epsilon\widetilde X_{j_0}\pmod{2^{35}},
$$


and the same multiplier works for $\widetilde Y$ and every degree-$81$ numerator.

---

# Part III. Exact weighted octet relations

## 8. The octet norm weight has exact valuation $3$

Define


$$
\sigma_{\mathcal O}
=\sum_{\epsilon\in\{0,1\}^3}u_\epsilon^2.
$$


Counting eight odd squares gives $8\mid\sigma_{\mathcal O}$, but by itself does not show exact depth $3$. The following locality argument supplies the stronger statement.

### 8.1 Odd-factorial locality

For $m\ge0$, write


$$
\Phi(m)=2^{-v_2(m!)}m!
=\prod_{s\ge0}O\!\left(\left\lfloor m/2^s\right\rfloor\right),
$$


where


$$
O(M)=\prod_{\substack{1\le k\le M\\k\ {\rm odd}}}k.
$$



For $p\ge3$,


$$
\boxed{O(M+2^p)\equiv O(M)\pmod{2^p}.}
\tag{8.1}
$$


Indeed, the intervening odd factors form a complete set of odd residues modulo $2^p$, whose product is $1$.

The varying factorial arguments of $K(j)$ are


$$
j,\qquad N-j,\qquad b-j,\qquad a+b-j-1.
$$



On an active row, the low-byte borrow state for $K$ is exactly the same as for an attaining atom:

* $000$ on low byte $J$;
* $101$ on low byte $J+128$.

The fixed upper words also agree. Hence toggles $38,41$ leave the corresponding borrow states identical from the relevant checkpoint onward.

Consider the ratio for toggling bit $52$. For factorial scales $s\le49$, the arguments change by a multiple of $8$, so the odd-factorial contribution is unchanged modulo $8$ by (8.1). For scales $s\ge50$, the arguments after division by $2^s$ are independent of the toggles $38,41$.

Therefore the odd unit multiplier for bit $52$, modulo $8$, is the same across the other four positions of the octet.

### 8.2 Exact octet depth

Let that common multiplier be $c\pmod8$. Pair the octet along bit $52$. Squaring a congruence modulo $8$ between odd units gives a congruence modulo $16$, so


$$
\sigma_{\mathcal O}
\equiv
(1+c^2)\sum_{\epsilon_{38},\epsilon_{41}}u_{\epsilon_{38},\epsilon_{41},0}^{\,2}
\pmod{16}.
$$


Now


$$
1+c^2\equiv2\pmod8,
$$


and a sum of four odd squares is $4\pmod8$. Thus


$$
\boxed{\sigma_{\mathcal O}\equiv8\pmod{16}.}
$$



Consequently,


$$
\boxed{
\alpha_{\mathcal O}:=\sigma_{\mathcal O}/8\in\mathbb Z_{(2)}^\times.
}
\tag{8.2}
$$



For a valuation-nine quartet, no additional locality argument is needed:


$$
\sigma_{\mathcal Q}=\sum_{\epsilon\in\{0,1\}^2}u_\epsilon^2
\equiv4\pmod8,
$$


so


$$
\boxed{
\beta_{\mathcal Q}:=\sigma_{\mathcal Q}/4\in\mathbb Z_{(2)}^\times.
}
\tag{8.3}
$$



These are weighted original-row identities, not unweighted row counts.

---

# 9. Pairing active octets by bit $6$

The support proof in §3 shows that toggling bit $6$ maps


$$
J=0\longleftrightarrow64,\qquad
J=4\longleftrightarrow68,
$$


with the same bit-$7$ branch and exactly the same accepted upper path.

It therefore pairs active octets into sets of sixteen original rows.

The first normalized coordinate


$$
x_j=\widetilde X_j/2^9
$$


has parity


$$
1,0,1,0
$$


in the ordered support classes $0,4,64,68$. Thus paired representatives $j,j'$ satisfy


$$
\boxed{x_{j'}\equiv x_j\pmod2.}
\tag{9.1}
$$



## 9.1 The two octets have the same weight to high precision

For a fixed high-bit toggle $t\ge38$, compare its $K$-unit ratio in the two low-bit-$6$ paired octets.

After eight bits, the factorial-argument borrow states agree. Hence all factorial quotients at scales $s\ge8$ are independent of this low-bit toggle.

At precision $2^p$, the scales $s\le t-p$ disappear from the high-toggle ratio by odd-factorial periodicity. The remaining scales are at least $8$ whenever


$$
p\le t-7.
$$


Thus, for every edge of the active octet, its odd unit multiplier is independent of the low-bit-$6$ choice modulo $2^p$ for


$$
p\le31.
$$



In particular, using only $p=12$,


$$
u_\epsilon'\equiv u_\epsilon\pmod{2^{12}},
$$


and therefore, conservatively after division by $8$,


$$
\boxed{\alpha_{\mathcal O'}\equiv\alpha_{\mathcal O}\pmod{2^9}.}
\tag{9.2}
$$



This is more than sufficient for the new physical norm congruence modulo $2^{30}$.

---

# 10. The explicit normalized two-dimensional Gram lattice

Choose representatives of a paired pair of octets. Put


$$
x=\frac{\widetilde X_j}{2^9},\qquad
x'=\frac{\widetilde X_{j'}}{2^9},
\qquad
z=\frac{x'-x}{2}\in\mathbb Z.
$$



Before identifying the two weights, the paired norm divided by $2^{22}$ has Gram matrix


$$
G(\alpha,\alpha')
=
\begin{pmatrix}
(\alpha+\alpha')/2&\alpha'\\
\alpha'&2\alpha'
\end{pmatrix}.
\tag{10.1}
$$


Every entry is $2$-locally integral, since both weights are odd. Moreover,


$$
\boxed{\det G(\alpha,\alpha')=\alpha\alpha'\in\mathbb Z_{(2)}^\times.}
$$



Using (9.2), modulo $2^8$ this becomes


$$
G(\alpha,\alpha')\equiv
\alpha
\begin{pmatrix}1&1\\1&2\end{pmatrix}.
$$


Thus the normalized contribution is


$$
\boxed{
\alpha\,Q(x,z),\qquad
Q(x,z)=x^2+2xz+2z^2=(x+z)^2+z^2.
}
\tag{10.2}
$$



This is the requested small normalized Gram lattice. Its divisions are explicit:

1. divide the physical first coordinate by $2^9$;
2. divide the paired normalized-coordinate difference by $2$;
3. divide an octet weight by $8$;
4. divide the sum of two odd weights by $2$, if using (10.1).

None of these divisions is an unguarded modular inverse.

## 10.1 Exact local norm depth

On the $J=0/64$ paired blocks, $x$ is odd. Hence


$$
Q(x,z)\equiv1\pmod2
$$


for every $z$.

Since $\alpha$ is odd, each such sixteen-row block has


$$
\boxed{
v_2\!\left(\sum_{\text{that block}}X_j^2\right)=22.
}
\tag{10.3}
$$


The physical comparison is amply sufficient to preserve this exact valuation.

This includes the sixteen-row block through $j_*$.

It is a local block statement, not an upper bound for the whole norm.

---

# 11. A structural depth-$22$ theorem and the exact residual congruence

For a valuation-nine quartet, let


$$
t=\widetilde X_j/2^{10}.
$$


Its contribution is, to the needed precision,


$$
2^{20}\sigma_{\mathcal Q}t^2
=
2^{22}\beta_{\mathcal Q}t^2.
$$



For a remaining row $j\in\mathcal C$, put


$$
c_j=\widetilde X_j/2^{11}.
$$


Its contribution is exactly


$$
2^{22}c_j^2.
$$



Combining all three layers proves


$$
\boxed{2^{22}\mid D_{\rm raw}.}
\tag{11.1}
$$



More precisely, with one representative for each paired active block and each valuation-nine quartet,


$$
\boxed{
\frac{D_{\rm raw}}{2^{22}}
\equiv
\sum_{\mathcal A\text{-pairs}}\alpha\,Q(x,z)
+
\sum_{\mathcal B\text{-quartets}}\beta\,t^2
+
\sum_{j\in\mathcal C}c_j^2
\pmod{2^8}.
}
\tag{11.2}
$$



The row-proportionality errors for the short lifts have much higher valuation than required. The restriction to modulus $2^8$ after division by $2^{22}$ is the physical norm-comparison limit $30-22=8$.

For the mixed form, the same grouping gives at least:

* depth $22$ on active paired blocks;
* depth $22$ on valuation-nine quartets;
* depth $21$ on $\mathcal C$, from $11+10$.

Thus it also gives a structural


$$
2^{21}\mid E_{\rm raw},
$$


but it does not explain the full evaluated mixed depth $29$.

---

# 12. What this explains about the primitive norm loss

Since the first content is exactly $9$,


$$
v_2(D_{\rm raw})-18\ge12
$$


is now rigorous.

The new theorem explains four of these primitive norm bits:

* the shallowest first coordinates have depth $9$;
* their octets supply three norm bits;
* the paired parity support supplies a fourth.

The remaining eight bits are exactly the congruence


$$
\boxed{
\sum_{\mathcal A\text{-pairs}}\alpha\,Q(x,z)
+
\sum_{\mathcal B\text{-quartets}}\beta\,t^2
+
\sum_{\mathcal C}c_j^2
\equiv0\pmod{256}.
}
\tag{12.1}
$$



The new $45$-bit contraction establishes this congruence at the original word. The present proof does not yet derive it from shorter symbolic relations.

### Precise obstruction to a purely local explanation

The normalized block lattice is not highly divisible:

* its active $2\times2$ Gram blocks have unit determinant;
* its active odd-support blocks have odd normalized norm;
* its other displayed coefficients $\beta$ and $1$ are units.

In particular, active odd-support sixteen-row blocks have exact raw norm depth $22$, not $30$.

Therefore the next eight bits cannot be obtained by asserting another common factor in every block norm. They require correlations **between** blocks, imposed by the actual numerator and original binary word.

This does not prove that a larger grouping or finer observable quotient cannot succeed. It identifies what such a result must actually control.

### Concrete follow-on lemma

A sufficient next structural lemma is:

> For the actual first numerator, the normalized amplitude vector in (11.2), with the explicit odd weights $\alpha,\beta$, lies in the zero-norm locus modulo $256$; moreover, a higher physical lift identifies its first nonzero norm layer.

Unlike a generic automaticity statement, this specifies the exact integral quadratic form, its actual amplitude divisions, and the cross-block congruence still needing proof. The accepted contraction supplies finite corroboration of its first clause, not a proof for any infinite family.

No upper bound on $v_2(D_{\rm raw})$ follows yet.

---

# Part IV. Audit of A4’s objections and the actual higher-precision plan

## 13. Which objections remain valid

A4’s earlier polarization objection was correct at its stated scope. From divisibility of all norms by $2^k$, polarization alone gives mixed divisibility by $2^{k-1}$, not $2^k$. The new weighted-row arguments are separate proofs and do not invalidate that objection.

A4 was also correct that the arithmetic identities involving $36,72,124,160,284,196$ were not, by themselves, physical truncation proofs.

Turn 4 supplied the missing tail and locality derivations:

* central terms have valuation $v_2(s!)$;
* first-force terms at index $i$ have valuation at least
  

$$
v_2\!\left(\lfloor i/2\rfloor!\right);
$$


* the factorial exterior has valuation at least $v_2(t!)$;
* the normalized inverse filtration gives bandwidth $4(P-1)$;
* the reconstruction exponents give the stated Laurent bounds.

The newly executed operator/Schur calculation now supplies the actual $32$-bit finite inverse data and residual checks. Full forcing and reconstruction remain separate obligations, as the receipt correctly says.

The polynomial-relation Smith exponent has no role in proving the physical tail or the unit Schur inverse.

---

# 14. Denominator orders and guarded fallback

## 14.1 The actual current common exponent is $2n+197$

The conservative $32$-bit dimensions are


$$
m=124,\quad T=36,\quad I=72,\quad R=160,
$$




$$
L_0=284,\qquad K_0=196.
$$



The reconstructed form before target-specific cancellation is


$$
\boxed{
z^{-284}\left(
\frac{H_2(z)}{(1-z)^{2n+197}}
+
\frac{H_1(z)}{(1-z)^{n+1}}
\right).
}
$$



Here $160=m+T$ is an exterior-load support bound. It is not the surviving denominator order. The exponent $197$ comes from $K_0+1$.

A4’s orders $92,88$, and rising-factorial valuations $88,85$, are arithmetically valid under A4’s explicitly hypothetical common order $160$ and factors $68,72$. Those hypotheses have not been established for the present reconstructed representation. They must not be imported into it.

Both $n$-branches must be evaluated afresh. Every actual contact and $1-z$ division remainder must be retained. No unchanged $44/48$ or $68/72$ factor is assumed.

## 14.2 One-base fallback, only after branch and contact checks

If both new $n$-branches vanish and the contact shift $z^{284}$ is verified, the factor-independent one-base presentation has order at most $197$.

Its exact guards are


$$
v_2\bigl((a)^{\overline{197}}\bigr)=197,
$$




$$
v_2(197!)=193,\qquad
\max_r v_2\binom{197}{r}=6.
$$


Hence the universal fixed-divisor exponent is


$$
t_{197}=187,
$$


and the loss is


$$
197-187=10
$$


per column, or $20$ per quadratic payload.

Therefore:

* a physical Gram target of $32$ bits needs $52$ kernel bits;
* if one elects to use the quadratic dividend from true $32$-bit physical columns, the norm is determined modulo $2^{42}$ and the mixed form modulo $2^{41}$;
* those enlarged targets would require respectively $62$ and $61$ kernel bits in this fallback.

These are conditional guards for the representation actually obtained, not requests to repeat an accepted target.

If either $n$-branch survives, this one-base fallback is inapplicable as written.

## 14.3 Ratio and logarithmic guards

For exact depths $d=v_2(D_{\rm raw})$, $e=v_2(E_{\rm raw})$, reliable absolute $s$-bit precision in


$$
E_{\rm raw}/(2D_{\rm raw})
$$


requires


$$
\boxed{
M_E\ge s+d+1,\qquad
M_D\ge s+2d+1-e.
}
$$


A zero norm residue supplies no upper bound on $d$, so the current zeros alone do not close this guard.

Likewise the norm-relative logarithmic omission condition remains


$$
K_{\rm norm}+9-d-1\ge s,
$$


with


$$
K_{\rm norm}\ge2000b-138.
$$


The lower bound $d\ge30$ cannot be substituted as though it were an upper bound.

Absolute divisibility sufficient to omit a term from a fixed-modulus physical calculation is distinct from this norm-relative omission. Neither permits deleting that term from the whole same-index approximation error.

---

# Part V. New bounded verification, without huge binomials

## 15. A direct physical witness at $j_*$

A useful independent check is


$$
\boxed{X_{j_*}\bmod1024=512.}
$$



It can be evaluated without constructing any enormous binomial integer.

For each $0\le r\le81$:

1. Put $k_r=b-j_*-r$.
2. Compute the exact atom valuation using bit counts:
   

$$
\nu_r=
   v_2\binom N{j_*}
   +
   v_2\binom{a+80+k_r}{k_r}.
$$


3. Terms with $\nu_r\ge10$ vanish modulo $1024$.
4. For $\nu_r=8$, evaluate only the odd unit modulo $4$.
5. For $\nu_r=9$, evaluate only its parity.

The odd part of a factorial is evaluated through


$$
\Phi_p(m)=
\prod_{s\ge0}
g_p\!\left(
\left\lceil\frac{\lfloor m/2^s\rfloor}{2}\right\rceil
\right)
\pmod{2^p}.
$$


Here $p\le2$. One may use


$$
g_1(h)=1,\qquad
g_2(h)=1+2\binom h2\pmod4.
$$


All inversions are odd-unit inversions.

Finally compute


$$
\sum_{r=0}^{81}(A_f)_r\,\frac{h_r(j_*)}{2^8}\pmod4.
$$



### Inputs

* the original $N,a,b,j_*$;
* $A_f\bmod4$;
* at most $82$ bit-count valuations and bounded odd-factorial products.

### Expected verifiable output



$$
\boxed{
\widetilde X_{j_*}/2^8\equiv2\pmod4,
\qquad X_{j_*}\equiv512\pmod{1024}.
}
$$



This independently checks a physical coordinate, rather than rechecking only a parity-sum interpretation.

---

# 16. A new sixteen-row block check

A second, optional bounded check directly tests the new Gram mechanism on the block through $j_*$:


$$
j_*\mathbin{\oplus}
\epsilon_6 2^6
\mathbin{\oplus}\epsilon_{38}2^{38}
\mathbin{\oplus}\epsilon_{41}2^{41}
\mathbin{\oplus}\epsilon_{52}2^{52}.
$$


All sixteen indices lie in the original range.

For this block, the base kernel has exact valuation $10$: its low-byte contribution is $3$, and its accepted upper contribution is $7$. The same holds throughout the block.

### Inputs

* the original parameters;
* the retained short first numerator;
* these sixteen indices;
* odd-factorial arithmetic modulo at most $2^{12}$ for normalized $K$-units;
* physical first-coordinate residues modulo at most $2^{19}$.

### Nonunit guards

* Computing $K/2^{10}\pmod{2^{12}}$ from a raw $K$-residue would require $22$ raw bits. Direct odd-factorial unit evaluation avoids that subtraction of precision.
* Computing $\alpha=\sigma/8\pmod{2^9}$ requires $\sigma\pmod{2^{12}}$.
* Computing $z=(x'-x)/2\pmod{2^8}$ requires $x,x'\pmod{2^9}$.
* The exact first-coordinate content division uses nine bits; no even inverse is taken.

### Expected verifiable structural output

1. both octet weights satisfy
   

$$
\sigma\equiv8\pmod{16};
$$


2. their normalized weights agree modulo $2^9$;
3. the normalized matrix is
   

$$
\alpha G_0\pmod{2^8};
$$


4. its determinant is odd;
5. the sixteen-row physical norm has exact valuation $22$.

The actual residue of that norm divided by $2^{22}$ modulo $256$ is not supplied here and should not be invented. It must be odd.

This is a new small local verification. It is not a repetition of the global $45$-bit contraction, and it cannot by itself bound the global norm depth because other blocks can cancel it.

---

# 17. All-prime normalization and the whole error

The binary first-column content and the normalized block forms do not determine:

* odd-prime row contents;
* the least actual common clearer;
* the final gcd of the norm and mixed numerator;
* the actual primitive denominator.

Retain


$$
A_B=N_{B,1}^{T}\Omega N_{B,1},\qquad
H_B=N_{B,1}^{T}\Omega N_{B,2},
$$




$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
}
$$


With the least actual common clearer $d_B$, retain the actual primitive multiplier


$$
d_B^2/g_B.
$$



The whole same-index approximation form is still


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n.
}
$$



The normalization by $2^9$, $2^{10}$, or $2^{22}$ used in the local analysis is not a replacement for this final all-prime gcd.

Nor does any conclusion here extend from the single original $u_0$ word to an infinite original family. A4’s separate endpoint and differential-rank results have their own domains and do not supply that missing infinite all-prime comparison.

---

# 18. Proof-status ledger

| Statement | Status |
|---|---|
| New physical norm zero modulo $2^{30}$ | Accepted new finite computation |
| New physical mixed zero modulo $2^{29}$ | Accepted new finite computation |
| Four-support interpretation of the parity test | **Proved here** |
| First physical binary content exactly $9$ | **Proved**, using the supplied parity outputs |
| Second physical binary content at least $10$ | **Proved** |
| Primitive first-column binary norm loss at least $12$ | **Rigorous deduction** |
| Active rows form octets at $38,41,52$ | **Proved here** |
| Valuation-nine rows form quartets at $41,52$ | **Proved here** |
| Octet norm weight has exact valuation $3$ | **Proved here** |
| Low-bit-$6$ paired weights agree to the required precision | **Proved here** |
| Explicit normalized matrix $\alpha G_0$, $\det G_0=1$ | **Derived here**, with division guards |
| First global norm structurally divisible by $2^{22}$ | **Proved here** |
| Odd-support sixteen-row block norm has exact depth $22$ | **Proved here** |
| Remaining normalized global congruence modulo $256$ | Finite corroboration from the accepted new contraction |
| Structural explanation of those last eight bits | Open |
| First nonzero global norm layer | Open |
| Complete $32$-bit operator/Schur lift | Accepted new finite computation |
| Full new force/head/numerators | Not yet claimed |
| New $n$-branch disappearance and factor removals | Must be evaluated afresh |
| All-prime actual primitive denominator versus whole error on an infinite original sequence | Open |
| Irrationality or rationality of $e+\pi$ | Unresolved |

---

## Conclusion

The exact-content interpretation is now proved, so the new finite norm zero really implies a primitive binary norm loss of at least $12$.

The new mathematical result is an explicit original-row decomposition:


$$
\boxed{
\text{active octets}
\;\longrightarrow\;
\text{paired sixteen-row blocks}
\;\longrightarrow\;
\alpha
\begin{pmatrix}1&1\\1&2\end{pmatrix}.
}
$$


It proves structural norm depth $22$ and, on the first column’s odd support, exact sixteen-row block depth $22$.

That exact local depth sharpens the obstruction. The global depth at least $30$ is not another hidden content factor in each such block. It is a genuine cross-block cancellation, expressed by the explicit normalized congruence (12.1) modulo $256$.

The immediate remaining mathematical bottleneck is therefore


$$
\boxed{
\text{derive the cross-block weighted norm congruence structurally,
and obtain an actual upper bound for the global norm depth}.
}
$$



The new bounded arithmetic useful for auditing this advance is the direct $j_*$ coordinate evaluation, optionally followed by its sixteen-row normalized Gram check. Both use only bit-count valuations, short numerator data, and bounded odd-factorial/unit arithmetic.

The global research bottleneck remains


$$
\boxed{
\text{the actual all-prime primitive denominator against the whole
nonzero same-index error on an infinite original sequence}.
}
$$


No unconditional proof or disproof of the irrationality of $e+\pi$ has been obtained.
