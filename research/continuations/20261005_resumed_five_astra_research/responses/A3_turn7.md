> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3, Turn 7 — A terminal-plane reduction, an exact logarithmic companion, and the arithmetic obstruction in the exponential displacement

## 1. Executive conclusion

The objective remains an unconditional proof or disproof of the irrationality of


$$
S=e+\pi.
$$


It is not resolved here.

This report advances the **actual** $d=2$ producer. In particular, it does not replace


$$
\Theta^{\exp,\mathrm{flat}}+n!\mathfrak u_n^{\exp}F(n)
$$


by either the flat target or its leading homogeneous digit.

The main new results proved below are:

1. **A forced three-term recurrence in the original producer index.**  
   The normalized diagonal exponential force
   

$$
b_n^{\exp}:=\frac{w_0^{\exp}(n)}{(n!)^2}
$$


   satisfies an explicitly forced version of the same recurrence as $\tau_n$. The complete logarithmic diagonal satisfies its homogeneous version.

2. **An exact evaluation of the entire logarithmic contact vector.**  
   Let
   

$$
\rho_0=0,\qquad \rho_1=1,\qquad
   (n+2)\rho_{n+2}=(2n+3)\rho_{n+1}+(n+1)\rho_n.
$$


   Then the complete logarithmic force is
   

$$
\boxed{
   w^{\log}
   =4(n!)^2
   \begin{pmatrix}
   \rho_n\\[1mm]
   \dfrac{n+1}{2}(\rho_n+\rho_{n+1})\\[2mm]
   \dfrac{(n+1)(n+2)}2\rho_{n+2}
   \end{pmatrix}.
   }
$$


   This retains every logarithmic forcing term and the original terminal boundary.

3. **A sharper selected-prime restoration theorem.**  
   At the eligible selected primes,
   

$$
\boxed{
   w^{\log}\in
   p^{\,2v_p(n!)-\lfloor\log_p n\rfloor}\mathbb Z_{(p)}^3.
   }
$$


   Thus Turn 6’s restoration budget can be sharpened from
   $\prod p^{\lfloor\log_p(2n+2)\rfloor}$ to
   

$$
\boxed{
   B_{\mathcal P}^{*}(n)
   =\prod_{p\in\mathcal P}p^{\lfloor\log_p n\rfloor}
   \le n^{|\mathcal P|}.
   }
$$


   This is still only a **selected-prime** statement.

4. **An exact exponential contact displacement and a proof of its arithmetic obstruction.**  
   A normalized discrete Wronskian $\omega_n$, defined explicitly below, satisfies a factorial-series tail identity and the real bound
   

$$
|\omega_n|\le \frac{64\,7^n}{n!}.
$$


   Nevertheless, at every eligible selected prime,
   

$$
\boxed{
   v_p(\omega_n)=-2v_p(n!),\qquad
   (n!)^2\omega_n\equiv2(-1)^n\tau_n\pmod p.
   }
$$


   In particular, $\omega_n\ne0$. Its small real size is accompanied by a large primitive denominator, not by a proved small integral dual vector.

5. **An exact two-scalar terminal-plane formula for the correct moving residue.**  
   The exponential force is reduced to its homogeneous scalar and one contact displacement. The resulting formula retains the full term $n!F(n)$, and makes explicit why neither the real-small displacement nor the terminal plane alone supplies the missing height theorem.

No sufficiently short infinite-family dual vector is produced. No explicit subexponential-height solution family is produced. The remaining obstruction is identified more sharply, but is not removed.

No tools were executed.

---

## 2. Scope, accepted results, and the finite receipt

### 2.1 Original indices and finite boundaries

The principal infinite families remain


$$
n=15^r,\quad r\ge2,\qquad \mathcal P=\{3,5\},
$$


or


$$
n=105^r,\quad r\ge2,\qquad \mathcal P=\{3,5,7\}.
$$



Throughout the actual reconstruction,


$$
d=2,\qquad b=3.
$$


The contact matrix has rows and columns $0,1,2$, and the reconstructed columns retain coordinates $0,1,2,3$.

Write


$$
Q(z)=1-z+\frac{z^2}{2},\qquad f_n=(n!)^2,
$$


and


$$
\mathcal B_N^{[m]}=N![z^N]\bigl(e^zQ(z)^m\bigr).
$$


Thus the original contact matrix is


$$
C_{ij}=(n+i)^{\underline j}\mathcal B_{n+i-j}^{[n]}.
$$



The complete force still uses the original maximum index $2n+2$. None of the arguments below continues a finite inverse past its boundary.

### 2.2 What is accepted and what is newly proved here

A4 Turn 14 accepts A3 Turn 5’s:

- complete scalar recurrence;
- three-$\tau$ first-force formula;
- near-factorial logarithmic strip;
- endpoint congruence and its stated $3,5,7$-adic consequences;
- $n^{5/2}$-scale threshold-height obstruction;
- exponential-height compatibility construction;
- exact dual-certificate criterion.

Those results are reused only at their stated scopes.

Turn 6’s homogeneous decomposition follows directly from the first-order differential equation and is rechecked in Section 3. Its middle-depth conclusion and selected-prime distortion proof are valid under the stated unit and precision hypotheses. The new arguments below strengthen the logarithmic strip and further reduce the exponential force.

The new specialized identities in this report have proofs here, but have not received a separate independent audit.

The binary construction in A4 Turn 14 has different parameters and normalization. Its high-sector compensation does not establish a reconstruction theorem for this $3\times3$ producer.

### 2.3 Exact scope of the completed computation

The supplied receipt reports:



$$
\begin{array}{c|rrrr}
n&15&30&105&210\\ \hline
\text{recurrence comparisons}&18&33&108&213\\
v_5(v_0)&2&3&3&2
\end{array}
$$



It also reports that the retained endpoints agree with the prior whole-column normalization and that all 18 specified bounded reconstruction tests are empty.

These are substantial finite checks. They do **not** establish infinite absence of polynomial- or subexponential-height reconstructions.

The supplied recurrence script does not, by itself, check all of Turn 6’s new flat-decomposition identities. The proofs below do not treat the receipt as having done so.

No further window enumeration is requested.

---

## 3. Rechecking the homogeneous split and the terminal plane

Let


$$
\mathscr H(z)=\frac{e^z+f(z)}{1-z},
\qquad
f(0)=0,\qquad f'(z)=\frac2{Q(z)},
$$


and


$$
A_n(z)=Q(z)^n\mathscr H^{(n)}(z).
$$


The accepted complete differential equation is


$$
\mathscr L_nA_n=e^zQ^{n+1}+2R_n,
$$


where


$$
\mathscr L_nA
=(1-z)QA'
-\bigl[n(1-z)Q'+(n+1)Q\bigr]A,
$$


and $R_n$ has degree $n$.

Define


$$
\mathcal Z_n(z)=\frac{n!Q(z)^n}{(1-z)^{n+1}}.
$$


Direct differentiation gives


$$
\mathscr L_n\mathcal Z_n=0.
$$


The contact coefficients of $\mathcal Z_n$ are exactly the first force $z$.

Since $A_n(0)=n!\eta_n$,


$$
A_n^{\mathrm{flat}}=A_n-\eta_n\mathcal Z_n
$$


has zero initial value and satisfies the **same complete forced equation**. Hence


$$
w=w^{\mathrm{flat}}+\eta_nz.
$$



For the exponential part, set


$$
s_n^{\exp}:=\sum_{j=0}^n\frac1{j!}=\frac{F(n)}{n!}.
$$


Then, exactly,


$$
\boxed{
w^{\exp}=w^{\exp,\mathrm{flat}}+s_n^{\exp}z.
}
\tag{3.1}
$$



The endpoint-difference determinant is invariant under adding a scalar multiple of $z$. Consequently, the exponential residue has the exact decomposition


$$
\boxed{
\Theta^{\exp}
=\Theta^{\exp,\mathrm{flat}}
+n!\mathfrak u_n^{\exp}F(n).
}
\tag{3.2}
$$



This confirms the correct target. The term $F(n)$ is not replaced by $1$.

At the original terminal boundary, put


$$
a_n=\frac{(n+1)(n+2)}2,\qquad b_n=2n+3,
$$


and


$$
E_n:=\mathcal B_{n+1}^{[n+1]}.
$$


The accepted recurrence at $N=n+1$ gives


$$
\boxed{
w_2-b_nw_1+a_nw_0=E_n.
}
\tag{3.3}
$$


The corresponding right side is zero for the first force and for the logarithmic force separately.

This relation will now be used to reduce, rather than merely describe, the remaining contact data.

---

## 4. A forced three-term recurrence in the original index

The following reduction uses adjacent original producers. It does not change the contact boundary of any producer.

### 4.1 Contiguity before contact extraction

For either the complete function or either force component separately,


$$
A_{n+1}=QA_n'-nQ'A_n.
\tag{4.1}
$$



Write


$$
D_n:=w_0(n)=n![z^n]A_n(z).
$$


Here $D_n$ is a diagonal force coefficient, not an endpoint determinant.

Coefficient extraction in (4.1) yields


$$
D_{n+1}
=w_2(n)-w_1(n)-\frac{n(n+1)}2w_0(n).
$$


Using the terminal relation (3.3),


$$
\boxed{
D_{n+1}
=2(n+1)w_1(n)-(n+1)^2D_n+E_n.
}
\tag{4.2}
$$



Also set


$$
G_n:=\mathcal B_{n+2}^{[n+1]}.
$$


Applying the accepted recurrence at $N=n+2$, where the polynomial logarithmic force is again zero, gives


$$
\boxed{
w_1(n+1)
=(n+1)(3n+5)w_1(n)
-(n+1)^2(n+2)D_n
+(2n+3)E_n+G_n.
}
\tag{4.3}
$$



Substituting (4.2) into the next instance of (4.2) proves the following.

### Theorem 4.1 — Diagonal forced recurrence

For the complete force and for its exponential part,


$$
\boxed{
D_{n+2}
=(n+2)(2n+3)D_{n+1}
+(n+2)(n+1)^3D_n+\Psi_n,
}
\tag{4.4}
$$


where the complete forcing term is


$$
\boxed{
\Psi_n
=(n+1)(n+2)E_n+2(n+2)G_n+E_{n+1}.
}
\tag{4.5}
$$



For the logarithmic part, the same recurrence holds with forcing zero.

#### Normalized form

Define


$$
b_n^\bullet=\frac{D_n^\bullet}{(n!)^2},
\qquad
\psi_n=\frac{\Psi_n}{(n+2)((n+1)!)^2}.
$$


Then


$$
\boxed{
(n+2)b_{n+2}^{\exp}
=(2n+3)b_{n+1}^{\exp}
+(n+1)b_n^{\exp}+\psi_n.
}
\tag{4.6}
$$


The same equation holds for the complete diagonal. The logarithmic diagonal satisfies


$$
\boxed{
(n+2)b_{n+2}^{\log}
=(2n+3)b_{n+1}^{\log}
+(n+1)b_n^{\log}.
}
\tag{4.7}
$$



The initial values are


$$
b_0^{\exp}=1,\qquad b_1^{\exp}=3,
$$




$$
b_0^{\log}=0,\qquad b_1^{\log}=4.
$$



All terms in (4.5) come from the exponential forcing at actual terminal indices. The vanishing of the logarithmic forcing in (4.7) is a consequence of the degree bound on $R_n$, not an omission of that force.

---

## 5. Exact solution of the logarithmic contact force

### 5.1 The companion sequence

Let


$$
\rho_0=0,\qquad \rho_1=1,
$$


and


$$
(n+2)\rho_{n+2}
=(2n+3)\rho_{n+1}+(n+1)\rho_n.
\tag{5.1}
$$


The first-force sequence satisfies the same recurrence:


$$
(n+2)\tau_{n+2}
=(2n+3)\tau_{n+1}+(n+1)\tau_n,
\qquad \tau_0=\tau_1=1.
$$



Equation (4.7) and the initial values prove


$$
b_n^{\log}=4\rho_n.
$$



Using (4.2) and the terminal relation now gives the entire force.

### Theorem 5.1 — Complete logarithmic contact formula

For every nonnegative original index $n$,


$$
\boxed{
w^{\log}
=4f_n
\begin{pmatrix}
\rho_n\\[1mm]
\dfrac{n+1}{2}(\rho_n+\rho_{n+1})\\[2mm]
\dfrac{(n+1)(n+2)}2\rho_{n+2}
\end{pmatrix}.
}
\tag{5.2}
$$



This is an exact identity for the original finite force sums.

### 5.2 A finite convolution and its denominators

Let


$$
T(t)=\sum_{n\ge0}\tau_nt^n=(1-2t-t^2)^{-1/2},
$$


and


$$
R(t)=\sum_{n\ge0}\rho_nt^n.
$$


The recurrence gives


$$
(1-2t-t^2)R'(t)-(1+t)R(t)=1.
$$


Since $T$ solves the corresponding homogeneous equation,


$$
R(t)=T(t)\int_0^tT(s)\,ds.
$$


Therefore


$$
\boxed{
\rho_n
=\sum_{j=0}^{n-1}
\frac{\tau_j\tau_{n-1-j}}{j+1}.
}
\tag{5.3}
$$



Because


$$
\tau_j
=\sum_{h=0}^{\lfloor j/2\rfloor}
2^{-h}\binom j{2h}\binom{2h}h,
$$


a denominator of $\rho_n$ divides


$$
2^{\lfloor(n-1)/2\rfloor}\operatorname{lcm}(1,\ldots,n).
\tag{5.4}
$$


In particular, for every odd prime,


$$
\boxed{
v_p(\rho_n)\ge-\lfloor\log_p n\rfloor.
}
\tag{5.5}
$$



### 5.3 Exact logarithmic displacement in the terminal plane

The discrete Wronskian is especially simple:


$$
\boxed{
\tau_n\rho_{n+1}-\tau_{n+1}\rho_n
=\frac{(-1)^n}{n+1}.
}
\tag{5.6}
$$



Indeed, the recurrence multiplies this Wronskian by
$-n/(n+1)$ at each step, and its initial value is $1$.

Put


$$
P_n=\begin{pmatrix}0\\1\\2n+3\end{pmatrix}.
$$


Since the first force is


$$
z=f_n
\begin{pmatrix}
\tau_n\\[1mm]
\dfrac{n+1}{2}(\tau_n+\tau_{n+1})\\[2mm]
\dfrac{(n+1)(n+2)}2\tau_{n+2}
\end{pmatrix},
$$


equations (5.2) and (5.6) imply


$$
\boxed{
w^{\log}
=\frac{4\rho_n}{\tau_n}z
+\frac{2(-1)^nf_n}{\tau_n}P_n.
}
\tag{5.7}
$$



This is the promised terminal-plane reduction of the **complete** logarithmic force. Its nonhomogeneous plane displacement is explicitly nonzero.

---

## 6. Sharpening the selected-prime restoration budget

Assume $p>2$, $p\mid n$, $\tau_n$ is a $p$-adic unit, and the accepted local inverse theorem applies.

Let


$$
N_p=v_p(n!),\qquad m_p=2N_p,\qquad
d_p^*=\lfloor\log_p n\rfloor,
\qquad K_p^*=m_p-d_p^*.
$$



The first term in (5.7) has valuation at least $m_p-d_p^*$. The second has valuation exactly $m_p$. Thus:

### Theorem 6.1 — Sharper complete-force strip



$$
\boxed{
w^{\log}\in p^{K_p^*}\mathbb Z_{(p)}^3.
}
\tag{6.1}
$$



Consequently, provided $K_p^*\ge1$,


$$
\boxed{
\Theta-\Theta^{\exp}
\in p^{K_p^*}\mathbb Z_{(p)}.
}
\tag{6.2}
$$



The proof of Turn 6’s denominator-distortion theorem then applies with $d_p^*$ in place of $\lfloor\log_p(2n+2)\rfloor$. For every reduced weight $a/k$,


$$
\boxed{
\left|v_p(q_\lambda)-v_p(q_\lambda^{\exp})\right|
\le\lfloor\log_p n\rfloor.
}
\tag{6.3}
$$



Hence


$$
\boxed{
(B_{\mathcal P}^*(n))^{-1}
\le
\frac{(q_\lambda)_{\mathcal P}}
     {(q_\lambda^{\exp})_{\mathcal P}}
\le B_{\mathcal P}^*(n),
\qquad
B_{\mathcal P}^*(n)\le n^{|\mathcal P|}.
}
\tag{6.4}
$$



### Why the denominator proof remains valid

If $p\mid k$, reducedness and the local unit hypotheses give


$$
v_p(q_\lambda)
=v_p(q_\lambda^{\exp})
=m_p+v_p(k).
$$



If $p\nmid k$, the two reconstruction errors


$$
a-k\Theta,\qquad a-k\Theta^{\exp}
$$


are congruent modulo $p^{K_p^*}$. Their valuations are either equal below $K_p^*$, or both at least $K_p^*$. Truncating at $m_p$ changes the local denominator exponent by at most $m_p-K_p^*=d_p^*$.

This argument includes exact cancellation: the convention is
$\min(m_p,\infty)=m_p$.

### Scope

This strengthens the near-factorial precision. It does not alter the original index or delete any force term.

It also does not control:

- unselected-prime endpoint factors;
- the full least clearer;
- the final all-prime gcd;
- the whole primitive denominator.

---

## 7. The exponential discrete Wronskian

The logarithmic force has now been evaluated exactly. The remaining difficult arithmetic is in the forced exponential companion.

Define


$$
W_n^{\exp}
=\tau_nb_{n+1}^{\exp}-\tau_{n+1}b_n^{\exp},
$$


and


$$
\boxed{
\omega_n=(-1)^n(n+1)W_n^{\exp}.
}
\tag{7.1}
$$



### 7.1 Exact first-order forced recurrence

Using (4.6) and the homogeneous recurrence for $\tau_n$,


$$
(n+2)W_{n+1}^{\exp}
=-(n+1)W_n^{\exp}+\tau_{n+1}\psi_n.
$$


Therefore


$$
\boxed{
\omega_{n+1}
=\omega_n+(-1)^{n+1}\tau_{n+1}\psi_n,
\qquad \omega_0=2.
}
\tag{7.2}
$$



Equivalently,


$$
\boxed{
\omega_n
=2+\sum_{j=0}^{n-1}(-1)^{j+1}\tau_{j+1}\psi_j.
}
\tag{7.3}
$$



This is an explicit scalar recurrence derived from the actual exponential force.

### 7.2 The exact terminal displacement

Define


$$
\delta_n^{\exp}
=w_1^{\exp}
-\frac{z_1}{z_0}w_0^{\exp}.
$$


Equation (4.2) gives


$$
\boxed{
\delta_n^{\exp}
=\frac{(-1)^nf_n\omega_n}{2\tau_n}
-\frac{E_n}{2(n+1)}.
}
\tag{7.4}
$$



Thus


$$
\boxed{
w^{\exp}
=\frac{b_n^{\exp}}{\tau_n}z
+\delta_n^{\exp}P_n+E_ne_2.
}
\tag{7.5}
$$



The three force coordinates have been reduced to:

- one homogeneous scalar $b_n^{\exp}/\tau_n$;
- one explicitly forced displacement $\omega_n$;
- the explicit terminal exponential coefficient $E_n$.

This is an exact reduction, not an approximation.

---

## 8. Small in the real absolute value, large in the selected $p$-adic absolute values

This section supplies a precise obstruction to converting the exponential displacement into a short dual vector merely because its real value is small.

### 8.1 A real factorial bound

For


$$
\mathscr H^{\exp}(z)=\frac{e^z}{1-z},
$$


Leibniz’s rule gives


$$
A_n^{\exp}(z)
=\frac{n!Q(z)^n}{(1-z)^{n+1}}
e^z\sum_{j=0}^n\frac{(1-z)^j}{j!}.
$$


The exact Taylor remainder for the exponential implies


$$
A_n^{\exp}(z)
=e\,\mathcal Z_n(z)
-eQ(z)^n\int_0^1 e^{-u}u^ne^{uz}\,du.
\tag{8.1}
$$



For $0\le u\le1$,


$$
\left|N![z^N]e^{uz}Q(z)^n\right|
\le N!e(5/2)^n.
$$


Hence, for $i=0,1,2$,


$$
\boxed{
|w_i^{\exp}-ez_i|
\le
\frac{e^2(n+i)!}{n+1}(5/2)^n.
}
\tag{8.2}
$$



The positive coefficient formula for $\tau_n$ gives


$$
\tau_n\le(1+\sqrt2)^n.
$$


Also $\tau_{n+1}/\tau_n\le3$, so


$$
\frac{z_1}{z_0}\le2(n+1).
$$


It follows from (8.2) that


$$
|\delta_n^{\exp}|
\le3e^2n!(5/2)^n.
$$


Moreover,


$$
|E_n|
\le e(n+1)!(5/2)^{n+1}.
$$


Substitution into (7.4) proves


$$
\boxed{
|\omega_n|
\le\frac{64\,7^n}{n!}.
}
\tag{8.3}
$$



The constants are intentionally coarse. Their purpose is a rigorous factorial-scale bound, not an optimized asymptotic.

In particular, $\omega_n\to0$ in the real absolute value. The coefficient bounds also make the series below absolutely convergent, and (7.3) yields


$$
\boxed{
\omega_n
=-\sum_{j=n}^{\infty}(-1)^{j+1}\tau_{j+1}\psi_j,
}
\tag{8.4}
$$


with


$$
2+\sum_{j=0}^{\infty}(-1)^{j+1}\tau_{j+1}\psi_j=0.
$$



This is a proved factorial-tail identity.

### 8.2 Exact selected-prime pole and nonvanishing

Now let $p>2$, $p\mid n$, and suppose $\tau_n$ is a $p$-adic unit.

The homogeneous recurrence gives


$$
\tau_{n+1}\equiv\tau_n\pmod p,
$$


hence


$$
z_1/z_0\equiv1\pmod p.
$$



Directly from the exponential finite sums,


$$
w_0^{\exp}\equiv1,\qquad
w_1^{\exp}\equiv2\pmod p.
$$


Thus


$$
\delta_n^{\exp}\equiv1\pmod p.
\tag{8.5}
$$



Also


$$
E_n=\sum_j[z^j]Q^{n+1}\,(n+1)^{\underline j}.
$$


All terms with $j\ge2$ contain the factor $n$. The first two terms give


$$
E_n\equiv1-(n+1)^2\equiv0\pmod p.
\tag{8.6}
$$



Equation (7.4) therefore proves:

### Theorem 8.1 — Full-depth pole of the exponential displacement



$$
\boxed{
f_n\omega_n\equiv2(-1)^n\tau_n\pmod p,
}
\tag{8.7}
$$


and consequently


$$
\boxed{
v_p(\omega_n)=-2v_p(n!).
}
\tag{8.8}
$$



In particular,


$$
\boxed{\omega_n\ne0}
$$


at every index with such an eligible prime.

This nonvanishing is exact and arithmetic. It does not depend on a finite-order real asymptotic.

### 8.3 The primitive denominator of the displacement

Write $\omega_n=A_n^\omega/D_n^\omega$ in lowest terms, with $D_n^\omega>0$. Since $\omega_n\ne0$, (8.3) gives


$$
\boxed{
D_n^\omega\ge\frac{n!}{64\,7^n}.
}
\tag{8.9}
$$


At selected primes, (8.8) gives exactly


$$
\boxed{
(D_n^\omega)_{\mathcal P}
=\prod_{p\in\mathcal P}p^{2v_p(n!)}.
}
\tag{8.10}
$$


Therefore


$$
\boxed{
(D_n^\omega)_{\mathcal P^c}
\ge
\frac{n!}
{64\,7^n\prod_{p\in\mathcal P}p^{2v_p(n!)}}.
}
\tag{8.11}
$$



For either fixed selected set, the denominator on the right has logarithm


$$
n\log n-O(n).
$$


Thus the primitive denominator of this real-small displacement has a superexponential unselected part.

**Important limitation.** This is a theorem about $D_n^\omega$, not about $q_\lambda$. The actual force contains $f_n\omega_n$; that multiplication can cancel much of $D_n^\omega$. It would be incorrect to transfer (8.11) directly to the primitive center.

What has been ruled out is the shortcut


$$
\text{“the Padé displacement is real-small, therefore it is a short integral dual.”}
$$


Its integral normalization must be analyzed, and that normalization is arithmetically substantial.

---

## 9. Exact terminal-plane formula for the correct two-stage target

This section retains the complete homogeneous scalar rather than simplifying it.

Put


$$
s=(1,-n,n(n+1))^T,
\qquad
U_0=\frac{u_0}{f_n},\qquad
U_3=\frac{u_3}{f_n}.
$$


Define the rational endpoint responses


$$
g_0=-s^TC^{-1}P_n,\qquad g_3=e_2^TC^{-1}P_n,
$$




$$
h_0=-s^TC^{-1}e_2,\qquad h_3=e_2^TC^{-1}e_2.
$$



For the exponential force, let


$$
\sigma_n=\frac{b_n^{\exp}}{\tau_n},
\qquad
\delta_n=\delta_n^{\exp},
$$


and set


$$
A_0=1+\delta_ng_0+E_nh_0,\qquad
A_3=\delta_ng_3+E_nh_3.
\tag{9.1}
$$


The exterior $+1$ appears explicitly in $A_0$.

Equation (7.5) gives


$$
v_0^{\exp}=A_0+\sigma_nu_0,\qquad
v_3^{\exp}=A_3+\sigma_nu_3.
$$


Define


$$
\mathcal D_n=U_0A_3-U_3A_0.
\tag{9.2}
$$


At the eligible primes, $\mathcal D_n$ is a unit.

The residue is therefore


$$
\boxed{
\Theta^{\exp}
=\frac{U_0A_3+f_n\sigma_nU_0U_3}{\mathcal D_n}.
}
\tag{9.3}
$$



Now write


$$
\xi_n=\frac{b_n^{\exp}-s_n^{\exp}\tau_n}{\tau_n},
\qquad
\sigma_n=\xi_n+\frac{F(n)}{n!}.
$$


Then


$$
\boxed{
\Theta^{\exp,\mathrm{flat}}
=\frac{U_0A_3+f_n\xi_nU_0U_3}{\mathcal D_n},
\qquad
\mathfrak u_n^{\exp}=\frac{U_0U_3}{\mathcal D_n}.
}
\tag{9.4}
$$


Thus


$$
\boxed{
\Theta^{\exp}
=\Theta^{\exp,\mathrm{flat}}
+n!\mathfrak u_n^{\exp}F(n)
}
$$


again, now with an explicit terminal-plane description of both terms.

### 9.1 Division-safe reconstruction

For $p\nmid k$, reconstruction modulo $p^{K_p}$, with the original


$$
K_p=2N_p-\lfloor\log_p(2n+2)\rfloor,
$$


is exactly the original two-stage problem:



$$
a-k\Theta^{\exp,\mathrm{flat}}\equiv0\pmod{p^{N_p}},
\tag{9.5}
$$


followed by


$$
\boxed{
\frac{a-k\Theta^{\exp,\mathrm{flat}}}
{k n!\mathfrak u_n^{\exp}}
\equiv F(n)
\pmod{p^{\,N_p-\lfloor\log_p(2n+2)\rfloor}}.
}
\tag{9.6}
$$



The quotient is formed only after (9.5) makes it $p$-integral.

The sharper theorem in Section 6 permits the stronger modulus $K_p^*$, replacing the final exponent in (9.6) by


$$
N_p-\lfloor\log_p n\rfloor.
$$



The original near-factorial problem is not changed or weakened.

### 9.2 Restoring the logarithmic force exactly

Equation (5.7) gives the exact replacements


$$
\sigma_n\longmapsto\sigma_n+\frac{4\rho_n}{\tau_n},
\qquad
\delta_n\longmapsto\delta_n+\frac{2(-1)^nf_n}{\tau_n}.
\tag{9.7}
$$


The terminal coefficient $E_n$ is unchanged.

Thus the complete logarithmic restoration has two distinct effects:

- a homogeneous scalar shift with possible denominator loss
  $\lfloor\log_p n\rfloor$;
- a transverse terminal-plane shift at exact depth $2N_p$.

This explains the sharper restoration budget while preserving the final logarithmic digits.

---

## 10. Why this does not yet give an infinite subexponential exclusion

### 10.1 The precise obstruction

The terminal-plane reduction is substantial, but its two scalars do not automatically have favorable simultaneous real and modular height.

The situation is now explicit:

- $\omega_n$ is factorially small over $\mathbb R$;
- $\omega_n$ has a pole of exact order $2v_p(n!)$ at every eligible selected prime;
- the force uses $f_n\omega_n$, whose selected-prime residue is a nonzero unit;
- the homogeneous scalar still includes the entire $F(n)$;
- Cramer coefficients and their all-prime contents remain in the residue.

Consequently, neither the small real remainder nor the terminal contact relation supplies the required small integral dual vector without an additional arithmetic compression theorem.

### 10.2 No valid reduction to a known factorial-series irrationality theorem

The real series in (8.4) is not a convergent $p$-adic factorial series at the selected primes.

Indeed, its partial sums differ from $\omega_n$ by the fixed rational number $2$. Along either original smooth family,


$$
v_p(\omega_n)=-2v_p(n!)\longrightarrow-\infty.
$$


Those partial sums are unbounded in the selected $p$-adic absolute value and therefore cannot converge there.

Thus a theorem about a convergent series such as


$$
\sum_{j\ge0}(-1)^jj!
$$


cannot be applied to (8.4) merely because both formulas involve factorials.

The earlier $\mathfrak D_p$ controls a low-order expansion in $n$. It does not, by itself, control the entire factorial-depth residue in (9.3).

Likewise, the continued fraction of the fixed real number $e$, or a fixed-target Padé irrationality theorem, does not establish a denominator-gap bound for the moving rational residue in (9.3). No such reduction with verified hypotheses is established here.

### 10.3 A concrete sufficient follow-on lemma

The new recurrence gives a specific arithmetic object on which a continued-fraction or displacement estimate can be attempted.

Let


$$
L_n=\prod_{p\in\mathcal P}p^{K_p}
$$


or, for the strengthened strip, $\prod p^{K_p^*}$. Let $r_n$ be the actual residue obtained from (9.3) modulo $L_n$.

A useful explicit target is:

> **Terminal-displacement continued-fraction gap lemma sought.**  
> For infinitely many indices in one specified original smooth family, prove that the continued-fraction denominators of the exact rational number $r_n/L_n$ do not jump directly from below $L_n^{1/3}$ to above $L_n^{2/3}$.

Here is the exact significance of that quantitative statement.

Choose consecutive convergents $p_j/q_j,p_{j+1}/q_{j+1}$ with


$$
q_j\le L_n^{1/3}<q_{j+1}\le L_n^{2/3}.
$$


Then the two **actual** dual vectors


$$
(q_j,\ p_jL_n-q_jr_n),
\qquad
(q_{j+1},\ p_{j+1}L_n-q_{j+1}r_n)
$$


have determinant $\pm L_n$, and both coordinates are bounded by $L_n^{2/3}$.

For any reconstruction with


$$
\max(|a|,k)<\tfrac12L_n^{1/3},
$$


both dual pairings would be integers divisible by $L_n$ and of absolute value less than $L_n$. Both would vanish, contradicting independence.

Since


$$
\log L_n
=
\left(2\sum_{p\in\mathcal P}\frac{\log p}{p-1}\right)n+O(\log n),
$$


this would exclude all subexponential-height reconstructions, even without imposing a threshold window.

The elementary implication is not the missing theorem. The missing theorem is the **actual gap bound for the residue produced by (7.2), (7.4), and (9.3)**. Generic lattice geometry, fixed-target transference, and random-residue heuristics do not prove it.

This is a concrete sufficient follow-on lemma, not a claim that such a bound has been established.

---

## 11. Full gcd, unselected endpoint factors, and whole error

### 11.1 The actual primitive reduction is retained

Let $d_B$ be the least clearer of all entries of both complete reconstructed columns. Reduce the two endpoint rows and retain


$$
\widetilde u_0=hA,\qquad \widetilde u_3=hB,\qquad \gcd(A,B)=1.
$$


Put


$$
J=B\widetilde v_0-A\widetilde v_3,\qquad
\mathcal V=A\widetilde v_3,\qquad
T=aJ+k\mathcal V.
$$


For reduced $a/k$, $k>0$,


$$
F_{\rm gcd}
=\gcd(|A|,|a|)\gcd(|B|,|a-k|),
$$




$$
G=\gcd(k,|J|),
\qquad
H_{\rm gcd}
=\gcd\!\left(h,\frac{|T|}{F_{\rm gcd}G}\right).
$$


The actual primitive pair is still


$$
\boxed{
q_\lambda=\frac{kh|AB|}{F_{\rm gcd}GH_{\rm gcd}},
\qquad
p_\lambda=
\operatorname{sgn}(AB)\frac{T}{F_{\rm gcd}GH_{\rm gcd}}.
}
\tag{11.1}
$$



None of the scalar reductions above replaces this gcd.

### 11.2 A useful all-prime consequence of the full formula

For a threshold weight, eventually $a\ne0$ and $a-k\ne0$. Since


$$
G\mid k,\qquad H_{\rm gcd}\mid h,\qquad F_{\rm gcd}\mid AB,
$$


the exact formula gives


$$
q_\lambda\ge\frac{|AB|}{F_{\rm gcd}}
\ge\frac{|AB|}{|a|\,|a-k|}.
\tag{11.2}
$$


More specifically,


$$
\boxed{
(q_\lambda)_{\mathcal P^c}
\ge
\frac{|AB|_{\mathcal P^c}}{|a|\,|a-k|}.
}
\tag{11.3}
$$



Thus a subexponential-height weight can remove only a subexponential amount from the coprime endpoint factor $|AB|_{\mathcal P^c}$ through $F_{\rm gcd}$. The final shared gcd acts on $h$; it does not freely cancel those coprime endpoint factors.

This is an exact consequence of the full normalization. No asymptotic lower bound for $|AB|_{\mathcal P^c}$ is proved here.

### 11.3 Whole evaluated error and nonvanishing

The retained whole-error identity is


$$
\boxed{
q_\lambda S-p_\lambda
=q_\lambda e_3\alpha_{n,2}
(\lambda-\Lambda_{n,2}),
}
\tag{11.4}
$$


where


$$
e_3=(-1)^{n+1}4\pi(1+\sqrt2)^{-2n-3}
(1+O(n^{-1})),
$$




$$
\alpha_{n,2}=\frac2{n^2}(1+O(n^{-1})),
$$


and


$$
\Lambda_{n,2}
=\frac{n^2}{2}+\frac{1-3\sqrt2}{2}n+O(1).
$$



A valid irrationality construction still requires


$$
\boxed{
0<
q_\lambda|e_3\alpha_{n,2}|
\,|\lambda-\Lambda_{n,2}|
\longrightarrow0.
}
\tag{11.5}
$$



The nonvanishing of $\omega_n$ in Theorem 8.1 does **not** imply the nonvanishing of this whole evaluated form. They are different quantities.

For a future candidate family one must prove, separately:

1. the actual reconstruction congruences;
2. the actual full primitive denominator;
3. $\lambda\ne\Lambda_{n,2}$;
4. the whole product in (11.5) tends to zero.

A finite-order threshold expansion does not certify nonvanishing for an exceptionally close candidate.

---

## 12. Bounded exact arithmetic for personal inspection

No computation is needed to make the preceding proofs conditional or unconditional: they are algebraic and analytic derivations. A bounded consistency audit of the new identities would nevertheless be useful.

No new window enumeration is proposed.

### 12.1 Inputs

Use the original inputs


$$
n=15,30,105,210.
$$



For each input:

- retain the existing complete and exponential contact vectors;
- compute only the additional diagonal coefficients at the adjacent original indices $n+1,n+2$;
- generate $\tau_j,\rho_j$ through $j=n+2$;
- form $E_n,G_n,E_{n+1},\Psi_n,\psi_n,\omega_n$.

The additional diagonal finite sums require force indices at most $2n+4$, hence at most $424$. These are auxiliary neighboring original producers, not an extension of any $3\times3$ inverse.

### 12.2 Expected exact zero residuals

Verify, for each input:

1. The complete and exponential diagonal recurrence (4.4).
2. The logarithmic identity (5.2).
3. The finite convolution (5.3).
4. The Wronskian identity (5.6).
5. The exponential plane identity (7.5).
6. The displacement identity (7.4).
7. The exact two-stage decomposition (9.3)–(9.4).
8. The complete restoration rule (9.7).

Every residual should be exactly zero over $\mathbb Q$.

### 12.3 Predicted selected-prime outputs

The new theorems predict:



$$
\begin{array}{c|c|r|r|r}
n&p&
K_p^*=2v_p(n!)-\lfloor\log_p n\rfloor&
v_p(\omega_n)&
f_n\omega_n\bmod p\\ \hline
15&3&10&-12&2\\
15&5&5&-6&2\\
30&3&25&-28&2\\
30&5&12&-14&2\\
105&3&96&-100&1\\
105&5&48&-50&3\\
105&7&32&-34&3\\
210&3&200&-204&2\\
210&5&99&-102&1\\
210&7&66&-68&6
\end{array}
\tag{12.1}
$$



The congruence column is


$$
2(-1)^n\tau_n\bmod p.
$$



The improved strip is consistent with every reported finite logarithmic endpoint-difference depth. That consistency is not being used as its proof.

No new candidate weight is asserted, so no new primitive pair or whole-error interval is claimed.

---

## 13. Final proof ledger and remaining bottleneck

### New results proved here

- An exact forced three-term recurrence for the normalized exponential diagonal force in the original index.
- An exact homogeneous recurrence and closed finite convolution for the entire logarithmic diagonal.
- An exact three-coordinate formula for the complete logarithmic force.
- An exact terminal-plane logarithmic displacement.
- A sharper logarithmic restoration strip and polynomial selected-prime denominator budget.
- An exact scalar exponential Wronskian recurrence and terminal displacement formula.
- A factorial real bound for that displacement.
- Exact selected-prime poles and correct nonvanishing of the displacement.
- A primitive-denominator lower bound for the displacement itself, with an explicit warning that it is not the primitive center denominator.
- An exact two-scalar formula retaining
  

$$
\Theta^{\exp,\mathrm{flat}}+n!\mathfrak u_n^{\exp}F(n).
$$


- A full-gcd lower bound showing why unselected coprime endpoint factors cannot be ignored.

### What is not proved

There is still no:

- infinite-family subexponential exclusion for the correct moving residue;
- explicit subexponential-height solution family;
- favorable all-prime primitive-denominator estimate for such a family;
- new family of nonzero whole primitive forms tending to zero.

### Exact remaining mathematical bottleneck

The terminal contact recurrence has reduced the exponential arithmetic to a homogeneous scalar and a forced displacement. The remaining task is to prove a sufficiently strong **integral-height estimate after their actual modular recombination and content cancellation**.

The real-small displacement alone is insufficient: its selected-prime poles and large primitive denominator are explicit. The complete homogeneous scalar $F(n)$ remains indispensable. No applicable fixed-target or convergent factorial-series theorem has been shown to control their recombination.

Even if that reconstruction problem is resolved constructively, the unselected endpoint factors, final gcd, actual primitive denominator, and whole nonzero error in (11.5) remain mandatory.



$$
\boxed{
\text{The irrationality or rationality of }e+\pi\text{ remains unresolved.}
}
$$


