> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 audit: upstream weighted identification closed; the two new lifts pass with explicit scope qualifications

The supplied upstream proofs resolve the identification dependencies isolated in A4 turn 5. In particular, the affine branches are now identified with the **actual ordinary moments**, and the coupled inverse-removal and half-symmetric quadratic calculations identify the scalar reconstructed by the closure certificates with the **actual normalized endpoint**.

My conclusions are:

| Claim | Audit conclusion |
|---|---|
| Regular weighted dyadic endpoint theorem | **PASS**, using the supplied exact finite coefficient/state certificates together with the now-audited upstream identifications |
| A1 first radical lift and primitive leading $3$-depth | **PASS** |
| A1 uniform actual odd-denominator law | **Not proved or implied** |
| A3 complete signed real-moment transform | **PASS**, including the adjacent exponential endpoint correction |
| A3 same-last-index upper-rate improvement | **PASS**, on its stated proportional-order range |
| A3 signed lower rate or primitive shrinking | **Not proved or implied** |
| Primorial consequence | **PASS as a lower bound for the actual denominator only** |

“PASS using certificates” does not mean that I executed their computations. It means that the paper identifications and finite-certificate implications are valid; the supplied coordinator-checked coefficient equalities provide the finite arithmetic inputs. Hashes alone would not provide those inputs.

I also prove a new local factorization lemma for the **actual primitive weighted polynomial**. It isolates a simple $3$-adic root near $-1$, whose displacement carries exactly the unresolved endpoint depth, and a separate root of valuation $-1$.

## 1. Weighted upstream identification

### 1.1 The affine branches are the actual moments

Let


$$
b_r=A\!\left(\left(\frac{x^2+1}{2}\right)^r\right).
$$


The supplied recurrence is


$$
b_{r+1}=(r+1)(2r+1)b_r-r(r+1)b_{r-1}-r.
$$


Putting $u=2t$, its even step is


$$
b_u=(-u+2u^2)b_{u-1}+(u-u^2)b_{u-2}+1-u.
$$


Substitution into the next step gives exactly


$$
\binom{b_{u+1}}{b_u}
=M(u)\binom{b_{u-1}}{b_{u-2}}+c(u),
$$


with every entry of $M,c$ displayed in the source. Thus the matrix used in the branch code is not an independently chosen interpolation model.

Each length-$a$ product contains


$$
u(u-2)\cdots(u-2a+2).
$$


On $u\in2\mathbb Z_2$, its valuation is at least $a+v_2(a!)$. For a fixed ordinary coefficient of degree $\ell$, its valuation is at least $\max(0,a-\ell)$. Consequently:

* the product expansion converges uniformly on the parity disk;
* it converges coefficientwise to integral ordinary series;
* substitution at nonnegative integer arguments reproduces the original recurrence, because the product terminates at $M(0)=0$.

These facts establish the required actual-moment identification.

As a further normalization check, reduction of the displayed matrix gives


$$
\bar M=
\begin{pmatrix}
0&u+u^3\\
u&u+u^2
\end{pmatrix},
\qquad
\bar c=\binom{1+u+u^2}{1+u}.
$$


Solving $(I-\bar M)\bar F=\bar c$ yields


$$
\bar E=\frac{1+u^2+u^3}{1+u+u^4},
\qquad
\bar O=\frac{1+u+u^3}{1+u+u^4},
$$


with precisely the stated branch order.

The ordinary-series construction also justifies


$$
\frac{\Delta_2^d b_r}{2^d d!}\in\mathbb Z_2
$$


and its Taylor-coefficient residue. This is the necessary link from ordinary branches to the normalized Gram entries.

### 1.2 The modulo-eight branch construction and supplied code agree

For an integral ordinary series,


$$
F(u-2)=F-2F'+2F''\pmod8.
$$


The omitted Taylor terms are $8$-divisible coefficientwise. With


$$
Q=(I-M)^{-1}c,\qquad R=(I-M)^{-1}M,
$$


iteration gives


$$
F=Q-2RQ'+4R(RQ')'+2RQ''\pmod8.
$$



The code implements this formula with the correct denominator powers. If $q/D$ is a component of $Q$, then it constructs


$$
Q'=\frac{q'D-qD'}{D^2},
$$


then the numerator of $RQ'$ over $D^3$, its derivative over $D^4$, and finally $R(RQ')'$ over $D^5$. The separate $2RQ''$ term is retained.

The normalized finite-difference conversion is also correct:


$$
\begin{aligned}
\rho_d(c)={}&t_d
+2\left((d+1)c+\binom{d+1}{2}\right)t_{d+1}\\
&+4\left(
\binom{d+2}{2}c^2
+(d+2)c\binom{d+1}{2}
+S(d+2,d)\right)t_{d+2}\pmod8.
\end{aligned}
$$


The corrected coordinate is


$$
c=\lfloor\text{start}/2\rfloor.
$$


Thus start $2$ uses $c=1$, not $c=0$.

For the four-mode construction, the reciprocal characteristic polynomial is


$$
\lambda^4+\lambda^3+2\lambda^2-4\lambda-3,
$$


which is exactly the polynomial used by the source code. Distinct residual roots make the confluent partial-fraction reconstruction integral. The proper branch modes have an integer-valued polynomial representation of degree at most six; the displayed finite-difference conversion raises the safe bound to at most ten. Therefore cancellation of Newton coefficients $5,\ldots,10$ is a **finite algebraic certificate of an all-order degree-four identity**, not extrapolation from moment samples.

One reproducibility qualification is worth recording: the supplied script records these Newton coefficients and the order-zero defects, but does not itself assert that all the stated high coefficients and defects vanish. Those conclusions use the reported coefficient outputs. An archival implementation could add those assertions without changing the mathematics.

**Status:** the previous missing actual-branch identification is closed. No additional upstream file is needed for it.

## 2. Coupled inverse removal and scalar reconstruction

### 2.1 Reversal gives the actual binary inverse

In


$$
\mathcal A_h=\mathbb F_2[X_0,\ldots,X_{h-1}]/(X_0^2,\ldots,X_{h-1}^2),
$$


write $R$ for complementary-index reversal and


$$
g_f=\sum_{d<m}f_{m-1-d}X_d.
$$


Then


$$
H_f=R M_{g_f}.
$$


Every positive-degree element squares to zero, so


$$
g_a^2=a_{m-1}^2=1.
$$


This proves the two-member inverse


$$
\bar B^{-1}=R\bar B R.
$$


Its canonical binary lift is exactly the stated OR kernel


$$
C_{(d,s),(e,t)}
=\mathbf1_{d\operatorname{OR}e=m-1}
 f_{s,t}(2m-2-d-e).
$$



Writing $BC=I+2E$,


$$
B^{-1}=C-2CE+4CE^2
      =3C-3CBC+CBCBC\pmod8.
$$


This removes the growing inverse without imposing symmetry on $E$.

### 2.2 The commutator correction is essential and is present

The actual member difference is


$$
B_{EE}-B_{PP}=2H.
$$


Consequently the member swap does not commute with $B$ at the required precision. The supplied calculation retains this through


$$
\bar C[E,T]=\operatorname{diag}(H^r,H^r)T.
$$


Using $E^T\bar C=\bar C E$, the second-carry quadratic term becomes


$$
\bar t^{\,T}\bar C E^2\bar\omega
=v^T E\bar\omega.
$$


The diagonal contribution from $\bar C T$ is supported at both last-member coordinates. It is not zero and has not been discarded.

Since


$$
S_2=t^TCBC\omega=S_1+2t^TCE\omega,
$$


the complete quotient reduces to


$$
U=S_2-2S_1-2v^T(BC\omega-\omega)\pmod8.
$$



### 2.3 The half-symmetric expansion gives the displayed full scalar

Set $x=C\omega$, $x=x_0+2x_1$, and


$$
t=T\omega-2k.
$$


Because $C$ commutes with $T$,


$$
S_2=x^TTBx-2k^Tx-4k^TCE\omega.
$$


Moreover,


$$
TB+BT=2N.
$$


Thus


$$
x^TTBx
=x_0^TTBx_0+4x_1^TNx_0+4x_1^TTBx_1\pmod8.
$$


The last quadratic expression reduces to its diagonal over $\mathbb F_2$, producing the source’s $\delta_0$. Therefore


$$
S_2=q_0+4\ell^Tx_1-2k^Tx-4b^TE\omega,
$$


and substitution gives


$$
\boxed{
U=q_0-2S_1-2\ell^Tx_0
 +2(\ell-k)^TC\omega
 -2(b+v)^T(BC\omega-\omega)\pmod8.
}
$$



This verifies the precise identity previously missing from my audit. In particular:

* $k$ must remain modulo $4$ in its first contraction;
* the last-coordinate additions in $b+v$ remain;
* canonical XOR corrections and additive integer lifts are not confused.

### 2.4 Binary responses and their all-degree meaning

The subset formulas in the supplied proofs establish the claimed periodic responses. Their key finite-field fact can be checked directly. If $\lambda$ is a root of


$$
X^4+X+1,
$$


then $\lambda^4=\lambda+1$. The pair sums of its four conjugates are $1$ and the two roots of


$$
Z^2+Z+1.
$$


Indeed, for $s=\lambda+\lambda^2$,


$$
s^2=s+1.
$$


Hence unequal-frequency contributions have period dividing three. Equal-frequency contributions are confined to the stated boundary coordinates. This explains why the finite field evaluations prove the complete periodic identities, rather than merely suggesting them.

Combining these identities with the already-checked rational-Cartier and linear-transfer closures proves


$$
U=4\pmod8
$$


for all positive odd $h$, with $h=1,3,5$ handled by the retained complete small-state certificates and the later indices covered by the exact closures.

**Status:** the previous coupled-identification dependency is closed. The later theorem correctly supersedes the provisional stopping points in the earlier notes.

## 3. Weighted final gcd, actual denominator, and nonvanishing

On


$$
n=4^j+1,\qquad j\ge1,\qquad
m=(n-1)/2,\qquad \sigma=n-2,
$$


the established same-basis arctangent filtration makes the complete normalized rational matrix a unit perturbation of the Pascal Gram matrix. Consequently


$$
v_2(\alpha)=\gamma,\qquad
v_2(\beta)=\gamma+v_2(Q_n(-1))-2\sigma,
$$


where


$$
\gamma=k(k-1)+2\sum_{i<k}v_2(i!).
$$



The audited endpoint identification now gives


$$
v_2(P_n(0))=2\sigma+2=2n-2,
\qquad
v_2(Q_n(-1))=3n-2.
$$


For any positive odd simultaneous clearer $D$, define


$$
g=\gcd(|D\alpha|,|D\beta|),\qquad
\varepsilon=\operatorname{sgn}(\beta).
$$


Then


$$
p=-\varepsilon D\alpha/g,\qquad
q=|D\beta|/g,
$$


and


$$
\boxed{
v_2(g)=\gamma,\qquad v_2(q)=n+2.
}
$$


This is the actual reduced denominator after the entire endpoint gcd.

The whole evaluated error is


$$
\boxed{
q(e+\pi)-p
=\varepsilon\frac Dg\bigl(\alpha+\beta(e+\pi)\bigr).
}
$$


The finite valuations prove $\alpha,\beta,Q_n(-1)\ne0$. They do not alone prove that the displayed real error is nonzero at every index. However, the strictly different reduced-denominator $2$-depths make all these centers distinct. Thus at most one regular index can have zero whole error.

No odd-content estimate or shrinking assertion follows from this audit.

## 4. A1 first radical lift and primitive polynomial

### 4.1 Modulo-nine moments: PASS

The factorial formula


$$
b_s=\sum_{\ell=0}^s
\binom{s}{\ell}(-2)^{s-\ell}\frac{(s+\ell)!}{s!}
$$


reduces uniformly modulo $9$ to $\ell<6$, since six consecutive integers contain at least two factors of $3$. Its three branches are


$$
b_{3r}\equiv1+6r(r+1),\qquad
b_{3r+1}\equiv0,\qquad
b_{3r+2}\equiv4+6r(r+1)\pmod9.
$$


Substitution into


$$
e_s=4b_s+4(s+1)b_{s+1}+(s+1)(s+2)b_{s+2}
$$


gives


$$
\boxed{e_{3r}\equiv3\pmod9\quad(r\ge0).}
$$


The boundary convention for terms $\ell>s$ is legitimate: their binomial coefficient is zero, and $-2$ is a $3$-adic unit.

### 4.2 The binomial inverse and radical Schur norm: PASS

For


$$
B_M(D,E)=\binom{D+E}{D},\qquad
P_M(D,a)=\binom Da,
$$


Vandermonde gives $B_M=P_MP_M^T$. With


$$
v_a=\binom Ma,\qquad b=P_Mv,
$$


the finite alternating-binomial identity yields


$$
(P_M^{-T}v)_D
=(-1)^{M-1-D}\binom MD.
$$


Thus $B_M^{-1}b=z$ exactly over $\mathbb Q$.

For the lifted radical vector $t=(-z,1)$,


$$
t^TB_{M+1}t
=\binom{2M}{M}
-\sum_{a=0}^{M-1}\binom Ma^2
=1.
$$


The actual eliminating vector differs from this lift by a vector in $3\mathbb Z_3^{3M}$, so its quadratic correction begins at $9$. Since $e_{3r}/3\equiv1$, it follows that


$$
\boxed{\delta\equiv3\pmod9.}
$$



The mixed Schur pairing is $A_{01}$ times the same Pascal Schur norm, hence $2\pmod3$. The constant coupling cancels modulo $3$. Therefore


$$
v_3(\eta_{\rm last})=-1,\qquad
3\eta_{\rm last}\equiv2\pmod3,
\qquad
\eta_{\rm const}\in\mathbb Z_3.
$$


These conclusions hold on the stated larger domain $n=3M+2$, $M\ge1$.

### 4.3 Factoring the actual primitive polynomial: PASS, with a scope clarification

On the regular family, $N=n-1=4^j$ is a $3$-adic unit. The monic polynomial expansion gives


$$
\min_a v_3([y^a]P_n)=-1:
$$


the coefficient of degree $n-1$ contains $-N\eta_{\rm last}$, while its other contribution is integral.

Hence, for the actual primitive integer polynomial $Q_n=L_nP_n$,


$$
\boxed{v_3(L_n)=1.}
$$


Every lower factorial ratio except the last contains $N-1=3M$, and therefore


$$
3P_n\equiv h_{n-1}\pmod3.
$$


It follows that


$$
\boxed{
\bar Q_n(y)=u_j(y+1)(y-1)^{n-2},
\qquad u_j\in\mathbb F_3^\times.
}
$$



This is a factorization of the **reduction of the actual primitive polynomial**. It is not an exact factorization by $y+1$ over $\mathbb Z$; indeed $Q_n(-1)\ne0$.

The exact endpoint relation is


$$
\boxed{
v_3(Q_n(-1))
=v_3(N!)+v_3(c\xi_{\rm const}-b\xi_{\rm last}).
}
$$


It retains the coupled numerator. The $n=65$ control gives


$$
v_3(64!)=21+7+2=30,
$$


and reports coupled-numerator depth $30$, hence primitive endpoint depth $60$. This is a valid finite normalization check, not an infinite endpoint law.

The full endpoint pair remains


$$
g=\gcd(|A|,|B|),\qquad
q=|B|/g,\qquad
p=-\operatorname{sgn}(B)A/g,
$$


with


$$
q(e+\pi)-p
=\frac{\operatorname{sgn}(B)}g\bigl(A+B(e+\pi)\bigr).
$$


Neither the radical lift nor the polynomial factorization evaluates the remaining rational-arctangent determinant content in $A,B$.

## 5. New follow-on lemma: two distinct $3$-adic root mechanisms

The preceding primitive reduction permits a stronger exact local description.

### Lemma

For every regular $n=4^j+1$, the actual primitive polynomial admits a factorization in $\mathbb Z_3[y]$


$$
\boxed{
Q_n(y)=(1-s_ny)(y-a_n)W_n(y),
}
$$


where


$$
v_3(s_n)=1,\qquad a_n\equiv-1\pmod3,
$$


$W_n$ has degree $n-2$ and unit leading coefficient, and


$$
\overline{W_n}(y)=u_j(y-1)^{n-2}.
$$


Moreover,


$$
\boxed{
v_3(a_n+1)=v_3(Q_n(-1))
=v_3((n-1)!)+v_3(c\xi_{\rm const}-b\xi_{\rm last}).
}
$$



### Proof

Consider the reciprocal polynomial


$$
Q_n^*(z)=z^nQ_n(1/z).
$$


Its constant coefficient is $\operatorname{lc}Q_n$, of valuation one. Its linear coefficient is the degree-$(n-1)$ coefficient of $Q_n$, a unit by the primitive reduction. Hensel’s lemma therefore supplies a unique root $s_n\in3\mathbb Z_3$. The Taylor equation at zero gives $v_3(s_n)=1$.

Division by the monic factor $z-s_n$ is integral. Reversing the quotient yields


$$
Q_n(y)=(1-s_ny)V_n(y),
$$


where $V_n\in\mathbb Z_3[y]$ has degree $n-1$ and unit leading coefficient. Modulo $3$,


$$
\bar V_n=u_j(y+1)(y-1)^{n-2}.
$$


The root $-1$ is simple in this reduction, so a second application of Hensel gives


$$
V_n=(y-a_n)W_n
$$


with the stated properties.

At $y=-1$,


$$
Q_n(-1)=(1+s_n)(-1-a_n)W_n(-1).
$$


Both $1+s_n$ and $W_n(-1)$ are units. This proves the valuation identity. Finally, $a_n\ne-1$, because the real signed-form argument proves $Q_n(-1)\ne0$. ∎

This separates two phenomena:

* the primitive leading depth corresponds to the root $s_n^{-1}$ of valuation $-1$;
* the unresolved endpoint depth corresponds to the displacement of the simple integral root $a_n$ from $-1$.

The first radical lift settles the former but not the latter.

## 6. A3 complete real-moment transform

### 6.1 Original endpoint normalization and complete decomposition: PASS

Using the original contiguous source, the compensated denominator is


$$
J_k=\frac{\mathscr D_k}{(k!)^2},
$$


distinct from the derivative scalar also denoted $J_k$ in parts of the source. Likewise the compensated numerator is $\mathscr X_k/(k!)^2$.

Substitution into


$$
Z_k=\frac{\mathscr X_k+(e+\pi)\mathscr D_k}{(k!)^2}
$$


gives exactly A3’s decomposition into


$$
\frac{(k+1)^2C_k\varepsilon_{k+1}-2S_k\varepsilon_k}{(k!)^2}
$$


and


$$
\frac{(k+1)^2C_k\mathcal E_{k,1}
-2S_k\mathcal E_{k,0}
-2f_kH_{k+1}W_k}{(k!)^2}.
$$


The last term is necessary.

### 6.2 Both Heine branches and the adjacent exponential correction: PASS

For ordinary Legendre $Q_l$,


$$
\varepsilon_l=-2^{l+2}i^{l+1}Q_l(-i).
$$


Continuation from infinity into the lower half-plane gives


$$
\sqrt{(-i)^2-1}=-i\sqrt2,
$$


and therefore


$$
\varepsilon_l
=4(-2)^l\int_0^\infty
(1+\sqrt2\cosh v)^{-l-1}\,dv.
$$


The upper-half-plane continuation uses $+i\sqrt2$; it is the conjugate formula and gives the same real signed deficit after conjugation. Mixing these square-root choices would reverse the required phase.

The checks


$$
\varepsilon_0=\pi,\qquad \varepsilon_1=2\pi-8
$$


confirm both scale and alternating sign.

For the exponential part, the adjacent truncation is genuinely different:


$$
\mathcal E_{k,1}
=e f_{k+1}\int_0^1e^{-x}\mathcal F_{k+1}'(x)\,dx.
$$


Integration by parts gives


$$
\boxed{
\mathcal E_{k,1}
=f_{k+1}H_{k+1}(1)
+e f_{k+1}\int_0^1e^{-x}\mathcal F_{k+1}(x)\,dx.
}
$$


Thus the correction in A3 is required by the original $T^{[k]}$, not optional.

### 6.3 Degree four and full support enclosure: PASS

Expanding the original $S_k,C_k$ gives the displayed formulas


$$
\frac{S_k}{(k!)^2}
=(k+1)^2\bigl((k+1)B_0^2+B_1^2-B_0B_2\bigr)
$$


and


$$
\frac{C_k}{(k!)^2}
=(k+1)\bigl(
B_0A_0+kB_0A_1-(k+1)B_1A_0+B_1A_1-B_2A_0
\bigr).
$$


After the external factors in the arctangent contribution, the largest polynomial degree is four.

The circle variables and Heine variable satisfy


$$
v_i\in[-M,M^{-1}],\qquad
u\in[-2M^{-1},0].
$$


Since


$$
[-M,M^{-1}]^2=[-1,M^2],
$$


their product lies in


$$
[-2M,2M^{-1}].
$$


Both signs are retained. The resulting finite signed pushforward measures therefore give an actual identity


$$
\mathcal Z_k^{\rm ar}
=\sum_{h=0}^4k^h\int T^k\,d\mu_h(T).
$$



“Supported on this interval” is the correct assertion. It does **not** assert a nonzero signed density everywhere on the interval, or at either maximizing location.

### 6.4 Whole transformed upper bound and same-$N$ gain: PASS

Because $5-2M>0$, the Euler differentiation bound is uniform throughout the support:


$$
\left|\left(T\frac d{dT}\right)^h
[T^n(5+T)^m]\right|
\le C_h(N+1)^h|T|^n(5+T)^m,
\qquad h\le4.
$$


Taking total variations is legitimate. The separate factorial-small bound retains both exponential deficits and the $H_{k+1}W_k$ term. Thus A3’s bound concerns the **whole evaluated compensated numerator**, not merely its arctangent part.

The maximizing negative point is


$$
x_c=\min\!\left(2M,\frac5{1+c}\right),
$$


while the positive contribution is


$$
2M^{-1}(5+2M^{-1})^c.
$$


Both are required.

Using the inherited eventual common sign and ratio


$$
J_{k+1}/J_k\longrightarrow d=2M^3
$$


gives


$$
\log|\mathcal J_{n,m}|
=n\log d+m\log(5+d)+o(n)
$$


for $m/n\to c>0$. The binomial sandwich proof is valid.

Finally,


$$
\alpha=\frac{5+d}{M^2}>5,
\qquad 5+2M^{-1}=M^2.
$$


These identities verify A3’s strict same-last-index improvement for


$$
0<c<
\frac{2\log M}{\log(M^4/(5+d))}.
$$


This is an upper-rate comparison with the unfiltered index $N=n+m$, not with the smaller starting index $n$.

### 6.5 Actual filtered gcd, domain, and primorial scope

For


$$
L_N=2^{N+1}(2N+2)!(N!)^4,
\quad
U=L_N\mathcal H_{n,m},\quad T=L_N\mathcal J_{n,m},
$$


retain


$$
g=\gcd(|U|,|T|),\qquad
P=-\operatorname{sgn}(T)U/g,\qquad q=|T|/g.
$$


Above the inherited endpoint-sign threshold, $T\ne0$ for every $m\ge0$. The complete primitive error is


$$
\boxed{
q(e+\pi)-P
=\frac{\operatorname{sgn}(T)L_N}{g}
 \sum_{j=0}^m\binom mj5^{m-j}Z_{n+j}.
}
$$



The primorial argument correctly yields


$$
\liminf\frac{\log q}{N_x\log\log N_x}\ge2
$$


on its admissible primorial subsequences. It remains a lower bound for the final reduced denominator.

Along the established subsequences with $3\mid N$, the actual denominators tend to infinity. If $e+\pi$ is irrational, no rational center equals it; if it is rational with denominator $b$, equality would force $q=b$, eventually impossible. This proves eventual nonvanishing there without assuming the target.

An error upper bound and a denominator lower bound cannot prove primitive growth. Nor does the analytic gain provide the missing upper bound for this final $q$.

## Closing record

### (1) New result and proof status

The weighted upstream paper audit is now closed: the actual moment branches, complete coupled quotient, binary responses, and full scalar reconstruction connect correctly to the supplied fixed-state certificates. The actual regular dyadic law is


$$
v_2(q)=n+2,\qquad n=4^j+1,\ j\ge1,
$$


after the final gcd.

A1’s first radical lift and primitive leading depth pass. A3’s complete real-moment transform, corrected exponential contribution, and same-$N$ upper-rate gain pass.

The new factorization lemma


$$
Q_n=(1-s_ny)(y-a_n)W_n
$$


is proved above and identifies the unresolved endpoint depth exactly with $v_3(a_n+1)$.

### (2) Exact remaining bottleneck

For the weighted odd arithmetic, the unresolved scalar is still


$$
c\xi_{\rm const}-b\xi_{\rm last},
$$


equivalently the displacement of the simple $3$-adic root near $-1$. Even its evaluation would not determine the full rational-arctangent endpoint gcd.

For the compensated analytic route, the missing lower result is a nonzero surviving signed amplitude at the maximizing saddle or endpoint. Independently, primitive shrinking requires a sufficiently sharp upper bound for the **actual final reduced denominator**.

None of the audited results decides the irrationality of $e+\pi$.

### (3) Computation request

**None.** No additional determinant nodes, repeated closure orbits, or repeated upstream-file requests are needed for this audit. The new root-factorization lemma is algebraic, and another finite endpoint value would not settle either remaining infinite bottleneck.
