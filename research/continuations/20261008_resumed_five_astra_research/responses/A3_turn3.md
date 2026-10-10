> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Ramified dyadic normalization and a whole-error obstruction for the prescribed two-square family

## Abstract and proof status

The rationality or irrationality of $e+\pi$ is **not decided in this report**.

The new result is a ramified $2$-adic analysis of the **actual source-normalized two-square construction**, including its polynomial contents, least affine clearer, and final all-prime gcd. It yields, at every prescribed original index


$$
N=9^{18+32u},\qquad u\ge0,
$$


the exact primitive-denominator valuation


$$
\boxed{v_2(q_N)=2N-s_2(N-2),}
\tag{A}
$$


where $s_2(n)$ denotes the sum of the binary digits of $n$.

In particular, this factor survives **after** both polynomial-content division and the final all-prime gcd. Combining (A) with the coordinator’s valid effective-degree lower bound gives


$$
\boxed{
q_N(e+\pi)-p_N
\ge
\frac{3\,2^{\,2N-s_2(N-2)}}
     {4(16\sqrt N+1)^2\,36^{16\sqrt N}}
\longrightarrow+\infty
}
\tag{B}
$$


at those same original indices. In fact, an elementary estimate below proves that the complete primitive error is greater than $1$ at **every** prescribed index.

Thus the specified two-square producer cannot provide vanishing primitive errors on any infinite subset of its prescribed original domain. This is a family-specific obstruction, not a rationality theorem for $e+\pi$.

The dyadic result has a broader scope. For odd $N\ge5$, it gives exact final-$q_N$ valuations whenever


$$
v_2(N-1)=1
\quad\text{or}\quad
v_2(N-1)\ge3.
$$


It therefore also excludes the entire growing subfamily $N-1=2^s$. In the remaining class $N\equiv5\pmod8$, a paid classification reduces possible exceptions to exceptionally close approximations to one explicitly defined $2$-adic root. That root condition is derived below, not inferred from $N=8$.

There is also an important domain observation: every prescribed original $N$ satisfies $5\mid N-1$. Consequently, the coordinator’s fixed-prime theorem already obstructs the whole prescribed domain once its root-exponential lower bound is accepted. The new contribution here is the independent ramified calculation, the exact formula (A), and the broader odd-index classification.

No $N=8$ construction or closed content calculation is repeated.

---

## 1. The exact family and its complete normalization

### 1.1 Source polynomials and the specified two squares

Use


$$
d\eta(t)=e^{t-1}\mathbf 1_{(-\infty,1]}(t)\,dt,
\qquad
Q_j(t)=L_j(1-t),
\qquad
E_j(t)=N!Q_j(t),
$$


with precisely


$$
0\le j\le N.
$$


The classical Laguerre normalization gives


$$
\int Q_jQ_r\,d\eta=\delta_{jr}.
$$



Write


$$
E_j(i)=\alpha_j+i\beta_j
$$


and retain


$$
\mathsf U=\sum_{j=0}^N\alpha_j^2,\qquad
\mathsf V=\sum_{j=0}^N\alpha_j\beta_j,\qquad
\mathsf W=\sum_{j=0}^N\beta_j^2,
$$




$$
\Delta=\mathsf U\mathsf W-\mathsf V^2,\qquad B=(N!)^2.
$$


The actual minimizing numerator is


$$
\Phi(t)=
\sum_{j=0}^N(\mathsf W\alpha_j-\mathsf V\beta_j)E_j(t).
$$


Thus


$$
\Phi(i)=\Delta,\qquad
f_N=\frac{\Phi}{\Delta},\qquad
\tau_N=\int f_N^2\,d\eta=\frac{B\mathsf W}{\Delta}.
$$



The two evaluation constraints are independent already in $Q_0=1,Q_1=t$, so $\Delta>0$. The Euclidean constrained-minimum argument in the sources applies to this full polynomial space and gives the stated $f_N$. The admissible comparison $(5-t^2)/6$ gives


$$
\tau_N\le\frac23.
$$


Consequently


$$
D=\Delta-B\mathsf W>0.
$$



The second square remains exactly


$$
g_N(t)=(1+t^2)(1-t)^{N-2}.
$$


Putting


$$
m=2N-4,\qquad
\mathcal R_4(x)=x^4+6x^3+19x^2+22x+12,
$$


its norm is


$$
T_N=m!\mathcal R_4(m)
=(2N)!-4(2N-1)!+8(2N-2)!-8(2N-3)!+4(2N-4)!.
$$


The producer is not changed:


$$
P_N=f_N^2+\frac{1-\tau_N}{T_N}g_N^2.
\tag{1.1}
$$


It satisfies


$$
P_N(i)=P_N(-i)=1,\qquad \int P_N\,d\eta=1,
$$


and is strictly positive on $0\le t<1$.

### 1.2 All source terms and the whole error

The exponential moments and endpoint identity are


$$
a_0=1,\qquad a_d=1-da_{d-1},
$$




$$
\int_0^1e^tt^d\,dt=e\,a_d-(-1)^dd!.
$$


For the arctangent channel,


$$
4\int_0^1\frac{t^d}{1+t^2}\,dt
=
\pi\Re(i^d)+2\log2\,\Im(i^d)+4\sigma_d,
$$


where


$$
\sigma_0=\sigma_1=0,\qquad
\sigma_d=\frac1{d-1}-\sigma_{d-2}.
$$



Thus odd powers carry a genuine $\log2$ source. It disappears here because the actual contact condition is $P_N(i)=1$, not because odd terms have been removed.

Set


$$
w(t)=e^t+\frac4{1+t^2}.
$$


On $[0,1]$,


$$
3\le w(t)<7.
\tag{1.2}
$$



### 1.3 Actual contents, least clearers, and final gcd

The raw integer objects remain


$$
\mathscr W_N=T_N\Phi^2+D\Delta g_N^2,
\qquad
\mathscr Z_N=T_N\Delta^2.
$$


Define their actual polynomial content and primitive reduction by


$$
h_N=\operatorname{cont}(\mathscr W_N),\qquad
W_N=\frac{\mathscr W_N}{h_N},\qquad
M_N=\frac{\mathscr Z_N}{h_N}.
$$


Because $\mathscr W_N(i)=\mathscr Z_N$, one has $h_N\mid\mathscr Z_N$. The polynomial $W_N$ is primitive, so $M_N$ is the actual least simultaneous coefficient clearer of $P_N$.

We also retain the actual first-square content


$$
d_N=\operatorname{cont}(\Phi),\qquad
\phi_N=\frac{\Phi}{d_N}.
$$


The established all-prime content theorem applies unchanged:


$$
h_N=
\gcd\!\left(
T_Nd_N^2(\phi_N(0))^2+D\Delta,\,
T_Nd_N^2c_N\gcd(2,c_N)
\right),
\tag{1.3}
$$


where


$$
c_N=\operatorname{cont}\bigl(\phi_N-\phi_N(0)g_N\bigr).
$$


For $N\ge3$, its established bound is $c_N\mid4(N-2)!$. Nothing below replaces $h_N$ by merely a forced divisor.

Monic division gives the complete quotient


$$
S_N(t)=\frac{W_N(t)-M_N}{1+t^2}
      =\sum_{j=0}^{2N-2}s_jt^j\in\mathbb Z[t].
$$


Retain the complete factorial endpoint


$$
B_{\mathrm{end},N}
=\sum_{d=0}^{2N}[t^d]W_N(t)(-1)^dd!.
$$


Let


$$
L_{\mathrm{ent},N}
=\operatorname{lcm}_{0\le j\le2N-2}
  \frac{j+1}{\gcd(j+1,4s_j)},
$$




$$
J_{\mathrm{arc},N}
=\sum_{j=0}^{2N-2}\frac{4s_jL_{\mathrm{ent},N}}{j+1},
\qquad
d_{\mathrm{arc},N}
=\gcd(L_{\mathrm{ent},N},J_{\mathrm{arc},N}),
$$




$$
\lambda_N=\frac{L_{\mathrm{ent},N}}{d_{\mathrm{arc},N}}.
$$


Thus $\lambda_N$ is the actual denominator, after summation, of


$$
\mathcal E_N
:=B_{\mathrm{end},N}-4\int_0^1S_N(t)\,dt.
\tag{1.4}
$$


Set


$$
A_N=\lambda_N\mathcal E_N\in\mathbb Z.
$$


Minimality gives $\gcd(\lambda_N,A_N)=1$. The final gcd is the **all-prime** integer


$$
\mathfrak G_N
=\gcd(\lambda_NM_N,|A_N|)
=\gcd(M_N,|A_N|),
\tag{1.5}
$$


and


$$
q_N=\frac{\lambda_NM_N}{\mathfrak G_N},
\qquad
p_N=\frac{A_N}{\mathfrak G_N}.
\tag{1.6}
$$



The complete source identity is


$$
\epsilon_N:=(e+\pi)-\frac{p_N}{q_N}
=\int_0^1P_N(t)w(t)\,dt>0.
$$


Consequently, with


$$
J_N=\int_0^1P_N(t)\,dt,
$$


the whole primitive error is


$$
\ell_N:=q_N(e+\pi)-p_N=q_N\epsilon_N>0,
\qquad
3q_NJ_N\le\ell_N\le7q_NJ_N.
\tag{1.7}
$$



All subsequent denominator claims concern this $q_N$, not a raw polynomial denominator.

### 1.4 Finite boundaries

The proof retains:

- basis indices $0,\ldots,N$;
- final polynomial degree $2N$;
- exponential moments and factorial endpoints only through $2N$;
- quotient degree $2N-2$;
- affine integration denominators only through $2N-1$.

The diagnostic $J_N$ may have denominators through $2N+1$. That does not introduce a successor exponential moment or factorial.

---

## 2. Check of the two new coordinator arguments

No error was found in either argument at its stated scope. The following records the essential checks without repeating the closed independent audits.

### 2.1 Odd primes dividing $N-1$

Let $p$ be odd and $p\mid N-1$. Write


$$
N=kp+1.
$$


The classical prime-level Laguerre congruence, or its direct finite-coefficient proof, gives for the actual source-normalized basis


$$
E_j\equiv0\pmod p\quad(j<kp),
$$


and the last two columns are


$$
E_{kp}\equiv R_p,\qquad E_{kp+1}\equiv tR_p\pmod p,
$$


where


$$
R_p(t)=(-(1-t))^{kp}.
$$


At $i$, the norm of $R_p(i)$ is $2^{kp}$, a unit modulo an odd prime. Hence


$$
\mathsf U\equiv\mathsf W\equiv2^{kp},\qquad
\mathsf V\equiv0,\qquad
\Delta\equiv2^{2kp}\pmod p.
$$


Thus $\Delta,D,d_N$ are $p$-units. For $N\ge4$, $p\mid T_N$, and


$$
\mathscr W_N\equiv D\Delta g_N^2\not\equiv0\pmod p.
$$


Therefore $h_N$ is also a $p$-unit and


$$
v_p(M_N)=v_p(T_N).
$$



The complete quotient is


$$
S_N=\frac{T_NQ_\Phi+D\Delta S_g}{h_N},
$$


where


$$
Q_\Phi=\frac{\Phi^2-\Delta^2}{1+t^2},\qquad
S_g=(1+t^2)(1-t)^m.
$$


All its monomial integration denominators are at most $2N-1=2kp+1$. Since


$$
2kp+1<p^{2k},
$$


their maximum $p$-adic denominator depth is at most $2k-1$. Also


$$
v_p(T_N)\ge\left\lfloor\frac{2kp-2}{p}\right\rfloor=2k-1.
$$


Thus the **entire first-square arctangent term**, after multiplication by $T_N$, is $p$-integral.

The evaluated second-square quotient integral is


$$
\beta_g
=\int_0^1S_g(t)\,dt
=\frac{m^2+5m+8}{(m+1)(m+2)(m+3)}.
\tag{2.1}
$$


If $s=v_p(N-1)$, then $v_p(\beta_g)=-s$: the numerator is $2\pmod p$, the outside denominator factors are units, and $m+2=2(N-1)$.

This negative valuation strictly dominates the paid first-square term and the integer endpoint. Therefore


$$
v_p(\lambda_N)=s,\qquad v_p(A_N)=0,\qquad
v_p(\mathfrak G_N)=0.
$$


The coordinator’s formula is consequently valid:


$$
\boxed{
v_p(q_N)=v_p(T_N)+v_p(N-1),
\quad N\ge4,\quad p\text{ odd},\quad p\mid N-1.
}
\tag{2.2}
$$



This proof uses a unit rotation only at odd primes. It supplies no dyadic conclusion.

### 2.2 The effective-degree lower bound

Expand the actual minimizer as


$$
f_N(t)=\sum_{j=0}^Nc_jL_j(1-t).
$$


Orthogonality and the minimum give


$$
\sum c_j^2=\tau_N\le\frac23<1.
$$



The finite Laguerre formula implies


$$
|L_j(z)|
\le\sum_{r\ge0}\frac{(j|z|)^r}{(r!)^2}
\le e^{2\sqrt{j|z|}}.
$$


The last inequality follows termwise from the even terms in the exponential series and
$\binom{2r}{r}\le4^r$.

On $|t|\le36$, Cauchy–Schwarz therefore gives


$$
|f_N(t)|\le \sqrt{N+1}\,e^{2\sqrt{37N}}=:C_N.
$$


Let


$$
\mu_N=\min\{N,\lceil16\sqrt N\rceil\},
$$


and let $f_{\mu_N}$ be the Taylor truncation of the actual $f_N$ at zero. If $\mu_N<N$, Cauchy’s coefficient estimate gives, uniformly on $|t|\le1$,


$$
|f_N(t)-f_{\mu_N}(t)|
\le \frac{C_N36^{-\mu_N}}{35}
=:\delta_N.
$$


The constants in the coordinator’s estimate check as follows:


$$
\delta_N(\mu_N+1)6^{\mu_N}
\le\frac{27N}{35}e^{-11\sqrt N}<\frac14.
\tag{2.3}
$$


Here $2\sqrt{37}<13$, $\log6>3/2$, and
$\mu_N\ge16\sqrt N$ in the nonzero-tail case.

For completeness, the shifted Legendre evaluation kernel gives, for every real polynomial $F$ of degree at most $r$,


$$
|F(i)|\le (r+1)6^r\|F\|_{L^2[0,1]}.
\tag{2.4}
$$


Indeed, the shifted Legendre polynomials have squared norms $1/(2j+1)$, and their finite coefficient formula gives


$$
|P_j(2i-1)|\le P_j(3)<6^j\quad(j>0).
$$


Cauchy–Schwarz and $\sum_{j=0}^r(2j+1)=(r+1)^2$ prove (2.4).

Since $f_N(i)=1$, (2.3), (2.4), and the reverse triangle inequality give


$$
\|f_N\|_{L^2[0,1]}
\ge \frac1{2(\mu_N+1)6^{\mu_N}}.
$$


The zero-tail case is even simpler. Thus the proposed lower bound is valid for every $N\ge2$:


$$
\boxed{
J_N\ge
\frac1{4(\mu_N+1)^2\,36^{\mu_N}}.
}
\tag{2.5}
$$


Together with the **whole** error identity,


$$
\boxed{
\ell_N\ge
\frac{3q_N}{4(\mu_N+1)^2\,36^{\mu_N}}.
}
\tag{2.6}
$$



No denominator or content division has been inserted into this analytic estimate.

---

## 3. A division-paid ramified block recurrence

The dyadic calculation must account for ramification at $1-i$. The odd-prime rotation argument is unavailable because the relevant norm is a power of $2$.

### 3.1 Integral shifted Laguerre recurrence

Use the monic integral polynomials


$$
H_j(t)=j!L_j(1-t).
$$


They satisfy


$$
H_0=1,\qquad H_1=t,\qquad
H_{j+1}=(t+2j)H_j-j^2H_{j-1}.
\tag{3.1}
$$


This is the finite Laguerre recurrence at the required normalization.

Put


$$
Z_j=H_j(i).
$$


Define normalized Gaussian values


$$
F_r=\frac{Z_{2r}}{2^r},
\qquad
G_r=\frac{Z_{2r+1}}{2^r}.
\tag{3.2}
$$


The divisions in (3.2) require proof. They are paid by the following integral recurrence.

Starting with


$$
F_0=1,\qquad G_0=i,\qquad F_1=-1+i,
$$


one obtains


$$
\boxed{
G_r=(4r+i)F_r-2r^2G_{r-1},
}
\tag{3.3}
$$




$$
\boxed{
F_{r+1}
=
\bigl(6r^2+2r-1+(4r+1)i\bigr)F_r
-r^2(4r+2+i)G_{r-1}.
}
\tag{3.4}
$$


Both right sides have Gaussian-integer coefficients.

To check the apparently nontrivial division in the even step, substitute (3.3) into


$$
2F_{r+1}=(4r+2+i)G_r-(2r+1)^2F_r.
$$


The coefficient of $F_r$ becomes


$$
(4r+2+i)(4r+i)-(2r+1)^2
=2\bigl(6r^2+2r-1+(4r+1)i\bigr),
$$


and the other coefficient is also divisible by $2$. This gives (3.4) and proves inductively that all $F_r,G_r$ in (3.2) are Gaussian integers.

These are divisions of evaluation values only. No claim is made that $H_j(t)/2^{\lfloor j/2\rfloor}$ is an integral polynomial.

### 3.2 Reduction in the ramified ring

Work in


$$
\mathbb Z[i]/2\mathbb Z[i].
$$


Let $\varepsilon=1+i$. Then $\varepsilon^2=0$. Reducing (3.3)–(3.4) gives


$$
G_r\equiv iF_r\pmod2,
\qquad
F_{r+1}\equiv\varepsilon F_r+rF_{r-1}\pmod2.
$$


Induction yields the exact parity pattern


$$
\boxed{
\begin{array}{c|cc}
r&F_r&G_r\\ \hline
r\ \text{even}&1&i\\
r\ \text{odd}&1+i&1+i
\end{array}
\quad\pmod2.
}
\tag{3.5}
$$



In particular, the real and imaginary parts of each $F_r$ and $G_r$ are not both even. Equivalently, with $v_{1-i}(1-i)=1$,


$$
v_{1-i}(Z_{2r})=v_{1-i}(Z_{2r+1})
=
\begin{cases}
2r,&r\text{ even},\\
2r+1,&r\text{ odd}.
\end{cases}
\tag{3.6}
$$


Formula (3.6) is a genuinely ramified evaluation statement, not an odd-prime unit-rotation argument.

---

## 4. Actual source and content valuations at every odd $N\ge5$

Write


$$
N=2K+1,\qquad K\ge2.
$$



### 4.1 The actual source normalization

For $0\le r\le K$ and $\epsilon\in\{0,1\}$, put


$$
e_r=v_2\!\left(\frac{K!}{r!}\right).
$$


Since


$$
v_2(N!)=K+v_2(K!),
\qquad
v_2((2r+\epsilon)!)=r+v_2(r!),
$$


there is an odd positive integer $b_{r,\epsilon}$ such that


$$
\frac{N!}{(2r+\epsilon)!}
=
2^{K-r+e_r}b_{r,\epsilon}.
\tag{4.1}
$$


Every division defining $b_{r,\epsilon}$ is exact.

Consequently


$$
E_{2r}(i)=2^{K+e_r}b_{r,0}F_r,
\qquad
E_{2r+1}(i)=2^{K+e_r}b_{r,1}G_r.
\tag{4.2}
$$


This is a normalization of the actual $E_j$, not replacement by a lower-index kernel.

If $K$ is even, $e_r=0$ only for $r=K$. If $K$ is odd, $e_r=0$ only for $r=K,K-1$. All earlier blocks carry at least one additional factor of $2$.

Define integral scaled Gram entries


$$
U'=\frac{\mathsf U}{2^{2K}},\qquad
V'=\frac{\mathsf V}{2^{2K}},\qquad
W'=\frac{\mathsf W}{2^{2K}}.
$$


By (3.5):

- an even-$r$ full pair contributes the identity matrix modulo $2$;
- an odd-$r$ full pair contributes twice the all-ones matrix, hence zero modulo $2$.

The surviving last block, or last two blocks, therefore gives


$$
\boxed{U'\equiv W'\equiv1,\qquad V'\equiv0\pmod2.}
\tag{4.3}
$$


It follows that


$$
v_2(\mathsf U)=v_2(\mathsf W)=2K,\qquad
v_2(\mathsf V)\ge2K+1,
$$




$$
\boxed{v_2(\Delta)=4K.}
\tag{4.4}
$$



Furthermore,


$$
v_2(B\mathsf W)=4K+2v_2(K!)>4K,
$$


because $K\ge2$. Therefore


$$
\boxed{v_2(D)=4K.}
\tag{4.5}
$$



### 4.2 The actual content of $\Phi$

Write $F_r=X_{r,0}+iY_{r,0}$ and
$G_r=X_{r,1}+iY_{r,1}$. In the monic integral basis $H_j$, the coefficient of $H_{2r+\epsilon}$ in $\Phi$ is exactly


$$
2^{\,4K-r+2e_r}b_{r,\epsilon}^2
\bigl(W'X_{r,\epsilon}-V'Y_{r,\epsilon}\bigr).
\tag{4.6}
$$


Every such coefficient has valuation at least $3K$.

At $r=K$, (3.5) and (4.3) show that at least one of the two displayed bracketed factors is odd:

- if $K$ is even, use $F_K$;
- if $K$ is odd, either $F_K$ or $G_K$ works.

Thus some coefficient in (4.6) has valuation exactly $3K$.

The change from the monic integral basis $H_0,\ldots,H_N$ to monomials is unimodular over $\mathbb Z$. It preserves polynomial content. Hence


$$
\boxed{v_2(d_N)=3K.}
\tag{4.7}
$$


This evaluates the $2$-part of the actual content; the odd part of $d_N$ has not been suppressed.

### 4.3 $T_N$, the raw content, and the least polynomial clearer

The identity


$$
\mathcal R_4(x)
=x(x+1)(x+2)(x+3)+8(x+1)^2+4
$$


gives


$$
v_2(\mathcal R_4(x))=2
$$


for every nonnegative integer $x$. Since $m=4K-2$,


$$
t_N:=v_2(T_N)
=4K-1-s_2(K-1)
=2N-2-s_2(N-2).
\tag{4.8}
$$


Put


$$
u_K=t_N-2K=2K-1-s_2(K-1).
$$


Since $s_2(K-1)\le K-1$,


$$
u_K\ge K\ge2.
\tag{4.9}
$$



By (4.4), (4.5), and (4.7),


$$
v_2\bigl(\operatorname{cont}(T_N\Phi^2)\bigr)
=t_N+6K=8K+u_K,
$$


whereas


$$
v_2(D\Delta)=8K.
$$


Because $g_N(0)=1$, the constant coefficient of $D\Delta g_N^2$ has valuation exactly $8K$, while every coefficient of the first summand has strictly larger valuation. Thus there is no exceptional dyadic content cancellation:


$$
\boxed{v_2(h_N)=8K.}
\tag{4.10}
$$


It follows that


$$
\boxed{v_2(M_N)=t_N.}
\tag{4.11}
$$



These calculations prove the following source-and-content table.

### Theorem 4.1 — Uniform dyadic source normalization

For every odd $N\ge5$,


$$
\boxed{
\begin{array}{c|c}
\text{actual quantity}&2\text{-adic valuation}\\ \hline
\mathsf U,\mathsf W&N-1\\
\mathsf V&\ge N\\
\Delta,D&2N-2\\
d_N=\operatorname{cont}(\Phi)&3(N-1)/2\\
h_N=\operatorname{cont}(\mathscr W_N)&4N-4\\
T_N,M_N&2N-2-s_2(N-2).
\end{array}}
\tag{4.12}
$$



The cases $N=2,3$ are not included. In particular, the exceptional small normalization at $N=3$ is not extrapolated.

---

## 5. Complete endpoint cancellation and the final dyadic gcd

The valuations of $M_N$ alone would not prove a denominator lower bound. We now pay the affine integration and final gcd.

### 5.1 Separating the two complete endpoint functionals

Since $\phi_N(i)=\Delta/d_N\in\mathbb Z$,


$$
Q_\phi(t)
=\frac{\phi_N(t)^2-(\Delta/d_N)^2}{1+t^2}
\in\mathbb Z[t].
$$


Define


$$
R_\phi=
\sum_d[t^d]\phi_N^2\,(-1)^dd!
-4\int_0^1Q_\phi(t)\,dt.
\tag{5.1}
$$


For the second square, retain the full endpoint


$$
R_g=B_g-4\beta_g,
\tag{5.2}
$$


where $\beta_g$ is (2.1).

Work locally in $\mathbb Z_{(2)}$, and put


$$
a=\frac{T_Nd_N^2}{h_N},\qquad
b=\frac{D\Delta}{h_N}.
$$


These need not be integers at odd primes. The actual all-prime $h_N$ remains in both fractions. The proved local valuations are


$$
v_2(a)=u_K,\qquad v_2(b)=0.
\tag{5.3}
$$



The complete quotient and complete affine endpoint are exactly


$$
S_N=aQ_\phi+bS_g,
$$




$$
\boxed{\mathcal E_N=aR_\phi+bR_g.}
\tag{5.4}
$$


Thus neither the factorial endpoint nor either arctangent contribution has been omitted.

### 5.2 Paying every first-square integration denominator

Put


$$
\kappa_K=\left\lfloor\log_2(2N-1)\right\rfloor
=\left\lfloor\log_2(4K+1)\right\rfloor.
$$



There is one useful additional parity payment. Every odd coefficient of the square $\phi_N^2$ is even. Division by the even polynomial $1+t^2$ preserves this property, so


$$
[t^j]Q_\phi\equiv0\pmod2\qquad(j\text{ odd}).
\tag{5.5}
$$


For an even integration denominator $j+1$, its numerator therefore contains at least one factor of $2$. Odd denominators cost no dyadic division. Hence


$$
v_2\!\left(\int_0^1Q_\phi\right)\ge1-\kappa_K,
$$


and, since the factorial endpoint is integral,


$$
v_2(R_\phi)\ge3-\kappa_K.
$$


Here $\kappa_K\ge3$, as $N\ge5$.

Define the paid first-square depth


$$
\boxed{
L_K=u_K+3-\kappa_K
=N+2-s_2(N-2)-\lfloor\log_2(2N-1)\rfloor.
}
\tag{5.6}
$$


Then


$$
\boxed{v_2(aR_\phi)\ge L_K.}
\tag{5.7}
$$



For $K\ge2$, $4K+1<2^{K+2}$, so $\kappa_K\le K+1$. Together with $u_K\ge K$, this gives


$$
L_K\ge2.
\tag{5.8}
$$



This is a bound for the full first-square endpoint, with every allowed denominator paid.

### 5.3 The second-square pole

The already evaluated factorial endpoint can be written without successor $C$-values:


$$
C_0=1,\qquad C_r=rC_{r-1}+1,
$$




$$
\boxed{
B_g=\mathcal R_4(m)C_m+m^3+6m^2+18m+17.
}
\tag{5.9}
$$


This is the complete factorial functional of $g_N^2$, not an asymptotic approximation.

Since $m$ is even, $B_g$ is odd. This also follows immediately from the constant and linear coefficients of $g_N^2$.

Let


$$
s=v_2(N-1)=1+v_2(K).
$$


At $m=4K-2$,


$$
m^2+5m+8=2(8K^2+2K+1),
$$


while the denominator of $\beta_g$ is


$$
(4K-1)(4K)(4K+1).
$$


Therefore


$$
\boxed{v_2(\beta_g)=-s,\qquad v_2(4\beta_g)=2-s.}
\tag{5.10}
$$



If $s=1$, then $R_g$ is odd. If $s\ge3$, then the negative valuation of $4\beta_g$ strictly dominates $B_g$. Thus


$$
v_2(R_g)=
\begin{cases}
0,&s=1,\\
2-s,&s\ge3.
\end{cases}
\tag{5.11}
$$


By (5.7)–(5.8), the first-square term cannot cancel either of these valuations.

### 5.4 Passing through the actual least clearer and final gcd

Recall that $\lambda_N$ is the actual denominator of $\mathcal E_N$, and


$$
A_N=\lambda_N\mathcal E_N,\qquad
\mathfrak G_N=\gcd(M_N,|A_N|).
$$



If $s=1$, (5.4) gives $v_2(\mathcal E_N)=0$. Hence


$$
v_2(\lambda_N)=v_2(A_N)=v_2(\mathfrak G_N)=0.
$$



If $s\ge3$, then $v_2(\mathcal E_N)=2-s<0$. Hence


$$
v_2(\lambda_N)=s-2,\qquad
v_2(A_N)=v_2(\mathfrak G_N)=0.
$$



We have proved an actual primitive-denominator theorem.

### Theorem 5.1 — Final dyadic denominator outside $N\equiv5\pmod8$

For every odd $N\ge5$, put


$$
t_N=2N-2-s_2(N-2),\qquad s=v_2(N-1).
$$


Then


$$
\boxed{
\begin{array}{c|c|c|c}
\text{condition}&v_2(\lambda_N)&v_2(\mathfrak G_N)&v_2(q_N)\\ \hline
s=1&0&0&t_N\\
s\ge3&s-2&0&t_N+s-2.
\end{array}}
\tag{5.12}
$$



The odd part of $\mathfrak G_N$ is not asserted to be $1$. It is unnecessary to evaluate that odd part to prove the displayed dyadic factor of the already primitive $q_N$.

---

## 6. Paid classification of the remaining odd class

The remaining class is


$$
N\equiv5\pmod8.
$$


Write


$$
N=4l+1,\qquad l\text{ odd},\qquad K=2l,\qquad m=8l-2.
$$


Here $s=2$, so both $B_g$ and $4\beta_g$ are odd. Their cancellation must be evaluated rather than ignored.

### 6.1 An exact scalar endpoint function

Formula (2.1) gives


$$
4\beta_g
=\frac{32l^2+4l+1}{l(64l^2-1)}.
$$


Set


$$
\mathcal B(x)=\mathcal R_4(x)C(x)+x^3+6x^2+18x+17,
$$


where, for nonnegative integers $m$, $C(m)=C_m$.

Define


$$
\boxed{
\mathcal F(l)
=
l(64l^2-1)\mathcal B(8l-2)
-(32l^2+4l+1).
}
\tag{6.1}
$$


At every actual index in this class,


$$
\boxed{
R_g=\frac{\mathcal F(l)}{l(64l^2-1)}.
}
\tag{6.2}
$$


The denominator in (6.2) is odd.

To classify the depth of $\mathcal F(l)$, use the following rigorously convergent $2$-adic interpolation:


$$
C(x)=\sum_{r=0}^{\infty}(x)_r,
\qquad
(x)_r=x(x-1)\cdots(x-r+1),\quad (x)_0=1.
\tag{6.3}
$$


For $x\in\mathbb Z_2$,


$$
v_2((x)_r)\ge v_2(r!).
$$


This follows first for integers from divisibility by $r!$, and then by $2$-adic continuity. Thus the series converges uniformly.

At a nonnegative integer $m$, all terms with $r>m$ vanish and


$$
C(m)=\sum_{r=0}^m\frac{m!}{(m-r)!}=C_m.
$$


Therefore (6.3) does not introduce any additional moment or factorial into an actual finite construction.

Every $(x)_r$ is an integer polynomial, so


$$
C(x)-C(y)\in(x-y)\mathbb Z_2.
\tag{6.4}
$$


The same property holds for $\mathcal B$. In particular,


$$
\mathcal B(8l_1-2)-\mathcal B(8l_2-2)
\in8(l_1-l_2)\mathbb Z_2.
\tag{6.5}
$$


Moreover, $\mathcal B(8l-2)$ is odd for every $l\in\mathbb Z_2$.

### 6.2 An isometry and a unique root

Let


$$
A(l)=l(64l^2-1).
$$


For $d=l_1-l_2$,


$$
A(l_1)-A(l_2)
=d\bigl(64(l_1^2+l_1l_2+l_2^2)-1\bigr).
$$


The bracket is odd. Using (6.5) in the difference of (6.1), we find


$$
\frac{\mathcal F(l_1)-\mathcal F(l_2)}{l_1-l_2}
\equiv1\pmod2.
$$


Consequently


$$
\boxed{
v_2(\mathcal F(l_1)-\mathcal F(l_2))
=v_2(l_1-l_2).
}
\tag{6.6}
$$



Also


$$
\mathcal F(l)\equiv l+1\pmod2.
$$


There is therefore a unique $\zeta\in\mathbb Z_2$ with


$$
\mathcal F(\zeta)=0.
$$


This can be proved directly by lifting one bit at a time: replacing a candidate $a$ by $a+2^r$ changes $\mathcal F(a)$ by $2^r\pmod{2^{r+1}}$, so exactly one next bit gives a root modulo $2^{r+1}$.

From (6.2) and (6.6),


$$
\boxed{v_2(R_g)=v_2(l-\zeta).}
\tag{6.7}
$$



Thus the endpoint depth has been reduced to a single explicitly defined $2$-adic root, with a proved isometry and an effective lifting recurrence. It is not left as an unnamed cancellation in a large sum.

### 6.3 Initial root digits and explicit residue classes

For odd $l$, $8l-2\equiv6\pmod{16}$. The small exact values


$$
\mathcal R_4(6)=3420,\qquad C_6=1957,\qquad
6^3+6\cdot6^2+18\cdot6+17=557
$$


give


$$
\mathcal B(8l-2)\equiv9\pmod{16}.
$$


Hence


$$
\mathcal F(l)\equiv-13l-1\pmod{16},
$$


and therefore


$$
\boxed{\zeta\equiv11\pmod{16}.}
\tag{6.8}
$$



A slightly deeper bounded hand check gives


$$
\boxed{\zeta\equiv75\pmod{128}.}
\tag{6.9}
$$


Here is a checkable derivation. The recurrence for $C_m$ gives


$$
C_m=m(m-1)C_{m-2}+m+1.
$$


Induction modulo $32$ shows


$$
C_m\equiv
\begin{cases}
1\pmod{32},&m\equiv0\pmod4,\\
5\pmod{32},&m\equiv2\pmod4.
\end{cases}
$$


At $l=11$, $m=86$, so $C_{86}\equiv5\pmod{32}$. Direct polynomial reduction gives


$$
\mathcal R_4(86)\equiv124,\qquad
86^3+6\cdot86^2+18\cdot86+17\equiv13\pmod{128},
$$


and hence


$$
\mathcal B(86)\equiv121\pmod{128}.
$$


Also


$$
11(64\cdot11^2-1)\equiv53,\qquad
32\cdot11^2+4\cdot11+1\equiv77\pmod{128}.
$$


Thus


$$
\mathcal F(11)\equiv53\cdot121-77\equiv64\pmod{128}.
$$


By the isometry, $v_2(11-\zeta)=6$, proving (6.9).

### 6.4 The paid final-gcd classification

Let


$$
r_l=v_2(l-\zeta).
$$


In the class $N\equiv5\pmod8$, $R_g$ is $2$-integral and even. By (5.7), the first-square term has valuation at least $L_K\ge2$. Therefore $\mathcal E_N$ is $2$-integral, and


$$
v_2(\lambda_N)=0.
$$



If


$$
r_l<L_K,
\tag{6.10}
$$


the second-square endpoint has strictly smaller valuation than the complete paid first-square endpoint. Equation (5.4) then gives


$$
v_2(\mathcal E_N)=r_l.
$$


As $r_l<L_K<t_N$, the final gcd has exactly that dyadic depth:


$$
\boxed{
v_2(\lambda_N)=0,\qquad
v_2(\mathfrak G_N)=r_l,\qquad
v_2(q_N)=t_N-r_l.
}
\tag{6.11}
$$



This is a statement about the actual final gcd, not a polynomial-content estimate.

For example, (6.8) gives the uniform residue-class formulas


$$
\boxed{
\begin{array}{c|c}
\text{class}&v_2(q_N)\\ \hline
N\equiv5\pmod{16}&t_N-1\\
N\equiv29\pmod{32}&t_N-2\\
N\equiv13\pmod{64}&t_N-3.
\end{array}}
\tag{6.12}
$$


The corresponding depths $1,2,3$ are strictly below $L_K$ throughout those classes for $N\ge5$. The check (6.9) also gives $r_l=6$ when $l\equiv11\pmod{128}$, subject to the same explicitly checked inequality $6<L_K$.

### 6.5 A uniform surviving exponential factor on the classified odd indices

For $s=1$ or $s\ge3$, Theorem 5.1 gives


$$
v_2(q_N)\ge t_N\ge N.
$$


For $s=2$ and $r_l<L_K$,


$$
v_2(q_N)
=t_N-r_l
\ge t_N-L_K+1
=N+\kappa_K-3
\ge N.
$$


We have proved:

### Theorem 6.1 — Paid odd-index no-go classification

For odd $N\ge5$, suppose either

1. $N\not\equiv5\pmod8$; or
2. $N=4l+1\equiv5\pmod8$ and
   

$$
v_2(l-\zeta)<L_K.
$$



Then


$$
\boxed{2^N\mid q_N,}
\tag{6.13}
$$


and therefore


$$
\boxed{
\ell_N\ge
\frac{3\,2^N}{4(\mu_N+1)^2\,36^{\mu_N}}
\longrightarrow+\infty
}
\tag{6.14}
$$


along every unbounded sequence of such indices.

In particular, $N-1=2^s$, $s\ge3$, is completely excluded as a source of vanishing primitive errors.

The possible remaining odd indices must satisfy the very restrictive condition


$$
\boxed{
N=4l+1,\quad l\text{ odd},\qquad
v_2(l-\zeta)\ge
4l+2-s_2(2l-1)-\lfloor\log_2(8l+1)\rfloor.
}
\tag{6.15}
$$


No theorem ruling out infinitely many such integers is claimed.

---

## 7. Application at every prescribed original index

Now return to the exact original domain


$$
N=9^{18+32u}=81^{9+16u},\qquad u\ge0.
$$


Let


$$
k=9+16u.
$$


The integer $k$ is odd, and


$$
N-1=80(1+81+\cdots+81^{k-1}).
$$


The parenthesized sum is odd. Consequently


$$
\boxed{v_2(N-1)=4,\qquad 5\mid N-1.}
\tag{7.1}
$$



Two consequences must be distinguished.

- The fixed odd-prime theorem (2.2), with $p=5$, already excludes the entire prescribed sequence once combined with (2.5). Thus “all odd divisors of $N-1$ moving to infinity” does not occur inside this original domain.
- The new ramified theorem gives a separate exact dyadic evaluation, without relying on an odd unit rotation.

At these indices, Theorem 5.1 gives


$$
v_2(\lambda_N)=2,\qquad
v_2(A_N)=v_2(\mathfrak G_N)=0.
$$


Together with (4.12),


$$
\boxed{
\begin{array}{c|c}
\text{actual quantity}&2\text{-adic valuation}\\ \hline
d_N&3(N-1)/2\\
\Delta,D&2N-2\\
h_N&4N-4\\
M_N&T_N:\quad 2N-2-s_2(N-2)\\
\lambda_N&2\\
\mathfrak G_N&0\\
q_N&2N-s_2(N-2).
\end{array}}
\tag{7.2}
$$


In the $M_N$ row, the displayed expression means
$v_2(M_N)=v_2(T_N)=2N-2-s_2(N-2)$.

In particular,


$$
q_N\ge2^{2N-s_2(N-2)}.
\tag{7.3}
$$



Here


$$
\sqrt N=9^{9+16u}
$$


is an integer greater than $64$, so


$$
\mu_N=16\sqrt N.
$$


Equations (2.6) and (7.3) prove (B).

### 7.1 An explicit all-original-index bound greater than $1$

No enormous original-index arithmetic is needed.

Write $x=\sqrt N$. The digit bound


$$
2^{s_2(N-2)}\le2(N-2)
$$


and $36<2^6$ give


$$
\ell_N>
\frac{3\,2^{\,2x^2-96x}}{2312x^4}.
$$


For integer $x\ge64$,


$$
2x^2-96x\ge32x,\qquad x^4\le2^{2x},\qquad2312<2^{12}.
$$


Therefore


$$
\boxed{
\ell_N>3\cdot2^{30\sqrt N-12}>1
\qquad
\text{for every }N=9^{18+32u}.
}
\tag{7.4}
$$



This is a strict lower bound on the **whole nonzero primitive error**, at every original index, after the final all-prime gcd.

### 7.2 What this proves and what it does not

It proves that this specified minimizing-plus-second-square producer cannot yield


$$
0<q_N(e+\pi)-p_N\longrightarrow0
$$


on any infinite subset of the prescribed original domain.

It does **not** prove that $e+\pi$ is rational. Nor does it disprove irrationality. Ordinary rational approximations can converge while their primitive errors grow; that is exactly the arithmetic obstruction here.

The original-domain no-go is complete for this producer. The global rationality question requires a different successful construction or a different argument.

---

## 8. Exact remaining obligations outside the prescribed domain

### 8.1 The broader odd-$N$ extension

For a hypothetical vanishing-error sequence of odd indices outside the prescribed domain, the proved results force both of the following:

1. For every fixed odd prime $p$, eventually $p\nmid N-1$, by (2.2) and the root-exponential lower bound.
2. Eventually $N=4l+1\equiv5\pmod8$ and the exceptional root condition (6.15) holds.

The power-of-two case $N-1=2^s$ is no longer open: Theorem 5.1 excludes it for all growing $s$.

A concrete follow-on lemma is therefore:

> **Open dyadic digit-gap lemma.**  
> For all sufficiently large positive odd integers $l$,
> 

$$
> v_2(l-\zeta)
> <
> 4l+2-s_2(2l-1)-\lfloor\log_2(8l+1)\rfloor.
> \tag{8.1}
>
$$



If proved, this lemma would complete the no-go theorem for all sufficiently large odd $N$ in the two-square extension.

The isometry and the root’s existence do not prove (8.1). A $2$-adic root can, in principle, have long digit gaps; a finite root computation cannot establish an eventual gap bound.

### 8.2 The exact endpoint bottleneck at exceptional indices

If (6.15) holds, both summands in


$$
\mathcal E_N
=
\frac{T_Nd_N^2}{h_N}R_\phi
+
\frac{D\Delta}{h_N}R_g
\tag{8.2}
$$


are divisible by a large power of $2$. Their **further cancellation** is then the unresolved dyadic issue. The earlier dominance argument no longer applies.

One alternative follow-on lemma would directly bound


$$
v_2(\mathcal E_N)\le t_N-N
$$


eventually on these exceptional indices. Because $v_2(\lambda_N)=0$ there, that would imply $v_2(q_N)\ge N$.

Neither such bound is proved here.

Even if exceptional indices produced favorable dyadic cancellation, success would still require control of all other primes in $\lambda_NM_N/\mathfrak G_N$ and the complete quantity $q_NJ_N$. A saving at $2$ alone would not prove primitive decay.

The even-$N$ extension is not classified by the present ramified theorem. It is outside the prescribed original domain, which consists entirely of odd $N$.

---

## 9. Non-transfer to the other finite producers

The conclusions above concern only the fixed two-square family.

The old binary producer retains


$$
b=9^{18+32u},\qquad n=4002b,
$$


contact range $0,\ldots,b-1$, reconstruction range $0,\ldots,b$, and physical terminal


$$
z_b=0.
$$


Its complete corrected columns remain


$$
x=\frac12RA^{-1}f,\qquad
y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},\qquad x=2^ax_0,
$$


and its complete return remains


$$
S=\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f.
$$


The retained paid statement


$$
v_2\!\left(\frac{S}{2^{a+1}}\right)\ge\chi-a,
\qquad
\chi=v_2\binom{n+b-1}{b-1},
$$


is not used as a theorem about the present $q_N$. Conversely, the new dyadic theorem does not evaluate that producer’s corrected-column contents or final gcd.

The compact pencil also retains its original finite domain


$$
0\le m<2k,\qquad0\le j<k,\qquad m+j\le3k-2,
$$


with


$$
c_n=a_{2n}-(-1)^n,\qquad
r_n=-(2n)!+4\rho_n,
\qquad
\rho_0=0,\quad \rho_{n+1}+\rho_n=\frac1{2n+1},
$$


and


$$
H_k(s)=
\det[C\mid\Lambda_k\mathcal R+s\Lambda_kwv^T],
\qquad
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5).
$$


No content or final-gcd theorem is transferred to that matrix.

The supplied $N=8$ receipt remains a finite certificate only. Neither its contents nor $\mathfrak G_8=1$ has been used to infer the results above.

---

## 10. Bounded new exact-arithmetic checks

No machine computation is needed for Theorems 4.1, 5.1, 6.1, or the original-index obstruction. The following are optional **new finite diagnostics**, not substitutes for those proofs. No such computation has been performed here.

### 10.1 A finite normalization receipt for the new dyadic cases

Use exactly


$$
N\in\{5,7,9,13,17,21,29,45\}.
$$


These values do not include the closed $N=8$ calculation.

#### Bounded inputs

- $H_0=1,H_1=t$ and recurrence (3.1), only through $H_N$;
- $E_j=(N!/j!)H_j$, $0\le j\le N$;
- all definitions in Section 1;
- moments and factorials only through $2N$.

Across the entire test:

- maximum basis degree: $45$;
- maximum final degree and factorial index: $90$;
- maximum quotient degree: $88$;
- maximum affine denominator: $89$;
- maximum $J_N$-integration denominator: $91$.

#### Expected verifiable outputs

1. Complete source data, $\Phi$, and the raw and primitive coefficient vectors.
2. Actual $d_N,h_N,M_N$, with polynomial-content Bézout certificates.
3. The identities
   

$$
W_N(i)=M_N,\qquad
   \sum_{d=0}^{2N}[t^d]W_N\,a_d=M_N.
$$


4. The full quotient identity
   

$$
(1+t^2)S_N=W_N-M_N.
$$


5. Actual $L_{\mathrm{ent},N}$, summed cancellation, least $\lambda_N$, $A_N$, final all-prime $\mathfrak G_N$, and primitive $p_N,q_N$, with gcd certificates.
6. The following predicted dyadic valuations:



$$
\begin{array}{c|r|r|r|r}
N&t_N=v_2(M_N)&v_2(\lambda_N)&v_2(\mathfrak G_N)&v_2(q_N)\\ \hline
5&6&0&1&5\\
7&10&0&0&10\\
9&13&1&0&14\\
13&21&0&3&18\\
17&28&2&0&30\\
21&37&0&1&36\\
29&52&0&2&50\\
45&84&0&6&78
\end{array}
$$



The $N=45$ prediction uses the proved finite congruence
$v_2(11-\zeta)=6$ and $L_{22}=37$.

7. Exact rational $q_NJ_N$ and the complete interval
   

$$
3q_NJ_N\le q_N(e+\pi)-p_N\le7q_NJ_N.
$$



These outputs establish only the listed finite normalizations.

### 10.2 A bounded root-lifting diagnostic

If a further root prefix is desired, take precision $2^{12}$.

Because $v_2(16!)=15\ge12$, uniformly on $\mathbb Z_2$,


$$
C(x)\equiv\sum_{r=0}^{15}(x)_r\pmod{2^{12}}.
$$


The sixteen falling-factorial terms are computed without division:


$$
P_0(x)=1,\qquad P_{r+1}(x)=(x-r)P_r(x).
$$



Use this finite polynomial in (6.1), and lift the unique root through twelve bits.

The expected output is:

- the unique odd integer $z_{12}\in[0,4095]$ with
  $\mathcal F(z_{12})\equiv0\pmod{4096}$;
- the check $z_{12}\equiv75\pmod{128}$;
- the successive bit-lift residues;
- exact verification of the change by $2^r\pmod{2^{r+1}}$ at each step.

This calculation would certify only a twelve-bit root prefix. It would not prove the open digit-gap lemma (8.1).

---

## Final assessment

### New proved result

A division-paid ramified block recurrence has been derived for the actual Laguerre evaluations at $1-i$. It evaluates, for every odd $N\ge5$,

- the dyadic source Gram valuations;
- the actual $\Phi$-content depth;
- the actual raw-polynomial content depth;
- the least polynomial-clearer depth.

The complete endpoint analysis then evaluates the least affine clearer and final dyadic gcd outside $N\equiv5\pmod8$, and gives a precise root-based classification inside that class.

At every prescribed original index,


$$
\boxed{
v_2(q_N)=2N-s_2(N-2),\qquad
q_N(e+\pi)-p_N>1,
}
$$


with the whole primitive error tending to $+\infty$.

### Proof status

This is an **unconditional no-go theorem for the specified two-square producer on its entire prescribed original domain**. It is not inferred from finite computations and does not depend on the closed $N=8$ normalization.

### Remaining mathematical bottleneck

There is no remaining arithmetic obligation needed to establish this original-domain failure.

For the broader odd-$N$ extension, the remaining dyadic issue is the exceptional root-closeness condition (6.15) and the complete endpoint cancellation (8.2). A bounded root computation cannot settle that infinite obligation. The even-$N$ extension and any favorable all-prime normalization there also remain untreated.

For the global objective, the conclusion remains unchanged:



$$
\boxed{\text{Neither rationality nor irrationality of }e+\pi\text{ has been proved.}}
$$



The present branch must obtain a genuinely different successful mechanism, rather than seek primitive decay from this fixed two-square family at the prescribed indices.
