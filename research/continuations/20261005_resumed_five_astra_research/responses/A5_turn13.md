> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, Turn 13 — Weighted first differences and uniform decay of the complete positive-shift tail

## Executive conclusion

The coordinator’s weighted first-difference proposal is valid for the complete first producer, under the accepted contact construction and factorial-tail hypotheses. The missing forcing estimate can be proved without combining an absolute bound with an unweighted local bound.

The decisive identity is a factorial budget for an individual complete-force summand. If its central index is $\ell$, put


$$
m=\left\lceil\frac{\ell}{2}\right\rceil,\qquad q=i-\ell.
$$


After writing the two falling products as factorials times binomial coefficients, their parameter-independent scalar has valuation


$$
v_2\!\left(\binom i\ell m!q!\right)
=v_2(i!)-v_2(\ell!)+v_2(m!)
\ge v_2\!\left(\left\lfloor i/2\right\rfloor!\right).
$$


This scalar remains present whichever single parameter factor is changed in a telescoping first difference.

Consequently, with


$$
W_r=\max\left\{0,\left\lceil\frac{r-3}{4}\right\rceil\right\},
\qquad
\beta_r=5+W_r-\left\lfloor\log_2(4W_r+3)\right\rfloor,
$$


the complete continued first solution satisfies


$$
\boxed{
v_2\bigl(p_r^*(k)-p_r^*(k')\bigr)
\ge v_2(k-k')+\beta_r.
}
\tag{1}
$$



Combining this *single weighted difference estimate* with the accepted negative-integer identities and the consecutive-product lemma gives, on every actual original index,


$$
\boxed{
v_2\!\left(
\frac{p_r^*(k)}{\prod_{c=1}^{L}(k+c)}
\right)
\ge \beta_r-v_2((L-1)!)
\quad
\left(1\le L\le\left\lfloor\frac{r+4}{128}\right\rfloor\right).
}
\tag{2}
$$



For the complete reconstructed positive-shift groups, this pays the entire high factorial denominator chain. Their normalized tails tend uniformly to zero, with the actual weight carries and finite boundaries retained.

This yields an **actual, content-relative first-column truncation theorem**: if $a$ is the actual binary content of the raw first column, a cutoff chosen for precision $a+t$ changes that column, after division by its actual content $2^a$, by a vector in $2^t\mathbb Z_2^{b+1}$. There is also an exact adaptive content certificate that does not assume $a$ in advance.

This does **not** evaluate the remaining complete low-shift norm or mixed contraction. In particular, it does not turn the fixed fifth-digit calculations in the older source into a variable-depth second-force theorem. The final all-prime gcd and the full primitive-denominator/whole-error comparison remain unresolved.

No tools were executed, and the closed $p_{380}$ calculation is not repeated.

---

## 1. Scope and preserved domains

Throughout,


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0,
$$


and


$$
b=128D+81,\qquad n=128C+66,\qquad C=4002D+2532,
$$




$$
k=2C+1,\qquad h=32k+1,\qquad n=64k+2,\qquad
b=\frac{32k+1}{2001}.
$$



Actual contact matrices have indices


$$
0\le i,j<b.
$$


Reconstructed scalar coordinates have indices


$$
0\le j\le b.
$$


Their block decomposition remains:

- $0\le t<D,\ 0\le\rho<128$;
- $t=D,\ 0\le\rho\le80$;
- the separate endpoint $j=b$.

Negative integers $k=-c$ are used only in the accepted compatible continuation.

I reuse, at their supplied scopes:

1. the complete central and force formulas;
2. integral finite contact transport and complete-symbol integrality;
3. the accepted precision–degree filtration;
4. the compatible complete inverse and its factorial tails;
5. the general negative-integer high-sector identity audited in A4turn14.

The new issue here is the **weighted** parameter difference of the complete first force and inverse. The accepted unweighted Lipschitz theorem alone would not establish it.

---

## 2. The missing complete-force factorial budget

Write $L(a)=v_2(a!)$, and set


$$
w_i=L(\lfloor i/2\rfloor).
$$



The complete force is


$$
F_i=
\sum_{\ell=0}^{i}
\binom i\ell
\left(\prod_{t=\ell+1}^{i}(n+t)\right)B_\ell(h),
\qquad g_i=(-1)^iF_i.
\tag{3}
$$



For a central coefficient $B_\ell$, its falling-factorial length is


$$
m=\lceil\ell/2\rceil.
$$


The remaining central prefactor is a product of integral affine functions of $h$. Denote it by $O_\ell(h)$. Thus a central summand can be written as


$$
O_\ell(h)\,m!\binom hm\,
a_{\ell,s}
\binom{h-\alpha_\ell}{s}
\binom{h+\delta_\ell}{s},
\tag{4}
$$


where the shifts are those in the displayed even and odd central formulas, and


$$
v_2(a_{\ell,s})=L(s).
\tag{5}
$$



The force product of length $q=i-\ell$ is


$$
\prod_{t=\ell+1}^{i}(n+t)
=q!\binom{n+i}{q}.
\tag{6}
$$



Therefore every individual summand of the complete force has the form


$$
C_{i,\ell}\,
O_\ell(h)\binom hm\binom{n+i}{q}\,
a_{\ell,s}
\binom{h-\alpha_\ell}{s}
\binom{h+\delta_\ell}{s},
\tag{7}
$$


with the parameter-independent integer


$$
C_{i,\ell}=\binom i\ell m!q!.
$$



### Lemma 1 — The force scalar retains the required weight

For $0\le\ell\le i$,


$$
\boxed{v_2(C_{i,\ell})\ge w_i.}
\tag{8}
$$



### Proof

Direct cancellation gives


$$
v_2(C_{i,\ell})=L(i)-L(\ell)+L(\lceil\ell/2\rceil).
$$


If $\ell=2j$, then


$$
L(\ell)-L(\lceil\ell/2\rceil)=L(2j)-L(j)=j.
$$


If $\ell=2j+1$, then


$$
L(2j+1)-L(j+1)
=j-v_2(j+1)\le j.
$$


Hence, in both cases,


$$
L(\ell)-L(\lceil\ell/2\rceil)\le\lfloor\ell/2\rfloor
\le\lfloor i/2\rfloor.
$$


Finally,


$$
L(i)-\lfloor i/2\rfloor=L(\lfloor i/2\rfloor)=w_i.
$$


This proves (8). ∎

This is the step that prevents a derivative of the $n$-product or central falling product from destroying the original force weight.

---

## 3. Weighted first differences of the complete force

Let $k,k'\in\mathbb Z_2$, $k\ne k'$, and put


$$
\lambda=v_2(k-k').
$$


Then


$$
v_2(h-h')=\lambda+5,\qquad
v_2(n-n')=\lambda+6,\qquad
v_2(b-b')=\lambda+5.
$$



For an integral binomial polynomial,


$$
v_2\!\left(\binom{x+\delta}{a}-\binom xa\right)
\ge v_2(\delta)-\lfloor\log_2a\rfloor
\qquad(a\ge1).
\tag{9}
$$



Apply the telescoping product difference to (7). Exactly one factor is changed in each resulting term.

### 3.1 Changing $\binom hm$

The scalar $C_{i,\ell}$ remains unchanged. The loss is at most


$$
\lfloor\log_2m\rfloor\le\lfloor\log_2\max(1,i)\rfloor.
$$



### 3.2 Changing $\binom{n+i}{q}$

Again $C_{i,\ell}$ remains. The loss is at most


$$
\lfloor\log_2q\rfloor,
$$


and the parameter increment has the additional bit $\lambda+6$.

### 3.3 Changing the affine central prefactor

The polynomial $O_\ell$ has integral coefficients. Its difference is divisible by $h-h'$; all the factorial scalar in (8) is retained.

### 3.4 Changing either central-sum binomial

The loss is at most $\lfloor\log_2s\rfloor$, but the scalar $a_{\ell,s}$ has depth $L(s)$, and


$$
L(s)\ge\lfloor\log_2s\rfloor.
\tag{10}
$$


Thus these changes do not consume the force weight $w_i$.

These observations prove the following complete-force statement.

### Theorem 2 — Weighted complete-force difference

For every $i\ge0$,


$$
\boxed{
v_2\bigl(g_i(k)-g_i(k')\bigr)
\ge
\lambda+5+w_i-\lfloor\log_2\max(1,i)\rfloor.
}
\tag{11}
$$



The estimate is for the complete central sums, not fixed truncations.

Indeed, for a changed central-sum binomial, the remaining tail depth includes


$$
L(s)-\lfloor\log_2s\rfloor\longrightarrow\infty.
$$


For the other changed factors, it includes $L(s)\to\infty$. Thus passage to the complete factorially convergent sums is justified.

---

## 4. All positions in a complete contact word

Expand the accepted inverse in contact words. An individual word starts with force degree $i$, and its contact expansion orders are


$$
a_1,\ldots,a_m\ge1.
$$


Write


$$
R=a_1+\cdots+a_m,\qquad W=w_i+R.
$$



The accepted complete-symbol normalization gives:

- scalar depth at least $a_j$ for a contact of expansion order $a_j$;
- contact degree increase at most $4a_j$;
- integral unchanged contact factors;
- a symbol parameter difference retaining its expansion-order depth.

Also,


$$
i\le4w_i+3.
$$


Consequently every intermediate degree, and every endpoint-binomial index arising anywhere in the word, is at most


$$
i+4R\le4W+3.
\tag{12}
$$



There are four kinds of changed positions.

### 4.1 The initial force

Equation (11), followed by unchanged integral contacts, gives


$$
\lambda+5+W-\lfloor\log_2\max(1,i)\rfloor,
$$


which is at least


$$
\lambda+5+W-\lfloor\log_2(4W+3)\rfloor.
$$



### 4.2 The symbol coefficient of any contact

Use the accepted normalization


$$
\binom ha(2U)^a
=
2^a(h)_{\underline a}\frac{U^a}{a!}.
$$


The divided-power factor is integral, and $(h)_{\underline a}$ is an ordinary integral polynomial. Its difference retains the factor $2^a$ and gains $\lambda+5$. No factorial denominator is newly lost.

### 4.3 An $n$-binomial at any contact position

Its index is bounded by that contact’s symbol degree and hence by $4W+3$. The parameter increment has depth $\lambda+6$, so the claimed budget is valid with a spare bit.

### 4.4 Any endpoint factor in any suffix iterate

For suffix powers, use the exact telescoping difference


$$
\mathscr S_b^v-\mathscr S_{b'}^v
=
\sum_{a=0}^{v-1}
\mathscr S_b^a(\mathscr S_b-\mathscr S_{b'})
\mathscr S_{b'}^{\,v-1-a}.
\tag{13}
$$


Only one endpoint functional is changed in each term. Its binomial index is bounded by (12). All other factors are integral.

Thus the endpoint cost is one logarithmic loss,


$$
\lfloor\log_2(4W+3)\rfloor,
$$


not a sum of such losses over the suffix length or word length.

This argument includes endpoint changes:

- before or after a bulk contact;
- inside any iterated suffix;
- after a previous endpoint reset to a lower degree;
- at every position in the Neumann word.

It does not rely on treating endpoint injections as absent at ordinary actual parameters.

### Theorem 3 — Complete differentiated-word budget

Every telescoping first-difference term of a complete word of weight $W$ has valuation at least


$$
\boxed{
\lambda+5+W-\lfloor\log_2(4W+3)\rfloor.
}
\tag{14}
$$



### Uniform tails

The right side of (14), minus $\lambda$, tends to infinity with $W$. At bounded $W$:

- only finitely many force indices occur;
- only finitely many positive contact-order compositions occur;
- every contact has finitely many symbol degrees and suffix positions;
- the remaining central-sum tails converge by the estimates in Section 3.

This supplies the uniform tail justification needed to sum all words and pass to the compatible coefficient limit.

---

## 5. The proposed coefficient estimate is proved

An output coefficient of degree $r$ can receive a word contribution only if


$$
r\le4W+3.
$$


Hence $W\ge W_r$.

For integral $W\ge0$, the function


$$
W-\lfloor\log_2(4W+3)\rfloor
$$


is nondecreasing: on increasing $W$ by one, the logarithmic floor increases by at most one.

Theorem 3 therefore proves


$$
\boxed{
v_2\bigl(p_r^*(k)-p_r^*(k')\bigr)
\ge v_2(k-k')+\beta_r.
}
\tag{15}
$$



This is the coordinator’s proposed bound, with the necessary $W_r=\max(0,\ldots)$ convention for the lowest degrees.

**No step adds separate absolute and unweighted local estimates.** The force factorial scalar and the contact-order scalar were retained inside each differentiated summand before summation.

---

## 6. Exact roots and simultaneous product compensation

The accepted general negative-integer identity gives


$$
p_r^*(-c)=0
\qquad(c\ge1,\ r\ge128c-4).
\tag{16}
$$


Thus, with


$$
J_r=\left\lfloor\frac{r+4}{128}\right\rfloor,
$$


comparison with each root yields


$$
v_2(p_r^*(k))
\ge
\beta_r+\max_{1\le c\le J_r}v_2(k+c).
\tag{17}
$$



For completeness, the consecutive-product lemma states


$$
\sum_{c=1}^{L}v_2(k+c)
-\max_{1\le c\le L}v_2(k+c)
\le v_2((L-1)!).
\tag{18}
$$


To prove it, remove a factor with greatest valuation. At each depth $a$, at most


$$
\left\lceil\frac L{2^a}\right\rceil-1
=
\left\lfloor\frac{L-1}{2^a}\right\rfloor
$$


remaining factors are divisible by $2^a$. Sum over $a$.

On actual indices all $k+c$ are nonzero. Combining (17) and (18) proves (2).

This is a pointwise valuation theorem. It does not assert an integral ordinary-power-series quotient.

---

## 7. Complete positive-shift reconstruction with actual carries

Use the complete reconstruction


$$
F_s(x;2n)
=
\binom{2n+s-1}{s}
\sum_{r\ge s}p_r\binom{x}{r-s},
$$




$$
U_s(x)=F_s(x)+xF_s(x-1)+xF_{s+1}(x-1).
\tag{19}
$$


All three terms are retained.

For $s\ge0$, put


$$
c_s=\left\lfloor\frac{s+4}{128}\right\rfloor.
$$


When $c_s\ge1$, every coefficient in $U_s(j)$ has index at least $s$, so


$$
v_2(U_s(j))
\ge
\beta_s+\max_{1\le c\le c_s}v_2(k+c).
\tag{20}
$$



For an actual interior coordinate $j=128t+\rho<b$, retain


$$
d=D-t,\qquad K=k+d,\qquad
J_d=\binom{k+d-1}{d},
$$




$$
a_0=\left\lfloor\frac{84-\rho}{128}\right\rfloor,\qquad
l_0=\left\lfloor\frac{80-\rho-s}{128}\right\rfloor.
$$


For a valid nonzero moment, the exact stripped quotient is


$$
\frac{\mathcal M_s(j)}{J_d}
=
2^{m_{\rho s}}u_{\rho s}
\frac{K^{a_0+1}d_{\underline{-l_0}}}
{k\prod_{c=1}^{c_s}(k+c)},
\tag{21}
$$


where $u_{\rho s}$ is odd and $m_{\rho s}\ge0$.

Invalid actual moments are zero; they are not represented by factorials with negative arguments.

Let


$$
\mathcal B_t=\binom Ct J_d,
\qquad
A_{j,s}=W_jU_s(j)\mathcal M_s(j).
$$


The exact weight depths remain


$$
v_2\!\left(\frac{W_j}{\binom Ct}\right)
=
\begin{cases}
v_2\binom{68}{\rho},&\rho\le68,\\[2mm]
v_2\binom{196}{\rho}+v_2(C-t),&\rho>68.
\end{cases}
\tag{22}
$$



### Theorem 4 — Weighted normalized high-shift bound

For every actual original index, every interior coordinate, and every $s\ge124$,


$$
\boxed{
\begin{aligned}
v_2(A_{j,s}/\mathcal B_t)\ge{}&
v_2\!\left(W_j/\binom Ct\right)
+m_{\rho s}\\
&+v_2\!\left(K^{a_0+1}d_{\underline{-l_0}}\right)
+\beta_s-v_2((c_s-1)!).
\end{aligned}
}
\tag{23}
$$



This is the complete Turn 12 normalization with its factorial loss now paid by the weighted first difference.

---

## 8. An explicit uniform tail cutoff

Define


$$
\delta_s=\beta_s-v_2((c_s-1)!).
$$


Although $\delta_s$ need not be monotone at every block transition, it has a uniform linear lower bound.

For integral $W\ge0$,


$$
\lfloor\log_2(4W+3)\rfloor\le W/2+2.
$$


Also,


$$
v_2((c-1)!)\le c-1,\qquad
W_s\ge(s-3)/4,\qquad c_s\le(s+4)/128.
$$


Consequently, for $s\ge124$,


$$
\boxed{
\delta_s\ge\frac{15s+460}{128}.
}
\tag{24}
$$



In particular, the convenient sufficient cutoff


$$
\boxed{S(T)=\max\{124,\lceil9T\rceil\}}
\tag{25}
$$


ensures $\delta_s\ge T$ for every $s\ge S(T)$, for nonnegative integral $T$.

Therefore


$$
\boxed{
\sum_{s\ge S(T)}A_{j,s}
\in2^T\mathcal B_t\mathbb Z_2
}
\tag{26}
$$


uniformly over **all** actual $u$ and interior coordinates.

This includes the shortened block $t=D,\rho\le80$. No nonexistent coordinates $\rho>80$ are added to that block.

### The endpoint requires separate treatment

The actual endpoint is


$$
2X_b=W_b\,b\theta_{b-1}.
\tag{27}
$$


It must not be discarded on the grounds that high positive shifts decay.

At $j=b-1$, the moment length is zero; its suffix reconstruction has only shift $0$. After reconstruction to coordinate $b$, this is an endpoint contribution, equivalently the negative-shift boundary term in an extended notation.

Thus the positive-shift truncation in (26) leaves the **entire endpoint unchanged**. It does not show that the endpoint’s high Newton coefficients can be omitted.

---

## 9. Actual content-relative truncation

Let the raw first column be


$$
A=(2X_j)_{0\le j\le b}.
$$


Define $A^{<S}$ by retaining:

- the complete negative-shift and low positive-shift groups $s<S$;
- all actual interior coordinates;
- the complete endpoint (27).

Only the positive-shift groups $s\ge S$ are removed.

Since $\mathcal B_t$ is an actual integer, (26) gives


$$
A-A^{<S(T)}\in2^T\mathbb Z_2^{b+1}.
\tag{28}
$$



The accepted $N>0$ implies $A\ne0$. Its actual binary content


$$
a=\min_{0\le j\le b}v_2(A_j)
$$


is therefore finite.

### Theorem 5 — Actual relative-content theorem

For every actual original index and every integer $t\ge1$,


$$
\boxed{
2^{-a}\bigl(A-A^{<S(a+t)}\bigr)
\in2^t\mathbb Z_2^{b+1}.
}
\tag{29}
$$


Moreover,


$$
\boxed{
\operatorname{cont}_2(A^{<S(a+t)})=a.
}
\tag{30}
$$



### Proof

Equation (28), with $T=a+t$, proves (29). Every coordinate of $A$ is divisible by $2^a$, and at least one has exact valuation $a$. Adding a vector divisible by $2^{a+1}$ preserves that minimum valuation. ∎

This theorem concerns the **actual first-column content**, not merely the content of reference kernels.

### Adaptive certificate without prior knowledge of $a$

For a trial $T$, compute the complete retained column $A^{<S(T)}$ modulo $2^T$. If some coordinate has valuation $a_T<T$, then


$$
\boxed{\operatorname{cont}_2(A)=a_T.}
\tag{31}
$$


Increasing $T$ eventually produces such a certificate, because $a<\infty$.

This is a rigorous termination statement for each actual index. It is not a complexity estimate uniform in the very large finite dimension $b+1$.

---

## 10. Consequences for complete norm and mixed errors

The new tail theorem controls truncation errors, not the value of the remaining scalar.

Put


$$
B=(4Y_j)_{0\le j\le b},
\qquad
c=\min_jv_2(B_j).
$$


Here $B$ means the **complete second column**, including its factorial/exterior force, logarithmic force, all contact terms, and endpoint $+1$.

If $T>a$, equation (28) implies


$$
\boxed{
v_2\!\left(\sum_j A_j^2-\sum_j(A_j^{<S(T)})^2\right)
\ge T+a+1,
}
\tag{32}
$$


because


$$
A_j^2-(A_j^{<S})^2
=2A_j^{<S}(A_j-A_j^{<S})+(A_j-A_j^{<S})^2.
$$



Likewise,


$$
\boxed{
v_2\!\left(\sum_j A_jB_j-\sum_jA_j^{<S(T)}B_j\right)
\ge T+c.
}
\tag{33}
$$



Since


$$
\sum_jA_j^2=4N,\qquad \sum_jA_jB_j=8H,
$$


these are same-index, complete-column truncation certificates.

For the stated raw norm target


$$
\sum_j A_j^2-8S(C,D)\pmod{2^{2\mu+6}},
\tag{34}
$$


it suffices to choose


$$
T>a,\qquad T+a+1\ge2\mu+6.
\tag{35}
$$


A corresponding raw mixed target of precision $M$ requires $T+c\ge M$.

### What remains unevaluated

Equations (32)–(35) do not prove that (34) vanishes. The retained low-shift quantities still contain:

- complete coefficient evaluations;
- actual higher-digit binomial units;
- endpoint-coupled low sectors;
- the full second producer in mixed expressions.

In particular, “finitely many shift labels” does not mean “a bounded-degree polynomial independent of the actual index.” At a large actual coordinate, a low-shift producer can still involve many Newton coefficients.

The older $Q_5$ input was explicitly conditional and fixed-precision. It cannot be promoted here to arbitrary target $2\mu+4$.

Thus the assignment’s first alternative—an actual relative-content theorem—is achieved in (29)–(31). A practical, uniformly reduced **complete scalar evaluation** at variable target remains an outstanding step.

---

## 11. A concrete next lemma

The positive high-shift obstruction is no longer the bottleneck. A useful next target is:

> **Complete low-shift contraction lemma.**  
> At a requested raw scalar precision $M$, and with the tail cutoff certified by (23) or (25), represent and evaluate the retained norm and mixed contractions using a bounded set of complete low-sector producers and exact actual-kernel sums. The representation must include the second factorial/exterior force, every logarithmic term not justified as negligible at precision $M$, the shortened block, and the endpoint $+1$.

A proof must control normalized units as well as valuations. The fifth-digit support reduction in the older source demonstrates why carry support alone is insufficient.

A separate weighted first-difference audit for the **second** complete force may be useful, but it is not supplied by the first-force proof above. Its exterior and logarithmic pieces must be budgeted independently.

---

## 12. Bounded exact arithmetic for independent inspection

No dense precision-$128$ rational-polynomial inverse is needed for the new weighted theorem.

A compact proposed audit is the following.

### Inputs

1. The complete central formulas displayed in the sources.
2. Force formula (3).
3. The exact finite suffix/contact identities.
4. The parameter line
   

$$
h=32k+1,\quad n=64k+2,\quad b=(32k+1)/2001.
$$


5. Bounds
   

$$
0\le i\le31,\qquad 0\le s\le15,\qquad
   \text{total contact expansion order }R\le3.
$$



### Expected verifiable outputs

1. For every $0\le\ell\le i\le31$, the exact integer
   

$$
v_2\!\left(\binom i\ell
   \left\lceil\frac\ell2\right\rceil!(i-\ell)!\right)-w_i,
$$


   verified nonnegative.

2. For the finitely retained force summands and contact words, exact rational-polynomial telescoping identities for
   

$$
f(k)-f(k'),
$$


   retaining each changed position separately.

3. For each such term, a certificate of the normalized difference budget (14), using integral binomial-basis expressions rather than an ordinary monomial coefficient test that could introduce artificial denominators.

4. Direct finite contact-matrix comparisons at small positive odd choices such as $b=1,3$, with $n=4002b$, keeping the actual finite endpoints. These parameters lie on the same continuation line, but are **not** claimed to be members of the original exponential family.

This audit would corroborate the force normalization and endpoint-position bookkeeping only at its stated finite scope. The all-index theorem is the symbolic argument in Sections 2–5.

For an actual variable-target scalar calculation, the required additional inputs are the actual $C,D,\mu$, certified content information, and the complete second-force formulas at the requested precision. Its output should be the complete retained scalar residue together with the tail certificates (32)–(33), not merely a list of surviving paths or coordinates.

---

## 13. Primitive arithmetic and the whole evaluated error

The least actual clearer $d_B$, both complete lifted columns, and the metric remain unchanged:


$$
N_B=d_B[u,v],
$$




$$
A_B=N_{B,1}^{T}\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^{T}\Omega N_{B,2}.
$$


The accepted mixed nonvanishing $H_B\ne0$ is retained.

The final reduction is


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
}
\tag{36}
$$


This is the full gcd, including every odd prime. The primitive multiplier remains $d_B^2/g_B$.

The whole evaluated error is


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n>0
\quad\text{eventually},
}
\tag{37}
$$


where


$$
\log|\epsilon_n|
=
-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
\tag{38}
$$



The new binary relative-content theorem does not bound the full $q_n$ after (36). To obtain irrationality by this construction, one still needs a same-index estimate making the whole nonzero quantity in (37) tend to zero.

---

## Final ledger

### New results proved

1. **Weighted complete-force first difference**, with a factorial scalar that survives changes in either the central falling product or the remaining $n$-product.

2. **Complete differentiated-word control**, including every symbol, bulk, suffix, and endpoint position, with uniform tails.

3. **The proposed weighted coefficient theorem**
   

$$
v_2(p_r^*(k)-p_r^*(k'))
   \ge v_2(k-k')+\beta_r.
$$



4. **Simultaneous weighted product compensation** from the exact negative-integer roots.

5. **Uniform decay of the complete normalized positive-shift tail** on every actual original index, retaining weight carries and the shortened block.

6. **An actual first-column relative-content theorem and adaptive content certificate**, with the endpoint retained exactly.

### Exact remaining bottleneck

The next unresolved mathematical task is the complete, unit-sensitive **low-shift norm and mixed contraction at variable precision**, including the independently complete second force. Beyond it remain the final all-prime gcd and the actual primitive-denominator comparison with the whole nonzero evaluated error.

The classical binomial, factorial, generating-function, and Schur methods are reused at their stated scopes. No exhaustive novelty claim is made.



$$
\boxed{\text{The irrationality of }e+\pi\text{ remains unresolved.}}
$$


