> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4, Turn 10 — Audit of the original-word content theorem, certified precision gains, and sharper endpoint observability

## Executive assessment

The new sources resolve the two principal omissions identified in turn 9. A5 now supplies a physical tail/head argument, and its original-word carry analysis is substantially stronger than the earlier low-byte parity argument. Those new derivations must be assessed on their merits; the earlier absence of a source was not a disproof.

My conclusions are:

1. **A5’s original-word kernel theorem survives audit.** The common upper carry problem has minimum $7$, the full degree-$81$ kernel has sharp content $2^8$, and its active rows form quartets obtained by toggling bits $38$ and $41$. The common odd proportionality applies to the **whole kernel row**, not just an individual coordinate or numerator.

2. **There is a repairable error in A5’s depth-$20$ proof.** After dividing a complete column by $2^9$, its numerator coefficients need not remain integral. The proof must first apply whole-row proportionality to the original integral numerator and then pay nine bits when dividing. The available congruence is modulo $2^{25}$, so the divided congruence still holds modulo $2^{16}$, much more than the required modulo $4$. With this correction,
   

$$
X,Y\in2^9\mathbb Z^{b+1},
   \qquad
   2^{20}\mid \langle V,W\rangle
   \quad(V,W\in\mathbb ZX+\mathbb ZY)
$$


   is proved at the original index.

3. **The four support classes are correct and all are nonempty on the original finite domain.** An explicit supported witness for class $J\in\{0,4,64,68\}$ is
   

$$
(r,j)=(81-J,\ j_*+J).
$$


   Thus the supplied eight parity sums have their claimed interpretation. They establish
   

$$
\boxed{c_2(X)=9,\qquad c_2(Y)\ge10.}
$$


   In fact, the first column has valuation exactly $9$ at $j_*$, as well as at $j_*+64$.

4. **The new $45$-kernel-bit contraction is correctly guarded and is genuinely new evaluated precision.** It establishes
   

$$
\boxed{D_{\rm raw}\equiv0\pmod{2^{30}},\qquad
   E_{\rm raw}\equiv0\pmod{2^{29}}.}
$$


   These remain lower bounds, not exact depths. Since the first column now has exact content $9$, its primitive binary norm loss satisfies
   

$$
\boxed{\nu=v_2(D_{\rm raw})-18\ge12.}
$$



5. **A5’s physical cutoff tuple is now justified at its stated integral/unit scope:**
   

$$
\boxed{m=124,\quad T=36,\quad I=72,\quad R=160,\quad
   L_0=284,\quad K_0=196.}
$$


   The new operator/Schur receipt certifies that stage only. It does not certify an uncomputed force, head, reconstructed numerator, branch cancellation, or polynomial factor.

   The representation actually derived here has denominator exponent
   

$$
\boxed{2n+197}
$$


   before factor removal—not $2n+160$. Consequently, turn 9’s explicitly conditional $92/88$ consequences do not apply.

6. **A2’s compatible second lower lift, terminal coefficient $14$, and norm-only short-head radical reduction are valid at their stated scopes.** The repeated-block argument can be completed explicitly for every incoming interface. Together with the retained complete integral finite-normal-form theorem, it proves unbounded actual first-column content on every original arithmetic progression. It does not prove unbounded primitive norm loss.

7. **A1’s rank-four theorem and uniform observation bounds are proofs, not consequences of its finite receipt.** The receipt corroborates the algebra and finite coefficients. The local-branch argument proves differential rank exactly four; the inverse-lattice argument proves the original-branch observation exponents $(-6,-4)$.

   Two further results follow:
   - an exact three-case formula for the actual observation loss, determined by the primitive endpoint pair modulo $9$;
   - a sharper cumulative content bound,
     

$$
\boxed{
     c(V_N)\le
     \left\lfloor\frac{N+1}{3}\right\rfloor-1
     +v_3((2N+1)!)-v_3(N).
     }
$$


     In particular,
     

$$
\boxed{
     c_m\le
     \left\lfloor\frac m3\right\rfloor-5
     +v_3((2m-1)!).
     }
$$


     This is still linear, not logarithmic.

No code was executed for this report. Supplied receipts are used as finite execution evidence after auditing their mathematical interpretation and, where supplied, their source. No accepted bounded computation is proposed for repetition.

The irrationality or rationality of $e+\pi$ remains unresolved.

---

# I. Independent audit of A5’s original-word kernel theorem

## 1. Fixed parameters and complete columns

Throughout this part,


$$
b=9^{18}=150094635296999121,\qquad
n=4002b=600678730458590482242,
$$




$$
N=n+2,\qquad a=2n,
$$


and the physical row domain remains


$$
\boxed{0\le j\le b.}
$$



The retained complete twenty-bit presentations are


$$
F(z)=\frac{A_f(z)}{(1-z)^{a+81}},
\qquad
E(z)=\frac{A_e(z)}{(1-z)^{a+77}},
$$


with the accepted degree bounds and parity masks. The second presentation includes the complete retained second force, finite return, terminal factorial cancellation, and exterior $+1$.

For integer lifts of these numerators, suppressing the common physical row signs,


$$
X_j=\binom Nj[z^{b-j}]F(z),\qquad
Y_j=\binom Nj[z^{b-j}]E(z).
$$


The signs do not change contents or products $X_j^2,X_jY_j$.

Put


$$
C=a+80,\qquad B_r=b-r,\qquad S_r=C+B_r,
$$


and


$$
h_r(j)=\binom Nj\binom{C+B_r-j}{B_r-j},
\qquad 0\le r\le81.
$$


A negative lower index means zero. No unsupported row is added to the finite sum.

---

## 2. The min-plus recurrence computes the required valuation

For a supported row, Kummer’s theorem gives


$$
v_2(h_r(j))
=
\#\{\text{borrows in }N-j\}
+
\#\{\text{carries in }C+(B_r-j)\}.
$$



At scale $2^t$, with lower prefix $q=j\bmod2^t$, define


$$
\lambda_N=\mathbf1_{q>N\bmod2^t},\quad
\lambda_B=\mathbf1_{q>B_r\bmod2^t},\quad
\lambda_S=\mathbf1_{q>S_r\bmod2^t},
$$


and


$$
\kappa_t=
\left\lfloor
\frac{(C\bmod2^t)+(B_r\bmod2^t)}{2^t}
\right\rfloor.
$$


The valuation contribution is


$$
d_t=\kappa_t+\lambda_N+\lambda_B-\lambda_S.
$$



This is the correct carry-minus-borrow identity. The transition in the supplied audit source,


$$
\lambda'_A=\mathbf1_{\varepsilon+\lambda_A>A_t},
\qquad \varepsilon\in\{0,1\},
$$


is exactly ordinary binary subtraction. Therefore its accepted terminal state $(0,0,0)$ enforces the finite support rather than evaluating an unrestricted completion.

The recurrence is a pointwise valuation calculation. It is not a Gram evaluation.

---

## 3. Why all 82 shifts have one upper problem

The low bytes are


$$
N\bmod256=68,\qquad C\bmod256=212,
$$




$$
B_r\bmod256=209-r,\qquad S_r\bmod256=165-r.
$$


For every $0\le r\le81$,


$$
68<S_r\bmod256<B_r\bmod256,
\qquad \kappa_8=1.
$$



Thus the possible incoming masks at $t=8$ are precisely


$$
0,\ 4,\ 5,\ 7.
$$


Also, subtracting $r\le81$ from either $b$ or $C+b$ does not borrow out of its low byte. Hence all upper bits, including the upper $\kappa_t$, are identical for all 82 shifts.

The displayed min-plus table is therefore one common upper calculation over **all four possible incoming low-byte states**. Its important checkpoints are


$$
\begin{array}{c|rrrr}
t=38&0:4&2:5&6:6&7:5\\
t=41&0:4&2:6&6:6&7:8,
\end{array}
$$


and at $t=58$,


$$
0:7,\quad4:8,\quad6:17,\quad7:9.
$$



At that point the remaining bits of $B_r$ vanish. A $B_r$-borrow cannot subsequently clear, so masks $6,7$ cannot terminate acceptably. Mask $0$ completes at no further cost. Mask $4$ requires the additional $N$-borrows described by A5.

Consequently,


$$
\boxed{\text{every accepted upper path costs at least }7.}
$$



The supplied source checks the recurrence on the actual word, checks all 82 full-shift minima, and checks the indicated checkpoint values. Its arithmetic output is finite in scope, but the finite scope is exactly the one required for this fixed original-word theorem.

At the eighth scale every allowed mask contributes at least one:


$$
d_8=1+f(x)\ge1.
$$


Therefore


$$
\boxed{v_2(h_r(j))\ge8}
$$


for every original supported row and every shift.

---

## 4. Sharpness and the original attaining row

A5’s witness is


$$
j_*=
2^9+2^{10}+2^{23}+2^{27}+2^{31}
+2^{43}+2^{48}+2^{50}
=1416173266667008.
$$


It satisfies $0\le j_*\le b-81$.

Every set bit of $j_*$ is a set bit of $N$, so $\binom N{j_*}$ is odd. For


$$
k=b-81-j_*,
$$


the addition $C+k$ has eight carries. The supplied source independently evaluates the two binomial valuations and returns total valuation $8$.

Thus


$$
\boxed{
\min_{\substack{0\le r\le81\\0\le j\le b}}
v_2(h_r(j))=8.
}
$$



This is sharp content of the whole kernel lattice. It does not say that every shift separately has a valuation-$8$ coordinate.

---

# II. Active quartets, whole-row proportionality, and Gram depth

## 5. The active-quartet argument is valid

A row is active when at least one $h_r(j)$ has valuation $8$. Such a path must have low-byte cost $1$ and upper cost $7$.

At both checkpoints $t=38,41$, the remaining minimum cost from each listed state is $3$. The forward table then forces a cost-$7$ upper path to be in state $0$ at both checkpoints.

At bits $38$ and $41$, the three fixed bits are $(1,1,1)$ and the local carry contribution is zero. Starting from state $0$, either choice of the next $j$-bit returns to state $0$.

Therefore toggling either bit:

- preserves the valuation;
- preserves terminal acceptance;
- preserves the same shift’s support;
- preserves the original finite cutoff.

The active rows consequently split into the disjoint quartets


$$
j,\quad j\oplus2^{38},\quad j\oplus2^{41},\quad
j\oplus2^{38}\oplus2^{41}.
$$



The endpoint claim here is substantive: it follows from preservation of the accepted borrow path, not from assuming that a large bit toggle stays inside the interval.

---

## 6. Whole-row proportionality is stronger than equal valuations

Retain


$$
K(j)=\binom Nj\binom{a+b-j-1}{b-j},
$$


and the exact shift identity


$$
h_r(j)=\frac{K(j)}{2^7d}P_r(j),
\qquad d\ \text{odd},
$$


where


$$
P_r\in\operatorname{Int}_{\le81}(\mathbb Z).
$$



For every integer-valued polynomial $P$ of degree at most $81$,


$$
P(j+2^t)-P(j)\in2^{t-6}\mathbb Z
\qquad(t\ge7).
$$


Indeed, expanding in the binomial basis and applying Vandermonde reduces this to


$$
v_2\binom{2^t}{i}=t-v_2(i)\ge t-6,
\qquad1\le i\le81.
$$



Now let $j,j'$ be adjacent members of an active quartet. For a shift $r$ attaining valuation $8$ at these rows,


$$
v_2(K(j))+v_2(P_r(j))=15.
$$


Both terms are nonnegative. The translation difference is divisible by $2^{32}$, so the valuations of $P_r(j)$ and $P_r(j')$ agree. Hence


$$
v_2(K(j'))=v_2(K(j)).
$$



Thus


$$
u=\frac{K(j')}{K(j)}
$$


is an odd $2$-local unit, and the same $u$ works for every shift:


$$
\boxed{
h_s(j')-u h_s(j)\in2^{25}\mathbb Z_{(2)}
\quad(0\le s\le81).
}
$$



This proves proportionality of the entire row. Equality of the individual valuations alone would not have sufficed for the mixed Gram argument.

---

## 7. Universal kernel Gram depth $18$

Let $Z,Z'$ be two integer-numerator vectors in this kernel lattice.

- On a nonactive row, both are divisible by $2^9$, so their product is divisible by $2^{18}$.
- On an active quartet, divide them by $2^8$. The whole-row congruence remains valid modulo $2^{17}$, in particular modulo $4$. Adjacent normalized products are multiplied by $u^2\equiv1\pmod4$. Hence the four normalized products are equal modulo $4$, and their sum vanishes modulo $4$.

Therefore


$$
\boxed{
2^{18}\mid \sum_{j=0}^{b}Z_jZ'_j.
}
$$



This proves a universal lower Gram depth. Neither A5 nor this audit proves that depth $18$ is attained by a Gram product.

---

## 8. The parity lifts and pointwise depth $9$

The parity lifts are


$$
X_j^{(0)}
=\binom Nj\binom{a+b-j-1}{b-j-3},
\qquad
Y_j^{(0)}
=\binom Nj\binom{a+b-j-1}{b-j}.
$$



Their upper carry problem is the same one just audited. For the first lift,


$$
(B,C)\bmod256=(206,134),
$$


and for the second,


$$
(B,C)\bmod256=(209,131).
$$


Both have $S\bmod256=84$, $\kappa_8=1$, and the same upper bits.

For $X^{(0)}$, the first four bits contribute at least three events. The listed sixteen low-prefix costs verify this directly. For $Y^{(0)}$, the first three bits contribute at least two. The bit-$7$ event and the upper minimum $7$ are separate contributions. Hence


$$
\boxed{
X^{(0)}\in2^{11}\mathbb Z^{b+1},\qquad
Y^{(0)}\in2^{10}\mathbb Z^{b+1}.
}
$$



The coordinator’s original-word min-plus evaluation returns minima $11,10$, respectively. The structural argument needs their lower bounds; the exact minima are supplied finite arithmetic.

Write


$$
A_f=z^3(1-z)^{78}+2B_f,
$$




$$
(1-z)^4A_e=(1-z)^{81}+2B_e.
$$


Then


$$
X=X^{(0)}+2Z_f,\qquad
Y=Y^{(0)}+2Z_e,
$$


where $Z_f,Z_e$ are integral kernel vectors. Thus


$$
\boxed{X,Y\in2^9\mathbb Z^{b+1}.}
$$


On a nonactive row, the stronger conclusion is


$$
\boxed{X_j,Y_j\in2^{10}\mathbb Z.}
$$



---

## 9. Repair of A5’s division step and proof of Gram depth $20$

A5 writes that after division by $2^9$, the complete columns “remain integer-numerator kernel vectors.” That assertion is not justified and is generally false. Integral values after division do not imply integral coefficients in the original numerator basis.

The correct argument is:

1. The undivided complete short columns have integral numerators of degree at most $81$, after putting the second over the common denominator.
2. Whole-row proportionality therefore gives
   

$$
X_{j'}-uX_j,\quad Y_{j'}-uY_j
   \in2^{25}\mathbb Z_{(2)}.
$$


3. Their values are divisible by $2^9$. Dividing the displayed congruences pays nine bits:
   

$$
\frac{X_{j'}}{2^9}-u\frac{X_j}{2^9},
   \quad
   \frac{Y_{j'}}{2^9}-u\frac{Y_j}{2^9}
   \in2^{16}\mathbb Z_{(2)}.
$$


4. Modulo $4$, the normalized mixed products are constant across the quartet, because $u^2\equiv1\pmod4$.

On nonactive rows, each product is already divisible by $2^{20}$. On active quartets, division of the product by $2^{18}$ leaves a four-term sum divisible by $4$.

Therefore the conclusion is valid:


$$
\boxed{
2^{20}\mid\sum_{j=0}^{b}V_jW_j
\qquad(V,W\in\mathbb ZX+\mathbb ZY).
}
$$



The repair uses the actual available proportionality precision. It does not silently preserve numerator integrality after division.

---

# III. The four support classes and exact actual first-column content

## 10. Derivation of the low-byte support classification

Put


$$
u=81-r,\qquad0\le u\le81.
$$


Then


$$
B_r\bmod256=128+u,\qquad C\bmod256=212.
$$



For the low byte to contribute exactly one event, the first seven bits must contribute none.

Let $q=j\bmod128$. No weight borrow in these bits requires


$$
q\ \text{to be a bit-subset of }68,
$$


so


$$
q=J\in\{0,4,64,68\}.
$$



No addition carry in these seven bits requires


$$
(u-J)\bmod128
$$


to be disjoint from $84=64+16+4$. Such a residue is at most $43$. If $u<J$, the residue is at least $60$, which is impossible. Hence there is no lower borrow, and


$$
u=J+k,\qquad k\mathbin{\&}84=0.
$$


Equivalently,


$$
\boxed{u\mathbin{\&}16=0,\qquad u\mathbin{\&}68=J.}
$$



The eighth bit of $j$ may be $0$ or $1$. The resulting low prefixes are exactly


$$
J,\qquad J+128.
$$


They enter the common upper problem in masks $0$ and $5$, respectively.

For a fixed $J$, all eligible shifts therefore have:

- the same low cost $1$;
- the same two possible low prefixes;
- the same incoming upper states;
- the same upper acceptance and cost-$7$ conditions.

After division by $2^8$, every nonzero kernel value on this support is odd and therefore equals $1$ modulo $2$. Thus all eligible shifts have the same support function modulo $2$.

Different $J$’s have disjoint supports because their low prefixes differ.

This proves the asserted four-class description.

---

## 11. Nonempty original supports: explicit witnesses

Nonemptiness should not be left implicit in an upper-path calculation.

For each


$$
J\in\{0,4,64,68\},
$$


take


$$
r_J=81-J,\qquad j_J=j_*+J.
$$


Then


$$
b-r_J-j_J=b-81-j_*.
$$


So the second binomial has exactly the same eight-carry lower argument as the original witness.

Also, $J$ is a bit-subset of the low byte of $N$, while $j_*$ has zero low byte and is already a bit-subset of $N$. Consequently


$$
\binom N{j_J}\ \text{is odd}.
$$


Thus


$$
\boxed{v_2(h_{r_J}(j_J))=8.}
$$



All four pairs lie in the original finite support. The shifts are


$$
81,\ 77,\ 17,\ 13,
$$


which belong to the respective displayed shift sets.

This independently closes the support theorem’s nonemptiness obligation.

---

## 12. Interpretation of the eight supplied parity sums

For


$$
\chi_J(B)=\sum_{r\in\mathcal R_J}B_r\pmod2,
$$


the support theorem now proves


$$
Z/2^8\not\equiv0\pmod2
\iff
(\chi_0,\chi_4,\chi_{64},\chi_{68})(B)\ne0.
$$



The supplied calculation returns


$$
\chi(B_f)=(1,0,1,0),\qquad
\chi(B_e)=(0,0,0,0).
$$



These are new evaluated sums on the retained numerator arrays, not inferred from Gram zeros. Since the support theorem has now been audited, their consequences are rigorous:


$$
\boxed{c_2(X)=9,\qquad c_2(Y)\ge10.}
$$



More specifically, at $j_*$, class $J=0$ gives


$$
Z_{f,j_*}/2^8\equiv1\pmod2.
$$


Since $X_{j_*}^{(0)}/2^9$ is even,


$$
X_{j_*}/2^9\equiv1\pmod2.
$$


Thus $j_*$ is an actual exact-content witness for the first column. Class $J=64$ gives another at $j_*+64$.

All these statements transfer to the complete physical columns: changing a coordinate by a multiple of $2^{20}$ cannot change its valuation $9$, nor its divisibility by $2^{10}$.

The second column’s exact content remains undetermined.

---

# IV. Audit of the new $45$-kernel-bit contraction

## 13. Physical comparison precision

Let $x,y$ be the actual complete columns and $\widetilde x,\widetilde y$ their retained twenty-bit integer lifts:


$$
x=\widetilde x+2^{20}h,\qquad
y=\widetilde y+2^{20}k.
$$



Using the proved lower contents $9,9$,


$$
x^Tx-\widetilde x^T\widetilde x
=
2^{21}\widetilde x^Th+2^{40}h^Th
\in2^{30}\mathbb Z,
$$


and


$$
x^Ty-\widetilde x^T\widetilde y
=
2^{20}h^T\widetilde y+
2^{20}\widetilde x^Tk+
2^{40}h^Tk
\in2^{29}\mathbb Z.
$$



The stronger second-column content $10$ does not improve the mixed minimum, because the term $2^{20}\widetilde x^Tk$ is guaranteed only depth $29$.

Therefore


$$
\boxed{
D_{\rm raw}\equiv\widetilde D\pmod{2^{30}},\qquad
E_{\rm raw}\equiv\widetilde E\pmod{2^{29}}.
}
$$



These are the exact comparison ranges used by the new source.

---

## 14. Denominator divisions and odd-unit inversions

The retained fixed-divisor normalizations are


$$
S_{ff}=2^{14}d_f^2\widetilde D,
\qquad
S_{fe}=2^{16}d_fd_e\widetilde E,
$$


where $d_f,d_e$ are odd.

The new source:

- evaluates the shared transport at $45$ bits;
- retains $S_{ff}$ modulo $2^{44}$, sufficient for $30$ bits after division by $2^{14}$;
- retains $S_{fe}$ modulo $2^{45}$, sufficient for $29$ bits after division by $2^{16}$;
- checks those exact divisibilities before shifting;
- checks rising-factorial valuations $(80,77)$;
- inverts only the odd denominator units;
- checks reduction to the earlier $22/21$-bit outputs.

The deliberate reduction of the norm numerator to $44$ bits is correct. A $45$-bit numerator could yield an additional lifted norm bit, but the current physical comparison would not certify that extra bit.

The supplied receipt returns


$$
S_{ff}\equiv0\pmod{2^{44}},\qquad
S_{fe}\equiv0\pmod{2^{45}},
$$


and hence


$$
\boxed{
D_{\rm raw}\equiv0\pmod{2^{30}},\qquad
E_{\rm raw}\equiv0\pmod{2^{29}}.
}
$$



The retained transport has 71 consumed digits and terminal state $000$, preserving $0\le j\le b$. The source reuses the previously audited transport implementation; this is a new payload-precision evaluation, not an independent implementation of transport.

No higher physical producer is claimed or needed for this particular dividend.

---

## 15. Exact content now identifies the primitive norm normalization

Since


$$
c_2(X)=9,
$$


the vector


$$
x_{\rm prim}=X/2^9
$$


is binary-primitive. Thus


$$
D_{\rm raw}=2^{18}x_{\rm prim}^Tx_{\rm prim},
$$


and


$$
\boxed{
\nu=v_2(x_{\rm prim}^Tx_{\rm prim})
=v_2(D_{\rm raw})-18\ge12.
}
$$



This is a lower bound for an exactly specified primitive norm. It is not an exact value of $\nu$, because the norm residue is still zero at its highest evaluated precision.

The first nonzero norm layer, a ratio at prescribed precision, and a norm-relative logarithmic omission certificate remain unevaluated.

---

# V. The physical $32$-bit construction

## 16. Tail estimates now supplied by A5

### 16.1 Central tail

For $\delta=0,1$,


$$
v_2\!\left(\frac{2^s(s!)^2}{(2s+\delta)!}\right)=v_2(s!).
$$


After cancellation, the remaining denominator is odd. Since


$$
v_2(36!)=34,
$$


every central term with $s\ge36$ vanishes modulo $2^{32}$.

Thus


$$
\boxed{T=36}
$$


is safe without an even modular inverse.

### 16.2 First-force head

For the central prefactor,


$$
v_2(B_\ell)\ge
v_2\!\left(\left\lceil\frac\ell2\right\rceil!\right).
$$


The falling product of length $i-\ell$, combined with $\binom i\ell$, gives


$$
v_2(\text{summand})
\ge
v_2(i!)-v_2(\ell!)
+
v_2\!\left(\left\lceil\frac\ell2\right\rceil!\right).
$$


Using


$$
v_2(\ell!)-
v_2\!\left(\left\lceil\frac\ell2\right\rceil!\right)
\le\left\lfloor\frac\ell2\right\rfloor
$$


and


$$
v_2(i!)-\left\lfloor\frac i2\right\rfloor
=
v_2\!\left(\left\lfloor\frac i2\right\rfloor!\right),
$$


each original first-force term with $i\ge72$ has valuation at least $34$.

Hence


$$
\boxed{I=72}
$$


is a tail theorem, not an extrapolation from a finite zero interval.

### 16.3 Exterior tail

For


$$
v_t=(b+1)\cdots(b+t),
$$




$$
v_2(v_t)\ge v_2(t!).
$$


Thus only $t<36$ must be retained modulo $2^{32}$. A bandwidth-$m$ operator enlarges this to length


$$
\boxed{R=m+36.}
$$



---

## 17. Operator bandwidth and the supplied Schur stage

The normalized operator is identity plus an even operator of bandwidth at most four. Therefore


$$
(I+Q)^{-1}\equiv\sum_{k=0}^{31}(-Q)^k\pmod{2^{32}},
\qquad Q\in2R,
$$


has bandwidth at most


$$
\boxed{m=4(32-1)=124.}
$$



The new operator source implements this integral divided-power construction. Its checks have the claimed dimensions:

- $248$ filtration checks;
- $249=2m+1$ symbol/inverse residual checks;
- $30752=2m^2$ entries in the two inverse-product checks;
- $15376=m^2$ transpose entries;
- $15376$ padded-zero entries;
- $15376$ unit-parity entries.

The relevant arrays and indices are internally consistent:

- $F$ has shape $248\times124$;
- its largest binomial lower index is $248+123=371$;
- the independent backward solve $Z$ has shape $372\times124$;
- the padding $Z[:124]=0$ leaves the $248$-row part used in the transpose comparison;
- the index $m+t-s$ used in $G$ ranges exactly from $0$ through $247$.

The matrix $S$ is checked to be identity modulo $2$. Consequently every pivot in the displayed elimination is odd, and its inverse is integral over $\mathbb Z_2$. Both inverse products and the independently formed transpose relation are checked modulo $2^{32}$.

This certifies the new operator and finite endpoint inverse at the reported precision. It does **not** yet certify the force-dependent endpoint right-hand sides, the complete head, or either reconstructed physical column.

---

## 18. Correct Laurent dimensions and reconstruction exponent

With


$$
m=124,\quad I=72,\quad R=160,
$$


the safe offsets are


$$
\boxed{L_0=284,\qquad K_0=196.}
$$



The source exponents are


$$
r-s+e+L_0,\qquad K_0-\mathrm{extra}-e,
$$


with $e\le s\le m$, and $\mathrm{extra}=0$ or $I$. The retained head and exterior support bounds make both exponents nonnegative. The head numerator has $r\le I-1$; the negative exterior range ends at $r=-1$. Thus the resulting $2n$-branch polynomial has degree at most


$$
L_0+K_0-1=479,
$$


hence length $480$.

The reconstruction increases the denominator exponent by one and the numerator degree by at most two. Explicitly, for


$$
g(z)=z^{-L_0}\frac{H(z)}{(1-z)^\lambda},
$$


the operator corresponding to $(k-b)g_k-g_{k-1}$ is


$$
(z\partial_z-b-z)g
=
z^{-L_0}
\frac{
z(1-z)H'
-(L_0+b+z)(1-z)H
+\lambda zH
}{(1-z)^{\lambda+1}}.
$$


Its numerator degree is at most $\deg H+2$.

Accordingly the reconstructed representation is


$$
\boxed{
z^{-284}
\left(
\frac{H_2(z)}{(1-z)^{2n+197}}
+
\frac{H_1(z)}{(1-z)^{n+1}}
\right),
}
$$


with safe lengths


$$
\deg H_2\le481\quad(\text{length }482),
\qquad
\deg H_1\le285\quad(\text{length }286).
$$



The independent-jet dimensions are also consistent:


$$
\mathrm{JET}=247,\qquad \mathrm{MAX}=371,
$$


and the largest required inverse-power coefficient is


$$
247+284=371+160=531.
$$



The full principal-part/jet range is


$$
-284\le k\le247.
$$


The terminal relation must retain


$$
\boxed{-b\,g_0-1,}
$$


not merely $-b\,g_0$. This is the complete exponential exterior correction, not an additional copy of it.

---

## 19. What has not been inherited

No new computation has yet established either reconstructed $n$-branch to be zero modulo $2^{32}$.

Likewise, neither the old factor counts nor the old short orders persist automatically. In this representation:

- denominator exponent before removal: $2n+197$;
- factors $44,48$, **if newly proved**, would leave orders $153,149$;
- orders $81,77$, **if newly proved**, would require factors $116,120$.

Turn 9’s $92/88$ calculation assumed a different, explicitly conditional order-$160$ presentation. It is inapplicable here.

The required new decisions are coefficientwise:

1. both reconstructed $n$-branches;
2. the $z^{284}$ contact factor if a branch is removed;
3. the actual multiplicity of $1-z$, with every division remainder retained.

Monic division by $z$ or $1-z$ causes no binary precision loss. The issue is whether the divisibility is true.

---

## 20. Fixed-divisor fallback

If the new $n$-branches vanish and the contact factor is checked, both surviving numerators have degree at most $197$ over


$$
(1-z)^{a+197}.
$$



For $R=197$,


$$
v_2(197!)=193.
$$


Because $197$ is odd, there is no carry at bit $0$ in a decomposition $197=r+(197-r)$; there can be at most six carry positions below the top bit. The decomposition


$$
197=70+127
$$


attains six. Hence


$$
\max_r v_2\binom{197}{r}=6,
$$


and the universal fixed-divisor exponent is


$$
\boxed{t_{197}=187.}
$$



For the actual $a$, its residue modulo $512$ is $132$, so the rising factorial has the valuations of the interval $132,\ldots,328$:


$$
v_2((a)^{\overline{197}})
=99+50+25+12+6+3+1+1
=\boxed{197}.
$$


There is no multiple of $512$ in this interval.

Thus the fixed-divisor loss is $10$ per column, or $20$ per Gram payload. A $32$-bit Gram target needs $52$ kernel bits, exactly as A5 states.

A further conditional dividend is available once the **true** $32$-bit columns exist. Their known contents imply comparison precision


$$
D_{\rm raw}\pmod{2^{42}},\qquad
E_{\rm raw}\pmod{2^{41}}.
$$


In the unshortened $197$-order fallback, those targets require $62$ and $61$ kernel bits, respectively. A shared $62$-bit transport has payload degree at most $394$ and envelope


$$
\left\lfloor\frac{394}{2^t}\right\rfloor+122.
$$



These are conditional future guards, not evaluated residues or instructions to rerun an accepted calculation. If an $n$-branch survives, it must remain in the observable and this one-base fallback does not apply as written.

---

# VI. Audit of A2’s second lower lift and complete-column content theorem

## 21. Compatible $\mathsf D_2$ and the literal-lift correction

The phase is


$$
n\equiv29(7+24\cdot29)=20387\pmod{29^3}.
$$


For


$$
c_s(n)=s![z^s]\phi(z)^{-n},\qquad
\phi(z)=1-z+\frac{z^2}{2},
$$


the exact recurrence


$$
c_{s+1}=(s+n)c_s
-s\left(n+\frac{s-1}{2}\right)c_{s-1}
$$


is correct.

For $s<29$, the logarithmic expansion gives the stated compatible coefficients


$$
d_s=
24q_s+\frac{49}{2}s!
\sum_{r=1}^{s-1}\frac{a_ra_{s-r}}{r(s-r)}
\pmod{29}.
$$


At $s=29$, the nonlinear terms have the additional factorial valuation, so only the linear term remains modulo $29^3$. The residues


$$
28!\equiv-1+18\cdot29,\qquad
a_{29}\equiv1+14\cdot29\pmod{29^2}
$$


give $d_{29}=4$.

The recurrence then gives


$$
d_{29+r}
=(r-1)!(7\cdot21^r+4\cdot9^r),
\qquad1\le r\le29.
$$


For $59\le s\le86$, the Frobenius reduction supplies the extra factor of $29$, and for $s\ge87$, $v_{29}(s!)\ge3$. Thus the support really ends at $58$.

The conversion


$$
d_s^{\rm old}=d_s-7s!9^{s-1}\pmod{29},
\qquad1\le s<29,
$$


correctly compensates for the different literal lift of $\mathsf D_1$.

The coordinator’s 120-symbol checks corroborate these formulas and the lift conversion at their finite scope. The proof of the infinite zero tail comes from the factorial/Frobenius argument, not from checking 120 symbols.

The corrected actual low coefficients remain


$$
\boxed{21,-21\pmod{29}.}
$$


The receipt’s low sum $9$ and $K_{34}=12$ give $9\cdot12=21\pmod{29}$, consistently with turn 9.

---

## 22. Terminal coefficient $14$

The original terminal row is


$$
Z_{w,b}=bW_b\theta_{b-1}.
$$


Using the actual baseline head,


$$
\theta_{b-1}/f_0^0\equiv F_{26}\equiv22\pmod{29},
$$


and $b\equiv27\pmod{29}$, gives


$$
bF_{26}\equiv14\pmod{29}.
$$



Therefore


$$
\boxed{
\frac{Z_{w,b}}{29^3}
\equiv14\cdot29\,A_0\,\frac{W_b}{29^4}
\pmod{29^2}.
}
$$



This does not assume $v_{29}(W_b)=4$. If the weight is deeper, its quotient residue may vanish.

The coordinate’s square is zero modulo $29^2$, so it disappears from this particular divided norm. It does **not** disappear from the next column.

---

## 23. The short-head radical: valid for the norm, not the column

The baseline divisibility extends to head indices $0\le r\le291$. The relevant lower two-digit minuends remain at least $547$, while a weight index with no low weight borrow is at most $205$. The upper/lower sums therefore force a low carry, and the retained higher configuration supplies the other two events.

For the first lower correction, A2 correctly separates:

- $1\le t<29$, where $\binom{-n}{t}$ supplies an additional factor;
- $t=0,29$, where the surviving head offsets are $r=29k$, $0\le k\le10$;
- the reconstruction row factors, which must be retained in the exceptional cases.

This is not a claim that arbitrary positive-offset atoms have three factors. Its scope is the actual coefficient-weighted normal ordering with the displayed row factors.

The radical calculation then uses the exact identity


$$
\binom{2n+r-1}{r}
\binom{2n+b-1-j}{K-r}
=
\binom{2n+b-1-j}{K}
\frac{2n}{2n+r}\binom Kr.
$$


For $r=29k$, the remaining denominator $14+k$ is a unit for $0\le k\le10$. The multiplier depends only on the first two digits $d,e$, not on the high continuation.

Thus the high-interface cancellation remains proportional to the established difference


$$
\mathscr T_{\rm I}-\mathscr T_{\rm II}.
$$


The corrected complete low coefficients are $21,-21$. A2’s displayed pair $(10,19)$ is a scalar multiple of that pair:


$$
(21,8)=5(10,19)\pmod{29}.
$$


Since its $K_a$ is an unspecified common low scalar, this normalization difference does not invalidate the radical cancellation. It should not, however, replace the corrected actual coefficients in a normalized numerical formula.

Consequently


$$
\boxed{
S^T(Ba/29^3)=0\pmod{29}
}
$$


for the stated head range.

The complete perturbation formula retains


$$
29Ba
$$


in the next column. Pairing with the leading vector removes that perturbation from the first divided norm, yielding


$$
\boxed{\eta=A_0^2\eta_{\rm short}.}
$$



The compatible second lower correction and the actual second finite endpoint return remain in $\eta_{\rm short}$. Neither has been eliminated by the radical theorem, and their combined next-norm value is not supplied.

---

## 24. Repeated blocks: explicit audit of every incoming interface

At the three decisive positions, the stable digits are


$$
W:(7,3,9),\qquad B:(28,0,20),\qquad C:(15,6,18).
$$



Let the incoming weight borrow, lower-index borrow, and addition carry be


$$
\alpha,\beta,\gamma\in\{0,1\}.
$$


For the chosen digit $d$ of $j$, write


$$
\alpha'=\mathbf1_{d+\alpha>W},
\qquad
\beta'=\mathbf1_{d+\beta>B},
$$




$$
k=B-d-\beta+29\beta',
\qquad
\gamma'=\mathbf1_{C+k+\gamma\ge29}.
$$


The valuation contribution is $\alpha'+\gamma'$.

### First decisive digit

Here $W=7,B=28,C=15$.

If there is no weight borrow, then $d\le7$. Consequently $\beta'=0$ and


$$
k=28-d-\beta\ge20.
$$


Thus $C+k+\gamma\ge35$, forcing an addition carry.

So this digit contributes at least one event for every incoming interface.

### Middle and last decisive digits

Suppose the middle digit, with $W=3,B=0,C=6$, contributes no event. Then $d\le3$.

If $\beta'=1$, then


$$
C+k+\gamma=35-d-\beta+\gamma\ge31,
$$


contradicting absence of an addition carry. Therefore $\beta'=0$, which forces $d=\beta=0$.

The lower borrow into the last digit is therefore zero. At that last digit,


$$
W=9,\quad B=20,\quad C=18.
$$


Absence of a weight borrow gives $d\le9$, so


$$
k=20-d\ge11,
$$


and $C+k\ge29$, forcing an addition carry.

Thus the middle and last digits cannot both contribute zero events.

We have proved, without restricting the incoming flags,


$$
\boxed{\text{each prescribed block contributes at least two events}.}
$$



---

## 25. Bounded offsets and complete solved charges

The offset argument also survives audit.

The relevant multiplication remainders below the three decisive positions are


$$
20387\quad\text{and}\quad16385.
$$


They remain strictly between the relevant three-digit boundaries under the full incoming multiplication-carry bounds. The lower three digits of $\beta$ are $5044$, so a propagated shift $-1,0,1$ in $b+v$ does not alter the decisive digits either.

Choosing


$$
29^m>87K+2
$$


places every bounded offset below the repeated blocks. It may induce a carry or borrow into the first block, but the preceding interface proof covers all such possibilities. Each later block is covered again independently; no assumption that the interface resets to zero is needed.

The passage from atoms to the complete column uses the retained finite-normal-form theorem at its exact precision-dependent scope:


$$
M=29K-1,\qquad L=58K+2,
$$


with all head and exterior offsets inside the stated bounds and **all solved endpoint charges $29$-integral**. This integrality is essential: an uncontrolled denominator in a charge could consume the block valuations.

Under that established theorem, every term of the complete $K$-precision normal form is divisible by $29^{2r}$. There is no cancellation of denominators to be assumed after summation.

At the original terminal row $j=b$, the same block forces weight borrows at its first and third decisive positions. Hence


$$
v_{29}(W_b)\ge2r,
$$


and the integral terminal contact coordinate preserves the bound.

Therefore


$$
2r\ge K\quad\Longrightarrow\quad
Z_w\in29^K\mathbb Z_{29}^{b+1}.
$$



This includes the original terminal row and the complete finite return.

---

## 26. Realization on every original arithmetic progression

The retained principal-unit parametrization realizes every compatible finite continuation above the fixed six-digit prefix.

Given $u\equiv u_0\pmod h$, choose


$$
m\ge6+v_{29}(h)
$$


and retain the corresponding lower prefix of $b(u_0)$. Append the required repeated blocks. The resulting congruence for $u$ modulo a power of $29$ is compatible with $u\equiv u_0\pmod h$, so the Chinese remainder theorem supplies infinitely many nonnegative original indices.

Taking sufficiently large members ensures that all finite-memory lengths remain below the original cutoff.

Thus A2’s conclusion is valid:


$$
\boxed{
\forall u_0,h,R,\quad
\text{infinitely many original }u\equiv u_0\pmod h
\text{ have }c\ge R.
}
$$



It follows that no original arithmetic progression is eventually characterized by $c=1$.

This theorem concerns the complete corrected first column. It does not imply unbounded primitive norm loss, and it does not evaluate the complete mixed-force relative alignment.

---

# VII. A1’s rank, recurrence, and observation theorem

## 27. Differential rank exactly four

The quartic coordinate


$$
P(x,t)=t^4-t^3+xt-2x=0,
\qquad \sigma^2=t(2-t),
$$


and the outputs


$$
\mathcal A=\frac{\sigma t}{-3t^2+10t-6},
\qquad
\frac{\mathcal B}{\mathcal A}=\frac{t(t-1)}{2-t}
$$


are consistent with the reciprocal identities and the distinguished branch $t(0)=\sigma(0)=1$.

The displayed polynomial system follows by multiplication by $P_t$ and differentiation in the basis


$$
\frac{\sigma}{P_t}(1,t,t^2,t^3).
$$


The supplied receipt checks the matrix identities and determinant factors exactly. Its finite endpoint checks corroborate that the recurrence uses the actual varying-$m$, same-$A$ adjacent pair.

The rank lower bound does not follow from those checks. It follows from A1’s local branch proof:

- one branch has $\mathcal A=1+O(x)$;
- three branches near $t=0$ have nonzero coefficients at exponents
  

$$
\frac12,\quad\frac56,\quad\frac76;
$$


- their Fourier coefficient matrix is nonsingular;
- these three branches are independent, and the branch with nonzero constant term is independent of them.

The expansion coefficients $1,\frac53,\frac{193}{72}$ are correct. Connectivity of the algebraic covering makes these branches analytic continuations of the same output. Any rational homogeneous differential equation for $\mathcal A$ must therefore have at least four independent solutions.

Combined with the anti-invariant upper bound,


$$
\boxed{\operatorname{rank}_{\rm diff}(\mathcal A)=
\operatorname{rank}_{\rm diff}(\mathcal A,\mathcal B)=4.}
$$



This does not alter the retained infinite exact ternary-section-rank obstruction.

---

## 28. Recurrence and uniform observation

The coefficient recurrence has no nonnegative forward denominator zero. Its singular reverse step at $n=0$ is correctly handled by


$$
V_0=(1,1)^T,\qquad V_1=(-5,-4)^T.
$$


No inverse transition at $n=0$ is used.

The same-index observation matrix $O(n)$ has the displayed determinant


$$
\det O(n)=
\frac{n(3n-1)(3n+1)(8n+5)}
{(n+1)(2n+1)^2(6n+1)}.
$$


The lower and upper observation inequalities use bounds on the matrix entries and the adjugate, not determinant valuation alone. They are valid for every vector in $\mathbb Q_3^2$.

On the original branch,


$$
A=2m-1=4^j-1.
$$


Since $j\equiv81\pmod{243}$, LTE gives


$$
v_3(A)=1+v_3(j)=5.
$$


With $n=m-1$, the other relevant factors are units, and the smallest entry valuation is $-6$, while the determinant valuation is $-10$. Thus the local Smith exponents are exactly


$$
\boxed{(-6,-4).}
$$


Consequently


$$
c(V_{m-1})-6\le c_m\le c(V_{m-1})-4.
$$



The finite sample $m=851$ confirms one instance of the algebra. It does not prove the uniform statement or evaluate an original-window tuple.

---

# VIII. Two stronger consequences for the actual endpoint projection

## 29. Exact three-case observation loss

The observation interval can be sharpened to an exact direction-dependent formula.

Write


$$
n=m-1,\qquad A=2n+1,
$$


and abbreviate


$$
F=394n^2+367n+78,\qquad
G=52n^2+46n+9,
$$




$$
H=22n+7,\qquad I=4n+1,\qquad J=8n+5.
$$



Direct inversion of the displayed $O(n)$ gives


$$
w_n=
-\frac{A}{3n(3n+1)J}
\bigl(3(n+1)I\,a_m+G\,b_m\bigr),
$$




$$
s_n=
-\frac{A}{3(3n-1)(3n+1)J}
\bigl(3(n+1)H\,a_m+F\,b_m\bigr).
$$



All denominator factors outside the displayed $3$ are units on the original branch.

Let


$$
L=3(n+1)I\,a_m+G\,b_m.
$$


The exact factorization audited by A1 gives


$$
HG-FI=-3(6n+1)(3n+1)J.
$$


Eliminating $b_m$ between the two bracketed expressions therefore leaves a unit times $9a_m$. Hence


$$
c(V_{m-1})
=
4+\min\{v_3(L),\,2+v_3(a_m)\}.
$$



Now put


$$
a_m=3^{c_m}\bar a,\qquad b_m=3^{c_m}\bar b,
\qquad \min(v_3(\bar a),v_3(\bar b))=0.
$$


Because $G$ is a unit, primitivity implies


$$
c(V_{m-1})-c_m
=
4+\min\!\left\{2,\,
v_3\bigl(3(n+1)I\bar a+G\bar b\bigr)\right\}.
$$



On the original branch $n\equiv4\pmod9$. Thus


$$
3(n+1)I\equiv3,\qquad G\equiv-1\pmod9.
$$


We obtain the exact formula


$$
\boxed{
c(V_{m-1})-c_m
=
4+\min\{2,v_3(\bar b-3\bar a)\}.
}
\tag{29.1}
$$



Equivalently:

- loss $4$ iff $\bar b\not\equiv0\pmod3$;
- loss $5$ iff $\bar b\equiv0\pmod3$ but
  $\bar b\not\equiv3\bar a\pmod9$;
- loss $6$ iff $\bar b\equiv3\bar a\pmod9$.

This is an exact actual projection/content law. It does not assert which case occurs at an unevaluated original index.

---

## 30. A sharper cumulative transition bound

A1’s uniform entry estimate pays one factor of $3$ at every step. The recurrence shows that this is unnecessary in two residue classes.

Let $T(n)$ be its two-coordinate transition and $n\ge1$.

### Case $n\equiv0\pmod3$

The numerators of both coefficients in the $s_{n+1}$ row are divisible by $3$, and the formulas for $u_n$ are integral. Since $n+1$ and $2n+1$ are units, every entry of $T(n)$ is integral.

Using


$$
v_3(\det T(n))=v_3(n)+v_3(2n+3),
$$


the inverse-adjugate bound gives


$$
c(V_{n+1})\le c(V_n)+v_3(n)+v_3(2n+3).
$$



### Case $n\equiv2\pmod3$

Again the two $s$-row numerators are divisible by $3$. If $k=v_3(n+1)\ge1$, every transition entry has valuation at least $-k$. Here


$$
v_3(\det T(n))=-k,
$$


so $T(n)^{-1}$ is integral. Therefore


$$
c(V_{n+1})\le c(V_n).
$$



### Case $n\equiv1\pmod3$

The original estimate gives


$$
\min v_3(T(n)_{ij})\ge-1-v_3(2n+1),
$$


while


$$
v_3(\det T(n))=-v_3(2n+1).
$$


Thus


$$
c(V_{n+1})\le c(V_n)+1.
$$



Combining the cases,


$$
\boxed{
c(V_{n+1})-c(V_n)
\le
\mathbf1_{n\equiv1\ (3)}
+v_3(n)+v_3(2n+3).
}
$$



Starting from $c(V_1)=0$, summation gives


$$
\boxed{
c(V_N)\le
\left\lfloor\frac{N+1}{3}\right\rfloor-1
+v_3((2N+1)!)-v_3(N),
\qquad N\ge1.
}
\tag{30.1}
$$



Indeed, the factorial terms telescope exactly as in A1, while the number of indices $1\le n\le N-1$ with $n\equiv1\pmod3$ is $\lfloor(N+1)/3\rfloor$.

For $N=m-1$ on the original branch, $v_3(N)=0$, and the observation upper bound yields


$$
\boxed{
c_m\le
\left\lfloor\frac m3\right\rfloor-5
+v_3((2m-1)!).
}
\tag{30.2}
$$



This improves the linear coefficient of the previous estimate. It remains a linear bound of order $4m/3$; no sublinear or logarithmic theorem has been proved.

The concrete remaining lemma is now to control the actual seeded transition product substantially more sharply, and then its normalized direction—equivalently, the relevant primitive endpoint lines.

---

# IX. Retained normalization identities and complete-error obligations

## 31. A3’s all-prime seed factor and extra binary force factor

The turn-9 results remain unchanged.

For the actual integral endpoint projections, with


$$
\delta_j=\gcd(|R_j|,|C_j|),\qquad
R_j^*=R_j/\delta_j,\quad C_j^*=C_j/\delta_j,
$$


and $R_j\ne0$,


$$
\boxed{
d_j=
|R_j^*|\,
\frac{n!}{\gcd(n!,|E_nR_j^*+C_j^*|)}.
}
$$


This is an all-prime identity. In particular, the seed-dependent multiplier divides $n!$, and the seed-free valuation law holds for every $p>n$.

Also,


$$
\boxed{
v_2(r_3\mathbf U)\ge v_2(n+1)+1
\quad(n\equiv3\pmod4),
}
$$


and throughout the original odd-index domains,


$$
\boxed{v_2(\gamma_3)\le2v_2(n!)-1.}
$$


At $n=3375$, the retained consequences are $v_2(r_3\mathbf U)\ge5$ and $v_2(\gamma_3)\le6733$.

These are endpoint normalization statements, not replacements for the final weighted all-prime gcd.

---

## 32. No finite boundary, force, or row normalization has been removed

For A2, retain the source rows


$$
1\le i\le b-2,
$$


the contact domain $0\le j<b$, and the physical reconstruction through $j=b$. In particular,


$$
Y=\mathcal RA^{-1}\mathbf r+W_be_b
$$


remains complete, and


$$
29^3U_a^TQ
=
29^3(r_0G^{(3)}_{a0}+r_1G^{(3)}_{a1})
+\sum_{\ell=1}^{b-2}\mathcal H_\ell\lambda'_{a,\ell}
+W_bU_{a,b}
$$


retains its whole right-hand side. There is no source row at $b-1$, and the exterior is not an extra recurrence step.

For A1, retain the pole cutoff


$$
0\le v\le2n-2,
$$


both corrected columns, all lower-pole/factorial/LOW terms, nonlinear endpoint corrections, and the full terminal relations


$$
\mu_{i+\nu}^{\langle26\rangle}
+\sum_{k=0}^{\nu-1}f_k\mu_{i+k}^{\langle26\rangle}
=b_i^{\langle26\rangle},
\qquad0\le i\le\nu-2,
$$




$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
$$


The coordinate $\omega_{\nu-1}$ remains present.

No row contents or least actual two-column clearer have been replaced by the selected-prime contents proved here.

---

## 33. Actual primitive denominators and whole same-index errors

For the weighted construction,


$$
A_B=N_{B,1}^T\Omega N_{B,1},\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
$$


The gcd is over all primes. The approximation quantity remains


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
$$



For the determinant construction,


$$
g_\ell=\gcd(|A_\ell|,|B_\ell|),\qquad
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
$$



For A3’s weighted endpoint combination, the retained formula is


$$
q_\lambda=
\frac{kh|AB|}{F_{\rm gcd}GH_{\rm gcd}},
\qquad
p_\lambda=
\operatorname{sgn}(AB)
\frac{T_{\rm wt}}{F_{\rm gcd}GH_{\rm gcd}},
$$


with whole error


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda e_3\alpha_{n,2}(\lambda-\Lambda_{n,2}).
}
$$



None of the local results above evaluates these final all-prime gcds or proves that the whole nonzero form tends to zero on an infinite original sequence.

---

# X. Remaining new work and proof status

## 34. Bounded arithmetic that is still needed

No accepted min-plus audit, eight-parity calculation, $45$-bit contraction, $32$-bit operator/Schur stage, second-symbol audit, or quartic identity audit should be repeated.

### A. Complete the new physical $32$-bit columns

**Inputs**

- the newly certified $124$-band operator and finite Schur inverse;
- original $b,n$;
- complete force formulas;
- $T=36,I=72,R=160,L_0=284,K_0=196$;
- the original finite endpoint and exterior formulas.

**Required verifiable output**

1. Both complete force-dependent heads and solved endpoint charges modulo $2^{32}$.
2. Both reconstructed branches for both columns.
3. Principal-part and jet residuals over $-284\le k\le247$.
4. The terminal check including $-b\,g_0-1$.
5. New $n$-branch zero/nonzero decisions.
6. New contact-factor and $1-z$-division remainders.
7. Denominator and fixed-divisor guards for the representation actually obtained.
8. New contraction residues at the subsequently selected, physically justified precision.

No branch zero or factor count is an input assumption.

### B. Evaluate the complete next $29$-adic short-input norm

**Inputs**

- the fixed short head $h_i^{[0]}=i!\bmod29$, $0\le i<29$;
- compatible $\mathsf D_1,\mathsf D_2$;
- precision-$29^5$ bounds $M=144,L=292$;
- the full second endpoint equation;
- the original terminal row;
- the established leading support and high observables.

**Required verifiable output**

- solved second endpoint charges;
- the pairing of the leading vector with the complete next lift;
- the carry from the whole leading squared norm modulo $29^2$;
- their combined
  

$$
\eta_{\rm short}
  =\frac{T_{\rm short}^TT_{\rm short}}{29}\pmod{29};
$$


- either a symbolic zero for every compatible high continuation, or the explicit surviving high observables and their evaluated low coefficients.

The complete next column still requires its actual head correction $29Ba$, even though that correction is radical for this divided norm.

### C. Follow-on lemma for A1

No further fixed algebraic identity check is needed to justify the results above. The outstanding theorem concerns the actual solution:


$$
V_N=T(N-1)\cdots T(1)(-5,-4)^T.
$$



A useful next lemma would prove a substantially sublinear content bound on the original $N=m-1$, together with control of its normalized direction. Formula (29.1) now makes the endpoint observation component exact; the remaining difficulty is the actual transition product and projective arithmetic, not an unspecified observation matrix.

---

## 35. Proof-status ledger

| Claim | Status after this audit |
|---|---|
| Common upper min-plus minimum $7$ for all 82 shifts | Audited exact finite-word certificate |
| Sharp degree-$81$ kernel content $2^8$ | Proved, with original attaining row |
| Active quartets at bits $38,41$ | Proved |
| Whole-row common odd proportionality | Proved |
| Universal kernel Gram depth at least $18$ | Proved |
| Parity-lift contents at least $11,10$ | Proved; exact minima finitely corroborated |
| Complete column content at least $9$ | Proved |
| Complete Gram depth at least $20$ | Proved after paying the nine-bit division loss |
| Four support classes and nonempty original supports | Independently proved |
| First actual column content exactly $9$ | Proved using supplied parity sums |
| Second actual column content at least $10$ | Proved using supplied parity sums |
| $D_{\rm raw}=0\bmod2^{30}$, $E_{\rm raw}=0\bmod2^{29}$ | New accepted finite evaluation with audited guards |
| Primitive binary norm loss $\nu\ge12$ | Proved |
| Exact norm or mixed depth | Not determined |
| Physical cutoff tuple $124,36,72,160,284,196$ | Derived at the retained integral/unit scope |
| New $32$-bit operator and Schur inverse | Accepted finite stage |
| New $32$-bit heads, numerators, branch zeros, factors | Not yet supplied |
| Compatible $29$-adic $\mathsf D_2$ | Audited proof and finite corroboration |
| Terminal coefficient $14$ | Proved |
| Short-head radical and norm-only reduction | Audited |
| Complete $\eta_{\rm short}$ | Unevaluated |
| Actual $29$-adic content unbounded on every original progression | Proved using the complete integral finite normal form |
| A1 differential rank exactly four | Proved by local branches |
| Original-branch observation exponents $(-6,-4)$ | Proved uniformly |
| Exact three-case observation loss (29.1) | **New theorem** |
| Improved cumulative bound (30.1)–(30.2) | **New theorem; still linear** |
| Infinite all-prime denominator versus whole-error comparison | Open |
| Irrationality or rationality of $e+\pi$ | Unresolved |

---

# Conclusion

The most important completed local result is now an **actual**, not merely ambient, binary normalization statement:


$$
\boxed{
c_2(X)=9,\qquad c_2(Y)\ge10,
}
$$


together with the genuinely evaluated higher residues


$$
\boxed{
v_2(D_{\rm raw})\ge30,\qquad
v_2(E_{\rm raw})\ge29,\qquad
\nu\ge12.
}
$$



The depth-$20$ structural theorem survives, but only after correcting the claim that numerator integrality persists under division by $2^9$. Whole-row proportionality has ample precision to pay that division correctly.

The physical $32$-bit construction now has a justified finite dimensional contract and a certified operator/Schur stage. Its remaining force-dependent work must use the actual exponent $2n+197$, retain both branches until checked, and preserve the complete terminal exterior.

On the $3$-adic endpoint side, the new exact projection formula


$$
\boxed{
c(V_{m-1})-c_m
=
4+\min\{2,v_3(\bar b_m-3\bar a_m)\}
}
$$


removes the residual ambiguity in the observation loss. The improved cumulative estimate remains linear, so the essential seeded-transition and primitive-direction bottleneck is not closed.

Finally, A2’s repeated-block theorem genuinely concerns the complete first column on every original progression. It rules out an eventual $c=1$ progression, but does not supply the primitive norm or complete mixed-force theorem needed globally.

The exact global bottleneck remains:


$$
\boxed{
\text{control of the actual all-prime primitive denominator against the
whole nonzero same-index error on an infinite original sequence}.
}
$$



No unconditional proof or disproof of the irrationality of $e+\pi$ has been established.
