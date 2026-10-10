> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 — binary audit passed; a new graded $29$-adic contraction

**Status.** I do not prove or disprove irrationality of $e+\pi$, and I do not establish the complete MAIN29 zero-norm alignment assertion.

I obtain two substantive results.

1. **A5turn14’s infinite binary cancellation passes the audit.** The off-pair argument is valid, and the reference substitution has sufficient precision. Using the coordinator’s complete fixed-operator certificate, its paired conclusion strengthens to individual congruence
   

$$
X_j\equiv Y_j\pmod4\qquad(64\mid j,\ 0\le j<b).
$$


   This conclusion retains the large binomial kernel and all higher index digits.

2. **The four fixed $29$-adic sections eliminate every initial product grade at least $3$.** In particular, the entire last factorial block $31\le d\le59$, although nonzero in the complete $Q$-column, contributes **zero to the contracted defect modulo $29^6$**. I also prove a common residual-norm factor for the entire grade-$2$ contribution. The remaining obstruction is confined to grades $0$ and $1$, together with identification of their residual norm-zero locus.

The second result is a contraction statement, not merely disappearance of a Laurent row.

---

## 1. Independent audit of the binary infinite assertion

The domain is exactly


$$
b=9^r,\qquad n=4002b,\qquad r\ge1,\qquad r\equiv2\pmod{16}.
$$


Write


$$
b=128D+81,\qquad n=128C+66,\qquad h=n/2,
$$


and retain A5’s actual weighted columns


$$
X=Z_w/(2R),\qquad Y=V_w/(4b!),\qquad
R=2^h\binom{2h}{h}.
$$


All coordinate indices are $0\le j\le b$; the contact inverse has indices $0\le i,j<b$.

### 1.1 Off-pair support: passed

For odd $j$,


$$
W_j=\binom{n+2}{j}
=\frac{n+2}{j}\binom{n+1}{j-1},
$$


so $v_2(W_j)\ge2$.

Modulo $2$, the supplied polynomial forcing has values $0,1,1,1$ on residues modulo $4$. Since


$$
(1+z)^{-2n}=(1+z)^{-4h}
\equiv(1+z^4)^{-h}\pmod2,
$$


the finite upper boundary gives, with $M=(b-1)/4$,


$$
\theta^P_{4k}=0,\qquad
\theta^P_{4k+a}
=\binom{h+M-k-1}{M-k-1}\pmod2
\quad(a=1,2,3),
$$


whenever the coordinate lies in the inverse.

For $j\equiv3\pmod4$, the reconstruction difference is even. For $j=4k+1$, the only delicate case is $W_j/4$ odd. Then Lucas applied to


$$
\binom{n+1}{4k}
$$


forces $k$ even, because $n+1\equiv3\pmod8$. Now $M$ is even and $h$ is odd, so the displayed reconstruction binomial is even. Consequently


$$
X_j\equiv0\pmod4
$$


at every odd nonterminal coordinate.

At $j=b$, Lucas gives


$$
v_2(W_b)\ge3,
$$


and the exact endpoint reconstruction therefore gives $X_b\equiv0\pmod4$ as well.

For completeness, the asserted complete residual formula


$$
\eta_j\equiv(-1)^j
\left[
M_{-1}+2M_{-2}+6M_{-3}
+\left(4(1+j)+6\binom j3\right)M_0+4jM_2
\right]\pmod8
$$


also checks directly against the certified $Q$-polynomial modulo $8$. Here


$$
M_v=\binom{2n+b-1-j}{b-1-j-v}.
$$


Indeed, the five boundary terms reduce to the first three terms, and


$$
Q(X)\equiv4+4X+6\binom X3\pmod8
$$


gives the remaining terms by finite moment summation.

This formula yields:

* $Y_j$ is even when $j\equiv2\pmod4$;
* for $j=4k$,
  

$$
Y_{4k}\equiv
  \binom{32C+17}{k}
  \binom{h+M-k}{M-k}\pmod2.
$$



The first factor permits $k\equiv0,1,16,17\pmod{32}$; the second forces $k$ even. Thus the only possible even-coordinate odd entries of $Y$ are the prescribed pair coordinates. The complete endpoint is even because $8\mid W_b$.

Therefore the parity vector $z$ is supported only at odd coordinates, where $X/2$ is even. This proves


$$
\boxed{\xi^Tz=0\pmod2.}
$$



This part of the proof is independent of the sampled paired discrepancies.

### 1.2 Reference substitution: precision passed

For integer shifts $\delta$,


$$
v_2\!\left(\binom{x+\delta}{a}-\binom xa\right)
\ge v_2(\delta)-\lfloor\log_2 a\rfloor
$$


follows from Vandermonde and


$$
v_2\binom{\delta}{i}\ge v_2(\delta)-v_2(i).
$$



Here


$$
v_2(n-2)\ge6,\qquad v_2(b-81)\ge7.
$$


The lower indices involving $n$ in the closure operator are at most $4$; those involving $b$, through both required applications, are at most $13$. Their changes are therefore divisible by $16$. Integral finite differences preserve that divisibility.

Hence the substitution $(n,b)\mapsto(2,81)$ is valid for the **bounded polynomial operators** at the stated precisions. It is not a substitution in the large binomial kernel.

Likewise, for $64\mid j$ and $1\le a\le13$,


$$
v_2\binom ja\ge6-\lfloor\log_2a\rfloor\ge3,
$$


and


$$
\binom{2n+a-1}{a}\equiv\binom{a+3}{3}\pmod{16}.
$$


These are exactly the precision losses needed in A5’s kernel reduction.

### 1.3 Higher digits: passed, with a strengthening

The certified full coefficient vectors give


$$
(d_0,\ldots,d_{13})
\equiv(0,6,10,12,0,8,8,0,0,0,0,0,0,0)\pmod{16}.
$$


In particular, $\kappa=0$.

A5’s polynomial argument—not its sixteen samples—then gives


$$
\mathcal H(16m)\equiv0\pmod{16}
\qquad(m\ge0).
$$


The unrestricted convolution remains


$$
H_j\equiv
\sum_{v=0}^{m}
\binom{16C+7+v}{v}\mathcal H(16(m-v))
\pmod{16},
\qquad b-1-j=16m.
$$


Thus $H_j\equiv0\pmod{16}$ at every relevant $64$-multiple, regardless of the higher digits of $C,D$. Consequently


$$
\boxed{X_j\equiv Y_j\pmod4\qquad(64\mid j,\ 0\le j<b).}
$$



Together with the proved off-pair statement, this verifies the infinite assertion


$$
\boxed{\Delta=0\pmod2.}
$$



The complete five-tail residual and the whole logarithmic-forcing bound remain the inputs to this argument. Nothing here replaces them by selected forcing terms.

---

## 2. MAIN29: grading before multiplication

Now use exactly the odd-family domain


$$
p=29,\qquad b=3^a,\qquad n=2001b,\qquad
a\ge1,\qquad a\equiv432827\pmod{682892},\qquad m_w=1.
$$


Retain


$$
\widehat P=Z_w/p^2,\qquad
\widehat Q=Y/p^3,\qquad Y=V_w/b!,
$$


and


$$
D_0=\widehat P^T\widehat P\bmod p,\qquad
M_0=\widehat P^T\widehat Q\bmod p.
$$



The contracted numerator represents


$$
6C_n Z_w^TY-pZ_w^TZ_w\pmod{p^6}.
$$



### 2.1 The useful homogeneous pieces

Split the kernel coefficients into their $p$-adic digits **before taking products**:


$$
\mathcal P=\sum_{i=0}^{2}p^i\mathcal P_i\pmod{p^3},
\qquad
\mathcal Q=\sum_{v=0}^{3}p^v\mathcal Q_v\pmod{p^4}.
$$


The established graded Newton bounds imply


$$
\deg_j\mathcal P_i,\ \deg_r\mathcal P_i\le29(i+1).
$$



For $\mathcal Q_v$, its contact part has both degrees at most $29v$. Its boundary part has $j$-degree at most $1$ and Laurent support


$$
-\lambda_v\le\deg_s\le0,\qquad
\lambda_0=\lambda_1=2,\quad\lambda_2=31,\quad\lambda_3=60.
$$



A mixed product $\mathcal P_i\mathcal Q_v$ has initial grade $w=i+v$. A norm product in $p\mathcal P_i\mathcal P_{i'}$ has grade $w=1+i+i'$; for its support bounds put $v=i'+1$.

For either type, pad the Newton contraction to


$$
K_w=29(w+1)+1.
$$


Padding only inserts the compensating factor $(1+z)$; it changes no coefficient.

Let $R_w$ denote the resulting Laurent numerator. Its coefficient extraction has bases


$$
(1+r)^{A_0}(1+s)^{A_0}U^{N_0}(1+z)^{N_0-K_w},
$$


where


$$
A_0=n+b-3,\qquad N_0=n+2,\qquad
U=z(1+r)(1+s)+rs,
$$


and target $(b,b,N_0)$. Its relevant bounds are


$$
\deg_r R_w\le29(i+1),\quad
\deg_s^+R_w\le29v,\quad
\deg_zR_w\le K_w.
$$



The actual binomial coefficients $\binom{n+2}{k}$ in $R_w$ are retained at the required precision. They have not been replaced by four-digit representatives.

---

## 3. Four fixed sections: concrete support evaluation

The four low digits are


$$
\begin{array}{c|rrrr}
 &0&1&2&3\\ \hline
b&27&28&5&28\\
A_0&24&6&1&7\\
N_0&2&7&24&7\\
N_0-K_w&1&6-w&24&7.
\end{array}
$$



For a base $f$, write


$$
G_f=(f^{29}-f(X^{29}))/29.
$$


At the four successive sections let the ghost-count vectors be


$$
t,\ u,\ v',\ \ell\in\mathbb Z_{\ge0}^{\{r,s,U,z\}}.
$$


Only paths satisfying


$$
w+|t|+|u|+|v'|+|\ell|\le5
$$


can contribute modulo $p^6$.

The following support bounds follow by inserting the displayed fixed digits in each section. They are independent of all higher digits.



$$
\begin{array}{c|c|c|c}
\text{after section}&r\text{-range}&s\text{-range}&z\text{-range}\\ \hline
1&
[0,\ i+t_r+t_U]&
[-\max(1,v),\ v-1+t_s+t_U]&
[0,\ w+1+t_U+t_z]\\[1mm]
2&
[0,\ u_r+u_U-1]&
[-1,\ u_s+u_U-1]&
[0,\ u_U+u_z]\\[1mm]
3&
[0,\ \chi_r+v'_r+v'_U]&
[0,\ \chi_s+v'_s+v'_U]&
[0,\ v'_U+v'_z]\\[1mm]
4&
[0,\ \ell_r+\ell_U-1]&
[0,\ \ell_s+\ell_U-1]&
[0,\ \ell_U+\ell_z],
\end{array}
\tag{1}
$$


where


$$
\chi_r=\mathbf1_{u_r\ge2},\qquad
\chi_s=\mathbf1_{u_s\ge2}.
$$



For contact-only terms the negative $s$-ranges can be omitted.

Here are the two decisive cancellations in deriving the table. At the second section, the $r$-degree before extraction is at most


$$
i+t_r+t_U+(6-t_r)+(7-t_U)+29(u_r+u_U)
=i+13+29(u_r+u_U).
$$


Extracting residue $28$ gives the upper bound $u_r+u_U-1$. At the fourth section the corresponding degree is at most


$$
14+29(\ell_r+\ell_U),
$$


again giving $\ell_r+\ell_U-1$. The same calculation applies to $s$. The possible negative $s$-power disappears at the third section because its target residue is $5$.

Therefore every surviving path requires


$$
u_r+u_U\ge1,\qquad
\ell_r+\ell_U\ge1,\qquad
\ell_s+\ell_U\ge1.
\tag{2}
$$



In particular, at least two ghost factors are compulsory.

### Consequence for grades $4,5$

These grades have budget at most one ghost. Thus


$$
\boxed{\text{Every initial grade }w\ge4\text{ contributes }0\pmod{p^6}.}
\tag{3}
$$



This is already stronger than the ungraded degree-$86$ storage reduction.

---

## 4. The last compulsory ghost: an evaluated scalar

For grade $3$, the entire ghost budget is two. Thus:

* sections one and three have no ghosts;
* section two has either $u=e_U$, or $u=e_r$ for a boundary term;
* section four has $\ell=e_U$.

By (1), the numerator after the third section is a scalar. The fourth section is therefore controlled by the single universal polynomial


$$
\Phi(z)=
\Lambda_{28,28,7}
\left((1+r)^7(1+s)^7U^7(1+z)^7G_U\right).
\tag{4}
$$


The support table shows that $\Phi$ is a scalar plus a multiple of $z$.

### Proposition 1 — evaluated universal section



$$
\boxed{\Phi(z)\equiv58z\pmod{29^2}.}
\tag{5}
$$


In particular, $\Phi=0\pmod{29}$.

#### Proof

In the coefficient positions $r^{28}s^{28}$, the subtracted polynomial $U(r^{29},s^{29},z^{29})$ contributes nothing: every term involving $r^{29}$ or $s^{29}$ is too large, and the remaining $z^{29}$ term leaves $r,s$-degree at most $14$.

Thus the constant coefficient of $\Phi$ would come from


$$
[r^{28}s^{28}z^7]\,
(1+r)^7(1+s)^7U^{36}(1+z)^7.
$$


It is zero: selecting at most $28$ copies of $rs$ from $U^{36}$ leaves $z$-degree at least $8$.

The coefficient of $z$ is exactly


$$
\frac1{29}\sum_{k=0}^{7}
\binom{36}{k}\binom7k
\binom{43-k}{15}^{\,2}.
\tag{6}
$$


Every $\binom{43-k}{15}$ is divisible by $29$, and


$$
\frac1{29}\binom{43-k}{15}
\equiv
\frac{(-1)^k}{15\binom{14}{k}}\pmod{29}.
$$


Consequently the coefficient of $z$, divided once more by $29$, is


$$
15^{-2}\sum_{k=0}^{7}
\left(\frac{\binom7k}{\binom{14}{k}}\right)^2
\equiv4\cdot15\equiv2\pmod{29}.
$$


For direct verification, the eight ratios are


$$
1,\ 15,\ 27,\ 4,\ 12,\ 21,\ 24,\ 3,
$$


whose squared sum is $15\pmod{29}$. This proves (5). ∎

### Consequence for grade $3$

The two compulsory ghosts already provide $p^2$; Proposition 1 supplies a further $p$. Thus an initial grade-$3$ term is zero modulo $p^6$:


$$
\boxed{\text{Every initial grade }w\ge3\text{ contributes }0\pmod{29^6}.}
\tag{7}
$$



### Consequence for the last factorial block

The block


$$
31\le d\le59,\qquad F_d=(b+d)!/b!,
$$


has grade $3$. Its contribution to the boundary coefficients, including the induced contributions at lower boundary indices, therefore disappears in the complete mixed contraction modulo $p^6$. Subsequent contact action on this block has grade at least $4$ and was already absent at the column precision.

Hence


$$
\boxed{\text{The complete }31\le d\le59\text{ block contributes }0
\text{ to }6C_nZ_w^TY-pZ_w^TZ_w\pmod{29^6}.}
\tag{8}
$$



This explains why the surviving Laurent coefficient $6j$ does not decide the scalar: its entire factorial block cancels after contraction.

---

## 5. A residual-norm factor for grade $2$

Write the unfixed part of $b$ as


$$
b=687936+29^4h.
$$


No restriction on its higher digits has been imposed. On the original domain $h$ is the integer determined by the original power $3^a$, not an independently chosen cylinder point.

After four sections,


$$
N=\left\lfloor\frac{n+2}{29^4}\right\rfloor=2001h+1946,
$$




$$
A=\left\lfloor\frac{n+b-3}{29^4}\right\rfloor=N+h+1.
$$


In particular,


$$
N=3+29N_1,\qquad N_1=69h+67.
$$


Put


$$
h=29H+d,\qquad 0\le d<29,
$$


and define the genuine residual norm


$$
\boxed{
T(N_1,H)=
\sum_{k=0}^{H}
\binom{N_1}{k}^{2}
\binom{2N_1+H-k}{H-k}^{2}\pmod{29}.
}
\tag{9}
$$


The zero-binomial convention retains the actual finite index range.

### Proposition 2 — a small-state norm-divisibility relation

Suppose a terminal state has offsets


$$
\lambda=(\lambda_r,\lambda_s,\lambda_U,\lambda_z),\qquad
|\lambda|\le3,
$$


and a numerator monomial $r^\alpha s^\beta z^\gamma$ satisfying the actual fourth-section support


$$
0\le\alpha\le\lambda_r+\lambda_U-1,\quad
0\le\beta\le\lambda_s+\lambda_U-1,\quad
0\le\gamma\le\lambda_U+\lambda_z.
$$


Then its complete residual coefficient is


$$
\begin{aligned}
&[r^hs^hz^N]\,
r^\alpha s^\beta z^\gamma
(1+r)^{A-\lambda_r}(1+s)^{A-\lambda_s}
U^{N-\lambda_U}(1+z)^{N-\lambda_z}\\
&\hspace{25mm}\equiv
\Psi_{\lambda,\alpha,\beta,\gamma}(d)\,
T(N_1,H)\pmod{29},
\end{aligned}
\tag{10}
$$


where the multiplier is the explicit sum of at most four terms


$$
\begin{aligned}
\Psi_{\lambda,\alpha,\beta,\gamma}(d)
=\sum_{k=0}^{3-\lambda_U}
&\binom{3-\lambda_U}{k}
\binom{3-\lambda_z}{\lambda_U+k-\gamma}\\
&\times
\binom{d+7-\lambda_r-\lambda_U-k}{d-\alpha-k}
\binom{d+7-\lambda_s-\lambda_U-k}{d-\beta-k}
\pmod{29}.
\end{aligned}
\tag{11}
$$



#### Proof

Because $|\lambda|\le3$, neither $N-\lambda_U$ nor $N-\lambda_z$ borrows through the digit $N\bmod29=3$.

For a nonzero low-digit coefficient, $A-\lambda_r$ and $A-\lambda_s$ have high parts $N_1+H$. If their low parts overflow $29$, the support bounds make the required low coefficient zero: after Frobenius reduction the corresponding degree is strictly below $d$.

The low $r,s,z$ degrees are otherwise less than their targets plus $29$, so the next section leaves a constant numerator. Expanding the low power $U^{3-\lambda_U}$ gives precisely (11). The remaining high coefficient is


$$
[r^Hs^Hz^{N_1}]
(1+r)^{N_1+H}(1+s)^{N_1+H}
U^{N_1}(1+z)^{N_1},
$$


whose expansion is (9). ∎

This is a norm-divisibility invariant for these concrete residual states, not an unspecified kernel contraction.

### 5.1 A completely evaluated two-state relation

The two states left by a single final $U$-ghost have numerators $1,z$. Denote their contractions by $F_0,F_1$. Proposition 2 gives


$$
F_0=\phi_0(d)T,\qquad F_1=\phi_1(d)T\pmod{29},
\tag{12}
$$


where, setting


$$
B_t=
\begin{cases}
\binom{t+6}{6}\pmod{29},&0\le t\le22,\\
0,&\text{otherwise},
\end{cases}
$$


one has


$$
\boxed{
\phi_0=3B_d^2+6B_{d-1}^2+B_{d-2}^2,\qquad
\phi_1=B_d^2+6B_{d-1}^2+3B_{d-2}^2.
}
\tag{13}
$$


Thus


$$
\boxed{\phi_1(d)F_0-\phi_0(d)F_1=0.}
\tag{14}
$$



Both multipliers are nonzero for $0\le d\le24$, and both vanish for $25\le d\le28$. For example, $\phi_1$ on $0,\ldots,24$ is


$$
(1,26,8,17,19,6,13,17,19,15,24,26,10,10,8,21,6,1,5,25,28,24,8,8,3);
$$


$\phi_0(d)=\phi_1(24-d)$.

Consequently these two residual states have exactly aligned zeros, with all higher digits contained in the common norm $T$.

### 5.2 Scope for the full grade-$2$ contribution

Grade $2$ has room for at most three ghosts.

* With two ghosts, Proposition 1 supplies the additional factor $29$; the surviving numerator is a multiple of $z$.
* With three ghosts, the final offset sum is at most two, so Proposition 2 applies directly.

It follows that the complete grade-$2$ contribution $E_{[2]}$ satisfies


$$
\boxed{
E_{[2]}\in29^5\mathbb Z_{29},\qquad
E_{[2]}/29^5\equiv K_2\,T(N_1,H)\pmod{29}
}
\tag{15}
$$


for an actual scalar $K_2$ determined by the retained graded coefficients.

Its value is not needed for this divisibility assertion. In particular, the entire grade-$2$ contribution vanishes on $T=0$.

---

## 6. What remains unresolved

The new cancellation reduces the complete defect to


$$
\mathcal E\equiv E_{[0]}+E_{[1]}+E_{[2]}\pmod{29^6},
$$


with


$$
E_{[2]}/29^5\in T\mathbb F_{29},
$$


and all higher grades eliminated.

I have **not** shown either of the following:

1. that the combined grade-$0$ and grade-$1$ residual numerator is divisible by the same $T$;
2. that zero of the actual normalized norm $D_0$ is equivalent to $T=0$.

Those are genuine remaining conditions. The proof above does not authorize replacing “actual norm-zero state” by “$T=0$ state.”

The unevaluated part now lies in the higher-precision carries of the two lowest initial grades, rather than in the last factorial block or the degree-$86$ top rows. A unit-norm auxiliary mismatch would still not settle this obstruction.

---

## 7. Actual primitive arithmetic and whole errors

No local identity above changes the primitive normalization.

For the odd family, retain the stated actual factorial metric


$$
\Omega=\operatorname{diag}\bigl((n+2)_j^2\bigr)
$$


and the least common denominator of the two actual columns,


$$
N_B=d_B[u,v],\qquad v_{29}(d_B)=0.
$$


Then


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
p_n=H_B/g_B,\qquad q_n=A_B/g_B>0.
$$


The primitive multiplier on the integer coefficient pair is $1/g_B$; the actual denominator is $q_n$, not $d_B$.

With


$$
\delta=v_{29}(\widehat P^T\widehat P),\qquad
\mu=v_{29}(\widehat P^T\widehat Q),
$$


the supplied exact interface remains


$$
v_{29}(g_B)
=\min\{4F_n+4+\delta,\ 2F_n+F_b+5+\mu\},
$$




$$
v_{29}(q_n)
=\max\{0,\ 2F_n-F_b-1+\delta-\mu\}.
$$


The norm is nonzero by positivity; finiteness of the mixed valuation retains the supplied original-family nonvanishing dependency.

At the supplied status of the complete signed-error theorem,


$$
\epsilon_n=p_n/q_n-(e+\pi)>0
\quad\text{eventually},
$$


and the whole primitive form is


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n<0}
$$


with


$$
\log|\epsilon_n|
=-\left(2+\frac1{2001}\right)n\log(1+\sqrt2)+o(n).
$$



For the binary family, retain its different, explicitly stated weights


$$
\omega_j=j!\binom{n+2}{j}=(n+2)_{\underline j}.
$$


Its exact denominator formula remains


$$
v_2(q_n)=
\max\left\{0,\frac{3n}{2}-v_2(b!)-s_2(n)-1-(\gamma-\alpha)\right\}.
$$


The audited one-digit cancellation gives no all-depth estimate for $\gamma-\alpha$. Its supplied whole error is eventually positive:


$$
q_n(e+\pi)-p_n=-q_n\epsilon_n>0.
$$



The complete forces and endpoints remain in these real errors. No global denominator-rate estimate follows from the new local contractions.

---

# Concluding ledger

## (1) New result and proof status

**Proved here:**

* A5’s off-pair cancellation and reference-substitution precision pass independently.
* With the complete fixed-operator certificate, binary paired coordinates satisfy the stronger individual congruence $X_j\equiv Y_j\pmod4$.
* The graded four-section support table (1), with all higher parameter digits retained.
* The evaluated universal section
  

$$
\Phi(z)=58z\pmod{841}.
$$


* Every initial product grade at least $3$ vanishes in the contracted defect modulo $29^6$.
* In particular, the entire last factorial block contributes zero after contraction.
* The explicit low-dimensional norm-divisibility relations (10)–(15), including zero alignment of the two states $F_0,F_1$.

**Not proved:** complete MAIN29 norm-zero alignment, all-depth valuation alignment, a global bound on the actual primitive denominator, or irrationality/rationality of $e+\pi$.

## (2) Exact remaining bottleneck

Evaluate the combined **grade-$0$ and grade-$1$** residuals at their remaining precision and compare their actual norm-zero locus with the residual norm $T(N_1,H)$.

The last factorial block is no longer an unresolved scalar obstruction at this digit.

## (3) Bounded computation request

No $b=1395217$ run is requested.

An optional independent audit of the new evaluated scalar requires only eight small terms:



$$
p=29,\qquad
S_*=\sum_{k=0}^{7}
\binom{36}{k}\binom7k\binom{43-k}{15}^{2}.
$$



**Expected verifiable output**


$$
29^2\mid S_*,
\qquad
S_*/29^2\equiv2\pmod{29},
$$


together with the eight ratios


$$
\binom7k/\binom{14}{k}
\equiv(1,15,27,4,12,21,24,3)\pmod{29}.
$$



This is eight exact binomial terms with upper indices at most $43$, not a large-cylinder calculation. It audits Proposition 1; the infinite assertions above rest on the section and support proofs, not on that finite check.
