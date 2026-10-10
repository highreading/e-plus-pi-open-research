> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, Turn 7 — A genuine high-shift obstruction and a force-weighted replacement for kernel content

## Executive conclusions

The complete residual estimate


$$
N-2S(C,D)\in 2^{2\mu+4}\mathbb Z_2
\tag{0.1}
$$


is **not proved or disproved** by the supplied material. There is, however, a concrete obstruction to extending the six-floor-case argument by asserting a uniformly bounded loss for each restored moment.

The main new result is an explicit example within the **actual original family**, with the actual moment index and an original coordinate:

> At $j=0$, the restored moment $s=380$ has an unbounded negative valuation relative to the old higher kernel. More precisely, on original indices for which
> 

$$
> \ell=v_2(k+3)\ge4,\qquad k=2C+1,
>
$$


> one has
> 

$$
> \boxed{
> v_2\!\left(\frac{\mathcal M_{380}(0)}{\mathcal B_0}\right)=2-\ell.
> }
> \tag{0.2}
>
$$


> Such original indices exist with arbitrarily large $\ell$. Moreover, the exact Newton moment multiplier
> 

$$
> a_{380}(2n)=\binom{2n+379}{380}
>
$$


> is odd on these indices.

Thus a fixed moment shift can have arbitrarily large common-kernel loss, and the mandatory multiplier $a_{380}(2n)$ does **not** absorb it. A bound depending only on the numerical size of the shift is false, even on the original exponential family.

This is **not** a counterexample to (0.1): the actual coefficient multiplying this moment has not been determined at the required depth. It is a rigorous counterexample to an intermediate integrality assertion that an all-depth proof might otherwise use.

There are also two positive advances.

1. The supplied whole logarithmic-force estimate is strong enough to remove that force at the varying target precision $2\mu+4$, after a new explicit comparison with an elementary upper bound for $\mu$. This is not an extrapolation of its old fixed-precision omission.
2. A force-weighted moment content, rather than the content of $\mathcal B_t$ alone, gives a division-safe formulation of the complete norm and mixed contraction. Its exact formulas below retain all original coordinates, the shortened terminal block, and the exterior $+1$. What remains missing is a bound for this content and the resulting complete scalar residual.

No tools, external endpoints, or files have been accessed. No computation is reported as executed.

---

## 1. Source audit and unchanged domain

Throughout,


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0,
$$




$$
b=128D+81,\qquad n=128C+66,\qquad C=4002D+2532,
$$


and


$$
k=2C+1=8004D+5065.
$$



The contact inverse has its original finite range


$$
0\le i,j<b.
$$


The scalar coordinates have range


$$
0\le j\le b.
$$


The block decomposition is exactly


$$
0\le t<D,\quad 0\le\rho<128,
$$


followed by


$$
t=D,\quad 0\le\rho\le80,
$$


with the exterior coordinate $j=b=128D+81$ separate.

Retain


$$
X=\frac{Z_w}{2R},\qquad
Y=\frac{V_w}{4b!},\qquad
N=X^TX>0,\qquad H=X^TY\ne0.
$$



The accepted higher kernel and its content are


$$
\mathcal B_t=\binom Ct\binom{k+D-t-1}{D-t},
\qquad
\mu=\min_{0\le t\le D}v_2(\mathcal B_t).
$$



Turn 6 establishes, at its stated scope,


$$
N=2S(C,D)+256R_u,\qquad R_u\in\mathbb Z_2,
\tag{1.1}
$$


and proves the exact model theorem for $S$. I do not re-prove that theorem.

### 1.1 What is and is not supplied at all depths

The packet supplies an exact arbitrary-monomial contact operator and exact finite suffix identities. Those can be reused beyond the previously computed degrees.

It does **not** display a complete all-depth normalized central-force formula. The local-force certificate explicitly refers to equations in prior turn 20 and to truncation arguments in resumed turn 1, neither of which is reproduced here as a complete all-depth formula. Its coefficient lists are residues modulo $256$, not definitions of the full force.

Consequently, it would be unjustified to assign the missing Newton coefficients by lifting the displayed integer representatives.

The withdrawn separate-period-$512$ assertion in turn 3 is not used. The safe-period correction and the later accepted finite certificates are retained only at their stated precision.

---

## 2. General floor shifts: the exact quotient beyond six cases

Let


$$
j=128t+\rho,\qquad d=D-t,\qquad K=k+d.
$$


For any integer moment index $s$, the actual moment is


$$
\mathcal M_s(j)
=
\binom{128K+84-\rho}{128d+80-\rho-s},
\tag{2.1}
$$


provided the lower argument is between zero and the upper argument; otherwise it is zero.

Define


$$
a_0=\left\lfloor\frac{84-\rho}{128}\right\rfloor,\qquad
l_0=\left\lfloor\frac{80-\rho-s}{128}\right\rfloor,\qquad
c_0=\left\lfloor\frac{4+s}{128}\right\rfloor,
$$


and the corresponding remainders $a,l,c\in\{0,\ldots,127\}$.

Unlike in the old truncated calculation, $l_0,c_0$ are now unrestricted integers subject to validity of the factorial arguments.

Seven-level factorial stripping gives the exact identity


$$
\mathcal M_s(j)
=
2^{m_{\rho s}}u_{\rho s}
\frac{(K+a_0)!}{(d+l_0)!(k+c_0)!},
\tag{2.2}
$$


where


$$
m_{\rho s}
=
127(a_0-l_0-c_0)
+v_2(a!)-v_2(l!)-v_2(c!)
$$


and $u_{\rho s}$ is the exact odd factorial-unit quotient. This formula is used only when all actual factorial arguments are nonnegative.

Relative to


$$
J_d=\binom{k+d-1}{d},
$$


the high quotient is therefore


$$
\boxed{
\frac{\mathcal M_s(j)}{J_d}
=
2^{m_{\rho s}}u_{\rho s}
\frac{(K+a_0)!\,d!\,(k-1)!}
     {(d+l_0)!\,(k+c_0)!\,(K-1)!}.
}
\tag{2.3}
$$



Equation (2.3) is the all-shift replacement for the six-case table. It is an exact rational identity, **not** an integrality assertion.

The possible denominator factors $k+1,k+2,\ldots$ are precisely where the old division-safe basis can fail.

---

## 3. A fixed restored moment has unbounded common-kernel loss

### Theorem 1 — Actual-family loss at $s=380,\ j=0$

Suppose an original index satisfies


$$
\ell=v_2(k+3)\ge4.
$$


Then


$$
\boxed{
v_2\!\left(\frac{\mathcal M_{380}(0)}{\mathcal B_0}\right)=2-\ell.
}
\tag{3.1}
$$


Furthermore,


$$
\boxed{v_2\!\left(\binom{2n+379}{380}\right)=0.}
\tag{3.2}
$$



#### Proof

At $j=0$, one has $t=\rho=0$, $d=D$, $K=k+D$, and


$$
\mathcal B_0=J_D.
$$


For $s=380$,


$$
80-s=-300=128(-3)+84,\qquad 4+s=384=128\cdot3.
$$


Thus


$$
a_0=0,\quad l_0=-3,\quad c_0=3,\qquad
a=l=84,\quad c=0.
$$


The low power of two in (2.2) is zero. Hence


$$
\mathcal M_{380}(0)
=
u\binom{k+D}{D-3},
\qquad u\in\mathbb Z_2^\times.
$$


All these lower arguments are valid on the original family.

The exact ratio is


$$
\frac{\binom{k+D}{D-3}}{\binom{k+D-1}{D}}
=
\frac{(k+D)D(D-1)(D-2)}
{k(k+1)(k+2)(k+3)}.
\tag{3.3}
$$



Now


$$
k+3=4(2001D+1267).
$$


The hypothesis $\ell\ge4$ implies


$$
D\equiv1\pmod4.
$$


More precisely,


$$
2001(D-1)=(2001D+1267)-3268.
$$


Since $v_2(3268)=2$ and $v_2(2001D+1267)=\ell-2$, we obtain:

- if $\ell>4$, $v_2(D-1)=2$;
- if $\ell=4$, the valuation of $D-1$ need not equal $2$.

Accordingly, first take $\ell\ge5$. Then


$$
v_2(D)=v_2(D-2)=0,\qquad v_2(D-1)=2.
$$


Also $D\equiv5\pmod8$, while $k\equiv-3\pmod8$, so


$$
v_2(k+D)=1.
$$


Finally,


$$
v_2(k)=v_2(k+2)=0,\qquad v_2(k+1)=1.
$$


Taking valuations in (3.3) gives


$$
1+0+2+0-(0+1+0+\ell)=2-\ell.
$$



Thus (3.1) holds for $\ell\ge5$. For the threshold $\ell=4$, the universally valid formula is instead


$$
v_2\!\left(\frac{\mathcal M_{380}(0)}{\mathcal B_0}\right)
=
v_2(k+D)+v_2(D-1)-1-\ell.
\tag{3.4}
$$


The claimed uniform version of the theorem therefore requires $\ell\ge5$, and that is the version used below.

For the multiplier, put


$$
A=2n=128k+4.
$$


Then


$$
\binom{A+379}{380}
=\frac{\prod_{r=0}^{379}(A+r)}{380!}.
$$


Since


$$
A=-380+128(k+3),
$$


and $\ell\ge5$, the difference between $A+r$ and $-380+r$ has valuation at least $12$. Every nonzero integer in $\{-380,\ldots,-1\}$ has valuation at most $8$. Therefore


$$
v_2(A+r)=v_2(380-r)
$$


for every $0\le r\le379$. The numerator and denominator have equal valuation, proving (3.2). ∎

**Corrected theorem statement.** The exact unbounded-loss conclusion is


$$
\boxed{
\ell=v_2(k+3)\ge5
\quad\Longrightarrow\quad
v_2\!\left(
\frac{a_{380}(2n)\mathcal M_{380}(0)}{\mathcal B_0}
\right)=2-\ell.
}
\tag{3.5}
$$



The threshold correction above is included explicitly rather than suppressing a boundary case in the valuation argument.

### 3.1 Why this is a relevant moment, not a formal shifted kernel

For an exact Newton coefficient $p_r$, the finite suffix reconstruction gives


$$
F_s(x;A)
=
\binom{A+s-1}{s}
\sum_{r\ge s}p_r\binom{x}{r-s}.
$$


At $x=0$,


$$
F_s(0;A)=a_s(A)p_s.
$$


The reconstruction terms multiplied by $x$ vanish there. Thus the $s=380$ term in the first raw column at $j=0$, if present, is exactly


$$
p_{380}\,a_{380}(A)\,\mathcal M_{380}(0).
\tag{3.6}
$$



There is no extra factor of $W_0$, since $W_0=1$, and no reconstruction factor $j$ to absorb the loss.

For this term to be divisible by $2^\mu$ merely because $\mathcal B_0$ is, its coefficient must compensate for the loss. Its exact valuation is


$$
v_2(p_{380})+v_2(\mathcal B_0)+2-\ell.
\tag{3.7}
$$



The current packet does not determine $v_2(p_{380})$ on these original indices.

---

## 4. Arbitrarily long losses occur on the original exponential family

The preceding theorem does not rely on a freely chosen odd $D$.

### Lemma 2 — Original reachability at every binary precision

For distinct nonnegative integers $u,v$,


$$
\boxed{v_2(D_u-D_v)=1+v_2(u-v).}
\tag{4.1}
$$



#### Proof

For $u>v$,


$$
D_u-D_v
=
9^{18+32v}\frac{9^{32(u-v)}-1}{128}.
$$


The elementary lifting-the-exponent identity gives


$$
v_2(9^{32(u-v)}-1)=8+v_2(u-v).
$$


Subtracting $v_2(128)=7$ proves (4.1). ∎

Consequently, for every $q\ge1$, the values


$$
D_u\bmod2^q,\qquad 0\le u<2^{q-1},
$$


are all the odd residues, each exactly once.

Because $2001$ is odd,


$$
2001D+1267\equiv0\pmod{2^m}
$$


has a unique odd solution modulo $2^m$. Choosing one further binary digit yields original indices with


$$
v_2(2001D_u+1267)=m
$$


exactly. Hence


$$
v_2(k_u+3)=m+2
$$


is arbitrarily large.

Combining this with (3.5) proves:



$$
\boxed{
\inf_{u\ge0}
v_2\!\left(
\frac{a_{380}(2n_u)\mathcal M_{380}(0)}
{\mathcal B_0(C_u,D_u)}
\right)=-\infty.
}
\tag{4.2}
$$



### What has been disproved

There is no finite constant $L_{380}$ such that


$$
a_{380}(2n_u)\mathcal M_{380}(0)
\in2^{-L_{380}}\mathcal B_0\mathbb Z_2
$$


for every original $u$.

In particular, no loss bound depending only on the fixed shift size $380$ can justify this common-kernel reduction.

### What has not been disproved

Equation (4.2) does not show that the actual complete force has a nonzero coefficient of insufficient depth. It also does not exclude cancellation among different restored moments or after squaring and summing.

It therefore does **not** disprove


$$
N-2S\in2^{2\mu+4}\mathbb Z_2.
$$



The missing hypothesis is now concrete: control of the actual coefficient $p_{380}$, or a cancellation identity that avoids estimating (3.6) separately, on the reachable branch $k+3\to0$ in $\mathbb Z_2$.

---

## 5. The logarithmic force can be bounded at the varying target

The logarithmic force need not remain an unspecified possible obstruction at this particular target.

Let


$$
L=\operatorname{bitlength}(2C+D).
$$


Taking $t=0$ in the kernel minimum and using the carry interpretation of
$\binom{2C+D}{D}$ gives the elementary bound


$$
\boxed{\mu\le L.}
\tag{5.1}
$$


Indeed, the number of binary carries in the addition $2C+D$ is at most the number of digit positions.

Set


$$
T=2\mu+4,\qquad p=T+3.
\tag{5.2}
$$


Then


$$
p\le2L+7.
$$



The retained whole logarithmic-force estimate is


$$
v_2(h_i^F/b!)
\ge
2000b+2-2\lfloor\log_2(8005b-1)\rfloor.
\tag{5.3}
$$


Since


$$
2C+D=\frac{8005b-213}{128},
$$


the right side of (5.3) exceeds $2L+7$ throughout the original domain. The left side grows linearly in $b$, whereas the displayed logarithmic bounds are already dominated for $b\ge81$, and the actual first $b$ is much larger.

Thus


$$
\boxed{h_i^F/b!\in2^p\mathbb Z_2}
\tag{5.4}
$$


uniformly in the original finite index $i$.

The retained contact inverse and Pascal reconstruction are integral at their raw-column interfaces. Therefore this whole-force divisibility is preserved through those operations. The final division by $4$ in $Y$ loses at most two bits.

This proves that the whole logarithmic force is negligible for the norm/mixed calculations modulo $2^T$ at the target (5.2).

**Important distinction:** this argument estimates the complete force in the original integral operator before any division by $\mathcal B_t$. It is unaffected by the negative normalized valuation in (4.2).

---

## 6. A valid growing factorial cutoff

For


$$
f_a=\frac{(b+a)!}{b!}=\prod_{r=1}^{a}(b+r),
$$


the original $b$ is odd. Among the first $2p$ factors there are exactly $p$ even integers. Therefore


$$
v_2(f_{2p})\ge p,
$$


and monotonicity yields


$$
\boxed{f_a\in2^p\mathbb Z_2\qquad(a\ge2p).}
\tag{6.1}
$$



Accordingly, a safe complete factorial-tail calculation at raw precision $p$ retains


$$
0\le a<2p.
\tag{6.2}
$$



This is deliberately a safe cutoff, not a claim of minimality. It replaces the fixed nine-entry truncation by a bound that grows with the required precision.

Again, the omission is justified **before** common-kernel normalization. A term known to vanish under the complete integral operator does not need to be rescued after division by $\mathcal B_t$.

The actual exterior data at this precision must be recomputed from these complete factorial inputs. The old nine entries cannot be reused as all-depth representatives.

---

## 7. Complete finite contact inversion: what can be written unconditionally

The exact contact symbol in the supplied convention is


$$
\phi^n=(1+2U)^h,\qquad h=n/2,
$$


where $U$ is the integral divided-power polynomial of degree four.

Let


$$
\lambda_s(n)=[x^{[s]}]\bigl((1+2U)^h-1\bigr).
$$


Then


$$
\lambda_s(n)
=
\sum_{r=1}^{h}2^r\binom hr[x^{[s]}]U^r.
\tag{7.1}
$$


All $\lambda_s$ are even integers.

Using the accepted exact monomial transport, define the **actual finite** contact correction


$$
K_{n,b}=\sum_s\lambda_s(n)C_s^{II},
\qquad 0\le i,j<b.
\tag{7.2}
$$


At raw precision $p$, only $r<p$ in (7.1) can survive, so only


$$
s\le4(p-1)
$$


need be retained in the contact symbol.

Because $K_{n,b}$ is even,


$$
\boxed{
(I+K_{n,b})^{-1}
\equiv
\sum_{r=0}^{p-1}(-K_{n,b})^r\pmod{2^p}.
}
\tag{7.3}
$$



This is a complete finite inverse at the chosen precision, with no change of matrix endpoints.

But (7.3) still needs the complete input forces. It does not manufacture their unknown higher coefficients from the modulus-$256$ receipt.

---

## 8. Corrected content-relative operator

A common higher kernel can always be used over $\mathbb Q_2$. The issue is which normalization makes the resulting operator integral.

For a complete first raw interior reconstruction at precision $p$, write


$$
2X_j\equiv
(-1)^{j+1}\sum_s A_{j,s}\pmod{2^p},
\qquad
A_{j,s}=W_jU_s(j;2n)\mathcal M_s(j).
\tag{8.1}
$$


Similarly, for the complete raw defect,


$$
4(Y_j-X_j)\equiv
(-1)^{j+1}\sum_s B_{j,s}\pmod{2^p},
\tag{8.2}
$$


where $B_{j,s}$ includes all retained polynomial and exterior moments.

The moment ranges here are the ranges obtained from the complete precision-$p$ force and inverse—not the old ranges $[-1,15]$ and $[-10,15]$.

For $j=128t+\rho<b$, define


$$
\mathcal L^X_{j,s}
=\frac{A_{j,s}}{\mathcal B_t},
\qquad
\mathcal L^E_{j,s}
=\frac{B_{j,s}}{\mathcal B_t}.
\tag{8.3}
$$


Equation (2.3), together with the exact weight stripping, computes these rational coefficients without suppressing any high-shift denominator.

### 8.1 Force-weighted term content

Define


$$
c_X(p)=
\min\left\{
v_2(A_{j,s}),\ v_2(2X_b^{(p)})
\right\},
\tag{8.4}
$$


and


$$
c_E(p)=
\min\left\{
v_2(B_{j,s}),\ v_2(4(Y_b-X_b)^{(p)})
\right\},
\tag{8.5}
$$


where zero terms are ignored and the endpoint representatives are computed from the complete precision-$p$ data.

Equivalently, the interior part of (8.4) is


$$
\min_{j,s}\left\{
v_2(\mathcal B_t)+v_2(\mathcal L^X_{j,s})
\right\}.
\tag{8.6}
$$



These are **force-weighted term contents**. They are not asserted to equal coordinate content: addition of moments can increase coordinate divisibility.

By definition,


$$
2^{-c_X(p)}A_{j,s},\qquad
2^{-c_E(p)}B_{j,s}
$$


are integral. This gives an integral normalized moment operator even when the individual losses relative to $\mathcal B_t$ are unbounded.

Unlike normalization by $2^\mu$, this replacement cannot silently erase the denominator in (3.3).

### 8.2 Complete norm and mixed contraction

Let


$$
F_j^{(p)}=\sum_s A_{j,s},\qquad
G_j^{(p)}=\sum_s B_{j,s}.
$$


Include separately


$$
F_b^{(p)}=W_b\,b\theta_{b-1}^{(p)},
\tag{8.7}
$$




$$
G_b^{(p)}
=
W_b\bigl(1+b\eta_{b-1}^{(p)}-2b\theta_{b-1}^{(p)}\bigr).
\tag{8.8}
$$


The exterior $+1$ is explicit.

The complete contractions are


$$
\boxed{
4N\equiv
\sum_{t=0}^{D-1}\sum_{\rho=0}^{127}
\bigl(F_{128t+\rho}^{(p)}\bigr)^2
+
\sum_{\rho=0}^{80}
\bigl(F_{128D+\rho}^{(p)}\bigr)^2
+
\bigl(F_b^{(p)}\bigr)^2
\pmod{2^p},
}
\tag{8.9}
$$


and


$$
\boxed{
8(H-N)\equiv
\sum_{t=0}^{D-1}\sum_{\rho=0}^{127}
F_{128t+\rho}^{(p)}G_{128t+\rho}^{(p)}
+
\sum_{\rho=0}^{80}
F_{128D+\rho}^{(p)}G_{128D+\rho}^{(p)}
+
F_b^{(p)}G_b^{(p)}
\pmod{2^p}.
}
\tag{8.10}
$$



With $p=T+3$, these determine both scalars modulo $2^T$. Division is applied only to the complete raw contractions.

These formulas are a corrected all-precision framework. They are **not** an evaluated residual theorem. In particular, no inequality relating $c_X(p),c_E(p)$ to $\mu$ is claimed without the complete force coefficients.

---

## 9. The concrete follow-on lemma

The shift example isolates a testable obligation more precise than “restore the tail.”

### Force–shift compensation lemma

For the complete precision-$p$ forces and every retained moment, prove a bound for


$$
v_2\!\left(W_jU_s(j;2n)\mathcal M_s(j)\right)
\tag{9.1}
$$


and its defect analogue that includes the exact negative part of the high quotient (2.3).

On the specific branch of Theorem 1, this must in particular control


$$
v_2(p_{380}(u))
+
v_2(\mathcal B_0(u))
+2-v_2(k_u+3).
\tag{9.2}
$$



There are two mathematically distinct ways forward:

1. **Coefficient compensation:** prove that the actual complete coefficient gains the needed $k+3$-adic depth.
2. **Grouped compensation:** combine moments before normalization and prove a cancellation identity for that group, including its exact finite boundary.

The second option may be necessary. The first is not supplied merely by a fixed absolute lower bound on $v_2(p_{380})$.

Even successful compensation would establish only a content bound. To prove (0.1), one must then evaluate


$$
\frac14\sum_{j=0}^{b}\bigl(F_j^{(p)}\bigr)^2-2S(C,D)
\pmod{2^{2\mu+4}}
\tag{9.3}
$$


with every complete term present. Mixed cancellation requires the parallel evaluation of (8.10).

---

## 10. Bounded exact arithmetic worth doing next

I do **not** request the minimum-multiplicity parity computation being added by the coordinator.

The following different calculation audits the new shift obstruction and its original-family reachability. It requires neither a growing matrix nor large factorials.

### Inputs

For each


$$
\ell=5,6,\ldots,12,
$$


use


$$
D_u=\frac{9^{18+32u}-81}{128},
\qquad
k_u=8004D_u+5065,
$$


and seek the unique original residue class with


$$
v_2(k_u+3)=\ell.
$$



This can be done by binary lifting of $u$, using (4.1). Only modular exponentiation is needed. To determine $D_u\bmod2^q$, compute $9^{18+32u}\bmod2^{q+7}$ before subtracting $81$ and dividing by $128$.

### Expected verifiable output

For each $\ell$, output:

1. A nonnegative residue representative $u_\ell$.
2. The residues of $D_{u_\ell}$ and $k_{u_\ell}$ sufficient to certify
   

$$
v_2(k_{u_\ell}+3)=\ell.
$$


3. The valuation tuple
   

$$
\bigl(
   v_2(k+D),v_2(D),v_2(D-1),v_2(D-2),
   v_2(k),v_2(k+1),v_2(k+2),v_2(k+3)
   \bigr)
$$


   with expected value
   

$$
\boxed{(1,0,2,0,\ 0,1,0,\ell).}
$$


4. The resulting exact relative valuation
   

$$
\boxed{2-\ell.}
$$


5. The parity certificate
   

$$
\boxed{\binom{2n+379}{380}\equiv1\pmod2,}
$$


   verified from the 380 numerator-factor valuations, or from Lucas’s theorem.

This finite calculation would independently certify eight instances of the proved mechanism. It would not determine the actual $p_{380}$, the complete residual, or any irrationality conclusion.

A subsequent **force** calculation should not begin from the old residue vector. Its necessary input is the missing exact normalized central-force formula, followed by (7.1)–(7.3) at the chosen precision and the cutoff (6.2). Its expected output is the complete coefficient vector and a coefficient-valued finite-inverse residual, not an extrapolation of degree $15$.

---

## 11. Full gcd, actual primitive denominator, and whole error

No primitive normalization changes.

With the least actual clearer $d_B$, set


$$
N_B=d_B[u,v],
$$




$$
A_B=N_{B,1}^{T}\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^{T}\Omega N_{B,2},
$$




$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=\frac{A_B}{g_B}>0,\qquad
p_n=\frac{H_B}{g_B}.
}
\tag{11.1}
$$


This is the full integer gcd, including every odd prime. The primitive multiplier remains


$$
d_B^2/g_B.
$$



Writing


$$
\alpha=v_2(N),\qquad \gamma=v_2(H),
$$


the accepted interface remains


$$
v_2(q_n)=
\max\left\{
0,\frac{3n}{2}-v_2(b!)-s_2(n)-1-(\gamma-\alpha)
\right\}.
\tag{11.2}
$$


The shift theorem assigns neither $\alpha$ nor $\gamma-\alpha$.

The retained whole signed error is


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi)<0
\quad\text{eventually},
$$




$$
\log|\epsilon_n|
=
-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$


Thus the whole evaluated form is


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n>0
}
\quad\text{eventually}.
\tag{11.3}
$$



A same-index upper bound for the **full** primitive denominator, sufficient to make (11.3) tend to zero, remains necessary for an irrationality argument by these approximants. A dyadic content theorem alone is not that bound.

---

## 12. Final ledger

### New rigorous results

1. **All-shift quotient:** equation (2.3) replaces the six-case table without asserting false integrality.
2. **Actual-family counterexample to bounded common-kernel loss:** the fixed moment $s=380$ at $j=0$ satisfies
   

$$
v_2\!\left(
   a_{380}(2n)\mathcal M_{380}(0)/\mathcal B_0
   \right)=2-v_2(k+3)
$$


   whenever $v_2(k+3)\ge5$, and these depths are unbounded on original indices.
3. **Growing-target logarithmic cutoff:** the supplied whole logarithmic-force estimate exceeds the raw precision required by $2\mu+4$, using $\mu\le\operatorname{bitlength}(2C+D)$.
4. **Growing factorial cutoff:** $a<2p$ is a safe complete exterior factorial range at raw precision $p$.
5. **Corrected normalization:** force-weighted term content gives an integral moment operator and complete norm/mixed contraction formulas, with the shortened terminal block and exterior $+1$ retained.

### Not proved

The actual force coefficient at the dangerous shift has not been evaluated, and grouped cancellation has not been established. Therefore neither


$$
N-2S\in2^{2\mu+4}\mathbb Z_2
$$


nor its negation is proved.

### Exact remaining bottleneck

The immediate bottleneck is the **complete force–shift interaction**, exemplified by (9.2): determine whether actual coefficient depth or actual grouped cancellation compensates for arbitrarily long high-binomial denominator chains.

After that remain the complete scalar residual, the mixed contraction, the full odd-prime gcd, and the same-index primitive-denominator/whole-error comparison.



$$
\boxed{\text{The irrationality of }e+\pi\text{ remains unresolved.}}
$$


