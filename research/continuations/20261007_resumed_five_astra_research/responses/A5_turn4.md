> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5 Turn 4 — Integral torsion in the observable quotient, an exact force identity, and bounds for the actual content

## Executive summary

The rationality or irrationality of $e+\pi$ remains unresolved. In particular, this report does **not** produce the requested infinite-family primitive relative law


$$
E-r(u)Q\equiv0\pmod{2^K},
$$


nor an independently specified $r(u)$ and certificates proving such a law.

There are, however, three new rigorous results.

1. **The derivative-image obstruction can be described exactly at terminal acceptance.**  
   After the corrected integral evaluator has terminated, its three derivative images do not constitute the full acceptance kernel. The quotient contains explicit $2$-primary torsion:
   

$$
\boxed{
   \bigoplus_{(k,l)\in\mathbb Z^2}
   \mathbb Z/\gcd(2^L,k,l)\mathbb Z .
   }
$$


   The $(0,0)$-coordinate is the actual acceptance. The other surviving coordinates are genuine integral obstructions to a derivative certificate, although they are invisible to acceptance. Thus characteristic-zero reduction loses precisely relevant information.

2. **An accessible exact identity evaluates the beginning of the actual normalized force on every original index.**  
   Writing $h=n/2=2001b$, the identity gives
   

$$
\mathfrak f_0\equiv2\pmod8,\qquad
   \mathfrak f_1\equiv1\pmod8,\qquad
   \mathfrak f_2\equiv3\pmod8,\qquad
   \mathfrak f_3\equiv1\pmod4,
$$


   and the complete parity profile
   

$$
\boxed{\mathfrak f_i\equiv
   \begin{cases}
   1,&i=1,2,3,\\
   0,&\text{otherwise}
   \end{cases}\pmod2.}
$$


   These are infinite-original-family statements, not extrapolations from auxiliary data.

3. **The actual first-column content admits a proved, inexpensive bound.**  
   For the content convention $x=2^a x_0$, with $x_0$ primitive over $\mathbb Z_2$,
   

$$
\boxed{0\le a\le \lfloor\log_2(n+3)\rfloor-1.}
$$


   Stronger source-dependent bounds are available from two explicitly odd reconstructed contact differences:
   

$$
\boxed{
   a\le
   \min\left\{
   v_2\binom{n+2}{b-4},
   v_2\binom{n+2}{b-3}
   \right\}-1.
   }
$$


   Their right-hand sides require only binary digit counts of integers of size $O(\log n)$, not an original-size matrix.

These results remove an unproved nonnegativity assumption on $a$, bound its possible size, and identify the exact integral failure of the proposed derivative-image strategy. They do not evaluate the constant coordinate of the actual paid relative numerator.

---

## 1. Original objects and retained scope

Throughout this report,


$$
\boxed{b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.}
$$


The contact matrix has indices $0\le i,j<b$. Physical reconstruction has rows $0\le j\le b$.

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


The finite matrix and normalized force are


$$
A_{ij}
=
\sum_{s=0}^{n+i}
\lambda_s\binom{n+i}{s}\binom{2n+i-s}{j},
$$




$$
f_i^0=
\frac{(n+i)!}{n!}[t^n](1+2t+2t^2)^n(1+t)^i,
\qquad
\mathfrak f_i=\frac{f_i^0}{R}.
$$



For a physical contact vector,


$$
(\mathcal Rz)_j=W_j(jz_{j-1}-z_j),
\qquad z_{-1}=z_b=0.
$$


The corrected columns remain


$$
x=\frac12\mathcal RA^{-1}\mathfrak f,\qquad
y=\frac{\mathcal RA^{-1}(h^e+h^F)+e_0}{4b!}.
$$


In particular, the logarithmic force $h^F$ has not been removed.

Write


$$
z^f=A^{-1}\mathfrak f,\qquad
z^k=A^{-1}k,\qquad
k=\frac{h^e-A(j!)_{0\le j<b}}{b!}.
$$


With $\Delta_jz=jz_{j-1}-z_j$, retain the complete raw forms


$$
\mathcal U=
\sum_{j=0}^{b-1}W_j^2(\Delta_jz^f)^2
+b^2W_b^2(z^f_{b-1})^2,
\tag{1.1}
$$




$$
\mathcal V=
\sum_{j=0}^{b-1}W_j^2(\Delta_jz^f)(\Delta_jz^k)
+W_b^2\,bz^f_{b-1}(bz^k_{b-1}+1).
\tag{1.2}
$$


Thus


$$
\boxed{
Q=2^{-2a-2}\mathcal U,\qquad
E=2^{-a-3}\mathcal V.
}
\tag{1.3}
$$



### 1.1 Reused assembly, without repeating its audits

At raw precision $2^L$, retain


$$
I=\min(b-1,8L-2),\quad m=4(L-1),\quad
T=\min(2L-1,2n-1),\quad V=T+m.
$$


The established filtrations are used at exactly this scope:


$$
\mathfrak f_i\equiv0\pmod{2^L}\quad(i>I),\qquad
\lambda_s\equiv c_s\equiv0\pmod{2^L}\quad(s>m).
$$


The complete source is


$$
k=\sum_{t=0}^{2n-1}\frac{(b+t)!}{b!}\mathbf a_{b+t},
$$


with paid prefix


$$
s=\sum_{t=0}^T a_te_{b+t},\qquad a_t=\frac{(b+t)!}{b!}.
$$



The finite completion retains


$$
\eta_f=U_n^{(m)}KS^{-1}D_f,
$$




$$
\xi_v=
\sum_{t=0}^Ta_t
\sum_{\substack{0\le r\le t\\0\le v-r\le m}}
\binom n{t-r}\lambda_{v-r}\binom{b+v}{v-r},
$$




$$
\delta=KS^{-1}G^{[V]}\xi-\xi,\qquad
\theta_v=\sum_{w=v}^V\binom n{w-v}\delta_w.
\tag{1.4}
$$


Here $K,S,D_f,G^{[V]}$ are the finite Schur data of the supplied type-$2$ assembly; the $K$-term is zero-padded beyond its actual coordinates. No return term in (1.4) is omitted.

The completed polynomial-vector identities are


$$
\widehat z^f\equiv\overline z^f,\qquad
\widehat z^k\equiv\overline z^k-s\pmod{2^L}.
\tag{1.5}
$$


They follow from the finite completion and inverse-operator proofs, not from the new $25$-position receipt.

Indeed,


$$
\Delta_js=
\begin{cases}
-1,&j=b,\\
0,&b<j\le b+T,\\
a_{T+1},&j=b+T+1,\\
0,&\text{otherwise}.
\end{cases}
\tag{1.6}
$$


Consequently, exterior pairing with $\widehat z^f$ retains the physical contribution at $b$, while the high endpoint pairs with zero modulo the raw modulus. This is the proof mechanism for assembled tail/terminal cancellation. It does not set the physical value $z_b^k$ equal to $-1$.

Both differential boundaries remain:


$$
\mathscr L_n
\left(
\frac{\phi^ng_n-e^z\phi^nU_b}{b!}
\right)
=e^z\phi^{n+1}(C_{b-1}+C_b).
\tag{1.7}
$$



The corrected coefficient evaluator is reused under


$$
\boxed{n>4(I+2m+T+4)+2.}
\tag{1.8}
$$


Its denominator transition uses


$$
(1-t)^2=(1-t^2)-2t(1-t),
$$


not the false earlier identity.

### 1.2 Scope of the new finite receipt

The supplied receipt establishes its stated auxiliary case:


$$
b=2,\quad n=8004,\quad L=3.
$$


Its nonzero exterior observations are


$$
4(F_0^2+F_1^2),\qquad 6F_0+2F_1\pmod8.
$$


The exact high endpoint is $-20160$, before reduction. These values are consistent with the complete-boundary argument and are stronger evidence than zero-tail checks.

They are not an infinite law, a primitive-content computation, or an evaluation of an original index. None of the closed audits is repeated below.

---

## 2. A new exact identity for the actual normalized force

The force calculation can be reduced to short sums without first extracting a coefficient of degree $n$.

Put


$$
P(t)=1+2t+2t^2,\qquad
C_m=[t^m]P(t)^{2h},
$$


and define


$$
A_h=\frac{C_{2h}}{R},\qquad
B_h=\frac{C_{2h-1}}{R}.
$$


Thus $A_h=\mathfrak f_0$.

For $0\le j\le h$, set


$$
T_j=
\frac{2^j\bigl(h(h-1)\cdots(h-j+1)\bigr)^2}{(2j)!},
\qquad T_0=1.
\tag{2.1}
$$



### Theorem 2.1 — Exact central and adjacent force identities

One has


$$
\boxed{A_h=\sum_{j=0}^hT_j,}
\tag{2.2}
$$




$$
\boxed{
B_h=\sum_{j=0}^{h-1}\frac{h-j}{2j+1}T_j.
}
\tag{2.3}
$$


Moreover,


$$
\boxed{
v_2(T_j)=v_2(j!)+2v_2\binom hj.
}
\tag{2.4}
$$



#### Proof

For the central coefficient, choose $h-j$ quadratic factors, $2j$ linear factors, and $h-j$ constant factors. Their contribution, divided by


$$
R=2^h(2h)!/(h!)^2,
$$


is exactly $T_j$.

For the adjacent coefficient, choose $h-j-1$ quadratic factors, $2j+1$ linear factors, and $h-j$ constant factors. Division by $R$ gives


$$
\frac{2^j(h!)^2}
{(h-j-1)!(h-j)!(2j+1)!}
=\frac{h-j}{2j+1}T_j.
$$



Finally,


$$
h(h-1)\cdots(h-j+1)=j!\binom hj,
$$


and


$$
v_2((2j)!)=2j-s_2(j),\qquad
v_2(j!)=j-s_2(j).
$$


Substitution proves (2.4). ∎

Every summand in (2.2)–(2.3) is $2$-adically integral. The apparent factorial denominators are therefore manageable exact divisions, not inversions of even elements.

---

## 3. Evaluation on every original index

The original parameter word gives


$$
b=9^{18+32u}\equiv17\pmod{32},
$$


because $9^2\equiv17\pmod{32}$, $9^4\equiv1\pmod{32}$, and $18+32u\equiv2\pmod4$. Therefore


$$
\boxed{h=2001b\equiv1\pmod{32}.}
\tag{3.1}
$$



For $j=0,1$,


$$
T_0=1,\qquad T_1=h^2.
$$


For $j=2,3$, the hypothesis $h\equiv1\pmod4$ makes $\binom hj$ even. Thus (2.4) gives $v_2(T_j)\ge3$. For $j\ge4$,


$$
v_2(j!)\ge3.
$$


It follows that


$$
A_h\equiv1+h^2\equiv2\pmod8.
\tag{3.2}
$$



In (2.3), the $j=0$ term is $h$. The $j=1$ term is


$$
\frac{h-1}{3}h^2,
$$


which vanishes modulo $8$ by (3.1). All terms with $j\ge2$ also vanish modulo $8$. Hence


$$
\boxed{B_h\equiv h\equiv1\pmod8.}
\tag{3.3}
$$



### 3.1 An exact recurrence for the full force

Let


$$
F_i=\mathfrak f_i.
$$


Then


$$
F_0=A_h,\qquad F_1=(n+1)(A_h+B_h),
\tag{3.4}
$$


and, for $i\ge0$,


$$
\boxed{
\begin{aligned}
2F_{i+2}={}&(4n+4i+6)F_{i+1}\\
&-(3i+n+2)(n+i+1)F_i\\
&+i(n+i)(n+i+1)F_{i-1},
\end{aligned}}
\tag{3.5}
$$


where the last term is zero for $i=0$.

#### Derivation

Put


$$
M_i=[t^n]P(t)^n(1+t)^i.
$$


With $z=1+t$, this is the residue at $z=1$ of


$$
z^i\frac{(2z^2-2z+1)^n}{(z-1)^{n+1}}.
$$


The residue of a derivative is zero. Apply this to the product of that weight with


$$
a(z)z^i,\qquad
a(z)=(z-1)(2z^2-2z+1)=2z^3-4z^2+3z-1.
$$


Direct differentiation gives


$$
\begin{aligned}
0={}&(2i+2n+4)M_{i+2}
-(4i+4n+6)M_{i+1}\\
&+(3i+n+2)M_i-iM_{i-1}.
\end{aligned}
$$


Multiplying by $(n+i+1)!/(n!R)$ gives (3.5). ∎

The recurrence has an exact division by $2$. Its use modulo a power of $2$ must therefore retain one extra bit for every unprotected recurrence step.

### 3.2 Complete parity profile

There is also an integral expression avoiding the first recurrence division:


$$
F_2=(n+1)\bigl((3h+2)A_h+(4h+3)B_h\bigr).
\tag{3.6}
$$


Using $h\equiv1\pmod8$, (3.2), and (3.3),


$$
F_0\equiv2,\qquad F_1\equiv1,\qquad F_2\equiv3\pmod8.
$$


Equation (3.5) at $i=1$, evaluated modulo $8$, gives


$$
2F_3\equiv2\pmod8,
$$


so $F_3\equiv1\pmod4$.

At $i=2$, the same recurrence modulo $4$ gives $2F_4\equiv0\pmod4$. At $i=3$, it gives $2F_5\equiv0\pmod4$; at $i=4$, it gives $2F_6\equiv0\pmod4$.

The established force filtration gives $F_i\equiv0\pmod2$ for every $i\ge7$. We have therefore proved:

### Theorem 3.1 — Actual original-family force parity

For every original index,


$$
\boxed{
\mathfrak f_i\equiv
\mathbf1_{i=1}+\mathbf1_{i=2}+\mathbf1_{i=3}\pmod2.
}
\tag{3.7}
$$



This evaluates the entire force modulo $2$, including its tail.

---

## 4. The actual contact solution modulo $2$

At $L=1$, the established symbol filtration gives


$$
\lambda_s\equiv0\pmod2\qquad(s>0).
$$


Consequently, on the original finite contact range,


$$
A\equiv P_{\mathrm{Pascal}}U_{2n}\pmod2,
\tag{4.1}
$$


where


$$
(P_{\mathrm{Pascal}})_{ij}=\binom ij,\qquad
(U_{2n})_{ij}=\binom{2n}{j-i}.
$$


Both finite triangular factors have diagonal $1$. Thus $A$ is invertible over $\mathbb Z_2$. This is consistent with, and does not bypass, the complete Schur solve: reducing that solve modulo $2$ eliminates $K$ and leaves exactly (4.1).

Let


$$
q=P_{\mathrm{Pascal}}^{-1}\mathfrak f.
$$


By (3.7),


$$
q_j\equiv\binom j1+\binom j2+\binom j3
\equiv
\begin{cases}
0,&j\equiv0\pmod4,\\
1,&j\not\equiv0\pmod4.
\end{cases}
\pmod2.
\tag{4.2}
$$



Since $2n=4h$,


$$
(1+z)^{-4h}\equiv(1+z^4)^{-h}\pmod2.
$$


Thus


$$
z^f_j
\equiv q_j\sum_{\ell=0}^{\lfloor(b-1-j)/4\rfloor}\binom{-h}{\ell}
\pmod2.
$$


Modulo $2$, the negative-binomial signs disappear, and hockey-stick summation gives


$$
\boxed{
z^f_j\equiv
q_j\binom{h+r_j}{r_j}\pmod2,\qquad
r_j=\left\lfloor\frac{b-1-j}{4}\right\rfloor.
}
\tag{4.3}
$$



Write $b=4d+1$. For $0\le s<d$,


$$
z^f_{4s}=0,
$$




$$
z^f_{4s+1}=z^f_{4s+2}=z^f_{4s+3}
=\binom{h+d-s-1}{d-s-1}\pmod2.
\tag{4.4}
$$


In particular,


$$
\boxed{
z^f_{b-4}=z^f_{b-3}=z^f_{b-2}=1,\qquad
z^f_{b-1}=0\pmod2.
}
\tag{4.5}
$$



These are actual contact residues at original indices.

---

## 5. Bounds for the actual content

Let $N=n+2$. Since $h\equiv1\pmod{32}$,


$$
N=2h+2\equiv4\pmod{64}.
\tag{5.1}
$$


Lucas’s theorem implies that $W_j=\binom Nj$ can be odd only if $j\equiv0\pmod4$.

For such $j<b$, (4.4) gives $z^f_j\equiv0\pmod2$, and $jz^f_{j-1}\equiv0\pmod2$. Therefore $\Delta_jz^f$ is even. At every other contact row $W_j$ is even. At the physical terminal, $b$ is odd and $W_b$ is even.

Thus $\mathcal Rz^f$ is even in every physical row, proving


$$
\boxed{x=\tfrac12\mathcal Rz^f\in\mathbb Z_2^{b+1},\qquad a\ge0.}
\tag{5.2}
$$



For an upper bound, (4.5) gives


$$
\Delta_{b-4}z^f\equiv1,\qquad
\Delta_{b-3}z^f\equiv1\pmod2.
\tag{5.3}
$$


Hence the actual content satisfies


$$
\boxed{
a\le
\min\{v_2(W_{b-4}),v_2(W_{b-3})\}-1.
}
\tag{5.4}
$$


This is not a bound for a computational clearer. It is a bound for the actual reconstructed first column.

Using


$$
v_2\binom Nj=s_2(j)+s_2(N-j)-s_2(N),
$$


the two scalar bounds are


$$
\begin{aligned}
v_2(W_{b-4})
&=s_2(b-4)+s_2(4001b+6)-s_2(4002b+2),\\
v_2(W_{b-3})
&=s_2(b-3)+s_2(4001b+5)-s_2(4002b+2).
\end{aligned}
\tag{5.5}
$$



For a simpler uniform bound, Kummer’s theorem bounds the number of binary carries by $\lfloor\log_2(N+1)\rfloor$. Therefore


$$
\boxed{
0\le a\le \lfloor\log_2(n+3)\rfloor-1.
}
\tag{5.6}
$$



### 5.1 A sharper concrete content bottleneck

The parity formulas also show that if $W_j$ is even, then


$$
W_j\Delta_jz^f\equiv0\pmod4.
\tag{5.7}
$$


Only the case $v_2(W_j)=1$ needs explanation.

Such a $j$ is even. If $j\equiv0\pmod4$, then $\Delta_jz^f$ is already even. If $j=4s+2$, the condition $v_2(W_j)=1$ implies


$$
\binom{N-1}{j-1}\equiv1\pmod2.
$$


Since $N-1\equiv3\pmod8$, this forces $s$ even. But $d=(b-1)/4$ is even, so $d-s-1$ is odd. As $h$ is odd,


$$
\binom{h+d-s-1}{d-s-1}\equiv0\pmod2.
$$


Equation (4.4) again makes the reconstructed difference even.

At an odd-weight row, $j\equiv0\pmod4$, so


$$
x_j\equiv-\frac{z^f_j}{2}\pmod2.
$$


The terminal cannot contribute an odd $x_b$. We obtain the exact criterion


$$
\boxed{
a=0
\iff
\text{there exists }0\le j<b
\text{ with }\binom{n+2}{j}\text{ odd and }z^f_j\equiv2\pmod4.
}
\tag{5.8}
$$



This is a concrete follow-on lemma: evaluate the actual inverse modulo $4$ on the Lucas mask of $n+2$. It is substantially more specific than an unrestricted search for a nonzero reconstructed row.

---

## 6. What the complete source gives at this depth

Modulo $2$, every factorial-prefix coefficient except $a_0$ vanishes because $b+1$ is even. The complete source therefore reduces to the exterior column at $b$.

Using the finite factorization (4.1), its contact solution is


$$
\boxed{
z^k_j\equiv-\binom{-2n}{b-j}\pmod2,\qquad 0\le j<b.
}
\tag{6.1}
$$


For example, this follows by applying $U_{-2n}$ to the contact truncation of $U_{2n}e_b$: the omitted exterior coordinate is precisely $e_b$.

Because $4\mid2n$, (6.1) is supported only on $j\equiv b\equiv1\pmod4$. Hence $\mathcal Rz^k$ is even at all contact rows. Together with (5.2),


$$
\mathcal U\equiv0\pmod4,\qquad
\mathcal V\equiv0\pmod4.
\tag{6.2}
$$


These are raw congruences, not primitive digits.

There is also an original-family distinction from the auxiliary $b=2$ receipt. Since


$$
v_2(W_b)\ge2,\qquad z^f_{b-1}\equiv z^k_{b-1}\equiv0\pmod2,
$$


the actual physical terminals satisfy


$$
b^2W_b^2(z^f_{b-1})^2\equiv0\pmod{64},
$$




$$
W_b^2\,bz^f_{b-1}(bz^k_{b-1}+1)\equiv0\pmod{32}.
\tag{6.3}
$$


They are retained, not deleted. These bounds do not justify removing them after arbitrarily deep primitive division.

---

## 7. Exact integral obstruction to the derivative-image approach

The common-tuple consolidation is integral: multiplying a class polynomial by


$$
t^{\bar B-B_\tau}
\prod_i(1+v_i)^{N_{i,\tau}-\bar N_i}
(1-t)^{\bar M-M_\tau}
$$


puts it over the common tuple without division. This validates the algebraic consolidation independently of any finite receipt.

Continue the corrected evaluator until


$$
N_1=N_2=N_3=N_4=B_{\rm tar}=0.
$$


Acceptance is then


$$
[t^0X^0Y^0]\frac{P}{(1-t)^M}
=[X^0Y^0]P(0,X,Y).
\tag{7.1}
$$


Discarding positive $t$-degree at this stage is exact for acceptance; it is not an assertion that those terms are derivative images.

Let


$$
R_L=\mathbb Z/2^L\mathbb Z,\qquad
\mathscr A_L=R_L[X^{\pm1},Y^{\pm1}].
$$


The projected derivative operators are


$$
\overline{\mathscr D}_X(H)=D_X((1+X)H),
$$




$$
\overline{\mathscr D}_Y(H)=D_Y((1+Y^{-1})H),
\qquad
\overline{\mathscr D}_t(H)=0.
\tag{7.2}
$$



### Theorem 7.1 — Full projected integral derivative quotient

There is a coefficientwise isomorphism


$$
\boxed{
\frac{\mathscr A_L}
{\operatorname{im}\overline{\mathscr D}_X+
 \operatorname{im}\overline{\mathscr D}_Y}
\cong
\bigoplus_{(k,l)\in\mathbb Z^2}
\mathbb Z/\gcd(2^L,k,l)\mathbb Z.
}
\tag{7.3}
$$


The summands have finite support for each Laurent polynomial. The $(0,0)$-summand is $R_L$ and is exactly acceptance.

#### Proof

For every Laurent polynomial $F$,


$$
F(X,Y)-F(-1,Y)
$$


is divisible by $1+X$ in the integral Laurent ring. Therefore


$$
D_XF
=
D_X\!\left((1+X)
\frac{F(X,Y)-F(-1,Y)}{1+X}\right).
$$


It follows that


$$
\operatorname{im}\overline{\mathscr D}_X=\operatorname{im}D_X.
$$


The same argument, using evaluation at $Y=-1$, gives


$$
\operatorname{im}\overline{\mathscr D}_Y=\operatorname{im}D_Y.
$$



On the monomial $X^kY^l$,


$$
D_X(X^kY^l)=kX^kY^l,\qquad
D_Y(X^kY^l)=lX^kY^l.
$$


Thus its coefficient is reduced modulo the ideal generated by $k,l,2^L$. Different monomials do not interact. This proves (7.3). ∎

### 7.1 An explicit surviving torsion direction

The polynomial $X^2$ has zero acceptance, but its class is nonzero modulo the derivative images for every $L\ge1$. Its coefficient survives modulo $2$.

On the other hand,


$$
\overline{\mathscr D}_X(X-1)=2X^2.
\tag{7.4}
$$


Thus its class has exact order $2$.

This is a genuine obstruction at terminal acceptance, within the small support boxes relevant to the evaluator. It is not caused by a large artificial pole or a large support choice.

More generally, a nonconstant monomial survives whenever both exponents are even, with order


$$
2^{\min(L,v_2(k),v_2(l))},
$$


using $v_2(0)=+\infty$.

### 7.2 Explicit integral reduction, including all divisions

For $k\in\mathbb Z$, put


$$
T_k(X)=\frac{X^k-(-1)^k}{1+X},
$$


and for $l\in\mathbb Z$,


$$
S_l(Y)=\frac{Y^l-(-1)^l}{1+Y^{-1}}.
$$


These are integral Laurent polynomials; the displayed divisions are exact polynomial divisions, not introduced poles. They satisfy


$$
\overline{\mathscr D}_X(T_kY^l)=kX^kY^l,
$$




$$
\overline{\mathscr D}_Y(X^kS_l)=lX^kY^l.
\tag{7.5}
$$



For a coefficient $C_{kl}$, set


$$
g_{kl}=\gcd(2^L,k,l).
$$


Choose an integer remainder $\rho_{kl}$ modulo $g_{kl}$, and integers


$$
\alpha_{kl}k+\beta_{kl}l+\gamma_{kl}2^L=g_{kl}.
$$


The division


$$
q_{kl}=\frac{C_{kl}-\rho_{kl}}{g_{kl}}
$$


is exact. Equations (7.5) then give a coefficientwise integral certificate reducing $C_{kl}X^kY^l$ to $\rho_{kl}X^kY^l$.

This supplies explicit projected $H_X,H_Y$, with $H_t=0$, **once the actual coefficients are supplied**. It does not prove that their residual torsion coordinates vanish.

Over characteristic zero, every nonzero $g_{kl}$ becomes invertible, leaving only the constant coordinate. That is precisely why the supplied characteristic-zero telescoping literature does not settle the integral problem.

---

## 8. Application to the actual paid relative numerator

For an independently specified integral candidate $r(u)$, use


$$
c=\max(2a+2,a+3).
$$


The actual paid relative numerator is


$$
\boxed{
N_r=
2^{c-a-3}\mathcal V
-r(u)\,2^{c-2a-2}\mathcal U,
\qquad
E-r(u)Q=2^{-c}N_r.
}
\tag{8.1}
$$


All exponents in (8.1) are nonnegative. The new content theorem validates this normalization with the actual $a\ge0$, but does not replace $a$ by its upper bound in the definition.

At raw precision $L=K+c$, let the actual completed assembly and corrected evaluator produce terminal polynomials $P_E^{\rm fin},P_Q^{\rm fin}$. Define


$$
P_r^{\rm fin}
=
2^{c-a-3}P_E^{\rm fin}
-r(u)\,2^{c-2a-2}P_Q^{\rm fin}.
\tag{8.2}
$$


Theorem 7.1 applies to this actual polynomial, not merely to arbitrary formal kernels.

It separates two distinct questions:

* **Acceptance question:** is the constant coefficient of
  $P_r^{\rm fin}(0,X,Y)$ zero modulo $2^{K+c}$?
* **Derivative-certificate question:** in addition, do all nonconstant coefficients satisfy their divisibilities by $g_{kl}$?

The second condition is stronger. A failure of a derivative-image search can therefore be entirely unrelated to failure of the relative law.

Conversely, a generic characteristic-zero decomposition can hide powers of $2$ in the coefficients required to remove these torsion coordinates. Those powers must be paid before primitive division.

### What has not been obtained

No actual value of the constant coordinate in (8.2) has been proved at primitive depth on an infinite original subfamily. No independently specified nontrivial $r(u)$ has been derived from the source. Defining $r$ by $E/Q$ would merely restate the unknown and is not done.

Accordingly, the formulas above are an exact integral quotient theorem and reduction mechanism, **not a completed relative-law certificate**.

---

## 9. A bounded algorithm for the actual force, with explicit payment

The identities of §2 give more than parity information.

For requested precision $2^P$, equation (2.4) implies


$$
v_2(T_j)\ge v_2(j!)\ge\lfloor j/2\rfloor.
$$


Hence terms with $j\ge2P$ vanish modulo $2^P$ in both (2.2) and (2.3). Only $j<2P$ need be evaluated.

Put


$$
d_j=j-s_2(j).
$$


Since


$$
v_2((2j)!)=2j-s_2(j),
$$


one may calculate


$$
T_j=
\frac{(h_{\underline j})^2}{2^{d_j}}
\left(\frac{(2j)!}{2^{\,2j-s_2(j)}}\right)^{-1}.
\tag{9.1}
$$


The power-of-two division is exact; the remaining denominator is odd.

To obtain $T_j\bmod2^P$, it suffices to calculate the numerator before this division modulo


$$
2^{P+d_j}.
$$


Thus knowing $h$ modulo $2^{3P}$ is a safe uniform parameter bound for all $j<2P$. The factors $2j+1$ in (2.3) are odd.

To obtain the entire paid force prefix $F_0,\ldots,F_I\bmod2^L$, choose


$$
\boxed{P=L+I.}
\tag{9.2}
$$


Calculate the seeds modulo $2^P$, then use (3.5), losing at most one bit at each exact division by $2$. This leaves at least the requested $L$ bits.

This is a bounded short-factorial computation. It does not extract a coefficient of degree $n$, and it does not invert an original-size matrix.

---

## 10. A new, sharply bounded arithmetic task

No computation was performed for this report.

A useful new coordinator-authored check would validate the actual-force identities at an original index, without repeating any closed assembly audit.

### Inputs

Take


$$
u=0,\qquad b=9^{18},\qquad n=4002b,\qquad L=8.
$$


Then


$$
I=62,\qquad P=L+I=70.
$$



Use:

* the exact integer $h=2001\cdot9^{18}$;
* $0\le j<140$ in (2.2)–(2.3);
* factorial indices at most $278$;
* seed arithmetic modulo $2^{70}$, with predivision arithmetic modulo at most $2^{209}$;
* recurrence indices $0\le i\le60$.

A direct short-product implementation uses fewer than $4\cdot10^4$ modular multiplications of at most $209$-bit residues, apart from similarly bounded bookkeeping and odd inversions. No contact matrix is requested.

### Expected certifiable output

The output should include:

1. $A_h,B_h\bmod2^{70}$, with the exact powers of $2$ removed in each summand recorded.
2. The actual vector
   

$$
(\mathfrak f_0,\ldots,\mathfrak f_{62})\pmod{256}.
$$


3. Certificates of the recurrence equations at the precisions used before each division.
4. The predicted reductions
   

$$
\mathfrak f_0\equiv2,\quad
   \mathfrak f_1\equiv1,\quad
   \mathfrak f_2\equiv3\pmod8,
$$


   

$$
\mathfrak f_3\equiv1\pmod4,\qquad
   \mathfrak f_4,\mathfrak f_5,\mathfrak f_6\equiv0\pmod2.
$$


5. Optionally, the two binary digit-count bounds in (5.5), with their intermediate integers.

This establishes only the stated finite force computation. The infinite parity and content-bound theorems rest on the proofs above. The check would not evaluate $E$, $Q$, the final gcd, or the whole error.

---

## 11. Remaining arithmetic and analytic obligations

### 11.1 Primitive precision

The required raw depths remain


$$
L_Q=K+2a+2,\qquad L_E=K+a+3.
$$


The new bound on $a$ provides a finite logarithmic upper bound for these depths, but does not justify replacing the actual content by a guessed constant.

The evaluator introduces no additional whole-pair clearing loss. This does not erase the divisions in (1.3), (8.1), or the short factorial calculations.

### 11.2 Logarithmic guard

Retain


$$
\mathcal L_s=s![z^s]\frac{F(z)}{1-z},
\qquad
B_*=n-v_2(b!)-1-2s_2(n)-\ell.
$$


The logarithmic contribution may be omitted only where the original guard protects the requested observation **after all divisions**. None of the new parity, quotient, or content results extends that guard.

### 11.3 Actual clearer and all-prime gcd

The producer normalization remains


$$
\omega_j=j!W_j,\qquad
u_j=\frac{2\Lambda R\,x_j}{\omega_j},\qquad
v_j=\frac{4b!\,y_j}{\omega_j}.
$$


Its actual least simultaneous clearer is


$$
\boxed{
d_B=\operatorname{lcm}_{0\le j\le b}
\{\operatorname{den}(u_j),\operatorname{den}(v_j)\}.
}
$$


No reconstructed row content is divided out.

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
$$


This is the all-prime final gcd, not a binary substitute.

For every prime,


$$
v_p(q_n)=
\max\left\{
v_p\!\left(\frac{\Lambda R}{2b!}\right)
+v_p(\mathcal N)-v_p(\mathcal H),0
\right\}.
$$


The supplied established ternary law is retained at its stated original-family scope:


$$
v_3(q_n)=n-\frac{b+15}{2}.
$$


It has not been recomputed or extended here.

### 11.4 Same-index whole error

Finally,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),\qquad
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
$$


An irrationality proof through this producer still requires, on the same infinitely many original indices, a nonzero whole error and a favorable estimate involving the actual primitive denominator. For example,


$$
0<|q_n(e+\pi)-p_n|\longrightarrow0
$$


would contradict rationality.

Neither the new force residues nor an eventual primitive exponential digit would by itself establish that whole-error statement.

---

## 12. Proof-status ledger and conclusion

| Statement | Status |
|---|---|
| New $b=2$, $25$-position receipt | Accepted only at its stated auxiliary finite scope |
| Completed source/type-$2$ assembly and corrected evaluator | Reused with their exact hypotheses and full boundaries |
| Exact central and adjacent normalized-force identities | **Newly proved** |
| Complete actual force parity on all original indices | **Newly proved** |
| Actual contact solution modulo $2$ | **Newly proved** |
| Nonnegativity and logarithmic upper bound for actual $a$ | **Newly proved** |
| Stronger endpoint digit-count bound for $a$ | **Newly proved** |
| Exact criterion (5.8) for $a=0$ | **Newly proved; criterion not yet evaluated** |
| Full terminal projected derivative quotient | **Newly proved** |
| Nonconstant $2$-primary torsion invisible to acceptance | **Explicitly exhibited and classified** |
| Actual source-dependent $r(u)$ and primitive relative certificate | Open |
| Infinite-original nonzero primitive $E$ digit | Open |
| Same-index actual denominator versus nonzero whole error | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

The new results are substantive but local. The exact force identity evaluates genuine original-family information and yields the first proved bounds here for the actual content:


$$
\boxed{0\le a\le \lfloor\log_2(n+3)\rfloor-1.}
$$



The image approach has a precise obstruction, not merely an unsuccessful search: its integral quotient contains nonconstant torsion directions which characteristic-zero reduction removes by division. Even after those directions are understood, the constant coordinate of the actual paid relative numerator remains unevaluated.

The next sharply defined tasks are therefore:

1. use the complete modulo-$4$ solve to evaluate criterion (5.8), rather than assume $a=0$;
2. evaluate the constant coordinate of the actual paid relative terminal polynomial for an independently specified $r(u)$, on an explicit infinite original subfamily;
3. then control the actual all-prime denominator and nonzero whole error on those same indices.

No unconditional rationality or irrationality conclusion for $e+\pi$ follows at the present stage.
