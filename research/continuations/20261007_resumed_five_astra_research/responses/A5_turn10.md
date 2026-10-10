> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of Family005 and an exact compact $e+\pi$ transfer

## 1. Findings and proof status

I reviewed all the mathematical sections supplied for Family005: foundations, odd-prime arithmetic, prime-index nonvanishing, real-place interpolation, energy reduction, the numerical certificate, and the concluding comparison. I did not treat the bibliography, provenance, or existence of supplementary programs as verification of a mathematical claim.

The findings are:

1. **The structural proof is coherent at the level checked here.** In particular, the Taylor cancellation, the distinction between the two odd-prime denominator layers, the auxiliary successor row in prime-index nonvanishing, the Hardy-space determinant cancellation, and the matched damping argument fit together with their stated boundaries.
2. **The fixed modular and real-value certificates have not been reproduced in this response.** Their recipes are bounded and exact. Thus my conclusion about the claimed Catalan theorem is conditional on those finite certificates, not an unconditional endorsement of their tabulated outputs.
3. **The manuscript does not transfer directly to the original binary approximation family.** Its local column operations bound determinant denominators; they do not establish paid binary acceptance, scalar norm nonisotropy, an ALL-prime final gcd, or the actual primitive denominator of that family.
4. **A new exact transfer is proved below:** a specific $2\times2$ compact mixed-moment determinant whose entries have exactly equal $e$- and $\pi$-coefficients, and whose determinant is an explicitly evaluated, nonzero rational linear form in $e+\pi$. This is a genuine finite construction, not an irrationality proof.
5. **A quantitative obstruction is also proved:** the exponential endpoint-coefficient functional has factorial norm growth even on monomials bounded by one on $[0,1]$. Consequently a compact integral representation does not make the contact arithmetic inexpensive.

The global question of the rationality or irrationality of $e+\pi$ remains unresolved.

---

## 2. Reconstruction of the Family005 argument

### 2.1 Original parameters, rows, and contact range

For this section only, the manuscript’s parameters are


$$
n=48N,\quad a=11N,\quad b=7N,\quad q=g=4N,\quad h=2N,
$$




$$
L=59N,\qquad C=63N,\qquad H=65N,\qquad A=19N.
$$


These are not the parameters of the binary $e+\pi$ family.

With


$$
f=\sqrt{1-t^2},\qquad w=\frac{t}{1+f},
$$


the involution $w\mapsto w^{-1}$ fixes $t$ and negates $f$. The rows are


$$
R_r=(1-t)^h t^{C-1}w^{r-g},\quad
P_r=\frac{R_r+R_r^*}{2},\quad
D_r=\frac{t(R_r^*-R_r)}{2f},
\qquad 0\le r<n.
$$


The Chebyshev formulas give integer polynomials


$$
P_r=(1-t)^h t^{C-1}T_{|r-g|}(1/t),
$$




$$
D_r=\operatorname{sgn}(r-g)(1-t)^h
t^{C-1}U_{|r-g|-1}(1/t).
$$


Their lower and upper degree bounds are


$$
\operatorname{supp}P_r\subseteq[A,H-1],\qquad
\operatorname{supp}D_r\subseteq[A+1,H-1].
$$



The decisive identity is exact:


$$
\frac{tP_r}{f}-D_r=\frac{tR_r}{f}.
$$


Since $w=t/2+O(t^3)$, its order at zero is at least


$$
C+r-g\ge C-g=L.
$$


Thus cancellation holds for every raw column $b\le j<L$, including all raw columns used by the prescribed filter


$$
s^{b+k}(1-s)^q,\qquad 0\le k<n.
$$


There is no missing upper filtered column.

### 2.2 Moment rationality and cancellation

The two kernels are


$$
M(i,j)=\int_{-1}^{1}\int_0^1
\frac{|t|}{f(t)}\frac{t^i s^j}{1-ts}\,ds\,dt,
$$




$$
Z(i,j)=\int_0^1\int_0^1\frac{t^i s^j}{1-ts}\,ds\,dt.
$$


The logarithmic endpoint singularity after integrating in $s$ is integrable against $dt/\sqrt{1-t^2}$. Hence the geometric-series and finite polynomial manipulations are justified by absolute integrability.

Writing


$$
c_l=4^{-l}\binom{2l}{l},
$$


the elementary moments satisfy


$$
m_{2l}=\frac{2}{(2l+1)c_l},\qquad m_{2l+1}=0.
$$


The boundary starts are


$$
M(0,0)=4G,\qquad M(0,1)=\frac32\zeta(2).
$$


The stated recurrences propagate these starts to


$$
M(i,j)=M^0(i,j)+4G\,c_{(i-j)/2}
+\frac32\zeta(2)c_{(j-i-1)/2},
$$


where an inadmissible $c$-index means zero. Also


$$
Z(i,j)=Z^0(i,j)+[i=j]\zeta(2).
$$



Consequently the coefficient of $\zeta(2)$ in


$$
F_j(r)=M(P_r,j)-\frac32Z(D_r,j)
$$


is


$$
\frac32[t^j]\left(\frac{tP_r}{f}-D_r\right)=0
\qquad(j<L).
$$


Thus


$$
F_j(r)\in\mathbb Q+\mathbb QG.
$$



This is an entrywise cancellation, not merely a cancellation after taking the determinant. That distinction is essential for a prospective $e+\pi$ transfer.

### 2.3 The estimate at two

The manuscript does not identify its real moment series with a $2$-adic series without correction. It introduces a separately convergent $2$-adic series


$$
M_{\rm s}(i,j)=\sum_{k\ge0}\frac{m_{i+k}}{j+k+1}
$$


and retains two homogeneous discrepancies $e_1,e_2$.

For even $u$,


$$
v_2(m_u)\ge u+1-\log_2(u+1),
$$


so convergence and the uniform lower bound for the smoothed columns follow. The original raw columns are then decomposed into:

- smoothed columns;
- $e_1$-columns expanded in fixed $P$-coefficient vectors;
- $e_2$ and rational-$Z$ columns expanded in fixed $D$-coefficient vectors.

Alternation forces distinct expansion indices within each coefficient-vector family. It does **not** force distinctness across the two families; the proof correctly avoids that assertion.

If the numbers of the two exceptional column types are $m,l$, the resulting quadratic lower bound is


$$
-(H-b)m+\frac32m^2+\frac12l^2+C(n-m-l)
-O_G(n\log n).
$$


Minimization first gives $l=n-m$, then


$$
v_2(\Delta_N)\ge
-\frac{505}{4608}n^2-O_G(n\log n).
$$


The proof also applies to every full raw minor, which is exactly what is needed to pass through the integer filter.

### 2.4 First odd-prime layer: $p^{-2}$

For


$$
2\sqrt H<p\le H,
$$


excluding fixed denominator primes of the hypothetical rational $G$, the digit reductions establish local integrality after multiplication by $p^2$:


$$
p^2M^0(i,j)\equiv E_dM^0(i',j')\pmod p,
$$


and the corresponding residue-matched reduction for $Z^0$.

Important boundary details are present:

- $i'$ may equal $-1$;
- $M^0(-1,j')=k^+_{j'+1}$ is an algebraic convention, not an integral;
- extraction for $P$ uses $tPE$ and the shift $(u+1)p+\ell$;
- extraction for $D$ uses $up+\ell$.

The explicit $H_z^*$-formulas justify both integrality and the reductions. In the even minus-boundary calculation, the complete blocks ending at even multiples of $p$ are essential; the proof accounts for them rather than replacing them by a partial block.

For appropriate residues,


$$
X_\ell=V_\ell,\qquad X_{p+\ell}=U_\ell-V_\ell,
\quad X_j=p^2F_j\bmod p.
$$


The support bound gives $U_\ell=0$ for $\ell\le A$. Pairing a low column with its high partner therefore improves the pair sum from $p^{-2}$ to $p^{-1}$.

This is only a one-power improvement. The manuscript does not incorrectly call those sums integral.

### 2.5 Second odd-prime layer: $p^{-1}$

For $p>H/2$, put


$$
K=L-p,\qquad J=H-p.
$$


For central columns,


$$
b\le j<\min(p,L),\qquad j\ge J,
$$


the next residue is


$$
pF_j\equiv-\sum_{0\le\ell<J}\frac{V_\ell}{j-\ell}\pmod p.
$$


All denominators $j-\ell$ are units at $p$.

Retained noncentral columns supply representatives $Y_\ell$ with


$$
p^2Y_\ell\equiv \pm V_\ell.
$$


Adding $p$ times such columns to a central column cancels its $p^{-1}$-residue. The unknown next coefficient of $Y_\ell$ becomes integral after that multiplication, so no unproved second-digit cancellation is required.

The only unrepresented residues lie in


$$
\max(0,K)\le\ell<\min(b,J).
$$


After a further invertible local column change, the pool contains:

- $R$ columns with possible loss two;
- at most $S$ additional columns with possible loss one;
- integral remaining columns.

Therefore


$$
v_p(\Delta_N)\ge-\min(2n,n+R,2R+S).
$$



This is a valid two-layer argument. Leading-residue rank alone would not have proved it.

### 2.6 ALL-prime determinant lower bound

The piecewise loss function has area


$$
\int_0^{65}d(x)\,dx=\frac{8609}{2}.
$$


The small odd primes contribute $o(n^2)$; primes above $H$, once fixed denominator primes are below $H$, contribute no negative valuation. The weighted prime number theorem then gives


$$
\sum_{p\text{ odd}}v_p(\Delta_N)\log p
\ge-\frac{8609}{4608}n^2-o(n^2).
$$



For a **nonzero rational** determinant,


$$
\log|\Delta_N|=\sum_pv_p(\Delta_N)\log p.
$$


Combining all primes yields


$$
\liminf\left(\frac{\log|\Delta_N|}{n^2}-\frac12\log2\right)
\ge-\frac{8609}{4608}-\frac{2809}{4608}\log2
>-2.29084.
$$



This is an ALL-prime estimate for the manuscript’s rational determinant. It is not an ALL-prime gcd estimate for the binary scalar construction.

---

## 3. Prime-index nonvanishing

Set $N=p$. The palindromic polynomial space has two triangular bases, whose transition matrix $\mathbf a$ has


$$
\det\mathbf a=2^{-p(p-1)/2}\ne0\quad\text{in }\mathbb F_p.
$$


The companion transition is


$$
\mathbf b=\mathbf a\Pi,
$$


where $\Pi$ fixes no nonzero residue individually but pairs $i$ with $p-i$, and kills $e_0$.

Frobenius decomposes every original row $r=pr_0+i$ into a base row $r_0$ and one successor row $r_0+1$. The last successor is row $48$, not row $47$. Its degree-$18$ term in $P$ and degree-$19$ term in $D$ must be retained. The supplied proof retains them and verifies that their extraction begins at the correct original degree $20p-i$.

After the residue-preserving filter, the scaled matrix reduces to


$$
\mathcal L_p=\mathbf a^T\otimes\mathcal B_0+
\mathbf b^T\otimes\mathcal B_1.
$$


Right multiplication by $(\mathbf a^T)^{-1}\otimes I$ gives


$$
I\otimes\mathcal B_0+\Pi^T\otimes\mathcal B_1.
$$


The eigenvalues of $\Pi^T$ are $0,1,-1$, with multiplicities


$$
1,\quad (p-1)/2,\quad(p-1)/2.
$$


Hence


$$
\det\mathcal L_p=(\det\mathbf a)^{48}
\det\mathcal B_0
\det(\mathcal B_0+\mathcal B_1)^{(p-1)/2}
\det(\mathcal B_0-\mathcal B_1)^{(p-1)/2}.
$$



**Checked implication.** If the three fixed rational determinants are nonzero, then under $G\in\mathbb Q$,


$$
v_p(\Delta_p)=-96p
$$


for every sufficiently large prime $p$.

**Unreproduced finite premise.** The displayed elimination tables modulo $101$ are intended to prove those three fixed nonvanishing assertions. I checked that the recipes have only unit scalar denominators modulo $101$, but did not independently reproduce the 144 pivots.

---

## 4. Real-place interpolation and uniform energy

### 4.1 The signed two-sheet structure

The real integral has one $t$-Vandermonde and two $s$-Vandermondes. Its sheet coefficients are


$$
(\xi_{\rm f},\xi_{\rm n})=
(1/2,1/2)\quad(x<0),\qquad
(-1/4,5/4)\quad(x>0).
$$


Thus the positive half-interval is genuinely signed. Positivity cannot supply nonvanishing.

Factoring the far sheet produces mixed evaluations


$$
x_i^{n-1-r}+h_*(x_i)x_i^r,
\qquad
h_*(x_i)=c_ix_i^{D_*},
$$


with $c_i=1$ or $-5$.

### 4.2 Uniform interpolation

Under


$$
\sum_i\frac{1-x_i^2}{1+x_i^2}\le D_*,
$$


the Blaschke-product estimate on the imaginary diameter bounds


$$
F(z)=z^{D_*}/B(z).
$$


The Cauchy integral gluing has the correct jump: left minus right is $6F$, matching $1-(-5)=6$.

The contour deformations occur only near $\pm i$, away from the real poles. They preserve the fixed integral and yield


$$
\|h_*\|_\infty\le10e^{12}n.
$$


No node-separation lower bound is introduced.

### 4.3 Hardy-space determinant cancellation

In


$$
\mathcal H_Q=\{v/Q:\deg v<n\},
\qquad Q(z)=\prod_i(1-x_i z),
$$


the reversal


$$
R(v/Q)=z^{n-1}v(1/z)/Q
$$


is a complex-linear isometry. This follows by changing $\theta$ to $-\theta$ in the circle integral and using the real coefficients of $Q$.

Projection to $\mathcal H_Q$ preserves evaluations at the nodes because the reproducing kernels $1/(1-x_i z)$ belong to that space. Thus the mixed evaluation determinant factors algebraically as


$$
\det(E)\det(L)\det(R),
\qquad L=I+JR.
$$


Since $\det E=V(x)$,


$$
\frac{|\det(\text{mixed evaluations})|}{|V(x)|}
\le(1+10e^{12}n)^n.
$$


No inverse-Vandermonde norm is used.

The complementary Hadamard bound correctly retains


$$
2^{-\binom n2};
$$


this is a principal $n^2$-scale contribution, not a negligible prefactor.

### 4.4 Matched damping and endpoint corrections

The damping factors


$$
\tau=1-\varepsilon,\quad
\rho(x)=1-\varepsilon(1-x),\quad
\sigma(s)=1-\varepsilon\sqrt{1-s}
$$


are used consistently in pure and cross interactions. They produce the exact negative squares


$$
-\kappa\sum_{k\ge1}\frac{A_k^2}{k},
\qquad
-\frac12\sum_{k\ge1}\frac{(B_k-2C_k)^2}{k}.
$$



The cross comparison has the needed upper-bound direction:


$$
-\log|z|^2
\le-\log|z_\varepsilon|^2+6\varepsilon.
$$


The opposite-sign power interaction is also treated explicitly.

The omitted diagonals cost endpoint terms


$$
-\frac1{2n}\langle\log(1-x)\rangle,\qquad
-\frac1n\langle\log(1-s)\rangle,
$$


in addition to bounded $O_\varepsilon(1/n)$ terms. They are not discarded before taking a supremum. The surviving positive endpoint coefficients force maximizers into common compact subsets. Taking $n\to\infty$ first and $\varepsilon\downarrow0$ second is therefore justified.

I found no analytic obstruction in this part of the supplied proof.

---

## 5. What the finite real certificate proves—if reproduced

The certificate supplies four rational derivative numerators of degrees


$$
36,\quad24,\quad13,\quad9.
$$


Its logic is sound:

1. Descartes transforms bound roots in each partition interval.
2. The listed sign-changing brackets provide the same number of roots.
3. Equality exhausts the roots and makes them simple.
4. Finite division points are evaluated separately.
5. Singular endpoints have limit $-\infty$.
6. The whole-bracket derivative bound converts point values into bounds at stationary points.

There are 43 root brackets and seven additional finite evaluation points. The displacement allowance is


$$
120000\cdot2\cdot10^{-10}=0.000024
$$


per supremum.

The logarithm and argument approximations use rational series with explicit remainder bounds. Complex logarithm branches are handled correctly through the factorization and principal-argument convention.

**Distinction:** I verified the method and its error propagation, not the tabulated exact sign variations, bracket signs, or fifty rational value outputs.

Conditional on their reproduction, the resulting real upper bound is


$$
\limsup\left(\frac{\log|\Delta_N|}{n^2}-\frac12\log2\right)
\le-2.290939875.
$$


Together with the fixed-matrix certificate, this contradicts the finite-place lower bound under $G\in\mathbb Q$.

Thus the remaining verification identified here is finite and specific. It is not an invitation to infer a theorem from official provenance.

---

## 6. A new exact compact determinant for $e+\pi$

The following construction tests the essential transfer requirement directly: the separate $e$- and $\pi$-coefficients match in every entry.

### 6.1 Exact exponential and arctangent functionals

For a polynomial $P$, repeated integration by parts gives


$$
\int_0^1e^tP(t)\,dt
=e\,\mathcal A(P)-\mathcal B(P),
$$


where


$$
\mathcal A(P)=\sum_{j=0}^{\deg P}(-1)^jP^{(j)}(1),
\qquad
\mathcal B(P)=\sum_{j=0}^{\deg P}(-1)^jP^{(j)}(0).
$$



Define


$$
a_m=\mathcal A(t^m).
$$


Then


$$
a_0=1,\qquad a_m=1-ma_{m-1},
$$


and


$$
a_m=(-1)^m m!\sum_{j=0}^m\frac{(-1)^j}{j!}.
$$


The even values needed below are


$$
a_0=1,\quad a_2=1,\quad a_4=9,\quad
a_6=265,\quad a_8=14833.
$$



For even powers,


$$
4\int_0^1\frac{t^{2k}}{1+t^2}\,dt
=(-1)^k\pi+
4\sum_{\ell=0}^{k-1}\frac{(-1)^\ell}{2k-1-2\ell}.
$$



For an even polynomial $P$, the coefficient of $\pi$ in
$4\int P/(1+t^2)$ is $P(i)$. Therefore the compact mixed moment


$$
\int_0^1\left(e^t+\frac4{1+t^2}\right)P(t)t^{2j}\,dt
$$


has matching period coefficients precisely when


$$
\boxed{\mathcal A(t^{2j}P)=(-1)^jP(i).}
$$



This is the exact contact condition for this construction.

### 6.2 Two explicit contact rows

Take


$$
P_0(t)=t^4-4t^2-117,
\qquad
P_1(t)=t^6-133t^2-6884.
$$


For $j=0,1$, direct substitution gives


$$
\begin{array}{c|cc}
&j=0&j=1\\ \hline
\mathcal A(t^{2j}P_0)&-112&112\\
(-1)^jP_0(i)&-112&112\\
\mathcal A(t^{2j}P_1)&-6752&6752\\
(-1)^jP_1(i)&-6752&6752.
\end{array}
$$


Thus matching is exact in all four entries.

Let $s=e+\pi$, and define


$$
\mathcal D=
\det_{0\le r,j<2}
\left[
\int_0^1
\left(e^t+\frac4{1+t^2}\right)
P_r(t)t^{2j}\,dt
\right].
$$



The rational parts of the first five even moments are


$$
-1,\quad2,\quad-\frac{80}{3},\quad
-\frac{10748}{15},\quad-\frac{4233904}{105}.
$$


Consequently the matrix is exactly


$$
\begin{pmatrix}
-112s+\frac{247}{3}&
112s-\frac{12658}{15}\\[2mm]
-6752s+\frac{88522}{15}&
6752s-\frac{1769048}{35}
\end{pmatrix}.
$$


Its quadratic term cancels, and expansion gives


$$
\boxed{
\mathcal D=
\frac{1289257492-223466880(e+\pi)}{1575}.
}
$$



This is a fully evaluated compact determinant, not a named unevaluated integral.

### 6.3 Unconditional nonvanishing

The rational zero of this linear form is less than $29/5$, because


$$
1289257492
<
\frac{29}{5}\,223466880
=1296107904.
$$


Meanwhile


$$
e>\sum_{j=0}^{4}\frac1{j!}=\frac{65}{24}.
$$


Using


$$
\frac\pi4=\arctan(1/2)+\arctan(1/3)
$$


and $\arctan x>x-x^3/3$ for $0<x<1$,


$$
\pi>
4\left(\frac12-\frac1{24}+\frac13-\frac1{81}\right)
=\frac{505}{162}.
$$


These lower bounds imply $e+\pi>29/5$. Therefore


$$
\mathcal D<0.
$$



**New proved result.** The displayed compact mixed determinant is nonzero, and every one of its entries belongs to $\mathbb Q+\mathbb Q(e+\pi)$ by exact coefficient matching.

Its associated integer form is


$$
1575\mathcal D
=1289257492-223466880(e+\pi)\ne0.
$$


The numerator and coefficient have gcd $4$, so the primitive integer form is


$$
322314373-55866720(e+\pi)\ne0.
$$


This is one finite linear form. There is no claim that it is small enough, or belongs to an infinite useful sequence.

---

## 7. The factorial transfer barrier

The compactness of the preceding integral does not bound the arithmetic of $\mathcal A$.

For every even $m\ge2$, the alternating-series estimate gives


$$
\frac13<
\sum_{j=0}^{m}\frac{(-1)^j}{j!}
\le\frac12.
$$


Hence


$$
\frac{m!}{3}<a_m\le\frac{m!}{2}.
$$


Yet $\|t^m\|_{\infty,[0,1]}=1$. Therefore the norm of $\mathcal A$ on degree-$m$ polynomials equipped with the supremum norm is at least $m!/3$.

By contrast, the $\pi$-coefficient of $t^{2k}$ is merely $(-1)^k$. Thus period matching compares a factorial-size functional with a bounded oscillatory one.

For degree $m$, the arithmetic scale is


$$
\log(m!)=m\log m-m+O(\log m).
$$


If an $n$-row extension uses degree proportional to $n$, a naive rowwise payment can produce an $n^2\log n$ determinant-height cost. Such a cost cannot be absorbed by a fixed negative $n^2$-scale energy constant.

This is a barrier to a naive extension, not a proof that every extension fails. Correlated contact cancellation could reduce the cost, but that requires proof.

A concrete follow-on obligation is:

> Construct an infinite family of exact-contact rows for the compact mixed functional above, with controlled integer lattice height, nonzero determinants, and a real bound that survives the actual arithmetic payment.

The finite determinant proves compatibility and nonvanishing at one size. It does not establish that obligation.

---

## 8. Consequences for the original binary family

The original binary indices remain


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
$$


Contact is $0,\ldots,b-1$; physical reconstruction is $0,\ldots,b$, with $z_b=0$. The complete columns remain


$$
x=\frac12RA^{-1}f,\qquad
y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},
\qquad x=2^a x_0.
$$


No part of the new compact construction is identified with these columns.

The accepted facts retained here include $a\ge1$, source integrality, boundary completion, and the stated finite inverse information. The scalar acceptance is still


$$
S=\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f,
\qquad S/2^{a+1}\in\mathbb Z.
$$



If the full-return theorem under review is accepted, it supplies


$$
v_2(S)\ge1+\chi,\qquad
\chi=v_2\binom{n+b-1}{b-1}.
$$


After payment, this would give only


$$
v_2\!\left(S/2^{a+1}\right)\ge\chi-a.
$$


The subtraction of $a$ is indispensable.

I reuse, without recomputation, the supplied finite facts:

- at $u=0$, $\chi=27$;
- the sufficient endpoint upper bound is $21$;
- the resulting certified excess is $6$;
- the 2800 finite tail-convolution cases have been settled.

They establish neither positive paid excess on an infinite original index set nor an ALL-prime final gcd bound.

The actual column contents, least simultaneous clearer, scalar norm


$$
Q=x_0^Tx_0,
$$


final gcd and primitive denominator must still be tracked. In particular, the known original denominator valuation


$$
v_3(q)=n-\frac{b+15}{2}
$$


remains in force. Neither the Family005 determinant estimates nor the new finite compact determinant removes it.

The supplied scope does not include complete formulas for that final gcd and primitive numerator/denominator. I therefore do not substitute a guessed quotient for them.

---

## 9. Bounded exact verification tasks

No computation was performed here.

### 9.1 Family005 fixed matrices

**Inputs:** the stated arrays on $0\le i\le64$, $0\le j\le58$; rows $0,\ldots,48$, including all auxiliary-row terms; modulus $101$.

**Output:** the three exact pivot lists and swap records for


$$
\mathcal B_0,\qquad\mathcal B_0+\mathcal B_1,\qquad
\mathcal B_0-\mathcal B_1.
$$


Agreement establishes these three fixed rational nonvanishing assertions. The proved Frobenius argument—not the finite computation by itself—then supplies eventual prime-index nonvanishing.

### 9.2 Family005 real certificate

**Inputs:** the supplied rational trial coefficients, the four derivative numerators, the partition points, 43 brackets, and fifty evaluation points.

**Output:**

- degrees $36,24,13,9$;
- all stated Descartes variation counts;
- strict sign changes at every bracket;
- outward rational bounds meeting the coarse cutoffs;
- the stated norm bounds.

These outputs validate the finite premises of the global-supremum argument.

### 9.3 New compact determinant

An optional small independent check has inputs only


$$
P_0=t^4-4t^2-117,\qquad P_1=t^6-133t^2-6884,
$$


and the five even moments through degree eight.

Expected output:


$$
\mathcal D=
\frac{1289257492-223466880(e+\pi)}{1575},
$$


with matching period coefficients in every entry and primitive coefficient pair


$$
(322314373,\ 55866720).
$$


The derivation above already proves this identity.

---

## 10. Final conclusion

The Family005 manuscript presents a structurally coherent conditional proof package: its infinite reductions connect the exact finite certificates to the claimed contradiction. I found no precise structural gap in the supplied mathematical arguments, but I have not reproduced the finite modular and real-value tables and therefore do not certify the headline theorem unconditionally here.

The new result is an explicit, nonzero compact determinant for $e+\pi$, with exact entrywise period matching and fully evaluated primitive integer linear form. Its finite scope is explicit.

The remaining $e+\pi$ bottleneck is unchanged in its essential form: one needs integer approximants at **one and the same infinite set of original indices**, with the actual primitive denominator after all contents, clearers, paid divisions, and the ALL-prime gcd, together with


$$
0<|q_n(e+\pi)-p_n|\longrightarrow0.
$$


The present work supplies neither that infinite arithmetic statement nor a compatible infinite compact replacement. It does supply a checked finite transfer and an explicit factorial obstruction that any such replacement must overcome.
