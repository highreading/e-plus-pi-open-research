> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 Turn 10 — Completing the exponential source and isolating its denominator payments

## Abstract and proof status

This report does **not** prove either rationality or irrationality of $e+\pi$.

The principal new result is an exact completion of the exponential source in the original finite producer. It keeps the entire factorial subtraction and shows explicitly how its upper boundary contribution cancels the physical terminal. The resulting formula has a **nonzero lower-boundary term**:


$$
\boxed{
Y^{e}
=\frac1{b!}\left(\mathcal RA^{-1}\widehat r^{\,e}+e_0\right).
}
\tag{1}
$$


Here $\widehat r^{\,e}$ is an explicitly specified integral source obtained by finite integration by parts. Formula (1) is not an omission of the exterior source: the full exterior has been included before the cancellation is made.

Two arithmetic consequences are also proved.

* The logarithmic source has an explicit common **all-prime source divisor**
  

$$
\boxed{
  K_n=
  \frac{(n!)^2}
  {b!\,2^{(n-1)/2}\operatorname{lcm}(1,\ldots,n+1)}
  \in\mathbb Z_{>0}
  }
  \tag{2}
$$


  at every original index, and $K_n\mid r_i^F$ on every original contact row.
* With the actual $d_B$ fixed, the auxiliary clearer from Turn 9 satisfies an exact denominator reduction:
  

$$
\boxed{
  m_B=
  \operatorname{lcm}\!\left(
  \frac{\operatorname{den}(J_B)}
       {\gcd(\operatorname{den}(J_B),|r_0^F|)},
  \operatorname{den}(U_B)
  \right).
  }
  \tag{3}
$$


  In particular, the denominator of the complete exponential scalar does not introduce an independent third payment. A fully paid upper divisor for $m_B$, and an explicit factorial cancellation in its first argument, are given below.

These are source and denominator-bookkeeping results. They do **not** establish a new divisor of the actual final $g_B$. In particular, neither (1) nor (2) evaluates the remaining contraction against the actual first column.

The established new saving in the logarithm of the **actual primitive denominator** is therefore


$$
\boxed{\Delta\log q_n=0.}
$$



---

## 1. Original family, boundaries, and normalization

Throughout,


$$
p=29,\qquad
b=3^{249005515+574312172u},\qquad
n=2001b,
$$


with


$$
u=2+29^9t,\qquad t\in\mathbb Z_{\ge0}.
$$


In particular, every original $b$ and $n$ is odd.

Set


$$
N=n+2,\qquad W_j=\binom Nj.
$$


The contact coordinates remain $0\le j<b$; the recurrence rows remain


$$
1\le i\le b-2;
$$


and reconstructed vectors have coordinates $0\le j\le b$. Write


$$
(Cv)_j=jv_{j-1}-v_j,\qquad v_{-1}=v_b=0,
\qquad
\mathcal R=\operatorname{diag}(W_j)C.
$$



No block is enlarged. Thus, in particular, the retained decomposition


$$
b=29^3B+5044,\qquad j=\ell+29^3J<b
$$


still has endpoint $B$ for $\ell<5044$, and endpoint $B-1$ otherwise.

Let


$$
Q(z)=1-z+\frac{z^2}{2},\qquad a_s(n)=[z^s]Q(z)^n.
$$


The actual matrix is the original square restriction of


$$
A_{\rm ext}(i,j)
=\sum_s a_s(n)(n+i)_{\underline s}
\binom{2n+i-s}{j}.
$$


The complete sources are


$$
f_i^0=
\frac{(n+i)!}{n!}
[z^n](1+2z+2z^2)^n(1+z)^i
$$


and


$$
r_i=r_i^e+r_i^F,
$$


where


$$
r_i^e=\sum_s a_s(n)(n+i)_{\underline s}T_{2n+i-s},
\qquad
T_m=\frac1{b!}\sum_{q=b}^{m}(m)_{\underline q},
$$


and


$$
r_i^F=\frac1{b!}
\sum_s a_s(n)(n+i)_{\underline s}L_{2n+i-s}.
$$



The complete physical columns remain


$$
Z_w=\mathcal RA^{-1}f^0,\qquad
Y=\mathcal RA^{-1}r+W_be_b,
$$


and


$$
Y^e=\mathcal RA^{-1}r^e+W_be_b.
$$



### Established results reused

I reuse the proved source recurrence and displacement identities


$$
\mathcal Df^0=0,\qquad
\mathcal Dr^F=0,\qquad
\mathcal Dr^e=\mathcal H,
$$




$$
\mathcal DA=-\mathcal VC,\qquad
\mathcal H=\mathcal Ve_b,
$$


where, on the original recurrence rows,


$$
(\mathcal Dx)_i
=x_{i+1}-\alpha_ix_i+\beta_ix_{i-1}+\gamma_ix_{i-2},
$$




$$
\alpha_i=2n+2i+1,\quad
\beta_i=\frac{(n+i)(n+3i-1)}2,\quad
\gamma_i=\frac{(n+i)(n+i-1)(1-i)}2.
$$


At $i=1$, $\gamma_1=0$; no negative coordinate is introduced.

The source determinant evaluated in Turn 9 is also reused:


$$
\boxed{
f_0r_1^F-f_1r_0^F=-G_n,
\qquad
G_n=\frac{2^{n+1}(n!)^2}{b!}.
}
\tag{4}
$$


Its proof by the Legendre companion recurrence and Casoratian is not repeated or claimed as a new method.

---

## 2. Finite integration by parts for the complete exponential source

### 2.1 An integral polynomial attached to each actual row

Define


$$
P_i(x)=x^nQ(D_x)^n x^{n+i},
\qquad D_x=\frac{d}{dx}.
$$


Expansion gives


$$
P_i(x)=
\sum_s a_s(n)(n+i)_{\underline s}x^{2n+i-s}.
\tag{5}
$$


Therefore


$$
\boxed{
A_{\rm ext}(i,j)=[t^j]P_i(1+t).
}
\tag{6}
$$



Although $Q(z)$ has a coefficient $1/2$, the operator


$$
Q(D_x)=1-D_x+\frac{D_x^2}{2}
$$


preserves $\mathbb Z[x]$: $D_x^2/2$ sends $x^m$ to
$\binom m2x^{m-2}$. Consequently,


$$
P_i(x)\in\mathbb Z[x],
\qquad
A_{\rm ext}(i,j)\in\mathbb Z.
\tag{7}
$$



This is an all-prime integrality statement, not merely $29$-integrality.

For a polynomial $P$, put


$$
\mathscr S P=\sum_{k=0}^{\deg P}D_x^kP.
$$


This is a finite operator satisfying


$$
(1-D_x)\mathscr SP=P.
$$


Repeated integration by parts yields


$$
\int_0^\infty e^{-t}P(1+t)\,dt=(\mathscr SP)(1).
\tag{8}
$$


Every boundary contribution at infinity vanishes because an exponential dominates a polynomial. At the lower endpoint, all the derivatives of $P$ appearing in $\mathscr SP$ remain.

Define the completed exponential source by


$$
\boxed{
\widehat r_i^{\,e}:=(\mathscr SP_i)(1).
}
\tag{9}
$$


It is integral.

There is also a division-free factorial-moment evaluation of (9). Let


$$
E_0=1,\qquad E_m=mE_{m-1}+1.
$$


Then


$$
E_m=m!\sum_{k=0}^m\frac1{k!}
=\int_0^\infty e^{-t}(1+t)^m\,dt,
$$


so


$$
\widehat r_i^{\,e}
=\sum_s a_s(n)(n+i)_{\underline s}E_{2n+i-s}.
\tag{10}
$$


Formula (10), together with the integral-polynomial construction (5), introduces no new rational denominator.

It does not, by itself, evaluate an original-size final contraction.

---

### 2.2 The complete factorial subtraction

Let


$$
a=(0!,1!,\ldots,(b-1)!)^T.
$$


From (6),


$$
\widehat r_i^{\,e}
=\sum_{j=0}^{2n+i}j!\,A_{\rm ext}(i,j).
\tag{11}
$$


On the other hand, the original definition of $T_m$ gives


$$
r_i^e
=\sum_{j=b}^{2n+i}\frac{j!}{b!}A_{\rm ext}(i,j).
\tag{12}
$$


Thus every original exterior column is present, and


$$
\boxed{
b!r^e=\widehat r^{\,e}-Aa.
}
\tag{13}
$$



In particular, (12) proves directly that


$$
\boxed{r^e\in\mathbb Z^b.}
\tag{14}
$$


The quotient $j!/b!$ is integral for every retained exterior index $j\ge b$.

Equation (13) is not a replacement of the exterior by a single boundary column. It is the exact sum of the whole exterior, followed by subtraction of all $b$ original interior factorial columns.

---

### 2.3 The physical terminal becomes a lower-boundary term

The finite reconstruction of $a$ can be evaluated completely:


$$
(Ca)_0=-1,
$$




$$
(Ca)_j=j(j-1)!-j!=0
\qquad(1\le j<b),
$$


and, because $a_b=0$,


$$
(Ca)_b=b(b-1)!=b!.
$$


Hence


$$
\boxed{
\mathcal Ra=-e_0+b!W_be_b.
}
\tag{15}
$$



Apply the same finite $A^{-1}$ to (13), reconstruct, and add the physical terminal:


$$
\begin{aligned}
Y^e
&=\frac1{b!}\mathcal RA^{-1}\widehat r^{\,e}
-\frac1{b!}\mathcal Ra+W_be_b\\
&=\frac1{b!}\left(\mathcal RA^{-1}\widehat r^{\,e}+e_0\right).
\end{aligned}
$$


This proves (1).

The cancellation of the upper terminal in this calculation is legitimate because it has been explicitly matched against the upper return in (15). The lower return $e_0/b!$ remains. Deleting it would change the complete column.

Also, $A^{-1}$ is still the original finite inverse. Any lower and upper returns used in an implementation of that inverse are unchanged.

---

## 3. The completed source in actual final normalization

Turn 9 defines a rational force functional $\mathcal L_B$ after fixing:

* the actual first column;
* the actual least simultaneous clearer $d_B$;
* the original column-normalization factors;
* the actual mixed contraction.

It also retains a fixed physical-endpoint contribution.

These data determine a rational linear functional $\mathcal T_B$ on the physical reconstructed space such that


$$
\mathcal L_B(s)=\mathcal T_B(\mathcal RA^{-1}s),
\qquad
H_B=\mathcal T_B(Y).
\tag{16}
$$


This does **not** identify $H_B$ with an unnormalized dot product $Z_w^TY$.

For completeness, the extension in (16) is well-defined. The image of $\mathcal R$ has dimension $b$, and $e_b$ is not in it: solving $Cv=e_b$ from the lower boundary forces $v=0$, contradicting its last row. Thus the image of $\mathcal R$, together with the physical endpoint direction, is the whole reconstructed space.

Keep


$$
J_B=\mathcal L_B(f^0),\qquad
U_B=\mathcal L_B(h^{(1)}),
$$


with $h^{(1)}_0=0,h^{(1)}_1=1$, and let $H_{E,B}$ be the actual complete exponential mixed response.

Applying (1) through this fixed functional gives


$$
\boxed{
H_{E,B}
=\frac1{b!}
\left(\mathcal L_B(\widehat r^{\,e})+\mathcal T_B(e_0)\right).
}
\tag{17}
$$


Consequently,


$$
\boxed{
I_B+C_B
=\frac{m_B}{b!}
\left(
b!r_0^FJ_B
+f_0\mathcal L_B(\widehat r^{\,e})
+f_0\mathcal T_B(e_0)
\right).
}
\tag{18}
$$



This is a boundary-correct reduction of the complete exponential residue in actual normalization. It is **not an evaluation of that residue**. The lower-boundary scalar in (18) and the actual directional contraction remain to be controlled.

A proposed argument that factors a large common divisor from the completed source while omitting $\mathcal T_B(e_0)$ therefore fails at a precise point: it has removed a term belonging to the original physical column.

---

## 4. An explicit factorial-scale divisor of the logarithmic source

The next result concerns the source lattice, not the final gcd.

### 4.1 Denominators of the classical companion

Use the notation from Turn 9:


$$
e_n=p_n(1),\qquad
d_n=\frac2{\mathrm i}\int_{\zeta_-}^{\zeta_+}
\frac{p_n(1)-p_n(t)}{1-t}\,dt.
$$


The already established recurrences are


$$
(n+1)e_{n+1}=(2n+1)e_n+ne_{n-1},
$$




$$
(n+1)d_{n+1}=(2n+1)d_n+nd_{n-1},
$$


with


$$
e_0=e_1=1,\qquad d_0=0,\quad d_1=4.
$$



The Rodrigues coefficient formula gives


$$
e_j=[z^j]\left(\frac12+z+z^2\right)^j.
$$


Every term contributing to the central coefficient uses the same number, say $r$, of constant and quadratic factors. Hence


$$
\boxed{
2^{\lfloor j/2\rfloor}e_j\in\mathbb Z.
}
\tag{19}
$$



A useful companion formula follows directly from the recurrences. Set


$$
E(s)=\sum_{j\ge0}e_js^j=(1-2s-s^2)^{-1/2},
\qquad
D(s)=\sum_{j\ge0}d_js^j.
$$


The recurrence for $d_j$ gives


$$
(1-2s-s^2)D'(s)-(1+s)D(s)=4.
$$


Since


$$
\frac{E'(s)}{E(s)}=\frac{1+s}{1-2s-s^2},
$$


we obtain


$$
\left(\frac{D(s)}{E(s)}\right)'=4E(s).
$$


Using $D(0)=0$,


$$
D(s)=4E(s)\int_0^sE(t)\,dt.
$$


Coefficient comparison proves


$$
\boxed{
d_j=4\sum_{k=1}^j\frac{e_{j-k}e_{k-1}}{k}.
}
\tag{20}
$$



This classical companion calculation is used only to bound denominators. It is not a new Casoratian method.

Let


$$
L_m^{\rm lcm}=\operatorname{lcm}(1,\ldots,m).
$$


Equations (19)–(20) imply


$$
\boxed{
2^{\lfloor(j-1)/2\rfloor}L_j^{\rm lcm}\,d_j\in\mathbb Z.
}
\tag{21}
$$



---

### 4.2 The common source divisor

Every original $n$ is odd. Put


$$
\kappa_n=2^{(n-1)/2}L_{n+1}^{\rm lcm},
\qquad
M_n=\frac{(n!)^2}{b!}.
$$


The actual initial charges, evaluated in Turn 9, are


$$
r_0^F=M_nd_n,
$$




$$
r_1^F=M_n\frac{n+1}{2}(d_{n+1}+d_n).
\tag{22}
$$


Since $(n+1)/2$ is integral, (21) shows that both expressions in (22) are integer multiples of $M_n/\kappa_n$, provided the latter is integral.

#### Lemma 4.1

At every original index,


$$
\kappa_n\mid M_n.
$$



**Proof.** For an odd prime $\ell$, $n+1$ is not a power of $\ell$, because $n+1$ is even. Therefore


$$
v_\ell(L_{n+1}^{\rm lcm})=v_\ell(L_n^{\rm lcm})
\le v_\ell(n!).
$$


Since $b\le n$,


$$
v_\ell(M_n)=2v_\ell(n!)-v_\ell(b!)\ge v_\ell(n!).
$$


This covers all odd primes.

At $2$, using $n$ odd,


$$
v_2(n!)\ge\frac{n-1}{2}+\left\lfloor\frac n4\right\rfloor,
\qquad
v_2(b!)\le b-1.
$$


Hence


$$
v_2(M_n)\ge n-b+2\left\lfloor\frac n4\right\rfloor
\ge\frac{3n-3}{2}-b.
$$


Subtracting


$$
v_2(\kappa_n)=\frac{n-1}{2}+\lfloor\log_2(n+1)\rfloor
$$


leaves at least


$$
n-b-1-\lfloor\log_2(n+1)\rfloor.
$$


For $n=2001b\ge2001$, this is positive; for example,
$\log_2(n+1)\le n/2$ gives the lower bound $n/2-b-1>0$.
Thus the divisibility also holds at $2$. ∎

Define the positive integer


$$
K_n=M_n/\kappa_n.
$$


Equations (22) prove $K_n\mid r_0^F,r_1^F$.

The coefficients $\alpha_i,\beta_i,\gamma_i$ of the homogeneous recurrence are integers. For $\beta_i$, the two factors in its numerator differ by the odd integer $2i-1$; for $\gamma_i$, the consecutive factors $n+i,n+i-1$ supply the factor $2$. Forward recurrence therefore preserves divisibility by $K_n$.

### Theorem 4.2 — All-prime logarithmic source content

At every unchanged original index,


$$
\boxed{
K_n\mid r_i^F\qquad(0\le i<b).
}
\tag{23}
$$


Moreover,


$$
\boxed{K_n\mid G_n.}
\tag{24}
$$



The latter follows from


$$
G_n=2^{n+1}M_n=2^{n+1}\kappa_nK_n.
$$



Its exact valuation is


$$
\boxed{
v_\ell(K_n)=
2v_\ell(n!)-v_\ell(b!)
-\frac{n-1}{2}\mathbf1_{\ell=2}
-\lfloor\log_\ell(n+1)\rfloor.
}
\tag{25}
$$


All these exponents are nonnegative on the original family.

The elementary bound $\log L_m^{\rm lcm}=O(m)$, together with Stirling’s formula, gives


$$
\boxed{
\log K_n=
\left(2-\frac1{2001}\right)n\log n+O(n).
}
\tag{26}
$$


No prime-number theorem is needed for this scale statement.

**Scope limitation.** Equation (23) is a divisor of the actual source vector. It does not imply divisibility of $\mathcal RA^{-1}r^F$, of either actual weighted column content, or of $g_B$.

---

## 5. A restriction on inverse-denominator primes

There is a short original-object argument that removes three primes from the finite inverse payment.

### Theorem 5.1

If $\ell$ is an odd prime dividing $n$, then


$$
\det A\equiv1\pmod\ell.
\tag{27}
$$


In particular, on the original family,


$$
A\in\operatorname{GL}_b(\mathbb Z_3)
\cap\operatorname{GL}_b(\mathbb Z_{23})
\cap\operatorname{GL}_b(\mathbb Z_{29}).
\tag{28}
$$



**Proof.** Work with polynomial differential operators over $\mathbb Z_\ell$. Since $2$ is a unit and the operators commute,


$$
Q(D)^\ell
\equiv 1-D^\ell+2^{-\ell}D^{2\ell}\pmod\ell.
$$


The operator $D^\ell$ sends every integral polynomial into $\ell\mathbb Z_\ell[x]$, because its coefficients contain products of $\ell$ consecutive integers. Thus


$$
Q(D)^\ell\equiv1\pmod\ell.
$$


If $\ell\mid n$, it follows that


$$
Q(D)^n\equiv1\pmod\ell.
$$


Using (5)–(6),


$$
A_{ij}\equiv\binom{2n+i}{j}\pmod\ell.
$$



The finite matrix on the right has determinant $1$. Indeed, Vandermonde’s identity factors it as


$$
\binom{2n+i}{j}
=\sum_{k=0}^{b-1}\binom ik\binom{2n}{j-k},
$$


the product of a lower unitriangular and an upper unitriangular $b\times b$ matrix. Hence (27).

Finally,


$$
2001=3\cdot23\cdot29,
$$


so the conclusion applies to $3,23,29$. ∎

The $29$-unit conclusion was already established. The point here is the elementary extension to the other two prime divisors of the actual $n$, without a new matrix computation.

It supplies no claim about inverse denominators at other primes.

---

## 6. The actual auxiliary clearer after $d_B$ is fixed

For a rational number $x$, let $\operatorname{den}(x)$ denote its positive reduced denominator, with $\operatorname{den}(0)=1$.

The Turn 9 complete identity is


$$
f_0H_B=r_0^FJ_B+f_0H_{E,B}-G_nU_B.
\tag{29}
$$


Its quantities are in actual final normalization, with the original $d_B$ fixed.

The auxiliary $m_B$ is the least simultaneous clearer of


$$
r_0^FJ_B,\qquad f_0H_{E,B},\qquad U_B.
$$



### Theorem 6.1 — Exact removal of the third denominator payment

At every original index,


$$
m_B=
\operatorname{lcm}\bigl(
\operatorname{den}(r_0^FJ_B),\operatorname{den}(U_B)
\bigr).
\tag{30}
$$


Equivalently, with


$$
s_J=\operatorname{den}(J_B),\qquad
s_U=\operatorname{den}(U_B),
$$


one has


$$
\boxed{
m_B=
\operatorname{lcm}\left(
\frac{s_J}{\gcd(s_J,|r_0^F|)},s_U
\right).
}
\tag{31}
$$



**Proof.** Theorem 4.2 makes $r_0^F$ integral. Also $G_n,f_0,H_B$ are integers. Rearranging (29),


$$
f_0H_{E,B}=f_0H_B-r_0^FJ_B+G_nU_B.
$$


Thus any integer clearing $r_0^FJ_B$ and $U_B$ automatically clears $f_0H_{E,B}$. Conversely, a simultaneous clearer of the three original scalars must clear those two. This proves (30).

For an integer $r$ and a reduced rational $a/s$,


$$
\operatorname{den}(ra/s)=s/\gcd(s,|r|).
$$


Applying this to $r=r_0^F$ proves (31). ∎

Since $K_n\mid r_0^F$, this gives the explicit bound


$$
\boxed{
m_B\mid
\operatorname{lcm}\left(
\frac{s_J}{\gcd(s_J,K_n)},s_U
\right).
}
\tag{32}
$$


Prime by prime,


$$
\boxed{
v_\ell(m_B)\le
\max\left\{
[v_\ell(s_J)-v_\ell(K_n)]_+,\,
v_\ell(s_U)
\right\}.
}
\tag{33}
$$



Thus the factorial-scale source divisor can eliminate the norm-direction contribution to the auxiliary denominator. It does not eliminate the $h^{(1)}$-direction payment $s_U$.

### 6.1 A fully paid upper divisor

Write


$$
\mathcal T_B(x)=t_B^Tx,
$$


where $t_B\in\mathbb Q^{b+1}$ is the actual functional from §3. Define


$$
\rho_B=\min\{r\ge1:rt_B\in\mathbb Z^{b+1}\}.
$$


This is an auxiliary payment belonging to the actual normalization; it is not substituted for $d_B$.

Let


$$
\Delta_A=\min\{\Delta\ge1:\Delta A^{-1}\in M_b(\mathbb Z)\}.
$$


This is the actual inverse clearer, equivalently the largest Smith invariant of the integral matrix $A$.

Since $f^0,h^{(1)},r^e,r^F$ are integral and $\mathcal R$ is integral,


$$
s_J\mid\rho_B\Delta_A,\qquad
s_U\mid\rho_B\Delta_A.
$$


Therefore


$$
\boxed{m_B\mid\rho_B\Delta_A.}
\tag{34}
$$


There is no additional $b!$ factor in (34).

Theorem 5.1 further gives


$$
v_3(\Delta_A)=v_{23}(\Delta_A)=v_{29}(\Delta_A)=0,
$$


and hence


$$
\boxed{
v_\ell(m_B)\le v_\ell(\rho_B)
\qquad(\ell=3,23,29).
}
\tag{35}
$$



Equations (32)–(35) are genuine denominator bounds after the same actual $d_B$ has been fixed. They remove a redundant scalar clearer and expose precisely which inverse and normalization payments remain.

They are **not yet an asymptotically adequate estimate**: no suitable bound on the actual $s_U$, $\rho_B$, or the remaining prime factors of $\Delta_A$ has been established.

---

## 7. The remaining accepting scalar, with every division exposed

The preceding reduction permits a more specific next arithmetic target.

Put


$$
\tau_B=\rho_Bt_B\in\mathbb Z^{b+1}
$$


and define the integral adjoint numerator


$$
z_B=
\Delta_AA^{-T}C^T\operatorname{diag}(W_j)\tau_B
\in\mathbb Z^b.
$$


Then, exactly,


$$
\mathcal L_B(s)=\frac{z_B^Ts}{\rho_B\Delta_A},
\qquad
\mathcal T_B(e_0)=\frac{(\tau_B)_0}{\rho_B}.
$$


Define the integer


$$
\Xi_B=
b!r_0^Fz_B^Tf^0
+
f_0\left(z_B^T\widehat r^{\,e}
+\Delta_A(\tau_B)_0\right).
\tag{36}
$$


Equation (18) becomes


$$
\boxed{
I_B+C_B
=\frac{m_B\Xi_B}{b!\rho_B\Delta_A}.
}
\tag{37}
$$



The terms in (36) have specific origins:

* $b!r_0^Fz_B^Tf^0$ is the retained norm-direction contribution;
* $z_B^T\widehat r^{\,e}$ contains the complete exponential source;
* $\Delta_A(\tau_B)_0$ is the lower return left by the exact cancellation of the physical upper terminal.

No denominator in (37) has been suppressed.

### Concrete follow-on lemma

The explicit $K_n$ from (2), rather than an unspecified factorial product, is now a possible test divisor. A sufficient next arithmetic statement would include


$$
K_n\mid A_B
\tag{38}
$$


and


$$
\boxed{
\frac{K_nb!\rho_B\Delta_A}
{\gcd(K_nb!\rho_B\Delta_A,m_B)}
\mid \Xi_B.
}
\tag{39}
$$


Indeed, (39) is exactly the condition $K_n\mid I_B+C_B$, with the divisions in (37) paid.

To make this useful for the actual denominator, one must also control:

1. the loss $\gcd(K_n,m_Bf_0)$;
2. overlap with factors already in the proved gcd, including the actual weighted content $k_1$;
3. the resulting positive parts in the actual prime-by-prime formula for $q_n$.

Equations (38)–(39) remain open. The new work does not prove them merely by defining $\Xi_B$. The outstanding task is an evaluated directional-source or adjoint-boundary identity for (36), not a new name for its contraction.

The exact obstruction to a premature conclusion is now visible: even after the complete factorial subtraction is evaluated, the finite inverse acts on a second direction whose denominator is not controlled by the already cleared complete columns. The lower-boundary scalar also survives.

---

## 8. A bounded exact arithmetic check of the new completion

No original-size computation is proposed. The old determinant check, rank audit, and recurrence audit need not be repeated.

A genuinely new small check can verify the factorial completion and display the inverse-denominator issue.

### Inputs

Use only the auxiliary values


$$
n=3,\qquad b=3,\qquad N=5.
$$


These are **not** original-family indices.

Form


$$
Q(z)^3,\qquad
P_i(x)=x^3Q(D_x)^3x^{3+i},
\qquad i=0,1,2.
$$


Compute $A_{ij}=[t^j]P_i(1+t)$ for $0\le i,j\le2$, and compute $E_m$ from


$$
E_0=1,\qquad E_m=mE_{m-1}+1
$$


only through $m=8$.

### Expected exact output

The matrix is


$$
A=
\begin{pmatrix}
-5&-3&15\\
1&-17&-33\\
16&53&13
\end{pmatrix},
\qquad
\det A=-1142=-2\cdot571.
$$


The completed source is


$$
\widehat r^{\,e}=
\begin{pmatrix}
394\\2444\\18101
\end{pmatrix}.
$$


With


$$
a=(1,1,2)^T,
$$


one obtains


$$
Aa=
\begin{pmatrix}
22\\-82\\95
\end{pmatrix},
\qquad
r^e=
\frac{\widehat r^{\,e}-Aa}{6}
=
\begin{pmatrix}
62\\421\\3001
\end{pmatrix}.
$$


The finite reconstruction must give


$$
Ca=(-1,0,0,6)^T,
$$


and, since $W=(1,5,10,10)$,


$$
\mathcal Ra=-e_0+60e_3.
$$


Thus the two sides of


$$
Y^e=\frac{\mathcal RA^{-1}\widehat r^{\,e}+e_0}{6}
$$


must agree exactly.

For the independent homogeneous direction,


$$
h^{(1)}=(0,1,9)^T,
$$


the expected inverse is


$$
A^{-1}h^{(1)}
=\frac1{1142}
\begin{pmatrix}
-4020\\1655\\-1009
\end{pmatrix}.
$$


This illustrates an inverse denominator at a prime not dividing $n$, despite integral source data.

That last observation is only an auxiliary example. It does not prove that the same prime, or any particular inverse loss, occurs on the original family. The infinite-family theorems above rest on their algebraic proofs, not on this calculation.

---

## 9. Actual contents, all-prime gcd, and whole same-index error

The original final normalization is unchanged:


$$
N_B=d_B[\mathbf u_B,\mathbf v_B],
\qquad
\omega_j=\frac{(n+2)!}{(n+2-j)!},
$$




$$
\Omega=\operatorname{diag}(\omega_0^2,\ldots,\omega_b^2),
$$




$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,
\qquad
H_B=N_{B,1}^T\Omega N_{B,2}.
$$


The actual gcd and primitive pair are


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad
p_n=H_B/g_B.
}
\tag{40}
$$


The gcd is over **all primes**, and the primitive multiplier remains


$$
d_B^2/g_B.
$$



Write the actual weighted columns as


$$
\operatorname{diag}(\omega_j)N_{B,i}=k_iv_i,
$$


where $k_i>0$ is the actual content and $v_i$ is primitive. With


$$
S=v_1^Tv_1,\qquad T=v_1^Tv_2,
$$


the unchanged valuation formula is


$$
\boxed{
v_\ell(q_n)=
\left[
v_\ell(k_1)-v_\ell(k_2)+v_\ell(S)-v_\ell(T)
\right]_+.
}
\tag{41}
$$


Neither $K_n$, $\rho_B$, nor $\Delta_A$ replaces these actual contents or the original $d_B$.

At the same original indices,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


and the whole error is


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n.
}
\tag{42}
$$


Using the retained signed whole-error theorem at its stated scope,


$$
\epsilon_n\ne0\quad\text{eventually},
$$


and


$$
\log|\epsilon_n|
=-\lambda n+o(n),
\qquad
\lambda=
\left(2+\frac1{2001}\right)\log(1+\sqrt2).
\tag{43}
$$


Its proof is not contained in the supplied excerpts and is not independently reproduced here.

An irrationality conclusion still requires an infinite subset of the unchanged original indices on which


$$
0<|q_n\epsilon_n|\longrightarrow0.
\tag{44}
$$


For example, an actual bound


$$
\log q_n\le(\lambda-\delta)n
$$


for some fixed $\delta>0$, together with (43), would suffice. No such bound is proved here.

No upper bound on $\nu$ has been inferred from the bound on $c$. The closed scalar-antidifference obstruction has not been enlarged beyond its established ansatz.

---

## 10. Proof-status ledger and conclusion

| Statement | Status |
|---|---|
| Original complete recurrence, displacement, rank-three reduction, and Turn 9 charge determinant | Reused |
| Complete factorial identity $b!r^e=\widehat r^{\,e}-Aa$ | **Proved** |
| Boundary-correct completion $Y^e=(\mathcal RA^{-1}\widehat r^{\,e}+e_0)/b!$ | **Proved** |
| All-prime integrality of the complete exponential source | **Proved** |
| Explicit $K_n\mid r_i^F$ on every original contact row | **Proved** |
| $A$ is a unit matrix locally at $3,23,29$ | **Proved; $29$ reused in scope** |
| Exact reduction of $m_B$ to the two denominators in (31) | **Proved after the actual $d_B$ is fixed** |
| Paid upper divisor $m_B\mid\rho_B\Delta_A$ | **Proved** |
| Asymptotically sufficient control of the actual $h^{(1)}$-direction payment | Open |
| Evaluation of the complete normalized residue $I_B+C_B$ | Open |
| A new nontrivial divisor of the actual final $g_B$ | Not established |
| New saving in $\log q_n$ | **Zero established** |
| Rationality or irrationality of $e+\pi$ | Unresolved |

The new exponential calculation identifies exactly what finite integration by parts accomplishes:


$$
\boxed{
Y^e=\frac1{b!}
\left(\mathcal RA^{-1}\widehat r^{\,e}+e_0\right).
}
$$


It evaluates the complete factorial subtraction and its physical upper-boundary cancellation, while retaining the lower return.

The accompanying arithmetic work supplies a factorial-scale logarithmic **source** divisor and removes the complete exponential scalar as an independent auxiliary denominator payment. It also shows that the actual contact inverse adds no denominators at $3,23,29$.

The exact remaining bottleneck is the normalized accepting scalar (36): its directional contraction and lower-boundary term must be evaluated deeply enough to prove a paid congruence such as (39), together with actual norm divisibility and a bound on the surviving auxiliary losses. Only then can the result pass through the actual contents and all-prime gcd to the primitive denominator.

The only bounded new calculation proposed is the $n=b=3$ completion check in §8, with all inputs and expected outputs specified. It verifies finite algebra only. No original-size calculation, and no inference from auxiliary finite data to the infinite original family, is proposed.
