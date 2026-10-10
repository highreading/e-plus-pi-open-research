> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Research report: audit of Family017 and the new finite-producer arithmetic

## 1. Scope and principal conclusions

This report audits the complete supplied Family017 manuscript first, followed by A2 Turn 9 and A5 Turn 7. No tools or computations were used. References below are to the supplied file names, section headings, and equation labels; no external bibliography, formalization, or repository claim is treated as additional verification.

The conclusions are as follows.

1. **Family017:** I find that the supplied argument does reconstruct its separated, center-uniform interpolation theorem, rather than merely invoking a dimension count. In particular, the local multiplicity comparison, the persistent-component argument, and the passage through an ordinary blowup address the principal potential gaps in that theorem. Subject to the standard algebraic-geometric results explicitly identified below, the subsequent nonvanishing, Gaussian-integer clearing, analytic determinant estimates, and parameter choices give the claimed conclusion for $\pi$. This is a mathematical audit of the supplied proof, not a claim about external referee acceptance or Lean verification.

2. **No transfer to $e+\pi$:** Even accepting $\mu(\pi)=2$, Family017 supplies no implication that $e+\pi$ is irrational. Its application depends on exact logarithmic periods with algebraic exponential values. The supplied mixed producer does not satisfy a demonstrated analogue of those hypotheses.

3. **A2 Turn 9:** The exact initial-charge determinant
   

$$
f_0^0r_1^F-f_1^0r_0^F
   =-\frac{2^{n+1}(n!)^2}{b!}
$$


   is verified on its unchanged original family. This is an actual evaluated obligation, not merely a reformulation. Its propagation through the complete finite inverse is valid under the explicitly reused recurrence identities. Its proposed factorial-content transfer remains conditional on unevaluated complete exponential-channel divisibility and clearing losses.

4. **A5 Turn 7:** The infinite exclusion of content one on $u\equiv1\pmod4$ is verified using the previously accepted modulo-$8$ criterion, without reopening that calculation. The short-adjoint algebra and finite hockey-stick evaluation are correct. Their application at depth $L$ still requires the stated complete finite-completion theorem and its actual return. The all-prime least-clearer and column-content identities are also verified in the actual corrected columns.

5. **Global objective:** None of these results establishes, on the same infinite original indices,
   

$$
p_n,q_n\in\mathbb Z,\qquad q_n>0,\qquad
   0<|q_n(e+\pi)-p_n|\longrightarrow0.
$$


   The remaining obstruction is an asymptotically adequate estimate for the **actual primitive denominator**, after the all-prime final gcd, paired with the **whole nonzero error**.

The two original producer families must not be identified with one another. Their parameters, normalizations, and arithmetic information differ.

---

# Part I. Family017

## 2. The precise interpolation assertion

In `interpolation.tex`, Theorem `geom:interpolation` fixes


$$
m,K\ge1,\qquad w_0,v_0>0,\qquad 0<\theta<1
$$


with


$$
K\theta^m<1,\qquad K(w_0/v_0)\theta^m<1.
$$


It then chooses $w_1,\ldots,w_m$ successively, independently of the centers.

For


$$
W=(w_0,w_1,\ldots,w_m),\qquad
V=(v_0,w_1/\theta,\ldots,w_m/\theta),
$$


the claimed surjection is


$$
\mathcal P_W(H)\longrightarrow
\bigoplus_{j=0}^{K-1}\mathcal J_V(H),
$$


given by


$$
P\longmapsto
P\bigl(1+t,c_{j1}+u_1+\log(1+t),\ldots,
c_{jm}+u_m+\log(1+t)\bigr).
$$


The target retains exactly the coefficients satisfying


$$
v_0s+\sum_i(w_i/\theta)\beta_i<H.
$$



The quantifiers matter:

- thresholds for the successive weights cannot depend on the centers;
- each coordinate list $c_{0i},\ldots,c_{K-1,i}$ must be pairwise distinct;
- the eventual threshold for $H$ may depend on the centers;
- $H$ tends to infinity only after all those data have been fixed.

A favorable leading dimension count alone would not prove this assertion. The manuscript supplies additional geometric arguments, audited next.

## 3. Local multiplicity: the claimed uniformity is justified

The local lemma `geom:multiplicity` compares a coordinate normal basis $A$ and a commuting-field normal basis $B$ for the same component $Z$.

Its hypotheses include:

- polynomial equations of weighted degree at most $N$;
- $Z$ an irreducible component of their zero set;
- a commuting analytic frame;
- vanishing on $Z$ of all derivatives with cost less than $\varepsilon N$.

At a suitable smooth point of $Z$, the $B$-flows give transverse parameters $b_1,\ldots,b_k$. Persistence means that the equations contain no transverse monomial of weight below $\varepsilon N$.

A coordinate slice in the directions $A$ is transverse to $Z$. On that slice the $b$'s remain analytic coordinates. Substitution of the remaining local coordinates as analytic functions of $b$ cannot create a monomial of lower positive weight. Thus the local quotient length is at least


$$
\#\left\{\alpha\in\mathbb Z_{\ge0}^k:
\sum_{b\in B}\kappa_b\alpha_b<\varepsilon N\right\}.
$$


The unit-cube argument gives the stronger bound


$$
\#\{\cdots\}\ge
\frac{(\varepsilon N)^k}{k!\prod_{b\in B}\kappa_b}.
$$


The paper uses only half this bound.

The upper bound is also properly weighted. After taking $k$ generic constant linear combinations of the equations, use


$$
x_a=\lambda_a+z_a^{M_0\rho_a}.
$$


Choose $\lambda_a$ so that the preimages of the point are unramified. There are


$$
\prod_{a\in A}M_0\rho_a
$$


such preimages, each preserving the local intersection length, and the substituted equations have ordinary degree at most $M_0N$. The isolated-zero Bézout bound consequently gives


$$
\operatorname{length}\le
\frac{N^k}{\prod_{a\in A}\rho_a}.
$$



Combining the bounds proves the manuscript's inequality


$$
\prod_{a\in A}\rho_a
\le 2k!\varepsilon^{-k}\prod_{b\in B}\kappa_b.
$$



**Audit decision.** This lemma is justified under the standard isolated-intersection Bézout theorem used in its proof. It does not require a hidden analytic radius estimate or a threshold depending on the equations or component.

## 4. Separated weights and the persistent-component argument

### 4.1 Separation really is center-independent

Equation `geom:separation` requires


$$
\prod_{a\in A}w_a>C_*\prod_{b\in B}v_b
$$


when the largest positive index in $A\triangle B$ belongs to $A$.

For such a pair, let that largest differing index be $i$. The ratio is $w_i$ times an expression depending only on earlier weights and fixed parameters. An index larger than $i$ belongs to both sets or neither; if it belongs to both, it contributes


$$
w_j/v_j=\theta.
$$


Thus increasing $w_i$ enforces the required finite list of inequalities without involving any center coordinate. This establishes the required order of choice.

### 4.2 From excess contact to derivative persistence

If the curve inequality failed, the dimension count supplies a nonzero $F_N$ of degree at most $N$ with order at least $(1+3\sigma)N$ at every center.

The commuting fields


$$
D_0=Y\partial_Y+\sum_i\partial_{X_i},
\qquad D_i=\partial_{X_i}
$$


preserve weighted polynomial degree. In the formal interpolation coordinates they are


$$
D_0=(1+t)\partial_t,\qquad D_i=\partial_{u_i},
$$


so their order costs are at most $v_0,v_i$, respectively.

Derivatives of total cost at most $\sigma N$ therefore retain branch orders at least


$$
(1+2\sigma)Nh_P.
$$


The pole degree of any nonzero restriction to the curve is at most $N\deg_W C$. Under the assumed violation, the zero degree exceeds that pole degree. Hence all those derivative restrictions vanish.

The nested derivative zero sets contain the curve. Their selected irreducible components have dimensions between $1$ and $m$, so the $m+3$ levels force an adjacent repeated component. The local multiplicity lemma applies to that persistent component with


$$
\varepsilon=\sigma/(m+2).
$$



### 4.3 Why persistence forces $Y$ to be constant

Choose the largest positive coordinate direction $\partial_{X_i}$ that is nontangent to the persistent component.

Some coordinate normal basis contains it. If a frame normal basis omitted $D_i$, the separation inequality would contradict the multiplicity comparison. Every frame normal basis must therefore contain $D_i$.

Consequently, all the other frame vectors fail to span the normal quotient. Their ambient span is


$$
\ker(dX_i-dY/Y),
$$


so


$$
dX_i=dY/Y
$$


on the component.

If $Y$ were nonconstant, restriction to a suitable algebraic curve and passage to its smooth complete model would yield a contradiction: $dY/Y$ has a nonzero residue at a zero or pole of $Y$, while the exact differential $dX_i$ has residue zero everywhere.

If every positive coordinate direction is tangent, properness directly forces $dY=0$. Thus $Y$ is constant in either case.

The subsequent argument in the fiber $Y=1$ is also substantive. The coordinate and differential normal bases now coincide. Separation forces a unique normal-basis index set, hence some $X_i$ is constant on the persistent component. Coordinatewise distinctness permits at most one prescribed center on the curve. For a nonconstant coordinate $X_l$, zero–pole comparison then gives


$$
\deg_W C\ge\theta^{-1}\sum h_P
>(1+\sigma)\sum h_P.
$$



**Audit decision.** The curve inequality is proved by the supplied argument. In particular, its use of coordinatewise distinctness occurs at a necessary and identifiable point; it is not an unstated generic-position assumption.

## 5. From curve positivity to the exact coefficient packets

The final subsection of `interpolation.tex` must handle two issues: weighted formal ideals and ordinary powers on a potentially singular projective scheme.

The paper handles them as follows.

Choose $R$ so that every $R/w_a$ and $R/v_a$ is integral. The monomial projective compactification has


$$
L\cdot C=R\deg_W C.
$$


Replace each logarithm by a fixed Taylor polynomial with omitted terms of weight greater than $v_i$. This preserves both branch contact and every finite weighted quotient.

At each center use the algebraic ideal


$$
I_j=(t^{R/v_0},(u_1')^{R/v_1},\ldots,(u_m')^{R/v_m}).
$$


For each branch,


$$
\operatorname{ord}_P I=Rh_P.
$$



On the ordinary blowup,


$$
I\mathcal O_{X'}=\mathcal O_{X'}(-E),\qquad A=p^*L.
$$


The curve inequality proves that $A-(1+\sigma)E$ has nonnegative degree on every noncontracted curve. Contracted curves have positive $-E$-degree by relative ampleness. Thus the class is nef.

For sufficiently large $a$, $aA-E$ is ample, and the displayed identity


$$
A-E=
\frac{a-1}{a(1+\sigma)-1}\bigl(A-(1+\sigma)E\bigr)
+\frac{\sigma}{a(1+\sigma)-1}(aA-E)
$$


has the correct coefficients. Nef-plus-ample therefore makes $A-E$ ample.

The remaining standard inputs are:

1. eventual graded-piece recovery and higher direct-image vanishing for a standard Noetherian Rees algebra;
2. projection formula and Leray;
3. Serre vanishing;
4. eventual surjectivity from ambient homogeneous polynomials to sections of $L^n$.

These give, for sufficiently large $n$,


$$
H^1(X,I^nL^n)=0.
$$


Crucially, the argument uses **ordinary powers** $I^n$, and only eventually. It does not assert equality with integral closures or with the weighted order ideal. The inclusion


$$
I^n\subseteq\{\text{weight}\ge nR\}
$$


is in the correct direction: surjectivity modulo the smaller ideal implies surjectivity onto the desired smaller quotient.

**Proof status.** On these standard geometric inputs, whose required projectivity, Noetherianity, integrality, and coherent-ideal hypotheses are supplied, the separated interpolation theorem is established. I do not identify an unfilled center-uniformity step in the supplied proof.

## 6. Determinant nonvanishing and rational integerization

In `determinant.tex`, logarithms are replaced by


$$
G_i(t)=\sum_{1\le k<T_i}\frac{(-1)^{k+1}}k t^k,
\qquad
T_i=\left\lceil F_0w_i/v_0\right\rceil .
$$


The first omitted weight satisfies


$$
v_0T_i\ge F_0w_i>w_i/\theta.
$$


Thus the replacement is an invertible filtered coordinate change.

The rows remain exactly


$$
0\le j<K,\qquad s,\beta\ge0,\qquad
v_0s+w\beta/\theta<H,
$$


and the columns satisfy


$$
w_0h+w\alpha\le H.
$$


Interpolation gives full row rank, hence a nonzero square minor $\Delta_H$ using **all** rows.

For arithmetic clearing, the manuscript scales:

- column $\alpha$ by $\prod_iq_i^{\alpha_i}$;
- row $\beta$ by $\prod_iq_i^{-\beta_i}$;
- every resulting entry by
  

$$
D_H=\prod_i\operatorname{lcm}(1,\ldots,T_i-1)^{\lfloor H/w_i\rfloor}.
$$



The resulting determinant is a nonzero Gaussian integer. Therefore


$$
\log|\Delta_H|
\ge-M\log D_H
-\sum_{\rm columns}\alpha\cdot\log q
+\sum_{\rm rows}\beta\cdot\log q.
$$


The row scaling is a genuine payment; it is not omitted from the inequality.

Writing


$$
\bar b=\frac1{MH}\sum_{\rm rows}w\beta,
$$


the estimates give


$$
\frac{\log|\Delta_H|}{MH}
\ge -(1-\bar b)-E_{\rm ar},
$$


with exactly the printed


$$
E_{\rm ar}
=\frac{4\log2\,F_0m}{v_0}
+4\log2\sum_i\frac1{w_i}
+\frac{\theta}{w_*}.
$$



This integerization is valid. It is not, and need not be, a claim of least clearing or primitive determinant content.

## 7. The analytic estimate and incompatible bounds

The translated functions are


$$
f_{a,P}(z)=[u^a]P(e^z,z+u_1,\ldots,z+u_m).
$$


For a monomial,


$$
f_{a,P}(z)=\binom{\alpha}{a}e^{hz}z^{|\alpha|-|a|}.
$$



The exact row identity in `det:row-identity` retains:

- rational-approximation shifts $j(r_i-\omega)$;
- every logarithmic truncation tail;
- all transverse indices;
- all Taylor orders needed for the original row.

A nonzero tail coefficient obeys


$$
wd<H/F_0.
$$


Thus the loss of approximation-error powers caused by tails is paid by the term $\nu/F_0$ in $E_{\rm tr}$.

Within a fixed transverse group $a$, repeated Taylor degrees give identical coefficient rows and annihilate a determinant summand. Distinct degrees force


$$
\sum d\ge\sum_a\binom{n_a}{2}.
$$


The geometric-series estimate therefore gives


$$
|\det T|
\le
\exp\left\{-\frac{\log2}{4}\sum_an_a^2
+MH(E_{\rm hol}+o(1))\right\}.
$$


The $o(1)$ is uniform because all dimensions, weights, and centers are fixed before $H\to\infty$.

The two alternatives are correctly compared:

- at least $\eta M$ indices have $wa\le AH$, giving collision saving $cL$;
- otherwise the approximation factors give saving
  

$$
\nu(A(1-\eta)-\bar b).
$$



Since $\bar b\le\theta$,


$$
\nu(A(1-\eta)-\bar b)-(1-\bar b)
\ge
\nu(A(1-\eta)-\theta)-(1-\theta)=g.
$$



The parameter construction in `conclusion.tex` checks the needed strict margins. In particular,


$$
A^2<\theta
$$


allows


$$
A/\theta<C<1/A,
$$


followed by


$$
A<B<\min(1/C,C\theta).
$$


Consequently,


$$
K/w_0\to0,\qquad v_0\to\infty,\qquad
L=\frac{\eta^2(B/A)^m}{2(m+1)}\to\infty.
$$


After fixing such an $m$, unbounded approximation denominators allow the successive weight thresholds to be met. Their center independence is exactly what avoids circularity.

**Audit conclusion for Family017.** The supplied mathematical chain supports its claimed exponent-two theorem on the standard geometric inputs specified in §5. I find no separate arithmetic or analytic gap after interpolation. This conclusion does not rely on the catalogue wording or the existence of a Lean link.

The dyadic-spacing lemma in `series.tex` is also valid. Its applications to Flint–Hills convergence and the generalized convergence criterion follow from the exponent bound; they supply no additional mixed-period theorem.

## 8. Why this does not prove anything decisive about $e+\pi$

Family017 uses


$$
\omega=2\pi i,\qquad e^{j\omega}=1,
$$


and rational centers approximating these exact logarithmic periods. This gives both the rational matrix and the common entire test functions used in the collision argument.

Replacing $\pi$ by $e+\pi$ would destroy that verified setup:


$$
e^{2i(e+\pi)}=e^{2ie},
$$


for which the supplied work establishes none of the necessary algebraic or rational integerization properties.

More basically, if $e+\pi=r\in\mathbb Q$, then $\pi=r-e$. Rational translation and sign preserve irrationality exponent, so this would imply


$$
\mu(\pi)=\mu(e).
$$


There is no contradiction: the classical exponent of $e$ is also two.

Thus even the joint assertions $\mu(e)=\mu(\pi)=2$ do not settle their sum.

---

# Part II. A2 Turn 9

## 9. Original scope and the evaluated determinant

The unchanged A2 domain is


$$
u=2+29^9t,\quad t\ge0,\qquad
b=3^{249005515+574312172u},\qquad n=2001b.
$$


Hence every original $n$ is odd.

The contact range is $0\le i,j<b$, recurrence rows are $1\le i\le b-2$, and reconstruction is $0\le j\le b$. The split


$$
b=29^3B+5044
$$


retains its unequal block endpoints. Nothing in the determinant evaluation alters these boundaries.

### 9.1 Verification of the initial-charge evaluation

A2 §3 introduces


$$
R(t)=t^2-t+\tfrac12,\qquad
p_n(t)=\frac1{n!}\frac{d^n}{dt^n}R(t)^n.
$$


The roots are $\zeta_\pm=(1\pm i)/2$. The defining recurrence for $L_m$ gives


$$
\frac{L_m}{m!}
=\frac2i\int_{\zeta_-}^{\zeta_+}\frac{1-t^m}{1-t}\,dt.
$$


This is a polynomial integral, with no logarithm branch issue.

Repeated integration by parts proves


$$
\int_{\zeta_-}^{\zeta_+}p_n(t)t^k\,dt=0\quad(k<n),
$$


because $R(t)^n$ has endpoint zeros of order $n$.

The source identifications are correct:


$$
f_0=2^ne_n,\qquad
f_1=2^{n-1}(n+1)(e_{n+1}+e_n),
$$


where $e_n=p_n(1)$, and


$$
\ell_0=(n!)^2d_n,\qquad
\ell_1=\frac{(n!)^2(n+1)}2(d_{n+1}+d_n),
$$


where $\ell_i=b!r_i^F$.

Both $e_n$ and $d_n$ satisfy


$$
(n+1)y_{n+1}=(2n+1)y_n+ny_{n-1}\qquad(n\ge1),
$$


with


$$
(e_0,e_1)=(1,1),\qquad(d_0,d_1)=(0,4).
$$


Their Casoratian therefore satisfies


$$
\mathcal W_n=-\frac n{n+1}\mathcal W_{n-1},
\qquad
\mathcal W_n=\frac{4(-1)^n}{n+1}.
$$


Substitution yields


$$
f_0\ell_1-f_1\ell_0=2(-2)^n(n!)^2.
$$



This verifies the actual new evaluation


$$
\boxed{f_0r_1^F-f_1r_0^F=-G_n,\qquad
G_n=\frac{2^{n+1}(n!)^2}{b!}.}
$$



## 10. Complete finite propagation and payments

Using the explicitly reused homogeneous source recurrence,


$$
f^0=f_0h^{(0)}+f_1h^{(1)},\qquad
r^F=r_0^Fh^{(0)}+r_1^Fh^{(1)},
$$


the determinant evaluation gives


$$
f_0r^F-r_0^Ff^0=-G_nh^{(1)}.
$$


Thus


$$
f_0Y-r_0^FZ_w=f_0Y^e-G_n\mathcal RA^{-1}h^{(1)}.
$$



Here


$$
Y^e=\mathcal RA^{-1}r^e+W_be_b.
$$


The physical terminal is retained with coefficient $f_0$ on both sides. The same finite inverse is used throughout, so its finite returns are not removed.

The division-free form is preferable at arbitrary primes. At $29$, division by $f_0$ is legitimate under the retained unit theorem. The logarithmic adjoint contribution is exactly


$$
-\eta_1G_n/f_0.
$$


The all-prime valuation formula


$$
v_\ell(G_n)=(n+1)\mathbf1_{\ell=2}
+2v_\ell(n!)-v_\ell(b!)
$$


is immediate and correct.

### What is not established

The equality above does not make $G_n$ a divisor of the final mixed scalar.

A2 Theorem 6.1 is a correct elementary transfer statement:


$$
F\mid G_n,\quad F\mid A_B,\quad F\mid I_B+C_B
\quad\Longrightarrow\quad
\frac{F}{\gcd(F,m_Bf_0)}\mid g_B.
$$


Its significant hypotheses are still open. In particular:

- $m_B$ is an additional rational-clearing payment;
- $d_B$ remains the actual least simultaneous column clearer;
- existing contents cannot be counted again as new gcd savings;
- no factorial-scale complete exponential residue has been evaluated.

The actual final quantities remain


$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B,
$$


over **all primes**, with primitive multiplier $d_B^2/g_B$.

Under the retained whole-error theorem,


$$
\epsilon_n\ne0\ \text{eventually},\qquad
\log|\epsilon_n|
=-\left(2+\frac1{2001}\right)\log(1+\sqrt2)\,n+o(n).
$$


The relevant error is still $-q_n\epsilon_n$, not one source contribution.

---

# Part III. A5 Turn 7

## 11. The infinite content exclusion is verified

The A5 family is separately


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
$$


Its contact range is $0\le j<b$, and its physical range is $0\le j\le b$.

I reuse, without recalculation, the accepted criterion


$$
a=1\iff
\exists\,s\in[0,d],\ s\text{ even}:
v_2\binom gs+v_2\binom{h+d-s}{d-s}=1,
$$


together with $a\ge1$.

The lifting formula gives


$$
v_2(9^{32t}-1)=8+v_2(t).
$$


The divisions defining $d,h,g$ are paid by knowing $b$ modulo $2^{k+2}$. For $u\equiv1\pmod4$,


$$
b\equiv977\pmod{1024},\qquad
(d,g,h)\equiv(244,81,161)\pmod{256}.
$$



The eight-bit exclusion in A5 §2 is valid:

- With no subtraction borrow, even $s$ is one of $0,16,64,80$ modulo $256$. Then $d-s$ and $h$ share bits $5$ and $7$, producing at least two carries.
- With exactly one subtraction borrow and no addition carry, the low word of $d-s$ has bits $0,5,7$ unset and is at most $94$. The only possible single outgoing-borrow patterns force $d-s$ to have bit $5$ set, a contradiction.

Full Kummer cost is at least prefix cost. Therefore


$$
\boxed{a(u)\ge2\quad\text{for every }u\equiv1\pmod4.}
$$



This is an infinite original-family result. It is not an exact higher-content theorem and gives no asymptotic denominator saving.

## 12. Short adjoint: valid algebra, conditional finite application

The exact telescope is


$$
\sum_{j=0}^{b}x_j=S/2,\qquad
S=\sum_{j=0}^{b-1}(n+1-j)W_jz_j^f.
$$


Hence primitive norm parity requires


$$
Q\equiv S/2^{a+1}\pmod2.
$$


One must know $S$ modulo $2^{a+2}$, or use a sufficient proved upper bound for $a$.

The adjoint algebra in A5 §3 is correct. Starting from


$$
\sum_j\ell_jt^j=(n+1-t)(1+t)^{n+1},
$$


right multiplication by $U_{-n}$ gives


$$
(n+1)+nt-t^2.
$$


Since


$$
c_0=1,\qquad c_1=n,\qquad c_2=n^2,
$$


the divided-power multiplication produces


$$
(n+1)-nt-t^2.
$$


After the second $U_{-n}$,


$$
\boxed{\sum_{k\ge0}\mu_kt^k
=((n+1)-nt-t^2)(1+t)^{-n}.}
$$



The six-product expression for $\mathcal H_i(B)$ follows from finite hockey-stick summation and the identities for $\binom{j+1}{i}$ and $\binom{j+2}{i}$. It is an evaluated contact sum, not a renamed original-length sum.

However, its application remains


$$
S\equiv
\sum_{i=0}^{I}(-1)^i\mathfrak f_i\mathcal H_i(b-1)
+\sum_{v=0}^{m-1}\mu_{b+v}(\eta_f)_v
\pmod{2^L}.
$$


The return $\eta_f$ is essential. Higher symbol coefficients disappear from the observation but not from that return.

The source telescope in A5 §4 also retains its terminal:


$$
\sum_{t=0}^{T}a_t\ell_{b+t}+W_b
=a_{T+1}W_{b+T+1}.
$$


Only after this equality may the last term be discarded modulo $2^L$. Its factorial coefficient contains $2L$ consecutive factors when $T=2L-1$, so it has at least $L$ factors of two.

Neither linear acceptance is the mixed quadratic observation $E-rQ$. The payment


$$
E-rQ=2^{-2a-2}\bigl(2^{a-1}\mathcal V-r\mathcal U\bigr)
$$


and the logarithmic guard remain necessary.

The complete finite-completion theorem at general $L$ is explicitly reused by A5; its full proof and the definitions of every Schur-system block are not reproduced in the supplied excerpt. My independent verification here establishes the new adjoint algebra and its consequence **under that stated finite-completion premise**, not a fresh proof of the premise.

## 13. Actual all-prime saturation and cofactor identity

The corrected columns give exactly


$$
u=\mathsf D\zeta,\qquad v=e_0+\mathsf D\rho.
$$


Consequently,


$$
\sum_ju_j=0,\qquad \sum_jv_j=1.
$$


Both the complete second force and the physical terminal are needed.

Integral partial sums invert these transformations, proving


$$
d_B=\operatorname{lcm}(D_\zeta,D_\rho).
$$


Writing


$$
c_\zeta=\gcd_j|D_\zeta\zeta_j|,
$$


minimality gives


$$
\gcd(c_\zeta,D_\zeta)=1.
$$


The difference map preserves coordinate gcd, so


$$
c_U=\frac{d_B}{D_\zeta}c_\zeta.
$$


The minimally cleared second column has content one: a common prime would divide its coordinate sum $D_\rho$ and, by partial sums, every $D_\rho\rho_j$, contradicting minimality. Hence


$$
c_V=\frac{d_B}{D_\rho}.
$$



Writing $D_\zeta=gr$, $D_\rho=gs$, with $\gcd(r,s)=1$, proves


$$
\boxed{\gcd(c_U,c_V)=1.}
$$



This uses classical integer-lattice algebra, but its application is an actual evaluated assertion about the complete producer: shared column content is exactly one.

The primitive minor gcd $M$ satisfies


$$
M\mid D_\rho
$$


by summing minors against the coordinate-sum identities. This does not control the scalar norm/mixed gcd. The example printed in A5 §5.3 correctly demonstrates that independent primitive vectors can still have a common norm/inner-product factor.

Finally,


$$
A_B=c_U^2N^\circ,\qquad H_B=c_Uc_VH^\circ.
$$


With


$$
\delta=\gcd(c_U,|H^\circ|),
$$


coprimality of $c_U,c_V$ gives exactly


$$
\boxed{
q_n=\frac{c_U}{\delta}
\frac{N^\circ}
{\gcd(N^\circ,|c_VH^\circ/\delta|)}.
}
$$


This is generic gcd algebra correctly specialized to the actual columns. It does not evaluate either scalar cofactor.

The retained ternary law


$$
v_3(q_n)=n-\frac{b+15}{2}
$$


must remain part of every denominator comparison. A fixed binary content improvement does not remove it.

---

# Part IV. Remaining work and verification plan

## 14. Concrete follow-on obligations

### A2: complete exponential-residue transfer

The evaluated logarithmic determinant isolates a specific remaining task. On an explicitly infinite subset of


$$
u=2+29^9t,
$$


one must construct a specified factorial-floor product $F_n\mid G_n$ and prove


$$
F_n\mid A_B,\qquad I_B+C_B\equiv0\pmod{F_n},
$$


while bounding the loss


$$
\gcd(F_n,m_Bf_0)
$$


and subtracting factors already present in known contents.

Naming $I_B+C_B$ is not a solution. A useful next lemma must evaluate its complete exponential response, including finite returns and normalization.

### A5: paid infinite acceptance and scalar cofactors

A concrete sufficient norm-parity lemma would give, on an infinite original subfamily,


$$
a(u)\le A(u),\qquad
S(u)\equiv0\pmod{2^{A(u)+2}},
$$


using the full head-plus-return formula.

Even that would only be a local norm result. The global task still requires aggregate control of


$$
\gcd(c_U,|H^\circ|),\qquad
\gcd(N^\circ,|c_VH^\circ/\delta|),
$$


not merely minor saturation or first-column content.

## 15. Bounded exact arithmetic

No repeated modulo-$8$ calculation or old sampled certificate is needed.

The genuinely new finite target is A5's proposed $u=0$, depth-$12$ acceptance:


$$
b=150094635296999121,\qquad n=4002b,
$$




$$
L=12,\quad I=94,\quad m=44,\quad T=23,\quad V=67.
$$


The scope condition reduces to $n>838$, which holds.

The seed truncation is paid: for $r\ge16$,


$$
v_2(r!)\ge12,
$$


and the largest effective binary denominator among the retained $r\le15$ terms is $2^{11}$. Thus the proposed $h\bmod2^{23}$ input suffices for a falling-factorial implementation at modulus $4096$.

The expected certificate should report:

1. all retained seed residues;
2. the $95$-entry force head modulo $4096$;
3. the actual $44\times44$ Schur matrix, right-hand side, and verified solution;
4. all $44$ return entries;
5. separate head and return contributions;
6. $S(0)\bmod4096$.

If $S(0)=0\bmod4096$, the accepted bound $a(0)\le10$ proves $Q(0)$ even. Otherwise, the result supplies only the valuation of $S(0)$ below $12$, with any remaining dependence on $a(0)$ stated explicitly.

**Acquisition limitation:** the supplied text names, but does not fully define, all matrices used to build that Schur system. Therefore the coordinator must attach the accepted finite-completion definitions before authoring the calculation. Omitting them would leave an incompletely specified arithmetic task. No numerical output is asserted here, and no finite output would prove an infinite acceptance law.

## 16. Final proof-status ledger

| Result | Status after this audit |
|---|---|
| Family017 center-uniform interpolation | Verified on the stated standard geometric inputs |
| Family017 determinant nonvanishing and integerization | Verified |
| Family017 analytic comparison and parameter order | Verified |
| Family017 implication for $e+\pi$ | None established |
| A2 exact initial-charge determinant | Verified evaluated identity on every original index |
| A2 complete reconstructed identity | Verified under the reused finite recurrence/inverse framework |
| A2 useful factorial-scale final gcd divisor | Open |
| A5 $a\ge2$ for $u\equiv1\pmod4$ | Verified infinite original-family result |
| A5 short-adjoint algebra | Verified |
| A5 higher-depth finite application | Conditional on the stated complete finite-completion theorem |
| A5 actual coprime column contents | Verified all-prime assertion |
| A5 relative scalar-cofactor formula | Verified exact identity, not an asymptotic estimate |
| Same-index integer/nonzero/denominator/whole-error criterion | Not established |
| Rationality or irrationality of $e+\pi$ | Unresolved |

## Conclusion

The substantial reusable progress is specific:

- Family017 supplies a separated logarithmic interpolation and determinant mechanism with checked quantifiers, but no demonstrated mixed logarithm–exponential transfer.
- A2 evaluates the previously unresolved two-charge determinant and proves that a single homogeneous logarithmic direction cannot suffice.
- A5 proves an infinite content-one exclusion, shortens an actual norm acceptance to a finite head plus the actual return, and rules out shared complete-column content after least simultaneous clearing.

The exact remaining global bottleneck is not integerization alone, local content alone, or determinant nonvanishing alone. It is a sufficiently strong **all-prime scalar cancellation estimate for the actual primitive denominator**, valid on the **same infinite original indices** as a proved **nonzero whole-error estimate**.

Until that joint estimate is supplied, the unconditional rationality or irrationality of $e+\pi$ remains open.
