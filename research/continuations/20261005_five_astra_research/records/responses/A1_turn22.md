> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1 — partial sixth-digit evaluation and MAIN29 high-index audit

I obtain one new sixth-precision contraction:


$$
\boxed{KRK^T\equiv0\pmod{27}.}
$$


I also supply the missing factorial-unit argument underlying MAIN29’s high-index separation. With the bounded reconstruction and whole-force bounds retained as inputs, that audit supports the corrected multiplier and first-digit zero alignment.

**I do not complete the main assignment:** the actual nonedge $F,J$ entries and their LOW-unit projections have not been evaluated at the new precision. Thus I do not claim $A_9/9=0$, $A_{27}/3=0$, or an evaluated sixth endpoint image.

## 1. Weighted domain and precision retained

Throughout the weighted calculation,


$$
j>0,\quad243\mid j,\quad n=4^j+1,\quad
H=3^{h-1},\quad A=n-2=H-D,\quad0<D<H/8748.
$$


Use the actual monomial columns $1,y,\ldots,y^m$, where


$$
m=\frac{A+1}{2},\qquad d=\frac{3D}{2}-1,\qquad
\nu=\frac D2-1.
$$


HIGH is the finite interval $d\le a\le m$; the radical lifts are


$$
z_i=y^i(y-1)^D,\qquad0\le i<\nu.
$$



The actual core remains


$$
Q^{\rm loc}=(y+1)(y-1)^A(\beta+3y)+3^7R_0,
\qquad \beta=-71-A,
$$


and only the primitive unit $\lambda=L_n/3$ is stripped. The factorial force, endpoint-subtracted quotient, and every pole under the original cutoff remain part of the complete matrix.

I reuse, without reproving, A4turn21’s direct annihilation and identity


$$
T_6\equiv-\left(A_9/9+A_{27}/3+A_{81}\right)\pmod3.
$$


A4’s separate assignment concerns $A_{81}$.

## 2. New coefficient-band calculation for the actual HIGH inverse

The inverse used here is exactly


$$
R_{ab}=[z^{d+m-a-b}](1-z)^{-A},
\qquad d\le a,b\le m.
$$



### 2.1 Power-compression lemma

For $H=3^s$ and $1\le k\le s+1$,


$$
(1-z)^H\equiv
(1-z^{H/3^{k-1}})^{3^{k-1}}\pmod{3^k}.
\tag{1}
$$



To prove this, start with $f(z)^3\equiv f(z^3)\pmod3$. If $X\equiv Y\pmod{3^a}$, then


$$
X^3-Y^3=3Y^2(X-Y)+3Y(X-Y)^2+(X-Y)^3
$$


is divisible by $3^{a+1}$. Iterating gives (1). Both sides have constant term one, so inversion preserves the congruence in $\mathbb Z_3[[z]]$.

Consequently, modulo $27$, put $G=H/9$. Then


$$
(1-z)^{-A}
\equiv(1-z)^D(1-z^G)^{-9}\pmod{27}.
$$


For coefficients of degree below $H$, this is the explicit band expansion


$$
\boxed{
(1-z)^{-A}\equiv
(1-z)^D
\left(
1+9z^G+18z^{2G}+3z^{3G}
+9z^{4G}+18z^{5G}
+6z^{6G}+9z^{7G}+18z^{8G}
\right)
\pmod{27,\ z^H}.
}
\tag{2}
$$


Indeed, the band coefficients are $\binom{8+k}{8}\pmod{27}$, for $0\le k\le8$.

Thus the complete coefficient formula at this precision is


$$
[z^t](1-z)^{-A}
\equiv
\sum_{k=0}^{8}c_k(-1)^{t-kG}
\binom D{t-kG}\pmod{27},
\tag{3}
$$


with the invalid-binomial convention and


$$
(c_0,\ldots,c_8)=(1,9,18,3,9,18,6,9,18).
$$


This keeps all bands, including their higher digits; it is not merely a support statement modulo $3$.

### 2.2 Evaluation of $KRK^T\bmod27$

For the actual $K$ in the supplied contraction, its $(i,l)$ entry selects the coefficient degree


$$
t=D+\frac{H+3}{6}+i+l,\qquad0\le i,l<\nu.
$$


Since $i+l\le D-4$,


$$
G+D<t<2G.
$$


For the upper inequality, it is enough that


$$
2D-\frac72<\frac H{18},
$$


which follows from $D<H/8748$.

Every band in (2) lies in an interval $[kG,kG+D]$. The displayed $t$ lies strictly between the first and second interior bands. Hence


$$
\boxed{KRK^T=0\pmod{27}.}
\tag{4}
$$



This uses the supplied finite-HIGH coefficient-selection identity. It does not replace a truncated HIGH convolution by an unrestricted one.

### 2.3 What remains in $A_9$

A4turn21 gives $Je_d\in81\mathbb Z_3^\nu$. Therefore, using (4),


$$
\boxed{
A_9\equiv
2\operatorname{Sym}(e,KRFe_d)
+4(FRF)_{dd}ee^T\pmod{27}.
}
\tag{5}
$$


The fifth calculation evaluates those two terms only modulo $9$. Their next digits remain unevaluated here.

In particular, (2) alone cannot settle (5): the nonedge coefficients of $Fe_d\bmod27$, including its actual LOW projection, are still required. Nor does it evaluate the $F,J$ convolutions in $A_{27}\bmod9$. No conclusion about the sixth endpoint image follows.

## 3. MAIN29: repair of the higher-index factorial-unit justification

The audit domain remains


$$
p=29,\quad b=3^a,\quad n=2001b,\quad
a\ge1,\quad a\equiv432827\pmod{682892}.
$$


Coordinates are $0\le j\le b$; contact inverses have indices $0\le i,j<b$.

Both MAIN29 and the binary family use the **falling** metric


$$
\omega_j=j!\binom{n+2}{j}=(n+2)_{\underline j},
\qquad \Omega=\operatorname{diag}(\omega_j^2).
$$


The weighted reconstructed coordinates use $W_j=\binom{n+2}{j}$. No rising metric is substituted.

### 3.1 Exact factorial stripping

Define


$$
U_p(t)=\prod_{\substack{1\le r\le t\\p\nmid r}}r.
$$


Exactly,


$$
t!=p^{\lfloor t/p\rfloor}\lfloor t/p\rfloor!\,U_p(t),
\qquad
U_p(t)\equiv(-1)^{\lfloor t/p\rfloor}(t\bmod p)!\pmod p.
\tag{6}
$$



Apply (6) four times to a product of binomial coefficients. If $c$ is the total number of carries in its first four digit positions, then, after division by $p^c$, its residue equals

* a ratio of factorials of the four low digits;
* the sign $(-1)^c$;
* the **remaining high factorial ratio**.

There is no additional unidentified higher-index unit. To see the sign assertion, at stripping level $r$, the difference between the sums of the numerator and denominator quotients is exactly the carry across that level. Summing over the four levels gives $c$.

If an explicit coefficient supplies $p^v$, the same statement applies after division by $p^{c+v}$. Terms with $c+v>3$ vanish at the normalized $Q$-precision. Terms with $c+v=3$ require only the low unit modulo $p$.

This proves the factorial-unit separation needed in Lemma 2, rather than assuming that factorial units themselves depend only on low digits.

### 3.2 Why $e+u=1$

Use the source notation


$$
L=29^4,\quad j=LJ+x,\quad v=687936-x,\quad
e=\mathbf1_{x>191112},
$$




$$
u=\left\lfloor\frac{382219+v}{L}\right\rfloor.
$$


Restrict to the old $P$-support $\mathcal X$, where the base binomial product has exactly two low carries.

If $e=0$, then $x\le191112$, so $u=1$.

If $e=u=1$, both binomials have a carry at digit position $3$. The compulsory carry across the pair at position $1$ would give at least three low carries, contradicting $x\in\mathcal X$.

Thus


$$
e+u=1.
\tag{7}
$$


The change from $382220+v$ to $382219+v$ can cross a block boundary only when $v=L-382220$, whose units digit is zero. On $\mathcal X$, however, $x_0\le2$, so $v_0\in\{25,26,27\}$. That exception is excluded.

For $-31\le q\le0$,


$$
0\le v-q<L.
$$


Therefore the lower high index remains $h-J$, including at $J=h$. The remaining high factorial ratio is exactly


$$
\frac{N!}{J!(N-J-e)!}
\frac{(2N+h-J+u)!}{(h-J)!(2N)!}
=
F(J)(N-J)^e(2N+h-J+1)^u.
\tag{8}
$$


Equations (6)–(8) justify Lemma 2’s common high factor for every higher index, not merely for the enumerated low cases.

## 4. MAIN29: contact, last block, and endpoint audit

The following conclusions retain the supplied bounded reconstruction and whole logarithmic-force bound as inputs.

* **Contact on old support.** The first contact polynomial has degree-$28$ representation
  

$$
a(X)=9\left(\binom{b-X+28}{28}+\binom{b-X+29}{28}\right)\pmod{29}.
$$


  On old $P$-support, $j_0\le2$, so $a(j)=j\,a(j-1)=0\pmod{29}$. Its reconstructed coefficients supply the extra factor needed after multiplication by the external $29$. This validates its disappearance from $M_0$, rather than merely its raw polynomial residue.

* **Boundary coefficients $c_0,c_1$.** Replacing them by their unit residues introduces coefficients divisible by $29$. Their reconstructed monomials are the $q=0,-1,-2$ terms with the appropriate $j$-factor, already divisible by $29^3$. These replacements are therefore legitimate modulo $29^4$.

* **Last factorial block.** For $31\le d\le59$, coefficient valuation at least three combines with the negative-power reconstruction’s compulsory digit-$3$ carry. Thus this entire block vanishes modulo $29^4$ after reconstruction. It is not deleted from the original force.

* **Endpoint.** The absorbed Laurent boundary retains the endpoint $+W_b$. At $j=b$, the weight has three low borrows, hence $\widehat P_b=0\pmod{29}$. Its contribution to $D_0,M_0$ is zero for this reason, not because the endpoint is absent.

Accordingly, the high-index step in A2turn18 **passes with the explicit factorial-stripping repair above**. Combined with its bounded-kernel identities and the coordinator’s fixed low-constant evaluations, this supports


$$
K_{01}=0,\qquad D_0=C_n^2f(d)T(N_1,H),\qquad
D_0=0\Longrightarrow M_0=0.
$$


This audit does not independently reconstruct the contact inverse from definitions absent from the supplied earlier turns; it retains the stated complete bounded-kernel interface. Nor does first-digit alignment establish an all-depth valuation bound.

## 5. Primitive arithmetic and nonvanishing scope

For the weighted determinant family retain


$$
g=\gcd(|A_{\rm det}|,|B_{\rm det}|).
$$


When $B_{\rm det}\ne0$,


$$
q=\frac{|B_{\rm det}|}{g},\qquad
p=-\frac{\operatorname{sgn}(B_{\rm det})A_{\rm det}}g,
$$


and


$$
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_{\rm det})\ell^k}{g}
\det H_{\rm complete},
\qquad k=(n+1)/2.
$$


The primitive multiplier is $\ell^k/g$. The new calculation gives neither response nonvanishing nor whole-error nonvanishing.

For MAIN29 retain


$$
N_B=d_B[u,v],\quad
A_B=N_{B,1}^T\Omega N_{B,1},\quad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad q_B=A_B/g_B,\qquad p_B=H_B/g_B.
$$


The primitive multiplier on the rational pair is $d_B^2/g_B$, and the whole error is exactly


$$
q_B(e+\pi)-p_B=-q_B\epsilon_n.
$$


Its stated eventual sign and nonvanishing retain the complete signed-error theorem as an input. No local carry argument proves the necessary global denominator rate.

## Closing ledger

1. **New result and proof status.** Proved: the explicit inverse coefficient bands modulo $27$, $KRK^T=0\pmod{27}$, and the factorial-stripping justification of MAIN29’s high-index factorization. The MAIN29 first-digit audit passes within its stated complete bounded-kernel and whole-force interfaces.

2. **Exact remaining bottleneck.** Evaluate $KRFe_d$ and $(FRF)_{dd}$ modulo $27$, and every remaining $A_{27}$ contraction modulo $9$, using actual nonedge $F,J$ coefficients and LOW-unit projections. These have not been evaluated here. Subsequently, actual final-denominator control and nonzero whole primitive errors tending to zero remain necessary for irrationality.

3. **Computation request.** None. Repeating the completed low-digit enumeration would not resolve the missing weighted coefficient/projection calculation or the global denominator problem.
