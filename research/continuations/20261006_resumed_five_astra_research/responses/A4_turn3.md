> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4, Turn 3 — Independent audits, a repaired resonance intersection, and sharper specialized moment-content identities

## Executive conclusions

The three reports make genuine advances, but none closes the actual primitive-denominator/whole-error comparison needed for irrationality of $e+\pi$.

My independent conclusions are as follows.

1. **A1’s exact Jacobi/factorial comparison and inverse-loss stability are valid.** The pole integral uses exactly the original finite cutoff. The factorial matrix remains present and is an integral $3^h$-perturbation. The full-versus-Schur comparison is also valid under the retained corrected-column integrality.

2. **The normalization objection can be repaired on an infinite subfamily of the current $C_{16}$ window.** Deep resonance already forces
   

$$
j\equiv81\pmod{243}
$$


   once its depth is at least $6$. A quantitative arithmetic-progression/real-window intersection argument supplies the narrower $C_{16}$ window while preserving
   

$$
\log(j+1)=O(t).
$$


   This repairs the application of the old unit-normalized continuation to that subfamily—not to every current-window index. Importantly, it does **not** require the separate endpoint-unit digit condition on $J_m(-1)$.

3. **A1’s eight-state content evaluator and whole Bézout pivot identity are correct at their stated scopes.** The generalized-binomial borrow tail terminates here because the half-integral upper parameters have eventually constant ternary digit $1$. The collision
   

$$
\operatorname{cont}_3(J_m)=4+\operatorname{cont}_3(J_{m-1})
$$


   remains genuinely unresolved. A bound for $J_m$ alone cannot decide it.

4. **A5’s new exterior-load and four-variable contraction construction survives the audit.** In particular:
   - the finite exterior-load factorization has the right order;
   - signed reversal and the band correction preserve the boundary $b-1$;
   - the Laurent principal part produces the exterior $+1$ with the correct sign;
   - reconstruction raises the first-branch exponent from $2n+124$ to $2n+125$;
   - consequently the additional kernel pole is $123$, not $124$;
   - the $x$- and $y$-shifts remain independent.

   The proposed short-numerator construction is a valid new bounded calculation using the accepted Schur inverse. It contains no operation linear in $b$, provided its complete first-force input is supplied. The subsequent high-coefficient extraction remains unevaluated and has no proved practical resource bound.

5. **The specialized A3 content restriction admits a useful strengthening.** At every prime $p>n+2$, the actual exponential third coordinate is a unit whenever the first two primitive-row outputs have positive common valuation. Thus the actual triple primitivization loses no additional $p$-content:
   

$$
\boxed{
   v_p(\gamma_j)
   =
   \min\{v_p(r_jv),v_p(r_jw)\},
   \qquad j=0,3.
   }
$$


   This uses the evaluated terminal return and, at endpoint $0$, the exterior correction.

   Moreover, the linear-defect upper bounds become equalities outside two explicit quadratic exceptional factors, and the common structural content has an exact formula:
   

$$
\boxed{
   \gcd(\gamma_0,\gamma_3)_{>n+2}
   =
   \gcd\!\left(
   |D_{\rm mom}H|,
   |D_{\rm mom}B_0^\partial|,
   |P_n|
   \right)_{>n+2}.
   }
$$


   This sharpens the one-moment product bound and the structural imbalance bound.

No computation was executed. I do not request repetition of the accepted Schur solve, any accepted producer, any accepted finite bound, or the coordinator’s current $n=225$ post-processing for $\mathcal B,\mathcal F$.

---

# 1. Scope and notation

The three original domains remain separate.

### Ternary Jacobi/Schur domain



$$
n=4^j+1,\qquad 81\mid j,\qquad j>0,
$$




$$
A=4^j-1=H-D,\qquad H=3^{h-1},\qquad
m=\frac{A+1}{2}=2^{2j-1},
$$


with the current window


$$
j\equiv81\pmod{243},
\qquad
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad
C_{16}=147968\,3^{15}.
$$



### Binary weighted-contact domain



$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
$$


For A5’s proposed new calculation, $u=0$, $M=20$, and


$$
b=150094635296999121,\qquad
n=600678730458590482242.
$$


The contact coordinates are $0,\ldots,b-1$, and reconstruction ends at $b$.

### Three-contact complete-endpoint domain



$$
n=15^r,\quad r\ge2,
\qquad\text{or}\qquad
n=105^r,\quad r\ge2.
$$


The contact coordinates remain $0,1,2$, reconstruction remains $0,1,2,3$, and the complete producer ends at $2n+2$.

In this last domain I use


$$
b=c_{n-1},\qquad c=c_n,\qquad d=c_{n+1}
$$


only inside the moment-content discussion. These are moments, not the large contact boundary in A5.

---

# 2. A1 audit: the exact comparison and its normalization scope

## 2.1 The pure Jacobi/factorial comparison is exact

For


$$
Q_c(y)=(y+1)(y-1)^A(-71-A+3y)
$$


and $P,Q\in\mathcal P_m$,


$$
\frac{Q_cPQ}{y+1}=(y-1)^A(-71-A+3y)PQ.
$$


Its degree is at most


$$
A+1+2m=2A+2=2n-2.
$$


Therefore every coefficient is included in the original pole range


$$
2v+1\le4n-3.
$$



There is no missing tail between the finite pole sum and the integral. Consequently


$$
\boxed{
G_c=G_J+3^hF_c,
\qquad
(F_c)_{ab}=-\frac14\mathfrak f(Q_cy^{a+b}),
}
$$


with


$$
F_c\in M_{m+1}(\mathbb Z_3).
$$



This statement retains the full factorial evaluation. It does not replace it by zero.

The pure matrix is nonsingular: $r_0=(A+71)/3>1$, so the integral weight has constant nonzero sign on $(0,1)$.

## 2.2 Inverse-loss stability is correctly proved

If


$$
M'=M+3^hF,\qquad F\in M_N(\mathbb Z_3),
\qquad \lambda(M)<h,
$$


then


$$
K=M^{-1}3^hF\in3M_N(\mathbb Z_3).
$$


Thus $I+K$ is unimodular and


$$
(M')^{-1}=(I+K)^{-1}M^{-1}.
$$


Left multiplication by an integral unimodular matrix preserves the minimum entry valuation. Hence


$$
\boxed{\lambda(M')=\lambda(M).}
$$



No unit hypothesis concerning a Jacobi polynomial is needed for this abstract stability statement. Such hypotheses enter only when the Jacobi formula is used to verify $\lambda(G_J)<h$.

## 2.3 Full-versus-Schur loss uses both corrected sides

The original columns $[U\ Z\ Y]$ form a monic degree-ordered basis, hence an integral unimodular basis. The retained integrality of


$$
L_c=E_c^{-1}B_c^{\rm mix}
$$


then gives the integral congruence


$$
G_c\sim_{\mathbb Z_3}\operatorname{diag}(E_c,S_c).
$$



This congruence is a simultaneous row-and-column correction. It is not justified by correcting only one factor in a bilinear product.

For nonsingular $S_c$,


$$
\lambda(G_c)=\max\{\lambda(E_c),\lambda(S_c)\}.
$$


The accepted bounds


$$
\lambda(E_c)\le1,\qquad S_c\in3^{26}M_\nu(\mathbb Z_3)
$$


give


$$
\lambda(G_c)=s_c
$$


because $s_c\ge26$. A1 correctly avoids promoting $\lambda(E_c)\le1$ to an unsupported equality.

---

# 3. Repairing the current-window resonance intersection

A1turn3 is right that the normalizer cannot be assigned its resonant valuation on every current-window index. However, the old established original-family continuation is enough to repair the scope on an infinite subfamily. Two points need to be made explicit.

## 3.1 Deep resonance already fixes the required residue class

Let


$$
\varepsilon=4^{j+1}-247,\qquad v_3(\varepsilon)=t.
$$


For $t\ge6$,


$$
4^{j+1}\equiv247\pmod{3^6}.
$$


Equivalently,


$$
4^j\equiv1+\frac{3^5}{4}\pmod{3^6}.
$$



First, LTE gives $v_3(j)=4$. Write $j=81a$, with $3\nmid a$. The elementary congruence


$$
4^{81}\equiv1+3^5\pmod{3^6}
$$


then yields


$$
4^j\equiv1+a3^5\pmod{3^6}.
$$


Since $4^{-1}\equiv1\pmod3$, comparison gives $a\equiv1\pmod3$. Therefore


$$
\boxed{
t\ge6\quad\Longrightarrow\quad j\equiv81\pmod{243}.
}
$$



Thus the residue requirement is not an additional restricted-digit conjecture.

## 3.2 A quantitative real-window intersection lemma

The needed real restriction is a fixed open interval. Let


$$
\vartheta=\frac{\log4}{\log3}.
$$


For $k=\lceil j\vartheta\rceil$, put $H=3^k$. Then


$$
\frac DH
=
1-3^{\{j\vartheta\}-1}+3^{-k}.
$$



Choose a closed interval strictly inside


$$
\left(
1+\log_3(1-C_{16}^{-1}),
\;
1+\log_3(1-(2C_{16})^{-1})
\right).
$$


If $\{j\vartheta\}$ lies in that smaller interval and $j$ is sufficiently large, then


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}}.
$$



It remains to impose this condition in the exact resonance progression without losing $\log j=O(t)$.

### Lemma 3.1 — Quantitative intersection

For every sufficiently large $t$, there is a positive integer $j$ such that


$$
v_3(4^{j+1}-247)=t,
$$




$$
j\equiv81\pmod{243},
\qquad
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
$$


and


$$
\log(j+1)=O(t),
$$


with a constant independent of $t$.

### Proof

The powers of $4$ generate the principal-unit subgroup modulo powers of $3$. Thus


$$
4^{j+1}\equiv247\pmod{3^t}
$$


specifies one residue class modulo $3^{t-1}$. Among its three lifts modulo $3^t$, exactly one has valuation at least $t+1$; the other two have valuation exactly $t$. Choose either of those two progressions:


$$
j=a_t+3^t k.
$$



A standard consequence of the archimedean theorem on nonzero linear forms in fixed logarithms of algebraic numbers gives constants $c>0,\kappa>0$ such that


$$
\|q\vartheta\|\ge c q^{-\kappa}\qquad(q\ge1).
$$


Here the relevant nonzero linear form is


$$
q\log4-p\log3.
$$


It is nonzero because $4^q\ne3^p$.

For completeness, this supplies the required hitting bound directly. Apply the Erdős–Turán discrepancy inequality to


$$
a_t\vartheta+k3^t\vartheta,\qquad 1\le k\le N.
$$


For a fixed frequency cutoff $K$, the geometric-sum bound and the displayed lower bound give


$$
D_N\ll \frac1K+\frac{3^{\kappa t}}N
\sum_{\ell=1}^{K}\ell^{\kappa-1}.
$$


Choose $K$ as a constant large enough for the fixed real interval, and then


$$
N=C\,3^{\kappa t}
$$


with $C$ sufficiently large. The discrepancy is smaller than the interval length, so the progression hits that interval. Consequently


$$
j=O(3^{(\kappa+1)t}),
$$


which gives $\log(j+1)=O(t)$.

The residue assertion follows from §3.1. ∎

This argument invokes an **archimedean fixed-logarithm lower bound**, not the supplied $3$-adic Bugeaud–Laurent estimate. The roles are different: the former supplies the quantitative real-window intersection; the latter is part of the already established resonant continuation.

## 3.3 What this repairs—and what it does not

The constructed indices satisfy the listed deep-resonance hypotheses used in A1turn1, including the growth condition needed for its bound


$$
3^t+t-D(1+t)^3.
$$


They also lie in the narrower current window. Therefore the retained continuation gives, on this sufficiently large subfamily,


$$
v_3(a_m)=1,\qquad \mathfrak a=a_m/3\equiv25\pmod{27}.
$$



The endpoint-unit criterion


$$
J_m(-1)\in\mathbb Z_3^\times
$$


is **not** needed to obtain this normalizer. It is a separate condition used for the fully evaluated endpoint-unit branch in A1turn1.

There is a second useful scope distinction. The formula


$$
N_m=9\kappa_m^2h_m
=
\frac{2^{2A+3}(3A+2)}
{(A+1)((4A+3)/3)\,U(m)}
$$


already proves $N_m\in\mathbb Z_3^\times$ whenever $v_3(A)=5$. That unit statement does not need the deep-resonance endpoint branch.

Hence:

- the current window does not establish $v_3(a_m)=1$ for all its indices;
- an infinite current-window deep-resonance subfamily does establish it;
- no intersection with the restricted-digit endpoint-unit branch has been proved or used.

On that certified subfamily,


$$
\boxed{
s_c=h-2-\operatorname{cont}_3(\mathcal E).
}
$$


This is a legitimate same-index application of the old normalization, not a blanket current-window assertion.

---

# 4. A1’s content rules: unit hypotheses and terminating tails

## 4.1 The polynomial-content formula is valid

The basis


$$
X^k(X-1)^{m-k},\qquad 0\le k\le m,
$$


is integral unimodular: its least-degree term has coefficient $(-1)^{m-k}$. Therefore


$$
\operatorname{cont}_3(J_m)
=
\min_k\left(
v_3\binom{3m-1}{k}
+
v_3\binom{m-\tfrac12}{m-k}
\right).
$$



This conclusion concerns the entire polynomial. It does not identify its content with the valuation at $X=-1$.

## 4.2 The generalized-binomial borrow rule is rigorous here

For $\alpha\in\mathbb Z_3$ and $r\ge0$, with none of


$$
\alpha,\alpha-1,\ldots,\alpha-r+1
$$


equal to zero, counting factors divisible by $3^a$ gives


$$
v_3\binom{\alpha}{r}
=
\sum_{a\ge1}
\left(
\#\{0\le i<r:i\equiv\alpha\pmod{3^a}\}
-\left\lfloor\frac r{3^a}\right\rfloor
\right).
$$


The summand is $1$ exactly when


$$
\alpha\bmod3^a<r\bmod3^a.
$$


That is the outgoing borrow after $a$ ternary positions.

For the present upper parameters


$$
m-\frac12,\qquad m-\frac32,
$$


no factor vanishes, and the ternary digits are eventually $1$. After the digits of the lower nonnegative integer have ended, an incoming borrow therefore clears at the next eventual-$1$ position.

Accordingly, A1’s eight-state dynamic program has a genuine finite termination rule.

The qualifications are important:

- this is not a claim that every arbitrary $3$-adic upper parameter has a uniformly short tail;
- an integer upper parameter with a vanishing binomial must be handled separately;
- the actual digits of $m=2^{2j-1}$ remain part of the input;
- a fixed number of states does not make construction of those actual digits free.

No unit assumption is required for this content evaluator.

## 4.3 The whole Bézout identity is correct

With


$$
T=XZ+\mathfrak a J_m,
$$


one has


$$
(X-Y)\mathcal E(X,Y)=T(X)Z(Y)-Z(X)T(Y).
$$


Multiplication by the primitive polynomial $X-Y$ preserves content, so


$$
\boxed{
\operatorname{cont}_3(\mathcal E)
=
\min_{i<k}v_3(t_i z_k-z_i t_k).
}
$$



If $z=\operatorname{cont}_3(Z)$ and $p$ is a coefficient position of minimum valuation, the pivot reduction gives


$$
\boxed{
\operatorname{cont}_3(\mathcal E)
=
z+\min_i v_3\!\left(
t_i-\frac{t_p}{\widetilde z_p}\widetilde z_i
\right),
\qquad \widetilde Z=3^{-z}Z.
}
$$



The pivot coefficient is a unit **after the actual content has been removed**. No endpoint-unit hypothesis is involved.

The certificate is linear in the coefficient length, not in the digit length of $m$. Thus a dense implementation remains an original-degree computation.

## 4.4 The collision branch remains open

On the certified scalar branch,


$$
v_3(\rho)=4,\qquad \mathfrak a\in\mathbb Z_3^\times,
$$


A1’s noncollision formulas are correct:


$$
\operatorname{cont}_3(\mathcal E)
=
2\min(r,4+u)
\qquad(r\ne4+u).
$$



At


$$
r=4+u,
$$


the construction of $Z$ can cancel, and the subsequent whole Bézout numerator can cancel again. Neither cancellation is decided by a bound for $r$ alone.

The repaired resonance intersection therefore does **not** prove $s_c<32$. It removes a normalization-scope obstruction on a genuine original subfamily and leaves the exact content decision intact.

---

# 5. A5 audit: the complete exterior-load construction

## 5.1 The source must be the normalized tail after factorial subtraction

A5 starts from


$$
r=\frac{h^e+h^F-A(j!)_{0\le j<b}}{b!}.
$$


Its exponential tail formula must be read as the formula for the exponential part **after** the actual finite factorial subtraction:


$$
r_i^e\equiv
\sum_{t=0}^{23}v_t
\sum_{s=0}^{76}\lambda_s
\binom{n+i}{s}\binom{2n+i-s}{b+t}
\pmod{2^{20}}.
$$



It must not be reinterpreted as a formula for $h_i^e/b!$ before subtraction.

With that interpretation, the complete factorial subtraction is retained in the construction. The bound $v_2(t!)\ge20$ for $t\ge24$ justifies the stated exterior-tail truncation.

## 5.2 The block factorization has the correct order

Partitioning at the actual contact boundary gives


$$
U_\infty=
\begin{pmatrix}U&T\\0&U_{\rm out}\end{pmatrix},
\qquad
H_\infty=
\begin{pmatrix}H&0\\K&H_{\rm out}\end{pmatrix}.
$$


Since $F=U^{-1}T$, the upper-left block of $U_\infty H_\infty U_\infty$ is


$$
U(H+FK)U=UJU.
$$


The upper-right block is


$$
UJT+T H_{\rm out}U_{\rm out}.
$$


Consequently


$$
A^{-1}A^+_{\rm out}
=
F+U^{-1}J^{-1}F H_{\rm out}U_{\rm out}.
$$



Applying the finite exterior load yields exactly A5’s formula


$$
\boxed{
A^{-1}r^e
=
F_{24}v+
U^{-1}J^{-1}F_{100}h^{\rm out}
\pmod{2^{20}}.
}
$$



The intermediate transfer indices through $99$ do not enlarge the solved contact system or reconstruction domain.

## 5.3 Signed reversal and the finite band boundary are correct

For $B=b-1$, signed reversal converts $U^{-1}$ into multiplication by


$$
t(z)=(1-z)^{-n},
$$


followed by projection to degrees $<b$.

The inverse-band action is


$$
\Psi G
=
\sum_{s=0}^{76}(-1)^sc_s
\binom{B-\theta}{s}
z^{-s}(G-P_{<s}G).
$$


At a retained coefficient $0\le k<b$, this gives


$$
\sum_s(-1)^sc_s\binom{B-k}{s}g_{k+s}.
$$



If $k+s\ge b$, then


$$
s>B-k,
$$


and the ordinary binomial coefficient is zero. Thus the analytic extension cannot return an unphysical coefficient across the finite boundary.

This is an exact finite-boundary mechanism, not an infinite-band approximation.

## 5.4 The full exterior transfer series has the right sign

Because $B$ is even,


$$
\boxed{
\mathcal F_r(z)
=
(-1)^rz^{-r-1}\bigl(t(z)P_r(z)-1\bigr),
\qquad
P_r=P_{\le r}(1-z)^n.
}
$$



The subtraction of $1$ is precisely the entire principal-part cancellation of the transfer column. In particular,


$$
tP_r-1=O(z^{r+1}),
$$


so $\mathcal F_r$ is analytic.

For a load,


$$
\mathcal F_\eta=tA_\eta-B_\eta.
$$


Dropping $B_\eta$ before applying $\Psi$ would alter the source and its Schur endpoint correction. A5 does not make that omission.

---

# 6. A5 reconstruction, exponent shifts, and the complete contraction

## 6.1 The Laurent principal part produces the exterior $+1$

A5’s contact representative satisfies


$$
G_e^*=G_e^{\rm an}+B_v,
\qquad
[z^{-1}]B_v=v_0=1.
$$


The reconstruction operator is


$$
\mathfrak C_b=\theta-b-z.
$$


Its constant coefficient on $G_e^*$ is therefore


$$
[z^0]\mathfrak C_bG_e^*
=
-b[z^0]G_e^{\rm an}-1.
$$



Since $b$ is odd, signed reversal changes an exterior $+1$ at physical coordinate $j=b$ into $-1$. The sign is correct.

At the opposite endpoint, $k=b$, the coefficient of the unneeded $g_b$ is zero:


$$
[z^b]\mathfrak C_bG=-g_{b-1}.
$$


Hence reconstruction still uses only contact coordinates $0,\ldots,b-1$.

## 6.2 The two-branch degree bounds are sound

With


$$
L_0=176,\qquad k_0=124,
$$


the contact representatives have the form


$$
G_\alpha
=
z^{-L_0}\left(
\frac{P_{\alpha,2}}{(1-z)^{2n+124}}
+
\frac{P_{\alpha,1}}{(1-z)^n}
\right),
$$


where


$$
\deg P_{\alpha,2}\le299,\qquad
\deg P_{\alpha,1}\le175.
$$



The divided-derivative formula used to obtain this form is integral. It does not require inversion of $s!$ modulo $2^{20}$.

Reconstruction raises each branch denominator exponent by one:


$$
\widehat G_\alpha
=
z^{-176}\sum_{\rho=1}^2
\frac{\widehat P_{\alpha,\rho}}
{(1-z)^{\rho n+\delta_\rho+1}},
$$


where $\delta_1=0,\delta_2=124$. The numerator degrees are at most


$$
301,\qquad177.
$$



Thus the stated counts of $952$ contact residue slots and $960$ reconstructed residue slots are valid upper bounds.

## 6.3 Why the additional kernel pole is $123$

For


$$
Q_{\rho,\sigma}
=(1-x)^\rho(1-y)^\sigma-d(1+u)(u+xy),
$$


one has


$$
[d^n]\frac1{Q_{\rho,\sigma}}
=
\frac{((1+u)(u+xy))^n}
{(1-x)^{\rho(n+1)}(1-y)^{\sigma(n+1)}}.
$$



For the second branch, the needed reconstructed exponent is


$$
2n+124+1=2n+125.
$$


The marker denominator already contributes $2n+2$. The additional exponent must therefore be


$$
(2n+125)-(2n+2)=123.
$$



Thus A5’s kernel exponent $k_0-1=123$ is correct. Replacing it by $124$ would introduce a one-power error.

The first branch needs no additional pole because its exponent is $n+1$, exactly the marker contribution.

## 6.4 The squared-weight contraction preserves the cutoff

The identity


$$
[u^{n+2}](1+u)^{n+2}(u+xy)^{n+2}
=
\sum_j\binom{n+2}{j}^2(xy)^j
$$


glues the common weight index while leaving $x$ and $y$ independent.

The actual output is obtained from


$$
[x^by^bu^{n+2}]
\widehat G_f(x)\widehat G_\alpha(y)
(1+u)^{n+2}(u+xy)^{n+2}.
$$



For $j>b$, the coefficient required from the **complete** first-column series $\widehat G_f(x)$ has negative degree and vanishes. This enforces the original cutoff.

A single Laurent branch need not have that vanishing property. Accordingly, the branch cancellations must be performed before one interprets the expression as a truncated physical contraction.

After clearing the Laurent shifts, the full target is


$$
[x^{b+176}y^{b+176}u^{n+2}d^n].
$$


A numerator monomial $x^ry^s$ changes it to


$$
b+176-r,\qquad b+176-s
$$


in the two variables separately. Replacing those shifts by a function only of $r+s$ would be invalid.

## 6.5 The logarithmic qualification remains essential

At absolute precision $20$, the accepted bound


$$
K_{\rm norm}>20
$$


justifies omission of $h^F/b!$. Thus the construction represents the complete second column modulo $2^{20}$, not merely an arbitrary exponential surrogate.

At a greater precision, this omission must be rechecked. If the required depth exceeds $K_{\rm norm}$, the complete logarithmic contraction


$$
E_F=\sum_{i=0}^{b-1}w_i\,\frac{h_i^F}{b!}
$$


must be restored.

The accepted twenty-bit Schur inverse cannot be silently promoted to a higher-precision inverse.

---

# 7. Is A5’s proposed bounded numerator calculation valid?

**Yes, at the stated input and precision scope.**

It uses only:

- the accepted $76\times76$ Schur inverse;
- bounded band and exterior-load arrays;
- the complete $48$-entry first-force prefix;
- small-lower-index binomial coefficients;
- polynomial prefix operations and divided derivatives.

The four symbolic band applications have the stated first-branch lengths


$$
48,\ 76,\ 100,\ 76.
$$


The bound


$$
3003(48+76+100+76)=900900
$$


on uncollected first-branch contributions is correct. Collecting by derivative exponent and Laurent power prevents an unnecessary polynomial expansion per contribution.

The proposed independent reversed-prefix check through degree $151$ requires binomial lower indices no larger than $327$. At the stated original integers, exact streamed binomial arithmetic therefore uses bounded-size integers, not factorials of order $n$ or $b$.

Two qualifications prevent overclaiming:

1. The first $152$ reversed coefficients are a **finite corroboration** of the construction. They do not independently verify all $b$ contact coordinates. The all-coordinate conclusion comes from the algebraic derivation.

2. The numerator construction is not the weighted Gram calculation. The four-variable high coefficients remain unevaluated. General rational-series or Cartier existence results do not supply the missing practical extraction bound.

There is no hidden original-length work in constructing the short numerators **once the stated complete inputs are supplied**. The unclosed high-coefficient extraction is precisely where an original-scale cost could still remain.

---

# 8. A3 audit: what the large-prime hypotheses actually do

A3’s linear-defect restrictions are valid. The relevant definitions are


$$
H=b+(n-3)c-2(n-1)d,
$$




$$
B_0^\partial=6d-(n+6)c,
\qquad
B_3^\partial=2(n+2)d-(n+3)c,
$$


and


$$
P_n=n^2+5n+3.
$$



For $p>n+2$:

- the moments through $c_{n+2}$ are $p$-integral;
- $2,3,n+1,n+2$ are units;
- the vectors $v,w$ span an integral saturated rank-two module;
- their normal
  

$$
q_\partial=(n+2,-2(2n+3),2(n+2))^T
$$


  is primitive;
- the complete exponential contact vector divided by $n!$ is $p$-integral.

These are separate uses of the large-prime condition.

## 8.1 Backward primitivity is correctly proved

The raw coefficient recurrence has backward coefficient $1/2$. If


$$
p\mid b,c,d,
$$


it successively forces divisibility of every earlier raw coefficient, contradicting $c_0=1$. Hence


$$
\min\{v_p(b),v_p(c),v_p(d)\}=0.
$$



This does not transfer unchanged to small primes. For example, after factorial normalization $a_k=k!c_k$, the recurrence has backward coefficient


$$
\frac{k(k-1)}2.
$$


At primes dividing $k(k-1)$, backward propagation is no longer invertible.

Likewise, $p=n+2$, if prime, is not covered merely because $b,c,d$ themselves may be integral there: the endpoint vectors and $c_{n+2}$ introduce the denominator $n+2$.

No small unselected prime has disappeared from the global normalization.

---

# 9. New result: the actual third coordinate causes no large-prime primitive loss

Let $r_j$ be the primitive integer row proportional to $R_j$, and define


$$
m_j=\min\{v_p(r_jv),v_p(r_jw)\}.
$$


A3 writes


$$
v_p(\gamma_j)=m_j-\delta_j,
$$


where $\delta_j$ is the minimum valuation of all three actual outputs.

The following evaluates $\delta_j$ completely at the large primes.

## Theorem 9.1 — Exact specialized large-prime primitivization

On either original odd family, for every $p>n+2$,


$$
\boxed{\delta_0=\delta_3=0.}
$$


Consequently


$$
\boxed{
v_p(\gamma_j)=m_j,\qquad j=0,3.
}
$$



### Proof

If $m_j=0$, then one of the first two outputs is already a unit, so $\delta_j=0$.

Suppose $m_j>0$. Since $r_j$ is primitive and annihilates $v,w$ modulo $p$,


$$
r_j\equiv u q_\partial^T\pmod p
$$


for a unit $u$.

Retain the actual third-coordinate vectors


$$
s_3^{\exp}=\frac{\widehat w^{\exp}}{n!},
\qquad
s_0^{\exp}=\frac{\widehat w^{\exp}-T_0}{n!}.
$$


The terminal return gives the exact evaluations


$$
\boxed{
q_\partial^Ts_3^{\exp}=\frac{2F_n}{n!},
}
$$




$$
\boxed{
q_\partial^Ts_0^{\exp}
=\frac{2(n+1)(2d-c)}{n!},
}
$$


where


$$
F_n=d-c+\frac b2.
$$



For endpoint $3$, the defect congruences give


$$
\frac dc\equiv\frac{n+3}{2(n+2)},
\qquad
\frac bc\equiv\frac{3(n+1)}{n+2}\pmod p,
$$


with $c$ a unit. Therefore


$$
\frac{F_n}{c}\equiv\frac{n+1}{n+2}\pmod p,
$$


which is a unit.

For endpoint $0$, the defect congruences give


$$
\frac dc\equiv\frac{n+6}{6}\pmod p,
$$


again with $c$ a unit. Hence


$$
\frac{2d-c}{c}\equiv\frac{n+3}{3}\pmod p.
$$


The original $n$ is odd and at least $225$. Thus $n+3$ is even and every prime factor of $n+3$ is at most


$$
\frac{n+3}{2}<n+2.
$$


So $n+3$ is a unit at every $p>n+2$.

In both cases the actual third output $r_js_j^{\exp}$ is a unit. Therefore $\delta_j=0$. ∎

This conclusion depends on the evaluated original force. It would not follow for a freely chosen third coordinate. The endpoint-$0$ subtraction of $T_0$, which encodes the exterior $+1$, is indispensable.

---

# 10. New exact defect laws and a sharper common-content identity

## 10.1 Two explicit saturation exceptions

Define


$$
Q_0(n)=n^2+6n+4,
\qquad
Q_3(n)=n^2+4n+1.
$$



### Theorem 10.1 — Exact structural contents away from the saturation exceptions

For $p>n+2$,


$$
p\nmid Q_0(n)
\quad\Longrightarrow\quad
\boxed{
v_p(\gamma_0)=
\min\{v_p(H),v_p(B_0^\partial)\},
}
$$


and


$$
p\nmid Q_3(n)
\quad\Longrightarrow\quad
\boxed{
v_p(\gamma_3)=
\min\{v_p(H),v_p(B_3^\partial)\}.
}
$$



### Proof

The upper bounds are A3’s proved restrictions. If the relevant defect minimum is zero, equality follows immediately.

Suppose the minimum is positive. Then $c$ is a unit, and the actual moment state reduces to the displayed projective direction.

For endpoint $3$, use the kernel columns $T_0,T_1$. On its projective direction, their first two-coordinate minor is


$$
c^2-bd
=
-\frac{Q_3(n)}{2(n+2)^2}c^2
\pmod p.
$$


It is a unit when $p\nmid Q_3(n)$.

For endpoint $0$, use


$$
k_{0,1}=T_1+nT_0,
\qquad
k_{0,2}=T_2-n(n+1)T_0.
$$


On its projective direction, the corresponding minor is


$$
-\frac{n(n+3)Q_0(n)}{18}c^2
\pmod p.
$$


All factors other than $Q_0(n)$ are units at the primes under consideration.

Thus the two kernel columns form a saturated basis of the primitive row’s kernel. In such a basis, the content of the two normal defects $q_\partial^Tk_{j,\ell}$ equals the content of the two outputs $r_jv,r_jw$: both measure the content of the wedge of the two primitive normals.

A3’s evaluated defect transformations have unit determinants at $p>n+2$, so these normal-defect contents are precisely


$$
\min(v_p(H),v_p(B_j^\partial)).
$$


Theorem 9.1 then identifies them with $v_p(\gamma_j)$. ∎

At primes dividing $Q_j(n)$, the upper bound remains valid, but this reverse equality has not been established. A polynomially bounded exceptional **support** must not be confused with a bound for all possible valuation multiplicities there.

## 10.2 The common content is exact even without excluding those quadratics

Let


$$
D_{\rm mom}=2^n(n+2)!,
$$


and define the integer


$$
\boxed{
V_n=
\gcd\!\left(
|D_{\rm mom}H|,
|D_{\rm mom}B_0^\partial|,
|P_n|
\right)_{>n+2}.
}
$$



### Theorem 10.2 — Exact common structural content



$$
\boxed{
\gcd(\gamma_0,\gamma_3)_{>n+2}=V_n.
}
$$



### Proof

The identity


$$
(n+2)B_0^\partial-3B_3^\partial=-P_nc
$$


shows that if both defect gcds have positive valuation, then $c$ is a unit and


$$
\min\{v_p(H),v_p(B_0^\partial),v_p(B_3^\partial)\}
=
\min\{v_p(H),v_p(B_0^\partial),v_p(P_n)\}.
$$



Such a prime divides $P_n$. But


$$
Q_0-P_n=n+1,\qquad Q_3-P_n=-(n+2),
$$


while


$$
P_n=(n+1)(n+4)-1=(n+2)(n+3)-3.
$$


Therefore


$$
\gcd(P_n,Q_0)=1,\qquad \gcd(P_n,Q_3)\mid3.
$$


No prime $p>n+2$ dividing $P_n$ divides either saturation exception.

Theorem 10.1 therefore applies to both endpoints at every prime where a common defect can occur. Their common content is exactly the displayed minimum. Since $D_{\rm mom}$ is a unit at these primes, this is precisely $V_n$. ∎

## 10.3 Sharper product and imbalance bounds

Each $(\gamma_j)_{>n+2}$ divides $|D_{\rm mom}H|_{>n+2}$. Combining this with the exact common content gives


$$
\boxed{
(\gamma_0\gamma_3)_{>n+2}
\mid
|D_{\rm mom}H|_{>n+2}\,V_n.
}
$$


This is sharper than replacing $V_n$ by the whole factor $(P_n)_{>n+2}$.

For the structural imbalance,


$$
R_\gamma=\frac{\gamma_0\gamma_3}{\gcd(\gamma_0,\gamma_3)^2},
$$


one obtains


$$
\boxed{
(R_\gamma)_{>n+2}
\mid
\frac{|D_{\rm mom}H|_{>n+2}}{V_n}.
}
$$



These are exact divisor statements for the actual specialized triples. They do not yet give an $\exp(O(n))$ bound.

---

# 11. Nonvacuity of the linear moment factor

A3’s divisor statement is meaningful even when $H=0$, but then divisibility by its numerator is vacuous and no logarithmic size bound follows. The eventual nonvanishing can be supplied directly.

Put


$$
P(z)=1+z+\frac{z^2}{2},\qquad r=\sqrt2.
$$


Since


$$
(-1)^kc_k=[z^k]e^{-z}P(z)^n,
$$


the positive saddle satisfies


$$
\frac{rP'(r)}{P(r)}=1.
$$


Its variance is


$$
r\frac{d}{dr}\left(\frac{rP'(r)}{P(r)}\right)=2-\sqrt2.
$$



The standard one-saddle Cauchy-integral argument, with fixed shift $s$, gives


$$
c_{n+s}
=
(-1)^{n+s}
\frac{e^{-\sqrt2}(1+\sqrt2)^n(\sqrt2)^{-s}}
{\sqrt{2\pi n(2-\sqrt2)}}
\left(1+O(n^{-1})\right).
$$


The proof uses the strict inequality


$$
|P(re^{i\theta})|<P(r)\qquad(\theta\ne0)
$$


and the Gaussian expansion at $\theta=0$; the analytic amplitude $e^{-re^{i\theta}}$ is nonzero there.

Thus


$$
\frac bc=-\sqrt2+O(n^{-1}),
\qquad
\frac dc=-\frac1{\sqrt2}+O(n^{-1}),
$$


and


$$
\boxed{
\frac Hc=n(1+\sqrt2)+O(1).
}
$$


Therefore $H\ne0$ for all sufficiently large original indices.

This also recovers


$$
\frac{F_n}{c}=-(1+\sqrt2)+O(n^{-1}),
\qquad
\frac{2d-c}{c}=-(1+\sqrt2)+O(n^{-1}),
$$


consistent with the retained terminal nonvanishing.

Because $D_{\rm mom}$ clears the moments,


$$
\log|\operatorname{num}(H)|\le n\log n+O(n).
$$


This remains factorial-scale arithmetic control. The asymptotic does not bound the reduced numerator gcds by $\exp(O(n))$.

---

# 12. Complete forcing, guards, and primitive arithmetic remain unchanged

## 12.1 No terminal forcing is removed

For A3’s displacement recurrence, the forcing remains


$$
\psi_m=
\frac{(m+1)(m+2)E_m+2(m+2)G_m+E_{m+1}}
{(m+2)((m+1)!)^2}.
$$


All three terms remain. The complete displacement includes the logarithmic contribution


$$
\mathscr S_m=\omega_m+4.
$$


Nothing in the new structural-content proof changes the original force cutoff $2n+2$, the terminal return, or the common resultant currently being processed by the coordinator.

For the ternary return, retain


$$
\lambda_{i+\nu}
+\sum_{k=0}^{\nu-1}\bar f_k\lambda_{i+k}
=\bar b_i^{\langle26\rangle},
\qquad0\le i\le\nu-2,
$$


and


$$
J^T\varepsilon+\omega
=
-\varepsilon-s\bigl(\theta e_{\nu-1}
+3^{26}b^{\langle26\rangle}\bigr).
$$


Here $b^{\langle26\rangle}$ is the original complete forcing vector, including the retained leading extractions, lower poles, factorial force, and LOW subtraction. No moment beyond $D-4$ is added, and $\omega_{\nu-1}$ is not deleted.

## 12.2 Matrix protection is not endpoint protection

Even if A1’s content calculation eventually proves $s_c<32$, the strict directional guard remains


$$
v_3\!\left(e_c^TB_c^{-1}e_c-3^{26}d_c\right)
<6-2u_{\rm end}.
$$


Alternatively, the complete cofactor pair remains


$$
D_0=\det\Theta,
$$




$$
D_1=e_{\rm act}^T\operatorname{adj}(\Theta)e_{\rm act}
-3^{26}d_{\rm act}\det\Theta.
$$


The second term in $D_1$ cannot be discarded.

## 12.3 A5’s norm-relative precision is still unknown

If


$$
d_0=v_2(D_{\rm raw}),\qquad e_0=v_2(E_{\rm raw}),
$$


then precision $2^s$ for


$$
\frac HN=\frac{E_{\rm raw}}{2D_{\rm raw}}
$$


requires, sufficiently,


$$
M_E\ge s+d_0+1,\qquad
M_D\ge s+2d_0+1-e_0,
$$


as well as $M_E>e_0$, $M_D>d_0$.

A zero twenty-bit residue would establish only a lower bound on a valuation. It would not certify a primitive norm, a relative-output law, or a denominator valuation.

## 12.4 The all-prime final gcds are unchanged

The archived $n=225$ row contents remain


$$
(508500,\ 28350,\ 15525,\ 772).
$$


The least clearer is still taken over all eight reconstructed entries. None of the new large-prime identities replaces those row contents or their unselected-prime factors.

For endpoint weights, the actual primitive pair remains


$$
q_\lambda=\frac{kh|AB|}{F_{\rm gcd}GH_{\rm gcd}},
\qquad
p_\lambda=
\operatorname{sgn}(AB)\frac{T}{F_{\rm gcd}GH_{\rm gcd}},
$$


with all three gcd factors retained at every prime. Its whole error is


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda e_3\alpha_{n,2}(\lambda-\Lambda_{n,2}).
}
$$



For the ternary determinant route,


$$
g_\ell=\gcd(|A_\ell|,|B_\ell|),\qquad
q=\frac{|B_\ell|}{g_\ell},
$$


and


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
{g_\ell}\det H_{\rm complete}.
}
$$



For A5’s weighted route,


$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=\frac{A_B}{g_B},\qquad
p_n=\frac{H_B}{g_B},
$$


and


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n.
}
$$



These are the actual primitive denominators and the whole same-index errors. Local content restrictions do not by themselves prove their nonvanishing and decay.

---

# 13. New bounded arithmetic warranted by this audit

No accepted calculation needs to be rerun.

## 13.1 A5 short-numerator construction

This is the substantive new bounded calculation still warranted.

### Inputs

- the exact original $b,n$;
- modulus $2^{20}$, $m=76$;
- the accepted $\lambda_s,c_s,\overline K,S^{-1}$;
- the complete actual $f_0,\ldots,f_{47}$;
- $v_t=(b+t)!/b!$, $0\le t\le23$.

### Required output

1. The four complete contact numerator lists, with degree bounds $299,175$.
2. The four reconstructed numerator lists, with degree bounds $301,177$.
3. The two new endpoint right-hand sides and their products with the supplied inverse.
4. Zero residuals for the prescribed $152$-coefficient reversed-prefix comparisons.
5. Zero residuals for every principal-part identity:
   

$$
P_{<0}G_f=0,\qquad P_{<0}G_e^*=B_v.
$$


6. The signed exterior-endpoint identity
   

$$
[z^0]\widehat G_e=-b[z^0]G_e^{\rm an}-1.
$$


7. The four kernel records with additional pole exponent $123$ and the full target
   

$$
[x^{b+176}y^{b+176}u^{n+2}d^n].
$$



Unless the high coefficients are actually extracted, the receipt must continue to state that the original weighted Gram pair has not been computed.

## 13.2 Small symbolic verification of the new A3 identities

No new producer is needed. A bounded rational-polynomial check may verify:

- the two terminal normal evaluations in Theorem 9.1;
- the two specialized kernel minors in Theorem 10.1;
- the polynomial relations
  

$$
Q_0-P_n=n+1,\qquad Q_3-P_n=-(n+2);
$$


- the two divisions
  

$$
P_n=(n+1)(n+4)-1=(n+2)(n+3)-3.
$$



The inputs are symbolic $n,b,c,d$, with A3’s formulas for $c_{n-2}$ and $c_{n+2}$, followed by the two projective substitutions. The expected output is an exact zero numerator for each residual.

This would corroborate the fixed algebra only. It would not evaluate an original-family gcd or replace the coordinator’s separate $\mathcal B,\mathcal F$ post-processing.

---

# 14. Final proof-status ledger

| Statement | Status after this audit |
|---|---|
| A1 exact pure-Jacobi/factorial comparison | Proved at the original cutoff |
| A1 inverse-loss stability | Proved under $\lambda(G_J)<h$ |
| Full loss equals Schur loss on the retained depth-$26$ branch | Proved using both corrected sides |
| Deep resonance forces $j\equiv81\pmod{243}$ | Proved for $t\ge6$ |
| Deep resonance intersects the current $C_{16}$ window with $\log j=O(t)$ | Proved using a fixed-logarithm quantitative rotation bound |
| Unit normalizer on that infinite current-window subfamily | Recovered from the retained continuation |
| Unit normalizer on every current-window index | Not proved |
| Eight-state Jacobi content evaluator | Valid, with the stated terminating half-integral tails |
| Whole Bézout pivot-content identity | Proved |
| Collision-branch content at threshold $h-33$ | Open |
| A5 complete exterior-load and signed-reversal construction | Valid at the stated precision and boundary |
| A5 $123$-pole four-variable contraction | Valid |
| Bounded construction of the short numerators | Valid specification; not executed |
| Original weighted norm and mixed output | Unevaluated |
| Actual A3 large-prime triple loss $\delta_j=0$ | **Proved here** |
| Exact A3 defect contents away from $Q_0,Q_3$ | **Proved here** |
| Exact common structural content and sharpened imbalance divisor | **Proved here** |
| Eventual nonvanishing of the shared linear moment $H$ | **Proved here** |
| Exponential all-prime content/denominator control | Open |
| Infinitely many nonzero primitive whole errors tending to zero | Open |

## Conclusion

The main new arithmetic result is that the complete original terminal force makes the third coordinate locally primitive at every prime $p>n+2$, and this permits an exact common-content law:


$$
\boxed{
\gcd(\gamma_0,\gamma_3)_{>n+2}
=
\gcd\!\left(
|D_{\rm mom}H|,
|D_{\rm mom}B_0^\partial|,
|n^2+5n+3|
\right)_{>n+2}.
}
$$


In particular,


$$
\boxed{
(R_\gamma)_{>n+2}
\mid
\frac{|D_{\rm mom}H|_{>n+2}}
{\gcd(|D_{\rm mom}H|,|D_{\rm mom}B_0^\partial|,|P_n|)_{>n+2}}.
}
$$



The main scope correction is that the old deep-resonance continuation does apply on an infinite subfamily of the present $C_{16}$ window, without assuming endpoint units. The main computational validation is that A5’s new short-numerator construction is genuinely bounded, while its complete high-coefficient contraction remains unevaluated.

The exact remaining bottlenecks are:

1. the whole Jacobi collision content and subsequent endpoint guard;
2. practical norm-sensitive extraction of A5’s four-variable complete outputs;
3. arithmetic control of the evaluated complete-force resultant and all omitted small-prime content;
4. the final all-prime primitive denominator against the same-index whole nonzero error.



$$
\boxed{
\text{No unconditional proof or disproof of the irrationality of }e+\pi
\text{ has been obtained.}
}
$$


