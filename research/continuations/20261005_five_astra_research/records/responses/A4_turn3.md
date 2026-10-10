> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 review: normalization passes; a scalar-transfer dependency remains; the full Gram bound is unconditional

The direct determinant bound requested in the assignment is valid, with exactly the proposed normalization. It removes the signed spectral gap altogether.

For matched $b=4$, the row and contraction normalizations pass. The four-prime certificate, **together with the scalar transfer assertion used by A2**, yields the full-family exclusion with rate gap greater than $0.30319406432$, retaining the final endpoint gcd and the whole nonzero error. There is, however, a documentary gap in an independent proof of that implication: the supplied sources assert, but do not supply a proof of, the five-coordinate scalar transfer theorem. I distinguish this dependency from the now-settled finite certificate.

The moving-pole rank and cancellation argument passes on its stated domain. Its separate claim of exact dyadic depth $n+2$, and hence its distinct-center nonvanishing argument, is not supplied by the dyadic source included here.

## 1. Matched $b=4$: differential and integral normalization

### 1.1 Differential row identity: PASS

Write $F=\mathscr F_k$. Using A2’s differential equation, differentiation of $T_kF$ reduces to


$$
(T_kF)'=(k+1)B_kF.
$$


There is a useful way to check the next step without conflating the two adjacent operators. Since


$$
B_{k+1}=B_k-D+1,
$$


direct differentiation gives, for any polynomial $G$,


$$
(B_{k+1}G)'=(B_k-1)G'+2G.
$$


Apply this with $G=\mathscr F_{k+1}=T_kF$, and use $G'=(k+1)B_kF$. Thus


$$
\frac{\mathscr F_{k+2}''}{k+2}
=(k+1)(B_k^2-B_k)F+2T_kF.
$$


Reducing the fourth and third derivatives using the differential equation and its derivative gives A2’s three displayed coefficients. In particular, the coefficient of $F''$ becomes


$$
(k+1)\bigl(2x^2-(2k+3)x\bigr)+x^2
=(2k+3)x(x-k-1).
$$


The coefficients of $F'$ and $F$ similarly give


$$
\frac{\mathscr F_{k+2}''}{k+2}
=(k+1)^3F+(2k+3)C_kF.
$$


Consequently, with $k=n+1$,


$$
R_3=(n+2)^3R_1+(2n+5)R_{\rm new}.
$$



The important arithmetic point is valid: $C_k$ has integral polynomial coefficients at every integer $k$, so $R_{\rm new}$ is an integral row. There is no division by $2n+5$ in a residue field.

### 1.2 Factor $12$: PASS

Use the simultaneous column transformation


$$
(C_0,C_1,C_2,C_3,C_4)
\longmapsto
(C_0,C_1-C_0,C_2-C_1,C_3-C_2,C_4-C_3).
$$


Its determinant is one. For a high jet row of a polynomial $P$, the last four entries become


$$
(P'-P)^{(j)}(1),\qquad 0\le j\le3.
$$


For the two cumulative rows they become derivatives of $\mathscr F_n$ and $F'/k$, respectively. These are integral polynomials, including $F'/k$ by the supplied derivative divisibility lemma.

The $j$-th such column is divisible by $j!$. Hence


$$
(\sigma,\chi,\kappa)
=12(2n+5)(\widehat\sigma,\widehat\chi,\widehat\kappa)
$$


over the integers. This includes the singular residue classes $p\mid2n+5$.

### 1.3 Global contraction normalization: PASS

Let


$$
d_n=\gcd(|\widehat\sigma_n|,|\widehat\chi_n|,
                         |\widehat\kappa_n|).
$$


On the nonzero-triple domain the actual primitive contractions are the hatted contractions divided by $d_n$. Dividing individual high-row contents and maximal-minor content first gives the same primitive triple: each such division scales all three contractions by the same rational factor.

If


$$
\widehat V_n
=\widehat\sigma_n\mathcal A_n
-\widehat\chi_n\mathcal B_n-\widehat\kappa_n,
$$


then


$$
V_n^*=\widehat V_n/d_n.
$$


Since $\mathcal A_n,\mathcal B_n\in\mathbb Z[1/2]$, a unit value of $\widehat V_n$ at an odd prime forces $p\nmid d_n$. In that case $V_n^*$ is also a unit. No periodicity of the globally primitive triple is needed.

## 2. Precisely what remains in the normalized transfer audit

The integral replacement-row formulas express the hatted contractions as fixed polynomials in


$$
n,h_n,u_n,v_n
$$


with coefficients in $\mathbb Z[1/6]$, and $\widehat V_n$ as such a polynomial in the five scalar coordinates.

Therefore, **if** those coordinates satisfy


$$
m\equiv n\pmod{p^a}
\quad\Longrightarrow\quad
(h,u,v,\mathcal A,\mathcal M)_m
\equiv(h,u,v,\mathcal A,\mathcal M)_n\pmod{p^a},
\tag{2.1}
$$


then A2’s normalized transfer follows at every $p\ge5$, with no loss of precision at $p\mid2n+5$.

This deduction passes. But a proof of (2.1) is not present in the supplied complete sources. A2 calls it the “proved scalar transfer”; the certificate itself labels normalized transfer a written dependency. In particular, no explicit definition or recurrence for the scalar $\mathcal M_n$, accompanied by the proof of its transfer, is supplied.

Polynomial dependence alone does not prove (2.1). Nor do the 46 finite rows prove it.

**Audit disposition:** the normalization part of transfer passes; the underlying scalar-transfer theorem remains an inherited, not independently verified, dependency. The full $b=4$ exclusion needs only the following much narrower statement:


$$
\widehat V_{n+p}\equiv\widehat V_n\pmod p,
\qquad n\ge0,\quad p\in\{5,11,13,17\}.
\tag{2.2}
$$


All-depth transfer and root lifting are unnecessary for this particular exclusion.

## 3. Exact full-family $b=4$ exclusion, conditional only on that transfer dependency

Let


$$
\mathcal P=\{5,11,13,17\}.
$$


The supplied independently regenerated certificate states that $\widehat V_r$ is a unit at every residue $0\le r<p$, for every $p\in\mathcal P$. Assuming (2.2), it follows that


$$
v_p(V_n^*)=0\qquad(n\ge0,\ p\in\mathcal P).
\tag{3.1}
$$



For $n\ge4$, retain the complete endpoint numerator


$$
T_n=Q_n^*+\frac{2^{n+1}}{(n!)^2}V_n^*,
\qquad \frac{X_n}{Y_n}=\frac{T_n}{D_n^*}.
$$


Take any valid positive integer clearer $\Lambda_n$, for example the conservative clearer in the supplied growing-degree arithmetic source, and put


$$
N_n=\Lambda_nT_n,\quad Z_n=\Lambda_nD_n^*,\quad
g_n=\gcd(|N_n|,|Z_n|).
$$


The actual center is


$$
c_n=-X_n/Y_n=p_n/q_n,\qquad
q_n=\frac{|Z_n|}{g_n}.
\tag{3.2}
$$



For each fixed $p\in\mathcal P$, eventually


$$
2v_p(n!)>\lfloor\log_p(n+1)\rfloor.
$$


The moment bound $v_p(Q_n^*)\ge-\lfloor\log_p(n+1)\rfloor$, combined with (3.1), then gives strict separation of the two complete numerator terms:


$$
v_p(T_n)=-2v_p(n!).
$$


In particular $T_n\ne0$, and actual reduction gives


$$
v_p(q_n)=2v_p(n!)+v_p(D_n^*)\ge2v_p(n!).
\tag{3.3}
$$


This is a statement after the final endpoint gcd, not about a nominal factorial denominator.

Legendre’s formula yields


$$
\log q_n\ge
2\sum_{p\in\mathcal P}v_p(n!)\log p
=W_4n-O(\log n),
\quad
W_4=2\sum_{p\in\mathcal P}\frac{\log p}{p-1}.
\tag{3.4}
$$


The supplied fixed-$b$ theorem applies to this same endpoint-matched system at $b=4$. It gives eventual endpoint nonvanishing and the complete evaluated error


$$
S-c_n=(-1)^n\epsilon_n(\sqrt2-1)^4(1+o(1)),
\qquad
\log\epsilon_n=-\tau n+o(n),
$$


where $S=e+\pi$ and $\tau=2\log(1+\sqrt2)$. This error is eventually nonzero. Therefore


$$
\boxed{
\liminf_{n\to\infty}
\frac1n\log|q_nS-p_n|
\ge W_4-\tau>0.30319406432.
}
\tag{3.5}
$$



**Precise pass/fail:** the infinite implication (3.1)–(3.5), including global normalization, final gcd, nonvanishing and whole error, passes. An unconditional independent certification of the complete exclusion is not yet justified from this source packet because (2.2) has not been proved here. No repetition of the finite certificate is needed.

## 4. Moving-pole theorem: PASS, with a separate nonvanishing correction

For $n=4^j+1$, $j\ge1$, and $3n<p\le4n-3$, the rank argument is sound.

If $d=\deg(Q\bmod p)$ and $D=(p+1)/2-d$, then


$$
(pR)_{ij}=0\pmod p\quad(i+j<D),
$$


and its first possible nonzero anti-diagonal has value $4Q_d$. The trailing block therefore has rank


$$
h=\max(0,n+d-(p+1)/2).
$$


Primitivity ensures $Q\bmod p\ne0$, so degree drops are handled correctly.

The endpoint row is genuinely outside this pole block:


$$
2(n+r)-1=3n-2<p.
$$


The change to $1,y^i-(-1)^i$ leaves the pole residue unchanged. Thus the endpoint lies in the zero part for every index and prime in the domain, not merely at $n=5,p=17$.

With $s=k-h$, the integral Schur complement gives


$$
A=p^s\det\mathcal D\det\mathcal E,\qquad
B=p^s(\ell/p)w\det\mathcal D\det\mathcal E_0.
$$


Consequently


$$
v_p(g)\ge s\ge\frac{p-3n+2}{2},
$$


and, on $B\ne0$, the displayed residual final-$q$ formula is exact. Unit basis changes preserve these local valuations.

Finally, partial summation from $\vartheta(x)=x+o(x)$ gives


$$
\log\mathfrak C_n=\frac14n^2+o(n^2).
$$


The $O(1)$ displacement of the upper endpoint contributes only $O(n\log n)=o(n^2)$.

**Correction:** the included dyadic source proves


$$
v_2(q_{\rm center})=2+v_2(\eta)
$$


on this regular family and explicitly leaves $v_2(\eta)$ unresolved. It does not prove the $n+2$ depth asserted later by A1. Thus the moving-pole cancellation passes, but the distinct-center argument based on those exact depths cannot be certified from these sources.

## 5. New direct full absolute Gram bound

Set $k=r+1$, and use exactly the unimodular endpoint basis


$$
f_0=1,\qquad f_i=y^i-(-1)^i,\quad1\le i\le r.
$$


Define the full signed and absolute compact Gram matrices


$$
J_{ij}=\int_0^1 f_i(x^2)f_j(x^2)Q(x^2)
\left(e^x+\frac4{1+x^2}\right)\,dx,
$$




$$
(G_{\rm full})_{ij}=\int_0^1 f_i(x^2)f_j(x^2)|Q(x^2)|
\left(e^x+\frac4{1+x^2}\right)\,dx.
$$


No positivity of $Q$ is assumed.

In this basis,


$$
J=R_{\rm end}+Sw\,e_0e_0^T.
$$


By the precise bordered normalization,


$$
\ell^k\det J=A+BS.
$$


Hence, on $B\ne0$,


$$
\boxed{
q|S-c|=\frac{|A+BS|}{g}
=\frac{\ell^{r+1}}{g}|\det J|.
}
\tag{5.1}
$$


This identity does not require estimating $H^{-1}$, or even constructing the stationary polynomial.

Andréief gives


$$
\det J=\frac1{k!}\int_{[0,1]^k}
\prod_{i<j}(x_j^2-x_i^2)^2
\prod_{j=1}^k Q(x_j^2)
\left(e^{x_j}+\frac4{1+x_j^2}\right)\,dx_j.
$$


The endpoint basis has determinant-one transition from monomials, so its determinant of evaluations is the ordinary Vandermonde. Taking absolute values under the integral gives exactly


$$
|\det J|\le\det G_{\rm full}.
$$


Therefore


$$
\boxed{
q|S-c|\le\frac{\ell^{r+1}}{g}\det G_{\rm full}.
}
\tag{5.2}
$$


The signed determinant and spectral gap have disappeared completely.

## 6. An explicit asymptotic bound and the remaining content budget

Let


$$
M_n=\max_{0\le y\le1}|Q_n(y)|>0.
$$


Since $e^x+4/(1+x^2)<7$,


$$
\det G_{\rm full}\le(7M_n)^kD_k,
$$


where


$$
D_k=\det\left(\frac1{2i+2j+1}\right)_{0\le i,j<k}
=\frac{\prod_{i<j}4(j-i)^2}
       {\prod_{i,j}(2i+2j+1)}.
\tag{6.1}
$$


This is a full-size determinant bound: the previous extra $4^r$ from factoring endpoint-vanishing polynomials is unnecessary.

The Cauchy product, or its consecutive quotient


$$
\frac{D_{k+1}}{D_k}
=\frac{4^k(k!)^2}
{(4k+1)\prod_{i=0}^{k-1}(2i+2k+1)^2},
$$


gives by Stirling’s formula


$$
\log D_k=-(\log4)k^2+O(k\log k).
\tag{6.2}
$$


Thus the new primitive-error estimate is


$$
\boxed{
q|S-c|\le \frac{\ell^k(7M_n)^kD_k}{g}.
}
\tag{6.3}
$$



Write $g=\mathfrak C_n g_n'$ in the fixed primitive-$Q$ normalization. Since


$$
\log\ell=4n+o(n),\qquad k=(n+1)/2,
$$


(6.3) and the moving-pole divisor imply


$$
\log\!\left(\frac{\ell^k(7M_n)^kD_k}{g}\right)
\le
k\log M_n+
\left(\frac74-\frac{\log2}{2}\right)n^2
-\log g_n'+o(n^2).
\tag{6.4}
$$


The explicit quadratic coefficient is approximately $1.40342640972$, and is positive.

This sharply identifies why the present unconditional bounds do not yet produce small primitive errors: even after the new common-content divisor and the Vandermonde gain, the bound retains


$$
k\log M_n+1.40342640972\,n^2
$$


before further content cancellation. An estimate for compact size and additional content must overcome this amount. There is no unknown spectral parameter left.

All these expressions have the correct scaling. Multiplying $Q$ by a positive integer $a$ multiplies $A,B,g$ by $a^k$, and $\det G_{\rm full}$ by $a^k$; both sides of (5.2) are unchanged.

## Concluding ledger

### (1) New result and proof status

**Proved here:** the exact-scale bound


$$
q|S-c|\le\ell^{r+1}\det(G_{\rm full})/g,
$$


and its explicit Cauchy/Vandermonde bound (6.3)–(6.4), without assuming $Q$ positive.

**Review passes:** A2’s differential row replacement, integral $12(2n+5)$ normalization, global contraction normalization, and A1’s moving-pole rank, endpoint placement, Schur cancellation and PNT divisor.

**Conditional conclusion:** the full matched-$b=4$ exclusion with gap $>0.30319406432$ follows from the supplied finite certificate and the still-unreviewed scalar transfer dependency.

### (2) Exact remaining bottleneck

For matched $b=4$, supply a written proof of the narrow four-prime transfer (2.2); no further residue certificate is needed.

For the weighted family, control the explicit residual budget in (6.4), and establish an unbounded domain with $B\ne0$ and $A+BS\ne0$. The determinant inequality itself proves neither nonvanishing nor irrationality.

The arithmetic nature of $e+\pi$ remains undecided.

### (3) Computation request

**None.** The outstanding matched-$b=4$ task is a written infinite transfer proof, not another finite computation.
