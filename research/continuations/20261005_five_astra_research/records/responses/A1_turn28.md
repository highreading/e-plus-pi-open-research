> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The actual regular-force interface and the local polynomial congruence

## 1. Outcome and source boundary

The missing force-and-coordinate interface **does close**. In the original factorial-divided coordinates, the complete orthogonality forcing is integral, the first $3M$ nonconstant coordinates form a $3$-adic unit block, and the actual solution satisfies


$$
3\eta_{d+1}\equiv
\begin{cases}
\theta(-1)^{M-D}\binom MD,&d=3D,\quad 0\le D\le M,\\
0,&3\nmid d,
\end{cases}
\pmod3,
\qquad
\theta=3\eta_N\equiv2\pmod3.
$$


The sign is positive relative to the radical vector with final coordinate $1$. The minus sign in the polynomial expansion enters separately.

Consequently, reusing turn17’s true jets and projection theorem at their stated scope, the actual local polynomial obeys


$$
\boxed{
Q_n^{\rm loc}-Q_{\rm core}\in
3^{v_3(j)+2}\mathbb Z_3[y]\qquad(3\mid j),
}
$$


where


$$
Q_n^{\rm loc}=3P_n,\qquad
Q_{\rm core}=(y+1)(y-1)^{n-2}\bigl(3y-71-(n-2)\bigr).
$$


Below I also supply a coefficient lemma extending turn17’s $v_3(j)\ge2$ Taylor deduction to $v_3(j)=1$. No true jet is recomputed.

This closes a local construction interface. It does **not** evaluate the primitive center denominator or prove irrationality of $e+\pi$.

### Verification gate

The bounded archive check here is a comparison of the supplied complete texts, especially turns4, 5, 14, 17 and the coordinator support reconstruction. No external search facility is available in this conversation; I therefore do not claim a fresh primary-literature search. The classical ingredients used below—Pascal inversion, Lucas reduction, Schur elimination and factorial moments—are established methods, not global novelty claims.

Two source qualifications matter:

* “Integral inverse” below means an inverse over $\mathbb Z_3$, **not** necessarily over $\mathbb Z$.
* The supplied dyadic theorem proves
  

$$
v_2(q_{\rm center})=2+v_2(\eta_{\rm dyadic}).
$$


  It does not prove the later assertion $v_2(q)=n+2$. I do not use that assertion or infer pairwise distinct centers from it.
* The exact endpoint formula $v_3(Q_n(-1))=2v_3((n-1)!)$ is cited in later turns from an omitted turn9 argument. It is not proved by the force interface below and is unnecessary for the factorial-tail argument.

---

## 2. The complete actual Gram system and forcing

Throughout,


$$
n=4^j+1,\qquad N=n-1=3M+1,\qquad L=3M=N-1,\qquad j\ge1.
$$


Use precisely


$$
h_0=1,\qquad h_{d+1}=(y+1)(y-1)^d,
$$




$$
\psi_0=1,\qquad \psi_{d+1}=\frac{h_{d+1}}{d!}.
$$


The actual signed functional is


$$
\rho(F)=\mu(F)-F(-1),\qquad
\mu(F)=\int_0^\infty e^{-t}F((1-t)^2)\,dt.
$$



Define the **finite** system


$$
G_n=\bigl(\rho(\psi_i\psi_k)\bigr)_{0\le i,k<n},
\qquad
\omega_i=\rho\!\left(\psi_i\frac{h_n}{N!}\right),
\quad 0\le i<n.
$$


Then


$$
\boxed{\eta=G_n^{-1}\omega.}
$$



There is no truncation of the force. In particular,


$$
\omega_0=\frac{\mu((y+1)(y-1)^N)}{N!},
$$


and, for every $0\le d\le L$,


$$
\boxed{
\omega_{d+1}
=
\frac{\mu((y+1)^2(y-1)^{d+N})}{d!\,N!}.
}
$$


The negative mass contributes zero here because $h_n(-1)=0$.

### Factorial divisibility proves every entry integral

Under $y=(1-t)^2$,


$$
y-1=t(t-2).
$$


Thus, for $F\in\mathbb Z[y]$,


$$
(y-1)^sF(y)=t^sR(t),\qquad R\in\mathbb Z[t].
$$


Integration produces an integer linear combination of $(s+a)!$, so


$$
s!\mid\mu((y-1)^sF(y)).
$$



This proves $G_n\in M_n(\mathbb Z)$. It also proves


$$
\omega_0\in\mathbb Z,\qquad
\omega_{d+1}\in\mathbb Z,
$$


because


$$
\frac{(d+N)!}{d!\,N!}=\binom{d+N}{d}\in\mathbb Z.
$$


Hence all regular forces, including forces after any integral $3$-adic unit-block elimination, are $3$-integral.

---

## 3. The regular unit block and the exceptional column

Reorder the finite coordinates as


$$
E:\ d=0,\ldots,L-1;\qquad
W:\ (\text{constant},d=L).
$$


Write


$$
G_n=
\begin{pmatrix}
E&u&x\\
u^T&0&t_L\\
x^T&t_L&g_{LL}
\end{pmatrix}.
$$


The zero in the constant norm is the actual signed value $\rho(1)=0$.

Turn4’s residue calculation gives


$$
\overline E=B_M\otimes A,
$$


where


$$
B_M(D,E)=\binom{D+E}{D},\quad 0\le D,E<M,
\qquad
A=
\begin{pmatrix}
0&2&1\\
2&2&0\\
1&0&0
\end{pmatrix}.
$$


Here $\det A=1$ in $\mathbb F_3$. For


$$
P_M(D,a)=\binom Da,
$$


Vandermonde gives


$$
B_M=P_MP_M^T,\qquad \det B_M=1.
$$


Therefore


$$
\boxed{E^{-1}\in M_L(\mathbb Z_3).}
$$



### Exact binomial inversion behind the exceptional reduction

The last cross-column satisfies


$$
\bar x=b\otimes Ae_0,\qquad
b_D=\binom{M+D}{D},\quad 0\le D<M.
$$


Set $v_a=\binom Ma$, $a<M$. Then $b=P_Mv$, and


$$
\begin{aligned}
(B_M^{-1}b)_D
&=\sum_{a=D}^{M-1}(-1)^{a-D}\binom aD\binom Ma\\
&=(-1)^{M-1-D}\binom MD.
\end{aligned}
$$


This is an exact integer identity. Applying it to the residue of the actual block proves that $E^{-1}x$ reduces to the vector supported at $d=3D$, with those coefficients.

Let $f_d$ denote the original nonconstant coordinate vector corresponding to $\psi_{d+1}$. The exact eliminated exceptional vector is


$$
z_*=
f_L-\sum_{d=0}^{L-1}(E^{-1}x)_d f_d.
$$


It consequently reduces to


$$
\boxed{
z_*\equiv z:=
\sum_{D=0}^{M}(-1)^{M-D}\binom MD f_{3D}\pmod3.
}
$$


This is the required identification in the **original** divided coordinates.

It is important not to strengthen this statement incorrectly: $z$ is an exact integral representative of the residue of $z_*$; the actual $3$-adic exceptional column need not equal $z$ exactly.

---

## 4. The two-by-two solve, including constant coupling and force

Set


$$
\begin{pmatrix}a&\beta\\ \beta&c\end{pmatrix}
=
\begin{pmatrix}0&t_L\\t_L&g_{LL}\end{pmatrix}
-
\begin{pmatrix}u^T\\x^T\end{pmatrix}
E^{-1}
\begin{pmatrix}u&x\end{pmatrix},
$$


and retain both eliminated forces:


$$
\xi_0=\omega_0-u^TE^{-1}\omega_E,
\qquad
\xi_L=\omega_N-x^TE^{-1}\omega_E.
$$


Thus


$$
\delta=c-\frac{\beta^2}{a},
$$


and the exact solution is


$$
\boxed{
\eta_N=\frac{\xi_L-(\beta/a)\xi_0}{\delta},
}
$$




$$
\boxed{
\eta_{\rm const}=\frac{\xi_0-\beta\eta_N}{a},
}
$$




$$
\boxed{
\eta_E=E^{-1}\omega_E
       -E^{-1}u\,\eta_{\rm const}
       -E^{-1}x\,\eta_N.
}
$$



Turn5’s first-lift proof uses the full moment identity


$$
e_{3r}\equiv3\pmod9
$$


and the finite Pascal Schur norm $1$. Its resulting congruences are


$$
a\equiv2\pmod3,\quad \beta\equiv0\pmod3,\quad
\delta\equiv3\pmod9,
$$




$$
\xi_0\equiv0\pmod3,\qquad \xi_L\equiv2\pmod3.
$$


They imply


$$
\theta:=3\eta_N
=\frac{\xi_L-(\beta/a)\xi_0}{\delta/3}
\in\mathbb Z_3^\times,
\qquad
\boxed{\theta\equiv2\pmod3.}
$$


Also $\eta_{\rm const}\in\mathbb Z_3$.

Multiplying the reconstructed regular solution by $3$ now gives


$$
3\eta_E\equiv-(E^{-1}x)\theta\pmod3.
$$


Together with the binomial inversion and the final coordinate, this proves


$$
\boxed{
3\eta_{d+1}\equiv
\begin{cases}
\theta(-1)^{M-D}\binom MD,&d=3D,\quad 0\le D\le M,\\
0,&3\nmid d.
\end{cases}
}
$$


Furthermore $3\eta_{\rm const}\equiv0\pmod3$.

This establishes the support assertion, not merely $3\eta$-integrality.

### Check against the actual monic polynomial

Multiplying


$$
\psi_n-\sum_{i<n}\eta_i\psi_i
$$


by $N!$ gives exactly


$$
\boxed{
P_n=h_n-N!\eta_{\rm const}
-\sum_{d=0}^{N-1}\frac{N!}{d!}\eta_{d+1}h_{d+1}.
}
$$


It is monic and orthogonal to every polynomial of degree below $n$, hence is the actual monic orthogonal polynomial. In particular,


$$
P_n(-1)=-N!\eta_{\rm const}.
$$


There is no coordinate change between the support theorem and this expansion.

---

## 5. The full last-three factorial terms

Suppose $3\mid M$, and put


$$
m=v_3(M)=v_3(j)\ge1.
$$


The retained last term has $d=L$, coefficient $N\theta$ in $3P_n$.

The next three terms are **exactly**


$$
-NL(3\eta_L)h_L,
$$




$$
-NL(L-1)(3\eta_{L-1})h_{L-1},
$$




$$
-NL(L-1)(L-2)(3\eta_{L-2})h_{L-2}.
$$


Their $d$-indices are $L-1,L-2,L-3$, respectively. No factorial factor has been suppressed.

Each displayed factorial coefficient has valuation $m+1$. The support theorem gives


$$
3\eta_L\equiv0,\qquad
3\eta_{L-1}\equiv0,\qquad
3\eta_{L-2}\equiv-M\theta\equiv0\pmod3.
$$


Thus all three complete terms belong to $3^{m+2}\mathbb Z_3[y]$.

For every $d\le L-4$, the quotient $N!/d!$ contains both $L$ and $L-3$. Since


$$
v_3(L)=m+1,\qquad v_3(L-3)=1,
$$


these terms also have depth at least $m+2$.

Finally,


$$
3N!\eta_{\rm const}\in3^{1+v_3(N!)}\mathbb Z_3.
$$


Here $v_3(N!)\ge v_3(L)=m+1$, so the constant term has the required depth without invoking a doubled-factorial endpoint theorem.

Therefore


$$
\boxed{
3P_n\equiv
(y+1)(y-1)^L\bigl(3(y-1)-N\theta\bigr)
\pmod{3^{m+2}}.
}
$$



---

## 6. Reusing the true jets; closing the $m=1$ edge

Turn17 proves, without inferring derivatives from integer values,


$$
\Theta_{\rm raw}(0)=68,\qquad
(N\Theta_{\rm raw})'(0)\equiv3\pmod{27}.
$$


It also proves, under its stated projection hypotheses,


$$
\theta-\Theta_{\rm raw}(M)\in3^{m+2}\mathbb Z_3.
$$


The force-and-coordinate identification needed to apply its factorial-tail argument is now proved above.

For $m\ge2$, turn17 already yields


$$
N\theta\equiv68+3M\pmod{3^{m+2}}.
$$



For $m=1$, integral higher Taylor coefficients alone would not suffice: a quadratic term could survive modulo $27$. The following small additional lemma resolves that issue.

### Coefficient lemma

The restricted raw series satisfy


$$
H(T)\equiv1,\qquad G(T)\equiv2\pmod{3\mathbb Z_3[[T]]}.
$$


Consequently every nonconstant coefficient of $\Theta_{\rm raw}=G/H$, and of $(1+3T)\Theta_{\rm raw}$, is divisible by $3$.

**Proof.** Use turn17’s coefficient estimate for the complete moment summands:


$$
v_3([T^k]P_\ell(3T+r))
\ge
\max\{k,\lfloor2\ell/3\rfloor\}-v_3(\ell!).
$$


For $\ell\ge6$, the Gauss valuation is at least $2$. For $0\le\ell\le5$, all coefficients of degree at least $3$ have depth at least $2$; every nonconstant coefficient has depth at least $1$. The factor $(-8)^T$ is $1$ modulo $9$.

It follows, after retaining the full formula for $e_s$, that $e_{3T}$ modulo $9$ is a polynomial of degree at most two. Its constant is $e_0=12$, and its coefficients are divisible by $3$. Turn5 proves $e_{3t}\equiv3\pmod9$ for all nonnegative integers $t$. Thus


$$
e_{3T}/3\equiv1\pmod3
$$


coefficientwise: a polynomial of degree at most two over $\mathbb F_3$ that vanishes at all three residues is zero.

Likewise $e_{3T+1}\equiv2\pmod3$ coefficientwise. The block-factorial correction $J$ is $1$ modulo $3$, and the adjacent-factor multiplier is also $1$ modulo $3$. Turn17’s integral, Gauss-norm nonincreasing contraction preserves these congruences and sends the constant input $1$ to $1$. This gives the asserted reductions of $H,G$. Formal inversion of $H$ preserves integrality. ∎

Write


$$
(1+3M)\Theta_{\rm raw}(M)
=68+a_1M+\sum_{r\ge2}a_rM^r.
$$


The retained true jet gives $a_1\equiv3\pmod{27}$; the lemma gives $a_r\in3\mathbb Z_3$ for $r\ge2$. Therefore, for every $m\ge1$,


$$
v_3(a_rM^r)\ge1+2m\ge m+2.
$$


Combining this with the projection theorem yields


$$
\boxed{N\theta\equiv68+3M\pmod{3^{m+2}}\qquad(m\ge1).}
$$



Substitution into the complete factorial expansion proves


$$
\boxed{
Q_n^{\rm loc}\equiv
(y+1)(y-1)^{n-2}
\bigl(3y-71-(n-2)\bigr)
\pmod{3^{v_3(j)+2}},
\qquad 3\mid j.
}
$$



Thus no correction to the proposed core coefficient is required. The proof establishes the stated precision, not that it is always the exact valuation of the polynomial difference.

---

## 7. Precise fixed-depth transfer and its limitations

For every fixed $K\ge1$, on


$$
j=3^Kw,\qquad w\ge1,\qquad n=4^j+1,
$$


the now-closed polynomial interface gives


$$
\boxed{Q_n^{\rm loc}-Q_{\rm core}\in3^{K+2}\mathbb Z_3[y].}
$$


Also


$$
4^j-1\equiv3j\pmod{3^{K+2}},
$$


so equivalently


$$
Q_n^{\rm loc}\equiv
(y+1)(y-1)^{n-2}
\bigl(3y-71-3^{K+1}w\bigr)
\pmod{3^{K+2}}.
$$



For the actual primitive polynomial,


$$
Q_n=\lambda_nQ_n^{\rm loc},\qquad
\lambda_n=\operatorname{lc}(Q_n)/3\in\mathbb Z_3^\times.
$$


The unit is not removable from the actual matrix or its inverse contraction.

This does **not** automatically transfer core inverse valuations. In the original columns $1,y,\ldots,y^{k-1}$, the full metric must still retain its factorial force, every admissible arctangent pole unit, its finite cutoff, and endpoint subtraction. The sufficient inverse-loss conditions recorded in turn27,


$$
P>L_{\rm loss},\qquad
P+2\mu>v_3(\mathscr K_{\rm core}),
$$


must be checked with the actual available precision. Core positivity is not an actual response or denominator theorem.

---

## 8. Final gcd, primitive multiplier and whole error

For $0\le i,j<k=(n+1)/2$, retain


$$
R_{ij}=\sum_{t=0}^nQ_{n,t}
\left(
-(2(i+j+t))!
+
4\sum_{a=1}^{i+j+t}
\frac{(-1)^{i+j+t-a}}{2a-1}
\right).
$$


The complete matrix is


$$
H_{\rm complete}=R+(e+\pi)Q_n(-1)vv^T,
\qquad v_i=(-1)^i.
$$


Write


$$
\det H_{\rm complete}=\beta_0+\beta_1(e+\pi).
$$


For


$$
\ell=\operatorname{lcm}(1,3,\ldots,4n-3),
$$


put


$$
A_\ell=\ell^k\beta_0,\qquad B_\ell=\ell^k\beta_1,\qquad
g_\ell=\gcd(|A_\ell|,|B_\ell|).
$$


When $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


If $d_*$ is the least two-coefficient clearer and $g_*$ its final content, the actual primitive multiplier is


$$
\frac{d_*}{g_*}=\frac{\ell^k}{g_\ell}.
$$


The whole evaluated error remains


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell^k}{g_\ell}
\det H_{\rm complete}.
}
$$


Neither the local congruence nor a row clearer determines this $q$, the final gcd, or decay of this whole error.

---

## Closing ledger

**New rigorous local result.** The actual integral forcing and original-coordinate reconstruction prove the complete radical support with


$$
\theta=3\eta_N\equiv2\pmod3.
$$


All three dangerous factorial terms vanish at the required precision. Together with the retained true-jet/projection result, and the additional coefficient lemma above, this closes the actual polynomial congruence for every $3\mid j$.

**Exact remaining bottleneck.** The global problem still requires actual-coordinate inverse-loss control, evaluation of the complete determinant coefficient pair after its final gcd, and nonzero whole primitive errors tending to zero along an infinite sequence. No proof or disproof of irrationality of $e+\pi$ follows.

**Bounded exact-arithmetic check.** No growing-degree calculation is needed for the symbolic support proof. A useful independent check of the only additional coefficient step has inputs


$$
P_\ell(3T+r),\qquad 0\le\ell\le5,\quad r=0,1,2,3,
$$


with all coefficients reduced modulo $9$, followed by the complete formula for $e_s$. The expected verifiable output is


$$
e_{3T}\equiv3\pmod9,\qquad e_{3T+1}\equiv2\pmod3
$$


**coefficientwise**. The displayed Gauss bound certifies that every omitted $\ell\ge6$ contributes zero at that precision. This checks the $m=1$ extension; it is not a denominator computation or an irrationality certificate.
