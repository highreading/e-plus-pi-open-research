> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A second Gaussian–Hermite jet and an original-index lifting obstruction

## Abstract and proof status

The rationality or irrationality of $e+\pi$ is not decided here. Nor is the desired estimate


$$
\kappa_N^{\mathrm{prod}}\le (N!)^{1-\eta}e^{CN},
\qquad \eta>0,
$$


proved.

The new results are more limited, but they go beyond the first necessary congruence.

1. **An evaluated second Gaussian jet.**  
   At every original index and every $p\ge17$ dividing $2N-1$, both the divided Gaussian source $V$ and its complete endpoint $E_F$ are evaluated modulo $p^2$. The formula retains the actual changing $\alpha,\beta,\delta$, including primes dividing $g_B$. Its new scalar corrections are evaluated by the original affine states at indices $p-1,p$, together with Hermite endpoints at $k=(p+1)/2\le N$.

2. **A certified upper-depth contribution to the actual multiplier.**  
   Whenever the evaluated second source jet is nonzero modulo $p^2$,
   

$$
v_p(\kappa_N^{\mathrm{prod}})\le [1-h_p]_+.
$$


   Thus the entire contribution of those certified primes is at most
   

$$
\log(2N-1).
$$


   This is an upper bound on the actual positive-part mass, after the full Hermite credit. It does not assume endpoint surplus.

3. **An original-domain lifting obstruction.**  
   Under explicitly stated non-Wieferich and Gaussian-unit hypotheses, a first collision can be followed through $p$ genuine original indices. Exactly one of those indices has its Gaussian source divisible by $p^2$; the other $p-1$ have Gaussian source valuation exactly one. Both source equations have unit next-digit slopes. Their two exceptional lifts coincide precisely when a displayed second-order collision invariant vanishes.

   Consequently, a unit slope does not prove the regular continuation lemma. It selects a possible deeper lift rather than excluding it.

The regular simple-arc continuation lemma remains open at its full stated scope. More importantly, the certified band below does **not** control a quantitatively significant part of the unrestricted $p>N$ or $p\nmid d_K$ mass. The report does not convert an index-density statement into a pointwise $N\log N$ saving.

---

## 1. Original objects and the exact arithmetic target

Throughout,


$$
\boxed{N=9^{18+32u}=3^{36+64u},\qquad u\ge0,}
$$


and


$$
n=2N,\qquad m=N-3,\qquad \ell=2N-6.
$$


Every such $N$ is odd. The physical polynomial terminal remains $n=2N$.

Let


$$
C_j(t)=T_j(2t-1),\qquad C_j(i)=a_j+ib_j,
$$


with the original Chebyshev recurrence. Retain the paid Gaussian divisions


$$
g_B=\gcd(b_{N-1},b_N)>0,
$$




$$
\alpha=\frac{b_{N-1}}{g_B},\qquad
\beta=\frac{b_N}{g_B},\qquad
\delta=\frac{a_Nb_{N-1}-a_{N-1}b_N}{g_B}.
$$


Thus


$$
F=\alpha C_N-\beta C_{N-1},\qquad F(\pm i)=\delta.
$$



For integer polynomials,


$$
\eta(H)=\sum_{j\ge0}j![z^j]H(1-z),\qquad
E(H)=\sum_{j\ge0}(-1)^jj![t^j]H(t).
$$


Put


$$
\mathcal H=t(1-t)(1+t^2)^2,\qquad K=\mathcal H C_m^2,
$$




$$
U=-\eta(K),\qquad V=\eta(F^2)-\delta^2,\qquad c=\gcd(U,V).
$$


The actual content and primitive normalization are unchanged:


$$
\operatorname{cont}(W_{\rm raw})=g_B^2c,\qquad
\tau=U/c,\quad \nu=V/c,\quad M=\tau\delta^2.
$$



The reduced $K$-arc is still


$$
R_K=\frac{A_K(\ell^2)}{30(\ell^2-1)(\ell^2-9)(\ell^2-25)}
    =\frac{a_K}{d_K},
$$


in lowest terms, and


$$
y_K=d_KE_K-a_K,\qquad E_K=E(K).
$$


In particular,


$$
\gcd(d_K,y_K)=1.
$$



Retain


$$
\gamma=\gcd(\tau,y_K),\qquad
b^\circ=\gcd(\gamma,a_K),\qquad
r^\circ=\gamma/b^\circ.
$$


The established least-product-multiplier theorem is reused, not reproved. Its exact valuation formula is


$$
\boxed{
k_p:=v_p(\kappa_N^{\mathrm{prod}})
=
[c_p-h_p-2b_p-2(z_p-t_p)_+]_+,
}
\tag{1.1}
$$


where


$$
c_p=\min(v_p(U),v_p(V)),\quad t_p=v_p(U)-c_p,
$$




$$
z_p=v_p(y_K),\quad b_p=v_p(b^\circ),\quad
h_p=v_p(Q_{N-1}^{\mathrm H}Q_N^{\mathrm H}).
$$



All new upper bounds below are reconciled with (1.1).

### 1.1 The arc branch has no endpoint-surplus credit

Suppose


$$
p\ge17,\qquad p\mid2N-1=\ell+5.
$$


Then $p\nmid\ell-5$, while


$$
A_K(25)=450
$$


is a $p$-adic unit. Therefore


$$
v_p(d_K)=v_p(2N-1)>0,\qquad v_p(y_K)=0.
$$


Consequently,


$$
\boxed{z_p=b_p=0,\qquad k_p=[c_p-h_p]_+.}
\tag{1.2}
$$



This remains true at Gaussian exceptional primes. Nothing in the new jet creates endpoint surplus on this branch.

---

## 2. Starting point: the reviewed four-column collision

Write


$$
2N-1=ap,\qquad k=\frac{p+1}{2},\qquad
b=\frac{a-1}{2},\qquad \varsigma=(-1)^b.
$$


Here $a$ is odd and


$$
k\le N,\qquad p\le 2N-1.
$$



Use


$$
\mathscr D=\alpha^2-\beta^2,\qquad
\mathscr S=\alpha^2+\beta^2,
$$


and the evaluated constants


$$
A_{\mathrm H}=1629588422,\qquad
B_{\mathrm H}=395174561,
$$




$$
\mathfrak u=-5227842548,\qquad
\mathfrak e=-14210750303.
$$


Set


$$
L_Q^{(k)}=A_{\mathrm H}Q_k^{\mathrm H}
          +B_{\mathrm H}Q_{k-1}^{\mathrm H},
$$




$$
L_P^{(k)}=A_{\mathrm H}P_k^{\mathrm H}
          +B_{\mathrm H}P_{k-1}^{\mathrm H}.
$$



The reviewed first jets, expressed in the finite $k$-basis, are


$$
\boxed{
\begin{aligned}
4U&\equiv4\mathfrak u-45a\,k!L_Q^{(k)},\\
V&\equiv-\delta^2+2a\,k!\mathscr D Q_k^{\mathrm H},\\
4E_K&\equiv4\mathfrak e+45a\,k!L_P^{(k)},\\
E_F&\equiv2(\alpha+\beta)^2
             +2a\,k!\mathscr D P_k^{\mathrm H}
\end{aligned}
\pmod p.
}
\tag{2.1}
$$



This is the same collision as the turn16 formula in the original $N$-basis. The conversion uses


$$
Q_N^{\mathrm H}\equiv\varsigma Q_k^{\mathrm H},\qquad
P_N^{\mathrm H}\equiv P_k^{\mathrm H}\pmod p.
$$



**That conversion is only modulo $p$.** In the second jet below, $Q_k^{\mathrm H}$ is not silently replaced by $\varsigma Q_N^{\mathrm H}$ modulo $p^2$. The Hermite payment $h_p$ continues to use the actual endpoints $N-1,N$.

All four constants in (2.1) matter:

- $\mathfrak u$;
- the different endpoint constant $\mathfrak e$;
- the source subtraction $-\delta^2$;
- $2(\alpha+\beta)^2=2\alpha^2+4\alpha\beta+2\beta^2$.

---

## 3. A factorial-moment filtration for the second jet

This section gives the new algebraic input. It also accounts for the factorial tail that is absent from a first Frobenius jet.

Let


$$
w=1-2z,\qquad v=z(1-z),
$$


and write $\mathcal U_j$ for the Chebyshev polynomial of the second kind, to distinguish it from the source integer $U$.

Define


$$
R_p(z)=T_p(1-2z)-1,
$$




$$
S_p(z)=\bigl((1-2z)^2-1\bigr)\mathcal U_{p-1}(1-2z).
$$


Thus


$$
S_p=-4v\,\mathcal U_{p-1}(1-2z).
$$



Use the two finite factorial functionals


$$
\mathcal M_+(H)=\sum_j j![z^j]H,\qquad
\mathcal M_-(H)=\sum_j(-1)^jj![z^j]H.
$$



### Lemma 3.1 — The complete factorial bill

For every integer polynomial $J$ and every $r\ge0$,


$$
\boxed{
v_p\bigl(\mathcal M_\pm(JR_p^r)\bigr)\ge r.
}
\tag{3.1}
$$


Moreover,


$$
\boxed{
\begin{aligned}
\mathcal M_+(JR_pS_p)&\equiv
  2p\,\mathcal M_+(JS_p)\pmod{p^2},\\
\mathcal M_-(JR_pS_p)&\equiv
 -2p\,\mathcal M_-(JS_p)\pmod{p^2}.
\end{aligned}}
\tag{3.2}
$$



#### Proof

Polynomial Frobenius gives


$$
R_p\equiv-2z^p\pmod p.
$$


Hence


$$
R_p\in(p,z^p)\subset\mathbb Z_p[z].
$$


Every term in $R_p^r$ is therefore a sum of terms


$$
p^{r-j}z^{pj}H_j(z).
$$


Multiplication by $J$ cannot lower degrees. The corresponding factorial weights have valuation at least $j$, since


$$
v_p((pj)!)\ge j.
$$


This proves (3.1).

For the sharper assertion, the Chebyshev coefficient formula shows that the coefficients of $R_p$ in degrees $1,\ldots,k-1$ are divisible by $p^2$, and those in degrees $k,\ldots,p-1$ are divisible by $p$. Thus


$$
R_p=-2z^p+pG_p+p^2H_p,
$$


where every monomial of $G_p$ has degree at least $k$.

Also,


$$
S_p\equiv(-4)^k v^k\pmod p,
$$


so its reduction modulo $p$ begins in degree $k$. Consequently,


$$
pG_pS_p
$$


has, modulo $p^2$, degree at least $2k=p+1$. Its factorial moment is divisible by $p^2$. Therefore


$$
\mathcal M_\pm(JR_pS_p)
\equiv-2\mathcal M_\pm(z^pJS_p)\pmod{p^2}.
$$



For $0\le j<p$,


$$
(p+j)!\equiv-p\,j!\pmod{p^2}.
$$


Terms with $j\ge p$ vanish modulo $p^2$. Since $p$ is odd,


$$
\mathcal M_+(z^pH)\equiv-p\mathcal M_+(H)\pmod{p^2},
$$




$$
\mathcal M_-(z^pH)\equiv p\mathcal M_-(H)\pmod{p^2}.
$$


Substitution proves (3.2). ∎

The opposite signs in (3.2) are essential. They are a second-order manifestation of the two distinct endpoint functionals.

---

## 4. Evaluation of the new Gaussian scalars

Put


$$
B_p^+=\mathcal M_+(S_p),\qquad
B_p^-=\mathcal M_-(S_p).
$$



These are not left as unspecified moments. They have the following evaluations in the original affine states:


$$
\boxed{
B_p^+
=-2(p+1)+4p(p+1)\Theta_p-2\Theta_{p-1},
}
\tag{4.1}
$$




$$
\boxed{
B_p^-
=2(p+1)+4p(p+1)\Phi_p-2\Phi_{p-1}.
}
\tag{4.2}
$$



Indeed,


$$
S_p=\frac{T_{p+1}(1-2z)-T_{p-1}(1-2z)}2.
$$


Applying the two endpoint formulas and then the recurrence at $p$ gives (4.1)–(4.2). All state indices are at most $p\le n-1$.

Modulo $p$,


$$
B_p^+\equiv4k!Q_k^{\mathrm H},\qquad
B_p^-\equiv4k!P_k^{\mathrm H}.
$$


Thus the following divisions are integral:


$$
\boxed{
\beta_p^+
=\frac{B_p^+-4k!Q_k^{\mathrm H}}p,\qquad
\beta_p^-
=\frac{B_p^--4k!P_k^{\mathrm H}}p.
}
\tag{4.3}
$$


Only their residues modulo $p$ are needed for the second jet.

### 4.1 The $a^2$-correction

For $j=0,1$, put


$$
A_{p,j}^\pm
=\frac1p\mathcal M_\pm(T_j(1-2z)R_p).
$$


Integrality follows from Lemma 3.1.

These four residues are evaluated as


$$
\boxed{
\begin{aligned}
A_{p,0}^+&\equiv-4k!Q_{k-1}^{\mathrm H},\\
A_{p,1}^+&\equiv4k!
 \bigl(Q_k^{\mathrm H}+2Q_{k-1}^{\mathrm H}\bigr),\\
A_{p,0}^-&\equiv4k!P_{k-1}^{\mathrm H},\\
A_{p,1}^-&\equiv4k!
 \bigl(P_k^{\mathrm H}+2P_{k-1}^{\mathrm H}\bigr)
\end{aligned}
\pmod p.
}
\tag{4.4}
$$



Here is a derivation, including the division bill. Since


$$
R_p'=-2p\,\mathcal U_{p-1}(1-2z),
$$


and $R_p(0)=0$, integration by parts for the finite factorial functionals gives


$$
A_{p,0}^+=-2\mathcal M_+(\mathcal U_{p-1}),
$$




$$
A_{p,1}^+=2\mathcal M_+(\mathcal U_{p-1})
             +4\mathcal M_+(z\mathcal U_{p-1}),
$$


and


$$
A_{p,0}^-=2\mathcal M_-(\mathcal U_{p-1}),
$$




$$
A_{p,1}^-=6\mathcal M_-(\mathcal U_{p-1})
             -4\mathcal M_-(z\mathcal U_{p-1}).
$$



Set $r=k-1=(p-1)/2$. Modulo $p$,


$$
\mathcal U_{p-1}(1-2z)\equiv(-4)^rv^r.
$$


The paid Hermite identities give


$$
\mathcal M_+(v^r)=(-1)^rr!Q_r^{\mathrm H},\qquad
\mathcal M_-(v^r)=(-1)^rr!P_r^{\mathrm H}.
$$


Using


$$
(v^{r+1})'=(r+1)(1-2z)v^r
$$


evaluates the moments containing $z$. The only new division is by


$$
r+1=k<p,
$$


a $p$-adic unit. Finally,


$$
r!\equiv2k!\pmod p,\qquad 4^r\equiv1\pmod p,
$$


which yields (4.4).

No prime factor of $g_B$ is inverted in these evaluations.

---

## 5. The evaluated second Gaussian–Hermite jet

Define


$$
a_+=a+\frac{2p}{3}a(a^2-1),\qquad
a_-=a-\frac{2p}{3}a(a^2-1).
\tag{5.1}
$$


These are integers: $3\mid a(a^2-1)$.

### Theorem 5.1 — Complete Gaussian source and endpoint modulo $p^2$

At every original $N$, for every $p\ge17$ dividing $2N-1$,


$$
\boxed{
\begin{aligned}
V\equiv{}&
-\delta^2+\frac{a_+\mathscr D}{2}B_p^+\\
&+\frac{pa^2}{2}
 \bigl(\mathscr S A_{p,1}^+
       -2\alpha\beta A_{p,0}^+\bigr)
\pmod{p^2},
\end{aligned}}
\tag{5.2}
$$


and


$$
\boxed{
\begin{aligned}
E_F\equiv{}&
2(\alpha+\beta)^2+\frac{a_-\mathscr D}{2}B_p^-\\
&+\frac{pa^2}{2}
 \bigl(\mathscr S A_{p,1}^-
       +2\alpha\beta A_{p,0}^-\bigr)
\pmod{p^2}.
\end{aligned}}
\tag{5.3}
$$



Equivalently, after inserting the evaluated residues,


$$
\boxed{
\begin{aligned}
V\equiv{}&
-\delta^2+2ak!\mathscr D Q_k^{\mathrm H}\\
&+p\Bigl[
 \frac{a\mathscr D}{2}\beta_p^+
 +\frac43a(a^2-1)k!\mathscr D Q_k^{\mathrm H}\\
&\hspace{19mm}
 +2a^2k!\bigl(
   \mathscr S Q_k^{\mathrm H}
   +2(\mathscr S+\alpha\beta)Q_{k-1}^{\mathrm H}
 \bigr)
 \Bigr]
\pmod{p^2},
\end{aligned}}
\tag{5.4}
$$


and


$$
\boxed{
\begin{aligned}
E_F\equiv{}&
2(\alpha+\beta)^2+2ak!\mathscr D P_k^{\mathrm H}\\
&+p\Bigl[
 \frac{a\mathscr D}{2}\beta_p^-
 -\frac43a(a^2-1)k!\mathscr D P_k^{\mathrm H}\\
&\hspace{19mm}
 +2a^2k!\bigl(
   \mathscr S P_k^{\mathrm H}
   +2(\mathscr S+\alpha\beta)P_{k-1}^{\mathrm H}
 \bigr)
 \Bigr]
\pmod{p^2}.
\end{aligned}}
\tag{5.5}
$$



The cross coefficient in the second-order term is


$$
\mathscr S+\alpha\beta=\alpha^2+\alpha\beta+\beta^2.
$$


It must not be replaced by $(\alpha+\beta)^2$. The latter occurs in the complete endpoint constant, where the $4\alpha\beta$ contribution remains.

#### Proof

The exact square identity can be organized, in the source coordinate, as


$$
F(1-z)^2
=
\frac{\mathscr S}{2}-\alpha\beta w
+\left(\frac{\mathscr S w}{2}-\alpha\beta\right)
 T_a(1+R_p)
+\frac{\mathscr D}{2}\mathcal U_{a-1}(1+R_p)S_p.
\tag{5.6}
$$



The Taylor coefficients at $1$ are integral, and


$$
T_a(1+R_p)
=1+a^2R_p+\text{terms containing }R_p^2,
$$




$$
\mathcal U_{a-1}(1+R_p)
=a+\frac{a(a^2-1)}3R_p
 +\text{terms containing }R_p^2.
$$


Lemma 3.1 discards the latter terms modulo $p^2$, and (3.2) evaluates the remaining $R_pS_p$ term.

The constant part of (5.6) is


$$
\frac{(\alpha-\beta)^2}{2}(1+w),
$$


whose source factorial moment is zero. The required subtraction of $\delta^2$ therefore leaves exactly $-\delta^2$. This proves (5.2).

At the other endpoint $w=-(1-2z)$, $a$ is odd. The constant part becomes


$$
\frac{(\alpha+\beta)^2}{2}(1+(1-2z)).
$$


Its $\mathcal M_-$-moment is $2(\alpha+\beta)^2$. The sign in the second line of (3.2) gives $a_-$, while the mixed $R_p$-coefficient changes from $-\alpha\beta$ to $+\alpha\beta$. This proves (5.3).

Equations (5.4)–(5.5) follow from (4.3)–(4.4). ∎

### 5.1 Finite-boundary check

Every term used in the exact Gaussian expansion has degree at most $ap+1=n$:

- $T_a(1+R_p)$ has degree $ap$;
- the accompanying factor has degree at most one;
- $S_p$ has degree $p+1$;
- $\mathcal U_{a-1}(1+R_p)S_p$ has degree $ap+1$.

If $a=1$, the term involving $a(a^2-1)$ is zero. Thus the proof also covers the possible large prime


$$
p=2N-1>N
$$


without introducing a polynomial above the physical terminal.

The source-state indices in (4.1)–(4.2) are at most $n-1$, and the largest Hermite index is $k\le N$.

---

## 6. A quantitatively paid part of the actual positive-part mass

Let $\widehat V_{p,N}\in\mathbb Z/p^2\mathbb Z$ denote the completely specified residue in (5.2), or equivalently (5.4). Define


$$
\mathcal T_N=
\{p\ge17:\ p\mid2N-1,\ 
             \widehat V_{p,N}\not\equiv0\pmod{p^2}\}.
\tag{6.1}
$$



This test uses:

- the actual divided Gaussian coefficients modulo $p^2$;
- the original affine states at $p-1,p$;
- Hermite endpoints at $k-1,k$.

It does not use an unpaid raw square, a generic affine triple, or a presumed valuation of $V$.

### Theorem 6.1 — Certified second-jet mass bound

For every original $N$,


$$
\boxed{
p\in\mathcal T_N
\quad\Longrightarrow\quad
k_p\le[1-h_p]_+.
}
\tag{6.2}
$$


Consequently,


$$
\boxed{
\sum_{p\in\mathcal T_N}
[c_p-h_p-2b_p-2(z_p-t_p)_+]_+\log p
\le \log(2N-1).
}
\tag{6.3}
$$



#### Proof

Theorem 5.1 gives


$$
V\equiv\widehat V_{p,N}\pmod{p^2}.
$$


For $p\in\mathcal T_N$, either $v_p(V)=0$ or $v_p(V)=1$. Hence


$$
c_p\le1.
$$


At these arc-denominator primes, (1.2) gives $z_p=b_p=0$. Therefore


$$
k_p=[c_p-h_p]_+\le[1-h_p]_+.
$$


Summing over a subset of the prime divisors of $2N-1$ proves (6.3). ∎

This theorem pays the **full** Hermite credit. For example, if $h_p\ge1$ and $p\in\mathcal T_N$, then $k_p=0$, even if $h_p$ is much larger than one.

It is not asserted that every regular simple-arc prime lies in $\mathcal T_N$. Establishing that inclusion—or controlling its failure—is the outstanding arithmetic problem.

---

## 7. The next $K$-jet and the exact second collision

For the joint collision, the next $K$-coefficient must also be retained.

Suppose first that $a\ge3$, equivalently $p\le N$ on this arc branch. Put


$$
H_+(z)=\mathcal H(1-z),\qquad H_-(z)=\mathcal H(z),
$$




$$
J_\pm(z)=H_\pm(z)T_5(1-2z),
$$


and


$$
U_4^*(z)=5-80v+256v^2.
$$


Define the integral quantities


$$
A_{5,p}^\pm=\frac1p\mathcal M_\pm(J_\pm R_p),
$$




$$
B_{5,p}^\pm=\mathcal M_\pm(H_\pm S_pU_4^*).
\tag{7.1}
$$



These are finite, explicitly evaluable $p$-block coefficients. An exact coefficient formula, with no Gaussian division, is


$$
\mathcal U_{p-1}(1-2z)
=\sum_{r=0}^{p-1}(-4)^r
  \binom{p+r}{2r+1}z^r.
\tag{7.2}
$$


For the divided $A$-coefficients one may avoid division by $p$ altogether:


$$
\boxed{
A_{5,p}^+
=-2\mathcal M_+\left(
 \left(\sum_{j=0}^{11}J_+^{(j)}\right)
 \mathcal U_{p-1}(1-2z)\right),
}
\tag{7.3}
$$




$$
\boxed{
A_{5,p}^-
=2\mathcal M_-\left(
 \left(\sum_{j=0}^{11}(-1)^jJ_-^{(j)}\right)
 \mathcal U_{p-1}(1-2z)\right).
}
\tag{7.4}
$$


These identities follow from $R_p'=-2p\mathcal U_{p-1}$ and finite integration by parts.

The largest polynomial degree here is $p+11$. Since $a\ge3$ and $p\ge17$,


$$
p+11\le 3p+1\le n.
$$


The products used to prove the second-order truncation have degree at most $2p+11\le n$. Thus this calculation is entirely within the original terminal.

The resulting two columns are


$$
\boxed{
2U\equiv2\mathfrak u+a_+B_{5,p}^+
                    -pa^2A_{5,p}^+\pmod{p^2},
}
\tag{7.5}
$$




$$
\boxed{
2E_K\equiv2\mathfrak e-a_-B_{5,p}^-
                    +pa^2A_{5,p}^-\pmod{p^2}.
}
\tag{7.6}
$$


Their first reductions are the reviewed evaluations


$$
B_{5,p}^+\equiv-\frac{45}{2}k!L_Q^{(k)},\qquad
B_{5,p}^-\equiv-\frac{45}{2}k!L_P^{(k)}\pmod p.
$$



Equations (5.2), (5.3), (7.5), and (7.6) retain all four source/endpoint constants and both second-order endpoint signs.

### 7.1 A source-specific second collision invariant

To state a division-free Gaussian version, write


$$
A=b_{N-1},\qquad B=b_N,\qquad
d=a_Nb_{N-1}-a_{N-1}b_N,
$$




$$
D_{\rm raw}=A^2-B^2,\qquad
S_{\rm raw}=A^2+B^2,
$$


and


$$
V_{\rm raw}=g_B^2V.
$$


Set


$$
A_{F,p}^{\rm raw}
=S_{\rm raw}A_{p,1}^+-2AB A_{p,0}^+.
$$



If $p\mid U,V_{\rm raw}$, the following quotient is integral:


$$
\boxed{
\begin{aligned}
\Xi_{p,N}:={}&
\frac{
 2\mathfrak u\,D_{\rm raw}B_p^+
 +2d^2 B_{5,p}^+
}{p}\\
&-a^2\left(
 D_{\rm raw}B_p^+A_{5,p}^+
 +B_{5,p}^+A_{F,p}^{\rm raw}
\right)
\pmod p.
\end{aligned}}
\tag{7.7}
$$


Indeed, eliminating $a_+$ from (5.2) and (7.5) gives


$$
\boxed{
\Xi_{p,N}
\equiv
2\left(
D_{\rm raw}B_p^+\frac Up
-B_{5,p}^+\frac{V_{\rm raw}}p
\right)\pmod p.
}
\tag{7.8}
$$



This is the evaluated next joint obstruction. It contains the actual Gaussian data and the complete source forcing; it is not the first collision renamed.

If $\Xi_{p,N}\ne0$, then $U$ and $V_{\rm raw}$ cannot both be divisible by $p^2$. At $p\nmid g_B$, this proves $c_p\le1$, and hence the same paid bound as (6.2).

What is **not** proved is that $\Xi_{p,N}$ is always nonzero under the regular simple-arc hypotheses. The displayed finite coefficient evaluations do not, by themselves, establish that nonvanishing.

---

## 8. Why a unit slope does not close continuation: genuine original lifts

The obstruction can be demonstrated while retaining the original exponential index domain and the actual Gaussian recurrence.

### Theorem 8.1 — Original-index next-digit splitting

Suppose an original index $N=3^{36+64u}$ and a prime $p\ge17$ satisfy



$$
p\mid2N-1,\qquad v_p(2N-1)=1,\qquad p\le N,
$$




$$
p\mid U,V,
$$




$$
p\nmid g_B\delta\mathscr D\mathfrak u,
$$


and the base-$3$ non-Wieferich condition


$$
\boxed{v_p(3^{p-1}-1)=1.}
\tag{8.1}
$$



Then there is an explicitly defined positive integer $H$, with $p\nmid H$, such that the $p$ indices


$$
u_j=u+jpH,\qquad 0\le j<p,
$$


are all original indices with the same first collision and the same simple arc depth.

Among these $p$ indices:

- exactly one has $p^2\mid V$;
- exactly one has $p^2\mid U$;
- at the other indices, the corresponding source valuation is exactly one.

The two exceptional indices coincide if and only if


$$
\Xi_{p,N}=0.
\tag{8.2}
$$



#### Proof

**Step 1: validate the Gaussian period in the original setting.**

Since $N$ is a square and $2N\equiv1\pmod p$,


$$
\left(\frac2p\right)=1.
$$


At $w=-1+2i$, the Gaussian recurrence matrix is


$$
\mathcal M=
\begin{pmatrix}2w&-1\\1&0\end{pmatrix}.
$$


Its discriminant is $4(w^2-1)$, with


$$
w^2-1=-4(1+i).
$$


It is a unit at $p\ge17$.

If $i\in\mathbb F_p$, the eigenvalues lie in $\mathbb F_{p^2}$. If $i\notin\mathbb F_p$, then


$$
N_{\mathbb F_{p^2}/\mathbb F_p}(w^2-1)=32,
$$


which is a square because $(2/p)=1$. Hence the discriminant is a square in $\mathbb F_{p^2}$, and again the eigenvalues lie there. The matrix is semisimple. Therefore


$$
\mathcal M^{p^2-1}\equiv I\pmod p,
$$


and consequently


$$
\mathcal M^{p(p^2-1)}\equiv I\pmod{p^2}.
\tag{8.3}
$$



Put


$$
d_0=\frac{p^2-1}{3^{v_3(p^2-1)}}.
$$


Because $p+1\le2N$, the $3$-part of $p^2-1$ divides $N$. Choose


$$
H=\operatorname{lcm}\left(
 \operatorname{ord}_{d_0}(3^{64}),
 \operatorname{ord}_{p}(3^{64})
\right),
\tag{8.4}
$$


with order modulo $1$ interpreted as $1$.

Every prime factor of $d_0$ is smaller than $p$, so $p\nmid\varphi(d_0)$, and therefore $p\nmid H$. Condition (8.1) gives


$$
3^{64H}=1+pq\pmod{p^2},
\qquad q\not\equiv0\pmod p.
\tag{8.5}
$$



**Step 2: compute the actual index increment.**

For


$$
N_j=3^{36+64u_j},
$$


equation (8.5) gives


$$
N_j\equiv N(1+p^2qj)\pmod{p^3}.
$$


Writing


$$
2N_j-1=a_jp,
$$


we obtain


$$
\boxed{a_j\equiv a+pqj\pmod{p^2}.}
\tag{8.6}
$$


In particular $a_j\equiv a\not\equiv0\pmod p$, so the arc depth remains one.

The construction of $H$ also gives


$$
p(p^2-1)\mid N_j-N.
$$


Thus (8.3) freezes the raw Gaussian data modulo $p^2$:


$$
A_j\equiv A,\quad B_j\equiv B,\quad d_j\equiv d\pmod{p^2}.
\tag{8.7}
$$


Since $p\nmid g_B$ initially, the two raw imaginary parts do not both vanish modulo $p$; this remains true at every $N_j$. Therefore the actual Gaussian division remains a $p$-adic unit division. It may change by a unit, but


$$
v_p(V_j)=v_p(V_{{\rm raw},j}).
$$



**Step 3: evaluate the two next-digit slopes.**

In the second jets, every term explicitly multiplied by $p$ depends only on $a\bmod p$. Hence (8.6) gives


$$
\frac{V_{{\rm raw},j}-V_{\rm raw}}p
\equiv
qj\,\frac{D_{\rm raw}B_p^+}{2}\pmod p,
\tag{8.8}
$$


and


$$
\frac{U_j-U}{p}
\equiv qj\,\frac{B_{5,p}^+}{2}\pmod p.
\tag{8.9}
$$



The first source collision and $p\nmid\mathfrak u$ imply


$$
p\nmid B_{5,p}^+.
$$


The first Gaussian collision and $p\nmid d$ imply


$$
p\nmid D_{\rm raw}B_p^+.
$$


Thus both slopes in (8.8)–(8.9) are units.

Each affine function of $j\in\mathbb F_p$ consequently has exactly one zero. The two zeros coincide precisely when


$$
D_{\rm raw}B_p^+\frac Up
-B_{5,p}^+\frac{V_{\rm raw}}p
\equiv0\pmod p,
$$


which is (8.2) by (7.8). ∎

### 8.1 What this theorem proves—and what it does not

This is not an example made from freely chosen affine states. Every $u_j$ belongs to the original domain, and the Gaussian data are the actual recurrence values at $N_j$.

It proves an upper source-depth bound at $p-1$ of the $p$ next-digit lifts, with all further depths excluded there. It also proves that a unit slope necessarily leaves one possible deeper lift of each individual source.

It does **not** prove that the two exceptional lifts coincide. Nor does it prove that they never coincide.

If they coincide and $h_p=0$, the regular continuation problem has genuinely reached a common second-depth collision. If $h_p>0$, even a common second-depth collision may be fully paid: the regular lemma concerns depth beyond the **whole** $h_p$, not merely beyond the first source depth.

Thus (8.2), not the existence of unit slopes, is the next noncoincidence obligation.

---

## 9. A uniform higher-precision identity, with the full Hermite credit retained

For completeness, the Gaussian calculation extends to arbitrary precision without extending the physical terminal.

The Taylor coefficients


$$
t_{a,j}=
\frac{2^j a^2\prod_{r=1}^{j-1}(a^2-r^2)}{(2j)!}
\quad(j\ge1),
$$


and


$$
u_{a,j}=
\frac{2^j a\prod_{r=1}^{j}(a^2-r^2)}{(2j+1)!}
\quad(j\ge0)
$$


are integers: they are the actual coefficients of $T_a(1+x)$ and $\mathcal U_{a-1}(1+x)$.

Let


$$
J_F^+=\frac{\mathscr S}{2}(1-2z)-\alpha\beta.
$$


For every $d\ge1$,


$$
\boxed{
\begin{aligned}
V\equiv{}&-\delta^2\\
&+\sum_{j=1}^{\min(a,d-1)}
 t_{a,j}\mathcal M_+(J_F^+R_p^j)\\
&+\frac{\mathscr D}{2}
 \sum_{j=0}^{\min(a-1,d-1)}
 u_{a,j}\mathcal M_+(S_pR_p^j)
\pmod{p^d}.
\end{aligned}}
\tag{9.1}
$$


Lemma 3.1 pays every discarded term.

Every retained term has degree at most $ap+1=n$. The displayed factorial denominators are not inverted modulo $p$; their quotients are first taken as the integral Taylor coefficients they represent.

Taking


$$
d=h_p+2
$$


gives a valid post-Hermite-credit test. If that evaluated residue has valuation at most $h_p+1$, then


$$
c_p\le h_p+1,\qquad k_p\le1.
$$



Equation (9.1) is a rigorous finite-precision identity. It is **not**, without a nonvanishing argument, a proof of the continuation lemma. In particular, writing down its unevaluated higher terms does not bound the depth of a surviving collision. The fully evaluated second-order specialization is Theorem 5.1; higher-order noncoincidence remains open.

---

## 10. The original columns, forcing, returns, and clearing are unchanged

No old thirteen-weight array or closed coefficient calculation is rerun. For self-contained identification of the numerical objects, the smaller corrected centered columns suffice.

At $x=\ell^2$, retain


$$
\begin{aligned}
\mathcal P(x)&=-8x^3-1116x^2-8150x+151,\\
\mathcal Q(x)&=76x^2+2408x+5637,\\
\mathcal F(x)&=4x^2+492x+5463,\\
\mathcal G(x)&=4x^2+556x-3325,
\end{aligned}
$$


and


$$
\widetilde A=2\ell((2\ell+1)\mathcal Q-\mathcal P),
\qquad
\widetilde B=-2\ell\mathcal Q,
$$




$$
\widetilde C_U=\mathcal F-\mathcal P+2\ell\mathcal Q,
\qquad
\widetilde C_E=\mathcal G+\mathcal P-2(\ell+1)\mathcal Q.
$$


Then the complete columns are


$$
16U=\widetilde C_U-\widetilde A\Theta_\ell
                         -\widetilde B\Theta_{\ell-1},
$$




$$
16E_K=\widetilde C_E+\widetilde A\Phi_\ell
                         +\widetilde B\Phi_{\ell-1}.
$$



The divided Gaussian columns remain


$$
V=C_V-P\Theta_n-Q\Theta_{n-1},
$$




$$
E_F=C_F^E-P\Phi_n-Q\Phi_{n-1},
$$


where


$$
P=n\alpha^2+(n-2)\beta^2,
$$




$$
Q=4(n-1)(n-2)\beta^2-2(n-1)\alpha\beta,
$$




$$
C_V=\alpha^2+(2n-3)\beta^2-\delta^2,
$$




$$
C_F^E=\alpha^2+(5-2n)\beta^2+4\alpha\beta.
$$



The two affine states have seeds


$$
\Theta_0=\Phi_0=0,\qquad \Theta_1=\Phi_1=1,
$$


and, for exactly $1\le j\le n-1$,


$$
\Theta_{j+1}+4j\Theta_j-\Theta_{j-1}=2,
$$




$$
\Phi_{j+1}+4j\Phi_j-\Phi_{j-1}=2(-1)^j.
$$


Neither forcing coordinate is removed.

The canonical returns remain


$$
\mathcal R_{r;N}=d_KP_r^{\mathrm H}U+Q_r^{\mathrm H}y_K,
\qquad 0\le r\le N.
$$


With


$$
\Psi_j^{(r)}
=Q_r^{\mathrm H}\Phi_j-P_r^{\mathrm H}\Theta_j,
$$


their complete forced representation is


$$
\begin{aligned}
16\mathcal R_{r;N}
={}&d_K\bigl(
P_r^{\mathrm H}\widetilde C_U+
Q_r^{\mathrm H}\widetilde C_E+
\widetilde A\Psi_\ell^{(r)}+
\widetilde B\Psi_{\ell-1}^{(r)}
\bigr)\\
&-16Q_r^{\mathrm H}a_K,
\end{aligned}
$$


with both forcings


$$
\Psi_{j+1}^{(r)}+4j\Psi_j^{(r)}-\Psi_{j-1}^{(r)}
=2\bigl(Q_r^{\mathrm H}(-1)^j-P_r^{\mathrm H}\bigr).
$$



Both complete arcs are retained:


$$
R_F=4\int_0^1\frac{F^2-\delta^2}{1+t^2}\,dt,\qquad
R_K=4\int_0^1\frac K{1+t^2}\,dt.
$$


The monic quotient degrees remain at most $2N-2$. The square-arc return keeps both forcing terms:


$$
\xi_{j+1}=4\upsilon_j-2\xi_j-\xi_{j-1}+16b_j,
$$




$$
\upsilon_{j+1}
=-4\xi_j-2\upsilon_j-\upsilon_{j-1}
 +16(\ell_j-a_j),
$$


with the original zero seeds, and


$$
\ell_j=0\ \text{for odd }j,\qquad
\ell_j=(1-j^2)^{-1}\ \text{for even }j.
$$



After reducing both arcs,


$$
D=\operatorname{lcm}(\operatorname{den}R_F,\operatorname{den}R_K),
$$




$$
X=D(E_F-R_F),\qquad Y=D(E_K-R_K).
$$


Independently,


$$
\tau R_F+\nu R_K=b/\lambda
$$


is reduced to lowest terms. Then


$$
E=\tau E_F+\nu E_K,\qquad
A=\lambda E-b,\qquad
G=\gcd(M,A),
$$


and


$$
\boxed{p_N=A/G,\qquad q_N=\lambda M/G.}
\tag{10.1}
$$


The final gcd $G$ is over **all primes**.

The source, endpoint, and arc returns from the supplied finite system are not altered by the new local calculation. In particular, there is no new division by their elimination determinant, and neither a local factorial clearer nor a recurrence clearer replaces the actual least $D$.

### 10.1 New scalar and division ledger

| Operation | Payment |
|---|---|
| Division by $g_B$ | The actual original integer division; retained before evaluating $V$ |
| Division by $c$ | The actual content normalization $\tau,\nu$ |
| Factors $1/2$, $1/3$ in the new jets | Units at $p\ge17$; relevant Taylor coefficients are integral |
| $A_{p,j}^\pm/p$, $A_{5,p}^\pm/p$ | Lemma 3.1; alternatively the derivative identities remove the division |
| $\beta_p^\pm$ | Integral by the evaluated first congruence for $B_p^\pm$ |
| Hermite factorials | $k<p$, with actual Hermite index $k\le N$ |
| Raw/divided comparison in Theorem 8.1 | Used only under the explicit hypothesis $p\nmid g_B$ |
| Binary factors in old columns and determinant $2$ | Established payment reused; no modular inversion at $2$ |
| Arc and aggregate clearing | Actual reduced $D,\lambda$, unchanged |
| Final cancellation | Actual all-prime $G$, unchanged |

---

## 11. What remains unpaid, especially for large primes

The established deep-arc cap and binary payment retain their reviewed scope. The new certified set $\mathcal T_N$ adds (6.3).

This still does not give a fixed fractional-factorial saving.

### 11.1 Why the new bound is not quantitatively sufficient

Even if every regular prime dividing $2N-1$ were certified,


$$
\sum_{p\mid2N-1}\log p\le\log(2N-1).
$$


That support is too small, by itself, to establish a fixed saving from a possible $N\log N$ mass.

Theorem 8.1 concerns proportions among original **index lifts at a fixed prime**. The desired estimate is pointwise in each original $N$ and sums over **all primes with their full depths**. These are different assertions. No interchange between them is justified.

### 11.2 The unrestricted $p>N$ obstruction

On the branch $p\mid2N-1$, a prime $p>N$ must be


$$
p=2N-1.
$$


Theorem 5.1 covers that prime, including its Gaussian divisions, but it does not cover the rest of the $p>N$ range.

For $p>2N$, every factorial occurring in the original source moments has $p$-adic valuation zero. The Frobenius-tail mechanism used above therefore supplies no automatic payment. Trying to use the half-prime Hermite index $(p+1)/2$ would exceed $N$, violating the retained finite endpoint range.

For primes $N<p<2N$ not dividing $2N-1$, the source is not on the evaluated $ap\pm1,ap-5$ branch. The four constants and coefficients proved above cannot be transferred to those primes by replacing $N$ with a generic congruent parameter.

Thus this report does **not** establish a quantitatively significant bound for the unrestricted large-prime complement. That is a substantive remaining obligation, not a range paid by the small arc-support estimate.

### 11.3 Concrete next lemma

A precise next local target, at $p\le N$, is:

> **Second-collision nonvanishing lemma — open.**  
> Under the original regular simple-arc hypotheses, and with $p\nmid g_B$, prove that the explicitly evaluated invariant $\Xi_{p,N}$ in (7.7) is nonzero whenever $h_p=0$; or give an upper-depth bound, with a quantitatively summable exceptional contribution, for its vanishing cases.

This is more specific than a unit-slope assertion. Its coefficients are the actual Gaussian data and the finite $p$-block corrections (4.1)–(4.4), (7.1)–(7.4).

For $h_p>0$, the next required noncoincidence is at precision $p^{h_p+2}$, after the whole Hermite credit. Formula (9.1) is available at that precision, but its nonvanishing is not proved.

Even a successful local lemma would still require a separate mechanism for the quantitatively significant complement described above.

---

## 12. One new bounded arithmetic audit

No computation at an original enormous index is proposed. No old source array, deep-band constant evaluation, small-prime scan, or signed-return height calculation should be repeated.

The following single fixed audit is appropriate for the new second-order coefficient receipt. It tests an algebraic identity, not the original-family continuation assertion.

### Inputs

Work modulo


$$
23^2=529,
$$


with


$$
p=23,\qquad k=12,\qquad a=3.
$$



Use:

1. the two original affine recurrences with seeds $0,1$, only through index $70$;
2. the Hermite recurrence only through index $12$;
3. $12!\bmod529$;
4. formal symbols $\alpha,\beta,\delta$.

The comparison index is $N=35$, of terminal degree $70$. It is **not** claimed to be an original index; it is only a bounded check of the universally proved polynomial coefficient identity.

### Expected independently verifiable outputs

The base-block residues are


$$
\Theta_{22}=329,\quad \Theta_{23}=307,\quad \Theta_{24}=124
\pmod{529},
$$




$$
\Phi_{22}=418,\quad \Phi_{23}=204,\quad \Phi_{24}=163
\pmod{529}.
$$


The Hermite residues are


$$
Q_{11}^{\mathrm H}=284,\quad Q_{12}^{\mathrm H}=291,
$$




$$
P_{11}^{\mathrm H}=319,\quad P_{12}^{\mathrm H}=135
\pmod{529},
$$


and


$$
12!\equiv35\pmod{529}.
$$


Consequently,


$$
B_{23}^+\equiv30,\qquad B_{23}^-\equiv523\pmod{529},
$$




$$
\boxed{\beta_{23}^+\equiv1,\qquad
       \beta_{23}^-\equiv6\pmod{23}.}
$$


The four $A$-residues are


$$
(A_{23,0}^+,A_{23,1}^+,
 A_{23,0}^-,A_{23,1}^-)
\equiv(7,16,17,5)\pmod{23}.
$$



For $a=3$, the second-jet formulas must give


$$
\boxed{
V\equiv
344\alpha^2+138\alpha\beta+323\beta^2-\delta^2
\pmod{529},
}
$$




$$
\boxed{
E_F\equiv
292\alpha^2+349\alpha\beta+218\beta^2
\pmod{529}.
}
$$



An independent computation of the complete Gaussian columns at $n=70$, using $\Theta_{68},\Theta_{69},\Theta_{70}$ and their $\Phi$-counterparts, must give exactly those two quadratic coefficient vectors.

This finite audit checks the new signs, the $p$-tail contribution, and the mixed coefficient. It cannot establish nonvanishing of $\Xi_{p,N}$, a uniform multiplier estimate, producer retirement, or irrationality of $e+\pi$.

---

## 13. The actual whole error and final conclusion

The producer remains


$$
P_N(t)=\frac{F(t)^2+(V/U)K(t)}{\delta^2},
$$


with the same positive whole error


$$
\boxed{
\epsilon_N=
\int_0^1P_N(t)\left(e^t+\frac4{1+t^2}\right)\,dt>0.
}
$$


At the same original indices,


$$
\boxed{
q_N(e+\pi)-p_N=q_N\epsilon_N>0,
\qquad q_N=\frac{\lambda_NM_N}{G_N}.
}
$$



The complete rational enclosure is unchanged:


$$
3J_N<\epsilon_N<7J_N,
\qquad
J_N=\frac{J_F+(V/U)J_K}{\delta^2},
$$


where


$$
J_F=
\alpha^2\frac{2N^2-1}{4N^2-1}
+\beta^2\frac{2(N-1)^2-1}{4(N-1)^2-1},
$$


and, writing $j_r=(1-4r^2)^{-1}$,


$$
J_K=\frac{61}{420}
+\frac{
916j_m-399(j_{m+1}+j_{m-1})
-58(j_{m+2}+j_{m-2})
-(j_{m+3}+j_{m-3})
}{8192}.
$$


Thus


$$
q_NJ_N
=\frac{\lambda_N}{G_N}
  \bigl(\tau_NJ_F+\nu_NJ_K\bigr),
$$


with both positive summands retained.

A future strict multiplier estimate would, by the established signed-return implication, force


$$
\log(q_N\epsilon_N)
\ge \frac{\eta}{2}N\log N-O(N)\longrightarrow+\infty
$$


on these same original indices. That would retire this producer only. It would not decide the rationality of $e+\pi$.

### Final proof-status ledger

| Statement | Status |
|---|---|
| Original domain, Gaussian division, physical terminal, complete columns and forcing | Retained |
| Least $D$, least $\lambda$, all-prime $G$, actual $q_N$, whole positive error | Retained |
| Fixed-product theorem, separation, Gaussian division and signed-return bounds | Reused at their stated review scope |
| Evaluated Gaussian source and endpoint modulo $p^2$ | **Proved here** |
| Certified contribution (6.3) to the actual positive-part mass | **Proved here** |
| Original-index next-digit splitting under Theorem 8.1 hypotheses | **Proved here** |
| Explicit second joint collision invariant | **Derived here** |
| Uniform nonvanishing of that invariant | **Open** |
| Regular continuation after the whole Hermite credit | **Open** |
| Quantitatively significant control of unrestricted $p>N$ or $p\nmid d_K$ mass | **Not proved** |
| Fixed $\eta>0$, producer retirement, rationality or irrationality of $e+\pi$ | **Unresolved** |

**The new result is an evaluated second Gaussian–Hermite jet, a certified upper-depth contribution to the least product multiplier, and an original-domain proof of the precise next-lift obstruction. The remaining bottleneck is simultaneous higher-order noncoincidence after the full Hermite credit, together with genuinely significant all-prime control outside the small arc-root support. No strict global multiplier saving or conclusion about $e+\pi$ follows yet.**
