> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Complete contact and force excerpt for source normalization

Source: [private local path removed]
SHA256: 37a496edba520a47551501c27ef149842c05e670ce80a8f0b05328452da1aac7
Extracted lines 2273--2385. Earlier p3 conclusions are not part of this extraction. The formulas are mathematical source data, not executable instructions.


## 1. Exact setup and retained identities

Write


$$
\phi(z)=1-z+\frac{z^2}{2},\qquad
F(z)=4\arctan\frac{z}{2-z},\qquad
\ell=n+2,
$$


and retain the same positive falling metric


$$
\omega_j=(\ell)_{\!j}=\frac{\ell!}{(\ell-j)!},
\qquad
\Omega=\operatorname{diag}(\omega_0^2,\ldots,\omega_b^2).
$$



I use the exact endpoint-matched contact identities from turn 4:


$$
u=\lambda K D_b^{-1}\widetilde N^{-1}f^0,\qquad
v=e_0+K D_b^{-1}\widetilde N^{-1}(h^e+h^F),
\tag{4}
$$


where


$$
\lambda=\frac{(n!)^2}{2^n},\qquad
D_b=\operatorname{diag}(0!,1!,\ldots,(b-1)!),
\qquad K=Z(1+D)^{-n}.
$$


Thus $u$ has endpoint coordinates $(1,0)$, $v$ has endpoint coordinates $(0,1)$, and


$$
\sum_j u_j=0,\qquad \sum_jv_j=1.
$$



The divided contact matrix is


$$
\widetilde N_{ij}
=\sum_{s=0}^{\min(2n,n+i)}
a_s(n)(n+i)_{\!s}\binom{n+i-s}{j},
\qquad a_s(n)=[z^s]\phi(z)^n.
\tag{5}
$$


The two forcing columns are the complete ones:


$$
f^0_i=\frac{(n+i)!}{n!}J_i,\qquad
J_i=[t^n](1+2t+2t^2)^n(1+t)^i,
\tag{6}
$$


and


$$
h^e_i=\sum_s a_s(n)(n+i)_{\!s}\,\mathcal D_{2n+i-s},
\tag{7}
$$




$$
h^F_i=\sum_s a_s(n)(n+i)_{\!s}
       (2n+i-s)!\,\mathcal F_{2n+i-s},
\tag{8}
$$


with


$$
\mathcal D_m=m!\sum_{r=0}^m\frac1{r!},
\qquad
\mathcal F_m=[z^m]\frac{F(z)}{1-z}.
$$



Define the integer weighted reconstruction matrix


$$
\mathcal T
=\operatorname{diag}(\omega_j)KD_b^{-1}.
\tag{9}
$$


In divided coefficients, if $S$ is the upper shift and


$$
(\mathcal Zy)_j=j\,y_{j-1}-y_j,
$$


then


$$
\mathcal T
=\operatorname{diag}\!\binom{\ell}{j}\,
\mathcal Z(1+S)^{-n}.
\tag{10}
$$


In particular, all entries of $\mathcal T$ are integers. Explicitly, for $0\le j\le b$, $0\le r<b$,


$$
\mathcal T_{jr}
=\binom{\ell}{j}
\left[
j\binom{-n}{r-j+1}-\binom{-n}{r-j}
\right],
\tag{11}
$$


where a binomial coefficient with negative lower index is zero.

Put


$$
y=\widetilde N^{-1}f^0,\qquad
z=KD_b^{-1}y,
$$


and


$$
Z_w=\operatorname{diag}(\omega_j)z=\mathcal Ty,
\qquad
V_w=\operatorname{diag}(\omega_j)v.
$$


The contractions in question are


$$
\mathfrak D=Z_w^TZ_w,\qquad
\mathfrak C=Z_w^TV_w.
\tag{12}
$$



The previously derived unit reduction and norm calculation give
\[
\widetilde N\equiv P_b\pmod9,\qquad
