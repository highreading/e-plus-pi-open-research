> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4, Turn 13 — Actual original $29$-adic zeros, saturated endpoint products, and paid Jacobi normalization

## Executive assessment

The newly supplied work makes a substantive advance beyond the closed Turn 12 audits. In particular, the $29$-adic calculation is no longer confined to auxiliary inputs: the new prefix receipts, combined with A2’s integral connection, establish zeros of the actual retained observable at four original indices, independently of every unread high digit.

My conclusions are as follows.

1. **A2’s ordinary-precision connection is valid.** It processes the numerator of the whole divided observable $D$ at precision $29^2$, and only then reduces the remaining high moments to precision $29$. Both cutoff branches and terminal carry $0$ are retained. High nonunit binomial terms cannot restore a contribution to $D\bmod29$.

2. **A2’s killing-word and density-one theorems are valid at their stated scope.** The word $(0,2,5,28)$, read least significant first, forces pointwise divisibility of every retained high weight. The original principal-unit parametrization then gives relative density one of
   

$$
D=S_0=S_2=\kappa=0
$$


   in every fixed original arithmetic progression.

3. **The new original-prefix receipts establish actual zeros at**
   

$$
\boxed{u=0,\ 1,\ 2,\ 381475.}
$$


   The ordinary and first-digit-weighted matrix products both vanish after $5,13,1,3$ digits, respectively. Thus all four branch moments vanish for every high continuation and the actual finite terminal observation. By the already accepted identity
   

$$
\eta=A_0^2\kappa,
$$


   these are physical $\eta=0$ statements; **no unit hypothesis on $A_0$ is needed for this direction**.

4. **A3’s saturated joint-content theorem and exact Smith index are correct.** The loss is precisely $(e-s)_+$, with $s=v_p(\sigma_n)$; it cannot be replaced by $e$. Every unit used in the argument is legitimate at $p>n+2$. The new $3375$ receipt verifies the actual cross-product identities and complete-force fields, without regenerating the producer or denominator extraction.

5. **A3’s odd-$15$-exponent binary law is proved.** The parameter period is $16$, while the needed index period is $32$. The primitive contact-row divisions are paid before the force projection. On
   

$$
n=15^{2a+1},\qquad a\ge1,
$$


   the actual endpoint denominators satisfy
   

$$
\boxed{v_2(d_0)=v_2(d_3)=v_2(n!)+\frac{n-3}{2}.}
$$



6. **A1’s seventeen-coordinate modulo-$9$ transition, first-$2$ injection and two-digit divided-carry return are correct.** The new receipt evaluates the inherited suffix carries rather than discarding them. Its $364$ middle words are finite cylinders, not certified original powers. In particular, the witness $M=202$ disproves a universal *all-middle-word* claim that the first absorbing $2$ always leaves endpoint content exactly one.

7. **The Jacobi bridge closes the normalization uncertainty in A1 Turn 15.** The coefficient outputs are exactly
   

$$
J_m(-1),\qquad J_{m-1}(-1)
$$


   with the same parameter $A=2m-1$, not an independently rescaled pair. They remain distinct from the similarly named recurrence scalars and from full polynomial contents.

I also derive three new relations:

- a short original $29$-adic zero criterion yielding eight explicit residue classes modulo $841$;
- an exact **product-content** constraint, rather than another common-gcd bound;
- an exact content-loss formula for the induced Christoffel endpoint map.

None evaluates a first nonzero primitive norm layer, the complete mixed-force alignment, or an infinite all-prime denominator/whole-error comparison. The irrationality or rationality of $e+\pi$ remains unresolved.

No code was executed for this report, and no accepted computation is proposed for repetition.

---

# I. A2 Turn 9: the whole divided carry really reduces to ordinary precision

## 1. The exact finite object

Retain


$$
p=29,\qquad
b=3^{249005515+574312172u}
 =\beta+p^6C,\qquad
\beta=410910916,
$$




$$
n=2001b,\qquad u\ge0.
$$



The high finite sum is


$$
X=2001C+1382,
$$




$$
V(q)=\binom Xq\binom{2X+C-q}{C-q},
\qquad 0\le q\le C.
$$



The divided observable is


$$
D=
\frac{1}{p}\sum_{q=0}^{C}
\left((2X+C+1-q)^2-(X-q)^2\right)V(q)^2
\pmod p.
\tag{1.1}
$$



The division in (1.1) belongs to the entire finite difference. It is not a termwise operation.

The retained physical carry row is


$$
\boxed{
\kappa
=21D+16S_2+
(25+18C+19C^2+24C^3)S_0\pmod{29}.
}
\tag{1.2}
$$



Nothing in the new connection changes this row or its original cutoff.

---

## 2. Both low-digit branches are necessary and correctly retained

Write


$$
C=\delta+pm,\qquad
a=69C+47,\qquad B=2a+1.
$$


Then


$$
X=19+pa,\qquad 2X=9+pB.
$$



For $q+k=C$, put


$$
q=d+pr,\qquad k=e+ps.
$$


The exact low addition gives


$$
d+e=\delta+p\varepsilon,\qquad
r+s=m-\varepsilon,\qquad \varepsilon\in\{0,1\}.
$$



The supported low pairs are


$$
0\le d,e\le19.
$$


For each branch,


$$
L_\varepsilon=m-\varepsilon,\qquad
0\le r\le L_\varepsilon,
$$


and the high factor is


$$
U_\varepsilon(r)
=
\binom ar
\binom{B+L_\varepsilon-r}{L_\varepsilon-r}.
$$



Thus the second branch has range $0\le r\le m-1$, not $0\le r\le m$. If $m=0$, it is empty. This is exactly the branch distinction required by the original finite sum.

---

## 3. Why high nonunit terms cannot revive $D$

This is the principal precision issue, and A2 resolves it correctly.

### 3.1 Terms with a low valuation event

If either low binomial has a valuation event, then


$$
p\mid V(q),
$$


hence


$$
V(q)^2\in p^2\mathbb Z.
$$


Its contribution to the whole numerator in (1.1) is divisible by $p^2$, and therefore disappears after division by $p$ and reduction modulo $p$.

No cancellation assumption is needed for these excluded terms.

### 3.2 Terms with supported low digits but a high nonunit factor

The one-level factorial-unit expansion is valid with the high binomial retained as an exact integer factor. It does not require that factor to be a unit. Thus, for supported $d,e$,


$$
V(q)^2
\equiv
w_dw_e\,U_\varepsilon(r)^2
\bigl(1+2p(E+h_e)\bigr)
\pmod{p^2},
$$


where


$$
w_t=\binom{19}{t}^2
$$


and the displayed harmonic corrections have only unit denominators.

If $p\mid U_\varepsilon(r)$, its square again makes the entire contribution zero modulo $p^2$.

### 3.3 Why high unit lifts are unnecessary after contraction

For fixed $(\varepsilon,r)$, the factor $U_\varepsilon(r)^2$ is independent of the low pair. The exact integer identity


$$
\sum_{\mathcal E_{\delta,\varepsilon}}
(e-d)w_dw_e=0
\tag{3.1}
$$


annihilates the undivided leading term.

Consequently, after summing over the low pairs, the bracket multiplying $U_\varepsilon(r)^2$ is already divisible by $p$. Changing the high factor by a multiple of $p$ changes that contracted numerator only by a multiple of $p^2$.

This is the precise reason that **ordinary high precision suffices**. It is not an inference from $S_0\equiv0$ alone, nor an illicit division of a zero residue.

---

## 4. Audit of the connection formula

Define, on the exact low sets,


$$
K_{\delta,\varepsilon}
=\sum w_dw_e,\qquad
J_{\delta,\varepsilon}
=\sum d^2w_dw_e,
$$




$$
H_{\delta,\varepsilon}
=\sum(e-d)w_dw_eh_e,\qquad
T_{\delta,\varepsilon}
=\sum(e-d)w_dw_et_e.
$$



There are exactly $20^2=400$ ordered low pairs across the entire table.

Let


$$
M_{\varepsilon,0}=\sum_{r=0}^{L_\varepsilon}U_\varepsilon(r)^2,
\qquad
M_{\varepsilon,1}=\sum_{r=0}^{L_\varepsilon}rU_\varepsilon(r)^2
\pmod p.
$$



The multiplier in (1.1) factors exactly as


$$
(X+C+1)(3X+C+1-2q).
$$


In the low/high coordinates it is


$$
\bigl(20+\delta+p(a+m)\bigr)
\bigl(e-d+p(3a+2+s-r)\bigr).
$$



The $p(a+m)$-term vanishes after the exact antisymmetric contraction (3.1). The compatible low reflection supplies the additional $2H$-term. Combining it with the factorial-unit correction gives


$$
(3a+2)(K+2H)+(s-r)(K+2T).
$$



Since $s-r=L_\varepsilon-2r$, the resulting connection is


$$
\boxed{
\begin{aligned}
D=(20+\delta)\sum_{\varepsilon=0}^{1}
\Big[
&(3a+2)(K_{\delta,\varepsilon}+2H_{\delta,\varepsilon})
M_{\varepsilon,0}\\
&+(K_{\delta,\varepsilon}+2T_{\delta,\varepsilon})
(L_\varepsilon M_{\varepsilon,0}-2M_{\varepsilon,1})
\Big]\pmod p.
\end{aligned}}
\tag{4.1}
$$


Together with


$$
S_0=\sum_\varepsilon K_{\delta,\varepsilon}M_{\varepsilon,0},
\qquad
S_2=\sum_\varepsilon J_{\delta,\varepsilon}M_{\varepsilon,0},
\tag{4.2}
$$


this proves the ordinary-precision reduction.

The argument bypasses the previously identified singular rational-moment pivot. It does not invert it.

---

## 5. The two-state closure represents the actual finite terminal condition

For digits $a_i,B_i,m_i$, A2 uses


$$
\mathsf K_i[e,f]
=
\sum_{\substack{
0\le d\le a_i\\
0\le k\le28-B_i\\
d+k=m_i+29f-e}}
\binom{a_i}{d}^2\binom{B_i+k}{k}^2.
\tag{5.1}
$$



The conditions have distinct roles:

- $d\le a_i$ excludes a borrow in $a-r$;
- $k\le28-B_i$ excludes a carry in $B+s$;
- $e,f$ are the incoming and outgoing carries in $r+s+\varepsilon=m$.

The initial row $e_\varepsilon^T$ retains the branch $\varepsilon$. The terminal column is $e_0$, so an unfinished addition carry is not accepted:


$$
M_{\varepsilon,0}
=e_\varepsilon^T\mathsf K_0\cdots\mathsf K_{L-1}e_0.
$$



For the first moment only the least significant digit of $r$ is relevant modulo $29$. Therefore only $\mathsf K_0$ is replaced by its $d$-weighted version:


$$
M_{\varepsilon,1}
=e_\varepsilon^T\mathsf K_0^{[1]}
\mathsf K_1\cdots\mathsf K_{L-1}e_0.
$$



This is an integral two-state realization of the particular finite moments. It is not a claim about arbitrary higher-precision moments or a completed Hahn measure.

---

## 6. Meaning of the new connection receipt

The supplied coordinator source compares:

- all $400$ low pairs;
- $90$ complete divided-carry evaluations;
- $302$ direct high moments;
- all $138=69\cdot2$ incoming multiplication/doubling interfaces for the killing word.

These are correctly scoped checks. In particular, the direct whole observable is accumulated modulo $841$ before division by $29$, and the high moments are compared with their exact branch ranges.

The auxiliary values remain


$$
\begin{array}{c|cccc}
C&D&S_0&S_2&\kappa\\ \hline
0&18&1&0&26\\
1&18&26&13&9\\
2&19&13&2&10.
\end{array}
$$



They are corroboration of the connection, not original-index values.

The same receipt now instantiates the original killing-word progression:


$$
\boxed{u\equiv381475\pmod{707281}.}
$$


Its modular data are


$$
C_0=276031,\qquad g=644279,
$$


and the target residue is


$$
C\equiv687155\pmod{29^4}.
$$



The progression’s all-member conclusion comes from the proved prefix criterion and principal-unit congruence, not from the four checked representatives alone.

---

# II. Original $29$-adic annihilation: theorem, actual receipts, and a shorter new cylinder

## 7. The killing-word theorem is correct

For


$$
a=69C+47,
$$


the multiplication carry always lies in $\{0,\ldots,68\}$. The digits $0,2,5$ force


$$
a_{h+2}=1
$$


and force the corresponding digit of $B=2a+1$ to be $3$, independently of the incoming multiplication and doubling carries.

The final digit $28$ therefore gives, at position $h+3$,


$$
X_t=1,\qquad (2X)_t=3,\qquad C_t=28.
$$



If $V(q)$ were a unit, Kummer’s criterion would require


$$
q_t\le1,\qquad (C-q)_t\le25.
$$


Even allowing the incoming addition carry, their sum is at most $27$, whereas the output digit is $28$. This is impossible.

Hence


$$
29\mid V(q)\qquad(0\le q\le C).
$$


The conclusion for $D$ is then pointwise safe:


$$
V(q)^2\in29^2\mathbb Z
\quad\Longrightarrow\quad
D=0\pmod{29}.
$$



This establishes


$$
\boxed{D=S_0=S_2=\kappa=0.}
\tag{7.1}
$$



---

## 8. The relative-density-one argument is also valid

The retained parametrization gives compatible bijections


$$
u\bmod29^N\longmapsto C(u)\bmod29^N.
$$



For $R$ disjoint four-digit positions, the proportion of residue classes avoiding the killing word in every position is


$$
\left(1-\frac1{29^4}\right)^R.
$$



Every index with nonzero $\kappa$ avoids all those occurrences. Thus its upper density is at most the displayed quantity for every $R$, and is therefore zero.

Inside a progression $u\equiv u_0\pmod h$, the lower $v_{29}(h)$ digits are fixed. Placing the test blocks above them and applying the compatible bijection, together with CRT for the prime-to-$29$ part of $h$, gives the same limiting argument.

This proves relative natural density one in every fixed original progression. It does not prove eventual annihilation at every index.

---

## 9. Why the actual-prefix receipts are decisive

The new original-prefix program computes $C$ modulo $29^{129}$ from the original modular power. This determines:

- $a$ and $B$ to at least $128$ digits;
- $m=\lfloor C/29\rfloor$ to $128$ digits.

Thus every inspected matrix digit is determined by the actual original integer.

The two products are:

1. the ordinary product;
2. the product weighted only at its first digit.

The program requires **both full $2\times2$ products** to be zero. Consequently:

- both branch rows are annihilated;
- every possible high tail is annihilated;
- the actual final column $e_0$ is annihilated.

The receipt establishes


$$
\begin{array}{c|c|c}
u&\text{digits consumed}&(D,S_0,S_2,\kappa)\bmod29\\ \hline
0&5&(0,0,0,0)\\
1&13&(0,0,0,0)\\
2&1&(0,0,0,0)\\
381475&3&(0,0,0,0).
\end{array}
\tag{9.1}
$$



These zeros may arise from matrix cancellation; they need not imply pointwise divisibility of every summand. That distinction does not weaken the conclusion, because the integral connection (4.1) has already discharged the extra precision obligation for $D$.

### Physical interpretation

The accepted complete-column reduction is


$$
\eta=A_0^2\kappa.
$$


Thus $\kappa=0$ implies $\eta=0$ whether $A_0$ is a unit or a nonunit.

The reverse style of inference is different: a nonzero auxiliary $\kappa$ would not establish a nonzero physical $\eta$ without the necessary information about $A_0$.

The receipt’s conditional label does not alter this mathematics. With the retained norm reduction accepted, (9.1) gives actual physical zeros at the indicated layer.

---

## 10. New short original-zero criterion

The new receipts permit a useful hand deduction without reading additional digits.

### Proposition 10.1

If


$$
\boxed{C\equiv7+29t\pmod{841},\qquad 21\le t\le28,}
\tag{10.1}
$$


then


$$
D=S_0=S_2=\kappa=0\pmod{29}.
$$



#### Proof

Here


$$
a_0=(69\cdot7+47)\bmod29=8,\qquad B_0=17,
$$


and $m_0=t$.

Every summand in the first digit matrix would require


$$
d\le8,\qquad k\le11,
$$


so $d+k\le19$. But its carry equation requires


$$
d+k=t+29f-e\ge t-1\ge20.
$$


Thus the entire first matrix is zero. Its weighted version is zero for the same support reason. Equations (4.1)–(4.2) finish the proof. ∎

Using the supplied modular receipt,


$$
\beta\equiv-2,\qquad C_0\equiv183,\qquad g\equiv73\pmod{841},
$$


hence


$$
C(u)\equiv183+695u\pmod{841}.
$$


Since $695^{-1}\equiv144\pmod{841}$, condition (10.1) is equivalent to


$$
u\equiv-29t-114\pmod{841}.
$$



Therefore


$$
\boxed{
u\bmod841\in
\{2,31,60,89,118,756,785,814\}
\Longrightarrow
D=S_0=S_2=\kappa=\eta=0.
}
\tag{10.2}
$$



This is a new explicit original-family consequence. It uses the already supplied modular data and a one-matrix support argument, not a rerun.

It remains a zero theorem at the retained layer. It neither identifies the next primitive norm layer nor removes the complete mixed-force obligation.

---

# III. A3 Turn 8: exact saturation and the odd binary class

## 11. The common contact column is locally primitive

Retain


$$
m=n+1,\qquad N=n+2,
$$


and


$$
L=nJ_0+J_1.
$$



In the basis $v',w',e_2$,


$$
L=\frac12(Pv'+Qw'+Fe_2),
$$


where


$$
P=nX+Y,\quad Q=nZ+2X-Y,
$$




$$
F=2m\bigl(Y-2X-(n-1)Z\bigr).
$$



At $p>N$:

- $2,m,N$ are units;
- $\det[v',w',e_2]=2N^2$ is a unit;
- the map
  

$$
(X,Y,Z)\mapsto\left(P,Q,\frac{F}{2m}\right)
$$


  has determinant $-N$, also a unit.

Thus $L\equiv0\pmod p$ would force $X=Y=Z=0\pmod p$, contrary to retained moment primitivity.

Therefore


$$
\operatorname{cont}(L)_{>N}=1.
$$



There is no implicit large-prime denominator in this step.

---

## 12. The contact-row Smith index is exactly the stated one

For the raw rows


$$
\mathscr R_0=(-1,n,-nm)\operatorname{adj}(J),\qquad
\mathscr R_3=(0,0,1)\operatorname{adj}(J),
$$


the cross-product identity is


$$
\mathscr R_0\times\mathscr R_3=\det(J)L.
$$



If $c_0,c_3$ are their actual contents, then


$$
r_0\times r_3
=\pm\frac{\det J}{c_0c_3}L.
$$


Consequently,


$$
\boxed{
\sigma_n=
\frac{|\det J|\operatorname{cont}(L)}{c_0c_3}.
}
\tag{12.1}
$$



The two-row matrix has first Smith invariant $1$, because an actual primitive row already has entry gcd $1$. Its second Smith invariant is the gcd of its $2\times2$ minors, namely $\sigma_n$.

At $p>N$,


$$
\boxed{
v_p(\sigma_n)=v_p(\det J)-v_p(c_0)-v_p(c_3).
}
\tag{12.2}
$$



This is the exact transverse lattice cost. The two-row observation is not saturated merely because its rows are individually primitive.

---

## 13. Audit of the $(e-s)_+$ theorem

Let


$$
e=\min\{v_p(R_0),v_p(R_3),v_p(C_0),v_p(C_3)\},
\qquad s=v_p(\sigma_n).
$$



Because $L$ is primitive over $\mathbb Z_p$, it can be completed to a local basis. In that basis the two-row matrix is $(A\ 0)$, with


$$
v_p(\det A)=s.
$$



Applying the adjugate to two projections divisible by $p^e$ gives transverse coordinates divisible by $p^{e-s}$, when $e>s$. Therefore, with $d=e-s>0$,


$$
\mathbf H\equiv\lambda L,\qquad
\mathbf C\equiv\mu L\pmod{p^d}.
$$



The reference pair $(h,\ell)$ generates the unit ideal at $p>N$, so $\mathbf H$ is primitive and $\lambda$ is a unit. Comparing coordinates then gives, in order,


$$
F\equiv0,\qquad Z\equiv0,\qquad Y-2X\equiv0,\qquad \ell\equiv0
\pmod{p^d}.
$$



Finally,


$$
\mathbf H\wedge\mathbf C\equiv0\pmod{p^d}
$$


forces


$$
\mathscr K_n=hT_n-\ell S_n\equiv0\pmod{p^d}.
$$



Hence


$$
\boxed{
(e-s)_+
\le
\min\{v_p(\ell),v_p(Z),v_p(Y-2X),v_p(\mathscr K_n)\}.
}
\tag{13.1}
$$



The proof pays $s$ once. It neither ignores $s$ nor introduces a fictitious $2s$ loss.

The complete residual is essential: its normal coordinate is $mZ$, and


$$
\mathscr K_n
=h_nb_{n+1}-h_{n+1}b_n-2(n!)^3.
$$


The logarithmic term has not been dropped.

---

## 14. Scope of the new $3375$ receipt

The coordinator reconstruction correctly distinguishes


$$
\ell=n!\tau_{n+1}
$$


from the fixed-parameter reference value


$$
h_{n+1}=\frac m2(h+\ell).
$$


Its construction of $b_{n+1}$ and $\mathscr K_n$ uses the latter where required. This distinction matters.

The receipt establishes:


$$
\operatorname{bits}(\Sigma_n)=116931,
$$


but


$$
\boxed{
g_n=1,\qquad
\gcd(\ell,Z,Y-2X,\mathscr K_n)_{>3377}=1.
}
\tag{14.1}
$$



Thus the large Smith index is genuinely present, while the actual joint cancellation does not use it at this index.

The saturated divisibility check is numerically $1\mid1$. It is not, by itself, evidence for the sharpness of the exponent loss. The exact cross-product and saturation identities are the substantive lattice corroboration.

The binary fields are


$$
\begin{array}{c|cc}
&0&3\\ \hline
v_2(c_j)&5&0\\
v_2(\alpha_j)&1&1\\
v_2(\beta_j)&4&4\\
v_2(G_j)&1&1\\
v_2(R_j)&1691&1691\\
v_2(r_j\mathbf U)&5&5\\
v_2(C_j)&5&5.
\end{array}
\tag{14.2}
$$



These are new archived-data fields, not regenerated denominator values.

---

## 15. The odd-$15$-exponent binary proof survives audit

Assume


$$
n=15^{2a+1},\qquad a\ge1.
$$


Then


$$
n\equiv15\pmod{32},\qquad m=16u,\quad u\text{ odd}.
$$



### 15.1 Parameter and index periods

The coefficients


$$
c_i(n)=i![z^i]\left(1-z+\frac{z^2}{2}\right)^n
$$


are integer polynomials in $n$, and


$$
v_2(c_i(n))\ge v_2(i!)-\lfloor i/2\rfloor.
$$



Modulo $16$, all terms with $i\ge12$ vanish. For $i\le11$, Vandermonde’s identity with


$$
v_2\binom{32}{r}=5-v_2(r)
$$


pays the needed index shift.

Thus:

- the parameter may be reduced modulo $16$;
- the relevant moment index may be reduced modulo $32$.

The parameter is reduced to $-1$, and the retained recurrence for $e^z/q(z)$ gives


$$
(C,B,A,D,E)\equiv(0,10,7,1,10)\pmod{16}.
$$



There is no unjustified period-$16$ reduction of the index.

### 15.2 Primitive divisions

For endpoint $0$,


$$
\mathscr R_0=mN(X_0,Y_0,Z_0),\qquad
(X_0,Y_0,Z_0)\equiv(2,0,0)\pmod{16}.
$$


Therefore the raw content has valuation $5$, and the primitive row satisfies


$$
x_0\text{ odd},\qquad y_0,z_0\in8\mathbb Z.
$$



For endpoint $3$, the first raw coordinate is odd. Its content has valuation $0$.

The actual endpoint equations then yield


$$
v_2(\alpha_j)=1,\qquad v_2(\beta_j)=4,
$$


and, after the paid divisions,


$$
\frac{\beta_j}{16}\equiv
-u\,\frac{\alpha_j}{2}\pmod4.
\tag{15.1}
$$



This congruence is not being asserted for an unnormalized row.

### 15.3 Reference and complete force

With $k=(n-1)/2$,


$$
v_2(h)\ge k+1,\qquad v_2(\ell)=k-3.
$$


The terms in $h\alpha_j+\ell\beta_j$ have distinct depths, so


$$
v_2(R_j)=k+4.
$$



The force identity


$$
u_s(n)=\sum_i\binom si c_i(n)E_{n+s-i}
$$


is the retained complete exponential force. Its guarded modulo-$4$ reduction gives


$$
u_n-A\equiv1,\qquad u_{n+1}-D\equiv3\pmod4.
$$



Using (15.1) in the exact projection formula gives


$$
\frac{r_j\mathbf U}{16}\equiv2\pmod4,
$$


hence


$$
v_2(r_j\mathbf U)=5.
$$



The seed term is deeper than $5$. The retained complete logarithmic clearer gives


$$
v_2(r_j\mathbf Q)
\ge2v_2(n!)-n+3-\lfloor\log_2(n+1)\rfloor>5
$$


on the stated original subfamily. Thus


$$
v_2(C_j)=5.
$$



Finally, the actual all-prime denominator formula


$$
d_j=
\frac{|n!R_j|}
{\gcd(|n!R_j|,\ |E_nR_j+C_j|)}
$$


gives


$$
\boxed{
v_2(d_0)=v_2(d_3)=v_2(n!)+k-1.
}
\tag{15.2}
$$



This is an infinite-family theorem, not an extrapolation from (14.2). The separate $n\equiv17\pmod{32}$ certificate remains with the coordinator; no repetition is needed here.

---

# IV. New product-content relations: what $B_0,B_3$ can and cannot control

## 16. The reference-sensitive refinement does constrain the exclusive *projection* factor

Retain


$$
\delta_j=\gcd(R_j,C_j)_{>N},
\qquad
\delta_j\mid\mathfrak D_j\mid B_j\delta_j,
\qquad
\gcd(B_0,B_3)=1.
$$



Define the actual and projected endpoint-exclusive products


$$
\mathcal E_\delta
=\frac{\delta_0\delta_3}{\gcd(\delta_0,\delta_3)^2},
$$




$$
\mathcal E_{\mathfrak D}
=\frac{\mathfrak D_0\mathfrak D_3}
{\gcd(\mathfrak D_0,\mathfrak D_3)^2}.
$$


Put $B=B_0B_3$.

### Proposition 16.1



$$
\boxed{
\frac{\mathcal E_{\mathfrak D}}
{\gcd(\mathcal E_{\mathfrak D},B)}
\mid\mathcal E_\delta,
\qquad
\frac{\mathcal E_\delta}
{\gcd(\mathcal E_\delta,B)}
\mid\mathcal E_{\mathfrak D}.
}
\tag{16.1}
$$



#### Proof

At a retained prime, write


$$
v_p(\delta_0)=a,\quad v_p(\delta_3)=b,
$$




$$
v_p(\mathfrak D_0)=a+u,\quad
v_p(\mathfrak D_3)=b+v.
$$


Then


$$
0\le u\le v_p(B_0),\qquad
0\le v\le v_p(B_3).
$$


The two exclusive exponents are $|a-b|$ and $|a+u-b-v|$. The reverse triangle inequality gives


$$
\bigl||a+u-b-v|-|a-b|\bigr|
\le u+v\le v_p(B).
$$


This is exactly the pair of divisibilities in (16.1). ∎

Therefore the exclusive projected product and the actual exclusive product differ by at most the reference-sensitive projection cost:


$$
\left|\log\mathcal E_{\mathfrak D}
-\log\mathcal E_\delta\right|
\le\log(B_0B_3)=O(\log n).
\tag{16.2}
$$



This is a genuinely exclusive-product comparison, not another common-gcd statement.

**But it does not bound $\mathcal E_\delta$.** Large one-sided recurrence-generated cancellation remains possible. The refinement controls projection artifacts, not the actual exclusive arithmetic content.

---

## 17. A new exact product certificate from the shared column

There is an additional relation that does constrain the product ideal itself.

Use the shared-column coefficients $P,Q,F$ from §11, and define


$$
M_L=Qh-P\ell,
$$




$$
\boxed{
\mathcal D_L=mZM_L-F\mathscr K_n.
}
\tag{17.1}
$$


This is the actual residual for $L=nJ_0+J_1$; equivalently, it is the corresponding fixed linear combination of the retained endpoint-$3$ residuals.

### Theorem 17.1 — Endpoint determinant/product identity

With consistent primitive-row signs,


$$
\boxed{
c_0c_3(R_0C_3-R_3C_0)
=
\mp\frac{mN^2}{2}\det(J)\,\mathcal D_L.
}
\tag{17.2}
$$



Consequently, at every $p>N$,


$$
\boxed{
v_p(\delta_0)+v_p(\delta_3)
\le v_p(\Sigma_n)+v_p(\mathcal D_L).
}
\tag{17.3}
$$



#### Proof

The scalar triple-product identity gives


$$
R_0C_3-R_3C_0
=(r_0\times r_3)\cdot(\mathbf H\times\mathbf C).
$$



In the basis $v',w',e_2$,


$$
L=\frac12(P,Q,F),\quad
\mathbf H=\frac m2(h,\ell,0),\quad
\mathbf C=(S_n,T_n,mZ).
$$


Since the basis determinant is $2N^2$,


$$
\begin{aligned}
L\cdot(\mathbf H\times\mathbf C)
&=\frac{mN^2}{2}
\left[mZ(P\ell-Qh)+F(hT_n-\ell S_n)\right]\\
&=-\frac{mN^2}{2}\mathcal D_L.
\end{aligned}
$$



Substitute the exact cross-product formula from §12 to obtain (17.2).

Each term $R_0C_3$ and $R_3C_0$ is divisible by $\delta_0\delta_3$ at the retained primes. The factor $mN^2/2$ and the large-prime part of $\operatorname{cont}(L)$ are units. Equation (12.2) therefore gives (17.3). ∎

If $\mathcal D_L\ne0$, the global form is


$$
\boxed{
\frac{\delta_0\delta_3}
{\gcd(\delta_0\delta_3,\Sigma_n)}
\mid |\mathcal D_L|_{>N}.
}
\tag{17.4}
$$



Combining this with the $B_j$-refinement gives


$$
\boxed{
\frac{\mathfrak D_0\mathfrak D_3}
{\gcd(\mathfrak D_0\mathfrak D_3,\Sigma_nB_0B_3)}
\mid |\mathcal D_L|_{>N}.
}
\tag{17.5}
$$



If $\mathcal D_L=0$, the underlying divisibility into $0$ remains valid, but supplies no height bound.

### Why this is a real advance, and why it is not closure

The joint theorem controls a minimum of endpoint valuations. Equation (17.3) controls their **sum**, after paying the collision index once. It is thus a product-content relation, not a reformulated common-gcd estimate.

It retains the full force:


$$
\mathcal D_L
=
2F(n!)^3+
\left[mZM_L-F(h_nb_{n+1}-h_{n+1}b_n)\right].
$$


The logarithmic term is not omitted.

However, neither $\Sigma_n$ nor the large-prime part of $\mathcal D_L$ has the required subfactorial bound. The new identity does not turn real dominance into congruential noncancellation.

A concrete next lemma is now:

> **Collision-saturated product certificate.**  
> In $\mathbb Z[1/N!]$, construct a second controlled complete-force element in
> 

$$
> \bigl((R_0,C_0)(R_3,C_3):\Sigma_n\bigr)
>
$$


> whose gcd with the explicit element $\mathcal D_L$ has logarithm $o(n\log n)$, and bound the actual overlap
> 

$$
> \gcd(\delta_0\delta_3,\Sigma_n)
>
$$


> at the same scale on an infinite original subsequence.

This is a product-ideal target. A certificate for only the common endpoint ideal would not suffice.

---

# V. A1 Turn 15: the paid modulo-$9$ module and actual endpoint normalization

## 18. The seventeen-coordinate transition is correctly normalized

The exact parametrization is


$$
x=\frac{u(1+u)^3}{1-u},\qquad
\sigma^2=1-u^2.
$$


The four differential identities in A1 cancel the characteristic-zero factor $d(t)$ exactly. Therefore the starting numerators


$$
N_{\mathcal A}=b^7a^8,\quad
N_{\mathcal B}=ub^6a^9,\quad
N_W=b^8a^7,\quad
N_S=b^8a^8
$$


represent the actual outputs, where $a=1+u$, $b=1-u$.

The square-root correction


$$
\sigma(u)\equiv
\sigma(u^3)\frac{1-u^6}{(1-u^2)^4}\pmod9
$$


is legitimate in $\mathbb Z_3[[u]]$. The denominators are units.

The index correction


$$
x(u)^{-3q}
\equiv x(u^3)^{-q}
\left(1-\frac{3qu}{(1-u)^2}\right)\pmod9
$$


explains why the next digit $q\bmod3$ is needed.

After padding the denominators and sectioning, the transition is exactly


$$
\begin{aligned}
\mathcal T_{r,q}(N)(v)
=(1-v^2)^3\Lambda_0\Big(
&u^{-r}Na^{6-3r}b^{6+r}\\
&-3q\,u^{1-r}Na^{6-3r}b^{4+r}
\Big)\pmod9.
\end{aligned}
\tag{18.1}
$$



No negative multiple of $3$ occurs among the possible negative exponents, and


$$
\deg\mathcal T_{r,q}(N)\le15
\qquad(\deg N\le16).
$$


The terminal functional is $N(0)$.

Thus the invariant is a seventeen-coordinate module over $\mathbb Z/9\mathbb Z$, with nine explicit digit/lookahead maps. The proof, not the finite samples, establishes the all-index transition identity.

---

## 19. The first-$2$ carry is paid, and the inherited part survives

The embedding


$$
\iota(H)=b^6a^4H
$$


matches the actual integral differential normalization.

For the stated integer lifts of $R,P$, the evaluated injections are


$$
\boxed{
\mathcal T_{2,q}(\iota(R))/3
\equiv\iota(b^2)\pmod3,
}
$$




$$
\boxed{
\mathcal T_{2,q}(\iota(P))/3
\equiv\iota\bigl(b(1+qa)\bigr)\pmod3.
}
\tag{19.1}
$$



The quotient is well-defined because the entire transition vector was first obtained modulo $9$, and its coefficients are divisible by $3$.

For an actual state


$$
N=s\iota(H)+3Z\pmod9,
$$


the divided result is


$$
s\iota(J_{H,q})+\overline{\mathcal T}_2(Z).
\tag{19.2}
$$


The second term cannot be omitted.

The coordinator implementation respects this distinction: it computes the actual suffix states for all three lookahead digits and subtracts the prescribed integral $R$-lift before dividing the remainder by $3$.

The receipt does not print the full inherited-carry arrays, so I do not invent or quote unprovided coefficient vectors. The source records them in the archived certificate, and its whole-word evaluations include them.

---

## 20. The two-digit return is valid

After the first layer vanishes, a state is $3Z\pmod9$. Subsequent divided transitions are purely characteristic-three:


$$
\mathcal T_{r,q}(3Z)/3=\overline{\mathcal T}_r(Z).
$$



For $\deg Z\le16$, the first digit produces a numerator of degree at most $5$ over


$$
a^{3+r}b^3.
$$


A second digit, with the displayed denominator padding, produces degree at most $3$ over


$$
a^{2+s}b^2.
$$


Multiplication by $a^{2-s}$ puts it over $a^4b^2$, with degree at most $5$.

Thus the divided carry returns to the accepted seven-dimensional numerator space after two digits. No further modulo-$9$ injection is required once the first layer is zero.

---

## 21. What the new ternary receipt proves

The new checks have the stated scopes:

- $153=17\cdot3\cdot3$ degree-basis cases;
- $80$ characteristic-zero endpoint values at $141\le m\le180$;
- $6$ paid injection checks;
- $364=\sum_{\ell=0}^{5}3^\ell$ arbitrary middle words.

The leading-$25$-ones functional is explicitly supplied. Its final lookahead is $0$, as required at the top of the digit word.

The finite classification is


$$
63\text{ endpoint units},\qquad
240\text{ exact endpoint content }1,\qquad
61\text{ endpoint content }\ge2.
$$



The count $63=\sum_{\ell=0}^{5}2^\ell$ is consistent with the previously proved mod-$3$ omission language. It does not enlarge that theorem’s original-power scope.

The witnesses are


$$
\begin{array}{c|c|c}
M&(\mathcal A,\mathcal B,W,S)\bmod9&\text{endpoint conclusion}\\ \hline
\varnothing&(5,7,1,1)&c_m=0\\
2&(3,6,6,6)&c_m=1\\
202&(0,0,0,0)&c_m\ge2.
\end{array}
\tag{21.1}
$$



These are actual endpoint evaluations at the integers defined by the displayed digit words. They are **not** certified members of the original power-of-two orbit.

The last witness decisively excludes:


$$
\text{“For every middle word containing \(2\), the endpoint content is exactly \(1\).”}
$$


It does not exclude that conclusion on some separately proved original subfamily.

---

## 22. The fixed-depth original-window density argument is sound

On a compatible fixed congruence for $m\bmod3^t$, the original relation


$$
m=2^{-1}4^j
$$


gives a fixed arithmetic progression for $j$. Compatibility with


$$
j\equiv81\pmod{243}
$$


is essential.

The exact real window differs from its limiting irrational-rotation interval by the retained exponentially small term $3^{-k}$. Squeezing between fixed inner and outer intervals proves the stated positive density on every nonempty fixed progression.

The window also forces the leading $25$ ones for sufficiently large indices. With the retained suffix, the original progression remains


$$
j\equiv1539\pmod{2187},
$$


possibly refined by further compatible fixed-depth congruences.

Lagarias’s supplied theorem is used only as the sublinear bound


$$
O(J^{0.9725})
$$


for omission among


$$
\left\lfloor3^{-8}2^{2j-1}\right\rfloor.
$$


Subtracting this from a positive-density window set proves relative density one of $c_m\ge1$.

It does not select a divided primitive direction, bound $c_m$ above, or allow a congruence depth increasing with $j$.

---

# VI. The Jacobi bridge and a new exact primitive-content formula

## 23. Exact endpoint identification

The supplied Bernstein definition gives, without changing $A=2m-1$,


$$
\boxed{
J_m(-1)=a_m^{\mathrm{end}},\qquad
J_{m-1}(-1)=b_m^{\mathrm{end}}.
}
\tag{23.1}
$$



The second identity uses


$$
s+A=3m-2
$$


at $s=m-1$. It does not reset $A$ to $2(m-1)-1$.

There is no hidden scalar or change of basis in (23.1). A1’s earlier missing-bridge uncertainty is therefore closed by the new source.

A small integrality clarification is appropriate: the displayed Bernstein normalization is generally in $\mathbb Z[1/2][y]$, hence in $\mathbb Z_3[y]$. For example,


$$
J_s(0)=(-1)^s\binom{s-\tfrac12}{s}
$$


is generally dyadic rather than an ordinary integer. This does not affect the $3$-adic argument, but it does mean that an additional ordinary-integer normalization must not be silently inserted.

Endpoint content is still not full polynomial content.

---

## 24. The Christoffel map has determinant valuation four

Write


$$
a=a_m^{\mathrm{end}},\qquad b=b_m^{\mathrm{end}},
$$


and distinguish the recurrence scalars by superscript “sc”. The exact source identity gives


$$
z:=Z_{\mathrm{source}}(-1)=\gamma a+\theta b,
$$


where


$$
\gamma=
\frac{1+\beta_m^{\mathrm{sc}}+a_m^{\mathrm{sc}}}{A+74},
\qquad
\theta=\frac{\rho_m}{A+74}.
$$



Thus


$$
\binom a z
=
\begin{pmatrix}1&0\\ \gamma&\theta\end{pmatrix}
\binom a b.
\tag{24.1}
$$



On the stated integral scalar branch, $\gamma\in\mathbb Z_3$, and


$$
v_3(\theta)=4.
$$


The matrix has Smith exponents $(0,4)$, not $(0,0)$.

In fact, the determinant valuation itself follows directly on the original $j$-congruence:


$$
A=4^j-1,\qquad
v_3(A)=v_3(4-1)+v_3(j)=5.
$$


Hence


$$
v_3(4A+3)=1,\qquad
v_3(\rho_m)=5-1=4,
$$


while $A+74$ is a unit.

The integrality and valuation assumptions on the other scalars remain separate from this determinant calculation.

---

## 25. New exact content-loss theorem

### Theorem 25.1

Suppose the map (24.1) is integral, with $v_3(\theta)=4$. Let


$$
c=\min(v_3(a),v_3(b)),
\qquad
(a,b)=3^c(\bar a,\bar b),
$$


where $(\bar a,\bar b)$ is primitive. Then


$$
\boxed{
\min(v_3(a),v_3(z))
=
c+\min\{v_3(\bar a),4\}.
}
\tag{25.1}
$$



#### Proof

The unimodular row operation $z\mapsto z-\gamma a$ gives


$$
\min(v_3(a),v_3(z))
=
\min(v_3(a),v_3(\theta b)).
$$


After removing $3^c$, this is


$$
c+\min(v_3(\bar a),4+v_3(\bar b)).
$$


If $\bar a$ is a unit, the minimum is $0$. Otherwise primitivity makes $\bar b$ a unit, and the minimum is $\min(v_3(\bar a),4)$. ∎

### Consequences

1. The forward endpoint-content loss can be any value from $0$ to $4$; it is not automatically $4$.

2. Worst-case inverse transport must pay four digits. Since
   

$$
b=\theta^{-1}(z-\gamma a),
$$


   recovering $b$ modulo $3^K$ requires the appropriate numerator modulo $3^{K+4}$.

3. If $\bar a$ is a unit, then
   

$$
\frac za=\gamma+\theta\frac ba.
$$


   Distinct primitive endpoint directions can agree in the transformed projective coordinate through four additional digits. A low-precision transformed direction therefore does not recover the original direction.

4. Modulo-$9$ evaluation with $c=1$ determines the primitive endpoint pair only modulo $3$. It is insufficient for an unrestricted inverse Christoffel transport or for distinguishing all deeper content-loss cases.

This gives an exact normalization law beyond the determinant warning. It still says nothing by itself about the contents of the full polynomials $J_m,J_{m-1}$, or about the scalar-unit hypotheses required by the normalized root-line comparison.

---

# VII. Complete producers and final primitive normalization remain intact

## 26. Endpoint construction

The domain remains


$$
n=15^r\ \text{or}\ 105^r,\qquad r\ge2.
$$



The original $3\times3$ matrix, forcing through $2n+2$, complete terminal return and both corrected columns remain


$$
u=(-sx_0,\ sx_0-sx_1,\ sx_1-sx_2,\ sx_2),
$$




$$
v=(1-sy_0,\ sy_0-sy_1,\ sy_1-sy_2,\ sy_2).
$$


The exterior $+1$ is retained.

The least clearer is over all eight entries. The accepted reconstruction row contents at $3375$ remain


$$
(113940000,\ 9780750,\ 10125,\ 1).
$$


They are not replaced by contact-row contents or by $\sigma_n$.

For reduced $\lambda=a/k_{\rm wt}$, retain the all-prime factors


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


The actual denominator remains


$$
q_\lambda=
\frac{k_{\rm wt}h_{\rm end}|A_{\rm wt}B_{\rm wt}|}
{F_{\rm gcd}G_{\rm wt}H_{\rm gcd}},
$$


and the whole same-index error is


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=q_\lambda e_3\alpha_{n,2}(\lambda-\Lambda_{n,2}).
}
$$



The five accepted $3375$ whole-form enclosures remain nonzero and of absolute value greater than $1$. None is changed by the new local content identities.

---

## 27. Ternary construction

The finite spaces remain


$$
0\le v\le2n-2,\quad 0\le u<D,\quad 0\le i<\nu,\quad d\le b\le m,
$$




$$
d=\frac{3D}{2}-1,\qquad \nu=\frac D2-1.
$$



Retain


$$
\widehat Z^{\,\mathrm{act}}
=\widehat Z^{\,c}-3^6WE_{\mathrm{act}}^{-1}T_R,
$$




$$
S_{\mathrm{act}}-S_c
=3^6K_Z-3^{12}T_R^TE_{\mathrm{act}}^{-1}T_R,
$$


and


$$
Q_{\mathrm{act}}=Q_c+3^6R_{\mathrm{prod}},
\qquad R_{\mathrm{prod}}=R_{25}+3^{25}\Delta_{25}.
$$



Every pole, lower term, factorial force, LOW subtraction and unpaired boundary term remains part of the complete producer. The terminal return still has rows $0\le i\le\nu-2$, retains $\omega_{\nu-1}$, and adds no moment beyond $D-4$.

After actual row contents and the actual least clearer,


$$
g_\ell=\gcd(|A_\ell|,|B_\ell|),\qquad
q=\frac{|B_\ell|}{g_\ell},
$$


with the gcd over all primes, and


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{g_\ell}
\det H_{\rm complete}.
}
$$



The endpoint module and Christoffel content theorem do not evaluate this gcd or this determinant.

---

## 28. The $29$-adic construction

The original domains remain


$$
0\le j<b,\qquad 1\le i\le b-2,\qquad 0\le j\le b.
$$



Both corrected columns remain


$$
Z_w=\mathcal RA^{-1}f^0,\qquad
Y=\mathcal RA^{-1}\mathbf r+W_be_b.
$$



The complete mixed-force identity is still


$$
\boxed{
p^3U_a^TQ
=
p^3(r_0G^{(3)}_{a0}+r_1G^{(3)}_{a1})
+\sum_{\ell=1}^{b-2}\mathcal H_\ell\lambda'_{a,\ell}
+W_bU_{a,b}.
}
$$


Here both initial charges retain their complete exponential and logarithmic components:


$$
r_i=\sum_s a_s(n)(n+i)_{\underline s}
\left(T_{2n+i-s}+\frac{L_{2n+i-s}}{b!}\right),
\qquad i=0,1,
$$


and every permitted source row remains


$$
\mathcal H_i
=\sum_s a_s(n+1)(n+i)_{\underline s}
\binom{2n+i-s+1}{b},
\qquad1\le i\le b-2.
$$



There is no source row $b-1$; the terminal exterior at $b$ is not another recurrence step. Division by $p^3$ belongs to the whole right-hand side.

The unresolved alignment remains


$$
x^TQ-p^c\rho_nx^Tx
\equiv0\pmod{p^{c+\nu+1}},
\qquad N_{\log}\ge c+4+\nu.
$$



After the actual row contents, metric and two-column clearer,


$$
A_B=N_{B,1}^T\Omega N_{B,1},\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad q_n=A_B/g_B.
$$


The whole error remains


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
$$



The new physical zero at one norm layer neither evaluates $g_B$ nor supplies the first nonzero primitive norm layer.

---

# VIII. Remaining bottlenecks, arithmetic status, and conclusion

## 29. What is now closed, and what remains open

### Closed by proof plus the new receipts

- The whole-$D$ ordinary-precision connection.
- Both finite cutoff branches and terminal carry $0$.
- Carry-independent killing-word annihilation.
- Relative-density-one original annihilation in every fixed progression.
- Actual original zeros at $u=0,1,2,381475$.
- The exact contact-row Smith index and saturated joint theorem.
- The odd-$15$-exponent binary denominator law.
- The seventeen-coordinate paid modulo-$9$ transition.
- First-$2$ injection with inherited carry retained.
- Two-digit return of the divided carry.
- Exact same-parameter Jacobi endpoint normalization.

### New results in this report

- The eight explicit original zero classes in (10.2).
- The exclusive-product comparison (16.1).
- The exact determinant/product certificate (17.2)–(17.5).
- The exact Christoffel endpoint-content formula (25.1).

### Still open

1. **Endpoint construction:** control of the actual collision overlap and endpoint-exclusive product on an infinite original subsequence. The new product certificate supplies an explicit complete-force element, but not the necessary small gcd or height estimate.

2. **Ternary construction:** primitive endpoint direction on a realizable original family, with the scalar-branch and full-polynomial normalization hypotheses actually established. The bridge is no longer missing; reachability and primitive content are.

3. **$29$-adic construction:** the first nonzero primitive norm layer and complete mixed-force alignment. The completed lower connection and prefix calculations should not be prescribed again.

4. **Global objective:** an actual all-prime primitive denominator estimate combined with a whole, nonzero, same-index error tending to zero along an infinite original sequence.

---

## 30. Bounded exact arithmetic status

No additional bounded computation is required to prove the new symbolic relations above.

The only new short arithmetic used in this report was the hand reduction supporting (10.2), with inputs


$$
C_0=276031,\quad g=644279,\quad \beta=410910916,\quad p^2=841.
$$


Its verifiable outputs are


$$
C_0\equiv183,\quad g\equiv73,\quad \beta\equiv-2,
$$




$$
C(u)\equiv183+695u,\qquad695^{-1}\equiv144\pmod{841},
$$


and the eight residue classes displayed in (10.2). The zero-matrix proof then applies uniformly to every continuation.

No producer, old denominator extraction, accepted modulo-$3$ calculation, lower $29$-adic connection, or accepted whole-error enclosure needs to be rerun. The coordinator’s separate $n\equiv17\pmod{32}$ certificate remains unchanged.

A finite arithmetic check cannot establish the remaining infinite product-content bound by itself.

---

## Final conclusion

The strongest new factual change is that the supplied work now contains **actual original-index physical zeros**, not merely auxiliary carry evaluations:


$$
\boxed{
u=0,1,2,381475
\quad\Longrightarrow\quad
D=S_0=S_2=\kappa=\eta=0
}
$$


at the retained $29$-adic layer. Their validity rests on the paid whole-carry connection and annihilation of both full prefix products, with the original finite terminal condition preserved.

The endpoint analysis now has an explicit product relation:


$$
\boxed{
\frac{\mathfrak D_0\mathfrak D_3}
{\gcd(\mathfrak D_0\mathfrak D_3,\Sigma_nB_0B_3)}
\mid|\mathcal D_L|_{>n+2}
}
$$


when $\mathcal D_L\ne0$. This advances beyond common cancellation, but does not bound the remaining evaluated residual.

The Jacobi analysis now has both an exact normalization bridge and an exact primitive-content law:


$$
\boxed{
c(a,Z_{\rm source}(-1))
=
c(a,b)+\min\{v_3(\bar a),4\}.
}
$$


The determinant-four precision loss is therefore concrete, not merely qualitative.

The exact remaining global bottleneck is unchanged in kind but narrower in its local components:


$$
\boxed{
\text{control actual arithmetic cancellation and primitive normalization on an
infinite original family, then compare the actual all-prime denominator with
the whole nonzero same-index error.}
}
$$



No unconditional proof or disproof of the irrationality of $e+\pi$ has been obtained.
