> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, turn 6 — Exact original norm depth, and a zero-separator theorem for the retained amplitudes

## Executive conclusion

The new sources close the former norm-depth uncertainty at the single original word


$$
b_0=9^{18}=150094635296999121,\qquad n_0=4002b_0.
$$



After auditing the new head, reconstruction, factor removal, payload normalization and contraction interfaces, I find **no new mathematical gap in the stated finite result**, provided the already accepted parameterized transport and finite operator identities are reused at their established scope. In particular,


$$
\boxed{v_2(D_{\rm raw})=33,\qquad v_2(E_{\rm raw})=34.}
$$


The retained exact first content is $9$, so the binary norm loss after removing that content is now exactly


$$
\boxed{33-2\cdot9=15.}
$$


Moreover,


$$
\boxed{\frac{E_{\rm raw}}{2D_{\rm raw}}\equiv49\pmod{2^7}.}
$$


The logarithmic norm-relative guard is now genuinely settled at this word. No all-prime normalization or estimate for the whole real error follows.

The new mathematical advance is a **zero-separator tensorization theorem**. It uses the actual retained short numerators, not arbitrary replacement numerators, and preserves the entire inclusive row range. It proves that sufficiently separated low and high binary blocks multiply the normalized norm and mixed form by the **same explicitly defined high-block norm**.

This has two consequences.

1. **A rigorous obstruction to a naive continuity argument.** For the family obtained by retaining the actual $u_0$ numerator arrays while varying the original binomial parameters, the normalized norm is not $2$-adically continuous at $b_0$. Along
   

$$
b_L=b_0+3\cdot2^L,\qquad L\ge135,
$$


   its first binary content remains exactly $9$, but its raw norm depth is $34$, rather than $33$. Its primitive binary norm loss is therefore $16$, rather than $15$.

2. **A target-specific conditional transfer to infinitely many original $u$.** A precise bounded operator-continuity lemma would transfer the theorem to the complete producers at
   

$$
b(u)=9^{18+32u}.
$$


   The downstream head, forcing, endpoint return, reconstruction and factor-removal continuity is proved below from the supplied source. What remains unproved from the attachments is uniform parameter continuity of the bounded operator/Schur input arrays themselves. The new theorem supplies the missing *terminal contraction mechanism* once that bounded input lemma is established; it does not merely invoke automaticity.

Thus the present turn does **not** claim an unconditional infinite-family result for the complete physical producers. It supplies a proved contraction theorem, a sharply scoped obstruction using the actual normalized amplitudes, and an explicit remaining producer lemma.

---

# 1. Scope and notation

Throughout the finite audit, retain exactly


$$
b_0=150094635296999121,\qquad
n_0=600678730458590482242,
$$




$$
N_0=n_0+2,\qquad a_0=2n_0,
$$


and the original physical row domain


$$
\boxed{0\le j\le b_0.}
$$



The complete physical columns are denoted $X,Y$, with the common row signs suppressed only in products where they cancel. The accepted content results remain


$$
\boxed{v_2(\operatorname{content}X)=9,\qquad
v_2(\operatorname{content}Y)\ge10.}
$$



The new short arrays in the receipt give integer lifts


$$
F_0(z)=\frac{A_f(z)}{(1-z)^{a_0+63}},\qquad
G_0(z)=\frac{A_e(z)}{(1-z)^{a_0+62}},
$$


with


$$
\deg A_f=63,\qquad \deg A_e=62.
$$


Their corresponding weighted columns agree with the complete physical columns modulo $2^{32}$.

These are **32-bit presentations**, not assertions that the exact complete generating functions over characteristic zero have those same short denominators.

---

# 2. Audit of the new physical provenance

## 2.1 Central series and first-force tail

The head source uses the accepted exact central formulas and evaluates the rational factors with `Fraction`. Before modular inversion it checks that the reduced denominator is odd.

For


$$
\frac{2^s(s!)^2}{(2s+\delta)!},\qquad \delta\in\{0,1\},
$$


the retained valuation identity is


$$
v_2\!\left(\frac{2^s(s!)^2}{(2s+\delta)!}\right)=v_2(s!).
$$


Consequently all $s\ge36$ have depth at least


$$
v_2(36!)=34,
$$


and are absent modulo $2^{32}$ for a proved tail reason, not because a finite sample happened to vanish.

Likewise, the first-force tail estimate


$$
v_2(\text{force term at }i)
\ge
v_2\!\left(\left\lfloor i/2\right\rfloor!\right)
$$


eliminates every $i\ge72$ modulo $2^{32}$.

The code additionally checks the finite interval $72\le i\le95$. That is a consistency check; the infinite tail justification is the retained theorem.

There is no even modular inverse in either calculation.

## 2.2 Exterior load and its terminal cancellation

The exterior factorial sequence is


$$
v_t=(b_0+1)\cdots(b_0+t),\qquad v_0=1.
$$


The source retains $v_0,\ldots,v_{35}$, verifies $v_{36}=0\pmod{2^{32}}$, and forms all $160$ exterior-load entries appropriate to bandwidth $124$.

The apparent difference between `T=36` in the head source and `T=35` in the numerator source is not a mathematical inconsistency: the retained factorial indices are $0,\ldots,35$, a list of length $36$. The latter source obtains that list from the head artifact.

The negative principal part is essential. Writing its coefficients as


$$
g_{-r}=(-1)^{r-1}v_{r-1}\qquad(1\le r\le36),
$$


the reconstruction gives


$$
(-r-b_0)g_{-r}-g_{-r-1}
=
(-1)^r\bigl((b_0+r)v_{r-1}-v_r\bigr)=0.
$$


At the last retained index the same cancellation uses $v_{36}=0\pmod{2^{32}}$.

At $k=0$, the preceding coefficient is $g_{-1}=1$, so the complete reconstructed coefficient is


$$
\boxed{-b_0g_0-1.}
$$


The source checks this explicitly. The exterior contribution has neither been omitted nor added twice.

## 2.3 Finite endpoint return

The reconstruction uses:

- the new $124$-band inverse coefficients;
- the new finite Schur inverse;
- the complete selected terminal vector;
- the corresponding `Kbar` return;
- separate returns for the first force and exponential exterior.

The first-force return is subtracted from the entire analytic source. The exponential return is combined with the entire $160$-entry exterior load before the Laurent construction.

The internal symbol $B=b_0-1$ in these formulas does **not** change the physical contraction range. The latter remains $0\le j\le b_0$.

## 2.4 What the jet checks prove

The source checks both constructions over


$$
-284\le k\le247,
$$


giving $1064$ response checks and $1064$ reconstruction checks.

These compare two separately formulated bounded constructions using shared physical input data. They are not an independently implemented transport.

Also, finite jet agreement alone would not justify an arbitrary global two-branch identity with exponents depending on $n_0$. The global interpretation continues to use the accepted algebraic source formulas, finite inverse identities, tail bounds and degree bounds. The jet checks audit that construction; they do not replace those hypotheses.

Under those retained identities, the new source correctly supplies the previously outstanding complete forcing and reconstruction data.

---

# 3. Branch disappearance and maximal factor removal

The starting reconstructed representation is


$$
z^{-284}
\left(
\frac{H_2(z)}{(1-z)^{2n_0+197}}
+
\frac{H_1(z)}{(1-z)^{n_0+1}}
\right).
$$



The relevant common exponent is therefore


$$
\boxed{2n_0+197,}
$$


not $2n_0+160$.

For both columns the source checks every coefficient of the reconstructed $n$-branch and obtains zero modulo $2^{32}$. It then checks all $284$ coefficients needed for the contact factor $z^{284}$.

After that contact removal, the numerator has degree $197$. Repeated division by $1-z$ yields:



$$
\begin{array}{c|c|c|c}
\text{column}&\text{removed factors}&\text{remaining order/degree}
&\text{next remainder}\\ \hline
\text{first}&134&63&2^{30}\\
\text{second}&135&62&2^{31}
\end{array}
$$



These are maximal multiplicities **in the polynomial ring modulo $2^{32}$**. They are not characteristic-zero multiplicity claims.

The divisions are safe over this non-field coefficient ring: $1-z$ has unit leading coefficient. The source also reconstructs the entire numerator from the quotient and all removed factors. The nonzero next remainder certifies maximality.

The old factors $44,48$ were sufficient factors, not maximality certificates. Hence the smaller new orders create no conflict.

---

# 4. Audit of the Newton payloads and nonunit divisions

For order $R$, the exact conversion is


$$
X_j
=
\frac{K(j)}{(a_0)^{\overline R}}
\sum_{r=0}^{R}A_r
(b_0-j)_{\underline r}
(a_0+b_0-j)^{\overline{R-r}},
$$


where


$$
K(j)=
\binom{N_0}{j}
\binom{a_0+b_0-j-1}{b_0-j}.
$$



## 4.1 Universal fixed divisors

Every falling product of length $r$ is divisible by $r!$, and every rising product of length $R-r$ is divisible by $(R-r)!$. Thus a universal binary fixed divisor is


$$
t_R
=
\min_r\bigl(v_2(r!)+v_2((R-r)!)\bigr)
=
v_2(R!)-\max_r v_2\binom Rr.
$$



For the actual orders:


$$
t_{63}=57,\qquad t_{62}=52.
$$



Indeed:

- $63$ has all six low bits equal to $1$, so every $\binom{63}{r}$ is odd and $t_{63}=v_2(63!)=57$;
- $v_2(62!)=57$, and the maximum binomial valuation is $5$, giving $t_{62}=52$.

These are sufficient universal fixed divisors. No claim that they equal the actual numerator-specific content is needed.

## 4.2 Denominator valuations

Since


$$
a_0\equiv132\pmod{256},
$$


the $63$-term rising interval has binary valuation


$$
32+16+8+4+2+1=63,
$$


and the $62$-term interval has valuation


$$
31+16+8+4+2+1=62.
$$



Hence the coordinate losses are


$$
63-57=6,\qquad62-52=10,
$$


and the quadratic losses are exactly


$$
\boxed{12\text{ for the norm},\qquad16\text{ for the mixed form}.}
$$



## 4.3 Newton conversion guards

The monomial payloads are computed modulo $2^{400}$. The subsequent fixed-divisor divisions need only:

- $57+57=114$ input bits for the first normalized payload;
- $57+52=109$ input bits for the second.

Thus the $400$-bit storage is more than sufficient.

The evaluations at $R+1$ consecutive integers and finite differences produce the Newton coefficients of the degree-$\le R$ integer-valued polynomial after exact division by $2^{t_R}$. No even number is inverted.

The product payload degrees are


$$
126,\qquad125.
$$



The odd denominator units are evaluated to $42$ bits, sufficient for both the $42$-bit norm and $41$-bit mixed output.

---

# 5. Contraction range and physical comparison precision

The contraction call uses exactly


$$
(N,b,C)=(n_0+2,b_0,2n_0-1)
$$


and the two new payloads at shared kernel precision $57$.

Its receipt records:

- all $71$ input digits;
- terminal state $000$;
- the original inclusive range $0\le j\le b_0$;
- the complete exterior already incorporated into the columns.

There is no change from $j\le b_0$ to $j<b_0$, no padded physical endpoint and no infinite completion of the row sum.

The transport implementation is reused. The new payload construction and its precision requirements have been separately inspected; this is not a claim of independent transport implementation.

For physical columns supplied modulo $2^{32}$, the retained contents imply


$$
D_{\rm raw}-\widetilde X^T\widetilde X\in2^{42}\mathbb Z,
$$


and


$$
E_{\rm raw}-\widetilde X^T\widetilde Y\in2^{41}\mathbb Z.
$$


The mixed bound is limited by the first content $9$; the stronger second content $10$ does not raise its minimum beyond $41$.

Thus the precision budget is


$$
42+12=54,\qquad41+16=57.
$$


A shared $57$-bit contraction is sufficient.

**Finite-audit conclusion.** The new residues have the stated physical interpretation. No additional $u_0$ operator, numerator or contraction calculation is required.

---

# 6. Exact normalized amplitudes at the original word

The residues factor as


$$
2448131358720=285\cdot2^{33},
$$




$$
223338299392=13\cdot2^{34}.
$$


Both odd factors are nonzero within the supplied precision, so


$$
\boxed{d=33,\qquad e=34}
$$


are exact.

Set


$$
x=\frac{X}{2^9},\qquad y=\frac{Y}{2^{10}},
$$


and define the whole normalized forms


$$
A=x^Tx=\frac{D_{\rm raw}}{2^{18}},
\qquad
B=x^Ty=\frac{E_{\rm raw}}{2^{19}}.
$$


Then


$$
\boxed{
A\equiv285\cdot2^{15}\pmod{2^{24}},
\qquad
B\equiv13\cdot2^{15}\pmod{2^{22}}.
}
\tag{6.1}
$$


In particular,


$$
v_2(A)=v_2(B)=15.
$$



These are statements about the entire normalized amplitude vectors, including every original row.

The ratio is


$$
\frac{E_{\rm raw}}{2D_{\rm raw}}=\frac BA.
$$


Modulo $128$,


$$
285\equiv29,\qquad29^{-1}\equiv53,
$$


so


$$
13\cdot53\equiv49\pmod{128}.
$$



Equivalently, the actual amplitudes satisfy


$$
\boxed{x^T(y-49x)\equiv0\pmod{2^{22}}.}
\tag{6.2}
$$


This is a useful target-specific formulation of the mixed cancellation. It is not a coordinatewise proportionality statement.

## 6.1 Ratio and logarithmic guards

The two ratio guards give


$$
s\le41-33-1=7,
$$




$$
s\le42-2\cdot33-1+34=9.
$$


Thus the certified absolute precision is exactly the claimed


$$
\boxed{s=7.}
$$



The retained logarithmic lower bound now gives


$$
2000b_0-138+9-33-1
=
2000b_0-163
=
300189270593998241837.
$$


It exceeds $7$ by an enormous margin.

This closes the norm-relative omission issue at $u_0$. It does not authorize deleting that contribution from the whole same-index real error.

---

# Part I. A new terminal theorem

# 7. The retained-payload family

For the next theorem, retain the **actual two short numerator arrays printed in the new receipt**, as integer arrays. For any positive integer $b$, put


$$
n=4002b,\qquad N=n+2,\qquad a=2n,
$$


and define


$$
\widehat X_j(b)
=
\binom Nj
\sum_{r=0}^{63}(A_f)_r
\binom{a+62+b-j-r}{b-j-r},
$$




$$
\widehat Y_j(b)
=
\binom Nj
\sum_{r=0}^{62}(A_e)_r
\binom{a+61+b-j-r}{b-j-r},
\qquad 0\le j\le b,
$$


with unsupported lower indices giving zero.

At $b=b_0$, these are the accepted $32$-bit physical lifts.

At other $b$, they are the **retained-payload family**. They are not yet identified with the complete physical producers there. This distinction is essential.

The following theorem evaluates how the entire finite contraction changes under a sufficiently long zero separator.

---

# 8. Zero-separator tensorization theorem

Take


$$
T=103,\qquad L\ge135,\qquad g=L-T\ge32,
$$


and


$$
b'=b_0+2^Lh,\qquad h\ge1.
$$


Put


$$
m_h=2^g h,\qquad M=2^T.
$$



For $0\le k\le m_h$, define the exact integer


$$
H_{L,h}(k)
=
\binom{4002m_hM}{kM}
\binom{(8005m_h-k)M}{(m_h-k)M},
$$


and its full finite norm


$$
\boxed{
S_{L,h}=\sum_{k=0}^{m_h}H_{L,h}(k)^2.
}
\tag{8.1}
$$



### Theorem 1 — Whole-row tensorization with the original endpoints

Write an original row of the $b'$-problem uniquely as


$$
j=j_0+Mk,\qquad0\le j_0<M.
$$



Then, modulo $2^{32}$,

- if $0\le j_0\le b_0$,
  

$$
\boxed{
  \widehat X_j(b')
  \equiv H_{L,h}(k)\widehat X_{j_0}(b_0),
  }
$$


  

$$
\boxed{
  \widehat Y_j(b')
  \equiv H_{L,h}(k)\widehat Y_{j_0}(b_0);
  }
  \tag{8.2}
$$


- if $j_0>b_0$, both coordinates vanish modulo $2^{32}$.

Consequently, over the entire original range $0\le j\le b'$,


$$
\boxed{
\widehat D(b')\equiv S_{L,h}D_{\rm raw}(b_0)\pmod{2^{42}},
}
\tag{8.3}
$$




$$
\boxed{
\widehat E(b')\equiv S_{L,h}E_{\rm raw}(b_0)\pmod{2^{41}}.
}
\tag{8.4}
$$



Every retained-payload first coordinate is divisible by $2^9$, and every retained-payload second coordinate is divisible by $2^{10}$.

## Proof

### Step 1: The low arguments fit below bit $71$

For either order $R=63,62$, every relevant low factorial argument is bounded by


$$
a_0+b_0+R-1<2^{71}.
$$


The first top is $N_0<2^{71}$.

### Step 2: Splitting a supported binomial

For $0\le v\le u<2^{71}$, the exact factorial ratio gives


$$
\frac{\binom{MA+u}{MB+v}}
{\binom{MA}{MB}\binom uv}
=
\frac{\prod_{i=1}^{u}(1+MA/i)}
{\prod_{i=1}^{v}(1+MB/i)
 \prod_{i=1}^{u-v}(1+M(A-B)/i)}.
$$


Each factor on the right is a $2$-local unit congruent to $1$ modulo


$$
2^{T-70}=2^{33}.
$$


Therefore


$$
\binom{MA+u}{MB+v}
\equiv
\binom{MA}{MB}\binom uv
\pmod{2^{32}},
\tag{8.5}
$$


with the stronger multiplicative unit statement available when needed.

Apply this to both binomials in each supported atom. The high factors are independent of $R$ and $r$, and their product is precisely $H_{L,h}(k)$.

### Step 3: Unsupported low shifts cannot leak through the separator

For an atom with shift $r$, let


$$
B_r=b_0-r,\qquad C_R=a_0+R-1,\qquad S_r=C_R+B_r.
$$


Their order is


$$
B_r<N_0<S_r<2^{71}.
$$



If $j_0>B_r$, the borrow state after $T$ bits is one of


$$
010,\quad110,\quad111.
$$


Across the next $g$ positions the fixed parameter bits are all zero. Such a state either remains unchanged or becomes $111$; its valuation cost at every position is at least one.

Thus every globally supported atom whose low shift is unsupported acquires at least $g\ge32$ factors of $2$. Globally unsupported atoms are already zero.

This proves both the zero assertion for $j_0>b_0$ and the correct zero interpretation of individual shifts near the low endpoint.

### Step 4: The endpoint is exact

The rows


$$
j=j_0+Mk,\qquad
0\le j_0\le b_0,\quad0\le k\le m_h,
$$


all satisfy


$$
j\le b_0+Mm_h=b'.
$$


The terminal row $k=m_h,\ j_0=b_0$ is included.

All other original rows contribute zero modulo $2^{32}$. No nonzero endpoint term has been added or discarded.

### Step 5: Passing to the quadratic forms

The model rows in (8.2) have contents at least $9,10$. A coordinatewise error divisible by $2^{32}$ therefore changes the first norm only by a multiple of $2^{42}$, and the mixed form only by a multiple of $2^{41}$.

Summing all rows proves (8.3)–(8.4). ∎

This is a terminal theorem for the entire contraction, not a fixed-row continuity statement.

---

# 9. Consequences for the actual normalized amplitudes

Define


$$
\widehat A(b')=\frac{\widehat D(b')}{2^{18}},
\qquad
\widehat B(b')=\frac{\widehat E(b')}{2^{19}}.
$$


Theorem 1 and (6.1) yield


$$
\boxed{
\widehat A(b')
\equiv285\cdot2^{15}S_{L,h}\pmod{2^{24}},
}
\tag{9.1}
$$




$$
\boxed{
\widehat B(b')
\equiv13\cdot2^{15}S_{L,h}\pmod{2^{22}}.
}
\tag{9.2}
$$



If


$$
t=v_2(S_{L,h})\le6,
$$


both depths are determined:


$$
\boxed{
v_2(\widehat D(b'))=33+t,\qquad
v_2(\widehat E(b'))=34+t.
}
\tag{9.3}
$$


The same high-block factor cancels from the mixed ratio, giving


$$
\boxed{
\frac{\widehat E(b')}{2\widehat D(b')}
\equiv49\pmod{2^{7-t}}.
}
\tag{9.4}
$$



The precision loss $t$ is explicit. No assertion that the high-block norm is a unit has been smuggled into the cancellation.

---

# Part II. A sharply scoped obstruction

# 10. The high-block parity is explicit

By Lucas’s theorem, odd $H_{L,h}(k)$ require


$$
k=2^g\ell.
$$


Their parity then equals the parity of


$$
\binom{4002h}{\ell}
\binom{8005h-\ell}{h-\ell}.
$$



Hence


$$
S_{L,h}
\equiv
\sum_{\ell=0}^{h}
\binom{4002h}{\ell}
\binom{8005h-\ell}{h-\ell}
\pmod2.
$$


The sum is the coefficient of $z^h$ in


$$
(1+z)^{4002h}(1-z)^{-8004h-1}.
$$


Modulo $2$, this becomes $(1-z)^{-4002h-1}$, so


$$
\boxed{
S_{L,h}\equiv\binom{4003h}{h}\pmod2.
}
\tag{10.1}
$$



In particular, if $h\equiv3\pmod4$, then $h$ and $4002h$ both have bit $1$ set. Their addition has a carry, and


$$
\boxed{2\mid S_{L,h}.}
\tag{10.2}
$$



This conclusion comes from the full high-block contraction, including its terminal range.

---

# 11. An exact two-odd-row calculation at $h=3$

For $h=3$,


$$
4002h=12006\equiv2\pmod4,\qquad
8004h=24012\equiv0\pmod4.
$$



Among $\ell=0,1,2,3$, the first binomial is odd exactly for


$$
\ell=0,2.
$$


For both choices the second binomial is also odd.

Thus exactly two high-block entries are odd. Every odd square is $1\pmod4$, and every even square is $0\pmod4$. Therefore


$$
\boxed{S_{L,3}\equiv2\pmod4,\qquad v_2(S_{L,3})=1.}
\tag{11.1}
$$



This is an evaluated exact arithmetic argument. It does not require construction of the enormous high-block norm.

At $k=0$, $H_{L,3}(0)$ is odd. The retained attaining row $j_*$ therefore still gives


$$
\widehat X_{j_*}(b_0+3\cdot2^L)
\equiv\text{odd}\cdot512\pmod{1024}.
$$


Consequently the first binary content remains exactly $9$.

We have proved:

### Theorem 2 — Failure of norm-depth continuity for the retained actual payload

For every $L\ge135$, let


$$
b_L=b_0+3\cdot2^L.
$$


Then the retained-payload family satisfies


$$
\boxed{
v_2(\operatorname{content}\widehat X(b_L))=9,
}
$$




$$
\boxed{
v_2(\widehat D(b_L))=34,\qquad
v_2(\widehat E(b_L))=35,
}
$$


and


$$
\boxed{
\frac{\widehat E(b_L)}{2\widehat D(b_L)}
\equiv49\pmod{64}.
}
$$



Its first primitive binary norm loss is exactly


$$
\boxed{34-18=16.}
$$



Yet $b_L\to b_0$ in $\mathbb Z_2$, while the original primitive binary norm loss is $15$.

Thus the normalized norm map for this retained actual payload is **not $2$-adically continuous at $b_0$**.

### Exact scope of the obstruction

This disproves a continuity claim for the complete finite contraction of the retained $u_0$ payload. It uses the actual normalized norm and mixed amplitudes (6.1), not the already closed observation that one sixteen-row block has depth $22$.

It does **not** prove that the complete physical producers at $b_L$ use the same numerator arrays. That requires the producer-continuity lemma below.

Nor does it disprove a correctly formulated stability theorem with a high-block multiplier. Theorem 1 supplies precisely such a theorem.

---

# 12. Infinitely many original parameters exhibit the separator obstruction

Let


$$
q=9^{32}.
$$


The lifting-the-exponent formula gives


$$
v_2(q-1)=8,
\qquad
v_2(q^u-1)=8+v_2(u)\quad(u\ne0).
$$


Thus modulo $2^K$, $q$ generates the subgroup


$$
1+256\mathbb Z/2^K\mathbb Z.
$$



For any fixed $L\ge135$, the congruence


$$
b_0q^u\equiv b_0+3\cdot2^L\pmod{2^{L+2}}
$$


therefore has a residue class of solutions


$$
u\pmod{2^{L-6}}.
$$


It contains infinitely many nonnegative original indices.

For all those indices,


$$
b(u)=b_0+2^Lh,\qquad h\equiv3\pmod4.
$$


Consequently Theorem 1 and (10.2) prove, for the retained-payload family on these original parameters,


$$
\boxed{
v_2(\widehat D(b(u)))\ge34,\qquad
v_2(\widehat E(b(u)))\ge35.
}
\tag{12.1}
$$



This is an unconditional infinite-family statement for the precisely defined retained-payload family. It is not yet an unconditional infinite-family statement for the complete physical producers.

In particular, a fixed low residue of $b$, however long, does not force the $u_0$ norm depth even when the numerator arrays themselves are held fixed.

---

# Part III. The precise transfer to the complete producers

# 13. Downstream producer continuity is provable from the supplied source

At precision $32$, the supplied head and numerator sources read the bounded arrays


$$
\lambda,\quad CC,\quad \overline K,\quad S_{\rm end}^{-1}.
$$



The following lemma isolates their role.

### Lemma 3 — Complete downstream continuity

Suppose $b'\equiv b_0\pmod{2^{41}}$, $n'=4002b'$, and the four bounded operator/Schur arrays above agree with their $b_0$ values modulo $2^{32}$.

Then the supplied head and numerator formulas produce the same, modulo $2^{32}$,

- complete first-force head;
- factorial exterior and complete exterior load;
- both endpoint returns;
- both Laurent branches;
- complete reconstruction, including the terminal $-bg_0-1$;
- branch-zero decisions and contact factor;
- maximal $1-z$ division results and short numerator arrays.

## Proof

For every fixed $r\ge1$,


$$
\binom{x+2^Lt}{r}-\binom xr
=
\sum_{i=1}^{r}\binom{2^Lt}{i}\binom{x}{r-i}.
$$


Since


$$
v_2\binom{2^Lt}{i}\ge L-v_2(i),
$$


the difference is divisible by


$$
2^{L-\lfloor\log_2r\rfloor}.
\tag{13.1}
$$



Every variable-top binomial in the supplied downstream construction has lower index at most $531$. Since


$$
\lfloor\log_2 531\rfloor=9,
$$


parameter agreement modulo $2^{41}$ gives agreement modulo $2^{32}$.

The central parameter is


$$
n/2=2001b,
$$


so there is no hidden loss from division by $2$ along the assigned family.

All remaining operations are:

- integral sums and products;
- multiplication by fixed rational constants with odd reduced denominator;
- multiplication by the assumed congruent bounded arrays;
- coefficient shifts;
- division by the unit polynomial $1-z$.

The terminal sign depends only on the parity of $b$, which is unchanged.

The tail bounds are uniform here: $T=36$, $I=72$, $m=124$, $R=160$ remain valid, and the absolute logarithmic omission bound remains more than sufficient for these larger positive parameters.

Thus every downstream array, including both complete returns and reconstructions, is unchanged modulo $2^{32}$. ∎

This is a statement about the complete supplied formulas, not merely their first few output coefficients.

---

# 14. The remaining bounded producer lemma

The missing premise is now explicit.

> **Operator-parameter continuity lemma (OPC).**  
> There is an explicit integer $C$ such that, for every original positive parameter $b\equiv b_0\pmod{2^C}$, the precision-$32$ arrays
> 

$$
> \lambda(b),\quad CC(b),\quad \overline K(b),\quad S_{\rm end}(b)^{-1}
>
$$


> agree modulo $2^{32}$ with their $b_0$ arrays, with the same finite boundary construction.

The attached downstream sources read these arrays from an artifact. Their inspected $u_0$ values do not prove OPC for other parameters.

This is not a defect in the accepted finite computation. It is an unproved family premise.

## 14.1 What OPC would immediately prove

Assume OPC and choose


$$
L\ge\max(135,C).
$$


Then Lemma 3 identifies the complete physical columns modulo $2^{32}$ with the retained-payload columns at every original $b(u)\equiv b_0\pmod{2^L}$.

Theorem 1 then applies to the **complete physical contraction**, including the finite return and terminal exterior.

In particular, the infinite original residue class constructed in §12 would satisfy


$$
v_2(D_{\rm raw}(u))\ge34,\qquad
v_2(E_{\rm raw}(u))\ge35,
$$


with first content at least $9$ and second content at least $10$.

More generally, whenever the associated high factor has exact depth $t\le6$,


$$
v_2(D_{\rm raw}(u))=33+t,\qquad
v_2(E_{\rm raw}(u))=34+t,
$$


and


$$
\frac{E_{\rm raw}(u)}{2D_{\rm raw}(u)}
\equiv49\pmod{2^{7-t}}.
$$



That would be a genuine infinite-family mechanism, not an extrapolation of the original $71$-digit receipt.

It would still not determine the actual first content when the high block has no unit coordinate, nor the final all-prime denominator.

---

# 15. A bounded certificate for OPC—not a rerun of the operator calculation

The appropriate next bounded task is a **symbolic parameter-continuity certificate**, not another evaluation of the accepted $u_0$ arrays.

### Inputs

The exact fixed-precision formulas for the finite entries generating


$$
\lambda,\quad CC,\quad\overline K,\quad S_{\rm end}.
$$



### Required certificate

For each relevant scalar input, exhibit a representation with:

1. a proved finite degree bound;
2. an integer-valued numerator, with any fixed nonunit denominator explicitly recorded;
3. a denominator unit on the original parameter class.

For example, if an entry is represented as


$$
f(b)=\frac{P(b)}{2^cU(b)},
$$


where $P\in\operatorname{Int}_{\le d}(\mathbb Z)$ and $U$ is an integer polynomial odd on the parameter class, then (13.1) supplies a continuity bound from


$$
L\ge32+c+\lfloor\log_2\max(1,d)\rfloor,
$$


together with the corresponding unit-denominator congruence.

For the matrix inverse, use the exact identity


$$
S(b)^{-1}-S(b_0)^{-1}
=
S(b)^{-1}\bigl(S(b_0)-S(b)\bigr)S(b_0)^{-1}.
$$


Once both matrices are units over $\mathbb Z_{(2)}$, inversion loses no binary precision.

### Expected verifiable output

An explicit $C$, all nonunit guards, and the uniform conclusion in OPC.

This task does not recompute the accepted operator values. It proves how their defining finite formulas vary with the parameter.

The small high-block arithmetic needed for Theorem 2 is already completed in §11: its inputs are $h=3$, $4002h=12006$, $8004h=24012$, and its verifiable output is exactly two odd high-block entries and


$$
S_{L,3}\equiv2\pmod4.
$$



---

# 16. What the new theorem controls—and what it does not

The zero-separator theorem controls:

- both retained numerator arrays;
- every original row $0\le j\le b'$;
- unsupported shifts near the endpoint;
- the inclusive terminal row;
- first and second binary content lower bounds;
- the whole norm and mixed form to their stated precisions;
- a common high-block multiplier;
- the guarded mixed ratio when that multiplier has sufficiently small exact depth.

After OPC, the same statements would control the complete physical producers, including their bounded endpoint returns.

It does **not** control:

- odd-prime row contents;
- the least actual common clearer;
- the final all-prime gcd;
- the actual primitive denominator;
- the whole signed real approximation error;
- nonvanishing of that whole error on an infinite original sequence.

No Hahn-measure identification, generic automaticity theorem, or unrestricted lattice argument supplies those missing conclusions. The proofs above instead use the exact binomial atoms, their original endpoint and the actual retained amplitudes.

---

# 17. All-prime normalization and the whole same-index error

Retain the complete integer columns and


$$
A_B=N_{B,1}^{T}\Omega N_{B,1},
\qquad
H_B=N_{B,1}^{T}\Omega N_{B,2}.
$$


The final normalization remains


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=\frac{A_B}{g_B},\qquad
p_n=\frac{H_B}{g_B}.
}
$$


With the least actual common clearer $d_B$, the actual primitive multiplier is


$$
\boxed{\frac{d_B^2}{g_B}.}
$$



Neither the first content $2^9$, nor the normalized norm loss $15$, nor a common binary high-block factor is a replacement for this all-prime gcd.

The approximation quantity remains


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n,
}
$$


with the **whole same-index** error $\epsilon_n$.

An irrationality proof still requires an infinite original sequence on which the whole form is nonzero and tends to zero after multiplication by the actual primitive denominator. No such conclusion has been established here.

---

# 18. Proof-status ledger

| Statement | Status |
|---|---|
| Complete physical $32$-bit head, force, exterior and finite return at $u_0$ | Accepted new finite computation, audited here |
| Both reconstructed $n$-branches vanish modulo $2^{32}$ | Accepted new finite computation |
| Contact $z^{284}$ and maximal factors $134,135$ | Accepted new finite computation, with unit-division audit |
| Short orders $63,62$, fixed divisors $57,52$, losses $12,16$ | Explicitly justified |
| Full $71$-digit norm/mixed contraction with original endpoint | Accepted new finite computation |
| $v_2(D_{\rm raw})=33,\ v_2(E_{\rm raw})=34$ | Rigorous finite conclusion |
| First primitive binary norm loss $15$ | Rigorous deduction from retained exact content |
| $E_{\rm raw}/(2D_{\rm raw})=49\pmod{128}$ | Rigorous guarded deduction |
| Original norm-relative logarithmic guard | Closed |
| Zero-separator whole-row and whole-contraction theorem | **Proved here** |
| Retained actual payload has exact loss $16$ along $b_0+3\cdot2^L$ | **Proved here** |
| Failure of normalized-norm continuity for that retained payload | **Proved here**, sharply scoped |
| Infinite original residue classes with retained-payload depths at least $34,35$ | **Proved here** |
| Downstream complete-producer continuity given bounded input-array continuity | **Proved here** |
| OPC for the actual operator/Schur formulas | Open bounded symbolic lemma |
| Infinite-family transfer to complete physical producers | Conditional on OPC |
| All-prime primitive denominator versus whole nonzero error | Open |
| Irrationality or rationality of $e+\pi$ | Unresolved |

---

## Conclusion

The former $u_0$ norm-depth bottleneck is closed:


$$
\boxed{
d=33,\qquad e=34,\qquad
\text{first primitive binary norm loss}=15,\qquad
E/(2D)\equiv49\pmod{128}.
}
$$



The new result is an explicit terminal mechanism:


$$
\boxed{
\text{actual retained low amplitudes}
\quad\longrightarrow\quad
\text{whole-row tensorization}
\quad\longrightarrow\quad
\text{a common high-block norm multiplier}.
}
$$



It proves that naive low-parameter continuity of the normalized norm is false even for the actual retained payload. The appropriate family statement must include the high-block contraction; it cannot simply freeze the original depth $33$.

The next mathematical obligation is now concrete:


$$
\boxed{
\text{prove uniform parameter continuity of the bounded operator/Schur inputs,
then apply the proved terminal theorem}.
}
$$


The required bounded work is a symbolic continuity certificate with explicit nonunit guards, not a rerun of any accepted $u_0$ calculation.

Even after that transfer, the ultimate bottleneck remains


$$
\boxed{
\text{the actual all-prime primitive denominator versus the whole,
nonzero same-index error on an infinite original sequence}.
}
$$



No unconditional proof or disproof of the irrationality of $e+\pi$ has been obtained.
