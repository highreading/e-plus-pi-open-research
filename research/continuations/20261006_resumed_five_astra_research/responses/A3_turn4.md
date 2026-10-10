> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3, Turn 4 — The actual moment–force connection, fixed-seed force congruences, and selected-prime endpoint denominator laws

## Executive conclusion

The irrationality or rationality of $e+\pi$ remains unresolved.

The actual exponential-force recurrence does yield new arithmetic information. The main advance here is not a determinant-only saturation assertion. It is a collection of **fixed-seed, primewise identities for the actual endpoint triples and denominators**.

Write


$$
a_k(n)=k!\,[z^k]e^zq(z)^n,\qquad
u_k(n)=k!\,[z^k]\Omega_n(z),
\qquad
q(z)=1-z+\frac{z^2}{2},
$$


where


$$
\Omega_n(z)=q(z)^n
\frac{d^n}{dz^n}\left(\frac{e^z}{1-z}\right).
$$



The new force congruences are


$$
\boxed{
n'\equiv n\pmod{p^s}
\ \Longrightarrow\
u_k(n')\equiv u_k(n)\pmod{p^s}
}
\tag{E1}
$$


for every prime $p$, and


$$
\boxed{
k'\equiv k\pmod{p^s}
\ \Longrightarrow\
u_{k'}(n)\equiv u_k(n)\pmod{p^s}
}
\tag{E2}
$$


for odd $p$. These are statements about the **actual factorial seed**, not arbitrary solutions of the force recurrence.

They lead to the following endpoint result. Let $p$ be one of $3,5,7$ and suppose $p\mid n$. Put


$$
s=v_p(n),\qquad t=v_p(n!).
$$


Then, for the original endpoint normalization,


$$
\boxed{
v_p(\gamma_3)=v_p(d_3)=2t,
}
\tag{E3}
$$


whereas


$$
\boxed{
v_p(\gamma_0)\le 2t-s,
\qquad
v_p(d_0)\le 2t-s.
}
\tag{E4}
$$


Consequently,


$$
\boxed{
v_p(d_3)-v_p(d_0)\ge v_p(n).
}
\tag{E5}
$$



Thus, on both original families,


$$
\boxed{n\mid |AB|,}
\tag{E6}
$$


where, as before,


$$
v_p(|AB|)=|v_p(d_0)-v_p(d_3)|.
$$


This is an unconditional selected-prime imbalance statement within the original, nondegenerate endpoint construction. It is only a polynomial lower bound in $n$, not the much stronger denominator/error comparison needed for irrationality.

There is a different, explicit law for the selected prime $7$ on $n=15^r$. At every such original index,


$$
\boxed{
v_7(\gamma_0)=v_7(\gamma_3)=2v_7(n!),
\qquad
v_7(d_3)=2v_7(n!),
}
\tag{E7}
$$


and


$$
\boxed{
v_7(d_0)=2v_7(n!)+\eta_7(n),\qquad \eta_7(n)\ge1,
}
\tag{E8}
$$


where $\eta_7(n)$ is an explicitly specified reference-projection valuation below. Here the denominator imbalance has the **opposite orientation** from that at primes dividing $n$.

The correct coefficient-level augmented connection is also derived. Because the moment and force transfers differ, the natural closed mixed quadratic state has dimension $15$, not the conditional nine-state same-transfer system from Turn 3. A rational relative gauge identifies the original force seed exactly. Neither result, by itself, excludes the large-prime terminal lines jointly with $X_j$.

No producer has been executed here. The accepted $n=225$ calculations are not requested again. The scheduled $n=17$ validation and single $n=3375$ producer remain the coordinator’s existing work.

---

## 1. Scope and source assessment

The index domain remains


$$
n=15^r,\quad r\ge2,
\qquad\text{or}\qquad
n=105^r,\quad r\ge2.
$$



The following objects are unchanged:

- the $3\times3$ contact matrix;
- both corrected reconstructed columns, each with coordinates $0,1,2,3$;
- complete forcing through exactly $2n+2$;
- the complete logarithmic-force vector;
- the original terminal return;
- the exterior $+1$;
- the least clearer over all eight reconstruction entries;
- the actual row contents and primitive triples;
- every prime in the final gcd;
- the same-index whole error.

I retain Turn 3’s moment congruences and exact moment-content conclusions at their proved scope. The common-defect law remains subject to the announced independent review. The new force congruences and selected-prime denominator arguments below do not require an unproved extension of that common-defect law to endpoint triples.

Turn 2’s two-kernel comparison remains valid only with its stated normalization-unit hypotheses, in particular at $p>n+2$. Nothing below extends that comparison to small primes merely by changing its cutoff.

The separate binary results in A4 Turn 4 remain precision-scoped finite results. They are not used as endpoint-family theorems here. Likewise, the primary-literature gate supplies background methods, not a ready-made arithmetic estimate for this fixed finite target.

---

## 2. The actual force recurrence and its relative gauge

### 2.1 The generating function and fixed seed

To avoid confusion with the displacement scalar also denoted $\omega_n$ in earlier reports, use the capital letter


$$
\Omega_n(z)=q(z)^n A_n(z),
\qquad
A_n(z)=\frac{d^n}{dz^n}\left(\frac{e^z}{1-z}\right).
$$



Let


$$
E_m=A_m(0).
$$


Then


$$
E_0=1,\qquad E_m=mE_{m-1}+1,
$$


and


$$
E_m=\sum_{r=0}^m(m)_r.
\tag{2.1}
$$



The identity


$$
(1-z)A_n'-(n+1)A_n=e^z
$$


gives


$$
(1-z)q\,\Omega_n'
-\bigl((n+1)q+n(1-z)q'\bigr)\Omega_n
=q\,e^zq^n.
\tag{2.2}
$$



Set


$$
C_k=2^k a_k(n),\qquad W_k=2^k u_k(n).
$$


Coefficient comparison in (2.2) yields precisely


$$
\begin{aligned}
W_{k+1}={}&2(2k+1)W_k
+2k(2n+1-3k)W_{k-1}\\
&+4k(k-1)(k-n-1)W_{k-2}\\
&+2C_k-4kC_{k-1}+4k(k-1)C_{k-2}.
\end{aligned}
\tag{2.3}
$$



The initial force values are


$$
\boxed{
W_0=E_n,\qquad
W_1=2(E_n+1),\qquad
W_2=4\bigl((n+2)E_n+3-n\bigr).
}
\tag{2.4}
$$



Thus the coordinator’s recurrence and seed are algebraically consistent with the stated complete OGF. This derivation does not replace the scheduled direct finite-force validation.

### 2.2 An exact rational relative gauge

Leibniz’s rule gives


$$
A_n(z)=e^z R_n(z),
$$


where


$$
\boxed{
R_n(z)=
\sum_{r=0}^n\frac{(n)_r}{(1-z)^{r+1}}
=
\frac{n!}{(1-z)^{n+1}}
\sum_{j=0}^n\frac{(1-z)^j}{j!}.
}
\tag{2.5}
$$


Hence


$$
\boxed{\Omega_n(z)=R_n(z)e^zq(z)^n.}
\tag{2.6}
$$



The relative differential equation is


$$
\boxed{
(1-z)R_n'-(n+z)R_n=1,
\qquad R_n(0)=E_n.
}
\tag{2.7}
$$



This is a target-specific gauge identity, not a homogeneous approximation. In particular, the general solution of the force equation differs from the original one by


$$
c\,\frac{q(z)^n}{(1-z)^{n+1}}.
\tag{2.8}
$$


The original seed forces $c=0$.

Equation (2.6) is useful arithmetically, but it is not a three-state coefficientwise conjugacy: multiplication by $R_n(z)$ is a coefficient convolution. Treating it as a fixed $3\times3$ gauge would be incorrect.

---

## 3. The correct augmented moment–force–exterior connection

For $k\ge2$, put


$$
M_k=(C_k,C_{k-1},C_{k-2})^T,\qquad
F_k=(W_k,W_{k-1},W_{k-2})^T.
$$


Then


$$
M_{k+1}=P_kM_k,\qquad
F_{k+1}=Q_kF_k+B_kM_k,
\tag{3.1}
$$


with


$$
P_k=
\begin{pmatrix}
2(k+1-n)&2k(2n-k-1)&4k(k-1)\\
1&0&0\\
0&1&0
\end{pmatrix},
\tag{3.2}
$$




$$
Q_k=
\begin{pmatrix}
2(2k+1)&2k(2n+1-3k)&4k(k-1)(k-n-1)\\
1&0&0\\
0&1&0
\end{pmatrix},
\tag{3.3}
$$


and


$$
B_k=
\begin{pmatrix}
2&-4k&4k(k-1)\\
0&0&0\\
0&0&0
\end{pmatrix}.
\tag{3.4}
$$



In particular,


$$
\det P_k=4k(k-1),\qquad
\det Q_k=4k(k-1)(k-n-1).
\tag{3.5}
$$



The force transfer is singular at $k=n+1$ over characteristic zero. This is not a removable detail in a determinant-propagation argument.

### 3.1 What happens to the wedge

Let


$$
Z_k=M_k\wedge F_k.
$$


The exact identity is


$$
\boxed{
Z_{k+1}
=(\wedge^2P_k)Z_k
+(P_kM_k)\wedge\bigl((Q_k-P_k)F_k+B_kM_k\bigr).
}
\tag{3.6}
$$



The last term contains both:

- a mixed moment–force term;
- a quadratic moment source.

Thus Turn 3’s nine-state same-transfer formula cannot be applied silently.

### 3.2 A closed fifteen-state system

Define the nine mixed coordinates


$$
H_k=M_kF_k^T
$$


and the six ordinary quadratic monomials in $M_k$, equivalently the symmetric matrix


$$
S_k=M_kM_k^T.
$$


Then


$$
\boxed{
H_{k+1}=P_kH_kQ_k^T+P_kS_kB_k^T,
\qquad
S_{k+1}=P_kS_kP_k^T.
}
\tag{3.7}
$$


These equations give an integral linear system on $9+6=15$ coordinates. No division by $2$ is needed.

The determinant of this block transfer is


$$
\boxed{
(\det P_k)^7(\det Q_k)^3.
}
\tag{3.8}
$$


Indeed, the mixed block has determinant


$$
(\det P_k)^3(\det Q_k)^3,
$$


and the symmetric-square block has determinant $(\det P_k)^4$.

This is the correct low-dimensional mixed connection for the actual recurrences.

### 3.3 What the connection does not establish

Neither (3.7) nor the fixed gauge (2.6) supplies an invariant whose terminal value excludes the two endpoint lines jointly with $X_j$. The existing terminal-line obstruction therefore survives.

This is a statement about the present proof, not a claim that no stronger invariant can exist. A useful stronger invariant would have to evaluate on the actual seed and yield a Bézout relation involving the selected terminal projections—not merely the complete mixed state.

The next sections extract arithmetic from the seed directly, rather than from a transfer determinant.

---

## 4. Fixed-seed congruences for the actual force

### 4.1 Factorial-seed periodicity

For every prime $p$, $s\ge1$, and nonnegative integers $m,m'$,


$$
m'\equiv m\pmod{p^s}
\quad\Longrightarrow\quad
E_{m'}\equiv E_m\pmod{p^s}.
\tag{4.1}
$$



**Proof.** For $r\ge p^s$, the falling factorial $(m)_r$ is divisible by $p^s$, because it is an integer multiple of $r!$. Thus


$$
E_m\equiv
\sum_{r=0}^{p^s-1}(m)_r\pmod{p^s}.
$$


The right side is an integer polynomial in $m$. ∎

In particular,


$$
p^s\mid m\quad\Longrightarrow\quad E_m\equiv1\pmod{p^s}.
\tag{4.2}
$$



### 4.2 Congruence in the exponent $n$

Write


$$
b_r^{q}(n)=r!\,[z^r]q(z)^n.
$$


Turn 3’s integral exponential-coefficient argument proves


$$
b_r^{q}(n)\in\mathbb Z[n].
$$


Leibniz’s rule now gives the exact finite expression


$$
\boxed{
u_k(n)=
\sum_{r=0}^k
\binom{k}{r}b_r^{q}(n)E_{n+k-r}.
}
\tag{4.3}
$$


Terms with $r>2n$ vanish.

Combining polynomial congruence with (4.1) proves


$$
\boxed{
n'\equiv n\pmod{p^s}
\quad\Longrightarrow\quad
u_k(n')\equiv u_k(n)\pmod{p^s}.
}
\tag{4.4}
$$



A particularly useful specialization is


$$
\boxed{
p^s\mid n
\quad\Longrightarrow\quad
u_k(n)\equiv E_k\pmod{p^s}.
}
\tag{4.5}
$$



### 4.3 Odd-prime index periodicity

For fixed $n$, write $q(z)^n=\sum q_rz^r$, with $q_r\in\mathbb Z[1/2]$. Then


$$
u_k(n)=\sum_{r=0}^{2n}q_r(k)_r E_{n+k-r},
\tag{4.6}
$$


where terms with $r>k$ are zero.

Modulo $p^s$, with $p$ odd, replace $E_m$ by the polynomial in the proof of (4.1). This also defines the expression when the argument $m$ is negative; those artificially extended terms are multiplied by $(k)_r=0$ in the original nonnegative-index evaluation.

The resulting expression is a polynomial in $k$ over $\mathbb Z_p$. Therefore


$$
\boxed{
u_{k+p^s}(n)\equiv u_k(n)\pmod{p^s},
\qquad p\text{ odd}.
}
\tag{4.7}
$$



These congruences cross the singular transfer positions without inverting any transfer coefficient.

### 4.4 Terminal specialization at $p^s\mid n$

Combining (4.5), (4.7), and Turn 3’s moment congruences gives


$$
\boxed{
(a_n,a_{n+1},a_{n+2})\equiv(1,1,1)\pmod{p^s},
}
\tag{4.8}
$$




$$
\boxed{
(u_n,u_{n+1},u_{n+2})\equiv(1,2,5)\pmod{p^s},
\qquad p\text{ odd}.
}
\tag{4.9}
$$



The difference $(0,1,4)$ in these factorial-normalized coordinates is exactly where the exterior subtraction enters the small-prime calculation.

---

## 5. An exact all-prime endpoint-triple formula

This section keeps the actual primitive row and the actual exterior-corrected exponential coordinate.

Let $r_j\in\mathbb Z^3$ be a primitive integral row proportional to


$$
R_j=\ell_j\operatorname{adj}(T).
$$


Its sign is irrelevant for the valuations below.

Set


$$
N=n+2,
$$




$$
v'=(2N,N,n+1)^T,\qquad
w'=(0,N,2n+3)^T,
\tag{5.1}
$$


so that


$$
v=\frac{v'}{2N},\qquad w=\frac{w'}{2N}.
$$



Define the **complete exterior-corrected force vector**


$$
\boxed{
\mathcal U=
\begin{pmatrix}
(n+1)(n+2)(u_n-a_n)\\
(n+2)(u_{n+1}-a_{n+1})\\
u_{n+2}-a_{n+2}
\end{pmatrix}.
}
\tag{5.2}
$$


Since the actual exponential contact force has entries


$$
(\Omega_{n,n},\Omega_{n,n+1},\Omega_{n,n+2}),
$$


this is exactly


$$
\mathcal U=(n+2)!\,(\widehat w^{\exp}-T_0).
\tag{5.3}
$$



In particular,


$$
s^{\exp}
=\frac{\widehat w^{\exp}-T_0}{n!}
=\frac{\mathcal U}{n!(n+2)!}.
\tag{5.4}
$$


The subtraction of $T_0$ is retained. At endpoint $0$, it is what produces the exterior $+\Delta$, hence the original exterior $+1$.

Put


$$
K_n=\frac{n!(n+1)!}{2},
\qquad
G_j=\gcd(r_jv',r_jw').
\tag{5.5}
$$


The integer $K_n$ is well-defined for all retained indices.

A common integral representative of the actual endpoint triple is


$$
\boxed{
\bigl(K_n\,r_jv',\ K_n\,r_jw',\ r_j\mathcal U\bigr).
}
\tag{5.6}
$$


Consequently,


$$
\boxed{
\gamma_j=
\frac{K_nG_j}
{\gcd(K_nG_j,r_j\mathcal U)}.
}
\tag{5.7}
$$



This yields the exact all-prime valuation law


$$
\boxed{
v_p(\gamma_j)=
\max\!\left\{
0,\,
v_p(K_n)+
\min\{v_p(r_jv'),v_p(r_jw')\}
-v_p(r_j\mathcal U)
\right\}.
}
\tag{5.8}
$$



The primitive pair is, up to simultaneous sign,


$$
\boxed{
(\mathfrak a_j,\mathfrak b_j)
=\left(\frac{r_jv'}{G_j},\frac{r_jw'}{G_j}\right).
}
\tag{5.9}
$$



This formula includes:

- the actual reference-plane clearer;
- factorial force normalization;
- actual row content, through the primitive $r_j$;
- the complete exponential coordinate;
- exterior restoration.

It does not identify a normalized moment gcd with an endpoint-triple gcd.

---

## 6. Reference arithmetic and the actual small-prime dual content

For clarity, the original reference normalization can be characterized by


$$
\tau_0=\tau_1=1,\qquad \rho_0=0,\quad \rho_1=1,
$$


and the common recurrence


$$
(m+1)y_{m+1}=(2m+1)y_m+my_{m-1}.
\tag{6.1}
$$


The retained complete logarithmic-force vector is


$$
4n!\,(\rho_nv+\rho_{n+1}w).
$$



The original integral reference coordinates are


$$
t_0=L\tau_n,\qquad t_1=L\tau_{n+1},
$$




$$
r_0^{\rm ref}=4L\rho_n,\qquad
r_1^{\rm ref}=4L\rho_{n+1}.
\tag{6.2}
$$


No particular numerical value of $L$ is substituted below.

Define


$$
\xi_j=\mathfrak a_j\tau_n+\mathfrak b_j\tau_{n+1},
\qquad
\eta_j=4(\mathfrak a_j\rho_n+\mathfrak b_j\rho_{n+1}),
\tag{6.3}
$$


and


$$
\zeta_j=\gamma_j\eta_j+\mathsf E_j.
\tag{6.4}
$$


Then, exactly,


$$
X_j=L\xi_j,\qquad V_j=L\zeta_j.
\tag{6.5}
$$



Therefore the actual denominator satisfies the all-prime identity


$$
\boxed{
v_p(d_j)=
\max\{0,\,
v_p(\gamma_j)+v_p(\xi_j)-v_p(\zeta_j)\}.
}
\tag{6.6}
$$


This is merely the original all-prime gcd formula expressed before the common factor $L$; no prime has been discarded.

### 6.1 A denominator bound for the reference companion

Multiplying (6.1) by $m!$ shows that


$$
m!\tau_m,\qquad m!\rho_m
$$


are integers. Hence


$$
\boxed{
v_p(\eta_j)\ge-v_p((n+1)!).
}
\tag{6.7}
$$



This bound is sufficient below. It does not require guessing that $L$ is a least denominator.

### 6.2 Exact dual-content bookkeeping at small primes

Write


$$
G_t=\gcd(t_0,t_1).
$$


With the original dual remainders written as


$$
\mathcal R_j^{(i)}
=t_iV_j-r_i^{\rm ref}\gamma_jX_j,
\qquad i=0,1,
\tag{6.8}
$$


one has the exact integer ideal equality


$$
(X_j,\mathcal R_j^{(0)},\mathcal R_j^{(1)})
=(X_j,t_0V_j,t_1V_j).
$$


Thus


$$
\boxed{
\mathcal C_j^\sharp=\gcd(|X_j|,G_t|V_j|),
}
\tag{6.9}
$$


and


$$
\boxed{
v_p(\mathcal C_j^\sharp)
=\min\{v_p(X_j),v_p(V_j)+v_p(G_t)\}.
}
\tag{6.10}
$$



At the large primes where $G_t$ is a unit, this reduces to the accepted large-prime formula. At small primes the extra $G_t$-depth must be retained.

In particular, $\mathcal C_j^\sharp$ is not automatically the actual cancellation


$$
\gcd(\gamma_jX_j,V_j)
$$


at small primes.

### 6.3 Why the selected reference values are units

The reference sequence has the constant-term representation


$$
\boxed{
\tau_m=\operatorname{CT}_x
\left(1+x+\frac1{2x}\right)^m
=
\sum_{h\ge0}
\binom m{2h}\binom{2h}{h}2^{-h}.
}
\tag{6.11}
$$


It follows either from the diagonal coefficient


$$
[z^m]\frac{q(z)^m}{(1-z)^{m+1}}
$$


by the substitution $z=u/(1+u)$, or directly from its generating function.

For odd $p$, if $m=a+pb$, $0\le a<p$, Frobenius and constant-term extraction give


$$
\boxed{\tau_{a+pb}\equiv\tau_a\tau_b\pmod p.}
\tag{6.12}
$$


Indeed, the Laurent exponents in the low-digit factor lie strictly between $-p$ and $p$, so only exponent $0$ can match an exponent divisible by $p$.

The complete one-digit tables are


$$
\begin{array}{c|l}
p&(\tau_0,\ldots,\tau_{p-1})\pmod p\\ \hline
3&(1,1,2)\\
5&(1,1,2,4,1)\\
7&(1,1,2,4,5,1,6).
\end{array}
\tag{6.13}
$$


No entry is zero. Thus


$$
\boxed{p\nmid\tau_m\quad\text{for }p=3,5,7,\ m\ge0.}
\tag{6.14}
$$



If $p\mid n$, the last base-$p$ digit is $0$, and


$$
\boxed{\tau_{n+1}\equiv\tau_n\pmod p.}
\tag{6.15}
$$



The small tables are finite exact arithmetic; the all-index conclusion follows from the proved digit identity, not from extrapolating the tables.

---

## 7. New theorem at odd primes dividing $n$

Let $p$ be an odd prime dividing $n$, and set


$$
s=v_p(n),\qquad t=v_p(n!).
$$



### 7.1 Primitive-row residues

The locally integral matrix $n!T$ is


$$
n!T=
\begin{pmatrix}
a_n&na_{n-1}&n(n-1)a_{n-2}\\
a_{n+1}/(n+1)&a_n&na_{n-1}\\
a_{n+2}/((n+1)(n+2))&a_{n+1}/(n+1)&a_n
\end{pmatrix}.
$$


Using the moment congruence modulo $p^s$,


$$
n!T\equiv
\begin{pmatrix}
1&0&0\\
1&1&0\\
1/2&1&1
\end{pmatrix}\pmod{p^s}.
\tag{7.1}
$$


Its determinant is a unit. Therefore the actual primitive endpoint rows are, up to local unit multiples,


$$
\boxed{
r_0\equiv(-1,0,0),\qquad
r_3\equiv(1/2,-1,1)
\pmod{p^s}.
}
\tag{7.2}
$$



The reference clearers satisfy


$$
v'\equiv(4,2,1),\qquad w'\equiv(0,2,3)\pmod{p^s}.
$$


Consequently,


$$
\boxed{v_p(G_0)=v_p(G_3)=0.}
\tag{7.3}
$$



### 7.2 The actual exterior coordinate

Equations (4.8)–(4.9) give


$$
\boxed{\mathcal U\equiv(0,2,4)^T\pmod{p^s}.}
\tag{7.4}
$$


Hence


$$
v_p(r_0\mathcal U)\ge s,\qquad
v_p(r_3\mathcal U)=0.
\tag{7.5}
$$



Since $v_p(K_n)=2t$, formula (5.8) proves


$$
\boxed{
v_p(\gamma_3)=2t,
}
\tag{7.6}
$$


and, writing $e_0=v_p(r_0\mathcal U)$,


$$
\boxed{
v_p(\gamma_0)=\max(0,2t-e_0),
\qquad e_0\ge s.
}
\tag{7.7}
$$



These are actual endpoint-triple statements.

### 7.3 Denominator consequences at $p=3,5,7$

Now assume $p\in\{3,5,7\}$. By (7.2), (5.9), and (6.15),


$$
v_p(\xi_0)=v_p(\xi_3)=0.
\tag{7.8}
$$



For endpoint $3$, the primitive triple has $v_p(\gamma_3)=2t>0$, so $\mathsf E_3$ is a unit. Also


$$
v_p(\gamma_3\eta_3)\ge2t-t=t>0.
$$


Thus


$$
v_p(\zeta_3)=0.
$$


Equation (6.6) gives


$$
\boxed{v_p(d_3)=2t.}
\tag{7.9}
$$



For endpoint $0$, let $g_0=v_p(\gamma_0)$. Since


$$
v_p(\eta_0)\ge-t,\qquad \mathsf E_0\in\mathbb Z,
$$


one has


$$
v_p(\zeta_0)\ge\min(g_0-t,0).
$$


Therefore


$$
v_p(d_0)\le\max(g_0,t).
\tag{7.10}
$$


Because $e_0\ge s$, $g_0\le2t-s$, and $t\ge s$,


$$
\boxed{v_p(d_0)\le2t-s.}
\tag{7.11}
$$



This proves (E3)–(E5).

More precisely, if $e_0<t$, then $g_0>t$, so no cancellation with the unit $\mathsf E_0$ is possible:


$$
\boxed{
v_p(d_0)=2t-e_0\qquad(e_0<t).
}
\tag{7.12}
$$


If $e_0\ge t$, the exact remaining endpoint-$0$ cancellation is the explicitly evaluated $\zeta_0$ in (6.4), and


$$
v_p(d_0)\le t.
\tag{7.13}
$$



### 7.4 Dual content at these primes

Let $\ell=v_p(L)$. The selected-prime reference units imply


$$
v_p(G_t)=\ell,\qquad v_p(X_0)=v_p(X_3)=\ell.
$$


At endpoint $3$,


$$
v_p(V_3)=\ell,
$$


so


$$
\boxed{v_p(\mathcal C_3^\sharp)=\ell.}
\tag{7.14}
$$



At endpoint $0$, the exact law is


$$
\boxed{
v_p(\mathcal C_0^\sharp)
=\min\{\ell,\,2\ell+v_p(\zeta_0)\}.
}
\tag{7.15}
$$


This retains the actual reference clearer and the whole exponential coordinate.

---

## 8. The selected prime $7$ on $n=15^r$

Here


$$
n\equiv1\pmod7.
$$


This prime does not divide $n$, so the preceding theorem does not apply to it.

Using exponent and index congruence, reduce to $n=1$. The relevant factorial moment residues are


$$
(a_{n-2},a_{n-1},a_n,a_{n+1},a_{n+2})
\equiv(3,1,0,0,1)\pmod7.
\tag{8.1}
$$


The actual force residues are


$$
(u_n,u_{n+1},u_{n+2})
\equiv(3,1,4)\pmod7.
\tag{8.2}
$$


For example, at $n=1$,


$$
u_1=3,\qquad u_2=8,\qquad u_3=32.
$$



Thus


$$
n!T\equiv
\begin{pmatrix}
0&1&0\\
0&0&1\\
6&0&0
\end{pmatrix}\pmod7,
$$


and the primitive rows are, up to unit multiples,


$$
\boxed{
r_0\equiv(6,2,6),\qquad r_3\equiv(0,6,0).
}
\tag{8.3}
$$



The reference and force vectors reduce to


$$
v'\equiv(6,3,2),\qquad
w'\equiv(0,3,5),\qquad
\mathcal U\equiv(4,3,3).
$$


Therefore


$$
(r_0v',r_0w')\equiv(5,1),\qquad
(r_3v',r_3w')\equiv(4,4),
\tag{8.4}
$$


and


$$
r_0\mathcal U\equiv6,\qquad
r_3\mathcal U\equiv4\pmod7.
\tag{8.5}
$$



Put $t=v_7(n!)$. Formula (5.8) gives


$$
\boxed{v_7(\gamma_0)=v_7(\gamma_3)=2t.}
\tag{8.6}
$$


The reference companion bound again makes $\zeta_0,\zeta_3$ units.

Since $n\equiv1\pmod7$, the digit identity gives


$$
\tau_{n+1}\equiv2\tau_n\pmod7.
$$


Thus (8.4) implies


$$
\xi_0\equiv0\pmod7,\qquad \xi_3\not\equiv0\pmod7.
$$


Define the actual projection depth


$$
\boxed{
\eta_7(n)=
v_7\!\left(
\mathfrak a_0\tau_n+\mathfrak b_0\tau_{n+1}
\right).
}
\tag{8.7}
$$


Then $\eta_7(n)\ge1$, and the exact denominator laws are


$$
\boxed{
v_7(d_0)=2t+\eta_7(n),\qquad
v_7(d_3)=2t.
}
\tag{8.8}
$$



This is a supported divisor law with an explicit outstanding scalar valuation, not a determinant-only conclusion.

For $\ell=v_7(L)$, the corresponding dual contents are


$$
\boxed{
v_7(\mathcal C_3^\sharp)=\ell,\qquad
v_7(\mathcal C_0^\sharp)
=\min\{\ell+\eta_7(n),2\ell\}.
}
\tag{8.9}
$$


The actual cancellation in the endpoint denominator has valuation $\ell$. Thus (8.9) also exhibits concretely why small-prime dual content cannot be substituted for actual denominator cancellation.

---

## 9. Other small-prime regimes, including $p\mid n+1$ and $2$

The preceding selected-prime results do not solve every prime $p\le n+2$. The remaining regimes can nevertheless be stated precisely.

### 9.1 Odd primes dividing $n+1$

Let $p$ be odd,


$$
s=v_p(n+1),\qquad t=v_p(n!).
$$


Use the integral matrix


$$
J=(n+2)!T.
$$


Odd-prime index periodicity gives


$$
a_{n+1}\equiv1,\qquad a_{n+2}\equiv2\pmod{p^s}.
$$


Hence


$$
J\equiv
\begin{pmatrix}
0&0&0\\
1&0&0\\
2&1&0
\end{pmatrix}\pmod{p^s}.
\tag{9.1}
$$


Its endpoint-$3$ adjugate row is primitive and satisfies


$$
r_3\equiv(1,0,0)\pmod{p^s}
$$


up to a unit.

It follows that


$$
v_p(G_3)=0,\qquad v_p(r_3\mathcal U)\ge s.
$$


Therefore


$$
\boxed{
v_p(\gamma_3)
=
\max\{0,\,2t+s-v_p(r_3\mathcal U)\}
\le2t.
}
\tag{9.2}
$$



The endpoint-$0$ raw row is divisible by $p^s$; its primitive reduction must actually be performed. Moment-state primitivity does not determine that reduction.

For these primes, equations (5.8), (6.6), and (6.10) are the exact all-prime specification. A stronger uniform endpoint-$0$ saturation estimate is not proved here.

### 9.2 The reference-plane lattice at primes dividing $n+2$

One has


$$
v'\times w'=(n+2)\,q_\partial.
\tag{9.3}
$$


For odd $n$, $q_\partial$ is primitive. The two-column integral reference lattice therefore has saturation index $n+2$.

This identifies a genuine reference-plane cost at every prime dividing $n+2$, not just at a prime equal to $n+2$. Formula (5.8) includes it through $G_j$; no large-prime normal-line argument is applied there.

### 9.3 Explicit $2$-adic seed parity

For odd $n$, the exponent congruence reduces $u_k(n)$ modulo $2$ to $u_k(1)$. From


$$
u_k(1)=E_{k+1}-kE_k+\binom{k}{2}E_{k-1}
$$


and $E_m\equiv1,0$ for even, odd $m$, respectively,


$$
\boxed{
u_k(n)\pmod2:\quad 0,1,0,0
}
\tag{9.4}
$$


with period four.

Together with the moment pattern $1,0,0,1$, this yields


$$
\boxed{
\mathcal U\equiv
\begin{cases}
(0,0,1)^T,&n\equiv1\pmod4,\\
(0,1,1)^T,&n\equiv3\pmod4.
\end{cases}
}
\tag{9.5}
$$



Also,


$$
v'\equiv(0,1,0),\qquad w'\equiv(0,1,1)\pmod2.
$$


Writing $r_j=(r_{j,0},r_{j,1},r_{j,2})$, one obtains:

- $G_j$ is odd exactly when $r_{j,1}$ or $r_{j,2}$ is odd;
- if $n\equiv1\pmod4$, then $r_j\mathcal U$ is odd exactly when $r_{j,2}$ is odd;
- if $n\equiv3\pmod4$, then $r_j\mathcal U$ is odd exactly when $r_{j,1}+r_{j,2}$ is odd.

The exact valuation formula is


$$
\boxed{
v_2(\gamma_j)=
\max\!\left\{
0,\,
2v_2(n!)+v_2(n+1)-1
+v_2(G_j)-v_2(r_j\mathcal U)
\right\}.
}
\tag{9.6}
$$



This explicitly incorporates the $2$-adic factorial cost, reference pair, and exterior coordinate. It is not yet a bounded uniform saturation theorem at $2$.

---

## 10. What has advanced, and the exact remaining bottleneck

### 10.1 A genuine infinite-family denominator statement

For $n=15^r$, apply §7 at $p=3,5$. For $n=105^r$, apply it at $p=3,5,7$. This proves


$$
n\mid |AB|.
$$


On $15^r$, §8 supplies the additional, oppositely oriented $7$-adic imbalance.

These statements are not finite extrapolations. They follow from:

1. the exact force OGF and seed;
2. prime-power congruences;
3. actual primitive-row reductions;
4. the complete exterior coordinate;
5. reference denominator control;
6. the actual endpoint denominator gcd.

They are nevertheless far too weak, by themselves, for the irrationality objective.

### 10.2 The large-prime terminal-line bottleneck remains

The fixed-seed gauge and fifteen-state connection do not presently prove a bound for


$$
\gcd(X_j^\circ,\mathcal F,\mathcal F_j^{\rm alt})_{>n+2}.
$$


The two selected determinants can still vanish on the endpoint lines described in Turn 3 while an unselected mixed coordinate is a unit.

The concrete follow-on target is therefore:

> **Fixed-seed projected-content lemma.**  
> Bound, on infinitely many original indices, the total prime-power depth of the actual terminal-line intersections jointly with $X_j^\circ$, using the actual seed $E_n$, or prove an equivalent lower bound for the actual all-prime denominator imbalance.

The new congruences close part of the small-prime problem. They do not close the large-prime projected-content estimate or the remaining small-prime regimes.

### 10.3 A more focused small-prime follow-on lemma

The all-prime formula (5.8) reduces the remaining local issue to evaluated scalars:


$$
G_j=\gcd(r_jv',r_jw'),
\qquad
r_j\mathcal U,
\qquad
\zeta_j=\gamma_j\eta_j+\mathsf E_j.
$$



A useful next lemma would bound the combined excess


$$
v_p(r_j\mathcal U)-v_p(G_j)
$$


and the cancellation depth in $\zeta_j$, uniformly over the unhandled primes $p\le n+2$, with the actual primitive rows retained.

A real saddle estimate for the force or reference values does not bound these rational-height quantities.

---

## 11. Actual primitive denominator and same-index whole error

The new local formulas do not replace any reconstruction row or primitive pair.

The endpoint denominator is still


$$
\boxed{
d_j=\frac{|\gamma_jX_j|}
{\gcd(|\gamma_jX_j|,|V_j|)}.
}
\tag{11.1}
$$



For a reduced weight $\lambda=a/k$, retain


$$
J_{\rm wt}=B\widetilde v_0-A\widetilde v_3,
\qquad
T_{\rm wt}=aJ_{\rm wt}+kA\widetilde v_3,
$$




$$
F_{\rm gcd}
=\gcd(|A|,|a|)\gcd(|B|,|a-k|),
$$




$$
G=\gcd(k,|J_{\rm wt}|),
\qquad
H_{\rm gcd}
=
\gcd\!\left(h,\frac{|T_{\rm wt}|}{F_{\rm gcd}G}\right).
$$


The actual primitive pair remains


$$
\boxed{
q_\lambda=
\frac{kh|AB|}{F_{\rm gcd}GH_{\rm gcd}},
\qquad
p_\lambda=
\operatorname{sgn}(AB)
\frac{T_{\rm wt}}{F_{\rm gcd}GH_{\rm gcd}}.
}
\tag{11.2}
$$


Every prime remains in the final gcd.

The same-index whole error remains


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda e_3\alpha_{n,2}
(\lambda-\Lambda_{n,2}).
}
\tag{11.3}
$$


An irrationality proof still requires an infinite sequence satisfying


$$
\boxed{
0<
q_\lambda|e_3\alpha_{n,2}|
\,|\lambda-\Lambda_{n,2}|
\longrightarrow0.
}
\tag{11.4}
$$



The accepted $n=225$ row contents remain


$$
(508500,\ 28350,\ 15525,\ 772).
$$


Its five accepted whole-form evaluations remain nonzero and greater than $1$ in absolute value. No result here changes those finite evaluations.

---

## 12. Proof status and bounded exact arithmetic

### 12.1 Status ledger

| Statement | Status |
|---|---|
| Actual force recurrence and initial three-state seed | Proved from the OGF |
| Rational relative gauge identifying the original seed | Proved |
| Fifteen-state mixed quadratic connection | Proved |
| Nine-state same-transfer system for this actual force | Not applicable without further transformation |
| Force congruence in $n$ at every prime power | Proved |
| Odd-prime-power force index periodicity | Proved |
| Exact all-prime endpoint-triple formula (5.8) | Proved |
| Exact small-prime dual-content bookkeeping | Proved with the original dual remainders |
| Selected-prime $\gamma_3$ and $d_3$ laws at $p\mid n$ | Proved |
| Selected-prime denominator imbalance at least $v_p(n)$ | Proved |
| Oppositely oriented $7$-adic law on $15^r$ | Proved |
| Uniform all-small-prime saturation cost | Open |
| Fixed-seed large-prime terminal-line avoidance/content bound | Open |
| Actual primitive whole-error sequence tending to zero | Open |
| Irrationality or rationality of $e+\pi$ | Unresolved |

### 12.2 No repeated producer work

No accepted $n=225$ computation should be rerun.

The coordinator’s scheduled $n=17$ direct validation already addresses the new producer recurrence and complete logarithmic identity. No second validation is requested here.

The scheduled $n=3375$ producer remains a single original computation with all eight entries. No outcome for it is assumed.

### 12.3 New expected checks on the eventual $n=3375$ artifact

The new theorems give precise post-processing checks, requiring no regeneration of its force.

For $n=3375=15^3$,


$$
v_3(n!)=1684,\qquad
v_5(n!)=843,\qquad
v_7(n!)=560.
$$


Therefore the expected verifiable outputs are


$$
\boxed{
v_3(\gamma_3)=v_3(d_3)=3368,
\qquad
v_5(\gamma_3)=v_5(d_3)=1686,
}
\tag{12.1}
$$


and


$$
\boxed{
v_3(d_0)\le3365,\qquad
v_5(d_0)\le1683.
}
\tag{12.2}
$$



At $7$,


$$
\boxed{
v_7(\gamma_0)=v_7(\gamma_3)=1120,
\qquad
v_7(d_3)=1120,
}
\tag{12.3}
$$




$$
\boxed{
v_7(d_0)=1120+\eta_7(3375),\qquad
\eta_7(3375)\ge1.
}
\tag{12.4}
$$



The post-processing inputs are:

- the archived actual primitive endpoint triples;
- the actual endpoint denominators;
- the actual primitive rows;
- the already produced moment and force coefficients;
- the actual $L,t_i,r_i^{\rm ref}$.

The additional scalar outputs should be


$$
v_p(r_0\mathcal U),\quad p=3,5,
\qquad
\eta_7(3375),
$$


together with zero residuals for (5.6)–(5.9) and the original dual identities.

These are theorem-driven checks on a new artifact, not predictions that its large-prime contents are $1$, and not a proposal to rerun any accepted bounded computation.

---

## Conclusion

The actual force transfer differs materially from the moment transfer. Its correct mixed connection contains both a bilinear correction and a quadratic source, and its force block is singular at $k=n+1$. The fixed seed is nevertheless accessible through an exact rational relative gauge and prime-power congruences.

That seed information yields new endpoint arithmetic:



$$
\boxed{
v_p(\gamma_3)=v_p(d_3)=2v_p(n!)
\quad
\text{for }p\in\{3,5,7\},\ p\mid n,
}
$$


while


$$
\boxed{
v_p(d_0)\le2v_p(n!)-v_p(n).
}
$$


Hence


$$
\boxed{n\mid |AB|}
$$


on both original families. At $7$ on $15^r$, a separate fixed-seed calculation gives the opposite endpoint orientation and the exact supported law (8.8).

The remaining mathematical bottleneck is not full-state primitivity. It is control of the actual projected endpoint arithmetic—large-prime terminal-line intersections jointly with $X_j$, and the still-unhandled small-prime saturation and cancellation depths—followed by the actual all-prime primitive denominator versus the same-index whole error.



$$
\boxed{\text{No unconditional proof or disproof of the irrationality of }e+\pi\text{ has been obtained.}}
$$


