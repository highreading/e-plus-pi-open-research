> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3 Turn 14: Columnwise arithmetic compression and the remaining all-prime content problem

## 1. Result and proof status

The rationality or irrationality of $e+\pi$ remains unresolved.

This report makes a new, explicit arithmetic reduction of the **actual coefficient content**


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|).
$$


It does **not** establish the requested upper bound


$$
\log G_k\le (2-\varepsilon)k^2\log k+O(k^2),
$$


nor a common divisor large enough to prove primitive decay using the established whole-error upper bound.

The principal new proved result is an evaluated divisor arising from the complete rational moment columns. Define


$$
\Lambda_{k,j}
=\operatorname{lcm}(1,3,\ldots,4k+2j-3),
\qquad 0\le j<k,
$$


and


$$
\boxed{
E_k=\frac{\Lambda_k^k}{\prod_{j=0}^{k-1}\Lambda_{k,j}},
\qquad
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5).
}
$$


Then:

1. $\Lambda_{k,j}$ is the **actual least clearer of the complete raw rational moment column** indexed by $j$.
2. $E_k$ is an integer and divides both original coefficients.
3. More strongly,
   

$$
\boxed{
   D_{k-1}E_k\mid G_k,
   \qquad
   D_{k-1}=\prod_{r=0}^{k-2}(r!)^2.
   }
   \tag{1.1}
$$


   This is a product divisibility statement, not merely divisibility by the least common multiple of two known factors.
4. Every prime-power exponent in $E_k$ is evaluated:
   

$$
\boxed{
   v_p(E_k)=
   \sum_{\substack{a\ge1\\4k-3<p^a\le6k-5}}
   \frac{p^a-4k+3}{2}
   \quad(p\ \text{odd}),\qquad v_2(E_k)=0.
   }
   \tag{1.2}
$$



This is new information about the **actual two scalar coefficients**, obtained without choosing a nonsaturated contact frame or omitting any rational arctangent correction.

A second proved result is the explicit all-prime height ceiling


$$
\boxed{
G_k\le U_k
:=
\Lambda_k^k\,4^k k!\,28^{k-1}h_{k-1}
\prod_{r=0}^{k-1}(2k+4r)!,
\qquad k\ge32,
}
\tag{1.3}
$$


where


$$
h_m=\det\left(\frac1{2i+2j+1}\right)_{0\le i,j<m}.
$$


It improves the previously available coefficient-height ceiling of leading order $6k^2\log k$ to


$$
\log U_k=4k^2\log k+O(k^2).
$$


It remains too weak for the requested obstruction.

The exact unresolved issue is now isolated further: the moment recurrences give explicit **forced divisibility**, including (1.2), but do not yet control **additional simultaneous divisibility of the two affine coefficients**, especially at primes exceeding all moment denominators.

No finite computation is claimed to have been performed.

---

## 2. Exact objects and established inputs

Throughout,


$$
k\ge2,\qquad 0\le m<2k,\qquad 0\le j<k.
$$


The largest moment index is exactly


$$
m+j\le3k-2.
$$



The integer and rational recurrences are


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


and


$$
r_n=-(2n)!+4\rho_n.
$$


In particular,


$$
\boxed{
r_{n+1}+r_n
=-(2n+2)!-(2n)!+\frac4{2n+1}.
}
\tag{2.1}
$$


The factorial endpoint term and the complete rational arctangent term are both retained.

Set


$$
\Phi=(c_{m+j})_{\substack{0\le j<k\\0\le m<2k}},
\qquad
\mathcal R_{mj}=r_{m+j},
$$




$$
w_m=(-1)^m,\qquad v_j=(-1)^j.
$$


The original integer polynomial is


$$
\boxed{
H_k(s)=
\det[\Phi^T\mid \Lambda_k\mathcal R+s\Lambda_kwv^T]
=H_{0,k}+H_{1,k}s.
}
\tag{2.2}
$$



The period matrix has rank at most one, so this determinant is affine. All arithmetic statements below concern precisely the coefficients in (2.2).

### 2.1 Reused content and saturation results

The supplied proofs establish:

- $C_k=(c_{i+j})_{i,j<k}$ is nonsingular for $k\ge2$.
- The contact kernel is saturated.
- Its successive leading-coefficient payments telescope:
  

$$
\prod_{m=k}^{2k-1}e_{k,m}
  =\frac{|\det C_k|}{\delta_{k,2k-1}}.
$$


- For a saturated integer contact basis $X$,
  

$$
H_k(s)=\pm\delta_{k,2k-1}\Lambda_k^k
  \det\mathcal M_X(s).
$$


- Every size-$k$ contact minor is divisible by $D_{k-1}$.

The last statement is the established integer Laguerre-frame theorem with the negative atom retained. It will be reused, not rederived.

### 2.2 Reused whole-error nonvanishing and lower bound

Write $s_0=e+\pi$. The Turn 13 theorem gives, for every $k\ge32$,


$$
(-1)^kH_k(s_0)>0,\qquad (-1)^kH_{1,k}>0,
\tag{2.3}
$$


and


$$
\boxed{
|H_k(s_0)|
\ge
\Lambda_k^kJ_k^\nu\gamma_k^k\mathfrak h_k,
}
\tag{2.4}
$$


where


$$
\gamma_k=
\frac4k\left(\frac{k^2-1}{144}\right)^k-1-2^k,
$$




$$
\mathfrak h_k=
\det\left(\frac1{i+j+1}\right)_{i,j<k}>0,
$$


and $J_k^\nu$ is the positive compact Hankel determinant.

The proof supplied for this theorem uses the complete signed functional


$$
L=\mu-\delta_{-1}
$$


and moments only through $3k-2$. It does not depend on the unevaluated finite inequalities in Family090.

In particular,


$$
\log|H_k(s_0)|\ge2k^2\log k-O(k^2).
\tag{2.5}
$$


We retain the exact positive factors in (2.4); (2.5) is only its asymptotic consequence.

---

## 3. New theorem: the exact clearer of each complete rational moment column

The raw array has one least simultaneous clearer, $\Lambda_k$, but its individual columns have different least clearers. Their distinction produces a compulsory scalar factor.

### Theorem 3.1 — Exact raw-column clearers

For every $k\ge2$ and $0\le j<k$, the least positive integer clearing


$$
r_j,r_{j+1},\ldots,r_{2k-1+j}
$$


is


$$
\boxed{
\Lambda_{k,j}
=\operatorname{lcm}(1,3,\ldots,4k+2j-3).
}
\tag{3.1}
$$



#### Proof: sufficiency

For every entry in this column,


$$
n\le2k-1+j.
$$


All denominators occurring in $\rho_n$ are positive odd integers at most


$$
2n-1\le4k+2j-3.
$$


The factorial summand in $r_n$ is an integer. Therefore $\Lambda_{k,j}$ clears the entire column.

#### Proof: necessity

Suppose a positive integer $C$ clears every entry of the column.

For


$$
j\le n\le2k-2+j,
$$


both $Cr_n$ and $Cr_{n+1}$ are integers. Equation (2.1) then gives


$$
C\frac4{2n+1}\in\mathbb Z.
$$


Since $2n+1$ is odd,


$$
2n+1\mid C.
$$


Thus $C$ is divisible by every odd integer in


$$
[\,2j+1,\;4k+2j-3\,].
\tag{3.2}
$$



It remains to check that the lcm of the odd integers in this interval is already the lcm of all positive odd integers up to its upper endpoint.

Let $q=p^a$ be any odd prime power satisfying


$$
q\le4k+2j-3.
$$



If $q\ge2j+1$, it appears directly in (3.2). Otherwise $q\le2j-1$. Choose the least odd multiple of $q$ not below $2j+1$. Consecutive odd multiples differ by $2q$, so the chosen multiple is less than


$$
2j+1+2q\le6j-1.
$$


Because $j\le k-1$,


$$
6j-1\le4k+2j-3.
$$


It therefore belongs to (3.2), and again $q\mid C$.

Every prime power required by $\Lambda_{k,j}$ divides $C$, proving minimality. ∎

### Boundary audit

The recurrence is used only between entries already present in the column:


$$
n=j,\ldots,2k-2+j.
$$


No successor moment beyond $r_{3k-2}$ is introduced.

The last column has


$$
\Lambda_{k,k-1}
=\operatorname{lcm}(1,3,\ldots,6k-5)
=\Lambda_k.
$$


Thus the least simultaneous clearer of the **whole raw array** remains exactly $\Lambda_k$. Theorem 3.1 does not replace it by a smaller number.

---

## 4. New evaluated factor in the final all-prime scalar gcd

Define the integer affine polynomial


$$
\widehat H_k(s)=
\det\left[
\Phi^T\ \middle|\
\left(\Lambda_{k,j}
[r_{m+j}+s(-1)^{m+j}]\right)_
{\substack{m<2k\\j<k}}
\right].
\tag{4.1}
$$


Theorem 3.1 proves the integrality of every scalar coefficient in every right column.

Since $\Lambda_{k,j}\mid\Lambda_k$, columnwise extraction gives the exact identity


$$
\boxed{
H_k(s)=E_k\widehat H_k(s),
\qquad
E_k=\prod_{j=0}^{k-1}\frac{\Lambda_k}{\Lambda_{k,j}}\in\mathbb Z_{>0}.
}
\tag{4.2}
$$



This is an arithmetic identity in the original finite matrix, not an analytic normalization.

### Theorem 4.1 — Product divisor of the actual coefficient content

For every $k\ge32$,


$$
\boxed{D_{k-1}E_k\mid G_k.}
\tag{4.3}
$$



More generally, $D_{k-1}E_k$ divides both coefficients of $H_k(s)$ for every $k\ge2$.

#### Proof

Expand $\widehat H_k(s)$ along its $k$ contact columns.

Every term is a size-$k$ contact minor multiplied by an integer polynomial minor from the right block. The established Laguerre-frame theorem says that each contact minor is divisible by $D_{k-1}$. Hence


$$
D_{k-1}\mid\widehat H_{0,k},\qquad
D_{k-1}\mid\widehat H_{1,k}.
$$


Multiplication by the exact integer $E_k$ in (4.2) proves the claim. ∎

This proof is important when $D_{k-1}$ and $E_k$ share primes: it establishes their **product** as a divisor. It is not obtained by combining two independent divisibilities through an unjustified multiplication.

### 4.1 Exact all-prime valuation formula

For an odd prime $p$,


$$
v_p(\Lambda_{k,j})
=\#\{a\ge1:p^a\le4k+2j-3\}.
$$


Therefore


$$
\begin{aligned}
v_p(E_k)
&=\sum_{j=0}^{k-1}
\left(v_p(\Lambda_k)-v_p(\Lambda_{k,j})\right)\\
&=\sum_{\substack{a\ge1\\p^a\le6k-5}}
\#\{0\le j<k:4k+2j-3<p^a\}.
\end{aligned}
$$


A power $p^a\le4k-3$ contributes zero. For


$$
4k-3<p^a\le6k-5,
$$


the number of admissible $j$ is exactly


$$
\frac{p^a-4k+3}{2}.
$$


This proves (1.2).

Consequently, the new divisor is completely specified by a finite interval of prime powers. It is not a named, unevaluated residual gcd.

### 4.2 Size of the new factor

The elementary lcm estimate reused in the sources gives


$$
\log\Lambda_k=O(k).
$$


Thus


$$
0\le\log E_k\le k\log\Lambda_k=O(k^2).
\tag{4.4}
$$



Accordingly,


$$
\log(D_{k-1}E_k)=k^2\log k+O(k^2).
\tag{4.5}
$$



The new factor therefore makes a genuine exponential-scale improvement, but does not change the leading $k^2\log k$ coefficient supplied by the contact-minor divisor.

### 4.3 The actual primitive pair is unchanged

Let


$$
\widehat G_k=\gcd(|\widehat H_{0,k}|,|\widehat H_{1,k}|).
$$


Identity (4.2) gives the exact all-prime equality


$$
G_k=E_k\widehat G_k.
$$


Hence


$$
\frac{|H_{1,k}|}{G_k}
=\frac{|\widehat H_{1,k}|}{\widehat G_k},
\qquad
\frac{|H_k(s_0)|}{G_k}
=\frac{|\widehat H_k(s_0)|}{\widehat G_k}.
$$


No new approximant has been substituted for the original one.

---

## 5. A new explicit upper bound for the actual content

An evaluated upper bound is also available, although its leading scale is still insufficient.

The Turn 13 slope identity is


$$
\frac{(-1)^kH_{1,k}}{\Lambda_k^k}
=
\frac1{(k-1)!}
\int
V(y)^2\prod_{j=1}^{k-1}(1+y_j)^2
\det\widetilde M_y\,d\nu^{k-1}(y),
\tag{5.1}
$$


where


$$
\widetilde Q_y(x)
=(x+1)\prod_{j=1}^{k-1}(x-y_j),
$$


and


$$
(\widetilde M_y)_{ab}
=\int x^{a+b}\widetilde Q_y(x)\,d\mu(x),
\qquad 0\le a,b<k.
$$



This identity retains the complete original determinant. The disappearance of the negative atom in this derivative identity is justified by the cross-Vandermonde zero when both variables are at $-1$; it is not an omission of the atom.

### 5.1 Entry bound

For $0\le x\le1$,


$$
|\widetilde Q_y(x)|\le2.
$$


For $x\ge1$,


$$
|\widetilde Q_y(x)|
\le(x+1)x^{k-1}\le2x^k.
$$


Put $N=k+a+b$. Since $\mu$ has mass one and moments $a_{2N}$,


$$
|(\widetilde M_y)_{ab}|
\le2+2a_{2N}
\le4(2N)!.
\tag{5.2}
$$


Here $N\ge k\ge2$, and the established bound $a_{2N}\le(2N)!$ applies.

The maximum degree is


$$
k+(k-1)+(k-1)=3k-2,
$$


exactly the original boundary.

### 5.2 Determinant bound

Factorial log-convexity, as already used in A5 Turn 12, implies that the largest permutation product is obtained by pairing increasing row and column indices. Thus


$$
|\det\widetilde M_y|
\le
4^k k!\prod_{r=0}^{k-1}(2k+4r)!.
\tag{5.3}
$$



Taking absolute values in (5.1) gives


$$
|H_{1,k}|
\le
\Lambda_k^k4^k k!
\left(\prod_{r=0}^{k-1}(2k+4r)!\right)
J_{k-1}^{(1+x)^2\nu}.
\tag{5.4}
$$



Under $x=t^2$,


$$
(1+t^2)^2\left(e^t+\frac4{1+t^2}\right)\le28
\qquad(0\le t\le1).
$$


Positive-semidefinite comparison of moment matrices therefore yields


$$
J_{k-1}^{(1+x)^2\nu}\le28^{k-1}h_{k-1}.
$$


This proves


$$
|H_{1,k}|\le U_k
$$


with $U_k$ as in (1.3).

For $k\ge32$, the reused nonvanishing theorem gives $H_{1,k}\ne0$, so


$$
G_k\le|H_{1,k}|\le U_k.
$$



### 5.3 What this upper bound actually achieves

The factorial product satisfies


$$
\begin{aligned}
\log\prod_{r=0}^{k-1}(2k+4r)!
&=\left(\sum_{r=0}^{k-1}(2k+4r)\right)\log k+O(k^2)\\
&=4k^2\log k+O(k^2).
\end{aligned}
$$


The remaining factors in $U_k$ contribute $O(k^2)$. Hence


$$
\boxed{\log G_k\le4k^2\log k+O(k^2).}
\tag{5.5}
$$



This is an upper bound on the **actual final gcd**, not on $\det C_k$. Nevertheless, it is a coefficient-height ceiling, not a sufficiently sharp content theorem.

---

## 6. Consequences for the whole primitive error

For $k\ge32$, define the actual primitive pair by


$$
q_k=\frac{|H_{1,k}|}{G_k},
\qquad
p_k=-\frac{\operatorname{sgn}(H_{1,k})H_{0,k}}{G_k}.
$$


Then


$$
\gcd(p_k,q_k)=1,
$$


and the Turn 13 signs give


$$
\boxed{
q_k(e+\pi)-p_k
=\frac{|H_k(e+\pi)|}{G_k}>0.
}
\tag{6.1}
$$



The established whole-error upper bound remains


$$
F_k^\perp
=
\Lambda_k^k21^kk!h_k
\prod_{r=0}^{k-1}(2k+4r)!.
$$


The new divisor gives the valid improvement


$$
\boxed{
0<q_k(e+\pi)-p_k
\le\frac{F_k^\perp}{D_{k-1}E_k}.
}
\tag{6.2}
$$


Its logarithmic upper-bound scale is still


$$
3k^2\log k+O(k^2).
$$


It does not prove decay.

On the other hand, the new upper bound for $G_k$, combined with (2.4), gives


$$
q_k(e+\pi)-p_k
\ge
\frac{\Lambda_k^kJ_k^\nu\gamma_k^k\mathfrak h_k}{U_k}.
\tag{6.3}
$$


At the currently proved leading scales, this only gives


$$
\log\bigl(q_k(e+\pi)-p_k\bigr)
\ge-2k^2\log k-O(k^2).
$$


It does not prove divergence.

Thus neither direction of the requested primitive-error conclusion follows from the new bounds.

---

## 7. The precise obstruction to an upper content bound from the recurrences

The recurrences supply:

- exact denominator depths;
- exact compulsory column factors;
- factorial-frame divisibility of contact minors;
- finite congruence descriptions of the moments.

These are principally mechanisms for proving **lower bounds on valuations**. An upper bound for $G_k$ requires proving that the two complete coefficients do not acquire substantial additional simultaneous divisibility.

The obstruction can be stated precisely at primes outside the entire denominator range.

Let


$$
A_k=[\Phi^T\mid\Lambda_k\mathcal R],
$$




$$
u_k=\Lambda_kw,\qquad
z_k=(0,\ldots,0,v_0,\ldots,v_{k-1})^T.
$$


Then


$$
H_k(s)=\det(A_k+s u_kz_k^T),
$$


and


$$
H_{1,k}=z_k^T\operatorname{adj}(A_k)u_k.
\tag{7.1}
$$



Let $p>6k-5$ be prime. None of the raw rational denominators has a $p$-pole, and $p$ divides neither $D_{k-1}$ nor $E_k$. Nevertheless,


$$
p\mid G_k
$$


is equivalent to the simultaneous congruences


$$
\det A_k\equiv0\pmod p,
\qquad
z_k^T\operatorname{adj}(A_k)u_k\equiv0\pmod p.
\tag{7.2}
$$



There are two distinct ways this can occur.

1. If
   

$$
\operatorname{rank}_{\mathbb F_p}A_k\le2k-2,
$$


   every entry of $\operatorname{adj}(A_k)$ vanishes modulo $p$, so both congruences hold automatically.

2. If $\operatorname{rank}A_k=2k-1$, choose nonzero right and left nullvectors $x,y$. Then
   

$$
\operatorname{adj}(A_k)=\kappa xy^T
$$


   for some nonzero $\kappa\in\mathbb F_p$, and the second congruence becomes
   

$$
(z_k^Tx)(y^Tu_k)=0.
   \tag{7.3}
$$



Thus the missing theorem is a uniform **rank-and-transversality statement for the actual mixed pencil**, together with prime-power control. Contact-matrix nonsingularity over $\mathbb Q$, scalar recurrence invertibility, and denominator enumeration do not establish it.

This is also why a unique-corner residue calculation or a finite Smith table cannot settle the final content problem. Those results do not control (7.2) at every other prime, or its higher-power analogues.

---

## 8. A concrete, falsifiable follow-on arithmetic lemma

The following is a working conjecture, not a proved statement.

Define the completely explicit integer


$$
\boxed{
B_k=D_{k-1}E_k\,2^{2k^2}\Lambda_k^{2k}.
}
\tag{8.1}
$$



### Proposed content-envelope lemma

For every $k\ge32$,


$$
\boxed{G_k\mid B_k.}
\tag{8.2}
$$



Equivalently, the following three concrete assertions would suffice:

1. **Large-prime exclusion**
   

$$
p>6k-5\implies p\nmid G_k.
$$



2. **Odd-prime depth bound**
   

$$
v_p(G_k)
   \le
   v_p(D_{k-1})+v_p(E_k)
   +2k\,v_p(\Lambda_k)
   \qquad(p\ \text{odd}).
$$



3. **Binary depth bound**
   

$$
v_2(G_k)\le v_2(D_{k-1})+2k^2.
$$



The constants in this proposed envelope are not consequences of the supplied recurrences. They are explicit parameters of a deliberately falsifiable conjecture. No computed evidence for the conjecture is asserted here.

Its structural motivation is specific: after the proved factorial-frame factor and the now evaluated column-clearer factor are removed, it asks whether the remaining content is supported only on the finite denominator primes, with controlled depth, apart from a separately allowed binary contribution. The exact obstruction in §7 identifies what would have to be proved to justify that expectation.

### Conditional consequence

If (8.2) holds, then


$$
\log G_k
\le
\log D_{k-1}+\log E_k+2k^2\log2+2k\log\Lambda_k
=
k^2\log k+O(k^2).
$$


Combining this with the retained whole-error lower bound gives


$$
\boxed{
\log\bigl(q_k(e+\pi)-p_k\bigr)
\ge k^2\log k-O(k^2)\longrightarrow+\infty.
}
\tag{8.3}
$$



Therefore this conjecture would prove a genuine obstruction to primitive decay for this compact family.

It would **not** prove that $e+\pi$ is rational, nor rule out a different irrationality construction.

For the original-index restriction, it would be enough to establish the same envelope on an infinite set


$$
k=9^{18+32u}.
$$


The all-$k$ conjecture above is stronger and provides a practical finite falsification target.

---

## 9. One bounded exact-arithmetic calculation

No calculation is required for the proofs in §§3–6. One new finite calculation can discriminate the conjecture in §8 without repeating the closed $k=2,\ldots,10$ Smith work.

### Input: $k=32$

Generate:

- $a_0,\ldots,a_{188}$ from
  

$$
a_0=1,\qquad a_d=1-da_{d-1};
$$


- $c_0,\ldots,c_{94}$;
- $\rho_0,\ldots,\rho_{94}$ and $r_0,\ldots,r_{94}$;
- $\Lambda_{32}=\operatorname{lcm}(1,3,\ldots,187)$;
- the two $64\times64$ integer matrices defining $H_{32}(0)$ and $H_{32}(1)$.

Set


$$
H_{0,32}=H_{32}(0),\qquad
H_{1,32}=H_{32}(1)-H_{32}(0).
$$



The new factor has the explicit prime-power description


$$
\begin{aligned}
E_{32}={}&
127^1\,131^3\,137^6\,139^7\,149^{12}\,151^{13}\\
&\cdot157^{16}\,163^{19}\,167^{21}\,
13^{22}\,173^{24}\,179^{27}\,181^{28}.
\end{aligned}
\tag{9.1}
$$


The $13^{22}$ factor comes from the prime power $13^2=169$, not from a prime in that interval.

Also,


$$
D_{31}=\prod_{r=0}^{30}(r!)^2,
$$


and the conjectural envelope is


$$
B_{32}=D_{31}E_{32}\,2^{2048}\Lambda_{32}^{64}.
$$



### Expected verifiable outputs

1. The exact integers $H_{0,32}$ and $H_{1,32}$.
2. Their exact gcd
   

$$
G_{32}=\gcd(|H_{0,32}|,|H_{1,32}|),
$$


   with an extended-Euclidean certificate
   

$$
U H_{0,32}+V H_{1,32}=G_{32}.
$$


3. Verification of the proved divisibility
   

$$
D_{31}E_{32}\mid G_{32}.
$$


4. The actual primitive pair
   

$$
q_{32}=\frac{|H_{1,32}|}{G_{32}},\qquad
   p_{32}=-\frac{H_{0,32}}{G_{32}},
$$


   using $H_{1,32}>0$, as supplied by the $k\ge32$ theorem.
5. The exact integer
   

$$
W_{32}=\frac{G_{32}}{\gcd(G_{32},B_{32})}.
$$



The conjectured output is $W_{32}=1$. Any output $W_{32}>1$ falsifies the all-$k$ content-envelope conjecture immediately.

No unrestricted factorization is needed. If desired, trial division by the finitely many primes at most $187$ distinguishes an excessive small-prime valuation from a residual factor coprime to every prime in the permitted support.

This is one bounded determinant-and-gcd calculation, not a Smith search. A successful test would establish only the case $k=32$. Since $32$ is not one of the original binary indices, it would not establish even one original-index instance of the conjecture.

---

## 10. Arithmetic ledger: what has not been replaced

The new column factor does not identify any of the following quantities with one another.

For a saturated integer contact basis $X$, write


$$
B_{rj}=\sum_mX_{rm}r_{m+j},
\qquad u_r=\sum_mX_{rm}(-1)^m.
$$


Its actual entry clearer remains


$$
L_X=
\frac{\Lambda_k}
{\gcd\!\left(\Lambda_k,\{\Lambda_kB_{rj}\}_{r,j}\right)}.
$$


After this clearing, an actual row content is


$$
\gcd\left(L_Xu_r,\{L_XB_{rj}\}_{j}\right).
$$


No value for these row contents is inferred from $E_k$.

If


$$
L_X^k\det\mathcal M_X(s)=A_0+A_1s,
$$


the least simultaneous clearer of the two rational determinant coefficients remains


$$
\frac{L_X^k}{\gcd(L_X^k,A_0,A_1)},
$$


and the remaining content after that clearing is


$$
\frac{\gcd(A_0,A_1)}
{\gcd(L_X^k,A_0,A_1)}.
$$



For individually cleared monic contact rows, the primitive polynomial contents remain $1$, while their nonsaturation index remains


$$
J_k=
\frac{\prod_{m=k}^{2k-1}d_m}
{|\det C_k|/\delta_{k,2k-1}}.
$$


That frame-index factor is separate from $E_k$.

The direct block route used here avoids choosing such a frame. Its final normalization is still exactly


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|),
$$


and its actual denominator and whole error remain those in (6.1).

---

## 11. Original binary domain, forcing, returns, and terminal condition

Nothing in the new compact arithmetic identifies this family with the original binary reconstruction.

That original domain remains


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
$$


The contact indices are


$$
0,\ldots,b-1,
$$


while physical reconstruction includes


$$
0,\ldots,b,\qquad z_b=0.
$$



The complete corrected columns remain


$$
x=\frac12RA^{-1}f,
\qquad
y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},
\qquad x=2^ax_0.
$$


Neither $h^F$, $e_0$, nor the factor $4b!$ is removed.

The complete return scalar remains


$$
S=\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f.
$$


After the paid division, the retained valuation statement is only


$$
v_2\!\left(\frac{S}{2^{a+1}}\right)\ge\chi-a,
\qquad
\chi=v_2\binom{n+b-1}{b-1}.
$$


The subtraction of $a$ remains indispensable.

The norm


$$
Q=x_0^Tx_0,
$$


the actual corrected-column contents, least simultaneous clearer, and final all-prime scalar gcd are not evaluated by the compact calculation. No compact quantity is substituted for them.

Likewise, the established original valuation


$$
v_3(q)=n-\frac{b+15}{2}
$$


is unchanged and is not transferred to the compact family.

All proved compact statements above hold at


$$
k=b(u),
$$


because they hold for every $k\ge32$. This preserves the same infinite original parameter set for compact nonvanishing and any future compact content bound, but does not equate the two primitive pairs.

---

## 12. Final assessment

### Newly proved

- The exact least clearer of each complete raw rational moment column:
  

$$
\Lambda_{k,j}=\operatorname{lcm}(1,3,\ldots,4k+2j-3).
$$


- The evaluated all-prime factor
  

$$
E_k=\Lambda_k^k/\prod_j\Lambda_{k,j},
$$


  including its complete prime-power valuation formula.
- The product divisibility
  

$$
D_{k-1}E_k\mid G_k.
$$


- The explicit upper bound
  

$$
G_k\le U_k,\qquad
  \log U_k=4k^2\log k+O(k^2).
$$



### Conditional deduction

The explicit proposed envelope


$$
G_k\mid D_{k-1}E_k\,2^{2k^2}\Lambda_k^{2k}
$$


would imply divergence of the actual primitive whole error, including on the same infinite original indices.

### Auxiliary finite check

The single proposed $k=32$ determinant-and-gcd calculation can falsify that all-$k$ envelope. It cannot prove an infinite content theorem.

### Exact remaining bottleneck

The outstanding obligation is still an upper bound on **additional simultaneous coefficient divisibility** beyond the forced factors, or a substantially larger proved divisor paired with a sufficient whole-error upper bound.

At large primes, this becomes the concrete singular-pencil problem (7.2)–(7.3). No supplied moment recurrence, contact-minor divisor, finite Smith receipt, or corner-pole theorem currently excludes that phenomenon uniformly or bounds its prime-power depth.

Accordingly, this turn supplies a new evaluated arithmetic factor and a sharper actual-content ceiling, but **does not yet prove either primitive decay or primitive divergence for the compact family, and proves no rationality or irrationality theorem for $e+\pi$**.
