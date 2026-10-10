> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Adjacent contact determinants, primitive-denominator growth, and a diagnostic mixed construction

## 1. Results and proof status

The rationality or irrationality of


$$
s_0=e+\pi
$$


remains unresolved.

This report pursues a direction different from an upper bound on the all-prime content of a single coefficient pair. The principal new results are:

1. **An exact adjacent-size recurrence for the complete affine determinants.** After determinant-preserving row and column operations, the period parameter occupies one matrix entry. The resulting matrices are nested. A two-row, two-column bordering calculation gives an integral, denominator-paid recurrence and an exact identity for
   

$$
p_{k+1}q_k-p_kq_{k+1}.
$$


   The factorial endpoints and the complete rational arctangent corrections remain in the recurrence.

2. **Quantitative lower growth of actual primitive denominators.** Using the supplied rational-error comparison, not raw coefficient heights, one obtains
   

$$
q_k\longrightarrow\infty,
   \qquad
   \limsup_{k\to\infty}\frac{\log q_k}{k}
   \ge \frac12\log\frac{16}{7}.
$$


   On the original infinite parameter set
   

$$
K_u=9^{18+32u},\qquad u\ge0,
$$


   consecutive primitive rational zeros are strictly increasing, and
   

$$
q_{K_u}q_{K_{u+1}}
   \ge
   \frac{(16/7)^{K_u-1}}{84(4K_u-3)}.
$$


   In particular, writing $B=9^{32}$,
   

$$
\limsup_{u\to\infty}
   \frac{\log q_{K_u}}{K_u}
   \ge \frac{\log(16/7)}{B+1}>0.
$$



3. **A precisely defined alternative mixed construction with a proved obstruction.** A Taylor approximation to $e$, combined with complete Machin arctangent truncations at a chosen terminal prime-power index, has a nonzero whole primitive error bounded away from zero. The proof uses an exact valuation of its actual primitive denominator, after the final all-prime gcd. This is a scoped obstruction for that alternative, not for every mixed construction.

These results do **not** prove either


$$
\frac{q_k}{k896^k}\longrightarrow\infty
$$


or


$$
q_k\,k(7/16)^k\longrightarrow0.
$$


The new lower bounds are substantially weaker than the first target, while the available upper bound is much too large for the second.

No computation is claimed to have been performed. A small, optional adjacent-size arithmetic check is specified in §11; it does not duplicate the coordinator’s $k=32$ calculation.

---

## 2. Exact objects and reused results

### 2.1 Complete moments and original finite boundaries

Throughout the compact construction,


$$
k\ge2,\qquad 0\le m<2k,\qquad 0\le j<k.
$$


The complete moment sequences are


$$
a_0=1,\qquad a_d=1-da_{d-1},
$$




$$
c_n=a_{2n}-(-1)^n,
$$




$$
\rho_0=0,\qquad
\rho_{n+1}+\rho_n=\frac1{2n+1},
$$




$$
r_n=-(2n)!+4\rho_n.
$$



Set


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5).
$$


The actual integer affine polynomial is


$$
H_k(s)=
\det\left[
(c_{m+j})\ \middle|\
\bigl(\Lambda_k[r_{m+j}+s(-1)^{m+j}]\bigr)
\right]
=H_{0,k}+H_{1,k}s.
\tag{2.1}
$$



Its maximum moment index is exactly $3k-2$, its maximum factorial is $(6k-4)!$, and its last possible odd denominator is $6k-5$.

The actual final normalization is


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|),
$$




$$
q_k=\frac{|H_{1,k}|}{G_k},\qquad
p_k=-\frac{\operatorname{sgn}(H_{1,k})H_{0,k}}{G_k}.
\tag{2.2}
$$


Thus $q_k>0$ and $\gcd(p_k,q_k)=1$ whenever $H_{1,k}\ne0$.

### 2.2 Analytic inputs reused at their proved scope

The supplied sign theorem gives, for $k\ge32$,


$$
(-1)^kH_k(s_0)>0,\qquad (-1)^kH_{1,k}>0.
\tag{2.3}
$$


Consequently,


$$
\ell_k:=q_ks_0-p_k
=\frac{|H_k(s_0)|}{G_k}>0.
\tag{2.4}
$$



For $k\ge64$, put


$$
\varepsilon_k=s_0-\frac{p_k}{q_k}=\frac{\ell_k}{q_k}.
$$


The quantitative comparison assigned for this turn is


$$
L_k\le\varepsilon_k\le U_k,
\tag{2.5}
$$


where


$$
L_k=\frac{112}{(4k-3)896^k},
\qquad
U_k=84(4k-3)\left(\frac7{16}\right)^{k-1}.
\tag{2.6}
$$



These are bounds for the zero of the **actual primitive affine pair**. Common scalar factors cancel in $\varepsilon_k$, but not in $\ell_k$.

The best supplied raw-growth result is also retained:


$$
\log|H_k(s_0)|=4k^2\log k+O(k^2).
\tag{2.7}
$$


The weaker leading-$2$ lower bound is not used as the current result.

The new conditioning argument in A5 Turn 13 and A3’s column-factor argument are used according to their displayed proofs. This report does not describe their pending independent audit as already completed. The sign theorem and the matching raw scale have the separate acceptance status stated in the coordinator packet.

### 2.3 Arithmetic input reused

Write


$$
D_{k-1}^{\mathrm{Lag}}=\prod_{r=0}^{k-2}(r!)^2
$$


and


$$
E_k=\frac{\Lambda_k^k}{\prod_{j=0}^{k-1}\Lambda_{k,j}},
\qquad
\Lambda_{k,j}=\operatorname{lcm}(1,3,\ldots,4k+2j-3).
$$


The established divisibility is


$$
D_{k-1}^{\mathrm{Lag}}E_k\mid G_k.
\tag{2.8}
$$


It remains only a lower divisor of $G_k$, not its value.

---

## 3. Concentrating the period parameter in one entry

The first step produces a genuinely nested matrix without discarding the arctangent channel.

Define


$$
\sigma_n=c_{n+1}+c_n=a_{2n+2}+a_{2n},
\tag{3.1}
$$


and


$$
\tau_n=r_{n+1}+r_n
=-(2n+2)!-(2n)!+\frac4{2n+1}.
\tag{3.2}
$$



Equation (3.2) is the full corrected recurrence. In particular, $\tau_n$ is not a factorial-only approximation.

### 3.1 Determinant-preserving operations

First work with the rational determinant $H_k(s)/\Lambda_k^k$.

1. In descending order $m=2k-1,\ldots,1$, replace row $m$ by
   

$$
R_m+R_{m-1}.
$$


   The period term disappears from every row except row $0$.

2. In descending order $j=k-1,\ldots,1$, replace right column $j$ by the sum of right columns $j$ and $j-1$. The period term then disappears from every column except right column $0$.

Both transformations are integral and unitriangular, with determinant $1$.

Finally, order the columns as


$$
T_0,C_0,T_1,C_1,\ldots,T_{k-1},C_{k-1},
\tag{3.3}
$$


where $C_j$ is a contact column and $T_j$ denotes a transformed right column. The permutation has sign


$$
\omega_k=(-1)^{k(k+1)/2}.
\tag{3.4}
$$



### 3.2 The resulting infinite array

Let $\mathscr M(s)$ be the array with rows $r\ge0$ and paired columns $T_j,C_j$, $j\ge0$, defined as follows:

- Column $T_0$:
  

$$
\mathscr M_{0,T_0}(s)=s-1,\qquad
  \mathscr M_{r,T_0}(s)=\tau_{r-1}\quad(r\ge1).
$$



- Contact column $C_j$:
  

$$
\mathscr M_{0,C_j}=c_j,\qquad
  \mathscr M_{r,C_j}=\sigma_{r+j-1}\quad(r\ge1).
$$



- Right column $T_j$, $j\ge1$:
  

$$
\mathscr M_{0,T_j}=\tau_{j-1},
$$


  

$$
\mathscr M_{r,T_j}
  =\tau_{r+j-1}+\tau_{r+j-2}\quad(r\ge1).
$$



Its leading $2k\times2k$ submatrix therefore satisfies


$$
\det\mathscr M_k(s)
=\omega_k\frac{H_k(s)}{\Lambda_k^k}.
\tag{3.5}
$$



Only the top-left entry depends on $s$. Increasing $k$ by one adds exactly two rows and the columns $T_k,C_k$.

This nesting is the structural point: it was not present in the original grouped-column notation, but it follows from explicit unimodular operations.

---

## 4. An integral adjacent-$k$ recurrence

To keep the bordering calculation integral, fix one adjacent pair $k,k+1$ and set


$$
\lambda=\Lambda_{k+1},\qquad
t=\frac{\Lambda_{k+1}}{\Lambda_k}\in\mathbb Z_{>0}.
\tag{4.1}
$$



Multiply every $T$-column in the relevant leading $(2k+2)\times(2k+2)$ array by $\lambda$, leaving every contact column unchanged. All entries are now integers, apart from the indeterminate $s$, which occurs as $\lambda(s-1)$.

Let


$$
F(s)=\det\mathscr M_k^{[\lambda]}(s),
\qquad
F^+(s)=\det\mathscr M_{k+1}^{[\lambda]}(s).
$$


Then


$$
F(s)=\omega_k t^kH_k(s),
\qquad
F^+(s)=\omega_{k+1}H_{k+1}(s).
\tag{4.2}
$$


The multiplier $t^k$ is retained throughout.

### 4.1 Explicit blocks

Put $N=2k$. Partition the enlarged matrix as


$$
\begin{pmatrix}
\lambda(s-1)&b&\beta\\
d&B_0&U\\
\delta&V&W
\end{pmatrix},
\tag{4.3}
$$


where $B_0$ has size $2k-1$, corresponding to rows and columns $1,\ldots,2k-1$.

The two new columns are $T_k,C_k$, and the two new rows are $2k,2k+1$. In particular,


$$
\beta=(\lambda\tau_{k-1},\,c_k),
\tag{4.4}
$$




$$
U_{r,0}
=\lambda(\tau_{r+k-1}+\tau_{r+k-2}),
\qquad
U_{r,1}=\sigma_{r+k-1},
\quad 1\le r\le2k-1,
\tag{4.5}
$$


and


$$
\delta=
\begin{pmatrix}
\lambda\tau_{2k-1}\\
\lambda\tau_{2k}
\end{pmatrix}.
\tag{4.6}
$$


The entries of $V$ and $W$ are given by the same explicit array formulas in §3.2.

Thus the new bottom-right right-column entry is


$$
\lambda(\tau_{3k}+\tau_{3k-1}),
$$


and the adjacent contact entry is $\sigma_{3k}$.

The largest underlying original moment is $r_{3k+1}$, exactly


$$
3(k+1)-2.
$$


The largest factorial is $(6k+2)!$, and the last odd denominator is $6k+1$. These are precisely the $k+1$ boundaries, not extra successor moments.

### 4.2 Integer Schur numerators

Define


$$
D=\det B_0
$$


and the integer matrices and vectors


$$
\mathcal S=DW-V\operatorname{adj}(B_0)U,
\tag{4.7}
$$




$$
\mathcal t=D\beta-b\operatorname{adj}(B_0)U,
\tag{4.8}
$$




$$
\mathcal z=D\delta-V\operatorname{adj}(B_0)d.
\tag{4.9}
$$


Here $\mathcal S$ is $2\times2$, $\mathcal t$ is $1\times2$, and $\mathcal z$ is $2\times1$.

Finally put


$$
\mathcal K=\det\mathcal S,
\qquad
\mathcal T=\mathcal t\,\operatorname{adj}(\mathcal S)\mathcal z.
\tag{4.10}
$$



These are completely specified integer quantities in the original adjacent finite moment windows.

### Theorem 4.1 — Paid adjacent recurrence

For $k\ge64$,


$$
\boxed{
D^2F^+(s)=\mathcal K F(s)-\mathcal T.
}
\tag{4.11}
$$


Moreover,


$$
F_1=\lambda D,\qquad
F_1^+=\frac{\lambda\mathcal K}{D},
\tag{4.12}
$$


and $D\ne0$, $\mathcal K\ne0$.

#### Proof

The coefficient of $s$ in the leading block is $\lambda D$. By (4.2) and the reused slope nonvanishing, $D\ne0$.

Eliminate $B_0$ in (4.3). The remaining $3\times3$ block is


$$
\begin{pmatrix}
\lambda(s-1)-bB_0^{-1}d&
\beta-bB_0^{-1}U\\
\delta-VB_0^{-1}d&
W-VB_0^{-1}U
\end{pmatrix}.
$$


Its upper-left entry is $F(s)/D$. The other blocks are


$$
\mathcal t/D,\qquad \mathcal z/D,\qquad \mathcal S/D.
$$


Using the $1+2$ block determinant formula,


$$
F^+(s)
=
\frac{\det(\mathcal S)F(s)
-\mathcal t\operatorname{adj}(\mathcal S)\mathcal z}{D^2}.
$$


This proves (4.11). Coefficient comparison proves (4.12). The nonzero slope of $F^+$ then gives $\mathcal K\ne0$. ∎

The division by $D^2$ is fully accounted for: (4.11) proves that the displayed integer numerator is coefficientwise divisible by $D^2$. It does **not** justify dividing the original $H_k$ by an additional guessed factor.

The denominator-free identity itself extends polynomially to singular $B_0$; only its divided form uses $D\ne0$.

---

## 5. Exact resultant and primitive cross-difference identities

Write


$$
F(s)=F_0+F_1s,\qquad
F^+(s)=F_0^++F_1^+s.
$$


Equation (4.11) gives


$$
F_0F_1^+-F_0^+F_1
=\frac{\lambda\mathcal T}{D}.
\tag{5.1}
$$



Now define the actual integer cross difference


$$
\Delta_k=p_{k+1}q_k-p_kq_{k+1}.
\tag{5.2}
$$


Since the primitive pairs use the signs in (2.3),


$$
\Delta_k
=
-\frac{H_{0,k}H_{1,k+1}-H_{0,k+1}H_{1,k}}
{G_kG_{k+1}}.
$$


Using (4.2), including its sign and factor $t^k$, gives:

### Theorem 5.1 — Complete adjacent primitive identity


$$
\boxed{
D\,t^kG_kG_{k+1}\Delta_k
=(-1)^k\lambda\mathcal T.
}
\tag{5.3}
$$



Every quantity in this identity belongs to the complete original moment determinants or to their explicitly defined adjacent border. In particular, neither $G_k$ nor $G_{k+1}$ has been replaced by a lower divisor.

For the rational zeros


$$
z_k=\frac{p_k}{q_k},
$$


one also obtains the exact gap formula


$$
\boxed{
z_{k+1}-z_k
=\frac{\mathcal T}{\lambda D\mathcal K}.
}
\tag{5.4}
$$


Equivalently,


$$
\boxed{
\varepsilon_{k+1}
=
\varepsilon_k-\frac{\mathcal T}{\lambda D\mathcal K}.
}
\tag{5.5}
$$



These identities isolate the adjacent obstruction more precisely than the statement that “the period matrix has rank one”:

- adjacent zeros coincide exactly when $\mathcal T=0$;
- their ordering depends on the sign of the complete scalar in (5.4);
- their primitive cross difference includes the full division by
  

$$
t^kG_kG_{k+1}.
$$



Separate positivity of $H_k(s_0)$ and $H_{1,k}$ does not determine any of these three matters.

---

## 6. Quantitative consequences for actual primitive denominators

The following consequences use rational separation of the actual reduced fractions. They are not height estimates for an unreduced coefficient.

### 6.1 The denominators tend to infinity

From (2.5),


$$
z_k\longrightarrow s_0,\qquad z_k<s_0.
$$


Suppose $q_k$ did not tend to infinity. Then some bounded denominator range would occur infinitely often. Since the $z_k$ eventually lie in a fixed bounded interval, only finitely many reduced fractions in that range are possible. One would therefore recur infinitely often and, by convergence, equal $s_0$, contradicting $\varepsilon_k>0$.

Thus


$$
\boxed{q_k\longrightarrow\infty.}
\tag{6.1}
$$



This argument does not assume irrationality of $s_0$.

### 6.2 An exponential lower bound on infinitely many compact indices

There must be infinitely many $k$ for which $\Delta_k\ne0$. Otherwise $z_k$ would eventually be constant, again contradicting positive convergence to $s_0$.

For $k\ge64$, $U_k$ is decreasing. At every transition $\Delta_k\ne0$,


$$
1\le|\Delta_k|
=q_kq_{k+1}|z_{k+1}-z_k|
=q_kq_{k+1}|\varepsilon_k-\varepsilon_{k+1}|
\le q_kq_{k+1}U_k.
$$


Hence


$$
\boxed{
q_kq_{k+1}
\ge
\frac{(16/7)^{k-1}}{84(4k-3)}
\qquad(\Delta_k\ne0).
}
\tag{6.2}
$$


In particular,


$$
\max(q_k,q_{k+1})
\ge
\frac{(16/7)^{(k-1)/2}}{\sqrt{84(4k-3)}}.
\tag{6.3}
$$



Because such transitions occur at unbounded indices,


$$
\boxed{
\limsup_{k\to\infty}\frac{\log q_k}{k}
\ge\frac12\log\frac{16}{7}.
}
\tag{6.4}
$$



The recurrence supplies the concrete zero criterion $\mathcal T=0$; the rational-error theorem proves that it cannot hold eventually.

### 6.3 Strict ordering on the same infinite original indices

Let


$$
K_u=9^{18+32u},\qquad B=9^{32},
$$


so $K_{u+1}=BK_u$.

We first prove an explicit separation estimate. For $k\ge64$,


$$
\frac{U_{16k}}{L_k}
\le
\frac{3072}{7}k^2\left(\frac7{512}\right)^k
<
\frac{439k^2}{64^k}
<\frac12.
\tag{6.5}
$$


The last inequality is elementary: the displayed expression decreases for $k\ge64$, and its value there is already below $1/2$. No numerical search is needed.

Since $B>16$ and $U_k$ is decreasing,


$$
\varepsilon_{BK}
\le U_{BK}\le U_{16K}<\frac12L_K\le\frac12\varepsilon_K.
\tag{6.6}
$$


Therefore, for every original $K=K_u$,


$$
z_{BK}>z_K,
$$


and


$$
\frac12L_K
<
z_{BK}-z_K
\le U_K.
\tag{6.7}
$$



The integer


$$
p_{BK}q_K-p_Kq_{BK}
$$


is consequently positive. It follows that


$$
\boxed{
q_Kq_{BK}\ge\frac1{U_K}
=
\frac{(16/7)^{K-1}}{84(4K-3)}.
}
\tag{6.8}
$$



This holds at every consecutive pair of original indices, not merely at an unspecified compact transition.

### 6.4 An explicit infinite original-index lower-growth set

Define


$$
f(K)=
\frac{(16/7)^{K/(B+1)}}{\sqrt{768K}}.
\tag{6.9}
$$


A direct multiplication shows


$$
f(K)f(BK)
=
\frac{(16/7)^K}{768\sqrt B\,K}
<
\frac{(16/7)^{K-1}}{84(4K-3)}.
$$


Thus (6.8) implies that at least one of


$$
q_K\ge f(K),\qquad q_{BK}\ge f(BK)
\tag{6.10}
$$


holds.

Consequently the explicitly defined set


$$
\mathcal U=
\{u\ge0:q_{K_u}\ge f(K_u)\}
$$


is infinite and meets every pair of consecutive original positions. In particular,


$$
\boxed{
\limsup_{u\to\infty}
\frac{\log q_{K_u}}{K_u}
\ge\frac{\log(16/7)}{B+1}.
}
\tag{6.11}
$$



This is a lower bound for the actual denominators $q_{K_u}$, with their final all-prime gcds already divided out.

### 6.5 The available upper bound

For comparison, the supplied slope ceiling and (2.8) give


$$
q_k\le
\frac{
\Lambda_k^k4^kk!\,28^{k-1}h_{k-1}
\prod_{r=0}^{k-1}(2k+4r)!
}{
D_{k-1}^{\mathrm{Lag}}E_k
},
\tag{6.12}
$$


hence


$$
\log q_k\le3k^2\log k+O(k^2).
\tag{6.13}
$$



This is a valid upper bound on the primitive denominator because the proved divisor has been paid. It is reused arithmetic, not the new achievement of this turn, and it is far too weak to prove primitive decay.

---

## 7. What the recurrence does not yet prove

### 7.1 No adjacent interlacing theorem has been assumed

Formula (5.4) is exact, but its numerator is


$$
\mathcal T=\mathcal t\operatorname{adj}(\mathcal S)\mathcal z,
$$


not a positive Gram determinant. The finite matrix $B_0$ is a mixed contact/arctangent matrix. Its nonsingularity does not imply a sign for $\mathcal T$.

The supplied one-index comparisons allow


$$
\frac{U_{k+1}}{L_k}
$$


to grow exponentially. They therefore do not compare $\varepsilon_{k+1}$ and $\varepsilon_k$ at adjacent indices. The use of $16k$, and hence of the much sparser original progression, avoids that unresolved comparison by an explicit separation estimate.

### 7.2 Why the new denominator lower bound is insufficient

The whole primitive error obeys


$$
\ell_k=q_k\varepsilon_k,
\qquad
q_kL_k\le\ell_k\le q_kU_k.
\tag{7.1}
$$



The exponential rate in (6.4) is only


$$
\frac12\log(16/7),
$$


whereas the stated divergence target requires growth beyond rate


$$
\log896.
$$


Thus even on the subsequence furnished by (6.4), the lower bound $q_kL_k$ need not tend to infinity.

Conversely, (6.13) does not imply $q_kU_k\to0$.

There is therefore no primitive-divergence or irrationality conclusion hidden in §6.

### 7.3 A concrete follow-on analytic lemma

The bordering formulas give a specific next lemma, distinct from an all-prime content theorem.

Since


$$
\varepsilon_k=\frac{F(s_0)}{\lambda D},
$$


equation (5.4) gives


$$
\frac{z_{k+1}-z_k}{\varepsilon_k}
=
\frac{\mathcal T}{\mathcal K F(s_0)}.
\tag{7.2}
$$



A concrete target is:

> **Adjacent contraction lemma.** For all sufficiently large $k$,
> 

$$
> \boxed{
> \frac{\mathcal T}{\mathcal K F(s_0)}\ge\frac12.
> }
> \tag{7.3}
>
$$



All quantities in (7.3) are defined by the complete finite moments in §§3–4. If proved, it would give


$$
0<\varepsilon_{k+1}\le\frac12\varepsilon_k,
$$


so every adjacent pair would be distinct and (6.2) would hold eventually at every $k$.

This is an **open lemma**, not a consequence of positivity alone. Its proof requires a correlated comparison of neighboring determinants; the separate bounds in (2.5) do not supply it.

Even this analytic lemma would not by itself solve irrationality. For example, if it were supplemented by the genuinely arithmetic assertions


$$
|\Delta_k|\le C,\qquad
C^{-1}\le\frac{q_{k+1}}{q_k}\le C
\tag{7.4}
$$


on an infinite tail, then


$$
1\le \Delta_k
=q_kq_{k+1}(z_{k+1}-z_k)
\ge \frac{q_k^2\varepsilon_k}{2C},
$$


while $\Delta_k\le C$ would give


$$
q_k^2\varepsilon_k\le2C^2.
$$


Consequently


$$
0<\ell_k=q_k\varepsilon_k
\le \sqrt{2}\,C\sqrt{\varepsilon_k}\longrightarrow0.
$$


That would prove irrationality.

Neither condition in (7.4) is presently established. Through (5.3), their arithmetic content is explicit rather than hidden behind a continued-fraction analogy.

---

## 8. One alternative mixed construction, with its actual obstruction

The compact family has **not** been proved impossible. Nevertheless, because its adjacent arithmetic remains unresolved, it is useful to evaluate one precisely specified alternative rather than propose an unanalysed new search.

The following construction combines a Taylor endpoint for $e$ with both channels of Machin’s formula. Its obstruction is provable after primitive reduction.

### 8.1 Definition on the original parameter progression

Retain $u\ge0$, and put


$$
t=18+32u,\qquad
N=\frac{5^t+1}{2},\qquad n=2N.
\tag{8.1}
$$


Thus $N$ is odd.

Define


$$
E_n=\sum_{j=0}^n\frac1{j!},
$$




$$
A_N(a)=\sum_{j=0}^{N-1}
\frac{(-1)^j}{(2j+1)a^{2j+1}},
$$


and the rational number


$$
R_u=E_n+16A_N(5)-4A_N(239).
\tag{8.2}
$$



The exact identity


$$
\pi=16\arctan(1/5)-4\arctan(1/239)
\tag{8.3}
$$


is used with both arctangent terms retained. For completeness, if $\theta=\arctan(1/5)$, then


$$
\tan(4\theta)=\frac{120}{119},
$$


and


$$
\tan\!\left(4\theta-\arctan(1/239)\right)=1.
$$


The angle lies in the appropriate interval, giving (8.3).

### 8.2 Exact primitive normalization

Reduce each of the three rational summands in (8.2) separately:


$$
E_n=\frac{P_e}{Q_e},\qquad
16A_N(5)=\frac{P_5}{Q_5},\qquad
-4A_N(239)=\frac{P_{239}}{Q_{239}},
$$


with positive denominators and coprime numerator-denominator pairs.

These reductions can be defined exactly by:

- the integer numerator $\sum_{j=0}^n n!/j!$ and its gcd with $n!$ for $E_n$;
- the raw least term clearer
  

$$
\operatorname{lcm}_{0\le j<N}\bigl((2j+1)a^{2j+1}\bigr)
$$


  for each arctangent sum, followed by the actual numerator-denominator gcd, including the coefficients $16$ and $-4$.

The actual least simultaneous clearer of these three reduced summands is


$$
C_u=\operatorname{lcm}(Q_e,Q_5,Q_{239}).
$$


Let


$$
P_u=C_uR_u,\qquad
G_u'=\gcd(|P_u|,C_u),
$$


and define the actual primitive pair


$$
p_u'=\frac{P_u}{G_u'},\qquad
q_u'=\frac{C_u}{G_u'}.
\tag{8.4}
$$



No raw lcm is substituted for $q_u'$.

### 8.3 An exact terminal $5$-adic denominator

The final term of $A_N(5)$ has denominator


$$
(2N-1)5^{2N-1}
=5^{\,2N-1+t}.
$$


It is the unique term of smallest $5$-adic valuation.

Indeed, an earlier term has index $j=N-1-h$, $h\ge1$, and odd denominator factor


$$
2j+1=5^t-2h.
$$


Its denominator valuation is


$$
5^t-2h+v_5(5^t-2h)
<
5^t+t=2N-1+t.
$$


For $2h<5^t$, one has $v_5(5^t-2h)=v_5(2h)<t$, which proves the strict inequality.

Hence


$$
v_5(A_N(5))=-(2N-1+t).
\tag{8.5}
$$


Multiplication by $16$ leaves this valuation unchanged.

By contrast,


$$
v_5(E_n)\ge-v_5(n!)>-(2N-1+t),
$$


since $n=2N$ and $v_5((2N)!)<N/2$. Also,


$$
v_5(A_N(239))\ge-t,
$$


because $239$ is a $5$-adic unit and every odd factor $2j+1$ is at most $5^t$.

Thus the first arctangent channel has uniquely smallest valuation in the complete sum (8.2). There can be no cancellation at that valuation. After the final all-prime gcd,


$$
\boxed{
v_5(q_u')=2N-1+t.
}
\tag{8.6}
$$



This is an exact valuation of the **actual primitive denominator**, not merely divisibility of a chosen clearer.

### 8.4 The complete whole error

For odd $N$, the finite geometric-series identity gives


$$
A_N(a)-\arctan(1/a)
=
\mathcal R_a
:=
\int_0^{1/a}\frac{x^{2N}}{1+x^2}\,dx>0.
$$


The full remainder satisfies


$$
\frac1{(1+a^{-2})(2N+1)a^{2N+1}}
\le\mathcal R_a
\le\frac1{(2N+1)a^{2N+1}}.
\tag{8.7}
$$



Let $\mathcal E_n=e-E_n>0$. Then the whole mixed error is exactly


$$
R_u-s_0
=16\mathcal R_5-4\mathcal R_{239}-\mathcal E_n.
\tag{8.8}
$$



For $N\ge16$,


$$
\mathcal E_n\le\frac2{(2N+1)!}\le\mathcal R_5.
$$


For example, using $e<3$ and the factorial lower bound,


$$
\frac{\mathcal E_n}{\mathcal R_5}
\le
\frac{52}{5}\left(\frac{15}{2N}\right)^{2N}<1.
$$


Also,


$$
\frac{\mathcal R_{239}}{\mathcal R_5}
\le\frac{26}{25}\left(\frac5{239}\right)^{2N+1}<\frac14.
$$


Therefore the complete error, with neither secondary channel omitted, obeys


$$
R_u-s_0\ge8\mathcal R_5>0.
\tag{8.9}
$$



Combining (8.6), (8.7), and (8.9),


$$
\begin{aligned}
p_u'-q_u's_0
&=q_u'(R_u-s_0)\\
&\ge
5^{2N-1+t}\,
\frac{8\cdot25}{26(2N+1)5^{2N+1}}\\
&=
\frac4{13}\frac{5^t}{2N+1}\\
&=
\frac4{13}\frac{2N-1}{2N+1}
>\frac14.
\end{aligned}
\tag{8.10}
$$



Thus:

### Theorem 8.1 — Scoped alternative-producer obstruction
For every $u\ge0$ in (8.1), the alternative mixed rational has


$$
\boxed{
p_u'-q_u'(e+\pi)>\frac14.
}
\tag{8.11}
$$


Its ordinary rational error tends to zero, but its nonzero whole primitive error does not.

### 8.5 How its balance differs from the compact family

Here the arctangent error has scale


$$
\mathcal R_5\asymp
\frac{5^{-2N-1}}{2N+1},
$$


while the forced factor of the actual denominator is


$$
5^{2N-1+t}.
$$


The exponential scales cancel, and the remaining factor


$$
\frac{5^t}{2N+1}
=\frac{2N-1}{2N+1}
$$


stays bounded away from zero.

The compact family instead has an unresolved cancellation between raw factorial-size coefficients and their all-prime content. The alternative has an explicit terminal-prime obstruction that survives that final normalization.

This does not rule out Padé-type arctangent channels, different terminal choices, or other mixed determinants. It rules out precisely the construction (8.1)–(8.4) as a primitive-decay proof.

---

## 9. Normalization ledger

### 9.1 Compact determinant clearers and contents

For the rational affine polynomial $H_k(s)/\Lambda_k^k$, define


$$
d_{H,k}=\gcd(\Lambda_k^k,H_{0,k},H_{1,k}).
$$


Its actual least simultaneous coefficient clearer is


$$
\frac{\Lambda_k^k}{d_{H,k}},
$$


and its content after that clearing is


$$
\frac{G_k}{d_{H,k}}.
$$


After both payments, the primitive pair is exactly $H_k/G_k$, up to orientation.

The adjacent calculation does not change these quantities. It introduces the explicit common-step factor $t^k$ in (4.2), which remains in (5.3).

### 9.2 Contact basis payments

If one uses a contact basis instead of the direct block determinant, the established payments remain separate:

- individual monic contact-row clearers;
- the saturation index
  

$$
\frac{|\det C_k|}{\delta_{k,2k-1}};
$$


- the actual projected entry clearer;
- actual row and column contents;
- the least simultaneous clearer of the resulting two affine coefficients;
- the final all-prime coefficient gcd.

For a saturated integer contact basis $X$, with


$$
B_{rj}^{X}=\sum_mX_{rm}r_{m+j},
$$


the least entry clearer remains


$$
L_X=
\frac{\Lambda_k}
{\gcd\!\left(\Lambda_k,\{\Lambda_kB_{rj}^{X}\}_{r,j}\right)}.
$$


If


$$
L_X^k\det\mathcal M_X(s)=A_0+A_1s,
$$


the least simultaneous coefficient clearer is


$$
\frac{L_X^k}{\gcd(L_X^k,A_0,A_1)},
$$


and the remaining content is


$$
\frac{\gcd(A_0,A_1)}
{\gcd(L_X^k,A_0,A_1)}.
$$



No value for these contents is inferred from the Schur recurrence. The direct block route avoids choosing a nonsaturated frame; it does not evaluate its residual gcd by another name.

---

## 10. Original binary producer: preserved but not identified

All compact conclusions above apply at


$$
k=K_u=9^{18+32u}.
$$


This is not an identification with the original binary producer.

That producer retains


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0,
$$


contact indices $0,\ldots,b-1$, physical reconstruction indices $0,\ldots,b$, and


$$
z_b=0.
$$



Its complete corrected columns remain


$$
x=\frac12RA^{-1}f,
\qquad
y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},
\qquad
x=2^ax_0.
$$


The terms $h^F$, $e_0$, and the factor $4b!$ are not removed.

The complete return scalar remains


$$
S=\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f,
$$


and the paid valuation statement remains only


$$
v_2\!\left(\frac{S}{2^{a+1}}\right)\ge\chi-a,
\qquad
\chi=v_2\binom{n+b-1}{b-1}.
$$


The subtraction of $a$ is indispensable.

Its norm $Q=x_0^Tx_0$, actual corrected-column contents, least simultaneous clearer, and final all-prime scalar gcd are not evaluated by this report. The original valuation


$$
v_3(q^{\mathrm{bin}})=n-\frac{b+15}{2}
$$


is not transferred to $q_k$.

Likewise, the alternative construction in §8 uses the same parameter $u$ but is a distinct producer with explicitly different finite sums. It claims no binary forcing or denominator transfer.

---

## 11. One bounded optional arithmetic check

No computation is needed for the proofs above.

If the coordinator wants one transcription check of the new adjacent identity, a bounded $k=11\to12$ check is sufficient. It avoids the closed $k\le10$ Smith work and does not duplicate the active $k=32$ calculation.

### Inputs

Generate exactly:

- $a_0,\ldots,a_{68}$;
- $\rho_0,\ldots,\rho_{34}$;
- $c_0,\ldots,c_{34}$ and $r_0,\ldots,r_{34}$;
- $\Lambda_{11}=\operatorname{lcm}(1,3,\ldots,61)$;
- $\lambda=\Lambda_{12}=\operatorname{lcm}(1,3,\ldots,67)$.

Here


$$
t=\lambda/\Lambda_{11}=67.
$$



Form the $22\times22$ and $24\times24$ original determinants, and the explicitly transformed $24\times24$ matrix of §4. Its inner $B_0$ has size $21\times21$.

### Expected verifiable outputs

1. The exact coefficient pairs of $H_{11}$ and $H_{12}$, with determinant certificates.

2. The exact integers $D,\mathcal K,\mathcal T$.

3. Coefficientwise verification of
   

$$
D^2F^+(s)-\mathcal K F(s)+\mathcal T=0,
$$


   where
   

$$
F(s)=\omega_{11}67^{11}H_{11}(s),
   \qquad
   F^+(s)=\omega_{12}H_{12}(s).
$$



4. Verification of
   

$$
D(F_0F_1^+-F_0^+F_1)-\lambda\mathcal T=0.
$$



5. If primitive pairs are also reported, their actual gcds should have divisibility and extended-Euclidean certificates, followed by verification of (5.3).

The denominator-free identities are valid regardless of whether the finite output $D$ vanishes. No $k=11$ sign or interlacing assertion is presumed. Such a calculation would check only this adjacent finite instance; it would not establish an infinite denominator theorem.

---

## 12. Final assessment

### Newly proved

- A nested, complete-moment representation with the parameter in one entry.
- The integral adjacent recurrence
  

$$
D^2F^+=\mathcal K F-\mathcal T.
$$


- The paid primitive resultant identity
  

$$
D\,t^kG_kG_{k+1}\Delta_k=(-1)^k\lambda\mathcal T.
$$


- Unconditional lower growth of actual primitive denominators, including quantitative lower growth on an infinite subset of the same original indices.
- A terminal-prime obstruction for the single alternative mixed construction in §8.

### Conditional deductions

An adjacent contraction estimate together with bounded primitive cross differences and balanced neighboring denominators would imply primitive decay and hence irrationality. Those arithmetic hypotheses are not proved.

### Auxiliary finite check

The optional $k=11\to12$ calculation checks the new recurrence and its normalization only. It has no infinite scope.

### Exact remaining bottleneck

The new recurrence exposes, but does not yet control, the reduced adjacent scalar


$$
\Delta_k
=
\frac{(-1)^k\lambda\mathcal T}
{D\,t^kG_kG_{k+1}}.
$$


The current analytic bounds neither determine the sign of every adjacent gap nor bound this primitive integer after both actual all-prime gcds.

For the global objective, the remaining requirement is still a nonzero whole primitive error tending to zero on an admissible infinite set:


$$
0<\frac{|H_k(e+\pi)|}{G_k}\longrightarrow0.
$$


No such sequence is established here.

The advance is therefore a concrete adjacent determinant mechanism and an evaluated primitive-denominator consequence—not an unconditional resolution of the rationality or irrationality of $e+\pi$.
