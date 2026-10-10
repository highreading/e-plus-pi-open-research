> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2: audited even binary theorem, and a first lift on the odd $29$-adic column-zero class

No rationality or irrationality decision for $e+\pi$ follows.

There are three new conclusions.

1. **A5 turn 7’s even binary column formula, boundary cancellation, norm identity, and finite-precision divisions pass the audit.** Its binary transfer decides the first norm digit using arbitrarily many index digits. It is **not** an all-depth valuation theorem.

2. On the original odd family
   

$$
n=2001\,3^a,\qquad b=3^a,\qquad a\equiv31\pmod{812},
$$


   the next $P$-column digit has a particularly simple formula. Write
   

$$
p=29,\quad n=pN,\quad b=pB+27,\quad
   J=\operatorname{CT}(t^{-1}+2+2t)^n.
$$


   Every product
   

$$
\binom Nq\binom{2N+B-q}{B-q},\qquad 0\le q\le B,
$$


   is divisible by $p$. Define the **exact integer**
   

$$
T_q=\frac1p\binom Nq\binom{2N+B-q}{B-q}.
   \tag{A}
$$


   Then the actual first normalized column digit is
   

$$
\boxed{
   \left(\frac{Z_{w,pq}}p,\frac{Z_{w,pq+1}}p,
                 \frac{Z_{w,pq+2}}p\right)
   \equiv
   J(-1)^qT_q(-1,2,-1)\pmod p,
   }
   \tag{B}
$$


   and every other coordinate, including $j=b$, vanishes modulo $p$.
   The actual contact correction is included in the proof below; it cancels in this weighted first lift.

3. **The content is not uniformly exactly one.** The first-lift Boolean rule below proves
   

$$
\boxed{
   Z_w\in29^2\mathbb Z_{29}^{b+1}
   \quad\text{if}\quad
   a\equiv432827\pmod{682892}.
   }
   \tag{C}
$$


   This is an infinite subclass of $a\equiv31\pmod{812}$, obtained without any distribution hypothesis for the digits of $3^a$.

On the entire class $a\equiv31\pmod{812}$, I also prove the stronger complete-$Q$ divisibility


$$
\boxed{\frac{V_w}{b!}\in29^2\mathbb Z_{29}^{b+1}.}
\tag{D}
$$


I give an explicit complete-residual and actual-inverse formula modulo $29^3$, which determines the next normalized $Q$-digit and the two evaluated normalized contractions. I do **not** prove that their relative valuation is uniform.

---

## 1. Independent audit of A5 turn 7

This section concerns only the different, even family


$$
a=2r,\quad b=9^r,\quad n=4002b,\quad r\ge1.
$$


Retain


$$
h=n/2,\quad R=2^h\binom{2h}{h},\quad
X=\frac{Z_w}{2R},\quad Y=\frac{V_w}{4b!},
$$


and


$$
d=\frac{b-1}{8},\qquad A=\frac{h-1}{4}=4002d+500.
$$



### 1.1 Divided coefficients and forcing cutoff

Here $h\equiv1\pmod8$. In the integral divided-power ring, write


$$
\phi^2=1+2U.
$$


For $k=2,3$, respectively,


$$
v_2\!\left(4\binom hk\right)\ge4,\qquad
v_2\!\left(8\binom h3\right)\ge4;
$$


the terms $k\ge4$ already have their required factor $16$. Thus the displayed reduction


$$
(d_0,\ldots,d_4)\equiv(1,-2,4,-6,6)\pmod{16},
\qquad d_s\equiv0\pmod{16}\quad(s>4)
$$


is valid in the required coefficient ring.

The forcing cutoff also passes. In the two normalized coefficient sums, the factor $(h)_j$, or $(h)_{j+1}$, supplies $8$ once $l\ge3$. The residual summand has valuation at least $v_2(r!)$, so the claimed vanishing is not obtained by dropping denominators informally. The three surviving coefficient values are


$$
B_0\equiv2,\quad B_1\equiv3,\quad B_2\equiv3\pmod8.
$$


Multiplication by the remaining consecutive products gives


$$
f^0/R\equiv(2,1,3,1,4,4,0,\ldots)\pmod8.
$$



### 1.2 The inverse-contact boundary cancellation is correct

Modulo $4$, let $g=P^{-1}(f^0/R)$. Then


$$
g_i=(-1)^i\left(2-i+3\binom i2-\binom i3\right)\pmod4,
$$


and hence


$$
g_{4q}/2\equiv1+q\pmod2.
$$



Put $M=(b-1)/4$ and $L=(h+1)/2$. In the base solution $y^0=T(-n)g$, the finite boundary gives


$$
y^0_{4q}=y^0_{4q+2}
=\binom{L+M-q-1}{M-q-1}\pmod2
\quad(q<M),
$$


but


$$
y^0_{4M}=0.
$$


The last equality is indispensable.

For the contact correction at a row divisible by four, the $s=1,3$ terms vanish by the low binary digit. In the $s=4$ term, pair the columns $4q$ and $4q+2$. Their $y^0$-entries and their $\binom{j+4}{4}$-entries agree. The remaining pair is


$$
\binom{2h}{4u}+\binom{2h}{4u+2}
\equiv
\binom h{2u}+\binom h{2u+1}=0\pmod2.
$$


This includes lower-index boundary cases under the usual zero convention. The sole unpaired terminal column contributes zero because $y^0_{4M}=0$.

Therefore the inverse-contact correction really vanishes in the asserted rows. This is a cancellation for the actual finite solution, not an assertion that the correction matrix vanishes on arbitrary inputs.

### 1.3 Reconstruction, endpoint, and norm

The identity


$$
(1+z)^{-4h}
\equiv
(1+z^4)^{-h}
-2hz^2(1+z^4)^{-h-1}\pmod4
$$


is correct. The two finite sums involving the index $k$ cancel after division by two. This gives


$$
\theta^P_{4q}/2
\equiv
(1+q)\binom{h+M-q}{M-q}\pmod2.
$$



The weight analysis then passes:

- odd $j$, including the endpoint $j=b$, have $4\mid W_j$;
- at $j=4q+2$, a nonzero $W_j/2$ requires even $q$, and the remaining binomial vanishes;
- at $j=4q$, only even $q=2k$ survives.

Consequently,


$$
\boxed{
X_{8k}\equiv
\binom Ak\binom{2A+d-k}{d-k}\pmod2,
\quad 0\le k\le d,
}
$$


with zero at every other coordinate.

Squaring is the identity modulo two, so the **evaluated** norm is the coefficient of $z^d$ in


$$
(1+z)^A(1-z)^{-2A-1}
=(1+z)^{-A-1}\quad\text{over }\mathbb F_2.
$$


Thus


$$
\boxed{X^TX\equiv\binom{A+d}{d}\pmod2.}
$$



This proves precisely the stated unit criterion


$$
X^TX\in\mathbb Z_2^\times\iff d\mathbin{\&}A=0.
$$



### 1.4 What the binary transfer does—and does not—prove

The transfer


$$
a_i\equiv4002\delta_i+c_i\pmod2,\qquad
c_{i+1}=\left\lfloor\frac{4002\delta_i+c_i}{2}\right\rfloor,
\quad c_0=500,
$$


correctly computes all binary digits of $A$, with $0\le c_i\le4002$.

It is an **all-index-digit rule for one evaluated norm digit**. In particular, it does not prove


$$
v_2(X^TX)=v_2\binom{A+d}{d}
$$


when that first digit is zero.

The infinite obstruction $r\equiv2\pmod{16}$ passes: $d\equiv10$ and $A\equiv8\pmod{16}$ share the $2^3$-digit. At $r=2$, the two surviving coordinates are exactly $0,64$, so the stronger finite conclusion


$$
X^TX\equiv2\pmod4
$$


is justified by the two odd squares.

Finally, the finite-precision inverse


$$
T(-2n)(I-2E+4E^2-8E^3)P^{-1}\pmod{16}
$$


has the correct matrix order. Computing the $P$-numerator modulo $8$ before dividing by $2$, and the complete $Q$-numerator modulo $16$ before dividing by $4$, supplies both normalized columns modulo $4$. The endpoint is present in the latter numerator. Those exact divisions pass.

**Audit status:** the new even theorem passes. No even all-depth relative-valuation theorem follows from it.

---

## 2. Original odd class and notation for its first lift

Return exclusively to


$$
n=2001\,3^a,\quad b=3^a,\quad a\ge1,\quad m_w=1,
$$


and now impose


$$
a\equiv31\pmod{812}.
\tag{2.1}
$$


Set


$$
p=29,\quad n=pN,\quad b=pB+27.
$$


The fixed low digits are


$$
\boxed{
B\equiv28\pmod p,\qquad
N\equiv7\pmod p.
}
\tag{2.2}
$$



Write


$$
W_j=\binom{n+2}{j},
$$


and, for a length-$b$ vector $\theta$, use


$$
(\mathcal Z\theta)_j=j\theta_{j-1}-\theta_j,
\quad
\theta_{-1}=\theta_b=0.
$$


The actual columns are


$$
Z_w=\operatorname{diag}(W_j)\mathcal Z
       T(-n)\widetilde N^{-1}f^0,
\tag{2.3}
$$




$$
Y:=\frac{V_w}{b!}
=W_be_b+\operatorname{diag}(W_j)\mathcal Z
       T(-n)\widetilde N^{-1}(\rho/b!).
\tag{2.4}
$$



The supplied constant-term recurrence and reflection show that


$$
J=\operatorname{CT}(t^{-1}+2+2t)^n
$$


is a $29$-adic unit. No hypothesis on the digits of $3^a$ is needed for that particular fact.

For $0\le q\le B$, let


$$
H=B-q,\qquad A_H=\binom{2N+H}{H}.
$$


The low-digit obstruction implies


$$
p\mid \binom Nq A_H.
\tag{2.5}
$$


Indeed, if $q_0=q\bmod p\le7$, then $H_0=28-q_0\ge21$, so $A_H\equiv0\pmod p$. If $q_0>7$, then $\binom Nq\equiv0\pmod p$.

Thus the divisions defining $T_q$ in (A) are exact integer divisions.

---

## 3. Actual contact inversion in the $P$-column lift

The main point here is to show why the first lift is not altered by the contact correction.

### 3.1 The normalized forcing correction has support below $2p$

For $i<p$, Frobenius gives $f_i^0\equiv Ji!\pmod p$. For $i\ge p$, both sides are divisible by $p$. Hence


$$
f^0/J=(i!)_{i<b}+pF\pmod{p^2}
\tag{3.1}
$$


for an integral $p$-adic vector $F$.

For $i\ge2p$, the consecutive product


$$
\frac{(n+i)!}{n!}
$$


contains at least two multiples of $p$; the Laurent coefficients entering $J_i$ are integers. Therefore


$$
F_i=0\pmod p\qquad(i\ge2p).
\tag{3.2}
$$



Let


$$
g=P^{-1}(i!)_{i<b};
$$


then $g_i={!i}$, the derangement number.

### 3.2 Explicit first inverse correction

Write


$$
P^{-1}\widetilde N=T(n)+pE\pmod{p^2}.
$$


For $k=pq+u$, the actual correction is


$$
\begin{aligned}
E_{kj}={}&
N\sum_{s=1}^{p-1}\ell_s(k)_s\binom n{j-k+s}\\
&+Nq\binom n{j-k+p}
+N^2\binom{n-p}{j-k}\pmod p,
\end{aligned}
\tag{3.3}
$$


where


$$
\ell_s=[z^s]\log(1-z+z^2/2)\pmod p.
$$


This follows from the Newton transform of the defining contact coefficients; the $s=p$ terms supply the last two summands. Terms $s>p$ vanish modulo $p^2$.

Thus the actual divided $P$-solution satisfies


$$
\frac{\theta^P}{J}
=
T(-2n)g
+pT(-2n)\bigl(P^{-1}F-E\,T(-n)g\bigr)
\pmod{p^2}.
\tag{3.4}
$$



### 3.3 Evaluation of the correction in the relevant rows

For $u=0,1,2$, the support bound (3.2) and Lucas give


$$
(P^{-1}F)_{pq+u}=(-1)^q(\alpha_u+\beta_u q)
\tag{3.5}
$$


for explicitly finite low-digit constants $\alpha_u,\beta_u$. Their individual values are immaterial here because the weighted operator annihilates this entire two-dimensional row form.

To verify the contact part just as explicitly, put $y=T(-n)g$. In these rows,


$$
y_{pq+u}
=(-1)^q {!u}\binom{N+H}{H}\pmod p.
$$


Using $T(N)T(-N)=I$ in the finite block range, (3.3) gives


$$
\boxed{
(Ey)_{pq+u}
=(-1)^q
\left[
-Nu\,!(u-1)-Nq\,!u+N^2(H+1)\,!u
\right]\pmod p,
}
\tag{3.6}
$$


with $u\,!(u-1)=0$ at $u=0$. Here $\ell_1=-1,\ell_2=0$. The term involving $q-1$ is absent at $q=0$, exactly as its factor $q$ requires.

Consequently the bracket in (3.4), in these rows, is again


$$
(-1)^q(\alpha'_u+\beta'_u q).
$$


Applying $T(-2n)$ reduces it to a linear combination of


$$
(-1)^qA_H,\qquad
(-1)^q\binom{2N+H}{H-1}.
\tag{3.7}
$$


For example, the weighted-index sum is evaluated by


$$
\sum_{h=0}^{H}h\binom{2N+h-1}{h}
=2N\binom{2N+H}{H-1}.
$$



If $W_{pq+u}$ is a unit, then $q_0\le7$, so $H_0\ge21$. Both binomials in (3.7) vanish modulo $p$. If $W_{pq+u}$ is not a unit, the explicit prefactor $p$ in (3.4) already makes its weighted contribution zero modulo $p^2$.

At low digit zero, the predecessor term in $\mathcal Z$ has the extra factor $pq$, so the first inverse correction cannot contribute there either.

Therefore the actual contact and forcing corrections make **zero contribution to the first normalized weighted $P$-digit**.

---

## 4. Evaluation of the base solution and proof of the next column digit

It remains to lift


$$
\theta^0=T(-2n)g.
$$



### 4.1 A finite-boundary formula

For arbitrary forcing $f_l$, finite binomial summation gives, with $L=b-1-j$,


$$
\begin{aligned}
(T(-2n)P^{-1}f)_j
={}&\sum_{l=0}^{b-1}(-1)^{j+l}f_l
\sum_{t=0}^{\min(l,L)}
\binom j{l-t}\binom{2n+t-1}{t}
\binom{2n+L}{L-t}.
\end{aligned}
\tag{4.1}
$$


This follows from


$$
\sum_{k=0}^{M}(-1)^k\binom Uk=(-1)^M\binom{U-1}{M},
$$


after expanding $\binom{j+k}{l}$. No terms beyond $b-1$ are introduced.

Apply (4.1) with $f_l=l!$. Modulo $p^2$, only $l<2p$ is required.

Suppose $j=pq+u$, $u=0,1,2$, and $\binom Nq$ is a unit. Then


$$
L=pH+26-u,\qquad H_0\ge21.
$$


In (4.1):

- for $l<p$, every $t\ge1$ has an explicit factor $p$; its other binomial vanishes modulo $p$;
- for $p\le l<2p$, the factor $l!$ supplies $p$. Only $t=0,p$ could survive, and their higher binomials again vanish modulo $p$.

The surviving term is therefore


$$
\frac{\theta^0_{pq+u}}p
\equiv
(-1)^q {!u}\frac{A_H}{p}\pmod p.
\tag{4.2}
$$



The replacement of


$$
\binom{p(2N+H)+26-u}{pH+26-u}
$$


by $A_H$ after division by $p$ is legitimate. The equal-low-digit factorial ratio is $1\pmod p$, while


$$
\binom{pU}{pV}\equiv\binom UV\pmod{p^2}.
$$


For completeness, the latter follows by expanding


$$
(1+z)^{pU}
=\bigl(1+z^p+pA(z)\bigr)^U\pmod{p^2},
$$


where $A$ has no exponents divisible by $p$; the term linear in $pA$ cannot contribute to $z^{pV}$.

If instead $\binom Nq$ is divisible by $p$, only the already known leading digit of $\theta^0$ is needed. These two cases combine without division by a possibly nonunit binomial.

### 4.2 Weights outside the three supported residues

For $3\le s<p$,


$$
\frac1p\binom{pN+2}{pq+s}
\equiv
\frac{2N(-1)^{s-3}}{s(s-1)(s-2)}
\binom{N-1}{q}\pmod p.
\tag{4.3}
$$


If the last binomial is nonzero, then $q_0\le6$. The relevant leading $P$-solution terms involve $A_H$, or the adjacent boundary value with $H-1$, and both vanish because their low lower digit is at least $21$.

At $j=b$, (4.3) has $q=B$, whose low digit is $28$. Therefore $W_b/p\equiv0\pmod p$, so the terminal $P$-coordinate also vanishes after division by $p$.

Combining (3.4)–(4.3) with the actual multiplication gives exactly


$$
\boxed{
\left(\frac{Z_{w,pq}}p,\frac{Z_{w,pq+1}}p,
                 \frac{Z_{w,pq+2}}p\right)
\equiv J(-1)^qT_q(-1,2,-1)\pmod p,
}
$$


with all other coordinates zero.

In particular,


$$
\boxed{
\frac{\mathfrak D}{p^2}
\equiv6J^2\sum_{q=0}^{B}T_q^2\pmod p.
}
\tag{4.4}
$$


This is a lifted **actual-column** formula, not a lift inferred from the scalar norm alone.

---

## 5. Exact first-lift content rule and failure of uniform content one

Let


$$
\kappa=\min_jv_p(Z_{w,j}).
$$


Since $J$ and the coordinates of $(-1,2,-1)$ are units,


$$
\boxed{
\kappa=1
\iff
\exists q\in[0,B]:
v_p\!\left(\binom NqA_{B-q}\right)=1.
}
\tag{5.1}
$$



This criterion has a small changing-boundary Boolean reduction.

Write


$$
B=28+pC,\qquad C=c+pD,\quad0\le c<p.
$$


The constraint $N=69b$ gives


$$
N=7+pN_1,\qquad
N_1=24+pN_2,\qquad
\boxed{N_2=68+69C.}
\tag{5.2}
$$



Define $\mathcal H_{d,e}(M,D)$ to mean that some $x,y\ge0$ satisfy


$$
x+y=D-e,\qquad
\binom Mx\binom{-2M-d}{y}\not\equiv0\pmod p.
$$


These are the Boolean states from the earlier four-state recursion.

### 5.1 First borrow and changing upper indices

Put $h=B-q$. At the first digit, $q_0+h_0=28$; an outgoing addition carry would require $57$, which exceeds $2p-2=56$.

Exactly one initial binomial borrow can occur in two ways:

- $q_0=14,\ldots,28$: the $N$-binomial borrows, and the remaining upper pair is
  

$$
(N_1-1,\,-2N_1-1);
$$


- $q_0=0,\ldots,7$: the negative-upper binomial borrows, and the remaining upper pair is
  

$$
(N_1,\,-2N_1-2).
$$



The first-borrow multipliers are units: $N_1\equiv24$ and
$-2N_1-1\equiv9\pmod p$. Thus no extra zero is hidden in this reduction.

At the second digit the upper pairs are respectively


$$
(23,9),\qquad(24,8).
$$


Both have total degree $32$. After that digit, both become the same higher pair


$$
(N_2,-2N_2-2).
$$


There is always a no-carry option. A carry option exists exactly when $c\le3$.

Therefore


$$
\boxed{
\kappa=1
\iff
\mathcal H_{2,0}(N_2,D)
\ \vee\
\bigl(c\le3\ \wedge\ \mathcal H_{2,1}(N_2,D)\bigr).
}
\tag{5.3}
$$



For clarity, this Boolean rule is fully explicit. If


$$
M=m_0+pM',\qquad D=d_0+pD',
$$


put


$$
d'=\left\lceil\frac{2m_0+d}{p}\right\rceil,\qquad
v_0=pd'-2m_0-d.
$$


Then


$$
\mathcal H_{d,e}(M,D)=
\bigvee_{k=0}^{1}
\left[
0\le d_0-e+pk\le m_0+v_0
\ \wedge\
\mathcal H_{d',k}(M',D')
\right],
\tag{5.4}
$$


with terminal vector $(\mathrm{true},\mathrm{false},\mathrm{true},\mathrm{false})$.

Equations (5.3)–(5.4) decide whether the actual content is exactly one. They do not purport to give its valuation when this digit also vanishes.

### 5.2 An infinite second-content obstruction

Choose the four low base-$29$ digits of $b$ to be


$$
\boxed{b\equiv(27,28,5,28)_{29}\pmod{29^4}.}
\tag{5.5}
$$


Then $c=5>3$, so only $\mathcal H_{2,0}$ remains in (5.3). Moreover,


$$
N_2\equiv68+69\cdot5\equiv7\pmod{29},
\qquad D\equiv28\pmod{29}.
$$


In state $d=2$, the other upper digit is


$$
29-2\cdot7-2=13.
$$


Its maximum possible digit sum is $7+13=20<28$. Both outgoing Boolean branches are therefore absent, regardless of every higher digit.

Hence (5.5) implies $\kappa\ge2$.

This digit condition is attained on an explicit infinite exponent class. A checkable modular calculation is


$$
3^{28}\equiv1+15p+13p^2+28p^3\pmod{p^4}.
$$


For


$$
t=1+11p+18p^2=15458
$$


one obtains


$$
27(3^{28})^t
\equiv27+28p+5p^2+28p^3\pmod{p^4}.
$$


Thus


$$
a=3+28t=432827,
$$


and the period used here is $28p^3=682892$. Consequently


$$
\boxed{
a\equiv432827\pmod{682892}
\Longrightarrow
Z_w\in29^2\mathbb Z_{29}^{b+1}.
}
$$


Also $432827\equiv31\pmod{812}$, as required.

This disproves uniform content one on the proposed first candidate class.

---

## 6. The complete $Q$-column also gains a second factor

Continue on the entire class $a\equiv31\pmod{812}$.

Let


$$
t=T(-n)\widetilde N^{-1}(\rho/b!).
$$


The complete logarithmic forcing is zero modulo $p^2$ by


$$
v_p(h_i^F/b!)
\ge F_n-F_b-\lfloor\log_p(2n+b-1)\rfloor>2.
$$



For $s=0,1,2$, the actual projected inverse and the two factorial blocks give


$$
\frac{t_{pq+s}}p
\equiv
-\frac{K_H}{27!}L_{27,s}
+\frac{(B+1)s!}{27!}\binom{-2N}{H+1}\pmod p,
\tag{6.1}
$$


where


$$
K_H=-2N(-1)^HA_H.
$$


The inverse-contact and nonconstant-residual corrections vanish in these rows by their low-digit support, rather than by omission.

Now $B+1\equiv0\pmod p$. At a unit-weight coordinate, $q_0\le7$, so $A_H=0\pmod p$. Thus every term of (6.1) vanishes there.

The low-digit-zero predecessor contributes


$$
q\,\binom{-2N}{H+1}/27!.
$$


If $q_0=0$, its prefactor vanishes. For $1\le q_0\le7$, the lower digit of $H+1$ is $29-q_0\ge22$, while $-2N\bmod29=15$; the binomial vanishes.

Outside low digits $0,1,2$, the only potentially nonzero leading residual boundary is at low digit $27$. Its first weight digit contains $\binom{N-1}{q}$, which forces $q_0\le6$, while its residual binomial has lower digit at least $22>15$. It therefore vanishes too. The endpoint has $W_b/p=0\pmod p$.

Hence


$$
\boxed{Y=V_w/b!\in p^2\mathbb Z_p^{b+1}.}
\tag{6.2}
$$


In particular,


$$
v_p(\mathfrak D)\ge2,\qquad v_p(\Xi)\ge3,
\quad \Xi=Z_w^TY,
\tag{6.3}
$$


on the whole candidate class. On the further class (C),


$$
v_p(\mathfrak D)\ge4,\qquad v_p(\Xi)\ge4.
$$


The latter two lower bounds must not be subtracted to obtain a relative valuation.

---

## 7. Explicit complete carry through $p^3$

The remaining normalized $Q$-digit can be determined without an unspecified inverse or Schur complement.

Put


$$
d_s=s![z^s]\phi(z)^n,\qquad \phi(z)=1-z+z^2/2.
$$


The integral strengthening gives


$$
v_p(d_s)\ge1+v_p((s-1)!)\quad(s\ge1).
$$


Thus only $s\le2p=58$ is needed modulo $p^3$.

### 7.1 The changing factorial boundary

Since


$$
b+2=p^2(C+1),
$$


the first new factorial block has valuation at least two, not one. For $2\le d\le30$,


$$
\frac{(b+d)!}{p^2b!}
\equiv-(C+1)(d-2)!\pmod p.
$$


The next multiple of $p$ occurs at $d=31$, so all later tails vanish modulo $p^3$.

Therefore the **complete** residual modulo $p^3$ is


$$
\boxed{
\begin{aligned}
r_i^{(3)}={}&
\sum_{s=0}^{58}d_s\binom{n+i}{s}
\left[
\binom{2n+i-s}{b}
+(b+1)\binom{2n+i-s}{b+1}
\right]\\
&-p^2(C+1)\sum_{d=2}^{30}(d-2)!
                 \binom{2n+i}{b+d}
\pmod{p^3}.
\end{aligned}}
\tag{7.1}
$$


The nonconstant $s$-terms in the second block have valuation at least three, which explains their absence.

The whole logarithmic contribution is zero here because


$$
F_n-F_b-\lfloor\log_p(2n+b-1)\rfloor\ge3
$$


throughout the assigned class. At a higher precision this bound must again be checked; it is not a permanent license to discard that forcing.

### 7.2 Actual inverse with all terms required at this precision

Define the finite matrix


$$
E^*_{kj}
=
\sum_{s=1}^{58}\frac{d_s}{p}
\binom{j+s}{s}\binom n{j+s-k}\pmod{p^2},
\tag{7.2}
$$


and


$$
\mathcal E=E^*T(-n).
$$


The entries in (7.2) are obtained directly by applying $P^{-1}$ to the defining contact sum. All matrix indices remain $0,\ldots,b-1$.

Then


$$
\boxed{
T(-n)\widetilde N^{-1}
\equiv
T(-2n)(I-p\mathcal E+p^2\mathcal E^2)P^{-1}
\pmod{p^3}.
}
\tag{7.3}
$$


The quadratic inverse correction is necessary.

Set


$$
\eta^{(3)}
=
T(-2n)(I-p\mathcal E+p^2\mathcal E^2)P^{-1}r^{(3)}
\pmod{p^3}.
$$


The second normalized $Q$-digit is consequently the explicit vector


$$
\boxed{
Q^{[2]}_j\equiv
\frac{
W_b\delta_{j,b}
+W_j(j\eta^{(3)}_{j-1}-\eta^{(3)}_j)
}{p^2}\pmod p.
}
\tag{7.4}
$$


The divisions are valid by (6.2). Computing the numerator modulo $p^3$ supplies the quotient modulo $p$, including the endpoint.

### 7.3 Actual evaluated normalized contractions

Define the exact integral columns


$$
P^{[1]}=Z_w/p,\qquad Q^{[2]}=Y/p^2.
$$


Then


$$
\mathfrak D=p^2(P^{[1]})^TP^{[1]},\qquad
\Xi=p^3(P^{[1]})^TQ^{[2]}.
$$


Their first evaluated digits are


$$
\boxed{
(P^{[1]})^TP^{[1]}
\equiv6J^2\sum_qT_q^2\pmod p,
}
\tag{7.5}
$$


and


$$
\boxed{
(P^{[1]})^TQ^{[2]}
\equiv
J\sum_{q=0}^{B}(-1)^qT_q
\left(-Q^{[2]}_{pq}+2Q^{[2]}_{pq+1}-Q^{[2]}_{pq+2}\right)
\pmod p.
}
\tag{7.6}
$$



These are finite-depth laws for the actual contractions. In particular, they expose the new changing factorial boundary $b+2=p^2(C+1)$.

I have not proved that the two residues in (7.5)–(7.6) are simultaneously units, or that their subsequent valuations agree. On the infinite subclass (C), the entire first normalized $P$-digit is zero, so another lift is genuinely necessary.

---

## 8. Final gcd, actual denominator, and same-center error

Let


$$
F_n=v_{29}(n!),\qquad F_b=v_{29}(b!),
$$


and set


$$
\alpha=v_{29}\bigl((P^{[1]})^TP^{[1]}\bigr),\qquad
\gamma=v_{29}\bigl((P^{[1]})^TQ^{[2]}\bigr).
$$


The norm is positive. The complete mixed contraction is nonzero on the original family by the retained original $3$-adic theorem, so both valuations are finite.

The local least actual $B$-lift denominator remains


$$
v_{29}(d_B)=0.
$$


For


$$
N_B=d_B[u,v],\quad
A_B=N_{B,1}^T\Omega N_{B,1},\quad
H_B=N_{B,1}^T\Omega N_{B,2},
$$


retain


$$
g_B=\gcd(A_B,|H_B|),\qquad
p_n=H_B/g_B,\qquad q_n=A_B/g_B.
$$


The exact local identities now read


$$
\boxed{
v_{29}(g_B)=
\min\{4F_n+2+\alpha,\ 2F_n+F_b+3+\gamma\},
}
\tag{8.1}
$$




$$
\boxed{
v_{29}(q_n)=
\max\{0,\ 2F_n-F_b-1+\alpha-\gamma\}.
}
\tag{8.2}
$$



Thus the next relative obligation is exactly


$$
\gamma-\alpha.
$$


Neither (7.5) nor the Boolean content rule evaluates that difference at all depths.

At the supplied dependency status of the complete signed-rate theorem, with


$$
\tau=\left(2+\frac1{2001}\right)\log(1+\sqrt2),
$$


the same odd centers satisfy


$$
\epsilon_n=c_n-(e+\pi)>0\quad\text{eventually},\qquad
\log|\epsilon_n|=-\tau n+o(n).
$$


Their whole primitive evaluated error is


$$
\boxed{
L_n=q_n(e+\pi)-p_n=-q_n\epsilon_n<0
\quad\text{eventually}.
}
$$


All prime contributions remain:


$$
\begin{aligned}
\log|L_n|
={}&\left(n-\frac{b+13}{2}\right)\log3\\
&+\max\{0,2F_n-F_b-1+\alpha-\gamma\}\log29\\
&+\sum_{\ell\ne3,29}v_\ell(q_n)\log\ell
-\tau n+o(n).
\end{aligned}
$$


No even-family valuation is added to this accounting.

---

# Concluding ledger

## (1) New result and proof status

**Audit passed**

- A5 turn 7’s full even binary column formula.
- Its actual inverse-contact boundary cancellation.
- Its evaluated norm identity and infinite nonunit obstruction.
- Its modulo-$8$/modulo-$16$ exact divisions.
- Its transfer is an all-index-digit rule, not an all-depth valuation rule.

**Proved here from the supplied defining contact construction**

- The actual next odd $P$-column digit (B) on $a\equiv31\pmod{812}$.
- The complete stronger divisibility $V_w/b!\in29^2\mathbb Z_{29}^{b+1}$ on that class.
- The exact first-lift Boolean content rule (5.3), including its changed upper indices and coefficient boundary.
- The infinite obstruction
  

$$
a\equiv432827\pmod{682892}
  \Longrightarrow Z_w\in29^2\mathbb Z_{29}^{b+1}.
$$


  Therefore content one is **not uniform** on the proposed candidate class.
- An explicit complete residual, actual inverse, second normalized $Q$-digit, and evaluated-contraction reduction through $29^3$.

**Not proved**

A uniform relative norm/mixed valuation law, a favorable global final-gcd rate, or irrationality or rationality of $e+\pi$.

## (2) Exact remaining bottleneck

On $a\equiv31\pmod{812}$, after the now justified normalizations,


$$
\boxed{
\gamma-\alpha=
v_{29}\bigl((P^{[1]})^TQ^{[2]}\bigr)
-
v_{29}\bigl((P^{[1]})^TP^{[1]}\bigr).
}
$$


The explicit formula (7.4) is the next actual-column input to this problem.

On the proved subclass where $P^{[1]}\equiv0\pmod{29}$, a further $P$-lift is unavoidable. The first-carry scalar congruence cannot replace that lift.

Even a local solution would leave the other prime contributions in the final same-center denominator.

## (3) Bounded exact computation request

**One auxiliary falsification audit of the new lifted-column theorem—not an original-index prime-mass calculation.**

Use


$$
p=29,\qquad b=839,\qquad n=2001b=1678839,
\qquad m_w=1,
$$


with the original defining contact and complete forcing, modulo $29^3$.

This auxiliary pair has precisely the low-digit configuration used in the proof:


$$
B=28,\quad N=57891,\quad N\bmod29=7,\quad
\lfloor N/29\rfloor\bmod29=24.
$$


It is not of the form $b=3^a$, so no original-family $3$-law or aggregate conclusion is requested for it.

**Expected verifiable outputs**

1. Check
   

$$
J\equiv13\pmod{29}.
$$



2. For all $0\le q\le28$, compare the direct $Z_w/29\bmod29$ with
   

$$
13(-1)^q
   \frac{\binom{57891}{q}
         \binom{115782+28-q}{28-q}}{29}
   (-1,2,-1)
$$


   at coordinates $29q,29q+1,29q+2$, and zero elsewhere.

   A specific nonzero unit prediction is
   

$$
T_0\equiv18,\qquad
   \boxed{Z_{w,0}/29\equiv27\pmod{29}.}
$$



3. Check the whole-column prediction
   

$$
\boxed{V_w/b!\equiv0\pmod{29^2}.}
$$



4. Compare the direct $Q^{[2]}\bmod29$ with (7.1)–(7.4), and return the two evaluated residues (7.5)–(7.6), without an imposed nonzero prediction for the mixed residue.

5. Certify omission of the complete logarithmic forcing at this precision using
   

$$
F_n=59957,\quad F_b=28,\quad
   \lfloor\log_{29}(2n+b-1)\rfloor=4,
$$


   so its divided valuation is at least
   

$$
\boxed{59925>3.}
$$



This would test the new first lift, its inverse cancellation, and its changed factorial boundary in one bounded calculation. It would not prove any infinite assertion by computation.
