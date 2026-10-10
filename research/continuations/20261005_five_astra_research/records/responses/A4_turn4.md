> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 independent review, turn 4

## Summary of dispositions

1. **Matched $b=4$: PASS.** The newly supplied scalar proofs close the earlier documentary gap. The falling-factorial compensation has sufficient precision, and the common-index formulas handle unequal supports for **both** $I(\mathscr F_n)$ and $I(x\mathscr F_n)$. Together with the supplied four-prime certificate and fixed-$b$ whole-error theorem, they prove the unconditional infinite implication claimed by A2. No additional residue computations are needed.

2. **Weighted regular dyadic theorem:** the older note is indeed superseded. The final-gcd transfer from
   

$$
U\equiv4\pmod8
$$


   to
   

$$
v_2(q_{\rm center})=n+2
$$


   passes. The supplied later theorem describes a legitimate finite-state proof, not extrapolation from degrees. However, the actual full-state closure receipts for its last two machines are not reproduced in this packet. I identify that narrow independent-verification dependency below; it is **not** a mathematical counterexample or a reason to reclassify the author theorem as merely a conjectural pattern.

3. **A5’s bordered-minor identity: PASS**, on its stated rank and nonzero-endpoint domain. The five-tail high-row saturation and falling metric also pass; I independently derive their most important divisibility and derivative identities below. The exceptional matching case really does require a further digit. The offset $p=n+2$ is auxiliary and supplies no additional prime when $n=P-1$ is even.

4. **New compact-size result:** for the actual primitive weighted polynomial $Q=q_n$, its compact norm is controlled by its actual endpoint:
   

$$
\boxed{
   \max_{0\le y\le1}|Q(y)|
   \le |Q(-1)|
      \left(4n\,e^{\,4\sqrt{(2n-1)\sqrt2}}-1\right).
   }
$$


   This is an explicit subexponential loss relative to $Q(-1)$, obtained from the actual rank-one modified orthogonal polynomial and ordinary Laguerre polynomials. It replaces the previously uncontrolled compact-size term in the determinant budget by an endpoint-size term, with only $O(n^{3/2})$ extra cost. It does not settle the endpoint/content balance.

No irrationality decision for $e+\pi$ follows.

---

# 1. Matched $b=4$: the scalar-transfer gap is closed

I use $(x)_r=x(x-1)\cdots(x-r+1)$, with $(x)_0=1$.

## 1.1 Precision of the coefficient compensation

Put


$$
a_s(n)=[z^s](1-z+z^2/2)^n.
$$


All these coefficients are integral at every odd prime.

Suppose $m\ge n\ge0$ and $p^a\mid m-n$, with $p$ odd. For $s\ge1$, expansion of


$$
(1+(\phi-1))^{m-n},\qquad \phi=1-z+z^2/2,
$$


gives


$$
v_p(a_s(m)-a_s(n))\ge a-\lfloor\log_p s\rfloor.
\tag{1.1}
$$


Indeed every nonconstant contribution has an index $1\le j\le s$, and


$$
v_p\binom{m-n}{j}\ge a-v_p(j)
\ge a-\lfloor\log_p s\rfloor.
$$



For every integer $x$, including negative integers,


$$
(x)_r=r!\binom xr,
\qquad
v_p((x)_r)\ge v_p(r!).
\tag{1.2}
$$


For $s\ge1$,


$$
v_p(s!)\ge\lfloor\log_p s\rfloor:
$$


if $p^k\le s<p^{k+1}$, the factor $p^k$ alone has valuation $k$. Thus the loss in (1.1) is fully compensated by a falling factorial of length at least $s$.

More explicitly, for fixed $d\ge0$,


$$
\begin{aligned}
&(m)_{s+d}a_s(m)-(n)_{s+d}a_s(n)\\
&=\bigl((m)_{s+d}-(n)_{s+d}\bigr)a_s(n)
 +(m)_{s+d}\bigl(a_s(m)-a_s(n)\bigr).
\end{aligned}
$$


The first term is divisible by $p^a$, since the falling factorial is an integer polynomial. The second is divisible by $p^a$ by (1.1)–(1.2). The case $s=0$ is immediate.

Consequently the defining formula


$$
H_n^{(d)}(1)=\sum_{s\ge0}(n)_{s+d}a_s(n)
\tag{1.3}
$$


transfers modulo $p^a$. No extra digit is needed.

## 1.2 Unequal supports: both integral coordinates

Define on $\mathbb Z_p$


$$
\mathscr D(x)=\sum_{r\ge0}(x)_r.
\tag{1.4}
$$


The inequality (1.2) extends to $x\in\mathbb Z_p$ by continuity, so this series converges uniformly. Every partial sum is an integer polynomial; therefore


$$
x\equiv y\pmod{p^a}
\quad\Longrightarrow\quad
\mathscr D(x)\equiv\mathscr D(y)\pmod{p^a}.
\tag{1.5}
$$


For $j\ge0$,


$$
\mathscr D(j)=\sum_{r=0}^j(j)_r
=j!\sum_{r=0}^j\frac1{r!}
=I(x^j).
$$



Expanding $\mathscr F_n=x^nH_n$ gives the exact formulas


$$
\mathcal A_n=I(\mathscr F_n)
=\sum_{s\ge0}(n)_sa_s(n)\mathscr D(2n-s),
\tag{1.6}
$$




$$
\mathcal M_n=I(x\mathscr F_n)
=\sum_{s\ge0}(n)_sa_s(n)\mathscr D(2n+1-s).
\tag{1.7}
$$


At a nonnegative integer $n$, these are finite in value because $(n)_s=0$ for $s>n$.

When comparing $m$ and $n$, take one common finite range $0\le s\le\max(m,n)$. The arguments of $\mathscr D$ are allowed to be negative. Such arguments are defined by (1.4), while the corresponding out-of-support coefficient is exactly zero. Hence there is no use of a negative factorial and no unaccounted boundary term.

The coefficient product transfers by Section 1.1; the $\mathscr D$-factor transfers by (1.5). This proves all-depth transfer of both integral coordinates. Since


$$
\mathcal B_n=\mathcal M_n+H_n(1)-H_n'(1),
$$


it transfers as well.

**Conclusion:** the full five-coordinate transfer assertion used in A2 turn 3 is proved.

## 1.3 Normalized $b=4$ transfer

The hatted determinant circuit uses the integral replacement functions $F,z,w$, and only the Taylor-column divisions by


$$
0!,1!,2!,3!.
$$


Its fixed coefficient denominators therefore involve only $2$ and $3$. The derivative recurrences and exact division-free normalized derivative formulas give polynomial expressions in the five scalar coordinates and $n$.

Thus for every $p\ge5$,


$$
m\equiv n\pmod{p^a}
\Longrightarrow
(\widehat\sigma,\widehat\chi,\widehat\kappa,\widehat V)_m
\equiv
(\widehat\sigma,\widehat\chi,\widehat\kappa,\widehat V)_n
\pmod{p^a}.
\tag{1.8}
$$


There is no division by $2n+5$, including on its residue-field zero set.

This closes the dependency identified in my previous report.

---

# 2. The four-prime infinite implication, including the final gcd

I do not repeat the finite tables.

Let


$$
\mathcal P_4=\{5,11,13,17\},
\qquad
d_n=\gcd(|\widehat\sigma_n|,|\widehat\chi_n|,
                         |\widehat\kappa_n|).
$$


The supplied unit certificate, together with (1.8), gives


$$
v_p(\widehat V_n)=0
\qquad(n\ge0,\ p\in\mathcal P_4).
$$


Since $d_n\mid\widehat V_n$,


$$
v_p(d_n)=0,\qquad v_p(V_n^*)=0.
\tag{2.1}
$$


This does not assert periodicity of the globally primitive triple.

For actual approximants $n\ge4$, retain


$$
S_n^*=Q_n^*+\frac{2^{n+1}}{(n!)^2}V_n^*,
\qquad
\frac{X_n}{Y_n}=\frac{S_n^*}{D_n^*}.
$$


With any valid common clearer $\lambda_n>0$, set


$$
N_n=\lambda_nS_n^*,\qquad Z_n=\lambda_nD_n^*,
\qquad g_n=\gcd(|N_n|,|Z_n|).
$$


On $D_n^*\ne0$, the actual primitive center is


$$
c_n=\frac{p_n}{q_n}=-\frac{S_n^*}{D_n^*},
$$


where


$$
\boxed{
q_n=\frac{|Z_n|}{g_n},\qquad
p_n=-\operatorname{sign}(Z_n)\frac{N_n}{g_n}.
}
\tag{2.2}
$$



For $p\in\mathcal P_4$,


$$
v_p(Q_n^*)\ge-\lfloor\log_p(n+1)\rfloor.
$$


For $n\ge p$,


$$
2v_p(n!)>\lfloor\log_p(n+1)\rfloor.
$$


Together with (2.1), this proves strict separation in the **whole numerator**:


$$
v_p(S_n^*)=-2v_p(n!).
$$


In particular $S_n^*\ne0$, and (2.2) gives


$$
\boxed{
v_p(q_n)=2v_p(n!)+v_p(D_n^*)\ge2v_p(n!).
}
\tag{2.3}
$$


The common arithmetic domain is $n\ge17,\ D_n^*\ne0$.

The supplied fixed-$b$ theorem at $b=4$ supplies eventual $Y_n\ne0$ and the whole nonzero error


$$
e+\pi-c_n
=\frac{R_n(1)}{Y_n}
=(-1)^n\epsilon_n(\sqrt2-1)^4(1+o(1)),
\qquad
\log\epsilon_n=-\tau n+o(n).
$$


Consequently,


$$
\liminf_{n\to\infty}\frac1n
 \log|q_n(e+\pi)-p_n|
\ge
2\sum_{p\in\mathcal P_4}\frac{\log p}{p-1}-\tau.
\tag{2.4}
$$



**Unconditional audit disposition:** PASS for the claimed infinite implication, with the supplied finite certificate and established fixed-$b$ theorem as inputs. There is no remaining scalar-transfer hypothesis. In particular the supplied strict positive rate margin excludes shrinking primitive forms on every unbounded-index subsequence of this matched family.

This is an exclusion of this family, not an irrationality result.

---

# 3. The later weighted dyadic theorem and distinct-center nonvanishing

## 3.1 The final-gcd calculation passes

Use the regular family


$$
n=4^j+1,\qquad j\ge1,\qquad
m=(n-1)/2,\qquad \sigma=n-2.
$$


Let


$$
\det(R+S wvv^T)=\alpha+\beta S,\qquad w=Q(-1).
$$


For an odd common clearer $D$, put


$$
g=\gcd(|D\alpha|,|D\beta|).
$$


With the denominator chosen positive,


$$
q_{\rm center}=\frac{|D\beta|}{g},
\qquad
p_{\rm center}
=-\operatorname{sign}(\beta)\frac{D\alpha}{g}.
\tag{3.1}
$$


The sign qualification matters if $\beta<0$.

The established divided-basis and same-basis arctangent argument gives


$$
v_2(\alpha)=\gamma,\qquad
v_2(\beta)=\gamma+v_2(w)-2\sigma.
\tag{3.2}
$$


Thus the complete endpoint gcd, not a row content, satisfies


$$
v_2(g)=\min\{v_2(\alpha),v_2(\beta)\}.
$$



The newer endpoint theorem supplies


$$
U=\frac{P_n(0)}{(2^m m!)^2}\equiv4\pmod8.
\tag{3.3}
$$


Hence


$$
v_2(P_n(0))=2\sigma+2=2n-2.
$$


Since


$$
Q(2z-1)=\lambda2^nP_n(z),\qquad \lambda\ \text{odd},
$$


we obtain


$$
v_2(w)=n+v_2(P_n(0))=3n-2.
$$


Substituting into (3.2),


$$
v_2(\beta)=\gamma+n+2,\qquad v_2(g)=\gamma,
$$


and therefore


$$
\boxed{v_2(q_{\rm center})=n+2.}
\tag{3.4}
$$



No odd-prime cancellation can alter this dyadic conclusion.

## 3.2 What the supplied argument establishes, and what remains to inspect

The newer theorem uses the right sort of finite proof:

* an a priori finite-degree moment representation;
* exact cancellation of its surplus coefficients;
* a fixed rational Cartier transition;
* full-state, phase-inclusive repetition;
* fixed finite transfers for the remaining linear contractions;
* separate treatment of small depths and boundary terms.

In particular, equality of **entire states** at two depths, under a deterministic transition, proves equality at all subsequent corresponding depths. This is not the invalid inference “several values of $U$ equal $4$, therefore all do.”

The supplied moment-polynomial receipt contains actual coefficient arrays and the claimed vanishing coefficients. It is substantially more informative than a list of degree evaluations.

There is nevertheless a precise limit to this independent review: the packet does **not** reproduce the complete arrays for

1. the six rational-Cartier states establishing phase-inclusive closure $h_7=h_3$; and
2. the four $225$-coordinate linear-transfer orbits, terminal tables, and boundary outputs establishing closure at step $11=$ step $3$.

Those are explicitly invoked by Sections 5–7 of the exact endpoint theorem. The theorem describes them, but their coefficients cannot be independently compared from the text and two JSON receipts supplied here. The earlier modulo-$8$ branch derivation used to obtain the proper rational branch functions is also referenced rather than fully reproduced.

Accordingly:

* **I withdraw the earlier documentary objection based on the older unresolved-$\eta$ note.**
* **The final arithmetic implication (3.3) $\Rightarrow$ (3.4) passes independently.**
* **The author theorem remains a supplied exact finite-state theorem, not a conjectural numerical pattern.**
* A complete independent certificate-level signoff on (3.3) still requires the specific closure data just listed. I have found no counterexample to it.

## 3.3 Distinct centers and nonvanishing

Once (3.4) is established, the centers at distinct regular indices are pairwise distinct: equal reduced rational numbers have the same reduced denominator, hence the same dyadic denominator valuation, whereas $n+2$ is strictly increasing.

Therefore at most one center can equal $S=e+\pi$, irrespective of whether $S$ is rational or irrational. Since the regular sequence is infinite, its whole primitive forms are eventually nonzero:


$$
\boxed{
q_{\rm center}S-p_{\rm center}
=\operatorname{sign}(\beta)\frac{D}{g}
  \bigl(\alpha+\beta S\bigr)\ne0
}
\tag{3.5}
$$


apart from at most one index.

This is the correct distinct-center implication. It neither assumes irrationality nor proves decay of these forms.

---

# 4. A5’s global bordered-minor identity

Let $A_0$ have rank $N-2$, with saturated kernel


$$
\mathscr L=\ker_{\mathbb Q}(A_0)\cap\mathbb Z^N.
$$


Assume $\boldsymbol e(\mathscr L)\ne0$, so


$$
\boldsymbol e(\mathscr L)=h\mathbb Z,\qquad h>0.
$$


Let $X_0$ be an integer extension of the integer-valued endpoint functional $D_0\boldsymbol x$ on $\mathscr L$.

Such an extension exists because a saturated subgroup of a finite-rank free abelian group is a direct summand.

Take Smith form


$$
UA_0V=[D\ 0\ 0].
$$


The last two columns of $V$ form a basis of $\mathscr L$, and


$$
\Delta_A=|\det D|.
$$


For any appended integer row $r$, its bordered maximal minors have gcd


$$
\Delta_A\gcd((rV)_{N-1},(rV)_N).
$$


Thus


$$
\Delta_e=\Delta_A h,
\qquad
\Delta_x=\Delta_A\gcd(|a|,|b_{\rm end}|).
$$


It follows exactly that


$$
\boxed{
\frac h\gamma
=\frac{\Delta_e}{\gcd(\Delta_e,\Delta_x)}.
}
\tag{4.1}
$$



The formula is independent of row clearers and of the extension $X_0$: two extensions differ by a row vanishing on $\mathscr L$, hence have the same last two Smith coordinates.

**PASS**, with the explicit nonzero-image qualification above. Normality alone should not be used as a substitute for that qualification unless its source theorem includes it.

The formula retains the actual matching row. Replacing $A_0$ by only the high block would compute a different scalar.

---

# 5. Five-tail audit at $p=n+2$

Assume


$$
n=p-2,\quad p\text{ odd},\quad b\ge6,\quad 2b-3<p,\quad s=b-4.
$$



## 5.1 Unit high block and the forced division

For $0\le a<p$, the coefficient formula for $H_{p+a}$ gives


$$
H_{p+a}(x)\equiv x^pH_a(x)\pmod p.
$$


Indeed terms with falling-factorial length exceeding $a$ acquire a factor $p$, while the remaining coefficients reduce to those at $a$. Hence


$$
\mathscr F_{p+a}(x)\equiv x^{2p}\mathscr F_a(x)\pmod p.
$$


For derivative orders $<p$, evaluation at $1$ reduces to the corresponding derivative of $\mathscr F_a$.

Therefore the rows $l=a+2$, $1\le a\le b-4$, have zeros for $j>a-1$ and diagonal entries $(2a)!$. These are units under the stated inequality. The unit Schur chart $z=Jy$ is valid.

For the row at $k=p$, use


$$
\frac{H_p'}p
=\sum_{s=0}^{p-1}(p-1)_sa_s(p)x^{p-s-1}
\equiv x^{p-1}\pmod p.
$$


Also $H_p\equiv x^p\pmod p$. Thus


$$
\frac{\mathscr F_p'}p
=x^{p-1}H_p+x^p\frac{H_p'}p
\equiv2x^{2p-1}\pmod p.
$$


Consequently


$$
\boxed{
\frac{E_{p,j+1}}p\equiv2(-1)^j j!\pmod p.
}
\tag{5.1}
$$


This is an exact integer division before reduction. It confirms A5’s normalized second low row.

## 5.2 Independence of the two low rows

Differentiating the exact adjacent recurrence and reducing the differential equation gives the division-free operator


$$
\frac{\mathscr F_{k+1}'}{k+1}
=
x\mathscr F_k''
+(1-k-2x)\mathscr F_k'
+(k-1+2x)\mathscr F_k.
\tag{5.2}
$$


At $k=p-1$, differentiation $j$ times and evaluation at $1$, together with (5.1), yields


$$
E_{j+2}+jE_{j+1}-2jE_j+2jE_{j-1}=2c_j,
\qquad c_j=(-1)^jj!.
\tag{5.3}
$$


For $j\ge1$, direct substitution shows that the same left-hand operator annihilates $c_j$.

If the two five-tail rows were proportional, applying (5.3) at $j=s+1$ would give $0=2c_{s+1}$, impossible. All indices lie within the five tails, and $c_{s+1}$ is a unit.

Thus the normalized high block is saturated. There is no extra combined high-row content left after the displayed division by $p$.

## 5.3 Matching and endpoint ranks

The endpoint formulas retain the full $T_P,T_U$ expressions. In particular, coefficients divisible by $p$ must not simply be discarded inside factorial sums that have one possible $p$-pole. A5 does not make that discard: the quantities $W_s$ and $T_{U,s}$ remain in the formulas.

The reduced system is


$$
\boldsymbol d y=\boldsymbol e_Ey
=(\boldsymbol f-\Theta\boldsymbol1)y=0,
$$


with endpoints


$$
B(1)=\boldsymbol1y,\qquad
A(1)=-\varepsilon T_{U,s}\boldsymbol1y
+\varepsilon c_s\boldsymbol gy.
$$


The minor


$$
\det[\boldsymbol1;\boldsymbol d;\boldsymbol f]_{\{0,1,2\}}
=-(s+1)
$$


is a unit. Hence the rank-four chart, when present, makes both the matching row and appended endpoint sum primitive.

At the exceptional rank-three chart, the two equations


$$
HA=2(s+1)(s+3),\qquad HC=2(H-1)
$$


are precisely the two remaining recurrence compatibility conditions. They do not automatically imply a matching rank drop:

* If $A+C\Theta\ne0$, the matching row still has rank three, while the endpoint sum lies in its span.
* If $A+C\Theta=0$, the matching row loses rank modulo $p$, and its primitive next-digit Schur row is required.

The nonzero endpoint minor quoted by A5 in the first case is consistent with the fitted-row calculation. It gives an $A$-endpoint unit even though $p\mid h$, and therefore $p\nmid\gamma$. This is a scalar obstruction, not a proof of prime survival in the final denominator.

**PASS for this distinction.** Treating the second case as already saturated would be an error; A5 explicitly does not do so.

## 5.4 The actual falling metric

This part can also be checked directly.

The contiguous identity gives


$$
\frac{\mathscr F_{p+1}''}{p+1}
=(2p+1)(2\mathscr F_p-\mathscr F_p')
+p^3\mathscr F_{p-1}.
$$


For $j\ge1$, divide its $j$-th derivative by $p$ and use (5.1):


$$
\boxed{
\frac{E_{p+1,j+2}}p
\equiv2(j+2)(-1)^{j-1}(j-1)!\pmod p.
}
\tag{5.4}
$$


Also $E_{p+1,2}\equiv2\pmod p$.

The first unit high row therefore gives


$$
z_0/p\equiv-\sum_{j=s}^{s+4}(j+2)D_j,
\quad
D_j=(-1)^{j-1}(j-1)!y_{j-s}.
$$


For $1\le j<s$, $z_j\in p\mathbb Z_p$, so its weighted coordinate disappears after dividing by $p$ and reducing. The zeroth coordinate does not disappear. Hence


$$
\boxed{
\frac{z^T\Omega z'}{p^2}
\equiv
\sum_{j=s}^{s+4}D_jD_j'
+\left(\sum_{j=s}^{s+4}(j+2)D_j\right)
 \left(\sum_{j=s}^{s+4}(j+2)D_j'\right).
}
\tag{5.5}
$$


The rank-one addition in A5’s metric is necessary and has the correct sign.

A nonzero restriction on the primitive zero-endpoint direction gives exact norm depth $2$; rank four alone does not give that nonvanishing. A5 correctly retains this additional test.

The further translation from this norm depth to the symbols $v_p(\delta)=2$ and $p\nmid q_n$ uses the proportional construction’s definitions of $T,\delta,\alpha,r$, which are not fully defined in the supplied A5 report. The local metric calculation passes; independent verification of that last translation requires those definitions, not another high-row computation.

Finally, if $n=P-1$ with $P$ odd, then $n+2=P+1$ is even and exceeds $2$. The parity restriction is exact. This auxiliary calculation cannot be counted as an additional surviving or canceled prime at those indices.

---

# 6. New compact norm bound using the actual weighted polynomial

This result is independent of the missing finite-state receipts.

Let


$$
\mu(F)=\int_0^\infty e^{-t}F((1-t)^2)\,dt,
\qquad
\rho(F)=\mu(F)-F(-1).
$$


Let $q_n$ denote the monic $\rho$-orthogonal polynomial, $n\ge2$, and let $p_n$ be the monic $\mu$-orthogonal polynomial. Write $K_n$ for the $\mu$-kernel on degrees $<n$, and


$$
K=K_n(-1,-1).
$$



The exact rank-one modification identity is


$$
q_n(y)=p_n(y)+q_n(-1)K_n(-1,y),
$$




$$
q_n(-1)=\frac{p_n(-1)}{1-K}.
$$


Here $K\ge3/2$, so the denominator is nonzero.

All zeros of every $p_j$ are positive. For $0\le y\le1$ and every positive root $r$,


$$
|y-r|\le1+r.
$$


Therefore


$$
|p_j(y)|\le|p_j(-1)|.
$$


Termwise in the orthogonal kernel expansion,


$$
|K_n(-1,y)|\le K.
$$


It follows that


$$
\left|\frac{q_n(y)}{q_n(-1)}\right|
\le (K-1)+K=2K-1.
\tag{6.1}
$$



We now bound $K$ explicitly, using the actual even-composed polynomial space.

For $\deg F<n$, put


$$
P(t)=F((1-t)^2).
$$


Then $\deg P\le2n-2$,


$$
\mu(F^2)=\int_0^\infty e^{-t}P(t)^2\,dt,
\qquad F(-1)=P(1+i).
$$


Expand $P$ in the ordinary Laguerre polynomials $L_j$, normalized by


$$
\int_0^\infty e^{-t}L_j(t)L_l(t)\,dt=\delta_{jl}.
$$


Cauchy–Schwarz gives


$$
|F(-1)|^2
\le \mu(F^2)\sum_{j=0}^{2n-2}|L_j(1+i)|^2.
$$


Taking the supremum defining the evaluation norm,


$$
K\le\sum_{j=0}^{2n-2}|L_j(1+i)|^2.
\tag{6.2}
$$



Since


$$
L_j(z)=\sum_{r=0}^j(-1)^r\binom jr\frac{z^r}{r!},
$$


we have


$$
|L_j(z)|
\le\sum_{r\ge0}\frac{(j|z|)^r}{(r!)^2}
\le e^{2\sqrt{j|z|}}.
$$


The last inequality follows by comparing the diagonal terms with


$$
\left(\sum_{r\ge0}\frac{(\sqrt{j|z|})^r}{r!}\right)^2.
$$


At $z=1+i$, $|z|=\sqrt2$. Thus a convenient uniform bound is


$$
K\le2n\,e^{4\sqrt{(2n-1)\sqrt2}}.
$$


Combining with (6.1), and restoring any rational normalization, proves:

> **Compact endpoint domination lemma.** For the actual primitive integer weighted polynomial $Q=q_n$, $n\ge2$,
> 

$$
> \boxed{
> M_n:=\max_{0\le y\le1}|Q(y)|
> \le |Q(-1)|\,C_n,
> \quad
> C_n=4n\,e^{4\sqrt{(2n-1)\sqrt2}}-1.
> }
> \tag{6.3}
>
$$



This is not an ordinary derangement Hankel determinant evaluation. It uses the actual even-composed subspace only through its inclusion in the full Laguerre space.

## 6.1 Effect on the primitive-error budget

Retain the primitive-$Q$ normalization of the direct Gram bound:


$$
A=\ell^k\alpha,\qquad B=\ell^k\beta,\qquad
g=\gcd(|A|,|B|),\qquad q=|B|/g,
$$


and $c=-A/B$, on $B\ne0$. The entire evaluated error is


$$
q|S-c|=\frac{|A+BS|}{g}.
$$


The prior absolute-Gram inequality and (6.3) give


$$
\boxed{
q|S-c|
\le
\frac{\ell^k(7|Q(-1)|C_n)^kD_k}{g},
}
\tag{6.4}
$$


where


$$
D_k=\det\left(\frac1{2i+2j+1}\right)_{0\le i,j<k}.
$$



Since $k=(n+1)/2$,


$$
k\log C_n=O(n^{3/2}).
$$


Thus, retaining the previously proved moving-pole divisor
$g=\mathfrak C_ng'_n$, the compact/content budget becomes


$$
\boxed{
\log\!\left(
\frac{\ell^k(7|Q(-1)|C_n)^kD_k}{g}
\right)
\le
k\log|Q(-1)|
+\left(\frac74-\frac{\log2}{2}\right)n^2
-\log g'_n+o(n^2).
}
\tag{6.5}
$$



This is a concrete improvement in the dependency structure: no independent estimate for the compact maximum $M_n$ is needed. Its excess over the actual endpoint is subexponential. What remains is the arithmetic balance between the actual endpoint size and the final determinant-pair content. The dyadic valuation of $Q(-1)$ alone does not bound its absolute size or supply that balance.

---

# Closing ledger

## (1) New result and proof status

* **Closed independently:** matched-$b=4$ scalar transfer, including falling-factorial precision and both unequal-support integral coordinates.
* **PASS:** the four-prime infinite implication, with the actual final gcd, primitive denominator, eventual endpoint nonvanishing, and whole evaluated error retained.
* **PASS:** the later weighted theorem’s final-gcd implication $U\equiv4\pmod8\Rightarrow v_2(q)=n+2$, and its consequent pairwise-distinct-center/nonvanishing argument.
* **Certificate-level dependency identified:** the two complete finite-state closure datasets needed to independently verify the later theorem’s final residue $U\equiv4\pmod8$. This does not reinstate the older conjectural status or refute the author theorem.
* **PASS:** A5’s bordered-minor identity, five-tail high-row saturation, matching-rank distinction, and actual falling metric.
* **New proved lemma:** explicit compact endpoint domination (6.3), with the resulting revised full-error budget (6.5).

## (2) Exact remaining bottleneck

The irrationality of $e+\pi$ remains unresolved.

For the weighted determinant route, even after eliminating an independent compact-size problem, no bound proves that


$$
\frac{\ell^k|Q(-1)|^k e^{O(n^{3/2})}D_k}{g}\longrightarrow0.
$$


The whole final gcd $g$, not only its dyadic part or moving-pole divisor, remains essential.

For the proportional route, the exceptional matching congruences and possible additional matching saturation are real unresolved local conditions. Their aggregate effect at the **same index**, together with the final scalar cancellation $\gcd(k,r)$, remains uncontrolled. The auxiliary $p=n+2$ calculation does not apply as a prime offset on the selected even-$n$ sequence.

## (3) Bounded computation or source request

**No new prime scan or degree atlas is requested.**

The already proposed single instance


$$
(n,p,b,m)=(15,17,6,1)
$$


is appropriate for auditing A5’s formulas. Its output should retain the exact matching-row saturation, the metric’s zeroth-coordinate rank-one contribution, and the fully reduced denominator if a center is reconstructed.

For independent verification of the weighted exact endpoint theorem, request only the already existing:

1. six full rational-Cartier state pairs witnessing $h_7=h_3$, including denominator phases;
2. four full linear-transfer state pairs witnessing step $11=$ step $3$, with their terminal and boundary tables;
3. the modulo-$8$ branch identity data from which the supplied moment chart is derived.

Expected output is coefficientwise equality under the stated deterministic transitions, followed by the complete residue reconstruction $U=4\pmod8$. These are bounded exact certificate checks; no new execution is authorized here.
