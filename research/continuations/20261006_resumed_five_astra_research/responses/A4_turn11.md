> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4, Turn 11 — Audit of the complete physical $32$-bit pipeline, the $29$-adic norm reduction, and the remaining primitive-denominator obstruction

## Executive conclusions

The new execution evidence closes the previously outstanding original-$u_0$ binary computation. After auditing the supplied source, its divisions, its finite ranges, and its physical comparison precision, I accept


$$
\boxed{
D_{\rm raw}\equiv2448131358720\pmod{2^{42}},
\qquad
E_{\rm raw}\equiv223338299392\pmod{2^{41}}.
}
$$


These imply the **exact**, rather than lower-bound, valuations


$$
\boxed{
v_2(D_{\rm raw})=33,\qquad v_2(E_{\rm raw})=34.
}
$$


Together with the retained exact first-column content $c_2(X)=9$, they give


$$
\boxed{v_2\!\left((X/2^9)^T(X/2^9)\right)=15.}
$$


The guarded local quotient is


$$
\boxed{\frac{E_{\rm raw}}{2D_{\rm raw}}\equiv49\pmod{2^7}.}
$$



The complete physical producer passes audit at its stated scope:

- $T=36,\ I=72,\ m=124,\ R=160$;
- both complete force-dependent finite returns;
- all principal parts and the exterior contribution producing $-b\,g_0-1$;
- starting denominator exponent $2n+197$;
- both reconstructed $n$-branch zero decisions modulo $2^{32}$;
- contact divisibility by $z^{284}$;
- maximal certified $(1-z)$-factor counts $134,135$, **in the modular polynomial presentations actually computed**;
- short orders $63,62$;
- fixed divisors $57,52$, denominator valuations $63,62$, and quadratic normalization losses $12,16$.

The shared $57$-bit transport is reused, not independently reimplemented. The new result is one original word, not an infinite-family theorem.

For A2 turn 7, I accept the complete norm-only reduction


$$
\boxed{
\eta=A_0^2\kappa(b,n),\qquad
\kappa(b,n)=
\frac1{29^7}
\sum_{j=0}^{b-1}
\binom{n+2}{j}^{2}
\binom{2n+b-1-j}{b-1-j}^{2}
\pmod{29}.
}
$$


The whole finite sum, not a termwise quotient, is divided by $29^7$. The compatible $\mathsf D_2$, crossed $\mathsf D_1z_1$, complete second finite return, and terminal coordinate are retained before elimination.

One wording in the first-lower denominator argument requires clarification: a falling product can contain a factor of valuation two while the corresponding binomial coefficient, after division by $29!$, has valuation only one. Paying that factorial division explicitly repairs the argument; it does not overturn the reduction.

The corrected leading coefficients remain


$$
\boxed{21,-21\pmod{29}.}
$$


The value of $\kappa$ remains unevaluated.

Two further consequences are proved below.

1. **The sixteen-row normalized Gram decomposition extends to the full new physical norm precision.** With the new $32$-bit lifts, its normalized residual is determined modulo $2^{20}$, and equals
   

$$
\boxed{\frac{D_{\rm raw}}{2^{22}}\equiv583680
   =2^{11}\cdot285\pmod{2^{20}}.}
$$


   Thus the normalized cross-block sum has exact valuation $11$. This is still a single-word result.

2. **The complete $29$-adic next-norm residue vanishes infinitely often in every original arithmetic progression.** Consequently, any nonzero value of that residue is necessarily a point of failure of congruence-local constancy on the original index set. This strengthens the previous fixed-prefix conditional rigidity statement, but does not prove that the residue is identically zero.

No code was executed for this report. No accepted bounded calculation is proposed for repetition.

The irrationality or rationality of $e+\pi$ remains unresolved.

---

# I. Audit conventions and preserved mathematical objects

The binary and $29$-adic families must remain distinct.

For the new binary calculation,


$$
b=9^{18}=150094635296999121,\qquad
n=4002b=600678730458590482242,
$$


and every contraction retains


$$
\boxed{0\le j\le b.}
$$



For A2,


$$
p=29,\qquad
b=3^{249005515+574312172u},\qquad n=2001b,\qquad u\ge0.
$$


The three domains remain:

- contact coordinates: $0\le j<b$;
- source rows: $1\le i\le b-2$;
- reconstructed coordinates: $0\le j\le b$.

In particular,


$$
Z_w=\mathcal RA^{-1}f^0,\qquad
Y=\mathcal RA^{-1}\mathbf r+W_be_b
$$


are not replaced by truncated or homogeneous columns.

I distinguish the following kinds of evidence throughout:

- **Proof:** an algebraic, valuation, or finite-boundary argument establishing the claimed scope.
- **Audited finite execution:** a supplied receipt whose mathematical interpretation and inspected source are consistent.
- **Conditional deduction:** a consequence requiring a stated additional hypothesis.
- **Unevaluated specification:** a precisely defined arithmetic task without an output.

The supplied artifact hashes identify the intended dependency chain. They do not turn a computation into an independent implementation, nor do labels such as “PASS” substitute for checking its mathematics.

---

# II. Priority 1: the complete original-$u_0$ physical $32$-bit pipeline

## 1. The head producer preserves the established tail contract

The head source uses


$$
Q=2^{32},\qquad h=n/2.
$$



### 1.1 Central terms

Every rational central factor is formed first as an exact `Fraction`. Its denominator is asserted odd before reduction modulo $Q$. Thus no inverse of an even denominator is used.

The retained tail theorem is


$$
v_2\!\left(\frac{2^s(s!)^2}{(2s+\delta)!}\right)
=v_2(s!),\qquad \delta=0,1.
$$


Since


$$
v_2(36!)=34,
$$


the loop $0\le s<36$ is justified modulo $2^{32}$.

The calculation of $96$ central coefficients is bounded corroboration. The reason all omitted central terms vanish is the tail theorem, not the number of coefficients evaluated.

### 1.2 First force

The first-force source evaluates


$$
f_i=\sum_{\ell=0}^{i}
\binom i\ell
\left(\prod_{t=\ell+1}^{i}(n+t)\right)B_\ell
\pmod{2^{32}}.
$$


All factors are integral.

The retained estimate


$$
v_2(\text{first-force term at }i)
\ge
v_2\!\left(\left\lfloor i/2\right\rfloor!\right)
$$


makes $i\ge72$ negligible modulo $2^{32}$. The source additionally checks $f_{72},\ldots,f_{95}=0$, but does not rely on that finite zero interval to prove the infinite tail.

The receipt’s head length $72$, minimum depth $0$, and $66$ nonzero residues are consistent with the actual calculation.

### 1.3 Exterior load

The factorial exterior is


$$
v_t=(b+1)\cdots(b+t),\qquad v_0=1.
$$


Its tail satisfies


$$
v_2(v_t)\ge v_2(t!).
$$


The source retains $v_0,\ldots,v_{35}$, verifies $v_{36}=0\bmod2^{32}$, and forms:

- an upper exterior load of length $36$;
- the complete operator-acted exterior load of length $160=124+36$.

The apparently different declaration `T = 35` in the numerator source is the **largest retained exterior index**. It is not a change from the tail cutoff $T=36$.

The source also retains the previously proved absolute logarithmic omission bound. It does not use that absolute omission, by itself, as a norm-relative omission theorem.

**Conclusion:** the new head and complete exterior load are accepted at physical precision $32$, using the retained tail proofs.

---

## 2. Finite Schur loads and Laurent dimensions

The new numerator source reuses the certified $124$-band operator and finite Schur inverse. It does not regenerate or replace that accepted stage.

The force-dependent loads are solved through the retained reversal/sign selection and


$$
\mathrm{KBAR}\,\mathrm{SINV}.
$$


Both columns receive their own solved finite return.

The Laurent dimensions are


$$
I=72,\quad m=124,\quad R=160,\quad
L_0=284,\quad K_0=196,
$$


with


$$
\mathrm{JET}=247,\qquad \mathrm{MAX}=371.
$$



The source indexing is consistent:

- the largest inverse-power index used in the jet calculations is
  

$$
371+159+1=531=247+284;
$$


- the head polynomial has exponents $0,\ldots,71$;
- exterior source exponents lie between $-160$ and $-1$;
- the table of rising binomial factors covers all required source and prefix indices.

For a source term with Laurent exponent $r$, derivative indices $0\le e\le s\le124$, and extra denominator offset $0$ or $72$, the construction uses


$$
r-s+e+284,\qquad 196-\mathrm{extra}-e.
$$


Both are nonnegative in every retained case.

For the $2n$-branch,


$$
(r-s+e+284)+(196-\mathrm{extra}-e)
=480+r-s-\mathrm{extra}\le479.
$$


This explains the degree bound $479$, rather than inferring it from the output.

The reconstruction is the exact operation


$$
(z\partial_z-b-z)
\left(z^{-284}\frac{H(z)}{(1-z)^\lambda}\right),
$$


so it raises the denominator exponent by one and the numerator degree by at most two. The resulting presentation is therefore


$$
\boxed{
z^{-284}
\left(
\frac{H_2(z)}{(1-z)^{2n+197}}
+
\frac{H_1(z)}{(1-z)^{n+1}}
\right).
}
$$


The degree bounds $481$ and $285$ agree with the allocated arrays.

No order-$160$ denominator is used.

---

## 3. The jet and terminal checks have the claimed ranges

There are


$$
247-(-284)+1=532
$$


indices in the range


$$
-284\le k\le247.
$$


Checking two columns therefore gives


$$
2\cdot532=\boxed{1064}
$$


source-jet checks, and the same number of reconstructed checks.

The negative exponential principal parts are retained. At $k=0$, the preceding exterior coefficient is $1$, giving


$$
(k-b)g_k-g_{k-1}\big|_{k=0}
=
\boxed{-b\,g_0-1}.
$$


The source explicitly checks this identity. It does not substitute $-b\,g_0$, and it does not add a second copy of the exterior correction.

The rational numerator formula is derived algebraically, including prefix subtraction from the **whole** analytic source. Consequently, the conclusion is not an extrapolation from $532$ checked coefficients to an arbitrary series. The finite jet comparisons independently corroborate an already specified rational construction.

That distinction matters: finitely many coefficients alone would not justify arbitrary cancellation between two unrelated huge-exponent branches.

---

## 4. Branch disappearance and factor removal

The receipt reports, coefficientwise modulo $2^{32}$,

- both reconstructed $n$-branches are zero;
- both surviving $2n$-branch numerators are divisible by $z^{284}$;
- the post-contact numerator degree is $197$ before $(1-z)$-division.

The division algorithm for $1-z$ is exact in $(\mathbb Z/2^{32}\mathbb Z)[z]$. If


$$
P(z)=(1-z)Q(z)+r,
$$


its recursive coefficient construction gives $r=P(1)$. Since the leading coefficient of $1-z$ is a unit, no binary precision is lost.

The source also rebuilds all removed factors and compares the result with the original post-contact numerator.

The two first failed division remainders are


$$
2^{30},\qquad 2^{31},
$$


both nonzero modulo $2^{32}$. Thus the certified factor counts are maximal for these modular polynomial presentations:


$$
\boxed{134,\qquad135.}
$$


They leave


$$
197-134=63,\qquad197-135=62,
$$


as reported.

This establishes


$$
\boxed{
\widetilde F=\frac{A_{63}}{(1-z)^{2n+63}},
\qquad
\widetilde E=\frac{B_{62}}{(1-z)^{2n+62}}
\pmod{2^{32}}.
}
$$



“Maximal” here does **not** assert an exact characteristic-zero factorization of an unspecified higher-precision producer.

The old $44/48$ factors were chosen sufficient factors, not asserted maximal factors. Their counts alone are no contradiction to the new orders.

---

## 5. The exact fixed-divisor normalization

Put


$$
a=2n,\qquad
K(j)=\binom{n+2}{j}\binom{a+b-j-1}{b-j}.
$$


For a numerator of degree at most $R$, the exact shift identity is


$$
\binom{n+2}{j}
[z^{b-j}]\frac{\sum_{r=0}^R A_rz^r}{(1-z)^{a+R}}
=
\frac{K(j)}{(a)^{\overline R}}\,U_R(j),
$$


where


$$
U_R(j)=
\sum_{r=0}^R
A_r(b-j)_{\underline r}
(a+b-j)^{\overline{R-r}}.
$$


This is precisely the polynomial constructed by the new source.

Every product


$$
(b-j)_{\underline r}
(a+b-j)^{\overline{R-r}}
$$


is divisible, as an integer-valued polynomial, by


$$
r!(R-r)!.
$$


Hence the universal binary fixed divisor is


$$
t_R=\min_r\{v_2(r!)+v_2((R-r)!)\}
=v_2(R!)-\max_rv_2\binom Rr.
$$



### Order $63$

Since $63$ has all six low bits set, every $\binom{63}{r}$ is odd. Thus


$$
t_{63}=v_2(63!)=63-6=\boxed{57}.
$$



### Order $62$

Here


$$
v_2(62!)=62-5=57,
$$


and the maximum binomial valuation is $5$, attained at $r=31$. Therefore


$$
t_{62}=57-5=\boxed{52}.
$$



### Denominator valuations

The relevant interval begins at


$$
a\equiv132\pmod{256}.
$$


For length $63$, the valuations are those of $132,\ldots,194$:


$$
32+16+8+4+2+1=\boxed{63}.
$$


For length $62$, they are those of $132,\ldots,193$:


$$
31+16+8+4+2+1=\boxed{62}.
$$



Writing the odd denominator units as $d_f,d_e$, the column losses are


$$
63-57=6,\qquad62-52=10.
$$


The quadratic losses are consequently


$$
\boxed{12\quad\text{and}\quad16.}
$$



---

## 6. Newton conversion and payload precision

The source constructs $U_f,U_e$ modulo $2^{400}$, then evaluates the fixed-divisor quotients at enough consecutive integers to determine their Newton coefficients.

The required predivision moduli are only


$$
2^{57+57}=2^{114},
\qquad
2^{57+52}=2^{109}.
$$


Thus the $400$-bit polynomial coefficients are more than sufficient.

At each sampled integer, exact divisibility by the relevant $2^{t_R}$ is checked before shifting. Taking forward differences of the quotient values is legitimate because the quotient is an integer-valued polynomial.

The normalized degrees are


$$
63,\qquad62.
$$


Accordingly,

- the squared payload has degree at most $126$;
- the mixed payload has degree at most $125$.

The source uses $127$ and $126$ values, respectively. These are exactly sufficient.

The integer representatives of the $32$-bit numerator coefficients are used to define exact integral lifts. Their computation at higher internal precision does not manufacture additional physical coefficient precision; that precision is supplied only by the comparison argument below.

---

## 7. Physical comparison precision

Let the complete physical columns be $X,Y$, and the new integral short lifts be $\widetilde X,\widetilde Y$. Then


$$
X-\widetilde X,\quad Y-\widetilde Y
\in2^{32}\mathbb Z^{b+1}.
$$


The retained content theorem gives


$$
X,\widetilde X\in2^9\mathbb Z^{b+1},
\qquad
Y,\widetilde Y\in2^{10}\mathbb Z^{b+1}.
$$



Writing $X=\widetilde X+2^{32}h$,


$$
X^TX-\widetilde X^T\widetilde X
=
2^{33}\widetilde X^Th+2^{64}h^Th
\in2^{42}\mathbb Z.
$$


Similarly,


$$
X^TY-\widetilde X^T\widetilde Y\in2^{41}\mathbb Z.
$$


The mixed term involving $\widetilde X$ limits the latter precision to $41$, even with the stronger second-column content.

Therefore the correct physical targets are


$$
\boxed{M_D=42,\qquad M_E=41.}
$$



The required dividend precisions are


$$
42+12=54,\qquad41+16=57.
$$


A shared $57$-bit contraction is sufficient. The source reduces the norm dividend to $54$ bits before its $12$-bit division and retains all $57$ mixed bits before its $16$-bit division.

All remaining inversions are of odd units.

The retained transport consumes $71$ digits and accepts terminal state $000$, preserving the inclusive finite range $0\le j\le b$. Its $524$ transitions and $10078$ valuation-degree checks are finite execution evidence for this word and these payloads.

---

## 8. Exact depths and the quotient guard

The reported residues factor as


$$
2448131358720=2^{33}\cdot285,
$$




$$
223338299392=2^{34}\cdot13.
$$


Both odd quotients are visible below the certified moduli. Hence


$$
\boxed{v_2(D_{\rm raw})=33,\qquad v_2(E_{\rm raw})=34.}
$$



Since the first column’s content is exactly $2^9$ at the prime $2$,


$$
\boxed{\nu_2=33-18=15.}
$$



For absolute $s$-bit accuracy in $E/(2D)$, denominator perturbation and numerator perturbation require


$$
M_E-d-1\ge s,
\qquad
M_D+e-2d-1\ge s.
$$


Here these margins are


$$
41-33-1=7,\qquad
42+34-66-1=9.
$$


Thus $s=7$ is valid.

Moreover,


$$
\frac{E_{\rm raw}}{2D_{\rm raw}}
\equiv\frac{13}{285}
\equiv\frac{13}{29}\pmod{128}.
$$


Since


$$
29^{-1}\equiv53\pmod{128},
$$


the quotient is


$$
13\cdot53\equiv\boxed{49}\pmod{128}.
$$



The norm-relative logarithmic guard now also has a valid upper norm depth to use:


$$
2000b-138+9-33-1
=
\boxed{300189270593998241837}.
$$


It comfortably exceeds $7$.

This closes that **local quotient omission guard**. It does not remove the logarithmic contribution from the whole real approximation error.

---

# III. A sharper interpretation of the sixteen-row decomposition

## 9. Audit of the portion of A5 needed here

A5’s block argument uses more than equal row valuations:

1. valuation-eight rows form octets at bits $38,41,52$;
2. valuation-nine rows form quartets at bits $41,52$;
3. complete kernel rows have a common odd multiplier under these toggles;
4. active octets pair under bit $6$;
5. the paired first-column normalized coordinates have the same parity.

The fixed-divisor identity and $v_2(K(j))\ge10$ give


$$
h_r(j')-u h_r(j)\in2^{t-3}\mathbb Z_{(2)}
$$


for a toggle at bit $t$. The lowest precision used on an active octet is therefore $35$, from $t=38$.

A5’s odd-factorial locality argument establishes:

- an octet weight $\sigma\equiv8\pmod{16}$, so $\alpha=\sigma/8$ is odd;
- a quartet weight $\sigma_{\mathcal Q}\equiv4\pmod8$, so $\beta=\sigma_{\mathcal Q}/4$ is odd;
- agreement of paired high-toggle unit ratios modulo $2^p$ for $p\le31$.

These are sufficient for the displayed normalized matrix. In particular, no polarization shortcut is used to infer mixed depth from norm depth.

The exact local block-$22$ conclusion survives:


$$
v_2\!\left(\sum_{\text{an odd-support sixteen-row block}}X_j^2\right)=22.
$$



---

## 10. New theorem: the block decomposition at the full new norm precision

The new short numerators can be placed over the old common order $81$:


$$
A_{63}(z)(1-z)^{18},
\qquad
B_{62}(z)(1-z)^{19}.
$$


Both have degree at most $81$ and integral coefficients. Thus the same whole-row proportionality theorem applies to the new $32$-bit lifts.

The retained physical parity and content assertions transfer to these lifts because they agree with the complete columns modulo $2^{32}$.

On a paired active block, put


$$
x=\widetilde X_j/2^9,\qquad
x'=\widetilde X_{j'}/2^9,\qquad
z=(x'-x)/2.
$$


The divisions are integral.

For the paired weights, choose the already proved locality precision $p=24$. Conservatively,


$$
\sigma'-\sigma\in2^{24}\mathbb Z_{(2)}
\quad\Longrightarrow\quad
\alpha'-\alpha\in2^{21}\mathbb Z_{(2)}.
$$


After the additional division by two in the paired Gram matrix, this is sufficient modulo $2^{20}$.

The octet row-proportionality error is at least $2^{35}$. Since the first coordinates are divisible by $2^9$, its contribution to a squared norm has depth at least


$$
35+9+1=45,
$$


above the physical norm comparison limit $42$. The quartet errors are deeper still.

Consequently A5’s decomposition strengthens to


$$
\boxed{
\frac{D_{\rm raw}}{2^{22}}
\equiv
\sum_{\mathcal A\text{-pairs}}\alpha\,Q(x,z)
+
\sum_{\mathcal B\text{-quartets}}\beta\,t^2
+
\sum_{j\in\mathcal C}c_j^2
\pmod{2^{20}},
}
\tag{10.1}
$$


where


$$
Q(x,z)=x^2+2xz+2z^2,
$$


and the row sets, weights, and amplitude divisions are the original ones.

The new contraction evaluates this whole normalized expression:


$$
\boxed{
\frac{D_{\rm raw}}{2^{22}}
\equiv583680=2^{11}\cdot285\pmod{2^{20}}.
}
\tag{10.2}
$$



Thus:

- four primitive norm bits are explained by the local grouping;
- the normalized cross-block sum has exact valuation $11$;
- together they give the exact primitive norm loss $4+11=15$.

This is a new precise interpretation of the accepted computation. It is not a structural proof of the eleven cross-block bits for an infinite family.

---

# IV. Priority 2: audit of A2 turn 7’s complete norm-only elimination

## 11. The enlarged three-digit radical is valid

Let


$$
V_j=(-1)^{j+1}\frac{W_jP_j}{p^3},\qquad
P_j=\binom{2n+b-1-j}{b-1-j},\qquad V_b=0,
$$


and $S=V\bmod p$.

The arbitrary multiplier claim requires more than knowing the total low contraction vanishes. It requires that changing the first three digits not change the interface entering the remaining contraction.

That interface can be checked directly.

The relevant first three digits are


$$
W:(2,7,24),\qquad
b-1:(26,28,5),\qquad
2n:(0,14,19).
$$


On the stated support:

- $d\in\{0,1,2\}$ causes no first-digit borrow or addition carry;
- for $e\le7$, the second digit contributes an addition carry but no weight borrow;
- for $e\ge14$, it contributes a weight borrow but no addition carry;
- $f\le5$ clears both possibilities, with no lower-index borrow.

Thus the outgoing three-digit interface is the same in both allowed $e$-branches. The first-three-digit contraction can indeed be replaced by an arbitrary scalar $K_H$, while the later factors remain unchanged.

Therefore, for every function $H(d,e,f)$,


$$
\sum_jS_j^2H(d,e,f)
=
K_H\cdot12\,
\bigl(10\mathscr T_{\rm I}+19\mathscr T_{\rm II}\bigr)
=0\pmod{29}.
$$


This uses the exact finite-range identity between the two high sums.

The corrected actual leading pair $21,-21$ is not replaced by $10,19$. The latter pair describes the common digit-five factorization used to prove the radical zero.

---

## 12. The full inverse expansion is retained before elimination

A2 correctly starts with


$$
\begin{aligned}
\mathcal RA^{-1}h^{[0]}
\equiv{}&
\mathcal R\mathsf R_{2n}w\\
&+p\,\mathcal R\mathsf R_n\mathsf D_1\mathsf R_nw
+p\,\mathcal R\mathsf R_{2n}z_1\\
&+p^2\,\mathcal R\mathsf R_n\mathsf D_2\mathsf R_nw\\
&+p^2\,\mathcal R\mathsf R_n\mathsf D_1\mathsf R_nz_1
+p^2\,\mathcal R\mathsf R_{2n}z_2
\pmod{p^5}.
\end{aligned}
\tag{12.1}
$$


In particular, the crossed term $\mathsf D_1z_1$ is present.

Terms of coefficient order at least three are discarded only using the established weighted $p^2$ safeguard. The normal-order and finite-return scopes are the accepted


$$
M=144,\qquad L=292.
$$



---

## 13. Second-lower and crossed-return divisibility

### 13.1 Complete $\mathsf D_2$

For $s\le58$, normal ordering produces


$$
\binom{-n}{t}\binom{2n+t+r-1}{r},
\qquad 0\le t\le s,\quad0\le r<29.
$$


Modulo $p$,

- $t\not\equiv0\pmod p$ supplies a coefficient factor $p$;
- when $t\equiv0\pmod p$, $r>0$ supplies a coefficient factor $p$.

Together with the weighted $p^2$ safeguard, those terms have depth at least three.

For the exceptional cases


$$
t=0,29,58,\qquad r=0,
$$


the row factors must be kept. If the two low weight digits do not borrow, then


$$
J=j\bmod p^2\le205.
$$


A nonzero unshifted row factor forces $a\le J$, so the low lower index is


$$
838+a-J\in[633,838].
$$


The upper addend $406+t$ forces a low carry. The shifted row factor gives the corresponding interval


$$
839+a-J\in[634,838].
$$


The retained digits $3,4,5$ give two further events for every incoming interface.

Thus the coefficient-weighted second-lower terms are in $p^3$, and


$$
p^2\mathcal R\mathsf R_n\mathsf D_2\mathsf R_nw
\equiv0\pmod{p^5}.
$$



This uses the complete compatible support through $58$.

### 13.2 $\mathsf D_1z_1$

The first return is supported at $b,b+1$. The same coefficient separation applies, now with exterior offsets $0,1$.

In the exceptional shifted offset-$2$ case, loss of the extra low event can occur only at $j_0=0$, where the reconstruction factor $j$ supplies $p$.

Hence


$$
p^2\mathcal R\mathsf R_n\mathsf D_1\mathsf R_nz_1
\equiv0\pmod{p^5}.
$$



These are pointwise output-precision eliminations, not merely norm cancellations.

---

## 14. The second endpoint charges

The crossed lower inverse is


$$
H=I-p\mathsf D_1+p^2(\mathsf D_1^2-\mathsf D_2)\pmod{p^3}.
$$


Its second-order support ends at $58$.

For $2\le r\le28$,


$$
b+r=p^2A+(r-2),\qquad A\equiv6\pmod p.
$$



If $r<s<29$, $\binom{b+r}{s}$ has two low borrows and therefore depth at least two. For $s=29$,


$$
\frac1p\binom{b+r}{29}\equiv6\pmod p.
$$


A direct Vandermonde proof is available: every term involving
$\binom{p^2A}{p-k}$, $1\le k\le r-2$, is divisible by $p^2$, while


$$
\binom{p^2A}{p}\equiv pA\pmod{p^2}.
$$



All second-order coefficients with $s>r$, $s\le58$, are killed by the corresponding Lucas zero. The same check covers $29\le r\le57$; beyond that the crossed bandwidth is exhausted.

The surviving first coefficient is $7p$, so


$$
q_{2,r}=7\cdot6\,y_{0,b+r-29}
=13\,y_{0,b+r-29}\pmod p.
$$



The finite short-head contact identity gives


$$
y_{0,b+r-29}=(-1)^rF_{r-2},\qquad
F_0=1,\quad F_d=1-dF_{d-1}.
$$


Equivalently,


$$
F_d=\sum_{t=0}^d(-1)^t d_{\underline t}.
$$



The exterior map does not change these rows at this order: off-diagonal shifts within this range have positive length below $p$, and their $n$-binomial factor vanishes modulo $p$; upper triangularity prevents the lower exterior rows from feeding higher ones.

Therefore


$$
\boxed{
z_{2,r}=13(-1)^rF_{r-2}\quad(2\le r\le28),
\qquad z_{2,r}=0\quad(r\ge29).
}
$$


In particular,


$$
z_{2,2}=13,\qquad z_{2,3}=0,\qquad z_{2,4}=13.
$$



The charges at $r=0,1$ are not asserted zero. Their reconstructed atoms already have depth three, so their coefficient $p^2$ makes them irrelevant modulo $p^5$.

---

## 15. The second-return contraction and its denominators

The potentially dangerous denominator occurs when a rising product near $b-j$ reaches


$$
b+d+2-j.
$$


On the leading support,


$$
b+d+2-j
=
p^2(6-f+\text{a multiple of }p)
$$


when $e=0$. Its normalized unit is $6-f$, which is nonzero because $0\le f\le5$.

For the unshifted atom:

- $r<d+2$ does not reach this denominator;
- $r=d+2$ reaches it without yet reaching the matching numerator multiple of $p$;
- $r>d+2$ includes that numerator multiple and regains the additional factor.

Thus only $r=d+2$ can contribute to $E_r/p^2$. The shifted reconstruction similarly leaves only $r=d+1$, with its factor $d$.

After cancellation of the common unit products,


$$
\frac{G_j}{S_j}
=
\frac{14}{6-f}
\left(
(-1)^{d+1}z_{2,d+2}
+(-1)^d d\,z_{2,d+1}
\right).
$$


For $d=0,1,2$, the bracket is $-13$, giving


$$
\boxed{
G_j=S_j\,\frac{21}{6-f}\,\mathbf1_{e=0}\pmod p.
}
$$


The enlarged radical now proves


$$
\boxed{S^TG=0\pmod p.}
$$



This is an evaluated symbolic zero for the complete second return, not an assumption that the return vanishes as a column.

---

## 16. First-return and first-lower contractions

### 16.1 First return

For $r=0,1$, the atom ratio contains


$$
2n\,
\frac{(2n+b-j)^{\overline r}}
     {(b-j)^{\overline{r+1}}}.
$$


The denominators are units on the leading support except for the shifted $r=1$ possibility involving $b+2-j$.

When $d=0$:

- if $e\ne0$, both $b+2-j$ and $j$ have valuation one;
- if $e=0$, $b+2-j$ has valuation two and $j$ has valuation at least two.

The reconstruction factor $j$ pays that denominator. The remaining $2n$ supplies a factor $p$. Therefore the first-return correction is zero pointwise on the leading support after division by $p^3$, and its norm pairing vanishes.

### 16.2 First lower: explicit denominator audit and a clarification

For the displayed atom ratio


$$
\frac{(N_j+1)^{\overline{s+\varepsilon}}}
     {(2n+1)^{\overline{t+r}}}
\frac{K_j!}{(K_j+a-r+\varepsilon)!},
$$


the possible denominator losses are controlled as follows.

1. Since $t+r\le57$, the only possible multiple of $p$ in
   $(2n+1)^{\overline{t+r}}$ is $2n+29$, of valuation one.

2. A denominator near $b-j$ has valuation at most two. Its possible second unit is $6-f$.

3. The two losses cannot occur together. If $t+r\ge29$, then
   

$$
a-r+\varepsilon=s-t-r+\varepsilon\le1,
$$


   where the near-$b-j$ denominator is a unit or absent.

4. The exceptional row factorial at $a=29,t=0$ must be paid explicitly.

For the fourth point, the source’s wording should not be read as claiming


$$
v_p\binom j{29}\ge2
\quad\text{whenever }e=0.
$$


That is generally false: for $f\ne0$, its valuation is typically one.

The correct statement is that the falling numerator contains a factor of valuation at least two, and division by $29!$ consumes one. Indeed, when $e=0$,


$$
\frac1p\binom j{29}\equiv f\pmod p.
$$


That remaining factor is exactly what is needed: the associated rising numerator has first normalized unit $14$, whereas the near-$b-j$ denominator can cost two factors.

This clarification preserves the conclusion. After all cancellations, only $j\bmod p^3$ is needed; if an exceptional row factor is deeper, the contribution is zero at the required layer.

Thus


$$
\frac{L_{1,j}}{p^3}=S_jH_1(d,e,f)\pmod p
$$


for a genuine low-three-digit function, and the radical proves


$$
S^T(L_1/p^3)=0\pmod p.
$$



**Verdict:** accept the first-lower elimination with the factorial-payment clarification above.

---

## 17. Baseline factorization and terminal support

For


$$
U=p^{-3}\mathcal R\mathsf R_{2n}w,
$$


the exact finite-head identity yields, on the leading support,


$$
U_j=V_j(1+pH_0(d,e))\pmod{p^2}.
$$


The denominators $2n+r$, $1\le r<29$, and $b-j$ are units there.

Off the leading support, both $U_j,V_j$ are divisible by $p$. Hence


$$
U^TU-V^TV
=
2p\sum_jS_j^2H_0(d,e)
=0\pmod{p^2}.
$$



The terminal coordinate remains


$$
\frac{Z_{w,b}}{p^3}
\equiv14pA_0\frac{W_b}{p^4}\pmod{p^2}.
$$


Its square vanishes modulo $p^2$, which explains its absence from this norm residue. It remains in the actual column and in other pairings.

Combining all terms in (12.1) gives the accepted complete reduction


$$
\boxed{
\eta=A_0^2\kappa(b,n).
}
$$


No division by $A_0$ has been made; no unit hypothesis on $A_0$ is silently introduced.

The value of $\kappa$ is still open.

---

# V. The potential receipt and the infinite content theorem

## 18. What the new $696$-inequality receipt proves

There are


$$
2^3\cdot29=232
$$


choices of incoming flags and digit at each of the three positions. Thus the receipt’s


$$
232+232+232=696
$$


checks have the stated complete finite scope.

The potential inequalities telescope because the outgoing lower borrow at the middle position is the incoming lower borrow at the last. They prove at least two valuation events per prescribed block for every incoming interface.

The offset counts are also correct:

- $-1,\ldots,2001$: $2003$ values;
- $-1,\ldots,4002$: $4004$ values;
- lower offsets: three values.

This is useful corroboration of the analytic potential proof.

It is **not** a substitute for the complete solved-charge integrality theorem. That theorem separately follows from


$$
K_\times\in pM(\mathbb Z_p),
\qquad
(I+K_\times\mathsf DF)^{-1}
\equiv
\sum_{\ell=0}^{K-1}(-K_\times\mathsf DF)^\ell
\pmod{p^K},
$$


together with the retained integral finite normal ordering and exterior support bounds.

Both ingredients are required to transfer block valuations to the complete reconstructed column.

---

## 19. New consequence: dense zeros of the complete next-norm residue

Define the actual next-norm residue on the original family by


$$
\eta(u)=\frac{Z_w(u)^TZ_w(u)}{p^7}\pmod p.
$$


The retained leading-norm theorem makes this integral.

The complete-column content theorem supplies infinitely many indices in every original progression with $c\ge2$. At such an index,


$$
v_p(Z_w^TZ_w)\ge2c+4\ge8,
$$


and therefore


$$
\eta(u)=0.
$$



Hence:

### Theorem 19.1
For every original progression $u\equiv u_0\pmod h$, there are infinitely many indices in that progression for which


$$
\boxed{\eta(u)=A_0(u)^2\kappa(b(u),n(u))=0.}
$$



This is unconditional within the retained complete-column theorems.

A sharper consequence concerns possible finite-prefix descriptions.

### Corollary 19.2
If $\eta(u_*)\ne0$ at an original index $u_*$, then $\eta$ is not constant on any congruence neighborhood of $u_*$ in the original index set.

Indeed, every such neighborhood contains infinitely many zeros by Theorem 19.1.

Thus a proof that $\eta$ is congruence-locally constant at every original index—even with a radius depending on the index—would force


$$
\eta\equiv0.
$$



This is stronger than requiring one uniform fixed prefix for all indices. It does not supply the needed local constancy. Prime-power finite-state background alone does not prove it for a finite sum whose cutoff grows with the original index.

Nor can one conclude dense zeros of $\kappa$ itself without controlling $A_0$: the factor $A_0^2$ must remain.

---

# VI. A concrete whole-carry lemma and a bounded auxiliary calculation

## 20. Exact extraction of the outstanding carry

The following lemma isolates precisely what must be computed.

### Lemma 20.1 — Whole leading-square carry

Let


$$
a_j=\binom{n+2}{j}
\binom{2n+b-1-j}{b-1-j},
\qquad 0\le j<b.
$$


Assume the retained phase theorem $v_p(a_j)\ge3$. Put


$$
\mathcal J_3=\{j:0\le j<b,\ v_p(a_j)=3\},
\qquad
u_j=a_j/p^3\quad(j\in\mathcal J_3).
$$


Then


$$
\boxed{
\kappa(b,n)=
\frac1p\left(\sum_{j\in\mathcal J_3}u_j^2\pmod{p^2}\right)
\pmod p,
}
\tag{20.1}
$$


where the parenthesized whole residue is divisible by $p$.

#### Proof

If $v_p(a_j)\ge4$, then $a_j^2\equiv0\pmod{p^8}$. If $v_p(a_j)=3$, then


$$
a_j^2=p^6u_j^2.
$$


Therefore


$$
\sum_{j=0}^{b-1}a_j^2
\equiv
p^6\sum_{j\in\mathcal J_3}u_j^2
\pmod{p^8}.
$$


The established leading cancellation says the right-hand unit sum is divisible by $p$. Dividing the whole expression by $p^7$ gives (20.1). ∎

This makes the obstruction explicit: the leading modulo-$p$ cancellation does not determine the carry of the unit-square sum modulo $p^2$.

An exact recurrence, if useful for a bounded control, is


$$
\frac{a_{j+1}}{a_j}
=
\frac{(n+2-j)(b-1-j)}
     {(j+1)(2n+b-1-j)},
\qquad 0\le j\le b-2.
$$


Valuations are updated separately; only the stripped units are inverted. The recurrence stops at the actual finite endpoint.

---

## 21. A genuinely bounded sparse auxiliary control

No binary rerun is needed. The remaining new arithmetic is the $29$-adic whole carry.

If the coordinator proceeds with an auxiliary high-word control, the following is a concrete bounded option.

Define the fixed low phase


$$
b_0=
3^{249005515}\bmod29^6,
\qquad 0\le b_0<29^6.
$$


For example, choose auxiliary inputs


$$
b^{(C)}=b_0+29^6C,\qquad
n^{(C)}=2001b^{(C)},\qquad C=0,1.
$$


These are auxiliary integers with the required low phase. They are **not claimed to be original powers**.

The low candidate support has


$$
3\cdot23\cdot6\cdot22\cdot1\cdot21
=\boxed{191268}
$$


possible six-digit words. For each auxiliary input, enumerate only those candidates and the bounded high continuations, then enforce


$$
\boxed{0\le j<b^{(C)}}
$$


explicitly. Compute the complete atom valuation and retain only valuation-three atoms.

For $C=0,1$, the total candidate count before cutoff and valuation pruning is at most


$$
191268(1+2)=\boxed{573804}.
$$



### Exact unit arithmetic

At precision $p^2=841$, define


$$
\Phi_p(M)=p^{-v_p(M!)}M!\pmod{p^2}.
$$


It can be evaluated by the exact identity


$$
\Phi_p(M)=
\prod_{s\ge0}
\prod_{\substack{1\le k\le\lfloor M/p^s\rfloor\\p\nmid k}}k
\pmod{p^2}.
$$


The inner products use a fixed prefix table modulo $841$; complete unit blocks have product $-1$. All factorial-ratio inversions are of $29$-adic units.

### Required verifiable output

For each chosen auxiliary $C$:

1. the exact auxiliary $b,n$ and enforced cutoff;
2. candidate and valuation-three counts;
3. the unit-square sum
   

$$
U_C=\sum_{j\in\mathcal J_3}u_j^2\pmod{841};
$$


4. the check $29\mid U_C$;
5. the evaluated residue
   

$$
\kappa_C=U_C/29\pmod{29};
$$


6. agreement with the whole numerator residue
   

$$
\sum_{j=0}^{b-1}a_j^2
   \equiv29^6U_C\pmod{29^8}.
$$



No numerical value of $\kappa_C$ is asserted here. This is an unevaluated specification.

Even a successful auxiliary computation would establish only those auxiliary values. It would not evaluate an original power, prove all-continuation vanishing, or settle the primitive denominator.

---

# VII. Why the local results do not yet control the actual denominator

## 22. Content growth is not denominator improvement

The obstruction can be stated exactly without changing any row contents in the actual construction.

Suppose, for explanatory purposes, an integral weighted pair is written


$$
N_1=s_1U,\qquad N_2=s_2V.
$$


With the same retained metric,


$$
A=s_1^2a,\qquad H=s_1s_2h,
$$


where


$$
a=U^T\Omega U,\qquad h=U^T\Omega V.
$$


Then


$$
\boxed{
q=\frac{s_1a}{\gcd(s_1a,\,s_2h)}.
}
\tag{22.1}
$$



Thus increasing first-column content can:

- cancel completely if the second column scales compatibly;
- remain in the primitive denominator if the mixed pairing does not scale compatibly.

For example, in an abstract one-coordinate integral model, scaling both columns by $p^K$ leaves the primitive quotient unchanged, whereas scaling only the first can produce denominator $p^K$.

These are not counterexamples to the actual source family. They prove that content growth alone cannot imply the missing denominator bound.

The binary residues now determine exact selected-prime depths for the raw pair. They do not determine its odd-prime gcd, and they do not identify that raw pair with every row-normalized final pair without the corresponding exact normalization identities.

---

## 23. The actual all-prime normalization remains unchanged

Retain


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
}
$$


The gcd is over all primes. The least actual two-column clearer $d_B$ and primitive multiplier


$$
d_B^2/g_B
$$


remain part of the construction.

Equivalently,


$$
\log q_n
=
\sum_\ell
\max\{v_\ell(A_B)-v_\ell(H_B),0\}\log\ell.
$$


The new binary calculation evaluates one local contribution for its specified raw normalization. It supplies no bound for the entire sum above.

For A2, the complete mixed-force identity remains


$$
p^3U_a^TQ
=
p^3(r_0G^{(3)}_{a0}+r_1G^{(3)}_{a1})
+\sum_{\ell=1}^{b-2}\mathcal H_\ell\lambda'_{a,\ell}
+W_bU_{a,b}.
$$


There is still no source row at $b-1$, and the terminal exterior is not an additional recurrence step.

The unresolved relative alignment remains


$$
x^TQ-p^c\rho_nx^Tx
\equiv0\pmod{p^{c+\nu+1}},
\qquad
N_{\log}\ge c+4+\nu.
$$


The norm-only eliminations do not prove this mixed-force statement.

---

## 24. The whole same-index error is still the decisive quantity

For the weighted construction,


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
$$


The actual $q_n$ and the complete $\epsilon_n$ must be evaluated or bounded at the same original index.

The retained determinant and weighted-endpoint versions likewise keep their full normalizations:


$$
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{g_\ell}
\det H_{\rm complete},
$$


and


$$
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda e_3\alpha_{n,2}(\lambda-\Lambda_{n,2}).
$$



No local modular omission removes a term from these real identities.

A concrete sufficient global lemma would establish, on an infinite sequence of original indices,


$$
0<|q_n\epsilon_n|\longrightarrow0
$$


using the actual all-prime $q_n$. The strict nonzero condition matters: under a rationality hypothesis, a nonzero integer-denominator linear form cannot tend to zero.

None of the present sources proves this lemma.

---

# VIII. Proof-status ledger and conclusion

| Claim | Status after this audit |
|---|---|
| Complete physical $32$-bit first head and exterior load | Accepted finite execution under retained tail proofs |
| Both force-dependent finite Schur loads | Accepted in the new numerator construction |
| $1064$ source and $1064$ reconstruction checks | Audited finite execution |
| Terminal $-b\,g_0-1$ | Explicitly retained and checked |
| Both $n$-branches zero modulo $2^{32}$ | Accepted coefficientwise finite result |
| Contact $z^{284}$ | Accepted coefficientwise finite result |
| Modular maximal factors $134,135$ | Accepted, with nonzero failed remainders |
| Orders $63,62$, fixed divisors $57,52$, losses $12,16$ | Independently derived |
| Physical norm/mixed precision $42/41$ | Proved from content and $32$-bit comparison |
| $v_2(D_{\rm raw})=33,\ v_2(E_{\rm raw})=34$ | Exact finite-word result |
| Primitive binary norm loss $15$ | Rigorous deduction |
| $E_{\rm raw}/(2D_{\rm raw})=49\bmod128$ | Guarded exact local result |
| Norm-relative logarithmic guard at seven bits | Closed at this original word |
| Sixteen-row residual modulo $2^{20}$ | New deduction from the higher physical lift |
| Normalized cross-block valuation $11$ | Exact finite-word deduction |
| Arbitrary low-three-digit $29$-adic radical | Proved using the common outgoing interface |
| Complete $\mathsf D_2$ and $\mathsf D_1z_1$ eliminations | Accepted after audit |
| $z_{2,r}=13(-1)^rF_{r-2}$ and terminal support | Accepted after audit |
| Complete second-return contraction | Proved zero |
| First-lower contraction | Accepted with explicit factorial-payment clarification |
| $\eta=A_0^2\kappa$ | Accepted complete norm-only reduction |
| Value of $\kappa$ | Unevaluated |
| $696$-inequality potential receipt | Accepted finite corroboration |
| Complete arbitrary-precision endpoint integrality | Separate retained proof, not supplied by that receipt |
| Infinite content theorem on every original progression | Retained complete-column theorem |
| Infinitely many zeros of $\eta$ in every progression | New unconditional consequence |
| All-prime primitive denominator versus whole error | Open |
| Irrationality or rationality of $e+\pi$ | Unresolved |

## Final assessment

The former original-$u_0$ binary norm upper-bound obligation is now closed:


$$
\boxed{
c_2(X)=9,\quad
v_2(D_{\rm raw})=33,\quad
v_2(E_{\rm raw})=34,\quad
\nu_2=15.
}
$$


The complete physical pipeline—not merely a formal short numerator—supports those conclusions.

A2’s new report also advances beyond its earlier unevaluated second-return specification. After the explicit denominator clarification, its complete norm reduction is valid:


$$
\boxed{
\eta=A_0^2\,
\frac1{29^7}
\sum_{j=0}^{b-1}
\binom{n+2}{j}^{2}
\binom{2n+b-1-j}{b-1-j}^{2}
\pmod{29}.
}
$$


The remaining local computation is exactly the carry of that whole finite leading-square sum modulo $29^8$. No head, $\mathsf D_2$, or second-return charge remains as an unresolved input to this particular norm.

The exact global bottleneck is unchanged:


$$
\boxed{
\text{control of the actual all-prime primitive denominator against the
whole nonzero same-index error on an infinite original sequence}.
}
$$



The new exact binary valuation, the strengthened finite Gram interpretation, the complete $29$-adic norm-only reduction, and the dense-zero consequence are genuine progress. They do not yet provide an unconditional proof or disproof of the irrationality of $e+\pi$.
