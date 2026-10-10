> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 audit: all-sublinear scalar closure and shifted whole-column transfer

## Executive verdict

The two audits have different outcomes.

1. **A3turn25’s scalar argument closes the all-sublinear relative-error interface**, using:
   - the already audited UB conclusion;
   - the archived exact equilibrium stationary-value identity, at its stated algebraic scope;
   - the original characteristic-integral reconstruction formulas.

   I find no additional restriction on the rate at which $b/n\to0$. There is one worthwhile repair: the bounded/slow-$d$ join can be proved directly from the estimates in turn25, without invoking an incompletely reproduced earlier relative-asymptotic theorem. I give that proof below.

2. **A2turn21’s high-factor construction and shifted whole-column divisibility pass.** Its treatment of higher carries, offsupport coordinates, precision and the actual endpoint is structurally sound.

   **The final mixed/norm transfer passes conditional on the stated leading low-polynomial identities.** However, the supplied texts do not independently certify those identities coefficientwise: they give the kernel construction and the four contracted constants, but not the definition or coefficient certificate for the old support $\mathcal X$, $c(x)$, and $\xi(x)$. This is a specific bounded verification gap—not a defect in the now-supplied kernel definitions, and not a reason to reject the high-factor argument. The finite norm table alone does not fill it.

Neither result bounds the actual primitive denominator after the final gcd. Irrationality of $e+\pi$ remains unresolved.

---

## 1. Scope of the checks and source use

This report checks the supplied archive excerpts and responses. No filesystem, executable arithmetic environment or external-search tool is available in this exchange; I therefore do **not** claim fresh archive searches, primary-literature searches, hash verification, or executed calculations.

The supplied archive records bounded searches and primary-source checks for:

- Selberg/characteristic-integral methods;
- Brascamp–Lieb variance estimates;
- stability and zero-free methods;
- equilibrium and saddle-point analysis.

The classical results are used only with the hypotheses actually exhibited here. In particular:

- a positive principal ensemble is not substituted for the actual complex integral;
- odd outer sectors remain signed;
- zero-freeness of an insertion is not mistaken for zero-freeness of its expectation;
- a formal equilibrium stationary identity is not itself a scalar-integral asymptotic.

For the main audit, UB is reused as instructed, with coercivity on the actual image replacing the unnecessary surjectivity assertion.

---

# Part I. A3turn25: all-sublinear scalar closure

Throughout this part,


$$
\sigma=\sqrt2,\quad M=1+\sqrt2,\quad \rho=M^{-1},\quad d=b-1,
$$


and


$$
n\to\infty,\qquad 1\le b=o(n),\qquad 0\le j\le b.
$$



All uniform statements below include both parities of $n$.

## 2. Sector normalization and adjacent norms: pass

For a symmetric insertion $G$, the sector factor


$$
\frac{(-1)^{nk}}{k!(r-k)!}
$$


is correct. It comes from the original $1/r!$ normalization and the choice of the $k$ outer variables. There is no further binomial multiplier.

The same-weight norm comparison is also correct. All dimensions use the same $n,q$ and one-particle measure, so


$$
\frac{Z_r(q)}{Z_{r-k}(q)}
=\prod_{\ell=r-k}^{r-1}h_\ell(q).
$$


The arc lower bound


$$
h_\ell(q)\ge C_\delta g_\delta^n
                  \frac{B_\delta^\ell}{(\ell+1)^2}
$$


therefore controls the actual adjacent-dimensional quotient.

The number of Vandermonde factors involving outer particles is


$$
k(r-k)+\binom{k}{2}\le kr.
$$


Bounding each by $4$ gives the stated sector estimate, with harmless enlargement of constants:


$$
\frac{\text{absolute \(k\)-outer sector}}{Z_r(q)}
\le \frac1{k!}
\left[Cr^2(4/B_\delta)^r(Mg_\delta)^{-n}\right]^k.
$$


For $r=o(n)$, its bracket is exponentially small. Fixed-order characteristic derivatives introduce only powers of $d$; these do not change that conclusion.

**No parity loss occurs:** the absolute estimate bounds the possible cancellation caused by the original $(-1)^{nk}$, rather than removing that sign.

## 3. Gamma insertion and actual normalization: pass

The normalized degree-$k$ gamma term has constant coefficient $1$. Its nonconstant coefficient sum is bounded by


$$
\sum_{\ell=1}^k
\binom{k}{\ell}\sigma^\ell
\frac{\Gamma(n+k-\ell)}{\Gamma(n+k)}
\le (1+\sigma/n)^k-1.
$$


The actual middle-coordinate reference is a positive combination of these normalized terms. Consequently


$$
\sup_{|z_\ell|\le1}|S_j(z)-1|
\le e^{\sigma d/n}-1=O(d/n)
$$


uniformly over every actual coordinate.

This proves more than the older sector bound and correctly retains $B_j$, the exact top-column reference scale. It does not replace $R_j$ by a top-column approximation.

For positive real $q$, reflection gives an odd principal phase and hence


$$
\mathbb E_q e^{i\Phi_q}=1+O(d/n).
$$


Together with $S_j=1+O(d/n)$, this gives


$$
s_jA_j(q)=B_jZ_d(q)
 \left(1+O(d/n)+O(e^{-\eta n+Cd})\right).
$$


The normalization is the actual complex expectation, not merely its modulus.

The cases $d=0,1$ cause no problem. In particular,


$$
d=0:\qquad R_0=-1,\quad R_1=1.
$$



## 4. Zero-free logarithms and reciprocal anchors: pass

Fixed disks around $M,\rho$, strictly inside the supplied zero-free regions, are simply connected. Thus the real-anchored logarithms exist there.

The modulus comparison gives


$$
|\Re\mathcal H_j|\le C(d+1).
$$


Interior harmonic estimates then bound its derivatives. One need not assert an unrestricted global logarithm on the annulus $2\le |q|\le3$. The proof uses only the fixed local disks.

The anchor identity is exact:


$$
|z^{-1}+M|=M|z^{-1}+\rho|,\qquad |z|=1.
$$


Thus


$$
Z_d(M)=M^dZ_d(\rho),
$$


with identical normalized positive measures at the two anchors. Actual noncancellation then supplies


$$
\log\frac{s_jA_j(\rho)}{s_jA_j(M)}
=-d\log M+O(d/n)+O(e^{-\eta n+Cd}).
$$



This avoids an order-one normalization error that a leading partition-function approximation would not exclude.

## 5. Actual saddles, Gaussian constants and contours: pass

The logarithmic derivative estimates give, uniformly,


$$
r_{j,\pm}=1+O(d/n),
$$


and


$$
\lambda_{j,+}=2a+O(d/n),\qquad
\lambda_{j,-}=2\beta+O(d/n),
$$


where


$$
a=\frac{\sigma}{2M},\qquad \beta=\frac{\sigma M}{2}.
$$


Therefore


$$
\sqrt{\lambda_{j,+}/\lambda_{j,-}}
=M^{-1}(1+o(1)).
$$



The scalar contour measure is $d\zeta/(i\zeta)$. On $\zeta=re^{i\theta}$ it becomes $d\theta$, so no additional factor $r$ belongs in the Gaussian prefactor.

The local window $|\theta|\le n^{-2/5}$ gives the uniform exponent remainder


$$
O(n|\theta|^3)=O(n^{-1/5}).
$$


The remaining central arc is controlled by strict angular curvature.

For the remote arcs, the decisive bound is


$$
C\sqrt n\,\exp[-n/400+Cd].
$$


It is exponentially small for **every** $d=o(n)$, including arbitrarily slow convergence of $d/n$ to zero.

Both minus connectors are required and both are present. At their endpoints,


$$
h(e^{\pm i\pi/4})=0,
$$


and along them


$$
h(re^{\pm i\pi/4})
=\frac{r+r^{-1}}2-1
 \pm i\frac{r-r^{-1}}2.
$$


Hence each connector is exponentially negligible compared with the positive real saddle. The orientation determines an additive connector sign, but its absolute bound suffices here.

The resulting scalar normalization ratio is exactly


$$
\frac{2n!}{n!/(2\pi)}=4\pi.
$$


Combining it with the Gaussian ratio supplies the additional $M^{-1}$.

## 6. UB and stationary values: pass at the retained algebraic input

For $d\to\infty$, UB gives


$$
(\log A_j)'(q)-dL_c'(q)=O(1),\qquad c=d/n.
$$


Integrating over either real saddle displacement, of length $O(c)$, yields an **absolute logarithmic error**


$$
O(c)=o(1),
$$


not $O(d\,c)$ or $O(nc^2)$.

The actual and equilibrium anchored phase functions are therefore uniformly $O(c)$-close on their common $O(c)$ saddle intervals. Comparing their minima is legitimate because both radial curvatures remain positive.

Using the archived exact equilibrium identity


$$
\Phi_+(r_+(c))-\Phi_-(r_-(c))=(2+c)\log M
$$


then gives


$$
n\Psi_{j,-}(r_{j,-})-n\Psi_{j,+}(r_{j,+})
=-(2n+d)\log M+o(1).
$$



Here the equilibrium identity is reused as an exact algebraic source result, not as an integration theorem. The contour analysis above is the additional argument that makes it applicable to the actual forces.

### Repair: a self-contained bounded/slow-$d$ join

Turn25’s appeal to a previous relative regime is unnecessary.

From the already established local derivative bounds,


$$
r_{j,\pm}-1=O(d/n).
$$


Taylor expansion between $1$ and the actual saddle therefore gives


$$
n\bigl(\Psi_{j,\pm}(r_{j,\pm})
             -\Psi_{j,\pm}(1)\bigr)
=O(d^2/n).
$$


At the anchors,


$$
n\bigl(\Psi_{j,-}(1)-\Psi_{j,+}(1)\bigr)
=-(2n+d)\log M
 +O(d/n)+O(e^{-\eta n+Cd}).
$$


Consequently, uniformly when $b\le n^{1/8}$,


$$
n\Psi_{j,-}(r_{j,-})-n\Psi_{j,+}(r_{j,+})
=-(2n+d)\log M+o(1).
$$


This includes $d=0,1$.

On $b>n^{1/8}$, one has $d\to\infty$, so UB applies. This split covers oscillating allocations as well as bounded ones and introduces no rate restriction.

It follows that


$$
\boxed{\frac{F_j}{P_j}
=4\pi M^{-2n-b}(1+o(1))}
$$


uniformly in all actual coordinates.

## 7. Scalar lower bound, complete $eE$, and endpoint: pass

At the real plus saddle, $g(r)\ge M$, while eventually $\sigma+r>2$. Thus


$$
|P_j|\ge C^{-1}n!n^{-1/2}M^nB_jZ_d(0).
$$



The complete exponential force is


$$
eE_i=-[z^{n+i}](1-z+z^2/2)^n
                 \int_0^1s^ne^{1-s+sz}\,ds.
$$


On $|z|=\sigma$,


$$
|1-z+z^2/2|\le \sigma M,
$$


which gives


$$
\sigma^i|eE_i|\le \frac{e^\sigma M^n}{n+1}.
$$


Summing the full elementary-symmetric insertion yields


$$
|E_j/P_j|\le \frac{C2^d}{n!\sqrt n}.
$$



For coordinate zero, the same-weight identity and the trial polynomial $z^d$ give


$$
Z_{d+1}(0)/Z_d(0)=h_d(0)\le e^\sigma M^n.
$$


Therefore


$$
|D/P_0|\le \frac{C\sqrt n}{n!B_0},
\qquad B_0=(n)_d\sigma^{-d}\ge1
$$


eventually, with $B_0=1$ for $d=0$.

After division by $M^{-2n-b}$, the logarithms of both residual bounds are at most


$$
-n\log n+O(n)+O(d).
$$


They tend to $-\infty$ on every sublinear allocation. No exponential-force term or coordinate-zero endpoint has been dropped.

## 8. Main conclusion and metric scope

The exact whole coordinate error remains


$$
\frac{v_j}{u_j}-S
=\frac{E_j}{P_j}
 +(-1)^{n+1}\frac{F_j}{P_j}
 +(-1)^n\delta_{j0}\frac D{P_j}.
$$


Hence, at the source dependencies specified above,


$$
\boxed{
\frac{v_j}{u_j}-S
=(-1)^{n+1}4\pi M^{-2n-b}(1+o(1)).
}
$$



For every positive diagonal metric in these same actual coordinates,


$$
c_W-S
=\sum_j
\frac{W_{jj}u_j^2}{\sum_\ell W_{\ell\ell}u_\ell^2}
\left(\frac{v_j}{u_j}-S\right).
$$


Uniformity makes the conclusion valid even for arbitrarily varying positive diagonal entries:


$$
\boxed{
c_W-S=(-1)^{n+1}4\pi M^{-2n-b}(1+o(1))\ne0
}
$$


eventually.

There is no corresponding assertion here for nondiagonal metrics.

---

# Part II. A2turn21: shifted transfer

## 9. Finite kernels and precision: pass

The supplied turns13/15 resolve the kernel-definition issue.

The identity


$$
C_s(k,l)=
\sum_{v=0}^s
\binom{k}{s-v}\binom nv
\binom{-v}{l-k+s-v}
$$


comes from the displayed row generating function. In its finite multiplication, the intermediate index is at most $l<b$. Thus the inverse remains the actual $b\times b$ inverse.

The signed-Newton closure retains the upper limit


$$
b-1-k+s-v.
$$


Its hockey-stick summation is exact. The valuation/degree filtration is valid for the actual integer-valued polynomial operators.

The boundary elimination also preserves all exterior terms before eliminating them into the $c_s$. Endpoint absorption uses the exact convolution identity giving the extended value $-1$ at $j=b$, thereby retaining the genuine $+W_b$.

At the precision needed for turn21, the reconstruction factors justify:

- positive support through $q=58$;
- negative support through $q=-60$;
- retention of the unit boundary and both contributing factorial blocks;
- removal of higher blocks only after their coefficient valuations are combined with reconstruction carries.

The warning in turn22 about freezing $j$ occurs one precision later. Its omitted term has valuation $5$ in $Y$, so it does **not** invalidate turn21’s $Y\bmod p^5$ construction.

## 10. Common high-factor ideal and whole divisibility: pass

Write $j=LJ+x$, $L=29^4$. Exact four-level stripping leaves


$$
F(J)(N-J)^e(2N+h-J+1)^u(h-J)^r.
$$


The factors $e,u$ depend only on $x$, not on the retained Laurent exponent $q$. Thus every retained term contains


$$
G_x=\ell_1^e\ell_0^u.
$$


The explicit intervals give $e+u\ge1$ for every $0\le x<L$.

The low normalization must be checked before drawing this conclusion. The supplied carry decomposition does pay for it locally, including the extra low factor in $jW_jB_{-2}$. It does not divide a high binomial or an $\ell$-factor.

For $25\le d\le28$, Lucas gives


$$
29\mid F(J)\ell_0(J),\qquad
29\mid F(J)\ell_1(J)
$$


for every actual $J$. Indeed:

- for $d=26,27,28$, $F(J)\equiv0$;
- for $d=25$, its only possible nonzero low residue is $J\equiv3$, where both linear factors vanish.

Thus


$$
\boxed{
P,Q\in29\mathbb Z_{29}^{b+1},
\qquad Z_w\in29^3\mathbb Z_{29}^{b+1},
\qquad Y\in29^4\mathbb Z_{29}^{b+1}.
}
$$


This conclusion includes all offsupport coordinates and all higher carries. Higher carries can add divisibility; no unit assumption on $F(J)$ is made.

## 11. Polynomial cancellation: sound mechanism, bounded certification gap

Turn21 correctly requires cancellation in


$$
\mathbb F_{29}[J],
$$


not cancellation of coordinate values after multiplication by $F(J)$.

If the stated leading identities hold coefficientwise, then:

- on $\mathcal X$, cancellation of the nonzero polynomial $\ell_e$ gives
  

$$
A_x=C_nc(x),\qquad B_x=\xi(x);
$$


- outside $\mathcal X$, cancellation of the nonzero polynomial $G_x$ gives
  

$$
A_x=0.
$$



Consequently offsupport $P$-coordinates vanish modulo $29^2$, and contribute nothing to the shifted contractions.

The remaining exact sums are


$$
D/29^2=C_n^2\sum_e\kappa_e\sum_{J=0}^hS_e(J)^2,
$$




$$
M/29^2=C_n\sum_eg_e\sum_{J=0}^hS_e(J)^2
\pmod{29}.
$$


Since $g_e=\kappa_e/6$, these prove the claimed relation.

**What is not independently certified by the attachments:** the coefficientwise leading support identities used in that cancellation. The four numbers $\kappa_e,g_e$ certify contracted constants, not the identities of all low polynomials. Turns13/15 provide an explicit procedure to verify them, but an explicit procedure is not its executed output.

Accordingly,


$$
\boxed{
M/29^2=(6C_n)^{-1}D/29^2\pmod{29}
}
$$


passes as a rigorous implication of those polynomial identities. Its unconditional construction-level certification still requires the bounded check below.

## 12. Fifth-digit boundaries and endpoint: pass

The exact ranges are retained:


$$
t\le d:\ 0\le k\le H,\qquad
t>d:\ 0\le k\le H-1.
$$


The latter terms have two low carries in the shifted classes and vanish after division by $29$.

The no-carry exception $d=25,t=3$ produces exactly the two stated residual moments. Single-carry cases produce the contiguous high factors; no high binomial is divided as a unit.

The actual endpoint has


$$
W_b\in29^4\mathbb Z_{29},
$$


so its contribution to $M/29^2$ is zero. The $1$ in


$$
Y_b=W_b(1+b\theta^Q_{b-1})
$$


is retained.

The numerical $\rho$-table may remain a finite arithmetic input. Multiplication by $6^{-1}=5\bmod29$ gives the displayed $\sigma$-table correctly. Its numerical correctness is separate from the polynomial-transfer certificate.

---

# 13. Primitive arithmetic and final status

For a rational metric, retain the least actual two-column clearer and the final gcd:


$$
N_B=d_B[u,v],\quad
A_B=N_{B,1}^T\Omega N_{B,1},\quad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_B=A_B/g_B,\quad p_B=H_B/g_B.
$$


The primitive multiplier on the rational Gram pair is $d_B^2/g_B$, and


$$
q_BS-p_B=q_B(S-c_W)
$$


is the whole evaluated error.

The all-sublinear theorem must **not** be applied to the fixed-ratio family $n=2001b$. That family retains its separate supplied signed-rate dependency.

### New result and proof status

- The main scalar interface passes, with a direct, self-contained slow/bounded-$d$ join.
- The shifted whole-column divisibility passes from the supplied complete kernels.
- The shifted mixed/norm relation has a sound construction-level proof conditional on a specific coefficientwise leading-polynomial certificate.
- No all-depth alignment or final primitive-denominator bound is established.

### Exact remaining bottlenecks

Analytically, no additional sublinear scalar rate restriction remains at the retained source inputs.

Arithmetically, finite-depth alignment does not control $\mu-\delta$ at arbitrary depth, nor the denominator across all primes. An irrationality argument still needs an infinite same-index sequence on which the actual reduced denominator times the nonzero whole error tends to zero.

### Bounded exact calculation required for the secondary audit

Use $p=29$, $L=29^4$, the supplied graded kernels and all $0\le x<L$. Construct the **natural** leading stripping polynomials over $\mathbb F_{29}[J]$, keeping the higher-parameter residue symbolic or enumerating it.

Return:

1. coefficientwise verification of the claimed leading $P,Q$ identities on $\mathcal X$;
2. coefficientwise zero verification for the leading $P$-multiplier outside $\mathcal X$;
3. verification that every supported fibre has the asserted actual range;
4. the four contracted residues
   

$$
(\kappa_0,\kappa_1,g_0,g_1)=(11,18,26,3).
$$



All divisions must be justified before reduction, and no polynomial may be replaced by its class modulo $J^{29}-J$.

Successful output would certify the missing finite polynomial lemma and complete this secondary transfer audit. It would not establish all-depth alignment, a primitive-denominator rate, or irrationality of $e+\pi$.
