> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 Turn 8 — Referee report on the seeded contact reduction, terminal projection, binary force, and adjacent ternary sectors

## 1. Executive assessment

The supplied work does **not** establish either rationality or irrationality of $e+\pi$. The new arithmetic nevertheless contains several valid and useful results.

My principal conclusions are as follows.

1. **A3’s seeded factorial companion and large-prime gcd equality are correct**, under the stated nonvanishing and actual-contact hypotheses. In particular, the proof correctly pays the additional planar content
   

$$
b_c=\gcd(d_c,|C|)
$$


   and evaluates the valuation of the **actual**
   

$$
g_{\rm aff}=\gcd(|F|,|CM|).
$$


   No assumption that $W_{j,3}$ is a unit is needed. The equality is an exact reduction of the gcd target, not a subfactorial estimate.

2. **A2’s exact normal vector, unit norm, projector, and unitriangular content identities are valid.** Its stronger relative-source congruence remains an unproved sufficient condition. A terminal-coordinate test substantially sharpens its compatibility requirements. Under the original moment-column specialization described below, the complete second source gives
   

$$
\psi_{b-1}\equiv0\pmod{29},
$$


   and consequently
   

$$
v_{29}\!\left((PY)_b\right)=v_{29}(W_b).
$$


   Thus the terminal obstruction is not automatically removed by tangential projection. In particular, the stronger vector congruence requires
   

$$
v_{29}(W_b)\ge c+4+\nu.
$$


   No original index violating this inequality is certified here.

3. **A5’s force identities, parity theorem, content bounds, Lucas-mask criterion, and projected torsion quotient are valid.** There is a useful improvement: the displayed recurrence does **not** require division of an unknown force value by $2$. Its coefficients can be divided integrally in advance. This gives a recurrence with integer coefficients, hence no accumulated loss of one bit per step.

   It also gives the following stronger infinite-family result:
   

$$
\boxed{
   (\mathfrak f_0,\mathfrak f_1,\mathfrak f_2,\mathfrak f_3)
   \equiv(2,1,3,1)\pmod4,\qquad
   \mathfrak f_i\equiv0\pmod4\quad(i\ge4).
   }
$$


   This is proved below, not extrapolated from the parent receipts.

4. **A1’s adjacent-window obstruction is correct for its explicit candidate matrix.** The original congruences $s\equiv1\pmod9$ and $c'\equiv4\pmod9$, and the nonnegative determinant-valuation layers, do imply
   

$$
\dim\ker K_{26}\ge242.
$$


   This is a lower bound on nullity, not an exact rank. I give a sharper exact reduction of the total nullity to two square-sector kernels and one boundary-coordinate restriction. Transport of this candidate operator to the actual ternary producer remains conditional.

The previously closed core-depth-$26$, paid-contact, weak prime-$29$ tail, and complete-boundary reviews are not reopened.

---

## 2. Domains and proof conventions

The four original index domains are different and must not be mixed.

| Stream | Original domain |
|---|---|
| A3 | $n=15^r$ or $105^r$, $r\ge2$ |
| A2 | $b=3^{249005515+574312172u}$, $n=2001b$, $u\ge0$, $u\equiv2\pmod{29^9}$ |
| A5 | $b=9^{18+32u}$, $n=4002b$, $u\ge0$ |
| A1 | $j>0$, $j\equiv84645\pmod{531441}$, with the original $D/H$-window and finite terminal $Y_m$ |

Auxiliary recurrence indices do not enlarge these approximation domains.

Throughout, the valuation of a nonzero vector is the minimum valuation of its coordinates, and $v_p(0)=+\infty$. A subscript $>N$ on an integer gcd means its product of prime-power factors at primes greater than $N$.

I distinguish:

- identities proved directly from displayed formulas;
- deductions using expressly retained producer results;
- conditional specializations needing an original-object identification;
- finite receipts;
- open infinite-family obligations.

---

# Part I. A3: seeded factorial companion and exact paid gcd

## 3. The factorial companion retains the actual seed

Put $m=n+1$, $N=n+2$. The reference recurrence is


$$
N\tau_{n+2}=(2n+3)\tau_{n+1}+m\tau_n,
\qquad \tau_0=\tau_1=1.
$$


The companion has the same recurrence and


$$
\sigma_0=0,\qquad \sigma_1=1.
$$



Its Casoratian


$$
\mathcal C_n=\tau_n\sigma_{n+1}-\tau_{n+1}\sigma_n
$$


satisfies


$$
\mathcal C_{n+1}=-\frac{n+1}{n+2}\mathcal C_n,\qquad \mathcal C_0=1.
$$


Therefore


$$
\boxed{\mathcal C_n=\frac{(-1)^n}{n+1}.}
$$



Writing $s_n=n!\sigma_n$ gives the integral recurrence


$$
s_0=0,\quad s_1=1,\quad
s_{n+2}=(2n+3)s_{n+1}+(n+1)^2s_n.
$$



The response formula is also consistent. If


$$
U_n(z)=\sum_{k\ge0}u_k(n)\frac{z^k}{k!},
\qquad
u_{k+1}=(n+k+1)u_k+1,\quad u_0=0,
$$


then


$$
(1-z)U_n'(z)=(n+1)U_n(z)+e^z.
$$


Consequently,


$$
U_n(z)=\frac{e^zS_n(z)-E_n}{(1-z)^{n+1}},
$$


because


$$
\frac{d}{dz}\bigl(e^zS_n(z)\bigr)=e^z(1-z)^n.
$$


Multiplication by $q(z)^n$ gives A3’s displayed coefficient formula for $b_k(n)$.

At original odd indices, the endpoints


$$
\xi_n=\frac m2b_n(n),\qquad
\zeta_n=b_{n+1}(n)-\frac m2b_n(n)
$$


are integral. Reusing the established actual transverse identity,


$$
\mathcal K_n=\tau_n\zeta_n-\tau_{n+1}\xi_n,
$$


define


$$
U^\sharp=\xi_n+2m!s_n,\qquad
V^\sharp=\zeta_n+2n!s_{n+1}.
$$


The Casoratian gives


$$
\tau_nV^\sharp-\tau_{n+1}U^\sharp
=\mathcal K_n+2(-1)^n(n!)^2.
$$


Hence, on the original odd domain,


$$
\boxed{
2(n!)^2-\mathcal K_n
=\tau_{n+1}U^\sharp-\tau_nV^\sharp.
}
$$



The seed check at $n=2$ is correct:


$$
s_2=3,\quad s_3=19,\quad U_2^\sharp=36,\quad V_2^\sharp=83,
$$


and


$$
2\cdot83-4\cdot36=22=14+8.
$$


Thus the transverse seed $14$ has not been erased.

This construction is sequence-specific. It does not contradict the closed nonexistence result for a universal rational tensor gauge.

---

## 4. Every primitive payment in the contact reduction

For one retained actual contact, write


$$
\pi=\frac{\mathbf c}{\kappa}
=\varepsilon\frac{(z\times W)^T}{h}
=(d_cA,d_cB,c_0),
$$


where


$$
\gcd(A,B)=1,\qquad \gcd(d_c,c_0)=1.
$$



These are separate normalizations:

- $h$: content of the actual cross product;
- $\kappa$: content of the actual transformed row $\mathbf c$;
- $d_c$: content of its first two primitive coordinates;
- $b_c=\gcd(d_c,|C|)$: the additional planar payment.

None is the final row content or the final primitive-denominator gcd.

The contact equations are


$$
d_c(AP+BQ)+c_0F=0,
$$




$$
d_c(AW_1+BW_2)+c_0W_3=0.
$$


Since $\gcd(d_c,c_0)=1$,


$$
\boxed{d_c\mid F,\qquad d_c\mid W_3.}
$$



Set


$$
f_0=F/d_c,\qquad \omega=W_3/d_c,\qquad
b_c=\gcd(d_c,|C|).
$$


Then


$$
\mathscr E=
\frac{d_c(AU^\sharp+BV^\sharp)+c_0C}{b_c}
$$


is integral. The division by $b_c$ is exact in the original numerator, not a replacement of that numerator by a more favorable one.

Choose $s,t\in\mathbb Z$ with $As+Bt=1$, and put


$$
\mathcal R=A\widehat h+B\widehat\ell,\qquad
\nu=s\widehat\ell-t\widehat h,\qquad
J=Qs-Pt.
$$


The coordinate change has determinant $1$, and


$$
M=J\mathcal R+c_0f_0\nu.
$$


Using the companion identity gives


$$
\boxed{
\Theta=b_c\bigl(\mathcal RH+f_0\nu\mathscr E\bigr),
}
$$


where


$$
H=\frac{CJ+F(tU^\sharp-sV^\sharp)}{b_c}\in\mathbb Z.
$$


Similarly,


$$
\boxed{
\widehat{\mathcal B}
=b_c\bigl(\mathcal RH_W+\omega\nu\mathscr E\bigr),
}
$$


with


$$
H_W=
\frac{C(W_2s-W_1t)+W_3(tU^\sharp-sV^\sharp)}{b_c}\in\mathbb Z.
$$



The integrality of both coefficients uses the paid divisibilities $b_c\mid C,F,W_3$.

---

## 5. Valuation of the actual $g_{\rm aff}$: all branches

Let


$$
D=\frac{|\widehat R|}{\gcd(|\widehat R|,|F|)},
\qquad
\widehat R=\kappa d_c\mathcal R,
$$


and fix a prime $p>N$ dividing $D$.

The retained bound $\kappa\mid2N^2$ makes $\kappa$ a $p$-adic unit. The reference transfers and their inverses are integral and invertible at $p>N$; the initial reference pair is primitive there. Since the multiplier $L$ is a power of $2$, $(\widehat h,\widehat\ell)$ is primitive over $\mathbb Z_p$.

Write


$$
a=v_p(d_c),\quad w=v_p(f_0),\quad
r=v_p(\mathcal R),\quad k=v_p(b_c).
$$


Then


$$
v_p(D)=r-w>0.
$$


The unimodular coordinate change implies


$$
\nu\in\mathbb Z_p^\times.
$$



Now evaluate


$$
g_{\rm aff}=\gcd(|F|,|CM|),
$$


without substituting a different payment.

### Branch 1: $a=0$

Here $k=0$, $v_p(F)=w$, and


$$
M=J\mathcal R+c_0f_0\nu
$$


has valuation at least $w$. Hence


$$
v_p(g_{\rm aff})=w=w+k.
$$



This includes both $p\nmid F$, where $w=0$, and $p\mid F$, where $w>0$.

### Branch 2: $a>0$

Primitivity gives $v_p(c_0)=0$. Since $r>w$, the two terms in $M$ have unequal valuations, and


$$
v_p(M)=w.
$$


Therefore


$$
v_p(g_{\rm aff})
=\min(a+w,v_p(C)+w)
=w+\min(a,v_p(C))
=w+k.
$$



This also covers $C=0$, using $v_p(C)=+\infty$.

Thus in every contributing branch,


$$
\boxed{v_p(g_{\rm aff})=v_p(b_cf_0).}
$$



Dividing the exact identity for $\Theta$ by this actual gcd gives


$$
T_{\rm aff}
=\frac{b_cf_0}{g_{\rm aff}}
\left(\frac{\mathcal R}{f_0}H+\nu\mathscr E\right).
$$


The prefactor is a $p$-adic unit, while


$$
v_p(\mathcal R/f_0)=v_p(D).
$$


Consequently


$$
\min(v_p(T_{\rm aff}),v_p(D))
=\min(v_p(\mathscr E),v_p(D)).
$$



### Referee conclusion



$$
\boxed{
\gcd(|T_{\rm aff}|,D_j)_{>N}
=
\gcd(|\mathscr E_j|,D_j)_{>N}.
}
$$



No condition on $v_p(W_{j,3})$ entered this proof.

---

## 6. Exclusion rule, zero cases, and quantitative scope

The companion projection is a unit at every $p>N$ dividing $D_j$. Indeed, the matrix


$$
\begin{pmatrix}
\tau_n&\tau_{n+1}\\
\sigma_n&\sigma_{n+1}
\end{pmatrix}
$$


has unit determinant, while $(A,B)^T$ is primitive and its first image coordinate is divisible by $p$. Its second image coordinate must be a unit.

Thus, in


$$
\mathscr E=Z^{\rm seed}+Q^{\rm fac},
$$


one has


$$
v_p(Q^{\rm fac})=a-k.
$$



- If $a>v_p(C)$, then $a-k>0$, whereas $c_0C/b_c$ is a unit. Hence $\mathscr E$ is a unit.
- Otherwise $a=k$, so $Q^{\rm fac}$ is a unit, and
  

$$
p^e\mid T_{\rm aff}
  \iff
  Z^{\rm seed}/Q^{\rm fac}\equiv-1\pmod{p^e},
  \qquad 1\le e\le v_p(D).
$$



The saturation deletion rule in A3 follows.

The old residual satisfies


$$
v_p\!\left(
\gcd\!\left(D,\left|\frac F{g_{\rm aff}}\widehat{\mathcal B}\right|\right)
\right)
=
\min\bigl(v_p(D),v_p(\mathscr E)+v_p(W_3)\bigr).
$$


Hence its excess factor is exactly attributable to $W_3$, with the divisibility claimed in A3.

### Special cases

1. **$W_3=0$:** the new equality remains valid. The old upper bound can then become completely uninformative.

2. **$\mathscr E=0$:** the new equality remains valid with
   

$$
\gcd(D,0)=D.
$$


   It does not prove nonvanishing of $\mathscr E$, $T_{\rm aff}$, or the approximation error.

3. **$Z^{\rm seed}=0$:** the exclusion rule gives no surviving large-prime resonance. This is consistent with the branch analysis; it is not an exception to it.

4. **$\widehat R=0$:** this is outside the retained nonzero-contact denominator construction. It must not be treated as an ordinary positive contact denominator.

5. **Producer nonvanishing:** the local proof assumes the actual normalized contacts exist, $F\ne0$, and the relevant $\widehat R_j\ne0$. It does not independently prove these conditions at every original index.

The smaller exact target


$$
\operatorname{lcm}_{j=0,3}\gcd(D_j,|\mathscr E_j|)_{>N}
$$


has not been shown to have logarithm $o(n\log n)$. An exact deletion factor can equal $1$ along an infinite set. The almost-$S$-unit literature is not applicable merely because these objects satisfy polynomial-coefficient recurrences; the factorial outside-$S$ height remains a genuine obstruction.

---

# Part II. A2: exact terminal geometry and compatibility of the stronger source condition

## 7. Normal vector, unit norm, and content identities

Here $p=29$, $N=n+2$, and


$$
(\mathcal R\theta)_j=W_j(j\theta_{j-1}-\theta_j),
\qquad
W_j=\binom Nj,
$$


with the original finite conditions $\theta_{-1}=\theta_b=0$.

Define


$$
t_j=\frac{(N-j)!}{(N-b)!},\qquad 0\le j\le b.
$$


Then $t_b=1$ and


$$
t_j=(N-j)t_{j+1}.
$$


The coefficient of $\theta_j$ in $t^T\mathcal R\theta$ is


$$
-t_jW_j+t_{j+1}(j+1)W_{j+1}=0.
$$


Therefore


$$
t^TZ_w=0,\qquad t^TY=W_b.
$$



The original exponent is $3\pmod{28}$, so $b\equiv27\pmod{29}$, and


$$
N-b+1=2000b+3\equiv5\pmod{29}.
$$


Thus


$$
t_{b-r}\equiv5\cdot6\cdots(4+r)\pmod{29}.
$$


The terms vanish for $r\ge25$. The displayed 25 squares sum to $269$, hence


$$
\boxed{\tau=t^Tt\equiv8\pmod{29}.}
$$



It follows that


$$
P=I-\frac{tt^T}{\tau}
$$


is an integral orthogonal projector over $\mathbb Z_{29}$, and


$$
Y=PY+\frac{W_b}{\tau}t.
$$


Because both complementary projections are integral,


$$
\boxed{
v_{29}(Y)=\min\{v_{29}(PY),v_{29}(W_b)\}.
}
$$



For $\bar Z=Z_w/C_n$,


$$
\boxed{
\Delta(\bar f)=\bar Z^T(6PY-29\bar Z).
}
$$


This identity retains, rather than deletes, the physical terminal.

### Unitriangular transformation

Let


$$
C_{jk}=\frac{(N-k)!}{(N-j)!},\qquad 0\le k\le j<b,
$$


and define $E$ as in A2. Its inverse is particularly simple:


$$
(E^{-1}v)_j=v_j-(N-j+1)v_{j-1},
$$


with $v_{-1}=0$, including the last row $j=b$. Thus $E$ is unimodular over $\mathbb Z$.

Consequently,


$$
E\mathcal R\theta=(-W_0\theta_0,\ldots,-W_{b-1}\theta_{b-1},0)^T,
$$


and the stated physical content identities follow exactly. These identities are valid at every prime at which the columns are integral; only the orthogonal projection uses the prime-$29$ unit $\tau$.

---

## 8. A sharper terminal test for the stronger congruence

Put


$$
h=6\psi-p\bar\theta,
\qquad
\bar\theta=A^{-1}(f^0/C_n),
$$


and define


$$
S_j=\sum_{k=0}^j C_{jk}^2.
$$


Since $t_k=C_{jk}t_j$,


$$
\boxed{B_j=t_jS_j.}
$$


The sequence is generated without a long unevaluated sum:


$$
S_{-1}=0,\qquad
S_j=1+(N-j+1)^2S_{j-1}.
$$


At $j=b$, this gives $S_b=\tau$. Therefore


$$
(N-b+1)^2S_{b-1}=\tau-1.
$$



Let


$$
w=v_p(W_b).
$$


Since


$$
bW_b=(N-b+1)W_{b-1},
$$


and both $b$ and $N-b+1$ are units modulo $29$,


$$
v_p(W_{b-1})=w.
$$



The last source-coordinate residual is consequently


$$
\begin{aligned}
\rho_{b-1}
&=W_{b-1}h_{b-1}+\frac{6W_b}{\tau}B_{b-1}\\
&=
W_{b-1}\left[
h_{b-1}+\frac6b\left(1-\frac1\tau\right)
\right].
\end{aligned}
$$


Modulo $29$,


$$
\frac6b\left(1-\frac1\tau\right)
\equiv1.
$$


Thus, whenever $K>w$, the proposed stronger condition requires


$$
\boxed{h_{b-1}\equiv-1\pmod{29}.}
$$


Since $\bar\theta$ is integral, it requires


$$
\boxed{\psi_{b-1}\equiv24\pmod{29}.}
$$



This is an actual compatibility test, not a definition of the desired value.

---

## 9. What the original moment-column specialization predicts

The preceding test needs only A2’s displayed finite reconstruction. A further conclusion uses the original moment-column identification of the exterior block:


$$
A_{ik}
=
\sum_s a_s(n)(n+i)_{\underline s}
\binom{2n+i-s}{k}.
\tag{M}
$$


It is important to state this identification: an interior inverse formula alone does not determine exterior columns.

For the original moment producer, (M) is checked by expanding


$$
T_m=\sum_{h\ge0}\frac{(b+h)!}{b!}\binom m{b+h}
$$


in the complete exponential source. It is the same finite/exterior moment-column rule, not an arbitrarily selected continuation.

Here $p\mid n$. With $\lambda_s=s!a_s(n)$,

- $1\le s<p$ gives $\lambda_s\equiv0\pmod p$ by Frobenius;
- $s\ge p$ gives the same conclusion because $s!$ is divisible by $p$, while the coefficient denominators are powers of $2$.

Thus


$$
A_{ik}\equiv\binom{2n+i}{k}\pmod p.
$$



The exterior factorial coefficients satisfy


$$
z_0=1,\qquad z_1=b+1,\qquad z_h\equiv0\pmod p\quad(h\ge2),
$$


because $b+2\equiv0\pmod p$.

The logarithmic source also vanishes at this precision, with a paid bound. Solving its recurrence gives


$$
L_m=m!\sum_{r=1}^m\frac{2u_{r-1}}r.
$$


The $u_r$ are $p$-integral, so


$$
v_p(L_m)\ge v_p(m!)-\lfloor\log_p m\rfloor.
$$


For each nonzero source term, multiplication by $(n+i)_{\underline s}$ and division by $b!$ gives the uniform lower bound


$$
2v_p(n!)-v_p(b!)
-\lfloor\log_p(2n+b-1)\rfloor.
$$


This is positive on the original family. Hence this modulo-$29$ calculation does not discard an unpaid logarithmic term.

Writing the finite Pascal factorization and retaining its truncation at $b-1$, the last coordinate of the response to the surviving exterior columns is


$$
\psi_{b-1}
\equiv
-\binom{-2n}{1}
-(b+1)\left(
2n\binom{-2n}{1}+\binom{-2n}{2}
\right)
\equiv0\pmod p.
$$



Accordingly, under the original specialization (M),


$$
\boxed{\psi_{b-1}\equiv0\pmod{29}.}
$$



This is incompatible with the stronger condition at any original index for which $K>w$. More directly,


$$
(PY)_b
=W_b\left(1+b\psi_{b-1}-\frac1\tau\right),
$$


whose bracket is $1-1/8\ne0\pmod{29}$. Therefore


$$
\boxed{v_{29}((PY)_b)=w.}
$$


Also


$$
\bar Z_b=bW_b\bar\theta_{b-1},
$$


so


$$
v_{29}\bigl((6PY-p\bar Z)_b\bigr)=w.
$$



### Changed assessment

The stronger vector condition


$$
6PY-p\bar Z\in p^{c+4+\nu}
$$


requires


$$
\boxed{v_p(W_b)\ge c+4+\nu.}
$$


The tangential content condition itself requires


$$
v_p(W_b)\ge c+3
$$


under this source specialization.

This does **not** yet disprove either condition on the original family: the packet does not establish an original index with the contrary comparison between $w,c,\nu$.

There is one documentary qualification. If A2’s omitted definition of $A_{IE}$ is not accepted as the moment continuation (M), the terminal-residue computation is conditional precisely on that identification. The normal-vector, projection, content, and last-coordinate compatibility identities above are independent of this qualification.

---

## 10. A more economical all-depth lemma

The vector congruence is stronger than the scalar alignment actually needed.

Define


$$
\delta_j=
\frac{\bar Z_j-(N-j)\bar Z_{j+1}}{p^{c+2}},
\qquad 0\le j<b.
$$


These are integral. Moreover, they are not all divisible by $p$. Indeed,


$$
E^{-T}\bar Z
=
\bigl(p^{c+2}\delta_0,\ldots,p^{c+2}\delta_{b-1},\bar Z_b\bigr)^T,
$$


and orthogonality to $t$ gives


$$
\sum_{j<b}p^{c+2}\delta_jB_j+\tau\bar Z_b=0.
$$


If all $\delta_j$ were divisible by $p$, then so would every coordinate of $\bar Z/p^{c+2}$, contradicting primitivity.

With


$$
\rho_j=W_jh_j+\frac{6W_b}{\tau}B_j,
$$


one obtains the exact identity


$$
\boxed{
\Delta(\bar f)=-p^{c+2}\sum_{j<b}\delta_j\rho_j.
}
$$


Therefore the target is exactly


$$
\sum_{j<b}\delta_j\rho_j\equiv0\pmod{p^{c+4+\nu}}.
$$



This identity does not evaluate that sum. It does, however, expose two genuine savings for a follow-on proof.

1. A coordinatewise sufficient condition only needs
   

$$
\rho_j\in p^{\max(0,K-v_p(\delta_j))},
   \qquad K=c+4+\nu,
$$


   rather than modulus $p^K$ uniformly.

2. Since $B_j=t_jS_j$, the boundary correction is automatically zero modulo $p^K$ whenever
   

$$
v_p(W_b)+v_p(t_j)\ge K.
$$


   In particular, it is confined to a terminal strip of length at most
   

$$
p\max(K-v_p(W_b),0),
$$


   using the elementary factorial valuation of a product of consecutive integers.

The materially sharpened next obligation is thus a **weighted scalar source identity with a finite terminal strip**, not an untested uniform vector congruence. It must still be proved from the complete first and second sources and the whole original digit word.

---

## 11. High-denominator Cartier closure

A2’s transition formula is correct for


$$
P_h\in\mathbb Z[t,z^{\pm1}],\qquad
\deg_tP_h\le h,\quad \operatorname{supp}_zP_h\subset[-h,h].
$$


The polynomial-in-$t$ hypothesis matters.

For $m=\lceil h/p\rceil$,


$$
Q^{-h}
=
Q^{pm-h}\bigl(Q(t^p,z^p)+pV_Q\bigr)^{-m}.
$$


Integral binomial expansion and Cartier extraction yield exactly A2’s formula. The numerator bounds become $p(m+k)$ before Cartier and $m+k$ afterward, while the coefficient retains at least $p^{m+k-1}$. Thus closure holds at every fixed precision.

The initialization and factorial cutoff are also valid:

- excess $z$-support contracts by at least a factor $p$ per step;
- $i<\min(b,pa)$ is a sufficient surviving-source cutoff at precision $p^a$;
- $J_0(n)^{-1}$ is paid only because the original-family unit theorem is retained;
- acceptance requires the **whole actual word** of $n$, not merely a low prefix.

One terminology correction is appropriate. The number


$$
\sum_{h=1}^r(h+1)(2h+1)
$$


counts representation slots; it is not necessarily the intrinsic dimension of an independent module basis. For example,


$$
p\,P/Q=p\,(PQ)/Q^2
$$


can give redundant representations inside the allowed support. This does not affect closure or evaluation.

The weak first-source tail lemma already accepted in Turn 7 is sufficient and remains closed.

---

# Part III. A5: force arithmetic, actual content, and integral certificates

## 12. Central and adjacent identities

For $n=2h$,


$$
T_j=\frac{2^j(h_{\underline j})^2}{(2j)!}
$$


gives


$$
A_h=\sum_{j=0}^hT_j,\qquad
B_h=\sum_{j=0}^{h-1}\frac{h-j}{2j+1}T_j.
$$


The multinomial derivation in A5 is correct, and


$$
v_2(T_j)=v_2(j!)+2v_2\binom hj.
$$


Thus all terms are $2$-adically integral; the factorial denominators are paid exactly.

The original word gives $h\equiv1\pmod{32}$. The claimed residues


$$
A_h\equiv2,\qquad B_h\equiv1\pmod8
$$


follow from the stated valuation argument.

---

## 13. New result: the force recurrence is integrally divided in advance

A5 writes


$$
\begin{aligned}
2F_{i+2}={}&(4n+4i+6)F_{i+1}\\
&-(3i+n+2)(n+i+1)F_i\\
&+i(n+i)(n+i+1)F_{i-1}.
\end{aligned}
$$


The residue derivation is correct. But every coefficient on the right is even.

More explicitly,


$$
\frac{(3i+n+2)(n+i+1)}2
=
\binom{n+i+2}{2}+i(n+i+1),
$$


and


$$
\frac{i(n+i)(n+i+1)}2
=i\binom{n+i+1}{2}.
$$


Therefore


$$
\boxed{
\begin{aligned}
F_{i+2}={}&(2n+2i+3)F_{i+1}\\
&-\left[\binom{n+i+2}{2}+i(n+i+1)\right]F_i\\
&+i\binom{n+i+1}{2}F_{i-1}.
\end{aligned}
}
\tag{13.1}
$$



This is an integer-coefficient recurrence. Once its coefficients are evaluated as integers, modular propagation loses **no force precision**.

Accordingly, A5’s prescription $P=L+I$ is safe but unnecessarily expensive. Seed precision $2^L$ suffices for propagation to any fixed prefix modulo $2^L$. Exact even divisions remain in the short-factorial seed calculation and in evaluating binomial coefficients, but there is no accumulated one-bit loss per recurrence step.

---

## 14. New infinite-family theorem: the complete force modulo $4$

In fact, $h\equiv1\pmod4$ is enough.

For $j=2,3$, $\binom hj$ is even. For $j\ge4$, $v_2(j!)\ge3$. Hence


$$
A_h\equiv1+h^2\equiv2\pmod4.
$$


In the adjacent sum, the $j=1$ term is


$$
(h-1)h^2/3\equiv0\pmod4,
$$


and all later terms vanish modulo $4$. Thus


$$
B_h\equiv1\pmod4.
$$



Since $n\equiv2\pmod8$,


$$
F_0\equiv2,\qquad
F_1=(n+1)(A_h+B_h)\equiv1\pmod4.
$$


Using the integral recurrence:



$$
F_2\equiv7F_1-6F_0\equiv3\pmod4,
$$




$$
F_3\equiv9F_2-14F_1+6F_0\equiv1\pmod4,
$$




$$
F_4\equiv11F_3-25F_2+20F_1\equiv0\pmod4,
$$




$$
F_5\equiv13F_4-39F_3+45F_2\equiv0\pmod4,
$$




$$
F_6\equiv15F_5-56F_4+84F_3\equiv0\pmod4.
$$


Three consecutive zeros now propagate by (13.1).

### Theorem
On every original A5 index,


$$
\boxed{
F_i\equiv
\begin{cases}
2,&i=0,\\
1,&i=1,\\
3,&i=2,\\
1,&i=3,\\
0,&i\ge4
\end{cases}
\pmod4.
}
$$



This proves the complete modulo-$4$ source profile seen in the parent receipts. It is not a finite-computation extrapolation.

---

## 15. Content bounds and the Lucas-mask criterion

The finite modulo-$2$ factorization and its inverse give


$$
z^f_j\equiv q_j\binom{h+r_j}{r_j}\pmod2,
\qquad
r_j=\left\lfloor\frac{b-1-j}{4}\right\rfloor,
$$


where $q_j=0$ for $j\equiv0\pmod4$ and $q_j=1$ otherwise.

The finite upper bound $b-1$ is essential to the hockey-stick sum. The endpoint residues


$$
z^f_{b-4}=z^f_{b-3}=z^f_{b-2}=1,\qquad z^f_{b-1}=0\pmod2
$$


follow.

Because $N=n+2\equiv4\pmod{64}$, odd $W_j$ occur only at $j\equiv0\pmod4$. At such rows the reconstructed difference is even; at the other rows $W_j$ is even. Thus


$$
x=\tfrac12\mathcal Rz^f\in\mathbb Z_2^{b+1}.
$$


The two odd endpoint differences give


$$
0\le a\le
\min\left\{
v_2\binom{n+2}{b-4},
v_2\binom{n+2}{b-3}
\right\}-1,
$$


and therefore the stated logarithmic upper bound.

The extra modulo-$4$ argument for even-weight rows is correct. In particular, a row with $v_2(W_j)=1$ cannot produce an odd coordinate of $x$. Hence


$$
\boxed{
a=0
\iff
\exists\,j<b:
\binom{n+2}{j}\text{ odd and }z^f_j\equiv2\pmod4.
}
$$



The physical terminal does not create an omitted witness.

### Scope of the parent receipts

The supplied selected-row receipt records, at $u=0,\ldots,4$,


$$
z^f_0=z^f_4=0\pmod4,
$$


and the displayed four near-terminal residues. It reports no $a=0$ witness.

That does **not** prove $a>0$, even at those five indices: the full Lucas mask was not exhausted. It also gives no infinite-family content conclusion.

The force-certificate excerpt is a finite receipt for the stated original $u=0$ calculation and auxiliary algorithm checks. Its hash and metadata do not extend its mathematical scope. No closed calculation needs to be repeated.

---

## 16. Integral torsion and stronger acceptance certificates

At terminal acceptance, the projected operators satisfy


$$
\operatorname{im}\overline{\mathscr D}_X=\operatorname{im}D_X,\qquad
\operatorname{im}\overline{\mathscr D}_Y=\operatorname{im}D_Y.
$$


The exact Laurent divisions by $1+X$ and $1+Y^{-1}$ are valid, including negative exponents.

Since $D_X$ and $D_Y$ act diagonally on $X^kY^l$,


$$
\boxed{
\mathscr A_L/
(\operatorname{im}\overline{\mathscr D}_X+
 \operatorname{im}\overline{\mathscr D}_Y)
\cong
\bigoplus_{k,l}\mathbb Z/\gcd(2^L,k,l)\mathbb Z.
}
$$


The constant summand is acceptance. The nonconstant summands are genuine torsion invisible to acceptance.

For example, $X^2$ has zero acceptance and nonzero class of order $2$:


$$
\overline{\mathscr D}_X(X-1)=2X^2.
$$



### Consequence for certificate design

A derivative-image certificate is unnecessarily restrictive. A complete terminal acceptance certificate may instead have the form


$$
P_r^{\rm fin}(0,X,Y)
=
\overline{\mathscr D}_XH_X+
\overline{\mathscr D}_YH_Y+
T,
$$


where $T$ is an explicitly listed **nonconstant** torsion remainder, with its coefficient reductions and exact Bézout payments recorded.

If the constant coefficient is zero, such a certificate always exists by A5’s coefficientwise reduction. The torsion remainder need not vanish.

This repairs the certificate class, not the missing arithmetic value. One still needs:

- an independently specified $r(u)$;
- the actual completed terminal polynomial;
- proof that its constant coefficient vanishes at the paid primitive precision on an infinite original subfamily.

For


$$
c=\max(2a+2,a+3),
$$


the numerator must remain


$$
N_r=
2^{c-a-3}\mathcal V
-r(u)\,2^{c-2a-2}\mathcal U,
\qquad
E-r(u)Q=2^{-c}N_r.
$$


The actual $a$, not its upper bound, belongs in this definition.

---

# Part IV. A1: adjacent-window sectors

## 17. Original congruences and determinant payments

The original progression gives


$$
j\equiv81\pmod{729}.
$$


Since


$$
v_3(4^{729}-1)=7,
$$


one has $4^j\equiv4^{81}\pmod{3^7}$.

In the expansion of $(1+3)^{81}$, division by $243$ gives initial nonconstant terms


$$
1,\quad120,\quad9480,
$$


whose sum is $7\pmod9$. For $4\le k<81$,


$$
v_3\binom{81}{k}=4-v_3(k),
$$


so the remaining terms vanish modulo $9$ after the division. Thus


$$
\frac{4^j-1}{243}\equiv7\pmod9.
$$


For sufficiently large $h$,


$$
2s=\frac D{243}\equiv-7\equiv2\pmod9,
$$


and


$$
\boxed{s\equiv1\pmod9.}
$$


Also


$$
c'=\frac{3^{h-31}-1}{2}\equiv4\pmod9
$$


when $h\ge33$.

The real-window infinitude argument is valid: irrational rotation along the original arithmetic progression visits every strict interior window infinitely often. It supplies no extra favorable ternary digits.

For the square sectors, the determinant product is valid once the strict interior margin ensures all factorial arguments are nonnegative. With $L+B=2s$, the $q=3^k$ layer is a periodic floor difference whose full-period sum is zero. Its nonzero intervals occur with the positive interval before the negative interval, and with equal total lengths. Therefore every initial partial sum is nonnegative.

At $q=9$, the original residues give



$$
(s,L,B)\equiv(1,4,7)
\quad\text{or}\quad
(1,3,8).
$$


The remaining initial segment has length one and contributes $1$. Hence both square determinants are divisible by $3$.

All denominator factorial valuations are included in this argument.

---

## 18. Nullity: correct lower bound and sharper exact reduction

The sector involution is


$$
a\longmapsto121-a\pmod{243}.
$$


It has:

- $61$ equal paired couples with parameter $T=c'$;
- $59$ equal paired couples and one fixed sector with $T=c'-1$;
- the unequal pair $\{122,242\}$, of lengths $s$ and $s-1$.

Thus A1’s lower bound


$$
\boxed{\dim\ker K\ge242}
$$


is correct.

A useful refinement is available. Set


$$
\alpha=\dim\ker B_s(c'),\qquad
\beta=\dim\ker B_s(c'-1),
$$


and let


$$
\eta=
\operatorname{rank}\left(
\ker B_s(c'-1)\longrightarrow\mathbb F_3,\;
x\longmapsto x_{s-1}
\right)\in\{0,1\}.
$$


The unequal block is $B_s(c'-1)$ with its last column deleted. Its kernel has dimension $\beta-\eta$, so its full symmetric paired block has nullity


$$
1+2(\beta-\eta).
$$


Therefore


$$
\boxed{
\dim\ker K
=
122\alpha+121\beta+1-2\eta.
}
\tag{18.1}
$$



This reduces the entire sector-rank question to two square kernels and one exact boundary-coordinate restriction. Since $\alpha,\beta\ge1$, it recovers the lower bound $242$.

Equation (18.1) is not an evaluated exact rank until $\alpha,\beta,\eta$ are determined on the original words. Also, $\eta$ concerns the last polynomial coefficient; it is **not** the actual endpoint functional $X(-1)$. The latter must be tracked separately.

The actual operator identification remains conditional. Neither this formula nor the determinant divisibility repairs the previously identified ternary transport gap.

---

# Part V. Preservation of the actual arithmetic and error

## 19. No local reduction changes the producers

The following data remain unchanged.

### A3

The complete force is


$$
w_i=
\sum_{j=0}^{\min(2n,n+i)}
q_j(n+i)^{\underline j}\mathcal W_{2n+i-j},
\qquad 0\le i\le2,
$$


with both the exponential and logarithmic terms in $\mathcal W$, and maximum force index $2n+2$.

The physical returns remain


$$
N_0=\det T+R_0\widehat w,\qquad N_3=R_3\widehat w.
$$


For


$$
x=T^{-1}(n!t),\qquad y=T^{-1}\widehat w,
$$


the complete corrected columns remain


$$
u=(-sx_0,sx_0-sx_1,sx_1-sx_2,sx_2),
$$




$$
v=(1-sy_0,sy_0-sy_1,sy_1-sy_2,sy_2).
$$


In particular, the exterior $+1$ is retained.

The least simultaneous clearer is the actual $D_8$, followed by the actual all-prime row contents $g_j^{(8)}$. For the weighted endpoint combination, retain


$$
q_\lambda=
\frac{k_{\rm wt}h_{\rm end}|A_{\rm wt}B_{\rm wt}|}
{F_{\rm gcd}G_{\rm wt}H_{\rm gcd}},
$$


with exactly the three all-prime gcd payments stated in A3. Neither $D_j$ nor $\mathscr E_j$ replaces this denominator.

The whole error remains


$$
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda e_3\alpha_{n,2}(\lambda-\Lambda_{n,2}).
$$



### A2

The finite contact range remains $0\le j<b$, source recurrence rows $1\le i\le b-2$, and reconstructed rows $0\le j\le b$. The complete second source retains both initial charges, all recurrence forcing, factorial subtraction, logarithmic contribution, and both finite returns.

The columns are still


$$
Z_w=Lf^0,\qquad Y=L\mathbf r+W_be_b.
$$


Neither division by $C_n$ nor division by $\tau$ is an all-prime normalization.

With the actual integer columns, actual contents, and least simultaneous clearer $d_B$,


$$
A_B=N_{B,1}^T\Omega N_{B,1},\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\quad p_n=H_B/g_B.
$$


The gcd is over all primes. The whole signed error remains


$$
q_n(e+\pi)-p_n=-q_n\epsilon_n.
$$



### A5

The corrected columns remain


$$
x=\frac12\mathcal RA^{-1}\mathfrak f,\qquad
y=\frac{\mathcal RA^{-1}(h^e+h^F)+e_0}{4b!}.
$$


The raw forms retain their physical terminal terms:


$$
b^2W_b^2(z^f_{b-1})^2
$$


in $\mathcal U$, and


$$
W_b^2\,bz^f_{b-1}(bz^k_{b-1}+1)
$$


in $\mathcal V$.

The complete finite completion, both differential boundaries, and the logarithmic guard remain in force. No shallow congruence permits deleting these terms after arbitrary primitive division.

The actual least simultaneous clearer $d_B$ remains attached to


$$
u_j=\frac{2\Lambda R\,x_j}{\omega_j},\qquad
v_j=\frac{4b!\,y_j}{\omega_j}.
$$


No reconstructed row content is newly divided out. Retain


$$
A_B=d_B^2\,4\Lambda^2R^2(x^Tx),
\qquad
H_B=d_B^2\,8\Lambda Rb!(x^Ty),
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\quad p_n=H_B/g_B.
$$


Again,


$$
q_n(e+\pi)-p_n=-q_n\epsilon_n
$$


is the whole error.

### A1

The complete functional, its finite cutoff, and physical terminal $Y_m$ remain unchanged. The actual return closure and complete bordered diagonal must be retained in any next Schur calculation.

With the prescribed actual contents and least clearer,


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$




$$
g_\ell=\gcd(|A_\ell|,|B_\ell|),
\qquad
q=|B_\ell|/g_\ell,
$$


and


$$
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
{g_\ell}\det H_{\rm complete}.
$$


The candidate radical does not evaluate the actual relative cofactor valuation or pay a future inverse of a further Schur block.

---

## 20. Bounded calculations worth authoring

No computation was executed for this report. No closed producer or parent receipt should be rerun merely for confirmation.

### 20.1 A3: one new seeded gcd audit

**Input:** $n=225$, with the exact actual $3\times3$ producer, its two contacts, the short response recurrence, and the companion recurrence.

**Output:** the actual $h_j,\kappa_j,d_{c,j},b_{c,j}$, the exact residual identities, and


$$
\gcd(T_{\rm aff},D_j)_{>227}
=
\gcd(\mathscr E_j,D_j)_{>227}.
$$


Also record which valuation branches occur and which do not.

Ordinary gcds followed by removal of primes at most $227$ suffice. No unrestricted large-integer factorization is required. This checks one original index only.

### 20.2 A2: terminal compatibility specialization

**Bounded inputs:** arithmetic modulo $29$, with


$$
n\equiv0,\quad b\equiv27,\quad \tau\equiv8,
$$


the two surviving exterior coefficients $1,b+1$, and binomial degrees $1,2$.

**Expected outputs:**


$$
\psi_{b-1}\equiv0,\qquad
\frac6b(1-\tau^{-1})\equiv1,
$$


and therefore the nonzero last residual coefficient.

The coordinator should explicitly certify that the retained A2 exterior block is (M). This small calculation does not compare the actual $w,c,\nu$, and does not establish an infinite alignment law.

### 20.3 A5: new Lucas-mask rows, not the two already checked

At $u=0$, select, for example, the first $32$ previously untested integers $j<b$ satisfying the exact submask condition


$$
j\ \&\ \neg(n+2)=0.
$$


Use the retained selected-row finite solve modulo $4$, with its full return correction. The now-proved complete source modulo $4$ is $(2,1,3,1,0,\ldots)$.

**Expected output:** exact $z^f_j\bmod4$, the odd-weight certificate for each row, and either:

- a residue $2$, proving $a=0$ at that one original index; or
- an explicit statement that this bounded list found no witness.

The second outcome would not prove $a>0$.

---

## 21. Decision ledger

| Claim | Referee decision |
|---|---|
| A3 seeded companion and factorial identity | Proved from the actual seed |
| A3 planar payment and actual $g_{\rm aff}$ valuation | Correct in every contributing branch |
| A3 large-prime gcd equality | Correct under retained nonzero-contact hypotheses |
| A3 seed-sensitive exclusion | Correct, including zero conventions |
| Subfactorial seeded-contact gcd estimate | Open |
| A2 weak normalized tail | Closed result reused |
| A2 normal vector, unit norm, projector | Correct |
| A2 unitriangular content identities | Correct |
| A2 stronger source congruence | Sufficient, not established |
| A2 terminal residue $\psi_{b-1}\equiv0$ | Proved under the explicit original moment-column identification (M) |
| Necessity $v_{29}(W_b)\ge c+4+\nu$ for the stronger vector law | Proved under that specialization |
| Original violating index for that necessity | Not certified |
| A2 arbitrary-precision Cartier closure | Correct at stated support and whole-word scope |
| A5 central/adjacent identities and parity | Correct |
| A5 integer-coefficient recurrence | New proved improvement; no accumulated recurrence precision loss |
| Entire A5 force modulo $4$ | New infinite-original-family theorem |
| A5 content bounds and $a=0$ criterion | Correct; criterion not globally evaluated |
| Parent force and selected-row receipts | Finite scope only |
| A5 integral torsion quotient | Correct |
| Torsion-aware acceptance certificates | Available; actual accepting constant still open |
| A1 original $s,c'$ congruences and nonnegative floor layers | Correct |
| A1 nullity at least $242$ | Correct for the candidate matrix |
| Exact reduction (18.1) | New proved structural refinement |
| Actual ternary operator transport | Still conditional |
| Same-index all-prime denominator versus whole nonzero error | Open |

---

## 22. Conclusion

The strongest new unconditional arithmetic statement proved in this review is the complete binary force law


$$
\boxed{
\mathfrak f\equiv(2,1,3,1,0,0,\ldots)\pmod4
}
$$


on every original A5 index, together with its integer-coefficient, precision-preserving recurrence.

The A3 contact equality is confirmed with all actual primitive payments. The A2 terminal calculation exposes a sharper necessary condition for its proposed strong source law, subject to the explicitly identified exterior specialization. The A1 candidate obstruction is confirmed and reduced to two square-sector kernels plus a boundary restriction.

The remaining mathematical bottlenecks are precise:

1. bound the aggregate depth of A3’s surviving seeded factorial congruences on an infinite original subsequence;
2. prove the actual A2 weighted scalar source alignment, after checking the terminal compatibility and retaining the complete sources;
3. evaluate A5’s actual primitive acceptance constant for an independently specified relative law;
4. repair actual ternary transport, then evaluate the original sector radicals, endpoint restrictions, and paid next Schur digit;
5. combine the resulting arithmetic with the **actual all-prime primitive denominator** and the **nonzero whole error at the same infinite original indices**.

For any one producer, an irrationality proof would follow from


$$
0<|q_n(e+\pi)-p_n|\longrightarrow0
$$


on such a sequence. None of the present results establishes that condition.



$$
\boxed{\text{The rationality or irrationality of }e+\pi\text{ remains unresolved.}}
$$


