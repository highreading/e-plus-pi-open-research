> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, turn 12 — Audited factorial alignment and an original-family obstruction to coefficientwise norm and residual truncation

## Executive conclusions

The two new statements in A4 turn 16 pass the audit, with the already agreed generating-function correction:



$$
\mathcal L_m=m![z^m]\frac{F(z)}{1-z},
\qquad
\mathcal L_m\ne m![z^m](e^zF(z))
$$


in general. In particular, the stronger paid logarithmic guard is valid:


$$
\boxed{
B_*=n-v_2(b!)-1-2s_2(n)-\ell,
\qquad
\ell=\lfloor\log_2(2n+b-1)\rfloor.
}
$$



A4’s complete adjoint/factorial-tail formula is also correct:


$$
\boxed{
4E=W_bx_{0,b}+
\sum_{j=b}^{2n+b-1}\frac{j!}{b!}\theta_j,
\qquad
E=x_0^Ty^E.
}
$$


Its truncation at


$$
j\le \min\{2n+b-1,\ b+T+\ell+2\}
$$


does determine $E\bmod 2^T$, with the whole division by $4$ paid. This is a formula for the complete exponential contraction, not a termwise truncation theorem for the factorial-aligned residual.

I do **not** obtain either of the main outstanding estimates:

* a uniform original-family bound
  

$$
\nu<(0.45866\ldots-\varepsilon)n;
$$


* an exclusion, or a favorable original branch, for the additional normalized exponential resonance of approximately $0.04134n$.

There is, however, a new unconditional obstruction using the **actual forced adjoint on every original index**, rather than arbitrary primitive vectors.

### New result: the actual adjoint has shallow coefficients in the far tail

Let


$$
w=A^{-T}\mathcal R^Tx_0,\qquad
c_w=\min_i v_2(w_i),
$$


and let $\theta_j=w^T\mathbf a_j$ be A4’s complete source observations. Then


$$
\boxed{
0\le c_w\le
w_*:=\max_{0\le j<b}v_2\binom{n+2}{j}
\le\lfloor\log_2(n+2)\rfloor,
}
\tag{E1}
$$


and, more significantly,


$$
\boxed{
\min_{2n\le j\le 2n+b-1}v_2(\theta_j)=c_w.
}
\tag{E2}
$$



Thus the genuine far source block always contains a coefficient of logarithmic valuation. It is not a high-content tail.

The common adjoint also gives an exact derangement-moment formula for the norm. Writing


$$
\mathfrak d_j=j!\sum_{r=0}^{j}\frac{(-1)^r}{r!},
$$


one has


$$
\boxed{
\sum_{j=0}^{2n+b-1}\mathfrak d_j\theta_j
=\Lambda w^Tf^0
=2^{a+1}\Lambda R\,Q,
\qquad Q=x_0^Tx_0.
}
\tag{E3}
$$


The sum on the left has valuation exactly


$$
\boxed{
\frac{3n}{2}-s_2(n)+a+\nu+1,
}
\tag{E4}
$$


although one of its actual summands with $j\ge2n$ has valuation at most $w_*+\ell=O(\log n)$.

This proves **linearly deep cancellation already built into the actual norm observation**, before the exceptional primitive loss $\nu$ is counted.

An analogous statement holds for an integerized complete exponential residual. It has actual far-tail summands of logarithmic valuation, even though its complete sum is divisible by approximately $2^{(1+1/4002)n}$ automatically. Consequently:

> The paid factorial cutoff for $E$ cannot be transferred coefficientwise to either the norm observation or the factorial-aligned residual. The obstruction occurs on every original index and follows from the actual finite matrix and actual adjoint.

This is an infinite-original-family support restriction and a precise obstruction to the proposed shortcut. It is **not** a bound on the additional cancellation.

A second original-domain restriction concerns separator constructions. For


$$
b(u)=b_0q^u,\qquad b_0=9^{18},\quad q=9^{32},
$$


one has exactly


$$
\boxed{
v_2(b(u)-b_0)=8+v_2(u)\qquad(u>0).
}
\tag{E5}
$$


A nontrivial original parameter agreeing with $b_0$ through $L$ bits therefore has


$$
u\ge2^{L-8}.
$$


In particular, the accepted separator regime $L\ge135$ requires an original parameter whose binary word has more than $10^{40}$ bits. The fixed-depth separator theorem remains valid, but a full-high-word implementation of it does not become a feasible original-branch construction.

No computation was executed, and no accepted computation is proposed for repetition.

---

# 1. Preserved finite objects and primitive normalization

Throughout,


$$
\boxed{
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
}
$$


The contact matrix has exactly $b$ rows and columns:


$$
0\le i,j<b.
$$


The reconstructed columns have exactly the physical rows


$$
\boxed{0\le j\le b.}
$$



Put


$$
h=\frac n2,\qquad
R=2^h\binom nh,\qquad
\Lambda=\frac{(n!)^2}{2^n},
\qquad
W_j=\binom{n+2}{j},
$$


and


$$
\lambda_s=s![z^s]\left(1-z+\frac{z^2}{2}\right)^n.
$$



The finite matrix and fixed first force are


$$
A_{ij}=
\sum_{s=0}^{n+i}
\lambda_s\binom{n+i}{s}\binom{2n+i-s}{j},
\tag{1.1}
$$




$$
f_i^0=
\frac{(n+i)!}{n!}
[t^n](1+2t+2t^2)^n(1+t)^i.
\tag{1.2}
$$



The reconstruction is


$$
(\mathcal Rz)_j=W_j(jz_{j-1}-z_j),
\qquad z_{-1}=z_b=0.
\tag{1.3}
$$


Both corrected columns remain


$$
Z_w=\mathcal RA^{-1}f^0,
\qquad
V_w=\mathcal RA^{-1}(h^e+h^F)+e_0,
\tag{1.4}
$$


with


$$
x=\frac{Z_w}{2R},
\qquad
y=\frac{V_w}{4b!},
\qquad
N=x^Tx,\quad H=x^Ty.
\tag{1.5}
$$



Write


$$
x=2^ax_0,\qquad
Q=x_0^Tx_0=2^\nu Q_*,
\qquad Q_*\in\mathbb Z_2^\times.
\tag{1.6}
$$


The established actual-content theorem is reused:


$$
\boxed{
0\le a\le w_*-1
\le\lfloor\log_2(n+2)\rfloor-1.
}
\tag{1.7}
$$


The A4 and A5 arguments establish the same theorem using the same physical first-force witness. They are independent audits, not two distinct new results.

## 1.1 Least clearer, row contents, and the final gcd

Let


$$
\omega_j=j!W_j.
$$


The original unweighted columns corresponding to the weighted columns above are


$$
u_j=\frac{2\Lambda R\,x_j}{\omega_j},
\qquad
v_j=\frac{4b!\,y_j}{\omega_j}.
$$


The least simultaneous clearer is the actual one:


$$
d_B=
\operatorname{lcm}_{0\le j\le b}
\bigl\{\operatorname{den}(u_j),\operatorname{den}(v_j)\bigr\},
\tag{1.8}
$$


with reduced positive denominators.

No row content of $(d_Bu_j,d_Bv_j)$ is divided out in this report. The retained producer and its all-prime reduction remain


$$
A_B=d_B^2\,4\Lambda^2R^2N,
\qquad
H_B=d_B^2\,8\Lambda Rb!H,
$$




$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\quad p_n=H_B/g_B.
}
\tag{1.9}
$$



With


$$
\mathscr D_n=\frac{\Lambda R}{2b!},
$$


the actual rational center satisfies


$$
\frac{p_n}{q_n}=\frac{H}{\mathscr D_nN},
$$


and for every prime $p$,


$$
\boxed{
v_p(q_n)=
\max\{v_p(\mathscr D_n)+v_p(N)-v_p(H),0\}.
}
\tag{1.10}
$$



All binary statements below concern these columns. None replaces the final gcd by a coordinate content, a high-block norm, or a selected-prime divisor.

---

# 2. Audit of the refined complete logarithmic guard

## 2.1 The source convention is settled

The contact excerpt defines


$$
\mathcal L_m=m![z^m]\frac{F(z)}{1-z}.
$$


Equivalently,


$$
\mathcal L_m=m\mathcal L_{m-1}+g_m,
\qquad g_m=F^{(m)}(0),
$$


so that


$$
\boxed{
\mathcal L_m=
\sum_{r=1}^{m}\frac{m!}{r!}g_r.
}
\tag{2.1}
$$



The repeated $e^zF$ label in A4 turn 16 is false, but its displayed finite sum is the correct one. The valuation proof uses that finite sum and therefore survives.

The already established scalar estimate is


$$
v_2(\mathcal L_m)
\ge
1+v_2(m!)-\lfloor\log_2m\rfloor
-\left\lfloor\frac{m-1}{2}\right\rfloor.
\tag{2.2}
$$



## 2.2 Payment of the outer binomial

Set $N_i=n+i$ and $m=2n+i-s=n+(N_i-s)$. Then


$$
v_2\!\left(\lambda_s\binom{N_i}{s}\right)
\ge
v_2(N_i!)-v_2((N_i-s)!)-\lfloor s/2\rfloor.
$$


Also


$$
v_2(m!)-v_2((N_i-s)!)\ge v_2(n!).
$$


Consequently every complete source summand has valuation at least


$$
v_2(N_i!)+v_2(n!)+1-\ell
-\lfloor s/2\rfloor-\lfloor(m-1)/2\rfloor.
$$


Using $s+m=2n+i$ gives


$$
v_2(h_i^F)\ge
n+\lfloor i/2\rfloor+2-s_2(n+i)-s_2(n)-\ell.
\tag{2.3}
$$


Now


$$
s_2(n+i)\le s_2(n)+s_2(i),
\qquad
s_2(i)\le\lfloor i/2\rfloor+1,
$$


hence


$$
\boxed{
v_2(h_i^F)\ge n+1-2s_2(n)-\ell.
}
\tag{2.4}
$$



Transport through the actual $2$-integral $A^{-1}$ and $\mathcal R$, followed by the whole division by $4b!$, proves


$$
\boxed{
y^F\in2^{B_*}\mathbb Z_2^{b+1},
\qquad
B_*=n-v_2(b!)-1-2s_2(n)-\ell.
}
\tag{2.5}
$$



This audits A4’s refinement affirmatively.

The improvement over the earlier guard is exactly


$$
B_*-B_n=1+2\ell-2s_2(n)\ge1.
$$


It improves the logarithmic allowance, not the linear coefficient.

---

# 3. Audit of the complete factorial tail and its alignment

Let


$$
M=2n+b-1,
$$


and define the auxiliary source columns


$$
(\mathbf a_j)_i=
\sum_{s=0}^{n+i}
\lambda_s\binom{n+i}{s}
\binom{2n+i-s}{j},
\qquad 0\le j\le M.
\tag{3.1}
$$


Only $0\le j<b$ are matrix columns. The other $\mathbf a_j$ do not enlarge $A$.

Set


$$
w=A^{-T}\mathcal R^Tx_0,
\qquad
\theta_j=w^T\mathbf a_j.
\tag{3.2}
$$


Then


$$
\boxed{
w^Tf^0=2^{a+1}R\,Q.
}
\tag{3.3}
$$



The complete exponential scalar obeys


$$
\mathcal D_m=\sum_{j=0}^{m}j!\binom mj,
$$


and therefore


$$
h^e=\sum_{j=0}^{M}j!\mathbf a_j.
\tag{3.4}
$$



For $j<b$,


$$
\theta_j=(\mathcal R^Tx_0)_j
=(j+1)W_{j+1}x_{0,j+1}-W_jx_{0,j}.
$$


The full finite telescoping identity is


$$
\sum_{j=0}^{b-1}j!\theta_j
=-x_{0,0}+b!W_bx_{0,b}.
\tag{3.5}
$$


Thus, for $E=x_0^Ty^E$,


$$
\boxed{
4E=W_bx_{0,b}
+\sum_{j=b}^{M}\frac{j!}{b!}\theta_j.
}
\tag{3.6}
$$



The terminal is exactly the physical $b$-th row.

## 3.1 Paid precision

To determine $E\bmod2^T$, equation (3.6) must be evaluated modulo $2^{T+2}$ before division. Since $\theta_j\in\mathbb Z_2$, it suffices to choose $J$ with


$$
v_2((J+1)!/b!)\ge T+2.
$$


A4’s sufficient choice


$$
\boxed{
J=\min\{M,\ b+T+\ell+2\}
}
\tag{3.7}
$$


is valid.

If the digit of $E$ at depth $T$, rather than just divisibility by $2^T$, is required, one evaluates $E\bmod2^{T+1}$ and correspondingly pays one additional input bit. This distinction remains important when testing the first nonzero digit.

Later we prove $\theta_j\in2^{c_w}\mathbb Z_2$. If $c_w$ is known, the exact sufficient condition improves to


$$
v_2((J+1)!/b!)+c_w\ge T+2.
\tag{3.8}
$$


Because $c_w=O(\log n)$, this is not a new linear-scale improvement.

## 3.2 Agreement with the complete factorial residual

Reuse the exact factorial-force identity from turn 11:


$$
\sum_{s=0}^{n+i}
\lambda_s\binom{n+i}{s}(2n+i-s)!
=\Lambda f_i^0.
\tag{3.9}
$$



Let


$$
\sigma_n=\frac{\mathcal D_n}{n!},
\qquad
c_n=\mathscr D_n\sigma_n,
\qquad
d=\frac n2-v_2(b!)-1.
$$


Then


$$
c_n=2^du_n,\qquad u_n\in\mathbb Z_2^\times,
$$


and the complete split is


$$
y^E=c_nx+z^E,
\qquad
E=c_n2^aQ+\Psi,
\qquad
\Psi=x_0^Tz^E.
\tag{3.10}
$$



Here $z^E$ is still defined by the complete residual source


$$
\rho_i=
\sum_{s=0}^{n+i}
\lambda_s\binom{n+i}{s}
\sum_{r=n+1}^{2n+i-s}\frac{(2n+i-s)!}{r!},
$$


and the actual terminal:


$$
z^E=\frac{\mathcal RA^{-1}\rho+e_0}{4b!}.
\tag{3.11}
$$



Equations (3.6) and (3.10) are compatible. The important limitation is:



$$
\boxed{
\text{The factorial tail truncates }E.
\text{ It does not separately truncate }\rho,\ z^E,\text{ or }\Psi.
}
\tag{3.12}
$$



The next sections make this limitation quantitative for the actual original family.

---

# 4. New theorem: logarithmic content of the actual common adjoint

The primitive first column satisfies the endpoint relation


$$
x_{0,b}=-\sum_{j=0}^{b-1}t_jx_{0,j},
\qquad
t_j=\frac{\omega_b}{\omega_j}.
\tag{4.1}
$$


On the original powers, $b\equiv1\pmod8$. Each $t_j$, $j<b$, contains the factor


$$
n+3-b=4001b+3,
$$


which has valuation $2$. Hence


$$
t_j\in4\mathbb Z.
\tag{4.2}
$$



Write


$$
\zeta=(x_{0,0},\ldots,x_{0,b-1})^T.
$$


Then


$$
x_0=
\begin{pmatrix}I\\-t^T\end{pmatrix}\zeta,
$$


and $\zeta$ is primitive: if its entries were all even, the endpoint relation would make $x_0$ nonprimitive.

Let $C$ be the $b\times b$ lower-bidiagonal reconstruction matrix


$$
(Cz)_j=jz_{j-1}-z_j,\qquad 0\le j<b,
$$


and put


$$
D_W=\operatorname{diag}(W_0,\ldots,W_{b-1}).
$$


Then


$$
\mathcal R=
\begin{pmatrix}I\\-t^T\end{pmatrix}D_WC,
$$


so


$$
\boxed{
\mathcal R^Tx_0
=C^TD_W(I+tt^T)\zeta.
}
\tag{4.3}
$$



Both $C^T$ and $A^{-T}$ are unimodular over $\mathbb Z_2$. Also


$$
\det(I+tt^T)=1+t^Tt\in\mathbb Z_2^\times.
$$


Therefore $(I+tt^T)\zeta$ is primitive.

Multiplication by $D_W$ can raise minimum coordinate valuation by at most $w_*$. It follows that:

### Theorem 4.1 — Actual adjoint-content bound
For every original index,


$$
\boxed{
0\le c_w:=\min_i v_2(w_i)\le w_*
\le\lfloor\log_2(n+2)\rfloor.
}
\tag{4.4}
$$



This is a new statement about the actual common adjoint. It does not repeat the first-column content theorem.

## 4.1 The full Gram matrix is retained

For completeness,


$$
G=\mathcal R^T\mathcal R
$$


is the actual tridiagonal matrix with


$$
G_{ii}=W_i^2+(i+1)^2W_{i+1}^2,
$$




$$
G_{i,i+1}=G_{i+1,i}=-(i+1)W_{i+1}^2.
\tag{4.5}
$$


In particular, its last diagonal entry includes $b^2W_b^2$.

The factorization above gives


$$
\det G=
\left(\prod_{j=0}^{b-1}W_j^2\right)(1+t^Tt).
\tag{4.6}
$$


The second factor is a binary unit.

This explains why the complete Gram structure bounds the adjoint content but does not by itself bound


$$
\nu=v_2(\zeta^T(I+tt^T)\zeta).
$$


The outstanding question is the value of this quadratic form at its **fixed forced vector**, not its determinant.

---

# 5. The common adjoint polynomial and a new exact norm moment

Define


$$
P_i(t)=
\sum_{s=0}^{n+i}
\lambda_s\binom{n+i}{s}(1+t)^{2n+i-s}.
\tag{5.1}
$$


Then


$$
P_i(t)=\sum_{j=0}^{M}(\mathbf a_j)_i t^j,
$$


and the actual adjoint polynomial is


$$
\boxed{
P(t)=\sum_{i=0}^{b-1}w_iP_i(t)
=\sum_{j=0}^{M}\theta_jt^j.
}
\tag{5.2}
$$



Each $P_i$ is an integer polynomial, monic of degree $2n+i$.

There is also an exact differential-operator description. With $\xi=1+t$,


$$
\boxed{
P_i(\xi-1)
=\xi^n\phi(D_\xi)^n\xi^{n+i},
\qquad
\phi(z)=1-z+\frac{z^2}{2}.
}
\tag{5.3}
$$


Thus


$$
P(\xi-1)
=\xi^n\phi(D_\xi)^n
\left(\sum_{i=0}^{b-1}w_i\xi^{n+i}\right).
\tag{5.4}
$$



This is an identity for the complete finite source polynomial. It does not continue the contact equations past $b-1$.

## 5.1 Factorial moments after translation

Introduce the finite polynomial functional


$$
\mathcal M(\xi^m)=m!.
$$


Define


$$
\mathfrak d_j=\mathcal M((\xi-1)^j)
=\sum_{m=0}^{j}(-1)^{j-m}\binom jm m!
=j!\sum_{r=0}^{j}\frac{(-1)^r}{r!}.
\tag{5.5}
$$


These are the classical derangement numbers.

Applying $\mathcal M$ to (5.1) after $t=\xi-1$, and using the complete factorial-force identity, gives


$$
\mathcal M(P_i(\xi-1))=\Lambda f_i^0.
$$


Consequently:

### Theorem 5.1 — Complete derangement-moment norm identity


$$
\boxed{
S_N:=\sum_{j=0}^{M}\mathfrak d_j\theta_j
=\Lambda w^Tf^0
=2^{a+1}\Lambda R\,Q.
}
\tag{5.6}
$$



This is a finite identity. No convergence of a factorial series or $2$-adic integral is being asserted.

Since


$$
v_2(\Lambda)=n-2s_2(n),
\qquad
v_2(R)=\frac n2+s_2(n),
$$


we obtain the exact valuation


$$
\boxed{
v_2(S_N)=
V:=\frac{3n}{2}-s_2(n)+a+\nu+1.
}
\tag{5.7}
$$



The force is nonzero, reconstruction is injective, and the rational norm $Q$ is positive. Thus $S_N\ne0$, so this valuation is finite.

---

# 6. New original-family support theorem

The leading-degree structure of the $P_i$ now gives a useful fact that does not follow merely from primitivity.

For $0\le r<b$,


$$
\theta_{2n+r}
=
\sum_{i=r}^{b-1}
w_i[t^{2n+r}]P_i(t).
\tag{6.1}
$$


The matrix in (6.1) is upper triangular over $\mathbb Z$, with diagonal entries $1$, because $P_i$ is monic of degree $2n+i$.

Hence that matrix is unimodular over $\mathbb Z_2$, and therefore


$$
\boxed{
\min_{2n\le j\le M}v_2(\theta_j)=c_w.
}
\tag{6.2}
$$



This proves the far-tail support assertion (E2) for the actual adjoint on every original index.

## 6.1 Valuations of the norm weights

The derangement recurrence gives, for $j\ge2$,


$$
\boxed{
v_2(\mathfrak d_j)=
\begin{cases}
0,&j\ \text{even},\\[2mm]
v_2(j-1),&j\ \text{odd}.
\end{cases}
}
\tag{6.3}
$$



Indeed, $\mathfrak d_j=j\mathfrak d_{j-1}+(-1)^j$ shows that even-index derangements are odd. For odd $j\ge3$,


$$
\mathfrak d_j=(j-1)(\mathfrak d_{j-1}+\mathfrak d_{j-2}),
$$


and the parenthesized factor is odd.

Choose $j_*\in[2n,M]$ with $v_2(\theta_{j_*})=c_w$. Then


$$
\boxed{
v_2(\mathfrak d_{j_*}\theta_{j_*})
\le c_w+\ell
\le w_*+\ell.
}
\tag{6.4}
$$



Combining (5.7) and (6.4) proves:

### Theorem 6.1 — Forced baseline norm cancellation

For every original index, the exact norm-moment sum contains an actual far-tail summand of valuation at most $w_*+\ell$, whereas the complete sum has valuation


$$
\frac{3n}{2}-s_2(n)+a+\nu+1.
$$


Thus the cancellation depth above the smallest summand valuation is at least


$$
\boxed{
\frac{3n}{2}-s_2(n)+a+\nu+1-w_*-\ell.
}
\tag{6.5}
$$



In particular, it is already linear in $n$ without assuming that $\nu$ is large.

### What this obstructs

This is a concrete original-domain obstruction to an argument of the form:

> “The common adjoint has a primitive or shallow coordinate, and the source coefficients have controlled valuations; therefore the norm contraction cannot be very deep.”

For this actual force and actual finite matrix, shallow adjoint observations coexist with approximately $1.5n$ forced cancellation in the coefficient representation of the norm.

The theorem does **not** show that $\nu$ is large. It shows why a valuation-minimum argument cannot bound $\nu$ without first accounting for the complete, already forced cancellation.

---

# 7. The complete residual has the same obstruction

The norm identity lets us compare the factorial tail and the aligned residual with all units explicit.

Because


$$
4b!E=x_{0,0}+\sum_{j=0}^{M}j!\theta_j
$$


and


$$
4b!c_n2^aQ=\sigma_nS_N,
$$


we have


$$
4b!\Psi=
x_{0,0}+\sum_{j=0}^{M}(j!-\sigma_n\mathfrak d_j)\theta_j.
\tag{7.1}
$$



Multiplying by $n!$, define the integral coefficient weights


$$
\beta_j=n!j!-\mathcal D_n\mathfrak d_j.
\tag{7.2}
$$


Then


$$
\boxed{
\mathcal P_\Psi:=
4b!n!\Psi
=
n!x_{0,0}+\sum_{j=0}^{M}\beta_j\theta_j.
}
\tag{7.3}
$$



Equivalently, after the actual finite terminal cancellation,


$$
\boxed{
\mathcal P_\Psi
=
n!b!W_bx_{0,b}
+n!\sum_{j=b}^{M}j!\theta_j
-\mathcal D_nS_N.
}
\tag{7.4}
$$



Equations (7.3) and (7.4) are the exact interface between A4’s factorial tail and the turn-11 complete residual.

## 7.1 Actual far-tail residual summands are shallow

Since $n$ is even, $\mathcal D_n$ is odd. For $j\ge2n$,


$$
v_2(n!j!)>\ell\ge v_2(\mathfrak d_j).
$$


Therefore the two terms defining $\beta_j$ have unequal valuations, and


$$
\boxed{
v_2(\beta_j)=v_2(\mathfrak d_j)
\qquad(2n\le j\le M).
}
\tag{7.5}
$$



At the same $j_*$ as in §6,


$$
\boxed{
v_2(\beta_{j_*}\theta_{j_*})
\le c_w+\ell\le w_*+\ell.
}
\tag{7.6}
$$



Yet $\Psi\in\mathbb Z_2$, so the complete sum in (7.3) satisfies


$$
\boxed{
v_2(\mathcal P_\Psi)
\ge v_2(n!)+v_2(b!)+2
=
n+b-s_2(n)-s_2(b)+2.
}
\tag{7.7}
$$



Thus the actual integerized residual also exhibits at least


$$
n+b-O(\log n)
$$


of built-in cancellation above a shallow far-tail summand.

This conclusion includes the possibility $\Psi=0$; it does not presume nonvanishing of this individual residual.

## 7.2 A target-specific interface restriction

Suppose the target $T=a+\nu+k$ is logarithmically protected:


$$
T\le B_*.
$$


A4’s sufficient cutoff then satisfies


$$
\begin{aligned}
J
&\le b+B_*+\ell+2\\
&=n+s_2(b)+1-2s_2(n)
<2n.
\end{aligned}
\tag{7.8}
$$



Therefore:

* the paid factorial evaluation of $E\bmod2^T$ omits the whole block $2n\le j\le M$;
* that same block necessarily contains a logarithmically shallow summand in the norm-moment representation;
* it also necessarily contains a logarithmically shallow summand in the integerized residual representation.

### Corollary 7.1 — No coefficientwise transfer of the paid cutoff

On every original index, throughout the logarithmically protected target regime, the exponential factorial cutoff cannot be applied to the norm or residual by a termwise valuation argument.

It remains legitimate to compute the short factorial observation and subtract the **whole evaluated norm-aligned scalar**. What is not legitimate is to replace that global subtraction by deleting the corresponding far source coefficients.

This is a genuine infinite-original support restriction. It makes no claim that the aggregate omitted block is nonzero modulo a specified modulus: aggregate cancellation is precisely the unresolved issue.

---

# 8. Exact valuation and unit at first resonance

The foregoing obstruction must not obscure the exact comparison that is already proved.

Set


$$
z=a+\nu,\qquad
d=\frac n2-v_2(b!)-1.
$$


The first-resonance depth for $\Psi$ is $z+d$.

Let


$$
P_0=v_2(4b!n!)
=v_2(n!)+v_2(b!)+2,
$$


and let


$$
U=\frac{4b!n!}{2^{P_0}}\in\mathbb Z_2^\times.
$$


A direct calculation gives


$$
\boxed{
P_0+z+d=V,
}
\tag{8.1}
$$


where $V=v_2(S_N)$ is given in (5.7).

Moreover,


$$
4b!n!\,c_n2^aQ=\mathcal D_nS_N.
$$


Consequently,


$$
\boxed{
Uu_nQ_*=\mathcal D_n\frac{S_N}{2^V}.
}
\tag{8.2}
$$


If $v_2(\Psi)=z+d$, then


$$
\boxed{
U\frac{\Psi}{2^{z+d}}
=\frac{\mathcal P_\Psi}{2^V}.
}
\tag{8.3}
$$



Thus the required normalized cancellation is exactly cancellation between


$$
\mathcal D_n\frac{S_N}{2^V}
\quad\text{and}\quad
\frac{\mathcal P_\Psi}{2^V},
$$


both units. There is no unspecified unit conversion between A4’s formula and the turn-11 residual.

The aligned scalar alone is not the target. The whole residual must match both its valuation and its unit.

## 8.1 Updated guards

Using $B_*$, the nonresonance hypothesis becomes


$$
z+d<B_*
\quad\Longleftrightarrow\quad
\boxed{
a+\nu<\frac n2-2s_2(n)-\ell.
}
\tag{8.4}
$$


If this holds and


$$
v_2(\Psi)\ne z+d,
$$


the established nonresonance theorem gives


$$
\delta_2\le d.
$$



For a target $k>d$, logarithmic omission in the divisibility test is justified by


$$
z+k\le B_*.
\tag{8.5}
$$


A strict inequality protects the next digit.

At the denominator-relevant scale, the additional normalized cancellation remains


$$
\boxed{
k-d=
\left(\eta-\frac12+\frac1{4002}\right)n+o(n)
=0.04134\ldots\,n+o(n).
}
\tag{8.6}
$$



The new support theorem does not prove or disprove this extra cancellation. It establishes why the shorter factorial support of $E$ does not, by itself, resolve it.

---

# 9. Original exponent dependence: a rigorous separator cost restriction

The accepted separator theorem is an original-family theorem at its stated fixed precision. Its use for a feasible prescribed branch has a separate cost.

Put


$$
b_0=9^{18},\qquad q=9^{32}.
$$


Since


$$
v_2(q-1)=8,\qquad q\equiv1\pmod8,
$$


the lifting-the-exponent formula gives


$$
\boxed{
v_2(q^u-1)=8+v_2(u)
\qquad(u>0).
}
\tag{9.1}
$$


As $b_0$ is odd,


$$
\boxed{
v_2(b(u)-b_0)=8+v_2(u).
}
\tag{9.2}
$$



Hence a nonzero original index with


$$
b(u)\equiv b_0\pmod{2^L}
$$


must satisfy


$$
u\ge2^{L-8}.
\tag{9.3}
$$


The bound is attained at $u=2^{L-8}$ when $L\ge8$.

The binary word length of the resulting parameter is at least


$$
\log_2 b_0+2^{L-8}\log_2q.
\tag{9.4}
$$


For the accepted separator requirement $L\ge135$, this exceeds $10^{40}$ bits.

Therefore a procedure linear in the complete high-word length is not a feasible bounded original-index calculation in that separator regime. Its small number of states does not remove the cost of reading the required word.

## 9.1 Small high blocks are not original branches

If


$$
b(u)=b_0+2^Lh
\qquad(u>0,\ h\in\mathbb Z),
$$


then


$$
v_3(b(u)-b_0)=v_3(b_0)=36,
$$


because $q^u-1$ is a ternary unit. Thus


$$
\boxed{v_3(h)=36.}
\tag{9.5}
$$



In particular, the useful auxiliary high blocks $h=3$ and $h=11$ cannot be original parameters for any $L$. The sources did not claim otherwise; equation (9.5) now supplies an explicit original-domain obstruction to using them as prescribed original branches.

## 9.2 Scope of this restriction

For every $u>0$,


$$
v_2(b(u)-b_0)\le8+\log_2u,
$$


whereas


$$
n(u)=4002b_0q^u.
$$


Thus the available agreement depth with the fixed seed is $o(n(u))$, indeed much smaller.

This does not exclude an accidental linear resonance at $b(u)$. It excludes obtaining such a resonance merely by treating fixed-seed parameter agreement or a fixed-depth separator receipt as a linear-depth certificate.

The previously accepted norm noncontinuity remains a valid concrete original-family warning. It is not upgraded here to noncontinuity of the norm divided by the actual varying coordinate content.

---

# 10. What has been established about the requested norm bound

The following quantities are now logarithmically controlled on every original index:


$$
a=O(\log n),\qquad c_w=O(\log n).
$$


The far adjoint block is also completely classified at the level of content:


$$
\min_{2n\le j\le M}v_2(\theta_j)=c_w.
$$



These results do **not** imply


$$
\nu<(\rho-\varepsilon)n,
\qquad
\rho=1-\frac1{4002}-\eta.
$$



The precise obstruction is not an arbitrary isotropic vector. It is the actual identity


$$
\sum_j\mathfrak d_j\theta_j
=2^{a+1}\Lambda RQ,
$$


whose left side has shallow actual far-tail terms while its complete value is already forced to depth


$$
\frac{3n}{2}-s_2(n)+a+1+\nu.
$$



Accordingly, a useful next lemma must control **excess cancellation after this baseline has been extracted**. Bounding individual coefficients, proving that the adjoint is primitive, or observing a unit determinant does not do that.

### Concrete follow-on lemma: forced excess-cancellation control

Retain the actual polynomial $P$ from (5.2), with $w$ obtained from the finite forced solve, not chosen independently. A sufficient norm lemma is:

> There exist $\varepsilon>0$ and an effective original-index threshold such that the complete derangement observation has no excess cancellation of depth $(\rho-\varepsilon)n$ above its forced baseline:
> 

$$
> v_2\!\left(\sum_{j=0}^{M}\mathfrak d_j\theta_j\right)
> <
> \frac{3n}{2}-s_2(n)+a+1+(\rho-\varepsilon)n.
>
$$


> The proof must use the dependence of $w$ on $f^0$ and $b=9^{18+32u}$; it cannot follow from the coefficient valuations alone, by Theorem 6.1.

This is still an outstanding lemma, not a theorem of this report. Its advantage over a generic resultant specification is that its complete coefficient weights, forced cancellation baseline, physical source support, and actual shallow-tail obstruction are now explicit.

After such a norm lemma, the distinct resonance obligation remains: control the excess cancellation between the two units in (8.2)–(8.3) through the depth in (8.6). The paid factorial formula provides the legitimate evaluation route; it does not supply that control.

---

# 11. The actual denominator and the whole error

The historical ternary denominator theorem is reused at its established scope:


$$
\boxed{
v_3(q_n)=n-\frac{b+15}{2}.
}
\tag{11.1}
$$


It remains credited to the earlier archive.

At $2$,


$$
v_2(q_n)=\max\{C_n-\delta_2,0\},
$$


where


$$
C_n=\frac{3n}{2}-v_2(b!)-s_2(n)-1.
\tag{11.2}
$$



Let


$$
\mathcal O_n=
\sum_{p\ne2,3}v_p(q_n)\log p\ge0.
$$


Under the retained whole-error theorem,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
\qquad
\log|\epsilon_n|=-\beta n+o(n),
$$


with eventual nonvanishing, the exact asymptotic budget remains


$$
\boxed{
\log|q_n\epsilon_n|
=
(\kappa-\beta)n
-\min(\delta_2,C_n)\log2
+\mathcal O_n+o(n).
}
\tag{11.3}
$$



Nothing in the new support theorem reduces $\mathcal O_n$.

If the established nonresonance hypotheses hold, then $\delta_2\le d$, and the earlier deduction still gives


$$
|q_n\epsilon_n|\longrightarrow\infty
$$


along that infinite original sequence. This is a conditional exclusion of that portion of the approximation family.

A favorable binary branch, if eventually constructed, would still have to pay the nonnegative other-prime residual and preserve


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n
}
$$


with the complete same-index error. Neither the exponential component alone nor an unreduced denominator is an acceptable substitute.

---

# 12. Literature and computation status

The supplied primary-literature gate is consistent with the arguments above:

* factorial valuations, binomial valuations, derangement recurrences, and triangular integral basis changes are classical;
* general diagonal or prime-power state machinery does not evaluate this forced quadratic observation;
* standard orthogonal-polynomial measures have not been identified with this exact finite weighted Gram matrix;
* no inspected theorem supplied in the packet controls the actual original-power norm excess or the normalized complete residual resonance.

No new external literature inspection is claimed in this turn. No irreducibility theorem, finite-field Weil estimate, or general automaticity result is imported without its required hypotheses.

## 12.1 Bounded arithmetic

**No bounded exact calculation is needed to prove the new results above, and no new calculation is commissioned.**

In particular, this report does not request:

* an original-size dense solve;
* the old precision-32 producer;
* any accepted high-counter calculation;
* the abandoned logarithmic zero diagnostic;
* regeneration of a final gcd, denominator, or whole-error receipt.

The new identities have explicit symbolic inputs:

1. the original $A,f^0,\mathcal R$;
2. the actual $w=A^{-T}\mathcal R^Tx_0$;
3. the complete source polynomials $P_i$;
4. the exact factorial and derangement weights.

Their verifiable outputs are:


$$
\min_{2n\le j\le M}v_2(\theta_j)=c_w,
$$




$$
\sum_j\mathfrak d_j\theta_j=\Lambda w^Tf^0,
$$




$$
4b!n!\Psi=n!x_{0,0}+\sum_j
(n!j!-\mathcal D_n\mathfrak d_j)\theta_j.
$$



A bounded computation of an already proof-forced zero would add no information. Conversely, the unknown original linear-depth norm and resonance digits are not made feasible merely by specifying these formulas. No unevaluated specification is presented as an arithmetic receipt.

---

# 13. Proof-status ledger

| Statement | Status |
|---|---|
| Correct logarithmic generating function $F/(1-z)$ | Verified against the contact source |
| A4’s refined guard $B_*$ | **Audited and proved** |
| Actual first-column content $a=O(\log n)$ | Reused; same theorem independently audited by A4 and A5 |
| Complete adjoint/factorial-tail formula | **Audited and proved** |
| Paid cutoff for $E\bmod2^T$ | **Audited, including the whole two-bit division** |
| Actual common-adjoint content $c_w=O(\log n)$ | **New proof** |
| Exact far-tail content $\min_{j\ge2n}v_2(\theta_j)=c_w$ | **New theorem on every original index** |
| Complete derangement-moment norm identity | **New exact derivation** |
| Linearly deep forced baseline cancellation in that norm observation | **New original-family obstruction** |
| Shallow far-tail summands in the integerized complete residual | **New original-family support theorem** |
| Coefficientwise transfer of the exponential cutoff to norm/residual | **Not justified; explicit obstruction proved** |
| Original separator word-length and $v_3(h)=36$ restrictions | **Proved** |
| Target-specific bound $\nu<(\rho-\varepsilon)n$ | Open |
| Actual extra normalized exponential resonance of depth $\sim0.04134n$ | Open |
| Favorable original branch with paid all-prime denominator and whole error | Not established |
| Irrationality or rationality of $e+\pi$ | Unresolved |

---

## Conclusion

A4’s refined logarithmic protection and complete factorial-tail formula are valid. Their compatibility with the turn-11 factorial residual is now explicit down to the exact valuation and odd unit.

The new arithmetic result is an original-family support and cancellation theorem:


$$
\boxed{
\begin{gathered}
c_w=O(\log n),\\
\min_{2n\le j\le2n+b-1}v_2(\theta_j)=c_w,\\
\sum_j\mathfrak d_j\theta_j
=2^{a+1}\Lambda RQ.
\end{gathered}}
$$


It proves that the actual norm observation contains shallow far-tail summands but undergoes approximately $1.5n$ of forced cancellation before the primitive norm loss $\nu$ is measured. The complete integerized exponential residual has an analogous shallow-tail obstruction.

This answers the requested shortcut audit with a concrete obstruction on the original domain: **the same adjoint and the same finite matrix already force linear cancellation among low-valuation coefficient terms.** A paid cutoff for the factorial-weighted exponential observation cannot be applied coefficientwise to the norm or to the aligned residual.

The exact remaining bottleneck is excess cancellation after those forced baselines:

1. bound or classify the actual original-power primitive norm loss $\nu$;
2. evaluate the valuation and unit of the complete residual relative to the aligned norm term through the additional $0.04134n$-scale;
3. retain logarithmic matching wherever its guard is exceeded;
4. pay every remaining prime in the actual primitive denominator against the complete, nonzero, same-index error.

No bounded computation is needed for the proofs reported here. No feasible new computation resolving an unknown original linear-depth interface has been identified.

**The main norm and resonance targets remain open, and no unconditional proof or disproof of the irrationality of $e+\pi$ follows.**
