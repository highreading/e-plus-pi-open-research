> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the rectangular source flag and the multiple-return quarter window

## 1. Conclusions

The new mathematical arguments in **A2 turn 13**, the parent **rectangular contact-rank note**, and the parent **multiple-return quarter-window note** pass this independent audit at the scopes stated below.

The principal conclusions are:

1. **The rising source payment is valid.**  
   Its full integer form is
   

$$
\mathcal B_q(d)
   =2^{\binom q2}\prod_{j=0}^{q-2}(d+1)_j.
$$


   Its binary depth is
   

$$
B_q(d)=\binom q2+\sum_{j=0}^{q-2}v_2((d+1)_j).
$$


   The older depth $b_q$ is impossible at every $q\ge18$, regardless of the chosen original return columns.

2. **The rectangular root argument is correct.**  
   Both unit denominators must be cleared. The resulting polynomial has degree at most $L-1$, and its forced root multiplicity is at least $m$, while the polynomial $Q$ carrying the proposed row relation has degree less than $m$. This proves the asserted rectangular rank without a growing determinant calculation.

3. **The physical source transfer is correct, including even sizes.**  
   At odd source sizes the cheapest atom position is unique. At even sizes two positions tie, and their cofactors add. The nested flag is a flag of **original columns**, not of columns transformed by the parity convolution.

4. **The multiple-return mixed payment is correct.**  
   The finite Newton argument pays all weighted return columns simultaneously, even in the presence of arbitrary free integer columns. The atom is used only as such a free column. The case $p=0$ is covered.

5. **All correction terms are paid in the quarter window.**  
   The three strict inequalities
   

$$
L_d>8q+4m_d+6,\qquad
   \alpha_d-2>4q,\qquad
   d-2q+1-2m_d>0
$$


   imply the complete corrected-minor comparison through depth $\Theta_q(d)$. Their largest odd admissible rank is
   

$$
q_{\rm quarter}=\frac d4-O(\log d).
$$



6. **On the narrower stated original rotation subfamily, the complete cofactor depth is attained at every size**
   

$$
5\le q\le q_{\rm quarter},
$$


   not just at odd sizes.

The independent audit does **not** extend to the new all-order similarity theorem in my turn 21. Its different audit remains pending. None of the arguments below uses that theorem.

### New result after the audit

I also prove a stronger statement at the first evaluated mixed layer of the actual paid five-column residual pencil. It includes the feedback from the corrected pivot, rather than only the direct bottom-return summand.

Let $\mathcal P_k^{[5],{\rm C}}$ be the precisely defined pure-Cauchy cofactor reference in Section 9. Then


$$
\boxed{
\frac{\mathcal P_k^{[5]}-\mathcal P_k^{[5],{\rm C}}}
     {2^{L_d+7}}
\pmod2
}
$$


is an explicitly evaluated **rank-one matrix**. On a remaining return column $r$, its residue is


$$
\boxed{
\binom i5\,
\Bigl(S_5(r)+\eta_{r+2d+(r\mathbin{\&}d)}\Bigr),
\qquad 5\le i\le d+1.
}
$$


Both complete affine coefficient borders have residue zero at this layer. The actual remaining returns $r=2$ and $r=3$, at residual row $i=5$, both attain the difference depth


$$
\boxed{L_d+7.}
$$



This is an evaluated statement about the **whole first mixed perturbation of the paid residual pencil**, not a valuation of the whole residual entry, a new common-column pivot, or a terminal coefficient bound.

The rationality or irrationality of $e+\pi$ remains unresolved.

---

## 2. Original objects, finite boundaries, and paid arithmetic interface

### 2.1 The unchanged domain

Throughout,


$$
\boxed{k=9^{18+32u},\qquad u\ge0,\qquad d=k-1.}
$$


In particular,


$$
d\equiv2\pmod3,\qquad v_2(d)=4,\qquad d\equiv208\pmod{256}.
$$



The finite index ranges are retained:

- top-source row: $0\le n<d$;
- original return order: $0\le r<d$;
- a top jet is used only when $n+j<d$;
- residual row $i$, $0\le i\le d+1$, is original physical row $d+i$.

The last original moment, factorial, and odd denominator remain


$$
\boxed{3k-2=3d+1,\qquad (6k-4)!,\qquad 6k-5=6d+1.}
$$



### 2.2 Complete sequences and returns

Retain


$$
a_0=1,\qquad a_n=1-na_{n-1},
$$




$$
u_n=a_{2n},\quad f_n=(2n)!,\quad w_n=(-1)^n,\quad c_n=u_n-w_n,
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
\boxed{
\tau_n=-(2n+2)!-(2n)!+\frac4{2n+1}.
}
$$


Thus, with


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5),
$$


the actual integer forcing is


$$
\boxed{
T_n=-\Lambda_k\bigl((2n+2)!+(2n)!\bigr)
+\frac{4\Lambda_k}{2n+1}.
}
$$



No factorial term is suppressed.

### 2.3 Actual clearers, contents, gcd, denominator, and whole error

The determinant is


$$
H_k(s)=
\det\left[
(c_{m+j})\
\middle|\
\bigl(\Lambda_k(r_{m+j}+s(-1)^{m+j})\bigr)
\right]
=H_{0,k}+H_{1,k}s,
$$


with $0\le m<2k$, $0\le j<k$.

The individual least entry clearers are


$$
\Lambda_{k,j}
=\operatorname{lcm}(1,3,\ldots,4k+2j-3).
$$


Set


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|),\qquad
d_{H,k}=\gcd(\Lambda_k^k,H_{0,k},H_{1,k}).
$$


The actual least simultaneous coefficient clearer of $H_k/\Lambda_k^k$, and the content after clearing, are


$$
\boxed{
\frac{\Lambda_k^k}{d_{H,k}},
\qquad
\frac{G_k}{d_{H,k}}.
}
$$



The original rectangles remain


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


For their maximal-minor contents,


$$
\mathscr R_k=\delta_{2k-1}(Z_k),\qquad
\mathscr L_k=\delta_{2k-1}(Y_k),
$$


the established interface is


$$
\operatorname{lcm}(\mathscr L_k,\mathscr R_k)
\mid G_k\mid \Lambda_k\mathscr L_k\mathscr R_k.
$$



At every original index, the retained sign and nonvanishing results give


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
$$


All gcds here are all-prime gcds. None is replaced by a binary lower divisor.

### 2.4 Exact corrected columns

Put


$$
P_d(x)=\prod_{h=0}^{d-1}(2x+2h+1),\qquad
\mathcal A_dy=\Delta^d(P_dy).
$$


The equality uses the actual evenness of $d$. The operator acts only on the first $d$ original rows, with determinant payment


$$
\Omega_k=\prod_{n<d}P_d(n).
$$



For


$$
b(t)=4t^2+6t+3,
$$


the complete top forcing block is


$$
F_k(n,j)=
-\Lambda_k\sum_{h=0}^d(-1)^h\binom dh
P_d(n+h)b(n+h+j)(2(n+h+j))!,
\quad n,j<d.
$$


Since


$$
b(t)(2t)!=(2t+2)!+(2t)!,
$$


this is the full forcing block.

Write


$$
F_k=-\Lambda_kD_fK_dD_f,\qquad
D_f=\operatorname{diag}((2n)!)_{n<d},
$$


and


$$
\eta_d^F=\det K_d.
$$


The oddness of $\eta_d^F$ and of all leading principal determinants of $K_d$ is established reuse.

Retain


$$
\alpha=\alpha_d=v_2((2d)!),\qquad
\beta=v_2((2d-2)!),\qquad \alpha-\beta=5,
$$




$$
h_d=(2d-2)!,\qquad
\widehat D_f=h_dD_f^{-1},
$$




$$
N_d=\widehat D_f\operatorname{adj}(K_d)\widehat D_f,
\qquad
\delta_k=\Lambda_k\eta_d^Fh_d^2,
$$




$$
f_k=(-\Lambda_k)^d\eta_d^F
\left(\prod_{n<d}(2n)!\right)^2.
$$



The complete bottom forcing is


$$
\boxed{
R(i,j)=
\frac{\Lambda_k}{2(d+i+j)+1}
-\frac{\Lambda_k}{4}b(d+i+j)(2(d+i+j))!,
\quad i\le d+1,\ j<d.
}
$$



Every return division remains the full division


$$
D_r=2^rr!,\qquad
\mathfrak D_d=\prod_{r<d}D_r.
$$


Define


$$
\mathsf a_n=\frac{(\mathcal A_dc)_n}{2^d},
\qquad
t_n^{(r)}
=\frac{(\mathcal A_d\Delta^r\sigma)_n}{2^{\alpha+1}D_r}.
$$


The corrected columns are exactly


$$
x=RN_d\mathsf a+\frac{\delta_k}{2^{d+2}}c_{\rm bot},
$$




$$
z^{(r)}
=RN_dt^{(r)}
+\frac{\delta_k}{2^{\alpha+3}D_r}(\Delta^r\sigma)_{\rm bot}.
$$


For $\psi_0=r,\ \psi_1=w$, both borders remain


$$
\boxed{
\mathfrak b_h
=RN_d\Lambda_k(\mathcal A_d\psi_h)_{\rm top}
+\frac{\delta_k\Lambda_k}{4}(\psi_h)_{\rm bot},
\qquad h=0,1.
}
$$


Thus


$$
\mathcal Q_k(s)=
[x,z^{(0)},\ldots,z^{(d-1)},\mathfrak b_0+s\mathfrak b_1].
$$



It is useful to set


$$
L_d=\alpha-12,\qquad M_d=\alpha-d+1,\qquad
\gamma_k=\delta_k/2^{2\beta},
$$


where $\gamma_k$ is the actual odd integer


$$
\Lambda_k\eta_d^F\operatorname{odd}(h_d)^2.
$$


Then, exactly,


$$
\mathcal Q_k(s)
=RN_d\mathcal A_k(s)+2^{L_d}\gamma_k\mathcal W_k(s),
$$


where


$$
\mathcal W_k(s)=
\left[
2^{M_d}\frac{c_{\rm bot}}2,\
(\eta_r^{(d+i)})_{r<d},\
2^\alpha\Lambda_k(r+sw)_{\rm bot}
\right].
$$


Also,


$$
R=R^{\rm C}-2^{\alpha-2}V,
$$


with


$$
R^{\rm C}(i,j)=\frac{\Lambda_k}{2(d+i+j)+1},
\qquad
V(i,j)=\frac{\Lambda_kb(d+i+j)(2(d+i+j))!}{2^\alpha}.
$$


Both $R^{\rm C}$ and $V$ are integer matrices on the stated finite ranges.

### 2.5 The already paid five-column interface

The fixed selected columns are


$$
[x,z^{(1)},z^{(0)},z^{(5)},z^{(4)}].
$$


Their established cofactor depths $5,19,39,72$, and the actual odd quotients $\mu_{2,k},\ldots,\mu_{5,k}$, are reused.

In particular, the paid all-prime identities retain


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


Thus


$$
\nu_k=64+\nu_k^{[5]}.
$$



With $\lambda_d=d\alpha+4d+4$,


$$
\boxed{
|\delta_k|^{d+2}\Omega_k|\mu_{5,k}|^{d-4}G_k
=
|f_k|\,2^{\lambda_d+d+69}\mathfrak D_d\,g_k^{[5]}.
}
$$


Consequently,


$$
v_2(G_k)=\chi_k+64+\nu_k^{[5]},
$$


where


$$
\chi_k=d^2+4d+29+(d+4)s_2(d)-3\sum_{n<d}s_2(n).
$$



No new theorem below alters this interface.

---

## 3. Audit of A2 turn 13’s source-rank statements

### 3.1 Established entry laws and their precise normalization

The all-order contact-entry law and the full product-rule identity are established reuse. The three normalizations must nevertheless remain distinct:


$$
J^{\mathbb Z}_{jr}(n)
=\frac{\Delta^jt_n^{(r)}}{2^j(r+1)_j},
$$




$$
U^{\mathbb Z}_{jr}(n)
=\frac{\Delta^jt_n^{(r)}}{2^j(d+1)_j},
$$


and


$$
\mathcal J_{jr}
=\frac{\Delta^jt_n^{(r)}}{2^jj!}\pmod2.
$$


They satisfy


$$
\binom{d+j}{j}U^{\mathbb Z}_{jr}
=
\binom{r+j}{j}J^{\mathbb Z}_{jr},
$$


and hence


$$
\mathcal J_{jr}
=\binom{d+j}{j}U_{jr}
=\binom{r+j}{j}J_{jr}.
$$



The full rising identity is


$$
U^{\mathbb Z}_{jr}(n)
=
o_d\sum_{h=0}^d
\binom dh Q_h(n)
\binom{d-h+r+j}{r}
\eta_{d-h+r+j}^{(n+h)}.
$$


Every summand is integral. This proves divisibility by the entire integer


$$
2^j(d+1)_j,
$$


not just its binary part.

The two-carry rule in A2 is also correctly scoped. In


$$
C(a,b,K)
=\omega^{2b}
\sum_{\substack{u+v=K\\u\subseteq_{\rm bit}a\\v\subseteq_{\rm bit}b}}
\omega^{-v},
$$


each admissible pair of binary choices corresponds to exactly one carry path. There are only carries $0,1$, and a zero input digit gives one zero choice. This proves the stated logarithmic entry cost. It does not prove a logarithmic growing-determinant algorithm.

### 3.2 Independent derivation of the new bitwise law

The claimed law is


$$
\boxed{
\mathcal J_{jr}
=
\begin{cases}
\eta_{j+r+2d+(r\mathbin{\&}d)},
&j\mathbin{\&}(d\mathbin{|}r)=0,\\
0,&j\mathbin{\&}(d\mathbin{|}r)\ne0.
\end{cases}
}
$$



If $j\mathbin{\&}r\ne0$, the factor $\binom{r+j}{j}$ is even. If $j\mathbin{\&}d\ne0$, the factor $\binom{d+j}{j}$ is even. It remains to evaluate the no-carry case


$$
j\mathbin{\&}r=j\mathbin{\&}d=0.
$$



The identity used by A2 can be checked directly by Vandermonde:


$$
\binom{d+j}{t+j}\binom{t+j+r}{j+r}
=
\sum_a
\binom ra\binom{d+j}{j+a}\binom{d-a}{t-a}.
$$


Indeed, expand


$$
\binom{t+j+r}{t}
=\sum_a\binom ra\binom{t+j}{t-a}
$$


and then combine the last binomial with $\binom{d+j}{t+j}$.

Modulo $2$, a surviving $a$ must be a binary subset of both $r$ and $d$. Thus


$$
a\subseteq_{\rm bit} e,\qquad e=r\mathbin{\&}d.
$$


Since $d$ is even, both $a$ and $d-a$ are even.

Using


$$
\eta_m
=\operatorname{Tr}\!\left(
\omega^{m+2}[1+(m+1)\omega]
\right),
$$


the inner sum, after $t=a+h$, is


$$
\operatorname{Tr}\!\left(
\omega^{j+r+2+2d-a}[1+(j+r+1)\omega]
\right).
$$


The derivative term vanishes here because the exponent $d-a$ is even. This is a consequence of the no-carry reorganization; it does not remove the derivative term from the general filter.

Finally,


$$
\sum_{a\subseteq_{\rm bit}e}\omega^{-a}
=(1+\omega^{-1})^e=\omega^e.
$$


Since $e$ is even, the resulting trace is precisely


$$
\eta_{j+r+2d+e}.
$$



**Verdict: PASS.**

### 3.3 Exact rank and actual return columns

Let


$$
m_d=1+\lfloor\log_2d\rfloor,\qquad
F_d=2^{m_d}-1-d.
$$


For $1\le q\le d$, define


$$
C_d(q)=\#\{0\le j<q:j\mathbin{\&}d=0\}.
$$



The vanishing rows give the upper bound


$$
\operatorname{rank}\mathcal J\le C_d(q).
$$


List the surviving row indices increasingly as $j_0,\ldots,j_{C_d(q)-1}$, and choose


$$
r_\ell=F_d-j_\ell.
$$


Because $j_\ell$ is a submask of $F_d$, this subtraction is its binary complement within $F_d$. In particular,


$$
0\le r_\ell\le F_d<2^{m_d-1}\le d.
$$


Thus all selected returns are actual returns $r<d$.

The entry in row $j_a$, column $r_\ell$, can be nonzero only if


$$
j_a\subseteq_{\rm bit}j_\ell.
$$


It vanishes for $a>\ell$. On the diagonal,


$$
j_\ell+r_\ell=F_d,\qquad r_\ell\mathbin{\&}d=0.
$$


The diagonal value is


$$
\eta_{F_d+2d}=\eta_{2^{m_d}-1+d}.
$$


Since $d\equiv2\pmod6$, the last index is $3$ or $5\pmod6$; both corresponding contact parities are $1$. The selected matrix is therefore triangular with unit diagonal.

Hence


$$
\boxed{\operatorname{rank}\mathcal J=C_d(q).}
$$



The claimed submask flags are valid **jet flags**. They need not use minimizing consecutive jet orders and do not, by themselves, solve the atom-containing physical-source problem.

The lifting argument is also valid. Since


$$
v_2(9^{32}-1)=8,
$$


adding $2^{H-8}$ to $u$ toggles precisely the next required bit modulo $2^{H+1}$. Thus every congruence


$$
d\equiv208\pmod{2^H}
$$


is obtained on an infinite original residue class of $u$. This proves unbounded jet-flag sizes without a digit-distribution conjecture.

**Verdict: PASS, with the jet/physical distinction retained.**

---

## 4. The rising source divisor and the atom cofactor

Write


$$
S_j=(d+1)_j.
$$


The sequence $S_j$ is a divisibility chain.

For one atom and $q-1$ return sources, finite Newton expansion followed by Cauchy–Binet gives the full integer divisor


$$
\boxed{
\mathcal B_q(d)=2^{\binom q2}\prod_{j=0}^{q-2}S_j.
}
$$


To see the payment termwise, choose increasing Newton orders


$$
j_0<\cdots<j_{q-1}.
$$


Every row contributes $2^{j_a}$. Expansion in the atom column leaves $q-1$ rising factors, whose product is divisible by


$$
\prod_{j=0}^{q-2}S_j.
$$


The Pascal minors in the finite Newton expansion are integers.

If all $q$ sources are returns, one obtains the stronger integer divisor


$$
2^{\binom q2}\prod_{j=0}^{q-1}S_j.
$$



Consequently,


$$
B_q(d)=v_2(\mathcal B_q(d))
=\binom q2+\sum_{j=0}^{q-2}v_2(S_j).
$$



### 4.1 Exact obstruction to the old depth

The difference from the older payment is


$$
B_q(d)-b_q
=\sum_{j=0}^{q-2}v_2\binom{d+j}{j}.
$$


At every original index, the $2^4$-digit of $d$ is present. The term $j=16$ is positive. Therefore


$$
\boxed{B_q(d)>b_q\qquad(q\ge18).}
$$



This is an obstruction in the original sources, for every choice of original return columns. It is not a counterexample involving unrelated sequences.

### 4.2 Exact odd-size and even-size source tests

For the minimizing consecutive top rows


$$
T_q=\{d-q,\ldots,d-1\},
$$


the forward-difference row transformation has determinant $1$.

Put


$$
A_j=\frac{\Delta^j\mathsf a_{d-q}}{2^j},
\qquad A_j\equiv1\pmod2.
$$


Expansion in the atom column gives the exact integral formula


$$
\frac{\det A_S[T_q,:]}{\mathcal B_q(d)}
=
\sum_{j=0}^{q-1}
(\pm)A_j\,\frac{S_{q-1}}{S_j}
\det U^{\mathbb Z}[\{0,\ldots,q-1\}\setminus\{j\},S_{\rm ret}].
\tag{4.1}
$$



This formula retains every odd rising factor before parity is taken.

- If $q$ is odd, $q-1$ is even and
  

$$
v_2(S_{q-1})-v_2(S_{q-2})=v_2(d+q-1)>0.
$$


  The unique cheapest atom position is $j=q-1$.

- If $q$ is even, $q-1$ is odd. The last increment is zero, while the preceding increment is positive. Exactly the last two atom positions tie. Their odd multipliers and normalized atom entries both reduce to $1$.

Thus the binary contact tests are exactly



$$
U_0,\ldots,U_{q-2}\qquad(q\text{ odd}),
$$


and


$$
U_0,\ldots,U_{q-3},\ U_{q-2}+U_{q-1}
\qquad(q\text{ even}).
$$



**Verdict: PASS.** In particular, the even-size statement cannot be justified by a unique-minimum argument; the tied cofactor sum is essential.

---

## 5. Independent audit of the mixed Cauchy and complete-compound arguments

### 5.1 Exact mixed Cauchy identity

Let $I$ contain $a$ distinct increasing forcing-column indices, and let


$$
Q_I(i)=\prod_{j\in I}(2(d+i+j)+1),
\qquad
\Phi_a=\prod_{j=0}^{a-1}j!.
$$


For a square mixed determinant,


$$
\boxed{
\det[R^{\rm C}[M,I],Z[M]]
=
\frac{\Lambda_k^a2^{a(a-1)}\Phi_aV(I)}
     {\prod_{i\in M}Q_I(i)}
\det\left[
\left(\binom ij\right)_{j<a},\ Q_I(i)Z_i
\right].
}
\tag{5.1}
$$



Here every odd denominator is explicit.

After multiplying row $i$ by $Q_I(i)$, the Cauchy columns become


$$
\Lambda_k\prod_{j'\in I,\ j'\ne j}(2i+2d+2j'+1).
$$


Their coefficient determinant in the monomial basis is


$$
\Lambda_k^a2^{a(a-1)}V(I).
$$


One may verify the sign by evaluating at the distinct roots
$-d-j-\tfrac12$: the sign from the evaluation Vandermonde cancels the sign from the products of root differences. Passing from monomials to the binomial basis contributes $\Phi_a$. This proves (5.1).

Since


$$
\frac{V(I)}{\Phi_a}\in\mathbb Z,
$$


the binary payment is


$$
c_a=a(a-1)+2v_2(\Phi_a).
$$



An odd denominator in (5.1) is a binary unit, not the integer $1$. No all-prime divisibility assertion is obtained by silently discarding it.

### 5.2 The factorial-adjugate minimum

Set


$$
e_n=v_2\!\left(\frac{h_d}{(2n)!}\right),
\qquad
E_q=\sum_{n=d-q}^{d-1}e_n.
$$


The $e_n$ strictly decrease with $n$, because


$$
e_n-e_{n+1}=1+v_2(n+1)>0.
$$



For a $q$-minor of $N_d$,


$$
v_2\det N_d[I,J]\ge
\sum_{i\in I}e_i+\sum_{j\in J}e_j\ge2E_q.
$$


Equality can occur at the minimum only for


$$
I=J=T_q.
$$


For that principal minor, Jacobi’s complementary-minor identity reduces the remaining adjugate factor to an odd power of $\det K_d$ times the leading complementary determinant of $K_d$, which is odd.

Thus the minimum $2E_q$ is attained uniquely at the principal pair $T_q,T_q$. This uses the odd leading complementary determinant, not merely $\det K_d$ being odd.

### 5.3 Audit of A2’s $d/8$ comparison

For a selected $q$-column common matrix, suppose:

- $h$ columns come from the bottom-correction matrix;
- $p=q-h$ columns remain product columns;
- $v$ of those $p$ forcing columns use the factorial part of $R$;
- $a=p-v$ are rational Cauchy columns.

Generalized Cauchy–Binet gives a $p$-minor of $N_d$, a $p$-minor of the actual top sources, and a mixed bottom determinant. Every such term has lower depth


$$
hL_d+v(\alpha-2)+c_a+2E_p+B_p(d).
\tag{5.2}
$$


If the atom is taken from the bottom correction, the remaining source columns are all returns, so $B_p$ is still valid. The atom’s extra scalar is retained in the exact expansion; ignoring its nonnegative depth only weakens this particular estimate.

The relevant marginal formulas are


$$
c_r-c_{r-1}=2\bigl(r-1+v_2((r-1)!)\bigr),
$$




$$
E_r-E_{r-1}
=2r-2+s_2(d-r)-s_2(d-1),
$$


and, for $r\ge2$,


$$
B_r-B_{r-1}=r-1+v_2((d+1)_{r-2}).
$$


At $r=1$, all increments are zero.

They imply, for $r\le q\le d$,


$$
c_r-c_{r-1}\le4q,\qquad
E_r-E_{r-1}\le2q+m_d,\qquad
B_r-B_{r-1}\le2q+m_d.
$$


Therefore every term containing a correction exceeds


$$
\Theta_q=c_q+2E_q+B_q
$$


under A2’s strict inequalities


$$
L_d>10q+3m_d,\qquad \alpha-2>4q.
$$



The verification for $q\le d/8$ is valid on the enormous original domain. No asymptotic assertion is needed in place of the strict inequalities.

Finally, the unique minimal $N_d$-minor and the exact Cauchy determinant give


$$
\boxed{
\frac{\det\mathcal C_S[M]}{2^{\Theta_q}}
\equiv
\frac{\det A_S[T_q]}{2^{B_q}}\,
\frac{V(M)}{\Phi_q}\pmod2.
}
\tag{5.3}
$$



**Verdict: PASS.** This is a complete compound comparison, not an entrywise deletion of the corrections.

---

## 6. Independent audit of the rectangular root theorem

Only the established joint kernel is used here:


$$
\operatorname{Tr}\!\left(
(1+\omega^2Y)^{2d}
\frac{\omega^2+\omega(X+Y)}{(1+\omega(X+Y))^2}
\right).
$$


The corrected phase and the already closed leading $64/128$ evaluations are reused; their arithmetic audit is not repeated.

### 6.1 Derivation of the actual cross rectangle

The numerator is


$$
(1+\omega^2Y)^{2d}
=(1+\omega Y^2)^d.
$$


The coefficient of $S^s$ in


$$
\frac{\omega^2+\omega S}{(1+\omega S)^2}
$$


is $\omega^{s+2}$ for even $s$, and $\omega^s$ for odd $s$.

For row $2h$, column $2l+1$, and numerator term $Y^{2v}$, Lucas reduction gives


$$
\binom{2(h+l-v)+1}{2(l-v)+1}
\equiv\binom{h+l-v}{l-v}.
$$


For row $2h+1$, column $2l$, the same reduction gives the same binomial coefficient. The odd/odd block is zero.

Squaring inside the trace changes the internal exponent to


$$
h+l+v+2.
$$


Consequently, after parity reordering, the first $2m$ rows and first $2L$ columns are


$$
\begin{pmatrix}
C_{m,L,d}&A_{m,L,d}\\
A_{m,L,d}&0
\end{pmatrix},
$$


where


$$
\boxed{
A(h,l)
=[Y^l]\operatorname{Tr}\!\left(
\omega^{h+2}
\frac{(1+\omega^2Y)^d}{(1+\omega Y)^{h+1}}
\right).
}
\tag{6.1}
$$


This is the required cross rectangle with the correct conjugate phase.

### 6.2 Clearing both denominators and reducing the exponent

Let $L=2^a$, put $\rho=d\bmod L$, and assume


$$
\boxed{2L\le d,\qquad m\ge1,\qquad \rho+2m\le L.}
$$



Suppose a binary row relation $c_0,\ldots,c_{m-1}$ annihilates all $L$ columns. Set


$$
p(Y)=1+\omega Y,\qquad q(Y)=1+\omega^2Y,
$$




$$
Q(Y)=\sum_{h=0}^{m-1}
c_h\omega^{h+2}p(Y)^{m-h-1}.
$$


Then $\deg Q\le m-1$, and the row relation is


$$
F+F^\sigma=0\pmod{Y^L},
\qquad
F=\frac{q^dQ}{p^m}.
$$



Both $p^m$ and $q^m$ have constant term $1$. Multiplying by **both** denominators gives


$$
q^{d+m}Q+p^{d+m}Q^\sigma=0\pmod{Y^L}.
\tag{6.2}
$$



Because $L$ is dyadic,


$$
p^L\equiv q^L\equiv1\pmod{Y^L}.
$$


The inequality $\rho+2m\le L$, with $m\ge1$, implies


$$
\rho+m<L.
$$


Thus there is no wrap when reducing the exponent:


$$
d+m\bmod L=\rho+m.
$$


Equation (6.2) is therefore the congruence of the polynomial


$$
P(Y)=q^{\rho+m}Q+p^{\rho+m}Q^\sigma.
$$


Its degree satisfies


$$
\deg P\le \rho+2m-1\le L-1.
$$


Hence congruence modulo $Y^L$ implies the exact polynomial identity $P=0$.

### 6.3 Root multiplicity

At the root $Y=\omega^2$ of $p$, the factor $q$ is nonzero. Therefore


$$
p^{\rho+m}\mid Q.
$$


But


$$
\deg Q<m\le\rho+m.
$$


Thus $Q=0$. The polynomials $p^{m-h-1}$, multiplied by nonzero scalars $\omega^{h+2}$, form a basis of the degree-$<m$ polynomials. Every $c_h$ is zero.

Therefore $A_{m,L,d}$ has row rank $m$.

The full parity-reordered rectangle has row rank $2m$: its odd-column block first kills any even-row coefficients in a row relation, and the even-column block then kills the odd-row coefficients.

### 6.4 Undoing only the normalized parity convolution

Multiplication by $(1+Y+Y^2)^d$ is a finite unit upper-triangular transformation on the first $2L$ **normalized parity columns**. Its inverse exists on that same finite rectangle. Thus the original normalized contact rectangle also has row rank $2m$.

This proves the existence of a unit minor using distinct original columns


$$
0\le r<2L\le d.
$$


It does not install transformed parity columns into the integer pencil.

Adding the atom and using Section 4 gives an attaining source minor on


$$
T_{2m+1}=\{d-2m-1,\ldots,d-1\}.
$$


Every jet satisfies $n+j<d$.

**Verdict: PASS, including the finite cutoff, root multiplicity, original-column scope, and physical source rows.**

### 6.5 Original rotation subfamily

Let


$$
a=\lfloor\log_2k\rfloor,\qquad L=2^{a-1}.
$$


On


$$
\frac98\,2^a<k<\frac54\,2^a,
$$


one has


$$
2L\le d,\qquad
\frac L4-1<\rho=d-2L<\frac L2-1.
$$


The parent’s $m=L/8$ choice satisfies the root condition and, at every original size, gives $q=L/4+1\le d/8$.

The sharper $q_\star$ statement also passes. The first mixed inequality gives


$$
q_\star<d/5,\qquad q_\star=d/5-O(\log d),
$$


and


$$
\rho+q_\star-1
<
\rho+\frac{2L+\rho}{5}-1<L.
$$


Thus the root criterion applies through that odd rank.

The interval contains infinitely many original indices because


$$
18\log_2 9+32u\log_2 9
$$


is an irrational rotation. Irrationality of $\log_2 9$ follows from unique prime factorization. Every tail of an irrational rotation is dense, so the interval is hit infinitely often.

No binary-distribution claim is used.

---

## 7. Independent audit of the multiple-return quarter window

### 7.1 Full finite Newton payment

Consider $a$ Cauchy columns, $t$ weighted return columns


$$
W_r(i)=\eta_r^{(d+i)},
$$


and $v$ free integer columns, with $q=a+t+v$.

After the exact row clearing in (5.1), the first $a$ columns are


$$
\binom i0,\ldots,\binom i{a-1}.
$$


The other columns are multiplied by $Q_I(i)$.

For every relevant $j$,


$$
2^jj!\mid\Delta^jQ_I(i).
$$


Indeed, $Q_I(i)$ is an integer polynomial in $2i$; a term $(2i)^b$ with $b\ge j$ contributes a multiple of $2^bj!$, while lower-degree terms vanish.

The exact return jet is


$$
\Delta^jW_r(i)
=2^j(r+1)_j\eta_{r+j}^{(d+i)}.
$$


Since $j!\mid(r+1)_j$, it also has divisor $2^jj!$.

The finite product rule gives


$$
\Delta^j(Q_IW_r)(i)
=\sum_{b=0}^j\binom jb
\Delta^bQ_I(i)\,
\Delta^{j-b}W_r(i+b).
$$


Every summand is divisible by $2^jj!$, because


$$
\binom jb\,b!(j-b)!=j!.
$$



Now use finite Newton expansion through $\max M$. The first $a$ polynomial columns force the Newton orders $0,\ldots,a-1$. Every remaining order is at least $a$. In the remaining determinant, expansion in the $t$ weighted columns selects $t$ distinct orders. The divisibility chain


$$
2^jj!\mid 2^{j+1}(j+1)!
$$


therefore pays the full product


$$
\prod_{j=a}^{a+t-1}2^jj!.
$$



After reinstating the exact Cauchy prefactor, this proves


$$
\boxed{
v_2\det[R^{\rm C}[M,I],W_{\rm ret}[M],Z[M]]
\ge c_a+\sum_{j=a}^{a+t-1}\lambda_j,
\quad
\lambda_j=j+v_2(j!).
}
\tag{7.1}
$$



This proof covers $a=0$, $t=0$, and arbitrary free integer columns. All Newton expansions are finite. If $i+j\le\max M\le d+1$, then the largest return index is at most


$$
d+(d+1)+(d-1)=3d,
$$


whose successor moment is $3d+1$, the original terminal.

**Verdict: PASS.**

### 7.2 Every $h/v$ correction term without the atom in $W$

Use


$$
p=q-h,\qquad a=p-v.
$$


If the atom is not among the $h$ bottom-correction columns, all those columns are weighted returns. The termwise payment is


$$
hL_d+v(\alpha-2)+c_a+2E_p+B_p
+\sum_{j=a}^{a+h-1}\lambda_j.
\tag{7.2}
$$



The exact marginal bounds imply


$$
\Theta_q-\Theta_p
\le h(10p+5h+5+3m_d),
$$


and


$$
c_p-c_a\le4pv.
$$


Since $a+h-1<q\le d$,


$$
\sum_{j=a}^{a+h-1}\lambda_j
\ge h(2a+h-1-m_d).
$$


Subtracting $\Theta_q$ from (7.2) gives


$$
\boxed{
h(L_d-8q+4h-6-4m_d)
+v(\alpha-2-4q+2h).
}
\tag{7.3}
$$



The algebra of this subtraction is correct; in particular, the $2hv$ term is not lost.

### 7.3 Atom in $W$, including $p=0$

If the atom is among the bottom corrections, $h\ge1$. Its scalar $2^{M_d}$ is retained. The remaining $h-1$ weighted columns receive the Newton payment; the atom $c_{\rm bot}/2$ is only a free integer column.

All $p$ top sources are now returns. Their extra payment is


$$
e_p=
\begin{cases}
v_2((d+1)_{p-1}),&p\ge1,\\
0,&p=0.
\end{cases}
$$


Thus the difference from (7.2) is


$$
M_d+e_p-\lambda_{a+h-1}.
$$



The bounds


$$
M_d\ge d-m_d+1,\qquad
e_p\ge p-m_d-2
$$


hold also at $p=0$, with the displayed definition $e_0=0$. Since


$$
a+h-1=q-v-1,
$$


the extra payment is at least


$$
\boxed{
d+p-2q+2v+1-2m_d
\ge d-2q+1-2m_d.
}
\tag{7.4}
$$



No factorial-jet divisor for the atom is assumed. The all-bottom case $p=a=0$ is included.

**Verdict: PASS.**

### 7.4 Three strict inequalities and the quarter rank

Assume


$$
\boxed{
L_d>8q+4m_d+6,\quad
\alpha-2>4q,\quad
d-2q+1-2m_d>0.
}
\tag{7.5}
$$


Then (7.3) is positive whenever $h+v>0$, and the atom case has the additional positive payment (7.4). Every correction term therefore has depth at least $\Theta_q+1$.

Hence


$$
\boxed{
\det\mathcal C_S[M]
\equiv
\det(R^{\rm C}N_dA_S)[M]
\pmod{2^{\Theta_q+1}}.
}
\tag{7.6}
$$



For the original large $d$, the first inequality is the active endpoint. Writing


$$
X_d=\frac{2d-s_2(d)-4m_d-18}{8},
$$


the largest admissible odd $q$ is the largest odd integer strictly below $X_d$; the other two conditions then have linear slack. In particular,


$$
X_d-2\le q_{\rm quarter}<X_d,
$$


so


$$
\boxed{q_{\rm quarter}=d/4-O(\log d).}
$$



All three strict inequalities remain part of the theorem.

### 7.5 Every intervening source rank on the narrower original subfamily

Restrict the same original indices to


$$
\frac98\,2^a<k<\frac76\,2^a,
\qquad L=2^{a-1}.
$$


Then


$$
\frac L4-1<\rho=d-2L<\frac L3-1.
$$


For every odd $q\le q_{\rm quarter}$,


$$
\rho+q-1
<
\rho+\frac d4-1
=\frac L2+\frac{5\rho}{4}-1<L.
$$


The rectangular theorem therefore gives full rank for every even contact prefix through $q_{\rm quarter}-1$.

For even $q$, the source test consists of $q-2$ ordinary rows and


$$
U_{q-2}+U_{q-1}.
$$


The first $q$ contact rows are independent, so this test has rank $q-1$.

Let $\mathcal R_q$ denote the row space of the relevant atom-cofactor test. Then


$$
\mathcal R_q\subset\mathcal R_{q+1}.
$$


At an odd-to-even step, the new row is a sum of the next two independent rows. At an even-to-odd step, that sum lies in the two ordinary rows replacing it.

A set of original coordinate columns giving an invertible evaluation on $\mathcal R_q$ remains independent on $\mathcal R_{q+1}$. The coordinate functionals span $\mathcal R_{q+1}^*$, so one additional original column extends the set. This is a basis-extension proof, not an assumed execution of a growing selection algorithm.

Starting from the established original columns


$$
1,0,5,4,
$$


one obtains a nested original-column flag at every


$$
5\le q\le q_{\rm quarter}.
$$



Combining source attainment with (5.3) and (7.6), the original first $q$ residual rows


$$
i=0,\ldots,q-1
$$


attain


$$
\boxed{\Theta_q(d)=c_q+2E_q+B_q(d).}
$$


Their original physical row labels are $d,\ldots,d+q-1$. The actual odd cofactor quotient remains


$$
\mu_{q,k}=\det\Pi_{q,k}/2^{\Theta_q},
$$


and is not assigned the integer value $1$.

The narrower interval is again hit infinitely often by the same irrational rotation.

**Verdict: PASS at every intervening even and odd size on the stated infinite original subfamily.**

---

## 8. Audit of A2’s first direct correction layer

Let


$$
\mathcal C^{[5]}=[x,z^{(1)},z^{(0)},z^{(5)},z^{(4)}],
$$


and retain the actual complete pivot $\Pi_{5,k}$. Define


$$
M_{5,k}=\frac{V_{5,k}\operatorname{adj}(\Pi_{5,k})}{2^{72}},
\qquad
\mathcal E_5=[-M_{5,k}\mid\mu_{5,k}I].
$$


The established cofactor theorem makes $M_{5,k}$ integral, and


$$
\mathcal E_5\mathcal C^{[5]}=0.
$$


The actual residual pencil is


$$
\mathcal P_k^{[5]}(s)
=\frac12\mathcal E_5\mathcal Q_{k,\rm remaining}(s).
$$



The interpolation coefficient sum is $1\pmod2$. Since $R$ is row-constant modulo $2$, and every column of $\mathcal W_k$ is row-constant modulo $2$, the matrices


$$
R_5=\frac12\mathcal E_5R,\qquad
W_5=\frac12\mathcal E_5\mathcal W_k
$$


are integral. Therefore the all-depth identity


$$
\mathcal P_k^{[5]}
=R_5N_d\mathcal A_{\rm remaining}
+2^{L_d}\gamma_kW_{5,\rm remaining}
$$


is valid with both complete borders.

For a return $r$,


$$
W_{5,r}(i)
=
\frac{\det[\mathcal C^{[5]},\eta_r^{\rm bot}]
[\{0,1,2,3,4,i\}]}{2^{73}}.
$$


The established source and factorial-adjugate payments are $12$ and $30$. The one-return mixed payment is


$$
H_5=c_5+5+v_2(5!)=38.
$$


Thus the leading determinant depth is $80$, yielding


$$
\boxed{
2^7\mid W_{5,r}(i),\qquad
2^{-7}W_{5,r}(i)
\equiv\binom i5S_5(r)\pmod2,
}
$$


where


$$
S_5(r)=
\begin{cases}
\operatorname{Tr}(\omega^{r+1}),&r\mathbin{\&}4=0,\\
\operatorname{Tr}(\omega^{r+2}),&r\mathbin{\&}4\ne0.
\end{cases}
$$


The unique minimal $N_d$-minor supplies the residue; every other pair costs at least one further binary digit. Complete-column and factorial corrections are above this precision because $L_d\ge100$ on the original domain.

At $i=5,r=3$, the residue is $1$. Hence the direct summand has exact depth $L_d+7$.

**Verdict: PASS.** The report correctly does not identify this summand’s depth with the depth of the whole residual entry.

---

## 9. New theorem: the complete first mixed perturbation, including both borders

The previous section evaluates the direct $W_5$ term. It does not by itself evaluate the first mixed perturbation of the complete residual pencil, because $R_5$ depends on the corrected pivot. The following result pays that feedback.

### 9.1 A precise reference, not a replacement pencil

For every original column label $a$, let $A_a$ be its actual top source, including


$$
A_{\mathfrak b_h}=\Lambda_k(\mathcal A_d\psi_h)_{\rm top}.
$$


Define the pure-Cauchy reference column


$$
B_a=R^{\rm C}N_dA_a.
$$


Let


$$
B_S=[B_x,B_{z^{(1)}},B_{z^{(0)}},B_{z^{(5)}},B_{z^{(4)}}].
$$



For $5\le i\le d+1$, define


$$
\boxed{
\mathcal P^{[5],{\rm C}}_{k,a}(i)
=
\frac{\det[B_S,B_a][\{0,1,2,3,4,i\}]}{2^{73}}.
}
\tag{9.1}
$$


This is the exact cofactor normalization used by the actual residual pencil. In particular,


$$
\mathcal P^{[5]}_{k,a}(i)
=
\frac{\det[\mathcal C^{[5]},\mathcal Q_{k,a}]
[\{0,1,2,3,4,i\}]}{2^{73}}.
\tag{9.2}
$$



The reference entries are integral. For return columns this follows from the pure source/Cauchy payments at size $6$; for the borders it also follows from the stronger entrywise source bounds proved next.

The reference is used only to measure a difference. It does not replace $\mathcal P_k^{[5]}$, its actual odd pivot quotient, its coefficient gcd, or its primitive error.

### 9.2 A new paid border-source lemma

Define


$$
B_h^{\rm top}=\Lambda_k(\mathcal A_d\psi_h)_{\rm top}.
$$


Then, on the original domain,


$$
\boxed{
2^d\mid N_dB_1^{\rm top},\qquad
2^{d+1}\mid N_dB_0^{\rm top}
}
\tag{9.3}
$$


entrywise.

#### Proof for the linear border

For $w_n=(-1)^n$,


$$
\Delta^jw_n=(-2)^jw_n.
$$


In the product rule for $\Delta^d(P_dw)$, every term has a factor $2^h$ from $\Delta^hP_d$ and $2^{d-h}$ from the $w$-jet. Hence


$$
2^d\mid \Lambda_k\mathcal A_dw.
$$


Both diagonal factors $\widehat D_f$ and $\operatorname{adj}(K_d)$ are integer matrices, proving the first claim.

#### Proof for the constant border

Write


$$
r=-f+4\rho.
$$



First, every entry of $\mathcal A_df$ is divisible by $(2n)!$ in top row $n$, because it is an integer combination of


$$
P_d(n+h)(2(n+h))!,\qquad h\ge0.
$$


Consequently,


$$
\widehat D_f\,\Lambda_k\mathcal A_df
$$


is divisible by the full integer $h_d$. Thus $N_d\Lambda_k\mathcal A_df$ is divisible by $2^\beta$.

For the rational part, put $g_n=(2n+1)^{-1}$. The recurrence is


$$
(\Delta+2)\rho=g.
$$


The exact reciprocal jets are


$$
\Delta^tg_n
=\frac{(-2)^tt!}{\prod_{a=0}^t(2n+2a+1)}.
$$


Induction using


$$
\Delta^t\rho=\Delta^{t-1}g-2\Delta^{t-1}\rho
$$


gives


$$
v_2(\Delta^t\rho_n)\ge t-1\qquad(t\ge1).
$$


All denominators are odd and are cleared by the actual $\Lambda_k$ in the relevant finite range.

In the product rule for $\Delta^d(P_d\,4\rho)$, a term with $h<d$ has depth at least


$$
h+(d-h-1)+2=d+1.
$$


The $h=d$ term has depth at least $d+2$. Therefore


$$
2^{d+1}\mid\Lambda_k\mathcal A_d(4\rho).
$$



Finally,


$$
\beta=2d-s_2(d)-5\ge d+1
$$


at every original index. Combining the factorial and rational parts proves the second claim. ∎

The factorial term of $r$ was essential in this proof; it was not omitted.

### 9.3 Complete border differences are above the first mixed layer

Every product reference border and every factorial-forcing version of it is divisible by the corresponding power in (9.3), since $R^{\rm C}$ and $V$ are integer matrices.

A correction in one of the five selected common columns therefore leaves at least $2^d$, respectively $2^{d+1}$, from the border column. A direct bottom-border correction has the full additional factor $2^\alpha$. Moreover, on bottom rows $m\ge d$,


$$
2^2\mid\Lambda_kr_m.
$$



It follows termwise from the exact six-column determinant expansion that


$$
\boxed{
v_2\!\left(
\mathcal P^{[5]}_{k,\mathfrak b_1}
-\mathcal P^{[5],{\rm C}}_{k,\mathfrak b_1}
\right)
\ge L_d+d-73,
}
\tag{9.4}
$$


and


$$
\boxed{
v_2\!\left(
\mathcal P^{[5]}_{k,\mathfrak b_0}
-\mathcal P^{[5],{\rm C}}_{k,\mathfrak b_0}
\right)
\ge L_d+d+1-73.
}
\tag{9.5}
$$


These bounds include the complete constant border $-f+4\rho$, the complete linear border $w$, and their bottom corrections.

In particular, both differences vanish modulo $2^{L_d+8}$.

### 9.4 Evaluation of all return-column first variations

Let


$$
R_0=(1,0,5,4)
$$


be the four selected return orders, and let $r$ be any actual remaining return.

Expand the six-column determinant in (9.2) around its pure-Cauchy term. To determine the difference modulo


$$
2^{L_d+81},
$$


before division by $2^{73}$, the following terms are invisible:

- two or more bottom corrections, whose scalar depth is at least $2L_d$;
- the atom bottom correction, with depth at least $L_d+M_d$;
- one bottom correction and a factorial-forcing correction;
- two or more factorial-forcing corrections.

A single factorial-forcing correction with no bottom correction has at least


$$
(\alpha-2)+c_5+2E_6+B_6
\ge (L_d+10)+72=L_d+82.
$$


Thus it is also invisible.

These inequalities hold with large slack at every original index. The only surviving class consists of **one weighted-return bottom correction and five pure product columns**.

For each such term:

- the mixed Cauchy payment is $H_5=38$;
- the $N_d$-minor payment is $30$;
- the five-source payment is $12$.

The total is $80$. Only $I=J=T_5$ can contribute to its normalized parity.

The resulting source cofactor sum is the determinant of the five contact rows


$$
U_0,\ U_1,\ U_2,\ U_3,\ S_5
$$


on the return columns


$$
(1,0,5,4,r).
$$


The already established source-five theorem gives a unit evaluation of the first four rows on $R_0$. No fixed cofactor calculation is repeated here.

The new functional comparison needed for this variation is


$$
(S_5(s))_{s\in R_0}
=(U_{0,s})_{s\in R_0}
=(1,1,1,0),
$$


which follows directly from the evaluated formulas. Adding $U_0$ to the last row therefore makes its first four entries zero. The remaining determinant is


$$
S_5(r)+U_{0,r}.
$$


The audited bitwise law gives


$$
U_{0,r}
=\eta_{r+2d+(r\mathbin{\&}d)}.
$$



Define the fully evaluated binary scalar


$$
\boxed{
\kappa_d(r)
=S_5(r)+\eta_{r+2d+(r\mathbin{\&}d)}.
}
\tag{9.6}
$$


This is not a named unevaluated cofactor sum.

Since


$$
\frac{V(\{0,1,2,3,4,i\})}{\Phi_6}=\binom i5,
$$


we obtain the new congruence


$$
\boxed{
\mathcal P^{[5]}_{k,r}(i)
-\mathcal P^{[5],{\rm C}}_{k,r}(i)
\equiv
2^{L_d+7}\gamma_k\binom i5\kappa_d(r)
\pmod{2^{L_d+8}}.
}
\tag{9.7}
$$



This expansion includes the corrections in the selected pivot columns. It is therefore stronger than the direct-$W_5$ formula.

### 9.5 A nonzero whole first mixed layer

Because $d$ has its lowest four binary digits zero,


$$
2\mathbin{\&}d=3\mathbin{\&}d=0.
$$


The evaluated contact parities give


$$
S_5(2)=0,\quad U_{0,2}=1,
\qquad
S_5(3)=1,\quad U_{0,3}=0.
$$


Hence


$$
\boxed{\kappa_d(2)=\kappa_d(3)=1.}
$$


At the first remaining residual row $i=5$,


$$
\binom55=1.
$$


Therefore


$$
\boxed{
v_2\!\left(
\mathcal P^{[5]}_{k,2}(5)
-\mathcal P^{[5],{\rm C}}_{k,2}(5)
\right)
=
v_2\!\left(
\mathcal P^{[5]}_{k,3}(5)
-\mathcal P^{[5],{\rm C}}_{k,3}(5)
\right)
=L_d+7.
}
\tag{9.8}
$$



Combining (9.4)–(9.8), the normalized difference of the complete residual pencils has rank exactly one over $\mathbb F_2$. Its row factor is


$$
\left(\binom i5\right)_{i=5}^{d+1},
$$


its return-column factor is $(\kappa_d(r))$, and both affine border factors are zero.

### 9.6 A legitimate division-free isolation

Choose the lift $\kappa_d(r)\in\{0,1\}$. In both the actual residual pencil and its reference, perform the integer column operations


$$
\text{column }r\longleftarrow
\text{column }r-\kappa_d(r)\,\text{column }2,
\qquad r\ne2.
$$


These are unimodular operations on the actual remaining columns. They leave both borders unchanged and preserve both coefficient determinants.

After them, every return-column difference except column $2$ is divisible by $2^{L_d+8}$. Column $2$ retains an entry of exact difference depth $L_d+7$ at row $i=5$.

This is an actual integer operation, unlike the normalized parity convolution used in the source-rank argument. No division and no new odd pivot assumption is involved.

---

## 10. What has not been proved

### 10.1 The quarter endpoint is not a proved correction-transition rank

The inequalities defining $q_{\rm quarter}$ are sufficient conditions for the disappearance of mixed terms at depth $\Theta_q+1$. Their failure does not prove that a correction begins contributing immediately at the next rank.

Thus the report proves:

- complete attaining cofactors through the stated quarter window;
- an actual, nonzero first mixed perturbation layer in the paid five-column residual pencil.

It does not identify the first rank beyond that window where a growing complete cofactor changes its leading residue.

### 10.2 The old division-by-two algorithm is not established at all ranks

A nested family of unit normalized minors does not, by itself, prove that the old row-constant division-by-two procedure extends unchanged. A growing elimination would still have to retain:

- the actual complete Cramer numerators;
- the actual odd cofactor quotients;
- every row and column payment;
- both full affine borders.

The quarter-window minor theorem proves none of those additional algorithmic identities beyond their established scope.

### 10.3 Rank-forced mixed terms remain unavoidable

The pure product has rank at most $d$:


$$
\operatorname{rank}(RN_d\mathcal A_k)\le d.
$$


Therefore:

- a complete $(d+1)$-common-column minor must use a bottom correction;
- a complete $(d+2)$-column coefficient determinant must use at least two bottom-correction columns in its rank expansion.

The local first-layer theorem does not supply those final missing directions.

### 10.4 A concrete next local lemma

Let


$$
D_k=\mathcal P_k^{[5]}-\mathcal P_k^{[5],{\rm C}}.
$$


The new theorem proves


$$
v_2(\operatorname{content}_1D_k)=L_d+7
$$


and, because its normalized parity has rank one,


$$
v_2(\operatorname{content}_2D_k)\ge2L_d+15.
$$



A concrete next test is the original two-row, two-return minor


$$
D_k[\{5,6\},\{2,3\}].
$$


Its normalized leading coefficient is


$$
\frac{\det D_k[\{5,6\},\{2,3\}]}{2^{2L_d+15}}
\equiv
\frac{D_{k,3}(6)-D_{k,2}(6)}{2^{L_d+8}}
\pmod2.
$$


Thus an attaining second mixed direction reduces to one explicitly specified next-layer residue.

Determining that residue requires more than the currently established parity kernel: it requires the relevant contact-source and factorial-adjugate data one binary digit deeper, together with the actual odd Cauchy denominators. The two borders remain rigorously above this local difference precision by (9.4)–(9.5), but their complete product parts must still be carried.

This is a precise follow-on lemma, not an assumed second mixed pivot.

---

## 11. Global arithmetic and analytic status

The unresolved binary target remains


$$
\boxed{
\nu_k^{[5]}
\le \frac{15}{4}k^2-64+O(k\log k),
\qquad k=9^{18+32u}.
}
$$


No audited or new theorem above proves it.

The exact normalizations remain


$$
\frac{|P_{1,k}^{[5]}|}{g_k^{[5]}}
=\frac{|H_{1,k}|}{G_k}=q_k,
$$


and


$$
\boxed{
\frac{|P_{0,k}^{[5]}+P_{1,k}^{[5]}(e+\pi)|}{g_k^{[5]}}
=
\frac{|H_k(e+\pi)|}{G_k}
=\ell_k>0.
}
$$


The reference pencil and its mixed difference are not substituted into these formulas.

The established ternary content statements retain only their proved scope. The separate $p\ge5$ descents, large-prime exclusions, higher ternary obligations, and other producer obligations receive no new status from this report.

The closed same-$H$ analytic estimate is reused:


$$
\log|H_k(e+\pi)|
\ge
4k^2\log k+
\left(15\log2-\frac92\log3+\frac4{85}\right)k^2
+o(k^2).
$$


Any primitive-error divergence or producer-retirement conclusion still requires the independent arithmetic controls. A conclusion obtained only on the rotation subfamily would not retire every other original index. In any event, producer retirement is not an irrationality or rationality proof for $e+\pi$.

---

## 12. Proof-status ledger and computation scope

| Statement | Audit status |
|---|---|
| Established all-order F4 entry law and full weighted divisors | Reused at their stated scope |
| A2 bitwise law for $\mathcal J$ and exact rank $C_d(q)$ | **PASS: independently derived** |
| A2 submask jet flags and original lifting subfamilies | **PASS: jet scope only** |
| Full rising source divisor and failure of old $b_q$ for $q\ge18$ | **PASS** |
| Odd atom minimum and even tied cofactor sum | **PASS** |
| Exact mixed Cauchy identity, including odd denominators | **PASS** |
| A2 complete mixed-compound comparison | **PASS** |
| Parent rectangular root-rank theorem | **PASS: independently proved** |
| Parent odd physical flag and fifth-window rotation refinement | **PASS** |
| Multiple-return payment with free columns | **PASS** |
| All $h/v$ correction terms and atom case, including $p=0$ | **PASS** |
| Three strict quarter-window conditions | **PASS** |
| Every-size original physical flag on the narrower rotation subfamily | **PASS** |
| Complete cofactor depth $\Theta_q$ throughout that flag | **PASS** |
| A2 direct $L_d+7$ weighted-return correction layer | **PASS at its stated summand scope** |
| Complete first mixed residual perturbation, including pivot feedback | **New proved theorem** |
| Both complete border-difference bounds (9.4)–(9.5) | **New proved theorem** |
| Rank-one first mixed layer and original-column isolation | **New proved theorem** |
| Turn 21’s new all-order similarity/rank theorem | Separate different audit still pending; not used here |
| Growing all-rank elimination and joint terminal coefficient upper | **Open** |
| All-prime final gcd control and $e+\pi$ decision | **Open** |

No tools have been used. No original-sized array, solve, growing selection execution, old fixed cofactor computation, or closed $8192$-comparison receipt has been rerun.

No bounded exact arithmetic calculation is needed for the proofs in this report, so none is proposed. The next-layer residue in Section 10.4 is a mathematical proof obligation; an original-sized solve is not an acceptable substitute for deriving its required finite-depth structure.

---

## Final conclusion

The rectangular source-rank and multiple-return quarter-window arguments pass this independent audit. Their combined unconditional result is an attaining nested flag of **original** common columns, at every size through


$$
q_{\rm quarter}=d/4-O(\log d),
$$


on the explicit infinite original rotation subfamily


$$
\frac98\,2^{\lfloor\log_2k\rfloor}
<k<
\frac76\,2^{\lfloor\log_2k\rfloor}.
$$


The minimizing consecutive top rows attain $B_q(d)$, and the complete first $q$ residual physical rows attain


$$
\Theta_q(d)=c_q+2E_q+B_q(d).
$$



The new follow-on result evaluates the complete first mixed perturbation of the already paid five-column residual pencil:


$$
\boxed{
2^{-(L_d+7)}
\bigl(\mathcal P_k^{[5]}-\mathcal P_k^{[5],{\rm C}}\bigr)
\equiv
\left(\binom i5\right)_i
\left(\kappa_d(r)\right)_r
\pmod2,
}
$$


with


$$
\kappa_d(r)=S_5(r)+\eta_{r+2d+(r\mathbin{\&}d)},
$$


and with zero entries in both complete affine coefficient-border positions. The actual remaining returns $2$ and $3$ certify nonzero depth $L_d+7$ at the first remaining physical row.

The exact global bottleneck remains the genuinely mixed growing elimination after the certified window, the rank-forced final correction directions, and the **joint** depth of the two complete terminal coefficients. Other-prime payment remains independent. The actual all-prime gcd, primitive denominator, and nonzero whole error are unchanged at the same original indices.

No unconditional rationality or irrationality conclusion for $e+\pi$ has been obtained.
