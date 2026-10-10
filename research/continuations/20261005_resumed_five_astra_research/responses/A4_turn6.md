> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 independent audit, Turn 6

## Executive verdict

**The principal new arithmetic results in A3 Turn 2 and A2 Turn 2 pass this audit, at their stated hypotheses and with the retained reconstruction dependencies made explicit below. Neither report proves or disproves irrationality of $e+\pi$.**

The decisive conclusions are:

1. **A3’s prime-survival theorem is valid for the complete endpoint producer.** If
   

$$
p>d\ge2,\qquad p\mid n,\qquad \tau_nD_d\not\equiv0\pmod p,
$$


   then
   

$$
\boxed{v_p(\widehat q)=2v_p(n!).}
$$


   This concerns the actual primitive denominator after endpoint row contents, the shared endpoint factor, and the full final gcd. The exterior $+1$ is essential to the local calculation.

2. **A3’s infinite denominator-budget obstructions and distinct-center nonvanishing arguments are valid.** They do not supply a lower bound for the actual evaluated error. A diverging product of a denominator with an error upper-bound scale is not a lower bound for the primitive form.

3. **A2’s complete norm transfer on the 100 accepted population cylinders is valid**, using the retained precision-three natural-polynomial representation:
   

$$
\boxed{
   \frac D{29^2}\equiv
   C_n^2f(d)\sum_{k=0}^{H}(X_k/29)^2\pmod{29}.
   }
$$


   The nonadmissible fifth digits—including the shifted high-end case—must be treated as in the proof, rather than discarded using only leading Lucas support.

4. On the preferred original cylinder $t\equiv364\pmod{841}$,
   

$$
\boxed{
   D\equiv5C_n^2\mathcal T\pmod{29^4},\qquad
   D,\mathcal T\in29^3\mathbb Z_{29},
   }
$$


   and
   

$$
\boxed{
   M-(6C_n)^{-1}D\equiv0\pmod{29^4}.
   }
$$


   Both one-carry branches and both finite sum-carry branches are needed.

5. **A2’s deeper-content refinement obstruction is valid.** In particular, no finite subcylinder of the accepted population can guarantee exact norm depth two for every original index. The same argument also rules out a finite preferred-cylinder refinement guaranteeing exact norm depth three for every original index.

6. **The proposed Wilson precision-two one-carry recurrence is valid**, with precise factorial-unit notation and a concrete termination rule supplied below. The proposed 406-entry initialization remains an unperformed bounded calculation, not an original-family unit certificate.

No tools were executed. The already accepted population, universal-$\Gamma_0$, and carry-free precision-two results are reused rather than replayed.

---

# Part I. A3: complete endpoint arithmetic

## 1. Producer recurrences and finite boundaries

Retain $b=d+1$, the contact indices $0\le i,j\le d$, and reconstruction coordinates $0\le j\le b$.

Set


$$
Q(z)=1-z+\frac{z^2}{2},\qquad q_j=[z^j]Q(z)^n,
$$


with $q_j=0$ outside $0\le j\le2n$. An explicit coefficient recurrence, useful for checking the producer independently, is


$$
\boxed{
(j+1)q_{j+1}
=(j-n)q_j+\left(n-\frac{j-1}{2}\right)q_{j-1},
}
$$


with $q_0=1,q_{-1}=0$. It follows from


$$
Q(z)(Q(z)^n)'=n(-1+z)Q(z)^n.
$$



For


$$
\mathcal B_k=k![z^k](e^zQ(z)^n),
$$


differentiation gives


$$
Q(z)(e^zQ(z)^n)'
=\left(1-n+(n-1)z+\frac{z^2}{2}\right)e^zQ(z)^n.
$$


Equating exponential-generating-function coefficients yields exactly


$$
\boxed{
\mathcal B_{k+1}
=(k+1-n)\mathcal B_k
+\frac{k(2n-k-1)}2\mathcal B_{k-1}
+\frac{k(k-1)}2\mathcal B_{k-2}.
}
$$


The negative-index convention and $\mathcal B_0=1$ are correct.

Likewise, from the complete coefficient


$$
\eta_\ell=\sum_{s=0}^{\ell}\frac1{s!}
+\sum_{s=1}^{\ell}\frac{2\alpha_{s-1}}s,
$$


one obtains


$$
\boxed{
\mathcal W_\ell=\ell\mathcal W_{\ell-1}
+1+2(\ell-1)!\alpha_{\ell-1},
\qquad \mathcal W_0=1.
}
$$


This recurrence retains both force components.

The row-scaled system is therefore


$$
C_{ij}=(n+i)^{\underline j}\mathcal B_{n+i-j},
$$




$$
z_i=(n+i)!\,n!\,[z^{n+i}]
\frac{Q(z)^n}{(1-z)^{n+1}},
$$




$$
w_i=\sum_{j=0}^{\min(2n,n+i)}
q_j(n+i)^{\underline j}\mathcal W_{2n+i-j}.
$$


The highest required $\mathcal W$-index is $2n+d$. Under the prime theorem’s hypotheses, $n\ge p>d$, so the stated row-scaling identity has no negative-index ambiguity.

With $x=C^{-1}z,\ y=C^{-1}w$, the endpoints are


$$
\boxed{
u_0=-s^Tx,\quad u_b=x_d,\qquad
v_0=1-s^Ty,\quad v_b=y_d,
}
$$


where $s_j=(-1)^jn^{\overline j}$.

**Audit finding:** the endpoint $+1$, the full force, and the actual finite contact inverse have all been preserved. The adjugate formulation and Schur-complement endpoint update are algebraically correct; the latter requires its displayed intermediate pivots to be nonzero.

---

## 2. Proof of exact local prime survival

Let


$$
N_p=v_p(n!),\qquad p>d\ge2,\qquad p\mid n.
$$



### 2.1 Contact invertibility

Frobenius gives $q_j\equiv0\pmod p$ for $1\le j<p$. Every falling factorial of length at least $p$, when present, is divisible by $p$. Thus


$$
\mathcal B_k\equiv1\pmod p,
\qquad
C_{ij}\equiv i^{\underline j}\pmod p.
$$


Consequently,


$$
\det C\equiv\prod_{i=0}^{d}i!\not\equiv0\pmod p.
$$


The finite matrix is invertible, and $C^{-1}$ is $p$-integral.

### 2.2 First-column endpoint valuations

The coefficient series used in the first force is constant modulo $p$ across the relevant block of $p$ consecutive indices. Hence


$$
\frac{z_i}{(n!)^2}\equiv i!\tau_n\pmod p.
$$


The triangular system


$$
\sum_{j=0}^{i}i^{\underline j}X_j=i!
$$


has solution $X_j=D_j/j!$, because


$$
\sum_{j=0}^{i}\binom ijD_j=i!.
$$


Therefore


$$
\frac{x_j}{(n!)^2}\equiv\tau_n\frac{D_j}{j!}\pmod p,
$$


and


$$
\frac{u_0}{(n!)^2}\equiv-\tau_n,\qquad
\frac{u_b}{(n!)^2}\equiv\tau_n\frac{D_d}{d!}\pmod p.
$$


Under $\tau_nD_d\not\equiv0\pmod p$,


$$
\boxed{v_p(u_0)=v_p(u_b)=2N_p.}
$$



### 2.3 Complete companion and the exterior term

For $\ell\ge2p$,


$$
v_p(\ell!)>\lfloor\log_p\ell\rfloor.
$$


Thus every term $2\ell!\alpha_{s-1}/s$ in the logarithmic part of $\mathcal W_\ell$ vanishes modulo $p$. This is a valuation argument for the complete contribution, not a replacement of the producer.

It follows that


$$
w_i\equiv\sum_{t=0}^{i}i^{\underline t}\pmod p,
\qquad y_j\equiv1\pmod p.
$$


Since $s_j\equiv0\pmod p$ for $j\ge1$,


$$
\boxed{
v_0=1-s^Ty\equiv0\pmod p,\qquad v_b\equiv1\pmod p.
}
$$


Omitting the exterior $1$ would change this calculation.

All reconstructed coordinates are $p$-integral. Hence the least actual two-column clearer has


$$
p\nmid d_B.
$$


Moreover, the unit at $v_b$ prevents a common $p$-factor in the cleared two-column array.

### 2.4 Every endpoint gcd factor

Write


$$
t_p=\min\{2N_p,v_p(v_0)\},
$$


with the usual convention for $v_0=0$. Then $1\le t_p\le2N_p$, and primitive row reduction gives


$$
v_p(r_0)=t_p,\qquad v_p(r_b)=0,
$$




$$
v_p(h)=2N_p-t_p,\qquad
v_p(A)=0,\qquad v_p(B)=t_p.
$$


Because $\widetilde v_b$ is a unit,


$$
J=B\widetilde v_0-A\widetilde v_b
$$


is a unit.

In the source’s notation,


$$
a=n^2/\gcd(n^2,d),\qquad k=d/\gcd(n^2,d).
$$


Here $a\equiv0\pmod p$, while $k$ and $a-k$ are units. Therefore


$$
T=aJ+kA\widetilde v_b
$$


is a unit, and


$$
v_p(F)=v_p(G)=v_p(H_{\rm gcd})=0.
$$



The global endpoint formula itself is correct:


$$
\widehat q=\frac{k h|AB|}{FGH_{\rm gcd}}.
$$


Indeed, using $\gcd(A,B)=1$, endpoint row primitivity, and $\gcd(a,k)=1$, prime-by-prime reduction gives


$$
\gcd(kAB,T)=FG;
$$


the remaining cancellation is exactly


$$
\gcd\!\left(h,\frac{|T|}{FG}\right).
$$



Thus


$$
\boxed{
v_p(\widehat q)=v_p(h)+v_p(B)=2N_p.
}
$$



The raw-minor warning is also correct:


$$
v_p(U_bV_0-U_0V_b)=2N_p
=v_p(r_0r_bh),
\qquad v_p(J)=0.
$$


Its factorial divisibility has already been consumed by normalization and cannot be counted again.

---

## 3. Digit transfer, infinite subfamilies, and nonvanishing

The constant-term representation


$$
\tau_n=\operatorname{CT}(z^{-1}+1+z/2)^n
$$


proves


$$
\tau_n\equiv\prod_i\tau_{n_i}\pmod p.
$$


The reason is specific and sufficient: the exponents contributed by a single base-$p$ digit lie strictly between $-p$ and $p$, so only exponent zero can pair with the remaining multiple-of-$p$ exponents.

The displayed seeds through index ten, their residues at $3,5,7,11$, and the derangement values


$$
D_2=1,\quad D_3=2,\quad D_4=9,\quad D_8=14833
$$


are consistent with their exact recurrences. These seeds cover every digit for each of those four primes. They do not establish any claim about infinitely many seed-good primes.

Consequently the stated genuine subfamilies pass:

- $d=2,\ 105\mid n$, using $3,5,7$;
- $d=3,4,\ 385\mid n$, using $5,7,11$;
- $d=2,3,4,8,\ n=11m$, using $11$.

On the last family,


$$
v_{11}(\widehat q_{11m,d})=2v_{11}((11m)!)
$$


strictly increases. The reduced rational centers are pairwise distinct. A fixed real number can equal at most one of them, proving eventual nonvanishing of the whole error without presupposing irrationality.

### Budget versus evaluated form

A3’s estimates establish, for example,


$$
\frac{\widehat qM^{-2n-3}}n\longrightarrow\infty
\quad(d=2,\ 105\mid n).
$$


This is a genuine obstruction to making the existing sufficient upper-bound budget small.

It does **not** imply


$$
|\widehat q(e+\pi)-\widehat p|\longrightarrow\infty.
$$


The actual error could be much smaller than its proved upper bound.

The appropriate next lemma remains a quantitative lower bound for the complete signed endpoint defect, with the factorial residual bounded separately. A3’s proposed defect inequality has the correct normalization and would imply the claimed exclusion result when combined with the retained endpoint magnitude law.

---

# Part II. A2: actual depth-two and depth-three norm arithmetic

## 4. Scope of the reconstruction input

Retain exactly


$$
a=432827+682892t,\quad t\ge0,\quad
b=3^a,\quad n=2001b,
$$


the coordinates $0\le j\le b$, the contact indices $0\le i,j<b$, and the falling metric.

The present audit uses the retained representation


$$
P_{LJ+x}\equiv(-1)^{j+1}F(J)P_x(J)\pmod{p^3},
$$




$$
Q_{LJ+x}\equiv(-1)^{j+1}F(J)Q_x(J)\pmod{p^3},
\qquad p=29.
$$


Its scope includes the complete factorial boundary, the unfrozen $LJ\,W_jB_{-2}(j)$ insertion, the whole-force logarithmic valuation bound, and the exterior endpoint.

These construction identities are not newly inferred from the population calculation or from the older finite convolution certificate.

On the accepted population $p\mid F(J)$, division by $p$ gives


$$
P_{LJ+x}/p
\equiv(-1)^{j+1}(F(J)/p)P_x(J)\pmod{p^2}.
$$


There is no division by a possibly nonunit $F(J)$.

For $x>b_*$, the factor $h-J$ permits extension to $J=h$ with zero added contribution. Outside the leading support, $P_x\equiv0\pmod p$, so the normalized square vanishes modulo $p^2$; this includes the actual endpoint $j=b$.

Therefore


$$
\boxed{
D/p^2\equiv
C_n^2\sum_{J=0}^{h}K_d(J)(F(J)/p)^2\pmod p.
}
$$



---

## 5. Nonadmissible fifth digits and the shifted high end

Write $J=pk+s$. The actual ranges remain


$$
k\le H\quad(s\le d),\qquad k\le H-1\quad(s>d).
$$



For admissible $s$,


$$
0\le s\le3,\qquad0\le d-s\le22,
$$


first-level stripping gives


$$
F(pk+s)/p\equiv
\binom3s\binom{d-s+6}{6}(X_k/p)\pmod p.
$$



The nonadmissible table passes. After the low carry is removed, its first three single-carry cases contain respectively


$$
(2A+H-k+1)X_k,\quad (A-k)X_k,\quad (H-k)X_k.
$$


They vanish modulo $p$ by population content. The two-low-carry case also vanishes.

The final shifted case is the important one:


$$
(A-k)\binom Ak
\binom{2A+H-k-1}{H-k-1}.
$$


Let $r=k\bmod p$, $a_0=A\bmod p$, and $z=H\bmod p$.

- If $r>a_0$, the first binomial vanishes.
- If $r=a_0$, $A-k$ vanishes.
- If $r<a_0$, then $r<z$, and
  

$$
2a_0+z-1-r\ge a_0+z\ge p.
$$


  The second binomial has a low carry.

Here $k\le H-1$ is preserved, so $H-k-1\ge0$. No fictitious terminal summand is introduced.

This proves the complete transfer


$$
\boxed{
D/p^2\equiv C_n^2f(d)
\sum_{k=0}^{H}(X_k/p)^2\pmod p
}
$$


on all 100 accepted classes. The unit assertion for $f(d)$ uses its accepted finite table at $0\le d\le24$.

---

## 6. Preferred-cylinder one-carry quotients and antisymmetry

On $t\equiv364\pmod{841}$,


$$
H=20+pG,\qquad A=9+pB,\qquad B\equiv19\pmod p.
$$


Put


$$
Y_m=\binom Bm\binom{2B+G-m}{G-m}.
$$



For $k=pm+s$, the two single-carry ranges give


$$
X_{pm+s}/p\equiv
\begin{cases}
u_s(2B+G-m+1)Y_m,&0\le s\le9,\\
u_s(B-m)Y_m,&10\le s\le20,
\end{cases}
$$


where


$$
u_s=-\frac{9!}{18!\,s!\,(20-s)!}.
$$


The remaining $21\le s\le28$ have two low carries and vanish after normalization modulo $p$. Both contributing ranges retain $0\le m\le G$.

The common $u_s$ formula in both branches is correct: reflection of the complementary factorial below $p$ produces the same sign and denominator.

The low sums are


$$
\sum_{s=0}^{9}u_s^2=10,\qquad
\sum_{s=10}^{20}u_s^2=19=-10.
$$


Hence, writing $S=\sum(X_k/p)^2$,


$$
S\equiv10(G+20)\sum_{m=0}^{G}(G-2m)Y_m^2\pmod p.
$$



### Finite antisymmetry

Write $G=pR+z,\ m=pq+s$, and let


$$
\varepsilon=\mathbf1_{s>z},\qquad l=z-s+p\varepsilon.
$$


Nonzero terms require $s,l\le19$. For each fixed $\varepsilon$, their low squared weight is


$$
\binom{19}{s}^2\binom{19}{l}^2,
$$


and their high factor is independent of $s,l$. The high range is


$$
q\le R\quad(\varepsilon=0),\qquad
q\le R-1\quad(\varepsilon=1).
$$


The involution $(s,l)\leftrightarrow(l,s)$ preserves each range and changes


$$
G-2m\equiv l-s
$$


to its negative. Each branch therefore cancels separately, including its high endpoint.

Thus


$$
\boxed{S\equiv0\pmod p,\qquad \mathcal T\in p^3\mathbb Z.}
$$



The weighted version


$$
\sum_{k=0}^{H}k(X_k/p)^2\equiv0\pmod p
$$


also follows: the two weighted low sums are negatives of each other, so the same antisymmetric high contraction applies.

---

## 7. $D\bmod p^4$ and $M\bmod p^4$

Let $Z_k=X_k/p$. Only $J=pk$ survives in the normalized norm modulo $p^2$. Exact first-level unit stripping gives


$$
F(pk)/p\equiv
Z_k[1+p(H\mathsf H_6+k(\mathsf H_3-\mathsf H_6))]
\pmod{p^2}.
$$


With


$$
\mathsf H_6=1,\qquad \mathsf H_3-\mathsf H_6=25,
$$


and


$$
\widetilde K(pk)\equiv5+p(4-k)\pmod{p^2},
$$


the product is


$$
\widetilde K(pk)(F(pk)/p)^2
\equiv Z_k^2[5+p(1+17k)]\pmod{p^2}.
$$



The unknown ordinary low correction contributes


$$
pV_P(0)\sum Z_k^2,
$$


which vanishes modulo $p^2$. The constant and first-moment corrections also vanish by the two cancellations just proved. Therefore


$$
\boxed{D\equiv5C_n^2\mathcal T\pmod{p^4}.}
$$



For the mixed product, the accepted ordinary-polynomial identity gives


$$
\sum_x(P_xQ_x-rP_x^2)
\equiv p(27C_n+20J_{29})K_d(J)\pmod{p^2},
$$


where $r=(6C_n)^{-1}$.

Because both actual columns are divisible by $p$, their representation errors modulo $p^3$ affect scalar products only modulo $p^4$. Consequently, on all 100 classes,


$$
M\equiv(r+p\lambda)D\pmod{p^4},
\qquad
\lambda=(27C_n+20J_{29})/C_n^2\pmod p.
$$


On the preferred cylinder $p^3\mid D$, so


$$
\boxed{M-rD\equiv0\pmod{p^4}.}
$$



Thus a unit $\mathcal T/p^3$ at an actual index implies


$$
v_p(D)=v_p(M)=3.
$$


If it vanishes, the formulas establish only that both valuations are at least four.

---

## 8. Deeper-content extensions: a stronger consequence

The source’s digit-extension argument is valid. After fixing $H\bmod p^m$, choose the next free digits so that


$$
A_{m+1}=2,\qquad H_{m+1}=28.
$$


This is possible because the relevant affine coefficient is $69\equiv11\pmod{29}$, a unit.

At that digit, the digit of $2A$ is $4$ or $5$. If neither defining binomial of $X_k$ had an outgoing carry there, then


$$
k_{m+1}\le2,\qquad l_{m+1}\le24.
$$


Even allowing an incoming sum carry,


$$
k_{m+1}+l_{m+1}+\sigma\le27,
$$


contradicting the digit $H_{m+1}=28$.

This forces a second binomial carry at a position distinct from the population’s first-digit carry. Hence every $X_k$ is divisible by $p^2$. The fifth-digit quotient formulas then give $p^2\mid F(J)$, and the actual representations imply


$$
P,Q\in p^2\mathbb Z_p^{b+1},\qquad D,M\in p^4\mathbb Z_p.
$$


The accepted LTE bijection transfers this finite extension to original nonnegative $t$.

**Additional consequence of this audit:** on the preferred cylinder, no finite refinement can guarantee


$$
D/p^3\in\mathbb Z_p^\times
$$


for every original continuation either. Every such refinement contains a further refinement with $p^4\mid D$.

This does not exclude exact-depth-three indices; it excludes certifying all of them by an unrestricted finite cylinder.

---

# Part III. The proposed one-carry recurrence

## 9. Factorial units, Wilson precision, and divisions

Define distinctly


$$
F_p(N)=\prod_{\substack{1\le r\le N\\p\nmid r}}r,
\qquad
\mathcal U_p(N)=N!/p^{v_p(N!)}.
$$


Then


$$
F_p(pm+r)\equiv(28!)^m r!(1+pm\mathsf H_r)\pmod{p^2},
$$


and


$$
\mathcal U_p(N)=F_p(N)\mathcal U_p(\lfloor N/p\rfloor).
$$


The recursive factor must not be omitted.

For a complete path, the exponents of $28!$ in the two factorial ratios at level $i$ are respectively $\beta_{i+1}$ and $\gamma_{i+1}$. Squaring therefore gives exactly the source’s factor


$$
(28!)^{2(\beta_{i+1}+\gamma_{i+1})}.
$$


Keeping $28!\bmod841$, rather than replacing it by $-1$, is necessary.

The adjacent-digit harmonic expression uses the actual digits of


$$
A,\quad 2A+l,\quad k,\quad A-k,\quad 2A,\quad l.
$$


It remains valid when a carry occurs. Thus the path formula


$$
(X_k/p)^2\equiv
\prod_i g_i\left(1+2p\sum_iE_i\right)\pmod{p^2}
$$


is correct for accepted paths with exactly one total binomial carry.

Terms with two or more carries vanish in $S\bmod p^2$; on the population there are no zero-carry terms. Therefore the selection is exact at this scope.

All factorial denominators in $g_i$ are units. The divisions by $p$ in $X_k/p$, $S/p$, and initialization weights are justified separately by content or proved cancellation—not by modular inversion of $p$.

## 10. Compression and drain

The six-component harmonic accumulator is sufficient because the correction is linear in the next digit tuple. The displayed $W,Z$ updates remain valid after merging paths.

For a fixed $H,d$, affine and doubling carries are deterministic. Only the sum carry, binomial borrow/carry, and accumulated carry count branch.

A concrete safe termination rule is:

1. Process all digits of $H$, generating $A$ and $2A$ by the affine and doubling recurrences.
2. Append four zero input digits.
3. Accept only
   

$$
\sigma=\beta=\gamma=0,\qquad v=1.
$$



Three zero inputs drain the affine and doubling carries as in the accepted recurrence. The fourth zero digit closes the last adjacent-digit harmonic term. A terminal borrow is rejected; an outgoing binomial carry at a zero-top stage would violate the one-carry budget on this population.

The resulting terminal $W$ is exactly $S\bmod841$.

## 11. Two-layer initialization

The proposed inputs


$$
H_0,H_1=(20,z),\quad A_0,A_1=(9,19),\quad
(2A)_0,(2A)_1=(18,9)
$$


are correct.

After the first digit, a surviving path has already spent its unique binomial carry. After the second digit, survival forces $\beta=\gamma=0$, leaving only $\sigma=0,1$.

The assertion


$$
W_\sigma(z)\equiv0\pmod{29}
$$


for each boundary state is justified by the branchwise antisymmetry proved above, not merely by cancellation after summing over unknown high continuations. Thus


$$
r_\sigma(z)=W_\sigma(z)/29\bmod29
$$


is a legitimate exact division.

At the third digit, $W\bmod29=0$, so new harmonic accumulators vanish. The retained initialization $Z_\sigma(z)$ still contributes once through


$$
g[r_\sigma(z)+2\tau\cdot Z_\sigma(z)].
$$


Thereafter ordinary carry-free weights modulo $29$ suffice, with the actual terminal boundary retained.

---

# Part IV. Primitive denominators, remaining bottlenecks, and bounded calculation

## 12. No local content may bypass the final gcd

For A2 retain


$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
$$


With $\delta=v_{29}(D)$, $\mu=v_{29}(M)$,


$$
v_{29}(g_B)=
\min\{4F_n+4+\delta,\ 2F_n+F_b+5+\mu\},
$$




$$
\boxed{
v_{29}(q_n)=
\max\{0,2F_n-F_b-1+\delta-\mu\}.
}
$$


Exact common depth three therefore does not create a new favorable relative valuation:


$$
\delta=\mu=3
\quad\Longrightarrow\quad
v_{29}(q_n)=\max\{0,2F_n-F_b-1\}.
$$



For both constructions, preserve the whole evaluated errors:


$$
\widehat q(e+\pi)-\widehat p
=\widehat q(e+\pi-\widehat c),
$$




$$
q_n(e+\pi)-p_n=-q_n\epsilon_n.
$$


The retained analytic assertions keep their source hypotheses and proof status. No logarithmic force, exponential residual, contact boundary, or exterior endpoint has been removed from these real quantities.

---

## 13. Exact remaining mathematical bottlenecks

### A3

Prove quantitative separation from the endpoint cancellation threshold, for example the stated fixed-$d=2$ defect lower bound on $105\mid n$. Distinct centers prove eventual nonvanishing, but not a useful rate.

### A2

Evaluate or control


$$
\mathcal T/29^3\bmod29
$$


along the actual growing digit strings obtained from $3^a$. A nonzero finite initialization coefficient is not an actual-index unit. Moreover, a universal unit theorem on a finite cylinder is obstructed by deeper-content refinements.

On branches where the next norm digit vanishes, one needs deeper relative valuation information. A concrete next actual-column lemma is to determine the normalized defect


$$
\frac{M-(6C_n)^{-1}D}{29^4}\pmod{29}
$$


together with $D/29^4\bmod29$, at the precision required on those branches. A higher auxiliary convolution alone does not automatically supply this actual mixed-product information.

### Irrationality objective

Neither report establishes a same-index sequence of nonzero whole primitive forms tending to zero. Full all-prime denominator control remains separate from the reviewed local arithmetic.

---

## 14. Bounded exact calculation for personal inspection

The immediate useful calculation is A2’s two-layer one-carry initialization.

**Inputs**

- $p=29$, modulus $841$;
- $0!,\ldots,28!\bmod841$;
- $\mathsf H_0,\ldots,\mathsf H_{28}\bmod29$;
- $28!$ at full precision modulo $841$;
- the two input digit layers above for each $z=0,\ldots,28$;
- the audited carry, $W$, and six-component $Z$ updates.

**Expected verifiable output**

For every $z$ and $\sigma\in\{0,1\}$:

1. $W_\sigma(z)\bmod841$;
2. an exact divisibility receipt $29\mid W_\sigma(z)$;
3. $r_\sigma(z)=W_\sigma(z)/29\bmod29$;
4. the six residues $Z_\sigma(z)$.

This is 406 normalized field entries, plus the unnormalized weights and divisibility receipts, with at most 17,661 candidate two-digit paths.

For a bounded implementation cross-check, compare the complete recurrence with direct exact sums at


$$
H=20+29G,\qquad A=2001H+67,\qquad 0\le G\le28.
$$


Compute $X_k$ by exact integer arithmetic over $0\le k\le H$, and compare


$$
\sum_{k=0}^{H}(X_k/29)^2\bmod841.
$$


Any recursive computation of $X_k$ must verify exact integer division before reduction.

These are auxiliary finite tests. They do not replace original $H$ by a freely chosen small integer, establish a higher-tail theorem, or certify irrationality.

---

## Final proof-status ledger

**Accepted after independent derivation:** A3’s complete recurrences, endpoints, local clearer, full endpoint gcd, exact prime survival, digit transfer, infinite subfamilies, and distinct-center nonvanishing; A2’s complete normalized norm transfer, shifted fifth-digit vanishing, preferred-cylinder one-carry cancellation, $D$ and mixed congruences modulo $29^4$, deeper-content refinement, and Wilson precision-two recurrence.

**Clarified:** factorial-unit notation, explicit zero-digit drain, the exact scope of finite computations, and the distinction between denominator-budget failure and a lower bound for the evaluated primitive form.

**Additional deduction:** deeper-content refinements also obstruct any finite preferred-cylinder theorem asserting exact norm depth three for every original continuation.

**Still unresolved:** quantitative A3 endpoint separation; A2’s actual higher-tail norm digit and deeper relative valuations; and the all-prime primitive-denominator/error comparison needed for the research objective.



$$
\boxed{\text{The irrationality or rationality of }e+\pi\text{ remains unresolved.}}
$$


