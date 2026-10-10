> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4, turn 14 — Complete-source audits, a reference-intersection product certificate, and the recovered primitive denominator

## Executive conclusions

The new sources close two previously explicit interfaces, but they do not close the irrationality problem.

1. **Binary separator promotion.** The operator guard $39$, downstream guard $40$, and therefore the proposed guard $41$, are sufficient for the stated precision-$32$ integral presentations. Below I supply an additional exact formula for the normalized first head that pays the positive-order coefficient divisions; the constant-order calculation alone would not suffice. With the retained complete-producer identities, the separator theorem applies to both complete columns on the original inclusive range $0\le j\le b$.

   Consequently, infinitely many original indices in each of the indicated binary neighborhoods have
   

$$
v_2(D_{\rm raw})\ge34,\qquad v_2(E_{\rm raw})\ge35.
$$


   This does **not** prove infinitely many original blocks of exact high-norm depth one.

2. **The eight-state counter is mathematically sound.** In particular, a minimum whose multiplicity is $0\bmod8$ remains a reachable minimum. The supplied implementation preserves this distinction. Its 64 exact auxiliary sums and 32 full-word tests corroborate precisely those finite cases; no original high word has been evaluated.

3. **A3’s primewise Smith argument and its global product/exclusive divisibilities are valid.** The new $3375$ receipt shows that the particular canonical scalar is arithmetically very large after removing all small-prime factors:
   

$$
U_{3375}=2^{14}\cdot31\cdot67\cdot211\cdot239,
   \qquad \operatorname{bits}(U_{3375})=41.
$$


   This is not a subsequence impossibility theorem.

   I prove a new, second product certificate. It intersects A3’s certificate with the product of the two canonically normalized reference projections. Its excess over the actual large-prime endpoint product is supported on, and bounded by the square of, an explicit **reference-transverse content**. This gives an alternative arithmetic target that does not require the entire canonical $\Theta_n$ to be smooth.

4. **A1’s modulo-$9$ killing theorem is valid.** The universal seventeen-coordinate operator $0202$ kills the inherited divided carry, not merely the new injection. The original progression
   

$$
j\equiv84645\pmod{531441}
$$


   is now an accepted finite identification of the previously proved progression. The modulo-$27$ transition construction is also correct. Its forty zero endpoint pairs do not establish a universal modulo-$27$ killing theorem or an original-power primitive direction.

5. **A2’s hypothesis $\mathbf H$ is closed by the recovered actual head.** The recovery occurs before the integral finite normal ordering, in the correct coordinates. The physical saturation-and-radical proof then gives, unconditionally on the original progression,
   

$$
\boxed{u\equiv2\pmod{24389}\Longrightarrow
   Z_w\in29^4\mathbb Z_{29}^{\,b+1},\quad
   Z_w^TZ_w\in29^9\mathbb Z_{29}.}
$$


   Thus $c\ge2,d\ge9$ are now unconditional there. Neither is inferred from the contracted tail zero.

6. **The binary final bridge is recovered, not globally missing.** It gives the actual all-prime denominator through
   

$$
\frac{p_n}{q_n}
   =\frac{2b!}{\lambda R}\frac{H}{N}.
$$


   In the range where A5’s raw ratio is proved to be a binary unit, the actual primitive denominator has a large binary exponent $C_n$, rather than the zero binary denominator suggested by looking only at the raw ratio.

The final all-prime denominator versus the whole nonzero same-index error remains the decisive unresolved obligation.

---

# 1. Binary promotion: divisions, continuity, and the complete finite boundary

Throughout this section,


$$
b=b(u)=9^{18+32u},\qquad n=4002b,\qquad h=n/2=2001b.
$$


I retain the original physical range


$$
\boxed{0\le j\le b.}
$$



To avoid the notation collision in the recovered bridge, I will later distinguish A5’s current raw columns from the older columns called $X,Y$.

## 1.1 The operator continuity argument is valid over $\mathbb Z_2$

For integral $x,t$,


$$
\binom{x+2^Lt}{r}-\binom xr
=\sum_{i=1}^r\binom{2^Lt}{i}\binom{x}{r-i},
$$


and therefore


$$
v_2\!\left(\binom{x+2^Lt}{r}-\binom xr\right)
\ge L-\lfloor\log_2r\rfloor.
$$


This includes generalized binomials with negative integral top.

Applied to the displayed operator formulas:

- the largest lower index in $F$ is $371$, with affine top coefficient $-4002$;
- the crossing and inverse-symbol lower indices are at most $124$;
- $\lambda_s$ and $CC_s$ are integral divided-power coefficients;
- the symbol filtration is
  

$$
v_2(\lambda_s),v_2(CC_s)\ge\lceil s/4\rceil.
$$



The worst displayed operator loss is consequently $7$ bits. Thus $L=39$ gives precision $32$.

Moreover,


$$
\overline K\equiv0\pmod2,\qquad S_{\rm end}=I+G\overline K\equiv I\pmod2.
$$


Hence $S_{\rm end}^{-1}$ exists over $\mathbb Z_2$, and


$$
S_{\rm end}(b')^{-1}-S_{\rm end}(b)^{-1}
=S_{\rm end}(b')^{-1}
\bigl(S_{\rm end}(b)-S_{\rm end}(b')\bigr)
S_{\rm end}(b)^{-1}
$$


loses no binary precision.

Here **integral inverse means $\mathbb Z_2$-integral**, not necessarily an integer matrix over $\mathbb Z$.

The finite padded solve also retains its actual $372$-row boundary. The lower padded zero block follows from $CC_r\equiv0\bmod2^{32}$ for $r\ge125$; it is not an extrapolation of a finite receipt to an infinite inverse.

## 1.2 A complete positive-order first-head normalization

The recovered contact source supplies


$$
f_i^0=\frac{(n+i)!}{n!}J_i,\qquad
J_i=[t^n](1+2t+2t^2)^n(1+t)^i,
$$


and


$$
R=2^h\binom{2h}{h}.
$$



It is important to audit $f_i^0/R$ for every retained positive order, rather than checking only $J_0/R$.

Put


$$
\phi(z)=1-z+\frac{z^2}{2},
\qquad
c_t=\frac{2^t}{\binom{2t}{t}}.
$$


Then the following identity holds exactly:


$$
\boxed{
\sum_{i\ge0}\frac{f_i^0}{R}\frac{z^i}{i!}
=(1-z)^{-2n-1}
\sum_{t=0}^{h}
c_t\binom ht^2\phi(z)^{h-t}.
}
\tag{1.1}
$$



### Derivation

First,


$$
\sum_{i\ge0}\frac{f_i^0}{R}\frac{z^i}{i!}
=\frac1R[t^n]\frac{(1+2t+2t^2)^n}
{(1-z(1+t))^{n+1}}.
$$


Writing $a=z/(1-z)$, the formal residue substitution


$$
t=\frac{u}{1+au}
$$


gives


$$
[t^n]\frac{(1+2t+2t^2)^n}{(1-at)^{n+1}}
=[u^n]\bigl(1+2(a+1)u+(a^2+2a+2)u^2\bigr)^n.
$$


For $n=2h$, expanding its central coefficient and dividing by
$2^h\binom{2h}{h}$ yields (1.1).

Now


$$
v_2(c_t)=t-v_2\binom{2t}{t}
=t-s_2(t)=v_2(t!).
\tag{1.2}
$$


Thus the reduced denominator of $c_t$ is odd.

More explicitly, the $i$-th divided coefficient of the right side of (1.1) is a sum of terms


$$
c_t\binom ht^2
\,i!\binom{2n+i-r}{i-r}
\binom{h-t}{r-q}\binom{r-q}{q}
(-1)^{r-2q}2^{-q},
\tag{1.3}
$$


where $0\le r\le i$ and $0\le q\le\lfloor r/2\rfloor$.

Every potentially nonunit coefficient division in (1.3) is paid:


$$
v_2(i!)-q
\ge v_2(i!)-\lfloor i/2\rfloor
=v_2(\lfloor i/2\rfloor!).
\tag{1.4}
$$


All remaining parameter-dependent factors are integer-valued binomials.

Consequently:

- $f_i^0/R\in\mathbb Z_2$ for every $i$;
- the tail $t\ge36$ has depth at least $v_2(36!)=34$;
- the head tail $i\ge72$ has depth at least $34$;
- for the retained $i\le71$, the binomial continuity loss is at most $6$ bits.

This supplies a direct all-positive-order justification of the normalized first-head claim used by A5.

It also identifies the limitation correctly: if one instead stores ordinary coefficients $(f_i^0/R)/i!$, one cannot divide a precision-$32$ residue by $i!$ and retain precision $32$. One must use the exact formula or supply the additional $v_2(i!)$ bits. The accepted construction uses the integral divided-coordinate form.

The reconstruction’s displayed $D_b^{-1}$ divisions are likewise paid in all orders by the exact identity


$$
\mathcal T_{jr}
=\binom{n+2}{j}
\left[
j\binom{-n}{r-j+1}-\binom{-n}{r-j}
\right],
$$


not merely by a constant-order argument.

## 1.3 Downstream precision and all complete terms

For the supplied downstream integral formulas, the largest lower index is $531$, occurring with affine coefficient $4002$ or $8004$. The worst loss is $9-1=8$ bits. Thus


$$
\boxed{b\equiv b_0\pmod{2^{40}}}
$$


is sufficient for precision $32$.

This conclusion retains:

- both full force inputs;
- the $160$-entry exterior load;
- both finite terminal returns;
- both Laurent branches;
- the entire prefix subtraction;
- the terminal selection and reversal;
- the exterior value $-bg_0-1$;
- the original branch and terminal cutoffs.

Division by a fixed unit-constant polynomial is coefficientwise integral, so it does not introduce a hidden positive-order loss. This does not promote modular factor counts to characteristic-zero multiplicities.

The parameter-dependent logarithmic omission bound is retained as


$$
1+2000b-s_2(2001b)+s_2(b)
-\lfloor\log_2(8005b-1)\rfloor,
$$


rather than replacing its logarithmic term by a constant computed at $b_0$.

**Audit conclusion:** A5’s guards $39$ and $40$, hence $41$, are sufficient for the stated complete modular producer. Formula (1.1) supplies the positive-order normalization argument that should accompany that conclusion.

---

# 2. What the separator and the eight-state counter prove

## 2.1 Complete-original tensorization

Retain


$$
T=103,\qquad L\ge135,\qquad M=2^T,\qquad
b=b_0+2^Lh,\qquad m_h=2^{L-T}h.
$$


The supported factorial splitting and the unsupported-row carry argument together yield the complete coordinate comparison modulo $2^{32}$.

The unsupported case is not justified by a formal negative valuation. Once the low row exceeds the relevant low cutoff, its borrow state enters the zero separator in one of


$$
010,\quad110,\quad111.
$$


Each zero-parameter digit contributes at least one genuine event to the sum of the two binomial valuations. The $L-T\ge32$ separator therefore kills the unsupported atom at the required precision.

All supported model rows satisfy


$$
0\le j_0+Mk\le b,
$$


including $j_0=b_0,k=m_h$. No terminal block is completed beyond the original range.

Thus the complete whole contractions satisfy


$$
D_{\rm raw}(b)\equiv S_{L,h}D_0\pmod{2^{42}},
\qquad
E_{\rm raw}(b)\equiv S_{L,h}E_0\pmod{2^{41}}.
\tag{2.1}
$$



If


$$
c=\min_kv_2(H_{L,h}(k)),\qquad t=v_2(S_{L,h}),
$$


then for $c\le22$,


$$
v_2(\operatorname{content}_2 X_{\rm raw})=9+c
$$


and


$$
D_{\rm raw}\equiv285\,2^{33}S_{L,h}\pmod{2^{42+c}},
$$




$$
E_{\rm raw}\equiv13\,2^{34}S_{L,h}\pmod{2^{41+c}}.
\tag{2.2}
$$



These are finite-precision comparisons, not exact integer factorizations by $S_{L,h}$.

## 2.2 Infinite original classes: even high norm, not exact depth one

Since


$$
v_2(9^{32u}-1)=8+v_2(u),
$$


for every fixed $L\ge135$ there is an original arithmetic progression of indices satisfying


$$
b(u)\equiv b_0+3\cdot2^L\pmod{2^{L+2}}.
$$


On it $h\equiv3\bmod4$, and the high norm is even. Hence infinitely many original indices satisfy


$$
\boxed{
v_2(D_{\rm raw})\ge34,\qquad
v_2(E_{\rm raw})\ge35.
}
\tag{2.3}
$$



This proves the asserted raw-norm noncontinuity at $b_0$, and also noncontinuity after division by the **fixed** factor $2^{18}$. It does not concern normalization by the varying actual content.

For $h=4H+3$, the stronger identity is


$$
S_{L,h}\equiv2\binom{4003H+3002}{H}\pmod4,
$$


so


$$
v_2(S_{L,h})=1
\iff H\mathbin{\&}(4002H+3002)=0.
\tag{2.4}
$$


This tests the whole $H$. Congruence $h\equiv3\bmod4$ alone does not force it. Neither the source proof nor the new receipt proves that infinitely many original powers pass (2.4).

## 2.3 Audit of minimum/minimum-plus-one counting

For


$$
a_k=\binom{4002m}{k}\binom{8005m-k}{m-k},
\qquad0\le k\le m,
$$


the subtraction-borrow formula gives


$$
v_2(a_k)=v_2\binom{8005m}{m}
+B_{4002m}(k)+B_m(k)-B_{8005m}(k).
$$


The eight-state transition therefore correctly uses weight


$$
\alpha'+\beta'-\gamma'.
$$



Starting and ending in $000$ is essential. Processing the bit length of $8005m$ and accepting only terminal $000$ enforces all three nonnegative subtractions, especially $k\le m$. Additional leading zero digits cannot rescue a nonzero terminal borrow.

At a fixed state, all continuations are identical for all paths reaching that state. Therefore terms more than one above its reachable minimum can never become one of the two lowest final exponents through a later continuation from that same state.

The implementation correctly distinguishes:

- **no reachable path**, represented by absence of the state;
- **reachable paths with count $0\bmod8$**, represented by a present state and its true minimum.

The zero placeholder for the minimum-plus-one coefficient cannot create a falsely smaller minimum: the corresponding minimum transition is always present and is one exponent lower. It contributes zero to coefficients when that level is genuinely absent.

Finally,


$$
\frac{\sum_k a_k^2}{2^{2c}}
\equiv N_c+4N_{c+1}\pmod8
$$


uses only the fact that odd squares are $1\bmod8$.

The supplied 64 complete exact sums, the separated $h=3,11$ cases, and the 32 full-word tests are accepted finite corroborations. They need no repetition.

---

# 3. A3’s product certificate, and a new reference-intersection certificate

Here the original domain remains


$$
n=15^r\quad\text{or}\quad n=105^r,\qquad r\ge2,
$$


with


$$
m=n+1,\qquad N=n+2.
$$


All statements in this section about “large primes” mean $p>N$.

## 3.1 Audit of the existing Smith inequalities

A3’s local factorization


$$
\begin{pmatrix}R_0&C_0\\R_3&C_3\end{pmatrix}=AB
$$


has the required hypotheses:

- each row of $A$ is primitive;
- $v_p(\det A)=s$, the actual contact collision depth;
- $B$ has content $b$ and determinant depth $d$.

The exact transverse content is


$$
b=\min\{v_p(\ell),v_p(Z),v_p(Y-2X),v_p(\mathscr K_n)\}.
$$


The proof uses both primitivity hypotheses at their stated large-prime scope. Its converse correctly requires $P$ and $h$ to be units after the displayed vanishing conditions.

The determinant calculation is also correct:


$$
\det(L,\mathbf H,\mathbf C)
=-\frac{mN^2}{2}\mathcal D_L.
$$


All prefactors are units at $p>N$, and the canonical normalization


$$
\Theta_n=\frac{2^{m/2}}{n!}\mathcal D_L
$$


is a unit rescaling there.

For


$$
e_j=\min\{v_p(R_j),v_p(C_j)\},
$$


the deductions


$$
b\le e_j\le d-b,
$$




$$
0\le\min(e_0,e_3)-b\le s,
$$


and


$$
e_0\ne e_3\Longrightarrow\min(e_0,e_3)=b+s
$$


are valid.

Consequently,


$$
|e_0-e_3|\le(d-2b-s)_+,
$$




$$
e_0+e_3\le d+\min(s,d-2b).
$$


These imply exactly A3’s product and exclusive divisibilities:


$$
\delta_0^{>}\delta_3^{>}
\mid
\mathcal W_n
:=D_n^{>}\gcd(\Sigma_n,\mathcal A_n),
\tag{3.1}
$$




$$
E_{0,n}E_{3,n}
\mid
\frac{\mathcal A_n}{\gcd(\mathcal A_n,\Sigma_n)}.
\tag{3.2}
$$



No primewise unit conclusion follows from the real saddle dominance. The saddle argument proves eventual nonvanishing and the stated real height of $\Theta_n$, and nothing stronger arithmetically.

## 3.2 What the new $3375$ scalar receipt establishes

The exact canonical split is


$$
|\Theta_{3375}|=U_{3375}D_{3375}^{>},
$$


where


$$
U_{3375}
=2^{14}\cdot31\cdot67\cdot211\cdot239
=1\,716\,077\,084\,672.
$$


The reported bit lengths are


$$
\operatorname{bits}(\Theta)=110096,\qquad
\operatorname{bits}(D^{>})=110055,\qquad
\operatorname{bits}(U)=41,
$$


and


$$
\gcd(\Sigma,D^{>})=1.
$$



Thus, at this index,


$$
\mathcal B=1,\qquad
\mathcal W=D^{>}.
$$


The certificate is extremely loose compared with the accepted
$\delta_0^{>}=\delta_3^{>}=1$.

This refutes any assertion that this particular canonical integer has a large factorial-cubed small-prime part **at $3375$**. It neither refutes an asymptotic $O(n)$-error smoothness estimate nor excludes a favorable infinite subsequence. The complete producer and old denominator extraction were not rerun.

## 3.3 A second product-ideal element

Use the canonical integral reference values


$$
\widehat h=2^{m/2}\tau_n,\qquad
\widehat\ell=2^{m/2}\tau_{n+1}.
$$


For the actual primitive contact rows $r_0,r_3$, define


$$
\boxed{
\widehat R_j
=\frac m2\left(
\widehat h\,r_jv'
+\widehat\ell\,r_jw'
\right)
=\frac{2^{m/2}}{n!}R_j\in\mathbb Z.
}
\tag{3.3}
$$


Then


$$
\boxed{\mathcal T_n=\widehat R_0\widehat R_3}
\tag{3.4}
$$


is a second element of the localized product ideal
$(R_0,C_0)(R_3,C_3)$.

Unlike $\Theta_n$, this element uses only the reference column and the actual primitive contact rows. It contains no substituted or truncated residual force.

Define the reference-transverse content


$$
\boxed{
\mathcal K_{{\rm ref},n}
=
\gcd\!\left(
|F|,\,
|Q\widehat h-P\widehat\ell|
\right)_{>N}.
}
\tag{3.5}
$$


Finally put


$$
\boxed{
\mathcal G_n=\gcd(\mathcal W_n,|\mathcal T_n|).
}
\tag{3.6}
$$


The convention $\gcd(a,0)=a$ makes this definition valid even at a zero reference projection.

### Theorem 3.1 — Reference-intersection product certificate

Whenever $\Theta_n\ne0$,


$$
\boxed{
\delta_0^{>}\delta_3^{>}
\mid\mathcal G_n
\mid
\delta_0^{>}\delta_3^{>}\,
\mathcal K_{{\rm ref},n}^{\,2}.
}
\tag{3.7}
$$



In particular, away from the primes of $\mathcal K_{\rm ref}$,


$$
\boxed{
v_p(\mathcal G_n)=v_p(\delta_0^{>}\delta_3^{>}).
}
\tag{3.8}
$$



Thus intersecting the two certificates is exact outside an explicitly identified reference-content obstruction.

### Proof

Fix $p>N$. Scale the reference column by $2^{m/2}/n!$, which is a unit at $p$. In the coordinates $v',w',e_2$, the content of its projection transverse to $L$ is the content of the wedge $L\wedge\widehat{\mathbf H}$.

Since $(\widehat h,\widehat\ell)=\mathbb Z_p$, its valuation is


$$
k=\min\{v_p(F),v_p(Q\widehat h-P\widehat\ell)\}.
\tag{3.9}
$$



Choose transverse coordinates in which this reference projection is


$$
p^k\binom10.
$$


Write the full source matrix as


$$
B=
\begin{pmatrix}
p^k&u\\
0&v
\end{pmatrix}.
$$


Then


$$
v_p(v)=d-k,
$$


and deleting the factor $p^k$ from the first source column gives


$$
B'=
\begin{pmatrix}
1&u\\
0&v
\end{pmatrix}.
$$



Write the primitive observation rows as $(a_j,b_j)$, and set


$$
t_j=v_p(a_j),\qquad d'=d-k.
$$


For the product with $B'$,


$$
e'_j=\min\{v_p(a_j),v_p(ua_j+vb_j)\}
=\min(t_j,d').
\tag{3.10}
$$


Indeed, if $t_j>0$, row primitivity makes $b_j$ a unit; if $t_j=0$, the equality is immediate.

The determinant depth $s$ of the observation matrix implies:

- if $t_0\ne t_3$, then $\min(t_0,t_3)=s$;
- if $t_0=t_3=t$, then $t\le s$.

These two cases give


$$
e'_0+e'_3
=\min\!\left(d'+\min(s,d'),\,t_0+t_3\right).
\tag{3.11}
$$



For the original source,


$$
e'_j\le e_j\le e'_j+k.
$$


A3’s certificate has depth


$$
w=d+\min(s,d-2b),
$$


while the corresponding certificate for $B'$ has depth


$$
w'=d-k+\min(s,d-k).
$$


Since $b\le k$,


$$
w-w'
=k+\min(s,d-2b)-\min(s,d-k)
\le2k.
\tag{3.12}
$$



The reference product has depth


$$
v_p(\mathcal T_n)=2k+t_0+t_3.
$$


Therefore


$$
\begin{aligned}
v_p(\mathcal G_n)
&=\min(w,2k+t_0+t_3)\\
&\le2k+\min(w',t_0+t_3)\\
&=2k+e'_0+e'_3\\
&\le2k+e_0+e_3.
\end{aligned}
$$


Conversely, the actual endpoint product divides both $\mathcal W_n$ and $\mathcal T_n$, so


$$
e_0+e_3\le v_p(\mathcal G_n).
$$


This proves (3.7) prime by prime. ∎

## 3.4 Advancement of the exclusive-product target

The new certificate gives


$$
\mathfrak D_0\mathfrak D_3
\mid\Pi_0(n)\Pi_3(n)\mathcal G_n,
\tag{3.13}
$$


and


$$
E_{0,n}E_{3,n}
\mid
\frac{\mathcal G_n}{g_n^2}.
$$


Combining with A3,


$$
\boxed{
E_{0,n}E_{3,n}
\mid
\gcd\!\left(
\frac{\mathcal A_n}{\gcd(\mathcal A_n,\Sigma_n)},
\frac{\mathcal G_n}{g_n^2}
\right).
}
\tag{3.14}
$$



A version not requiring the actual $g_n$ is


$$
E_{0,n}E_{3,n}
\mid
\gcd\!\left(
\frac{\mathcal A_n}{\gcd(\mathcal A_n,\Sigma_n)},
\frac{\mathcal G_n}{\mathcal B_n^2}
\right).
\tag{3.15}
$$



This is a genuine alternative to demanding smoothness of all of $\Theta_n$. A sufficient new arithmetic target is


$$
\boxed{
\log\mathcal G_n-2\log\mathcal B_n=o(n\log n)
}
\tag{3.16}
$$


on an infinite original subsequence, or the stronger $O(n)$ estimate.

The theorem does not prove that estimate. Its advance is an exact, force-sensitive intersection certificate whose excess is confined to the explicit reference content (3.5).

At $3375$, the accepted endpoint product $1$ gives the new checkable restriction


$$
\boxed{\mathcal G_{3375}\mid\mathcal K_{{\rm ref},3375}^{\,2}.}
\tag{3.17}
$$


No numerical value of these two new fields is asserted here.

---

# 4. Ternary endpoint audit and the paid modulo-$27$ transition

## 4.1 The modulo-$9$ killing theorem retains the inherited carry

A1’s suffix calculation places the characteristic-three pair in


$$
(-\iota(R),\iota(R)).
$$


Before the first absorbing $2$, the nonzero states remain signed copies of $R$ or $P$. At that $2$, both actual modulo-$9$ states become divisible by $3$, with quotient containing both:

- the inherited suffix/middle carry;
- the newly injected paid correction.

The subsequent $0202$ operator annihilates every element of the full seventeen-coordinate divided module. Its proof uses the two-digit return


$$
Z\longmapsto bK,\qquad \deg K\le2,
$$


followed by


$$
bK\longmapsto P(k_0-k_1u)\longmapsto0.
$$


No inherited direction is omitted.

Thus


$$
20202\subset M\Longrightarrow X_m\equiv Y_m\equiv0\pmod9
$$


is proved, and the exact-window progression supplies a positive-density original family with $c_m\ge2$.

The new value


$$
j_*=84645\pmod{531441}
$$


is an accepted finite resolution of the already proved discrete-log specification. It requires no repetition.

## 4.2 Derivation of the modulo-$27$ correction terms

Write


$$
a=1+u,\qquad b=1-u,\qquad Q=1-u^2,
$$


and use the endpoint residue representation with


$$
\sigma(u)=\sqrt{Q(u)},\qquad x(u)=\frac{u\,a(u)^3}{b(u)}.
$$



Since $Q(u^3)/Q(u)^3\equiv1\bmod3$,


$$
\left(\frac{Q(u^3)}{Q(u)^3}\right)^{9/2}\equiv1\pmod{27},
$$


and hence


$$
\boxed{
\sigma(u)\equiv
\sigma(u^3)\frac{Q(u^3)^4}{Q(u)^{13}}
\pmod{27}.
}
\tag{4.1}
$$



Also,


$$
a(u^3)=a(u)^3-3ua(u),\qquad
b(u^3)=b(u)^3+3ub(u).
$$


It follows that


$$
\frac{x(u^3)}{x(u)^3}
\equiv
1-\frac{3u}{b^2}
+\frac{9u^2}{b^4}
-\frac{9u}{a^2}
\pmod{27},
$$


and therefore


$$
\boxed{
\left(\frac{x(u^3)}{x(u)^3}\right)^q
\equiv
1-\frac{3qu}{b^2}
+9\binom{q+1}{2}\frac{u^2}{b^4}
-\frac{9qu}{a^2}
\pmod{27}.
}
\tag{4.2}
$$



These are precisely the four terms in the coordinator implementation.

For $m=3q+r$, padding the resulting denominator to $Q^{54}$, sectioning, and restoring the $Q^{26}$ normalization gives multipliers


$$
a^{15-3r}b^{15+r},\quad
a^{15-3r}b^{13+r},\quad
a^{15-3r}b^{11+r},\quad
a^{13-3r}b^{15+r},
$$


with shifts


$$
-r,\quad1-r,\quad2-r,\quad1-r
$$


and weights


$$
1,\quad-3q,\quad9\binom{q+1}{2},\quad-9q.
$$


Thus the construction is correct.

The lookahead must be $q\bmod9$: the first correction depends on that residue, while the two $9$-weighted corrections depend only on $q\bmod3$. The code supplies exactly the next two ternary digits.

For degree at most $52$, sectioning and multiplication by $Q^{12}$ give degree at most $51$. Negative shifted exponents cannot survive the section: their only possible negative values are $-1,-2$, not negative multiples of $3$. This supplies a symbolic degree proof behind the 1431 basis checks.

## 4.3 Scope of the new zeros

The receipt establishes:

- 80 new characteristic-zero endpoint comparisons at $181\le m\le220$;
- 1431 finite basis/transition checks;
- zero modulo $27$ for the 40 specified words $H20202$, $|H|\le3$.

It does not establish that the entire reachable module after $20202$ is killed modulo $27$. Nor does it evaluate the middle word of an eligible original power.

A1 is already pursuing that universal proof or counterexample. I do not duplicate it.

## 4.4 Same-parameter Jacobi and determinant-four loss

The exact identities remain


$$
X_m=J_m^{[2m-1]}(-1),\qquad
Y_m=J_{m-1}^{[2m-1]}(-1).
$$


The adjacent polynomial retains the same parameter $2m-1$.

On the stated integral scalar branch,


$$
Z_{\rm src}(-1)=\lambda_mX_m+\mu_mY_m,
$$


where $\lambda_m$ is a $3$-adic unit and $v_3(\mu_m)=4$. Hence


$$
\min\{v_3(X_m),v_3(Z_{\rm src}(-1))\}
=c_m+\min\{v_3(\bar X_m),4\}.
$$


Recovering the original normalized second endpoint pays the four-digit division. A modulo-$27$ endpoint zero neither removes that loss nor proves a full polynomial-content statement.

---

# 5. The recovered $29$-adic head closes $\mathbf H$

Here


$$
p=29,\qquad
b=3^{249005515+574312172u},\qquad
n=2001b.
$$


The original contact, source, and reconstruction ranges remain respectively


$$
0\le j<b,\qquad1\le i\le b-2,\qquad0\le j\le b.
$$



## 5.1 Identification in the correct integral coordinates

Because $p\mid n$,


$$
(1+2t+2t^2)^n
\equiv(1+2t^p+2t^{2p})^{n/p}\pmod p.
$$


For $0\le i<p$, only the constant term of $(1+t)^i$ can contribute to the coefficient of $t^n$. Thus


$$
J_i\equiv J_0\pmod p.
$$


Also,


$$
\frac{(n+i)!}{n!}\equiv i!\pmod p.
$$


For $i\ge p$, the same integral product contains $n+p$, so it is divisible by $p$.

Therefore


$$
\boxed{
f_i^0\equiv
\begin{cases}
J_0i!&0\le i<29,\\
0&i\ge29
\end{cases}
\pmod{29}.
}
\tag{5.1}
$$



This is the actual head before $\mathsf P_-$ is applied. Thus


$$
f^0=J_0h^{[0]}+29h^{[1]}
$$


with integral remainder in the same coordinates. The integral finite normal form preserves the explicit factor $29$.

No unit assumption on $J_0$ is needed.

This closes $\mathbf H$; it is not an inference from the norm identity $\eta=A_0^2\kappa$.

## 5.2 Audit of the physical proof after closing $\mathbf H$

A2’s argument then applies to every retained shift


$$
0\le a\le523,\qquad -350\le v\le346.
$$



- The shifts do not cross the three-digit low boundary.
- Physical positions $3,4,5$ retain the all-interface two-event certificate.
- At position $7$, the triple $(8,25,17)$ forces an additional event for every incoming interface.
- Every coefficient-$29$ correction therefore has depth at least $4$.
- The coefficient-unit short-head terms have their additional event in positions $0,1$, also giving depth at least $4$.

The finite return remains the actual integral return with $G\in29M(\mathbb Z_{29})$. Its first-order contribution is included, not set to zero.

For the normalized $29^4$-layer, all active low pieces enter the common upper block with zero interface. Integral row factors have bounded binomial indices below $29^3$, so their residues depend only on the low three digits. All first-order head, lower, and return coefficients therefore enter the finite low scalar $\mathscr L$.

The upper contraction is


$$
12\left[
10\sum_{q=0}^{C}(F_{\rm I}/29)^2+
19\sum_{q=0}^{C}(F_{\rm II}/29)^2
\right].
$$


The branchwise first-moment reflection gives


$$
2(T_1/29^2)=7(T_0/29^2)\pmod{29},
$$


which annihilates this combination.

The actual endpoint is not silently added: $U(B)/29^3=0\bmod29$ proves that the two different final low-block ranges give the same contraction.

Finally, the original terminal weight has six forced borrows, so


$$
v_{29}(W_b)\ge6.
$$


Its restored terminal square is therefore zero at the required layer for a proved phase-specific reason.

### Unconditional conclusion



$$
\boxed{
u\equiv2\pmod{24389}
\Longrightarrow
Z_w\in29^4\mathbb Z_{29}^{\,b+1},
\qquad
Z_w^TZ_w\in29^9\mathbb Z_{29}.
}
\tag{5.2}
$$


In A2’s notation, $c\ge2,d\ge9$ are now unconditional.

The new tail receipt—42 paid contributions, 135918 exact auxiliary atoms, and actual $u=2$ tail annihilation after six digits—is compatible with this conclusion. It does not supply the physical-column argument and does not establish exact content.

## 5.3 A useful precision correction for the next layer

There is no need to assume in advance that $c=2$ merely to **test** the raw norm digit at depth $9$.

If the complete column is known modulo $29^6$, and (5.2) is known, then


$$
Z_w=29^4z_1+29^5z_2+O(29^6)
$$


gives


$$
\boxed{
\frac{Z_w^TZ_w}{29^8}
\equiv z_1^Tz_1+2\cdot29\,z_1^Tz_2
\pmod{29^2}.
}
\tag{5.3}
$$


The omitted coordinate error contributes first at depth $10$.

Thus a nonzero $29^9$-digit would simultaneously prove:

- exact raw norm depth $d=9$;
- exact coordinate content $29^4$, hence $c=2$;
- one extra primitive norm-cancellation digit.

A zero would prove only $d\ge10$. The $z_2$ terms must include the full second-lower, crossed-return, higher-head, and endpoint contributions.

This is a new physical precision statement, not a request to rerun the accepted tail controls.

---

# 6. The recovered binary final bridge changes the denominator interpretation

## 6.1 Coordinate identification, not inference from a norm equality

Let the current raw columns be


$$
a=\frac{Z_w}{R},\qquad b_{\rm raw}=\frac{V_w}{b!},
$$


and write


$$
D_{\rm raw}=a^Ta,\qquad E_{\rm raw}=a^Tb_{\rm raw}.
$$


The older normalized columns are exactly


$$
X=\frac a2=\frac{Z_w}{2R},\qquad
Y=\frac{b_{\rm raw}}4=\frac{V_w}{4b!}.
$$


Thus


$$
N=X^TX=\frac{D_{\rm raw}}4,\qquad
H=X^TY=\frac{E_{\rm raw}}8.
$$



The first equality follows from the actual normalized head and linear reconstruction. The second follows from the retained complete second-force/factorial-subtraction identity, including the exterior term. Neither is inferred solely from $D_{\rm raw}=4N$.

The contact excerpt gives


$$
\operatorname{diag}(\omega)u=\lambda Z_w,\qquad
\operatorname{diag}(\omega)v=V_w,
$$


with the prescribed


$$
\Omega=\operatorname{diag}(\omega_j^2).
$$


Therefore


$$
A_B=d_B^2\lambda^2R^2D_{\rm raw},
\qquad
H_B=d_B^2\lambda Rb!E_{\rm raw}.
\tag{6.1}
$$



The earlier packet-relative caution about absent definitions was legitimate as a description of that packet. These definitions are not globally missing after the documentary recovery.

Any additional row-content operation requires its exact compensating metric identity. The prescribed $u,v,\Omega$ cannot be replaced by independently rescaled rows with the metric left unchanged.

## 6.2 Actual all-prime denominator

Set


$$
\xi_n=\frac{2b!}{\lambda R}.
$$


Then


$$
\frac{p_n}{q_n}
=\xi_n\frac{H}{N}
=\xi_n\frac{E_{\rm raw}}{2D_{\rm raw}},
$$


and for every prime $\ell$,


$$
\boxed{
v_\ell(q_n)
=\max\!\left\{
v_\ell(D_{\rm raw})-v_\ell(E_{\rm raw})
+v_\ell(\lambda R)-v_\ell(b!),\,0
\right\}.
}
\tag{6.2}
$$


This formula is valid for rational raw forms using their exact valuations. An integer gcd of raw forms would first require a specified integral clearer; the actual integer gcd is $g_B=\gcd(A_B,|H_B|)$.

In particular,


$$
v_2(\xi_n)
=1+v_2(b!)-\frac{3n}{2}+s_2(n)
=-C_n,
$$


where


$$
\boxed{
C_n=\frac{3n}{2}-1-v_2(b!)-s_2(n).
}
\tag{6.3}
$$



At $b_0$, and at any separated original index satisfying A5’s exact-ratio guard $t-c\le6$,


$$
v_2\!\left(\frac{E_{\rm raw}}{2D_{\rm raw}}\right)=0.
$$


Consequently,


$$
\boxed{v_2(q_n)=C_n.}
\tag{6.4}
$$



For $n=4002b$,


$$
C_n=6002b-1+s_2(b)-s_2(2001b)>0.
$$


Thus raw binary cancellation does not make the actual primitive denominator odd. The factorial/central normalization restores a very large binary denominator.

All odd-prime contributions in (6.2) remain to be controlled.

## 6.3 A new actual Gram relation and its precision bill

A5’s undivided relative congruence is


$$
E_{\rm raw}-98D_{\rm raw}\in2^{41+c}\mathbb Z_2
\qquad(c\le22).
$$


Combining it with the exact final bridge gives the actual relation


$$
\boxed{
\lambda R\,H_B-98b!\,A_B
=d_B^2\lambda^2R^2b!
\bigl(E_{\rm raw}-98D_{\rm raw}\bigr).
}
\tag{6.5}
$$


This retains the actual clearer and both actual Gram forms.

After division by $2D_{\rm raw}$, the available raw-ratio precision is only


$$
7+c-t.
$$


Multiplication by $\xi_n$, whose valuation is $-C_n$, changes the center precision to


$$
\boxed{7+c-t-C_n.}
\tag{6.6}
$$


This is the appropriate cross-route precision correction. Neither high-norm cancellation nor a raw unit ratio can be transported to the final center without paying both losses.

---

# 7. Preserved constructions and the whole-error obligation

None of the audits or new certificates changes the original finite constructions.

- **Binary route:** both complete corrected columns, both finite returns, both Laurent branches, the inclusive $j=b$ endpoint, and the exterior $-bg_0-1$ remain.
- **$29$-adic route:** the second-force identity remains
  

$$
29^3U_a^TQ
  =29^3(r_0G^{(3)}_{a0}+r_1G^{(3)}_{a1})
  +\sum_{\ell=1}^{b-2}\mathcal H_\ell\lambda'_{a,\ell}
  +W_bU_{a,b}.
$$


  Both initial charges and every complete source row are retained. There is no source row at $b-1$, and the exterior at $b$ is not an extra recurrence step.
- **Ternary matrix route:** the original $0\le v\le2n-2$ cutoff, both Schur-corrected columns, the complete pole/factorial/LOW forcing, the unpaired boundary terms, and $\omega_{\nu-1}$ remain. No moment beyond $D-4$ is introduced.
- **A3 endpoint route:** the original $3\times3$ contact matrix, force cutoff $2n+2$, complete logarithmic companion, exterior $+1$, all eight reconstruction entries, and actual reconstruction row contents remain. At $3375$, those contents are still
  

$$
(113940000,\ 9780750,\ 10125,\ 1).
$$



For the Gram routes, the final pair is still


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\quad p_n=H_B/g_B,
$$


with gcd over **all primes**, and


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
\tag{7.1}
$$



For the ternary determinant route,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
$$


and


$$
\boxed{
q(e+\pi)-p
=\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{g_\ell}
\det H_{\rm complete}.
}
\tag{7.2}
$$



For A3’s weighted endpoint route, all factors
$F_{\rm gcd},G_{\rm wt},H_{\rm gcd},h_{\rm end}$ remain in the actual $q_\lambda,p_\lambda$, and the whole error is still


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=q_\lambda e_3\alpha_{n,2}(\lambda-\Lambda_{n,2}).
}
\tag{7.3}
$$



The local results above do not evaluate these whole errors or prove their nonvanishing on an infinite family.

---

# 8. New bounded arithmetic and final proof status

## 8.1 No completed control should be repeated

No repetition is needed of:

- the $u_0$ binary producer, witness, block, or Gram computations;
- the 64 high-counter sums or 32 depth-one tests;
- the 1431 modulo-$27$ basis checks, 80 direct coefficients, or 40 word tests;
- the $j_*=84645$ lift;
- the 42 paid $29$-adic contributions, auxiliary sums, or six-digit original tail annihilation;
- the $3375$ producer, endpoint gcds, denominator extraction, whole forms, or canonical $\Theta$ split.

The proofs in this report require no further finite execution.

## 8.2 A genuinely new archived-data calculation

To assess the new product certificate, a useful new postprocessing is:

### Inputs

From the already retained $3375$ artifact:

- $P,Q,F,\widehat h,\widehat\ell$;
- the actual primitive rows $r_0,r_3$;
- $v',w'$;
- the already computed $\mathcal W=D^{>}$;
- the prime list through $3377$.

### New outputs

Compute


$$
\widehat R_j
=\frac m2(\widehat h\,r_jv'+\widehat\ell\,r_jw'),
$$




$$
\mathcal K_{\rm ref}
=\gcd(F,Q\widehat h-P\widehat\ell)_{>3377},
$$




$$
\mathcal G=\gcd(D^{>},\widehat R_0\widehat R_3).
$$



The expected verifiable certificates are:

1. integrality of both $\widehat R_j$;
2. the exact reference-scaling identities;
3. the exact values and bit lengths of $\mathcal K_{\rm ref}$ and $\mathcal G$;
4. the zero remainder
   

$$
\boxed{\mathcal K_{\rm ref}^{\,2}\bmod\mathcal G=0;}
$$


5. if $\mathcal K_{\rm ref}=1$, the forced conclusion $\mathcal G=1$.

The numerical values of these new fields are **unevaluated specifications**, not anticipated receipts. This calculation would not recompute the old endpoint gcds.

## 8.3 Status ledger

| Claim | Status after this audit |
|---|---|
| Binary operator guard $39$, downstream guard $40$ | Proved at the supplied integral precision-$32$ scope |
| Positive-order normalized binary first head | Explicitly derived in (1.1)–(1.4) |
| Complete-original separator transfer | Proved using the retained complete-producer identities |
| Infinite original $h\equiv3\bmod4$ depth lower bounds | Proved |
| Infinitely many original exact depth-one high blocks | Open |
| Eight-state minimum/count implementation | Audited; finite receipt accepted |
| A3 Smith/product/exclusive divisibilities | Valid |
| Canonical $3375$ split | Exact finite fact |
| New reference-intersection product certificate | **Proved** |
| Small-height bound for that new certificate | Open |
| A1 universal modulo-$9$ killing word | Valid |
| Modulo-$27$ transition construction | Derived and valid |
| Universal modulo-$27$ killing or original primitive direction | Open |
| A2 actual-head interface $\mathbf H$ | **Closed** |
| Original $u\equiv2\bmod24389$: $c\ge2,d\ge9$ | **Unconditional** |
| Exact $29$-adic content and next nonzero norm layer | Open |
| Binary final $u,v,\Omega$ bridge | Recovered and identified |
| Binary exponent of actual $q_n$ in the exact-ratio range | **$C_n$, as in (6.4)** |
| All-prime denominator bound and whole nonzero error comparison | Open |
| Irrationality or rationality of $e+\pi$ | Unresolved |

---

## Conclusion

The principal new product result is


$$
\boxed{
\delta_0^{>}\delta_3^{>}
\mid
\gcd\!\left(
\mathcal W_n,\widehat R_0\widehat R_3
\right)
\mid
\delta_0^{>}\delta_3^{>}\mathcal K_{{\rm ref},n}^{\,2}.
}
$$


It replaces an undifferentiated smoothness demand on the large canonical scalar by an explicit intersection problem, exact outside a computable reference-content obstruction.

The recovered $29$-adic head also closes a genuine outstanding interface:


$$
\boxed{
u\equiv2\pmod{24389}
\Longrightarrow c\ge2,\quad d\ge9
}
$$


for the complete physical first column and its complete norm.

Finally, the recovered binary bridge shows why raw cancellation is not the final denominator calculation:


$$
\boxed{
v_2(q_n)=C_n
}
$$


where the exact raw-ratio hypotheses hold.

The remaining bottleneck is precise: obtain a sufficiently small **actual all-prime primitive denominator**, including every content, clearer, collision, and final gcd factor, and compare it with the **whole nonzero error at the same original index** on an infinite original sequence.

No argument supplied or proved here establishes that comparison. The irrationality of $e+\pi$ therefore remains unresolved.
