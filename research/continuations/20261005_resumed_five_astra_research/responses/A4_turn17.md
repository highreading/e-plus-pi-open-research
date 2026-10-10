> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4, Turn 17 — Independent audit of the scalar, displacement, and normalized binary-force reductions

## Executive findings

The supplied arguments establish several useful local results, but they do not settle the irrationality of $e+\pi$.

My main audit conclusions are:

1. **A1turn9’s scalar theorem is valid.** Its finite Pascal vector respects the genuinely shorter residue-$2$ class. The proof gives
   

$$
\eta_n\equiv\chi_n\equiv3\pmod9
   \qquad(n\ge5,\ n\equiv2\pmod3).
$$


   The complete-force cancellation, sharp producer inverse loss, nonzero endpoint valuation, and quadratic precision protection follow at their stated scopes.

2. **A2turn6’s terminal residues and finite displacement identities are valid under the retained hypotheses.** The nonzero $29$-digit table supports a uniform digit-product theorem, not merely a finite sample. The complete second-force terminal residue includes the factorial subtraction, logarithmic force, and exterior $+1$. The nearest-neighbor exclusions hold with the stated integrality and degree hypotheses; “every original index” must mean every index satisfying the hypotheses actually used, including the preferred cylinder.

3. **The three-column reduction is a rational reduction, not automatically a saturated weighted-lattice reduction.** A useful strengthening is available: before weighting, the displayed three columns form a saturated integral kernel basis whenever the contact matrix and recurrence have the required integral properties. Weighting and subsequent normalization still require their own lattice accounting.

4. **A5turn14’s Newton recurrence computes the raw column $V_w$, not $4Y$ at the same precision.** The coordinator’s exact normalization bridge is correct:
   

$$
4Y=\frac{V_w}{b!}.
$$


   Therefore computing $4Y\bmod2^M$ through that raw recurrence requires
   

$$
P=v_2(b!)+M.
$$


   Its degree bound then scales with $b$, not just with $M$. This is the decisive correction to any precision-sized normalized interpretation.

5. **A new, genuinely evaluable relative consequence is proved below.** The complete logarithmic budget gives an explicit certificate for when omission of the logarithmic force is harmless in the *normalized ratio* $H/N$, after paying the actual first-column content and actual norm valuation. The criterion is
   

$$
v_2\!\left(\frac HN-\frac{H^{(e)}}N\right)
   \ge J+a-\alpha-2,
$$


   where
   

$$
J=K_F(n,b)-v_2(b!),\qquad
   a=\min_jv_2(X_j),\qquad \alpha=v_2(N).
$$


   This is a proved relative error bound, not a proof of norm/mixed alignment. It yields a finite residue certificate under an explicit, checkable threshold.

No tools were executed. The supplied code and receipts are treated as mathematical source data; I have not independently regenerated their artifacts.

---

## 1. Domains, boundaries, and evidence

The three arithmetic settings must remain distinct.

### Ternary producer

The original A1 family is


$$
n=4^j+1,\qquad j>0,\qquad81\mid j,
$$


with the additional real-window and residual-space hypotheses retained wherever the residual reduction is used. In particular,


$$
A=n-2=H-D,\quad H=3^{h-1},\quad
m=\frac{A+1}{2},\quad d=\frac{3D}{2}-1,\quad
\nu=\frac D2-1.
$$


The residual coordinates and HIGH endpoints are not enlarged.

The new scalar theorem itself has the larger, separately proved scope


$$
n\ge5,\qquad n\equiv2\pmod3.
$$


That enlargement does **not** extend the order-six producer correction or the residual determinant reduction to arbitrary auxiliary orders.

### $29$-adic contact system

The retained family is


$$
a=432827+682892t,\quad b=3^a,\quad n=2001b,
$$


with the preferred cylinder


$$
t\equiv364\pmod{841}
$$


where required. Contact coordinates are $0\le i,j<b$; reconstructed coordinates are $0\le j\le b$.

### Binary contact system

The original family is


$$
b=9^{18+32u},\quad n=4002b,\quad u\ge0,
$$


with


$$
b=128D+81,\quad n=128C+66,\quad C=4002D+2532.
$$


The shortened terminal block remains $0\le\rho\le80$, followed by the separate coordinate $j=b$.

### Scope of the receipts

The scalar receipt reports twelve auxiliary orders


$$
5,8,\ldots,32,\ 83,\ 245,
$$


not an original-family residual calculation. Its comparisons through $3^{11}$, and quotient comparisons through $3^{10}$, support the implementation of the proved scalar identities.

The displacement receipt checks four finite systems and reports rational rank three. It does not report a saturated weighted basis or an all-depth normalized Gram law.

The weighted-force receipt checks 192 complete-force differences at integral odd $k$, 33,153 factorial scalar cases, and 8,069 cutoff inequalities. Those checks have exactly their stated finite scope.

---

# Part I. Audit of A1turn9

## 2. The finite Pascal vector is correct

Write


$$
n=3N+2,\qquad N\ge1.
$$


The residue-class sizes are


$$
N+1,\quad N+1,\quad N.
$$


Let


$$
c_i=(-1)^{N-i}\binom Ni,\quad
w_{3i}=c_i,\quad w_{3i+1}=-c_i,\quad w_{3i+2}=0
$$


on the actual available coordinates.

For


$$
Z_{ij}=\binom{i+j}{i},\qquad 0\le i,j\le N,
$$


the finite Pascal factorization gives $Zc=e_N$. Consequently, in the shorter residue-$2$ block, the output is the first $N$ entries of $e_N$, hence zero.

This verifies the endpoint-sensitive step


$$
\mathsf T_nw\equiv u\pmod3.
$$


Adding a fictitious last residue-$2$ coordinate would invalidate this step. A1 does not do so.

## 3. The extra digit in $\eta_n$ is proved, not sampled

The actual recurrence gives


$$
\gamma_r\bmod9=
1,0,4,4,0,7,1,0,4
$$


periodically, and hence


$$
\gamma_{3s+1}\equiv0,\qquad
\gamma_{3s}+2\gamma_{3s+2}\equiv0\pmod9.
$$


The stated binomial congruences follow from expanding $(1+z)^{3s}$ modulo $9$, with unit denominators in the second identity.

Put $v=\mathsf T_n^{-1}u$. Since $w-v\in3\mathbb Z_3^n$,


$$
u^T\mathsf T_n^{-1}u
\equiv2u^Tw-w^T\mathsf T_nw\pmod9.
$$


The two contractions are


$$
u^Tw\equiv3(N+1),\qquad
w^T\mathsf T_nw\equiv6N\pmod9.
$$


Because $3\mid F$,


$$
\eta_n\equiv-6(N+1)+6N\equiv3\pmod9.
$$



There is no hidden large-$N$ hypothesis. The exceptional $n=2$ is correctly excluded.

## 4. Complete-force cancellation and endpoint valuation

The complete force satisfies


$$
\mathsf T_n^{-1}\tau
=
3nz^++(b_c+6)e_{n-1}
+\frac{2b_c}{n-1}e_{n-2}.
$$


Using


$$
u_{n-2}=-\frac{n-1}{2}u_{n-1}
$$


gives the exact cancellation


$$
\chi_n=3n\sigma_n+6u_{n-1}.
$$


Both lower-degree terms are included; their $b_c$-dependence cancels in this contraction.

The shorter-class vector also gives $\sigma_n\equiv1\pmod3$, so


$$
\chi_n\equiv3\pmod9,\qquad
\xi_n=\frac{\chi_n}{\eta_n}\in1+3\mathbb Z_3.
$$



The subsequent valuation deductions are sound:



$$
v_3(\det C_n)
=
2\sum_{a=0}^{n-2}v_3(a!)+1,
$$


and


$$
\min_{a,b}v_3((\Gamma_n^{-1})_{ab})
=-2v_3(F)-1.
$$



For the latter, the terminal entry of $v$ is a unit, so the rank-one term $v_{n-1}^2/\eta_n$ has valuation $-1$, which cannot cancel with the integral entry of $\mathsf T_n^{-1}$. Multiplication by the two terminal factorial inverses attains the claimed minimum.

The exact actual endpoint remains


$$
Q_n^{\rm loc}(-1)=-F^2\xi_n\ne0,
$$


thus


$$
v_3(Q_n^{\rm loc}(-1))=2v_3(F).
$$


This is not the zero endpoint of the core $Q_c$.

## 5. Quadratic precision protection is valid

For approximate solutions $w_r,z_r$ accurate modulo $3^r$,


$$
F^2-2u^Tw_r+w_r^T\mathsf T_nw_r
\equiv\eta_n\pmod{3^{2r}},
$$


and


$$
u^Tz_r+w_r^Tk-w_r^T\mathsf T_nz_r
\equiv\sigma_n\pmod{3^{2r}}.
$$


These are exact quadratic/bilinear error identities. No condition number is being presumed.

Thus to determine $\xi_n\bmod3^M$, input precision $3^{M+1}$ and


$$
r=\left\lceil\frac{M+1}{2}\right\rceil
$$


solution digits suffice. The only scalar loss is division of $\eta_n$ by $3$.

For the terminal correction $R=\mathcal E_n/3^6$, the $3^{p+7}$ input budget is sufficient **provided the accepted original-family order-six divisibility and factorial-tail hypotheses remain in force**.

### A1 audit conclusion

The producer precision problem is closed at this scope. The later residual pair is not.

In particular, the sharpened endpoint gives, on the audited depth-$14$ window and when the relevant pair is nonzero,


$$
v_3(q)=
\max\!\left\{0,\,
h-14+2v_3(F)+v_3(\mathcal D_1)-v_3(\mathcal D_0)
\right\}.
$$


Nothing in the scalar theorem proves $\mathcal D_0\mathcal D_1\ne0$ or evaluates their relative valuation.

---

# Part II. Audit of A2turn6

## 6. The $29$-digit table and product argument

The table is independently specified by either


$$
(r+1)j_{r+1}=2(2r+1)j_r+4rj_{r-1}
$$


or


$$
j_r=\sum_{a=0}^{\lfloor r/2\rfloor}
\binom r{2a}\binom{2a}a2^{r-a}.
$$


All denominators in the recurrence through $j_{28}$ are units modulo $29$. The supplied receipt checks agreement and the absence of zeros.

The passage from this finite table to all actual higher digits is rigorous. For


$$
J=[t^0](t^{-1}+2+2t)^n,
$$


the lowest-digit factor has exponents in $[-28,28]$. Only exponent zero can match a multiple of $29$. Repeated Frobenius factorization therefore gives


$$
J\equiv\prod_\nu j_{n_\nu}\not\equiv0\pmod{29}.
$$



Consequently


$$
2\theta_{b-26}-\theta_{b-25}\equiv-J
$$


is a unit. It is not a fixed residue independent of the unfixed higher digits.

## 7. Complete second-force terminal residue

The key normalized exponential quantity is


$$
T_m=\sum_{q=b}^m\binom mq\frac{q!}{b!}.
$$


Since $b\equiv27\pmod{29}$, only $q=b,b+1$ survive modulo $29$:


$$
T_m\equiv\binom mb-\binom m{b+1}.
$$


The logarithmic contribution is zero at this precision because of the **whole-force** bound, not because it is omitted from the definition.

Thus


$$
r_i\equiv
\binom{2n+i}{b}-\binom{2n+i}{b+1}\pmod{29}.
$$


Lucas’s theorem puts its support in row residues $27,28$.

The finite inverse


$$
A^{-1}\equiv(I+S)^{-2n}\mathsf P^{-1}\pmod{29}
$$


preserves the complementary vanishing condition: inverse Pascal coefficients vanish across the prohibited low-digit inclusion, and the upper-shift factor has only offsets divisible by $29$. Hence


$$
\psi_j\equiv0\pmod{29}\quad(j\bmod29\le26),
$$


especially


$$
\psi_{b-1}\equiv0.
$$



The actual endpoint is therefore


$$
Y_b/W_b=1+b\psi_{b-1}\equiv1\pmod{29}.
$$


The exterior $+1$ is indispensable.

## 8. Nearest-neighbor exclusions: valid scope and explicit degree accounting

The terminal identity yields


$$
1-29\kappa_h
=
\mathscr S\bigl(
1+b\psi_{b-1}
-29s_nb\theta_{b-1}-29t_b(h)
\bigr).
$$


Integral edges imply $h(b-1)$ is integral because the terminal edge multiplier is a unit. For integral $s_n$,


$$
1-29\kappa_h\equiv8\pmod{29}.
$$



### Integral-valued case

If $h$ is integral-valued at all actual edge indices, then every $t_i(h)$, and hence $\kappa_h$, is integral. This contradicts the preceding congruence.

This proves exclusion at every index satisfying the hypotheses used here. It should **not** be read as an extension to arbitrary $t$ outside the preferred cylinder unless the needed normal and endpoint congruences are separately established there.

### Fixed-degree case

The denominator bound can be made concrete. For degree at most $d$, use the actual nodes


$$
j=0,29,58,\ldots,29d
$$


when they lie in the edge range. Their edge multipliers are units modulo $29$, so $h(29r)$ is integral.

Lagrange interpolation gives


$$
h\in29^{-C_d}\mathbb Z_{29}[J],
\qquad
C_d=d+v_{29}(d!).
$$


Indeed, the denominator at node $29r$ has valuation


$$
d+v_{29}(r!)+v_{29}((d-r)!)
\le d+v_{29}(d!).
$$


This supplies an explicit sufficient fixed-degree threshold


$$
v_{29}(b-B)>14675394+\max(C_d-1,0).
$$



For degree $27$, a sharper choice gives $C_{27}=1$: take all 27 unit-edge residues modulo $29$, then one additional actual node congruent to one of them modulo $29$. The interpolation denominators have valuation at most one. Thus the stated degree-$27$ threshold


$$
v_{29}(b-B)>14675394
$$


is justified.

These are exclusions of the specified operator mechanism, not disproofs of scalar alignment.

## 9. Exact logarithmic homogeneity and finite displacement

The differential identity


$$
\phi F'=2
$$


implies


$$
P_n=\phi^{n+1}F^{(n+1)},\qquad
P_{n+1}=\phi P_n'-(n+1)\phi'P_n,
$$


and therefore $\deg P_n\le n$.

Hence the logarithmic source in the recurrence vanishes **exactly** in rows


$$
1\le i\le b-2.
$$


It survives in the two initial complete-force values. This is stronger than a fixed-precision estimate but does not make the full logarithmic force zero.

The generating-column identity and elementary $B_j^{(n)}$ identity give


$$
\mathcal DA=-\mathcal VC,\qquad
\mathcal Df^0=0,\qquad
\mathcal D\mathbf r=\mathcal Ve_b.
$$


The row $i=1$ has $\gamma_1=0$, so no negative contact coordinate is introduced. The final column $k=b$ is required and retained.

The symbolic proof supports these identities. The four finite checks verify only their implementations at those systems.

## 10. Rational rank versus saturated lattice

Surjectivity of $\mathcal D$, together with integral invertibility of $A$, proves surjectivity of $\mathcal V$ at the $29$-adic scope. Thus


$$
\dim\ker\mathcal V=3.
$$


The displayed weighted columns have rational rank three, distinguished by their two independent homogeneous initial data and the nonzero exterior charge of the third column.

That is not, by itself, a saturated weighted basis theorem.

### A useful strengthening: saturated unweighted kernel basis

Let


$$
q_0=CA^{-1}h^{(0)},\qquad
q_1=CA^{-1}h^{(1)},\qquad
q_*=CA^{-1}\tau+e_b.
$$


Suppose the recurrence coefficients are integral and $A\in\mathrm{GL}_b(\mathbb Z_p)$. Then


$$
\boxed{
\ker_{\mathbb Z_p}\mathcal V
=\mathbb Z_pq_0\oplus\mathbb Z_pq_1\oplus\mathbb Z_pq_*.
}
$$



**Proof.** The square matrix $[C,e_b]$ is lower triangular with unit diagonal entries $-1,\ldots,-1,1$. Every integral vector has a unique representation


$$
q=Cx+t e_b,\qquad x\in\mathbb Z_p^b,\ t\in\mathbb Z_p.
$$


If $\mathcal Vq=0$, then


$$
\mathcal DAx=t\mathcal H.
$$


Therefore $Ax-t\tau$ is a homogeneous recurrence solution, uniquely of the form


$$
a_0h^{(0)}+a_1h^{(1)}
$$


with integral initial values. Substitution proves the assertion. ∎

Weighting by $\operatorname{diag}(W_j)$ gives an exact basis of the **weighted image lattice**. It does not prove that image is saturated in the ambient weighted coordinate space. Its saturation defect can be measured by Smith invariants or valuations of maximal minors; these are separate arithmetic data.

For the binary setting, the recurrence coefficients are also integral: the apparent factors $1/2$ divide the displayed integer products. The even-$n$ contact unit theorem supplies the other hypothesis. Nevertheless, binary normalization of the actual columns still requires the exact factors $R_{\rm central}$ and $b!$.

## 11. Saturated adjoint criterion

The adjoint solution


$$
A^Tz=\mathcal R^T\Pi d
$$


is integral at the retained $29$-adic scope. Backward recurrence elimination uses only unit pivots and yields


$$
29^3\mathfrak v
=
\frac{r_0}{f_0^0}\,29^{c+2}\mathfrak b
+\mathcal E_{\rm force}.
$$


Here $f_0^0$ is a proved unit and $r_0\in29\mathbb Z_{29}$, so the extracted coefficient after division by $29^3$ is integral.

Thus


$$
\mathfrak v\in\mathfrak b\mathbb Z_{29}
\iff
\mathcal E_{\rm force}\in29^3\mathfrak b\mathbb Z_{29}
$$


is valid.

It remains a criterion, not a proof of the right-hand divisibility. The full residual is


$$
\eta_1\left(r_1-\frac{f_1^0}{f_0^0}r_0\right)
+\sum_{i=1}^{b-2}\lambda_i\mathcal H_i
+W_b(\Pi d)_b.
$$


Neither the interior factorial source nor the exterior endpoint may be suppressed.

---

# Part III. Audit and correction of A5turn14

## 12. The whole logarithmic budget is valid

The coefficient estimate


$$
v_2(\alpha_r)\ge-\lfloor r/2\rfloor
$$


gives


$$
v_2(m!\mathcal F_m)
\ge
L(m)+1-\left\lfloor\frac{m-1}{2}\right\rfloor
-\lfloor\log_2m\rfloor.
$$


Every actual summand has


$$
n\le m=2n+i-s\le2n+b-1.
$$


The complete divided-power coefficients are integral. Therefore


$$
h^F\in2^{K_F(n,b)}\mathbb Z_2^b,
$$


where


$$
K_F(n,b)=1+L(n/2)-\lfloor\log_2(2n+b-1)\rfloor.
$$



The finite inverse and reconstruction lose no binary precision in the raw normalization. This part of A5turn14 is sound.

## 13. The raw Newton recurrence is also valid

The complete even-$n$ symbol has the expansion


$$
\phi^n=(1+2U)^{n/2},
$$


with expansion order $a$ contributing valuation at least $a$ and degree at most $4a$.

For the raw exponential force,


$$
\mathcal D_m=\sum_{q=0}^m(m)_{\underline q},
$$


the factorial tail is controlled by $L(q)$. A retained term of total weight $w$ has degree at most $4w+1$. The finite interpolation operator $\Pi_b$ preserves all actual row values and never increases degree.

Thus, for raw precision $P\le K_F$, the iteration has a representative of degree


$$
\min(b-1,4P-3),
$$


and reconstructs the complete raw column $V_w\bmod2^P$, including its exterior $e_0$.

This is a legitimate bounded-state raw calculation. It is not yet the required normalized calculation.

## 14. Exact normalization: where the apparent reduction is lost

Let


$$
U=(I+S)^n,\quad A=\widetilde N U,\quad
\mathcal R=\operatorname{diag}(W_j)C,
\quad f=(j!)_{0\le j<b}.
$$


Then


$$
\mathcal T=\mathcal R U^{-1}.
$$



The finite factorial reconstruction is


$$
Cf=-e_0+b!e_b.
$$


Indeed, every interior coordinate $1\le j<b$ is


$$
j(j-1)!-j!=0,
$$


while the first and last coordinates are $-1$ and $b!$. Weighting gives


$$
\mathcal Rf=-e_0+b!W_be_b.
$$



For the complete force


$$
r=\frac{h^e+h^F-Af}{b!},
$$


we therefore obtain


$$
\begin{aligned}
V_w
&=e_0+\mathcal R A^{-1}(h^e+h^F)\\
&=e_0+\mathcal Rf+b!\mathcal R A^{-1}r\\
&=b!\bigl(\mathcal R A^{-1}r+W_be_b\bigr).
\end{aligned}
$$


Hence


$$
\boxed{4Y=\mathcal R A^{-1}r+W_be_b.}
$$



The first-column bridge is likewise exact:


$$
\boxed{2X=\mathcal R A^{-1}(f^0/R_{\rm central}).}
$$



The raw-to-normalized precision loss is consequently


$$
\boxed{P=L(b)+M}
$$


for $4Y\bmod2^M$. The raw Newton degree bound becomes


$$
4L(b)+4M-3.
$$


Since $L(b)=b-s_2(b)$, this scales with $b$. On the original family, the support bound at this precision does not provide a short normalized coordinate range.

**Correction:** A5turn14 proves a precision-sized algorithm for raw $V_w$ at fixed raw precision, but not a precision-sized algorithm for normalized $4Y$ at fixed normalized precision.

## 15. What remains after exact factorial subtraction

The normalized exponential force is


$$
r_i^{(e)}
=
\sum_s a_s(n)(n+i)_{\underline s}
\sum_{t\ge0}
\binom{2n+i-s}{b+t}\frac{(b+t)!}{b!}.
$$


Since


$$
\frac{(b+t)!}{b!}=t!\binom{b+t}{t},
$$


terms with $L(t)\ge M$ vanish modulo $2^M$.

This leaves only $O(M)$ values of $t$, but the lower binomial indices remain $b+t$. A small number of shift labels is not a bounded-degree row polynomial theorem. Those high-index kernels are the precise obstruction to transferring the raw Newton argument unchanged.

The normalized logarithmic budget is


$$
\boxed{
J=K_F(n,b)-L(b).
}
$$


It may be used only after this loss has been paid.

## 16. Auxiliary parameter correction

For $n=4002b$,


$$
k=\frac{2001b-1}{32}.
$$


The proposed $b=1,3$ weighted-difference probes do not have $k\in\mathbb Z_2$. They cannot test a theorem restricted to integral $k$.

This does not invalidate their use as auxiliary tests of a separately proved raw even-$n$ contact identity. It does invalidate using them to certify the restricted weighted parameter-transfer theorem.

The coordinator’s replacement receipt uses integral odd $k$ and complete continued central forces. Its finite checks are appropriately scoped; they do not establish an all-word theorem.

---

# Part IV. A new evaluable relative consequence

## 17. Normalized logarithmic protection for the actual ratio

The following result uses the actual content and actual norm, not a model content.

### Proposition — Relative logarithmic protection

On the original binary family, write


$$
N=X^TX>0,\qquad H=X^TY,
$$


and define


$$
a=\min_jv_2(X_j),\qquad \alpha=v_2(N).
$$


Let $Y^{(e)}$ be obtained from the exact normalized formula for $Y$ by replacing the complete force $r$ by its complete factorial/exponential part $r^{(e)}$, while retaining $W_be_b$. Put


$$
H^{(e)}=X^TY^{(e)},\qquad
J=K_F(n,b)-L(b).
$$


Then


$$
\boxed{
v_2(H-H^{(e)})\ge a+J-2,
}
$$


and


$$
\boxed{
v_2\!\left(\frac HN-\frac{H^{(e)}}N\right)
\ge a+J-\alpha-2.
}
$$



**Proof.** The normalized logarithmic input is $h^F/b!$, of depth at least $J$. Integral contact inversion and reconstruction give


$$
4(Y-Y^{(e)})\in2^J\mathbb Z_2^{b+1}.
$$


Thus every coordinate of $Y-Y^{(e)}$ has depth at least $J-2$. Multiplication by $X_j$ and summation give the first inequality. Division by the nonzero $N$ gives the second. ∎

### Evaluable consequence

For any target integer $s$, if


$$
\boxed{J\ge s+\alpha-a+2,}
$$


then


$$
\boxed{
\frac HN\equiv\frac{H^{(e)}}N\pmod{2^s}.
}
$$


The congruence is interpreted in $\mathbb Q_2$ by valuation of the difference; it does not presume either ratio is integral.

This is a relative result because it pays the full actual norm valuation $\alpha$, including primitive-norm cancellation beyond column content.

It is genuinely evaluable:

* $J$ follows from factorial digit sums;
* $a$ and $\alpha$ can be certified by finite exact arithmetic or by modular calculation continued until their first nonzero digits are found;
* the exponential force at sufficient precision uses the finite $t$-tail above;
* every contact boundary and the exterior $W_be_b$ remains present.

It is **not** a uniform theorem that the threshold always holds at a prescribed relative depth. In particular, no bound on $\alpha-a$ has been proved here.

## 18. A finite factorial-force certificate

Set


$$
\mathsf U=2X,\quad
\mathsf V=4Y,\quad
c=\min_jv_2(\mathsf U_j)=a+1,\quad
d=v_2(\mathsf U^T\mathsf U)=\alpha+2.
$$


For an integer $T\ge1$, retain exactly those $t$ with $L(t)<T$ in the normalized exponential force, solve the actual finite contact system, and reconstruct $\mathsf V^{[T]}$ with the endpoint term.

Then


$$
\mathsf V-\mathsf V^{[T]}
\in2^{\min(J,T)}\mathbb Z_2^{b+1},
$$


so


$$
\boxed{
v_2\!\left(
\frac HN-
\frac{\mathsf U^T\mathsf V^{[T]}}
     {2\,\mathsf U^T\mathsf U}
\right)
\ge c+\min(J,T)-d-1.
}
$$



Thus a sufficient, explicit certificate for the ratio modulo $2^s$ is


$$
\boxed{\min(J,T)\ge s+d+1-c.}
$$



This procedure still permits an original-sized finite contact solve. It is not advertised as an $M$-sized algorithm. Its advance is a proved **relative stopping rule**, with all normalization and content losses exposed.

---

# Part V. Remaining bottlenecks and bounded arithmetic

## 19. Concrete follow-on lemma

The next useful binary lemma is now precise:

> **Normalized high-index contraction lemma.**  
> For the actual relation $n=4002b$, $b=9^{18+32u}$, evaluate the contact/reconstruction contractions generated by
> 

$$
> \binom{2n+i-s}{b+t},
> \qquad L(t)<T,
>
$$


> with the complete symbol and actual finite endpoint, at precision sufficient for
> 

$$
> \mathsf U^T\mathsf U,\qquad
> \mathsf U^T\mathsf V.
>
$$


> The proof must control units and primitive-norm cancellation, not merely count retained shift labels or bound common content.

The rational displacement identities can organize this problem into three columns. They do not evaluate their normalized Gram entries. The saturated unweighted basis lemma above identifies the exact integral kernel, but weighting and normalized Gram cancellation remain outstanding.

For A2, the corresponding unresolved local lemma remains


$$
\mathcal E_{\rm force}\in29^3\mathfrak b\,\mathbb Z_{29},
$$


followed by the retained unit-scale congruence.

For A1, the unresolved local object remains the actual residual determinant/cofactor pair, including nonvanishing and relative valuation.

## 20. Proposed bounded exact calculation

The scalar and displacement receipts need not be repeated as the principal next experiment.

A focused normalization check can use the auxiliary systems


$$
(n,b)=(66,3),\ (66,5),\ (66,9),
\qquad M=8.
$$


These have integral odd $k=(n-2)/64=1$, but are **not** original indices and do not satisfy $n=4002b$. They test the algebraic normalization and raw-versus-normalized precision distinction only.

For these inputs,


$$
K_F=1+L(33)-\lfloor\log_2(132+b-1)\rfloor=25.
$$


Thus raw precision


$$
P=L(b)+8
$$


is within the proved logarithmic budget in all three cases.

### Inputs

Construct the exact finite $\widetilde N,U,A,C,\mathcal R$, the complete forces, and $f=(j!)_{j<b}$. Use the full normalized exponential tail and justify logarithmic omission only at its proved precision.

### Expected verifiable output

1. Exact finite endpoint identity:
   

$$
\mathcal Rf+e_0-b!W_be_b=0.
$$



2. Exact normalization identity:
   

$$
e_0+\mathcal R A^{-1}(h^e+h^F)
   =
   b!\left(\mathcal R A^{-1}r+W_be_b\right).
$$



3. Agreement modulo $2^8$ between:
   * raw Newton computation at $P=L(b)+8$, followed by valuation-safe division by $b!$;
   * direct normalized contact computation at precision $8$.

4. A precision ledger showing that raw precision $8$ alone guarantees only normalized precision $8-L(b)$, not $8$.

5. Optionally, Smith data for the unweighted three-column kernel basis and for its weighted image, reported separately. Rational rank three is not a substitute for these lattice data.

For a relative-ratio implementation test, form the exact auxiliary first column, compute its actual $c,d$, and check the bound in §18 whenever its threshold is satisfied. A passing output certifies only these finite systems.

---

# Part VI. Primitive arithmetic and final status

## 21. Full gcd and whole error remain indispensable

For the Gram constructions, retain the least actual two-column clearer and the full integer pair


$$
N_B=d_B[u,v],\qquad
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2}.
$$


The primitive approximation is


$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
$$


The primitive multiplier is $d_B^2/g_B$. No single-prime calculation replaces this all-prime gcd.

In the binary family, the retained exact interface is


$$
v_2(q_n)=
\max\!\left\{0,\,
\frac{3n}{2}-L(b)-s_2(n)-1-(\gamma-\alpha)
\right\}.
$$


The present audit does not uniformly determine $\gamma-\alpha$.

Within the accepted complete signed-error theorem,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi)<0
\quad\text{eventually},
$$


and


$$
\log|\epsilon_n|
=
-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$


The whole evaluated form is


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n>0}
$$


eventually. The missing global estimate is one forcing this **entire** nonzero same-index quantity to tend to zero.

The analogous $29$-adic full gcd and signed error, and A1’s determinant-based full gcd and whole determinant error, likewise remain unchanged. None is replaced by a local scalar residue.

## 22. Closing proof-status ledger

| Result | Audit status |
|---|---|
| A1 shorter-class Pascal vector | Valid with actual finite endpoints |
| $\eta_n\equiv\chi_n\equiv3\pmod9$ | Proved for $n\ge5,\ n\equiv2\pmod3$ |
| A1 complete-force cancellation | Exact |
| Producer inverse loss and nonzero endpoint valuation | Valid deductions |
| Quadratic scalar precision protection | Valid |
| $29$-digit table | Finite exact table, supported by supplied independent receipt |
| Uniform digit-product nonvanishing | Proved symbolically |
| Complete second-force terminal residue | Valid at retained hypotheses |
| Integral-valued and fixed-degree nearest-neighbor exclusions | Valid with scope and denominator qualifications stated above |
| Full logarithmic interior homogeneity | Exact finite recurrence result |
| Three-column rational reduction | Valid |
| Saturated unweighted kernel basis | Proved here |
| Saturated weighted/normalized Gram law | Not proved |
| A2 adjoint norm-factor criterion | Valid equivalence; divisibility remains open |
| A5 whole logarithmic budget | Valid |
| A5 raw Newton recurrence | Valid at raw precision |
| Precision-sized normalized $4Y$ algorithm from that recurrence | Not established; normalization costs $L(b)$ digits |
| Actual-content relative logarithmic protection | Proved here with explicit evaluable threshold |
| Uniform normalized norm/mixed alignment | Unresolved |
| Full primitive-denominator/whole-error comparison | Unresolved |

### Final conclusion

The audit confirms the ternary producer scalar theorem and the complete-force displacement reductions. It also identifies the exact binary normalization obstruction: **a raw precision-sized second-column recurrence does not remain precision-sized after division by $b!$.**

The new relative protection theorem provides a valid stopping criterion for complete normalized ratio calculations, and the unweighted kernel lemma strengthens the lattice interpretation of the three-column reduction. Neither result evaluates the all-depth normalized Gram law or controls the final primitive denominator.



$$
\boxed{\text{An unconditional proof or disproof of irrationality of }e+\pi
\text{ remains unresolved.}}
$$


