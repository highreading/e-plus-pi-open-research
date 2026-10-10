> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the Laguerre bridge, orthogonal compression, and contact-minor divisor

## 1. Executive conclusions

The two bridges survive independent symbolic checking, but they concern **different determinants**.

1. **A2’s coefficient theorem is proved.** For the exact rational matrix
   

$$
H_{rj}(X)=X-A_{n+r,j}-B_j,\qquad 0\le r,j<b,
$$


   the Laguerre reduction, confluent normalization, and reciprocal-moment argument prove
   

$$
[X]\det H(X)>0
$$


   at every original admissible index
   

$$
b=3^{249005515+574312172u},\qquad n=2001b,\qquad
   u\equiv2\pmod{29^9}.
$$


   Here and below, $u$ remains in its original allowed domain; no extension of that domain is assumed. Consequently its paid coefficient $U_n$ is strictly positive.

2. **A2’s whole-error nonvanishing remains open.** The proof of coefficient positivity does not prove a sign for the complete mixed error. The auxiliary $n=3,b=3$ example identifies a failure of a positive-integrand argument, not a failure of the original coefficient theorem.

3. **A5’s real orthogonal compression and bound are valid.** They estimate the existing integer affine polynomial without redefining its arithmetic coefficients. The negative point mass and the full compact weight are retained. The stated improvement
   

$$
\log(F_k^\perp/F_k)=-c_*k^2+O(k\log k)
$$


   has the correct constant.

4. **The parent’s all-prime divisor is valid:**
   

$$
D_{k-1}\mid\delta_{k,2k-1},\qquad
   D_{k-1}\mid H_{0,k},H_{1,k}.
$$


   It is a divisor, not an exact Smith or final-gcd formula.

5. **A new arithmetic consequence closes one part of A2’s scalar ledger.** On every original A2 index, the actual combined arctangent charge is an integer:
   

$$
\boxed{\ell=1.}
$$


   In fact, writing
   

$$
M_d=\operatorname{lcm}(1,3,\ldots,4d-1),\qquad d=b-1,\quad h=n-d,
$$


   one has
   

$$
h!\mid \gamma_j,\qquad h!\mid F,\qquad
   \frac{4h!}{M_d}\mid\mathcal B.
$$


   The last expression is an integer at the original indices. Thus the exact primitive denominator there simplifies to
   

$$
\boxed{
   q_n=\frac{|F|}{\gcd(|F|,|E+\mathcal B|)}.
   }
$$


   This is an arithmetic improvement, not a proof of small nonzero error.

No unconditional rationality or irrationality theorem for $e+\pi$ follows.

---

## 2. Scope and boundaries of the audit

For A2 set


$$
d=b-1,\qquad h=n-d=2000b+1,\qquad \alpha=d+1=b.
$$


At the original indices, $b,n,h$ are odd and $d$ is even. All finite row operations below use only


$$
n,n+1,\ldots,n+d,
$$


and columns $0,\ldots,d$.

The exact entries being audited are


$$
A_{m,j}
=j!\sum_{s=0}^{m-j}(-1)^s\binom{m-j}{s}\frac1{(j+s)!},
\qquad
B_j=4\sum_{s=0}^{2j-1}\frac{(-1)^s}{2s+1}.
$$


The empty sum defining $B_0$ is zero.

The earlier A2 producer, with separate corrected forcing, returns, and physical terminal, is not completely specified in these sources. Thus this report proves statements about the displayed turn-11 matrix, not an undocumented identification with that producer. In particular, $\Lambda_m$ in the quoted exponential endpoint identity is not defined in the supplied file. The rational matrix audit does not depend on filling in that missing definition: its whole-error identity is derived directly below from the polynomial charges.

For A5 the compact matrix has exactly


$$
0\le m<2k,\qquad 0\le j<k,\qquad k\ge2.
$$


Its original binary producer remains distinct. The supplied boundary and correction data are retained:


$$
b=9^{18+32u},\quad n=4002b,\quad u\ge0,\qquad z_b=0,
$$




$$
x=\frac12RA^{-1}f,\qquad
y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},\qquad x=2^ax_0.
$$


The return sum remains


$$
S=\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f,
$$


and its quoted paid consequence remains


$$
v_2(S/2^{a+1})\ge\chi-a,\qquad
\chi=v_2\binom{n+b-1}{b-1}.
$$


Neither the subtraction of $a$, the source $h^F$, nor $e_0$ can be removed. The compact proof evaluates none of that producer’s actual contents, simultaneous clearer, norm $x_0^Tx_0$, or final all-prime gcd.

---

## 3. A2: finite reduction and normalization

### 3.1 Laguerre identities and degree ranges

With


$$
L_m^{(\beta)}(x)
=\sum_{s=0}^m(-1)^s\binom{m+\beta}{m-s}\frac{x^s}{s!},
$$


coefficient comparison gives


$$
A_{m,j}=\frac{L_{m-j}^{(j)}(1)}{\binom mj},
\quad
(L_m^{(\beta)})'=-L_{m-1}^{(\beta+1)},
\quad
L_m^{(\beta+1)}=(1-\partial_x)L_m^{(\beta)}.
$$



The first forward difference, followed by induction, gives


$$
\Delta_m^r A_{n,j}
=(-1)^r\frac{j!(n-j)!}{(n+r)!}L_{n-j}^{(j+r)}(1).
$$


All indices satisfy $n-j\ge h>0$ on the original domain.

Define


$$
f_j=L_{n-j}^{(j)},\qquad g_j=L_{n-j}^{(j+1)}.
$$


Then $g_j=(1-\partial_x)f_j$. Repeated use of


$$
L_m^{(\beta)}=L_m^{(\beta+1)}-L_{m-1}^{(\beta+1)}
$$


gives


$$
g_j=\sum_{a=0}^{d-j}(-1)^a\binom{d-j}{a}
L_{n-j-a}^{(\alpha)}.
$$


The smallest degree is exactly $n-d=h$, and the largest is $n$. In descending degree order, the transition matrix has diagonal $1$. Therefore


$$
\operatorname{span}(g_0,\ldots,g_d)
=\operatorname{span}(L_h^{(\alpha)},\ldots,L_n^{(\alpha)}).
$$



### 3.2 Row-operation signs

Replacing row $r$ by its $r$-th forward difference has determinant $1$. For $r\ge1$, both $X$ and the entire column-constant source $B_j$ disappear. The first row retains both.

The row scaling signs contribute exponent


$$
\sum_{r=1}^d(r+1)=\frac{d(d+3)}2.
$$


Replacing $(1-\partial)^s g$, $0\le s<d$, by $g^{(s)}$ contributes exponent


$$
\sum_{s=0}^{d-1}s=\frac{d(d-1)}2.
$$


Their sum is $d(d+1)$, which is even. Thus there is no residual sign:


$$
K_n\det H(X)=
\det\begin{pmatrix}
\binom nj(X-B_j)-f_j(1)\\
g_j(1)\\
g'_j(1)\\
\vdots\\
g_j^{(d-1)}(1)
\end{pmatrix}_{j=0}^d,
$$


where


$$
K_n=
\frac{\prod_{r=0}^d(n+r)!}
{\prod_{j=0}^d j!(n-j)!}.
$$


It is positive and integral: each factor


$$
\frac{(n+r)!}{r!(n-r)!}
=\binom{n+r}{2r}\frac{(2r)!}{r!}
$$


is an integer.

**Decision:** A2’s finite reduction and complete factorial normalization are accepted.

---

## 4. A2: positive-moment bridge and strict coefficient sign

### 4.1 Orthogonality and contact

For $x^\alpha e^{-x}\,dx$ on $(0,\infty)$, Rodrigues’ formula and integration by parts give the usual Laguerre orthogonality. The monic normalization


$$
\widehat L_m^{(\alpha)}=(-1)^m m!L_m^{(\alpha)}
$$


has norm


$$
\int_0^\infty(\widehat L_m^{(\alpha)})^2x^\alpha e^{-x}\,dx
=m!(m+\alpha)!.
$$


The boundary terms vanish because $\alpha\ge0$; all relevant polynomial moments are finite.

Let $z_j$ be the first-row signed cofactors of the reduced determinant and put $Q=\sum z_jg_j$. Then


$$
Q^{(s)}(1)=0\quad(0\le s<d),
$$


and $Q$ is orthogonal to every polynomial of degree below $h$ for the original Laguerre weight.

Because $d$ is even,


$$
w_d(x)=x^\alpha(x-1)^de^{-x}
$$


is a positive measure except at isolated zeros, with infinite support and all moments. If $p_h$ denotes its monic orthogonal polynomial, uniqueness gives


$$
Q=\tau_n(x-1)^dp_h,
$$


once the nonzero leading cofactor is established.

### 4.2 Cofactor and confluent signs

The cofactor $z_0$ is the Wronskian of $g_1,\ldots,g_d$. The triangular contiguous transition has determinant $1$.

Reversing the descending degree list contributes


$$
(-1)^{d(d-1)/2}.
$$


Passing to monic Laguerre polynomials contributes


$$
(-1)^{\sum_{N=h}^{n-1}N}.
$$


Their combined exponent is $dh+d(d-1)$, even when $d$ is even.

The confluent Christoffel identity gives


$$
W(\widehat L_h^{(\alpha)},\ldots,
\widehat L_{h+d-1}^{(\alpha)})(1)
=
\left(\prod_{s=0}^{d-1}s!\right)
\frac{\Delta_h}{\Delta_h^{(0)}},
$$


where


$$
\Delta_h^{(0)}=\prod_{i=0}^{h-1}i!(i+\alpha)!.
$$


The derivative factorials come from confluence of the evaluation Vandermonde. The modified weight initially appears as $(1-x)^d$ times the original weight; even $d$ makes it exactly $w_d$.

Consequently


$$
z_0=
\frac{\prod_{s=0}^{d-1}s!}{\prod_{N=h}^{n-1}N!}
\frac{\Delta_h}{\Delta_h^{(0)}}>0,
\qquad
\tau_n=\frac{(-1)^nz_0}{n!}.
$$


This also supplies the nonzero cofactor needed in the preceding uniqueness argument.

### 4.3 Reciprocal divided differences and integrability

Polynomial inversion of $1-\partial$ gives


$$
f_j(y)=\int_0^\infty e^{-u}g_j(y+u)\,du.
$$


Thus


$$
f_j(0)=\binom nj,\qquad
f_j(1)=e\int_1^\infty e^{-x}g_j(x)\,dx.
$$


The affine coefficient is therefore


$$
[X]\det H(X)=\frac{\tau_n}{K_n}J,
\qquad
J=\int_0^\infty e^{-x}(x-1)^dp_h(x)\,dx.
$$



The zeros of $p_h$ are distinct and in $(0,\infty)$, by positivity and infinite support of $w_d$. Interpolate $x^{-\alpha}$ at these zeros by $I$, with $\deg I<h$. Then


$$
J=\int p_h^2w_d\,f[r_1,\ldots,r_h,x]\,dx,
\qquad f(x)=x^{-\alpha}.
$$


Since


$$
f^{(h)}(x)=(-1)^h(\alpha)_h x^{-\alpha-h},
$$


the divided difference has strict sign $(-1)^h$.

Integrability is not merely formal. Near zero, $p_h(0)\ne0$, and the divided difference is $O(x^{-\alpha})$; $x^\alpha$ in $w_d$ cancels that singularity. At infinity, the interpolation identity reduces the integrand to a polynomially bounded factor times $e^{-x}$. At interpolation nodes the divided difference is continuous by confluence.

It follows that


$$
(-1)^hJ>0.
$$


Finally,


$$
\operatorname{sgn}(\tau_nJ)=(-1)^{n+h}=(-1)^d=1.
$$



**Infinite-domain decision:**


$$
\boxed{U_n>0\text{ at every original admissible A2 index}.}
$$


This conclusion is symbolic, not an extrapolation from the five finite receipts.

---

## 5. A2: moment determinant, integer recurrence, and actual reduction

### 5.1 Checking $Z$ without an unevaluated sign assertion

Put


$$
\nu_\ell=\sum_{a=0}^d(-1)^{d-a}\binom da(\ell+a)!,
\quad a_0=0,\quad a_i=d+i\ (1\le i\le h),
$$


and


$$
Z=\det[\nu_{a_i+j}]_{i,j=0}^h.
$$



A short independent derivation of its scalar relation is useful. In this determinant replace the last monomial column $x^h$ by $p_h(x)$; monicity preserves the determinant. Its entries in rows $1,\ldots,h$ vanish because those rows integrate $x^{i-1}p_h$ against $w_d$. The entry in row zero is $J$. Expansion down this column yields


$$
Z=(-1)^hJ\Delta_h>0.
$$


The entries are integers, so $Z\in\mathbb Z_{>0}$. This also verifies the sign of the stated Schur–Andréief representation: the ascending exponent list corresponds to the partition $(d^h)$.

Substitution gives exactly


$$
[X]\det H(X)=\mathfrak c_{n,d}Z,
$$


with


$$
\mathfrak c_{n,d}=
\frac{\left(\prod_{s=0}^{d-1}s!\right)
      \left(\prod_{j=0}^dj!\right)}
{\left(\prod_{i=0}^{h-1}i!(i+d+1)!\right)
 \left(\prod_{r=0}^d(n+r)!\right)}.
$$



### 5.2 Integer charges

The moments used for constructing $p_h$ are


$$
\mu_\ell=\sum_{a=0}^d(-1)^{d-a}\binom da
(\ell+d+1+a)!.
$$


The three-term orthogonal recurrence has positive norm denominators. Moments through $\mu_{2h-1}$ suffice, and their largest factorial is $(2n)!$.

Let $a$ be the least coefficient clearer of monic $p_h$, and set


$$
r=a(x-1)^dp_h=\sum_{\ell=0}^nr_\ell x^\ell.
$$


The polynomial $ap_h$ is primitive: a common divisor of all its coefficients would divide its leading coefficient $a$ and contradict minimality of the clearer. Gauss’s lemma then proves that $r$ is primitive.

The charges


$$
F=\sum r_\ell\ell!,
\qquad
E=\sum r_\ell\sum_{s=0}^{\ell}\frac{\ell!}{s!}
$$


are integers and satisfy


$$
F=aJ,\qquad E=e\int_1^\infty e^{-x}r(x)\,dx.
$$


In particular $F<0$ on the original domain.

For $r=\sum_{j=0}^d\gamma_jg_j$, the coefficient of $x^{n-j}$ in $g_i$, $i\le j$, is


$$
\frac{(-1)^{n-j}}{(n-j)!}\binom{n+1}{j-i}.
$$


Hence


$$
\gamma_j=(-1)^{n-j}(n-j)!r_{n-j}
-\sum_{i<j}\binom{n+1}{j-i}\gamma_i.
$$


This proves the asserted integer recurrence with its exact sign and factorial.

Define


$$
w_j=\binom nj\gamma_j,\qquad
\mathcal B=\sum_jw_jB_j=\frac T\ell
$$


in lowest terms. Then $\sum_jw_j=F$, and


$$
\det H(X)=\frac{\tau_n}{aK_n}(FX-E-\mathcal B).
$$



### 5.3 Paid matrix and final gcd

The retained payment is


$$
R_{rj}=A_{n+r,j}+B_j,\quad W_{rj}=(n+r)!R_{rj},
$$




$$
\kappa_r=\gcd((n+r)!,W_{r0},\ldots,W_{rd}),\quad
C_r=(n+r)!/\kappa_r,
$$




$$
Y_{rj}=C_rR_{rj},\quad
c_j=\gcd_{0\le r\le d}(C_r,Y_{rj}),
$$




$$
\mathcal L_n=\operatorname{lcm}_rC_r,\qquad
P_n=\frac{\prod_rC_r}{\prod_jc_j}.
$$


At original indices the displayed factorial clears all entry denominators, including those of $B_j$. Thus


$$
D_n(X)=\det[(C_rX-Y_{rj})/c_j]
=P_n\det H(X)=U_nX-V_n
$$


is integral.

No replacement of these actual contents or of $\mathcal L_n$ is made. Since $\gcd(\ell,T)=1$,


$$
g=\gcd(|F|,|\ell E+T|)
=\gcd(|\ell F|,|\ell E+T|).
$$


Therefore


$$
q_n=\frac{\ell|F|}{g},\qquad
p_n=\frac{\operatorname{sgn}(F)(\ell E+T)}g,
$$


and the exact all-prime paid coefficient gcd is


$$
G_n=U_n\frac{g}{\ell|F|}.
$$


These are exact reductions, not gcd estimates.

---

## 6. New result: the actual arctangent denominator is $1$ on the original A2 domain

### Proposition

For any instance of the preceding construction with $n\ge d$,


$$
h!\mid\gamma_j\quad(0\le j\le d),\qquad h=n-d.
$$


If $M_d\mid h!$, then


$$
\mathcal B\in\frac{4h!}{M_d}\mathbb Z.
$$


In particular, at every original A2 index,


$$
\boxed{\ell=1.}
$$



### Proof

In the triangular recurrence, every forcing term


$$
(-1)^{n-j}(n-j)!r_{n-j}
$$


is divisible by $h!$, since $n-j\ge h$. Induction on $j$ proves $h!\mid\gamma_j$, hence $h!\mid w_j$ and $h!\mid F$.

Every denominator in $B_j/4$ is odd and at most $4d-1$. Thus


$$
M_d B_j/4\in\mathbb Z.
$$


Writing $w_j=h!v_j$, with $v_j\in\mathbb Z$, gives


$$
\mathcal B=\frac{4h!}{M_d}
\sum_jv_j\left(\frac{M_dB_j}{4}\right).
$$



On the original domain,


$$
h=2000b+1>4b-5=4d-1.
$$


Every integer entering $M_d$ divides $h!$, so their least common multiple divides $h!$. Therefore $\mathcal B$ is integral. ∎

This proves an exact cancellation in the **combined** arctangent charge, without replacing its actual denominator by an oversized lcm. It yields


$$
g=\gcd(|F|,|E+\mathcal B|),\qquad
q_n=\frac{|F|}{g},
$$


and


$$
q_n(e+\pi)-p_n
=\frac{\operatorname{sgn}(F)}g
\bigl(F(e+\pi)-E-\mathcal B\bigr).
$$



It does **not** prove that $g$ is large: the simultaneous cancellation involving $E+\mathcal B$ remains unknown.

---

## 7. A2: whole mixed error and the remaining obstruction

With $W(y)=\sum_jw_jy^j$, direct integration gives


$$
F(e+\pi)-E-\mathcal B
=
e\int_0^1e^{-x}r(x)\,dx
+4\int_0^1\frac{W(s^4)}{1+s^2}\,ds.
$$


Both complete endpoint contributions are present.

The Laguerre dilation and contiguous identities give


$$
W(y)=\int_0^\infty e^{-x}r(x)L_n^{(0)}((1-y)x)\,dx.
$$


For $d+1\le k\le n$,


$$
\int e^{-x}x^kr(x)\,dx
=a\int x^{k-d-1}p_h(x)w_d(x)\,dx=0,
$$


because $0\le k-d-1<h$. Thus


$$
W(y)=\sum_{k=0}^d
\frac{(-1)^k}{k!}\binom nk(1-y)^k
\int_0^\infty e^{-x}x^kr(x)\,dx.
$$


The remaining integrals have sign $(-1)^h$, but their multipliers alternate. This is the precise obstruction to reusing the reciprocal-moment sign proof.

The parent’s finite $n=3,b=3$ receipt exhibits this obstruction:


$$
W(0)<0,\quad W(5/9)=1/3,\quad W(1)<0.
$$


It neither refutes coefficient positivity nor decides the whole error on any original index.

A concrete sufficient follow-on lemma, now simplified by $\ell=1$, is:


$$
0<
\left|
e\int_0^1e^{-x}r(x)\,dx+
4\int_0^1\frac{W(s^4)}{1+s^2}\,ds
\right|
\le \frac{g}{b}
$$


on one infinite subset of the original progression with $b\to\infty$. That would give nonzero primitive errors bounded by $1/b$. This lemma is open.

---

## 8. A5: exact compression and the complete signed estimate

Write


$$
L(f)=\int f\,d\mu-f(-1),\qquad
c_n=a_{2n}-(-1)^n,
$$


and


$$
r_n=-(2n)!+4\rho_n,\qquad
\rho_{n+1}+\rho_n=\frac1{2n+1}.
$$


These retain the negative mass and both rational endpoint corrections.

For the positive compact measure


$$
\int f\,d\nu=\int_0^1f(t^2)
\left(e^t+\frac4{1+t^2}\right)dt,
$$


integration by parts and the arctangent recurrence give


$$
\nu_n=e\,c_n+(e+\pi)(-1)^n+r_n.
$$


Consequently,


$$
H_k(e+\pi)=\Lambda_k^k\det[\Phi^T\mid N],
\qquad
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5).
$$


The maximal index $m+j=3k-2$ explains the last odd denominator $6k-5$.

Let $P_n$ be monic orthogonal polynomials for the full $\nu$. The row change from monomials to $P_n$ is real lower triangular with determinant $1$. It is used only in evaluating this determinant. It is **not** an integral or rational arithmetic normalization of $H_{0,k},H_{1,k}$.

The compact block becomes upper triangular in its top $k$ rows, with diagonal $h_n^\nu$, and zero in its bottom $k$ rows. Therefore


$$
H_k(e+\pi)=(-1)^{k^2}\Lambda_k^kJ_k^\nu\det T^{(k)},
$$


where


$$
T^{(k)}_{rj}
=\int z^jP_{k+r}(z)\,d\mu-(-1)^jP_{k+r}(-1).
$$


The block-exchange sign is exactly $(-1)^{k^2}$.

Positivity and full support on $(0,1)$ put all zeros of $P_n$ in that interval. Hence


$$
|P_n(z)|\le1\ (0\le z\le1),\quad
|P_n(z)|\le z^n\ (z\ge1),\quad
|P_n(-1)|\le2^n.
$$


Since $\mu$ has mass $1$, for $n=k+r$, $N=n+j$,


$$
|T_{rj}^{(k)}|\le1+a_{2N}+2^n\le3(2N)!.
$$


The alternating factorial formula gives $0<a_{2N}\le(2N)!$; $n\ge2$ supplies the remaining elementary bounds.

Factorial log-convexity makes the diagonal pairing maximal:


$$
\prod_r(2k+2r+2\sigma(r))!
\le\prod_r(2k+4r)!.
$$


Thus


$$
|\det T^{(k)}|\le3^kk!\prod_r(2k+4r)!.
$$



Finally the **full** compact density is bounded by $7$, so


$$
J_k^\nu\le7^kh_k,\qquad
h_k=\frac{2^{k(k-1)}(\prod_{j=1}^{k-1}j!)^2}
{\prod_{r,j=0}^{k-1}(2r+2j+1)}.
$$


This yields the accepted bound


$$
\boxed{
|H_k(e+\pi)|\le
\Lambda_k^k21^kk!h_k\prod_{r=0}^{k-1}(2k+4r)!.
}
$$



The three Stirling sums supplied in A5 give the coefficient


$$
4\log2+\frac92\log3-12\log2
-\frac12\log2-\frac34
=-c_*,
$$


where


$$
c_*=\frac{17}{2}\log2-\frac92\log3+\frac34>0.
$$


Thus the claimed $\exp(-c_*k^2+O(k\log k))$ improvement is correct. It improves an upper bound; it is not an asymptotic evaluation of the actual signed determinant.

---

## 9. Parent divisor and A5’s arithmetic ledger

For $d\eta(t)=e^{t-1}dt$, $t\le1$, the polynomials


$$
Q_r(t)=r!L_r^{(0)}(1-t)
$$


are monic and integral. Substitution $u=1-t$ gives norms $(r!)^2$. Their recurrence


$$
Q_{r+1}=(t+2r)Q_r-r^2Q_{r-1}
$$


also verifies integral coefficients directly.

Every even monomial has integer coordinates in this full frame. A finite cross-moment matrix therefore factors as


$$
R_I\operatorname{diag}((r!)^2)R_J^T.
$$


For each size-$s$ Cauchy–Binet term, the selected degrees satisfy $r_j\ge j$. Hence its product of norms is divisible by


$$
D_s=\prod_{j=0}^{s-1}(j!)^2.
$$


This proves divisibility of every cross-moment minor.

Subtracting the actual rank-one mass changes a size-$k$ determinant by a sum of size-$(k-1)$ cofactors with integer multipliers. Both parts are divisible by $D_{k-1}$. Laplace expansion in the contact columns then proves


$$
D_{k-1}\mid\delta_{k,2k-1},\qquad
D_{k-1}\mid H_{0,k},H_{1,k}.
$$



No claim about the Smith form of the restricted even frame is needed.

A5’s separate arithmetic ledger remains:


$$
L_X=
\frac{\Lambda_k}
{\gcd(\Lambda_k,\{\Lambda_kB_{rj}\})},
$$


and, if $L_X^k\det\mathcal M_X=A_0+A_1s$, its least coefficient clearer is


$$
\frac{L_X^k}{\gcd(L_X^k,A_0,A_1)}.
$$


Its residual integer content is


$$
\frac{\gcd(A_0,A_1)}{\gcd(L_X^k,A_0,A_1)}.
$$


For the block polynomial itself,


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|),\qquad
q_k=|H_{1,k}|/G_k
$$


when $H_{1,k}\ne0$, and its whole primitive error has magnitude


$$
|H_k(e+\pi)|/G_k.
$$



The divisor alone leaves an upper-bound logarithm


$$
\log(F_k^\perp/D_{k-1})=3k^2\log k+O(k^2).
$$


That proves insufficiency of these bounds, not divergence of the actual errors.

---

## 10. Acceptance ledger, finite checks, and final bottleneck

| Claim | Independent decision |
|---|---|
| A2 finite differences, degree block, factorial payment | Accepted |
| A2 cofactor/Wronskian and confluent signs | Accepted |
| A2 reciprocal divided-difference sign and integrability | Accepted |
| A2 $U_n>0$ on every original admissible index | Proved |
| A2 integer charge recurrence and exact primitive reduction | Accepted |
| A2 complete mixed-error identity | Accepted |
| A2 whole-error nonvanishing on an infinite original subset | Open |
| A2 actual arctangent denominator $\ell=1$ on original indices | **New proved result** |
| A5 real compression, determinant sign, full-weight root estimate | Accepted |
| A5 factorial rearrangement and exponential improvement | Accepted |
| Parent all-prime $D_{k-1}$ divisor | Accepted |
| Exact all-size final scalar gcd in either family | Open |
| Transfer between distinct compact/producer primitive pairs | Not justified |
| Rationality or irrationality of $e+\pi$ | Unresolved |

The five Laguerre receipts and the compact $k=3$ receipt remain finite premises. Their listed exact-arithmetic procedures use complete moments and endpoint corrections, and the interval construction includes explicit exponential and Machin-series remainder bounds. I have not executed them or independently recomputed their large integer outputs. No closed Family005 or Smith calculation needs repetition.

### Optional bounded check of the new divisibility statement

No computation is needed for its proof. A small transcription check not among the five closed Laguerre instances would use


$$
(n,b)=(19,5),\quad d=4,\quad h=15,\quad M_d=45045.
$$


Construct $p_{15}$ using moments through $\mu_{29}$, whose largest factorial is $38!$, and then construct $r,\gamma_j,F,E,\mathcal B$.

Expected exact verifiable output:


$$
15!\mid\gamma_j\quad(0\le j\le4),\qquad
15!\mid F,
$$




$$
\mathcal B\in\frac{4\cdot15!}{45045}\mathbb Z,\qquad
\operatorname{den}(\mathcal B)=1.
$$


This is only an auxiliary finite check, not an original-domain experiment or evidence for error decay.

### Final research status

The strongest new conclusion here is that A2’s arctangent denominator obligation simplifies **exactly**, on its entire original domain, to $\ell=1$. Together with the accepted positive-coefficient theorem, this leaves the explicit scalar problem


$$
g_n=\gcd(|F|,|E+\mathcal B|)
$$


and the complete signed error


$$
F(e+\pi)-E-\mathcal B.
$$



For A5, the exact remaining analytic object is the signed determinant $T^{(k)}$, including its negative point mass; its arithmetic counterpart is the actual final $G_k$, not merely $D_{k-1}$.

The unresolved global bottleneck is simultaneous proof, on the **same infinite original indices**, of nonzero whole errors and decay after all actual primitive reductions. Neither bridge supplies that missing result, and neither establishes rationality or irrationality of $e+\pi$.
