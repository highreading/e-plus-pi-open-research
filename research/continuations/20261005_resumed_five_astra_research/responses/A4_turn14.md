> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4, Turn 14 — Independent audit of the exact binary cancellation and the complete-force endpoint arithmetic

## Executive conclusions

The new binary calculation resolves the earlier individual-coefficient obstruction, once its source formulas are audited. More strongly, the observed finite falling-factorial law has a structural explanation that proves the zero without relying on the numerical evaluation.

The principal conclusions are:

1. **A5turn11’s endpoint factorization is correct.** At $n=-190$, every endpoint injection into Newton degrees at least $190$ vanishes identically. This cancellation includes all endpoint moments and is independent of the value of $b$.

2. **The high-sector inverse and rational-limit formula are correctly normalized.** The coordinator’s code uses the supplied complete central formulas, their correct terminating ranges, the correct force transformation, and the correct factorial normalization. Its two inverse implementations do not independently validate those source formulas, but the formula-level audit below supplies that missing check.

3. **The finite falling-factorial pattern is structural.** At the continued parameter,
   

$$
\boxed{
   p_{190+m}=B_{190}(-95)\,(189)_{\underline m}
   \qquad(m\ge0).
   }
$$


   In particular,
   

$$
\boxed{p_d=0\qquad(d\ge380).}
$$


   This is an exact identity for the continued coefficient system, not an extrapolation from the 191 computed coefficients.

4. **The uniform Lipschitz gain $\ell+3$ passes**, using the accepted complete Newton filtration and complete-symbol integrality. Consequently, on the original family,
   

$$
\boxed{
   v_2\!\left(\mathfrak p_d(u)\right)
   \ge v_2(k+3)+3
   \qquad(d\ge380).
   }
$$


   This strengthens the requested result for $d=380$. It removes the earlier *individual-shift obstruction associated with this coefficient*. It does not evaluate the grouped scalar, the mixed contraction, or the final primitive denominator.

5. **A3turn5’s complete-force recurrence, three-$\tau$ formula, near-factorial strip, endpoint congruence, and stated $3,5,7$-adic consequences pass at their stated scopes.** Its height obstruction and exponential-height compatibility construction also pass. The finite values
   

$$
w_5(15)=2,\quad w_5(30)=3,\quad
   w_5(105)=3,\quad w_5(210)=2
$$


   remain finite results, not a universal valuation law.

No tools were executed. The source code and receipts were inspected as mathematical data; hashes are identifiers, not substitutes for proofs.

**No unconditional proof or disproof of irrationality of $e+\pi$ follows.**

---

## 1. Domains and normalization retained

For the binary construction, the original parameters remain


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0,
$$




$$
b=128D+81,\quad n=128C+66,\quad C=4002D+2532,
$$




$$
k=2C+1,\qquad h=32k+1,\qquad n=64k+2,\qquad
b=\frac{32k+1}{2001}.
$$



The contact matrices retain indices


$$
0\le i,j<b.
$$


The reconstructed columns retain all coordinates $0\le j\le b$: the full $128$-blocks, the final shortened block $0\le\rho\le80$, and the separate endpoint $j=b$.

The value


$$
k=-3,\qquad h=-95,\qquad n=-190,\qquad b=-95/2001
$$


is used only in the accepted compatible polynomial continuation. It is not a replacement of the original finite matrix by a matrix of negative size.

For A3, the distinct construction retains


$$
d=2,\qquad b=3,
$$


a $3\times3$ contact system indexed by $0,1,2$, and reconstructed coordinates $0,1,2,3$. These two constructions are not conflated.

---

# Part I. Exact binary endpoint cancellation

## 2. Audit of the complete endpoint factorization

Write


$$
E_d(x)=\binom xd,\qquad
\mathscr J E_d=E_{d+1},\qquad
\mathcal L_bE_d=\binom b{d+1}.
$$


The accepted finite suffix formula is


$$
\mathscr S_b=-\mathscr J+E_0\mathcal L_b.
$$



For a polynomial $P$, put


$$
c_t(P)=\mathcal L_b\mathscr S_b^tP.
$$


Noncommutative telescoping gives


$$
\mathscr S_b^vP
=(-\mathscr J)^vP+
\sum_{a=0}^{v-1}(-1)^aE_a\,c_{v-1-a}(P).
\tag{2.1}
$$


Every integration constant is present in this expression.

The contact operator is


$$
\mathscr C_{s;n,b}P(x)
=
\sum_{v=0}^s
(-1)^{s-v}\binom{x}{s-v}\binom nv
\mathscr S_b^vP(x-s+v).
\tag{2.2}
$$



For its bulk part,


$$
\binom{x}{s-v}\binom{x-s+v}{d+v}
=
\binom{d+s}{s-v}E_{d+s}(x),
$$


so Vandermonde gives


$$
\mathscr C_{s;n,b}E_d
=
(-1)^s\binom{n+d+s}{s}E_{d+s}+R_sE_d.
\tag{2.3}
$$



For an endpoint term in (2.1), set $e=s-v+a$. Its sign is $(-1)^e$, its moment is always $c_{s-1-e}(P)$, and its remaining coefficient sums to


$$
\sum_{v=s-e}^s\binom nv\binom e{s-v}
=\binom{n+e}{s}.
$$


Thus


$$
\boxed{
R_sP=
\sum_{e=0}^{s-1}
(-1)^e\binom{n+e}{s}
\mathcal L_b\mathscr S_b^{s-1-e}P\,E_e.
}
\tag{2.4}
$$



This proof validates the new factorization directly from the original suffix formula. In particular, it does not estimate separate endpoint constants and then assume cancellation.

At $n=-190$, if $e\ge190$ and $e<s$, then


$$
\binom{n+e}{s}=\binom{e-190}{s}=0.
$$


Therefore


$$
\boxed{[E_e]R_sP=0\qquad(e\ge190).}
\tag{2.5}
$$



The continued endpoint $b=-95/2001$ is retained inside every moment. Its value is immaterial to the vanishing factor, not omitted from the calculation.

### Consequence for the earlier path analysis

The earlier last-endpoint valuation screens allowed transitions that now cancel identically. They remain valid lower-bound arguments, but they are no longer the appropriate mechanism for deciding this coefficient. Their possible surviving paths cannot indicate a nonzero contribution after (2.4) is summed.

---

## 3. Audit of the high-sector inverse and the coordinator’s implementation

At $h=-95$, the complete symbol is


$$
\left(1-2z+2z^2-z^3+\frac{z^4}{4}\right)^{-95}
=
\left(1-z+\frac{z^2}{2}\right)^{-190}.
\tag{3.1}
$$



Let its divided-power coefficients be $\lambda_s$. At output degree $190+m$, the bulk binomial in (2.3) becomes


$$
\binom{m}{s}.
$$


If $s>m$, that coefficient is zero; hence there is no bulk input from below degree $190$. Equation (2.5) eliminates every high-sector endpoint input.

With $g_i=(-1)^iF_i$, the exact recurrence is therefore


$$
p_{190+m}
+\sum_{s=1}^m(-1)^s\lambda_s\binom ms
p_{190+m-s}
=g_{190+m}.
\tag{3.2}
$$


Since $190$ is even, $g_{190+m}=(-1)^mF_{190+m}$.

For exponential generating functions,


$$
Q_*(t)=\sum_{m\ge0}p_{190+m}\frac{t^m}{m!},
\qquad
G(t)=\sum_{m\ge0}(-1)^mF_{190+m}\frac{t^m}{m!},
$$


equation (3.2) gives


$$
\boxed{
Q_*(t)=\left(1+t+\frac{t^2}{2}\right)^{190}G(t).
}
\tag{3.3}
$$



The changed force is also correct:


$$
F_{190+m}
=
\sum_{a=0}^m
\binom{190+m}{190+a}\frac{m!}{a!}B_{190+a}(-95).
\tag{3.4}
$$


Every original force term with central index below $190$ contains the factor $n+190=0$.

### Code-level normalization checks

The supplied coordinator code correctly implements:

- the even prefactor with $t=1,\ldots,j$;
- the odd prefactor with $t=0,\ldots,j$;
- the respective falling factorials of lengths $j$ and $j+1$;
- the scalar denominators $(2s)!$ and $(2s+1)!$;
- generalized binomial coefficients for negative upper arguments;
- the terminating range $0\le s\le j-95$;
- the force multiplier $m!/a!$;
- the sign $(-1)^m$;
- exponential-generating-function factorial normalization.

The symbol recurrence in the code is the coefficient form of


$$
q(z)\phi'(z)=h\,q'(z)\phi(z),
$$


with the correct divided-power coefficients of


$$
q(z)=1-2z+2z^2-z^3+\frac{z^4}{4}.
$$



The count


$$
\sum_{a=0}^{95}(a+1)+\sum_{a=0}^{94}(a+1)=9216
$$


is correct for central indices $190,\ldots,380$.

Thus the receipt establishes the stated exact finite calculation. The following argument supplies an independent structural reason for its result.

---

## 4. Structural cause of the falling-factorial law

The central formulas permit an exact generating-function evaluation.

It is useful to perform the algebra with


$$
h=-H,\qquad n=-2H,\qquad H\ge1,
$$


and then specialize to $H=95$. This generalization is an algebraic identity for the displayed central formulas; it is not an assertion that all such parameters belong to the original family.

Put


$$
\lambda=2H,\qquad B_* = B_{2H}(-H).
$$


The initial coefficient is nonzero:


$$
B_*=(2H-1)!!\,(H)^{\overline H}
=\frac{(2H)!}{2^H H!}\frac{(2H-1)!}{(H-1)!}.
\tag{4.1}
$$



### 4.1 The shifted central coefficients

For $a\ge0$, direct division of the central prefactors by $B_*$ gives


$$
\frac{B_{2H+2a}(-H)}{B_*}
=
(-1)^a(2a-1)!!(\lambda)^{\overline a}
\,{}_2F_1\!\left(-a,\lambda+a;\frac12;\frac12\right),
\tag{4.2}
$$


and


$$
\frac{B_{2H+2a+1}(-H)}{B_*}
=
(-1)^{a+1}(2a+1)!!(\lambda)^{\overline{a+1}}
\,{}_2F_1\!\left(-a,\lambda+a+1;\frac32;\frac12\right).
\tag{4.3}
$$


Both hypergeometric expressions terminate at $a$. For example,


$$
\frac{2^s(s!)^2}{(2s)!}
\binom{-\lambda-a}{s}\binom as
=
\frac{(-a)^{\overline s}(\lambda+a)^{\overline s}}
{(1/2)^{\overline s}s!}\,2^{-s}.
$$


The odd formula follows in the same way with $3/2$.

These finite sums are exactly the even and odd coefficient formulas for


$$
(1+x+x^2/2)^{-\lambda}.
$$


For completeness, define $C_r^\lambda(y)$ by


$$
(1-2yz+z^2)^{-\lambda}
=\sum_{r\ge0}C_r^\lambda(y)z^r.
$$


Expansion of the binomial series gives


$$
C_{2a}^\lambda(y)
=(-1)^a\frac{(\lambda)^{\overline a}}{a!}
\,{}_2F_1(-a,\lambda+a;1/2;y^2),
$$




$$
C_{2a+1}^\lambda(y)
=(-1)^a\frac{2(\lambda)^{\overline{a+1}}}{a!}\,
y\,{}_2F_1(-a,\lambda+a+1;3/2;y^2).
$$


Substitute $y=-1/\sqrt2$, $z=x/\sqrt2$, and multiply the coefficient of $x^r$ by $r!$. The results are precisely (4.2)–(4.3).

Consequently,


$$
\boxed{
\sum_{a\ge0}B_{2H+a}(-H)\frac{x^a}{a!}
=
B_*(1+x+x^2/2)^{-2H}.
}
\tag{4.4}
$$



This identity is over formal rational power series. It does not require a real convergence argument.

### 4.2 Transforming the complete force

Let the left side of (4.4) be $C_*(x)$. From the exact changed-force formula,


$$
\begin{aligned}
G(t)
&=\sum_{m\ge0}(-1)^m\frac{F_{2H+m}}{m!}t^m\\
&=(1+t)^{-2H-1}
C_*\!\left(-\frac{t}{1+t}\right).
\end{aligned}
\tag{4.5}
$$


Indeed, for each fixed $a$,


$$
\sum_{m\ge a}\binom{2H+m}{2H+a}(-t)^m
=(-t)^a(1+t)^{-2H-a-1}.
$$



Now


$$
1-\frac{t}{1+t}
+\frac{t^2}{2(1+t)^2}
=
\frac{1+t+t^2/2}{(1+t)^2}.
$$


Equations (4.4)–(4.5) therefore imply


$$
G(t)
=
B_*(1+t)^{2H-1}(1+t+t^2/2)^{-2H}.
\tag{4.6}
$$


Multiplication by the exact high-sector inverse yields


$$
\boxed{Q_*(t)=B_*(1+t)^{2H-1}.}
\tag{4.7}
$$



At $H=95$,


$$
\boxed{
p_{190+m}=B_{190}(-95)(189)_{\underline m}
\qquad(m\ge0).
}
\tag{4.8}
$$



The falling factorial has a zero factor for every $m\ge190$. Thus


$$
\boxed{\mathfrak p_d^*(-3)=0\qquad(d\ge380).}
\tag{4.9}
$$



This proves the coordinator’s observed law, extends it beyond the finite checked range, and independently proves


$$
\mathfrak p_{380}^*(-3)=0.
$$



---

## 5. Audit of the uniform Lipschitz gain

The continuity argument is valid, but its logical dependencies should remain explicit:

- complete factorial tails for the central force;
- the accepted precision–degree filtration;
- integrality of the complete contact construction;
- evenness of the complete contact perturbation.

Let


$$
\ell=v_2(k-k').
$$


Then


$$
v_2(h-h')=\ell+5,\quad
v_2(n-n')=\ell+6,\quad
v_2(b-b')=\ell+5.
$$



### 5.1 Complete-force differences

For $x,\delta\in\mathbb Z_2$,


$$
v_2\!\left(\binom{x+\delta}{s}-\binom xs\right)
\ge v_2(\delta)-\lfloor\log_2s\rfloor.
\tag{5.1}
$$


This follows from Vandermonde and


$$
\binom{\delta}{j}=\frac{\delta}{j}\binom{\delta-1}{j-1}.
$$



In both central sums, the scalar coefficient has valuation $v_2(s!)$, and


$$
v_2(s!)\ge\lfloor\log_2s\rfloor.
$$


Thus the scalar pays the binomial-difference loss. The prefactors are integral ordinary polynomials in $h$. Taking the complete factorially convergent sums gives


$$
B_i(h)-B_i(h')\in2^{\ell+5}\mathbb Z_2.
$$


The remaining force products are integral polynomials in $n$, so


$$
g(k)-g(k')\in2^{\ell+5}\mathcal M.
\tag{5.2}
$$



### 5.2 Contact differences

For a Newton coefficient of valuation $w$, the accepted envelope gives


$$
d\le4w+3.
$$


An expansion-order-$r$ contact has symbol degree $s\le4r$, scalar depth at least $r$, and endpoint binomial indices at most $d+s$.

A telescoping parameter difference changes one endpoint factor at a time. All other factors remain integral. Hence the loss is the maximum relevant binomial loss, not a sum of losses over suffix iterations:


$$
v_2(\text{changed term})
\ge
\ell+5+w+r-\lfloor\log_2(d+s)\rfloor.
$$


Since


$$
d+s\le4(w+r)+3,\qquad
\lfloor\log_2(4W+3)\rfloor\le W+2,
$$


the result is at least $\ell+3$.

For the symbol’s $h$-dependence, the useful normalization is


$$
\binom hr(2U)^r
=
2^r(h)_{\underline r}\frac{U^r}{r!}.
$$


The divided-power integrality of $U^r/r!$ and ordinary-polynomial integrality of $(h)_{\underline r}$ give difference depth at least $\ell+5+r$. The $n$-difference has one additional parameter bit and is no worse.

The estimates also justify passage to the compatible limit: as the input valuation or contact order grows, the bound


$$
w+r-\lfloor\log_2(4(w+r)+3)\rfloor
$$


tends to infinity.

Therefore


$$
(\mathscr K(k)-\mathscr K(k'))P(k')
\in2^{\ell+3}\mathcal M.
\tag{5.3}
$$


Subtracting the two complete equations and using the integral inverse of $I+\mathscr K(k)$ gives


$$
\boxed{
P(k)-P(k')\in2^{\ell+3}\mathcal M.
}
\tag{5.4}
$$



### Strengthened actual-family theorem

Combining (4.9) and (5.4) proves:

> **High-tail compensation theorem.**  
> On the original family $b=9^{18+32u}$, $n=4002b$, $u\ge0$, every continued Newton coefficient of degree $d\ge380$ satisfies
> 

$$
> \boxed{
> \mathfrak p_d(u)\in8(k+3)\mathbb Z_2.
> }
>
$$


> Equivalently,
> 

$$
> v_2(\mathfrak p_d(u))\ge v_2(k+3)+3.
>
$$



For $d=380$, the accepted all-family precision-$96$ result remains available as well:


$$
v_2(\mathfrak p_{380}(u))
\ge\max\{96,\ v_2(k+3)+3\}.
$$



This is pointwise divisibility. It does not assert that the quotient is represented by a convergent ordinary power series.

---

# Part II. Audit of A3turn5

## 6. Complete-force recurrence and terminal forcing

Let


$$
Q(z)=1-z+\frac{z^2}{2},\qquad
\mathscr H(z)=\frac{e^z+f(z)}{1-z},
\quad f'(z)=\frac2{Q(z)},\quad f(0)=0.
$$


Differentiating


$$
(1-z)\mathscr H'-\mathscr H=e^z+2/Q
$$


$n$ times is legitimate and gives the stated equation.

With


$$
R_n=Q^{n+1}(1/Q)^{(n)},
$$


one obtains exactly


$$
R_{n+1}=QR_n'-(n+1)Q'R_n.
$$


For $A_n=Q^n\mathscr H^{(n)}$,


$$
(1-z)QA_n'
-\left[1+(n-1)z-\frac{n-1}{2}z^2\right]A_n
=e^zQ^{n+1}+2R_n.
$$


Extracting divided-power coefficients yields


$$
\begin{aligned}
a_{N+1}^{(n)}
={}&(2N+1)a_N^{(n)}
+\frac{N(2n+1-3N)}2a_{N-1}^{(n)}\\
&+\frac{N(N-1)(N-n-1)}2a_{N-2}^{(n)}
+\mathcal B_N^{[n+1]}+2N![z^N]R_n.
\end{aligned}
$$


The signs and coefficients pass.

The initial value $a_0^{(n)}=\mathcal W_n$ and the entire $R_n$ force are necessary. The logarithmic/arctangent contribution is present in both.

The terminal coefficient


$$
[z^n]R_n=(-1)^n\frac{(n+1)!}{2^n}
$$


also passes. At an odd prime dividing $n$, its terminal forcing has valuation $2v_p(n!)$, since $n+1$ is a unit.

---

## 7. Three-$\tau$ stripping and the complete-force strip

The substitution $z=x/(1+x)$ gives


$$
t_i=\operatorname{CT}_x
(x^{-1}+1+x/2)^n x^{-i}(1+x)^i.
$$


If $a_j=[x^j](x^{-1}+1+x/2)^n$, then $a_{-j}=2^ja_j$. Consequently,


$$
t_0=\tau_n,\qquad
t_1=\frac{\tau_n+\tau_{n+1}}2,\qquad
t_2=\frac{\tau_{n+2}}2.
$$


Thus the displayed factorial-stripped first force is correct.

For the logarithmic force, a summand has the exact form


$$
2q_j\,N!\,n!\binom{2n+i-j}{n}\frac{\alpha_{r-1}}r,
\qquad N=n+i,\quad r\le2n+2.
$$


For $p>2$, $p\mid n$, $i=0,1,2<p$,


$$
v_p(N!)=v_p(n!).
$$


All factors other than $r^{-1}$ are $p$-integral. Therefore


$$
w_i^{\log}\in
p^{\,2v_p(n!)-\lfloor\log_p(2n+2)\rfloor}\mathbb Z_{(p)}.
$$


Since the actual row-scaled inverse is $p$-integral, the endpoint strip follows.

**Precision clarification:** “agreement through depth $K_p(n)$” means congruence modulo $p^{K_p(n)}$. It does not certify the next digit.

---

## 8. Endpoint congruence and exact valuations

The endpoint normalization is


$$
v_0=1-s_n^Ty,\qquad
s_n=(1,-n,n(n+1))^T.
$$


The $+1$ is essential.

For the exponential companion, write $y^{\exp}=\mathbf1+e$, with $e\in p^s\mathbb Z_{(p)}^3$, $s=v_p(n)$. The first row and endpoint identities give


$$
v_0^{\exp}\equiv-f_0\pmod{p^{2s}},
\qquad f=w^{\exp}-C\mathbf1.
$$



The exact first-row expansion is


$$
f_0=
\sum_{j=0}^n q_jn^{\underline j}
\left[F(2n-j)-1-(n-j)^2\right].
$$


For $j\ge1$,


$$
v_p(q_jn^{\underline j})
\ge
2s+v_p((j-1)!)-v_p(j).
$$


The only possible deficit for odd $p$ is at $j=p$; there the bracket supplies the missing factor of $p$. Hence


$$
f_0\equiv F(2n)-1-n^2\pmod{p^{2s}}.
$$



Finally,


$$
x^{\underline t}
=(-1)^{t-1}(t-1)!\,x+x^2P_t(x),
\qquad P_t\in\mathbb Z[x],
$$


proves


$$
\boxed{
v_0\equiv-2n\mathfrak D_p
\pmod{p^{\min(2s,K_p(n))}},
\qquad
\mathfrak D_p=\sum_{r\ge0}(-1)^rr!.
}
$$



The small exact evaluations


$$
\mathfrak D_3\equiv2\pmod3,\quad
\mathfrak D_7\equiv4\pmod7,\quad
\mathfrak D_5\equiv20\pmod{25}
$$


give precisely the claimed results:


$$
v_3(v_0)=v_3(n)\quad(15\mid n),
$$




$$
v_7(v_0)=v_7(n)\quad(105\mid n),
$$




$$
v_5(v_0)\ge v_5(n)+1\quad(15\mid n),
$$


and


$$
v_5(v_0)=v_5(n)+1
\quad(15\mid n,\ 25\mid n).
$$



The required modulus strictly exceeds the leading valuation in each asserted exact case. For $v_5(n)=1$, the modulus does not decide the next digit.

The attached receipt correctly exhibits that distinction:


$$
\begin{array}{c|rrrr}
n&15&30&105&210\\ \hline
v_5(v_0)&2&3&3&2.
\end{array}
$$


It disproves the guess that all four probes have $w_5=2$. It does not prove a residue-class law for all indices.

---

## 9. Height obstruction and compatible cancellation

The threshold-height argument passes without applying a fixed-target approximation theorem to the moving residue.

From


$$
a-k=n_{\mathcal P}b,\qquad n=rn_{\mathcal P},
$$


and the fixed-width window, the constructed rational


$$
x=\frac{2b-rnk}{rk}
$$


satisfies


$$
\left|x-(1-3\sqrt2)\right|\le\frac{2(C+1)}n.
$$


Its reduced denominator is at most $rk$. The nonzero integer


$$
P^2-2PQ-17Q^2
$$


then gives


$$
k\ge
\sqrt{\frac{n}{2(6\sqrt2+1)(C+1)}}\,\frac1r.
$$


Since $a/k\asymp n^2$, the height bound


$$
\max(|a|,k)\gg_C n^{5/2}/r
$$


follows.

This excludes bounded-denominator weights when $r$ is bounded. It does not exclude polynomial height of sufficiently large degree.

The exponential-height compatibility construction also passes:

- $K=L+1$ is coprime to $L$;
- choosing $A_*$ in the required progression retains all local congruences;
- reduction of $A_*/K$ divides only by a factor coprime to $L$;
- the constructed weight stays a fixed positive distance from the actual threshold;
- the exact whole-error identity consequently proves nonvanishing and the stated error scale.

Its arithmetic conclusion remains limited: selected-prime cancellation coexists with analytic improvement, but no favorable all-prime primitive-denominator bound has been established.

The dual-vector criterion is valid as an exact absence certificate. Producing suitably short dual vectors on an infinite original-index family remains an open lemma, not a consequence of generic lattice geometry.

---

# Part III. What remains necessary for irrationality

## 10. Full primitive arithmetic is not replaced by coefficient compensation

For the binary construction, retain the least actual clearer $d_B$ and


$$
N_B=d_B[u,v],
$$




$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2}.
$$


The accepted mixed nonvanishing is unchanged. The final arithmetic is


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
}
$$


The gcd is over all primes, and the primitive multiplier is $d_B^2/g_B$.

The reconstructed endpoints remain


$$
2X_b=W_b\,b\theta_{b-1},
\qquad
4Y_b=W_b(1+b\eta_{b-1}).
$$


The second endpoint’s $+1$, complete exterior force, and complete logarithmic force remain present.

The whole evaluated error remains


$$
q_n(e+\pi)-p_n=-q_n\epsilon_n>0
\quad\text{eventually},
$$


with


$$
\log|\epsilon_n|
=-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$



For A3, retain instead its exact endpoint gcd decomposition:


$$
q_\lambda=\frac{kh|AB|}{FGH_{\rm gcd}},
\qquad
p_\lambda=\operatorname{sgn}(AB)\frac{T}{FGH_{\rm gcd}}.
$$


Its whole evaluated form is


$$
\boxed{
|q_\lambda(e+\pi)-p_\lambda|
=
q_\lambda|e_3\alpha_{n,2}|\,
|\lambda-\Lambda_{n,2}|.
}
$$



Neither a zero high-sector tail at a continued parameter nor selected-prime resonance controls either complete primitive denominator.

---

## 11. Concrete follow-on lemmas and bounded calculations

### 11.1 Immediate binary follow-on lemma

The former coefficient-limit decision is closed. A useful next target is now:

> **Grouped complete-force relative-content lemma.**  
> Use the exact high-sector polynomial
> 

$$
> Q_*(t)=B_{190}(-95)(1+t)^{189}
>
$$


> and the actual high-tail compensation to evaluate the grouped norm and mixed residuals, including the low-sector endpoint moments, every original coordinate, and the complete second force.

The obstruction is precise: the low sector remains endpoint-coupled, and the mixed contraction contains force components not determined by the first-column high-sector identity. No termwise compensation theorem alone evaluates those contractions.

### 11.2 Small structural binary certificate

No further calculation is needed to prove $p_{380}^*(-3)=0$. A compact independent consistency certificate would nevertheless be useful.

**Inputs**

- The 191 exact central values already computed;
- $B_*=B_{190}(-95)$;
- the differential equation
  

$$
(1+x+x^2/2)C_*'(x)=-190(1+x)C_*(x).
$$



**Expected output**

For $0\le r\le189$, verify exactly


$$
B_{191+r}
=-(190+r)B_{190+r}
-\frac{r(379+r)}2B_{189+r},
$$


with the $r=0$ second term omitted, and verify the nonzero initial value (4.1).

This checks the central-source normalization directly, rather than merely cross-checking two inverses using the same central data. Its finite scope is explicit; the proof of (4.4) supplies the all-index identity.

### 11.3 A3’s next bounded $5$-adic calculation

The proposed $625$-class computation is mathematically well posed after retaining its scope:

- use the truncated polynomial expressions $q_0,\ldots,q_{14}$;
- replace the exponential factorial sum modulo $125$ by its first 15 falling-factorial terms;
- compute the endpoint with the exterior $+1$;
- inspect $n=5t$, $0\le t<625$.

The coefficient-denominator bound justifies period $5^5$ modulo $125$. The expected output is


$$
t\longmapsto v_0^{\exp}/25\pmod5,
$$


with zero classes explicitly listed. At actual indices with $K_5(n)\ge3$, the same table applies to the complete endpoint modulo $125$.

A nonzero entry proves exact valuation $2$ in that class under those hypotheses. A zero entry proves only valuation at least $3$; it does not establish exact valuation $3$.

---

## Final proof-status ledger

### New result

The central formulas imply the exact structural identity


$$
\boxed{
\sum_{m\ge0}p_{190+m}\frac{t^m}{m!}
=
B_{190}(-95)(1+t)^{189}.
}
$$


Together with the audited complete Lipschitz estimate, this proves the strengthened actual-family theorem


$$
\boxed{
\mathfrak p_d(u)\in8(k+3)\mathbb Z_2
\qquad(d\ge380).
}
$$



Thus the exact zero in the coordinator’s receipt is not merely a finite modular contact, and the earlier individual-shift obstruction for $p_{380}$ is removed.

### Remaining mathematical bottleneck

The unresolved task is to control the **complete grouped scalar and mixed contraction**, and ultimately the **actual primitive denominator after the full all-prime gcd**, on the same original indices for which the **whole evaluated error is nonzero and sufficiently small**.

For A3’s resonant construction, the corresponding unresolved task is an infinite-family short-reconstruction or dual-height theorem for the actual moving residue, followed by that same all-prime denominator and whole-error comparison.

The cited classical identities and approximation literature do not supply these missing actual-force statements automatically.



$$
\boxed{
\text{No unconditional proof or disproof of irrationality of }e+\pi
\text{ has been obtained.}
}
$$


