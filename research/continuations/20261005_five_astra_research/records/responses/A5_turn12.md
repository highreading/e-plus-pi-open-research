> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5: CRT obstruction closed; a second binary norm law and a fixed-boundary mixed lift

The mesoscopic analytic argument applies to the **same actual centers** used in the CRT arithmetic calculation. After checking the coordinate and metric bridge, the two results combine unconditionally: the selected CRT primitive center forms grow exponentially and therefore cannot be shrinking irrationality forms.

For the main family $n=4002b,\ b=9^r$, I obtain a further infinite-index result on


$$
r\equiv2\pmod{16}.
$$


Both first normalized contractions vanish modulo $2$, and the next norm digit has a closed binomial formula. In particular, norm depth one is **not uniform**:


$$
r\equiv18\pmod{32}\quad\Longrightarrow\quad v_2(X^TX)\ge2.
$$



I also reduce the complete next mixed digit to a forcing supported at the **five boundary indices $b,\ldots,b+4$**, with the actual inverse and endpoint retained. This gives an explicit formula for the possible defect between the two next digits. **I do not complete the proof that this defect always vanishes, nor produce a counterexample to that assertion.** Thus the requested alignment question remains open, but at a more specific finite-boundary contraction.

No conclusion about rationality or irrationality of $e+\pi$ follows.

---

## 1. Exact center and metric bridge

Write $S=e+\pi$. I distinguish the actual ordinary $B$-coefficient coordinates from the divided coordinates used in the arithmetic calculations.

For a length-$b$ vector $\theta$, put


$$
p_\theta(t)=\sum_{j=0}^{b-1}\theta_j\frac{t^j}{j!},
\qquad
(\mathcal Z\theta)_j=j\theta_{j-1}-\theta_j,
$$


where $\theta_{-1}=\theta_b=0$. Then the exact ordinary coefficient identity is


$$
[t^j](t-1)p_\theta(t)=\frac{(\mathcal Z\theta)_j}{j!}.
\tag{1.1}
$$



The movement of the $Q$-endpoint from coordinate zero to coordinate $b$ is also exact, not a change of center. Namely,


$$
(t-1)\sum_{j=0}^{b-1}t^j=t^b-1.
\tag{1.2}
$$


Thus subtracting the retained factorial vector $(j!)_{j<b}$ from the divided solution changes


$$
e_0+(t-1)p(t)
$$


into


$$
t^b+(t-1)p_{\mathrm{res}}(t).
$$


This explains the endpoint $\omega_b e_b$ in $V_w$.

For the arithmetic metric in question, define explicitly


$$
\omega_j=(n+2)_{\underline j}=j!\binom{n+2}{j},
\qquad
\Omega=\operatorname{diag}(\omega_j^2),
\qquad
W_j=\binom{n+2}{j}.
\tag{1.3}
$$


The falling factorial in (1.3) is explicit; it is not being identified with a differently defined rising-factorial metric.

With


$$
\lambda=\frac{(n!)^2}{2^n},
$$


the supplied actual reconstruction and (1.1) give


$$
\Omega^{1/2}u=\lambda Z_w,\qquad
\Omega^{1/2}v=V_w.
\tag{1.4}
$$


Consequently the actual center is


$$
c_\Omega
=\frac{u^T\Omega v}{u^T\Omega u}
=\frac{Z_w^TV_w}{\lambda Z_w^TZ_w}.
\tag{1.5}
$$


In particular, after


$$
Z_w=2RX,\qquad V_w=4b!Y,
$$


equation (1.5) becomes exactly


$$
c_\Omega=\frac{2b!}{\lambda R}\frac{X^TY}{X^TX}.
\tag{1.6}
$$



The analytic theorem concerns arbitrary positive diagonal metrics in the **ordinary actual coordinates**. Equations (1.1)–(1.5) therefore provide the required bridge to this particular arithmetic metric without changing either column or center.

---

## 2. Analytic audit and unconditional closure of the CRT obstruction

### 2.1 Audit of the mesoscopic step

The strengthening to


$$
3\le b=o(n)
\tag{2.1}
$$


passes the supplied hypotheses.

The essential checks are these.

* The uniform zero-free input is eventually available because $b=o(n)$ implies $b\le n/1000$. No fixed-positive-ratio theorem is evaluated at $c=0$.
* On the two fixed $q$-disks, the positive partition comparison bounds the real part of the actual logarithm by $O(b)$.
* The real anchor is indispensable: together with harmonic estimates and the Cauchy–Riemann equations, it bounds the **whole holomorphic logarithm** and its fixed-order derivatives by $O(b)$.
* Hence the actual finite-$n$ saddle moves by $O(b/n)$, and its exponent changes by $O(b^2/n)=O(b)$. The characteristic insertion is retained.
* The remote/main ratio is
  

$$
O\!\left(\sqrt n\,e^{-n/400+Cb}\right)=o(1).
$$


  The two minus-contour connectors are retained and are exponentially smaller.
* The whole exponential residual and the coordinate-zero endpoint have relative sizes bounded by
  

$$
\frac{e^{Cb}}{n!\sqrt n},
  \qquad
  \frac{C\sqrt n\,e^{Cb}}{n!B_0},
$$


  respectively. They are factorially smaller than the signed $F_j/P_j$ term.

These estimates are uniform in $0\le j\le b$. Thus every coordinate error has the same eventual sign and the same two-sided logarithmic estimate:


$$
\operatorname{sign}(c_j-S)=(-1)^{n+1},
\qquad
\log|c_j-S|=-2n\log(1+\sqrt2)+O(b+1).
\tag{2.2}
$$


The exact convex identity


$$
c_\Omega-S
=
\sum_j
\frac{\omega_j^2u_j^2}{\sum_\ell\omega_\ell^2u_\ell^2}(c_j-S)
\tag{2.3}
$$


then transfers both the sign and the two-sided bound to (1.5). This step requires a diagonal positive metric, which (1.3) supplies.

Normality and $u_j\ne0$ are retained throughout. Equation (2.2) is a statement about the **whole evaluated error**, not a logarithmic component alone.

### 2.2 Same-center CRT conclusion

Use precisely the previously specified CRT sequence:


$$
b=9^r,\qquad
K=3+\lfloor\log_2(b+4)\rfloor,
$$


with $h$ the least integer at least $b^3$ satisfying


$$
h\equiv1\pmod{2^K},\qquad h\equiv0\pmod{3b},
\qquad n=2h.
\tag{2.4}
$$


Then $n=2b^3+O(b^2)$, so (2.1) applies.

Retain the least actual lift denominator and the **final** Gram gcd:


$$
N_B=d_B[u,v],
$$




$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
p_n=H_B/g_B,\qquad q_n=A_B/g_B.
\tag{2.5}
$$


The established CRT arithmetic laws, including the corrected $b+2$ ternary tail, give on these same centers


$$
v_2(q_n)=\frac{3n}{2}-v_2(b!)-s_2(n)-1,
\tag{2.6}
$$


and, with $a=2r,\ k=v_3(n)$ and


$$
\beta=k+v_3(b!)-a,
$$




$$
v_3(q_n)=n-s_3(n)+1-\beta.
\tag{2.7}
$$


Their corresponding final-gcd depths remain


$$
v_2(g_B)=\frac{3n}{2}-s_2(n)+v_2(b!)+3,
\qquad
v_3(g_B)=2v_3(n!)+\beta.
\tag{2.8}
$$



Since $n$ is even, the analytic audit now gives, unconditionally,


$$
\epsilon_n=\frac{p_n}{q_n}-S<0
\quad\text{eventually},
\qquad
\log|\epsilon_n|=-2n\log(1+\sqrt2)+o(n).
\tag{2.9}
$$


Thus the whole primitive evaluated form


$$
L_n=q_nS-p_n=-q_n\epsilon_n
\tag{2.10}
$$


is eventually positive and nonzero, and


$$
\begin{aligned}
\log L_n
={}&v_2(q_n)\log2+v_3(q_n)\log3\\
&+\sum_{\ell\ne2,3}v_\ell(q_n)\log\ell
-2n\log(1+\sqrt2)+o(n).
\end{aligned}
\tag{2.11}
$$


All the omitted prime contributions in a lower bound are nonnegative. Therefore


$$
\boxed{
\liminf_{r\to\infty}\frac{\log L_n}{n}
\ge
\frac32\log2+\log3-2\log(1+\sqrt2)>0.
}
\tag{2.12}
$$



This closes the scoped CRT obstruction: **these selected primitive center forms grow exponentially.** It does not exclude other endpoint directions or decide the nature of $S$.

---

# Part II. The main binary family

From here onward the indices are exclusively


$$
b=9^r,\qquad n=4002b,
\tag{3.1}
$$


not the CRT allocation.

Write


$$
h=n/2,\quad
R=2^h\binom{2h}{h},\quad
X=\frac{Z_w}{2R},\quad
Y=\frac{V_w}{4b!}.
$$


Both columns are $2$-integral. Put


$$
\alpha=v_2(X^TX),\qquad \gamma=v_2(X^TY).
\tag{3.2}
$$


The norm is positive, and the retained same-family ternary theorem makes the complete mixed contraction nonzero. Hence these valuations are finite.

---

## 3. A closed next norm digit on $r\equiv2\pmod{16}$

Assume


$$
r\equiv2\pmod{16}.
\tag{3.3}
$$


Define


$$
D=\frac{b-81}{128},
\qquad
C=\frac{A-8}{16}=4002D+2532,
\qquad
A=\frac{h-1}{4}.
\tag{3.4}
$$


Then


$$
b=128D+81,\qquad
d=\frac{b-1}{8}=16D+10,\qquad
A=16C+8.
$$



The established first-column formula was


$$
X_{8k}\equiv
\binom Ak\binom{2A+d-k}{d-k}\pmod2.
\tag{3.5}
$$


Lucas reduction of its low four binary digits shows that its support occurs in equal pairs:


$$
\boxed{
X_{128t}\equiv X_{128t+64}\equiv e_t\pmod2,
\qquad 0\le t\le D,
}
\tag{3.6}
$$


where


$$
e_t=
\binom Ct\binom{2C+1+D-t}{D-t}\pmod2,
\tag{3.7}
$$


and every other coordinate of $X$ is even.

Indeed, the permitted $k$'s are $16t$ and $16t+8$. For both choices the low digits contribute one, and their higher-digit factors are exactly (3.7).

An odd square is $1\bmod4$, while an even square is $0\bmod4$. Hence the second norm digit depends only on (3.6):


$$
\frac{X^TX}{2}\equiv\sum_{t=0}^D e_t\pmod2.
$$


Over $\mathbb F_2$,


$$
(1+z)^C(1-z)^{-2C-2}=(1+z)^{-C-2}.
$$


Taking the coefficient of $z^D$ proves


$$
\boxed{
\frac{X^TX}{2}
\equiv
\binom{C+D+1}{D}\pmod2.
}
\tag{3.8}
$$



Thus


$$
\boxed{
\alpha=1
\iff
D\mathbin{\&}(C+1)=0.
}
\tag{3.9}
$$


When this test fails, it proves $\alpha\ge2$, not its exact larger value.

This is also an explicit carry rule: compute the binary digits of


$$
C+1=4002D+2533
$$


using initial carry $2533$, and reject a unit whenever a digit of $D$ and the corresponding output digit are both one.

### An infinite second-depth obstruction

Write $r=2+16t$. Since


$$
9^{16}\equiv129\pmod{256},
$$


we have


$$
D=\frac{9^r-81}{128}\equiv t\pmod2.
$$


But $C+1=4002D+2533$ is odd. Consequently,


$$
\boxed{
r\equiv18\pmod{32}
\quad\Longrightarrow\quad
D\mathbin{\&}(C+1)\ne0
\quad\Longrightarrow\quad
\alpha\ge2.
}
\tag{3.10}
$$



The finite depth-one result at $r=2$ therefore cannot be promoted to a uniform depth-one theorem.

---

## 4. A fixed-boundary formula for the complete $Q$-solution

This section derives a new reduction of the next mixed calculation. It is valid on (3.3).

Let


$$
T(a)_{ij}=\binom a{j-i},\qquad 0\le i,j<b,
$$


and let $P$ be the lower Pascal matrix. Set


$$
(c_1,c_2,c_3,c_4)=(-1,2,-3,3).
$$


Modulo $16$, the actual contact factorization is


$$
P^{-1}\widetilde N=(I+2E)T(n),
\tag{4.1}
$$


where


$$
E_{ij}
=
\sum_{s=1}^4c_s
\sum_{t=0}^s
\binom i{s-t}\binom nt
\binom{-t}{j+s-i-t}.
\tag{4.2}
$$



The complete logarithmic forcing divided by $b!$ is zero at this precision by its retained valuation bound. The exponential residual retains exactly the tails $b,\ldots,b+4$.

### 4.1 Why only five boundary inputs are needed

Let $a$ be the finitely supported infinite vector


$$
a_{b+t}=\frac{(b+t)!}{b!},\quad 0\le t\le4,
\qquad a_k=0\quad\text{otherwise}.
$$


The exact Vandermonde convolution underlying the residual gives


$$
P^{-1}(\rho/b!)
\equiv
(I+2E_\infty)T_\infty(2n)a
\pmod{16}.
\tag{4.3}
$$


All sums here are finite. Let $\Pi$ denote restriction to indices below $b$, and put


$$
v=T_\infty(2n)a,\qquad
B_t=v_{b+t}
=\sum_{u=t}^4\frac{(b+u)!}{b!}\binom{2n}{u-t}.
\tag{4.4}
$$


Then the part of $v$ outside the actual matrix is supported **exactly within**


$$
b,\ b+1,\ b+2,\ b+3,\ b+4.
\tag{4.5}
$$



Solving (4.3) with the actual finite inverse, and using
$T_\infty(-2n)T_\infty(2n)a=a$, gives


$$
\boxed{
\begin{aligned}
\eta_i\equiv{}&
-\sum_{t=0}^4\binom{-2n}{b+t-i}B_t\\
&+2\left[
T(-2n)(I-2E+4E^2-8E^3)\,
\left(\sum_{t=0}^4E_{\cdot,b+t}B_t\right)
\right]_i
\pmod{16}.
\end{aligned}
}
\tag{4.6}
$$


Here


$$
\eta=T(-n)\widetilde N^{-1}(\rho/b!).
$$


Thus (4.6) is a formula for the **complete actual** residual solution. It is not an infinite-matrix replacement of the finite inverse: the second line is precisely the correction for the missing boundary columns.

### 4.2 The boundary map has rank two at the required precision

On (3.3),


$$
n\equiv66\pmod{256},\qquad b\equiv81\pmod{128}.
$$


Consequently, modulo $8$, (4.2) agrees with its $n=2$ expression. For $k\ge b>i$,


$$
E_{ik}\equiv(-1)^{k-i}
\left((k-i)B_i^\circ+D_i^\circ\right)\pmod8,
\tag{4.7}
$$


where


$$
B_i^\circ=2+3i+3\binom i2,\qquad
D_i^\circ=2i+3\binom i2-6\binom i3.
\tag{4.8}
$$


Thus the boundary map is generated by the two functionals


$$
\sum_t(-1)^tB_t,\qquad
\sum_t t(-1)^tB_t.
$$



Direct evaluation of (4.4), using only the stated low digits, yields


$$
(B_0,\ldots,B_4)\equiv(5,10,6,8,8)\pmod{16}.
\tag{4.9}
$$


Therefore


$$
\boxed{
\sum_{t=0}^4E_{i,b+t}B_t
\equiv
t_i:=(-1)^{i+1}
\left(6+6i-15\binom i3\right)
\pmod8.
}
\tag{4.10}
$$



Moreover,


$$
Et\equiv0\pmod2.
\tag{4.11}
$$


To check this, $t_i\bmod2=\binom i3$, supported at $i\equiv3\pmod4$. In $E\bmod2$, the only potentially surviving lower-shift contribution is the $s=4$ term. Its contribution at $i=4q+3$ is $q\bmod2$. The upper $s=4$ contribution counts the remaining indices $3\bmod4$; since $(b-1)/4$ is even, its parity is also $q$. They cancel. The other terms vanish by their low digits.

Combining (4.6)–(4.11) gives the economical formula


$$
\boxed{
\eta
\equiv
-\left(\sum_{t=0}^4
 B_t\binom{-2n}{b+t-i}\right)_{i<b}
+2T(-2n)t-4T(-2n)Et
\pmod{16}.
}
\tag{4.12}
$$


The absent higher inverse term is justified by (4.11), not discarded by convention.

The actual endpoint is still


$$
Y_j=\frac{W_b\delta_{j,b}+W_j(j\eta_{j-1}-\eta_j)}4.
\tag{4.13}
$$



---

## 5. The first mixed digit vanishes on the whole norm-zero class

The preceding boundary formula proves more than a prescription for computation.

For any $j\equiv0\pmod{64}$, set $L=b-1-j$. From (4.10), finite binomial moment summation gives


$$
(T(-2n)t)_j
\equiv
-6\binom{2n+L}{L}\pmod4.
\tag{5.1}
$$


For example, the required identity is


$$
\sum_{k=0}^L
\binom{a+k-1}{k}\binom{k}{v}
=
\binom{a+v-1}{v}\binom{a+L}{L-v}.
\tag{5.2}
$$


In (5.1), the other terms vanish modulo $4$ because $j$ is divisible by $64$, $2n\equiv4\pmod{16}$, and
$\binom{2n+2}{3}\equiv0\pmod4$.

Using (4.9), the three possibly nonzero boundary terms modulo $8$, together with (5.1), yield


$$
\boxed{
\eta_j/4\equiv\binom{2n+L}{L}\pmod2
\qquad(j\equiv0\pmod{64}).
}
\tag{5.3}
$$


The division is justified by the preceding modulo-$8$ calculation.

Now write


$$
n=128C+66,\qquad b=128D+81.
$$


For $j=128t+64s,\ s=0,1$, Lucas reduction in (4.13) and (5.3) gives


$$
\boxed{
Y_{128t}\equiv Y_{128t+64}\equiv e_t\pmod2,
}
\tag{5.4}
$$


with the same $e_t$ as (3.7).

Since $X$ is even off these paired positions,


$$
\boxed{
X^TY\equiv X^TX\equiv0\pmod2
\quad\text{throughout }r\equiv2\pmod{16}.
}
\tag{5.5}
$$


Thus both divisions requested in the question are legitimate on this whole class, not merely at $r=2$.

---

## 6. Explicit next mixed contraction and the remaining alignment defect

Here is a complete fixed-boundary formula for the next digit.

Use the known inverse-Pascal transform of the full normalized $P$-forcing:


$$
F_i=(-1)^i
\left(
2-i+3\binom i2-\binom i3
+4\binom i4-4\binom i5
\right)\pmod8.
$$


Compute


$$
\theta^P
=
T(-2n)(I-2E+4E^2)F\pmod8,
\tag{6.1}
$$


and compute $\eta\bmod16$ by (4.12). Extend both by zero at $-1,b$, and define


$$
A_j=W_j(j\theta^P_{j-1}-\theta^P_j),
$$




$$
B_j^{\rm act}
=W_b\delta_{j,b}+W_j(j\eta_{j-1}-\eta_j).
\tag{6.2}
$$


Then


$$
A_j\equiv2X_j\pmod8,\qquad
B_j^{\rm act}\equiv4Y_j\pmod{16}.
$$


Because of these divisibilities and (5.5),


$$
\boxed{
\frac{X^TY}{2}
\equiv
\frac1{16}\sum_{j=0}^b A_jB_j^{\rm act}
\pmod2.
}
\tag{6.3}
$$


The numerator is evaluated modulo $32$ before division. The supplied precisions suffice:
an error $8$ in $A_j$ multiplies a multiple of $4$, and an error $16$ in $B_j^{\rm act}$ multiplies a multiple of $2$.

Together, (3.8) and (6.3) are explicit finite-boundary contractions for the two requested next digits.

### An integral binary module—without dividing by $6$

Let $e$ be the $0$-$1$ vector with


$$
e_{128t}=e_{128t+64}=e_t
$$


and zero elsewhere. Choose residues $x=X\bmod4,\ y=Y\bmod4$, and write


$$
x=e+2\xi,\qquad
y=e+z+2\upsilon
\quad\text{in }(\mathbb Z/4\mathbb Z)^{b+1}.
\tag{6.4}
$$


Here $z$ is the $0$-$1$ parity vector of $Y-e$. Equation (5.4) shows that $z$ is supported away from the indices divisible by $64$, so $e^Tz=0$.

Expanding (6.4) gives the exact next-digit identity


$$
\boxed{
\frac{X^TY}{2}
=
\frac{X^TX}{2}
+\Delta
\pmod2,
}
\tag{6.5}
$$


where


$$
\boxed{
\Delta
=
e^T(\xi+\upsilon)+\xi^Tz
\pmod2.
}
\tag{6.6}
$$



This is an integral construction. No orthogonal projection with denominator $6$, or denominator $2$, has been treated as integral. The one-digit loss is retained explicitly in (6.4)–(6.6).

The support statement must also be precise:

* the **forcing boundary** for the complete $Q$-part of $\Delta$ is $b,\ldots,b+4$;
* its propagation through the actual finite inverse is (4.6), or the rank-two reduction (4.12);
* the endpoint is at coordinate $b$;
* $\Delta$ itself is **not asserted to be coordinate-boundary-supported**. In particular, $\xi^Tz$ can involve interior coordinates.

This identifies the obstruction that a first-digit or pair-support argument misses.

### Alignment status

The two next digits align if and only if


$$
\Delta=0.
\tag{6.7}
$$


The finite $r=2$ control has $\Delta=0$, consistently with both depths being one. I have not established (6.7) for every $r\equiv2\pmod{16}$, and I have not shown that it fails.

In particular, (3.10) produces an infinite subclass on which a valid alignment theorem would force


$$
\gamma\ge2.
$$


It does not itself prove that assertion.

---

## 7. Final gcd and the still-needed relative bound on the main family

Nothing above changes the actual local identities. With $s=s_2(n)$,


$$
v_2(A_B)=3n-2s+2+\alpha,
$$




$$
v_2(H_B)=\frac{3n}{2}-s+v_2(b!)+3+\gamma,
$$


and


$$
\boxed{
v_2(g_B)=
\min\left\{
3n-2s+2+\alpha,\,
\frac{3n}{2}-s+v_2(b!)+3+\gamma
\right\}.
}
\tag{7.1}
$$


Therefore the actual primitive denominator satisfies


$$
\boxed{
v_2(q_n)=
\max\left\{
0,\frac{3n}{2}-v_2(b!)-s_2(n)-1-(\gamma-\alpha)
\right\}.
}
\tag{7.2}
$$



The target sufficient estimate remains


$$
\gamma-\alpha\le2000b+o(n).
\tag{7.3}
$$


The new norm law does not prove (7.3). Nor may the lower bounds $\alpha,\gamma\ge1$ be subtracted to obtain a relative bound.

For these fixed-ratio centers the retained whole signed-error theorem gives


$$
\epsilon_n=c_n-S<0\quad\text{eventually},
$$




$$
\log|\epsilon_n|
=-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$


Their complete primitive evaluated form remains


$$
q_nS-p_n=-q_n\epsilon_n>0
\quad\text{eventually}.
\tag{7.4}
$$



---

## 8. Derived bounded control at $b=729,\ n=2917458$

The product is


$$
\boxed{4002\cdot729=2917458.}
$$



This index is $r=3$, not in (3.3). It is useful as a finite original-center test of the general normalized finite formulas, not as a test proving the infinite alignment assertion.

### 8.1 Finite normalized central-coefficient sums

Use common raw precision


$$
2^{10}=1024.
$$


This supplies $X\bmod512$ and $Y\bmod256$, hence both normalized contractions modulo $256$.

Let


$$
D_i=\frac{(2h+i)!}{(2h)!},\qquad
B_l=\frac{D_l[t^{2h-l}](1+2t+2t^2)^{2h}}{R}.
$$


The exact normalized formulas are


$$
B_{2j}
=
\left(\prod_{t=1}^j(2h+2t-1)\right)
(h)_{\underline j}
\sum_{r\ge0}
\frac{2^r(r!)^2}{(2r)!}
\binom{h-j}{r}\binom{h+j}{r},
\tag{8.1}
$$




$$
B_{2j+1}
=
\left(\prod_{t=0}^j(2h+2t+1)\right)
(h)_{\underline{j+1}}
\sum_{r\ge0}
\frac{2^r(r!)^2}{(2r+1)!}
\binom{h-j-1}{r}\binom{h+j}{r}.
\tag{8.2}
$$


Both coefficient ratios in the summands have valuation $v_2(r!)$. Since


$$
v_2(12!)=10,
$$


only


$$
0\le r\le11,\qquad 0\le l\le22
\tag{8.3}
$$


are needed modulo $1024$. All denominators remaining after extracting powers of two are odd units.

Now


$$
f_i^0/R=\sum_{l=0}^i
\binom il\frac{D_i}{D_l}B_l.
\tag{8.4}
$$


The factorial ratio has valuation at least $v_2((i-l)!)$. Consequently only


$$
0\le i\le33
\tag{8.5}
$$


are needed at this precision. Thus no expansion of degree comparable to $n$ is required.

### 8.2 Contact and complete residual cutoffs

In the integral divided-power ring,


$$
\phi^n=(1+2U)^h.
$$


Modulo $1024$, retain only powers $U^k$ with $k\le9$. Since $\deg U=4$, the divided contact coefficients satisfy


$$
d_s\equiv0\pmod{1024}\qquad(s>36).
\tag{8.6}
$$



At $b=729$,


$$
v_2\!\left(\frac{(b+9)!}{b!}\right)=10.
$$


Therefore the complete exponential residual needs only tails


$$
b,\ldots,b+8.
\tag{8.7}
$$


The boundary argument of Section 4 applies with these nine indices and the contact coefficients from (8.6).

For the whole logarithmic forcing,


$$
h=1458729,\qquad
v_2(729!)=723,\qquad
\lfloor\log_2(2n+b-1)\rfloor=22.
$$


Hence


$$
\boxed{
v_2(h_i^F/b!)
\ge1458729+1-44-723
=1457963>10.
}
\tag{8.8}
$$


Its omission modulo $1024$ is therefore certified for the entire contribution.

### 8.3 Structured inverse, not a dense cubic inverse

With the general divided coefficients, set


$$
E_{ij}
=
\sum_{s=1}^{36}\frac{d_s}{2}
\sum_{t=0}^s
\binom i{s-t}\binom nt
\binom{-t}{j+s-i-t}.
\tag{8.9}
$$


Then


$$
P^{-1}\widetilde N=(I+2E)T(n)\pmod{1024}.
$$



The inverse is the explicit Newton/Neumann polynomial


$$
(I+2E)^{-1}
\equiv\sum_{\ell=0}^{9}(-2E)^\ell\pmod{1024}.
\tag{8.10}
$$


It can be obtained by Newton doubling and applied to vectors by Horner evaluation.

No dense $729^3$ operation is necessary. Indeed, writing $L$ for the lower shift,


$$
E=
\sum_{s=1}^{36}\frac{d_s}{2}
\sum_{t=0}^s\binom nt\,
\operatorname{diag}\!\binom i{s-t}\,
L^{s-t}T(-t).
\tag{8.11}
$$


All $T(-t)x$, $0\le t\le36$, can be generated successively using $T(-1)$, each in linear time by an alternating suffix sum. This gives a structured vector application of $E$, followed by (8.10).

### A specific finite prediction

Here


$$
d=91,\qquad A=364682,\qquad A\bmod128=10.
$$


The only possible submasks $k\le91$ of $A$ are


$$
0,\ 2,\ 8,\ 10.
$$


For every one, $d-k$ has the $2^4$-bit set, as does $2A$. Thus the established leading-column formula gives


$$
\boxed{
X\equiv0\pmod2,\qquad X^TX\equiv0\pmod4
}
\tag{8.12}
$$


at this prescribed index. This prediction has finite scope.

---

# Concluding ledger

## (1) New result and proof status

**Closed unconditionally**

* The mesoscopic analytic theorem applies to the exact CRT arithmetic center through the explicit ordinary/divided-coordinate metric bridge.
* The same CRT primitive forms, after the final gcd, satisfy the positive exponential lower rate (2.12). This selected shrinking-form route is excluded.

**Proved for the main binary family on $r\equiv2\pmod{16}$**

* Equal paired first-column support, (3.6).
* The next norm digit
  

$$
(X^TX)/2\equiv\binom{C+D+1}{D}\pmod2.
$$


* The infinite obstruction
  

$$
r\equiv18\pmod{32}\Longrightarrow v_2(X^TX)\ge2.
$$


* The matching $Y$-parity on the paired support, and therefore $X^TY\equiv0\pmod2$ on the entire class.
* A complete five-boundary-input formula for $Y\bmod4$, retaining the actual inverse and endpoint.
* The explicit integral next-digit defect (6.6), without using a nonintegral binary projection.

**Not proved**

The vanishing or nonvanishing of that defect for all assigned indices, the sufficient relative bound (7.3), or irrationality or rationality of $e+\pi$.

## (2) Exact remaining bottleneck

At the next binary layer the precise unresolved assertion is


$$
\boxed{
e^T(\xi+\upsilon)+\xi^Tz=0\pmod2,
}
$$


with $x,y$ computed from (6.1) and the fixed-boundary formula (4.12).

Even a positive answer would establish only one additional alignment digit. The infinite subclass (3.10) would then require another lift. The main sufficient obligation remains a justified bound on $\gamma-\alpha$, not uniform unit or depth-one assertions.

## (3) Bounded exact computation request

If the coordinator chooses to perform one additional computation, use only


$$
\boxed{
n=2917458,\quad b=729,\quad m_w=1,\quad\text{raw modulus }1024.
}
$$



Use (8.1)–(8.11), with:

* normalized central sums $l\le22,\ r\le11$;
* normalized forcing support $i\le33$;
* divided contact cutoff $s\le36$;
* factorial tails $b,\ldots,b+8$;
* the whole-logarithmic-forcing certificate (8.8);
* structured vector inversion, not a dense cubic inverse.

**Expected verifiable outputs**

1. $X\bmod512$, $Y\bmod256$, and confirmation of (8.12).
2. $X^TX\bmod256$, $X^TY\bmod256$.
3. Since $X$ is even, also
   

$$
(X^TX)/4\bmod256,\qquad (X^TY)/2\bmod256,
$$


   using the extra supplied $X$-bit.
4. Exact depths whenever the residues certify them; otherwise explicitly stated lower bounds.
5. With $s_2(n)=8$, comparison against the actual local identities
   

$$
v_2(A_B)=8752360+\alpha,\qquad
   v_2(H_B)=4376905+\gamma,
$$


   

$$
v_2(g_B)=\min\{8752360+\alpha,\ 4376905+\gamma\},
$$


   

$$
v_2(q_n)=\max\{0,\ 4375455+\alpha-\gamma\}.
$$



No unit or depth-equality prediction is imposed on this control. Its outcome would be finite corroboration or falsification of the finite formulas, not a proof of an infinite relative-valuation assertion.
