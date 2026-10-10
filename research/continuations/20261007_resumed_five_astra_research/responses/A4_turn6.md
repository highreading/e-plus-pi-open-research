> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent referee report: complete boundary cancellation and the universal rational-gauge obstruction

## Abstract and verdict

The two principal claims under review are valid at their stated scopes:

1. **Binary assembled-boundary theorem.** On the original domain
   

$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0,
$$


   and at a raw precision satisfying the stated bounded-precision hypothesis, the extended type-$2$ formulas represent the **whole completed polynomial vectors**, not merely their contact coordinates. Their assembled offset tails equal the complete physical terminal contributions modulo the paid raw modulus. Consequently, explicit tail subtraction and separate physical-terminal addition cancel in the assembled observations.

2. **Endpoint rational-gauge decision.** The supplied coefficient matrix represents the six stated cleared gauge identities with the correct coordinate ordering, denominator and degree bounds. Its left-null witness is valid. Combined with the universal denominator and infinity bounds, it excludes **every rational solution of the displayed six-component tensor gauge equation**. No seed equation is needed.

The at-most-$32$ merging argument, the common integral observation module, and the three derivative-image certificates also survive the audit. The derivative images are, however, **sufficient-only submodules of the acceptance kernel**. Neither full-kernel equality nor membership of the actual relative polynomial has been proved.

I give below a direct polynomial-vector proof of the boundary statement and a compact independent verification of the endpoint witness. The latter also yields a useful additional observation: the homogeneous rational gauge equation has no nonzero solution, so the reported rank $22$ follows without repeating Gaussian elimination.

None of these results proves rationality or irrationality of $e+\pi$.

---

## 1. Domains, retained objects, and scope of this review

Two distinct original domains are relevant here.

### 1.1 Binary producer

Throughout the binary discussion,


$$
\boxed{b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.}
$$


The contact matrix has indices $0\le i,j<b$, and physical reconstruction has rows $0\le j\le b$.

Write


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


The actual contact matrix and normalized force remain


$$
A_{ij}
=\sum_{s=0}^{n+i}
\lambda_s\binom{n+i}{s}\binom{2n+i-s}{j},
$$




$$
f_i^0=\frac{(n+i)!}{n!}
[t^n](1+2t+2t^2)^n(1+t)^i,
\qquad
\mathfrak f=f^0/R.
$$



Physical reconstruction is


$$
(\mathcal Rz)_j=W_j(jz_{j-1}-z_j),
\qquad z_{-1}=z_b=0.
$$


In particular, the corrected columns remain


$$
x=\frac12\mathcal RA^{-1}\mathfrak f,
\qquad
y=\frac{\mathcal RA^{-1}(h^e+h^F)+e_0}{4b!}.
$$


The logarithmic component $h^F$, the exterior $e_0$, and every physical row are retained.

Set


$$
z^f=A^{-1}\mathfrak f,\qquad
z^k=A^{-1}k,\qquad
k=\frac{h^e-A(j!)_{0\le j<b}}{b!}.
$$


With $\Delta_jz=jz_{j-1}-z_j$, the complete raw observations are


$$
\mathcal U
=\sum_{j=0}^{b-1}W_j^2(\Delta_jz^f)^2
+b^2W_b^2(z^f_{b-1})^2,
\tag{1.1}
$$


and


$$
\mathcal V
=\sum_{j=0}^{b-1}W_j^2(\Delta_jz^f)(\Delta_jz^k)
+W_b^2bz^f_{b-1}(bz^k_{b-1}+1).
\tag{1.2}
$$


Both summands in the last terminal factor are compulsory.

If $x=2^ax_0$, with $a$ the actual first-column binary content, then


$$
Q=2^{-2a-2}\mathcal U,\qquad
E=2^{-a-3}\mathcal V.
\tag{1.3}
$$



### 1.2 Endpoint producer

The endpoint construction retains its separate original domain


$$
\boxed{n=15^r\ \text{or}\ n=105^r,\qquad r\ge2.}
$$


Consecutive integers $n\ge2$ are auxiliary recurrence indices. The original integral normalization


$$
L_n=2^{(n+1)/2}
$$


is used at the original odd indices.

No conclusion is transferred between these domains. This review changes no previously stated ternary or $29$-adic obligation.

---

# Part I. The whole binary completion and boundary observation

## 2. Precision hypotheses and finite degree bounds

At raw precision $2^L$, $L\ge1$, retain


$$
I=\min(b-1,8L-2),\qquad m=4(L-1),
$$




$$
d_{\rm tail}=\min(m,b),\qquad
T=\min(2L-1,2n-1),\qquad V=T+m.
$$


The reused filtrations are


$$
\mathfrak f_i\equiv0\pmod{2^L}\quad(i>I),
\qquad
\lambda_s\equiv c_s\equiv0\pmod{2^L}\quad(s>m),
$$


where


$$
c_0=1,\qquad
c_s=-\sum_{r=1}^s\binom sr\lambda_rc_{s-r}.
$$


The complete source is reduced only to its paid prefix:


$$
k\equiv\sum_{t=0}^{T}a_t\mathbf a_{b+t}\pmod{2^L},
\qquad
a_t=\frac{(b+t)!}{b!}.
\tag{2.1}
$$



For the offset-kernel evaluator and its parameter bounds, impose


$$
\boxed{n>4D+2,\qquad D=I+2m+T+4.}
\tag{2.2}
$$


This remains a bounded-precision theorem, not a half-length precision theorem.

The full-vector argument below has a finite degree bound. The completed first-force input has degree at most $b+m-1$, and the completed source-difference input has degree at most $b+V$. Applying $\mathcal J$ can increase degree by at most $m$. Thus


$$
\deg\widehat z^f\le b+2m-1,\qquad
\deg\widehat z^k\le b+T+2m.
\tag{2.3}
$$


After reconstruction, degree at most


$$
b+T+2m+1
\tag{2.4}
$$


suffices for both channels. These are bounds on auxiliary polynomial vectors; they do not enlarge the contact system or the physical reconstruction.

---

## 3. Why the completion identities hold in every degree

Work with divided-power coefficient vectors:


$$
z^{[j]}=\frac{z^j}{j!}.
$$


Multiplication and differentiation have integral matrices in this basis. Define


$$
\mathcal U_\gamma=(1+\partial_z)^\gamma,
\qquad
\mathcal M=\mathcal U_n\mathcal H_\lambda\mathcal U_n,
\qquad
\mathcal J=\mathcal U_{-n}\mathcal H_c\mathcal U_{-n}.
$$


Negative binomial expansions are finite on each polynomial. The retained inverse-symbol identity gives, as whole polynomial operators modulo $2^L$,


$$
\mathcal J\mathcal M=\mathcal M\mathcal J=1.
\tag{3.1}
$$



The contact restriction of $P\mathcal M$, where $P$ is multiplication by $e^z$, is the actual matrix $A$. This is the established finite factorization, not a new contact equation.

### 3.1 First force: the entire contact prefix must be retained

Let $\overline z^f$ be $z^f$ padded by zero beyond $b-1$, and form


$$
q=\mathcal M\overline z^f.
$$


Its contact coordinates are


$$
q_j=(P^{-1}\mathfrak f_{\le I})_j
=\sum_{i=0}^{\min(I,j)}(-1)^{j-i}\binom ji\mathfrak f_i,
\qquad 0\le j<b.
\tag{3.2}
$$


Although $\mathfrak f_{\le I}$ is short, the transformed contact vector in (3.2) generally is **not** supported only through $I$. The full prefix $0\le j<b$ is necessary.

Let


$$
r=\mathcal U_n\overline z^f,\qquad w=\mathcal H_\lambda r.
$$


The vector $r$ is contact-supported. The exterior part of $w$ is


$$
w_{b:b+m-1}=K E_{\rm tail}^Tr.
$$


Using the retained finite solve,


$$
E_{\rm tail}^Tr=S^{-1}D_f.
$$


Therefore the exterior part of $q=\mathcal U_nw$ is exactly


$$
\eta_f=U_n^{(m)}KS^{-1}D_f.
$$


No higher coordinate occurs. Hence $q=q^f$, and (3.1) proves


$$
\boxed{\mathcal Jq^f\equiv\overline z^f\pmod{2^L}}
\tag{3.3}
$$


in every polynomial coefficient, including every coefficient above the contact range.

### 3.2 Complete source: the returned part cancels before applying $\mathcal J$

Put


$$
s=\sum_{t=0}^{T}a_te_{b+t}.
$$


The complete source relation is


$$
k\equiv \pi_bP\mathcal Ms\pmod{2^L},
$$


where $\pi_b$ means contact restriction.

The exterior coordinates of $\mathcal H_\lambda\mathcal U_ns$ split into two parts:


$$
K\rho_{\rm ret}+\xi.
$$


Here


$$
(\rho_{\rm ret})_h
=\sum_{t=0}^{T}a_t\binom n{t+d_{\rm tail}-h},
$$


and


$$
\xi_v=
\sum_{t=0}^{T}a_t
\sum_{\substack{0\le r\le t\\0\le v-r\le m}}
\binom n{t-r}\lambda_{v-r}\binom{b+v}{v-r}.
\tag{3.4}
$$


Formula (3.4) follows by separating the exterior input coordinates $b+r$ before multiplication by the symbol. It includes the entire paid factorial prefix.

For the zero-padded contact solution $\overline z^k$, the retained finite return identity is


$$
E_{\rm tail}^T\mathcal U_n\overline z^k
=\rho_{\rm ret}+S^{-1}G^{[V]}\xi.
\tag{3.5}
$$


Consequently, the exterior difference


$$
\mathcal M\overline z^k-\mathcal Ms
$$


is


$$
U_n^{(V+1)}\bigl(KS^{-1}G^{[V]}\xi-\xi\bigr)=\theta.
$$


Its contact part is zero, since the two contact source equations agree and the finite Pascal matrix is invertible.

Thus, with


$$
q^\theta=\sum_{v=0}^{V}\theta_ve_{b+v},
$$


we have the whole polynomial identity


$$
q^\theta=\mathcal M(\overline z^k-s)\pmod{2^L}.
$$


Applying $\mathcal J$ gives


$$
\boxed{\mathcal Jq^\theta\equiv\overline z^k-s\pmod{2^L}.}
\tag{3.6}
$$



This derivation explains exactly why deleting $\rho_{\rm ret}$, any part of the Schur return, or part of the prefix would invalidate the argument.

It also preserves the complete differential source


$$
\mathscr L_n
\left(\frac{\phi^ng_n-e^z\phi^nU_b}{b!}\right)
=e^z\phi^{n+1}(C_{b-1}+C_b).
$$


Neither differential boundary has been removed.

---

## 4. Audit of the extended binomial formulas

The normal-order formula is


$$
\mathcal J
=\sum_{s=0}^m c_s\sum_{r=0}^s
(-1)^r\binom{n+r-1}{r}
M_{z^{[s-r]}}\mathcal U_{-(2n+r)}.
\tag{4.1}
$$



### 4.1 Exterior profiles

Applying (4.1) to $e_{b+v}$ gives, for every $j\ge0$,


$$
\begin{aligned}
\Psi_{jv}
={}&(-1)^{b+v-j}\sum_{s=0}^m(-1)^sc_s
\sum_{r=0}^s\binom{n+r-1}{r}\binom j{s-r}\\
&\qquad\cdot
\binom{2n+b+v+s-1-j}{b+v+s-r-j}.
\end{aligned}
\tag{4.2}
$$



There is no hidden ambiguity about negative upper indices. If the lower index


$$
k=b+v+s-r-j
$$


is nonnegative, the upper index is


$$
2n+r+k-1\ge0.
$$


If $k<0$, the stipulated negative-lower-index convention makes the term zero. Thus (4.2) agrees with the polynomial action of $\mathcal J$, including above contact.

### 4.2 Head profiles

For $0\le\ell\le b-1$,


$$
\begin{aligned}
&\sum_{k=\max(\ell,i)}^{b-1}
\binom{\alpha+k-\ell-1}{k-\ell}\binom ki\\
&\quad=
\sum_{q=0}^{i}
\binom{\alpha+q-1}{q}\binom{\ell}{i-q}
\binom{\alpha+b-1-\ell}{b-1-\ell-q}.
\end{aligned}
\tag{4.3}
$$


Indeed, use


$$
\binom ki=\sum_q\binom\ell{i-q}\binom{k-\ell}{q},
$$


then


$$
\binom{\alpha+v-1}{v}\binom vq
=\binom{\alpha+q-1}{q}
\binom{\alpha+v-1}{v-q},
$$


and finite hockey-stick summation.

For $\ell>b-1$, the left side is empty and every lower endpoint index on the right is negative. Both sides are zero.

Taking $\ell=j-(s-r)$ in (4.3), and using


$$
\binom j{s-r}\binom{j-(s-r)}{i-q}
=\binom{s-r+i-q}{s-r}\binom j{s-r+i-q},
$$


gives the displayed head formula $B_{ji}$ for every $j\ge0$. If $j<s-r$, the relevant terms vanish because their lower binomial indices exceed $j$.

Again, whenever the final lower index


$$
k=b+s-r-q-1-j
$$


is nonnegative, its upper index is


$$
2n+r+q+k\ge0.
$$


Thus the same conventions agree with full $\mathcal J$-action, not just with contact coordinates.

### 4.3 Whole-vector conclusion

The extended profiles


$$
\widehat z^f_j=
\sum_{i=0}^{I}\mathfrak f_iB_{ji}
+\sum_{v=0}^{m-1}(\eta_f)_v\Psi_{jv},
\qquad
\widehat z^k_j=\sum_{v=0}^{V}\theta_v\Psi_{jv}
$$


therefore satisfy


$$
\boxed{
\widehat z^f\equiv\overline z^f,\qquad
\widehat z^k\equiv\overline z^k-s
\pmod{2^L}
}
\tag{4.4}
$$


as whole finite polynomial vectors.

This establishes the outstanding extension claim independently of the $25$-position receipt.

---

## 5. Complete assembled boundary cancellation

Define


$$
\widehat F_j=j\widehat z^f_{j-1}-\widehat z^f_j,\qquad
\widehat G_j=j\widehat z^k_{j-1}-\widehat z^k_j.
$$


The factorial relation


$$
a_t=(b+t)a_{t-1}
$$


gives the exact source reconstruction


$$
\Delta_js=
\begin{cases}
-1,&j=b,\\
0,&b<j\le b+T,\\
a_{T+1},&j=b+T+1,\\
0,&\text{otherwise}.
\end{cases}
\tag{5.1}
$$


The high source endpoint is retained.

From (4.4),


$$
\widehat F_j\equiv
\begin{cases}
\Delta_jz^f,&j<b,\\
bz^f_{b-1},&j=b,\\
0,&j>b,
\end{cases}
\tag{5.2}
$$


and


$$
\widehat G_j\equiv
\begin{cases}
\Delta_jz^k,&j<b,\\
bz^k_{b-1}+1,&j=b,\\
-a_{T+1},&j=b+T+1,\\
0,&\text{other }j>b.
\end{cases}
\tag{5.3}
$$


The high endpoint contributes zero to the mixed observation because $\widehat F_j\equiv0$ there—not because the source endpoint has been deleted.

### 5.1 Every offset tail is an exterior contribution

After reconstruction and the integral product formula


$$
\binom jd\binom je
=\sum_{r=\max(d,e)}^{d+e}
\frac{r!}{(r-d)!(r-e)!(d+e-r)!}\binom jr,
\tag{5.4}
$$


let $\gamma_\kappa^Q,\gamma_\kappa^E$ be the assembled kernel coefficients.

For an individual kernel, ordering $\varepsilon_1\le\varepsilon_2$, its tail is precisely its contribution at


$$
j=b,\ldots,b+\varepsilon_1
$$


when $\varepsilon_1\ge0$. If $\varepsilon_1<0$, there is no exterior contribution because the first large binomial has negative lower index for $j\ge b$.

Therefore, for fixed integral lifts of the residue coefficients, distributivity gives exact finite identities


$$
\sum_\kappa\gamma_\kappa^Q\mathcal T_{{\rm off},\kappa}
=\sum_{j\ge b}W_j^2\widehat F_j^2,
$$




$$
\sum_\kappa\gamma_\kappa^E\mathcal T_{{\rm off},\kappa}
=\sum_{j\ge b}W_j^2\widehat F_j\widehat G_j.
\tag{5.5}
$$


These sums are finite both by polynomial support and by $W_j=0$ for $j>n+2$.

Substitution of (5.2)–(5.3) proves


$$
\boxed{
\sum_\kappa\gamma_\kappa^Q\mathcal T_{{\rm off},\kappa}
\equiv b^2W_b^2(z^f_{b-1})^2\pmod{2^L},
}
\tag{5.6}
$$




$$
\boxed{
\sum_\kappa\gamma_\kappa^E\mathcal T_{{\rm off},\kappa}
\equiv W_b^2bz^f_{b-1}(bz^k_{b-1}+1)\pmod{2^L}.
}
\tag{5.7}
$$



Thus the complete raw observations are


$$
\boxed{
\mathcal U\equiv\sum_\kappa\gamma_\kappa^Q\operatorname{Acc}_L(\kappa),
\qquad
\mathcal V\equiv\sum_\kappa\gamma_\kappa^E\operatorname{Acc}_L(\kappa)
\pmod{2^L},
}
\tag{5.8}
$$


where acceptance is taken before explicit tail subtraction.

### Referee qualification

The phrase “tails cancel” must mean (5.6)–(5.8). Individual tails need not vanish. Nor is the corresponding polynomial state asserted to be zero.

The auxiliary value $\widehat z_b^k=-1$ is used in this proof only. The physical boundary remains


$$
z_b^k=0.
$$



The supplied $b=2,n=8004,L=3$ receipt is consistent with this theorem and has genuinely nonzero terminal observations. Its finite scope is unchanged; it is not used as the proof.

---

# Part II. Merging, the common module, and sufficient annihilators

## 6. Exact audit of the at-most-$32$ argument

Put


$$
J=2L-1,\qquad r_f=m+I+1,\qquad
\rho=T+2m+1,\qquad
\Delta_\varepsilon=\rho+I+1.
$$


The actual reconstructed atoms satisfy


$$
0\le d\le2r_f,\qquad
-I-1\le\varepsilon_i\le\rho,\qquad
-1\le a_i\le r_f-1.
\tag{6.1}
$$


In particular, $\delta\le\Delta_\varepsilon$. Together with (2.2), these inequalities validate the Euler-kernel hypotheses. For example,


$$
b+\varepsilon_1\ge b-I-1\ge0,
$$


and


$$
2n+a_1-\delta\ge2n-1-\Delta_\varepsilon>0.
$$



The five varying entries are


$$
N_1,\ N_3,\ N_4,\ M,\ B_{\rm tar};
$$


$N_2$ is common. Their initial spreads are bounded by


$$
2r_f,\quad r_f+\Delta_\varepsilon,\quad
r_f+\Delta_\varepsilon,\quad2r_f,\quad\Delta_\varepsilon.
$$


Each update contracts an integer interval of width $w$ to width at most $\lceil w/2\rceil$. Hence after


$$
t_0=
\left\lceil\log_2\max(2r_f,r_f+\Delta_\varepsilon)\right\rceil
$$


each varying entry has at most two values. There are at most $2^5=32$ tuples.

This alone does not bound merged support. The necessary additional argument is the absolute-coordinate estimate


$$
-J(1-2^{-s})+\frac d{2^s}
\le x\le
J(1-2^{-s})+\frac d{2^s},
$$


and its analogue for $y,\delta$. At $s=t_0$, every state lies in


$$
-J\le x,y\le J+1,\qquad 0\le\deg_tP\le3J.
$$


Thus a safe union bound per tuple is


$$
\boxed{(3J+1)(2J+2)^2.}
\tag{6.2}
$$



The source’s union/merge proof is therefore correct. It does not assume that coincident tuples have coincident support centers.

---

## 7. Common exponent module

At the merge stage define


$$
\bar N_i=\min_\tau N_{i,\tau},\qquad
\bar M=\max_\tau M_\tau,\qquad
\bar B=\max_\tau B_\tau.
$$


Then


$$
\bar P=
\sum_\tau t^{\bar B-B_\tau}P_\tau
\prod_i(1+v_i)^{N_{i,\tau}-\bar N_i}
(1-t)^{\bar M-M_\tau}
\tag{7.1}
$$


satisfies


$$
\sum_\tau\mathcal A(P_\tau;\mathbf N_\tau,M_\tau,B_\tau)
=\mathcal A(\bar P;\bar{\mathbf N},\bar M,\bar B).
\tag{7.2}
$$



The signs and directions of the denominator and target adjustments are correct. In particular,


$$
(1-t)^{\bar M-M_\tau}(1-t)^{-\bar M}
=(1-t)^{-M_\tau}.
$$


Every introduced exponent is $0$ or $1$, and no division occurs.

Because $N_2$ is already common, a safe common support box is


$$
0\le\deg_t\bar P\le3J+3,
$$




$$
-J\le x\le J+2,\qquad
-J-1\le y\le J+2.
$$


Its size is at most


$$
\boxed{(3J+4)(2J+3)(2J+4).}
\tag{7.3}
$$



Thus the actual pair has a common tuple with


$$
\mathcal U\equiv\mathcal A(\bar P_Q),\qquad
\mathcal V\equiv\mathcal A(\bar P_E)\pmod{2^L}.
$$



---

## 8. Audit of the three integral derivative images

Write


$$
\mathscr R=
\frac{(1+X)^{N_1}(1+t/X)^{N_2}
(1+tY)^{N_3}(1+1/Y)^{N_4}}{(1-t)^M}.
$$



For $D_X=X\partial_X$, direct differentiation gives


$$
\begin{aligned}
&D_X\!\left(H(1+X)(1+t/X)\mathscr R\right)\\
&=\mathscr R\Bigl((1+X)(1+t/X)D_XH\\
&\hspace{17mm}
+H\bigl((N_1+1)X(1+t/X)
-(N_2+1)(t/X)(1+X)\bigr)\Bigr).
\end{aligned}
$$


This is exactly $\mathscr D_X(H)\mathscr R$. Its $X$-constant term is zero.

The analogous calculation for $Y$ gives exactly


$$
\mathscr D_Y(H)\mathscr R
=D_Y\!\left(H(1+tY)(1+1/Y)\mathscr R\right).
$$



Finally, with


$$
F=(1+t/X)(1+tY)(1-t),
$$


the product rule yields


$$
\mathscr D_t(H)\mathscr R
=(D_t-B_{\rm tar})(HF\mathscr R).
$$


The coefficient $(M-1)t$ in the displayed $\mathscr D_t$ is correct: $Mt$ comes from differentiating the denominator and $-t$ from differentiating the factor $1-t$.

Therefore


$$
\boxed{
\mathcal A(\mathscr D_XH)=
\mathcal A(\mathscr D_YH)=
\mathcal A(\mathscr D_tH)=0
}
\tag{8.1}
$$


integrally and modulo every $2^L$.

No factorial division or nonunit pivot is involved.

### Exact limitation

What has been proved is only


$$
\operatorname{im}\mathscr D_X+
\operatorname{im}\mathscr D_Y+
\operatorname{im}\mathscr D_t
\subseteq\ker\mathcal A.
\tag{8.2}
$$


Equality is not established. In particular, characteristic-zero reduction modulo total derivatives does not by itself establish equality over $\mathbb Z/2^L\mathbb Z$, eliminate torsion, or prove actual-source membership.

---

## 9. The binary obligation that genuinely remains

The exterior observation is now closed. The unresolved local problem is the **actual interior relative acceptance**.

For $a\ge0$ and an integral candidate $r$,


$$
E-rQ
=2^{-2a-3}(2^a\mathcal V-2r\mathcal U).
$$


Hence a sufficient certificate at primitive depth $K$ is


$$
2^a\bar P_E-2r\bar P_Q
\equiv
\mathscr D_XH_X+\mathscr D_YH_Y+\mathscr D_tH_t
\pmod{2^{K+2a+3}}.
\tag{9.1}
$$


The entire construction must use that raw precision.

Without an independently established sign condition on $a$, use


$$
c=\max(2a+2,a+3)
$$


and the integral numerator


$$
2^{c-a-3}\bar P_E-r\,2^{c-2a-2}\bar P_Q
\tag{9.2}
$$


at modulus $2^{K+c}$, with $L\ge1$.

A concrete follow-on lemma is therefore:

> **Actual relative-membership lemma.** On an explicitly specified infinite subset of the original $u$-domain, certify the actual content $a$, construct $r(u)$, and give bounded-support $H_X,H_Y,H_t$ satisfying (9.1) or (9.2), using the actual normalized force, $\eta_f,\theta$, and original parameter word.

This is an explicit polynomial-identity target. Failure of a search in one support box would not disprove the relative congruence.

The new boundary theorem proves no nonzero infinite-original $E$-digit and no nontrivial relative law by itself.

---

# Part III. Independent validation of the endpoint certificate

## 10. The exact transfer and coefficient encoding

Use the tensor ordering


$$
\mathbf Y_n=
(P_n\tau_n,P_n\tau_{n+1},
Q_n\tau_n,Q_n\tau_{n+1},
F_n\tau_n,F_n\tau_{n+1})^T.
$$



Factoring the supplied coefficient table gives the following explicit transfer matrices:


$$
U_n=
\begin{pmatrix}
0&(n+1)(n+2)&(n+2)/2\\
n+2&-(n^2+3n+1)&-\dfrac{n(n+2)}{2(n+1)}\\
-(n+2)(2n+3)&(n+2)(n^2+3n+1)&
\dfrac{(n+2)(n^2-2)}{2(n+1)}
\end{pmatrix},
\tag{10.1}
$$




$$
R_n=
\begin{pmatrix}
0&1\\[1mm]
\dfrac{n+1}{n+2}&\dfrac{2n+3}{n+2}
\end{pmatrix},
\qquad K(n)=U_n\otimes R_n.
\tag{10.2}
$$


These make the transfer implicit in the excerpts explicit. Their identification with the actual endpoint recurrence uses the retained physical-source and endpoint-transfer theorem; it is not inferred merely from the matrix’s asymptotics.

The forcing row is


$$
\gamma(n)=
\left(
0,\frac{n+2}{2},
-\frac{(n+1)^2}{2},
\frac{(n+1)^2+1}{2},
-\frac{n+1}{4},
\frac{n^2+3n+3}{4(n+1)}
\right).
$$



The gauge equation is


$$
\ell(n+1)K(n)+(n+1)^2\ell(n)=\gamma(n).
\tag{10.3}
$$



Let


$$
D(n)=(n+1)^2(n+2),
$$




$$
C(n)=4(n+1)(n+2)D(n)D(n+1)
=4(n+1)^3(n+2)^4(n+3),
$$


and set


$$
\mu(n)=\frac{C(n)}{D(n+1)}
=4(n+1)^3(n+2)^2,
$$




$$
\nu(n)=\frac{C(n)(n+1)^2}{D(n)}
=4(n+1)^3(n+2)^3(n+3).
\tag{10.4}
$$



For an unknown coefficient $a_{ij}$ in $A_i(n)$, its contribution to cleared component $k$ is exactly


$$
\boxed{
\mu(n)(n+1)^jK_{ik}(n)+\nu(n)n^j\delta_{ik}.
}
\tag{10.5}
$$


Thus the coefficient in row $(k,d)$, column $(i,j)$, is the coefficient of $n^d$ in (10.5).

This formula verifies the label convention and the shift $A_i(n+1)$. For example,


$$
\nu(n)=96+464n+936n^2+1020n^3+648n^4+240n^5+48n^6+4n^7,
$$


which is the self-term appearing in the table. Also


$$
\mu(n)K_{3,0}(n)=\mu(n)(n+1),
$$


whose coefficients are


$$
16,80,164,176,104,32,4,
$$


again agreeing with the displayed table.

The six right-hand-side polynomials are


$$
\begin{aligned}
b_0(n)&=0,\\
b_1(n)&=2(n+1)^3(n+2)^5(n+3),\\
b_2(n)&=-2(n+1)^5(n+2)^4(n+3),\\
b_3(n)&=2(n+1)^3(n+2)^4(n+3)(n^2+2n+2),\\
b_4(n)&=-(n+1)^4(n+2)^4(n+3),\\
b_5(n)&=(n+1)^2(n+2)^4(n+3)(n^2+3n+3).
\end{aligned}
\tag{10.6}
$$


These are exactly $C\gamma_k$, including the sign of the forcing.

The actual maximum cleared degrees are


$$
10,10,10,10,9,9.
$$


Therefore the $64$ listed coefficient equations are complete:


$$
4\cdot11+2\cdot10=64.
$$


No degree-$11$ equation is missing; the degree-$11$ bound in Turn 5 was safe but not sharp.

---

## 11. Universal denominator and degree bounds

The retained pole-orbit theorem gives


$$
D(n)\ell(n)\in\mathbb Q[n]^6.
$$


Its orientation is correct: a leftmost pole is one step to the right of a pole of the forward transfer, while a rightmost pole is a pole of its inverse. The only possible poles are $-2,-1$, of orders at most $1,2$, respectively.

For the infinity bound, put


$$
S(n)=\operatorname{diag}(1,1,n),\qquad
\widetilde U(n)=S(n+1)^{-1}U_nS(n).
$$


From (10.1),


$$
n^{-2}\widetilde U(n)\longrightarrow
U_\infty=
\begin{pmatrix}
0&1&1/2\\
0&-1&-1/2\\
0&1&1/2
\end{pmatrix},
$$


and


$$
R_n\longrightarrow R_\infty=
\begin{pmatrix}0&1\\1&2\end{pmatrix}.
$$


The rank-one matrix $U_\infty$ has eigenvalues $0,0,-1/2$. Hence


$$
\det(I_6+U_\infty\otimes R_\infty)
=
\left(1-\frac{1+\sqrt2}{2}\right)
\left(1-\frac{1-\sqrt2}{2}\right)
=-\frac14.
\tag{11.1}
$$



For


$$
h(n)=\ell(n)(S(n)\otimes I_2),
$$


the transformed forcing has degree at infinity at most $2$. If $h$ had positive degree $d$, its leading coefficient would be annihilated by the invertible matrix in (11.1), a contradiction.

Thus every rational gauge has numerator degrees at most


$$
\boxed{3,3,3,3,2,2}
\tag{11.2}
$$


over $D$. The $22$-unknown system is universal for rational gauges of (10.3).

### Additional consequence: rank $22$ without elimination

For the homogeneous gauge equation, the same leading-coefficient argument works for **every integer degree at infinity**, including negative degrees. Its right side is zero, so any nonzero rational solution would again have a nonzero leading coefficient annihilated by (11.1).

Therefore the homogeneous rational gauge equation has only the zero solution. The map from the $22$ numerator coefficients to the cleared residual coefficients is injective. Hence


$$
\boxed{\operatorname{rank}A=22.}
\tag{11.3}
$$



---

## 12. Compact exact verification of the left-null witness

The witness uses only components $0,1,2,3$. Write its coefficient weights as follows, padding each list with zeros through degree $6$:


$$
\begin{aligned}
(w_{0d})&=\frac1{512}
(157761,-110238,69864,-38160,16240,-4128,0),\\
(w_{1d})&=\frac1{512}
(-103167,56212,-26056,9272,-1936,0,0),\\
(w_{2d})&=\frac1{32768}
(-767530797,543460314,-360414644,217821672,\\
&\hspace{39mm}-114360784,47364768,-11942720),\\
(w_{3d})&=\frac1{512}
(-169043,91892,-42296,14840,-3024,0,0).
\end{aligned}
\tag{12.1}
$$


These are precisely the JSON weights at equation blocks starting at $0,11,22,33$.

Define


$$
W_i(n)=\sum_{d=0}^6w_{id}n^{6-d},
\qquad W_4=W_5=0,
$$


and


$$
G_i=\nu W_i,\qquad
H_i=\mu\sum_{k=0}^3K_{ik}W_k.
$$


For $r=0,1,2,3$, put


$$
g_{ir}=[n^{6-r}]G_i,\qquad
h_{ir}=[n^{6-r}]H_i.
$$



Direct polynomial multiplication gives the following small table:


$$
\begin{array}{c|c|c}
i&(g_{i0},g_{i1},g_{i2},g_{i3})
 &(h_{i0},h_{i1},h_{i2},h_{i3})\\ \hline
0&(-6,12,-18,16)&(6,-18,48,-112)\\
1&(-14,20,-22,-16)&(14,-34,76,-124)\\
2&\frac1{32}(1107,-979,915,-659)
 &\frac1{32}(-1107,2086,-3980,7448)\\
3&(-4,4,-10,42)&(4,-8,22,-88)\\
4&(0,0,0,0)&(0,0,0,\ *)\\
5&(0,0,0,0)&(0,0,0,\ *)
\end{array}
\tag{12.2}
$$


The starred entries are unused because $A_4,A_5$ have degree at most $2$.

For clarity, the polynomials used for the second column of this verification can be written without a Kronecker product. With $s_2=n^2+3n+1$,


$$
\begin{aligned}
H_0&=\mu(n+1)(n+2)W_3,\\
H_1&=\mu\bigl((n+1)^2W_2+(n+1)(2n+3)W_3\bigr),\\
H_2&=\mu\bigl((n+2)W_1-s_2W_3\bigr),\\
H_3&=\mu\left((n+1)W_0+(2n+3)W_1
-\frac{(n+1)s_2}{n+2}W_2
-\frac{(2n+3)s_2}{n+2}W_3\right),\\
H_4&=\mu(n+2)\bigl(-(2n+3)W_1+s_2W_3\bigr),\\
H_5&=\mu\bigl(-(n+1)(2n+3)W_0-(2n+3)^2W_1\\
&\hspace{30mm}+(n+1)s_2W_2+(2n+3)s_2W_3\bigr).
\end{aligned}
\tag{12.3}
$$


All denominators in (12.3) cancel against $\mu$.

For the unknown $a_{ij}$, the witness product with its column is


$$
\sum_{r=0}^j\binom jr h_{ir}+g_{ij}.
\tag{12.4}
$$


Every value in (12.4) is zero by (12.2), for $j\le3$ in the first four components and $j\le2$ in the last two. This proves


$$
w^TA=0.
$$



The componentwise witness products with (10.6) are


$$
(0,\ 1,\ -5,\ 5,\ 0,\ 0).
\tag{12.5}
$$


For example, the component-$2$ numerator over $32768$ is $-163840$, giving $-5$. Therefore


$$
\boxed{w^Tb=1.}
\tag{12.6}
$$



Equations (12.4) and (12.6) are an exact inconsistency proof. Together with (11.3), they give


$$
\boxed{\operatorname{rank}A=22,\qquad
\operatorname{rank}(A\mid b)=23.}
$$



No seed equation was used, and none is needed.

---

## 13. What the endpoint decision excludes—and what it does not

The conclusion is


$$
\boxed{\text{No rational row }\ell(n)\in\mathbb Q(n)^6
\text{ satisfies (10.3).}}
\tag{13.1}
$$


This is not merely a failed guessed denominator or degree class.

It does **not** prove:

- nonexistence of every endpoint representation;
- nonexistence of nonrational gauges;
- nonexistence of representations using additional coordinates;
- a contact-gcd or resonance bound;
- a favorable primitive-denominator estimate.

There is one further distinction worth making explicit. A rational formula valid only after evaluation on the particular sequence $\mathbf Y_n$ need not automatically be a coefficientwise gauge: its residual might be a nonzero rational row annihilating that sequence. Excluding such formulas requires either rational independence of the actual sequence coordinates or a calculation in their actual relation quotient. That issue is not settled by the present gauge certificate.

---

# Part IV. Replacement targets and paid arithmetic

## 14. What replaces the excluded rational gauge

Searching again over larger rational denominators or numerator degrees for (10.3) is no longer a mathematical obligation. It is ruled out by the theorem.

A natural exact replacement is to retain the forced endpoint as a seventh coordinate:


$$
\begin{pmatrix}\mathcal K_{n+1}\\ \mathbf Y_{n+1}\end{pmatrix}
=
\begin{pmatrix}
-(n+1)^2&\gamma(n)\\
0&K(n)
\end{pmatrix}
\begin{pmatrix}\mathcal K_n\\ \mathbf Y_n\end{pmatrix},
\tag{14.1}
$$


with the actual seed


$$
\mathcal K_2=14,\qquad
\mathbf Y_2=(0,0,20,40,-132,-264)^T.
$$


Multiplication by $4(n+1)(n+2)$ clears every entry of this step matrix integrally. This is a sufficient step clearer only, not the producer’s least simultaneous clearer.

The rational-gauge obstruction says that this extension cannot be split by the stated rational row change of coordinates. The appropriate follow-on options are therefore:

1. work directly with the actual seeded seven-coordinate extension;
2. find a different, explicitly paid nonrational or enlarged endpoint representation;
3. determine the actual rational relation module of $\mathbf Y_n$, if a sequence-specific representation is sought.

The arithmetic target remains an actual-contact bound. In particular, a useful certificate must control the retained denominators


$$
D_j=\frac{|\widehat R_j|}
{\gcd(|\widehat R_j|,|F|)}
$$


and the complete endpoint residuals, including primes with $v_p(F)=0$. Adding $F$ as an extra ideal generator can lose precisely that unit-force branch.

A concrete remaining target is an actual-contact Bézout/support estimate yielding


$$
\log J_{\rm res}=o(n\log n)
$$


on an explicitly specified infinite original endpoint subsequence, followed by the required all-prime bound for the actual producer pair. The gauge decision supplies no such estimate.

---

## 15. Binary payment and primitive depth

The boundary cancellation, common-module merge and derivative certificates introduce no additional whole-combination division:


$$
e_{\rm sum}=0.
$$


They do not remove existing divisions.

Examples of compulsory payments include:

- the normalization $\mathfrak f=f^0/R$;
- factorial divisions in falling-factorial binomial evaluation;
- the whole primitive divisions in (1.3);
- the original $4b!$ normalization of the complete second column.

For the force normalization,


$$
v_2(R)=h+s_2(n),
$$


so a direct evaluation of $f^0/R$ at depth $L$ must account for that loss. A short support theorem is not a short computation of the normalized force.

For example, falling-factorial evaluation of


$$
2^r\binom hr\pmod{2^L}
$$


requires the corresponding parameter precision, such as


$$
h\pmod{2^{L-r+v_2(r!)}}.
$$


Similarly, evaluating $\binom{n+2}{d}$ in that manner requires


$$
n+2\pmod{2^{L+v_2(d!)}}.
$$



The primitive output depths remain


$$
\boxed{L_Q=K+2a+2,\qquad L_E=K+a+3.}
\tag{15.1}
$$


The entire raw observation must be obtained before its whole division. No tail or terminal is divided separately.

The logarithmic guard also remains unchanged:


$$
B_*=n-v_2(b!)-1-2s_2(n)-\ell.
$$


Outside the range protected after all normalizations, the complete original logarithmic contribution must be evaluated.

---

## 16. Least clearer, final gcd, actual denominator, and whole error

### 16.1 Binary producer

Retain


$$
\omega_j=j!W_j,\qquad
u_j=\frac{2\Lambda R\,x_j}{\omega_j},\qquad
v_j=\frac{4b!\,y_j}{\omega_j}.
$$


The actual least simultaneous clearer is


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


the actual integers and primitive pair remain


$$
A_B=d_B^2\,4\Lambda^2R^2\mathcal N,
\qquad
H_B=d_B^2\,8\Lambda Rb!\mathcal H,
$$




$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
}
\tag{16.1}
$$


The gcd is over **all primes**.

The retained valuation identity is


$$
v_p(q_n)=
\max\left\{
v_p\!\left(\frac{\Lambda R}{2b!}\right)
+v_p(\mathcal N)-v_p(\mathcal H),\,0
\right\}.
$$


The established ternary law


$$
v_3(q_n)=n-\frac{b+15}{2}
$$


is reused at its stated original-family scope, not recomputed.

Finally,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
\qquad
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
\tag{16.2}
$$



### 16.2 Endpoint producer

The complete endpoint reconstruction retains its exterior $+1$, the least simultaneous clearer of all eight entries,


$$
D_8=\operatorname{lcm}_{0\le j\le3}
\{\operatorname{den}(u_j),\operatorname{den}(v_j)\},
$$


and the actual row contents


$$
g_j=\gcd(|D_8u_j|,|D_8v_j|).
$$


The accepted finite contents at $3375$ are not altered or recomputed.

The complete residual remains


$$
C_j^{\rm complete}
=\mathcal E_j^\circ+
2n!(n+1)!\bigl(\alpha_j\rho_n+\beta_j\rho_{n+1}\bigr),
$$


with


$$
d_j=
\frac{|n!R_j|}
{\gcd(|n!R_j|,|E_nR_j+C_j^{\rm complete}|)}.
$$


The supplied weighted producer’s actual denominator remains


$$
q_\lambda=
\frac{k_{\rm wt}h_{\rm end}|A_{\rm wt}B_{\rm wt}|}
{F_{\rm gcd}G_{\rm wt}H_{\rm gcd}},
$$


with every prescribed gcd taken over all primes. It is not replaced by a gauge denominator or a step clearer.

Its whole error remains


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=q_\lambda e_3\alpha_{n,2}(\lambda-\Lambda_{n,2}).
}
\tag{16.3}
$$



For either producer, an irrationality argument still requires a nonzero whole error and a favorable estimate involving the actual primitive denominator on the **same infinitely many original indices**. For example,


$$
0<|q_n(e+\pi)-p_n|\longrightarrow0
$$


would contradict rationality. Neither reviewed theorem establishes this.

---

## 17. Bounded verification specification

No new producer-scale computation is required to prove the two audited statements, and no tool execution was performed here.

If the coordinator wants a compact independent arithmetic receipt for the endpoint witness—without repeating elimination—the bounded inputs are:

- the matrices (10.1)–(10.2);
- $\mu,\nu$ from (10.4);
- the four weight lists (12.1);
- the six forcing polynomials (10.6).

The required operations are polynomial multiplication and coefficient extraction in degree at most $14$.

Expected verifiable outputs are:

1. the table (12.2);
2. the $22$ zero values in (12.4);
3. the componentwise right-hand-side products
   

$$
(0,1,-5,5,0,0);
$$


4. their sum $1$.

No rank computation is needed: rank $22$ follows from the homogeneous infinity argument.

The $25$-position binary check should not be repeated. A future binary relative-membership computation would need, before it is well specified, an actual original parameter specialization, a certified content/depth, a candidate $r$, and explicit support bounds for $H_X,H_Y,H_t$. Failure in a bounded box would have only that bounded scope.

---

## 18. Final proof-status ledger

| Statement | Referee conclusion |
|---|---|
| Whole first-force completion above contact | Proved modulo the paid raw modulus |
| Whole complete-source completion, including returns and high endpoint | Proved |
| Extended head/type-$2$ formulas agree with full $\mathcal J$-action | Proved |
| Assembled tails equal complete physical terminals | Proved |
| Tail-free assembled observation formula | Proved |
| At most $32$ tuples and absolute-coordinate union bound | Proved |
| Common integral exponent module | Proved |
| Three derivative images annihilate acceptance | Proved |
| Full acceptance kernel equals those images | Open |
| Actual relative-polynomial membership or infinite-original nonzero digit | Open |
| Universal endpoint denominator and degree bounds | Valid |
| Certificate labels, multiplier, forcing sign, and degree coverage | Valid |
| Exact left-null witness | Valid |
| No rational gauge of the displayed six-component type | Proved |
| No endpoint representation of any kind | Not proved and not implied |
| Actual-contact resonance or all-prime gcd improvement | Open |
| Same-index nonzero whole-error/primitive-denominator comparison | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

## Conclusion

The genuinely changed conclusions are these:



$$
\boxed{
\text{The complete binary exterior boundary observation is now rigorously closed.}
}
$$





$$
\boxed{
\text{The displayed endpoint rational-gauge problem is now rigorously closed negatively.}
}
$$



The binary bottleneck is no longer an unproved tail correction: it is the paid observation of the **actual source-dependent common-module polynomials**, or an explicit integral relative-membership certificate at true primitive depth.

The endpoint bottleneck is no longer finding a larger rational ansatz for the same gauge. The replacement is an actual seeded nonsplit extension, another explicitly paid representation, or the actual sequence-relation quotient, followed by a genuine contact/arithmetic estimate.

Beyond both local reductions, the decisive global obligation is unchanged: control the actual contents, least simultaneous clearer, **all-prime final gcd**, actual primitive denominator, and **nonzero whole evaluated error on the same infinite original indices**.

**No unconditional proof of either rationality or irrationality of $e+\pi$ has been obtained.**
