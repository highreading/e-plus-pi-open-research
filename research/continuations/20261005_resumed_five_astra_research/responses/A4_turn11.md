> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4, Turn 11 — Audit of the higher-tail scalar and precision-weighted force restoration

## Executive conclusions

The objective remains an unconditional proof or disproof of irrationality of $e+\pi$. **Neither is obtained by the supplied work.**

The two principal audit conclusions are as follows.

1. **A2’s higher-tail scalar passes, at the scope of the accepted one-carry recurrence and actual reconstruction.** All coefficient tables agree with the exported initializer. Both endpoints $R$ and $R-1$ are necessary, and the parameter is $E=2C+1$, including its carry. The all-digit polynomial formula is correct. Its seed-degree bound can be improved from $43$ to **$42$**.

   The resulting scalar decides the actual norm and mixed-product valuations only when it is nonzero. Its vanishing gives an absolute lower bound, not an all-depth relative-valuation theorem. The proposed actual defect current remains an **unconstructed sufficient criterion**.

2. **A5’s quadratic degree estimate is far too large for coefficient screening.** Precision must be charged to each contact order before degrees are added. Even its conservative input cutoff gives
   

$$
\deg P_p\le 10p-5\pmod{2^p},
$$


   which already excludes coefficient $380$ at both $16$ and $32$ bits.

   A sharper consequence of the stated central prefactor bounds is
   

$$
v_2(F_i)\ge v_2\!\left(\left\lfloor\frac i2\right\rfloor!\right),
$$


   and consequently
   

$$
\boxed{\deg P_p\le 4p-1\pmod{2^p}.}
$$


   Thus, under that central-force interface,
   

$$
\boxed{\mathfrak p_{380}\equiv0\pmod{2^{95}}}
$$


   uniformly on the original family. The proposed $16$-, $32$-, and $64$-bit evaluations cannot detect a nonzero coefficient limit. **Precision $96$ is the first precision not excluded by this bound.**

There is an important documentary limitation: A5 references the central formulas “Turn 20, equations 2.1–2.2,” but those formulas are not reproduced in the attached material. I can audit the consequences of the stated central prefactor structure, and give complete derivations from that structure. I cannot independently certify omitted central summands or denominators. The sharper actual-coefficient conclusion therefore has that explicit input dependency; it is not a verification of unseen formulas.

No tools were executed. The supplied literature gate is retained, without reopening the $p=23$ branch or making an exhaustive novelty claim.

---

# I. Scope and original domains

The two families must remain separate.

### The $29$-adic family

A2 works with


$$
a=432827+682892t,\qquad t\ge0,\qquad b=3^a,\qquad n=2001b,
$$


on the accepted cylinder


$$
t\equiv364\pmod{841}.
$$


There,


$$
b=687936+29^5H,\qquad H\equiv20\pmod{29}.
$$



The actual scalar coordinates are $0\le j\le b$, while each contact matrix has indices $0\le i,j<b$. The accepted actual reconstruction is


$$
D\equiv5C_n^2\mathcal T\pmod{29^4},
\qquad
M-\rho_nD\equiv0\pmod{29^4},
\qquad \rho_n=(6C_n)^{-1}.
$$



These are fixed-precision congruences for the complete actual columns, not all-depth factorizations.

### The binary family

A5 works with


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0,
$$


and


$$
b=128D+81,\qquad C=4002D+2532,\qquad k=2C+1.
$$


Thus


$$
h=32k+1,\qquad n=64k+2,\qquad b=\frac{32k+1}{2001}.
$$



The finite contact range is $0\le i,j<b$. Reconstruction retains


$$
0\le t<D,\quad0\le\rho<128;
\qquad t=D,\quad0\le\rho\le80;
\qquad j=b
$$


with the last coordinate separate.

Nothing below changes these domains or boundaries.

---

# II. A2: complete audit of the normalized higher-tail scalar

## 1. Affine decomposition and the mandatory carry

Write


$$
H=20+29z+29^2R,\qquad 0\le z<29,\qquad R\ge0.
$$


Direct expansion gives


$$
A=2001H+67=9+19\cdot29+29^2C,
$$


where


$$
C=2001R+69z+47.
$$


Doubling gives


$$
2A=18+9\cdot29+29^2(2C+1).
$$


Therefore


$$
\boxed{E=2C+1.}
$$



The $+1$ is not a convention: it is the carry from $2\cdot19=9+29$. Replacing $E$ by $2C$ changes the higher-tail binomial, its lowest-digit support, and potentially every later digit.

Also,


$$
C\equiv11z+18\pmod{29},
\qquad
3C+1\equiv4z+26\pmod{29}.
$$



These identities pass.

## 2. Both finite tail endpoints are necessary

After the two initialized digits, the retained states have sum carry $\sigma\in\{0,1\}$. If the high part of $k$ is $u$, the high part of $H-k$ is


$$
R-u-\sigma.
$$


Hence the two ranges are precisely


$$
0\le u\le R,\qquad 0\le u\le R-1.
$$



The second range is empty at $R=0$. It cannot be merged with the first range by retaining an additional endpoint term, since that would correspond to a negative high part of $H-k$.

Define


$$
B_{L,u}=\binom Cu\binom{E+L-u}{L-u},
$$




$$
\mathscr T_L=\sum_{u=0}^{L}B_{L,u}^2,\qquad
\mathscr V_L=\sum_{u=0}^{L}(2u-L)B_{L,u}^2,
$$


with $\mathscr T_{-1}=\mathscr V_{-1}=0$. These conventions preserve the actual terminal condition.

## 3. All coefficients agree with the exported initializer

Every exported row has


$$
Z_\sigma=(0,h_\sigma,j_\sigma,h_\sigma,0,-j_\sigma).
$$


All $58$ displayed values of $W_\sigma$ are divisible by $29$, and their displayed quotients agree with


$$
r_\sigma=W_\sigma/29\pmod{29}.
$$



The coefficient extraction is


$$
a_\sigma=r_\sigma+2h_\sigma(4z+26),
\qquad
b_\sigma=2(j_\sigma-h_\sigma)
\pmod{29}.
$$



Substitution into these expressions gives the following audit result:



$$
\begin{array}{c|rrrr}
z&a_0&b_0&a_1&b_1\\ \hline
0&11&3&5&26\\
1&25&5&10&24\\
2&2&26&8&3\\
3&17&6&17&23\\
4&17&7&22&22\\
5&17&6&27&23\\
6&9&26&5&3\\
7&18&5&11&24\\
8&7&3&27&26
\end{array}
$$


In particular, $b_1=-b_0$ in every row.

For $9\le z\le28$, the $\sigma=1$ row is zero and $j_0=h_0$. The resulting multipliers are


$$
\begin{array}{c|rrrrrrrrrr}
z&9&10&11&12&13&14&15&16&17&18\\ \hline
\lambda_z&7&9&25&2&27&7&9&8&27&9
\end{array}
$$


and


$$
\begin{array}{c|rrrrrrrrrr}
z&19&20&21&22&23&24&25&26&27&28\\ \hline
\lambda_z&1&9&19&13&10&26&10&25&10&14.
\end{array}
$$



Thus **all coefficient tables in A2 pass**. This is a direct audit of the finite supplied initializer, not an extrapolation from the $33$ auxiliary comparisons.

## 4. Division and harmonic-update audit

The divisions used here are legitimate for the following distinct reasons.

* $X_k/29$ is integral by the accepted common-content theorem.
* If
  

$$
S=\sum_k(X_k/29)^2,
$$


  then $29\mid S$ by the accepted $\mathcal T\in29^3\mathbb Z$. Therefore $\mathcal T/29^3=S/29$ is integral.
* $W_\sigma/29\pmod{29}$ is determined because $W_\sigma$ is supplied modulo $29^2$ and is divisible by $29$.

The harmonic correction cannot simply be discarded at initialization. Its contribution is


$$
\tau\cdot Z_\sigma
=
h_\sigma(3C+1)
+(j_\sigma-h_\sigma)(2u-(R-\sigma))
\pmod{29}.
$$


It is discharged in the next update. Only after that update does the new harmonic accumulator vanish, because its update contains $W_\sigma\bmod29=0$.

Accordingly, the resulting formula is


$$
\boxed{
\frac{\mathcal T}{29^3}
\equiv
a_0\mathscr T_R+b_0\mathscr V_R
+a_1\mathscr T_{R-1}+b_1\mathscr V_{R-1}
\pmod{29}.
}
$$



The derivation uses the accepted one-carry recurrence. The initializer alone would not prove the recurrence or its all-tail validity. At that stated dependency, the derivation is sound.

## 5. The all-digit polynomial product passes

Let


$$
\Pi_m(x)=\sum_{j=0}^{m}\binom mj^2x^j\in\mathbb F_{29}[x],
\qquad \theta=x\frac d{dx}.
$$


Take complete digit expansions


$$
C=\sum_{i=0}^{N-1}c_i29^i,\qquad
E=\sum_{i=0}^{N-1}e_i29^i,
$$


with $29^N>\max(C,E,R)$.

For the first binomial, Lucas gives the factors $\Pi_{c_i}$. For the second, a unit term requires no carry in $E+\ell$, and then


$$
\binom{e_i+\ell_i}{\ell_i}^2
\equiv
\binom{28-e_i}{\ell_i}^2\pmod{29}.
$$


The higher zero digits of $E$ contribute


$$
\prod_{i\ge N}\Pi_{28}(x^{29^i})
=\frac1{1-x^{29^N}}.
$$


That factor contributes nothing beyond its constant term through degree $R$.

Thus no terminal factor is lost in the finite coefficient extraction.

Writing $c=c_0$, $f=28-e_0$, the seed is


$$
\begin{aligned}
\Lambda_z(x)={}&(a_0+a_1x)\Pi_c\Pi_f\\
&+(b_0+b_1x)\bigl((\theta\Pi_c)\Pi_f-\Pi_c(\theta\Pi_f)\bigr).
\end{aligned}
$$


Then


$$
\boxed{
\frac{\mathcal T}{29^3}
\equiv[x^R]\Lambda_z(x)
\prod_{i=1}^{N-1}\Pi_{c_i}(x^{29^i})
                     \Pi_{28-e_i}(x^{29^i})
\pmod{29}.
}
$$



Differentiating only the lowest-digit factors is correct in characteristic $29$. The $x$ multiplying the $\sigma=1$ coefficients correctly represents $R-1$; there is no missing derivative of that shift.

### New refinement: the maximum seed degree is $42$

For $0\le c\le28$,


$$
c+f=
\begin{cases}
27-c,&0\le c\le13,\\
56-c,&14\le c\le28.
\end{cases}
$$


Thus $c+f\le42$.

For $z\ge9$, the seed is simply $\lambda_z\Pi_c\Pi_f$, so its degree is at most $42$.

For $z=0,\ldots,8$, the respective values of $c+f$ are


$$
38,\ 27,\ 16,\ 34,\ 23,\ 41,\ 30,\ 19,\ 37.
$$


The extra factor $x$ therefore gives degree at most $42$, not $43$.

This bound is attained: at $z=26$, $c=14$, $f=28$, and


$$
\Lambda_{26}=25\Pi_{14}\Pi_{28}
$$


has degree $42$.

Hence


$$
\boxed{\max_z\deg\Lambda_z=42.}
$$



## 6. Actual relative valuations: exactly what follows

Write $\Phi_z(R)$ for the scalar just audited. The accepted actual reconstruction gives


$$
D/29^3\equiv5C_n^2\Phi_z(R)\pmod{29},
$$




$$
M/29^3\equiv\rho_n5C_n^2\Phi_z(R)\pmod{29}.
$$



With the retained unit hypotheses on $C_n$ and $\rho_n$:

* If $\Phi_z(R)\ne0$, then
  

$$
v_{29}(D)=v_{29}(M)=3,
$$


  and the defect has valuation at least $4=v_{29}(D)+1$.

* If $\Phi_z(R)=0$, then only
  

$$
v_{29}(D),v_{29}(M)\ge4
$$


  follows. The same absolute defect congruence does not become a relative congruence one digit beyond the actual norm.

This distinction is essential. A primitive sum of squares over $\mathbb Z_{29}$ can acquire arbitrarily deep cancellation, since $-1$ is a square modulo $29$. Positivity over the reals does not prevent that phenomenon.

### New actual consequence: two annihilating tail classes

At $z=9$,


$$
c=1,\qquad e=3,\qquad f=25,\qquad
\Lambda_9=7\Pi_1\Pi_{25}.
$$


This seed has degree $26<29$, and every higher factor involves only powers of $x^{29}$. Therefore


$$
\boxed{
R\equiv27\ \text{or}\ 28\pmod{29}
\quad\Longrightarrow\quad
\Phi_9(R)=0.
}
$$



A2 exhibited the class $28$; the same proof includes $27$. By the accepted original-parameter lifting theorem, both finite digit prescriptions are attained on nonempty original congruence classes, with infinitely many nonnegative representatives.

Consequently, on both classes,


$$
\boxed{v_{29}(D),v_{29}(M)\ge4.}
$$



This is an actual fixed-precision consequence. It is not an all-depth valuation assertion.

## 7. Auxiliary blockers and their quantifiers

The identity used in A2’s blocker proof,


$$
A=29(69H)+67,
$$


is exact.

After fixing $H\bmod29^m$, the digit $H_m$ can set $A_{m+1}=2$, since the relevant coefficient is $69\equiv11\pmod{29}$, a unit. Setting $H_{m+1}=28$ then forces a borrow or carry at that position for every $k+(H-k)=H$.

Incoming carries do not invalidate the argument: absence of the two outgoing binomial carries would require


$$
k_{m+1}\le2,\qquad \ell_{m+1}\le24,
$$


and hence


$$
k_{m+1}+\ell_{m+1}+\sigma\le27,
$$


which cannot have output digit $28$.

The valid conclusion is


$$
\forall r\ge1,\quad
\exists\text{ a further nonempty original cylinder on which }\kappa_X\ge r.
$$


It is not


$$
\exists\text{ one finite original index with }\kappa_X=\infty.
$$


Nor is a compatible infinite digit prescription necessarily represented by a nonnegative integer parameter.

The all-depth minimum-carry recurrence correctly computes auxiliary content from complete finite digit strings, including the drain and terminal acceptance. It does not classify the complete actual Gram pair.

## 8. The actual current is still an open construction

The proposed identity


$$
e_J=\alpha_nd_J+\mathcal B_{J+1}-\mathcal B_J,
\qquad
\alpha_n\in29\mathbb Z_{29},
$$


with


$$
\mathcal B_0=\mathcal B_{h+1}=0,
$$


would imply


$$
M=(\rho_n+\alpha_n)D
$$


and therefore equality of the actual norm and mixed valuations at all depths.

That implication is correct. But it is a criterion, not its construction.

Indeed, formally setting $\alpha_n=(M-\rho_nD)/D$ and defining currents by partial sums merely repackages the desired conclusion. It neither proves $\alpha_n\in29\mathbb Z_{29}$ nor constructs a division-safe local identity.

The outstanding lemma must produce $\alpha_n$ and the currents directly from the complete finite reconstruction, retaining both actual boundaries, the factorial data, the full contact insertion, and the target-appropriate logarithmic force. Nothing in the initializer supplies those mixed-defect data.

---

# III. A5: force restoration and the precision-weighted degree bound

## 9. Central cutoffs: valid implications, but a missing primary formula

The displayed scalar factors satisfy


$$
v_2\!\left(\frac{2^s(s!)^2}{(2s)!}\right)
=
v_2\!\left(\frac{2^s(s!)^2}{(2s+1)!}\right)
=v_2(s!).
$$


Thus the central summation cutoff $s<2p$ is safe **if all accompanying factors are integral**, as asserted.

The central prefactor argument gives the more informative bounds


$$
v_2(B_{2j}(h))\ge v_2(j!),\qquad
v_2(B_{2j+1}(h))\ge v_2((j+1)!).
\tag{9.1}
$$


These imply the stated $\ell<4p$ cutoff.

The logical qualification is that (9.1) requires the falling prefactor to be multiplied by an integral central sum, without an unaccounted denominator. The exact central formulas needed to inspect that assertion are referenced but not attached. Therefore:

* the cutoff deductions from (9.1) are verified below;
* the omitted defining formulas themselves are not independently audited here;
* no fixed-$256$ receipt can replace that missing formula-level check.

## 10. A sharper forcing valuation

The complete displayed force is


$$
F_i(h,n)=
\sum_{\ell=0}^{i}\binom i\ell
(n+i)_{\underline{i-\ell}}B_\ell(h).
$$



### Proposition 1 — factorial forcing envelope

Assume (9.1). Then, uniformly for $h,n\in\mathbb Z_2$,


$$
\boxed{
v_2(F_i(h,n))
\ge w_i:=v_2\!\left(\left\lfloor\frac i2\right\rfloor!\right).
}
\tag{10.1}
$$



### Proof

A product of $q$ consecutive $2$-adic integers is divisible by $q!$. It suffices to bound each summand.

Put $i=2m$. For $\ell=2j$, the binary digit-sum formula gives


$$
v_2\binom{2m}{2j}=v_2\binom mj,
$$


and


$$
v_2((2m-2j)!)=(m-j)+v_2((m-j)!).
$$


The summand valuation is therefore at least


$$
v_2\binom mj+v_2(j!)
 +(m-j)+v_2((m-j)!)
=v_2(m!)+(m-j).
$$



For $\ell=2j+1$, with $j\le m-1$, use


$$
\binom{2m}{2j+1}
=\frac{2m}{2j+1}\binom{2m-1}{2j}.
$$


Since


$$
v_2\binom{2m-1}{2j}=v_2\binom{m-1}{j},
$$


the valuation lower bound becomes


$$
v_2(m!)+(m-j)+v_2(j+1)\ge v_2(m!).
$$



Now put $i=2m+1$. For both $\ell=2j$ and $\ell=2j+1$,


$$
v_2\binom{2m+1}{\ell}=v_2\binom mj.
$$


The even-$\ell$ lower bound is


$$
v_2(m!)+(m-j),
$$


and the odd-$\ell$ lower bound is


$$
v_2(m!)+(m-j)+v_2(j+1).
$$


All summands have valuation at least $v_2(m!)$. Summation proves (10.1). ∎

This proof includes the binomial factor $\binom i\ell$; dropping it would miss the clean factorial envelope.

### Sharper forcing cutoff

Let


$$
m_p=\min\{m\ge0:v_2(m!)\ge p\}.
$$


Then


$$
\boxed{F_i\equiv0\pmod{2^p}\qquad(i\ge2m_p).}
$$


This is substantially sharper than $i<6p$.

Likewise, the bounds (9.1) allow a sharper central-index screen: even index $2j$ needs $v_2(j!)<p$, and odd index $2j+1$ needs $v_2((j+1)!)<p$.

## 11. Arbitrary contact orders and coefficient-valued inversion

The contact symbol is


$$
\phi^n=(1+2U)^h,
\qquad
U=\sum_{s=1}^{4}u_sz^{[s]},
\quad (u_1,u_2,u_3,u_4)=(-1,2,-3,3).
$$



The divided-power algebra is integral: products introduce integer multinomial coefficients. Consequently, its order-$r$ contribution


$$
2^r\binom hr U^r
$$


has valuation at least $r$ and degree at most $4r$. Thus $r\ge p$ can be omitted modulo $2^p$.

For the suffix operator, the endpoint remains $b-1$:


$$
\mathscr T_{v,b}f(y)
=\sum_{z=y}^{b-1}
\binom{v+z-y-1}{v-1}f(z).
$$


Its polynomial continuation has degree at most $\deg f+v$ in $y$. Multiplication by $\binom{x}{s-v}$ gives


$$
\deg\mathscr C_s f\le\deg f+s.
$$



At an actual row $0\le x<b$, any nonzero term has $s-v\le x$, so


$$
y=x-s+v\ge0.
$$


There is no hidden use of negative-index matrix rows in the finite-row identity.

Under the accepted integral Newton transport, the complete $\mathscr K_p$ maps the Newton coefficient lattice into twice itself. Hence


$$
P_p=\sum_{q=0}^{p-1}(-\mathscr K_p)^qg_p
$$


satisfies


$$
(I+\mathscr K_p)P_p-g_p
=(-1)^{p-1}\mathscr K_p^pg_p
\in2^p\operatorname{Int}(\mathbb Z_2).
$$



This is a valid coefficient-valued inverse residual, not merely a finite matrix-row test.

### Finite-vector versus polynomial coefficients

For arbitrarily large $p$, the polynomial degree may exceed the finite matrix dimension $b$. One must not infer equality of every formal polynomial coefficient from equality at the $b$ matrix rows.

For coefficient $380$, however, the original $b$ is always greater than $380$. Its Newton coefficient is determined by rows $0,\ldots,380$ through finite differences. Thus equality at the actual rows is sufficient for this particular coefficient. The polynomial-continuation construction is a useful lift; it should not be confused with uniqueness of all coefficients above the finite boundary.

## 12. The corrected degree bounds

### First correction: contact precision cannot be spent repeatedly

A term involving successive contact orders $r_1,\ldots,r_q$ has valuation at least


$$
R_c=r_1+\cdots+r_q
$$


and degree increment at most $4R_c$.

It survives modulo $2^p$ only if $R_c\le p-1$, before charging any valuation of its input. Therefore, even using A5’s conservative $\deg g_p\le6p-1$,


$$
\boxed{\deg P_p\le10p-5\pmod{2^p}.}
\tag{12.1}
$$



This already gives


$$
d_{16}\le155,\qquad d_{32}\le315.
$$


Thus coefficient $380$ is excluded at both precisions without a large computation.

### Proposition 2 — sharp envelope from the stated force bounds

Assume (9.1) and the accepted integral contact transport. Modulo $2^p$, $P_p$ has a representative of Newton degree at most


$$
\boxed{4p-1.}
\tag{12.2}
$$



### Proof

The input term $F_i\binom xi$ has valuation at least $w_i$ from (10.1). A contact word of total order $R_c$ can survive only if


$$
w_i+R_c\le p-1.
$$


Its degree is at most


$$
i+4R_c
\le4(p-1)+(i-4w_i).
$$



Write $i=2m$ or $2m+1$. Since


$$
v_2(m!)\ge\left\lfloor\frac m2\right\rfloor,
$$


we have


$$
i-4w_i
\le2m+1-4\left\lfloor\frac m2\right\rfloor
\le3.
$$


Thus every surviving term has degree at most $4p-1$. ∎

The value $3$ is attained in this lower-bound optimization, for example at $i=3$. Thus $4p-1$ is the sharp envelope obtainable from these particular uniform valuation and degree estimates. It is **not** a claim that the actual top coefficient is nonzero: additional force or transport cancellation may sharpen the actual degree further.

## 13. Consequence for coefficient $380$

At precisions $16,32,64,95$, (12.2) gives


$$
\begin{array}{c|rrrr}
p&16&32&64&95\\ \hline
4p-1&63&127&255&379.
\end{array}
$$


Consequently,


$$
\boxed{
\mathfrak p_{380}\equiv0\pmod{2^{95}}
}
\tag{13.1}
$$


on every original index, under the stated central-force interface.

The compatible continuation, if constructed as in the next section, obeys the same bound at $k=-3$.

**Corrected computation policy:** do not request coefficient-limit evaluations at $16$, $32$, or $64$ bits to test nonvanishing. Their answers are forced to be zero by the degree estimate. Precision $96$, with degree envelope $383$, is the first not ruled out.

A related conditional actual consequence is worth recording. On a reachable branch with


$$
5\le\ell=v_2(k+3)\le97,
$$


the individual normalized $380$-term has valuation at least


$$
95+2-\ell\ge0.
$$


Thus the audited lower bound already compensates this one shift through $\ell=97$. It says nothing decisive for arbitrarily large $\ell$.

---

# IV. Continuity, compatibility, and the negative parameter

## 14. What must be proved for coefficient compatibility

Rational-polynomial evaluation is continuous on $\mathbb Q_2$, but continuity alone does not prove that two precision constructions agree modulo the smaller power of $2$.

Compatibility requires:

1. uniform central-tail divisibility;
2. uniform forcing-tail divisibility;
3. integral Newton action of every retained suffix/contact operator;
4. the coefficient-valued inverse residual.

With those ingredients, truncating at a higher precision changes the result only by a multiple of the lower modulus.

The suffix integrality extension can be justified without treating $b$ as a negative matrix dimension. For fixed degree, every coefficient is a rational polynomial in the parameters. On nonnegative integer parameters, finite sums and finite differences give integral Newton coefficients. Continuity and density then extend integrality to $\mathbb Z_2$-parameters. Equivalently, one may first prove the multivariate integer-valued polynomial identities.

Under that argument, the residues define a continuous function


$$
\mathfrak p_{380}^{*}:\mathbb Z_2\longrightarrow\mathbb Z_2.
$$


Uniform compatibility modulo $2^p$ gives uniform convergence of continuous approximants, so continuity of the limit follows.

## 15. Evaluation at $k=-3$ is not a negative-sized matrix

The substitutions are correctly


$$
k=-3,\qquad h=-95,\qquad n=-190,\qquad b=-95/2001.
$$


Since $2001$ is odd, $b\in\mathbb Z_2$.

These are parameters of polynomial continuation after the actual endpoint dependence has been encoded. They do not define a finite contact matrix with a negative number of rows.

A5 makes this distinction correctly.

The rational polynomials can have even coefficient denominators from binomial and summation polynomials. Thus “odd parameter denominator $2001$” must not be read as claiming that every ordinary-power coefficient has odd denominator. Exact rational arithmetic or explicit valuation stripping remains necessary.

## 16. The denominator-cylinder bound passes

For a finite polynomial


$$
\Pi_p(k)=\sum_a c_ak^a,
$$


define


$$
\delta_p=\max(0,-\min_a v_2(c_a)).
$$


If $\Pi_p=0$, set $\delta_p=0$.

Then $2^{\delta_p}\Pi_p\in\mathbb Z_2[k]$, and


$$
\Pi_p(k)-\Pi_p(k')
=(k-k')Q(k,k')
$$


with $2^{\delta_p}Q\in\mathbb Z_2[k,k']$. Hence


$$
v_2(\Pi_p(k)-\Pi_p(k'))
\ge v_2(k-k')-\delta_p.
$$



Therefore the claimed cylinder implication is correct:


$$
v_2(k+3)\ge p+\delta_p
\Longrightarrow
\mathfrak p_{380}(k)\equiv\Pi_p(-3)\pmod{2^p},
$$


where actual-family agreement is used on the left.

This is a finite sufficient modulus, not necessarily a minimal one.

If a future calculation yields a nonzero residue of valuation $q<p$, the resulting failure of termwise compensation follows. If the limit is zero, continuity alone still does not prove the required linear gain


$$
v_2(\mathfrak p_{380}(k))\ge v_2(k+3)-2.
$$


That distinction in A5 is correct.

---

# V. Complete second force, finite endpoints, and scalar residual

The factorial cutoff


$$
\frac{(b+a)!}{b!}\in2^p\mathbb Z_2\qquad(a\ge2p)
$$


is valid. The displayed exterior coefficients and insertion retain the actual $b+a$, not a small surrogate endpoint.

The arbitrary-order insertion has degree at most $s-1$, since each summand has degree


$$
(s-v)+(v-1)=s-1.
$$


Its sign is well defined on the original odd-$b$ family. A continuation beyond that family would require retaining the chosen parity convention, rather than treating $(-1)^b$ as an ordinary polynomial.

The logarithmic force may be omitted at the specific target


$$
T=2\mu+4,\qquad p=T+3,
$$


by the retained whole-force estimate. This is not an all-precision statement that the logarithmic force vanishes.

The exterior endpoint remains


$$
2X_b=W_b\,b\theta_{b-1},\qquad
4Y_b=W_b(1+b\eta_{b-1}).
$$


The $+1$ is indispensable.

After complete reconstruction, the outstanding norm theorem is still the whole scalar congruence


$$
\sum_{j=0}^{b}(F_j^{[p]})^2-8S(C,D)
\equiv0\pmod{2^{T+2}}.
$$


Neither the coefficient bound nor continuity at $k=-3$ proves it. In particular, all moments must be grouped before division by a moving common kernel. Individual term integrality is not equivalent to the desired grouped content or the additional norm cancellation.

---

# VI. Assessment of the coordinator’s three new exact audits

## 17. Forty-one normalized orders and six signed producer cases

The certificate contains:

* orders $1,\ldots,32$, plus $47,48,49,80,81,82,120,121,122$: $41$ orders;
* six exact signed cases $n=2,5,8,11,14,17$;
* $48$ reported direct checks of the $\gamma$-sequence.

The determinant residues agree with the retained theorem:


$$
\det\mathsf T_n\equiv
\begin{cases}
2,&n\equiv2\pmod3,\\
1,&n\equiv0,1\pmod3.
\end{cases}
$$


The displayed terminal pivots agree with the proved value $2\pmod3$.

The six signed cases corroborate the exact rank-one and force formulas. They also correctly avoid importing the original order-six producer congruence into auxiliary orders. In particular, the differing values of $v_3(\eta_n)$ and $v_3(\xi_n)$ demonstrate why auxiliary cases must not be silently assigned original-family integrality conclusions.

The receipt’s phrase “general unit/localization theorem still needs its proof” is outdated relative to the retained Turn 10 proof. The logical status is:

* the general unit theorem is supplied by that proof;
* these calculations corroborate it at $41$ finite orders;
* the calculations are not its proof.

The Turn 10 support theorem remains retained. A1’s corrected-column force remains a separate obligation.

## 18. Ninety-six full-gcd endpoint-weight probes

The counts sum correctly:


$$
21+19+28+28=96.
$$


They concern $d=2$ and $n=15,30,105,210$.

The listed values $m$ agree with $2v_p(n!)$, and every displayed companion valuation $w$ is at least $v_p(n)=1$. The variation in $w$ is consistent with the theorem being a lower bound rather than an exact universal value.

The reported direct full-gcd checks and whole-interval nonvanishing are useful finite corroboration. But the receipt does not display every probed weight, full integer numerator and denominator, or interval enclosure. I therefore accept its reported finite scope; I do not claim to have independently recomputed those outputs.

It supplies no asymptotic denominator theorem, no absence of moving resonant weights, and no replacement for the all-prime gcd.

## 19. Twelve actual reachable shift classes

The twelve cases have $\ell=5,\ldots,16$, the corrected valid threshold. Their tuples agree with


$$
(1,0,2,0;\ 0,1,0,\ell),
$$


and the displayed relative moment valuations are $2-\ell$. The mandatory multiplier is a unit in every case.

They corroborate actual original-family reachability and the fixed-moment singularity. They do not evaluate $\mathfrak p_{380}$.

The sharper coefficient envelope explains why these particular classes cannot by themselves demonstrate failure of coefficient compensation: under (9.1), the coefficient has valuation at least $95$, much more than these twelve shift losses require.

Arbitrarily deep reachability remains a theorem from LTE, not a consequence of the twelve samples.

---

# VII. Full gcd, primitive denominator, and whole error

For either two-column construction retain


$$
N_B=d_B[u,v],
$$


with the actual least clearer, and


$$
A_B=N_{B,1}^{T}\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^{T}\Omega N_{B,2}.
$$


The final normalization is


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
}
$$



No auxiliary content or single-prime calculation replaces this gcd.

For A2, writing $\delta=v_{29}(D)$, $\mu=v_{29}(M)$, the retained interface remains


$$
v_{29}(g_B)
=\min\{4F_n+4+\delta,\;2F_n+F_b+5+\mu\},
$$




$$
v_{29}(q_n)
=\max\{0,\;2F_n-F_b-1+\delta-\mu\}.
$$


The nonzero higher-tail scalar gives $\delta=\mu=3$. Its zero classes do not determine $\delta-\mu$.

For A5, with $\alpha=v_2(N)$, $\gamma=v_2(H)$,


$$
v_2(q_n)=
\max\left\{
0,\frac{3n}{2}-v_2(b!)-s_2(n)-1-(\gamma-\alpha)
\right\}.
$$


The coefficient envelope determines neither $\alpha$ nor $\gamma$.

In both families, the complete evaluated form is


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
$$


The source’s signed-error results retain their own proof status and original scope:

* A2: $\epsilon_n>0$ eventually, with exponential rate
  

$$
-\left(2+\frac1{2001}\right)n\log(1+\sqrt2)+o(n);
$$


* A5: $\epsilon_n<0$ eventually, with rate
  

$$
-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$



Real norm positivity, mixed-product nonvanishing, and eventual nonvanishing of the whole error are distinct statements. No zero modular residue disproves an asserted nonzero integer or real quantity.

An irrationality construction still needs a same-index infinite sequence with


$$
0<|q_n(e+\pi)-p_n|\longrightarrow0,
$$


using the **actual full primitive denominator**.

---

# VIII. Narrower next lemma and bounded exact arithmetic

## 20. The next mathematical lemma

For A2, the local task remains the actual relative-defect identity, not another auxiliary carry classification:

> Construct a division-safe finite-boundary current for the complete actual defect, with both endpoint currents zero and a scalar in $29\mathbb Z_{29}$, or provide a different proof controlling the defect relative to the full norm, including primitive-norm cancellation.

For A5, the immediate task can now be narrowed:

> Verify from the exact central formulas that the bounds (9.1) hold coefficientwise and uniformly, then construct the precision-filtered first solution in which input degree $i$ costs $w_i$ bits and contact order $r$ costs at least $r$ bits.

That lemma gives the $4p-1$ bound and the uniform $2^{95}$-divisibility of coefficient $380$. After it, the remaining coefficient question starts at precision $96$, not $16$.

## 21. A useful bounded calculation

### First: a formula-level certificate, not a large evaluation

**Inputs:** the exact central formulas referenced by A5, together with the displayed forcing and contact operators.

**Required verifiable output:**

1. Factorizations proving
   

$$
B_{2j}\in j!\operatorname{Int}(\mathbb Z_2),\qquad
   B_{2j+1}\in(j+1)!\operatorname{Int}(\mathbb Z_2),
$$


   with every remaining denominator accounted for.
2. Confirmation that the central summation tails are uniformly divisible by $2^p$.
3. Confirmation of the integral Newton suffix/contact action with endpoint $b-1$.

These are symbolic obligations through arbitrary indices, not finite numerical samples.

### Then, if those identities are certified: precision $96$

Use exact rational or valuation/odd-unit arithmetic to construct the filtered coefficient at


$$
h=-95,\qquad n=-190,\qquad b=-95/2001.
$$



Retain only:

* force indices satisfying $w_i<96$;
* contact words satisfying $w_i+\sum r_j<96$;
* degrees through $383$;
* the actual endpoint polynomial dependence.

**Expected verifiable output:**


$$
\boxed{\Pi_{96}(-3)\equiv0\ \text{or}\ 2^{95}\pmod{2^{96}}.}
$$


Those are the only possibilities given the proved envelope.

Also return:

* a reproducible expression for $\Pi_{96}$;
* a coefficient-valued inverse residual modulo $2^{96}$;
* a valid denominator bound $\delta_{96}$;
* compatibility with the theoretical zero residue modulo $2^{95}$.

If the residue is $2^{95}$, it certifies limiting valuation $95$ and yields the explicit cylinder


$$
v_2(k+3)\ge96+\delta_{96}
$$


on which that valuation holds. It would disprove all-depth termwise compensation for this moment on sufficiently deep reachable branches.

If the residue is zero, it proves only divisibility by $2^{96}$, and further work is required. No nonzero answer is presumed, and no runtime claim is made.

For the A2 seed compression, an optional smaller certificate needs at most $29\cdot43=1247$ field coefficients, using the corrected maximum degree $42$. Repeating the initializer or its $33$ comparisons is unnecessary.

---

# Final proof-status ledger

| Claim | Status after this audit |
|---|---|
| A2 initializer-derived coefficients | Verified from all supplied rows |
| Both higher-tail endpoints | Correct and necessary |
| Mandatory $E=2C+1$ carry | Verified |
| All-digit product and terminal factor | Correct |
| Seed degree bound | Improved to exact maximum $42$ |
| Nonzero scalar implies $v_{29}(D)=v_{29}(M)=3$ | Established at retained reconstruction scope |
| Two $z=9$ annihilating residue classes | Established; actual lower bounds $v_{29}(D),v_{29}(M)\ge4$ |
| Arbitrarily deep auxiliary blockers | Correct with finite-refinement quantifiers |
| All-depth actual defect current | Not constructed |
| A5 coefficient-valued finite inverse | Correct under retained integral transport |
| A5 $16/32$-bit coefficient screening | Coefficient $380$ excluded by precision-weighted degree |
| Sharper $\deg P_p\le4p-1$ | Proved from stated central prefactor bounds |
| Actual $\mathfrak p_{380}\in2^{95}\mathbb Z_2$ | Consequence of that interface; exact omitted central formulas still need formula-level certification |
| Continuation and compatibility at $k=-3$ | Valid with uniform tails and integral coefficient transport |
| Denominator-cylinder estimate | Correct |
| Complete binary norm residual | Still unproved |
| Three new exact audits | Finite corroboration only |
| Full primitive denominator/whole-error comparison | Still missing |

## Conclusion

The substantive new deductions are the exact seed-degree bound $42$, an additional originally reachable annihilating higher-tail class, and the precision-weighted force estimate that moves the first potentially informative coefficient-$380$ computation to **$96$ bits**.

The exact remaining local bottlenecks are:

* A2’s complete actual defect relative to the full norm, not merely auxiliary content;
* A5’s verified full central-force interface, followed by actual coefficient compensation or a complete grouped-cancellation theorem and the whole scalar residual.

The global bottleneck is unchanged: no supplied argument yet controls the full final gcd and actual primitive denominator sufficiently to make the complete nonzero evaluated error tend to zero along an infinite original sequence.



$$
\boxed{\text{The irrationality or rationality of }e+\pi\text{ remains unresolved.}}
$$


