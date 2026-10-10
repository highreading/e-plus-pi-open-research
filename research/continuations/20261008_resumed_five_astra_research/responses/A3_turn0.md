> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A full-degree, two-source quadratic-contact producer for $e+\pi$

## Abstract and proof status

The rationality or irrationality of $e+\pi$ is **not decided here**.

This report constructs a materially different family from the compact mixed square and the other supplied producers. The change is substantive:

- the polynomial variable is the original integration variable $t$, not only $t^2$;
- odd powers are admitted;
- the resulting $\log 2$ source is retained and then eliminated by an exact additional constraint at the conjugate points $i,-i$;
- the exponential and arctangent coefficients are matched by a **quadratic contact condition**, realized by an explicit rational sum of two squares.

Thus positivity of the complete error follows directly from the actual integrand. It is not inferred from a scalar analogue of an unproved mixed-normality statement.

For every integer $N\ge2$, the construction below gives explicitly defined coprime integers


$$
p_N\in\mathbb Z,\qquad q_N\in\mathbb Z_{>0},
$$


with


$$
\ell_N:=q_N(e+\pi)-p_N>0.
$$


All polynomial contents, coefficient clearers, and the final all-prime gcd are retained.

Let


$$
T_N=(2N)!-4(2N-1)!+8(2N-2)!-8(2N-3)!+4(2N-4)!.
$$


A new quantitative theorem proved below is


$$
\boxed{
\frac{q_N}{(2N-3)T_N}
<
\ell_N
\le
2^{15}q_NN\exp\!\left(-\frac{\sqrt N}{3}\right),
\qquad N\ge64.
}
\tag{0.1}
$$


There is also an exact rationally evaluable comparison


$$
\boxed{3q_NJ_N\le \ell_N\le7q_NJ_N,}
\tag{0.2}
$$


where $J_N>0$ is the integral over $[0,1]$ of the explicitly constructed rational polynomial.

These statements hold, in particular, at every original binary/compact index


$$
\boxed{N=b(u)=9^{18+32u},\qquad u\ge0.}
\tag{0.3}
$$



The new arithmetic representation has the unconditional bound


$$
\log q_N\le12N\log N+O(N).
\tag{0.4}
$$


This is an actual upper bound for this family’s primitive denominator, not a substitution for it. It is still much too large to combine with the stretched-exponential analytic bound in (0.1).

The remaining obstruction is therefore explicit: the complete paid normalization must be controlled on an infinite subset of (0.3). No such infinite-domain arithmetic theorem is proved here.

---

## 1. Source assessment and separation of constructions

### 1.1 What the supplied no-go gates establish

The following distinctions are essential.

**The compact square.** Its original objects remain


$$
0\le m<2k,\qquad 0\le j<k,\qquad m+j\le3k-2,
$$


with


$$
c_n=a_{2n}-(-1)^n,\qquad
r_n=-(2n)!+4\rho_n,
$$




$$
\rho_0=0,\qquad \rho_{n+1}+\rho_n=\frac1{2n+1},
$$


and


$$
H_k(s)=
\det[C\mid \Lambda_k\mathcal R+s\Lambda_kwv^T],
\qquad
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5).
$$


The accepted sign, conditioning, column-clearer, and rational-error theorems concern this same finite matrix. They do not identify its final content


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|).
$$



The later ledger reports a completed finite $k=32$ refutation of the proposed content envelope, with excess binary depth $2^{547}$. The underlying numerical certificate is not reproduced in the packet, so I do not independently verify that numerical value here. In any event, the older envelope was not a proved theorem and cannot be used. The reported refutation has only its stated finite scope. No duplicate $k=32$ calculation is proposed.

**The distinct Laguerre matrix.** On its retained domain,


$$
b=3^{249005515+574312172u},\quad
n=2001b,\quad d=b-1,\quad h=2000b+1,
$$


with the supplied admissibility conditions, A2’s argument gives


$$
|F|<\sqrt b\,R.
$$


Together with the retained theorem $h\mid q$, where $q=|F|/g$, this yields


$$
\frac gR=\frac{|F|}{qR}<\frac{\sqrt b}{h},
$$


and hence, using the complete error lower bound,


$$
q(e+\pi)-p>\frac{h}{2\sqrt b}>1000\sqrt b.
$$


The contact-deformation argument has the requisite discrete hypotheses: its quadrature nodes lie above $1$, its weights remain positive, and the logarithmic weight derivative is increasing on the actual discrete support. This is a family-specific obstruction, not a theorem about every construction using classical Laguerre polynomials.

**The short rectangular and two-seed gates.** The factorial Gram diagonalization mechanism is established background, including the scope cautions for even-index matrices and evaluation perturbations. The $N=4$ two-seed counterexample excludes its proposed all-$N$ constant-sign Markov-ratio identification. It does not establish eventual failure of every mixed AT property; the packet itself supplies a reason not to extrapolate its particular negative Hankel determinant.

The new construction below does not assume any of those missing mixed-normality statements.

### 1.2 The old binary producer is not altered or transferred

The original binary data remain


$$
b=9^{18+32u},\qquad n=4002b,
$$


with contact range $0,\ldots,b-1$, reconstruction range $0,\ldots,b$, and physical terminal


$$
z_b=0.
$$


Its complete corrected columns remain


$$
x=\frac12RA^{-1}f,\qquad
y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},
\qquad x=2^ax_0.
$$


Its complete return remains


$$
S=\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f,
$$


and the retained paid valuation is


$$
v_2\!\left(\frac{S}{2^{a+1}}\right)\ge\chi-a,
\qquad
\chi=v_2\binom{n+b-1}{b-1}.
$$


Neither its corrected-column contents nor its final gcd are evaluated by the new argument. Its denominator valuation does not transfer to the $q_N$ constructed here.

### 1.3 What changes in the new producer

The old compact construction uses even polynomials. Here the actual admissible space is


$$
\mathbb Q[t]_{\le N},
$$


and the final nonnegative polynomial has degree exactly $2N$. Its source constraints are


$$
\int_{-\infty}^1e^{t-1}P_N(t)\,dt=1,
\qquad
P_N(i)=P_N(-i)=1.
\tag{1.1}
$$


These are not a basis change within the old compact pencil.

The finite $N=3$ certificate in Section 7 has nonzero odd coefficients. In particular, this is not merely the unchanged even-polynomial square written in different coordinates.

No claim of global literature novelty is made. The formulas and certificate below make the proposed family precise enough for a separate overlap gate.

---

## 2. Complete endpoint identities, including the new source

Define


$$
d\eta(t)=e^{t-1}\mathbf1_{(-\infty,1]}(t)\,dt.
$$


Its moments are the integers


$$
a_0=1,\qquad a_d=1-da_{d-1}.
\tag{2.1}
$$


Integration by parts gives


$$
\int_{-\infty}^1t^d\,d\eta(t)=a_d,
$$


and


$$
\int_0^1e^tt^d\,dt=e\,a_d-(-1)^dd!.
\tag{2.2}
$$



For the arctangent channel, put


$$
\xi_d=\Re(i^d),\qquad \zeta_d=\Im(i^d),
$$


and define


$$
\sigma_0=\sigma_1=0,\qquad
\sigma_d=\frac1{d-1}-\sigma_{d-2}\quad(d\ge2).
\tag{2.3}
$$


Then


$$
4\int_0^1\frac{t^d}{1+t^2}\,dt
=
\pi\xi_d+2\log2\,\zeta_d+4\sigma_d.
\tag{2.4}
$$


Indeed, the initial integrals are $\pi$ and $2\log2$, and


$$
\frac{t^d}{1+t^2}
=t^{d-2}-\frac{t^{d-2}}{1+t^2}.
$$



Thus the full mixed moment is


$$
\int_0^1t^d\left(e^t+\frac4{1+t^2}\right)dt
=
e\,a_d+\pi\xi_d+2\log2\,\zeta_d
-(-1)^dd!+4\sigma_d.
\tag{2.5}
$$


The odd-power $\log2$ term has not been omitted.

Let


$$
w(t)=e^t+\frac4{1+t^2},\qquad 0\le t\le1.
$$


We will use


$$
3\le w(t)<7.
\tag{2.6}
$$



### 2.1 The exact source-contact principle

Suppose $P\in\mathbb Q[t]$ satisfies


$$
\int P\,d\eta=1,\qquad P(i)=1.
\tag{2.7}
$$


Because $P$ is real, $P(-i)=1$ as well. Therefore


$$
P(t)=1+(1+t^2)S_P(t)
$$


for a rational polynomial $S_P$.

Writing


$$
B(P)=\sum_d [t^d]P(t)\,(-1)^dd!,
$$


equations (2.2) and (2.4) give the complete identity


$$
\boxed{
\int_0^1P(t)w(t)\,dt
=
e+\pi-
\left(B(P)-4\int_0^1S_P(t)\,dt\right).
}
\tag{2.8}
$$


The exponential coefficient is $1$. The $\pi$ coefficient is $1$. The $\log2$ coefficient is exactly


$$
\Im P(i)=0.
$$


This is an added genuine source constraint, not a deleted error term.

---

## 3. An explicit rational sum-of-squares solution of the contact conditions

### 3.1 Classical Gram diagonalization used at its actual scope

Let


$$
L_j(y)=\sum_{r=0}^j(-1)^r\binom jr\frac{y^r}{r!}
$$


be the ordinary Laguerre polynomial. The classical identity


$$
\int_0^\infty e^{-y}L_j(y)L_k(y)\,dy=\delta_{jk}
\tag{3.1}
$$


is used here for the full polynomial space.

For completeness, its normalization follows from


$$
L_j(y)=\frac{e^y}{j!}\frac{d^j}{dy^j}(e^{-y}y^j).
$$


Integration by parts gives orthogonality to lower degrees. Applying the same calculation to $L_j$, whose leading coefficient is $(-1)^j/j!$, gives norm $1$. All boundary terms vanish.

Consequently,


$$
Q_j(t):=L_j(1-t)
$$


is an orthonormal basis for $\mathbb R[t]_{\le N}$ in $L^2(\eta)$.

This classical diagonalization is background, not a new Smith-form claim.

### 3.2 Integer source data

Fix $N\ge2$, and define


$$
E_j(t)=N!Q_j(t)\in\mathbb Z[t],
\qquad 0\le j\le N.
\tag{3.2}
$$


Write


$$
E_j(i)=\alpha_j+i\beta_j,\qquad \alpha_j,\beta_j\in\mathbb Z.
$$


Set


$$
\mathsf U=\sum_{j=0}^N\alpha_j^2,\qquad
\mathsf V=\sum_{j=0}^N\alpha_j\beta_j,\qquad
\mathsf W=\sum_{j=0}^N\beta_j^2,
$$




$$
\Delta=\mathsf U\mathsf W-\mathsf V^2,\qquad
B=(N!)^2.
\tag{3.3}
$$


The vectors $(\alpha_j)$ and $(\beta_j)$ are independent already in coordinates $j=0,1$, because $Q_0=1$ and $Q_1=t$. Hence


$$
\Delta>0.
$$



Define the integer polynomials


$$
\mathcal A(t)=\sum_{j=0}^N\alpha_jE_j(t),\qquad
\mathcal B(t)=\sum_{j=0}^N\beta_jE_j(t),
$$




$$
\Phi(t)=\mathsf W\mathcal A(t)-\mathsf V\mathcal B(t),
\qquad
f_N(t)=\frac{\Phi(t)}{\Delta}.
\tag{3.4}
$$


Direct evaluation gives


$$
\Phi(i)=\Delta,
\qquad f_N(i)=1.
\tag{3.5}
$$



Orthogonality gives


$$
\int\Phi(t)^2\,d\eta(t)=B\mathsf W\Delta,
$$


so


$$
\tau_N:=\int f_N^2\,d\eta=\frac{B\mathsf W}{\Delta}.
\tag{3.6}
$$



### 3.3 The exact minimizing property

Among real polynomials $f$ of degree at most $N$ satisfying $f(i)=1$, $f_N$ uniquely minimizes $\int f^2\,d\eta$.

Indeed, writing $f=\sum c_jE_j$, the constraints are


$$
\sum\alpha_jc_j=1,\qquad \sum\beta_jc_j=0,
$$


and the squared norm is $B\sum c_j^2$. Solving this two-constraint Euclidean minimum gives


$$
c_j=\frac{\mathsf W\alpha_j-\mathsf V\beta_j}{\Delta},
$$


which is precisely (3.4).

In particular, the admissible polynomial


$$
f_2(t)=\frac{5-t^2}{6}
$$


shows, for every $N\ge2$,


$$
\tau_N\le
\frac{25-10a_2+a_4}{36}
=\frac{25-10+9}{36}
=\frac23.
\tag{3.7}
$$


Thus


$$
D:=\Delta-B\mathsf W>0.
\tag{3.8}
$$



### 3.4 The second square and its exactly evaluated norm

Put


$$
g_N(t)=(1+t^2)(1-t)^{N-2}.
\tag{3.9}
$$


It has degree $N$, integer coefficients, and


$$
g_N(i)=g_N(-i)=0.
$$



With $y=1-t$,


$$
g_N(t)=y^{N-2}(y^2-2y+2).
$$


Therefore


$$
\begin{aligned}
T_N:=\int g_N^2\,d\eta
={}&(2N)!-4(2N-1)!+8(2N-2)!\\
&-8(2N-3)!+4(2N-4)!>0.
\end{aligned}
\tag{3.10}
$$



Now define


$$
\boxed{
P_N(t)=f_N(t)^2+\frac{1-\tau_N}{T_N}g_N(t)^2.
}
\tag{3.11}
$$


This rational polynomial satisfies


$$
P_N(i)=1,\qquad
\int P_N\,d\eta=\tau_N+(1-\tau_N)=1.
\tag{3.12}
$$


Moreover,


$$
P_N(t)>0\qquad(0\le t<1),
$$


because $1-\tau_N\ge1/3$ and $g_N(t)>0$ there.

This proves the two-source quadratic contact conditions in the actual objects.

---

## 4. Complete paid normalization and the actual primitive pair

No division in (3.11) is free.

### 4.1 Raw integer polynomial and actual polynomial content

Equations (3.4), (3.6), and (3.8) give


$$
P_N(t)=\frac{\mathscr W_N(t)}{\mathscr Z_N},
$$


where


$$
\boxed{
\mathscr W_N(t)=T_N\Phi(t)^2+D\Delta\,g_N(t)^2,
\qquad
\mathscr Z_N=T_N\Delta^2.
}
\tag{4.1}
$$


Both are integral, and


$$
\mathscr W_N(i)=\mathscr Z_N.
$$



Let the **actual polynomial content** be


$$
h_N=\gcd\{[t^d]\mathscr W_N(t):0\le d\le2N\}.
\tag{4.2}
$$


Since evaluation at $i$ is an integer linear combination of the coefficients in each real and imaginary component,


$$
h_N\mid\mathscr Z_N.
$$


Define


$$
W_N(t)=\frac{\mathscr W_N(t)}{h_N}\in\mathbb Z[t],
\qquad
M_N=\frac{\mathscr Z_N}{h_N}\in\mathbb Z_{>0}.
\tag{4.3}
$$


Then $W_N$ is primitive and


$$
P_N=\frac{W_N}{M_N},\qquad W_N(i)=M_N.
$$



Because the coefficients of $W_N$ have gcd $1$, the **actual least simultaneous coefficient clearer of $P_N$** is exactly $M_N$.

### 4.2 Complete rational endpoint term

Monic polynomial division gives


$$
S_N(t):=\frac{W_N(t)-M_N}{1+t^2}\in\mathbb Z[t],
\qquad \deg S_N=2N-2.
\tag{4.4}
$$


Write


$$
W_N(t)=\sum_{d=0}^{2N}w_dt^d,\qquad
S_N(t)=\sum_{j=0}^{2N-2}s_jt^j,
$$


and retain the entire factorial endpoint


$$
B_{\mathrm{end},N}=\sum_{d=0}^{2N}w_d(-1)^dd!.
\tag{4.5}
$$



The least clearer of the **individual arctangent quotient terms** is


$$
L_{\mathrm{ent},N}
=
\operatorname{lcm}_{0\le j\le2N-2}
\frac{j+1}{\gcd(j+1,4s_j)}.
\tag{4.6}
$$


Set


$$
J_{\mathrm{arc},N}
=
\sum_{j=0}^{2N-2}\frac{4s_jL_{\mathrm{ent},N}}{j+1}\in\mathbb Z,
$$




$$
d_{\mathrm{arc},N}
=\gcd(L_{\mathrm{ent},N},J_{\mathrm{arc},N}),
\qquad
\lambda_N=\frac{L_{\mathrm{ent},N}}{d_{\mathrm{arc},N}}.
\tag{4.7}
$$


Thus $\lambda_N$ is the actual denominator, in lowest terms, of


$$
B_{\mathrm{end},N}-4\int_0^1S_N(t)\,dt.
$$


It is the **actual least simultaneous coefficient clearer** of the rational affine polynomial


$$
M_Ns-\left(B_{\mathrm{end},N}-4\int_0^1S_N(t)\,dt\right).
$$



Define


$$
A_N
=
\lambda_N B_{\mathrm{end},N}
-\frac{J_{\mathrm{arc},N}}{d_{\mathrm{arc},N}}
\in\mathbb Z.
\tag{4.8}
$$


Minimality of $\lambda_N$ gives


$$
\gcd(\lambda_N,A_N)=1.
\tag{4.9}
$$



### 4.3 Final all-prime gcd

The final gcd is


$$
\boxed{
\mathfrak G_N=\gcd(\lambda_NM_N,|A_N|).
}
\tag{4.10}
$$


It includes every prime and its full depth. By (4.9),


$$
\mathfrak G_N=\gcd(M_N,|A_N|),
\qquad
\gcd(\mathfrak G_N,\lambda_N)=1.
\tag{4.11}
$$



The actual primitive pair is


$$
\boxed{
q_N=\frac{\lambda_NM_N}{\mathfrak G_N}>0,
\qquad
p_N=\frac{A_N}{\mathfrak G_N}.
}
\tag{4.12}
$$


In particular,


$$
\lambda_N\mid q_N.
\tag{4.13}
$$


The arctangent coefficient clearer cannot subsequently disappear into the final gcd.

### 4.4 The whole error

Applying (2.8) to $P_N=W_N/M_N$ gives


$$
\boxed{
\ell_N
=
q_N(e+\pi)-p_N
=
\frac{\lambda_N}{\mathfrak G_N}
\int_0^1W_N(t)w(t)\,dt
=
q_N\int_0^1P_N(t)w(t)\,dt>0.
}
\tag{4.14}
$$


This is the complete error, with both channels and every rational endpoint term included.

---

## 5. A proved quantitative two-source interpolation lemma

The next result evaluates the analytic gain. It does not leave the source kernel as an unnamed or unevaluated asymptotic object.

### Lemma 5.1

For $N\ge64$,


$$
\boxed{
\tau_N\le2048N\exp\!\left(-\frac{\sqrt N}{3}\right).
}
\tag{5.1}
$$



### Proof

We construct an admissible polynomial and use the minimizing property of $f_N$.

For $r=N,N-1$, put


$$
R_r(t)=T_r\!\left(1-\frac{1-t}{8N}\right),
$$


where $T_r$ is the Chebyshev polynomial.

With $y=1-t$, the argument lies in $[-1,1]$ for $0\le y\le16N$. On the remaining tail,


$$
\left|T_r\!\left(1-\frac y{8N}\right)\right|
\le\left(\frac y{4N}\right)^r.
$$


Consequently,


$$
\begin{aligned}
\|R_r\|_\eta^2
&\le1+\frac{(2r)!}{(4N)^{2r}}\\
&\le1+\left(\frac{r}{2N}\right)^{2r}
\le2.
\end{aligned}
\tag{5.2}
$$


No factorial beyond $(2N)!$ has been used.

At $t=i$, the Chebyshev argument is


$$
z=1-\delta+i\delta,\qquad \delta=\frac1{8N}.
$$


Write


$$
z=\cosh(\alpha+i\theta),
\qquad \alpha>0,\quad 0<\theta<\frac\pi2.
$$


Solving for $s=\sinh^2\alpha$ gives


$$
s=
\frac{\delta}
{\sqrt{1+(1-\delta)^2}+1-\delta}.
$$


For $0<\delta\le1/8$, the denominator is between $2$ and $5/2$. Hence


$$
\frac1{20N}<\sinh^2\alpha<\frac1{16N}.
$$


Using $\operatorname{arsinh}x\ge x/\sqrt{1+x^2}$, we obtain


$$
\frac1{5\sqrt N}\le\alpha\le\frac1{4\sqrt N},
\qquad
\sin\theta=\frac{\delta}{\sinh\alpha}\ge\frac1{2\sqrt N}.
\tag{5.3}
$$



Let


$$
a_r=\Re T_r(z),\qquad b_r=\Im T_r(z),
$$


and


$$
\mathcal D=a_Nb_{N-1}-a_{N-1}b_N.
$$


Since $T_r(z)=\cosh(r(\alpha+i\theta))$,


$$
\mathcal D
=
-\frac12\left[
\sinh((2N-1)\alpha)\sin\theta
+\sinh\alpha\sin((2N-1)\theta)
\right].
$$


For $N\ge64$, $(2N-1)\alpha\ge2$, and


$$
\sinh\alpha\le\frac12\sin\theta.
$$


It follows that


$$
|\mathcal D|
\ge
\frac{\sin\theta}{8}e^{(2N-1)\alpha}
\ge
\frac{e^{(2N-1)\alpha}}{16\sqrt N}.
\tag{5.4}
$$



The polynomial


$$
F(t)=
\frac{b_{N-1}R_N(t)-b_NR_{N-1}(t)}{\mathcal D}
$$


has real rational coefficients and satisfies $F(i)=1$. Moreover,


$$
|b_r|\le|T_r(z)|\le e^{r\alpha}.
$$


The sum of the absolute values of its two displayed coefficients is therefore at most


$$
32\sqrt N\,e^{-(N-1)\alpha}.
$$


Using (5.2),


$$
\|F\|_\eta^2
\le2048N e^{-2(N-1)\alpha}
\le2048N e^{-\sqrt N/3},
$$


where the last inequality follows from (5.3) and $N\ge6$.

Since $f_N$ is the exact minimizer, $\tau_N\le\|F\|_\eta^2$. ∎

The Chebyshev polynomials in this proof are auxiliary comparison objects. They do not replace the producer or introduce unrecorded arithmetic divisions.

---

## 6. Evaluated error bounds and new arithmetic gates

### 6.1 Ordinary and whole-error estimates

On $[0,1]$,


$$
\frac{w(t)}{e^{t-1}}
=
e+\frac{4e^{1-t}}{1+t^2}
\le5e<15.
$$


Thus


$$
\int_0^1f_N(t)^2w(t)\,dt\le15\tau_N.
\tag{6.1}
$$


Also,


$$
g_N(t)^2\le4(1-t)^{2N-4},
$$


so


$$
\int_0^1g_N(t)^2w(t)\,dt
\le\frac{28}{2N-3}.
\tag{6.2}
$$



For $N\ge4$, the explicit factorial expression gives


$$
T_N\ge\left(1-\frac2N\right)(2N)!\ge\frac12(2N)!.
\tag{6.3}
$$


Combining (3.11), Lemma 5.1, and (6.1)–(6.3),


$$
\int_0^1P_Nw
\le
30720N e^{-\sqrt N/3}
+
\frac{56}{(2N-3)(2N)!}.
$$


For $N\ge64$, the second term is at most $N e^{-\sqrt N/3}$. Hence


$$
\boxed{
0<
e+\pi-\frac{p_N}{q_N}
\le
2^{15}N e^{-\sqrt N/3}.
}
\tag{6.4}
$$



For a lower bound, $1-\tau_N\ge1/3$, $w\ge3$, and


$$
g_N(t)^2\ge(1-t)^{2N-4}
$$


give


$$
\int_0^1P_Nw
>
\frac1{(2N-3)T_N}.
\tag{6.5}
$$


Multiplication by the actual $q_N$ proves (0.1).

### 6.2 An exact rational error diagnostic

Define


$$
J_N=\int_0^1P_N(t)\,dt>0.
\tag{6.6}
$$


Then (2.6) gives the exact comparison


$$
3q_NJ_N\le\ell_N\le7q_NJ_N.
$$



This quantity is fully rational. In addition to direct coefficient integration, it has the decomposition


$$
J_N=
\frac1{\Delta^2}\int_0^1\Phi(t)^2\,dt
+
\frac{D}{\Delta T_N}B_N^{g},
\tag{6.7}
$$


where


$$
\boxed{
B_N^{g}
=
\frac1{2N-3}
+
\frac4{(2N-3)(2N-2)(2N-1)}
+
\frac{24}{(2N-3)(2N-2)(2N-1)(2N)(2N+1)}.
}
\tag{6.8}
$$


The first term is the finite rational Hilbert quadratic form in the coefficients of $\Phi$. The positive second term is completely evaluated.

Thus, for this family,


$$
\ell_N\longrightarrow0
\quad\Longleftrightarrow\quad
q_NJ_N\longrightarrow0
\tag{6.9}
$$


along any specified index set. This equivalence is useful for exact finite diagnostics, but it is not by itself an infinite-domain proof.

### 6.3 A proved source-content gate

Let


$$
d_{\Phi,N}=\gcd\{[t^j]\Phi(t):0\le j\le N\}.
$$


Because $g_N$ is primitive, Gauss’s lemma gives


$$
\boxed{
\gcd(T_Nd_{\Phi,N}^2,D\Delta)\mid h_N.
}
\tag{6.10}
$$


For $N\ge3$, $g_N(1)=0$. Evaluating the raw polynomial at $i$ and $1$ therefore gives


$$
\boxed{
h_N\mid T_N\gcd(\Delta^2,\Phi(1)^2).
}
\tag{6.11}
$$


These are genuine all-prime divisibility statements about the new polynomial content. Neither identifies that content exactly.

### 6.4 A proved endpoint-prime survival lemma

Let $p$ be prime with


$$
N<p\le2N-1.
$$


Among the denominators $1,\ldots,2N-1$, the only multiple of $p$ is $p$ itself. Therefore


$$
\boxed{
v_p(\lambda_N)=
\begin{cases}
1,&p\nmid s_{p-1},\\
0,&p\mid s_{p-1}.
\end{cases}
}
\tag{6.12}
$$


There is no cancellation with another $p$-denominator term.

If $p\nmid s_{p-1}$, then (4.11) additionally gives


$$
\boxed{v_p(q_N)=1+v_p(M_N).}
\tag{6.13}
$$


Such a prime survives the final all-prime gcd in full.

The converse statement “$p\mid s_{p-1}$ implies $p\nmid q_N$” is **not** asserted: a prime can still survive through $M_N/\mathfrak G_N$.

This lemma is a concrete new arithmetic gate. It specifically tests the complete, content-reduced quotient $S_N$, not an uncleared or selectively truncated column.

### 6.5 An actual denominator-height bound

From the finite Laguerre expansion,


$$
|E_j(i)|
\le N!\sum_{r=0}^j\binom jr\frac{|1-i|^r}{r!}
<N!3^j.
$$


Hence


$$
\Delta^2
\le (N+1)^4(N!)^8\,3^{8N}.
$$


The explicit expression for $T_N$ gives $T_N<(2N)!$, and


$$
\lambda_N\le\operatorname{lcm}(1,\ldots,2N-1)\le(2N-1)!.
$$


Since $h_N,\mathfrak G_N\ge1$,


$$
\boxed{
q_N
\le
(2N-1)!(2N)!(N+1)^4(N!)^8\,3^{8N}.
}
\tag{6.14}
$$


Stirling’s estimate yields (0.4).

This changes the arithmetic representation from a large mixed determinant to a polynomial-sized source calculation. But the bound is still factorial in $N$, whereas the proved analytic gain is stretched-exponential. Multiplying these bounds does not give primitive decay.

---

## 7. A complete hand-verifiable finite normalization at $N=3$

This is an auxiliary finite calculation, not an original-index instance and not an asymptotic theorem.

For $N=3$,


$$
(\alpha_j)=(6,0,-6,-10),\qquad
(\beta_j)=(0,6,6,2).
$$


Thus


$$
\mathsf U=172,\quad \mathsf V=-56,\quad \mathsf W=76,
$$




$$
\Delta=9936,\qquad D=7200,\qquad T_3=392.
$$


Furthermore,


$$
\Phi(t)=72(79-9t-59t^2-9t^3),
$$


and


$$
g_3(t)=1-t+t^2-t^3.
$$


The rational minimizer and its norm are


$$
f_3(t)=\frac{79-9t-59t^2-9t^3}{138},
\qquad
\tau_3=\frac{19}{69}.
$$



The raw normalization is


$$
\mathscr Z_3=38\,699\,845\,632,
$$


and the actual polynomial content is


$$
h_3=82\,944.
$$


After that paid division,


$$
M_3=466\,578,
$$




$$
\begin{aligned}
W_3(t)={}&153767-36564t-223817t^2-12270t^3\\
&+91841t^4+24294t^5+2847t^6.
\end{aligned}
\tag{7.1}
$$


Its content is $1$, certified already by


$$
31\,343\cdot36\,564-7\,453\cdot153\,767=1.
$$



The two source conditions are exactly


$$
W_3(i)=466\,578,
$$


and, using


$$
(a_0,\ldots,a_6)=(1,0,1,-2,9,-44,265),
$$




$$
\sum_{d=0}^6[t^d]W_3(t)\,a_d=466\,578.
$$



Polynomial division gives


$$
S_3(t)
=-312811-36564t+88994t^2+24294t^3+2847t^4.
$$


The complete endpoints are


$$
B_{\mathrm{end},3}=1\,155\,061,
$$




$$
4\int_0^1S_3(t)\,dt=-\frac{17\,687\,126}{15}.
$$


Therefore


$$
L_{\mathrm{ent},3}=\lambda_3=15,
$$




$$
A_3=35\,013\,041,
\qquad
\lambda_3M_3=6\,998\,670.
$$


The final all-prime gcd is exactly $7$, with Bézout certificate


$$
472\,981\cdot6\,998\,670
-
94\,543\cdot35\,013\,041
=7.
$$


Thus


$$
\boxed{
p_3=5\,001\,863,\qquad q_3=999\,810.
}
\tag{7.2}
$$



The rational integral diagnostic is


$$
J_3=\frac{16\,933\,507}{97\,981\,380},
\qquad
\boxed{q_3J_3=\frac{16\,933\,507}{98}.}
\tag{7.3}
$$


Consequently


$$
\frac{3\cdot16\,933\,507}{98}
\le
q_3(e+\pi)-p_3
\le
\frac{7\cdot16\,933\,507}{98}.
$$


This proves only the stated finite error interval.

The content gate is also nontrivial:


$$
\gcd(T_3d_{\Phi,3}^2,D\Delta)=41\,472
$$


is only half the actual content $82\,944$. The final gcd $7$ is another distinct payment. This finite example directly illustrates why the forced content, actual polynomial content, coefficient clearer, and final gcd must not be conflated.

---

## 8. Original-domain conclusion and the remaining mathematical obligation

### 8.1 Uniform statements at the same original indices

Every construction and identity above is valid for every integer $N\ge2$. The estimates in Section 5 and the upper bound in Section 6 hold for every $N\ge64$.

Therefore they hold pointwise at


$$
N=9^{18+32u},\qquad u\ge0.
$$


No auxiliary finite value such as $N=3$ is substituted for that original domain.

The new producer’s exact finite boundary is:

- basis indices $0,\ldots,N$;
- final polynomial degree $2N$;
- exponential moments and factorials only through $2N$;
- complete arctangent quotient degree $2N-2$;
- possible quotient denominators only through $2N-1$.

No successor moment, additional physical row, or omitted terminal condition is used.

### 8.2 Why this does not yet prove irrationality

A sufficient arithmetic lemma would be the following.

> **Original-index primitive-saving lemma — open.**  
> On an explicitly specified infinite subset of
> 

$$
> N=9^{18+32u},
>
$$


> the actual quantities defined in Section 4 satisfy
> 

$$
> \frac{\lambda_NM_N}{\mathfrak G_N}
> \le \exp\!\left(\frac{\sqrt N}{4}\right).
> \tag{8.1}
>
$$



If this were proved, then


$$
0<\ell_N
\le
2^{15}N\exp\!\left(-\frac{\sqrt N}{12}\right)
\longrightarrow0.
$$


If $e+\pi=A/B$ were rational, every nonzero such error would satisfy


$$
\ell_N=\frac{Aq_N-Bp_N}{B}\ge\frac1B,
$$


a contradiction.

But (8.1) is not established. In particular:

1. the bound (6.14) is much larger;
2. $\lambda_N$ survives completely in $q_N$;
3. the content bounds (6.10)–(6.11) do not determine $h_N$;
4. no theorem here controls the remaining all-prime factor $M_N/\mathfrak G_N$.

This is the precise obstruction to promoting the new rational approximation theorem to an irrationality proof.

### 8.3 A concrete follow-on gate in the opposite direction

The proved lower bound also makes a potential failure theorem precise.

> **Paid-denominator floor question — open.**  
> Does
> 

$$
> q_N\ge(2N-3)T_N
> \tag{8.2}
>
$$


> hold eventually on the original indices?

If so, (6.5) would give $\ell_N>1$ there, excluding this producer as a source of vanishing primitive errors.

This is not asserted as a theorem or promoted from the $N=3$ example. The point of (8.2), together with the proved prime-survival lemma, is to provide a specific arithmetic question about the new finite objects—not an appeal to a generic normality or almost-everywhere principle.

The exact bottleneck remains


$$
\boxed{
q_NJ_N
=
\frac{\lambda_NM_N}{\mathfrak G_N}\,J_N
\quad\text{on an infinite subset of the original indices.}
}
\tag{8.3}
$$



---

## 9. Bounded exact arithmetic proposal

No machine calculation is needed for the theorems proved above. The $N=3$ normalization is given with explicit exact certificates.

If a fresh independent normalization receipt is desired after the coordinator’s overlap gate, a bounded test at **$N=8$** is sufficient to inspect the new arithmetic mechanisms.

### Exact inputs

1. The polynomials
   

$$
E_j(t)=8!L_j(1-t),\qquad 0\le j\le8.
$$


2. Their Gaussian-integer values $E_j(i)$.
3. The definitions (3.3)–(4.12).
4. The moments $a_0,\ldots,a_{16}$ from (2.1).
5. The factorials through $16!$.
6. The exact norm
   

$$
T_8=16!-4\cdot15!+8\cdot14!-8\cdot13!+4\cdot12!.
$$



### Expected verifiable outputs

- the source integers $\mathsf U,\mathsf V,\mathsf W,\Delta,D$;
- the complete coefficients of $\Phi,\mathscr W_8,W_8,S_8$;
- the actual content $h_8$, with a coefficient Bézout certificate;
- verification of
  

$$
W_8(i)=M_8,\qquad
  \sum_{d=0}^{16}[t^d]W_8(t)a_d=M_8;
$$


- verification of both content divisibilities (6.10)–(6.11);
- $L_{\mathrm{ent},8}$, the actual $\lambda_8$, and its minimality certificate;
- $A_8,\mathfrak G_8,p_8,q_8$, with a final Bézout certificate;
- the exact rational numbers
  

$$
q_8J_8,\qquad \frac{q_8}{13T_8};
$$


- the residues
  

$$
s_{10}\pmod{11},\qquad s_{12}\pmod{13},
$$


  computed **after the actual content division**, and verification of the endpoint-prime survival lemma.

This test would establish only those finite facts. It would not establish (8.1), (8.2), or any original-index asymptotic.

---

## Final assessment

The new proved result is an explicit **full-degree, two-source, quadratic-contact producer** with:

- complete exponential, arctangent, and odd-power source terms;
- exact elimination of the $\log2$ source;
- a strictly positive whole error;
- a fully paid primitive normalization;
- an evaluated stretched-exponential ordinary-error bound;
- new content and endpoint-prime survival gates;
- a complete finite normalization certificate.

The old compact final gcd, old binary projection, and old adjacent-resultant obligations have not been solved or silently transferred.

The new family genuinely changes the available arithmetic representation and the contact geometry. Nevertheless, its proved analytic gain does not yet beat its **actual primitive denominator**. The unresolved mathematical task is to control


$$
\frac{\lambda_NM_N}{\mathfrak G_N}J_N
$$


at the same infinite original indices.

Accordingly, **neither rationality nor irrationality of $e+\pi$ is proved here**.
