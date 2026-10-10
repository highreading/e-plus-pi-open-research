> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the exact factorial-coordinate differential identity

Date: 2026-09-13. Reviewer: audit_sources.

**PASS.** The complete source
raw_factorial_b_exact_differential_identity.md is correct, including
every coefficient, its mod-$p$ transfer, and the actual exponential
endpoint. No correction is required.

I independently reconstructed the identity before reading the saved
source; that derivation is also in Sections 6--7 of
raw_positive_residue_schur_and_endpoint_transfer.md.
Both derivations use the original reviewed reconstruction


$$
S=(1+t^2)^nU,\quad W=t^n(t-1)^nV,\quad
 w_{n+r}=S_{n+r}/r!,\quad U_j=(n+j)!b_j.
$$


For $0\le r\le2n$, the coefficient of $t^r$ in
$(1+\partial_t^2)^n[t^nb(t)]$ is


$$
\frac1{r!}\sum_{h=0}^n\binom nh U_{r-n+2h}.
$$


Replacing $h$ by $n-h$ gives $S_{n+r}/r!=w_{n+r}$,
the coefficient of $W/t^n$. Out-of-range $U$ coefficients
are zero; no low coefficient has been dropped. Thus


$$
(t-1)^nV=(1+\partial_t^2)^n[t^nb]
$$


is an exact integer-polynomial identity. It does not equate the two
distinct raw Rodrigues derivatives.

Over $\mathbb F_p[t]$, $\partial_t^p=0$ holds on all polynomial
degrees, not only on degrees below $p$. Hence
$(1+\partial_t^2)^{mp+k}=(1+\partial_t^2)^k$.
The factor $[t(t-1)]^{mp}$ has derivative zero. Applying the
identity to a $p$-integral scalar congruence
$b_n=c(t-1)^{n-k}b_k$ therefore gives


$$
(t-1)^nV_n=c\,t^{n-k}(t-1)^nV_k.
$$


Cancelling the nonzero polynomial in the integral domain
$\mathbb F_p[t]$ is valid even though it vanishes at $t=1$.
This proves the full $V$-polynomial congruence.

For the endpoint transfer, with $r=n-k+s$, the integer border
has terms $\binom{n+j}j(n+r)_{\underline j}$.
All $j\ge p$ terms vanish modulo $p$. For $j<p$, reduction
of the first factor via its product formula is valid because $j!$
is a unit; it gives $\binom{k+j}j$, including the case where
that binomial itself vanishes modulo $p$. The falling factorial
becomes $(k+s)_{\underline j}$. Under $p>2k$, precisely the
terms through $j=k+s<p$ remain, producing the actual small
border $D_{k,s}$. Thus


$$
\widehat P_{e,n}(1)\equiv c\,\widehat P_{e,k}(1)\pmod p
$$


uses the correct common cofactor orientation and no factorial loss.

The source correctly keeps the prerequisite $b$-congruence separate;
it is supplied by the same-size Schur and Lucas argument in the
positive-residue note. No lift beyond modulo $p$, arbitrary-model
comparison, or unit assertion about an exceptional seed is inferred.

As a small exact normalization check using the already identified
degree-two data, the Appell values $\mathcal A_2(1)=5$,
$\mathcal A_3(1)=13$, $\mathcal A_4(1)=49$ give


$$
M_D^{[2]}(1)=\frac12
 \det\begin{pmatrix}5&2&2\\13&15&6\\49&52&60\end{pmatrix}=925.
$$


For $V_2=940-64t+49t^2$, the exact borders are
$(D_{2,0},D_{2,1},D_{2,2})=(19,106,685)$, so


$$
V_2(1)=925,\qquad
 \widehat P_{e,2}(1)=940\cdot19-64\cdot106+49\cdot685=44641.
$$


This is a bounded arithmetic check of a fixed existing seed, not a
new large-degree approximant solve. The residue-two criterion can
therefore be stated without a primality assumption as
$p>4,\ p\nmid925\cdot44641$.
