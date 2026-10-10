> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Paid contact transport, temporal depth repulsion, and the remaining arithmetic obstruction

## Abstract

The supplied archive establishes that the companion and complete terminal residual used in A3 turn 3 are not new objects. With the same normalization,


$$
\sigma_n=\rho_n,\qquad U_n^\sharp=S_n,\qquad V_n^\sharp=T_n,
$$


and the paid residual is exactly


$$
\mathscr E_j=\frac{C_j}{\kappa_j b_{c,j}}.
$$



This report proves the requested transport of the archived all-prime intersection theorem:


$$
\kappa_3b_{c,3}\mid4(n+1)^2(n+2)^2,
$$




$$
\kappa_0b_{c,0}\mid4(n+1)^2(n+2)^2(n+3).
$$


Consequently, this payment has **no prime factor above $n+2$** on either original odd family. The paid equality therefore becomes


$$
\gcd(|T_{\rm aff}|,D_j)_{>n+2}
=
\gcd(|C_j|,D_j)_{>n+2}.
$$


It supplies no new large-prime saving merely by replacing $C_j$ with $\mathscr E_j$.

The genuinely different result concerns the moving-prime alignment inventory. Using the actual moment and reference recurrences, including their actual seeds, we prove a uniform temporal repulsion theorem. For a fixed original block $n\le k\le t$, $t=bn$, and every prime $p>t+2$, let


$$
a_k(p)=
\min\!\left\{
v_p(F_k),
v_p(Q_k\tau_k-P_k\tau_{k+1})
\right\}.
$$


Then


$$
\boxed{\sum_{k=n}^{t-1}\min\{a_k(p),a_{k+1}(p)\}\le3.}
$$


More precisely, every summand is at most $1$, and three consecutive positive alignments are impossible. Thus **large depth cannot persist into the next step** at a moving prime above the terminal cutoff.

This is a rigorous restriction on the actual seeded trajectories, not a subfactorial acquisition theorem. Large isolated terminal entrances remain uncontrolled. We also prove a sharply delimited obstruction to seed-blind height and recurrence arguments: the complete contact is affine-linear in the logarithmic companion amplitude, with unit slope at every eligible contact prime. Such arguments cannot distinguish the actual amplitude $2$ from amplitudes that force complete resonance.

No unconditional proof of rationality or irrationality of $e+\pi$ follows. The final all-prime contents, actual primitive denominator, moving-prime losses, and nonzero whole error remain indispensable.

---

## 1. Scope, original domain, and reused results

The approximation indices remain exactly


$$
\boxed{n=15^r\quad\text{or}\quad n=105^r,\qquad r\ge2.}
$$


In particular, every original $n$ is odd and $n\ge225$. Set


$$
m=n+1,\qquad N=n+2,\qquad L=2^{(n+1)/2}.
$$



Consecutive indices below are used only to analyze the already supplied recurrences. They do not enlarge the approximation domain.

We reuse, at their stated scope:

1. the finite producer and its physical boundary;
2. the actual primitive endpoint rows;
3. the complete terminal decomposition;
4. the companion with its stated seed normalization;
5. the archived all-prime theorem for $\gcd(G_j,C_j)$;
6. the archived projected ideal equalities above $n+2$;
7. the closed universal-gauge decision.

We do not repeat the companion derivation, the old projected ideal calculations, the gauge search, or producer $3375$.

The contact arguments retain the hypotheses


$$
\det T\ne0,\qquad F\ne0,\qquad \widehat R_j\ne0
$$


where the corresponding quantities are used. The temporal theorem proved later does not require division by these contacts.

The archived all-prime theorem depends on the archived moment-primitivity result and the exact endpoint kernels. Its supplied proof records the losses at $2$, at primes dividing $n+1$, and at primes dividing $n+2$. We use that theorem with those costs intact; we do not replace it by an unproved determinant-primitivity assertion.

---

## 2. The actual contacts and the overlap transport

### 2.1 Original moment and contact objects

Let


$$
q(z)=1-z+\frac{z^2}{2},\qquad
a_k(n)=k![z^k]e^zq(z)^n,
$$


and


$$
X=ma_n,\qquad Y=mn\,a_{n-1},\qquad Z=2a_{n+1}-ma_n.
$$


Retain


$$
P=nX+Y,\qquad Q=nZ+2X-Y,
$$




$$
F=2m(Z-Q),\qquad C=mZ.
$$


Here $C$ is the scalar moment quantity; $C_j$ below is a complete contact projection.

The finite matrix is


$$
T=
\begin{pmatrix}
c_n&c_{n-1}&c_{n-2}\\
c_{n+1}&c_n&c_{n-1}\\
c_{n+2}&c_{n+1}&c_n
\end{pmatrix},
\qquad
c_k=[z^k]e^zq(z)^n.
$$


Its endpoint raw rows are


$$
R_j^{\rm raw}=\ell_j\operatorname{adj}(T),\qquad
\ell_0=(-1,n,-nm),\quad \ell_3=(0,0,1).
$$


The rows $r_j$ are the actual primitive integer rows obtained from these raw rows by the recorded least denominator, three-coordinate content, and sign normalization.

Write


$$
V=(v'\;w'\;e_2)=
\begin{pmatrix}
2N&0&0\\
N&N&0\\
m&2n+3&1
\end{pmatrix},
\qquad e_2=(0,0,1)^T,
$$


and


$$
\mathbf c_j=r_jV.
$$


Thus, in the archive’s notation,


$$
\mathbf c_j=(\alpha_j,\beta_j,r_{j,2}),
\qquad
G_j=\gcd(|\alpha_j|,|\beta_j|).
$$



The actual contact content is


$$
\kappa_j=\gcd(|c_{j,1}|,|c_{j,2}|,|c_{j,3}|),
$$


and


$$
\pi_j=\frac{\mathbf c_j}{\kappa_j}.
$$


Writing


$$
\pi_j=(d_{c,j}A_j,d_{c,j}B_j,c_{0,j}),
\qquad \gcd(A_j,B_j)=1,
$$


we have


$$
G_j=\kappa_jd_{c,j}.
$$



The additional payment is


$$
b_{c,j}=\gcd(d_{c,j},|C|).
$$



These contents are not the later eight-entry row contents $g_j^{(8)}$.

### 2.2 Exact identification of the residual

The archived complete terminal decomposition is


$$
\mathbf C=S_nv'+T_nw'+Ce_2,
$$


with


$$
S_n=\frac m2b_n+2n!m!\rho_n,
$$




$$
T_n=b_{n+1}-\frac m2b_n+2n!m!\rho_{n+1}.
$$


Its evaluated contact is


$$
C_j=r_j\mathbf C.
$$



Because the companion normalization in turn 3 is identical to the archived normalization,


$$
U_n^\sharp=S_n,\qquad V_n^\sharp=T_n.
$$


Consequently,


$$
C_j
=\kappa_j\bigl(\pi_{j,1}U_n^\sharp+
\pi_{j,2}V_n^\sharp+\pi_{j,3}C\bigr),
$$


and therefore


$$
\boxed{C_j=\kappa_jb_{c,j}\mathscr E_j.}
\tag{2.1}
$$



This is an identity of the actual evaluated objects, not an analogy between two constructions.

### 2.3 Polynomial transport of the payment

Since $b_{c,j}\mid d_{c,j}$,


$$
\kappa_jb_{c,j}\mid \kappa_jd_{c,j}=G_j.
$$


Equation (2.1) also gives


$$
\kappa_jb_{c,j}\mid C_j.
$$


Hence


$$
\boxed{\kappa_jb_{c,j}\mid\gcd(G_j,C_j).}
\tag{2.2}
$$



The archived theorem now gives


$$
\boxed{\kappa_3b_{c,3}\mid4m^2N^2,}
\tag{2.3}
$$




$$
\boxed{\kappa_0b_{c,0}\mid4m^2N^2(n+3).}
\tag{2.4}
$$



Because $n$ is odd, $n+3$ is even. Every prime divisor of $n+3$ is therefore at most


$$
\frac{n+3}{2}<n+2.
$$


All prime divisors of $m$ and $N$ are also at most $N$. Thus


$$
\boxed{(\kappa_jb_{c,j})_{>N}=1.}
\tag{2.5}
$$



Two consequences should be distinguished:

* **All-prime size:** the payment has logarithm $O(\log n)$.
* **Above the cutoff:** the payment makes no change whatsoever to valuations.

In particular,


$$
v_p(\mathscr E_j)=v_p(C_j)\qquad(p>N).
\tag{2.6}
$$



No finite computation is required for this transport.

---

## 3. What the paid equality adds—and what it does not add

Retain


$$
\widehat h=L\tau_n,\qquad \widehat\ell=L\tau_{n+1},
$$




$$
M=Q\widehat h-P\widehat\ell,
$$




$$
\Theta=CM+F\bigl(2L(n!)^2-\mathscr K_n^\circ\bigr),
$$




$$
g_{\rm aff}=\gcd(|F|,|CM|),\qquad
T_{\rm aff}=\Theta/g_{\rm aff},
$$


and


$$
D_j=\frac{|\widehat R_j|}
{\gcd(|\widehat R_j|,|F|)}.
$$



### 3.1 Validation of the paid valuation comparison

For completeness, the key valuation step can be checked without redoing the companion or projected-ideal derivations.

Suppress $j$. Put


$$
d=d_c,\qquad b=b_c,\qquad f_0=F/d.
$$


Choose $s,t\in\mathbb Z$ with $As+Bt=1$, and define


$$
\mathcal R=A\widehat h+B\widehat\ell,\qquad
\nu=s\widehat\ell-t\widehat h.
$$


The retained contact-chart identities are


$$
\widehat R=\kappa d\mathcal R,
$$




$$
M=J\mathcal R+c_0f_0\nu,
$$




$$
\Theta=b(\mathcal RH+f_0\nu\mathscr E),
$$


where $J,H$ are integers.

Let $p>N$ divide $D$, and write


$$
a=v_p(d),\quad w=v_p(f_0),\quad r=v_p(\mathcal R),
\quad k=v_p(b).
$$


Since $\kappa$ is a unit,


$$
v_p(D)=r-w>0.
$$


The reference pair is primitive over $\mathbb Z_p$, and the displayed change of coordinates is unimodular. Hence $\nu$ is a unit.

If $a=0$, then $v_p(M)\ge w$, so


$$
v_p(g_{\rm aff})=w=w+k.
$$


If $a>0$, primitivity of $\pi$ makes $c_0$ a unit. The two terms in the formula for $M$ have respectively valuation $>w$ and $w$, so


$$
v_p(M)=w,
$$


and


$$
v_p(g_{\rm aff})=\min(a+w,v_p(C)+w)=w+k.
$$



Dividing the identity for $\Theta$ by the actual $g_{\rm aff}$ gives


$$
T_{\rm aff}
=
\frac{bf_0}{g_{\rm aff}}
\left(\frac{\mathcal R}{f_0}H+\nu\mathscr E\right).
$$


The prefactor is a unit, while


$$
v_p(\mathcal R/f_0)=v_p(D).
$$


Therefore


$$
\min\{v_p(T_{\rm aff}),v_p(D)\}
=
\min\{v_p(\mathscr E),v_p(D)\}.
$$



Combining this with (2.6) proves, under the retained contact nonvanishing hypotheses,


$$
\boxed{
\gcd(|T_{\rm aff}|,D_j)_{>N}
=
\gcd(|\mathscr E_j|,D_j)_{>N}
=
\gcd(|C_j|,D_j)_{>N}.
}
\tag{3.1}
$$



This verification does not assume that $W_{j,3}$ is a unit.

### 3.2 Comparison with the archived endpoint correlation

Let


$$
\mathcal H_j=\gcd(|\widehat R_j|,|C_j|)_{>N},
\qquad
\mathcal S_j=\gcd(D_j,|C_j|)_{>N}.
$$


For a prime $p>N$, write


$$
r=v_p(\widehat R_j),\quad f=v_p(F),\quad c=v_p(C_j).
$$


Then


$$
v_p(\mathcal H_j)=\min(r,c),
$$


whereas


$$
\boxed{v_p(\mathcal S_j)=\min((r-f)_+,c).}
\tag{3.2}
$$



Equivalently, at all primes before restriction to $>N$,


$$
\boxed{
\gcd(D_j,|C_j|)
=
\frac{\gcd(|\widehat R_j|,|FC_j|)}
{\gcd(|\widehat R_j|,|F|)}.
}
\tag{3.3}
$$


This follows from


$$
\min(r,f+c)-\min(r,f)=\min((r-f)_+,c).
$$



In particular,


$$
\mathcal S_j\mid\mathcal H_j,
$$


and


$$
\boxed{
\mathcal H_j/\mathcal S_j
\mid\gcd(|F|,\mathcal H_j).
}
\tag{3.4}
$$


Indeed, the difference of the exponents in (3.2) is nonnegative and at most both $f$ and $\min(r,c)$.

The archive’s local ideal theorem already evaluates the unpaid correlation through the complete $I_j,J_j$. Formula (3.2) is its comparison with the paid reference denominator. It does not establish a small value for either side.

### 3.3 Exact endpoint gain assessment

There are three different claims here.

1. **A valid arithmetic refinement:** the turn-3 comparison with the older $\widehat{\mathcal B}_j$ removes an extraneous factor supported on $W_{j,3}$.

2. **No new residual above the cutoff:** by (2.5), replacing $C_j$ by $\mathscr E_j$ removes no prime above $N$.

3. **No proved primitive-endpoint saving:** neither operation establishes a new asymptotic decrease in the actual primitive endpoint denominators. Those denominators are determined by the complete corrected columns and their actual all-prime contents.

The archived theorem also gives a useful exclusion:


$$
p>N,\quad p\mid G_j\quad\Longrightarrow\quad p\nmid C_j.
$$


Thus such a prime contributes nothing to $\mathcal S_j$. Any surviving contact resonance has


$$
p\nmid G_j,
$$


and therefore $p\nmid d_{c,j}$.

The quantitative problem is still the evaluated correlation with $C_j$, not a new invariant produced by the notation $\mathscr E_j$.

---

## 4. A negative lemma for seed-blind height and recurrence methods

The following statement precisely limits one class of approaches. It does **not** say that every method using recurrences is impossible.

### 4.1 Varying only the complete companion amplitude

Keep the actual moments, endpoint rows, exponential response, and companion fixed. Define the auxiliary family


$$
\mathbf C^{(a)}
=
\mathbf B+
a\,n!m!(\rho_nv'+\rho_{n+1}w'),
\qquad a\in\mathbb Z.
$$


The actual complete terminal is $\mathbf C^{(2)}$.

At endpoint $j$,


$$
C_j^{(a)}=B_j+aH_j,
$$


where


$$
B_j=r_j\mathbf B,\qquad
H_j=n!m!(\alpha_j\rho_n+\beta_j\rho_{n+1}).
$$


These are integers: the factorial clearers are part of the established companion construction.

Let


$$
D_j^\circ
=
\prod_{\substack{p>N,\ p\mid D_j\\p\nmid G_j}}
p^{v_p(D_j)}.
$$



### Theorem 4.1 — Exact seed-blind resonance obstruction

For every prime $p\mid D_j^\circ$,


$$
H_j\in\mathbb Z_p^\times.
$$


Consequently:

* for each $e\le v_p(D_j^\circ)$, there is exactly one residue class of $a\bmod p^e$ for which
  

$$
p^e\mid C_j^{(a)};
$$


* there is exactly one residue class $a\bmod D_j^\circ$ for which
  

$$
D_j^\circ\mid C_j^{(a)}.
$$



#### Proof

At such a prime, $(\alpha_j,\beta_j)$ is primitive because $p\nmid G_j$. Also


$$
\alpha_j\tau_n+\beta_j\tau_{n+1}
=\widehat R_j/L
$$


is divisible by $p$, since $p\mid D_j$.

The matrix


$$
\begin{pmatrix}
\tau_n&\tau_{n+1}\\
\rho_n&\rho_{n+1}
\end{pmatrix}
$$


has determinant


$$
\frac{(-1)^n}{n+1},
$$


a unit at $p>N$. Thus its second product with the primitive vector
$(\alpha_j,\beta_j)^T$ is a unit:


$$
\alpha_j\rho_n+\beta_j\rho_{n+1}\in\mathbb Z_p^\times.
$$


The factorials are also units because $p>N$. Hence $H_j$ is a unit.

The congruence


$$
B_j+aH_j\equiv0\pmod{p^e}
$$


has exactly one solution. The simultaneous statement follows by the Chinese remainder theorem. ∎

### 4.2 What the obstruction rules out

This family preserves:

* the actual endpoint kernels;
* the actual moment state;
* the reference recurrence and companion normalization;
* the exponential response;
* the transverse physical terminal identity, since $q_\partial v'=q_\partial w'=0$.

It does **not** preserve the actual complete logarithmic amplitude $a=2$. Thus it is not a family of counterexamples to the desired fixed-seed theorem.

Its implication is narrower and rigorous:

> Endpoint kernels, recurrence membership, primitivity, factorial clearers, and coarse heights alone cannot establish contact avoidance uniformly over this family. The proof must use arithmetic information that distinguishes the actual complete amplitude $2$.

This remains true at factorial height scale. Choosing the CRT representative


$$
0\le a<D_j^\circ
$$


gives


$$
|C_j^{(a)}|\le |B_j|+D_j^\circ|H_j|.
$$


The displayed objects have coarse logarithmic heights $O(n\log n)$: this follows, for example, by clearing the finite $3\times3$ matrix with $(n+2)!$, bounding its cofactors, and using the supplied coefficient bounds and factorial companion recurrence. The fully resonant CRT representatives therefore remain in that same coarse height class.

This does not prove that $D_j^\circ$ is large. It proves that a height argument admitting such a large $D_j^\circ$ cannot exclude full resonance merely from those bounds.

Neither a constant-coefficient recurrence theorem nor an almost-$S$-unit theorem repairs this gap under the supplied hypotheses. The reference generating function is not rational, and the unremoved factorial has outside-fixed-$S$ height


$$
\log(n!)-O_S(n).
$$


No applicable representation, small outside-$S$ ratio, or exceptional-set avoidance has been proved.

---

## 5. A new moving-prime theorem: uniform temporal depth repulsion

We now turn to a different arithmetic feature of the actual recurrences.

### 5.1 The actual seeded trajectories

For auxiliary index $k$, write


$$
m_k=k+1,\qquad N_k=k+2,\qquad A_k=k^2+3k+1.
$$


The actual moment state is


$$
z_k=(P_k,Q_k,F_k)^T,\qquad z_2=(0,10,-66)^T,
$$


with


$$
z_{k+1}=
\begin{pmatrix}
0&m_kN_k&N_k/2\\
N_k&-A_k&-\dfrac{kN_k}{2m_k}\\
-N_k(2k+3)&N_kA_k&
\dfrac{N_k(k^2-2)}{2m_k}
\end{pmatrix}z_k.
$$


The actual reference has seed


$$
(\tau_2,\tau_3)=(2,4)
$$


and recurrence


$$
\binom{\tau_{k+1}}{\tau_{k+2}}
=
\begin{pmatrix}
0&1\\
m_k/N_k&(2k+3)/N_k
\end{pmatrix}
\binom{\tau_k}{\tau_{k+1}}.
$$



Fix an original block


$$
n\le k\le t,\qquad t=bn,\quad b\in\{15,105\},
$$


and a prime $p>t+2$. Define


$$
\overline M_k=Q_k\tau_k-P_k\tau_{k+1},
$$




$$
a_k(p)=\min\{v_p(F_k),v_p(\overline M_k)\}.
\tag{5.1}
$$


At original indices,


$$
M_k=L_k\overline M_k,
$$


and $L_k$ is a $p$-adic unit. Hence (5.1) is exactly the alignment depth used by the original inventory at those endpoints.

### 5.2 Local integrality and primitivity are valid for the actual seeds

A direct determinant calculation gives


$$
\boxed{\det\mathsf U_k=\frac{(k+1)(k+2)^2(k+3)}2.}
\tag{5.2}
$$


For $2\le k<t$, every numerator factor and denominator in this determinant is a unit at $p>t+2$. Thus $\mathsf U_k$ and its inverse are integral over $\mathbb Z_p$.

The seed $z_2$ is primitive over $\mathbb Z_p$, since its integer content is $2$. Therefore every $z_k$, $2\le k\le t$, is primitive over $\mathbb Z_p$.

Similarly,


$$
\det\mathsf R_k=-\frac{k+1}{k+2}
$$


is a unit, and the reference seed $(2,4)$ is primitive. Hence


$$
(\tau_k,\tau_{k+1})
$$


is primitive over $\mathbb Z_p$ throughout the block.

These conclusions use the actual seeds. No generic initial state is substituted.

### Theorem 5.1 — One-step depth restriction

For $n\le k<t$, put


$$
B_k=2k+3,\qquad K_k=k^2+8k+11.
$$


Then


$$
\boxed{
\min\{a_k(p),a_{k+1}(p)\}
\le v_p(B_kK_k).
}
\tag{5.3}
$$



#### Proof

Let


$$
e=\min\{a_k(p),a_{k+1}(p)\}>0.
$$


Work modulo $p^e$, and abbreviate


$$
m=k+1,\quad N=k+2,\quad A=k^2+3k+1,
\quad B=2k+3,
$$




$$
u=\tau_k,\qquad v=\tau_{k+1}.
$$



Since $F_k\equiv0$ and $Q_ku-P_kv\equiv0$, reference primitivity implies


$$
(P_k,Q_k,F_k)\equiv\eta(u,v,0)\pmod{p^e}
\tag{5.4}
$$


for some $\eta$. Moment primitivity makes $\eta$ a unit.

Applying the actual moment recurrence to (5.4) gives


$$
F_{k+1}/N\equiv\eta(-Bu+Av)\pmod{p^e}.
$$


Thus


$$
Bu-Av\equiv0\pmod{p^e}.
\tag{5.5}
$$



The reference recurrence gives


$$
u'=v,\qquad v'=(mu+Bv)/N.
$$


Also,


$$
P_{k+1}\equiv \eta mNv,\qquad
Q_{k+1}\equiv\eta(Nu-Av).
$$


Consequently,


$$
\overline M_{k+1}
\equiv
\eta v\bigl((N-m^2)u-Hv\bigr)\pmod{p^e},
\tag{5.6}
$$


where


$$
H=A+mB=3k^2+8k+4.
$$



The relevant elimination is explicit:


$$
(N-m^2)A-BH=-m^2(k^2+8k+11)=-m^2K_k.
\tag{5.7}
$$



If $v$ is a unit, (5.6) makes the bracket zero modulo $p^e$. Multiplying that bracket by $B$ and using (5.5) yields


$$
m^2K_kv\equiv0\pmod{p^e}.
$$


Thus $e\le v_p(K_k)$.

If $v$ is not a unit, $u$ is a unit. Equation (5.5) implies $p\mid B$. Modulo $p$, this means $k=-3/2$, and hence


$$
N-m^2\equiv\frac14\pmod p.
$$


The bracket in (5.6) is therefore a unit. It follows that


$$
v\equiv0\pmod{p^e}.
$$


Equation (5.5) then gives


$$
B\equiv0\pmod{p^e},
$$


so $e\le v_p(B_k)$.

Both cases prove (5.3). ∎

### Theorem 5.2 — Uniform aggregate overlap bound

For every prime $p>t+2$,


$$
\boxed{
\min\{a_k(p),a_{k+1}(p)\}\le1
\quad(n\le k<t),
}
\tag{5.8}
$$


and


$$
\boxed{
\sum_{k=n}^{t-1}\min\{a_k(p),a_{k+1}(p)\}\le3.
}
\tag{5.9}
$$


Moreover, three consecutive positive depths are impossible.

#### Proof

For $k\le t-1$,


$$
0<B_k\le2t+1<p^2,
$$


and


$$
0<K_k\le t^2+6t+4<(t+3)^2\le p^2.
$$


Thus either factor has $p$-adic valuation at most $1$.

They cannot both be divisible by $p$: substituting $k=-3/2$ gives


$$
4K_k\equiv5\pmod p,
$$


whereas $p>t+2>5$. Equation (5.8) follows from Theorem 5.1.

A positive overlap can occur only at a root modulo $p$ of


$$
(2k+3)(k^2+8k+11).
$$


There are at most three such roots. The interval $n,\ldots,t-1$ has length less than $p$, so it contains at most three representatives of them. This proves (5.9).

For the last assertion, three consecutive positive depths would make both


$$
(2k+3)(k^2+8k+11)
$$


and


$$
(2k+5)(k^2+10k+20)
$$


zero modulo $p$. The four possible pairings of factors give:

* $2k+3=2k+5=0$: only $p=2$;
* $2k+3=0$ and $k^2+10k+20=0$: only $p=29$;
* $k^2+8k+11=0$ and $2k+5=0$: only $p=11$;
* both quadratic factors zero: their difference gives $2k+9=0$, and substitution gives $p=19$.

All are excluded by $p>t+2$. ∎

### 5.3 The actual quantitative gain

The theorem proves more than a height estimate:

* a depth of at least $2$ cannot persist at the next step;
* only three adjacent overlap positions are possible for each moving prime over an entire original block;
* the total depth shared by adjacent positions is at most $3$, independently of $n,t,p$.

This is a uniform theorem about the actual trajectories.

It does not control a single isolated value $a_t(p)$. In particular, it does not yet bound


$$
\sum_{p>t+2}(a_t(p)-a_n(p))_+\log p.
$$


An arbitrarily deep terminal entrance is consistent with the proved temporal restrictions if the preceding position has depth zero.

---

## 6. Why temporal repulsion alone cannot give a subfactorial budget

A precise limitation is useful.

Consider nonnegative depth arrays satisfying only the conclusions of Theorem 5.2 and a coarse height restriction


$$
a_k(p)\log p\le C\,t\log t.
$$


Set every depth equal to zero except


$$
a_t(p)=\left\lfloor\frac{C\,t\log t}{\log p}\right\rfloor.
$$


All adjacent overlaps are zero; there are no three consecutive positive entries; and the height restriction holds. Nevertheless, the terminal acquisition can have logarithmic weight comparable to $t\log t$.

These arrays are **not asserted to arise from the actual recurrences**. They show exactly what the proved local restrictions do not imply.

Thus an argument using only:

* coarse heights;
* invertible recurrence transport;
* one-step overlap bounds; and
* absence of long runs

cannot establish an $o(t\log t)$ acquisition upper bound. It must additionally control the arithmetic of isolated entrances.

### 6.1 Explicit entrance kernels for a follow-on attack

The missing mechanism can be stated in the actual previous-step coordinates, with the full $F_k$ terms retained.

Let


$$
u=\tau_k,\qquad v=\tau_{k+1},\qquad
H_k=3k^2+8k+4.
$$


Define


$$
\boxed{
\mathcal L_k
=
-2m_k(2k+3)P_k
+2m_k(k^2+3k+1)Q_k
+(k^2-2)F_k,
}
\tag{6.1}
$$


and


$$
\boxed{
\begin{aligned}
\mathcal E_k={}&
2m_kN_kP_kv-2m_k^3Q_ku
-2m_kH_kQ_kv\\
&-\bigl(m_k^2u+(3k^2+7k+3)v\bigr)F_k.
\end{aligned}
}
\tag{6.2}
$$


Direct substitution into the two recurrences gives


$$
\boxed{\mathcal L_k=\frac{2m_k}{N_k}F_{k+1},}
\qquad
\boxed{\mathcal E_k=2m_k\overline M_{k+1}.}
\tag{6.3}
$$


At $p>t+2$, all displayed scalar multipliers are units.

Equations (6.1)–(6.2) exhibit the full entrance conditions. In particular, dropping the $F_k$ terms would analyze repeated alignment, not an actual new entrance.

### 6.2 A concrete sufficient isolated-entrance lemma

Here is one sufficient target for a **subfactorial acquisition upper bound**, not for irrationality by itself.

> **Isolated-entrance lemma.** On an infinite subset of one original family, with $t=bn$, prove both
> 

$$
> \sum_{\substack{p>t+2\\p\mid\mathcal L_{t-1},\ p\mid\mathcal E_{t-1}}}
> \log p=o(t\log t)
> \tag{6.4}
>
$$


> and
> 

$$
> \sum_{\substack{p>t+2\\a_{t-1}(p)\le1}}
> \bigl(\min\{v_p(\mathcal L_{t-1}),
> v_p(\mathcal E_{t-1})\}-1\bigr)_+\log p
> =o(t\log t).
> \tag{6.5}
>
$$


> The states in these formulas must be the states generated by the actual seeds above.

Theorem 5.2 ensures that every positive excess-depth term at the terminal lies in the class in (6.5). Equations (6.3) then show that (6.4)–(6.5) imply


$$
\sum_{p>t+2}a_t(p)\log p=o(t\log t),
$$


and hence the same upper bound for terminal acquisition.

The two parts separate first-level prime support from deep lifting. Neither part is proved here. Their value as a follow-on target is that the repeated-alignment branch has now been disposed of quantitatively: the remaining problem is the actual fixed-seed entrance locus (6.1)–(6.2).

Depending on the intended inventory budget, one may instead need a lower bound for acquisition. The repulsion theorem supplies neither a lower bound nor the claimed upper bound. The budget must specify the required direction.

---

## 7. Preservation of the physical construction and final arithmetic

None of the preceding reductions modifies the producer.

### 7.1 Complete force, finite boundary, and physical returns

Retain


$$
q_j=[z^j]q(z)^n,
$$




$$
\alpha_0=\alpha_1=1,\qquad
\alpha_r=\alpha_{r-1}-\frac12\alpha_{r-2},
$$




$$
\eta_s=\sum_{r=0}^{s}\frac1{r!}
+\sum_{r=1}^{s}\frac{2\alpha_{r-1}}r,
\qquad
\mathcal W_s=s!\eta_s,
$$


and


$$
\boxed{
w_i=
\sum_{j=0}^{\min(2n,n+i)}
q_j(n+i)^{\underline j}\mathcal W_{2n+i-j},
\qquad 0\le i\le2.
}
\tag{7.1}
$$


Both exponential and logarithmic contributions remain. The maximum physical force index is exactly


$$
K=2n+2.
$$


The differential-source formulation retains the coefficient $1$ of $\mathfrak f_K$ in $b_{K+1}$. No inverse is extended beyond this terminal.

With


$$
\widehat w_i=w_i/(n+i)!,
$$


the physical returns remain


$$
\boxed{
N_0=\det T+R_0^{\rm raw}\widehat w,\qquad
N_3=R_3^{\rm raw}\widehat w.
}
\tag{7.2}
$$



The auxiliary amplitude family in Section 4 is only a negative-method test. It is not substituted into (7.1) or (7.2).

### 7.2 Complete corrected columns and actual contents

Retain


$$
x=T^{-1}(n!t),\qquad y=T^{-1}\widehat w,
$$


where


$$
t=
\begin{pmatrix}
\tau_n\\
(\tau_n+\tau_{n+1})/2\\
\tau_{n+2}/2
\end{pmatrix},
\qquad
S=
\begin{pmatrix}
1&-n&nm\\
0&1&-2n\\
0&0&1
\end{pmatrix}.
$$


Write $sx=Sx,\ sy=Sy$. Then


$$
u=(-sx_0,\ sx_0-sx_1,\ sx_1-sx_2,\ sx_2),
$$




$$
\boxed{
v=(1-sy_0,\ sy_0-sy_1,\ sy_1-sy_2,\ sy_2).
}
\tag{7.3}
$$


The exterior $+1$ is retained.

The least simultaneous clearer is


$$
\boxed{
D_8=\operatorname{lcm}_{0\le j\le3}
\bigl(\operatorname{den}(u_j),\operatorname{den}(v_j)\bigr).
}
\tag{7.4}
$$


The actual all-prime row contents and primitive entries are


$$
g_j^{(8)}=\gcd(|D_8u_j|,|D_8v_j|),
$$




$$
\widetilde u_j=D_8u_j/g_j^{(8)},\qquad
\widetilde v_j=D_8v_j/g_j^{(8)}.
\tag{7.5}
$$


For a nonzero endpoint, its actual primitive denominator is


$$
|\widetilde u_j|.
$$


It is not $D_j$, $G_j$, $\kappa_jb_{c,j}$, or a selected-prime normalization.

### 7.3 Moving-prime losses remain paid

The retained block inventory identity remains


$$
\boxed{
\mathcal I_t=
\frac{\mathcal I_n c^{\min}_{n,t}}
{\mathcal M_{n,t}\mathcal L_{n,t}},
}
\tag{7.6}
$$


with


$$
\mathcal M_{n,t}
=
\prod_{n+2<p\le t+2}
p^{\min(v_p(F_n),v_p(M_n))}
$$


and


$$
\mathcal L_{n,t}
=
\prod_{p>t+2}p^{(a_n(p)-a_t(p))_+}.
$$



The temporal theorem does not cancel either the medium-prime loss or the terminal-depth loss. Nor does it remove any division or exterior payment in the retained whole-telescope argument.

### 7.4 The final all-prime gcd and primitive weight denominator

Let


$$
h_{\rm end}=\gcd(|\widetilde u_0|,|\widetilde u_3|),
$$




$$
\widetilde u_0=h_{\rm end}A_{\rm wt},\qquad
\widetilde u_3=h_{\rm end}B_{\rm wt}.
$$


For a reduced weight $\lambda=a/k_{\rm wt}$, $k_{\rm wt}>0$, retain


$$
J_{\rm wt}
=B_{\rm wt}\widetilde v_0-A_{\rm wt}\widetilde v_3,
$$




$$
T_{\rm wt}
=aJ_{\rm wt}+k_{\rm wt}A_{\rm wt}\widetilde v_3,
$$




$$
F_{\rm gcd}
=
\gcd(|A_{\rm wt}|,|a|)
\gcd(|B_{\rm wt}|,|a-k_{\rm wt}|),
$$




$$
G_{\rm wt}=\gcd(k_{\rm wt},|J_{\rm wt}|),
$$




$$
H_{\rm gcd}
=
\gcd\!\left(
h_{\rm end},
\frac{|T_{\rm wt}|}{F_{\rm gcd}G_{\rm wt}}
\right).
$$


The actual primitive fraction is


$$
\boxed{
q_\lambda=
\frac{k_{\rm wt}h_{\rm end}|A_{\rm wt}B_{\rm wt}|}
{F_{\rm gcd}G_{\rm wt}H_{\rm gcd}},
}
\tag{7.7}
$$




$$
\boxed{
p_\lambda=
\operatorname{sgn}(A_{\rm wt}B_{\rm wt})
\frac{T_{\rm wt}}
{F_{\rm gcd}G_{\rm wt}H_{\rm gcd}}.
}
\tag{7.8}
$$


Every gcd here is all-prime.

The whole error is


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda\left[
(e+\pi)
-\lambda\frac{\widetilde v_0}{\widetilde u_0}
-(1-\lambda)\frac{\widetilde v_3}{\widetilde u_3}
\right].
}
\tag{7.9}
$$


Equivalently, in the retained notation,


$$
q_\lambda(e+\pi)-p_\lambda
=q_\lambda e_3\alpha_{n,2}(\lambda-\Lambda_{n,2}).
$$



An irrationality proof requires


$$
\boxed{0<|q_\lambda(e+\pi)-p_\lambda|\longrightarrow0}
\tag{7.10}
$$


on the **same infinite original indices** for which the arithmetic bounds hold.

A nonvanishing theorem for the archived scalar Wronskian does not by itself prove nonvanishing of (7.9). Likewise, a signed-error theorem for another specified weighting scheme cannot be transferred without its hypotheses.

---

## 8. A new bounded exact-arithmetic audit

No computation has been executed.

The overlap identities and the payment transport do not require another computation at $225$. The following optional calculation instead decides a new bounded moving-prime quantity.

### 8.1 Inputs

Use the original block


$$
\boxed{n=225,\qquad t=3375.}
$$


Use exactly the primes


$$
\boxed{3377<p\le5000}
$$


and depth cutoff


$$
\boxed{E=4.}
$$



The primes in this finite interval can be certified by trial division by primes at most $70$. No factorization of a large recurrence value is required.

For each such prime, calculate the actual seeded recurrences modulo $p^4$, from $k=2$ through $3375$, with


$$
z_2=(0,10,-66),\qquad (\tau_2,\tau_3)=(2,4).
$$


Every recurrence denominator is invertible modulo $p^4$, since $p>3377$.

Define the exactly determined clipped depths


$$
a_k^{[4]}(p)=
\min\{4,v_p(F_k),v_p(\overline M_k)\}.
$$



This calculation uses the moment and reference recurrences only. It does not rerun producer $3375$, the corrected columns, or the archived companion calculation.

### 8.2 Expected verifiable output

For each prime, provide:

1. $a_{225}^{[4]}(p)$ and $a_{3375}^{[4]}(p)$;
2. every $k\in[225,3374]$ with
   

$$
\min(a_k^{[4]}(p),a_{k+1}^{[4]}(p))>0;
$$


3. verification that each such overlap has depth $1$, that there are at most three, and that
   

$$
p\mid(2k+3)(k^2+8k+11);
$$


4. a list of endpoint entries clipped at $4$, explicitly marked as having unresolved greater depth.

The new finite acquisition and terminal-loss products are


$$
\boxed{
\mathcal A^{[4]}
=
\prod_{3377<p\le5000}
p^{(a_{3375}^{[4]}(p)-a_{225}^{[4]}(p))_+},
}
$$




$$
\boxed{
\mathcal L^{[4]}
=
\prod_{3377<p\le5000}
p^{(a_{225}^{[4]}(p)-a_{3375}^{[4]}(p))_+}.
}
$$


The output should verify the exact restricted identity


$$
\prod_{3377<p\le5000}p^{a_{3375}^{[4]}(p)}
=
\left(\prod_{3377<p\le5000}p^{a_{225}^{[4]}(p)}\right)
\frac{\mathcal A^{[4]}}{\mathcal L^{[4]}}.
$$



All modular states lie modulo $p^4<5000^4$. The number of primes, steps, and matrix operations is explicitly bounded by the stated interval and terminal.

This audit establishes only its clipped, finite-prime, single-block scope. It does not measure the medium-prime loss, primes above $5000$, or depths greater than $4$, and cannot imply an infinite acquisition theorem.

---

## 9. Proof ledger and final conclusion

| Statement | Status |
|---|---|
| Companion and complete terminal decomposition | Established archive results, reused |
| $\mathscr E_j=C_j/(\kappa_jb_{c,j})$ | Exact overlap identification |
| Polynomial all-prime bound for $\kappa_jb_{c,j}$ | Proved transport |
| Absence of payment primes above $n+2$ | Proved on the original odd domain |
| Paid equality with $\gcd(D_j,C_j)_{>n+2}$ | Proved under retained contact hypotheses |
| New large-prime saving from renaming $C_j$ | None |
| Seed-blind affine-amplitude obstruction | Proved, with explicitly limited scope |
| One-step moving-prime depth restriction | New theorem, proved from actual seeds and recurrences |
| Aggregate adjacent shared depth $\le3$ per moving prime | New theorem, proved |
| Subfactorial isolated-entrance estimate | Open |
| Subfactorial complete contact correlation | Open |
| Required moving-prime acquisition bound | Open |
| All-prime primitive denominator bound giving whole-error decay | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

The principal new quantitative theorem is


$$
\boxed{
\sum_{k=n}^{t-1}
\min\!\left\{
v_p(F_k),v_p(\overline M_k),
v_p(F_{k+1}),v_p(\overline M_{k+1})
\right\}
\le3
\qquad(p>t+2).
}
$$


It proves that deep moving-prime alignment cannot persist and that adjacent overlap has uniformly bounded total depth over an original block.

The exact remaining obstruction is different: **isolated entrances and fixed-seed contact resonances may still carry factorial-scale prime weight**. Coarse heights, recurrence invertibility, and the proved local repulsion do not control that weight. The actual complete seed must enter a new arithmetic estimate, such as a bound on the fixed-seed entrance kernels (6.1)–(6.2), or a genuinely quantitative theorem for the complete $C_j$.

Even such an estimate must be transported through the original medium-prime and terminal-depth losses, all actual row contents and $D_8$, and the final all-prime gcd. It must then yield the nonzero whole-error convergence (7.10) at the same infinite original indices.

If $e+\pi=a/d$ were rational, every nonzero integer linear form


$$
q(e+\pi)-p
$$


would have absolute value at least $1/d$. Thus (7.10) would prove irrationality. No theorem established here supplies it.



$$
\boxed{\text{The unconditional rationality or irrationality of }e+\pi\text{ remains unresolved.}}
$$


