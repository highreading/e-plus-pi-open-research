> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4, Turn 20 — Audit of the actual Hankel normalization, prime-power Gram transfers, and fully normalized endpoint factors

## Executive conclusion

The supplied work does **not** prove or disprove the irrationality of


$$
S=e+\pi.
$$



The principal reductions in A1turn11, A2turn8, and A5turn17 survive audit at their stated scopes. Their consequences must, however, be separated carefully:

- **A1:** The actual terminal generator gives a unit resultant, and the determinant-one Krylov transformation gives an integral Hankel representation of the complete residual pair. These are genuine normalization results. They do not prove residual nonvanishing or a favorable relative valuation.
- **A2:** The odd-prime unit signs, finite-ring power quotient, interval-product orientation, and complete six-entry Gram construction are valid. They establish finite-precision evaluation, not the desired norm-relative output law.
- **A5:** The interior divided-power inverse is genuinely precision-sized. The finite-endpoint commutator is valid with a minor indexing convention made explicit below. Ordinary low-degree jets provably cannot support the final translation. Closure of a usable complete moment representation remains open.
- **Endpoint correction:** The coordinator’s correction is essential. The $A,B$ in the primitive denominator formula are formed **after making each complete endpoint row primitive**. They depend on the complete second force. My Turn 19 wording identifying their growth problem with first-column endpoint growth alone was incorrect and is withdrawn.

A corrected exact consequence is available. It expresses the actual endpoint product prime by prime through the two complete rows, and quantifies precisely the possible distortion caused by their row gcds. This gives a usable replacement for the defective growth formulation.

No tools were executed. The attached receipts are treated as supplied bounded arithmetic evidence; I do not claim independent execution or hash verification.

---

## 1. Domains and scope of the audit

The constructions remain distinct.

### 1.1 A1: the $3$-adic residual construction

Retain


$$
n=4^j+1,\qquad j>0,\qquad81\mid j,
$$


and


$$
A=n-2=H-D,\qquad H=3^{h-1},\qquad 0<D<H/972.
$$


The finite spaces are


$$
m=\frac{A+1}{2},\qquad d=\frac{3D}{2}-1,\qquad \nu=\frac D2-1,
$$




$$
U_a=(y-1)^a\quad(0\le a<D),\qquad
z_i=(y-1)^Dy^i\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m).
$$



The depth-$16$ conclusions apply only on the accepted sufficiently large window


$$
j\equiv81\pmod{243},\qquad
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=512\cdot17^2\,3^{15}.
$$



### 1.2 A2: the preferred $29$-adic family

Retain


$$
a=432827+682892t,\qquad b=3^a,\qquad n=2001b,
$$




$$
t\ge0,\qquad t\equiv364\pmod{841}.
$$


Contact coordinates are $0,\ldots,b-1$; reconstructed coordinates are $0,\ldots,b$.

### 1.3 A5: the binary family

Retain


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
$$


With $b=128D+81$, the last contact block has only residues $0,\ldots,80$, followed by the separate reconstructed endpoint $j=b$.

### 1.4 Endpoint-growth construction

The original smooth families remain


$$
n=15^r,\ r\ge2,\qquad\text{or}\qquad n=105^r,\ r\ge2,
$$


with $d=2$, three contact coordinates, and four reconstructed coordinates.

The receipt cases $15,30,105,210$ are finite consistency tests, not an infinite-family growth theorem.

### Dependency convention

Previously accepted block-invertibility, corrected-column, symbol-filtration, normalized-force, and producer-precision results are reused at their recorded hypotheses. Where a source invokes one of these results rather than reproving it, the present audit does not silently expand its scope.

The structured Hankel/Bezoutian mechanism, finite-ring Fitting theory, divided-power calculus, and prime-power digit methods are established background. No exhaustive novelty claim is made.

---

# Part I. Audit of A1turn11

## 2. Complete functional, finite displacement, and actual terminal residue

The functional must remain


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\sum_{\substack{v\ge0\\2v+1\le4n-3}}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1},
\qquad \mathfrak f(y^r)=(2r)!.
$$


Neither its factorial term nor its endpoint subtraction is dispensable.

Let


$$
Q_n^{\rm loc}=Q_c+3^6R,\qquad
Q_c=(y+1)(y-1)^A(\beta+3y),
$$


and


$$
G(f,g)=\mathcal M(Q_n^{\rm loc}fg).
$$



For truncated multiplication


$$
\mathscr Tf=yf-t(f)y^{m+1},\qquad t(f)=[y^m]f,
$$


the exact commutator is


$$
G(f,\mathscr Tg)-G(\mathscr Tf,g)
=t(f)\mathfrak r(g)-\mathfrak r(f)t(g).
$$


The subtraction inside


$$
\mathfrak r(f)=
\mathcal M\!\left(Q_n^{\rm loc}y^{m+1}(f-t(f)y^m)\right)
$$


ensures that the potentially exterior highest product cancels. No new HIGH coordinate is introduced.

With corrected residual columns $\widehat Z=Z-WK_{\rm elim}$, orthogonality gives


$$
S_{\rm act}\mathscr D-\mathscr D^TS_{\rm act}
=t_{\rm act}r_{\rm act}^T-r_{\rm act}t_{\rm act}^T,
$$


where


$$
\mathscr D=\mathscr C-e_0\ell^T.
$$



### 2.1 The terminal residue calculation is correct

At the original cutoff, the only odd denominator with valuation $h$ is $3^h=3H$. All other pole terms and the factorial term vanish modulo $3$. The functional is integral on the bounded-degree coefficient spaces used here.

For $z_i=(y-1)^Dy^i$, the surviving coefficient is


$$
[y^{r_*}](y-1)^H(\beta+3y)y^{m+1+i},
\qquad r_*=\frac{3H-1}{2}.
$$


The required index in $(y-1)^H$ is


$$
r_*-(m+1+i)=H+\nu-1-i.
$$


It exceeds $H$ when $i<\nu-1$, and equals $H$ when $i=\nu-1$. Since $\beta\equiv1\pmod3$,


$$
\boxed{r_{\rm act}\equiv e_{\nu-1}\pmod3.}
$$



The accepted corrected-column congruence also gives


$$
\ell_i\equiv-3\binom d{D-1}\mathbf1_{i=\nu-1}\pmod9,
\qquad
t_{\rm act}\equiv0\pmod9.
$$



**Verdict:** the actual unit terminal generator is established from the complete functional and the accepted corrected-column input. It is not a surrogate terminal channel.

---

## 3. Determinant-one Krylov basis and the final companion equation

Define


$$
p_0=1,\qquad p_{i+1}=Xp_i+\ell_i.
$$


For $i<\nu-1$,


$$
\mathscr De_i=e_{i+1}-\ell_i e_0,
$$


so induction gives


$$
p_i(\mathscr D)e_0=e_i.
$$



The actual last-column equation is


$$
\mathscr De_{\nu-1}
=-\sum_{i=0}^{\nu-1}q_i e_i-\ell_{\nu-1}e_0.
$$


Thus the annihilating monic polynomial is exactly


$$
\boxed{f=p_\nu+\sum_{i=0}^{\nu-1}q_i p_i.}
$$


The terminal $\ell_{\nu-1}$ is present through $p_\nu$; it has not been omitted.

Let $\mathsf P$ have columns equal to the coefficient vectors of $p_i$. It is upper triangular with diagonal $1$. Therefore


$$
\mathsf K\mathsf P=I,\qquad
\mathsf K=[e_0,\mathscr De_0,\ldots,\mathscr D^{\nu-1}e_0],
$$


and


$$
\boxed{\det\mathsf K=1,\qquad \mathscr D\mathsf K=\mathsf KJ_f.}
$$



The assertion


$$
\mathsf K\equiv I\pmod9
$$


is consistent with the residue of $\ell$: only its last coordinate can be nonzero modulo $9$, and that coordinate does not enter the first $\nu$ Krylov columns.

Consequently


$$
f\equiv q_d-3\binom d{D-1}\pmod9.
$$



### 3.1 Repeated-root factorization

Write


$$
L=3^t,\qquad D=2La_0,\qquad \nu=La_0-1.
$$


The coefficients of $(1-z)^{-D}$ modulo $3$ occur only at powers divisible by $L$. Substitution in the explicit quotient coefficients yields


$$
\boxed{
f(X)\equiv X^{L-1}
\left(
\sum_{r=0}^{a_0-1}
\binom{2a_0+r-1}{r}X^{a_0-1-r}
\right)^L
\pmod3.
}
$$



This is correct. On the depth-$16$ window $L=243$, so a simple-root or unit-discriminant argument is unavailable.

**Verdict:** determinant one, the polynomial $f$, and its repeated-root factorization all withstand audit.

---

## 4. Unit resultant and integral Hankel transfer

Let $\mathsf B_f$ be the coefficient matrix of


$$
\frac{f(X)-f(Y)}{X-Y}.
$$


For the column-companion convention used here,


$$
J\mathsf B_f=\mathsf B_fJ^T,\qquad
\mathsf B_fe_{\nu-1}=e_0,
$$


and


$$
\det\mathsf B_f=(-1)^{\nu(\nu-1)/2}.
$$



Set


$$
r_0=\mathsf K^Tr_{\rm act},\qquad
\mathsf R(X)=\sum_i(\mathsf B_fr_0)_iX^i.
$$


Since $r_0\equiv e_{\nu-1}\pmod3$,


$$
\mathsf R\equiv1\pmod3.
$$


For monic $f$,


$$
\boxed{
\mathfrak u=\operatorname{Res}(f,\mathsf R)
=\det\mathsf R(J)\in1+3\mathbb Z_3.
}
$$



The normalization is therefore legitimate even though $f\bmod3$ has repeated roots.

On the depth-$16$ window, write $S_{\rm act}=-3^{16}\Psi$. The sheared vector


$$
a=\frac{t_{\rm act}-\theta r_{\rm act}}{3^{16}},
\qquad
\theta=\frac{(t_{\rm act})_{\nu-1}}{(r_{\rm act})_{\nu-1}},
$$


is integral: this follows entrywise from the displacement identity and the unit terminal coordinate.

With


$$
\mathsf U=\mathsf R(J)^{-1},\qquad
\mathsf V=\mathsf K\mathsf U,
$$


one has


$$
\mathsf U^Tr_0=e_{\nu-1},
\qquad
\det\mathsf V=\mathfrak u^{-1}.
$$


Thus


$$
\mathsf H=\mathsf V^T\Psi\mathsf V
$$


satisfies


$$
\mathsf HJ-J^T\mathsf H
=e_{\nu-1}b^T-be_{\nu-1}^T.
$$



For $i,j\le\nu-2$, this is precisely


$$
\mathsf H_{i,j+1}=\mathsf H_{i+1,j}.
$$


Hence $\mathsf H$ is integral Hankel.

The last-column equations have the correct sign:


$$
\mu_{i+\nu}+\sum_{k=0}^{\nu-1}f_k\mu_{i+k}=b_i,
\qquad0\le i\le\nu-2.
$$


The final one determines $\mu_{2\nu-2}$. There is no additional actual moment $\mu_{2\nu-1}$.

**Verdict:** the integral Hankel transfer is proved, but only for the complete residual form. It proves no residual determinant is nonzero.

---

## 5. Complete endpoint block and cofactor subtraction

The block


$$
\boxed{
B_{WZ}=T_{WZ}-T_{WW}K_{\rm elim}+K_{\rm elim}\mathscr D
}
$$


is necessary. It is the $W$-component of truncated multiplication on the corrected residual columns.

Evaluation at $-1$ gives


$$
\mathscr D^Te_{\rm act}+B_{WZ}^Tw_-
=-e_{\rm act}-(-1)^{m+1}t_{\rm act}.
$$


After transport,


$$
J^T\varepsilon+\omega
=-\varepsilon-s(\theta e_{\nu-1}+3^{16}b).
$$


Both the interior recurrence and the final companion equation therefore retain $\omega$, including its last coordinate.

The endpoint residues are


$$
\varepsilon_i\equiv(-1)^i\pmod3.
$$


All divisions


$$
\lambda_i=\varepsilon_{i+1}/\varepsilon_i
$$


are consequently unit divisions.

The basis


$$
1,\quad X-\lambda_0,\quad X^2-\lambda_1X,\quad\ldots
$$


has determinant $1$, and its last $\nu-1$ vectors span the endpoint kernel. Its Gram block is


$$
(\mathsf H_\partial)_{ij}
=\mu_{i+j+2}-(\lambda_i+\lambda_j)\mu_{i+j+1}
+\lambda_i\lambda_j\mu_{i+j}.
$$


The adjugate identity, valid also at singular matrices, is


$$
\varepsilon^T\operatorname{adj}(\mathsf H)\varepsilon
=\varepsilon_0^2\det\mathsf H_\partial.
$$



Therefore the complete pair is


$$
\boxed{
\delta_0=\mathfrak u^2\det\mathsf H,
}
$$




$$
\boxed{
\delta_1=\mathfrak u^2
\left(
\varepsilon_0^2\det\mathsf H_\partial
-c_\partial\det\mathsf H
\right),
\qquad c_\partial=3^{16}d_{\rm act}.
}
$$



The subtraction is indispensable. Even though $c_\partial\in3^{15}\mathbb Z_3$, it cannot be discarded in a norm-relative or determinant-relative calculation of unknown depth.

The radical classification in A1 is valid over the fraction field, with the actual matrix and endpoint evaluated there. It must not be confused with a corank statement merely modulo $3$.

---

## 6. Audit of $R$-precision $p+10$ and producer input $p+17$

The sufficient budget is sound. It can be justified without relying on the sharper terminal $p+9$ sub-budget.

Suppose


$$
R'-R\in3^q\mathbb Z_3[y].
$$


The producer changes by $3^{q+6}\Delta R$.

The normalized LOW blocks retain this full depth because their perturbation functionals have an extra factor $3$ at the relevant degree bounds. The same applies to $C/3$. For example, the maximal degree of $\Delta R\,Y_bz_i$ is


$$
(A+1)+m+(d-1)=\frac{3H-1}{2}=r_*.
$$


After division by $y+1$, the degree is below $r_*$, so the unique valuation-zero pole is absent. This explains why normalization by $3$ does not lose a producer digit in this mixed block.

Unit inversion in the normalized LOW/HIGH system then shows that the actual return data, $K_{\rm elim}$, and raw Schur pairings vary by at least $3^{q+6}$.

Taking


$$
q=p+10
$$


therefore gives raw precision $3^{p+16}$. It is sufficient for:

1. the whole sheared numerator divided by $3^{16}$;
2. the whole residual pairing divided by $3^{16}$;
3. the actual terminal and endpoint data at every precision subsequently required.

All remaining transformations use integral operations or demonstrated unit inverses. Thus


$$
\boxed{R\bmod3^{p+10}\text{ suffices for normalized data modulo }3^p.}
$$



Using the accepted producer theorem at its stated seven-digit loss gives


$$
\boxed{\text{producer input precision }3^{p+17}.}
$$



This is a sufficient output-precision theorem, not a theorem that fixed $p$ detects the first nonzero determinant digit. Exact core data must also be supplied at the raw and normalized working precisions used by the implementation.

### A1 remaining bottleneck

The unresolved pair is exactly


$$
\det\mathsf H,\qquad
\varepsilon_0^2\det\mathsf H_\partial-c_\partial\det\mathsf H.
$$


The unit resultant removes a normalization obstacle; it does not determine either member of this pair.

---

# Part II. Audit of A2turn8

## 7. Odd-prime units, binomials, and force guards

### 7.1 The odd-prime sign is correct

For $p=29$,


$$
O_K(N+p^K)=-O_K(N)\pmod{p^K},
$$


because the product of the units modulo an odd prime power is $-1$.

The factorial-unit expansion


$$
U_K(N)=
(-1)^{\sum_{h\ge K}(h-K+1)N_h}
\prod_{\ell\ge0}
O_K\!\left(\sum_{r=0}^{K-1}N_{\ell+r}p^r\right)
$$


has the correct sign exponent. The position-dependent parity is necessary.

For valid $0\le B\le A$,


$$
\binom AB
=p^eU_K(A)U_K(B)^{-1}U_K(A-B)^{-1}\pmod{p^K}
$$


is correct. Invalid binomial ranges must be rejected before this quotient is formed.

Similarly,


$$
\binom{-n}{d}=(-1)^d\binom{n+d-1}{d}
$$


requires the parity of the whole base-$29$ digit sum of $d$, not merely its lowest digit.

### 7.2 Normalized exponential-force truncation

The coefficient formula


$$
a_s(n)=(-1)^s\sum_{v=0}^{\lfloor s/2\rfloor}
2^{-v}\binom n{s-v}\binom{s-v}{v}
$$


is integral at $29$.

The truncation to


$$
0\le s,t<pK
$$


is safe because $s!$ or $t!$ already has valuation at least $K$ outside these ranges. The valid-term restrictions remain


$$
s\le n+i,\qquad b+t\le2n+i-s,
$$


together with the original source limits.

The lower index $b+t$ cannot be replaced by a bounded index.

### 7.3 First-force binomial formula

The identity


$$
1+2z+2z^2=(1+z)^2+z^2
$$


gives


$$
\boxed{
J_i=\sum_{v=0}^{\lfloor n/2\rfloor}
\binom nv\binom{2n-2v+i}{n-2v}.
}
$$


This part is correct.

There is a small implementation detail worth making explicit: the multiplier


$$
\frac{(n+i)!}{n!}=i!\binom{n+i}{i}
$$


is not literally one of the fixed polynomial factors listed in the digit-summation lemma. It is nevertheless covered by a finite extension of that lemma. Modulo $p^K$, it vanishes for $i\ge pK$; for $i<pK$, $i!$ is a precision-sized table entry. Alternatively one can track its clipped factorial valuation and unit part. This closes the stated coverage without a nonunit division.

### 7.4 Complete logarithmic force

The bound


$$
N_{\log}=2F_n-F_b-\lfloor\log_p(2n+b-1)\rfloor
$$


and the implication


$$
N_{\log}\ge b
$$


are valid on the retained family.

Thus the exceptional branch $K>N_{\log}$ implies $b<K$ and $n<2001K$. Exact rational generation of the complete logarithmic force in that branch is bounded in terms of $K$. It is not permissible to use only its homogeneous interior displacement or to suppress its two initial values.

---

## 8. Finite-ring power quotient and interval-product orientation

For $B\in M_3(\mathbb Z/p^K\mathbb Z)$, the image chain stabilizes by step $3K$, the module length. Standard finite-length Fitting theory then splits off the stable image, where $B$ is invertible.

The stable image is a direct summand of a free module over the local ring, hence free of rank at most three. Modulo $p$, the semisimple order divides


$$
\operatorname{lcm}(p-1,p^2-1,p^3-1),
$$


and the unipotent order divides $p$, since $p>3$. Lifting contributes at most $p^{K-1}$.

Accordingly,


$$
\boxed{
B^{q+\Pi_K}=B^q\quad(q\ge3K),\qquad
\Pi_K=731640\,p^K.
}
$$


The theorem is correct. It is an application of established Fitting and finite linear-group facts, not a new general finite-ring theorem.

For the recurrence matrices,


$$
\mathcal P(u,v)=T_v\cdots T_u.
$$


Writing the interval length as $q p^K+r$, the later, incomplete block acts on the left:


$$
\boxed{\mathcal P(u,v)=Q_{a,r}B_a^q.}
$$


This orientation is correct. The phase of the remainder is again $a$ by periodicity.

The convention for a zero-length interval should be explicitly $I$.

---

## 9. Particular source, six Gram entries, and projection

The homogeneous initialization uses only $h_0,h_1$, since $\gamma_1=0$. No artificial negative initial index is needed.

For the particular solution, the source $\mathcal H_\ell$ is injected into the first recurrence coordinate at step $\ell$, and is propagated to $j$ by


$$
T_{j-1}\cdots T_{\ell+1}.
$$


Thus


$$
\boxed{
\tau_j=
\sum_{\ell=1}^{j-1}
e_1^T(T_{j-1}\cdots T_{\ell+1})e_1\,\mathcal H_\ell
}
$$


has the correct endpoint and empty-product convention.

The source formula with $a_s(n+1)$ must remain the complete source inherited from the accepted displacement. It is not interchangeable with the first-force formula using $a_s(n)$.

After expanding the finite inverse into words of length below $K$, the number of summation variables is bounded in terms of $K$. The recurrence weights are finite-state by the preceding power quotient. Consequently adding the coordinate summation $0\le j\le b$ indeed covers all six Gram entries.

The three reconstruction cases are essential:


$$
j=0,\qquad 1\le j<b,\qquad j=b.
$$


In particular,


$$
\mathbf B_b=W_b(b\zeta_{b-1}+e_*^T)
$$


retains the exterior $+1$.

The charges telescope:


$$
\ell^TB_0=\ell^TB_1=0,\qquad \ell^TB_*=W_b.
$$


Hence


$$
G=G^{\rm raw}-\frac{W_b^2}{\mathscr S}e_*e_*^T.
$$


The projection inverse is a unit inverse on the preferred family. This does not make the weighting unimodular or replace the weighted saturated lattice by $\mathbb Z_{29}^3$.

**Verdict:** complete finite-precision Gram evaluability is established. Practical state size and a relation between the two actual output channels are different questions.

---

## 10. Original reachability and true-norm logarithmic protection

The reparameterization is exact:


$$
a=249005515+574312172u,\qquad574312172=28\cdot29^5.
$$


Since


$$
3^{28}\equiv1+15\cdot29\pmod{29^2},
$$


lifting the exponent gives


$$
\boxed{
v_{29}(b(u)-b(v))=6+v_{29}(u-v),\qquad u\ne v.
}
$$



This proves finite-prefix lifting within the indicated cylinder. It does not replace original integer inputs by arbitrary infinite digit strings, prove fixed-prefix dependence of the Gram output, or preserve an independent real window automatically.

For logarithmic protection, let


$$
P=p^cx,\qquad \nu=v_p(x^Tx).
$$


Integral inversion and reconstruction give


$$
Y-Y^{(e)}\in p^{N_{\log}}\mathbb Z_p^{b+1}.
$$


Therefore


$$
v_p(M-M^{(e)})\ge c+N_{\log}-3,
$$


and, for the actual nonzero norm $D=P^TP$,


$$
\boxed{
v_p\!\left(\frac MD-\frac{M^{(e)}}D\right)
\ge N_{\log}-c-3-\nu.
}
$$


The threshold


$$
N_{\log}\ge c+4+\nu
$$


is correct for agreement modulo $p$.

This explicitly pays primitive norm cancellation. Column content alone is insufficient.

### A2 remaining bottleneck

The transfer does not prove


$$
\boxed{
\mathcal C-29\rho_n\mathcal N\in29^2\mathcal N\mathbb Z_{29}.
}
$$


The normalization certificate at


$$
d=v_{29}(\mathcal N),\qquad K=d+2
$$


is correct. A zero residue for $\mathcal N$ modulo $29^K$ gives only a lower bound on $d$, not a relative-output certificate.

---

# Part III. Audit of A5turn17

## 11. Compressed interior divided-power inverse

The polynomial realizations are correct:


$$
U^{-T}Z=P_b((1+x)^{-n}Z),\qquad
L^{-T}Z=Z(x-1).
$$


The two truncated multiplications may be combined; translation may not be moved through truncation.

For divided derivatives,


$$
\partial^{[s]}\partial^{[t]}
=\binom{s+t}{s}\partial^{[s+t]}.
$$


Thus the inverse coefficients satisfy


$$
c_0=1,\qquad
c_k=-\sum_{s=1}^k\binom ks\lambda_s c_{k-s}.
$$


Given the accepted filtration


$$
v_2(\lambda_s)\ge\lceil s/4\rceil,
$$


induction proves


$$
v_2(c_k)\ge\lceil k/4\rceil.
$$


Consequently


$$
\boxed{
(H^T)^{-1}\equiv
\sum_{k=0}^{4(M-1)}c_k\partial^{[k]}\pmod{2^M}.
}
$$



The $O(M^2)$ operation count is correct **for computing the inverse coefficients once the symbol coefficients are supplied**. It does not include an unproved cost for generating those symbol coefficients, evaluating the complete adjoint, or evaluating its scalar outputs.

No factorial division or precision loss occurs in this interior inversion.

---

## 12. Endpoint commutator and translation obstruction

For $s<b$, the displayed commutator is directly correct. To cover every $s\ge1$ as a literal polynomial identity, use


$$
\boxed{
P_b\partial^{[s]}F-\partial^{[s]}P_bF
=
\sum_{r=\max(0,s-b)}^{s-1}
\binom{b+r}{s}f_{b+r}x^{b+r-s}.
}
$$


The source’s formula with lower limit $0$ has the same intended value if terms with $\binom{b+r}{s}=0$ are omitted before writing their possibly negative powers. The corrected lower limit removes that notational ambiguity.

After translation, these upper-boundary monomials become dense binomial polynomials. Therefore:

> Bounded boundary rank survives, but bounded coordinate support does not.

The jet obstruction is rigorous:


$$
x^d\equiv0\pmod{x^d},
\qquad
(x-1)^d\not\equiv0\pmod{x^d}.
$$


It already holds modulo $2$. Thus translation is not an endomorphism of the ordinary jet quotient.

This disproves that particular compression route, not every possible finite-state or moment compression.

---

## 13. Kernel closure and norm-sensitive precision

The three kernel operations have the correct adjoint orientations:


$$
\kappa(k)\mapsto\mathbf1_{k\ge s}\binom ks\kappa(k-s),
$$




$$
\kappa(i)\mapsto\sum_{j=i}^{b-1}\kappa(j)\binom{-n}{j-i},
$$




$$
\kappa(j)\mapsto\sum_{i=0}^{j}\kappa(i)(-1)^{j-i}\binom ji.
$$



Their formulas are not, by themselves, closure in a bounded module. In particular, naming each transformed finite sum as a new kernel indefinitely would not prove a compression theorem.

The outstanding closure obligation must include:

- actual reconstruction weights and adjacent-coordinate products;
- the genuine high-index binomials;
- symbolic upper-boundary terms;
- the separate reconstructed endpoint;
- the full logarithmic force when its omission budget fails.

For


$$
D_{\rm raw}=\mathsf a^T\mathsf a,\qquad
E_{\rm raw}=\mathsf a^T\mathsf b,
$$


with valuations $d,e$, the quotient is


$$
H/N=E_{\rm raw}/(2D_{\rm raw}).
$$


The sufficient common precision


$$
\boxed{
M\ge\max\{s+d+1,\ s+2d+1-e\},\qquad M>d,e
}
$$


is correct.

The Turn 19 distinction remains necessary:

- squaring an approximate column of error depth $T$ gives norm-error depth at least
  

$$
\min(T+a+1,2T);
$$


- a one-sided adjoint contraction using the exact first force gives only the general bound $T+a$.

The interior operator theorem does not certify the unknown $d,e$.

---

# Part IV. Corrected complete-endpoint consequence

## 14. Retraction of the deficient growth formulation

My Turn 19 wording suggested controlling the $A,B$ in the primitive denominator by analyzing the endpoints obtained from $C^{-1}z$, followed by their first-column common content.

That is insufficient.

Let the least actual common clearer produce the complete integer endpoint rows


$$
(U_0,V_0),\qquad(U_3,V_3).
$$


The second components use the **complete** force, including logarithmic restoration and the exterior $+1$.

Define


$$
g_0=\gcd(|U_0|,|V_0|),\qquad
g_3=\gcd(|U_3|,|V_3|),
$$


then


$$
u_0=U_0/g_0,\qquad u_3=U_3/g_3,
$$


and only then


$$
h=\gcd(|u_0|,|u_3|),\qquad A=u_0/h,\qquad B=u_3/h.
$$



Thus


$$
\boxed{
A=\frac{U_0}{g_0h},\qquad B=\frac{U_3}{g_3h}.
}
$$


Both row gcds depend on the complete second force.

The coordinator certificate implements this normalization correctly.

---

## 15. New exact row-normalized endpoint law

Assume $U_0U_3\ne0$. For any prime $\ell$, write


$$
u_i^\ell=v_\ell(U_i),\qquad v_i^\ell=v_\ell(V_i),
$$


with the usual convention $v_\ell(0)=+\infty$. Then


$$
v_\ell(g_i)=\min(u_i^\ell,v_i^\ell).
$$


After row primitivization, the first-component valuation is


$$
u_i^\ell-v_\ell(g_i)=\max(u_i^\ell-v_i^\ell,0),
$$


with value $0$ when $V_i=0$.

Removing the common $h$ leaves one of $A,B$ an $\ell$-adic unit. Hence:

### Theorem 15.1 — Actual complete-row relative law


$$
\boxed{
v_\ell(|AB|)
=
\left|
\bigl(u_0^\ell-v_\ell(g_0)\bigr)
-
\bigl(u_3^\ell-v_\ell(g_3)\bigr)
\right|.
}
$$


Equivalently, when both second components are nonzero,


$$
\boxed{
v_\ell(|AB|)
=
\left|
(u_0^\ell-v_0^\ell)_+
-
(u_3^\ell-v_3^\ell)_+
\right|.
}
$$



This identity is exact at every prime. It uses the complete rows, not merely the first-column ratio.

### 15.1 Quantified distortion from the raw first-column ratio

Let


$$
H_0=\gcd(|U_0|,|U_3|),\qquad
A_{\rm raw}=U_0/H_0,\quad B_{\rm raw}=U_3/H_0,
$$


and define the row-gcd imbalance


$$
R_g=\frac{g_0g_3}{\gcd(g_0,g_3)^2}.
$$


For every prime,


$$
v_\ell(|A_{\rm raw}B_{\rm raw}|)
=|u_0^\ell-u_3^\ell|,
$$


whereas


$$
v_\ell(R_g)=|v_\ell(g_0)-v_\ell(g_3)|.
$$


The reverse triangle inequality gives


$$
\boxed{
\left|
v_\ell(|AB|)
-v_\ell(|A_{\rm raw}B_{\rm raw}|)
\right|
\le v_\ell(R_g).
}
$$



For any fixed selected-prime set $\mathcal P$,


$$
\boxed{
\left|
\log|AB|_{\mathcal P^c}
-\log|A_{\rm raw}B_{\rm raw}|_{\mathcal P^c}
\right|
\le\log(R_g)_{\mathcal P^c}.
}
$$



This is a usable corrected growth bridge: raw first-column growth becomes relevant only after paying the **actual complete-row gcd imbalance**.

Without such payment, even large raw endpoint height can disappear. For instance, the nondegenerate integer rows


$$
(N,N),\qquad(1,0)
$$


have raw first-column ratio $N$, but row primitivization gives first components $1,1$, hence $A=B=1$. This is an algebraic illustration, not an original-family counterexample.

---

## 16. Consequence for the full primitive denominator

Retain the supplied exact formula


$$
q_\lambda=\frac{kh|AB|}{F_{\rm gcd}G H_{\rm gcd}},
$$


where


$$
F_{\rm gcd}=\gcd(|A|,|a|)\gcd(|B|,|a-k|),
$$




$$
G\mid k,\qquad H_{\rm gcd}\mid h.
$$


Thus primewise


$$
v_\ell(q_\lambda)\ge
v_\ell(|AB|)-v_\ell(F_{\rm gcd}).
$$



When $a(a-k)\ne0$,


$$
v_\ell(F_{\rm gcd})\le v_\ell(a)+v_\ell(a-k).
$$


Combining with Theorem 15.1 gives the actual-row lower bound


$$
\boxed{
v_\ell(q_\lambda)\ge
\max\!\left\{
0,\,
\left|
u_0^\ell-u_3^\ell-v_\ell(g_0)+v_\ell(g_3)
\right|
-v_\ell(a)-v_\ell(a-k)
\right\}.
}
$$



A weaker but convenient product consequence is


$$
\boxed{
(q_\lambda)_{\mathcal P^c}
\ge
\frac{
|A_{\rm raw}B_{\rm raw}|_{\mathcal P^c}
}{
(R_g)_{\mathcal P^c}\,|a(a-k)|_{\mathcal P^c}
}.
}
$$



This deduction preserves all gcd factors. It does not prove that its right side grows on an original family.

### Concrete follow-on lemma

The corrected growth obligation is:

> On one specified original smooth family, estimate the fully normalized quantity
> 

$$
> \log|AB|_{\mathcal P^c},
>
$$


> or prove a useful lower bound for
> 

$$
> \log|A_{\rm raw}B_{\rm raw}|_{\mathcal P^c}
> -
> \log(R_g)_{\mathcal P^c},
>
$$


> with $g_0,g_3$ formed from the complete second-force endpoint rows.

A proof about $C^{-1}z$ alone does not establish this lemma.

---

# Part V. Receipts, bounded checks, and final proof obligations

## 17. Scope of the attached receipts

### 17.1 Terminal companion receipt

The supplied program explicitly:

1. computes complete exponential and logarithmic contact forces;
2. reconstructs both complete endpoint rows;
3. uses the archived least clearer;
4. divides each row by its own gcd;
5. removes the common first-component factor;
6. compares the resulting $A,B$ with the archived values.

That is the correct normalization sequence.

The reported row gcds


$$
(2400,1),\quad(93000,1),\quad(12799500,8),\quad(112547400,943)
$$


underscore why the second force matters.

The adjacent full producers in this program reach source index $2n+6$, as the receipt records. Thus the maximum for $n=210$ is $426$. My earlier proposed bound $424$ did not cover this program’s complete adjacent-producer construction.

The logarithmic depths are consistent with being at least $K_\star$; several exceed that bound. The floating-point logarithmic summaries are diagnostic summaries of finite integer quantities, not rigorous infinite growth estimates.

### 17.2 Binary adjoint receipt

The receipt reports agreement of the complete finite factorization, adjoint residual, and both scalar contractions for the two auxiliary systems.

Its raw values imply exactly


$$
H/N\equiv417\pmod{512}\quad(b=81),
$$


and


$$
H/N\equiv17\pmod{64}\quad(b=209).
$$


The true endpoint contribution happens to vanish at the reported modulus in both cases. That finite zero does not authorize removing the endpoint from a symbolic or higher-precision formula.

Neither case belongs to the original exponential-index Gram family.

---

## 18. Bounded exact arithmetic for personal inspection

No additional finite computation is needed to prove the algebraic identities above. The following calculations would inspect implementations at explicitly bounded scopes.

### A. Complete-row normalization audit

Use the four archived endpoint cases $n=15,30,105,210$, including their least clearers and complete $U,V$ arrays.

Compute:


$$
g_0,g_3,h,A,B,\quad A_{\rm raw},B_{\rm raw},\quad R_g.
$$



**Expected verifiable output:**

- exact reproduction of archived $A,B$;
- exact reproduction of the four row-gcd pairs;
- verification, for every prime dividing the finite integers involved, of Theorem 15.1;
- verification of the row-gcd distortion inequality;
- no claim of asymptotic growth.

### B. A1 synthetic structured-algebra audit

Use the order-three input stated in A1turn11:


$$
f=X^3+17X^2+126X+585,\qquad \mathsf R=1+3X,
$$




$$
\mathsf H=
\begin{pmatrix}
1&2&5\\
2&5&14\\
5&14&42
\end{pmatrix},
\qquad \varepsilon=(1,-1,1)^T.
$$



**Expected output:**


$$
\det\mathsf K=1,\qquad
\operatorname{Res}(f,1+3X)=-14711,
$$




$$
\det\mathsf H=1,\qquad
\det\mathsf H_\partial=74,
$$


and the complete cofactor expression, including subtraction,


$$
14711^2(74-3^{15}).
$$



This tests algebra and signs, not original-family residual divisibility.

### C. A2 digit and propagator checks

Use $p=29$, $K=1,2$, with the finite ranges and recurrence phases specified in A2.

**Expected output:** zero discrepancies between exact binomials and the sign-sensitive unit formula; zero matrices for interval-product comparisons and the power-quotient identity.

For the auxiliary $n=29,b=4,K=2$ Gram test, preserve the actual projection scalar and complete logarithmic branch.

### D. A5 interior and endpoint operator check

Use the smallest original parameters


$$
b=150094635296999121,\qquad
n=600678730458590482242,
$$


with $M=20$, $m=76$, and the complete symbol coefficients $\lambda_0,\ldots,\lambda_{76}$.

**Expected output:**

- zero inverse residuals through order $152$;
- the stated coefficient-depth bounds;
- zero endpoint-commutator residuals using the corrected finite range;
- no length-$b$ vector allocation;
- no claim that this computes the original norm or mixed scalar.

The first closure gate must output actual finite reduction identities and module dimensions. An unevaluated transformed kernel is not a completed reduction.

---

## 19. Primitive denominators and whole evaluated errors

The local audits leave the global normalization obligations intact.

### A1

With the least actual clearer $\ell_{\rm clr}$,


$$
g_\ell=\gcd\!\left(
|\ell_{\rm clr}^{m+1}\beta_0|,
|\ell_{\rm clr}^{m+1}\beta_1|
\right),
$$


and the primitive denominator is obtained from the complete integer pair. The evaluated error remains


$$
qS-p=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{g_\ell}
\det H_{\rm complete}.
$$


The $3$-adic unit resultant does not determine this all-prime gcd or whole determinant error.

### A2 and A5

Retain


$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B,
$$


with the least actual two-column clearer and primitive multiplier $d_B^2/g_B$.

The relevant error is


$$
\boxed{q_nS-p_n=-q_n\epsilon_n.}
$$


A local norm-relative law would still not supply an all-prime bound on $q_n$.

### Complete endpoint construction

Retain


$$
q_\lambda=\frac{kh|AB|}{F_{\rm gcd}G H_{\rm gcd}},
$$


and


$$
\boxed{
q_\lambda S-p_\lambda
=q_\lambda e_3\alpha_{n,2}(\lambda-\Lambda_{n,2}).
}
$$


Nonvanishing of an exponential Wronskian or transverse displacement is not proof that this whole evaluated expression is nonzero.

---

## 20. Final proof-status ledger

| Item | Audit status |
|---|---|
| A1 actual terminal-generator residue | Valid from complete functional and accepted corrected columns |
| A1 determinant-one Krylov basis | Proved |
| A1 companion polynomial and final equation | Correct |
| A1 repeated-root factorization | Correct; blocks a simple-root route |
| A1 actual unit resultant | Proved |
| A1 integral Hankel transfer | Proved on the depth-$16$ window |
| A1 complete $B_{WZ}$ endpoint transport | Correct and indispensable |
| A1 endpoint-kernel cofactor with subtraction | Correct, including singular cases |
| A1 $R$-precision $p+10$, input $p+17$ | Sufficient at accepted producer/block scope |
| A1 residual nonvanishing and relative valuation | Open |
| A2 odd-prime signs and guarded binomial evaluation | Correct |
| A2 first-force formula | Correct; factorial multiplier coverage made explicit |
| A2 Fitting quotient $(3K,\Pi_K)$ | Correct application of established theory |
| A2 interval-product orientation and particular source propagation | Correct |
| A2 complete six-entry Gram evaluation and projection | Valid finite-precision construction |
| A2 original finite-prefix reachability | Correct at its finite-prefix scope |
| A2 true-norm logarithmic protection | Correct |
| A2 actual norm-relative output law | Open |
| A5 compressed interior divided-power inverse | Correct |
| A5 finite-endpoint commutator | Correct with explicit zero-term/index convention |
| A5 ordinary jet quotient for complete translation | Disproved |
| A5 feasible complete kernel closure | Open |
| Complete-row endpoint normalization | Corrected here |
| Exact actual-row valuation and distortion law | Proved here |
| Infinite fully normalized endpoint-growth theorem | Open |
| Full primitive-denominator/whole-error comparison | Open |

## Conclusion

The new rigorous consequence of this audit is the complete-row endpoint law


$$
v_\ell(|AB|)
=
\left|
v_\ell(U_0)-v_\ell(U_3)-v_\ell(g_0)+v_\ell(g_3)
\right|,
$$


together with its exact distortion bound and its full-gcd primitive-denominator consequence. This repairs the previous growth formulation without substituting raw first-column height for the actual normalized endpoint factor.

The remaining mathematical bottlenecks are precise:

1. **A1:** determine the actual Hankel determinant and complete endpoint-minor difference, including nonvanishing and relative valuation.
2. **A2:** prove or refute the actual norm-relative output relation at the first nonzero norm digit.
3. **A5:** close and evaluate the complete boundary-aware moment transforms at norm-sensitive precision.
4. **Endpoint route:** control the actual complete-row gcd distortion, not merely the raw first-column ratio.
5. **Every route:** retain the least clearer, final all-prime gcd, actual primitive denominator, and whole nonzero evaluated error on the same original indices.

The supplied finite PASS receipts validate only their stated finite systems. They establish no infinite growth, alignment, or irrationality law.



$$
\boxed{\text{An unconditional proof or disproof of the irrationality of }e+\pi
\text{ remains unresolved.}}
$$


