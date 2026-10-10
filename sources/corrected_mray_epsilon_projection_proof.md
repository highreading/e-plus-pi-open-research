> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Corrected m-ray windows: exact epsilon reflection and pole projection

This fragment supplies a finite exact proof of the epsilon-independence and
the two $\Lambda$ identities for the corrected A/B Cartier windows.  It does
not prove the remaining fresh-prime coprimality statement: the resulting
pair is exactly the already-known $(\Lambda_1,\Lambda_2)$ pair.

## 1. Uniform coefficient-section interpolants

Put



$$
N=10m+3,\qquad K=4m+2,\qquad M=4m+3,\qquad d=6m+9
$$



and



$$
G_m(z)=\frac{(1-z)^{10m+3}}{(1-z^4)^{4m+3}}
       =\frac{(1-z)^{6m}}
       {\{(1+z)(1+z^2)\}^{4m+3}}.
$$



Thus



$$
G_m(1/z)=z^dG_m(z).                                      \tag{1.1}
$$



For $\epsilon\in\{1,3\}$ and an integer $R$, define the exact rational
section interpolant



$$
T_\epsilon(R)=
 \sum_{\substack{0\le j\le N\\j\equiv\epsilon-R\ (4)}}
 (-1)^j\binom Nj
 \binom{(16m+8-R-j)/4}{K}.                               \tag{1.2}
$$



For $1\leq R\leq d-1$, every prime $p>6m$ with
$p\equiv\epsilon\pmod4$ reduces (1.2) modulo $p$ to the coefficient
$[z^{p-R}]G_m$; this includes the relevant cases where the displayed
exponent is negative, when the reduction is zero.  Equivalently, in this
range (1.2) is the value at formal $p=0$ of the coefficient
quasipolynomial on the congruence class $p\equiv\epsilon\pmod4$.

Since $K$ is even,



$$
\binom{K-(R+j)/4}{K}
 =\binom{(R+j)/4-1}{K}.                                  \tag{1.3}
$$



This form makes the reflection transparent.

## 2. Exact epsilon-difference reflection

Define



$$
\Delta_R=T_1(R)-T_3(R).
$$



For every integer $R$ with $1\leq R\leq d-1$, one has



$$
\boxed{\Delta_R=\Delta_{d-R}.}                          \tag{2.1}
$$



Indeed, write the difference of the two residue-class indicators as



$$
\chi_R(j)=
 1_{j\equiv1-R\ (4)}-1_{j\equiv3-R\ (4)}.
$$



In the sum for $\Delta_{d-R}$, substitute $j\mapsto N-j$.  Because



$$
N+d=16m+12=4(K+1),
$$



the generalized binomial in (1.3) is carried to



$$
\binom{K-(R+j)/4}{K}
 =\binom{(R+j)/4-1}{K}.
$$



Also, $N$ is odd, so $(-1)^{N-j}=-(-1)^j$, while
$\chi_{d-R}(N-j)=-\chi_R(j)$.  The two minus signs cancel, proving
(2.1).

The corrected obstruction forms are



$$
D_1^{(\epsilon)}=T_\epsilon(6m+1)-T_\epsilon(8),        \tag{2.2}
$$





$$
D_2^{(\epsilon)}=
 \sum_{R=6m+2}^{6m+4}T_\epsilon(R)
 -\sum_{R=5}^{7}T_\epsilon(R).                           \tag{2.3}
$$



Since $d-(6m+1)=8$ and



$$
\{d-(6m+2),d-(6m+3),d-(6m+4)\}=\{7,6,5\},
$$



(2.1) proves the exact rational identities



$$
\boxed{D_i^{(1)}=D_i^{(3)}\quad(i=1,2).}                \tag{2.4}
$$



This proves epsilon-independence without an infinitude-of-primes
argument.

## 3. Projection to the pole at $z=-1$

The poles of $G_m$ are $-1,i,-i$, each of order $M$.  In the local
coordinate $w=1+z$, put



$$
H_m(w)=w^MG_m(w-1)
 =\frac{(2-w)^{6m}}{(w^2-2w+2)^M}.                       \tag{3.1}
$$



For completeness, write the partial fractions as



$$
G_m(z)=\sum_{\alpha\in\{-1,i,-i\}}\sum_{k=1}^M
 a_{\alpha,k}(1-z/\alpha)^{-k}.
$$



On the congruence class $p\equiv\epsilon\pmod4$, the contribution of
one summand to $[z^{p-R}]G_m$ is



$$
a_{\alpha,k}\alpha^{R-p}
 \binom{p-R+k-1}{k-1}.
$$



Its formal section value at $p=0$ is therefore



$$
a_{\alpha,k}\alpha^{R-\epsilon}
 \binom{k-R-1}{k-1}.                              \tag{3.2a}
$$



The average $(T_1(R)+T_3(R))/2$ kills the principal parts at $i$ and
$-i$: after the common $\alpha^R$ factor in (3.2a), their phase
factors average to



$$
\frac{i^{-1}+i^{-3}}2=0,
 \qquad
 \frac{(-i)^{-1}+(-i)^{-3}}2=0.
$$



At $-1$, both odd epsilon values give the phase $-1$.  Since
$a_{-1,k}=[w^{M-k}]H_m(w)$, summing (3.2a) and using



$$
\binom{k-R-1}{k-1}=(-1)^{k-1}\binom{R-1}{k-1}
$$



gives the exact pole-projection formula



$$
\Phi_R:=\frac{T_1(R)+T_3(R)}2
 =-(-1)^R[w^{M-1}]H_m(w)(1-w)^{R-1}.                    \tag{3.2}
$$



Combining (2.4) and (3.2), with $K=M-1$, yields



$$
\boxed{
 D_1=[w^K]H_m(w)\bigl((1-w)^{6m}+(1-w)^7\bigr),}       \tag{3.3}
$$



and



$$
\boxed{
 D_2=-[w^K]H_m(w)
 \bigl((1-w)^{6m+1}+(1-w)^4\bigr)(1-w+w^2).}           \tag{3.4}
$$



## 4. Exact identification with $\Lambda_2$ and $\Lambda_1$

Use the Cayley substitution



$$
w=\frac{2t}{1+t}.
$$



Coefficient extraction transforms as



$$
[w^K]F(w)
 =2^{-K}[t^K](1+t)^{K-1}F\!\left(\frac{2t}{1+t}\right). \tag{4.1}
$$



Moreover,



$$
2-w=\frac2{1+t},\qquad
 1-w=\frac{1-t}{1+t},\qquad
 w^2-2w+2=\frac{2(1+t^2)}{(1+t)^2}.                    \tag{4.2}
$$



Applying (4.1)--(4.2) to (3.3) gives



$$
D_1=2^{-2m-5}[t^K]
 \frac{(1-t)^{6m}(1+t)^7+(1+t)^{6m}(1-t)^7}
 {(1+t^2)^M}.                                           \tag{4.3}
$$



The two summands are interchanged by $t\mapsto-t$, and $K$ is even.
Therefore



$$
\boxed{
 D_1=2^{-2m-4}\Lambda_2,\qquad
 \Lambda_2=[t^{4m+2}]
 \frac{(1-t)^{6m}(1+t)^7}{(1+t^2)^{4m+3}}.}            \tag{4.4}
$$



For the sum of (3.3) and (3.4), take the even part after the same
substitution.  If



$$
F(t)=(1-t)^{6m}(1+t)^4,
$$



the numerator from one member of each reflected pair is



$$
F(t)\bigl((1+t)^3-(1+3t^2)(1-t)\bigr)
 =4t(1+t^2)F(t).                                        \tag{4.5}
$$



Consequently



$$
\boxed{
 D_1+D_2=2^{-2m-2}\Lambda_1,\qquad
 \Lambda_1=[t^{4m+1}]
 \frac{(1-t)^{6m}(1+t)^4}{(1+t^2)^{4m+2}}.}            \tag{4.6}
$$



Thus the corrected A/B obstruction is exactly the old
$(\Lambda_2,\Lambda_1)$ obstruction in different coordinates.  The proof
repairs the section/reflection error and explains epsilon-independence,
but it supplies no new Bezout or coprimality theorem.
