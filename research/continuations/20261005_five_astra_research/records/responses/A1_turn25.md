> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## Verdict

The proposed finite-boundary mechanism closes **for the core form**, and the retained precision-protection lemma transfers the result to the actual polynomial. The essential boundary fact is that monic division at the lower edge identifies the actual LOW projection at every required finite precision; this follows from a coefficient gap, not from assuming projection compatibility.

Here is a sufficient domain, with a slightly enlarged constant to simplify the width estimates. For each fixed integer $r\ge6$, require


$$
\boxed{
j>0,\quad v_3(j)\ge r-2,\quad n=4^j+1,\quad
H=3^{h-1},\quad
0<D=H-(n-2)<\frac{H}{C_r},\quad h\ge r+2,
}
$$


where


$$
\boxed{C_r=512(r+1)^2\,3^{r-1}.}
$$


On this domain, the actual normalized radical Schur form satisfies


$$
\boxed{\mathcal R_{\rm rad}\in3^r\operatorname{Mat}_{\nu}(\mathbb Z_3).}
$$



This is a fixed-depth divisibility theorem. It gives neither an exact denominator nor an irrationality proof.

---

## 1. Actual form and the precision used

Retain


$$
A=H-D,\quad d=\frac{3D}{2}-1,\quad
\nu=\frac D2-1,\quad m=\frac{A+1}{2},\quad
r_1=\frac{H-1}{2},\quad r_*=\frac{3H-1}{2}.
$$


The actual column space is


$$
\langle1,y,\ldots,y^m\rangle,
$$


with HIGH $d\le a\le m$, LOW unit columns $U=(1,\ldots,y^{D-1})$, and


$$
z_i=y^i(y-1)^D,\qquad0\le i<\nu.
$$



Only the primitive unit $\lambda=L_n/3$ is stripped. The complete functional remains


$$
\mathcal M(T)=
-\frac{3^h}{4}\mathfrak f(T)
+
\sum_{\substack{0\le a\le h\\ c\ge1\ {\rm odd},\,3\nmid c\\
c3^a\le4n-3}}
3^{h-a}c^{-1}
[y^{(c3^a-1)/2}]
\frac{T-T(-1)}{y+1}.
$$


In particular, every original cutoff and the factorial force are retained.

Write


$$
Q_c=(y+1)B_A(\beta+3y),\qquad B_A=(y-1)^A,
$$


and


$$
Q^{\rm loc}=Q_c+3^\tau T,\qquad \tau=v_3(j)+2\ge r.
$$


The retained precision-protection lemma gives


$$
\mathcal R_{\rm rad}(Q^{\rm loc})
\equiv\mathcal R_{\rm rad}(Q_c)\pmod{3^r}.
$$


Thus it suffices to prove the core assertion.

For the core, the factorial contribution is in $3^h$ before division by $3$, and in $3^{h-1}$ afterwards. Since $h-1\ge r+1$, it can be omitted in the following calculations modulo $3^r$, including the definitions of $L,X,F$. Perturbing their unit inverses preserves that precision. This is a precision reduction of the complete form, not a replacement metric.

---

## 2. A coefficient lemma with valuations

Put


$$
u=h-1,\qquad G=H/3^{r-1}.
$$


For $0<k<H$,


$$
v_3\binom Hk=u-v_3(k).
$$


Consequently, at precision $3^q$, $1\le q\le r$, $B_H=(y-1)^H$ is supported on multiples of


$$
G_q=H/3^{q-1}.
$$


The endpoint coefficients are units; an interior coefficient at $k$ has exactly the valuation displayed above.

For the inverse series,


$$
a_k=[z^k](1-z)^{-H}=\binom{H+k-1}{k},
$$


the identity


$$
a_k=\frac Hk\binom{H+k-1}{k-1}
$$


gives


$$
v_3(a_k)\ge u-v_3(k)\qquad(0<k<H).
$$


Thus, below degree $H$, this inverse series has the same support containment modulo $3^q$.

All coarser grids $G_q$ are odd multiples of $G$. It is therefore legitimate to use the common grid $G$ throughout, without discarding the coefficient valuations.

For a lower-pole term of weight $3^t$, only $B_H\bmod3^{r-t}$ is needed. If its selected coefficient has index


$$
\frac{cH/3^t-1}{2},
$$


subtracting an integer-grid exponent and a surviving $B_H$-exponent leaves a half-grid index. Indeed, in units $G/2$, the numerator is odd: the pole contributes $c3^{r-1-t}$, while polynomial-grid shifts contribute even integers. Terms $t\ge r$ vanish by their weights. This accounts individually for every admissible pole, without pairing or extending its cutoff.

---

## 3. Width budget

Use symmetric half-grid shifts $|s|\le w$. An internal polynomial has the form


$$
y^{kG+s}(y-1)^D,\qquad |s|\le w,
$$


and is required to lie wholly in HIGH. Edge width $w$ means the first or last $w+1$ HIGH coordinates.

The estimates below give:

* $R$: no increase in width;
* $F$ on an internal polynomial: increase at most $1$;
* $F$ on the lower edge: increase at most $\nu+1$;
* $R$ on the upper edge: no increase.

Start with


$$
w_0=\nu+1.
$$


After at most $r-2$ applications of $F$,


$$
w\le(r-1)(\nu+1)\le(r-1)D.
$$


For all auxiliary degree estimates, use the larger bound


$$
W=4(r+1)(D+2).
$$


On the stated domain $D\ge6$, and


$$
G>512(r+1)^2D.
$$


In particular,


$$
\boxed{W+2D+2<G/8.}
$$


This single inequality supplies every separation used below. It also ensures that all edge intervals used here are much shorter than HIGH.

---

## 4. Operation 1: the complete $V$-support

The core formula is


$$
V_{ia}=(ee_m^T)_{ia}
+\sum_{t=0}^{h-1}3^t
 B_t\!\left(B_H(\beta+3y)y^{i+a}\right)
\pmod{3^r}.
$$


Its top term is exactly the indicated corner: since


$$
i+a\le \nu-1+m=r_1-1,
$$


only the linear factor at the final radical/HIGH indices reaches the top coefficient after division by $3$.

Every lower term lies at a half-grid position with shift $-i-\epsilon$, $\epsilon\in\{0,1\}$, by Section 2. Thus $V$ has half-grid support of width $w_0$, plus the upper corner.

More strongly,


$$
\boxed{
V_{ia}=0\pmod{3^r}
\quad(0\le i<\nu,\ d\le a\le d+W).
}
$$


To verify this directly, the exponents $i+a+\epsilon$ lie in a low interval of length less than $W+2D+2<G/8$. Adding any surviving $B_H$-exponent gives an integer-grid band, whereas each retained pole is on the half-grid. The top corner is absent there.

This proves the required extended lower-edge annihilation at the actual precision.

---

## 5. Operation 2: $R$-images and their finite truncations

The exact inverse is


$$
R_{ab}=[z^{D+r_1-a-b}](1-z)^{-A}
=[z^{D+r_1-a-b}](1-z)^D(1-z)^{-H}.
$$


Every coefficient degree used in HIGH satisfies


$$
D+r_1-a-b\le D+r_1-2d<H.
$$


Section 2 therefore applies to the entire finite inverse.

For a basis input $e_b$, the term $a_{kG}z^{kG}$ of the inverse series gives, before HIGH intersection,


$$
a_{kG}\,y^{r_1-b-kG}(y-1)^D.
$$


Here $D$ is even, so reversing the coefficients of $(1-z)^D$ introduces no additional sign. The coefficient $a_{kG}$ retains the valuation bound of Section 2.

If


$$
b=\frac{(2l+1)G-1}{2}+s,
$$


then


$$
r_1-b-kG
=\left(\frac{3^{r-1}-2l-1}{2}-k\right)G-s.
$$


Thus the image consists of integer-grid polynomial copies with shift bounded by $w$.

The upper HIGH boundary has macroscopic center $H/2$, a half-grid center. An integer-grid polynomial of width $w+D<G/8$ cannot be partially cut there: it is either wholly inside or wholly outside.

At the lower boundary, only a copy centered at integer-grid center zero can be cut. Its largest exponent is at most $w+D$; its surviving HIGH part therefore lies in


$$
[d,w+D]\subseteq[d,d+w].
$$


Hence every such truncation belongs to the lower-edge module with no width increase. This explicitly resolves the finite truncation.

---

## 6. Operation 3: actual $F$ on internal polynomial copies

Let


$$
p=y^{kG+s}(y-1)^D
$$


be wholly in HIGH. Then


$$
B_Ap=B_Hy^{kG+s}.
$$



First consider its actual LOW force. For $u<D$, the top coefficient in $X_U p$ vanishes by the original degree bound. Every remaining coefficient extraction is a half-grid extraction from


$$
B_H(\beta+3y)y^{kG+s+u}.
$$


Its local shift has magnitude at most $w+D+1<G/8$, so


$$
\boxed{X_Up=0\pmod{3^r}.}
$$


Since $L_U^{-1}$ is integral, the actual LOW projection term in $Fp$ vanishes modulo $3^r$.

The remaining terms are


$$
c_0E_0p+
\bigl([y^{r_*}]yB_Apy^a\bigr)_a+
\left(\sum_t3^tB_t(B_Ap(\beta+3y)y^a)\right)_a,
\qquad c_0=(\beta-1)/3.
$$


Each is supported on the half-grid. The linear factor increases the shift width by at most one. Any finite upper-edge occurrence is already covered by the allowed upper-edge module.

No coefficient division occurs in this operation: $c_0\in\mathbb Z_3$, all pole units are integral, and the LOW correction has just been proved negligible at the required precision.

---

## 7. Operation 4: the actual lower-edge projection

Take $0\le s\le w$ and divide monically:


$$
y^{d+s}=r_s+(y-1)^Dq_s,\qquad \deg r_s<D,
$$


where explicitly


$$
q_s=\sum_{a=0}^{\nu+s}
\binom{D+a-1}{a}y^{\nu+s-a}.
$$


All coefficients are integral, and


$$
\deg q_s=\nu+s.
$$



For every $u<D$, the difference between the LOW force of $y^{d+s}$ and that of $r_s$ is extracted from


$$
B_H(\beta+3y)q_sy^u.
$$


Its nongrid shifts range from zero to at most


$$
\nu+w+D<W+2D.
$$


They cannot meet any retained half-grid extraction. Its top coefficient also vanishes by degree. Therefore


$$
X_Ue_{d+s}\equiv L_Ur_s\pmod{3^r},
$$


and hence


$$
\boxed{L_U^{-1}X_Ue_{d+s}\equiv r_s\pmod{3^r}.}
$$


This proves the actual projection identification uniformly through the required boundary width.

Substitution into the exact definition of $F$ gives


$$
Fe_{d+s}\equiv
c_0E_0e_{d+s}
+\bigl([y^{r_*}]yB_Ay^{a+d+s}\bigr)_a
+\left(\sum_t3^tB_t(B_H(\beta+3y)q_sy^a)\right)_a
\pmod{3^r}.
$$


The first term is supported in the last $s+1$ coordinates, and the second in the last $s+2$. The lower terms lie on half-grid bands with shifts between $-(\nu+s+1)$ and zero.

Thus this operation increases the width by at most $\nu+1$, with integral coefficients. This is the needed boundary closure.

---

## 8. Operation 5: the exact edge transport by $R$

For $b=m-s$,


$$
D+r_1-a-b=d+s-a.
$$


Consequently,


$$
R_{a,m-s}=0\qquad(a>d+s).
$$


Thus


$$
\boxed{R(\text{upper edge of width }w)
\subseteq\text{lower edge of width }w}
$$


exactly, over $\mathbb Z_3$. There is no new interior band and no width loss hidden in an infinite-series extension.

---

## 9. Complete Schur contraction

First, the same half-grid gap proves


$$
Z^TLZ\equiv0,\qquad Z^TLU\equiv0\pmod{3^r}.
$$


For these entries the top coefficient is absent by degree. Their lower extractions involve respectively


$$
B_H(\beta+3y)(y-1)^Dy^{i+l},
\qquad
B_H(\beta+3y)y^{i+u},
$$


whose shifts are bounded by $2D$. Thus this also proves the required direct-force precision.

After eliminating $U$, write


$$
\widetilde V=V-Z^TLU\,L_U^{-1}X_U.
$$


Then


$$
\widetilde V\equiv V\pmod{3^r},
$$


and the normalized radical form is


$$
\mathcal R_c=
Z^TLZ-Z^TLU\,L_U^{-1}U^TLZ
-3\widetilde V(E_0+3F)^{-1}\widetilde V^T.
$$



Modulo $3^r$, the inverse requires only


$$
(E_0+3F)^{-1}
=\sum_{a=0}^{r-2}(-3)^a(RF)^aR
$$


inside this expression; the omitted terms acquire valuation at least $r$ after its outer factor $3$.

By Operations 1–5, each retained walk sends $V^T$ into internal integer-grid copies plus lower-edge vectors, within the width budget. The left $V$ annihilates:

* the internal copies by the integer/half-grid gap, including separation from its upper corner;
* the lower-edge vectors by the direct vanishing proved in Section 4.

Hence every retained closed contraction is zero modulo $3^r$. The direct LOW terms already vanish at that precision. Therefore


$$
\mathcal R_c\in3^r\operatorname{Mat}_{\nu}(\mathbb Z_3).
$$


Precision protection now proves the asserted theorem for $Q^{\rm loc}$, and restoring $\lambda$ preserves it.

---

## 10. Endpoint and primitive arithmetic

The actual transported endpoint must still be computed from the actual eliminated columns, not from uncorrected geometric columns. Its retained residue is


$$
e_{\rm rad}\equiv((-1)^i)_{0\le i<\nu}\ne0\pmod3.
$$


The actual-polynomial perturbation changes the transported columns only in $3^{\tau-1}$, so this residue is protected. The theorem does **not** evaluate


$$
3^{-r}\mathcal R_{\rm rad}\pmod3
$$


or its endpoint image.

No new numerical final-gcd exponent is asserted without the corresponding coefficient-pair normalization argument. Retain the already justified bound on the applicable subclass, rather than subtracting unrelated determinant and cofactor lower bounds.

For the complete integer pair,


$$
g=\gcd(|A_{\rm det}|,|B_{\rm det}|).
$$


When $B_{\rm det}\ne0$,


$$
q=\frac{|B_{\rm det}|}{g},\qquad
p=-\frac{\operatorname{sgn}(B_{\rm det})A_{\rm det}}g,
$$


and the **whole** primitive error is


$$
\boxed{
q(e+\pi)-p
=\frac{\operatorname{sgn}(B_{\rm det})\ell^{(n+1)/2}}g
\det H_{\rm complete}.
}
$$


The primitive multiplier is $\ell^{(n+1)/2}/g$. Neither response nonvanishing nor whole-error nonvanishing follows from this fixed-depth support theorem.

### Closing ledger

1. **New result and proof status.** Proved: all five finite-boundary operations, including integral coefficient control, explicit lower truncations, actual LOW-projection identification, and a uniform width budget. Consequently, for each fixed $r\ge6$, the actual normalized radical Schur form is divisible by $3^r$ on the displayed domain with $C_r=512(r+1)^2 3^{r-1}$.

2. **Exact remaining bottleneck.** The first possibly nonzero divided radical, its transported distinguished cofactor, and the relative final coefficient-pair content remain unevaluated. Fixed-depth divisibility does not control the actual reduced denominator on indices supporting nonzero whole primitive errors tending to zero. Irrationality of $e+\pi$ remains unresolved.

3. **Computation request.** None. The closure proof is symbolic and uniform; no finite rank scan is used as evidence for the theorem.
