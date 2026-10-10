> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The truncated Hahn operator and the complete three-column channel

## Abstract and proof status

The supplied work does not establish either rationality or irrationality of $e+\pi$. This report does not resolve that problem.

The overlap correction is accepted in full. The complete source recurrence, the vanishing of its logarithmic interior forcing, first-force homogeneity, the shifted-moment displacement, the rank-$(b-2)$ theorem, the three-dimensional reduction, and the reduced adjoint force channel are established results of the earlier report. They are not new results of Turn 7. The recovered entrywise definition also identifies the moment producer with the actual matrix $A$; the former documentary qualification is withdrawn.

The new calculation here is an explicit formula for the **finite Hahn defect on all three complete columns**, including the lower boundary and the nonzero upper return. It separates two different finite operators that must not be conflated:

* the reflecting finite operator on $0,\ldots,b$;
* the restriction of the full-support Hahn operator, which requires an additional value at $b+1$.

The calculation gives a precise test for invariance of the original kernel. It does **not** evaluate that test or prove that it fails for the original moments. Accordingly, no complete-source obstruction, primitive norm digit, bound for $\nu$, or new factor in the final gcd is claimed.

This is therefore a partial report rather than a completed solution of the assignment’s accepting-value requirement. Its main useful output is the boundary-correct defect formula and a sharper adjoint compatibility condition. The unresolved evaluation is stated explicitly below.

---

## 1. Original objects and results reused

Throughout, retain exactly


$$
p=29,\qquad
b=3^{249005515+574312172u},\qquad
n=2001b,\qquad
u\ge0,\quad u\equiv2\pmod{29^9},
$$


and put


$$
N=n+2,\qquad W_j=\binom Nj,\qquad w_j=W_j^2.
$$



The domains are unchanged:


$$
0\le j<b\quad\text{for contact coordinates},\qquad
1\le i\le b-2\quad\text{for source recurrence rows},
$$


and


$$
0\le j\le b\quad\text{for reconstructed coordinates}.
$$



Let $C$ denote the unweighted reconstruction:


$$
(Cv)_j=jv_{j-1}-v_j,\qquad v_{-1}=v_b=0,
$$


so that


$$
\mathcal R=\operatorname{diag}(W_j)C.
$$



The actual extended matrix is


$$
A_{\mathrm{ext}}(i,j)
=\sum_s a_s(n)(n+i)_{\underline s}
  \binom{2n+i-s}{j},
\qquad
a_s(n)=[z^s]\left(1-z+\frac{z^2}{2}\right)^n.
$$


The square matrix $A$ is its original $b\times b$ interior restriction.

The complete sources remain


$$
f_i^0=\frac{(n+i)!}{n!}
[z^n](1+2z+2z^2)^n(1+z)^i
$$


and


$$
r_i=\sum_s a_s(n)(n+i)_{\underline s}
\left(T_{2n+i-s}+\frac{L_{2n+i-s}}{b!}\right).
$$


Here


$$
T_m=\frac1{b!}\sum_{q=b}^m(m)_{\underline q},
\qquad
L_0=0,\quad
L_m=mL_{m-1}+2(m-1)![z^{m-1}]\phi(z)^{-1}.
$$


Thus both logarithmic initial charges and every factorial source row are retained.

I reuse, without rederivation,


$$
\mathcal Df^0=0,\qquad \mathcal D r=\mathcal H,
\qquad
\mathcal DA=-\mathcal VC,\qquad
\mathcal H=\mathcal Ve_b.
$$


The rectangular matrix is


$$
\mathcal V_{ik}
=[x^k]\left\{
(1+x)^{n+1}\phi(D)^{n+1}(1+x)^{n+i}
\right\},
\quad
1\le i\le b-2,\quad 0\le k\le b.
$$



In particular,


$$
K:=\ker\mathcal V
$$


has dimension three over $\mathbb Q$, and the following are its actual unweighted basis columns:


$$
k_0=CA^{-1}h^{(0)},\qquad
k_1=CA^{-1}h^{(1)},\qquad
k_*=CA^{-1}\tau+e_b.
$$


Here


$$
\mathcal Dh^{(r)}=0,\qquad
(h^{(0)}_0,h^{(0)}_1)=(1,0),\quad
(h^{(1)}_0,h^{(1)}_1)=(0,1),
$$


and


$$
\mathcal D\tau=\mathcal H,\qquad \tau_0=\tau_1=0.
$$



The complete reconstructed columns are exactly


$$
Z_w=\operatorname{diag}(W_j)
       (f_0^0k_0+f_1^0k_1),
$$




$$
Y=\operatorname{diag}(W_j)
       (r_0k_0+r_1k_1+k_*).
$$


No saturation of this basis in the weighted integral lattice is assumed.

---

## 2. Which Hahn operator acts on the original finite space?

The classical parameters are


$$
\alpha=\beta=-N-1.
$$


For degrees $0,\ldots,N$, these lie in the supplied negative-parameter Hahn range. The corresponding full-support weight is, up to a common sign, $\binom Nj^2$. This is a statement on $0,\ldots,N$, not an orthogonality theorem on the original interval $0,\ldots,b$.

Write


$$
a_j=(N-j)^2,\qquad c_j=j^2.
$$


The elementary balance identity is


$$
w_ja_j=w_{j+1}c_{j+1}.
\tag{2.1}
$$



### 2.1 The reflecting finite operator

A well-defined operator on vectors indexed only by $0,\ldots,b$ is


$$
(L_bv)_0=a_0(v_1-v_0),
$$




$$
(L_bv)_j=a_j(v_{j+1}-v_j)+c_j(v_{j-1}-v_j),
\quad 1\le j<b,
$$




$$
(L_bv)_b=c_b(v_{b-1}-v_b).
\tag{2.2}
$$



The last row is a reflecting boundary. It is not the full Hahn last row at $j=b$.

From (2.1), direct pairing of adjacent edges gives


$$
\langle u,L_bv\rangle_w
=
-\sum_{j=0}^{b-1}w_ja_j
(u_{j+1}-u_j)(v_{j+1}-v_j),
\tag{2.3}
$$


where


$$
\langle u,v\rangle_w=\sum_{j=0}^bw_ju_jv_j.
$$


Thus $L_b$ is self-adjoint for the actual truncated weight.

### 2.2 Restriction of the full operator

If a vector is extended to $b+1$, the full Hahn expression instead gives


$$
(\widehat Lv)_b=(L_bv)_b+a_b(v_{b+1}-v_b).
$$


Consequently,


$$
\begin{aligned}
&\sum_{j=0}^bw_j
\bigl(u_j(\widehat Lv)_j-(\widehat Lu)_jv_j\bigr)\\
&\qquad=
w_ba_b(u_bv_{b+1}-u_{b+1}v_b).
\end{aligned}
\tag{2.4}
$$



There is no lower return: $c_0=0$. The upper return coefficient is the explicitly evaluated positive integer


$$
\boxed{
w_ba_b
=\binom Nb^2(N-b)^2
=(b+1)^2\binom N{b+1}^2>0.
}
\tag{2.5}
$$


On the original family,


$$
N-b=2000b+2>0.
$$



The physical reconstruction at $j=b$ does not specify a value at $b+1$. Hence an argument using $\widehat L$ must supply and justify an extension rule. Setting its return to zero without such a rule changes the problem.

Equation (2.5) evaluates a boundary coefficient, not an actual norm or accepting value.

---

## 3. Exact finite defect on the complete moment rows

Define


$$
F=\mathcal V L_b.
$$


The following formulas compute every entry of $F$, with neither boundary suppressed.

For $1\le i\le b-2$,


$$
\boxed{
F_{i0}=\mathcal V_{i1}-N^2\mathcal V_{i0},
}
\tag{3.1}
$$


and, for $1\le k<b$,


$$
\boxed{
F_{ik}
=(N-k+1)^2\mathcal V_{i,k-1}
+(k+1)^2\mathcal V_{i,k+1}
-\bigl((N-k)^2+k^2\bigr)\mathcal V_{ik}.
}
\tag{3.2}
$$


At the upper boundary,


$$
\boxed{
F_{ib}
=(N-b+1)^2\mathcal V_{i,b-1}
-b^2\mathcal V_{ib}.
}
\tag{3.3}
$$



These follow simply by multiplying a row of $\mathcal V$ by the tridiagonal matrix (2.2). In particular, (3.3) differs from the interior formula.

### 3.1 Polynomial form, including the discarded exterior coefficient

Let


$$
P_i(t)=\sum_{k\ge0}\mathcal V^{\mathrm{ext}}_{ik}t^k
=(1+t)^{n+1}\phi(D)^{n+1}(1+t)^{n+i}
$$


and $E=t\,d/dt$. Define the polynomial operator


$$
\mathscr T_N
=t(N-E)^2+t^{-1}E^2-(N-E)^2-E^2.
\tag{3.4}
$$


The term $t^{-1}E^2P_i$ is polynomial because $E^2$ kills the constant term.

For interior coefficients, (3.4) is exactly (3.1)–(3.2). The original finite row is therefore


$$
\boxed{
\sum_{k=0}^bF_{ik}t^k
=
[\mathscr T_NP_i]_{\le b}
+
\left(
(N-b)^2\mathcal V_{ib}
-(b+1)^2\mathcal V^{\mathrm{ext}}_{i,b+1}
\right)t^b.
}
\tag{3.5}
$$



The last parenthesis is important. It contains both:

* the correction from the full diagonal to the reflecting diagonal;
* the removal of the actual exterior moment coefficient at $b+1$.

Neither is an optional simplification.

---

## 4. Defect on the original three columns

The exact three-column defect matrix is


$$
\mathfrak F
=
\bigl[F k_0,\ F k_1,\ F k_*\bigr].
$$


Using the complete basis definitions gives


$$
\boxed{
\begin{aligned}
\mathfrak F_0&=FCA^{-1}h^{(0)},\\
\mathfrak F_1&=FCA^{-1}h^{(1)},\\
\mathfrak F_*&=FCA^{-1}\tau+Fe_b.
\end{aligned}
}
\tag{4.1}
$$


Its last explicit source term is


$$
\boxed{
(Fe_b)_i
=(N-b+1)^2\mathcal V_{i,b-1}-b^2\mathcal H_i.
}
\tag{4.2}
$$



Thus the actual first and second column defects are


$$
\mathcal V L_b
\bigl(\operatorname{diag}(W_j)^{-1}Z_w\bigr)
=f_0^0\mathfrak F_0+f_1^0\mathfrak F_1,
\tag{4.3}
$$




$$
\boxed{
\mathcal V L_b
\bigl(\operatorname{diag}(W_j)^{-1}Y\bigr)
=r_0\mathfrak F_0+r_1\mathfrak F_1+\mathfrak F_*.
}
\tag{4.4}
$$



The inverse weight notation in (4.3)–(4.4) is only shorthand for the already defined unweighted columns. It licenses no integral division by $W_j$.

In particular, the second defect contains the complete $r_0,r_1$, the complete solution $\tau$ driven by every $\mathcal H_i$, and the physical $e_b$ contribution (4.2).

### 4.1 Exact invariance criterion

Since $k_0,k_1,k_*$ form a basis of $K$,


$$
\boxed{
L_bK\subseteq K
\quad\Longleftrightarrow\quad
\mathfrak F_0=\mathfrak F_1=\mathfrak F_*=0.
}
\tag{4.5}
$$



Equivalently, because $\mathcal V$ has full row rank,


$$
L_bK\subseteq K
\quad\Longleftrightarrow\quad
\mathcal VL_b=M\mathcal V
$$


for some rational matrix $M$.

This is an exact criterion, not a proof of invariance. In particular, the known identity


$$
\mathcal DA=-\mathcal VC
$$


does not evaluate any of the three expressions in (4.1): the new factor $L_b$ occurs between $\mathcal V$ and the reconstructed columns.

**Open point.** I have not proved that (4.1) vanishes, nor exhibited a nonzero actual entry at the original indices. Consequently, it would be unjustified to announce either a closed Hahn reduction or a complete-source no-go theorem.

The fixed-parameter scalar antidifference obstruction from Turn 7 remains valid at its stated scope. It does not decide (4.5).

---

## 5. Consequence for the adjoint force route

The earlier adjoint reduction should therefore remain active rather than be replaced by an unproved Hahn closure.

Retain its actual saturated adjoint data


$$
A^Tz=\mathcal R^T\Pi d,
\qquad
z=\mathcal D^T\lambda+\eta_0e_0+\eta_1e_1.
$$


These are the original adjoint vector and backward recurrence, not a newly chosen eigenfunction.

The closed force identity is


$$
p^3\mathfrak v
=
\frac{r_0}{f_0^0}p^{c+2}\mathfrak b
+\mathcal E_{\mathrm{force}},
$$


where


$$
\mathcal E_{\mathrm{force}}
=
\eta_1\left(r_1-\frac{f_1^0}{f_0^0}r_0\right)
+\lambda^T\mathcal H
+W_b(\Pi d)_b.
\tag{5.1}
$$



Since $\mathcal H=\mathcal Ve_b$, define the complete adjoint boundary vector


$$
s=\operatorname{diag}(W_j)\Pi d+\mathcal V^T\lambda.
$$


Then


$$
\boxed{
\mathcal E_{\mathrm{force}}
=
\eta_1\left(r_1-\frac{f_1^0}{f_0^0}r_0\right)+s_b.
}
\tag{5.2}
$$


This is the earlier boundary reduction, not a new evaluated scalar.

The new finite defect identifies the compatibility required if Hahn machinery is used to calculate $s$. Indeed,


$$
L_b^T\mathcal V^T=(\mathcal VL_b)^T=F^T.
\tag{5.3}
$$


Thus any proposed closed Hahn evolution for $\mathcal V^T\lambda$ must account for $F^T\lambda$ with the upper correction in (3.5). The omitted exterior coefficient cannot be absorbed into a homogeneous adjoint evolution without proof.

### Concrete follow-on lemma

A useful next lemma is the following genuinely arithmetic statement:

> For the actual saturated adjoint data, evaluate $s_b$ modulo
> 

$$
> 29^{3+v_{29}(\mathfrak b)}
>
$$


> with all divisions paid, and prove
> 

$$
> s_b\equiv
> -\eta_1\left(r_1-\frac{f_1^0}{f_0^0}r_0\right)
> \pmod{29^{3+v_{29}(\mathfrak b)}}.
> \tag{5.4}
>
$$



This would establish the first reduced force obligation. It would still need the archived unit-scale congruence and the final normalization transfer.

Equation (5.4) is open. Merely rewriting $s_b$ as $\lambda^T\mathcal H+W_b(\Pi d)_b$ does not prove it.

---

## 6. Arithmetic payments and the all-prime budget

The defect calculation uses integer coefficients only. No Hahn eigenvalue, parameter pivot, or binomial weight has been inverted.

If a Hahn basis is subsequently used, every change-of-basis determinant and every spectral denominator must be retained. Full-support orthogonality supplies neither a saturated basis for the original weighted lattice nor the actual contents of its columns.

The actual final normalization remains


$$
N_B=d_B[u,v],
$$


where $d_B$ is the least simultaneous clearer, and


$$
A_B=N_{B,1}^T\Omega N_{B,1},\qquad
H_B=N_{B,1}^T\Omega N_{B,2}.
$$


Thus


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=\frac{A_B}{g_B},\qquad
p_n=\frac{H_B}{g_B}.
}
\tag{6.1}
$$


The primitive multiplier remains $d_B^2/g_B$.

Writing the actual weighted contents as


$$
\operatorname{diag}(\omega_j)N_{B,i}=k_iv_i
$$


with $v_i$ primitive, and setting


$$
S=v_1^Tv_1,\qquad T=v_1^Tv_2,
$$


gives, prime by prime,


$$
\boxed{
v_\ell(q_n)
=
\max\{v_\ell(k_1)-v_\ell(k_2)+v_\ell(S)-v_\ell(T),0\}.
}
\tag{6.2}
$$



The gcd in (6.1) is over all primes.

The established bound


$$
c+2\le\lfloor\log_{29}(n+2)\rfloor
$$


shows that a saving of only $29^{O(c)}$ contributes merely $O(\log n)$ to $\log q_n$. No bound of this kind has yet been proved for the whole primitive norm cancellation.

A concrete different mechanism would be **simultaneous factorial-content transfer across primes**: use the exact factors in


$$
f_i^0=i!\binom{n+i}{i}J_i
$$


and the complete exterior factorial source to prove lower bounds on


$$
v_\ell(k_2T)-v_\ell(k_1S)
$$


for a growing set of primes $\ell$, after restoring the actual clearer and both actual contents. The required aggregate statement is a weighted bound on the positive parts in (6.2), not merely divisibility of an unnormalized source.

This is a proposed arithmetic mechanism, not an established theorem. The limitation of a $29^{O(c)}$ saving is proved; impossibility of the producer is not.

---

## 7. Whole error and the unresolved global comparison

At the same original indices, retain


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi)
$$


and the whole evaluated error


$$
q_n(e+\pi)-p_n=-q_n\epsilon_n.
$$


Under the expressly retained signed whole-error theorem,


$$
\epsilon_n\ne0
\quad\text{eventually},\qquad
\log|\epsilon_n|=-\lambda n+o(n),
$$


where


$$
\lambda=\left(2+\frac1{2001}\right)\log(1+\sqrt2).
$$



An irrationality conclusion requires an infinite original subfamily on which


$$
0<|q_n\epsilon_n|\longrightarrow0.
$$


Neither a truncated Hahn identity nor a local congruence at unrelated indices suffices.

This report supplies no new estimate for $\log q_n$, so it supplies no improvement to that final comparison.

---

## 8. Bounded exact verification

No first-original matrix calculation and no repeated rank, low-row, or source audit is proposed.

A bounded symbolic check can verify the new defect formulas.

### Inputs

* An indeterminate $N$.
* An arbitrary polynomial
  

$$
P(t)=v_0+v_1t+\cdots+v_5t^5.
$$


* Cutoff $b=4$.
* The $5\times5$ reflecting matrix $L_4$ defined by (2.2).
* $E=t\,d/dt$ and $\mathscr T_N$ from (3.4).

### Expected exact output

The coefficient vector of


$$
[\mathscr T_NP]_{\le4}
+\bigl((N-4)^2v_4-25v_5\bigr)t^4
$$


must equal


$$
(v_0,v_1,v_2,v_3,v_4)L_4.
$$


The five polynomial differences should all be zero.

Separately, the two-variable edge calculation should verify (2.4), including the coefficient


$$
\binom Nb^2(N-b)^2.
$$



This calculation checks only the finite operator algebra. It does not decide original-kernel invariance or a primitive norm valuation. No bounded original-family accepting-value computation is justified here, because a compact evaluated representation of the actual defect or adjoint boundary state has not yet been established.

---

## Conclusion

The new proved result is the complete finite Hahn defect formula (3.1)–(3.5), together with its application (4.1)–(4.4) to all three original source columns. It records the physical terminal source and the nonzero upper Green return without replacing the original cutoff by $N$.

The exact remaining local bottleneck is to **evaluate** the three defects in (4.1), or, independently, to evaluate the actual adjoint boundary scalar $s_b$ sufficiently deeply to prove (5.4). This report does neither; it therefore does not claim the requested invariant relation, a complete-source obstruction, a norm digit, or a bound for $\nu$.

Beyond that local bottleneck lies the unchanged global obligation: restore the unsaturated lattice payments, actual contents, least simultaneous clearer, and all-prime gcd, and compare the resulting actual primitive denominator with the nonzero whole error on the same infinite original indices. Rationality or irrationality of $e+\pi$ remains unresolved.
