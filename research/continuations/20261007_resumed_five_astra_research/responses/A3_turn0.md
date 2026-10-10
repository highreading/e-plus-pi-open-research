> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3, resumed research report — Global scalar charts, exact contact-index restrictions, and the remaining seeded resonance problem

## Executive summary

The irrationality of $e+\pi$ remains unresolved.

This report proves three arithmetic statements relevant to the two assigned bottlenecks.

1. **The actual-seed scalar reduction is valid throughout every multiplicative block.** In fact,
   

$$
F_s\ne0\qquad(s\ge2),
$$


   including the even auxiliary indices. Moreover, the off-diagonal numerator
   

$$
\mathcal T_s:=2(2s+3)P_s+3F_s
$$


   is nonzero for every $s\ge2$. Thus the two-dimensional reduction and second-order scalar recurrence of Turn 15 require no pivot changes on these blocks.

   This removes an unresolved chart hypothesis. It does **not** make the displayed divisors $p$-adic units or bound their large-prime content.

2. **The last three prefix coefficients of the actual transverse Green functional are jointly primitive at every $p>N$.** This remains true after the two final moment-source terms have been fixed. Consequently, there is no automatic large-prime divisibility gain from the Green kernel itself. Any resonance restriction must use the actual fixed-seed values of the source coefficients, rather than triangularity or common kernel content.

3. **The common saturated factor admits an exact contact-index formula.** Under the retained large-prime primitivity of the actual contact coordinates,
   

$$
\boxed{
   \gcd(\mathfrak S_0,\mathfrak S_3)
   =
   \gcd(\mathfrak S_0,C_{\rm sat})
   =
   \gcd(\mathfrak S_3,C_{\rm sat}).
   }
$$


   Equivalently,
   

$$
\boxed{
   \mathfrak S_0\mathfrak S_3
   =
   J_{\rm res}\,
   \gcd\!\left(|T_{\rm aff}|,D_0,C_{\rm sat}\right).
   }
$$


   This sharpens the divisibility in Turn 15 to an equality for the shared factor. It does not estimate that factor.

A sharp local countermodel shows that even a **unit contact index**, full-state primitivity, and the complete affine identities permit arbitrarily deep **exclusive** resonance. Thus the contact cross product alone cannot bound $J_{\rm res}$.

Neither


$$
\log c^{\min}_{n,bn}=o(n\log n)
$$


nor a subfactorial estimate for the actual $J_{\rm res}$ is proved. All final all-prime denominators and whole errors remain unchanged.

---

## 1. Scope, source audit, and notation

The approximation domain remains exactly


$$
\boxed{n=15^r\quad\text{or}\quad n=105^r,\qquad r\ge2.}
$$


For a multiplicative block, $t=bn$, with $b=15$ or $105$.

Consecutive indices $s$ below are auxiliary recurrence indices only. In particular, at such indices I use


$$
\overline M_s=Q_s\tau_s-P_s\tau_{s+1}.
$$


The normalization


$$
M_s=L_s\overline M_s,\qquad L_s=2^{(s+1)/2},
$$


is invoked in the original integer normalization only at the original odd indices. This avoids treating $L_s$ as a rational scale at even auxiliary indices. At the odd primes under consideration, the endpoint valuations agree.

I reuse the following closed results at their stated scope:

- the actual transfer $z_{s+1}=\mathsf U_sz_s$, its inverse and determinant;
- the seed $z_2=(0,10,-66)^T$;
- reference-pair and full-state large-prime primitivity;
- the evaluated backward remainder and its actual-unit property;
- the actual-seed reduction and its exterior-content theorem;
- the finite Green formula, both final-source identities, and exact seed subtraction;
- the full saturation theorem and the paid contact-coordinate content;
- the all-prime endpoint and weighted primitive normalizations.

The supplied twelve-identity receipt supports its stated algebraic checks. It does not certify a cofactor-growth theorem, a joint-gcd estimate, a least primitive denominator, or an infinite nonzero whole-error bound. None of those is inferred here.

I found no discrepancy in those certified identities needed for the arguments below. Two limitations matter:

* Turn 15 correctly did **not** establish nonvanishing at all auxiliary chart pivots. Section 2 supplies that missing proof.
* The $3375$ scalar receipt explicitly says that the canonical smooth part is **not** a multiple of $(n!)^3$. A universal factorial-cubed absorption claim for that smooth part would therefore be false at that original index. The receipt says nothing about an eventual infinite-family replacement.

The accepted $3375$ and $11025$ computations are not repeated or extended.

The supplied literature descriptions are also retained at their stated scope. Rowland–Yassawi provide prime-power automatic congruence machinery and, in the later work, complexity bounds for algebraic series and diagonals. Those results do not evaluate this complete finite response or bound its moving-large-prime gcd. Paule–Schneider provide creative-telescoping machinery, not the missing paid boundary-and-gcd certificate here. No theorem for constant-coefficient recurrence gcds is being applied to this polynomial-coefficient recurrence.

---

## 2. Global nonvanishing of the actual scalar charts

Write the moment parameter explicitly:


$$
a_k(s)=k![z^k]e^zq(z)^s,\qquad
q(z)=1-z+\frac{z^2}{2}.
$$


The moments are integers: factorial-normalized series with integral coefficients form a ring, and both $e^z$ and $q(z)$ belong to it.

Recall


$$
P_s=s(s+1)\bigl(a_s(s)+a_{s-1}(s)\bigr)
$$


and


$$
F_s=2(s+1)\bigl(Y_s-2X_s-(s-1)Z_s\bigr).
$$



### Theorem 2.1 — Every actual $F$-chart is nonzero

For every auxiliary integer $s\ge2$,


$$
F_s\ne0.
$$


More precisely,


$$
\boxed{v_2(F_s)=1\qquad\text{when \(s\) is even}.}
$$



#### Proof

First suppose $s$ is even. Put


$$
q(z)^{s/2}=\sum_{j\ge0}u_j\frac{z^j}{j!},
\qquad u_j\in\mathbb Z,\quad u_0=1.
$$


For $k>0$, the factorial-normalized coefficient of its square is


$$
\sum_{j=0}^k\binom{k}{j}u_ju_{k-j}.
$$


Terms with $j\ne k-j$ occur in equal pairs. If $k=2j>0$, the remaining middle coefficient is even because


$$
\binom{2j}{j}=2\binom{2j-1}{j-1}.
$$


Consequently,


$$
q(z)^s\equiv1\pmod2
$$


in the ring of factorial-normalized integral series. Multiplying by $e^z$, whose factorial-normalized coefficients are all $1$, gives


$$
\boxed{a_k(s)\equiv1\pmod2\qquad(k\ge0,\ s\ \text{even}).}
$$



For even $s$, $s+1$ is odd. Hence $X_s$ and $Z_s$ are odd, while $Y_s$ is even. Therefore


$$
Y_s-2X_s-(s-1)Z_s
$$


is odd. This proves $v_2(F_s)=1$.

For odd $s\ge3$, the retained moment argument applies unchanged:


$$
F_s\equiv-2\pmod s.
$$


Since $s$ is odd, this excludes $F_s=0$. These cases cover all $s\ge2$. ∎

### Theorem 2.2 — Every scalar off-diagonal pivot is nonzero

Define


$$
\mathcal T_s=2(2s+3)P_s+3F_s.
$$


Then


$$
\boxed{\mathcal T_s\ne0\qquad(s\ge2).}
$$



#### Proof

For even $s$, the parity result above gives


$$
P_s=s(s+1)\bigl(a_s(s)+a_{s-1}(s)\bigr),
$$


so


$$
v_2(P_s)\ge v_2(s)+1\ge2.
$$


Thus


$$
v_2\!\left(2(2s+3)P_s\right)\ge3,
\qquad
v_2(3F_s)=1.
$$


The two summands cannot cancel, and in fact


$$
v_2(\mathcal T_s)=1.
$$



For odd $s$, $s\mid P_s$, and therefore


$$
\mathcal T_s\equiv-6\pmod s.
$$


For odd $s\ge5$, this excludes zero.

The remaining index is $s=3$. One exact application of the retained transfer to the genuine seed gives


$$
z_3=(-12,-22,352)^T.
$$


Hence


$$
\mathcal T_3=2\cdot9\cdot(-12)+3\cdot352=840\ne0.
$$


∎

### Corollary 2.3 — The Turn 15 scalar reduction is globally admissible on the block

The retained off-diagonal formula is


$$
\mathfrak b_s
=
-\frac{(s+1)(s+2)^2\mathcal T_s}{2F_{s+1}}.
$$


Theorems 2.1–2.2 show that


$$
F_sF_{s+1}\mathfrak b_s\ne0
\qquad(s\ge2).
$$



Thus, for


$$
r_s=\mathsf W_{s,t}^{-1}(\tau_t,\tau_{t+1},0)^T,
\qquad
r_s=\lambda_sz_s+(x_s,y_s,0)^T,
$$


the entire block can use the single actual chart


$$
\lambda_s=\frac{(r_s)_3}{F_s}.
$$


There are no auxiliary pivot changes.

The retained second-order recurrence is valid at every required scalar step. Its backward terminal data can be obtained from


$$
(x_t,y_t)=(\tau_t,\tau_{t+1})
$$


by one inversion of $\mathsf A_{t-1}$, followed by backward scalar recurrence. No transfer after $t-1$, and no extra physical source row, is needed.

---

## 3. What global chart admissibility does not pay

The preceding result is nonvanishing over $\mathbb Q$, not a unit assertion at large primes.

Let


$$
H_s=(r_s)_3.
$$


Then the scalar telescope is exactly


$$
\lambda_{s+1}-\lambda_s
=
\frac{H_{s+1}}{F_{s+1}}-\frac{H_s}{F_s}.
$$


If


$$
X_s=F_s(r_s)_1-P_sH_s,\qquad
Y_s=F_s(r_s)_2-Q_sH_s,
$$


its numerator identity is


$$
\boxed{
u_{31,s}X_s+u_{32,s}Y_s
=
F_sH_{s+1}-F_{s+1}H_s.
}
$$


Thus the apparent intermediate chart denominators cancel in the **whole evaluated telescope**, as already anticipated in Turn 15.

This is an exact cancellation statement, not a bound on its resulting numerator.

For example, the inverse-transfer formulas give a small-prime-supported integer


$$
D_{s,t}^{\rm sm}
=
2^{t+1}\prod_{k=s}^{t-1}(k+1)(k+2)(k+3)
$$


that clears $r_s$. Consequently,


$$
D_{s,t}^{\rm sm}F_s
$$


clears $(\lambda_s,x_s,y_s)$. At $p>t+2$, the least simultaneous denominator of this triple has exponent exactly


$$
\boxed{
\bigl(v_p(F_s)-v_p(H_s)\bigr)_+,
}
$$


because $\lambda_s=H_s/F_s$, while $x_s,y_s$ are integral combinations of $r_s$ and $\lambda_s$ in $\mathbb Z_p$.

This pointwise description is obtained **after the complete evaluation**. It does not authorize dropping denominators from individual scalar-recursion operations.

There is also a precise determinant obstruction:


$$
\det\mathsf A_s=\det\mathsf U_s\,\frac{F_s}{F_{s+1}},
$$


so


$$
\boxed{
v_p\!\left(\det(\mathsf A_{t-1}\cdots\mathsf A_n)\right)
=
v_p(F_n)-v_p(F_t)
\qquad(p>t+2).
}
$$


Thus the reduced transfer is not automatically unimodular at a newly acquired terminal divisor of $F_t$.

Most importantly, the retained exterior theorem still gives


$$
\min_i v_p\bigl((z_s\times r_s)_i\bigr)
=
a_t,
\qquad
a_t=\min\{v_p(F_t),v_p(M_t)\}.
$$


Primitive exterior normalization still costs $\mathcal I_t$. The new nonvanishing theorem does not remove that cost.

### Exact acquisition accounting, including medium primes

At $p>t+2$, let


$$
a_s=\min\{v_p(F_s),v_p(\overline M_s)\}.
$$


The retained fixed-seed remainder proves


$$
v_p(c^{\min}_{n,t})=(a_t-a_n)_+.
$$



Define the retreat factor


$$
\mathcal L_{n,t}
=
\prod_{p>t+2}p^{(a_n-a_t)_+}
$$


and retain


$$
\mathcal M_{n,t}
=
\prod_{n+2<p\le t+2}
p^{\min(v_p(F_n),v_p(M_n))}.
$$


Then the exact inventory is


$$
\boxed{
\mathcal I_t
=
\frac{\mathcal I_n\,c^{\min}_{n,t}}
{\mathcal M_{n,t}\mathcal L_{n,t}}.
}
$$



This keeps the medium primes between the moving thresholds. It supplies no estimate for either acquisition or retreat.

Nor has the reference-frame composition changed: its two summands may cancel, and its scalar $\alpha_{u,t}$ is a unit under the retained **common-alignment** hypotheses, not merely because the scalar chart is nonzero over $\mathbb Q$.

Therefore the assigned quantity


$$
\boxed{
\log c^{\min}_{n,bn}
=
\sum_{p>bn+2}(a_{bn}-a_n)_+\log p
}
$$


remains unbounded at the required subfactorial scale.

---

## 4. A new arithmetic restriction on the actual Green weights

Return to an original index. Write the physical exponential source as $\mathfrak f_i$, to distinguish it from the alignment scalar $F$.

Set


$$
W_{n,i}
=
\widehat h\,\mathsf G_{n+1,i}
-\frac m2(\widehat h+\widehat\ell)\mathsf G_{n,i}.
$$


The retained, completely evaluated transverse formula is


$$
\begin{aligned}
\mathscr K_n^\circ={}&
\sum_{i=0}^{n-2}W_{n,i}\mathfrak f_i\\
&+\frac{(3n+1)\widehat h-m\widehat\ell}{2}
  \frac{Y-X+Z}{n}\\
&+\frac{\widehat h}{2}(3X-Y-Z).
\end{aligned}
\tag{4.1}
$$


Both final moment-source terms remain in this expression. Also,


$$
\Xi_n=\kappa-\mathscr K_n^\circ,
\qquad
\kappa=2L(n!)^2,
\qquad
\Theta=CM+F\Xi_n.
\tag{4.2}
$$



### Theorem 4.1 — Three-prefix Green primitivity

For every original $n$, and every prime $p>N=n+2$,


$$
\boxed{
\min\bigl\{
v_p(W_{n,n-2}),
v_p(W_{n,n-3}),
v_p(W_{n,n-4})
\bigr\}=0.
}
\tag{4.3}
$$



In particular,


$$
\boxed{
\gcd\bigl(
|W_{n,n-2}|,|W_{n,n-3}|,|W_{n,n-4}|
\bigr)_{>N}=1.
}
$$



#### Proof

The retained integrating-factor identity implies


$$
(1-z)q(z)B_n'(z)
-\bigl(n(1-z)q'(z)+m q(z)\bigr)B_n(z)
=
\sum_{k\ge0}\mathfrak f_k\frac{z^k}{k!}.
$$


The two polynomial coefficients are


$$
(1-z)q(z)=1-2z+\frac32z^2-\frac12z^3
$$


and


$$
n(1-z)q'(z)+m q(z)
=
1+(n-1)z-\frac{n-1}{2}z^2.
$$


Coefficient extraction therefore gives


$$
\boxed{
b_{k+1}
=
(2k+1)b_k
+\frac{k(2n+1-3k)}2b_{k-1}
+\frac{k(k-1)(k-n-1)}2b_{k-2}
+\mathfrak f_k.
}
\tag{4.4}
$$



This is used only inside the permitted finite range.

For


$$
\beta_k=(b_k,b_{k-1},b_{k-2})^T,
$$


write the homogeneous transfer as


$$
\mathsf B_k^{(n)}
=
\begin{pmatrix}
2k+1 & k(2n+1-3k)/2 & k(k-1)(k-n-1)/2\\
1&0&0\\
0&1&0
\end{pmatrix}.
$$


Its determinant is


$$
\det\mathsf B_k^{(n)}
=
\frac{k(k-1)(k-n-1)}2.
$$


In particular,


$$
\det\mathsf B_{n-1}^{(n)}
=-(n-1)(n-2),
\qquad
\det\mathsf B_n^{(n)}
=-\frac{n(n-1)}2.
\tag{4.5}
$$


Both are units at every $p>N$.

Hold all earlier data and the final two sources
$\mathfrak f_{n-1},\mathfrak f_n$ fixed. The variations of


$$
(\mathfrak f_{n-2},\mathfrak f_{n-3},\mathfrak f_{n-4})
$$


map to the variation of $\beta_{n-1}$ by the matrix


$$
\mathsf C_n=
\begin{pmatrix}
1&2n-3&
(2n-3)(2n-5)+\dfrac{(n-2)(7-n)}2\\
0&1&2n-5\\
0&0&1
\end{pmatrix}.
\tag{4.6}
$$


This matrix has determinant $1$.

The transverse functional on $\beta_{n+1}$ is the row


$$
\ell_n=
\left(
\widehat h,\,
-\frac m2(\widehat h+\widehat\ell),\,
0
\right).
$$


It is primitive over $\mathbb Z_p$: $m/2$ is a unit, and
$(\widehat h,\widehat\ell)$ is primitive.

The three source weights in question are therefore exactly


$$
\boxed{
(W_{n,n-2},W_{n,n-3},W_{n,n-4})
=
\ell_n\mathsf B_n^{(n)}
\mathsf B_{n-1}^{(n)}\mathsf C_n.
}
\tag{4.7}
$$


The matrix multiplying $\ell_n$ is invertible over $\mathbb Z_p$, since


$$
\boxed{
\det\!\left(
\mathsf B_n^{(n)}
\mathsf B_{n-1}^{(n)}\mathsf C_n
\right)
=
\frac{n(n-1)^2(n-2)}2.
}
\tag{4.8}
$$


Multiplication by an invertible integral matrix preserves the ideal generated by a row’s coordinates. This proves (4.3). ∎

For example, the first of these weights is explicitly


$$
\boxed{
W_{n,n-2}
=
\frac{(5n^2-1)\widehat h-(2n^2+n-1)\widehat\ell}{2}.
}
\tag{4.9}
$$



### Consequence: the obstruction is in the seeded values, not kernel content

Even with the two final source terms fixed, the transverse Green map is locally surjective through these three prefix coordinates: at each $p>N$, at least one of their coefficients is a unit.

Thus there is no argument of the form “all earlier source weights acquire a large common $p$-adic factor, so the final two moment terms force nonresonance.” The actual kernel does not have that property.

This is not permission to vary the physical source. The actual $\mathfrak f_i$ are fixed by the moment recurrence. Rather, the theorem identifies what a successful argument must exploit: **the arithmetic correlations among those fixed values**. The Green kernel and its finite triangular structure alone cannot supply the missing estimate.

---

## 5. An exact contact-index formula for shared saturation

This section uses only the actual contact rows, including their retained coordinate-content payment.

Let


$$
z=(P,Q,F),\qquad
g_z=\gcd(|P|,|Q|,|F|),\qquad
z^*=z/g_z.
$$


The large-prime part of $g_z$ is $1$. Let


$$
c_j=(\alpha_j,\beta_j,\gamma_j),\qquad j=0,3,
$$


be the actual contact-coordinate rows, with


$$
c_j\cdot z^*=0,
\qquad
c_0\times c_3=\lambda_{\rm ct}z^*.
$$


Their coordinate contents have no prime factor above $N$. The retained endpoint nondegeneracy gives $\lambda_{\rm ct}\ne0$.

Put


$$
v=(\widehat h,\widehat\ell,0),\qquad
\widehat R_j=c_j\cdot v.
$$



### Theorem 5.1 — Exact common-reference content

For every $p>N$, write


$$
a=v_p(\mathcal I_n),\quad
r_j=v_p(\widehat R_j),\quad
\ell=v_p(\lambda_{\rm ct}).
$$


Then


$$
\boxed{
\min(r_0,r_3)
=
\min(r_0,a+\ell)
=
\min(r_3,a+\ell).
}
\tag{5.1}
$$



Equivalently,


$$
\boxed{
\frac{\gcd(|\widehat R_0|,|\widehat R_3|)_{>N}}{\mathcal I_n}
=
\gcd\!\left(
\frac{|\widehat R_0|}{\mathcal I_n},
|\lambda_{\rm ct}|
\right)_{>N},
}
\tag{5.2}
$$


and the same formula holds with $0$ replaced by $3$.

#### Proof

Work over $\mathbb Z_p$. The annihilator


$$
\mathcal L=\{c\in\mathbb Z_p^3:c\cdot z^*=0\}
$$


is a saturated free module of rank $2$, since $z^*$ is primitive.

The paid contact-coordinate content says that $c_0$ is primitive in $\mathcal L$. Extend it to a basis $c_0,d$, choosing the orientation so that


$$
c_0\times d=z^*.
$$


Then


$$
c_3=u\,c_0+\lambda_{\rm ct}d
$$


for some $u\in\mathbb Z_p$.

Set $R_d=d\cdot v$. The ideal generated by $R_0,R_d$ is the content ideal of the class of $v$ modulo the line spanned by $z^*$. It is also the content ideal of $z^*\times v$. Since


$$
z\times v=(-F\widehat\ell,F\widehat h,-M),
$$


reference primitivity and the fact that $g_z$ is a unit give


$$
\min(v_p(\widehat R_0),v_p(R_d))=a.
\tag{5.3}
$$



Now


$$
(\widehat R_0,\widehat R_3)
=
(\widehat R_0,\lambda_{\rm ct}R_d)
$$


as ideals. If $v_p(\widehat R_0)=a$, both sides of the first equality in (5.1) are $a$. If $v_p(\widehat R_0)>a$, equation (5.3) gives $v_p(R_d)=a$, and hence


$$
\min(r_0,r_3)=\min(r_0,\ell+a).
$$


Interchanging the two primitive contact rows proves the symmetric equality. ∎

No exterior state was made primitive in this proof. The occurrence of $\mathcal I_n$ is an exact content identity, not a free normalization or a height estimate.

### Corollary 5.2 — Exact shared saturated factor

Retain


$$
D_j=\frac{|\widehat R_j|}
{\gcd(|\widehat R_j|,|F|)}
$$


and


$$
C_{\rm sat}
=
\left(
\frac{|\lambda_{\rm ct}|}
{\gcd(|\lambda_{\rm ct}|,|F|/\mathcal I_n)}
\right)_{>N}.
$$


Then


$$
\boxed{
\gcd(D_0,D_3)_{>N}
=
\gcd(D_0,C_{\rm sat})
=
\gcd(D_3,C_{\rm sat}).
}
\tag{5.4}
$$



Consequently,


$$
\boxed{
\gcd(\mathfrak S_0,\mathfrak S_3)
=
\gcd(|T_{\rm aff}|,D_0,C_{\rm sat})
=
\gcd(\mathfrak S_0,C_{\rm sat}).
}
\tag{5.5}
$$



#### Proof

At $p>N$, put $f=v_p(F)$. Since $a\le f$, Theorem 5.1 gives


$$
\begin{aligned}
v_p\bigl(\gcd(D_0,D_3)\bigr)
&=(\min(r_0,r_3)-f)_+\\
&=\min\bigl((r_0-f)_+,(\ell-(f-a))_+\bigr).
\end{aligned}
$$


These are exactly the valuations on the right of (5.4).

The retained primitive affine normalization gives


$$
\mathfrak S_j=\gcd(|T_{\rm aff}|,D_j)_{>N}.
$$


Taking the common gcd and using (5.4) proves (5.5). ∎

Thus Turn 15’s product divisibility sharpens to


$$
\boxed{
\mathfrak S_0\mathfrak S_3
=
J_{\rm res}\,
\gcd(|T_{\rm aff}|,D_0,C_{\rm sat}).
}
\tag{5.6}
$$



This is not an additional factor to divide out after applying an already stronger source/collision certificate. If a retained filter already contains this common-reference information, (5.6) explains that information; it does not create a second saving.

### A useful correction to the quantitative target

For the subfactorial saturation objective, bounding the entire $C_{\rm sat}$ is sufficient but not necessary. Always,


$$
J_{\rm res}\le \mathfrak S_0\mathfrak S_3\le J_{\rm res}^2.
$$


Hence


$$
\boxed{
\log(\mathfrak S_0\mathfrak S_3)=o(n\log n)
\quad\Longleftrightarrow\quad
\log J_{\rm res}=o(n\log n).
}
\tag{5.7}
$$



Accordingly, a valid replacement for the stronger requested estimate
$\log J_{\rm res}+\log C_{\rm sat}=o(n\log n)$ is a proof of the estimate for $J_{\rm res}$ alone. This avoids paying the height of contact collision at primes that do not actually resonate.

Equation (5.7) is a budget equivalence, not a proof of either estimate.

---

## 6. A sharp counter-obstruction: a unit contact index permits deep exclusive resonance

The following local example shows exactly what cannot follow from the algebraic identities alone. It is **not** an alternative producer and is **not** a counterexample to the actual fixed-seed conjecture.

Fix an odd prime $p$, an integer $h\ge1$, and write $q=p^h$. Let $\kappa$ be any integer prime to $p$. Take


$$
z=(1,1,1),\qquad
v=(1,2,0),\qquad
C=1.
$$


Then


$$
F=1,\qquad M=-1,\qquad \mathcal I=1.
$$



Choose primitive contact rows


$$
c_0=(q-2,1,1-q),
\qquad
c_3=(1,0,-1).
$$


They annihilate $z$, and


$$
c_0\times c_3=-z.
$$


Thus


$$
\lambda_{\rm ct}=-1,\qquad C_{\rm sat}=1.
$$


Their reference evaluations are


$$
\widehat R_0=q,\qquad \widehat R_3=1.
$$



Now set


$$
A^\circ=0,\qquad B^\circ=\kappa-1-q.
$$


The complete transverse and canonical scalars are


$$
\mathscr K^\circ=B^\circ-2A^\circ=\kappa-1-q,
$$




$$
\Theta=CM+F(\kappa-\mathscr K^\circ)
=-1+1+q=q.
$$


Therefore


$$
T_{\rm aff}=q,\qquad
\mathfrak S_0=q,\qquad
\mathfrak S_3=1,\qquad
J_{\rm res}=q.
$$



The affine projections are


$$
\mathcal E_0^\circ=\kappa-2q,\qquad
\mathcal E_3^\circ=-1,
$$


both units at $p$. The complete cross-affine identity holds:


$$
\widehat R_0\mathcal E_3^\circ
-\widehat R_3\mathcal E_0^\circ
=q-\kappa
=
\lambda_{\rm ct}(\kappa F-\Theta).
$$



Thus all of the following coexist:

- full-state and reference primitivity;
- primitive contact coordinates;
- unit contact index;
- unit force and moment observations;
- the complete, nonzero $\kappa$ term;
- the complete cross-affine identity;
- arbitrarily deep saturation at one endpoint.

This proves that contact noncollision does not enforce individual nonresonance. Its rigorous role is to restrict **shared** resonance.

Conversely, the contact index can be large while there is no saturation at all. For example, keep the same $z,v,C$, and take


$$
c_0=(1,0,-1),\qquad
c_3=(1,q,-1-q),
$$


so $\lambda_{\rm ct}=q$. With


$$
A^\circ=0,\qquad B^\circ=\kappa-2,
$$


one gets $\Theta=1$, hence


$$
\mathfrak S_0=\mathfrak S_3=J_{\rm res}=1,
\qquad C_{\rm sat}=q.
$$


This is why estimating the unselected height of $C_{\rm sat}$ may be unnecessarily expensive.

The actual source excludes arbitrary choices of $A^\circ,B^\circ$. The outstanding task is to prove a restriction using that exclusion. The algebraic identities by themselves do not provide it.

---

## 7. A concrete remaining seeded congruence obligation

Theorem 4.1 gives a uniform admissible local source coordinate.

At a prime $p>N$, put $f=v_p(F)$. If


$$
v_p(CM)<f,
$$


then


$$
v_p(\Theta)=v_p(CM)<f,
$$


so $p$ cannot contribute to $J_{\rm res}$.

Otherwise $CM/F\in\mathbb Z_p$. Choose


$$
i=i(n,p)\in\{n-4,n-3,n-2\}
$$


with $W_{n,i}\in\mathbb Z_p^\times$, and define


$$
\mathscr K_n^{(i)}
=
\mathscr K_n^\circ-W_{n,i}\mathfrak f_i.
$$


This retains every other prefix term and both final moment-source terms.

On a contributing prime, $g=\gcd(|F|,|CM|)$ has valuation $f$, so


$$
v_p(T_{\rm aff})
=
v_p\!\left(\kappa+\frac{CM}{F}-\mathscr K_n^\circ\right).
$$


For every depth $\nu\ge1$,


$$
\boxed{
v_p(T_{\rm aff})\ge\nu
\iff
\mathfrak f_i
\equiv
W_{n,i}^{-1}
\left(
\kappa+\frac{CM}{F}-\mathscr K_n^{(i)}
\right)
\pmod{p^\nu}.
}
\tag{7.1}
$$



This is now a source-specific congruence involving an admissible unit coefficient at every large prime. It is not merely a free homogeneous-state condition. Nevertheless, no bound for the depth or aggregate prime support of (7.1) has been proved.

A sufficient follow-on lemma is:

> **Seeded transverse Bézout lemma.**  
> On an infinite original subsequence, construct from the actual moment recurrence and the finite Green response integers $C_n>0$ and coefficients
> 

$$
> A_n,B_n\in\mathbb Z[1/p:p\le N]
>
$$


> such that
> 

$$
> A_nT_{\rm aff}+B_nH_{\rm ref}=C_n,
> \qquad
> \log(C_n)_{>N}=o(n\log n).
>
$$


> All occurrences of $\mathscr K_n^\circ$ must use (4.1), and $\kappa$ must remain complete.

Such a lemma would imply $J_{\rm res}\mid(C_n)_{>N}$, hence the needed subfactorial saturated product by (5.7). It is not supplied by the unit Green weights; those weights show precisely why the **fixed values** must enter its proof.

On the alignment side, the concrete remaining lemma is still a bound for acquisition in the now globally valid scalar/telescoping system:


$$
\sum_{p>bn+2}(a_{bn}-a_n)_+\log p=o(n\log n).
$$


No primitive exterior division is available for free.

A bound on all sufficiently large consecutive geometric blocks would propagate to a subfactorial $\mathcal I_n$. A bound on an arbitrary sparse set of blocks would additionally require control of the initial alignments at those blocks. The medium-prime factors in Section 3 cannot be suppressed when reconstructing those initial alignments.

---

## 8. The original finite construction and final arithmetic remain unchanged

None of these arguments changes the producer.

### 8.1 Complete source and physical terminal

The physical exponential source remains


$$
\mathfrak f_k
=
(n+1)a_k-nk\,a_{k-1}
+\frac{(n-1)k(k-1)}2a_{k-2}
+\frac{k(k-1)(k-2)}2a_{k-3}
$$


through


$$
\boxed{K=2n+2.}
$$


The coefficient of $\mathfrak f_K$ in $b_{K+1}$ remains $1$, and the original terminal-return functional is unchanged.

The logarithmic $F/(1-z)$ forcing is not replaced by a homogeneous equation. Both exponential boundary columns remain in the original finite reconstruction. Cancellation of a homogeneous contribution inside $\mathscr K_n^\circ$ does not delete either boundary from the producer.

The complete endpoint residual remains


$$
\boxed{
C_j^{\rm complete}
=
\mathcal E_j^\circ+
2n!m!(\alpha_j\rho_n+\beta_j\rho_{n+1}).
}
$$



### 8.2 Corrected columns, exterior $+1$, and actual row contents

Retain


$$
x=T^{-1}(n!t),\qquad y=T^{-1}\widehat w,
$$




$$
S=
\begin{pmatrix}
1&-n&n(n+1)\\
0&1&-2n\\
0&0&1
\end{pmatrix},
\qquad sx=Sx,\quad sy=Sy,
$$




$$
u=(-sx_0,\ sx_0-sx_1,\ sx_1-sx_2,\ sx_2),
$$




$$
v=(1-sy_0,\ sy_0-sy_1,\ sy_1-sy_2,\ sy_2).
$$


The exterior $+1$ is retained.

The least simultaneous clearer is over all eight rational entries. Each resulting row is divided by its actual two-entry **all-prime** content. The accepted $3375$ contents remain


$$
(113940000,\ 9780750,\ 10125,\ 1).
$$


No contact-lattice index or large-prime gcd replaces them.

### 8.3 Actual endpoint and weighted primitive denominators

The endpoint denominator remains


$$
\boxed{
d_j=
\frac{|n!R_j|}
{\gcd(|n!R_j|,\ |E_nR_j+C_j^{\rm complete}|)}.
}
$$



For the retained reduced weight $\lambda=a/k_{\rm wt}$, keep


$$
J_{\rm wt}
=
B_{\rm wt}\widetilde v_0-A_{\rm wt}\widetilde v_3,
$$




$$
T_{\rm wt}
=
aJ_{\rm wt}+k_{\rm wt}A_{\rm wt}\widetilde v_3,
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


Then


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



These are the actual all-prime primitive quantities. The auxiliary denominator of $\Theta/F$ is not substituted for them.

The whole error remains


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda e_3\alpha_{n,2}
(\lambda-\Lambda_{n,2}).
}
$$


Neither its nonvanishing nor its required smallness has been proved at an infinite set of the same original indices where the proposed arithmetic estimates would hold.

---

## 9. Proof ledger and bounded exact arithmetic

| Statement | Status |
|---|---|
| $F_s\ne0$ for every auxiliary $s\ge2$ | **Proved** |
| $v_2(F_s)=1$ for even $s$ | **Proved** |
| $\mathcal T_s=2(2s+3)P_s+3F_s\ne0$ for all $s\ge2$ | **Proved** |
| Global admissibility of the actual scalar chart | **Proved** |
| Subfactorial multiplicative-block cofactor | **Not proved** |
| Three-prefix Green weights primitive at $p>N$ | **Proved** |
| Exact common-reference/contact-index formula | **Proved under the retained actual contact hypotheses** |
| Exact shared-saturation formula | **Proved** |
| Unit contact index excludes exclusive resonance | **Disproved as an implication of the algebraic identities alone** |
| Subfactorial actual $J_{\rm res}$ | **Not proved** |
| Subfactorial $C_{\rm sat}$ | **Not proved; not necessary for (5.7)** |
| Infinite favorable all-prime primitive whole forms | **Not established** |
| Rationality or irrationality of $e+\pi$ | **Unresolved** |

### Bounded calculation, if an independent symbolic audit is desired

No computer calculation was performed. No new producer, alignment sample, $3375$ endpoint calculation, or $11025$ calculation is requested.

The proofs do not require further numerical data. A small independent audit of the new polynomial identities has completely bounded inputs:

1. the matrices $\mathsf B_n^{(n)},\mathsf B_{n-1}^{(n)},\mathsf C_n$ displayed in Section 4;
2. the symbolic row
   

$$
\ell_n=(h,-(n+1)(h+\ell)/2,0);
$$


3. the degree-three polynomial differential operator preceding (4.4);
4. optionally, the two explicit contact countermodels of Section 6.

Expected verifiable outputs are:

- the coefficient recurrence (4.4);
- the exact determinant
  

$$
\det(\mathsf B_n^{(n)}\mathsf B_{n-1}^{(n)}\mathsf C_n)
  =n(n-1)^2(n-2)/2;
$$


- the first coordinate of the row product equal to
  

$$
\bigl((5n^2-1)h-(2n^2+n-1)\ell\bigr)/2;
$$


- the three source-response coordinates in (4.7), obtained by at most four finite companion steps;
- the stated contact cross products and the complete identities for $\Theta$ in Section 6.

These are rational-polynomial identities in fixed-size matrices. Their verification would establish only those identities, not either asymptotic gcd estimate.

---

## Conclusion

The actual fixed-seed reduction is now unconditionally available on every auxiliary step:


$$
\boxed{F_s\mathcal T_s\ne0\qquad(s\ge2).}
$$


This removes the chart-patching uncertainty without treating any newly exposed divisor as free.

On the affine side, the last three prefix weights of the actual transverse Green functional have no common large-prime content, even after both final moment-source terms are fixed. Thus an eventual nonresonance theorem must use the true seeded source correlations.

The contact cross product gives the exact shared-saturation restriction


$$
\boxed{
\gcd(\mathfrak S_0,\mathfrak S_3)
=
\gcd(|T_{\rm aff}|,D_0,C_{\rm sat}),
}
$$


but a unit contact index still permits arbitrarily deep exclusive resonance at the algebraic-interface level. The remaining joint-growth problem is therefore genuinely a problem about the evaluated fixed source.

The exact unresolved bottlenecks are:

1. subfactorial **new terminal alignment acquisition** over multiplicative blocks, without circular exterior normalization;
2. a seeded arithmetic bound for
   

$$
J_{\rm res}=\gcd(|T_{\rm aff}|,H_{\rm ref})_{>N},
$$


   retaining the complete prefix, both final moment terms, and $\kappa$;
3. the actual all-prime final gcd, primitive denominator, and nonzero whole-error comparison at the **same infinite original indices**.



$$
\boxed{\text{No unconditional proof or disproof of the irrationality of }e+\pi\text{ is obtained.}}
$$


