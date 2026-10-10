> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3, Turn 12 — A fixed-seed alignment obstruction and a sharper complete-force elimination theorem

## Executive summary

The irrationality of $e+\pi$ remains unresolved.

This turn makes two advances, neither of which is an infinite-family small-content theorem.

1. **The actual moment recurrence gives an explicit integral backward-observation matrix for $\mathcal I_n$.** Its determinant can be evaluated:
   

$$
\boxed{
   \det \mathsf O_n
   =
   \frac{n(n+2)}{n+1}
   \frac{(n-1)!\,n!}{2^{n-1}}\,F.
   }
$$


   The displayed prefactor is a unit at every prime $p>n+2$. Consequently, the proposed backward-transfer argument encounters **exactly the original moment factor $F$** in its observation determinant. Invertibility of the moment transfer does not remove that factor.

   This is a fixed-seed, original-domain obstruction to that particular proof strategy—not a counterexample to $\mathcal I_n=1$. I obtain neither $\mathcal I_n=1$ nor a subfactorial bound for $\mathcal I_n$.

2. **A third integral complete-force identity removes the loss from using only $\alpha_j,\beta_j$.** Paying the actual coordinate content of the primitive contact row gives
   

$$
\boxed{
   \gcd(\Delta_{j,n},|\mathcal E_{j,n}|)
   =
   \gcd(F,\widehat R_j,\mathcal E_{j,n})_{>n+2}.
   }
$$


   Thus the earlier $F^2$ upper bound can be replaced by an exact elimination with $F$.

   More precisely, define the actual moment/contact obstruction
   

$$
\boxed{
   \mathcal Z_{j,n}
   =
   \gcd(|Z|,|\alpha_j|,|\beta_j|)_{>n+2}.
   }
$$


   Then, throughout the original domain,
   

$$
\boxed{
   \mathcal Z_{j,n}
   \mid
   \gcd(\Delta_{j,n},|\mathcal E_{j,n}|)
   \mid
   \gcd(\Delta_{j,n},|F|)
   \mid
   \mathcal I_n\mathcal Z_{j,n}.
   }
   \tag{E1}
$$


   Also,
   

$$
\boxed{
   \operatorname{lcm}(\mathcal I_n,\mathcal Z_{j,n})
   \mid \gcd(\Delta_{j,n},|F|).
   }
   \tag{E2}
$$


   In particular, **away from reference alignment**,
   

$$
\boxed{
   \gcd(\Delta_{j,n},|\mathcal E_{j,n}|)
   =
   \gcd(\Delta_{j,n},|F|)
   =
   \mathcal Z_{j,n}
   \quad\text{prime by prime}.
   }
   \tag{E3}
$$



This is a proved support-and-cost reduction for an actual part of $\Delta_j$. It does not bound the remaining affine cancellation, where the evaluated force may be a unit, or cancellation deeper than its valuation.

The new $3375$ arithmetic is accepted at its finite scope:


$$
\boxed{\gcd(F,Q\widehat h-P\widehat\ell)=128,\qquad \mathcal I_{3375}=1.}
$$


The retained filters and retained $\gcd(D^{>},\Sigma)=1$ give


$$
\boxed{\Delta_{0,3375}=\Delta_{3,3375}=\mathcal G_{3375}=1}
$$


algebraically, without recalculating those endpoint or filter gcds.

No accepted bounded computation is proposed again. At the end I give only the requested, unevaluated $O(n)$-recurrence specification for the new alignment content at $n=11025$.

---

# 1. Source reconciliation and unchanged scope

Throughout the endpoint argument,


$$
n=15^r\quad\text{or}\quad n=105^r,\qquad r\ge2,
$$


and


$$
m=n+1,\qquad N=n+2,\qquad L=2^{m/2}.
$$



I retain


$$
X=ma_n,\qquad Y=mna_{n-1},\qquad Z=2a_{n+1}-ma_n,
$$




$$
P=nX+Y,\qquad Q=nZ+2X-Y,
$$




$$
F=2m\bigl(Y-2X-(n-1)Z\bigr),
$$


and


$$
\widehat h=L\tau_n,\qquad
\widehat\ell=L\tau_{n+1},\qquad
M=Q\widehat h-P\widehat\ell.
$$



A useful exact relation is


$$
\boxed{F=2m(Z-Q).}
\tag{1.1}
$$



The reference-alignment content is


$$
\mathcal I_n=\gcd(|F|,|M|)_{>N}.
$$



All localization below is expressly at $p>N$. It is not used to alter the final all-prime primitive normalization.

## 1.1 A3 and A4 use the same alignment content

A4’s $\mathcal K_{\rm ref}$ is exactly $\mathcal I_n$.

There is a harmless but important normalization difference in the endpoint references. Writing


$$
\widehat R_j=\alpha_j\widehat h+\beta_j\widehat\ell
$$


as in A3, A4’s reference in its product certificate is


$$
\widehat R_j^{\,A4}=\frac m2\,\widehat R_j.
$$


Since $m/2$ is an integer with prime support at most $N$, these have identical valuations at $p>N$.

I therefore write A4’s certificate as


$$
\mathcal G_n
=
\gcd\!\left(\mathcal W_n,\,
\left|\widehat R_0\widehat R_3\right|\right);
$$


this is the same large-prime integer as its original definition.

No common Smith argument needs to be repeated.

## 1.2 The filtered certificate already divides the intersection certificate

The retained results give


$$
\mathcal W_n^{\rm ref}\mid\mathcal W_n
$$


and


$$
\mathcal W_n^{\rm ref}
\mid\Delta_{0,n}\Delta_{3,n}
\mid |\widehat R_0\widehat R_3|.
$$


Consequently,


$$
\boxed{\mathcal W_n^{\rm ref}\mid\mathcal G_n.}
\tag{1.2}
$$



Combining the two reports yields the useful ordering


$$
\boxed{
\delta_0^{>}\delta_3^{>}
\mid\mathcal W_n^{\rm ref}
\mid\mathcal G_n
\mid\mathcal I_n^2\delta_0^{>}\delta_3^{>}.
}
\tag{1.3}
$$



Thus $\mathcal G_n$ is an alternative, simpler intersection certificate, but intersecting it again with the already constructed $\mathcal W_n^{\rm ref}$ cannot improve the latter.

This observation does not supply a height estimate for either certificate.

## 1.3 What is established at $3375$

The new source computes $F,M$ from the retained original moment and reference entries. The reported small-prime exponents and large cofactor give


$$
\gcd(|F|,|M|)=2^7=128,\qquad \mathcal I_{3375}=1.
$$



The deduction of the endpoint scalar/reference gcds is also valid. Since the retained data have


$$
\gcd(D^{>},\Sigma)=1,
$$


removing the $\Sigma$-part from an endpoint reference does not change its gcd with $D^{>}$. Hence the retained $V_0=V_3=1$ imply


$$
\gcd(D^{>},|\widehat R_0|)
=
\gcd(D^{>},|\widehat R_3|)=1.
$$


Therefore


$$
\Delta_0=\Delta_3=\mathcal G=1.
$$



These are finite facts and algebraic consequences of finite facts. They establish no infinite-family alignment bound.

---

# 2. First attempt: exploit the fixed moment and reference recurrences

This section gives an explicit original-seed calculation. Its purpose is to determine what the proposed transfer argument actually proves and where it stops.

## 2.1 Integral moment recurrence

For fixed original $n$, put


$$
A_n(z)=e^zq(z)^n
=\sum_{k\ge0}a_k\frac{z^k}{k!},
\qquad q(z)=1-z+\frac{z^2}{2}.
$$


The identity


$$
qA_n'=(q+nq')A_n
$$


gives


$$
\boxed{
a_{k+1}
=(k+1-n)a_k
+\frac{k(2n-k-1)}2a_{k-1}
+\frac{k(k-1)}2a_{k-2}.
}
\tag{2.1}
$$


Both displayed half-products are integers.

The actual fixed seed is


$$
\boxed{
a_0=1,\qquad a_1=1-n,\qquad a_2=(n-1)^2.
}
\tag{2.2}
$$



Only the coefficients through $a_{n+1}$ are used here. This does not extend the complete-force cutoff or introduce another terminal return.

Set


$$
s_k=(a_{k-1},a_k,a_{k+1})^T.
$$


For $1\le k\le n-1$,


$$
s_{k+1}=\mathsf A_k s_k,
$$


where


$$
\mathsf A_k=
\begin{pmatrix}
0&1&0\\
0&0&1\\
\dfrac{k(k+1)}2&
\dfrac{(k+1)(2n-k-2)}2&
k+2-n
\end{pmatrix}.
\tag{2.3}
$$


Thus


$$
\det\mathsf A_k=\frac{k(k+1)}2.
$$



Define


$$
\mathsf C_n=\mathsf A_{n-1}\cdots\mathsf A_1,
\qquad
\chi_n=\det\mathsf C_n
=\frac{(n-1)!\,n!}{2^{n-1}}.
\tag{2.4}
$$


Every prime divisor of $\chi_n$ is at most $N$.

The fixed seed and terminal state satisfy


$$
s_n=\mathsf C_n s_1,\qquad
s_1=(1,1-n,(n-1)^2)^T.
$$



In particular, $\mathsf C_n$ is invertible over $\mathbb Z_p$ for every $p>N$. This proves primitivity of the full moment state there. It does **not**, on its own, prove primitivity of a two-coordinate observation of that state.

## 2.2 Integral reference normalization

For a bounded computation, a convenient integral reference sequence is


$$
t_k=2^{\lfloor k/2\rfloor}\tau_k.
$$


Its integrality follows directly from the constant-term formula for $\tau_k$.

The standard recurrence


$$
(k+1)\tau_{k+1}=(2k+1)\tau_k+k\tau_{k-1}
$$


becomes


$$
\boxed{
(k+1)t_{k+1}
=
\begin{cases}
(2k+1)t_k+2k\,t_{k-1},&k\ \text{even},\\[2mm]
2(2k+1)t_k+2k\,t_{k-1},&k\ \text{odd},
\end{cases}
}
\tag{2.5}
$$


with $t_0=t_1=1$. Every displayed division by $k+1$ is exact.

Since original $n$ is odd,


$$
\boxed{\widehat h=2t_n,\qquad \widehat\ell=t_{n+1}.}
\tag{2.6}
$$



This normalization pays the dyadic denominators explicitly. It makes no claim about primitivity of the evaluated alignment observation.

---

# 3. An integral backward exterior identity for the actual alignment content

## 3.1 The terminal alignment line

The linear map from


$$
s_n=(a_{n-1},a_n,a_{n+1})^T
$$


to $(P,Q,F)^T$ is


$$
\mathsf L_n=
\begin{pmatrix}
mn&mn&0\\
-mn&m(2-n)&2n\\
2m^2n&2m^2(n-3)&-4m(n-1)
\end{pmatrix},
$$


and


$$
\boxed{\det\mathsf L_n=4m^3nN.}
\tag{3.1}
$$


This determinant has only primes at most $N$.

Introduce the integral $3\times2$ matrix


$$
\mathsf V_n=
\begin{pmatrix}
4&2n(n-1)\\
2n&-2n(n-1)\\
mn&3mn
\end{pmatrix}
$$


and the terminal reference vector


$$
v_n^{\rm ref}
=\mathsf V_n
\binom{\widehat h}{\widehat\ell}.
$$


A direct multiplication gives


$$
\boxed{
\mathsf L_n v_n^{\rm ref}
=
2mnN
\begin{pmatrix}
\widehat h\\ \widehat\ell\\0
\end{pmatrix}.
}
\tag{3.2}
$$



At $p>N$, all factors paid in (3.1)–(3.2) are units. The retained transverse-content theorem therefore identifies $\mathcal I_n$ with the large-prime content of


$$
s_n\times v_n^{\rm ref}.
$$



## 3.2 Pulling the exterior product back to the fixed seed

Put


$$
z_n=\operatorname{adj}(\mathsf C_n)v_n^{\rm ref}\in\mathbb Z^3.
$$


The cross-product transformation law gives the exact integral identity


$$
\boxed{
\mathsf C_n^T(s_n\times v_n^{\rm ref})
=
s_1\times z_n.
}
\tag{3.3}
$$



Write $a=1-n$, so $s_1=(1,a,a^2)^T$. The content of $s_1\times z_n$ is the gcd of


$$
(z_n)_2-a(z_n)_1,\qquad
(z_n)_3-a^2(z_n)_1.
$$


Indeed, its third remaining coordinate is an integral linear combination of these two.

Define


$$
\mathsf U_n=
\begin{pmatrix}
-a&1&0\\
-a^2&0&1
\end{pmatrix},
\qquad
\mathsf O_n
=
\mathsf U_n\operatorname{adj}(\mathsf C_n)\mathsf V_n.
\tag{3.4}
$$


No row content is divided out of $\mathsf O_n$.

We obtain


$$
\boxed{
\mathcal I_n
=
\gcd\!\left(
\left|(\mathsf O_n(\widehat h,\widehat\ell)^T)_1\right|,
\left|(\mathsf O_n(\widehat h,\widehat\ell)^T)_2\right|
\right)_{>N}.
}
\tag{3.5}
$$



Equation (3.3) is an integral exterior propagation identity for the actual seed. But (3.5), by itself, is only a new expression for the same content. Its usefulness depends on the arithmetic of the actual observation matrix.

## 3.3 The observation determinant is not smooth: it contains $F$

The determinant of $\mathsf O_n$ can be evaluated without constructing all its entries.

The cross product of the two rows of $\mathsf U_n$ is $s_1$. If $v_h,v_\ell$ are the columns of $\mathsf V_n$, then


$$
\det\mathsf O_n
=
\chi_n\,s_n\cdot(v_h\times v_\ell).
\tag{3.6}
$$


A direct calculation gives


$$
v_h\times v_\ell
=
2nN
\begin{pmatrix}
mn\\
m(n-3)\\
-2(n-1)
\end{pmatrix}.
$$


Since


$$
F
=
2m\left(
mn\,a_{n-1}+m(n-3)a_n-2(n-1)a_{n+1}
\right),
$$


we conclude:

### Theorem 3.1 — Fixed-seed backward-observation determinant


$$
\boxed{
\det\mathsf O_n
=
\frac{nN}{m}\,\chi_n F
=
2nN\chi_n\,\frac{F}{2m}.
}
\tag{3.7}
$$


The second expression is an integer identity.

For every $p>N$,


$$
\boxed{v_p(\det\mathsf O_n)=v_p(F)}
\tag{3.8}
$$


when $F\ne0$; if $F=0$, the observation matrix is singular.

### Consequence

The moment transfer $\mathsf C_n$ has only small-prime determinant support. The **observation after that transfer does not**: its determinant contains the original evaluated $F$.

Therefore the following proposed inference is invalid:


$$
\text{invertible moment transfer}
+\text{primitive reference pair}
\Longrightarrow \mathcal I_n=1.
$$



For this particular fixed seed and this particular terminal observation, the missing step is exactly the evaluated projection through $\mathsf O_n$. Its determinant reproduces $F$, up to paid small-prime factors.

This is not a generic arbitrary-companion counterexample. It is an exact obstruction arising from the original recurrence and original seed.

### What has not been achieved

The backward identity has not produced a right-hand side with subfactorial height or only small-prime support. In particular:

* no further factorial normalization is available for free;
* the bound
  

$$
\log\mathcal I_n\le\log(n!)+O(n)
$$


  remains factorial-scale;
* $\mathcal I_n=1$ is neither proved nor disproved on the original family.

A useful next alignment lemma would have to control the **evaluated pair**
$\mathsf O_n(\widehat h,\widehat\ell)^T$, not merely $\det\mathsf C_n$ or the primitivity of $(\widehat h,\widehat\ell)$.

---

# 4. A third complete-force identity

We now return to the actual complete scalar and actual primitive contact rows.

For each endpoint $j=0,3$,


$$
\alpha_j=r_jv',\qquad
\beta_j=r_jw',\qquad
\gamma_j=r_je_2,
$$


and


$$
P\alpha_j+Q\beta_j+F\gamma_j=0.
\tag{4.1}
$$



The rows $r_j$ here are the retained **actual primitive contact rows**. They are not raw adjugate rows, and they are not the reconstructed two-entry rows.

Set


$$
v_n=u_n-a_n,\qquad v_{n+1}=u_{n+1}-a_{n+1},
$$


and abbreviate


$$
A=\frac m2v_n,\qquad
B=v_{n+1}-\frac m2v_n,\qquad
C=mZ,
$$




$$
\kappa=2L(n!)^2.
$$


Then


$$
\mathcal E_j=A\alpha_j+B\beta_j+C\gamma_j.
\tag{4.2}
$$


Also,


$$
\mathcal T=CQ-FB,\qquad
\mathcal S=-CP+FA,
$$


and the full canonical scalar is


$$
\boxed{
\Theta
=\mathcal T\widehat h+\mathcal S\widehat\ell+\kappa F
=CM-F(\widehat hB-\widehat\ell A)+\kappa F.
}
\tag{4.3}
$$



The nonzero logarithmic contribution $\kappa F=2LF(n!)^2$ is retained.

The actual complete endpoint residual remains


$$
\boxed{
C_j^{\rm complete}
=
\mathcal E_j-E_nR_j
+2n!m!\,(\alpha_j\rho_n+\beta_j\rho_{n+1}).
}
\tag{4.4}
$$


Nothing below replaces this by $\mathcal E_j$.

## 4.1 The missing third identity

The retained first two identities can be written


$$
\alpha_j(\Theta-\kappa F)-\mathcal T\widehat R_j
=F\widehat\ell\,\mathcal E_j,
\tag{4.5}
$$




$$
\beta_j(\Theta-\kappa F)-\mathcal S\widehat R_j
=-F\widehat h\,\mathcal E_j.
\tag{4.6}
$$



Define


$$
D_{\rm exp}=QA-PB.
$$



### Theorem 4.1 — Third integral endpoint identity


$$
\boxed{
\gamma_j(\Theta-\kappa F)
=
M\mathcal E_j-D_{\rm exp}\widehat R_j.
}
\tag{4.7}
$$



#### Proof

Expanding $M\mathcal E_j-\gamma_j(\Theta-\kappa F)$, using (4.3), gives


$$
M(A\alpha_j+B\beta_j)
+F\gamma_j(\widehat hB-\widehat\ell A).
$$


Substitute $F\gamma_j=-P\alpha_j-Q\beta_j$. The remaining expression is


$$
(QA-PB)(\alpha_j\widehat h+\beta_j\widehat\ell)
=D_{\rm exp}\widehat R_j.
$$


Rearrangement proves (4.7). ∎

Unlike the first two identities alone, (4.7) retains information on the chart where $\alpha_j,\beta_j$ are both divisible by the prime.

---

# 5. Paying the actual row-coordinate content

Let


$$
\eta_j=\gcd(|\alpha_j|,|\beta_j|,|\gamma_j|).
$$



Because $r_j$ is an actual primitive integral row, and the coordinate matrix $(v',w',e_2)$ has determinant $2N^2$,


$$
\boxed{\eta_j\mid2N^2.}
\tag{5.1}
$$


Thus $\eta_j$ is a unit at every $p>N$, but it need not equal $1$ over $\mathbb Z$.

Choose integers $a_j,b_j,c_j$ satisfying


$$
a_j\alpha_j+b_j\beta_j+c_j\gamma_j=\eta_j.
$$


Combining (4.5)–(4.7) gives the fully integral identity


$$
\boxed{
\eta_j(\Theta-\kappa F)
=
U_j\widehat R_j+V_j\mathcal E_j,
}
\tag{5.2}
$$


where


$$
U_j=a_j\mathcal T+b_j\mathcal S-c_jD_{\rm exp},
$$




$$
V_j=a_jF\widehat\ell-b_jF\widehat h+c_jM.
$$



This pays the actual coordinate content. There is no assumption that $\gcd(\alpha_j,\beta_j)=1$.

Both $\eta_j$ and $\kappa$ have prime support at most $N$. Hence, over $\mathbb Z_p$ for $p>N$,


$$
(\Theta,\widehat R_j,\mathcal E_j)
=
(F,\widehat R_j,\mathcal E_j).
$$



### Theorem 5.1 — Exact complete-force elimination


$$
\boxed{
\gcd(\Delta_{j,n},|\mathcal E_{j,n}|)
=
\gcd(F,\widehat R_j,\mathcal E_{j,n})_{>N}.
}
\tag{5.3}
$$



This is an all-depth identity. It improves the earlier bound


$$
\gcd(\Theta,\widehat R_j,\mathcal E_j)_{>N}\mid(F^2)_{>N}
$$


to an exact gcd with $F$.

It also supplies an exact complete affine congruence system for $\Delta_j$: at $p>N$, the conditions


$$
\widehat R_j\equiv0\pmod{p^t}
$$


and


$$
\begin{aligned}
F(\widehat h\mathcal E_j-\kappa\beta_j)&\equiv0,\\
F(\widehat\ell\mathcal E_j+\kappa\alpha_j)&\equiv0,\\
M\mathcal E_j+\kappa F\gamma_j&\equiv0
\end{aligned}
\pmod{p^t}
\tag{5.4}
$$


are jointly equivalent to


$$
p^t\mid\widehat R_j,\qquad p^t\mid\Theta.
$$



The third congruence is essential when division by $F$ is unavailable.

---

# 6. A new moment/contact bound for the force-overlap part of $\Delta_j$

Define


$$
\mathcal Z_j
=
\gcd(|Z|,|\alpha_j|,|\beta_j|)_{>N},
$$




$$
\mathcal J_j=\gcd(\Delta_j,|F|),
\qquad
\mathcal K_j=\gcd(\Delta_j,|\mathcal E_j|).
\tag{6.1}
$$



The integers $\mathcal Z_j$ are well defined and positive. If $Z=\alpha_j=\beta_j=0$, row primitivity and (4.1) would give $F=0$, hence $\Theta=0$, contrary to the retained all-original nonvanishing theorem.

### Theorem 6.1 — Alignment-localized force-overlap cost

At every original index,


$$
\boxed{
\mathcal Z_j\mid\mathcal K_j\mid\mathcal J_j
\mid\mathcal I_n\mathcal Z_j,
}
\tag{6.2}
$$


and


$$
\boxed{
\operatorname{lcm}(\mathcal I_n,\mathcal Z_j)\mid\mathcal J_j.
}
\tag{6.3}
$$



Consequently,


$$
\boxed{
\operatorname{strip}_{\mathcal I_n}(\mathcal K_j)
=
\operatorname{strip}_{\mathcal I_n}(\mathcal J_j)
=
\operatorname{strip}_{\mathcal I_n}(\mathcal Z_j).
}
\tag{6.4}
$$



#### Proof

Fix $p>N$. Use $v_p(0)=+\infty$, and write


$$
f=v_p(F),\quad \mu=v_p(M),\quad z=v_p(Z),
$$




$$
r=v_p(\widehat R_j),\quad d=v_p(\Theta),\quad
g=\min(v_p(\alpha_j),v_p(\beta_j)),
$$




$$
a=\min(f,\mu)=v_p(\mathcal I_n).
$$


Let


$$
t=v_p(\mathcal J_j)=\min(f,d,r),
\qquad
\zeta=v_p(\mathcal Z_j)=\min(z,g).
$$



**First, $\mathcal Z_j\mid\mathcal K_j$.**  
If $\zeta>0$, row primitivity makes $\gamma_j$ a unit. Relation (4.1) gives $f\ge\zeta$. Equations (4.2)–(4.3) then give


$$
v_p(\mathcal E_j),\ r,\ d\ge\zeta.
$$


Hence $v_p(\mathcal K_j)\ge\zeta$.

**Second, $\mathcal K_j\mid\mathcal J_j$.**  
This follows from the exact elimination (5.3).

**Third, $\mathcal I_n\mid\mathcal J_j$.**  
The retained transverse-content statement gives $r\ge a$, and the scalar identity


$$
\Theta=mZM-F\widehat{\mathscr K}
$$


gives $d\ge a$. Also $f\ge a$.

**Finally, $t\le a+\zeta$.**  
The scalar identity implies


$$
z+\mu\ge t.
\tag{6.5}
$$


The shared-column and reference relations give


$$
M\alpha_j=Q\widehat R_j+F\widehat\ell\gamma_j,
$$




$$
M\beta_j=-P\widehat R_j-F\widehat h\gamma_j.
$$


Therefore


$$
\mu+g\ge t.
\tag{6.6}
$$



If $t\le a$, the desired bound is immediate. If $t>a$, then $f\ge t>a$, so necessarily $\mu=a$. Equations (6.5)–(6.6) yield


$$
z,g\ge t-a,
$$


hence


$$
t\le a+\min(z,g)=a+\zeta.
$$



We have proved


$$
\zeta\le v_p(\mathcal K_j)\le t\le a+\zeta,
\qquad a\le t.
$$


This proves all assertions. ∎

## 6.1 What this reduction accomplishes

The force-overlap part of $\Delta_j$ is no longer bounded merely by an undifferentiated $F^2$.

It is controlled by


$$
\mathcal I_n
\quad\text{and}\quad
\gcd(Z,\alpha_j,\beta_j)_{>N},
$$


with only one copy of the alignment cost:


$$
\boxed{
\frac{\mathcal K_j}{\mathcal Z_j}\mid\mathcal I_n,
\qquad
\frac{\mathcal J_j}{\mathcal Z_j}\mid\mathcal I_n.
}
\tag{6.7}
$$



Away from alignment, the answer is exact and uses only the actual moment/contact entries. It does not require computing the complete force to evaluate this particular overlap.

The actual primitive contact-row normalization remains indispensable: replacing $r_j$ by an unnormalized raw row would change $\mathcal Z_j$ and invalidate the stated cost.

## 6.2 What it does not accomplish

Let


$$
k_j=v_p(\Delta_j),\qquad e_j^{\rm exp}=v_p(\mathcal E_j).
$$


The theorem controls


$$
\min(k_j,e_j^{\rm exp})
\quad\text{and}\quad
\min(k_j,v_p(F)).
$$


It does **not** control $k_j$ itself.

In particular:

* if $\mathcal E_j$ is a unit, the first controlled quantity is zero, while the affine cancellation in (5.4) can still occur;
* if $k_j>v_p(F)$, the second controlled quantity stops at $v_p(F)$;
* bounding a clipped gcd does not bound the full depth of every prime appearing in it.

Thus the new theorem cannot justify support-stripping the entire $\mathcal E_j$-supported part of $\Delta_j$ at the cost $\mathcal K_j$. That would again lose higher valuation information.

---

# 7. Collision depth and the product certificates remain intact

The new elimination theorem concerns the actual canonical scalar/reference gcds. It does not replace the collision analysis.

The retained quantities


$$
\mathcal B_n,\qquad \Sigma_n,\qquad
H_n^{\rm ref},\qquad V_{j,n},\qquad
\mathcal W_n^{\rm ref}
$$


keep their original definitions, including:

* source-content removal;
* the complete collision depth;
* defect-support stripping;
* removal of the full collision depth from each reference before the exclusive gcd.

The combined product statement remains


$$
\delta_0^{>}\delta_3^{>}
\mid\mathcal W_n^{\rm ref}
\mid\mathcal G_n
\mid\mathcal I_n^2\delta_0^{>}\delta_3^{>}.
$$



Nothing in (6.2) permits replacing the complete residual by $\mathcal E_j$, replacing $\Sigma_n$ by its radical, or counting a collision prime only once.

At $3375$, the retained $\Delta_0=\Delta_3=1$ implies, as a theorem consequence,


$$
\mathcal Z_0=\mathcal Z_3=\mathcal J_0=\mathcal J_3
=\mathcal K_0=\mathcal K_3=1.
$$


These are deductions, not newly executed gcd calculations.

---

# 8. The binary-family source challenge

The recovered binary normalization must not be judged from a raw binary ratio alone.

For the complete binary family with $n=4002b$, the retained prime-$3$ theorem is


$$
\boxed{v_3(q_n)=n-\frac{b+15}{2}.}
\tag{8.1}
$$


In the range where the exact raw-ratio hypothesis also gives A4’s binary exponent,


$$
v_2(q_n)=C_n,
$$


one therefore has the simultaneous lower bound


$$
\boxed{
q_n\ge
2^{C_n}\,
3^{\,n-(b+15)/2}.
}
\tag{8.2}
$$



The prime-$3$ contribution is part of the actual factorial normalization of the primitive denominator. It is not removed by selected binary congruence success.

The coordinator’s retained whole-error comparison already makes this contribution fatal to the stated shallow binary route. I do not reopen that accepted calculation, and I do not substitute an unprovided asymptotic constant for the retained one.

The valid general comparison is always with


$$
q_n(e+\pi)-p_n=-q_n\epsilon_n,
$$


using the actual all-prime $q_n$. Neither a raw unit ratio nor favorable selected-prime congruences suffice.

This does not prove that every possible binary argument fails. It does rule out preferring that shallow route on the basis of the selected-prime evidence alone.

---

# 9. Preserved reconstruction, final gcd, and whole same-index error

The endpoint construction is unchanged.

The complete forcing remains


$$
F_k=(n+1)a_k-nk\,a_{k-1}
+\frac{(n-1)k(k-1)}2a_{k-2}
+\frac{k(k-1)(k-2)}2a_{k-3}
$$


through the original cutoff $2n+2$, with the complete terminal return.

The corrected columns remain


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


The exterior $+1$ in $v_0$ is retained.

The least clearer is taken over all eight entries, followed by division of each reconstructed row by its actual two-entry content. The accepted $3375$ contents remain


$$
(113940000,\ 9780750,\ 10125,\ 1).
$$



These are distinct from the contact-row contents and from $\eta_j$.

For the retained reduced weight $\lambda=a/k_{\rm wt}$, keep


$$
J_{\rm wt}=B_{\rm wt}\widetilde v_0-A_{\rm wt}\widetilde v_3,
$$




$$
T_{\rm wt}=aJ_{\rm wt}+k_{\rm wt}A_{\rm wt}\widetilde v_3,
$$




$$
F_{\rm gcd}
=\gcd(|A_{\rm wt}|,|a|)
 \gcd(|B_{\rm wt}|,|a-k_{\rm wt}|),
$$




$$
G_{\rm wt}=\gcd(k_{\rm wt},|J_{\rm wt}|),
$$




$$
H_{\rm gcd}
=\gcd\!\left(
h_{\rm end},
\frac{|T_{\rm wt}|}{F_{\rm gcd}G_{\rm wt}}
\right).
$$



The actual primitive pair is


$$
\boxed{
q_\lambda
=
\frac{k_{\rm wt}h_{\rm end}|A_{\rm wt}B_{\rm wt}|}
{F_{\rm gcd}G_{\rm wt}H_{\rm gcd}},
}
$$




$$
\boxed{
p_\lambda
=
\operatorname{sgn}(A_{\rm wt}B_{\rm wt})
\frac{T_{\rm wt}}{F_{\rm gcd}G_{\rm wt}H_{\rm gcd}}.
}
$$



Every prime remains in these final gcds. The large-prime structural reductions above do not replace this normalization.

Finally,


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda e_3\alpha_{n,2}(\lambda-\Lambda_{n,2}).
}
\tag{9.1}
$$


The five accepted $3375$ whole forms remain nonzero and have absolute value greater than $1$. Neither $\Theta\ne0$, $\mathcal G=1$, nor the new elimination theorem changes those whole-error evaluations.

---

# 10. The precise remaining arithmetic lemma

The recurrence attempt and the force elimination now separate two unresolved issues more sharply.

## 10.1 Alignment

A sufficient alignment advance would be an original-family estimate


$$
\log\mathcal I_n=o(n\log n).
$$


The backward construction shows exactly what must be controlled:


$$
\mathsf O_n
\binom{\widehat h}{\widehat\ell}.
$$



The determinant identity


$$
\det\mathsf O_n
=\text{small-prime unit}\times F
$$


does not provide that control. A successful proof needs an evaluated Bézout or propagation statement for this fixed reference vector, not just nonsingularity of the transfer.

## 10.2 The remaining affine depth

Theorem 6.1 gives


$$
\mathcal K_0\mathcal K_3
\mid \mathcal I_n^2\mathcal Z_0\mathcal Z_3.
$$


Therefore a concrete sufficient next lemma is the following.

> **Affine-depth remainder lemma.**  
> On an infinite original subsequence, prove
> 

$$
> 2\log\mathcal I_n+\log(\mathcal Z_0\mathcal Z_3)
> =o(n\log n),
>
$$


> and
> 

$$
> \sum_{j=0,3}\ \sum_{p>N}
> \left(
> \min\{v_p(\Theta_n),v_p(\widehat R_j)\}
> -v_p(\mathcal E_j)
> \right)_+\log p
> =o(n\log n).
> \tag{10.1}
>
$$


> The congruences to be controlled are the complete three-equation system (5.4), including $\kappa F$.

Indeed, the second sum is exactly


$$
\log\frac{\Delta_0\Delta_3}{\mathcal K_0\mathcal K_3}.
$$


Together these estimates would give


$$
\log(\Delta_0\Delta_3)=o(n\log n),
$$


and hence


$$
\log\mathcal W_n^{\rm ref}=o(n\log n).
$$



This is a sufficient follow-on lemma, not a proof of it. It explicitly preserves the excess depth beyond the evaluated force valuation.

Even that arithmetic estimate would not finish an irrationality proof. The actual weighted all-prime gcd and the whole nonzero same-index error would still have to be controlled.

---

# 11. The one new bounded alignment calculation: $n=11025$

No finite execution is needed for the theorems above.

The scoped archive result permits one genuinely new calculation: the reference-alignment content at


$$
n=105^2=11025.
$$


Its scope is only


$$
F,\quad M=Q\widehat h-P\widehat\ell,\quad
\gcd(F,M),\quad \mathcal I_{11025}.
$$



It does not produce force, contacts, endpoint denominators, weighted denominators, or whole errors.

The following specification uses the integral recurrences (2.1) and (2.5), with $O(n)$ integer recurrence steps. It has not been executed here.

```python
from math import gcd, isqrt

n = 11025
assert n == 105**2 and n % 2 == 1
m, N = n + 1, n + 2

# Fixed-parameter moment recurrence.
# At the end: am, ac, ap = a_{n-1}, a_n, a_{n+1}.
am, ac, ap = 1, 1 - n, (n - 1)**2
for k in range(2, n + 1):
    b = k * (2*n - k - 1)
    c = k * (k - 1)
    assert b % 2 == 0 and c % 2 == 0
    nxt = (k + 1 - n)*ap + (b//2)*ac + (c//2)*am
    am, ac, ap = ac, ap, nxt

X = m * ac
Y = m * n * am
Z = 2 * ap - m * ac
P = n * X + Y
Q = n * Z + 2 * X - Y
F = 2 * m * (Y - 2*X - (n - 1)*Z)
assert F == 2*m*(Z - Q)

# t_k = 2^{floor(k/2)} tau_k, all divisions exact.
tm, tc = 1, 1
for k in range(1, n + 1):
    lead = (2*k + 1) * (2 if k % 2 else 1)
    num = lead*tc + 2*k*tm
    tn, rem = divmod(num, k + 1)
    assert rem == 0
    tm, tc = tc, tn

hhat, ellhat = 2*tm, tc
Mref = Q*hhat - P*ellhat

common = gcd(abs(F), abs(Mref))
assert common > 0

sieve = bytearray(b"\x01") * (N + 1)
sieve[0:2] = b"\x00\x00"
for p in range(2, isqrt(N) + 1):
    if sieve[p]:
        for k in range(p*p, N + 1, p):
            sieve[k] = 0

I = common
small = []
small_product = 1
for p in range(2, N + 1):
    if not sieve[p]:
        continue
    e = 0
    while I % p == 0:
        I //= p
        e += 1
    if e:
        small.append((p, e))
        small_product *= p**e

assert common == small_product * I

result = {
    "n": n,
    "alignment_gcd_hex": hex(common),
    "alignment_small_prime_exponents": small,
    "I_large_hex": hex(I),
    "I_large_bits": I.bit_length(),
    "F_bits": abs(F).bit_length(),
    "M_ref_bits": abs(Mref).bit_length(),
    "scope": "reference alignment only",
}
```

### Expected verifiable output

The expected output is not a predicted numerical value of $\mathcal I_{11025}$. It is:

1. exact completion of every moment and reference recurrence step;
2. the exact integer $\gcd(F,M)$;
3. its complete prime-power part through $11027$;
4. the exact remaining $\mathcal I_{11025}$;
5. the identity
   

$$
\gcd(F,M)
   =
   \mathcal I_{11025}
   \prod_{p\le11027}p^{v_p(\gcd(F,M))}.
$$



If $\mathcal I_{11025}>1$, that is a genuine original-domain counterexample to uniform $\mathcal I_n=1$. If it equals $1$, it is one further finite corroboration and no more.

No value is inferred in advance.

---

# Final status

| Statement | Status |
|---|---|
| $\gcd(F,M)=128$, $\mathcal I_{3375}=1$ | Accepted new exact finite arithmetic |
| $\Delta_{0,3375}=\Delta_{3,3375}=\mathcal G_{3375}=1$ | Algebraically derived from retained filters |
| $\mathcal W^{\rm ref}\mid\mathcal G$ | New direct combination of retained theorems |
| Integral moment backward-exterior identity | Proved |
| $\det\mathsf O_n=(nN/m)\chi_nF$ | New exact original-seed theorem |
| $\mathcal I_n=1$ on every original index | Neither proved nor disproved |
| Subfactorial bound for $\mathcal I_n$ | Not proved |
| Third complete-force endpoint identity | Proved |
| Exact elimination $\gcd(\Delta_j,\mathcal E_j)=\gcd(F,\widehat R_j,\mathcal E_j)_{>N}$ | Proved |
| $\mathcal Z_j\mid\mathcal K_j\mid\mathcal J_j\mid\mathcal I_n\mathcal Z_j$ | New infinite-domain support-and-cost theorem |
| Required bound on remaining affine depth | Not proved |
| New alignment calculation at $11025$ | Unevaluated bounded specification |
| Infinite nonzero primitive whole forms tending to zero | Not proved |
| Irrationality of $e+\pi$ | Unresolved |

## Conclusion

The recurrence calculation identifies an exact obstruction to the hoped-for automatic alignment proof:


$$
\boxed{
\det\mathsf O_n
=
\frac{n(n+2)}{n+1}
\frac{(n-1)!\,n!}{2^{n-1}}F.
}
$$


The transfer is invertible at large primes, but its actual fixed-seed observation still carries $F$. No subfactorial alignment estimate follows.

The new complete-force result is


$$
\boxed{
\mathcal Z_{j,n}
\mid
\gcd(\Delta_{j,n},|\mathcal E_{j,n}|)
\mid
\gcd(\Delta_{j,n},|F|)
\mid
\mathcal I_n\mathcal Z_{j,n}.
}
$$


It retains the logarithmic constant $2LF(n!)^2$, pays the actual primitive row-coordinate content, and is exact away from reference alignment.

The remaining bottleneck is the full depth of the actual affine cancellation—not merely its overlap with $F$ or with the evaluated exponential-force projection. That depth must be controlled on an infinite original family, with collision depth preserved, before the actual all-prime weighted denominator and the nonzero whole same-index error can be compared successfully.



$$
\boxed{\text{No unconditional proof or disproof of the irrationality of }e+\pi
\text{ has been obtained.}}
$$


