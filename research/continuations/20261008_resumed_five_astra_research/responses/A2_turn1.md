> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent referee report on the full-degree two-square construction

## Executive conclusion

The attached work does **not** decide whether $e+\pi$ is rational or irrational.

My conclusions are as follows.

1. **The full-degree two-square producer is mathematically valid.** Its exponential source, odd arctangent source, $\log 2$ cancellation, real rational minimizer, strict positivity, and paid primitive normalization all have correct proofs at the stated degrees.

2. **The Chebyshev comparison is valid, including its complex phases.** In particular, the determinant used to impose the two real conditions at $i$ does not vanish. The resulting stretched-exponential bound is an ordinary-error bound; it is not a primitive-error decay theorem.

3. **The $N=8$ receipt is a finite normalization certificate, not evidence for an infinite-index conclusion.** Independent reductions below establish its actual polynomial content and final all-prime gcd:
   

$$
h_8=2^{40}3^2=9\,895\,604\,649\,984,\qquad \mathfrak G_8=1.
$$


   They also distinguish the two endpoint primes:
   

$$
11\nmid\lambda_8,\qquad 13\mid\lambda_8.
$$


   Indeed, $11$ nevertheless survives in $q_8$, through $M_8$.

4. **The construction is not a new parameterization of the entire common-kernel lattice.** That was already established in the Stein/Robin source. What is new in the proposed producer is the specified minimizing polynomial plus the specified second square.

5. **A new uniform arithmetic theorem is proved here for this exact ansatz.** It gives an exact content formula and evaluates the auxiliary moment gcd that controls exceptional content cancellation. Writing
   

$$
d_N=\operatorname{cont}(\Phi),\qquad
   \phi_N=\Phi/d_N,\qquad
   a_N^\circ=\phi_N(0),
$$


   and
   

$$
c_N=\operatorname{cont}\bigl(\phi_N-a_N^\circ g_N\bigr),
$$


   one has, for every $N\ge3$,
   

$$
\boxed{c_N\mid 4(N-2)!}
   \tag{E.1}
$$


   and, for every $N\ge2$,
   

$$
\boxed{
   h_N=
   \gcd\!\left(
      T_Nd_N^2(a_N^\circ)^2+D\Delta,\,
      T_Nd_N^2c_N\gcd(2,c_N)
   \right).
   }
   \tag{E.2}
$$


   Consequently, at every odd prime $p>N-2$,
   

$$
\boxed{
   v_p(h_N)=
   \min\!\left(v_p(T_N)+2v_p(d_N),\,
                    v_p(D)+v_p(\Delta)\right).
   }
   \tag{E.3}
$$


   Thus the previously unevaluated possibility of *extra* raw-polynomial content is confined to small primes. This is an all-degree theorem, not an extrapolation from $N=8$.

6. A second new calculation evaluates the complete second-square rational endpoint and gives an explicit criterion for whether certain factorial primes enter the **final** gcd. This makes the remaining arithmetic question more specific, but it does not settle primitive decay or failure.

The unresolved quantity remains the actual, fully normalized expression


$$
\boxed{
q_NJ_N
=
\frac{\lambda_NT_N\Delta^2}{h_N\mathfrak G_N}\,
\int_0^1P_N(t)\,dt
}
$$


on an infinite subset of


$$
\boxed{N=9^{18+32u},\qquad u\ge0.}
$$



---

## 1. Scope, original indices, and non-transfer of other producers

Throughout this report the producer under audit has

- basis indices $0,\ldots,N$;
- admissible minimizing polynomials of degree at most $N$;
- final polynomial degree exactly $2N$;
- exponential moments and factorial endpoints only through degree $2N$;
- arctangent quotient degree $2N-2$;
- quotient denominators only through $2N-1$.

The unweighted diagnostic $J_N=\int_0^1P_N$ can involve denominators through $2N+1$. This does **not** introduce a successor exponential moment or factorial.

The construction is defined for every $N\ge2$, and the stated Chebyshev estimate is proved for $N\ge64$. Accordingly, every such theorem applies pointwise at the required original indices


$$
N=b(u)=9^{18+32u},\qquad u\ge0.
$$


The auxiliary values $N=3$ and $N=8$ are not original-index instances.

### 1.1 Objects from the old binary producer are not modified

The old binary producer retains


$$
b=9^{18+32u},\qquad n=4002b,
$$


contact range $0,\ldots,b-1$, reconstruction range $0,\ldots,b$, and physical terminal


$$
z_b=0.
$$


Its complete corrected columns are


$$
x=\frac12RA^{-1}f,\qquad
y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},\qquad x=2^ax_0,
$$


and its complete return is


$$
S=\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f.
$$


The stated paid valuation


$$
v_2\!\left(\frac{S}{2^{a+1}}\right)\ge \chi-a,
\qquad
\chi=v_2\binom{n+b-1}{b-1},
$$


does not become a valuation theorem for the new $q_N$.

Likewise, the compact matrix retains


$$
0\le m<2k,\quad 0\le j<k,\quad m+j\le3k-2,
$$


and its original pencil


$$
H_k(s)=
\det[C\mid\Lambda_k\mathcal R+s\Lambda_kwv^T],
\qquad
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5).
$$


Nothing below evaluates its final content.

The reported no-go theorem for the separate Laguerre matrix, and the reported finite compact counterexample, are not used as theorems about this construction. Their full underlying objects and certificates are not supplied here for a fresh independent audit.

### 1.2 Reuse of the Stein/Robin result

For an integer polynomial $F$, the supplied Stein/Robin theorem already parameterizes the entire lattice


$$
\int F\,d\eta=F(i)=F(-i)\in\mathbb Z.
$$


It therefore applies to the integer polynomial $W_N$ constructed below.

That established theorem is reused, not reproved. In particular, a claim that the present work newly parameterizes the *whole* common-kernel mechanism would be incorrect. The specific minimizing-plus-second-square choice is the object requiring independent review.

---

## 2. Audit of all three source channels

Set


$$
d\eta(t)=e^{t-1}\mathbf1_{(-\infty,1]}(t)\,dt.
$$



### 2.1 Exponential source

Integration by parts gives


$$
a_d:=\int_{-\infty}^1t^d\,d\eta(t),\qquad
a_0=1,\qquad a_d=1-da_{d-1}.
$$


Hence every $a_d$ is an integer.

Repeated integration by parts on $[0,1]$, with the lower endpoint retained, gives


$$
\boxed{
\int_0^1e^tt^d\,dt=e\,a_d-(-1)^dd!.
}
\tag{2.1}
$$


The factorial term is the complete lower-endpoint contribution.

### 2.2 Arctangent and odd-power $\log 2$ sources

Let


$$
\xi_d=\Re(i^d),\qquad \zeta_d=\Im(i^d),
$$


and


$$
\sigma_0=\sigma_1=0,\qquad
\sigma_d=\frac1{d-1}-\sigma_{d-2}\quad(d\ge2).
$$


The initial cases are


$$
4\int_0^1\frac{dt}{1+t^2}=\pi,\qquad
4\int_0^1\frac{t\,dt}{1+t^2}=2\log2.
$$


Using


$$
\frac{t^d}{1+t^2}
=t^{d-2}-\frac{t^{d-2}}{1+t^2}
$$


then proves


$$
\boxed{
4\int_0^1\frac{t^d}{1+t^2}\,dt
=\pi\xi_d+2\log2\,\zeta_d+4\sigma_d.
}
\tag{2.2}
$$


Thus the full mixed moment is


$$
\int_0^1t^d\left(e^t+\frac4{1+t^2}\right)dt
=
e\,a_d+\pi\xi_d+2\log2\,\zeta_d
-(-1)^dd!+4\sigma_d.
$$



There is no missing odd-power source.

### 2.3 Contact and exact source cancellation

Suppose $P\in\mathbb Q[t]$ satisfies


$$
\int P\,d\eta=1,\qquad P(i)=1.
$$


Reality of its coefficients gives $P(-i)=1$, so


$$
P=1+(1+t^2)S_P,\qquad S_P\in\mathbb Q[t].
$$


Writing


$$
B(P)=\sum_d[t^d]P\,(-1)^dd!,
$$


equations (2.1)–(2.2) yield


$$
\boxed{
\int_0^1P(t)\left(e^t+\frac4{1+t^2}\right)dt
=
e+\pi-
\left(B(P)-4\int_0^1S_P(t)\,dt\right).
}
\tag{2.3}
$$


The $\log2$ coefficient vanishes because it is $2\Im P(i)$, not because the odd terms were discarded.

For later comparison, put


$$
w(t)=e^t+\frac4{1+t^2}.
$$


On $[0,1]$,


$$
3\le w(t)<7.
\tag{2.4}
$$



**Verdict:** the complete source identities and cancellation are accepted.

---

## 3. Audit of the rational minimizer and both squares

### 3.1 Integral basis and kernel normalization

Let


$$
Q_j(t)=L_j(1-t),\qquad E_j(t)=N!Q_j(t).
$$


The classical Laguerre orthogonality, under $y=1-t$, gives


$$
\int Q_jQ_k\,d\eta=\delta_{jk},\qquad
\int E_jE_k\,d\eta=(N!)^2\delta_{jk}.
$$


This is being used on the full polynomial space of degree at most $N$, not on an even-index subspace.

A useful integral monic basis is


$$
H_j(t)=j!L_j(1-t).
$$


It satisfies


$$
H_0=1,\qquad H_1=t,\qquad
H_{j+1}=(t+2j)H_j-j^2H_{j-1}.
\tag{3.1}
$$


Thus $H_j$ is monic and integral, and


$$
E_j=\frac{N!}{j!}H_j.
$$



Write


$$
E_j(i)=\alpha_j+i\beta_j,
$$


and retain the exact source integers


$$
\mathsf U=\sum\alpha_j^2,\quad
\mathsf V=\sum\alpha_j\beta_j,\quad
\mathsf W=\sum\beta_j^2,
$$




$$
\Delta=\mathsf U\mathsf W-\mathsf V^2,\qquad B=(N!)^2.
$$


Since $E_0=N!$ and $E_1=N!t$, the two evaluation vectors are independent. Hence $\Delta>0$.

Define


$$
\Phi=\sum_{j=0}^N(\mathsf W\alpha_j-\mathsf V\beta_j)E_j.
$$


Then


$$
\Phi(i)=\Delta,\qquad
\int\Phi^2\,d\eta=B\mathsf W\Delta.
$$


Consequently


$$
f_N=\frac{\Phi}{\Delta},\qquad
\tau_N=\int f_N^2\,d\eta=\frac{B\mathsf W}{\Delta}.
$$



### 3.2 The real rational minimum

Writing $f=\sum c_jE_j$, the condition $f(i)=1$ is exactly


$$
\sum\alpha_jc_j=1,\qquad \sum\beta_jc_j=0.
$$


The norm is $B\sum c_j^2$. The unique Euclidean constrained minimum is


$$
c_j=\frac{\mathsf W\alpha_j-\mathsf V\beta_j}{\Delta}.
$$


This proves the stated minimizing property, with rational coefficients.

The admissible polynomial


$$
\frac{5-t^2}{6}
$$


has norm $2/3$, because $a_2=1$ and $a_4=9$. Therefore


$$
\tau_N\le\frac23,\qquad
D:=\Delta-B\mathsf W>0.
\tag{3.2}
$$



The minimizer also satisfies the useful orthogonality condition


$$
\boxed{
\int f_Nk\,d\eta=0
\quad
\text{if }\deg k\le N,\ k(i)=0,\ k\in\mathbb R[t].
}
\tag{3.3}
$$


Indeed, $f_N+\varepsilon k$ is admissible for every real $\varepsilon$, and differentiation of its squared norm at $\varepsilon=0$ gives (3.3).

### 3.3 The second square and strict positivity

Take exactly


$$
g_N=(1+t^2)(1-t)^{N-2}.
$$


It is primitive, integral, of degree $N$, and vanishes at $i,-i$.

With $y=1-t$,


$$
g_N=y^{N-2}(y^2-2y+2).
$$


Its norm is exactly


$$
\boxed{
T_N=(2N)!-4(2N-1)!+8(2N-2)!
-8(2N-3)!+4(2N-4)!.
}
\tag{3.4}
$$


This is positive because it is the integral of a nonzero square.

The specified producer is


$$
P_N=f_N^2+\frac{1-\tau_N}{T_N}g_N^2.
$$


It satisfies


$$
P_N(i)=1,\qquad \int P_N\,d\eta=1.
$$


Moreover,


$$
P_N(t)>0\qquad(0\le t<1),
$$


because $1-\tau_N\ge1/3$ and $g_N(t)>0$ there.

The degree is exactly $2N$: the second square has a strictly positive coefficient multiplying its degree-$2N$ leading term, and a sum of real squares cannot cancel that term.

**Verdict:** the minimizer, the exact second-square norm, both contact conditions, and strict positivity are accepted.

---

## 4. Paid contents, clearers, final gcd, and whole error

The raw objects must remain


$$
\mathscr W_N=T_N\Phi^2+D\Delta g_N^2,\qquad
\mathscr Z_N=T_N\Delta^2.
\tag{4.1}
$$


No cancellation in this formula is presumed.

Let


$$
h_N=\operatorname{cont}(\mathscr W_N).
$$


Since $\mathscr W_N(i)=\mathscr Z_N$, one has $h_N\mid\mathscr Z_N$. Define


$$
W_N=\mathscr W_N/h_N,\qquad
M_N=\mathscr Z_N/h_N.
$$


Then $W_N$ is primitive and


$$
P_N=W_N/M_N.
$$


It follows that $M_N$ is exactly the least positive simultaneous coefficient clearer of $P_N$.

For comparison, the actual clearer of $f_N$ alone is


$$
\frac{\Delta}{\operatorname{cont}(\Phi)}.
$$


Its square has the square of this clearer. The second-square coefficient has its own reduced denominator. Neither individual reduction licenses replacing the actual content $h_N$ of their sum.

Monic division gives the complete integer quotient


$$
S_N=\frac{W_N-M_N}{1+t^2}
=\sum_{j=0}^{2N-2}s_jt^j.
$$


Retain the full factorial endpoint


$$
B_{\mathrm{end},N}
=\sum_{d=0}^{2N}w_d(-1)^dd!.
$$



The least clearer of the **individual** terms $4s_j/(j+1)$ is


$$
L_{\mathrm{ent},N}
=\operatorname{lcm}_{0\le j\le2N-2}
\frac{j+1}{\gcd(j+1,4s_j)}.
$$


After summing, there can be further cancellation:


$$
J_{\mathrm{arc},N}
=\sum_j\frac{4s_jL_{\mathrm{ent},N}}{j+1},
$$




$$
d_{\mathrm{arc},N}
=\gcd(L_{\mathrm{ent},N},J_{\mathrm{arc},N}),\qquad
\lambda_N=L_{\mathrm{ent},N}/d_{\mathrm{arc},N}.
$$


Thus


$$
A_N=\lambda_NB_{\mathrm{end},N}
-J_{\mathrm{arc},N}/d_{\mathrm{arc},N}
$$


is integral and


$$
\gcd(\lambda_N,A_N)=1.
$$



The actual final all-prime gcd is


$$
\boxed{
\mathfrak G_N
=\gcd(\lambda_NM_N,|A_N|)
=\gcd(M_N,|A_N|).
}
\tag{4.2}
$$


Consequently


$$
\boxed{
q_N=\frac{\lambda_NM_N}{\mathfrak G_N},\qquad
p_N=\frac{A_N}{\mathfrak G_N}.
}
\tag{4.3}
$$


In particular, $\lambda_N\mid q_N$.

Finally, (2.3) proves the complete error identity


$$
\boxed{
\ell_N=q_N(e+\pi)-p_N
=\frac{\lambda_N}{\mathfrak G_N}
 \int_0^1W_N(t)w(t)\,dt
=q_N\int_0^1P_N(t)w(t)\,dt>0.
}
\tag{4.4}
$$


This is the whole evaluated error, not a selected channel.

**Verdict:** the normalization definitions and deductions are accepted. Merely defining $h_N$ and $\mathfrak G_N$, however, does not constitute a uniform evaluation of them.

---

## 5. Audit of the analytic Chebyshev comparison

The complex phase calculation is important enough to check explicitly.

For $r=N,N-1$, put


$$
R_r(t)=T_r\!\left(1-\frac{1-t}{8N}\right).
$$


With $y=1-t$, the argument lies in $[-1,1]$ for $0\le y\le16N$. Beyond that interval,


$$
\left|T_r\!\left(1-\frac y{8N}\right)\right|
\le \left(\frac y{4N}\right)^r.
$$


Therefore


$$
\|R_r\|_\eta^2
\le1+\frac{(2r)!}{(4N)^{2r}}
\le1+\left(\frac r{2N}\right)^{2r}
\le2.
\tag{5.1}
$$



At $t=i$, write


$$
z=1-\delta+i\delta=\cosh(\alpha+i\theta),
\qquad \delta=\frac1{8N},
$$


with $\alpha>0$ and $0<\theta<\pi/2$.

Setting $s=\sinh^2\alpha$, elimination of $\theta$ gives


$$
s^2+2\delta(1-\delta)s-\delta^2=0,
$$


hence


$$
s=\frac{\delta}
{\sqrt{1+(1-\delta)^2}+1-\delta}.
$$


The stated denominator bounds imply


$$
\frac1{20N}<s<\frac1{16N},
$$


and therefore


$$
\frac1{5\sqrt N}\le\alpha\le\frac1{4\sqrt N},
\qquad
\sin\theta=\frac{\delta}{\sinh\alpha}
\ge\frac1{2\sqrt N}.
\tag{5.2}
$$



Let


$$
a_r=\Re T_r(z),\qquad b_r=\Im T_r(z).
$$


Because


$$
T_r(z)=\cosh(r\alpha)\cos(r\theta)
+i\sinh(r\alpha)\sin(r\theta),
$$


direct product-to-sum calculation gives


$$
\begin{aligned}
\mathcal D
&=a_Nb_{N-1}-a_{N-1}b_N\\
&=-\frac12\left[
\sinh((2N-1)\alpha)\sin\theta
+\sinh\alpha\sin((2N-1)\theta)
\right].
\end{aligned}
\tag{5.3}
$$


Thus the oscillatory second term is retained.

For $N\ge64$,


$$
(2N-1)\alpha\ge2,\qquad
\sinh\alpha\le\frac12\sin\theta.
$$


Writing $x=(2N-1)\alpha$, it follows that


$$
|\mathcal D|
\ge\frac{\sin\theta}{2}\left(\sinh x-\frac12\right)
\ge\frac{\sin\theta}{8}e^x
\ge\frac{e^{(2N-1)\alpha}}{16\sqrt N}.
\tag{5.4}
$$


The elementary middle inequality holds for $x\ge2$.

Hence


$$
F=
\frac{b_{N-1}R_N-b_NR_{N-1}}{\mathcal D}
$$


is admissible. Its coefficients are rational: $z\in\mathbb Q(i)$, and Chebyshev polynomials have rational coefficients.

Using $|b_r|\le e^{r\alpha}$, the sum of the absolute values of the two displayed coefficients is at most


$$
32\sqrt N\,e^{-(N-1)\alpha}.
$$


Together with (5.1),


$$
\|F\|_\eta^2
\le2048N e^{-2(N-1)\alpha}
\le2048N e^{-\sqrt N/3}.
$$


The last inequality follows from $6(N-1)\ge5N$, valid for $N\ge6$.

The minimum property therefore proves


$$
\boxed{
\tau_N\le2048N e^{-\sqrt N/3}\qquad(N\ge64).
}
\tag{5.5}
$$



### 5.1 Conversion to the whole error

On $[0,1]$,


$$
\frac{w(t)}{e^{t-1}}\le5e<15.
$$


Also,


$$
g_N(t)^2\le4(1-t)^{2N-4},
$$


and


$$
T_N\ge\left(1-\frac2N\right)(2N)!\ge\frac12(2N)!
\qquad(N\ge4).
$$


These give the asserted upper bound


$$
\int_0^1P_Nw
\le2^{15}N e^{-\sqrt N/3}\qquad(N\ge64).
$$


For the small factorial remainder used in this estimate, one may note that


$$
e^{\sqrt N/3}\le2^N\le(2N)!
$$


and $N(2N-3)\ge56$ in the relevant range.

Conversely, $1-\tau_N\ge1/3$, $w\ge3$, and


$$
g_N^2\ge(1-t)^{2N-4}
$$


give the strict lower bound


$$
\int_0^1P_Nw>\frac1{(2N-3)T_N}.
$$


Thus


$$
\boxed{
\frac{q_N}{(2N-3)T_N}
<
\ell_N
\le
2^{15}q_NN e^{-\sqrt N/3}.
}
\tag{5.6}
$$



For


$$
J_N=\int_0^1P_N(t)\,dt>0,
$$


equation (2.4) gives


$$
\boxed{3q_NJ_N\le\ell_N\le7q_NJ_N.}
\tag{5.7}
$$



**Verdict:** the analytic argument is accepted. Its exact obstruction is arithmetic multiplication by the actual $q_N$.

The source height bound


$$
q_N\le
(2N-1)!(2N)!(N+1)^4(N!)^8\,3^{8N}
$$


also follows from the stated elementary coefficient estimates. It yields


$$
\log q_N\le12N\log N+O(N),
$$


which is much too large to imply decay from (5.6).

---

## 6. New uniform theorem: exact content reduction and an evaluated moment gcd

This section supplies the principal new all-degree arithmetic result.

### Theorem 6.1 — Exact content formula for the specified two-square ansatz

Let $N\ge2$, and use exactly the producer defined above. Set


$$
d_N=\operatorname{cont}(\Phi),\qquad
\phi_N=\Phi/d_N,\qquad a_N^\circ=\phi_N(0),
$$




$$
c_N=\operatorname{cont}(\phi_N-a_N^\circ g_N).
$$


Then $c_N>0$, and


$$
\boxed{
h_N=
\gcd\!\left(
T_Nd_N^2(a_N^\circ)^2+D\Delta,\,
T_Nd_N^2c_N\gcd(2,c_N)
\right).
}
\tag{6.1}
$$



For every $N\ge3$,


$$
\boxed{
c_N\mid4(N-2)!.
}
\tag{6.2}
$$


Moreover,


$$
c_N\mid\frac{\Delta}{d_N},
\qquad
c_N\mid\phi_N(1)\quad(N\ge3).
\tag{6.3}
$$



#### Proof of the exact content formula

Suppress the subscript $N$, and put


$$
a=\phi(0),\qquad c=\operatorname{cont}(\phi-ag).
$$


Since $\phi(i)=\Delta/d\ne0$ and $g(i)=0$, the polynomial $\phi-ag$ is nonzero. Thus $c>0$.

Because $g(0)=1$ and $\phi$ is primitive,


$$
\gcd(a,c)=1.
\tag{6.4}
$$


Indeed, a common prime divisor would divide every coefficient of $\phi$.

Next,


$$
\operatorname{cont}(\phi+ag)=\gcd(2,c).
\tag{6.5}
$$


To prove this, an odd prime dividing all coefficients of $\phi+ag$ would divide its constant coefficient $2a$, then $a$, and then all coefficients of $\phi$, a contradiction. A factor $4$ in its content is likewise impossible: its constant coefficient would force $a$ even and then every coefficient of $\phi$ even. Finally, divisibility of all coefficients by $2$ is equivalent for $\phi+ag$ and $\phi-ag$.

Gauss’s lemma now gives


$$
\operatorname{cont}(\phi^2-a^2g^2)
=c\gcd(2,c).
\tag{6.6}
$$



Write


$$
A=T d^2,\qquad B_0=D\Delta.
$$


Then


$$
\mathscr W=A\phi^2+B_0g^2.
$$


Its constant coefficient is $Aa^2+B_0$. Subtracting this constant coefficient times the coefficient vector of $g^2$ leaves


$$
A(\phi^2-a^2g^2).
$$


Since $g^2(0)=1$, this coefficient operation preserves the gcd of the coefficient vector. Equation (6.1) follows from (6.6). ∎

### 6.1 The evaluated moment gcd

Put


$$
n=N-2,\qquad
\mathcal R_4(x)=x^4+6x^3+19x^2+22x+12.
$$


For $0\le j\le n$, use the admissible kernel polynomial


$$
k_j(t)=(1+t^2)(1-t)^j.
$$


Equation (3.3) gives


$$
\int\phi_Nk_j\,d\eta=0.
$$


Writing


$$
\phi_N=a_N^\circ g_N+c_NR_N,\qquad R_N\in\mathbb Z[t],
$$


and using integrality of all $\eta$-moments, we obtain


$$
c_N\mid a_N^\circ\int g_Nk_j\,d\eta.
$$


By (6.4),


$$
c_N\mid\int g_Nk_j\,d\eta.
\tag{6.7}
$$



Under $y=1-t$,


$$
\int g_Nk_j\,d\eta
=
\int_0^\infty e^{-y}y^{n+j}(y^2-2y+2)^2\,dy
=(n+j)!\mathcal R_4(n+j).
\tag{6.8}
$$



The required gcd is not left unevaluated:

### Lemma 6.2

For every integer $n\ge1$,


$$
\boxed{
\gcd_{0\le j\le n}
\bigl((n+j)!\mathcal R_4(n+j)\bigr)=4n!.
}
\tag{6.9}
$$



#### Proof

The identity


$$
\mathcal R_4(x)
=x(x+1)(x+2)(x+3)+8(x+1)^2+4
\tag{6.10}
$$


shows that, for every nonnegative integer $x$,


$$
v_2(\mathcal R_4(x))=2.
$$


Indeed, the product of four consecutive integers is divisible by $8$, and the remaining terms are $0+4\pmod8$. Thus every number in (6.9) is divisible by $4n!$, and the term $j=0$ prevents any additional factor of $2$.

Let $p$ be odd.

If $p\le2n+1$, choose $j\in[0,n]$ so that


$$
n+j\equiv-1\pmod p
$$


and there is no multiple of $p$ strictly between $n$ and $n+j$. Then


$$
v_p((n+j)!)=v_p(n!),
$$


while


$$
\mathcal R_4(n+j)\equiv\mathcal R_4(-1)=4\not\equiv0\pmod p.
$$


Hence there is no extra factor of $p$.

If $p>2n+1$ and $n\ge4$, all factorials are $p$-units. If $p$ divided all the numbers in (6.9), the monic quartic $\mathcal R_4$ would vanish at the five distinct residues


$$
n,n+1,n+2,n+3,n+4,
$$


which is impossible.

The remaining $n=1,2,3$ cases are the small exact calculations


$$
\gcd(60,392)=4,
$$




$$
\gcd(392,2952,25056)=8,
$$




$$
\gcd(2952,25056,236640,2462400)=24.
$$


These are respectively $4n!$. ∎

Combining (6.7)–(6.9) proves (6.2). Evaluation of $\phi_N-a_N^\circ g_N$ at $i$, and at $1$ when $N\ge3$, proves (6.3).

This completes Theorem 6.1.

### 6.2 Consequences for actual large-prime content

At any prime $p\nmid2c_N$, equation (6.1) gives


$$
v_p(h_N)
=\min\!\left(v_p(T_N)+2v_p(d_N),\,
                 v_p(D)+v_p(\Delta)\right).
$$


By (6.2), this holds at every odd prime $p>N-2$.

There is also a source-only evaluation of $d_N$ at primes $p>N$:


$$
\boxed{
v_p(d_N)=\min\bigl(v_p(\mathsf W),v_p(\mathsf V)\bigr).
}
\tag{6.11}
$$


Here $v_p(0)=+\infty$ if necessary.

To check (6.11), express $\Phi$ in the monic integral basis $H_j$. Its $H_j$-coefficient is


$$
\left(\frac{N!}{j!}\right)^2
\left(
\mathsf W\Re H_j(i)-\mathsf V\Im H_j(i)
\right).
$$


For $p>N$, every prefactor is a $p$-unit. All coefficients are combinations of $\mathsf W,\mathsf V$, and the $j=0,1$ coefficients are respectively


$$
(N!)^2\mathsf W,\qquad -(N!)^2\mathsf V.
$$


The monic basis transformation is unimodular over $\mathbb Z$, proving the assertion.

Thus the exact high-prime valuation of $h_N$ is now determined by $T_N,\Delta,D,\mathsf W,\mathsf V$. No unknown polynomial content remains at those primes.

This theorem does **not** determine the final $\mathfrak G_N$. That is a different gcd, arising after the rational endpoint has been evaluated.

---

## 7. New endpoint evaluation and a final-gcd test for factorial primes

The second square permits further exact compression.

Put


$$
m=2N-4.
$$


Then


$$
\boxed{T_N=m!\mathcal R_4(m).}
\tag{7.1}
$$



### 7.1 Complete second-square endpoint

Define integers


$$
C_0=1,\qquad C_r=rC_{r-1}+1.
$$


Equivalently,


$$
C_r=\int_0^\infty e^{-x}(1+x)^r\,dx.
$$


No numerical approximation to $e$ is used.

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


Eliminating the four successor $C$'s by their recurrence yields the evaluated identity


$$
\boxed{
B_g=\mathcal R_4(m)C_m+m^3+6m^2+18m+17.
}
\tag{7.2}
$$



The complete arctangent quotient integral is


$$
\boxed{
\beta_g:=
\int_0^1\frac{g_N(t)^2}{1+t^2}\,dt
=
\frac{m^2+5m+8}{(m+1)(m+2)(m+3)}.
}
\tag{7.3}
$$


The unweighted square integral is


$$
\boxed{
B_N^g=
\frac1{m+1}
+\frac4{(m+1)(m+2)(m+3)}
+\frac{24}{(m+1)(m+2)(m+3)(m+4)(m+5)}.
}
\tag{7.4}
$$



Thus the complete second-square rational endpoint is the explicitly evaluated rational number


$$
R_g=B_g-4\beta_g.
$$



For the first square, let


$$
Q_\Phi=\frac{\Phi^2-\Delta^2}{1+t^2}\in\mathbb Z[t],
$$


and retain its complete endpoint


$$
R_\Phi=
\sum_d[t^d]\Phi^2\,(-1)^dd!
-4\int_0^1Q_\Phi(t)\,dt.
$$


The original output is exactly


$$
\boxed{
A_N=\frac{\lambda_N}{h_N}
\left(T_NR_\Phi+D\Delta R_g\right).
}
\tag{7.5}
$$


The factors $T_N,\Delta,h_N,\lambda_N$ have not been suppressed.

Likewise,


$$
\boxed{
q_NJ_N=
\frac{\lambda_N}{h_N\mathfrak G_N}
\left(
T_N\int_0^1\Phi(t)^2\,dt+D\Delta B_N^g
\right).
}
\tag{7.6}
$$



### 7.2 A uniform explanation of missing interior endpoint primes

Let


$$
N<p\le2N-4
$$


be prime, and assume


$$
p\nmid D\Delta.
\tag{7.7}
$$


Then $p\mid T_N$, $p\nmid h_N$, and reduction of the actual content-reduced quotient gives


$$
S_N(t)\equiv
\frac{D\Delta}{h_N}(1+t^2)(1-t)^m
\pmod p.
$$


Write $m=p+r$. Since $p>N$,


$$
0\le r\le p-6.
$$


In characteristic $p$,


$$
(1-t)^m=(1-t^p)(1-t)^r.
$$


The coefficient of $t^{p-1}$ in $(1+t^2)(1-t)^m$ is therefore zero. Hence


$$
s_{p-1}\equiv0\pmod p.
$$


The endpoint-prime lemma then proves


$$
\boxed{v_p(\lambda_N)=0.}
\tag{7.8}
$$



This is a uniform theorem under explicit hypotheses. In particular, it explains why an interior factorial prime can be absent from $\lambda_N$; its absence need not result from unexplained cancellation in a large sum.

### 7.3 A precise test for the final gcd at regular factorial primes

Assume additionally that $v_p(T_N)=1$, equivalently here that


$$
p\nmid\mathcal R_4(m).
$$


Put


$$
c_{\Phi,p}=[t^{p-1}]Q_\Phi.
$$


Because the quotient denominators are at most $2N-1<2p$, only the denominator $p$ contributes a pole at $p$. Equation (7.5) therefore gives


$$
\frac{h_NA_N}{\lambda_N}
\equiv
D\Delta R_g-4\frac{T_N}{p}c_{\Phi,p}
\pmod p.
$$


The rational $R_g$ is $p$-integral: its denominator in (7.3) is prime to $p$.

Define


$$
\boxed{
\Psi_{N,p}
=
D\Delta R_g-4\frac{T_N}{p}c_{\Phi,p}
\quad\text{in }\mathbb Z_{(p)}.
}
\tag{7.9}
$$


Under these hypotheses,


$$
v_p(M_N)=1,\qquad v_p(\lambda_N)=v_p(h_N)=0.
$$


Thus


$$
\boxed{
v_p(q_N)=
\begin{cases}
1,&\Psi_{N,p}\not\equiv0\pmod p,\\
0,&\Psi_{N,p}\equiv0\pmod p.
\end{cases}
}
\tag{7.10}
$$



This is a test for the **final** gcd, not merely the coefficient clearer. It replaces an unspecified cancellation at these primes by a specific original-object residue.

No assertion that these residues are uniformly nonzero is made.

---

## 8. Independent $N=8$ audit

The following reductions use the actual polynomials and integers, not the JSON pass flags.

### 8.1 Basis and all 81 pair identities

The listed basis coefficients can be checked against


$$
[t^k]E_j
=
\frac{8!}{k!}
\sum_{r=k}^j
\frac{(-1)^{r+k}\binom jr}{(r-k)!}.
\tag{8.1}
$$


Alternatively, one can use the integral recurrence (3.1) and $E_j=(8!/j!)H_j$.

Thus the nine listed polynomials are exactly $8!L_j(1-t)$, $0\le j\le8$. Classical orthogonality consequently verifies **all 81** pair identities:


$$
\int E_jE_k\,d\eta=(8!)^2\delta_{jk}.
$$


No finite-box inference is needed.

Their contents are respectively


$$
40320,\ 40320,\ 20160,\ 6720,\ 1680,\ 336,\ 56,\ 8,\ 1.
$$



The Gaussian evaluations, divided by $16$, are


$$
\begin{array}{c|r|r}
j&\alpha_j/16&\beta_j/16\\ \hline
0&2520&0\\
1&0&2520\\
2&-2520&2520\\
3&-4200&840\\
4&-4620&-1680\\
5&-3696&-4284\\
6&-1596&-6356\\
7&1340&-7452\\
8&4673&-7312
\end{array}
\tag{8.2}
$$


These reproduce


$$
\mathsf U=23\,430\,492\,416,\quad
\mathsf V=-5\,195\,165\,696,\quad
\mathsf W=47\,098\,327\,040.
$$



### 8.2 A smaller exact certificate for $\Phi,\Delta,D$

Set


$$
\delta=1\,026\,675\,460\,727\,799,\qquad
d^\ast=953\,654\,656\,031\,799.
$$


Direct source-integer arithmetic gives


$$
\Delta=2^{20}\delta,\qquad D=2^{20}d^\ast.
$$


For example,


$$
\delta
=
91\,525\,361\cdot11\,498\,615
-16(1\,268\,351)^2.
$$


Also


$$
\delta-d^\ast=73\,020\,804\,696\,000.
$$



Let $a_j,b_j$ denote the two columns in (8.2), and define the complete degree-eight polynomial


$$
\phi(t)=
\sum_{j=0}^8
\bigl(11\,498\,615\,a_j+1\,268\,351\,b_j\bigr)E_j(t).
\tag{8.3}
$$


Then the supplied $\Phi$ is exactly


$$
\Phi=2^{16}\phi.
$$



Useful coefficients are


$$
\phi(0)=5\,791\,849\,088\,102\,855,
$$




$$
[t^7]\phi=2\,537\,346\,481\,032,\qquad
[t^8]\phi=44\,458\,845\,383.
$$


The last two are coprime. Hence


$$
\boxed{d_{\Phi,8}=2^{16}.}
$$



For the new content parameter,


$$
\gcd\!\left(
34\,753\,631\,875\,098\,162,\,
5\,791\,804\,629\,257\,472
\right)=6.
$$


These are, up to sign, the last two coefficients of
$\phi-\phi(0)g_8$.

Furthermore,


$$
\phi\equiv1+t^8\pmod2,
$$


and


$$
\phi\equiv
2(1+t^2+t^3+t^5+t^6+t^8)\pmod3.
$$


These are exactly $\phi(0)g_8$ modulo $2$ and $3$. Therefore


$$
\boxed{c_8=6.}
\tag{8.4}
$$



### 8.3 Exact raw content and least coefficient clearer

Put


$$
\delta'=\delta/3=342\,225\,153\,575\,933,
$$




$$
d' =d^\ast/3=317\,884\,885\,343\,933,
$$


and


$$
T=16\,341\,618\,585\,600.
$$


The complete raw polynomial factors as


$$
\boxed{
\mathscr W_8
=
2^{40}3^2
\left(
7\,092\,716\,400\,\phi^2+\delta'd'g_8^2
\right).
}
\tag{8.5}
$$


Also


$$
\mathscr Z_8=2^{40}3^2T(\delta')^2.
$$



The polynomial in parentheses in (8.5) is primitive. Indeed, Theorem 6.1 reduces its content to


$$
\gcd\!\left(
7\,092\,716\,400\,\phi(0)^2+\delta'd',\,
85\,112\,596\,800
\right).
$$


Here


$$
85\,112\,596\,800
=2^6\,3^5\,5^2\,7\,11\,2843.
$$


The first argument has residues


$$
1,\ 1,\ 4,\ 4,\ 6,\ 1843
$$


modulo $2,3,5,7,11,2843$, respectively, and


$$
\gcd(1843,2843)=1.
$$


For the last residue one may check


$$
\delta'\equiv603,\qquad d'\equiv2285\pmod{2843}.
$$



It follows independently that


$$
\boxed{h_8=2^{40}3^2=9\,895\,604\,649\,984.}
$$


Consequently


$$
\boxed{
W_8=7\,092\,716\,400\,\phi^2+\delta'd'g_8^2,
\qquad
M_8=T(\delta')^2.
}
\tag{8.6}
$$


Expansion of (8.6) gives the complete listed primitive coefficient vector, and


$$
M_8=
1\,913\,898\,596\,391\,279\,830\,143\,092\,166\,756\,269\,280\,358\,400.
$$



This is an alternative exact content certificate; it does not depend on the enormous supplied coefficient Bézout vector.

The individual minimizing-polynomial clearer is


$$
\Delta/2^{16}=48\delta'
=16\,426\,807\,371\,644\,784.
$$


Moreover,


$$
\tau_8
=\frac{24\,340\,268\,232\,000}{\delta'},\qquad
1-\tau_8=\frac{d'}{\delta'}.
$$


The relevant coprimalities show that the second-square coefficient has least clearer $T\delta'$. The actual clearer of their sum is nevertheless the $M_8$ in (8.6), as certified by primitivity.

### 8.4 Source identities without a large moment dot product

Equation (8.3) gives


$$
\phi(i)=48\delta'.
$$


Thus


$$
W_8(i)
=7\,092\,716\,400(48\delta')^2
=T(\delta')^2=M_8.
$$



The norm identity for $\Phi$, together with the definition of $d'$, similarly gives


$$
\int W_8\,d\eta=T(\delta')^2=M_8.
$$


Hence both source identities are independently established for the complete polynomial.

### 8.5 Endpoint clearers and their minimality

Using the full quotient


$$
S_8=(W_8-M_8)/(1+t^2),
$$


the fifteen individual denominator contributions, for $j+1=1,\ldots,15$, are


$$
1,1,3,1,5,3,7,1,3,5,1,3,13,7,15.
$$


Their lcm is


$$
L_{\mathrm{ent},8}=1365.
$$



The complete endpoint reductions are


$$
B_{\mathrm{end},8}
=5062005975859159595648266218328272116450405,
$$




$$
J_{\mathrm{arc},8}
=-7748468471133139106523899508657576285466307864.
$$


The latter has residues


$$
1,\ 1,\ 2,\ 10
$$


modulo $3,5,7,13$, respectively. Therefore


$$
d_{\mathrm{arc},8}=1,\qquad
\boxed{\lambda_8=1365.}
$$


In particular, no prime in $1365$ can be removed by the final gcd.

The complete output integer is


$$
\boxed{
A_8
=14658106628180891954583782896675667724421110689.
}
$$


The equality


$$
A_8=1365\,B_{\mathrm{end},8}-J_{\mathrm{arc},8}
$$


is an exact decimal-integer identity.

For the two requested post-content residues, alternating base-$1000$ reduction gives


$$
s_{10}\equiv704\equiv0\pmod{11},
$$




$$
s_{12}\equiv-82\equiv9\pmod{13}.
$$


Thus


$$
v_{11}(\lambda_8)=0,\qquad v_{13}(\lambda_8)=1.
$$



### 8.6 Independent all-prime proof that $\mathfrak G_8=1$

Since $M_8=T(\delta')^2$, it suffices to prove


$$
\gcd(A_8,T)=\gcd(A_8,\delta')=1.
$$



For the factors of $T$, the residues of $A_8$ modulo


$$
2,3,5,7,11,2843
$$


are respectively


$$
1,2,4,5,7,1187.
$$


Also $\gcd(1187,2843)=1$. This proves $\gcd(A_8,T)=1$.

For the remaining factor,


$$
A_8\equiv200\,490\,906\,603\,640
\pmod{342\,225\,153\,575\,933}.
$$


Euclid’s algorithm gives gcd $1$; its terminal nonzero remainders include


$$
5495,\ 5431,\ 64,\ 55,\ 9,\ 1.
$$


Therefore


$$
\boxed{\mathfrak G_8=1.}
$$



The supplied final Bézout witness is the exact identity


$$
\begin{aligned}
&319058402166828410521045905945930651200890001\,q_8\\
&\quad-
56864848268904141075913804572534105642149791\,A_8
=1.
\end{aligned}
$$


The independent gcd argument above makes the mathematical normalization independent of this long decimal witness.

Thus


$$
\boxed{
p_8=A_8,\qquad
q_8=2612471584074096968145320807622307567689216000.
}
$$



### 8.7 Exact error diagnostics and the new local prime test

The complete finite rational calculation gives


$$
\boxed{
q_8J_8
=
\frac{8914263188229099878762210316607355940514931431}{68}.
}
\tag{8.7}
$$


An integer-only checksum for this value is


$$
\sum_{d=0}^{16}
\frac{12\,252\,240}{d+1}\,w_d
=
132\cdot8914263188229099878762210316607355940514931431.
\tag{8.8}
$$


Every multiplier on the left is integral.

Also


$$
\boxed{
\frac{q_8}{13T}
=105(\delta')^2
=12297395852707447378805666151345.
}
$$


The whole error therefore satisfies exactly the interval printed in the certificate:


$$
\frac{26742789564687299636286630949822067821544794293}{68}
\le q_8(e+\pi)-p_8
\le
\frac{62399842317603699151335472216251491583604520017}{68}.
$$



The new second-square formulas evaluate here to


$$
B_g=44\,421\,124\,848\,845,\qquad
\beta_g=\frac{106}{1365},\qquad
B_8^g=\frac{7279}{92820}.
$$



At $p=11$,


$$
\Delta\equiv3,\quad D\equiv7,\quad T/11\equiv6,\quad
R_g\equiv2\pmod{11}.
$$


From the five relevant coefficients of $\Phi$,


$$
(\Phi_4,\Phi_5,\Phi_6,\Phi_7,\Phi_8)
\equiv(9,0,1,0,8)\pmod{11},
$$


one obtains


$$
c_{\Phi,11}\equiv6\pmod{11}.
$$


Hence


$$
\Psi_{8,11}\equiv3\cdot7\cdot2-4\cdot6\cdot6
\equiv8\not\equiv0\pmod{11}.
$$


Theorem (7.10) independently confirms


$$
v_{11}(q_8)=1.
$$



Thus the precise finite conclusion is:

> $\lambda_8$ lacks $11$, but $q_8$ does not.  
> The prime $13$ survives through $\lambda_8$.  
> The final gcd is $1$, and the whole primitive error is enormous.

None of these finite facts proves eventual behavior.

---

## 9. Accept/correct/reject ledger

| Claim or proposed inference | Verdict | Exact reason |
|---|---|---|
| Complete exponential endpoint identity | **Accept** | Both endpoints retained; factorial term correct. |
| Odd arctangent and $\log2$ terms | **Accept** | Initial odd integral and recurrence are correct. |
| Exact $\log2$ elimination | **Accept** | Follows from the actual condition $P_N(i)=1$. |
| Real rational minimum at $i$ | **Accept** | Two independent real constraints and a positive Euclidean norm. |
| Both-square contact construction | **Accept** | Correct norms; $D>0$; degree exactly $2N$. |
| Strict positivity of the whole error | **Accept** | Actual integrand is positive on a set of positive measure. |
| Paid definitions of $h_N,M_N,\lambda_N,\mathfrak G_N$ | **Accept** | No free division; least clearers and all-prime gcd are distinguished. |
| Old content bounds as an exact uniform evaluation of $h_N$ | **Reject that inference** | They were only divisibilities. Theorem 6.1 supplies a stronger exact formula. |
| Chebyshev determinant and complex phases | **Accept** | The oscillatory term is retained and bounded; determinant is nonzero. |
| Height bound $\log q_N\le12N\log N+O(N)$ | **Accept** | Valid but insufficient for primitive decay. |
| $N=8$ normalization and error receipt | **Accept as finite arithmetic** | Independent basis, content, clearer, and all-prime gcd reductions given above. |
| $N=8$ as an original-index or asymptotic instance | **Reject** | $8\ne9^{18+32u}$; finite scope only. |
| New parameterization of the whole common-kernel lattice | **Correct scope** | The Stein/Robin source already parameterized that lattice. |
| Transfer of compact, binary, or old Laguerre gcd theorems | **Reject** | Different finite objects and different normalization payments. |
| Irrationality of $e+\pi$ from the present bounds | **Not proved** | Actual primitive $q_NJ_N$ is uncontrolled on the required infinite domain. |

---

## 10. Remaining bottleneck and bounded arithmetic requests

### 10.1 What the new theorem has genuinely narrowed

The raw content is no longer governed only by one lower and one upper divisibility:

- equation (6.1) is an exact all-prime formula;
- the auxiliary moment gcd is evaluated as $4(N-2)!$;
- extra content cancellation is confined to primes at most $N-2$;
- at primes $p>N$, even $d_N$'s valuation is source-only;
- regular interior factorial primes have an explicit final-gcd test $\Psi_{N,p}$.

These statements hold at **every** required original index.

What remains is not an unspecified positivity or normality issue. It is the arithmetic of the complete endpoint (7.5), especially:

1. low-prime depths in the exact content formula;
2. cancellation in the actual $\lambda_N$;
3. the all-prime final gcd $\mathfrak G_N$, including kernel-prime factors of $\Delta$;
4. their combined effect on the positive expression (7.6).

A concrete follow-on arithmetic lemma is to control the residues $\Psi_{N,p}$, and their prime-power analogues where required, on specified classes of primes at the original indices. Such control must then be combined with the remaining kernel-prime and small-prime payments. Merely proving that a few primes survive is not enough to establish primitive decay or failure.

### 10.2 Conditional implications, not theorems

If one proved, on an infinite subset of the original indices,


$$
q_N\le e^{\sqrt N/4},
$$


then (5.6) would imply $0<\ell_N\to0$. Rationality
$e+\pi=A/B$ would instead force every nonzero $\ell_N$ to be at least $1/B$, a contradiction.

Conversely, if one proved eventually on those indices that


$$
q_N\ge(2N-3)T_N,
$$


then (5.6) would imply $\ell_N>1$, excluding this family as a source of vanishing primitive errors.

Neither arithmetic hypothesis is proved here.

### 10.3 Bounded exact arithmetic appropriate for coordinator inspection

No enormous original-index calculation is proposed. The new uniform theorems above need no machine calculation.

If a byte-for-byte audit of the decimal JSON is desired, the remaining appropriate task is a bounded $N=8$ transcription check, not a new large experiment.

**Inputs**

- $E_j=8!L_j(1-t)$, $0\le j\le8$, or recurrence (3.1);
- the reduced evaluation table (8.2);
- the factorized polynomials (8.3), (8.5), and (8.6);
- the supplied complete $W_8,S_8$ coefficient arrays;
- factorials through $16!$;
- the two supplied Bézout witnesses;
- denominators $1,\ldots,17$ for the rational integral checksum only.

**Expected verifiable outputs**

1. Zero coefficient differences between the factorized and listed raw and primitive polynomials.
2. $d_{\Phi,8}=2^{16}$, $c_8=6$, and $h_8=2^{40}3^2$.
3. The coefficient-witness dot product equal to $h_8$ for the raw vector, equivalently $1$ for the primitive vector.
4. The full quotient identity
   

$$
(1+t^2)S_8=W_8-M_8.
$$


5. The exact endpoint values, individual clearer list, and
   

$$
L_{\mathrm{ent},8}=\lambda_8=1365.
$$


6. The final Bézout dot product equal to $1$.
7. The integer checksum (8.8), the stated $q_8/(13T_8)$, and the two post-content residues $0\pmod{11}$, $9\pmod{13}$.
8. As a small check of the new theorem,
   

$$
\gcd_{0\le j\le6}(6+j)!\mathcal R_4(6+j)=2880.
$$



The all-81 orthogonality computation is optional: identification of the listed basis with the classical Laguerre basis already proves all those identities algebraically.

---

## Final proof status

The full-degree two-square construction survives independent mathematical review. Its positivity, complete sources, analytic comparison, and paid primitive normalization are sound.

The new proved result is an exact content theorem for this fixed ansatz, including the evaluated identity


$$
\gcd_{0\le j\le N-2}
(N-2+j)!\mathcal R_4(N-2+j)=4(N-2)!,
$$


together with an evaluated second-square endpoint and a precise final-gcd test at regular factorial primes.

These results materially narrow the arithmetic obstruction. They do **not** prove


$$
q_NJ_N\to0
$$


or its failure at the required infinite original indices.

Accordingly, **neither rationality nor irrationality of $e+\pi$ is established**. The exact remaining bottleneck is the combined, all-prime normalization


$$
\boxed{
\frac{\lambda_NT_N\Delta^2}{h_N\mathfrak G_N}
}
$$


acting on the nonzero whole error at those same indices.
