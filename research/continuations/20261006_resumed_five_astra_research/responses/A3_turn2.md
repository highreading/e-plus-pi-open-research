> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3, Turn 2 — Removing the diagonal force from the common resultant, and resolving its exceptional moment factor up to polynomial cost

## Executive conclusion

The irrationality or rationality of $e+\pi$ remains unresolved.

A4’s specialized moment–force syzygy and its integer Bézout consequence survive inspection. They use the same linear moment


$$
H=b+(n-3)c-2(n-1)d
$$


as A3 Turn 1, and they retain the exterior $+1$. Their common resultant can indeed be combined with the complete displacement decomposition to eliminate $B_n$ **from the resultant itself**, not merely modulo an endpoint denominator.

The resulting identity is


$$
\boxed{
\mathcal F
=
\frac{D^2L^2}{n+1}\,\Theta,
}
$$


where


$$
\boxed{
\Theta
=
H\!\left((-1)^n n!\mathscr S_n-\tau_nF_n
          +2(n+1)d\,\tau_{n+1}\right)
+(n+1)(2d-c)
 \left(\tau_{n+1}\bigl(2(n-1)d+3c\bigr)-\tau_n(2d-c)\right).
}
\tag{E1}
$$


Here $D=2^n(n+1)!$, $\mathscr S_n=\omega_n+4$, and $F_n=d-c+b/2$. Thus:

- $B_n$ has canceled exactly;
- the complete forced displacement remains;
- the terminal return remains;
- the polynomial terms created by the exterior correction remain;
- no division by $H$ has been performed.

The main further advance is a **two-kernel repair of the exceptional $H$-factor**. Two additional, explicitly evaluated terminal remainders give content bounds with only the polynomial costs


$$
Q_0=n^2+6n+4,\qquad Q_3=n^2+4n+1.
$$


At primes $p>n+2$, the actual structural and complete-force contents can be compared with these evaluated moment/resultant gcds within factors supported on $Q_j$. This yields a new polynomial-distortion description of the actual large-prime endpoint denominators.

This is not a uniform $O(n)$ content estimate. It identifies, more precisely than a common-resultant formula alone, the evaluated gcds that still require an infinite arithmetic theorem.

No accepted computation is requested again. The $n=225$ facts remain finite facts.

---

## 1. Scope and notation

The original families remain


$$
n=15^r,\quad r\ge2,
\qquad\text{and}\qquad
n=105^r,\quad r\ge2.
$$


In particular, every retained $n$ is odd.

The contact matrix remains $3\times3$, with coordinates $0,1,2$. Both reconstructed columns retain coordinates $0,1,2,3$. The complete force ends at exactly $2n+2$.

Write


$$
c_k=[z^k]\left(e^z\left(1-z+\frac{z^2}{2}\right)^n\right),
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
c&b&a\\ d&c&b\\ e_*&d&c
\end{pmatrix},
\qquad \Delta=\det T.
$$



The endpoint rows and reference columns are unchanged:


$$
R_j=\ell_j\operatorname{adj}(T),\qquad
\ell_0=(-1,n,-n(n+1)),\quad \ell_3=(0,0,1),
$$




$$
v=
\begin{pmatrix}1\\1/2\\(n+1)/(2(n+2))\end{pmatrix},
\qquad
w=
\begin{pmatrix}0\\1/2\\(2n+3)/(2(n+2))\end{pmatrix}.
$$


Set


$$
\alpha_j=R_jv,\qquad \beta_j=R_jw.
$$



The actual primitive triples remain


$$
(\gamma_j\mathfrak a_j,\gamma_j\mathfrak b_j,\mathsf E_j)
=
\sigma_j\left(\alpha_j,\beta_j,\frac{N_j^{\exp}}{n!}\right),
$$


with


$$
\gcd(\mathfrak a_j,\mathfrak b_j)=1,\qquad
\gcd(\gamma_j,\mathsf E_j)=1.
$$


In particular, $\mathsf E_j$ is always the evaluated exponential coordinate, including the exterior contribution at endpoint $0$.

Retain


$$
X_j=\mathfrak a_jt_0+\mathfrak b_jt_1,\qquad
M_j=\gamma_jX_j,\qquad
V_j=\gamma_jY_j+L\mathsf E_j.
$$


The actual endpoint denominator is


$$
\boxed{
d_j=\frac{|M_j|}{\gcd(|M_j|,|V_j|)}.
}
\tag{1.1}
$$



I use


$$
\mathcal C_j^\sharp
=
\gcd\bigl(|X_j|,|\mathcal R_j^{(0)}|,|\mathcal R_j^{(1)}|\bigr).
$$


At $p>n+1$, the accepted dual identity gives


$$
v_p(\mathcal C_j^\sharp)=\min\{v_p(X_j),v_p(V_j)\}.
\tag{1.2}
$$



The stronger kernel statements below use $p>n+2$. The possible prime $p=n+2$, and all smaller unselected primes, are not silently discarded.

---

## 2. Assessment of A4’s specialized identities

### 2.1 The syzygy is an identity for the actual complete force

To avoid confusing the coefficient force with the displacement Wronskian, write


$$
f_0=\widehat w_0^{\exp},\qquad f_1=\widehat w_1^{\exp}.
$$


A4’s quantities are


$$
\mathcal P=Hf_0+C,\qquad
\mathcal Q=H(2f_1-f_0)-K^2,
\tag{2.1}
$$


where


$$
K=2d-c,\qquad C=3c^2-2d(b+c).
$$



The vector identity in A4 is


$$
H(\widehat w^{\exp}-T_0)
-K(T_1+nT_0)
=\mathcal Pv+\mathcal Qw.
\tag{2.2}
$$


Both endpoints annihilate $T_1+nT_0$. Also


$$
R_0T_0=-\Delta,\qquad R_3T_0=0.
$$


Multiplication by $R_j$ therefore gives exactly


$$
\boxed{
HN_j^{\exp}=\alpha_j\mathcal P+\beta_j\mathcal Q.
}
\tag{2.3}
$$



This verifies the substantive point: the same subtraction of $T_0$ is valid for **both** endpoints, and at endpoint $0$ it encodes $+\Delta$, hence the exterior $+1$.

The associated determinant identity is also correct:


$$
\boxed{
\alpha_0\beta_3-\beta_0\alpha_3
=
\Delta\,\frac{n+1}{2(n+2)}H.
}
\tag{2.4}
$$



### 2.2 The integer divisibilities have the stated scope

With


$$
D=2^n(n+1)!,\qquad
\mathcal B=n!D^2H,
$$


and


$$
P_0=D^2\mathcal P,\qquad Q_0^{\rm A4}=D^2\mathcal Q,
$$


equation (2.3) gives


$$
\mathcal B\,\mathsf E_j
=
\gamma_j(\mathfrak a_jP_0+\mathfrak b_jQ_0^{\rm A4}).
$$


Primitivity of the **actual** triple consequently proves


$$
\gamma_j\mid\mathcal B.
$$



A4’s explicit integer Bézout identity likewise proves


$$
\mathcal C_j^\sharp\mid G_t\mathcal F.
$$


No additional assertion about the size or support of $\mathcal F$ follows from that divisibility.

The exact law away from $\mathcal B$,


$$
v_p(\mathcal C_j^\sharp)
=
\min\{v_p(X_j),v_p(\mathcal F)\},
\qquad p>n+1,\quad p\nmid\mathcal B,
\tag{2.5}
$$


is valid.

The remaining work is to evaluate $\mathcal F$, and then to repair what happens at $H$.

---

## 3. Exact removal of $B_n$ from $\mathcal F$

### 3.1 Complete displacement decomposition

A3 Turn 1 established


$$
\frac{\widehat w^{\exp}}{n!}
=
B_nv+B_{n+1}w
-\frac{F_n}{2(n+1)n!}a_\partial,
\qquad
a_\partial=
\begin{pmatrix}0\\1\\1/(n+2)\end{pmatrix},
\tag{3.1}
$$


where


$$
F_n=d-c+\frac b2.
$$


Thus


$$
f_0=n!B_n,
\qquad
2f_1-f_0=n!B_{n+1}-\frac{F_n}{n+1}.
\tag{3.2}
$$



The complete displacement is


$$
\mathscr S_n=\omega_n+4,
$$


with


$$
\omega_n=(-1)^n(n+1)
(\tau_nB_{n+1}-\tau_{n+1}B_n).
$$


Its recurrence retains all three forcing terms:


$$
\mathscr S_{m+1}
=
\mathscr S_m+(-1)^{m+1}\tau_{m+1}\psi_m,
$$




$$
\psi_m=
\frac{(m+1)(m+2)E_m+2(m+2)G_m+E_{m+1}}
{(m+2)((m+1)!)^2}.
\tag{3.3}
$$


The initial value remains $\mathscr S_0=6$.

### 3.2 Cancellation inside the common resultant

A4’s common resultant is


$$
\mathcal F
=
D^2L^2
\left(
\tau_n\mathcal Q-\tau_{n+1}\mathcal P
+\frac{4(-1)^n n!H}{n+1}
\right).
\tag{3.4}
$$


Substituting (3.2) into (2.1) gives


$$
\begin{aligned}
\tau_n\mathcal Q-\tau_{n+1}\mathcal P
={}&
n!H(\tau_nB_{n+1}-\tau_{n+1}B_n)\\
&-\frac{\tau_nHF_n}{n+1}
-\tau_nK^2-\tau_{n+1}C.
\end{aligned}
$$


The Wronskian and the complete logarithmic restoration therefore give


$$
\boxed{
\frac{\mathcal F}{D^2L^2}
=
\frac{(-1)^n n!H\mathscr S_n}{n+1}
-\frac{\tau_nHF_n}{n+1}
-\tau_nK^2-\tau_{n+1}C.
}
\tag{3.5}
$$



This is the requested cancellation of $B_n$ from $\mathcal F$ itself.

The cancellation is exact. It is not an estimate based on the real size of $B_n$, and it does not remove the forced displacement.

### 3.3 A form adapted to the exceptional moment

Introduce


$$
J=2(n-1)d+3c=(n-1)K+(n+2)c.
$$


The moment identities give


$$
b=H+(n-1)K+2c,\qquad
F_n=\frac{H+nK+c}{2},
\tag{3.6}
$$


and


$$
C=-2dH-KJ.
\tag{3.7}
$$


Consequently (3.5) becomes (E1):


$$
\boxed{
\mathcal F=\frac{D^2L^2}{n+1}\Theta,
}
\tag{3.8}
$$




$$
\boxed{
\Theta
=
H\left((-1)^n n!\mathscr S_n-\tau_nF_n
+2(n+1)d\,\tau_{n+1}\right)
+(n+1)K(\tau_{n+1}J-\tau_nK).
}
\tag{3.9}
$$



In particular,


$$
\boxed{
\Theta\equiv
(n+1)K(\tau_{n+1}J-\tau_nK)\pmod H.
}
\tag{3.10}
$$


There is no universal additional factor $H$ to divide out.

---

## 4. Denominator audit

Let


$$
\mathfrak M=\frac{D^2L^2}{n+1}.
$$


This is an integer, and


$$
v_p(\mathfrak M)=2v_p(D)+2v_p(L)-v_p(n+1).
\tag{4.1}
$$


Equation (3.8) is the exact equality


$$
\mathcal F=\mathfrak M\Theta.
$$


Thus for every prime, with the usual convention for zero,


$$
v_p(\mathcal F)=v_p(\mathfrak M)+v_p(\Theta).
\tag{4.2}
$$


At $p>n+1$, $\mathfrak M$ is a unit.

A useful explicit integrality check is obtained by defining


$$
\Xi=(-1)^n n!\mathscr S_n-\tau_nF_n+(n+1)\tau_{n+1}c.
\tag{4.3}
$$


Equations (3.2)–(3.3) imply


$$
\boxed{
\frac{\Xi}{n+1}
=
\tau_n(2f_1-f_0)-\tau_{n+1}(f_0-c)
+\frac{4(-1)^n n!}{n+1}.
}
\tag{4.4}
$$


Since $D$ clears $f_0,f_1,c$, and $L$ clears the reference values,


$$
DL\,\frac{\Xi}{n+1}\in\mathbb Z.
\tag{4.5}
$$



This proves integrality of the denominator-cleared expressions used below directly from the retained finite force.

No cost from $\operatorname{den}(B_n)$ is needed in (3.8): $B_n$ has canceled before the final clearing. If one instead performs the endpoint Bézout subtraction involving $B_n$, the earlier cost


$$
\operatorname{den}(B_n)\mid 2^n(n!)^2
$$


still applies. These are different operations and should not be conflated.

---

## 5. The common resultant is a terminal determinant for a common kernel column

The exterior-corrected complete column


$$
\boxed{
s=\frac{\widehat w-T_0}{n!}
}
\tag{5.1}
$$


works for both endpoints:


$$
R_js=\frac{N_j}{n!},\qquad j=0,3.
$$


Put


$$
t=\tau_nv+\tau_{n+1}w,
$$


and


$$
q_\partial=
\begin{pmatrix}
n+2\\-2(2n+3)\\2(n+2)
\end{pmatrix}.
$$


Then


$$
q_\partial^Tv=q_\partial^Tw=0,\qquad
q_\partial^Ta_\partial=-4(n+1).
$$



The common kernel column is


$$
k_H=T_1+nT_0.
$$


Using the actual moment recurrence,


$$
\boxed{
k_H=(H+J)v+Kw-\frac H2a_\partial.
}
\tag{5.2}
$$


In particular,


$$
q_\partial^Tk_H=2(n+1)H.
$$



A direct determinant calculation from (3.1) and the complete logarithmic contribution gives


$$
\boxed{
\Theta=2(n+2)n!\det(t,s,k_H).
}
\tag{5.3}
$$



Thus A4’s common resultant is exactly a rescaled instance of A3’s terminal-determinant construction. It is not a separate generic gcd object.

The exceptional factor $H$ appears because $k_H$ can become tangent to the reference plane $\operatorname{span}(v,w)$. The next step is therefore to retain a second actual kernel column rather than divide by $H$.

---

## 6. Two evaluated alternative terminal remainders

Define the moment defects


$$
B_0^\partial=6d-(n+6)c=3K-(n+3)c,
$$




$$
B_3^\partial=2(n+2)d-(n+3)c=(n+2)K-c.
\tag{6.1}
$$



Use the following kernel columns:


$$
k_0=T_2+(n+2)T_1+nT_0,
\qquad
k_3=T_1-(n+2)T_0.
\tag{6.2}
$$


They satisfy


$$
R_0k_0=0,\qquad R_3k_3=0,
$$


and


$$
q_\partial^Tk_j=2(n+1)B_j^\partial.
\tag{6.3}
$$



Their complete evaluations in the basis $v,w,a_\partial$ are


$$
k_j=A_j^\partial v+B_j^{\rm coord}w
-\frac{B_j^\partial}{2}a_\partial,
\tag{6.4}
$$


where


$$
\begin{array}{c|cc}
j&A_j^\partial&B_j^{\rm coord}\\ \hline
0&
3H+(4n-2)K+(2n+5)c&
(3-n)K-H\\[1mm]
3&
H+(n-1)K-nc&
-H-(n-1)K-c.
\end{array}
\tag{6.5}
$$



Define


$$
\boxed{
\Theta_j
=
B_j^\partial\Xi
-(n+1)K
\left(\tau_nB_j^{\rm coord}
-\tau_{n+1}A_j^\partial\right).
}
\tag{6.6}
$$


Then


$$
\boxed{
\Theta_j=2(n+2)n!\det(t,s,k_j).
}
\tag{6.7}
$$



The corresponding integer remainders are


$$
\boxed{
\mathcal F_j^{\rm alt}
=\mathfrak M\Theta_j\in\mathbb Z.
}
\tag{6.8}
$$


Integrality follows from (4.5), because $D$ clears every moment expression in (6.5)–(6.6).

These formulas contain only:

- the complete displacement $\mathscr S_n$;
- the terminal coefficient $F_n$;
- the actual moment defects;
- the reference values;
- the exterior-correction terms carried by $K$ and $\Xi$.

They contain no $B_n$, and no omitted endpoint correction.

---

## 7. The actual exponential coordinate does not erase large-prime structural content

This point strengthens A3 Turn 1 and is important for avoiding free-triple reasoning.

Choose a primitive integral row $r_j$ with


$$
R_j=\chi_jr_j.
$$


For $p>n+2$, let


$$
m_j=\min\{v_p(r_jv),v_p(r_jw)\},
$$


and


$$
\delta_j=
\min\left\{
v_p(r_jv),v_p(r_jw),
v_p\!\left(r_j\frac{\widehat w^{\exp}-T_0}{n!}\right)
\right\}.
$$


The actual triple normalization gives


$$
v_p(\gamma_j)=m_j-\delta_j.
$$



### Theorem 7.1 — No large-prime loss from primitivizing the third coordinate

For every original-family index and every $p>n+2$,


$$
\boxed{\delta_j=0,\qquad v_p(\gamma_j)=m_j.}
\tag{7.1}
$$



### Proof

If $m_j=0$, the assertion is immediate.

Suppose $m_j>0$. Since $r_j$ is primitive and annihilates $v,w$ modulo $p$, it is a unit multiple of $q_\partial^T$ modulo $p$. Its exact kernel columns then imply


$$
H\equiv B_j^\partial\equiv0\pmod p.
$$


The coefficient recurrence proves that $(b,c,d)$ is primitive at $p$. As in A3 Turn 1, $c$ is therefore a unit.

For $j=3$,


$$
K\equiv\frac{c}{n+2}\pmod p.
$$


For $j=0$,


$$
K\equiv\frac{n+3}{3}c\pmod p.
$$


Both are units. For the second statement, note that $n$ is odd: a prime $p>n+2$ cannot divide the even integer $n+3$.

The complete exponential column satisfies


$$
\boxed{
q_\partial^T
\frac{\widehat w^{\exp}-T_0}{n!}
=
\frac{2(n+1)K}{n!}.
}
\tag{7.2}
$$


Its right side is a unit. Hence the actual third output is a unit, so $\delta_j=0$. ∎

This is an evaluated-force statement. In particular, large structural content cannot be made harmless by supposing that the actual exponential coordinate shares and removes it.

---

## 8. Structural contents are equivalent to the two defect gcds up to polynomial factors

Set


$$
\boxed{
Q_0=n^2+6n+4,\qquad Q_3=n^2+4n+1.
}
\tag{8.1}
$$


For $p>n+2$, put


$$
e_j(p)=\min\{v_p(H),v_p(B_j^\partial)\},
\qquad g_j(p)=v_p(\gamma_j).
$$



A3 Turn 1 gave $g_j(p)\le e_j(p)$. The reverse estimate has only polynomial cost.

### Theorem 8.1 — Polynomial-cost structural equivalence



$$
\boxed{
\max\{0,e_j(p)-v_p(Q_j)\}
\le g_j(p)\le e_j(p).
}
\tag{8.2}
$$



### Proof

Only $e=e_j(p)>0$ needs consideration. The moment state is congruent modulo $p^e$ to the corresponding projective direction, with $c$ a unit.

At those directions, direct evaluation of the actual adjugate rows gives


$$
R_0\equiv
c^2\frac{n(n+3)Q_0}{36(n+2)}q_\partial^T
\pmod{p^e},
\tag{8.3}
$$




$$
R_3\equiv
-c^2\frac{Q_3}{4(n+2)^3}q_\partial^T
\pmod{p^e}.
\tag{8.4}
$$


All displayed factors other than $Q_j$ are units at the primes under consideration.

If $e>v_p(Q_j)$, the content of the raw row $R_j$ is exactly $v_p(Q_j)$. Its two outputs against $v,w$ have valuations at least $e$. Dividing by the row content therefore gives


$$
m_j\ge e-v_p(Q_j).
$$


Theorem 7.1 identifies $m_j$ with $g_j(p)$. If $e\le v_p(Q_j)$, the lower bound is trivial. ∎

Let $U_j$ be the large-prime defect gcd from A3 Turn 1:


$$
U_j=
\gcd\bigl(|D_{\rm mom}H|,
          |D_{\rm mom}B_j^\partial|\bigr)_{>n+2},
\qquad
D_{\rm mom}=2^n(n+2)!.
$$


Then


$$
\boxed{
(\gamma_j)_{>n+2}\mid U_j
\mid (Q_j)_{>n+2}(\gamma_j)_{>n+2}.
}
\tag{8.5}
$$



Thus the linear-moment gcd obstruction is not merely a loose upper bound. Apart from polynomial factors, it is the actual structural content.

The earlier shared-factor improvement remains:


$$
\boxed{
U_0U_3
\mid
\left((n^2+5n+3)\,|\operatorname{num}(H)|\right)_{>n+2}.
}
\tag{8.6}
$$



---

## 9. Repairing the exceptional $H$-factor in the complete-force content

### 9.1 Exact denominator cost in A4’s single-resultant law

For completeness, A4’s transformation also gives an exact description at primes dividing $H$.

Let $p>n+1$, and write


$$
x=v_p(X_j),\quad f=v_p(\mathcal F),\quad
h=v_p(H),\quad g=v_p(\gamma_j),\quad v=v_p(V_j).
$$


Assume $H\ne0$. Since


$$
v_p(\mathcal B/\gamma_j)=h-g,
$$


the same unimodular two-form argument gives


$$
\boxed{
\min(x,f)=\min(x,h-g+v).
}
\tag{9.1}
$$



If $g>0$, then $V_j$ is a unit, so


$$
v_p(\mathcal C_j^\sharp)=0.
$$


If $g=0$, equation (9.1) shows explicitly the possible extra $H$-depth in $\gcd(X_j,\mathcal F)$.

This is the precise obstruction to applying A4’s law at $H$ without modification.

### 9.2 Retaining the second kernel removes that obstruction up to $Q_j$

Remove from $|X_j|$ the entire factors supported on primes dividing $\gamma_j$:


$$
X_j^\circ
=
\frac{|X_j|}
{\prod_{p\mid\gamma_j}p^{v_p(X_j)}}.
\tag{9.2}
$$


This is not a change of the actual row or denominator. It is an auxiliary integer used only in the next gcd.

Define


$$
\boxed{
\mathfrak D_j
=
\gcd\bigl(
X_j^\circ,\,
|\mathcal F|,\,
|\mathcal F_j^{\rm alt}|
\bigr)_{>n+2}.
}
\tag{9.3}
$$



### Theorem 9.1 — Two-kernel complete-content equivalence



$$
\boxed{
(\mathcal C_j^\sharp)_{>n+2}
\mid\mathfrak D_j
\mid
(Q_j)_{>n+2}(\mathcal C_j^\sharp)_{>n+2}.
}
\tag{9.4}
$$



In particular, outside the prime support of $Q_j$, this is an exact content formula, including primes dividing $H$.

### Proof

Fix $p>n+2$.

If $p\mid\gamma_j$, the actual $\mathsf E_j$ is a unit, so $V_j$ is a unit and $\mathcal C_j^\sharp$ has valuation zero. The definition of $X_j^\circ$ also makes $\mathfrak D_j$ a unit.

Suppose $p\nmid\gamma_j$. By Theorem 7.1, the pair


$$
(r_jv,r_jw)
$$


is primitive over $\mathbb Z_p$.

If $p\nmid X_j$, there is nothing to prove. Otherwise, complete $t$ to a basis


$$
t,z,a_\partial,
\qquad z\in\operatorname{span}_{\mathbb Z_p}(v,w),
$$


of unit determinant. Then $r_jz$ is a unit.

Write a kernel column $k$ and the complete column $s$ in this basis. Since $r_jk=0$, reduction modulo $r_jt$ gives


$$
\det(t,s,k)
\equiv u\,k_a\,r_js\pmod{r_jt},
$$


where $u$ is a unit and $k_a$ is the $a_\partial$-coordinate of $k$.

For $k_H$ and $k_j$, those coordinates are respectively


$$
-\frac H2,\qquad -\frac{B_j^\partial}{2}.
$$


Using (5.3), (6.7), and the fact that all clearing factors are units at $p$, we obtain


$$
\boxed{
\min\{v_p(X_j),v_p(\mathcal F),v_p(\mathcal F_j^{\rm alt})\}
=
\min\{x,e_j(p)+v_p(V_j)\}.
}
\tag{9.5}
$$


Meanwhile


$$
v_p(\mathcal C_j^\sharp)=\min\{x,v_p(V_j)\}.
$$


The difference between these two valuations lies between $0$ and $e_j(p)$. Because $g_j(p)=0$, Theorem 8.1 gives


$$
e_j(p)\le v_p(Q_j).
$$


This proves (9.4). ∎

### Consequence

The unresolved common-resultant gcd has now been sharpened from


$$
\gcd(X_j,\mathcal F)\quad\text{away from }H
$$


to the fully evaluated three-generator gcd


$$
\gcd(X_j^\circ,\mathcal F,\mathcal F_j^{\rm alt}),
$$


with only a polynomial exceptional cost.

This does **not** show that the gcd is small. It does show that the potentially large $H$-factor is no longer an unaccounted denominator cost.

---

## 10. A polynomial-distortion formula for the actual large-prime denominators

The preceding results can be combined without replacing the actual row contents.

Define


$$
\boxed{
\widehat K_j
=
\frac{U_j\,|X_j|_{>n+2}}{\mathfrak D_j}.
}
\tag{10.1}
$$


This is an integer because $\mathfrak D_j\mid X_j^\circ\mid |X_j|$.

### Theorem 10.1 — Actual denominator comparison



$$
\boxed{
(d_j)_{>n+2}\mid\widehat K_j
\mid (Q_j)_{>n+2}(d_j)_{>n+2}.
}
\tag{10.2}
$$



### Proof

At $p>n+2$, write


$$
g=v_p(\gamma_j),\quad x=v_p(X_j),\quad
c_*=v_p(\mathcal C_j^\sharp),\quad
e=e_j(p),\quad z=v_p(\mathfrak D_j).
$$


The actual denominator has exponent


$$
v_p(d_j)=g+x-c_*.
$$


The auxiliary integer has exponent


$$
v_p(\widehat K_j)=e+x-z.
$$



If $g>0$, then $z=c_*=0$, and the difference is $e-g$, which lies in $[0,v_p(Q_j)]$.

If $g=0$, equation (9.5) gives


$$
0\le z-c_*\le e.
$$


Thus


$$
v_p(\widehat K_j)-v_p(d_j)=e-(z-c_*)
$$


also lies in $[0,e]\subseteq[0,v_p(Q_j)]$. ∎

Let


$$
\widehat Z
=
\frac{\widehat K_0\widehat K_3}
{\gcd(\widehat K_0,\widehat K_3)^2}.
$$


Because the actual endpoint imbalance is


$$
v_p(|AB|)=|v_p(d_0)-v_p(d_3)|,
$$


Theorem 10.1 gives


$$
\boxed{
\left|
v_p(|AB|)-v_p(\widehat Z)
\right|
\le v_p(Q_0Q_3),
\qquad p>n+2.
}
\tag{10.3}
$$


Consequently,


$$
\boxed{
\log|AB|_{>n+2}
=
\log\widehat Z+O(\log n).
}
\tag{10.4}
$$



This is a new polynomial-distortion reduction of the **actual** large-prime denominator imbalance. It improves the nature of the reduction, but does not estimate $\widehat Z$.

In particular, neither (10.4) nor the large finite value at $n=225$ proves an infinite growth theorem.

---

## 11. What remains of the support problem

The strong original-family assertion


$$
(\mathcal C_j^\sharp)_{>n+1}=1
$$


has not been proved or disproved here.

For $p>n+2$ outside $Q_j$, Theorem 9.1 now gives the exact criterion


$$
\boxed{
p\mid\mathcal C_j^\sharp
\iff
p\mid X_j^\circ,\quad
p\mid\mathcal F,\quad
p\mid\mathcal F_j^{\rm alt}.
}
\tag{11.1}
$$


At primes dividing $H$, the second evaluated kernel—not a formal division by $H$—is what repairs the criterion.

Moreover, Theorems 8.1 and 9.1 show


$$
\begin{aligned}
&\log(U_0U_3\mathfrak D_0\mathfrak D_3)\\
&\qquad=
\log\bigl((\gamma_0\gamma_3
\mathcal C_0^\sharp\mathcal C_3^\sharp)_{>n+2}\bigr)
+O(\log n).
\end{aligned}
\tag{11.2}
$$


Thus these evaluated gcds are, up to polynomial factors, the actual content obstruction. There is no remaining factorial-sized normalization loss hidden in this large-prime comparison.

A concrete sufficient follow-on lemma is now:

> **Fixed-seed two-kernel content lemma.**  
> On infinitely many indices in one retained original family, prove a suitable bound for
> 

$$
> U_0U_3\mathfrak D_0\mathfrak D_3,
>
$$


> or prove a direct lower bound for the imbalance $\widehat Z$, while separately controlling the actual contribution from primes $p\le n+2$ outside the selected set.

An $O(n)$ logarithmic bound for the displayed content product would be sufficient for the corresponding content step. It is not established here.

The missing input is arithmetic of the **fixed initial exponential solution** under the actual coefficient and displacement recurrences. Real asymptotics of $\mathscr S_n$, $H$, or the terminal determinants do not bound their reduced numerator gcds.

---

## 12. A limited recurrence-compatible counterexample

There is a useful rigorous distinction between:

1. a support theorem for the original fixed finite exponential force; and
2. a support theorem inferred only from the diagonal forced recurrence and the terminal return.

The second, stronger assertion is false.

The following small exact example is **not** an original-family counterexample and does **not** use the original exponential initial condition. Its scope is explicitly limited to the diagonal recurrence, its complete forcing $\psi_m$, and the contact terminal relation.

Take $n=2$, with the actual moments


$$
b=-1,\qquad c=\frac12,\qquad d=\frac16,
\qquad
H=-\frac{11}{6},\qquad F_2=-\frac56.
$$


The actual endpoint-$0$ coefficients are


$$
\alpha_0=-\frac43,\qquad \beta_0=-\frac{11}{8}.
$$



Modify the diagonal solution by the homogeneous companion


$$
B_m^\dagger=B_m+6\rho_m.
\tag{12.1}
$$


This leaves **every** $\psi_m$ unchanged. It changes the initial value $B_1$ from $3$ to $9$, while leaving $B_0=1$.

Construct the contact force from $B_n^\dagger,B_{n+1}^\dagger$ using the same complete decomposition and the same terminal coefficient. At $n=2$, it is


$$
\widehat w^{\exp,\dagger}
=
\left(\frac{57}{2},\frac{133}{3},\frac{505}{8}\right)^T.
$$


It satisfies


$$
4\widehat w_2^{\exp,\dagger}
=
7\widehat w_1^{\exp,\dagger}
-2\widehat w_0^{\exp,\dagger}
-\frac56.
$$


The exterior $+\Delta$ is retained, and the resulting actual modified third coordinate is


$$
\frac{N_0^{\exp,\dagger}}{2!}
=-\frac{1441}{24}.
$$


Hence its primitive triple is exactly


$$
(-32,-33,-1441),\qquad \gamma_0^\dagger=1.
$$



With the unchanged reference normalization


$$
L=48,\quad t_0=96,\quad t_1=192,\quad
r_0=288,\quad r_1=608,
$$


one gets


$$
X_0^\dagger=-9408,\qquad V_0^\dagger=-98448,
$$


and


$$
\boxed{
\mathcal C_0^{\sharp,\dagger}=1344,
\qquad
(\mathcal C_0^{\sharp,\dagger})_{>4}=7.
}
\tag{12.2}
$$



Thus the diagonal recurrence with its complete forcing and terminal return does not, by itself, imply large-prime support $1$.

**Exact limitation.** The modified contact force is not the original finite exponential sum generated by $e^z/(1-z)$; its initial exponential boundary has changed. Therefore this example does not disprove the original-family support assertion. It identifies precisely why an original-family proof must use the fixed exponential boundary, not just the displayed diagonal recurrence.

No free coefficient triple was chosen: the third coordinate above was evaluated from the modified recurrence-compatible force, with the exterior correction included.

---

## 13. The completed $n=225$ evidence remains unchanged

The supplied finite audit retains:

- all eight reconstructed entries;
- the least common clearer over those eight entries;
- all four row contents
  

$$
(508500,\ 28350,\ 15525,\ 772);
$$


- complete force through $452$;
- the exterior $+1$;
- all-prime primitive reductions.

At that one index,


$$
(\gamma_0)_{>226}=(\gamma_3)_{>226}
=(\mathcal C_0^\sharp)_{>226}
=(\mathcal C_3^\sharp)_{>226}=1,
$$


and $|AB|_{>226}$ has $2314$ digits.

The whole-form conclusions also remain:


$$
\begin{array}{c|r|r}
\text{weight}&\text{sign}&
\lfloor\log_{10}|\text{whole form}|\rfloor\\ \hline
0&-&1815\\
1&-&1817\\
1/2&-&2976\\
n^2/2&+&2974\\
\text{reference-canceling}&-&1290.
\end{array}
$$


All five are rigorously nonzero and greater than $1$ in absolute value.

These facts neither establish an infinite support theorem nor a successful irrationality sequence. In particular, reference cancellation does not cancel the whole error.

I do not request the producer, force generation, dual-content processing, enclosure calculation, or A4’s already assigned new post-processing again.

---

## 14. Actual primitive denominator and same-index whole error

None of the new auxiliary gcds changes the original normalization.

For a reduced weight $\lambda=a/k$, $k>0$, retain


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


The actual primitive pair is still


$$
\boxed{
q_\lambda=
\frac{kh|AB|}{F_{\rm gcd}GH_{\rm gcd}},
\qquad
p_\lambda=
\operatorname{sgn}(AB)
\frac{T_{\rm wt}}{F_{\rm gcd}GH_{\rm gcd}}.
}
\tag{14.1}
$$


Every prime remains in the final gcd.

The same-index whole error is still


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda e_3\alpha_{n,2}
(\lambda-\Lambda_{n,2}).
}
\tag{14.2}
$$


An irrationality proof requires an infinite sequence for which


$$
\boxed{
0<
q_\lambda|e_3\alpha_{n,2}|
\,|\lambda-\Lambda_{n,2}|
\longrightarrow0.
}
\tag{14.3}
$$


No theorem in this report establishes that condition.

---

## 15. Proof status and bounded verification

### 15.1 Status ledger

| Statement | Status |
|---|---|
| A4’s actual moment–force syzygy, including exterior correction | Verified algebraically |
| A4’s integer Bézout divisor and exact law away from $\mathcal B$ | Valid at stated hypotheses |
| Removal of $B_n$ from $\mathcal F$ itself | Proved in §3 |
| Exact denominator-cleared surviving resultant | Proved in §§3–4 |
| Common resultant as a common-kernel terminal determinant | Proved in §5 |
| Two evaluated alternative terminal remainders | Proved in §6 |
| No large-prime primitivization loss from the actual exponential coordinate | Proved in §7 |
| Structural defect gcd versus $\gamma_j$, within $Q_j$ | Proved in §8 |
| Two-kernel gcd versus $\mathcal C_j^\sharp$, within $Q_j$ | Proved in §9 |
| Actual large-prime denominator imbalance within polynomial distortion | Proved in §10 |
| Infinite original-family support or $O(n)$ content bound | Open |
| Original-family strong support assertion disproved | No |
| Recurrence-only support assertion | Refuted at the exact limited scope of §12 |
| Successful primitive whole-error sequence | Open |

### 15.2 New bounded arithmetic, without repeating accepted work

No further producer calculation is needed for the proofs above.

A genuinely new finite symbolic verification can use


$$
\mathbb Q(n,b,c,d,\tau,\tau_1,\mathscr S)
$$


with


$$
a=2(n+1)d-2c-(n-1)b,\qquad
e_*=\frac{4d+(n-2)c+b}{2(n+2)}.
$$


Its inputs are the displayed definitions of $T,v,w,a_\partial$, $H,K,J,F_n$, and the three kernel columns $k_H,k_0,k_3$.

The expected verifiable outputs are exact zero residuals for:

1. the three basis decompositions (5.2), (6.4)–(6.5);
2. the determinant identities (5.3), (6.7), using the full force decomposition;
3. the two projective row evaluations (8.3)–(8.4);
4. the equality between (3.5) and (3.8)–(3.9).

The small recurrence-compatible example has the exact expected gcd output


$$
\gcd\bigl(9408,\,
|96(-98448)-288(-9408)|,\,
|192(-98448)-608(-9408)|\bigr)=1344.
$$


This verifies only that limited example, not an original-family statement.

No execution is represented as having occurred here.

---

## Conclusion

The new target-specific result is not merely another divisor bound for a common resultant.

First, the homogeneous diagonal has been removed from A4’s common resultant exactly:


$$
\boxed{
\mathcal F
=
\frac{D^2L^2}{n+1}
\left[
H\left((-1)^nn!\mathscr S_n-\tau_nF_n
+2(n+1)d\tau_{n+1}\right)
+(n+1)(2d-c)
\left(\tau_{n+1}(2(n-1)d+3c)-\tau_n(2d-c)\right)
\right].
}
$$



Second, the actual coefficient recurrence and the evaluated kernel columns repair the exceptional $H$-factor. The remaining structural and complete-force gcds agree with the actual contents up to the polynomial factors


$$
n^2+6n+4,\qquad n^2+4n+1.
$$


This produces the rigorous comparison


$$
\boxed{
\log|AB|_{>n+2}=\log\widehat Z+O(\log n),
}
$$


with $\widehat Z$ defined by explicit evaluated moment and complete-terminal gcds.

The exact remaining bottleneck is an infinite arithmetic estimate for those fixed-seed gcds—or a direct imbalance theorem for $\widehat Z$—together with the unselected primes at most $n+2$. Even that would still have to be combined with the actual all-prime primitive denominator and the same-index whole-error criterion.



$$
\boxed{\text{The irrationality or rationality of }e+\pi\text{ remains unresolved.}}
$$


