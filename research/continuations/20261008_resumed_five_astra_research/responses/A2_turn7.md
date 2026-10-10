> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A finite-depth $3$-adic analysis of the original mixed rectangles

## 1. Outcome and proof status

The rationality or irrationality of $e+\pi$ remains unresolved.

The principal odd-localized descent question also remains unresolved in this report:


$$
\mathcal W_k^{\mathrm{odd}}
\stackrel{?}{\in}
I_{2k-1}(Y_k)\,\mathbb Z[1/2],
\qquad k=9^{18+32u}.
$$


I do **not** produce dyadic Bézout coefficients for its original maximal minors, nor an odd-prime valuation exceeding the proposed allowance. In particular, the new result below is not presented as a certificate for that assertion.

There is, however, a new evaluated theorem for the **original, unweighted matrices at every original index**. It determines an entire initial segment of their $3$-primary Smith spectra, including actual depths rather than just ranks.

Write


$$
k=K_u=3^s,\qquad s=36+64u,
$$


and let $s_3(j)$ be the sum of the ternary digits of $j$. If $e_{A,i}$ are the $3$-adic valuations of the nonzero Smith invariant factors of $A=Y_k$ or $Z_k$, then, for


$$
1\le h\le 19+32u,
$$


the multiset of capped valuations is exactly


$$
\boxed{
\{\min(e_{A,i},h)\}_{i=1}^{2k-1}
=
\{\underbrace{0,\ldots,0}_{k}\}
\;\cup\;
\{\min(j-s_3(j),h):0\le j\le k-2\}.
}
\tag{1.1}
$$



This theorem:

* concerns the original physical rectangles, not a weighted stack;
* uses the complete integer entries $\Lambda_k\tau_n$;
* retains the contact atom in $Z_k$, where it supplies an additional local unit pivot;
* never reduces an unscaled arctangent coefficient through a denominator divisible by $3$;
* uses no moment beyond the original terminal;
* determines actual low-depth invariant factors, but does **not** determine either maximal-minor content.

A second new calculation sharpens the finite-jet height payment to its next constant:


$$
\boxed{
\log\mathscr R_k+\log\mathscr L_k
=
\log\mathscr C_{Z,k}+\log\mathscr C_{Y,k}
-8k^2\log k
+(24-18\log3)k^2+o(k^2).
}
\tag{1.2}
$$


The exact identity retaining $\zeta_{Z,k}$, $\chi_{Y,k}$, and every clearer is given below. Equation (1.2) is an evaluated **payment**, not an upper bound for the two jet contents.

The precise remaining difficulty is high-depth, all-prime arithmetic. The finite-depth theorem does not control the long remaining tails of the $3$-primary spectra, the other odd primes, or the actual required binary exponent.

---

## 2. Fixed original objects and source scope

### 2.1 Original sequences, matrices, and terminal

Retain


$$
a_0=1,\qquad a_d=1-da_{d-1},
$$




$$
u_n=a_{2n},\qquad f_n=(2n)!,\qquad w_n=(-1)^n,
\qquad c_n=u_n-w_n,
$$


and


$$
\rho_0=0,\qquad \rho_{n+1}+\rho_n=\frac1{2n+1},
\qquad r_n=-f_n+4\rho_n.
$$



The complete returns are


$$
\sigma_n=c_{n+1}+c_n=u_{n+1}+u_n
$$


and


$$
\boxed{
\tau_n=r_{n+1}+r_n
=-(2n+2)!-(2n)!+\frac4{2n+1}.
}
\tag{2.1}
$$



For every compact index $k\ge2$, put


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5).
$$


The original arrays are


$$
Z_k=
\left[
(c_{m+j})_{\substack{0\le m<2k\\0\le j<k}}
\ \middle|\
(\Lambda_k\tau_{m+j})_{\substack{0\le m<2k\\0\le j<k-1}}
\right]
\tag{2.2}
$$


and


$$
Y_k=
\left[
(\sigma_{m+j})_{\substack{0\le m<2k-1\\0\le j<k}}
\ \middle|\
(\Lambda_k\tau_{m+j})_{\substack{0\le m<2k-1\\0\le j<k}}
\right].
\tag{2.3}
$$



Thus $Z_k$ has shape $2k\times(2k-1)$, and $Y_k$ has shape
$(2k-1)\times2k$. Their actual maximal-minor contents are


$$
\mathscr R_k=\delta_{2k-1}(Z_k),\qquad
\mathscr L_k=\delta_{2k-1}(Y_k).
$$



The physical terminal remains


$$
\boxed{
\text{moment }3k-2,\qquad (6k-4)!,\qquad
\text{last odd denominator }6k-5.
}
\tag{2.4}
$$


The largest return index is $3k-3$.

### 2.2 Affine determinant and actual primitive normalization

Retain


$$
H_k(z)=
\det\left[
(c_{m+j})\ \middle|\
\bigl(\Lambda_k(r_{m+j}+z(-1)^{m+j})\bigr)
\right]
=H_{0,k}+H_{1,k}z.
\tag{2.5}
$$



Whenever $H_{1,k}\ne0$, the final gcd and primitive pair are


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|),
$$




$$
q_k=\frac{|H_{1,k}|}{G_k},\qquad
p_k=-\frac{\operatorname{sgn}(H_{1,k})H_{0,k}}{G_k}.
\tag{2.6}
$$


The universally valid signed identity is


$$
q_k(e+\pi)-p_k
=
\frac{\operatorname{sgn}(H_{1,k})H_k(e+\pi)}{G_k}.
\tag{2.7}
$$



On the supplied original nonvanishing and positivity domain,


$$
\boxed{
0<\ell_{K_u}
=q_{K_u}(e+\pi)-p_{K_u}
=\frac{|H_{K_u}(e+\pi)|}{G_{K_u}}.
}
\tag{2.8}
$$


Equivalently, if


$$
\epsilon_k=\left|e+\pi-\frac{p_k}{q_k}\right|,
$$


then $q_k\epsilon_k=|H_k(e+\pi)|/G_k$, and this equals $\ell_k>0$ on the original indices.

No content divisor below is substituted for $G_k$.

### 2.3 Results reused at their stated scope

The following are reused, not recalculated:

1. The bordered-content relations
   

$$
\boxed{
   \operatorname{lcm}(\mathscr R_k,\mathscr L_k)
   \mid G_k\mid \Lambda_k\mathscr R_k\mathscr L_k.
   }
   \tag{2.9}
$$



2. The exact finite-jet content transfers, including their actual corrections.

3. The source-specific result, locally checked by the parent and reserved for later independent audit,
   

$$
\mathcal W_k\notin I_{2k-1}(Y_k)\qquad(k\ge18).
   \tag{2.10}
$$


   Its binary proof is not reattempted here.

4. The established binary lower bounds
   

$$
v_2(\mathscr L_k)\ge\nu^Y_k,\qquad
   v_2(\mathscr R_k)\ge\nu^Z_k.
   \tag{2.11}
$$



5. The supplied analytic estimate, only on its stated original-index scope,
   

$$
\log|H_k(e+\pi)|=4k^2\log k+O(k^2).
   \tag{2.12}
$$



The selected $k=6,7,8$ JSON does not reproduce its large minor and Bézout arrays. Its flag and hashes are not, by themselves, mathematical proofs of the contents. The assignment reports that the full receipts were checked; I use their conclusions only at those finite scales. No new theorem below depends on those numerical contents.

No closed $k=3$, $k=4$, $k=5$, $k=6$–$8$, $32/33$, weighted-stack, or pure-contact Smith computation is repeated.

---

## 3. What the odd-localized assertion requires

Define


$$
\mathcal W_k^{\mathrm{odd}}
=
3^{2k}\Lambda_k^k
\left(\prod_{j=0}^{k-1}\operatorname{odd}(j!)\right)^4.
\tag{3.1}
$$



Because the original maximal-minor ideal is


$$
I_{2k-1}(Y_k)=\mathscr L_k\mathbb Z,
$$


the proposed assertion is equivalent to


$$
\boxed{
\operatorname{odd}(\mathscr L_k)\mid
\mathcal W_k^{\mathrm{odd}}.
}
\tag{3.2}
$$


For each odd prime $p$, its exact allowance is


$$
B_p(k)=
k\bigl(2\mathbf1_{p=3}+v_p(\Lambda_k)\bigr)
+4\sum_{j=0}^{k-1}v_p(j!).
\tag{3.3}
$$


Thus one needs


$$
v_p(\mathscr L_k)\le B_p(k)
\quad\text{for every odd }p.
\tag{3.4}
$$


In particular, $B_p(k)=0$ for $p>6k-5$.

If (3.2) holds, the least possible binary exponent in an integer identity


$$
\sum_j\beta_jM_{k,j}
=
2^a\mathcal W_k^{\mathrm{odd}}
\tag{3.5}
$$


is


$$
\boxed{a=v_2(\mathscr L_k),}
\tag{3.6}
$$


where the $M_{k,j}$ are the actual signed maximal minors.

Indeed, every integer combination on the left is divisible by $\mathscr L_k$. Conversely, an actual Bézout identity for their gcd, multiplied by
$\mathcal W_k^{\mathrm{odd}}/\operatorname{odd}(\mathscr L_k)$, gives (3.5) with that exponent.

This equivalence does not construct the required coefficients. In particular, the proved lower bound $\nu^Y_k$ cannot be substituted for the actual exponent in (3.6).

---

## 4. New theorem: a capped $3$-primary Smith spectrum

The next result is finite algebra on the original arrays. Its proof is independent of the weighted stack.

### Theorem 4.1

Let


$$
k=3^s,\qquad s\ge4,
$$


and let


$$
1\le h\le \left\lfloor\frac{s+2}{2}\right\rfloor.
\tag{4.1}
$$


For $A=Y_k$ or $Z_k$, let


$$
e_{A,1}\le\cdots\le e_{A,2k-1}
$$


be the $3$-adic Smith valuations, allowing $+\infty$ if a rational-rank deficiency were present.

Then


$$
\boxed{
\{\min(e_{A,i},h)\}_{i=1}^{2k-1}
=
\{\underbrace{0,\ldots,0}_{k}\}
\cup
\{\min(2v_3(j!),h):0\le j\le k-2\}.
}
\tag{4.2}
$$


Equivalently, by Legendre’s formula,


$$
2v_3(j!)=j-s_3(j),
$$


so (4.2) is exactly (1.1).

At the original indices $s=36+64u$, the theorem applies through


$$
h=19+32u.
$$



### 4.1 Finite periodicity of the actual contact sequence

For every positive integer $Q$,


$$
a_{n+Q}\equiv a_n\pmod Q.
\tag{4.3}
$$


To prove this, observe first that


$$
a_Q=1-Qa_{Q-1}\equiv1=a_0\pmod Q.
$$


If $a_{Q+n-1}\equiv a_{n-1}$, the original recurrence gives


$$
a_{Q+n}
=1-(Q+n)a_{Q+n-1}
\equiv1-na_{n-1}
=a_n\pmod Q.
$$



Consequently, for odd $Q$,


$$
u_{n+Q}\equiv u_n,\qquad
\sigma_{n+Q}\equiv\sigma_n\pmod Q.
\tag{4.4}
$$


The atom $w_n=(-1)^n$ is not $Q$-periodic when $Q$ is odd. That distinction will be used, rather than suppressed, in the $Z_k$ proof.

Only congruences between physical entries and lower-index entries will be used. No additional moment is required.

### 4.2 A unit return block at $3$

Put


$$
Q=3^h,\qquad
n_0=\frac{3k-1}{2}.
\tag{4.5}
$$


Since


$$
3^{s+1}=3k\le6k-5<3^{s+2},
$$


we have


$$
v_3(\Lambda_k)=s+1.
\tag{4.6}
$$



Write the complete integer return entry as


$$
T_n=\Lambda_k\tau_n
=
-\Lambda_k\bigl((2n+2)!+(2n)!\bigr)
+\frac{4\Lambda_k}{2n+1}.
\tag{4.7}
$$


Every quotient in (4.7) is an integer within the physical range.

Because $h\le s+1$, the factorial part of (4.7) vanishes modulo $Q$. Thus


$$
T_n\equiv \frac{4\Lambda_k}{2n+1}\pmod Q.
\tag{4.8}
$$


This is a congruence for an **integer quotient**. It is not an attempt to interpret $1/(2n+1)$ modulo $3^h$.

Modulo $3$, the only nonzero return entry occurs when


$$
2n+1=3k,
$$


namely at $n=n_0$. Therefore


$$
T_n\equiv
\gamma\,\mathbf1_{n=n_0}\pmod3,
\qquad
\gamma=\frac{4\Lambda_k}{3k}\not\equiv0\pmod3.
\tag{4.9}
$$



Let $r$ denote the number of return columns:


$$
r=k\quad\text{for }Y_k,\qquad
r=k-1\quad\text{for }Z_k.
$$


Select and order the physical pivot rows as


$$
m_i=n_0-i,\qquad 0\le i<r.
\tag{4.10}
$$


The corresponding $r\times r$ return block


$$
M_{ij}=T_{n_0-i+j}
$$


satisfies


$$
M\equiv\gamma I_r\pmod3.
\tag{4.11}
$$


Hence it is invertible over $\mathbb Z_{(3)}$, and over $\mathbb Z/Q\mathbb Z$.

These are actual original rows. For $Y_k$, the selected rows are


$$
\frac{k+1}{2},\ldots,\frac{3k-1}{2};
$$


for $Z_k$, they are


$$
\frac{k+3}{2},\ldots,\frac{3k-1}{2}.
$$



### 4.3 The support separation valid through depth $h$

Set


$$
D=3^{s+2-h}.
\tag{4.12}
$$


The restriction $2h\le s+2$ implies


$$
Q\mid D.
\tag{4.13}
$$



Equation (4.8) shows that


$$
T_n\not\equiv0\pmod Q
\quad\Longrightarrow\quad
D\mid 2n+1.
\tag{4.14}
$$


For the pivot block,


$$
2(n_0-i+j)+1=3k+2(j-i).
$$


Since $D\mid3k$, a nonzero entry modulo $Q$ requires


$$
D\mid j-i.
\tag{4.15}
$$


In particular, $M$ and $M^{-1}$ are block diagonal modulo $Q$ with respect to the residue classes of the column index modulo $Q$.

For a free row $m$, a nonzero return entry in column $j$ requires


$$
m+j\equiv n_0\pmod Q.
\tag{4.16}
$$



This is the source-specific support fact that makes the following Schur reduction evaluable.

### 4.4 Schur reduction of the contact-return columns

Partition rows into pivot rows $P$ and free rows $F$. Temporarily order return columns first. For any contact block $C$, the corresponding Schur complement is


$$
S=C_F-T_FM^{-1}C_P.
\tag{4.17}
$$



First take $C_{m,c}=\sigma_{m+c}$. By (4.4), the pivot contact row with index $i$ is, modulo $Q$,


$$
(C_P)_{i,c}=\sigma_{n_0-i+c}.
$$


Because $M^{-1}_{j,i}=0$ unless $i\equiv j\pmod Q$,


$$
(M^{-1}C_P)_{j,c}
=d_j\,\sigma_{n_0-j+c}
\tag{4.18}
$$


for a scalar $d_j\in\mathbb Z/Q\mathbb Z$.

When $T_F(m,j)\ne0$, equation (4.16) makes


$$
\sigma_{n_0-j+c}=\sigma_{m+c}\pmod Q.
$$


Thus


$$
S_{m,c}=\eta_m\sigma_{m+c}\pmod Q,
\tag{4.19}
$$


where


$$
\eta_m=
1-\sum_jT_F(m,j)d_j.
$$



All entries of $T_F$ vanish modulo $3$, because the unit-return antidiagonal has already been placed in $P$. Hence


$$
\eta_m\equiv1\pmod3.
\tag{4.20}
$$


Every $\eta_m$ is therefore a unit modulo $Q$.

The result is stronger than a rank calculation: after legitimate local unit operations, the residual contact-return block is exactly a row-unit multiple of the original periodic $\sigma$-block modulo $Q$.

### 4.5 Completion for $Y_k$

For $Y_k$, there are $k$ return pivots. Its free rows number $k-1$, and its first free interval is


$$
0,\ldots,\frac{k-1}{2}.
$$


Under (4.1), $h\le s-1$, so


$$
Q=3^h\le k/3.
$$


Thus the free interval contains $0,\ldots,Q-1$, and the contact shifts also contain $0,\ldots,Q-1$.

After dividing rows by the units $\eta_m$, the remaining matrix is


$$
(\sigma_{m+c})_{\substack{m\in F\\0\le c<k}}
\pmod Q.
$$


Its rows and columns repeat with period $Q$. Integer row and column subtractions reduce the repetitions to zero, leaving the $Q\times Q$ block


$$
\Sigma_Q=(\sigma_{a+b})_{0\le a,b<Q}.
\tag{4.21}
$$



Hence, modulo $Q$, $Y_k$ is equivalent to:

* $k$ unit diagonal entries;
* the block $\Sigma_Q$;
* zero rows or columns completing the original rectangular shape.

### 4.6 Completion for $Z_k$: the atom supplies a unit

For $Z_k$, first make the integer unit-triangular contact-column transformation


$$
(c_0,c_1,\ldots,c_{k-1})
\longmapsto
(c_0,\sigma_0,\ldots,\sigma_{k-2}),
\tag{4.22}
$$


where notation denotes entire shifted columns. Indeed, the new column $\sigma_j$ is the sum of the old columns $c_j+c_{j+1}$.

There are $k-1$ return pivots. The calculation above applies to all $k-1$ $\sigma$-columns. For the remaining $c_0=u_0-w_0$ column, the periodic $u$-part is transformed by the same row factor $\eta_m$, while the atom gives a separate vector.

After dividing free rows by $\eta_m$, the remaining contact columns therefore have the form


$$
u_m-b_m,\qquad
\sigma_m,\ldots,\sigma_{m+k-2},
\tag{4.23}
$$


where


$$
b_m\equiv w_m\pmod3.
\tag{4.24}
$$



Since $Q$ is odd and $u$ is $Q$-periodic modulo $Q$,


$$
\frac12\sum_{j=0}^{Q-1}(-1)^j\sigma_{m+j}
=
\frac{u_m+u_{m+Q}}2
\equiv u_m\pmod Q.
\tag{4.25}
$$


All these $\sigma$-columns are present: $Q\le k-1$. The division by $2$ is a unit operation modulo $3^h$.

Subtracting (4.25) from the first column in (4.23) leaves $-b_m$. The free rows include both $m=0$ and $m=Q$. Their $\sigma$-rows agree modulo $Q$, but


$$
b_Q-b_0\equiv (-1)^Q-1=-2\not\equiv0\pmod3.
\tag{4.26}
$$


The row difference $Q-0$ therefore gives a unit pivot in the retained atom column and zero entries in all the $\sigma$-columns.

Eliminating that atom pivot does not alter the remaining $\sigma$-block. The first $Q$ free rows remain available, and periodic reduction again leaves $\Sigma_Q$.

Thus $Z_k$ has:

* $k-1$ unit return pivots;
* one unit pivot supplied by the contact atom;
* the same block $\Sigma_Q$;
* the remaining zero rows and columns.

The atom has not been deleted. Its nonperiodicity is exactly what produces the additional unit.

### 4.7 Evaluation of the cyclic contact block

It remains to evaluate $\Sigma_Q$. This uses the standard factorial Gram factorization, with its hypotheses checked explicitly.

Let


$$
U_Q=(u_{a+b})_{0\le a,b<Q}.
$$


If $P$ is the cyclic row-shift matrix, then


$$
\Sigma_Q=(I+P)U_Q\pmod Q.
$$


Since $Q$ is odd and $P^Q=I$,


$$
(I+P)^{-1}
=\frac12\sum_{j=0}^{Q-1}(-P)^j.
\tag{4.27}
$$


Thus $I+P$ is a unit matrix modulo $Q$.

Multiplication of indices by $2$ permutes the residue classes modulo $Q$. Using the periodicity of $a_n$,


$$
u_{a+b}=a_{2(a+b)}
$$


shows that $U_Q$ is row-and-column permutation equivalent modulo $Q$ to


$$
A_Q=(a_{r+t})_{0\le r,t<Q}.
\tag{4.28}
$$



The original recurrence gives the finite identity


$$
a_d=\sum_{j=0}^d(-1)^j\binom dj j!.
\tag{4.29}
$$


It follows that


$$
\Delta^j a_0=(-1)^j j!.
$$


The finite double-Pascal transformation therefore sends $A_Q$ to


$$
((-1)^{r+t}(r+t)!)_{0\le r,t<Q}.
$$


Removing row and column signs leaves the factorial Hankel matrix


$$
F_Q=((r+t)!)_{0\le r,t<Q}.
$$



For completeness, its needed Gram factorization is


$$
F_Q=L\,\operatorname{diag}((j!)^2)_{j=0}^{Q-1}L^T,
\tag{4.30}
$$


where


$$
L_{rj}=
\begin{cases}
\displaystyle \binom rj\frac{r!}{j!},&j\le r,\\
0,&j>r.
\end{cases}
$$


This $L$ is integer unit lower triangular. The entry identity is simply


$$
\sum_j
\binom rj\frac{r!}{j!}(j!)^2
\binom tj\frac{t!}{j!}
=
r!t!\sum_j\binom rj\binom tj
=(r+t)!.
$$


Thus no factorial division has been declared a unit.

Consequently,


$$
\Sigma_Q
\sim
\operatorname{diag}((j!)^2)_{j=0}^{Q-1}
\pmod{3^h}.
\tag{4.31}
$$



Combining Sections 4.5–4.7 gives $k$ unit factors followed by these factorial-square factors. For $j\ge Q$, one has $2v_3(j!)\ge h$; therefore the zero factors completing the rectangle can be written as the capped terms with $Q\le j\le k-2$. This proves (4.2). ∎

### 4.8 Boundary and division audit

Every operation above is on an original finite block.

* The return pivots are original rows and columns.
* All return entries retain their factor $\Lambda_k$.
* The factorial part is removed only in a congruence where its valuation has been proved at least $h$.
* No unscaled $1/(2n+1)$ is reduced modulo $3^h$.
* The largest original return index remains $3k-3$.
* The largest underlying moment remains $3k-2$.
* The cyclic blocks use only lower-index contact values already inside that boundary.
* The local divisions are by units in $\mathbb Z_{(3)}$ or $\mathbb Z/3^h\mathbb Z$.

The last point is important: a $3$-local unit need not be a dyadic unit. These operations do not constitute a certificate over $\mathbb Z[1/2]$.

---

## 5. Explicit consequences at every original index

The uniform choice $h=19$ is available for every $K_u$. The valuations below $19$ are fully evaluated:

| $3$-adic valuation | Multiplicity in either original rectangle |
|---:|---:|
| $0$ | $k+3$ |
| $2$ | $3$ |
| $4$ | $3$ |
| $8$ | $3$ |
| $10$ | $3$ |
| $12$ | $3$ |
| $16$ | $3$ |
| $18$ | $3$ |
| at least $19$ | $k-25$ |

Indeed, for $j=0,\ldots,23$, the values $2v_3(j!)$ occur in blocks of three:


$$
0,\ 2,\ 4,\ 8,\ 10,\ 12,\ 16,\ 18.
$$


At $j=24$, the value is $20$, so every later value is at least $19$.

In particular,


$$
\boxed{
\operatorname{rank}_{\mathbb F_3}Y_k
=
\operatorname{rank}_{\mathbb F_3}Z_k
=k+3
}
\tag{5.1}
$$


at every original index. More substantially, neither matrix has a Smith factor of valuation $1,3,5,6,7,9,11,13,14,15,$ or $17$.

The sum of the known positive valuations is


$$
3(2+4+8+10+12+16+18)=210.
$$


Hence the following are actual determinantal-ideal statements:


$$
\boxed{
v_3\bigl(\delta_{k+24}(Y_k)\bigr)
=
v_3\bigl(\delta_{k+24}(Z_k)\bigr)
=210.
}
\tag{5.2}
$$


These are ideals of smaller minors, not the maximal-minor ideals requested in the odd-descent problem.

The capped total valuation is


$$
\boxed{
\sum_{i=1}^{2k-1}\min(e_{A,i},19)
=19k-265.
}
\tag{5.3}
$$


The two original maximal-minor contents thus have identical $3$-primary front ends through this depth. Their deeper tails remain undetermined.

---

## 6. Why this does not prove or disprove odd descent

### 6.1 The exact $3$-adic allowance

At $k=3^s$,


$$
v_3(\Lambda_k)=s+1.
$$


Also,


$$
\begin{aligned}
\sum_{j=0}^{k-1}v_3(j!)
&=\sum_{a=1}^s\sum_{j=0}^{k-1}\left\lfloor\frac{j}{3^a}\right\rfloor\\
&=\frac{k}{2}\sum_{a=1}^s\left(\frac{k}{3^a}-1\right)
=\frac{k(k-1-2s)}4.
\end{aligned}
$$


Therefore


$$
\boxed{
v_3(\mathcal W_k^{\mathrm{odd}})
=k^2+(2-s)k.
}
\tag{6.1}
$$



The new theorem does not show that the complete valuation of either content exceeds or is bounded by (6.1).

For comparison, the already proved contact-minor divisibility gives the lower bound


$$
v_3(\mathscr R_k),\,v_3(\mathscr L_k)
\ge 2\sum_{j=0}^{k-2}v_3(j!)
=
\frac{(k-2)(k-1-2s)}2.
\tag{6.2}
$$


Its difference from the proposed allowance is


$$
\boxed{
k^2+(2-s)k
-\frac{(k-2)(k-1-2s)}2
=
\frac{k^2+7k-2-4s}{2}>0.
}
\tag{6.3}
$$


Thus the established factorial lower divisor supplies no $3$-adic disproof of the odd target.

### 6.2 The exact obstruction to extending the new argument

Two finite-depth restrictions were used.

First, the complete factorial contribution in $\Lambda_k\tau_n$ vanishes modulo $3^h$ only under the proved payment $h\le s+1$.

Second, the contact-period argument needs


$$
3^h\mid3^{s+2-h},
$$


that is,


$$
2h\le s+2.
$$


Beyond that depth, nonzero return entries need not preserve the contact residue classes modulo $3^h$. The row-scalar identity (4.19) is then no longer justified.

This is a precise mathematical obstruction, not merely a missing computation. Reusing (4.19) at larger depths would discard genuine cross-residue terms. Reusing (4.8) without its valuation restriction would additionally discard the complete factorial forcing.

The allowance (6.1) is quadratic in $k$, while the controlled depth is only $O(\log k)$. The theorem therefore does not reach the relevant high-depth tail.

### 6.3 Why the local reductions are not dyadic Bézout coefficients

The pivot determinant in (4.11) is a unit at $3$, but it can have other odd prime divisors. Inverting it is valid for the present $3$-primary analysis; it is not automatically valid over $\mathbb Z[1/2]$.

Thus there are two separate unpaid steps in any attempted promotion:

1. control the deeper $3$-primary tail;
2. replace the prime-local inverses by an actual simultaneous odd-prime certificate.

Neither follows from the capped Smith spectrum.

### 6.4 A concrete next high-depth lemma

A falsifiable, source-specific next target at the prime $3$ is the following.

Let $M_k^{(0)}$ and $M_k^{(k-1)}$ be the two actual maximal minors of $Y_k$ obtained by omitting, respectively, the first and last contact-return columns. Both retain **all $k$ original scaled return columns**.

A sufficient next lemma would be


$$
\boxed{
\min\!\left(
v_3(M_k^{(0)}),\,v_3(M_k^{(k-1)})
\right)
\le k^2+(2-s)k,
\qquad k=3^s=K_u.
}
\tag{6.4}
$$


Here $v_3(0)=+\infty$.

This is stronger than necessary for the $3$-part of odd descent, but it specifies two original cofactors rather than an unspecified state or augmented matrix. The actual unit return block from Section 4 gives an exact $3$-local Schur expression for each cofactor. What remains is to evaluate or bound those complete high-depth determinants, including the cross-residue and factorial terms that the finite-depth theorem cannot remove.

Equation (6.4) is an **open follow-on lemma**, not a consequence of Theorem 4.1. Even its proof would settle only the $3$-part, not all odd primes.

---

## 7. Exact finite-jet objects and retained payments

The new local theorem does not change the finite-jet arrays.

For clarity, they can be identified directly by finite formulas, without invoking an infinite characteristic-$p$ series. Put


$$
h_Z=2k-3,\quad b_Z=2k-1,
\qquad
h_Y=2k-1,\quad b_Y=2k+1.
$$


For a finite input column $y$, define


$$
(T_\star y)_m
=
\sum_{r=0}^{m}
(-1)^r\binom{b_\star}{r}
(2m-2r+1)_{h_\star+2r}\,y_{m-r}.
\tag{7.1}
$$


The ranges are $m<2k$ for $Z$ and $m<2k-1$ for $Y$.

These transformations factor as


$$
T_\star=D_\star S_\star,
$$


where $S_\star$ is integer unit lower triangular and


$$
(D_Z)_{mm}=(2m+1)_{2k-3},
\qquad
(D_Y)_{mm}=(2m+1)_{2k-1}.
\tag{7.2}
$$


Indeed,


$$
(S_\star)_{m,m-r}
=
(-1)^r\binom{b_\star}{r}
\frac{(2m)!}{(2m-2r)!}.
$$


The largest factor in the diagonal payments is $6k-5$.

The established integer jet arrays are


$$
\mathbf J_{Z,k}
=
T_Z[\,c_{m+j}\mid \tau_{m+j}\,],
\qquad
\mathbf J_{Y,k}
=
T_Y[\,\sigma_{m+j}\mid \tau_{m+j}\,].
\tag{7.3}
$$


The complete $\tau$ from (2.1) is used in every term of (7.1). Its odd denominators are absorbed by the displayed rising factorials. There is no omitted forcing column or commutator shortcut in this finite definition.

Let their actual contents be


$$
\mathscr C_{Z,k}=\delta_{2k-1}(\mathbf J_{Z,k}),
\qquad
\mathscr C_{Y,k}=\delta_{2k-1}(\mathbf J_{Y,k}).
$$



Retain


$$
t_Z=\prod_{m=0}^{2k-1}(2m+1)_{2k-3},
\qquad
t_Y=\prod_{m=0}^{2k-2}(2m+1)_{2k-1}.
\tag{7.4}
$$



If $\mathbf v$ is the actual primitive signed cofactor vector of $S_ZZ_k$, retain its actual least simultaneous clearer


$$
\boxed{
\zeta_{Z,k}
=
\operatorname{lcm}_{0\le m<2k}
\frac{(2m+1)_{2k-3}}
{\gcd((2m+1)_{2k-3},|v_m|)}.
}
\tag{7.5}
$$


For the $Y$-jet minor-type gcds $a_Y,b_Y$, retain


$$
\boxed{
\chi_{Y,k}
=
\frac{\gcd(\Lambda_ka_Y,b_Y)}{\gcd(a_Y,b_Y)},
\qquad \chi_{Y,k}\mid\Lambda_k.
}
\tag{7.6}
$$



The exact content transfers remain


$$
\boxed{
\mathscr R_k=
\frac{\Lambda_k^{k-1}\mathscr C_{Z,k}\zeta_{Z,k}}{t_Z},
\qquad
\mathscr L_k=
\frac{\Lambda_k^{k-1}\mathscr C_{Y,k}\chi_{Y,k}}{t_Y}.
}
\tag{7.7}
$$


Neither correction is assigned the value $1$.

Also unchanged are:

* the individual original right-column clearers
  

$$
\Lambda_{k,j}=\operatorname{lcm}(1,3,\ldots,4k+2j-3);
$$


* the complete return-array clearer $\Lambda_k$;
* the previously established contact-frame contents and divided-contact factorial payments—no contact column is divided by them in the new proof;
* the actual least simultaneous coefficient clearer of $H_k/\Lambda_k^k$,
  

$$
\boxed{
  \frac{\Lambda_k^k}{d_{H,k}},
  \qquad
  d_{H,k}=\gcd(\Lambda_k^k,H_{0,k},H_{1,k});
  }
  \tag{7.8}
$$


* its remaining coefficient content $G_k/d_{H,k}$;
* the final all-prime gcd $G_k$ and primitive denominator $q_k=|H_{1,k}|/G_k$.

---

## 8. New evaluation of the critical next height constant

### 8.1 The two row-payment products

Consider the base product


$$
T_0(k)=
\prod_{m=0}^{2k-1}\prod_{r=1}^{2k}(2m+r).
$$


Deleting the finitely many boundary strips distinguishing $t_Z,t_Y$ from this product changes its logarithm by $O(k\log k)$. A Riemann-sum calculation gives


$$
\log T_0(k)
=
4k^2\log k
+k^2\int_0^2\int_0^2\log(2x+y)\,dy\,dx
+O(k\log k).
$$


The logarithmic singularity at the origin is integrable; the boundary-cell contribution is absorbed in the displayed error.

The integral is explicitly


$$
\begin{aligned}
\int_0^2\int_0^2\log(2x+y)\,dy\,dx
&=\frac12\int_0^4\int_0^2\log(u+y)\,dy\,du\\
&=9\log3-6.
\end{aligned}
$$


Therefore


$$
\boxed{
\log t_Z=\log t_Y
=
4k^2\log k+(9\log3-6)k^2+O(k\log k),
}
\tag{8.1}
$$


where the equality means that both have the displayed expansion, not that the products are equal.

Taking logarithms in the exact identities (7.7) yields


$$
\begin{aligned}
\log\mathscr R_k+\log\mathscr L_k
={}&
\log\mathscr C_{Z,k}+\log\mathscr C_{Y,k}
-8k^2\log k\\
&+2(k-1)\log\Lambda_k
-(18\log3-12)k^2\\
&+\log\zeta_{Z,k}+\log\chi_{Y,k}
+O(k\log k).
\end{aligned}
\tag{8.2}
$$


This form retains the actual corrections explicitly.

Now


$$
\log\zeta_{Z,k}=O(k\log k),\qquad
\log\chi_{Y,k}=O(k).
$$


Also, the standard prime number theorem for the lcm gives


$$
\log\Lambda_k=6k+o(k).
$$


Indeed, $\Lambda_k$ is the odd part of $\operatorname{lcm}(1,\ldots,6k-5)$.

Consequently,


$$
\boxed{
\log\mathscr R_k+\log\mathscr L_k
=
\log\mathscr C_{Z,k}+\log\mathscr C_{Y,k}
-8k^2\log k
+(24-18\log3)k^2+o(k^2).
}
\tag{8.3}
$$



This sharpens the previous $O(k^2)$ payment. It does not bound the unknown jet contents.

### 8.2 Height of the odd certificate and the actual binary payment

The standard finite factorial summation gives


$$
\sum_{j=0}^{k-1}\log(j!)
=
\frac12k^2\log k-\frac34k^2+O(k\log k).
$$


Furthermore,


$$
\sum_{j=0}^{k-1}v_2(j!)
=\frac12k^2+O(k\log k).
$$


Thus


$$
\boxed{
\log\mathcal W_k^{\mathrm{odd}}
=
2k^2\log k+(3-2\log2)k^2+o(k^2).
}
\tag{8.4}
$$



Suppose, conditionally, that odd descent were proved for both rectangles. Write the **actual** binary depths as


$$
a_Y=v_2(\mathscr L_k),\qquad
a_Z=v_2(\mathscr R_k).
$$


Then


$$
\log\mathscr R_k+\log\mathscr L_k
\le
(a_Y+a_Z)\log2+2\log\mathcal W_k^{\mathrm{odd}}.
\tag{8.5}
$$



If one additionally proved


$$
a_Y+a_Z\le A k^2+o(k^2),
$$


then


$$
\log G_k
\le
4k^2\log k+
\bigl(A\log2+6-4\log2\bigr)k^2+o(k^2).
\tag{8.6}
$$


This still reaches only the critical leading coefficient $4$.

No such useful binary upper bound is proved here. The established lower bounds cannot supply it. The accepted size estimate gives only the much weaker


$$
a_Y,a_Z
\le \frac{\log\mathcal U_k}{\log2}
=
\frac4{\log2}k^2\log k+O(k^2),
$$


not $O(k^2)$.

### 8.3 Exact critical comparison still needed

For example, if future work established


$$
\log\mathscr C_{Z,k}+\log\mathscr C_{Y,k}
\le 12k^2\log k+C_Jk^2+o(k^2)
$$


and


$$
\log|H_k(e+\pi)|
\ge 4k^2\log k+C_Hk^2+o(k^2),
$$


then (2.9) and (8.3) would force whole-error divergence provided


$$
\boxed{
C_H>C_J+24-18\log3.
}
\tag{8.7}
$$


This is a conditional implication with an evaluated payment constant. Neither required content bound nor the required critical analytic comparison is supplied by the present theorem.

A strict leading bound


$$
\log\mathscr C_{Z,k}+\log\mathscr C_{Y,k}
\le(12-\eta)k^2\log k+O(k^2)
$$


would, as before, force divergence. That would retire this compact producer as a source of primitive whole-error decay; it would not prove $e+\pi$ rational.

---

## 9. The separate binary producer is unchanged

No compact conclusion is transferred to the separate binary producer. Its domain and physical terminal remain


$$
b=9^{18+32u},\qquad n=4002b,\qquad
j=0,\ldots,b-1,\qquad z_b=0.
$$



Its complete corrected columns remain


$$
x=\frac12RA^{-1}f,\qquad
y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},
\qquad x=2^ax_0,
$$


and its complete return remains


$$
S=\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f.
$$


Only the supplied paid estimate


$$
v_2\!\left(\frac{S}{2^{a+1}}\right)\ge\chi-a,
\qquad
\chi=v_2\binom{n+b-1}{b-1},
$$


is retained.

Its $Q=x_0^Tx_0$, corrected-column contents, actual least simultaneous clearer, actual primitive denominator, and final all-prime gcd are not altered or replaced by compact quantities.

---

## 10. A bounded new arithmetic audit

No computation is needed for Theorem 4.1 or the next-constant calculation. Their proofs above are finite algebra and explicit summation.

If the coordinator wants a new arithmetic audit of the source-specific Schur reduction, the following bounded test checks the endpoint of its depth hypothesis without reopening a closed scale.

### Inputs



$$
k=81=3^4,\qquad h=3,\qquad \text{modulus }27.
$$


Use exactly the original recurrences and


$$
\Lambda_{81}=\operatorname{lcm}(1,3,\ldots,481).
$$



The physical inputs are bounded by

* moment $241$;
* factorial $482!$;
* last odd denominator $481$;
* $Z_{81}$ of shape $162\times161$;
* $Y_{81}$ of shape $161\times162$.

Reduce the complete integer entries $\Lambda_{81}\tau_n$, not the unscaled rational $\tau_n$.

The return pivot rows are

* $121,120,\ldots,41$ for $Y_{81}$;
* $121,120,\ldots,42$ for $Z_{81}$.

### Expected verifiable outputs

For each original rectangle, its Smith form over $\mathbb Z/27\mathbb Z$ has diagonal profile


$$
\boxed{
1^{[84]},\qquad 9^{[3]},\qquad 0^{[74]},
}
\tag{10.1}
$$


with the extra zero row or column required by its rectangular shape.

A verifiable receipt can consist of unit row and column operations modulo $27$, or equivalent pivot witnesses, establishing:

1. $84$ unit pivots;
2. after those pivots, every remaining entry is divisible by $9$;
3. after division of that residual block by $9$, its rank modulo $3$ is exactly $3$.

The predicted rank modulo $3$ is therefore $84$, and the predicted capped total valuation is


$$
3\cdot2+74\cdot3=228.
$$



This is an auxiliary finite audit of a theorem already derived above. It is not a test of all-prime odd descent, not a computation of either full content, and not a claim of normality at growing good primes. Any execution would require a separate coordinator scope check and parent-authored bounded implementation.

---

## 11. Proof-status ledger

| Statement | Status |
|---|---|
| Integral descent $\mathcal W_k\in I_{2k-1}(Y_k)$ for original $k$ | **Already disproved in the supplied work**; not reattempted |
| Capped $3$-primary Smith spectrum (4.2) for the original $Y_k,Z_k$ | **New proof**, including every original index |
| Contact atom retained and evaluated as a local unit in $Z_k$ | **New proof** |
| Actual valuations in the table of Section 5 | **New evaluated consequence**, not a finite experiment |
| Exact local ideal valuation $v_3(\delta_{k+24})=210$ | **New proof** at all original indices |
| Odd-localized maximal-minor descent for $Y_k$ | **Open** |
| Corresponding odd-localized descent for $Z_k$ | **Open** |
| Actual dyadic Bézout coefficients on original maximal minors | **Not constructed** |
| Useful upper bound $v_2(\mathscr L_k),v_2(\mathscr R_k)=O(k^2)$ | **Open** |
| Next constant $24-18\log3$ in the paid jet-content transfer | **New explicit evaluation** |
| Strict combined content estimate or decisive critical-constant comparison | **Open** |
| Proposed $k=81$, modulus $27$ audit | **Bounded auxiliary calculation, not executed** |
| Nonzero primitive whole-error decay or divergence at $K_u$ | **Open** |
| Rationality or irrationality of $e+\pi$ | **Unresolved** |

## Final conclusion

The new original-family result is an explicit $3$-adic finite-depth normal form for both unweighted rectangles. At every original index, it determines their Smith valuations through depth $19+32u$; at the uniform depth $19$, it gives the fully evaluated spectrum in Section 5 and the actual local determinantal-ideal valuation $210$.

The proof retains the complete scaled forcing, original rows and columns, contact atom, and physical terminal. Its limitation is equally explicit: beyond $2h\le s+2$, the return support no longer preserves the relevant contact residue classes, and the high-depth Schur terms cannot be removed. Local pivot inverses also do not become dyadic inverses automatically.

Accordingly, the main odd-descent obligation is still open. What remains is an actual all-odd-prime maximal-minor certificate or a genuine violating depth, followed—if descent holds—by an upper bound paying the **actual** binary exponents. At the critical combined height, the newly evaluated payment constant must also be included in the whole-error comparison.

The final all-prime gcd remains $G_k$, the primitive denominator remains $|H_{1,k}|/G_k$, and the relevant nonzero whole error remains $|H_k(e+\pi)|/G_k$ at the same infinite original indices. No conclusion about the rationality of $e+\pi$ follows yet.
