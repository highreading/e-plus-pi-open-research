> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4, Turn 8 — Audit of the original binary Gram computation, exact saturation, and the next $29$-adic column

## Executive conclusions

The two new binary computations survive the mathematical audit at their stated scope, but the $29$-adic report contains an arithmetic error in its new low Gram coefficient.

1. **The $512$-bit saturation certificate has a valid exact lift.**  
   The degree-$3,\ldots,162$ triangular minor proves that the reported modular annihilators lift to exact integral annihilators modulo $2^{351}$. The reported unit pairing with three integral quotient representatives then gives an exact saturated coordinate system. I give the complete argument below; finite annihilation alone would not suffice.

   Consequently, for the specified integer lifts of the retained short numerators, the reported free contents
   

$$
157,\qquad154
$$


   are exact, and the claimed sufficient observable precisions
   

$$
\boxed{23,\qquad23}
$$


   are justified. These are statements about the exact lifted payloads, not about unprovided higher physical digits.

2. **The original twenty-bit binary Gram evaluation is correctly normalized and finitely terminated.**  
   The source implements the proved factorial-ratio transport, uses the correct integer-valued payloads, divides only after the exact normalization identities justify division, and accepts precisely the original range $0\le j\le b$. The physical endpoint is not lost. Its contribution, including the exterior correction in the second column, is already in the accepted $A_e$.

   Thus the supplied execution receipt supports
   

$$
\boxed{D_{\rm raw}\equiv E_{\rm raw}\equiv0\pmod{2^{20}}.}
$$


   These are lower bounds on valuations, not exact depths. No ratio precision or norm-relative logarithmic omission follows merely from these zeros.

3. **There is a small, rigorous precision dividend from the already-proved evenness of both columns.**  
   Twenty-bit physical column data determine the norm modulo $2^{22}$, and the mixed contraction modulo $2^{21}$. This is a quadratic stability theorem, not an assumption that an arbitrary integer lift supplies new physical data.

   Therefore the first warranted extension is a **new $37$-kernel-bit contraction**, using the existing physical data, to obtain
   

$$
\boxed{D_{\rm raw}\pmod{2^{22}},\qquad E_{\rm raw}\pmod{2^{21}}.}
$$


   No twenty-bit producer needs to be rerun. Beyond that guaranteed range, genuinely new physical information is needed unless stronger content or sensitivity bounds are proved.

4. **A2turn5’s low coefficient $K_{34}=27$ is incorrect.**  
   Its own displayed finite sum gives
   

$$
\sum_{a=0}^{7}\bigl((a+1)\cdots(a+7)\bigr)^2
   \equiv9\pmod{29},
$$


   not $13$. Consequently,
   

$$
\boxed{K_{34}=12,\qquad
   L_{\mathrm I}^{(3)}=21,\qquad
   L_{\mathrm{II}}^{(3)}=8=-21\pmod{29}.}
$$


   I independently recover the factorization producing these coefficients, so this is not merely a discrepancy with an unevaluated formula.

   The important norm conclusion nevertheless survives: the two high sums are equal on the **original finite range**, so the corrected coefficients still give
   

$$
\boxed{d\ge7.}
$$



5. **The $C\equiv814\pmod{841}$ obstruction extends to eleven original residue classes.**  
   More precisely,
   

$$
\boxed{
   C\equiv2+29\gamma\pmod{841},\quad18\le\gamma\le28
   \ \Longrightarrow\ c\ge2,\quad d\ge8.
   }
$$


   Each of these eleven $C$-classes corresponds to one residue class of the original orbit parameter $u\bmod841$. This is a new, rigorous content/norm consequence. It is not an exact content classification.

I did not execute either program or recompute either hashed artifact. The execution results below are attributed to the supplied receipts; the exact-lifting, normalization, precision, and $29$-adic arguments are mathematical audits of the supplied sources.

---

# Part I. Exact saturation of the original binary relation matrix

## 1. The matrix being certified is the correct one

For this part,


$$
b=150094635296999121,\qquad
n=600678730458590482242=4002b,
$$


and


$$
N=n+2,\qquad a=2n.
$$



The actual scalar functional is


$$
\mathscr L(P)=
\sum_{j=0}^{b}
\binom Nj^2
\binom{a+b-j-1}{b-j}^{2}P(j).
$$



Set


$$
\mathcal A(j)=(N-j)^2(b-j)^2,\qquad
\mathcal B(j)=j^2(a+b-j)^2,
$$


and


$$
\Delta R(j)=\mathcal A(j)R(j+1)-\mathcal B(j)R(j).
$$



The exact finite telescoping identity gives


$$
\mathscr L(\Delta R)=0.
$$


At the lower endpoint, $\mathcal B(0)=0$; at the upper endpoint,


$$
\mathcal A(b)=(N-b)^2(b-b)^2=0.
$$



The coordinator’s matrix $L$ therefore correctly has:

- rows corresponding to degrees $0,\ldots,162$;
- columns $\Delta j^k$, $0\le k\le159$;
- shape $163\times160$.

This is the actual zero-flux presentation, rather than the older presentation with an additional formal boundary generator. The difference between the reported binary rank $80$ here and rank $81$ in that older formal presentation is not a contradiction.

For every $k$,


$$
\deg\Delta j^k=k+3,\qquad
[j^{k+3}]\Delta j^k=k+2n-4.
$$


Thus the submatrix $T$ on rows $3,\ldots,162$ is triangular, and


$$
\det T=\prod_{k=0}^{159}(k+2n-4)\ne0.
$$


The reported exact valuation is


$$
v_2(\det T)=161.
$$



In particular, the rational column rank really is $160$, and the rational left-kernel dimension is three.

---

## 2. Why the modular Smith exponents are exact

The source verifies, modulo $2^{512}$,


$$
ULV=
\begin{pmatrix}
\operatorname{diag}(2^{e_1},\ldots,2^{e_{160}})\\
0
\end{pmatrix},
$$


with $U,V$ invertible modulo $2^{512}$. It also verifies $UU^{-1}=I$.

The receipt reports


$$
\#\{i:e_i=0\}=80,\qquad
\#\{i:e_i>0\}=80,
$$




$$
\sum_i e_i=157,\qquad
\max_i e_i=8.
$$



These exponents are not merely truncated guesses. To see this, lift $U,V$ to matrices invertible over $\mathbb Z_2$. Then the exact transformed matrix has the form


$$
\begin{pmatrix}D\\0\end{pmatrix}+2^{512}R,
\qquad
D=\operatorname{diag}(2^{e_i}).
$$


Its upper square block is


$$
D\left(I+2^{512}D^{-1}R_{\rm top}\right).
$$


Because $\max e_i=8$, the parenthesized matrix lies in


$$
I+2^{504}M_{160}(\mathbb Z_2)
$$


and is invertible. The lower block can then be removed by integral row operations. Hence the exact matrix has precisely the reported $2$-primary invariant exponents.

The triangular-minor valuation $161$ and Smith total $157$ have different roles. There is no requirement that they agree.

---

## 3. Exact lifting of the three annihilators

This is the essential saturation argument.

Let $C_0$ be the $3\times163$ matrix formed from the last three rows of the reported $U$, using any integer representatives of their residues. The modular check says


$$
C_0L\in2^{512}M_{3\times160}(\mathbb Z).
$$



Let $I=\{3,\ldots,162\}$, so $L_I=T$. Define a correction supported on these coordinates by


$$
(\delta C)_I=-C_0LT^{-1},\qquad
(\delta C)_{\{0,1,2\}}=0.
$$


Then


$$
(C_0+\delta C)L
=C_0L-C_0LT^{-1}T=0
$$


**exactly**.

Since $T$ is integral and $v_2(\det T)=161$,


$$
T^{-1}\in2^{-161}M_{160}(\mathbb Z_2).
$$


Therefore


$$
\delta C\in2^{512-161}M_{3\times163}(\mathbb Z_2)
=2^{351}M_{3\times163}(\mathbb Z_2).
$$



Put


$$
\widehat C=C_0+\delta C.
$$


We have proved


$$
\boxed{
\widehat CL=0,\qquad
\widehat C\equiv C_0\pmod{2^{351}},
\qquad
\widehat C\in M_{3\times163}(\mathbb Z_{(2)}).
}
$$



The rational inverse used in the correction is legitimate: its possible power-of-two denominator is paid for by the $512$-bit residual, and all remaining denominators are odd.

### The unit pairing completes the saturation proof

Let $B_0$ be the $163\times3$ matrix of the three reported quotient representatives, again lifted to integer entries. The source verifies


$$
C_0B_0\equiv I_3\pmod{2^{512}}.
$$


Consequently


$$
M:=\widehat CB_0\equiv I_3\pmod{2^{351}}
$$


is invertible over $\mathbb Z_{(2)}$. Define


$$
C=M^{-1}\widehat C.
$$


Then


$$
\boxed{
CL=0,\qquad CB_0=I_3,\qquad
C\equiv C_0\pmod{2^{351}}.
}
\tag{3.1}
$$



Now let


$$
S=\operatorname{span}_{\mathbb Q}(L)\cap\mathbb Z_{(2)}^{163}
$$


be the saturated relation module. Since $C$ is surjective, its kernel is a saturated rank-$160$ submodule. It contains all columns of $L$, whose rational span also has dimension $160$. Therefore


$$
\ker C=S.
$$


Thus


$$
\mathbb Z_{(2)}^{163}/S\simeq\mathbb Z_{(2)}^3,
$$


and the columns of $B_0$ give an exact quotient basis.

This proves the claimed exact saturation. It does not rely on the invalid implication


$$
2^s x\equiv0\pmod{2^M}\Longrightarrow x\equiv0\pmod{2^M}.
$$



---

## 4. The reported payload contents and the $23$-bit conclusion

Let $p_f,p_m\in\mathbb Z^{163}$ be the coefficient vectors of the exact polynomials formed from the specified integer lifts:


$$
U_f^2,\qquad U_fU_e.
$$


The mixed polynomial is correctly padded from degree $158$ to the common degree-$162$ presentation.

Its exact saturated coordinates are


$$
c_f=Cp_f,\qquad c_m=Cp_m.
$$


By (3.1), the reported coordinate arrays are correct modulo $2^{351}$.

Since the reported minimum valuations are


$$
s_f=157<351,\qquad s_m=154<351,
$$


these minima are exact:


$$
\boxed{
\operatorname{cont}_2(c_f)=157,\qquad
\operatorname{cont}_2(c_m)=154.
}
$$



Moreover, evaluation kills the saturated relation module. Indeed, it kills $L$ exactly, and its target is torsion-free. Hence, writing $S_i$ for the three integral polynomials represented by $B_0$,


$$
\mathscr L(U_f^2)=\sum_{i=1}^3c_{f,i}\mathscr L(S_i),
$$




$$
\mathscr L(U_fU_e)=\sum_{i=1}^3c_{m,i}\mathscr L(S_i).
$$



The original denominator valuations are


$$
v_2(D_f^2)=160,\qquad v_2(D_fD_e)=157.
$$


Thus twenty output bits require the numerator sums modulo $2^{180}$ and $2^{177}$. After extracting the exact coordinate contents, sufficient observable precisions are


$$
180-157=23,\qquad177-154=23.
$$



Therefore the coordinator’s conclusion is correct:


$$
\boxed{K_f=K_m=23.}
$$



### Scope restriction

These are exact contents of the payloads obtained from the **specified integer lifts of twenty-bit short coefficients**. They are not automatically the contents of an unknown higher-precision physical numerator. Changing those lifts can change their exact saturated contents while leaving the twenty-bit physical contractions unchanged.

That distinction does not invalidate the computation. It specifies what the computation actually proves.

---

# Part II. Audit of the original binary Gram transport

## 5. Scale, signs, and the force basis

The accepted reconstructed series are


$$
F(z)=\frac{A_f(z)}{(1-z)^{a+81}},\qquad
E(z)=\frac{A_e(z)}{(1-z)^{a+77}}
\pmod{2^{20}},
$$


with $a=2n$.

The source uses


$$
U_\alpha(j)=
\sum_{r=0}^{R_\alpha}
A_{\alpha,r}(b-j)_{\underline r}
(a+b-j)^{\overline{R_\alpha-r}},
$$


where


$$
R_f=81,\qquad R_e=77,
$$


and


$$
D_\alpha=(a)^{\overline{R_\alpha}}.
$$



The exact coefficient identity is


$$
F_{b-j}=\frac{U_f(j)}{D_f}
\binom{a+b-j-1}{b-j},
$$


and similarly for $E$. This confirms both the shift and the denominator.

The two Gram products use the same signed reversal, so the signs cancel in both the square and the mixed product. The program therefore correctly evaluates


$$
\widetilde D=
\frac{\mathscr L(U_f^2)}{D_f^2},
\qquad
\widetilde E=
\frac{\mathscr L(U_fU_e)}{D_fD_e}.
$$



At the retained physical precision,


$$
\widetilde D\equiv D_{\rm raw},\qquad
\widetilde E\equiv E_{\rm raw}\pmod{2^{20}}.
$$



No further exterior $+1$ is to be added: the accepted second numerator $A_e$ already contains it, along with its certified finite return and other retained second-force terms. Conversely, the contraction program does not independently prove that provenance; it uses the previously certified complete $A_e$.

---

## 6. Integer-valued normalization and final division

The established fixed-divisor identities give


$$
P_f=U_f/2^{73}\in\operatorname{Int}_{\le81}(\mathbb Z),
\qquad
P_e=U_e/2^{68}\in\operatorname{Int}_{\le77}(\mathbb Z).
$$


Also


$$
D_f=2^{80}d_f,\qquad D_e=2^{77}d_e,
$$


with $d_f,d_e$ odd.

Consequently


$$
S_{ff}:=\mathscr L(P_f^2)
=2^{14}d_f^2\widetilde D,
$$




$$
S_{fe}:=\mathscr L(P_fP_e)
=2^{16}d_fd_e\widetilde E.
\tag{6.1}
$$



The source’s payload construction is sound:

- evaluating $U_f$ modulo $2^{36+73}$ and dividing its values by $2^{73}$ determines $P_f$ modulo $2^{36}$;
- the analogous exponent for $P_e$ is $36+68$;
- the retained $341$-bit arrays provide more than enough information;
- finite differences reconstruct the integer-valued polynomials without modular inversion of factorials.

The final shifts by $14$ and $16$ implement the exact divisions in (6.1). The remaining inversions are of odd units. There is no hidden even inverse.

Using a shared $36$-bit transport and then retaining


$$
S_{ff}\pmod{2^{34}},\qquad
S_{fe}\pmod{2^{36}}
$$


is sufficient for the stated twenty-bit outputs.

---

## 7. The factorial-ratio transition is implemented correctly

The weight is


$$
T(j)=
\left(
\frac{N!\,(S-j)!}
{c!\,j!\,(N-j)!\,(b-j)!}
\right)^2,
\qquad
c=2n-1,\quad S=c+b.
$$



The program’s three flags are exactly the borrows in


$$
N-j,\qquad b-j,\qquad S-j.
$$


For a next bit $\epsilon$, it computes


$$
\lambda_C'=\mathbf1_{\epsilon+\lambda_C>\nu_C},
$$


and the associated residual digit


$$
\eta_C=\nu_C-\lambda_C-\epsilon+2\lambda_C'.
$$



The power of two is


$$
d_t=\kappa_{t+1}+\lambda_N'+\lambda_b'-\lambda_S',
$$


and the code checks $d_t\in\{0,1,2\}$. Its odd-factorial correction is precisely the squared ratio obtained from


$$
(2h+\epsilon)!=2^h h!\,g(h+\epsilon).
$$



The implementation also correctly handles the polynomial operations:

- `consecutive_values` updates a forward-difference table in the proper order;
- `newton_at` performs exact integer divisions when forming generalized binomial coefficients;
- negative arguments occur only in the odd-unit extension and are handled by the proved recurrence;
- the number of interpolation values is sufficient for the unreduced product degree;
- the degree and valuation-layer tests are applied before the resulting polynomial is retained.

The proof of closure is A5’s direct integer-valued-polynomial argument. The finite checks in the program corroborate that implementation; they are not being extrapolated into a general transport theorem.

---

## 8. The nonlinear finite-end condition is retained

At a fixed digit depth, the three borrow flags are threshold functions of one common lower prefix. Hence there are at most four reachable states. The source computes exactly those possible threshold patterns.

The terminal condition is not an arbitrary convention. After all $71$ digits:

- $h=0$;
- the terminal $b$-borrow is zero exactly when $j\le b$;
- because $b<N,S$, every such $j$ also has zero terminal $N$- and $S$-borrow.

Thus accepting only


$$
(\lambda_N,\lambda_b,\lambda_S)=(0,0,0)
$$


selects precisely


$$
\boxed{0\le j\le b.}
$$



The path $j=b$ is accepted. Its physical contribution is not confused with the zero telescoping flux $\mathcal A(b)=0$.

The receipt’s figures—$71$ digits, $248$ transitions, at most four live states, and $2399$ coefficient checks—are finite execution data for this input and precision. They are consistent with the proved bounds, but are not universal counts for higher precision.

---

## 9. Accepted numerical conclusion and its limits

The supplied receipt reports


$$
D_{\rm raw}\equiv0\pmod{2^{20}},
\qquad
E_{\rm raw}\equiv0\pmod{2^{20}}.
$$



After the source audit, the appropriate accepted statement is


$$
\boxed{
v_2(D_{\rm raw})\ge20,\qquad
v_2(E_{\rm raw})\ge20.
}
\tag{9.1}
$$



The $102$ direct small-input comparisons, of which $91$ are nonzero, corroborate the implementation at those finite inputs. The exact transport proof, not those comparisons, supplies the general identity used at the original input.

Nothing in (9.1) determines:

- either exact valuation;
- the ratio $E_{\rm raw}/(2D_{\rm raw})$;
- the all-prime gcd;
- a norm-relative logarithmic omission guard.

In particular, the relation


$$
\frac{H}{N_{\rm ratio}}
=\frac{E_{\rm raw}}{2D_{\rm raw}}
$$


still requires its actual denominator-depth precision analysis.

---

# Part III. A minimal justified precision extension

## 10. A quadratic stability lemma

The already-proved parity statement says that both complete weighted columns are even. This gives more scalar precision than a generic bilinear estimate would give.

### Lemma 10.1 — Physical precision versus Gram precision

Let $x,y$ be finite integral columns. Suppose


$$
x\equiv\widetilde x\pmod{2^{M_x}},\qquad
y\equiv\widetilde y\pmod{2^{M_y}},
$$


and


$$
\operatorname{cont}_2(x),\operatorname{cont}_2(\widetilde x)\ge a,
\qquad
\operatorname{cont}_2(y),\operatorname{cont}_2(\widetilde y)\ge c.
$$


Then


$$
x^Tx-\widetilde x^T\widetilde x
\in
2^{\min(M_x+a+1,\,2M_x)}\mathbb Z,
\tag{10.1}
$$


and


$$
x^Ty-\widetilde x^T\widetilde y
\in
2^{\min(M_x+c,\,M_y+a,\,M_x+M_y)}\mathbb Z.
\tag{10.2}
$$



#### Proof

Write


$$
x=\widetilde x+2^{M_x}h,\qquad
y=\widetilde y+2^{M_y}k.
$$


Then


$$
x^Tx-\widetilde x^T\widetilde x
=
2^{M_x+1}\widetilde x^Th+2^{2M_x}h^Th,
$$


which proves (10.1). Similarly,


$$
x^Ty-\widetilde x^T\widetilde y
=
2^{M_x}h^T\widetilde y
+2^{M_y}\widetilde x^Tk
+2^{M_x+M_y}h^Tk.
$$


This proves (10.2). ∎

The same argument applies with an integral fixed Gram matrix between the columns. Here the weights have already been incorporated into the physical coordinates.

### Application to the present input

Take


$$
M_x=M_y=20,\qquad a=c=1.
$$


Then


$$
\boxed{
D_{\rm raw}\text{ is determined modulo }2^{22},
\qquad
E_{\rm raw}\text{ is determined modulo }2^{21}.
}
\tag{10.3}
$$



This does **not** evaluate those extra digits. It proves that evaluating them using the retained integer lifts will recover genuine physical digits in exactly this range.

---

## 11. The first new bounded calculation

The existing source computed a shared $36$-bit transport but retained only $S_{ff}\bmod2^{34}$ in its artifact. I do not request a rerun of that accepted computation.

A new, strictly higher target is:



$$
\boxed{\text{shared kernel precision }37.}
$$



Using the existing physical short arrays, evaluate


$$
S_{ff}\pmod{2^{36}},\qquad
S_{fe}\pmod{2^{37}}.
$$


Then recover


$$
\boxed{
D_{\rm raw}\pmod{2^{22}},\qquad
E_{\rm raw}\pmod{2^{21}}
}
$$


by the same exact divisions and odd normalizers.

This is justified by Lemma 10.1; it is not a claim that an arbitrary lift supplies unlimited higher physical precision.

### Exact inputs

- the same original $b,n$;
- the retained $U_f,U_e$ arrays modulo $2^{341}$;
- the same normalizations $2^{73},2^{68}$;
- the same $71$-digit word;
- the same physical endpoint and complete $A_e$.

At $37$ kernel bits, the payload construction needs only


$$
U_f\pmod{2^{110}},\qquad
U_e\pmod{2^{105}},
$$


already contained in the retained arrays.

The uniform state degree bounds are


$$
162+2(37-1)=234,\qquad
158+2(37-1)=230,
$$


and after eight digits both are at most $72$. There are still at most four reachable borrow states.

### Expected verifiable output

The new certificate should give:

- $S_{ff}\bmod2^{36}$ and $S_{fe}\bmod2^{37}$;
- the recovered norm modulo $2^{22}$;
- the recovered mixed contraction modulo $2^{21}$;
- reduction to the accepted twenty-bit zeros;
- the same terminal-state and valuation-layer checks;
- exact valuations only when the new residues are nonzero.

No nonzero outcome is predicted. If both new residues vanish, the conclusions become only


$$
v_2(D_{\rm raw})\ge22,\qquad
v_2(E_{\rm raw})\ge21.
$$



---

## 12. What genuinely new physical precision would require

Using only the present content bounds $a,c\ge1$:

- $21$-bit physical data for both columns guarantee the norm modulo $2^{23}$;
- they guarantee the mixed contraction modulo $2^{22}$.

Thus a natural next genuinely physical target, if needed, is


$$
\boxed{
\text{columns modulo }2^{21}
\quad\Longrightarrow\quad
D_{\rm raw}\pmod{2^{23}},\
E_{\rm raw}\pmod{2^{22}}.
}
\tag{12.1}
$$



If the same short presentations remain valid, the sufficient shared kernel precision is then $38$. But their persistence at the new physical precision must be proved, not assumed.

### Required head/operator plan

Only new precision layers should be produced. The accepted twenty-bit work is not to be repeated.

The new layer must include:

1. both actual force heads at the precision required by the normalized inverse-loss bound;
2. every previously discarded branch whose certified valuation no longer exceeds the new threshold;
3. the complete finite endpoint solve;
4. both reconstructed columns and the second column’s exterior contribution;
5. a new-bit check of any short-numerator divisibility or discarded-branch assertion used at the higher precision.

For a finite endpoint equation


$$
Eq=t,
$$


a corrected operator and right-hand side satisfy the exact identity


$$
q'-q
=(E+\delta E)^{-1}
\bigl(t+\delta t-(E+\delta E)q\bigr).
\tag{12.2}
$$


If $q$ solves the chosen lower-precision lift exactly, this becomes


$$
q'-q=(E+\delta E)^{-1}(\delta t-\delta E\,q).
$$



Formula (12.2) preserves the nonlinear finite return. Replacing the inverse by $E^{-1}$ requires a separate valuation justification.

If the normalized inverse has a loss $\sigma$, the relevant operator and residual data must be supplied with that loss paid. The relation-matrix Smith exponent $8$ is **not** a substitute for this physical inverse-loss bound.

The supplied binary postprocessing sources do not certify a numerical head length for physical precision $21$. In particular, the output numerator degrees $81,77$ are not a universal head-memory theorem. A numerical higher-precision head cutoff must come from the retained physical tail and inverse bounds.

---

# Part IV. Independent review of A2turn5

## 13. Scope and the retained finite problem

This is a different original family:


$$
p=29,\qquad
b=3^{249005515+574312172u},\qquad
n=2001b,\qquad u\ge0.
$$



The reconstructed range remains $0\le j\le b$, and the source rows remain


$$
1\le i\le b-2.
$$


The two corrected columns remain


$$
Z_w=\mathcal RA^{-1}f^0,\qquad
Y=\mathcal RA^{-1}\mathbf r+W_be_b.
$$



With


$$
P=Z_w/p^2=p^cx,
$$


where $x$ is $p$-primitive, the norm valuation is


$$
d=2c+4+\nu,\qquad \nu=v_p(x^Tx).
$$



I retain the established input information


$$
g=0,\qquad f_1^0/f_0^0\equiv465\pmod{841}.
$$



---

## 14. Audit of the complete $p^{-3}$ column reduction

The decisive issue is whether the actual next head, $p\mathsf D_1$, and the solved endpoint were eliminated by valid weighted divisibility—not merely because the preceding column vanished.

The supplied argument meets that obligation, under the retained finite normal-form and truncation hypotheses.

### 14.1 The complete next head

The reconstructed baseline short-head atoms have


$$
(a,v)=(r+1,-r-1),\qquad(r+1,-r),
\qquad0\le r\le233.
$$



Digits $3,4,5$ force at least two valuation events. If the first two weight digits do not borrow, then


$$
j\bmod841\le205.
$$


The two lower minuends are $838-r,839-r$, both exceeding $205$, while the upper addend is $406+r$. Hence their sum after subtracting the weight index is at least


$$
1244-205=1039>841.
$$


A further low addition carry is forced.

Thus the baseline reconstruction maps the entire relevant integral head into $p^3$-divisible columns. Consequently the retained term $pBh^{[1]}$ vanishes modulo $p^4$, including the actual digit


$$
h^{[1]}_1=16.
$$



### 14.2 The compatible $p\mathsf D_1$ terms

For $1\le t<29$, the coefficient $\binom{-n}{t}$ supplies an extra factor $p$. The surviving cases are precisely those displayed in A2turn5.

The row-factor cases are important and correct:

- for $s<29,t=0$, a nonzero $\binom js\bmod p$, with no low weight borrow, forces $s\le j_0\le2$;
- for the shifted term, a nonzero $j\binom{j-1}s\bmod p$ forces $j_0\ge s+1$, leaving only the stated case;
- for $s=29,t=0$, absence of the extra low event forces $j_1=0$, which kills the displayed row factor;
- for $s=t=29$, the low addition carry is forced directly.

The conclusion concerns the **coefficient-weighted reconstructed terms**. It does not falsely claim a third carry for every unweighted positive-offset atom.

### 14.3 The actual first endpoint return

The solved first endpoint charges are retained in


$$
z_1=z_{1,0}e_b+z_{1,1}e_{b+1}.
$$


For offsets $v=0,1$, the additional low event is forced. For $v=2$, a missing event requires $j_0=0$, and the reconstruction factor $j$ then supplies the factor $p$.

Therefore the endpoint contribution vanishes modulo $p^4$ only **after** retaining and reconstructing the solved endpoint.

### 14.4 Reduction to the single atom and the sign

After these eliminations, only $r=0$ from the leading factorial head survives at this precision. The contact coefficient has sign $(-1)^j$; applying


$$
W_j(j\theta_{j-1}-\theta_j)
$$


produces $(-1)^{j+1}$.

For $j_0\in\{0,1,2\}$, $b-j$ is a unit and the adjacent positive binomials agree modulo $p$. The identity


$$
dF_{d-1}+F_d=1
$$


then gives the reported single-atom formula. For $j_0>2$, the additional event gives zero at this level.

Thus I retain


$$
\boxed{
\frac{Z_{w,j}}{p^3}
\equiv
A_0(-1)^{j+1}
\frac{\binom{n+2}{j}\binom{2n+b-1-j}{b-1-j}}{p^3}
\pmod p,\qquad j<b.
}
\tag{14.1}
$$


The quotient is integral.

At $j=b$, the four forced low weight borrows give $v_p(W_b)\ge4$, so the actual terminal coordinate is zero at this precision.

In particular,


$$
\boxed{c\ge1.}
$$



---

## 15. Low support and the finite partial last block

The relevant low digits are consistent with


$$
b\bmod p^6=(27,28,5,28,0,20)_{29},
$$




$$
(n+2)\bmod p^6=(2,7,24,7,3,9)_{29}.
$$



Equality in the three-event lower bound gives exactly the displayed support


$$
d\in\{0,1,2\},
$$




$$
e\in\{0,\ldots,7\}\cup\{14,\ldots,28\},
$$




$$
f\in\{0,\ldots,5\},
$$




$$
t\in\{0,\ldots,7\}\cup\{15,\ldots,28\},
\qquad k=0,\qquad0\le\ell\le20.
$$



Every supported low residue $s$ is strictly below $\beta=b\bmod p^6$. Indeed, even at equality in the higher low digits, its digit zero is at most $2$, whereas $\beta_0=27$.

Therefore, for


$$
j=s+p^6q,\qquad b=\beta+p^6C,
$$


the exact supported range is


$$
\boxed{0\le q\le C.}
$$


The last block is not artificially completed; all supported residues in that block are genuinely inside the original cutoff.

The outgoing carries produce the reported high factors


$$
V(q)=\binom Xq\binom{2X+C-q}{C-q},
$$




$$
F_{\mathrm I}(q)=(2X+C+1-q)V(q),\qquad
F_{\mathrm{II}}(q)=(X-q)V(q),
$$


where


$$
X=2001C+1382.
$$



---

## 16. Correction of the low Gram coefficients

This is the failed claim in A2turn5.

### 16.1 Independent recovery of the factor $K_{34}$

For digit $3$, after combining the weight and positive-binomial factorial units and squaring:

- the range $0\le t\le7$ gives, up to the common factor $(7!/15!)^2$,
  

$$
\bigl((a+1)\cdots(a+7)\bigr)^2,\qquad a=7-t\in\{0,\ldots,7\};
$$


- the range $15\le t\le28$ gives the same polynomial with
  

$$
a=36-t\in\{8,\ldots,21\}.
$$



At digit $4$, the corresponding factors are $7^2$ and $3^2$.

The full finite-field sum of this degree-$14$ polynomial is zero, and its values at $a=22,\ldots,28$ vanish. Hence the second range contributes the negative of the first. This proves the source’s structural formula


$$
K_{34}
=
\left(\frac{7!}{15!}\right)^2
(7^2-3^2)
\sum_{a=0}^{7}\bigl((a+1)\cdots(a+7)\bigr)^2.
\tag{16.1}
$$



The error is in evaluating the last sum.

### 16.2 Explicit arithmetic

Modulo $29$, the eight products and their squares are:



$$
\begin{array}{c|rrrrrrrr}
a&0&1&2&3&4&5&6&7\\ \hline
(a+1)\cdots(a+7)
&23&10&16&5&21&4&28&27\\
\text{square}
&7&13&24&25&6&16&1&4
\end{array}
$$



Their sum is


$$
7+13+24+25+6+16+1+4=96\equiv9\pmod{29}.
$$


Also


$$
\left(\frac{7!}{15!}\right)^2=1,\qquad
7^2-3^2\equiv11.
$$


Therefore


$$
\boxed{K_{34}=11\cdot9=12\pmod{29},}
$$


not $27$.

The other displayed factors survive audit:



$$
K_{012}=27,
$$


and the digit-five sums are


$$
\sum_{\ell=0}^{9}\binom{20}{\ell}^2=10,\qquad
\sum_{\ell=10}^{20}\binom{20}{\ell}^2=19.
$$



Hence the corrected complete low coefficients are


$$
\boxed{
L_{\mathrm I}^{(3)}=27\cdot12\cdot10=21,
}
$$




$$
\boxed{
L_{\mathrm{II}}^{(3)}=27\cdot12\cdot19=8=-21
\pmod{29}.
}
\tag{16.2}
$$



Thus the claimed numerical pair $11,-11$ is disproved by explicit arithmetic. No rerun of an older auxiliary Gram computation is needed.

---

## 17. The high-sum symmetry is valid on the original finite range

Write


$$
C=\delta+pC_7,\qquad X=19+pY.
$$


For $q=d+pr$, write


$$
C-q=k+p(C_7-r-\varepsilon),
$$


where


$$
d+k=\delta+p\varepsilon,\qquad\varepsilon\in\{0,1\}.
$$



A nonzero low factor requires $0\le d,k\le19$. Its squared weight is


$$
\binom{19}{d}^2\binom{9+k}{k}^2
=
\binom{19}{d}^2\binom{19}{k}^2.
$$



For fixed $\varepsilon$, the high factor is independent of $d,k$. Crucially, the exact high-index range is


$$
0\le r\le C_7-\varepsilon.
$$


It is unchanged by exchanging $d$ and $k$. This explicitly checks the partial last block rather than appealing to a symmetry of a completed sum.

The multiplier difference is


$$
(10+\delta-d)^2-(19-d)^2
\equiv(\delta+20)(\delta-2d)\pmod p.
$$


Under $d\leftrightarrow k$,


$$
\delta-2k\equiv-(\delta-2d)\pmod p.
$$


The weight is symmetric, so the terms cancel, including fixed points.

Therefore


$$
\boxed{\mathscr T_{\mathrm I}=\mathscr T_{\mathrm{II}}\pmod{29}.}
$$



With the corrected coefficients, the whole leading norm is


$$
\boxed{
\left(\frac{Z_w}{p^3}\right)^T
\left(\frac{Z_w}{p^3}\right)
\equiv
21A_0^2(\mathscr T_{\mathrm I}-\mathscr T_{\mathrm{II}})
=0\pmod p.
}
\tag{17.1}
$$



Thus the principal conclusion survives:


$$
\boxed{d\ge7.}
$$


If $c=1$, this implies $\nu\ge1$. It does not prove $c=1$, $\nu=1$, or $d=7$.

---

# Part V. A sharper original-orbit content obstruction

## 18. Eleven obstructed $C$-classes

The source’s obstruction $C\equiv814=(2,28)_{29}\pmod{841}$ is correct, but the same proof gives more.

### Theorem 18.1

For the original family, if


$$
\boxed{
C\equiv2+29\gamma\pmod{841},
\qquad18\le\gamma\le28,
}
\tag{18.1}
$$


then


$$
\boxed{c\ge2,\qquad d\ge8.}
$$



#### Proof

Since


$$
X=2001C+1382=19+29(69C+47),
$$


the condition $C_0=2$ gives


$$
X_0=19,\qquad X_1=11,
$$


and therefore


$$
(2X)_0=9,\qquad(2X)_1=23.
$$



If


$$
V(q)=\binom Xq\binom{2X+C-q}{C-q}
$$


is nonzero modulo $29$, write $K=C-q$. Lucas’ condition for the first factor and the no-carry condition for the second imply


$$
q_0\le19,\qquad K_0\le19,
$$




$$
q_1\le11,\qquad K_1\le5.
$$


Thus


$$
q_1+K_1\le16.
$$



Let $\varepsilon\in\{0,1\}$ be the carry from digit zero in $q+K=C$. At digit one,


$$
q_1+K_1+\varepsilon
=\gamma+29\varepsilon_1.
$$


The left side is at most $17$, whereas $\gamma\ge18$. This is impossible.

Hence $V(q)=0$ for every $q$, so the complete column (14.1) vanishes modulo $p$:


$$
Z_w\in p^4\mathbb Z_p^{b+1}.
$$


Since $P=Z_w/p^2$, we have $c\ge2$. Therefore


$$
d=2c+4+\nu\ge8.
$$


∎

This two-digit obstruction is sharp within the slice $C_0=2$ as a **low-digit feasibility test**:

- for $0\le\gamma\le16$, one can choose low digits with carry $\varepsilon=0$;
- for $\gamma=17$, choose $\varepsilon=1$, $q_0=12$, $K_0=19$, $q_1=11$, $K_1=5$.

This does not show that the corresponding complete high-word column is nonzero. Higher digits can still obstruct it.

---

## 19. Occurrence on the original power orbit

Let


$$
T=574312172=28\cdot29^5.
$$


The retained calculation


$$
3^{28}\equiv1+15\cdot29\pmod{29^2}
$$


gives


$$
v_{29}(3^T-1)=6,\qquad
\frac{3^T-1}{29^6}\equiv15\pmod{29}.
$$



For


$$
C(u)=\frac{3^{249005515+Tu}-\beta}{29^6},
$$


the increment under $u\mapsto u+29^k$, divided by $29^k$, is a unit modulo $29$. Its first residue is


$$
\beta\cdot15\equiv27\cdot15\equiv-1\pmod{29}.
$$


Thus $u\mapsto C(u)$ is a bijection modulo $29^k$.

In particular, each class in (18.1) corresponds to exactly one $u\bmod841$. The source’s $C\equiv814$ class is one of these eleven classes.

The word “unique” must be interpreted correctly: there is a unique original $u$-class mapping to a **specified** $C$-class. The source does not prove that $814$ is the only obstructed $C$-class, and Theorem 18.1 shows that it is not.

No numerical labels for the eleven $u$-classes are needed for this theorem.

---

# Part VI. Remaining complete-force and global obligations

## 20. What remains open locally

### Binary side

The exact twenty-bit Gram zeros are now established finite data. The immediate unresolved question is whether the norm first becomes nonzero in the rigorously accessible additional digits.

If it remains zero, one needs either:

- genuinely higher physical columns with certified finite return and truncation; or
- a stronger theorem controlling content, norm depth, or sensitivity.

A different unvalidated integer lift is not a substitute.

### $29$-adic side

The next local task remains the complete


$$
Z_w/p^3\pmod{29^2},
$$


including the actual next head, lower-operator corrections, and solved endpoint. The required whole norm is


$$
\frac{(Z_w/p^3)^T(Z_w/p^3)}{29}\pmod{29},
$$


formed only after assembling the whole numerator.

The corrected leading coefficient is $21$, not $11$. The eleven obstructed classes must be recognized by any proposed content stratification.

There is no uniform $c=1$ theorem. Nor has a uniform upper bound on $c$ or the primitive norm loss $\nu$ been proved.

### Split $3$-adic endpoint form

The coordinator’s discriminant deduction from A4turn7 is correct: the form splits over $\mathbb Q_3$, with root depths $3,4$ and first units $-1$. Hence a coefficient-only anisotropic valuation bound is unavailable.

I do not reopen the accepted scalar or factorial calculations. Original-family line avoidance, or a bound on approach to those lines, remains the appropriate obligation being advanced by A1.

---

## 21. Both corrected columns and the full forcing remain unchanged

Nothing in this report changes the original finite producer.

On the $29$-adic side, the complete second-force identity remains


$$
p^3U_a^TQ
=
p^3(r_0G^{(3)}_{a0}+r_1G^{(3)}_{a1})
+\sum_{\ell=1}^{b-2}\mathcal H_\ell\lambda'_{a,\ell}
+W_bU_{a,b}.
$$


Both initial charges, every source row $1\le\ell\le b-2$, and the exterior term at $b$ remain. There is no source row at $b-1$, and the exterior row is not a recurrence step.

The actual target is still


$$
x^TQ-p^c\rho_nx^Tx
\equiv0\pmod{p^{c+\nu+1}},
$$


with $\rho_n$ defined independently, and with the logarithmic guard


$$
N_{\log}\ge c+4+\nu.
$$



On the inherited full-producer side, the original pole cutoff remains


$$
0\le v\le2n-2.
$$


Both corrected representatives, all lower-pole and factorial forcing, LOW subtraction, and the nonlinear endpoint elimination remain. In particular, the terminal return is not replaced by a homogeneous equation:


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


No moment beyond the retained boundary is introduced, and $\omega_{\nu-1}$ is not discarded.

The binary contraction audit uses the certified complete physical arrays at their stated precision. It does not settle any separate higher-precision or norm-relative omission obligation.

---

## 22. All-prime normalization and the whole same-index error

No row content or actual clearer has been divided away in these local conclusions.

After restoring all row contents and the least actual two-column clearer $d_B$, retain


$$
A_B=N_{B,1}^{T}\Omega N_{B,1}>0,
\qquad
H_B=N_{B,1}^{T}\Omega N_{B,2},
$$


and the **all-prime** gcd


$$
\boxed{g_B=\gcd(A_B,|H_B|).}
$$



The actual primitive pair is


$$
\boxed{
q_n=A_B/g_B,\qquad p_n=H_B/g_B,
}
$$


and the primitive multiplier remains $d_B^2/g_B$.

The evaluated approximation error is the whole same-index expression


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n.
}
$$



Neither a selected-prime norm zero nor a content improvement determines $g_B$, $q_n$, or the size of this whole form.

Even under the retained signed-error asymptotic at its stated family scope, the missing global theorem is still an infinite original-sequence comparison between:

- the actual primitive denominator after the all-prime gcd; and
- the complete, nonzero, same-index error.

A single original Gram evaluation cannot supply that theorem.

---

# Proof-status ledger

| Statement | Status |
|---|---|
| Original $163\times160$ matrix and zero telescoping flux | Audited |
| Reported modular Smith identities | Supplied finite execution certificate |
| Exactness of the reported Smith exponents | Proved from the verified modular normal form |
| Exact annihilator lift modulo $2^{351}$ | **Proved here explicitly** |
| Exact saturated quotient coordinates after unit pairing | **Proved here explicitly** |
| Lifted payload free contents $157,154$ | Certified by the supplied finite data and exact-lift theorem |
| Sufficient observable precisions $23,23$ | Verified |
| Binary scale, sign, normalization, and finite-end encoding | Audited |
| $D_{\rm raw}=E_{\rm raw}=0\bmod2^{20}$ | Accepted finite computation |
| Exact binary norm or mixed depth | Not established |
| Existing physical data determine norm modulo $2^{22}$, mixed modulo $2^{21}$ | **New proof** |
| Those additional residues | Not evaluated here |
| A2 complete $p^{-3}$ single-atom column | Verified under retained finite-normal-form hypotheses |
| A2 claimed low coefficients $11,-11$ | **Incorrect** |
| Corrected low coefficients $21,-21$ | **Explicitly derived and evaluated here** |
| High-sum equality with the original partial last block | Verified |
| $29$-adic norm bound $d\ge7$ | Survives with corrected coefficient |
| $c\ge2,d\ge8$ on eleven original residue classes | **New theorem** |
| Exact content or first nonzero primitive norm digit on those classes | Open |
| Complete second-force alignment at the true relative depth | Open |
| All-prime primitive denominator versus whole error | Open |
| Irrationality or rationality of $e+\pi$ | Unresolved |

---

## Conclusion

The new binary work closes two genuine finite obligations:



$$
\boxed{\text{exact saturated postprocessing}}
$$


and


$$
\boxed{\text{the original complete twenty-bit weighted norm and mixed contraction}.}
$$



The saturation proof is valid after explicitly correcting the modular annihilators with the rational inverse of the degree-$3,\ldots,162$ minor and normalizing their unit pairing. The Gram zeros are valid lower bounds, not exact depths.

The immediate new bounded calculation is a $37$-kernel-bit extension using the existing physical data. The quadratic stability lemma proves that its norm modulo $2^{22}$ and mixed output modulo $2^{21}$ are genuine physical information. Further digits require a certified physical lift or a stronger structural bound.

On the $29$-adic side, the claimed low coefficient $11$ must be replaced by $21$. The whole leading norm still vanishes because the high-sum symmetry is valid with the original finite cutoff. The content obstruction also strengthens to eleven original residue classes, on which


$$
\boxed{c\ge2,\qquad d\ge8.}
$$



The exact remaining local bottlenecks are higher physical norm depth on the binary side and the complete next-order finite-return content/norm law on the $29$-adic side. The global bottleneck remains all-prime control of the actual primitive denominator against the whole nonzero same-index error on an infinite original sequence.



$$
\boxed{\text{An unconditional proof or disproof of the irrationality of }e+\pi
\text{ remains unresolved.}}
$$


