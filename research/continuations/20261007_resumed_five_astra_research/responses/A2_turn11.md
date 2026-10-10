> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Research report: audit of Family005 and an exact factorial-contact construction for $e+\pi$

## 1. Executive summary and proof status

This report has two distinct parts.

1. **Audit of the complete supplied Family005 manuscript.**  
   I reconstructed its rational moment decomposition, Taylor cancellation, the estimate at $2$, both odd-prime denominator layers, prime-index Frobenius reduction, bounded Hardy-space interpolation, and the uniform energy argument. **I did not find a structural proof gap in those displayed arguments.** The proposed conclusion about Catalan’s constant still depends on independently checking two explicit finite certificates:
   - the three fixed $48\times48$ matrices modulo $101$;
   - the rational root-count and value certificate for the real-place barriers.

   No computation was performed here. In particular, the supplied pivot and barrier tables are not being treated as verified merely because they appear in the manuscript.

2. **A concrete transfer test for $e+\pi$.**  
   I give an explicit compact mixed moment matrix whose entries lie in
   

$$
\mathbb Q+\mathbb Q(e+\pi).
$$


   The coefficients of $e$ and $\pi$ match **exactly**. The exponential channel is retained through its genuine factorial charge functional, not replaced by Catalan’s algebraic density.

   For this new construction I prove:
   - exact factorial Taylor contact;
   - explicit rational entries and integer payments;
   - the exact least clearer for the full contact array;
   - exact small-prime row and column contents, including the prime $29$;
   - a uniform real determinant bound obtained by finite row differences;
   - a nonzero whole-error obstruction showing that the most immediate scalar extracted from the construction cannot prove irrationality.

   The construction does **not** presently prove irrationality of $e+\pi$. Its outstanding determinant nonvanishing and final ALL-prime scalar-gcd estimates are stated precisely below.

The global research objective therefore remains unresolved: **this report proves neither rationality nor irrationality of $e+\pi$.**

---

## 2. Scope and index lock

In the Family005 audit, the symbols $n,a,b,q,g,h$ have the manuscript’s meanings. In the transfer section they are reset explicitly.

For the original A2 stream, I retain the supplied indices


$$
b=3^{249005515+574312172u},\qquad
n=2001b,\qquad
u\equiv2\pmod{29^9},
\tag{2.1}
$$


with $u$ restricted to the original allowed integer domain. No passage to arbitrary $n$, arbitrary primes as original indices, or a different approximation family is used to claim an A2 gain.

The accepted logarithmic charge determinant is reused at its stated normalization:


$$
\det C_{\log,n}
=-\frac{2^{n+1}(n!)^2}{b!}.
\tag{2.2}
$$


Its proof is not reopened.

The supplied material does not include explicit formulas for the complete A2 exponential residue, all original corrected columns, or the auxiliary scalar clearer. Consequently, the new matrix below is **not identified with that producer**. None of its contents or cancellations is transferred to the old primitive denominator without a proved change-of-frame identity retaining the full forcing, returns, finite upper boundary, and physical terminal.

The complete Family005 proof sections supplied in the prompt have been included in this audit. Full primary proofs for Family017 and Family022 were not supplied here; no theorem from those families is adopted.

---

# Part I. Audit of Family005

## 3. The exact polynomial rows and moment decomposition

### 3.1 Parameters, support, and contact

Family005 uses


$$
\begin{gathered}
n=48N,\quad a=11N,\quad b=7N,\quad q=g=4N,\quad h=2N,\\
L=59N,\quad C=63N,\quad H=65N,\quad A=19N.
\end{gathered}
\tag{3.1}
$$


Here $N$ is any positive integer.

Set


$$
f(t)=\sqrt{1-t^2},\qquad
w=\frac{t}{1+f(t)}.
$$


Then


$$
t=\frac{2w}{1+w^2},\qquad
f=\frac{1-w^2}{1+w^2}.
$$


The involution $w\mapsto w^{-1}$ fixes $t$ and negates $f$.

For $0\le r<n$,


$$
R_r=(1-t)^h t^{C-1}w^{r-g},\qquad
P_r=\frac{R_r+R_r^*}{2},\qquad
D_r=\frac{t(R_r^*-R_r)}{2f}.
\tag{3.2}
$$


Writing $d=|r-g|$, the Chebyshev identities give


$$
P_r=(1-t)^h t^{C-1}T_d(1/t),
$$




$$
D_r=\operatorname{sgn}(r-g)(1-t)^h t^{C-1}U_{d-1}(1/t).
\tag{3.3}
$$


These are integer polynomials. Since $d\le44N-1$,


$$
\operatorname{supp}P_r\subseteq\{A,\ldots,H-1\},\qquad
\operatorname{supp}D_r\subseteq\{A+1,\ldots,H-1\}.
\tag{3.4}
$$



The contact identity is exact:


$$
\frac{tP_r}{f}-D_r=\frac{tR_r}{f}.
$$


Because $w=t/2+O(t^3)$, its order at zero is


$$
C+r-g=L+r\ge L.
$$


Thus


$$
\frac{tP_r}{f}-D_r=O(t^L).
\tag{3.5}
$$



The finite boundary matters. The raw columns have indices


$$
b\le j<L.
$$


The filter $s^{b+k}(1-s)^q$, $0\le k<n$, uses raw degrees through


$$
b+(n-1)+q=L-1,
$$


not $L$. Every filtered column is therefore inside the proved contact range.

---

### 3.2 Moments and their two nonrational starting values

Define


$$
M(i,j)=\int_{-1}^1\int_0^1
 \frac{|t|}{\sqrt{1-t^2}}\frac{t^is^j}{1-ts}\,ds\,dt,
$$




$$
Z(i,j)=\int_0^1\int_0^1\frac{t^is^j}{1-ts}\,ds\,dt.
\tag{3.6}
$$


The stated logarithmic endpoint majorant proves absolute convergence, including the signed $t$-integral.

Put


$$
c_l=4^{-l}\binom{2l}{l},
$$


with $c_z=0$ unless $z$ is a nonnegative integer. The one-variable moments are


$$
m_i=
\begin{cases}
\dfrac{2}{(i+1)c_{i/2}},&i\ge0\text{ even},\\
0,&i\ge0\text{ odd},
\end{cases}
\qquad m_{-1}=0.
\tag{3.7}
$$


They satisfy


$$
(i+1)m_i=i\,m_{i-2}.
$$



Termwise integration gives


$$
M(i,j)=\sum_{u\ge0}\frac{m_{i+u}}{j+u+1},
\qquad
M(i,j)-M(i+1,j+1)=\frac{m_i}{j+1}.
\tag{3.8}
$$



For $K_d^-=M(d,0)$ and $K_d^+=M(0,d)$, the boundary recurrences are


$$
dK_d^-=(d-1)K_{d-2}^-+m_{d-2}+m_{d-1},
$$




$$
(d-1)K_d^+=(d-2)K_{d-2}^++\frac2{d-1},
\tag{3.9}
$$


with $K_1^-=2$. Their two independent nonrational starts are


$$
K_0^-=K_0^+=4G,\qquad K_1^+=\frac{\pi^2}{4}
=\frac32\zeta(2).
\tag{3.10}
$$



The manuscript supplies direct derivations of these starts:
- the first reduces to $-4\int_0^{\pi/4}\log\tan v\,dv$;
- the second follows from the Taylor series of $(\arcsin x)^2$.

Neither start is being inferred from a numerical evaluation.

Let $k_d^\pm$ satisfy the same rational recurrences with


$$
k_0^-=k_0^+=k_1^+=0,\qquad k_1^-=2.
$$


Then


$$
M^0(i,j)=
\begin{cases}
k^-_{i-j}-\displaystyle\sum_{k=1}^{j}\frac{m_{i-j+k-1}}k,&i\ge j,\\[6pt]
k^+_{j-i}-\displaystyle\sum_{k=j-i+1}^{j}
 \frac{m_{k-(j-i)-1}}k,&i<j.
\end{cases}
\tag{3.11}
$$


The convention


$$
M^0(-1,j)=k^+_{j+1}
\tag{3.12}
$$


is algebraic; it is not an additional improper integral.

With $B_i^{(d)}=\sum_{k=1}^i k^{-d}$,


$$
Z^0(i,j)=
\begin{cases}
-B_i^{(2)},&i=j,\\
\dfrac{B_i^{(1)}-B_j^{(1)}}{i-j},&i\ne j.
\end{cases}
\tag{3.13}
$$


The exact decomposition is


$$
\boxed{
M(i,j)=M^0(i,j)+4G\,c_{(i-j)/2}
+\frac32\zeta(2)c_{(j-i-1)/2}
}
\tag{3.14}
$$


and


$$
Z(i,j)=Z^0(i,j)+[i=j]\zeta(2).
\tag{3.15}
$$



The orientations of the two $c$-kernels are important: the $G$-kernel propagates toward $i\ge j$, whereas the $\zeta(2)$-kernel propagates toward $j>i$.

---

### 3.3 Exact cancellation of $\zeta(2)$

The raw column is


$$
F_j(r)=M(P_r,j)-\frac32 Z(D_r,j).
$$


Its $\zeta(2)$-coefficient is


$$
\frac32\left(
\sum_i[t^i]P_r\,c_{(j-i-1)/2}-[t^j]D_r
\right)
=\frac32[t^j]\left(\frac{tP_r}{f}-D_r\right).
$$


It vanishes for every raw index $j<L$, by (3.5). Hence


$$
F_j(r)=
\sum_i[t^i]P_r\left(M^0(i,j)+4G\,c_{(i-j)/2}\right)
-\frac32\sum_i[t^i]D_r Z^0(i,j).
\tag{3.16}
$$



Therefore every raw and filtered entry belongs to


$$
\mathbb Q+\mathbb QG.
$$


The single hypothesis $G\in\mathbb Q$ makes the determinant rational. No rationality hypothesis on $\pi^2$ is used.

**Audit conclusion:** the rationality step is complete, with the original finite column boundary intact.

---

## 4. The estimate at $2$

The manuscript’s $2$-adic argument is not merely an entrywise denominator estimate. It exploits alternating coefficient vectors.

For even $u$,


$$
v_2(m_u)
=1+u-v_2\binom{u}{u/2}
\ge u+1-\log_2(u+1).
$$


Consequently


$$
M_{\mathrm s}(i,j)=\sum_{k\ge0}\frac{m_{i+k}}{j+k+1}
$$


converges in $\mathbb Q_2$, and, for $0\le i,j<H$,


$$
v_2(M_{\mathrm s}(i,j))\ge i-2\log_2H-1.
\tag{4.1}
$$



The same finite recurrences hold $2$-adically because the telescoping tails tend to zero. There are exactly two homogeneous discrepancies:


$$
e_1=4G-M_{\mathrm s}(0,0),\qquad
e_2=-M_{\mathrm s}(0,1).
$$


After contraction with $P_r$, contact converts the second discrepancy into a coefficient of $D_r$. Thus the complete raw column splits into:
- a smoothed column $S_j$;
- an exceptional $G$-kernel column $E_j$;
- a $D$-coefficient/harmonic column $B_j$.

Removing $(1-t)^h$, write the fixed coefficient vectors as $\mathbf p_u,\mathbf d_u$. The Chebyshev recurrence gives


$$
v_2(\mathbf p_u)\ge u-1,\qquad
v_2(\mathbf d_u)\ge u-1.
$$


For a determinant term containing $m$ exceptional $E$-columns and $l$ $B$-columns, alternation forces distinct coefficient indices within each group:


$$
\sum_Eu\ge\frac{m(m-1)}2,\qquad
\sum_Bu\ge\frac{l(l-1)}2.
$$


Distinct raw column indices also give


$$
\sum_Ej\ge mb+\frac{m(m-1)}2.
$$



These are legitimate distinctness statements. The proof does **not** require the $E$-indices to be distinct from the $B$-indices.

The resulting lower bound is


$$
v_2(\Delta_N)\ge
-O_G(n\log(n+2))
+\min_{m+l\le n}
\left\{
-(H-b)m+\frac32m^2+\frac12l^2+C(n-m-l)
\right\}.
\tag{4.2}
$$


Since $C\ge n$, the real minimum occurs at $l=n-m$. With


$$
\delta=\frac{q+g+h}{n}=\frac5{24},
$$


completion of the square yields


$$
\boxed{
v_2(\Delta_N)\ge
-\frac{505}{4608}n^2-O_G(n\log(n+2)).
}
\tag{4.3}
$$


The same proof applies to every full raw minor, so Cauchy–Binet legitimately transfers it through the integer filter.

**Audit conclusion:** no omitted $2$-adic discrepancy, coefficient convolution, or filter denominator was found.

---

## 5. Both odd-prime layers

### 5.1 Digit reduction and its hypotheses

For


$$
2\sqrt H<p\le H,
$$


one has $H<p^2/4$. After excluding the fixed denominator primes of a hypothetical rational $G$, the $G$-coefficient in (3.16) is $p$-integral.

Set


$$
E(t)=(1-t^2)^{(p-1)/2},\qquad
\epsilon=(-1)^{(p-1)/2}.
$$


Its coefficients satisfy


$$
E_d\equiv c_{d/2}\pmod p,\qquad
E_{p-1-d}=\epsilon E_d.
\tag{5.1}
$$



The rational boundary arrays are controlled by


$$
H_z^*=
\begin{cases}
c_{z/2},&z\text{ even},\\[2pt]
\dfrac1{z\,c_{(z-1)/2}},&z\text{ odd},
\end{cases}
\qquad
\frac{H_{z+2}^*}{H_z^*}=\frac{z+1}{z+2}.
\tag{5.2}
$$


In particular,


$$
k_u^-=
\begin{cases}
H_u^*\displaystyle\sum_{\substack{1\le z\le u\\z\ {\rm even}}}
 \frac2{z^2(H_z^*)^2},&u\text{ even},\\[6pt]
H_u^*\displaystyle\sum_{\substack{1\le z\le u\\z\ {\rm odd}}}\frac2z,
 &u\text{ odd},
\end{cases}
$$




$$
k_{u+1}^+
=H_u^*\sum_{\substack{1\le z\le u\\z\equiv u\ (2)}}
 \frac2{z^2H_z^*}.
\tag{5.3}
$$



Writing $z=Pp+r$, the parity/carry calculation gives


$$
p\,m_{z-1}\equiv E_{p-1-r}m_{P-1}\pmod p,
\tag{5.4}
$$


and


$$
p^2k_u^-\equiv E_{p-1-r}k_P^-,
\qquad
p^2k_{u+1}^+\equiv E_r k_{P+1}^+
\pmod p.
\tag{5.5}
$$



The potentially delicate even-minus calculation retains complete blocks


$$
z=mp-\lambda,\qquad
m=2,4,\ldots,P,\quad \lambda=0,2,\ldots,p-1.
$$


Its block factor is


$$
\sum_{j=0}^{(p-1)/2}c_j^2
\equiv
\binom{p-1}{(p-1)/2}
=\epsilon\pmod p.
\tag{5.6}
$$


There is no unaccounted partial block when the terminal residue $r$ is even; when $r$ is odd, the prefactor makes the leading reduction vanish.

For $0\le i,j<H$, put


$$
\ell=j\bmod p,\quad d=(j-i-1)\bmod p,
$$




$$
i'=\frac{i+1+d-\ell}{p}-1,\qquad j'=\lfloor j/p\rfloor.
$$


Then $i'\ge-1$, and


$$
p^2M^0(i,j)\equiv E_dM^0(i',j')\pmod p,
\tag{5.7}
$$




$$
p^2Z^0(i,j)\equiv
\begin{cases}
Z^0(\lfloor i/p\rfloor,j'),&i\equiv j\pmod p,\\
0,&i\not\equiv j\pmod p.
\end{cases}
\tag{5.8}
$$



The convention $M^0(-1,j')=k^+_{j'+1}$ is necessary in (5.7). Dropping it would invalidate the leading column formula.

---

### 5.2 First layer: paired raw columns

For each residue $\ell$, define


$$
P'_u=[t^{(u+1)p+\ell}]\,tP(t)E(t),\qquad
D'_u=[t^{up+\ell}]D(t).
$$


Then


$$
X_{kp+\ell}:=p^2F_{kp+\ell}\bmod p
=\sum_{u\ge-1}P'_uM^0(u,k)
-\frac32\sum_{u\ge0}D'_uZ^0(u,k).
\tag{5.9}
$$



If $\ell\ge H-2p$, only $u=-1,0,1$ can contribute. With


$$
V_\ell=2P'_1-\frac32D'_1,\qquad
U_\ell=2P'_{-1}-\frac32D'_0,
$$


the exact small-array values give


$$
X_\ell=V_\ell,\qquad
X_{p+\ell}=U_\ell-V_\ell.
\tag{5.10}
$$


The support bound implies $U_\ell=0$ for $\ell\le A$.

Thus, for


$$
\max(b,H-2p)\le\ell<\min(p,L-p,A),
$$


the high column can be replaced by the pair sum, gaining one power of $p$. The operation and its inverse are integral over $\mathbb Z_p$.

For $p\le H/2$, the number of such pairs is


$$
d_0=\bigl(\min(p,L-p,A)-\max(b,H-2p)\bigr)_+.
$$


Because a full minor chooses $n$ columns from a pool of $n+q$, it contains at least $(d_0-q)_+$ improved columns. Hence


$$
v_p(\Delta_N)\ge-2n+(d_0-q)_+.
\tag{5.11}
$$



This is a denominator-layer statement about complete minors, not an assertion of primitive scalar saturation.

---

### 5.3 Second layer: central columns and retained representatives

For $p>H/2$, put


$$
K=L-p,\qquad J=H-p.
$$


A central column satisfies


$$
b\le j<\min(p,L),\qquad j\ge J.
$$


For every contributing degree $i$, $|i-j|<p$; the starting boundary values are therefore integral. Reducing the remaining harmonic terms gives


$$
\boxed{
pF_j\equiv-\sum_{0\le\ell<J}\frac{V_\ell}{j-\ell}\pmod p.
}
\tag{5.12}
$$


Every denominator $j-\ell$ is a unit.

The proof then **retains** noncentral columns representing $V_\ell$. If


$$
p^2Y_\ell\equiv\sigma_\ell V_\ell\pmod p,
$$


the shear


$$
F_j\longmapsto F_j+
p\sum_\ell a_{\ell j}Y_\ell,\qquad
a_{\ell j}\equiv\frac{\sigma_\ell}{j-\ell}\pmod p,
\tag{5.13}
$$


cancels the represented part of (5.12).

This is the crucial paid second-layer operation. If


$$
Y_\ell=p^{-2}y_0+p^{-1}y_1+y_2,
$$


then


$$
pY_\ell=p^{-1}y_0+y_1+py_2.
$$


The unknown second coefficient is already integral and causes no omitted $p^{-1}$ error.

The resulting counts are


$$
R=K_++(K-A)_++(J-\max(b,K))_+,
$$




$$
S=(\min(A,K)-b)_+
+(\min(b,J)-\max(0,K))_+.
\tag{5.14}
$$


They yield


$$
\boxed{
v_p(\Delta_N)\ge-\min(2n,n+R,2R+S).
}
\tag{5.15}
$$



The argument also covers $K\le0$, missing low columns, and the endpoint $p=H$. The optional pair at $\ell=A$ is not discarded; it remains among the retained columns.

**Audit conclusion:** the second layer is genuinely proved. It is not inferred from leading rank alone.

---

## 6. The ALL-prime lower bound

Writing $x=p/N$, the odd-prime loss function is


$$
d(x)=
\begin{cases}
96,&0\le x\le25,\\
146-2x,&25\le x\le29,\\
88,&29\le x\le65/2,\\
153-2x,&65/2\le x\le69/2,\\
222-4x,&69/2\le x\le40,\\
182-3x,&40\le x\le58,\\
124-2x,&58\le x\le59,\\
65-x,&59\le x\le65,\\
0,&x\ge65.
\end{cases}
\tag{6.1}
$$


Its exact area is


$$
\int_0^{65}d(x)\,dx=\frac{8609}{2}.
\tag{6.2}
$$



The small odd primes contribute only


$$
O\!\left(n\sqrt H\log H+n\log\operatorname{den}G\right)=o(n^2).
$$


For sufficiently large $N$, primes $p>H$ introduce no negative valuation.

The ordinary prime number theorem, in the form $\theta(y)\sim y$, gives


$$
\frac1N\sum_{p\le65N}d(p/N)\log p
\longrightarrow\int_0^{65}d(x)\,dx.
$$


No prime number theorem in arithmetic progressions is needed.

For a nonzero rational determinant, the exact product formula is


$$
\log|\Delta_N|=\sum_pv_p(\Delta_N)\log p.
$$


Combining all primes therefore gives


$$
\liminf
\left(\frac{\log|\Delta_N|}{n^2}-\frac12\log2\right)
\ge
-\frac{8609}{4608}
-\frac{2809}{4608}\log2
>-2.29084,
\tag{6.3}
$$


along any sequence of nonzero determinants under $G\in\mathbb Q$.

The requirement “nonzero” is indispensable here. It is supplied separately, not by positivity.

---

## 7. Frobenius nonvanishing at prime scales

### 7.1 The varying basis change is proved invertible

Set $N=p$, with $p$ an odd prime. The palindromic polynomial space of degree at most $2p-2$ has bases


$$
U_\ell=(2w)^\ell(1+w^2)^{p-1-\ell},
$$




$$
Q_i=w^i\sum_{j=0}^{p-i-1}w^{2j}.
$$


Writing $Q_i=\sum_\ell a_{\ell i}U_\ell$, comparison of lowest terms gives


$$
a_{\ell i}=0\quad(\ell<i),\qquad
a_{ii}=2^{-i}.
$$


Thus


$$
\det\mathbf a=2^{-p(p-1)/2}\ne0.
\tag{7.1}
$$



With $Q'_0=0$, $Q'_i=Q_{p-i}$, and $\mathbf b=\mathbf a\Pi$, one obtains


$$
E(t)w^i=\sum_{\ell=0}^{p-1}t^\ell
(a_{\ell i}+b_{\ell i}w^p).
\tag{7.2}
$$



### 7.2 Both extraction shifts are retained

Writing $r=pr_0+i$, Frobenius gives


$$
tP_rE
=\sum_\ell t^\ell t'
\left(a_{\ell i}\underline P_{r_0}(t')
+b_{\ell i}\underline P_{r_0+1}(t')\right),
$$




$$
D_r
=\sum_\ell t^\ell
\left(a_{\ell i}\underline D_{r_0}(t')
+b_{\ell i}\underline D_{r_0+1}(t')\right).
\tag{7.3}
$$


The extra $t'$ in the first identity is exactly consumed by the extraction exponent $(u+1)p+\ell$. The second extraction has no such shift.

The successor row $48$ is essential. Its minimum degrees are


$$
\min\deg\underline P_{48}=18,\qquad
\min\deg\underline D_{48}=19.
$$


For the last growing row block these terms begin at the original degree $20p-i$, exactly as required. They cannot be removed to make the base matrices look uniform.

### 7.3 Fixed blocks and their scope

For $p>260$, the condition $p>2\sqrt{65p}$ holds. After excluding the fixed denominator primes of $G$, the scaled growing matrix reduces to


$$
\mathcal L_p
=\mathbf a^T\otimes\mathcal B_0
+\mathbf b^T\otimes\mathcal B_1.
$$


Right multiplication by $(\mathbf a^T)^{-1}\otimes I$ gives


$$
I_p\otimes\mathcal B_0+\Pi^T\otimes\mathcal B_1.
$$


The eigenvalues of $\Pi$ are $0,1,-1$, with multiplicities


$$
1,\quad\frac{p-1}{2},\quad\frac{p-1}{2}.
$$


Hence


$$
\det\mathcal L_p
=(\det\mathbf a)^{48}\det\mathcal B_0\,
\det(\mathcal B_0+\mathcal B_1)^{(p-1)/2}
\det(\mathcal B_0-\mathcal B_1)^{(p-1)/2}.
\tag{7.4}
$$



The finite certificate asserts that all three fixed determinants are nonzero modulo $101$. **If that assertion is independently verified**, they are nonzero rational numbers. Excluding their finitely many numerator and denominator primes then proves


$$
v_p(\Delta_p)=-2(48p)=-96p
\tag{7.5}
$$


for every sufficiently large prime $p$.

The modulus $101$ verifies only the fixed matrices. The infinite prime-index conclusion comes from the symbolic reduction (7.4), not from extrapolating a finite computation.

---

## 8. Bounded interpolation and the real determinant

The two applications of Andréief retain the factor


$$
\frac1{(n!)^2}.
$$


After the substitution $t=2x/(1+x^2)$, the mixed sheet determinant is


$$
\mathcal R_n(x)=
\det\left[
\xi_{\mathrm f}(x_i)x_i^{g-r}
+\xi_{\mathrm n}(x_i)x_i^{r-g}
\right],
$$


where


$$
(\xi_{\mathrm f},\xi_{\mathrm n})=
\begin{cases}
(1/2,1/2),&x<0,\\
(-1/4,5/4),&x>0.
\end{cases}
\tag{8.1}
$$


Thus the sheet ratio is $1$ on the negative interval and $-5$ on the positive interval. Neither branch is omitted.

Put $D_*=n-1-2g$. In the first case,


$$
\sum_i\frac{1-x_i^2}{1+x_i^2}\le D_*.
\tag{8.2}
$$


For


$$
B(z)=\prod_i\frac{z-x_i}{1-x_i z},\qquad F(z)=\frac{z^{D_*}}{B(z)},
$$


the logarithmic derivative estimate on the imaginary diameter gives


$$
|B(iu)|\ge u^{D_*}\qquad(0<u\le1).
$$


Consequently $F$ is uniformly bounded there. A fixed Cauchy integral with jump $6F$ glues the two expressions


$$
z^{D_*}-B(z)\mathcal C(z),\qquad
-5z^{D_*}-B(z)\mathcal C(z).
$$


The jump sign is correct: the left lateral Cauchy value minus the right one equals $6F$.

The contour deformation near $\pm i$ proves


$$
\|h_*\|_\infty\le10e^{12}n,
\tag{8.3}
$$


independently of node separation. The exterior holomorphic neighborhood may shrink with the nodes; the proof does not require it to be uniform.

The Hardy-space step is also genuinely finite-dimensional. In


$$
\mathcal H_Q=\{v/Q:\deg v<n\},\qquad Q(z)=\prod_i(1-x_i z),
$$


the reversal $v(z)\mapsto z^{n-1}v(1/z)$ is an isometry because $Q$ has real coefficients. Projection onto $\mathcal H_Q$ preserves evaluation at every $x_i$. Therefore the evaluation determinant cancels algebraically, rather than through an inverse-Vandermonde norm estimate.

This gives


$$
|\mathcal R_n(x)|
\le(1+10e^{12}n)^n\,
\mathcal V(1/x)\prod_i|x_i|^g.
\tag{8.4}
$$


In the complementary case, the separate Hadamard argument gives


$$
|\mathcal R_n(x)|
\le(3/2)^n n^{n/2}2^{-\binom n2}
\prod_i(1+x_i^2)^{(n-1)/2}|x_i|^{g-(n-1)}.
\tag{8.5}
$$



All factorial, measure-mass, and sheet-sum factors are retained. Their logarithms are $O(n\log n)$, not silently discarded as exact identities.

**Audit conclusion:** the interpolation estimate is center- and separation-uniform in the required sense. No unproved general interpolation theorem is doing hidden work.

---

## 9. Uniform energy reduction

The exact finite identity contains the correction


$$
\frac{\kappa+2}{2n}\log(1+x^2)
$$


and the constant


$$
c_{\kappa,n}
=\frac Cn+\frac{\kappa-2}{2}-\frac{\kappa+1}{2n}.
$$


The exponent of $|x|$ is exactly $a+2g$; there is no lost singular finite-size term at $x=0$.

The potentially dangerous point is uniformity before taking a supremum. The manuscript addresses it by matched damping:


$$
\tau=1-\varepsilon,\quad
\rho(x)=1-\varepsilon(1-x),\quad
\sigma(s)=1-\varepsilon\sqrt{1-s}.
\tag{9.1}
$$


The pure and cross kernels then use the same moments


$$
A_k=\langle\tau^kT_k(x)\rangle,\quad
B_k=\langle\rho(x)^kx^k\rangle,\quad
C_k=\langle\sigma(s)^kT_k(s)\rangle.
$$


Their quadratic contribution is exactly


$$
-\kappa\sum_{k\ge1}\frac{A_k^2}{k}
-\frac12\sum_{k\ge1}\frac{(B_k-2C_k)^2}{k}.
\tag{9.2}
$$



The comparisons have the required signs, including:
- opposite-sign $xx'$ in the power kernel;
- the cross singularity near $x=s=1$.

The omitted diagonals cost, in addition to $O_\varepsilon(1/n)$,


$$
-\frac1{2n}\langle\log(1-x)\rangle
-\frac1n\langle\log(1-s)\rangle.
\tag{9.3}
$$


These terms weaken, but do not remove, the positive endpoint charges.

For $n\ge24$, the weakened endpoint coefficients remain at least $1/24$. This forces all maximizers into compact sets independent of $n$ and small $\varepsilon$. The justified limit order is


$$
n\to\infty\quad\text{first},\qquad
\varepsilon\downarrow0\quad\text{second}.
$$


This removes $O_\varepsilon(1/n)$ before damping is removed.

The final dual bound is


$$
\begin{aligned}
(-1+\alpha+\gamma)\log2
&+\kappa\|p\|_*^2+\frac12\|v\|_*^2\\
&+\sup_x\{W_\kappa(x)+\lambda D(x)-2\kappa T(p,x)-S(v,x)\}\\
&+\sup_s\{\beta\log s+\gamma\log(1-s)+2T(v,s)\}.
\end{aligned}
\tag{9.4}
$$



**Audit conclusion:** the usual empirical-diagonal and endpoint-uniformity gap is not present in the displayed proof.

---

## 10. What remains to be independently certified in Family005

There are two substantive finite arithmetic checks.

### 10.1 Fixed modular certificate

The bounded input is:
- moment indices $0\le i\le64$, $0\le j\le58$;
- polynomial rows $0\le r\le48$, including the auxiliary degree-$18$ coefficient;
- four consecutive-difference operations;
- the three $48\times48$ matrices $\mathcal B_0+\sigma\mathcal B_1$, $\sigma=0,1,-1$;
- arithmetic in $\mathbb F_{101}$.

The expected verifiable output is:
- all three matrices have rank $48$;
- the pivot and swap records agree with the supplied certificate, or another exact elimination record proves the same ranks.

The coordinator has already assigned this reproduction. It should not be duplicated merely to reopen a closed calculation.

### 10.2 Real barrier certificate

The bounded input is the supplied rational trial coefficients and four derivative numerators of degrees


$$
36,\quad24,\quad13,\quad9.
$$


The expected outputs are:
- respectively $18,15,5,5$ exhausted simple derivative roots in the stated brackets;
- all finite division-point values included;
- the rational norm and point-value cutoffs;
- the bracket derivative bound $120000$;
- the resulting global bounds


$$
-2.290939875,\qquad -2.296789875.
$$



The logarithm and argument algorithms are mathematically adequate:
- the logarithm uses an explicit positive geometric remainder;
- the octant reduction leaves a rational tangent;
- the arctangent remainder is explicit;
- the complex logarithm branches are controlled.

What has not been done here is the actual rational arithmetic validating the tables.

Subject to these finite checks, the source lower bound $>-2.29084$, nonvanishing at $N=p$, and real upper bound $<-2.2909$ do contradict one another under $G\in\mathbb Q$.

The historical bibliography and hyperbolic-volume corollaries require their separately cited premises. They are not inputs to the determinant contradiction, and they provide no implication concerning $e+\pi$.

---

# Part II. A concrete factorial-compatible construction for $e+\pi$

## 11. Why the factorial channel cannot be replaced by a compact algebraic moment functional

For a polynomial $P$, define its exponential charge by


$$
\mathcal E(P)=\sum_{k\ge0}(-1)^kP^{(k)}(1).
\tag{11.1}
$$


The sum is finite. Taylor expansion and the gamma integral give the exact identity


$$
\boxed{
\mathcal E(P)
=\int_0^\infty e^{-u}P(1-u)\,du
=e^{-1}\int_{-\infty}^{1}e^tP(t)\,dt.
}
\tag{11.2}
$$


In particular,


$$
\mathcal E((1-t)^k)=k!.
\tag{11.3}
$$



Thus $\mathcal E$ is not a bounded finite signed measure on a fixed compact interval. If it were supported in $[-R,R]$, with total variation $M$, then


$$
k!\le M(1+R)^k
$$


for all $k$, which is impossible.

This is the exact obstruction to replacing the factorial charge by Catalan’s compact algebraic density. A compact **real integral representation** can still be used, but its rational period coefficients carry factorial arithmetic. That arithmetic must be paid.

---

## 12. Exact endpoint contact for the exponential coefficient

Define


$$
\Lambda_m(t)=
\sum_{k=0}^{m}
(-1)^k\binom{m+1}{k+1}\frac{(1-t)^k}{k!}.
\tag{12.1}
$$


These are $L_m^{(1)}(1-t)$, but no external Laguerre theorem is needed below.

The generating function follows directly from the binomial series:


$$
\sum_{m\ge0}\Lambda_m(t)z^m
=(1-z)^{-2}
\exp\!\left(-\frac{(1-t)z}{1-z}\right).
\tag{12.2}
$$



### Proposition 12.1 — Exact factorial contact

For every $m\ge0$ and $0\le j\le m$,


$$
\boxed{\mathcal E(\Lambda_m(t)t^j)=1.}
\tag{12.3}
$$



#### Proof

Substitute $t=1-u$ in (11.2). Applying $\mathcal E$ coefficientwise to (12.2) gives


$$
\begin{aligned}
\sum_{m\ge0}\mathcal E(\Lambda_m t^j)z^m
&=(1-z)^{-2}
\int_0^\infty e^{-u/(1-z)}(1-u)^j\,du\\
&=\sum_{k=0}^{j}
(-1)^k\binom jk k!(1-z)^{k-1}.
\end{aligned}
$$


For $m\ge j$, every term with $k\ge1$ has degree at most $j-1$, so its $z^m$-coefficient vanishes. The $k=0$ term is $(1-z)^{-1}$, whose coefficient is $1$. ∎

This is an exact period-coefficient matching mechanism for the exponential channel. It is not a numerical approximation to its charge.

---

## 13. Complete rational entries and exact cancellation of the separate periods

Define


$$
A_{m,j}
=j!\sum_{\ell=0}^{m-j}
(-1)^\ell\binom{m-j}{\ell}\frac1{(j+\ell)!},
\qquad 0\le j\le m.
\tag{13.1}
$$


Then


$$
\boxed{
\int_0^1 e^t t^j\Lambda_m(t)\,dt=e-A_{m,j}.
}
\tag{13.2}
$$



To verify the rational term, the full integral over $(-\infty,1]$ equals $e$ by Proposition 12.1. The omitted interval contributes


$$
\int_{-\infty}^0e^tt^j\Lambda_m(t)\,dt.
$$


Its generating function is


$$
(-1)^j j!(1-z)^{j-1}e^{-z/(1-z)}.
$$


Extracting the coefficient of $z^m$ gives precisely (13.1). Thus both endpoints are included in (13.2).

For the $\pi$-channel, put


$$
B_j=4\sum_{k=0}^{2j-1}\frac{(-1)^k}{2k+1},
\qquad B_0=0.
\tag{13.3}
$$


Polynomial division gives


$$
\boxed{
4\int_0^1\frac{s^{4j}}{1+s^2}\,ds=\pi-B_j.
}
\tag{13.4}
$$


Only even powers occur, so there is no $\log2$ coefficient.

Now return to the original A2 values $n,b$ in (2.1), and set


$$
m_r=n+r,\qquad 0\le r<b.
$$


Define the $b\times b$ matrix


$$
H_{rj}
=\int_0^1e^t t^j\Lambda_{m_r}(t)\,dt
+4\int_0^1\frac{s^{4j}}{1+s^2}\,ds,
\qquad 0\le r,j<b.
\tag{13.5}
$$


Since $j\le b-1<n\le m_r$, every entry lies in the contact range. Its exact value is


$$
\boxed{
H_{rj}=(e+\pi)-A_{m_r,j}-B_j.
}
\tag{13.6}
$$



This is a genuinely compact mixed moment matrix: it can be viewed as a moment pairing on the disjoint union of two copies of $[0,1]$, with measures $e^t\,dt$ and $4\,ds/(1+s^2)$. The arithmetic exponential charge remains the noncompact factorial functional (11.2).

The construction matches $e$ and $\pi$ with coefficient $1$ in every entry. Under $e+\pi\in\mathbb Q$, there is no unwanted separate coefficient left to cancel.

---

## 14. Integer payments, actual contents, and the least clearer

### 14.1 Polynomial payment

The polynomial


$$
m!\Lambda_m(t)
$$


has integer coefficients and is monic. Therefore:
- its polynomial content is $1$;
- its actual least coefficient clearer is exactly $m!$.

This is already a major arithmetic difference from the integral Chebyshev rows of Family005.

Put


$$
N_{m,j}=m!A_{m,j}
=j!\sum_{\ell=0}^{m-j}
(-1)^\ell\binom{m-j}{\ell}\frac{m!}{(j+\ell)!}\in\mathbb Z.
\tag{14.1}
$$



### Lemma 14.1 — A factorial residue congruence

If $p$ is prime and $m\equiv j\pmod p$, then


$$
\boxed{
\frac{N_{m,j}}{j!}\equiv(-1)^{m-j}\pmod p.
}
\tag{14.2}
$$



#### Proof

Reindex (14.1) by $h=m-j-\ell$:


$$
\frac{N_{m,j}}{j!}
=(-1)^{m-j}
\sum_{h=0}^{m-j}
(-1)^h\binom{m-j}{h}\frac{m!}{(m-h)!}.
$$


The $h=0$ term is $1$.

For $1\le h<p$, the binomial coefficient is divisible by $p$, because $p\mid m-j$. For $h\ge p$, the product


$$
m(m-1)\cdots(m-h+1)
$$


contains a multiple of $p$. Every nonconstant term therefore vanishes modulo $p$. ∎

### Corollary 14.2 — Exact full-contact clearer

For every $m$,


$$
\boxed{
\operatorname{lcm}_{0\le j\le m}\operatorname{den}(A_{m,j})=m!.
}
\tag{14.3}
$$



Indeed, for each prime $p\le m$, choose $j=m\bmod p$. Then $j! \not\equiv0\pmod p$, so $N_{m,j}$ is a $p$-adic unit. No factor of $p^{v_p(m!)}$ can be removed from the simultaneous clearer. This proves the statement over **all primes**, not just one chosen prime.

---

### 14.2 The complete mixed rational part

For our finite window, define


$$
R_{rj}=A_{m_r,j}+B_j,\qquad
W_{rj}=m_r!R_{rj}.
\tag{14.4}
$$


Every denominator in $B_j$ is an odd integer at most $4j-1$, hence less than $4b$. Since $m_r\ge2001b$, every $W_{rj}$ is an integer.

The actual row content and least row clearer are


$$
\kappa_r=\gcd\bigl(m_r!,W_{r0},\ldots,W_{r,b-1}\bigr),
\qquad
C_r=\frac{m_r!}{\kappa_r}.
\tag{14.5}
$$


Thus


$$
Y_{rj}=C_rR_{rj}=\frac{W_{rj}}{\kappa_r}\in\mathbb Z,
$$


and


$$
\gcd(C_r,Y_{r0},\ldots,Y_{r,b-1})=1.
\tag{14.6}
$$


The least simultaneous clearer of all $R_{rj}$ is exactly


$$
\boxed{\mathcal L_n=\operatorname{lcm}_{0\le r<b}C_r.}
\tag{14.7}
$$



No estimated clearer is substituted for these exact objects.

---

### 14.3 Exact contents at every prime $p\le b$

For $p\le b$,


$$
v_p(m_r!B_j)>v_p(j!).
\tag{14.8}
$$


One way to see this is to use


$$
v_p(B_j)\ge-\lfloor\log_p(4b-1)\rfloor,
$$


whereas


$$
v_p(m_r!)-v_p(j!)
\ge \lfloor m_r/p\rfloor-\lfloor j/p\rfloor.
$$


The latter is at least $2000b/p-1$, overwhelmingly larger than the logarithmic denominator loss. Thus the complete $\pi$-rational term is retained and cannot cancel the residue in Lemma 14.1.

Choose $j=m_r\bmod p<b$. Lemma 14.1 and (14.8) imply


$$
v_p(\kappa_r)=0,\qquad
\boxed{v_p(C_r)=v_p(m_r!)\quad(p\le b).}
\tag{14.9}
$$



Now define the actual content of column $j$, including both its period and rational coefficients, by


$$
c_j=\gcd_{0\le r<b}(C_r,Y_{rj}).
\tag{14.10}
$$


All $N_{m,j}$ are divisible by $j!$. The window $m=n,\ldots,n+b-1$ contains a representative of every residue modulo $p\le b$. Choosing $m\equiv j\pmod p$ in Lemma 14.1 therefore proves


$$
\boxed{
v_p(c_j)=v_p(j!)\quad
(0\le j<b,\ p\le b).
}
\tag{14.11}
$$


In particular $j!\mid c_j$. Possible additional factors at primes $p>b$ remain in the exact gcd (14.10); they are not silently discarded.

These are actual contents of this new finite matrix. They are not a bound on the original A2 norm valuation $\nu$.

---

### 14.4 The exact cost at $29$

Because


$$
2001=3\cdot23\cdot29,\qquad n=2001b,
$$


one has $29\mid n$. At the first row and first column,


$$
N_{n,0}\equiv(-1)^n=-1\pmod{29}.
$$


Since $B_0=0$,


$$
\boxed{
v_{29}(C_0)=v_{29}(n!)
=\frac{n-s_{29}(n)}{28}.
}
\tag{14.12}
$$


The proposed auxiliary exponential contact is therefore not a $29$-adic unit-cost operation.

This is a concrete obstruction to treating the unpaid exponential residue and auxiliary clearer as harmless companions to the accepted logarithmic determinant (2.2).

---

## 15. Quantified arithmetic cost of the new construction

For $m\in[n,n+b-1]$, primes $p>b$ contribute only $O(m)$ to $\log(m!)$. For the original indices, $b$ is much larger than $2002$, so such primes have $p^2>m$, and


$$
\sum_{p>b}v_p(m!)\log p
=\sum_{k\le2001}\bigl(\theta(m/k)-\theta(b)\bigr)_+
=O(m).
\tag{15.1}
$$


The ordinary prime number theorem suffices; an elementary Chebyshev bound would also give the required $O(m)$.

Since all row-content cancellation occurs at primes $p>b$,


$$
\log C_r=\log(m_r!)+O(n).
$$


Similarly, (14.11) and $c_j\mid C_0\mid n!$ give


$$
\log c_j=\log(j!)+O(n).
$$



Define the complete row-and-column payment


$$
P_n=\frac{\prod_{r=0}^{b-1}C_r}
          {\prod_{j=0}^{b-1}c_j}.
\tag{15.2}
$$


It is an integer: every $c_j$ divides every $C_r$, so this follows prime by prime.

Stirling’s formula, with $n=2001b$, now gives


$$
\sum_{r=0}^{b-1}\log((n+r)!)
=\frac{4003}{2}b^2\log b+O(b^2),
$$




$$
\sum_{j=0}^{b-1}\log(j!)
=\frac12b^2\log b+O(b^2).
$$


Therefore


$$
\boxed{
\log P_n=2001\,b^2\log b+O(b^2).
}
\tag{15.3}
$$



This is a proved arithmetic cost after the actual row and column contents have been removed. It is not merely the cost of an arbitrary oversized common denominator.

---

## 16. A uniform real estimate using the complete finite row window

The rational entries satisfy an exact finite-difference identity:


$$
A_{m+1,j}-A_{m,j}
=-\frac{A_{m+1,j+1}}{j+1}.
\tag{16.1}
$$


It follows directly by subtracting the binomial sums in (13.1).

More generally,


$$
\Delta_m^rA_{n,j}
=(-1)^rj!
\sum_{\ell=0}^{n-j}
(-1)^\ell\binom{n-j}{\ell}
\frac1{(j+r+\ell)!}.
\tag{16.2}
$$



Replace row $r$ of $H$ by the $r$-th forward difference of rows $0,\ldots,r$. This is a lower-triangular integer row operation with diagonal $1$, hence determinant $1$. It uses exactly the finite window through $m=n+b-1$.

For $r\ge1$, both $e+\pi$ and the entire $B_j$ term cancel under this operation:


$$
\Delta_m^rH_{n,j}=-\Delta_m^rA_{n,j}.
$$


No separate exponential or logarithmic remainder is omitted.

Using


$$
\binom{n-j}{\ell}\le\frac{n^\ell}{\ell!},
\qquad
(j+r+\ell)!\ge(j+r)!\,\ell!,
$$


we obtain


$$
|\Delta_m^rH_{n,j}|
\le\frac{j!}{(j+r)!}
\sum_{\ell\ge0}\frac{n^\ell}{(\ell!)^2}
\le\frac{e^{2\sqrt n}}{r!}.
\tag{16.3}
$$


The last inequality follows because the diagonal terms of
$e^{\sqrt n}e^{\sqrt n}$ include the displayed sum.

For the first row, $e+\pi<7$ and


$$
|A_{n,j}|\le e^{2\sqrt n}
$$


give


$$
|H_{0j}|\le8e^{2\sqrt n}.
$$


Hadamard’s inequality therefore proves the uniform bound


$$
\boxed{
|\det H|
\le
M_n:=
\frac{8\,b^{b/2}e^{2b\sqrt n}}
     {\prod_{r=1}^{b-1}r!}.
}
\tag{16.4}
$$


Consequently


$$
\log M_n=-\frac12b^2\log b+O(b^2).
\tag{16.5}
$$



This is a real determinant estimate for the exact mixed construction, not a replacement of the exponential channel by a Catalan kernel.

But after the paid contents,


$$
\boxed{
\log(P_nM_n)
=\frac{4001}{2}b^2\log b+O(b^2).
}
\tag{16.6}
$$


The presently proved real decay does not pay the arithmetic cost.

---

## 17. The actual primitive scalar denominator and whole error

After removing the exact column contents, define integer matrices


$$
\mathsf A_{rj}=\frac{C_r}{c_j},\qquad
\mathsf Z_{rj}=\frac{Y_{rj}}{c_j}.
$$


The matrix $\mathsf A$ has rank one. Therefore


$$
D_n(X)=\det(X\mathsf A-\mathsf Z)
$$


is affine:


$$
D_n(X)=U_nX-V_n,
\qquad U_n,V_n\in\mathbb Z.
\tag{17.1}
$$


These coefficients have an explicit bounded integer-determinant definition:


$$
V_n=-\det(-\mathsf Z),
$$




$$
U_n=\det(\mathsf A-\mathsf Z)-\det(-\mathsf Z).
\tag{17.2}
$$


Also,


$$
D_n(e+\pi)=P_n\det H.
\tag{17.3}
$$



If $U_n\ne0$, let


$$
G_n=\gcd(|U_n|,|V_n|),
$$


where the gcd includes **all primes**, and define


$$
q_n=\frac{|U_n|}{G_n},\qquad
p_n=\frac{\operatorname{sgn}(U_n)V_n}{G_n}.
\tag{17.4}
$$


These are the actual primitive numerator and denominator of this construction. The whole error is exactly


$$
\boxed{
q_n(e+\pi)-p_n
=\frac{\operatorname{sgn}(U_n)P_n}{G_n}\det H.
}
\tag{17.5}
$$



Neither $U_n\ne0$ nor $\det H\ne0$ has been proved on an infinite original index set. Nor has the required final scalar gcd been evaluated. The definitions (17.1)–(17.5) isolate those obligations; they do not solve them.

### Concrete follow-on lemma

A sufficient new lemma for this explicit matrix would be:

> On one infinite subset of the original indices (2.1), prove $U_n\ne0$, prove $\det H\ne0$, and prove
> 

$$
> G_n\ge e^b P_nM_n.
> \tag{17.6}
>
$$



Then (17.5) and (16.4) would give


$$
0<|q_n(e+\pi)-p_n|\le e^{-b}\longrightarrow0.
$$



In terms of the presently proved budget, it would suffice to establish, for some fixed $\varepsilon>0$,


$$
\log G_n\ge
\left(\frac{4001}{2}+\varepsilon\right)b^2\log b
\tag{17.7}
$$


on the same nonzero infinite original sequence. Alternatively, a correspondingly stronger real estimate could replace part of this gcd requirement.

This is a specific factorial-saturation and nonvanishing problem for explicit integer matrices. A fixed-modulus rank check or a column-content estimate alone would not establish it.

---

## 18. A proved whole-error obstruction for the immediate scalar

The first matched entry is


$$
H_{00}=(e+\pi)-A_{n,0},
\qquad
A_{n,0}=\sum_{k=0}^{n}\frac{(-1)^k\binom nk}{k!}.
\tag{18.1}
$$


It is tempting to regard $A_{n,0}$ as an approximation to $e+\pi$. It is not.

Define


$$
J(t)=\frac1{2\pi}\int_0^{2\pi}
\cos(2\sqrt t\cos\theta)\,d\theta.
$$


Then $|J(t)|\le1$, and expansion of the cosine gives


$$
J(t)=\sum_{k\ge0}\frac{(-1)^kt^k}{(k!)^2}.
$$


Termwise gamma integration is absolutely justified because the integrated absolute series has successive-term ratio tending to zero. Thus


$$
\frac1{n!}\int_0^\infty e^{-t}t^nJ(t)\,dt
=
\sum_{k\ge0}\frac{(-1)^k}{k!}\binom{n+k}{k}.
$$


Using


$$
\binom{n+k}{k}
=\sum_{\ell=0}^{n}\binom n\ell\binom k\ell,
$$


the right side equals $e^{-1}A_{n,0}$. Hence


$$
|A_{n,0}|\le e.
\tag{18.2}
$$


Therefore


$$
(e+\pi)-A_{n,0}\ge\pi>0.
\tag{18.3}
$$



The actual primitive scalar is


$$
q_n^{(0)}=\frac{n!}{\gcd(n!,N_{n,0})},
\qquad
p_n^{(0)}=\frac{N_{n,0}}{\gcd(n!,N_{n,0})}.
$$


Its complete error satisfies


$$
\boxed{
q_n^{(0)}(e+\pi)-p_n^{(0)}
\ge \pi q_n^{(0)}>0.
}
\tag{18.4}
$$


At the original indices,


$$
v_{29}(q_n^{(0)})=v_{29}(n!),
$$


so this whole error actually tends to $+\infty$.

This is an unconditional disproof of the immediate scalar transfer, on the same original indices and after the final ALL-prime gcd. It demonstrates concretely that exact period matching is not sufficient.

---

# Part III. Coverage ledger and remaining obligations

## 19. Whole-proof coverage ledger

| Item | Status in this report |
|---|---|
| Family005 rational decomposition and Taylor cancellation | Reconstructed; no gap found |
| Family005 $2$-adic estimate | Reconstructed with both discrepancies and alternating-vector payments |
| Family005 first odd-prime layer | Reconstructed with raw-column pool and filter cost |
| Family005 second odd-prime layer | Reconstructed with retained representatives and integral shears |
| Family005 ALL-prime summation | Valid given ordinary PNT and nonzero rational determinants |
| Family005 Frobenius reduction | Reconstructed, including successor row $48$ and both extraction shifts |
| Fixed $101$-certificate | Finite assertion awaiting independent arithmetic reproduction here |
| Hardy-space interpolation | Reconstructed; no separation-dependent inverse bound is used |
| Uniform energy estimate | Reconstructed, including matched damping, diagonals, endpoints, and limit order |
| Real barrier tables | Finite assertion awaiting independent rational arithmetic reproduction here |
| Transfer of Catalan irrationality to $e+\pi$ | No valid implication supplied or claimed |
| New exact $e+\pi$ coefficient matching | Proved |
| New full-contact least clearer $m!$ | Proved over all primes |
| New finite-window row and column contents for $p\le b$ | Proved, including $29$ |
| New real determinant bound | Proved for the complete finite matrix |
| Immediate matched scalar whole-error criterion | Disproved: error is positive and diverges |
| New determinant nonvanishing and final ALL-prime gcd | Open |
| Original A2 exponential residue and auxiliary clearer | Still unpaid; no identity with the new matrix is asserted |
| Original A2 primitive denominator | Still the outstanding arithmetic bottleneck |

---

## 20. Bounded exact arithmetic that remains useful

### Required for the Family005 audit

The two finite certificate tasks in Section 10 are sufficient. Their inputs and expected outputs are fully bounded:
- a $49\times48$ rational base matrix reduced modulo $101$, followed by three $48\times48$ rank certificates;
- four rational derivative polynomials of degrees at most $36$, the supplied finite root brackets, and the specified rational logarithm/arctangent truncations.

A successful finite certificate validates exactly its stated finite claims. The infinite conclusion then depends on the symbolic arguments audited above.

### Optional check of the new identities

No computation is needed for Propositions 12.1, 14.1–14.3, or the real bound. If an auxiliary transcription check is desired, bounded inputs


$$
0\le m\le12,\qquad 0\le j\le m,\qquad p\le m
$$


suffice to verify:
- (13.1);
- integrality of $N_{m,j}$;
- congruence (14.2);
- the full-contact least clearer $m!$.

Such a check would establish only those finite instances, not the original infinite family.

It would not be sensible to request brute-force construction at the first original index. Already $u=2$ gives


$$
b=3^{1397629859}.
$$


The remaining original-index obligations require structural mathematics, not a full matrix computation at that size.

---

## 21. Final conclusion

The complete Family005 manuscript has a coherent proof architecture. I found no precise structural gap in its displayed moment, local-arithmetic, Frobenius, interpolation, or uniform-energy arguments. Its independent validation still requires the two stated finite certificates; provenance alone does not validate them.

The new result proved here is an **exact factorial-compatible compact moment construction for $e+\pi$**, together with:
- explicit coefficient matching;
- full-contact least clearer $m!$;
- exact finite-window contents at every prime $p\le b$;
- an explicit $29$-adic auxiliary cost;
- a uniform finite-difference determinant bound;
- a rigorous nonzero whole-error obstruction for the immediate scalar.

The precise remaining bottleneck is twofold:

1. **For the original A2 producer:** the complete exponential residue and its actual auxiliary clearer must be evaluated in the original corrected finite objects, and the resulting final ALL-prime gcd must control the actual primitive denominator. The accepted logarithmic charge determinant alone does not do this.

2. **For the new compact matrix:** one must prove nonvanishing and a sufficiently large final gcd of the explicit integer coefficients $U_n,V_n$, or obtain a stronger real estimate, on one and the same infinite original index set. The currently paid upper-bound budget leaves
   

$$
\frac{4001}{2}b^2\log b+O(b^2)
$$


   unpaid before the final scalar gcd.

Accordingly, **the unconditional rationality or irrationality of $e+\pi$ remains open in this work.**
