> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, turn 2 — Integral transport of the actual single-summand target

## Executive conclusion

The new short-polynomial certificate changes the problem substantially. I use it at precisely its certified scope: the original index, the complete corrected columns, and physical precision $2^{20}$. I do not reopen the head, contact, Laurent, reconstruction, or Schur calculations.

There are three advances.

1. **The new telescoping boundary is exactly zero.**  
   With the artificial shift removed, $L=b$, so the upper boundary contains $(L-b)^2=0$. This is an exact consequence of the new summand, not an omission of the physical endpoint or its exterior $+1$.

2. **An integer-valued normalization reduces the kernel guards from $321,315$ to $14,16$, without evaluating or dividing a moment by a nonunit.**  
   In the binomial-polynomial lattice,
   

$$
\frac{U_f}{2^{73}},\qquad \frac{U_e}{2^{68}}
$$


   are integral integer-valued polynomials. Consequently the two Gram contractions can be recovered from integral scalar sums at only
   

$$
\boxed{34\text{ and }36\text{ kernel bits}.}
$$


   These bounds require no additional physical-force precision.

3. **Those scalar sums have a practical, explicitly bounded binary transport.**  
   I derive a division-free polynomial/carry algorithm for this factorial ratio. Along the actual 71-digit word:
   - there are at most **four reachable carry states** at any digit;
   - each state contains one integer-valued polynomial per requested observable;
   - the polynomial degree is at most $228$ in a uniform initial envelope;
   - after eight digits, the degrees are at most $66$ and $70$, respectively;
   - all divisions during transport are inversions of proved odd units.

Thus this report supplies the outstanding **practical integral observable-transport lemma**, rather than another unevaluated fraction-free identity involving a 341-bit moment.

I have not executed the new contraction. No numerical Gram residue, actual norm depth, or all-prime primitive denominator is claimed. The new bounded computation at the end uses only the attached short data and elementary kernel arithmetic.

---

## 1. Fixed original problem and accepted inputs

Retain


$$
b=150094635296999121,\qquad
n=600678730458590482242=4002b,
$$




$$
N=n+2,\qquad a=2n,\qquad q=2^{20}.
$$



The physical reconstructed rows are exactly


$$
0\le j\le b,
$$


with


$$
W_j=\binom Nj.
$$


The reversed coefficient index is


$$
k=b-j.
$$



The accepted complete reconstructed series are


$$
F(z)=\frac{A_f(z)}{(1-z)^{a+81}},
\qquad
E(z)=\frac{A_e(z)}{(1-z)^{a+77}}
\pmod q,
\tag{1.1}
$$


where


$$
\deg A_f=81,\qquad \deg A_e=77.
$$



Here $E$ already includes the complete second force, finite Schur return, terminal factorial cancellation, and physical exterior $+1$. None is to be added again.

Writing


$$
F_k=[z^k]F,\qquad E_k=[z^k]E,
$$


the common signed-reversal factors cancel in the products, giving


$$
D_{\rm raw}\equiv
\sum_{j=0}^{b}W_j^2F_{b-j}^{\,2}\pmod q,
\tag{1.2}
$$




$$
E_{\rm raw}\equiv
\sum_{j=0}^{b}W_j^2F_{b-j}E_{b-j}\pmod q.
\tag{1.3}
$$



There is no unspecified weight clearer in these formulas.

### 1.1 Evidence used, without extending its scope

The supplied source and receipt certify:

- both discarded $n$-branches vanish coefficientwise modulo $2^{20}$;
- the complete reconstructed numerators have the certified $z^{176}$ factors;
- the $44$ and $48$ divisions by $1-z$ have zero remainders;
- the short degrees are $81,77$;
- the normalized payload degrees are $162,158$;
- the two full polynomial moment identities hold modulo $2^{341}$;
- the corrected unsaturated guards are $321,315$, not $321,313$;
- no original Gram pair was evaluated.

The twelve bounded conversion checks corroborate the shift conversion at their twelve stated inputs. The general conversion itself is justified by the factorial identity, not by extrapolating those checks.

I do not extend any of these physical-column assertions beyond twenty bits.

---

## 2. The actual single summand and its zero boundary

Define


$$
H(k)=\binom{a+k-1}{k},
$$


and


$$
T(j)=\binom Nj^{\!2}H(b-j)^2
=
\binom Nj^{\!2}
\binom{a+b-j-1}{b-j}^{\!2},
\qquad 0\le j\le b.
\tag{2.1}
$$



For $\alpha=f,e$, let


$$
R_f=81,\qquad R_e=77,
$$




$$
D_\alpha=(a)^{\overline{R_\alpha}},
$$


and retain the supplied integral polynomials


$$
U_\alpha(j)=
\sum_{r=0}^{R_\alpha}
A_{\alpha,r}
(b-j)_{\underline r}
(a+b-j)^{\overline{R_\alpha-r}}.
\tag{2.2}
$$



The exact shift conversion for integer lifts of the short coefficients is


$$
F_{b-j}=\frac{U_f(j)}{D_f}H(b-j),
\qquad
E_{b-j}=\frac{U_e(j)}{D_e}H(b-j).
\tag{2.3}
$$



Therefore the lifted contractions are


$$
\widetilde D=
\frac{1}{D_f^2}\sum_{j=0}^{b}T(j)U_f(j)^2,
\tag{2.4}
$$




$$
\widetilde E=
\frac{1}{D_fD_e}\sum_{j=0}^{b}T(j)U_f(j)U_e(j).
\tag{2.5}
$$



They are integers, and


$$
\widetilde D\equiv D_{\rm raw},\qquad
\widetilde E\equiv E_{\rm raw}\pmod q.
\tag{2.6}
$$



Changing a short coefficient by a multiple of $q$ changes each reconstructed coefficient by a multiple of $q$, so this use of integer lifts is legitimate.

### 2.1 The new boundary observable

Put


$$
\mathcal A(j)=(N-j)^2(b-j)^2,
\qquad
\mathcal B(j)=j^2(a+b-j)^2,
$$


and


$$
\Delta R(j)=\mathcal A(j)R(j+1)-\mathcal B(j)R(j).
\tag{2.7}
$$



For $0\le j<b$,


$$
T(j)\mathcal A(j)=T(j+1)\mathcal B(j+1).
$$


Consequently


$$
\sum_{j=0}^{b}T(j)\Delta R(j)
=
T(b)\mathcal A(b)R(b+1)
-
T(0)\mathcal B(0)R(0).
\tag{2.8}
$$



Both terms are exactly zero:


$$
\mathcal B(0)=0,\qquad
\mathcal A(b)=(N-b)^2(b-b)^2=0.
$$



Thus


$$
\boxed{\sum_{j=0}^{b}T(j)\Delta R(j)=0.}
\tag{2.9}
$$



The formal upper-boundary observable remains


$$
\mathcal E=T(b)\mathcal A(b),
$$


but its actual value is now


$$
\boxed{\mathcal E=0.}
\tag{2.10}
$$



This does **not** erase the physical $j=b$ row. That row is present in (1.2)–(1.3), and its exterior correction is already embedded in $A_e$.

In particular, the supplied nonzero residues named `boundary_R_b1` are values of $R(b+1)$, not nonzero boundary contributions. They are multiplied by the exact zero $\mathcal E$.

---

## 3. The short presentations and their nonunit components

For degree $D$, retain the presentation with generators


$$
1,j,\ldots,j^D,\mathcal E
$$


and relation columns


$$
\Delta j^k-(b+1)^k\mathcal E,
\qquad 0\le k\le D-3.
\tag{3.1}
$$



The two required matrices are exactly


$$
\boxed{164\times160\quad(D=162),}
$$




$$
\boxed{160\times156\quad(D=158).}
$$



The leading coefficient of $\Delta j^k$ is


$$
k+\tau,\qquad \tau=a-4=2n-4,
$$


so the rational column ranks are $160,156$.

Modulo $2$,


$$
\mathcal A(j)\equiv\mathcal B(j)\equiv j^2(j+1)^2,
$$


and hence


$$
\Delta R\equiv
j^2(j+1)^2\bigl(R(j+1)-R(j)\bigr).
\tag{3.2}
$$



The same finite-dimensional argument as in turn 1 now gives:

| Payload | Matrix | Binary rank | Nonunit Smith pivots | Sum of their valuations, at most |
|---|---:|---:|---:|---:|
| $U_f^2$ | $164\times160$ | $81$ | $79$ | $161$ |
| $U_fU_e$ | $160\times156$ | $79$ | $77$ | $158$ |

These are the checks appropriate for the coordinator’s one planned Smith inspection.

### 3.1 What saturation does—and does not—permit

Suppose an exact relation implies


$$
2^s L=0
$$


after evaluation in $\mathbb Z_2$. Since $\mathbb Z_2$ is torsion-free, the evaluated $L$ is zero. Thus exact telescoping relations may be saturated when their exact vanishing has been established.

But the finite congruence


$$
2^s x\equiv0\pmod{2^p}
$$


does not imply $x\equiv0\pmod{2^p}$. It implies only


$$
x\equiv0\pmod{2^{p-s}}.
$$



The transport below does not confuse these statements. It does not divide by a Smith pivot, and it does not discard a nonunit coordinate. It evaluates the actual payloads directly in an integral function lattice containing all the monomial observables in the two presentations.

The Smith images remain useful diagnostics. They are no longer a prerequisite for paying hundreds of kernel guard bits.

---

## 4. Integer-valued normalization: the guards become $14,16$

Let


$$
\operatorname{Int}_{\le d}(\mathbb Z)
=
\left\{
P\in\mathbb Q[j]:
\deg P\le d,\ P(\mathbb Z)\subseteq\mathbb Z
\right\}.
$$



Its standard integral basis is


$$
\binom j0,\binom j1,\ldots,\binom jd.
$$


The coordinates are forward differences:


$$
P(j)=\sum_{r=0}^{d}\Delta_{\!+}^{\,r}P(0)\binom jr.
\tag{4.1}
$$



This basis does not require modular division by $r!$.

### Lemma 1 — Fixed divisors of the shift-conversion polynomials

For the actual $R_f=81,R_e=77$,


$$
\boxed{
P_f:=U_f/2^{73}\in\operatorname{Int}_{\le81}(\mathbb Z),
}
\tag{4.2}
$$




$$
\boxed{
P_e:=U_e/2^{68}\in\operatorname{Int}_{\le77}(\mathbb Z).
}
\tag{4.3}
$$



#### Proof

For every integer $k$,


$$
k_{\underline r}
(a+k)^{\overline{R-r}}
=
r!(R-r)!
\binom kr
\binom{a+k+R-r-1}{R-r}.
\tag{4.4}
$$


The two generalized binomial coefficients are integers. Hence each summand has fixed divisor at least


$$
2^{\min_{0\le r\le R}\{v_2(r!)+v_2((R-r)!)\}}.
$$



Now


$$
v_2(r!)+v_2((R-r)!)
=
v_2(R!)-v_2\binom Rr.
$$


For $R=81,77$, the largest binomial valuation is $5$. Indeed, these are odd numbers below $128$, so carries can occur only at positions $1,\ldots,5$; the maximum is attained by


$$
81=18+63,\qquad 77=14+63.
$$


Also


$$
v_2(81!)=78,\qquad v_2(77!)=73.
$$


The fixed-divisor exponents are therefore $73,68$.

Every summand in (2.2) has the asserted fixed divisor. Division yields an integer-valued polynomial, and its forward-difference coordinates are integers. ∎

These are sufficient universal divisors. I do not claim that they are the maximal fixed divisors of the actual arrays.

### 4.1 Exact scalar identities with small guards

Use the accepted valuations


$$
v_2(D_f)=80,\qquad v_2(D_e)=77,
$$


and write


$$
D_f=2^{80}d_f,\qquad D_e=2^{77}d_e,
$$


where $d_f,d_e$ are odd.

Define the integral observables


$$
S_{ff}=\sum_{j=0}^{b}T(j)P_f(j)^2,
$$




$$
S_{fe}=\sum_{j=0}^{b}T(j)P_f(j)P_e(j).
\tag{4.5}
$$



Equations (2.4)–(2.5) become


$$
\boxed{S_{ff}=2^{14}d_f^2\,\widetilde D,}
\tag{4.6}
$$




$$
\boxed{S_{fe}=2^{16}d_fd_e\,\widetilde E.}
\tag{4.7}
$$



Therefore


$$
\boxed{
D_{\rm raw}\equiv
d_f^{-2}\frac{S_{ff}}{2^{14}}\pmod{2^{20}},
}
\tag{4.8}
$$




$$
\boxed{
E_{\rm raw}\equiv
(d_fd_e)^{-1}\frac{S_{fe}}{2^{16}}\pmod{2^{20}}.
}
\tag{4.9}
$$



The divisions by $2^{14}$ and $2^{16}$ are justified by the exact integer identities (4.6)–(4.7). They are not modular inversions.

It suffices to evaluate


$$
\boxed{S_{ff}\pmod{2^{34}},\qquad S_{fe}\pmod{2^{36}}.}
\tag{4.10}
$$



This removes two named obstructions:

- the $161,158$ pivot-product losses are not incurred;
- the shift-normalization losses $160,157$ are reduced to $14,16$ by using the correct integer-valued lattice.

No 341-bit moment remains in the proposed evaluation.

### 4.2 Constructing these payloads from the retained arrays

No source calculation is needed.

For $P_f$, evaluate the supplied $U_f$ at $0,\ldots,81$, form forward differences, and divide the differences by $2^{73}$. For $P_e$, use $0,\ldots,77$ and divide by $2^{68}$.

To obtain them modulo $2^{36}$, it is enough to use $U_f$ modulo $2^{109}$ and $U_e$ modulo $2^{104}$. Both are already available inside the retained 341-bit arrays.

Form


$$
P_f^2\in\operatorname{Int}_{\le162}(\mathbb Z),
\qquad
P_fP_e\in\operatorname{Int}_{\le158}(\mathbb Z)
$$


by evaluations and forward differences. Every operation is integral.

---

# Part II. A bounded integral binary transport

## 5. An elementary odd-factorial polynomial lemma

Define


$$
g(h)=\prod_{r=1}^{h}(2r-1),\qquad h\ge0,
$$


with $g(0)=1$.

Thus


$$
(2h+\epsilon)!
=
2^h h!\,g(h+\epsilon),
\qquad \epsilon\in\{0,1\}.
\tag{5.1}
$$



The following quantitative fact is the key to a small module.

### Lemma 2 — Low-degree integer-valued approximation of odd factorials

For every $p\ge1$, the function $g(h)$ modulo $2^p$ is represented by an integer-valued polynomial of degree at most


$$
2p-2.
$$



More precisely, if


$$
g(h)=\sum_{r\ge0}\gamma_r\binom hr
$$


is its Newton expansion on nonnegative integers, then


$$
\boxed{v_2(\gamma_r)\ge\lceil r/2\rceil\quad(r\ge1).}
\tag{5.2}
$$



#### Proof

The exponential generating function is


$$
\sum_{h\ge0}g(h)\frac{t^h}{h!}=(1-2t)^{-1/2}.
$$


Binomial inversion gives


$$
\sum_{r\ge0}\gamma_r\frac{t^r}{r!}
=
e^{-t}(1-2t)^{-1/2}.
$$


Its logarithm is


$$
-t-\frac12\log(1-2t)
=
\sum_{m\ge2}\frac{2^{m-1}}m t^m
=
\sum_{m\ge2}2^{m-1}(m-1)!\frac{t^m}{m!}.
$$



The exponential formula expresses $\gamma_r$ as a sum over partitions of an $r$-element set having no singleton blocks, with a block of size $m$ contributing


$$
2^{m-1}(m-1)!.
$$


A partition with $s$ blocks contributes a multiple of $2^{r-s}$, and $s\le\lfloor r/2\rfloor$. Thus every contribution is divisible by


$$
2^{r-\lfloor r/2\rfloor}=2^{\lceil r/2\rceil}.
$$


This proves (5.2).

Terms with $r\ge2p-1$ vanish modulo $2^p$. ∎

### 5.1 Translation, negative arguments, products and reciprocals

Modulo $2^p$, write the preceding polynomial in valuation layers:


$$
g(h)=\sum_{\nu=0}^{p-1}2^\nu G_\nu(h),
\qquad
G_\nu\in\operatorname{Int}_{\le2\nu}(\mathbb Z).
\tag{5.3}
$$



The same degree-by-valuation bound holds for:

- $g(K+h)$ and $g(K-h)$, for every integer $K$;
- finite products of such functions;
- their reciprocals;
- their squares and inverse squares.

Translation preserves integer-valuedness and does not increase degree. Products preserve the bound because degrees and valuations add.

Every value of $g$ is odd. Since $g\equiv1\pmod2$, its reciprocal is obtained from the finite geometric expansion in $g-1$; this also preserves the bound.

For negative arguments, use the unique odd-unit extension determined by


$$
g(h+1)=(2h+1)g(h).
\tag{5.4}
$$


The same truncated Newton polynomial represents that extension. The recurrence follows modulo $2^p$ as an integer-valued polynomial identity, since it holds at every nonnegative integer.

Thus evaluating these correction factors never requires division by an even number.

---

## 6. The exact factorial-ratio states

Put


$$
c=a-1=2n-1,\qquad S=c+b.
$$


Then


$$
T(j)=
\left(
\frac{N!\,(S-j)!}
{c!\,j!\,(N-j)!\,(b-j)!}
\right)^2.
\tag{6.1}
$$



For a digit position $t$, let


$$
N_t=\left\lfloor\frac N{2^t}\right\rfloor,\quad
b_t=\left\lfloor\frac b{2^t}\right\rfloor,\quad
c_t=\left\lfloor\frac c{2^t}\right\rfloor,\quad
S_t=\left\lfloor\frac S{2^t}\right\rfloor.
$$



After a lower-bit prefix $r$, $0\le r<2^t$, has been selected, write


$$
j=r+2^t h.
$$


Introduce the three borrow flags


$$
\lambda_C=
\begin{cases}
1,&r>C\bmod 2^t,\\
0,&r\le C\bmod 2^t,
\end{cases}
\qquad C=N,b,S.
\tag{6.2}
$$



The remaining factorial ratio is


$$
R_{t,\lambda}(h)=
\frac{N_t!\,(S_t-\lambda_S-h)!}
{c_t!\,h!\,(N_t-\lambda_N-h)!\,(b_t-\lambda_b-h)!}.
\tag{6.3}
$$



For valid original $j$, all factorial arguments along this decomposition are nonnegative.

### 6.1 At most four reachable states

Although three flags admit eight formal bit patterns, at a fixed $t$ they are threshold functions of the same $r$. Sort


$$
N\bmod2^t,\quad b\bmod2^t,\quad S\bmod2^t.
$$


As $r$ increases, a flag changes only when its threshold is crossed.

Therefore


$$
\boxed{\text{at most four borrow states are reachable at any digit}.}
\tag{6.4}
$$



Coincident thresholds reduce this number further. This bound is exact and target-specific; it is not an empirical reachable-state count.

---

## 7. One binary transition, with all powers of two explicit

Choose the next bit


$$
h=2h'+\epsilon,\qquad \epsilon\in\{0,1\}.
$$



Let $\nu_C$ denote the current low bit of $C_t$. For $C=N,b,S$,


$$
\lambda_C'
=
\mathbf1_{\epsilon+\lambda_C>\nu_C},
\tag{7.1}
$$


and


$$
\eta_C=\nu_C-\lambda_C-\epsilon+2\lambda_C'\in\{0,1\}.
\tag{7.2}
$$



Also put


$$
\kappa_{t+1}=S_{t+1}-c_{t+1}-b_{t+1}\in\{0,1\}.
$$


The factorial power of two contributed at this digit is


$$
d_t=\kappa_{t+1}+\lambda_N'+\lambda_b'-\lambda_S'.
\tag{7.3}
$$



For reachable states,


$$
\lambda_N'\in\{0,1\},
\qquad
\kappa_{t+1}+\lambda_b'-\lambda_S'\in\{0,1\},
$$


so


$$
\boxed{d_t\in\{0,1,2\}.}
\tag{7.4}
$$



Applying (5.1) to all six factorials gives


$$
R_{t,\lambda}(2h'+\epsilon)^2
=
2^{2d_t}\,
G_{t,\lambda,\epsilon}(h')\,
R_{t+1,\lambda'}(h')^2,
\tag{7.5}
$$


where the odd correction is explicitly


$$
\boxed{
G_{t,\lambda,\epsilon}(h)=
\left[
\frac{
g(N_{t+1}+\nu_N)\,
g(S_{t+1}-\lambda_S'+\eta_S-h)
}{
g(c_{t+1}+\nu_c)\,
g(h+\epsilon)\,
g(N_{t+1}-\lambda_N'+\eta_N-h)\,
g(b_{t+1}-\lambda_b'+\eta_b-h)
}
\right]^2.
}
\tag{7.6}
$$



By Lemma 2 and §5.1,


$$
G_{t,\lambda,\epsilon}(h)
=
\sum_{\nu=0}^{p-1}2^\nu
G_{t,\lambda,\epsilon,\nu}(h)
\pmod{2^p},
$$


with


$$
\deg G_{t,\lambda,\epsilon,\nu}\le2\nu.
\tag{7.7}
$$



Every denominator in (7.6) is odd. There is no hidden nonunit division.

---

## 8. Observable transport and its terminal evaluation

For an integer-valued payload $P$, initialize


$$
P_{0,(0,0,0)}(h)=P(h),
$$


with all other states zero.

The update is


$$
\boxed{
P_{t+1,\lambda'}(h)
\mathrel{+}=
2^{2d_t}
G_{t,\lambda,\epsilon}(h)
P_{t,\lambda}(2h+\epsilon)
\pmod{2^p}.
}
\tag{8.1}
$$



At every step, states with the same new borrow flags are added.

This is the integral transport map. It applies to:

- the two actual normalized payloads;
- every monomial moment in the short presentations;
- any integral linear combination supplied by their Smith-coordinate inspection.

It does not assume that section maps preserve the original polynomial-telescoping quotient. Instead, it transports the observable and the factorial-ratio state together.

### Theorem 3 — Exact terminal contraction

For $p\ge1$ and $P\in\operatorname{Int}(\mathbb Z)$, after the 71 transitions,


$$
\boxed{
P_{71,(0,0,0)}(0)
=
\sum_{j=0}^{b}T(j)P(j)
\pmod{2^p}.
}
\tag{8.2}
$$



#### Proof

Repeatedly apply the exact factorization (7.5). Each path chooses the 71 binary digits of $j$, and its transported polynomial accumulates the exact odd factors and powers of two in $T(j)$, together with the original $P(j)$.

All four constants $N,b,c,S$ are below $2^{71}$. At the terminal digit, $h=0$.

The terminal flag $\lambda_b=0$ is exactly the condition $j\le b$. Since $b<N,S$, a valid $j$ also has $\lambda_N=\lambda_S=0$. Conversely, terminal state $(0,0,0)$ implies $j\le b$.

For an accepted path, all terminal factorials are $0!=1$, so the terminal remaining ratio is $1$. Thus the accepted state sums exactly the original range $0,\ldots,b$. ∎

This proves the finite cutoff directly. It is neither an infinite sum nor a standard full Hahn replacement.

---

## 9. The section maps preserve a small actual module

The key section identity is


$$
\binom{2h+\epsilon}{r}
=
\sum_{u=0}^{r}
C_{\epsilon}(r,u)\binom hu,
\tag{9.1}
$$


where


$$
C_{\epsilon}(r,u)
=
[z^r](1+z)^\epsilon(2z+z^2)^u.
\tag{9.2}
$$



These coefficients are integers, and


$$
\boxed{
v_2(C_\epsilon(r,u))\ge\max(0,2u-r).
}
\tag{9.3}
$$



Indeed, for $\epsilon=0$, the nonzero term is


$$
2^{2u-r}\binom{u}{r-u}.
$$


For $\epsilon=1$, add the analogous contribution from $r-1$. Each nonzero term has the asserted valuation.

### Theorem 4 — Uniform degree-by-valuation bound

Suppose the initial payload has degree at most $D$. At digit $t$, each transported state admits a valuation-layer representation


$$
P_{t,\lambda}(h)
=
\sum_{\nu=0}^{p-1}2^\nu P_{t,\lambda,\nu}(h)
\pmod{2^p},
$$


such that


$$
\boxed{
\deg P_{t,\lambda,\nu}
\le
\left\lfloor\frac D{2^t}\right\rfloor+2\nu.
}
\tag{9.4}
$$



#### Proof

The assertion holds initially.

Consider an input layer $2^\alpha P_\alpha$, of degree at most


$$
D_t+2\alpha,\qquad D_t=\lfloor D/2^t\rfloor.
$$


If sectioning contributes an additional valuation $s$, (9.3) bounds its output degree by


$$
\left\lfloor\frac{D_t+2\alpha+s}{2}\right\rfloor
\le
\left\lfloor\frac{D_t}{2}\right\rfloor+\alpha+s.
$$


Multiplying by correction layer $2^\nu G_\nu$ adds degree at most $2\nu$. Multiplication by $2^{2d_t}$ adds valuation but no degree.

The new layer is $\alpha+s+\nu+2d_t$, and the output degree is at most


$$
\left\lfloor\frac{D_t}{2}\right\rfloor
+
2(\alpha+s+\nu+2d_t).
$$


This is (9.4) at digit $t+1$. Additions and binary carries between layers can only increase the layer index, preserving the bound. ∎

### 9.1 Actual sizes

For $S_{ff}$, take


$$
D=162,\qquad p=34.
$$


For $S_{fe}$, take


$$
D=158,\qquad p=36.
$$



A combined Newton-coefficient array for a state needs degree at most


$$
B_t=\left\lfloor\frac D{2^t}\right\rfloor+2(p-1).
\tag{9.5}
$$



| Observable | Uniform initial degree envelope | Degree after eight digits | Reachable states |
|---|---:|---:|---:|
| $S_{ff}\bmod2^{34}$ | $228$ | $66$ | at most $4$ |
| $S_{fe}\bmod2^{36}$ | $228$ | $70$ | at most $4$ |

Thus, using full-residue Newton arrays, the respective stable storage bounds are


$$
4\cdot67=268,\qquad 4\cdot71=284
$$


residues.

Even the uniform initial envelope uses only


$$
4\cdot229=916
$$


residues per observable. Initially only one state is actually occupied.

These are proved reachable-module bounds, not dense envelopes with millions of unverified states.

### 9.2 Relation to the nonunit Smith components

The transport accepts any integer-valued polynomial of the specified degree. In particular, it contains all the monomial generators and all integral Smith-coordinate combinations of the short presentations.

No nonunit component is discarded. No inference of the form


$$
2^s x=0\pmod{2^p}\Longrightarrow x=0\pmod{2^p}
$$


is used.

The actual boundary observable is transported as the exact scalar zero established in (2.10). The physical endpoint remains in the accepted terminal sum.

This is the required bounded actual module; it is not a claim that a three-state rational quotient is automatically integral.

---

## 10. The explicit original target digits

The original coefficient target after removal of the artificial shift is


$$
(x\text{-index},y\text{-index},u\text{-index},d\text{-index})
=
(b,b,n+2,n).
$$



The following 18-hex-digit words encode the padded 71-bit targets: expand each hexadecimal digit to four bits and delete the first, zero padding bit. Read the result from least significant bit to most significant bit during transport.

| Integer | Exact hexadecimal word |
|---|---|
| $b$ | `0002153e468b91c6d1` |
| $n$ | `2090178ad1dce60f42` |
| $N=n+2$ | `2090178ad1dce60f44` |
| $c=2n-1$ | `41202f15a3b9cc1e83` |
| $S=c+b$ | `41224453ea455de554` |

The factorial transport uses the last four relevant constants $N,b,c,S$, all derived from the same original $b,n$. It does not change the coefficient target or introduce a neighboring index.

At digit $t$, the input bits in (7.1)–(7.6) are explicitly


$$
\nu_C(t)=\left(\left\lfloor C/2^t\right\rfloor\bmod2\right),
\qquad 0\le t<71,
$$


for the displayed constants.

---

## 11. A practical integral implementation

The preceding bounds support a straightforward exact-arithmetic implementation, not a general automaticity citation.

### 11.1 Polynomial representation

Store an integer-valued polynomial as its Newton coefficients


$$
P(h)=\sum_r p_r\binom hr\pmod{2^p}.
$$



Use only:

- modular additions and multiplications;
- forward-difference tables;
- exact generalized binomial coefficients for evaluating a short polynomial at a large integer;
- inverses of odd residues.

No factorial is inverted modulo $2^p$.

### 11.2 Constructing a correction polynomial

For each digit/state/bit transition:

1. Compute the new flags and $d_t$.
2. Evaluate (7.6) at
   

$$
h=0,\ldots,2p-2.
$$


3. Form forward differences to obtain the correction’s Newton coefficients.
4. Check the proved divisibility
   

$$
v_2([{\textstyle\binom h r}]G)\ge\lceil r/2\rceil
   \quad(r>0).
   \tag{11.1}
$$



To evaluate $g(K)$ at a large integer $K$, use the degree-$(2p-2)$ polynomial of Lemma 2. Consecutive values can then be generated from


$$
g(K+1)=(2K+1)g(K)
$$


or its odd-unit inverse.

The largest required degree is $70$. Large-argument binomial evaluation involves only short exact products, not products of length $b$ or $n$.

### 11.3 Updating an observable without rational interpolation

If the current state has degree at most $B_t$, the unreduced product


$$
G(h)P(2h+\epsilon)
$$


has degree at most


$$
L_t=B_t+2p-2.
$$



Compute its values at $0,\ldots,L_t$, then recover its Newton coefficients by finite differences. The coefficients beyond $B_{t+1}$ must vanish modulo $2^p$, by Theorem 4, and can be checked before removal.

For the two runs,


$$
L_t\le294\quad\text{and}\quad L_t\le298.
$$



After the initial contraction, the corresponding bounds are only $132,140$.

### 11.4 Arithmetic scale

There are:

- 71 digits;
- at most four states;
- two outgoing bit transitions per state;
- polynomial tables of length below $300$, rapidly falling below $141$.

A direct forward-table/finite-difference implementation requires on the order of tens of millions of short modular arithmetic operations per observable, plus a small number of short large-argument binomial evaluations. A conservative implementation can remain below $10^8$ such basic table operations for the two observables together, with caching of the common correction data.

The residues have at most 36 bits. Products may use a standard wider intermediate or ordinary arbitrary-precision integers.

The practical claim is therefore supported by explicit state, degree, digit, and arithmetic bounds. It does not depend on an unenumerated large reachable support.

---

## 12. A further exact check: both original columns are even

The accepted parity masks imply


$$
A_f(z)\equiv z^3(1+z)^{78},
\qquad
A_e(z)\equiv(1+z)^{77}\pmod2.
$$


Hence


$$
F(z)\equiv\frac{z^3}{(1+z)^{a+3}},
\qquad
E(z)\equiv\frac1{(1+z)^a}\pmod2.
\tag{12.1}
$$



Here


$$
N\equiv0\pmod4,\qquad b\equiv1\pmod4,\qquad a\equiv4\pmod8.
$$



If $W_j$ is odd, Lucas’ criterion forces $j\equiv0\pmod4$. Then $k=b-j\equiv1\pmod4$.

For $F_k$, the relevant coefficient is


$$
\binom{a+k-1}{k-3}.
$$


The lower index $k-3\equiv2\pmod4$ has bit $1$ set, as does $a+2$. Thus its binomial coefficient is even.

For $E_k$, oddness would require


$$
k\mathbin{\&}(a-1)=0.
$$


But $k$ and $a-1$ are both odd, so this is impossible.

If $W_j$ is even, the weighted coordinate is already even. Therefore


$$
\boxed{
2\mid \mathsf a_j,\qquad 2\mid\mathsf b_j
\quad(0\le j\le b).
}
\tag{12.2}
$$



This proves lower bounds on the actual binary column contents:


$$
a_{\rm cont}\ge1,\qquad c_{\rm cont}\ge1.
$$


It does not identify their exact contents.

Consequently


$$
\boxed{4\mid D_{\rm raw},\qquad4\mid E_{\rm raw}.}
\tag{12.3}
$$



For the new scalar computation, this supplies stronger expected divisibility checks:


$$
\boxed{2^{16}\mid S_{ff},\qquad2^{18}\mid S_{fe}.}
\tag{12.4}
$$



These checks use the complete physical columns and the original weights. No row content has been divided out.

---

## 13. Norm depth and the logarithmic guard

The scalar identities provide an exact norm-depth relation.

If


$$
S_{ff}\not\equiv0\pmod{2^{34}},
$$


then


$$
v_2(\widetilde D)=v_2(S_{ff})-14<20.
$$


Since $\widetilde D\equiv D_{\rm raw}\pmod{2^{20}}$,


$$
\boxed{
v_2(D_{\rm raw})=v_2(S_{ff})-14.
}
\tag{13.1}
$$



Likewise, a nonzero mixed scalar residue gives


$$
\boxed{
v_2(E_{\rm raw})=v_2(S_{fe})-16<20.
}
\tag{13.2}
$$



If either normalized output is zero modulo $2^{20}$, the conclusion is only a lower bound of $20$ for its valuation. The calculation must report that distinction.

Let


$$
d_0=v_2(D_{\rm raw}),\qquad e_0=v_2(E_{\rm raw}).
$$


The ratio interface remains


$$
\frac{H}{N_{\rm ratio}}=\frac{E_{\rm raw}}{2D_{\rm raw}}.
$$



The physical precision requirements remain


$$
M_E\ge s+d_0+1,
\qquad
M_D\ge s+2d_0+1-e_0.
\tag{13.3}
$$



The new kernel guards do not increase the physical precision. Therefore a twenty-bit Gram pair does not automatically provide a twenty-bit ratio.

For the omitted logarithmic force, retain the norm-relative sufficient condition


$$
K_{\rm norm}+a_{\rm cont}-d_0-1\ge s,
\tag{13.4}
$$


with the accepted


$$
K_{\rm norm}\ge2000b-138.
$$



If the new Gram residue certifies $d_0<20$, then (12.2) and the enormous accepted $K_{\rm norm}$ immediately verify (13.4) for the contemplated small values of $s$. If the norm residue vanishes, this inference is not available without further norm-depth control.

Thus the new scalar calculation can remove the original norm-depth obstruction when its norm output is nonzero, but no such output is predicted here.

---

# Part III. Bounded work warranted now

## 14. Inputs and exact expected outputs

No accepted producer or bounded verification is to be rerun.

### 14.1 Inputs

Use only:

1. the attached short artifact, hash  
   `95b1a321781e3f6a60460fef79cddb2fa40db95aa927cb23cf76015926d95478`;
2. its $A_f,A_e,U_f,U_e$ arrays;
3. the exact $b,n$;
4. the accepted $D_f,D_e$ valuations $80,77$;
5. the formulas in §§4–11.

The odd normalization units needed at the end are


$$
d_f=D_f/2^{80},\qquad d_e=D_e/2^{77}\pmod{2^{20}}.
$$


They can be obtained by multiplying the odd parts of the respective short consecutive products. This supplies the needed unit data; it is not a request to repeat the accepted guard certificate.

### 14.2 The coordinator’s one Smith inspection

Use precisely the two short presentations of §3 and the actual payload images already specified.

Expected checks:

- sizes $164\times160$, $160\times156$;
- rational ranks $160,156$;
- binary ranks $81,79$;
- nonunit pivot counts $79,77$;
- total nonunit valuations at most $161,158$;
- actual payload coordinates;
- formal boundary retained and actual value recorded as zero.

The Gram algorithm does not require dividing by those pivots.

### 14.3 New payload post-processing

Produce Newton arrays for


$$
P_f=U_f/2^{73},\qquad P_e=U_e/2^{68}.
$$



Expected checks:

- every divided forward difference has the proved divisibility;
- degrees at most $81,77$;
- payload degrees at most $162,158$;
- zero reconstruction residual in the retained precision.

This is new lattice post-processing, not a repeat of shift conversion or contact reconstruction.

### 14.4 New original Gram contraction

Run (8.1) for:

- $P=P_f^2$, modulo $2^{34}$;
- $P=P_fP_e$, modulo $2^{36}$.

For each digit, record:

- the exact digit position and input bits;
- reachable borrow masks;
- $d_t\in\{0,1,2\}$ for every transition;
- the maximum Newton degree;
- zero coefficients beyond the proved bound;
- the valuation-by-degree check from Theorem 4.

The final outputs are


$$
S_{ff}\pmod{2^{34}},\qquad
S_{fe}\pmod{2^{36}},
$$


then


$$
D_{\rm raw}\pmod{2^{20}},\qquad
E_{\rm raw}\pmod{2^{20}}
$$


via (4.8)–(4.9).

Expected verifiable checks include:

- acceptance only of terminal borrow state $(0,0,0)$;
- all 71 digits consumed;
- $S_{ff}\equiv0\pmod{2^{16}}$;
- $S_{fe}\equiv0\pmod{2^{18}}$;
- the two normalized outputs divisible by $4$;
- exact valuations reported only for nonzero residues;
- zero residues reported as lower bounds, not exact depths.

No numerical values of these final residues are asserted in this report.

---

## 15. Global arithmetic and irrationality status

The new transport is a finite local result. It neither supplies nor replaces the final all-prime normalization.

With the least actual two-column clearer $d_B$, retain the complete integer columns and


$$
A_B=N_{B,1}^{T}\Omega N_{B,1},
\qquad
H_B=N_{B,1}^{T}\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),
$$




$$
q_n=\frac{A_B}{g_B},
\qquad
p_n=\frac{H_B}{g_B}.
$$



The primitive multiplier remains


$$
\frac{d_B^2}{g_B}.
$$



A binary Gram computation cannot determine the all-prime gcd $g_B$, the least actual clearer, or the actual primitive denominator $q_n$.

The approximation quantity remains the whole same-index form


$$
q_n(e+\pi)-p_n=-q_n\epsilon_n.
$$



Conditional on the previously stated complete signed-error asymptotic,


$$
\log|\epsilon_n|
=
-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n),
$$


one still needs an infinite original subsequence on which the **actual primitive denominator** makes the whole nonzero form tend to zero.

The endpoint-family results in A4 remain restricted to their stated families and prime ranges. They do not furnish the missing all-prime infinite-family estimate for this binary construction.

No irrationality theorem follows from the single original pair.

---

## 16. Proof-status ledger

| Statement | Status |
|---|---|
| Original complete twenty-bit columns and short arrays | Accepted finite certificate; not regenerated |
| Corrected unsaturated guards $321,315$ | Accepted finite certificate |
| New upper telescoping boundary is exactly zero | **Proved** |
| Short presentation sizes and binary ranks | **Proved** |
| $U_f/2^{73},U_e/2^{68}$ are integer-valued | **Proved** |
| Integral scalar guards $14,16$ | **Proved** |
| Odd-factorial approximation of degree $2p-2$ | **Proved** |
| Exact factorial-ratio binary transport | **Proved** |
| At most four reachable borrow states | **Proved** |
| Uniform degree-by-valuation closure | **Proved** |
| Practical evaluation sizes for the actual 71-bit target | **Proved bounds** |
| Both original weighted columns are even | **Proved at the certified physical precision** |
| Original Gram residues | New bounded calculation; **not executed here** |
| Exact original norm depth | Determined only if the computed norm residue is nonzero |
| Twenty-bit ratio from twenty-bit physical data | Not automatic; precision conditions retained |
| All-prime primitive denominator and whole error | Open |
| Irrationality or rationality of $e+\pi$ | Unresolved |

---

## Conclusion

The actual short-polynomial target now admits a practical integral contraction.

The decisive change is not another rational reduction to a few moments. It is the combination of:



$$
\boxed{
\text{integer-valued normalization}
+
\text{odd-factorial polynomial approximation}
+
\text{four-state finite carry transport}.
}
$$



For the two complete original columns, this yields the exact scalar relations


$$
\boxed{
S_{ff}=2^{14}d_f^2\widetilde D,\qquad
S_{fe}=2^{16}d_fd_e\widetilde E,
}
$$


and evaluates their left sides through a proved bounded module at only $34,36$ kernel bits.

The remaining local task is now a concrete, modest exact-arithmetic contraction using the supplied short arrays—not an unresolved state-closure lemma and not a 341-bit unevaluated moment. Its output must still be computed and inspected before numerical Gram or norm-depth claims are made.

The global bottleneck remains separate:



$$
\boxed{
\text{all-prime control of the actual primitive denominator
against the whole same-index nonzero error on an infinite original sequence}.
}
$$



Accordingly,


$$
\boxed{\text{the irrationality of }e+\pi\text{ remains unproved.}}
$$


