> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4, Turn 16 — Independent audit of weighted tail control and factorial-depth resonance splitting

## Executive assessment

The principal new arguments in A5turn12/13 and A3turn6 pass, **at the stated scope of the accepted complete contact construction, compatible continuation, and local endpoint theorems**. The weighted argument in A5turn13 is materially stronger than adding an absolute estimate to an unweighted local estimate: its factorial weight survives inside each differentiated summand.

Two qualifications are essential:

1. **Divided-power integrality must be stated in the divided-power coefficient lattice, not in the ordinary integral polynomial ring.** With that clarification, the symbol normalization is correct, and its proof is supplied below.
2. **The polynomial denominator-distortion theorem is only a selected-prime theorem.** It neither bounds the full primitive denominator nor permits omission of the logarithmic force from exact primitive reduction or whole-error evaluation.

The audit establishes the following conclusions.

- The complete-force scalar $C_{i,\ell}$ survives every relevant telescoping change.
- The differentiated-word estimate, including all bulk, contact, suffix, and endpoint positions, is valid.
- The degree bound $4W+3$, the required monotonicity, the factorial compensation, the linear bound for $\delta_s$, and the cutoff $S(T)$ are valid.
- The resulting actual first-column content-relative truncation theorem is valid, provided the complete endpoint and complete retained low-shift producers remain present.
- A3’s homogeneous/flat splitting, invariant determinant, middle factorial-depth digit, and two specified simplified-target exclusions are valid.
- Restoring the complete logarithmic force changes the selected-prime denominator by at most the stated polynomial factor.
- A sharper, endpoint-sensitive version of that last stability theorem follows; it is proved in Section 8 below.

These results do **not** settle irrationality or rationality of $e+\pi$. The actual relative scalar, mixed contraction, unselected-prime gcd, and whole nonzero evaluated form remain global obligations.

No tools were executed. The supplied source and receipt were read only as mathematical data. The accepted A1turn8 and A2turn5 audit is not reopened.

---

## 1. Domains, boundaries, and scope of accepted inputs

### 1.1 Binary producer

The original binary family remains


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0,
$$


with


$$
b=128D+81,\qquad n=128C+66,\qquad C=4002D+2532,
$$




$$
k=2C+1,\qquad h=32k+1,\qquad n=64k+2,\qquad
b=\frac{32k+1}{2001}.
$$



The contact matrix indices remain


$$
0\le i,j<b.
$$


The reconstructed scalar coordinates remain


$$
0\le j\le b,
$$


partitioned into the full blocks


$$
0\le t<D,\quad 0\le\rho<128,
$$


the shortened block


$$
t=D,\quad 0\le\rho\le80,
$$


and the separate endpoint $j=b$.

Negative integers $k=-c$ are evaluation parameters of the accepted compatible continuation. They are not negative matrix sizes.

### 1.2 A3 producer

A3 retains


$$
d=2,\qquad b=3,
$$


with contact indices $0,1,2$, reconstructed coordinates $0,1,2,3$, and complete force index at most $2n+2$.

Its new infinite-family conclusions concern


$$
n=15^r,\quad r\ge2,
$$


or


$$
n=105^r,\quad r\ge2.
$$


These are original producer indices, not rescaled factorial parameters.

### 1.3 Status of reused results

The following are reused only at their accepted scope:

- the complete central and force formulas;
- the finite suffix/contact identities;
- the compatible Newton-lattice construction and factorial tails;
- the finite precision–degree filtration;
- the local endpoint and full-gcd classification at eligible primes;
- the retained whole-error identities and nonvanishing results.

The proofs below address the new weighted and splitting assertions. They do not infer an infinite theorem from the finite receipts.

---

# Part I. A5turn12/13

## 2. The force scalar survives every first difference

Write


$$
L(m)=v_2(m!),\qquad w_i=L(\lfloor i/2\rfloor).
$$


For a complete-force summand with central index $\ell$, put


$$
m=\lceil\ell/2\rceil,\qquad q=i-\ell.
$$



After the two falling products are rewritten, the parameter-independent scalar is


$$
C_{i,\ell}=\binom i\ell\,m!\,q!.
$$


Its exact valuation is


$$
v_2(C_{i,\ell})
=L(i)-L(\ell)+L(\lceil\ell/2\rceil).
$$



If $\ell=2j$, then


$$
L(\ell)-L(\lceil\ell/2\rceil)=L(2j)-L(j)=j.
$$


If $\ell=2j+1$, then


$$
L(\ell)-L(\lceil\ell/2\rceil)
=L(2j+1)-L(j+1)
=j-v_2(j+1)\le j.
$$


Consequently,


$$
v_2(C_{i,\ell})
\ge L(i)-\lfloor i/2\rfloor
=L(\lfloor i/2\rfloor)=w_i.
$$



Thus


$$
\boxed{v_2(C_{i,\ell})\ge w_i.}
$$



This scalar is independent of $k,h,n,b$. Therefore it remains present when a telescoping difference changes any one of:

- $\binom hm$;
- $\binom{n+i}{q}$;
- the integral affine-product prefactor $O_\ell(h)$;
- either central-sum binomial.

There is no legitimate cancellation of $m!$ or $q!$ from this budget merely because the corresponding binomial factor is differentiated.

For the two central scalar types,


$$
a_{\ell,s}
=\frac{2^s(s!)^2}{(2s)!}
\quad\text{or}\quad
\frac{2^s(s!)^2}{(2s+1)!},
$$


one has


$$
v_2(a_{\ell,s})=L(s),
$$


since


$$
L(2s)=L(2s+1)=s+L(s).
$$


This is the precise factorial depth available to pay a changed central-binomial loss.

### 2.1 Complete-force difference

For $x,\delta\in\mathbb Z_2$ and $a\ge1$,


$$
\binom{x+\delta}{a}-\binom xa
=\sum_{j=1}^a\binom{\delta}{j}\binom{x}{a-j},
$$


and


$$
\binom{\delta}{j}=\frac{\delta}{j}\binom{\delta-1}{j-1}.
$$


Hence


$$
v_2\!\left(\binom{x+\delta}{a}-\binom xa\right)
\ge v_2(\delta)-\lfloor\log_2a\rfloor.
$$



Let


$$
\lambda=v_2(k-k').
$$


The parameter increments have depths


$$
v_2(h-h')=\lambda+5,\qquad
v_2(n-n')=\lambda+6,\qquad
v_2(b-b')=\lambda+5.
$$



Changing $\binom hm$ or $\binom{n+i}{q}$ loses at most
$\lfloor\log_2\max(1,i)\rfloor$. Changing $O_\ell$ loses no factorial weight. Changing a central-sum binomial loses at most $\lfloor\log_2s\rfloor$, paid by


$$
L(s)\ge\lfloor\log_2s\rfloor.
$$



Therefore the stated complete-force estimate follows:


$$
\boxed{
v_2(g_i(k)-g_i(k'))
\ge
\lambda+5+w_i-\lfloor\log_2\max(1,i)\rfloor.
}
$$



The passage from finite central sums to the complete sums is justified because the residual central depths are either $L(s)$ or


$$
L(s)-\lfloor\log_2s\rfloor,
$$


both tending to infinity.

**Verdict:** A5turn13’s missing force estimate is proved. It does not add unrelated lower bounds.

---

## 3. Divided powers and every differentiated contact position

### 3.1 The correct meaning of integrality of $U^a/a!$

From


$$
1+2U=\left(1-z+\frac{z^2}{2}\right)^2
$$


one obtains


$$
U=-z+z^2-\frac{z^3}{2}+\frac{z^4}{8}
=-\frac z{1!}+2\frac{z^2}{2!}
-3\frac{z^3}{3!}+3\frac{z^4}{4!}.
$$



Thus $U$ has integral **divided-power coefficients**. It is not an ordinary polynomial in $\mathbb Z[z]$, and $U^a/a!$ need not lie in $\mathbb Z[z]$.

For a direct proof of the needed statement, write


$$
U=\sum_{j=1}^4 u_j\frac{z^j}{j!},
\qquad (u_1,u_2,u_3,u_4)=(-1,2,-3,3).
$$


Then


$$
d![z^d]\frac{U^a}{a!}
=
\sum_{\substack{m_1+\cdots+m_4=a\\
m_1+2m_2+3m_3+4m_4=d}}
\frac{d!}{\prod_{j=1}^4m_j!(j!)^{m_j}}
\prod_{j=1}^4u_j^{m_j}.
$$


The displayed factorial quotient counts partitions of a labelled $d$-element set into $m_j$ unordered blocks of size $j$. It is an integer. Therefore


$$
\boxed{\frac{U^a}{a!}\text{ has integral divided-power coefficients}.}
$$



This is exactly the coefficient lattice required by the contact normalization. No ordinary-coefficient integrality claim is needed.

Now


$$
\binom ha(2U)^a
=2^a(h)_{\underline a}\frac{U^a}{a!}.
$$


Since $(h)_{\underline a}\in\mathbb Z[h]$, its first difference is divisible by $h-h'$. A changed symbol coefficient therefore retains depth $a$ and gains $\lambda+5$.

**Clarification required in the source:** “The divided-power factor is integral” should explicitly mean integral in this divided-power lattice.

### 3.2 Degree and endpoint-index bounds

For a contact word starting at force degree $i$, let the contact expansion orders be $a_1,\ldots,a_m$, and put


$$
R=\sum_j a_j,\qquad W=w_i+R.
$$



The symbol degree of an order-$a_j$ contact is at most $4a_j$. Also


$$
i\le4w_i+3.
$$


For example, writing $i=2m$ or $2m+1$, this follows from


$$
L(m)\ge\lfloor m/2\rfloor.
$$



Thus every intermediate degree is at most


$$
i+4R\le4W+3.
$$



For a suffix iterate, $\mathscr S_b$ increases degree by at most one. In a contact of symbol degree $s$, a changed endpoint functional can encounter at most degree $d+s-1$, hence an endpoint binomial index at most $d+s$. Earlier endpoint resets lower degree; they do not increase this bound.

Therefore


$$
\boxed{\text{every relevant endpoint-binomial index is at most }4W+3.}
$$



### 3.3 Exhaustive changed-position accounting

A first difference of a complete word is expanded by the product telescoping identity. Each term changes exactly one position.

| Changed position | Retained depth | Additional change budget |
|---|---:|---:|
| Initial complete force | $w_i+R=W$ | $\lambda+5-\lfloor\log_2\max(1,i)\rfloor$ |
| Symbol coefficient | $W$ | $\lambda+5$ |
| Contact $n$-binomial | $W$ | at least $\lambda+6-\lfloor\log_2(4W+3)\rfloor$ |
| Endpoint functional in any suffix iterate | $W$ | $\lambda+5-\lfloor\log_2(4W+3)\rfloor$ |

For suffix powers,


$$
\mathscr S_b^v-\mathscr S_{b'}^v
=
\sum_{a=0}^{v-1}
\mathscr S_b^a(\mathscr S_b-\mathscr S_{b'})
\mathscr S_{b'}^{v-1-a}.
$$


Only one endpoint functional changes in each summand. Consequently the logarithmic loss occurs once, not once per suffix step.

This accounts for endpoint changes:

- before and after bulk transport;
- inside every suffix iterate;
- following an earlier endpoint reset;
- at every position of the Neumann word.

Every differentiated term consequently has depth


$$
\boxed{
\lambda+5+W-\lfloor\log_2(4W+3)\rfloor.
}
$$



At bounded $W$, there are only finitely many possible starting degrees, positive contact-order compositions, symbol degrees, and suffix positions. The remaining central tails converge by Section 2. As $W\to\infty$, the displayed depth tends to infinity.

**Verdict:** the complete differentiated-word argument passes, including its limit passage.

---

## 4. Coefficient bound, negative-integer roots, and factorial compensation

### 4.1 Monotonicity

Define


$$
f(W)=W-\lfloor\log_2(4W+3)\rfloor,\qquad W\in\mathbb Z_{\ge0}.
$$


At $W=0$, the logarithmic floors for $4W+3$ and $4W+7$ differ by one. For $W\ge1$,


$$
4W+7<2(4W+3),
$$


so the logarithmic floor again increases by at most one. Thus $f(W+1)\ge f(W)$.

An output degree $r$ requires


$$
W\ge W_r:=\max\left\{0,\left\lceil\frac{r-3}{4}\right\rceil\right\}.
$$


Therefore


$$
\boxed{
v_2(p_r^*(k)-p_r^*(k'))
\ge v_2(k-k')+\beta_r,
\quad
\beta_r=5+W_r-\lfloor\log_2(4W_r+3)\rfloor.
}
$$


In particular, $\beta_r$ is nondecreasing.

### 4.2 Negative-integer continuation and actual endpoints

The endpoint remainder identity is


$$
R_sP
=
\sum_{e=0}^{s-1}
(-1)^e\binom{n+e}{s}
\mathcal L_b\mathscr S_b^{s-1-e}P\,E_e.
$$


At $n=-N$, every term with $e\ge N$ vanishes because


$$
\binom{e-N}{s}=0,\qquad 0\le e-N<s.
$$


All endpoint moments remain present until this factor is evaluated.

Bulk transport from below $N$ into degree $N+m$ has multiplier


$$
\binom ms=0
$$


when the input degree is below $N$. Thus the continued high sector is closed independently of the endpoint value.

The complete force and central generating functions then give


$$
\sum_{m\ge0}p_{N+m}\frac{t^m}{m!}
=B_N(1+t)^{N-1},
$$


with $B_N\ne0$. Therefore


$$
p_{N+m}=B_N(N-1)_{\underline m},
\qquad p_r=0\quad(r\ge2N).
$$



This proves the high-sector statement within the accepted compatible continuation. It does not change any actual finite boundary. On the parameter line,


$$
k=-c\implies N=64c-2,
$$


so


$$
\boxed{p_r^*(-c)=0\quad(r\ge128c-4).}
$$



### 4.3 The product loss is retained, not suppressed

For $L$ consecutive nonzero integers, removal of a factor of maximal binary valuation leaves at most


$$
\left\lfloor\frac{L-1}{2^a}\right\rfloor
$$


multiples of $2^a$ at every depth $a$. Hence


$$
\sum_{c=1}^L v_2(k+c)-\max_{1\le c\le L}v_2(k+c)
\le v_2((L-1)!).
$$



Combining this with the **single weighted difference estimate** yields


$$
\boxed{
v_2\!\left(
\frac{p_r^*(k)}{\prod_{c=1}^L(k+c)}
\right)
\ge
\beta_r-v_2((L-1)!),
\quad
1\le L\le\left\lfloor\frac{r+4}{128}\right\rfloor.
}
$$



This is pointwise division-safe valuation control. It is not an assertion that the quotient belongs to an ordinary integral power-series ring.

---

## 5. Positive-shift tails and actual content-relative truncation

### 5.1 Complete reconstructed group

All three terms in


$$
U_s(j)=F_s(j)+jF_s(j-1)+jF_{s+1}(j-1)
$$


are retained. At an actual integer coordinate their binomial multipliers are integral, and their coefficient indices are at least $s$. Thus, with


$$
c_s=\left\lfloor\frac{s+4}{128}\right\rfloor,
$$




$$
v_2(U_s(j))
\ge
\beta_s+\max_{1\le c\le c_s}v_2(k+c)
\qquad(s\ge124).
$$



The exact moment normalization is


$$
\frac{\mathcal M_s(j)}{J_d}
=
2^{m_{\rho s}}u_{\rho s}
\frac{K^{a_0+1}d_{\underline{-l_0}}}
{k\prod_{c=1}^{c_s}(k+c)}.
$$


Here the actual $k$ is odd, $m_{\rho s}\ge0$, and valid moments have nonnegative factorial arguments. Invalid moments are zero.

Thus every denominator factor $k+c$ is accounted for, and the remaining factorial loss is exactly the one bounded above:


$$
\begin{aligned}
v_2(A_{j,s}/\mathcal B_t)\ge{}&
v_2\!\left(W_j/\binom Ct\right)+m_{\rho s}\\
&+v_2\!\left(K^{a_0+1}d_{\underline{-l_0}}\right)
+\beta_s-v_2((c_s-1)!).
\end{aligned}
$$


The numerator and carry terms are nonnegative and have not been replaced by units.

### 5.2 Audit of the linear bound

For integer $W\ge0$,


$$
\lfloor\log_2(4W+3)\rfloor\le W/2+2.
$$


A finite verification for $W=0,1,2,3$, followed by induction in steps of two using


$$
4(W+2)+3\le2(4W+3)\qquad(W\ge2),
$$


proves this inequality.

Therefore


$$
\beta_s\ge3+\frac{W_s}{2}.
$$


Using


$$
v_2((c_s-1)!)\le c_s-1,\qquad
W_s\ge\frac{s-3}{4},\qquad
c_s\le\frac{s+4}{128},
$$


one obtains


$$
\begin{aligned}
\delta_s
&:=\beta_s-v_2((c_s-1)!)\\
&\ge4+\frac{s-3}{8}-\frac{s+4}{128}\\
&=\frac{15s+460}{128}.
\end{aligned}
$$


Hence


$$
\boxed{\delta_s\ge(15s+460)/128\qquad(s\ge124).}
$$



For nonnegative integral $T$,


$$
S(T)=\max\{124,\lceil9T\rceil\}
$$


is sufficient: if $s\ge S(T)$, then


$$
15s+460\ge135T+460\ge128T.
$$



Thus


$$
\boxed{
\sum_{s\ge S(T)}A_{j,s}
\in2^T\mathcal B_t\mathbb Z_2
}
$$


uniformly over the actual family and actual interior coordinates.

### 5.3 Endpoint retention and relative content

The separate endpoint remains


$$
2X_b=W_b\,b\theta_{b-1}.
$$


The positive-shift deletion must leave this expression unchanged. In particular, the tail theorem does not justify discarding high Newton coefficients from this endpoint or from retained low-shift producers.

Let


$$
A=(2X_j)_{0\le j\le b}.
$$


With complete low-shift groups and complete endpoint retained,


$$
A-A^{<S(T)}\in2^T\mathbb Z_2^{b+1}.
$$


Since $A\ne0$, its actual content


$$
a=\min_jv_2(A_j)
$$


is finite. For $t\ge1$,


$$
\boxed{
2^{-a}(A-A^{<S(a+t)})
\in2^t\mathbb Z_2^{b+1},
}
$$


and the truncated vector has the same content $a$.

The adaptive certificate is also valid: if a coordinate of $A^{<S(T)}\bmod2^T$ has minimum valuation $a_T<T$, then the true content is $a_T$.

This is a per-index termination theorem. It is not a uniform complexity theorem or a bounded-degree reduction independent of the actual index.

### 5.4 Raw norm and mixed factors

Put


$$
B=(4Y_j)_{0\le j\le b},
\qquad c=\min_jv_2(B_j),
$$


with the complete second force and endpoint $+1$ included.

For integral $T>a$, writing $E=A-A^{<S(T)}$,


$$
A_j^2-(A_j-E_j)^2=2A_jE_j-E_j^2.
$$


Thus


$$
v_2\!\left(\sum_jA_j^2-\sum_j(A_j^{<S(T)})^2\right)
\ge T+a+1,
$$


because $2T\ge T+a+1$. Also


$$
v_2\!\left(\sum_jA_jB_j-\sum_jA_j^{<S(T)}B_j\right)
\ge T+c.
$$



The normalizations are


$$
\boxed{\sum_jA_j^2=4N,\qquad \sum_jA_jB_j=8H.}
$$


Consequently the corresponding bounds after dividing to recover $N,H$ lose respectively two and three bits.

**Verdict:** A5turn13’s relative-content and raw contraction-error theorems pass. They do not evaluate the retained scalar or mixed contraction.

---

# Part II. A3turn6

## 6. Homogeneous splitting, invariant determinant, and the middle digit

### 6.1 Exact splitting

Let


$$
\mathcal Z_n(z)=\frac{n!Q(z)^n}{(1-z)^{n+1}}.
$$


Its logarithmic derivative is


$$
\frac{\mathcal Z_n'}{\mathcal Z_n}
=n\frac{Q'}Q+\frac{n+1}{1-z},
$$


so


$$
\mathscr L_n\mathcal Z_n=0.
$$


Its contact coefficients are exactly the first force:


$$
(n+i)![z^{n+i}]\mathcal Z_n=z_i.
$$



Since


$$
A_n(0)=n!\eta_n,\qquad \mathcal Z_n(0)=n!,
$$


the zero-initial-value solution


$$
A_n^{\mathrm{flat}}=A_n-\eta_n\mathcal Z_n
$$


satisfies the same complete forced equation. Therefore


$$
\boxed{w=w^{\mathrm{flat}}+\eta_nz.}
$$



Both exponential and logarithmic forcing remain in the flat recurrence.

With $f_n=(n!)^2$, the endpoint determinants satisfy


$$
Y=Y^{\mathrm{flat}}+\eta_nf_nX,\qquad
R=R^{\mathrm{flat}}+\eta_nf_nZ.
$$


Thus


$$
\boxed{
XR-ZY=XR^{\mathrm{flat}}-ZY^{\mathrm{flat}}.
}
$$


The $\Delta$ term in $Y^{\mathrm{flat}}$, representing the exterior $+1$, is indispensable.

It follows that


$$
\boxed{
\Theta-\Theta^{\mathrm{flat}}
=n!\mathfrak u_n\bigl(F(n)+n!\ell_n\bigr),
\qquad
\mathfrak u_n=\frac{XZ}{XR-ZY}.
}
$$



### 6.2 Eligibility

At $p=3,5,7$, the one-digit values of $\tau_j$ are all nonzero modulo $p$:


$$
\begin{array}{c|l}
p&(\tau_0,\ldots,\tau_{p-1})\pmod p\\ \hline
3&(1,1,2)\\
5&(1,1,2,4,1)\\
7&(1,1,2,4,5,1,6).
\end{array}
$$


The accepted Lucas-type constant-term identity therefore makes $\tau_n$ a unit at every selected prime on the stated families.

The accepted contact congruence has determinant $2$ modulo these odd primes. Hence $C^{-1}$ is $p$-integral. The established local conclusions give


$$
X,Z,R,\Delta\in\mathbb Z_{(p)}^\times,\qquad Y\in p\mathbb Z_{(p)},
$$


and therefore $XR-ZY$ and $\mathfrak u_n$ are units.

### 6.3 Nonzero middle-depth digit

Let $N_p=v_p(n!)$. Since $p\mid n$,


$$
F(n)=1+nF(n-1)\equiv1\pmod p.
$$


Also


$$
v_p(\ell_n)\ge-\lfloor\log_pn\rfloor.
$$


Under


$$
N_p>\lfloor\log_pn\rfloor,
$$




$$
F(n)+n!\ell_n\equiv1\pmod p.
$$


Thus


$$
\boxed{v_p(\Theta-\Theta^{\mathrm{flat}})=N_p.}
$$



Using


$$
X/\Delta\equiv-\tau_n,\quad
Z/\Delta\equiv\tau_n/2,\quad
R/\Delta\equiv1,\quad Y/\Delta\equiv0\pmod p,
$$


one gets


$$
\mathfrak u_n\equiv\tau_n/2\pmod p,
$$


and hence


$$
\boxed{
\frac{\Theta-\Theta^{\mathrm{flat}}}{n!}
\equiv\frac{\tau_n}{2}\pmod p.
}
$$



All ten valuation/residue predictions in A3turn6’s table are consistent with these formulas. The theorem is symbolic; the existing receipt does not itself contain the flat-splitting checks.

---

## 7. Actual denominator exclusions and logarithmic restoration

### 7.1 A direct local denominator identity

The weighted rational center is


$$
c_\lambda
=\frac ak\frac{v_0}{u_0}
+\left(1-\frac ak\right)\frac{v_3}{u_3}.
$$


Substitution gives the exact identity


$$
\boxed{
c_\lambda
=-\frac{(XR-ZY)(a-k\Theta)}
{k(n!)^2XZ}.
}
$$


At an eligible prime, all factors other than $k,(n!)^2,a-k\Theta$ are units.

For a reduced weight $a/k$, $k>0$, this proves


$$
v_p(q_\lambda)=
\begin{cases}
2N_p-\min\{2N_p,v_p(a-k\Theta)\},&p\nmid k,\\
2N_p+v_p(k),&p\mid k.
\end{cases}
$$


Here $v_p(0)=+\infty$. This is the valuation of the reduced rational denominator, so it already includes the full local gcd.

### 7.2 Simplified-target exclusions

If $p\nmid k$ and


$$
v_p(a-k\Theta^{\mathrm{flat}})>N_p,
$$


then unequal-depth subtraction gives


$$
v_p(a-k\Theta)=N_p,
$$


and therefore


$$
\boxed{v_p(q_\lambda)=N_p.}
$$



For


$$
\Theta^{[1]}=\Theta^{\mathrm{flat}}+n!\mathfrak u_n,
$$


the smooth-family congruences give


$$
v_p(F(n)-1)=w_p,
$$


where


$$
w_3=r,\qquad w_5=r+1,\qquad w_7=r.
$$


The logarithmic prefix has strictly greater depth on these families. Consequently


$$
v_p(\Theta-\Theta^{[1]})=N_p+w_p.
$$


A reconstruction of $\Theta^{[1]}$ to strictly greater depth therefore leaves


$$
\boxed{v_p(q_\lambda)=N_p-w_p.}
$$



The full-gcd allocations also follow. When $0<w_p<2N_p$, the reduced endpoint data have local depths


$$
v_p(h)=2N_p-w_p,\quad v_p(A)=0,\quad v_p(B)=w_p,
$$


while the relevant reduced companion coordinates and $J$ are units. On the deep resonant branch,


$$
v_p(F_{\rm gcd})=w_p,\qquad v_p(G)=0,
$$


and


$$
v_p(H_{\rm gcd})
=\min\{2N_p-w_p,\ v_p(a-k\Theta)-w_p\}.
$$


This gives exactly the source’s allocations.

These are exclusions of two specified wrong targets, not exclusions of short reconstruction of the correct residue.

### 7.3 Complete logarithmic force

Every logarithmic force summand is


$$
2q_j(n+i)!\,n!
\binom{2n+i-j}{n}\frac{\alpha_{r-1}}r,
\qquad r\le2n+2.
$$


Because $i=0,1,2<p$, $p\mid n$, and $\alpha_j,q_j$ are $p$-integral,


$$
v_p((n+i)!)=N_p,
$$


and hence


$$
w-w^{\exp}\in p^{K_p}\mathbb Z_{(p)}^3,
\qquad
K_p=2N_p-\lfloor\log_p(2n+2)\rfloor.
$$


The integral inverse carries this to the complete endpoints.

On the stated families, $K_p\ge1$, so the exponential-only endpoint data retain the necessary unit conditions and the exterior $+1$. The residue denominators are units, yielding


$$
\Theta-\Theta^{\exp}\in p^{K_p}\mathbb Z_{(p)}.
$$



For $p\nmid k$, clipped reconstruction depths can consequently differ by at most


$$
2N_p-K_p=\lfloor\log_p(2n+2)\rfloor.
$$


For $p\mid k$, both denominator exponents equal $2N_p+v_p(k)$.

Thus


$$
\boxed{
|v_p(q_\lambda)-v_p(q_\lambda^{\exp})|
\le\lfloor\log_p(2n+2)\rfloor.
}
$$


Multiplication over a fixed selected set gives


$$
\boxed{
B_{\mathcal P}(n)^{-1}
\le\frac{(q_\lambda)_{\mathcal P}}
{(q_\lambda^{\exp})_{\mathcal P}}
\le B_{\mathcal P}(n)
\le(2n+2)^{|\mathcal P|}.
}
$$



The restriction to a fixed selected set is essential. Nothing here bounds the accumulated contribution of unselected primes.

### 7.4 Terminal boundary identity

At recurrence index $N=n+1$,

- the coefficient containing $N-n-1$ vanishes;
- $[z^{n+1}]R_n=0$.

Thus


$$
\boxed{
w_2-(2n+3)w_1+\frac{(n+1)(n+2)}2w_0
=\mathcal B_{n+1}^{[n+1]}.
}
$$


The same linear functional annihilates $z$ and $w^{\log}$ separately.

This uses exactly the original three contact coefficients. It does not extend the inverse past its finite boundary.

---

## 8. A further consequence: sharper endpoint-sensitive denominator stability

The logarithmic-restoration theorem can be sharpened without changing the weight or discarding any force.

Let


$$
\delta Y=Y-Y^{\exp},\qquad
\delta R=R-R^{\exp},
$$


and write


$$
\mathscr D=XR-ZY,\qquad
\mathscr D^{\exp}=XR^{\exp}-ZY^{\exp}.
$$


Direct subtraction gives


$$
\boxed{
\Theta-\Theta^{\exp}
=
\frac{XZ\bigl(R^{\exp}\delta Y-Y^{\exp}\delta R\bigr)}
{\mathscr D\,\mathscr D^{\exp}}.
}
$$



At an eligible prime, the outside factors and $R^{\exp}$ are units. Since $\Delta$ is a unit,


$$
v_p(\delta Y)=v_p(v_0-v_0^{\exp}),\qquad
v_p(\delta R)=v_p(v_3-v_3^{\exp}).
$$


Put


$$
L_p=
\min\left\{
v_p(v_0-v_0^{\exp}),
\ v_p(v_0^{\exp})+v_p(v_3-v_3^{\exp})
\right\}.
$$


Then


$$
\boxed{v_p(\Theta-\Theta^{\exp})\ge L_p.}
$$



Applying the same clipped-depth argument proves the stronger stability estimate


$$
\boxed{
|v_p(q_\lambda)-v_p(q_\lambda^{\exp})|
\le
2N_p-\min\{2N_p,L_p\}.
}
$$


For $p\mid k$, the difference remains zero.

This is a new rigorous consequence of the supplied determinant formulas. It explains why restoring the logarithmic force may cost fewer digits than the universal $d_p$-bound.

For example, the receipt certifies at $n=15,p=3$


$$
v_3(v_0-v_0^{\exp})=10,\qquad K_3=9,\qquad
v_3(v_0^{\exp})=1.
$$


The whole-force strip gives


$$
v_3(v_3-v_3^{\exp})\ge9.
$$


Therefore $L_3\ge10$, and the distortion bound improves from $3$ to $2$ at this input.

This improvement is finite at that input. The endpoint-sensitive lemma itself is general under its explicit unit hypotheses.

---

# Part III. Finite certification and remaining proof obligations

## 9. What the supplied receipt establishes

The supplied personally authored code retains:

- complete coefficients through force index $2n+2$;
- the initial value $\mathcal W_n$;
- the polynomial forcing $R_n$;
- original contact rows and columns $0,1,2$;
- the endpoint exterior $+1$;
- comparison with the previously supplied full-column endpoints;
- reduced-weight conditions and exact primitive reduction for any returned candidate.

It independently compares the recurrence with the complete finite coefficient sum through $N=n+2$. The recorded counts $18,33,108,213$ are $n+3$, as expected.

The empty-window calculation uses a conservative rational enclosure of the algebraic window. Therefore emptiness of its outer search region certifies emptiness of the intended window. The result is:

- four specified producer indices;
- the specified selected sets and three moduli;
- height at most $n^3$;
- window radius $16$;
- selected-prime-unit denominators;
- all 18 lists empty.

It proves no infinite absence theorem, no general polynomial-height exclusion, and no all-prime asymptotic statement.

Because all lists are empty, the candidate-specific full-gcd and whole-form code was not exercised on a candidate by these windows. This does not diminish the certified emptiness, but it limits what those branches certify.

---

## 10. Concrete next lemma and bounded exact checks

### 10.1 Next binary lemma

The positive-shift tail obstruction is now controlled. The next genuine binary obligation is:

> **Complete low-shift contraction lemma.**  
> At a requested raw precision $M$, evaluate the retained norm and mixed contractions after the proved positive-shift truncation, with complete coefficient producers, actual binomial units, the shortened block, the separate endpoint, and the complete second force. Prove the required scalar residue rather than only a valuation bound on deleted terms.

For the norm target


$$
\sum_{j=0}^bA_j^2-8S(C,D)\pmod{2^{2\mu+6}},
$$


a sufficient first-column truncation precision is


$$
T>a,\qquad T+a+1\ge2\mu+6.
$$


A raw mixed target of precision $M$ requires


$$
T+c\ge M.
$$



A finite number of retained shift labels does not yet make this a bounded-degree computation independent of the actual index.

### 10.2 Next A3 lemma

The correct remaining reconstruction target is


$$
a-k\Theta^{\exp,\mathrm{flat}}
-k n!\mathfrak u_n^{\exp}F(n)
\equiv0\pmod{L_{\mathrm{strip}}},
$$


together with a fixed-width threshold window and a proved height bound on an infinite original smooth family.

On the stated families, $N_p>d_p$, so the two-stage formulation is valid. The division by $kn!\mathfrak u_n^{\exp}$ is performed only after lower-half divisibility has been established, and with $p\nmid k$. There is no premature inversion of a nonunit factorial.

The missing theorem is an infinite-family construction or exclusion for this **actual moving residue**, not a uniqueness theorem for arbitrary rational reconstruction.

### 10.3 Bounded arithmetic worth inspecting

No repetition of the 18 empty searches is needed.

A useful augmentation at


$$
n=15,30,105,210
$$


is:

1. Run the same complete recurrence with initial value zero.
2. Verify exactly
   

$$
w-w^{\mathrm{flat}}-\eta_nz=0.
$$


3. Verify the three terminal identities and invariant determinant.
4. Verify the exact residue decomposition and the ten middle-depth outputs in A3turn6.
5. Compute both endpoint differences
   

$$
v_0-v_0^{\exp},\qquad v_3-v_3^{\exp},
$$


   and return $L_p$ from Section 8.
6. Return the exact determinant residual
   

$$
(\Theta-\Theta^{\exp})\mathscr D\mathscr D^{\exp}
   -XZ(R^{\exp}\delta Y-Y^{\exp}\delta R),
$$


   whose expected value is zero.

For a non-vacuous bounded denominator check, use, for example, the fixed reduced weights


$$
0,\quad1,\quad\frac12,\quad\frac13,\quad\frac15,\quad\frac17
$$


at those four inputs. These are normalization probes, not threshold candidates. For each, compare direct rational reduction with the full endpoint-gcd formula and the universal and refined selected-prime distortion bounds.

Expected outputs are exact rational identities, exact reduced numerators and denominators, full gcd factors, and selected-prime valuations. No analytic irrationality conclusion follows from these probes.

---

## 11. Primitive arithmetic and whole error remain unchanged

For the binary construction, retain the least actual clearer $d_B$, both complete columns, and


$$
A_B=N_{B,1}^{T}\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^{T}\Omega N_{B,2}\ne0.
$$


The final reduction remains


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
}
$$


This gcd includes every odd prime. The primitive multiplier is still $d_B^2/g_B$.

The whole evaluated error remains


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n>0
\quad\text{eventually},
}
$$


where


$$
\log|\epsilon_n|
=
-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$



For A3, the actual full reduction remains


$$
\boxed{
q_\lambda=\frac{kh|AB|}{F_{\rm gcd}GH_{\rm gcd}},\qquad
p_\lambda=\operatorname{sgn}(AB)
\frac{T}{F_{\rm gcd}GH_{\rm gcd}},
}
$$


with every gcd hypothesis retained. Its whole evaluated form is


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=q_\lambda e_3\alpha_{n,2}
(\lambda-\Lambda_{n,2}).
}
$$


An irrationality argument requires a same-index family for which


$$
0<
q_\lambda|e_3\alpha_{n,2}|
\,|\lambda-\Lambda_{n,2}|
\longrightarrow0.
$$


Selected-prime cancellation and a finite-order threshold expansion do not establish this.

---

## Final proof-status ledger

### Results passing this audit

1. Weighted complete-force first differences with the scalar $C_{i,\ell}$ preserved.
2. Divided-power symbol integrality in the correct coefficient lattice.
3. Complete differentiated-word control at every force, symbol, bulk, suffix, and endpoint position.
4. The coefficient weight $\beta_r$, root-product compensation, and complete normalized positive-shift tail decay.
5. Actual first-column content-relative truncation, with the endpoint retained exactly.
6. Correct raw norm and mixed factors $4N$ and $8H$.
7. Exact homogeneous/flat splitting and invariant determinant.
8. The nonzero middle factorial-depth digit and the two specified simplified-target exclusions.
9. Polynomial selected-prime denominator distortion under restoration of the complete logarithmic force.
10. The exact terminal contact identity.

### Further consequence proved here

The endpoint-sensitive determinant identity yields a potentially sharper local denominator-distortion bound:


$$
|v_p(q_\lambda)-v_p(q_\lambda^{\exp})|
\le
2N_p-\min\{2N_p,L_p\},
$$


with $L_p$ defined from the two complete endpoint differences.

### Exact remaining bottleneck

For the binary route, the next obstacle is the complete, unit-sensitive low-shift norm and mixed contraction at variable precision.

For A3, it is an infinite-family height theorem for the correct forced moving residue, including its shifted-factorial scalar.

For both routes, the unresolved global obligations are the **full all-prime primitive denominator**, the **actual relative scalar**, and a **whole evaluated form that is nonzero and tends to zero on the same original indices**.



$$
\boxed{\text{No unconditional proof or disproof of irrationality of }e+\pi
\text{ is obtained.}}
$$


