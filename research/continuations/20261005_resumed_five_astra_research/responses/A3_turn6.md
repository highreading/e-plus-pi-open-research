> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3, Turn 6 — A factorial-depth decomposition of the actual resonance and a polynomial-cost theorem for restoring the logarithmic force

## 1. Executive conclusion

The objective remains an unconditional proof or disproof of the irrationality of


$$
S=e+\pi.
$$


It is not resolved here.

This report advances the actual reconstruction problem at $d=2$, rather than repeating rational-reconstruction uniqueness or the previously obtained $n^{5/2}$ height obstruction.

The main results are:

1. **An exact homogeneous/forced decomposition of the actual moving residue.**  
   Writing
   

$$
F(n)=\sum_{t=0}^{n}n^{\underline t},
   \qquad
   \ell_n=\sum_{r=1}^{n}\frac{2\alpha_{r-1}}r,
$$


   the complete residue has the exact form
   

$$
\boxed{
   \Theta
   =\Theta^{\mathrm{flat}}
   +n!\,\mathfrak u_n\bigl(F(n)+n!\ell_n\bigr).
   }
   \tag{1.1}
$$


   Here $\Theta^{\mathrm{flat}}$ and the selected-prime unit $\mathfrak u_n$ are obtained from the **zero-initial-value forced recurrence**, with both the exponential and logarithmic forcing retained. The denominator governing the endpoint difference is independent of the removed homogeneous initial value.

2. **A proved, nonzero digit at the middle of the factorial precision.**  
   At the eligible primes considered below, put $N_p=v_p(n!)$. Then
   

$$
\boxed{
   v_p(\Theta-\Theta^{\mathrm{flat}})=N_p,
   \qquad
   \frac{\Theta-\Theta^{\mathrm{flat}}}{n!}
   \equiv\frac{\tau_n}{2}\pmod p.
   }
   \tag{1.2}
$$


   Thus the homogeneous initial value is not a negligible low-order normalization. It first enters at exactly half of the full depth $2N_p$, and its first normalized digit is nonzero.

3. **An infinite, factorial-scale obstruction to two specific reconstruction shortcuts.**  
   On the original families
   

$$
n=15^r,\quad r\ge2,
   \qquad\text{or}\qquad
   n=105^r,\quad r\ge2,
$$


   a weight that deeply reconstructs $\Theta^{\mathrm{flat}}$ instead of $\Theta$ leaves exactly $N_p$ powers of $p$ in the actual primitive denominator. Replacing the homogeneous factorial scalar by its leading value $1$ improves this by only $O(r)=O(\log n)$ digits. These are actual full-gcd statements, not statements about a raw minor.

4. **Restoring the complete logarithmic force costs only a polynomial factor in the selected-prime denominator budget.**  
   Let $q_\lambda^{\exp}$ be the reduced denominator of the auxiliary exponential-only center, with the exterior $+1$ retained, and let $q_\lambda$ be the actual complete denominator. For every reduced weight $a/k$,
   

$$
\boxed{
   B_{\mathcal P}(n)^{-1}
   \le
   \frac{(q_\lambda)_{\mathcal P}}
        {(q_\lambda^{\exp})_{\mathcal P}}
   \le B_{\mathcal P}(n),
   \quad
   B_{\mathcal P}(n)
   =\prod_{p\in\mathcal P}p^{\lfloor\log_p(2n+2)\rfloor}.
   }
   \tag{1.3}
$$


   In particular, $B_{\mathcal P}(n)\le(2n+2)^{|\mathcal P|}$. Exact full cancellation still requires the final logarithmic digits, but **an exponential selected-prime cancellation rate is unaffected by restoring them**.

5. **An exact terminal contact relation.**
   

$$
\boxed{
   \frac{(n+1)(n+2)}2\,w_0-(2n+3)w_1+w_2
   =\mathcal B_{n+1}^{[n+1]}.
   }
   \tag{1.4}
$$


   The same combination annihilates the first force and annihilates the logarithmic force separately. This is an exact consequence at the original finite boundary, not a continuation of the inverse outside that boundary.

These results do **not** exclude all polynomial- or subexponential-height reconstructions of the correct residue. They identify a genuine factorial-depth obstruction to simplified reconstruction and reduce the exponential-budget question to a complete, explicitly nested reconstruction problem.

No tools were executed.

---

## 2. Scope, original objects, and audit status

### 2.1 Original families

The main infinite-family statements use either


$$
\mathcal P=\{3,5\},\qquad n=15^r,\quad r\ge2,
\tag{2.1}
$$


or


$$
\mathcal P=\{3,5,7\},\qquad n=105^r,\quad r\ge2.
\tag{2.2}
$$


These are restrictions of the **original producer index $n$**. There is no rescaling of its factorials or contact boundary.

Throughout,


$$
d=2,\qquad b=3.
$$


The contact system has rows and columns $0,1,2$; reconstruction has coordinates $0,1,2,3$.

### 2.2 Complete producer

Set


$$
Q(z)=1-z+\frac{z^2}{2},\qquad q_j=[z^j]Q(z)^n,
$$


and


$$
\alpha_0=\alpha_1=1,\qquad
\alpha_j=\alpha_{j-1}-\frac12\alpha_{j-2}.
$$


In particular,


$$
\alpha_j\in\mathbb Z[1/2],
$$


which supplies the odd-prime integrality explicitly requested in the independent audit.

Define


$$
\eta_L=\sum_{r=0}^{L}\frac1{r!}
+\sum_{r=1}^{L}\frac{2\alpha_{r-1}}r,
\qquad
\mathcal W_L=L!\eta_L.
$$


The actual force is


$$
w_i
=\sum_{j=0}^{\min(2n,n+i)}
q_j(n+i)^{\underline j}\mathcal W_{2n+i-j},
\qquad 0\le i\le2.
\tag{2.3}
$$


Its maximum force index remains exactly $2n+2$.

The contact matrix and first force are


$$
C_{ij}=(n+i)^{\underline j}\mathcal B_{n+i-j},
\qquad
\mathcal B_L=L![z^L](e^zQ(z)^n),
\tag{2.4}
$$




$$
z=(n!)^2\bar z,
\qquad
\bar z=
\begin{pmatrix}
\tau_n\\[1mm]
\dfrac{n+1}{2}(\tau_n+\tau_{n+1})\\[2mm]
\dfrac{(n+1)(n+2)}2\tau_{n+2}
\end{pmatrix}.
\tag{2.5}
$$



With


$$
x=C^{-1}z,\qquad y=C^{-1}w,
\qquad
s_n=(1,-n,n(n+1))^T,
$$


the endpoints remain


$$
u_0=-s_n^Tx,\quad u_3=x_2,
\qquad
v_0=1-s_n^Ty,\quad v_3=y_2.
\tag{2.6}
$$



For clarity, the full reconstruction is still


$$
u=\mathsf I\mathcal Sx,\qquad
v=\mathsf I\mathcal Sy+e_0,
$$


where


$$
\mathcal S=
\begin{pmatrix}
1&-n&n(n+1)\\
0&1&-2n\\
0&0&1
\end{pmatrix},
\qquad
\mathsf I=
\begin{pmatrix}
-1&0&0\\
1&-1&0\\
0&1&-1\\
0&0&1
\end{pmatrix}.
\tag{2.7}
$$


The least clearer is taken over all entries of these two full columns.

### 2.3 What is reused and what is rederived

The accepted local theorem applies at every selected prime in (2.1)–(2.2). In particular, $\tau_n$ is a unit there, and


$$
v_p(u_0)=v_p(u_3)=2v_p(n!),\qquad
v_p(v_3)=0,\qquad p\nmid d_B.
\tag{2.8}
$$



I rechecked the algebra behind Turn 5’s differential recurrence and its factorial stripping. The coefficient of $a_{N-2}^{(n)}$ is indeed


$$
\frac{N(N-1)(N-n-1)}2,
$$


which is essential for the terminal identity proved below.

The sharper endpoint congruence also follows by the displayed Turn 5 argument:


$$
v_0\equiv-2n\mathfrak D_p
\pmod{p^{\min(2v_p(n),K_p(n))}},
\quad
\mathfrak D_p=\sum_{j\ge0}(-1)^jj!,
\tag{2.9}
$$


where


$$
K_p(n)=2v_p(n!)-\lfloor\log_p(2n+2)\rfloor.
$$


The potentially deficient term in the coefficient estimate is $j=p$; its additional bracket divisibility restores the claimed modulus. Thus on (2.1)–(2.2),


$$
w_3:=v_3(v_0)=r,\qquad
w_5:=v_5(v_0)=r+1,
\qquad
w_7:=v_7(v_0)=r
\tag{2.10}
$$


when the prime is selected. The restriction $r\ge2$ avoids the unresolved general $v_5(n)=1$ branch.

At the four supplied finite indices, the actual measured values remain


$$
\boxed{
v_5(v_0)=2,3,3,2
\quad\text{at }n=15,30,105,210.
}
\tag{2.11}
$$


No uniform value $2$ is assumed on that branch.

The fixed-$d$ whole-error expansion is reused at the scope reviewed in A4 Turn 10. The separate A1 and A5 results, including finite high-shift computations, do not establish an A3 reconstruction theorem.

---

## 3. Exact separation of the homogeneous initial value

This section supplies the main structural result about the high digits.

### 3.1 The homogeneous solution is exactly the first force

Write


$$
\mathscr H(z)=\frac{e^z+f(z)}{1-z},
\qquad f(0)=0,\quad f'(z)=\frac2{Q(z)},
$$


and


$$
A_n(z)=Q(z)^n\mathscr H^{(n)}(z).
$$


The complete differential equation is


$$
\mathscr L_n A_n=e^zQ^{n+1}+2R_n,
\tag{3.1}
$$


where


$$
\mathscr L_n A
=(1-z)QA'
-\bigl[n(1-z)Q'+(n+1)Q\bigr]A
$$


and


$$
R_n=Q^{n+1}(1/Q)^{(n)}.
$$



Define


$$
\mathcal Z_n(z)=\frac{n!Q(z)^n}{(1-z)^{n+1}}.
\tag{3.2}
$$


Direct logarithmic differentiation gives


$$
\mathscr L_n\mathcal Z_n=0.
\tag{3.3}
$$


Moreover,


$$
(n+i)![z^{n+i}]\mathcal Z_n=z_i.
\tag{3.4}
$$



Since


$$
A_n(0)=\mathcal W_n=n!\eta_n,\qquad
\mathcal Z_n(0)=n!,
$$


the function


$$
A_n^{\mathrm{flat}}=A_n-\eta_n\mathcal Z_n
\tag{3.5}
$$


has zero constant term and satisfies the **same complete forced equation** (3.1).

Thus the complete scalar recurrence can be run with initial value zero, without altering either forcing term. If $w^{\mathrm{flat}}$ denotes its three contact coefficients, then


$$
\boxed{
w=w^{\mathrm{flat}}+\eta_n z.
}
\tag{3.6}
$$



This identity is exact over $\mathbb Q$. It is not an omission of the exponential or logarithmic force.

### 3.2 Endpoint shifts and invariance of the endpoint-difference denominator

Use the factorial-stripped determinants


$$
\Delta=\det C,
$$




$$
X=-s_n^T\operatorname{adj}(C)\bar z,\qquad
Z=e_2^T\operatorname{adj}(C)\bar z,
$$




$$
Y=\Delta-s_n^T\operatorname{adj}(C)w,\qquad
R=e_2^T\operatorname{adj}(C)w.
\tag{3.7}
$$


Then, with $f_n=(n!)^2$,


$$
u_0=f_nX/\Delta,\quad u_3=f_nZ/\Delta,
\qquad
v_0=Y/\Delta,\quad v_3=R/\Delta.
$$



Define $Y^{\mathrm{flat}},R^{\mathrm{flat}}$ by replacing $w$ with $w^{\mathrm{flat}}$, while retaining the $\Delta$ term in $Y^{\mathrm{flat}}$. Equation (3.6) gives


$$
Y=Y^{\mathrm{flat}}+\eta_nf_nX,
\qquad
R=R^{\mathrm{flat}}+\eta_nf_nZ.
\tag{3.8}
$$


Consequently,


$$
\boxed{
\mathscr D_n:=XR-ZY
=XR^{\mathrm{flat}}-ZY^{\mathrm{flat}}.
}
\tag{3.9}
$$



The homogeneous scalar changes both rational centers by the same amount. Their difference, and the displayed determinant governing it, do not change.

At the eligible primes, $X,Z,R,\Delta$ are units and $Y$ is divisible by $p$, so $\mathscr D_n$ is a unit. Set


$$
\mathfrak u_n=\frac{XZ}{\mathscr D_n},
\qquad
\Theta^{\mathrm{flat}}
=\frac{XR^{\mathrm{flat}}}{\mathscr D_n}.
\tag{3.10}
$$


Then


$$
\boxed{
\Theta=\Theta^{\mathrm{flat}}+f_n\eta_n\mathfrak u_n.
}
\tag{3.11}
$$



Finally,


$$
\eta_n=\frac{F(n)}{n!}+\ell_n,
\quad
F(n)=\sum_{t=0}^{n}n^{\underline t},
\quad
\ell_n=\sum_{r=1}^{n}\frac{2\alpha_{r-1}}r,
$$


so (3.11) proves


$$
\boxed{
\Theta
=\Theta^{\mathrm{flat}}
+n!\mathfrak u_n\bigl(F(n)+n!\ell_n\bigr).
}
\tag{3.12}
$$



This separates the actual higher reconstruction into a forced contact quantity and one shifted-factorial scalar.

---

## 4. The middle-depth digit is nonzero

### Theorem 4.1 — Exact factorial-depth entry of the initial value

Let $p\in\{3,5,7\}$ be eligible, $p\mid n$, and suppose


$$
N_p:=v_p(n!)>\lfloor\log_p n\rfloor.
\tag{4.1}
$$


Then


$$
\boxed{
v_p(\Theta-\Theta^{\mathrm{flat}})=N_p.
}
\tag{4.2}
$$


More precisely,


$$
\boxed{
\frac{\Theta-\Theta^{\mathrm{flat}}}{n!}
\equiv\frac{\tau_n}{2}\pmod p.
}
\tag{4.3}
$$



Both original families (2.1)–(2.2), and all four supplied finite indices, satisfy (4.1).

### Proof

The factorial polynomial satisfies


$$
F(n)=nF(n-1)+1.
$$


Since $p\mid n$,


$$
F(n)\equiv1\pmod p.
\tag{4.4}
$$


Also


$$
v_p(\ell_n)\ge-\lfloor\log_p n\rfloor.
$$


Thus (4.1) implies


$$
F(n)+n!\ell_n\equiv1\pmod p.
\tag{4.5}
$$


Since $\mathfrak u_n$ is a unit, (3.12) proves (4.2).

For the normalized digit, the accepted first-force calculation gives


$$
X/\Delta\equiv-\tau_n,\qquad
Z/\Delta\equiv\tau_n/2\pmod p.
$$


Meanwhile,


$$
R/\Delta\equiv1,\qquad Y/\Delta\equiv0\pmod p.
$$


Therefore


$$
\mathfrak u_n
=\frac{XZ}{XR-ZY}
\equiv \frac{Z}{\Delta}
\equiv\frac{\tau_n}{2}\pmod p.
$$


Together with (3.12) and (4.5), this proves (4.3). ∎

### Higher digits before the final logarithmic strip

The same proof gives a deeper congruence:


$$
\boxed{
\frac{\Theta-\Theta^{\mathrm{flat}}}{n!}
\equiv \mathfrak u_nF(n)
\pmod{p^{\,N_p-\lfloor\log_p n\rfloor}}.
}
\tag{4.6}
$$



Thus essentially the entire second half of the factorial precision is controlled by the exact factorial polynomial $F(n)$, multiplied by a contact unit. The logarithmic prefix must still be restored for its final digits.

The first normalized digit is not a conjectural “random digit.” It is explicitly forced by $\tau_n$.

---

## 5. An infinite obstruction to incomplete higher reconstruction

The preceding theorem gives an actual denominator consequence.

### 5.1 Reconstructing the zero-initial-value residue

Suppose $p\nmid k$ and


$$
v_p(a-k\Theta^{\mathrm{flat}})>N_p.
\tag{5.1}
$$


By Theorem 4.1,


$$
v_p\!\left(k(\Theta-\Theta^{\mathrm{flat}})\right)=N_p.
$$


Hence


$$
\boxed{
v_p(a-k\Theta)=N_p.
}
\tag{5.2}
$$


The actual local primitive-denominator formula therefore gives


$$
\boxed{
v_p(q_\lambda)=2N_p-N_p=N_p.
}
\tag{5.3}
$$



This is a full-gcd conclusion for the **complete actual center**. It is not a denominator computed from the auxiliary flat force.

On $n=15^r$, $r\ge2$, the actual resonance orders are $w_3=r$, $w_5=r+1$, and $N_p>w_p$. Consequently, under (5.1),


$$
v_p(a-k)=w_p,
$$




$$
\boxed{
v_p(F_{\rm gcd})=w_p,\qquad
v_p(G)=0,\qquad
v_p(H_{\rm gcd})=N_p-w_p,
}
\tag{5.4}
$$


and the remaining denominator exponent is exactly $N_p$. The same statement holds at $7$ on $n=105^r$.

Thus a deep reconstruction of the flat residue achieves only half-factorial cancellation in the actual denominator.

### 5.2 Keeping only the leading homogeneous scalar

A slightly less severe shortcut is


$$
\Theta^{[1]}
:=\Theta^{\mathrm{flat}}+n!\mathfrak u_n.
\tag{5.5}
$$


Its error is


$$
\Theta-\Theta^{[1]}
=n!\mathfrak u_n\bigl(F(n)-1+n!\ell_n\bigr).
\tag{5.6}
$$



Let $s=v_p(n)$. The elementary falling-factorial expansion gives


$$
F(n)-1\equiv n\mathfrak D_p\pmod{p^{2s}}.
\tag{5.7}
$$


Indeed,


$$
n^{\underline t}
=(-1)^{t-1}(t-1)!\,n+n^2P_t(n),
\qquad P_t\in\mathbb Z[n],
$$


and the omitted factorial tail is sufficiently divisible.

Since


$$
\mathfrak D_3\equiv2\pmod3,\qquad
\mathfrak D_7\equiv4\pmod7,\qquad
v_5(\mathfrak D_5)=1,
$$


equation (5.7) implies, on the smooth families with $r\ge2$,


$$
v_3(F(n)-1)=r,\qquad
v_7(F(n)-1)=r,\qquad
v_5(F(n)-1)=r+1.
\tag{5.8}
$$


The logarithmic term in (5.6) has strictly higher valuation. Therefore


$$
\boxed{
v_p(\Theta-\Theta^{[1]})=N_p+w_p.
}
\tag{5.9}
$$



If a weight reconstructs $\Theta^{[1]}$ to depth exceeding $N_p+w_p$, then


$$
\boxed{
v_p(q_\lambda)=N_p-w_p,
\qquad
v_p(H_{\rm gcd})=N_p.
}
\tag{5.10}
$$



### Meaning and limitation

The improvement from $\Theta^{\mathrm{flat}}$ to $\Theta^{[1]}$ buys only $w_p=O(\log n)$ further digits. It does not recover the missing half of the factorial precision.

These are genuine infinite exclusions of specified simplified reconstruction targets at an exponential scale. They are **not** exclusions of reconstruction of the correct $\Theta$.

Nor do (5.3) or (5.10), by themselves, prove divergence of the whole primitive forms. For the selected sets,


$$
\frac12\left(\log3+\frac12\log5\right)<2\log(1+\sqrt2),
$$


and


$$
\frac12\left(\log3+\frac12\log5+\frac13\log7\right)
<2\log(1+\sqrt2).
$$


The surviving half-factorial selected denominator is below the analytic exponential rate. The unselected denominator and the whole error still matter.

---

## 6. Restoring the logarithmic force changes the selected denominator only polynomially

This is the second main theorem. It clarifies which part of the high-digit problem is essential at the exponential-budget scale.

Let $w^{\exp}$ be the complete exponential contribution to the force. Define


$$
Y^{\exp}=\Delta-s_n^T\operatorname{adj}(C)w^{\exp},
\qquad
R^{\exp}=e_2^T\operatorname{adj}(C)w^{\exp},
$$


and


$$
\Theta^{\exp}
=\frac{XR^{\exp}}{XR^{\exp}-ZY^{\exp}}.
\tag{6.1}
$$


The exterior $+1$, represented by $\Delta$, is retained.

Write


$$
m_p=2v_p(n!),\qquad
d_p=\lfloor\log_p(2n+2)\rfloor,\qquad
K_p=m_p-d_p.
$$



### 6.1 Complete-force precision

Each logarithmic summand in the $i$-th force has the form


$$
2q_j(n+i)!\,n!
\binom{2n+i-j}{n}\frac{\alpha_{r-1}}r.
\tag{6.2}
$$


Here $r\le2n+2$, and, since $i<p$ and $p\mid n$,


$$
v_p((n+i)!)=v_p(n!).
$$


All other displayed factors apart from $1/r$ are $p$-integral. Therefore


$$
w-w^{\exp}\in p^{K_p}\mathbb Z_{(p)}^3.
\tag{6.3}
$$


As $C^{-1}$ is $p$-integral and the relevant residue denominators are units,


$$
\boxed{
\Theta-\Theta^{\exp}\in p^{K_p}\mathbb Z_{(p)}.
}
\tag{6.4}
$$



The complete force has not been discarded: (6.4) specifies exactly where its remaining digits can act.

### Theorem 6.1 — Uniform polynomial distortion of the selected denominator

For a reduced weight $a/k$, let $q_\lambda$ denote the actual complete primitive denominator. Let $q_\lambda^{\exp}$ denote the reduced denominator obtained from the auxiliary exponential-only center, with the same first column and the exterior $+1$.

Then


$$
\boxed{
\left|v_p(q_\lambda)-v_p(q_\lambda^{\exp})\right|
\le d_p.
}
\tag{6.5}
$$


Consequently, for either fixed selected set,


$$
\boxed{
B_{\mathcal P}(n)^{-1}
\le
\frac{(q_\lambda)_{\mathcal P}}
     {(q_\lambda^{\exp})_{\mathcal P}}
\le
B_{\mathcal P}(n),
\quad
B_{\mathcal P}(n)=\prod_{p\in\mathcal P}p^{d_p}
\le(2n+2)^{|\mathcal P|}.
}
\tag{6.6}
$$



### Proof

If $p\mid k$, both complete and exponential-only companions satisfy the accepted local hypotheses, and


$$
v_p(q_\lambda)=v_p(q_\lambda^{\exp})=m_p+v_p(k).
$$



Suppose $p\nmid k$. Set


$$
\nu=v_p(a-k\Theta),\qquad
\nu_{\exp}=v_p(a-k\Theta^{\exp}).
$$


By (6.4), either:

* both valuations are equal and less than $K_p$; or
* both are at least $K_p$.

Thus


$$
\left|\min(m_p,\nu)-\min(m_p,\nu_{\exp})\right|
\le m_p-K_p=d_p.
$$


The actual local denominator formulas are


$$
v_p(q_\lambda)=m_p-\min(m_p,\nu),
$$




$$
v_p(q_\lambda^{\exp})=m_p-\min(m_p,\nu_{\exp}).
$$


This proves (6.5), and multiplication proves (6.6). ∎

### 6.2 Consequences for the reconstruction target

If


$$
a\equiv k\Theta^{\exp}\pmod{p^{K_p}},
$$


then the same weight satisfies


$$
a\equiv k\Theta\pmod{p^{K_p}},
$$


and its actual selected denominator obeys


$$
\boxed{
(q_\lambda)_{\mathcal P}\le B_{\mathcal P}(n).
}
\tag{6.7}
$$



Therefore:

* a short reconstruction through the near-factorial strip already removes all but polynomially many selected factorial factors;
* restoring the final logarithmic strip can change exact full cancellation, but not the selected exponential cancellation rate;
* there is no need to alter the weight merely to retain that exponential rate.

This is not a global bound on $q_\lambda$. Primes outside $\mathcal P$, the coefficient denominator, and all remaining endpoint factors still require the full primitive reduction.

In particular, the final logarithmic strip remains essential for exact arithmetic and exact gcd output. It is no longer an independent obstacle to an **exponential selected-prime budget**.

---

## 7. A terminal contact identity and the resulting nested reconstruction problem

### 7.1 Exact terminal relation

The complete recurrence is


$$
\begin{aligned}
a_{N+1}^{(n)}
={}&(2N+1)a_N^{(n)}
+\frac{N(2n+1-3N)}2a_{N-1}^{(n)}\\
&+\frac{N(N-1)(N-n-1)}2a_{N-2}^{(n)}
+\mathcal B_N^{[n+1]}+2N![z^N]R_n.
\end{aligned}
\tag{7.1}
$$


At $N=n+1$,

* the coefficient of $a_{n-1}^{(n)}$ is zero;
* $R_n$ has degree $n$, so its coefficient is zero.

Since $w_i=a_{n+i}^{(n)}$, one obtains


$$
\boxed{
w_2-(2n+3)w_1+\frac{(n+1)(n+2)}2w_0
=\mathcal B_{n+1}^{[n+1]}.
}
\tag{7.2}
$$


Also


$$
\mathcal B_{n+1}^{[n+1]}
=
\mathcal B_{n+1}
-(n+1)\mathcal B_n
+\frac{n(n+1)}2\mathcal B_{n-1}.
\tag{7.3}
$$



Let


$$
\ell_n^{\,T}
=\left(\frac{(n+1)(n+2)}2,\,-(2n+3),\,1\right).
$$


Then


$$
\boxed{
\ell_n^Tz=0,\qquad
\ell_n^Tw^{\log}=0,\qquad
\ell_n^Tw^{\mathrm{flat}}=\mathcal B_{n+1}^{[n+1]}.
}
\tag{7.4}
$$



These are exact finite-boundary identities. In particular, the logarithmic force occupies the same terminal plane as the homogeneous first force. This does not make it proportional to the first force, and it does not justify deleting it.

### 7.2 A two-stage reconstruction problem

Apply the homogeneous decomposition to the exponential-only force. Denote the resulting quantities by


$$
\Theta^{\exp,\mathrm{flat}},
\qquad
\mathfrak u_n^{\exp}.
$$


There is now no logarithmic prefix, so


$$
\boxed{
\Theta^{\exp}
=\Theta^{\exp,\mathrm{flat}}
+n!\mathfrak u_n^{\exp}F(n)
}
\tag{7.5}
$$


exactly.

For each selected prime, reconstruction through $K_p=2N_p-d_p$ is therefore equivalent to


$$
a-k\Theta^{\exp,\mathrm{flat}}
-k n!\mathfrak u_n^{\exp}F(n)
\equiv0\pmod{p^{2N_p-d_p}}.
\tag{7.6}
$$



Because the second term has valuation $N_p$, this separates into:

1. the lower-half condition
   

$$
\boxed{
   a-k\Theta^{\exp,\mathrm{flat}}\equiv0\pmod{p^{N_p}};
   }
   \tag{7.7}
$$



2. after that exact division, the upper-half condition
   

$$
\boxed{
   \frac{a-k\Theta^{\exp,\mathrm{flat}}}
        {k n!\mathfrak u_n^{\exp}}
   \equiv F(n)\pmod{p^{N_p-d_p}}.
   }
   \tag{7.8}
$$



The quotient in (7.8) is formed only after (7.7) has made it $p$-integral. No nonunit modular inverse is taken prematurely.

This is a concrete higher-reconstruction problem. The upper-half target is the exact shifted-factorial polynomial satisfying


$$
F(0)=1,\qquad F(j)=jF(j-1)+1.
\tag{7.9}
$$


A leading-value replacement $F(n)\mapsto1$ fails by the exact factorial-depth obstruction in Section 5.

### What this does not prove

The decomposition does not show that a short weight satisfying both stages exists. Nor does it supply a short dual vector excluding it.

The difficult information is not merely the valuation of $v_0$, nor the first digit of $\Theta-1$. It is the simultaneous archimedean and modular behavior of the actual pair


$$
\left(\Theta^{\exp,\mathrm{flat}},
      \mathfrak u_n^{\exp}F(n)\right)
$$


through precision proportional to $n$.

Classical shifted-factorial, binomial, or orthogonal-polynomial identities establish the identities above; they do not automatically provide a height theorem for that moving pair.

---

## 8. Full primitive normalization and whole evaluated error

### 8.1 The actual full gcd is unchanged

Let $d_B$ be the least common denominator of the full reconstructed columns. Form


$$
U=d_Bu,\qquad V=d_Bv,
$$


reduce both endpoint rows, and write


$$
\widetilde u_0=hA,\qquad
\widetilde u_3=hB,\qquad
\gcd(A,B)=1.
$$


Put


$$
J=B\widetilde v_0-A\widetilde v_3,
\qquad
\mathcal V=A\widetilde v_3,
\qquad
T=aJ+k\mathcal V.
$$


For $\gcd(a,k)=1$, $k>0$,


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


The actual primitive pair remains


$$
\boxed{
q_\lambda=\frac{kh|AB|}{F_{\rm gcd}GH_{\rm gcd}},
\qquad
p_\lambda=
\operatorname{sgn}(AB)
\frac{T}{F_{\rm gcd}GH_{\rm gcd}}.
}
\tag{8.1}
$$



The auxiliary flat and exponential decompositions do not replace $d_B$, the row contents, or this final gcd.

### 8.2 Whole same-index error

The retained exact whole-error identity is


$$
\boxed{
q_\lambda S-p_\lambda
=q_\lambda e_3\alpha_{n,2}
(\lambda-\Lambda_{n,2}),
}
\tag{8.2}
$$


where


$$
\Lambda_{n,2}
=\frac{n^2}{2}
+\frac{1-3\sqrt2}{2}n+O(1),
$$




$$
e_3=(-1)^{n+1}4\pi M^{-2n-3}(1+O(n^{-1})),
\qquad
\alpha_{n,2}=\frac2{n^2}(1+O(n^{-1})).
\tag{8.3}
$$


These are whole-error quantities, including the complete factorial residual and the exterior endpoint contribution.

Consequently, even a successful reconstruction from Section 7 must still establish


$$
\boxed{
0<
q_\lambda|e_3\alpha_{n,2}|
\,|\lambda-\Lambda_{n,2}|
\longrightarrow0.
}
\tag{8.4}
$$



Three separate issues remain:

1. the weight must be short enough;
2. the **entire** primitive denominator must be favorable;
3. the distance to the actual threshold must be nonzero and sufficiently controlled.

Theorem 6.1 resolves none of the unselected-prime denominator factors. A finite-order threshold expansion does not supply nonvanishing for an exceptionally close candidate.

---

## 9. A sharpened follow-on lemma

The next arithmetic target can now be stated without requiring exact full logarithmic cancellation at the outset.

### Proposed higher-reconstruction lemma

On


$$
n=15^r,\qquad r\ge2,
$$


set


$$
L_{\rm strip}
=3^{2v_3(n!)-\lfloor\log_3(2n+2)\rfloor}
 5^{2v_5(n!)-\lfloor\log_5(2n+2)\rfloor}.
$$


Determine whether there are infinitely many reduced weights $a/k$ satisfying


$$
\left|\frac ak-
\left(\frac{n^2}{2}+\frac{1-3\sqrt2}{2}n\right)\right|
\le C,
$$




$$
\log\max(|a|,k)=o(n),
$$


and the two-stage actual congruences (7.7)–(7.8).

Either of the following would constitute a substantial next theorem:

* **Constructive direction:** an explicit short solution family, followed by its full actual gcd and whole-error analysis;
* **Exclusion direction:** an actual dual vector for the residue in (7.5), with a proved archimedean bound strong enough to exclude the specified height range.

The logarithmic force must then be restored for the exact denominator. Theorem 6.1 guarantees that this restoration changes the selected-prime budget only polynomially.

The present obstruction shows why replacing $F(n)$ by $1$, or discarding the homogeneous initial value, does not prove this lemma: those substitutions lose a positive proportion of the factorial precision.

---

## 10. Bounded exact arithmetic for personal inspection

No additional weight enumeration or $n^3$-window search is requested. The coordinator’s scheduled four-index recurrence/residue calculation can check the new statements using the same arrays.

### 10.1 Inputs

Use only


$$
n=15,30,105,210,\qquad d=2,
$$


with the already retained complete force, original contact matrix, least clearer, and full reconstructed columns.

In addition to the actual recurrence, run the **same forced recurrence with initial value zero**, obtaining $w^{\mathrm{flat}}$.

### 10.2 Expected exact identities

For each input, verify:

1. **Homogeneous-force separation**
   

$$
w-w^{\mathrm{flat}}-\eta_n z=0.
$$



2. **Terminal boundary identity**
   

$$
\ell_n^Tw-\mathcal B_{n+1}^{[n+1]}=0,
   \quad
   \ell_n^Tz=0,
   \quad
   \ell_n^Tw^{\log}=0.
$$



3. **Invariant endpoint-difference determinant**
   

$$
XR-ZY
   =XR^{\mathrm{flat}}-ZY^{\mathrm{flat}}.
$$



4. **Exact residue decomposition**
   

$$
\Theta-\Theta^{\mathrm{flat}}
   =n!\mathfrak u_n(F(n)+n!\ell_n).
$$



These are rational equalities; the expected residual is exactly zero.

### 10.3 Predicted middle-depth outputs

The theorem predicts the following exact valuations and normalized residues:


$$
\begin{array}{c|c|c|c}
n&p&
v_p(\Theta-\Theta^{\mathrm{flat}})
&
(\Theta-\Theta^{\mathrm{flat}})/n!\pmod p\\ \hline
15&3&6&1\\
15&5&3&2\\
30&3&14&2\\
30&5&7&3\\
105&3&50&2\\
105&5&25&3\\
105&7&17&1\\
210&3&102&2\\
210&5&51&4\\
210&7&34&5
\end{array}
\tag{10.1}
$$


The last column follows from the accepted digit product for $\tau_n$, followed by division by $2$ modulo $p$.

These outputs do not depend on guessing the $v_5(n)=1$ endpoint valuation. The supplied actual values $2,3,3,2$ remain unchanged.

### 10.4 Denominator-budget check without new enumeration

For any weights already produced by the scheduled finite search, compare the actual complete denominator with the reduced exponential-only denominator and verify


$$
\left|v_p(q_\lambda)-v_p(q_\lambda^{\exp})\right|
\le\lfloor\log_p(2n+2)\rfloor.
\tag{10.2}
$$


Return the full actual $F_{\rm gcd},G,H_{\rm gcd},p_\lambda,q_\lambda$, not merely the selected-prime comparison.

Any whole-error interval must still be computed from the complete center and $e+\pi$. These finite checks establish only their stated inputs.

---

## 11. Final proof ledger and exact bottleneck

### New results established in this report

* An exact affine decomposition of the **actual** resonance into a zero-initial-value forced part and a homogeneous factorial scalar.
* Invariance of the endpoint-difference determinant under that homogeneous separation.
* An explicit, nonzero digit at depth $v_p(n!)$, halfway through the full factorial precision.
* Infinite full-gcd obstructions to reconstructing the flat residue or retaining only the leading homogeneous scalar.
* A uniform polynomial bound for the distortion of the selected-prime denominator when the complete logarithmic force is restored.
* An exact terminal contact-plane identity.
* A division-safe two-stage formulation of the remaining higher reconstruction.

### What is not established

There is no proof that the correct threshold window contains, or excludes, subexponential-height solutions of the complete reconstruction problem. No sufficiently small actual full primitive denominator has been proved for such a family. No new same-index family of nonzero whole primitive forms tending to zero has been constructed.

### The precise remaining bottleneck

The remaining exponential-budget arithmetic is now the following actual moving-residue problem:


$$
\boxed{
\begin{gathered}
a-k\Theta^{\exp,\mathrm{flat}}
-k n!\mathfrak u_n^{\exp}F(n)
\equiv0\pmod{L_{\rm strip}},\\
\left|\frac ak-
\left(\frac{n^2}{2}+\frac{1-3\sqrt2}{2}n\right)\right|=O(1),\\
\log\max(|a|,k)=o(n),
\end{gathered}
}
$$


on a specified original smooth family.

The complete logarithmic force is still required for exact final digits and exact primitive reduction, but it cannot change the selected cancellation rate exponentially. The missing theorem is an infinite-family height estimate for the **actual forced contact residue coupled to the shifted-factorial scalar**, not another uniqueness statement and not another first-digit valuation.

Even after that arithmetic theorem, the full all-prime denominator and the whole nonzero error must satisfy (8.4).



$$
\boxed{\text{The irrationality or rationality of }e+\pi\text{ remains unresolved.}}
$$


