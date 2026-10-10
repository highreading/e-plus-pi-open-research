> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3, Turn 13 — An actual index-transfer system and a paid nonresonance bound for affine excess

## Executive summary

The irrationality of $e+\pi$ remains unresolved.

I accept the new original-index calculation at its stated scope:


$$
\boxed{
\gcd(F,Q\widehat h-P\widehat\ell)=8,\qquad
\mathcal I_{11025}=1.
}
$$


It uses the genuine moment and normalized-reference recurrences. It does **not** calculate the complete force, contact rows, endpoint contents, primitive denominator, or whole error. Together with


$$
\gcd(F,M)_{3375}=128,\qquad \mathcal I_{3375}=1,
$$


it supplies two finite observations, not an infinite-family theorem. Neither calculation is repeated or requested again.

This turn proves three further statements.

1. **The actual fixed-seed alignment problem has a nine-coordinate transfer in the index $n$, not merely a transfer in the coefficient index for fixed $n$.**  
   An exact diagonal generating-function calculation couples the exponential moments to the same algebraic function that generates the Legendre reference. It yields an explicit third-order recurrence for
   

$$
D_n:=a_n(n),
$$


   with genuine initial values, and then an explicit nine-coordinate linear realization of the two evaluated observations $F_n$ and $M_n/L_n$.

   This is a usable interface for propagation between original indices. It does **not** establish that the two observed coordinates generate the unit ideal.

2. **A finite integral Green formula evaluates the seed-subtracted exponential force, including its last permitted source coefficient.**  
   The formula has an integral triangular kernel and terminal coefficient $1$. It therefore cannot silently omit the last source term. It also shows explicitly that the seed-subtracted coefficients have height
   

$$
\log |b_n|,\ \log |b_{n+1}|
   \le \log(n!)+O(n),
$$


   rather than the larger height of the un-subtracted exponential-force coefficients.

   This removes a genuine seed-induced factorial-height term. It does not remove the complete logarithmic constant $\kappa F$.

3. **The nonresonant part of the requested excess has a new paid bound.**  
   Let
   

$$
\mathcal E_j^\circ=\mathcal E_j-E_nR_j
$$


   denote the seed-subtracted exponential projection, not the complete residual. The excess computed using $\mathcal E_j^\circ$ is exactly the same as the excess computed using $\mathcal E_j$. At a large prime, put
   

$$
f=v_p(F),\quad \mu=v_p(M),\quad
   c_j=v_p(\gamma_j),\quad e_j^\circ=v_p(\mathcal E_j^\circ).
$$


   At every prime satisfying the **nonresonance condition**
   

$$
\boxed{\mu+e_j^\circ\ne f+c_j,}
$$


   the excess is paid by alignment and, only on the force-unit chart, an additional actual moment/contact gcd:
   

$$
\boxed{
   \bigl(v_p(\Delta_j)-e_j^\circ\bigr)_+
   \le
   v_p(\mathcal I_n)
   +
   \mathbf 1_{\{e_j^\circ=0\}}
   \min\{v_p(M),v_p(\gamma_j)\}.
   }
   \tag{E1}
$$


   Consequently, the product of the nonresonant excess prime powers divides
   

$$
\boxed{\mathcal I_n\,\gcd(M,\gamma_j)_{>N}.}
   \tag{E2}
$$



This is a genuine paid connection for part of the actual affine excess. It does not bound the resonant part. In particular, the generic unit chart


$$
f=\mu=c_j=e_j^\circ=0
$$


is resonant. Thus (E1) does not exclude the principal force-unit obstruction.

No unconditional subfactorial estimate for $\mathcal I_n$, for the full excess sum, or for the resulting primitive whole forms is obtained.

---

# 1. Scope, source assessment, and notation

Throughout the approximation argument,


$$
n=15^r\quad\text{or}\quad n=105^r,\qquad r\ge2,
$$


with


$$
m=n+1,\qquad N=n+2,\qquad L=2^{m/2}.
$$



All large-prime statements are expressly at $p>N$. This localization is not applied to the final all-prime primitive normalization.

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


Thus


$$
\mathcal I_n=\gcd(|F|,|M|)_{>N}.
$$



The Turn 12 observation determinant, third complete-force identity, payment of the full contact-coordinate content, exact localized ideal equality, and the chain involving $\mathcal Z_j,\mathcal K_j,\mathcal J_j$ are reused at their proved scope. They are not reproved below. Nor is another intersection with $\mathcal W^{\rm ref}$ proposed.

## 1.1 The $11025$ receipt

The supplied code advances the actual moment recurrence from


$$
a_{-2}=a_{-1}=0,\qquad a_0=1,
$$


which produces


$$
a_1=1-n,\qquad a_2=(n-1)^2.
$$


It stores exactly $a_{n-1},a_n,a_{n+1}$. Its normalized reference recurrence starts from $t_0=t_1=1$, and every division by $k+1$ is checked as exact.

The reported smooth factor is $2^3$, the remaining large part is $1$, and the all-prime gcd has four bits. These fields agree with the coordinator’s stated exact value $8$.

The accepted conclusion is therefore exactly


$$
\gcd(F,M)=8,\qquad \mathcal I_{11025}=1.
$$


No further $11025$ field is inferred.

## 1.2 Literature scope

The formal Lagrange inversion, algebraic generating functions, tensor-product realization, integrating-factor formula, and nonarchimedean valuation arguments below are classical machinery. No novelty claim is made for those methods.

I use no irreducibility or Galois theorem as a bound on a gcd of evaluated values. The supplied literature gate identifies no inspected theorem that controls the particular evaluated alignment or affine resonance required here.

---

# 2. A coupled generating function for the actual diagonal moments

The fixed-parameter coefficient recurrence is useful for computing a given original index. For propagation between original indices, a different organization is needed.

Temporarily display the moment parameter:


$$
a_k(d)=k![z^k]e^zq(z)^d,
\qquad q(z)=1-z+\frac{z^2}{2}.
$$



Define


$$
D_n=a_n(n)\qquad(n\ge0),
$$


and


$$
B_0=1,\qquad B_n=a_{n-1}(n)\qquad(n\ge1).
$$


The auxiliary values $n=0,1,2,\ldots$ in this section define a recurrence and its seeds. They do not enlarge the approximation domain.

Put


$$
s(t)=\sqrt{1+2t-t^2},
$$


with constant term $1$, and let $w(t)$ be the unique formal solution of


$$
w=tq(w),\qquad w(0)=0.
$$


Explicitly,


$$
w(t)=\frac{1+t-s(t)}t.
$$



## Theorem 2.1 — Exact diagonal coupling

In $\mathbb Q[[t]]$,


$$
\boxed{
\mathscr A(t):=\sum_{n\ge0}D_n\frac{t^n}{n!}
=\frac{e^{w(t)}}{s(t)},
}
\tag{2.1}
$$


and


$$
\boxed{
\mathscr J(t):=\sum_{n\ge0}B_n\frac{t^n}{n!}
=e^{w(t)}.
}
\tag{2.2}
$$



Since


$$
\sum_{n\ge0}\tau_nt^n=\frac1{\sqrt{1-2t-t^2}},
$$


the actual coupling is


$$
\boxed{
\mathscr A(t)
=
\mathscr J(t)\sum_{n\ge0}(-1)^n\tau_nt^n.
}
\tag{2.3}
$$



### Proof

The diagonal form of Lagrange inversion gives, for a formal series $\phi$,


$$
\sum_{n\ge0}[z^n]\phi(z)q(z)^n\,t^n
=
\frac{\phi(w)}{1-tq'(w)}.
$$


Here


$$
1-tq'(w)=1+t-tw=s(t).
$$


Taking $\phi(z)=e^z$ proves (2.1).

For $n\ge1$, ordinary Lagrange inversion gives


$$
[t^n]e^{w(t)}
=
\frac1n[z^{n-1}]e^zq(z)^n
=
\frac{a_{n-1}(n)}{n!}.
$$


The constant term is $1=B_0$, proving (2.2).

Finally, $s(t)^{-1}$ is the Legendre-reference generating function with $t$ replaced by $-t$, proving (2.3). ∎

Equation (2.3) is an exact coupling with the genuine exponential seed. It is not a pointwise proportionality between $D_n$ and $\tau_n$. Its coefficient at degree $n$ is a convolution involving all earlier $B_k$.

That distinction is important: an evaluated congruence at degree $n$ does not permit cancellation of the formal factor $e^{w(t)}$.

---

# 3. An explicit recurrence in the parameter $n$

The two series in Theorem 2.1 satisfy a small differential system.

## Proposition 3.1 — Differential interface

Writing


$$
d(t)=1+2t-t^2,
$$


one has


$$
\boxed{
t^2\mathscr J'
=-\mathscr J+(1+t)\mathscr A,
}
\tag{3.1}
$$




$$
\boxed{
t^2d(t)\mathscr A'
=
(1+t)\mathscr J
+(1+t)(t^2-t-1)\mathscr A.
}
\tag{3.2}
$$



### Proof

Differentiating $w=tq(w)$ gives


$$
w'=\frac{w}{ts}.
$$


Since $\mathscr J=e^w=s\mathscr A$,


$$
\mathscr J'
=\frac{w}{t}\mathscr A
=\frac{(1+t)\mathscr A-\mathscr J}{t^2},
$$


which is (3.1).

Also,


$$
\frac{\mathscr A'}{\mathscr A}
=w'-\frac{s'}s
=\frac{w}{ts}-\frac{1-t}{d(t)}.
$$


Using $s=1+t-tw$ and $s^2=d(t)$ reduces this expression to (3.2). ∎

The coefficient equations yield a recurrence with fixed initial values.

## Theorem 3.2 — Actual diagonal moment recurrence

The sequence $D_n=a_n(n)$ has


$$
\boxed{D_0=1,\qquad D_1=0,\qquad D_2=1,}
\tag{3.3}
$$


and, for every $k\ge3$,


$$
\boxed{
\begin{aligned}
2(k-2)D_k={}&
-(k-1)(k^2+2k-6)D_{k-1}\\
&+(k-1)^2(k-2)(3-2k)D_{k-2}\\
&+(k-1)^3(k-2)^2D_{k-3}.
\end{aligned}}
\tag{3.4}
$$



For $n\ge2$,


$$
\boxed{
B_n
=
-\frac{n+1}{n-1}D_n
-2nD_{n-1}
+n(n-1)D_{n-2}.
}
\tag{3.5}
$$



Every displayed division evaluates exactly for these fixed-seed sequences.

### Derivation

Coefficient extraction from (3.1) gives


$$
B_n=D_n+nD_{n-1}-n(n-1)B_{n-1}.
\tag{3.6}
$$


Combining coefficients in (3.1)–(3.2) gives


$$
(n+1)D_n+(n-1)B_n
+2n(n-1)D_{n-1}
-n(n-1)^2D_{n-2}=0.
\tag{3.7}
$$


This proves (3.5).

Substitute (3.5) and its index-$(n-1)$ version into (3.6), and clear the displayed factors $n-1,n-2$. The result is (3.4).

The initial values follow directly from the defining moments. The recurrence is started at $k=3$; its singular coefficient at $k=2$ is not divided through. ∎

This finite lower boundary is part of the result. In particular, $D_2$ is a genuine seed, not a value inferred from a singular recurrence step.

---

# 4. Recovering the original terminal moments and alignment observations

The recurrence above advances the parameter $n$. It must still recover the terminal moments belonging to that same parameter.

Multiplication by $q(z)$ gives the exact identity


$$
\boxed{
a_{n+1}(n)
=
D_{n+1}+(n+1)D_n-\frac{n(n+1)}2B_n.
}
\tag{4.1}
$$


This is a relation between already defined coefficients. It adds no physical matrix row and changes no force cutoff.

Consequently,


$$
\boxed{
Z=2D_{n+1}+mD_n-mnB_n,
}
\tag{4.2}
$$




$$
\boxed{P=mn(D_n+B_n),}
\tag{4.3}
$$




$$
\boxed{
Q=nZ+2mD_n-mnB_n,
}
\tag{4.4}
$$


and


$$
\boxed{
F
=
2m\left(
mn^2B_n-m^2D_n-2(n-1)D_{n+1}
\right).
}
\tag{4.5}
$$



Thus the original $F,P,Q$ are explicit linear observations of a three-coordinate state propagated in $n$.

## 4.1 The moment transfer

For $n\ge2$, put


$$
x_n=(D_n,D_{n-1},D_{n-2})^T.
$$


Then


$$
x_{n+1}=\mathsf T_nx_n,
$$


where


$$
\boxed{
\mathsf T_n=
\begin{pmatrix}
-\dfrac{n(n^2+4n-3)}{2(n-1)}
&
\dfrac{n^2(1-2n)}2
&
\dfrac{n^3(n-1)}2\\[2mm]
1&0&0\\
0&1&0
\end{pmatrix}.
}
\tag{4.6}
$$


Its genuine initial state is


$$
\boxed{x_2=(1,0,1)^T.}
\tag{4.7}
$$



The row


$$
\mathsf b_n=
\left(
-\frac{n+1}{n-1},\ -2n,\ n(n-1)
\right)
$$


gives $B_n=\mathsf b_nx_n$. Equations (4.2)–(4.5) then give explicit rows


$$
\mathsf p_n,\quad \mathsf q_n,\quad \mathsf f_n
$$


such that


$$
P=\mathsf p_nx_n,\qquad
Q=\mathsf q_nx_n,\qquad
F=\mathsf f_nx_n.
$$



All denominators introduced here have prime support at most $n+2$.

## 4.2 The reference transfer

Put


$$
y_n=(\tau_{n+1},\tau_n)^T.
$$


The reference recurrence gives


$$
y_{n+1}=\mathsf V_ny_n,
\qquad
\boxed{
\mathsf V_n=
\begin{pmatrix}
\dfrac{2n+3}{n+2}&\dfrac{n+1}{n+2}\\[2mm]
1&0
\end{pmatrix},
}
\tag{4.8}
$$


with


$$
\boxed{y_2=(4,2)^T.}
\tag{4.9}
$$



## Theorem 4.1 — Nine-coordinate actual alignment realization

Define


$$
\mathfrak s_n=
\binom{x_n}{x_n\otimes y_n}\in\mathbb Q^9.
$$


Then


$$
\boxed{
\mathfrak s_{n+1}
=
\operatorname{diag}
\bigl(\mathsf T_n,\mathsf T_n\otimes\mathsf V_n\bigr)
\mathfrak s_n.
}
\tag{4.10}
$$



The two observations are


$$
\boxed{F_n=\mathsf f_nx_n,}
$$


and


$$
\boxed{
\frac{M_n}{L_n}
=
\bigl(\mathsf q_n\otimes(0,1)
-\mathsf p_n\otimes(1,0)\bigr)
(x_n\otimes y_n).
}
\tag{4.11}
$$



At every original target $n$, these are exactly the original fixed-seed $F_n,M_n$.

### Proof

The tensor-product identity follows from


$$
(\mathsf T_nx_n)\otimes(\mathsf V_ny_n)
=(\mathsf T_n\otimes\mathsf V_n)(x_n\otimes y_n).
$$


Equation (4.11) is


$$
Q\tau_n-P\tau_{n+1}=M/L.
$$


The preceding derivations identify every moment observation with the actual parameter-$n$ coefficient. ∎

For reference,


$$
\det\mathsf T_n=\frac{n^3(n-1)}2,\qquad
\det\mathsf V_n=-\frac{n+1}{n+2}.
$$


Hence the nine-coordinate determinant is


$$
\left(
-\frac{n^3(n-1)(n+1)}{2(n+2)}
\right)^3.
$$



This determinant records the exact paid transfer factors. It is **not** used to infer primitivity of the two observations.

---

# 5. What this does—and does not—prove about $\mathcal I_n$

The new interface differs from the Turn 12 transfer in a substantive way:

* Turn 12 propagated coefficients for a **fixed parameter** $n$.
* Equations (4.6)–(4.11) propagate the **actual diagonal family in $n$**.

Thus multiplicative blocks


$$
n\longmapsto 15n,\qquad n\longmapsto105n
$$


can now be expressed by explicit products of fixed-size matrices, starting from a fixed seed.

Nevertheless, the missing arithmetic step remains an observation problem. The nine-coordinate state can be primitive while both evaluated observations vanish modulo a prime power.

The generating-function identity


$$
\mathscr A=\mathscr J/s
$$


does not repair that problem: its coefficient interface is a convolution. An endpoint congruence for two coefficients is not stable under cancellation of $\mathscr J$, differentiation, or extraction of an inverse series.

I therefore obtain neither


$$
\mathcal I_n=1
$$


nor


$$
\log\mathcal I_n=o(n\log n).
$$



## 5.1 A concrete propagation lemma now available for attack

The explicit matrices permit a sharper follow-on target than “use transfer invertibility.”

For $b=15$ or $105$, a sufficient lemma would supply a positive integer $c_{b,n}$ with


$$
\log c_{b,n}=O(n),
$$


and evaluated identities


$$
\boxed{
\begin{aligned}
c_{b,n}F_n&=A_{b,n}F_{bn}+B_{b,n}M_{bn},\\
c_{b,n}M_n&=C_{b,n}F_{bn}+D_{b,n}M_{bn},
\end{aligned}}
\tag{5.1}
$$


where the coefficients lie in


$$
\mathbb Z\bigl[1/p:\ p\le bn+2\bigr].
$$



The coefficients must be derived for the actual state transported by (4.10), not for freely chosen homogeneous states.

Such identities would imply


$$
\mathcal I_{bn}
\mid
(c_{b,n})_{>bn+2}\,
(\mathcal I_n)_{>bn+2}.
$$


Iteration along a geometric sequence would give


$$
\log\mathcal I_{b^r}=O(b^r),
$$


hence the desired subfactorial bound.

Equation (5.1) is an outstanding evaluated Bézout-propagation obligation. It is not proved by the matrix determinants, and I do not claim it here.

---

# 6. A finite integral Green interface for the whole exponential source

We next address the force side, keeping the original cutoff.

For fixed original $n$, retain


$$
H_n(z)=\frac{q(z)^n}{(1-z)^m}
=\sum_{k\ge0}h_k\frac{z^k}{k!},
$$


and the seed-subtracted series


$$
B_n(z)=\Omega_n(z)-E_nH_n(z)-A_n(z)
=\sum_{k\ge0}b_k\frac{z^k}{k!}.
$$



To avoid ambiguity, $B_n(z)$ in this section is the force series; the integer $B_n$ in Sections 2–4 was the diagonal moment $a_{n-1}(n)$.

The retained differential identity is


$$
\left(\frac{B_n}{H_n}\right)'
=(m+z)e^z(1-z)^n,
$$


with $b_0=-1$. Hence


$$
\boxed{
B_n(z)
=
H_n(z)\left[
-1+\int_0^z(m+t)e^t(1-t)^n\,dt
\right].
}
\tag{6.1}
$$



This formula can be made completely finite and integral.

## 6.1 Direct integral source coefficients

Define


$$
g_r=r![z^r]e^z(1-z)^n
=
\sum_{s=0}^{\min(n,r)}
(-1)^s\binom ns(r)_s,
$$


and


$$
\nu_r=mg_r+r g_{r-1},
\qquad g_{-1}=0.
$$


These are integers.

Coefficient extraction in (6.1) gives


$$
\boxed{
b_k
=
-h_k+
\sum_{r=0}^{k-1}
\binom{k}{r+1}\nu_rh_{k-r-1}.
}
\tag{6.2}
$$



In particular,


$$
b_0=-1,\qquad b_1=n,\qquad b_2=n+2-n^2.
$$


Thus the genuine lower boundary is preserved.

## 6.2 Green kernel for the original $F_i$

Let


$$
W_n(z)=\frac{(1-z)^n}{q(z)^{n+1}}
=\sum_{r\ge0}\omega_r\frac{z^r}{r!}.
$$


Each $\omega_r$ is integral.

One direct integrality proof expands


$$
q(z)^{-n-1}
=
\sum_{a\ge0}\binom{n+a}{a}
\left(z-\frac{z^2}{2}\right)^a.
$$


A coefficient of degree $r$ has dyadic denominator dividing
$2^{\lfloor r/2\rfloor}$, which is cleared by $r!$. Multiplication by $(1-z)^n$ preserves factorial-normalized integrality.

The complete force series is


$$
\sum_{i\ge0}F_i\frac{z^i}{i!}
=q(z)(m+z)A_n(z).
$$


Therefore


$$
W_n(z)\sum_{i\ge0}F_i\frac{z^i}{i!}
=(m+z)e^z(1-z)^n,
$$


so


$$
\nu_r=\sum_{i=0}^r\binom ri\omega_{r-i}F_i.
$$



Substitution into (6.2) yields:

## Theorem 6.1 — Finite integral whole-source Green formula

For $k\ge1$,


$$
\boxed{
b_k=-h_k+\sum_{i=0}^{k-1}\mathsf G_{k,i}F_i,
}
\tag{6.3}
$$


where


$$
\boxed{
\mathsf G_{k,i}
=
\sum_{r=i}^{k-1}
\binom{k}{r+1}\binom ri
\omega_{r-i}h_{k-r-1}
\in\mathbb Z.
}
\tag{6.4}
$$


Moreover,


$$
\boxed{\mathsf G_{k,k-1}=1.}
\tag{6.5}
$$



### Boundary proof

All sums in (6.3)–(6.4) are finite. At the upper edge $i=k-1$, only $r=k-1$ occurs, and


$$
\binom kk\binom{k-1}{k-1}\omega_0h_0=1.
$$


Thus the last source $F_{k-1}$ appears with coefficient exactly $1$.

Let the retained source cutoff be


$$
K=2n+2.
$$


The formula through $b_{K+1}$ uses exactly $F_0,\ldots,F_K$, and no source beyond $K$. In the differential equation, coefficients through degree $K$ depend only on $b_0,\ldots,b_{K+1}$. Hence this finite solution agrees with the retained recurrence at every permitted source row.

The retained terminal-return functional is applied to these same coefficients. It is not replaced by a new terminal condition, and no recurrence row after the original cutoff is appended. In particular, deleting $F_K$ would change the last propagated coefficient by $F_K$; it is not a harmless truncation. ∎

This theorem gives the exact finite source interface needed for a recurrence-based argument about the force. It is not an unevaluated generic telescoping specification.

---

# 7. Seed subtraction preserves the requested excess and removes one height term

For each actual primitive contact row $r_j$, $j=0,3$, retain


$$
\alpha_j=r_jv',\qquad
\beta_j=r_jw',\qquad
\gamma_j=r_je_2.
$$



Define


$$
A^\circ=\frac m2b_n,\qquad
B^\circ=b_{n+1}-\frac m2b_n,\qquad
C=mZ,
$$


and


$$
\boxed{
\mathcal E_j^\circ
=
A^\circ\alpha_j+B^\circ\beta_j+C\gamma_j.
}
\tag{7.1}
$$



Using


$$
h_n=n!\tau_n,\qquad
h_{n+1}=\frac m2n!(\tau_n+\tau_{n+1}),
$$


one obtains the exact identity


$$
\boxed{
\mathcal E_j
=
\mathcal E_j^\circ
+
E_n\,\frac{mn!}{2L}\,\widehat R_j
=
\mathcal E_j^\circ+E_nR_j.
}
\tag{7.2}
$$



The multiplier $mn!/(2L)$ is integral throughout the original domain. Indeed, for odd $n\ge7$,


$$
v_2(n!)\ge \left\lfloor\frac n2\right\rfloor+
\left\lfloor\frac n4\right\rfloor
\ge\frac{n+1}{2},
$$


and $m/2$ is integral.

## Proposition 7.1 — Exact invariance of excess under seed subtraction

For


$$
k_j=v_p(\Delta_j)=\min\{v_p(\Theta),v_p(\widehat R_j)\},
$$


one has


$$
\boxed{
(k_j-v_p(\mathcal E_j))_+
=
(k_j-v_p(\mathcal E_j^\circ))_+.
}
\tag{7.3}
$$



### Proof

The difference in (7.2) is divisible by $\widehat R_j$, hence has valuation at least $k_j$.

If $v_p(\mathcal E_j)<k_j$, subtracting a term of valuation at least $k_j$ leaves that valuation unchanged. If $v_p(\mathcal E_j)\ge k_j$, both sides of (7.3) are zero. ∎

Thus seed subtraction is legitimate for the requested excess sum. It is not a substitution of a different error.

## 7.1 Explicit height gain

Take $|z|=1/4$. Then


$$
|H_n(z)|
\le
\frac43\left(\frac{41}{24}\right)^n,
$$


and


$$
|(m+z)e^z(1-z)^n|
\le
\left(m+\frac14\right)e^{1/4}\left(\frac54\right)^n.
$$


Equation (6.1) and Cauchy’s estimate give, uniformly for $k\le2n+3$,


$$
|b_k|\le k!\,e^{O(n)}.
$$


In particular,


$$
\boxed{
|b_n|+|b_{n+1}|\le n!\,e^{O(n)}.
}
\tag{7.4}
$$


The same elementary coefficient estimate bounds the moments in $Z$. Therefore


$$
\boxed{
|\mathcal E_j^\circ|
\le
n!\,e^{O(n)}
\bigl(|\alpha_j|+|\beta_j|+|\gamma_j|\bigr).
}
\tag{7.5}
$$



This is a real, paid height reduction in the exponential projection.

It does **not** remove the complete logarithmic contribution. The actual complete residual is still


$$
\boxed{
C_j^{\rm complete}
=
\mathcal E_j^\circ
+
2n!m!\,
(\alpha_j\rho_n+\beta_j\rho_{n+1}).
}
\tag{7.6}
$$


Equivalently, it is the retained


$$
\mathcal E_j-E_nR_j+
2n!m!(\alpha_j\rho_n+\beta_j\rho_{n+1}).
$$



---

# 8. A paid bound for the nonresonant affine excess

Set


$$
D^\circ=QA^\circ-PB^\circ,
\qquad
\kappa=2L(n!)^2.
$$


Seed subtraction leaves the canonical scalar unchanged:


$$
\Theta
=
CM-F(\widehat hB^\circ-\widehat\ell A^\circ)+\kappa F.
$$



The retained third complete-force identity, after the exact substitution (7.2), is


$$
\boxed{
\gamma_j\Theta+D^\circ\widehat R_j
=
M\mathcal E_j^\circ+\kappa F\gamma_j.
}
\tag{8.1}
$$


The first two identities likewise hold with the seed-subtracted coefficients.

The constant $\kappa F$ remains present. At $p>N$, $\kappa$ is a unit.

Fix such a prime and write


$$
k=v_p(\Delta_j),\quad
e=v_p(\mathcal E_j^\circ),\quad
f=v_p(F),\quad
\mu=v_p(M),\quad
c=v_p(\gamma_j),
$$


and


$$
a=\min(f,\mu)=v_p(\mathcal I_n).
$$


Use $v_p(0)=+\infty$.

Call the prime **nonresonant for endpoint $j$** when


$$
\boxed{\mu+e\ne f+c.}
\tag{8.2}
$$


If $\mathcal E_j^\circ=0$, the excess is zero and needs no bound.

## Theorem 8.1 — Nonresonant excess bound

At a nonresonant prime with finite $e$,


$$
\boxed{
(k-e)_+
\le
a+\mathbf1_{\{e=0\}}\min(\mu,c).
}
\tag{8.3}
$$


In particular, if $e>0$,


$$
\boxed{(k-e)_+\le v_p(\mathcal I_n).}
\tag{8.4}
$$



### Proof

Both terms on the left of (8.1) are divisible by $p^k$. Hence


$$
k\le v_p(M\mathcal E_j^\circ+\kappa F\gamma_j).
$$


Under nonresonance, the two summands have unequal valuations, so


$$
\boxed{k\le\min(\mu+e,f+c).}
\tag{8.5}
$$



**Case 1: $e=0$.**  
Then


$$
k\le\min(\mu,f+c).
$$


The elementary inequality


$$
\min(\mu,f+c)
\le \min(\mu,f)+\min(\mu,c)
$$


proves (8.3).

**Case 2: $e>0$ and $c=0$.**  
Equation (8.5) gives


$$
(k-e)_+
\le \bigl(\min(\mu+e,f)-e\bigr)_+
\le\min(\mu,f)=a.
$$



**Case 3: $e>0$ and $c>0$.**  
The full contact-coordinate content is a unit at $p>N$. Therefore at least one of $\alpha_j,\beta_j$ is a unit.

If $\alpha_j$ is a unit, the first seed-subtracted affine identity has right side


$$
F(\widehat\ell\,\mathcal E_j^\circ+\kappa\alpha_j).
$$


Its parenthesis is a unit, because $e>0$ and $\kappa\alpha_j$ is a unit. Thus $k\le f$. The second identity gives the same conclusion when $\beta_j$ is the unit.

We therefore have


$$
(k-e)_+\le(f-e)_+\le f.
$$



If $\mu+e<f+c$, equation (8.5) also gives


$$
(k-e)_+\le\mu.
$$


If $\mu+e>f+c$, then


$$
\mu>f+c-e\ge f-e,
$$


so again


$$
(k-e)_+\le\mu.
$$


Together these give $(k-e)_+\le\min(f,\mu)=a$. ∎

## 8.1 Global paid connection

Let $\mathcal N_j$ be the product of the excess prime powers at nonresonant primes:


$$
\mathcal N_j
=
\prod_{\substack{p>N\\ \mu+e\ne f+c}}
p^{(k-e)_+}.
$$


When $M,\gamma_j$ are not both zero, Theorem 8.1 implies


$$
\boxed{
\mathcal N_j
\mid
\mathcal I_n\,\gcd(|M|,|\gamma_j|)_{>N}.
}
\tag{8.6}
$$


If $M=\gamma_j=0$, both terms in (8.1) have infinite valuation at every prime, so there are no nonresonant primes; then $\mathcal N_j=1$.

Thus


$$
\boxed{
\log\mathcal N_j
\le
\log\mathcal I_n+
\log\gcd(|M|,|\gamma_j|)_{>N}.
}
\tag{8.7}
$$



This is not merely a new name for the original excess sum. It gives a divisibility bound for a specified part of that sum in terms of an actual moment/contact gcd, with alignment paid once.

No subfactorial estimate for the additional gcd is proved.

---

# 9. The exact obstruction left by resonance

Theorem 8.1 leaves the primes satisfying


$$
\boxed{
v_p(M)+v_p(\mathcal E_j^\circ)
=
v_p(F)+v_p(\gamma_j).
}
\tag{9.1}
$$



At such a prime, the two terms


$$
M\mathcal E_j^\circ,\qquad \kappa F\gamma_j
$$


have the same valuation. Their unit parts may cancel to higher depth. The nonzero constant $\kappa F\gamma_j$ is precisely what makes this an affine problem rather than a homogeneous content problem.

The most important unresolved chart is


$$
p\nmid FM\gamma_j\mathcal E_j^\circ.
$$


Here both sides of (9.1) are zero automatically. The nonresonance theorem supplies no exclusion at all.

This is why neither the exact ideal equality nor the new Green formula finishes the depth estimate:

* the ideal equality controls the force-overlap part;
* the Green formula evaluates the remaining force with the correct seed and terminal source;
* but neither controls cancellation between the two evaluated unit terms in (8.1).

The explicit Green formula identifies the remaining arithmetic object without introducing a generic resultant:


$$
\mathcal E_j^\circ
=
\frac m2(\alpha_j-\beta_j)
\left(-h_n+\sum_{i=0}^{n-1}\mathsf G_{n,i}F_i\right)
+
\beta_j
\left(-h_{n+1}+\sum_{i=0}^{n}\mathsf G_{n+1,i}F_i\right)
+
mZ\gamma_j.
\tag{9.2}
$$


Every coefficient and boundary term in this expression has been specified and proved integral.

A successful resonance theorem must use additional arithmetic of this evaluated finite sum, the actual contact row, and the actual moment/reference state. Polynomial irreducibility does not supply such a theorem.

## 9.1 A sufficient next affine lemma

A concrete sufficient continuation is:

> **Evaluated resonant Green-lift lemma.**  
> On an infinite original subsequence, prove
> 

$$
> \sum_{j=0,3}
> \log\gcd(|M_n|,|\gamma_j|)_{>N}
> =o(n\log n),
>
$$


> together with
> 

$$
> \sum_{j=0,3}
> \sum_{\substack{p>N\\
> v_p(M)+v_p(\mathcal E_j^\circ)
> =
> v_p(F)+v_p(\gamma_j)}}
> \bigl(v_p(\Delta_j)-v_p(\mathcal E_j^\circ)\bigr)_+
> \log p
> =o(n\log n),
>
$$


> using the finite Green expression (9.2), including its genuine initial value and upper boundary.

Combined with a subfactorial alignment estimate and the retained overlap theorem, this would bound the full requested excess.

This is a sufficient lemma, not a theorem proved in this report. The new content is the explicit index-transfer and finite-force interfaces, and the proved payment of the nonresonant part.

---

# 10. Construction and normalization remain unchanged

None of the preceding identities changes the endpoint construction.

## 10.1 Both contacts and all source/collision contents

Both endpoints $j=0,3$ use their actual primitive contact rows. No raw adjugate row replaces them, and no coordinate gcd is silently divided out.

The source content $\mathcal B_n$, full collision depth $\Sigma_n$, reference collision ceiling $H_n^{\rm ref}$, exclusive reference filters $V_{j,n}$, and $\mathcal W_n^{\rm ref}$ retain their previous definitions and full valuations.

In particular:

* source content is removed before the collision comparison;
* the full collision depth, not its radical, is removed from each reference before the exclusive gcd;
* the new factor $\gcd(M,\gamma_j)_{>N}$ is a paid factor in (8.6), not a replacement for a source or collision content;
* no second intersection with an already stronger certificate is asserted to improve it.

## 10.2 Original force and terminal boundary

The force remains


$$
F_k=(n+1)a_k-nk\,a_{k-1}
+\frac{(n-1)k(k-1)}2a_{k-2}
+\frac{k(k-1)(k-2)}2a_{k-3}
$$


through


$$
K=2n+2,
$$


with the complete retained terminal return.

Theorem 6.1 evaluates that same finite source. It neither omits the terminal source nor adds a new source beyond the cutoff.

## 10.3 Both corrected reconstruction columns

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


The exterior $+1$ in $v_0$ remains.

The least simultaneous clearer is over all eight entries. Every reconstructed row is then divided by its actual two-entry content. The accepted $3375$ contents remain


$$
(113940000,\ 9780750,\ 10125,\ 1).
$$


They are not contact-row contents and are not replaced by any large-prime gcd in this report.

## 10.4 All-prime endpoint and weighted normalization

The endpoint denominator remains


$$
\boxed{
d_j=
\frac{|n!R_j|}
{\gcd(|n!R_j|,\ |E_nR_j+C_j^{\rm complete}|)}.
}
\tag{10.1}
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
\tag{10.2}
$$



Every prime remains in these final gcds. The large-prime arguments above do not alter this normalization.

## 10.5 Whole nonzero same-index error

The whole evaluated error remains


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda e_3\alpha_{n,2}
(\lambda-\Lambda_{n,2}).
}
\tag{10.3}
$$



The five accepted $3375$ whole forms remain nonzero and have absolute value greater than $1$. Nothing proved here changes those finite evaluations.

Neither $\Theta_n\ne0$ nor a finite value $\mathcal I_n=1$ proves nonvanishing or smallness of a proposed primitive whole form.

---

# 11. Proof status and bounded arithmetic

## 11.1 Status ledger

| Statement | Status |
|---|---|
| $\gcd(F,M)_{11025}=8,\ \mathcal I_{11025}=1$ | Accepted exact finite computation |
| $\gcd(F,M)_{3375}=128,\ \mathcal I_{3375}=1$ | Retained exact finite computation |
| Exact diagonal coupling with the Legendre generating function | Proved |
| Third-order recurrence for $D_n=a_n(n)$, with genuine seeds | Proved |
| Nine-coordinate transfer for actual $F_n,M_n/L_n$ | Proved |
| Infinite-family $\mathcal I_n=1$ | Neither proved nor disproved |
| Subfactorial bound for $\mathcal I_n$ | Not proved |
| Integral finite Green formula, including terminal source coefficient $1$ | Proved |
| Exact invariance of excess under seed subtraction | Proved |
| Seed-subtracted force coefficient height $\log(n!)+O(n)$ | Proved |
| Nonresonant excess divisibility (8.6) | Proved |
| Subfactorial bound for the resonant excess | Not proved |
| Successful all-prime weighted denominator/whole-error comparison | Not proved |
| Irrationality of $e+\pi$ | Unresolved |

## 11.2 Numerical execution

No code has been executed for this report.

No regeneration of either accepted alignment calculation is requested. No old producer, endpoint gcd, primitive denominator, or whole-error computation is proposed again.

The new theorems are proved symbolically and require no bounded numerical calculation for their validity. Their independently checkable exact outputs are already explicit:

* seeds $D_0,D_1,D_2=(1,0,1)$;
* reference seed $y_2=(4,2)$;
* recurrence (3.4);
* observation identities (4.2)–(4.5);
* Green boundary $\mathsf G_{k,k-1}=1$;
* seed identities $b_0=-1,b_1=n,b_2=n+2-n^2$.

A further finite alignment value would not establish either outstanding infinite lemma. I therefore do not substitute another numerical sample for the missing propagation or resonance proof.

---

# Conclusion

The first new result is an exact cross-index interface for the original fixed-seed alignment problem:


$$
\boxed{
\mathscr A(t)=\frac{e^{w(t)}}{\sqrt{1+2t-t^2}},
\qquad
w=t\left(1-w+\frac{w^2}{2}\right),
}
$$


together with a third-order diagonal moment recurrence and an explicit nine-coordinate realization of $F_n,M_n/L_n$.

This gives a concrete recurrence on which a multiplicative-block propagation lemma can be formulated. It does not make the two evaluated observations primitive.

The second new result is a finite integral force interface with the genuine seed and upper source boundary:


$$
\boxed{
b_k=-h_k+\sum_{i=0}^{k-1}\mathsf G_{k,i}F_i,
\qquad
\mathsf G_{k,k-1}=1.
}
$$


It exposes and removes the seed-induced factorial-height term without deleting the logarithmic contribution.

The third result is the paid nonresonant excess bound:


$$
\boxed{
\prod_{\substack{p>N\\
v_p(M)+v_p(\mathcal E_j^\circ)\ne
v_p(F)+v_p(\gamma_j)}}
p^{(v_p(\Delta_j)-v_p(\mathcal E_j^\circ))_+}
\mid
\mathcal I_n\,\gcd(M,\gamma_j)_{>N}.
}
$$



The exact remaining bottlenecks are:

1. **evaluated backward propagation of the two alignment observations**, with subfactorial paid cost, along infinitely many original indices; and
2. **higher-depth cancellation on the resonant affine chart**, especially where $F,M,\gamma_j,\mathcal E_j^\circ$ are all units, with the nonzero $\kappa F$ term retained.

Even resolving those arithmetic bottlenecks would still leave the actual all-prime weighted gcd and the whole nonzero same-index error to be controlled.



$$
\boxed{\text{No unconditional proof or disproof of the irrationality of }e+\pi
\text{ has been obtained.}}
$$


