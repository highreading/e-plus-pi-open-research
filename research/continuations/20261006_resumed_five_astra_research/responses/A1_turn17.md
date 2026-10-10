> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1 turn17 — The stronger killing cylinder, its first divided image, and the remaining original-family obstruction

## Executive conclusion

The stronger cylinder theorem is valid. In fact, its divisibility does not require the leading $25$ ones.

Let


$$
t_*=1194953,\qquad P_*=3^{13}=1594323.
$$


Then, for every positive integer $m$ satisfying


$$
m\equiv t_*\pmod{P_*},
$$


both complete Jacobi polynomials in the established normalization satisfy


$$
\boxed{
J_m^{[\,2m-1\,]}(y),\ J_{m-1}^{[\,2m-1\,]}(y)
\in 27\mathbb Z_3[y].
}
\tag{E.1}
$$


Consequently,


$$
\boxed{X_m\equiv Y_m\equiv0\pmod{27}.}
\tag{E.2}
$$



This is not an extrapolation from the forty tested words. The proof is a termwise factorial-valuation argument: the fixed tail forces one factor of $3$ at each of the three distinct levels


$$
3^9,\qquad 3^{11},\qquad 3^{13}
$$


in every Bernstein summand of each polynomial.

There is also an explicit answer at the next precision. For


$$
m=(1^{25}H20202\,01011112)_3,
$$


a small signed digit observable $\psi(H)\in\mathbb F_3$, defined and proved below, gives


$$
\boxed{
\left(\frac{X_m}{27},\frac{Y_m}{27}\right)
\equiv\bigl(\psi(H),-\psi(H)\bigr)\pmod3.
}
\tag{E.3}
$$


Its image is exactly


$$
\boxed{\{(0,0),(1,2),(2,1)\}.}
\tag{E.4}
$$



The vanishing criterion is particularly simple. Here $H$ is written most significant digit first:


$$
\boxed{
\psi(H)\ne0
\iff
H\in\{0,1\}^{*}\{1,2\}^{*}.
}
\tag{E.5}
$$


Equivalently, $\psi(H)\ne0$ precisely when no digit $2$ of $H$ lies to the left of a digit $0$.

Thus:

* if $H$ satisfies (E.5), then $c_m=3$, the primitive endpoint direction is
  

$$
\boxed{[\bar X_m:\bar Y_m]=[1:-1]\quad\text{over }\mathbb F_3,}
$$


  and the two full Jacobi polynomial contents are both exactly $3$;
* otherwise $c_m\ge4$. This does **not** say that either full polynomial content is at least $4$.

The instantiated original progression is retained without recomputation:


$$
\boxed{j\equiv84645\pmod{531441}.}
$$


Every sufficiently large exact-window index in this progression has $c_m\ge3$. Its density among positive $j$ is


$$
\boxed{
\frac1{531441}\log_3
\frac{1-\frac1{2C_{16}}}{1-\frac1{C_{16}}}>0.
}
\tag{E.6}
$$



What is not established is an infinite original subfamily whose entire intervening word $H$ satisfies (E.5). A fixed trailing congruence does not ensure that global digit-language condition. The new result therefore determines the next divided image and the exact direction whenever it is primitive, but does not certify an infinite original exact-$c_m=3$ family.

The actual-force transfer, all-prime primitive denominator, and whole same-index error remain separate obligations. Irrationality of $e+\pi$ remains unresolved.

---

## 1. Source audit and scope

I retain


$$
j>0,\qquad j\equiv81\pmod{243},\qquad
m=2^{2j-1},\qquad A=2m-1,
$$


and


$$
H_{\mathrm{win}}=3^{h-1},\qquad D=H_{\mathrm{win}}-A,
$$


with the original exact window


$$
\frac1{2C_{16}}<\frac D{H_{\mathrm{win}}}<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
\tag{1.1}
$$



The endpoint notation remains


$$
X_m=J_m^{[\,2m-1\,]}(-1),\qquad
Y_m=J_{m-1}^{[\,2m-1\,]}(-1).
\tag{1.2}
$$


Both degrees use the same parameter $A=2m-1$. The attached normalization note and turn16 give exact characteristic-zero identities, not merely congruences or projective identifications.

### 1.1 Accepted finite receipts

The modulo-$9$ receipt establishes its stated finite checks:

* $153$ degree-basis cases;
* $80$ characteristic-zero endpoint comparisons at $m=141,\ldots,180$;
* six paid injections;
* the recorded suffix carries and leading-ones functional;
* $364$ stated middle words.

The modulo-$27$ receipt establishes:

* $1431$ degree-basis cases;
* $80$ characteristic-zero endpoint comparisons at $m=181,\ldots,220$;
* forty words $H20202$, $|H|\le3$, with both endpoints zero modulo $27$;
* the numerical original congruence representative $j_*=84645$.

I accept those finite outputs at that scope. None of them is rerun or used as a substitute for the universal proofs below.

The supplied classical prime-power coefficient-extraction machinery is reused as background. The target-specific claims requiring proof are the displayed module, the forced valuation levels, and the actual divided observable.

---

## 2. Audit of the paid modulo-$27$ module

Write


$$
a=1+u,\qquad b=1-u,\qquad Q=1-u^2,
\qquad x(u)=\frac{ua^3}{b},
\qquad \sigma^2=Q,\quad \sigma(0)=1.
$$



Define


$$
\mathcal E_n^{(27)}(N)
=
\operatorname{res}_{u=0}
x(u)^{-n}\sigma(u)\frac{N(u)}{Q(u)^{26}}\frac{du}{u}.
\tag{2.1}
$$



### 2.1 Square-root Frobenius identity

For $F\in\mathbb Z_3[[u]]$,


$$
F(u)^3\equiv F(u^3)\pmod3.
$$


Raising this congruence to the ninth power yields


$$
F(u)^{27}\equiv F(u^3)^9\pmod{27}.
$$


For $F=\sigma$, the exact square relation gives


$$
\sigma(u)Q(u)^{13}
\equiv
\sigma(u^3)Q(u^3)^4\pmod{27}.
$$


Since $Q(0)=1$,


$$
\boxed{
\sigma(u)\equiv
\sigma(u^3)\frac{Q(u^3)^4}{Q(u)^{13}}
\pmod{27}.
}
\tag{2.2}
$$



### 2.2 Index-ratio correction

Put


$$
t=\frac{u}{b^2},\qquad s=\frac{u}{a^2}.
$$


The exact identities


$$
1-u^3=b^3+3ub,\qquad
1+u^3=a^3-3ua
$$


give


$$
R:=\frac{x(u^3)}{x(u)^3}
=
\frac{(1-3s)^3}{1+3t}.
\tag{2.3}
$$


Therefore


$$
R\equiv1-3t+9t^2-9s\pmod{27}.
$$


For every nonnegative integer $q$,


$$
\boxed{
R^q\equiv
1-3qt+9\binom{q+1}{2}t^2-9qs
\pmod{27}.
}
\tag{2.4}
$$


The coefficient $\binom{q+1}{2}$ is an integer. The expression depends only on $q\bmod9$.

### 2.3 The four-term transition

For $n=3q+r$, $0\le r\le2$, let


$$
\begin{aligned}
\mathcal U_{r,q}(N)(v)=Q(v)^{12}\Lambda_0\Bigl(
&u^{-r}Na^{15-3r}b^{15+r}\\
&-3q\,u^{1-r}Na^{15-3r}b^{13+r}\\
&+9\binom{q+1}{2}u^{2-r}Na^{15-3r}b^{11+r}\\
&-9q\,u^{1-r}Na^{13-3r}b^{15+r}
\Bigr).
\end{aligned}
\tag{2.5}
$$



Then


$$
\boxed{
\mathcal E_{3q+r}^{(27)}(N)
\equiv
\mathcal E_q^{(27)}\bigl(\mathcal U_{r,q}(N)\bigr)
\pmod{27}.
}
\tag{2.6}
$$



**Proof.** Insert (2.2) and (2.4) into (2.1). The common denominator can be padded to $Q(u)^{54}$, producing exactly the four Laurent numerators in (2.5). Moreover,


$$
Q(u)^{54}\equiv Q(u^3)^{18}\pmod{27}.
$$


After sectioning, the numerator $Q(u^3)^4$ leaves denominator $Q(v)^{14}$. Multiplication of the numerator by $Q(v)^{12}$ restores denominator $Q(v)^{26}$. The formal residue-section identity completes the reduction. ∎

If $\deg N\le52$, the largest exponent in the first Laurent numerator is at most $82-3r$; the other three have smaller bounds. The smallest exponent is at least $-2$, so no negative multiple of $3$ is sectioned. Consequently


$$
\deg\mathcal U_{r,q}(N)
\le24+\left\lfloor\frac{82-3r}{3}\right\rfloor
=51-r.
\tag{2.7}
$$


Thus the $53$-coordinate space is invariant.

The initial numerators are exactly


$$
\boxed{
N_X=b^{25}a^{26},\quad
N_Y=ub^{24}a^{27},\quad
N_W=b^{26}a^{25},\quad
N_S=b^{26}a^{26}.
}
\tag{2.8}
$$


These follow from the actual differentials, not from a new branch choice.

This proves the general module formula independently of the eighty endpoint samples. The required lookahead is $q\bmod9$, hence the next two ternary digits, with zeros beyond the final digit.

---

## 3. A termwise valuation obstruction to a unit Bernstein coefficient

The stronger cylinder can be proved more directly than by multiplying $53\times53$ matrices.

For an odd power $P=3^h$, define


$$
\alpha_P(s)=\left(s+\frac{P-1}{2}\right)\bmod P,
$$


with residue in $\{0,\ldots,P-1\}$.

For $0\le r\le s$, count factors divisible by $P$ in


$$
\binom{s-\tfrac12}{r}
=
\frac{\prod_{i=0}^{r-1}(2s-1-2i)}{2^r r!}.
$$


The numerator factors divisible by $P$ occur at


$$
i\equiv\alpha_P(s)\pmod P.
$$


Hence the contribution of level $P$ to the valuation of this binomial coefficient is


$$
\boxed{
\mathbf 1_{\{r\bmod P>\alpha_P(s)\}}.
}
\tag{3.1}
$$



For an ordinary binomial coefficient,


$$
v_3\binom{n}{k}
=
\sum_{h\ge1}
\mathbf 1_{\{k\bmod3^h>n\bmod3^h\}}.
\tag{3.2}
$$



Thus each level contributes a nonnegative integer to


$$
v_3\left(
\binom{n}{k}\binom{s-\tfrac12}{s-k}
\right).
\tag{3.3}
$$


A factor forced at one level cannot be canceled by a negative contribution at another level.

### Lemma 3.1 — A simultaneous forcing interval

Let $P=3^h$, and suppose


$$
\boxed{
\frac{2P}{3}+1
\le t:=m\bmod P
\le\frac{5P-3}{6}.
}
\tag{3.4}
$$


Then level $P$ contributes at least one to the valuation of every Bernstein coefficient of each of


$$
J_m^{[\,2m-1\,]},\qquad J_{m-1}^{[\,2m-1\,]}.
$$



**Proof.** Treat the two cases as


$$
s=m,\quad n=3s-1,
$$


and


$$
s=m-1,\quad n=3s+1.
$$



Write $r=s-k$, $w=r\bmod P$, and $t_s=s\bmod P$. A zero contribution from both binomial factors would require


$$
w\le \alpha_P(s),
\qquad
(t_s-w\bmod P)\le n\bmod P.
\tag{3.5}
$$



For the first polynomial, $t_s=t$, and under (3.4),


$$
\alpha_P(s)=t-\frac{P+1}{2},\qquad
n\bmod P=3t-1-2P<t.
$$


Because $w\le\alpha_P(s)<t$, there is no wrap in $t-w$. Conditions (3.5) therefore require


$$
2P+1-2t\le w\le t-\frac{P+1}{2}.
\tag{3.6}
$$


But


$$
6t<5P+3
$$


under (3.4), so this interval is empty.

For the adjacent polynomial, $t_s=t-1$. The required lower bound on $w$ is again $2P+1-2t$, while the upper bound is


$$
t-\frac{P+3}{2},
$$


which is smaller still. Thus its interval is also empty. ∎

This lemma concerns every coefficient in the actual Bernstein sum. It is not an endpoint-cancellation argument.

---

## 4. The universal modulo-$27$ killing cylinder

The fixed tail gives the following three residues:


$$
\begin{array}{c|r|r|r}
P&m\bmod P&2P/3+1&(5P-3)/6\\ \hline
3^9=19683&13973&13123&16402\\
3^{11}=177147&132071&118099&147622\\
3^{13}=1594323&1194953&1062883&1328602.
\end{array}
\tag{4.1}
$$


All three residues lie in the forcing interval of Lemma 3.1.

### Theorem 4.1 — Stronger fixed-tail theorem

For every positive integer $m$ satisfying


$$
m\equiv1194953\pmod{1594323},
$$


one has


$$
\boxed{
J_m^{[\,2m-1\,]},\ J_{m-1}^{[\,2m-1\,]}
\in27\mathbb Z_3[y].
}
\tag{4.2}
$$


In particular,


$$
\boxed{X_m\equiv Y_m\equiv0\pmod{27}.}
\tag{4.3}
$$



**Proof.** Each Bernstein coefficient of either polynomial receives at least one valuation contribution at each of the distinct levels $3^9,3^{11},3^{13}$. All remaining level contributions are nonnegative. Every Bernstein coefficient is therefore divisible by $27$.

The basis polynomials $y^k(y-1)^{s-k}$ have integral coefficients, so the entire polynomials belong to $27\mathbb Z_3[y]$. Evaluation at $-1$ proves (4.3). ∎

### Scope of the theorem

This proves the requested assertion for every word


$$
m=(1^{25}H20202\,01011112)_3,
$$


with arbitrary finite $H$.

It actually proves more:

* the leading $25$ ones are unnecessary for divisibility;
* neither inherited layer is set to zero;
* there is no favorable-carry hypothesis;
* no global endpoint continuity in $m\in\mathbb Z_3$ is asserted;
* the conclusion is obtained directly for the complete characteristic-zero polynomials.

The result is compatible with turn16’s earlier warning about polynomial content. A lower bound for full content is now proved for this particular cylinder. Equality between endpoint content and full polynomial content still requires further information.

---

## 5. Paying for the next divided image

Modulo $27$ cannot determine $(X_m/27,Y_m/27)\bmod3$. The following argument works at the required modulo-$81$ precision by retaining exactly those characteristic-zero summands having valuation $3$.

### 5.1 Exact factorial form of an endpoint summand

For


$$
n=3s+\varepsilon,\qquad \varepsilon\in\{-1,1\},
$$


the signed summand in $J_s(-1)$, with $r=s-k$, is


$$
(-1)^s
\binom{n}{k}\binom{s-\tfrac12}{s-k}2^{s-k}
=
(-1)^s
\frac{n!(2s)!}
{(n-k)!(2k)!s!(s-k)!\,2^{s-k}}.
\tag{5.1}
$$



Let $d_2(N)$ denote the number of ternary digits equal to $2$ in $N$. For the unit part of a factorial,


$$
\boxed{
3^{-v_3(N!)}N!
\equiv(-1)^{v_3(N!)+d_2(N)}\pmod3.
}
\tag{5.2}
$$


This follows by grouping the nonmultiples of $3$ into complete blocks and recursively applying the same identity to $\lfloor N/3\rfloor!$.

If the valuation of (5.1) is $e$, its unit residue is therefore


$$
\boxed{
(-1)^{e+k+d_2(n)+d_2(2s)-d_2(n-k)-d_2(2k)-d_2(s)-d_2(s-k)}.
}
\tag{5.3}
$$


The sign $(-1)^k$ includes both the evaluation sign and $2^{-(s-k)}$. No sign from the adjacent polynomial is omitted.

Because Theorem 4.1 proves that every summand has valuation at least $3$, only summands with valuation exactly $3$ contribute to the endpoint divided by $27$, modulo $3$. There is no lower-valuation cancellation whose carry would need to be reconstructed.

### 5.2 Which valuation patterns can contribute?

For a contributing summand, the valuation contributions must be:

* exactly one at levels $3^9,3^{11},3^{13}$;
* zero at every other level.

This produces a small digit transfer rather than a large coefficient sum.

For clarity, the transfer can be derived by keeping:

1. the addition carry in $k+(s-k)=s$;
2. the borrow in $n-k$;
3. the borrow in the generalized-binomial comparison (3.1);
4. the carry in $2k$.

Each local weight is given by (5.3), digit by digit. Thus the following finite transfer tables are algebraic identities for all digits, not empirical samples.

---

## 6. Exact suffix reduction for the valuation-three terms

The first eight low-to-high digits of $m$ are


$$
2,1,1,1,1,0,1,0.
$$



At these eight levels a contributing summand must have zero valuation contribution.

### 6.1 First eight digits

For $X_m$, the permissible low residues of $r=s-k$ are exactly


$$
r\bmod3^8=729,\qquad 486.
$$


Both finish with zero addition carry and zero doubling carry for $k$, and each has digit weight $-1$. Their aggregate weight is


$$
-1-1=1\quad\text{in }\mathbb F_3.
\tag{6.1}
$$



For $Y_m$, the first five digits independently allow $k_i=0$ or $1$, with $r_i=1-k_i$. Each two-choice digit has aggregate weight $-2=1$. The remaining three suffix digits have combined weight $-1$. Thus the aggregate is


$$
-1.
\tag{6.2}
$$



After the eight digits, all retained carry data are identical for the two endpoints. Their aggregate weights are opposite:


$$
\boxed{X:\ 1,\qquad Y:\ -1.}
\tag{6.3}
$$



This is where the actual two endpoint initial conditions enter the next-layer proof.

### 6.2 The five digits $2,0,2,0,2$

At each of the three forced $2$-positions, exactly one of the two binomial comparisons must borrow. At the intervening $0$-positions both outgoing borrows must vanish.

For example, at the first such $2$, the only admissible digit choices are


$$
(k_i,r_i)=(2,0),\qquad(0,2),
$$


with digit weights $-1,+1$, respectively. The pair $(1,1)$ creates two valuation contributions and is excluded from the valuation-three quotient.

At the following $0$, the two paths returning to zero addition carry have total weight $2=-1$, while the paths returning with addition carry one cancel. The same two-digit calculation applies to the next $2,0$.

After all five digits, and after including the global factor


$$
(-1)^e=(-1)^3,
$$


the $X$-weights of the two surviving borrow states are


$$
+1,\qquad-1.
\tag{6.4}
$$


The $Y$-weights are their negatives.

The first following digit sends this two-state combination to exactly the same observable state as the normal state denoted $\mathsf E(1)$ below. This holds for each possible following digit $0,1,2$, including the first leading $1$ when $H$ is empty.

This gives a universal reduction of the actual two inherited layers. They have not been replaced by a bare injection.

---

## 7. The next divided observable

The quotient can now be evaluated by a signed automaton with five live state types and one zero state.

A state is a type $\mathsf A,\mathsf B,\mathsf C,\mathsf D,\mathsf E$ together with an amplitude $v\in\mathbb F_3$. A displayed minus sign negates that amplitude. All zero amplitudes and the state $\bot$ represent zero.

Start in


$$
\boxed{\mathsf E(1).}
\tag{7.1}
$$



Read $H$ **least significant digit first**, hence from right to left in its displayed ternary word.

The transitions and the terminal functional, which includes all twenty-five leading ones, are


$$
\begin{array}{c|ccc|c}
\text{state}&0&1&2&\text{terminal value}\\ \hline
\mathsf A(v)&\mathsf A(v)&\mathsf C(-v)&\bot&-v\\
\mathsf B(v)&\mathsf A(v)&\mathsf C(v)&\bot&v\\
\mathsf C(v)&\mathsf A(v)&\mathsf C(v)&\bot&v\\
\mathsf D(v)&\mathsf B(v)&\mathsf D(-v)&\mathsf E(-v)&-v\\
\mathsf E(v)&\mathsf A(v)&\mathsf D(v)&\mathsf E(-v)&v\\
\bot&\bot&\bot&\bot&0.
\end{array}
\tag{7.2}
$$


Define $\psi(H)$ to be the terminal value.

The states $\mathsf B,\mathsf C$ have identical future observables and could be merged. They are retained separately here because they arise from different carry configurations in the derivation.

### 7.1 Verification of the transfer and leading functional

Here is an uncompressed form that makes (7.2) checkable.

Let $p$ be the preceding, less significant digit of $s$, and $z$ the carry in $2s$. After the first higher digit has cleared the two exceptional borrows, the possible environments are


$$
(p,z)=(0,0),(1,0),(1,1),(2,1).
$$


For $z=0$, keep amplitudes $(v,w)$ for addition carry $0,1$; for $z=1$, only addition carry zero is possible.

The exact transfers obtained from (5.3) are


$$
\begin{array}{c|ccc}
\text{environment}&0&1&2\\ \hline
(0,0):(v,w)&(0,0):(v,0)&(1,0):(-v-w,0)&(2,1):0\\
(1,0):(v,w)&(0,0):(v,-w)&(1,0):(v-w,-w)&(2,1):w\\
(1,1):v&(0,0):(v,v)&(1,1):-v&(2,1):-v\\
(2,1):v&(0,0):(v,0)&(1,1):v&(2,1):-v.
\end{array}
\tag{7.3}
$$



The leading-$25$-ones functionals are


$$
\begin{array}{c|c}
(0,0):(v,w)&-v-w\\
(1,0):(v,w)&v-w\\
(1,1):v&-v\\
(2,1):v&v.
\end{array}
\tag{7.4}
$$



For example, in environment $(1,0)$, a digit $1$ acts by


$$
(v,w)\longmapsto(v-w,-w).
$$


This is an involution, so twenty-five iterations leave first coordinate $v-w$. In environment $(1,1)$, each $1$ negates the amplitude. The other two rows reduce to these cases after the first leading digit.

Beyond the highest digit, the zero-addition-carry term has terminal weight one. A nonzero addition carry cannot terminate in $k+(s-k)=s$, so its contribution is zero. Thus the actual terminal return in this digit evaluation is retained.

The reachable configurations in (7.3) are exactly those represented in (7.2):


$$
\begin{aligned}
\mathsf A(v)&=(0,0):(v,0),&
\mathsf B(v)&=(0,0):(v,v),\\
\mathsf C(v)&=(1,0):(v,0),&
\mathsf D(v)&=(1,1):v,\\
\mathsf E(v)&=(2,1):v.
\end{aligned}
$$


This proves the signed observable table.

### Theorem 7.1 — First divided image of the killing cylinder

For every finite ternary word $H$,


$$
m=(1^{25}H20202\,01011112)_3
$$


satisfies


$$
\boxed{
\left(\frac{X_m}{27},\frac{Y_m}{27}\right)
\equiv\bigl(\psi(H),-\psi(H)\bigr)\pmod3,
}
\tag{7.5}
$$


where $\psi$ is defined by (7.1)–(7.2).

**Proof.** Theorem 4.1 pays the division by $27$ termwise. Equations (5.1)–(5.3) give the exact residue of every valuation-three summand. Sections 6 and 7 sum precisely those summands, retaining all addition, subtraction and doubling carries. The initial aggregates for the two endpoints are opposite, and all subsequent transfers are linear. Finally, (7.4) evaluates the complete leading block and the terminal coefficient extraction. ∎

### Corollary 7.2 — Exact zero criterion and image

One has


$$
\boxed{
\psi(H)\ne0
\iff H\in\{0,1\}^{*}\{1,2\}^{*}.
}
\tag{7.6}
$$



**Proof.** Before the first low-to-high $0$, the live state is $\mathsf D$ or $\mathsf E$; digits $1,2$ preserve a nonzero amplitude. The first $0$ enters $\mathsf A$ or $\mathsf B$. Thereafter digits $0,1$ keep the state among $\mathsf A,\mathsf B,\mathsf C$, while any $2$ kills it.

All surviving amplitudes are multiplied only by $1$ or $-1$, and every live terminal value is nonzero. Hence a zero occurs exactly when a $2$ is processed after a $0$, namely when the displayed high-to-low word has a $2$ to the left of a $0$. ∎

In particular,


$$
\psi(\varnothing)=1,\qquad
\psi(0)=-1,\qquad
\psi(20)=0.
\tag{7.7}
$$


Thus the image in (E.4) is exact, not just an upper bound.

These identities predict the new modulo-$81$ values


$$
\begin{array}{c|c}
H&(X_m,Y_m)\pmod{81}\\ \hline
\varnothing&(27,54)\\
0&(54,27)\\
20&(0,0).
\end{array}
\tag{7.8}
$$


They are consequences of the symbolic proof; no unreported numerical run is being claimed.

---

## 8. Primitive direction, full content, and observation loss

Let


$$
c_m=\min\{v_3(X_m),v_3(Y_m)\}.
$$



If $\psi(H)\ne0$, Theorem 7.1 gives


$$
\boxed{c_m=3,\qquad [\bar X_m:\bar Y_m]=[1:-1]\pmod3.}
\tag{8.1}
$$



Theorem 4.1 already proves that every coefficient of both Jacobi polynomials is divisible by $27$. Since each evaluated endpoint has valuation exactly $3$, neither polynomial can have larger full content. Therefore


$$
\boxed{
\operatorname{cont}_3(J_m^{[A]})
=
\operatorname{cont}_3(J_{m-1}^{[A]})
=3
\quad\text{when }\psi(H)\ne0.
}
\tag{8.2}
$$



This equality is proved on the stated cylinder-language branch. It is not a general identification of polynomial and endpoint content.

The retained observation law is


$$
c(V_{m-1})-c_m
=
4+\min\{2,v_3(\bar Y_m-3\bar X_m)\}.
$$


For the primitive direction (8.1), $\bar Y_m$ is a unit, so


$$
\boxed{c(V_{m-1})=7.}
\tag{8.3}
$$



If $\psi(H)=0$, all that follows at this precision is


$$
c_m\ge4.
$$


The full polynomial contents remain at least $3$; they are not thereby proved to be at least $4$.

---

## 9. Original-domain realization and its exact limitation

The accepted congruence calculation gives


$$
4^{84645}\equiv795583\pmod{1594323},
\qquad84645\equiv81\pmod{243}.
$$


Therefore


$$
\boxed{
j\equiv84645\pmod{531441}
\Longrightarrow
m=2^{-1}4^j\equiv1194953\pmod{1594323}.
}
\tag{9.1}
$$



Theorem 4.1 applies to every positive original index in that progression, whether or not it satisfies the real window.

For the window, retain


$$
\alpha=\log_3 4,\quad
a_0=\frac1{2C_{16}},\quad b_0=\frac1{C_{16}},
\quad k=h-1.
$$


For sufficiently large eligible indices,


$$
\frac D{3^k}=1-3^{\{j\alpha\}-1}+3^{-k}.
\tag{9.2}
$$


The final term is retained. Squeezing the exact interval between fixed inner and outer intervals, and using irrational-rotation equidistribution on the fixed progression, gives relative density


$$
\delta=\log_3\frac{1-a_0}{1-b_0}>0.
\tag{9.3}
$$



The original window still forces the leading $1^{25}$, because $C_{16}>3^{25}$. Hence:

### Theorem 9.1 — Original positive-density $c_m\ge3$ family

The sufficiently large exact-window indices in


$$
j\equiv84645\pmod{531441}
$$


satisfy


$$
\boxed{c_m\ge3,}
$$


and have density


$$
\boxed{\delta/531441}
$$


among all positive $j$.

### What this does not realize

To obtain $c_m=3$ from the new classification, the actual entire intervening word must satisfy


$$
H\in\{0,1\}^{*}\{1,2\}^{*}.
\tag{9.4}
$$


An arbitrary finite trailing extension does not force this condition on all more significant digits.

Accordingly:

* the original positive-density $c_m\ge3$ theorem is unconditional;
* the exact-$c_m=3$ direction theorem is unconditional for every stated cylinder word satisfying (9.4);
* infinitude of original exact-window powers satisfying (9.4) is not proved.

Nor is a relative-density-one $c_m\ge4$ assertion being made. The supplied Lagarias theorem concerns omission of a single digit in $\lfloor\lambda2^k\rfloor$, for fixed $\lambda$. It does not, as stated, supply the required count for the moving split language (9.4).

This is now a precise global digit bottleneck, rather than an unspecified inherited-carry problem.

---

## 10. Jacobi/Christoffel transport remains a separate arithmetic map

The established exact identity remains


$$
Z_{\rm src}(-1)
=
\frac{(1+\beta_m+\chi_m)X_m+\rho_mY_m}{A+74},
\qquad
\rho_m=\frac{A(3A+1)}{(4A+1)(4A+3)}.
\tag{10.1}
$$



The corresponding affine endpoint map has determinant


$$
\frac{\rho_m}{A+74},
$$


of valuation $4$ on the retained branch. It is not unimodular.

On the separately justified scalar branch $\chi_m\in3\mathbb Z_3$, write


$$
\lambda_m=\frac{1+\beta_m+\chi_m}{A+74},\qquad
\mu_m=\frac{\rho_m}{A+74}.
$$


Then


$$
\lambda_m\equiv-1\pmod3,\qquad v_3(\mu_m)=4.
$$



For a cylinder word with $\psi(H)\ne0$,


$$
\frac{Z_{\rm src}(-1)}{27}
\equiv-\psi(H)\pmod3.
\tag{10.2}
$$


Thus the transformed endpoint pair also has content exactly $3$.

This does not establish the scalar congruence


$$
\mathfrak a=\chi_m/3\equiv25\pmod{27},
$$


or actual-force preservation, or an original infinite family on that scalar branch. Recovering the second primitive endpoint from the transformed pair still pays the four-digit inverse loss.

The content equality (8.2) is a genuine new input available **if** an original index satisfying the nonzero-language condition is supplied. It does not supply the remaining scalar hypotheses.

---

## 11. A concrete complete-force transfer lemma

The new local arithmetic gives a definite primitive direction, not merely another zero layer. To use it in the finite producer, the next task should be an exact structured contraction of the complete residual.

The appropriate criterion is stronger and more targeted than entrywise precision of the matrix perturbation.

### Lemma 11.1 — Exact residual criterion for endpoint transfer

Let $E$ be the actual finite matrix over $\mathbb Z_3$, nonsingular over $\mathbb Q_3$. Let $z_0$ be a proposed reference solution and


$$
f_{\rm comp}=b-Ez_0
$$


the **complete actual residual**, in the same row normalization. Let $L$ be the two-row physical endpoint extraction matrix, including the actual column normalization. Put


$$
d_E=v_3(\det E).
$$


Then


$$
z_{\rm act}-z_0=E^{-1}f_{\rm comp},
$$


and


$$
\boxed{
L(z_{\rm act}-z_0)\in3^{c+1}\mathbb Z_3^2
\iff
L\,\operatorname{adj}(E)f_{\rm comp}
\in3^{d_E+c+1}\mathbb Z_3^2.
}
\tag{11.1}
$$



**Proof.** Use


$$
E^{-1}=\frac{\operatorname{adj}(E)}{\det E},
$$


and write $\det E=3^{d_E}u$, $u\in\mathbb Z_3^\times$. Division by the unit $u$ does not change valuations. ∎

For the newly classified primitive branch $c=3$, the required congruence is


$$
\boxed{
L\,\operatorname{adj}(E)f_{\rm comp}
\equiv0\pmod{3^{d_E+4}}.
}
\tag{11.2}
$$



This is an exact, two-coordinate structured-force obligation. It neither replaces the complete residual by its leading pole nor assumes that an entrywise $3^6$ perturbation survives a large inverse loss.

What remains to be done is to instantiate $E,L,f_{\rm comp}$ with the retained finite producer and prove the contraction (11.2), or evaluate its nonzero correction. No such contraction is claimed here.

---

## 12. The complete finite producers are unchanged

The finite spaces remain


$$
0\le v\le2n-2,
$$




$$
U_u=x^u\quad(0\le u<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m),\qquad
d=\frac{3D}{2}-1,\qquad \nu=\frac D2-1.
$$



Both corrected columns remain


$$
\widehat Z^{\,\mathrm{act}}
=
\widehat Z^{\,c}-3^6WE_{\mathrm{act}}^{-1}T_R,
$$


with the complete Schur correction


$$
S_{\mathrm{act}}-S_c
=
3^6K_Z-3^{12}T_R^TE_{\mathrm{act}}^{-1}T_R.
$$


Also retain


$$
Q_{\mathrm{act}}=Q_c+3^6R_{\mathrm{prod}},
\qquad
R_{\mathrm{prod}}=R_{25}+3^{25}\Delta_{25}.
$$



The complete finite perturbation remains


$$
\begin{aligned}
\Delta_{ad}
={}&-\frac{3^h}{4}\mathfrak f(Q_{\mathrm{act}}y^{a+d})\\
&+3^{h+6}
\sum_{2v+1\le4n-3}
\frac{
[y^v]\bigl(R_{\mathrm{prod}}y^{a+d}
-(-1)^{a+d}R_{\mathrm{prod}}(-1)\bigr)/(y+1)
}{2v+1},
\end{aligned}
\qquad0\le a,d\le m.
\tag{12.1}
$$


This retains the full pole pair, both leading extractions, every permitted lower pole, factorial forcing, LOW subtraction, every correction layer, and the unpaired finite-boundary terms.

The terminal return remains


$$
\mu_{i+\nu}^{\langle26\rangle}
+\sum_{k=0}^{\nu-1}f_k\mu_{i+k}^{\langle26\rangle}
=b_i^{\langle26\rangle},
\qquad0\le i\le\nu-2,
$$




$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
\tag{12.2}
$$


No moment beyond $D-4$ is introduced, and $\omega_{\nu-1}$ is retained.

After all actual row contents, the actual multiplier, and the least actual clearer,


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
\qquad
g_\ell=\gcd(|A_\ell|,|B_\ell|)
$$


still use the gcd over **all primes**. For $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
$$


and


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{g_\ell}
\det H_{\rm complete}.
}
\tag{12.3}
$$



The weighted producer likewise retains


$$
A_B=N_{B,1}^T\Omega N_{B,1},\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B,
$$


with the whole evaluated error


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
\tag{12.4}
$$



The local content $3$, when exact, is not a substitute for these row contents, final gcds, actual denominators, or whole errors.

---

## 13. New bounded arithmetic for independent corroboration

No accepted modulo-$9$, modulo-$27$, or discrete-log computation needs to be repeated. No further computation is a premise of the proofs above.

For independent corroboration of the new divided-image theorem, a genuinely new modulo-$81$ calculation is available with an explicit bounded module.

### 13.1 A paid modulo-$81$ evaluator

Use denominator $Q^{80}$, degree at most $160$, and initial endpoint numerators


$$
N_X^{(81)}=b^{79}a^{80},\qquad
N_Y^{(81)}=ub^{78}a^{81}.
\tag{13.1}
$$



The Frobenius identity is


$$
\sigma(u)\equiv
\sigma(u^3)\frac{Q(u^3)^{13}}{Q(u)^{40}}
\pmod{81}.
$$


From the exact ratio (2.3),


$$
R^q
\equiv
\sum_{\substack{i,j\ge0\\i+j\le3}}
(-3)^i3^j
\binom{3q}{i}\binom{-q}{j}
\frac{u^{i+j}}{a^{2i}b^{2j}}
\pmod{81}.
$$


Thus


$$
\boxed{
\begin{aligned}
\mathcal U^{(81)}_{r,q}(N)
=Q(v)^{39}\Lambda_0
\sum_{\substack{i,j\ge0\\i+j\le3}}
&(-3)^i3^j\binom{3q}{i}\binom{-q}{j}\\
&\cdot u^{i+j-r}N
a^{42-3r-2i}b^{42+r-2j}
\pmod{81}.
\end{aligned}
}
\tag{13.2}
$$


Only $q\bmod27$ is required.

Padding to $Q^{162}$, sectioning, and restoring $Q^{80}$ proves the formula exactly as in Section 2. Its output degree is at most $159$, so the $161$-coordinate space is invariant.

This is a specification for a new calculation, not a claim that it has been executed.

### 13.2 Minimal inputs and expected output

**Inputs**

* the two polynomials (13.1);
* transition (13.2);
* the full low-to-high digit sequence
  

$$
2,1,1,1,1,0,1,0,\ 2,0,2,0,2,\ \operatorname{reverse}(H),\ 1^{25};
$$


* three-digit lookahead, with zeros beyond the leading block;
* $H=\varnothing,\ 0,\ 20$.

**Expected verifiable output**


$$
\boxed{
(27,54),\qquad(54,27),\qquad(0,0)\pmod{81},
}
\tag{13.3}
$$


respectively.

A larger but still bounded new corroboration can use all $H$ of lengths $4$ and $5$, comparing each modulo-$81$ endpoint pair with


$$
27\bigl(\psi(H),-\psi(H)\bigr)\pmod{81}.
$$


That is a new-precision test, not a rerun of the forty modulo-$27$ zeros. It would establish only the stated finite comparisons; the every-word conclusion rests on the proof above.

No individual original real-window index is certified by this proposed calculation.

---

## 14. Proof-status ledger and remaining bottlenecks

| Statement | Status |
|---|---|
| Coordinator modulo-$27$ module at general degree and index | Proved in Section 2 |
| Previously reported finite receipts | Accepted at their stated finite scopes; not rerun |
| Universal $H20202$ endpoint vanishing modulo $27$ | Proved |
| Full Jacobi polynomial content at least $3$ on the fixed tail | Proved termwise |
| Original positive-density $c_m\ge3$ family at $j\equiv84645\pmod{531441}$ | Proved |
| Next divided image $(X_m/27,Y_m/27)\bmod3$ | Explicitly determined and proved |
| Exact nonzero language for that image | Proved |
| Primitive direction $[1:-1]$, exact full contents $3$, and observation content $7$ on that language | Proved |
| Infinite original exact-window family in the nonzero language | Not proved |
| Relative-density-one higher cancellation | Not asserted |
| Scalar congruence and actual complete-force preservation | Open |
| Actual all-prime primitive denominator and whole nonzero same-index error comparison | Open |
| Proposed modulo-$81$ corroboration | Unevaluated specification; not a premise |

The local obstruction has changed substantially. It is no longer the absence of a paid quotient or the unknown inherited suffix carry. Those have been resolved through the valuation-three observable.

The remaining arithmetic bottlenecks are now:

1. **Original reachability:** produce an infinite original exact-window family for which the complete intervening word lies in
   

$$
\{0,1\}^{*}\{1,2\}^{*},
$$


   or determine a different primitive layer on a realizable family.

2. **Scalar and complete-force transfer:** verify the separate scalar branch and evaluate the exact residual contraction (11.2), with both corrected columns, the full finite force, and terminal return retained.

3. **Global normalization and error:** control the actual all-prime primitive denominator against the whole evaluated nonzero error at the same indices.

## Conclusion

The forty modulo-$27$ zeros reflect a genuine universal theorem:


$$
\boxed{
m\equiv1194953\pmod{1594323}
\Longrightarrow
J_m^{[\,2m-1\,]},J_{m-1}^{[\,2m-1\,]}
\in27\mathbb Z_3[y].
}
$$



The next layer is not left as an unspecified larger automaton:


$$
\boxed{
\left(X_m/27,Y_m/27\right)
\equiv(\psi(H),-\psi(H))\pmod3,
}
$$


with an explicit signed observable and the exact nonvanishing language


$$
\boxed{\psi(H)\ne0\iff H\in\{0,1\}^{*}\{1,2\}^{*}.}
$$



This supplies a genuine primitive-direction and full-content statement wherever the next image is nonzero. It also exposes precisely why the fixed original index congruence alone cannot guarantee that nonzero branch.

The original positive-density $c_m\ge3$ family is proved. An original infinite primitive-direction family, complete-force preservation, and the actual denominator/whole-error comparison are not.



$$
\boxed{\text{The irrationality or rationality of }e+\pi\text{ remains unresolved.}}
$$


