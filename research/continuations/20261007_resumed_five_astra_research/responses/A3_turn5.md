> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Complete-source prime crossings and the limitation of full-frame primitivity

## Abstract

The rationality or irrationality of $e+\pi$ remains unresolved.

This report gives two new, explicitly checkable results for the **actual complete source**, with logarithmic amplitude exactly $2$.

First, the physical source has an evaluated prime-crossing law. If


$$
n+2<p\le 2n+2,\qquad p\ \text{prime},
$$


and $0\le d\le 2n+2-p$, then


$$
\boxed{\mathcal W_{p+d}\equiv E_d-2\left(\frac{-1}{p}\right)d!\pmod p,}
$$


where


$$
E_0=1,\qquad E_d=dE_{d-1}+1.
$$


In particular,


$$
\mathcal W_p\equiv
\begin{cases}
-1& p\equiv1\pmod4,\\
3& p\equiv3\pmod4.
\end{cases}
$$


Both values are units in the original range. A second-order version is also proved. It identifies the exact fixed-seed quantities governing the first $p$-adic lift: the preceding complete source value, a Wilson quotient, and a half-exponent Fermat quotient. This is an evaluated theorem about the complete forcing, not a generic recurrence-membership assertion.

Second, the physical augmented frame is matched exactly to the archived complete terminal. This permits an all-prime determinantal evaluation of the least simultaneous clearer $D_8$. It also gives a precise obstruction to the proposed use of **all maximal minors of the full augmented frame**:

* their content measures the order of a two-generated lattice quotient;
* $D_8$ measures its exponent;
* endpoint correlation concerns a different, endpoint-restricted frame;
* an endpoint annihilator does not annihilate the omitted moment column.

Thus full-frame primitivity, even if proved, would not by itself bound $\gcd(D_j,C_j)$. At a prime where the moment determinant is a unit, full-frame primitivity is automatic and records no endpoint-correlation depth at all.

The pointwise subfactorial correlation bound, useful moving-prime acquisition, and the same-index nonzero primitive whole-error estimate remain open.

---

## 1. Scope and reused mathematics

The approximation domain is unchanged:


$$
\boxed{n=15^r\quad\text{or}\quad n=105^r,\qquad r\ge2.}
$$


Every such $n$ is odd and $n\ge225$. Throughout,


$$
m=n+1,\qquad N=n+2,\qquad K=2n+2.
$$



Auxiliary coefficient indices and recurrence indices below do not enlarge this domain.

We reuse the following supplied results at their stated scope:

1. the finite producer and its physical terminal $K$;
2. the actual primitive endpoint rows;
3. the companion with seeds $\rho_0=0,\rho_1=1$;
4. the complete terminal decomposition;
5. the polynomial intersection payment
   

$$
\kappa_3b_{c,3}\mid4m^2N^2,\qquad
   \kappa_0b_{c,0}\mid4m^2N^2(n+3);
$$


6. the paid contact identity
   

$$
\gcd(|T_{\rm aff}|,D_j)_{>N}
   =\gcd(|C_j|,D_j)_{>N};
$$


7. the turn-4 temporal repulsion theorem;
8. the closed universal rational-gauge obstruction.

The companion and polynomial payment are not new results here. Neither the companion nor producer $3375$ is recomputed.

The contact construction is used only where its retained hypotheses hold:


$$
\det T\ne0,\qquad F\ne0,\qquad \widehat R_j\ne0
$$


for the endpoint under consideration. No new nonvanishing theorem for those contacts is asserted.

The supplied proofs of the archived polynomial intersection theorem rely on the archived moment-primitivity theorem. That dependence remains explicit; a full-frame determinant argument is not substituted for it.

---

## 2. The actual physical source

Put


$$
q(z)=1-z+\frac{z^2}{2},\qquad q_j=[z^j]q(z)^n.
$$


The complete source is


$$
\alpha_0=\alpha_1=1,\qquad
\alpha_s=\alpha_{s-1}-\frac12\alpha_{s-2},
$$




$$
\eta_s=\sum_{r=0}^s\frac1{r!}
       +2\sum_{r=1}^s\frac{\alpha_{r-1}}r,
\qquad
\mathcal W_s=s!\eta_s.
$$


Its physical terminal vector remains


$$
\boxed{
w_i=
\sum_{j=0}^{\min(2n,n+i)}
q_j(n+i)^{\underline j}\mathcal W_{2n+i-j},
\qquad 0\le i\le2,
}
\tag{2.1}
$$


with


$$
\widehat w_i=\frac{w_i}{(n+i)!}.
$$



The largest source index in (2.1) is exactly $K=2n+2$.

The source satisfies the elementary but important recurrence


$$
\boxed{
\mathcal W_s=s\mathcal W_{s-1}
 +1+2(s-1)!\alpha_{s-1}\qquad(s\ge1).
}
\tag{2.2}
$$


Indeed, multiply


$$
\eta_s-\eta_{s-1}=\frac1{s!}+\frac{2\alpha_{s-1}}s
$$


by $s!$.

The coefficient $2$ in (2.2) is the actual logarithmic amplitude. It will be used essentially.

All congruences involving these rational source values are interpreted in $\mathbb Z_{(p)}$. Their only possible denominator primes come from powers of $2$, so this causes no difficulty for the odd primes used below.

---

## 3. A new evaluated theorem: complete-source prime crossings

### 3.1 Evaluation of the logarithmic coefficient at a prime

Let $p$ be odd and put


$$
\chi_p=\left(\frac{-1}{p}\right),\qquad
\varepsilon_p=\left(\frac2p\right).
$$



The recurrence for $\alpha_s$ has characteristic roots


$$
r_\pm=\frac{1\pm i}{2}.
$$


Thus


$$
\alpha_s=\frac{r_+^{s+1}-r_-^{s+1}}{r_+-r_-}.
$$


In particular, for odd $p$,


$$
\boxed{
\alpha_{p-1}
=\chi_p\varepsilon_p\,2^{-(p-1)/2}.
}
\tag{3.1}
$$



This can also be checked without adjoining $i$: the recurrence gives the repeating sign pattern


$$
\alpha_0=1,\quad \alpha_2=\frac12,\quad
\alpha_4=-\frac14,\quad \alpha_6=-\frac18,
$$


and the same pattern continues after multiplication by $1/16$.

Euler's criterion applied to $2$ now gives


$$
\boxed{\alpha_{p-1}\equiv\chi_p\pmod p.}
\tag{3.2}
$$



### Theorem 3.1 — The actual complete prime-crossing law

For every original $n$, every prime


$$
N<p\le K,
$$


and every integer $d$ with


$$
0\le d\le K-p,
$$


one has


$$
\boxed{
\mathcal W_{p+d}\equiv E_d-2\chi_p d!\pmod p,
}
\tag{3.3}
$$


where


$$
E_0=1,\qquad E_d=dE_{d-1}+1.
$$



#### Proof

At $s=p$, equation (2.2), Wilson's theorem and (3.2) give


$$
\mathcal W_p
\equiv1+2(p-1)!\alpha_{p-1}
\equiv1-2\chi_p\pmod p.
\tag{3.4}
$$



Because $p>N=n+2$,


$$
K=2n+2<2p.
$$


Consequently, for $1\le d\le K-p$, the factorial


$$
(p+d-1)!
$$


is divisible by $p$. Equation (2.2) reduces to


$$
\mathcal W_{p+d}\equiv d\mathcal W_{p+d-1}+1\pmod p.
$$


The sequence


$$
E_d-2\chi_p d!
$$


has this recurrence and the initial value $1-2\chi_p$. This proves (3.3). ∎

### Corollary 3.2 — The crossing seed is a unit

In the original range,


$$
\boxed{
\mathcal W_p\equiv
\begin{cases}
-1& p\equiv1\pmod4,\\
3& p\equiv3\pmod4,
\end{cases}
\pmod p.
}
\tag{3.5}
$$


Since $p>N\ge227$, neither value vanishes.

This statement uses the actual amplitude $2$. It is not a claim about a variable-amplitude family.

### What the theorem does not say

It does **not** imply that any $\widehat w_i$, complete contact $C_j$, or augmented-frame minor is a unit. The convolution in (2.1) can cancel unit source contributions.

It does show why a proof must retain the complete physical forcing. Although the divisions by $(n+i)!$ are units at $p>N$, the source indices reach $K$, and their passage through $p$ creates the nonzero correction in (3.3).

---

## 4. The first deep lift is also explicit

The first-level formula is insufficient for a depth bound. The terms discarded modulo $p$ reappear modulo $p^2$. We now evaluate them.

Define the integer quotients


$$
\mathfrak w_p=\frac{(p-1)!+1}{p},
\qquad
\mathfrak h_p=
\frac{2^{(p-1)/2}-\varepsilon_p}{p}.
\tag{4.1}
$$


The first is a Wilson quotient. The second is an integer by Euler's criterion.

Set


$$
B_d=E_d-2\chi_p d!,
\qquad
R_d=\frac{\mathcal W_{p+d}-B_d}{p}\in\mathbb Z_{(p)}.
$$



### Theorem 4.1 — Evaluated fixed-seed lifting recurrence

For $N<p\le K$, the residue of $R_0$ is


$$
\boxed{
R_0\equiv
\mathcal W_{p-1}
+2\chi_p\bigl(\mathfrak w_p+\varepsilon_p\mathfrak h_p\bigr)
\pmod p.
}
\tag{4.2}
$$


For $1\le d\le K-p$,


$$
\boxed{
R_d\equiv
dR_{d-1}+B_{d-1}-2(d-1)!\,a_d
\pmod p,
}
\tag{4.3}
$$


where the coefficient $a_d$ is evaluated by


$$
\boxed{
a_d=
\begin{cases}
\alpha_d & \chi_p=1,\\[2mm]
\dfrac12\alpha_{d-2} & \chi_p=-1,
\end{cases}
\quad\text{in }\mathbb F_p,
}
\tag{4.4}
$$


with $\alpha_{-1}=0$.

#### Proof

Write


$$
\alpha_{p-1}=\chi_p+p\lambda_p.
$$


Using (3.1) and


$$
2^{(p-1)/2}=\varepsilon_p+p\mathfrak h_p,
$$


we obtain


$$
\lambda_p\equiv-\chi_p\varepsilon_p\mathfrak h_p\pmod p.
$$


Also,


$$
(p-1)!=-1+p\mathfrak w_p.
$$


Substitution in the exact equation


$$
\mathcal W_p=p\mathcal W_{p-1}+1
             +2(p-1)!\alpha_{p-1}
$$


gives (4.2).

For $d\ge1$, substitute


$$
\mathcal W_{p+d-1}=B_{d-1}+pR_{d-1}
$$


into (2.2). Since $B_d=dB_{d-1}+1$,


$$
R_d\equiv dR_{d-1}+B_{d-1}
       +2\frac{(p+d-1)!}{p}\alpha_{p+d-1}\pmod p.
$$


Wilson's theorem gives


$$
\frac{(p+d-1)!}{p}\equiv-(d-1)!\pmod p.
$$



It remains to evaluate $\alpha_{p+d-1}$. If $\chi_p=1$, Frobenius fixes $r_+$ and $r_-$, giving


$$
\alpha_{p+d-1}\equiv\alpha_d.
$$


If $\chi_p=-1$, Frobenius interchanges the roots, giving


$$
\alpha_{p+d-1}
\equiv
\frac{r_-r_+^d-r_+r_-^d}{r_+-r_-}
=\frac12\alpha_{d-2}.
$$


This proves (4.3)–(4.4). ∎

### Arithmetic significance

Equations (4.2)–(4.4) are a finite recurrence with a completely specified actual seed. They are more informative than the assertion that a complete response satisfies some recurrence.

They also expose a genuine limitation:

> First-level unit information does not control deep lifting. Already at the next level, the lift depends on the actual preceding complete source value and on two explicit prime quotients.

No estimate for their aggregate endpoint cancellations is proved here.

---

## 5. Matching the physical frame to the archived complete terminal

We next connect the finite source to the proposed augmented moment frame.

Let


$$
c_k=[z^k]e^zq(z)^n,\qquad
T=
\begin{pmatrix}
c_n&c_{n-1}&c_{n-2}\\
c_{n+1}&c_n&c_{n-1}\\
c_{n+2}&c_{n+1}&c_n
\end{pmatrix},
$$


and put


$$
J=N!T,\qquad H=N!t,
$$


where


$$
t=
\begin{pmatrix}
\tau_n\\
(\tau_n+\tau_{n+1})/2\\
\tau_{n+2}/2
\end{pmatrix}.
$$


Write $J_0,J_1,J_2$ for the columns of $J$.

The archived complete terminal is


$$
\mathbf C=S_cv'+T_cw'+C e_2,
\tag{5.1}
$$


where


$$
v'=(2N,N,m)^T,\qquad
w'=(0,N,2n+3)^T,\qquad C=mZ,
$$




$$
S_c=\frac m2 b_n+2n!m!\rho_n,
\qquad
T_c=b_{n+1}-\frac m2b_n+2n!m!\rho_{n+1}.
\tag{5.2}
$$


This is precisely the previously recovered companion normalization.

Let


$$
E_n=n!\sum_{r=0}^n\frac1{r!}.
$$



### Proposition 5.1 — Exact physical-to-complete column identity

At every original index,


$$
\boxed{
N!\widehat w=J_0+E_nH+\mathbf C.
}
\tag{5.3}
$$



#### Derivation

The ordinary generating series of the partial sums $\eta_s$ is


$$
\sum_{s\ge0}\eta_s z^s
=
\frac{e^z+2\int_0^z q(t)^{-1}\,dt}{1-z}.
$$


Therefore


$$
\widehat w_i
=[z^{n+i}]
q(z)^n\frac{d^n}{dz^n}
\left(
\frac{e^z+2\int_0^zq(t)^{-1}\,dt}{1-z}
\right).
\tag{5.4}
$$


Indeed, expanding the derivative gives exactly the finite sum (2.1).

For the exponential part,


$$
q(z)^n\frac{d^n}{dz^n}\frac{e^z}{1-z}
=
\frac{q(z)^n}{(1-z)^{n+1}}e^z
n!\sum_{r=0}^n\frac{(1-z)^r}{r!}.
$$


The archived response generating identity consequently splits this as


$$
B_n(z)+e^zq(z)^n
+E_n\frac{q(z)^n}{(1-z)^{n+1}}.
$$


At the three retained terminal coefficients, these give respectively

* the archived exponential terminal $\mathbf B/N!$;
* $J_0/N!$;
* $E_nH/N!$.

The archived three-row logarithmic terminal identity, with amplitude exactly $2$, supplies $\mathbf Q/N!$. Since $\mathbf C=\mathbf B+\mathbf Q$, equation (5.3) follows.

Only the retained three-row logarithmic identity is used. No recurrence for that logarithmic column at earlier coefficient indices is inferred, and no finite inverse is extended past $K$. ∎

---

## 6. The two fully corrected columns

Define the integral $4\times3$ matrix


$$
B_\partial=
\begin{pmatrix}
-1&n&-nm\\
1&-n-1&nm+2n\\
0&1&-2n-1\\
0&0&1
\end{pmatrix}.
\tag{6.1}
$$


It is the matrix sending $x$ to the corrected column $u$.

The last three rows of $B_\partial$ form an upper-triangular unimodular matrix. Hence $B_\partial$ has an integral left inverse.

Put


$$
A_{\rm src}=n!H,\qquad
B_{\rm src}=\mathbf C+E_nH.
\tag{6.2}
$$


Equation (5.3) gives


$$
x=J^{-1}A_{\rm src},\qquad
y=e_0+J^{-1}B_{\rm src}.
$$


Consequently,


$$
\boxed{
u=B_\partial J^{-1}A_{\rm src},
\qquad
v=e_1+B_\partial J^{-1}B_{\rm src},
}
\tag{6.3}
$$


where now


$$
e_1=(0,1,0,0)^T.
$$



This is the exact transformed location of the exterior correction. It has not been discarded: the original exterior $+1$ at row $0$, combined with $B_\partial e_0$, becomes the integral $e_1$ in (6.3).

At $p>N$, $n!$ is a unit, and the column operation


$$
v\longmapsto v-\frac{E_n}{n!}u
$$


is integral over $\mathbb Z_p$. It gives


$$
v-\frac{E_n}{n!}u
=e_1+B_\partial J^{-1}\mathbf C.
\tag{6.4}
$$


This local shear is legitimate. It is not used as a globally integral shear.

---

## 7. A new all-prime determinant theorem for $D_8$

Assume $\det J\ne0$, and write


$$
\Delta=\det J,\qquad Q=|\Delta|.
$$



Consider the actual integral augmented frame


$$
\mathcal A=[J_0,J_1,J_2,A_{\rm src},B_{\rm src}].
\tag{7.1}
$$



Define:

* $d_{\rm one}$: the gcd of $\Delta$ and the six determinants obtained by replacing **one** column of $J$ by $A_{\rm src}$ or $B_{\rm src}$;
* $d_{\rm all}$: the gcd of all ten maximal minors of $\mathcal A$.

Both are positive all-prime contents.

### Theorem 7.1 — One-replacement content, full-frame content, and actual clearer

For the two actual complete corrected columns,


$$
\boxed{D_8=\frac{Q}{d_{\rm one}}.}
\tag{7.2}
$$


Moreover,


$$
\boxed{
d_{\rm all}\mid d_{\rm one}\mid Q,
\qquad
d_{\rm one}^{\,2}\mid Qd_{\rm all}.
}
\tag{7.3}
$$



The finite lattice quotient


$$
\frac{J\mathbb Z^3+\mathbb ZA_{\rm src}
                  +\mathbb ZB_{\rm src}}
     {J\mathbb Z^3}
\tag{7.4}
$$


has invariant factors


$$
\boxed{
\frac{d_{\rm one}}{d_{\rm all}},
\qquad
\frac{Q}{d_{\rm one}},
}
\tag{7.5}
$$


allowing an invariant factor equal to $1$.

#### Proof of the clearer formula

Set


$$
a=\operatorname{adj}(J)A_{\rm src},
\qquad
b=\operatorname{adj}(J)B_{\rm src}.
$$


The six coordinates of $a,b$, up to signs, are the six one-replacement determinants.

By (6.3), the eight integer numerators over the common denominator $\Delta$ are


$$
U=B_\partial a,\qquad
V=\Delta e_1+B_\partial b.
\tag{7.6}
$$


Because $B_\partial$ has an integral left inverse,


$$
\gcd(Q,U_0,\ldots,U_3,V_0,\ldots,V_3)
=\gcd(Q,a_0,a_1,a_2,b_0,b_1,b_2)
=d_{\rm one}.
$$


The least simultaneous clearer is therefore $Q/d_{\rm one}$.

This proves (7.2) for the **actual eight entries**, including their exterior correction.

#### Proof of the divisibilities

The first two divisibilities in (7.3) follow from the definitions.

For the last one, use the adjugate determinant identity


$$
\Delta\,\det(J_i,A_{\rm src},B_{\rm src})
=
\pm\det
\begin{pmatrix}
a_r&b_r\\
a_s&b_s
\end{pmatrix},
\tag{7.7}
$$


where $\{r,s\}$ is the complementary pair to $i$, with the appropriate orientation.

Every coordinate of $a,b$ is divisible by $d_{\rm one}$. Thus


$$
d_{\rm one}^2
\mid
\Delta\,\det(J_i,A_{\rm src},B_{\rm src}).
$$


It also divides $\Delta$ times every one-replacement minor and $\Delta^2$. Taking the gcd of these products proves


$$
d_{\rm one}^2\mid Qd_{\rm all}.
$$



#### Proof of the invariant factors

The numerator lattice in (7.4) has index $d_{\rm all}$ in $\mathbb Z^3$, while $J\mathbb Z^3$ has index $Q$. Thus the quotient has order $Q/d_{\rm all}$.

It is generated by two elements. Its exponent is exactly the least simultaneous denominator of


$$
J^{-1}A_{\rm src},\quad J^{-1}B_{\rm src},
$$


which is $D_8$. Hence its two invariant factors are its exponent $Q/d_{\rm one}$ and the order divided by that exponent, namely $d_{\rm one}/d_{\rm all}$. ∎

### Consequence for the proposed primitivity argument

At a prime $p>N$, the full frame is locally column-equivalent to


$$
[J,H,\mathbf C].
$$


If its maximal minors are primitive at $p$, then $v_p(d_{\rm all})=0$. Theorem 7.1 gives


$$
\boxed{
\left\lceil\frac{v_p(\Delta)}2\right\rceil
\le v_p(D_8)\le v_p(\Delta).
}
\tag{7.8}
$$



Thus full-frame primitivity does not directly make the common clearer small. At a singular moment prime, it forces at least half of the determinant depth into that clearer.

This does not determine the primitive endpoint denominators, because their actual row contents can still cancel factors. Those contents must be retained separately.

---

## 8. Actual row contents are also recovered exactly

Let $U,V$ be the integer numerator columns in (7.6), and put


$$
g_j^{\rm num}=\gcd(|U_j|,|V_j|).
$$


Then


$$
\boxed{
g_j^{(8)}=\frac{g_j^{\rm num}}{d_{\rm one}},
}
\tag{8.1}
$$


and, with the sign coming from $\Delta$,


$$
\boxed{
\widetilde u_j=
\operatorname{sgn}(\Delta)\frac{U_j}{g_j^{\rm num}},
\qquad
\widetilde v_j=
\operatorname{sgn}(\Delta)\frac{V_j}{g_j^{\rm num}}.
}
\tag{8.2}
$$



For a nonzero endpoint,


$$
\boxed{
|\widetilde u_j|
=\frac{|U_j|}{\gcd(|U_j|,|V_j|)}.
}
\tag{8.3}
$$



These are all-prime formulas. Neither $d_{\rm all}$ nor $D_j$ is substituted for an actual row content.

---

## 9. Evaluation of the extra three maximal minors

The distinction between $d_{\rm one}$ and $d_{\rm all}$ is not merely formal: their difference is exactly the addition of the three minors


$$
\det(J_i,A_{\rm src},B_{\rm src}),\qquad i=0,1,2.
$$


For the actual complete source, these admit an explicit evaluation.

Retain the moment coordinates $X,Y,Z$, and define


$$
R=mZ+(n-1)(X-Y).
$$


Set


$$
\begin{aligned}
W^{(0)}&=(X,Z,f_0)^T,\\
W^{(1)}&=(Y,2X-Y,f_1)^T,\\
W^{(2)}&=(R,2Y-R,f_2)^T,
\end{aligned}
$$


where the archived terminal identities give


$$
\begin{aligned}
f_0&=Y-X-(2n+1)Z,\\
f_1&=NY-(3n+4)X+NZ,\\
f_2&=mNX-m(n+4)Y+mNZ.
\end{aligned}
\tag{9.1}
$$


A direct coordinate calculation gives


$$
J_i=\frac12VW^{(i)},\qquad
H=\frac{m!}{2}V(\tau_n,\tau_{n+1},0)^T.
\tag{9.2}
$$



The actual complete determinant is


$$
\Omega_n=\tau_nT_c-\tau_{n+1}S_c.
$$


By the reused companion identity, at the original odd indices,


$$
\boxed{\Omega_n=\mathcal K_n-2(n!)^2.}
\tag{9.3}
$$



Since the $E_nH$ term cancels in a determinant containing $H$,


$$
\det(J_i,A_{\rm src},B_{\rm src})
=n!\det(J_i,H,\mathbf C).
$$


Using $\det V=2N^2$, equations (9.2)–(9.3) yield


$$
\boxed{
\begin{aligned}
\det(J_i,A_{\rm src},B_{\rm src})
=\frac{n!m!N^2}{2}\Big[
&C\bigl(\tau_{n+1}W^{(i)}_1-\tau_nW^{(i)}_2\bigr)\\
&+\bigl(\mathcal K_n-2(n!)^2\bigr)f_i
\Big].
\end{aligned}
}
\tag{9.4}
$$



This evaluation retains:

* the actual complete amplitude $2$;
* the actual transverse seed through $\mathcal K_n$;
* the full factorial term;
* all three original moment columns.

Equation (9.4), together with the Plücker identity (7.7), is an algebraic certificate for exactly what the additional maximal minors do. It does not assert that their gcd is small.

---

## 10. The precise endpoint-rank obstruction

The endpoint rows annihilate only two moment combinations:


$$
\begin{array}{c|c|c}
j&\text{annihilated columns}&\text{omitted column}\\ \hline
3&J_0,\ J_1&J_2\\
0&nJ_0+J_1,\ -nmJ_0+J_2&J_0.
\end{array}
\tag{10.1}
$$



Let these two kernel columns be $K_{j,1},K_{j,2}$, and define their actual content


$$
h_j^K=
\gcd\bigl(\text{coordinates of }K_{j,1}\times K_{j,2}\bigr).
$$


Up to the retained sign normalization,


$$
K_{j,1}\times K_{j,2}=h_j^K r_j.
$$


Thus


$$
\boxed{
r_jJ_{\rm omit}=\pm\frac{\Delta}{h_j^K}.
}
\tag{10.2}
$$



The original endpoint kernel lattice has index $h_j^K$ in its saturation


$$
\ker(r_j:\mathbb Z^3\to\mathbb Z).
$$


This saturation is therefore a paid operation, not a free unit assumption.

Choose an integral basis of the saturated kernel. In the corresponding unimodular row coordinates, the gcd of the maximal minors of the **endpoint-restricted** saturated frame is


$$
\gcd(|r_jH|,|r_j\mathbf C|).
\tag{10.3}
$$


After adjoining the omitted moment column, it becomes


$$
\boxed{
\gcd\left(
|r_jH|,\ |C_j|,\ \left|\frac{\Delta}{h_j^K}\right|
\right).
}
\tag{10.4}
$$



For the unsaturated frame, the maximal-minor content lies between the saturated content and $h_j^K$ times that content, by divisibility. Thus the kernel-content payment remains explicit.

At $p>N$,


$$
r_jH=\frac{m!}{2L}\widehat R_j,
$$


and the multiplier is a unit. Consequently, the endpoint frame records


$$
\min\{v_p(\widehat R_j),v_p(C_j)\},
$$


whereas the full saturated frame records only


$$
\boxed{
\min\left\{
v_p(\widehat R_j),v_p(C_j),
v_p\!\left(\frac{\Delta}{h_j^K}\right)
\right\}.
}
\tag{10.5}
$$



The paid target remains


$$
\boxed{
v_p\gcd(D_j,C_j)
=
\min\{(v_p(\widehat R_j)-v_p(F))_+,v_p(C_j)\}.
}
\tag{10.6}
$$



### What has been refuted—and what has not

The attempted implication

> “the same endpoint annihilates the reference and complete terminal, so the full augmented frame loses rank”

is missing the condition


$$
r_jJ_{\rm omit}\equiv0.
$$


Equation (10.2) identifies that missing condition exactly.

In particular, if $p\nmid\Delta$, then $p\nmid h_j^K$, the omitted-column projection is a unit, and the full frame has rank $3$, regardless of the endpoint-restricted rank.

This is a checkable obstruction to that **rank argument**. It is not a numerical counterexample to a conjectural bound on the actual $\gcd(D_j,C_j)$, and it does not prove or disprove full augmented-frame primitivity.

---

## 11. A distinct next mechanism: source-crossing lifts in the endpoint frame

The new prime-crossing formulas suggest a different mechanism from full-frame primitivity.

For $N<p\le K$, split the physical convolution (2.1) according to whether


$$
2n+i-j<p
\quad\text{or}\quad
2n+i-j\ge p.
$$


On the latter range, Theorems 3.1 and 4.1 replace the long complete source by:

1. the evaluated first-level sequence $E_d-2\chi_pd!$;
2. the evaluated lifting recurrence (4.3);
3. the fixed seed (4.2).

The correct rank object is then the endpoint-restricted frame


$$
[K_{j,1},K_{j,2},H,\mathbf C],
$$


with its actual kernel-content payment $h_j^K$.

### Concrete follow-on lemma

A useful next lemma would establish an **inhomogeneous prime-power transfer for this endpoint-restricted frame**, with the following explicit requirements:

* its source input is (2.2), not a homogeneous surrogate;
* at the physical crossing $s=p$, its initial correction is exactly (4.2);
* every later source term $2(s-1)!\alpha_{s-1}$ is retained at the appropriate $p$-adic depth;
* the endpoint kernel saturation costs exactly $h_j^K$;
* the original paid contact removes exactly $v_p(F)$, as in (10.6);
* the transfer yields a quantitative restriction on the depth of **isolated** endpoint rank drops.

This is a source-sensitive exterior-recurrence problem, not a reopening of the universal rational gauge.

Two limitations are immediate:

* the present formulas supply only the first two $p$-adic levels;
* primes $p>K$ do not cross the physical source and require a separate argument.

A subfactorial contact theorem still has to control all surviving primes and all depths on an infinite original subsequence.

---

## 12. Acquisition direction and retained losses

Turn 4 proves


$$
\sum_{k=n}^{t-1}\min\{a_k(p),a_{k+1}(p)\}\le3
\qquad(p>t+2),
$$


but leaves isolated entrances uncontrolled. Nothing here changes that conclusion.

For an original block $t=bn$, $b\in\{15,105\}$, retain


$$
\boxed{
\mathcal I_t=
\frac{\mathcal I_n c^{\min}_{n,t}}
{\mathcal M_{n,t}\mathcal L_{n,t}},
}
\tag{12.1}
$$


where


$$
\mathcal M_{n,t}
=
\prod_{n+2<p\le t+2}
p^{\min(v_p(F_n),v_p(M_n))}
$$


and


$$
\mathcal L_{n,t}
=
\prod_{p>t+2}p^{(a_n(p)-a_t(p))_+}.
$$



The source-crossing band $N<p\le K$ is not the same object as this block's medium-prime loss.

Taking logarithms in (12.1),


$$
\log\mathcal I_t
=
\log\mathcal I_n+\log c^{\min}_{n,t}
-\log\mathcal M_{n,t}-\log\mathcal L_{n,t}.
$$


Therefore, if useful inventory must grow, the required acquisition estimate is a **lower bound** for $\log c^{\min}_{n,t}$, sufficient to pay both losses and the remaining budget.

By contrast, a small endpoint-resonance factor requires an **upper bound** for a loss such as


$$
\log\operatorname{lcm}_{j=0,3}\gcd(D_j,C_j)_{>N}.
$$



These directions cannot be interchanged. Neither the new source unit nor full-frame primitivity provides the necessary lower bound for useful acquisition.

---

## 13. Preservation of the final approximation

The physical returns remain


$$
N_0=\det T+R_0^{\rm raw}\widehat w,
\qquad
N_3=R_3^{\rm raw}\widehat w.
$$


The coefficient $1$ of the terminal force $\mathfrak f_K$ in $b_{K+1}$ remains present. No inverse is extended beyond $K$.

The actual least clearer and contents are


$$
D_8=\operatorname{lcm}_{0\le j\le3}
\bigl(\operatorname{den}(u_j),\operatorname{den}(v_j)\bigr),
$$




$$
g_j^{(8)}=\gcd(|D_8u_j|,|D_8v_j|),
$$




$$
\widetilde u_j=D_8u_j/g_j^{(8)},\qquad
\widetilde v_j=D_8v_j/g_j^{(8)}.
$$


Theorem 7.1 evaluates $D_8$ without replacing these contents.

For nonzero endpoints, put


$$
h_{\rm end}=\gcd(|\widetilde u_0|,|\widetilde u_3|),
$$




$$
\widetilde u_0=h_{\rm end}A_{\rm wt},\qquad
\widetilde u_3=h_{\rm end}B_{\rm wt}.
$$


For a reduced weight $\lambda=a/k_{\rm wt}$, $k_{\rm wt}>0$, retain


$$
J_{\rm wt}
=B_{\rm wt}\widetilde v_0-A_{\rm wt}\widetilde v_3,
$$




$$
T_{\rm wt}
=aJ_{\rm wt}+k_{\rm wt}A_{\rm wt}\widetilde v_3,
$$




$$
F_{\rm gcd}
=
\gcd(|A_{\rm wt}|,|a|)
\gcd(|B_{\rm wt}|,|a-k_{\rm wt}|),
$$




$$
G_{\rm wt}=\gcd(k_{\rm wt},|J_{\rm wt}|),
$$




$$
H_{\rm gcd}
=
\gcd\!\left(
h_{\rm end},
\frac{|T_{\rm wt}|}{F_{\rm gcd}G_{\rm wt}}
\right).
$$


The actual primitive fraction is


$$
\boxed{
q_\lambda=
\frac{k_{\rm wt}h_{\rm end}|A_{\rm wt}B_{\rm wt}|}
{F_{\rm gcd}G_{\rm wt}H_{\rm gcd}},
}
$$




$$
\boxed{
p_\lambda=
\operatorname{sgn}(A_{\rm wt}B_{\rm wt})
\frac{T_{\rm wt}}
{F_{\rm gcd}G_{\rm wt}H_{\rm gcd}}.
}
$$



Every gcd here is all-prime.

The required error is the **whole** evaluated expression


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda\left[
(e+\pi)
-\lambda\frac{\widetilde v_0}{\widetilde u_0}
-(1-\lambda)\frac{\widetilde v_3}{\widetilde u_3}
\right].
}
\tag{13.1}
$$


Equivalently, in the retained notation,


$$
q_\lambda(e+\pi)-p_\lambda
=q_\lambda e_3\alpha_{n,2}(\lambda-\Lambda_{n,2}).
$$



An irrationality proof still requires


$$
\boxed{
0<|q_\lambda(e+\pi)-p_\lambda|\longrightarrow0
}
\tag{13.2}
$$


on the **same infinite original indices** carrying the arithmetic estimates. No result proved here supplies (13.2).

---

## 14. A bounded exact calculation deciding a new finite object

No computation has been executed.

The following calculation is directed at the new determinantal distinction, not at a random-prime audit. It does not request producer $3375$ or another companion calculation.

### Inputs

Use the single original index


$$
\boxed{n=225,\quad N=227,\quad K=452.}
$$



The mathematical inputs are:

* $q(z)^{225}$, only through degree $452$;
* the five moment coefficients defining $J$;
* the reference recurrence through index $227$;
* the source recurrence (2.2) through index $452$;
* the finite physical formula (2.1).

If these entries already exist in retained data, reuse them.

Form


$$
H=227!\,t,\qquad
\mathbf C=227!\widehat w-J_0-E_{225}H,
$$


and then the actual integral frame


$$
[J,\ 225!H,\ \mathbf C+E_{225}H].
$$



### Expected verifiable outputs

The calculation should return:

1. $\Delta$, the seven minors defining $d_{\rm one}$, and the additional three minors defining $d_{\rm all}$;
2. the exact integers
   

$$
d_{\rm one},\quad d_{\rm all},\quad
   d_{\rm one}/d_{\rm all},\quad |\Delta|/d_{\rm one};
$$


3. zero residuals in the three adjugate identities (7.7);
4. the eight numerators $U_j,V_j$, and verification of
   

$$
D_8=|\Delta|/d_{\rm one},\qquad
   g_j^{(8)}=\gcd(|U_j|,|V_j|)/d_{\rm one};
$$


5. the two actual kernel contents $h_j^K$, the omitted-column projections, and verification of (10.2);
6. the large-prime parts, obtained by removing primes at most $227$, of
   

$$
d_{\rm one}/d_{\rm all}
$$


   and of the discrepancy between the saturated endpoint content (10.3) and full-frame content (10.4).

A discrepancy equal to $1$ must be reported as such. It would mean only that this particular finite index does not exhibit that discrepancy.

As a separate, tightly bounded source check, use


$$
\boxed{p=229}
$$


and verify (3.3) and (4.2)–(4.3) for


$$
0\le d\le223
$$


modulo $229^2$. Here $\chi_{229}=1$, so the first-level prediction is explicitly


$$
\mathcal W_{229+d}\equiv E_d-2d!\pmod{229}.
$$



No unrestricted factorization is needed. Exact gcds, fixed-size determinants, and removal of primes at most $227$ suffice for the listed all-prime and large-prime contents.

This calculation establishes only its single-index finite scope.

---

## 15. Proof status and conclusion

| Statement | Status |
|---|---|
| Companion, complete-contact overlap, polynomial payment | Reused at supplied scope |
| Universal rational gauge obstruction | Closed; not reopened |
| Complete-source prime-crossing formula (3.3) | **New, proved** |
| Unit crossing seed for amplitude exactly $2$ | **New, proved** |
| Explicit first lifting recurrence (4.2)–(4.4) | **New, proved** |
| Exact physical frame matching | Proved using retained three-row terminal identities |
| All-prime formula $D_8=|\Delta|/d_{\rm one}$ | **Proved for the actual corrected columns** |
| Relative invariant factors and quadratic divisibility | **Proved** |
| Full-frame rank inference from endpoint annihilation | **Obstructed by the explicit omitted-column projection** |
| Full augmented-frame primitivity | Not proved or disproved |
| Polynomial or subfactorial $\gcd(D_j,C_j)$ bound | Open |
| Fixed-seed isolated-entrance bound | Open |
| Useful acquisition lower bound with both losses paid | Open |
| Same-index nonzero whole-error decay | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

The principal new arithmetic information is


$$
\boxed{
\mathcal W_{p+d}\equiv E_d-2\left(\frac{-1}{p}\right)d!\pmod p,
}
$$


together with its explicit $p^2$-lifting seed and recurrence. It evaluates an actual part of the complete physical response that must be retained at primes above $n+2$.

The principal complete-frame conclusion is equally precise:

> All maximal minors of the full augmented frame are not the determinantal ideal governing either the exact least clearer or the endpoint correlation. The missing information is explicitly measured by one-replacement minors, actual kernel saturation contents, and the omitted moment-column projection.

The exact remaining arithmetic bottleneck is control of the **depth and aggregate prime weight of fixed-seed endpoint-restricted rank drops**, including isolated entrances and primes beyond the physical source crossing. Any such control must still be transported through the original losses, actual row contents, the final all-prime weight gcd, and the nonzero whole error at the same infinite original indices.

If $e+\pi=a/d$ were rational, every nonzero integer linear form $q(e+\pi)-p$ would have absolute value at least $1/d$. Therefore (13.2) would prove irrationality. The present theorems do not establish that final chain.



$$
\boxed{\text{No unconditional rationality or irrationality proof for }e+\pi\text{ is obtained.}}
$$


