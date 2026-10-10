> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Valid-prime m-ray Cartier reduction

## Scope and status

This note gives an exact reduction of the remaining fresh-prime obstruction
on the valid ray



$$
p=6m+q,\qquad p>6m,\qquad q\text{ odd},\qquad 3\nmid q.
$$



It also records an exact-computation pattern for the same known obstruction.
The reduction is proved below.  The final factorial divisibility is currently
a conjecture supported by exact scans, not yet a uniform theorem.

## 1. Weighted Cayley residue

Put



$$
P(z)=1+z+z^2+z^3=(1+z)(1+z^2),\qquad
 E=2m+q-1=\frac{p+2q-3}{3},
$$



and



$$
J_s=\frac{P(z)^{E-s}}{z^q(1-z)^q}\,dz,
 \qquad c_s=\operatorname {Res}_0J_s,
 \qquad r_s=\operatorname {Res}_1J_s.
$$



The exact Cayley calculation gives



$$
\lambda_s=2^{E+2s+1-q}(2c_s+r_s)\pmod p.
$$



The known adjacent relation gives



$$
16(10m+2)(10m+3)\lambda_0
 -4(10m+3)(20m+5)\lambda_1
 +8(2m+1)(4m+1)\lambda_2=0.
$$



Since the last coefficient is a p-unit when p>6m, a common zero of
$\lambda_0,\lambda_1$ forces $\lambda_2=0$.

## 2. Cartier coefficient window

Set



$$
W_s=[z(1-z)]^{p-q}P^{E-s}=z^{p-q}H_s,
 \qquad H_s=(1-z)^{p-q}P^{E-s}.
$$



Because



$$
J_s=[z(1-z)]^{-p}W_s\,dz,
$$



the numerator of $\mathcal C(J_s)$ is linear.  The equation
$2c_s+r_s=0$ says that its coefficients at $1,z$ agree.  The two
coefficients are



$$
a_s=[z^{p-1}]W_s=[z^{q-1}]H_s,
$$



and



$$
b_s=[z^{2p-1}]W_s.
$$



The initial factor $z^{p-q}$ is essential: $W_s$ itself is not
reciprocal about its full degree.  Instead $H_s$ is reciprocal of degree
$2p+q-3-3s$, and hence



$$
b_s=[z^{p-2-3s}]H_s.
$$



This is the corrected reflection formula used below.

## 3. Eliminate q on the valid ray

Now use $q=p-6m$.  Since



$$
E-2=p-4m-3,
$$



the relevant reciprocal factor is



$$
H_2=(1-z)^{p-q}P^{E-2}.
$$



Using $P=(1-z^4)/(1-z)$, and then Frobenius in characteristic p,
gives through degree $<p$



$$
(1-z)^{p-q}P^{E-2}
 \equiv
 G_m(z):=\frac{(1-z)^{10m+3}}{(1-z^4)^{4m+3}}
 =\frac{(1-z)^{6m}}{P(z)^{4m+3}}
 \pmod {z^p}.
$$



Thus the rational function is independent of q and p; p only selects the
index and its residue modulo 4.

Define the two coefficient windows



$$
A_r=[z^{q-r}]G_m=[z^{p-6m-r}]G_m,
 \qquad
 B_r=[z^{p-r}]G_m.
$$



For $s=2$, the Cartier condition is $A_1=B_8$.  For $s=1$, it is



$$
A_1+A_2+A_3+A_4=B_5+B_6+B_7+B_8.
$$



Therefore put



$$
\mathcal L_1=A_1-B_8,
\qquad
 \mathcal L_2=A_2+A_3+A_4-B_5-B_6-B_7.
$$



The exact scaled congruences are



$$
\lambda_2=2^{2m+4}\mathcal L_1,
\qquad
 \lambda_1=2^{2m+2}(\mathcal L_1+\mathcal L_2)
 \pmod p.
$$



Thus a common zero of $\lambda_0,\lambda_1$, which forces
$\lambda_2=0$, necessarily forces both $\mathcal L_1,\mathcal L_2$
to vanish.

Let $\epsilon=p\bmod4\in\{1,3\}$.  Expanding the numerator and the
negative binomial denominator gives the p-free rational representative



$$
A_r^{(\epsilon)}(m)=
 \sum_{\substack{0\le j\le10m+3\\
 j\equiv\epsilon-6m-r\ (4)}}
 (-1)^j\binom{10m+3}{j}
 \binom{(10m+8-r-j)/4}{4m+2}.
$$



Because $4m+2<p$, reducing this rational number modulo p is legitimate,
and



$$
A_r\equiv A_r^{(\epsilon)}(m)\pmod p.
$$



The second window has the equally explicit representative



$$
B_r^{(\epsilon)}(m)=
 \sum_{\substack{0\le j\le10m+3\\
 j\equiv\epsilon-r\ (4)}}
 (-1)^j\binom{10m+3}{j}
 \binom{(16m+8-r-j)/4}{4m+2}.
$$



Every common zero of $\lambda_0,\lambda_1$ therefore forces



$$
p\mid\operatorname {num}(\mathcal L_1),\qquad
 p\mid\operatorname {num}(\mathcal L_2).
$$



Equivalently, the two obstruction values are



$$
\mathcal L_1=[z^{p-6m-1}]G_m-[z^{p-8}]G_m,
$$





$$
\mathcal L_2=
 \sum_{r=2}^4[z^{p-6m-r}]G_m-
 \sum_{r=5}^7[z^{p-r}]G_m.
$$



### Exact identification with the original fixed-m coefficients

For degree $4m+s<p$, Frobenius also reduces the original logarithmic
coefficient itself to the p-independent integer



$$
\Lambda_s(m)=[z^{4m+s}]
 \frac{(1-z)^{6m}(1+z)^{1+3s}}
 {(1+z^2)^{4m+1+s}}.
$$



The corrected obstruction pair satisfies the exact rational identities



$$
\mathcal L_1=\frac{\Lambda_2}{2^{2m+4}},
\qquad
 \mathcal L_1+\mathcal L_2=\frac{\Lambda_1}{2^{2m+2}}.
$$



These identities prove that the representatives are independent of
$\epsilon$.  They also show that the m-ray pair is the old
$(\Lambda_1,\Lambda_2)$ obstruction in new coordinates, rather than a
logically stronger obstruction.  A finite exact proof by section reflection,
projection to the pole at $z=-1$, and a Cayley substitution is given in
`sources/corrected_mray_epsilon_projection_proof.md`.

## 4. Exact experimental factorial certificate

For each $m$, put $\mathcal L_1,\mathcal L_2$ over their least common
denominator $D$.  The probe verifies that $D$ is a power of 2.  Write



$$
\widetilde{\mathcal L}_i=D\mathcal L_i\in\mathbb Z.
$$



For both $\epsilon=1,3$, exact arithmetic through $1\le m\le1000$
gives



$$
\gcd\bigl(\widetilde{\mathcal L}_1,
            \widetilde{\mathcal L}_2\bigr)
 \mid (6m)!.
$$



This is stronger than merely saying that every common prime divisor is at
most $6m$.  A uniform proof would immediately finish the fresh-prime
case, because the candidate p satisfies $p>6m$.

The factorial-gcd statement is also stronger than needed on the exceptional
ray $p=10m+3$, where the original coprimality problem has already been
proved separately.  That ray should remain separated when using the
$(\Lambda_1,\Lambda_2)$ reformulation, since intermediate equivalences in
the adjacent-recurrence argument can degenerate there.

The reproducible corrected probe is
`scripts/mixed_cubic_valid_mray_cartier_gcd_probe.py`.  Results produced by
the earlier discarded same-A formula are explicitly obsolete and are not
evidence for this statement.  The byte-stable $m\le1000$ output is
`results/mixed_cubic_valid_mray_cartier_gcd_probe_m1000.json`;
it also verifies the direct corrected A/B formulas against the
$(\Lambda_1,\Lambda_2)$ coefficients through $m=30$.  This is finite
evidence only, not a proof of the displayed divisibility.

### Four-section forced factors

Write



$$
(1-z)^{10m+3}=\sum_{a=0}^3z^aA_a(z^4),
\qquad
 A_a(u)=(-1)^a\sum_{\ell=0}^{d_a}
 \binom{10m+3}{a+4\ell}u^\ell,
$$



where



$$
d_a=\left\lfloor\frac{10m+3-a}{4}\right\rfloor.
$$



Set



$$
C_a(k)=[u^k]\frac{A_a(u)}{(1-u)^{4m+3}}.
$$



Then $C_a(k)$ is a polynomial of degree at most $4m+2$, and



$$
C_a(k)=\sum_{\ell=0}^{d_a}(-1)^a
 \binom{10m+3}{a+4\ell}
 \binom{k-\ell+4m+2}{4m+2}.
$$



For every



$$
1\le t\le e_a:=4m+2-d_a,
$$



each binomial in the sum vanishes at $k=-t$.  Hence the exact forced
factorization



$$
C_a(k)=(k+1)(k+2)\cdots(k+e_a)R_a(k)
$$



holds, with $\deg R_a\le d_a$.  If $m=2v$, all four values are
$e_a=3v+2$.  If $m=2v+1$, then
$e_0=e_1=3v+3$ and $e_2=e_3=3v+4$.

There are now two section evaluations, not one.  Put



$$
\epsilon\equiv p\pmod4,
 \qquad
 \delta\equiv q\equiv\epsilon-2m\pmod4,
$$



with $\epsilon,\delta\in\{1,3\}$.  The A-window uses base index



$$
k_q=\frac{-6m-\delta}{4}\pmod p,
$$



while the B-window uses



$$
k_p=\frac{-\epsilon}{4}\pmod p.
$$



For a base residue $\rho\in\{1,3\}$, the coefficient at distance r is



$$
C_{(\rho-r)\bmod4}
 \left(k+\left\lfloor\frac{\rho-r}{4}\right\rfloor\right).
$$



Applying this once with $(\rho,k)=(\delta,k_q)$ gives $A_r$, and
once with $(\rho,k)=(\epsilon,k_p)$ gives $B_r$.  This explicitly
corrects the discarded same-A formula, which incorrectly reflected
$W_s$ about its full degree and compared two coefficients from the
A-window.

Finally, logarithmic differentiation gives the exact residual recurrence



$$
n c_n=-(10m+3)(c_{n-1}+c_{n-2}+c_{n-3})
 +(n+6m+5)c_{n-4},
$$



where $c_{4k+a}=C_a(k)$.  This is an explicit four-section contiguous
system for the residual polynomials $R_a$.  The missing uniform step is
an integral Bezout consequence of this system showing that the two displayed
evaluations generate the unit ideal after inverting $(6m)!$.

The exact corrected fixed-m factor checker is
`scripts/analyze_mray_four_sections.py`.

### Separate common-index summand forms

Within either window, put $a=j+r$.  The A-window uses the congruence class



$$
a\equiv\epsilon-6m\pmod4,
$$



and the generalized binomial factor



$$
H_A(a)=\binom{(10m+8-a)/4}{4m+2}.
$$



Since a is odd,



$$
A_r=(-1)^{r+1}\sum_{a\equiv\epsilon-6m\ (4)}
 \binom{10m+3}{a-r}H_A(a).
$$



The B-window separately uses $a\equiv\epsilon\pmod4$ and



$$
H_B(a)=\binom{(16m+8-a)/4}{4m+2},
$$



so



$$
B_r=(-1)^{r+1}\sum_{a\equiv\epsilon\ (4)}
 \binom{10m+3}{a-r}H_B(a).
$$



The ordinary binomial is zero outside its natural range.  The step ratios
are



$$
\frac{H_A(a+4)}{H_A(a)}
 =\frac{-6m-a}{10m+8-a},
 \qquad
 \frac{H_B(a+4)}{H_B(a)}
 =\frac{-a}{16m+8-a}.
$$



These formulas provide a correct step-four summation framework, but the
exact $\Lambda_1,\Lambda_2$ identification above shows that they do not
yet provide new leverage over the pre-existing obstruction.

## 5. Correct weighted telescoper

For completeness, the exact five-term recurrence for the weighted residue
sequence is re-derived by
`scripts/weighted_cayley_recurrence_obstruction_certificate.py`.  Its replay

```text
python scripts/weighted_cayley_recurrence_obstruction_certificate.py \
  --output results/weighted_cayley_recurrence_obstruction_certificate.json
```

records the recurrence, the exact telescoper



$$
H_s=\frac{z(1-z)U_s(z)}{P(z)^3},
$$



and verifies the rational identity exactly (`telescoper_identity_zero = true`).

### Why the three-term propagation shortcut stops

The separate exact certificate
`sources/weighted_cayley_three_term_no_go.md` proves that the analogous
uniform rational three-term telescoper at the next row does not exist.  The
complete simple-pole Hermite system at $s=1$ has determinant



$$
2^9 3^7 7(q-3)(2q-9)^2(5q-9)(5q-6).
$$



On valid prime rays it is nonsingular except for the explicitly checked
endpoint $p=7$ and the exceptional ray $p=10m+3$.  The endpoint gives
no recurrence coordinates, while the exceptional ray gives only the
already-known identity $B_2=0$, with no $B_3$ term.  Thus the special
$s=0$ relation cannot be iterated to a terminal anchor by this mechanism.
This no-go result does not exclude prime-specific characteristic-$p$
certificates with higher $P$-pole order.
