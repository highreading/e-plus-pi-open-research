> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4, Turn 19 — Independent audit of the diagonal-force reduction and binary adjoint contraction

## Executive conclusion

The attached work does **not** prove or disprove the irrationality of


$$
S=e+\pi.
$$



The principal algebraic reductions in A3turn7 and A5turn16 withstand audit, with the qualifications and precision corrections below.

1. **A3’s complete diagonal recurrence and logarithmic contact normalization are correct.** The logarithmic companion is classical: it is the Legendre second-kind polynomial companion in DLMF 14.7.4, after the stated imaginary change of variable. What requires—and receives—a separate normalization argument is its identification with the **complete original contact force**, including all three contact coordinates.

2. **A3’s exponential Wronskian, factorial real bound, selected-prime pole, and displacement nonvanishing are correct.** None implies nonvanishing of the whole evaluated $e+\pi$ form, or a favorable primitive denominator for its rational center.

3. **The sharper logarithmic strip and denominator comparison remain selected-prime results.** Their use requires the accepted local inverse and endpoint-unit hypotheses. They do not control the unselected endpoint factor or the final all-prime gcd.

4. **The continued-fraction implication is valid as a conditional lattice argument.** No theorem establishing its moving-residue gap hypothesis is supplied. The cited rational-reconstruction algorithmic literature does not fill that gap.

5. **A5’s finite band-plus-boundary factorization, inverse-transpose orientations, endpoint adjoint vector, and one-variable contraction are correct at their stated normalized precision.** The source-term guards must remain explicit. The bounded band does not compress the actual length-$b$ adjoint polynomial.

6. **The newly attached central evaluator repairs the missing-import problem.** Its factorial-tail truncation is mathematically justified. The full coordinate certificate now supports inspection of the auxiliary Gram sums and contents, rather than only their summaries. This is still supplied finite evidence: no execution or hash regeneration is claimed here.

7. **There is a precision qualification to the first-column replacement rule.** For a replacement error of coordinate depth $T$, the universally valid norm-error bound is
   

$$
\min(T+a+1,2T),
$$


   not always $T+a+1$. Moreover, a one-sided adjoint contraction using the exact force has a different, generally weaker, error budget. These distinctions matter when using truncation to obtain relative outputs.

The immediate outstanding problems are concrete: either prove a compressed, unit-sensitive law for the **actual binary adjoint moments**, or establish growth of the **actual $d=2$ coprime endpoint factor** after its exact normalization. Neither follows from unit contact solves, small initial forces, or classical Legendre reference estimates.

No tools were used. All proposed calculations below are bounded mathematical checks for personal inspection, not proposed code execution.

---

## 1. Domains, boundaries, and proof-status conventions

The two constructions must remain separate.

### A3: original $d=2$ endpoint producer

The infinite families are


$$
n=15^r,\quad r\ge2,\qquad \mathcal P=\{3,5\},
$$


or


$$
n=105^r,\quad r\ge2,\qquad \mathcal P=\{3,5,7\}.
$$


Here


$$
d=2,\qquad b=3,
$$


with contact coordinates $0,1,2$ and reconstructed coordinates $0,1,2,3$. The complete force of each producer uses its original terminal index $2n+2$.

The finite inputs $15,30,105,210$ are consistency tests, not an infinite-family theorem.

### A5: original binary family

The domain is exactly


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
$$


Contact coordinates are $0\le i,j<b$; reconstructed coordinates are $0\le j\le b$.

In the block notation


$$
b=128D+81,
$$


the last contact block contains only residues $0,\ldots,80$. The coordinate $j=b$ is a separate reconstructed endpoint.

The systems $b=81,209$ are auxiliary systems satisfying the relevant continuation congruences. Neither is an original exponential-family index.

### Status of dependencies

The previously accepted recurrence, local inverse, normalization bridge, symbol filtration, complete force budgets, and signed-error theorems are reused only at their recorded scopes. Algebraic identities derived below are rigorous consequences of those inputs. Supplied arithmetic receipts remain finite evidence unless their individual arithmetic is explicitly checked in the text.

The accepted monic Legendre reference bounds, second-kind Wronskian, and all-degree $b=0$ obstruction are background results, not new results of this report.

---

# Part I. A3turn7

## 2. Complete diagonal recurrence: audit and derivation

Write


$$
Q(z)=1-z+\frac{z^2}{2},\qquad f_n=(n!)^2,
$$


and


$$
\mathcal B_N^{[m]}=N![z^N]e^zQ(z)^m.
$$


For


$$
A_n=Q^n\mathscr H^{(n)},
$$


the exact contiguity relation is


$$
A_{n+1}=QA_n'-nQ'A_n.
$$



Let


$$
D_n=w_0(n)=n![z^n]A_n.
$$


Coefficient extraction at the original contact coordinates gives


$$
D_{n+1}
=w_2(n)-w_1(n)-\frac{n(n+1)}2D_n.
$$


Using the complete terminal relation


$$
w_2-(2n+3)w_1+\frac{(n+1)(n+2)}2w_0=E_n,
\qquad
E_n=\mathcal B_{n+1}^{[n+1]},
$$


one obtains


$$
D_{n+1}=2(n+1)w_1(n)-(n+1)^2D_n+E_n.
\tag{2.1}
$$



The next terminal coefficient, with


$$
G_n=\mathcal B_{n+2}^{[n+1]},
$$


gives


$$
w_1(n+1)
=(n+1)(3n+5)w_1(n)
-(n+1)^2(n+2)D_n
+(2n+3)E_n+G_n.
\tag{2.2}
$$


Substitution of (2.2) into the next instance of (2.1) yields


$$
\boxed{
D_{n+2}
=(n+2)(2n+3)D_{n+1}
+(n+2)(n+1)^3D_n+\Psi_n,
}
$$


where


$$
\boxed{
\Psi_n=(n+1)(n+2)E_n+2(n+2)G_n+E_{n+1}.
}
$$



All three forcing terms are necessary. In particular, $E_{n+1}$ must not be dropped.

For


$$
b_n^\bullet=\frac{D_n^\bullet}{(n!)^2},
\qquad
\psi_n=\frac{\Psi_n}{(n+2)((n+1)!)^2},
$$


the normalized exponential recurrence is


$$
\boxed{
(n+2)b_{n+2}^{\exp}
=(2n+3)b_{n+1}^{\exp}+(n+1)b_n^{\exp}+\psi_n.
}
\tag{2.3}
$$



For the logarithmic component, the polynomial force has already ended at the coefficient positions used here. Consequently its diagonal recurrence is homogeneous. This is a degree-based vanishing statement, not deletion of the logarithmic force.

**Verdict:** A3’s recurrence and normalization are correct. Adjacent producers are used only to establish contiguity; no finite contact inverse is extended beyond its boundary.

---

## 3. Classical Legendre companion and complete contact normalization

Let


$$
\tau_0=\tau_1=1,\qquad
\rho_0=0,\quad\rho_1=1,
$$


with both sequences satisfying


$$
(n+2)y_{n+2}=(2n+3)y_{n+1}+(n+1)y_n.
$$



The classical identifications are


$$
\tau_n=i^nP_n(-i),\qquad
\rho_n=i^{n-1}W_{n-1}(-i)\quad(n\ge1),
$$


where $W_{n-1}$ is the polynomial companion occurring in DLMF 14.7.4. Thus the companion sequence itself is classical overlap.

### 3.1 The normalization obligation

For the logarithmic function,


$$
f(0)=0,\qquad f'(z)=2/Q(z),
$$


one has


$$
\frac{f(z)}{1-z}=2z+3z^2+\cdots.
$$


Therefore


$$
b_0^{\log}=0,\qquad b_1^{\log}=4.
$$


The homogeneous diagonal recurrence then gives


$$
b_n^{\log}=4\rho_n.
$$



Applying (2.1) with zero logarithmic terminal right side gives


$$
w_1^{\log}
=2f_n(n+1)(\rho_n+\rho_{n+1}).
$$


The original terminal relation gives the remaining coordinate. Hence


$$
\boxed{
w^{\log}
=4f_n
\begin{pmatrix}
\rho_n\\[1mm]
\dfrac{n+1}{2}(\rho_n+\rho_{n+1})\\[2mm]
\dfrac{(n+1)(n+2)}2\rho_{n+2}
\end{pmatrix}.
}
\tag{3.1}
$$



This proves the complete original contact-force identification, including its factor $4(n!)^2$.

### 3.2 Convolution and Wronskian

The generating functions give


$$
R(t)=T(t)\int_0^tT(s)\,ds,\qquad
T(t)=(1-2t-t^2)^{-1/2},
$$


so


$$
\rho_n=\sum_{j=0}^{n-1}\frac{\tau_j\tau_{n-1-j}}{j+1}.
\tag{3.2}
$$


This is consistent with the classical second-kind convolution.

For odd $p$,


$$
v_p(\rho_n)\ge-\lfloor\log_p n\rfloor.
$$


The discrete Wronskian satisfies


$$
\tau_n\rho_{n+1}-\tau_{n+1}\rho_n
=\frac{(-1)^n}{n+1}.
\tag{3.3}
$$


Indeed, its initial value is $1$, and the recurrence multiplies consecutive Wronskians by $-n/(n+1)$.

With


$$
P_n=(0,1,2n+3)^T,
$$


equations (3.1)–(3.3) give


$$
\boxed{
w^{\log}
=\frac{4\rho_n}{\tau_n}z
+\frac{2(-1)^nf_n}{\tau_n}P_n.
}
\tag{3.4}
$$



**Verdict:** the complete contact normalization is proved; the underlying companion and Wronskian are not claimed as new classical results.

---

## 4. Sharper strip and denominator-stability scope

Assume


$$
p>2,\qquad p\mid n,\qquad \tau_n\in\mathbb Z_{(p)}^\times,
$$


and retain the accepted local inverse and endpoint-unit hypotheses.

Set


$$
N_p=v_p(n!),\qquad
K_p^*=2N_p-\lfloor\log_p n\rfloor.
$$


The first term of (3.4) has depth at least $K_p^*$, and its transverse term has depth exactly $2N_p$. Thus


$$
\boxed{
w^{\log}\in p^{K_p^*}\mathbb Z_{(p)}^3.
}
$$



The passage to


$$
\Theta-\Theta^{\exp}\in p^{K_p^*}\mathbb Z_{(p)}
$$


uses the accepted local endpoint normalization; it does not follow from a force valuation without that normalization.

For reduced $a/k$, the local denominator comparison is valid:

- if $p\mid k$, the unit hypotheses give the same exponent $2N_p+v_p(k)$;
- if $p\nmid k$, the two reconstruction errors agree modulo $p^{K_p^*}$, and truncation of their valuations at $2N_p$ changes the denominator exponent by at most $\lfloor\log_p n\rfloor$.

Therefore


$$
\boxed{
|v_p(q_\lambda)-v_p(q_\lambda^{\exp})|
\le\lfloor\log_p n\rfloor.
}
$$



This proves the selected-prime budget


$$
B_{\mathcal P}^*(n)
=\prod_{p\in\mathcal P}p^{\lfloor\log_p n\rfloor}
\le n^{|\mathcal P|}.
$$



It proves nothing by itself about unselected primes, the least full clearer, or the complete primitive denominator.

The older receipt’s `log_force_strip_depth` entries must be read as the older **certified budgets**, not exact measured minima. Some are smaller than the new bound. If those fields were intended as exact valuations, they would conflict with the sharper theorem and would require clarification.

---

## 5. Exponential Wronskian, real tail, and arithmetic nonvanishing

Define


$$
W_n^{\exp}
=\tau_nb_{n+1}^{\exp}-\tau_{n+1}b_n^{\exp},
\qquad
\omega_n=(-1)^n(n+1)W_n^{\exp}.
$$


Subtracting the homogeneous and forced recurrences gives


$$
\boxed{
\omega_{n+1}
=\omega_n+(-1)^{n+1}\tau_{n+1}\psi_n,
\qquad \omega_0=2.
}
\tag{5.1}
$$



The actual transverse contact displacement is


$$
\boxed{
\delta_n^{\exp}
=\frac{(-1)^nf_n\omega_n}{2\tau_n}
-\frac{E_n}{2(n+1)}.
}
\tag{5.2}
$$


Consequently


$$
\boxed{
w^{\exp}
=\frac{b_n^{\exp}}{\tau_n}z
+\delta_n^{\exp}P_n+E_ne_2.
}
\tag{5.3}
$$



### 5.1 Real bound

The exact exponential remainder gives


$$
A_n^{\exp}(z)
=e\mathcal Z_n(z)
-eQ(z)^n\int_0^1e^{-u}u^ne^{uz}\,du.
$$


Using the coefficient majorant


$$
|N![z^N]e^{uz}Q^n|\le N!e(5/2)^n
$$


yields A3’s contact-error estimate. Together with


$$
\tau_n\le(1+\sqrt2)^n,\qquad z_1/z_0\le2(n+1),
$$


equation (5.2) gives


$$
|\omega_n|
\le
(6e^2+\tfrac52e)
\frac{((5/2)(1+\sqrt2))^n}{n!}
\le\frac{64\,7^n}{n!}.
\tag{5.4}
$$


Thus the stated constant is safe.

The explicit coefficient bounds on $\Psi_n$ imply absolute convergence of the series generated by (5.1). Since $\omega_n\to0$,


$$
\omega_n
=-\sum_{j=n}^{\infty}(-1)^{j+1}\tau_{j+1}\psi_j.
$$


This is a real factorial-tail identity, not a selected-prime convergent factorial series.

### 5.2 Direct verification of the selected-prime congruences

A useful explicit justification of the finite-sum congruences is as follows. Write


$$
Q^n=\sum_h q_hz^h,\qquad
F(m)=m!\sum_{j=0}^m\frac1{j!}.
$$


Then


$$
w_i^{\exp}
=\sum_{h=0}^{n+i}
q_h(n+i)^{\underline h}F(2n+i-h).
\tag{5.5}
$$


For odd $p\mid n$:

- when $i=0$, every term with $h\ge1$ contains $n$, so
  

$$
w_0^{\exp}\equiv F(2n)\equiv1\pmod p;
$$


- when $i=1$, the $h=1$ term contains $q_1=-n$, and all $h\ge2$ terms contain $n$, so
  

$$
w_1^{\exp}\equiv F(2n+1)\equiv2\pmod p.
$$



Here $F(m)=mF(m-1)+1$ supplies the last congruences.

The $\tau$-recurrence gives


$$
\tau_{n+1}\equiv\tau_n\pmod p,
\qquad z_1/z_0\equiv1\pmod p.
$$


Also $E_n\equiv0\pmod p$, by separating its first two falling-factorial terms. Hence (5.2) proves


$$
\boxed{
f_n\omega_n\equiv2(-1)^n\tau_n\pmod p,
\qquad
v_p(\omega_n)=-2v_p(n!).
}
\tag{5.6}
$$


In particular, $\omega_n\ne0$ at every eligible index.

### 5.3 Denominator warning

For the reduced denominator $D_n^\omega$, nonvanishing and (5.4) give


$$
D_n^\omega\ge\frac{n!}{64\,7^n}.
$$


Equation (5.6) identifies its selected-prime part exactly.

This does **not** bound the denominator of the reconstructed center: the force uses $f_n\omega_n$, and multiplication by $f_n$ can cancel these poles.

Likewise,


$$
\omega_n\ne0
$$


does not imply


$$
q_\lambda S-p_\lambda\ne0.
$$


Those are different quantities.

---

## 6. Actual terminal-plane residue and two-stage target

The homogeneous split is exact:


$$
w^{\exp}
=w^{\exp,\mathrm{flat}}+\frac{F(n)}{n!}z.
$$


Thus the moving residue must remain


$$
\boxed{
\Theta^{\exp}
=\Theta^{\exp,\mathrm{flat}}
+n!\mathfrak u_n^{\exp}F(n).
}
\tag{6.1}
$$


Replacing $F(n)$ by $1$ is not justified.

Using A3’s endpoint responses, with the exterior $+1$ retained in


$$
A_0=1+\delta_ng_0+E_nh_0,
$$


the endpoint determinant cancellation gives


$$
\mathcal D_n=U_0A_3-U_3A_0
$$


and


$$
\Theta^{\exp}
=\frac{U_0A_3+f_n\sigma_nU_0U_3}{\mathcal D_n}.
$$


The cancellation is of the common homogeneous contribution in the determinant, not of the homogeneous contribution in the numerator.

At eligible primes, where $k$ and $\mathfrak u_n^{\exp}$ are units, reconstruction first requires


$$
a-k\Theta^{\exp,\mathrm{flat}}\equiv0\pmod{p^{N_p}}.
$$


Only after this divisibility has been established may one form


$$
\frac{a-k\Theta^{\exp,\mathrm{flat}}}
{k n!\mathfrak u_n^{\exp}}
\equiv F(n)
\pmod{p^{N_p-\lfloor\log_p n\rfloor}}.
$$


The older, weaker exponent remains valid as well.

The logarithmic restoration has exactly the two shifts


$$
\sigma_n\mapsto\sigma_n+\frac{4\rho_n}{\tau_n},
\qquad
\delta_n\mapsto\delta_n+\frac{2(-1)^nf_n}{\tau_n}.
$$



**Verdict:** the target and terminal-plane formula are correct, subject to the retained unit hypotheses.

---

## 7. Continued-fraction gap implication

Let $r/L$ be the actual residue fraction, with


$$
a\equiv kr\pmod L.
$$


Suppose consecutive continued-fraction convergents satisfy


$$
q_j\le L^{1/3}<q_{j+1}\le L^{2/3}.
$$


The dual vectors


$$
d_j=(q_j,p_jL-q_jr),\qquad
d_{j+1}=(q_{j+1},p_{j+1}L-q_{j+1}r)
$$


have determinant $\pm L$.

The convergent error bound gives


$$
|p_jL-q_jr|<L/q_{j+1}<L^{2/3}.
$$


For the next vector, either it is the exact final convergent and the error is zero, or its next denominator is larger than $q_{j+1}$, giving the same bound.

For


$$
\max(|a|,k)<\tfrac12L^{1/3},
$$


each pairing


$$
q_\ell a+(p_\ell L-q_\ell r)k
$$


is divisible by $L$ and has absolute value less than $L$. Both must vanish, contradicting independence.

**Verdict:** this implication is correct, including for a rational residue whose reduced denominator may divide $L$.

What is open is precisely the stated gap condition for the actual residue (6.1). Fast polynomial rational reconstruction or XGCD algorithms do not establish this arithmetic condition. Nor would exclusion of small reconstructions, by itself, prove irrationality of $e+\pi$.

---

## 8. Full gcd and the genuine endpoint-growth obligation

Retain the complete normalization


$$
q_\lambda=\frac{kh|AB|}{F_{\rm gcd}GH_{\rm gcd}},
$$


with


$$
F_{\rm gcd}=\gcd(|A|,|a|)\gcd(|B|,|a-k|),
\quad
G=\gcd(k,|J|),
$$


and


$$
H_{\rm gcd}
=\gcd\!\left(h,\frac{|T|}{F_{\rm gcd}G}\right).
$$



Since $G\mid k$ and $H_{\rm gcd}\mid h$,


$$
\frac{k}{G}\frac{h}{H_{\rm gcd}}
$$


is an integer. Therefore


$$
q_\lambda\ge\frac{|AB|}{F_{\rm gcd}}.
$$


When $a(a-k)\ne0$,


$$
F_{\rm gcd}\le |a|\,|a-k|,
$$


and primewise


$$
\boxed{
(q_\lambda)_{\mathcal P^c}
\ge
\frac{|AB|_{\mathcal P^c}}{|a|\,|a-k|}.
}
\tag{8.1}
$$



This is a valid consequence of the **full** gcd formula. No omitted shared gcd can freely erase the coprime endpoint factor.

A concrete next lemma is:

> On one specified original smooth family, determine or bound
> 

$$
> \log |AB|_{\mathcal P^c}
>
$$


> for the actual reduced endpoints obtained from $C^{-1}z$, after clearing and removing their actual common content.

One can express these endpoints through


$$
-s^T\operatorname{adj}(C)z,\qquad
e_2^T\operatorname{adj}(C)z,
$$


but an archimedean estimate for these cofactors is not enough: their exact rational clearers and common content must also be bounded.

No actual $d=2$ infinite-family endpoint-growth bridge is proved in the packet. The accepted $b=0$ primitive-growth obstruction does not supply it.

---

# Part II. A5turn16 and the complete finite certificate

## 9. Band-plus-boundary factorization and transpose orientations

At precision $2^M$, let


$$
m=\min(2n,4(M-1)).
$$


The binomial identity used after the finite Pascal transform is correct:


$$
\binom{n+i}{s}\binom{n+i-s}{j}
=\binom{j+s}{s}\binom{n+i}{j+s}.
$$



Interior terms have $j+s<b$; crossing terms have


$$
j+s=b+r,\qquad0\le r<m.
$$


Only the last $\min(m,b)$ contact columns can occur in the crossing block.

Subtracting the missing part of the full binomial convolution gives


$$
F_{jr}
=-\sum_{v=0}^r
\binom{-n}{b+v-j}\binom n{r-v}.
$$


The minus sign and the finite tail limit are correct.

Thus


$$
A\equiv LUJU\pmod{2^M},
\qquad
J=H+J_{\rm end}E.
$$


Here $H$ is lower triangular with diagonal $1$, and


$$
H\equiv I,\qquad J_{\rm end}\equiv0\pmod2.
$$



Consequently


$$
\boxed{
A^{-T}\equiv L^{-T}U^{-T}J^{-T}U^{-T}.
}
$$


This order is correct.

With


$$
Z=H^{-T}E^T,
$$


the transpose Woodbury formula is


$$
J^{-T}v
=z^{(0)}
-Z(I+J_{\rm end}^TZ)^{-1}J_{\rm end}^Tz^{(0)},
\qquad z^{(0)}=H^{-T}v.
$$


The Schur matrix is congruent to $I$ modulo $2$, so only unit inversion is used.

Finally,


$$
(U^{-T}z)_j=\sum_{i=0}^j\binom{-n}{j-i}z_i,
$$


and


$$
(L^{-T}t)_i
=\sum_{j=i}^{b-1}(-1)^{j-i}\binom ji\,t_j.
$$


Both orientations and endpoints are correct.

**Important interpretation:** the correction matrix is banded and the boundary correction has bounded rank. Its inverse need not be banded. These identities do not reduce the actual polynomial length from $b$ to $O(M)$.

---

## 10. Endpoint adjoint vector and one-variable mixed contraction

For


$$
\mathsf a=\mathcal RA^{-1}f,\qquad
\mathsf b=\mathcal RA^{-1}r+W_be_b,
$$


the adjoint input is


$$
\boxed{
q_j=-W_j\mathsf a_j+(j+1)W_{j+1}\mathsf a_{j+1},
\quad0\le j<b.
}
$$


In particular, $q_{b-1}$ contains $\mathsf a_b$.

With $w=A^{-T}q$,


$$
\boxed{
4N=w^Tf,\qquad
8H=w^Tr+W_b\mathsf a_b.
}
\tag{10.1}
$$


These are exact finite-dimensional identities.

For


$$
\mathscr W(x)=\sum_{i=0}^{b-1}w_ix^i,
$$


coefficientwise interpretation of


$$
\binom{n+\Theta}{s},\qquad\Theta=x\,d/dx,
$$


avoids division by a potentially nonunit $s!$.

The coefficient identity


$$
[z^{b+t}](1+z)^{2n-s}
\left[\binom{n+\Theta}{s}\mathscr W\right](1+z)
=
\sum_{i=0}^{b-1}w_i
\binom{n+i}{s}\binom{2n+i-s}{b+t}
$$


proves A5’s contraction.

### Valid-term guards

The safe finite interpretation retains


$$
a<M,\quad s\le4a,\quad a+v_2(t!)<M,
$$


together with the original source restrictions, including


$$
s\le n+i,\qquad b+t\le2n+i-s
$$


when the binomial term is nonzero.

On the original small-precision branch, $s\le2n$, so the displayed polynomial power is nonnegative. If this fails, use the guarded original finite sum, not an unqualified negative-power coefficient extraction.

The normalized logarithmic contribution may be omitted only when


$$
M\le K_{\rm norm}.
$$


Otherwise the exact additional term is


$$
\sum_{i=0}^{b-1}w_i\,h_i^F/b!.
$$


The separate endpoint term $W_b\mathsf a_b$ remains in every branch.

---

## 11. Norm cutoff and a precision correction

The accepted complete first-force budget gives


$$
v_2(f_i)\ge v_2(\lfloor i/2\rfloor!).
$$


Thus


$$
4N\equiv\sum_{i<\min(b,I_M)}f_iw_i\pmod{2^M}.
$$


The sufficient bound $I_M\le4M$ is valid. At $M=13$, the budget itself permits


$$
I_{13}=32,
$$


since $v_2(15!)=11$ and $v_2(16!)=15$. The certificate’s earlier zeros are extra finite information, not a stronger general cutoff.

### Correct replacement-error lemma

Let


$$
\widetilde{\mathsf a}=\mathsf a+\varepsilon,\qquad
\varepsilon\in2^T\mathbb Z_2^{b+1},
\qquad
a=\min_jv_2(\mathsf a_j).
$$


Then


$$
\widetilde{\mathsf a}^{\,T}\widetilde{\mathsf a}
-\mathsf a^T\mathsf a
=2\mathsf a^T\varepsilon+\varepsilon^T\varepsilon,
$$


so universally


$$
\boxed{
v_2(\widetilde{\mathsf a}^{\,T}\widetilde{\mathsf a}
-\mathsf a^T\mathsf a)
\ge\min(T+a+1,2T).
}
\tag{11.1}
$$


The simpler depth $T+a+1$ follows when $T\ge a+1$. Without that condition or an additional cancellation theorem, it is not automatic.

For a fixed exact second column of content $c$,


$$
v_2(\widetilde{\mathsf a}^{\,T}\mathsf b-\mathsf a^T\mathsf b)
\ge T+c.
$$



There is a further distinction for the adjoint implementation. If $\widetilde w$ is formed from $\widetilde{\mathsf a}$, but the contraction uses the **exact** force $f$, then


$$
\widetilde w^Tf
=\widetilde{\mathsf a}^{\,T}\mathsf a.
$$


Its norm-channel error is only guaranteed to have depth


$$
T+a,
$$


not $T+a+1$.

**Practical consequence:** a first-column truncation budget must specify whether it evaluates a squared approximate column or a one-sided adjoint contraction. Their guard digits are different.

---

## 12. Central evaluator and supplied finite arithmetic

### 12.1 Missing import repaired

The attached evaluator explicitly uses


$$
a_s=\frac{2^s(s!)^2}{(2s+\varepsilon)!},
\qquad \varepsilon\in\{0,1\}.
$$


Legendre’s factorial formula gives


$$
v_2(a_s)=v_2(s!).
$$


For integer $h$, the generalized binomial factors in the central sum are integral. The prefactor is also integral.

Since


$$
v_2(96!)=96-s_2(96)=94,
$$


every omitted term $s\ge96$ has depth at least $94$. The stop at $96$ is therefore safe for modulus $2^{64}$, and hence for the downstream modulus $2^{13}$.

This repairs the reproducibility gap in the previous packet. It does not turn the finite parameter-difference checks into an all-word or relative norm theorem.

The signed diagnostic `force(k)` and the normalized positive-sign force assembly in the contact certificate have different displayed conventions. The latter must be interpreted through the accepted normalization bridge; one must not insert the former’s factor $(-1)^i$ into the contact input.

### 12.2 Auxiliary relative digits

From the supplied complete Gram residues:

- $b=81$:
  

$$
N\equiv1062\pmod{2048},\quad H\equiv486\pmod{1024}.
$$


  Thus
  

$$
H/N\equiv243/531\equiv417\pmod{512}.
$$



- $b=209$:
  

$$
N\equiv560\pmod{2048},\quad H\equiv304\pmod{1024}.
$$


  Thus
  

$$
H/N\equiv19/35\equiv17\pmod{64}.
$$



The divisions and modular inverses in A5 are correct.

The supplied coordinates also exhibit the contents directly:


$$
\begin{array}{c|rrrrrr}
b&a&c&d=v_2(4N)&e=v_2(8H)&d-2a&e-a-c\\ \hline
81&1&2&3&4&1&1\\
209&2&3&6&7&2&2
\end{array}
$$


For example, the coordinate-zero pairs $(6170,3876)$ and $(2420,6344)$ attain the reported contents. Thus column primitivity does not imply primitive norm-unit behavior.

### 12.3 Original unit pivot

The original $f_0$ values are even; the $f_1$ values are odd. The inverses


$$
1545^{-1}\equiv2105,\qquad5641^{-1}\equiv6201\pmod{8192}
$$


are correct, as are


$$
\boxed{
f_0/f_1\equiv7602,1970,4530,7090\pmod{8192}.
}
$$



The resulting Gram-channel formulas are valid at the four supplied indices. The zeros $r_0,r_1$ leave $B_*$, including its endpoint; they do not annihilate the mixed contraction.

The certificate now includes full auxiliary coordinate arrays, but no original-family Gram arrays. Its singular “One complete … system” scope string remains stale and should say **two auxiliary systems**.

---

## 13. Raw and relative guard-digit ledger

Let


$$
D=\mathsf a^T\mathsf a,\qquad E=\mathsf a^T\mathsf b,
\qquad d=v_2(D),\quad e=v_2(E).
$$


Then


$$
H/N=E/(2D).
$$



If both raw quantities are known modulo $2^M$, and $M>d,e$, quotient perturbation gives


$$
v_2(\text{ratio error})
\ge\min(M-d-1,M+e-2d-1).
$$


Thus A5’s sufficient condition


$$
\boxed{
M\ge\max(s+d+1,\ s+2d+1-e)
}
$$


is correct.

An asymmetric version, useful in practice, is:


$$
\boxed{
M_E\ge s+d+1,\qquad
M_D\ge s+2d+1-e,
}
\tag{13.1}
$$


with $M_E>e$, $M_D>d$.

Other mandatory losses are:

| Output or operation | Required precision |
|---|---|
| $N\bmod2^s$ from $D=4N$ | $D\bmod2^{s+2}$ |
| $H\bmod2^s$ from $E=8H$ | $E\bmod2^{s+3}$ |
| Normalized force modulo $2^M$ by raw division by $b!$ | Raw numerator modulo $2^{M+v_2(b!)}$ |
| Omit complete logarithmic force | Require $M\le K_{\rm norm}$ |
| Assignment’s variable raw target | Require $M\ge2\mu+6$ |
| Replace second-force initials at depth $T$, ratio modulo $2^s$ | Require $T\ge s+d+1-a$ |

For the two auxiliary systems, $e=d+1$, so raw $M=13$ gives exactly $s=9$ and $s=6$. This explains the moduli $512$ and $64$; no extra relative digit is justified.

---

# Part III. Follow-on results and remaining proof obligations

## 14. A justified route toward actual relative outputs

A valid next step is an adaptive, norm-sensitive evaluation, not an assumption of alignment.

1. Evaluate the actual raw norm and mixed channels at a declared precision.
2. If either is zero at that precision, increase the precision; do not assign an exact valuation to a zero residue.
3. Once $d,e$ are certified by nonzero digits, apply (13.1) for the desired relative modulus.
4. Preserve the full endpoint correction, the high coefficient index $b+t$, and the complete logarithmic contribution whenever its omission budget is exceeded.

The missing mathematical compression can be stated narrowly:

> **Actual adjoint-moment compression lemma.**  
> Construct, for the original binary family, a precision-controlled representation sufficient to evaluate
> 

$$
> \sum_{i<I_M}f_iw_i
>
$$


> and every guarded moment
> 

$$
> [z^{b+t}](1+z)^{2n-s}
> \left[\binom{n+\Theta}{s}\mathscr W\right](1+z),
>
$$


> including the finite boundary Schur correction, without retaining $b$ coefficients. Prove its behavior under $b\mapsto9^{32}b$, with the actual norm valuation paid.

Classical digit-transfer methods supply background for finite evaluability. They do not already prove this specialized compressed moment law or a preserved relation between its two outputs.

---

## 15. Bounded exact checks for personal inspection

These checks would validate implementations and finite outputs only.

### A. A3 recurrence and contact normalization

Inputs:


$$
n=15,30,105,210.
$$


Retain the complete original contact vectors and add only neighboring diagonal data through $n+2$. Auxiliary force indices need reach at most $2n+4$, hence $424$.

Expected exact outputs:

- zero residual for the complete forced recurrence, including all of $\Psi_n$;
- zero residual for (3.1), (3.4), (5.2), and (5.3);
- zero residual for the actual two-stage target (6.1);
- the selected-prime valuations and residues predicted by (5.6);
- logarithmic depths at least $K_p^*$, with older budget fields clearly labeled as bounds.

### B. Binary adjoint audit

Inputs:


$$
(b,n)=(81,324162),(209,836418),\qquad M=13.
$$


Use the supplied complete force and coordinate arrays, symbol degree $48$, and actual endpoint coordinates.

Expected outputs:


$$
A^Tw-q\equiv0\pmod{8192},
$$


and agreement of the direct and adjoint contractions:


$$
\begin{array}{c|cc}
b&4N\bmod8192&8H\bmod8192\\ \hline
81&4248&3888\\
209&2240&2432
\end{array}
$$



The one-variable extraction must agree with the mixed entry after adding $W_b\mathsf a_b$. Report that endpoint contribution separately, but retain it in the total.

The resulting relative certificates are exactly


$$
H/N\equiv417\pmod{512},\qquad
H/N\equiv17\pmod{64}.
$$



### C. Replacement-precision check

For a small integral test vector and an explicit perturbation of depth $T=a$, verify the two terms in


$$
2\mathsf a^T\varepsilon+\varepsilon^T\varepsilon.
$$


Expected output: the general bound is (11.1); the stronger $T+a+1$ bound requires its additional hypothesis. Separately distinguish the one-sided adjoint contraction from the squared approximate norm.

No original-family conclusion follows from these bounded checks.

---

## 16. Final primitive denominators and whole evaluated errors

### A3

The complete primitive pair remains


$$
q_\lambda=\frac{kh|AB|}{F_{\rm gcd}GH_{\rm gcd}},
\qquad
p_\lambda=
\operatorname{sgn}(AB)\frac{T}{F_{\rm gcd}GH_{\rm gcd}}.
$$


Its whole error is


$$
\boxed{
q_\lambda S-p_\lambda
=q_\lambda e_3\alpha_{n,2}(\lambda-\Lambda_{n,2}).
}
$$


A successful irrationality construction requires the entire expression to be nonzero and tend to zero. Displacement nonvanishing does not replace proof that


$$
\lambda\ne\Lambda_{n,2}.
$$



### A5

Retain the least actual two-column clearer and complete integer Gram pair:


$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
$$


The primitive multiplier is $d_B^2/g_B$, including every prime.

The binary interface remains


$$
v_2(q_n)=
\max\left\{
0,\frac{3n}{2}-v_2(b!)-s_2(n)-1-(\gamma-\alpha)
\right\}.
$$


Neither auxiliary equality $\gamma=\alpha$ nor the four original initial zeros establishes an original-family equality.

Under the accepted signed-error theorem,


$$
\boxed{
q_nS-p_n=-q_n\epsilon_n>0
}
$$


eventually. Irrationality by this route still needs a same-index bound forcing this **whole** positive expression to zero.

---

## Final proof-status ledger

| Item | Audit result |
|---|---|
| Complete A3 diagonal recurrence | Valid, with all three forcing terms |
| Classical Legendre companion | Reused classical result |
| Complete original logarithmic contact normalization | Proved |
| Sharper logarithmic strip | Valid under stated selected-prime hypotheses |
| Selected-prime denominator stability | Valid at that scope only |
| Exponential Wronskian and factorial real tail | Valid |
| Selected-prime pole and displacement nonvanishing | Valid |
| Actual $F(n)$ two-stage target | Valid and indispensable |
| Continued-fraction exclusion implication | Valid conditional argument |
| Actual moving-residue gap theorem | Open |
| Full-gcd unselected endpoint lower bound | Valid |
| Actual $d=2$ endpoint-growth bridge | Open |
| Binary band-plus-boundary factorization | Valid |
| All displayed inverse-transpose orientations | Correct |
| Endpoint $q$ and exterior mixed contribution | Correct |
| One-variable contraction | Valid with explicit source guards |
| Norm cutoff | Valid |
| First-column norm replacement budget | Requires correction/qualification |
| Central evaluator tail | Valid; missing import repaired |
| Auxiliary ratio digits and original $f_1$ pivot digits | Correct finite deductions |
| Original binary relative norm/mixed theorem | Open |
| Full primitive-denominator/whole-error comparison | Open |

## Conclusion

The substantive audit result is that the two proposed reductions are mathematically usable **without changing their original indices, finite boundaries, complete forces, or endpoint terms**. The complete logarithmic normalization is established; the binary adjoint orientation and normalized contraction are confirmed. The precision analysis is sharpened by distinguishing quadratic norm replacement from one-sided adjoint evaluation.

The exact remaining bottleneck is arithmetic, not merely algebraic inversion:

- for A3, control the actual moving-residue height or the actual coprime endpoint factor after full content removal;
- for A5, evaluate and relate the actual normalized adjoint moments at precision tied to the first nonzero norm digit;
- for either route, control the least clearer, final all-prime gcd, actual primitive denominator, and whole nonzero evaluated error.



$$
\boxed{\text{The irrationality or rationality of }e+\pi\text{ remains unresolved.}}
$$


