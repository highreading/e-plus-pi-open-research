> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5 turn 7: an infinite carry obstruction to the proposed unit theorem

I do **not** obtain the requested two-prime exclusion. I do obtain a new obstruction which shows that the norm-unit assertion cannot hold on the entire even-exponent class.

Write


$$
a=2r,\qquad b=9^r,\qquad n=4002b,\qquad r\ge1,
$$


and retain the prescribed normalizations


$$
X=\frac{Z_w}{2R},\qquad Y=\frac{V_w}{4b!},
\qquad
R=2^{n/2}\binom n{n/2}.
$$


Set


$$
d=\frac{b-1}{8},\qquad
h=\frac n2=2001b,\qquad
A=\frac{h-1}{4}=4002d+500.
$$



The new exact norm calculation is


$$
\boxed{
X^TX\equiv \binom{A+d}{d}
=\binom{4003d+500}{d}\pmod2.
}
\tag{1}
$$


More strongly, the entire first binary digit of $X$ is


$$
\boxed{
X_{8k}\equiv
\binom Ak\binom{2A+d-k}{d-k}\pmod2
\quad(0\le k\le d),
}
\tag{2}
$$


and every other coordinate is zero modulo $2$, including the endpoint $j=b$.

Consequently,


$$
\boxed{
X^TX\text{ is a }2\text{-adic unit}
\iff d\mathbin{\&}(4002d+500)=0,
}
\tag{3}
$$


where $\&$ denotes bitwise intersection.

In particular, on the infinite class


$$
\boxed{r\equiv2\pmod{16}\quad\text{equivalently }a\equiv4\pmod{32},}
$$


the norm is even. Thus the proposed norm-and-mixed **unit theorem on all $a=2r$** is false.

This does **not** disprove a suitable relative-depth theorem. A larger norm valuation can help the denominator lower bound if the complete mixed contraction does not acquire a corresponding larger valuation. That mixed-contraction question remains open here.

I also give below an exact modulo-$16$ reduction of the complete $Q$-column, and a modulo-$8$ reduction of the $P$-column, using only finite binomial sums and a cubic contact-inverse correction. These retain the growing boundaries, endpoint column, and full forcing. They determine both evaluated contractions modulo $4$, but I do not claim a uniform nonvanishing result from that reduction.

---

## 1. Exact arithmetic setting

Throughout this report,


$$
r\ge1,\quad b=9^r,\quad n=4002b,\quad h=n/2,\quad \ell=n+2.
$$


Thus


$$
b\equiv1\pmod8,\qquad h\equiv1\pmod8,\qquad n\equiv2\pmod{16}.
$$



Let $P=P_b$ be the $b\times b$ Pascal matrix,


$$
P_{ij}=\binom ij,
$$


and let


$$
T(t)_{ij}=
\begin{cases}
\binom t{j-i},&j\ge i,\\
0,&j<i.
\end{cases}
$$


All these are the actual finite $b\times b$ matrices. In particular,


$$
T(t)T(u)=T(t+u)
$$


holds with the genuine finite boundaries.

Put


$$
W_j=\binom{\ell}{j}.
$$


For a length-$b$ divided-coefficient vector $\theta$, extend it by
$\theta_{-1}=\theta_b=0$, and write


$$
(\mathcal Z\theta)_j=j\theta_{j-1}-\theta_j,
\qquad 0\le j\le b.
$$



The exact reconstructed normalized columns are


$$
\frac{Z_w}{R}
=\operatorname{diag}(W_j)\mathcal Z\theta^P,
\qquad
\theta^P=T(-n)\widetilde N^{-1}(f^0/R),
\tag{4}
$$


and


$$
\frac{V_w}{b!}
=
W_b e_b+\operatorname{diag}(W_j)\mathcal Z\eta,
\qquad
\eta=T(-n)\widetilde N^{-1}(\rho/b!).
\tag{5}
$$


The vector $\rho$ includes the exponential tail, the complete logarithmic forcing, and the exact endpoint subtraction.

I use the established whole-column integrality


$$
X,Y\in\mathbb Z_2^{b+1}.
$$


The calculations below identify new digits after those divisions; they do not replace the evaluated contractions by column contents.

---

## 2. A stronger finite divided-power reduction on this class

Let


$$
\phi(z)=1-z+\frac{z^2}{2},\qquad
d_s=s![z^s]\phi(z)^n.
$$


Work in the integral divided-power coefficient ring. We have


$$
\phi(z)^2=1+2U(z),
$$


where $U$ has divided coefficients


$$
(-1,2,-3,3)
$$


in degrees $1,2,3,4$.

Because $h\equiv1\pmod8$,


$$
(1+2U)^h
=\sum_{k=0}^h 2^k\binom hk U^k
\equiv1+2U\pmod{16}.
$$


Indeed:

- $2h\equiv2\pmod{16}$;
- $4\binom h2$ is divisible by $16$;
- $8\binom h3$ is divisible by $16$;
- every term with $k\ge4$ contains $16$.

Therefore, uniformly in the growing dimension,


$$
\boxed{
(d_0,d_1,d_2,d_3,d_4)
\equiv(1,-2,4,-6,6)\pmod{16},
\qquad d_s\equiv0\pmod{16}\quad(s>4).
}
\tag{6}
$$



This is a coefficient statement in the divided-power ring, not an inference from $n\bmod16$ about arbitrary binomial coefficients. Higher binary digits of the binomial factors below are still retained.

The contact matrix consequently satisfies


$$
\widetilde N\equiv B(n)+2C\pmod{16},
\qquad B(n)=PT(n),
\tag{7}
$$


where the integer matrix $C$ is


$$
\begin{aligned}
C_{ij}={}&
-\binom{n+i}{1}\binom{n+i-1}{j}
+2\binom{n+i}{2}\binom{n+i-2}{j}\\
&-3\binom{n+i}{3}\binom{n+i-3}{j}
+3\binom{n+i}{4}\binom{n+i-4}{j}.
\end{aligned}
\tag{8}
$$



In particular, all inverse corrections through modulus $16$ can be kept explicitly.

---

## 3. The normalized $P$-forcing has a fixed short residue

The normalization formulas supplied in turn 6 yield, on the present class, the stronger residue


$$
\boxed{
f^0/R\equiv(2,1,3,1,4,4,0,\ldots,0)^T\pmod8.
}
\tag{9}
$$


Thus modulo $4$,


$$
f^0/R\equiv(2,1,3,1,0,\ldots,0)^T.
\tag{10}
$$



Here is a derivation, including the support cutoff.

Use the notation


$$
B_l=\frac{D_lA_l}{R},
\qquad
D_l=\frac{(2h+l)!}{(2h)!}
$$


from the normalized coefficient sums. Their exact formulas show that each summand of $B_{2j}$ has valuation at least


$$
v_2((h)_{\!j})+v_2(r!),
$$


and each summand of $B_{2j+1}$ has valuation at least


$$
v_2((h)_{\!j+1})+v_2(r!).
$$


Since $8\mid h-1$, this gives


$$
B_l\equiv0\pmod8\qquad(l\ge3).
\tag{11}
$$



For $l=0,1,2$, terms with $r\ge4$ vanish modulo $8$, since $v_2(r!)\ge3$. Direct substitution in the remaining terms, using $8\mid h-1$, gives


$$
B_0\equiv2,\qquad B_1\equiv3,\qquad B_2\equiv3\pmod8.
\tag{12}
$$


For example,


$$
B_0=1+h^2+
\frac{h^2(h-1)^2}{6}+\cdots\equiv2\pmod8.
$$


The corresponding corrections in $B_1,B_2$ each contain enough powers from $h-1$ to vanish modulo $8$.

Now


$$
\frac{f_i^0}{R}
=\sum_{l=0}^i
\binom il\frac{D_i}{D_l}B_l.
\tag{13}
$$


Only $l=0,1,2$ remain modulo $8$. Since $n\equiv2\pmod{16}$, evaluating $i=0,\ldots,5$ gives precisely


$$
2,1,3,1,4,4.
$$


For $i\ge6$, the surviving consecutive products contain $n+6$, which is divisible by $8$, or an earlier factor already sufficient for the required vanishing. This proves (9).

The short forcing residue does **not** make the reconstructed weighted column local: the finite inverse Pascal and Toeplitz transforms still run to $b-1$.

---

## 4. Proof of the whole-column formula (2)

Set


$$
M=\frac{b-1}{4}=2d,\qquad
L=\frac{h+1}{2}=2A+1.
$$



### 4.1 Inverse Pascal transform of the forcing

Let


$$
g=P^{-1}(f^0/R).
$$


From (10),


$$
g_i\equiv
(-1)^i\left(
2-i+3\binom i2-\binom i3
\right)\pmod4.
\tag{14}
$$


Consequently,


$$
g_{4q}/2\equiv1+q\pmod2,
\qquad
g_i\equiv
\begin{cases}
0,&4\mid i,\\
1,&4\nmid i
\end{cases}
\pmod2.
\tag{15}
$$



Modulo $4$, write


$$
\widetilde N=B(n)+2E_0,
$$


where $E_0$ can be taken modulo $2$ as the sum of the $s=1,3,4$ correction columns. Then


$$
\theta^P
\equiv
T(-2n)g
-2T(-2n)P^{-1}E_0T(-n)g
\pmod4.
\tag{16}
$$



The second term is the contact-inverse carry. It must be evaluated, not discarded merely because the matrix is a unit.

### 4.2 The contact-inverse carry vanishes at indices divisible by $4$

Let


$$
y^0=T(-n)g\pmod2.
$$


The finite upper boundary $b-1=4M$ gives, for $0\le q<M$,


$$
\boxed{
y^0_{4q}=y^0_{4q+2}
=
\binom{L+M-q-1}{M-q-1}\pmod2,
}
\tag{17}
$$


while


$$
y^0_{4M}=0.
\tag{18}
$$


These follow by summing the appropriate even and odd terms of
$(1+S)^{-2h}$; the last singleton coordinate in (18) is essential.

For every nonnegative $m$,


$$
(P^{-1}(\binom{n+i}{m})_{i<b})_j
=\binom n{m-j}.
$$


Thus, at an index $i$ divisible by $4$,


$$
(P^{-1}E_0y^0)_i
=
\sum_{j<b}y^0_j
\sum_{s\in\{1,3,4\}}
\binom{j+s}{s}\binom n{j+s-i}
\pmod2.
\tag{19}
$$



The $s=1,3$ terms vanish: if the final binomial is odd, then $j+s-i$ is even, whereas the odd lower digit of $s$ makes $\binom{j+s}{s}$ even.

For $s=4$, pair $j=4q$ with $j=4q+2$. Their $y^0$-values agree by (17), and their factors $\binom{j+4}{4}$ agree modulo $2$. The remaining pair is


$$
\binom n{4(q+1)-i}
+
\binom n{4(q+1)-i+2}.
$$


Since $n=2h$ with $h$ odd, its reduction is


$$
\binom h{2u}+\binom h{2u+1}=0\pmod2.
\tag{20}
$$


The unpaired terminal value vanishes by (18).

It follows that


$$
(P^{-1}E_0y^0)_{4q}=0\pmod2.
$$


Moreover $T(-2n)$ shifts only by multiples of $4$ modulo $2$. Therefore the entire inverse-carry term in (16) vanishes at indices divisible by $4$.

This cancellation uses the true finite boundary. It is not an infinite-transform replacement.

### 4.3 The first divided digit at multiples of $4$

The formal-series identity


$$
(1+z)^{-4h}
\equiv
(1+z^4)^{-h}
-2h z^2(1+z^4)^{-h-1}
\pmod4
\tag{21}
$$


gives, for $0\le q\le M$,


$$
\frac{\theta^P_{4q}}2
\equiv
(1+q)\binom{h+M-q}{M-q}\pmod2.
\tag{22}
$$


To see the cancellation explicitly, put $H=M-q$. The two sums apart from
$(1+q)\sum_{k=0}^H\binom{-h}{k}$ are


$$
\sum_{k=0}^H k\binom{-h}{k},
\qquad
-h\sum_{k=0}^{H-1}\binom{-h-1}{k},
$$


which agree modulo $2$ and cancel. The remaining finite binomial sum gives (22).

### 4.4 Applying the actual weights

From (4),


$$
X_j=\frac{W_j}{2}
\left(j\theta^P_{j-1}-\theta^P_j\right).
\tag{23}
$$



- For odd $j$, $4\mid W_j$, so $X_j\equiv0\pmod2$.
- For $j=4q+2$,
  

$$
W_j/2\equiv\binom{L-1}{q}\pmod2.
$$


  If this is nonzero, $q$ is even. But then $M-1-q$ is odd, and
  

$$
\binom{h+M-1-q}{M-1-q}=0\pmod2.
$$


  Hence these coordinates also vanish.
- For $j=4q$, formula (22) gives
  

$$
X_{4q}\equiv
  \binom Lq(1+q)
  \binom{h+M-q}{M-q}\pmod2.
  \tag{24}
$$



Only even $q=2k$ remain. Lucas reduction in (24) gives


$$
X_{8k}\equiv
\binom Ak\binom{2A+d-k}{d-k}\pmod2.
$$


This proves (2), including all $0\le j\le b$.

---

## 5. The evaluated norm and its all-depth binary carry rule

Because squaring is the identity modulo $2$, (2) gives


$$
X^TX\equiv
\sum_{k=0}^d
\binom Ak\binom{2A+d-k}{d-k}\pmod2.
$$


This is the coefficient of $z^d$ in


$$
(1+z)^A(1-z)^{-2A-1}.
$$


Over $\mathbb F_2$, it equals


$$
(1+z)^{-A-1}.
$$


Therefore


$$
X^TX\equiv\binom{A+d}{d}\pmod2,
$$


proving (1).

Lucas–Kummer now proves (3). This criterion can be evaluated by a finite binary carry transfer whose state bound is independent of $r$.

Write


$$
d=\sum_{i\ge0}\delta_i2^i,\qquad \delta_i\in\{0,1\}.
$$


Initialize $c_0=500$, and use


$$
a_i\equiv4002\delta_i+c_i\pmod2,
\qquad
c_{i+1}=\left\lfloor\frac{4002\delta_i+c_i}{2}\right\rfloor.
\tag{25}
$$


Then $(a_i)$ are exactly the binary digits of $A=4002d+500$. The state remains in


$$
0\le c_i\le4002.
$$


The norm is a unit exactly when no transition has


$$
\delta_i=a_i=1.
\tag{26}
$$



This is an all-depth rule for the actual evaluated norm digit. No bounded set of low digits is asserted to decide it in general.

### An infinite obstruction

For $r\equiv2\pmod{16}$,


$$
d=\frac{9^r-1}{8}
\equiv r+8\binom r2\equiv10\pmod{16}.
$$


Hence


$$
A=4002d+500\equiv2d+4\equiv8\pmod{16}.
$$


The binary digit $2^3$ is present in both $d$ and $A$. Thus


$$
\boxed{X^TX\equiv0\pmod2\qquad(r\equiv2\pmod{16}).}
\tag{27}
$$



This disproves the proposed unit assertion on that infinite subclass. It does not establish the size of the mixed contraction there.

---

## 6. A new symbolic prediction at the first obstructed index

This is a deduction from (2), not an executed numerical control.

Take


$$
r=2,\qquad a=4,\qquad b=81,\qquad n=324162.
$$


Then


$$
d=10,\qquad A=40520.
$$


For $0\le k\le10$, the condition $\binom Ak$ odd restricts $k$ to $0,8$. The second factor in (2) is odd at both values. Therefore


$$
\boxed{X\equiv e_0+e_{64}\pmod2.}
\tag{28}
$$


In particular, $X$ has unit common content, but its norm is not a unit.

Moreover, an odd square is $1\pmod4$ and an even square is $0\pmod4$. Thus (28) proves the exact valuation


$$
\boxed{X^TX\equiv2\pmod4,\qquad v_2(X^TX)=1.}
\tag{29}
$$



This is a concrete instance where primitive column content and evaluated norm depth differ.

---

## 7. Complete mixed contraction: exact corrections through modulus $16$

The mixed contraction is not determined by the norm calculation. The following reduction keeps the information required to calculate its first two digits without a growing matrix inversion.

### 7.1 Complete divided residual modulo $16$

Since $b\equiv1\pmod8$,


$$
v_2\!\left(\frac{(b+5)!}{b!}\right)\ge4.
$$


Consequently, the exponential factorial tail after division by $b!$ needs only


$$
t=b,b+1,b+2,b+3,b+4
$$


modulo $16$.

Put


$$
\alpha_j=\frac{(b+j)!}{b!},\qquad 0\le j\le4.
$$


Their residues are


$$
(\alpha_0,\ldots,\alpha_4)
\equiv
(1,\ 2+8d,\ 6+8d,\ 8,\ 8)\pmod{16}.
\tag{30}
$$


Combining this with (6), the complete divided residual satisfies


$$
\boxed{
\frac{\rho_i}{b!}\equiv
\sum_{s=0}^4 d_s\binom{n+i}{s}
\sum_{j=0}^4
\alpha_j\binom{2n+i-s}{b+j}
\pmod{16},
}
\tag{31}
$$


where the $d_s$ in this formula may be taken as the integers


$$
1,-2,4,-6,6.
$$



The complete logarithmic forcing is legitimately zero at this precision. The supplied whole-forcing bound gives


$$
v_2(h_i^F/b!)
\ge
\frac n2+1
-2\lfloor\log_2(2n+b-1)\rfloor-v_2(b!).
$$


Since $n=4002b$ and $b\ge9$, this is strictly greater than $4$. For example, using
$\log_2(8005b)<13+b$ and $v_2(b!)<b$ gives the lower bound


$$
1998b-25>4.
$$


Thus (31) is a reduction of the **whole** residual, not an exponential-only definition.

### 7.2 Exact inverse carry

Define the finite matrix


$$
E=P^{-1}CT(-n),
\tag{32}
$$


with $C$ as in (8). From


$$
\widetilde N\equiv
\bigl(P+2CT(-n)\bigr)T(n)\pmod{16},
$$


we obtain


$$
\boxed{
T(-n)\widetilde N^{-1}
\equiv
T(-2n)(I-2E+4E^2-8E^3)P^{-1}
\pmod{16}.
}
\tag{33}
$$


The cubic term $-8E^3$ is retained. The next term vanishes modulo $16$.

Let $r^{(16)}$ denote the right side of (31). Then


$$
\boxed{
\eta\equiv
T(-2n)(I-2E+4E^2-8E^3)P^{-1}r^{(16)}
\pmod{16}.
}
\tag{34}
$$


All matrices in (32)–(34) have precisely the original dimension $b$. In particular, no terms beyond the upper boundary are inserted into a convolution.

For the $P$-column, let


$$
f^{(8)}=(2,1,3,1,4,4,0,\ldots,0)^T.
$$


Then


$$
\boxed{
\theta^P\equiv
T(-2n)(I-2E+4E^2)P^{-1}f^{(8)}
\pmod8.
}
\tag{35}
$$



### 7.3 Exact evaluated contractions modulo $4$

Equations (34)–(35), followed by the actual weighted reconstruction, give


$$
\boxed{
X_j\equiv
\frac{W_j(j\theta^P_{j-1}-\theta^P_j)}2\pmod4,
}
\tag{36}
$$


and


$$
\boxed{
Y_j\equiv
\frac{
W_b\delta_{j,b}
+W_j(j\eta_{j-1}-\eta_j)
}{4}\pmod4.
}
\tag{37}
$$


The divisions are exact local divisions justified by the established whole-column normalizations. The endpoint $W_be_b$ is explicitly present in (37).

Therefore


$$
X^TX,\qquad X^TY\pmod4
$$


are determined by the finite formulas (30)–(37), including the complete inverse carry. This is a new bounded reduction, not a claim that the resulting growing sums are units.

At the first binary layer, (2) also gives the shorter exact expression


$$
\boxed{
X^TY\equiv
\sum_{\substack{0\le k\le d\\
\binom Ak\binom{2A+d-k}{d-k}\ \mathrm{odd}}}
\frac{\eta_{8k}}4
\pmod2.
}
\tag{38}
$$


For every included index, $W_{8k}$ is odd, so the required division of $\eta_{8k}$ by $4$ is valid. The endpoint has zero $X$-residue, but its inclusion in the full column formula remains necessary.

At $(n,b)=(324162,81)$, formula (38) becomes


$$
\boxed{
X^TY\equiv\frac{\eta_0+\eta_{64}}4\pmod2.
}
\tag{39}
$$


I have not evaluated that remaining residue here. In particular, I do not claim that the norm obstruction is accompanied by either a unit mixed contraction or an additional mixed cancellation.

---

## 8. Actual final gcd and reduced denominator

Let


$$
\alpha=v_2(X^TX),\qquad
\gamma=v_2(X^TY).
$$


The norm is positive. The complete mixed contraction is nonzero throughout this domain by the retained coefficient-$4002$ theorem at $3$, so both valuations are finite.

The exact center is


$$
c_n=\frac{2b!}{\lambda R}\,
\frac{X^TY}{X^TX},
\qquad
\lambda=\frac{(n!)^2}{2^n}.
\tag{40}
$$



Retain the least actual $B$-lift denominator $d_B$, the integer Gram contractions $A_B,H_B$, and


$$
g_B=\gcd(A_B,|H_B|),\qquad
p_n=H_B/g_B,\qquad q_n=A_B/g_B.
\tag{41}
$$


Using the established $v_2(d_B)=0$, put


$$
s=s_2(n),\qquad F_b=v_2(b!).
$$


Then


$$
v_2(A_B)=3n-2s+2+\alpha,
\tag{42}
$$




$$
v_2(H_B)=\frac{3n}{2}-s+F_b+3+\gamma.
\tag{43}
$$


Hence the **evaluated final gcd** is


$$
\boxed{
v_2(g_B)=
\min\left\{
3n-2s+2+\alpha,\
\frac{3n}{2}-s+F_b+3+\gamma
\right\},
}
\tag{44}
$$


and the **actual primitive denominator** satisfies


$$
\boxed{
v_2(q_n)=
\max\left\{
0,\
\frac{3n}{2}-F_b-s-1+\alpha-\gamma
\right\}.
}
\tag{45}
$$



No difference of lower bounds has been used.

At the new symbolic index $(n,b)=(324162,81)$,


$$
s_2(n)=8,\qquad F_b=78,\qquad \alpha=1.
$$


Thus


$$
\boxed{
v_2(q_n)=\max(0,486157-\gamma),
}
\tag{46}
$$


and


$$
\boxed{
v_2(g_B)=\min(972473,486316+\gamma).
}
\tag{47}
$$


The actual value of $\gamma$ has not been established here.

At these same centers, the retained $3$-adic law remains


$$
v_3(q_n)=n-\frac{b+15}{2}.
\tag{48}
$$


But (45) does not yet provide the infinite lower rate needed to combine with (48).

---

## 9. Whole evaluated error and scope

At the stated dependency status of the supplied proportional signed-rate theorem, eventually


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi)<0,
\qquad
\log|\epsilon_n|=-\tau_c n+o(n),
$$


where


$$
\tau_c=\left(2+\frac1{4002}\right)\log(1+\sqrt2).
$$


The actual complete primitive error is therefore


$$
\boxed{
L_n=q_n(e+\pi)-p_n=-q_n\epsilon_n>0
}
$$


eventually, and


$$
\log|L_n|=\log q_n-\tau_c n+o(n).
$$



The arithmetic theorem required for the proposed aggregate transfer has not passed. Accordingly, I do not assert the aggregate exclusion or carry out that conditional transfer as though its hypothesis were proved.

The new infinite norm obstruction excludes an **arithmetic unit conjecture**, not the proportional center construction, not all even exponents, and not rationality or irrationality of $e+\pi$.

---

# Concluding ledger

## (1) New result and proof status

**Proved from the exact coefficient and reconstruction formulas:**

1. On every even exponent $a=2r\ge2$,
   

$$
X_{8k}\equiv
   \binom{4002d+500}{k}
   \binom{8004d+1000+d-k}{d-k}\pmod2,
   \qquad d=(9^r-1)/8,
$$


   with all other coordinates zero modulo $2$.

2. The complete evaluated norm has the exact first digit
   

$$
\boxed{
   X^TX\equiv\binom{4003d+500}{d}\pmod2.
   }
$$



3. An all-depth, bounded-state binary carry rule decides that norm digit.

4. The norm is nonunit on the infinite class
   

$$
\boxed{a\equiv4\pmod{32}.}
$$


   Thus a norm-and-mixed unit theorem on **all** even exponents is false.

5. At $(n,b)=(324162,81)$, the symbolic formulas prove
   

$$
\boxed{
   X\equiv e_0+e_{64}\pmod2,\qquad v_2(X^TX)=1.
   }
$$


   This prediction has not been independently executed here.

6. Equations (30)–(37) give exact finite reductions of both normalized columns and both evaluated contractions modulo $4$, retaining the complete forcing, endpoint, growing boundaries, and inverse corrections through modulus $16$.

**Not proved:** a uniform unit theorem for the complete mixed contraction, a sufficient relative-depth estimate, or a same-center two-prime exclusion.

## (2) Exact remaining bottleneck

The remaining arithmetic quantity is still


$$
\boxed{
\gamma-\alpha
=
v_2(X^TY)-v_2(X^TX).
}
$$



The norm part now has an exact first-digit carry law, and its universal unit assertion is disproved. What is still needed is either:

- a complete mixed-contraction theorem on a specified infinite even-exponent subclass; or
- a quantitative upper bound for $\gamma-\alpha$ sufficient for (45).

The finite formulas (30)–(38) expose the next obstruction explicitly. Their binomial coefficients retain higher binary digits, and the sum in (38) generally runs over a growing, digit-selected set of coordinates. No support argument supplies its nonzero amplitude.

## (3) Bounded exact computation request

**REQUEST: pro / max / high — one falsification audit of the derived carry rule, not another pattern scan.**

**Input**


$$
a=4,\qquad n=324162,\qquad b=81,\qquad m_w=1.
$$



**Required predicted outputs**


$$
\boxed{
f^0/R\equiv(2,1,3,1,4,4,0,\ldots,0)\pmod8,
}
$$




$$
\boxed{
Z_w/R\equiv2e_0+2e_{64}\pmod4,
}
$$


and consequently


$$
\boxed{
X^TX\equiv2\pmod4,\qquad v_2(X^TX)=1.
}
$$



These outputs directly test the new all-depth norm formula at its first predicted failure. The purpose is to falsify or corroborate the symbolic carry derivation, not to infer an infinite law from another regular index.

If the complete $Q$-column is included in the same bounded audit, compare its direct residue with (30)–(37) and certify


$$
X^TY\equiv(\eta_0+\eta_{64})/4\pmod2.
$$


No numerical nonzero prediction for that mixed residue is made here. Its computation would resolve this specific newly exposed carry, not the infinite relative-depth bottleneck.
