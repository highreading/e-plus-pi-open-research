> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The signed-source Chebyshev producer: exact content, complete clearing, and a primitive-denominator obstruction

## 1. Scope and outcome

The index domain is unchanged:


$$
\mathcal N=\{N_u=9^{18+32u}:u\in\mathbb Z_{\ge0}\}.
$$


Every index in $\mathcal N$ is at least $256$. No replacement subsequence is introduced.

The old Laguerre two-square producer is retired on $\mathcal N$, as directed. Its accepted obstruction is not extended or recomputed here. The compact and original ternary routes remain separate.

For the **new signed-source Chebyshev producer**, this report proves:

1. **The proposed analytic normalization is valid.** Its complete ordinary error is positive and satisfies a two-sided exponential estimate
   

$$
c_RR^{-2N}<\epsilon_N<C_RR^{-2N}.
$$


   In particular, the supplied upper bound has the correct exponential scale; there is no hidden faster decay.

2. **An exact, all-prime content formula.** With explicitly defined integers $g_N,c_N$,
   

$$
\boxed{h_N=g_N^2c_N.}
$$


   This evaluates the polynomial-content problem as one scalar source gcd, without assuming that the finite observed contents persist.

3. **A surviving-divisor theorem for the actual primitive denominator $q_N$**, after the least aggregate clearer and the final ALL-prime gcd have both been retained.

4. **An unconditional lower bound for the actual positive whole error**:
   

$$
\boxed{
   q_N\epsilon_N>
   \frac{N^N}
        {512\,2400^N\,c_N\sqrt{119N\log_2N}}
   \qquad(N\ge256).
   }
   \tag{1.1}
$$


   This is not a bound on the raw denominator. It applies to the final reduced $q_N$.

The remaining obstruction is explicit. The new producer cannot have shrinking primitive whole errors unless its **polynomial source-content gcd** is exceptionally large:


$$
\log c_N\ge N\log N-O(N).
\tag{1.2}
$$


No proof of such growth, or of an upper bound excluding it, is supplied by the attached work or proved below.

Thus this is a substantive but partial arithmetic resolution. It does **not** yet retire the new producer, and it does not decide whether $e+\pi$ is rational or irrational.

---

## 2. The original objects and the analytic audit

Write


$$
C_j(t)=T_j(2t-1),\qquad
C_0=1,\quad C_1=2t-1,\quad
C_{j+1}=2(2t-1)C_j-C_{j-1}.
$$


Let


$$
C_j(i)=a_j+ib_j,\qquad a_j,b_j\in\mathbb Z,
$$


and retain exactly


$$
d=a_Nb_{N-1}-a_{N-1}b_N,\qquad
B=b_{N-1}C_N-b_NC_{N-1}.
$$


Subscripts $N$ are occasionally suppressed.

The source functional is


$$
\eta(H)=\int_{-\infty}^1e^{t-1}H(t)\,dt.
$$


For every polynomial,


$$
\eta(H)=\sum_{k=0}^{\deg H}(-1)^kH^{(k)}(1).
\tag{2.1}
$$


In particular, $\eta(\mathbb Z[t])\subseteq\mathbb Z$, and


$$
\eta(t^j)=(-1)^j\,!j.
$$



Define, without alteration,


$$
K=t(1-t)(1+t^2)^2C_{N-3}^2,\qquad
U=-\eta(K),\qquad I=\eta(B^2).
$$


The raw producer is


$$
W_{\rm raw}=UB^2+(I-d^2)K,\qquad Z=Ud^2.
\tag{2.2}
$$



All polynomial functionals in this report terminate at their actual finite degrees. In particular, $K$ has degree $2N$, $W_{\rm raw}$ has degree at most $2N$, and the eventual monic quotient has degree at most $2N-2$. No terminal coefficient or endpoint contribution is omitted.

### 2.1 The determinant and the complex normalization

Put $c_j=C_j(i)$. The recurrence at $i$ gives


$$
\operatorname{Im}(c_{j+1}\overline{c_j})
=4|c_j|^2+\operatorname{Im}(c_j\overline{c_{j-1}}).
$$


Since the initial imaginary part is $2$,


$$
d=-2-4\sum_{j=1}^{N-1}|c_j|^2<0.
\tag{2.3}
$$


Consequently,


$$
B(i)=B(-i)=d,\qquad f:=B/d,\qquad f(i)=f(-i)=1.
\tag{2.4}
$$



This proof is exact and does not require a phase-separation assumption.

### 2.2 The signed correction really has $U>0$

On $[0,1]$,


$$
0\le K(t)\le1.
$$


On $[-3,-2]$,


$$
-K(t)\ge150,
$$


because $|C_{N-3}(t)|\ge1$ there. Hence the negative source contribution has magnitude at least


$$
150e^{-4}>150/81>1,
$$


whereas the positive contribution from $[0,1]$ is less than $1$. Thus


$$
U>0.
\tag{2.5}
$$



There is no cancellation of unbounded integrals in this argument: the two signed regions are separately estimated.

### 2.3 Positivity at every original index

The leading coefficient of the rational polynomial $f=B/d$ has magnitude at least $1/|d|$, and its degree is at least $N-1$. The monic Laguerre minimum, applied after $x=1-t$, gives


$$
\eta(f^2)\ge \frac{[(N-1)!]^2}{d^2}.
\tag{2.6}
$$


Also $|C_j(i)|\le6^j$, so


$$
|d|\le6^{2N-1}.
$$


The fixed inequality needed at $N=256$ can be checked without reproducing its large integer certificate:


$$
255!>(255/e)^{255}>85^{255}
>72^{255}=2^{255}6^{510}>6^{511}.
$$


Induction then gives


$$
(N-1)!>6^{2N-1}\qquad(N\ge256).
$$


Thus $I>d^2$ throughout the required domain.

Therefore


$$
P=\frac{B^2}{d^2}+\frac{I-d^2}{Ud^2}K
\tag{2.7}
$$


is nonnegative and nonzero on $[0,1]$, and


$$
\eta(P)=P(i)=P(-i)=1.
\tag{2.8}
$$



The coefficient of $K$ is positive, but $K$ changes sign on the source half-line. The bounded-source-norm hypothesis of the retired Laguerre argument is absent. Applying that old lower bound to this $P$ would therefore be invalid.

---

## 3. The complete ordinary error has exactly exponential scale

Let


$$
z=-1+2i,\qquad \zeta+\zeta^{-1}=2z,\qquad R=|\zeta|>1.
$$


One convenient exact expression is


$$
R=1+\sqrt2+\sqrt{2+2\sqrt2}<5.
$$


Then


$$
C_j(i)=\frac{\zeta^j+\zeta^{-j}}2.
$$



The supplied estimates give, with


$$
K_R=
\frac{R^2(1+R^{-2})(1+R^{-1})}
     {2(1-R^{-2})^2},
$$


the valid upper bound


$$
0<\epsilon_N:=
\int_0^1P_N(t)\left(e^t+\frac4{1+t^2}\right)dt
\le 7(1+2^{17})K_R^2R^{-2N}.
\tag{3.1}
$$



For clarity, the payments behind that estimate are as follows. If


$$
s=\frac{|b_{N-1}|+|b_N|}{|d|},
$$


then


$$
s\le K_RR^{-N},\qquad |f(t)|\le s\quad(0\le t\le1),
$$


and


$$
\eta(f^2)\le s^2\{1+4^{2N}(2N)!\}.
$$


For $N\ge4$, positivity of the coefficients of $T_{N-3}(1+2x)$ gives


$$
U\ge 2^{4N-16}(2N)!.
\tag{3.2}
$$


Consequently the coefficient of $K$ in (2.7) is at most $2^{17}s^2$. Both summands of $P$, not just $f^2$, are included in (3.1).

There is also a useful new lower bound.

### Proposition 3.1 — Uniform lower bound for the actual ordinary error

For every $N\ge256$,


$$
\boxed{
\epsilon_N>
\frac{R^{-2N}}{1+R^{-2}}.
}
\tag{3.3}
$$



#### Proof

Adjacent shifted Chebyshev polynomials have opposite parity about $t=1/2$, so


$$
\int_0^1C_NC_{N-1}\,dt=0.
$$


Moreover,


$$
\int_0^1C_j(t)^2\,dt
=\frac{2j^2-1}{4j^2-1}\ge\frac13
\qquad(j\ge1).
\tag{3.4}
$$


It follows that


$$
\int_0^1f^2\,dt
\ge \frac{b_{N-1}^2+b_N^2}{3d^2}.
$$


By Cauchy–Schwarz,


$$
d^2
\le (b_{N-1}^2+b_N^2)(a_N^2+a_{N-1}^2)
\le (b_{N-1}^2+b_N^2)(|c_N|^2+|c_{N-1}|^2).
$$


Since the whole kernel is strictly larger than $3$ and $P\ge f^2$,


$$
\epsilon_N>
\frac1{|c_N|^2+|c_{N-1}|^2}.
$$


Finally, $|c_j|\le R^j$, giving (3.3). ∎

Combining (3.1) and (3.3),


$$
\boxed{\epsilon_N\asymp R^{-2N}}
\tag{3.5}
$$


with constants independent of $N$.

Thus, on the same original indices,


$$
q_N\epsilon_N\longrightarrow0
\quad\Longleftrightarrow\quad
q_N=o(R^{2N}).
\tag{3.6}
$$


This equivalence concerns the actual whole error, not one selected component.

---

## 4. An exact all-prime polynomial-content theorem

Define


$$
g=\gcd(b_{N-1},b_N)>0,
$$


and put


$$
\alpha=b_{N-1}/g,\qquad
\beta=b_N/g,\qquad
F=B/g=\alpha C_N-\beta C_{N-1},\qquad
\delta=d/g.
\tag{4.1}
$$


Then


$$
F(i)=F(-i)=\delta\in\mathbb Z.
$$


Set


$$
I_0=\eta(F^2)=I/g^2,\qquad
V=I_0-\delta^2,\qquad
c=\gcd(U,V)>0.
\tag{4.2}
$$


For $N\ge256$, $V>0$.

### Theorem 4.1 — Exact content

For every $N\ge3$,


$$
\boxed{\operatorname{cont}(B)=g,}
\tag{4.3}
$$


and


$$
\boxed{h=\operatorname{cont}(W_{\rm raw})=g^2c.}
\tag{4.4}
$$



Consequently, with


$$
\tau=U/c,\qquad \nu=V/c,
\tag{4.5}
$$


one has


$$
\boxed{
W_{\rm prim}=\tau F^2+\nu K,\qquad
M=\tau\delta^2,\qquad
\gcd(\tau,\nu)=1.
}
\tag{4.6}
$$



#### Proof

The Chebyshev recurrence modulo $8$ gives


$$
C_{2j}\equiv1\pmod8,\qquad
C_{2j+1}\equiv2t-1\pmod8.
\tag{4.7}
$$


Hence


$$
b_{2j}\equiv0\pmod8,\qquad
b_{2j+1}\equiv2\pmod8.
$$


Thus $v_2(g)=1$, and exactly one of $\alpha,\beta$ is odd.

Since $\gcd(\alpha,\beta)=1$,


$$
F(0)=(-1)^N(\alpha+\beta),\qquad
F(1)=\alpha-\beta
$$


are coprime: any common odd divisor would divide both $\alpha,\beta$, and both endpoint values are odd. Therefore


$$
\gcd(F(0),F(1))=1.
\tag{4.8}
$$


This proves that $F$ is primitive, and hence proves (4.3).

Now


$$
W_{\rm raw}=g^2(UF^2+VK).
$$


Let $h_0=\operatorname{cont}(UF^2+VK)$. Since $K(0)=K(1)=0$, equation (4.8) gives


$$
h_0\mid
\gcd\bigl(UF(0)^2,UF(1)^2\bigr)=U.
$$


Then


$$
h_0\mid VK.
$$


The coefficient of $t$ in $K$ is $1$, so $K$ is primitive and $h_0\mid V$. Conversely, $\gcd(U,V)$ divides every coefficient of $UF^2+VK$. Thus $h_0=c$, proving (4.4)–(4.6). ∎

This proof treats **all primes simultaneously**. It does not infer polynomial content from a few leading coefficients or from selected prime valuations.

What remains unevaluated in (4.4) is precisely the scalar source gcd $c$. That distinction will be important below.

---

## 5. Uniform local consequences in the original objects

These local results are not sufficient for primitive decay or divergence. They do, however, audit several patterns visible in the finite diagnostic without extrapolating from that diagnostic.

### 5.1 Exact $2$-adic content and an odd primitive denominator

For every $N\ge3$,


$$
v_2(U)=2,\qquad 16\mid V,\qquad v_2(c)=2.
\tag{5.1}
$$


Therefore


$$
\boxed{v_2(h)=4,\qquad M\ \text{is odd}.}
\tag{5.2}
$$



To verify the first assertion, write


$$
H=t(1-t)(1+t^2)^2.
$$


From (4.7), $C_m^2$ is congruent modulo $8$ either to $1$ or to


$$
(2t-1)^2=1+4t(t-1).
$$


Now $\eta(H)=-332$, and


$$
\eta\!\left(t^2(1-t)^2(1+t^2)^2\right)
$$


is even. Indeed, modulo $2$ its polynomial is


$$
t^2+t^4+t^6+t^8,
$$


and each even source moment is odd. Hence $U\equiv4\pmod8$.

Also (4.7) and the divisibility of the even-indexed $b_j$ imply


$$
F(t)\equiv F(0)\pmod8.
$$


Since $\delta=F(i)\in\mathbb Z$, one obtains


$$
16\mid F^2-\delta^2
$$


coefficientwise, and therefore $16\mid V$. This proves (5.1).

The **actual least aggregate affine clearer** is odd as well. Here is a coefficientwise proof only of that local assertion; it is not a replacement of the aggregate clearer by an entrywise lcm.

Each coefficient $[t^r]C_j$ is divisible by $2^r$, because $C_j=T_j(2t-1)$. Thus


$$
v_2([t^r]W_{\rm prim})\ge \max(r-6,0).
$$


Write


$$
S=\frac{W_{\rm prim}-M}{1+t^2}=\sum_j s_jt^j.
$$


Top-down monic division gives the exact finite formula


$$
s_j=\sum_{\substack{k\ge0\\j+2+2k\le2N}}
(-1)^k[t^{j+2+2k}]W_{\rm prim}.
\tag{5.3}
$$


Hence


$$
v_2(s_j)\ge\max(j-4,0).
$$


For every $j\ge0$,


$$
2+\max(j-4,0)\ge v_2(j+1).
$$


Therefore every $4s_j/(j+1)$ is $2$-integral, and so is their complete sum. The least aggregate clearer $\lambda$ is odd. Since $M$ is odd,


$$
\boxed{q_N\ \text{is odd}.}
\tag{5.4}
$$



### 5.2 No source-content factors $3$ or $5$ at the original indices

Modulo $3$, put $x=1-t$. Only source-jet terms of degree at most $2$ matter. With $m=N-3$,


$$
H(1-x)\equiv x\pmod{3,x^3},
$$


and


$$
C_m(1-x)^2\equiv1+2m^2x\pmod{3,x^2}.
$$


Consequently,


$$
U\equiv-(1+m^2)\not\equiv0\pmod3.
\tag{5.5}
$$


Thus $3\nmid c$ for every $N$.

At an original index, $N\equiv1\pmod5$. In $\mathbb F_3[i]$, let $z=-1+2i$; then $z^2=z+1$, and the Chebyshev recurrence has the sequence


$$
1,\ z,\ 2z+1,\ 2z+1,\ z,\ 1,\ z,\ldots.
$$


Thus $C_N(i)=z$, $C_{N-1}(i)=1$, and $d\not\equiv0\pmod3$. Hence $3\nmid g$ at every original index.

For the $5$-adic assertion, original indices satisfy


$$
N\equiv3\pmod6,\qquad N\equiv1\pmod4.
$$


Evaluation at the two roots $i=\pm2$ in $\mathbb F_5$ gives


$$
(a_N,b_N)\equiv(2,1),\qquad
(a_{N-1},b_{N-1})\equiv(4,4),\qquad
d\equiv4\pmod5.
\tag{5.6}
$$


In particular, $5\nmid g$.

Write $m=N-3=5k+3$. The exact low Taylor coefficients give


$$
C_m(1-x)
\equiv1+2x+3x^2+3(k+1)x^3
\pmod{5,x^4}.
$$


Multiplication by $H(1-x)$ then gives


$$
U\equiv-(k+1)
=-\frac{N-1}{5}\pmod5.
\tag{5.7}
$$


If $5\mid U$, then $N\equiv1\pmod{25}$.

The recurrence matrix on $\mathbb F_5[x]/(x^5)$ has period dividing $25$: modulo $x$ it is unipotent of order $5$, and a further fifth power kills the nilpotent correction. Hence, when $N\equiv1\pmod{25}$,


$$
C_N(1-x)\equiv1-2x,\qquad C_{N-1}(1-x)\equiv1
\pmod{5,x^5}.
$$


Using (5.6),


$$
B(1-x)\equiv3+2x,
$$


so


$$
I-d^2\equiv
\eta((3+2x)^2)-1
\equiv4-1=3\pmod5.
$$


Thus $5\nmid V$ whenever $5\mid U$, proving $5\nmid c$.

We have proved, on the full original domain,


$$
\boxed{
v_2(h)=4,\qquad \gcd(h,15)=1,\qquad
c=4c_{\rm odd},\quad \gcd(c_{\rm odd},15)=1.
}
\tag{5.8}
$$


This is a calculation for the **new $U_N$**. No prime formula from the retired factorial source has been imported.

---

## 6. Complete, finite evaluators for the source and affine columns

The following formulas make the remaining arithmetic objects explicit. They also specify every forcing term and the finite terminal.

Define


$$
\mathcal H_j=\eta(C_j),\qquad
\mathcal E_j=\sum_{k=0}^j(-1)^kC_j^{(k)}(0).
$$


Their initial values are


$$
(\mathcal H_0,\mathcal H_1,\mathcal H_2)=(1,-1,9),
$$




$$
(\mathcal E_0,\mathcal E_1,\mathcal E_2)=(1,-3,25).
$$


The identity


$$
4C_j=\frac{C_{j+1}'}{j+1}-\frac{C_{j-1}'}{j-1}
$$


gives, for $j\ge2$,


$$
(j-1)\mathcal H_{j+1}
+4(j^2-1)\mathcal H_j
-(j+1)\mathcal H_{j-1}=-2,
\tag{6.1}
$$


and


$$
(j-1)\mathcal E_{j+1}
+4(j^2-1)\mathcal E_j
-(j+1)\mathcal E_{j-1}=2(-1)^j.
\tag{6.2}
$$


The inhomogeneous terms in both recurrences are essential.

For either functional $\mathcal L=\eta$ or the complete exponential endpoint,


$$
\begin{aligned}
\mathcal L(F^2)
={}&\frac{\alpha^2+\beta^2}{2}
+\frac{\alpha^2}{2}\mathcal L(C_{2N})
+\frac{\beta^2}{2}\mathcal L(C_{2N-2})\\
&-\alpha\beta\{\mathcal L(C_{2N-1})+\mathcal L(C_1)\}.
\end{aligned}
\tag{6.3}
$$


Thus $I_0$ and the complete endpoint $E_F$ are evaluated by (6.1)–(6.3), through terminal $2N$.

For $K$, the exact identity


$$
H=\frac1{2048}
(458C_0+176C_1-399C_2-168C_3-58C_4-8C_5-C_6)
$$


gives, with


$$
(\gamma_0,\ldots,\gamma_6)=(458,176,-399,-168,-58,-8,-1),
$$




$$
\mathcal L(K)=\frac1{8192}\sum_{r=0}^6\gamma_r
\bigl(2\mathcal L(C_r)+
\mathcal L(C_{2m+r})+
\mathcal L(C_{|2m-r|})\bigr),
\quad m=N-3.
\tag{6.4}
$$


This is a fixed seven-term evaluator, with terminal at most $2N$. The divisions by $2$ and $8192$ are exact consequences of integral polynomial identities; they are not unrecorded denominator cancellations.

### 6.1 The complete rational arc of $F^2$

Let


$$
R_j(t)=\frac{C_j(t)-a_j-b_jt}{1+t^2}\in\mathbb Z[t],
$$


and define


$$
\xi_j=4\int_0^1R_j(t)\,dt,\qquad
\upsilon_j=4\int_0^1tR_j(t)\,dt.
$$


Put


$$
\ell_j=\int_0^1C_j(t)\,dt
=
\begin{cases}
0,&j\ \text{odd},\\
(1-j^2)^{-1},&j\ \text{even}.
\end{cases}
$$


Starting with


$$
\xi_0=\xi_1=\upsilon_0=\upsilon_1=0,
$$


the complete recurrence is


$$
\xi_{j+1}=4\upsilon_j-2\xi_j-\xi_{j-1}+16b_j,
\tag{6.5}
$$




$$
\upsilon_{j+1}
=-4\xi_j-2\upsilon_j-\upsilon_{j-1}
+16(\ell_j-a_j).
\tag{6.6}
$$


These follow from


$$
R_{j+1}=(4t-2)R_j-R_{j-1}+4b_j
$$


and


$$
t^2R_j=C_j-a_j-b_jt-R_j.
$$


Thus neither the return terms nor the affine forcing has been dropped.

The complete arc correction for $F^2$ is


$$
\boxed{
R_F:=4\int_0^1\frac{F^2-\delta^2}{1+t^2}\,dt
=\frac{\alpha^2\xi_{2N}
+\beta^2\xi_{2N-2}
-2\alpha\beta\xi_{2N-1}}2.
}
\tag{6.7}
$$



### 6.2 A closed rational evaluation of the $K$-arc

Set


$$
j_r=\frac1{1-4r^2},\qquad j_{-r}=j_r.
$$


Chebyshev linearization and $\int_0^1C_{2r}=j_r$ give


$$
\boxed{
R_K:=4\int_0^1\frac{K}{1+t^2}\,dt
=
\frac{13}{30}
+\frac{
42j_m-20(j_{m+1}+j_{m-1})
-(j_{m+2}+j_{m-2})
}{128}.
}
\tag{6.8}
$$



For example, this follows by retaining the even part, under $x=2t-1$, of


$$
4t(1-t)(1+t^2)
=\frac{(1-x^2)(x^2+2x+5)}4,
$$


whose even part is


$$
\frac{21T_0-20T_2-T_4}{32}.
$$



Thus the least denominator of this **complete** column is obtained by reducing the explicit rational number (6.8). It is not the monomial-entry lcm. In particular, it divides the explicit polynomial-size clearer


$$
128\cdot30
\prod_{r=-2}^{2}|1-4(m+r)^2|.
\tag{6.9}
$$



---

## 7. The exact ordinary integral, including both positive summands

The ordinary unweighted integral can also be evaluated without a degree-$2N$ named sum.

Define


$$
J_F=\int_0^1F^2\,dt
=
\alpha^2\frac{2N^2-1}{4N^2-1}
+\beta^2\frac{2(N-1)^2-1}{4(N-1)^2-1}.
\tag{7.1}
$$


The mixed term vanishes by parity.

For $K$,


$$
\boxed{
J_K:=\int_0^1K\,dt
=
\frac{61}{420}
+\frac{
916j_m-399(j_{m+1}+j_{m-1})
-58(j_{m+2}+j_{m-2})
-(j_{m+3}+j_{m-3})
}{8192}.
}
\tag{7.2}
$$


To verify it, the even part of


$$
(1-x^2)(x^2+2x+5)^2
$$


is


$$
25-11x^2-13x^4-x^6
=\frac{458T_0-399T_2-58T_4-T_6}{32}.
$$


Applying $T_m^2=(1+T_{2m})/2$ gives (7.2).

Consequently the exact rational number


$$
\boxed{
J_N:=\int_0^1P_N\,dt
=\frac{J_F+(V/U)J_K}{\delta^2}
}
\tag{7.3}
$$


satisfies


$$
\boxed{3J_N<\epsilon_N<7J_N.}
\tag{7.4}
$$


Both summands of $P_N$ are present in (7.3).

After primitive normalization,


$$
\boxed{
q_NJ_N=\frac{\lambda_N}{G_N}
\bigl(\tau_NJ_F+\nu_NJ_K\bigr).
}
\tag{7.5}
$$


Thus (7.4)–(7.5) are exact rational enclosures for the **whole evaluated primitive error**, not merely for its exponential component.

---

## 8. The least aggregate clearer and the final ALL-prime gcd

Let


$$
E_F=\sum_j(-1)^jj![t^j]F^2,\qquad
E_K=\sum_j(-1)^jj![t^j]K.
$$


Both are integers, evaluated completely by Section 6.

From (4.6),


$$
E=\tau E_F+\nu E_K.
$$


The complete affine arc is


$$
R_W=\tau R_F+\nu R_K.
$$


Reduce this single aggregate rational number:


$$
R_W=\frac b\lambda,\qquad
\gcd(b,\lambda)=1,\qquad \lambda>0.
\tag{8.1}
$$


This $\lambda$ is the **actual least aggregate affine clearer**.

Define


$$
A=\lambda E-b,\qquad
G=\gcd(M,A).
\tag{8.2}
$$


Since $\gcd(A,\lambda)=1$,


$$
\gcd(\lambda M,A)=G.
$$


Hence


$$
\boxed{
q=\frac{\lambda M}{G},\qquad p=\frac A G.
}
\tag{8.3}
$$



Repeated integration by parts and monic division give


$$
\int_0^1W_{\rm prim}e^t\,dt=eM-E,
$$




$$
4\int_0^1\frac{W_{\rm prim}}{1+t^2}\,dt=M\pi+\frac b\lambda.
$$


Because $W_{\rm prim}=MP$,


$$
\boxed{
q(e+\pi)-p=q\epsilon_N>0.
}
\tag{8.4}
$$



No polynomial-content division, rational clearer, or final gcd is omitted.

### 8.1 An auxiliary clearer that is not substituted for $\lambda$

For the next theorem only, let


$$
D=\operatorname{lcm}\bigl(\operatorname{den}(R_F),
                         \operatorname{den}(R_K)\bigr),
$$


where each denominator is taken after complete rational reduction. Define


$$
X=D(E_F-R_F),\qquad Y=D(E_K-R_K).
\tag{8.5}
$$


Then $X,Y\in\mathbb Z$, and


$$
\frac pq=\frac{\tau X+\nu Y}{D\tau\delta^2}.
\tag{8.6}
$$


Crucially,


$$
\tau X+\nu Y=\frac D\lambda A,
$$


and therefore


$$
\boxed{
\gcd(D\tau\delta^2,\tau X+\nu Y)
=\frac D\lambda G.
}
\tag{8.7}
$$


Thus the unused factor $D/\lambda$ returns inside the final gcd. Formula (8.6) is exactly the same primitive rational number as (8.3); $D$ has not replaced the least aggregate $\lambda$.

---

## 9. A surviving-divisor theorem reaching the actual $q_N$

### Theorem 9.1 — All-prime survival from the signed source column

With the exact quantities above,


$$
\boxed{
\frac{\tau}{\gcd(\tau,Y)}\mid q.
}
\tag{9.1}
$$



#### Proof

Because $\gcd(\tau,\nu)=1$,


$$
\gcd(\tau,\tau X+\nu Y)=\gcd(\tau,Y).
$$


Reducing (8.6) cannot remove from its denominator any factor of $\tau$ not in this gcd. This proves (9.1), prime power by prime power, including primes also dividing $D$ or $\delta$. ∎

The theorem is useful because $Y$ belongs to a **pure $e$-column**.

Let


$$
L_K=\int_0^1K(t)\left(e^t+\frac4{1+t^2}\right)dt.
$$


Since $\eta(K)=-U$ and $K(i)=K(-i)=0$,


$$
E_K-R_K=-Ue-L_K.
$$


Thus


$$
\boxed{Y+DUe=-DL_K,}
\tag{9.2}
$$


with


$$
0<L_K<7J_K\le7.
\tag{9.3}
$$



A large cancellation of the surviving $\tau$-part would therefore produce an unusually strong rational approximation to $e$. This allows the final gcd to be controlled without assuming $G=1$, and without restricting attention to selected primes.

### Theorem 9.2 — Primitive-denominator lower bound

Put


$$
H_e(x)=4\log_2x+8.
$$


Then


$$
\boxed{
q>
\frac{\sqrt U}
     {cD\sqrt{7H_e(DU)}}.
}
\tag{9.4}
$$


The constant $7$ can be replaced by the explicit rational $7J_K$.

#### Proof

The established effective estimate from Euler’s continued fraction is


$$
|Qe-P|>\frac1{QH_e(Q)}
\qquad(P\in\mathbb Z,\ Q\ge1).
\tag{9.5}
$$


Its hypotheses include unreduced rational pairs. For completeness, convergents satisfy the usual bound with their next partial quotient; Euler’s partial quotients and Fibonacci denominator growth give the factor $H_e(Q)$. Nonconvergents satisfy the stronger Legendre bound. Reduction of a nonprimitive pair only strengthens (9.5).

Let


$$
a=\gcd(\tau,Y).
$$


Since $a\mid U$, the integers


$$
Q=DU/a,\qquad P=-Y/a
$$


are legitimate inputs to (9.5). Equation (9.2) gives


$$
|Qe-P|=\frac{DL_K}{a}.
$$


Consequently,


$$
\frac{DL_K}{a}>
\frac{a}{DUH_e(Q)},
$$


or


$$
a^2<D^2UL_KH_e(Q)
\le7D^2UH_e(DU).
$$


Using (9.1) and $\tau=U/c$,


$$
q\ge\frac{\tau}{a}>
\frac{\sqrt U}{cD\sqrt{7H_e(DU)}}.
$$


This proves (9.4). ∎

This is the principal new arithmetic estimate. It bounds the **actual primitive denominator after the ALL-prime final gcd**. Its limitation is equally precise: the initial source-content divisor $c$ remains in the denominator of the bound.

---

## 10. Comparison with the actual whole error

Both column arc denominators divide


$$
L_{2N-1}:=\operatorname{lcm}(1,\ldots,2N-1),
$$


so


$$
D\mid L_{2N-1}.
\tag{10.1}
$$



A coarse explicit exponential bound suffices. The quotient $L_{2n}/L_n$ divides $\binom{2n}{n}$, hence


$$
L_{2n}\le4^nL_n.
$$


Dyadic iteration gives


$$
D<4^{4N}=256^N.
\tag{10.2}
$$



The coefficient norm of $K$ gives


$$
U\le8\,36^{N-3}(2N)!.
\tag{10.3}
$$


Together with (10.2), this implies, for $N\ge256$,


$$
H_e(DU)\le17N\log_2N.
\tag{10.4}
$$



On the other hand, (3.2) and $n!>(n/e)^n$ give


$$
\sqrt U\ge2^{2N-8}\sqrt{(2N)!}
>\frac1{256}\left(\frac{8N}{e}\right)^N.
\tag{10.5}
$$


Combine (3.3), (9.4), and (10.2)–(10.5). Since


$$
1+R^{-2}<2,\qquad e<3,\qquad R<5,
$$


one obtains


$$
\boxed{
q_N\epsilon_N>
\frac{N^N}
 {512\,2400^N\,c_N\sqrt{119N\log_2N}}.
}
\tag{10.6}
$$



Every factor in this estimate has a stated role:

- $U$ is the actual signed Chebyshev source, not the retired factorial source;
- $c$ is the actual remaining polynomial-content gcd;
- $D$ is used only as an auxiliary bound, with its excess over $\lambda$ exactly returned in (8.7);
- the entire final gcd is allowed in Theorems 9.1–9.2;
- $\epsilon_N$ is the actual positive whole ordinary error.

### 10.1 A rigorous conditional no-go

A concrete sufficient follow-on lemma is:

> **Source-content lemma SC.** For all sufficiently large original indices,
> 

$$
> \boxed{
> \gcd\!\left(
> -\eta(K_N),
> \eta\!\left((B_N/g_N)^2\right)-(d_N/g_N)^2
> \right)
> \le N^{N/2}.
> }
> \tag{10.7}
>
$$



If SC holds, then (10.6) gives


$$
q_N\epsilon_N>
\frac{(\sqrt N/2400)^N}
     {512\sqrt{119N\log_2N}}
\longrightarrow\infty
$$


on the same original indices. Thus SC would retire this producer.

More generally, any uniform bound


$$
\log c_N\le(1-\delta)N\log N+O(N)
\qquad(\delta>0)
\tag{10.8}
$$


would suffice.

### 10.2 A necessary condition for success

Conversely, if this producer were to satisfy


$$
q_N\epsilon_N\longrightarrow0
$$


on the original domain, then (10.6) would force


$$
\frac{
512\,2400^N\,c_N\sqrt{119N\log_2N}
}{N^N}\longrightarrow\infty.
\tag{10.9}
$$


In particular,


$$
\boxed{\log c_N\ge N\log N-O(N).}
\tag{10.10}
$$



Thus ordinary exponential decay can only survive primitive normalization here if the **initial polynomial content itself absorbs roughly a square-root-factorial portion of the signed source**.

This necessity is not visible from a raw factorial upper bound on $Z$, and it is not proved by the finite diagnostic.

---

## 11. Why the archive barriers do not finish this arithmetic

The fixed-target positive theorem is valid at its stated integer hypotheses, but $P_N(i)=1$ is a rational normalization. The relevant integer polynomial is $W_{\rm prim}$, whose target is


$$
M=\tau\delta^2.
$$



This target is genuinely unbounded. Indeed, (2.3) gives


$$
|d|\ge(1-R^{-2})^2R^{2N-2},
$$


whereas $g\le\max(|b_N|,|b_{N-1}|)\le R^N$. Hence


$$
|\delta|\ge(1-R^{-2})^2R^{N-2},
\qquad M\ge\delta^2\longrightarrow\infty.
$$


Therefore the fixed-target theorem cannot be applied with target $1$.

The growing-target synchronization barrier does apply to $W_{\rm prim}$. In particular, polynomial primitivity does not imply that the final output gcd is small. The archive’s explicit linear-cross-content example rules out that shortcut.

The new argument above uses a more specific fact: cancellation of the surviving $U/c$ contribution must also cancel against the pure $e$-column $K$, and (9.5) controls that cancellation. But it does **not** control the prior common divisor


$$
c=\gcd(U,V).
$$


If $c$ is already of square-root-factorial size, the lower bound (10.6) may be too weak. Dropping $c$, or setting it equal to its finite observed value, would be an unpaid division and an invalid proof.

That is the exact obstruction to completing a no-go argument from the estimates presently proved.

---

## 12. A bounded arithmetic check relevant to the remaining lemma

No new finite computation is needed to verify the theorems above. The supplied $N=3,\ldots,12$ normalization certificate remains auxiliary finite evidence, and no duplicate diagnostic is proposed.

A useful **optional modular certificate**, specifically for the new source-content bottleneck, has the following bounded specification.

### Inputs

- Original indices
  

$$
N_u=9^{18+32u},\qquad 0\le u\le7;
$$


- primes
  

$$
p\in\{7,11,13\};
$$


- modulus $p^9$;
- source-jet ring
  

$$
(\mathbb Z/p^9\mathbb Z)[x]/(x^{9p});
$$


- the exact Chebyshev recurrence, evaluated at $t=1-x$, and at $t=i$ in
  

$$
(\mathbb Z/p^9\mathbb Z)[i].
$$



The largest jet degree is $116$; the largest factorial needed is $116!$, reduced modulo the stated modulus. Terms of degree at least $9p$ contribute zero to the source modulo $p^9$, because $v_p(j!)\ge9$ there. Thus this truncation is justified for this modular calculation only; it is not a truncation of the ordinary error.

### Expected verifiable outputs

For each of the $24$ input pairs $(u,p)$:

1. residues of $b_N,b_{N-1},d,U$, and $I-d^2$ modulo $p^9$;
2. the local paid content exponent
   

$$
r=\min(v_p(b_N),v_p(b_{N-1}));
$$


3. when $r\le4$, the residue
   

$$
\frac{I-d^2}{p^{2r}}
   \pmod{p^{9-2r}},
$$


   with the division explicitly certified;
4. the resulting value, or certified lower truncation, of
   

$$
v_p(c)
   =\min\{v_p(U),\,v_p(I-d^2)-2r\}.
   \tag{12.1}
$$


   A case with $r\ge5$ must be marked unresolved at this precision, not assigned a guessed valuation.

The unit part of $g/p^r$ does not change the valuation in (12.1). The output would therefore concern the **actual source content after its paid local square division**.

This check could reveal odd source-content factors or invalidate an overstrong guess such as $c_N=4$. Even a clean table would establish only these $24$ modular cases. It would not prove SC, a uniform ALL-prime gcd bound, or primitive-error decay.

---

## 13. Final proof status

### New proved statements

- The signed-source Chebyshev analytic construction is valid at every original index.
- Its actual ordinary error satisfies
  

$$
\epsilon_N\asymp R^{-2N},
$$


  with an explicit positive lower bound.
- Its polynomial content is exactly
  

$$
h_N=g_N^2c_N.
$$


- The complete least aggregate clearer, final gcd, and primitive denominator are retained through (8.1)–(8.7).
- The all-prime surviving-divisor theorem and the effective irrationality of $e$ yield the unconditional actual-whole-error bound (10.6).
- On the original domain, $v_2(h_N)=4$, $\gcd(h_N,15)=1$, and $q_N$ is odd.

### Conditional implication

A sub-square-root-factorial bound such as SC would prove that this new producer also has diverging primitive whole errors at the original indices.

### Auxiliary finite evidence

The supplied $N=3,\ldots,12$ certificate has only that finite scope. The optional modular certificate in Section 12 would likewise have only its explicitly bounded scope.

### Exact remaining bottleneck

The missing theorem is a uniform estimate for the explicit scalar source gcd


$$
c_N=
\gcd\!\left(
-\eta(K_N),
\eta((B_N/g_N)^2)-(d_N/g_N)^2
\right)
$$


at the same infinite original indices.

If this gcd is sub-square-root-factorial, the new lower bound rules out success. If it is exceptionally large, that alone still does not prove success: the actual $\lambda_N$, final $G_N$, and $q_N/R^{2N}$ must then be resolved.

Accordingly, the new producer is **not yet proved successful or unsuccessful**. No materially different replacement producer is asserted on the false premise that its failure has already been established.

The global objective—an unconditional proof that $e+\pi$ is rational or irrational—remains open.
