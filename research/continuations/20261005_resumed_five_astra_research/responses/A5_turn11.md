> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, Turn 11 — Exact cancellation of all high-sector endpoint injections

## Executive conclusion

The endpoint remainder admits a substantially stronger identity than the degree bound in Turn 10. After summing its integration constants, its Newton coefficient of degree $e<s$ is


$$
\boxed{
[E_e]\,R_sP
=
(-1)^e\binom{n+e}{s}\,
\mathcal L_b\mathscr S_b^{\,s-1-e}P,
}
\tag{1}
$$


where


$$
E_e(x)=\binom xe,\qquad
\mathcal L_bP=\sum_{d\ge0}[E_d]P\,\binom b{d+1}.
$$



Consequently, at the exact continued parameter $n=-190$,


$$
\boxed{
[E_e]\,R_sP=0
\qquad(e\ge190,\ s>e).
}
\tag{2}
$$


**All endpoint injections into the high sector cancel identically.** This is not a valuation estimate, and it does not require replacing the actual endpoint $b=-95/2001$.

The resulting high-sector recurrence can be inverted explicitly. In particular, the coefficient limit is the following **finite rational number**, with no unresolved endpoint inverse:


$$
\boxed{
\mathfrak p_{380}^{*}(-3)
=
190!\,[t^{190}]
\left(1+t+\frac{t^2}{2}\right)^{190}
\sum_{m=0}^{190}\frac{(-1)^mF_{190+m}(-95,-190)}{m!}\,t^m.
}
\tag{3}
$$


Every force entry on the right uses only central indices $190\le\ell\le380$, and every central sum there terminates at depth at most $95$.

A second new result gives a quantitative parameter-continuity estimate:


$$
\boxed{
v_2\!\left(
\mathfrak p_{380}^{*}(k)-\mathfrak p_{380}^{*}(k')
\right)
\ge v_2(k-k')+3.
}
\tag{4}
$$


Thus, **if the finite rational number (3) is zero**, the required individual-term compensation follows, with a stronger bound than requested:


$$
\mathfrak p_{380}^{*}(k)\in8(k+3)\mathbb Z_2.
\tag{5}
$$



I do not claim an unevaluated rational sum to be zero or nonzero. The remaining coefficient decision is now a bounded exact rational calculation, rather than a dense inverse or an all-depth $2$-adic limit calculation. No such calculation has been executed here.

The unconditional irrationality or rationality of $e+\pi$ remains unresolved.

---

## 1. Scope and source audit

The original family is unchanged:


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0,
$$




$$
b=128D+81,\qquad n=128C+66,\qquad C=4002D+2532,
$$




$$
k=2C+1,\qquad h=32k+1,\qquad n=64k+2,\qquad
b=\frac{32k+1}{2001}.
$$



Actual contact matrices retain indices $0\le i,j<b$. Scalar coordinates retain $0\le j\le b$, with full blocks


$$
0\le t<D,\quad0\le\rho<128,
$$


the shortened final block


$$
t=D,\quad0\le\rho\le80,
$$


and the separate coordinate $j=b$.

The substitution


$$
k=-3,\qquad h=-95,\qquad n=-190,\qquad b=-95/2001
\tag{1.1}
$$


is used only in the established polynomial continuation.

### Accepted results reused

I reuse:

* integral Newton-lattice contact transport;
* the complete force formulas and their uniform factorial tails;
* the complete precision–degree envelope
  

$$
\deg P_p\le4p-1\pmod{2^p};
$$


* A4 Turn 12’s accepted actual-family theorem
  

$$
\mathfrak p_{380}(u)\in2^{96}\mathbb Z_2,
  \qquad
  \mathfrak p_{380}^{*}(-3)\in2^{96}\mathbb Z_2;
$$


* the corrected singularity theorem only for $v_2(k+3)\ge5$;
* the stated original-family reachability result.

The two endpoint computations in the supplied JSON retain only their stated finite scope. They are unnecessary for the accepted precision-$96$ theorem.

Turn 10’s bulk–boundary identity and precision-$138$ bound are pending independent audit. Below I give a self-contained derivation of a stronger endpoint identity from the accepted suffix formula. The new reduction does not need the numerical bound $138$.

The literature gate is retained at its stated methodological scope. No cited infinite Hankel, factorial-series, or classical Schur result evaluates the specialized scalar considered here.

---

## 2. Summing every endpoint constant

Put


$$
\mathscr J E_d=E_{d+1},\qquad
\mathcal L_bE_d=\binom b{d+1}.
$$


The exact suffix formula is


$$
\mathscr S_b=-\mathscr J+E_0\mathcal L_b.
\tag{2.1}
$$



For a polynomial $P$, define its endpoint moments


$$
c_t(P)=\mathcal L_b\mathscr S_b^tP,\qquad t\ge0.
\tag{2.2}
$$



### Lemma 1 — Complete integration-constant expansion

For every integer $v\ge1$,


$$
\boxed{
\mathscr S_b^vP
=
(-\mathscr J)^vP+
\sum_{a=0}^{v-1}(-1)^aE_a\,c_{v-1-a}(P).
}
\tag{2.3}
$$



#### Proof

Apply the noncommutative telescoping identity


$$
A^v-B^v=\sum_{a=0}^{v-1}B^a(A-B)A^{v-1-a}
$$


with $A=\mathscr S_b$, $B=-\mathscr J$. Since


$$
A-B=E_0\mathcal L_b,\qquad B^aE_0=(-1)^aE_a,
$$


the result follows. ∎

This formula retains all dependence on $b$, including feedback from high input degrees into the constants $c_t(P)$.

---

## 3. Exact endpoint factorization

The contact operator is


$$
\mathscr C_{s;n,b}P(x)
=
\sum_{v=0}^{s}
(-1)^{s-v}\binom{x}{s-v}\binom nv
\mathscr S_b^vP(x-s+v).
\tag{3.1}
$$



The bulk contribution on $E_d$ is


$$
(-1)^s\binom{n+d+s}{s}E_{d+s}.
\tag{3.2}
$$


Indeed, multiplication of the bulk terms uses


$$
\binom{x}{s-v}\binom{x-s+v}{d+v}
=
\binom{d+s}{s-v}E_{d+s}(x),
$$


followed by Vandermonde.

We now sum the entire endpoint remainder.

### Theorem 2 — Factorization of each endpoint output coefficient

For every $s\ge1$,


$$
\boxed{
R_sP
=
\sum_{e=0}^{s-1}
(-1)^e\binom{n+e}{s}
c_{s-1-e}(P)\,E_e.
}
\tag{3.3}
$$



#### Proof

Substitute the second term of (2.3) into (3.1). For its term indexed by $v,a$, put


$$
e=s-v+a.
$$


Then


$$
\binom{x}{s-v}E_a(x-s+v)
=
\binom e{s-v}E_e(x),
$$


and its sign is $(-1)^e$. Moreover,


$$
v-1-a=s-1-e,
$$


so all contributions to the same output coefficient use the **same endpoint moment**.

For fixed $e<s$, the permissible indices are $s-e\le v\le s$. Hence the coefficient equals


$$
(-1)^ec_{s-1-e}(P)
\sum_{v=s-e}^{s}\binom nv\binom e{s-v}.
$$


Vandermonde evaluates the sum as $\binom{n+e}{s}$. ∎

This is the cancellation missing from a valuation-path treatment in which different endpoint summands are estimated separately.

### Corollary 3 — Complete high-sector endpoint annihilation

At $n=-190$,


$$
R_sP\in\operatorname{span}\{E_0,\ldots,E_{189}\}
\tag{3.4}
$$


for every $s$ and every input $P$.

For if $e\ge190$ and $s>e$, then $e-190$ is a nonnegative integer smaller than $s$, and


$$
\binom{e-190}{s}=0.
$$



This is stronger than “degree $<s$.” It combines **all high-sector injections exactly**, for the actual continued endpoint as well as every other endpoint for which the polynomial identity is defined.

The relation $n=4002b$ is therefore not needed to obtain the cancellation. It is nevertheless preserved when applying the theorem to the actual continuation.

---

## 4. Exact high-sector inverse

Write the complete symbol as


$$
1+\sum_{s\ge1}\lambda_s\frac{z^s}{s!}
=
(1+2U(z))^{-95}.
$$


Its ordinary polynomial base factors exactly:


$$
1+2U(z)
=
1-2z+2z^2-z^3+\frac{z^4}{4}
=
\left(1-z+\frac{z^2}{2}\right)^2.
$$


Thus


$$
\boxed{
1+\sum_{s\ge1}\lambda_s\frac{z^s}{s!}
=
\left(1-z+\frac{z^2}{2}\right)^{-190}.
}
\tag{4.1}
$$



Let $g_e=(-1)^eF_e$. Combining Theorem 2 with recurrence 7.1 gives, for $m\ge0$,


$$
\boxed{
p_{190+m}
+
\sum_{s=1}^{m}
(-1)^s\lambda_s\binom ms p_{190+m-s}
=
g_{190+m}.
}
\tag{4.2}
$$


There is no low-sector input and no endpoint remainder in this equation.

Define formal series over $\mathbb Q_2$:


$$
Q(t)=\sum_{m\ge0}\frac{p_{190+m}}{m!}t^m,\qquad
G(t)=\sum_{m\ge0}\frac{g_{190+m}}{m!}t^m.
$$


Then (4.2) becomes


$$
\left(1+t+\frac{t^2}{2}\right)^{-190}Q(t)=G(t).
$$


Therefore


$$
\boxed{
Q(t)=\left(1+t+\frac{t^2}{2}\right)^{190}G(t).
}
\tag{4.3}
$$



This formal-series argument requires no analytic convergence in the real variable $t$. Each coefficient involves finitely many operations.

The factorial normalization in (4.2)–(4.3) is precisely the telescoping bulk factorial content from Turn 10; no factorial valuation has been discarded.

---

## 5. The coefficient limit is a finite rational expression

At $n=-190$, the complete force satisfies, for $i\ge190$,


$$
F_i
=
\sum_{\ell=190}^{i}
\binom i\ell
\frac{(i-190)!}{(\ell-190)!}\,B_\ell(-95).
\tag{5.1}
$$


Terms with $\ell<190$ vanish because their product contains $n+190=0$.

For every $\ell\ge190$, the relevant central sum terminates because its factor


$$
\binom{h+j}{s}=\binom{j-95}{s}
$$


vanishes for $s>j-95$.

It follows that every $F_i$ in (5.1) is rational. In particular, define


$$
a_r=[t^r]\left(1+t+\frac{t^2}{2}\right)^{190}.
$$


Then


$$
\boxed{
Z:=\mathfrak p_{380}^{*}(-3)
=
190!\sum_{m=0}^{190}
a_{190-m}(-1)^m
\sum_{a=0}^{m}
\binom{190+m}{190+a}\frac{B_{190+a}(-95)}{a!}.
}
\tag{5.2}
$$



For direct exact evaluation,


$$
a_r=
\sum_{q=0}^{\lfloor r/2\rfloor}
\frac{190!}
{q!\,(r-2q)!\,(190-r+q)!}\,2^{-q},
\qquad 0\le r\le190.
\tag{5.3}
$$



### What this establishes

The coefficient limit is not an irreducibly infinite $2$-adic quantity. It is exactly the finite rational number (5.2).

Only central indices


$$
190\le\ell\le380
$$


are needed. Across those indices, the complete terminating central formulas contain


$$
\sum_{j=95}^{190}(j-94)
+
\sum_{j=95}^{189}(j-94)
=
4656+4560
=
\boxed{9216}
$$


central summands before any simplification.

No low central infinite sum, endpoint-moment inverse, or high-sector path screen is needed to evaluate $Z$.

### What remains unproved

I have not evaluated the numerator of (5.2). Consequently, I do not assert either $Z=0$ or $v_2(Z)<\infty$.

The exact remaining coefficient obstruction is now explicit:

> Determine whether the numerator of the finite rational expression (5.2), after exact cancellation, is zero.

A finite exact rational evaluation can decide this question completely. A finite modular zero cannot.

---

## 6. Quantitative parameter continuity

The finite reduction resolves the endpoint difficulty at the limit. A separate estimate resolves the previous lack of a quantitative continuity modulus.

Write


$$
\ell=v_2(k-k').
$$



### 6.1 Complete forcing differences

For $s\ge1$, the standard binomial difference estimate gives


$$
v_2\!\left(\binom{x+\delta}{s}-\binom xs\right)
\ge v_2(\delta)-\lfloor\log_2s\rfloor.
\tag{6.1}
$$


Also,


$$
L(s)=v_2(s!)\ge\lfloor\log_2s\rfloor.
\tag{6.2}
$$



In each central summand, the normalized scalar has depth $L(s)$. Thus its depth pays the entire loss in (6.1). The central prefactors are integral ordinary polynomials in $h$. Since


$$
v_2(h(k)-h(k'))=\ell+5,
$$


the complete central formulas yield


$$
v_2(B_i(h(k))-B_i(h(k')))\ge\ell+5
\tag{6.3}
$$


uniformly in $i$.

The force products are integral polynomials in $n$, and $n(k)-n(k')$ has depth $\ell+6$. Therefore


$$
\boxed{
g(k)-g(k')\in2^{\ell+5}\mathcal M,
}
\tag{6.4}
$$


where $\mathcal M$ is the completed integral Newton lattice used by the accepted construction.

The complete sums converge with their stated factorial tails; (6.4) does not truncate them at a fixed old precision.

### 6.2 Endpoint losses in a contact difference

Consider an input term $a_dE_d$, with $v_2(a_d)\ge w$, followed by symbol order $r\ge1$. The degree envelope implies


$$
d\le4w+3.
\tag{6.5}
$$



In an order-$r$ contact, $s\le4r$. Its $b$-dependence uses binomials $\binom bj$ with


$$
j\le d+s.
$$


The telescoping difference of iterated suffix operators changes one such parameter factor at a time; it does not add the binomial losses from every suffix iteration.

Since $b(k)-b(k')$ has depth $\ell+5$, a $b$-difference has depth at least


$$
\ell+5-\lfloor\log_2(d+s)\rfloor+w+r.
\tag{6.6}
$$


Here the $r$ comes from the complete order-$r$ symbol.

But


$$
d+s\le4(w+r)+3,
$$


and


$$
\lfloor\log_2(4W+3)\rfloor\le W+2
\qquad(W\ge0).
$$


Thus (6.6) is at least $\ell+3$.

The $n$-difference is no worse: its parameter increment has one more bit, and its binomial index is at most $s$.

For the $h$-difference in the symbol, divided-power integrality of $U^r/r!$, together with (6.1)–(6.2), gives depth at least $\ell+5+r$. Hence it too satisfies the required estimate.

Summing the complete retained contributions and passing to the compatible limit yields


$$
\boxed{
(\mathscr K(k)-\mathscr K(k'))P(k')
\in2^{\ell+3}\mathcal M.
}
\tag{6.7}
$$



### Theorem 4 — Uniform Lipschitz gain

Subtract the two exact equations:


$$
(I+\mathscr K(k))(P(k)-P(k'))
=
g(k)-g(k')
-
(\mathscr K(k)-\mathscr K(k'))P(k').
$$


The inverse of $I+\mathscr K(k)$ preserves the integral lattice because $\mathscr K(k)$ is even. Equations (6.4) and (6.7) prove


$$
\boxed{
P(k)-P(k')\in2^{\ell+3}\mathcal M.
}
\tag{6.8}
$$


In particular, (4) follows.

### Consequences for the local factor question

If $Z=0$, then


$$
v_2(\mathfrak p_{380}^{*}(k))
\ge v_2(k+3)+3.
\tag{6.9}
$$


This proves the requested valuation form of local divisibility, more strongly than


$$
v_2(\mathfrak p_{380}^{*}(k))\ge v_2(k+3)-2.
$$



This is a pointwise divisibility theorem; I do not additionally claim a convergent power-series representation of its quotient.

If $Z\ne0$, put $q=v_2(Z)$. Then


$$
v_2(k+3)+3>q
\quad\Longrightarrow\quad
v_2(\mathfrak p_{380}^{*}(k))=q.
\tag{6.10}
$$


On sufficiently deep reachable branches, individual-term compensation consequently fails.

Thus the exact evaluation of (5.2) now decides the individual coefficient-compensation alternative, without a further unproved continuity lemma.

---

## 7. Grouped high-sector suffix identity

Even a nonzero $Z$ would not disprove the full scalar residual. The same decomposition gives a useful exact grouping for that subsequent problem.

For a finite retained polynomial, write


$$
P=P_{<190}+P_{\ge190}.
$$


At the continued parameter, define


$$
H_m=
m!\,[t^m]
\left(1+t+\frac{t^2}{2}\right)^{190}G(t).
$$


Then $p_{190+m}=H_m$, and the high part of the finite suffix reconstruction is exactly


$$
\boxed{
(-1)^j
\sum_{m\ge0}H_m
\sum_{s=0}^{190+m}
\binom{2n+s-1}{s}
\binom{j}{190+m-s}\mathcal M_s(j),
}
\tag{7.1}
$$


with both sums bounded by the retained polynomial degree.

This combines all high-sector coefficients before common-kernel division. It is a regrouping identity, not a content theorem. The low sector remains coupled to endpoint moments and must still be included in the complete scalar.

No single high coefficient, whether zero or nonzero, evaluates


$$
\sum_{j=0}^{b}(F_j^{[p]})^2-8S(C,D)
\pmod{2^{2\mu+6}}.
\tag{7.2}
$$



---

## 8. Bounded exact arithmetic now worth performing

The proposed precision-$139$ valuation screen can retain its intended corroborative role. However, Theorem 2 shows why a screen treating endpoint summands independently may admit paths that cancel identically.

The more decisive bounded task is now the exact rational evaluation of (5.2).

### Inputs

1. $h=-95,\ n=-190,\ b=-95/2001$.
2. Complete central formulas for $190\le\ell\le380$, with their exact terminating limits.
3. Formula (5.1) for $190\le i\le380$.
4. Either:
   * the triangular recurrence (4.2), using the exact symbol (4.1); or
   * the explicit convolution (5.2)–(5.3).

The two routes should be implemented independently for cross-checking.

### Expected verifiable outputs

1. The reduced rational value
   

$$
Z=A/B,\qquad \gcd(A,B)=1,\quad B>0,
$$


   or an exact straight-line certificate for that value.
2. A definitive certificate that $A=0$, or that $A\ne0$.
3. If $A\ne0$,
   

$$
v_2(Z)=v_2(A)-v_2(B).
$$


4. Agreement of the triangular recurrence and polynomial convolution through $m=190$.
5. Compatibility with the accepted $2^{96}$-vanishing.
6. Separately, comparison with Turn 10’s pending $2^{138}$-bound, without assuming that bound to force the output.

This is a finite exact rational computation. It can certify an identically zero limit because (5.2) is an exact equality, not merely a finite-precision approximation.

No expected nonzero residue is asserted. In particular, $139$ is not identified as the first nonzero precision.

---

## 9. Full scalar and primitive arithmetic obligations

The second column remains a separate complete-force problem. Its factorial/exterior input, contact insertions, and logarithmic input are retained. The logarithmic force may be omitted only at the precisions justified by the accepted whole-input estimate.

The endpoints remain


$$
2X_b=W_b\,b\theta_{b-1},
\qquad
4Y_b=W_b(1+b\eta_{b-1}),
$$


including the $+1$.

The full norm and mixed contractions retain every original coordinate, the shortened terminal block, and the separate endpoint. Accepted nonvanishing $N>0$ and $H\ne0$ is unchanged.

With the least actual clearer $d_B$,


$$
N_B=d_B[u,v],\qquad
A_B=N_{B,1}^{T}\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^{T}\Omega N_{B,2},
$$


the final reduction remains


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
}
$$


The gcd includes all primes. The primitive multiplier remains $d_B^2/g_B$.

The whole evaluated error remains


$$
q_n(e+\pi)-p_n=-q_n\epsilon_n>0
\quad\text{eventually},
$$


where


$$
\log|\epsilon_n|
=
-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$


Neither the high-sector cancellation nor a future evaluation of $Z$ supplies the missing bound on the full primitive denominator.

---

## Final ledger

### New results proved here

1. **Exact endpoint factorization**
   

$$
[E_e]R_sP
   =
   (-1)^e\binom{n+e}{s}
   \mathcal L_b\mathscr S_b^{s-1-e}P.
$$



2. **Identical cancellation of all high-sector endpoint injections** at $n=-190$.

3. **Exact factorial-normalized high-sector inverse**
   

$$
Q(t)=\left(1+t+\frac{t^2}{2}\right)^{190}G(t).
$$



4. **A finite rational formula for the coefficient limit**, involving only central indices $190,\ldots,380$ and 9216 terminating central summands.

5. **Quantitative parameter continuity**
   

$$
v_2(\mathfrak p_{380}^{*}(k)-\mathfrak p_{380}^{*}(k'))
   \ge v_2(k-k')+3.
$$


   Therefore a zero limit would imply the required local compensation.

### Exact remaining bottleneck

The immediate coefficient decision is the zero/nonzero status of the finite rational number (5.2). It has not been evaluated in this response.

Beyond that decision remain the complete grouped scalar content, the mixed contraction with the complete second force, the final all-prime gcd, and a same-index comparison of the actual primitive denominator with the whole nonzero evaluated error.



$$
\boxed{\text{No unconditional proof or disproof of irrationality of }e+\pi
\text{ is obtained.}}
$$


