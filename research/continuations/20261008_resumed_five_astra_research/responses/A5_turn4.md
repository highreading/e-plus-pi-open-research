> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the two-square arithmetic, and a uniform obstruction on the original indices

## Abstract and conclusions

The attached work does **not** decide whether $e+\pi$ is rational or irrational. This report does, however, resolve an important question about the specified two-square producer.

The principal conclusions are:

1. **A2’s exact raw-content formula is correct.** Its proof accounts for exceptional cancellation between the two squares. The auxiliary divisibility
   

$$
c_N\mid 4(N-2)!
$$


   is correct for $N\ge 3$, and its proof evaluates the relevant moment gcd rather than leaving it as an unspecified sum.

2. **A2’s regular-factorial-prime criterion is correct at its stated hypotheses.** In particular, the correction
   

$$
-4\frac{T_N}{p}[t^{p-1}]
       \frac{\Phi_N^2-\Delta_N^2}{1+t^2}
$$


   is essential. The second-square endpoint alone does not determine the final gcd.

3. **The coordinator’s last-prime-block calculation and final-denominator formula are correct:**
   

$$
\boxed{
   v_p(q_N)=v_p(T_N)+v_p(N-1)
   }
$$


   for every $N\ge4$ and every odd prime $p\mid N-1$. This is a statement about the **actual primitive denominator**, after the actual polynomial content, least affine clearer, and final all-prime gcd.

4. **The root-exponential ordinary-error lower bound is correct.** The real Laguerre coefficient norm, entire growth estimate, simultaneous Taylor-tail estimates on $[0,1]$ and at $i$, and complex Legendre evaluation estimate all have valid proofs. Consequently, for each fixed odd prime $p$,
   

$$
q_N(e+\pi)-p_N\longrightarrow+\infty
   \qquad
   (N\to\infty,\ N\equiv1\pmod p).
$$



5. **There is a stronger, uniform conclusion on the retained original domain.** Every original index
   

$$
N=9^{18+32u},\qquad u\ge0,
$$


   satisfies $N\equiv1\pmod5$. Thus the fixed-prime theorem is not merely a bad subsequence result there. It covers **every original index**. Writing
   

$$
r=\sqrt N=3^{18+32u},
$$


   I obtain the explicit bound
   

$$
\boxed{
   q_N(e+\pi)-p_N
   >
   2^{\,r^2-100r-12}>1
   }
   \tag{A}
$$


   at every original index. In particular, the whole primitive error diverges on the entire retained original sequence.

6. **A new final-gcd theorem advances another moving-prime residue class.** If
   

$$
p\ge5,\qquad p\ne71,\qquad N=kp+2,\qquad k\ge1,
$$


   then
   

$$
\boxed{
   v_p(\lambda_N)=v_p(\mathfrak G_N)=0,\qquad
   v_p(q_N)=v_p(T_N)=v_p((2N-4)!).
   }
   \tag{B}
$$


   The exceptional constant $71$ is obtained from the complete second-square endpoint, not guessed from finite data. A further prime-power refinement at $71$ is given below.

These results exclude this particular two-square ansatz as a source of vanishing primitive errors at the required original indices. They do **not** exclude its extension at every other integer $N$, every other positive polynomial in the accepted source plane, or the distinct compact, binary, and Laguerre constructions.

---

## 1. Scope, boundaries, and objects that are not being changed

### 1.1 The retained original domain

The original indices remain


$$
\boxed{N=b(u)=9^{18+32u},\qquad u\ge0.}
\tag{1.1}
$$



The new two-square family is defined for all integers $N\ge2$, but an all-$N$ theorem is not automatically an original-domain theorem until its hypotheses have been checked in (1.1).

Its exact finite boundaries remain:

- Laguerre basis indices $0,\ldots,N$;
- minimizing-polynomial degree at most $N$;
- final polynomial degree exactly $2N$;
- exponential moments and factorial endpoints only through $2N$;
- arctangent quotient degree $2N-2$;
- arctangent integration denominators only through $2N-1$.

The unweighted diagnostic $\int_0^1P_N$ may involve denominators through $2N+1$. This introduces neither a successor exponential moment nor an additional factorial endpoint.

### 1.2 The old binary producer is not silently altered

Its separate data remain


$$
b=9^{18+32u},\qquad n=4002b,
$$


with contact range $0,\ldots,b-1$, reconstruction range $0,\ldots,b$, and physical terminal


$$
z_b=0.
$$



Its complete corrected columns remain


$$
x=\frac12RA^{-1}f,\qquad
y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},
\qquad x=2^ax_0.
$$


The complete return remains


$$
S=\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f,
$$


and the retained paid valuation is


$$
v_2\!\left(\frac{S}{2^{a+1}}\right)\ge\chi-a,
\qquad
\chi=v_2\binom{n+b-1}{b-1}.
$$



No theorem proved below evaluates that producer’s corrected-column contents or final gcd.

Likewise, the compact matrix retains


$$
0\le m<2k,\qquad 0\le j<k,\qquad m+j\le3k-2,
$$


with


$$
c_n=a_{2n}-(-1)^n,\qquad
r_n=-(2n)!+4\rho_n,\qquad
\rho_0=0,\quad
\rho_{n+1}+\rho_n=\frac1{2n+1},
$$


and


$$
H_k(s)=\det[C\mid\Lambda_k\mathcal R+s\Lambda_kwv^T],
\qquad
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5).
$$


Its final content is not determined here.

The separate Laguerre-matrix obstruction also retains its separate index domain and hypotheses. Its denominator divisibility is not transferred to the present $q_N$.

### 1.3 Reuse of closed work

The closed $N=8$ normalization is reused at its finite scope, including


$$
h_8=2^{40}3^2,\qquad
\lambda_8=1365,\qquad
\mathfrak G_8=1.
$$


The established distinction


$$
11\nmid\lambda_8,\quad 11\mid q_8,
\qquad
13\mid\lambda_8
$$


is also retained. No duplicate $N=8$ expansion or all-81-pair computation is proposed.

The literature ingredients used below are classical Laguerre orthogonality and its finite expansion, the Carlitz congruence at prime modulus, Legendre evaluation kernels, and Cauchy’s coefficient estimate. Their particular applications are derived below. No exhaustive novelty claim is made.

---

## 2. The actual source-normalized producer and its paid primitive pair

This section fixes the objects to which every subsequent valuation applies.

### 2.1 Complete source identities

Set


$$
d\eta(t)=e^{t-1}\mathbf1_{(-\infty,1]}(t)\,dt.
$$


Its moments satisfy


$$
a_0=1,\qquad a_d=1-da_{d-1},
$$


and hence are integers. Integration by parts gives


$$
\int_0^1 e^tt^d\,dt=e\,a_d-(-1)^dd!.
\tag{2.1}
$$



For the arctangent channel, put


$$
\xi_d=\Re(i^d),\qquad \zeta_d=\Im(i^d),
$$


and


$$
\sigma_0=\sigma_1=0,\qquad
\sigma_d=\frac1{d-1}-\sigma_{d-2}.
$$


Then


$$
4\int_0^1\frac{t^d}{1+t^2}\,dt
=\pi\xi_d+2\log2\,\zeta_d+4\sigma_d.
\tag{2.2}
$$


Thus the odd-power $\log2$ source is present until the actual contact condition eliminates it.

If $P\in\mathbb Q[t]$ satisfies


$$
\int P\,d\eta=1,\qquad P(i)=1,
\tag{2.3}
$$


then $P(-i)=1$ and


$$
S_P=\frac{P-1}{1+t^2}\in\mathbb Q[t].
$$


Writing


$$
B(P)=\sum_d[t^d]P\,(-1)^dd!,
$$


the complete identity is


$$
\boxed{
\int_0^1P(t)\left(e^t+\frac4{1+t^2}\right)dt
=e+\pi-\left(B(P)-4\int_0^1S_P(t)\,dt\right).
}
\tag{2.4}
$$



Let


$$
w(t)=e^t+\frac4{1+t^2}.
$$


On $[0,1]$,


$$
3\le w(t)<7.
\tag{2.5}
$$



### 2.2 The minimizing polynomial

Let


$$
Q_j(t)=L_j(1-t),\qquad E_j(t)=N!Q_j(t),\qquad 0\le j\le N.
$$


The $Q_j$ are real and orthonormal in $L^2(\eta)$, while $E_j\in\mathbb Z[t]$.

Write


$$
E_j(i)=\alpha_j+i\beta_j,
$$


and define


$$
\mathsf U=\sum\alpha_j^2,\qquad
\mathsf V=\sum\alpha_j\beta_j,\qquad
\mathsf W=\sum\beta_j^2,
$$




$$
\Delta=\mathsf U\mathsf W-\mathsf V^2,\qquad B=(N!)^2.
$$


The two evaluation vectors are independent already at $j=0,1$, so $\Delta>0$.

Set


$$
\Phi(t)=
\sum_{j=0}^N(\mathsf W\alpha_j-\mathsf V\beta_j)E_j(t).
$$


Then


$$
\Phi(i)=\Delta,\qquad
\int\Phi^2\,d\eta=B\mathsf W\Delta.
$$


Consequently,


$$
f_N=\frac{\Phi}{\Delta},\qquad
\tau_N=\int f_N^2\,d\eta=\frac{B\mathsf W}{\Delta}.
\tag{2.6}
$$



This is the real minimum-norm polynomial of degree at most $N$ satisfying $f(i)=1$. The competitor


$$
\frac{5-t^2}{6}
$$


has squared norm


$$
\frac{25-10a_2+a_4}{36}=\frac23.
$$


Therefore


$$
\tau_N\le\frac23,\qquad
D:=\Delta-B\mathsf W>0.
\tag{2.7}
$$



The minimum also gives


$$
\int f_Nk\,d\eta=0
\quad
\text{when }\deg k\le N,\ k\in\mathbb R[t],\ k(i)=0.
\tag{2.8}
$$



### 2.3 The second square

Retain exactly


$$
g_N(t)=(1+t^2)(1-t)^{N-2}.
$$


With


$$
m=2N-4,\qquad
\mathcal R_4(x)=x^4+6x^3+19x^2+22x+12,
$$


its norm is


$$
T_N=\int g_N^2\,d\eta=m!\mathcal R_4(m).
\tag{2.9}
$$


Equivalently,


$$
T_N=(2N)!-4(2N-1)!+8(2N-2)!
       -8(2N-3)!+4(2N-4)!.
$$



The producer is


$$
\boxed{
P_N=f_N^2+\frac{1-\tau_N}{T_N}g_N^2.
}
\tag{2.10}
$$


It satisfies both conditions in (2.3), has degree exactly $2N$, and is strictly positive on $[0,1)$.

### 2.4 Actual contents, least clearers, and final gcd

The raw integer objects are


$$
\mathscr W_N=T_N\Phi^2+D\Delta g_N^2,\qquad
\mathscr Z_N=T_N\Delta^2.
$$


Let


$$
h_N=\operatorname{cont}(\mathscr W_N),
$$


and define


$$
W_N=\frac{\mathscr W_N}{h_N},\qquad
M_N=\frac{\mathscr Z_N}{h_N}.
\tag{2.11}
$$


Because $\mathscr W_N(i)=\mathscr Z_N$, one has $h_N\mid\mathscr Z_N$. The polynomial $W_N$ is primitive, so $M_N$ is the **least simultaneous coefficient clearer** of $P_N$.

Put


$$
S_N=\frac{W_N-M_N}{1+t^2}
=\sum_{j=0}^{2N-2}s_jt^j\in\mathbb Z[t],
$$


and retain the whole factorial endpoint


$$
B_{\mathrm{end},N}
=\sum_{d=0}^{2N}[t^d]W_N\,(-1)^dd!.
$$



The entrywise arctangent clearer is


$$
L_{\mathrm{ent},N}
=
\operatorname{lcm}_{0\le j\le2N-2}
\frac{j+1}{\gcd(j+1,4s_j)}.
$$


After the terms are summed, let


$$
J_{\mathrm{arc},N}
=\sum_j\frac{4s_jL_{\mathrm{ent},N}}{j+1},
$$




$$
d_{\mathrm{arc},N}
=\gcd(L_{\mathrm{ent},N},J_{\mathrm{arc},N}),\qquad
\lambda_N=\frac{L_{\mathrm{ent},N}}{d_{\mathrm{arc},N}}.
$$


Thus $\lambda_N$, not merely $L_{\mathrm{ent},N}$, is the least denominator of


$$
R_N:=B_{\mathrm{end},N}-4\int_0^1S_N.
$$


Set


$$
A_N=\lambda_NR_N\in\mathbb Z.
$$


Minimality gives


$$
\gcd(\lambda_N,A_N)=1.
\tag{2.12}
$$



The final all-prime gcd and primitive pair are


$$
\boxed{
\mathfrak G_N=\gcd(\lambda_NM_N,|A_N|)
             =\gcd(M_N,|A_N|),
}
\tag{2.13}
$$




$$
\boxed{
q_N=\frac{\lambda_NM_N}{\mathfrak G_N},\qquad
p_N=\frac{A_N}{\mathfrak G_N}.
}
\tag{2.14}
$$


In particular, $\lambda_N\mid q_N$.

Finally, the whole error is


$$
\boxed{
\ell_N:=q_N(e+\pi)-p_N
=q_N\int_0^1P_N(t)w(t)\,dt>0.
}
\tag{2.15}
$$


For


$$
J_N=\int_0^1P_N(t)\,dt,
$$


we have the exact comparison


$$
3q_NJ_N\le\ell_N\le7q_NJ_N.
\tag{2.16}
$$



No denominator used below is a substitute for this $q_N$.

---

## 3. Audit of A2’s exact raw-content theorem

Define


$$
d=\operatorname{cont}(\Phi),\qquad
\phi=\Phi/d,\qquad a=\phi(0),
$$


and


$$
c=\operatorname{cont}(\phi-ag_N).
$$



### 3.1 Exact content formula

Since $\phi(i)=\Delta/d\ne0$ whereas $g_N(i)=0$, the polynomial $\phi-ag_N$ is nonzero, so $c>0$.

Because $g_N(0)=1$ and $\phi$ is primitive,


$$
\gcd(a,c)=1.
\tag{3.1}
$$



Next,


$$
\operatorname{cont}(\phi+ag_N)=\gcd(2,c).
\tag{3.2}
$$


Indeed:

- an odd prime dividing $\phi+ag_N$ coefficientwise divides its constant coefficient $2a$, hence $a$, and then every coefficient of $\phi$, a contradiction;
- divisibility of the content by $4$ would similarly force $a$ and all coefficients of $\phi$ to be even;
- coefficientwise divisibility by $2$ is equivalent for $\phi+ag_N$ and $\phi-ag_N$.

Gauss’s lemma therefore gives


$$
\operatorname{cont}(\phi^2-a^2g_N^2)
=c\gcd(2,c).
\tag{3.3}
$$



Put


$$
A_0=T_Nd^2,\qquad B_0=D\Delta.
$$


The raw polynomial is


$$
\mathscr W_N=A_0\phi^2+B_0g_N^2.
$$


Its constant coefficient is $A_0a^2+B_0$. Subtracting this constant coefficient times $g_N^2$ leaves


$$
A_0(\phi^2-a^2g_N^2).
$$


Because $g_N^2(0)=1$, this operation preserves the gcd of the coefficient vector. Hence


$$
\boxed{
h_N=
\gcd\!\left(
T_Nd^2a^2+D\Delta,\,
T_Nd^2c\gcd(2,c)
\right).
}
\tag{3.4}
$$



This is an exact all-prime formula, not only a forced-content divisor.

### 3.2 The evaluated moment gcd

Let $n=N-2\ge1$. For $0\le j\le n$, use


$$
k_j(t)=(1+t^2)(1-t)^j.
$$


These have degree at most $N$ and vanish at $i$. By (2.8),


$$
\int\phi k_j\,d\eta=0.
$$


Writing


$$
\phi=ag_N+cR,\qquad R\in\mathbb Z[t],
$$


and using integrality of the $\eta$-moments, we obtain


$$
c\mid a\int g_Nk_j\,d\eta.
$$


Equation (3.1) then gives


$$
c\mid\int g_Nk_j\,d\eta.
$$



Under $y=1-t$,


$$
\int g_Nk_j\,d\eta
=(n+j)!\mathcal R_4(n+j).
\tag{3.5}
$$



The gcd of these moments is exactly


$$
\boxed{
\gcd_{0\le j\le n}(n+j)!\mathcal R_4(n+j)=4n!.
}
\tag{3.6}
$$



Here is the complete argument.

First,


$$
\mathcal R_4(x)
=x(x+1)(x+2)(x+3)+8(x+1)^2+4,
$$


so


$$
v_2(\mathcal R_4(x))=2
$$


for every nonnegative integer $x$. Thus the exact common $2$-part is the $2$-part of $4n!$.

For an odd prime $p\le2n+1$, choose $n+j$ to be one less than the first multiple of $p$ strictly exceeding $n$. This choice lies in $[n,2n]$: it is immediate if $p\le n+1$, while for $n+1<p\le2n+1$ the chosen value is $p-1$. There is no multiple of $p$ between $n$ and $n+j$, and


$$
\mathcal R_4(n+j)\equiv\mathcal R_4(-1)=4\pmod p.
$$


Hence no extra $p$-factor beyond $n!$ is common.

If $p>2n+1$ and $n\ge4$, all factorials in (3.6) are $p$-units. A common $p$-factor would make the monic quartic $\mathcal R_4$ vanish at the five distinct residues


$$
n,n+1,n+2,n+3,n+4,
$$


which is impossible. The cases $n=1,2,3$ are the stated small gcds $4,8,24$.

Therefore


$$
\boxed{c_N\mid4(N-2)!\qquad(N\ge3).}
\tag{3.7}
$$


Evaluation at $i$, and at $1$ when $N\ge3$, also gives


$$
c_N\mid\Delta/d,\qquad c_N\mid\phi_N(1).
$$



### 3.3 Necessary scope qualifications

For $N\ge3$ and an odd prime $p>N-2$, equation (3.7) implies $p\nmid c_N$. Equation (3.4) then yields


$$
\boxed{
v_p(h_N)=
\min\!\left(
v_p(T_N)+2v_p(d_N),\
v_p(D)+v_p(\Delta)
\right).
}
\tag{3.8}
$$



The restriction $N\ge3$ in (3.7) is real. At $N=2$,


$$
d=8,\quad \phi=5-t^2,\quad c=6,
$$


so $c\nmid4$. The exact content formula still holds:


$$
\Delta=48,\quad D=16,\quad T_2=12,\quad h_2=1536.
$$


The odd-prime valuation consequence can also be checked directly at this isolated endpoint.

For $p>N$, the source-only formula


$$
\boxed{
v_p(d_N)=\min(v_p(\mathsf W),v_p(\mathsf V))
}
\tag{3.9}
$$


is correct. To see this, use the monic integral basis


$$
H_j(t)=j!L_j(1-t).
$$


The $H_j$-coefficient of $\Phi$ is


$$
\left(\frac{N!}{j!}\right)^2
\left(\mathsf W\Re H_j(i)-\mathsf V\Im H_j(i)\right).
$$


All prefactors are $p$-units. The $j=0,1$ coefficients are


$$
(N!)^2\mathsf W,\qquad -(N!)^2\mathsf V,
$$


and the monic basis change is unimodular.

Equation (3.9) must not be used for $p\le N$. Nor does (3.8) by itself determine the final gcd $\mathfrak G_N$.

**Audit verdict:** A2’s exact content theorem is valid, with the foregoing endpoint and prime-range qualifications.

---

## 4. Audit of the complete second-square endpoint and the $\Psi$ criterion

### 4.1 Evaluating the second-square endpoint

Define


$$
C_0=1,\qquad C_r=rC_{r-1}+1,
$$


and


$$
H_3(x)=x^3+6x^2+18x+17.
$$



The complete factorial endpoint of $g_N^2$ is


$$
B_g=\sum_d[t^d]g_N^2\,(-1)^dd!.
$$


Since


$$
g_N(-x)^2=(1+x^2)^2(1+x)^m,
$$


expansion in powers of $1+x$ gives


$$
B_g=C_{m+4}-4C_{m+3}+8C_{m+2}-8C_{m+1}+4C_m.
$$


Repeated use of the recurrence gives


$$
\boxed{
B_g=\mathcal R_4(m)C_m+H_3(m).
}
\tag{4.1}
$$



The complete arctangent quotient integral is


$$
\begin{aligned}
\beta_g
&=\int_0^1(1+t^2)(1-t)^m\,dt\\
&=\frac1{m+1}
+\frac2{(m+1)(m+2)(m+3)}\\
&=\boxed{\frac{m^2+5m+8}{(m+1)(m+2)(m+3)}}.
\end{aligned}
\tag{4.2}
$$



Likewise,


$$
\boxed{
\int_0^1g_N^2
=
\frac1{m+1}
+\frac4{(m+1)(m+2)(m+3)}
+\frac{24}{(m+1)(m+2)(m+3)(m+4)(m+5)}.
}
\tag{4.3}
$$



Thus


$$
R_g=B_g-4\beta_g
\tag{4.4}
$$


is the complete second-square rational endpoint.

For the first square, define


$$
Q_\Phi=\frac{\Phi^2-\Delta^2}{1+t^2}\in\mathbb Z[t],
$$




$$
R_\Phi=
\sum_d[t^d]\Phi^2\,(-1)^dd!
-4\int_0^1Q_\Phi.
$$


Then the complete endpoint numerator before the final gcd is


$$
\boxed{
A_N=\frac{\lambda_N}{h_N}
\left(T_NR_\Phi+D\Delta R_g\right).
}
\tag{4.5}
$$


Both squares and both endpoint channels remain in this formula.

### 4.2 Regular interior factorial primes

Assume


$$
N<p\le2N-4,\qquad p\nmid D\Delta.
\tag{4.6}
$$


Then $p\mid T_N$, while $p\nmid h_N$. Reduction of the actual quotient gives


$$
S_N\equiv\frac{D\Delta}{h_N}(1+t^2)(1-t)^m\pmod p.
$$


Write $m=p+r$. The range in (4.6) gives


$$
0\le r\le p-6.
$$


Since


$$
(1-t)^m=(1-t^p)(1-t)^r\pmod p,
$$


the coefficient of $t^{p-1}$ in $(1+t^2)(1-t)^m$ vanishes.

Among the integration denominators $1,\ldots,2N-1$, the only multiple of $p$ is $p$. Hence


$$
v_p(\lambda_N)=0.
\tag{4.7}
$$



Now also assume


$$
p\nmid\mathcal R_4(m),
\tag{4.8}
$$


so $v_p(T_N)=1$. Set


$$
c_{\Phi,p}=[t^{p-1}]Q_\Phi.
$$


All $p$-integral terms in $T_NR_\Phi$ vanish modulo $p$, but the single arctangent pole contributes


$$
-4\frac{T_N}{p}c_{\Phi,p}.
$$


Therefore


$$
\boxed{
\Psi_{N,p}
=
D\Delta R_g-4\frac{T_N}{p}c_{\Phi,p}
}
\tag{4.9}
$$


is the correct complete residue, and


$$
\boxed{
v_p(q_N)=
\begin{cases}
1,&\Psi_{N,p}\not\equiv0\pmod p,\\
0,&\Psi_{N,p}\equiv0\pmod p.
\end{cases}
}
\tag{4.10}
$$



The correction in (4.9) cannot be dropped. Content information alone does not imply (4.10).

For a direct coefficient implementation,


$$
c_{\Phi,p}
=
\sum_{r=0}^{N-(p+1)/2}
(-1)^r[t^{p+1+2r}]\Phi^2.
\tag{4.11}
$$


This follows from monic division by $1+t^2$, starting at the highest degree. It computes the coefficient of the **complete** quotient.

A useful reduction is also available. If $m=p+r$, then


$$
C_m\equiv C_r\pmod p,\qquad
\frac{T_N}{p}\equiv-r!\mathcal R_4(r)\pmod p.
$$


Thus (4.9) can be evaluated without the large factorial $m!$, using the reduced endpoint at $r$ and the same complete $c_{\Phi,p}$.

**Audit verdict:** the criterion is correct. Its hypotheses exclude kernel primes $p\mid\Delta$, primes dividing $D$, and the higher-depth case $p\mid\mathcal R_4(m)$. It is not a criterion for arbitrary primes.

---

## 5. Audit of the last source-normalized prime block and final $q_N$

### 5.1 The polynomial congruence

To avoid a notation conflict, write


$$
\widehat H_j(x)=j!L_j(x).
$$


For $j=kp+a$, $0\le a<p$,


$$
\boxed{
\widehat H_j(x)\equiv(-x)^{kp}\widehat H_a(x)\pmod p.
}
\tag{5.1}
$$



A direct proof is sufficient. In the finite expansion


$$
\widehat H_j(x)=
\sum_{r=0}^j(-1)^r\binom jr\frac{j!}{r!}x^r,
$$


all terms with $r<kp$ contain the factor $kp$ in $j!/r!$. For $r=kp+b$, Lucas’s congruence and the factorial quotient give


$$
\binom{kp+a}{kp+b}\equiv\binom ab,\qquad
\frac{(kp+a)!}{(kp+b)!}\equiv\frac{a!}{b!}\pmod p.
$$


This proves (5.1), without division by $p$.

### 5.2 The actual $E_j=N!L_j(1-t)$ block

Let $p\le N$ be odd and write


$$
N=kp+a,\qquad 0\le a<p.
$$


Then


$$
E_j\equiv0\pmod p\qquad(j<kp),
$$


and


$$
\boxed{
E_{kp+r}(t)
\equiv
\frac{a!}{r!}R_p(t)\widehat H_r(1-t),
\qquad
R_p(t)=(t-1)^{kp},
\quad 0\le r\le a.
}
\tag{5.2}
$$



This is the last block of the **original source-normalized basis**. It is not an unscaled kernel at a replacement index.

Put


$$
\zeta=R_p(i)=x+iy.
$$


In the algebra $\mathbb F_p[i]=\mathbb F_p[X]/(X^2+1)$,


$$
\zeta\bar\zeta=2^{kp}\ne0.
$$


This proves invertibility even when $p\equiv1\pmod4$, where the algebra is split and is not a field.

If $K_a$ denotes the $2\times2$ evaluation Gram matrix of the partial block, multiplication by $\zeta$ gives


$$
K_N\equiv
\begin{pmatrix}x&-y\\y&x\end{pmatrix}
K_a
\begin{pmatrix}x&y\\-y&x\end{pmatrix}
\pmod p.
$$


Consequently,


$$
\boxed{
\Delta_N\equiv2^{2kp}\Delta_a\pmod p.
}
\tag{5.3}
$$



This is only a prime-modulus identity. It does not license division by a singular $\Delta_a$ or assert a prime-power depth.

### 5.3 The class $N\equiv1\pmod p$

Here $a=1$, and the partial evaluation vectors are $1$ and $i$. Thus


$$
\mathsf U_N\equiv\mathsf W_N\equiv2^{kp},\qquad
\mathsf V_N\equiv0,\qquad
\Delta_N\equiv2^{2kp}\pmod p.
\tag{5.4}
$$


Since $p\mid N!$,


$$
D=\Delta-(N!)^2\mathsf W\equiv\Delta\not\equiv0\pmod p.
$$



The actual polynomial reduction is


$$
\Phi_N(t)\equiv
2^{kp}R_p(t)(x-yt)\pmod p.
\tag{5.5}
$$


Because $x^2+y^2\ne0$, this polynomial is nonzero. Hence $d_N$ is a $p$-unit.

For $N\ge4$,


$$
m=2N-4=2kp-2
$$


and $p\mid T_N$. Therefore


$$
\mathscr W_N\equiv D\Delta g_N^2\not\equiv0\pmod p.
$$


The actual content $h_N$ is a $p$-unit. Thus


$$
\boxed{v_p(M_N)=v_p(T_N).}
\tag{5.6}
$$



### 5.4 Paying the whole first-square integral

The exact quotient identity is


$$
S_N=
\frac{T_NQ_\Phi+D\Delta S_g}{h_N},
\qquad
S_g=(1+t^2)(1-t)^m.
\tag{5.7}
$$


Let


$$
a_{\max}=\left\lfloor\log_p(2N-1)\right\rfloor.
$$


Since $Q_\Phi\in\mathbb Z[t]$ has degree at most $2N-2$,


$$
v_p\!\left(\int_0^1Q_\Phi\right)\ge-a_{\max}.
\tag{5.8}
$$



For $p\ge3$, $k\ge1$,


$$
2kp+1<p^{2k}.
$$


The base case is $2p+1<p^2$; multiplication by $p^2$ proves the induction step. Hence


$$
a_{\max}\le2k-1.
$$


On the other hand,


$$
v_p(T_N)\ge
\left\lfloor\frac{2kp-2}{p}\right\rfloor
=2k-1.
$$


Therefore


$$
\boxed{
T_N\int_0^1Q_\Phi\in\mathbb Z_{(p)}.
}
\tag{5.9}
$$



This pays the complete first-square arctangent term.

### 5.5 The negative beta valuation, least clearer, and final gcd

Let


$$
s=v_p(N-1)\ge1.
$$


At $m\equiv-2\pmod p$,


$$
m^2+5m+8\equiv2\pmod p,
$$


while $m+1$ and $m+3$ are units and


$$
v_p(m+2)=v_p(2(N-1))=s.
$$


Thus


$$
v_p(\beta_g)=-s.
\tag{5.10}
$$



In (5.7), the first-square integral is $p$-integral, while the second-square integral has valuation $-s$. The factors $D,\Delta,h_N$ are units. Hence


$$
v_p\!\left(\int_0^1S_N\right)=-s.
$$


The factorial endpoint $B_{\mathrm{end},N}$ is an integer, and $4$ is a $p$-unit. Therefore


$$
v_p(R_N)=-s.
$$


Because $\lambda_N$ is the least denominator of $R_N$,


$$
v_p(\lambda_N)=s,\qquad v_p(A_N)=0.
$$


The final all-prime gcd consequently has


$$
v_p(\mathfrak G_N)=0.
$$


Combining this with (5.6) proves


$$
\boxed{
v_p(q_N)=v_p(T_N)+v_p(N-1),
\quad N\ge4,\quad p\mid N-1,\quad p\text{ odd}.
}
\tag{5.11}
$$



**Audit verdict:** every normalization payment required for the final-$q_N$ statement is present. There is no unsupported step in this theorem.

---

## 6. Audit of the ordinary-error lower bounds

### 6.1 The complex Legendre evaluation estimate

Let


$$
\mathcal L_j(t)=P_j(2t-1),
$$


where $P_j$ is the Legendre polynomial. Rodrigues’ formula gives


$$
\int_0^1\mathcal L_j\mathcal L_r=0\quad(r<j),
\qquad
\int_0^1\mathcal L_j^2=\frac1{2j+1}.
$$


The finite expansion is


$$
\mathcal L_j(t)
=\sum_{r=0}^j(-1)^{j+r}
\binom jr\binom{j+r}{r}t^r.
$$


Hence


$$
|\mathcal L_j(i)|
\le\sum_{r=0}^j\binom jr\binom{j+r}{r}
=P_j(3).
$$


The classical normalized integral representation gives


$$
0<P_j(3)\le(3+2\sqrt2)^j<6^j
\quad(j>0).
$$


Therefore


$$
\sum_{j=0}^d(2j+1)|\mathcal L_j(i)|^2
\le(d+1)^2\,36^d.
$$



Expanding a real polynomial $F$ of degree at most $d$ in this orthogonal basis and applying complex Cauchy–Schwarz yields


$$
\boxed{
\|F\|_{L^2[0,1]}
\ge\frac{|F(i)|}{(d+1)6^d}.
}
\tag{6.1}
$$



For the actual $f_N(i)=1$,


$$
J_N\ge\int_0^1f_N^2
\ge\frac1{(N+1)^2\,36^N}.
\tag{6.2}
$$



### 6.2 The older $255255$ progression bound

The supplied finite integer certificate establishes only the fixed inequality


$$
2^{240}
3^{120}5^{60}7^{40}11^{24}13^{20}17^{15}
>13^{240}.
$$


Thus, for


$$
C=\sum_{p\in\{3,5,7,11,13,17\}}\frac{\log p}{p-1},
$$


it gives


$$
e^C>\frac{13}{2}.
$$



Combining this fixed constant with (5.11), factorial valuations, and the weaker lower bound (6.2) gives exactly


$$
\ell_N>
\frac{48}{28561}\,
\frac{(13/12)^{2N}}
{(2N-4)^6(N+1)^2}
$$


when $N\equiv1\pmod{255255}$.

The certificate is reused; its large integer multiplication is not repeated.

There is an important domain distinction:


$$
3\mid 9^{18+32u},
$$


so **no original index** is $1\pmod{255255}$. The older progression result is a valid auxiliary all-$N$ obstruction, but it does not itself obstruct the retained original sequence.

### 6.3 The real Laguerre coefficient norm

The actual minimizer expands as


$$
f_N(t)=\sum_{j=0}^Nc_jL_j(1-t),
$$


where


$$
c_j=\frac{N!(\mathsf W\alpha_j-\mathsf V\beta_j)}{\Delta}.
$$


All $c_j$ are real, and orthonormality gives


$$
\boxed{
\sum_{j=0}^Nc_j^2
=\tau_N
=\frac{(N!)^2\mathsf W}{\Delta}
\le\frac23<1.
}
\tag{6.3}
$$


This norm statement does not divide out an arithmetic content.

### 6.4 Entire growth estimate

The finite Laguerre formula and


$$
\binom jr\le\frac{j^r}{r!}
$$


give, for complex $z$,


$$
|L_j(z)|
\le\sum_{r\ge0}\frac{(j|z|)^r}{(r!)^2}
\le e^{2\sqrt{j|z|}}.
\tag{6.4}
$$


For the last inequality, the $2r$-th term of $e^{2\sqrt x}$ dominates $x^r/(r!)^2$, because $\binom{2r}{r}\le4^r$.

For $|t|\le36$, one has $|1-t|\le37$. Equations (6.3)–(6.4) and Cauchy–Schwarz give


$$
\boxed{
|f_N(t)|\le
C_N:=\sqrt{N+1}\,e^{2\sqrt{37N}}.
}
\tag{6.5}
$$



### 6.5 Simultaneous Taylor-tail bounds

To distinguish the truncation degree from the denominator $M_N$, write


$$
M_{\mathrm{tr}}
=\min\!\left(N,\left\lceil16\sqrt N\right\rceil\right).
\tag{6.6}
$$


Let $F_{\mathrm{tr}}$ be the Taylor polynomial of the actual $f_N$ at $0$, through this degree.

If $M_{\mathrm{tr}}=N$, the tail is zero. Otherwise Cauchy’s coefficient bound on $|t|=36$ gives


$$
|f_N(t)-F_{\mathrm{tr}}(t)|
\le
\delta_N:=\frac{C_N36^{-M_{\mathrm{tr}}}}{35},
\qquad |t|\le1.
\tag{6.7}
$$


This single disk estimate covers both the whole interval $[0,1]$ and the point $i$.

Set


$$
K=(M_{\mathrm{tr}}+1)6^{M_{\mathrm{tr}}}.
$$


In the nonzero-tail case,


$$
M_{\mathrm{tr}}\ge16\sqrt N,\qquad
M_{\mathrm{tr}}+1\le18\sqrt N.
$$


Also


$$
\sqrt{N+1}\le\frac32\sqrt N,\qquad
2\sqrt{37}<13,\qquad \log6>\frac32.
$$


Therefore


$$
\delta_NK
\le\frac{27N}{35}e^{-11\sqrt N}<\frac14.
\tag{6.8}
$$


The final inequality follows because $x^2e^{-11x}$ decreases for $x\ge1$, and $e^{-11}<2^{-11}$.

Thus


$$
|F_{\mathrm{tr}}(i)|\ge\frac34.
$$


Applying (6.1) to the real polynomial $F_{\mathrm{tr}}$, and then the reverse triangle inequality, yields


$$
\|f_N\|_{L^2[0,1]}
\ge\frac{3}{4K}-\delta_N
\ge\frac1{2K}.
$$


When the tail is zero, (6.1) gives an even stronger estimate. Consequently,


$$
\boxed{
J_N\ge
\frac1{4(M_{\mathrm{tr}}+1)^2\,36^{M_{\mathrm{tr}}}}
\qquad(N\ge2).
\tag{6.9}
$$



**Audit verdict:** the root-exponential lower estimate is valid. It is a lower bound for the actual positive polynomial’s integral, not a comparison of two upper bounds.

---

## 7. Whole-error divergence and the original-domain uniform theorem

### 7.1 Each fixed odd-prime class

Let $p$ be fixed and odd, and suppose $N\ge4$, $p\mid N-1$. Put $m=2N-4$.

The factorial digit formula gives


$$
v_p(m!)=\frac{m-s_p(m)}{p-1},
$$


with


$$
s_p(m)\le(p-1)\bigl(\lfloor\log_pm\rfloor+1\bigr).
$$


Using (5.11) and $v_p(N-1)\ge1$,


$$
v_p(q_N)\ge
\frac{m}{p-1}-\lfloor\log_pm\rfloor.
$$


Since $p^{\lfloor\log_pm\rfloor}\le m$,


$$
q_N\ge\frac{p^{m/(p-1)}}{m}.
\tag{7.1}
$$



Equations (2.16) and (6.9) now give


$$
\boxed{
\ell_N\ge
\frac{3p^{m/(p-1)}}
{4m(M_{\mathrm{tr}}+1)^2\,36^{M_{\mathrm{tr}}}}.
}
\tag{7.2}
$$


For fixed $p$, the positive logarithmic term is linear in $N$, while


$$
M_{\mathrm{tr}}\log36=O(\sqrt N).
$$


Hence


$$
\boxed{
\ell_N\longrightarrow+\infty
\quad
(N\to\infty,\ N\equiv1\pmod p,\ p\text{ fixed and odd}).
}
\tag{7.3}
$$



There is no unsupported step in this combined claim at its stated all-$N$ scope. The first unsupported extension would be to assert coverage of every integer $N$, or coverage of an original-domain intersection without checking that intersection.

### 7.2 Every original index lies in the $p=5$ class

At the actual original indices,


$$
N=9^{18+32u}
=81^{9+16u}
\equiv1\pmod5.
\tag{7.4}
$$


Thus (7.2) applies to **every** original index.

More precisely,


$$
v_5(N-1)=1+v_5(9+16u).
\tag{7.5}
$$


This follows from the elementary lifting identity for $81=1+80$: raising a number congruent to $1\pmod5$ to the fifth power increases $v_5(x-1)$ by one, while raising it to an exponent prime to $5$ preserves that valuation.

Since


$$
m\equiv-2\pmod5,\qquad
\mathcal R_4(m)\equiv\mathcal R_4(-2)=12\not\equiv0\pmod5,
$$


the exact surviving valuation is


$$
\boxed{
v_5(q_N)
=
v_5((2N-4)!)+1+v_5(9+16u).
}
\tag{7.6}
$$


At these same indices,


$$
v_5(h_N)=v_5(\Delta_N)=v_5(D_N)
=v_5(\mathfrak G_N)=0,
$$


and


$$
v_5(\lambda_N)=1+v_5(9+16u).
$$


Other primes in the final all-prime gcd cannot remove this surviving $5$-power.

### 7.3 An explicit bound valid at every original index

Write


$$
r=\sqrt N=3^{18+32u}.
$$


Here $r>16$, so


$$
M_{\mathrm{tr}}=16r.
$$


From (7.2) with $p=5$,


$$
\ell_N\ge
\frac{3\,5^{r^2/2-1}}
{4(2r^2-4)(16r+1)^2\,36^{16r}}.
$$


Using


$$
2r^2-4<2r^2,\qquad 16r+1\le17r,
$$


we get


$$
\ell_N>
\frac3{11560}\,
\frac{5^{r^2/2}}{r^4\,36^{16r}}.
$$


Now


$$
\frac3{11560}>2^{-12},\qquad
5^{r^2/2}>2^{r^2},\qquad
36^{16r}<2^{96r},\qquad
r^4\le2^{4r}.
$$


Therefore


$$
\boxed{
\ell_N>2^{r^2-100r-12}.
}
\tag{7.7}
$$


For $r\ge101$, the exponent is positive. Every original $r$ is much larger than $101$, without requiring any large-index computation.

This proves (A), and establishes:

> **New proved original-domain no-go theorem.**  
> For the specified minimizing-polynomial-plus-$g_N$-square ansatz,
> 

$$
> q_N(e+\pi)-p_N>1
>
$$


> at every retained original index $N=9^{18+32u}$, and these whole primitive errors tend to $+\infty$ as $u\to\infty$.

This is uniform on the original domain. It is not merely a collection of bad fixed-prime subsequences.

It does not prove the older, much stronger denominator floor


$$
q_N\ge(2N-3)T_N.
$$


That floor is no longer needed for the obstruction: the root-exponential lower bound is substantially stronger than the old factorial-scale ordinary lower bound.

---

## 8. New final-gcd arithmetic on the moving class $N\equiv2\pmod p$

The preceding audit also permits a new exact theorem at a different last partial block.

### Theorem 8.1

Let


$$
p\ge5,\qquad p\ne71,\qquad N=kp+2,\qquad k\ge1.
$$


Then


$$
\boxed{
v_p(h_N)=v_p(\Delta_N)=v_p(D_N)=0,
}
$$




$$
\boxed{
v_p(\lambda_N)=v_p(A_N)=v_p(\mathfrak G_N)=0,
}
$$


and


$$
\boxed{
v_p(q_N)=v_p(T_N)=v_p((2N-4)!).
}
\tag{8.1}
$$



#### Proof

The source-normalized block at index $2$ consists of


$$
2,\qquad 2t,\qquad t^2+2t-1.
$$


Its evaluations at $i$ are


$$
2,\qquad2i,\qquad-2+2i.
$$


Thus


$$
\mathsf U_2=\mathsf W_2=8,\qquad
\mathsf V_2=-4,\qquad
\Delta_2=48.
$$


Equation (5.3) gives


$$
\Delta_N\equiv2^{2kp}48\not\equiv0\pmod p.
$$


Since $p\mid N!$, $D_N\equiv\Delta_N\pmod p$. Also $d_N$ is a unit because $\Phi_N(i)=\Delta_N$.

Here


$$
m=2N-4=2kp.
$$


Thus


$$
\mathcal R_4(m)\equiv12\pmod p,
$$


so


$$
v_p(T_N)=v_p(m!)\ge2k.
$$


The raw second-square term is nonzero modulo $p$, proving $v_p(h_N)=0$.

The complete first-square quotient has denominators at most


$$
2N-1=2kp+3.
$$


For $p\ge5$, $k\ge1$,


$$
2kp+3<p^{2k}.
$$


Hence


$$
v_p(T_NR_\Phi)\ge
v_p(T_N)-\lfloor\log_p(2N-1)\rfloor
\ge1.
\tag{8.2}
$$



Meanwhile, $m\equiv0\pmod p$ and


$$
C_m=mC_{m-1}+1\equiv1\pmod p.
$$


Equations (4.1)–(4.4) give


$$
B_g\equiv12+17=29,\qquad
\beta_g\equiv\frac{8}{6}=\frac43,
$$


and therefore


$$
\boxed{
R_g\equiv29-\frac{16}{3}=\frac{71}{3}\pmod p.
}
\tag{8.3}
$$


This is a unit when $p\ne71$.

Let


$$
K_N:=T_NR_\Phi+D\Delta R_g.
$$


Equations (8.2)–(8.3) show that $K_N$ is a $p$-unit. Since $h_N$ is a unit,


$$
R_N=K_N/h_N
$$


is a $p$-unit. Therefore its least denominator $\lambda_N$ is a unit, and so is $A_N=\lambda_NR_N$. The final gcd has no $p$-factor.

Finally,


$$
v_p(M_N)=v_p(T_N),
$$


which proves (8.1). ∎

This is an actual final-gcd theorem. It does not claim that $\mathfrak G_N=1$ globally; it determines its valuation at every prime covered by the theorem.

### 8.1 A uniform moving-prime consequence

Theorem 8.1 and the factorial digit bound give


$$
q_N\ge\frac{p^{m/(p-1)}}{pm}
$$


on its residue classes. The slightly stronger bound (7.1) holds when $p\mid N-1$.

Suppose, at each $N$ under consideration, there is a prime $p\le\sqrt N$ satisfying either

- $p$ is odd and $p\mid N-1$; or
- $p\ge5$, $p\ne71$, and $p\mid N-2$.

The function $\log x/(x-1)$ is decreasing for $x>1$. With $x=\sqrt N\ge2$,


$$
\frac{m\log p}{p-1}
\ge\frac{(2x^2-4)\log x}{x-1}
\ge2x\log x
=\sqrt N\log N.
$$


Combining this with (6.9) gives the uniform bound


$$
\boxed{
\ell_N\ge
\frac{\exp\!\bigl(\sqrt N(\log N-16\log36)\bigr)}
{31104\,N^{5/2}}.
}
\tag{8.4}
$$


Its right side tends to $+\infty$.

Thus the argument now covers moving primes up to $\sqrt N$ under explicit, validated residue conditions. It still does not cover every integer $N$.

---

## 9. The exceptional prime $71$: a further final-gcd depth

The exception in (8.3) is genuine and merits a prime-power calculation rather than deletion from the endpoint.

### 9.1 A bounded constant calculation

The recurrence


$$
C_0=1,\qquad C_j=jC_{j-1}+1
$$


gives


$$
\boxed{C_{70}\equiv4\pmod{71}.}
\tag{9.1}
$$


A small residue certificate, in consecutive blocks, is:


$$
\begin{array}{c|l}
j& C_j\bmod71\\ \hline
0\!:\!9&1,2,5,16,65,42,40,68,48,7\\
10\!:\!19&0,1,13,28,38,3,49,53,32,41\\
20\!:\!29&40,60,43,67,47,40,47,63,61,66\\
30\!:\!39&64,68,47,61,16,64,33,15,3,47\\
40\!:\!49&35,16,34,44,21,23,65,3,3,6\\
50\!:\!59&17,16,52,59,63,58,54,26,18,69\\
60\!:\!69&23,55,3,48,20,24,24,47,2,68\\
70&4
\end{array}
$$


Each entry is checked by one multiplication and one reduction. This is finite arithmetic, not an extrapolation in $N$.

### 9.2 A prime-power theorem away from one lifted residue class

Let


$$
N=71k+2,\qquad k\ge2,\qquad m=142k.
$$


The source, content, and beta-denominator unit conclusions in Theorem 8.1 remain valid.

For $k\ge2$,


$$
2k\cdot71+3<71^{2k-1},
$$


so the complete first-square term satisfies


$$
v_{71}(T_NR_\Phi)\ge2.
\tag{9.2}
$$



Since $71\mid m$,


$$
C_m\equiv1+mC_{70}\pmod{71^2}.
$$


Expanding (4.1)–(4.4) to first order in $m$ gives


$$
R_g\equiv
\frac{71}{3}
+m\left(12C_{70}+\frac{418}{9}\right)
\pmod{71^2}.
$$


Using (9.1),


$$
12C_{70}+\frac{418}{9}\equiv55\pmod{71}.
$$


Hence


$$
\boxed{
\frac{R_g}{71}\equiv24+39k\pmod{71}.
}
\tag{9.3}
$$


The unique zero of this linear expression is


$$
k\equiv54\pmod{71}.
$$



Therefore:

> **New prime-power refinement.**  
> If
> 

$$
> N=71k+2,\qquad k\ge2,\qquad k\not\equiv54\pmod{71},
>
$$


> then
> 

$$
> v_{71}(A_N)=v_{71}(\mathfrak G_N)=1,
>
$$


> 

$$
> \boxed{
> v_{71}(q_N)=v_{71}(T_N)-1.
> }
> \tag{9.4}
>
$$



Indeed, (9.2) makes the first-square term zero modulo $71^2$, while (9.3) gives the second-square endpoint valuation exactly one. The factors $D,\Delta,h_N,\lambda_N$ are units.

This explicitly evaluates a nontrivial part of the **final** gcd.

### 9.3 The small boundary $N=73$

For completeness, $k=1$ requires the first-square correction; (9.2) does not apply.

Modulo $71$, the last block gives


$$
\Delta\equiv192\equiv50,\qquad D\equiv50,
$$


and


$$
\Phi(t)\equiv
32(t^{71}-1)(t^2+3t-2).
$$


The quotient $Q_\Phi$ has integration denominators through $145$, so both $71$ and $142$ contribute. Direct monic division gives


$$
[t^{70}]Q_\Phi=36\cdot32^2,\qquad
[t^{141}]Q_\Phi=-18\cdot32^2
\pmod{71}.
$$


Consequently,


$$
71\int_0^1Q_\Phi
\equiv
36\cdot32^2-\frac{18\cdot32^2}{2}
\equiv29\pmod{71}.
$$


Also


$$
T_{73}/71^2\equiv24\pmod{71}.
$$


Thus


$$
\frac{T_{73}R_\Phi}{71}\equiv-4\cdot24\cdot29\equiv56\pmod{71}.
$$


Equation (9.3) gives $R_g/71\equiv63$, while $D\Delta\equiv15$. Hence


$$
\frac{K_{73}}{71}
\equiv56+15\cdot63
\equiv7\not\equiv0\pmod{71}.
$$


It follows that


$$
\boxed{
v_{71}(M_{73})=2,\quad
v_{71}(\lambda_{73})=0,\quad
v_{71}(\mathfrak G_{73})=1,\quad
v_{71}(q_{73})=1.
}
\tag{9.5}
$$



This is an auxiliary finite local normalization. It is not an original-index instance, and it does not assert that the global gcd $\mathfrak G_{73}$ equals $71$.

It also illustrates why the one-pole $\Psi$ formula for $p>N$ cannot be copied unchanged into the low-prime range: here there are two relevant $p$-denominators.

---

## 10. Proof status and exact remaining bottlenecks

### 10.1 What has now been proved

The following are rigorous statements about the actual objects:

- A2’s exact all-prime raw-content formula;
- the evaluated auxiliary gcd $4(N-2)!$;
- the complete second-square endpoint;
- the regular-factorial-prime $\Psi$ criterion, with its full correction;
- the last-source-block congruence, including odd split Gaussian algebras;
- the actual primitive-denominator formula at every odd $p\mid N-1$;
- the root-exponential ordinary-error lower bound;
- whole-error divergence on each fixed odd-prime $N\equiv1\pmod p$ progression;
- **uniform whole-error divergence at every retained original index**;
- the new final-gcd theorem on $N\equiv2\pmod p$, $p\ge5$, $p\ne71$;
- the stated $71$-adic final-gcd refinement.

The proof of the original-domain obstruction does not depend on any new large finite computation.

### 10.2 What is conditional or still open

The statement


$$
0<q_N(e+\pi)-p_N\to0
$$


would imply irrationality of $e+\pi$, because a rational number with fixed denominator cannot have nonzero integer linear-form errors tending to zero. That implication remains valid.

For this particular ansatz on the original domain, however, its hypothesis is now disproved by (7.7). The old primitive-saving lemma on those indices cannot hold.

For the extension to arbitrary $N$, a uniform no-go is still open. The uncovered arithmetic includes:

- kernel-prime classes in which the partial determinant $\Delta_a$ vanishes;
- the ramified prime $2$, being advanced separately;
- moving residue classes not covered by the last-block theorems;
- the remaining regular-factorial-prime $\Psi$ residues and higher-depth analogues;
- the combined all-prime final gcd on any proposed surviving subsequence.

Bad fixed-prime subsequences alone would not establish a uniform all-$N$ obstruction. The original-domain theorem is stronger for a specific reason: the fixed prime $5$ is forced at **every** original index.

Finally, neither a family-specific obstruction nor an enormous positive primitive error implies that $e+\pi$ is rational. The global rationality question remains unresolved.

---

## 11. A bounded exact-arithmetic follow-on

No repeated $N=8$ computation is needed. A small modular task can advance the remaining lifted $71$-adic class.

Take


$$
p=71,\qquad k=54,\qquad N=3836,\qquad m=7668.
$$


Here


$$
v_{71}(T_N)
=
\left\lfloor\frac{7668}{71}\right\rfloor
+
\left\lfloor\frac{7668}{71^2}\right\rfloor
=108+1=109,
$$


and


$$
\left\lfloor\log_{71}(2N-1)\right\rfloor=2.
$$


Thus the complete first-square endpoint has valuation at least $107$. It cannot affect a calculation modulo $71^3$.

The source-normalized block theorem already proves that


$$
\Delta_N,\ D_N,\ h_N,\ \lambda_N
$$


are $71$-adic units. Equation (9.3) proves $71^2\mid R_g$.

### Exact bounded inputs

Use


$$
71^3=357911,
$$


the integer $m=7668$, and the polynomials


$$
\mathcal R_4(x)=x^4+6x^3+19x^2+22x+12,
$$




$$
H_3(x)=x^3+6x^2+18x+17.
$$



The identity


$$
C_m=\sum_{r=0}^m(m)_r,
\qquad
(m)_r=m(m-1)\cdots(m-r+1),
$$


gives the bounded reduction


$$
C_m\equiv\sum_{r=0}^{212}(m)_r\pmod{71^3}.
\tag{11.1}
$$


Every omitted product has at least three factors divisible by $71$. Thus only 213 falling-factorial terms are needed.

Then evaluate, modulo $71^3$,


$$
R_g=
\mathcal R_4(m)C_m+H_3(m)
-
4\frac{m^2+5m+8}{(m+1)(m+2)(m+3)}.
\tag{11.2}
$$


The displayed denominator is a unit modulo $71^3$.

### Expected verifiable outputs

A receipt should contain:

1. $C_{7668}\bmod357911$, computed from (11.1);
2. the modular inverse of the denominator in (11.2);
3. $R_g\bmod357911$;
4. verification that $R_g\equiv0\pmod{5041}$;
5. the residue
   

$$
\rho=\frac{R_g}{5041}\pmod{71}.
$$



No nonzero value of $\rho$ is assumed.

- If $\rho\ne0$, the proved normalization identities give
  

$$
v_{71}(\mathfrak G_{3836})=2,\qquad
  v_{71}(q_{3836})=107.
$$


- If $\rho=0$, they give
  

$$
v_{71}(\mathfrak G_{3836})\ge3,
$$


  and a further explicitly bounded prime-power calculation would be required.

This task addresses one finite prime-power gate. It would not prove a uniform theorem on the remaining lifted residue class or decide the irrationality of $e+\pi$.

---

## Final assessment

The audited arithmetic and analytic claims survive review at their exact hypotheses. In particular, the last-block theorem really reaches the **least affine clearer and final all-prime gcd**, and the Taylor argument really supplies a **lower bound for the whole ordinary error**.

The decisive new conclusion is that the retained original indices all satisfy $N\equiv1\pmod5$. Consequently, the specified two-square family has


$$
\boxed{
q_N(e+\pi)-p_N
>
2^{\,N-100\sqrt N-12}
}
$$


at every original index, and its whole primitive errors diverge uniformly there.

The new $N\equiv2\pmod p$ theorem and the $71$-adic refinement further advance the final-gcd arithmetic on other residue classes. They do not justify a uniform no-go over every integer $N$.

Thus the original primitive-decay bottleneck for this particular ansatz is resolved **negatively**, but the global research objective is not achieved:



$$
\boxed{\text{Neither rationality nor irrationality of }e+\pi\text{ is proved.}}
$$


