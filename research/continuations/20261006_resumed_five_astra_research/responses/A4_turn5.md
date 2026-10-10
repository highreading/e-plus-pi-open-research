> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4, Turn 5 — Universal suffix synchronization, exact-window applicability, and an all-prime audit

## Executive conclusion

The coordinator’s new suffix argument is a proof proposal of a different kind from the eleven earlier power samples. Its central synchronization claim is correct:



$$
\boxed{
m\equiv851\pmod{6561}
\quad\Longrightarrow\quad
\operatorname{cont}_3(J_m)=\operatorname{cont}_3(J_{m-1}).
}
$$



The accepted eight-digit vector supplies a finite initial certificate. The universal conclusion follows because **all subsequent input streams and the admissible terminal conditions coincide**. It is not an extrapolation from the eleven samples or the 81 auxiliary complete-content checks.

The constructive upper-content policy is also correct, once its state invariant and termination are stated explicitly. The possible prefix/suffix overlap needs an argument, but it does not invalidate the result: on the sufficiently large exact $C_{16}$ window, overlap is impossible. Consequently, on the **actual unit-normalized deep family**, with all retained finite-support and Schur hypotheses,



$$
\boxed{
r=u,\qquad
\operatorname{cont}_3(\mathcal E)=2r,\qquad
s_c\ge t+23.
}
$$



Thus



$$
\boxed{t\ge9\quad\Longrightarrow\quad s_c\ge32}
$$



on that stated domain. This excludes the proposed uniform inverse-comparison condition $s_c<32$; it does **not** prove that the actual perturbed matrix is singular or that an actual directional/cofactor argument fails.

The supplied primary-text specialization of Matveev’s theorem closes A1’s formerly conditional fixed-real-logarithm input. I give the quantitative progression-hitting argument below, including the exact window and exact resonance. Together with the retained moving-base continuation theorem, this supplies infinitely many original indices on which the required unit normalization and the new exclusion apply. Lack of visual PDF inspection is not a missing theorem-text hypothesis.

A3’s new all-prime moment-state primitivity theorem, its prime-power congruences, and its common normalized-defect law are correct. The singular transfer positions are handled by fixed-seed periodicity, not by fictitious invertibility. Two useful sharper consequences are:

1. the common normalized defect has no factor $13$, in addition to having no factor $3$;
2. on either original endpoint family, its part above $n+2$ is either $1$ or a **single prime to the first power**.

This sharpens the common structural factor in the actual denominator comparison, but does not make either projected endpoint pair primitive.

Finally, the accepted binary identity admits a new exact target-specific reduction: the $126\times126$ denominator kernel can be replaced by **251 common finite weighted moments** and two polynomial contractions. This reduction keeps the original row set and weights. Its denominator has exactly $127$ factors of $2$, so a direct modular implementation must account for a $254$-bit squared-denominator loss. The moment producer itself remains unevaluated.

No original producer, accepted suffix computation, finite jet calculation, or accepted $n=225$ calculation is requested again. No outcome is assigned to the pending $n=3375$ producer.

---

## 1. Scope: three index domains remain distinct

The following constructions must not be merged.

### 1.1 Ternary Jacobi/Schur family

Retain



$$
n=4^j+1,\qquad m=2^{2j-1},\qquad A=2m-1=4^j-1,
$$




$$
j\equiv81\pmod{243},\qquad H=3^{h-1},\qquad D=H-A,
$$


and the sufficiently large exact window


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$



Write


$$
L=h-1,\qquad t=v_3(8m-247)=v_3(4^{j+1}-247).
$$



The retained unit normalization is an additional theorem on the constructed deep family. It is not a consequence of the real window alone.

### 1.2 Endpoint moment families

Retain separately



$$
n=15^r,\quad r\ge2,
\qquad\text{or}\qquad
n=105^r,\quad r\ge2.
$$



These indices are odd and satisfy $9\mid n$. A3’s broader common-defect theorem only requires odd $n$ with $3\mid n$.

### 1.3 Accepted binary input

Retain the single accepted input



$$
b=9^{18}=150094635296999121,
$$




$$
n=4002b=600678730458590482242,
\qquad Q=2^{20},
$$


with


$$
m=76,\quad I=48,\quad R=100,\quad L_0=176,\quad K_0=124.
$$



Its accepted reconstructed-column identity is



$$
\widehat F(z)=\frac{V_f(z)}{(1-z)^{2n+125}},
\qquad
\widehat E(z)=\frac{V_e(z)}{(1-z)^{2n+125}}
\pmod{2^{20}},
$$


where both numerators have degree at most $125$.

No claim below promotes that identity to higher precision or another index.

---

## 2. Universal suffix synchronization: the proof is valid

Let


$$
m=851+6561M,\qquad M\ge0.
$$



The two digit evaluators use



$$
\begin{array}{c|ccc}
&\text{degree}&\text{integral upper index}&\text{half-integral upper index}\\ \hline
J_m&m&3m-1&m-\tfrac12\\
J_{m-1}&m-1&3m-2&m-\tfrac32.
\end{array}
$$



The accepted finite certificate gives, in state order


$$
000,001,010,011,100,101,110,111,
$$


the same exact vector after eight digits:



$$
\boxed{(0,\infty,\infty,\infty,\infty,1,1,3).}
\tag{2.1}
$$



Here the state records addition carry, integral-binomial borrow, and half-integral-binomial borrow.

### 2.1 The remaining streams are exactly equal

The degree quotients after removing eight digits are both $M$.

For the integral upper indices,


$$
3m-1=2552+6561(3M),
$$




$$
3m-2=2551+6561(3M).
$$



For the half-integral indices,


$$
m-\frac12
=
4131+6561\left(M-\frac12\right),
$$




$$
m-\frac32
=
4130+6561\left(M-\frac12\right).
$$



Thus the three remaining streams in both evaluators are exactly



$$
\boxed{M,\qquad 3M,\qquad M-\frac12.}
\tag{2.2}
$$



This includes the infinite $3$-adic half-index tail.

### 2.2 Terminal admissibility is also the same

The terminal rule is not merely “take state $000$ after some arbitrary number of digits.” It requires:

- finite nonnegative coefficient indices;
- zero final addition carry;
- zero final integral borrow;
- eventual clearing of the half-integral borrow;
- zero coefficient digits after their finite support.

After the common suffix, the remaining degree is the same $M$, so these finite-support conditions are identical. Once the degree digits have ended, a zero incoming addition carry forces both coefficient digits to be zero. The integral upper stream is finite, and the half-integral stream is eventually all $1$, so the usual clearing rule is common as well.

No information relevant to these future conditions has been omitted from the three-bit evaluator state.

### Theorem 2.1 — Universal synchronization

With the retained Jacobi normalization and $A=2m-1$,



$$
\boxed{
m\equiv851\pmod{6561}
\Longrightarrow
r:=\operatorname{cont}_3(J_m)
=
u:=\operatorname{cont}_3(J_{m-1}).
}
\tag{2.3}
$$



**Proof.** The exact state-cost vectors coincide after eight digits. Every subsequent transition and every admissible termination is identical by (2.2). The terminal minima therefore coincide. ∎

The 81 complete auxiliary checks and 3280 middle-word checks corroborate their finite scopes. Neither is needed to extrapolate (2.3).

---

## 3. Constructive upper content: state and carry audit

The proposed policy is valid. The useful invariant should be made explicit.

Above the fixed resonance suffix, let

- $d\in\{0,1,2\}$ be the current degree digit;
- $p$ be the preceding degree digit, hence the current integral-upper digit;
- $q\in\{0,1\}$ be the carry generating the digits of $M-\tfrac12$;
- $b$ be the integral-binomial borrow.

The half-index digit and next half-carry are



$$
\begin{array}{c|ccc}
q&d=0&d=1&d=2\\ \hline
0&1,\ 0&2,\ 0&0,\ 1\\
1&2,\ 0&0,\ 1&1,\ 1.
\end{array}
\tag{3.1}
$$



In each entry the first component is the half-index digit and the second is the next $q$.

Choose $k_d$, with $r_d=d-k_d$, by



$$
\begin{array}{c|ccc}
q&d=0&d=1&d=2\\ \hline
0&0&0&2\\
1&0&1&1.
\end{array}
\tag{3.2}
$$



### 3.1 The invariant

At entry to the unknown middle block,



$$
(c,b,e,q)=(0,0,0,0),
$$


and the preceding degree digit is $0$ or $1$.

The following properties are preserved:

1. $c=e=0$.
2. If $q=0$, then $p\in\{0,1\}$ and $b=0$.
3. If $b=1$, then $q=1$ and $p=2$.
4. If $q=1$, then $p\ge1$.

For property 4, the transitions producing $q=1$ are exactly a preceding digit $2$ from $q=0$, or a preceding digit $1$ or $2$ from $q=1$.

### 3.2 No addition carry or half-binomial borrow is created

By construction,


$$
k_d+r_d=d,
$$


so $c$ remains zero.

Inspection of (3.1)–(3.2) shows that $r_d$ never exceeds the half-index digit. Thus the half-binomial borrow remains zero.

### 3.3 The only charge event

When $q=0,d=2$, one chooses $k_d=2$, while $p\le1$. This creates exactly one integral borrow.

In every other case:

- $q=0,d=0,1$: $k_d=0$, with no incoming borrow;
- $q=1,b=0$: $p\ge1$ and $k_d\le1$;
- $q=1,b=1$: $p=2$ and $k_d\le1$.

Hence no other digit creates a borrow. In particular, a charge is always cleared at the next digit.

After a charge, the next half-carry is $q=1$, so the immediately following digit cannot be another charge. Therefore charge positions are separated by at least two positions.

For a middle word of length $M_{\rm len}$,



$$
\boxed{\text{path cost}\le\left\lceil\frac{M_{\rm len}}2\right\rceil.}
\tag{3.3}
$$



### 3.4 The leading-one block and final tail

A following block of $25$ ones creates no further charge:

- with $q=0$, choose $k_d=0,r_d=1$;
- with $q=1$, choose $k_d=1,r_d=0$;
- an incoming borrow from a final middle digit $2$ is cleared immediately.

After the most significant degree digit, the integral upper index has the required shifted terminal digit. The first zero degree digit causes no new borrow and clears $q$ if necessary. Subsequent zero coefficient digits are admissible, while the half-index tail is all $1$.

Thus the terminal evaluator state is genuinely $000$, with finite coefficient indices. The four zeros used in the supplied certificate are safe; they are not concealing an infinite nonzero coefficient tail.

---

## 4. Exact-window overlap audit

The proposed formula


$$
M_{\rm len}=L-t-25
$$


requires disjoint fixed blocks. This must be proved rather than assumed.

For sufficiently large inputs in the retained window, $m$ has $L$ ternary digits and at least $25$ leading ones. Indeed,



$$
m=\frac{3^L-D+1}{2},
$$


and


$$
C_{16}>3^{25}.
$$



The resonance digits above position $4$ alternate $0,1$, with


$$
m_i=
\begin{cases}
1,&i\ge4\text{ even},\\
0,&i\ge5\text{ odd}.
\end{cases}
\tag{4.1}
$$



Put $p=L-25$, the lowest position in the leading-one block.

### 4.1 Overlap of two or more digits is impossible

For the sufficiently large domain, $p\ge5$. Two consecutive resonance digits in that range include a zero. They cannot both belong to an all-one prefix.

Thus at most one digit could overlap:


$$
t\le p+1.
$$



### 4.2 A one-digit overlap contradicts the exact window

Suppose $t=p+1$. Compatibility forces the overlapping digit $m_p$ to be $1$, hence $p$ is even and $m_{p-1}=0$.

Now the prefix and suffix cover all digits. Every digit except the units digit is $0$ or $1$, and the units digit is $2$. Comparing with the $L$-digit all-one integer gives



$$
D=3^L-2m+1
=
2\sum_{\substack{i\ge1\\m_i=0}}3^i.
$$



In particular,


$$
\frac D{3^L}\ge\frac2{3^{26}}.
$$



But


$$
\frac2{3^{26}}>\frac1{C_{16}},
$$


because


$$
2C_{16}>3^{26}
\iff
295936>177147.
$$



This contradicts the exact upper window bound.

Therefore



$$
\boxed{t\le L-25,\qquad M_{\rm len}=L-t-25\ge0.}
\tag{4.2}
$$



This closes the overlap obligation on the stated sufficiently large domain.

---

## 5. Consequence for the core inverse loss

For $t\ge8$,


$$
m\equiv247/8\equiv851\pmod{6561}.
$$


Theorem 2.1 gives $r=u$.

On the retained unit-normalized branch,


$$
v_3(b_m)=v_3(a_m)=1,\qquad v_3(\rho)=4,
\qquad \mathfrak a=a_m/3\in\mathbb Z_3^\times.
$$



Consequently


$$
r<4+u,
$$


so the accepted noncollision identity applies:



$$
\boxed{\operatorname{cont}_3(\mathcal E)=2r.}
\tag{5.1}
$$



The collision $r=4+u$ is impossible on this entire suffix cylinder. The seven-row collision certificate remains valid elsewhere, but is unnecessary here.

The constructive path gives



$$
r\le\left\lceil\frac{L-t-25}{2}\right\rceil.
$$



Retaining the exact factorial perturbation comparison and the original integral Schur correction,



$$
s_c=h-2-\operatorname{cont}_3(\mathcal E)
=L-1-2r.
$$



Hence



$$
\boxed{
s_c\ge t+24-\bigl((L-t-25)\bmod2\bigr)\ge t+23.
}
\tag{5.2}
$$



This also records the slightly stronger parity-sensitive bound.

### Scope of the conclusion

Equation (5.2) holds when all of the following hold simultaneously:

- the actual original index and exact $C_{16}$ window;
- $t\ge8$;
- the retained sufficiently large support, degree and saturation conditions;
- the actual unit-normalized Jacobi kernel;
- the integral corrected-column/Schur hypotheses.

It is not a blanket assertion about every real-window index merely because $v_3(A)=5$.

On that domain,



$$
\boxed{t\ge9\Longrightarrow s_c\ge32.}
\tag{5.3}
$$



---

## 6. What is excluded, and what remains directionally possible

The two perturbation comparisons have different depths and different roles.

### 6.1 The factorial comparison remains valid

At the original finite cutoff,



$$
G_c=G_J+3^hF_c,\qquad F_c\in M_{m+1}(\mathbb Z_3).
$$



Under the unit-normalized inverse formula,



$$
\lambda(G_J)\le h-2<h.
$$



Thus the factorial perturbation preserves inverse loss. The new lower bound for $s_c$ does not invalidate this comparison.

### 6.2 The depth-$32$ actual/core comparison is not protected

The retained actual comparison is



$$
S_{\rm act}-S_c\in3^{32}M_\nu(\mathbb Z_3).
$$



Its simple inverse-stability criterion requires $s_c<32$, which (5.3) excludes on the deep family.

Equivalently, with



$$
B_c=-S_c/3^{26},\qquad
\Theta=-S_{\rm act}/3^{26},
$$


the largest Smith exponent of $B_c$ is


$$
s_c-26\ge6.
$$



The previous directional guard derived under a largest-Smith-exponent hypothesis $<6$ cannot simply be reused after that hypothesis has failed.

This is a limitation of the comparison theorem. It does not establish the valuation, invertibility, or noninvertibility of the actual matrix.

### 6.3 A genuinely directional alternative

There is an exact scalar identity that does not require a global inverse-loss bound.

Assume the two actual matrices involved are nonsingular, and put



$$
\Delta=\Theta-B_c,\qquad
\delta e=e_{\rm act}-e_c,
$$




$$
v=B_c^{-1}e_c,\qquad
w=\Theta^{-1}e_{\rm act}.
$$



Then



$$
\boxed{
\begin{aligned}
&\left(e_{\rm act}^{T}\Theta^{-1}e_{\rm act}
       -3^{26}d_{\rm act}\right)
-\left(e_c^{T}B_c^{-1}e_c-3^{26}d_c\right)\\
&\qquad=
\delta e^{T}(v+w)
-v^{T}\Delta w
-3^{26}(d_{\rm act}-d_c).
\end{aligned}}
\tag{6.1}
$$



This follows by substituting


$$
B_cv=e_c,\qquad \Theta w=e_{\rm act}.
$$



A useful follow-on lemma would prove that the right side has valuation strictly greater than the core scalar’s valuation, using the **actual** $\Delta,\delta e,d_{\rm act}-d_c$, and would separately prove actual nonsingularity.

Alternatively, one can work directly with the complete cofactor pair



$$
D_0=\det\Theta,
$$




$$
\boxed{
D_1=e_{\rm act}^{T}\operatorname{adj}(\Theta)e_{\rm act}
-3^{26}d_{\rm act}\det\Theta.
}
\tag{6.2}
$$



The subtraction in $D_1$ remains essential.

---

## 7. Matveev closes the quantitative exact-window intersection

### 7.1 The specialization meets the theorem’s hypotheses

Let


$$
\alpha=\log_3 4.
$$


For $q\ge1$, choose an integer $p$ nearest to $q\alpha$. Then



$$
\Lambda=q\log4-p\log3.
$$



The relevant checks are:

- $4,3$ are positive rational algebraic numbers;
- the number field is $\mathbb Q$, so $D=1$;
- their logarithmic heights are $\log4,\log3$;
- these also dominate the usual fixed lower floors in the height parameters;
- the coefficients $q,-p$ are integers;
- $|p|\le2q$;
- $\Lambda\ne0$, since $4^q=3^p$ is impossible by unique prime factorization.

Thus the supplied primary Corollary 2.3 text applies.

At two fixed rational numbers and $D=1$, its logarithmic dependence on the coefficient bound yields



$$
|\Lambda|\ge c_0q^{-K}
$$


with effective constants. The proposed $K=10^{12}$ is deliberately much larger than the specialized two-number constant. For scale, the familiar explicit real two-number consequence with factor


$$
1.4\,30^5\,2^{4.5}\log4\log3
$$


is already below $2\cdot10^9$; harmless fixed conversion factors do not threaten the proposed exponent.

If a formulation is made for $4^q3^{-p}-1$, nearest-integer choice gives bounded $|\Lambda|$, so comparison with $e^\Lambda-1$ changes only the effective constant.

Therefore



$$
\boxed{\|q\alpha\|\ge c q^{-K}\qquad(q\ge1)}
\tag{7.1}
$$


is now an established input at the supplied primary-text scope.

I do not claim a new visual inspection of the PDF. That is not needed to convert the supplied successful primary-text reading into “no primary theorem available.”

### 7.2 Exact resonance gives an actual arithmetic progression

Since


$$
\operatorname{ord}_{3^s}(4)=3^{s-1},
$$


the condition


$$
v_3(4^{j+1}-247)=t
$$


can be enforced by choosing one of the two nonextending lifts modulo $3^t$ of the unique solution modulo $3^{t-1}$.

Thus exact resonance is preserved on a progression


$$
j=a_t+3^t k.
\tag{7.2}
$$



For $t\ge6$, reduction modulo $729$, using


$$
4^{82}\equiv247\pmod{729},
$$


gives


$$
j\equiv81\pmod{243}.
$$


In particular $v_3(j)=4$, as required by the retained construction.

### 7.3 A fixed interval gives the exact $C_{16}$ window

Choose fixed numbers


$$
\frac1{2C_{16}}<d_1<d_2<\frac1{C_{16}}.
$$



For example, one can take


$$
d_1=\frac5{8C_{16}},\qquad d_2=\frac7{8C_{16}}.
$$



Choose $j$ so that the fractional part of $j\alpha$ lies in the fixed interval



$$
I=
\left(
1+\log_3(1-d_2),\
1+\log_3(1-d_1)
\right).
$$



With $L=\lceil j\alpha\rceil$,



$$
1-3^{j\alpha-L}\in(d_1,d_2).
$$



The actual window quantity is



$$
\frac D{3^L}
=
1-3^{j\alpha-L}+3^{-L}.
$$



For sufficiently large $L$, the final $3^{-L}$ lies within the fixed margins. Therefore the original, not an asymptotically substituted, window holds.

### 7.4 Quantitative hitting along the progression

Put $T=3^t$ and $\beta=T\alpha$. Let $w=|I|>0$, fixed independently of $t$.

Choose a fixed integer $Q$ large enough that $1/Q<w/4$. Dirichlet approximation supplies $1\le q\le Q$ with



$$
0<\delta:=\|q\beta\|\le1/Q.
$$



The lower bound (7.1), applied to $qT$, gives



$$
\delta\ge c(qT)^{-K}\ge c(QT)^{-K}.
$$



Successive steps of size $\delta$, in the appropriate orientation on the circle, hit any interval of length $w$ within $O(1/\delta)$ steps. Starting from any fixed point of the progression, this produces



$$
j=O(T^{K+1}).
$$



One may start at a representative at least $T$, ensuring that the resulting indices grow with $t$. Hence



$$
\boxed{\log(j+1)=O(t).}
\tag{7.3}
$$



All constants are effective, though very large.

### Conclusion of the intersection audit

The formerly conditional real-logarithm input is closed. The exact-resonance progression, exact window, original congruence, and quantitative growth condition can be imposed simultaneously.

The retained moving-base theorem then applies at its already established scope, giving the actual polar continuation and unit normalizer for all sufficiently large members of this constructed family.

No endpoint-unit digit restriction is being imposed. No restricted-digit infinitude theorem for powers of $2$ is needed.

Thus the new inverse-comparison exclusion holds on an **unconditional infinite subfamily of original indices**, after the retained sufficiently large threshold.

---

## 8. Audit of A3’s all-prime coefficient theorem

A3’s fixed-seed argument is correct.

Define


$$
a_k(n)=k![z^k]e^z\left(1-z+\frac{z^2}{2}\right)^n.
$$



The recurrence is



$$
a_{k+1}
=
(k+1-n)a_k
+\frac{k(2n-k-1)}2a_{k-1}
+\frac{k(k-1)}2a_{k-2},
\tag{8.1}
$$


with


$$
a_0=1,\qquad a_1=1-n,\qquad a_2=(n-1)^2.
$$



The transfer determinant is indeed $k(k-1)/2$. It is singular at some small-prime positions, so determinant support alone would not prove primitivity.

### 8.1 Congruence in $n$

The expansion through $(n)_m u(z)^m/m!$, with


$$
u(z)=-z+z^2/2,
$$


has integral exponential coefficients. Consequently



$$
a_k(n)\in\mathbb Z[n].
$$



Thus


$$
n'\equiv n\pmod N
\Longrightarrow
a_k(n')\equiv a_k(n)\pmod N,
$$


and, in particular,


$$
p^s\mid n\Longrightarrow a_k(n)\equiv1\pmod{p^s}.
$$



This genuinely uses the fixed exponential seed.

### 8.2 Odd-prime index periods

For fixed nonnegative $n$,



$$
a_k(n)=\sum_{r=0}^{2n}q_r(n)(k)_r,
\qquad q_r(n)\in\mathbb Z[1/2].
$$



Hence, for odd $p$,



$$
k'\equiv k\pmod{p^s}
\Longrightarrow
a_{k'}(n)\equiv a_k(n)\pmod{p^s}.
$$



This is valid even when reducing a large coefficient index to a small residue.

### 8.3 The $2$-adic period proof is valid

For


$$
b_r=r![z^r]q(z)^n,
$$


the denominator bound gives



$$
v_2(b_r)\ge
\sum_{\nu\ge2}\left\lfloor\frac r{2^\nu}\right\rfloor.
$$



The quantities $Q_r(k)$ in A3 are integral binomial combinations of later $b_j$, so the same lower bound at $r$ applies.

For $M=2^{s+1}$,



$$
a_{k+M}-a_k
=
\sum_{r=1}^{M}\binom Mr Q_r(k),
$$


and


$$
v_2\binom Mr=s+1-v_2(r)
$$


holds throughout $1\le r\le M$, including $r=M$.

The inequality


$$
\sum_{\nu\ge2}\left\lfloor\frac r{2^\nu}\right\rfloor
\ge v_2(r)-1
$$


therefore proves



$$
\boxed{a_{k+2^{s+1}}(n)\equiv a_k(n)\pmod{2^s}.}
\tag{8.2}
$$



No unjustified $2$-adic division occurs.

### 8.4 Singular transfer positions are avoided, not inverted

For odd $p$, reduce three consecutive indices modulo $p$.

- If the triple passes through residue $0$, one entry is $a_0=1$.
- Otherwise it lies inside $1,\ldots,p-1$. Backward recurrence uses coefficients
  

$$
r(r+1)/2,
$$


  all units until reaching $a_0$.

The singular positions $k\equiv0,1\pmod p$ are never crossed by an illicit inverse.

At $2$, the parity pattern is:

- all entries odd if $n$ is even;
- $1,0,0,1$, periodically, if $n$ is odd.

Every consecutive triple contains a unit at every prime. Hence



$$
\boxed{
\gcd(a_k(n),a_{k+1}(n),a_{k+2}(n))=1
}
\tag{8.3}
$$


for all $n,k\ge0$.

---

## 9. Audit of the moment and common-defect contents

Put


$$
x=a_{n-1}(n),\quad y=a_n(n),\quad z=a_{n+1}(n).
$$



For $n\ge1$,



$$
(n+1)!(b,c,d)
=
\bigl(n(n+1)x,(n+1)y,z\bigr).
$$



A3 correctly excludes all possible odd common primes:

- $p\mid n$: $z\equiv1\pmod p$;
- $p\mid n+1$: index periodicity gives $z\equiv a_0(n)=1\pmod p$.

The parity analysis then gives exactly



$$
\gcd\bigl(n(n+1)x,(n+1)y,z\bigr)
=
\varepsilon_n.
$$



Therefore, with the original clearer,



$$
\boxed{
\gcd(D_{\rm mom}b,D_{\rm mom}c,D_{\rm mom}d)
=
2^n(n+2)\varepsilon_n.
}
\tag{9.1}
$$



Now retain



$$
\begin{aligned}
h&=n(n+1)x+(n+1)(n-3)y-2(n-1)z,\\
b_0&=6z-(n+1)(n+6)y,\\
b_3&=2(n+2)z-(n+1)(n+3)y,
\end{aligned}
$$


and


$$
P_n=n^2+5n+3.
$$



The identities


$$
\det=-2n(n+1)^2P_n,
$$




$$
(n+2)b_0-3b_3=-(n+1)P_ny
\tag{9.2}
$$


are correct.

For odd $n$ divisible by $3$, the proof of



$$
\boxed{
\gcd(|h|,|b_0|,|b_3|)
=
2W_n,\qquad
W_n=\gcd(|h|,|b_0|,P_n),\quad 3\nmid W_n
}
\tag{9.3}
$$


is also correct.

The key multiplicity step is sound: at an odd common prime outside $3n(n+1)$, primitivity forces $y$ to be a unit. Equation (9.2) then controls the full prime-power depth of $P_n$, not just its support. The converse uses that $3$ is a unit there.

At $2$, A3’s two cases give exactly one common factor of $2$, while $P_n$ is odd.

Thus the all-prime normalized-defect law is accepted as a proof, not merely finite corroboration.

---

## 10. Two sharper consequences for common denominator structure

### 10.1 The prime $13$ is also excluded

The discriminant identity is



$$
(2n+5)^2=4P_n+13.
\tag{10.1}
$$



If $13\mid P_n$, then


$$
n\equiv4\pmod{13}.
$$



Using congruence in $n$ and odd-prime index periodicity,



$$
(x,y,z)
\equiv
\bigl(a_3(4),a_4(4),a_5(4)\bigr)
\pmod{13}.
$$



The fixed recurrence gives exactly



$$
a_0(4)=1,\quad a_1(4)=-3,\quad a_2(4)=9,
$$




$$
a_3(4)=-23,\quad a_4(4)=45,\quad a_5(4)=-39.
$$



Substitution in $h$ at $n=4$ yields



$$
20(-23)+5(45)-6(-39)=-1.
$$



Hence $h\equiv-1\pmod{13}$, and



$$
\boxed{13\nmid W_n.}
\tag{10.2}
$$



This is a fixed finite calculation embedded in a universal congruence proof. It is not an original-index producer computation.

Moreover, every prime $p\mid W_n$ is odd, is different from $3,13$, and satisfies



$$
\boxed{\left(\frac{13}{p}\right)=1.}
\tag{10.3}
$$



Indeed, (10.1) makes $13$ a nonzero square modulo $p$.

### 10.2 The common large-prime factor is at most one prime

On both original endpoint families, $9\mid n$, so



$$
v_3(P_n)=1.
$$



Since $3\nmid W_n$,



$$
W_n\mid P_n/3.
$$



Retain the accepted exact common structural factor



$$
V_n=(W_n)_{>n+2}
=
\gcd(\gamma_0,\gamma_3)_{>n+2}.
$$



Two primes above $n+2$, counted with multiplicity, have product greater than $(n+2)^2$, whereas



$$
P_n/3<(n+2)^2.
$$



Therefore



$$
\boxed{
V_n=1
\quad\text{or}\quad
V_n=p
}
\tag{10.4}
$$


for one prime $p>n+2$, occurring to exponent $1$.

Such a prime also satisfies (10.3).

By the retained actual-denominator comparison, $V_n$ divides both actual large-prime endpoint denominators. Thus, writing



$$
d_0=V_n d_0',\qquad d_3=V_n d_3',
$$


one has the exact cancellation



$$
\boxed{
\frac{d_0d_3}{\gcd(d_0,d_3)^2}
=
\frac{d_0'd_3'}{\gcd(d_0',d_3')^2}.
}
\tag{10.5}
$$



This is useful: the shared structural factor is completely harmless for imbalance and has at most one large prime. It does not bound either individual structural content, and it does not evaluate the force-content gcd.

---

## 11. Projected minors: the obstruction remains real

A3 correctly distinguishes full-state primitivity from projected-pair primitivity.

The three actual terminal forms are



$$
\Theta=\mu_1+n\mu_0,
$$




$$
\Theta_0=\mu_2+(n+2)\mu_1+n\mu_0,
$$




$$
\Theta_3=\mu_1-(n+2)\mu_0.
$$



At $p>n+2$, the transformation


$$
\mu\longmapsto(\Theta,\Theta_0,\Theta_3)
$$


has determinant $-2(n+1)$, a unit. Therefore



$$
\boxed{
\min\{v_p(\Theta),v_p(\Theta_0),v_p(\Theta_3)\}
=
\min_i v_p(\mu_i).
}
\tag{11.1}
$$



This supplies a useful joint statement:

> If the full actual minor vector is primitive at $p>n+2$, the two endpoint projection pairs cannot both have positive common $p$-content.

But either one can. The two individual kernels remain



$$
\mu\equiv\mu_0(1,-n,n(n+1))
$$


and


$$
\mu\equiv(0,0,\mu_2),
$$


respectively.

Under the retained unit clearing identifications, (11.1) also identifies the common part of the two complete projected gcds with the corresponding full-minor content, together with both actual $X_j^\circ$-conditions. It does not bound either individual projected gcd.

Thus a determinant-only exterior argument is still insufficient. The required follow-on theorem is a **fixed-seed terminal-line avoidance or intersection-depth estimate**, using the complete force and the actual $X_j^\circ$-conditions.

Neither moment primitivity nor the new single-prime statement for $V_n$ supplies that theorem.

---

## 12. New binary simplification: 251 common moments instead of a matrix kernel

The accepted single-denominator identity is retained without rerunning its source or jets.

Set



$$
d=125,\qquad B=2n,
$$


so


$$
\widehat F=\frac{V_f}{(1-z)^{B+d}},
\qquad
\widehat E=\frac{V_e}{(1-z)^{B+d}}
\pmod{2^{20}}.
$$



The following exact change of numerator basis gives a new target-specific contraction.

### 12.1 An integral Bernstein change of basis

For any polynomial $V$ of degree at most $d$, write



$$
V(z)=\sum_{r=0}^{d}c_r z^r(1-z)^{d-r}.
\tag{12.1}
$$



If $V(z)=\sum_i v_i z^i$, then



$$
\boxed{
c_r=\sum_{i=0}^{r}v_i\binom{d-i}{r-i}.
}
\tag{12.2}
$$



This is an integral unimodular basis change.

Consequently,



$$
\frac{V(z)}{(1-z)^{B+d}}
=
\sum_{r=0}^{d}
c_r\frac{z^r}{(1-z)^{B+r}}.
$$



For every $k\ge0$,



$$
[z^k]\frac{z^r}{(1-z)^{B+r}}
=
\binom{B+k-1}{k-r}.
$$



Put



$$
U(k)=\binom{B+k-1}{k},
\qquad
D_B=B(B+1)\cdots(B+d-1).
$$



The exact identity



$$
\binom{B+k-1}{k-r}
=
U(k)\frac{(k)_r}{B(B+1)\cdots(B+r-1)}
$$


holds also for $k<r$, with $(k)_r=0$.

Define the integer polynomial



$$
\boxed{
P_V(k)=
\sum_{r=0}^{d}
c_r(k)_r(B+r)^{\overline{d-r}}.
}
\tag{12.3}
$$



Then



$$
\boxed{
[z^k]\frac{V(z)}{(1-z)^{B+d}}
=
\frac{U(k)P_V(k)}{D_B}.
}
\tag{12.4}
$$



No $k$-dependent modular denominator has been introduced.

### 12.2 The original finite Gram pair

Keep the original row set $\mathcal I_{\rm orig}$ and original weights $\omega_k$, without extending or shortening them.

Let


$$
P_f=P_{V_f},\qquad P_e=P_{V_e}.
$$



Define the 251 common moments



$$
\boxed{
M_\ell=
\sum_{k\in\mathcal I_{\rm orig}}
\omega_k^2\,U(k)^2\,k^\ell,
\qquad 0\le\ell\le250.
}
\tag{12.5}
$$



Write


$$
P_f(k)^2=\sum_{\ell=0}^{250}A_\ell k^\ell,
\qquad
P_f(k)P_e(k)=\sum_{\ell=0}^{250}B_\ell k^\ell.
$$



Then, exactly,



$$
\boxed{
\langle\widehat F,\widehat F\rangle
=
D_B^{-2}\sum_{\ell=0}^{250}A_\ell M_\ell,
}
\tag{12.6}
$$




$$
\boxed{
\langle\widehat F,\widehat E\rangle
=
D_B^{-2}\sum_{\ell=0}^{250}B_\ell M_\ell.
}
\tag{12.7}
$$



This replaces the two contractions against a $126\times126$ kernel by two contractions against the same 251-entry moment vector.

It is an exact target reduction, not a claim that the original weighted sums have been evaluated.

### 12.3 The denominator loss is exactly $254$ bits after squaring

For the accepted input,



$$
B=2n=1201357460917180964484.
$$



Here


$$
B\equiv132\pmod{256},
$$


and


$$
\frac{B+124}{256}=4692802581707738143
$$


is odd.

Among $B,\ldots,B+124$, the counts divisible by


$$
2,4,8,16,32,64,128,256
$$


are respectively


$$
63,32,16,8,4,2,1,1,
$$


with no contribution from higher powers of $2$.

Therefore



$$
\boxed{v_2(D_B)=127,\qquad v_2(D_B^2)=254.}
\tag{12.8}
$$



For $2$-integral original squared weights, a straightforward division-free implementation may compute the moments and numerator contractions modulo $2^{274}$, divide the guaranteed factor $2^{254}$, and invert only the odd part of $D_B^2$.

The original numerator arrays are needed only modulo $2^{20}$: choose fixed integer lifts and apply the exact identity to those lifts. Different lifts change the original coefficient sequences, and hence the integral weighted contractions, by multiples of $2^{20}$. No new higher-precision column identity is being assumed.

If the actual metric has a nonunit weight denominator, its actual common clearer must be retained and its valuation added to this precision budget. The complete weight formula and row endpoints are not reproduced in the present packet, so I do not silently declare such a clearer to be $1$.

### Limitation

The polynomial transformations and the final 251-term contractions are small. A feasible producer for all the moments (12.5), at the original cutoff and with the original weights, is still missing.

This reduction does not identify the metric with a full Hahn measure, does not pass through singular recurrences by modular division, and does not establish a small automatic-state module.

---

## 13. Finite boundaries, complete forcing, and normalization remain unchanged

None of the new arguments alters the original Jacobi finite basis



$$
U_u=(y-1)^u,\quad 0\le u<D,
$$




$$
z_i=(y-1)^Dy^i,\quad0\le i<\nu,
$$




$$
Y_b=y^b,\quad d\le b\le m,
$$


where


$$
d=\frac{3D}{2}-1,\qquad \nu=\frac D2-1.
$$



Both corrected-column representatives remain required. Core-corrected columns are not substituted for actual-corrected columns in the endpoint scalar.

The complete functional remains



$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\sum_{\substack{v\ge0\\2v+1\le4n-3}}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1}.
$$



Both leading extractions, every permitted lower pole, the factorial force, and the LOW subtraction remain. The terminal range remains



$$
\mu_{i+\nu}^{\langle26\rangle}
+\sum_{k=0}^{\nu-1}f_k\mu_{i+k}^{\langle26\rangle}
=b_i^{\langle26\rangle},
\qquad0\le i\le\nu-2,
$$


and



$$
J^T\varepsilon+\omega
=
-\varepsilon-s\bigl(\theta e_{\nu-1}
+3^{26}b^{\langle26\rangle}\bigr).
$$



There is no added moment beyond $D-4$, and $\omega_{\nu-1}$ is not deleted.

For the endpoint construction, retain the original $3\times3$ contact matrix, both four-coordinate reconstructed columns, complete force through exactly $2n+2$, fixed exponential boundary, terminal return, exterior $+1$, and least clearer over all eight entries.

The accepted $n=225$ row contents remain



$$
(508500,\ 28350,\ 15525,\ 772).
$$



The pending $n=3375$ calculation remains pending.

---

## 14. Actual primitive denominators and same-index whole errors

### 14.1 Jacobi determinant construction

After restoring all actual row contents, multiplier factors and clearers, retain



$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$




$$
g_\ell=\gcd(|A_\ell|,|B_\ell|)
$$


over all primes.

For $B_\ell\ne0$,



$$
q=\frac{|B_\ell|}{g_\ell},
\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$



The whole same-index error is



$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{g_\ell}
\det H_{\rm complete}.
}
\tag{14.1}
$$



The new lower bound for $s_c$ does not evaluate this pair or its final gcd.

### 14.2 Endpoint-weight construction

The endpoint denominator remains



$$
d_j=
\frac{|\gamma_jX_j|}
{\gcd(|\gamma_jX_j|,|V_j|)}.
$$



For a reduced weight $\lambda=a/k$, retain



$$
J_{\rm wt}=B\widetilde v_0-A\widetilde v_3,
$$




$$
T_{\rm wt}=aJ_{\rm wt}+kA\widetilde v_3,
$$




$$
F_{\rm gcd}
=\gcd(|A|,|a|)\gcd(|B|,|a-k|),
$$




$$
G=\gcd(k,|J_{\rm wt}|),
$$




$$
H_{\rm gcd}
=
\gcd\!\left(h,\frac{|T_{\rm wt}|}{F_{\rm gcd}G}\right).
$$



The actual primitive pair is still



$$
\boxed{
q_\lambda=
\frac{kh|AB|}{F_{\rm gcd}GH_{\rm gcd}},
\qquad
p_\lambda=
\operatorname{sgn}(AB)
\frac{T_{\rm wt}}{F_{\rm gcd}GH_{\rm gcd}}.
}
\tag{14.2}
$$



Its complete error is



$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda e_3\alpha_{n,2}
(\lambda-\Lambda_{n,2}).
}
\tag{14.3}
$$



The required irrationality condition remains an infinite sequence with



$$
0<
q_\lambda|e_3\alpha_{n,2}|
\,|\lambda-\Lambda_{n,2}|
\longrightarrow0.
$$



Neither the all-prime moment theorem nor the binary contraction reduction establishes this.

---

## 15. New bounded work: inputs and verifiable outputs

No accepted calculation should be rerun.

### 15.1 No further suffix computation is needed

The supplied eight-digit vector, together with the exact common-stream argument and the invariant proof above, closes the universal suffix theorem.

The supplied 3280-word calculation already corroborates its stated finite policy scope. Repeating it would add no proof.

### 15.2 New small binary post-processing

A genuinely new bounded calculation can use the accepted degree-$125$ arrays directly.

**Inputs**

- the accepted $V_f,V_e$ arrays modulo $2^{20}$;
- the exact integer $B=2n$;
- $d=125$.

**Operations**

1. Apply (12.2) to obtain the two Bernstein-coordinate vectors.
2. Form the two integer polynomials $P_f,P_e$ by (12.3).
3. Form the coefficient vectors of $P_f^2$ and $P_fP_e$.
4. Reduce these data modulo $2^{274}$, using fixed integer lifts.
5. Record the odd part of $D_B$, with the exact valuation $127$.

**Expected verifiable output**

- two 126-entry transformed numerator vectors;
- two degree-at-most-$125$ polynomials;
- two 251-entry contraction vectors;
- exact algebraic residual zero in (12.1) and (12.3);
- the denominator valuation certificate (12.8).

This requires only bounded polynomial arithmetic—comfortably fewer than a million elementary coefficient operations. It does not regenerate the source, jets, Schur correction, or force.

### 15.3 The remaining weighted computation

To evaluate the Gram pair, the additional inputs must be the **actual** finite row endpoints, exact weights and any actual weight clearer.

The required output is the moment vector (12.5) at sufficient precision, a boundary certificate, and the two residues from (12.6)–(12.7).

A zero residue would establish only a lower valuation bound. A nonzero residue would establish the valuation within the retained precision.

No feasible uniformly bounded producer for that moment vector is proved here. That part remains an unevaluated specification.

---

## 16. Proof-status ledger and conclusion

| Claim | Status |
|---|---|
| Eight-digit state vector at $m\equiv851\pmod{6561}$ | Accepted exact finite certificate |
| Equality of all remaining streams and terminal conditions | Proved algebraically |
| Universal $r=u$ on that residue class | Proved |
| Constructive policy and charge separation | Proved by invariant |
| No prefix/suffix overlap on the sufficiently large exact window | Proved |
| $\operatorname{cont}_3(\mathcal E)=2r$ on the actual unit-normalized deep family | Proved |
| $s_c\ge t+23$, hence exclusion of $s_c<32$ for $t\ge9$ there | Proved |
| Quantitative exact-window intersection | Closed using the supplied primary Matveev text |
| Actual directional scalar or full cofactor valuation | Unresolved |
| A3 all-prime coefficient primitivity | Correct proof |
| A3 $2$-adic and odd-prime-power periods | Correct proofs |
| A3 common normalized-defect law | Correct proof |
| $13\nmid W_n$ | New proof |
| $V_n$ is $1$ or one large prime to exponent $1$ on original endpoint families | New proof |
| Individual projected endpoint-pair primitivity | Not implied; obstruction remains |
| Binary reduction to 251 common finite moments | New exact algebraic reduction |
| Original weighted moment vector and Gram pair | Not evaluated |
| Actual all-prime denominator versus same-index whole error | Unresolved |
| Irrationality or rationality of $e+\pi$ | Unresolved |

### New result and exact bottleneck

The local Jacobi target is now substantially closed:



$$
\boxed{
r=u,\qquad
\operatorname{cont}_3(\mathcal E)=2r,\qquad
s_c\ge t+23
}
$$



on the actual unit-normalized deep family in the exact $C_{16}$ window. The family can be reached unconditionally with the quantitative growth required by the retained continuation theorem.

The consequence is an **exclusion of one uniform inverse-transfer method**, not an irrationality result.

The remaining mathematical bottlenecks are now:

1. **Jacobi route:** control the actual directional scalar or complete cofactor pair despite the failed global inverse threshold, retaining both corrected columns and the complete forcing and terminal terms.
2. **Endpoint route:** bound the fixed seed’s prime-power intersections with the endpoint projection lines, together with the actual $X_j^\circ$-conditions and small-prime endpoint normalization.
3. **Binary route:** produce the original finite weighted moment vector in (12.5), or an equivalent rigorously bounded practical contraction, without changing the metric or boundary.
4. **Global conclusion:** compare the actual all-prime primitive denominator with the nonzero same-index whole error along an infinite sequence.



$$
\boxed{\text{No unconditional proof or disproof of the irrationality of }e+\pi
\text{ has been obtained.}}
$$


