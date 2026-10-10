> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1 continuation report: quantitative reachability is proved; the uniform $3$-adic logarithm input remains a precise dependency

## 1. Outcome and proof status

The rotation/progression step can be completed rigorously on the **original index domain**. More precisely, the fixed real-logarithm estimate available from the retained Matveev audit implies the following:

> For every sufficiently large prescribed resonance depth $t$, either exact-resonance progression contains an index $j_t$ in the required real window, with
> 

$$
> 3^t\le j_t\le C_0\,3^{(K+1)t}.
>
$$


> Consequently,
> 

$$
> v_3(4^{j_t+1}-247)=t,\qquad v_3(j_t)=4,\qquad
> \log(j_t+1)=O(t).
>
$$



Thus density is no longer the obstruction. The family has exact, increasing resonance depth, and the size bound is quantitative.

I also prove the proposed nested-residue estimate, in the slightly sharper form


$$
\boxed{\;
v_3(R_{b,u}(A))
\ge u+t-\max\!\left\{\lfloor\log_3u\rfloor,\,
\max_{0\le i<u}v_3(4A+1+4b-2i)\right\}.
\;}
\tag{1.1}
$$


All indices and denominator factors in this estimate are the actual finite ones.

For the $3$-adic logarithm step:

* the nonunit cases, the multiplicatively dependent cases, and nonvanishing of the actual differences are settled below;
* the multiplicatively independent case still requires an accurately sourced theorem with **uniform dependence on the moving integer $B$**;
* the packet does not contain a verified statement sufficient to certify that dependence, and I cannot safely reconstruct the precise Bugeaud–Laurent or Yu statement and all its hypotheses from the supplied material.

I therefore state that dependency explicitly rather than treat the proposed simplified bound as proved.

**Conditional on that one uniform logarithm estimate**, the later-denominator block vanishes modulo $3^{143}$ on the quantitative family just constructed. This is stronger than the required precision $3^{V_b+1}$. It gives the corrected Jacobi value laws and, using the retained grouped-residue digits, the quotient units


$$
\boxed{
v_3(a_m)=1,\quad \frac{a_m}{3}\equiv25\pmod{27};
\qquad
v_3(a_{m+1})=-2,\quad 9a_{m+1}\equiv5\pmod{27}.
}
\tag{1.2}
$$



These are statements about the exact Jacobi core, not about the complete matrix. I give an exact reduction of the terminal Wronskian, including its known scalar unit. Its valuation and the required original-coordinate precision losses remain unproved. No conclusion about irrationality of $e+\pi$ follows.

No external computation or literature retrieval was executed for this report. The supplied finite grouped-residue certificate is reused only at its stated scope.

---

## 2. Retained finite objects and precision

Throughout, preserve


$$
A=4^j-1,\qquad n=A+2,\qquad
h=\left\lfloor\log_3(4n-3)\right\rfloor,\qquad H=3^{h-1},
$$


with


$$
j>0,\qquad81\mid j,\qquad 0<H-A<H/972.
\tag{2.1}
$$


Also preserve


$$
m=\frac{A+1}{2},\qquad s=m+b,\qquad b\in\{0,1,2\},
$$




$$
\epsilon=4A-243=4^{j+1}-247,\qquad t=v_3(\epsilon),
$$




$$
I_b=122+2b,\qquad U_b=I_b+1,\qquad r_0=\frac{A+71}{3}.
$$



The exact finite decomposition is


$$
T_b(A):=r_0^{-s}p_s(r_0)
=N_b(A)+\epsilon^{-1}S_b(A),
\tag{2.2}
$$


where


$$
N_b(A)=\sum_{u=0}^{I_b}E_{b,u}(A),
\qquad
S_b(A)=\sum_{u=U_b}^{s}R_{b,u}(A).
$$


In particular, the actual upper boundary remains $s=m+b$.

The retained certificate concerns the grouped residue at $A_*=243/4$:


$$
\mathcal R_b=\sum_{u=U_b}^{\infty}R^*_{b,u}.
$$


Its stated outputs are


$$
\begin{array}{c|ccc}
b&0&1&2\\ \hline
V_b=v_3(\mathcal R_b)&133&135&134\\
3^{-V_b}\mathcal R_b\bmod27&2&22&16.
\end{array}
\tag{2.3}
$$


The proved residue-tail bound gives


$$
\mathcal R_b\equiv\sum_{u=U_b}^{280}R^*_{b,u}\pmod{3^{143}}.
$$



For $t\ge150$, the retained moving-degree arguments establish:

1. fixed-part transfer modulo $3^{143}$;
2. $v_3(\epsilon N_b(A))\ge t-5$;
3. $R_{b,u}(A)\in3^{143}\mathbb Z_3$ for
   

$$
281\le u\le\min(s,I_b+3^t);
$$


4. $R_{b,u}(A)\in3^{t+1}\mathbb Z_3$ for
   

$$
2h\le u\le s.
$$



Consequently, writing


$$
B_b(A)=
\sum_{u=I_b+3^t+1}^{\min(s,\,2h-1)}R_{b,u}(A),
\tag{2.4}
$$


with an empty sum equal to zero, those results actually give


$$
\boxed{
\epsilon T_b(A)-\mathcal R_b
\equiv B_b(A)\pmod{3^{143}}.
}
\tag{2.5}
$$


This follows because $t-5\ge145$ and $t+1\ge151$. It retains the nonresonant sum, rather than silently dropping it.

The outstanding block is therefore exactly (2.4).

---

## 3. The proposed $3$-adic logarithm estimate: what is verified and what is not

### 3.1 The moving integer and actual nonzero difference

Put $J=j+1$. Every denominator factor is


$$
D_{b,i}=4A+1+4b-2i=4^J-B_{b,i},
\qquad
B_{b,i}=2i+3-4b.
\tag{3.1}
$$



There is a direct, unconditional nonvanishing check on the **whole actual finite range**. If $0\le i<u\le s$, then $i\le s-1$, so


$$
\begin{aligned}
D_{b,i}
&\ge 4A+1+4b-2(s-1)\\
&=3A+2+2b>0.
\end{aligned}
\tag{3.2}
$$


Thus no actual denominator is zero. In particular, the exceptional equality $B=4^J$, for which a logarithm-difference bound would be meaningless, never occurs.

For the intermediate block we also have a useful size bound. Since


$$
4n-3=4^J+1<9^J,
$$


we have $h<2J$. For $i<u\le2h-1$,


$$
B_{b,i}\le2u+1\le4h-1<8J.
\tag{3.3}
$$


Positive $B$'s therefore move in a range of size $O(J)$, and individually satisfy $B\le2u+1$.

### 3.2 Nonunits and residue classes not equal to $1$

Because $4^J\equiv1\pmod3$, whenever


$$
B\not\equiv1\pmod3
$$


one has


$$
v_3(4^J-B)=0.
\tag{3.4}
$$


This includes every $B$ divisible by $3$.

Only positive $B\equiv1\pmod3$, together with a few explicitly bounded initial negative values, require further attention.

### 3.3 Multiplicative dependence is elementary here

Suppose $B>0$ and $4,B$ are multiplicatively dependent. Prime factorization shows that


$$
B=2^r,\qquad r\ge0.
$$


If $r$ is odd, then $B\equiv2\pmod3$, and (3.4) applies. If $r=2d$, then $B=4^d$.

For $J\ne d$, LTE gives exactly


$$
\boxed{
v_3(4^J-4^d)=1+v_3(|J-d|).
}
\tag{3.5}
$$


This remains true whether $J>d$ or $d>J$, after factoring out the smaller power of $4$.

On the actual denominator range, (3.2) implies $d<J$, and hence


$$
v_3(4^J-B)\le1+\log_3J.
\tag{3.6}
$$


The case $B=1$ is included by $d=0$.

Even without the actual restriction $B<4^J$, (3.5) gives


$$
v_3(4^J-B)\le1+\log_3(J+d),
$$


which is more than sufficient for a bound of the proposed shape after increasing an absolute constant. Thus multiplicative dependence does not obstruct the desired uniform estimate.

### 3.4 The finitely many nonpositive $B$'s

The only nonpositive values occurring for $b=0,1,2$ are among


$$
-5,\ -3,\ -1.
$$


The latter two give valuation zero. The value $-5$, occurring at $b=2,i=0$, gives


$$
4^J+5=\epsilon+252.
$$


For $t\ge7$,


$$
v_3(\epsilon+252)=v_3(252)=2.
\tag{3.7}
$$


Thus these initial factors contribute only a fixed bound. They cannot be omitted from the denominator maximum, but they cause no difficulty.

### 3.5 The exact missing independent-case statement

Here is a sufficient statement, formulated without an unverified attribution.

> **Uniform $3$-adic two-logarithm statement $(\mathrm P_3)$.**  
> There exists an effective absolute constant $C_3>0$ such that, for every integer $J\ge1$ and every integer $B\ge2$ satisfying
> 

$$
> B\equiv1\pmod3,\qquad 4,B\text{ multiplicatively independent},
>
$$


> one has
> 

$$
> v_3(4^J-B)
> \le C_3(1+\log B)(1+\log J)^2.
> \tag{3.8}
>
$$



For this project, the restricted version with $B<8J$ would already suffice.

The data for a prospective classical application are completely explicit:

* number field: $\mathbb Q$, degree $1$;
* prime: $3$;
* algebraic numbers: $4$ and $B$;
* both are $3$-adic units in $1+3\mathbb Z_3$;
* logarithmic heights:
  

$$
h(4)=\log4,\qquad h(B)=\log B;
$$


* integer coefficients: $J$ and $-1$, with coefficient maximum $J$;
* nonzero logarithmic form:
  

$$
\Lambda_3=J\log_3^{\mathrm{pad}}4-\log_3^{\mathrm{pad}}B.
$$



The last point is not merely formal. On $1+3\mathbb Z_3$, the $3$-adic logarithm is injective and satisfies


$$
v_3(\log x)=v_3(x-1).
$$


Therefore


$$
\Lambda_3=\log_3^{\mathrm{pad}}(4^J/B)\ne0,
\qquad
v_3(\Lambda_3)=v_3(4^J-B).
\tag{3.9}
$$



What is missing is a verified theorem whose height and coefficient parameters imply (3.8) with a constant independent of $B$. A theorem for each fixed $B$, with a constant $C(B)$ of unspecified growth, is insufficient.

The retained Bugeaud–Laurent bibliographic reference, the Yamada determinant-parameter reference, and the additional discussion of Yu bounds identify relevant literature. They do not, as reproduced in this packet, supply the exact statement and parameter verification needed here. In particular, I do not replace their hypotheses by the publisher abstract or guess their numerical constants.

This is an **unclosed theorem-application obligation**, not a counterexample to (3.8). The rest of the continuation can be proved conditionally on precisely this statement.

A weaker source result would also suffice if it gave, with fixed exponents and a uniform effective constant,


$$
v_3(4^J-B)\le
C(1+\log B)^a(1+\log J)^d.
\tag{3.10}
$$


The argument below only needs a fixed polynomial loss in $t$.

---

## 4. Quantitative progression/window hitting

This part closes unconditionally, using the retained Matveev result at its stated scope.

### 4.1 The fixed real-logarithm lower bound

Set


$$
\alpha=\log_3 4.
$$


For $q\ge1$, let $a$ be a nearest integer to $q\alpha$. Then


$$
\Lambda=q\log4-a\log3
$$


is nonzero: otherwise $4^q=3^a$, contradicting unique factorization.

The two algebraic numbers and their real logarithms are fixed. The coefficient $a$ satisfies $|a|\le2q$. The audited Matveev corollary therefore supplies effective constants $c>0$, $K\ge1$, depending only on $3,4$, such that


$$
\boxed{\|q\alpha\|\ge c q^{-K}\qquad(q\ge1).}
\tag{4.1}
$$


Decrease $c$, if necessary, so that $c\le1/2$.

This application uses a nonzero real logarithmic form over $\mathbb Q$; there is no moving algebraic number in it.

### 4.2 A uniform hitting lemma

> **Lemma 4.1.**  
> Suppose an irrational $\alpha$ satisfies (4.1). Let $\mathcal I$ be any open interval on $\mathbb R/\mathbb Z$ of length $\ell\in(0,1)$, and put
> 

$$
> Q=\left\lceil\frac4\ell\right\rceil.
>
$$


> For every integer $M\ge1$ and every starting point $x$, there is an integer
> 

$$
> 0\le k<c^{-1}Q^K M^K
>
$$


> such that
> 

$$
> x+kM\alpha\pmod1\in\mathcal I.
>
$$



**Proof.** Let $\beta=M\alpha$, and choose the first continued-fraction convergent $p_n/q_n$ of $\beta$ whose denominator satisfies $q_n\ge Q$. Its predecessor satisfies


$$
1\le q_{n-1}<Q.
$$


The convergent inequality and (4.1) give


$$
c(Mq_{n-1})^{-K}
\le\|q_{n-1}\beta\|
<\frac1{q_n}.
$$


Hence


$$
q_n<c^{-1}M^Kq_{n-1}^K
<c^{-1}Q^KM^K.
\tag{4.2}
$$



Write $q=q_n$, $p=p_n$. For $0\le k<q$,


$$
\operatorname{dist}_{\mathbb R/\mathbb Z}
\left(k\beta,\frac{kp}{q}\right)
<\frac1{q_{n+1}}<\frac1q.
$$


Since $p$ and $q$ are coprime, the rational points $kp/q$ form the complete grid of spacing $1/q$. A point on that grid lies within $1/(2q)$ of the center of the translated interval $\mathcal I-x$. The corresponding orbit point is within


$$
\frac1{2q}+\frac1q=\frac3{2q}
\le\frac{3\ell}{8}<\frac\ell2
$$


of that center. It belongs to the open interval. Equation (4.2) gives the claimed bound. ∎

This proves a bound uniform in both the progression modulus and its starting residue.

### 4.3 Exact resonance progressions

For $t\ge6$, the congruence


$$
4^{j+1}\equiv247\pmod{3^t}
$$


defines one class of $j$ modulo $3^{t-1}$. This follows from the fact that $4$ generates $1+3\mathbb Z/3^t\mathbb Z$, with order $3^{t-1}$.

Among its three lifts modulo $3^t$, one lifts to congruence modulo $3^{t+1}$; the other two satisfy


$$
v_3(4^{j+1}-247)=t.
\tag{4.3}
$$


Thus exact depth $t$ consists of two progressions modulo


$$
M=3^t.
$$



For any member of either progression,


$$
A=\frac{243+\epsilon}{4},\qquad v_3(\epsilon)=t>5,
$$


so $v_3(A)=5$. LTE then yields


$$
5=v_3(4^j-1)=1+v_3(j),
$$


hence


$$
\boxed{v_3(j)=4.}
\tag{4.4}
$$


In particular, the original condition $81\mid j$ is preserved exactly.

### 4.4 The original real window, including its additive correction

Put


$$
\rho=-\log_3(1-1/972)>0,
$$


and fix, for example,


$$
\delta_1=\rho/3,\qquad \delta_2=2\rho/3.
$$


Use the circle interval


$$
\mathcal I=(1-\delta_2,\,1-\delta_1).
\tag{4.5}
$$



Choose either exact-depth residue $r_t$ modulo $M=3^t$, with $0\le r_t<M$, and start at


$$
j_{\mathrm{start}}=r_t+M.
$$


Lemma 4.1 gives $k\ge0$ with


$$
j_t=r_t+M+Mk
$$


such that $\{j_t\alpha\}\in\mathcal I$, and


$$
M\le j_t
<2M+c^{-1}Q^K M^{K+1}.
\tag{4.6}
$$



Write


$$
j_t\alpha=N-\delta,\qquad \delta_1<\delta<\delta_2.
$$


Then


$$
4^{j_t}=3^{N-\delta},\qquad
\frac{A}{3^N}=3^{-\delta}-3^{-N}.
\tag{4.7}
$$


The term $3^{-N}$ matters: it is the difference between $4^j$ and $A=4^j-1$.

Because


$$
3^{-\delta_2}>1-1/972,
$$


for all sufficiently large $N$, (4.7) gives


$$
1-1/972<\frac A{3^N}<1.
\tag{4.8}
$$


Moreover, for such $N$,


$$
3\cdot3^N<4A+5<9\cdot3^N.
$$


Thus the original definition of $h$ gives


$$
h=N+1,\qquad H=3^{h-1}=3^N,
$$


and (4.8) is precisely


$$
0<H-A<H/972.
$$



Since $j_t\ge3^t$, the required lower bound on $N$ holds for every sufficiently large $t$.

We have proved:

> **Theorem 4.2 — original-domain quantitative reachability.**  
> There are effective constants $C_0,C_1,C_2$ and an effective threshold $t_0$ such that, for each integer $t\ge t_0$, either exact-resonance progression contains an original-domain index $j_t$ satisfying
> 

$$
> 3^t\le j_t\le C_0\,3^{(K+1)t},
> \qquad
> \log(j_t+1)\le C_1+C_2t.
>
$$


> Its exact resonance depth is $t$, and $v_3(j_t)=4$.

These indices form a genuine infinite family. No narrowing or replacement of the original real window has been made; the fixed subinterval was used only to ensure the strict original inequalities.

---

## 5. The nested-residue maximum estimate

The proposed high-depth counting principle is correct.

For an actual $u$, put


$$
L=\lfloor\log_3u\rfloor,
\qquad
d_{\max}=\max_{0\le i<u}v_3(D_{b,i}).
$$


Let $D_a(u)$ and $N_a(u)$ denote the denominator and numerator counts from the retained exact formula.

### 5.1 Exact high-depth denominator count

For $a>L$, we have $3^a>u$. Thus at most one index $i\in[0,u)$ satisfies


$$
D_{b,i}\equiv0\pmod{3^a}.
$$


The sets of satisfying indices are nested as $a$ increases. Since all denominator factors are nonzero,


$$
\boxed{
\sum_{a>L}D_a(u)=(d_{\max}-L)_+.
}
\tag{5.1}
$$


Indeed, $D_a(u)=1$ exactly for $L<a\le d_{\max}$, and is zero thereafter.

It follows immediately that the unmatched high-depth count obeys


$$
\sum_{a>L}\max\{0,D_a(u)-N_a(u)\}
\le(d_{\max}-L)_+.
\tag{5.2}
$$


There is no factor of $u$.

### 5.2 Application to the actual grouped terms

For $u\ge U_b$, the exact valuation formula is


$$
v_3(R_{b,u})
=u+t+v_3\binom{s}{u}
+\sum_{a\ge1}\bigl(N_a(u)-D_a(u)\bigr).
\tag{5.3}
$$


At depths $a\le L$, both $N_a(u)$ and $D_a(u)$ count one residue class in the same interval of length $u$, so


$$
N_a(u)-D_a(u)\ge-1.
$$


At higher depths, discard only the nonnegative numerator counts. Since the actual binomial coefficient is an integer, (5.1) and (5.3) imply


$$
\begin{aligned}
v_3(R_{b,u})
&\ge u+t-L-(d_{\max}-L)_+\\
&=u+t-\max\{L,d_{\max}\}.
\end{aligned}
$$


This proves (1.1).

The added $t$ removes precisely the denominator at $i=I_b$. No other deep denominator has been discarded.

---

## 6. Conditional closure of the later block

Assume $(\mathrm P_3)$.

Combining it with the elementary cases in §3, there is an effective constant $C_4$ such that, for every actual intermediate range,


$$
d_{\max}
\le C_4(1+\log(2u+1))(1+\log J)^2.
\tag{6.1}
$$


This includes the bounded initial negative $B$'s.

Since $u\le2h-1<4J$,


$$
d_{\max}\le C_5(1+\log J)^3.
\tag{6.2}
$$


The same bound, after increasing $C_5$, controls $L$.

On the indices $j_t$ supplied by Theorem 4.2,


$$
\max\{L,d_{\max}\}\le D(1+t)^3
\tag{6.3}
$$


for an effective constant $D$ independent of $t,b,u$.

Every term in the later block satisfies


$$
u\ge I_b+3^t+1>3^t.
$$


Therefore (1.1) gives


$$
v_3(R_{b,u})
\ge3^t+t-D(1+t)^3.
\tag{6.4}
$$


For all sufficiently large $t$, this is at least $143$. Consequently,


$$
\boxed{B_b(A)\in3^{143}\mathbb Z_3,\qquad b=0,1,2.}
\tag{6.5}
$$


The conclusion holds for the exact finite sum (2.4), including the case where it is empty.

Together with (2.5), this proves the following conditional theorem.

> **Theorem 6.1 — continuation conditional only on $(\mathrm P_3)$.**  
> On an infinite original-domain family with exact $t\to\infty$ and $\log(j+1)=O(t)$,
> 

$$
> \boxed{\epsilon T_b(A)\equiv\mathcal R_b\pmod{3^{143}},\qquad b=0,1,2.}
> \tag{6.6}
>
$$


> Hence
> 

$$
> \boxed{
> v_3(T_b(A))=V_b-t,\qquad
> v_3(p_{m+b}(r_0))=-(m+b)+V_b-t.
> }
> \tag{6.7}
>
$$



Thus the rotation and nested-count arguments do supply everything else needed for the proposed logarithm route. The obstruction is now the specific uniform independent-case estimate (3.8), not an additional hidden size/window argument.

---

## 7. Conditional Jacobi units, not just valuations

The retained residue digits allow more precise transfer than the three valuations alone.

Write


$$
\epsilon=3^t e,\qquad e\in\mathbb Z_3^\times,
$$


and


$$
\mathcal R_b=3^{V_b}\varrho_b,
\qquad
(\varrho_0,\varrho_1,\varrho_2)\equiv(2,22,16)\pmod{27}.
$$


Also put


$$
\eta=A+71,\qquad r_0=\eta/3.
$$


Under Theorem 6.1,


$$
p_{m+b}(r_0)
=
3^{-(m+b)+V_b-t}
\eta^{m+b}e^{-1}
\left(\varrho_b+O(3^{143-V_b})\right).
\tag{7.1}
$$


The factors $\eta^{m+b}$ and $e^{-1}$ are the actual units. They must not be replaced by $1$.

Since $v_3(A)=5$,


$$
\eta\equiv71\equiv17\pmod{27}.
$$


For


$$
a_m=\frac{p_{m+1}(r_0)}{p_m(r_0)},
$$


equation (7.1) gives


$$
\frac{a_m}{3}
\equiv17\frac{22}{2}
\equiv25\pmod{27}.
\tag{7.2}
$$


Similarly,


$$
9a_{m+1}
\equiv17\frac{16}{22}
\equiv5\pmod{27}.
\tag{7.3}
$$


All divisions here are by units modulo $27$.

The common factor $e^{-1}$ cancels in these ratios. It does not disappear from the individual evaluated polynomials.

---

## 8. Terminal Wronskian: an exact reduction and the remaining valuation obligation

Because the logarithm input is not yet verified, the two requested preliminary steps have not both closed unconditionally. I therefore do not assert a terminal Wronskian valuation.

Nevertheless, one can sharpen the next obligation and evaluate its known scalar unit.

Use $x$ for the polynomial variable, to distinguish it from the resonance depth $t$. Let


$$
P=p_m,\qquad Q=p_{m+1},\qquad R=p_{m+2},
$$




$$
a=a_m,\qquad d=a_{m+1}.
$$


Then


$$
F_m=Q-aP,\qquad F_{m+1}=R-dQ.
$$


Define


$$
W(f,g)=f'g-g'f.
$$


The terminal numerator is


$$
\mathcal W(x)=W(F_{m+1},F_m)(x).
$$



### 8.1 Elimination of $a_{m+1}$ from the Wronskian

The monic Jacobi recurrence has the form


$$
R(x)=(x-\beta)Q(x)-\gamma P(x).
$$


At $r_0$,


$$
d=r_0-\beta-\frac{\gamma}{a}.
\tag{8.1}
$$


The ratios are well-defined: $r_0>1$, while the zeros of these Jacobi polynomials lie in $(0,1)$.

Expanding the Wronskian gives


$$
\mathcal W=W(R,Q)-aW(R,P)+adW(Q,P).
$$


The recurrence implies


$$
W(R,Q)=Q^2+\gamma W(Q,P),
$$




$$
W(R,P)=PQ+(x-\beta)W(Q,P).
$$


Using (8.1), one obtains the exact identity


$$
\boxed{
\mathcal W(x)=Q(x)\bigl(Q(x)-aP(x)\bigr)
+a(r_0-x)W(Q,P)(x).
}
\tag{8.2}
$$


Thus the apparent dependence on the second quotient $a_{m+1}$ cancels exactly.

Put


$$
\mathfrak a=a_m/3.
$$


At $x=-1$, (8.2) becomes


$$
\boxed{
\mathcal W(-1)
=
Q(-1)^2
-3\mathfrak a\,P(-1)Q(-1)
+\mathfrak a(A+74)\,
\bigl(Q'P-P'Q\bigr)(-1).
}
\tag{8.3}
$$


Conditionally,


$$
\mathfrak a\equiv25\pmod{27},
\qquad
\mathfrak a(A+74)\equiv14\pmod{27}.
\tag{8.4}
$$



This reduction identifies the actual cancellation problem: it is between the complete endpoint quantities in (8.3), not between arbitrarily normalized columns or isolated polar residues.

### 8.2 The known scalar denominator and its unit

The retained exact identity is


$$
\mathscr K_{\rm core}
=
\left.
\frac{\mathcal W(x)}
{-3c\,a_mh_m(x-r_0)^2}
\right|_{x=-1},
\qquad
c=(-1)^A3^h/2.
$$


Here $A=4^j-1$ is odd. Since


$$
-1-r_0=-\frac{A+74}{3},
$$


the denominator simplifies exactly to


$$
-3c\,a_mh_m(-1-r_0)^2
=
\frac{3^h}{2}\,
\mathfrak a h_m(A+74)^2.
\tag{8.5}
$$


Thus


$$
\boxed{
\mathscr K_{\rm core}
=
\frac{2\,\mathcal W(-1)}
{3^h\mathfrak a h_m(A+74)^2}.
}
\tag{8.6}
$$


The known unit multiplying $3^hh_m$ in (8.5) is


$$
\frac{\mathfrak a(A+74)^2}{2}
\equiv
\frac{25\cdot20^2}{2}
\equiv5\pmod{27}.
\tag{8.7}
$$


In particular, conditionally,


$$
\boxed{
v_3(\mathscr K_{\rm core})
=
v_3(\mathcal W(-1))-h-v_3(h_m).
}
\tag{8.8}
$$



Equation (8.8) is not an evaluation of $v_3(\mathscr K_{\rm core})$: the numerator valuation remains to be established.

### 8.3 Concrete next endpoint lemma

A sufficient next lemma must determine, in the actual normalization, the first nonzero $3$-adic digit of


$$
Q(-1)^2
-3\mathfrak a\,P(-1)Q(-1)
+\mathfrak a(A+74)(Q'P-P'Q)(-1),
\tag{8.9}
$$


together with the exact norm factor $h_m$.

Knowing only $v_3(a_m)$, $v_3(a_{m+1})$, or even their first three unit digits does not determine (8.9). The endpoint Jacobi values and jets may have their own valuation losses and cancellations. Their normalizations cannot be suppressed.

Core positivity can supply core nonvanishing at its established scope. It does not give the required $3$-adic valuation, nor nonvanishing of the complete period response.

---

## 9. Actual-force transfer is still limited to precision $3^6$

The logarithm route, even if completed, does not improve the available actual-polynomial precision. On the resonant classes,


$$
v_3(j)=4,
$$


and the retained actual-force result supplies only


$$
Q_n^{\rm loc}=Q_{\rm core}+3^6R.
\tag{9.1}
$$



The matrix coordinates remain


$$
1,y,\ldots,y^m,\qquad 0\le a,d\le m.
$$


The complete functional remains


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\sum_{2v+1\le4n-3}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1}.
\tag{9.2}
$$


In particular, neither the factorial force nor the endpoint subtraction is removed.

The retained complete perturbation is


$$
\begin{aligned}
\Delta_{ad}
={}&-\frac{3^h}{4}
\mathfrak f(Q_n^{\rm loc}y^{a+d})\\
&+3^{h+6}
\sum_{2v+1\le4n-3}
\frac{
[y^v]\bigl(Ry^{a+d}-(-1)^{a+d}R(-1)\bigr)/(y+1)
}{2v+1},
\end{aligned}
\tag{9.3}
$$


with


$$
\Delta\in3^6M_{m+1}(\mathbb Z_3)
$$


at the accepted force theorem’s scope.

Accordingly, the previously stated sufficient transfer conditions must be checked with the actual available $P=6$:


$$
\boxed{
6>L,\qquad
6+2\mu>v_3(\mathscr K_{\rm core}),
}
\tag{9.4}
$$


using the original monomial-coordinate losses $L,\mu$. None of the polar calculations proves these inequalities.

Restoring the actual polynomial multiplier $\lambda_n$ multiplies the matrix by $\lambda_n$ and its inverse endpoint contraction by $\lambda_n^{-1}$. Even when this multiplier is a $3$-adic unit at the retained scope, its unit cannot be omitted from an endpoint-unit calculation, and it cannot be omitted from global primitive arithmetic.

---

## 10. Primitive denominator and whole error remain separate obligations

For the complete determinant, retain


$$
\det H_{\rm complete}=\beta_0+\beta_1(e+\pi),
\qquad k=m+1,
$$


and


$$
A_\ell=\ell^k\beta_0,\qquad B_\ell=\ell^k\beta_1,\qquad
g_\ell=\gcd(|A_\ell|,|B_\ell|).
$$


When $B_\ell\ne0$, the actual primitive denominator and numerator are


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


The whole evaluated error is


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell^k}{g_\ell}
\det H_{\rm complete}.
}
\tag{10.1}
$$


If $\delta$ is the least actual two-coefficient clearer and


$$
g_*=\gcd(|\delta\beta_0|,|\delta\beta_1|),
$$


then equivalently


$$
\frac{\delta}{g_*}=\frac{\ell^k}{g_\ell},
\qquad
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\delta}{g_*}
\det H_{\rm complete}.
\tag{10.2}
$$



Neither a local Jacobi valuation nor a nonzero grouped residue determines this final gcd, proves $B_\ell\ne0$, or proves that the whole error is nonzero and tends to zero. Those requirements remain essential for an irrationality argument.

---

## 11. Exact next inputs and bounded verification

### 11.1 Primary-source input actually needed

The immediate noncomputational request is a primary theorem statement sufficient to establish $(\mathrm P_3)$, or a fixed-polylogarithmic variant such as (3.10), with:

1. uniformity in positive integer $B$;
2. explicit height dependence for $h(B)=\log B$;
3. coefficient dependence for $(J,-1)$;
4. all $p$-adic unit and residue hypotheses;
5. any multiplicative-independence or determinant-cardinality hypotheses;
6. an effective constant independent of $J,B$.

The dependent cases need not be forced into that theorem; §3.3 already treats them exactly.

### 11.2 A bounded threshold certificate after that input is supplied

Once the logarithm theorem supplies an effective constant, choose an integer $D$ large enough for (6.3). A sufficient finite threshold certificate is an integer $T\ge150$, also beyond the fixed real-window threshold, satisfying


$$
\boxed{3^T\ge D(1+T)^3+143.}
\tag{11.1}
$$


For $T\ge2$, $3^T/(1+T)^3$ increases strictly with $T$, so one exact check establishes the corresponding inequality for every larger integer $t$.

**Inputs:** the integer $D$, and a proposed $T$.

**Arithmetic:** compute $3^T$, $D(1+T)^3$, and their difference; no rational divisions are needed.

**Expected certificate:** the exact nonnegative integer


$$
3^T-D(1+T)^3-143.
$$


The arithmetic uses $O(T+\log D)$-bit integers. Binary exponentiation uses $O(\log T)$ multiplications; schoolbook arithmetic gives a conservative polynomial resource bound in $T+\log D$. No $4^{j_t}$ or degree-$m$ Jacobi polynomial need be constructed.

This calculation cannot presently be instantiated with a certified $D$, because the uniform logarithm theorem application is the missing input.

No repetition of the retained grouped-residue calculation is needed. Further finite samples of original indices would not prove the missing uniform logarithm assertion or the endpoint lemma.

---

## 12. Closing ledger

### New rigorous results

1. **Quantitative original-domain hitting:** for each sufficiently large exact depth $t$, a prescribed exact-resonance progression meets the original real window at
   

$$
3^t\le j_t\le C_0\,3^{(K+1)t}.
$$


   Thus $\log(j_t+1)=O(t)$ is proved, not inferred from density.

2. **Nested-residue maximum bound:** the entire high-depth denominator count is
   

$$
(d_{\max}-\lfloor\log_3u\rfloor)_+,
$$


   yielding the sharper valuation bound (1.1).

3. **Elementary logarithm-application checks:** all actual differences are positive and nonzero; nonunit and multiplicatively dependent cases satisfy the required bounds uniformly; the finitely many initial negative $B$'s are explicitly controlled.

### Conditional deductions

A verified uniform independent-case $3$-adic logarithm estimate implies


$$
\epsilon T_b(A)\equiv\mathcal R_b\pmod{3^{143}}
$$


on that infinite family, hence the corrected core valuations with


$$
V=(133,135,134),
$$


and the quotient units in (1.2).

### Exact remaining bottlenecks

The immediate bottleneck is **the verified uniform theorem application $(\mathrm P_3)$**. After it is supplied, the next substantive obligations are:

* evaluate the whole terminal endpoint combination (8.9), including its true Jacobi units and norm;
* prove the original-coordinate transfer inequalities with only $P=6$;
* control the complete response, final gcd, actual primitive denominator, and whole nonzero real error.

**Overall status:** this report removes the quantitative reachability gap and proves the nested-residue estimate. It does not establish an unconditional continuation theorem, an actual-matrix terminal valuation, or irrationality of $e+\pi$. The irrationality of $e+\pi$ remains unresolved.
