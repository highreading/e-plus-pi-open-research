> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Dyadic source units, fully paid physical flags, and cancellation in the full-rank mixed coefficient expansion

## 1. Results and proof status

The rationality or irrationality of $e+\pi$ remains unresolved.

In particular, this report does **not** establish the primary terminal estimate


$$
\boxed{\nu_k^{[5]}\le \frac{15}{4}k^2-64+O(k\log k).}
\tag{1.1}
$$



It does, however, resolve a substantial part of the repaired source problem and identify a structural cancellation in the full-rank mixed expansion.

The new proved results are:

1. **An exact dyadic determinant law for the joint kernel.**  
   The $d$-dependent numerator can be handled at every dyadic size, not only before its first nonconstant term. If
   

$$
N=2^{a+1},\qquad x=d\bmod 2^a,
$$


   then the leading $N\times N$ additionally normalized contact matrix is a unit precisely when
   

$$
\boxed{
   \begin{cases}
   a\ \text{is even},&x=0,\\
   x\equiv1\pmod3,&x>0.
   \end{cases}}
   \tag{1.2}
$$


   This is an evaluated law in the actual binary digits of $d$.

2. **Optimal atom-containing physical source flags.**  
   Whenever the explicitly tested dyadic block in (1.2) is a unit and $N+1\le d$, there is a nested flag of actual return columns, beginning with the already paid order
   

$$
1,0,5,4,
$$


   whose atom-containing physical source minors attain
   

$$
B_q(d)=\binom q2+\sum_{j=0}^{q-2}v_2((d+1)_j)
$$


   for **every** $1\le q\le N+1$. The excess above $B_q(d)$ is exactly zero throughout that flag.

   The proof uses a finite parity operation only to prove rank. It does not transfer the parent’s parity column operation to the integer pencil.

3. **A growing complete corrected flag within the already proved mixed-compound window.**  
   The preceding source flag supplies the formerly open source-unit hypothesis in the turn13 comparison theorem. It therefore gives complete corrected cofactor contents
   

$$
\Theta_q(d)=c_q+2E_q+B_q(d)
$$


   through
   

$$
q\le \min\{N+1,\lfloor d/8\rfloor\},
$$


   together with fully paid Cramer interpolation of every remaining column and both borders.

4. **A multi-column mixed Cauchy residue theorem.**  
   A mixed determinant with $p$ rational Cauchy columns and $h$ normalized contact columns has a fully evaluated first possible residue. Its contact factor is the same joint kernel, now with parameter $p$. At even $p$ and dyadic $h$, its determinant is evaluated by the same dyadic law.

5. **A structural cancellation at full rank near the valuation-minimizing mixed range.**  
   After an exact, finite, fully paid transformation of the linear coefficient, let $\mathcal L_p(d)$ be the first possible payment of the sector using $p$ product columns and $d+2-p$ bottom corrections. For every
   

$$
3\le p\le\lfloor d/3\rfloor,
$$


   the complete $p$-sector is divisible by $2^{\mathcal L_p(d)+1}$, not merely $2^{\mathcal L_p(d)}$.

   The normalized parity sum at the nominal minimum is **zero**. It vanishes because the top and bottom contact rows are related by a finite shift polynomial. This cancellation occurs in the range
   

$$
p=\frac d4+O(\log d),
$$


   where the nominal payments are minimized:
   

$$
\min_p\mathcal L_p(d)=\frac{11}{4}d^2+O(d\log d).
$$



Thus lower-valuation optimization alone fails even in the promising mixed range. The remaining problem is to bound and evaluate the **excess after this structural cancellation**, while retaining the complete constant coefficient and all other mixed sectors.

No new numerical computation is used below.

---

## 2. Original objects and exact normalization retained

### 2.1 Domain, sequences, forcing, and terminal

Throughout,


$$
\boxed{k=9^{18+32u},\quad u\ge0,\qquad d=k-1.}
\tag{2.1}
$$


In particular,


$$
v_2(d)=4,\qquad d\equiv2\pmod3,\qquad d\equiv208\pmod{256}.
$$



The sequences remain


$$
a_0=1,\qquad a_n=1-na_{n-1},
$$




$$
u_n=a_{2n},\qquad f_n=(2n)!,\qquad
w_n=(-1)^n,\qquad c_n=u_n-w_n,
$$


and


$$
\rho_0=0,\qquad \rho_{n+1}+\rho_n=\frac1{2n+1},
\qquad r_n=-f_n+4\rho_n.
$$


The complete returns are


$$
\sigma_n=u_{n+1}+u_n=c_{n+1}+c_n
$$


and


$$
\boxed{\tau_n=-(2n+2)!-(2n)!+\frac4{2n+1}.}
\tag{2.2}
$$



Set


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5),\qquad T_n=\Lambda_k\tau_n.
$$


Thus neither factorial term is removed:


$$
T_n=-\Lambda_k\bigl((2n+2)!+(2n)!\bigr)
+\frac{4\Lambda_k}{2n+1}.
$$



The original affine determinant is


$$
H_k(s)=
\det\left[
(c_{m+j})\
\middle|\
\bigl(\Lambda_k(r_{m+j}+s(-1)^{m+j})\bigr)
\right]
=H_{0,k}+H_{1,k}s,
$$


where $0\le m<2k$, $0\le j<k$.

The physical last row and terminal remain


$$
\boxed{
m=2k-1=2d+1,\qquad
\text{moment }3k-2,\qquad
(6k-4)!,\qquad 6k-5.
}
\tag{2.3}
$$



### 2.2 Actual contents, least clearers, and primitive pair

The least original right-column entry clearers remain


$$
\Lambda_{k,j}
=\operatorname{lcm}(1,3,\ldots,4k+2j-3),
\qquad 0\le j<k.
$$


Their common least entry clearer is $\Lambda_k$.

Retain the actual all-prime gcds


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|),\qquad
d_{H,k}=\gcd(\Lambda_k^k,H_{0,k},H_{1,k}).
$$


The least simultaneous coefficient clearer of $H_k/\Lambda_k^k$, and its subsequent content, are exactly


$$
\boxed{\frac{\Lambda_k^k}{d_{H,k}},\qquad \frac{G_k}{d_{H,k}}.}
\tag{2.4}
$$



The original rectangles are


$$
Z_k=
\left[
(c_{m+j})_{\substack{m<2k\\j<k}}
\ \middle|\
(T_{m+j})_{\substack{m<2k\\j<k-1}}
\right],
$$




$$
Y_k=
\left[
(\sigma_{m+j})_{\substack{m<2k-1\\j<k}}
\ \middle|\
(T_{m+j})_{\substack{m<2k-1\\j<k}}
\right].
$$


Their actual maximal-minor contents satisfy the established interface


$$
\operatorname{lcm}(\mathscr L_k,\mathscr R_k)
\mid G_k\mid \Lambda_k\mathscr L_k\mathscr R_k,
$$


where


$$
\mathscr R_k=\delta_{2k-1}(Z_k),\qquad
\mathscr L_k=\delta_{2k-1}(Y_k).
$$



The accepted sign and nonvanishing results give


$$
q_k=\frac{|H_{1,k}|}{G_k}>0,\qquad
p_k=-\frac{(-1)^kH_{0,k}}{G_k},
$$


and


$$
\boxed{
0<\ell_k=q_k(e+\pi)-p_k
=\frac{|H_k(e+\pi)|}{G_k}.
}
\tag{2.5}
$$


These are not replaced by a lower gcd divisor or a selected error summand.

### 2.3 The complete corrected pencil

Let


$$
P_d(x)=\prod_{h=0}^{d-1}(2x+2h+1),\qquad
\mathcal A_dy=\Delta^d(P_dy).
$$


The operator is applied only to the first $d$ original rows, with determinant payment


$$
\Omega_k=\prod_{n=0}^{d-1}P_d(n).
$$



Writing $\mathfrak b(t)=4t^2+6t+3$, the complete top forcing is


$$
F_k(n,j)=
-\Lambda_k\sum_{i=0}^d(-1)^i\binom di
P_d(n+i)\mathfrak b(n+i+j)(2(n+i+j))!,
\quad n,j<d.
$$


Since


$$
\mathfrak b(t)(2t)!=(2t+2)!+(2t)!,
$$


both factorial terms are present.

With $D_f=\operatorname{diag}((2n)!)_{n<d}$, write


$$
F_k=-\Lambda_kD_fK_dD_f,\qquad \eta_d^F=\det K_d.
$$


The established Pascal congruence makes every leading principal determinant of $K_d$ odd.

Retain


$$
h_d=(2d-2)!,\quad
\beta_d=v_2(h_d),\quad
\alpha_d=v_2((2d)!)=\beta_d+5,
$$




$$
N_d=(h_dD_f^{-1})\operatorname{adj}(K_d)(h_dD_f^{-1}),
$$




$$
\delta_k=\Lambda_k\eta_d^Fh_d^2,\qquad
F_k^{-1}=-N_d/\delta_k,
$$


and


$$
f_k=(-\Lambda_k)^d\eta_d^F
\left(\prod_{n<d}(2n)!\right)^2.
$$



Residual row $i$, $0\le i<d+2$, is physical row $d+i$. The complete bottom forcing is


$$
R(i,j)=
\frac{\Lambda_k}{2(d+i+j)+1}
-\frac{\Lambda_k}{4}\mathfrak b(d+i+j)(2(d+i+j))!,
\quad j<d.
\tag{2.6}
$$



Every full Newton divisor is retained:


$$
D_r=2^rr!,\qquad
\mathfrak D_d=\prod_{r<d}D_r.
$$


The top sources are


$$
\mathsf a_n=\frac{(\mathcal A_dc)_n}{2^d},
\qquad
t_n^{(r)}
=\frac{(\mathcal A_d\Delta^r\sigma)_n}
       {2^{\alpha_d+1}D_r}.
$$


The complete columns are


$$
x=RN_d\mathsf a+\frac{\delta_k}{2^{d+2}}c_{\rm bot},
$$




$$
z^{(r)}
=RN_dt^{(r)}
+\frac{\delta_k}{2^{\alpha_d+3}D_r}
(\Delta^r\sigma)_{\rm bot},
$$


and


$$
\mathfrak b_j
=RN_d\Lambda_k(\mathcal A_d\psi_j)_{\rm top}
+\frac{\delta_k\Lambda_k}{4}(\psi_j)_{\rm bot},
\qquad \psi_0=r,\quad\psi_1=w.
$$


Thus


$$
\mathcal Q_k(s)
=[x,z^{(0)},\ldots,z^{(d-1)},\mathfrak b_0+s\mathfrak b_1].
\tag{2.7}
$$



The already evaluated complete pivots are reused:


$$
(t_2,t_3,t_4,t_5)=(5,19,39,72),\qquad
\det\Pi_{q,k}=2^{t_q}\mu_{q,k},
$$


with all $\mu_{q,k}$ odd. Their exact all-prime payments remain


$$
|\mu_{3,k}|^{d-2}g_k^{[2]}
=2^{13}|\mu_{2,k}|^{d-1}g_k^{[3]},
$$




$$
|\mu_{4,k}|^{d-3}g_k^{[3]}
=2^{19}|\mu_{3,k}|^{d-2}g_k^{[4]},
$$




$$
|\mu_{5,k}|^{d-4}g_k^{[4]}
=2^{32}|\mu_{4,k}|^{d-3}g_k^{[5]}.
$$



In particular,


$$
\nu_k=64+\nu_k^{[5]},
$$


and, with $\lambda_d=d\alpha_d+4d+4$,


$$
\boxed{
|\delta_k|^{d+2}\Omega_k|\mu_{5,k}|^{d-4}G_k
=
|f_k|\,2^{\lambda_d+d+69}\mathfrak D_d\,g_k^{[5]}.
}
\tag{2.8}
$$


Consequently,


$$
v_2(G_k)=\chi_k+64+\nu_k^{[5]},
$$


where


$$
\chi_k=d^2+4d+29+(d+4)s_2(d)-3\sum_{n<d}s_2(n).
$$



---

## 3. An evaluated all-order dyadic law for the repaired kernel

### 3.1 The normalized matrix

The full rising-factor identity is established reuse:


$$
\frac{\Delta^jt_n^{(r)}}{2^j(d+1)_j}
=
o_d\sum_{h=0}^d
\binom dh Q_h(n)
\binom{d-h+r+j}{r}
\eta_{d-h+r+j}^{(n+h)}
\in\mathbb Z,
\tag{3.1}
$$


where


$$
Q_h(n)=\prod_{a=h}^{d-1}(2n+2a+1),\qquad
o_d=\operatorname{odd}(d!).
$$



Write


$$
U_d(j,r)=
\frac{\Delta^jt_n^{(r)}}{2^j(d+1)_j}\pmod2.
$$


The physical base row disappears only at this normalized parity precision. Thus


$$
U_d(j,r)
=\sum_{t=0}^d
\binom dt\binom{t+j+r}{r}\eta_{t+j+r}.
\tag{3.2}
$$



Work over


$$
\mathbb F_4=\mathbb F_2[\omega]/(\omega^2+\omega+1).
$$


The contact parity is


$$
\eta_m=\operatorname{Tr}\!\left(
\omega^{m+2}[1+(m+1)\omega]\right).
$$



The joint kernel supplied in the parent note follows from (3.2). Multiplication by


$$
C_d(Y)=(1+Y+Y^2)^d
$$


gives


$$
\boxed{
C_d(Y)\sum_{j,r\ge0}U_d(j,r)X^jY^r
=
\operatorname{Tr}\!\left(
(1+\omega^2Y)^{2d}
\frac{\omega^2+\omega(X+Y)}
     {(1+\omega(X+Y))^2}
\right).
}
\tag{3.3}
$$



For completeness, the scalar in this identity is exact. Before multiplication by $C_d$, the binomial filter contributes


$$
\left(\frac{\omega^2+\omega Y}{1+\omega Y}\right)^d.
$$


Multiplication by $C_d$, including the outer $\omega^2$, contributes


$$
\omega^{2+2d}(1+\omega^2Y)^{2d}.
$$


Since $d\equiv2\pmod3$, $\omega^{2+2d}=1$.

On the first $N$ columns, multiplication by $C_d(Y)$ is a finite unit triangular operation over $\mathbb F_2$. It preserves the leading $N\times N$ determinant. No integer-pencil operation is inferred from it.

### 3.2 A finite dyadic trace-matrix recurrence

For $\beta\in\{\omega,\omega^2\}$, $\gamma=\beta^t$, define


$$
M_{a}(\beta,\gamma,D)
=
\left[
[X^hY^\ell]\,
\operatorname{Tr}\!\left(
\gamma\,\frac{(1+\beta Y)^D}
                 {1+\beta^2(X+Y)}
\right)
\right]_{0\le h,\ell<2^a}.
$$


Let its determinant be $F_a(t,D)$. The value is independent of the choice of $\beta$: conjugating every field element does not change its trace.

Only $D\bmod2^a$ matters, because


$$
(1+\beta Y)^{2^a}\equiv1\pmod{Y^{2^a}}.
$$



We now derive a recurrence by literal finite row and column parity blocks.

If $D=2E$, use


$$
\frac1{1+\beta^2(X+Y)}
=
\frac{1+\beta^2(X+Y)}
     {1+\beta(X^2+Y^2)}.
$$


After ordering rows and columns by parity, the matrix has the form


$$
\begin{pmatrix}C&A\\A&0\end{pmatrix}.
$$


The off-diagonal block has new root $\beta^2$, exponent $E$, and scalar $\gamma\beta^2$. Therefore


$$
\boxed{F_a(t,2E)=F_{a-1}(1-t,E).}
\tag{3.4}
$$


The square of the smaller determinant has been suppressed because it lies in $\mathbb F_2$.

If $D=2E+1$, the numerator calculation is


$$
(1+\beta Y)(1+\beta^2X+\beta^2Y)
=1+\beta^2X+Y+XY+Y^2.
$$


The parity blocks are therefore


$$
\begin{pmatrix}
M_\gamma(I+S)&M_\gamma\\
M_{\gamma\beta^2}&M_\gamma
\end{pmatrix},
$$


where $S$ is the finite column shift and the smaller matrices have root $\beta^2$ and exponent $E$.

Add the lower block row to the upper one. The upper-left block becomes


$$
M_\gamma(I+S)+M_{\gamma\beta^2}
=M_{\gamma\beta,E+1},
$$


because


$$
1+\beta^2+Y=\beta+Y=\beta(1+\beta^2Y).
$$


The result is block triangular. Hence


$$
\boxed{
F_a(t,2E+1)
=
F_{a-1}(2-t,E+1)\,F_{a-1}(-t,E).
}
\tag{3.5}
$$


All exponents $t$ are read modulo $3$.

At size one,


$$
F_0(t,D)=\operatorname{Tr}(\beta^t)
=
\begin{cases}0,&t=0,\\1,&t=1,2.\end{cases}
\tag{3.6}
$$



### 3.3 Closed solution of the recurrence

#### Theorem 3.1 — dyadic trace determinant

Let $x=D\bmod2^a$. Then


$$
\boxed{
F_a(t,D)=1
\iff
\begin{cases}
t\ne0,&x=0,\ a\text{ even},\\
t\ne1,&x=0,\ a\text{ odd},\\
t\equiv2-x\pmod3,&x>0.
\end{cases}}
\tag{3.7}
$$



#### Proof

The assertion at $a=0$ is (3.6).

For $x=0$, recurrence (3.4) applies at every step and sends $t$ to $1-t$. Applying this involution $a$ times gives the first two cases.

Suppose $0<x<2^a$.

If $x=2E$, then $E>0$, and the induction hypothesis in (3.4) gives


$$
1-t\equiv2-E\pmod3.
$$


Equivalently,


$$
t\equiv E-1\equiv2-2E=2-x\pmod3.
$$



If $x=2E+1$ and both $E$ and $E+1$ are nonzero residues modulo $2^{a-1}$, the two conditions from (3.5) are


$$
2-t\equiv2-(E+1),\qquad -t\equiv2-E.
$$


Both are equivalent to


$$
t\equiv E+1\equiv2-(2E+1)\pmod3.
$$



At the lower endpoint $E=0$, the first factor forces $t=1$, and the zero-residue rule for the second factor admits this value. At the upper endpoint $E+1=2^{a-1}$, the nonzero-residue condition on the second factor gives $t\equiv2^{a-1}\pmod3$; the zero-residue rule for the first factor admits exactly that value. This completes the induction. ∎

### 3.4 Application to the actual $d$-dependent numerator

Let $N=2m=2^{a+1}$. In (3.3), write $X^2=Z$, $Y^2=W$. Since


$$
(1+\omega^2Y)^{2d}=(1+\omega W)^d,
$$


the even/odd decomposition of the leading transformed matrix is


$$
\begin{pmatrix}C_m&A_m\\A_m&0\end{pmatrix},
$$


where


$$
A_m(h,\ell)
=[Z^hW^\ell]\,
\operatorname{Tr}\!\left(
\omega\frac{(1+\omega W)^d}
              {1+\omega^2(Z+W)}
\right).
$$


Thus its determinant is $F_a(1,d)$.

#### Corollary 3.2 — exact original-source dyadic unit law

For every permitted leading block,


$$
\boxed{
\det[U_d(j,r)]_{0\le j,r<N}=1
\iff
\begin{cases}
a\text{ even},&d\bmod2^a=0,\\
d\bmod2^a\equiv1\pmod3,&d\bmod2^a>0.
\end{cases}}
\tag{3.8}
$$



This proves the claimed all-order law. In particular, the numerator deformation has been evaluated, not ignored.

---

## 4. Optimal physical source flags at $B_q(d)$

### 4.1 A full integer source payment

Put


$$
R_j(d)=(d+1)_j,\qquad
\mathcal F_q(d)=2^{\binom q2}\prod_{j=0}^{q-2}R_j(d).
\tag{4.1}
$$


Its binary valuation is $B_q(d)$.

The rising-factor identity yields slightly more than the binary payment used previously:

> Every $q$-minor of an atom-containing top-source matrix is divisible by the full integer $\mathcal F_q(d)$.

Indeed, in a jet minor with orders $j_0<\cdots<j_{q-1}$, extract $2^{\sum j_a}$. Scale the atom column by $R_{j_{q-1}}(d)$, and divide row $a$ by $R_{j_a}(d)$. This is integral because


$$
R_{j_a}(d)\mid R_{j_{q-1}}(d).
$$


The resulting determinant identity pays


$$
2^{\sum j_a}\prod_{a=0}^{q-2}R_{j_a}(d).
$$


Since $j_a\ge a$, this is divisible by $\mathcal F_q(d)$. Finite Newton expansion returns the statement to arbitrary physical top-row minors.

This does not evaluate the odd content. It retains the full rising factors instead of identifying their odd parts with $1$.

### 4.2 The atom criterion as a nested row flag

Use the consecutive physical top rows


$$
T_q=\{d-q,\ldots,d-1\}.
$$


Their forward-difference transformation has determinant one.

Let $R_*=R_{q-1}(d)$. The integral normalized jet matrix has atom entries


$$
\frac{R_*}{R_j(d)}\frac{\Delta^j\mathsf a}{2^j}
$$


and return entries


$$
\frac{\Delta^jt^{(r)}}{2^jR_j(d)}.
$$


Exactly,


$$
\det A[T_q,:]=\mathcal F_q(d)\det W_q.
\tag{4.2}
$$



The atom entries reduce to $1$ precisely on the final valuation plateau of $R_j(d)$. Since $d$ is even, that plateau consists of:

- the last row when $q$ is odd;
- the last two rows when $q$ is even.

Consequently, the normalized contact rows relevant to the atom expansion are


$$
U_d(0,\bullet),\ldots,U_d(q-2,\bullet)
$$


for odd $q$, and


$$
U_d(0,\bullet),\ldots,U_d(q-3,\bullet),
\quad
U_d(q-2,\bullet)+U_d(q-1,\bullet)
$$


for even $q$.

Define paired rows


$$
G_{2h}=U_d(2h,\bullet)+U_d(2h+1,\bullet),
\qquad
G_{2h+1}=U_d(2h+1,\bullet).
\tag{4.3}
$$


The first $q-1$ rows of $G$ span exactly the required contact row space. Moreover, these row spaces are nested as $q$ increases.

### 4.3 Growing attainment theorem

#### Theorem 4.1 — optimal physical source flag

Suppose $N=2^{a+1}$, $N+1\le d$, and the digit condition (3.8) holds. Then there is an ordering of distinct actual return columns


$$
r_1,\ldots,r_N\in\{0,\ldots,N-1\},
$$


beginning with


$$
r_1,r_2,r_3,r_4=1,0,5,4,
$$


such that, for every $1\le q\le N+1$,


$$
\boxed{
v_2\det[\mathsf a,t^{(r_1)},\ldots,t^{(r_{q-1})}][T_q,:]
=B_q(d).
}
\tag{4.4}
$$



Every corresponding source content has binary valuation exactly $B_q(d)$.

#### Proof

By (3.8), the first $N$ rows of $U_d$, restricted to columns $0,\ldots,N-1$, are independent. The paired row operation (4.3) is invertible, so the first $N$ rows of $G$ are independent as well.

The established selected source calculations already give nonzero leading minors for the first four prescribed columns. Suppose columns $r_1,\ldots,r_s$ have been chosen so that the first $s$ rows of $G$ have a unit minor on them.

The first $s+1$ rows of $G$ are independent across the $N$ available columns. Therefore some unused column extends the existing unit minor to a unit $(s+1)$-minor. Choosing, for example, the least such actual column defines a nested flag. This is ordinary finite elimination applied to a matrix whose full rank has just been proved, not an assumption of generic normality.

The atom criterion and (4.2) identify each selected unit with


$$
2^{-B_q(d)}\det A[T_q,:]\equiv1\pmod2.
$$


The universal source divisor proves optimality. ∎

The construction is an actual-column existence theorem with a deterministic selection rule. It does not perform the kernel’s triangular operation on the complete integer pencil.

### 4.4 Explicit growing original subfamilies

For each $H\ge8$, the established lifting construction gives a unique residue


$$
u_H\pmod{2^{H-8}}
$$


such that


$$
9^{18+32u}\equiv209\pmod{2^H}
\quad\text{when}\quad
u\equiv u_H\pmod{2^{H-8}}.
\tag{4.5}
$$


The lift is explicit: $u_{H+1}$ is either $u_H$ or $u_H+2^{H-8}$, because the latter change toggles the next bit.

On this original congruence class,


$$
d\equiv208\pmod{2^H}.
$$


For every $8\le a\le H$,


$$
d\bmod2^a=208\equiv1\pmod3.
$$


Hence the unit law gives a flag through


$$
\boxed{q=2^{H+1}+1.}
\tag{4.6}
$$



A concrete increasing diagonal subfamily is


$$
u=u_H+2^{H-8},\qquad H\ge8.
\tag{4.7}
$$


Every member is an original admissible index. On this subfamily,


$$
\log k=\Theta(2^H),\qquad
2^{H+1}+1=\Theta(\log k),
$$


and certainly $2^{H+1}+1<d/8$.

Thus this is a rigorously growing optimal physical flag. It is not a statistical assertion about digits, and it does not claim a linear-size flag at every original index.

For any individual original $d$, (3.8) also provides a direct, exact digit test for all larger available dyadic blocks.

---

## 5. Fully paid corrected flags and both borders

Reuse the turn13 quantities


$$
e_n=v_2\!\left(\frac{h_d}{(2n)!}\right),\qquad
E_q=\sum_{n=d-q}^{d-1}e_n,
$$




$$
\Phi_q=\prod_{j=0}^{q-1}j!,\qquad
c_q=q(q-1)+2v_2(\Phi_q),
$$


and


$$
\Theta_q(d)=c_q+2E_q+B_q(d).
$$



The established mixed-compound comparison is valid under


$$
L_d>10q+3m_d,\qquad \alpha_d-2>4q,
$$


where


$$
L_d=\alpha_d-12,\qquad m_d=1+\lfloor\log_2d\rfloor.
$$


These inequalities hold for $q\le\lfloor d/8\rfloor$.

Combining that theorem with Theorem 4.1 now gives an unconditional conclusion at every index satisfying the explicit digit certificate:



$$
\boxed{
v_2\bigl(\operatorname{content}_q(\mathcal C^{[q]})\bigr)
=\Theta_q(d)
}
\tag{5.1}
$$


for


$$
q\le \min\{N+1,\lfloor d/8\rfloor\}.
$$


The first $q$ residual physical rows attain the valuation, and


$$
\frac{\det\mathcal C^{[q]}[M,:]}{2^{\Theta_q(d)}}
\equiv
\frac{V(M)}{\Phi_q}\pmod2.
\tag{5.2}
$$



Let the actual attaining cofactor be


$$
\det\Pi_{q,k}=2^{\Theta_q(d)}\mu_{q,k},
\qquad \mu_{q,k}\ \text{odd}.
$$


Then


$$
M_{q,k}
=\frac{V_{q,k}\operatorname{adj}(\Pi_{q,k})}{2^{\Theta_q(d)}}
$$


is integral. Its exact interpolation denominator is the actual odd integer $\mu_{q,k}$.

The Vandermonde residues imply that the interpolation coefficients sum to $1\pmod2$. Every complete column of $\mathcal Q_k(s)$, including both borders, is row-constant modulo $2$. Hence


$$
\mathcal P_k^{[q]}(s)
=
\frac{\mu_{q,k}C_{q,k}(s)-M_{q,k}U_{q,k}(s)}2
\tag{5.3}
$$


is an integer pencil, coefficientwise in $s$.

Writing its actual coefficient gcd as $g_k^{[q]}$, the paid comparison with the five-column pencil is


$$
\boxed{
|\mu_{q,k}|^{d+1-q}g_k^{[5]}
=
2^{\Theta_q(d)-q-67}
|\mu_{5,k}|^{d-4}g_k^{[q]}.
}
\tag{5.4}
$$


Thus


$$
\boxed{
\nu_k^{[5]}
=\Theta_q(d)-q-67+\nu_k^{[q]}.
}
\tag{5.5}
$$



This is a growing exact payment, not an upper bound for the remaining depth.

The full transfer is


$$
|\delta_k|^{d+2}\Omega_k|\mu_{q,k}|^{d+1-q}G_k
=
|f_k|\,2^{\lambda_d+\Theta_q(d)+d+2-q}
\mathfrak D_d\,g_k^{[q]}.
\tag{5.6}
$$



No new least-clearer claim is made for $\delta_k$ or $\mu_{q,k}$. Their complete odd factors remain in these identities.

---

## 6. A multi-column mixed Cauchy residue theorem

### 6.1 Exact mixed payment

Let


$$
R^{\rm C}(i,j)=\frac{\Lambda_k}{2(d+i+j)+1}.
$$


For a forcing-column set $I$ of size $p$, set


$$
Q_I(i)=\prod_{j\in I}(2(d+i+j)+1).
$$


The established exact mixed Cauchy identity is


$$
\det[R^{\rm C}[M,I],Z[M,:]]
=
\frac{\Lambda_k^p2^{p(p-1)}\Phi_pV(I)}
     {\prod_{i\in M}Q_I(i)}
\det\left[
\binom{i}{0},\ldots,\binom{i}{p-1},
Q_I(i)Z_i
\right].
\tag{6.1}
$$


Every odd denominator remains displayed.

Consider either normalized sequence


$$
\xi_r^{(m)}=\eta_r^{(m)}
=\frac{\Delta^r\sigma_m}{2^{r+1}r!},
$$


or


$$
\xi_r^{(m)}=\theta_r^{(m)}
=\frac{\Delta^ru_m}{2^rr!}.
$$


Both satisfy


$$
\Delta^j\xi_r^{(m)}
=2^j(r+1)_j\xi_{r+j}^{(m)}.
\tag{6.2}
$$



Define


$$
K_\xi^{(p)}(a,r)
=
\sum_{t=0}^p
\binom pt\binom{r+a+t}{r}\xi_{r+a+t}\pmod2.
\tag{6.3}
$$



#### Theorem 6.1 — several mixed contact columns

Let $|M|=p+h$, $|I|=p$, and let $r_1,\ldots,r_h$ be actual permitted contact orders. Put


$$
\lambda_j^{\rm jet}=j+v_2(j!),
\qquad
H_{p,h}=c_p+\sum_{j=p}^{p+h-1}\lambda_j^{\rm jet}.
$$


Then


$$
2^{H_{p,h}}\mid
\det[R^{\rm C}[M,I],(\xi_{r_b}^{(d+i)})_{b=1}^h],
$$


and


$$
\boxed{
\frac{\det[R^{\rm C}[M,I],\xi]}{2^{H_{p,h}}}
\equiv
\mathcal N_{p+h}(M)\mathcal N_p(I)
\det[K_\xi^{(p)}(a,r_b)]_{\substack{0\le a<h\\1\le b\le h}}
\pmod2.
}
\tag{6.4}
$$



#### Proof

The polynomial $Q_I$ satisfies


$$
\frac{\Delta^jQ_I(i)}{2^jj!}\equiv\binom pj\pmod2.
$$


Indeed, write it as a polynomial in $2i$; its coefficient of degree $j$, reduced modulo $2$, is $\binom pj$, while higher-degree terms acquire an extra factor $2$ after normalized differencing.

The shifted product rule and (6.2) therefore give


$$
\frac{\Delta^j(Q_I\xi_r)}{2^jj!}
\equiv
\sum_{t=0}^j
\binom p{j-t}\binom{r+t}{t}\xi_{r+t}.
\tag{6.5}
$$


For $j=p+a$, substitute $t=a+s$. The right side becomes exactly $K_\xi^{(p)}(a,r)$.

In (6.1), the first $p$ polynomial columns occupy Newton orders $0,\ldots,p-1$. The first possible remaining orders are $p,\ldots,p+h-1$, paying the stated sum of $\lambda_j^{\rm jet}$. Every larger selection has at least one further factor $2$. The finite Newton row determinant contributes $\mathcal N_{p+h}(M)$, and the Cauchy prefactor contributes $\mathcal N_p(I)$. ∎

Thus the mixed residue is not an unrelated determinant: it is the repaired joint contact kernel at parameter $p$.

### 6.2 Evaluated dyadic mixed units

For even $p$, the joint kernel of $K_\eta^{(p)}$, after multiplication by $(1+Y+Y^2)^p$, is


$$
\operatorname{Tr}\!\left(
\omega^{2+2p}(1+\omega^2Y)^{2p}
\frac{\omega^2+\omega(X+Y)}
     {(1+\omega(X+Y))^2}
\right).
$$


For $K_\theta^{(p)}$, it is


$$
\operatorname{Tr}\!\left(
\omega^{2+2p}(1+\omega^2Y)^{2p}
\frac1{1+\omega(X+Y)}
\right).
$$


Their even-size determinants are equal: their even/odd block decompositions have the same off-diagonal block.

Let $h=2^{a+1}$, $x=p\bmod2^a$, and $t=2p\bmod3$. Then


$$
\boxed{
\det[K_\xi^{(p)}(j,r)]_{0\le j,r<h}=1
\iff
\begin{cases}
t\ne0,&x=0,\ a\text{ even},\\
t\ne1,&x=0,\ a\text{ odd},\\
t\equiv2-x\pmod3,&x>0,
\end{cases}}
\tag{6.6}
$$


for both $\xi=\eta$ and $\xi=\theta$.

When the row and forcing-column sets are consecutive, (6.6) gives exact attainment of $H_{p,h}$. When its condition fails, the first possible mixed residue vanishes.

This evaluates genuine mixed bottom factors of the full-rank expansion. It does not yet evaluate the accompanying source minors or the aggregate terminal coefficient.

---

## 7. An exact finite transformation retaining the coefficient pair

The following transformation is useful for studying the full-rank mixed terms. It is applied to the complete finite objects, not to $RN_dA$ alone.

Define the complete linear map


$$
\mathscr T(y)=RN_d(\mathcal A_dy)_{\rm top}
+\frac{\delta_k}{4}y_{\rm bot}.
\tag{7.1}
$$


Then


$$
x=\frac{\mathscr T(c)}{2^d},\qquad
z^{(r)}=\frac{\mathscr T(\Delta^r\sigma)}
                  {2^{\alpha_d+1}D_r},
\qquad
\mathfrak b_j=\Lambda_k\mathscr T(\psi_j).
$$



### 7.1 Exact forcing annihilation

For every original forcing column $T_j$,


$$
\mathscr T(T_j)
=RN_dF_ke_j+\delta_kR e_j=0,
\tag{7.2}
$$


because $N_dF_k=-\delta_kI$.

Since the first $d$ forward differences of $\tau$ lie in the span of its first $d$ shifts,


$$
\mathscr T(\Delta^r\tau)=0,\qquad 0\le r<d.
$$



The finite Neumann identity for $E+1=\Delta+2$, with $d$ even, is


$$
y=\frac12\sum_{r=0}^{d-1}\left(-\frac{\Delta}{2}\right)^r
(\Delta+2)y
+2^{-d}\Delta^dy.
\tag{7.3}
$$


Applied to $r$, it gives the exact complete constant border


$$
\boxed{\mathfrak b_0=\Lambda_k2^{-d}\mathscr T(\Delta^dr).}
\tag{7.4}
$$


The right side still contains $-\Delta^df+4\Delta^d\rho$; no factorial or rational forcing term has been removed from it.

### 7.2 Integral weighted $u$-columns

For $0\le r\le d$, define


$$
v^{(r)}=\frac{\mathscr T(\Delta^ru)}{2^{\alpha_d}D_r},
\qquad
w_*=\frac{\mathscr T(w)}{2^d}.
\tag{7.5}
$$


These columns are integral.

For the top part, the same product-rule derivation as (3.1), with $\eta$ replaced by $\theta$, proves


$$
\frac{\Delta^j\bigl((\mathcal A_d\Delta^ru)/(2^{\alpha_d}D_r)\bigr)}
     {2^j(d+1)_j}
\in\mathbb Z.
\tag{7.6}
$$


For the bottom part, $\Delta^ru=2^rr!\theta_r$, so


$$
v^{(r)}
=RN_d\,\mathsf v^{(r)}
+2^{L_d}\gamma_k\theta_r^{\rm bot},
\tag{7.7}
$$


where


$$
\gamma_k=\frac{\delta_k}{2^{2\beta_d}}
=\Lambda_k\eta_d^F\operatorname{odd}(h_d)^2
$$


is retained in full.

The new $r=d$ division includes the full $D_d=2^dd!$, and has just been proved integral. This column comes from the existing terminal border; it is not an extra original return column.

The exact relations are


$$
z^{(r)}=v^{(r)}+(r+1)v^{(r+1)},
\tag{7.8}
$$




$$
x=2^{\alpha_d-d}v^{(0)}-w_*.
\tag{7.9}
$$



### 7.3 One paired finite pencil

Set


$$
a_r=(-1)^{d-r}\frac{d!}{r!},\qquad
\kappa_d=2^{\alpha_d-d}d!,\qquad
\mathfrak c_k=\Lambda_k2^{\alpha_d}d!.
$$


Finite triangular integer column operations transform the common columns into


$$
\kappa_dv^{(d)}-w_*,
\qquad
v^{(r)}-a_rv^{(d)},\quad 0\le r<d.
$$


Adding an integer polynomial multiple of the transformed atom column to the affine border gives the exact paired pencil


$$
\boxed{
\widehat{\mathcal Q}_k(s)=
\left[
\kappa_dv^{(d)}-w_*,
\ (v^{(r)}-a_rv^{(d)})_{r<d},
\ \mathfrak b_0+s\mathfrak c_kv^{(d)}
\right].
}
\tag{7.10}
$$


Its determinant is exactly $I_{0,k}+I_{1,k}s=\det\mathcal Q_k(s)$.

All transformations have determinant one. Every displayed factorial ratio is an integer. The full odd parts of $d!$, $D_r$, $\Lambda_k$, and $\gamma_k$ remain.

In particular,


$$
\boxed{
I_{1,k}
=-\mathfrak c_k
\det[w_*,v^{(0)},\ldots,v^{(d)}].
}
\tag{7.11}
$$



The constant coefficient is retained in the same finite compound system:


$$
\boxed{
\begin{aligned}
I_{0,k}
={}&
\kappa_d\det[v^{(0)},\ldots,v^{(d)},\mathfrak b_0]\\
&-\sum_{r=0}^d\frac{d!}{r!}
\det[w_*,v^{(0)},\ldots,\widehat{v^{(r)}},\ldots,v^{(d)},\mathfrak b_0].
\end{aligned}}
\tag{7.12}
$$


The hat denotes omission. Formula (7.12) follows by multilinearity from (7.10); it is not a declaration that any of these minors is a unit.

The physical boundary is unchanged. The largest new $u$-jet uses


$$
(2d+1)+d=3d+1=3k-2.
$$



---

## 8. Full mixed expansion and an evaluated cancellation at its nominal minimum

### 8.1 Every correction remains in the expansion

The original exact decomposition is


$$
\mathcal Q_k(s)
=RN_d\mathcal A_k(s)+2^{L_d}\gamma_k\mathcal W_k(s),
$$


where


$$
\mathcal W_k(s)=
\left[
2^{M_d}\frac{c_{\rm bot}}2,\ 
(\eta_r^{\rm bot})_{r<d},\
2^{\alpha_d}\Lambda_k(r+sw)_{\rm bot}
\right],
\qquad M_d=\alpha_d-d+1,
$$


and


$$
R=R^{\rm C}-2^{\alpha_d-2}V,
$$




$$
V(i,j)=
\frac{\Lambda_k\mathfrak b(d+i+j)(2(d+i+j))!}{2^{\alpha_d}}.
\tag{8.1}
$$



For either coefficient, the determinant expansion groups terms by:

- the number $p\le d$ of product columns;
- their actual column set;
- the two $p$-element forcing/source index sets in Cauchy–Binet;
- the subset of those forcing columns taken from $V$.

The scalar of a term with $h=d+2-p$ bottom corrections and $v$ factorial forcing corrections is


$$
(2^{L_d}\gamma_k)^h(-2^{\alpha_d-2})^v.
\tag{8.2}
$$



The top-source minors containing a coefficient border are not automatically covered by the atom-return bound $B_p(d)$. This is one reason an optimization based only on the old common-source payments cannot prove the terminal estimate.

### 8.2 The linear coefficient has a uniformly normalized full-rank form

For the determinant in (7.11), write $n=d+2$. Its columns have the exact form


$$
[w_*,v^{(0)},\ldots,v^{(d)}]
=
RN_d[\mathsf a_w,\mathsf v^{(0)},\ldots,\mathsf v^{(d)}]
+2^{L_d}\gamma_k
[2^{A_d}w,\theta_0,\ldots,\theta_d],
\tag{8.3}
$$


where


$$
A_d=v_2(d!)=\alpha_d-d.
$$



The top atom $\mathsf a_w=(\mathcal A_dw)/2^d$ has odd normalized $2^j$-jets. The other top sources have the full rising divisor (7.6). Hence the source payment $B_p(d)$ applies when the atom is a product column.

For $p\ge1$, define the explicit nominal payment


$$
\boxed{
\mathcal L_p(d)
=(n-p)L_d+c_p+2E_p+B_p(d)
+\sum_{j=p}^{n-1}\bigl(j+v_2(j!)\bigr).
}
\tag{8.4}
$$



### 8.3 Factorial forcing corrections are paid in this mixed range

A stronger column-dependent payment is available for $V$. Define


$$
g_j=v_2((2(d+j))!)-\alpha_d.
$$


Then every entry of column $j$ of $V$ is divisible by $2^{g_j}$.

The factorial diagonal of $N_d$ pays $e_j$ on the same forcing index, and


$$
\begin{aligned}
e_j+g_j
&=v_2((2(d+j))!)-v_2((2j)!)-5\\
&=2d+s_2(j)-s_2(d+j)-5\\
&\ge 2d-m_d-6.
\end{aligned}
\tag{8.5}
$$



Suppose $v$ of the $p$ forcing columns come from $V$, leaving $a=p-v$ Cauchy columns. The remaining $h=n-p$ bottom contact columns pay at least


$$
c_a+\sum_{j=a}^{n-v-1}\bigl(j+v_2(j!)\bigr)
$$


after the mixed Cauchy clearing.

If the bottom atom is among them, its missing factorial row payment is at most


$$
v_2((n-1)!)=v_2((d+1)!)=A_d,
$$


which is covered by its explicit factor $2^{A_d}$.

Using (8.5), the $N_d$-payment is at least


$$
E_p+E_{p-v}+v(2d-m_d-6).
$$


Comparison with (8.4) gives a further payment of at least


$$
v\bigl(\alpha_d-4p-3m_d-12\bigr).
\tag{8.6}
$$


Here we used


$$
E_p-E_{p-v}\le v(2p+m_d),\qquad
c_p-c_{p-v}\le4pv,
$$


and


$$
\lambda_{b+h}^{\rm jet}-\lambda_b^{\rm jet}
=2h+s_2(b)-s_2(b+h)\le2h+m_d.
$$



At every original index,


$$
\alpha_d>4p+3m_d+12
\qquad( p\le d/3).
$$


Thus every factorial forcing correction is invisible at the nominal layer $\mathcal L_p(d)$ throughout this range. This conclusion uses its actual column-dependent factorial payment; it is not the old entrywise deletion.

### 8.4 The actual parity sum vanishes

#### Theorem 8.1 — full-rank mixed-layer cancellation

For


$$
\boxed{3\le p\le\lfloor d/3\rfloor,}
$$


the complete sector of (8.3) using exactly $p$ product columns is divisible by


$$
\boxed{2^{\mathcal L_p(d)+1}.}
\tag{8.7}
$$



#### Proof

By the preceding subsection, terms containing a factorial forcing correction vanish at the nominal layer.

If the atom is a bottom correction, the top sources are all $u$-contact sources and have the additional rising payment


$$
v_2((d+1)_{p-1})>0
\qquad(p\ge3).
$$


The explicit bottom atom factor covers its missing bottom factorial payment. Such terms also vanish at the nominal layer.

It remains to consider the atom as a product column and no factorial forcing correction.

The factorial-adjugate minimum is uniquely attained at


$$
I=J=T_p=\{d-p,\ldots,d-1\}.
$$


Every other pair has an additional power of $2$. Thus the entire normalized parity sum comes from this one forcing/source index pair, but still includes every choice of which $u$-contact columns are product columns.

Let


$$
B_j(r)=\binom{r+j}{r}\theta_{r+j}.
$$


Then, as row vectors indexed by $0\le r\le d$,


$$
K_\theta^{(D)}(j,\bullet)=(1+E)^D B_j,
$$


where $E$ shifts the row index. Hence


$$
\boxed{
K_\theta^{(d)}(j,\bullet)
=(1+E)^{d-p}K_\theta^{(p)}(j,\bullet).
}
\tag{8.8}
$$



The top source atom expansion leaves:

- rows $K_\theta^{(d)}(0),\ldots,K_\theta^{(d)}(p-2)$ if $p$ is odd;
- rows $K_\theta^{(d)}(0),\ldots,K_\theta^{(d)}(p-3)$, followed by
  $K_\theta^{(d)}(p-2)+K_\theta^{(d)}(p-1)$, if $p$ is even.

The mixed bottom theorem supplies the $h=n-p$ rows


$$
K_\theta^{(p)}(0),\ldots,K_\theta^{(p)}(h-1).
$$



The Laplace sum over all product/contact column choices is therefore the determinant of this stacked contact matrix, with $d+1$ columns.

If $p$ is odd, (8.8) shows that every stacked row belongs to the span of


$$
K_\theta^{(p)}(0),\ldots,K_\theta^{(p)}(d-2).
$$


There are only $d-1$ such rows, whereas the contact determinant has size $d+1$.

If $p$ is even, every stacked row belongs to the span of


$$
K_\theta^{(p)}(0),\ldots,K_\theta^{(p)}(d-1),
$$


which has at most $d$ rows.

In both cases the actual parity sum is zero. This proves (8.7). ∎

The theorem evaluates an aggregate full-rank mixed layer. It is not merely a statement that individual entries or individual lower bounds are small.

### 8.5 The nominal minimizer is explicit

The payment increments can be simplified exactly. For $1\le p<d$,


$$
\boxed{
\begin{aligned}
\mathcal L_{p+1}(d)-\mathcal L_p(d)
={}&8p-2d+5-s_2(p)\\
&+2s_2(d-p-1)-s_2(d+p-1).
\end{aligned}}
\tag{8.9}
$$


To derive this, use


$$
c_{p+1}-c_p=2p+2v_2(p!),
$$




$$
B_{p+1}-B_p=p+v_2((d+1)_{p-1}),
$$




$$
E_{p+1}-E_p=e_{d-p-1},
$$


and


$$
s_2(d-1)=s_2(d)+3,
$$


which follows from $v_2(d)=4$.

The digit terms in (8.9) are $O(\log d)$. Therefore every minimizer lies in an explicitly bounded logarithmic strip around $d/4$; for example,


$$
\left|p-\frac d4\right|\le m_d+2
\tag{8.10}
$$


is more than sufficient for the original $d$.

Also,


$$
\mathcal L_p(d)
=3d^2-2dp+4p^2+O(d\log d),
$$


uniformly for $p=O(d)$. Hence


$$
\boxed{
\min_p\mathcal L_p(d)=\frac{11}{4}d^2+O(d\log d).
}
\tag{8.11}
$$



Crucially, Theorem 8.1 applies throughout the strip (8.10). The candidate minimum is therefore **not attained at its first parity layer**.

Equation (8.11) is a minimum of proved nominal payments. It is not an upper bound for the valuation of the full determinant.

---

## 9. What this does—and does not—prove about the terminal pair

### 9.1 The repaired source obligation is now substantially answered

The old budget $b_q$ remains disproved at growing orders, as established in turn13. The present result is different:

- it uses the repaired full rising payment;
- it evaluates the $d$-dependent numerator;
- it proves consecutive physical source attainment;
- it constructs nested actual return-column flags;
- it gives zero excess above $B_q(d)$ throughout each certified flag.

The old nonconsecutive submask jet flags are not used to claim this physical minimum.

### 9.2 The full-rank obstruction is now more precise

The pure product still has rank at most $d$. It cannot provide all $d+1$ common directions or either full $(d+2)$-column determinant.

The new calculation goes further: even after using a growing number of bottom corrections, the first possible mixed layer of the linear coefficient cancels in the near-minimizing range. The reason is the exact shift relation (8.8), not an accidental fixed-size singularity.

Thus a proposed proof that simply minimizes


$$
hL_d+c_p+2E_p+B_p+\text{bottom jet payments}
$$


and declares the corresponding coefficient odd is invalid.

### 9.3 The actual Cramer dependence remains intact

The five-column residual pencil is still


$$
\mathcal P_k^{[5]}(s)
=\frac12\mathcal E_5\mathcal Q_{k,\mathrm{remaining}}(s),
$$


where


$$
\mathcal E_5=[-M_{5,k}\mid\mu_{5,k}I],
\qquad
M_{5,k}=\frac{V_{5,k}\operatorname{adj}(\Pi_{5,k})}{2^{72}}.
$$


Both $M_{5,k}$ and $\mu_{5,k}$ depend on the complete corrected pivot.

The transformations in Section 7 are exact before this elimination, so their coefficient consequences propagate through the same exact scalar identities. They do not replace the complete interpolation matrix by a Cauchy approximation.

Likewise, the established direct correction at $L_d+7$ remains a valuation of one correction summand. Nothing here turns it into a valuation of a whole residual entry or terminal coefficient.

### 9.4 A concrete next lemma

The next useful result should be an **excess-and-noncancellation lemma for the full-rank mixed layers**, not another fixed pivot.

A specific sufficient version would prove, on stated original indices, that after the cancellations in Theorem 8.1:

1. the complete mixed expansion of at least one coefficient has a nonzero aggregate residue within $O(d\log d)$ additional binary layers of the explicit minimum in (8.11);
2. the residue includes all competing product counts, all near-minimal factorial-adjugate index sets, and every correction capable of reaching that precision;
3. the complete constant coefficient is tracked through (7.10)–(7.12), rather than assigned an assumed terminal unit.

For the linear coefficient alone, an estimate of the form


$$
v_2\det[w_*,v^{(0)},\ldots,v^{(d)}]
\le \min_p\mathcal L_p(d)+O(d\log d)
\tag{9.1}
$$


would already be stronger than the requested quadratic binary budget, because the additional factor $\mathfrak c_k$ in (7.11) has only $O(d)$ binary valuation.

But (9.1) is **open**. The proved leading cancellation prevents claiming it from the present parity calculation.

More generally, the exact original target is


$$
\min(v_2(I_{0,k}),v_2(I_{1,k}))
\le \frac{15}{4}k^2+d+5+O(k\log k),
\tag{9.2}
$$


because


$$
\min(v_2(I_{0,k}),v_2(I_{1,k}))
=d+69+\nu_k^{[5]}.
$$


No theorem above proves (9.2).

---

## 10. All-prime and analytic consequences remain separate

The actual primitive identities remain


$$
\boxed{
\frac{|P_{1,k}^{[5]}|}{g_k^{[5]}}
=\frac{|H_{1,k}|}{G_k}=q_k,
}
$$


and


$$
\boxed{
\frac{|P_{0,k}^{[5]}+P_{1,k}^{[5]}(e+\pi)|}{g_k^{[5]}}
=\frac{|H_k(e+\pi)|}{G_k}
=\ell_k>0.
}
\tag{10.1}
$$



The established ternary information is retained only at its proved scope:


$$
v_3(\mathscr L_k)=v_3(\mathscr R_k)=E_k,
\qquad
E_k=\frac{(k-2)(k-1-2s)}2
\quad(k=3^s),
$$


and


$$
E_k\le v_3(G_k)\le2E_k+s+1.
$$



The other odd-prime descents remain open:


$$
v_p(\mathscr L_k),v_p(\mathscr R_k)\le B_p(k)
\qquad(5\le p\le6k-5),
$$


where


$$
B_p(k)=k\bigl(2\mathbf1_{p=3}+v_p(\Lambda_k)\bigr)
+4\sum_{j<k}v_p(j!),
$$


and the large-prime exclusion remains open:


$$
v_p(\mathscr L_k)=v_p(\mathscr R_k)=0
\qquad(p>6k-5).
$$



The closed same-$H$ analytic estimate is reused:


$$
\log|H_k(e+\pi)|
\ge
4k^2\log k+
\left(15\log2-\frac92\log3+\frac4{85}\right)k^2
+o(k^2).
$$


Together with all the independent arithmetic targets, the contemplated binary bound would yield the already certified positive whole-error divergence margin


$$
\frac{57}{4}\log2-\frac72\log3-\frac{506}{85}>0.
$$



That would retire this producer as a source of primitive whole-error decay. It would not decide the rationality of $e+\pi$.

If the arithmetic bounds were proved only on the diagonal original subfamily (4.7), the implication would apply only there. It would not establish an all-index retirement statement.

---

## 11. Computation scope

No tools have been used.

No new bounded calculation is indispensable to the proofs in this report, and **no new computation is requested**.

In particular, this report does not request:

- a rerun of the old root-filter receipt;
- a fixed $32$- or $33$-column diagnostic;
- an original-sized source array;
- an original-sized determinant or Smith calculation.

The new dyadic determinant law is proved by the finite recurrence (3.4)–(3.7). The mixed cancellation is proved by the explicit shift relation (8.8). A finite numerical check of either theorem would authenticate only its stated finite inputs, not the remaining terminal estimate.

The next unresolved issue is a uniform higher-precision mixed-excess theorem. No bounded calculation currently specified here would establish that theorem.

---

## 12. Compact proved/conditional/open ledger

| Statement | Status |
|---|---|
| Original $D_r$, complete forcing, finite boundaries, $\Omega_k,\delta_k,\mu_{q,k}$, and all-prime transfers | **Established reuse, preserved exactly** |
| Old source budget $b_q$ attainable at growing orders | **Disproved in established work** |
| Dyadic law (3.8) for the $d$-dependent repaired kernel | **New proved evaluation** |
| Full integer source divisor $\mathcal F_q(d)$ | **New proved statement** |
| Optimal nested physical flags through each digit-certified block | **New proved statement** |
| Zero excess above $B_q(d)$ on those flags | **New proved statement** |
| Explicit growing original subfamily (4.7) | **New proved application; no digit statistics** |
| Complete corrected flags within $q\le d/8$, with both borders paid | **New consequence of the established mixed window and the new source theorem** |
| Multi-column mixed residue formula and dyadic mixed unit law | **New proved statements** |
| Exact paired transformation (7.10)–(7.12) | **New proved finite identities** |
| First full-rank mixed parity layer near $p=d/4$ is nonzero | **False: its aggregate parity is proved zero** |
| Complete $p$-sector divisibility $2^{\mathcal L_p+1}$ for $3\le p\le d/3$ | **New proved cancellation theorem** |
| Upper bound for the excess after this cancellation | **Open** |
| Required bound for the complete joint depth $\nu_k^{[5]}$ | **Open** |
| Other odd-prime descents and large-prime exclusion | **Separate open obligations** |
| Primitive whole-error divergence | **Conditional on all arithmetic targets** |
| Rationality or irrationality of $e+\pi$ | **Unresolved** |

## Final conclusion

The repaired source problem now has an evaluated growing solution: the joint kernel’s explicit numerator yields an exact dyadic unit law, and every certified block produces a nested flag of actual atom-containing physical source minors attaining the optimal payment $B_q(d)$. Within the already proved correction window, this gives growing complete corrected cofactors and fully paid interpolation of both borders.

The full-rank mixed calculation also produces a definite result, but it is an obstruction rather than the desired upper bound. Near the nominal minimizing product count $p=d/4$, the aggregate leading parity of the linear coefficient vanishes because its top and bottom contact rows satisfy an exact finite shift relation.

The remaining mathematical bottleneck is therefore precise: **bound the higher 2-adic excess after this structural mixed cancellation and prove noncancellation in the complete terminal coefficient pair**. The constant border, factorial forcing corrections outside the paid range, actual Cramer dependence, final all-prime gcd, primitive denominator, and nonzero whole error must all remain in that argument.

No unconditional conclusion about the rationality of $e+\pi$ has been obtained.
