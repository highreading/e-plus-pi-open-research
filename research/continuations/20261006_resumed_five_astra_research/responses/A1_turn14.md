> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1 turn14 — An evaluated characteristic-three Cartier observable for the actual endpoint pair

## Executive conclusion

The requested finite characteristic-three observable can be constructed and evaluated explicitly. It has a seven-dimensional polynomial numerator space, and, after the prescribed eight-digit suffix, its reachable states reduce to


$$
\boxed{\{0,R,-R,P,-P\}.}
$$



The resulting evaluation on the prefix–middle–suffix language is particularly simple. Write the base-three expansion of $m$, from most significant to least significant digit, as


$$
\boxed{m=(1^{25}\,M\,01011112)_3,}
\tag{0.1}
$$


where $M$ is the intervening middle word. Leading ones beyond the prescribed twenty-five are included in $M$. Let $N_{01}(M)$ be the number of adjacent occurrences of $01$ in $M$, read in the usual most-significant-digit-first order. Define


$$
\eta(M)=
\begin{cases}
0,&\text{if \(M\) contains a digit \(2\)},\\
(-1)^{N_{01}(M)}\in\mathbb F_3,&\text{if \(M\) uses only \(0,1\)}.
\end{cases}
\tag{0.2}
$$



For the **actual unit-branch generating functions** in the assignment, the answer is


$$
\boxed{
(a_m,b_m)\equiv \bigl(2\eta(M),\,\eta(M)\bigr)\pmod3.
}
\tag{0.3}
$$


The corresponding same-index state outputs satisfy


$$
\boxed{(w_m,s_m)\equiv\bigl(\eta(M),\eta(M)\bigr)\pmod3.}
\tag{0.4}
$$



Thus the middle word has not disappeared: its dependence is exactly evaluated by a five-state automaton.

* If the middle word contains no $2$, the endpoint pair is nonzero modulo $3$, and therefore its common $3$-adic content is exactly zero.
* If the middle word contains a $2$, both endpoints are divisible by $3$. This is **only divisibility**, not an evaluation of their primitive pair.
* The word witnesses below establish dependence on the prefix–suffix cylinder. They are not claimed to be witnesses among the original powers $m=2^{2j-1}$ satisfying the real window.

An additional same-index check gives


$$
\boxed{(w_{m-1},s_{m-1})\equiv(0,0)\pmod3}
\tag{0.5}
$$


throughout this cylinder. There is no conflict with a nonzero endpoint pair: the accepted observation matrix at $m-1$ has negative Smith exponents $(-6,-4)$.

No original tuple, complete producer, primitive denominator, or whole error is evaluated here. Irrationality of $e+\pi$ remains unresolved.

---

## 1. Scope and accepted inputs

I retain the original domain


$$
j>0,\qquad j\equiv81\pmod{243},\qquad
m=2^{2j-1},\qquad A_{\mathrm{ind}}=2m-1,
$$


and


$$
H_{\mathrm{win}}=3^{h-1},\qquad D=H_{\mathrm{win}}-A_{\mathrm{ind}},
$$




$$
\frac1{2C_{16}}<\frac D{H_{\mathrm{win}}}<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
\tag{1.1}
$$



Statements invoking the normalized scalar comparison still require


$$
m\equiv851\pmod{6561},\qquad
r=\operatorname{cont}_3(J_m)=\operatorname{cont}_3(J_{m-1}),
$$




$$
s=h-2-2r,\qquad
\mathfrak a\equiv25\pmod{27},\qquad
N_m\in\mathbb Z_3^\times.
\tag{1.2}
$$



The following source results are reused at their proved scope:

* the actual algebraic endpoint generating functions;
* the seeded recurrence for $V_n=(w_n,s_n)^T$;
* the exact same-index observation
  

$$
(a_m,b_m)^T=O(m-1)V_{m-1};
$$


* the original-branch observation exponents $(-6,-4)$;
* the exact phase Smith table and capped projective lifting rule;
* the proved linear content bound.

The receipt’s checks remain finite corroboration. In particular, the sample $m=851$ is not an original-window tuple.

The finite-field extraction mechanism below is classical Cartier machinery. The new work here is its explicit realization, transition calculation, and evaluation for these particular four outputs and this particular digit language.

---

## 2. A common seven-dimensional numerator space

All calculations in Sections 2–6 are over $\mathbb F_3$.

Use the actual branch


$$
u(1+u^3)=x(1-u),\qquad
\sigma^2=1-u^2,\qquad
u(0)=0,\quad \sigma(0)=1.
$$


Since $1+u^3=(1+u)^3$,


$$
x=\frac{u(1+u)^3}{1-u}.
\tag{2.1}
$$



The four outputs are


$$
\mathcal A=\sigma,\qquad
\mathcal B=\sigma\frac{x}{(1+u)^2},
\qquad
W=\sigma\frac{1-u}{1+u},
\qquad
S=\sigma(1-u).
\tag{2.2}
$$



Differentiation in characteristic three gives


$$
\boxed{\frac{dx}{x}=\frac{du}{u(1-u)}.}
\tag{2.3}
$$



For an output $f$, coefficient extraction can therefore be expressed as


$$
[x^n]f=\operatorname{res}_{u=0}
x(u)^{-n}f(u)\frac{dx}{x}.
\tag{2.4}
$$


The local parameter change is legitimate because $x=u+O(u^2)$.

Define


$$
D_*(u)=u(1-u)^2(1+u)^4
$$


and the differential associated with a numerator $H$:


$$
\omega_H=\frac{\sigma H(u)}{D_*(u)}\,du.
\tag{2.5}
$$



The numerator space is


$$
\boxed{\mathscr H=\{H\in\mathbb F_3[u]:\deg H\le6\}.}
\tag{2.6}
$$


It has seven basis elements $1,u,\ldots,u^6$, hence only $3^7$ possible numerator states.

The initial numerators for the actual outputs are:



$$
\begin{array}{c|c|c}
f&H_f\text{ such that }\omega_{H_f}=f\,dx/x
&(h_0,h_1,\ldots,h_6)\\ \hline
\mathcal A&(1-u)(1+u)^4&(1,0,2,1,0,2,0)\\
\mathcal B&u(1+u)^5&(0,1,2,1,1,2,1)\\
W&(1-u)^2(1+u)^3&(1,1,1,1,1,1,0)\\
S&(1-u)^2(1+u)^4&(1,2,2,2,2,2,1).
\end{array}
\tag{2.7}
$$



These numerators encode the specified branch and seed. They are not freely chosen algebraic solutions.

The final evaluation functional is


$$
\boxed{\epsilon(H)=H(0)=h_0.}
\tag{2.8}
$$


Indeed, $\sigma(0)=1$ and $D_*(u)/u$ has constant term one, so
$\operatorname{res}_{u=0}\omega_H=H(0)$.

---

## 3. Explicit digit transitions and proof of invariance

Let $\mathcal C$ denote Cartier on differentials. In the separating coordinate $u$,


$$
\mathcal C\!\left(\sum_i c_i u^i\,du\right)
=\sum_j c_{3j+2}u^j\,du,
$$


with the standard extension


$$
\mathcal C(g^3\omega)=g\,\mathcal C(\omega).
\tag{3.1}
$$



Because


$$
\sigma=\frac{\sigma^3}{1-u^2},
$$


equations (2.1) and (2.5) give, for $r=0,1,2$,


$$
\mathcal C(x^{-r}\omega_H)=\omega_{\Phi_r(H)},
\tag{3.2}
$$


where


$$
\boxed{
\Phi_r(H)=
\sum_{j\ge0}[u^{3j+2}]\bigl(H(u)K_r(u)\bigr)\,u^j
}
\tag{3.3}
$$


and


$$
K_r(u)=u^{2-r}(1-u)^{3+r}(1+u)^{7-3r}.
\tag{3.4}
$$



This identity follows directly by writing


$$
x^{-r}\omega_H
=
\left(\frac{\sigma}{D_*}\right)^3
H(u)K_r(u)\,du.
$$



### 3.1 The three small multiplier polynomials

Exact expansion over $\mathbb F_3$ yields


$$
\boxed{
\begin{aligned}
K_0&=u^2+u^3+u^5+u^6-u^8-u^9-u^{11}-u^{12},\\
K_1&=u-u^3-u^7+u^9,\\
K_2&=1-u-u^2+u^4+u^5-u^6.
\end{aligned}}
\tag{3.5}
$$



Their degrees are $12,9,6$. Consequently, for $\deg H\le6$,


$$
\deg\Phi_0(H)\le5,\qquad
\deg\Phi_1(H)\le4,\qquad
\deg\Phi_2(H)\le3.
\tag{3.6}
$$


This proves the genuinely finite numerator invariant.

### 3.2 Full coordinate transitions

For $H=(h_0,\ldots,h_6)$, all coordinates below are in $\mathbb F_3$:


$$
\boxed{
\begin{aligned}
\Phi_0(H)=\bigl(&h_0,\\
&h_3+h_2+h_0,\\
&h_6+h_5+h_3+h_2-h_0,\\
&h_6+h_5-h_3-h_2-h_0,\\
&-h_6-h_5-h_3-h_2,\\
&-h_6-h_5,\ 0\bigr),
\end{aligned}}
\tag{3.7}
$$




$$
\boxed{
\Phi_1(H)=
(h_1,\ h_4-h_2,\ -h_5-h_1,\ h_2-h_4,\ h_5,\ 0,\ 0),
}
\tag{3.8}
$$




$$
\boxed{
\Phi_2(H)=
(h_2-h_1-h_0,\ 
h_5-h_4-h_3+h_1+h_0,\ 
-h_6+h_4+h_3-h_2,\ 
h_6-h_5,\ 0,\ 0,\ 0).
}
\tag{3.9}
$$



These are explicit transitions for each of the three ternary digits.

### 3.3 Coefficient-evaluation theorem

If


$$
n=d_0+3d_1+\cdots+3^{L-1}d_{L-1},
$$


then


$$
\boxed{
[x^n]f=
\epsilon\!\left(
\Phi_{d_{L-1}}\cdots\Phi_{d_1}\Phi_{d_0}(H_f)
\right).
}
\tag{3.10}
$$



To prove this, write $n=3q+r$. Cartier preserves residues, and


$$
x^{-n}\omega_H=(x^{-q})^3x^{-r}\omega_H.
$$


Therefore


$$
\operatorname{res}x^{-n}\omega_H
=
\operatorname{res}x^{-q}\omega_{\Phi_r(H)}.
$$


Iteration finishes at the residue functional (2.8).

The digits are processed **least significant first**.

---

## 4. Evaluation of the prescribed suffix and leading ones

### 4.1 The suffix $851\bmod6561$

The eight ternary digits are


$$
851=(01011112)_3.
$$


Their processing order is


$$
2,1,1,1,1,0,1,0.
$$


Thus the suffix operator is


$$
\mathcal F=
\Phi_0\Phi_1\Phi_0\Phi_1^4\Phi_2.
\tag{4.1}
$$



Define


$$
\boxed{R=(-1,1,0,-1,1,0,0).}
\tag{4.2}
$$



A direct calculation with (3.7)–(3.9) gives the rank-one formula


$$
\boxed{
\mathcal F(H)=
(h_5-h_4-h_3+h_1+h_0)R.
}
\tag{4.3}
$$



Here is a compact derivation, including the intermediate cancellation. After $\Phi_2$ and then $\Phi_1^4$, the state has the form


$$
(p,q,-p,-q,0,0,0),
$$


where


$$
p=h_6-h_4-h_3+h_2,\qquad
q=h_5-h_4-h_3+h_1+h_0.
$$


The remaining three transitions give


$$
(p,q,-p,-q,0,0,0)
\xrightarrow{\;0\;}
(p,-q,p-q,q,p+q,0,0)
$$




$$
\xrightarrow{\;1\;}
(-q,-q,q,q,0,0,0)
\xrightarrow{\;0\;}qR.
$$



Applying (4.3) to the four initial numerators:


$$
\boxed{
\begin{array}{c|cccc}
f&\mathcal A&\mathcal B&W&S\\ \hline
\mathcal F(H_f)&2R&R&R&R.
\end{array}}
\tag{4.4}
$$



This is a evaluated suffix certificate for the actual four outputs.

### 4.2 The forced twenty-five leading ones

For a general numerator $H$,


$$
\Phi_1^2(H)
=
(h_4-h_2,\ h_1-h_5,\ -h_4+h_2,\ -h_1+h_5,\ 0,0,0).
\tag{4.5}
$$


On states of the form


$$
(p,q,-p,-q,0,0,0),
$$


the transition $\Phi_1$ swaps $p,q$. Since $25$ is odd,


$$
\boxed{
\epsilon(\Phi_1^{25}H)=h_1-h_5.
}
\tag{4.6}
$$



Thus the full prescribed leading block has been evaluated as the explicit functional


$$
\boxed{L(H)=h_1-h_5.}
\tag{4.7}
$$


It is not left as an unevaluated matrix power.

---

## 5. Five reachable states and exact middle-word dependence

Put


$$
\boxed{P=(1,1,-1,-1,0,0,0).}
\tag{5.1}
$$



The transition identities are


$$
\boxed{
\begin{array}{c|ccc|c}
\text{state}&0&1&2&L\\ \hline
R&R&P&0&1\\
P&-R&P&0&1\\
-R&-R&-P&0&-1\\
-P&R&-P&0&-1\\
0&0&0&0&0.
\end{array}}
\tag{5.2}
$$



Every entry follows by substitution in (3.7)–(3.9). This set is both closed under all three digits and reachable from $R$:

* $R$ is the initial suffix state;
* $P$ is reached by $1$;
* $-R$ is reached by the processing word $10$;
* $-P$ is reached by $101$;
* $0$ is reached by $2$.

Therefore (5.2) is a complete reachable-state table for the post-suffix observable, not merely a list of sampled states.

### Theorem 5.1 — Exact language evaluation

For every finite middle word $M$, including the empty word, equations (0.2)–(0.4) hold.

#### Proof

Process the middle word from right to left.

If any processed digit is $2$, the state becomes zero and remains zero.

Otherwise the state is a signed copy of $R$ or $P$. A digit $1$ puts it in the corresponding signed $P$-state. A digit $0$ puts it in a signed $R$-state, and changes the sign precisely when the preceding processed digit was $1$.

The starting state is $R$, so there is no initial sign change. Hence sign changes count adjacent $10$ in processing order, equivalently adjacent $01$ in the usual written order of $M$. The final functional takes value $1$ on both $R$ and $P$.

Together with the suffix scalars $2,1,1,1$, this proves the claimed four output values. ∎

### 5.1 Witness transitions

Three same-length middle words illustrate all possible values:


$$
\boxed{
\begin{array}{c|c|c|c}
M\text{, written MSB first}&\text{processing order}&\eta(M)&(a_m,b_m)\bmod3\\ \hline
000&000&1&(2,1)\\
011&110&-1&(1,2)\\
002&200&0&(0,0).
\end{array}}
\tag{5.3}
$$



For the nontrivial sign witness,


$$
R\xrightarrow{1}P\xrightarrow{1}P\xrightarrow{0}-R.
$$


For the zero witness,


$$
R\xrightarrow{2}0.
$$



All three middle words have even digit sum, so these examples do not depend on allowing an odd value of $m$. Nevertheless, they are **cylinder-language witnesses only**: no claim is made that their associated integers are powers $2^{2j-1}$, or satisfy the real window.

### 5.2 Exact consequence for eligible original indices

Every eligible original index possessing the stipulated digit decomposition is covered by the theorem. What remains unevaluated is which middle words actually occur among those original powers.

In particular,


$$
\boxed{
\begin{aligned}
M\in\{0,1\}^*
&\Longrightarrow c_m=0,\\
M\text{ contains }2
&\Longrightarrow c_m\ge1.
\end{aligned}}
\tag{5.4}
$$



This is a precise content obstruction, with a complete first-digit evaluation. It is not a uniform nonvanishing theorem for the original family.

---

## 6. The original state index $m-1$

The endpoint pair in (0.3) is extracted at index $m$. The observation identity uses $V_{m-1}$, so that shift must not be suppressed.

Since subtracting one changes only the final suffix digit,


$$
m-1=(1^{25}M01011111)_3.
$$


The corresponding suffix operator is


$$
\mathcal F_-=\Phi_0\Phi_1\Phi_0\Phi_1^5.
$$


The same intermediate calculation as in Section 4 gives


$$
\boxed{\mathcal F_-(H)=(h_4-h_2)R.}
\tag{6.1}
$$



For both actual state numerators,


$$
h_4-h_2=0:
\qquad
H_W:\ 1-1=0,\qquad
H_S:\ 2-2=0.
$$


Consequently


$$
\boxed{V_{m-1}\equiv(0,0)^T\pmod3}
\tag{6.2}
$$


for every intervening middle word.

This is again only a divisibility statement. It does not justify dividing the zero state by $3$ within the characteristic-three automaton.

The accepted original-branch observation inequality


$$
c(V_{m-1})-6\le c_m\le c(V_{m-1})-4
\tag{6.3}
$$


is retained unchanged. In particular, the nonzero endpoint cases in (5.4) have


$$
4\le c(V_{m-1})\le6.
$$


The new automaton does not select the exact state content within that interval.

---

## 7. Paid lifting when the first endpoint pair is zero

A characteristic-three zero state contains no information about the quotient by $3$. The exact obstruction is loss of higher $3$-adic digits, not failure of finite-field automaticity.

Here is a proved lifting mechanism, with its precision cost exposed.

### 7.1 Direct endpoint lifting

Work over $\mathbb Z/3^L\mathbb Z$, using the characteristic-zero identities


$$
P(x,t)=t^4-t^3+xt-2x=0,\qquad t(0)=1,
$$




$$
\sigma^2=t(2-t),\qquad \sigma(0)=1,
$$




$$
\mathcal A=\frac{\sigma t}{d(t)},\qquad
\mathcal B=\mathcal A\frac{t(t-1)}{2-t},
\qquad d(t)=-3t^2+10t-6.
\tag{7.1}
$$



The relevant constant terms are units:


$$
P_t(0,1)=1,\qquad 2\sigma(0)=2,\qquad
d(1)=1,\qquad 2-t(0)=1.
$$


Thus coefficient-by-coefficient implicit solving and unit-series inversion determine these series modulo


$$
(3^L,x^{m+1})
$$


without division by $3$.

It follows that $a_m,b_m\bmod3^L$ can be obtained by a finite, exact calculation at any specified $L$.

If


$$
c_m=r,
$$


then the primitive $3$-adic endpoint pair modulo $3^K$ requires, and is supplied by,


$$
\boxed{(a_m,b_m)\bmod3^{r+K}.}
\tag{7.2}
$$


Division by $3^r$ is performed on representatives known to that precision; changing representatives changes the quotient only by a multiple of $3^K$.

An adaptive calculation increases $L$ until the first nonzero endpoint digit appears. On the retained original branch, the already proved bound


$$
c_m\le m-7+v_3((2m-1)!)
\tag{7.3}
$$


provides a finite termination bound. This is a linear-scale bound, not a digit-compressed complexity claim.

### 7.2 Lifting through the accepted observation map

Alternatively, since every entry of $O(m-1)$ has valuation at least $-6$,


$$
\boxed{
V_{m-1}\bmod3^{L+6}
\quad\Longrightarrow\quad
(a_m,b_m)\bmod3^L.
}
\tag{7.4}
$$


Indeed, an input error in $3^{L+6}\mathbb Z_3^2$ produces an output error in $3^L\mathbb Z_3^2$.

Therefore primitive endpoint precision $3^K$, once $r=c_m$ is known, is guaranteed by


$$
\boxed{V_{m-1}\bmod3^{r+K+6}.}
\tag{7.5}
$$



If the state is computed by normalized recurrence, the accepted local lifting theorem still charges $r_n$ additional digits at each normalized transition. Nothing in the mod-$3$ automaton bounds that cumulative bill.

These are paid lifting mechanisms. Neither is claimed to be an evaluated higher-layer automaton or a feasible original-index calculation.

---

## 8. What has advanced, and the concrete next lemma

The earlier characteristic-zero infinite section-rank result presents no obstruction to the construction above. It concerns a different coefficient field and a different unrestricted realization problem.

The primary target has advanced from an algebraic existence statement to:

1. an explicit finite numerator invariant;
2. all three digit transitions;
3. the actual four starting numerators;
4. an explicit residue evaluation;
5. an evaluated suffix;
6. an evaluated twenty-five-digit leading block;
7. a complete five-state post-suffix table;
8. an exact rule for every intervening middle word.

The remaining primary arithmetic question is no longer “does the middle word matter?” It does, exactly as in (0.2).

A concrete follow-on target is:

> **Original-power middle-word lemma.**  
> For the retained original powers $m=2^{2j-1}$ satisfying the real window and the stipulated suffix and leading digits, determine whether their intervening ternary middle words can avoid the digit $2$. If they can, classify or exhibit eligible indices in that sublanguage. If they cannot, prove the exclusion and then evaluate the first nonzero $3$-adic endpoint layer with the precision charge in Section 7.

The word examples in (5.3) do not prove existence in this original-power subfamily.

The optional degree-twelve rational block numerator calculation was not needed for this primary advance and is not substituted for the now-explicit digit evaluation.

---

## 9. Full-producer and primitive-arithmetic boundaries

The new endpoint congruence changes none of the original finite constructions.

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



Both corrected columns and the nonlinear correction remain


$$
\widehat Z^{\,\mathrm{act}}
=\widehat Z^{\,c}-3^6WE_{\mathrm{act}}^{-1}T_R,
$$




$$
S_{\mathrm{act}}-S_c
=3^6K_Z-3^{12}T_R^TE_{\mathrm{act}}^{-1}T_R,
$$




$$
Q_{\mathrm{act}}=Q_c+3^6R_{\mathrm{prod}},
\qquad
R_{\mathrm{prod}}=R_{25}+3^{25}\Delta_{25}.
$$


Here the producer matrix $W$ is distinct from the generating function $W(x)$ used above.

Every $\Delta_H$ layer, unpaired cutoff contribution, exterior term, corrected factor and nonlinear term remains required. Complete forcing retains the full pole pair, both leading extractions, every permitted lower pole, factorial forcing and LOW subtraction.

The terminal return remains


$$
\mu_{i+\nu}^{\langle26\rangle}
+\sum_{k=0}^{\nu-1}f_k\mu_{i+k}^{\langle26\rangle}
=b_i^{\langle26\rangle},
\qquad0\le i\le\nu-2,
$$




$$
J^T\varepsilon+\omega
=-\varepsilon-s_{\mathrm{ret}}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
$$


No moment beyond $D-4$ is introduced, and $\omega_{\nu-1}$ is retained.

All row contents, the actual multiplier and the least actual clearer precede


$$
A_\ell=\ell_{\mathrm{clr}}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\mathrm{clr}}^{m+1}\beta_1,
$$




$$
g_\ell=\gcd(|A_\ell|,|B_\ell|)
$$


over **all primes**. For $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
$$


and the whole same-index error is


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\mathrm{clr}}^{m+1}}{g_\ell}
\det H_{\mathrm{complete}}.
}
$$



The second producer retains


$$
A_B=N_{B,1}^T\Omega N_{B,1},\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B,
$$


with


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
$$



A nonzero endpoint pair modulo $3$ does not evaluate these all-prime gcds or either whole error.

---

## 10. Bounded exact verification and proof-status ledger

No previously accepted bounded computation needs to be rerun.

The new hand-derived certificate can be checked using only arithmetic in $\mathbb F_3$.

### Inputs

* The four vectors in (2.7).
* The three multiplier polynomials in (3.5).
* The extraction rule (3.3).
* The two vectors $R,P$.

### Expected verifiable outputs

1. The coordinate transitions (3.7)–(3.9).
2. The rank-one suffix identity
   

$$
\Phi_0\Phi_1\Phi_0\Phi_1^4\Phi_2(H)
   =(h_5-h_4-h_3+h_1+h_0)R.
$$


3. The leading-block functional
   

$$
\epsilon\Phi_1^{25}(H)=h_1-h_5.
$$


4. The five-state table (5.2).
5. The shifted-suffix identity
   

$$
\Phi_0\Phi_1\Phi_0\Phi_1^5(H)=(h_4-h_2)R.
$$



These are bounded polynomial and vector identities. The proofs above already establish them; an independent calculation would be corroboration, not a missing premise. No remote execution is assumed or authorized.

| Statement | Status |
|---|---|
| Accepted recurrence, observation identities and local Smith/lifting results | Reused at their proved scope |
| Seven-dimensional characteristic-three numerator invariant | **Proved here** |
| Explicit transitions for digits $0,1,2$ | **Derived and evaluated here** |
| Actual four initial output numerators | **Derived here** |
| Suffix $851\bmod6561$ | **Evaluated here** |
| Twenty-five leading ones | **Evaluated here** |
| Complete post-suffix reachable-state table | **Proved here** |
| Every-middle-word formula (0.2)–(0.4) | **Proved here** |
| State divisibility at the actual shifted index $m-1$ | **Proved here** |
| Paid higher-precision lifting mechanism | **Proved here; not executed** |
| Middle-word classification among eligible original powers | Open |
| Primitive pair when the mod-$3$ output is zero | Not evaluated |
| Actual original tuple | None evaluated |
| Complete producers, all-prime primitive denominators and whole errors | Unresolved |

## Conclusion

The new result is the exact finite-language evaluation


$$
\boxed{
(a_m,b_m)\equiv
\begin{cases}
(0,0),&M\text{ contains }2,\\[2pt]
(-1)^{N_{01}(M)}(2,1),&M\in\{0,1\}^*,
\end{cases}
\pmod3.
}
$$



This is a rigorous evaluation of the requested characteristic-three observable on every middle word. It resolves the previous missing transition-table obligation without invoking an inappropriate characteristic-zero no-go argument.

The exact remaining local bottleneck is twofold:

1. determine which middle-word cases occur in the **eligible original-power family**;
2. in the zero-output case, evaluate higher $3$-adic layers with the explicitly paid precision needed for the primitive pair.

Beyond that remain the complete finite producers and the all-prime, same-index whole-error analysis.



$$
\boxed{\text{An unconditional proof or disproof of irrationality of }e+\pi
\text{ remains unresolved by this work.}}
$$


