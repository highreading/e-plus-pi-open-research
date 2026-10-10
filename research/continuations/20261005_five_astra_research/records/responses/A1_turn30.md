> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1: Moving-degree Jacobi continuation—an audited residue and a shorter unresolved range

## 1. Result and scope

The supplied exact-arithmetic receipt, together with the tail inequality audited below, establishes


$$
v_3(\mathcal R_0)=133,\qquad
v_3(\mathcal R_1)=135,\qquad
v_3(\mathcal R_2)=134.
$$


These are valuations of the **grouped polar residues at $A_*=243/4$**, not of the original evaluated Jacobi polynomials.

The new result is a moving-degree exclusion lemma: all terms between $u=281$ and the **next possible denominator resonance**


$$
u=I_b+3^t+1
$$


are harmless at the required precision, without any upper bound on $h$. Combined with turn27’s long-tail estimate, this reduces continuation (12) exactly to a possibly empty interval


$$
I_b+3^t+1\le u\le \min(s,2h-1).
$$



I do **not** prove that the sum on this remaining interval vanishes on an infinite original-index family. Nor do I disprove continuation (12). Below I give an exact equivalent remaining obligation and a numerator-paired residue-count criterion sufficient to settle it.

The earlier archive and literature gate is retained at its recorded scope. No search or execution tools are available here, so I claim neither a fresh literature search nor an independent execution of the supplied rational-sum certificate. The arguments below are elementary valuation arguments; no global novelty claim is made.

## 2. Original domain and exact grouping

Retain


$$
A=4^j-1,\quad n=A+2,\quad
h=\lfloor\log_3(4n-3)\rfloor,\quad H=3^{h-1},
$$




$$
j>0,\qquad81\mid j,\qquad0<H-A<H/972,
$$


and


$$
m=(A+1)/2,\qquad s=m+b,\qquad b\in\{0,1,2\}.
$$


Put


$$
\epsilon=4A-243,\quad t=v_3(\epsilon),\quad
I_b=122+2b,\quad U_b=I_b+1,\quad r_0=(A+71)/3.
$$



With turn29’s exact terms,


$$
T_b(A):=r_0^{-s}p_s(r_0)
=N_b(A)+\epsilon^{-1}S_b(A),
$$


where


$$
N_b(A)=\sum_{u=0}^{I_b}E_{b,u}(A),\qquad
S_b(A)=\sum_{u=U_b}^{s}R_{b,u}(A).
$$


Here


$$
R_{b,u}(A)=
(-1)^u\binom{s}{u}
\left(\frac3{A+71}\right)^u
\frac{\prod_{i=0}^{u-1}(A+2b-2i)}
{\prod_{\substack{0\le i<u\\i\ne I_b}}
(\epsilon+2(I_b-i))}.
$$


The upper boundary is the actual integer $s$; it is never replaced by an infinite boundary at the actual parameter.

## 3. Audit of the fixed polar residue

At $A_*=243/4$, write $R^*_{b,u}=R_{b,u}(A_*)$. Since


$$
s_*=(247+8b)/8\in\mathbb Z_3,
$$


the generalized binomial coefficient $\binom{s_*}{u}$ is $3$-integral. This follows, for example, by approximating $s_*$ by nonnegative integers in $\mathbb Z_3$, with $u$ fixed.

Every numerator factor is also $3$-integral, and


$$
v_3(12/527)=1.
$$


The omitted-denominator product is exactly


$$
\prod_{\substack{0\le i<u\\i\ne I_b}}2(I_b-i)
=
2^{u-1}I_b!(-1)^{u-U_b}(u-U_b)!.
$$


Consequently


$$
v_3(R^*_{b,u})
\ge u-v_3(I_b!)-v_3((u-U_b)!).
\tag{1}
$$


This proves convergence of $\mathcal R_b=\sum_{u\ge U_b}R^*_{b,u}$.

Using $v_3(q!)\le q/2$, the three bounds are


$$
\frac u2+\frac72,\qquad
\frac u2+\frac72,\qquad
\frac u2+\frac52.
$$


Thus every term with $u\ge281$ belongs to $3^{143}\mathbb Z_3$. The fixed certificate is valid:


$$
\mathcal R_b\equiv C_b:=\sum_{u=U_b}^{280}R^*_{b,u}
\pmod{3^{143}}.
\tag{2}
$$



The supplied receipt therefore gives


$$
\begin{array}{c|ccc}
b&0&1&2\\ \hline
V_b:=v_3(\mathcal R_b)&133&135&134\\
3^{-V_b}\mathcal R_b\pmod{27}&2&22&16
\end{array}
\tag{3}
$$


at the receipt’s exact computational scope. In particular, the $b=1$ depth is $135$, not the first term’s depth $136$.

## 4. New lemma: exclusion up to the second resonance

### Proposition

Suppose $t\ge7$. For every actual index and


$$
U_b\le u\le\min(s,I_b+3^t),
$$


one has


$$
v_3(R_{b,u}(A))
\ge u-v_3(I_b!)-v_3((u-U_b)!).
\tag{4}
$$


In particular,


$$
281\le u\le\min(s,I_b+3^t)
\quad\Longrightarrow\quad
R_{b,u}(A)\in3^{143}\mathbb Z_3.
\tag{5}
$$



**Proof.** For $0\le i<u$, $i\ne I_b$, the stated range gives


$$
0<|I_b-i|<3^t,
$$


because $I_b<3^t$. Hence


$$
v_3(I_b-i)<t
$$


and therefore


$$
v_3\bigl(\epsilon+2(I_b-i)\bigr)=v_3(I_b-i).
$$


The total denominator valuation is exactly


$$
v_3(I_b!)+v_3((u-U_b)!).
$$



At an actual index, $\binom{s}{u}$ is an integer and all numerator factors are integers. Also $v_3(A+71)=0$, so the evaluation factor contributes $u$. Dropping only nonnegative numerator valuations proves (4). Equation (5) follows from the audited bound in §3. ∎

This is not fixed-term continuity: its range grows exponentially with the resonance depth $t$, and it holds for every $h$. It does not, however, exclude later resonances when $h$ is sufficiently large.

## 5. Explicit fixed-part transfer and the nonresonant sum

For definiteness, take


$$
t\ge150.
\tag{6}
$$


This is deliberately conservative, avoiding a new coefficient scan.

For $u\le280$, all nonzero numerator factors at $A_*$, after multiplication by the unit denominator $4$ or $8$, have absolute value less than $2187=3^7$. Their valuations are therefore at most $6$. The omitted denominator factors have still smaller bounds.

Replacing $A_*$ by $A=A_*+\epsilon/4$ changes each such factor relatively by an element of $3^{t-6}\mathbb Z_3$. The same holds for the evaluation factor. Finite products and inverses of these relative units give


$$
R_{b,u}(A)=R^*_{b,u}\bigl(1+3^{t-6}z_{b,u}\bigr),
\qquad z_{b,u}\in\mathbb Z_3.
$$


The lower bound (1) is nonnegative throughout this fixed range. Hence


$$
\sum_{u=U_b}^{280}R_{b,u}(A)
\equiv C_b\equiv\mathcal R_b\pmod{3^{143}}.
\tag{7}
$$



The nonresonant sum must also be retained. For $1\le u\le I_b$, every denominator has valuation at most $5$. Counting one residue class at each depth gives


$$
\sum_{i=0}^{u-1}v_3(\epsilon+2(I_b-i))
\le v_3((u-1)!)+5.
$$


Thus


$$
v_3(E_{b,u})\ge u-v_3((u-1)!)-5\ge-5,
$$


and, including $E_{b,0}=1$,


$$
v_3(N_b(A))\ge-5,\qquad
v_3(\epsilon N_b(A))\ge t-5\ge145.
\tag{8}
$$



## 6. Exact reduced continuation obligation

Turn27’s tail theorem applies with the original cutoff and gives


$$
v_3(E_{b,u})\ge1\qquad(2h\le u\le s).
$$


Since $R_{b,u}=\epsilon E_{b,u}$,


$$
R_{b,u}\in3^{t+1}\mathbb Z_3
\qquad(2h\le u\le s).
\tag{9}
$$



Define the remaining finite block


$$
B_b(A)=
\sum_{u=I_b+3^t+1}^{\min(s,2h-1)}R_{b,u}(A),
\tag{10}
$$


with an empty sum interpreted as zero. Equations (5), (7), and (9) prove


$$
S_b(A)-\mathcal R_b\equiv B_b(A)\pmod{3^{V_b+1}}.
\tag{11}
$$



Therefore, on the stated domain with $t\ge150$, turn29’s continuation (12) is **equivalent** to


$$
\boxed{B_b(A)\in3^{V_b+1}\mathbb Z_3.}
\tag{12}
$$



If (12) holds, (8) yields the actual core value law


$$
\boxed{v_3(T_b(A))=V_b-t,\qquad
v_3(p_{m+b}(r_0))=-(m+b)+V_b-t.}
\tag{13}
$$


This is a conditional deduction, not an established infinite-family theorem.

A weaker condition sufficient for (13), without requiring preservation of the residue digit, is


$$
v_3\bigl(\mathcal R_b+B_b(A)\bigr)=V_b.
\tag{14}
$$


Thus preservation of the particular leading residue is stronger than necessary for the valuation objective.

## 7. Pairing all later denominator resonances with actual numerators

The remaining block admits an exact numerator-paired count formulation.

For $a\ge1$, let


$$
D_a(u)=\#\{0\le i<u:2i\equiv4A+1+4b\pmod{3^a}\},
$$




$$
N_a(u)=\#\{0\le i<u:2i\equiv A+2b\pmod{3^a}\},
$$


and


$$
F_a(u)=\#\{0\le i<u:i\equiv s\pmod{3^a}\}.
$$


Then


$$
v_3\binom{s}{u}
=\sum_{a\ge1}\left(F_a(u)-\left\lfloor u/3^a\right\rfloor\right),
$$


and exactly


$$
v_3(R_{b,u})
=u+t+\sum_{a\ge1}
\left(
N_a(u)+F_a(u)-D_a(u)-\left\lfloor u/3^a\right\rfloor
\right).
\tag{15}
$$


All counts use the **actual** $A=4^j-1$ and the actual interval $0\le i<u$. The added $t$ removes precisely the denominator at $i=I_b$.

For a useful sufficient bound, put $L=\lfloor\log_3u\rfloor$ and


$$
\mathcal D_b(u)=
\sum_{a>L}\max\{0,D_a(u)-N_a(u)\}.
$$


For $a\le L$, the two interval counts differ by at most one. For $a>L$, each is zero or one. Since the total binomial valuation is nonnegative, (15) implies


$$
\boxed{
v_3(R_{b,u})\ge u+t-L-\mathcal D_b(u).
}
\tag{16}
$$



Consequently the concrete follow-on lemma


$$
\boxed{
\mathcal D_b(u)\le
u+t-\lfloor\log_3u\rfloor-V_b-1
}
\tag{17}
$$


throughout the interval (10) would prove (12) coefficientwise. Grouped cancellation may prove (12) even where (17) fails.

The unresolved issue is now specific: a denominator residue can occur before its paired numerator residue at several successive high depths. Neither the power-of-four congruence nor fixed-$t$ density presently bounds the total unmatched depth $\mathcal D_b(u)$ sufficiently.

## 8. Reachability does not supply a size bound

For any fixed $t\ge150$, exact valuation


$$
v_3(4^{j+1}-247)=t
$$


defines two arithmetic progressions modulo $3^t$. LTE gives $v_3(j)=4$. Irrational rotation by $\log_3 4$, restricted to either progression, supplies infinitely many indices in the prescribed real window.

This proves that the family under discussion is genuinely an infinite original-index family. It does **not** prove (12) on that family.

In particular, the condition


$$
2h-1\le I_b+3^t
$$


would make (10) empty, but at fixed $t$ it bounds $h$, hence bounds $j$. It cannot establish an infinite family. Allowing $t$ to vary would require a separate simultaneous size-and-window argument, which is not supplied by density.

## 9. Terminal Wronskian and actual-force limit

The exact terminal identity remains


$$
\mathscr K_{\rm core}
=
\left.
\frac{F_{m+1}'F_m-F_m'F_{m+1}}
{-3c\,a_mh_m(t-r_0)^2}
\right|_{t=-1},
$$


where


$$
F_s=p_{s+1}-a_sp_s,\qquad
a_s=\frac{p_{s+1}(r_0)}{p_s(r_0)},\qquad
c=(-1)^A3^h/2.
$$


Even (13) would not evaluate cancellation in this Wronskian.

The original coordinates remain $1,y,\ldots,y^m$, with matrix indices $0\le a,b\le m$, and the complete functional is


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+3^h\sum_{2v+1\le4n-3}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1}.
$$


On these resonant classes the accepted actual force law supplies only


$$
Q_n^{\rm loc}=Q_{\rm core}+3^6R.
$$


Thus the complete perturbation is


$$
\Delta_{ab}=
-\frac{3^h}{4}\mathfrak f(Q_n^{\rm loc}y^{a+b})
+3^{h+6}\sum_{2v+1\le4n-3}
\frac{[y^v](Ry^{a+b}-(-1)^{a+b}R(-1))/(y+1)}
{2v+1}.
$$


In particular $\Delta\in3^6M_k(\mathbb Z_3)$. The actual unit multiplier $\lambda_n$ must be restored.

No formal pole increases this precision. The original-coordinate inverse losses and endpoint contraction still require the transfer conditions from turn21; the unresolved residual block divided by $3^6$ is not determined by this congruence alone.

## 10. Primitive arithmetic and conclusion

For the complete determinant retain


$$
\det H_{\rm complete}=\beta_0+\beta_1(e+\pi),
$$




$$
A_\ell=\ell^k\beta_0,\quad B_\ell=\ell^k\beta_1,\quad
g_\ell=\gcd(|A_\ell|,|B_\ell|).
$$


When $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
$$


and the whole error is exactly


$$
q(e+\pi)-p=
\frac{\operatorname{sgn}(B_\ell)\ell^k}{g_\ell}
\det H_{\rm complete}.
$$


Neither a polar residue nor a core valuation substitutes for this final gcd, primitive multiplier, actual denominator, or whole evaluated error.

**New proved result:** the fixed residue tail certificate passes, and the actual moving-degree terms from $281$ through $I_b+3^t$ are uniformly excluded. Continuation is reduced exactly to (12), with the numerator-paired criterion (17) as a concrete sufficient follow-on lemma.

**Remaining bottleneck:** control the grouped later-resonance block on an infinite original-index family, then evaluate the terminal Wronskian and respect the actual $3^6$ perturbation limit. Actual denominator and whole-error decay remain further obligations.

**Bounded computation:** no repeat fixed-residue calculation or coefficient scan is needed. The supplied receipt already has the required fixed inputs and outputs. The outstanding assertion is uniform in the actual index; further finite samples cannot establish it.

**Proof status:** the main moving-degree continuation remains unresolved. No unconditional proof or disproof of irrationality of $e+\pi$ follows.
