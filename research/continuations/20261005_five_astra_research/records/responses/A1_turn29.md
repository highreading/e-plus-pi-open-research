> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Terminal Jacobi resonance at $A_*=243/4$

## 1. Scope and outcome

The proposed coefficientwise dominance inequalities do fail on the original power-of-four index domain. For the first resonant terms, the exact relative valuations are


$$
\boxed{
v_3(E_{0,123})=133-t,\qquad
v_3(E_{1,125})=136-t,\qquad
v_3(E_{2,127})=134-t,
}
\tag{1}
$$


whenever


$$
t=v_3(4^{j+1}-247)\ge7.
$$


Such congruence classes are compatible both with $81\mid j$ and with the prescribed real window.

This is **not yet a counterexample to the proposed valuations of the evaluated polynomials**. Terms containing the same denominator must be summed. Below I give their exact grouping, a convergent polar-residue series, and a fixed, small exact-arithmetic calculation that determines whether its leading residue is nonzero.

There is an additional uniformity issue: the residue of this locally defined infinite series cannot automatically be substituted for the original, variable-degree polynomial. I identify that issue explicitly. Thus this report proves the coefficient obstruction and advances a concrete grouped-residue lemma, but does not claim a completed terminal valuation or an irrationality result.

### Source and verification boundary

I have read the supplied turn28 in full. On the present domain $v_3(j)\ge4$, its accepted force/support result supplies the local polynomial congruence at its stated precision. Its $v_3(j)=1$ extension is outside this assignment and is not used.

The dyadic $n+2$ and endpoint-valuation results remain separate archive dependencies, as requested; their absence from some supplied packets is not a contradiction.

No archive-access or browsing tool is available here. Consequently I cannot claim a fresh external search. The supplied search record and DLMF 18.5.E7 are retained as provenance for the classical hypergeometric framework, not as evidence for the valuation claims below. The nine auxiliary controls neither sample the original power-four domain nor resolve this resonance.

---

## 2. Exact first-resonance calculation

Retain


$$
A=4^j-1,\qquad s=\frac{A+1}{2}+b,\qquad
r_0=\frac{A+71}{3},\qquad b\in\{0,1,2\},
$$


and


$$
E_{b,u}=(-1)^u\binom{s}{u}
\prod_{i=0}^{u-1}\frac{A+2b-2i}{4A+1+4b-2i}\,r_0^{-u}.
$$



Set


$$
\epsilon=4A-243=4^{j+1}-247,\qquad
I_b=122+2b,\qquad U_b=I_b+1.
$$


Then


$$
4A+1+4b-2i=\epsilon+2(I_b-i).
\tag{2}
$$


In particular, the factor with $i=I_b$ is exactly $\epsilon$, with valuation $t$.

At $A_*=243/4$,


$$
s_*=\frac{247+8b}{8},\qquad
A_*+2b-2i=\frac{243+8b-8i}{4}.
$$


The denominators $4$ and $8$ are $3$-adic units.

### Fixed valuation table

For $u=U_b$, the relevant sums at $A_*$ are


$$
\begin{array}{c|r|r|r}
 &b=0&b=1&b=2\\ \hline
U_b&123&125&127\\
\displaystyle\sum_{\ell=0}^{U_b-1}v_3(247+8b-8\ell)
 &64&65&65\\
v_3(U_b!)&59&59&61\\
\displaystyle\sum_{i=0}^{U_b-1}v_3(243+8b-8i)
 &63&64&64\\
\displaystyle\sum_{\substack{0\le i<U_b\\i\ne I_b}}
v_3\bigl(2(I_b-i)\bigr)
 &58&59&61
\end{array}
\tag{3}
$$



Here is a direct check of the less immediate entries. For $b=0$, the numerator-factor sum is


$$
5+\left\lfloor\frac{122}{3}\right\rfloor+
\left\lfloor\frac{122}{9}\right\rfloor+
\left\lfloor\frac{122}{27}\right\rfloor+
\left\lfloor\frac{122}{81}\right\rfloor
=63.
$$


For the falling-factorial numerator $247-8\ell$, the counts at depths $1,\ldots,6$ are


$$
41,\ 14,\ 5,\ 2,\ 1,\ 1,
$$


whose sum is $64$. The last factor, at $\ell=122$, equals $-729$.

The $b=1,2$ lists are shifts of these lists. The additional nonunit factors contributing to the displayed totals are $255$, of valuation $1$, and $-741$, of valuation $1$. Legendre’s formula gives the factorial entries.

All fixed nonzero factors in (3) have valuation at most $6$. Therefore, when $t\ge7$, replacing $A_*$ by the actual $A$ preserves every entry of this table. Also $v_3(r_0)=-1$. Substitution proves (1).

Consequently:
- for $b=0$, the proposed bound $w_0(u)\ge1$ fails for $t\ge133$;
- for $b=1$, its analogue fails for $t\ge136$;
- for $b=2$, the proposed bound $w_2(u)\ge0$ fails for $t\ge135$.

These statements concern coefficients normalized by the leading evaluated term, not the valuation of their sum.

---

## 3. Grouping the shared denominator exactly

For an actual admissible integer $A$, define


$$
T_b(A)=r_0^{-s}p_s(r_0).
$$


Split its finite sum at the first resonance:


$$
T_b(A)=
\sum_{u=0}^{I_b}E_{b,u}(A)
+\frac{1}{\epsilon}
\sum_{u=U_b}^{s}R_{b,u}(A),
\tag{4}
$$


where


$$
R_{b,u}(A)=
(-1)^u\binom{s}{u}
\left(\frac3{A+71}\right)^u
\frac{\displaystyle\prod_{i=0}^{u-1}(A+2b-2i)}
{\displaystyle\prod_{\substack{0\le i<u\\i\ne I_b}}
(4A+1+4b-2i)}.
\tag{5}
$$


Equation (4) groups **every actual term containing the resonant factor**. It is an exact finite identity, with the original upper boundary $s$.

For each fixed $u\ge U_b$, (5) is regular at $A_*$. Write


$$
R^*_{b,u}=R_{b,u}(A_*).
$$


Then


$$
R^*_{b,u}
=
(-1)^u\binom{s_*}{u}
\left(\frac{12}{527}\right)^u
\frac{\displaystyle\prod_{i=0}^{u-1}(A_*+2b-2i)}
{\displaystyle\prod_{\substack{0\le i<u\\i\ne I_b}}2(I_b-i)}.
\tag{6}
$$



The residue of any fixed truncation is therefore the **sum** of its $R^*_{b,u}$, not its first term.

---

## 4. A rigorous polar-residue series and a fixed truncation bound

Define


$$
\mathcal R_b=\sum_{u=U_b}^{\infty}R^*_{b,u}.
\tag{7}
$$



### Proposition

The series (7) converges in $\mathbb Q_3$. More precisely,


$$
\boxed{
v_3(R^*_{b,u})
\ge
u-v_3(I_b!)-v_3((u-U_b)!).
}
\tag{8}
$$



**Proof.** Since $s_*\in\mathbb Z_3$, the generalized binomial coefficient
$\binom{s_*}{u}$ belongs to $\mathbb Z_3$. Every numerator factor in (6) is also $3$-integral, while $v_3(12/527)=1$. Finally,


$$
\prod_{\substack{0\le i<u\\i\ne I_b}}2(I_b-i)
=
2^{u-1}I_b!(-1)^{u-U_b}(u-U_b)!.
$$


Taking valuations proves (8). Since


$$
v_3(v!)\le v/2,
$$


the lower bound tends to infinity. ∎

For all three values of $b$, this gives the particularly convenient fixed certificate


$$
\boxed{
\mathcal R_b\equiv
\sum_{u=U_b}^{280}R^*_{b,u}\pmod{3^{143}\mathbb Z_3}.
}
\tag{9}
$$


Indeed, for $u\ge281$, the weakest bound is the $b=2$ bound


$$
u-61-\frac{u-127}{2}=\frac u2+\frac52\ge143.
$$



Thus a calculation involving at most $158$ rational terms per case—not a Jacobi polynomial of astronomical degree—determines every possible residue valuation below $143$.

### Exact recurrence for the calculation

Start from (6) at $u=U_b$, and use


$$
\boxed{
\frac{R^*_{b,u+1}}{R^*_{b,u}}
=
-\frac{s_*-u}{u+1}\,
\frac{A_*+2b-2u}{2(I_b-u)}\,
\frac{12}{527},
\qquad u\ge U_b.
}
\tag{10}
$$


All denominators in (10) are nonzero rational numbers.

I have not executed this calculation here. In particular, I do **not** assert that


$$
v_3(\mathcal R_b)=133,\ 136,\ 134
$$


merely because those are the first-term valuations. Those equalities, or their replacements after cancellation, are precisely what the bounded grouped calculation must establish.

### Concrete follow-on lemma

The immediate finite obligation is:

> For each $b=0,1,2$, compute
> 

$$
> C_b=\sum_{u=U_b}^{280}R^*_{b,u}
>
$$


> and certify either $v_3(C_b)<143$, together with its first nonzero unit digit, or $C_b\equiv0\pmod{3^{143}}$.

In the first case, (9) proves unconditionally that


$$
\mathcal R_b\ne0,\qquad v_3(\mathcal R_b)=v_3(C_b).
$$


In the second case, a deeper fixed truncation is necessary. No nonzero-residue conclusion follows from a zero output at this precision.

---

## 5. Why the formal polar residue is not yet an original-domain value theorem

Even a nonzero result in (9) would not by itself prove


$$
v_3(T_b(A))=v_3(\mathcal R_b)-t
\tag{11}
$$


for every sufficiently close original index.

The exact quantity in (4) is


$$
\sum_{u=U_b}^{s(A)}R_{b,u}(A),
$$


whose upper boundary grows with $A$. Fixed-term continuity does not imply continuity of this moving finite sum.

The precise obstruction is visible in (2). For $i\ne I_b$,


$$
v_3\bigl(\epsilon+2(I_b-i)\bigr)=v_3(I_b-i)
$$


is guaranteed only when $v_3(I_b-i)<t$. At indices congruent to $I_b\pmod{3^t}$, additional deep denominator effects become possible. These indices eventually occur inside the actual finite range.

Turn27’s proved tail bound remains valid:


$$
v_3(E_{b,u})\ge1\qquad(u\ge2h).
$$


Consequently the corresponding tail of $\epsilon T_b(A)$ has valuation at least $t+1$. But the intermediate range


$$
281\le u<2h
$$


still requires uniform control. It cannot be replaced without proof by the tail estimate at the rational parameter $A_*$.

A sufficient original-domain continuation lemma is therefore


$$
\boxed{
\sum_{u=U_b}^{s(A)}R_{b,u}(A)
\equiv\mathcal R_b\pmod{3^{V_b+1}},
\qquad V_b=v_3(\mathcal R_b),
}
\tag{12}
$$


on an explicitly specified infinite family of admissible indices. Together with a suitable lower bound for the nonresonant sum in (4), (12) would yield a corrected value law. This is a separate mathematical obligation, not a consequence of the fixed residue computation.

---

## 6. Reachability in the original index domain

The congruence classes are genuinely reachable.

The element $4$ generates the subgroup $1+3\mathbb Z/3^t\mathbb Z$, of order $3^{t-1}$. Since $247\equiv1\pmod3$, the congruence


$$
4^{j+1}\equiv247\pmod{3^t}
$$


defines one class of $j$ modulo $3^{t-1}$. Requiring exact valuation $t$ excludes one of its three lifts modulo $3^t$, leaving two arithmetic progressions.

For $t\ge6$,


$$
4^j-1=\frac{243+\epsilon}{4}
$$


has valuation $5$. LTE therefore gives


$$
1+v_3(j)=5,\qquad v_3(j)=4.
$$


In particular $81\mid j$, exactly as required.

To check the real window, put $\alpha=\log_3 4$. It is irrational: a rational equality would imply $4^a=3^c$ for positive integers $a,c$. Along any fixed progression $j=j_0+Mq$, the fractional parts of $j\alpha$ are dense.

Choose a fixed open interval


$$
0<\delta_1<\delta_2<-\log_3(1-1/972).
$$


Infinitely many members of the progression satisfy


$$
j\alpha=N-\delta,\qquad \delta_1<\delta<\delta_2.
$$


For sufficiently large such $j$,


$$
H=3^N,\qquad
\frac{A}{H}=3^{-\delta}-3^{-N}\in(1-1/972,1).
$$


Moreover $4A+5\in(3H,9H)$, so the prescribed definition gives $h=N+1$. Hence


$$
0<H-A<H/972.
$$



This establishes compatibility without constructing any enormous $4^j$. It does not impose an upper bound on $h$, so it does not resolve the intermediate-range issue in §5.

---

## 7. Actual-matrix and primitive-error safeguards

Everything above is core-only. The original columns remain


$$
1,y,\ldots,y^m,\qquad 0\le a,b\le m.
$$


The actual functional remains


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\sum_{2v+1\le4n-3}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1}.
$$


Neither its factorial force nor its endpoint subtraction is removed.

On the resonant classes, $v_3(j)=4$, so the accepted polynomial approximation supplies only


$$
Q_n^{\rm loc}-Q_{\rm core}\in3^6\mathbb Z_3[y].
$$


Restoring $Q_n=\lambda_nQ_n^{\rm loc}$ retains the actual unit multiplier. Any transfer still requires the original monomial-coordinate inverse and endpoint losses; the resonance supplies no extra perturbation precision.

Finally, if


$$
\det H_{\rm complete}=\beta_0+\beta_1(e+\pi),
\quad
A_\ell=\ell^k\beta_0,\quad B_\ell=\ell^k\beta_1,
$$


then


$$
g_\ell=\gcd(|A_\ell|,|B_\ell|),\qquad
q=\frac{|B_\ell|}{g_\ell},
$$


and the whole error is


$$
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell^k}{g_\ell}
\det H_{\rm complete}.
$$


No core residue replaces the final gcd, the actual primitive denominator, or this whole evaluated error.

## Conclusion

**Proved here:** the exact first-resonance valuations (1), failure of the proposed coefficientwise inequalities on reachable original index classes, exact grouping of the shared denominator, and the convergent polar-residue series with the fixed certificate (9).

**Not proved:** nonvanishing of that grouped residue, its transfer to the moving-degree original polynomial, the terminal Wronskian valuation, or actual-denominator/error control.

**Next bounded calculation:** inputs $A_*=243/4$, $b=0,1,2$, and recurrence (10), over $U_b\le u\le280$. Its verifiable output is each grouped residue modulo $3^{143}$, with its valuation and first nonzero unit digit when present.

**Exact remaining bottleneck:** after this finite residue test, prove the original-domain uniform grouping estimate (12), including the intermediate range not covered by fixed-term continuity or the $u\ge2h$ tail theorem. Irrationality of $e+\pi$ remains unresolved.
