> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## Result: an all-degree tail bound, but not yet the proposed three valuations

The coefficient normalization in the question is correct. I can also exclude **every sufficiently long coefficient interval**, including intervals meeting $3H$, from competing with the proposed dominant terms. The remaining obstruction is a precisely specified set of at most $2h$ near-leading coefficients for each polynomial.

This is a partial result: I do **not** obtain the three asserted valuations uniformly, and therefore do not substitute them as established facts into the endpoint Wronskian.

### 1. Domain and normalization

Use the original turn21 domain, not the narrower fixed-depth domains:


$$
j>0,\qquad81\mid j,\qquad n=4^j+1,\qquad
h=\lfloor\log_3(4n-3)\rfloor,
$$




$$
H=3^{h-1},\qquad A=4^j-1=H-D,\qquad
0<D<H/972,\qquad m=(A+1)/2.
$$


In particular,


$$
t_A:=v_3(A)=1+v_3(j)\ge5.
$$


Write


$$
r_0=(A+71)/3,\qquad v_3(r_0)=-1,
$$


and put $s=m+b$, where $b\in\{0,1,2\}$.

The monic Jacobi polynomial remains


$$
p_s(t)=
\frac{(-1)^s(\tfrac12)_s}{(s+A+\tfrac12)_s}
\sum_{\ell=0}^{s}
\frac{(-s)_\ell(s+A+\tfrac12)_\ell}
     {(\tfrac12)_\ell\,\ell!}t^\ell.
$$


Taking the ratio of its coefficient at $\ell=s-u$ to its leading coefficient gives, exactly,


$$
\boxed{
[t^{s-u}]p_s(t)=
(-1)^u\binom su
\frac{(s-u+\tfrac12)_u}
     {(A+2s+\tfrac12-u)_u}.
}
\tag{1}
$$


Thus the proposed normalization passes.

For valuation calculations, define


$$
N_{b,i}=A+2b-2i,\qquad
D_{b,i}=4A+1+4b-2i.
$$


Then (1) is equivalently


$$
c_{b,u}:=[t^{s-u}]p_s(t)
=(-1)^u\binom su
\prod_{i=0}^{u-1}\frac{N_{b,i}}{D_{b,i}}.
\tag{2}
$$


All factors in these products are nonzero on $0\le u\le s$. In particular, the denominator factors are positive.

Normalize the evaluated terms by the leading term:


$$
E_{b,u}=c_{b,u}r_0^{-u},\qquad
r_0^{-s}p_s(r_0)=\sum_{u=0}^{s}E_{b,u}.
$$


Their exact valuations are


$$
\boxed{
w_b(u):=v_3(E_{b,u})
=u+v_3\binom su+
\sum_{i=0}^{u-1}v_3(N_{b,i})
-\sum_{i=0}^{u-1}v_3(D_{b,i}).
}
\tag{3}
$$


Here $w_b(0)=0$. These formulas track the rational Jacobi denominators explicitly; no integral change of basis is being inferred.

### 2. New uniform lemma: all $u\ge2h$ are harmless

**Lemma.** On the entire domain above, for $b=0,1,2$ and $2h\le u\le m+b$,


$$
\boxed{w_b(u)\ge1.}
\tag{4}
$$



**Proof.** First,


$$
0<D_{b,i}\le 4A+9<9H=3^{h+1},
$$


so every denominator factor has valuation at most $h$.

For any $a\ge1$, the indices $i$ for which


$$
3^a\mid D_{b,i}
$$


form one residue class modulo $3^a$, because $2$ is invertible modulo $3^a$. Among $u$ consecutive indices, their number is at most


$$
\left\lfloor\frac{u-1}{3^a}\right\rfloor+1.
$$


Consequently


$$
\begin{aligned}
\sum_{i=0}^{u-1}v_3(D_{b,i})
&\le
\sum_{a=1}^{h}
\left(\left\lfloor\frac{u-1}{3^a}\right\rfloor+1\right)\\
&\le v_3((u-1)!)+h\\
&\le (u-1)/2+h.
\end{aligned}
\tag{5}
$$


The binomial coefficient and every numerator factor in (3) are integers. Dropping their nonnegative valuations gives


$$
w_b(u)\ge u-v_3((u-1)!)-h
\ge (u+1)/2-h.
$$


For $u\ge2h$, the right side is positive. Since $w_b(u)$ is an integer, (4) follows. ∎

This argument does not exclude a denominator of depth $h$; it accounts for one explicitly. Thus a long interval encountering $3H$, or another highly divisible denominator, is covered rather than omitted.

The degree is approximately $H/2$, whereas the remaining window has length at most $2h$. This is a genuine reduction of the unresolved coefficient problem, not a finite-degree verification.

### 3. The suggested initial dominant terms

The first terms have the expected valuations.

For $u=1$,


$$
E_{b,1}
=-\frac{s(A+2b)}{4A+1+4b}\,\frac3{A+71}.
$$


Using $v_3(A)\ge5$, one obtains


$$
\begin{array}{c|ccc}
b&0&1&2\\ \hline
v_3(s)&0&1&0\\
v_3(A+2b)&t_A&0&0\\
v_3(4A+1+4b)&0&0&2\\ \hline
w_b(1)&t_A+1&2&-1.
\end{array}
\tag{6}
$$


In particular, the third polynomial has a term of valuation $-1$ relative to its leading term, exactly as proposed.

For that third polynomial, the next term cannot tie:


$$
v_3\binom{m+2}{2}=1,
$$


while its two numerator factors $A+4,A+2$ are units and its denominator factors $4A+9,4A+7$ have total valuation $2$. Therefore


$$
\boxed{w_2(2)=2+1-2=1.}
\tag{7}
$$



What remains unproved is that no other near-leading term competes:


$$
\begin{cases}
w_b(u)\ge1,&b=0,1,\quad 2\le u<2h,\\
w_2(u)\ge0,&3\le u<2h.
\end{cases}
\tag{8}
$$


These inequalities would be sufficient, respectively, to give


$$
v_3(p_m(r_0))=-m,\qquad
v_3(p_{m+1}(r_0))=-(m+1),\qquad
v_3(p_{m+2}(r_0))=-(m+3).
$$


I have not proved (8).

The exact obstruction is the denominator residue


$$
4A+1+4b-2i\equiv0\pmod{3^a}
\tag{9}
$$


within the short window. The information $v_3(A)\ge5$ controls its first digits but does not, by itself, bound its deeper valuation. A proof must compare these denominator depths with **both** the numerator interval and the binomial valuation in (3). Merely retaining the factor $A$ appearing at $i=b$ does not complete that comparison.

### 4. A bounded exact replacement for the full evaluated polynomial

The lemma yields the uniform congruence


$$
\boxed{
r_0^{-s}p_s(r_0)
\equiv
\sum_{u=0}^{\min(s,\,2h-1)}E_{b,u}
\pmod{3\mathbb Z_3}.
}
\tag{10}
$$


The congruence is meaningful even if either side is nonintegral: their difference belongs to $3\mathbb Z_3$.

More generally, the same proof gives, for every integer $a\ge1$,


$$
\boxed{
\sum_{u=U}^{s}E_{b,u}\in3^a\mathbb Z_3
\quad\text{if}\quad U\ge2(h+a)-1.
}
\tag{11}
$$


Indeed, the lower bound in the proof is then at least $a$.

Thus any eventual valuation below $a$ can be certified from an explicit $O(h+a)$-term rational sum, independently of the exponentially larger Jacobi degree. This does **not** prove that such valuations are uniform in $j$, but it provides a bounded exact object for the next argument.

For reproducibility, every valuation in that object can be computed through residue counts. If $\rho_{b,a}$ is the representative in $[0,3^a-1]$ satisfying


$$
2\rho_{b,a}\equiv4A+1+4b\pmod{3^a},
$$


then the denominator contribution at depth $a$ is exactly


$$
\#\{0\le i<u:i\equiv\rho_{b,a}\pmod{3^a}\}
=
\max\left(0,1+\left\lfloor
\frac{u-1-\rho_{b,a}}{3^a}\right\rfloor\right).
\tag{12}
$$


The numerator has the identical formula with residue determined by
$2i\equiv A+2b\pmod{3^a}$, and the binomial contribution follows from Legendre’s formula. Equation (12), rather than a bound on denominator factors in isolation, is the remaining exact comparison problem.

### 5. Endpoint cancellation and actual-form transfer remain separate

I retain turn21’s exact formula


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
a_s=p_{s+1}(r_0)/p_s(r_0),\qquad
c=(-1)^A3^h/2.
$$


The result above does not evaluate its numerator. Even proving the three proposed valuations would not alone exclude cancellation between its two Wronskian products.

The actual columns remain $1,y,\ldots,y^m$. The complete metric remains


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
\sum_{\substack{0\le t\le h,\ c\ge1\ {\rm odd}\\
3\nmid c,\ c3^t\le4n-3}}
3^{h-t}c^{-1}
[y^{(c3^t-1)/2}]
\frac{F-F(-1)}{y+1}.
$$


No factorial force, pole unit, cutoff, or endpoint subtraction is removed by the Jacobi calculation.

For transfer from the core, the monomial-coordinate losses still must satisfy turn21’s sufficient conditions


$$
P>L,\qquad P+2\mu>v_3(\mathscr K_{\rm core}),
$$


with the actual available perturbation precision. Restoring the primitive polynomial unit
$\lambda=L_n/3$ multiplies the matrix by $\lambda$ and the inverse endpoint contraction by $\lambda^{-1}$.

Core positivity proves core nonvanishing only. Since


$$
Q_{\rm core}(-1)=0,
$$


it does not prove nonvanishing of the actual period response or the whole error.

### 6. Source audit concerning turn17

The already proved all-depth **analytic source** is explicitly turn17 §§1–4: restricted-series coefficient convergence, legitimate contraction of ordinary Taylor coefficients, the true jets, and the projection estimate. Turn17 §5 also proves the integral-force support lemma.

However, the supplied complete turn17 text expressly labels the polynomial conclusion conditional on verification of the full regular-force integrality and exceptional-column-to-$\eta$ coordinate map. Therefore I cannot accurately describe that document alone as an unconditional proof of the full actual-polynomial approximation. The missing issue is its stated coordinate application, not a need to redo its all-depth series argument.

### 7. Primitive arithmetic retained

For the complete determinant coefficient pair


$$
\det H_{\rm complete}=\beta_0+\beta_1(e+\pi),
$$


retain


$$
A_\ell=\ell^k\beta_0,\quad B_\ell=\ell^k\beta_1,\quad
g_\ell=\gcd(|A_\ell|,|B_\ell|),\qquad k=m+1.
$$


If $\delta$ is the least actual two-coefficient clearer and


$$
g_*=\gcd(|\delta\beta_0|,|\delta\beta_1|),
$$


then


$$
\frac{\delta}{g_*}=\frac{\ell^k}{g_\ell}.
$$


On indices with $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
$$


and the whole real error is


$$
\boxed{
q(e+\pi)-p=
\frac{\operatorname{sgn}(B_\ell)\ell^k}{g_\ell}
\det H_{\rm complete}
=
\frac{\operatorname{sgn}(B_\ell)\delta}{g_*}
\det H_{\rm complete}.
}
$$


No valuation of this actual $q$, response nonvanishing, or whole-error nonvanishing follows from the new lemma.

## Closing ledger

1. **New result and proof status.** Proved the coefficient normalization and an all-degree tail bound: every $u\ge2h$ has positive relative valuation for all three near-terminal Jacobi polynomials. More generally, (11) truncates the evaluated polynomial to $O(h+a)$ terms at precision $3^a$. The initial candidate dominant terms have the asserted depths. The three complete valuations remain unproved.

2. **Exact remaining bottleneck.** Prove the short-window comparisons (8), or identify and evaluate their exception classes using (3) and (12). After that, the Wronskian numerator still requires a cancellation argument, followed by actual-coordinate inverse-loss and perturbation transfer. Final gcd and nonzero whole-error decay remain unresolved; no irrationality conclusion is obtained.

3. **Computation request.** None. The next necessary step is a uniform residue-count comparison in the explicitly bounded window, not a finite-degree Jacobi scan.
