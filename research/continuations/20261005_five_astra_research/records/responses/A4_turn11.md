> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## A4 — analytic audit and an evaluated infinite-subfamily rank theorem

I obtain an explicit infinite subfamily on which **all three smaller matrices have exactly evaluated ranks**, and the endpoint-image tests fail. This gives a substantially larger, explicit lower bound for the actual distinguished cofactor and final gcd. It does **not** determine the next actual radical form or an exact reduced-denominator valuation.

For A3’s analytic argument, the cylinder identity and total real-zero count can be justified independently. The displayed local calculations are internally consistent. However, the supplied documents do not include the global map and the five actual weights needed to verify the asserted properness and absence of other critical values independently. I therefore distinguish the valid continuation lemma from its incompletely documented application.

---

# 1. Independent analytic audit

## 1.1 Cylinder identity and exactly two real zeros

For $a>0$, let


$$
I(\tau)=\int_0^\infty x^{1/2}
\frac{d^3}{dx^3}e^{-ax^2/2+\tau x}\,dx.
$$


Initially, for $\Re\nu>3$, three integrations by parts give


$$
\int_0^\infty x^{\nu-1}E_\tau'''(x)\,dx
=-(\nu-1)(\nu-2)(\nu-3)
\int_0^\infty x^{\nu-4}E_\tau(x)\,dx.
$$


The left side is analytic for $\Re\nu>0$. Continuing the right side and setting $\nu=3/2$ gives


$$
I(\tau)=-\frac38\operatorname{FP}
\int_0^\infty x^{-5/2}E_\tau(x)\,dx.
$$


Consequently,


$$
\boxed{
I(\tau)=-\frac{\sqrt\pi}{2}a^{3/4}
e^{\tau^2/(4a)}D_{3/2}(-\tau/\sqrt a).
}
$$


Thus A3’s constant and negative argument are correct.

Here is a direct zero-count argument, avoiding an unsupported appeal to a positive-zero theorem. Write


$$
Y_\nu(z)=e^{z^2/4}D_\nu(z).
$$


The cylinder recurrence and derivative identities give


$$
Y_\nu'(z)=\nu Y_{\nu-1}(z).
$$


The convergent cylinder integral gives


$$
Y_{-1/2}(z)=\frac1{\sqrt\pi}
\int_0^\infty t^{-1/2}e^{-t^2/2-zt}\,dt>0
\qquad(z\in\mathbb R).
$$


Hence $Y_{1/2}$ is strictly increasing. It tends to $+\infty$ at $+\infty$, by $Y_{1/2}(z)\sim z^{1/2}$. At $-\infty$ it tends to $-\infty$: indeed the displayed integral grows exponentially there, and integrating
$Y_{1/2}'=\tfrac12Y_{-1/2}$ proves the assertion. Therefore $Y_{1/2}$ has exactly one zero, say $\alpha$.

Now


$$
Y_{3/2}'=\frac32Y_{1/2}.
$$


Thus $Y_{3/2}$ decreases before $\alpha$ and increases after $\alpha$. Its limits at both ends are $+\infty$: the positive-end limit follows from $Y_{3/2}(z)\sim z^{3/2}$, and the negative-end limit follows by integrating the negative, unbounded $Y_{1/2}$. Finally,


$$
D_{3/2}(0)=\frac{2^{3/4}\sqrt\pi}{\Gamma(-1/4)}<0.
$$


There are therefore exactly two real zeros, one negative and one positive. Neither is the unique minimum, so both are simple. Alternatively, simplicity follows from uniqueness for the cylinder differential equation.

**Verdict:** A3’s total real-zero count is correct, with the above independent proof.

## 1.2 Quartic map, density correction, and next transition coefficient

From the *displayed* $Q_4$ and $L_2$, hemisphere averages give


$$
\langle t_i^4\rangle=\frac15,\qquad
\langle t_i^2t_j^2\rangle=\frac1{15},\qquad
\langle t_i^2\rangle=\frac13.
$$


These yield exactly


$$
\langle Q_4\rangle=-\frac b{60}-\frac{b^2}{5M},
\qquad
\langle L_2\rangle=\frac{b-2}{3}-\frac b{6M}.
$$


Radial inversion of $s=bR^2+Q_4+\cdots$ gives the relative correction


$$
\frac{\langle L_2\rangle}{b}
-\frac{5\langle Q_4\rangle}{2b^2}
=\frac{8b-15}{24b}+\frac1{3M}.
$$


The displayed quadratic weight correction has average, after division by $b$,


$$
\frac{6b^2-b}{3b}=2b-\frac13.
$$


Thus


$$
B_3=A\left(\frac{8b-15}{24b}+\frac1{3M}\right)
+2b-\frac13
$$


follows correctly from those local inputs.

Likewise, expanding $T^3=(-r+s)^3$, the first two terms of


$$
D^3=T^3\partial_s^3+3T^2\partial_s^2+T\partial_s,
$$


and the leading $f_2D^2$ term reproduces the coefficient $6r^2A$ in A3’s $\Xi$. The $f_4$ term and cubic phase correction have the displayed orders. The quartic phase first contributes at relative order $n^{-1}$, not $n^{-1/2}$.

**Limitation of this audit:** the global formulas defining the map and the weights $F,G,B,A_h$ are absent from the supplied sources. I can verify the arithmetic consequences of (3) and the stated quadratic weight expansion, but cannot independently derive those expansions from the actual map. Similarly, the global localization and whole exponential bound remain supplied dependencies.

## 1.3 Continuation and boundary terms: a precise conditional lemma

The continuation mechanism is valid under the following explicit hypotheses.

Let $f_h^{--}$, $0\le h\le4$, be real analytic on $(-r,0)$, and define there


$$
\mathcal F^{--}=\sum_{h=0}^4(D^*)^hf_h^{--},
\qquad D^*f=-(Tf)'.
$$


Assume:

1. the total effective amplitude agrees locally with $\mathcal F^{--}$ at the saddle;
2. $\mathcal F^{--}$ has a nonzero divergent singularity at $-r$;
3. the phase has exactly two inverse branches between its interior maximum and the level $\phi_c(-r)$, with the right endpoint of this continuation strictly inside $(-r,0)$.

Then some even Morse coefficient at the saddle is nonzero.

Indeed, in a local Morse coordinate $x$,


$$
\phi_c(T)=\phi_c(T_*)-x^2.
$$


If every even coefficient of the analytic transformed amplitude vanished, that amplitude would be odd. For the two branches $T_-(u),T_+(u)$, this is equivalent to


$$
\frac{\mathcal F^{--}(T_-(u))}{\phi_c'(T_-(u))}
=
\frac{\mathcal F^{--}(T_+(u))}{\phi_c'(T_+(u))}.
$$


Analytic continuation propagates this identity to the endpoint phase level. The left side diverges, whereas the right side stays finite—a contradiction.

There is **no legitimate global ordinary integration by parts across the singular endpoint** in this argument. To obtain the local effective amplitude, use a smooth cutoff supported inside the analytic interval and equal to one near the saddle. Integration by parts then has no endpoint terms; cutoff-derivative terms are off-saddle. Globally, $(D^*)^hf_h$ should instead be interpreted as a distribution if one wishes to include support endpoints.

The displayed endpoint data imply


$$
(D^*)^3f_3(-r+s)
=\frac38r^3AK\,s^{-5/2}+O(s^{-3/2}),
$$


while the stated $f_4$ leading order contributes only $s^{-3/2}$. Thus the required divergent coefficient is nonzero, conditional on those actual density expansions.

**Application status:** A3’s continuation past the $++$-component birth does not improperly change the germ: it continues the $--$ germ, not the total density. But the assertion that this germ is analytic throughout $(-r,0)$ still requires the actual global map. A sign restriction alone does not prove properness or exclude another critical value. Those two global assertions are not independently established by the source material supplied here.

---

# 2. An explicit infinite subfamily with evaluated ranks

Use A4 turn 10’s parameters, and put


$$
L=\frac Ht,\qquad \delta=L-C.
$$


The parameter relations simplify to


$$
R=\frac{L-1}{2},\qquad b+1=\frac{3\delta}{2}.
$$


Both $L$ and $C$ are odd, so $\delta$ is even.

Consider the specified subfamily


$$
\boxed{
\mathcal J^\dagger=
\{j\in\mathcal J_*:0<L-C<L/6\}.
}
$$


Equivalently,


$$
A<H<\frac65A,\qquad A=4^j-1.
$$


On this subfamily $\delta\ge2$. Write


$$
s=b+1=\frac{3\delta}{2}.
$$



### Infinitude

The number $\log_3 4$ is irrational, since a rational relation would give $4^u=3^v$ for positive integers $u,v$. Therefore the fractional parts of $3m\log_3 4$ are dense modulo one.

Choose them in a closed interval strictly inside


$$
(1-\log_3(6/5),1).
$$


For infinitely many $j=3m$, the next power of $3$ above $4^j-1$ then lies strictly between $A$ and $6A/5$. Call it $H$. For sufficiently large such $j$,


$$
3H\le4A+5<9H,
$$


so this $H$ is exactly the $H=3^{h-1}$ used in $\mathcal J_*$. Also $H-A\ge1$, giving $3H\ge3n-2$. Thus these indices belong to $\mathcal J^\dagger$.

This proves infinitude without making a finite computation stand in for it.

---

# 3. Exact ranks by a binomial recurrence

Because $L$ is a power of $3$,


$$
(z-1)^C=\frac{z^L-1}{(z-1)^\delta}
\quad\text{in }\mathbb F_3[z].
$$


For $0\le k<L$, since $\delta$ is even,


$$
[z^k](z-1)^C
=-\binom{\delta+k-1}{\delta-1}.
$$


Let


$$
a_k=\binom{\delta+k-1}{\delta-1}.
$$


Its generating function is $(1-z)^{-\delta}$, so it satisfies the order-$\delta$ recurrence


$$
(E-1)^\delta a_k=0.
$$


This recurrence is valid integrally, hence also modulo $3$, without dividing by $(\delta-1)!$.

All coefficient indices occurring in $H_0,H_1,J$ lie in $[0,L-1]$. The smallest is that of $H_1$:


$$
R-1-2(s-1)=\frac{L-6\delta+1}{2}>0.
$$


Therefore the recurrence gives


$$
\rho_0,\rho_1,\rho_J\le\delta.
$$



For completeness, the matching lower bound does not rely on a possibly vanishing binomial determinant product. For every integer $k\ge0$,


$$
\boxed{
\det(a_{k+i+j})_{0\le i,j<\delta}
=(-1)^{\delta(\delta-1)/2}.
}
$$


To prove this, apply successive forward-difference column operations, followed by the same row operations. The resulting entry is


$$
\Delta^{i+j}a_k.
$$


It is zero when $i+j\ge\delta$, and is $1$ when $i+j=\delta-1$. The resulting matrix is anti-triangular with anti-diagonal $1$, proving the formula.

Each smaller matrix contains such a $\delta$-square minor after reversing suitable rows and columns. Its determinant is a unit modulo $3$. Hence


$$
\boxed{\rho_0=\rho_1=\rho_J=\delta
\qquad(j\in\mathcal J^\dagger).}
$$



This evaluates the three parameter families rather than merely replacing them with other rank tests.

---

# 4. Evaluated endpoint-image tests

Every column of these matrices obeys, in its row index, the order-$\delta$ recurrence with characteristic root $1$. But


$$
(E-1)^\delta(-1)^u=(-2)^\delta(-1)^u
=(-1)^u\ne0\quad\text{in }\mathbb F_3.
$$


Since


$$
s=\frac{3\delta}{2}>\delta,
$$


there is room to test the recurrence on $s$ consecutive rows. Consequently,


$$
\boxed{
a_s\notin\operatorname{im}H_0,\qquad
a_s\notin\operatorname{im}H_1,\qquad
a_s\notin\operatorname{im}J.
}
$$


Thus the endpoint functional is nonzero on the actual first residue radical.

For the fourth test:

- if $\delta=2$, $J^T$ has two rows and rank two, so $a_{s-1}\in\operatorname{im}J^T$;
- if $\delta\ge4$, then $s-1>\delta$, and the same recurrence proves
  

$$
a_{s-1}\notin\operatorname{im}J^T.
$$



All four image tests are therefore evaluated on the stated subfamily.

---

# 5. Actual nullity, distinguished cofactor, and gcd consequences

Using the supplied first-residue identification,


$$
\operatorname{rank}\bar S
=(c+1)\delta+(c-2)\delta+2\delta=t\delta.
$$


Since


$$
d=ts-1=\frac{3t\delta}{2}-1,
$$


the exact first-residue nullity is


$$
\boxed{\nu=\frac{t\delta}{2}-1.}
$$


In particular, $t\ge9$ and $\delta\ge2$ give $\nu\ge8$.

For the **actual** integral lift $S$, residue-unit elimination proves


$$
\boxed{
v_3(\det S)\ge\frac{t\delta}{2}-1,\qquad
v_3(\operatorname{adj}(S)_{00})\ge\frac{t\delta}{2}-2.
}
$$


These are actual cofactor lower bounds, not exact cofactor depths. The nonzero endpoint projection does not by itself upgrade them to equalities: the divided radical form could still be singular or have further endpoint cancellation.

Using the normalization identities supplied in A4 turn 10, the final gcd satisfies


$$
\boxed{
v_3(g)\ge d+\nu=2t\delta-2
\qquad(j\in\mathcal J^\dagger).
}
$$


No subtraction of these lower bounds is made to claim a valuation of $q$.

---

# 6. Why the next actual radical form remains unresolved

The new rank theorem supplies an explicit recurrence-based radical. It does not supply the actual matrix modulo $9$.

If a unimodular basis with radical columns $Z$ gives


$$
P^TSP=
\begin{pmatrix}E&B\\B^T&C_1\end{pmatrix},
\qquad E\text{ a unit block},\quad B,C_1\equiv0\pmod3,
$$


the next actual form is


$$
\boxed{
W=\frac{C_1-B^TE^{-1}B}{3}.
}
$$


Its residue requires the actual $C_1\bmod9$; its next digit also requires the Schur correction. Replacing $S$ by the integer binomial representative would not compute this form.

The supplied documents do not give a general all-pole assembly formula with its coefficient ranges at arbitrary $j\in\mathcal J^\dagger$. The resolved $n=65$ pole list cannot supply it. Accordingly I do not claim an evaluated higher saturation or exact cofactor depth.

---

# 7. Final normalization and whole evaluated error

For the integer coefficient pair belonging to the complete weighted construction, retain


$$
g=\gcd(|A|,|B|),\qquad
q=\frac{|B|}{g},\qquad
p=-\frac{\operatorname{sgn}(B)A}{g}.
$$


For $n=4^j+1$, $k=(n+1)/2$,


$$
\boxed{
q(e+\pi)-p
=\frac{\operatorname{sgn}(B)}g\bigl(A+B(e+\pi)\bigr)
=\frac{\operatorname{sgn}(B)\ell^k}{g}
\det H_{\rm complete}.
}
$$


The new arithmetic conclusions hold on $\mathcal J^\dagger$, conditional only on the supplied identification of the actual first residue and its normalization formulas. They do not prove $B\ne0$ or nonvanishing of this whole error independently. Those remain dependent on the inherited regular-family theorems described in the sources; with those inputs, $B\ne0$ and at most one whole error vanishes.

No decay estimate for the actual primitive error, and no irrationality decision, follows.

## (1) New result and proof status

- **Proved independently:** the cylinder constant, negative argument, and exactly two simple real zeros.
- **Audited algebraically:** the displayed quartic/measure correction and full first transition correction, conditional on the stated local map and weight expansions.
- **Proved conditional continuation lemma:** vanishing of all even Morse coefficients contradicts analytic continuation of the same component germ to a nonzero endpoint singularity.
- **Proved on an explicit infinite subfamily:** all three ranks equal $\delta$; all endpoint-image tests are evaluated; the actual first-residue nullity is $t\delta/2-1$.
- **Actual arithmetic consequence:** distinguished-cofactor depth at least $t\delta/2-2$, and final gcd depth at least $2t\delta-2$. Exact depths remain unproved.

## (2) Exact remaining bottleneck

Analytically, independently verify the global $--$ map’s properness and critical-value list from its actual formula.

Arithmetically, assemble the actual matrix modulo $9$ and higher on the new subfamily, retaining every surviving pole and Schur correction. This is necessary to evaluate the divided radical form, distinguish exact cofactor depth from a lower bound, and control the actual denominator after the final gcd.

## (3) Computation request

**None at present.** No further $n=65$ computation is needed. The rank and endpoint results above are exact symbolic proofs. The missing next-stage input is a general actual all-pole assembly identity, not another finite rank table.
