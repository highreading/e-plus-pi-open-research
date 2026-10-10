> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3, Turn 1 — Specialized Bézout identities and a one-moment bound for the structural content

## Executive conclusion

The irrationality or rationality of


$$
S=e+\pi
$$


remains unresolved.

This report advances the arithmetic of the **actual specialized triples**


$$
\left(\alpha_j,\beta_j,\frac{N_j^{\exp}}{n!}\right),
\qquad j=0,3.
$$


It does not replace their exponential component by a freely chosen value.

The new results are:

1. **An exact Bézout elimination for the evaluated cancellation integer.**  
   The complete exponential-force recurrence eliminates its homogeneous diagonal component from
   

$$
\gcd(X_j,\mathcal R_j).
$$


   The remaining expression contains only the actual forced displacement, the terminal exponential coefficient, and the endpoint term—including the exterior $+1$. The denominator cost of this elimination is stated exactly.

2. **A specialized large-prime restriction on $\gamma_0,\gamma_3$.**  
   For every prime $p>n+2$, divisibility of either structural content forces the three actual exponential moments into one of two explicit projective residue classes. These classes coincide only at primes dividing
   

$$
P_n=n^2+5n+3.
$$



3. **Removal of one genuine moment factor from the structural-content bound.**  
   If
   

$$
H_n^{\mathrm{lin}}
   =b+(n-3)c-2(n-1)d,
$$


   then
   

$$
\boxed{
   (\gamma_0\gamma_3)_{>n+2}
   \mid
   \bigl(P_n\,|\operatorname{num}(H_n^{\mathrm{lin}})|\bigr)_{>n+2}.
   }
$$


   Thus the product of the two structural contents is controlled, at these primes, by **one linear moment numerator**, not its square and not a product of two quadratic cofactor expressions.

4. **A complete-force resultant bound for $\mathcal C_j$.**  
   Two explicitly evaluated terminal determinants bound each $(\mathcal C_j)_{>n+2}$, up to the already exponential factor $t_0$. Their formulas eliminate the homogeneous exponential component and retain the full terminal return and exterior correction.

These are rigorous identities and divisibility theorems. They do **not** prove an exponential bound for the primitive moment-pair heights, the missing $R_\gamma/R_{\mathcal C}$ bound, or superexponential growth of the actual complete-row factor.

No computation was executed. The coordinator’s existing $n=225$ implementation assignment is not requested again.

---

## 1. Scope and retained normalization

The original families remain


$$
n=15^r,\qquad r\ge2,\qquad \mathcal P=\{3,5\},
$$


and


$$
n=105^r,\qquad r\ge2,\qquad \mathcal P=\{3,5,7\}.
$$



The contact matrix is still $3\times3$, with indices $0,1,2$. Reconstruction still has coordinates $0,1,2,3$. The complete force for the producer at $n$ ends at exactly $2n+2$.

Write


$$
c_k=[z^k](e^zQ(z)^n),\qquad Q(z)=1-z+\frac{z^2}{2},
$$


and


$$
a=c_{n-2},\quad b=c_{n-1},\quad c=c_n,\quad
d=c_{n+1},\quad e_*=c_{n+2}.
$$


Thus


$$
T=
\begin{pmatrix}
c&b&a\\
d&c&b\\
e_*&d&c
\end{pmatrix},
\qquad \Delta=\det T.
$$



The accepted endpoint rows are


$$
R_j=\ell_j^T\operatorname{adj}(T),
$$


where


$$
\ell_0=(-1,n,-n(n+1)),\qquad \ell_3=(0,0,1).
$$



Retain


$$
v=
\begin{pmatrix}
1\\[1mm]1/2\\[1mm](n+1)/(2(n+2))
\end{pmatrix},
\qquad
w=
\begin{pmatrix}
0\\[1mm]1/2\\[1mm](2n+3)/(2(n+2))
\end{pmatrix}.
$$


Then


$$
\alpha_j=R_jv,\qquad \beta_j=R_jw,\qquad
\xi_j=\alpha_j\tau_n+\beta_j\tau_{n+1}.
$$



The complete endpoint numerators remain


$$
N_0^{\exp}=\Delta+R_0\widehat w^{\exp},
\qquad
N_3^{\exp}=R_3\widehat w^{\exp},
$$


and


$$
N_j=N_j^{\exp}
+4n!(\alpha_j\rho_n+\beta_j\rho_{n+1}).
$$



I reuse the preceding report’s primitive triples


$$
(\mathsf A_j,\mathsf B_j,\mathsf E_j)
=
\sigma_j\left(\alpha_j,\beta_j,\frac{N_j^{\exp}}{n!}\right),
$$


their contents


$$
\gamma_j=\gcd(|\mathsf A_j|,|\mathsf B_j|),
$$


and primitive pairs


$$
(\mathfrak a_j,\mathfrak b_j)
=(\mathsf A_j,\mathsf B_j)/\gamma_j.
$$



In particular,


$$
X_j=\mathfrak a_jt_0+\mathfrak b_jt_1,
$$




$$
\mathcal R_j=t_0L\mathsf E_j+\Omega\gamma_j\mathfrak b_j,
\qquad
\mathcal C_j=\gcd(|X_j|,|\mathcal R_j|).
$$



No new auxiliary normalization below replaces the least clearer of the original eight reconstructed entries or either actual endpoint-row content.

---

# 2. Complete exponential contiguity at the retained terminal boundary

The source’s forced recurrence is useful here, but its complete forcing must be retained. I give the derivation needed for the present application.

## 2.1 The terminal coefficient

Set


$$
F_n=d-c+\frac b2.
$$


Multiplication by $Q$ gives the exact identity


$$
\boxed{
E_n:=\mathcal B_{n+1}^{[n+1]}=(n+1)!F_n.
}
\tag{2.1}
$$



Let


$$
D_m=w_0^{\exp}(m),\qquad
B_m=\frac{D_m}{(m!)^2}.
$$


Here $B_m$ is a normalized diagonal exponential force, not an endpoint denominator.

For


$$
A_m^{\exp}(z)
=Q(z)^m\left(\frac{e^z}{1-z}\right)^{(m)},
$$


the differential equation gives, with $A_{m,N}=N![z^N]A_m^{\exp}$,


$$
\begin{aligned}
A_{m,N+1}
={}&(2N+1)A_{m,N}
+\frac{N(2m+1-3N)}2A_{m,N-1}\\
&+\frac{N(N-1)(N-m-1)}2A_{m,N-2}
+\mathcal B_N^{[m+1]}.
\end{aligned}
\tag{2.2}
$$



At $N=m+1$, this is exactly


$$
\boxed{
w_2^{\exp}-(2m+3)w_1^{\exp}
+\frac{(m+1)(m+2)}2w_0^{\exp}=E_m.
}
\tag{2.3}
$$


This is the retained terminal return; its right side is not discarded.

The contiguity identity


$$
A_{m+1}^{\exp}=Q(A_m^{\exp})'-mQ'A_m^{\exp}
$$


then gives


$$
\boxed{
D_{m+1}
=2(m+1)w_1^{\exp}(m)-(m+1)^2D_m+E_m.
}
\tag{2.4}
$$



Using (2.2) once more in the coefficient extraction for the next producer yields


$$
\begin{aligned}
w_1^{\exp}(m+1)
={}&(m+1)(3m+5)w_1^{\exp}(m)\\
&-(m+1)^2(m+2)D_m+(2m+3)E_m+G_m,
\end{aligned}
\tag{2.5}
$$


where


$$
G_m=\mathcal B_{m+2}^{[m+1]}.
$$



Consequently,


$$
\boxed{
(m+2)B_{m+2}
=(2m+3)B_{m+1}+(m+1)B_m+\psi_m,
}
\tag{2.6}
$$


with the **complete** forcing


$$
\boxed{
\psi_m=
\frac{(m+1)(m+2)E_m+2(m+2)G_m+E_{m+1}}
{(m+2)((m+1)!)^2}.
}
\tag{2.7}
$$



All three terms in (2.7) are necessary.

## 2.2 The actual forced displacement

Define


$$
\omega_m=(-1)^m(m+1)
\bigl(\tau_mB_{m+1}-\tau_{m+1}B_m\bigr).
$$


The recurrence gives


$$
\boxed{
\omega_{m+1}
=\omega_m+(-1)^{m+1}\tau_{m+1}\psi_m,
\qquad \omega_0=2.
}
\tag{2.8}
$$



For the complete force it is convenient to retain


$$
\boxed{\mathscr S_m=\omega_m+4.}
\tag{2.9}
$$


The $4$ is the entire logarithmic Wronskian contribution in the accepted normalization. It is not a replacement for the logarithmic force.

Thus


$$
\mathscr S_0=6,\qquad
\mathscr S_{m+1}
=\mathscr S_m+(-1)^{m+1}\tau_{m+1}\psi_m.
\tag{2.10}
$$



For the producer at $n$, only $B_n,B_{n+1}$, or equivalently (2.8) through $m=n-1$, are needed. The diagonal $B_{n+1}$ uses exponential-force coefficients through $2n+2$. No force through $2n+4$, and no enlarged finite inverse, is required.

---

# 3. An exact Bézout elimination for $\mathcal R_j$ and $X_j$

## 3.1 Specialized endpoint remainder

Put


$$
a_\partial=
\begin{pmatrix}
0\\1\\1/(n+2)
\end{pmatrix},
\qquad
\varepsilon_0=1,\quad \varepsilon_3=0.
$$



Equations (2.3)–(2.4), after the original row-factorial normalization, give


$$
\boxed{
\frac{\widehat w^{\exp}}{n!}
=
B_nv+B_{n+1}w
-\frac{F_n}{2(n+1)n!}\,a_\partial.
}
\tag{3.1}
$$



Define the actual terminal endpoint remainder


$$
\boxed{
\zeta_j
=
\varepsilon_j\Delta
-\frac{F_n}{2(n+1)}R_ja_\partial.
}
\tag{3.2}
$$


Then


$$
\boxed{
\frac{N_j^{\exp}}{n!}
=
\alpha_jB_n+\beta_jB_{n+1}+\frac{\zeta_j}{n!}.
}
\tag{3.3}
$$



In particular, $\zeta_0$ contains $+\Delta$. This is the original exterior $+1$, not an optional correction.

## 3.2 The cancellation identity

Using


$$
t_0=L\tau_n,\qquad
\Omega=\frac{4(-1)^nL^2}{n+1},
$$


and


$$
\tau_nB_{n+1}-\tau_{n+1}B_n
=\frac{(-1)^n\omega_n}{n+1},
$$


equation (3.3) gives


$$
\boxed{
\mathcal R_j-L\gamma_jB_nX_j
=
\mathscr T_j,
}
\tag{3.4}
$$


where


$$
\boxed{
\mathscr T_j
=
L^2\left[
\frac{(-1)^n\gamma_j\mathfrak b_j\mathscr S_n}{n+1}
+\frac{\sigma_j\tau_n\zeta_j}{n!}
\right].
}
\tag{3.5}
$$



This is an identity for the **evaluated specialized values**. Its right side contains:

- the complete forced displacement $\mathscr S_n=\omega_n+4$;
- the terminal exponential coefficient $F_n$;
- the actual endpoint cofactor action;
- $+\Delta$ at endpoint $0$.

It does not contain the homogeneous diagonal $B_n$.

### Exact integer form and denominator cost

Write the actual reduced diagonal value as


$$
B_n=\frac{u_n^{B}}{v_n^{B}},
\qquad
v_n^{B}>0,\qquad
\gcd(|u_n^{B}|,v_n^{B})=1.
$$


Define


$$
\boxed{
\mathscr T_j^{\mathrm{int}}
=
v_n^{B}\mathcal R_j
-L\gamma_ju_n^{B}X_j
=
v_n^{B}\mathscr T_j\in\mathbb Z.
}
\tag{3.6}
$$


Then, exactly,


$$
\gcd(|X_j|,|\mathscr T_j^{\mathrm{int}}|)
=
\gcd(|X_j|,|v_n^{B}\mathcal R_j|).
$$


Hence


$$
\boxed{
\mathcal C_j
\mid
\gcd(|X_j|,|\mathscr T_j^{\mathrm{int}}|)
\mid
v_n^{B}\mathcal C_j.
}
\tag{3.7}
$$



The complete finite exponential sum implies


$$
\boxed{
v_n^{B}\mid 2^n(n!)^2.
}
\tag{3.8}
$$


Indeed, $2^nw_0^{\exp}$ is integral, and $B_n=w_0^{\exp}/(n!)^2$.

Therefore, at every prime $p\nmid v_n^{B}$,


$$
\boxed{
v_p(\mathcal C_j)
=
\min\{v_p(X_j),v_p(\mathscr T_j)\}.
}
\tag{3.9}
$$


In particular, (3.9) holds for every $p>n+2$.

**What this removes.** The homogeneous exponential scalar has been removed from the cancellation problem by a genuine Bézout identity.

**What it does not remove.** At primes dividing $v_n^{B}$, the denominator cost in (3.7) is real and may be factorial-scale. Moreover, the actual displacement and terminal remainder in (3.5) still require arithmetic control.

---

# 4. A primitive-row content identity

The following elementary identity is used only as a tool for the specialized application.

Let $r\in\mathbb Z_p^3$ be primitive, and suppose $rk=0$. For arbitrary integral columns $x,y,k$,


$$
\boxed{
r_i\det(x,y,k)
=
(rx)(y\times k)_i-(ry)(x\times k)_i.
}
\tag{4.1}
$$


Since some $r_i$ is a unit,


$$
\boxed{
\min\{v_p(rx),v_p(ry)\}
\le v_p\det(x,y,k).
}
\tag{4.2}
$$



This is a Bézout/Smith-content statement: a content in two outputs is bounded by an evaluated determinant involving an exact kernel column.

The advancement below is not the abstract identity. It is the evaluation of its kernel columns and determinants for the original moment recurrence and complete force.

## 4.1 Application to the actual primitive triple

Choose a primitive integer row $r_j$ and a nonzero rational $\chi_j$ such that


$$
R_j=\chi_jr_j.
$$



Let $T_0,T_1,T_2$ denote the columns of $T$, and put


$$
s_j^{\exp}
=
\frac{\widehat w^{\exp}-\varepsilon_jT_0}{n!}.
\tag{4.3}
$$


Because


$$
R_0T_0=-\Delta,
$$


we have exactly


$$
\left(\alpha_j,\beta_j,\frac{N_j^{\exp}}{n!}\right)
=
\chi_j(r_jv,r_jw,r_js_j^{\exp}).
\tag{4.4}
$$



Thus the exterior correction is retained inside the actual third coordinate.

For $p>n+2$, all entries of $v,w,s_j^{\exp}$ are $p$-integral. Set


$$
m_j=\min\{v_p(r_jv),v_p(r_jw)\},
$$




$$
\delta_j=
\min\{v_p(r_jv),v_p(r_jw),v_p(r_js_j^{\exp})\}.
$$


Primitivizing the actual triple gives


$$
\boxed{
v_p(\gamma_j)=m_j-\delta_j\le m_j,
\qquad p>n+2.
}
\tag{4.5}
$$


The inequality uses $\delta_j\ge0$; no freely chosen exponential coordinate is involved.

---

# 5. Specialized linear-moment restrictions for $\gamma_0,\gamma_3$

## 5.1 The five moments reduce to three

The coefficient recurrence


$$
(k+1)c_{k+1}
=(k+1-n)c_k+
\left(n-\frac{k+1}{2}\right)c_{k-1}
+\frac12c_{k-2}
$$


gives


$$
\boxed{
a=2(n+1)d-2c-(n-1)b,
}
\tag{5.1}
$$




$$
\boxed{
e_*=\frac{4d+(n-2)c+b}{2(n+2)}.
}
\tag{5.2}
$$



Define


$$
q_\partial=
\begin{pmatrix}
n+2\\-2(2n+3)\\2(n+2)
\end{pmatrix}.
$$


Then


$$
v\times w=\frac{q_\partial}{4(n+2)}.
\tag{5.3}
$$



The exact kernel columns are


$$
\begin{array}{c|cc}
j&k_{j,1}&k_{j,2}\\ \hline
3&T_0&T_1\\
0&T_1+nT_0&T_2-n(n+1)T_0.
\end{array}
\tag{5.4}
$$


They satisfy $r_jk_{j,\ell}=0$, because $R_jT=\Delta\ell_j$.

## 5.2 Explicit evaluation of the kernel defects

Put


$$
\boxed{
H=b+(n-3)c-2(n-1)d,
}
\tag{5.5}
$$




$$
\boxed{
B_0^\partial=6d-(n+6)c,
\qquad
B_3^\partial=2(n+2)d-(n+3)c.
}
\tag{5.6}
$$



Using (5.1)–(5.2), direct calculation gives


$$
q_\partial^Tk_{0,1}=2(n+1)H,
$$




$$
q_\partial^Tk_{0,2}=2(n+1)J,
$$


where


$$
J=-(n+2)b-n^2c+2(n^2+n+1)d
$$


and


$$
\boxed{J+(n+2)H=B_0^\partial.}
\tag{5.7}
$$



For endpoint $3$,


$$
q_\partial^TT_0=H-B_3^\partial,
$$




$$
q_\partial^TT_1=(n+2)H+nB_3^\partial.
\tag{5.8}
$$


The determinant of the two coefficients of $(H,B_3^\partial)$ in (5.8) is $2(n+1)$.

Combining (4.2), (4.5), and these evaluations proves:

### Theorem 5.1 — Specialized structural-content restriction

For every prime $p>n+2$,


$$
\boxed{
v_p(\gamma_0)
\le
\min\{v_p(H),v_p(B_0^\partial)\},
}
\tag{5.9}
$$




$$
\boxed{
v_p(\gamma_3)
\le
\min\{v_p(H),v_p(B_3^\partial)\}.
}
\tag{5.10}
$$



These are bounds for the contents of the actual coefficient triples, not for arbitrary free triples.

---

## 5.3 The original moment state is primitive at these primes

For $p>n+2$, every $c_k$, $0\le k\le n+2$, is $p$-integral.

Suppose $p\mid b,c,d$. The recurrence, solved backward using its coefficient $1/2$, then forces successively


$$
p\mid c_{n-2},c_{n-3},\ldots,c_0.
$$


But $c_0=1$. Therefore


$$
\boxed{
\min\{v_p(b),v_p(c),v_p(d)\}=0,
\qquad p>n+2.
}
\tag{5.11}
$$



Consequently, if either pair of defects in (5.9)–(5.10) is divisible by $p$, then $c$ is a $p$-adic unit.

The congruences are particularly explicit. If $p^a\mid\gamma_0$, then


$$
\boxed{
\frac dc\equiv\frac{n+6}{6},
\qquad
\frac bc\equiv\frac{n^2+2n+3}{3}
\pmod{p^a}.
}
\tag{5.12}
$$


If $p^a\mid\gamma_3$, then


$$
\boxed{
\frac dc\equiv\frac{n+3}{2(n+2)},
\qquad
\frac bc\equiv\frac{3(n+1)}{n+2}
\pmod{p^a}.
}
\tag{5.13}
$$



Thus large-prime structural content requires the actual exponential moment state to hit one of two specific recurrence-determined directions.

---

# 6. Removing one complete moment factor from the $R_\gamma$ bound

The two directions above are not independent arbitrary obstructions.

Set


$$
\boxed{P_n=n^2+5n+3.}
\tag{6.1}
$$


Then


$$
\boxed{
(n+2)B_0^\partial-3B_3^\partial=-P_nc.
}
\tag{6.2}
$$



At any $p>n+2$ dividing both defect gcds, $c$ is a unit by (5.11). Hence their common depth is at most $v_p(P_n)$.

To formulate the integer divisibility without suppressing denominators, let


$$
D_{\mathrm{mom}}=2^n(n+2)!,
$$


which clears all five moments, and define


$$
U_0=
\gcd\bigl(|D_{\mathrm{mom}}H|,
          |D_{\mathrm{mom}}B_0^\partial|\bigr)_{>n+2},
$$




$$
U_3=
\gcd\bigl(|D_{\mathrm{mom}}H|,
          |D_{\mathrm{mom}}B_3^\partial|\bigr)_{>n+2}.
\tag{6.3}
$$


The notation $(\,\cdot\,)_{>n+2}$ means the integer factor supported on primes $>n+2$.

Since $D_{\mathrm{mom}}$ is a unit at those primes, Theorem 5.1 and (6.2) give


$$
\boxed{
(\gamma_j)_{>n+2}\mid U_j,
}
\tag{6.4}
$$




$$
\boxed{
\gcd(U_0,U_3)\mid(P_n)_{>n+2}.
}
\tag{6.5}
$$



Both $U_j$ divide $|D_{\mathrm{mom}}H|_{>n+2}$. Therefore


$$
U_0U_3
=\operatorname{lcm}(U_0,U_3)\gcd(U_0,U_3)
\mid
|D_{\mathrm{mom}}H|_{>n+2}(P_n)_{>n+2}.
$$



### Theorem 6.1 — One-linear-moment structural-content bound



$$
\boxed{
(\gamma_0\gamma_3)_{>n+2}
\mid
\bigl(P_n\,|\operatorname{num}(H)|\bigr)_{>n+2}.
}
\tag{6.6}
$$


In particular,


$$
\boxed{
(R_\gamma)_{>n+2}
\mid
\bigl(P_n\,|\operatorname{num}(H)|\bigr)_{>n+2}.
}
\tag{6.7}
$$



Also,


$$
\boxed{
\gcd(\gamma_0,\gamma_3)_{>n+2}\mid(P_n)_{>n+2}.
}
\tag{6.8}
$$



### Meaning and limitation

This removes a genuine factor: bounding the two endpoint defects separately would allow two copies of the linear moment numerator $H$. Their product needs only one copy, with the additional polynomial factor $P_n$.

The elementary coefficient bound gives


$$
\log|\operatorname{num}(H)|
\le n\log n+O(n).
$$


Thus


$$
\boxed{
\log(R_\gamma)_{>n+2}\le n\log n+O(n).
}
\tag{6.9}
$$



This is a rigorous factorial-scale upper bound, not an exponential one. It does not establish the desired $O(n)$ logarithmic bound.

The primes $p\le n+2$ outside $\mathcal P$ have not disappeared. Their contribution to $R_\gamma$ remains part of the unresolved all-prime problem.

---

# 7. Complete-force terminal resultants controlling $\mathcal C_j$

The preceding structural-content calculation used the actual third coefficient to justify primitivization, but did not yet use its full evaluated force to bound $\mathcal C_j$. That next step is also explicit.

## 7.1 The complete two-column output

Put


$$
t=\tau_nv+\tau_{n+1}w,
$$


and


$$
\boxed{
s_j
=
\frac{\widehat w-\varepsilon_jT_0}{n!}.
}
\tag{7.1}
$$


Then


$$
r_jt,\qquad r_js_j
$$


are, up to the same nonzero rational scalar, the two complete endpoint-row entries.

Using (3.1) and the accepted logarithmic normalization,


$$
\begin{aligned}
s_j={}&
(B_n+4\rho_n)v+(B_{n+1}+4\rho_{n+1})w\\
&-\frac{F_n}{2(n+1)n!}a_\partial
-\frac{\varepsilon_j}{n!}T_0.
\end{aligned}
\tag{7.2}
$$



Therefore


$$
\boxed{
t\times s_j
=
\frac{(-1)^n\mathscr S_n}{n+1}(v\times w)
-\frac{F_n}{2(n+1)n!}(t\times a_\partial)
-\frac{\varepsilon_j}{n!}(t\times T_0).
}
\tag{7.3}
$$



Again the homogeneous scalar has canceled exactly.

## 7.2 Explicit evaluated remainder vector

Let


$$
a_\partial^{\mathrm{int}}=(0,n+2,1)^T.
$$


Define


$$
\boxed{
Z_j^\partial
=
(-1)^nn!\mathscr S_nq_\partial
-2F_n(t\times a_\partial^{\mathrm{int}})
-4(n+1)(n+2)\varepsilon_j(t\times T_0).
}
\tag{7.4}
$$


Then


$$
\boxed{
Z_j^\partial
=
4(n+1)(n+2)n!\,(t\times s_j).
}
\tag{7.5}
$$



For the exact kernel columns (5.4), set


$$
\boxed{
\mathscr E_{j,\ell}
=
(Z_j^\partial)^Tk_{j,\ell},
\qquad \ell=1,2.
}
\tag{7.6}
$$



These are the **specialized complete terminal-resultant remainders**.

Their formula retains:

- the complete exponential recurrence through $\mathscr S_n$;
- the full logarithmic Wronskian contribution $4$;
- the terminal return $F_n$;
- the exterior contribution at $j=0$;
- the original endpoint kernel columns.

They contain no homogeneous diagonal $B_n$, and no quadratic endpoint row $R_j$.

All denominators in (7.4)–(7.6) are supported on primes at most $n+2$.

## 7.3 The content bound

For $p>n+2$, $L$ is a unit. With the primitive-row notation of Section 4, the actual integer complete-row content satisfies


$$
v_p(g_j^*)
=
\min\{v_p(r_jt),v_p(r_js_j)\}-\delta_j,
$$


where $\delta_j\ge0$. Thus


$$
v_p(g_j^*)
\le
\min\{v_p(r_jt),v_p(r_js_j)\}.
$$



Applying (4.2) to each actual kernel column and then using (7.5) gives


$$
\boxed{
v_p(g_j^*)
\le
\min_{\ell=1,2}v_p(\mathscr E_{j,\ell}),
\qquad p>n+2.
}
\tag{7.7}
$$



The preceding complete-row theorem gives


$$
\mathcal C_j\mid t_0g_j^*.
$$


Consequently:

### Theorem 7.1 — Complete-force resultant restriction

For every prime $p>n+2$,


$$
\boxed{
v_p(\mathcal C_j)
\le
v_p(t_0)
+\min_{\ell=1,2}v_p(\mathscr E_{j,\ell}).
}
\tag{7.8}
$$



Define the exact integer


$$
\boxed{
\mathfrak F_j
=
\gcd\bigl(
|\operatorname{num}(\mathscr E_{j,1})|,
|\operatorname{num}(\mathscr E_{j,2})|
\bigr)_{>n+2}.
}
\tag{7.9}
$$


Then


$$
\boxed{
(\mathcal C_j)_{>n+2}
\mid
(t_0)_{>n+2}\mathfrak F_j.
}
\tag{7.10}
$$



In particular,


$$
\boxed{
(R_{\mathcal C})_{>n+2}
\mid
(t_0)^2_{>n+2}\mathfrak F_0\mathfrak F_3.
}
\tag{7.11}
$$



This is a bound by explicit recurrence/end defects, not a claim that those evaluated gcds are small.

### Nonvacuity on the eventual original-family range

The accepted fixed-shift asymptotic gives


$$
F_n\ne0,\qquad 2d-c\ne0
$$


eventually. Moreover,


$$
(v\times w)^Ts_3=\frac{F_n}{2(n+2)n!},
$$




$$
(v\times w)^Ts_0
=\frac{(n+1)(2d-c)}{2(n+2)n!}.
$$


Thus $t\times s_j\ne0$ eventually.

If both determinants in (7.6) vanished while $t\times s_j\ne0$, their normal would be proportional to $R_j$, forcing $R_jt=0$, contrary to the accepted nonvanishing of $\xi_j$. Hence the two entries defining $\mathfrak F_j$ are not simultaneously zero on that eventual range.

This nonvacuity is not a bound on their gcd.

---

# 8. What has now been removed from the missing content problem

Combining the new results,


$$
\boxed{
(R_\gamma R_{\mathcal C})_{>n+2}
\mid
U_0U_3\,(t_0)^2_{>n+2}\mathfrak F_0\mathfrak F_3,
}
\tag{8.1}
$$


and


$$
\boxed{
U_0U_3
\mid
\bigl(P_n|\operatorname{num}(H)|\bigr)_{>n+2}.
}
\tag{8.2}
$$



Three genuine pieces have been removed:

1. **The homogeneous exponential diagonal** from the evaluated cancellation ideal, by (3.4)–(3.9).

2. **The quadratic adjugate-row content** from the large-prime bounds, by primitive-row Bézout identities.

3. **One copy of the shared linear moment numerator $H$** from the product of the two structural-content bounds, by (6.2).

What remains is still substantial.

Define the exact small-unselected-prime factor


$$
\mathscr B_n
=
(R_\gamma R_{\mathcal C})_{\{p\le n+2:\ p\notin\mathcal P\}}.
$$


Then the new bound is


$$
\boxed{
\log(R_\gamma R_{\mathcal C})_{\mathcal P^c}
\le
\log\mathscr B_n
+\log(U_0U_3\mathfrak F_0\mathfrak F_3)
+2\log t_0.
}
\tag{8.3}
$$


Here $\log t_0=O(n)$, but neither of the first two terms has been proved $O(n)$.

A concrete sufficient follow-on lemma is therefore:

> **Specialized terminal-resultant content lemma.**  
> On one specified original smooth family, prove
> 

$$
> \log\mathscr B_n+
> \log(U_0U_3\mathfrak F_0\mathfrak F_3)=O(n),
>
$$


> or obtain a suitably sharper bound for the actual endpoint imbalance directly.

This target is more specialized than a theorem about free coefficient triples:

- $U_0,U_3$ are gcds of explicitly listed **linear expressions in the actual three-moment state**;
- $\mathfrak F_0,\mathfrak F_3$ are gcds of the **evaluated complete terminal resultants** (7.4)–(7.6);
- $\mathscr B_n$ explicitly retains the omitted small unselected primes.

The theorem has not been proved here.

---

# 9. Why an exponential primitive moment-pair bound is still unsupported

The preceding report proved


$$
\log H(\kappa_j)
=
\log\max(|\mathfrak a_j|,|\mathfrak b_j|)+O(n).
$$


Nothing in the present argument changes that equivalence.

The new congruences show a precise original-family obstruction to obtaining a height bound solely from transformation noncollapse:

- large prime factors of $\gamma_0$ require the actual moment ratios to satisfy (5.12);
- large prime factors of $\gamma_3$ require (5.13);
- the two conditions have only the polynomial overlap $P_n$;
- nevertheless, either individual condition can still hold at prime-power depth governed by the numerator of the actual linear moment $H$.

The recurrence proves that the moment state is primitive at these primes, but it does not prove that its distance from either special direction has exponentially bounded arithmetic content.

Likewise, the complete-force recurrence removes $B_n$ from the cancellation, but leaves the evaluated remainders $\mathscr T_j$ and $\mathscr E_{j,\ell}$. Their real asymptotics do not bound their reduced numerator gcds.

Accordingly, I do not claim either that the exponential primitive moment-pair height bound is true or that it is false. The present result is a specialized divisor restriction with named remainders, not a resolution of that height problem.

---

# 10. Actual complete-row denominators and whole error remain unchanged

The original least clearer is still taken over **all eight entries** of the two reconstructed columns. All four row contents remain part of that normalization.

For the endpoint rows,


$$
M_j=\gamma_jX_j,\qquad
V_j=\gamma_jY_j+L\mathsf E_j,
$$


and the actual reduced denominator remains


$$
\boxed{
d_j=\frac{|M_j|}{\gcd(|M_j|,|V_j|)}.
}
\tag{10.1}
$$



The preceding complete-row comparison remains


$$
K_j=\frac{\gamma_j|X_j|}{\mathcal C_j},
\qquad
Z_K=\frac{K_0K_3}{\gcd(K_0,K_3)^2},
$$




$$
\boxed{
\left|v_p(|AB|)-v_p(Z_K)\right|
\le v_p(Lt_0)
}
\tag{10.2}
$$


at every prime.

The new bounds do not turn this exponential comparison into superexponential growth. They only restrict some of the possible content losses.

The selected-prime law remains


$$
\boxed{(|AB|)_{\mathcal P}=5n.}
\tag{10.3}
$$



For a reduced weight $\lambda=a/k$, retain


$$
J=B\widetilde v_0-A\widetilde v_3,\qquad
T=aJ+kA\widetilde v_3,
$$




$$
F_{\rm gcd}
=\gcd(|A|,|a|)\gcd(|B|,|a-k|),
$$




$$
G=\gcd(k,|J|),\qquad
H_{\rm gcd}
=\gcd\!\left(h,\frac{|T|}{F_{\rm gcd}G}\right).
$$


The actual primitive pair is still


$$
\boxed{
q_\lambda
=\frac{kh|AB|}{F_{\rm gcd}GH_{\rm gcd}},
\qquad
p_\lambda
=\operatorname{sgn}(AB)
\frac{T}{F_{\rm gcd}GH_{\rm gcd}}.
}
\tag{10.4}
$$



Every prime remains in the final gcd.

Finally, the same-index whole error is


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda e_3\alpha_{n,2}
(\lambda-\Lambda_{n,2}).
}
\tag{10.5}
$$


A successful irrationality construction still requires


$$
\boxed{
0<
q_\lambda|e_3\alpha_{n,2}|
\,|\lambda-\Lambda_{n,2}|
\longrightarrow0.
}
\tag{10.6}
$$



None of the new moment-direction restrictions or resultant nonvacuity statements proves the nonvanishing or decay in (10.6).

---

# 11. Proof status and bounded verification

## 11.1 Proof-status ledger

| Statement | Status |
|---|---|
| Original families, $3\times3$ contact matrix, four reconstructed rows | Retained unchanged |
| Complete force ending at $2n+2$ | Retained unchanged |
| Complete exponential diagonal recurrence and all three forcing terms | Derived above |
| Specialized endpoint remainder $\zeta_j$, including $+\Delta$ | Derived above |
| Integer Bézout elimination (3.6)–(3.7) | Proved |
| Exact cancellation identity outside $\operatorname{den}(B_n)$ | Proved |
| Large-prime primitive moment state | Proved from the coefficient recurrence |
| Explicit projective restrictions (5.12)–(5.13) | Proved |
| One-linear-moment bound for $(\gamma_0\gamma_3)_{>n+2}$ | Proved |
| Complete-force terminal-resultant bound for $(\mathcal C_j)_{>n+2}$ | Proved |
| Exponential bound for $U_0U_3$ or $\mathfrak F_0\mathfrak F_3$ | Open |
| Small-unselected-prime content bound | Open |
| Exponential primitive moment-pair height bound | Unsupported by the present results |
| Superexponential growth of actual $Z_K$ or $|AB|_{\mathcal P^c}$ | Open |
| Favorable actual primitive whole forms | Open |

## 11.2 No repeat of the $n=225$ request

The coordinator is already implementing the original $n=225$ audit. This report neither represents that producer as completed nor requests it again. It does not propose rerunning the accepted computations at $15,30,105,210$.

No bounded numerical computation is required for the proofs above.

An optional **new symbolic arithmetic check**, distinct from those producer computations, has the following finite specification:

- Work over
  

$$
\mathbb Q(n,b,c,d,\tau,\tau_1,B,B_1,\rho,\rho_1).
$$


- Substitute (5.1)–(5.2) for $a,e_*$.
- Form the stated $3\times3$ matrix, its two endpoint adjugate rows, and the four kernel columns (5.4).
- Verify the polynomial identities (5.7)–(5.8), (6.2), and the cross-product identity (7.5), using
  

$$
\tau B_1-\tau_1B=\frac{(-1)^n\omega}{n+1},
  \qquad
  \tau\rho_1-\tau_1\rho=\frac{(-1)^n}{n+1}.
$$



The expected verifiable output is an exact zero numerator for each residual after clearing the displayed denominators. This would check the finite symbolic algebra only; it would not estimate any evaluated gcd on the original families.

---

## Conclusion

The new specialized arithmetic step is twofold.

First, the evaluated cancellation admits an exact Bézout elimination:


$$
\boxed{
\mathcal R_j-L\gamma_jB_nX_j
=
L^2\left[
\frac{(-1)^n\gamma_j\mathfrak b_j(\omega_n+4)}{n+1}
+\frac{\sigma_j\tau_n\zeta_j}{n!}
\right],
}
$$


with the actual denominator of $B_n$, the full force, the terminal return, and the exterior $+1$ all retained.

Second, the moment recurrence imposes a genuine restriction on the structural contents:


$$
\boxed{
(\gamma_0\gamma_3)_{>n+2}
\mid
\left((n^2+5n+3)
\,|\operatorname{num}(b+(n-3)c-2(n-1)d)|\right)_{>n+2}.
}
$$


This removes one full moment factor from the two-endpoint structural-content bound.

The exact remaining bottleneck is arithmetic control of the explicit linear-moment gcds $U_0,U_3$, the complete terminal-resultant gcds $\mathfrak F_0,\mathfrak F_3$, and the small unselected-prime content. No exponential bound for their combined contribution has been established.

Even such a bound would still have to be combined with the actual all-prime primitive denominator and the same-index nonzero whole-error criterion.



$$
\boxed{\text{The irrationality or rationality of }e+\pi\text{ remains unresolved.}}
$$


