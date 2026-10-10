> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, Turn 8 — A binomial divisor of the complete short-adjoint acceptance

## Abstract

The rationality or irrationality of $e+\pi$ remains unresolved.

This report proves a new divisibility theorem for the **actual complete linear norm acceptance**, including its finite Schur return. On the unchanged original family


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0,
$$


put


$$
B=b-1,\qquad
\beta=\binom{n+B}{B},\qquad
\chi=v_2(\beta),
$$


and retain


$$
S=\sum_{j=0}^{b-1}(n+1-j)\binom{n+2}{j}z^f_j.
$$


Then


$$
\boxed{v_2(S)\ge \chi+1.}
\tag{A}
$$



This is not obtained by discarding the return. The proof establishes separately that:

* the complete retained force head is in $2\beta\mathbb Z_2$, modulo the working precision;
* the entire Schur-return observation is in $2\beta\mathbb Z_2$.

The head calculation uses the actual force recurrence to cancel potentially large denominators $n+r$. The return calculation uses the actual exterior multiplication matrix and its finite boundaries. Thus (A) is an evaluated divisibility statement, not an unevaluated scalar sum.

Writing $x=2^a x_0$ with the actual binary content, the exact payment gives


$$
\boxed{
v_2\!\left(\frac{S}{2^{a+1}}\right)
\ge \max\{0,\chi-a\}.
}
\tag{B}
$$


The established endpoint upper bound


$$
a\le A_{\rm end}:=v_2\binom gd
$$


therefore gives the entirely explicit sufficient criterion


$$
\boxed{\chi\ge A_{\rm end}+1\quad\Longrightarrow\quad Q\equiv0\pmod2.}
\tag{C}
$$



I also prove that $\chi$, and hence the guaranteed **raw** divisibility of $S$, is unbounded along specified infinite original-index subfamilies with $u\equiv1\pmod4$. What is not proved is that $\chi-a$, or even the sufficient difference $\chi-A_{\rm end}$, is positive on infinitely many original indices. This is the precise remaining payment obstruction for the new theorem.

No new all-prime scalar-cofactor bound or whole-error estimate is obtained. In particular, the new binary divisor does not supersede the actual least clearer, final all-prime gcd, primitive denominator, or the known exponentially large ternary denominator factor.

---

## 1. Original objects, boundaries, and proof dependencies

### 1.1 Unchanged original family

Throughout,


$$
\boxed{b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.}
$$


Contact coordinates are exactly


$$
0\le i,j<b,
$$


whereas physical reconstruction has exactly


$$
0\le j\le b.
$$



Retain


$$
h=\frac n2,\qquad d=\frac{b-1}{4},\qquad g=\frac{h+1}{2},
$$


so that


$$
h=8004d+2001,\qquad g=4002d+1001.
$$



The original coefficients and force are


$$
R=2^h\binom nh,\qquad
\Lambda=\frac{(n!)^2}{2^n},\qquad
\phi(z)=1-z+\frac{z^2}{2},
$$




$$
\lambda_s=s![z^s]\phi(z)^n,\qquad
W_j=\binom{n+2}{j},
$$




$$
A_{ij}=
\sum_{s=0}^{n+i}
\lambda_s\binom{n+i}{s}\binom{2n+i-s}{j},
$$


and


$$
\mathfrak f_i=
\frac{(n+i)!}{n!R}
[t^n](1+2t+2t^2)^n(1+t)^i.
$$



For a contact vector $z$, reconstruction is


$$
\Delta_jz=jz_{j-1}-z_j,\qquad z_{-1}=z_b=0,
\qquad
(\mathcal Rz)_j=W_j\Delta_jz.
$$


In particular, the physical terminal is always $z_b=0$.

The complete corrected columns remain


$$
x=\frac12\mathcal RA^{-1}\mathfrak f,
\qquad
y=\frac{\mathcal RA^{-1}(h^e+h^F)+e_0}{4b!}.
\tag{1.1}
$$


The logarithmic force $h^F$ is not deleted.

Write


$$
z^f=A^{-1}\mathfrak f,\qquad x=2^ax_0,
\qquad
a=\min_{0\le j\le b}v_2(x_j),
$$


and


$$
z^k=A^{-1}k,\qquad
k=\frac{h^e-A(j!)_{0\le j<b}}{b!}.
$$



The complete raw norm and mixed observations are


$$
\mathcal U=
\sum_{j=0}^{b-1}W_j^2(\Delta_jz^f)^2
+b^2W_b^2(z^f_{b-1})^2,
\tag{1.2}
$$




$$
\mathcal V=
\sum_{j=0}^{b-1}W_j^2(\Delta_jz^f)(\Delta_jz^k)
+W_b^2bz^f_{b-1}(bz^k_{b-1}+1).
\tag{1.3}
$$


Thus


$$
Q=2^{-2a-2}\mathcal U=x_0^Tx_0,\qquad
E=2^{-a-3}\mathcal V.
\tag{1.4}
$$



Both mixed terminal summands and the norm terminal remain present.

### 1.2 Results reused at their established scope

The new proof uses:

1. The reviewed universal result
   

$$
a\ge1.
$$



2. The reviewed exact endpoint valuation
   

$$
v_2(x_{b-1})=v_2\binom gd,
$$


   and hence
   

$$
\boxed{a\le A_{\rm end}:=v_2\binom gd.}
   \tag{1.5}
$$



3. The independently reviewed complete force modulo $8$:
   

$$
\mathfrak f\equiv(2,1,3,1,4,4,0,\ldots)^T\pmod8.
   \tag{1.6}
$$


   In particular,
   

$$
r\equiv0\pmod4\quad\Longrightarrow\quad
   \mathfrak f_r\in2\mathbb Z_2.
   \tag{1.7}
$$



4. The exact integral force recurrence
   

$$
\begin{aligned}
   \mathfrak f_{i+2}={}&(2n+2i+3)\mathfrak f_{i+1}\\
   &-\frac{(3i+n+2)(n+i+1)}2\mathfrak f_i\\
   &+\frac{i(n+i)(n+i+1)}2\mathfrak f_{i-1}.
   \end{aligned}
   \tag{1.8}
$$


   Its coefficient divisions are exact integer divisions.

5. The established finite Schur completion and Turn 7 short adjoint, with their stated precision restrictions.

The proof below does **not** use Turn 6’s unreviewed modulo-$8$ inverse, content-one criterion, or source-divisibility theorem. Consequently, the new theorem is independent of the pending review of those claims.

By contrast, the assertions


$$
a\ge2\quad\text{on }u\equiv1\pmod4
$$


and


$$
E\in2\mathbb Z_2
$$


remain dependent on that review when invoked through Turn 6. They are not needed below.

---

## 2. The retained paid short-adjoint completion

Fix a precision $L\ge2$, and put


$$
I=8L-2,\qquad m=4(L-1),\qquad T=2L-1.
$$


For the arguments below we require


$$
I+2<b
$$


and the established scope inequality


$$
\boxed{n>4(I+2m+T+4)+2=72L-26.}
\tag{2.1}
$$



All precisions used in this report satisfy these inequalities on the original family.

Let


$$
B=b-1,\qquad M=n+B,\qquad
\beta=\binom MB.
\tag{2.2}
$$


Original congruences give


$$
\boxed{
v_2(n)=1,\quad v_2(B)=4,\quad v_2(M)=1,\quad
M-1\ \text{odd}.
}
\tag{2.3}
$$



The established short adjoint is


$$
\sum_{j\ge0}\mu_jt^j
=\bigl((n+1)-nt-t^2\bigr)(1+t)^{-n}.
\tag{2.4}
$$


The complete acceptance is


$$
S\equiv
\sum_{i=0}^{I}(-1)^i\mathfrak f_i\,\mathcal H_i(B)
+\sum_{v=0}^{m-1}\mu_{b+v}(\eta_f)_v
\pmod{2^L},
\tag{2.5}
$$


where


$$
\eta_f=U_n^{(m)}K\Sigma^{-1}D_f.
\tag{2.6}
$$



Here $\Sigma$ is the actual finite Schur matrix. Its inverse is integral over $\mathbb Z_2$; it is not an infinite-matrix inverse.

The established head coefficients are


$$
\begin{aligned}
\mathcal H_i(B)={}&(n+1)\mathcal F_i(B)\\
&+n\bigl(\mathcal F_i(B-1)+\mathcal F_{i-1}(B-1)\bigr)\\
&-\bigl(\mathcal F_i(B-2)+2\mathcal F_{i-1}(B-2)
+\mathcal F_{i-2}(B-2)\bigr),
\end{aligned}
\tag{2.7}
$$


with


$$
\mathcal F_i(C)=
\binom{n+i-1}{i}\binom{n+C}{C-i}.
\tag{2.8}
$$


Negative lower indices are interpreted as zero.

The force truncation theorem supplies


$$
\mathfrak f_i\equiv0\pmod{2^L}\qquad(i>I)
\tag{2.9}
$$


in the relevant contact range. We will use the two actual entries
$\mathfrak f_{I+1},\mathfrak f_{I+2}$, rather than imposing a false terminal recurrence on a zero-truncated sequence.

---

## 3. New evaluation of the whole force-head divisor

The individual rational expression


$$
\frac{n}{n+r}
$$


can have a large binary denominator. Merely bounding each head term separately would therefore leave an unpaid denominator. The force recurrence cancels precisely this obstruction.

### 3.1 Regrouping the complete head by force differences

The elementary factorial identity


$$
\mathcal F_r(B)
=
\beta\,\frac{n}{n+r}\binom Br
\tag{3.1}
$$


also gives


$$
\mathcal F_r(B-1)
=
\beta\,\frac{B}{M}\frac{n}{n+r}\binom{B-1}{r},
$$




$$
\mathcal F_r(B-2)
=
\beta\,\frac{B(B-1)}{M(M-1)}
\frac{n}{n+r}\binom{B-2}{r}.
\tag{3.2}
$$



Regrouping (2.7) by $r$, the head in (2.5) is congruent modulo $2^L$ to


$$
\boxed{
\beta\sum_{r=0}^{I}(-1)^r\frac{n}{n+r}\,\mathcal T_r,
}
\tag{3.3}
$$


where the **actual force entries** occur in


$$
\begin{aligned}
\mathcal T_r={}&
(n+1)\mathfrak f_r\binom Br\\
&+\frac{nB}{M}
(\mathfrak f_r-\mathfrak f_{r+1})\binom{B-1}{r}\\
&-\frac{B(B-1)}{M(M-1)}
(\mathfrak f_r-2\mathfrak f_{r+1}+\mathfrak f_{r+2})
\binom{B-2}{r}.
\end{aligned}
\tag{3.4}
$$



To justify the two entries beyond $I$: the regrouping with zero extensions is exact. Replacing those zeros by the actual
$\mathfrak f_{I+1},\mathfrak f_{I+2}$ changes the expression only by integer multiples of these entries, through the original integral $\mathcal F_r$. Equation (2.9) therefore pays the change modulo $2^L$.

In particular, no recurrence has been applied across an artificial force boundary.

By (2.3),


$$
\frac{nB}{M}\in16\mathbb Z_2,\qquad
\frac{B(B-1)}{M(M-1)}\in8\mathbb Z_2.
$$


Thus


$$
\mathcal T_r\in\mathbb Z_2
\tag{3.5}
$$


for every retained $r$.

### Lemma 3.1 — Cancellation of the large head denominator

For every $0\le r\le I$,


$$
\boxed{\frac{n}{n+r}\mathcal T_r\in2\mathbb Z_2.}
\tag{3.6}
$$



#### Proof

Put


$$
s=n+r.
$$



**Case 1: $s$ is odd.**  
Then $n/s\in2\mathbb Z_2$, and (3.5) proves the assertion.

**Case 2: $v_2(s)=1$.**  
Since $n\equiv2\pmod4$, this implies $r\equiv0\pmod4$. Equations (1.7) and (3.4) show that $\mathcal T_r$ is even. The factor $n/s$ is a unit, so the result follows.

**Case 3: $t:=v_2(s)\ge2$.**  
Then $r\equiv2\pmod4$, so $r\ge2$ and $v_2(r)=1$.

Using the two standard adjacent-binomial identities in (3.4), write


$$
\mathcal T_r=\binom Br\,\mathcal J_r,
$$


where


$$
\begin{aligned}
\mathcal J_r={}&(n+1)\mathfrak f_r
+\frac{n(B-r)}M(\mathfrak f_r-\mathfrak f_{r+1})\\
&-\frac{(B-r)(B-r-1)}{M(M-1)}
(\mathfrak f_r-2\mathfrak f_{r+1}+\mathfrak f_{r+2}).
\end{aligned}
\tag{3.7}
$$


Since $B-r=M-s$, this becomes


$$
\mathcal J_r
=
2n\mathfrak f_r+(2-n)\mathfrak f_{r+1}-\mathfrak f_{r+2}
+s\,\mathcal E_r,
\tag{3.8}
$$


where $\mathcal E_r\in2^{-1}\mathbb Z_2$. This last assertion follows directly from $v_2(M)=1$ and $M-1$ odd.

Apply the actual recurrence (1.8) at $i=r-1$:


$$
\begin{aligned}
\mathfrak f_{r+1}-\mathfrak f_r
=s\Bigl(
2\mathfrak f_r
-\frac{3r+n-1}{2}\mathfrak f_{r-1}
+\frac{(r-1)(s-1)}2\mathfrak f_{r-2}
\Bigr).
\end{aligned}
\tag{3.9}
$$


Hence


$$
\mathfrak f_{r+1}-\mathfrak f_r
\in s\,2^{-1}\mathbb Z_2.
\tag{3.10}
$$



The recurrence at $i=r$, after using $r=s-n$, similarly gives


$$
\mathfrak f_{r+2}
=
3\mathfrak f_{r+1}+(n-1)\mathfrak f_r
+s\,\mathcal E'_r,
\qquad
\mathcal E'_r\in2^{-1}\mathbb Z_2.
\tag{3.11}
$$


Therefore


$$
2n\mathfrak f_r+(2-n)\mathfrak f_{r+1}-\mathfrak f_{r+2}
=
(n+1)(\mathfrak f_r-\mathfrak f_{r+1})
-s\mathcal E'_r
$$


belongs to $s\,2^{-1}\mathbb Z_2$. Equation (3.8) proves


$$
v_2(\mathcal J_r)\ge t-1.
\tag{3.12}
$$



Finally,


$$
\binom Br=\frac Br\binom{B-1}{r-1}
$$


and $v_2(B)=4,\ v_2(r)=1$ give


$$
v_2\binom Br\ge3.
$$


Consequently


$$
v_2\!\left(\frac n{s}\mathcal T_r\right)
\ge (1-t)+3+(t-1)=3.
$$


This is stronger than required. ∎

### Corollary 3.2 — Evaluated head divisibility

At every admissible precision,


$$
\boxed{
\sum_{i=0}^{I}(-1)^i\mathfrak f_i\mathcal H_i(B)
\in 2\beta\mathbb Z_2+2^L\mathbb Z_2.
}
\tag{3.13}
$$



The force recurrence has paid the potentially arbitrarily large denominators $n+r$. No upper bound on those valuations was assumed.

---

## 4. New evaluation of the complete finite-return divisor

The return is


$$
\mu_{\rm ext}^TU_n^{(m)}K\Sigma^{-1}D_f.
$$


The next calculation evaluates its accepting row before the Schur solve. It does not set the return to zero.

### 4.1 A finite tail-convolution identity

Let


$$
C_j=(-1)^j\binom{n+j-1}{j}.
$$


For positive $q$ and nonnegative $v$,


$$
\boxed{
\sum_{w=0}^{v}C_{q+w}\binom n{v-w}
=
(-1)^q
\frac{n}{q+v}
\binom{n+q-1}{q-1}\binom{n-1}{v}.
}
\tag{4.1}
$$



This is a classical finite binomial-convolution identity. Its use here is to evaluate the actual exterior observation.

For completeness, let


$$
F_q(t)=\sum_{w\ge0}C_{q+w}t^w,\qquad
R_q(t)=(1+t)^nF_q(t).
$$


The coefficient recurrence


$$
(j+1)C_{j+1}=-(n+j)C_j
$$


implies


$$
tR_q'(t)+qR_q(t)=qC_q(1+t)^{n-1}.
$$


Comparing the coefficient of $t^v$ gives


$$
(q+v)[t^v]R_q=qC_q\binom{n-1}{v},
$$


which is (4.1). Every coefficient used here is a finite sum.

Since


$$
\mu_j=(n+1)C_j-nC_{j-1}-C_{j-2},
$$


define


$$
\gamma_v=\sum_{w=0}^{v}\mu_{b+w}\binom n{v-w}.
$$


Equation (4.1) gives the explicit row


$$
\boxed{
\begin{aligned}
\gamma_v={}&(-1)^b\beta n\binom{n-1}{v}\\
&\times\left[
\frac{n+1}{b+v}
+\frac{nB}{M(b+v-1)}
-\frac{B(B-1)}{M(M-1)(b+v-2)}
\right].
\end{aligned}
}
\tag{4.2}
$$



Thus the entire return contribution is exactly


$$
\gamma^TK\Sigma^{-1}D_f.
\tag{4.3}
$$



### 4.2 The actual exterior multiplication cancels the apparent poles

Index the $m$ last contact coordinates by $t=0,\ldots,m-1$. The actual exterior multiplication matrix has entries


$$
K_{vt}
=
\lambda_k\binom{b+v}{k},
\qquad
k=m+v-t.
\tag{4.4}
$$


Coefficients outside the retained symbol are zero at the working precision. In every nonzero entry,


$$
\boxed{k\ge v+1.}
\tag{4.5}
$$



This inequality is a finite-boundary fact. It is important for the low-degree exceptions below.

The ordinary coefficient $[z^k]\phi(z)^n$ has denominator dividing $2^{\lfloor k/2\rfloor}$. Therefore, for $k\ge j$,


$$
\frac{\lambda_k}{k(k-1)\cdots(k-j+1)}
=(k-j)![z^k]\phi(z)^n
$$


gives


$$
v_2\!\left(\frac{\lambda_k}{k(k-1)}\right)\ge-1,
\tag{4.6}
$$




$$
v_2\!\left(\frac{\lambda_k}{k(k-1)(k-2)}\right)\ge-2.
\tag{4.7}
$$



Also,


$$
v_2(\lambda_k)\ge v_2\!\left(\left\lfloor\frac k2\right\rfloor!\right).
\tag{4.8}
$$


It follows that


$$
v_2(\lambda_k/k)\ge0\qquad(k\ge5).
\tag{4.9}
$$


Indeed, for even $k=2d\ge6$,


$$
v_2(d!)\ge1+v_2(d)=v_2(k);
$$


for odd $k$ there is nothing to prove.

The small actual coefficients are


$$
\lambda_1=-n,\qquad \lambda_2=n^2,
$$




$$
\lambda_4=n(n-1)(n^2+n-3),
$$


so


$$
v_2(\lambda_1)=1,\qquad
v_2(\lambda_2)=2,\qquad
v_2(\lambda_4)=1.
\tag{4.10}
$$



### Lemma 4.1 — The complete return row has divisor $2\beta$

For every retained column $t$,


$$
\boxed{
\sum_{v=0}^{m-1}\gamma_vK_{vt}\in2\beta\mathbb Z_2.
}
\tag{4.11}
$$



#### Proof

It suffices to prove the assertion term by term.

Put $X=b+v$. For $k\ge3$, use


$$
\frac{\binom Xk}{X}
=\frac1k\binom{X-1}{k-1},
$$




$$
\frac{\binom Xk}{X-1}
=\frac{X}{k(k-1)}\binom{X-2}{k-2},
$$




$$
\frac{\binom Xk}{X-2}
=\frac{X(X-1)}{k(k-1)(k-2)}
\binom{X-3}{k-3}.
\tag{4.12}
$$



After division by $\beta$, the second term in the bracket of (4.2), multiplied by $K_{vt}$, has fixed prefactor


$$
\frac{n^2B}{M},
\qquad
v_2\!\left(\frac{n^2B}{M}\right)=5.
$$


Equation (4.6) leaves valuation at least $4$.

The third term has fixed prefactor


$$
\frac{nB(B-1)}{M(M-1)},
\qquad
v_2\!\left(\frac{nB(B-1)}{M(M-1)}\right)=4.
$$


Equation (4.7) leaves valuation at least $2$.

For the first term, the factor $n$ pays one binary denominator. Equations (4.9)–(4.10) make it even except possibly when $k=4$. In that exceptional case, (4.5) restricts $v$ to $0,1,2,3$. The remaining product contains


$$
\binom{n-1}{v}\binom{b+v-1}{3}.
$$


It is even in all four cases:

* for $v=0,1,2$, the second upper argument is respectively $0,1,2\pmod4$, so its binomial coefficient with lower argument $3$ is even;
* for $v=3$, $n-1\equiv1\pmod4$, so $\binom{n-1}{3}$ is even.

Thus the first term is even as well.

It remains to check $k=1,2$, where not all three identities in (4.12) apply. By (4.5), the possibilities are only


$$
(k,v)=(1,0),(2,0),(2,1).
$$


For $v=0$, the denominator $b+v-1=B$ cancels the displayed numerator $B$ in (4.2), and $b+v-2=b-2$ is odd. For $v=1$, the denominator $b+v-2=B$ similarly cancels. Together with the exact valuations of $\lambda_1,\lambda_2$, every resulting term is even.

This proves (4.11). ∎

Since $D_f$ and $\Sigma^{-1}$ are integral over $\mathbb Z_2$, we obtain:

### Corollary 4.2 — Complete return divisibility



$$
\boxed{
\sum_{v=0}^{m-1}\mu_{b+v}(\eta_f)_v
\in2\beta\mathbb Z_2.
}
\tag{4.13}
$$



This is an evaluation of the **whole return observation**. The return vector itself need not vanish, and no individual return column has been omitted.

---

## 5. Main theorem and exact primitive payment

### Theorem 5.1 — Binomial divisibility of the actual complete acceptance

For every original index,


$$
\boxed{
v_2(S)\ge
1+v_2\binom{n+b-1}{b-1}.
}
\tag{5.1}
$$



#### Proof

At an admissible precision $L$, equations (2.5), (3.13), and (4.13) give


$$
S\in2\beta\mathbb Z_2+2^L\mathbb Z_2.
\tag{5.2}
$$



Let $\chi=v_2(\beta)$ and choose


$$
L=\max(2,\chi+1).
$$


Kummer’s theorem bounds $\chi$ by the number of binary positions in $n+B$, hence $L=O(\log n)$. On the original family, $n$ and $b=n/4002$ are already much larger than all the required linear functions of this $L$. Thus (2.1) and $I+2<b$ hold.

Equation (5.2) now implies $S\in2^{\chi+1}\mathbb Z_2$. ∎

This proof uses the reviewed force recurrence and parity, the complete finite Schur return, and the established short adjoint. It does not depend on the pending review of Turn 6’s inverse.

### 5.1 The paid scalar consequence

The exact physical summed-reconstruction identity is


$$
\sum_{j=0}^{b}x_j=S/2.
$$


Therefore


$$
\mathscr A:=\frac{S}{2^{a+1}}
=\sum_{j=0}^{b}(x_0)_j\in\mathbb Z_2.
\tag{5.3}
$$


Theorem 5.1 gives


$$
\boxed{
v_2(\mathscr A)\ge\max\{0,\chi-a\}.
}
\tag{5.4}
$$



Using the proved sufficient upper bound $a\le A_{\rm end}$,


$$
\boxed{
v_2(\mathscr A)\ge
\max\{0,\chi-A_{\rm end}\}.
}
\tag{5.5}
$$



Since $t^2\equiv t\pmod2$ for $t\in\mathbb Z_2$,


$$
Q=x_0^Tx_0\equiv\mathscr A\pmod2.
$$


Thus


$$
\boxed{
\chi\ge A_{\rm end}+1
\quad\Longrightarrow\quad Q\equiv0\pmod2.
}
\tag{5.6}
$$



This conclusion pays the actual content by a sufficient proved upper bound. It does not replace $a$ by a convenient guessed value.

A limitation is important: even a high valuation of $\mathscr A$ does **not** imply the same high valuation of $Q$. The square-versus-linear identity used here is only modulo $2$.

---

## 6. A growing original-family result—and its payment limitation

### 6.1 Unbounded raw acceptance divisibility on original indices

For each integer $K\ge10$, impose


$$
\boxed{4003b\equiv275\pmod{2^K}.}
\tag{6.1}
$$


Since $4003$ is odd, this specifies one odd residue for $b$.

Modulo $1024$, that residue is


$$
b\equiv977.
$$


Indeed,


$$
4003\cdot977\equiv275\pmod{1024}.
$$



The original orbit has the established exact order


$$
\operatorname{ord}_{2^K}(9^{32})=2^{K-8}
\qquad(K\ge8).
$$


Its residues are precisely the coset with


$$
b\equiv209\pmod{256}.
$$


Therefore (6.1) specifies a nonempty residue class


$$
u\equiv u_K\pmod{2^{K-8}},
$$


and every such class lies in $u\equiv1\pmod4$.

Now consider the addition


$$
n+B=4003b-1.
$$


At ten bits, (6.1) gives


$$
n\equiv322,\qquad B\equiv976,\qquad
n+B\equiv274\pmod{1024}.
$$


Since


$$
322+976=274+1024,
$$


there is an outgoing carry at bit $9$.

Moreover, (6.1) makes every result bit from bit $10$ through bit $K-1$ zero. An incoming carry cannot stop at a zero result bit: the two input bits must sum to one, and an outgoing carry remains. Hence the carry persists through all those positions.

Kummer’s theorem therefore gives


$$
\boxed{\chi\ge K-9.}
\tag{6.2}
$$


Theorem 5.1 yields


$$
\boxed{v_2(S)\ge K-8.}
\tag{6.3}
$$



Selecting increasing nonnegative representatives from these nonempty original residue classes proves:

### Theorem 6.1 — Unbounded raw short-adjoint divisibility

There are infinitely many original indices, all with $u\equiv1\pmod4$, on which the guaranteed valuation of the complete scalar $S$ is arbitrarily large.

This is a growing theorem proved from the original orbit and full carry propagation. It is not an extrapolation from a finite prefix table.

### 6.2 What this does not yet prove

The construction does not bound the actual $a$ on those same indices. It therefore does not prove that


$$
\chi-a\to\infty,
$$


or even that $\chi>a$ infinitely often.

The distinction is substantive. A residue restriction controlling $K$ low bits of $b$ does not control all the high bits contributing to the endpoint valuation $A_{\rm end}$. Selecting large representatives of a residue class can increase the latter substantially.

The new theorem is consequently:

* a proved, growing **raw** scalar-divisibility theorem;
* a proved, all-original **paid inequality** (5.4)–(5.5);
* not yet a proved growing positive paid acceptance on an infinite original subfamily.

### 6.3 A concrete remaining digit-sum lemma

The sufficient payment difference has no inverse or unevaluated force sum left in it. Since


$$
4g=n+2,\qquad 4d=B,
$$


Kummer’s formula gives


$$
A_{\rm end}
=s_2(B)+s_2(n-B+2)-s_2(n+2),
$$


whereas


$$
\chi=s_2(B)+s_2(n)-s_2(n+B).
$$


Because $n\equiv2\pmod{64}$,


$$
s_2(n+2)=s_2(n).
$$


Therefore


$$
\boxed{
\chi-A_{\rm end}
=
2s_2(4002b)
-s_2(4003b-1)
-s_2(4001b+3).
}
\tag{6.4}
$$



A concrete sufficient follow-on lemma is now:

> **Paid digit-sum excess lemma.** Prove that
> 

$$
> 2s_2(4002\cdot9^{18+32u})
> -s_2(4003\cdot9^{18+32u}-1)
> -s_2(4001\cdot9^{18+32u}+3)\ge1
>
$$


> on a specified infinite set of nonnegative original indices $u$.

That lemma would combine with Theorem 5.1 to prove primitive norm parity on that same infinite set, without determining the exact content.

A growing lower bound for this digit-sum excess would prove growing divisibility of the paid linear acceptance. Neither assertion is proved here. The raw carry construction in §6.1 is not a proof of this three-term digit-sum inequality.

---

## 7. Complete source, all-prime arithmetic, and whole error remain unchanged

The new theorem concerns $x$ alone. It does not permit removal of either source from $y$.

At precision $2^L$, retain the complete source coefficients


$$
a_t=\frac{(b+t)!}{b!},\qquad 0\le t\le T,
$$


and the source completion


$$
\xi_v=
\sum_{t=0}^{T}a_t
\sum_{\substack{0\le r\le t\\0\le v-r\le m}}
\binom n{t-r}\lambda_{v-r}\binom{b+v}{v-r},
$$




$$
\delta=K\Sigma^{-1}G^{[V]}\xi-\xi,
\qquad
\theta_v=\sum_{w=v}^{V}\binom n{w-v}\delta_w,
\qquad V=T+m.
\tag{7.1}
$$


The first term in $\delta$ is padded after its $m$ coordinates.

The physical source terminal remains


$$
\tau_b=W_b(bz^k_{b-1}+1),
$$


and the physical value remains $z_b^k=0$. The auxiliary completed exterior value is not substituted into the physical reconstruction.

For a relative scalar assertion,


$$
E-r(u)Q
=
2^{-2a-2}\left(2^{a-1}\mathcal V-r(u)\mathcal U\right),
\tag{7.2}
$$


all indicated divisions must still be paid. No higher-depth mixed-source law follows from Theorem 5.1.

Likewise, the logarithmic guard


$$
B_\star=n-v_2(b!)-1-2s_2(n)-\ell
$$


is not strengthened here.

### 7.1 Actual contents and least simultaneous clearer

Retain


$$
\omega_j=j!W_j,\qquad
u_j=\frac{2\Lambda R\,x_j}{\omega_j},\qquad
v_j=\frac{4b!\,y_j}{\omega_j},
$$


and the actual least simultaneous clearer


$$
\boxed{
d_B=\operatorname{lcm}_{0\le j\le b}
\{\operatorname{den}(u_j),\operatorname{den}(v_j)\}.
}
\tag{7.3}
$$



Let $U=d_Bu,\ V=d_Bv$, and let $c_U,c_V$ be their actual contents. The established finite factorial-coordinate identities give


$$
d_B=\operatorname{lcm}(D_\zeta,D_\rho),\qquad
c_U=\frac{d_B}{D_\zeta}c_\zeta,\qquad
c_V=\frac{d_B}{D_\rho},\qquad
\gcd(c_U,c_V)=1.
\tag{7.4}
$$


These remain unchanged.

In particular, the binomial factor in $S$ is not a newly authorized division of either producer column.

### 7.2 Actual all-prime final gcd and denominator

With


$$
\mathcal N=x^Tx,\qquad \mathcal H=x^Ty,
$$


retain


$$
A_B=d_B^2\,4\Lambda^2R^2\mathcal N,\qquad
H_B=d_B^2\,8\Lambda Rb!\mathcal H,
$$




$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
}
\tag{7.5}
$$



For the primitive columns $U^\circ=U/c_U,\ V^\circ=V/c_V$, define


$$
N^\circ=\sum_j\omega_j^2(U^\circ_j)^2,\qquad
H^\circ=\sum_j\omega_j^2U^\circ_jV^\circ_j,
$$


and


$$
\delta_{\rm sc}=\gcd(c_U,|H^\circ|).
$$


Then the established exact formula is


$$
\boxed{
q_n=
\frac{c_U}{\delta_{\rm sc}}\,
\frac{N^\circ}
{\gcd\!\left(N^\circ,\left|c_VH^\circ/\delta_{\rm sc}\right|\right)}.
}
\tag{7.6}
$$



Theorem 5.1 does not estimate either scalar cofactor in (7.6). In particular, it does not overcome the isotropy obstruction to deducing scalar gcd bounds from minor saturation.

The retained original-family ternary law is


$$
\boxed{v_3(q_n)=n-\frac{b+15}{2}.}
\tag{7.7}
$$


Thus the known exponential denominator contribution is still present at every index under discussion.

### 7.3 Whole error at the same original indices

The producer error remains


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


and the relevant whole error is exactly


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
\tag{7.8}
$$



No estimate or nonvanishing theorem for this whole expression is proved here. A proof that the linear acceptance has a large binary divisor is not an estimate for (7.8).

For example, a producer-based irrationality proof would still require


$$
0<|q_n(e+\pi)-p_n|\longrightarrow0
$$


on one and the same infinite set of original indices, using the actual $q_n$ in (7.5), not a binary surrogate.

---

## 8. Bounded new exact arithmetic at $u=0$

No computation has been performed here, and no outcome of the proposed depth-$12$ calculation is assumed.

The new theorem provides a cheap preliminary test that can sometimes settle the depth-$12$ acceptance without a numerical Schur solve.

### 8.1 First test: one actual binomial valuation

Use


$$
b=150094635296999121,\qquad n=4002b,\qquad B=b-1.
$$


Calculate


$$
\boxed{
\chi(0)=s_2(B)+s_2(n)-s_2(n+B).
}
\tag{8.1}
$$



This requires only the binary expansions of three explicitly specified integers. It is not a repetition of the completed content-one dynamic program.

The reviewed endpoint witness already supplies


$$
a(0)\le10.
$$


Consequently, if the new calculation gives


$$
\boxed{\chi(0)\ge11,}
$$


Theorem 5.1 proves


$$
S(0)\equiv0\pmod{4096}
$$


and hence


$$
Q(0)\equiv0\pmod2.
$$



This implication does not require the pending modulo-$8$ review: it uses the independently established upper bound $a(0)\le10$, not the dependent lower bound $a(0)\ge2$.

**Expected verifiable output:** the three exact binary expansions or digit-sum certificates, the integer $\chi(0)$, and the resulting yes/no decision for $\chi(0)\ge11$.

No answer to that calculation is asserted in this report.

### 8.2 If necessary: the complete $L=12$ acceptance

If the first test does not settle the acceptance, retain


$$
L=12,\qquad I=94,\qquad m=44,\qquad T=23.
$$


The complete return can be assembled using only near-terminal coordinates.

Let


$$
j_t=b-m+t,\qquad 0\le t<m.
$$


For the truncated symbol and inverse-symbol coefficients, use the established $\lambda_s,c_s$ modulo $4096$. Define


$$
F_{jv}
=
-\sum_{q=0}^{v}
\binom{-n}{b+q-j}\binom n{v-q},
$$




$$
K_{vt}
=
\lambda_{m+v-t}\binom{b+v}{m+v-t},
$$




$$
G_{tv}
=
\sum_s c_s\binom{j_t}{s}F_{j_t-s,v},
\qquad
\Sigma=I+GK.
\tag{8.2}
$$


Here the $s$-sum uses the retained inverse symbol, and symbol entries outside its retained range are zero modulo $4096$.

Form


$$
q_k=\sum_{i=0}^{94}(-1)^{k-i}\binom ki\mathfrak f_i,
$$


only for


$$
b-88\le k\le b-1.
$$


Then


$$
w_j=\sum_{k=j}^{b-1}\binom{-n}{k-j}q_k,
$$


and


$$
(D_f)_t
=
\sum_s c_s\binom{j_t}{s}w_{j_t-s}.
\tag{8.3}
$$


Every displayed sum is bounded by the stated small near-terminal ranges. No original-length vector or matrix is required.

Solve


$$
\Sigma z=D_f\pmod{4096},
$$


then form


$$
\eta_f=U_n^{(44)}Kz.
\tag{8.4}
$$


The return can be checked in two independently specified ways:


$$
\sum_{v=0}^{43}\mu_{b+v}(\eta_f)_v
\quad\text{and}\quad
\gamma^TKz,
\tag{8.5}
$$


where $\gamma$ is the explicit row (4.2). The two residues must agree.

The source-free norm calculation still uses the full force head and full force return. The fact that a divisibility theorem for the return is now proved does not authorize replacing the return by zero when its residue is needed below that divisor.

### 8.3 Expected certificate

A complete certificate should contain:

1. the paid force seeds and recurrence-generated entries through $i=96$;
2. the original head contribution modulo $4096$;
3. the regrouped recurrence-based head check from §3;
4. $K,G,\Sigma,D_f$ and a verified solution of the $44\times44$ unit system;
5. $\eta_f$;
6. both return evaluations in (8.5);
7. the separate head and return divisibility checks predicted by §§3–4;
8. the final residue $S(0)\pmod{4096}$.

The extra force entries $95,96$ are used to check the actual recurrence-based regrouping; they must not be replaced by artificial terminal values.

Whatever the outcome, this calculation establishes only a fact at $u=0$. It does not establish the infinite paid digit-sum excess lemma of §6.3.

---

## 9. Proof-status ledger and conclusion

| Statement | Status |
|---|---|
| Complete short adjoint and finite Schur completion | Reused established results at paid scope |
| Head denominators $n+r$ canceled using the actual force recurrence | **New proof** |
| Complete return row lies in $2\beta\mathbb Z_2^m$ | **New proof** |
| $v_2(S)\ge1+v_2\binom{n+b-1}{b-1}$ for every original index | **New proved original-family theorem** |
| Paid inequality $v_2(S/2^{a+1})\ge\max(0,\chi-a)$ | **New proved consequence with actual content** |
| Sufficient criterion $\chi\ge A_{\rm end}+1\Rightarrow Q$ even | **New proved conditional implication** |
| Unbounded raw divisibility on specified original classes inside $u\equiv1\pmod4$ | **New proved infinite result** |
| Positive or growing paid excess on infinitely many original indices | **Open** |
| Turn 6-dependent $a\ge2$ on $u\equiv1\pmod4$ | Conditional on pending review; not used here |
| New all-prime scalar-cofactor estimate | Not obtained |
| New $u=0$ binomial-valuation or depth-$12$ numerical outcome | Not supplied; bounded calculation specified |
| Same-index nonzero whole-error estimate | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

The main advance is the complete evaluated divisor


$$
\boxed{
S\in
2\binom{n+b-1}{b-1}\mathbb Z_2.
}
$$


Its proof includes the actual force recurrence, the last-contact boundary, the exterior multiplication matrix, the unit Schur return, and all normalization payments used to reach primitive norm parity.

The precise local bottleneck is now sharper than an unevaluated head-plus-return sum. A sufficient remaining assertion is positivity, on infinitely many original indices, of the explicit quantity


$$
\boxed{
2s_2(4002b)-s_2(4003b-1)-s_2(4001b+3).
}
$$


The report proves unbounded raw divisibility, but not this paid excess.

The global bottleneck is still larger: even an infinite primitive norm-parity theorem would not control the actual all-prime scalar cofactors in $q_n$, would not remove its known ternary exponential factor, and would not establish nonvanishing and decay of the whole error $q_n(e+\pi)-p_n$ at the same indices.

**Accordingly, this turn proves a new complete original-family scalar-divisibility theorem, but does not prove that $e+\pi$ is rational or irrational.**
