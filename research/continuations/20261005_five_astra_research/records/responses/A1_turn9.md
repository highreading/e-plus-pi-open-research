> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## A1 audit verdict

**The geometric-remainder proof passes.** With the factorial normalization in the proposal, it proves the exact normalized endpoint unit, not merely a valuation lower bound:


$$
\boxed{\frac{b}{L!}\equiv2,\qquad
\frac{c\xi_{\rm const}-b\xi_{\rm last}}{L!}\equiv2\pmod3.}
$$


Here


$$
n=3M+2,\quad N=3M+1,\quad L=3M,\quad M\ge1.
$$



The primitive-leading argument also extends to this entire polynomial domain. Consequently,


$$
\boxed{v_3(Q_n(-1))=2v_3(N!)\qquad(n=3M+2,\ M\ge1).}
$$


In particular this holds on every assigned regular index $n=4^j+1,\ j\ge1$.

For the next digit, I obtain **explicit uniform finite-sum formulas**, involving only binomial coefficients and nine-term moment residues, for


$$
c/3\bmod9,\qquad \xi_{\rm last}\bmod9.
$$


They contain no unknown Schur inverse or equivalent unresolved scalar. They give a constructive polynomial lift on the infinite class $3\mid j$, although I do not simplify their outputs to a fixed residue or bounded-state recurrence in $j$.

The orthogonality mechanism explicitly reuses the archive’s dyadic endpoint-doubling strategy. The geometric identity and Pascal factorization are classical.

---

## 1. Normalization and identification of the actual Schur symbols

To avoid the proposal’s double use of $\delta$, write


$$
x=y-1,\qquad \delta_S=c-b^2/a.
$$


Use the actual divided polynomials


$$
\phi_d=\frac{(y+1)x^d}{d!}.
$$


They need not have integral ordinary coefficients. The integral object is their divided-basis lattice and its moment matrix.

Put


$$
b_s^{\rm mom}=\frac{\mu(x^s)}{s!},\qquad
t_s=\mu(\phi_s),\qquad
e_s=\frac{\mu((y+1)^2x^s)}{s!}.
$$


Then, exactly,


$$
t_s=2b_s^{\rm mom}+(s+1)b_{s+1}^{\rm mom},
$$




$$
e_s=4b_s^{\rm mom}+4(s+1)b_{s+1}^{\rm mom}
 +(s+1)(s+2)b_{s+2}^{\rm mom},
$$


and


$$
G_{de}=\mu(\phi_d\phi_e)=\binom{d+e}{d}e_{d+e}.
$$



These formulas confirm the proposal’s factorial normalization. In particular there is no missing $d!$, $L!$, or $(L+d)!$.

Let $E=(G_{de})_{0\le d,e<L}$ and define


$$
\chi_i=\phi_i-\sum_{e<L}(E^{-1}G_{E,i})_e\phi_e,\qquad i=L,N.
$$


The established tensor reduction makes $E$ invertible over $\mathbb Z_3$. Thus the elimination coefficients are $3$-integral **in the divided basis**.

Because all $\phi_d$ vanish at $-1$,


$$
\rho(\phi_dF)=\mu(\phi_dF).
$$


If $\chi_0^{\,*}$ denotes the residual of the constant polynomial after eliminating $E$, orthogonality gives


$$
\rho(\chi_0^{\,*}\chi_i)=\mu(\chi_i).
$$


Therefore the proposal identifies the original Schur quantities correctly:


$$
b=\mu(\chi_L),\qquad
\xi_{\rm const}=\mu(\chi_N),\qquad
c=\mu(\chi_L^2),\qquad
\xi_{\rm last}=\mu(\chi_L\chi_N).
$$


No constant-row correction is missing.

The residue $t_s\equiv2\pmod3$ also checks directly: the moment residues $b_s^{\rm mom}\equiv1,0,1$ in the three residue classes, inserted into the displayed formula for $t_s$, give $2$ in every class.

---

## 2. Exact geometric remainder: full factorial divisibility

The exact identity is


$$
1=\frac{y+1}{2}\sum_{d=0}^{L-1}\left(-\frac{x}{2}\right)^d
  +\left(-\frac{x}{2}\right)^L.
$$


The coefficients of its first term in the $\phi_d$ basis are


$$
\frac{(-1)^d d!}{2^{d+1}}\in\mathbb Z_3.
$$


Orthogonality consequently gives


$$
\mu(\chi_i)=(-2)^{-L}\mu(x^L\chi_i),\qquad i=L,N.
$$



For every $e\ge0$,


$$
\mu(x^L\phi_e)
 =\frac{(L+e)!}{e!}\,t_{L+e}
 =L!\binom{L+e}{e}t_{L+e}.
$$


This includes both leading indices $e=L,N$ and every eliminated index. Because all elimination coefficients are $3$-integral,


$$
\boxed{b,\xi_{\rm const}\in L!\mathbb Z_3.}
$$



This is the decisive replacement for inverse-path bounds: it retains the entire exact remainder and the actual orthogonal projection.

---

## 3. The normalized unit: Lucas and the last Pascal complement

Index the eliminated coordinates as $e=3q+r$, with $0\le q<M$, $0\le r<3$. Write


$$
B_M(q,q')=\binom{q+q'}q,\qquad
A_*=
\begin{pmatrix}
0&2&1\\
2&2&0\\
1&0&0
\end{pmatrix}.
$$


The actual reduction is


$$
\bar E=\bar B_M\otimes\bar A_*.
$$


For the $L=3M$ column,


$$
\overline{G_{E,L}}=\bar k\otimes\bar A_*e_0,
\qquad k_q=\binom{M+q}{q}.
$$


Thus


$$
\overline{E^{-1}G_{E,L}}
 =(\bar B_M^{-1}\bar k)\otimes e_0.
$$


Only the coordinates $e=3q$ survive. This is exactly the support needed in the proposal.

Dividing the geometric identity by $L!$ and reducing gives


$$
\frac b{L!}\equiv
2(-2)^{-L}
\left[
\binom{2L}{L}
-\sum_{q<M}(B_M^{-1}k)_q\binom{L+3q}{3q}
\right]\pmod3.
$$


Lucas applies without any assumption that $M$ is a power:


$$
\binom{2L}{L}\equiv\binom{2M}{M},\qquad
\binom{L+3q}{3q}\equiv\binom{M+q}{q}.
$$



Finally, with $P_M(q,a)=\binom qa$,


$$
B_M=P_MP_M^T,\qquad \det B_M=1.
$$


The last Schur complement in $B_{M+1}$ is therefore exactly


$$
\binom{2M}{M}-k^TB_M^{-1}k=1.
$$


Since $(-2)^{-L}\equiv1\pmod3$,


$$
\boxed{b/L!\equiv2\pmod3.}
$$



The previously proved first lift gives $c\equiv3\pmod9$ and $\xi_{\rm last}\equiv2\pmod3$. These are consistent with the same tensor calculation: the radical norm uses $e_{3r}/3\equiv1$, and its mixed norm uses the tensor entry $(A_*)_{01}=2$, each multiplied by the last Pascal complement $1$.

Hence


$$
\frac{c\xi_{\rm const}-b\xi_{\rm last}}{L!}
\equiv 0-2\cdot2
\equiv2\pmod3.
$$


In particular,


$$
\boxed{
v_3(b)=v_3(L!),\qquad
v_3(c\xi_{\rm const}-b\xi_{\rm last})=v_3(L!).
}
$$


There is no subtraction of valuation lower bounds: the normalized second summand is a unit and the first vanishes modulo $3$.

---

## 4. Primitive normalization on the broader domain

The broader primitive-leading theorem follows from the same actual system; it does not require regularity.

First, $a$ is a unit throughout $n=3M+2$. Indeed the constant-to-$E$ vector reduces to $2\mathbf1$, while $\rho(1)=0$. Since


$$
B_M^{-1}\mathbf1=e_0,\qquad
\mathbf1^TA_*^{-1}\mathbf1\equiv1\pmod3,
$$


one gets


$$
a\equiv-1\pmod3.
$$



As $L\ge3$, the factorial divisibility gives $b\in3\mathbb Z_3$. Therefore


$$
\delta_S=c-b^2/a\equiv3\pmod9.
$$


The last projection coefficient satisfies


$$
\eta_{\rm last}
=\frac{\xi_{\rm last}-(b/a)\xi_{\rm const}}{\delta_S},
$$


so


$$
v_3(\eta_{\rm last})=-1,
$$


and every projection coefficient belongs to $3^{-1}\mathbb Z_3$.

The monic polynomial expansion is


$$
P_n=h_n-N!\eta_{\rm const}
-\sum_{d=0}^{N-1}\frac{N!}{d!}\eta_{d+1}h_{d+1},
\qquad h_{d+1}=(y+1)(y-1)^d.
$$


Thus $3P_n\in\mathbb Z_3[y]$. Its coefficient of $y^{n-1}$, before multiplication by $3$, is


$$
[y^{n-1}]h_n-N\eta_{\rm last}.
$$


Here $N=3M+1$ is a unit, so this coefficient has valuation exactly $-1$. Consequently, if


$$
Q_n=L_nP_n
$$


is the actual primitive integer polynomial with positive leading coefficient, then


$$
v_3(L_n)=1.
$$



Using the exact endpoint formula,


$$
P_n(-1)
=-N!\frac{c\xi_{\rm const}-b\xi_{\rm last}}{a\delta_S},
$$


and $v_3(L!)=v_3(N!)$, proves


$$
\boxed{
v_3(P_n(-1))=2v_3(N!)-1,\qquad
v_3(Q_n(-1))=2v_3(N!).
}
$$


The computed unit proves nonvanishing directly.

---

## 5. New follow-on lemma: explicit Pascal formulas for the next digits

The next digits can be calculated without solving another unspecified Schur system.

Define exact integers


$$
\tau_D=(-1)^{M-D}\binom MD,\qquad 0\le D\le M,
$$


and divided polynomials


$$
r=\sum_{D=0}^M\tau_D\phi_{3D},\qquad
s=\sum_{D=0}^M\tau_D\phi_{3D+1}.
$$


These are integral lifts of the residuals of $\phi_L,\phi_N$ modulo $3$. In particular their pairings with every eliminated coordinate are divisible by $3$.

Set


$$
R=\sum_{D,E=0}^M
 \tau_D\tau_E
 \binom{3(D+E)}{3D}e_{3(D+E)},
$$




$$
X=\sum_{D,E=0}^M
 \tau_D\tau_E
 \binom{3(D+E)+1}{3D}e_{3(D+E)+1},
$$


and, for $0\le i<L$,


$$
u_i=\frac13\sum_{D=0}^M
 \tau_D\binom{i+3D}{i}e_{i+3D}.
$$


Every $u_i$ is an integer. Also $R$ is divisible by $3$.

Let


$$
J=B_M^{-1}\otimes A_*^{-1}.
$$


There is no unknown inverse here: explicitly,


$$
(B_M^{-1})_{qr}
=(-1)^{q+r}
\sum_{a=\max(q,r)}^{M-1}\binom aq\binom ar,
$$


and


$$
A_*^{-1}=
\begin{pmatrix}
0&0&1\\
0&\tfrac12&-1\\
1&-1&2
\end{pmatrix}.
$$



Then the required digits are


$$
\boxed{
\frac c3\equiv\frac R3-3u^TJu\pmod9,\qquad
\xi_{\rm last}\equiv X\pmod9.
}
\tag{*}
$$



### Proof

Write $v_i=\mu(\phi_i r)=3u_i$ and $w_i=\mu(\phi_i s)$, so $w\in3\mathbb Z_3^L$. Exact elimination gives


$$
c=\mu(r^2)-v^TE^{-1}v,
$$




$$
\xi_{\rm last}=\mu(rs)-v^TE^{-1}w.
$$


As $E^{-1}\equiv J\pmod3$,


$$
v^TE^{-1}v\equiv9u^TJu\pmod{27}.
$$


The mixed correction is divisible by $9$. These establish $(*)$.

Thus only $e_s\bmod27$ is needed for $R$, and only $e_s\bmod9$ for $u,X$.

### Uniform bounded moment precision

For either precision, use


$$
b_s^{\rm mom}\equiv
\sum_{\ell=0}^{\min(s,8)}
 \binom{s}{\ell}(-2)^{s-\ell}
 (s+1)\cdots(s+\ell)
 \pmod{27}.
$$


Every omitted rising factorial with $\ell\ge9$ is divisible by $27$, because its valuation is at least $v_3(\ell!)\ge4$. Insert these nine-term residues into the exact formula for $e_s$.

This supplies a uniform finite-sum residue rule for every $M$. Its summation ranges grow with $M$; it is **not** a claimed bounded-state recurrence or a proof that the output is constant on an infinite class.

---

## 6. Audit of the polynomial digit on $3\mid j$

Now let


$$
n=4^j+1,\qquad j\ge1,\quad 3\mid j.
$$


Then $j\ge3$ and


$$
v_3(N-1)=v_3(4^j-1)=1+v_3(j)\ge2.
$$


For every $d\le N-2$, $N!/d!$ therefore contains a factor $9$. Since all $3\eta_i$ are integral, these lower nonconstant terms vanish modulo $9$ in $3P_n$. The constant term also vanishes, by the endpoint theorem.

Writing


$$
\theta_M=3\eta_{\rm last}\pmod9,
$$


gives


$$
\boxed{
3P_n(y)\equiv
(y+1)(y-1)^{N-1}
\bigl(3(y-1)-N\theta_M\bigr)\pmod9.
}
$$



The deep corrections really disappear:


$$
3\eta_{\rm last}
=\frac{\xi_{\rm last}-(b/a)\xi_{\rm const}}
       {c/3-b^2/(3a)}
\equiv \frac{\xi_{\rm last}}{c/3}\pmod9.
$$


Indeed $v_3(b),v_3(\xi_{\rm const})\ge v_3(63!)=30$ on this class. Formula $(*)$ therefore supplies $\theta_M$ explicitly.

For the **actual primitive polynomial** one must retain the global unit:


$$
\boxed{
Q_n(y)\equiv
\frac{L_n}{3}\,
(y+1)(y-1)^{N-1}
\bigl(3(y-1)-N\theta_M\bigr)\pmod9.
}
$$


Thus $3P_n\bmod9$ is the locally normalized primitive ray, not necessarily literally $Q_n\bmod9$.

At $n=65$, the supplied finite residues $c/3=4$, $\xi_{\rm last}=2\pmod9$ give


$$
\theta_M=2\cdot4^{-1}=5\pmod9.
$$


Since $64\equiv1\pmod9$,


$$
\boxed{3P_{65}\equiv(y+1)(y-1)^{63}(3y+1)\pmod9.}
$$


The digit derivation passes. The supplied numerical residues remain finite evidence unless independently recomputed; they are not used in the infinite endpoint proof.

---

## 7. Full endpoint gcd and whole evaluated error

The polynomial theorem does not determine the reduced rational-center denominator. Retain


$$
A=t_R\det K-z^T\operatorname{adj}(K)z,\qquad
B=\ell Q_n(-1)\det K,
$$




$$
g=\gcd(|A|,|B|),\qquad
q=\frac{|B|}{g},\qquad
p=-\frac{\operatorname{sgn}(B)A}{g}.
$$


The new exact input is


$$
v_3(B)=v_3(\ell)+2v_3(N!)+v_3(\det K).
$$


The actual denominator remains


$$
v_3(q)=\max\{0,v_3(B)-v_3(A)\}.
$$



For $k=(n+1)/2$ on the regular family, the whole error is still


$$
\boxed{
q(e+\pi)-p
=\frac{\operatorname{sgn}(B)}g\bigl(A+B(e+\pi)\bigr)
=\frac{\operatorname{sgn}(B)\ell^k}{g}\det H_{\rm complete}.
}
$$


All rational arctangent terms and both periods are retained. The inherited regular-family nonvanishing result supplies $B\ne0$, and the inherited distinct-center result supplies nonzero whole errors apart from at most one index. The new polynomial theorem alone supplies neither fact about the complete matrix nor decay of the whole error.

### (1) New result and proof status

**Proved:** the coordinator’s normalized endpoint-unit theorem; its transfer to the actual primitive endpoint; extension to every polynomial degree $n=3M+2,\ M\ge1$; and the explicit next-digit formulas $(*)$, which use only known Pascal algebra and bounded-precision moment sums.

**Audited:** the locally normalized $Q\bmod9$ derivation on $3\mid j$, including the $n=65$ specialization conditional on its supplied finite residues.

No irrationality or rationality conclusion for $e+\pi$ follows.

### (2) Exact remaining bottleneck

At the polynomial level, simplify the explicit sums $(*)$ to a fixed residue law or bounded-state recurrence if one exists. Literal primitive $Q\bmod9$ additionally retains the unit $L_n/3\bmod9$.

At the complete-center level, A4’s distinguished rational-arctangent Schur coordinate and the final gcd remain unresolved. Endpoint factorial depth cannot replace those quantities.

### (3) Bounded computation request

For **$M=21$, $n=65$ only**, evaluate the explicit formulas in Section 5:

- $R\bmod27$;
- $u\bmod3$ and $u^TJu\bmod3$;
- $X\bmod9$;
- $(R/3-3u^TJu)\bmod9$.

Expected verifiable outputs are


$$
R/3-3u^TJu\equiv4,\qquad X\equiv2,\qquad\theta_M\equiv5\pmod9.
$$


Retain the intermediate vector and sums as a certificate. This is an independent binomial-sum audit of the existing finite control, not another unit-block Gaussian elimination and not evidence sufficient for an infinite residue pattern.
