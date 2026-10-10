> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1 continuation — Weighted edge defects and a relative inverse certificate

## Executive summary

I do **not** establish or refute the proposed two-edge congruence for the complete core columns:


$$
[x^a]F_i\equiv0\pmod{3^{10}}\quad(0\le a<27),\qquad
[y^{m-k}]F_i\equiv0\pmod{3^{10}}\quad(0\le k<9).
$$


The supplied precision-$27$ support theorem and the two completed producer receipts do not establish these assertions. In particular, producer locality is not a locality theorem for the complete eliminated core.

There is, however, a useful improvement to the outstanding obligation. The upper-edge hypothesis in turn22 is substantially stronger than its multiplier argument requires. A sufficient replacement is


$$
\boxed{
[y^{m-k}]F_i\in3^{9-k}\mathbb Z_3
\qquad(0\le k\le8).
}
\tag{A}
$$


There is also a weaker, producer-dependent lower-edge condition:


$$
\boxed{
[x^a](qF_i)\in3^{10}\mathbb Z_3
\qquad(0\le a<27),
}
\tag{B}
$$


where $q$ is the degree-$\le27$ polynomial in the retained congruence


$$
\mathscr R\equiv(y+1)x^{A-27}q(x)\pmod{3^{10}}.
$$


Conditions (A) and (B), together with the retained complete-core orthogonality, imply


$$
\Phi_R\in3^{11}M,\qquad S_{\rm act}\in3^{17}M.
$$



More generally, I derive an explicit **boundary-defect identity**. It identifies exactly which pairings remain if these sufficient edge conditions fail. Failure of a coefficientwise edge condition need not be an obstruction to depth $17$: the relevant boundary defects can still pair to zero against the complete core.

For the inverse problem, I give a single finite-matrix certificate that would simultaneously:

1. prove core invertibility and an effective upper inverse-loss bound;
2. prove relative stability under the actual perturbation;
3. prove nonvanishing of the distinguished bordered cofactor.

No such certificate is evaluated here. Its advantage is that it measures the **actual relative perturbation**, rather than requiring an unnecessarily strong entrywise perturbation bound.

Thus the strongest established original-family Schur conclusion remains


$$
\boxed{S_{\rm act}\in3^{16}M.}
$$


The rationality or irrationality of $e+\pi$ remains unresolved.

---

## 1. Domain, accepted results, and audit limits

Throughout, the indices remain


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$


with


$$
m=2^{2j-1},\quad n=4^j+1,\quad A=n-2,\quad
H=3^{h-1},\quad D=H-A,
$$


and


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$


All uniform statements concern sufficiently large members of this retained window.

The finite spaces are exactly


$$
U_u=x^u\ (0\le u<D),\qquad
z_i=x^Dy^i\ (0\le i<\nu),\qquad
Y_b=y^b\ (d\le b\le m),
$$


where


$$
x=y-1,\qquad d=\frac{3D}{2}-1,\qquad \nu=\frac D2-1.
$$


I use $F_i=\widehat z_i^{\,c}$ for the **complete** core columns.

The functional is unchanged:


$$
\mathcal M(G)=
-\frac{3^h}{4}\mathfrak f(G)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](G-G(-1))/(y+1)}{2v+1},
\qquad \mathfrak f(y^r)=(2r)!.
\tag{1.1}
$$


Every application below uses this functional, including its factorial term and its original cutoff.

### 1.1 What the receipts establish

The two receipts, at their proved producer-locality scope, give


$$
c=0,\qquad g_0=g_1=g_2=0.
$$


I do not rerun or request either calculation. Their small full-matrix checks and wider suffix checks remain finite validation.

The retained turn22 conclusions used here are


$$
R_{\rm prod}=3\mathscr R,\qquad
\mathcal Q\in3^5M,
$$




$$
S_c\in3^{17}M,\qquad \Phi_R\in3^{10}M,
$$


and


$$
S_{\rm act}=S_c+3^6\Phi_R-3^{13}\mathcal Q.
\tag{1.2}
$$


Consequently,


$$
S_{\rm act}\in3^{17}M
\iff
\Phi_R\in3^{11}M.
\tag{1.3}
$$



### 1.2 Audit finding relevant to A1

I found no explicit contradiction in the displayed multiplier proof in turn22. Its problem is not a demonstrated false algebraic step; its hypotheses are unproved at the required precision.

Two scope restrictions are essential:

* The precision-$27$ complete-core support statement does not imply precision-$3^{10}$ edge vanishing.
* The positive-unit producer matrices in the receipts are not the eliminated core matrix. Their bounded propagation radii do not transfer automatically to $F_i$.

Several earlier complete-core support and normalization results are cited rather than derived in the attached reports. I reuse them only at the stated precision and scope. In particular, I do not extrapolate their support widths to ten digits.

The known statement $s_c\ge17$ is still only a **lower** bound on inverse loss. It cannot pay any inverse division.

---

## 2. A less restrictive two-edge theorem

Write


$$
Q_c=(y+1)x^A(\beta+3y)
=(y+1)x^A(b+3x),\qquad b=\beta+3\in\mathbb Z_3^\times.
$$


Reuse turn22’s proved producer support:


$$
\mathscr R\equiv(y+1)x^{A-27}q(x)\pmod{3^{10}},
\qquad \deg q\le27.
\tag{2.1}
$$



Define


$$
T(x)=\sum_{r=0}^{9}\frac{(-3x)^r}{b^{r+1}}.
\tag{2.2}
$$


Then


$$
(b+3x)T(x)=1-\left(-\frac{3x}{b}\right)^{10}
\equiv1\pmod{3^{10}}.
\tag{2.3}
$$



### Theorem 2.1 — Weighted-edge sufficient condition

Suppose, for every original residual index $i$,

1. the first $27$ $x$-coefficients of $qF_i$ belong to $3^{10}\mathbb Z_3$;
2. the upper coefficients satisfy
   

$$
[y^{m-k}]F_i\in3^{9-k}\mathbb Z_3
   \qquad(0\le k\le8).
   \tag{2.4}
$$



Then


$$
\Phi_{\mathscr R}\in3^{10}M,\qquad
\Phi_R\in3^{11}M,\qquad
S_{\rm act}\in3^{17}M.
$$



#### Proof

Set


$$
P_i=qF_i,\qquad
L_i=\sum_{a=0}^{26}[x^a]P_i\,x^a,\qquad
V_i=\frac{P_i-L_i}{x^{27}}.
\tag{2.5}
$$


These are integral polynomials, and $\deg V_i\le m$. The first hypothesis gives


$$
L_i\in3^{10}\mathbb Z_3[x].
\tag{2.6}
$$



We first transport (2.4) from $y$-coefficients to $x$-coefficients. Since $y=x+1$,


$$
[x^{m-k}]F_i
=
\sum_{t=0}^{k}
\binom{m-t}{m-k}[y^{m-t}]F_i.
$$


Each summand has valuation at least $9-t\ge9-k$. Therefore


$$
[x^{m-k}]F_i\in3^{9-k}\mathbb Z_3.
\tag{2.7}
$$



For $0\le k\le8$,


$$
[x^{m-k}]V_i=[x^{m+27-k}](qF_i).
$$


Writing $q=\sum_{\ell=0}^{27}q_\ell x^\ell$, only $\ell\ge27-k$ can contribute. Each contribution contains a coefficient


$$
[x^{m-t}]F_i,\qquad 0\le t\le k,
$$


and hence has valuation at least $9-k$. Thus


$$
[x^{m-k}]V_i\in3^{9-k}\mathbb Z_3.
\tag{2.8}
$$



Let


$$
K_i=\operatorname{tail}_{>m}(V_iT),\qquad
H_i=V_iT-K_i.
\tag{2.9}
$$


By construction, $\deg H_i\le m$.

A contribution to $K_i$ from the term of degree $r$ in $T$ uses a coefficient of $V_i$ of degree $m-k$ with


$$
0\le k<r\le9.
$$


Its valuation is at least


$$
r+(9-k)\ge10.
$$


Consequently,


$$
K_i\in3^{10}\mathbb Z_3[x].
\tag{2.10}
$$



Using (2.1), (2.3), (2.5), (2.6), and (2.10),


$$
\begin{aligned}
\mathscr RF_i
&\equiv
(y+1)\bigl(x^{A-27}L_i+x^AV_i\bigr)\\
&\equiv
(y+1)x^A(b+3x)H_i\\
&=Q_cH_i
\pmod{3^{10}}.
\end{aligned}
\tag{2.11}
$$



The fixed-cutoff functional maps integral polynomials to $\mathbb Z_3$. Multiplication by the integral complete column $F_j$ therefore gives


$$
\mathcal M(\mathscr RF_iF_j)
\equiv
\mathcal M(Q_cH_iF_j)
\pmod{3^{10}}.
\tag{2.12}
$$



The retained integral basis $[W,F]$ spans the polynomials of degree at most $m$. Decompose $H_i$ in that basis. Its $W$-part pairs to zero by complete-core orthogonality; its residual part pairs through $S_c\in3^{17}M$. Hence the right side of (2.12) is zero modulo $3^{10}$.

Thus $\Phi_{\mathscr R}\in3^{10}M$. Since $R_{\rm prod}=3\mathscr R$, linearity gives $\Phi_R\in3^{11}M$. Equation (1.2) completes the proof. ∎

### Significance

The upper-edge requirements are now


$$
3^9,\ 3^8,\ 3^7,\ldots,\ 3
$$


rather than nine copies of $3^{10}$. The lower condition can also be weaker than vanishing of the corresponding coefficients of $F_i$: multiplication by the actual $q$ may create additional divisibility or cancellation.

These are genuine reductions of the sufficient hypotheses. They are **not** proofs that the actual columns satisfy them.

---

## 3. The exact boundary obstruction if the sufficient jets fail

The preceding construction also gives an identity without either edge hypothesis.

Keep $L_i,V_i,H_i,K_i$ as in (2.5) and (2.9), and define the actual finite-degree defect


$$
B_i=\mathscr RF_i-Q_cH_i.
\tag{3.1}
$$


Then


$$
\boxed{
B_i\equiv
(y+1)\left(
x^{A-27}L_i+x^A(b+3x)K_i
\right)
\pmod{3^{10}}.
}
\tag{3.2}
$$



Indeed, substitute $V_iT=H_i+K_i$ into (2.3). The only discarded term is coefficientwise divisible by $3^{10}$.

The polynomial $B_i$ in (3.1) is the object to which the original functional is applied. The expression involving $K_i$ is an algebraic description of its residue; it introduces no new HIGH coordinate or residual column.

Complete-core orthogonality now yields


$$
\boxed{
(\Phi_{\mathscr R})_{ji}
\equiv\mathcal M(F_jB_i)\pmod{3^{10}}.
}
\tag{3.3}
$$



### Corollary 3.1 — Exact replacement for the coefficientwise test

At the retained scope,


$$
\boxed{
\Phi_R\in3^{11}M
\iff
\mathcal M(F_jB_i)\in3^{10}\mathbb Z_3
\quad\text{for all }i,j.
}
\tag{3.4}
$$



Thus there are two possible routes:

* prove the boundary defects themselves vanish modulo $3^{10}$;
* prove their **complete pairings** vanish modulo $3^{10}$.

The second route is strictly more general. A nonzero upper or lower edge coefficient does not, by itself, refute depth $17$.

This identifies the actual boundary obstruction more precisely than an unweighted two-edge support claim. What remains unavailable is an original-domain transport theorem for $L_i$, $K_i$, or their complete pairings.

### A quantitative version

If


$$
L_i\in3^\lambda\mathbb Z_3[x],\qquad
K_i\in3^\mu\mathbb Z_3[x]
$$


uniformly, then (3.2)–(3.3) imply


$$
\Phi_R\in3^{1+\min(10,\lambda,\mu)}M.
\tag{3.5}
$$


This can be combined with the already established $\Phi_R\in3^{10}M$; it must not replace that stronger retained bound when the new minimum is smaller.

Without further boundary information, the strongest established conclusion remains


$$
\Phi_R\in3^{10}M,\qquad S_{\rm act}\in3^{16}M.
$$



---

## 4. An effective inverse and cofactor certificate

An absolute Schur-depth calculation does not establish invertibility. The following certificate addresses the actual finite matrix and all inverse divisions explicitly.

### Theorem 4.1 — Paid approximate-inverse certificate

Let $S\in M_\nu(\mathbb Z_3)$. Suppose an integral matrix $B$, integers $t\ge0$, $k\ge1$, and an integral matrix $R$ satisfy


$$
BS=3^t(I+R),\qquad R\in3^kM_\nu(\mathbb Z_3).
\tag{4.1}
$$


Then $S$ is invertible and


$$
S^{-1}=3^{-t}(I+R)^{-1}B.
\tag{4.2}
$$


In particular,


$$
3^tS^{-1}\in M_\nu(\mathbb Z_3),
\tag{4.3}
$$


so the actual inverse loss is at most $t$.

If $S_{\rm act}=S+\Delta$ and


$$
B\Delta\in3^{t+1}M,
\tag{4.4}
$$


then


$$
S^{-1}\Delta\in3M.
\tag{4.5}
$$


Hence $S_{\rm act}$ is invertible, its inverse loss is also at most $t$, and


$$
\frac{\det S_{\rm act}}{\det S}\in1+3\mathbb Z_3.
\tag{4.6}
$$



#### Proof

The matrix $I+R$ is unimodular. Equation (4.1) therefore shows that $BS$ is invertible over $\mathbb Q_3$, so both square factors are invertible. Formula (4.2) follows immediately and proves (4.3).

By (4.2) and (4.4),


$$
S^{-1}\Delta
=(I+R)^{-1}3^{-t}B\Delta\in3M.
$$


Thus


$$
S_{\rm act}=S(I+S^{-1}\Delta)
$$


has a unimodular second factor. This proves the inverse and determinant assertions. ∎

The relative condition (4.4) can be substantially weaker than


$$
\Delta\in3^{t+1}M.
$$


It permits the actual perturbation to lie in directions on which the paid inverse numerator $B$ has additional divisibility.

### Distinguished cofactor

Let $e\in\mathbb Z_3^\nu$, $d\in\mathbb Z_3$, and define


$$
C=e^T\operatorname{adj}(S)e-d\det S.
\tag{4.7}
$$


Under (4.1), put


$$
w=e^TBe-3^td.
\tag{4.8}
$$


If


$$
u=v_3(w)<k,
\tag{4.9}
$$


then


$$
\boxed{
C\ne0,\qquad
v_3(C)=v_3(\det S)+u-t.
}
\tag{4.10}
$$



To prove this, note that


$$
(I+R)^{-1}B-B\in3^kM.
$$


Therefore


$$
3^t(e^TS^{-1}e-d)\equiv w\pmod{3^k}.
$$


Condition (4.9) determines the valuation of the left side exactly. Finally,


$$
C=\det S\,(e^TS^{-1}e-d).
$$



This is a noncancellation test for the **whole bordered expression**. Endpoint units alone do not supply it.

### What this does not prove

No $B,t,k$ satisfying these conditions have been constructed for the original core. The theorem supplies an effective verification target, not an upper inverse bound already achieved.

A useful next structural lemma would construct $B$ from the genuine finite eliminated operator, with:

* a uniform description of its boundary action;
* a proved residual $BS_c-3^tI$;
* a relative bound on $B(S_{\rm act}-S_c)$;
* a nonzero residue of the whole scalar (4.8), using the actual endpoint and diagonal term.

This would advance the inverse problem in a way that another producer digit does not.

---

## 5. Arithmetic specification and its scope

No new producer calculation is needed for Theorems 2.1–4.1. I do not commission the optional $452$-coordinate jet.

The next useful calculation must concern the complete core.

### Boundary certificate

For a specified actual original-window tuple $(j,h)$, the mathematical inputs are:

* the complete finite eliminated operator defining $F_i$;
* the actual polynomial $q\bmod3^{10}$;
* all complete columns, including their terminal corrections;
* the fixed functional (1.1).

A bounded certificate for that tuple consists of either:

1. the $27\nu$ lower residues
   

$$
[x^a](qF_i)\pmod{3^{10}}
$$


   and the $9\nu$ weighted upper residues
   

$$
[y^{m-k}]F_i\pmod{3^{9-k}},
$$


   all zero; or

2. if these are not zero, the complete defect-pairing matrix
   

$$
\bigl(\mathcal M(F_jB_i)\bmod3^{10}\bigr)_{j,i},
$$


   together with exact residual checks for the eliminated solves.

All nonunit divisions in constructing $F_i$ must be paid before reducing to these output moduli.

This is a finite certificate, not yet a fixed-width one. A fixed-width implementation requires precisely the missing core-transport theorem; producer locality cannot justify it.

### Inverse certificate

For the same actual index, inputs $S,\Delta,e,d,B,t,k$ should produce:



$$
BS-3^tI\equiv0\pmod{3^{t+k}},
$$




$$
B\Delta\equiv0\pmod{3^{t+1}},
$$


and a nonzero residue


$$
3^{-u}(e^TBe-3^td)\pmod3,\qquad u<k.
$$



These are bounded exact-arithmetic outputs with transparent divisions. A certificate at one index proves only that index. Uniform original-family conclusions require a structural construction or an exhaustive, proved finite-state reduction.

---

## 6. Consequences for the primitive approximation

Even a successful boundary certificate and inverse certificate would not, alone, prove irrationality.

Retain the actual row contents, actual multiplier, and least simultaneous clearer:


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$




$$
g_\ell=\gcd(|A_\ell|,|B_\ell|)
$$


over **all primes**. For $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
$$


and the whole error remains


$$
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
{g_\ell}\det H_{\rm complete}.
\tag{6.1}
$$



Nothing proved here modifies either exponential boundary column, the logarithmic forcing $F/(1-z)$, any exterior $+1$, or the physical terminal. None may be dropped in a later evaluation of (6.1).

A successful relative inverse certificate could protect the determinant and bordered-cofactor comparison. It would still not evaluate the final all-prime gcd, the actual primitive denominator, or the whole real error. The required infinite-index conclusion remains


$$
0<|q(e+\pi)-p|\longrightarrow0
$$


at the **same original indices**.

---

## Conclusion and proof status

The new proved result is a sharper boundary reduction:



$$
\boxed{
\begin{gathered}
[x^{<27}](qF_i)\equiv0\pmod{3^{10}},\\
[y^{m-k}]F_i\equiv0\pmod{3^{9-k}}\quad(0\le k\le8)
\end{gathered}
\ \Longrightarrow\
\Phi_R\in3^{11}M,\quad S_{\rm act}\in3^{17}M.
}
$$



The exact defect-pairing identity (3.3) remains valid when these sufficient edge conditions fail. It shows that the true obstruction is the complete boundary pairing, not merely a nonzero edge coefficient.

The original two-edge claim is **neither proved nor refuted here**. The precise local bottleneck is a ten-digit transport theorem for the genuine finite complete-core operator, with HIGH/LOW feedback and terminal corrections retained.

The inverse bottleneck is separate: construct and verify a paid approximate inverse with a useful relative perturbation bound and a nonzero whole bordered scalar. Theorem 4.1 gives an explicit certificate for that task, but no actual upper inverse bound or distinguished-cofactor nonvanishing has yet been obtained.

The cited automatic-congruence and creative-telescoping methods remain relevant machinery, not evaluations of these complete finite responses. No new literature search or theorem settling this obligation is claimed.



$$
\boxed{\text{The rationality or irrationality of }e+\pi\text{ remains unresolved.}}
$$


