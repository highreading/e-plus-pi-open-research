> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3, Turn 14 — Natural observation transfer, exact block remainders, and the saturated resonance budget

## Executive summary

The irrationality of $e+\pi$ remains unresolved.

This turn obtains a simpler transfer for the **actual alignment observations**, an exact fixed-seed description of the remainder obstructing multiplicative-block Bézout propagation, and a sharper combination of A4’s saturation theorem with seed subtraction.

The principal new results are:

1. **The actual three observations $(P_n,Q_n,F_n)$ close under a particularly simple parameter-$n$ transfer.** Writing
   

$$
m=n+1,\qquad N=n+2,\qquad H=n^2+3n+1,
$$


   the transfer is
   

$$
\boxed{
   \begin{pmatrix}P_{n+1}\\Q_{n+1}\\F_{n+1}\end{pmatrix}
   =
   \begin{pmatrix}
   0&mN&N/2\\
   N&-H&-nN/(2m)\\
   -N(2n+3)&NH&N(n^2-2)/(2m)
   \end{pmatrix}
   \begin{pmatrix}P_n\\Q_n\\F_n\end{pmatrix}.
   }
   \tag{E1}
$$


   Its determinant is
   

$$
\boxed{\frac{(n+1)(n+2)^2(n+3)}2.}
$$


   This is a change to natural observation coordinates in the genuine fixed-seed realization—not an arbitrary companion system.

2. **The multiplicative-block propagation attempt has an exact evaluated remainder.** For $t=bn$, $b\in\{15,105\}$, backward propagation gives
   

$$
\boxed{
   \binom{F_n}{M_n/L_n}
   =
   \mathbf A_{b,n}F_t+
   \mathbf B_{b,n}(M_t/L_t)
   +\sigma_t\,\boldsymbol\delta_{b,n}.
   }
   \tag{E2}
$$


   Here $\boldsymbol\delta_{b,n}$ is an explicit backward-transported reference-line defect. Crucially, the **actual fixed seed** implies that $\sigma_t$ is a unit modulo the terminal alignment ideal. Thus the last term cannot be discarded by appealing to state primitivity.

   I do **not** prove that this remainder can be paid with a cofactor of logarithmic height $O(n)$.

3. **A genuine, but limited, support-and-cost result follows for adjacent indices.** The common large-prime alignment depth at $n$ and $n+1$ divides
   

$$
\boxed{(2n+3)(n^2+8n+11).}
   \tag{E3}
$$


   Its logarithmic cost is $O(\log n)$. This proves that deep adjacent alignments are exceptional. It does **not** bound $\mathcal I_{15^r}$ or $\mathcal I_{105^r}$: separated indices can realign.

4. **A4’s full-depth saturation theorem eliminates the extra moment/contact gcd from Turn 13’s excess budget.** After exact seed subtraction, let
   

$$
\mathfrak X_j
   =
   \prod_{p>N}p^{(v_p(\Delta_j)-v_p(\mathcal E_j^\circ))_+},
   \qquad
   \mathfrak S_j
   =
   \prod_{p>N}p^{(v_p(\Delta_j)-v_p(F))_+}.
$$


   Then
   

$$
\boxed{
   \mathfrak X_j=\mathfrak S_j\,\mathfrak U_j,
   \qquad
   \mathfrak U_j\mid\mathcal I_n.
   }
   \tag{E4}
$$


   Thus only alignment and the **actual saturated unit charts** need payment. The additional factor $\gcd(M,\gamma_j)_{>N}$ from the earlier nonresonant estimate is no longer needed.

5. **There is an exact obstruction to obtaining another factorial-height saving merely by absorbing the logarithmic constant into a seed-adjusted force pair.** Put
   

$$
\mathscr K_n^\circ
   =\widehat h B^\circ-\widehat\ell A^\circ,
   \qquad
   \Xi_n=\kappa-\mathscr K_n^\circ.
$$


   Then, along the original families,
   

$$
\boxed{
   \log|\Xi_n|
   =
   2\log(n!)+\frac{n+3}{2}\log2+o(1).
   }
   \tag{E5}
$$


   Any absorption of this transverse logarithmic term into a two-coordinate force pair, while retaining $C=mZ$, must have coefficient height at least
   

$$
\boxed{2\log(n!)-O(n).}
$$


   This is a height obstruction to that particular repair. It is **not** a lower bound for the large-prime resonance content.

The requested subfactorial multiplicative-block alignment estimate and the requested saturated-resonance cost estimate remain unproved. No new finite alignment sample is substituted for either lemma.

---

# 1. Scope and source assessment

The approximation domain remains


$$
\boxed{
n=15^r\quad\text{or}\quad n=105^r,\qquad r\ge2.
}
$$


As before,


$$
m=n+1,\qquad N=n+2,\qquad L=2^{m/2}.
$$



Auxiliary consecutive indices below are used only to describe and prove a recurrence. They do not enlarge the approximation domain or alter any finite contact or forcing boundary.

I retain the actual definitions


$$
X=ma_n,\qquad Y=mna_{n-1},\qquad Z=2a_{n+1}-ma_n,
$$




$$
P=nX+Y,\qquad Q=nZ+2X-Y,
$$




$$
F=2m\bigl(Y-2X-(n-1)Z\bigr)=2m(Z-Q),
$$


and


$$
\widehat h=L\tau_n,\qquad
\widehat\ell=L\tau_{n+1},\qquad
M=Q\widehat h-P\widehat\ell.
$$


Thus


$$
\mathcal I_n=\gcd(|F|,|M|)_{>N}.
$$



## 1.1 Results reused at their proved scope

I reuse:

- the diagonal generating-function identities;
- the genuine diagonal seeds
  

$$
D_0,D_1,D_2=1,0,1;
$$


- the third-order recurrence beginning at $3$;
- the nine-coordinate realization;
- the finite integral Green formula, including its terminal coefficient $1$;
- exact seed subtraction;
- the three complete affine identities;
- the actual coordinate-content payment
  

$$
\eta_j\mid2N^2;
$$


- the exact local ideal equality and divisibility chain;
- A4’s full-depth saturation theorem and its actual unit-chart formulas.

The convolution


$$
\mathscr A=\mathscr J/s
$$


is not cancelled at an evaluated coefficient.

A4’s corrected binary logarithmic-source identification is valid at its stated binary scope. Its binary norm and prefix results are not imported into the present endpoint family.

## 1.2 Closed finite receipts

The accepted facts remain


$$
\gcd(F,M)_{3375}=128,\qquad \mathcal I_{3375}=1,
$$


and


$$
\gcd(F,M)_{11025}=8,\qquad \mathcal I_{11025}=1.
$$


At $3375$, the retained filters also give


$$
\Delta_0=\Delta_3=\mathcal G=1.
$$



No receipt is repeated, extended to an infinite family, or treated as a complete-force calculation at $11025$.

No C-finite recurrence gcd theorem is used. The recurrence here has polynomial coefficients and a singular lower boundary; no matching theorem with the required hypotheses has been supplied.

---

# 2. A natural three-coordinate transfer for the actual observations

The nine-coordinate realization can be made more transparent by replacing its moment coordinates with the actual observations $(P,Q,F)$.

To distinguish parameter-diagonal moments from the force series, write


$$
D_n=a_n(n),\qquad B_n=a_{n-1}(n).
$$



The established coefficient identities give


$$
B_{n+1}=D_{n+1}+(n+1)D_n-n(n+1)B_n.
\tag{2.1}
$$


They also imply


$$
\boxed{
D_{n+2}
=
-\frac{3(n+1)}2D_{n+1}
+\frac{(n+1)^2}{2}(D_n+B_{n+1}).
}
\tag{2.2}
$$



### Derivation of (2.2)

Use the established identity


$$
(k+1)D_k+(k-1)B_k
+2k(k-1)D_{k-1}
-k(k-1)^2D_{k-2}=0
$$


at $k=n+2$, and substitute


$$
B_{n+2}
=
D_{n+2}+(n+2)D_{n+1}
-(n+2)(n+1)B_{n+1}.
$$


After division by $2(n+2)$, this is exactly (2.2). No singular initial step is used.

Recall


$$
Z_n=2D_{n+1}+(n+1)D_n-n(n+1)B_n.
$$


Equation (2.1) immediately yields the useful identity


$$
\boxed{P_{n+1}=(n+1)(n+2)Z_n.}
\tag{2.3}
$$



Using (2.2) and the definitions of $P,Q,F$, one obtains


$$
\boxed{
Z_{n+1}
=
\frac12P_n-\frac{n^2+3n+1}{2}Z_n-\frac14F_n,
}
\tag{2.4}
$$


and


$$
\boxed{
Q_{n+1}
=
(n+2)P_n-(n^2+3n+1)Z_n+\frac12F_n.
}
\tag{2.5}
$$



Substitute


$$
Z_n=Q_n+\frac{F_n}{2(n+1)}
$$


and use $F_{n+1}=2(n+2)(Z_{n+1}-Q_{n+1})$.

## Theorem 2.1 — Natural observation transfer

For every auxiliary $n\ge2$,


$$
\boxed{
z_{n+1}=\mathsf U_nz_n,\qquad
z_n=(P_n,Q_n,F_n)^T,
}
$$


where


$$
\boxed{
\mathsf U_n=
\begin{pmatrix}
0&(n+1)(n+2)&(n+2)/2\\[1mm]
n+2&-(n^2+3n+1)&-\dfrac{n(n+2)}{2(n+1)}\\[2mm]
-(n+2)(2n+3)&(n+2)(n^2+3n+1)&
\dfrac{(n+2)(n^2-2)}{2(n+1)}
\end{pmatrix}.
}
\tag{2.6}
$$


Its determinant is


$$
\boxed{
\det\mathsf U_n
=
\frac{(n+1)(n+2)^2(n+3)}2.
}
\tag{2.7}
$$



The actual lower state is


$$
\boxed{z_2=(0,10,-66)^T.}
\tag{2.8}
$$



These are identities for the original fixed-seed diagonal family.

### Consequences

For a block $n\le k<t$, every denominator of $\mathsf U_k$, and every prime in its determinant, is at most $t+2$. Therefore


$$
\mathsf W_{n,t}
=
\mathsf U_{t-1}\cdots\mathsf U_n
$$


lies in


$$
\operatorname{GL}_3(\mathscr R_t),
\qquad
\mathscr R_t=\mathbb Z[1/p:p\le t+2].
\tag{2.9}
$$



The actual seed (2.8), together with these invertible transfers, proves that


$$
(P_n,Q_n,F_n)
$$


is primitive at every prime $p>n+2$. This is full-state primitivity only.

The nine-coordinate realization now has the equivalent natural form


$$
z_n\oplus(z_n\otimes y_n),
\qquad
y_n=(\tau_{n+1},\tau_n)^T.
$$


In these coordinates the two alignment observations are simply $F_n$ and


$$
\overline M_n:=Q_n\tau_n-P_n\tau_{n+1}.
$$


At original indices,


$$
M_n=L_n\overline M_n,
$$


and $L_n$ is a unit at all primes under consideration.

---

# 3. Exact multiplicative-block propagation—and its fixed-seed remainder

Take


$$
t=bn,\qquad b\in\{15,105\}.
$$


All constructions in this section take place in $\mathscr R_t$.

Define


$$
v_t=(\tau_t,\tau_{t+1},0)^T.
$$


The reference pair is primitive in $\mathscr R_t$, so there exist $u_t,v_t^\flat\in\mathscr R_t$ satisfying


$$
u_t\tau_t+v_t^\flat\tau_{t+1}=1.
$$


Put


$$
w_t=(-v_t^\flat,u_t,0)^T,
\qquad
\sigma_t=u_tP_t+v_t^\flat Q_t.
$$


Then the following is an exact decomposition of the actual terminal state:


$$
\boxed{
z_t=\sigma_tv_t+\overline M_tw_t+F_te_3.
}
\tag{3.1}
$$



Let


$$
\mathsf O_n=
\begin{pmatrix}
0&0&1\\
-\tau_{n+1}&\tau_n&0
\end{pmatrix}.
$$


Define the explicit block defect


$$
\boxed{
\boldsymbol\delta_{b,n}
=
\mathsf O_n\mathsf W_{n,t}^{-1}v_t.
}
\tag{3.2}
$$



Backward propagation of (3.1) gives:

## Theorem 3.1 — Actual evaluated block-remainder identity



$$
\boxed{
\binom{F_n}{\overline M_n}
=
\bigl(\mathsf O_n\mathsf W_{n,t}^{-1}e_3\bigr)F_t
+
\bigl(\mathsf O_n\mathsf W_{n,t}^{-1}w_t\bigr)\overline M_t
+
\sigma_t\boldsymbol\delta_{b,n}.
}
\tag{3.3}
$$



All coefficients belong to $\mathscr R_t$. The remainder is evaluated on the actual transported state.

Moreover,


$$
\boxed{
(F_t,\overline M_t,\sigma_t)=\mathscr R_t.
}
\tag{3.4}
$$



### Proof of the unit assertion

The matrix with columns $v_t,w_t,e_3$ has determinant $1$. Thus


$$
(P_t,Q_t,F_t)
\quad\text{and}\quad
(\sigma_t,\overline M_t,F_t)
$$


generate the same ideal. Actual fixed-seed primitivity proves (3.4). ∎

This is the point at which the genuine seed matters. At a prime dividing both terminal observations, $\sigma_t$ is a unit. It cannot supply an uncharged cancellation of the remainder.

In particular,


$$
\boxed{
(F_t,\overline M_t,F_n,\overline M_n)
=
(F_t,\overline M_t,\delta_{b,n,1},\delta_{b,n,2})
}
\tag{3.5}
$$


in $\mathscr R_t$.

Equation (3.3) is the attempted Bézout propagation identity with its missing term displayed. Multiplying by $L_n,L_t$, which are units in this ring, converts it to the original $M_n,M_t$ normalization.

## 3.1 What must be paid

At $p>t+2$, write


$$
a_s=\min\{v_p(F_s),v_p(M_s)\},
\qquad
d_p=\min_i v_p(\delta_{b,n,i}).
$$


Then (3.5) gives


$$
\min(a_n,a_t)=\min(a_t,d_p).
\tag{3.6}
$$



Consequently, a cofactor $c_{b,n}$ in the proposed identities (5.1) must pay at least


$$
\boxed{
v_p(c_{b,n})\ge(a_t-d_p)_+.
}
\tag{3.7}
$$



This is an exact obstruction interface, **not** a height estimate. I have not proved that the sum of these compulsory payments is $O(n)$, or even $o(n\log n)$.

The useful repair is now specific: control the backward reference-line defect (3.2) against terminal alignment, rather than trying to deduce observed primitivity from the block determinant.

---

# 4. A proved local obstruction: adjacent alignment has only polynomial common cost

The natural transfer also gives a target-specific theorem that is stronger than a generic rank warning, although weaker than the assigned multiplicative-block bound.

Write


$$
h=\tau_n,\qquad \ell=\tau_{n+1},
\qquad H=n^2+3n+1.
$$


Apply $\mathsf U_n$ to the actual reference direction $(h,\ell,0)^T$.

Its next $F$-observation is


$$
\boxed{
(n+2)\bigl(-(2n+3)h+H\ell\bigr).
}
\tag{4.1}
$$


Its next alignment observation is


$$
\boxed{
\ell\bigl((1-n-n^2)h-(n+2)(3n+2)\ell\bigr).
}
\tag{4.2}
$$



These expressions use the actual reference recurrence


$$
(n+2)\tau_{n+2}=(2n+3)\tau_{n+1}+(n+1)\tau_n.
$$



For $n\ge2$, the first expression is positive and the second negative: $\ell>h>0$, $H>2n+3$, and $1-n-n^2<0$. Thus the actual reference line is not an invariant alignment line, even over $\mathbb Q$.

More importantly, the two expressions have a paid common-content bound.

## Theorem 4.1 — Adjacent alignment isolation

For $n\ge2$, define


$$
\mathcal A_n^{\rm adj}
=
\prod_{p>n+3}
p^{\min\{v_p(F_n),v_p(\overline M_n),
v_p(F_{n+1}),v_p(\overline M_{n+1})\}}.
$$


Then


$$
\boxed{
\mathcal A_n^{\rm adj}
\mid
\bigl((2n+3)(n^2+8n+11)\bigr)_{>n+3}.
}
\tag{4.3}
$$


Hence


$$
\boxed{\log\mathcal A_n^{\rm adj}=O(\log n).}
\tag{4.4}
$$



### Proof

The fixed-seed decomposition from Section 3, now used forward for one step, shows that common alignment at $n,n+1$ is bounded by the common valuation of (4.1)–(4.2).

Set


$$
c=2n+3,\quad
a=1-n-n^2,\quad
b=(n+2)(3n+2).
$$


The relevant expressions, after removing the unit $n+2$, are


$$
-ch+H\ell,\qquad \ell(ah-b\ell).
$$



If $\ell$ is a unit, the common depth is bounded by the determinant


$$
cb-Ha
=
\boxed{(n+1)^2(n^2+8n+11)}.
\tag{4.5}
$$


Since $(h,\ell)$ is primitive, this follows by applying the adjugate of the corresponding $2\times2$ matrix.

If $p\mid\ell$, then $h$ is a unit. Unless $p\mid c$, the first expression is a unit. If $p\mid c$, then


$$
4a\equiv1\pmod c,
$$


so $a$ is a unit at $p$. The second expression has valuation $v_p(\ell)$, and


$$
\min\{v_p(-ch+H\ell),v_p(\ell)\}
=
\min\{v_p(c),v_p(\ell)\}
\le v_p(c).
$$


This proves (4.3). ∎

### Exact limitation

This theorem proves an $O(\log n)$ cost for **adjacent common alignment**, not for either individual alignment.

It does not imply


$$
\log\mathcal I_n=o(n\log n).
$$


In particular, the geometric targets $n$ and $15n$, or $n$ and $105n$, are not adjacent. Alignment may disappear and subsequently reappear. The block defect (3.2) retains precisely that possibility.

Thus (4.3) is a genuine support/cost restriction, but it is not accepted here as a substitute for the requested multiplicative-block lemma.

---

# 5. Combining seed subtraction with A4’s full saturation theorem

For each actual primitive contact row $r_j$, $j=0,3$, retain


$$
\alpha_j=r_jv',\qquad
\beta_j=r_jw',\qquad
\gamma_j=r_je_2,
$$


and


$$
P\alpha_j+Q\beta_j+F\gamma_j=0.
$$



The seed-subtracted projection is


$$
\mathcal E_j^\circ
=
A^\circ\alpha_j+B^\circ\beta_j+mZ\gamma_j,
$$


where


$$
A^\circ=\frac m2b_n,\qquad
B^\circ=b_{n+1}-\frac m2b_n.
$$


The exact relation remains


$$
\mathcal E_j-\mathcal E_j^\circ
=
E_n\frac{mn!}{2L}\widehat R_j.
\tag{5.1}
$$



Thus the complete affine identities and local elimination remain valid after this substitution, with the appropriately seed-subtracted coefficients. In particular,


$$
\min\{v_p(\Delta_j),v_p(\mathcal E_j)\}
=
\min\{v_p(\Delta_j),v_p(\mathcal E_j^\circ)\}.
\tag{5.2}
$$



## 5.1 The moment scalar is nonzero throughout the original domain

A small additional fixed-seed fact removes the $F=0$ branch here.

## Proposition 5.1
For every odd $n>2$,


$$
\boxed{F_n\equiv-2\pmod n.}
\tag{5.3}
$$


In particular, $F_n\ne0$ and $\gcd(F_n,n)=1$.

### Proof

Write


$$
q(z)^n=\sum_s c_sz^s,\qquad c_s\in\mathbb Z[1/2].
$$


Then


$$
a_n=\sum_s(n)_sc_s\equiv1\pmod n.
$$


Also,


$$
a_{n+1}
=
1+(n+1)c_1+\sum_{s\ge2}(n+1)_sc_s
\equiv1\pmod n,
$$


because $c_1=-n$, and $(n+1)_s$ contains $n$ for $s\ge2$. Reduction in $\mathbb Z[1/2]$ is legitimate because $n$ is odd.

Therefore $X\equiv Z\equiv1$, $Y\equiv0\pmod n$, giving (5.3). ∎

## 5.2 Full excess, not merely clipped overlap

Fix $p>N$, and write


$$
k=v_p(\Delta_j),\quad
f=v_p(F),\quad
e=v_p(\mathcal E_j^\circ),
$$




$$
a=v_p(\mathcal I_n),\qquad
\zeta=v_p(\mathcal Z_j).
$$



The retained chain gives


$$
\zeta\le\min(k,e),
\qquad
\min(k,f)\le a+\zeta.
\tag{5.4}
$$



A4’s saturation theorem, applied after the exact seed substitution, gives


$$
\boxed{
k>f\quad\Longrightarrow\quad
f=a+\zeta,\qquad e=\zeta.
}
\tag{5.5}
$$



Define


$$
s=(k-f)_+.
$$


If $s>0$, then


$$
(k-e)_+=a+s.
$$


If $s=0$, equations (5.4) give


$$
(k-e)_+\le a.
$$



We therefore obtain:

## Theorem 5.2 — Exact alignment-plus-saturation payment

For every $p>N$,


$$
\boxed{
(k-e)_+=s+u,\qquad 0\le u\le a.
}
\tag{5.6}
$$


When $s>0$, one has $u=a$.

Equivalently,


$$
\boxed{
\mathfrak X_j=\mathfrak S_j\,\mathfrak U_j,
\qquad
\mathfrak U_j\mid\mathcal I_n.
}
\tag{5.7}
$$



This improves the Turn 13 organization of the excess. The extra nonresonant factor


$$
\gcd(M,\gamma_j)_{>N}
$$


is unnecessary once A4’s full saturation theorem is available.

The whole depth also satisfies


$$
\boxed{
\Delta_j\mid\mathcal I_n\mathcal Z_j\mathfrak S_j.
}
\tag{5.8}
$$


Consequently,


$$
\log(\Delta_0\Delta_3)
\le
2\log\mathcal I_n
+\log(\mathcal Z_0\mathcal Z_3)
+\log(\mathfrak S_0\mathfrak S_3).
\tag{5.9}
$$



This is a full-depth statement, not a new clipped gcd.

## 5.3 Exactly which resonance charts remain

Only A4’s saturated charts contribute to $\mathfrak S_j$.

On positive-force saturation,


$$
e=\zeta>0,\qquad f=a+\zeta,\qquad a=v_p(M),
$$


and $\gamma_j$ is a unit. With the actual seeded projection,


$$
\Omega_{\gamma,j}
=
\frac{M\mathcal E_j^\circ}{\kappa F\gamma_j}
\in\mathbb Z_p^\times,
$$


one has


$$
\boxed{
s=
\min\left\{
(v_p(\widehat R_j)-f)_+,\,
v_p(1+\Omega_{\gamma,j})
\right\}.
}
\tag{5.10}
$$



On unit-force saturation, the actual unit $\alpha_j$ or $\beta_j$ is used:


$$
\Omega_{\alpha,j}
=\frac{\widehat\ell\,\mathcal E_j^\circ}{\kappa\alpha_j},
\qquad
\Omega_{\beta,j}
=-\frac{\widehat h\,\mathcal E_j^\circ}{\kappa\beta_j}.
\tag{5.11}
$$


The same formula holds with the admissible chart. If its $\Omega$ is not a unit, there is no excess.

The generic all-unit chart remains included. No term involving $\kappa$ has been removed.

---

# 6. The Green boundary can be tied more tightly to the actual moment state

The established Green formula is


$$
b_k=-h_k+\sum_{i=0}^{k-1}\mathsf G_{k,i}F_i,
\qquad
\mathsf G_{k,k-1}=1.
\tag{6.1}
$$


Here $F_i$ denotes the original force coefficient, not the scalar $F$.

Since $h_1=\omega_1=1$, its next-to-terminal coefficient is also explicit:


$$
\boxed{\mathsf G_{k,k-2}=2k-1.}
\tag{6.2}
$$



The final force coefficients entering $b_n,b_{n+1}$ are not freely variable. The actual moment recurrence gives:

## Proposition 6.1 — Actual final-source identities



$$
\boxed{
F_{n-1}=\frac{Y-X+Z}{n},
\qquad
F_n=\frac{3X-Y-Z}{2}.
}
\tag{6.3}
$$



The quotients are exact integers for the actual source.

### Derivation

Substitute the fixed-parameter moment recurrence into the stated complete formula for $F_{n-1}$ and $F_n$. For example,


$$
F_n
=
(2n+1)a_n-n^2a_{n-1}
-\frac{n(n-1)}2a_{n-2}.
$$


Using


$$
a_{n+1}
=
a_n+\frac{n(n-1)}2a_{n-1}
+\frac{n(n-1)}2a_{n-2}
$$


gives


$$
F_n=2ma_n-a_{n+1}-\frac{mn}{2}a_{n-1}
=\frac{3X-Y-Z}{2}.
$$


The first identity follows similarly. ∎

It follows that the complete seed-subtracted contact projection equals


$$
\begin{aligned}
\mathcal E_j^\circ={}&
-\frac m2(\alpha_j-\beta_j)h_n-\beta_jh_{n+1}\\
&+\sum_{i=0}^{n-2}
\left[
\frac m2(\alpha_j-\beta_j)\mathsf G_{n,i}
+\beta_j\mathsf G_{n+1,i}
\right]F_i\\
&+\left(\frac m2\alpha_j+\frac{3n+1}{2}\beta_j\right)
\frac{Y-X+Z}{n}\\
&+\frac{\beta_j}{2}(3X-Y-Z)+mZ\gamma_j.
\end{aligned}
\tag{6.4}
$$



This is an exact fixed-source expression. It pays both final source terms instead of treating them as adjustable forcing.

### What this does not prove

Equation (6.4) does not establish a small residue against $-\kappa$, or a bound on the saturated unit-cancellation depths.

It does identify a concrete repair requirement: any proposed Green-based resonance argument must exploit arithmetic of the actual prefix in (6.4), its displayed moment boundary, and the actual primitive contact row. The unit terminal coefficient prevents an automatic valuation gain from triangularity alone.

The physical source still runs through


$$
K=2n+2.
$$


The Green solution through $b_{K+1}$ still contains $F_K$ with coefficient $1$, and the original terminal-return functional is applied unchanged. Formula (6.4) neither shortens that physical source nor appends a new recurrence row.

---

# 7. A target-specific obstruction to another factorial-height saving

The seed-subtracted coefficients satisfy


$$
|A^\circ|+|B^\circ|\le n!\,e^{O(n)}.
\tag{7.1}
$$


The reference coefficients satisfy


$$
|\widehat h|+|\widehat\ell|\le e^{O(n)}.
\tag{7.2}
$$



Define


$$
\mathscr K_n^\circ
=
\widehat hB^\circ-\widehat\ell A^\circ,
\qquad
\Xi_n=\kappa-\mathscr K_n^\circ,
\qquad
\kappa=2L(n!)^2.
\tag{7.3}
$$


The canonical scalar is exactly


$$
\boxed{\Theta=mZM+F\Xi_n.}
\tag{7.4}
$$



## Theorem 7.1 — Size of the retained transverse logarithmic term

Along either original family,


$$
\boxed{
\Xi_n=\kappa\left(1+O\!\left(\frac{e^{Cn}}{n!}\right)\right)
}
\tag{7.5}
$$


for some fixed $C$. In particular, $\Xi_n>0$ for all sufficiently large original $n$, and


$$
\boxed{
\log|\Xi_n|
=
2\log(n!)+\frac{n+3}{2}\log2+o(1).
}
\tag{7.6}
$$



### Proof

Equations (7.1)–(7.2) give


$$
|\mathscr K_n^\circ|\le n!e^{Cn}.
$$


Divide by


$$
\kappa=2^{(n+3)/2}(n!)^2.
$$


The relative error tends to zero faster than any fixed exponential reciprocal. ∎

The homogeneous seed gauge


$$
(A^\circ,B^\circ)\longmapsto
(A^\circ+s\widehat h,\ B^\circ+s\widehat\ell)
$$


does not change $\mathscr K_n^\circ$.

Suppose one tries to absorb the complete logarithmic term into another force pair $(A^*,B^*)$, while retaining $C=mZ$, so that


$$
\widehat hB^*-\widehat\ell A^*=-\Xi_n.
\tag{7.7}
$$


Then


$$
|\Xi_n|
\le
(|\widehat h|+|\widehat\ell|)
\max\{|A^*|,|B^*|\}.
$$


Hence:

## Corollary 7.2 — Fixed-$C$ absorption obstruction

Every such pair satisfies


$$
\boxed{
\log\max\{|A^*|,|B^*|\}
\ge
2\log(n!)-O(n).
}
\tag{7.8}
$$



Thus a seed adjustment cannot turn the **complete** affine force into a pair of height $\log(n!)+O(n)$ while leaving the transverse logarithmic contribution unchanged.

### Scope of the obstruction

This does not prove that every possible cross-index arithmetic argument fails. In particular:

- it does not exclude a genuine divisibility or support theorem for the evaluated resonance;
- it does not bound the large-prime part of $\Xi_n$;
- it does not prove that the actual resonance budget is factorial;
- it does not authorize uncharged syzygy gauges or new denominators.

The important distinction is that a large integer may have only small-prime support. Theorem 7.1 is an exact height statement, not a support theorem.

Accordingly, the new transfer has **not** removed another actual factorial-height term from the resonance budget. The seed-induced saving from Turn 13 remains valid; the complete logarithmic term remains paid.

---

# 8. The outstanding arithmetic lemmas, now with explicit interfaces

## 8.1 Multiplicative-block alignment

The concrete identity available is (3.3). To obtain the proposed Bézout propagation with $\log c_{b,n}=O(n)$, one must pay the actual term


$$
\sigma_t\boldsymbol\delta_{b,n},
$$


where


$$
\boldsymbol\delta_{b,n}
=
\mathsf O_n
(\mathsf U_{t-1}\cdots\mathsf U_n)^{-1}
(\tau_t,\tau_{t+1},0)^T.
$$



The fixed seed makes $\sigma_t$ a unit on terminal alignment. The determinant cannot pay the defect.

The adjacent theorem proves that short-lived alignment has a polynomial common cost. It supplies no estimate for reappearance after a multiplicative block.

**Remaining alignment obligation:** prove a paid backward-observation identity, or another genuine subfactorial support/height restriction, on infinitely many original geometric indices.

Neither


$$
\mathcal I_n=1
$$


nor


$$
\log\mathcal I_n=o(n\log n)
$$


is established here.

## 8.2 Saturated unit resonance

After Theorem 5.2, the exact unpaid contribution is


$$
\boxed{
\log(\mathfrak S_0\mathfrak S_3)
=
\sum_{j=0,3}\sum_{p>N}
\min\left\{
(v_p(\widehat R_j)-v_p(F))_+,\,
v_p(1+\Omega_{j,p})
\right\}\log p,
}
\tag{8.1}
$$


where only A4’s admissible saturated charts contribute.

The new Green boundary identities ensure that its force argument is the actual fixed-source evaluation. They do not yet bound (8.1).

**Remaining resonance obligation:** prove


$$
\log(\mathfrak S_0\mathfrak S_3)=o(n\log n)
$$


on a suitable infinite original subsequence, using the evaluated contact row and the complete force—including $\kappa$ and the physical terminal.

No generic resultant or reformulation of (8.1) is counted as such a proof.

---

# 9. Construction, contents, normalization, and error remain unchanged

The arithmetic advances above do not change the producer.

## 9.1 Actual rows and complete filtering

The rows $r_0,r_3$ remain the actual primitive contact rows. No raw adjugate row is substituted.

The source content $\mathcal B_n$, full collision depth $\Sigma_n$, reference collision ceiling $H_n^{\rm ref}$, exclusive filters $V_{j,n}$, and $\mathcal W_n^{\rm ref}$ retain their definitions and full valuations.

In particular:

- source content is removed before collision comparison;
- full collision depth, not its radical, is removed from the references;
- contact-coordinate content, moment/contact overlap, and reconstructed row content remain distinct;
- no stronger existing certificate is “improved” by intersecting it again with a weaker one.

## 9.2 Complete finite forcing

The original force remains


$$
F_k=(n+1)a_k-nk\,a_{k-1}
+\frac{(n-1)k(k-1)}2a_{k-2}
+\frac{k(k-1)(k-2)}2a_{k-3}
$$


through


$$
\boxed{K=2n+2,}
$$


with the complete retained terminal return.

The complete endpoint residual is still


$$
\boxed{
C_j^{\rm complete}
=
\mathcal E_j^\circ
+
2n!m!(\alpha_j\rho_n+\beta_j\rho_{n+1}).
}
\tag{9.1}
$$


It is not replaced by $\mathcal E_j^\circ$.

## 9.3 Both corrected columns and all eight reconstructed entries

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


and


$$
u=(-sx_0,\ sx_0-sx_1,\ sx_1-sx_2,\ sx_2),
$$




$$
v=(1-sy_0,\ sy_0-sy_1,\ sy_1-sy_2,\ sy_2).
$$


The exterior $+1$ remains.

The least simultaneous clearer is over all eight entries, followed by the actual two-entry row-content divisions. The accepted $3375$ contents remain


$$
(113940000,\ 9780750,\ 10125,\ 1).
$$



## 9.4 All-prime primitive normalization

The endpoint denominator remains


$$
\boxed{
d_j=
\frac{|n!R_j|}
{\gcd(|n!R_j|,\ |E_nR_j+C_j^{\rm complete}|)}.
}
\tag{9.2}
$$



For the retained reduced weight $\lambda=a/k_{\rm wt}$, keep


$$
J_{\rm wt}=B_{\rm wt}\widetilde v_0-A_{\rm wt}\widetilde v_3,
$$




$$
T_{\rm wt}=aJ_{\rm wt}+k_{\rm wt}A_{\rm wt}\widetilde v_3,
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


The actual primitive pair is


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
\frac{T_{\rm wt}}{F_{\rm gcd}G_{\rm wt}H_{\rm gcd}}.
}
\tag{9.3}
$$


Every prime remains in these gcds.

## 9.5 Whole nonzero same-index error

The whole error remains


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda e_3\alpha_{n,2}
(\lambda-\Lambda_{n,2}).
}
\tag{9.4}
$$



The five accepted $3375$ whole forms remain nonzero and have absolute value greater than $1$. No result here changes those evaluations.

Even successful alignment and resonance estimates would still require control of the final all-prime weighted gcd and the whole nonzero same-index error.

---

# 10. Proof ledger and bounded exact arithmetic

| Statement | Status |
|---|---|
| Accepted alignment receipts at $3375,11025$ | Closed finite computations |
| Natural transfer (2.6) and determinant (2.7) | Proved |
| Actual evaluated block-remainder identity (3.3) | Proved |
| Fixed-seed unit property of the remainder multiplier | Proved |
| Multiplicative-block cofactor with $\log c_{b,n}=O(n)$ | Not proved |
| Adjacent common-alignment cost $O(\log n)$ | Proved, adjacent scope only |
| Subfactorial individual alignment on an infinite original family | Not proved |
| $F_n\equiv-2\pmod n$, hence $F_n\ne0$ | Proved |
| Exact excess factorization $\mathfrak X_j=\mathfrak S_j\mathfrak U_j$, $\mathfrak U_j\mid\mathcal I_n$ | Proved |
| Actual final-source identities (6.3) | Proved |
| Complete Green boundary and terminal retention | Reused and preserved |
| Fixed-$C$ logarithmic absorption height obstruction | Proved |
| Subfactorial saturated unit-resonance cost | Not proved |
| Favorable infinite primitive whole forms | Not established |
| Irrationality or rationality of $e+\pi$ | Unresolved |

## Bounded arithmetic

No numerical computation was executed. No already accepted bounded computation is requested again.

No new bounded calculation is needed for the proofs above. A finite symbolic audit, if desired, has the following completely specified inputs and outputs:

**Inputs**

- the rational matrix $\mathsf U_n$ in (2.6);
- the reference recurrence;
- the fixed-parameter moment recurrence;
- the Green kernel formula.

**Expected exact outputs**



$$
\det\mathsf U_n=\frac{(n+1)(n+2)^2(n+3)}2;
$$




$$
(2n+3)(n+2)(3n+2)
-(n^2+3n+1)(1-n-n^2)
=(n+1)^2(n^2+8n+11);
$$




$$
nF_{n-1}-(Y-X+Z)=0;
\qquad
2F_n-(3X-Y-Z)=0;
$$




$$
\mathsf G_{k,k-1}=1,\qquad
\mathsf G_{k,k-2}=2k-1.
$$



These are finite rational-polynomial identities, not another alignment sample and not an infinite-family numerical certificate.

---

# Conclusion

The new natural observation transfer gives a concrete multiplicative-block calculation on the actual fixed seed:


$$
\boxed{z_{n+1}=\mathsf U_nz_n.}
$$


Its determinant has only paid small-prime support, but the exact backward identity contains an explicit reference-line defect multiplied by a unit on terminal alignment. That is the precise obstruction to promoting transfer invertibility into the desired Bézout propagation.

The adjacent theorem proves a real, bounded-cost restriction:


$$
\boxed{
\mathcal A_n^{\rm adj}
\mid(2n+3)(n^2+8n+11).
}
$$


It does not control realignment over multiplicative blocks.

Combining A4’s full-depth theorem with exact seed subtraction gives the sharper excess payment


$$
\boxed{
\mathfrak X_j=\mathfrak S_j\mathfrak U_j,
\qquad
\mathfrak U_j\mid\mathcal I_n.
}
$$


Only alignment and the actual saturated unit charts remain; the earlier extra nonresonant moment/contact gcd is unnecessary.

The Green formula now includes explicit identities for its final two source contributions in terms of the actual moment state. Nevertheless, the retained transverse logarithmic term has height


$$
2\log(n!)+O(n),
$$


and cannot be absorbed into a fixed-$C$, seed-adjusted force pair at the smaller seed-subtracted height.

The exact remaining mathematical bottlenecks are:

1. a subfactorially paid **multiplicative-block observation propagation**, or another infinite-original alignment restriction;
2. a proved support/cost bound for the **saturated unit-cancellation sum**, with the complete force and terminal retained;
3. the actual all-prime primitive denominator and the whole nonzero same-index error comparison.



$$
\boxed{\text{No unconditional proof or disproof of the irrationality of }e+\pi
\text{ has been obtained.}}
$$


