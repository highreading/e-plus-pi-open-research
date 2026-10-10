> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 Turn 7 — Complete-source recurrences, a scalar telescoping obstruction, and a paid alternative to coordinate alignment

## Abstract

The global objective remains unresolved. This report does **not** prove either rationality or irrationality of $e+\pi$.

The investigation is moved from the stronger coordinate congruence to the actual norm and mixed contraction. The principal conclusions are:

1. **The original moment producer has an exact short source recurrence.** Its coefficients are integral, its leading coefficient is $1$, and its forcing is exactly the displayed $\mathcal H_i$, for $1\le i\le b-2$. The logarithmic contribution is not omitted: it enters both initial charges and is proved to contribute zero to the subsequent recurrence forcing.

2. **For that complete moment specialization, the source-denominator exponent is**
   

$$
\boxed{\delta=0.}
$$


   This follows from the exact recurrence and paid initial-value estimates, not from an assumption that an unspecified recurrence is integral.

3. **The first and second reconstructed columns satisfy the same shifted-moment annihilation equations.** These equations retain the physical terminal. They provide a concrete possible interface for a joint Green identity, rather than another coordinatewise sufficient congruence.

4. **A precise scalar no-go theorem is proved.** At every original index, the actual norm, expressed through its exact finite interpolation, admits no rational first-order hypergeometric antidifference in the reconstruction index. The obstruction is a strictly positive discrete residue. This rules out a natural direct scalar telescoping mechanism; it does not rule out parameter-shifting Green identities or genuinely joint recurrences.

5. **A different, explicitly paid mechanism is identified.** A contiguous identity for the binomial-square kernel does telescope after the parameter changes, but it has an explicit finite-boundary return. Applying that mechanism to the actual columns requires evolving their complete source data as well. The necessary source recurrence is now explicit; the required joint arithmetic closure is still open.

No upper bound for the actual norm cancellation $\nu$, no linear-scale scalar common factor, and no evaluated growing-precision norm/mixed accepting value is obtained. Consequently, the new results supply no established linear improvement in $\log q_n$.

---

## 1. Original objects and the scope of the source audit

Throughout,


$$
p=29,\qquad
b=3^{249005515+574312172u},\qquad n=2001b,
$$


where


$$
u\ge0,\qquad u\equiv2\pmod{p^9}.
$$


Set


$$
N=n+2,\qquad W_j=\binom Nj.
$$



The domains remain exactly:

- contact coordinates $0\le j<b$;
- recurrence source rows $1\le i\le b-2$;
- reconstructed coordinates $0\le j\le b$.

For contact vectors,


$$
(\mathcal R\theta)_j=W_j(j\theta_{j-1}-\theta_j),
\qquad \theta_{-1}=\theta_b=0.
$$


The actual columns are


$$
Z_w=\mathcal RA^{-1}f^0,\qquad
Y=\mathcal RA^{-1}\mathbf r+W_be_b.
$$


Write


$$
C_n=f_0^0,\qquad
\bar f=f^0/C_n,\qquad
\bar\theta=A^{-1}\bar f,\qquad
\psi=A^{-1}\mathbf r,
$$


so that


$$
\bar Z=Z_w/C_n=\mathcal R\bar\theta.
$$



I reuse the established unit theorem


$$
C_n\in\mathbb Z_{29}^{\times},
$$


the complete finite inverse and its returns, the completed first-source Cartier theory, the terminal-normal theorem, and the signed whole-error theorem at their stated scopes. None of the closed low-row or tail calculations is repeated.

The original finite split remains


$$
b=p^3B+5044,\qquad j=\ell+p^3J<b,
$$


with upper endpoint $B$ for $\ell<5044$ and $B-1$ otherwise.

### 1.1 What can be checked about the moment specialization

The referee supplies


$$
A_{ik}
=
\sum_s a_s(n)(n+i)_{\underline s}
\binom{2n+i-s}{k},
\qquad
a_s(n)=[z^s]\left(1-z+\frac{z^2}{2}\right)^n.
\tag{1.1}
$$



A documentary distinction is necessary. The A2 excerpts do not print a second, independent, exact entrywise definition of $A$. In particular, the reduced inverse


$$
A^{-1}\equiv R_{-2n,II}\mathsf P_-\pmod p
$$


does not, by itself, identify the exact exterior block.

Accordingly, the audit below verifies (1.1) against the **moment producer stated by the referee**, including its initial charges, forcing, logarithmic contribution and finite truncation. Results explicitly using that producer are identified as such. The scalar no-go theorem in §6 needs only the actual finite reconstruction and does not depend on this documentary issue.

---

## 2. Exact verification of the moment producer

Put


$$
Q(z)=1-z+\frac{z^2}{2},\qquad D=\frac{d}{dx},
$$


and define


$$
P_i(x)=x^nQ(D)^n x^{n+i}.
\tag{2.1}
$$


Since


$$
Q(D)^n x^{n+i}
=
\sum_s a_s(n)(n+i)_{\underline s}x^{n+i-s},
$$


we have


$$
P_i(x)
=
\sum_s a_s(n)(n+i)_{\underline s}x^{2n+i-s}.
$$


Therefore


$$
[x^k]P_i(1+x)
=
\sum_s a_s(n)(n+i)_{\underline s}
\binom{2n+i-s}{k}.
\tag{2.2}
$$



Thus (1.1) is exactly the Taylor-coefficient rule for this producer.

### 2.1 The exterior exponential force is the stated one

For every nonnegative integer $m$,


$$
T_m
=
\frac1{b!}\sum_{q=b}^m(m)_{\underline q}
=
\sum_{h\ge0}\frac{(b+h)!}{b!}\binom m{b+h}.
\tag{2.3}
$$


The last sum is finite: terms vanish when $b+h>m$.

Applying the producer to (2.3) gives precisely


$$
A_{IE}z,\qquad z_h=\frac{(b+h)!}{b!}.
$$


This is the actual moment continuation, not an exterior block inferred from the interior inverse.

For the full moment source, define


$$
V_m=T_m+\frac{L_m}{b!}.
$$


Then the complete row values are


$$
r_i
=
\sum_s a_s(n)(n+i)_{\underline s}V_{2n+i-s},
\qquad 0\le i<b.
\tag{2.4}
$$


At $i=0,1$, these are exactly the two printed initial charges. The logarithmic part of (2.4) is the moment-produced $h^F/b!$.

### 2.2 Check against the retained reduction of $A$

Write


$$
\lambda_s=s!a_s(n).
$$


Because $p\mid n$,

- for $1\le s<p$, Frobenius gives $a_s(n)\equiv0\pmod p$;
- for $s\ge p$, $s!$ is divisible by $p$, while $a_s(n)$ has only powers of $2$ in its denominator.

Hence


$$
\lambda_s\equiv0\pmod p\qquad(s\ge1),
$$


and


$$
A_{ik}\equiv\binom{2n+i}{k}\pmod p.
\tag{2.5}
$$



On the original finite contact range,


$$
\binom{2n+i}{k}
=
\sum_{r=0}^{b-1}\binom ir\binom{2n}{k-r}.
$$


The summands with $r>i$ vanish, so this is an exact finite factorization. It gives


$$
A_{II}\equiv \mathsf P_+R_{2n,II}\pmod p,
$$


and therefore


$$
A_{II}^{-1}\equiv R_{-2n,II}\mathsf P_-\pmod p.
\tag{2.6}
$$



In particular, this specialization has determinant a $p$-adic unit and has $p$-integral finite inverse. The check agrees with the retained inverse, but the logical direction is important: the exact moment rule implies the reduction, not conversely.

---

## 3. A complete short source recurrence, with the logarithm paid

This section supplies a new explicit recurrence for the moment producer. It also explains why two initial charges suffice even though three preceding row positions occur in the general formula.

For $i\ge1$, put


$$
m=n+i
$$


and define


$$
\begin{aligned}
(\mathscr D v)_i
={}&v_{i+1}-(2m+1)v_i
+\frac{m(n+3i-1)}2v_{i-1}\\
&-\frac{(i-1)m(m-1)}2v_{i-2}.
\end{aligned}
\tag{3.1}
$$


At $i=1$, the final coefficient is zero, so no negative source index is used.

Both coefficients containing $1/2$ are integers. For the first, the factors


$$
n+i,\qquad n+3i-1
$$


have opposite parity. The second contains $m(m-1)$.

### Theorem 3.1 — Exact recurrence of the complete source

For the moment specialization of §2,


$$
\boxed{(\mathscr D r)_i=\mathcal H_i
\qquad(1\le i\le b-2),}
\tag{3.2}
$$


where


$$
\mathcal H_i
=
\sum_s a_s(n+1)(n+i)_{\underline s}
\binom{2n+i-s+1}{b}.
\tag{3.3}
$$



The logarithmic contribution is retained in $r_0,r_1$, and its contribution to the right side of (3.2) is exactly zero.

#### Proof

Define the shifted moment polynomial


$$
Q_i^+(x)=x^{n+1}Q(D)^{n+1}x^{n+i}.
\tag{3.4}
$$


A differential-operator calculation gives


$$
\boxed{
(1-D)Q_i^+
=
P_{i+1}-(2m+1)P_i
+\frac{m(n+3i-1)}2P_{i-1}
-\frac{(i-1)m(m-1)}2P_{i-2}.
}
\tag{3.5}
$$



Here is a direct verification of its coefficients. Since


$$
Q'(D)=D-1,\qquad (D-1)^2=2Q(D)-1,
$$


commuting $x$ past $(1-D)Q(D)^{n+1}$ reduces the expression inside $x^nQ(D)^n$ to


$$
(1-D)Q(D)x^{m+1}+(n+2)Q(D)x^m-(n+1)x^m.
$$


Now


$$
(1-D)Q(D)=1-2D+\frac32D^2-\frac12D^3.
$$


The coefficients of


$$
x^{m+1},\quad x^m,\quad x^{m-1},\quad x^{m-2}
$$


are respectively


$$
1,\quad -(2m+1),\quad
\frac{m(n+3i-1)}2,\quad
-\frac{(i-1)m(m-1)}2,
$$


which proves (3.5).

The exponential raw moments satisfy


$$
T_k-kT_{k-1}=\binom kb.
\tag{3.6}
$$


Consequently, applying their moment functional to $(1-D)Q_i^+$ gives (3.3).

It remains to evaluate, rather than discard, the logarithmic forcing. Its recurrence is


$$
L_k-kL_{k-1}=2(k-1)!u_{k-1},
\qquad
u_r=[z^r]Q(z)^{-1}.
\tag{3.7}
$$


Apart from the factor $2/b!$, its contribution is


$$
\sum_s a_s(n+1)m_{\underline s}
(n+m-s)!\,u_{n+m-s}.
\tag{3.8}
$$


This equals


$$
m!\,[z^m]\left(Q(z)^{n+1}\frac{d^n}{dz^n}Q(z)^{-1}\right).
\tag{3.9}
$$



Let


$$
R_n(z)=Q(z)^{n+1}\frac{d^n}{dz^n}Q(z)^{-1}.
$$


Then


$$
R_0=1,\qquad
R_{n+1}=QR_n'-(n+1)Q'R_n.
\tag{3.10}
$$


Inductively,


$$
\deg R_n\le n.
$$


But $m=n+i>n$. Thus (3.9) is zero.

This proves (3.2), including the complete logarithmic contribution. ∎

### 3.1 The actual first source satisfies the homogeneous recurrence

The first source is


$$
f_i^0=\frac{(n+i)!}{n!}J_i(n),\qquad
J_i(n)=[z^n](1+2z+2z^2)^n(1+z)^i.
$$



It satisfies


$$
\boxed{(\mathscr D f^0)_i=0
\qquad(1\le i\le b-2).}
\tag{3.11}
$$



For completeness, this can be checked independently of the moment identification. With $t=1+z$,


$$
J_i(n)
=
\operatorname{Res}_{t=1}
\frac{t^i(2t^2-2t+1)^n}{(t-1)^{n+1}}\,dt.
$$


The residue of a derivative is zero. Applying this to


$$
t^{i-1}(2t^2-2t+1)(t-1)
\frac{(2t^2-2t+1)^n}{(t-1)^{n+1}}
$$


gives


$$
\begin{aligned}
0={}&2(n+i+1)J_{i+1}
-(4n+4i+2)J_i\\
&+(n+3i-1)J_{i-1}
-(i-1)J_{i-2}.
\end{aligned}
\tag{3.12}
$$


Multiplication by $(n+i)!/(2n!)$ gives (3.11). Again, at $i=1$, the negative-index term has coefficient zero.

Thus the complete first and second sources share the same explicit recurrence operator, with forcing $0$ and $\mathcal H_i$, respectively.

---

## 4. The complete source denominator is integral at $29$

Recall the auxiliary exponent


$$
\delta=\max\left\{0,-\min_{0\le i<b}v_p(r_i)\right\}.
$$



### Theorem 4.1 — Paid source integrality

For the complete moment specialization,


$$
\boxed{\mathbf r\in\mathbb Z_{29}^b,\qquad \delta=0.}
\tag{4.1}
$$



#### Proof

Every $a_s(n)$ and $a_s(n+1)$ is $29$-integral. Also,


$$
T_m\in\mathbb Z\qquad(m\ge b).
$$


The recurrence (3.2) has integral coefficients and leading coefficient $1$, while every $\mathcal H_i$ is $29$-integral. It therefore suffices to check both original initial charges.

Solving (3.7) gives


$$
L_m=2m!\sum_{r=1}^m\frac{u_{r-1}}r,
$$


where $u_r\in\mathbb Z_{29}$. Hence


$$
v_p(L_m)\ge v_p(m!)-\lfloor\log_p m\rfloor.
\tag{4.2}
$$



In a nonzero initial-charge summand, write


$$
k=n+i-s\ge0,\qquad m=n+k.
$$


Then


$$
\begin{aligned}
&v_p\left((n+i)_{\underline s}\frac{L_{n+k}}{b!}\right)\\
&\quad\ge
v_p((n+i)!)-v_p(k!)
+v_p((n+k)!)-v_p(b!)
-\lfloor\log_p(2n+b-1)\rfloor\\
&\quad\ge
2v_p(n!)-v_p(b!)
-\lfloor\log_p(2n+b-1)\rfloor.
\end{aligned}
\tag{4.3}
$$


The last inequality uses


$$
\frac{(n+k)!}{k!}=n!\binom{n+k}{n}.
$$



The final lower bound is the retained $N_{\log}$, which is positive on the original family. For example,


$$
N_{\log}\ge
\frac{3863}{28}b-\lfloor\log_p(4003b-1)\rfloor>0.
$$


Thus both complete initial charges are $29$-integral.

Forward use of (3.2), only through $i=b-2$, proves integrality of every original row. No nonunit division occurs. ∎

This theorem does not erase the logarithmic initial data. It proves that those data are integral and that their subsequent forcing is exactly zero. Nor does $\delta=0$ determine the actual least simultaneous clearer $d_B$, which is an all-prime object.

---

## 5. Actual scalar reconstruction and a new joint moment constraint

### 5.1 Check of the referee’s weighted scalar formula

Write


$$
\bar Z=p^a\bar x,\qquad a=c+2,
$$


with $\bar x$ primitive at $p$, and set


$$
d_j=\bar x_j-(N-j)\bar x_{j+1},
\qquad 0\le j<b.
\tag{5.1}
$$


These $d_j$ are the referee’s weighted differences; the notation avoids confusion with the source-denominator exponent $\delta$.

Reuse


$$
t_j=\frac{(N-j)!}{(N-b)!},\qquad
\tau=t^Tt\in\mathbb Z_p^\times,\qquad
P=I-\frac{tt^T}{\tau},
$$


and


$$
B_j=\sum_{k=0}^j\frac{(N-k)!}{(N-j)!}t_k.
$$



Put


$$
h=6\psi-p\bar\theta,\qquad
\rho_j=W_jh_j+\frac{6W_b}{\tau}B_j.
\tag{5.2}
$$


Direct finite summation by parts gives


$$
\bar Z^T\mathcal Rh
=
-p^a\sum_{j<b}d_jW_jh_j.
$$


The terminal contribution is $6W_b\bar Z_b$, and the exact normal identity gives


$$
p^a\sum_{j<b}d_jB_j=-\tau\bar Z_b.
$$


Therefore


$$
\boxed{
\Delta
=\bar Z^T(6PY-p\bar Z)
=-p^a\sum_{j<b}d_j\rho_j.
}
\tag{5.3}
$$



This validates the referee’s scalar reconstruction. It uses the complete $h$, not a head approximation. The target remains


$$
\sum_{j<b}d_j\rho_j\equiv0\pmod{p^{a+2+\nu}},
\tag{5.4}
$$


where


$$
\bar x^T\bar x=p^\nu\bar\eta,\qquad
\bar\eta\in\mathbb Z_p^\times.
$$



Neither the primitivity of the $d_j$ nor a terminal coordinate obstruction bounds the valuation of this completed sum.

### 5.2 A shifted-moment annihilator for both columns

Define the unweighted reconstructed coordinates directly:


$$
z_j=j\bar\theta_{j-1}-\bar\theta_j,
$$




$$
y_j=j\psi_{j-1}-\psi_j+\mathbf1_{j=b},
\tag{5.5}
$$


with the original zero boundary conventions. Thus


$$
\bar Z_j=W_jz_j,\qquad Y_j=W_jy_j.
$$


These definitions introduce no division by $W_j$.

Let


$$
\mathcal B_{ik}=[x^k]Q_i^+(1+x),
\qquad
1\le i\le b-2,\quad 0\le k\le b.
\tag{5.6}
$$


From (3.5),


$$
(\mathscr D A_{\bullet k})_i
=\mathcal B_{ik}-(k+1)\mathcal B_{i,k+1}.
\tag{5.7}
$$



Multiplying by the contact coordinates and retaining the last term $k=b$ yields


$$
(\mathscr D(A\bar\theta))_i
=-\sum_{k=0}^b\mathcal B_{ik}z_k.
$$


Since $\mathscr D\bar f=0$,


$$
\boxed{
\sum_{k=0}^b\mathcal B_{ik}z_k=0.
}
\tag{5.8}
$$



Similarly,


$$
-\sum_{k=0}^b\mathcal B_{ik}(y_k-\mathbf1_{k=b})
=(\mathscr D r)_i=\mathcal H_i.
$$


But


$$
\mathcal B_{ib}=\mathcal H_i.
$$


Hence


$$
\boxed{
\sum_{k=0}^b\mathcal B_{ik}y_k=0
\qquad(1\le i\le b-2).
}
\tag{5.9}
$$



The physical terminal is essential to the cancellation in (5.9).

There are also the exact integral terminal-normal relations


$$
\boxed{
\sum_{j=0}^b\frac{b!}{j!}z_j=0,\qquad
\sum_{j=0}^b\frac{b!}{j!}y_j=1.
}
\tag{5.10}
$$


They follow either by telescoping (5.5) or from $t^T\bar Z=0$ and $t^TY=W_b$.

### Significance and limitation

Equations (5.8)–(5.10) are a concrete joint interface for a Green calculation. Both complete columns obey the same shifted-moment constraints, with different normal data.

I do **not** infer that an indicated leading minor of $\mathcal B$ is a unit, or even use an unproved rank assertion. A small-dimensional parametrization obtained by solving these equations would have to retain the exact determinant and its valuation.

Nor are these moment constraints an evaluated norm identity. The actual contractions are still


$$
\bar Z^T\bar Z=\sum_{j=0}^bW_j^2z_j^2,\qquad
\bar Z^TY=\sum_{j=0}^bW_j^2z_jy_j.
\tag{5.11}
$$


The moment annihilator is not yet proved to be self-adjoint for the weight $W_j^2$. That is the missing hypothesis for a direct Christoffel–Darboux argument.

---

## 6. A precise no-go theorem for direct rational scalar telescoping

The next theorem concerns the **actual first column**, not a freely chosen replacement source.

### 6.1 Exact finite interpolation

Let $U(X)\in\mathbb Q[X]$, of degree at most $b$, be the unique polynomial satisfying


$$
U(j)=(-1)^j\bar\theta_j\quad(0\le j<b),
\qquad U(b)=0.
\tag{6.1}
$$


Define


$$
H(X)=XU(X-1)+U(X).
\tag{6.2}
$$


Then, at every original reconstructed coordinate,


$$
\boxed{
\bar Z_j=(-1)^{j-1}W_jH(j),
\qquad 0\le j\le b.
}
\tag{6.3}
$$


At $j=b$, the condition $U(b)=0$ is precisely the physical first-column boundary.

Likewise, let $V(X)$ interpolate


$$
V(j)=(-1)^j\psi_j\quad(0\le j<b),
\qquad V(b)=(-1)^{b+1},
\tag{6.4}
$$


and put


$$
G(X)=XV(X-1)+V(X).
$$


Then


$$
\boxed{
Y_j=(-1)^{j-1}W_jG(j).
}
\tag{6.5}
$$


The nonzero value in (6.4) encodes the physical $W_be_b$; it is not a changed boundary convention.

Thus the whole scalars are exactly


$$
\bar Z^T\bar Z=\sum_{j=0}^bW_j^2H(j)^2,
\tag{6.6}
$$




$$
\Delta=\sum_{j=0}^bW_j^2H(j)\bigl(6G(j)-pH(j)\bigr).
\tag{6.7}
$$



These formulas are not claimed as an evaluation. Their purpose is to test a specific scalar summation mechanism.

The interpolation is over $\mathbb Q$, not over $\mathbb Z_p$. For example, if $d_\theta$ clears the actual entries of $\bar\theta$, then


$$
d_\theta b!\,U\in\mathbb Z[X].
$$


No factorial interpolation denominator is silently declared a unit, and none replaces $d_B$.

### Theorem 6.1 — No rational first-order antidifference for the actual norm

At every original index there is no rational function $R(X)\in\mathbb Q(X)$ satisfying the rational-function identity


$$
\boxed{
\frac{(N-X)^2}{(X+1)^2}R(X+1)-R(X)=H(X)^2.
}
\tag{6.8}
$$



Equivalently, the actual norm summand in (6.6) has no first-order rational hypergeometric telescoping certificate of the form


$$
W_{j+1}^2R(j+1)-W_j^2R(j)=W_j^2H(j)^2.
$$



#### Proof

Set


$$
D_N(X)=\prod_{k=0}^N(X-k).
$$


Since


$$
\frac{D_N(X+1)}{D_N(X)}=\frac{X+1}{X-N},
$$


equation (6.8) would imply


$$
F(X+1)-F(X)=\frac{H(X)^2}{D_N(X)^2},
\qquad
F(X)=\frac{R(X)}{D_N(X)^2}.
\tag{6.9}
$$



For a rational function, the sum of the coefficients of poles of any fixed order along a complete integer-translation orbit is zero for a difference $F(X+1)-F(X)$. Indeed, translation shifts those finitely many coefficients by one position, and their total telescopes.

At the pole $X=k$, $0\le k\le N$, the coefficient of $(X-k)^{-2}$ on the right of (6.9) is


$$
\frac{H(k)^2}{D_N'(k)^2}
=
\frac{H(k)^2}{k!^2(N-k)!^2}.
\tag{6.10}
$$


All these poles belong to one translation orbit. Their sum is nonnegative, and it is strictly positive.

To see strict positivity, note first that $\bar Z\ne0$: the finite inverse is invertible, $\bar f_0=1$, and $\mathcal R$ is injective on the contact space. Hence $H\ne0$. Also,


$$
\deg H\le b+1<N+1,
$$


because $N=2001b+2$. Therefore $H$ cannot vanish at all $N+1$ integers $0,\ldots,N$.

The double-pole coefficient sum in (6.10) is consequently positive, contradicting the necessary zero-sum property of a rational difference. ∎

### 6.2 Exact scope of the no-go statement

This is an unconditional obstruction for the actual norm and its exact finite interpolation. It does not assume generic independence of source coordinates.

It rules out a rational-function antidifference certificate in the reconstruction index. It does **not** rule out:

- a recurrence that changes $n$ or another parameter;
- a matrix-valued Green identity using extra source states;
- a source-specific algebraic relation not expressible as (6.8);
- a finite lookup table containing already-computed partial sums.

The last possibility is not a useful collapse: it merely stores the scalar one was trying to evaluate.

The theorem also does not bound $\nu$. Positivity of a real discrete residue obstructs an exact rational telescoper; it is not a $29$-adic anisotropy statement.

### 6.3 The mixed defect has an exact two-residue test, not an automatic telescoper

For a polynomial $h$, the proper rational function $h/D_N^2$ has coefficients


$$
a_{2,k}=\frac{h(k)}{k!^2(N-k)!^2}
$$


and


$$
a_{1,k}
=
\frac{
h'(k)-2h(k)(\mathsf H_k-\mathsf H_{N-k})
}{
k!^2(N-k)!^2
},
\tag{6.11}
$$


where $\mathsf H_r=\sum_{m=1}^r1/m$.

When $\deg h<2N+2$, a rational antidifference exists exactly when


$$
\sum_{k=0}^Na_{2,k}=0,\qquad
\sum_{k=0}^Na_{1,k}=0.
\tag{6.12}
$$


Necessity is the same orbit-residue argument. Sufficiency follows by taking successive partial sums of the partial-fraction coefficients.

For the complete defect,


$$
h=H(6G-pH).
$$


No supplied theorem proves the two exact cancellations (6.12). In particular, terminal projection does not imply them.

I do not use (6.12) as a renamed proof obligation for the original congruence. It simply identifies why applying a rational telescoping routine to the complete scalar is not justified by the existing moment or terminal identities.

---

## 7. A different paid mechanism: parameter-contiguous telescoping with finite return

The no-go theorem concerns a primitive in $j$ at fixed parameters. A different mechanism is available when the binomial parameter changes.

Define the auxiliary finite kernel


$$
K_{N,b}=\sum_{j=0}^b\binom Nj^2.
$$


For the original application, $b<N$.

### Proposition 7.1 — Exact contiguous identity with the actual finite cutoff

One has


$$
\boxed{
(N+1)K_{N+1,b}-2(2N+1)K_{N,b}
=
(2b-3N-1)\binom Nb^2.
}
\tag{7.1}
$$



#### Proof

Let


$$
T_{N,j}=\binom Nj^2,\qquad
R_N(X)=\frac{X^2(2X-3N-3)}{(N+1-X)^2}.
$$


Direct algebra gives


$$
\begin{aligned}
&(N+1)\frac{T_{N+1,j}}{T_{N,j}}-2(2N+1)\\
&\qquad=
\frac{T_{N,j+1}}{T_{N,j}}R_N(j+1)-R_N(j).
\end{aligned}
\tag{7.2}
$$


Summing from $j=0$ to $b$, the lower return is zero and the upper return is


$$
T_{N,b+1}R_N(b+1)
=
(2b-3N-1)T_{N,b}.
$$


This proves (7.1). ∎

The right side is not optional. Replacing it by zero would use the complete-binomial boundary rather than the original boundary $b$.

At the original $N=n+2$, division by $N+1=n+3$ is paid at $29$, since $N+1\equiv3\pmod{29}$. Repeated parameter shifts, however, encounter nonunits. A joint recurrence must record those valuations; it cannot divide through all shifted leading coefficients as if they remained units.

### 7.1 Why this does not already evaluate the original norm

For a fixed weight $h(j)$, summation by parts in (7.2) gives


$$
\begin{aligned}
&(N+1)\sum_{j=0}^bT_{N+1,j}h(j)
-2(2N+1)\sum_{j=0}^bT_{N,j}h(j)\\
&\quad=
h(b)(2b-3N-1)T_{N,b}\\
&\qquad-
\sum_{j=1}^b
\bigl(h(j)-h(j-1)\bigr)
T_{N,j}
\frac{j^2(2j-3N-3)}{(N+1-j)^2}.
\end{aligned}
\tag{7.3}
$$



For the actual norm, $h=H^2$; for the defect, $h=H(6G-pH)$. These weights themselves depend on the complete moment problem. Moreover, changing $N$ does not preserve $n=2001b$ unless the full parameter evolution is accounted for.

Thus (7.1) is an evaluated auxiliary kernel identity, not an evaluated original accepting value. Equation (7.3) exhibits exactly what a joint mechanism must absorb:

- weighted differences of the actual first and second states;
- the parameter dependence of those states;
- the finite return at $b$;
- all leading-coefficient divisions.

### 7.2 A concrete follow-on lemma

The distinctly different route is now a **shifted-moment Green lemma**, not a stronger coordinate congruence.

A useful version must combine:

1. the explicit source recurrence $\mathscr D$ in (3.1);
2. its complete forcing $\mathcal H_i$;
3. the shifted-moment relations (5.8)–(5.9);
4. the parameter-contiguous kernel identity (7.2);
5. the two initial charges and the physical terminal.

The required output is not merely closure of a formal module. It must produce, on a specified infinite original subfamily, either:

- a nonzero leading residue of
  

$$
p^{-2a}\bar Z^T\bar Z
$$


  at a proved precision $M(n)$, establishing $\nu<M(n)$; or
- a complete evaluated relation between the norm and mixed contraction that survives restoration of the actual contents and clearer.

For example, a proved bound


$$
\nu=O(\log n)
$$


would show that the normalized $29$-adic norm cancellation, like the $c$-dependent gain, is only polynomial in $n$. It would not by itself control the actual $29$-part of $g_B$, because the actual column scalings and contents must still be restored.

The open mathematical step is to establish a finite joint closure with paid pivots or leading coefficients and then evaluate its accepting state on the whole actual word. Neither the source recurrence alone nor (7.1) supplies that closure.

---

## 8. Arithmetic scale: what has and has not changed

The proved Turn 6 bound remains


$$
a=c+2\le v_{29}\binom{n+2}{b}\le\lfloor\log_{29}(n+2)\rfloor.
\tag{8.1}
$$


Consequently, a gain consisting only of $29^{O(c)}$ contributes


$$
O(\log n)
$$


to the logarithmic denominator budget.

This turn proves $\delta=0$ for the complete moment source. That removes an unpaid source-denominator loss from local estimates. It does **not** establish an additional scalar gcd factor.

Likewise, the no-go theorem changes the available proof strategy, not the value of the actual denominator.

At present:

- no bound $\nu=o(n)$ has been proved;
- no linear-scale common scalar factor has been proved;
- no material $29$-adic saving has been ruled out;
- no logarithmic source may be omitted at a target depth merely because it was harmless at a fixed low depth.

The exact source recurrence retains the logarithm through its initial charges at every depth. If a truncated implementation uses the archived threshold $N_{\log}$, that threshold must still be checked at the actual


$$
K=a+2+\nu.
$$



---

## 9. Actual contents, least clearer, all-prime gcd, and whole error

No interpolation, projection, source recurrence or auxiliary parameter shift changes the original arithmetic normalization.

Retain the actual integer columns


$$
N_{B,1},\qquad N_{B,2},
$$


their actual contents, and their least simultaneous clearer $d_B$. Put


$$
\omega_j=\frac{(n+2)!}{(n+2-j)!},\qquad
\Omega=\operatorname{diag}(\omega_0^2,\ldots,\omega_b^2),
$$




$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2}.
$$


Then


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
}
\tag{9.1}
$$



The gcd is over **all primes**.

To retain both actual weighted contents, write


$$
\operatorname{diag}(\omega_j)N_{B,i}=k_iv_i,
$$


where $k_i>0$ is the actual integer content and $v_i$ is primitive. With


$$
S=v_1^Tv_1,\qquad T=v_1^Tv_2,
$$


one has


$$
A_B=k_1^2S,\qquad H_B=k_1k_2T,
$$


and


$$
\boxed{
g_B=k_1\gcd(k_1S,|k_2T|).
}
\tag{9.2}
$$


For every prime $\ell$,


$$
v_\ell(q_n)
=
\max\!\left\{
v_\ell(k_1)-v_\ell(k_2)+v_\ell(S)-v_\ell(T),\,0
\right\}.
\tag{9.3}
$$



The actual primitive multiplier remains


$$
d_B^2/g_B.
$$


Neither $C_n^{-1}$, $\tau^{-1}$, nor an interpolation denominator is a substitute for this normalization.

At the same original index,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
\qquad
q_n(e+\pi)-p_n=-q_n\epsilon_n.
$$


The retained signed whole-error theorem gives eventual nonzero error and


$$
\log|\epsilon_n|
=
-\lambda n+o(n),
\qquad
\lambda=
\left(2+\frac1{2001}\right)\log(1+\sqrt2).
\tag{9.4}
$$



Thus the required comparison remains


$$
\log|q_n\epsilon_n|
=
\log q_n-\lambda n+o(n).
\tag{9.5}
$$


An irrationality proof would follow from


$$
0<|q_n\epsilon_n|\longrightarrow0
$$


on the same infinite original indices.

**The established contribution of this turn to the linear budget for $\log q_n$ is zero.** Its contribution is a paid source recurrence, a precise obstruction to one scalar-collapse mechanism, and a more concrete alternative joint mechanism.

---

## 10. Bounded exact arithmetic for independent checking

No first-original $b\times b$ matrix computation is requested. No closed low-row, tail, unit-table or exterior audit needs to be repeated.

The new proofs can be checked symbolically with bounded inputs.

### 10.1 Contiguous-kernel certificate

**Inputs**

The indeterminates $N,X$ and


$$
R_N(X)=\frac{X^2(2X-3N-3)}{(N+1-X)^2}.
$$



**Calculation**

Clear the denominator $(N+1-X)^2$ in


$$
\frac{(N-X)^2}{(X+1)^2}R_N(X+1)-R_N(X)
-\left(\frac{(N+1)^3}{(N+1-X)^2}-2(2N+1)\right).
$$



**Expected verifiable output**

The zero polynomial. The remaining numerator has degree at most $3$ in $X$. The endpoint simplification must separately return


$$
T_{N,b+1}R_N(b+1)
=(2b-3N-1)T_{N,b}.
$$



This checks a new exact kernel identity. It does not establish an original-family norm valuation.

### 10.2 Source-recurrence coefficient certificate

**Inputs**

The indeterminates $n,m$, with $m=n+i$, and


$$
Q(D)=1-D+\frac{D^2}{2}.
$$



**Calculation**

Expand


$$
(1-D)Q(D)x^{m+1}+(n+2)Q(D)x^m-(n+1)x^m.
$$



**Expected verifiable output**

The four coefficients


$$
1,\quad -(2m+1),\quad
\frac{m(3m-2n-1)}2,\quad
\frac{m(m-1)(n+1-m)}2.
$$


After $m=n+i$, these are exactly the coefficients in (3.5).

The logarithmic cancellation is proved by the degree induction (3.10), not extrapolated from a finite coefficient check.

### 10.3 What is not requested

No bounded calculation here is claimed to evaluate:

- the actual $\nu$ at the first original index;
- the complete norm/mixed accepting value at growing depth;
- the actual weighted contents;
- the all-prime gcd;
- an infinite-family denominator estimate.

Those are mathematical obligations, not consequences of checking the two symbolic certificates.

---

## 11. Proof-status ledger

| Statement | Status |
|---|---|
| The referee’s weighted scalar reconstruction | **Checked exactly**, with the complete force and physical terminal |
| Moment formula (M) as the Taylor-coefficient rule of the supplied producer | **Verified algebraically** |
| Equality of (M) to any different, omitted exact definition of $A$ | Not inferable from the reduced inverse alone |
| Exact complete-source recurrence (3.2) | **Proved for the supplied moment specialization** |
| Logarithmic recurrence forcing is zero for $1\le i\le b-2$ | **Proved**, while retaining both logarithmic initial charges |
| $\delta=0$ for that complete source | **Proved** |
| Homogeneous recurrence for the actual first force | **Proved directly from its coefficient formula** |
| Joint shifted-moment constraints (5.8)–(5.9) | **Proved for the moment specialization**, with the physical terminal |
| A needed moment minor or pivot is a $29$-adic unit | Not asserted |
| Rational first-order norm telescoper of form (6.8) | **Proved impossible at every original index** |
| A parameter-contiguous binomial-square identity with exact finite return | **Proved** |
| An evaluated actual norm/mixed accepting value at growing precision | Open |
| A useful upper bound for the actual $\nu$ | Open |
| A linear-scale common factor with actual contents restored | Open |
| All-prime $q_n$ versus the nonzero whole same-index error | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

## Conclusion

The principal new source result is the explicit, division-paid recurrence


$$
\boxed{
r_{i+1}-(2n+2i+1)r_i
+\frac{(n+i)(n+3i-1)}2r_{i-1}
-\frac{(i-1)(n+i)(n+i-1)}2r_{i-2}
=\mathcal H_i.
}
$$


It retains both complete initial charges and proves, rather than assumes, that the logarithmic contribution creates no additional recurrence forcing. It also proves $\delta=0$ for the supplied complete moment specialization.

The principal new scalar result is a no-go theorem: the actual first-column norm has no rational first-order hypergeometric antidifference in the reconstruction index. Its obstruction is an explicitly positive discrete residue, not an unevaluated accepting sum or a generic-independence assumption.

A distinctly different route remains available: a parameter-shifting Green calculation combining the complete source recurrence, the shifted-moment annihilator, and a binomial-square contiguous identity with its exact finite return. What is missing is a paid joint closure that evaluates the actual norm and mixed scalar, or bounds $\nu$, on an infinite original subfamily.

Finally, any such local result must still be transferred through both actual weighted contents and the least simultaneous clearer to


$$
\boxed{q_n=\frac{A_B}{\gcd(A_B,|H_B|)}}
$$


and compared with the eventual nonzero **whole** error on the **same** infinite original indices. That all-prime arithmetic comparison—and therefore the unconditional irrationality problem—remains open.
