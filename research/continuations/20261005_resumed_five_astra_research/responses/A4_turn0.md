> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 independent review: quantitative centered comparison, prime-$29$ contact compression, and the global arithmetic interface

## 1. Conclusions and scope

The objective remains unresolved: **the supplied work does not prove either rationality or irrationality of $e+\pi$**.

The two assigned reviews have the following outcomes.

1. **The quantitative centered comparison passes after a correction to the exponential remainder.** The displayed polynomial power $6$ is not justified by the source’s unspecified polynomial losses. It can be removed by decreasing the exponential constant. At the retained, previously audited analytic inputs, there are constants $C,\kappa,\epsilon>0$ and $N$ such that
   

$$
\left|
   \log\!\left[\frac{F_j/F_b}{P_j/P_b}\right]
   +\frac{s_j}{n^2}
   \right|
   \le
   C\left(\frac{d^2}{n^3}+\frac d{n^3}\right)+Ce^{-\kappa n}
   \tag{1.1}
$$


   for
   

$$
n\ge N,\qquad 2\le d=b-1\le\epsilon n,\qquad 0\le j\le b.
$$


   Both parities are included. The same bound applies to the logarithmic ratios of the **whole coordinate errors**, after adjusting constants.

   The exact stationary point, real curvature, Gaussian noncancellation, and $O(n^{-1})$ signed first moment are justified below. There is a further scope correction: “sharp leading spread $d/n^2$” is an asymptotic conclusion on $d=o(n)$, not an asymptotic equivalence throughout a fixed positive-ratio strip.

2. **The proposed prime-$29$ contact compression passes.** Its reduction is valid for integer arguments, including negative shifted arguments, and supports coefficient recovery by finite differences because the relevant Newton degree is at most $57$. The phrase “degree bound $58$” must mean *58 coefficients*, not degree $58$.

   The boundary division $29^2\mid c_h$ for $h\ge2$, the reduced boundary force, and the leading contact polynomial all follow algebraically. The finite receipt is consistent with these statements. Its reported $3654$ comparisons remain a finite computation at its fixed representative; they are not the parameter-transfer theorem.

3. **The contact vectors do not evaluate $R_C$ or $\Gamma _0$.** They are suitable bounded kernel inputs for that calculation, subject to the already specified stripping, coefficientwise division, and original-boundary conditions. The handoff’s separate $\Gamma _1$ result is not a $\Gamma _0$ result.

4. **Neither review supplies a final-denominator estimate.** The raw-diagonal exclusion must be respected, and changing a basis without changing the rational center cannot evade it. Different weighted metrics are not automatically covered by an exclusion theorem for the original raw metric. Conversely, a different metric is not automatically a viable irrationality construction.

I have not executed arithmetic, verified hashes, accessed the linked archive notes, or conducted new literature searches. Numerical receipts below are used as supplied finite certificates.

---

# Part I. Quantitative centered comparison

## 2. Objects and retained inputs

Write


$$
\sigma=\sqrt2,\qquad M=1+\sqrt2,\qquad \rho=M^{-1},
\qquad \alpha=\sigma/M,\qquad d=b-1.
$$


The spread indices are


$$
s_0=d,\qquad s_j=b-j\quad(1\le j\le b).
$$



The finite systems remain


$$
H_b,T:\{0,\ldots,d\}^2,\qquad
K:\{0,\ldots,b\}\times\{0,\ldots,d\}.
$$


No extension of their inverses is used.

I reuse the passed qualitative CSC and its underlying interfaces, rather than repeat their audits. The quantitative ingredients relevant here are:

* the complete gamma insertion
  

$$
L_j=\log\mathcal S_j=-a_je_1+H_j,
$$


  with
  

$$
a_j\le C/n,\qquad
  |\partial_{z_i}H_j|\le Cd/n^2,\qquad
  |H_j|\le Cd^2/n^2;
$$


* the exact coefficient estimate
  

$$
\left|a_j-\frac{\sigma s_j}{dn}\right|
  \le C s_j/n^2;
  \tag{2.1}
$$


* positive-ensemble Hessian bounds on fixed anchor neighborhoods;
* the original-chamber truncated translation identity;
* full-circle zero-freeness and logarithmic derivative bounds;
* the complete scalar contours, including both minus connectors.

The new question is whether these estimates support a fixed, sufficiently small strip $2\le d\le\epsilon n$ and the stronger centered scalar transfer. They do.

## 3. Uniformity of the particle estimates

The explicit fixed-angle bound in A3turn28 has the form


$$
\mathbb P\{\max_i|\theta_i|>\delta\}
\le
\exp\left[
-\frac{kA^2}{8}n+
\frac d2\left(1+\log\frac{kA^2}{4c}\right)
\right],
\quad
A=\tan(\delta/2),\quad c=d/n.
\tag{3.1}
$$


Because


$$
c\left(1+\log\frac{kA^2}{4c}\right)\longrightarrow0
\quad(c\downarrow0),
$$


one fixed $\epsilon>0$ makes this at most $e^{-\kappa_0n}$ for every $0<c\le\epsilon$.

The normalization argument is legitimate. Strong convexity about the actual mode gives, along each ray, a Gaussian radial density multiplied by a nonincreasing factor. After angular integration, that factor is still nonincreasing. Monotone likelihood-ratio domination then compares the **normalized** radial distributions. An uncontrolled quotient of two unrelated partition bounds is not being used.

The complex-anchor modulus tilt need not be even. Its minimizer displacement


$$
|t_0|\le C\sqrt c/d
$$


and the mode comparison in A3turn28 supply a uniform bounded mode. Reflection is used only later, at the real anchors.

Consequently, for fixed $m$,


$$
\mathbb E\sum_i\theta_i^{2m}\le C_mdc^m,
$$


and the truncated translation calculation gives


$$
\operatorname{Var}(X)
=\frac d{n\alpha}
+O\!\left(\frac{d^2}{n^2}+\frac d{n^2}\right)
+\text{exponentially small terms}.
\tag{3.2}
$$


All constants can be chosen uniformly on the stated strip.

The singular full score is not assigned a globally bounded cubic remainder. The cutoff field retains the original chamber and controls its exceptional contribution by (3.1). This remains essential.

## 4. Quantitative anchor comparison

Define the actual full-circle quotient


$$
Q_j(q)=\frac{B_bA_j(q)}{\varepsilon_jB_jA_b(q)}.
$$


At either real anchor, its principal representation is


$$
Q_j(q)=
\frac{\mathbb E_q(\mathcal S_je^{i\Phi_q})}
     {\mathbb E_qe^{i\Phi_q}},
$$


before the exponentially small signed sectors are restored.

The retained centered estimates give


$$
\mathbb E_{e^{i\Phi_q}}e_1-\mathbb E_qe_1
=-\eta_q\operatorname{Var}(X)+O(c^2),
$$




$$
\mathbb E_{e^{i\Phi_q}}H_j-\mathbb E_qH_j
=O(d^2/n^3),
$$


and


$$
\log\mathbb E_{e^{i\Phi_q}}e^{L_j}
=\mathbb E_{e^{i\Phi_q}}L_j+O(d/n^3).
\tag{4.1}
$$


These follow from positive-measure variance estimates and centered quotients; no Brascamp–Lieb inequality is applied to a signed measure.

At $M,\rho$, the positive measures coincide, while


$$
\eta_\rho-\eta_M=-\rho.
$$


Thus


$$
\log Q_j(\rho)-\log Q_j(M)
=-a_j\rho\,\frac d{n\alpha}
+O(d^2/n^3+d/n^3)+\text{exponentially small terms}.
\tag{4.2}
$$



By (2.1),


$$
\left|
a_j\rho\,\frac d{n\alpha}-\frac{s_j}{n^2}
\right|
\le C\frac{s_jd}{n^3}
\le C\frac{d^2}{n^3},
\tag{4.3}
$$


using $\sigma\rho/\alpha=1$.

### The common-reference derivative estimate

The reference


$$
\mathcal R_j=\exp(\mathbb E_*L_j)
$$


is independent of $q$ and is the same on both disks. Positive modulus interpolation and centered phase normalization give


$$
Q_j(q)/\mathcal R_j
=1+O(d/n^2)+\text{exponentially small terms}
\tag{4.4}
$$


uniformly on fixed disks.

For $d\ge2$, the exponential term can be absorbed into $Cd/n^2$ after increasing $N$. On smaller disks, Cauchy’s formula therefore yields


$$
\partial_q^m\log Q_j(q)=O_m(d/n^2),\qquad m\ge1.
\tag{4.5}
$$


This use of Cauchy estimates is valid: it is applied to the actual holomorphic quotient, not to the nonholomorphic modulus-interpolation expectations.

## 5. Exact stationary point and real curvature

For the highest coordinate, put


$$
\mathcal F_\pm(r)
=n\log g_\pm(r)+\log A_b(\sigma\pm r),
\qquad g_+=g,\quad g_-=h.
$$


The logarithm is real on the relevant positive real interval, since $A_b$ is positive there.

The stationary equation is the **whole** equation


$$
\mathcal F_\pm'(r)=0.
\tag{5.1}
$$


The characteristic contribution has derivatives $O(d)$ on fixed neighborhoods. At $r=1$, the base first derivative vanishes, while its second derivative is a positive constant times $n$. Hence, for small fixed $\epsilon$,


$$
r_\pm=1+O(d/n)
$$


exists uniquely in a fixed neighborhood and


$$
c_0n\le \mathcal F_\pm''(r_\pm)\le C_0n.
\tag{5.2}
$$



On the circular arc, set


$$
G_\pm(\theta)=\mathcal F_\pm(r_\pm e^{i\theta}).
$$


Differentiating through $z=r_\pm e^{i\theta}$,


$$
G_\pm'(0)=ir_\pm\mathcal F_\pm'(r_\pm)=0,
$$


and


$$
G_\pm''(0)
=-r_\pm\mathcal F_\pm'(r_\pm)
-r_\pm^2\mathcal F_\pm''(r_\pm)
=-n\lambda_\pm,
$$


where


$$
0<\lambda_0\le\lambda_\pm\le\lambda_1.
\tag{5.3}
$$


In particular the curvature is real.

The base logarithms have bounded derivatives on the chosen neighborhoods; the characteristic logarithm contributes $O(d)$. Thus


$$
|G_\pm^{(3)}(\theta)|\le C(n+d)\le C'n.
\tag{5.4}
$$


The base angular-curvature margin survives an $O(d/n)$ perturbation. After shrinking $\epsilon$ and the central arc,


$$
\Re(G_\pm(\theta)-G_\pm(0))\le-\gamma n\theta^2.
\tag{5.5}
$$



There is no extra radial Jacobian: $d\zeta/(i\zeta)=d\theta$ on the circular arc.

## 6. Gaussian noncancellation and the signed first moment

Write on a symmetric fixed arc $[-a,a]$


$$
G(\theta)-G(0)=-\frac{n\lambda\theta^2}{2}+R(\theta),
\qquad |R(\theta)|\le Cn|\theta|^3.
$$


Choose $a$ so small that $Ca\le\lambda_0/4$. Then


$$
\left|
e^{G(\theta)-G(0)}-e^{-n\lambda\theta^2/2}
\right|
\le Cn|\theta|^3e^{-c n\theta^2}.
\tag{6.1}
$$


Therefore


$$
I:=\int_{-a}^a e^{G(\theta)-G(0)}\,d\theta
=\sqrt{\frac{2\pi}{n\lambda}}+O(n^{-1}),
$$


and


$$
|I|\ge c n^{-1/2}
\tag{6.2}
$$


for large $n$. This is an actual noncancellation proof.

The Gaussian odd moment vanishes. Multiplying (6.1) by $|\theta|$ gives


$$
\left|\int_{-a}^a\theta e^{G(\theta)-G(0)}\,d\theta\right|
\le Cn\int_{\mathbb R}|\theta|^4e^{-cn\theta^2}\,d\theta
\le Cn^{-3/2}.
$$


After division by (6.2),


$$
\left|
\frac{\int_{-a}^a\theta e^{G(\theta)-G(0)}\,d\theta}{I}
\right|
\le Cn^{-1}.
\tag{6.3}
$$


Also,


$$
\frac{\int_{-a}^a\theta^2|e^{G(\theta)-G(0)}|\,d\theta}{|I|}
\le Cn^{-1}.
\tag{6.4}
$$



These estimates justify the stronger scalar transfer. A modulus-only saddle would not justify (6.2) or (6.3).

## 7. Centered scalar transfer and the exponential correction

The displacement from each anchor to its real saddle is $O(d/n)$. By (4.5), its insertion cost is


$$
O(d^2/n^3).
$$


On the common highest-coordinate contour,


$$
\frac{Q_j(q(\theta))}{Q_j(q(0))}
=1+\beta_j\theta+O((d/n^2)\theta^2),
\qquad |\beta_j|\le Cd/n^2.
$$


Equations (6.3)–(6.4) give normalized insertion cost


$$
O(d/n^3).
\tag{7.1}
$$



Remote arcs and both minus connectors retain bounds of the form


$$
C(1+n+d)^K e^{-\eta n+C_1d}
\tag{7.2}
$$


for some fixed finite $K$. The sources do not establish that every such $K$ is at most $6$.

The rigorous repair is elementary. First choose $\epsilon$ with $C_1\epsilon\le\eta/4$. Then, for any $\kappa<3\eta/4$,


$$
(1+n+d)^K e^{-\eta n+C_1d}
\le C_{\kappa,K}e^{-\kappa n}.
\tag{7.3}
$$


Only finitely many derivative orders and contour estimates are used, so a common positive $\kappa$ exists.

Combining (4.2), (4.3), and (7.1) proves (1.1). **The polynomial power $6$ is unnecessary and should not be retained as a verified exponent.**

## 8. Whole error, nonvanishing, and metric spread

The whole coordinate error remains exactly


$$
e_j:=\frac{v_j}{u_j}-S
=
\frac{E_j}{P_j}
+(-1)^{n+1}\frac{F_j}{P_j}
+(-1)^n\delta_{j0}\frac D{P_j},
\tag{8.1}
$$


with


$$
eE_i=-[z^{n+i}](1-z+z^2/2)^n
\int_0^1s^ne^{1-s+sz}\,ds
$$


and the full elementary-symmetric insertion into $E_j$.

One scope repair is needed here. The all-sublinear equivalence


$$
F_j/P_j=4\pi M^{-2n-b}(1+o(1))
$$


cannot simply be invoked as a uniform equivalence on $d\le\epsilon n$. For that strip, the same saddle and anchor bounds nevertheless give the sufficient coarse estimate


$$
F_j/P_j\ge e^{-C n}>0.
\tag{8.2}
$$


Indeed, both saddle values differ from their anchors by $O(d^2/n)$, and all characteristic and base saddle factors have logarithms $O(n+d)$. Gaussian factors have uniformly comparable curvatures.

The factorial residual bounds therefore imply


$$
\frac{|E_j/P_j|+|\delta_{j0}D/P_j|}{F_j/P_j}
\le e^{-n\log n+O(n)}.
\tag{8.3}
$$


Thus, after increasing $N$, all whole errors have common sign $(-1)^{n+1}$, and


$$
\left|\log(e_j/e_b)+s_j/n^2\right|
\le R_{n,d},
\quad
R_{n,d}=C(d^2/n^3+d/n^3)+Ce^{-\kappa n}.
\tag{8.4}
$$



Normality gives $D>0$. The positive real Gaussian saddle, with exponentially smaller remainders, gives $P_j\ne0$ for every coordinate. Consequently


$$
u_j=(-1)^nP_j/D\ne0,
$$


in particular $u_0,u_b\ne0$.

For a positive diagonal metric in the original coordinates,


$$
c_W-S=\sum_j\alpha_je_j,\qquad
\alpha_j=\frac{W_{jj}u_j^2}{\sum_\ell W_{\ell\ell}u_\ell^2}.
$$


Hoeffding’s bounded-variable exponential estimate gives


$$
\left|
\log\frac{c_W-S}{e_b}
+\frac{\sum_j\alpha_js_j}{n^2}
\right|
\le R_{n,d}+\frac{d^2}{8n^4}.
\tag{8.5}
$$



Because every $u_j\ne0$, arbitrary strictly positive probability vectors are obtainable by choosing $W_{jj}\propto\alpha_j/u_j^2$. Hence the closure of attainable errors is exactly


$$
[\min_j e_j,\max_j e_j].
$$


The endpoint extremes need not be attained by strictly positive weights, but can be approached. Thus


$$
\left|
\sup_{W,V>0\ {\rm diagonal}}
\left|\log\frac{c_W-S}{c_V-S}\right|
-\frac d{n^2}
\right|
\le2R_{n,d}.
\tag{8.6}
$$



For $d=o(n)$, $d\ge2$, this proves asymptotic spread $d/n^2$. On the full fixed strip it proves the displayed quantitative estimate, with relative uncertainty $O(d/n+1/n)$, not a uniform relative $o(1)$.

---

# Part II. Prime-$29$ contact compression

## 9. Integer-value reduction of the finite contact operator

Put $p=29$. Let $h$ have integral Newton coefficients and degree at most $28$. The operator is the actual finite operator (A2turn23, (8.2)); its boundary factor remains


$$
\binom{b-1-X+s}{v+i}.
$$



Since $n\equiv0\pmod p$, for $1\le v\le28$,


$$
\binom nv\equiv0\pmod p.
$$


Therefore, for $1\le s\le28$,


$$
\mathscr L_{s,b}h(X)
\equiv(-1)^s\binom Xs h(X-s)\pmod p.
\tag{9.1}
$$



For $s=29$, only $v=29$ can survive, and


$$
\binom n{29}\equiv m:=n/p\pmod p.
$$


For $1\le i\le28$,


$$
\binom{28+i}{i}\equiv0\pmod p.
$$


Thus only $i=0$ survives:


$$
\mathscr L_{29,b}h(X)
\equiv
-\binom X{29}h(X-29)
+m h(X)\binom{b+28-X}{29}
\pmod p.
\tag{9.2}
$$



These are valid for every integer $X$. Generalized binomials at negative integers are integers; the eliminated factors depend only on the bounded indices and on $n$, not on a nonnegativity assumption for $X-s$.

### Why finite differences recover the coefficients

The compressed expressions have degree at most $57$. If an integer-valued polynomial $f$ of degree at most $57$ is divisible by $p$ at every integer, then


$$
\Delta^r f(0)=
\sum_{t=0}^r(-1)^{r-t}\binom rt f(t)
$$


is divisible by $p$ for $0\le r\le57$. These are exactly its Newton coefficients.

Thus the all-integer congruence proves coefficientwise congruence. Conversely, evaluation at $X=0,\ldots,57$ recovers all coefficients **once the degree bound has been proved**.

A 58-entry vector is correct. Degree $58$ would require 59 entries.

## 10. Boundary divisibility and reduced force

For $2\le r\le59$,


$$
F_r=(b+1)\cdots(b+r)
$$


contains $b+2$, and $p^2\mid b+2$. Hence


$$
p^2\mid F_r,\qquad p^2\mid c_h\quad(h\ge2).
\tag{10.1}
$$


Furthermore,


$$
c_1\equiv F_1=b+1\equiv-1\pmod{p^2},
$$


and


$$
c_0\equiv1+(b+1)2n\equiv1-2n\pmod{p^2}.
\tag{10.2}
$$



Every $d_s$ is divisible by $p$. Thus terms $h\ge2$ vanish in the contact force modulo $p^3$, and the complete reduced contact polynomial is


$$
\begin{aligned}
a_Q(X)\equiv
\sum_{s=1}^{58}d_s(-1)^{s+1}
\sum_{v=1}^s(-1)^v\binom X{s-v}\binom nv
\bigg[
&(1-2n)\binom{b-X+s-1}{v-1}\\
&+\binom{b-X+s}{v-1}
\bigg]\pmod{p^3}.
\end{aligned}
\tag{10.3}
$$


The plus sign on the second term includes both $c_1\equiv-1$ and the change in $(-1)^h$.

This simplification applies only to the contact force. Every $c_h$, $0\le h\le59$, remains necessary for the exterior reconstruction modulo $p^4$.

## 11. Leading contact polynomial and its factor of $p$

To evaluate $a_Q/p\bmod p$:

* $s\ge30$ has $v_p(d_s)\ge2$, so contributes zero;
* $s\le28$ has $\binom nv\equiv0\pmod p$;
* only $s=v=29$ survives.

At the fixed residue class, $m=7$ and


$$
d_{29}/29\equiv7\pmod{29}.
$$


The sign is negative, so the scalar coefficient is


$$
-7\cdot7\equiv9\pmod{29}.
$$


Consequently


$$
\frac{a_Q(X)}p
\equiv
9\left[
\binom{b-X+28}{28}
+\binom{b-X+29}{28}
\right]\pmod p.
\tag{11.1}
$$



Using reflection for generalized binomials and $b\equiv-2\pmod p$, this is coefficientwise


$$
9\binom X{27}+18\binom X{28}.
\tag{11.2}
$$


It is a degree-at-most-$28$ integer-valued polynomial modulo $p$.

If this polynomial is denoted by $a$, then


$$
h_Q\equiv a_Q-p\sum_{s=1}^{29}d_s\mathscr L_{s,b}a
\pmod{p^3}.
\tag{11.3}
$$


The explicit factor $p$ is indispensable. A second subsequent contact has valuation at least $3$ and vanishes.

The analogous calculation for $h_A\bmod p^2$ uses the leading degree-$28$ polynomial $h_0$. In both cases, the surviving corrected Newton degree is at most $57$.

## 12. Fixed receipt versus parameter transfer

The receipt reports:

* $3654$ operator comparisons at one representative;
* 58 coefficients of $h_A\bmod841$;
* 58 coefficients of $h_Q\bmod24389$;
* all 60 boundary coefficients modulo $707281$;
* the leading vector (11.2).

These outputs are not independently recomputed here. The comparison count alone does not specify enough to reconstruct the enumeration, but the algebra above proves the operator simplification independently of that enumeration.

### Kernel transfer within the low-digit cylinder

The bounded kernel coefficients also transfer beyond the representative. A useful elementary estimate is


$$
\binom{z+p^4t}{k}\equiv\binom zk\pmod{p^3},
\qquad 0\le k< p^2,
\tag{12.1}
$$


for integer $z,t$. Vandermonde’s identity proves it using


$$
v_p\binom{p^4t}{a}\ge4-v_p(a)\ge3
\quad(1\le a<p^2).
$$


For $k<p$, the stronger modulus $p^4$ holds.

Apply this to the bounded-index contact formulas:

* rising factorials are integral polynomials and change by multiples of $p^4$;
* binomial parameter changes lose at most one $p$-adic digit in the ranges used;
* contact coefficients supply the required additional powers of $p$;
* the formal moment residues are fixed by the stated low parameter class.

For the boundary, $F_r$ changes by a multiple of $p^4$. Terms $F_r\binom{2n}{r-h}$ with $r\ge2$ also have $v_p(F_r)\ge2$, so a possible one-digit loss in the binomial parameter does not affect modulus $p^4$. The cases $r=0,1$ have lower index at most one and no such loss.

Therefore the indicated kernel vectors and boundary residues are stable for the required precisions on the same low-digit cylinder, with the original odd parity retained. This proves kernel transfer; it does not assert that an arbitrary auxiliary integer belongs to the original power-$3$ domain.

### What still has to be retained in the universal table

The kernel calculation does not replace any of the following:

1. ordinary, coefficientwise low-polynomial identities rather than equality as functions on $\mathbb F_{29}$;
2. actual carry factors before dividing by $p^2$ or $p^3$;
3. the factor $x$ in the unit-boundary $q=-2$ term;
4. both actual high-index ranges
   

$$
0\le J\le h\quad(x\le b_*),\qquad
   0\le J\le h-1\quad(x>b_*);
$$


5. the actual endpoint, including its $+1$;
6. coefficientwise divisibility of the **summed** $H_{\rm flat}$ before division by $p$.

The earlier certificate gap concerning leading low-polynomial identities cannot be filled by the 58-entry kernel receipt alone. If those identities are taken from their separately certified construction, the universal-table transfer applies. Otherwise, the exact outstanding check is their ordinary coefficientwise version—not another contact-operator comparison.

There is no $\Gamma _0$ value in this receipt.

---

# Part III. Global arithmetic compatibility

## 13. What the raw-diagonal exclusion does—and does not—exclude

The handoff retains an all-parity theorem saying that the actual reduced integer error for the **original raw diagonal family** tends to infinity. That excludes a shrinking-form argument for that same rational family.

In particular, it excludes attempts consisting only of:

* multiplying both Gram coefficients by a common factor;
* changing the clearing denominator without changing the reduced fraction;
* a coordinate change accompanied by the corresponding metric transformation so that the rational center is unchanged.

Such changes preserve $p/q$, its reduced denominator, and $qS-p$.

However, the full statement and hypotheses of the linked exclusion note are not reproduced in this packet. It would therefore be unjustified to claim that it excludes every weighted contact construction mentioned here.

The factorial/falling metrics in the prime-$29$ and binary constructions are different metrics from an unweighted raw Gram metric. Keeping a diagonal metric after an arbitrary basis change can also change the rational center. These require their own arithmetic analysis. The A1 triadic construction likewise cannot be classified as the same excluded family merely from the summary provided.

The correct test is equality of the actual rational center, not similarity of formulas or a shared approximation basis.

## 14. Analytic rates must remain attached to their own families

For the sublinear family,


$$
c_W-S=(-1)^{n+1}4\pi M^{-2n-b}(1+o(1)),
\qquad b=o(n).
$$


The centered theorem shows that positive diagonal reweighting in the original coordinates does not yield an exponential improvement.

The fixed-ratio families retain separate rate statements:

* binary: $n=4002b$;
* prime-$29$: $n=2001b$.

Their fixed-ratio error theorems must not be replaced by the sublinear equivalence.

The new handoff’s whole binary result


$$
H\equiv N\pmod{64}
$$


is accepted at its stated parent-family scope. If $N\equiv0\pmod{64}$, it gives only the corresponding lower depth bounds. It does not bound the norm–mixed depth difference, all odd-prime contributions, or the final gcd. No older binary comparison is reopened here.

## 15. The exact joint estimate that would prove irrationality

For the actual rational columns and integral metric scaling, retain


$$
N_B=d_B[u,v],\qquad
A_B=N_{B,1}^{T}\Omega N_{B,1},\qquad
H_B=N_{B,1}^{T}\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_B=A_B/g_B,\qquad p_B=H_B/g_B.
$$


The multiplier relative to the uncleared rational Gram pair is


$$
d_B^2/g_B,
$$


and the whole evaluated form is exactly


$$
q_BS-p_B=q_B(S-c_\Omega).
\tag{15.1}
$$



For the sublinear construction, a sufficient missing statement is an infinite same-index sequence with


$$
\log(A_B/g_B)-(2n+b)\log M\longrightarrow-\infty.
\tag{15.2}
$$


Together with the proved nonzero whole-error law, this gives nonzero integer forms tending to zero.

For a fixed-ratio family with


$$
\log|c_\Omega-S|=-\lambda n+o(n),
$$


a robust sufficient estimate is


$$
\log q_B\le(\lambda-\delta)n
$$


on an infinite admissible sequence, for some $\delta>0$. A finer estimate is possible, but must control the actual $o(n)$ error jointly.

If $S=a/t$ were rational, every nonzero form in (15.1) would have absolute value at least $1/t$. This is the contradiction sought. Neither local congruences nor scalar-error refinements supply it.

## 16. Most promising next arithmetic interface

The next global lemma should address the **uncancelled cofactor**, not another normalization of an excluded raw family.

A precise target is


$$
\sum_{\ell\ {\rm prime}}
\max\{0,v_\ell(A_B)-v_\ell(H_B)\}\log\ell
\le (2n+b)\log M-\omega(n),
\qquad \omega(n)\to\infty,
\tag{16.1}
$$


on an infinite admissible sublinear sequence. The left side is exactly $\log q_B$.

A constructive sufficient version would exhibit an integer common divisor $G_B\mid A_B,H_B$, including all relevant primes, such that


$$
A_B/G_B\le M^{2n+b}e^{-\omega(n)}.
\tag{16.2}
$$


Since $G_B\mid g_B$, this bounds the actual reduced denominator. It does not require pretending that $G_B$ is the full gcd.

This is the most useful arithmetic interface for the present analytic work: a global common-divisor/cofactor certificate in a genuinely different metric family, paired with its own whole-error estimate. Prime-$29$ and binary depth calculations can contribute to it, but only as components. A theorem at one fixed prime and fixed precision cannot establish (16.1).

---

# 17. Bounded exact calculation for coordinator inspection

No numerical calculation is needed to finish the analytic review or the algebraic contact compression.

The remaining immediate finite task is the separate universal $R_C$ table.

### Inputs

* $p=29$, $L=29^4=707281$;
* the supplied 58-entry $h_A\bmod841$ and $h_Q\bmod24389$;
* all $c_h\bmod707281$, $0\le h\le59$;
* reconstruction powers $0,\ldots,58$ for $P$, and $-60,\ldots,58$ for $Q$;
* the explicit four-level stripping data of A2turn23;
* all $0\le x<L$, with original boundary ranges retained.

### Required divisions and certificates

1. Verify local divisibility before every normalization by $p^2$ or $p^3$; do not invert a carry factor or a possibly vanishing high polynomial.
2. Retain the $x$-factor at $q=-2$.
3. Return the nine $T^{(0)}$ residues modulo $841$ and eighteen harmonic residues modulo $29$.
4. Return the ordinary polynomial $H_{\rm flat}(D,J)$ and certify coefficientwise
   

$$
H_{\rm flat}\equiv0\pmod{29}.
$$


5. Divide only after that summation, reconstruct the ordinary degree-at-most-seven polynomial $R_C(D,J)$, and evaluate its 25 specified contractions using ordinary derivatives.
6. If the leading low-polynomial certificate is not already separately available, include it coefficientwise in this run.

### Resource scale

A streaming implementation need not store a length-$b$ inverse or all low-coordinate polynomials. There are at most


$$
707281(59+119)=125896018
$$


coordinate–Laurent pairs before valuation pruning. Each requires bounded four-level arithmetic, followed by fixed-size table accumulation. Working memory can be kept small apart from optional verification logs and kernel precomputations. This is an operation-count scale, not a measured runtime.

The expected output is a reproducible finite table and polynomial certificate—not an assumed zero $\Gamma _0$. No calculation is executed automatically.

---

# 18. Final status

**New reviewed result.** The quantitative centered bound is valid uniformly for $2\le d\le\epsilon n$, with a shrunken pure exponential remainder. The signed first moment is $O(n^{-1})$, and the whole-error and sharp attainable metric-spread conclusions follow with the stated scope corrections.

**New algebraic result.** The prime-$29$ contact compression, leading contact coefficient, 58-coefficient recovery, boundary division, and bounded kernel parameter transfer are justified. The finite receipt does not itself evaluate the universal $R_C$ table.

**Exact remaining bottlenecks.**

* Locally: the separate $R_C/\Gamma _0$ contraction certificate, retaining ordinary coefficients and all boundary terms.
* Globally: an infinite admissible sequence satisfying a final-gcd/cofactor bound such as (15.2) or (16.1), jointly with the appropriate nonzero whole-error theorem.
* Exclusion discipline: no basis or normalization change preserving an already excluded rational center can supply that sequence.



$$
\boxed{\text{The rationality or irrationality of }e+\pi\text{ remains unresolved.}}
$$


