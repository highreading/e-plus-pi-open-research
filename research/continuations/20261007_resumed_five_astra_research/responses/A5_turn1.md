> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5 Turn 1 — Cancellation of the exceptional coefficient, integral boundary completion, and a smaller paid reduction

## Executive summary

The rationality or irrationality of $e+\pi$ remains unresolved.

This report establishes a cancellation that the previous ten-master theorem did not establish:

> **For the actual assembled norm and complete exponential response, the exceptional type-$11$ master coefficient is zero.**  
> This holds before its computational denominator is divided out.

The reason is not a relation between unevaluated master moments. It is a finite Vandermonde cancellation inside the inverse-profile correction terms. After that cancellation, each reconstructed type-$1$ profile has polynomial degree at most $2D$ relative to the previous common baseline. Its type-$11$ product therefore has degree at most $4D$, below the exceptional degree $4D+5$.

There is a stronger, integral reformulation of the **actual finite solve**:

> By completing an auxiliary transformed vector only through its necessary exterior coordinates, and then normal-ordering the two inverse binomial factors, the complete first-force and exponential profiles can be represented using **type-$2$ atoms only**, modulo the paid raw precision.

The exterior coefficients are given explicitly below. They retain:

- the normalized force $\mathfrak f=f^0/R$;
- the full Schur return;
- the complete factorial source prefix;
- the finite contact return $F_{\cdot t}$;
- both source boundaries $C_{b-1},C_b$;
- the physical endpoint, including both terms
  

$$
W_b^2\,b z^f_{b-1}\bigl(bz^k_{b-1}+1\bigr).
$$



The integral change of representation itself introduces **no nonunit division**. A subsequent polynomial-adjoint reduction needs only three common moments, with a new computational clearer that divides the old type-$22$ clearer.

This is a genuine reduction of the additional arithmetic loss for the actual assembled objects. It is **not yet a practical primitive-digit algorithm**: the remaining moments still involve $0\le j<b$, the full original word, and potentially substantial extra precision.

A further original-family result classifies the large-offset losses in the new clearer. For example, at raw precision $L=32$, on the infinite original subdomain


$$
u\equiv1\pmod2,
$$


the two new computational losses are exactly


$$
\boxed{e_Q=3497,\qquad e_E=2735.}
$$


These are losses of the specified computational certificates, not valuations of $Q,E$, not producer contents, and not primitive-denominator data.

---

## 1. Preserved objects and scope

Throughout,


$$
\boxed{b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.}
$$


The contact matrix has exactly the indices


$$
0\le i,j<b,
$$


and physical reconstruction has exactly the rows


$$
0\le j\le b.
$$



Set


$$
h=\frac n2,\qquad
R=2^h\binom nh,\qquad
\Lambda=\frac{(n!)^2}{2^n},
$$




$$
\phi(z)=1-z+\frac{z^2}{2},\qquad
\lambda_s=s![z^s]\phi(z)^n,\qquad
W_j=\binom{n+2}{j}.
$$



The finite matrix and first force are


$$
A_{ij}
=
\sum_{s=0}^{n+i}
\lambda_s\binom{n+i}{s}\binom{2n+i-s}{j},
$$




$$
f_i^0
=
\frac{(n+i)!}{n!}
[t^n](1+2t+2t^2)^n(1+t)^i.
$$


Write


$$
\mathfrak f=f^0/R.
$$



For a contact vector $z$,


$$
(\mathcal Rz)_j=W_j(jz_{j-1}-z_j),
\qquad z_{-1}=z_b=0.
$$


The corrected columns remain


$$
x=\frac{\mathcal RA^{-1}f^0}{2R}
  =\frac12\mathcal RA^{-1}\mathfrak f,
$$




$$
y=\frac{\mathcal RA^{-1}(h^e+h^F)+e_0}{4b!}.
$$



Let


$$
x=2^ax_0,\qquad
\mathcal B=A^{-T}\mathcal R^T\mathcal RA^{-1},
$$




$$
k=\frac{h^e-A(j!)_{0\le j<b}}{b!},
\qquad
v_{\rm term}=bW_b^2A^{-T}e_{b-1}.
$$


Then


$$
Q=x_0^Tx_0
  =2^{-2a-2}\mathfrak f^T\mathcal B\mathfrak f,
$$




$$
E=x_0^Ty^E
  =2^{-a-3}\mathfrak f^T(\mathcal Bk+v_{\rm term}).
$$



For convenience, put


$$
z^f=A^{-1}\mathfrak f,\qquad z^k=A^{-1}k.
$$


Their raw pairings are


$$
\mathfrak f^T\mathcal B\mathfrak f
=
\sum_{j=0}^{b-1}W_j^2(\Delta_jz^f)^2
+
b^2W_b^2(z^f_{b-1})^2,
\tag{1.1}
$$


and


$$
\begin{aligned}
\mathfrak f^T(\mathcal Bk+v_{\rm term})
={}&
\sum_{j=0}^{b-1}W_j^2
(\Delta_jz^f)(\Delta_jz^k)\\
&+
\boxed{W_b^2\,b z^f_{b-1}(bz^k_{b-1}+1)}.
\end{aligned}
\tag{1.2}
$$


Here $\Delta_jz=jz_{j-1}-z_j$.

The two terms in the boxed terminal are both compulsory.

### 1.1 Reused mathematics

The supplied derivations establish, on the original family,


$$
\mathfrak f_i\in\mathbb Z_2,\qquad
v_2(\mathfrak f_i)\ge\left\lfloor\frac{i+1}{8}\right\rfloor.
$$


At raw precision $2^L$, retain


$$
I=\min(b-1,8L-2),\qquad
m=4(L-1),\qquad
d=\min(m,b),
$$




$$
T=\min(2L-1,2n-1).
\tag{1.3}
$$


The symbol and inverse-symbol coefficients satisfy


$$
\lambda_s\equiv c_s\equiv0\pmod{2^L}\quad(s>m),
$$


where


$$
c_0=1,\qquad
c_s=-\sum_{r=1}^s\binom sr\lambda_rc_{s-r}.
$$



The complete exponential source is still


$$
k=\sum_{t=0}^{2n-1}\frac{(b+t)!}{b!}\,\mathbf a_{b+t},
$$


and its paid prefix is


$$
k\equiv\sum_{t=0}^{T}a_t\mathbf a_{b+t}\pmod{2^L},
\qquad
a_t=\frac{(b+t)!}{b!}.
\tag{1.4}
$$



The supplied finite audits validate their listed finite cases. The symbolic $D=1$ certificate validates its polynomial identity for symbolic $b$. Neither audit supplies a primitive digit or an infinite-family valuation theorem.

The strengthened rational rank obstruction


$$
\operatorname{rank}_{\mathbb Q}
\bigl((\mathcal R^T\mathcal R)J-J^T(\mathcal R^T\mathcal R)\bigr)
=b-1
$$


is also retained. Nothing below treats that rational-rank statement as a modular forced-pairing estimate.

---

# 2. The exceptional type-$11$ coefficient vanishes for the assembled pair

This first cancellation can be proved directly inside the previous finite profiles. It does not require a new summation algorithm.

Put


$$
B_j=b-1-j.
$$



## 2.1 The finite correction collapses before pairing

For integers $v\ge1$ and $q_0\ge0$,


$$
\begin{aligned}
&\sum_{p=0}^{q_0}
\binom j{q_0-p}
\binom{n+p-1}{p}
\binom{n+B_j+v-1}{B_j+v-p}\\
&\hspace{15mm}=
\boxed{
\binom{b-1+v}{q_0}
\binom{n+B_j+v-1}{B_j+v}.
}
\end{aligned}
\tag{2.1}
$$



Indeed,


$$
\binom{n+p-1}{p}
\binom{n+t-1}{t-p}
=
\binom{n+t-1}{t}\binom tp,
$$


and Vandermonde gives


$$
\sum_p\binom j{q_0-p}\binom{b-1+v-j}{p}
=\binom{b-1+v}{q_0}.
$$



This identity is integral. In particular, it pays no factorial division.

Apply (2.1) to the subtraction part of the bulk profile, with


$$
q_0=s+i-q,
$$


and to the subtraction part of the exterior profile, with


$$
q_0=s.
$$


Thus every type-$1$ correction becomes a scalar multiple of


$$
(-1)^j
\binom{n+b+\rho-1-j}{b+\rho-j},
\qquad \rho\ge0.
\tag{2.2}
$$



The direct contact return $F_{\cdot t}$ already has this form. Multiplication by the normalized force, accumulation of the complete source prefix, and multiplication by $KS^{-1}$ change only its scalar coefficients.

Consequently, the **assembled** type-$1$ part of each contact profile is a finite linear combination of (2.2), not an arbitrary combination of the larger atom family.

## 2.2 Reconstruction preserves a much smaller degree

The reconstruction of (2.2) is a combination of


$$
(-1)^j
\binom{n+b+\rho-1-j}{b+\rho-j}
$$


and


$$
(-1)^j\binom j1
\binom{n+b+\rho-j}{b+\rho+1-j}.
\tag{2.3}
$$



In the old baseline


$$
A_1=n+b-D,\qquad B=b+D,
$$


both large binomials have offset difference


$$
\eta-\varepsilon=-1.
$$


Their conversion polynomial has degree


$$
2D+\eta-\varepsilon+d=2D-1+d.
$$


Thus the reconstructed type-$1$ profile has degree at most $2D$.

Its norm product and its product with the complete exponential profile therefore have type-$11$ polynomial degree at most


$$
\boxed{4D}.
$$



The old exceptional master degree is $4D+5$. Descending polynomial reduction cannot generate a degree above the input degree.

### Theorem 2.1 — Actual exceptional-coefficient cancellation

For the actual assembled norm and complete exponential response at raw precision $2^L$, the coefficient of


$$
M_{4D+5}^{11}
$$


in the old descending ten-master reduction is zero.

This cancellation occurs before division by


$$
C_{11}\Pi_{11}.
$$


It is therefore not an assertion of unproved divisibility of an evaluated moment combination.

### Scope

The previous $D=1$ witness remains correct. It excludes deleting the exceptional master for arbitrary kernels. The actual finite inverse/source assembly lies in a smaller polynomial subspace, and that witness does not belong to this subspace.

This theorem does **not** say that all remaining type-$11$ contributions vanish. The next construction eliminates them by an integral change of representation of the complete finite solve.

---

# 3. Integral normal ordering in divided-power coordinates

The useful basis here is the integer divided-power basis


$$
z^{[j]}=\frac{z^j}{j!}.
$$


An expression


$$
p(z)=\sum_j p_jz^{[j]}
$$


is represented by its integral coefficient vector $(p_j)$. Multiplication and differentiation have integral matrices in this basis.

For any integer $\gamma$, define on polynomials


$$
\mathcal U_\gamma=(1+\partial_z)^\gamma
=\sum_{\ell\ge0}\binom\gamma\ell\partial_z^\ell.
$$


Even when $\gamma<0$, the sum is finite on each polynomial.

Let $\mathcal H_\lambda$ and $\mathcal H_c$ denote multiplication by


$$
\sum_{s=0}^m\lambda_sz^{[s]},
\qquad
\sum_{s=0}^mc_sz^{[s]},
$$


respectively, modulo $2^L$. The inverse-symbol identity gives


$$
\mathcal H_c\mathcal H_\lambda=1\pmod{2^L}.
\tag{3.1}
$$



Define


$$
\boxed{
\mathcal J=\mathcal U_{-n}\mathcal H_c\mathcal U_{-n}.
}
\tag{3.2}
$$



## 3.1 An integral normal-order identity

Leibniz’s rule and


$$
\binom{-n}{\ell}\binom{\ell}{r}
=
\binom{-n}{r}\binom{-n-r}{\ell-r}
$$


give


$$
\mathcal U_{-n}M_{z^{[s]}}
=
\sum_{r=0}^s
\binom{-n}{r}
M_{z^{[s-r]}}\mathcal U_{-n-r}.
$$


Hence


$$
\boxed{
\mathcal J
=
\sum_{s=0}^m c_s
\sum_{r=0}^s
(-1)^r\binom{n+r-1}{r}
M_{z^{[s-r]}}\mathcal U_{-(2n+r)}.
}
\tag{3.3}
$$



Every coefficient in (3.3) is integral.

This is the desired Newton/divided-power feature: the normal ordering does not introduce $s!$, $r!$, or a large-offset denominator.

The normal-ordering mechanism is classical. The new issue addressed below is how to supply its input for the **original finite contact solve**, including its exterior returns.

---

# 4. Exact finite boundary completion

The full auxiliary operator behind the source columns is


$$
P\,\mathcal U_n\mathcal H_\lambda\mathcal U_n,
$$


where $P$ is multiplication by $e^z$ in divided-power coordinates.

Its contact restriction is exactly $A$. To check this, finite Vandermonde gives


$$
(PU_n)_{ir}=\binom{n+i}{r},
$$


and then


$$
\sum_{s,t}
\lambda_s
\binom{n+i}{s}\binom{n+i-s}{t}\binom n{j-t}
=
\sum_s\lambda_s\binom{n+i}{s}\binom{2n+i-s}{j}.
$$



All extended vectors used below are auxiliary polynomial coefficient vectors. No contact equation is added.

## 4.1 The unchanged finite Schur data

Retain


$$
F_{jv}
=
-\sum_{q=0}^v
\binom{-n}{b+q-j}\binom n{v-q},
\qquad 0\le j<b.
$$


Let $E_{\rm tail}$ inject the final $d$ contact coordinates, and let


$$
K_{rt}
=
\lambda_{d+r-t}\binom{b+r}{d+r-t},
\qquad
0\le r<m,\quad 0\le t<d.
$$


Set


$$
G_{\rm end}=E_{\rm tail}^TH^{-1}F^{(m)},
\qquad
S=I_d+G_{\rm end}K.
\tag{4.1}
$$


Because $K\equiv0\pmod2$, $S$ is a unit matrix over $\mathbb Z_2$.

For an exterior label $v$, also write


$$
G_v=E_{\rm tail}^TH^{-1}F_{\cdot v}.
\tag{4.2}
$$



## 4.2 Completion of the first-force solve

For the paid force prefix, define


$$
D_f
=
E_{\rm tail}^TH^{-1}U^{-1}P^{-1}\mathfrak f_{\le I},
\qquad
\zeta_f=S^{-1}D_f,
$$




$$
\beta_f=K\zeta_f,
\qquad
\eta_f=U_n^{(m)}\beta_f,
\tag{4.3}
$$


where $U_n^{(m)}$ is the $m\times m$ upper-triangular binomial matrix.

Form an auxiliary vector $q^f$ by


$$
q^f_j=(P^{-1}\mathfrak f_{\le I})_j
\quad(0\le j<b),
$$




$$
q^f_{b+v}=(\eta_f)_v
\quad(0\le v<m),
$$


and set all later coordinates to zero.

Then


$$
\boxed{z^f=\mathcal Jq^f\pmod{2^L}.}
\tag{4.4}
$$



### Proof

Start with the actual contact solution $z^f$, padded by zeros beyond $b-1$, and put


$$
r=\mathcal U_nz^f,\qquad
w=\mathcal H_\lambda r,\qquad
q=\mathcal U_nw.
$$


The vector $r$ is supported in the contact range. The exterior part of $w$ is exactly


$$
w_{b:b+m-1}=K E_{\rm tail}^Tr=K\zeta_f.
$$


Therefore


$$
q_{b:b+m-1}=U_n^{(m)}K\zeta_f=\eta_f.
$$


Its contact part is $P^{-1}\mathfrak f_{\le I}$, by the original finite equations.

Finally,


$$
\mathcal Jq
=
\mathcal U_{-n}\mathcal H_c
\mathcal U_{-n}\mathcal U_n
\mathcal H_\lambda\mathcal U_nz^f
=z^f\pmod{2^L}.
$$


This proves (4.4). ∎

The full Schur return has therefore become a short, explicitly specified exterior completion. It has not been discarded.

---

# 5. Complete source-response cancellation

This is the point at which the contact return and the complete source must both be used.

Put


$$
V=T+m.
$$


Define the exterior source coefficients


$$
\boxed{
\xi_v
=
\sum_{t=0}^{T}a_t
\sum_{\substack{0\le r\le t\\0\le v-r\le m}}
\binom n{t-r}\lambda_{v-r}
\binom{b+v}{v-r},
\qquad 0\le v\le V.
}
\tag{5.1}
$$


These are precisely the coefficients accumulated from the exterior sum in the complete source formula.

Let


$$
G^{[V]}=(G_0,\ldots,G_V),
\qquad
\zeta_E=S^{-1}G^{[V]}\xi.
$$


Pad $K\zeta_E$ by zeros after its $m$ coordinates, and set


$$
\delta_v=(K\zeta_E)_v-\xi_v,
$$




$$
\boxed{
\theta_v=\sum_{w=v}^{V}\binom n{w-v}\delta_w.
}
\tag{5.2}
$$



Then, on the original contact range,


$$
\boxed{
z^k_j
=
\sum_{v=0}^{V}\theta_v(\mathcal Je_{b+v})_j
\pmod{2^L},
\qquad 0\le j<b.
}
\tag{5.3}
$$



## 5.1 Derivation, including the contact return

Let


$$
s=\sum_{t=0}^{T}a_te_{b+t}.
$$


The source vector before contact restriction is


$$
P\mathcal U_n\mathcal H_\lambda\mathcal U_ns.
$$



The contact part of $\mathcal U_ns$ is the returned source vector. Its tail coordinates are


$$
(\rho_{\rm ret})_h
=
\sum_{t=0}^{T}a_t\binom n{t+d-h},
\qquad 0\le h<d.
\tag{5.4}
$$


The exterior part of $\mathcal H_\lambda\mathcal U_ns$ is


$$
K\rho_{\rm ret}+\xi.
$$



The finite solution formula from the supplied work gives


$$
E_{\rm tail}^T\mathcal U_nz^k
=
\rho_{\rm ret}+S^{-1}G^{[V]}\xi.
\tag{5.5}
$$


Thus the exterior part of the completed transformed vector for $z^k$ is


$$
U_n^{(V+1)}
K\bigl(\rho_{\rm ret}+S^{-1}G^{[V]}\xi\bigr).
$$



The transformed full source has exterior part


$$
U_n^{(V+1)}(K\rho_{\rm ret}+\xi).
$$


Subtracting them cancels the returned term $K\rho_{\rm ret}$, leaving


$$
U_n^{(V+1)}(KS^{-1}G^{[V]}\xi-\xi)=\theta.
$$



Their contact parts agree. Applying $\mathcal J$, and using


$$
\mathcal J\mathcal U_n\mathcal H_\lambda\mathcal U_ns=s,
$$


gives $z^k-s$. Since $s_j=0$ for $j<b$, this proves (5.3).

This cancellation would not be valid if the finite return $F_{\cdot t}$, part of the Schur return, or part of the source prefix were omitted.

## 5.2 Both differential source boundaries remain present

The source used here is the same source satisfying


$$
\mathscr L_n
\left(
\frac{\phi^ng_n-e^z\phi^nU_b}{b!}
\right)
=
e^z\phi^{n+1}(C_{b-1}+C_b),
$$


where


$$
C_j(z)=\sum_{r=0}^{j}\binom n{j-r}\frac{z^r}{r!},
\qquad
U_b(z)=\sum_{j=0}^{b-1}j!C_j(z).
$$


Equations (5.1)–(5.3) reorganize its complete factorial prefix. They do not replace $C_{b-1}+C_b$ by one boundary.

### A boundary warning

The auxiliary vector in (5.3), if evaluated beyond the contact range, represents $z^k-s$, not the zero-padded contact vector $z^k$. In particular, at $j=b$ its value is $-a_0=-1$ modulo $2^L$.

It must not be substituted as an invented contact value $z_b^k$. Physical reconstruction still uses $z_b^k=0$, with the separate exterior $+1$ in (1.2).

---

# 6. Explicit type-$2$-only profiles

The preceding construction is not merely an unspecified inverse. Normal ordering gives the following finite formulas.

## 6.1 Exterior profile

Define


$$
\Psi_{jv}=(\mathcal Je_{b+v})_j.
$$


Equation (3.3) gives


$$
\boxed{
\begin{aligned}
\Psi_{jv}
={}&(-1)^{b+v-j}
\sum_{s=0}^m(-1)^sc_s
\sum_{r=0}^s\binom{n+r-1}{r}\binom j{s-r}\\
&\qquad\cdot
\binom{2n+b+v+s-1-j}{b+v+s-r-j}.
\end{aligned}
}
\tag{6.1}
$$


All its atoms have $\alpha=2$.

## 6.2 First-force head profile

Let $B_{ji}$ be the result of applying $\mathcal J$ to the contact-truncated vector $P^{-1}e_i$. The finite hockey-stick calculation gives


$$
\boxed{
\begin{aligned}
B_{ji}
={}&(-1)^{j-i}
\sum_{s=0}^m(-1)^sc_s
\sum_{r=0}^s\binom{n+r-1}{r}
\sum_{q=0}^i
\binom{2n+r+q-1}{q}\\
&\quad\cdot
\binom{s-r+i-q}{s-r}
\binom j{s-r+i-q}
\binom{2n+b+s-1-j}{b+s-r-q-1-j}.
\end{aligned}
}
\tag{6.2}
$$



To derive it, put $t=s-r$ in (3.3), apply the one-inverse finite profile with parameter $2n+r$ at row $j-t$, and use


$$
\binom jt\binom{j-t}{i-q}
=
\binom{t+i-q}{t}\binom j{t+i-q}.
$$



Consequently,


$$
\boxed{
z^f_j
=
\sum_{i=0}^{I}\mathfrak f_iB_{ji}
+
\sum_{v=0}^{m-1}(\eta_f)_v\Psi_{jv}
\pmod{2^L},
}
\tag{6.3}
$$




$$
\boxed{
z^k_j=\sum_{v=0}^{T+m}\theta_v\Psi_{jv}
\pmod{2^L}.
}
\tag{6.4}
$$



These formulas have:

- no original-length inner convolution;
- no original-size inverse;
- no type-$1$ atom;
- no additional nonunit division.

They apply only at the contact indices $j<b$; the physical terminal is still (1.1)–(1.2).

---

# 7. A smaller baseline for the actual assembled polynomials

The integral profiles can now be converted to one common type-$22$ summand more economically than the old arbitrary-kernel conversion.

Put


$$
\rho=T+2m+1,
$$




$$
\mathsf A=2n+b-1,\qquad
\mathsf B=b+\rho,
\qquad
\Delta=\mathsf A-\mathsf B=2n-\rho-1.
\tag{7.1}
$$



We impose the same bounded-precision condition used previously,


$$
n>4D+2,\qquad D=I+2m+T+4.
\tag{7.2}
$$


It is more than sufficient for all baseline parameters and adjoint pivots below to be positive. It is not an extension to half-length precision.

The new common summand is


$$
\boxed{
t(j)=
\binom{n+2}{j}^{\!2}
\binom{\mathsf A-j}{\mathsf B-j}^{\!2},
\qquad 0\le j\le b.
}
\tag{7.3}
$$



## 7.1 Target-specific degree and denominator bounds

For an atom


$$
\binom jd
\binom{2n+b+\eta-j}{b+\varepsilon-j},
$$


put


$$
h=\eta+1,\qquad \ell=\rho-\varepsilon.
$$


Then


$$
\binom{2n+b+\eta-j}{b+\varepsilon-j}
=
\binom{\mathsf A-j}{\mathsf B-j}
\frac{(\mathsf A+1-j)^{\overline h}
      (\mathsf B-j)_{\underline\ell}}
     {(2n-\rho)^{\overline{h+\ell}}}.
\tag{7.4}
$$


The zero convention at a negative lower index is preserved by the falling factorial, just as in the earlier conversion.

Define


$$
r_f=m+I+1,\qquad r_k=m+1,
$$




$$
k_f=\rho+m+I+1=\rho+r_f,
\qquad
k_k=\rho+m.
\tag{7.5}
$$



Inspection of (6.1)–(6.2), including reconstruction, gives:

- first-force profile:
  

$$
d\le r_f,\qquad h+\ell\le k_f,\qquad
  \deg\le k_f+1;
$$


- complete exponential profile:
  

$$
d\le r_k,\qquad h+\ell\le k_k,\qquad
  \deg\le k_k+1.
$$



For example, a head atom has


$$
d=s-r+i-q,\quad
\eta=s-1,\quad
\varepsilon=s-r-q-1,
$$


so


$$
h+\ell=\rho+r+q+1,
$$


and


$$
d+h+\ell=\rho+s+i+1.
$$


Reconstruction increases this degree by at most one.

Thus valid profile clearers are


$$
\boxed{
C_f=r_f!\,(2n-\rho)^{\overline{k_f}},
\qquad
C_k=r_k!\,(2n-\rho)^{\overline{k_k}}.
}
\tag{7.6}
$$



Using integral representatives of the bounded-precision coefficient data, there are integral polynomials $P_f,P_k$ such that, for $j<b$,


$$
\Delta_jz^f
\equiv
(-1)^j
\binom{\mathsf A-j}{\mathsf B-j}\frac{P_f(j)}{C_f}
\pmod{2^L},
$$




$$
\Delta_jz^k
\equiv
(-1)^j
\binom{\mathsf A-j}{\mathsf B-j}\frac{P_k(j)}{C_k}
\pmod{2^L},
\tag{7.7}
$$


with


$$
\deg P_f\le k_f+1,\qquad
\deg P_k\le k_k+1.
$$



The meaning of these congruences is the original integral atom evaluation; no entrywise inversion of $C_f$ or $C_k$ modulo $2^L$ is being made.

The assembled polynomial degrees are therefore


$$
\boxed{
H_Q=2k_f+2,\qquad H_E=k_f+k_k+2.
}
\tag{7.8}
$$



---

# 8. Three moments, with every charge and division paid

Define


$$
\mathsf M_s=\sum_{j=0}^{b-1}j^st(j),
\qquad s=0,1,2.
\tag{8.1}
$$


The cutoff remains $j<b$.

For this summand, use


$$
u(j)=(n+2-j)^2(\mathsf B-j)^2,
\qquad
v(j)=j^2(\mathsf A+1-j)^2,
$$




$$
\mathscr TQ(j)=u(j)Q(j+1)-v(j)Q(j).
$$


The leading coefficient is


$$
\mathscr Tj^s
=
(s+\sigma)j^{s+3}+\cdots,
\qquad
\boxed{\sigma=2n-2\rho-4>0.}
\tag{8.2}
$$


There is no exceptional step.

Finite summation gives


$$
\sum_{j=0}^{b-1}t(j)\mathscr TQ(j)
=
\boxed{\mathsf T\,Q(b)},
$$


where


$$
\boxed{
\mathsf T
=
b^2(2n)^2W_b^2
\binom{2n-1}{\rho}^{\!2}.
}
\tag{8.3}
$$



This is the introduced telescoping charge. It is not the physical terminal.

Descending reduction of a polynomial of degree $H$ is paid by


$$
\Pi_H=(2n-2\rho-4)^{\overline{H-2}}.
$$


Hence the actual norm and exponential products are paid by


$$
\boxed{
\kappa_Q=C_f^2
(2n-2\rho-4)^{\overline{2k_f}},
}
\tag{8.4}
$$




$$
\boxed{
\kappa_E=C_fC_k
(2n-2\rho-4)^{\overline{k_f+k_k}}.
}
\tag{8.5}
$$



The complete paid right-hand sides consist of:

1. the appropriate linear combination of $\mathsf M_0,\mathsf M_1,\mathsf M_2$;
2. the charge $\mathsf TQ(b)$;
3. respectively,
   

$$
\kappa_Q b^2W_b^2(z^f_{b-1})^2,
   \tag{8.6}
$$


   or
   

$$
\boxed{
   \kappa_E W_b^2\,b z^f_{b-1}(bz^k_{b-1}+1).
   }
   \tag{8.7}
$$



Let


$$
e_Q=v_2(\kappa_Q),\qquad e_E=v_2(\kappa_E).
$$


To recover the raw numerator modulo $2^L$, the **whole** corresponding right-hand side must be evaluated modulo


$$
2^{L+e_Q}\quad\hbox{or}\quad2^{L+e_E}.
$$


Only then may its power of two be divided out and its odd factor inverted.

No separate divisibility is asserted for the individual moment terms.

## 8.1 The new clearer is genuinely smaller

Let $\kappa_{22}^{\rm old}$ be the previous type-$22$ clearer,


$$
(2D)!
\left((2n-2D+1)^{\overline{4D}}\right)^2
(2n-4D-2)^{\overline{10D-2}}.
$$



Then


$$
\boxed{
\kappa_Q\mid\kappa_{22}^{\rm old},
\qquad
\kappa_E\mid\kappa_{22}^{\rm old}.
}
\tag{8.8}
$$



### Proof

The variable-factor intervals in $C_f,C_k$ are


$$
[-\rho,m+I],\qquad[-\rho,m-1],
$$


as offsets from $2n$. Both are contained in


$$
[-2D+1,2D].
$$



Also


$$
(r_f!)^2\mid(2r_f)!\mid(2D)!,
$$


and


$$
r_f!r_k!\mid(r_f+r_k)!\mid(2D)!.
$$



The new adjoint-pivot intervals are


$$
[-2\rho-4,\,2m+2I-3]
$$


and


$$
[-2\rho-4,\,2m+I-4].
$$


Both lie inside the old interval


$$
[-4D-2,\,6D-5].
$$


Multiplying these divisibilities proves (8.8). ∎

This is a bound for the actual assembled profiles, not a blanket claim about arbitrary kernels in the old offset box.

It does not identify the least possible computational denominator of the assembled polynomial. Further coefficient content may reduce it.

---

# 9. Exact large-offset loss on the original family

The new losses involve only short products of factors $2n+c$. Their original-family behavior can be classified exactly.

Put


$$
q=9^{32},\qquad H_0=2001\cdot9^{18}.
$$


Then


$$
n=2H_0q^u,\qquad
v_2(q-1)=8,
$$


and direct modular arithmetic gives


$$
H_0\equiv161\pmod{256}.
$$


Therefore


$$
\boxed{2n\equiv644\pmod{1024}.}
\tag{9.1}
$$



## 9.1 Nonresonant and resonant offsets

If


$$
c\not\equiv380\pmod{1024},
$$


then


$$
\boxed{
v_2(2n+c)=v_2(644+c)<10,
}
\tag{9.2}
$$


independently of $u$.

If


$$
c\equiv380\pmod{1024},
$$


there is a unique $\zeta_c\in\mathbb Z_2$ such that


$$
q^{\zeta_c}=-\frac{c}{4H_0}.
$$


For every admissible integer $u$ with $2n+c\ne0$,


$$
\boxed{
v_2(2n+c)=10+v_2(u-\zeta_c).
}
\tag{9.3}
$$



### Proof

The map


$$
x\longmapsto q^x
$$


is a bijection from $\mathbb Z_2$ to $1+256\mathbb Z_2$. This follows from the $2$-adic logarithm, since


$$
v_2(\log q)=8.
$$


Moreover,


$$
v_2(q^x-q^y)=8+v_2(x-y).
$$


Multiplication by $4H_0$ adds two to the valuation. This proves (9.3); (9.2) follows directly from (9.1). ∎

Thus the loss of a specified product is unbounded on the original family exactly when its offset set contains a residue $380\bmod1024$.

This statement concerns the displayed product, not an unproved minimal denominator after all possible assembled-coefficient cancellation.

For comparison, the corresponding old factors $n+c$ are resonant precisely at


$$
c\equiv190\pmod{512}.
$$


The integral type-$2$-only representation removes those $n+c$ factors from the new scalar clearing products altogether.

## 9.2 Classification of an unbounded branch

If an offset $c$ occurs with multiplicity $\mu_c$ in $\kappa_Q$ or $\kappa_E$, its contribution is


$$
\mu_c\bigl(10+v_2(u-\zeta_c)\bigr).
$$


For two distinct resonant offsets,


$$
\boxed{
v_2(\zeta_c-\zeta_{c'})
=
v_2(c-c')-10.
}
\tag{9.4}
$$


Consequently, sufficiently close to one root $\zeta_c$, all other root contributions are fixed, and the unbounded growth has exact slope $\mu_c$.

This classifies the possible large-offset blow-up of the specified clearer.

## 9.3 An infinite subdomain with a proved paid bound

Fix a raw precision $L$, so that $I,m,T,\rho$ are fixed once the physical cutoffs no longer saturate. Let $r$ be the number of distinct resonant offsets in the new products.

Choose $h\ge0$ with


$$
2^h>r.
$$


Each resonant offset forbids one residue


$$
u\equiv\zeta_c\pmod{2^h}.
$$


At least one residue $w\pmod{2^h}$ is not forbidden. On the infinite original subdomain


$$
u\equiv w\pmod{2^h},
$$


every variable factor has valuation at most


$$
V_0=9+h.
$$



For a product of $\ell$ consecutive integers whose individual valuations are at most $V_0$,


$$
v_2(\text{product})\le \ell-1+V_0.
$$


Therefore


$$
\boxed{
e_Q
\le
2v_2(r_f!)+4k_f-3+3V_0,
}
\tag{9.5}
$$




$$
\boxed{
e_E
\le
v_2(r_f!)+v_2(r_k!)
+2(k_f+k_k)-3+3V_0.
}
\tag{9.6}
$$



These bounds are independent of the full word length of $b$ on that subdomain.

The quantifier is important: this constructs an infinite subdomain for a specified raw precision. It does not prove a uniform bound on the actual content $a$, and hence does not automatically give a fixed primitive-output depth there.

---

# 10. A concrete original-family loss theorem at $L=32$

For fixed raw precision, with unsaturated cutoffs,


$$
I=8L-2,\quad m=4L-4,\quad T=2L-1,
$$


so


$$
\rho=10L-8,\qquad
k_f=22L-13,\qquad
k_k=14L-12.
$$



The new norm product first encounters a resonant offset at $L=17$; the new exponential product first does so at $L=25$. Up to $L=32$, their only possible resonant offset is $c=380$.

Now


$$
H_0\equiv417\pmod{512},
\qquad
q\equiv257\pmod{512}.
$$


For odd $u$,


$$
H_0q^u\equiv161\pmod{512},
$$


and hence


$$
\boxed{2n\equiv644\pmod{2048}.}
\tag{10.1}
$$



At $L=32$,


$$
I=254,\quad m=124,\quad T=63,\quad \rho=312,
$$




$$
r_f=379,\quad r_k=125,\quad
k_f=691,\quad k_k=436.
$$



All relevant shifted residues lie strictly between $0$ and $2048$, so their valuations equal those of the following ordinary integer intervals:


$$
C_f:\quad332,\ldots,1022,
$$




$$
C_k:\quad332,\ldots,767,
$$




$$
\Pi_Q:\quad16,\ldots,1397,
$$




$$
\Pi_E:\quad16,\ldots,1142.
$$



Using $v_2(N!)=N-s_2(N)$,


$$
\begin{aligned}
e_Q
&=
2v_2(379!)
+2v_2(1022!/331!)
+v_2(1397!/15!)\\
&=2(372)+2(687)+1379\\
&=\boxed{3497},
\end{aligned}
\tag{10.2}
$$


and


$$
\begin{aligned}
e_E
&=
v_2(379!)+v_2(125!)
+v_2(1022!/331!)\\
&\qquad
+v_2(767!/331!)
+v_2(1142!/15!)\\
&=372+119+687+432+1125\\
&=\boxed{2735}.
\end{aligned}
\tag{10.3}
$$



### Theorem 10.1

On every original index with $u$ odd, the specified new raw-$32$ computational clearers have exactly the losses (10.2)–(10.3).

This is an infinite-original-family statement because (10.1) was proved on that family. It is not an extrapolation from finitely many auxiliary $b$.

### Practical interpretation

These losses are still large. Direct carry evaluation at raw precision plus several thousand bits is not justified as a practical primitive algorithm.

The theorem improves the normalization of the actual reduced target; it does not evaluate its moments or its primitive digits.

---

# 11. What remains open in the arithmetic reduction

The present report closes one specific outstanding obligation:



$$
\boxed{\text{The actual exceptional type-\(11\) coefficient is zero.}}
$$



It also supplies an explicit, integral, type-$2$-only source/response assembly and a smaller paid certificate.

The following obligations remain open.

## 11.1 Least loss of the actual polynomial certificate

The clearers $\kappa_Q,\kappa_E$ are proved sufficient. They are not asserted to be least.

A concrete next coefficient-side lemma is:

> For the explicitly assembled $P_f^2$ and $P_fP_k$ of §7, determine the $2$-adic content of their reduced remainder and adjoint polynomial in the integer-valued Newton basis, after the profile clearers have been included.

This is now a bounded polynomial problem with explicit inputs $\eta_f,\theta$, not an unspecified inverse or arbitrary-kernel problem.

A mere basis change does not prove a saving. For example, the leading Newton coefficient of $\mathscr T\binom js$ contains


$$
(s+\sigma)(s+1)(s+2)(s+3),
$$


so naïve Newton elimination can introduce additional nonunit pivots. A useful lemma must exploit the actual $P_f,P_k$, not just the integer-valuedness of arbitrary kernels.

## 11.2 The three complete moments are still unevaluated

Let the reduced exponential right-hand side be


$$
\begin{aligned}
\mathcal S_E={}&
a_0\mathsf M_0+a_1\mathsf M_1+a_2\mathsf M_2
+\mathsf TQ_E(b)\\
&+\kappa_EW_b^2\,b z^f_{b-1}(bz^k_{b-1}+1).
\end{aligned}
\tag{11.1}
$$


Its coefficients are supplied by the explicit bounded assembly above. Nevertheless, evaluating or bounding this **whole** expression remains necessary.

In particular, neither:

- the disappearance of the old exceptional coefficient, nor
- a small denominator for its polynomial reduction,

proves that the complete exponential bracket is nonzero.

The precise next moment-side target is a congruence for (11.1), at its paid modulus, on infinitely many original indices. It must include the large factor $W_b^2$ and both physical terminal terms.

---

# 12. Primitive normalization and the logarithmic contribution

For primitive output modulo $2^K$, the raw precisions are unchanged:


$$
\boxed{
L_Q=K+2a+2,\qquad L_E=K+a+3.
}
\tag{12.1}
$$



The new moment loss is additional:


$$
L_Q+e_Q\quad\hbox{or}\quad L_E+e_E.
$$


After the whole computational-clearer division, one must still perform the whole division by


$$
2^{2a+2}\quad\hbox{or}\quad2^{a+3}.
$$



The value of $a$ is the actual first-column content. It has not been recomputed or replaced by a computational polynomial content.

The logarithmic source remains


$$
\mathcal L_s=s![z^s]\frac{F(z)}{1-z},
$$


with the retained guard


$$
B_*=n-v_2(b!)-1-2s_2(n)-\ell.
$$


No logarithmic term is deleted beyond that guard. A primitive digit outside the protected range must include the complete original logarithmic contribution.

Thus no newly evaluated primitive $E$ digit, norm excess, or half-length nonzero residue is claimed here.

---

# 13. Actual clearer, all-prime gcd, denominator, and whole error

The producer normalization remains


$$
\omega_j=j!W_j,
$$




$$
u_j=\frac{2\Lambda R\,x_j}{\omega_j},
\qquad
v_j=\frac{4b!\,y_j}{\omega_j},
$$


and its actual least simultaneous clearer is


$$
\boxed{
d_B=
\operatorname{lcm}_{0\le j\le b}
\{\operatorname{den}(u_j),\operatorname{den}(v_j)\}.
}
\tag{13.1}
$$



No reconstructed row content is divided out.

Writing $N=x^Tx$ and $H=x^Ty$ for the producer’s norm and mixed form, retain


$$
A_B=d_B^2\,4\Lambda^2R^2N,
\qquad
H_B=d_B^2\,8\Lambda Rb!H,
$$




$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
}
\tag{13.2}
$$



The computational clearers $C_f,C_k,\kappa_Q,\kappa_E$ are unrelated to replacing $d_B$ or $g_B$.

For every prime $p$,


$$
v_p(q_n)
=
\max\{v_p(\mathscr D_n)+v_p(N)-v_p(H),0\},
\qquad
\mathscr D_n=\frac{\Lambda R}{2b!}.
$$


The established ternary law is retained:


$$
v_3(q_n)=n-\frac{b+15}{2}.
$$


It is not proposed for recomputation.

Finally,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


and the evaluated form remains


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n.
}
\tag{13.3}
$$



An irrationality argument using this producer would still require, on the **same infinitely many original indices**, a nonzero whole error and a favorable estimate involving the actual all-prime denominator. For example, nonzero values tending to zero in (13.3) would contradict rationality. No such estimate is established here.

The exponential pairing alone is not the whole evaluated error.

---

# 14. Bounded exact arithmetic specification

No computation is required for the symbolic cancellation and boundary-completion proofs above. No tool was used.

If an independent arithmetic certificate is desired for the new explicit loss theorem, it needs only the following bounded inputs:

- $L=32$;
- the proved original-family residue $2n\equiv644\pmod{2048}$ for odd $u$;
- factorial indices
  

$$
15,\ 125,\ 331,\ 379,\ 767,\ 1022,\ 1142,\ 1397.
$$



The expected verifiable outputs are


$$
\begin{array}{c|rrrrrrrr}
N&15&125&331&379&767&1022&1142&1397\\ \hline
v_2(N!)&11&119&326&372&758&1013&1136&1390
\end{array}
$$


and therefore


$$
\boxed{e_Q=3497,\qquad e_E=2735.}
$$



This calculation does not inspect an original-size matrix, a long sum, a primitive digit, a final gcd, or a whole error. It does not repeat the accepted polynomial or finite-profile audits.

No original-size primitive-response computation is proposed: the remaining moment-evaluation cost has not yet been brought within a justified practical bound.

---

# 15. Proof-status ledger

| Statement | Status |
|---|---|
| Supplied auxiliary finite-profile and finite-sum checks | Retained at their stated finite scope |
| Supplied symbolic $D=1$ generic exceptional witness | Retained |
| Exceptional type-$11$ coefficient for the actual assembled pair | **Proved zero** |
| Integral normal ordering of the two inverse binomial factors | **Proved** |
| Finite completion retaining the full Schur return | **Proved modulo paid raw precision** |
| Complete exponential completion retaining its contact return and full prefix | **Proved** |
| Type-$2$-only actual profile representation | **Proved** |
| Three-moment reduction with complete telescoping and physical charges | **Proved** |
| New clearers divide the old type-$22$ clearer | **Proved** |
| Exact large-offset classification on the original family | **Proved for the specified products** |
| Infinite admissible subdomains with uniform paid product bounds | **Proved at specified raw precision** |
| Actual least polynomial-reduction loss | Open |
| Evaluation/nonvanishing of the complete three-moment response | Open |
| Newly evaluated primitive $Q$ or $E$ digit | Not obtained |
| Same-index all-prime denominator versus nonzero whole error | Unresolved |
| Rationality or irrationality of $e+\pi$ | Unresolved |

---

## Conclusion

The principal new result is an actual source-response cancellation, not a generic reduction theorem:



$$
\boxed{
\text{The exceptional type-\(11\) master coefficient vanishes
for both actual assembled pairings.}
}
$$



A stronger integral construction gives


$$
\boxed{
\begin{gathered}
\text{normalized force + complete finite source + full Schur return}\\
\longrightarrow
\text{explicit type-\(2\)-only profiles, with no new nonunit division.}
\end{gathered}}
$$



Their weighted pairings admit a three-moment certificate with a strictly smaller sufficient clearer than the old type-$22$ certificate. The exact large-offset losses of that certificate have been classified on the original word $b=9^{18+32u}$, and an explicit infinite odd-$u$ subdomain has been given.

The remaining mathematical bottleneck is now the **paid value of the actual three-moment combination**, including its telescoping charge, the large $W_b^2$, and the complete physical terminal. A further coefficient-content theorem may lower the cost, but neither it nor a useful moment congruence has yet been proved.

After that local bottleneck, the actual contents, least simultaneous clearer, all-prime gcd, primitive denominator, and nonzero whole same-index error still have to be compared.

**The cancellation and finite-normalization results are rigorous. The primitive valuation application and the unconditional rationality or irrationality of $e+\pi$ remain open.**
