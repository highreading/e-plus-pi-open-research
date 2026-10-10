> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4, Turn 12 — Audited projection ideals, a stronger infinite-family denominator law, and the exact scope of the ternary and $29$-adic reductions

## Executive conclusions

The new coordinator receipts corroborate the three source reports at their stated finite scopes. They do not supply the missing infinite residual-content estimate or evaluate a new original-index whole error.

After an independent algebraic audit, I accept the following.

1. **A3’s four endpoint equations, twelve integral projection identities, and exact local projected ideal are correct.** The polynomial projection losses
   

$$
\Pi_3=n^2+4n+1,\qquad \Pi_0=n^2+6n+4
$$


   are justified at
   

$$
p>n+2,\qquad p\nmid G_j.
$$


   Their use involves neither division by the contact determinant nor cancellation of a nonunit normalization factor.

2. **The new $3375$ postprocessing has the advertised meaning.** It retains the complete exponential seed subtraction, logarithmic force, and terminal normal relation. The reported values are
   

$$
\boxed{\mathfrak D_0=\mathfrak D_3=1,}
$$


   and both normal-coefficient large-prime gcds excluding $G_j$ are $1$. These are finite results at $3375$, not an infinite $O(n)$ content estimate.

3. **A3’s actual binary denominator theorem is valid, and its infinite scope can be enlarged.** I prove below that
   

$$
\boxed{
   v_2(d_0)=v_2(n!)+\frac{n-3}{2},\qquad
   v_2(d_3)=v_2(n!)+\frac{n-7}{2}
   }
   \tag{A}
$$


   holds on
   

$$
\boxed{n=15^{2a}\quad\text{or}\quad n=105^{2a},\qquad a\ge1.}
   \tag{B}
$$


   Thus $105^{4a}$ can be replaced by $105^{2a}$. The additional class is $n\equiv17\pmod{32}$. This is a theorem about the **actual primitive endpoint denominators**, with the complete residual restored.

4. **The polynomial projection loss admits a sharper reference-sensitive bound.** Define
   

$$
L_3=h-(n+2)\ell,
$$


   

$$
L_0=(n+3)h-(n^2+5n+3)\ell,
$$


   and
   

$$
B_j=\gcd\!\left(\Pi_j,|L_j|\right)_{>n+2}.
$$


   Then
   

$$
\boxed{
   \gcd(R_j,C_j)_{>n+2}
   \mid\mathfrak D_j
   \mid B_j\,\gcd(R_j,C_j)_{>n+2}.
   }
   \tag{C}
$$


   Moreover,
   

$$
\boxed{\gcd(B_0,B_3)=1.}
   \tag{D}
$$


   This is an all-large-prime strengthening of A3’s projection comparison. It still does not bound the actual residual content.

5. **A1’s seven-dimensional characteristic-three realization and five-state language evaluation are correct.** The actual generating-function normalization, intrinsic Cartier operation, suffix orientation, and shifted index $m-1$ all survive audit. The coordinator’s $160$ direct coefficients and $3280$ words are corroboration, not the reason the all-word theorem holds.

6. **A genuine original real-window density consequence follows from the accepted Lagarias theorem.** On the original progression, with the stated real window and suffix $m\equiv851\pmod{6561}$, the eligible indices have positive density. Among them, the indices with a nonzero endpoint pair modulo $3$ have density zero. This does **not** classify individual powers, prove eventual omission exclusion, or evaluate the first nonzero primitive $3$-adic layer.

7. **A2’s complete two-unit-digit interface and three-observable row are correct.** In particular,
   

$$
\boxed{
   \kappa
   =21D(C)+16S_2(C)
   +(25+18C+19C^2+24C^3)S_0(C)\pmod{29}.
   }
   \tag{E}
$$


   The ordinary carry in $\lambda_{\mathrm I}+\lambda_{\mathrm{II}}$, both finite cutoff branches, and the zero-flux endpoints are essential and are present. The new sparse receipt verifies the three auxiliary values only:
   

$$
\boxed{754,\ 261,\ 290\pmod{841},\qquad
   \kappa=26,\ 9,\ 10.}
$$



No code was executed for this report. No accepted bounded computation is requested again.

The irrationality or rationality of $e+\pi$ remains unresolved.

---

# I. Audit conventions and retained boundaries

The three constructions have different index domains and must not be merged.

### Endpoint construction



$$
n=15^r\quad\text{or}\quad n=105^r,\qquad r\ge2.
$$



The original $3\times3$ contact matrix, force through $2n+2$, terminal return, both corrected four-coordinate columns, exterior $+1$, least eight-entry clearer, actual row contents, endpoint primitive rows, and all-prime weighted gcd remain unchanged.

### Characteristic-three construction



$$
j>0,\qquad j\equiv81\pmod{243},\qquad m=2^{2j-1},
$$


with the original real window. Additional content and unit hypotheses required by the normalized scalar comparison are not inferred from the new automaton or density argument.

### $29$-adic construction



$$
b=3^{249005515+574312172u},\qquad n=2001b,\qquad u\ge0,
$$


with


$$
0\le j<b,\qquad 1\le i\le b-2,\qquad 0\le j\le b
$$


for contact coordinates, source rows, and reconstructed coordinates, respectively.

The accepted complete reduction


$$
\eta=A_0^2\kappa
$$


is reused. In particular, none of the already closed head, first-lower, crossed-return, or second-return radical terms is reopened.

The retained binary computation from Turn 11 is also unchanged:


$$
v_2(D_{\rm raw})=33,\qquad v_2(E_{\rm raw})=34,
$$




$$
\nu_2=15,\qquad
\frac{E_{\rm raw}}{2D_{\rm raw}}\equiv49\pmod{128},
$$


and the full normalized cross-block depth is $11$. No further execution of that pipeline is needed here.

---

# II. Priority 1: the moment–reference reduction

## 1. The endpoint equations are correctly evaluated

Use A3’s notation


$$
m=n+1,\qquad N=n+2,
$$




$$
A=a_n,\quad B=a_{n-1},\quad D=a_{n+1},
$$




$$
X=mA,\qquad Y=mnB,\qquad Z=2D-mA.
$$



For an actual primitive endpoint row $r_j=(x_j,y_j,z_j)$, put


$$
\alpha_j=r_jv',\qquad \beta_j=r_jw',
$$


where


$$
v'=(2N,N,m)^T,\qquad w'=(0,N,2n+3)^T.
$$



The elementary row identity is


$$
\boxed{
2Nr_j=(\alpha_j-\beta_j,\,2\beta_j,\,0)+z_jq_\partial,
}
\tag{2.1}
$$


with


$$
q_\partial=(N,-2(2n+3),2N).
$$


This identity is exact over the integers.

Applying it to an annihilated contact column $J_i$, and dividing by the displayed common factor $N$, gives


$$
P_i\alpha_j+Q_i\beta_j+F_i z_j=0.
$$



For endpoint $3$, the annihilated columns are $J_0,J_1$. For endpoint $0$, they are


$$
nJ_0+J_1,\qquad -nmJ_0+J_2.
$$



The resulting coefficients are exactly


$$
\begin{array}{c|c|c|c}
(j,i)&P_{j,i}&Q_{j,i}&F_{j,i}\\ \hline
(3,0)&X&Z&Y-X-(2n+1)Z\\
(3,1)&Y&2X-Y&NY-(3n+4)X+NZ\\
(0,0)&nX+Y&nZ+2X-Y&
2m(Y-2X-(n-1)Z)\\
(0,1)&mZ-(n^2+1)X-(n-1)Y&
mY-(n-1)X-m^2Z&
2m(mX-NY+(n^2+n+1)Z).
\end{array}
\tag{2.2}
$$



There is a useful internal consistency check:


$$
(P_{0,0},Q_{0,0},F_{0,0})
=n(P_{3,0},Q_{3,0},F_{3,0})
 +(P_{3,1},Q_{3,1},F_{3,1}).
\tag{2.3}
$$


In particular,


$$
nF_{3,0}+F_{3,1}
=2m(Y-2X-(n-1)Z).
$$



The last row uses the terminal moment recurrence to eliminate $a_{n-2}$; it is not obtained by inverting the contact determinant. For example, its first two entries follow from


$$
P_2=mZ+(n-1)X-(n-1)Y,\qquad
Q_2=mY-(n-1)X-mZ
$$


and subtraction of $nm(P_{3,0},Q_{3,0})$.

**Verdict:** all four endpoint equations are valid for the actual endpoint kernels.

---

## 2. The reference-pair unit ideal can be checked independently

Put


$$
h=n!\tau_n,\qquad \ell=n!\tau_{n+1}.
$$



A3 invokes the retained Legendre companion result to conclude that $h,\ell$ generate the unit ideal for $p>n+2$. There is also a direct verification using the displayed constant-term reference sequence.

Its generating function is


$$
\sum_{k\ge0}\tau_k t^k=(1-2t-t^2)^{-1/2},
$$


so


$$
\boxed{
(k+1)\tau_{k+1}=(2k+1)\tau_k+k\tau_{k-1},
\qquad \tau_0=\tau_1=1.
}
\tag{2.4}
$$



At an odd prime $p>n+2$, every $\tau_k$ is $p$-integral, and $n!$ is a unit. If both $\tau_n,\tau_{n+1}$ vanished modulo $p$, recurrence (2.4), run backwards, would force


$$
\tau_{n-1}=\cdots=\tau_0=0\pmod p,
$$


because all the required integers $1,\ldots,n$ are units. This contradicts $\tau_0=1$.

Therefore


$$
\boxed{(h,\ell)=\mathbb Z_p\qquad(p>n+2).}
\tag{2.5}
$$



This is the unit-ideal fact needed in the local projection argument. It is **not** deduced from real nonvanishing of the complete Wronskian.

---

## 3. The complete residual and integral identities retain the forcing

The reference projection is


$$
\mathcal R_j=h\alpha_j+\ell\beta_j=\frac{2R_j}{m}.
\tag{2.6}
$$



Retain


$$
C_j=S_n\alpha_j+T_n\beta_j+mZz_j
\tag{2.7}
$$


and


$$
hT_n-\ell S_n=\mathscr K_n,
$$


where, at the original odd indices,


$$
\boxed{
\mathscr K_n=h_nb_{n+1}-h_{n+1}b_n-2(n!)^3.
}
\tag{2.8}
$$



The term $-2(n!)^3$ is the complete logarithmic contribution. The zero-seeded exponential residual is defined using


$$
b_s=u_s-E_nh_s-a_s,
$$


so the exponential seed and exterior subtraction have also been retained.

Define


$$
M_{j,i}=Q_{j,i}h-P_{j,i}\ell,
$$




$$
\mathcal D_{j,i}=mZ M_{j,i}-F_{j,i}\mathscr K_n.
\tag{2.9}
$$



With


$$
I_j=\beta_j\mathscr K_n+mhZz_j,\qquad
J_j=-\alpha_j\mathscr K_n+m\ell Zz_j,
$$


direct expansion gives


$$
\alpha_j\mathcal D_{j,i}
=mZQ_{j,i}\mathcal R_j+F_{j,i}J_j,
$$




$$
\beta_j\mathcal D_{j,i}
=-mZP_{j,i}\mathcal R_j-F_{j,i}I_j,
$$




$$
z_j\mathcal D_{j,i}=Q_{j,i}I_j-P_{j,i}J_j.
\tag{2.10}
$$



These are integral identities before localization. In particular, they do not silently divide out the $m$-factor from an earlier global identity.

---

## 4. The exact local ideal is correct

Fix


$$
p>n+2,\qquad p\nmid G_j,\qquad
G_j=\gcd(\alpha_j,\beta_j).
$$


Let


$$
r=v_p(R_j),\qquad c=v_p(C_j),\qquad
f=\min_i v_p(F_{j,i}).
$$



If $r=0$, the asserted minimum is zero. Otherwise choose $a,b\in\mathbb Z_p$ such that


$$
ah+b\ell=1,
$$


and put


$$
t_j=a\beta_j-b\alpha_j.
$$


Then


$$
\alpha_j=a\mathcal R_j-\ell t_j,\qquad
\beta_j=b\mathcal R_j+ht_j.
$$


Because $\mathcal R_j\in p\mathbb Z_p$ and $(\alpha_j,\beta_j)$ is primitive, $t_j$ is a unit.

Writing $V=aS_n+bT_n$, elimination gives


$$
t_j\mathcal D_{j,i}
=
\left(F_{j,i}V-mZ(aP_{j,i}+bQ_{j,i})\right)\mathcal R_j
-F_{j,i}C_j.
\tag{2.11}
$$


Both $t_j$ and $m/2$ are units at the stated scope. Hence


$$
\boxed{
(R_j,\mathcal D_{j,0},\mathcal D_{j,1})
=(R_j,F_{j,0}C_j,F_{j,1}C_j)
\quad\text{in }\mathbb Z_p.
}
\tag{2.12}
$$



Thus


$$
\boxed{
\min\{v_p(R_j),v_p(\mathcal D_{j,0}),v_p(\mathcal D_{j,1})\}
=\min\{r,c+f\}.
}
\tag{2.13}
$$



The restrictions $p>n+2$ and $p\nmid G_j$ are substantive. This is not an unrestricted all-prime identity.

---

## 5. Both polynomial projection bounds survive audit

The retained moment primitivity theorem gives


$$
\min\{v_p(X),v_p(Y),v_p(Z)\}=0
\qquad(p>n+2).
\tag{2.14}
$$



### Endpoint $3$

If $f>0$, the two equations $F_{3,i}=0\pmod{p^f}$ imply


$$
X\equiv NZ,\qquad Y\equiv3mZ\pmod{p^f}.
$$


Therefore $Z$ is a unit. Moreover,


$$
P_{3,0}Q_{3,1}-P_{3,1}Q_{3,0}
=2X^2-XY-YZ
\equiv-\Pi_3Z^2\pmod{p^f}.
$$


The two actual row equations and the unit ideal $(\alpha_3,\beta_3)$ force this determinant to vanish modulo $p^f$. Thus


$$
f\le v_p(\Pi_3).
$$



### Endpoint $0$

The two normal equations give


$$
Y\equiv2X+(n-1)Z,\qquad
(n+3)X\equiv3Z\pmod{p^f}.
$$



The division by $n+3$ is legitimate: original $n$ is odd, so $n+3$ is even, and every prime factor of $n+3$ is at most


$$
\frac{n+3}{2}<n+2.
$$


Hence


$$
X\equiv\frac{3Z}{n+3},\qquad
Y\equiv\frac{n^2+2n+3}{n+3}Z\pmod{p^f},
$$


with $Z$ a unit.

Substitution gives


$$
P_{0,0}Q_{0,1}-P_{0,1}Q_{0,0}
\equiv-\frac{n\Pi_0}{n+3}Z^2\pmod{p^f}.
$$


Again the determinant is divisible by $p^f$, and $n/(n+3)$ is a unit. Therefore


$$
f\le v_p(\Pi_0).
$$



**Verdict:** A3’s polynomial projection-cost theorem is proved at its claimed scope.

---

## 6. New theorem: a reference-sensitive projection bound

A3’s bound can be sharpened without introducing a contact determinant.

Define


$$
L_3=h-N\ell,
$$




$$
L_0=(n+3)h-(n^2+5n+3)\ell,
$$


and


$$
B_j=\gcd(\Pi_j,|L_j|)_{>n+2}.
$$



### Theorem 6.1

For the original endpoint construction,


$$
\boxed{
\delta_j^{>}\mid\mathfrak D_j\mid B_j\delta_j^{>},
\qquad
\delta_j^{>}=\gcd(R_j,C_j)_{>n+2}.
}
\tag{2.15}
$$



#### Proof

Work at a prime $p>n+2$, $p\nmid G_j$. Let


$$
e_p=\min(r,c+f)-\min(r,c)
$$


be the excess exponent introduced by projection. If $e_p=0$, there is nothing to prove.

Otherwise $r>c$ and $f>0$. Put


$$
k=\min(r,f).
$$


Then


$$
e_p\le k.
$$



Modulo $p^k$, both normal coefficients vanish and $\mathcal R_j=0$. Using the unit $t_j$ from §4, the transformed endpoint equations give


$$
M_{j,i}t_j\equiv0\pmod{p^k}.
$$


Hence


$$
M_{j,i}\equiv0\pmod{p^k}.
$$



For endpoint $3$, the normal equations give


$$
X\equiv NZ,\qquad Y\equiv3mZ,
$$


so


$$
M_{3,0}=Zh-X\ell\equiv Z(h-N\ell)=ZL_3\pmod{p^k}.
$$


Since $Z$ is a unit, $p^k\mid L_3$.

For endpoint $0$,


$$
Q_{0,0}\equiv Z,\qquad
P_{0,0}\equiv\frac{n^2+5n+3}{n+3}Z\pmod{p^k}.
$$


Consequently


$$
(n+3)M_{0,0}\equiv ZL_0\pmod{p^k},
$$


and $p^k\mid L_0$.

The polynomial theorem already gives $f\le v_p(\Pi_j)$. Therefore


$$
e_p\le\min\{v_p(\Pi_j),v_p(L_j)\}.
$$


Taking the product over all retained primes proves (2.15). The structural exclusion handles primes dividing $G_j$, which cannot divide $\delta_j^{>}$. ∎

### Joint-endpoint consequence

The identity


$$
4\Pi_3-(2n+3)(2n+5)=-11,
\qquad
\Pi_0-\Pi_3=2n+3
$$


shows


$$
\gcd(\Pi_0,\Pi_3)\mid11.
$$


All primes in $B_0,B_3$ exceed $n+2\ge227$. Hence


$$
\boxed{\gcd(B_0,B_3)=1.}
\tag{2.16}
$$



Thus the two endpoint projection excesses are coprime:


$$
\gcd\!\left(\frac{\mathfrak D_0}{\delta_0^{>}},
            \frac{\mathfrak D_3}{\delta_3^{>}}\right)=1.
\tag{2.17}
$$



This is a genuine joint-endpoint restriction. It concerns the **projection excesses**, not the actual contents $\delta_0^{>},\delta_3^{>}$; no coprimality of the latter has been proved.

---

## 7. Interpretation of the new $3375$ receipt

The coordinator source reconstructs


$$
a_s=s!\,\texttt{moment}_s,\qquad
u_s=s!\,\texttt{omega}_s
$$


from the retained artifact, forms the actual primitive contact rows, and uses


$$
C=U-E_nH+Q
$$


with the complete logarithmic $Q$.

Its prime extraction is not a selected-prime sample:

1. it removes every prime $p\le3377$ using a complete sieve;
2. for the projected quantities, it repeatedly removes $\gcd(\cdot,G_j)$, thereby removing every prime power supported on $G_j$;
3. it performs exact integer gcds on the remaining integers.

Thus the reported $\mathfrak D_j$ has precisely the all-large-prime scope in A3’s definition.

The new receipt establishes, at $n=3375$,


$$
\begin{array}{c|cc}
&j=0&j=3\\ \hline
\gcd(G_j,C_j)&6754&6754\\
\gcd(R_j,C_j)_{>3377}&1&1\\
\gcd(F_{j,0},F_{j,1})_{>3377,\ p\nmid G_j}&1&1\\
\mathfrak D_j&1&1.
\end{array}
$$



It also corroborates:

- four zero endpoint-equation residuals;
- twelve zero integral projection residuals;
- the complete terminal normal identity;
- the sign and stated real bounds for $\mathscr K_n$.

The proof of the infinite projection comparison is algebraic. The receipt corroborates it at this one original index. Neither the receipt nor the real Wronskian bound proves


$$
\log\mathfrak D_0+\log\mathfrak D_3=O(n).
$$



---

# III. Actual binary denominators: audit and enlarged infinite scope

## 8. A3’s original binary theorem is valid

Assume first


$$
n\equiv1\pmod8,
\qquad
t=v_2(n!),\qquad k=\frac{n-1}{2}.
$$



The actual primitive contact rows give


$$
v_2(G_0)=2,\qquad v_2(G_3)=0.
\tag{3.1}
$$



The constant-term reference analysis is also correct. For odd index $n=2k+1$, the terminal summand is uniquely of smallest valuation because the relative summands have valuation


$$
2v_2((k)_r)-r+s_2(r)>0\qquad(r\ge1).
$$


For the even index $n+1=2(k+1)$, the first two terminal-relative terms combine with multiplier


$$
1+(k+1)^2,
$$


of valuation exactly one, while all subsequent terms are deeper. Therefore


$$
v_2(\tau_n)=-v_2(k!),
$$




$$
v_2(\tau_{n+1})=-v_2(k!)+1.
\tag{3.2}
$$



The primitive reference coefficients at both endpoints are odd. Thus there is no cancellation between these two distinct depths, giving


$$
\boxed{v_2(R_0)=k+2,\qquad v_2(R_3)=k.}
\tag{3.3}
$$



The complete force calculation modulo $8$ proves


$$
v_2(r_jU)\ge3.
$$


Restoration of the seed and logarithmic force is valid:

- $v_2(E_nR_j)\ge k$;
- the retained logarithmic clearer gives
  

$$
v_2(r_jQ)\ge2t+v_2(G_j)-n-1-\lfloor\log_2(n+1)\rfloor>3
$$


  for every original $n\ge225$.

Hence


$$
v_2(C_j)\ge3.
\tag{3.4}
$$



At $n\equiv1\pmod{32}$, A3’s modulo-$16$ dot products are $8$, so $v_2(C_j)=3$. Its passage to the actual denominator uses the correct all-prime identity, not an unnormalized reference pair:


$$
d_j=
|R_j^*|\,
\frac{n!}{\gcd(n!,|E_nR_j^*+C_j^*|)}.
\tag{3.5}
$$



When $c=v_2(C_j)<r=v_2(R_j)$, $R_j^*$ is even and $C_j^*$ is odd. Therefore the gcd in (3.5) has no factor $2$, and


$$
v_2(d_j)=t+r-c.
\tag{3.6}
$$



This proves A3’s claimed theorem on $15^{2a}$ and $105^{4a}$.

---

## 9. New theorem: the missing class $n\equiv17\pmod{32}$

The same exact depth $3$ holds in the other class with $n\equiv1\pmod{16}$.

### Theorem 9.1

For every original index satisfying


$$
n\equiv1\pmod{16},
$$


one has


$$
\boxed{v_2(r_0U)=v_2(r_3U)=v_2(C_0)=v_2(C_3)=3.}
\tag{3.7}
$$



#### Proof

The class $n\equiv1\pmod{32}$ is already proved. Consider


$$
n\equiv17\pmod{32}.
$$



Parameter reduction modulo $16$ is to parameter $1$, and the valid index period modulo $16$ is $32$. At parameter $1$,


$$
a_s(1)=\frac{(s-1)(s-2)}2.
$$


Thus


$$
(a_{n-2},a_{n-1},a_n,a_{n+1},a_{n+2})
\equiv(11,9,8,8,9)\pmod{16}.
\tag{3.8}
$$



For the complete exponential-force coefficients,


$$
u_s(1)=\frac{s(s+1)}2E_{s-1}+2.
$$


The recurrence $E_r=rE_{r-1}+1$, with $E_0=1$, gives


$$
(E_{16},E_{17},E_{18})\equiv(1,2,5)\pmod{16}.
$$


Hence


$$
(u_n,u_{n+1},u_{n+2})
\equiv(11,8,8)\pmod{16}.
\tag{3.9}
$$



It follows that the complete exterior-corrected exponential vector is


$$
U=
\bigl(mN(u_n-a_n),\,N(u_{n+1}-a_{n+1}),\,u_{n+2}-a_{n+2}\bigr)
\equiv(2,0,15)\pmod{16}.
\tag{3.10}
$$



Substitution into A3’s exact normalized row formulas gives


$$
(X_0,Y_0,Z_0)\equiv(9,14,10)\pmod{16},
\tag{3.11}
$$


and


$$
\mathscr R_3/2\equiv(8,11,8)\pmod{16}.
\tag{3.12}
$$



The division by $2$ in (3.12) is paid before reduction. In the first coordinate, $D\equiv8\pmod{16}$ implies $D^2/2\equiv0\pmod{16}$; the other terms use the known unit $m/2\equiv9\pmod{16}$. Thus no extra bit has been silently assumed.

Now


$$
(9,14,10)\cdot(2,0,15)=168\equiv8\pmod{16},
$$




$$
(8,11,8)\cdot(2,0,15)=136\equiv8\pmod{16}.
\tag{3.13}
$$


The remaining primitive-row divisions are odd, so both dot products have exact valuation $3$.

Finally, the seed subtraction and logarithmic contribution are deeper than $3$, as in §8. Therefore the complete $C_j$ have the same exact valuation. ∎

### Corollary 9.2 — Enlarged actual-denominator family

Since


$$
15^2\equiv1\pmod{16},\qquad
105^2\equiv1\pmod{16},
$$


equations (3.3), (3.6), and (3.7) prove


$$
\boxed{
v_2(d_0)=t+k-1,\qquad v_2(d_3)=t+k-3
}
\tag{3.14}
$$


for


$$
\boxed{n=15^{2a}\quad\text{or}\quad n=105^{2a},\qquad a\ge1.}
\tag{3.15}
$$



In particular, if $h_{\rm end}=\gcd(d_0,d_3)$,


$$
\boxed{
v_2\!\left(\frac{d_0d_3}{h_{\rm end}^2}\right)=2.
}
\tag{3.16}
$$



This is an infinite-family theorem about the actual endpoint denominators. It does not determine their odd parts or the weight-dependent final gcd.

---

# IV. Priority 2: the characteristic-three observable

## 10. Actual normalization and coordinate-invariant residue extraction

The reduction from the characteristic-zero branch is consistent. With $t=1+u$,


$$
t^4-t^3+xt-2x=0
$$


becomes


$$
u(1+u)^3=x(1-u).
$$


Also


$$
d(1+u)=-3(1+u)^2+10(1+u)-6
\equiv1+u\pmod3.
$$


Thus the actual endpoint generating functions reduce to


$$
\mathcal A=\sigma,\qquad
\mathcal B=\sigma\frac{x}{(1+u)^2},
\qquad \sigma^2=1-u^2.
$$


They are not arbitrary choices of an algebraic branch.

Differentiation gives


$$
\frac{dx}{x}=\frac{du}{u(1-u)}.
\tag{4.1}
$$


Since $x=u+O(u^2)$, the change of local parameter preserves residues.

Cartier on differentials is intrinsic; its displayed coefficient formula in the separating coordinate $u$ is a coordinate expression of that operator. Consequently the proof does not assume that a coefficient-selection rule on functions is invariant under arbitrary substitutions. The invariant objects are the differentials


$$
\omega_H=\frac{\sigma H(u)}{u(1-u)^2(1+u)^4}\,du.
$$



Writing


$$
x^{-r}\omega_H
=\left(\frac{\sigma}{D_*}\right)^3 H K_r\,du
$$


gives exactly


$$
K_r=u^{2-r}(1-u)^{3+r}(1+u)^{7-3r}.
$$


Extraction of powers congruent to $2\pmod3$ proves the stated transitions.

The degree bounds


$$
\deg\Phi_0(H)\le5,\qquad
\deg\Phi_1(H)\le4,\qquad
\deg\Phi_2(H)\le3
$$


for $\deg H\le6$ establish the seven-dimensional invariant without appealing to a finite sample.

---

## 11. The suffix and five-state evaluation are correct

The suffix


$$
851=(01011112)_3
$$


is processed in the order


$$
2,1,1,1,1,0,1,0.
$$


The resulting operator is


$$
\mathcal F=\Phi_0\Phi_1\Phi_0\Phi_1^4\Phi_2,
$$


and the rank-one identity is


$$
\mathcal F(H)
=(h_5-h_4-h_3+h_1+h_0)R.
$$


The actual starting numerators yield


$$
(2R,R,R,R)
$$


for $(\mathcal A,\mathcal B,W,S)$.

The twenty-five leading ones produce


$$
L(H)=h_1-h_5.
$$



The five states


$$
0,\ R,\ -R,\ P,\ -P
$$


are closed under all three digits. The sign changes precisely when a processed $1$ is followed by a processed $0$, which is an occurrence of $01$ in the usual written middle word.

Therefore, for every finite $M$,


$$
\boxed{
(a_m,b_m)\equiv
\begin{cases}
(0,0),&M\text{ contains }2,\\
(-1)^{N_{01}(M)}(2,1),&M\in\{0,1\}^*.
\end{cases}
}
\tag{4.2}
$$



The shifted suffix for $m-1$ is different and is correctly retained:


$$
\mathcal F_-(H)=(h_4-h_2)R.
$$


It annihilates both actual state numerators modulo $3$. Hence


$$
V_{m-1}\equiv0\pmod3,
$$


without determining $V_{m-1}/3$.

The observation exponents $(-6,-4)$ explain why this is compatible with a nonzero endpoint pair. No primitive division of a characteristic-three zero state is justified.

### Receipt scope

The coordinator source verifies:

- $21$ transition identities on a basis;
- $7$ suffix, $7$ prefix, and $7$ shifted-suffix identities;
- the complete reachable five-state set;
- $160$ actual coefficient values at $61\le m\le140$;
- all $3280$ words of lengths $0,\ldots,7$.

The basis identities and reachable-state closure certify the finite linear realization. The direct coefficients corroborate its actual normalization at their finite indices. None of these computations classifies original powers.

---

## 12. New deduction: positive-density original windows, but density-zero nonzero mod-$3$ outputs

The supplied primary-literature gate records Lagarias’s theorem:

> For each fixed $\lambda>0$, the number of $k\le X$ for which the ternary expansion of $\lfloor\lambda2^k\rfloor$ omits $2$ is at most $25X^{0.9725}$, for sufficiently large $X$.

I use precisely that sublinear count.

### 12.1 The suffix selects a genuine original progression

Write


$$
j=81+243t.
$$


Modulo $6561$,


$$
2^{161}\equiv5225,\qquad
2^{486}\equiv5104=1+7\cdot729.
$$


Thus


$$
m=2^{2j-1}\equiv5225+8\cdot729\,t\pmod{6561}.
$$


The condition $m\equiv851\pmod{6561}$ is equivalent to


$$
t\equiv6\pmod9,
$$


or


$$
\boxed{j\equiv1539\pmod{2187}.}
\tag{4.3}
$$



This is a congruence condition on the original exponents, not a cylinder witness.

### 12.2 The real window has positive density on this progression

Let


$$
C=C_{16},\qquad
\Delta=
\log_3\!\left(\frac{1-\frac1{2C}}{1-\frac1C}\right)>0.
$$



For sufficiently large $j$, the real window is equivalent to


$$
\{\log_3(2^{2j}-1)\}
\in
\left(
1+\log_3(1-C^{-1}),
\ 1+\log_3(1-(2C)^{-1})
\right).
\tag{4.4}
$$


Now


$$
\log_3(2^{2j}-1)
=2j\log_3 2+\log_3(1-2^{-2j}),
$$


and the second term tends to zero exponentially.

On the progression (4.3), the rotation step is


$$
4374\log_3 2,
$$


which is irrational. Equidistribution therefore gives


$$
\boxed{
\#\{j\le J:\text{original progression, suffix, and real window}\}
=\frac{\Delta}{2187}J+o(J).
}
\tag{4.5}
$$



The small perturbation does not change this density: only points arbitrarily close to the two interval endpoints can change membership, and their limiting frequency tends to zero with the boundary neighborhood.

### 12.3 The leading ones are indeed forced

For $H=3^{h-1}$, write $\delta=D/H$. Then


$$
m=\frac{H(1-\delta)+1}{2}.
$$


The real window has


$$
0<\delta<\frac1{C_{16}}<3^{-25},
$$


because


$$
147968>3^{10}=59049.
$$


For all sufficiently large indices, this places $m$ inside the interval with twenty-five leading ternary ones. Thus the decomposition used by the automaton is valid.

### 12.4 Applying the sublinear omission count

Dropping the last eight digits gives


$$
\left\lfloor\frac m{3^8}\right\rfloor
=\left\lfloor3^{-8}2^{2j-1}\right\rfloor.
$$


Its ternary digits are the leading ones followed by $M$. It omits $2$ exactly when $M$ omits $2$.

Lagarias’s theorem with $\lambda=3^{-8}$ therefore bounds the number of nonzero cases in (4.2), among $j\le J$, by


$$
O(J^{0.9725})=o(J).
$$


Combining this with (4.5) proves:

### Theorem 12.1

Among original indices satisfying the prescribed progression, real window, and suffix, the proportion for which


$$
(a_m,b_m)\equiv(0,0)\pmod3
$$


tends to $1$.

Equivalently, the nonzero mod-$3$ endpoint cases have relative density zero in this positive-density original-window set.

This theorem does **not** assert:

- that there are only finitely many nonzero cases;
- that every sufficiently large original middle word contains $2$;
- a classification of individual original powers;
- the primitive endpoint pair in the zero-output case;
- positive density after imposing additional, presently unevaluated content or scalar-unit conditions from the normalized comparison.

The paid modulo-$9$ or higher lifting problem remains necessary.

---

# V. Priority 3: the whole $29$-adic carry

## 13. The two-unit-digit expansion accounts for the complete carry

The factorial-unit formula


$$
\mathcal F(29h+a)
\equiv(28!)^h a!(1+29hH_a)\pmod{841}
$$


is valid. Complete blocks have no first-order harmonic correction because


$$
H_{28}=0\pmod{29}.
$$



The fixed low support has $191268$ residues. Every supported low residue is below $\beta$, so the actual supported cutoff is exactly


$$
0\le q\le C.
$$


There is no completed final block.

At the six-digit interface the two high factors are correctly


$$
F_{\mathrm I}=(2X+C+1-q)V,\qquad
F_{\mathrm{II}}=(X-q)V.
$$



The digit-four correction is retained before contraction. Its affine dependence on $\ell$ is killed in the **sum of the two interface constants**, using


$$
\sum_{\ell=0}^{20}\binom{20}{\ell}^2
=\binom{40}{20},
$$




$$
\sum_{\ell=0}^{20}\ell\binom{20}{\ell}^2
=10\binom{40}{20},
$$


both divisible by $29$.

At digit five, the source keeps the genuine high-factor arguments. The harmonic sums give the slopes


$$
(C,q):\quad (1,19)\ \text{on I},\qquad (8,10)\ \text{on II}.
$$



Most importantly, the ordinary integer carry is present:


$$
\frac1{29}\binom{40}{20}\equiv2\pmod{29}.
$$


Its contribution is $5\cdot2=10$, and the surviving harmonic contribution is $12$. Hence


$$
\boxed{\lambda_{\mathrm I}+\lambda_{\mathrm{II}}
\equiv29\cdot22\pmod{841}.}
\tag{5.1}
$$



This is a congruence for the sum of the **actual compatible lifts**. Replacing $21+8=29$ by an integer zero would lose exactly the layer being computed.

The remaining common lift multiplies the whole difference


$$
\sum(F_{\mathrm I}^2-F_{\mathrm{II}}^2),
$$


which is divisible by $29$. Its contribution is therefore zero modulo $841$. This is a legitimate contracted elimination, not a separate evaluation of the two interface constants.

---

## 14. The weighted reflection preserves the finite range

A direct low-digit check makes the reflection argument transparent.

Write


$$
X=29x+19,\qquad
C=\delta+29C_7,
$$




$$
q=d+29r,\qquad
C-q=k+29(C_7-r-\varepsilon),
$$


where


$$
d+k=\delta+29\varepsilon.
$$



On nonzero low support,


$$
d,k\le19.
$$


Lucas reduction gives, up to the fixed higher factor,


$$
V(q)^2
\equiv
\binom{19}{d}^2\binom{19}{k}^2\pmod{29}.
\tag{5.2}
$$


Indeed,


$$
\binom{9+k}{k}\equiv(-1)^k\binom{19}{k}\pmod{29},
$$


and the sign disappears on squaring.

Exchanging $d,k$:

- preserves $\varepsilon$;
- preserves the higher factor;
- preserves
  

$$
0\le r\le C_7-\varepsilon;
$$


- exchanges the squared interface multipliers, because
  

$$
2X+C+1-q\equiv10+k=-(19-k),\qquad
  X-q\equiv19-d.
$$



Therefore


$$
\sum qF_{\mathrm I}^2
\equiv C\sum F_{\mathrm{II}}^2-\sum qF_{\mathrm{II}}^2
\pmod{29},
$$


and


$$
2S_1\equiv CS_0\pmod{29}.
\tag{5.3}
$$



No whole-word reflection or range completion is needed.

---

## 15. The cubic reduction is safe; unrestricted rank-three reduction is not

The exact coefficient-weighted recurrence gives


$$
V(q+1)^2\mathcal B(q+1)=V(q)^2\mathcal A(q),
$$


with


$$
\mathcal A(q)=(X-q)^2(C-q)^2,
$$




$$
\mathcal B(q)=q^2(2X+C+1-q)^2.
$$



Thus


$$
\sum_{q=0}^{C}V(q)^2
\bigl(\mathcal A(q)R(q+1)-\mathcal B(q)R(q)\bigr)=0.
$$


The endpoints are retained and have zero flux:


$$
\mathcal B(0)=0,\qquad \mathcal A(C)=0.
$$



For $R=1$, at $X\equiv19\pmod{29}$, the identity becomes


$$
\boxed{
11S_3-2CS_2+(3C+20C^2)S_1+13C^2S_0=0.
}
\tag{5.4}
$$


The pivot $11$ is a unit.

The whole interface first gives


$$
\kappa=21D+(22-C)T+20M.
$$


Subtracting $15$ times (5.4) from the last two terms yields


$$
16S_2+(4+22C+19C^2)S_1+(25+16C+8C^2)S_0.
$$


Using $2S_1=CS_0$ gives exactly


$$
\boxed{
\kappa
=21D+16S_2+
(25+18C+19C^2+24C^3)S_0\pmod{29}.
}
\tag{5.5}
$$



The divided observable remains


$$
D=\frac{X+C+1}{29}
\bigl((3X+C+1)S_0-2S_1\bigr)\pmod{29},
$$


where the **whole numerator** is divided by $29$.

A3-style or characteristic-zero rank reasoning cannot remove this precision requirement. For higher telescoping degrees the leading coefficient is


$$
r+2X+2\equiv r+11\pmod{29},
$$


which is singular at $r\equiv18\pmod{29}$. A2 correctly identifies this obstruction.

Likewise, treating a shift of size $29$ as uniformly small in all high binomial polynomials is invalid once factorial denominators contain $29$. The source’s example involving $\binom z{29}$ identifies the precise failure.

---

## 16. Meaning of the new sparse receipt

The coordinator implementation independently computes stripped factorial units modulo $841$, with valuation tracked separately. Every inversion is of a $29$-adic unit.

The initial incorrect-looking assignment to `beta` is overwritten before use by the authoritative digit expansion; the asserted operative value is


$$
\beta=410910916.
$$


It does not affect the calculation.

The $4245$ small binomial checks corroborate the unit routine. The three sparse evaluations then use


$$
191268,\qquad382536,\qquad573804
$$


atoms, respectively. Their total is $1147608$.

The reported outputs are


$$
\mathcal N(0)=754,\quad
\mathcal N(1)=261,\quad
\mathcal N(2)=290\pmod{841},
$$


all divisible by $29$, and hence


$$
\kappa(0)=26,\quad\kappa(1)=9,\quad\kappa(2)=10.
$$



The implementation explicitly does **not** prove outside-support exclusion. That exclusion comes from the retained valuation theorem. Nor does it evaluate either complete physical column, $A_0$, or an original power.

The all-compatible-family obstruction remains valid:


$$
C_h=\beta29^h\longrightarrow0\quad\text{\(29\)-adically},
$$


while


$$
\kappa(C_h)=0,\qquad \kappa(0)=26.
$$


Thus even continuity at $C=0$ fails on that enlarged family, not merely one proposed fixed-prefix rule.

This cannot be transferred to nonconstancy on the original power orbit. Conversely, realizing an auxiliary finite prefix on that orbit cannot transfer the auxiliary value $26$.

The physical statement remains


$$
\eta=A_0^2\kappa.
$$


Any deduction from nonzero $\kappa$ to an exact physical norm depth must additionally retain the required unit information about $A_0$; the auxiliary receipt supplies none.

---

# VI. Complete columns, final gcds, and the whole errors remain unchanged

## 17. Endpoint reconstruction and weighted primitive normalization

The retained endpoint columns are


$$
u=(-sx_0,\ sx_0-sx_1,\ sx_1-sx_2,\ sx_2),
$$




$$
v=(1-sy_0,\ sy_0-sy_1,\ sy_1-sy_2,\ sy_2),
$$


where $sx=Sx$, $sy=Sy$, with the original $S$. The first coordinate of $v$ retains its exterior $+1$.

The least clearer is over all eight entries. At $3375$, the actual reconstruction row contents remain


$$
\boxed{(113940000,\ 9780750,\ 10125,\ 1).}
$$



For a reduced weight $\lambda=a/k_{\rm wt}$, retain


$$
F_{\rm gcd}
=\gcd(|A_{\rm wt}|,|a|)
 \gcd(|B_{\rm wt}|,|a-k_{\rm wt}|),
$$




$$
G_{\rm wt}=\gcd(k_{\rm wt},|J_{\rm wt}|),
$$




$$
H_{\rm gcd}
=\gcd\!\left(h_{\rm end},
\frac{|T_{\rm wt}|}{F_{\rm gcd}G_{\rm wt}}\right).
$$


Then the actual primitive denominator is


$$
\boxed{
q_\lambda=
\frac{k_{\rm wt}h_{\rm end}|A_{\rm wt}B_{\rm wt}|}
{F_{\rm gcd}G_{\rm wt}H_{\rm gcd}}.
}
\tag{6.1}
$$


Every prime remains in these gcds.

The whole same-index error is


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=q_\lambda e_3\alpha_{n,2}(\lambda-\Lambda_{n,2}).
}
\tag{6.2}
$$


The five accepted $3375$ enclosures remain nonzero forms of absolute value greater than $1$. No new theorem above changes those evaluated values.

---

## 18. Characteristic-three producer boundaries

The finite spaces remain


$$
0\le v\le2n-2,\qquad
0\le u<D,\qquad
0\le i<\nu,\qquad
d\le b\le m,
$$


with


$$
d=\frac{3D}{2}-1,\qquad \nu=\frac D2-1.
$$



The complete corrected columns and nonlinear correction remain


$$
\widehat Z^{\,\mathrm{act}}
=\widehat Z^{\,c}-3^6WE_{\mathrm{act}}^{-1}T_R,
$$




$$
S_{\mathrm{act}}-S_c
=3^6K_Z-3^{12}T_R^TE_{\mathrm{act}}^{-1}T_R.
$$



The terminal return keeps its original rows $0\le i\le\nu-2$, the exterior $\omega_{\nu-1}$, and no moment beyond $D-4$. The endpoint automaton does not replace any $\Delta_H$ layer, force pole, LOW subtraction, or unpaired cutoff term.

After actual row contents and the least clearer,


$$
g_\ell=\gcd(|A_\ell|,|B_\ell|),\qquad
q=\frac{|B_\ell|}{g_\ell},
$$


and the error remains


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{g_\ell}
\det H_{\rm complete}.
}
\tag{6.3}
$$



Neither density-one divisibility modulo $3$ nor a nonzero endpoint residue evaluates this all-prime gcd.

---

## 19. The complete $29$-adic second force remains a separate obligation

The actual columns are


$$
Z_w=\mathcal RA^{-1}f^0,\qquad
Y=\mathcal RA^{-1}\mathbf r+W_be_b.
$$



The complete mixed-force identity remains


$$
p^3U_a^TQ
=
p^3(r_0G^{(3)}_{a0}+r_1G^{(3)}_{a1})
+\sum_{\ell=1}^{b-2}\mathcal H_\ell\lambda'_{a,\ell}
+W_bU_{a,b},
$$


with both complete initial charges and all source rows $1,\ldots,b-2$. There is no source row $b-1$, and the terminal exterior is not another recurrence step.

The unresolved relative alignment is still


$$
x^TQ-p^c\rho_nx^Tx
\equiv0\pmod{p^{c+\nu+1}},
\qquad
N_{\log}\ge c+4+\nu.
$$



The row metric, actual row contents, and least two-column clearer precede


$$
A_B=N_{B,1}^T\Omega N_{B,1},\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B.
$$


Thus


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n
}
\tag{6.4}
$$


still uses the whole same-index error.

---

# VII. Remaining bottlenecks and genuinely new bounded arithmetic

## 20. The principal outstanding arithmetic lemma

The priority endpoint obstruction is now sharply isolated.

The exact residuals are


$$
\mathcal D_{j,i}
=
2F_{j,i}(n!)^3+
\left(mZM_{j,i}-F_{j,i}
(h_nb_{n+1}-h_{n+1}b_n)\right).
\tag{7.1}
$$



The required follow-on lemma is:

> **Actual moment–reference content lemma.**  
> On an infinite subsequence of the original indices, prove
> 

$$
> \log\mathfrak D_0+\log\mathfrak D_3=O(n),
>
$$


> or at least
> 

$$
> \log\mathfrak D_0+\log\mathfrak D_3=o(n\log n).
>
$$



The new reference-sensitive theorem removes more possible projection excess, and shows that the two excesses are coprime. It does not establish this content estimate.

The precise obstruction is congruential cancellation between the factorial term and the evaluated remainder in (7.1), simultaneously with divisibility of the actual $R_j$. Neither real dominance nor the fact that $(n!)^3$ is a unit at $p>n$ excludes that cancellation.

For A1, the next local obligation is a paid higher-$3$-adic endpoint evaluation in the density-one zero-output case. For A2, it is an original-orbit evaluation or annihilation of the row


$$
(21,\ 25+18C+19C^2+24C^3,\ 16)
$$


on $(D,S_0,S_2)$, with $D$ known one extra digit before division.

Even after these local obligations, the actual all-prime denominator must still be compared with a whole, nonzero, same-index error.

---

## 21. Bounded exact arithmetic status

No additional calculation is needed to validate the accepted receipts, and none is requested again.

The new denominator extension in §9 is a symbolic residue proof. If a separate implementation certificate is desired, the only new bounded task is very small:

### Inputs

- the class $n\equiv17\pmod{32}$;
- the parameter-one formulas
  

$$
a_s(1)=\frac{(s-1)(s-2)}2,\qquad
  u_s(1)=\frac{s(s+1)}2E_{s-1}+2;
$$


- $E_0=1,\ E_r=rE_{r-1}+1$, through $r=18$;
- A3’s exact normalized endpoint-row formulas.

### Expected verifiable output



$$
(a_{n-2},a_{n-1},a_n,a_{n+1},a_{n+2})
=(11,9,8,8,9)\pmod{16},
$$




$$
(u_n,u_{n+1},u_{n+2})=(11,8,8)\pmod{16},
$$




$$
(X_0,Y_0,Z_0)=(9,14,10),\qquad
\mathscr R_3/2=(8,11,8),\qquad
U=(2,0,15)\pmod{16},
$$


and both dot products equal $8\pmod{16}$.

This would be new corroboration of the additional residue class, not a rerun of an original producer, the $225$ calculation, or the accepted binary pipeline. The hand derivation above already supplies the proof.

No finite gcd postprocessing can, by itself, establish the outstanding infinite residual-content estimate.

---

# VIII. Proof-status ledger and conclusion

| Statement | Status |
|---|---|
| A3’s four evaluated endpoint equations | Audited proof |
| Twelve integral projection identities | Audited proof; new $3375$ corroboration |
| Reference-pair unit ideal for $p>n+2$ | Independently justified by backward recurrence |
| Exact projected ideal | Audited proof at $p>n+2,\ p\nmid G_j$ |
| Polynomial losses $\Pi_0,\Pi_3$ | Audited proof |
| $\mathfrak D_0=\mathfrak D_3=1$ at $3375$ | Accepted new finite execution |
| Reference-sensitive losses $B_0,B_3$ | **New theorem** |
| Coprimality of the two projection excesses | **New joint-endpoint consequence** |
| A3’s binary denominator theorem on $15^{2a},105^{4a}$ | Accepted |
| Extension to $15^{2a},105^{2a}$ | **New infinite-family actual-denominator theorem** |
| Infinite $O(n)$ residual-content estimate | Open |
| Seven-dimensional Cartier invariant and actual normalization | Audited proof |
| Five-state all-middle-word evaluation | Audited proof |
| Coordinator coefficient and language checks | Finite corroboration |
| Positive-density original suffix/window progression | **Proved here** |
| Relative density one of mod-$3$ zero endpoints there | **Deduction using the stated Lagarias theorem** |
| Individual original-power omission classification | Open |
| Primitive higher-$3$-adic endpoint pair | Unevaluated |
| Whole $29$-adic two-unit-digit interface | Audited proof |
| Weighted finite-range reflection and safe cubic reduction | Audited proof |
| Auxiliary values $26,9,10$ | Accepted independent finite corroboration |
| Original-orbit $\kappa$ or physical $\eta$ evaluation | Open |
| All-prime primitive denominator versus whole error | Open |
| Irrationality or rationality of $e+\pi$ | Unresolved |

## Final assessment

The strongest new actual-denominator result is


$$
\boxed{
v_2(d_0)=v_2(n!)+\frac{n-3}{2},\qquad
v_2(d_3)=v_2(n!)+\frac{n-7}{2}
}
$$


on


$$
\boxed{n=15^{2a}\ \text{or}\ n=105^{2a}.}
$$


It uses the actual primitive rows, the complete exterior-corrected force, restoration of the seed and logarithmic terms, and the actual all-prime denominator formula.

The strongest new projection refinement is


$$
\boxed{
\delta_j^{>}\mid\mathfrak D_j
\mid\gcd(\Pi_j,|L_j|)_{>n+2}\,\delta_j^{>},
}
$$


with coprime endpoint excess bounds. This further reduces artificial projection loss but does not control recurrence-generated cancellation.

The ternary analysis now supports a genuine original-window density statement, while the $29$-adic analysis has a completely evaluated low interface and independently corroborated auxiliary carries. Neither supplies an original primitive higher-layer evaluation or a final all-prime denominator estimate.

The exact global bottleneck remains:


$$
\boxed{
\text{an infinite original-index bound for the actual arithmetic cancellation,
followed by control of the actual primitive denominator against the whole
nonzero same-index error.}
}
$$



No unconditional proof or disproof of the irrationality of $e+\pi$ has been obtained.
