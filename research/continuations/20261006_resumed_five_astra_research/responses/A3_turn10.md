> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3, Turn 10 — A recurrence-level obstruction to factorial cancellation, and a reference-filtered product certificate

## Executive conclusions

The irrationality or rationality of $e+\pi$ remains unresolved.

This turn makes two advances toward the assigned arithmetic target.

### 1. The complete scalar has no factors $3,5,7$, at any original index

For the unchanged canonical integer


$$
\Theta_n
=
\frac{2^{(n+1)/2}}{n!}
\left[mZ(Qh-P\ell)-F\mathscr K_n\right],
$$


I prove


$$
\boxed{\gcd(\Theta_n,105)=1}
\tag{E1}
$$


throughout the original domain


$$
n=15^r\quad\text{or}\quad n=105^r,\qquad r\ge2.
$$



In particular,


$$
\boxed{\Theta_n\ne0\quad\text{at every original index}.}
\tag{E2}
$$


This improves Turn 9’s eventual real nonvanishing to all-original-index arithmetic nonvanishing. It says nothing by itself about nonvanishing of a primitive whole approximation form.

There is also an exact, independently derived scalar binary law:


$$
\boxed{
n=15^{2a+1},\ a\ge1
\quad\Longrightarrow\quad
v_2(\Theta_n)=s_2(n)+6,
}
\tag{E3}
$$


where $s_2(n)$ is the binary digit sum.

These results use the **actual moment and complete-force recurrence**. They do not depend on acceptance of the independently reviewed endpoint binary denominator theorem.

They give a precise obstruction to a proposed factorial cancellation: even one additional factor $n!$ cannot be divided out of $\Theta_n$ as an integer. On the odd-exponent $15$-family, its entire $2,3,5,7$-supported part is only


$$
2^{s_2(n)+6}.
$$


The factorial-sized real term is therefore not an integer factorial factor.

This does **not** disprove


$$
\log U_n\ge3\log(n!)-O(n).
$$


Omitting any fixed finite collection of primes costs only $O(n)$ in $\log(n!)$. The required all-small-prime lower bound remains unsupported.

### 2. A different product certificate excludes collision primes using the actual references

Turn 9’s exclusive-depth rigidity can be combined with the actual normalized reference projections before estimating heights.

Put


$$
\widehat R_j=\alpha_j\widehat h+\beta_j\widehat\ell
=\frac{2^{(n+1)/2+1}}{mn!}R_j\in\mathbb Z,
$$


and retain


$$
\mathcal B_n=\gcd(\ell,Z,Y-2X,\mathscr K_n)_{>N},
\qquad
\Sigma_n=(\sigma_n)_{>N},
\qquad N=n+2.
$$


Define the **reference collision ceiling**


$$
\boxed{
H_n^{\rm ref}
=
\gcd\!\left(
\Sigma_n,\frac{|\widehat R_0|}{\mathcal B_n},
             \frac{|\widehat R_3|}{\mathcal B_n}
\right).
}
\tag{E4}
$$



The divisions displayed here are exact. If


$$
\delta_j^{>}=g_nE_{j,n},
\qquad g_n=\mathcal B_n\Gamma_n,
$$


then


$$
\boxed{\Gamma_n\mid H_n^{\rm ref}}
\tag{E5}
$$


and, more importantly,


$$
\boxed{
\gcd\!\left(E_{0,n}E_{3,n},
\frac{\Sigma_n}{H_n^{\rm ref}}\right)=1.
}
\tag{E6}
$$



Thus an endpoint-exclusive prime lying on $\Sigma_n$ is impossible unless **both actual normalized references reach the full collision depth above the source content**. This restriction is evaluable without first knowing the complete endpoint gcds.

After an additional endpoint-specific reference filter, §8 constructs an explicit positive integer


$$
\boxed{\mathcal W_n^{\rm ref}\mid\mathcal W_n}
\tag{E7}
$$


such that


$$
\boxed{
\delta_0^{>}\delta_3^{>}\mid\mathcal W_n^{\rm ref}.
}
\tag{E8}
$$


It is another nonzero element of the localized **product** ideal, not merely of a common ideal.

No exponential-height bound for this new certificate is proved. Its advantage is that it discards specified factors of the canonical scalar that cannot support endpoint-exclusive cancellation.

### 3. A4’s sharper projection loss is retained

With A4’s


$$
B_j=\gcd(\Pi_j,|L_j|)_{>N},
$$


the improved conclusion is


$$
\boxed{
\mathfrak D_0\mathfrak D_3
\mid B_0B_3\,\mathcal W_n^{\rm ref}.
}
\tag{E9}
$$


The coprimality of $B_0,B_3$ concerns projection excesses only. It is not used to assert coprimality or smallness of the actual residual contents.

---

# I. Source assessment and unchanged scope

## 1. The completed joint receipt

I accept the new $3375$ receipt at its stated finite scope.

The supplied source forms the actual raw contact rows from the adjugate of the retained $J$, divides by their actual three-coordinate contents, and verifies


$$
\mathscr R_0\times\mathscr R_3=\det(J)(nJ_0+J_1)
$$


as an exact integer vector identity. It then verifies the corresponding integer content identity.

Its extraction of large parts removes every prime through $3377$, not a selected-prime sample. Its complete residual is reconstructed as


$$
\mathbf C=\mathbf U-E_n\mathbf H+\mathbf Q,
$$


with the complete logarithmic $\mathbf Q$.

The accepted finite results include:

| Field | Verified value |
|---|---:|
| Raw cross-product residual | Zero |
| Integer saturation identity | Exact |
| Large shared-column content | $1$ |
| $\Sigma_{3375}$ bit length | $116931$ |
| Actual joint large gcd | $1$ |
| Actual large boundary gcd | $1$ |
| Raw contact-row binary contents | $5,0$ |
| Primitive $\alpha_j,\beta_j$ depths | $1,4$ |
| Reference depths | $1691,1691$ |
| Complete exterior-exponential depths | $5,5$ |
| Seed-and-log-restored depths | $5,5$ |

The very large $\Sigma_{3375}$ does not represent observed cancellation: the actual joint large gcd is $1$.

Nothing in the source asserts an independent infinite-family proof, and I do not upgrade these finite checks to one. No producer, old denominator calculation, old endpoint gcd, or whole-error enclosure is requested again.

The coordinator’s new computation of $\Theta_{3375}$, its canonical small/large parts, its clipped collision gcd, and certificate sizes remains pending. No numerical result from that task is assumed below.

## 2. A4’s projection refinement

A4’s proof uses the exact local projected ideal at


$$
p>N,\qquad p\nmid G_j.
$$


Its reference-sensitive restriction follows by imposing the reference equation simultaneously with the two normal equations. This is a legitimate refinement of the projection excess, not a cancellation of a contact determinant.

I therefore retain


$$
\delta_j^{>}\mid\mathfrak D_j\mid B_j\delta_j^{>},
$$


where


$$
\begin{aligned}
\Pi_3&=n^2+4n+1,
&
L_3&=h-N\ell,\\
\Pi_0&=n^2+6n+4,
&
L_0&=(n+3)h-(n^2+5n+3)\ell.
\end{aligned}
$$


Also,


$$
\gcd(B_0,B_3)=1.
$$



The extension of the even-exponent binary denominator law to $105^{2a}$ is retained at A4’s proved scope. It is not needed for the scalar arguments below.

## 3. Construction boundaries

Throughout,


$$
n=15^r\quad\text{or}\quad n=105^r,\qquad r\ge2,
$$


and


$$
m=n+1,\qquad N=n+2.
$$



The following are unchanged:

- the finite $3\times3$ contact matrix;
- the force cutoff $2n+2$;
- both corrected reconstruction columns;
- the complete terminal return;
- the exterior $+1$;
- the least clearer over all eight entries;
- the actual reconstruction row contents;
- the all-prime final weighted gcd;
- the actual primitive denominator;
- the whole error at the same original index.

The generating-function calculations below evaluate the retained coefficients. They neither extend a matrix boundary nor add another terminal recurrence step.

---

# II. The actual recurrence and an exact canonical remainder

## 4. Recovering the inhomogeneous recurrence from the retained force

Write


$$
q(z)=1-z+\frac{z^2}{2},
\qquad
A_n(z)=e^zq(z)^n
=\sum_{k\ge0}a_k\frac{z^k}{k!}.
$$



The retained homogeneous and exponential-force series are


$$
H_n(z)=\frac{q(z)^n}{(1-z)^{n+1}}
=\sum_{k\ge0}h_k\frac{z^k}{k!},
$$


and


$$
\Omega_n(z)
=q(z)^n\frac{d^n}{dz^n}\left(\frac{e^z}{1-z}\right)
=\sum_{k\ge0}u_k\frac{z^k}{k!}.
$$


Set


$$
B_n(z)=\Omega_n(z)-E_nH_n(z)-A_n(z)
=\sum_{k\ge0}b_k\frac{z^k}{k!}.
$$



These are exactly the retained seed-subtracted coefficients.

The elementary identity


$$
\frac{\Omega_n(z)}{H_n(z)}
=e^z n!\sum_{r=0}^n\frac{(1-z)^r}{r!}
$$


gives


$$
\left(\frac{\Omega_n}{H_n}\right)'
=e^z(1-z)^n.
$$


Also,


$$
\frac{A_n}{H_n}=e^z(1-z)^{n+1}.
$$


Consequently,


$$
\left(\frac{B_n}{H_n}\right)'
=(n+1+z)e^z(1-z)^n.
$$



Multiplication by $q(z)(1-z)$ yields


$$
\boxed{
q(z)(1-z)B_n'
-\left[nq'(z)(1-z)+(n+1)q(z)\right]B_n
=q(z)(n+1+z)A_n.
}
\tag{4.1}
$$



The right side is


$$
q(z)(n+1+z)
=(n+1)-nz+\frac{n-1}{2}z^2+\frac12z^3.
$$


Thus its $k$-th factorial-normalized coefficient is precisely


$$
F_k=(n+1)a_k-nk\,a_{k-1}
+\frac{(n-1)k(k-1)}2a_{k-2}
+\frac{k(k-1)(k-2)}2a_{k-3}.
$$



In particular, the actual recurrence is


$$
\boxed{
\begin{aligned}
b_{k+1}={}&(2k+1)b_k
+\frac{k(2n+1-3k)}2b_{k-1}\\
&+\frac{k(k-1)(k-n-1)}2b_{k-2}
+F_k.
\end{aligned}}
\tag{4.2}
$$


The same recurrence without $F_k$ holds for $h_k$.

The seeds remain


$$
(h_0,h_1,h_2)=(1,1,n+2),
$$




$$
(b_0,b_1,b_2)=(-1,n,n+2-n^2).
$$


For example, (4.2) at $k=0,1$ gives the displayed $b_1,b_2$. The seed $b_0=-1$ is essential.

This provides a recurrence-level basis for the congruences below; no arbitrary-source substitute is used.

## 5. Exact separation of the factorial term

Retain


$$
X=ma_n,\qquad Y=mna_{n-1},\qquad Z=2a_{n+1}-ma_n,
$$




$$
P=nX+Y,\qquad Q=nZ+2X-Y,
$$




$$
F=2m\bigl(Y-2X-(n-1)Z\bigr).
$$



Put


$$
L_{\rm ref}=2^{m/2},\qquad
\widehat h=L_{\rm ref}\tau_n,\qquad
\widehat\ell=L_{\rm ref}\tau_{n+1}.
$$


Both hatted references are integers.

For clarity, write


$$
v_n=u_n-a_n,\qquad v_{n+1}=u_{n+1}-a_{n+1}.
$$


The fixed exponential seed cancels from the Wronskian:


$$
h_nb_{n+1}-h_{n+1}b_n
=h_nv_{n+1}-h_{n+1}v_n.
$$


Using


$$
h_n=n!\tau_n,\qquad
h_{n+1}=\frac m2n!(\tau_n+\tau_{n+1}),
$$


the complete normalized companion is


$$
\widehat{\mathscr K}
=
\widehat h\,v_{n+1}
-\frac m2(\widehat h+\widehat\ell)v_n
-2L_{\rm ref}(n!)^2.
$$



Therefore


$$
\boxed{
\Theta_n
=
2L_{\rm ref}F(n!)^2
+\widehat h\,\mathcal T_n
+\widehat\ell\,\mathcal S_n,
}
\tag{5.1}
$$


where


$$
\boxed{
\begin{aligned}
\mathcal T_n
&=mZQ-Fv_{n+1}+\frac{mF}{2}v_n,\\
\mathcal S_n
&=-mZP+\frac{mF}{2}v_n.
\end{aligned}}
\tag{5.2}
$$


All quantities in (5.1) are integers.

Equation (5.1) is an exact determinant-remainder decomposition for the actual complete force. The seed cancellation is algebraic; the logarithmic contribution remains the term $2L_{\rm ref}F(n!)^2$. It has not been discarded.

The normalization has paid exactly the original factor $n!$:


$$
\Theta_n=\frac{L_{\rm ref}}{n!}\mathcal D_L.
$$


Nothing in (5.1) justifies a further factorial division.

---

# III. An all-odd-small-prime residue formula

## 6. Low-digit reduction of the actual moments and force

For an auxiliary nonnegative integer parameter $a$, define


$$
c_i(a)=i![z^i]q(z)^a.
$$


Then


$$
a_j(a)=\sum_{i=0}^j\binom ji c_i(a),
$$


and the actual force identity gives


$$
\boxed{
u_j(a)=\sum_{i=0}^j\binom ji c_i(a)E_{a+j-i}.
}
\tag{6.1}
$$


These auxiliary evaluations are used only for congruences. They are not additional approximation indices.

Fix an odd prime $p\le n$, and write


$$
n=pb+a,\qquad 0\le a<p.
$$



Because $q(z)^n\in\mathbb Z[1/2][z]$,


$$
v_p(c_i(n))\ge v_p(i!).
$$


Thus every term with $i\ge p$ vanishes modulo $p$. For $i<p$, Frobenius reduction gives


$$
c_i(n)\equiv c_i(a)\pmod p.
$$


Also,


$$
E_s\equiv E_{s\bmod p}\pmod p,
$$


directly from $E_s=sE_{s-1}+1$.

It follows that, when $a\le p-2$,


$$
\begin{aligned}
a_{n-1}(n)&\equiv a_{a-1}(a),\\
a_n(n)&\equiv a_a(a),\\
a_{n+1}(n)&\equiv a_{a+1}(a),
\end{aligned}
\qquad
u_n(n)\equiv u_a(a),\quad
u_{n+1}(n)\equiv u_{a+1}(a)
\pmod p,
\tag{6.2}
$$


with the evident interpretation of the $n a_{n-1}$ term when $a=0$.

### Reference reduction

The constant-term representation is


$$
\tau_k=\operatorname{CT}\left(1+z+\frac1{2z}\right)^k.
$$


For $k=pb+a$, $0\le a<p$, Frobenius gives


$$
\boxed{\tau_{pb+a}\equiv\tau_a\tau_b\pmod p.}
\tag{6.3}
$$


Indeed, an exponent contributed by the degree-$a$ Laurent factor lies between $-a$ and $a$; the only such exponent divisible by $p$ is zero.

Iterating (6.3) gives the usual digit product for this particular reference sequence.

### The complete scalar residue

For parameter $a$, form $X_a,Y_a,Z_a,P_a,Q_a,F_a$ by the same displayed polynomial formulas. Define the dyadic rational


$$
\begin{aligned}
\phi_a={}&(a+1)Z_a(Q_a\tau_a-P_a\tau_{a+1})\\
&-F_a\left[
\tau_a\bigl(u_{a+1}(a)-a_{a+1}(a)\bigr)
-\frac{a+1}{2}(\tau_a+\tau_{a+1})
 \bigl(u_a(a)-a_a(a)\bigr)
\right].
\end{aligned}
\tag{6.4}
$$



Since $p\le n$, the factorial term in (5.1) vanishes modulo $p$. Equations (6.2)–(6.3) prove


$$
\boxed{
L_{\rm ref}^{-1}\Theta_n
\equiv\tau_b\phi_a\pmod p,
\qquad 0\le a\le p-2.
}
\tag{6.5}
$$



If $a=p-1$, then $m\equiv0\pmod p$; both $mZ$ and $F$ vanish, so


$$
\boxed{\Theta_n\equiv0\pmod p.}
\tag{6.6}
$$



This is an exact support test at every odd prime $p\le n$. It is not merely a selected-prime observation. It determines whether $v_p(\Theta_n)=0$, but does not evaluate a positive valuation.

Among primes through $N=n+2$, the only additional possible odd prime is $p=N$. At that boundary the factorial term in (5.1) must be retained; formula (6.5) without it is not applicable.

## 7. Consequences: no $3,5,7$, and all-index nonvanishing

Two small auxiliary evaluations suffice.

At parameter $a=0$,


$$
a_0=a_1=1,\qquad u_0=1,\quad u_1=2,
$$


and


$$
Z_0=1,\quad P_0=0,\quad Q_0=2,\quad F_0=-2.
$$


Hence


$$
\boxed{\phi_0=4.}
\tag{7.1}
$$



At parameter $a=1$,


$$
a_0=1,\quad a_1=a_2=0,\qquad u_1=3,\quad u_2=8,
$$




$$
Z_1=0,\quad F_1=8,\qquad \tau_1=1,\quad\tau_2=2.
$$


Thus


$$
\boxed{\phi_1=8.}
\tag{7.2}
$$



The digit reference values needed for $p=3,5,7$ are:


$$
\begin{array}{c|l}
p&(\tau_0,\ldots,\tau_{p-1})\pmod p\\ \hline
3&(1,1,2)\\
5&(1,1,2,4,1)\\
7&(1,1,2,4,5,1,6).
\end{array}
$$


Every entry is nonzero. By (6.3),


$$
\tau_b\not\equiv0\pmod p
\qquad(p=3,5,7;\ b\ge0).
\tag{7.3}
$$



Every original $n$ is divisible by $3$ and $5$, so (6.5) with $a=0$ gives


$$
3\nmid\Theta_n,\qquad 5\nmid\Theta_n.
$$



For $n=105^r$, the same argument applies at $7$. For $n=15^r$,


$$
n\equiv1\pmod7,
$$


so (6.5) with $a=1$ and $\phi_1=8$ gives $7\nmid\Theta_n$.

We have proved:

### Theorem 7.1 — Arithmetic nonvanishing on the entire original domain


$$
\boxed{
\gcd(\Theta_n,105)=1
\quad\text{and hence}\quad
\Theta_n\ne0
}
$$


for every original index.

This conclusion uses the complete scalar, including the force remainder. Real dominance is not involved.

---

# IV. The scalar’s binary depth and the factorial obstruction

## 8. A standalone scalar binary theorem

Assume


$$
n=15^{2a+1},\qquad a\ge1.
$$


Then


$$
n\equiv15\pmod{32},\qquad v_2(m)=4.
$$


Put


$$
k=\frac{n-1}{2},\qquad t=v_2(n!).
$$


Thus $v_2(k+1)=3$ and


$$
t-v_2(k!)=k.
$$



Only very low moment and force precision is required.

### 8.1 Moment and force parities

The integral polynomial formula for $c_i(n)$ permits parameter reduction modulo $2$. At odd parameter,


$$
(c_0,c_1,c_2,c_3)\equiv(1,1,1,0)\pmod2,
$$


and $c_i\equiv0\pmod2$ for $i\ge4$, using


$$
v_2(c_i)\ge v_2(i!)-\lfloor i/2\rfloor.
$$


Therefore


$$
a_j\equiv1+j+\binom j2\pmod2.
$$


Since $n\equiv3\pmod4$,


$$
a_n\equiv1,\qquad a_{n-1}\equiv0,\qquad a_{n+1}\equiv1\pmod2.
\tag{8.1}
$$



Applying (6.1) modulo $2$, with $E_s\equiv1$ for even $s$ and $0$ for odd $s$, gives


$$
u_n\equiv u_{n+1}\equiv0\pmod2.
\tag{8.2}
$$



### 8.2 Reference depths

The terminal-summand argument in the constant-term formula gives


$$
v_2(\tau_n)\ge-v_2(k!)+1,
$$


and


$$
v_2(\tau_{n+1})=-v_2((k+1)!)
=-v_2(k!)-3.
$$


For completeness, the odd-index terminal-relative terms have ratios


$$
\frac{2^r(k)_r^2}{(2r+1)!}.
$$


The $r=1$ ratio is odd, so it cancels the terminal term modulo $2$; all $r\ge2$ ratios have positive valuation. For the even index, the $r=1$ ratio is $(k+1)^2$, of valuation $6$, and all other corrections are also deeper than the terminal term.

Consequently,


$$
v_2(h)\ge k+1,\qquad v_2(\ell)=k-3,
$$


and


$$
v_2(h_{n+1})
=v_2\!\left(\frac m2(h+\ell)\right)=k.
\tag{8.3}
$$



Equations (8.1)–(8.3) show that $b_n,b_{n+1}$ are odd. Hence


$$
\begin{aligned}
v_2(\mathscr K_n)
&=v_2\!\left(hb_{n+1}-h_{n+1}b_n-2(n!)^3\right)\\
&=k.
\end{aligned}
\tag{8.4}
$$


The term $-h_{n+1}b_n$ is uniquely of lowest valuation. The complete logarithmic term has depth $3t+1>k$.

### 8.3 The two terms of $\mathcal D_L$

From the moment parities,


$$
v_2(Z)=1,\qquad v_2(P)=4,\qquad v_2(Q)=1.
$$


Also,


$$
v_2\bigl(Y-2X-(n-1)Z\bigr)=2,
$$


so


$$
v_2(F)=7.
$$



The two terms in


$$
Qh-P\ell
$$


have depths at least $k+2$ and exactly $k+1$, respectively. Thus


$$
v_2(Qh-P\ell)=k+1.
$$


It follows that


$$
v_2\bigl(mZ(Qh-P\ell)\bigr)=k+6,
$$


whereas


$$
v_2(F\mathscr K_n)=k+7.
$$


Therefore


$$
v_2(\mathcal D_L)=k+6.
$$



Finally, paying the normalization exactly,


$$
\begin{aligned}
v_2(\Theta_n)
&=\frac m2-t+k+6\\
&=n+6-v_2(n!)\\
&=s_2(n)+6.
\end{aligned}
$$



### Theorem 8.1


$$
\boxed{
n=15^{2a+1},\ a\ge1
\quad\Longrightarrow\quad
v_2(\Theta_n)=s_2(n)+6.
}
$$



This proof uses neither the primitive contact-row binary contents nor an endpoint denominator formula. It is separate from the endpoint binary law still under review.

## 9. What this proves—and does not prove—about smoothness

The exact decomposition (5.1) and Theorems 7.1–8.1 rule out a tempting but invalid inference:

> The dominant term contains $(n!)^2F$, so the canonical complete scalar should retain a comparable factorial divisor.

In fact,


$$
v_3(\Theta_n)=v_5(\Theta_n)=v_7(\Theta_n)=0
$$


at every original index. Thus


$$
\Theta_n/n!\notin\mathbb Z
$$


throughout that domain.

On the odd-exponent $15$-family, even the binary depth is only $O(\log n)$, rather than the $\asymp n$ depth of $n!$. The complete recurrence remainder destroys those prospective factorial factors.

However, this is **not** a disproof of an all-small-prime estimate of the form


$$
\log U_n\ge3\log(n!)-O(n).
$$


For each fixed prime $p$,


$$
v_p(n!)\log p=O(n).
$$


The required smooth mass could, in principle, be supplied by the other primes through $N$.

What has been established is more precise:

- there is no extra factorial quotient available for free;
- the first-digit support at every odd $p\le n$ is governed by the complete residue $\tau_b\phi_a$, not by the factorial term;
- positive valuations at the remaining small primes require genuine higher-precision recurrence information;
- real dominance supplies no substitute for that information.

No all-small-prime lower bound of the requested strength is proved here.

---

# V. A different nonzero element of the product ideal

## 10. Reference-defect exclusion of endpoint-exclusive primes

Since Theorem 7.1 proves $\Theta_n\ne0$ everywhere in the original domain, Turn 9’s product and exclusive-content results now apply at every original index.

Retain


$$
D_n^{>}=(|\Theta_n|)_{>N},
\qquad
\mathcal A_n=\frac{D_n^{>}}{\mathcal B_n^2},
$$


and put


$$
C_n^{\rm clip}=\gcd(\mathcal A_n,\Sigma_n),
\qquad
X_n^{\rm exc}=\frac{\mathcal A_n}{C_n^{\rm clip}}.
$$


The earlier certificate is


$$
\mathcal W_n=D_n^{>}C_n^{\rm clip}.
$$



Define


$$
\widehat R_j=\alpha_j\widehat h+\beta_j\widehat\ell.
$$


For every $p>N$,


$$
v_p(\widehat R_j)=v_p(R_j),
$$


because


$$
\widehat R_j=\frac{2L_{\rm ref}}{mn!}R_j
$$


and the multiplier is a unit at that scope.

Since


$$
\mathcal B_n\mid\delta_j^{>}\mid\widehat R_j,
$$


the integers


$$
Y_j^{\rm ref}=\widehat R_j/\mathcal B_n
$$


are well defined. Set


$$
H_n^{\rm ref}
=\gcd(\Sigma_n,|Y_0^{\rm ref}|,|Y_3^{\rm ref}|).
$$



### Theorem 10.1 — Reference-defect exclusion

With


$$
g_n=\mathcal B_n\Gamma_n,
$$


one has


$$
\boxed{\Gamma_n\mid H_n^{\rm ref},}
\tag{10.1}
$$


and


$$
\boxed{
\gcd\!\left(E_{0,n}E_{3,n},
\frac{\Sigma_n}{H_n^{\rm ref}}\right)=1.
}
\tag{10.2}
$$



#### Proof

The earlier theorem gives $\Gamma_n\mid\Sigma_n$. Also,


$$
g_n\mid\delta_j^{>}\mid\widehat R_j,
$$


so $\Gamma_n\mid Y_j^{\rm ref}$ at both endpoints. This proves (10.1).

Turn 9 gives


$$
\gcd\!\left(E_{0,n}E_{3,n},\frac{\Sigma_n}{\Gamma_n}\right)=1.
$$


Since $\Gamma_n\mid H_n^{\rm ref}$,


$$
\frac{\Sigma_n}{H_n^{\rm ref}}
\mid
\frac{\Sigma_n}{\Gamma_n}.
$$


Equation (10.2) follows. ∎

### Primewise meaning

Let


$$
b=v_p(\mathcal B_n),\qquad s=v_p(\Sigma_n),
\qquad r_j=v_p(\widehat R_j).
$$


If


$$
\min(r_0,r_3)<b+s,
$$


then $p$ cannot be endpoint-exclusive.

Equivalently,


$$
\boxed{
e_0\ne e_3
\quad\Longrightarrow\quad
r_0,r_3\ge b+s.
}
\tag{10.3}
$$



This is a true restriction on the actual exclusive factors. It uses the actual references to detect when the full collision depth required by Turn 9 is unavailable.

## 11. An endpoint-specific reference bound

Define


$$
T_j^{\rm ref}
=
\frac{|Y_j^{\rm ref}|}
{\gcd(|Y_j^{\rm ref}|,\Sigma_n)}.
\tag{11.1}
$$


If $Y_j^{\rm ref}=0$, this definition gives $T_j^{\rm ref}=0$, which causes no difficulty in the gcds below.

Then


$$
\boxed{E_{j,n}\mid T_j^{\rm ref}.}
\tag{11.2}
$$



Indeed, if $p\mid E_{j,n}$, the two endpoint depths differ, and the smaller is exactly $b+s$. Thus


$$
v_p(E_{j,n})
=e_j-b-s
\le r_j-b-s
=v_p(T_j^{\rm ref}).
$$


At primes not dividing $E_{j,n}$, the divisibility is automatic.

This removes the full collision depth from the available reference depth before bounding an exclusive exponent.

## 12. The reference-filtered product certificate

For positive integers $x,z$, let


$$
\operatorname{strip}_{z}(x)
$$


denote the integer obtained from $x$ by removing every prime power whose prime divides $z$. It can be evaluated by repeated gcd and exact division, without factoring the large cofactor.

Set


$$
J_n^{\rm def}=\frac{\Sigma_n}{H_n^{\rm ref}},
$$




$$
X_n^\circ
=\operatorname{strip}_{J_n^{\rm def}}(X_n^{\rm exc}),
$$


and


$$
V_{j,n}=\gcd(X_n^\circ,T_j^{\rm ref}),
\qquad
V_n=\operatorname{lcm}(V_{0,n},V_{3,n}).
$$



Theorems 10.1–11.1 and Turn 9’s exclusive divisor give


$$
E_{j,n}\mid V_{j,n}.
$$


Because $\gcd(E_{0,n},E_{3,n})=1$,


$$
\boxed{E_{0,n}E_{3,n}\mid V_n.}
\tag{12.1}
$$



Meanwhile,


$$
g_n\mid\mathcal B_nH_n^{\rm ref}.
$$


Therefore


$$
\boxed{
\delta_0^{>}\delta_3^{>}
\mid
\mathcal B_n^2(H_n^{\rm ref})^2V_n.
}
\tag{12.2}
$$



Combining this with the earlier clipped certificate proves:

### Theorem 12.1 — Reference-filtered product element

The positive integer


$$
\boxed{
\mathcal W_n^{\rm ref}
=
\gcd\!\left(
\mathcal W_n,\,
\mathcal B_n^2(H_n^{\rm ref})^2V_n
\right)
}
\tag{12.3}
$$


satisfies


$$
\boxed{
\delta_0^{>}\delta_3^{>}\mid\mathcal W_n^{\rm ref}
\mid\mathcal W_n.
}
\tag{12.4}
$$



Consequently, $\mathcal W_n^{\rm ref}$ belongs to


$$
(R_0,C_0)(R_3,C_3)
$$


after localization only at primes at most $N$.

All integers in this construction have their displayed canonical normalizations. The certificate is not made artificially small by dividing an integer by unsupported small-prime factors.

### Why this is a different route

The new certificate does not require the entire large-prime part $D_n^{>}$ to be small.

A large factor of $D_n^{>}$ may be discarded from the exclusive bound if:

1. it lies on a collision prime where the two references do not both reach the required depth; or
2. the relevant endpoint reference lacks sufficient depth after the collision factor has been removed.

Thus failure of smoothness for this particular $\Theta_n$ would not automatically defeat the reference-filtered certificate.

No useful height estimate for the surviving factors is yet proved.

## 13. Combining the sharper projection cost

A4’s comparison now gives


$$
\boxed{
\mathfrak D_0\mathfrak D_3
\mid B_0B_3\,\mathcal W_n^{\rm ref}.
}
\tag{13.1}
$$


The projection cost remains polynomial:


$$
B_0B_3\le\Pi_0\Pi_3.
$$



The coprimality of $B_0,B_3$ is retained, but no estimate for actual residual content is inferred from it.

Since


$$
\mathcal B_n\mid
\left(2^{(n+1)/2}\tau_{n+1}\right)_{>N},
$$


the already established reference bound gives


$$
\log\mathcal B_n=O(n).
$$


Hence a concrete sufficient follow-on lemma for the new route is:

> **Reference-defect filtered-content lemma.**  
> On an infinite original subsequence, prove
> 

$$
> 2\log H_n^{\rm ref}+\log V_n=O(n),
>
$$


> or at least $o(n\log n)$, for the explicit quantities in §§10–12.

This target is different from bounding all of $D_n^{>}$: it concerns only the common reference collision ceiling and the exclusive factors surviving both support and depth filters.

---

# VI. What remains unproved

## 14. Scalar arithmetic status

Turn 9’s complete-scalar size estimate remains


$$
\log|\Theta_n|
=
3\log(n!)
+n\log(2+\sqrt2)
+\frac52\log n+O(1).
$$


The new congruences do not change that real estimate.

The original certificate still has exact height


$$
\log\mathcal W_n
=
\log|\Theta_n|-\log U_n
+\log\gcd(\Sigma_n,\mathcal A_n).
$$



Neither of the following has been proved:

- a sufficiently large all-small-prime factor $U_n$;
- a sufficiently small clipped collision gcd.

The alternative certificate introduces a genuinely narrower set of possible contributors, but neither


$$
H_n^{\rm ref}
\quad\text{nor}\quad
V_n
$$


has been bounded at the required infinite-family scale.

The new arithmetic nonvanishing is valuable because every displayed product certificate is now nonzero at every original index. It does not resolve the height problem.

## 15. Primitive whole-form nonvanishing remains separate

The scalar $\Theta_n$ is a determinant of the shared contact column with the complete reference and residual columns. It is not the final approximation error.

Thus


$$
\Theta_n\ne0
$$


does not imply


$$
q_\lambda(e+\pi)-p_\lambda\ne0
$$


for a proposed weight.

A successful irrationality argument would still require an infinite original-index family of actual primitive whole forms satisfying


$$
0<|q_\lambda(e+\pi)-p_\lambda|\longrightarrow0.
$$


No such family is proved here.

---

# VII. Final normalization and the whole same-index error

## 16. Both corrected columns and all row contents

With the retained notation


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


the complete columns remain


$$
u=(-sx_0,\ sx_0-sx_1,\ sx_1-sx_2,\ sx_2),
$$




$$
v=(1-sy_0,\ sy_0-sy_1,\ sy_1-sy_2,\ sy_2).
$$


The exterior $+1$ is retained in $v_0$.

The least clearer is over all eight entries, and every reconstructed row is divided by its actual two-entry content.

At $3375$, the accepted row contents remain


$$
(113940000,\ 9780750,\ 10125,\ 1).
$$


They are not replaced by contact-row contents, $\mathcal B_n$, or a reference-filter content.

## 17. Actual endpoint and weighted denominators

The all-prime endpoint identity remains


$$
\boxed{
d_j=
\frac{|n!R_j|}
{\gcd(|n!R_j|,\ |E_nR_j+C_j|)}.
}
\tag{17.1}
$$



For a reduced weight $\lambda=a/k_{\rm wt}$, retain


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
\right),
\qquad h_{\rm end}=\gcd(d_0,d_3).
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
\tag{17.2}
$$


Every prime remains in these gcds.

The whole same-index error remains


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda e_3\alpha_{n,2}(\lambda-\Lambda_{n,2}).
}
\tag{17.3}
$$



The five accepted $3375$ whole forms remain finite, nonzero values of absolute value greater than $1$. Nothing proved about $\Theta_n$ changes those evaluations.

---

# VIII. New bounded arithmetic and proof status

## 18. The assigned scalar computation is not repeated

The coordinator is already computing the new fields


$$
\Theta_{3375},\quad U_{3375},\quad D_{3375}^{>},
\quad \gcd(\Sigma_{3375},D_{3375}^{>}),
$$


and the corresponding certificate sizes.

No result from that calculation is assumed, and no repeat is proposed.

The present theorems supply new, independently verifiable predictions for that same canonical scalar:


$$
\boxed{
v_2(\Theta_{3375})=14,
\qquad
v_3(\Theta_{3375})=
v_5(\Theta_{3375})=
v_7(\Theta_{3375})=0.
}
\tag{18.1}
$$


Here $s_2(3375)=8$. These are theorem consequences, not reported execution outputs.

## 19. Optional new reference-filter postprocessing

No finite computation is required for the proofs above.

If the alternative certificate is to be assessed at the retained index, the genuinely new arithmetic is the following additional gcd-only postprocessing.

### Inputs

- the newly computed $D_{3375}^{>}$ and clipped gcd;
- the already retained $\Sigma_{3375}$;
- the actual primitive contact rows;
- $\widehat h,\widehat\ell$.

The accepted boundary receipt gives $\mathcal B_{3375}=1$; it need not be recomputed.

### New outputs

Form


$$
\widehat R_j=\alpha_j\widehat h+\beta_j\widehat\ell,
$$


then compute


$$
H^{\rm ref}=\gcd(\Sigma,\widehat R_0,\widehat R_3),
$$




$$
X^{\rm exc}=\frac{D^{>}}{\gcd(D^{>},\Sigma)},
\qquad
X^\circ=\operatorname{strip}_{\Sigma/H^{\rm ref}}(X^{\rm exc}),
$$




$$
T_j^{\rm ref}
=\frac{|\widehat R_j|}{\gcd(|\widehat R_j|,\Sigma)},
$$




$$
V_j=\gcd(X^\circ,T_j^{\rm ref}),
\qquad
V=\operatorname{lcm}(V_0,V_3),
$$


and


$$
\mathcal W^{\rm ref}
=\gcd\!\left(\mathcal W,(H^{\rm ref})^2V\right).
$$



The expected verifiable outputs are exact integers, bit lengths, and the identities


$$
X^\circ\mid X^{\rm exc},
\qquad
\gcd(X^\circ,\Sigma/H^{\rm ref})=1,
\qquad
\mathcal W^{\rm ref}\mid\mathcal W.
$$



No numerical sizes are predicted. In particular, the already observed complete joint gcd $1$ does **not** imply $H^{\rm ref}=1$, since $H^{\rm ref}$ uses the references without the complete residuals.

This task would neither rerun a producer nor recompute an old endpoint denominator or whole error.

## 20. Status ledger

| Statement | Status |
|---|---|
| New $3375$ joint/cross-product receipt | Accepted finite corroboration |
| $\Sigma_{3375}$ has $116931$ bits | Finite fact |
| Actual joint large gcd and boundary large gcd are $1$ | Finite facts |
| A4’s reference-sensitive projection cost | Reused at its proved scope |
| Actual complete-force recurrence (4.2) | Explicitly derived |
| Canonical determinant-remainder identity (5.1) | New exact identity |
| Odd-small-prime residue criterion (6.5)–(6.6) | New proof |
| $\gcd(\Theta_n,105)=1$ | New original-domain theorem |
| $\Theta_n\ne0$ at every original index | New arithmetic nonvanishing theorem |
| $v_2(\Theta_n)=s_2(n)+6$ on $15^{2a+1}$ | New standalone scalar theorem |
| Further factorial division of $\Theta_n$ | Rigorously obstructed |
| Required all-small-prime lower bound for $U_n$ | Not proved |
| Reference-defect exclusion of exclusive primes | New consequence for actual references |
| Reference-filtered nonzero product certificate | New proved certificate |
| Exponential height of either product certificate | Open |
| New $\Theta_{3375}$ decomposition and certificate sizes | Pending coordinator computation |
| Infinite primitive whole forms tending to zero | Open |
| Irrationality or rationality of $e+\pi$ | Unresolved |

---

# Conclusion

The scalar obstruction has advanced beyond eventual real nonvanishing.

The actual complete moment/force recurrence proves


$$
\boxed{\gcd(\Theta_n,105)=1}
$$


at every original index, and therefore proves $\Theta_n\ne0$ throughout the original domain. On $15^{2a+1}$,


$$
\boxed{v_2(\Theta_n)=s_2(n)+6.}
$$



These are also precise obstructions to treating the dominant factorial term as a factorial divisor of the canonical integer. They do not establish, or disprove, the required all-small-prime smoothness bound.

A different product-ideal route is now available. Actual reference depth excludes endpoint-exclusive cancellation at every collision prime for which both references fail to attain the full required depth. This yields the explicit filtered certificate


$$
\boxed{
\delta_0^{>}\delta_3^{>}
\mid\mathcal W_n^{\rm ref}\mid\mathcal W_n,
}
$$


and, with A4’s sharper projection cost,


$$
\boxed{
\mathfrak D_0\mathfrak D_3
\mid B_0B_3\,\mathcal W_n^{\rm ref}.
}
$$



The exact remaining arithmetic bottleneck is now either:

1. sufficient all-small-prime mass and a controlled clipped collision gcd for the canonical $\Theta_n$; or
2. an infinite-family bound for the smaller, reference-filtered factors $H_n^{\rm ref}$ and $V_n$.

Neither has been proved. Even a successful arithmetic bound must still be combined with the actual all-prime $q_\lambda$ and a nonzero whole same-index error tending to zero.



$$
\boxed{\text{No unconditional proof or disproof of the irrationality of }e+\pi
\text{ has been obtained.}}
$$


