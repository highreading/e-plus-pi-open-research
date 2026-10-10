> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3 — Two adjacent indices remove the fixed-order amplitude exceptions

## Summary and dependency scope

The proposed selector works. The essential point is that interior integration by parts transfers the Euler derivatives from the **entire kernel**


$$
K_{n,m}(T)=T^n(5+T)^m
$$


to the densities. Thus the interior effective amplitude is independent of the rounding parameter. For an odd-order amplitude zero, the first potentially nonzero even Morse coefficient is affine in the rounding parameter with nonzero slope. Two adjacent decompositions of the same $N=n+m$ therefore suffice.

There is also a two-choice selector in the bounded $\sqrt n$-transition windows. There one must use the first corrected profile, not just the leading cylinder profile. The resulting guaranteed amplitude loses a factor $n^{-1/2}$, but retains the same exponential rate and is nonzero.

The proofs below use the supplied exact five-measure identity, density analyticity, support and phase gaps, and whole exponential-correction estimate as inputs. The arithmetic conclusions additionally use the inherited denominator-transform law and the last-pole lower bound for the **actual final-gcd-reduced denominator**. These arithmetic inputs are not reproved here.

No conclusion decides the irrationality of $e+\pi$.

---

## 1. Interior integration by parts: the amplitude really is independent of rounding

Fix


$$
c\in(c_0,c_{\mathrm s}),\qquad
T_c=-\frac5{1+c},
$$


including the possibility $\mathcal F(T_c)=0$. Write


$$
\phi_c(T)=\log(-T)+c\log(5+T).
$$


Its negative-branch maximum is the nondegenerate interior saddle $T_c$.

Choose a smooth cutoff $\chi$ supported in a compact subinterval of the density-analytic interval, with $\chi=1$ near $T_c$. For each of the five densities, ordinary integration by parts gives exactly


$$
\int \chi f_h\,D^h K_{n,m}\,dT
=
\int K_{n,m}(D^*)^h(\chi f_h)\,dT,
\qquad
D^*f=-(Tf)'.
\tag{1}
$$


There are no boundary terms: $\chi f_h$ has compact support strictly inside the analytic interval.

By the product rule,


$$
\sum_{h=0}^4(D^*)^h(\chi f_h)
=\chi\mathcal F+R_\chi,
\qquad
\mathcal F=\sum_{h=0}^4(D^*)^hf_h,
\tag{2}
$$


where $R_\chi$ is supported away from the saddle.

In particular, **no dependence on $n,m$, or $\beta=m-cn$, enters $\mathcal F$**. A rounding-dependent adjoint amplitude would arise only if one incorrectly transferred derivatives from part of the kernel instead of from $K_{n,m}$ itself.

For bounded $\beta$, all contributions involving $R_\chi$, the original measures outside the saddle neighborhood, and the positive-support branch are bounded by


$$
O_c\!\left(e^{n\phi_c(T_c)}(5+T_c)^\beta n^4e^{-\eta n}\right)
\tag{3}
$$


for some $\eta>0$, uniformly over the prescribed bounded $\beta$-interval. Indeed:

* the fixed phase $\phi_c$ has a strict gap away from $T_c$;
* $c<c_{\mathrm s}$ gives a strict gap against the positive branch;
* the original Euler derivatives have at most polynomial growth $O(n^4)$ relative to the kernel when $m=cn+O(1)$.

The supplied estimate for the **whole** exponential correction is


$$
|\mathcal Z^{\rm exp}_{n,m}|
\le C(N+1)^4\frac{d^n}{n!}
\left(5+\frac d{n+1}\right)^m.
\tag{4}
$$


For bounded $\beta$, its logarithm is at most $-n\log n+O_c(n)$. It is therefore negligible relative to the saddle scale times every fixed negative power of $n$.

Equations (1)–(4) justify using the actual, rounding-independent amplitude $\mathcal F$, without dropping either boundary-cutoff terms or any part of the exponential correction.

---

## 2. Uniform Morse expansion for bounded rounding

Choose the orientation-preserving analytic Morse coordinate $z$ near $T_c$:


$$
T(0)=T_c,\qquad T'(0)>0,\qquad
\phi_c(T(z))=\phi_c(T_c)-\frac{z^2}{2}.
$$


Set


$$
b_c=5+T_c>0,
$$




$$
g(z)=\mathcal F(T(z))T'(z),\qquad
\ell(z)=\log\frac{5+T(z)}{b_c}.
\tag{5}
$$


Then


$$
\ell(0)=0,\qquad
\ell'(0)=\frac{T'(0)}{b_c}\ne0.
\tag{6}
$$



The exact rounding normalization is


$$
T^n(5+T)^m
=(-1)^n e^{n\phi_c(T_c)}b_c^\beta
e^{-nz^2/2}e^{\beta\ell(z)},
\qquad m=cn+\beta.
\tag{7}
$$


Thus $b_c^\beta$ must remain outside the Gaussian integral; it is not part of an unspecified error.

Because $\mathcal F$ is analytic and not identically zero on its connected interval, $g$ has a finite zero order $k$:


$$
g(z)=a_kz^k+a_{k+1}z^{k+1}+\cdots,\qquad a_k\ne0.
\tag{8}
$$



For a fixed compact interval of real $\beta$, the functions


$$
g(z)e^{\beta\ell(z)}
$$


have uniformly bounded Taylor remainders on a sufficiently small fixed $z$-interval. We may use a symmetric cutoff in $z$, equal to one near zero. Its complement is absorbed into (3).

Write


$$
M_{2j}=\int_{\mathbb R}u^{2j}e^{-u^2/2}\,du
=\sqrt{2\pi}(2j-1)!!.
\tag{9}
$$


Odd Taylor monomials integrate to zero under the symmetric cutoff. Taylor expansion through the next odd degree, followed by Gaussian moment estimates, gives the following **absolute uniform** expansions.

### Even zero order

If $k=2s$, then


$$
\boxed{
\frac{(-1)^n\mathcal Z_{n,m}}
{e^{n\phi_c(T_c)}b_c^\beta}
=
M_{2s}a_{2s}\,n^{-s-1/2}
+O_c(n^{-s-3/2}).
}
\tag{10}
$$


The first even coefficient is independent of $\beta$, since $\ell(0)=0$ and all lower coefficients of $g$ vanish.

### Odd zero order

If $k=2s+1$, define


$$
P_c(\beta)=a_{2s+2}+\beta\ell'(0)a_{2s+1}.
\tag{11}
$$


Then


$$
\boxed{
\frac{(-1)^n\mathcal Z_{n,m}}
{e^{n\phi_c(T_c)}b_c^\beta}
=
M_{2s+2}P_c(\beta)\,n^{-s-3/2}
+O_c(n^{-s-5/2}).
}
\tag{12}
$$


Here


$$
P_c'(\beta)=\ell'(0)a_{2s+1}\ne0.
\tag{13}
$$



These estimates include (3) and (4). They are uniform, in particular, for


$$
-(1+c)\le\beta\le1+c.
\tag{14}
$$



No assertion that the unrounded amplitude has a surviving even coefficient is needed. Even if $g$ were locally odd, the nonzero linear term of $\ell$ produces the affine coefficient (11).

---

## 3. The same-$N$, two-adjacent-index selector

For each sufficiently large integer $N$, put


$$
n_0=\left\lfloor\frac{N}{1+c}\right\rfloor,
\qquad m_0=N-n_0,
$$




$$
n_1=n_0+1,\qquad m_1=m_0-1.
\tag{15}
$$


For fixed $c>0$, both pairs eventually satisfy $n_i\ge2$, $m_i\ge0$.

Their rounding parameters satisfy exactly


$$
\beta_0=m_0-cn_0\in[0,1+c),
$$




$$
\beta_1=m_1-cn_1=\beta_0-(1+c)\in[-(1+c),0).
\tag{16}
$$



If $k$ is even, choose $i=0$.

If $k$ is odd, choose $i\in\{0,1\}$ maximizing


$$
|P_c(\beta_i)|,
\tag{17}
$$


with either fixed tie-breaking convention. Since


$$
P_c(\beta_0)-P_c(\beta_1)
=(1+c)\ell'(0)a_k,
$$


the triangle inequality yields


$$
\boxed{
\max_{i=0,1}|P_c(\beta_i)|
\ge \frac{1+c}{2}|\ell'(0)a_k|>0.
}
\tag{18}
$$



The uniform remainder in (12) is one full power of $n_i$ smaller than the selected main term. Consequently the selected whole numerator is eventually nonzero.

More precisely, with


$$
\alpha_c=
\begin{cases}
s+\tfrac12,&k=2s,\\[2mm]
s+\tfrac32,&k=2s+1,
\end{cases}
$$


there are constants $0<C_1<C_2<\infty$, depending on the fixed $c$, such that the selected pair satisfies


$$
\boxed{
C_1e^{n_i\phi_c(T_c)}b_c^{\beta_i}n_i^{-\alpha_c}
\le |\mathcal Z_{n_i,m_i}|
\le
C_2e^{n_i\phi_c(T_c)}b_c^{\beta_i}n_i^{-\alpha_c}.
}
\tag{19}
$$


In particular,


$$
\boxed{
\frac1{n_i}\log|\mathcal Z_{n_i,m_i}|
\longrightarrow \phi_c(T_c)=\log B_-(c).
}
\tag{20}
$$



This proves the requested selector theorem at every fixed $c\in(c_0,c_{\mathrm s})$, including every member of the previously defined finite exceptional set.

The constants need not be uniform as $c$ varies. The theorem concerns each fixed $c$, not arbitrary moving approaches to exceptional orders.

---

## 4. Actual primitive errors and the all-fixed-$c$ selected primorial exclusion

For each candidate pair retain, separately,


$$
L_N=2^{N+1}(2N+2)!(N!)^4,
\qquad
U_i=L_N\mathcal H_{n_i,m_i},
\qquad
V_i=L_N\mathcal J_{n_i,m_i},
$$




$$
g_i=\gcd(|U_i|,|V_i|),
$$




$$
P_i=-\operatorname{sgn}(V_i)\frac{U_i}{g_i},
\qquad
q_i=\frac{|V_i|}{g_i}>0.
\tag{21}
$$


These definitions apply once the inherited denominator theorem ensures $V_i\ne0$. They give


$$
\gcd(P_i,q_i)=1
$$


and the exact whole evaluated error


$$
\boxed{
q_i(e+\pi)-P_i
=q_i\,\frac{\mathcal Z_{n_i,m_i}}{\mathcal J_{n_i,m_i}}.
}
\tag{22}
$$



For the selected interior pair, (19) proves that (22) is nonzero. Using the inherited denominator-transform rate,


$$
\log|\mathcal J_{n_i,m_i}|
=n_i\log d+m_i\log(5+d)+o(n_i),
$$


we obtain


$$
\boxed{
\frac1{n_i}\log\left|e+\pi-\frac{P_i}{q_i}\right|
\longrightarrow
\log B_-(c)-\log d-c\log(5+d).
}
\tag{23}
$$



Now let


$$
N_x=\prod_{\substack{\ell\le x\\ \ell\text{ odd prime}}}\ell.
\tag{24}
$$


Both candidates in (15) have exactly this same $N_x$. The inherited last-pole lower bound applies to each candidate’s own $q_i$. Nothing is added, averaged, or transferred between their valuations or gcds.

Combining the new selector with the supplied bounded-rounding results in the other regimes gives a selected sequence for **every fixed $c>0$**:

* $0<c<c_0$: use the established negative-endpoint law;
* $c=c_0$: use the established bounded-rounding transition law;
* $c_0<c<c_{\mathrm s}$: use (15)–(18);
* $c=c_{\mathrm s}$: use established positive dominance under bounded rounding;
* $c>c_{\mathrm s}$: use the established positive-endpoint law.

Thus, under the inherited actual-$q$ primorial lower bound,


$$
\boxed{
\liminf_{x\to\infty}
\frac{\log|q_i(e+\pi)-P_i|}
{N_x\log\log N_x}\ge2
}
\tag{25}
$$


for the selected sequence at every fixed $c>0$.

This excludes shrinking primitive forms along these selected primorial sequences. It does **not** exclude every center in the two-parameter family, and does not decide rationality or irrationality.

---

## 5. Two choices also suffice in compact transition windows

Here the first correction is essential.

Use the supplied whole transition expansion


$$
\mathcal Z_{n,m}
=(-1)^nr^nh^mn^{3/4}
\left[\Psi(\tau)+n^{-1/2}\Xi(\tau)+O(n^{-1})\right],
\qquad
\tau=\frac{m-c_0n}{h\sqrt n},
\tag{26}
$$


uniformly for $\tau$ in compact real intervals. The profile $\Psi$ has the two supplied simple zeros $\tau_-,\tau_+$.

Define the computable corrected profile


$$
Q_n(t)=\Psi(t)+n^{-1/2}\Xi(t).
\tag{27}
$$


The argument below needs only uniformity of (26), smoothness of $\Xi$, and simplicity of the zeros. It does not require evaluating the density coefficient inside $\Xi$ numerically.

### 5.1 Fixed $n$, adjacent $m$

Take candidates $(n,m)$ and $(n,m+1)$. Their profile parameters differ by


$$
\tau_1-\tau_0=\frac1{h\sqrt n}.
\tag{28}
$$


Select the candidate maximizing $|Q_n(\tau_i)|$.

Choose disjoint small neighborhoods of the two simple roots on which $\Psi'$ has constant sign and absolute value at least $a_*>0$. For sufficiently large $n$,


$$
|Q_n'(t)|\ge a_*/2
$$


on these neighborhoods.

If the candidates lie near a root, the mean value theorem gives


$$
|Q_n(\tau_1)-Q_n(\tau_0)|
\ge \frac{a_*}{2h\sqrt n},
$$


so


$$
\max_i|Q_n(\tau_i)|
\ge \frac{a_*}{4h\sqrt n}.
\tag{29}
$$


Away from the root neighborhoods, $|\Psi|$ has a positive compact minimum; the bound is stronger there. Slightly enlarging the root neighborhoods handles candidates straddling their boundaries.

Subtracting the $O(n^{-1})$ remainder in (26), we obtain, uniformly on any fixed compact transition window,


$$
\boxed{
|\mathcal Z_{n,m_i}|
\ge C\,r^nh^{m_i}n^{1/4}>0
}
\tag{30}
$$


for the selected candidate and all sufficiently large $n$.

Thus two choices suffice. Higher coefficients are unnecessary for this selected lower bound.

### 5.2 Adjacent choices preserving $N$

For arithmetic applications, take


$$
(n_0,m_0)=(n,m),\qquad
(n_1,m_1)=(n+1,m-1).
\tag{31}
$$


Assume $\tau_0$ remains in a fixed compact interval. A direct expansion gives


$$
\begin{aligned}
\tau_1
&=\frac{h\sqrt n\,\tau_0-(1+c_0)}{h\sqrt{n+1}},\\
\tau_1-\tau_0
&=-\frac{1+c_0}{h\sqrt n}
-\frac{\tau_0}{2n}
+O(n^{-3/2}).
\end{aligned}
\tag{32}
$$


In particular their separation is bounded below by a positive constant times $n^{-1/2}$.

Select the candidate maximizing


$$
\left|Q_{n_i}(\tau_i)\right|.
\tag{33}
$$


Near either root,


$$
Q_{n+1}(\tau_1)-Q_n(\tau_0)
=\Psi'(\tau_0)(\tau_1-\tau_0)+O(n^{-1}),
\tag{34}
$$


uniformly. The first term is bounded below in absolute value by a positive multiple of $n^{-1/2}$. The same argument as above proves


$$
\boxed{
|\mathcal Z_{n_i,m_i}|
\ge C\,r^{n_i}h^{m_i}n_i^{1/4}>0.
}
\tag{35}
$$



Both candidates have the same $N$, so this version preserves the applicability of any inherited same-$N$ actual-denominator bound.

### 5.3 Why the first correction resolves the selector problem

Near a simple root $\tau_j$,


$$
Q_n(\tau)
=
\Psi'(\tau_j)
\left(
\tau-\tau_j+
\frac{\Xi(\tau_j)}{\Psi'(\tau_j)\sqrt n}
\right)
+O(n^{-1})
\tag{36}
$$


when $\tau-\tau_j=O(n^{-1/2})$. This is exactly the first corrected-zero expansion.

Adjacent integer orders differ at scale $n^{-1/2}$ in $\tau$. After incorporating $\Xi$, the remaining error is only $O(n^{-1})$, too small to cancel both separated corrected-profile values.

By contrast, the leading expansion


$$
\Psi(\tau)+O(n^{-1/2})
$$


alone has an error as large as the selector’s guaranteed signal. It cannot establish (30) or (35).

The earlier lattice-proximity obstruction therefore remains relevant for **one prescribed candidate**, but not for a selector allowed to choose between two adjacent candidates.

Finally, throughout a compact transition window,


$$
m=c_0n+O(\sqrt n),
$$


so (35), together with the corresponding uniform upper bound, gives the selected rate


$$
\frac1{n_i}\log|\mathcal Z_{n_i,m_i}|
\longrightarrow \log r+c_0\log h.
\tag{37}
$$


The polynomial loss does not change the exponential rate. The actual primitive error is again exactly (22), with the selected candidate’s own final gcd.

---

## Closing ledger

### (1) New result and proof status

**Proved from the supplied analytic inputs:**

1. Interior cutoff integration by parts produces the actual amplitude
   

$$
\mathcal F=\sum_{h=0}^4(D^*)^hf_h
$$


   independently of bounded rounding.
2. The uniform expansions (10) and (12), including cutoff terms, outside branches, and the entire exponential correction.
3. A two-adjacent-index, same-$N$ selector with eventual whole-error nonvanishing and the matching exponential rate at every fixed negative-dominant interior order.
4. A two-choice transition selector using $\Psi+n^{-1/2}\Xi$, with whole-numerator lower bound of order $r^nh^mn^{1/4}$, including a same-$N$ version.

**Arithmetic consequence using the inherited actual-denominator theorem:** the scoped selected primorial exclusion extends to every fixed $c>0$, with the final gcd and actual primitive error retained.

### (2) Exact remaining bottleneck

The selectors do not control every prescribed center. Arbitrary approaches to the phase-switch cancellation window, or prescribed transition choices tracking corrected roots, remain distinct questions.

More fundamentally, the present construction supplies growth exclusions on selected subsequences, not a sequence of nonzero primitive errors tending to zero. It therefore does not prove or disprove irrationality of $e+\pi$.

### (3) Computation request

**None.** The selectors are mathematically explicit through the Taylor coefficients defining $P_c$, or through the corrected profile $Q_n$. Their proofs require no lattice-distribution estimate and no finite scan.
