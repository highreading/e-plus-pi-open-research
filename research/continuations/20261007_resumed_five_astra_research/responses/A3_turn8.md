> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Family022 and the fixed-seed endpoint problem

## Abstract and principal conclusions

The supplied packet does **not** establish either rationality or irrationality of $e+\pi$. Family022’s main assertion is a metric theorem: for each prescribed shift and approximation function, its conclusion holds outside an exceptional null set of real numbers. It does not identify whether the particular number $e+\pi$ lies outside that set.

This report makes four more specific contributions.

1. **It separates the inspected local arithmetic from the uninspected global proof.** The packet contains the introduction, preliminaries, prescriptions, arithmetic, direct comparisons, and consequences. It omits the centres, tables, sparse, partitions, and joins sections. Several conclusions in the supplied sections depend essentially on those omissions. The whole manuscript cannot be certified from this packet.

2. **It gives a concrete deterministic test of the metric paper’s arithmetic against the actual paid endpoint contacts.** The tensor estimate applies to suitable finite integer supports, but its singleton specialization gives no contact saving. More decisively, the lcm estimate is asymptotically sharp on a diagonal graph formed from an actual paid-contact integer. The small-scale extraction alternative then returns a saturated diagonal configuration rather than a contradiction.

3. **It proves a new same-index arithmetic statement.** Every above-$N$, factorial-height integer has asymptotically full totient density. This applies unconditionally to turn 7’s fixed-source integer
   

$$
z_1=1+\frac{n!}{2^{(n-3)/2}}
$$


   on $\mathcal S=\{15^{2a}:a\ge1\}$, and it applies to the actual paid-contact integers at every nondegenerate original index. Consequently, totient capacities do not make these particular integers arithmetically small.

4. **It derives an explicit two-endpoint eliminant.** A primitive-row exterior-product identity cancels the coefficient $A_n$ between the two complete endpoint forcings, while retaining the exponential contribution and the endpoint-$0$ exterior correction. This bounds only the **common part** of the two contacts unless a further estimate controls isolated contacts. The eliminant’s required nonvanishing and subfactorial height remain open.

No expensive producer calculation is repeated. An optional new calculation is specified at the end using only already-produced endpoint records.

---

## 1. Original objects and arithmetic boundaries

### 1.1 The original indices are unchanged

Throughout,


$$
n=15^r\quad\text{or}\quad n=105^r,\qquad r\ge2,
$$


and


$$
m=n+1,\qquad N=n+2,\qquad K=2n+2.
$$



The infinite subfamily on which turn 7 proved the particularly strong first-coordinate statement is


$$
\mathcal S=\{15^{2a}:a\ge1\}.
$$



Statements about paid endpoint contacts require the archived nondegeneracy hypotheses


$$
\det T\ne0,\qquad F\ne0,\qquad R_0R_3\ne0.
$$


The packet does not prove that these conditions hold on an infinite subset of $\mathcal S$. No such infinitude is assumed below.

### 1.2 Complete fixed forcing and physical terminal

The source remains


$$
q(z)=1-z+\frac{z^2}{2},
\qquad
\alpha_0=\alpha_1=1,
\qquad
\alpha_s=\alpha_{s-1}-\frac12\alpha_{s-2},
$$




$$
\eta_s=\sum_{r=0}^s\frac1{r!}
       +2\sum_{r=1}^s\frac{\alpha_{r-1}}r,
\qquad
\mathcal W_s=s!\eta_s.
$$


Thus


$$
\mathcal W_s=s\mathcal W_{s-1}
 +1+2(s-1)!\alpha_{s-1}.
$$



In particular, neither the exponential forcing $1$ nor the amplitude-$2$ logarithmic forcing is removed.

The terminal convolution is


$$
\widehat w_i
=\sum_{a=0}^{n+i}[z^a]q(z)^n
 \frac{\mathcal W_{2n+i-a}}{(n+i-a)!},
\qquad 0\le i\le2.
$$


Its largest source index is exactly $K$. Nothing below extends the finite forcing problem past $K$.

Write


$$
c_k=[z^k]e^zq(z)^n,
\qquad
J=N!
\begin{pmatrix}
c_n&c_{n-1}&c_{n-2}\\
c_{n+1}&c_n&c_{n-1}\\
c_{n+2}&c_{n+1}&c_n
\end{pmatrix},
\qquad \Delta=\det J.
$$


Its columns are denoted $J_0,J_1,J_2$.

The reference is


$$
t=
\begin{pmatrix}
\tau_n\\
(\tau_n+\tau_{n+1})/2\\
\tau_{n+2}/2
\end{pmatrix},
\qquad H=N!t,
$$


where


$$
\tau_0=\tau_1=1,\qquad
(k+2)\tau_{k+2}=(2k+3)\tau_{k+1}+(k+1)\tau_k.
$$



To distinguish the scalar exponential partial sum from the vector exponential response, put


$$
E_n^{\mathrm{sc}}=n!\sum_{r=0}^n\frac1{r!}.
$$


The complete terminal identity is


$$
N!\widehat w=J_0+E_n^{\mathrm{sc}}H+\mathbf C.
$$


Thus the full correction vector, without dropping any column contribution, is explicitly


$$
C_i=
N!\sum_{a=0}^{n+i}[z^a]q(z)^n
 \frac{\mathcal W_{2n+i-a}}{(n+i-a)!}
-(J_0)_i-E_n^{\mathrm{sc}}H_i,
\qquad 0\le i\le2.
$$



### 1.3 Actual primitive rows, not unsaturated substitutes

Retain


$$
\mathbf t_j=\ell_j\operatorname{adj}(J),
\qquad
\ell_0=(-1,n,-nm),\quad \ell_3=(0,0,1),
$$




$$
h_j^K=\gcd(|t_{j,0}|,|t_{j,1}|,|t_{j,2}|),
\qquad
r_j=\frac{\sigma_j\mathbf t_j}{h_j^K},
\qquad \sigma_j\in\{\pm1\}.
$$


These are the actual kernel contents and saturated endpoint rows.

The retained projections include


$$
\mathbf t_0J_0=-\Delta,\qquad
\mathbf t_3J_2=\Delta,\qquad
\mathbf t_3J_0=0.
$$



Turn 7 supplies


$$
\mathbf Z_n=\mathbf E_n+A_n\mathbf L_n,
\qquad
A_n=\frac{n!N!}{2^{n-1}\operatorname{lcm}(1,\ldots,N)}\in\mathbb Z,
$$


with


$$
\|\mathbf E_n\|_\infty<8N!10^n,
\qquad
\|\mathbf L_n\|_\infty\le2^{11}320^n.
$$


The evaluated complete endpoint numerator is


$$
\boxed{\;
\Xi_j=r_j(\mathbf E_n-J_0)+A_n r_j\mathbf L_n.
\;}
\tag{1.1}
$$


Equivalently, using the complete terminal identity,


$$
\Xi_j=r_j\!\left(N!\widehat w-J_0-\mathcal W_nH\right).
$$



For endpoint $0$, this is


$$
\Xi_0=\frac{\sigma_0}{h_0^K}
\left[\mathbf t_0(\mathbf E_n+A_n\mathbf L_n)+\Delta\right].
\tag{1.2}
$$


The $+\Delta$ return is therefore still present.

### 1.4 Exact paid contacts

Turn 7’s genuine integral reference normalization is


$$
\mathcal B_j=r_j(2^nt)=\frac{2^nR_j}{N!}\in\mathbb Z\setminus\{0\}.
$$


For every $p>N$,


$$
v_p(\mathcal B_j)=v_p(R_j).
$$



Define


$$
V_j=\frac{|\mathcal B_j|}
          {\gcd(|\mathcal B_j|,|F|)}
$$


and the positive integer


$$
D_j=
\prod_{p>N}p^{\min\{v_p(V_j),v_p(\Xi_j)\}}.
\tag{1.3}
$$


If $\Xi_j=0$, the convention is $\gcd(V_j,0)=V_j$; the definition remains meaningful.

Then


$$
v_p(D_j)=
\min\{(v_p(R_j)-v_p(F))_+,v_p(\Xi_j)\},
\qquad p>N.
$$


Thus $D_j$ is the actual paid above-$N$ contact integer. The two-endpoint aggregate in turn 7 is


$$
\boxed{\;
\mathfrak C_n=[D_0,D_3].
\;}
\tag{1.4}
$$



This definition incorporates $F$ before forming the contact. It does not replace the final all-prime gcd of the rational approximation, discussed in Section 8.

---

## 2. What was actually supplied from Family022

### 2.1 Section-level coverage ledger

| Source component | Supplied? | What can be assessed here |
|---|---:|---|
| `main.tex` | Yes | Macros, theorem environments, abstract, section order, and dependencies |
| Introduction | Yes | Exact main quantifiers, claimed scope, and proof architecture |
| Preliminaries | Yes | Finite-block reduction, deficit law, elementary prime bounds, one-coordinate concentration, tensor kernel, determinant-cycle averages |
| Centres | **No** | Centre construction, hierarchy, density, lower bounds, and centre kernel cannot be checked |
| Prescriptions | Yes | Local CRT, reconstruction, model-separation, hard-mean, and soft-loss arguments; their global availability depends on omitted centre data |
| Tables | **No** | Projected-array definitions, update rules, conditional reduction, comparison hypotheses, and variance budget cannot be checked |
| Arithmetic | Yes | Sieve, rotation, lcm estimate, small-scale extraction, and box-sampling proof text |
| Direct comparisons | Yes | Detailed direct-comparison argument, but its global hypotheses depend on centres and tables |
| Sparse | **No** | Prime-step alignment estimates cannot be checked |
| Partitions | **No** | History-preserving partition construction cannot be checked |
| Joins | **No** | First-interaction estimates, capacity accounting, and closing induction cannot be checked |
| Consequences | Yes | Conditional mass-transference deduction from the main theorem |
| Bibliography | No | The cited external theorems are not supplied in primary mathematical form |

Consequently:

> The packet supports inspection and reuse of specific local lemmas at their stated hypotheses. It does not support certification of the entire claimed weak inhomogeneous Duffin–Schaeffer theorem.

The consequences section does not repair that omission: it begins by invoking the main Lebesgue-measure theorem.

### 2.2 Exact main quantifiers

The main assertion is


$$
\forall\gamma\in\mathbb R,\quad
\forall\psi:\mathbb N\to[0,\infty)
\text{ finite-valued},
$$




$$
\sum_q\frac{\phi(q)}q\psi(q)=\infty
\quad\Longrightarrow\quad
\left|\mathbb R\setminus W_\gamma(\psi)\right|=0,
$$


where


$$
W_\gamma(\psi)=
\{x:\|qx-\gamma\|<\psi(q)\text{ for infinitely many }q\}.
$$



The exceptional set may depend on **both** $\gamma$ and $\psi$. The theorem does not assert a single full-measure set of $x$ working simultaneously for all real shifts and all approximation functions.

Nor does it impose numerator coprimality. That distinction matters because several deterministic estimates in the proof are obtained only after introducing specially designed numerator restrictions.

### 2.3 Why fixed $e+\pi$ is not covered

Even a correct full-measure theorem does not locate a specified point.

For a simple illustration, take


$$
\gamma=\frac12,\qquad \psi(q)=\frac14.
$$


The weighted sum diverges: its terms along the primes are at least $1/8$. Nevertheless, at $x=0$,


$$
\|q x-\gamma\|=\frac12>\frac14
$$


for every $q$.

The issue is not special to rational $x$; the example simply makes the quantifier obstruction explicit. A null exceptional set may contain any particular prescribed real number.

Setting $x=e+\pi$, or instead setting $\gamma=e+\pi$, does not remove this problem. A deterministic transfer must supply information about the actual endpoint integers and their evaluated error.

---

## 3. Deterministic arithmetic genuinely available in the packet

### 3.1 Deficit laws and residue laws are different

The deficit law is


$$
\pi_L(d)=\frac{\phi(L/d)}L,\qquad d\mid L.
$$


It is a probability measure, with


$$
\Pr_{\pi_L}(p^j\mid d)=p^{-j}.
$$



This is a law on divisor masks. It is not a claim that a fixed endpoint numerator is uniformly distributed modulo $p^j$.

Separately, the determinant-cycle lemma averages numerator residues over complete cycles. Its conclusions require the actual cycle or a specified translation orbit. They do not hold pointwise at one selected numerator.

That distinction is maintained explicitly in Family022 and must also be maintained in an endpoint application.

### 3.2 Tensor kernel

The supplied preliminary proof establishes, for


$$
\frac12<u<1,\qquad s>1-u,
$$


and nonnegative integer-indexed sequences,


$$
\sum_{L,M}
\frac{(x_Ly_M)^u}
{\left(L/(L,M)\cdot M/(L,M)\right)^s}
\ll_{u,s}
\left(\sum_Lx_L\sum_My_M\right)^u.
\tag{3.1}
$$



The strict inequality $s>1-u$ is essential to the given proof: the one-prime excess has order


$$
p^{-s/(1-u)},
$$


and its Euler product is summable only beyond exponent $1$.

This is a deterministic statement. No metric quantifier is involved.

**Test on the endpoint data.** At a fixed nondegenerate original index, take singleton supports


$$
L=V_j,\qquad M=|\Xi_j|
$$


when $\Xi_j\ne0$, with weights one. All hypotheses hold. But (3.1) then says only


$$
\left(\frac{(V_j,|\Xi_j|)^2}{V_j|\Xi_j|}\right)^s\ll1,
$$


which is weaker than the elementary inequality that the fraction is at most one.

Thus its direct same-index specialization supplies no upper bound of the required form


$$
\log D_j=o(n\log n).
$$



For multiple indices, integer collisions must also be handled correctly. The lemma is indexed by distinct integer values, not by arbitrarily many labels carrying the same value. Compressing labels changes the weights inside the $u$-powers. One cannot silently apply it to an indexed sequence with unrestricted multiplicities.

### 3.3 Weighted lcm estimate

The arithmetic section’s lcm proposition has the following hypotheses:

* finite sets of positive integers;
* nonnegative vertex weights $f(v)\le\phi(v)$, $g(w)\le\phi(w)$;
* nonnegative edges satisfying
  

$$
e(v,w)\le f(v)g(w)
   h(v/(v,w))h(w/(v,w));
$$


* a common lcm cutoff $[v,w]\le Z$;
* $h_p\ge1$, bounded, tending to one, with every required moment product
  

$$
\prod_p\left(1+\frac{h_p^a-1}{p}\right)<\infty.
$$



It concludes


$$
\mathcal E\ll Z^{2(1-u)}(FG)^u.
\tag{3.2}
$$



The supplied proof addresses the critical exponent that the tensor lemma alone does not cover. Its essential additional ingredients are:

1. division by the exact local totient capacities during prime stripping;
2. common-pivot concentration in a hypothetical counterexample;
3. summable removal of double deviations and deviations of size at least two;
4. capacities $O(NA^2)$ for the resulting squarefree defect families;
5. moment-controlled inflation and a geometrically summable dyadic estimate.

These are genuine additional hypotheses and arguments, not merely a renamed gcd inequality.

For $h\equiv1$, all inflation hypotheses hold. This special case is sufficient for the concrete transfer test in Section 5.

### 3.4 Exact modeled equality: what its deterministic core requires

The proof of the exact-equality lemma contains a useful deterministic partner count. At common masks and a common rational model $\zeta=n_0/q$, it obtains


$$
q\mid s-t,\qquad
s\le H_{W'}^{h_s},\qquad
t\le H_V^{h_s},
\tag{3.3}
$$


where $s,t$ are coprime denominator ratios. When the bias is nonzero and the interval bumps meet, it also has


$$
|s-t|\ll \frac{s}{b_V}+\frac{t}{b_{W'}}.
\tag{3.4}
$$



For comparable large heights these inequalities force $s=t$. For disparate heights the partner-length sum is bounded by


$$
H_V^{1+2h_s}
\sum_{D\gtrsim H_V^{1/(3h_s)}}D^{h_s-1}=O(1),
$$


provided, as used there, $h_s<.01$.

The algebraic partner count is checkable from the displayed hypotheses. Its application to total first mass additionally uses:

* uniqueness of the rational model across the relevant rows;
* one actual row per fixed denominator and masks;
* the soft gcd tests;
* low-weight means bounded by $R(V)$;
* independent unrestricted mask averaging followed by Jensen’s inequality;
* the exact restoration of the row currency $r_i\phi(v)$.

For our endpoints, none of those numerator prescriptions has been established. In particular, primitiveness of $r_j$ does not establish the soft tests for the scalar contractions $r_jH$ and $r_j\mathbf Z_n$.

The exact-equality lemma is therefore not presently a theorem about $R_j,F,\Xi_j$.

---

## 4. A new rough-integer lemma at the original indices

Write


$$
R(a)=\frac{\phi(a)}a.
$$



### Theorem 4.1 — Totient density of factorial-height rough integers

Fix $C>0$. Suppose $a=a_n\ge1$ is an integer such that

1. every prime divisor of $a$ exceeds $N=n+2$;
2. $\log a\le Cn\log n$.

Then, uniformly over such integers,


$$
\sum_{p\mid a}\frac1p
=O_C\!\left(\frac{\log\log n}{\log n}\right),
\tag{4.1}
$$


and


$$
\boxed{\;
\frac{\phi(a)}a
=1-O_C\!\left(\frac{\log\log n}{\log n}\right).
\;}
\tag{4.2}
$$



For every fixed $B>0$,


$$
\prod_{p\mid a}R_p^{-B}
=1+O_{B,C}\!\left(\frac{\log\log n}{\log n}\right).
\tag{4.3}
$$



#### Proof

Take


$$
Y=n(\log n)^2.
$$



For primes in $(N,Y]$, the supplied elementary reciprocal-prime estimate gives


$$
\sum_{N<p\le Y}\frac1p
\ll
\frac1{\log N}
+\log\frac{\log Y}{\log N}
=O\!\left(\frac{\log\log n}{\log n}\right).
$$



For prime divisors of $a$ exceeding $Y$, use


$$
\frac1p\le\frac{\log p}{Y\log Y}.
$$


Hence


$$
\sum_{\substack{p\mid a\\p>Y}}\frac1p
\le
\frac{\log a}{Y\log Y}
=O_C((\log n)^{-2}).
$$


This proves (4.1).

Since all these primes exceed $N$,


$$
0\le-\log R(a)
=\sum_{p\mid a}-\log(1-1/p)
\ll\sum_{p\mid a}\frac1p.
$$


Exponentiation proves (4.2), and the same calculation proves (4.3). ∎

### 4.1 Application to the actual fixed source

Turn 7 proves unconditionally on $\mathcal S$ that


$$
z_1=1+\frac{n!}{2^{(n-3)/2}}
$$


has no prime factor at most $N$, and


$$
\log z_1
=n\log n-\left(1+\frac{\log2}{2}\right)n+O(\log n).
$$



Therefore


$$
\boxed{\;
\phi(z_1)
=z_1\left(1-O\!\left(\frac{\log\log n}{\log n}\right)\right)
\quad(n\in\mathcal S).
\;}
\tag{4.4}
$$



In particular,


$$
\log\phi(z_1)
=n\log n-\left(1+\frac{\log2}{2}\right)n+O(\log n).
$$



This is a new consequence for the **actual fixed-amplitude source**, not an arbitrary-seed construction. Its meaning is unfavorable to a proposed totient-capacity shortcut: the totient capacity of this factorial-height integer is asymptotically its entire size.

It still does not prove that this source coordinate survives either endpoint projection.

### 4.2 Application to actual paid contacts

The archived height budget gives


$$
\log\mathfrak C_n\le4n\log n+O(n)
$$


as a conservative bound, with actual kernel contents and payments retained in its sharper form.

Every prime factor of $D_0,D_3,\mathfrak C_n$ exceeds $N$. Therefore Theorem 4.1 gives, at every nondegenerate original index,


$$
R(D_j)=1-O\!\left(\frac{\log\log n}{\log n}\right),
$$




$$
\boxed{\;
R(\mathfrak C_n)
=1-O\!\left(\frac{\log\log n}{\log n}\right).
\;}
\tag{4.5}
$$



These conclusions remain true if one of the contact integers is $1$.

Thus the actual paid contacts are not forced to be small by having small totient density. They have asymptotically **large** totient density.

### 4.3 The larger admissible inflation used in the direct proof

Suppose a particular inflation satisfies the stronger pointwise condition


$$
\log h_p\le B\frac{\log p}{p}.
$$


This covers the type of logarithmically enhanced mismatch factor used in the supplied large-scale discussion.

For the same rough integers,


$$
\log h(a)\le B\sum_{p\mid a}\frac{\log p}{p}.
$$


Between $N$ and $Y$, a dyadic decomposition and the elementary prime-log bound give


$$
\sum_{N<p\le Y}\frac{\log p}{p}=O(\log\log n).
$$


Above $Y$,


$$
\sum_{\substack{p\mid a\\p>Y}}\frac{\log p}{p}
\le\frac{\log a}{Y}=O_C((\log n)^{-1}).
$$


Hence


$$
h(a)\le(\log n)^{O_{B,C}(1)}.
\tag{4.6}
$$



This controls the **inflation factor**, not the integer $a$. Multiplying a factorial-height contact by a polylogarithmic factor does not establish subfactorial contact loss.

No assertion like (4.3) is made for every $h$ satisfying only Family022’s abstract moment hypotheses.

---

## 5. An exact transfer test: the arithmetic estimates allow our contact obstruction

Let $D$ be any one of the actual integers


$$
D_0,\quad D_3,\quad \mathfrak C_n.
$$



### 5.1 The lcm estimate is asymptotically sharp here

Construct a one-vertex graph on each side:


$$
v=w=D,\qquad
f(D)=g(D)=\phi(D),\qquad
e(D,D)=\phi(D)^2.
$$


Take


$$
h\equiv1,\qquad Z=D.
$$



Every hypothesis of the lcm proposition is satisfied, with equality in the vertex and edge capacities.

The ratio between its left side and the scale on its right side is


$$
\frac{\phi(D)^2}
     {D^{2(1-u)}(\phi(D)^2)^u}
=
R(D)^{2(1-u)}.
$$


By (4.5),


$$
\boxed{\;
\frac{\mathcal E}
 {Z^{2(1-u)}(FG)^u}
=1-o(1).
\;}
\tag{5.1}
$$



This is a concrete application to an integer extracted from the actual $R_j,F,\Xi_j$. It proves that the local lcm inequality cannot, by itself, force that integer below factorial height.

The claim is limited: this diagonal graph is a deterministic encoding of a scalar contact, not a claim that it is Family022’s full projected-row construction.

### 5.2 Small-scale extraction returns a genuine saturated diagonal

Give both sides width


$$
r=\frac{\eta}{D},\qquad 0<\eta<1.
$$


The normalized totals are


$$
\mathsf F=\mathsf G=\eta R(D)\le1,
\qquad
\mathsf E=\eta^2R(D)^2,
$$


and the determinant scale is exactly


$$
[D,D]r=\eta.
$$



The proposed small-saving alternative would be


$$
\eta^2R(D)^2
\le
\eta^{1+\chi}
\bigl(\eta^2R(D)^2\bigr)^u.
$$


The quotient of the left side by the right side is


$$
\eta^{1-\chi-2u}R(D)^{2-2u}.
$$


Because $u>1/2$, this tends to infinity as $\eta\downarrow0$.

The structured alternative is not paradoxical. It is explicitly realized by


$$
N_{\mathrm{pivot}}=D,\qquad
U_0=T_0=a=b=c=d_1=1,
$$


with dyads $A=C=1$. The two capacities are


$$
D_1^{\mathrm{cap}}=D_2^{\mathrm{cap}}=\eta.
$$


They satisfy


$$
\eta^{2+\vartheta}\le\eta\le\eta^{-\vartheta},
$$


and the edge weight exceeds


$$
\eta^\vartheta D_1^{\mathrm{cap}}D_2^{\mathrm{cap}}
$$


for sufficiently small $\eta$.

Thus:

> The arithmetic extraction does not exclude the contact. It identifies a saturated configuration which the remaining numerator prescriptions would have to eliminate or pay.

Those prescriptions are precisely the hypotheses not established for our endpoints.

### 5.3 Why the rotation and sampling steps do not complete the transfer

The rotation lemma requires an integer or prime parameter ranging over an interval while its slope and target phase remain fixed.

In Family022, this is justified by explicit factor-switching parameterizations and unrestricted comparison laws. For our endpoints, the relevant scalar is


$$
\Xi_j=r_j(\mathbf E_n-J_0)+A_n r_j\mathbf L_n.
$$


No supplied identity parameterizes a varying divisor of $V_j$ so that:

* the actual fixed source remains the same;
* the physical terminal remains $K$;
* the actual row $r_j$ and its content are correctly transported;
* the needed phase is independent of the switched factor;
* the resulting majorant has the required totient capacity;
* the original contact is retained without unpaid conditioning.

This is the precise missing transfer interface.

The box-sampling corollary does allow auxiliary point-mass laws. The problem is therefore not simply that our data are deterministic. The problem is that a point mass does not supply the uniform factor variation needed by the rotation argument. If one replaces a complete residue average by a chosen residue, the comparison density can cost the full modulus; if the prescribed rule excludes that residue, the point cannot be retained at all.

Neither such a cost nor the effect of such a deletion has been paid for the actual endpoint numerators.

---

## 6. A new complete-source two-endpoint eliminant

The following identity is independent of Family022’s metric theorem.

Put


$$
X=\mathbf E_n-J_0,\qquad L=\mathbf L_n,
$$


and


$$
a_j=r_jX,\qquad b_j=r_jL.
$$


Then the complete forcing reads


$$
\Xi_j=a_j+A_nb_j.
$$



Define the integer


$$
\boxed{\;
\mathfrak D_n=a_0b_3-a_3b_0.
\;}
\tag{6.1}
$$



### Proposition 6.1 — Primitive exterior-product identity

At every nondegenerate original index,


$$
\mathfrak D_n=b_3\Xi_0-b_0\Xi_3
\tag{6.2}
$$


and


$$
\boxed{\;
\mathfrak D_n=
\frac{\sigma_0\sigma_3\Delta}{h_0^Kh_3^K}
\det\!\left(nJ_0+J_1,\ \mathbf E_n-J_0,\ \mathbf L_n\right).
\;}
\tag{6.3}
$$



The expression is an integer because its left side is a contraction of the actual primitive integer rows.

#### Proof

First,


$$
b_3\Xi_0-b_0\Xi_3
=b_3(a_0+A_nb_0)-b_0(a_3+A_nb_3)
=a_0b_3-a_3b_0.
$$


Thus the $A_n$-term cancels exactly, rather than being discarded.

For row vectors $u,v$ and an invertible $3\times3$ matrix $M$,


$$
(uM)\times(vM)=\det(M)(u\times v)M^{-T}.
$$


Apply this to $M=\operatorname{adj}(J)$. Since


$$
\det(\operatorname{adj}J)=\Delta^2,
\qquad
(\operatorname{adj}J)^{-T}=J^T/\Delta,
$$


and


$$
\ell_0\times\ell_3=(n,1,0),
$$


we obtain


$$
\mathbf t_0\times\mathbf t_3
=\Delta(nJ_0+J_1)^T.
$$


After the actual content divisions,


$$
r_0\times r_3
=\frac{\sigma_0\sigma_3\Delta}{h_0^Kh_3^K}
(nJ_0+J_1)^T.
$$


Taking the scalar product with $X\times L$ proves (6.3). ∎

### 6.1 The exterior return is visibly retained

Because


$$
\det(nJ_0+J_1,J_0,L)
=-\det(J_0,J_1,L),
$$


formula (6.3) is equivalently


$$
\mathfrak D_n=
\frac{\sigma_0\sigma_3\Delta}{h_0^Kh_3^K}
\left[
\det(nJ_0+J_1,\mathbf E_n,L)
+\det(J_0,J_1,L)
\right].
\tag{6.4}
$$



In raw-row form,


$$
\mathfrak D_n=
\frac{\sigma_0\sigma_3}{h_0^Kh_3^K}
\left[
(\mathbf t_0\mathbf E_n+\Delta)(\mathbf t_3L)
-(\mathbf t_3\mathbf E_n)(\mathbf t_0L)
\right].
\tag{6.5}
$$



The $+\Delta$ correction is explicit. Neither $\Delta$ nor either kernel content may be canceled further without a proved divisibility statement.

### 6.2 What this controls—and what it does not

Let


$$
C_n^{\mathrm{com}}=(D_0,D_3),
\qquad
I_n^{\mathrm{iso}}=\frac{D_0D_3}{(D_0,D_3)^2}.
$$


Since $C_n^{\mathrm{com}}$ divides both $\Xi_0$ and $\Xi_3$,


$$
\boxed{\;
C_n^{\mathrm{com}}\mid\mathfrak D_n.
\;}
\tag{6.6}
$$



Moreover,


$$
\mathfrak C_n=C_n^{\mathrm{com}}I_n^{\mathrm{iso}}.
\tag{6.7}
$$



If $\mathfrak D_n\ne0$, then


$$
\log\mathfrak C_n
\le \log|\mathfrak D_n|+\log I_n^{\mathrm{iso}}.
\tag{6.8}
$$



This is a precise split between common and isolated contact depth. It explains why an estimate for shared overlap alone is insufficient.

The elimination of $A_n$ does **not** establish a small-height certificate:

* $\mathbf E_n$ still has factorial height;
* $\Delta$ and the primitive-row contents remain;
* $\mathfrak D_n$ could vanish;
* isolated endpoint contacts remain in $I_n^{\mathrm{iso}}$.

### Concrete follow-on lemma

A sufficient next statement is:

> On a proved infinite set of nondegenerate original indices, establish
> 

$$
> \mathfrak D_n\ne0,\qquad
> \log|\mathfrak D_n|=o(n\log n),
>
$$


> for the **evaluated integer** (6.1), together with
> 

$$
> \log I_n^{\mathrm{iso}}=o(n\log n).
>
$$



By (6.8), this would prove the desired subfactorial bound for the combined paid contact over **all** primes $p>N$, including $p>K$.

This is an open lemma, not a proved height estimate. Its advantage over a generic “use an adjoint” proposal is that the candidate integer, the complete forcing combination, the exterior correction, the actual divisions, and the remaining isolated-contact term are now explicit.

---

## 7. Minimal missing sources for the next reading

Two distinct source needs should not be conflated.

### 7.1 To audit Family022’s global proof

The following omitted statements and proofs are essential:

1. **Centres**
   * `cen:hierarchy`;
   * the centre assignment and type/colour definitions;
   * `eq:centre-lower`;
   * `eq:centre-density`;
   * `eq:centre-kernel`;
   * the definitions of $U,T,K,\Theta_{ij},k_L,\delta_L,Y_0,Y_d$.

   These are needed even to validate the hypotheses of the supplied direct-comparison proposition.

2. **Tables**
   * the projected-array and update definitions;
   * `tab:conditional-reduction`;
   * `tab:first-join-input`;
   * `tab:variance-budget`;
   * the precise meaning of common translation orbits, clipping, and retained comparison laws.

3. **Sparse, partitions, joins**
   * prime-step comparison bounds;
   * construction of history-preserving partitions;
   * `join:capacity`;
   * the first-interaction estimates and the finite induction completing the variance budget.

The appropriate next acquisition is mathematical source text for these sections, not an assumption that their catalogue descriptions are correct.

### 7.2 To evaluate the new endpoint eliminant

The turn 7 excerpts omit the explicit construction of the vectors $\mathbf E_n,\mathbf L_n$, most of the endpoint denominator section, and the definition of the archived $F$.

For a new exact evaluation, the minimal endpoint source is:

* the full turn 7 forcing-decomposition formulas;
* the actual $F$-payment definition;
* the complete row-content and least-clearer formulas;
* the complete primitive-denominator formulas from turn 7 Section 8 and the referenced A4 result.

The present report does not invent those missing definitions.

---

## 8. Final denominator and whole error remain separate obligations

### 8.1 No above-$N$ contact estimate replaces the final gcd

The archived upper bound is retained as supplied:


$$
q_\lambda\le
\frac{
k_{\rm wt}(48e^2)^2m^2(n!)^2(N!)^6(325/8)^{2n}
}{
h_0^Kh_3^K\,g_0^*g_3^*\,\phi_0\phi_3\,
h_{\rm end}F_{\rm gcd}G_{\rm wt}H_{\rm gcd}
}.
\tag{8.1}
$$


Its factors denote the actual archived payments, not parameters that may be assigned favorable sizes. Their full definitions are absent from the excerpts, so no new numerical denominator is reconstructed here.

For clarity about the final all-prime reduction, let


$$
\frac{V_j^{\mathrm{end}}}{U_j^{\mathrm{end}}}
=\frac{\widetilde v_j}{\widetilde u_j},
\qquad
U_j^{\mathrm{end}}>0,
\qquad
(U_j^{\mathrm{end}},V_j^{\mathrm{end}})=1,
$$


be the actual reduced endpoint fractions.

If their original rational pairs require clearing, the legitimate procedure is to use the actual least simultaneous clearer and then the actual integer content. A larger convenient clearer is not automatically the actual primitive normalization.

For a rational weight $\lambda=a/b$, in lowest terms with $b>0$, set


$$
S=aV_0^{\mathrm{end}}U_3^{\mathrm{end}}
 +(b-a)V_3^{\mathrm{end}}U_0^{\mathrm{end}},
$$




$$
T=bU_0^{\mathrm{end}}U_3^{\mathrm{end}},
\qquad
G_{\mathrm{final}}=\gcd(|S|,T).
$$


Then the exact primitive result is


$$
p_\lambda=\frac{S}{G_{\mathrm{final}}},
\qquad
q_\lambda=\frac{T}{G_{\mathrm{final}}}.
\tag{8.2}
$$



The gcd in (8.2) is over **all primes**. Formula (1.3) concerns a different, earlier payment. It cannot substitute for $G_{\mathrm{final}}$.

Equations (8.1)–(8.2) are bookkeeping safeguards, not a claim to have evaluated the omitted denominator formulas.

### 8.2 The required error is the same-index whole error

The irrationality criterion remains


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=q_\lambda\left[
(e+\pi)
-\lambda\frac{\widetilde v_0}{\widetilde u_0}
-(1-\lambda)\frac{\widetilde v_3}{\widetilde u_3}
\right].
}
\tag{8.3}
$$



The required theorem is


$$
0<
\left|q_\lambda(e+\pi)-p_\lambda\right|
\longrightarrow0
$$


on the **same infinite original indices** for which the arithmetic estimates and nondegeneracy have been proved.

No estimate for one component, a different weight, or a neighboring index proves this.

Indeed, if $e+\pi=A/B$ were rational, every nonzero expression in (8.3) would have absolute value at least $1/B$. Thus the displayed nonzero convergence would imply irrationality. Neither Family022 nor the new results above establish that convergence.

---

## 9. Bounded exact arithmetic: optional new check only

No computation is needed for Theorem 4.1, the diagonal saturation calculation, or Proposition 6.1.

If the coordinator wishes to inspect the new eliminant numerically, the following is a bounded auxiliary check. It must use an already-produced endpoint record; it does **not** call for rerunning the $n=225$ producer.

### Inputs

At the single fixed original index $n=225$, take the existing exact records for


$$
J,\Delta,\sigma_j,h_j^K,r_j,\mathcal B_j,F,\Xi_j,
$$


and the actual turn 7 vectors


$$
\mathbf E_n,\mathbf L_n.
$$



If the latter vectors are not already available with their defining formulas, first obtain the omitted mathematical source. An arbitrary decomposition with the same sum is not a substitute.

### New exact outputs

1. The integers
   

$$
a_j=r_j(\mathbf E_n-J_0),\qquad b_j=r_j\mathbf L_n.
$$



2. The exact integer
   

$$
\mathfrak D_n=a_0b_3-a_3b_0
$$


   and its zero/nonzero status.

3. The exact zero residual
   

$$
h_0^Kh_3^K\mathfrak D_n
   -
   \sigma_0\sigma_3\Delta
   \det(nJ_0+J_1,\mathbf E_n-J_0,\mathbf L_n)
   =0.
$$



4. The exact paid gcds:
   

$$
G_j=\gcd\!\left(
   \frac{|\mathcal B_j|}{\gcd(|\mathcal B_j|,|F|)},
   |\Xi_j|
   \right).
$$


   Remove from $G_j$ only the prime powers with $p\le227$, obtaining $D_j$. This requires no factorization of the remaining large integer.

5. The integers
   

$$
C_n^{\mathrm{com}}=(D_0,D_3),\qquad
   I_n^{\mathrm{iso}}=\frac{D_0D_3}{(D_0,D_3)^2},
$$


   with exact checks
   

$$
C_n^{\mathrm{com}}\mid\mathfrak D_n,\qquad
   [D_0,D_3]=C_n^{\mathrm{com}}I_n^{\mathrm{iso}}.
$$



The expected algebraic residuals are zero. The actual size and nonvanishing of $\mathfrak D_n$ are outputs to inspect, not predictions made here.

This calculation would have only its stated finite scope. In particular, the already-known absence of positive reference depth in $227<p\le452$ at $n=225$ would not become an infinite contact theorem.

---

## 10. Final proof status

### Newly proved

* The rough-integer totient estimate (4.1)–(4.3).
* Its unconditional application to the actual fixed-source $z_1$ on $\mathcal S$.
* Its application to actual paid-contact integers at every nondegenerate original index.
* The exact asymptotic saturation test showing that Family022’s lcm estimate alone cannot make those contact integers subfactorial.
* The complete-source primitive eliminant identity (6.1)–(6.5).
* The exact decomposition of total paid contact into common and isolated parts, with the conditional bound (6.8).

### Not proved

* The global Family022 theorem from this partial packet.
* A deterministic application of its numerator prescriptions, factor switches, or variance budget to $R_j,F,\Xi_j$.
* Nonvanishing or subfactorial height of $\mathfrak D_n$.
* A subfactorial bound for isolated contacts.
* Infinitely many nondegenerate endpoint indices.
* The required nonzero whole-error convergence with the actual primitive denominator.
* Rationality or irrationality of $e+\pi$.

### Exact remaining bottleneck

Family022’s reusable arithmetic allows concentration; its later, highly structured numerator mechanism is what excludes or pays that concentration. Our fixed-seed endpoint construction has not been shown to possess that mechanism.

The concrete endpoint alternative now exposed is to evaluate and control


$$
\frac{\sigma_0\sigma_3\Delta}{h_0^Kh_3^K}
\det(nJ_0+J_1,\mathbf E_n-J_0,\mathbf L_n),
$$


while separately controlling the isolated paid contacts and then combining the resulting arithmetic with the **actual all-prime primitive denominator and nonzero whole error at the same infinite original indices**.

The factorial-height fixed source has not disappeared. One explicit coefficient has been eliminated between endpoints, but the remaining evaluated determinant and isolated contacts are still genuine mathematical obligations.
