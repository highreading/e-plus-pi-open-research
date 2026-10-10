> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, Turn 10 — Exact bulk–boundary separation at the negative continuation

## Executive conclusion

The leading-degree barrier can be strengthened to an **exact decomposition of every contact operator**. In the Newton basis $E_d(x)=\binom{x}{d}$, one has


$$
\boxed{
\mathscr C_{s;n,b}E_d
=
(-1)^s\binom{n+d+s}{s}E_{d+s}
+
R_{s,d;n,b},
\qquad \deg R_{s,d;n,b}\le s-1.
}
\tag{0.1}
$$



Thus there are no intermediate-degree terms between degrees $s$ and $d+s-1$. All terms other than the displayed bulk term are genuine endpoint contributions of degree at most $s-1$. This statement retains the endpoint $b$; it does not set its contribution to zero.

At $n=-190$, this has two consequences:

* bulk transport cannot cross degree $190$ from below;
* a crossing through an endpoint contribution must use symbol degree at least $191$, whose coefficient has substantial factorial divisibility.

Combining this exact separation with the changed complete force gives the new rigorous bound


$$
\boxed{\mathfrak p_{380}^{*}(-3)\equiv0\pmod{2^{138}}.}
\tag{0.2}
$$


In particular, the proposed precision-$96$ calculation cannot detect this coefficient. Neither can any calculation through precision $138$.

**This does not prove that precision $139$ detects it.** It is the first precision not excluded by the particular estimates proved below, not an evaluated first nonzero precision. I give an exact, endpoint-preserving coefficient recurrence and a small valuation-only screening calculation that should precede any inverse computation.

The limiting valuation, a local $(k+3)$ factor, and the complete grouped scalar content remain unresolved. No tools have been executed.

---

## 1. Scope and source assessment

The original domain is unchanged:


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



Actual contact matrices have indices $0\le i,j<b$. Scalar contractions have indices $0\le j\le b$, with the unchanged partition


$$
0\le t<D,\quad 0\le\rho<128;
\qquad
t=D,\quad 0\le\rho\le80;
\qquad
j=b.
$$



The substitution


$$
h=-95,\qquad n=-190,\qquad b=-95/2001
\tag{1.1}
$$


is made only in the established polynomial continuation. It does not define a negative-sized matrix.

I use the supplied complete central formulas and integral contact transport. Turn 9’s linear filtration follows from its displayed argument; the new argument below needs precisely these two ingredients:

1. a contact contribution of binomial-expansion order $r$ is divisible by $2^r$ and increases degree by at most $4r$;
2. modulo $2^p$, the full iterated solution has degree at most $4p-1$.

The finite reference code is not a calculation at (1.1). Its stated finite checks cannot evaluate the coefficient considered here. Likewise, A4’s corrected shift obstruction is reused only for


$$
v_2(k+3)\ge5.
$$



The classical identities used below—finite summation, Vandermonde, and factorial valuations—are methods, not previously supplied evaluations of this continued operator.

---

## 2. Exact separation of bulk and endpoint terms

Write


$$
E_d(x)=\binom xd,\qquad
\beta_m=\binom bm,
$$


and let $\mathscr S_b$ be the continued suffix operator. The established identity is


$$
\mathscr S_bE_d=\beta_{d+1}E_0-E_{d+1},
\qquad
\mathscr T_{v,b}=\mathscr S_b^v.
\tag{2.1}
$$



### Lemma 1 — Endpoint remainder for an iterated suffix

For every $d,v\ge0$,


$$
\mathscr S_b^vE_d=(-1)^vE_{d+v}+Q_{v,d;b},
\tag{2.2}
$$


where $Q_{0,d;b}=0$ and


$$
\deg Q_{v,d;b}\le v-1\qquad(v\ge1).
\tag{2.3}
$$


The complete endpoint remainder satisfies


$$
\boxed{
Q_{v+1,d;b}
=
(-1)^v\beta_{d+v+1}E_0+\mathscr S_bQ_{v,d;b}.
}
\tag{2.4}
$$



#### Proof

Apply (2.1) to the bulk term in (2.2). The new endpoint constant is
$(-1)^v\beta_{d+v+1}$, and suffix summation increases the degree of the previous remainder by at most one. Induction proves all assertions. ∎

The recurrence (2.4) includes every integration constant. It is not a highest-degree approximation.

### Theorem 2 — Exact contact decomposition

For every $s\ge1$,


$$
\mathscr C_{s;n,b}E_d
=
(-1)^s\binom{n+d+s}{s}E_{d+s}
+
R_{s,d;n,b},
\tag{2.5}
$$


where


$$
\boxed{
R_{s,d;n,b}(x)=
\sum_{v=1}^{s}
(-1)^{s-v}\binom{x}{s-v}\binom nv
Q_{v,d;b}(x-s+v)
}
\tag{2.6}
$$


and $\deg R_{s,d;n,b}\le s-1$.

#### Proof

Substitute (2.2) into the supplied contact formula. For its bulk part, use the exact product identity


$$
\binom{x}{s-v}\binom{x-s+v}{d+v}
=
\binom{d+s}{s-v}\binom{x}{d+s}.
$$


The signs combine to $(-1)^s$, and Vandermonde gives


$$
\sum_{v=0}^s\binom nv\binom{d+s}{s-v}
=\binom{n+d+s}{s}.
$$



Each remainder summand in (2.6) has degree at most


$$
(s-v)+(v-1)=s-1.
$$


This proves the complete identity. ∎

This is the missing strengthening of the leading-coefficient observation. A vanished bulk coefficient does **not** imply vanishing of $R_{s,d;n,b}$, but its entire possible support is now known.

---

## 3. The barrier and telescoping bulk valuations

At $n=-190$, the bulk coefficient is


$$
(-1)^s\binom{d+s-190}{s}.
$$


Hence


$$
d<190\le d+s
\quad\Longrightarrow\quad
\binom{d+s-190}{s}=0.
\tag{3.1}
$$



A path starting below degree $190$ can therefore enter the region $d\ge190$ only through an endpoint remainder.

For a bulk path starting at $d\ge190$, let its successive symbol degrees be $s_1,\ldots,s_q$, and put $S=\sum s_j$. The binomial multipliers telescope:


$$
\boxed{
\prod_{j=1}^q
\binom{d-190+s_1+\cdots+s_j}{s_j}
=
\frac{(d-190+S)!}{(d-190)!\prod_{j=1}^q s_j!}.
}
\tag{3.2}
$$



Thus their exact binary valuation is


$$
L(d-190+S)-L(d-190)-\sum_jL(s_j),
\qquad L(m)=v_2(m!).
\tag{3.3}
$$


It is not appropriate to replace these factors individually by an unspecified one-bit gain. Below the barrier, a crossing product is exactly zero, not a factorial quotient involving negative factorials.

Equation (3.2) is useful both analytically and in a valuation-screening calculation. The simpler bound in §6 does not yet extract all of its possible gain.

---

## 4. Factorial divisibility of the complete contact symbol

At the limiting parameter, write


$$
(1+2U(z))^{-95}-1
=\sum_{s\ge1}\lambda_s z^{[s]},
\qquad z^{[s]}=\frac{z^s}{s!}.
$$


Since


$$
2U(z)=-2z+2z^2-z^3+\frac{z^4}{4},
$$


the ordinary coefficient of degree $s$ in any power of $2U$ has denominator dividing


$$
2^{2\lfloor s/4\rfloor}.
$$


The coefficients $\binom{-95}{r}$ are integers. Therefore


$$
\boxed{
v_2(\lambda_s)\ge a(s):=L(s)-2\lfloor s/4\rfloor.
}
\tag{4.1}
$$



This bound also holds for the sum truncated at any expansion order $r<p$. It does not require cancellation between retained and omitted orders.

Two elementary properties will be useful:


$$
a(s+1)\ge a(s),
\tag{4.2}
$$


and


$$
a(s+4)-a(s)\ge1.
\tag{4.3}
$$


For (4.2), a decrement of $2\lfloor s/4\rfloor$ occurs only at a multiple of four, where the factorial valuation increases by at least two. For (4.3), four consecutive integers contribute at least three powers of two, while the subtracted term increases by two.

In particular,


$$
a(191)=90,\quad a(192)=94,\quad
a(193)=94,\quad a(194)=95.
\tag{4.4}
$$



These are factorial-coefficient bounds, not evaluations of the actual $\lambda_s$. The factor $\binom{-95}{r}$, and cancellation between expansion orders, may improve them.

---

## 5. The changed complete force

The complete force remains


$$
F_i=
\sum_{\ell=0}^i
\binom i\ell
\prod_{t=\ell+1}^i(t-190)\,B_\ell(-95).
\tag{5.1}
$$



For $i\ge190$, every term with $\ell<190$ vanishes exactly. For $\ell\ge190$,


$$
\prod_{t=\ell+1}^i(t-190)
=\frac{(i-190)!}{(\ell-190)!}.
\tag{5.2}
$$


Consequently,


$$
\boxed{
F_i=
\sum_{\ell=190}^i
\binom i\ell
\frac{(i-190)!}{(\ell-190)!}B_\ell(-95)
\qquad(i\ge190).
}
\tag{5.3}
$$



For $m=\lceil\ell/2\rceil$, the falling-factorial part of the central prefactor has valuation


$$
v_2\bigl((-95)_{\underline m}\bigr)
=L(94+m)-L(94)
=m+5-s_2(94+m),
\tag{5.4}
$$


where $L(94)=89$. The remaining affine prefactor factors are odd, and the complete central sum is integral.

Moreover, for both central parities with $j\ge95$, the factor


$$
\binom{h+j}{s}=\binom{j-95}{s}
$$


terminates the sum at $s=j-95$. Thus the entire central input in (5.3) is rational and finitely evaluable. No residue-vector extrapolation or unretained central tail is involved.

For the bounded range $190\le i\le551$, one has


$$
94+\lceil\ell/2\rceil\le370,\qquad
s_2(94+\lceil\ell/2\rceil)\le8.
$$


Hence


$$
v_2(B_\ell(-95))\ge\lceil\ell/2\rceil-3.
$$


The product in (5.2) contains at least $\lfloor(i-\ell)/2\rfloor$ even factors. Termwise in the complete force,


$$
\boxed{
v_2(F_i)\ge\lfloor i/2\rfloor-3
\qquad(190\le i\le551).
}
\tag{5.5}
$$



This deliberately discards additional binomial and central-sum divisibility. It is sufficient for the next theorem.

---

## 6. New vanishing theorem through precision $138$

### Theorem 3

At the continued parameters (1.1),


$$
\boxed{v_2(\mathfrak p_{380}^{*}(-3))\ge138.}
\tag{6.1}
$$



#### Proof

Work modulo $2^{138}$. The complete linear filtration permits a forcing and solution degree cutoff


$$
D=4\cdot138-1=551,
$$


and contact expansion orders $r<138$. Expand the finite Neumann solution into coefficient paths using the exact decomposition (2.5).

Every contact expansion order $r$ has valuation at least $r$ and increases degree by at most $4r$. Therefore, after a path reaches degree $e\le380$, reaching degree $380$ requires additional valuation at least


$$
\left\lceil\frac{380-e}{4}\right\rceil.
\tag{6.2}
$$


Degree decreases cannot invalidate this lower bound.

There are two cases.

**Case A: the path starts at forcing degree $d\ge190$.**

If $190\le d\le380$, (5.5) and (6.2) give


$$
v_2(\text{path})
\ge
\lfloor d/2\rfloor-3
+\left\lceil\frac{380-d}{4}\right\rceil
\ge140.
\tag{6.3}
$$


If $380<d\le551$, the forcing valuation alone is at least $187$.

Thus these paths vanish modulo $2^{138}$.

**Case B: the path starts below degree $190$.**

Consider its first entry into degree $e\ge190$. By (3.1), this cannot be a bulk transition. It must be an endpoint transition, and (2.6) requires


$$
s\ge e+1.
$$


The complete symbol coefficient for that transition has valuation at least


$$
a(s)\ge a(e+1).
$$



For $190\le e\le380$, the path therefore has valuation at least


$$
a(e+1)+\left\lceil\frac{380-e}{4}\right\rceil.
\tag{6.4}
$$


By (4.3), this expression is nondecreasing when $e$ increases by four. It suffices to check $e=190,191,192,193$; the respective bounds are


$$
138,\quad142,\quad141,\quad142.
$$


For $e>380$, (4.2) gives


$$
a(e+1)\ge a(382)=185.
$$



All paths in Case B also vanish modulo $2^{138}$. These cases exhaust the complete coefficient expansion. ∎

### What has, and has not, been determined

The rigorously excluded precision range has increased from


$$
p\le95
\quad\text{to}\quad
\boxed{p\le138}.
$$



The estimate admitting precision $139$ comes from an endpoint crossing near degree $190$, followed by the coarse degree-growth envelope. It does not show that such a path survives the actual endpoint coefficients, bulk factorial factors, or summation cancellations.

Accordingly, I do **not** identify $139$ as the actual first nonzero precision.

---

## 7. Exact coefficient recurrence for the next refinement

Let


$$
R_{s,d;-190,b}=\sum_{e=0}^{s-1}\rho_{s,d,e}E_e.
$$


The numbers $\rho_{s,d,e}$ are exactly defined by (2.4) and (2.6), with $b=-95/2001$.

If


$$
P=\sum_{e\ge0}p_eE_e,\qquad
g=\sum_{e\ge0}g_eE_e,\qquad g_e=(-1)^eF_e,
$$


then the coefficient equation $(I+\mathscr K)P=g$ becomes


$$
\boxed{
p_e+
\sum_{s=1}^{e}
\lambda_s(-1)^s\binom{e-190}{s}p_{e-s}
+
\sum_{s\ge e+1}\lambda_s
\sum_{d\ge0}\rho_{s,d,e}p_d
=g_e.
}
\tag{7.1}
$$



At fixed precision every sum is finite after the established weighted cutoffs.

This recurrence separates:

* a lower-triangular bulk operator;
* an endpoint contribution whose symbol degree must exceed its output degree;
* the complete force.

For $e\ge190$, the bulk sum automatically ignores all $e-s<190$, because the corresponding binomial is zero.

Equation (7.1) is sharper than an associated-graded leading-term recurrence: it is an exact coefficient identity, including the low-degree endpoint feedback from arbitrarily high retained input degrees.

### Concrete follow-on lemma

The next structural target is:

> **High-sector endpoint-content lemma.** Determine the valuation and cancellation of the complete endpoint injection into the sector $e\ge190$ in (7.1), after summing over all input degrees and all symbol orders, and propagate it by the triangular bulk inverse using the factorial quotient (3.2).

This is narrower than computing a dense inverse. It also makes clear why a bulk barrier alone does not prove finite degree or a zero coefficient limit: the endpoint term in (7.1) can inject new high-degree coefficients.

---

## 8. Bounded calculation to perform before any inverse

I recommend **a valuation-screening calculation, not a precision-$139$ dense inverse**.

### Inputs

Use the fixed test precision


$$
p=139,\qquad D=555,
$$


and:

1. the exact continued parameters (1.1);
2. complete force depths obtained from (5.3), with the terminating central formulas;
3. contact expansion orders $1\le r<139$;
4. their exact divided-power coefficients
   

$$
2^r\binom{-95}{r}[z^{[s]}]U^r,\qquad s\le4r;
$$


5. bulk transitions from (2.5);
6. endpoint support $0\le e<s$, initially using integrality alone.

For low forcing indices, the established uniform factorial-depth bound is sufficient for this first screen; no low central sum need be evaluated merely to obtain a valid lower bound.

### Calculation

Perform a finite minimum-cost path calculation on degree states $0,\ldots,555$, with costs equal to certified valuations, capped at $139$.

* A bulk edge $d\to d+s$ includes the exact valuation of
  $\binom{d+s-190}{s}$, with a zero coefficient treated as an absent edge.
* An endpoint edge $d\to e<s$ includes the exact valuation of its symbol coefficient, with zero additional endpoint depth unless separately proved.
* Retain the expansion-order weight as well as the valuation cost, so the original degree–precision filtration is enforced before pruning.

This calculation involves no rational polynomial inverse. It is a finite combinatorial lower-bound calculation. Its result can only strengthen, never weaken, the proved vanishing.

### Expected verifiable output

Return:

1. the minimum certified cost to degree $380$;
2. all predecessor transitions attaining a cost below $139$, if any;
3. a certificate that no discarded state can contribute below that cost;
4. for each candidate bulk chain, agreement between the sum of edge valuations and the factorial quotient (3.3).

If no path survives, precision $139$ is excluded without evaluating a solution. If paths survive, they identify the specific endpoint coefficients $\rho_{s,d,e}$ requiring exact evaluation. Only that reduced set should motivate further arithmetic.

### Independent residual requirement for a later coefficient evaluation

Any subsequently computed $P_p$ must satisfy a coefficient-valued residual checked independently from the bulk–boundary implementation:


$$
\boxed{
(I+\mathscr K_p)P_p-g_p\equiv0\pmod{2^p}.
}
\tag{8.1}
$$



The independent implementation should use the original suffix/contact formula, retaining full intermediate degrees before the complete contact application. A few values at selected rows are not an independent polynomial residual certificate.

No numerical output from this proposed screen or residual check is asserted here.

---

## 9. Uniformity and the original family

The new bound (6.1) is a theorem at $k=-3$. It is **not** the assertion


$$
\mathfrak p_{380}(u)\in2^{138}\mathbb Z_2
\quad\text{for every original }u.
$$



The continued polynomial-residue construction supplies only the following transfer at any fixed precision. If $\Pi_p(k)$ represents the actual coefficient modulo $2^p$, and


$$
2^{\delta_p}\Pi_p\in\mathbb Z_2[k],
$$


then


$$
v_2(k+3)\ge p+\delta_p
\Longrightarrow
\mathfrak p_{380}^{*}(k)\equiv\Pi_p(-3)\pmod{2^p}.
\tag{9.1}
$$


Thus (6.1) transfers to a sufficiently small, explicitly certifiable original-family cylinder once the corresponding denominator bound is supplied.

It does not prove the required unrestricted-depth compensation


$$
v_2(\mathfrak p_{380}^{*}(k))
\ge v_2(k+3)-2.
\tag{9.2}
$$


A fixed lower bound at the limit, however large, cannot substitute for (9.2).

The alternatives remain:

* a finite nonzero limiting residue would refute eventual individual-term compensation on sufficiently deep reachable branches;
* a zero limit would still require a quantitative local theorem, such as
  

$$
\mathfrak p_{380}^{*}(k)=(k+3)G(k),
  \qquad G(k)\in2^{-2}\mathbb Z_2,
$$


  throughout the required neighborhood.

Neither alternative has been established.

---

## 10. Full scalar and primitive arithmetic obligations remain

The result concerns one coefficient of the first solution. It does not prove the whole norm residual


$$
\sum_{j=0}^{b}(F_j^{[p]})^2-8S(C,D)
\equiv0\pmod{2^{2\mu+6}},
$$


nor the separate mixed contraction.

The complete second force remains required, including the exterior factorial force and the logarithmic force except where its whole-input valuation estimate justifies omission at the specified target precision.

The endpoints remain


$$
2X_b=W_b\,b\theta_{b-1},
\qquad
4Y_b=W_b(1+b\eta_{b-1}),
$$


with the $+1$ retained. The accepted nonvanishing $N>0$ and $H\ne0$ is unchanged.

With the least actual clearer $d_B$,


$$
N_B=d_B[u,v],\qquad
A_B=N_{B,1}^{T}\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^{T}\Omega N_{B,2},
$$


the primitive pair is still


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
}
$$


The gcd includes every odd prime; the primitive multiplier remains $d_B^2/g_B$.

The whole evaluated error is


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


No result here controls the full primitive denominator sufficiently to force that entire nonzero form to tend to zero.

---

## Final ledger

### New proved results

1. **Exact bulk–boundary decomposition**
   

$$
\mathscr C_sE_d
   =
   (-1)^s\binom{n+d+s}{s}E_{d+s}
   +R_{s,d},
   \qquad \deg R_{s,d}\le s-1.
$$



2. **Exact negative-parameter barrier:** bulk paths cannot cross degree $190$ from below.

3. **Exact telescoping bulk multiplier:** equation (3.2), with its full factorial valuation.

4. **Complete changed-force reduction:** for $i\ge190$, only $\ell\ge190$ survives, and those central sums terminate.

5. **New coefficient divisibility**
   

$$
\boxed{\mathfrak p_{380}^{*}(-3)\in2^{138}\mathbb Z_2.}
$$



6. **Exact coefficient recurrence** (7.1), retaining every endpoint contribution.

### Exact remaining bottleneck

The immediate unresolved quantity is the **complete endpoint injection into the high-degree sector**, together with its propagation through the factorial-weighted bulk inverse. This, rather than a dense precision-$96$ inversion, is the appropriate next target.

The actual first nonzero precision and limiting valuation remain unevaluated. Precision $139$ is only the next precision permitted by the present proof, and should first undergo the bounded valuation screen in §8.

Beyond the coefficient question remain quantitative general-$k$ compensation or complete grouped content, the full norm and mixed scalar theorems, the full gcd, and the same-index primitive-denominator/whole-error comparison.



$$
\boxed{\text{No unconditional proof or disproof of irrationality of }e+\pi
\text{ is obtained.}}
$$


