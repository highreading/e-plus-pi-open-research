> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2, Turn 3 — The complete first-order return cancels; the first possible normalized column is a two-carry column

## Executive assessment

The complete finite-end correction changes the first-order conclusion substantially.

I obtain the following results.

1. **The previous absolute norm statement was redundant.** The already proved divisibility of every reconstructed short-head entry by $29$ implies
   

$$
\mathcal N\equiv0\pmod{841}.
$$


   Thus writing $\mathcal N=a_fT_2\pmod{841}$, without evaluating the coefficient, did not advance the norm calculation.

2. **The complete first-order reconstructed return actually vanishes.** With compatible lifts of the lower-factor coefficients and their crossed-end coefficients,
   

$$
\boxed{
   \mathcal R\bigl(\mathsf R\mathsf D_1\mathsf R\mathsf P_--\mathsf E_1\bigr)h
   \equiv0\pmod{29}.
   }
$$


   This holds for arbitrary heads in the stated short-head range, not merely for the original first force. The proof below combines the finite endpoint with the interior before reducing the reconstructed output. It does not infer cancellation from a block-end recurrence state.

3. **There is an exact, boundary-aware normal ordering behind that cancellation.** After retaining and solving the actual endpoint equations, the complete inverse can be expressed using only upper parameters of the form
   

$$
-2n-a.
$$


   The apparent $-n-a$ return atoms in the uncombined formula cancel against the crossed finite-end terms. This gives a structural zero certificate for the absolute-$841$ short-head contraction: in this combined representation, its $T_1,T_2$ coefficients are both zero.

4. **At the first meaningful output normalization, the leading column is explicit.** For either homogeneous input, and hence for any normalized first-force initial pair, the first possible nonzero column after division by $29^2$ is given below by **four weighted binomial atoms**, with two explicitly specified low-digit coefficient functions. Its evaluation requires the valuation-two weighted layer, not the old valuation-zero $T_1,T_2$ quotient.

5. **The actual finite endpoint is nontrivial even though its first-order reconstructed return cancels.** I give a phase-compatible auxiliary input and a hand-derived endpoint solve:
   

$$
S_{\mathrm{red}}\equiv262I_2,\qquad
   S_{\mathrm{red}}^{-1}\equiv581I_2\pmod{841},
$$


   with a nonzero solved endpoint charge. This is a new bounded certificate, not a request to repeat the accepted kernel controls.

What is **not** obtained is a nonzero original norm digit, a bound on the primitive norm loss $\nu$, or the normalized whole-force alignment. In particular, the first possible normalized column derived here is not certified to have nonzero norm modulo $29$.

---

## 1. Scope and normalization audit

Throughout,


$$
p=29,\qquad
b=3^{249005515+574312172u},\qquad
n=2001b=29\cdot69b,\qquad u\ge0.
$$



The finite domains remain exactly


$$
0\le j<b,\qquad 1\le i\le b-2,\qquad 0\le j\le b
$$


for contact coordinates, source rows, and reconstructed coordinates, respectively.

Write


$$
W_j=\binom{n+2}{j},\qquad
(\mathcal R x)_j=W_j(jx_{j-1}-x_j),
$$


with the actual first and terminal reconstruction rows.

The actual columns remain


$$
Z_w=\mathcal R A^{-1}f^0,\qquad
Y=\mathcal R A^{-1}\mathbf r+W_be_b,
$$


and


$$
P=\frac{Z_w}{p^2},\qquad Q=\frac{Y}{p^3}.
$$



Retain


$$
P=p^c x,\qquad x\ \text{\(p\)-primitive},\qquad
\nu=v_p(x^Tx).
$$


Consequently,


$$
\boxed{
d=v_p(\mathcal N)=2c+4+\nu.
}
\tag{1.1}
$$



The target is still


$$
\boxed{
\mathcal C-p\rho_n\mathcal N\equiv0\pmod{p^{d+2}}.
}
\tag{1.2}
$$



### What the accepted computations establish

The supplied receipt establishes its stated finite controls: five phase kernels, twelve small tails, and ninety-six exact bounded kernels. It does not evaluate an original tail, normalized column, or norm digit.

I neither request those computations again nor request the new modulo-$841$ prefix/rank controls that the coordinator has undertaken.

### Correction to the preceding absolute statement

The depth-one output theorem already gave


$$
\mathcal R A^{-1}h\in p\mathbb Z_p^{b+1}
$$


for the relevant short heads. Therefore


$$
\|\mathcal R A^{-1}h\|^2\in p^2\mathbb Z_p.
$$



Thus


$$
\mathcal N\equiv a_fT_2\pmod{p^2}
$$


was weaker than an established zero unless its coefficient assembly supplied genuinely new relative information. It did not.

The result below improves the output divisibility itself, but even that is not yet a determination of $c$ or $\nu$.

---

## 2. Actual first-order lower-factor coefficients

Put


$$
\phi(z)=1-z+\frac{z^2}{2},\qquad
c_s(n)=s![z^s]\phi(z)^{-n}.
$$


The accepted divided-power inverse has entries


$$
\mathsf D_{jk}=c_{j-k}(n)\binom jk.
$$



Write


$$
m_0=\frac np=69b.
$$


On the actual phase,


$$
\boxed{m_0\equiv7\pmod p.}
\tag{2.1}
$$



Modulo $p^2$,


$$
\mathsf D=I+p\mathsf D_1,
\qquad
\mathsf D_1=\sum_{s=1}^{29}k_s\mathsf D_s,
$$


where


$$
(\mathsf D_s v)_j=\binom js v_{j-s}.
$$



The coefficients are


$$
\boxed{
k_s=m_0(s-1)!(21^s+9^s)\quad(1\le s\le28),
\qquad k_{29}=-m_0
}
\tag{2.2}
$$


in $\mathbb F_{29}$. All $30\le s\le57$ coefficients vanish at this order.

### Derivation

For $s<p$, expand


$$
\phi(z)^{-pm_0}=1-pm_0\log\phi(z)\pmod{p^2}.
$$


Since


$$
\phi(z)=(1-21z)(1-9z)\pmod p,
$$


equation (2.2) follows.

At $s=p$, Frobenius gives


$$
[z^p]\phi(z)^{-pm_0}\equiv m_0\pmod p,
$$


and Wilson gives $p!/p\equiv-1\pmod p$. Hence $k_p=-m_0$.

For $p<s<2p$, the coefficient of $z^s$ is zero modulo $p$, while $s!$ already contains $p$.

For explicit coefficient assembly, the list


$$
C_s=(s-1)!(21^s+9^s),\quad 1\le s\le28,
\qquad C_{29}=-1
$$


is


$$
\begin{array}{c|rrrrrrrrrrrrrrr}
s&1&2&3&4&5&6&7&8&9&10&11&12&13&14&15\\ \hline
C_s&1&0&28&26&23&0&3&21&26&0&19&6&7&0&1
\end{array}
$$




$$
\begin{array}{c|rrrrrrrrrrrrrr}
s&16&17&18&19&20&21&22&23&24&25&26&27&28&29\\ \hline
C_s&15&4&0&26&1&10&0&10&27&5&0&28&2&28 .
\end{array}
\tag{2.3}
$$


The actual $k_s$ are $7C_s\pmod{29}$.

Thus the first-order operator is no longer an unspecified coefficient object.

---

## 3. Exact normal ordering with the finite endpoint retained

This is the central identity.

For clarity, let $\mathsf R_\lambda$ denote the upper transform


$$
(\mathsf R_\lambda)_{jk}=\binom{-\lambda}{k-j}.
$$


Thus the source notation $\mathsf R$ is $\mathsf R_n$.

All operators in this section are applied to finite-support vectors. The temporarily extended coordinates are bookkeeping for crossed finite-boundary terms; they do not enlarge the original contact problem.

### 3.1 Normal-order identity

For every $s\ge0$ and finite-support vector $v$,


$$
\boxed{
(\mathsf R_n\mathsf D_s\mathsf R_n v)_j
=
\sum_{t=0}^s
\binom j{s-t}\binom{-n}{t}
(\mathsf R_{2n+t}v)_{j-s+t}.
}
\tag{3.1}
$$


A term with $j<s-t$ is zero.

Indeed,


$$
\binom{j+\ell}{s}
=\sum_{t=0}^s\binom j{s-t}\binom\ell t,
$$


and


$$
\binom{-n}{\ell}\binom\ell t
=
\binom{-n}{t}\binom{-n-t}{\ell-t}.
$$


Finite upper convolution then gives (3.1).

No division by $s!$ is used.

### 3.2 The complete exterior charge

At precision $p^K$, put


$$
M=29K-1.
$$


The lower factors may be truncated to bandwidth $M$. Let

- $w=\mathsf P_-h$, extended by zero beyond $b-1$;
- $y=T\theta$, where $\theta=A^{-1}h$;
- $K_\times$ be the complete crossed lower-factor matrix, from contact coordinates to rows $b,\ldots,b+M-1$;
- $T_{\rm out}$ be the upper transform on those exterior bookkeeping coordinates.

Define


$$
q=K_\times y,\qquad z=T_{\rm out}q.
$$



The accepted endpoint equation is, equivalently,


$$
\boxed{
(I+K_\times\mathsf D F)q
=
K_\times\mathsf D\mathsf R_n w.
}
\tag{3.2}
$$


This is the same finite return as the supplied Woodbury formula, written in the crossed-row space.

The complete inverse has the identity


$$
\boxed{
\theta
=
\left.
\mathsf R_n\mathsf D\mathsf R_n(w+z)
\right|_{0\le j<b}
\pmod{p^K}.
}
\tag{3.3}
$$



#### Why (3.3) retains the boundary

The finite factorization says that, for the zero-extended $y$,


$$
\left.THy\right|_{j<b}=w.
$$


Its actual outside part is


$$
\left.THy\right|_{j\ge b}=T_{\rm out}K_\times y=z.
$$


Therefore


$$
THy=w+z.
$$


Applying the finite-support inverses gives


$$
y=\mathsf D\mathsf R_n(w+z),
\qquad
\theta=\mathsf R_ny.
$$


The outside vanishing condition on $y$ is exactly the endpoint solve (3.2).

Thus (3.3) is not an infinite inverse substituted for the finite inverse. The exterior vector $z$ is determined by the complete finite return.

### Consequence

Applying (3.1) to (3.3), all upper-binomial factors have type


$$
\boxed{-2n-a.}
\tag{3.4}
$$



For the head part, the finite head transform supplies the usual additional small shift in $a$. For the exterior part, each component of $z$ supplies a binomial whose lower index retains the actual crossed endpoint $b+r$.

This is why combining the endpoint **before** taking the observable quotient matters.

---

## 4. The complete first-order return

Let


$$
v=\mathsf R_n\mathsf P_-h.
$$


For a compatible first-order lift, define the crossed divided-power values


$$
t_r=
\sum_{\substack{1\le s\le29\\s>r}}
k_s\binom{b+r}{s}v_{b+r-s},
\qquad 0\le r\le28.
\tag{4.1}
$$


The crossed lower factor at first order is the negative of this operator.

The first-order contact correction is therefore


$$
\boxed{
\mathsf C_1h
=
\mathsf R_n\mathsf D_1v+\mathsf R_nF\,t,
}
\tag{4.2}
$$


where $\mathsf C_1=\mathsf R\mathsf D_1\mathsf R\mathsf P_--\mathsf E_1$ modulo $p$.

The exact finite convolution identity


$$
\boxed{
(\mathsf R_nF)_{jr}
=
\binom{-n}{b+r-j}
-\sum_{u=0}^r
\binom{-2n}{b+u-j}\binom n{r-u}
}
\tag{4.3}
$$


shows what cancels.

The first term in (4.3) supplies precisely the missing upper-transform tail in $\mathsf R_n\mathsf D_1v$. Hence


$$
\boxed{
\mathsf C_1h
=
\mathsf R_n\mathsf D_1\mathsf R_n w
-
\sum_{u=0}^{28}
\binom{-2n}{b+u-j}(T_{\rm out}t)_u
}
\tag{4.4}
$$


coordinatewise, using the compatible lifts just specified.

By (3.1), both terms in (4.4) consist entirely of $\sigma=2$ atoms.

### 4.1 Scope of the weighted annihilator

The proof of Turn 2’s weighted $\sigma=2$ theorem extends, without changing its digit argument, from $a\le244$ to


$$
\boxed{
0\le a\le435,\qquad -244\le v\le245.
}
\tag{4.5}
$$


The reason is exact: the low two-digit part of $2n+a-1$ is


$$
405+a<841,
$$


so its digits $2,3,4,5$ remain the same four digits used in that proof.

Thus, throughout (4.5),


$$
\boxed{
W_j\binom{-2n-a}{b+v-j}\in p^2\mathbb Z_p.
}
\tag{4.6}
$$



For heads of length at most $244$, the atoms in (4.4), including reconstruction shifts, lie in this extended box.

### Theorem 4.1 — Complete first-order return cancellation

For every head $h$ of length at most $244$,


$$
\boxed{
\mathcal R\mathsf C_1h\equiv0\pmod p.
}
\tag{4.7}
$$



With the compatible normal-ordered lift (4.4), its reconstructed output is in fact in $p^2\mathbb Z_p^{b+1}$.

Together with the retained baseline annihilation,


$$
\mathcal R\mathsf R_{2n}\mathsf P_-h\equiv0\pmod{p^2},
$$


this proves


$$
\boxed{
\mathcal R A^{-1}h\equiv0\pmod{p^2}.
}
\tag{4.8}
$$



The terminal reconstruction row is included. Its weight satisfies the retained bound $v_p(W_b)\ge4$.

### What this decides about the old coefficients

After the complete endpoint combination is normal ordered, there are no surviving $\sigma=1$ atoms in this calculation. Consequently, at absolute precision $841$,


$$
\boxed{
a_f=b_f=c_f=0
}
\tag{4.9}
$$


is an explicit valid coefficient assembly for the short-head norm and complete mixed defect.

This is a structural cancellation certificate, not an inference from unevaluated values of $T_1,T_2$.

For an integral complete second column,


$$
\mathcal N\in p^4\mathbb Z_p,\qquad
\mathcal C-p\rho_n\mathcal N\in p^2\mathbb Z_p.
\tag{4.10}
$$


Neither statement reaches the actual exponent $2c+6+\nu$ in (1.2).

---

## 5. The first-order endpoint really is present: an actual bounded solve

The low phase $b\equiv-2\pmod{p^2}$ reduces the first-order crossed rows to two.

For $r\ge2$, the terms with $s<29$ in (4.1) vanish because


$$
s>r>(b+r)_0=r-2.
$$


The $s=29$ term also vanishes, since


$$
\binom{b+r}{29}\equiv0\pmod{29}
\qquad(2\le r\le28).
$$


Therefore


$$
\boxed{t_r=0\pmod p\quad(r\ge2).}
\tag{5.1}
$$



This is an evaluated rank-two first-order return, not an unspecified endpoint matrix.

### 5.1 A phase-compatible auxiliary input

Take


$$
\boxed{
b_{\rm aux}=410910916+3\cdot594823321
=2195380879,
}
$$




$$
\boxed{
n_{\rm aux}=2001b_{\rm aux}=4392957138879,
\qquad h=e_0.
}
\tag{5.2}
$$


Its seventh digit is $3$, compatible with the actual class $u\equiv6\pmod{29}$. It is not an original power.

For the necessary near-terminal coordinates,


$$
v_{b-\ell}=(-1)^{b-\ell},
\qquad1\le\ell\le29,
$$


because the available upper-transform length is below $29$.

The coefficient list (2.3) gives


$$
\sum_{s=1}^{28}C_s=-1,\qquad
\sum_{s=1}^{27}(s+1)C_s=16.
$$


Since $b_{\rm aux}$ is odd and $m_0\equiv7$,


$$
\boxed{(t_0,t_1)=(11,8)\pmod{29}.}
\tag{5.3}
$$



At the two relevant near-terminal coordinates, $F$ has residue $m_0$. The reduced endpoint matrix is therefore


$$
S_{\rm red}
=I_2-pm_0^2I_2
\equiv262I_2\pmod{841}.
$$


Its actual unit inverse is


$$
\boxed{
S_{\rm red}^{-1}\equiv581I_2\pmod{841}.
}
\tag{5.4}
$$



The right side is


$$
-p(t_0,t_1)^T=(522,609)^T\pmod{841},
$$


and the solved crossed charge is


$$
\boxed{q=(522,609)^T\pmod{841}.}
\tag{5.5}
$$



Thus the endpoint charge is nonzero. Its presence is essential to the normal-order identity, even though the complete first-order reconstructed return vanishes.

These are hand-derived finite residues, not reported execution results.

There is no counterexample here to universal first-order cancellation: the universal cancellation is true. The example instead prevents confusing that cancellation with a zero endpoint solve.

---

## 6. The first possible nonzero normalized reconstructed column

The preceding cancellation does **not** mean that the normalized column is zero. The baseline $\sigma=2$ output, discarded modulo $p^2$, must return after division by $p^2$.

### Theorem 6.1 — Leading normalized short-head column

For a head $h$ of length at most $176$,


$$
\boxed{
\mathcal R A^{-1}h
\equiv
\mathcal R\mathsf R_{2n}\mathsf P_-h
\pmod{p^3}.
}
\tag{6.1}
$$



#### Proof

Use the complete normal form (3.3) at $K=3$, so $M=86$.

Every $c_s(n)$, $s>0$, is divisible by $p$:

- for $s<p$, this follows from $p\mid n$;
- for $s\ge p$, it follows from $p\mid s!$.

Also $K_\times\equiv0\pmod p$, so the actual solved exterior vector $z$ is divisible by $p$.

The normal-ordered head atoms have


$$
a\le M+176=262,
$$


and the exterior and reconstruction offsets remain within the range in (4.5). Every reconstructed atom is therefore divisible by $p^2$.

All terms other than $s=0,z=0$ have one additional factor $p$, proving (6.1). ∎

This result identifies the entire first possible normalized column:


$$
\boxed{
\frac{\mathcal R A^{-1}h}{p^2}
\equiv
\frac{\mathcal R\mathsf R_{2n}\mathsf P_-h}{p^2}
\pmod p.
}
\tag{6.2}
$$



The division is by a proved common factor in every reconstructed summand. It is not division of a zero residue modulo $p^2$.

---

## 7. Explicit two-charge, four-atom formula for homogeneous heads

The nilpotent memory theorem now has a useful normalized application.

Let a homogeneous input have initial residues


$$
A=h_0,\qquad B=h_1,\qquad D=B-A
$$


in $\mathbb F_{29}$.

Let


$$
u_r=[z^r]\phi(z)^{-1}\pmod p,
\qquad
L_r=\sum_{q=1}^r\frac{u_{q-1}}q,\qquad L_0=0.
$$


Only $r\le28$ occurs, so all displayed denominators are units.

The homogeneous input modulo $p$ is


$$
\boxed{
h_r=r!(A+DL_r),\quad0\le r\le28,
}
\tag{7.1}
$$




$$
\boxed{
h_{29+r}=-Dr!,\quad0\le r\le28,
}
\tag{7.2}
$$


and vanishes thereafter.

These formulas use the actual rank-one/rank-two nilpotent memory theorem; they do not posit a surviving stable line.

Define the bounded low-digit functions


$$
F_d=\sum_{r=0}^d(-1)^r(d)_{\underline r},
$$




$$
G_d=\sum_{r=0}^d(-1)^r(d)_{\underline r}L_r,
\qquad0\le d\le28.
\tag{7.3}
$$


For example,


$$
F_0=1,\qquad F_d=1-dF_{d-1}.
$$



For $j_0=d,j_1=e$, put


$$
\boxed{
H_0(j)=AF_d+D(G_d+eF_d),\qquad
H_{29}(j)=-DF_d.
}
\tag{7.4}
$$



### Why only two upper parameters remain

In the finite head formula for $\mathsf R_{2n}\mathsf P_-h$, the coefficient


$$
\binom{2n+t-1}{t},\qquad0\le t\le57,
$$


is zero modulo $p$ unless $t=0$ or $t=29$. The two surviving coefficients are


$$
1,\qquad \frac{2n}{29}\equiv14\pmod{29}.
\tag{7.5}
$$



Every omitted coefficient multiplies a reconstructed weighted atom already divisible by $p^2$, so those omissions are valid after the stated normalization.

Define


$$
B_0(j)=\binom{-2n-1}{b-1-j},\qquad
B_{29}(j)=\binom{-2n-30}{b-30-j},
$$


with the original zero convention for negative lower indices.

### Explicit leading column

For $0\le j<b$, the first possible normalized output is


$$
\boxed{
\begin{aligned}
X_{A,D;j}
={}&(-1)^{b-1}\frac{W_j}{p^2}
\Bigl[
jH_0(j-1)\binom{-2n-1}{b-j}
-H_0(j)\binom{-2n-1}{b-1-j}\\
&\qquad\qquad
+14jH_{29}(j-1)\binom{-2n-30}{b-29-j}\\
&\qquad\qquad
-14H_{29}(j)\binom{-2n-30}{b-30-j}
\Bigr]\pmod p .
\end{aligned}
}
\tag{7.6}
$$


At $j=0$, the terms multiplied by $j$ are absent.

For the actual orbit, $(-1)^{b-1}=1$. The displayed form also tracks parity for auxiliary inputs.

The terminal coordinate satisfies


$$
\boxed{X_{A,D;b}=0\pmod p}
\tag{7.7}
$$


by $v_p(W_b)\ge4$. This is a valuation statement about the retained terminal coordinate, not a deletion of it at higher precision.

Equation (7.6) is the full leading normalized column in terms of four explicit weighted atoms. It is substantially smaller than an unevaluated general atom vector.

### Exact limitation

I have not proved that this column is nonzero on the original normalized first-force input, nor that its sum of squares is nonzero modulo $29$.

Accordingly, “first possible nonzero normalized column” is the justified claim. Calling it the first nonzero norm digit would be premature.

---

## 8. Input content must be separated from output content

To avoid silently identifying two different common factors, introduce


$$
g=\min\{v_p(f_0^0),v_p(f_1^0)\}.
$$


The homogeneous recurrence implies that $p^g$ is the common input content of $f^0$.

Write


$$
a_0=p^{-g}f_0^0,\qquad a_1=p^{-g}f_1^0.
$$


At least one of $a_0,a_1$ is a unit.

The normalized homogeneous input


$$
h=p^{-g}f^0
$$


has precision-sized support:


$$
h_j\equiv0\pmod{p^K}\qquad(j\ge58K+2).
\tag{8.1}
$$


Importantly, this bound depends on relative precision $K$, not on $g+K$.

Set


$$
\widehat X=\frac{\mathcal R A^{-1}h}{p^2}.
$$


Then


$$
P=p^g\widehat X.
$$


If


$$
\kappa=\min_jv_p(\widehat X_j),
$$


the retained output content is


$$
\boxed{c=g+\kappa.}
\tag{8.2}
$$



The leading vector $\widehat X\bmod p$ is exactly (7.6), with


$$
A=a_0\bmod p,\qquad D=(a_1-a_0)\bmod p.
$$



### Arbitrary head versus original first force

The unnormalized first force satisfies


$$
f_1^0\equiv f_0^0\pmod p.
$$


That does **not** prove


$$
a_1\equiv a_0\pmod p
$$


after division by an unknown positive $g$.

If the normalized equality does hold, then $D=0$, and the entire $-2n-30$ channel in (7.6) disappears. This is a useful conditional simplification, not an established original-force fact.

The required normalized head invariant is therefore the primitive initial pair


$$
\boxed{(a_0,a_1)\pmod{p^K},}
$$


not merely the unnormalized congruence $f_0^0=f_1^0\pmod p$.

---

## 9. Why the $p^2$ quotient does not evaluate this column

The old $T_1,T_2$ quotient retained only valuation-zero weight terms at absolute precision $p^2$. Formula (7.6) instead divides each weighted $\sigma=2$ atom by $p^2$.

For a normalized Gram summand, let

- $e_W$ be the weight-binomial valuation;
- $e_A,e_{A'}$ be the valuations of the two negative-binomial factors after positive-upper conversion.

Pointwise annihilation gives


$$
e_W+e_A\ge2,\qquad e_W+e_{A'}\ge2.
$$



After division by $p^4$, a summand can contribute to the norm modulo $p$ only when


$$
\boxed{
(e_W,e_A,e_{A'})
=(0,2,2),\ (1,1,1),\ \text{or }(2,0,0).
}
\tag{9.1}
$$



These are three **valuation layers**, not three previously established common tails.

They were all discarded by the old absolute-$p^2$ calculation. Consequently:



$$
\boxed{
\text{The old two-tail quotient does not determine the leading normalized norm.}
}
\tag{9.2}
$$



A precision-uniform two-tail theorem would need actual reduction identities for these divided weighted layers and their higher corrections. Neither the low quotient nor recurrence nilpotence supplies those identities.

---

## 10. A precise normalized whole-force identity

Define the two integral normalized homogeneous output columns


$$
X_a=\frac{\mathcal R A^{-1}h^{(a)}}{p^2},
\qquad a=0,1,
$$


and their Gram matrix


$$
G_{ab}=X_a^TX_b.
\tag{10.1}
$$



Define the integral adjoint output vectors


$$
w_a=A^{-T}\mathcal R^TX_a.
$$


Let $\lambda_{a,\ell}$ be the actual terminal-zero adjoint solution on


$$
1\le\ell\le b-2.
$$



The finite adjoint identity gives the exact complete formula


$$
\boxed{
X_a^TY
=
p^2(r_0G_{a0}+r_1G_{a1})
+\sum_{\ell=1}^{b-2}\mathcal H_\ell\lambda_{a,\ell}
+W_bX_{a,b}.
}
\tag{10.2}
$$



Since the actual $Y=p^3Q$,


$$
\boxed{
p^3X_a^TQ
=
p^2(r_0G_{a0}+r_1G_{a1})
+\sum_{\ell=1}^{b-2}\mathcal H_\ell\lambda_{a,\ell}
+W_bX_{a,b}.
}
\tag{10.3}
$$



The division by $p^3$ belongs to the **whole right side**. Individual initial, source, and endpoint terms must not be divided or omitted separately.

The complete initial values remain


$$
r_i=
\sum_s a_s(n)(n+i)_{\underline s}
\left(
T_{2n+i-s}+\frac{L_{2n+i-s}}{b!}
\right),
\qquad i=0,1,
\tag{10.4}
$$


and all actual source rows remain


$$
\mathcal H_i=
\sum_s a_s(n+1)(n+i)_{\underline s}
\binom{2n+i-s+1}{b},
\qquad1\le i\le b-2.
\tag{10.5}
$$



### What is precision-uniform here

For a requested relative precision, the recurrence inputs and adjoint impulse responses still have the accepted linear-in-precision memory. For example, evaluating $X_a\bmod p^k$ by direct guarded construction requires the homogeneous input modulo $p^{k+2}$, of length at most


$$
58(k+2)+2.
$$



This is a rigorous normalized finite-memory statement for the input and source-response components of (10.3).

It is **not** yet a bounded-memory evaluation of the nonlocal weighted sums. The missing information is now concretely the normalized Gram matrix and the complete adjoint source contractions, rather than three unspecified absolute-$841$ coefficients.

---

## 11. The remaining norm invariant and a useful follow-on lemma

At leading order, calculate


$$
\overline G=
\begin{pmatrix}
X_0^TX_0&X_0^TX_1\\
X_0^TX_1&X_1^TX_1
\end{pmatrix}\pmod p
\tag{11.1}
$$


using the explicit four-atom column (7.6).

This matrix, together with the primitive initial pair, is the next required return invariant.

### Conditional norm bound

If $\overline G$ is anisotropic over $\mathbb F_{29}$, then for every primitive initial pair


$$
\widehat X^T\widehat X\not\equiv0\pmod p.
$$


Consequently,


$$
\boxed{c=g,\qquad \nu=0,\qquad d=2g+4.}
\tag{11.2}
$$



This is a rigorous conditional deduction. The anisotropy hypothesis has not been established.

If $\overline G$ is isotropic or singular, the correct next calculation is the restriction to the actual normalized initial line and its next return digit—not a restart at arbitrary higher absolute precision.

### Why primitivity alone supplies no bound on $\nu$

Since


$$
12^2\equiv-1\pmod{29},
$$


Hensel lifting produces primitive two-coordinate integer vectors whose sum of squares is divisible by arbitrarily high powers of $29$.

Thus neither two initial coordinates nor a primitive output vector gives a general bound on $\nu$. This does not prove large $\nu$ for the actual family; it identifies the precise obstruction to obtaining a bound from dimension alone.

### Concrete next lemma

> **Normalized two-carry Gram and complete-force lemma.**  
> Evaluate the matrix (11.1), or prove its relevant anisotropy/nonvanishing property on the actual power orbit, using (7.6) and the three valuation layers (9.1). Then evaluate the whole combination (10.3), with both complete initial charges and the actual terminal charge, at the resulting norm-relative precision.

This is more specific than requesting another absolute-$29^K$ quotient.

---

## 12. A practical bounded evaluator for the new normalized layer

For a bounded auxiliary input such as (5.2), the leading normalized Gram calculation does not require enumeration of $0\le j<b$.

Expand the four terms in (7.6). Each pair is a finite-prefix binomial sum with a coefficient depending only on the first two digits of $j$.

A digit evaluator can retain:

- the original cutoff borrow for $(b-1)-j$;
- the weight subtraction borrow;
- the two lower-index subtraction borrows;
- the two addition carries for the converted negative binomials;
- the three valuation counts, bounded by $2$;
- the accumulated unit residue modulo $29$.

Accept precisely the layers (9.1), with all terminal support and carry conditions satisfied.

For these leading divided terms, only the first nonzero binomial unit is required. Lucas/Kummer and the leading-unit specialization of Granville suffice; no new automaticity theorem is needed.

A zero visible residue must not erase a hidden unit in a summand-recurrence implementation. In the digit implementation, pruning is justified only after a monotone carry budget has been exceeded.

The auxiliary input (5.2) has fewer than ten relevant base-$29$ digits. Sixteen atom-pair evaluations, with the bounded carry state just described, are a modest calculation. This is not an original $81$-million-digit scan.

### New calculation with fully predicted endpoint outputs

For (5.2), with $K=2,h=e_0$, the expected verifiable output is


$$
(t_0,t_1)=(11,8),\qquad t_r=0\ (r\ge2),
$$




$$
S_{\rm red}=262I_2,\qquad S_{\rm red}^{-1}=581I_2,
$$




$$
q=(522,609)^T\pmod{841},
$$


together with zero discrepancy in (4.3)–(4.4).

This calculation is new and bounded.

### Separate, unevaluated normalized calculation

For the same auxiliary $b,n$, the new two-carry evaluator should report the three entries of $\overline G$, its determinant, and its isotropic lines, if any. Those numerical outputs are **not predicted or claimed here**.

That is an unevaluated specification for the next normalized calculation, not a completed norm certificate and not evidence about an original power.

---

## 13. Exact normalized bottleneck and logarithmic guard

With the retained primitive output $P=p^cx$, the target (1.2) is exactly


$$
\boxed{
x^TQ-p^c\rho_n x^Tx
\equiv0\pmod{p^{c+\nu+1}}.
}
\tag{13.1}
$$



This displays why an absolute $p^2$ cancellation is inadequate: the normalized whole mixed contraction still has to match a term carrying the actual content $c$, with the entire norm loss $\nu$.

The independent $\rho_n$ must continue to come from its original definition. It is not determined from the mixed/norm ratio.

The logarithmic omission condition remains


$$
\boxed{
N_{\log}\ge c+4+\nu,
}
\tag{13.2}
$$


where


$$
N_{\log}
=
2v_p(n!)-v_p(b!)
-\lfloor\log_p(2n+b-1)\rfloor.
$$



Until (13.2) is certified at the true normalized depth, the logarithmic parts of both initial charges in (10.4) remain in the whole contraction.

---

## 14. Final gcd, actual denominator, and whole error

Nothing above changes a row content, either corrected column, or the least actual two-column clearer $d_B$.

Retain


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$


and the all-prime reduction


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
p_n=\frac{H_B}{g_B},\qquad
q_n=\frac{A_B}{g_B}>0.
}
\tag{14.1}
$$



The primitive multiplier remains $d_B^2/g_B$, and the actual denominator remains


$$
\boxed{
\log q_n
=
\sum_\ell
\max\{v_\ell(A_B)-v_\ell(H_B),0\}\log\ell.
}
\tag{14.2}
$$



For


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


the evaluated form is the whole same-index expression


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n.
}
\tag{14.3}
$$



At the retained scope of the signed-error theorem,


$$
\epsilon_n>0\quad\text{eventually},
\qquad
\log|\epsilon_n|
=
-\left(2+\frac1{2001}\right)n\log(1+\sqrt2)+o(n).
$$


A local $29$-adic return theorem would not by itself control the all-prime denominator in (14.2).

---

## Proof-status ledger

| Statement | Status |
|---|---|
| Earlier modulo-$29$ controls | Accepted at their stated finite scope; not requested again |
| New modulo-$841$ prefix/rank controls | Left to the coordinator’s stated implementation |
| Actual first-order divided-power coefficients | Explicitly derived |
| Complete finite-boundary normal ordering | Proved |
| Rank-two first-order endpoint on the actual low phase | Proved |
| Universal complete first-order reconstructed cancellation | Proved in the stated short-head range |
| Absolute-$841$ short-head $T_1,T_2$ coefficients | Structurally zero after complete combination |
| Leading normalized column modulo $29$ | Explicit four-atom formula proved |
| Nonzero original normalized column or norm digit | Not established |
| Equality of input content $g$ and retained output content $c$ | Conditional; not assumed |
| Precision-uniform normalized recurrence-memory statement | Proved, but not a nonlocal scalar evaluator |
| Precision-uniform two-tail closure of the whole normalized contraction | Open |
| Bound on the actual primitive norm loss $\nu$ | Open |
| New auxiliary endpoint residues | Hand-derived; execution not claimed |
| Auxiliary normalized Gram matrix | Unevaluated specification |
| Original normalized whole-force alignment | Open |
| All-prime denominator/whole-error comparison | Open |

## Conclusion

The new structural result is


$$
\boxed{
\text{the complete first-order short-head return cancels after reconstruction.}
}
$$



The cancellation is not explained by deleting the endpoint. The endpoint solve is generally nonzero; its crossed terms are exactly what removes the apparent $\sigma=1$ return in the finite normal ordering.

At the meaningful output normalization, the first possible column is


$$
\boxed{
p^{-2}\mathcal R A^{-1}h
\equiv
p^{-2}\mathcal R\mathsf R_{2n}\mathsf P_-h
\pmod p,
}
$$


and for a homogeneous normalized head it is the explicit four-atom expression (7.6).

The exact remaining local bottleneck is now the **normalized two-carry Gram matrix and the whole complete-force contraction**, evaluated on the primitive initial pair and at the actual loss $c+\nu+1$ in (13.1). The former $p^2$ low quotient does not evaluate that layer.

Even a successful resolution would leave the all-prime final gcd, actual primitive denominator, and whole same-index error to be compared. Therefore


$$
\boxed{
\text{An unconditional proof or disproof of irrationality of }e+\pi
\text{ remains unresolved.}
}
$$


