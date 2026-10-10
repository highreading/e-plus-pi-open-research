> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4, Turn 9 — Stronger binary content, a missing endpoint valuation factor, and a four-dimensional algebraic connection

## Executive conclusions

The unconditional irrationality or rationality of $e+\pi$ remains unresolved. The present audit nevertheless yields three additional rigorous results and clarifies the proposed higher-precision calculation.

1. **A5’s proof that both complete original binary columns are divisible by $4$ is valid.** Its phase, degree-$81$ kernel argument, parity numerators, and treatment of the complete second column survive audit. The total coordinate sums are divisible by $8$, including after restoration of the original row signs.

   There is, however, an important distinction in the stated mixed congruence:
   

$$
\boxed{32\mid D_{\rm raw},\qquad16\mid E_{\rm raw}}
$$


   is what A5 actually proves symbolically. Its argument does **not** prove $32\mid E_{\rm raw}$. That stronger mixed divisibility is already contained in the accepted finite twenty-bit evaluation, but should not be attributed to A5’s parity theorem.

2. **The stronger physical content gives an additional precision dividend:**
   

$$
\boxed{
   \text{twenty-bit complete columns determine }
   D_{\rm raw}\pmod{2^{23}},\quad E_{\rm raw}\pmod{2^{22}}.
   }
$$


   These extra residues have not been evaluated in the supplied material. They are not new zero lower bounds.

   The coordinator’s pending $37$-kernel-bit contraction can recover the norm modulo $2^{23}$, if it retains all $37$ numerator bits before the norm’s exact $14$-bit division. It still gives only the mixed contraction modulo $2^{21}$. The additional mixed bit requires a genuinely higher contraction target, not a new physical producer.

3. **The proposed physical $32$-bit cutoffs are not certified by the attached sources.** The arithmetic
   

$$
L(36)=34,\quad72=2\cdot36,\quad160=124+36,\quad
   284=124+160,\quad196=124+72
$$


   is correct. But the attachments do not state the physical head/locality theorem that turns the latter four identities into sufficient cutoffs. In particular, the relation-matrix Smith exponent $8$ supplies none of these bounds.

   Neither new-layer $P_1$-branch vanishing nor persistence of the factors $(1-z)^{68}$, $(1-z)^{72}$ follows from the old arrays. Both require new complete physical computations.

   If the proposed common order $160$ and those factors are certified, the new short orders are $92,88$, **not** $81,77$. Their rising-factorial denominator valuations are exactly
   

$$
\boxed{88,\qquad85.}
$$


   I give below a conservative contraction plan that does not require a new Smith computation.

4. **A3’s seed elimination and stated odd-prime endpoint laws survive audit at their exact scopes.** There is a useful stronger all-prime factorization. For its actual integral endpoint projections $R_j,C_j$, set
   

$$
\delta_j=\gcd(|R_j|,|C_j|),\qquad
   R_j^\ast=R_j/\delta_j,\quad C_j^\ast=C_j/\delta_j.
$$


   Whenever $R_j\ne0$,
   

$$
\boxed{
   d_j=
   |R_j^\ast|\,
   \frac{n!}{\gcd\!\left(n!,\,|E_nR_j^\ast+C_j^\ast|\right)}.
   }
$$


   Thus the entire seed-dependent part of the endpoint denominator is a divisor of $n!$. In particular, the seed-free denominator law is valid at every $p>n$, not only $p>n+2$. The finer $\gamma_j,\mathcal C_j^\sharp$ formulas still require their original normalization-unit hypotheses.

5. **There is a missing binary valuation factor in A3’s endpoint-$3$ analysis.** For $n\equiv3\pmod4$, its own primitive row and complete force give
   

$$
\boxed{v_2(r_3\mathbf U)\ge v_2(n+1)+1,}
$$


   rather than merely $v_2(n+1)$. Consequently, on both odd congruence classes,
   

$$
\boxed{v_2(\gamma_3)\le2v_2(n!)-1.}
$$


   At $n=3375$, this improves the theorem-derived bound to
   

$$
\boxed{v_2(r_3\mathbf U)\ge5,\qquad v_2(\gamma_3)\le6733.}
$$


   This is an actual endpoint-normalization improvement, not a full-state primitivity statement or a denominator bound at $2$.

6. **The proposed reciprocal identities for A1’s algebraic endpoints are correct.** They reveal an anti-invariant differential subspace of dimension four. Thus the joint differential rank is at most four, improving the degree-eight ambient bound:
   

$$
\boxed{\text{joint differential rank}\le4.}
$$


   This does not contradict A1’s valid infinite-rank obstruction for unrestricted exact ternary digit extraction. Nor does it bound same-index endpoint content.

No program was executed for this report. The new compiled-payload receipt is accepted as supplied finite execution evidence after the source audit below. No accepted producer, twenty-bit contraction, or completed original-index computation is proposed for regeneration.

---

# Part I. Audit of the stronger binary parity argument

## 1. Original parameters and physical completeness

The binary input remains


$$
b=150094635296999121,\qquad
n=600678730458590482242=4002b,
$$




$$
N=n+2,\qquad a=2n,
$$


with the original physical range


$$
\boxed{0\le j\le b.}
$$



The accepted complete twenty-bit series are


$$
F(z)=\frac{A_f(z)}{(1-z)^{a+81}},\qquad
E(z)=\frac{A_e(z)}{(1-z)^{a+77}}.
$$


The second numerator includes the retained second force, finite return, terminal factorial cancellation, and exterior $+1$. A5 does not add that exterior term twice or omit it.

For the sign-suppressed columns,


$$
X_j=\binom Nj[z^{b-j}]F(z),\qquad
Y_j=\binom Nj[z^{b-j}]E(z),
$$


the original common row signs cancel in


$$
\sum_jX_j^2,\qquad \sum_jX_jY_j.
$$



The parity conclusions use fewer than twenty physical bits. Therefore they transfer from the specified integer lifts to the actual complete columns. This transfer relies on the accepted physical provenance of $A_f,A_e$; the parity argument is not an independent proof of that provenance.

---

## 2. The original phase is correct

The required residues are


$$
b\equiv\mathtt{0x6d1}\pmod{4096},\qquad
n\equiv\mathtt{0xf42}\pmod{4096}.
$$


Indeed,


$$
4002\cdot\mathtt{0x6d1}\equiv\mathtt{0xf42}\pmod{4096}.
$$



Consequently,


$$
b\bmod256=209,\qquad N\bmod256=68=\mathtt{0x44},
$$


and


$$
(a+80)\bmod256=212=\mathtt{0xd4}.
$$



The smaller residues used later also follow:


$$
N\equiv a\equiv4\pmod8,\qquad b\equiv1\pmod8,
$$




$$
n\equiv2\pmod{16},\qquad b-3\equiv14\pmod{16}.
$$



These are hypotheses at the supplied original binary index. The reports do not establish persistence of the complete-column parity masks throughout an unspecified original family.

---

## 3. The general degree-$81$ kernel theorem is valid

Put $m=a+81$, and for $0\le r\le81$ define


$$
h_r(j)=
\binom Nj
\binom{m+b-j-r-1}{b-j-r},
\qquad0\le j\le b,
$$


with the second binomial defined to be zero when its lower index is negative.

### 3.1 Every kernel coordinate is even

Suppose $\binom Nj$ is odd. Lucas’ criterion forces


$$
j\bmod256\in\{0,4,64,68\}.
$$


Since


$$
(b-r)\bmod256=209-r\in[128,209],
$$


subtracting the possible low byte of $j$ causes no borrow into bit eight. Therefore


$$
(b-j-r)\bmod256\in[60,209].
$$



For a supported term, oddness of the second binomial would require


$$
(b-j-r)\mathbin{\&}(m-1)=0.
$$


But the complement of


$$
(m-1)\bmod256=\mathtt{0xd4}
$$


is $\mathtt{0x2b}=43$. A byte disjoint from $\mathtt{0xd4}$ cannot exceed $43$, contradicting the lower bound $60$.

Thus


$$
\boxed{2\mid h_r(j)}
$$


for every original row and every $0\le r\le81$. Unsupported terms are zero and cause no exception.

### 3.2 The complete kernel sums are divisible by $8$

The finite convolution is exact:


$$
\sum_{j=0}^{b}h_r(j)
=
[z^{b-r}]\frac{(1+z)^N}{(1-z)^m}.
$$


It neither extends the physical range nor deletes the terminal coordinate.

Because $4\mid N$,


$$
(1+z)^N\equiv(1-z)^N\pmod8.
$$


To verify this coefficientwise, write


$$
\left(\frac{1+z}{1-z}\right)^N
=\left(1+\frac{2z}{1-z}\right)^N.
$$


The linear term is divisible by $8$; the quadratic term has coefficient
$4\binom N2$, also divisible by $8$; every higher term contains at least $2^3$.

Hence


$$
\sum_jh_r(j)
\equiv
\binom{n+78+b-r}{b-r}\pmod8.
$$


Now


$$
(n+78)\bmod4096=\mathtt{0xf90},
$$


and


$$
(b-r)\bmod4096\in[\mathtt{0x680},\mathtt{0x6d1}].
$$


Adding the two lower indices forces carries at bits $9,10,11$. Kummer’s theorem gives


$$
\boxed{8\mid\sum_{j=0}^{b}h_r(j).}
$$



Therefore, for every integer polynomial $B$ of degree at most $81$, the column


$$
Z_j=\binom Nj[z^{b-j}]\frac{B(z)}{(1-z)^{a+81}}
$$


satisfies


$$
Z_j\in2\mathbb Z,\qquad \sum_jZ_j\in8\mathbb Z.
$$



This is a genuine phase-specific kernel theorem. It is not inferred from a finite Gram zero.

---

## 4. The two parity numerators really give four-divisible columns

The accepted parity masks are


$$
A_f\equiv z^3(1+z)^{78}\pmod2,\qquad
A_e\equiv(1+z)^{77}\pmod2.
$$


The integral lifts


$$
A_f^{(0)}=z^3(1-z)^{78},\qquad
A_e^{(0)}=(1-z)^{77}
$$


give


$$
F^{(0)}=\frac{z^3}{(1-z)^{a+3}},\qquad
E^{(0)}=\frac1{(1-z)^a}.
$$



Thus


$$
X_j^{(0)}
=\binom Nj\binom{a+b-j-1}{b-j-3},
$$




$$
Y_j^{(0)}
=\binom Nj\binom{a+b-j-1}{b-j}.
$$



A5’s two-factor carry analysis is correct:

- If $j$ is odd, subtraction from $N\equiv4\pmod8$ forces two low borrows, so $4\mid\binom Nj$.
- If $j$ is even, the second binomial in $Y_j^{(0)}$ has two carries because $a-1\equiv3\pmod8$ and $b-j$ is odd.
- For $X_j^{(0)}$, the low residues $a+2\equiv b-3\equiv6\pmod8$ give either two carries in the second binomial or one carry there together with a weight borrow. The split according to bits one and two of $j$ covers every even residue.

Therefore


$$
4\mid X_j^{(0)},\qquad4\mid Y_j^{(0)}.
$$



For the first column,


$$
A_f=A_f^{(0)}+2B_f,\qquad \deg B_f\le81.
$$


The difference $X-X^{(0)}$ is twice a column from the even kernel lattice, hence is divisible by $4$.

For the second column, putting both terms over the common denominator gives


$$
E(z)=\frac{(1-z)^4A_e(z)}{(1-z)^{a+81}},
$$


and


$$
(1-z)^4A_e(z)-(1-z)^{81}
$$


is even coefficientwise and has degree at most $81$. The same kernel argument applies.

Thus the stronger physical content theorem is proved:


$$
\boxed{
X,Y\in4\mathbb Z^{b+1}.
}
\tag{4.1}
$$



It is a lower bound on content, not an exact-content classification.

---

## 5. Total coordinate sums, signs, and the mixed-congruence distinction

The two parity-lift sums satisfy


$$
\sum_jX_j^{(0)}
\equiv\binom{n+b-3}{b-3}\pmod8,
$$




$$
\sum_jY_j^{(0)}
\equiv\binom{n+b-3}{b}\pmod8.
$$


The first binomial has three forced carries from


$$
n\equiv2,\quad b-3\equiv14\pmod{16}.
$$


For the second, $n-3\equiv7\pmod8$ and $b$ is odd, again forcing three carries.

The perturbations have sums divisible by $16$. Hence


$$
\boxed{
8\mid\sum_jX_j,\qquad8\mid\sum_jY_j.
}
\tag{5.1}
$$



These are statements about the **total** coordinate sums, not arbitrary partial sums.

Restoring any of the original row signs changes a total sum by a sum of terms $2X_j$ or $2Y_j$. By (4.1), these changes are divisible by $8$. Thus (5.1) also holds for the actual signed physical columns.

For $V=sX+tY$, every coordinate is divisible by $4$, and $\sum_jV_j$ is divisible by $8$. Since


$$
x^2\equiv4x\pmod{32}\qquad(x\in4\mathbb Z),
$$


we obtain


$$
\boxed{
\sum_j(sX_j+tY_j)^2\equiv0\pmod{32}.
}
\tag{5.2}
$$



Taking $V=X$ proves $32\mid D_{\rm raw}$. Polarization gives only


$$
2\sum_jX_jY_j\equiv0\pmod{32},
$$


or


$$
\boxed{16\mid E_{\rm raw}.}
\tag{5.3}
$$



### Why the extra mixed factor does not follow

This is a genuine logical distinction. For example,


$$
X=4(1,1,0),\qquad Y=4(1,0,1)
$$


have four-divisible coordinates and eight-divisible sums, and every integral combination has norm divisible by $32$, but


$$
X^TY=16\not\equiv0\pmod{32}.
$$



Thus A5’s symbolic argument cannot be upgraded to $32\mid E_{\rm raw}$ by polarization. Its actual report correctly states $16$.

For the original physical input, the accepted finite computation already proves the much stronger statement


$$
D_{\rm raw}\equiv E_{\rm raw}\equiv0\pmod{2^{20}}.
$$


That finite result includes mixed divisibility by $32$, but is a different source of evidence.

---

# Part II. Transport scope, compiled crosscheck, and the new precision dividend

## 6. Negative odd factorials and fixed-precision evaluation

A5’s correction of the negative-argument scope is necessary and valid.

The recurrence


$$
g(h+1)=(2h+1)g(h),\qquad g(0)=1,
$$


gives


$$
g(-m)=\frac{(-1)^m}{(2m-1)!!}\in\mathbb Z_{(2)}^\times.
$$


Negative values need not be integers.

The truncated Newton polynomial


$$
g_p(h)=\sum_{r=0}^{2p-2}\gamma_r\binom hr
$$


represents $g(h)\bmod2^p$ on all integers, not merely nonnegative ones. The proof through


$$
g_p(h+1)-(2h+1)g_p(h)
$$


is sound: its Newton coefficients are divisible by $2^p$, so the recurrence holds on every integer, and it can be run backwards using odd inverses.

This does not define negative ordinary factorials. Along accepted paths the original factorial arguments remain nonnegative; negative arguments occur only in the odd-unit interpolation extension.

A5’s threshold proof also establishes


$$
d_t\in\{0,1,2\}
$$


on every reachable prefix, including prefixes without an accepted terminal completion. Terminal acceptance at $000$, after all $71$ digits, still selects exactly $0\le j\le b$.

Fixed-precision Newton evaluation therefore needs a list of $2p-1$ coefficients, with degree at most $2p-2$, rather than a table of size $2^p$. Here $p$ must be the **actual working kernel precision**, which may exceed the requested physical column precision.

---

## 7. The new compiled-payload crosscheck is correctly normalized

The supplied source explicitly checks


$$
\texttt{content}+23\le351
$$


before dividing the reported free coordinates by their contents. The available post-division precisions are


$$
351-157=194,\qquad351-154=197.
$$


These are the relevant guards. The inequalities $194,197\le351$ alone would not justify the division; the source uses the stronger, correct condition.

The code then:

1. constructs the normalized free coordinates modulo $2^{23}$;
2. forms the degree-at-most-$162$ compiled polynomials in the three integral quotient representatives;
3. converts their $163$ consecutive values into Newton coefficients;
4. applies the retained finite transport;
5. divides the evaluated observables by $8$, justified by the exact saturated identities;
6. inverts only the odd denominator units.

The receipt reports


$$
\mathscr L(Q_f)\equiv\mathscr L(Q_m)\equiv0\pmod{2^{23}},
$$


and consequently


$$
\boxed{
D_{\rm raw}\equiv E_{\rm raw}\equiv0\pmod{2^{20}}.
}
$$



This independently crosschecks the distinct fixed-divisor payload construction, while sharing the audited transport routine. It is not a wholly independent implementation of the transport itself.

The reported $228$ transitions at this precision need not equal the $248$ reported for the higher-precision fixed-divisor calculation. Nothing in the theorem requires precision-independent transition counts.

The crosscheck supplies no additional physical digits beyond the same twenty-bit target. It should not be rerun.

---

## 8. Stronger quadratic stability

Let $x,y$ be the actual complete integral columns, and let $\widetilde x,\widetilde y$ be the retained integer lifts. Write


$$
x=\widetilde x+2^M h,\qquad
y=\widetilde y+2^M k.
$$


Both actual and lifted columns are divisible by $4$.

Then


$$
x^Tx-\widetilde x^T\widetilde x
=
2^{M+1}\widetilde x^Th+2^{2M}h^Th
\in2^{\min(M+3,2M)}\mathbb Z,
$$


and


$$
x^Ty-\widetilde x^T\widetilde y
=
2^Mh^T\widetilde y+
2^M\widetilde x^Tk+
2^{2M}h^Tk
\in2^{\min(M+2,2M)}\mathbb Z.
$$



At $M=20$,


$$
\boxed{
D_{\rm raw}\equiv\widetilde D\pmod{2^{23}},\qquad
E_{\rm raw}\equiv\widetilde E\pmod{2^{22}}.
}
\tag{8.1}
$$



This is one more guaranteed bit for each contraction than the turn-8 evenness argument supplied.

### What the pending $37$-bit calculation can return

The retained exact fixed-divisor normalizations are


$$
S_{ff}=2^{14}d_f^2\widetilde D,\qquad
S_{fe}=2^{16}d_fd_e\widetilde E.
$$


Thus a $37$-bit kernel determines


$$
\widetilde D\pmod{2^{23}},\qquad
\widetilde E\pmod{2^{21}}.
$$



Accordingly:

- the pending calculation can retain a genuine physical **norm modulo $2^{23}$** without increasing its kernel precision;
- its mixed result remains modulo $2^{21}$;
- a mixed result modulo $2^{22}$ needs $38$ fixed-divisor kernel bits, or equivalently a new $25$-bit compiled mixed-payload contraction followed by division by $8$.

The latter is a new target, not a request to regenerate the accepted twenty-bit calculation.

A $38$-bit fixed-divisor evaluation would arithmetically produce a lifted norm modulo $2^{24}$, but only its reduction modulo $2^{23}$ is guaranteed to be physical by the current theorem.

### Current valuation conclusions

Until new residues are returned, the established numerical lower bounds remain


$$
\boxed{v_2(D_{\rm raw})\ge20,\qquad v_2(E_{\rm raw})\ge20.}
$$


Equation (8.1) does not change those zeros into bounds $23,22$.

Nor does it supply an upper norm-depth bound or close the norm-relative logarithmic omission guard.

---

# Part III. Audit of the proposed physical $32$-bit plan

## 9. What follows from $T=36$, and what does not

The factorial valuation is


$$
L(T)=T-s_2(T).
$$


For $T=36$,


$$
L(36)=36-2=34\ge32.
$$



Thus, **if the retained physical tail theorem bounds every omitted, correctly normalized operator and forcing contribution by $2^{L(T)}$**, then $T=36$ provides two bits of margin over a $32$-bit target before any additional loss.

The arithmetic threshold itself does not require $36$: $L(34)=32$. The choice $36$ is safe under that tail hypothesis and may serve other locality requirements.

The implication from $v_2(T!)$ to a complete physical truncation is not automatic. It must apply after all displayed normalizations and to all omitted branches, including their reconstructed terminal effects.

### Unit endpoint inverse

For an integral endpoint matrix $E$ with odd determinant,


$$
E^{-1}=\frac{\operatorname{adj}(E)}{\det E}
$$


is integral over $\mathbb Z_2$. Hence this normalized endpoint inverse incurs **zero** binary precision loss.

For an approximate endpoint state $\widetilde q$, the exact error is


$$
q-\widetilde q=E^{-1}(t-E\widetilde q).
$$


Thus the complete endpoint residual, not merely the unreturned head, must be divisible by $2^{32}$.

This is the relevant inverse statement. The Smith exponent $8$ of the polynomial relation matrix is unrelated to it.

---

## 10. The other numerical cutoffs are not derivable from the supplied theorem statements

The proposal has the arithmetic pattern


$$
I=2T=72,\qquad m_{\rm head}=I+52=124,
$$




$$
R=m_{\rm head}+T=160,
$$




$$
L_0=m_{\rm head}+R=284,\qquad
K_0=m_{\rm head}+I=196.
$$



These identities are correct. Their **sufficiency** requires a physical theorem stating, with its normalization and indexing conventions:

- why head length $2T$ contains every retained operator interaction;
- why the required solved head is $I+52$;
- why output order is $m_{\rm head}+T$;
- why the two finite reconstruction bands are bounded by $m_{\rm head}+R$ and $m_{\rm head}+I$;
- how the complete finite endpoint return fits inside these bounds.

That theorem is not stated in the attached material. A4turn8 explicitly left the numerical higher-precision head cutoff uncertified. The degree-$81/77$ output presentations and the $163\times160$ relation matrix do not fill this gap.

Therefore the correct verdict is:



$$
\boxed{
\text{The proposed cutoffs are not certified here; they are not disproved.}
}
$$



They should not yet be treated as accepted physical memory bounds.

### Concrete missing lemma

The outstanding physical lemma should assert that, for the **original finite operator and both complete forces**, the proposed finite construction produces $\widetilde x,\widetilde y$ with


$$
x-\widetilde x,\ y-\widetilde y\in2^{32}\mathbb Z_2^{b+1},
$$


by proving all of the following:

1. a normalized tail bound at $T=36$;
2. the exact head dependency bound $I=72$;
3. the solved-head bound $m_{\rm head}=124$;
4. the finite reconstruction bounds $L_0=284,K_0=196$;
5. an integral unit endpoint inverse;
6. a complete endpoint residual divisible by $2^{32}$.

This is a finite-bound theorem, not a Smith calculation.

---

## 11. The two $P_1$ branches and short factors require new physical evidence

At the new layer, neither of the following can be inherited by lifting old residues:

- the vanishing of the two $P_1$ branches;
- divisibility of the newly produced numerators by $(1-z)^{68}$ and $(1-z)^{72}$.

The new calculation must form both branches at the required physical precision and include their full reconstruction and terminal return. A branch that vanished modulo $2^{20}$ may reappear between bits $20$ and $31$.

Similarly, for a newly certified polynomial numerator $A(z)$, divisibility by $(1-z)^s$ modulo $2^{32}$ can be checked exactly by verifying that the coefficients of


$$
A(1+y)
$$


in degrees $0,\ldots,s-1$ vanish modulo $2^{32}$. This is a new remainder test on the new physical numerator.

No such result is supplied.

---

## 12. Conditional consequences if order $160$ and both short factors persist

Suppose the new complete physical output is certified in the form


$$
F=\frac{B_f(z)}{(1-z)^{a+160}},\qquad
E=\frac{B_e(z)}{(1-z)^{a+160}}\pmod{2^{32}},
$$


with numerator degrees at most $160$, and suppose


$$
(1-z)^{68}\mid B_f,\qquad
(1-z)^{72}\mid B_e\pmod{2^{32}}.
$$



Then the short presentations have orders


$$
\boxed{R_f=92,\qquad R_e=88,}
$$


and numerator degrees at most $92,88$.

The old orders $81,77$, old payload degrees $162,158$, and old $163\times160$ quotient presentation cannot simply be reused for those new payloads.

### 12.1 Exact new denominator valuations

Since


$$
a\bmod256=132,
$$


the intervals defining the two rising factorials have the same valuations as $132,\ldots,223$ and $132,\ldots,219$, respectively. Neither interval crosses a multiple of $256$.

Therefore


$$
\begin{aligned}
v_2\bigl((a)^{\overline{92}}\bigr)
&=v_2(223!)-v_2(131!)\\
&=92-\bigl(s_2(223)-s_2(131)\bigr)\\
&=92-(7-3)=88,
\end{aligned}
$$


and


$$
\begin{aligned}
v_2\bigl((a)^{\overline{88}}\bigr)
&=v_2(219!)-v_2(131!)\\
&=88-(6-3)=85.
\end{aligned}
$$



Thus


$$
\boxed{
v_2(D_f)=88,\qquad v_2(D_e)=85.
}
\tag{12.1}
$$



No new fixed-divisor contents or saturated free contents have yet been proved for these new numerators.

### 12.2 A conservative contraction plan requiring no new Smith claim

The factorial-ratio transport applies directly to the integral numerator polynomials


$$
U_f^2,\qquad U_fU_e,
$$


of degrees at most $184,180$.

Because thirty-two physical bits and the proved content $4$ determine


$$
D_{\rm raw}\pmod{2^{35}},\qquad E_{\rm raw}\pmod{2^{34}},
$$


a sufficient direct numerator precision is


$$
2\cdot88+35=211
$$


for the norm and


$$
88+85+34=207
$$


for the mixed contraction.

Hence, conditional on the physical certification and short-factor tests,


$$
\boxed{
\mathscr L(U_f^2)\pmod{2^{211}},\qquad
\mathscr L(U_fU_e)\pmod{2^{207}}
}
$$


suffice, followed by the exact denominator divisions and odd-unit inversions.

This is deliberately conservative. It extracts no unproved fixed divisor and uses no uncomputed Smith data.

At a shared $211$-bit kernel precision, the retained transport theorem gives degree envelopes


$$
184+2(211-1)=604,\qquad
180+2(211-1)=600,
$$


and after eight digits both are at most $420$, with at most four reachable borrow states.

These are **conditional contraction bounds**, not a certification of the proposed physical producer’s memory bounds. Fixed-precision odd-factorial Newton evaluation avoids any exponential-size prefix table.

If the short factors fail, an unshort order-$160$ fallback is still possible once that physical presentation is certified, but its payload degree and exact denominator precision must be recalculated rather than borrowed from the old arrays.

---

# Part IV. Independent audit of A3’s seed elimination and endpoint laws

## 13. The exact seed decomposition is correct

Retain A3’s original odd-index domains


$$
n=15^r\quad\text{or}\quad n=105^r,\qquad r\ge2.
$$


The original $3\times3$ contact matrix, both corrected four-coordinate columns, and complete forcing through exactly $2n+2$ remain unchanged.

Let


$$
A_n(z)=D^n\!\left(\frac{e^z}{1-z}\right).
$$


Differentiating the underlying first-order equation $n$ times gives


$$
(1-z)A_n'-(n+1)A_n=e^z.
$$


Therefore


$$
\frac{d}{dz}\bigl((1-z)^{n+1}A_n(z)\bigr)
=e^z(1-z)^n.
$$


Using $A_n(0)=E_n$,


$$
\Omega_n(z)=
\frac{q(z)^n}{(1-z)^{n+1}}
\left(E_n+\int_0^ze^t(1-t)^n\,dt\right).
$$



A3’s coefficient extraction consequently gives


$$
\boxed{u_k=E_nh_k+g_k,\qquad h_k,g_k\in\mathbb Z[n].}
$$



The integrality argument for factorial-normalized coefficients of $q^n$ is valid at $2$, not merely at odd primes. The coefficients count singleton/pair partitions after the displayed factorial normalization.

The negative-index issue in the odd-prime periodicity proof is also handled correctly: the polynomial extension is multiplied by $(k)_r$, which is zero for $r>k$. No negative-index $E_m$ is introduced.

The binary period $2^{s+1}$ modulo $2^s$ follows from the stated derivative expansion and valuation bound. Replacing it by period $2^s$ would be unjustified.

At the three retained contact rows, the established reference identity makes the $E_n$-dependent force exactly proportional to the reference column. This proves the complete integral endpoint equation


$$
\boxed{
\frac{v_j^{\rm rec}}{u_j^{\rm rec}}
=
\frac{E_nR_j+C_j}{n!R_j}.
}
\tag{13.1}
$$


The definition of $C_j$ includes the zero-seeded exponential residual, subtraction of $T_0$, complete logarithmic force at its established three-row scope, and exterior correction.

It is not a homogeneous replacement of the actual force.

---

## 14. New all-prime factorization of the actual endpoint denominator

Equation (13.1) gives


$$
d_j=
\frac{|n!R_j|}
{\gcd(|n!R_j|,\ |E_nR_j+C_j|)}.
$$



Assume $R_j\ne0$, and define


$$
\delta_j=\gcd(|R_j|,|C_j|),\qquad
R_j^\ast=R_j/\delta_j,\quad C_j^\ast=C_j/\delta_j.
$$


Then


$$
\gcd(|R_j^\ast|,|C_j^\ast|)=1,
$$


so


$$
\gcd\!\left(|R_j^\ast|,
|E_nR_j^\ast+C_j^\ast|\right)=1.
$$



Cancelling $\delta_j$ from numerator and denominator and using this coprimality yields the exact identity


$$
\boxed{
d_j=
|R_j^\ast|\,
\frac{n!}
{\gcd\!\left(n!,\,|E_nR_j^\ast+C_j^\ast|\right)}.
}
\tag{14.1}
$$



### Consequences

First,


$$
\boxed{
\frac{|R_j|}{\gcd(|R_j|,|C_j|)}
\ \mid\ d_j\ \mid\
n!\frac{|R_j|}{\gcd(|R_j|,|C_j|)}.
}
\tag{14.2}
$$



Thus the seed-dependent denominator multiplier is a divisor of $n!$. This is an all-prime statement about the actual endpoint ratio.

Second, at every prime $p>n$,


$$
\boxed{
v_p(d_j)=\bigl(v_p(R_j)-v_p(C_j)\bigr)_+.
}
\tag{14.3}
$$


The larger cutoff $p>n+2$ is unnecessary for this denominator identity alone.

Third, at an arbitrary prime, write


$$
t=v_p(n!),\qquad r=v_p(R_j),\qquad c=v_p(C_j).
$$


If $c<r$, then $R_j^\ast$ is divisible by $p$ and the reduced numerator is a unit. Hence


$$
\boxed{v_p(d_j)=t+r-c\qquad(c<r).}
\tag{14.4}
$$


If $c\ge r$, then $R_j^\ast$ is a $p$-unit, and


$$
\boxed{0\le v_p(d_j)\le t.}
\tag{14.5}
$$



These are useful endpoint-specific threshold laws. They do not bound $r$ or $c$ along the original infinite families.

### Scope of A3’s finer laws

For


$$
R_j=\frac{(n+1)!}{2}G_j\xi_j,
$$


the formulas


$$
v_p(\gamma_j)=(g-c)_+,
$$




$$
v_p(\mathcal C_j^\sharp)
=\min\{x,(c-g)_+\},
$$




$$
v_p(d_j)=(g+x-c)_+
$$


remain correct at $p>n+2$, where the displayed normalizing factors are units.

One must not extend these finer formulas to exceptional normalizing primes merely because (14.3) extends to $p>n$. The structural threshold $g=v_p(G_j)$ is essential and has not been dropped.

---

## 15. The $p\ge5$, $p\mid n-1$ theorem survives audit

For $p^s\mid n-1$, A3 obtains


$$
r_0\equiv(1,-2,-6),\qquad r_3\equiv(0,1,0)\pmod{p^s},
$$


up to local units, and


$$
v'\equiv(6,3,2),\qquad w'\equiv(0,3,5),
$$




$$
\mathbf U\equiv(18,24,31).
$$



The resulting projections are


$$
(r_0v',r_0w')\equiv(-12,-36),\qquad
(r_3v',r_3w')\equiv(3,3),
$$




$$
r_0\mathbf U\equiv-216,\qquad r_3\mathbf U\equiv24.
$$


For every $p\ge5$, the structural gcds and force projections are units.

With $t=v_p(n!)$, the actual primitive-triple law therefore gives


$$
v_p(\gamma_0)=v_p(\gamma_3)=2t.
$$


The primitive exponential coordinate is a unit, whereas the logarithmic correction multiplied by $\gamma_j$ has positive valuation. Hence


$$
v_p(\zeta_0)=v_p(\zeta_3)=0,
$$


and


$$
\boxed{v_p(d_j)=2t+v_p(\xi_j),\qquad j=0,3.}
$$



This is a genuine complete-force cancellation exclusion at these primes. It does not assume that $\xi_j$ is a unit.

The reference-unit discussion is correctly restricted: the Lucas digit tables for $3,5,7$ do not establish an all-odd-prime unit theorem.

---

## 16. Both $p\mid n+1$ endpoint reductions are valid

Let $p$ be odd and $s=v_p(n+1)$. Using A3’s notation


$$
A=a_n,\ B=a_{n-1},\ C=a_{n-2},\
D=a_{n+1},\ E=a_{n+2},
$$


the raw endpoint-$0$ row has a factor $n+1$, and expansion gives


$$
\frac{\mathscr R_0}{n+1}
\equiv(A+B+1,\,2C,\,-2C)\pmod{p^s}.
$$


The moment recurrence gives $A+B+C\equiv1$, yielding


$$
\boxed{
r_0\equiv(2-C,2C,-2C),\qquad
r_3\equiv(1,0,0)\pmod{p^s}.
}
$$


The first vector is primitive modulo $p$, so the raw endpoint-$0$ row has exactly $s$ factors of $p$ in its row content.

The reference projections satisfy


$$
r_0v'\equiv4,\quad r_0w'\equiv0,\qquad
r_3v'\equiv2,\quad r_3w'\equiv0,
$$


so both $G_j$ are units.

The complete exponential vector reduces to


$$
\mathbf U\equiv(0,E_n-1,E_n-1)^T\pmod{p^s},
$$


annihilated by both primitive rows. Hence


$$
v_p(r_j\mathbf U)\ge s,
\qquad
v_p(\gamma_j)\le2v_p(n!).
$$



For odd $n$, $v_p(n!)\ge s$, giving the stated denominator bound


$$
\boxed{
v_p(d_j)\le2v_p(n!)+v_p(\xi_j).
}
$$


No extra reference-unit assumption is needed for this inequality.

These are endpoint results. They are not consequences of the primitivity of an ambient moment–force state.

---

# Part V. A missing binary factor in the endpoint-$3$ force projection

## 17. Strengthening the $n\equiv3\pmod4$ case

Let


$$
m=n+1,\qquad N=n+2,\qquad s=v_2(m)\ge2,
$$


and retain


$$
A=a_n,\quad B=a_{n-1},\quad
D=a_{n+1},\quad E=a_{n+2}.
$$



The raw endpoint-$3$ row is


$$
\mathscr R_3=
\left(
N^2D^2-mNAE,\;
m(nNBE-N^2AD),\;
m(mN^2A^2-nN^2BD)
\right).
$$



For $n\equiv3\pmod4$, the retained moment parity is


$$
A,D\ \text{odd},\qquad B,E\ \text{even}.
$$


Consequently,


$$
\mathscr R_{3,0}\equiv1\pmod2,
$$




$$
\frac{\mathscr R_{3,1}}m\equiv1\pmod2,
\qquad
\frac{\mathscr R_{3,2}}m\equiv0\pmod2.
\tag{17.1}
$$



The row is already primitive at $2$. Passing to the actual primitive integral row divides only by an odd factor, so all valuation conclusions below are unchanged.

The actual force parity for odd $n$ is


$$
u_k\bmod2=(0,1,0,0)\qquad(k\bmod4=0,1,2,3).
$$


Thus


$$
u_n\equiv u_{n+1}\equiv0\pmod2.
$$



The complete exterior-corrected exponential entries are


$$
U_0=mN(u_n-A),\qquad
U_1=N(u_{n+1}-D),\qquad
U_2=u_{n+2}-E.
$$


Therefore


$$
U_0/m\equiv1\pmod2,\qquad U_1\equiv1\pmod2.
\tag{17.2}
$$



Combining (17.1)–(17.2),


$$
\begin{aligned}
\frac{\mathscr R_3\mathbf U}{m}
&=
\mathscr R_{3,0}\frac{U_0}{m}
+\frac{\mathscr R_{3,1}}mU_1
+\frac{\mathscr R_{3,2}}mU_2\\
&\equiv1+1+0=0\pmod2.
\end{aligned}
$$



We have proved the additional factor:


$$
\boxed{
v_2(r_3\mathbf U)\ge s+1.
}
\tag{17.3}
$$



This cancellation was not used in A3’s turn-5 bound.

---

## 18. Consequence for the actual primitive normalization

As in A3, the reference projections give


$$
v_2(G_3)=1.
$$


For the normalizing factor


$$
K_n=\frac{n!(n+1)!}{2},
$$


write $t=v_2(n!)$. Then


$$
v_2(K_n)=2t+s-1.
$$



The exact primitive-triple law gives


$$
v_2(\gamma_3)
=
\bigl(v_2(K_n)+v_2(G_3)-v_2(r_3\mathbf U)\bigr)_+.
$$


Using (17.3),


$$
v_2(\gamma_3)\le2t-1.
$$



A3 already proves this same bound for $n\equiv1\pmod4$. Therefore, on the original odd-index domains,


$$
\boxed{
v_2(\gamma_3)\le2v_2(n!)-1.
}
\tag{18.1}
$$



At $n=3375$,


$$
v_2(n!)=3367,\qquad v_2(n+1)=4,
$$


so


$$
\boxed{
v_2(r_3\mathbf U)\ge5,\qquad
v_2(\gamma_3)\le6733.
}
\tag{18.2}
$$



These are theorem-derived statements. No archived force or endpoint entry was recomputed here.

They are not bounds for $v_2(d_3)$: the binary reference valuations and complete numerator cancellation in the actual all-prime denominator formula still have to be retained.

---

# Part VI. A1’s algebraic endpoints and the reciprocal reduction

## 19. Audit of the algebraic connection and digit-rank obstruction

A1’s coefficient formulas preserve the adjacent parameter $A=2m-1$ within each pair. The Lagrange-residue identity therefore gives the stated actual joint generating functions


$$
\mathcal A(x)=\frac{(1+Z)^3(1-Z)}{R(Z)},
$$




$$
\mathcal B(x)=
\frac{2Z(1+Z)^5}{(1+Z^2)(1-Z)R(Z)},
$$


where


$$
R(z)=1+8z-10z^2+8z^3+z^4
$$


and


$$
2Z(1+Z)^6=x(1+Z^2)^3(1-Z)^2.
$$



The rational map has degree eight: its coprime numerator and denominator have degrees seven and eight. Thus the degree-eight ambient field assertion is correct.

A1’s exact ternary-rank obstruction is also valid. Finite section rank for a rational sequence over $\mathbb Q_3$ implies the same finite rank over $\mathbb Q$, hence a fixed rational matrix realization with $O(\log m)$ digit transitions. Its real growth is polynomial.

The actual endpoint satisfies


$$
|a_m^{\rm end}|
\ge\binom{3m-1}{m}\ge2^m.
$$


Therefore its unrestricted exact ternary section span is infinite-dimensional.

This excludes a fixed exact finite-rank linear digit lattice, even with fixed scalar denominators on digit maps. It does not exclude fixed-modulus methods, nonlinear normalization, valuation-indexed lattices, or a proved smaller original-power language.

---

## 20. The reciprocal identities are correct

Set


$$
w=z+\frac1z.
$$


Then


$$
w+2=\frac{(1+z)^2}{z},\qquad
w-2=\frac{(1-z)^2}{z},\qquad
w=\frac{1+z^2}{z}.
$$


Substitution immediately gives


$$
\boxed{
x=\frac{2(w+2)^3}{w^3(w-2)}.
}
\tag{20.1}
$$



Also


$$
R(z)=z^2(w^2+8w-12).
$$


Hence


$$
\boxed{
\mathcal A=
\left(\frac1z-z\right)
\frac{w+2}{w^2+8w-12},
}
\tag{20.2}
$$


and


$$
\boxed{
\frac{\mathcal B}{\mathcal A}
=
\frac{2(w+2)}{w(w-2)}.
}
\tag{20.3}
$$



All three proposed identities are therefore independently verified.

The involution $z\mapsto1/z$ fixes $x$ and $w$, while changing the signs of both $\mathcal A$ and $\mathcal B$.

---

## 21. New consequence: a rank-at-most-four joint differential connection

Use the regular local parameter


$$
u=\frac1w=\frac{z}{1+z^2}.
$$


Then $u(0)=0$, $u'(0)=1/2$, and (20.1) becomes


$$
x=\frac{2u(1+2u)^3}{1-2u}.
$$


Equivalently,


$$
\boxed{
P(x,u)=16u^4+24u^3+12u^2+(2+2x)u-x=0.
}
\tag{21.1}
$$



Define


$$
\delta=\frac{1-z^2}{1+z^2},
\qquad
\delta^2=1-4u^2,\qquad \delta(0)=1,
$$


and


$$
Q(u)=1+8u-12u^2.
$$


The outputs become


$$
\boxed{
\mathcal A=\delta\,\frac{1+2u}{Q(u)},
}
\tag{21.2}
$$




$$
\boxed{
\mathcal B=
\delta\,\frac{2u(1+2u)^2}{(1-2u)Q(u)}.
}
\tag{21.3}
$$



The rational map $u\mapsto x$ has degree four, so


$$
[\mathbb Q(u):\mathbb Q(x)]=4.
$$


The anti-invariant part of the degree-eight field is


$$
\delta\,\mathbb Q(u),
$$


which is four-dimensional over $\mathbb Q(x)$. Both actual outputs lie in this subspace.

Differentiation preserves it. Indeed,


$$
\boxed{
u'=\frac{(1-2u)^2}{2(1+2u)^2Q(u)},
}
$$


and


$$
\boxed{
\frac{\delta'}{\delta}
=-\frac{4uu'}{1-4u^2}.
}
$$


Thus


$$
\frac d{dx}(\delta u^k)
=
\delta u'
\left(
ku^{k-1}-\frac{4u^{k+1}}{1-4u^2}
\right),
$$


which can be reduced modulo the quartic $P$ into the basis


$$
\delta,\ \delta u,\ \delta u^2,\ \delta u^3.
$$



Therefore


$$
\boxed{
\text{the actual joint endpoint differential rank is at most four.}
}
\tag{21.4}
$$



The minimal rank has not been computed.

### Normalization significance and limitation

This reduces the exact symbolic coefficient-connection problem from an eight-dimensional ambient field to a four-dimensional invariant subspace containing both actual outputs.

It does **not** give finite exact digit rank. Nor does the generating-function quotient $\mathcal B/\mathcal A$ equal the same-index quotient $b_m^{\rm end}/a_m^{\rm end}$.

Likewise, removing the formal unit $\delta(x)$ is a triangular convolution of coefficient sequences, not a same-index unit scaling of the endpoint pair. It cannot be used to preserve or bound $c_m$ without an additional observability argument.

The original requirements remain: on


$$
j>0,\quad j\equiv81\pmod{243},\quad m=2^{2j-1},
$$


one needs actual common-content control and the prescribed avoidance or approach bounds for the two split scalar lines. No such line-avoidance result follows from (21.4).

---

# Part VII. Complete forcing, primitive normalization, and remaining calculations

## 22. No finite boundary or forcing term has been changed

The binary argument retains every original coordinate $0\le j\le b$, both corrected columns, and the second column’s exterior contribution.

The $29$-adic conclusions forwarded from turn 8 remain unchanged:

- the corrected low coefficients are $21,-21$;
- the original source rows remain $1\le i\le b-2$;
- all eleven classes
  

$$
C\equiv2+29\gamma\pmod{841},\qquad18\le\gamma\le28,
$$


  remain obstructed as proved there;
- the complete next-order force and finite endpoint return remain outstanding.

For A3, the complete forcing still runs through exactly $2n+2$; the three-row logarithmic identity is used only at that scope. Both corrected four-coordinate columns and the exterior $+1$ remain.

For A1’s full producer, the original pole cutoff remains


$$
0\le v\le2n-2,
$$


and neither the nonlinear endpoint elimination nor any lower-pole, factorial, LOW, unpaired-cutoff, or exterior term is removed. In particular, the retained inhomogeneous return


$$
\mu_{i+\nu}^{\langle26\rangle}
+\sum_{k=0}^{\nu-1}f_k\mu_{i+k}^{\langle26\rangle}
=b_i^{\langle26\rangle},
\qquad0\le i\le\nu-2,
$$


and


$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right)
$$


remain intact, including $\omega_{\nu-1}$.

None of the new algebraic reorganizations introduces a moment beyond the retained finite boundary.

---

## 23. All-prime primitive denominators and whole same-index errors

The endpoint factorization (14.1) is an exact simplification of an actual endpoint denominator. It does not replace the final all-prime normalization of a weighted combination.

For A3’s reduced weight $\lambda=a/k$, retain


$$
q_\lambda=
\frac{kh|AB|}{F_{\rm gcd}GH_{\rm gcd}},
\qquad
p_\lambda=
\operatorname{sgn}(AB)
\frac{T_{\rm wt}}{F_{\rm gcd}GH_{\rm gcd}},
$$


with all primes retained in every gcd. The whole error remains


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda e_3\alpha_{n,2}(\lambda-\Lambda_{n,2}).
}
$$



For the weighted Gram normalization, after all actual row contents and the least actual two-column clearer have been restored,


$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\quad p_n=H_B/g_B,
$$


and


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
$$



For A1’s determinant construction, retain


$$
g_\ell=\gcd(|A_\ell|,|B_\ell|),
$$




$$
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



Selected-prime content improvements do not determine these final gcds, actual primitive denominators, or whole errors.

The completed $n=3375$ enclosures remain finite results for their five stated probes. They are neither rerun nor promoted to an infinite-family theorem.

---

## 24. New bounded arithmetic: inputs and verifiable outputs

### 24.1 Pending binary contraction

The coordinator’s already planned $37$-kernel-bit computation should, if convenient, retain:

- $S_{ff}\bmod2^{37}$, giving the genuine physical norm modulo $2^{23}$;
- $S_{fe}\bmod2^{37}$, giving the genuine mixed contraction modulo $2^{21}$;
- reduction to the accepted twenty-bit zeros;
- the same original terminal acceptance and valuation-layer checks.

No new physical producer is needed for these outputs.

The additional mixed bit can be obtained by a **new** $25$-bit compiled mixed-payload contraction using the existing exact saturated coordinates and integral quotient representatives. Its verifiable output is $E_{\rm raw}\bmod2^{22}$, after exact division by $8$. This is distinct from rerunning the accepted twenty-bit target.

### 24.2 Proposed physical $32$-bit construction

Before treating the numerical bounds as certified, supply the physical tail/head/band lemma identified in §10.

Then the new calculation must output:

1. both complete reconstructed columns modulo $2^{32}$;
2. the complete endpoint residual and unit-inverse certificate;
3. actual new-layer results for both $P_1$ branches;
4. the proposed order-$160$ output certificate;
5. remainder tests for $(1-z)^{68}$ and $(1-z)^{72}$;
6. all forcing and exterior-return contributions used in those tests.

If the short factors persist, the exact denominator valuations must be $88,85$, and the direct conservative contraction precisions in §12 provide a verifiable fallback without an assumed new fixed divisor.

### 24.3 Four-dimensional algebraic coefficient connection

This is a new fixed-degree symbolic problem, smaller than A1’s unevaluated degree-eight specification.

**Inputs:**


$$
P(x,u)=16u^4+24u^3+12u^2+(2+2x)u-x,
$$




$$
Q(u)=1+8u-12u^2,
$$


the two output functions (21.2)–(21.3), and the derivative identities in §21.

**Expected exact output:**

- a $4\times4$ rational connection in the basis
  $\delta,\delta u,\delta u^2,\delta u^3$;
- reduced output vectors;
- a rank certificate for the actual derivative-stable output span;
- complete polynomial-coefficient recurrences;
- the fixed initial data and every low-index boundary term;
- every nonnegative integer exceptional step and its continuation identity.

This computation would establish the exact recurrence. It would not by itself establish a $3$-adic normalization bound. The follow-on theorem must still bound cumulative transition loss **and endpoint observability loss** for the actual solution.

No original large $m$, original-power digit word, or endpoint expansion is required for this symbolic calculation.

---

# Final proof-status assessment

| Statement | Status |
|---|---|
| Original binary phase and degree-$81$ kernel argument | Audited proof |
| Both complete binary columns divisible by $4$ | Proved under the accepted complete parity masks |
| Total coordinate sums divisible by $8$, including original signs | Proved |
| Every integral two-column combination has norm divisible by $32$ | Proved |
| A5 symbolic mixed divisibility by $32$ | Not proved; A5 actually proves divisibility by $16$ |
| Original norm and mixed zeros modulo $2^{20}$ | Accepted finite computation, now crosschecked |
| Twenty-bit physical data determine norm modulo $2^{23}$, mixed modulo $2^{22}$ | **New proof** |
| Those additional residues | Not supplied |
| Proposed $T=36$ factorial valuation | Verified: $L(36)=34$ |
| Proposed physical head and reconstruction bounds | Not certified by the attached theorem statements |
| New-layer $P_1$ vanishing and short-factor persistence | Require new physical computation |
| Conditional new short denominator valuations $88,85$ | **Explicitly derived** |
| A3 exact seed elimination and stated odd-prime laws | Audited |
| All-prime endpoint factorization (14.1) | **New exact identity** |
| Seed-free endpoint denominator law at every $p>n$ | **New scope improvement** |
| Extra binary factor in $r_3\mathbf U$ for $n\equiv3\pmod4$ | **New proof** |
| Uniform odd-index bound $v_2(\gamma_3)\le2v_2(n!)-1$ | **New theorem** |
| A1 unrestricted exact digit-rank obstruction | Audited proof |
| Reciprocal identities | **Independently verified** |
| Joint differential rank at most four | **New proof** |
| Actual endpoint-content and split-line approach bounds | Open |
| Infinite all-prime denominator versus whole-error comparison | Open |
| Irrationality or rationality of $e+\pi$ | Unresolved |

## Conclusion

The principal new arithmetic improvement is not another ambient-state statement. It is the actual endpoint cancellation


$$
\boxed{
v_2(r_3\mathbf U)\ge v_2(n+1)+1
\quad(n\equiv3\pmod4),
}
$$


which yields


$$
\boxed{v_2(\gamma_3)\le2v_2(n!)-1}
$$


throughout the original odd-index domains.

On the binary Gram side, the audited four-divisibility of both complete columns supplies the stronger physical stability range


$$
\boxed{D_{\rm raw}\bmod2^{23},\qquad E_{\rm raw}\bmod2^{22},}
$$


but does not evaluate those digits or turn the existing zero residues into exact depths.

The reciprocal endpoint identities also reduce the exact algebraic differential problem to a four-dimensional anti-invariant subspace. The obstruction remains arithmetic: a recurrence must control the actual endpoint projection, not merely a primitive ambient state.

The exact remaining local bottlenecks are:

- certification of the proposed higher-precision physical head and finite reconstruction bounds, with both new branches and the full terminal return;
- actual higher norm/mixed residues;
- endpoint-specific seed-free residual intersection depths;
- cumulative $3$-adic normalization and observability loss for the actual endpoint solution.

The global bottleneck is unchanged:


$$
\boxed{
\text{control of the actual all-prime primitive denominator against the
whole nonzero same-index error on an infinite original sequence}.
}
$$



No unconditional proof or disproof of the irrationality of $e+\pi$ has been obtained.
