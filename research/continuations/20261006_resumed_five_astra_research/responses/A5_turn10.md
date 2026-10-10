> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, turn 10 — The linear binary bottleneck and an exact two-center cancellation obstruction

## Executive conclusions

The historical overlap correction is substantive and is adopted throughout this report.

- **A2 turn 8, §2 already proves the complete coefficient-$4002$ ternary norm lift, nonvanishing of the complete mixed contraction, and**
  

$$
\boxed{v_3(q_n)=n-\frac{b+15}{2}=\frac{8003b-15}{2}.}
$$


  This is reused, not presented as a new discovery. The alternative residual calculation in A5 turn 9 remains a useful verification of the normalization and complete-force accounting.

- **The scale obstruction in A5 turn 9 is correct.** With the actual corrected columns and all-prime primitive reduction retained, the shallow binary guards give
  

$$
\log q_n\ge \kappa n+O(\log n),\qquad
  \kappa=2.1380226\ldots,
$$


  whereas the retained whole-error theorem has
  

$$
\beta=1.7629674\ldots.
$$


  Thus the whole primitive error diverges along every infinite original sequence in that guarded regime.

- **I do not obtain either requested original-power binary conclusion:** neither a uniform sublinear upper bound for
  

$$
\delta_2=v_2(H)-v_2(N)
$$


  nor an original subsequence with $\delta_2\ge\eta n+o(n)$, where
  

$$
\eta=0.54109\ldots.
$$


  I give an exact integral formulation of that problem and identify why a conventional resultant/gcd comparison does not supply the needed upper bound.

- **There is a further scale issue in extending the current binary producer.** The available bound for the complete logarithmic contribution protects only about
  

$$
\left(\frac12-\frac1{4002}\right)n
$$


  binary digits. This is below $\eta n$. Consequently, the established absolute omission theorem does not justify dropping that force at the newly necessary precision. This is a limitation of the proved bound, not a proof that the logarithmic contribution has exactly that valuation.

- **The new proved arithmetic obstruction concerns an explicitly defined two-center modification.** For any two distinct original centers, consider every nontrivial integer affine combination
  

$$
c_{i,j}(A)=(1-A)c_i+A c_j,\qquad A\in\mathbb Z\setminus\{0,1\}.
$$


  The complete finite inputs and actual primitive pair are derived below. There is an exact congruence that cancels the entire ternary denominator. However, cancellation forces
  

$$
|A|\ge 3^{v_3(q_j)-v_3(q_i)}.
$$


  More generally, whether or not cancellation is attempted,
  

$$
\boxed{
  q_{i,j}(A)\,|A-1|
  \ge \frac12\,3^{v_3(q_j)-v_3(q_i)}.
  }
$$


  Combining this arithmetic inequality with the retained whole-error theorem proves
  

$$
\boxed{
  |q_{i,j}(A)\epsilon_{i,j}(A)|\longrightarrow\infty
  }
$$


  uniformly over these nontrivial integer affine combinations as the lower original index tends to infinity. For the combinations that cancel the entire ternary denominator, the **unmultiplied whole error itself diverges**.

This excludes that precisely defined modification. It does **not** exclude all rational two-center combinations, does **not** yet exclude the entire original one-center family, and does **not** decide the irrationality of $e+\pi$.

---

## 1. Preserved original objects and the normalization audit

Throughout the original family is


$$
b=b(u)=9^{18+32u},\qquad n=n(u)=4002b(u),\qquad u\ge0.
$$


Contact coordinates remain


$$
0\le i,r<b,
$$


and reconstructed coordinates remain


$$
\boxed{0\le j\le b.}
$$



Put


$$
h=\frac n2,\qquad
R=2^h\binom nh,\qquad
\lambda=\frac{(n!)^2}{2^n},
$$


and retain


$$
W_j=\binom{n+2}{j},\qquad
\omega_j=(n+2)_{\underline j},\qquad
\Omega=\operatorname{diag}(\omega_j^2).
$$



Let


$$
(\mathcal R z)_j=W_j(jz_{j-1}-z_j),
\qquad z_{-1}=z_b=0.
$$


The finite contact matrix is


$$
A=\widetilde N U_n,\qquad U_n=(1+S)^n,
$$


with exactly $b$ rows and columns.

The recovered first-force identity is


$$
f=f^0/R.
$$


Its verification in A5 turn 9 follows from the exact central-coefficient formula, rather than from Gram residues, and is retained.

Writing


$$
h^{\mathrm{tot}}=h^e+h^F,
$$


the complete columns are


$$
\boxed{
Z_w=\mathcal R A^{-1}f^0,\qquad
V_w=\mathcal R A^{-1}h^{\mathrm{tot}}+e_0.
}
\tag{1.1}
$$



The second identity contains the complete terminal $+1$. Equivalently, if


$$
t=(j!)_{0\le j<b},
$$


then


$$
\mathcal Rt=-e_0+b!W_be_b
$$


and hence


$$
\boxed{
V_w=\mathcal R A^{-1}(h^{\mathrm{tot}}-At)+b!W_be_b.
}
\tag{1.2}
$$


Thus the factorial subtraction and the terminal return are both retained.

The normalized binary columns are exactly


$$
x=\frac{Z_w}{2R},\qquad
y=\frac{V_w}{4b!},
\qquad
N=x^Tx,\qquad H=x^Ty.
\tag{1.3}
$$



The prescribed final columns, denoted here by $u^{\mathrm{col}},v^{\mathrm{col}}$ to avoid collision with the original parameter, satisfy


$$
\operatorname{diag}(\omega_j)u^{\mathrm{col}}=\lambda Z_w,
\qquad
\operatorname{diag}(\omega_j)v^{\mathrm{col}}=V_w.
$$


With the actual least simultaneous clearer $d_B$,


$$
N_B=d_B[u^{\mathrm{col}},v^{\mathrm{col}}],
$$


and


$$
A_B=N_{B,1}^T\Omega N_{B,1},\qquad
H_B=N_{B,1}^T\Omega N_{B,2}.
$$



Consequently,


$$
\boxed{
A_B=d_B^2\,4\lambda^2R^2N,\qquad
H_B=d_B^2\,8\lambda Rb!H.
}
\tag{1.4}
$$


No independent row-content division is made.

The final reduction is the ordinary all-prime reduction


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
}
\tag{1.5}
$$



Define


$$
\mathscr D_n=\frac{\lambda R}{2b!}
=\frac{(n!)^2\binom n{n/2}}{2^{n/2+1}b!}.
$$


The integrality proof from A5 turn 9 applies, giving


$$
\boxed{
\mathscr D_n\in\mathbb Z_{>0},\qquad
\frac{p_n}{q_n}=\frac{H}{\mathscr D_nN}.
}
\tag{1.6}
$$


Therefore, at every prime $\ell$,


$$
\boxed{
v_\ell(q_n)=
\max\{v_\ell(\mathscr D_n)+v_\ell(N)-v_\ell(H),0\}.
}
\tag{1.7}
$$



This is the exact normalization used below. In particular, no odd factorial factor is discarded as a binary unit.

---

## 2. Reusing the historical ternary theorem

A2 turn 8, §2 proves, for the even family $b=3^a$, $n=4002b$, $a\ge1$:

1. the complete norm lift
   

$$
Z_w^TZ_w\equiv6J_0^2\pmod9;
$$


2. $J_0\equiv1\pmod3$;
3. nonvanishing of the complete mixed contraction at its stated ternary depth;
4. $v_3(d_B)=0$;
5. the actual final valuations
   

$$
v_3(A_B)=2n-15,\qquad
   v_3(H_B)=n+\frac{b-15}{2}.
$$



Thus


$$
\boxed{
v_3(g_B)=n+\frac{b-15}{2},\qquad
v_3(q_n)=n-\frac{b+15}{2}.
}
\tag{2.1}
$$



The original family is entirely within that scope.

It is useful to write


$$
d_n:=v_3(q_n)
=\left(1-\frac1{8004}\right)n-\frac{15}{2}.
\tag{2.2}
$$


The constant $-15/2$ must be retained in an exact valuation, although it disappears from differences of two such valuations.

The ternary theorem also ensures $H\ne0$, so $\delta_2$ below is finite. It does not bound $\delta_2$.

No ternary $b=9$ computation is needed to recover this theorem.

---

## 3. Independent verification of the scale obstruction

### 3.1 The binary exponent

From (1.7),


$$
v_2(q_n)=\max\{C_n-\delta_2,0\},
\qquad
\delta_2=v_2(H)-v_2(N),
\tag{3.1}
$$


where


$$
C_n=\frac{3n}{2}-v_2(b!)-s_2(n)-1.
$$


Since $v_2(b!)=b-s_2(b)$,


$$
\boxed{
C_n=
\left(\frac32-\frac1{4002}\right)n
+s_2(b)-s_2(n)-1.
}
\tag{3.2}
$$


The digit-sum remainder is $O(\log n)$.

Under the retained separator hypotheses, including


$$
c\le22,\qquad t-c\le6,
$$


the complete-column theorem gives $v_2(N)=v_2(H)$. Hence


$$
v_2(q_n)=C_n.
$$



Combining only the actual $2$- and $3$-parts,


$$
\log q_n\ge \kappa n+O(\log n),
$$


with


$$
\boxed{
\kappa=
\left(\frac32-\frac1{4002}\right)\log2
+\left(1-\frac1{8004}\right)\log3
=2.1380226\ldots.
}
\tag{3.3}
$$



### 3.2 The whole error, not a selected component

The analytic input is the retained whole-error theorem at these same original indices:


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$




$$
\log|\epsilon_n|=-\beta n+o(n),
\qquad
\beta=\left(2+\frac1{4002}\right)\log(1+\sqrt2),
\tag{3.4}
$$


with eventual nonvanishing and its retained eventual sign.

Numerically,


$$
\beta=1.7629674\ldots,\qquad
\kappa-\beta=0.3750552\ldots>0.
$$



The evaluated primitive error is


$$
q_n(e+\pi)-p_n=-q_n\epsilon_n.
$$


Therefore, along every infinite original sequence satisfying the shallow separator guards,


$$
\boxed{
\log|q_n\epsilon_n|
\ge(\kappa-\beta)n+o(n)\longrightarrow+\infty.
}
\tag{3.5}
$$



This is a rigorous deduction from the retained analytic theorem and the exact arithmetic normalization. No logarithmic-force omission from a modular calculation is used in (3.4) or (3.5).

### 3.3 What the binary target must actually accomplish

Set


$$
\tau_3=\left(1-\frac1{8004}\right)\log3.
$$


If an infinite original sequence were to satisfy


$$
|q_n\epsilon_n|\to0,
$$


then (3.1), (2.2), and (3.4) force


$$
\boxed{
\delta_2\ge\eta n+o(n),
\qquad
\eta=\frac{\kappa-\beta}{\log2}
=0.54109\ldots.
}
\tag{3.6}
$$



This is necessary, not sufficient: all other prime contributions remain nonnegative.

For exclusion of the whole original family, the stronger assertion $\delta_2=o(n)$ is not indispensable. It would already suffice to prove


$$
\boxed{
\limsup_{\substack{u\to\infty\\ b=9^{18+32u}}}
\frac{\delta_2}{n}<\eta.
}
\tag{3.7}
$$


Indeed, a fixed margin below $\eta$ gives a positive exponential lower bound for $|q_n\epsilon_n|$.

Neither (3.7) nor the requested favorable subsequence is proved here.

---

## 4. An exact integral formulation of the outstanding binary problem

The next construction uses the actual complete finite producer. It does not replace it by a short modular presentation.

### 4.1 Full finite inputs

Let


$$
\phi(z)=1-z+\frac{z^2}{2},
\qquad
\lambda_s=s![z^s]\phi(z)^n.
$$


Then


$$
A_{ij}=
\sum_{s=0}^{n+i}
\lambda_s\binom{n+i}{s}\binom{2n+i-s}{j},
\qquad 0\le i,j<b.
\tag{4.1}
$$



The first force is


$$
f_i^0=\frac{(n+i)!}{n!}
[t^n](1+2t+2t^2)^n(1+t)^i.
\tag{4.2}
$$



For the second force, define the complete scalar sequences


$$
\mathcal D_0=1,\qquad
\mathcal D_m=m\mathcal D_{m-1}+1,
$$


and


$$
g_r=F^{(r)}(0),\qquad F'(z)=2/\phi(z),\qquad F(0)=0,
$$




$$
\mathcal L_0=0,\qquad
\mathcal L_m=m\mathcal L_{m-1}+g_m.
$$


Thus $\mathcal L_m=m!\mathcal F_m$ in the source notation. The complete forces are


$$
h_i^e=
\sum_{s=0}^{n+i}
\lambda_s\binom{n+i}{s}\mathcal D_{2n+i-s},
\tag{4.3}
$$




$$
h_i^F=
\sum_{s=0}^{n+i}
\lambda_s\binom{n+i}{s}\mathcal L_{2n+i-s}.
\tag{4.4}
$$


Every occurring factorial index lies in


$$
n\le 2n+i-s\le2n+b-1.
$$



These are finite formulas for the complete sources; no small-order force is substituted.

### 4.2 Odd determinant and globally cleared columns

Put


$$
\Delta=\det A.
$$


The integral divided-power expansion gives $\lambda_s\equiv0\pmod2$ for $s>0$. Hence


$$
A_{ij}\equiv\binom{2n+i}{j}\pmod2.
$$


The latter matrix is the finite product $P\,T(2n)$, of determinant $1$. Therefore


$$
\boxed{\Delta\ \text{is odd}.}
\tag{4.5}
$$



Define integer vectors


$$
z=\mathcal R\,\operatorname{adj}(A)f^0,
$$




$$
w=\mathcal R\,\operatorname{adj}(A)(h^e+h^F)+\Delta e_0.
\tag{4.6}
$$


They have exactly $b+1$ entries, and


$$
Z_w=z/\Delta,\qquad V_w=w/\Delta.
$$



Let


$$
\alpha_2=v_2(2R)=\frac n2+s_2(n)+1,
\qquad
\gamma_2=v_2(4b!)=v_2(b!)+2.
$$


The historically proved complete even normalization implies


$$
F:=z/2^{\alpha_2}\in\mathbb Z^{b+1},
\qquad
G:=w/2^{\gamma_2}\in\mathbb Z^{b+1}.
\tag{4.7}
$$


These are auxiliary global column clearings, not new row normalizations.

Write the odd positive integers


$$
r=\frac{2R}{2^{\alpha_2}},\qquad
s=\frac{4b!}{2^{\gamma_2}}.
$$


Then


$$
x=\frac{F}{r\Delta},\qquad
y=\frac{G}{s\Delta}.
$$



Set


$$
\mathcal S=F^TF>0,\qquad
\mathcal T=F^TG\ne0.
\tag{4.8}
$$


We now have the exact reduction


$$
\boxed{
\delta_2=v_2(\mathcal T)-v_2(\mathcal S).
}
\tag{4.9}
$$



The actual center is


$$
\frac{p_n}{q_n}
=\frac{r\mathcal T}{\mathscr D_n s\mathcal S}.
$$


Consequently its actual primitive denominator also has the entirely integral characterization


$$
\boxed{
q_n=
\frac{\mathscr D_n s\mathcal S}
{\gcd(\mathscr D_n s\mathcal S,\ |r\mathcal T|)}.
}
\tag{4.10}
$$


This is the same rational center as (1.5), reduced over all primes. It does not prescribe a different $d_B$, metric, or row-content operation.

### 4.3 Why the immediate resultant route does not answer the target

A standard resultant/Bezout identity for two specialized polynomial forms controls their common divisibility. Schematically,


$$
U(t)P(t)+V(t)Q(t)=\mathcal R(t)
$$


can bound


$$
\min\{v_2(P(t)),v_2(Q(t))\}
$$


after all coefficient denominators are paid.

The required quantity here is instead


$$
v_2(\mathcal T)-v_2(\mathcal S).
$$


An upper bound for their common valuation does not bound this positive difference: $\mathcal S$ may have modest valuation while $\mathcal T$ is much more divisible.

For the present complete objects, there is an additional obstacle. Their dimension, force length, and factorial normalization grow with $b$. The attached work does not supply a fixed-degree polynomial pair in $b$ whose resultant is a uniformly controlled substitute for $(\mathcal S,\mathcal T)$.

Thus a useful Bezout argument would need more than a nonzero resultant. It would need a **relative quotient identity**, with a coefficient whose binary valuation is controlled on the original powers. That identity has not been established.

Likewise, $\mathcal T\ne0$ gives only


$$
v_2(\mathcal T)\le\log_2|\mathcal T|.
$$


The source has no sublinear bound for this characteristic-zero height after the exact normalization in (4.7). Nonvanishing alone does not furnish the required binary upper bound.

---

## 5. The complete logarithmic contribution reaches the new precision question

There is a concrete reason that simply raising the precision of the old exponential-only presentation is not justified.

Split


$$
G=G_e+G_F,
$$


where


$$
G_e=
\frac{\mathcal R\operatorname{adj}(A)h^e+\Delta e_0}
     {2^{\gamma_2}},
\qquad
G_F=
\frac{\mathcal R\operatorname{adj}(A)h^F}
     {2^{\gamma_2}}.
\tag{5.1}
$$


On the original family these are integer vectors: the complete logarithmic bound supplies the required divisibility, and $G_e=G-G_F$.

Define


$$
\mathcal T_e=F^TG_e,\qquad
\mathcal T_F=F^TG_F.
$$


Then


$$
\boxed{\mathcal T=\mathcal T_e+\mathcal T_F}
\tag{5.2}
$$


is an exact complete-force decomposition, including the terminal $+1$ in $\mathcal T_e$.

Let


$$
c_F=\min_jv_2(F_j)\ge0,
\qquad
L=\left\lfloor\log_2(2n+b-1)\right\rfloor.
$$


The whole-force bound from A2 turn 8 gives


$$
v_2(h_i^F)\ge \frac n2+1-2L.
$$


Since the matrices in (5.1) are integral,


$$
\boxed{
v_2(\mathcal T_F)
\ge
c_F+\frac n2-1-v_2(b!)-2L.
}
\tag{5.3}
$$



Its certified linear coefficient, apart from $c_F$, is


$$
\frac12-\frac1{4002}
=0.4997501\ldots
<\eta.
\tag{5.4}
$$



Moreover,


$$
v_2(\mathcal S)\ge2c_F.
$$


Thus the lower bound (5.3) does not reach the precision


$$
v_2(\mathcal S)+\eta n
$$


needed to test the necessary large mixed-to-norm gap.

This proves the following limited but important statement:

> **Certified precision obstruction.**  
> The currently established absolute logarithmic omission bound does not justify omitting the complete logarithmic force at the linear binary precision required by the denominator/error comparison.

It does **not** prove that $\mathcal T_F$ first becomes nonzero near $0.49975n$. A stronger complete-force cancellation theorem could improve (5.3).

There is a parallel issue with the operator truncation. The established filtration


$$
v_2(\lambda_s)\ge\lceil s/4\rceil
$$


allows truncation beyond roughly $4K$ at precision $K$. At $K\sim\eta n$,


$$
4K\sim2.16436n>2n,
$$


the full degree of the symbol. That bound therefore supplies no short symbol at the target scale. This is an efficiency limitation of the known filtration, not a mathematical impossibility theorem.

### A concrete sufficient follow-on lemma

The exact decomposition (5.2) gives a narrower sufficient target:

> **Relative exponential depth and logarithmic nonresonance lemma.**  
> Prove, uniformly on $b=9^{18+32u}$, that for some $r_n=o(n)$,
> 

$$
> v_2(\mathcal T_e)\le v_2(\mathcal S)+r_n,
> \qquad
> v_2(\mathcal T_F)>v_2(\mathcal T_e).
> \tag{5.5}
>
$$



If (5.5) holds, the ultrametric inequality gives


$$
v_2(\mathcal T)=v_2(\mathcal T_e),
$$


hence $\delta_2\le r_n=o(n)$, excluding the original approximation family under the retained whole-error theorem.

This lemma is **not proved**. Its advantage over a generic high-block request is that it names the exact complete-force contractions whose relative depth must be controlled. In particular, it cannot be discharged by another high-block parity certificate.

---

## 6. A precisely defined two-center modification

Since no linear binary conclusion is established, I now investigate a concrete modification using two actual original centers.

For original parameters $i<j$, write


$$
c_i=\frac{p_i}{q_i},\qquad
c_j=\frac{p_j}{q_j},
$$


where these are the fully primitive centers from (1.5), not raw Gram ratios.

Consider


$$
\boxed{
c_{i,j}(A)=(1-A)c_i+A c_j,\qquad A\in\mathbb Z.
}
\tag{6.1}
$$


This is an affine combination, so it preserves the coefficient of the target $e+\pi$. It is not multiplication of a center by an arbitrary scalar, and it introduces no free companion.

### 6.1 Complete finite input and actual primitive integer form

The finite inputs are precisely the two complete original producers:

- dimensions $b(i)$ and $b(j)$;
- both full corrected columns at each index;
- both complete forces at each index;
- both terminal returns;
- each prescribed metric and least clearer;
- each final all-prime gcd.

No common cutoff or shortened row range is substituted.

The integer form for (6.1) is


$$
P_A=(1-A)p_iq_j+A p_jq_i,
\qquad
Q_A=q_iq_j.
\tag{6.2}
$$


Its actual primitive reduction is


$$
\boxed{
g_A=\gcd(Q_A,|P_A|),\qquad
q_A=Q_A/g_A,\qquad
p_A=P_A/g_A.
}
\tag{6.3}
$$



Although $Q_A$ is a product denominator, every extraneous common factor is removed in (6.3). No conclusion below is based on treating $Q_A$ as the primitive denominator.

The complete evaluated error is exactly


$$
\boxed{
\epsilon_A=c_{i,j}(A)-(e+\pi)
=(1-A)\epsilon_i+A\epsilon_j.
}
\tag{6.4}
$$


Thus


$$
q_A(e+\pi)-p_A=-q_A\epsilon_A.
\tag{6.5}
$$



---

## 7. New arithmetic theorem: ternary cancellation has an unavoidable coefficient cost

Let


$$
d_i=v_3(q_i),\qquad d_j=v_3(q_j),\qquad D=d_j-d_i>0.
$$


Write


$$
q_i=3^{d_i}s_i,\qquad q_j=3^{d_j}s_j,
\qquad 3\nmid s_is_j.
$$


Since the original fractions are primitive and $d_i,d_j>0$,


$$
3\nmid p_ip_j.
$$



From (6.2),


$$
P_A=
3^{d_i}
\left(
3^Dp_is_j
+A\bigl(p_js_i-3^Dp_is_j\bigr)
\right).
\tag{7.1}
$$


Put


$$
U=p_js_i-3^Dp_is_j.
$$


Then


$$
\boxed{3\nmid U.}
\tag{7.2}
$$



### Theorem 7.1 — Exact full-cancellation congruence

The actual primitive denominator $q_A$ is a ternary unit if and only if


$$
\boxed{
A\equiv-3^Dp_is_j\,U^{-1}\pmod{3^{d_j}}.
}
\tag{7.3}
$$


Every such integer $A$ satisfies


$$
\boxed{v_3(A)=D,\qquad |A|\ge3^D.}
\tag{7.4}
$$



#### Proof

Since


$$
v_3(Q_A)=d_i+d_j,
$$


the primitive denominator has no factor $3$ precisely when


$$
v_3(P_A)\ge d_i+d_j.
$$


By (7.1), this is equivalent to


$$
3^Dp_is_j+AU\equiv0\pmod{3^{d_j}},
$$


which is (7.3), because $U$ is a ternary unit.

Here $D=d_j-d_i<d_j$, and $p_is_jU^{-1}$ is a unit. Therefore the residue in (7.3), and every integer representative of it, has exact valuation $D$. This proves (7.4). ∎

Thus full ternary cancellation is arithmetically possible in this modification. It is not free: its integer coefficient must already have exponential size in the difference of the original indices’ ternary denominator exponents.

### Theorem 7.2 — Uniform denominator/coefficient tradeoff

For every $A\in\mathbb Z\setminus\{0,1\}$,


$$
\boxed{
q_A\,|A-1|\ge\frac12\,3^D.
}
\tag{7.5}
$$



#### Proof

Let $a=v_3(A)$.

If $a<D$, the two terms inside the parentheses in (7.1) have distinct valuations $D$ and $a$. Hence


$$
v_3(P_A)=d_i+a,
$$


so the actual primitive denominator satisfies


$$
v_3(q_A)=d_j-a.
$$


Also, for every integer $A\ne0,1$,


$$
|A-1|\ge\frac12|A|\ge\frac12\,3^a.
$$


Therefore


$$
q_A|A-1|
\ge3^{d_j-a}\frac{3^a}{2}
=\frac12\,3^{d_j}
\ge\frac12\,3^D.
$$



If $a\ge D$, then


$$
|A-1|\ge\frac12|A|\ge\frac12\,3^D,
$$


while $q_A\ge1$. This proves the second case. ∎

The proof retains the actual all-prime gcd. Other primes can only make $q_A$ larger than the ternary lower bound used in the first case.

---

## 8. The whole-error consequence for original powers

The preceding arithmetic becomes decisive because consecutive original indices are extremely far apart:


$$
\boxed{
\frac{n(j)}{n(i)}
=9^{32(j-i)}.
}
\tag{8.1}
$$



The retained error theorem gives


$$
\log|\epsilon_k|=-\beta n(k)+o(n(k)).
$$


It follows that, uniformly for $j>i$,


$$
\left|\frac{\epsilon_j}{\epsilon_i}\right|\longrightarrow0
\qquad(i\to\infty).
\tag{8.2}
$$


For example, bounding the two $o(n)$ terms by $\beta n/4$ proves this immediately from (8.1).

For all sufficiently large $i$, the ratio in (8.2) is at most $1/4$. Since


$$
|A|\le2|A-1|\qquad(A\in\mathbb Z\setminus\{0,1\}),
$$


equation (6.4) gives


$$
\boxed{
|\epsilon_A|
\ge\frac12\,|A-1|\,|\epsilon_i|.
}
\tag{8.3}
$$


In particular, the whole error is nonzero. More precisely,


$$
\epsilon_A=(1-A)\epsilon_i(1+o(1)),
\tag{8.4}
$$


uniformly in these integer coefficients.

Combining (7.5) and (8.3),


$$
|q_A\epsilon_A|
\ge\frac14\,3^D|\epsilon_i|.
\tag{8.5}
$$



By the historical ternary law,


$$
D=d_j-d_i
=\left(1-\frac1{8004}\right)(n(j)-n(i)).
$$


Therefore


$$
\boxed{
\log|q_A\epsilon_A|
\ge
\tau_3(n(j)-n(i))
-\beta n(i)+o(n(i))-\log4.
}
\tag{8.6}
$$



The coefficient is positive uniformly for $j>i$. Indeed, even the much weaker ratio $n(j)/n(i)\ge9$ would suffice:


$$
8\tau_3-\beta>0.
$$


The actual ratio is at least $9^{32}$.

We have proved:

### Theorem 8.1 — No-go for nontrivial integer affine two-center combinations

Assume the retained whole-error theorem at the original indices. For every choice


$$
i\to\infty,\qquad j>i,\qquad
A=A(i,j)\in\mathbb Z\setminus\{0,1\},
$$


the actual primitive combinations (6.2)–(6.3) satisfy


$$
\boxed{
|q_A\epsilon_A|\longrightarrow\infty.
}
\tag{8.7}
$$



This holds without any binary guard and without any upper bound on the integer coefficient $A$.

### Corollary 8.2 — Full ternary cancellation destroys even unmultiplied decay

If $A$ is chosen to satisfy the exact cancellation congruence (7.3), then


$$
|A|\ge3^D,
$$


and (8.3) implies


$$
|\epsilon_A|\ge\frac14\,3^D|\epsilon_i|
$$


for all sufficiently large lower indices. Consequently,


$$
\boxed{|\epsilon_A|\longrightarrow\infty.}
\tag{8.8}
$$



Thus this modification does provably cancel the ternary factorial factor, but it cannot retain a decaying whole error.

### Scope of the obstruction

This is a theorem about the explicitly defined integer affine family (6.1).

It is not a theorem about arbitrary rational affine weights. A rational weight can have a large independent denominator, and its cancellation and error accounting require a different primitive-pair analysis.

It is also not a theorem about every integer combination


$$
a(q_i(e+\pi)-p_i)+b(q_j(e+\pi)-p_j)
$$


after arbitrary normalization. No such unrestricted extension is inferred.

The present result is therefore narrower than an impossibility theorem for all two-center methods, but stronger than a bounded-coefficient test: it covers **every integer coefficient** in the defined family, including the exact coefficients that cancel the complete ternary denominator.

---

## 9. Proof status and the precise unresolved binary bottleneck

The situation is now:

| Statement | Status |
|---|---|
| Complete coefficient-$4002$ ternary norm lift and nonzero mixed contraction | Historical A2 turn 8 theorem, reused |
| Exact $v_3(q_n)=(8003b-15)/2$ | Historical theorem, reused |
| Exact corrected-column/final-scalar bridge | Retained and independently checked |
| Shallow-binary scale obstruction | Proved deduction from the retained whole-error theorem |
| Exact integral formulation $\delta_2=v_2(\mathcal T)-v_2(\mathcal S)$ | Proved here from the complete finite producer |
| Complete logarithmic omission reaches the necessary linear precision | **Not proved**; existing bound is insufficient |
| Uniform sublinear binary gap bound | Open |
| Original subsequence with $\delta_2\ge\eta n+o(n)$ | Open |
| Exact ternary-cancellation congruence for the defined two-center modification | **Proved here** |
| Uniform tradeoff $q_A|A-1|\ge3^D/2$ | **Proved here** |
| Failure of all nontrivial integer affine two-center combinations | Proved deduction from the retained whole-error theorem |
| Exclusion of the entire original one-center approximation family | Not proved |
| Irrationality or rationality of $e+\pi$ | Unresolved |

The original-power problem remains the valuation of the actual complete contraction


$$
\boxed{
\mathcal T
=
F^T
\frac{\mathcal R\operatorname{adj}(A)(h^e+h^F)+\Delta e_0}
     {2^{\gamma_2}}
}
$$


relative to


$$
\boxed{\mathcal S=F^TF.}
$$


A theorem about an arbitrary high word, a finite binary neighborhood, or the norm alone does not evaluate this quotient.

The existing finite high-block receipts are accepted at their stated scopes and are not proposed for repetition.

---

## 10. Bounded exact arithmetic: what is and is not needed

### 10.1 No computation is needed for the new obstruction theorem

Theorems 7.1, 7.2, and 8.1 are symbolic proofs. They require no new ternary norm receipt, high-block parity calculation, or evaluation of a new original high word.

No accepted bounded computation is being requested again.

### 10.2 A distinct, optional binary diagnostic at the relevant scale

If a new finite diagnostic is commissioned for the obstruction in §5, the useful target is **binary precision at the newly necessary linear scale**, not a rerun of the historical ternary theorem.

One precisely specified auxiliary input is


$$
\boxed{b=9,\qquad n=36018,\qquad K=20000.}
$$


This is not an original index. It is an auxiliary complete even-family input.

For this input,


$$
s_2(36018)=7,\qquad
\alpha_2=18017,\qquad
\gamma_2=9.
$$


Thus computation of the integer vectors $F,G_e,G_F$ modulo $2^{20000}$ can be made division-safe by producing their unnormalized numerators modulo


$$
\boxed{2^{38017}.}
$$



The complete inputs are:

- the full $9\times9$ matrix $A$;
- every $\lambda_s$ needed through $s=n+8=36026$;
- the exact first force (4.2);
- both full forces (4.3)–(4.4), with scalar indices through $72044$;
- the factorial subtraction, if using the residual form;
- the terminal $+\Delta e_0$, equivalently the terminal $9!W_9e_9$;
- all $10$ reconstructed rows.

Useful integer recurrences include


$$
\lambda_0=1,\qquad \lambda_1=-n,
$$




$$
\lambda_{s+1}
=(s-n)\lambda_s
+\frac{s(2n-s+1)}2\lambda_{s-1},
$$


whose displayed coefficient is an integer, and


$$
g_1=g_2=2,\qquad
g_r=(r-1)g_{r-1}
-\frac{(r-1)(r-2)}2g_{r-2}.
$$


The central coefficients $c_k=[t^k](1+2t+2t^2)^n$ can be computed exactly from


$$
c_0=1,\qquad c_{-1}=0,
$$




$$
k c_k
=2(n-k+1)c_{k-1}
+2(2n-k+2)c_{k-2},
$$


performing the indicated division in exact integers, not as an unjustified modular inverse.

**Expected verifiable output:**

1. confirmation that $\Delta$ is odd;
2. confirmation of the paid divisibilities defining $F,G_e,G_F$;
3. the residues
   

$$
\mathcal S,\quad \mathcal T_e,\quad
   \mathcal T_F,\quad \mathcal T
   \pmod{2^{20000}};
$$


4. the exact check
   

$$
\mathcal T\equiv\mathcal T_e+\mathcal T_F\pmod{2^{20000}};
$$


5. exact valuations when a residue is nonzero, and only a lower bound when it vanishes;
6. a direct comparison between reconstruction using (1.1) and the finite-subtraction/terminal form (1.2).

No numerical residues or depths are predicted here. This is an **unevaluated specification**, not a receipt. Its relevance is to test the complete logarithmic contribution beyond the currently certified omission scale. Even a successful output would establish only this auxiliary finite case, not an original-power gap theorem.

---

## Conclusion

The historical ternary denominator law is closed and must remain credited as such:


$$
\boxed{
v_3(q_n)=\frac{8003b-15}{2}.
}
$$



Together with the recovered exact scalar, it confirms that shallow binary cancellation has the wrong scale. The original one-center route needs a positive mixed-to-norm binary gap of approximately $0.54109n$, before accounting for the remaining primes.

I have not proved or excluded that gap on the original powers. The exact complete-force formulation shows why two shortcuts fail:

- a usual resultant/gcd bound controls common valuation, not the required positive valuation difference;
- the presently proved logarithmic omission bound falls below the necessary linear precision.

The new proved obstruction is different and concrete. For the explicitly defined integer affine combination of two actual original centers, complete ternary cancellation is governed by an exact congruence, but its coefficient cost overwhelms the whole error decay. More generally,


$$
\boxed{
q_A|A-1|
\ge\frac12\,3^{v_3(q_j)-v_3(q_i)}
}
$$


forces the primitive whole error to diverge for every nontrivial member of that modification family.

The remaining mathematical bottleneck is therefore still the actual complete original-power binary quotient


$$
\boxed{
v_2(\mathcal T)-v_2(\mathcal S),
}
$$


including the full logarithmic force and terminal $+1$, followed—if a favorable linear gap exists—by control of all remaining prime contributions.

No unconditional proof or disproof of the irrationality of $e+\pi$ follows.
