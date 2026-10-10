> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, Turn 16 — A one-variable adjoint contraction, and the relative residues actually certified by the supplied data

## Executive summary

The attached work does not prove or disprove the irrationality of $e+\pi$. Nor do the four original initial-value computations establish an original-family norm/mixed invariant.

There is, however, a useful specialization beyond expanding all Neumann words into many summation variables:

> **At precision $2^M$, one adjoint contact solve suffices for both the norm and the mixed contraction. Its contact correction has bandwidth at most $4(M-1)$, with a boundary correction of the same bounded rank. The norm then uses a small initial segment of the complete first force; the mixed contraction uses a one-variable polynomial moment with a differential producer of degree at most $4(M-1)$.**

The construction below:
- retains the actual finite contact boundary;
- uses only proved unit inversions;
- retains the normalized factorial tail and every logarithmic term not covered by its precision budget;
- includes the actual endpoint $W_b\mathsf a_b$;
- does not expand the second inverse or introduce one summation variable for every contact word.

This is an exact contraction reduction, **not yet a feasible original-index algorithm**. The remaining one-variable object can still have degree $b-1$. No small transfer representation for that object under $b\mapsto9^{32}b$ is proved here.

Two concrete consequences of the supplied finite arithmetic are also available:

1. At the two **auxiliary** systems, the actual relative residues are
   

$$
\boxed{\frac HN\equiv417\pmod{512}\quad(b=81),}
   \qquad
   \boxed{\frac HN\equiv17\pmod{64}\quad(b=209).}
$$


   These include the primitive-norm losses visible in the receipts.

2. At the four supplied **original** indices, the correct unit pivot is $f_1$, not $f_0$. The normalized homogeneous coefficient is
   

$$
\boxed{
   \frac{f_0}{f_1}\equiv
   7602,\ 1970,\ 4530,\ 7090\pmod{8192}
   \quad(u=0,1,2,3).
   }
$$


   These give an explicit, unit-normalized description of which actual Gram contractions must be evaluated. They do not evaluate those Gram entries.

No tools were executed.

---

## 1. Domain, normalization, and what is being reused

Throughout the original family is exactly


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
$$


The contact indices are


$$
0\le i,j<b,
$$


and reconstructed coordinates are


$$
0\le j\le b.
$$



In block notation,


$$
b=128D+81,\qquad n=128C+66,\qquad C=4002D+2532.
$$


Thus any block implementation must retain:
- full blocks $0\le t<D,\ 0\le\rho<128$;
- the shortened block $t=D,\ 0\le\rho\le80$;
- the separate endpoint $j=b$.

Write


$$
A=\widetilde N U,\qquad U=(I+S)^n,\qquad
\mathcal R=\operatorname{diag}(W_j)C,
$$


where


$$
W_j=\binom{n+2}{j},\qquad
(Cx)_j=jx_{j-1}-x_j,\qquad x_{-1}=x_b=0.
$$



The complete normalized columns are


$$
\mathsf a:=2X=\mathcal RA^{-1}f,
$$




$$
\mathsf b:=4Y=\mathcal RA^{-1}r+W_be_b,
$$


with


$$
f=f^0/R_{\rm central},\qquad
r=\frac{h^e+h^F-A(j!)_{0\le j<b}}{b!}.
$$


Consequently


$$
\mathsf a^T\mathsf a=4N,\qquad
\mathsf a^T\mathsf b=8H.
$$



I reuse the audited normalization bridge, finite displacement, complete-symbol filtration, and complete first-force factorial budgets. I do **not** assume that Turn 15’s general digit-transfer theorem has completed its independent audit. The contraction proved below does not require that theorem.

The $29$-adic arithmetic conclusions of A2turn7 are not transferred to $2$. Its finite matrix factorization is algebraic and can be adapted, but the binary integrality and unit assertions must—and below do—receive separate proofs.

---

## 2. What the supplied auxiliary residues really imply

The receipt gives complete normalized Gram residues, not merely raw factorial multiples.

### 2.1 Auxiliary system $b=81$

The supplied values are


$$
N\equiv1062\pmod{2048},\qquad
H\equiv486\pmod{1024}.
$$


Thus


$$
v_2(N)=v_2(H)=1.
$$


Dividing the two values by $2$, the available common quotient precision is $2^9$:


$$
\frac HN\equiv\frac{243}{531}\pmod{512}.
$$


Since


$$
531\equiv19\pmod{512},\qquad19\cdot27\equiv1\pmod{512},
$$


we obtain


$$
\boxed{\frac HN\equiv417\pmod{512}.}
$$



The actual column contents reported are


$$
a=\operatorname{cont}_2(\mathsf a)=1,\qquad
c=\operatorname{cont}_2(\mathsf b)=2.
$$


Therefore


$$
v_2(\mathsf a^T\mathsf a)-2a=3-2=1,
$$


and


$$
v_2(\mathsf a^T\mathsf b)-(a+c)=4-3=1.
$$


The primitive norm is **not** a unit: it has one further factor of $2$.

### 2.2 Auxiliary system $b=209$

Here


$$
N\equiv560\pmod{2048},\qquad
H\equiv304\pmod{1024},
$$


so


$$
v_2(N)=v_2(H)=4.
$$


The common quotient precision after division by $16$ is $2^6$:


$$
\frac HN\equiv\frac{19}{35}\pmod{64}.
$$


Because $35^{-1}\equiv11\pmod{64}$,


$$
\boxed{\frac HN\equiv17\pmod{64}.}
$$



The reported contents are $a=2,c=3$. Hence


$$
v_2(\mathsf a^T\mathsf a)-2a=6-4=2,
$$


and


$$
v_2(\mathsf a^T\mathsf b)-(a+c)=7-5=2.
$$



These calculations demonstrate why column primitivity cannot replace norm primitivity.

They also distinguish two possible extrapolations:

- Both auxiliary cases have $v_2(H)-v_2(N)=0$.
- They do **not** have the same relative unit modulo $64$:
  

$$
417\equiv33\not\equiv17\pmod{64}.
$$



Neither statement is an original-family theorem.

---

## 3. Using the actual original initial data with the three-column displacement

Let


$$
B_0=\mathcal RA^{-1}h^{(0)},\qquad
B_1=\mathcal RA^{-1}h^{(1)},\qquad
B_*=\mathcal RA^{-1}\tau+W_be_b,
$$


where $h^{(0)},h^{(1)}$ have initial values $(1,0),(0,1)$, and


$$
\mathcal D\tau=\mathcal Ve_b,\qquad \tau_0=\tau_1=0.
$$


These definitions retain the complete source and the actual finite displacement rows $1\le i\le b-2$.

Put


$$
\mathcal B=(B_0,B_1,B_*),\qquad G=\mathcal B^T\mathcal B.
$$


Here $G$ is the **actual binary raw Gram matrix**. No $29$-adic projection is being imported.

The displacement gives exactly


$$
\mathsf a=f_0B_0+f_1B_1,\qquad
\mathsf b=r_0B_0+r_1B_1+B_*.
$$



### 3.1 The available unit pivot

The supplied original data are


$$
(f_0,f_1)\equiv
(5954,1545),\ (4418,5641),\ (2882,1545),\ (1346,5641)
\pmod{8192}.
$$


Thus $f_0$ is not a unit, whereas $f_1$ is a unit in all four cases.

Direct integer arithmetic gives


$$
1545^{-1}\equiv2105,\qquad
5641^{-1}\equiv6201\pmod{8192}.
$$


Therefore, defining the exact binary ratio


$$
\eta=f_0/f_1,
$$


the four residues are


$$
\boxed{
\eta\equiv7602,\ 1970,\ 4530,\ 7090\pmod{8192}.
}
$$



The observed increment $2560$ modulo $8192$ is a four-value pattern only. No induction in $u$ follows from it.

### 3.2 The exact residual contraction with this pivot

Define


$$
\sigma=r_1/f_1,\qquad
\Delta=r_0-\eta r_1.
$$


Then, without division by $f_0$,


$$
\mathsf b-\sigma\mathsf a=\Delta B_0+B_*.
$$


Consequently


$$
\boxed{
\mathsf a^T\mathsf b-\sigma\,\mathsf a^T\mathsf a
=
\Delta(f_0G_{00}+f_1G_{01})
+f_0G_{0*}+f_1G_{1*}.
}
\tag{3.1}
$$



At the four supplied original indices,


$$
r_0\equiv r_1\equiv0\pmod{8192}.
$$


The basis columns are binary integral, so this proves at these indices, and at this precision only,


$$
\boxed{
4N\equiv f_1^2
\bigl(\eta^2G_{00}+2\eta G_{01}+G_{11}\bigr)
\pmod{8192},
}
\tag{3.2}
$$




$$
\boxed{
8H\equiv f_1(\eta G_{0*}+G_{1*})
\pmod{8192}.
}
\tag{3.3}
$$



These are the actual Gram channels selected by the supplied initial data. In particular, the zeros $r_0,r_1$ leave the entire third column $B_*$; they do not make the mixed output vanish.

The missing entries of $G$ cannot be reconstructed from the initial values alone.

---

## 4. Binary bounded-band factorization with the actual endpoint correction

Fix an absolute precision $2^M$. For $M>1$, set


$$
m=\min\{2n,4(M-1)\}.
$$


Use the complete-symbol expansion to choose coefficients $\lambda_s^{[M]}$ such that


$$
\lambda_s\equiv\lambda_s^{[M]}\pmod{2^M},\qquad
\lambda_s^{[M]}=0\quad(s>m).
$$


Here


$$
\lambda_0^{[M]}=1,\qquad
\lambda_s^{[M]}\in2\mathbb Z_2\quad(s>0).
$$



Let


$$
L_{ij}=\binom ij,\qquad U_{ij}=\binom n{j-i}
$$


in their triangular ranges.

The identity


$$
\binom{n+i}{s}\binom{n+i-s}{j}
=
\binom{j+s}{s}\binom{n+i}{j+s}
$$


gives


$$
(L^{-1}\widetilde N)_{ij}
\equiv
\sum_{s=0}^{m}
\lambda_s^{[M]}\binom{j+s}{s}\binom n{j+s-i}.
\tag{4.1}
$$



Define


$$
H_{kj}=
\begin{cases}
\lambda_{k-j}^{[M]}\binom{k}{k-j},
 &0\le k-j\le m,\\
0,&\text{otherwise},
\end{cases}
$$


on $0\le k,j<b$, and define the boundary matrices


$$
K_{rj}=
\begin{cases}
\lambda_{b+r-j}^{[M]}\binom{b+r}{b+r-j},
 &1\le b+r-j\le m,\\
0,&\text{otherwise},
\end{cases}
$$




$$
T^{\rm tail}_{ir}=\binom n{b+r-i},
\qquad 0\le r<m.
$$


Then


$$
L^{-1}\widetilde N\equiv UH+T^{\rm tail}K.
$$



Only the last $t_0=\min(m,b)$ columns of $K$ can be nonzero. Write


$$
K=\overline K E,
$$


where $E$ selects those actual last contact coordinates, and put


$$
F=U^{-1}T^{\rm tail},\qquad J_{\rm end}=F\overline K.
$$


The short formula


$$
F_{jr}
=
-\sum_{v=0}^{r}
\binom{-n}{b+v-j}\binom n{r-v}
\tag{4.2}
$$


follows by subtracting the missing tail from the full binomial convolution.

Thus


$$
\boxed{
A\equiv LU(H+J_{\rm end}E)U\pmod{2^M}.
}
\tag{4.3}
$$



### Unit accounting

Every off-diagonal entry of $H$, and every entry of $K$, contains a positive-index $\lambda_s^{[M]}$. Hence


$$
H\equiv I\pmod2,\qquad
J_{\rm end}\equiv0\pmod2.
$$


All triangular pivots of $H$ are exactly $1$. Every boundary Schur matrix below is congruent to the identity modulo $2$.

This is the binary justification. It does not use the $29$-adic Frobenius argument from A2turn7.

For $M=1$, the correction is empty and $A\equiv LU^2\pmod2$.

---

## 5. One adjoint solve for both scalar outputs

Once the first column $\mathsf a$ is known at the needed precision, define


$$
q=\mathcal R^T\mathsf a.
$$


Its entries are explicitly


$$
\boxed{
q_j=-W_j\mathsf a_j+(j+1)W_{j+1}\mathsf a_{j+1},
\qquad0\le j<b.
}
\tag{5.1}
$$


The last entry includes $\mathsf a_b$.

Let


$$
w=A^{-T}q.
$$


Then exact finite-dimensional duality gives


$$
\boxed{
4N=w^Tf,
}
\qquad
\boxed{
8H=w^Tr+W_b\mathsf a_b.
}
\tag{5.2}
$$



This avoids computing $A^{-1}r$. The second formula includes the true exterior endpoint, not an inferred interior substitute.

### 5.1 Explicit adjoint recurrence

Put $J=H+J_{\rm end}E$. From (4.3),


$$
A^{-T}\equiv L^{-T}U^{-T}J^{-T}U^{-T}.
$$



First form $v=U^{-T}q$. Solve $H^Tz^{(0)}=v$ backwards:


$$
\boxed{
z^{(0)}_j
=
v_j-
\sum_{s=1}^{\min(m,b-1-j)}
\lambda_s^{[M]}\binom{j+s}{s}z^{(0)}_{j+s}.
}
\tag{5.3}
$$



Let


$$
Z=H^{-T}E^T.
$$


Its $t_0$ columns satisfy the same backward recurrence with the corresponding endpoint unit-vector inputs. Then


$$
S=I_{t_0}+J_{\rm end}^TZ\equiv I_{t_0}\pmod2,
$$


and


$$
\boxed{
z=J^{-T}v
=z^{(0)}-ZS^{-1}J_{\rm end}^Tz^{(0)}.
}
\tag{5.4}
$$


The inverse can be evaluated by the finite geometric series


$$
S^{-1}\equiv
\sum_{\ell=0}^{M-1}[-(S-I)]^\ell\pmod{2^M}.
$$



Finally,


$$
w=L^{-T}U^{-T}z.
$$


The two transpose transforms have exact entries


$$
(U^{-T}z)_j
=\sum_{i=0}^{j}\binom{-n}{j-i}z_i,
$$




$$
(L^{-T}t)_i
=\sum_{j=i}^{b-1}(-1)^{j-i}\binom ji\,t_j.
\tag{5.5}
$$



Equations (5.1)–(5.5) are an explicit unit-sensitive adjoint transfer. They preserve the finite endpoints and use no division by the norm.

---

## 6. The specialized one-variable contraction

Define the actual adjoint polynomial


$$
\mathscr W(x)=\sum_{i=0}^{b-1}w_i x^i,
\qquad
\Theta=x\frac{d}{dx}.
$$


The polynomial operator


$$
\binom{n+\Theta}{s}
$$


is interpreted coefficientwise:


$$
\binom{n+\Theta}{s}\mathscr W(x)
=
\sum_{i=0}^{b-1}\binom{n+i}{s}w_i x^i.
$$


This interpretation introduces no unsafe modular division by $s!$.

### Theorem — One-variable normalized mixed contraction

Suppose $M\le K_{\rm norm}$, where


$$
K_{\rm norm}
=
1+v_2((n/2)!)-v_2(b!)
-\lfloor\log_2(2n+b-1)\rfloor.
$$


Then


$$
\boxed{
\begin{aligned}
8H\equiv{}&W_b\mathsf a_b\\
&+\sum_{\substack{a,t\ge0\\a+v_2(t!)<M}}
\ \sum_{s=0}^{4a}
\lambda_s^{(a)}\,t!\binom{b+t}{t}\\
&\hspace{12mm}\cdot
[z^{b+t}](1+z)^{2n-s}
\left[
\binom{n+\Theta}{s}\mathscr W
\right](1+z)
\pmod{2^M}.
\end{aligned}
}
\tag{6.1}
$$



Only valid source terms are included. On the usual original-index branch $M\ll n$, all displayed exponents $2n-s$ are nonnegative. If a chosen precision exceeds that range, one should use the original valid-term finite sum rather than introduce negative factorial arguments.

### Proof

For every valid $s,t$,


$$
\begin{aligned}
&[z^{b+t}](1+z)^{2n-s}
\left[
\binom{n+\Theta}{s}\mathscr W
\right](1+z)\\
&\qquad=
\sum_{i=0}^{b-1}
w_i\binom{n+i}{s}
[z^{b+t}](1+z)^{2n+i-s}\\
&\qquad=
\sum_{i=0}^{b-1}
w_i\binom{n+i}{s}
\binom{2n+i-s}{b+t}.
\end{aligned}
$$


Insert the complete normalized exponential-force truncation into (5.2) and interchange finite sums. The omitted exponential terms have depth at least $M$. The complete logarithmic force has depth at least $K_{\rm norm}$, and $w$ is integral. The endpoint term comes directly from (5.2). ∎

If $M>K_{\rm norm}$, the additional term is exactly


$$
\boxed{\sum_{i=0}^{b-1}w_i\,\frac{h_i^F}{b!}.}
\tag{6.2}
$$


It must be retained. The supplied logarithmic recurrence generates it without changing its definition.

### 6.1 The norm has a small first-force producer

The complete first-force factorial budget gives


$$
v_2(f_i)\ge v_2\!\left(\left\lfloor i/2\right\rfloor!\right).
$$


Since $w_i\in\mathbb Z_2$, define


$$
I_M=\min\left\{I:
v_2\!\left(\left\lfloor i/2\right\rfloor!\right)\ge M
\text{ for all }i\ge I
\right\}.
$$


Then


$$
\boxed{
4N\equiv
\sum_{0\le i<\min(b,I_M)}f_iw_i
\pmod{2^M}.
}
\tag{6.3}
$$


One may use the sufficient bound $I_M\le4M$.

Thus the same adjoint object supplies:
- a small-degree first-force contraction for the norm;
- genuine large-index moments for the mixed output.

This is precisely where the normalized factorial tail remains visible: the coefficient extraction in (6.1) is at $b+t$, not at a bounded substitute.

---

## 7. What this reduction accomplishes—and its exact limitation

The specialized contraction has fewer layers than the generic Turn 15 construction:

- no expansion into all Neumann words;
- no second-column inverse;
- no growing list of independent word-position variables;
- a monic band recurrence of width $O(M)$;
- an endpoint correction of rank $O(M)$;
- one actual adjoint polynomial $\mathscr W$;
- small differential producers acting on that polynomial.

However, the coefficient vector of $\mathscr W$ still has length $b$. The finite binomial transforms in (5.5) also retain their original ranges. Even linear time in $b$ would be infeasible at the smallest original $b$.

Accordingly, this report does **not** claim that (6.1) is presently feasible at an original index. It is a specialized exact reduction, not the requested completed original-family transfer invariant.

The precise obstruction is now:

> The band recurrence and bounded endpoint correction do not, by themselves, give a precision-controlled representation of the adjoint polynomial $\mathscr W$, or of its high coefficient extractions in (6.1), under the original update $b\mapsto9^{32}b$.

That is a more specific obstruction than generic evaluability.

---

## 8. Actual content losses and variable-depth targets

Let


$$
a=\min_jv_2(\mathsf a_j),\qquad
c=\min_jv_2(\mathsf b_j),
$$


and write


$$
d=v_2(\mathsf a^T\mathsf a),\qquad
e=v_2(\mathsf a^T\mathsf b).
$$


The primitive-norm and primitive-mixed losses are


$$
\nu=d-2a,\qquad \xi=e-a-c.
$$


No claim that $\nu=0$ is made.

Because


$$
\frac HN=\frac{\mathsf a^T\mathsf b}
{2\,\mathsf a^T\mathsf a},
$$


a raw residue calculation must pay the norm denominator, not just column content.

For example, if the numerator and denominator are both known modulo $2^M$, with their valuations $e,d$ certified below that precision, then the error in the reconstructed ratio has valuation at least


$$
\min\{M-d-1,\ M+e-2d-1\}.
\tag{8.1}
$$


This follows by writing the difference of two quotients over the product of their denominators.

Therefore a sufficient raw precision for the ratio modulo $2^s$ is


$$
\boxed{
M\ge
\max\{s+d+1,\ s+2d+1-e\},
}
\tag{8.2}
$$


together with $M>d,e$.

For the assignment’s variable raw target, the calculation must in any event include


$$
\boxed{M\ge2\mu+6.}
$$


A calculation at $M=13$ cannot be silently promoted to that target.

The accepted first-column truncation theorem remains available: if its replacement error has coordinate depth $T$, then the raw norm error has depth at least $T+a+1$, and the mixed error at least $T+c$. Those bounds can be used to reduce the first-column work, but they do not evaluate (6.1).

---

## 9. A concrete follow-on lemma

The next lemma should target the actual adjoint moments rather than all digit-transfer states.

### Adjoint moment quotient lemma — open

For the actual complete first column and


$$
w=A^{-T}\mathcal R^T\mathsf a,
$$


construct a precision-controlled representation of


$$
\mathscr W(x)=\sum_{i=0}^{b-1}w_i x^i
$$


sufficient to evaluate simultaneously:



$$
\sum_{i<I_M}f_iw_i,
$$


and


$$
[z^{b+t}](1+z)^{2n-s}
\left[\binom{n+\Theta}{s}\mathscr W\right](1+z),
$$


for


$$
a+v_2(t!)<M,\qquad s\le4a.
$$



The representation must:
1. retain the finite endpoint correction (5.4);
2. be stable under the actual multiplication $b\mapsto9^{32}b$, or have an explicitly evaluated defect;
3. preserve units, not merely carry support;
4. control relative precision after the actual $d,e,a,c$ losses;
5. avoid storing $b$ coefficients or enumerating $b$ rows.

A proof of this lemma would turn the specialized contraction into a plausible original-family computation. A further preserved relation between its two output channels would still be needed for a uniform norm/mixed theorem.

---

## 10. Bounded exact arithmetic worth inspecting

The next finite calculation should test the new contraction, not repeat a closed mod-$128$ table.

### Inputs

Use the two already supplied auxiliary systems:


$$
(b,n)=(81,324162),\qquad(209,836418),
$$


with $M=13$.

From the coordinator’s complete normalized data, or by regenerating those data from the displayed formulas, retain:
- the complete $\mathsf a,\mathsf b,f,r$ modulo $8192$;
- all actual endpoints;
- the complete-symbol truncation through degree $48$;
- the supplied logarithmic depth certificates.

### Computation

1. Form $q$ by (5.1).
2. Compute $w$ by the band-plus-boundary adjoint transfer (5.3)–(5.5).
3. Independently verify
   

$$
A^Tw-q\equiv0\pmod{8192}.
$$


4. Compare:
   

$$
w^Tf
   \quad\text{with}\quad
   \sum_{j=0}^{b}\mathsf a_j^2,
$$


   and
   

$$
w^Tr+W_b\mathsf a_b
   \quad\text{with}\quad
   \sum_{j=0}^{b}\mathsf a_j\mathsf b_j.
$$


5. Evaluate the right side of (6.1) by ordinary univariate coefficient arithmetic and compare it with the second scalar in step 4.
6. Report the endpoint contribution separately, without removing it from the final sum.

### Expected verifiable output

All residual differences should be zero modulo $8192$, and the final raw outputs should be



$$
\begin{array}{c|cc}
b&4N\bmod8192&8H\bmod8192\\ \hline
81&4248&3888\\
209&2240&2432
\end{array}
$$



The corresponding ratio certificates should be


$$
H/N\equiv417\pmod{512},\qquad
H/N\equiv17\pmod{64}.
$$



This is a bounded audit of the new contraction at two auxiliary systems. It would not establish an original-family scalar theorem.

For the original indices $u=0,1,2,3$, the supplied initial data already identify the channels (3.2)–(3.3). The missing calculation is the actual Gram or adjoint-moment output—not another computation of the same four initial zeros.

---

## 11. Final gcd, actual primitive denominator, and whole error

The local binary problem is not the final irrationality criterion.

Retain the least actual two-column clearer and the complete integer Gram pair:


$$
N_B=d_B[u,v],
$$




$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2}\ne0,
$$


with mixed nonvanishing reused only at its supplied original-family scope.

The final reduction remains


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad
p_n=H_B/g_B.
}
$$


This includes every prime. The primitive multiplier is


$$
d_B^2/g_B.
$$



The retained binary interface is


$$
v_2(q_n)=
\max\left\{
0,\frac{3n}{2}-v_2(b!)-s_2(n)-1-(\gamma-\alpha)
\right\},
$$


where


$$
\alpha=v_2(N),\qquad\gamma=v_2(H).
$$


Neither the auxiliary equalities $\gamma=\alpha$ nor the original initial zeros establish that equality throughout the original family.

Within the accepted complete signed-error theorem,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi)<0
\quad\text{eventually},
$$


and


$$
\log|\epsilon_n|
=
-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$


The whole evaluated form is


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n>0
\quad\text{eventually}.
}
$$


Irrationality by this route still requires a same-index estimate making this entire nonzero expression tend to zero.

---

## Conclusion and proof-status ledger

### New deductions established here

1. The supplied auxiliary Gram residues yield the relative values
   

$$
H/N\equiv417\pmod{512},\qquad H/N\equiv17\pmod{64},
$$


   with their actual primitive-norm losses exposed.

2. The supplied original initial data admit the correct unit normalization through $f_1$, giving
   

$$
f_0/f_1\equiv7602,1970,4530,7090\pmod{8192}.
$$


   Equations (3.1)–(3.3) identify the exact actual Gram channels selected by those data.

3. The binary contact inverse has an explicitly justified band-plus-boundary factorization at normalized precision.

4. A single adjoint solve gives both scalar outputs, and the complete mixed output has the one-variable contraction (6.1), including the genuine large-index kernels and endpoint.

### Not established

- An evaluated original-family norm/mixed residue.
- A preserved bilinear law under $b\mapsto9^{32}b$.
- A feasible precision-sized representation of the adjoint moment polynomial.
- A uniform primitive-norm cancellation theorem.
- The full all-prime primitive-denominator bound.

The immediate bottleneck is the **compressed, unit-sensitive transfer of the actual adjoint moments**, including their finite boundary correction. The subsequent bottleneck is their relative norm/mixed law at precision tied to the actual primitive norm. Beyond both remains the full gcd and whole-error comparison.



$$
\boxed{\text{An unconditional proof or disproof of irrationality of }e+\pi
\text{ remains unresolved.}}
$$


