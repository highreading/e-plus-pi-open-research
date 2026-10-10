> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Audit of the low-row certificate and the primitive-depth obstruction

## Abstract

The supplied zero certificate does **not** pass a direct mathematical spot check against its displayed dictionary and extraction rules.

At the single low coordinate $\ell=0$, those rules give


$$
\boxed{a_0=14,\qquad b_0^{\mathrm{prof}}=20\pmod{29},}
$$


where $b_0^{\mathrm{prof}}$ denotes the first column’s $JK$-profile, not the residue $b\bmod29^3=5044$. In particular, the assertion that all six profiles vanish is incompatible with the displayed inputs. This discrepancy is already visible in one coefficient-order-zero source atom; it does not involve an original high word, an exterior solve, or primitive content.

This does **not** prove that the final five observation coefficients are nonzero. A nonzero first-column profile can still pair to zero with the complete second-column profiles. Consequently, the whole original fixed-layer zero cannot presently be promoted from this certificate, but neither is it disproved by the spot check.

Beyond the fixed layer, I retain the supplied growing-depth complete-force theorem. I derive an exact, finite-boundary metric identity that isolates the missing source-specific alignment and its physical-terminal correction. I also give a precise limitation on attempts to obtain a bounded-content infinite subdomain merely by restricting finitely many low digits of the exponential word. Such restrictions, when attained, contain an original arithmetic progression; the retained unbounded-content theorem therefore excludes a uniform content bound on them.

No unconditional conclusion about the rationality of $e+\pi$ follows.

---

## 1. Original setting and scope

Throughout,


$$
p=29,\qquad D=p^3=24389,
$$


and the original indices are


$$
b=3^{249005515+574312172u},\qquad n=2001b,
$$


with


$$
u\ge0,\qquad u\equiv2\pmod{p^9}.
$$



The finite domains remain:

- contact coordinates $0\le j<b$;
- recurrence source rows $1\le i\le b-2$;
- reconstructed coordinates $0\le j\le b$.

Write


$$
W_j=\binom{n+2}{j},
\qquad
(\mathcal Rx)_j=W_j(jx_{j-1}-x_j),
\qquad x_{-1}=x_b=0.
$$


The actual columns are


$$
Z_w=\mathcal RA^{-1}f^0,
\qquad
Y=\mathcal RA^{-1}\mathbf r+W_be_b,
$$


where the complete recovered force is


$$
\mathbf r=A_{IE}z+\frac{h^F}{b!},
\qquad z_h=\frac{(b+h)!}{b!}.
$$



Thus the exponential subtraction, both initial charges, every recurrence source row, the finite returns, the logarithmic force formed from $F/(1-z)$, and the separate physical terminal are retained.

At the reviewed fixed layer,


$$
F=Z_w/p^4,\qquad G=Y/p^4,\qquad
\kappa=\frac{F^TG}{p^2}\pmod p.
$$



The original split is


$$
j=\ell+DJ<b,\qquad
0\le J\le
\begin{cases}
B,&\ell<5044,\\
B-1,&\ell\ge5044.
\end{cases}
$$


Nothing below changes that split or inserts $j=b$ as a contact atom.

---

## 2. A hand-checkable contradiction to the all-zero-profile claim

### 2.1 The relevant atom

The first source family in A2 Turn 1 is


$$
-\sum_{i=0}^{57}\sum_{r=0}^{i}
\widehat f_i(-1)^{b-1-r-i}
\binom{2n+r-1}{r}
\Psi_{r+1,-1-r,i-r}.
$$



The original $b$ is odd. For $i=r=0$, using $\widehat f_0=2$, the atom is therefore


$$
-2\Psi_{1,-1,0}.
$$



Its first reconstructed branch has


$$
\alpha=1,\qquad v'=-1,\qquad C_0=2.
$$


Indeed, the branch rule multiplies the atom coefficient by $(-1)^v=-1$. The second branch contains $\binom{0}{1}$, so it vanishes at $\ell=0$.

This sign calculation uses the original odd parity of $b$, not the even residue $5044$.

### 2.2 Exact low digits

At this branch,


$$
20389=(2,7,24)_{29},
$$




$$
16384+\alpha=16385=(0,14,19)_{29},
$$




$$
5044+v'=5043=(26,28,5)_{29}.
$$



At $\ell=0$, all three row digits are zero. The weight subtraction has no borrow. The lower-index subtraction also has no borrow.

The addition digits are


$$
0+26=26,
$$




$$
14+28=42=13+29,
$$




$$
19+5+1=25.
$$



Hence


$$
e=1,\qquad s=000.
$$


The branch is exactly a paid leading contribution:


$$
v_p(C_0)+e=0+1=1.
$$



No division by $p$ is required here.

### 2.3 The low unit

Formula (14.2) in A2 Turn 1 gives


$$
L
=
-\frac{13!}{14!\,28!}
 \frac{25!}{19!\,5!}
\pmod{29}.
$$



By Wilson’s theorem,


$$
\frac{13!}{14!\,28!}
=-\frac1{14}=2\pmod{29}.
$$


Also,


$$
\frac{25!}{19!\,5!}
=\frac{20\cdot21\cdot22\cdot23\cdot24\cdot25}{120}.
$$


The numerator is $15\pmod{29}$, while $120\equiv4\pmod{29}$, so this ratio is


$$
15\cdot4^{-1}=11\pmod{29}.
$$


Thus


$$
L=-2\cdot11=7\pmod{29}.
$$



The branch contributes


$$
C_0L=2\cdot7=14
$$


to $a_0$.

### 2.4 Why no other atom cancels this leading contribution at $\ell=0$

At $\ell=0$, a first reconstructed branch can survive only when its row degree is zero. Every second branch has positive row degree and vanishes.

For the first source family, degree zero requires $i=r$.

- For $1\le r<29$,
  

$$
\binom{2n+r-1}{r}\equiv0\pmod{29},
$$


  because $p\mid2n$.
- For $29\le r\le57$, the displayed head $\widehat f_r$ is divisible by $p$.

All these coefficients therefore have valuation at least one.

Their first-branch shifts are


$$
\alpha=r+1,\qquad v'=-1-r.
$$


For $0\le r\le57$, the digit-one value of $16385+r$ is $14$ or $15$, while that of $5043-r$ is at least $26$. At $\ell=0$, their addition consequently has at least one low carry. A coefficient already divisible by $p$ therefore has total order at least two and cannot change the leading profile.

The positive-symbol first source family has row degree $i+s\ge1$, so it is zero at $\ell=0$.

In the exceptional $s=29$ family, only $i=0$ has degree zero. Its coefficient is divisible by $p$, and its shifts again force a low carry, so it cannot contribute at leading order.

Finally, every displayed first return coefficient is divisible by $p$. For $0\le h\le28$, its first branch has shifts $(0,h)$. The number $16384$ has low digits $(28,13,19)$. At $\ell=0$:

- unless $(5044+h)\bmod29=0$, digit zero already carries;
- in the exceptional case $h=2$, the digit-two addition is $19+6=25$, but the return coefficient is zero in the supplied return array.

In particular, the two nonzero returns $h=0,1$ both have low carries and cannot contribute at leading order.

It follows that


$$
\boxed{a_0=14\pmod{29}.}
$$



The treatment of $h=2$ here uses the supplied explicit return value, not an invented general return-support theorem.

### 2.5 The $JK$-profile at the same coordinate

For the one leading branch,


$$
\Gamma=H_{24}+H_5-H_0-H_{25}
=H_5-\frac1{25}.
$$


Now


$$
H_5=1+15+10+22+6=25\pmod{29},
\qquad 25^{-1}=7,
$$


so


$$
\Gamma=18.
$$


Therefore


$$
\boxed{b_0^{\mathrm{prof}}=14\cdot18=20\pmod{29}.}
$$



This second nonzero profile value is obtained with the same paid extraction and the same original branch sign.

---

## 3. What the discrepancy proves—and what it does not

### 3.1 Proved discrepancy

The displayed dictionary and extraction formulas imply


$$
(a_0,b_0^{\mathrm{prof}})=(14,20).
$$


They therefore cannot produce six identically zero extracted profiles.

Grouping identical factorial-shift branches by source label does not explain this discrepancy. At $\ell=0$, the surviving unit coefficient in the relevant shift class is $2$; there is no second unit term in that class to cancel it.

The JSON certificate does not include the profile entries themselves. Its hash cannot replace those entries in a mathematical audit. Moreover, the five zero scalar coefficients and the source-pair zero crosschecks do not imply zero profiles.

I cannot determine, without execution or the actual emitted profile file, whether the discrepancy arose from a different executed file, a transcription mismatch, or an interpretation of the output. What is proved is the mathematical incompatibility of the all-zero-profile assertion with the displayed formulas.

### 3.2 No established missing unit or normalization correction

The spot check does not reveal a missing unit in formula (14.2), an unpaid division, or a wrong parity convention. On the contrary, applying those conventions as printed gives a nonzero answer.

Changing a sign to force the answer to zero would be unjustified. The issue must first be reconciled at the level of the reported calculation.

### 3.3 The five zero observation coefficients remain a separate question

The spot check does **not** prove


$$
\alpha,\delta,\lambda
$$


nonzero. For example,


$$
\alpha=\sum_\ell a_\ell g_\ell
$$


may vanish even when $a_0\ne0$.

Accordingly:

- the all-zero-profile claim is refuted;
- the final zero coefficient row is not independently validated here;
- the whole fixed-layer zero remains unpromoted from this certificate.

If a corrected audit validates


$$
\alpha=\delta=\lambda=0
$$


under the retained observable-order hypotheses, then the established formula gives


$$
\kappa=0
$$


uniformly on the original domain, without evaluating the high word.

That would be genuinely stronger than the already known implication


$$
c\ge5\Longrightarrow\kappa=0,
$$


because it would also cover original indices with smaller content. At present, that stronger conclusion is conditional.

---

## 4. An exact source-specific metric identity beyond the fixed layer

The growing-depth problem must use the actual primitive pair, not merely a larger modulus of the short dictionary.

Let


$$
\xi=A^{-1}f^0,\qquad \psi=A^{-1}\mathbf r.
$$


Thus


$$
Z_w=\mathcal R\xi,\qquad Y=\mathcal R\psi+W_be_b.
$$



Define the finite $b\times b$ matrix


$$
M=\mathcal R^T\mathcal R.
$$


Its entries can be computed directly from the original reconstruction:


$$
M_{ii}=W_i^2+(i+1)^2W_{i+1}^2,
\qquad 0\le i<b,
$$


and


$$
M_{i,i+1}=M_{i+1,i}=-(i+1)W_{i+1}^2,
\qquad 0\le i<b-1,
$$


with all other entries zero.

The last diagonal entry includes


$$
b^2W_b^2;
$$


this is the contribution from the physical coordinate $j=b$, not an extension of the contact range.

Consequently,


$$
Z_w^TZ_w=\xi^TM\xi,
$$


and


$$
Z_w^TY=\xi^TM\psi+bW_b^2\xi_{b-1}.
$$



Therefore the exact alignment defect is


$$
\boxed{
Z_w^TY-p\rho_nZ_w^TZ_w
=
\xi^TM A^{-1}(\mathbf r-p\rho_nf^0)
+bW_b^2\xi_{b-1}.
}
\tag{4.1}
$$



Substituting the complete force gives


$$
\boxed{
\begin{aligned}
Z_w^TY-p\rho_nZ_w^TZ_w
={}&
\xi^TM A^{-1}
\left(A_{IE}z+\frac{h^F}{b!}-p\rho_nf^0\right)\\
&+bW_b^2\xi_{b-1}.
\end{aligned}}
\tag{4.2}
$$



This identity preserves both finite inversions, the whole logarithmic force, and the terminal.

It is not a proof of alignment. Its value is that it identifies the exact source-specific assertion needed: a contraction identity for the actual force difference, including the explicitly displayed terminal correction. Merely showing that the two force sequences obey related interior recurrences would not suffice; their initial charges and the terminal term must also match at the required precision.

---

## 5. Growing-depth retention at the actual primitive precision

Write


$$
Z_w=p^{c+2}x,\qquad x\text{ primitive at }p,
$$




$$
x^Tx=p^\nu\eta,\qquad \eta\in\mathbb Z_p^\times,
$$


and


$$
d=2c+4+\nu,\qquad K=d-c=c+4+\nu.
$$



I reuse the supplied A2 Turn 14 theorem rather than repeat its exterior calculation.

At precision $p^K$, it retains:

- symbol indices
  

$$
0\le s\le p(K-1);
$$


- exterior indices
  

$$
0\le h\le p(K-1)+1;
$$


- the actual finite exterior solution, with its return;
- the logarithmic head of length
  

$$
L_{\log}(K)=
  \min\!\left(b,\ p\max\{K-N_{\log},0\}\right);
$$


- the physical terminal $W_be_b$.

Here


$$
N_{\log}
=
2v_p(n!)-v_p(b!)
-\lfloor\log_p(2n+b-1)\rfloor.
$$



The complete retained response is


$$
Y^{[K]}
=
\mathcal R\theta^{(e,[K])}
+W_be_b
+\mathcal RA^{-1}r^{(F,[K])},
$$


and the established result is


$$
Y-Y^{[K]}\in p^K\mathbb Z_p^{b+1}.
$$


Thus


$$
Z_w^T(Y-Y^{[K]})\in p^{d+2}\mathbb Z_p.
$$



The unresolved primitive observable is exactly


$$
\boxed{
x^TY^{[K]}-p^{K-1}\rho_n\eta
\pmod{p^K}.
}
\tag{5.1}
$$



Equation (4.2) identifies the full finite-source expression whose contraction must establish (5.1). No all-depth cancellation of that expression is proved by the supplied sources.

### The missing definition of $\rho_n$

The packet supplies no independent defining formula for $\rho_n$. What is needed is its actual index-dependent definition, including:

1. the exact numerator and denominator or equivalent original construction;
2. its relation, if any, to the original approximants or source charges;
3. the valuation $v_p(\rho_n)$;
4. enough unit precision for the norm term.

If $v_p(\rho_n)=-h<0$, write


$$
\rho_n=p^{-h}\widetilde\rho_n.
$$


Then the required datum is


$$
\widetilde\rho_n\eta\pmod{p^{h+1}},
$$


not merely $\rho_n\bmod p$. If $h>K-1$, the norm term is not even integral at the displayed normalization; congruence must then be interpreted after an additional paid scaling.

No integrality assumption is introduced here.

---

## 6. A target-specific obstruction to bounded-content low-digit domains

A proposed bounded-content infinite subdomain must constrain more than finitely many low digits of $b$.

### Proposition

Fix $m\ge1$. Suppose a condition depends only on


$$
b\bmod p^m
$$


and is attained by at least one original index. Then its original-index preimage contains an infinite arithmetic progression in $u$.

#### Proof

Set


$$
E=574312172,\qquad a=249005515.
$$


Since $3$ is a unit modulo $p^m$, the element $3^E$ has a finite multiplicative order


$$
T_m=\operatorname{ord}_{p^m}(3^E).
$$


Thus


$$
3^{a+E(u+T_m)}\equiv3^{a+Eu}\pmod{p^m}.
$$



If $u_*$ is an original index satisfying the condition, then every


$$
u=u_*+t\,\operatorname{lcm}(T_m,p^9),
\qquad t\ge0,
$$


has the same residue of $b$ modulo $p^m$ and remains in


$$
u\equiv2\pmod{p^9}.
$$


These are infinitely many original indices. ∎

### Consequence for content

Reuse the supplied theorem that $c$ is unbounded in every original arithmetic progression. The proposition implies:



$$
\boxed{
\text{No nonempty condition on finitely many low digits of }b
\text{ can by itself enforce a uniform bound on }c.
}
$$



This includes a finite union of admissible low-digit conditions and corresponding conditions on finitely many low digits of


$$
B=(b-5044)/p^3.
$$



This is a precise obstruction, not an assertion that no bounded-content infinite subdomain exists. Such a subdomain would have to use genuinely nonlocal information—for example, constraints involving word length or higher digits together with a proved content estimate.

The supplied facts do not prove that


$$
\{u:c(u)\le C,\ \nu(u)\le V\}
$$


is infinite for any explicit $C,V$. Unboundedness in every progression cannot supply that missing assertion.

### Concrete follow-on lemma

A useful next lemma would be:

> Construct an explicit nonlocal condition on the full original exponential word, prove that infinitely many original $u$ satisfy it, and prove on those same indices explicit bounds $c\le C$, $\nu\le V$, and a paid bound for $v_p(\rho_n)$.

Without such a lemma, bounded primitive precision cannot be inferred from a low-digit cylinder.

---

## 7. Minimal bounded reconciliation calculation

The closed large calculations should not be repeated. The immediate discrepancy can be inspected with a one-row calculation.

### Inputs

Use exactly the displayed seven source labels, atom formulas, symbol arrays and return values, with:



$$
p=29,\quad n_0=20387,\quad b_0=5044,\quad b\text{ odd},
$$


and only


$$
\ell=0.
$$



### Required output

For every branch surviving at $\ell=0$, report:

- source label;
- $(\alpha,v',r)$;
- coefficient modulo $841$;
- low digits;
- $e$, interface, and low unit;
- contribution to each of the three extracted profiles.

The expected verifiable first-column output is


$$
\boxed{a_0=14,\qquad b_0^{\mathrm{prof}}=20.}
$$



In particular, the row for the atom $-2\Psi_{1,-1,0}$ must contain


$$
C_0=2,\quad e=1,\quad s=000,\quad L=7,\quad\Gamma=18.
$$



This bounded reconciliation does not require any original high word, content computation, or new exterior solve. Only after reconciling it should the existing full low-row certificate be interpreted as evidence about $\alpha,\delta,\lambda$.

---

## 8. All-prime arithmetic and the whole error remain unchanged

No local normalization changes the actual row contents or the least simultaneous clearer $d_B$. Retain


$$
\omega_j=\frac{(n+2)!}{(n+2-j)!},
\qquad
\Omega=\operatorname{diag}(\omega_0^2,\ldots,\omega_b^2),
$$




$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,
\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),
\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
$$



The gcd is over **all primes**. The actual primitive multiplier is still


$$
d_B^2/g_B.
$$



At the same original index,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


and the whole evaluated error is


$$
q_n(e+\pi)-p_n=-q_n\epsilon_n.
$$



At the retained scope of the signed-error theorem, this error is eventually nonzero and


$$
\log|\epsilon_n|
=
-\left(2+\frac1{2001}\right)n\log(1+\sqrt2)+o(n).
$$



An irrationality proof still requires an all-prime bound on the actual $q_n$ making


$$
0<|q_n\epsilon_n|\longrightarrow0
$$


on the **same infinite original indices**. Neither the disputed fixed-layer certificate nor the exact metric identity supplies that bound.

---

## 9. Final proof-status ledger

| Claim | Status |
|---|---|
| The displayed extraction gives $a_0=14$, $b_0^{\mathrm{prof}}=20$ | **Proved by bounded hand arithmetic** |
| All six extracted profiles are zero | **Incompatible with the displayed formulas** |
| The final five observation coefficients are all zero | Reported finite result; requires reconciliation |
| Whole original fixed-layer zero beyond the known $c\ge5$ case | Not established here |
| Exact finite metric identity (4.2), including terminal | **Proved** |
| Growing-depth complete-force and paid-tail theorem | Reused at its stated scope |
| Primitive alignment at $K=c+4+\nu$ | Open |
| $\rho_n$ valuation and unit precision | Missing defining source |
| Finite low-digit restrictions cannot enforce bounded content | **Proved from periodicity and the retained unbounded-content theorem** |
| Explicit bounded-content infinite original subdomain | Open |
| All-prime denominator versus whole same-index error | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

## Conclusion

The immediate new result is an explicit audit obstruction:


$$
\boxed{a_0=14,\qquad b_0^{\mathrm{prof}}=20\pmod{29}.}
$$


It prevents acceptance of the asserted all-zero profiles without reconciliation, while leaving open the possibility that the completed five-coefficient observation row is nevertheless zero.

At primitive depth, the remaining mathematical bottleneck is the complete source contraction (4.2), evaluated at the actual $K=c+4+\nu$, with the logarithmic head retained, the terminal included, and $\rho_n$ paid at its true valuation. A bounded-content infinite subdomain additionally requires a nonlocal original-word argument; finite low-digit restrictions cannot provide it.

The next bounded arithmetic task is the single-row reconciliation above. The next substantive research tasks are an independently defined $\rho_n$, a source-specific contraction identity or evaluated relative digit, and an infinite original-domain content/precision theorem. The all-prime denominator comparison with the nonzero whole error remains a separate indispensable obligation.
